"""
Code Analysis Engine for Programming Visualization Platform
Supports Python, Java, C, and C++ with real AST parsing.
"""

import ast
import re
import json
from typing import Dict, List, Any, Optional

# Language detection patterns
LANGUAGE_PATTERNS = {
    "python": {
        "extensions": [".py"],
        "patterns": [
            r"^\s*(def\s+\w+|class\s+\w+|import\s+\w+|from\s+\w+\s+import|if\s+__name__\s*==\s*[\"']__main__[\"'])",
            r"print\s*\(",
            r":\s*$",
        ]
    },
    "java": {
        "extensions": [".java"],
        "patterns": [
            r"public\s+(class|interface|enum)\s+\w+",
            r"import\s+java\.",
            r"System\.out\.print",
            r"\bString\s+\w+",
        ]
    },
    "c": {
        "extensions": [".c", ".h"],
        "patterns": [
            r"#include\s*<",
            r"\b(int|void|char|float|double)\s+\w+\s*\(",
            r"printf\s*\(",
            r"struct\s+\w+",
        ]
    },
    "cpp": {
        "extensions": [".cpp", ".cc", ".cxx", ".hpp"],
        "patterns": [
            r"#include\s*<",
            r"\b(cout|cin|endl)\b",
            r"namespace\s+\w+",
            r"class\s+\w+.*\{",
            r"std::",
        ]
    }
}


def detect_language(code: str, filename: str = "") -> str:
    """Detect programming language from code content and filename."""
    if filename:
        ext = filename.lower()
        for lang, info in LANGUAGE_PATTERNS.items():
            for extension in info["extensions"]:
                if ext.endswith(extension):
                    return lang

    scores = {lang: 0 for lang in LANGUAGE_PATTERNS}
    for lang, info in LANGUAGE_PATTERNS.items():
        for pattern in info["patterns"]:
            matches = len(re.findall(pattern, code, re.MULTILINE))
            scores[lang] += matches

    if re.search(r"^\s+\w+.*:\s*$", code, re.MULTILINE):
        scores["python"] += 2

    if re.search(r"\b(cout|cin|endl|namespace|template|class\s+\w+.*:)", code):
        scores["cpp"] += 3

    best_lang = max(scores, key=scores.get)
    return best_lang if scores[best_lang] > 0 else "python"


