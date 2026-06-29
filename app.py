"""
Programming Visualization Platform
Main Flask Application - Public Access (No Login Required)
Developed by issu321
"""

import os
import sys
import json
import uuid
import logging
import webbrowser
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify, send_file
from werkzeug.utils import secure_filename

# Setup logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

logger.info("[APP] Starting Programming Visualization Platform...")

# Import modules with error handling
try:
    from database import init_db, save_analysis, get_user_history, get_analysis_by_id, get_stats
    from database import save_uploaded_file, get_user_files, save_report, get_user_reports
    logger.info("[APP] Database module loaded")
except Exception as e:
    logger.error(f"[APP] Failed to load database module: {e}")
    raise

try:
    from analyzers import analyze_code, detect_language
    logger.info("[APP] Analyzers module loaded")
except Exception as e:
    logger.error(f"[APP] Failed to load analyzers module: {e}")
    raise

try:
    from visualizer import CodeVisualizer, generate_report
    logger.info("[APP] Visualizer module loaded")
except Exception as e:
    logger.error(f"[APP] Failed to load visualizer module: {e}")
    raise

# Flask app configuration
app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "programming-visualization-secret-key-2024")
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024  # 16MB max file size

# Directories
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")
REPORTS_FOLDER = os.path.join(BASE_DIR, "reports")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(REPORTS_FOLDER, exist_ok=True)
os.makedirs(os.path.join(BASE_DIR, "database"), exist_ok=True)

ALLOWED_EXTENSIONS = {"py", "java", "c", "cpp", "cc", "cxx", "h", "hpp"}

# Anonymous user ID for all public operations
ANONYMOUS_USER_ID = 1


# ==================== DUMMY CURRENT_USER FOR TEMPLATES ====================
# Since this app has no login system, we inject a fake current_user object
# so templates that reference {{ current_user.username }} won't crash.
class AnonymousUser:
    username = "Guest"
    is_authenticated = False
    is_active = True
    is_anonymous = True
    id = ANONYMOUS_USER_ID

    def get_id(self):
        return ANONYMOUS_USER_ID


anonymous_user = AnonymousUser()
# ==========================================================================


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.context_processor
def inject_globals():
    return {
        "theme": session.get("theme", "dark"),
        "year": datetime.now().year,
        "current_user": anonymous_user  # <-- FIX: inject dummy user
    }


# ==================== HOME & STATIC PAGES ====================

@app.route("/")
def home():
    try:
        stats = get_stats()
    except Exception as e:
        logger.error(f"[HOME] Stats error: {e}")
        stats = {"total_users": 0, "total_analyses": 0, "total_files": 0, "language_stats": {}}
    return render_template("home.html", stats=stats)


