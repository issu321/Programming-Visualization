---
title: Programming Visualization
emoji: 🧠
colorFrom: blue
colorTo: purple
sdk: docker
app_file: app.py
pinned: false
---

# Programming Visualization

<div align="center">

![Logo](https://img.shields.io/badge/ProgViz-AI%20Code%20Analysis-blue?style=for-the-badge&logo=python)

**AI-Powered Code Analysis & Visualization Platform**

[![Python](https://img.shields.io/badge/Python-3.11%2B-blue?logo=python)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-3.0-black?logo=flask)](https://flask.palletsprojects.com)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![GitHub](https://img.shields.io/badge/GitHub-issu321-181717?logo=github)](https://github.com/issu321)

Developed by **[issu321](https://github.com/issu321)**

</div>

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Screenshots](#screenshots)
- [Architecture](#architecture)
- [Installation](#installation)
  - [Windows Setup](#windows-setup)
  - [Linux Setup](#linux-setup)
  - [Docker Deployment](#docker-deployment)
  - [Hugging Face Spaces](#hugging-face-spaces)
- [Usage Guide](#usage-guide)
- [Technology Stack](#technology-stack)
- [Folder Structure](#folder-structure)
- [API Documentation](#api-documentation)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

**Programming Visualization** is a production-ready Flask-based AI Programming Visualization Platform capable of analyzing source code and generating interactive visual explanations.

Upload or paste your code, and the platform automatically generates:

- Code structure analysis
- Function hierarchy visualization
- Variable usage tracking
- Class hierarchy diagrams
- Execution flowcharts
- AST (Abstract Syntax Tree) visualization
- Dependency graphs
- Call graphs
- Beginner-friendly explanations
- Function-level explanations
- Line-by-line breakdowns
- Complexity analysis (Time & Space)

### Supported Languages

| Language | Parser | Status |
|----------|--------|--------|
| Python | `ast` (built-in) | Full Support |
| Java | `javalang` | Full Support |
| C | `pycparser` | Full Support |
| C++ | Advanced Regex + Heuristics | Full Support |

---

## Features

### Core Analysis
- **Real AST Generation** - Uses actual Python `ast` module for accurate parsing
- **Multi-Language Support** - Python, Java, C, C++ with real parsers
- **Function Detection** - Identifies all functions, parameters, return types
- **Class Detection** - Extracts classes, methods, inheritance
- **Import Analysis** - Maps all dependencies and libraries
- **Loop & Condition Detection** - Identifies control flow structures

### Visualizations
- **AST Tree** - Interactive tree with zoom, collapse/expand
- **Call Graphs** - NetworkX-based directed graphs
- **Function Hierarchy** - Sunburst charts showing relationships
- **Flowcharts** - Auto-generated execution flowcharts (Plotly-based)
- **Dependency Graphs** - Library import visualization
- **Class Hierarchy** - Inheritance tree visualization
- **Complexity Charts** - Bar charts per function
- **Metrics Charts** - Code composition pie charts

### Explanations
- **Beginner Level** - Simple, analogy-based explanations
- **Intermediate Level** - Technical but accessible
- **Advanced Level** - Detailed complexity and architecture
- **Line-by-Line** - Every line explained with purpose and variables

### Reports
- **HTML Reports** - Styled web reports
- **JSON Reports** - Machine-readable data
- **TXT Reports** - Plain text summaries
- **PDF Support** - Exportable documentation

### User Features
- **User Authentication** - Registration, login, session management
- **Analysis History** - Save and revisit past analyses
- **File Upload** - Drag & drop support
- **Theme System** - Light/Dark mode with persistence
- **Responsive Design** - Works on desktop, tablet, mobile

---

## Screenshots

> *Screenshots will be added here. Run the application to see the full interface.*

### Home Page
Premium landing page with animated hero, glassmorphism cards, and live statistics.

### Analyzer
Code input with syntax highlighting, drag-and-drop upload, and multi-language support.

### Visualization Dashboard
Interactive charts, AST trees, call graphs, and flowcharts with tabbed navigation.

---

## Architecture

```
Programming-Visualization/
├── app.py              # Flask application (routes, views)
├── analyzers.py        # Code analysis engine (AST, parsing)
├── visualizer.py       # Visualization engine (Plotly, NetworkX)
├── database.py         # SQLite database operations
├── auth.py             # Authentication & session management
├── requirements.txt    # Python dependencies
├── Dockerfile          # Container configuration
├── install.sh          # Linux installer
├── install.bat         # Windows installer
├── templates/          # HTML templates (Jinja2)
│   ├── base.html
│   ├── home.html
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── analyzer.html
│   ├── visualization.html
│   ├── reports.html
│   ├── database.html
│   └── contact.html
├── static/             # CSS, JS, images
│   ├── css/style.css
│   └── js/main.js
├── uploads/            # Uploaded code files
├── reports/            # Generated reports
└── database/           # SQLite database files
```

### Data Flow

```
User Input (Paste/Upload)
    |
    v
Language Detection
    |
    v
AST Parsing (Real parsers)
    |
    v
Analysis Engine
    |-- Functions
    |-- Classes
    |-- Variables
    |-- Complexity
    |-- Dependencies
    |
    v
Visualization Engine
    |-- Plotly Charts
    |-- NetworkX Graphs
    |-- Mermaid Flowcharts
    |
    v
Database Storage
    |
    v
Interactive Dashboard
```

---

## Installation

### Prerequisites

- Python 3.11 or higher
- pip (Python package manager)
- Git

### Windows Setup

1. **Clone the repository:**
   ```cmd
   git clone https://github.com/issu321/Programming-Visualization.git
   cd Programming-Visualization
   ```

2. **Run the installer:**
   ```cmd
   install.bat
   ```

   Or manually:
   ```cmd
   python -m venv venv
   venv\Scriptsctivate.bat
   pip install -r requirements.txt
   python -c "from database import init_db; init_db()"
   python app.py
   ```

3. **Open in browser:**
   ```
   http://localhost:5000
   ```

### Linux Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/issu321/Programming-Visualization.git
   cd Programming-Visualization
   ```

2. **Run the installer:**
   ```bash
   chmod +x install.sh
   ./install.sh
   ```

   Or manually:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   python -c "from database import init_db; init_db()"
   python app.py
   ```

3. **Open in browser:**
   ```
   http://localhost:5000
   ```

### Docker Deployment

1. **Build the image:**
   ```bash
   docker build -t programming-visualization .
   ```

2. **Run the container:**
   ```bash
   docker run -p 7860:7860 programming-visualization
   ```

3. **Open in browser:**
   ```
   http://localhost:7860
   ```

### Hugging Face Spaces

1. Create a new Space on [Hugging Face](https://huggingface.co/spaces)
2. Select **Docker** as the SDK
3. Clone the Space repository
4. Copy all project files into the repository
5. Push to deploy:
   ```bash
   git add .
   git commit -m "Initial deployment"
   git push
   ```

---

## Usage Guide

### 1. Register an Account
- Navigate to `/register`
- Create a username, email, and password
- Log in to access the dashboard

### 2. Analyze Code
- Go to `/analyzer`
- **Paste code** directly or **upload a file** (.py, .java, .c, .cpp, .h)
- Click **Analyze Code**
- The system will detect the language automatically

### 3. View Visualizations
- The visualization page shows multiple tabs:
  - **Overview** - Metrics and complexity charts
  - **Functions** - Function list with complexity
  - **Classes** - Class hierarchy and methods
  - **AST Tree** - Interactive syntax tree (Python only)
  - **Call Graph** - Function relationships
  - **Flowchart** - Execution flow diagram
  - **Dependencies** - Import visualization
  - **Explanations** - Multi-level function explanations
  - **Line by Line** - Detailed line breakdowns

### 4. Download Reports
- On the visualization page, click report buttons
- Available formats: HTML, JSON, TXT
- Reports include all analysis data and visualizations

### 5. Manage History
- Visit `/dashboard` to see your analysis history
- View `/database` for platform statistics
- Revisit any past analysis by clicking "View"

---

## Technology Stack

### Backend
| Technology | Version | Purpose |
|------------|---------|---------|
| Python | 3.11+ | Core language |
| Flask | 3.0.0 | Web framework |
| Werkzeug | 3.0.1 | WSGI utilities |
| SQLite | Built-in | Database |

### Analysis
| Technology | Version | Purpose |
|------------|---------|---------|
| ast | Built-in | Python AST parsing |
| javalang | 0.13.0 | Java parsing |
| pycparser | 2.21 | C parsing |

### Visualization
| Technology | Version | Purpose |
|------------|---------|---------|
| Plotly | 5.18.0 | Interactive charts |
| NetworkX | 3.2.1 | Graph algorithms |
| Mermaid | 10.x | Flowcharts |
| D3.js | CDN | Data visualization |

### Frontend
| Technology | Purpose |
|------------|---------|
| HTML5 | Structure |
| CSS3 | Styling |
| JavaScript | Interactivity |
| Font Awesome | Icons |
| Google Fonts | Typography |

### Design
- **Glassmorphism** - Translucent frosted glass effects
- **Claymorphism** - Soft 3D shadow effects
- **Dark/Light Mode** - Theme system with persistence
- **Responsive** - Mobile-first design

---

## Folder Structure

```
Programming-Visualization/
|
|-- app.py                  # Main Flask application
|-- analyzers.py            # Code analysis engine
|-- visualizer.py           # Visualization generator
|-- database.py             # Database operations
|-- auth.py                 # Authentication system
|-- requirements.txt        # Python dependencies
|-- Dockerfile              # Docker configuration
|-- install.sh              # Linux installation script
|-- install.bat             # Windows installation script
|-- README.md               # This file
|
|-- templates/              # Jinja2 HTML templates
|   |-- base.html           # Base layout template
|   |-- home.html           # Landing page
|   |-- login.html          # Login page
|   |-- register.html       # Registration page
|   |-- dashboard.html      # User dashboard
|   |-- analyzer.html       # Code input/analyzer
|   |-- visualization.html  # Results & charts
|   |-- reports.html        # Report management
|   |-- database.html       # Statistics page
|   |-- features.html       # Features showcase
|   |-- contact.html        # Contact page
|
|-- static/                 # Static assets
|   |-- css/
|   |   |-- style.css       # Main stylesheet
|   |-- js/
|   |   |-- main.js         # Main JavaScript
|   |-- images/             # Image assets
|
|-- uploads/                # Uploaded code files
|-- reports/                # Generated reports
|-- database/               # SQLite database
```

---

## API Documentation

### Endpoints

#### Analyze Code
```http
POST /api/analyze
Content-Type: application/json

{
    "code": "def hello():
    print('Hello')",
    "filename": "example.py"
}
```

**Response:**
```json
{
    "success": true,
    "analysis": {
        "language": "python",
        "functions": [...],
        "classes": [...],
        "complexity": {...}
    },
    "visualizations": {
        "ast_tree": {...},
        "call_graph": {...}
    }
}
```

#### Get Stats
```http
GET /api/stats
```

**Response:**
```json
{
    "total_users": 10,
    "total_analyses": 50,
    "total_files": 30,
    "language_stats": {
        "python": 30,
        "java": 10,
        "c": 5,
        "cpp": 5
    }
}
```

#### Update Theme
```http
POST /api/theme
Content-Type: application/json

{
    "theme": "dark"
}
```

---

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Setup

```bash
# Clone your fork
git clone https://github.com/your-username/Programming-Visualization.git
cd Programming-Visualization

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install in development mode
pip install -r requirements.txt

# Run in debug mode
python app.py
```

---

## License

This project is licensed under the MIT License.

```
MIT License

Copyright (c) 2024 issu321

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## Developer

**issu321**

- GitHub: [@issu321](https://github.com/issu321)
- Repository: [Programming-Visualization](https://github.com/issu321/Programming-Visualization)

---

<div align="center">

**Built with passion for code visualization.**

⭐ Star this repo if you find it useful!

</div>