class PythonAnalyzer:
    """Real Python code analyzer using the ast module."""

    def __init__(self, code: str):
        self.code = code
        self.tree = None
        self.lines = code.split("\n")
        self.functions = []
        self.classes = []
        self.imports = []
        self.variables = []
        self.loops = []
        self.conditions = []
        self.exceptions = []
        self.calls = []
        self.complexity = {}

    def parse(self):
        """Parse the code into an AST."""
        try:
            self.tree = ast.parse(self.code)
            return True
        except SyntaxError as e:
            self.error = str(e)
            return False

    def analyze(self):
        """Perform full analysis."""
        if not self.parse():
            return self._fallback_analysis()

        for node in ast.walk(self.tree):
            if isinstance(node, ast.FunctionDef):
                self._analyze_function(node)
            elif isinstance(node, ast.ClassDef):
                self._analyze_class(node)
            elif isinstance(node, ast.Import):
                self.imports.extend([alias.name for alias in node.names])
            elif isinstance(node, ast.ImportFrom):
                module = node.module or ""
                self.imports.append(f"{module}.{node.names[0].name}" if module else node.names[0].name)
            elif isinstance(node, (ast.For, ast.While, ast.ListComp, ast.DictComp, ast.SetComp, ast.GeneratorExp)):
                self.loops.append(self._get_node_info(node))
            elif isinstance(node, ast.If):
                self.conditions.append(self._get_node_info(node))
            elif isinstance(node, ast.Try):
                self.exceptions.append(self._get_node_info(node))
            elif isinstance(node, ast.Call):
                self.calls.append(self._get_call_info(node))
            elif isinstance(node, ast.Name) and isinstance(node.ctx, ast.Store):
                self.variables.append(node.id)

        self.variables = list(set(self.variables))
        self.complexity = self._estimate_complexity()
        return self._build_result()

    def _analyze_function(self, node):
        """Analyze a function definition."""
        func_info = {
            "name": node.name,
            "line": node.lineno,
            "end_line": node.end_lineno,
            "args": [arg.arg for arg in node.args.args],
            "defaults": len(node.args.defaults),
            "decorators": [self._get_expr_name(d) for d in node.decorator_list],
            "docstring": ast.get_docstring(node),
            "returns": ast.unparse(node.returns) if node.returns else None,
            "body_lines": node.end_lineno - node.lineno if node.end_lineno else 0,
            "calls": [],
            "complexity": self._calc_function_complexity(node)
        }

        for child in ast.walk(node):
            if isinstance(child, ast.Call) and child != node:
                call_name = self._get_call_info(child)
                if call_name:
                    func_info["calls"].append(call_name)

        self.functions.append(func_info)

    def _analyze_class(self, node):
        """Analyze a class definition."""
        methods = []
        for item in node.body:
            if isinstance(item, ast.FunctionDef):
                methods.append({
                    "name": item.name,
                    "line": item.lineno,
                    "args": [arg.arg for arg in item.args.args]
                })

        self.classes.append({
            "name": node.name,
            "line": node.lineno,
            "end_line": node.end_lineno,
            "bases": [self._get_expr_name(base) for base in node.bases],
            "methods": methods,
            "docstring": ast.get_docstring(node)
        })

    def _get_node_info(self, node):
        return {
            "type": type(node).__name__,
            "line": node.lineno,
            "end_line": getattr(node, "end_lineno", node.lineno)
        }

    def _get_call_info(self, node):
        if isinstance(node.func, ast.Name):
            return node.func.id
        elif isinstance(node.func, ast.Attribute):
            return f"{self._get_expr_name(node.func.value)}.{node.func.attr}"
        return None

    def _get_expr_name(self, node):
        if isinstance(node, ast.Name):
            return node.id
        elif isinstance(node, ast.Attribute):
            return f"{self._get_expr_name(node.value)}.{node.attr}"
        elif isinstance(node, ast.Constant):
            return repr(node.value)
        return "<expr>"

    def _calc_function_complexity(self, node):
        complexity = 1
        for child in ast.walk(node):
            if isinstance(child, (ast.If, ast.While, ast.For, 
                                  ast.ListComp, ast.DictComp, ast.SetComp,
                                  ast.GeneratorExp, ast.ExceptHandler,
                                  ast.With, ast.Assert, ast.comprehension)):
                complexity += 1
            elif isinstance(child, ast.BoolOp):
                complexity += len(child.values) - 1
        return complexity

    def _estimate_complexity(self):
        max_loop_depth = 0

        def count_loop_depth(node, depth=0):
            nonlocal max_loop_depth
            max_loop_depth = max(max_loop_depth, depth)
            for child in ast.iter_child_nodes(node):
                if isinstance(child, (ast.For, ast.While, ast.ListComp, 
                                      ast.DictComp, ast.SetComp)):
                    count_loop_depth(child, depth + 1)
                else:
                    count_loop_depth(child, depth)

        if self.tree:
            count_loop_depth(self.tree)

        complexity_map = {
            0: ("O(1)", "O(1)", "Constant time - operations do not depend on input size."),
            1: ("O(n)", "O(n)", "Linear time - operations scale linearly with input size."),
            2: ("O(n\u00b2)", "O(n\u00b2)", "Quadratic time - nested loops cause squared growth."),
            3: ("O(n\u00b3)", "O(n\u00b3)", "Cubic time - deeply nested loops.")
        }

        time_c, space_c, desc = complexity_map.get(max_loop_depth, 
            ("O(n^k)", "O(n^k)", f"High complexity with {max_loop_depth} nested loop levels."))

        return {
            "time": time_c,
            "space": space_c,
            "description": desc,
            "loop_depth": max_loop_depth
        }

    def _fallback_analysis(self):
        self.functions = self._regex_find_functions()
        self.classes = self._regex_find_classes()
        self.imports = re.findall(r"^(?:from\s+(\w+)\s+import|import\s+(\w+))", 
                                   self.code, re.MULTILINE)
        self.imports = [i[0] or i[1] for i in self.imports]
        self.variables = list(set(re.findall(r"^(\w+)\s*=", self.code, re.MULTILINE)))
        self.complexity = {"time": "Unknown", "space": "Unknown", 
                          "description": "Could not parse syntax.", "loop_depth": 0}
        return self._build_result()

    def _regex_find_functions(self):
        funcs = []
        for match in re.finditer(r"^\s*def\s+(\w+)\s*\(([^)]*)\)", self.code, re.MULTILINE):
            funcs.append({
                "name": match.group(1),
                "line": self.code[:match.start()].count("\n") + 1,
                "args": [a.strip().split(":")[0].split("=")[0].strip() 
                        for a in match.group(2).split(",") if a.strip()],
                "calls": [],
                "complexity": 1
            })
        return funcs

    def _regex_find_classes(self):
        classes = []
        for match in re.finditer(r"^\s*class\s+(\w+)(?:\(([^)]*)\))?", self.code, re.MULTILINE):
            classes.append({
                "name": match.group(1),
                "line": self.code[:match.start()].count("\n") + 1,
                "bases": [match.group(2)] if match.group(2) else [],
                "methods": []
            })
        return classes

    def _build_result(self):
        return {
            "language": "python",
            "total_lines": len(self.lines),
            "code_lines": len([l for l in self.lines if l.strip() and not l.strip().startswith("#")]),
            "comment_lines": len([l for l in self.lines if l.strip().startswith("#")]),
            "blank_lines": len([l for l in self.lines if not l.strip()]),
            "functions": self.functions,
            "classes": self.classes,
            "imports": self.imports,
            "variables": self.variables,
            "loops": self.loops,
            "conditions": self.conditions,
            "exceptions": self.exceptions,
            "calls": list(set(self.calls)),
            "complexity": self.complexity,
            "ast_valid": self.tree is not None
        }

    def get_line_explanations(self):
        explanations = []
        for i, line in enumerate(self.lines, 1):
            stripped = line.strip()
            if not stripped or stripped.startswith("#"):
                continue
            explanation = self._explain_line(stripped, i)
            explanations.append({
                "line": i,
                "code": stripped,
                "explanation": explanation["text"],
                "purpose": explanation["purpose"],
                "variables": explanation["variables"]
            })
        return explanations

    def _explain_line(self, line, line_no):
        explanation = {"text": "", "purpose": "", "variables": []}

        if line.startswith("def "):
            match = re.match(r"def\s+(\w+)\s*\((.*?)\)", line)
            if match:
                explanation["text"] = f"Defines function '{match.group(1)}'. It takes {len(match.group(2).split(',')) if match.group(2) else 0} input(s)."
                explanation["purpose"] = "Creates a reusable block of code."
                if match.group(2):
                    explanation["variables"] = [a.strip() for a in match.group(2).split(",") if a.strip()]

        elif line.startswith("class "):
            match = re.match(r"class\s+(\w+)", line)
            if match:
                explanation["text"] = f"Defines class '{match.group(1)}' - a blueprint for objects."
                explanation["purpose"] = "Object-oriented programming structure."

        elif line.startswith("import ") or line.startswith("from "):
            explanation["text"] = "Imports external code libraries for use in this program."
            explanation["purpose"] = "Reuses existing code and functionality."

        elif line.startswith("if "):
            explanation["text"] = "Checks a condition and executes code only if it is true."
            explanation["purpose"] = "Decision making in the program."

        elif line.startswith("for "):
            explanation["text"] = "Loops over a sequence of items."
            explanation["purpose"] = "Repeats operations for each item."

        elif line.startswith("while "):
            explanation["text"] = "Repeats code while a condition remains true."
            explanation["purpose"] = "Loop with condition-based repetition."

        elif line.startswith("return "):
            explanation["text"] = "Sends a value back from the function to the caller."
            explanation["purpose"] = "Outputs the result of a function."

        elif "=" in line and not line.startswith("=="):
            var = line.split("=")[0].strip()
            explanation["text"] = f"Assigns a value to variable '{var}'."
            explanation["purpose"] = "Stores data for later use."
            explanation["variables"] = [var]

        elif "print(" in line:
            explanation["text"] = "Displays output to the screen."
            explanation["purpose"] = "Shows information to the user."

        else:
            explanation["text"] = "Executes this statement."
            explanation["purpose"] = "Program execution step."

        return explanation

    def get_function_explanations(self):
        explanations = []
        for func in self.functions:
            beginner = f"This function is named '{func['name']}'. It takes {len(func['args'])} input(s)"
            if func["args"]:
                beginner += f" ({', '.join(func['args'])})"
            beginner += " and does some work with them."

            intermediate = f"Function '{func['name']}' accepts parameters {func['args']}"
            if func["docstring"]:
                intermediate += f". Purpose: {func['docstring'][:100]}"

            advanced = f"Function '{func['name']}' (lines {func['line']}-{func['end_line']})"
            advanced += f" with cyclomatic complexity {func['complexity']}."
            advanced += f" Calls: {', '.join(func['calls'][:5]) or 'none'}."

            explanations.append({
                "name": func["name"],
                "beginner": beginner,
                "intermediate": intermediate,
                "advanced": advanced,
                "parameters": func["args"],
                "returns": func["returns"],
                "complexity": func["complexity"]
            })
        return explanations