@app.route("/features")
def features():
    return render_template("features.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


# ==================== DASHBOARD (PUBLIC) ====================

@app.route("/dashboard")
def dashboard():
    history = get_user_history()
    files = get_user_files()
    reports = get_user_reports()

    lang_counts = {}
    for h in history:
        lang = h.get("language", "unknown")
        lang_counts[lang] = lang_counts.get(lang, 0) + 1

    return render_template("dashboard.html",
                         history=history,
                         files=files,
                         reports=reports,
                         lang_counts=lang_counts)


# ==================== ANALYZER (PUBLIC) ====================

@app.route("/analyzer")
def analyzer():
    return render_template("analyzer.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    logger.info("[ANALYZE] Request received")

    try:
        code = ""
        filename = "untitled"
        language = ""

        # ===== HANDLE FILE UPLOAD =====
        if "file" in request.files:
            uploaded_file = request.files["file"]
            logger.info(f"[ANALYZE] File field present, filename: '{uploaded_file.filename}'")

            if uploaded_file and uploaded_file.filename and uploaded_file.filename.strip():
                if allowed_file(uploaded_file.filename):
                    try:
                        filename = secure_filename(uploaded_file.filename)
                        unique_id = str(uuid.uuid4())
                        filepath = os.path.join(UPLOAD_FOLDER, f"{unique_id}_{filename}")

                        logger.info(f"[ANALYZE] Saving to: {filepath}")
                        uploaded_file.save(filepath)
                        logger.info(f"[ANALYZE] File saved, size: {os.path.getsize(filepath)} bytes")

                        # Read file content
                        try:
                            with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                                code = f.read()
                        except Exception as read_err:
                            logger.error(f"[ANALYZE] Read error: {read_err}")
                            flash(f"Error reading file: {str(read_err)}", "danger")
                            return redirect(url_for("analyzer"))

                        if not code.strip():
                            flash("Uploaded file is empty.", "warning")
                            os.remove(filepath)
                            return redirect(url_for("analyzer"))

                        language = detect_language(code, filename)
                        file_size = os.path.getsize(filepath)
                        save_uploaded_file(ANONYMOUS_USER_ID, filename, filepath, language, file_size)
                        logger.info(f"[ANALYZE] File processed: {filename}, lang: {language}")

                    except Exception as upload_err:
                        logger.error(f"[ANALYZE] Upload failed: {upload_err}")
                        flash(f"Upload failed: {str(upload_err)}", "danger")
                        return redirect(url_for("analyzer"))
                else:
                    flash("Invalid file type. Supported: .py, .java", "danger")
                    return redirect(url_for("analyzer"))

        # ===== HANDLE PASTED CODE =====
        if not code and request.form.get("code", "").strip():
            code = request.form.get("code")
            filename = request.form.get("filename", "").strip() or "pasted_code.py"
            if not any(filename.endswith(ext) for ext in [".py", ".java", ".c", ".cpp", ".h", ".hpp"]):
                filename += ".py"
            language = detect_language(code, filename)
            logger.info(f"[ANALYZE] Pasted code, filename: {filename}, lang: {language}")

        if not code or not code.strip():
            flash("Please provide code or upload a file.", "warning")
            return redirect(url_for("analyzer"))

        # ===== PERFORM ANALYSIS =====
        logger.info(f"[ANALYZE] Starting analysis: {len(code)} chars")
        try:
            result = analyze_code(code, filename)
            result["raw_code"] = code
            logger.info(f"[ANALYZE] Analysis complete: {result['detected_language']}, {len(result.get('functions', []))} funcs")
        except Exception as analysis_err:
            logger.error(f"[ANALYZE] Analysis failed: {analysis_err}")
            flash(f"Analysis failed: {str(analysis_err)}", "danger")
            return redirect(url_for("analyzer"))

        # ===== GENERATE VISUALIZATIONS =====
        logger.info("[ANALYZE] Generating visualizations...")
        try:
            visualizer = CodeVisualizer(result)
            visualizations = visualizer.generate_all_visualizations()
            logger.info(f"[ANALYZE] Visualizations: {list(visualizations.keys())}")
        except Exception as viz_err:
            logger.error(f"[ANALYZE] Visualization error: {viz_err}")
            visualizations = {}

        # ===== SAVE TO DATABASE =====
        logger.info("[ANALYZE] Saving to database...")
        try:
            analysis_id = save_analysis(
                ANONYMOUS_USER_ID, filename, language, code[:5000], result, visualizations
            )
            session["last_analysis_id"] = analysis_id
            logger.info(f"[ANALYZE] Saved to DB: ID {analysis_id}")
        except Exception as db_err:
            logger.error(f"[ANALYZE] Database save failed: {db_err}")
            flash(f"Could not save analysis: {str(db_err)}", "warning")
            analysis_id = 0

        flash("Analysis completed successfully!", "success")
        return redirect(url_for("visualization", analysis_id=analysis_id))

    except Exception as e:
        logger.error(f"[ANALYZE] UNHANDLED ERROR: {e}")
        import traceback
        logger.error(traceback.format_exc())
        flash(f"Server error: {str(e)}", "danger")
        return redirect(url_for("analyzer"))


# ==================== VISUALIZATION (PUBLIC) ====================

@app.route("/visualization/<int:analysis_id>")
def visualization(analysis_id):
    try:
        analysis = get_analysis_by_id(analysis_id)
        if not analysis:
            flash("Analysis not found.", "danger")
            return redirect(url_for("dashboard"))

        result = analysis["analysis_result"]
        visualizations = analysis["visualizations"]

        return render_template("visualization.html",
                             analysis=analysis,
                             result=result,
                             visualizations=visualizations)
    except Exception as e:
        logger.error(f"[VISUALIZATION] Error: {e}")
        flash("Error loading visualization.", "danger")
        return redirect(url_for("dashboard"))


# ==================== REPORTS (PUBLIC) ====================

@app.route("/reports")
def reports():
    user_reports = get_user_reports()
    history = get_user_history()
    return render_template("reports.html", reports=user_reports, history=history)


@app.route("/generate_report/<int:analysis_id>/<report_type>")
def generate_report_route(analysis_id, report_type):
    try:
        analysis = get_analysis_by_id(analysis_id)
        if not analysis:
            flash("Analysis not found.", "danger")
            return redirect(url_for("reports"))

        result = analysis["analysis_result"]

        content = generate_report(result, report_type)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"report_{analysis_id}_{timestamp}.{report_type}"
        filepath = os.path.join(REPORTS_FOLDER, filename)

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)

        save_report(ANONYMOUS_USER_ID, analysis_id, report_type, filepath)

        if report_type == "json":
            return jsonify(json.loads(content))
        elif report_type == "html":
            return content
        else:
            return send_file(filepath, as_attachment=True, download_name=filename)
    except Exception as e:
        logger.error(f"[REPORT] Error: {e}")
        flash("Error generating report.", "danger")
        return redirect(url_for("reports"))


# ==================== DATABASE / STATS (PUBLIC) ====================

@app.route("/database")
def database_view():
    stats = get_stats()
    history = get_user_history()
    files = get_user_files()

    return render_template("database.html",
                         stats=stats,
                         history=history,
                         files=files)


# ==================== API ENDPOINTS (PUBLIC) ====================

@app.route("/api/analyze", methods=["POST"])
def api_analyze():
    try:
        data = request.get_json()
        if not data or "code" not in data:
            return jsonify({"error": "Code is required"}), 400

        code = data["code"]
        filename = data.get("filename", "api_code.py")

        result = analyze_code(code, filename)
        result["raw_code"] = code

        visualizer = CodeVisualizer(result)
        visualizations = visualizer.generate_all_visualizations()

        return jsonify({
            "success": True,
            "analysis": result,
            "visualizations": visualizations
        })
    except Exception as e:
        logger.error(f"[API] Error: {e}")
        return jsonify({"error": str(e)}), 500


@app.route("/api/stats")
def api_stats():
    try:
        return jsonify(get_stats())
    except Exception as e:
        logger.error(f"[API STATS] Error: {e}")
        return jsonify({"error": str(e)}), 500


@app.route("/api/theme", methods=["POST"])
def api_theme():
    try:
        data = request.get_json()
        theme = data.get("theme", "dark")
        session["theme"] = theme
        return jsonify({"success": True, "theme": theme})
    except Exception as e:
        logger.error(f"[API THEME] Error: {e}")
        return jsonify({"error": str(e)}), 500


# ==================== ERROR HANDLERS ====================

@app.errorhandler(404)
def not_found(e):
    return render_template("home.html", error="Page not found"), 404


@app.errorhandler(500)
def server_error(e):
    logger.error(f"[500] Server error: {e}")
    return render_template("home.html", error="Server error occurred"), 500


# ==================== MAIN ====================

if __name__ == "__main__":
    try:
        init_db()
        logger.info("[APP] Database initialized.")
    except Exception as e:
        logger.error(f"[APP] Database init failed: {e}")

    # Use PORT env var (Hugging Face Spaces uses 7860, local dev uses 5000)
    port = int(os.environ.get("PORT", 5000))
    host = os.environ.get("HOST", "0.0.0.0")

    logger.info(f"[APP] Starting server on {host}:{port}")

    # Auto-open browser only when running locally (not in Docker/HF Spaces)
    if not os.environ.get("DOCKER_ENV") and not os.path.exists("/.dockerenv"):
        url = f"http://127.0.0.1:{port}"
        try:
            webbrowser.open(url)
            logger.info(f"[APP] Auto-opened browser: {url}")
        except Exception as e:
            logger.warning(f"[APP] Could not auto-open browser: {e}")

    app.run(host=host, port=port, debug=True, use_reloader=False)
else:
    try:
        init_db()
        logger.info("[APP] Database initialized (non-main).")
    except Exception as e:
        logger.error(f"[APP] Database init failed: {e}")