class JavaAnalyzer:
    """Java code analyzer using javalang."""

    def __init__(self, code: str):
        self.code = code
        self.lines = code.split("\n")
        self.functions = []
        self.classes = []
        self.imports = []
        self.variables = []
        self.loops = []
        self.conditions = []
        self.complexity = {}

    def analyze(self):
        try:
            import javalang
            tree = javalang.parse.parse(self.code)

            for imp in tree.imports:
                self.imports.append(imp.path)

            for path, node in tree:
                if isinstance(node, javalang.tree.ClassDeclaration):
                    self._analyze_class(node)
                elif isinstance(node, javalang.tree.MethodDeclaration):
                    self._analyze_method(node)
                elif isinstance(node, javalang.tree.ForStatement):
                    self.loops.append({"type": "for", "line": node.position.line if node.position else 0})
                elif isinstance(node, javalang.tree.WhileStatement):
                    self.loops.append({"type": "while", "line": node.position.line if node.position else 0})
                elif isinstance(node, javalang.tree.IfStatement):
                    self.conditions.append({"line": node.position.line if node.position else 0})

            self.complexity = self._estimate_complexity()
            return self._build_result()

        except Exception as e:
            return self._fallback_analysis()

    def _analyze_class(self, node):
        methods = []
        for member in (node.body or []):
            if hasattr(member, "name"):
                methods.append({"name": member.name, "line": getattr(member.position, "line", 0) if hasattr(member, "position") else 0})

        self.classes.append({
            "name": node.name,
            "line": node.position.line if node.position else 0,
            "methods": methods
        })

    def _analyze_method(self, node):
        self.functions.append({
            "name": node.name,
            "line": node.position.line if node.position else 0,
            "args": [p.name for p in (node.parameters or [])],
            "return_type": str(node.return_type) if node.return_type else "void",
            "calls": [],
            "complexity": 1
        })

    def _estimate_complexity(self):
        loop_count = len(self.loops)
        if loop_count == 0:
            return {"time": "O(1)", "space": "O(1)", 
                   "description": "Constant operations.", "loop_depth": 0}
        elif loop_count == 1:
            return {"time": "O(n)", "space": "O(n)", 
                   "description": "Linear scan.", "loop_depth": 1}
        else:
            return {"time": "O(n\u00b2)", "space": "O(n\u00b2)", 
                   "description": "Multiple loops detected.", "loop_depth": 2}

    def _fallback_analysis(self):
        self.functions = []
        for match in re.finditer(r"(?:public|private|protected)?\s*(?:static)?\s*(?:<[^>]+>)?\s*(?:\w+)\s+(\w+)\s*\(([^)]*)\)", self.code):
            self.functions.append({
                "name": match.group(1),
                "args": [a.strip().split()[-1] if " " in a.strip() else a.strip() 
                        for a in match.group(2).split(",") if a.strip()],
                "line": self.code[:match.start()].count("\n") + 1,
                "complexity": 1
            })

        for match in re.finditer(r"class\s+(\w+)", self.code):
            self.classes.append({"name": match.group(1), "methods": []})

        self.imports = re.findall(r"import\s+([\w.]+);", self.code)
        self.complexity = {"time": "Unknown", "space": "Unknown", 
                          "description": "Fallback analysis.", "loop_depth": 0}
        return self._build_result()

    def _build_result(self):
        return {
            "language": "java",
            "total_lines": len(self.lines),
            "code_lines": len([l for l in self.lines if l.strip() and not l.strip().startswith("//")]),
            "comment_lines": len([l for l in self.lines if l.strip().startswith("//")]),
            "blank_lines": len([l for l in self.lines if not l.strip()]),
            "functions": self.functions,
            "classes": self.classes,
            "imports": self.imports,
            "variables": self.variables,
            "loops": self.loops,
            "conditions": self.conditions,
            "complexity": self.complexity
        }

    def get_line_explanations(self):
        explanations = []
        for i, line in enumerate(self.lines, 1):
            stripped = line.strip()
            if not stripped or stripped.startswith("//") or stripped.startswith("/*") or stripped.startswith("*") or stripped.startswith("*/"):
                continue
            explanation = self._explain_line(stripped, i)
            explanations.append({
                "line": i,
                "code": stripped,
                "explanation": explanation["text"],
                "purpose": explanation["purpose"],
                "variables": explanation["variables"]
            })
        return explanations

    def _explain_line(self, line, line_no):
        explanation = {"text": "", "purpose": "", "variables": []}

        if line.startswith("import ") or line.startswith("package "):
            explanation["text"] = "Imports or declares a package for this Java file."
            explanation["purpose"] = "Organizes code and reuses external libraries."

        elif "class " in line and "{" in line:
            match = re.search(r"(class|interface|enum)\s+(\w+)", line)
            if match:
                explanation["text"] = f"Declares a {match.group(1)} named '{match.group(2)}'."
                explanation["purpose"] = "Defines a blueprint for objects."

        elif "System.out.print" in line:
            explanation["text"] = "Prints output to the console."
            explanation["purpose"] = "Shows information to the user."

        elif "(" in line and ")" in line and not line.startswith("if ") and not line.startswith("for ") and not line.startswith("while ") and not line.startswith("switch ") and not line.startswith("catch "):
            match = re.search(r"(\w+)\s*\(([^)]*)\)", line)
            if match and match.group(1) not in ["if", "for", "while", "switch", "catch"]:
                explanation["text"] = f"Defines method '{match.group(1)}'. It may take parameters."
                explanation["purpose"] = "Creates a reusable block of code."
                if match.group(2).strip():
                    explanation["variables"] = [a.strip().split()[-1] if " " in a.strip() else a.strip() for a in match.group(2).split(",") if a.strip()]

        elif line.startswith("if "):
            explanation["text"] = "Checks a condition and executes the block if true."
            explanation["purpose"] = "Decision making in the program."

        elif line.startswith("for ") or line.startswith("for("):
            explanation["text"] = "Loops over a collection or range of values."
            explanation["purpose"] = "Repeats operations for each item."

        elif line.startswith("while ") or line.startswith("while("):
            explanation["text"] = "Repeats code while a condition remains true."
            explanation["purpose"] = "Loop with condition-based repetition."

        elif line.startswith("return "):
            explanation["text"] = "Returns a value from the method to the caller."
            explanation["purpose"] = "Outputs the result of a method."

        elif "=" in line and not line.startswith("==") and not line.startswith("!="):
            parts = line.split("=")
            if len(parts) >= 2:
                left = parts[0].strip()
                var = left.split()[-1] if " " in left else left
                explanation["text"] = f"Assigns a value to variable '{var}'."
                explanation["purpose"] = "Stores data for later use."
                explanation["variables"] = [var]

        elif line.startswith("//"):
            explanation["text"] = "Comment line."
            explanation["purpose"] = "Documentation for developers."

        else:
            explanation["text"] = "Executes this statement."
            explanation["purpose"] = "Program execution step."

        return explanation

    def get_function_explanations(self):
        explanations = []
        for func in self.functions:
            beginner = f"This method is named '{func['name']}'. It takes {len(func['args'])} input(s)"
            if func["args"]:
                beginner += f" ({', '.join(func['args'])})"
            beginner += " and performs operations with them."

            intermediate = f"Method '{func['name']}' accepts parameters {func['args']}."
            if func.get("return_type"):
                intermediate += f" Returns type: {func['return_type']}."

            advanced = f"Method '{func['name']}' (line {func['line']})"
            advanced += f" with cyclomatic complexity {func.get('complexity', 1)}."
            advanced += f" Calls: {', '.join(func.get('calls', [])[:5]) or 'none'}."

            explanations.append({
                "name": func["name"],
                "beginner": beginner,
                "intermediate": intermediate,
                "advanced": advanced,
                "parameters": func["args"],
                "returns": func.get("return_type", "void"),
                "complexity": func.get("complexity", 1)
            })
        return explanations


class CAnalyzer:
    """C code analyzer using pycparser or regex fallback."""

    def __init__(self, code: str):
        self.code = code
        self.lines = code.split("\n")
        self.functions = []
        self.classes = []
        self.imports = []
        self.variables = []
        self.loops = []
        self.conditions = []
        self.complexity = {}

    def analyze(self):
        try:
            from pycparser import c_parser
            parser = c_parser.CParser()
            tree = parser.parse(self.code, filename="<input>")

            for node in tree.ext:
                if hasattr(node, "decl") and hasattr(node, "body"):
                    self.functions.append({
                        "name": node.decl.name,
                        "line": node.coord.line if node.coord else 0,
                        "args": [p.name for p in (node.decl.type.args.params if node.decl.type.args else [])],
                        "return_type": self._get_c_type(node.decl.type),
                        "complexity": 1
                    })

            self.imports = re.findall(r"#include\s*<([^>]+)>", self.code)
            self.imports += re.findall(r"#include\s*\"([^\"]+)\"", self.code)

            self.loops = [{"type": "for/while", "line": i+1} 
                         for i, l in enumerate(self.lines) if re.match(r"\s*(for|while)\s*\(", l)]
            self.conditions = [{"line": i+1} 
                              for i, l in enumerate(self.lines) if re.match(r"\s*if\s*\(", l)]

            self.complexity = self._estimate_complexity()
            return self._build_result()

        except Exception:
            return self._fallback_analysis()

    def _get_c_type(self, typ):
        if hasattr(typ, "type") and hasattr(typ.type, "names"):
            return " ".join(typ.type.names)
        return "unknown"

    def _estimate_complexity(self):
        loop_count = len(self.loops)
        if loop_count == 0:
            return {"time": "O(1)", "space": "O(1)", "description": "Constant.", "loop_depth": 0}
        elif loop_count == 1:
            return {"time": "O(n)", "space": "O(n)", "description": "Linear.", "loop_depth": 1}
        else:
            return {"time": "O(n\u00b2)", "space": "O(n\u00b2)", "description": "Multiple loops.", "loop_depth": 2}

    def _fallback_analysis(self):
        for match in re.finditer(r"^(\s*(?:\w+\s+)+)(\w+)\s*\(([^)]*)\)\s*\{", self.code, re.MULTILINE):
            self.functions.append({
                "name": match.group(2),
                "line": self.code[:match.start()].count("\n") + 1,
                "args": [a.strip().split()[-1] if " " in a.strip() else a.strip()
                        for a in match.group(3).split(",") if a.strip()],
                "return_type": match.group(1).strip(),
                "complexity": 1
            })

        self.imports = re.findall(r"#include\s*<([^>]+)>", self.code)
        self.imports += re.findall(r"#include\s*\"([^\"]+)\"", self.code)

        self.loops = [{"type": "loop", "line": i+1} 
                     for i, l in enumerate(self.lines) if re.search(r"\b(for|while)\s*\(", l)]
        self.conditions = [{"line": i+1} 
                          for i, l in enumerate(self.lines) if re.search(r"\bif\s*\(", l)]

        self.complexity = {"time": "Unknown", "space": "Unknown", 
                          "description": "Fallback analysis.", "loop_depth": 0}
        return self._build_result()

    def _build_result(self):
        return {
            "language": "c",
            "total_lines": len(self.lines),
            "code_lines": len([l for l in self.lines if l.strip() and not l.strip().startswith("//")]),
            "comment_lines": len([l for l in self.lines if l.strip().startswith("//")]),
            "blank_lines": len([l for l in self.lines if not l.strip()]),
            "functions": self.functions,
            "classes": self.classes,
            "imports": self.imports,
            "variables": self.variables,
            "loops": self.loops,
            "conditions": self.conditions,
            "complexity": self.complexity
        }

    def get_line_explanations(self):
        explanations = []
        for i, line in enumerate(self.lines, 1):
            stripped = line.strip()
            if not stripped or stripped.startswith("//") or stripped.startswith("/*") or stripped.startswith("*") or stripped.startswith("*/"):
                continue
            explanation = self._explain_line(stripped, i)
            explanations.append({
                "line": i,
                "code": stripped,
                "explanation": explanation["text"],
                "purpose": explanation["purpose"],
                "variables": explanation["variables"]
            })
        return explanations

    def _explain_line(self, line, line_no):
        explanation = {"text": "", "purpose": "", "variables": []}

        if line.startswith("#include"):
            explanation["text"] = "Includes a header file for external functions."
            explanation["purpose"] = "Reuses existing code and libraries."

        elif line.startswith("#define"):
            explanation["text"] = "Defines a preprocessor macro or constant."
            explanation["purpose"] = "Creates reusable constants or macros."

        elif re.match(r"^\s*(struct|typedef|enum|union)\b", line):
            match = re.search(r"(struct|typedef|enum|union)\s+(\w+)", line)
            if match:
                explanation["text"] = f"Declares a {match.group(1)} named '{match.group(2)}'."
                explanation["purpose"] = "Defines a custom data type."

        elif re.search(r"\b(int|void|char|float|double|long|short|unsigned|signed|bool|FILE|static|extern|inline)\b.*\w+\s*\(", line):
            match = re.search(r"(\w+)\s*\(([^)]*)\)", line)
            if match and match.group(1) not in ["if", "for", "while", "switch"]:
                explanation["text"] = f"Defines function '{match.group(1)}'. It may take parameters."
                explanation["purpose"] = "Creates a reusable block of code."
                if match.group(2).strip():
                    explanation["variables"] = [a.strip().split()[-1] if " " in a.strip() else a.strip() for a in match.group(2).split(",") if a.strip()]

        elif line.startswith("if "):
            explanation["text"] = "Checks a condition and executes the block if true."
            explanation["purpose"] = "Decision making in the program."

        elif line.startswith("for ") or line.startswith("for("):
            explanation["text"] = "Loops with an initializer, condition, and increment."
            explanation["purpose"] = "Repeats operations a specific number of times."

        elif line.startswith("while ") or line.startswith("while("):
            explanation["text"] = "Repeats code while a condition remains true."
            explanation["purpose"] = "Loop with condition-based repetition."

        elif line.startswith("return "):
            explanation["text"] = "Returns a value from the function to the caller."
            explanation["purpose"] = "Outputs the result of a function."

        elif "printf(" in line or "scanf(" in line:
            explanation["text"] = "Performs input/output operation."
            explanation["purpose"] = "Interacts with the user or system."

        elif "=" in line and not line.startswith("==") and not line.startswith("!="):
            parts = line.split("=")
            if len(parts) >= 2:
                left = parts[0].strip()
                var = left.split()[-1] if " " in left else left
                explanation["text"] = f"Assigns a value to variable '{var}'."
                explanation["purpose"] = "Stores data for later use."
                explanation["variables"] = [var]

        elif line.startswith("//"):
            explanation["text"] = "Comment line."
            explanation["purpose"] = "Documentation for developers."

        else:
            explanation["text"] = "Executes this statement."
            explanation["purpose"] = "Program execution step."

        return explanation

    def get_function_explanations(self):
        explanations = []
        for func in self.functions:
            beginner = f"This function is named '{func['name']}'. It takes {len(func['args'])} input(s)"
            if func["args"]:
                beginner += f" ({', '.join(func['args'])})"
            beginner += " and performs operations with them."

            intermediate = f"Function '{func['name']}' accepts parameters {func['args']}."
            if func.get("return_type"):
                intermediate += f" Returns type: {func['return_type']}."

            advanced = f"Function '{func['name']}' (line {func['line']})"
            advanced += f" with cyclomatic complexity {func.get('complexity', 1)}."
            advanced += f" Calls: {', '.join(func.get('calls', [])[:5]) or 'none'}."

            explanations.append({
                "name": func["name"],
                "beginner": beginner,
                "intermediate": intermediate,
                "advanced": advanced,
                "parameters": func["args"],
                "returns": func.get("return_type", "void"),
                "complexity": func.get("complexity", 1)
            })
        return explanations


class CPPAnalyzer:
    """C++ code analyzer using regex-based parsing."""

    def __init__(self, code: str):
        self.code = code
        self.lines = code.split("\n")
        self.functions = []
        self.classes = []
        self.imports = []
        self.variables = []
        self.loops = []
        self.conditions = []
        self.complexity = {}

    def analyze(self):
        clean_code = re.sub(r"//.*$", "", self.code, flags=re.MULTILINE)
        clean_code = re.sub(r"/\*.*?\*/", "", clean_code, flags=re.DOTALL)

        for match in re.finditer(r"class\s+(\w+)(?:\s*:\s*(?:public|private|protected)\s+(\w+))?", clean_code):
            self.classes.append({
                "name": match.group(1),
                "line": clean_code[:match.start()].count("\n") + 1,
                "bases": [match.group(2)] if match.group(2) else [],
                "methods": []
            })

        func_pattern = r"(?:^|;)\s*(?:(?:inline|static|virtual|explicit|const)\s+)*(?:(?:\w+::)?(?:\w+)\s+)*(\w+)(?:\s*<[^>]+>)?\s*\(([^)]*)\)\s*(?:const)?\s*\{"
        for match in re.finditer(func_pattern, clean_code, re.MULTILINE):
            name = match.group(1)
            if name not in ["if", "while", "for", "switch", "catch"]:
                self.functions.append({
                    "name": name,
                    "line": clean_code[:match.start()].count("\n") + 1,
                    "args": [a.strip().split()[-1].replace("&", "").replace("*", "").strip() 
                            for a in match.group(2).split(",") if a.strip()],
                    "return_type": "auto",
                    "complexity": 1
                })

        self.imports = re.findall(r"#include\s*<([^>]+)>", self.code)
        self.imports += re.findall(r"#include\s*\"([^\"]+)\"", self.code)

        self.loops = [{"type": "loop", "line": i+1} 
                     for i, l in enumerate(self.lines) if re.search(r"\b(for|while|do\s*\{)\b", l)]

        self.conditions = [{"line": i+1} 
                          for i, l in enumerate(self.lines) if re.search(r"\bif\s*\(", l)]

        self.complexity = self._estimate_complexity()
        return self._build_result()

    def _estimate_complexity(self):
        loop_count = len(self.loops)
        if loop_count == 0:
            return {"time": "O(1)", "space": "O(1)", "description": "Constant.", "loop_depth": 0}
        elif loop_count == 1:
            return {"time": "O(n)", "space": "O(n)", "description": "Linear.", "loop_depth": 1}
        else:
            return {"time": "O(n\u00b2)", "space": "O(n\u00b2)", "description": "Multiple loops.", "loop_depth": 2}

    def _build_result(self):
        return {
            "language": "cpp",
            "total_lines": len(self.lines),
            "code_lines": len([l for l in self.lines if l.strip() and not l.strip().startswith("//")]),
            "comment_lines": len([l for l in self.lines if l.strip().startswith("//")]),
            "blank_lines": len([l for l in self.lines if not l.strip()]),
            "functions": self.functions,
            "classes": self.classes,
            "imports": self.imports,
            "variables": self.variables,
            "loops": self.loops,
            "conditions": self.conditions,
            "complexity": self.complexity
        }

    def get_line_explanations(self):
        explanations = []
        for i, line in enumerate(self.lines, 1):
            stripped = line.strip()
            if not stripped or stripped.startswith("//") or stripped.startswith("/*") or stripped.startswith("*") or stripped.startswith("*/"):
                continue
            explanation = self._explain_line(stripped, i)
            explanations.append({
                "line": i,
                "code": stripped,
                "explanation": explanation["text"],
                "purpose": explanation["purpose"],
                "variables": explanation["variables"]
            })
        return explanations

    def _explain_line(self, line, line_no):
        explanation = {"text": "", "purpose": "", "variables": []}

        if line.startswith("#include"):
            explanation["text"] = "Includes a header file for external functions."
            explanation["purpose"] = "Reuses existing code and libraries."

        elif line.startswith("#define"):
            explanation["text"] = "Defines a preprocessor macro or constant."
            explanation["purpose"] = "Creates reusable constants or macros."

        elif "class " in line and "{" in line:
            match = re.search(r"class\s+(\w+)", line)
            if match:
                explanation["text"] = f"Declares a class named '{match.group(1)}'."
                explanation["purpose"] = "Defines an object-oriented blueprint."

        elif "namespace " in line:
            match = re.search(r"namespace\s+(\w+)", line)
            if match:
                explanation["text"] = f"Declares namespace '{match.group(1)}'."
                explanation["purpose"] = "Organizes code into logical groups."

        elif re.search(r"\b(int|void|char|float|double|long|short|unsigned|signed|bool|auto|std::string|vector|map|static|extern|inline|virtual|explicit|const)\b.*\w+\s*\(", line):
            match = re.search(r"(\w+)\s*\(([^)]*)\)", line)
            if match and match.group(1) not in ["if", "for", "while", "switch", "catch"]:
                explanation["text"] = f"Defines function '{match.group(1)}'. It may take parameters."
                explanation["purpose"] = "Creates a reusable block of code."
                if match.group(2).strip():
                    explanation["variables"] = [a.strip().split()[-1].replace("&", "").replace("*", "").strip() for a in match.group(2).split(",") if a.strip()]

        elif line.startswith("if "):
            explanation["text"] = "Checks a condition and executes the block if true."
            explanation["purpose"] = "Decision making in the program."

        elif line.startswith("for ") or line.startswith("for("):
            explanation["text"] = "Loops with an initializer, condition, and increment."
            explanation["purpose"] = "Repeats operations a specific number of times."

        elif line.startswith("while ") or line.startswith("while("):
            explanation["text"] = "Repeats code while a condition remains true."
            explanation["purpose"] = "Loop with condition-based repetition."

        elif line.startswith("return "):
            explanation["text"] = "Returns a value from the function to the caller."
            explanation["purpose"] = "Outputs the result of a function."

        elif "cout" in line or "cin" in line or "printf(" in line or "scanf(" in line:
            explanation["text"] = "Performs input/output operation."
            explanation["purpose"] = "Interacts with the user or system."

        elif "=" in line and not line.startswith("==") and not line.startswith("!="):
            parts = line.split("=")
            if len(parts) >= 2:
                left = parts[0].strip()
                var = left.split()[-1] if " " in left else left
                explanation["text"] = f"Assigns a value to variable '{var}'."
                explanation["purpose"] = "Stores data for later use."
                explanation["variables"] = [var]

        elif line.startswith("//"):
            explanation["text"] = "Comment line."
            explanation["purpose"] = "Documentation for developers."

        else:
            explanation["text"] = "Executes this statement."
            explanation["purpose"] = "Program execution step."

        return explanation

    def get_function_explanations(self):
        explanations = []
        for func in self.functions:
            beginner = f"This function is named '{func['name']}'. It takes {len(func['args'])} input(s)"
            if func["args"]:
                beginner += f" ({', '.join(func['args'])})"
            beginner += " and performs operations with them."

            intermediate = f"Function '{func['name']}' accepts parameters {func['args']}."
            if func.get("return_type"):
                intermediate += f" Returns type: {func['return_type']}."

            advanced = f"Function '{func['name']}' (line {func['line']})"
            advanced += f" with cyclomatic complexity {func.get('complexity', 1)}."
            advanced += f" Calls: {', '.join(func.get('calls', [])[:5]) or 'none'}."

            explanations.append({
                "name": func["name"],
                "beginner": beginner,
                "intermediate": intermediate,
                "advanced": advanced,
                "parameters": func["args"],
                "returns": func.get("return_type", "void"),
                "complexity": func.get("complexity", 1)
            })
        return explanations


def analyze_code(code: str, filename: str = "") -> Dict[str, Any]:
    """Main entry point for code analysis."""
    language = detect_language(code, filename)

    if language == "python":
        analyzer = PythonAnalyzer(code)
        result = analyzer.analyze()
        result["line_explanations"] = analyzer.get_line_explanations()
        result["function_explanations"] = analyzer.get_function_explanations()
    elif language == "java":
        analyzer = JavaAnalyzer(code)
        result = analyzer.analyze()
        result["line_explanations"] = analyzer.get_line_explanations()
        result["function_explanations"] = analyzer.get_function_explanations()
    elif language == "c":
        analyzer = CAnalyzer(code)
        result = analyzer.analyze()
        result["line_explanations"] = analyzer.get_line_explanations()
        result["function_explanations"] = analyzer.get_function_explanations()
    elif language == "cpp":
        analyzer = CPPAnalyzer(code)
        result = analyzer.analyze()
        result["line_explanations"] = analyzer.get_line_explanations()
        result["function_explanations"] = analyzer.get_function_explanations()
    else:
        analyzer = PythonAnalyzer(code)
        result = analyzer.analyze()
        result["line_explanations"] = analyzer.get_line_explanations()
        result["function_explanations"] = analyzer.get_function_explanations()

    result["detected_language"] = language
    result["filename"] = filename
    return result
