<!-- ═══════════════════════════════════════════════════════════════════════════ -->
<!-- ║  PROGRAMMING VISUALIZATION — ULTIMATE README                          ║ -->
<!-- ║  Built by issu321 (Mohammed Usman)                                      ║ -->
<!-- ║  AI-Powered Code Analysis & Neural Visualization Platform               ║ -->
<!-- ═══════════════════════════════════════════════════════════════════════════ -->

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:00f2ff,50:7000ff,100:ff00e6&height=280&section=header&text=🧠%20PROGRAMMING%20VISUALIZATION&fontSize=50&fontColor=ffffff&fontAlignY=35&animation=twinkling&desc=AI-Powered%20Code%20Analysis%20%7C%20Neural%20Flowcharts%20%7C%20Interactive%20AST%20Trees&descSize=18&descAlignY=60"/>

<br>

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=700&size=24&duration=2800&pause=800&color=00F2FF&center=true&vCenter=true&width=900&lines=Upload+%E2%86%92+Analyze+%E2%86%92+Visualize+%E2%86%92+Understand;Multi-Language+AST+Parsing+%7C+Neural+Flowcharts+%7C+Interactive+Charts;Python+%E2%80%A2+Java+%E2%80%A2+C+%E2%80%A2+C%2B%2B+%E2%80%94+All+Supported;Built+with+%F0%9F%92%9C+by+issu321+%F0%9F%9A%80+Mohammed+Usman" alt="Typing Animation"/>

<br><br>

<p>
  <img src="https://img.shields.io/badge/Python-3.11+-00f2ff?style=for-the-badge&logo=python&logoColor=white&labelColor=0a0a1a"/>
  <img src="https://img.shields.io/badge/Flask-3.0.0-00ff88?style=for-the-badge&logo=flask&logoColor=white&labelColor=0a0a1a"/>
  <img src="https://img.shields.io/badge/AI-Analysis-ff00e6?style=for-the-badge&logo=tensorflow&logoColor=white&labelColor=0a0a1a"/>
  <img src="https://img.shields.io/badge/Status-Production-7000ff?style=for-the-badge&logo=github&logoColor=white&labelColor=0a0a1a"/>
  <img src="https://img.shields.io/badge/License-MIT-00f2ff?style=for-the-badge&logo=opensourceinitiative&logoColor=white&labelColor=0a0a1a"/>
  <img src="https://img.shields.io/badge/Platform-Cross--Platform-ff00e6?style=for-the-badge&logo=windows&logoColor=white&labelColor=0a0a1a"/>
</p>

<br>

<p>
  <a href="#-overview"><img src="https://img.shields.io/badge/Overview-00f2ff?style=flat-square&labelColor=0a0a1a"/></a>
  <a href="#-system-architecture"><img src="https://img.shields.io/badge/Architecture-7000ff?style=flat-square&labelColor=0a0a1a"/></a>
  <a href="#-neural-data-flow"><img src="https://img.shields.io/badge/Data_Flow-ff00e6?style=flat-square&labelColor=0a0a1a"/></a>
  <a href="#-feature-matrix"><img src="https://img.shields.io/badge/Features-00ff88?style=flat-square&labelColor=0a0a1a"/></a>
  <a href="#-installation"><img src="https://img.shields.io/badge/Install-00f2ff?style=flat-square&labelColor=0a0a1a"/></a>
  <a href="#-api-documentation"><img src="https://img.shields.io/badge/API-7000ff?style=flat-square&labelColor=0a0a1a"/></a>
  <a href="#-contributing"><img src="https://img.shields.io/badge/Contribute-ff00e6?style=flat-square&labelColor=0a0a1a"/></a>
</p>

</div>

<br>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=rect&color=0:00f2ff,50:7000ff,100:ff00e6&height=3&section=footer&reversal=true"/>
</p>

<br>

<h1 align="center">
  <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Electric%20Plug.png" width="35"/> 
  Overview
</h1>

<div align="center">

```
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║   PROGRAMMING VISUALIZATION  —  Where Source Code Meets Cognition           ║
║                                                                              ║
║   Transform raw code into stunning, interactive visual explanations.       ║
║   Upload, paste, or API-submit — watch the neural engine deconstruct         ║
║   your code into AST trees, call graphs, flowcharts, and complexity          ║
║   analyses in milliseconds.                                                  ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

</div>

<br>

**Programming Visualization** is a production-grade, Flask-based **AI Code Analysis & Visualization Platform** engineered for developers, educators, and students. It bridges the gap between raw syntax and visual comprehension through multi-layered neural parsing, real-time AST generation, and cinematic interactive charts.

### Mission Statement

> *"Every line of code tells a story. We just make it visible."*
> — **issu321** (Mohammed Usman)

<br>

<h3 align="center">Supported Languages</h3>

<div align="center">

| Language | Parser | AST Support | Complexity | Call Graph | Flowchart | Status |
|:--------:|:------:|:-----------:|:----------:|:----------:|:---------:|:------:|
| Python | `ast` (Built-in) | Full | O(n) | Full | Full | Production |
| Java | `javalang` | Full | O(n) | Full | Full | Production |
| C | `pycparser` | Full | O(n) | Full | Full | Production |
| C++ | Regex + Heuristics | Partial | O(n) | Full | Full | Beta |

</div>

<br>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=rect&color=0:ff00e6,50:7000ff,100:00f2ff&height=3&section=footer&reversal=true"/>
</p>

<br>

<h1 align="center">
  <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Gear.png" width="35"/> 
  System Architecture
</h1>

<h3 align="center">Neural Layer Architecture</h3>

```mermaid
graph TB
    subgraph INPUT["INPUT LAYER"]
        A1["File Upload (.py .java .c .cpp .h)"]
        A2["Code Paste (Direct Text Input)"]
        A3["API Endpoint (POST /api/analyze)"]
        A4["Mobile Browser (Responsive UI)"]
    end

    subgraph DETECT["DETECTION NEURON"]
        B1["Extension Analysis"]
        B2["Content Heuristics"]
        B3["Syntax Validation"]
        B4["Confidence Scoring"]
    end

    subgraph PARSE["PARSING CORE"]
        C1["Python AST Parser"]
        C2["Java Parser (javalang)"]
        C3["C Parser (pycparser)"]
        C4["C++ Parser (Regex + Heuristics)"]
    end

    subgraph ANALYZE["ANALYSIS CORE"]
        D1["Function Detection"]
        D2["Class Extraction"]
        D3["Variable Tracking"]
        D4["Complexity Analysis"]
        D5["Dependency Mapping"]
        D6["Control Flow Analysis"]
    end

    subgraph VIZ["VISUALIZATION NET"]
        E1["Plotly Charts"]
        E2["NetworkX Graphs"]
        E3["Mermaid Flowcharts"]
        E4["D3.js AST Trees"]
        E5["HTML Reports"]
    end

    subgraph OUTPUT["OUTPUT LAYER"]
        F1["Web Dashboard"]
        F2["Report Downloads"]
        F3["JSON Persistence"]
        F4["API Response"]
    end

    A1 --> B1
    A2 --> B2
    A3 --> B3
    A4 --> B1
    B1 --> B4
    B2 --> B4
    B3 --> B4
    B4 --> C1
    B4 --> C2
    B4 --> C3
    B4 --> C4
    C1 --> D1
    C2 --> D2
    C3 --> D3
    C4 --> D4
    D1 --> D5
    D2 --> D5
    D3 --> D6
    D4 --> D6
    D5 --> E1
    D6 --> E2
    D1 --> E3
    D2 --> E4
    D3 --> E5
    D4 --> E5
    E1 --> F1
    E2 --> F2
    E3 --> F3
    E4 --> F4
    E5 --> F1
    E5 --> F2

    classDef input fill:#0a0a1a,stroke:#00f2ff,stroke-width:3px,color:#fff
    classDef detect fill:#0a0a1a,stroke:#7000ff,stroke-width:3px,color:#fff
    classDef parse fill:#0a0a1a,stroke:#ff00e6,stroke-width:3px,color:#fff
    classDef analyze fill:#0a0a1a,stroke:#00ff88,stroke-width:3px,color:#fff
    classDef viz fill:#0a0a1a,stroke:#00f2ff,stroke-width:3px,color:#fff
    classDef output fill:#0a0a1a,stroke:#ff00e6,stroke-width:3px,color:#fff
    class A1,A2,A3,A4 input
    class B1,B2,B3,B4 detect
    class C1,C2,C3,C4 parse
    class D1,D2,D3,D4,D5,D6 analyze
    class E1,E2,E3,E4,E5 viz
    class F1,F2,F3,F4 output
```

<br>

<h3 align="center">Component Interaction Diagram</h3>

```mermaid
graph LR
    subgraph CLIENT["CLIENT BROWSER"]
        C1["Home Page"]
        C2["Analyzer"]
        C3["Dashboard"]
        C4["Visualization"]
        C5["Reports"]
    end

    subgraph FLASK["FLASK SERVER"]
        F1["Routes (app.py)"]
        F2["Session Manager"]
        F3["Theme Engine"]
    end

    subgraph ENGINE["ANALYSIS ENGINE"]
        E1["analyzers.py"]
        E2["detect_language()"]
        E3["analyze_code()"]
    end

    subgraph VIZENGINE["VIZ ENGINE"]
        V1["visualizer.py"]
        V2["CodeVisualizer"]
        V3["generate_report()"]
    end

    subgraph STORAGE["JSON STORAGE"]
        S1["analyses.json"]
        S2["files.json"]
        S3["reports.json"]
    end

    subgraph STATIC["STATIC ASSETS"]
        ST1["templates/"]
        ST2["css/style.css"]
        ST3["js/main.js"]
    end

    C1 --> F1
    C2 --> F1
    C3 --> F1
    C4 --> F1
    C5 --> F1
    F1 --> F2
    F1 --> F3
    F1 --> E1
    E1 --> E2
    E2 --> E3
    E3 --> V1
    V1 --> V2
    V2 --> V3
    V3 --> S1
    V3 --> S2
    V3 --> S3
    F1 --> ST1
    ST1 --> ST2
    ST1 --> ST3
    S1 --> C3
    S2 --> C3
    S3 --> C5
    V2 --> C4

    classDef client fill:#0a0a1a,stroke:#00f2ff,stroke-width:2px,color:#fff
    classDef flask fill:#0a0a1a,stroke:#7000ff,stroke-width:2px,color:#fff
    classDef engine fill:#0a0a1a,stroke:#ff00e6,stroke-width:2px,color:#fff
    classDef viz fill:#0a0a1a,stroke:#00ff88,stroke-width:2px,color:#fff
    classDef storage fill:#0a0a1a,stroke:#00f2ff,stroke-width:2px,color:#fff
    classDef static fill:#0a0a1a,stroke:#ff00e6,stroke-width:2px,color:#fff
    class C1,C2,C3,C4,C5 client
    class F1,F2,F3 flask
    class E1,E2,E3 engine
    class V1,V2,V3 viz
    class S1,S2,S3 storage
    class ST1,ST2,ST3 static
```

<br>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=rect&color=0:00f2ff,50:ff00e6,100:7000ff&height=3&section=footer&reversal=true"/>
</p>

<br>

<h1 align="center">
  <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Chart%20Increasing.png" width="35"/> 
  Neural Data Flow
</h1>

<h3 align="center">Complete Request Lifecycle Pipeline</h3>

```mermaid
flowchart LR
    subgraph USER["USER INTERFACE"]
        U1["Paste Code"]
        U2["Upload File"]
        U3["API Call"]
    end

    subgraph ROUTER["FLASK ROUTER"]
        R1["/analyzer Route"]
        R2["Language Detection"]
        R3["Security Check"]
    end

    subgraph ENGINE["ANALYSIS ENGINE"]
        E1["AST Parser"]
        E2["Function Scanner"]
        E3["Class Mapper"]
        E4["Complexity Calculator"]
        E5["Dependency Resolver"]
    end

    subgraph VIZ["VISUALIZATION ENGINE"]
        V1["Plotly Charts"]
        V2["NetworkX Graphs"]
        V3["Mermaid Flowcharts"]
        V4["D3.js Trees"]
        V5["HTML Reports"]
    end

    subgraph STORAGE["PERSISTENCE LAYER"]
        S1["analyses.json"]
        S2["files.json"]
        S3["reports.json"]
    end

    subgraph DASHBOARD["DASHBOARD"]
        D1["History View"]
        D2["Stats Cards"]
        D3["Language Pie"]
        D4["Report Manager"]
    end

    U1 --> R1
    U2 --> R1
    U3 --> R1
    R1 --> R3
    R3 --> R2
    R2 --> E1
    E1 --> E2
    E2 --> E3
    E3 --> E4
    E4 --> E5
    E5 --> V1
    E5 --> V2
    E5 --> V3
    E5 --> V4
    V1 --> V5
    V2 --> V5
    V3 --> V5
    V4 --> V5
    V1 --> S1
    V2 --> S2
    V3 --> S3
    S1 --> D1
    S2 --> D2
    S3 --> D3
    V5 --> D4
    D1 --> U1
    D2 --> U2

    classDef user fill:#0a0a1a,stroke:#00f2ff,stroke-width:3px,color:#fff
    classDef router fill:#0a0a1a,stroke:#7000ff,stroke-width:3px,color:#fff
    classDef engine fill:#0a0a1a,stroke:#ff00e6,stroke-width:3px,color:#fff
    classDef viz fill:#0a0a1a,stroke:#00ff88,stroke-width:3px,color:#fff
    classDef storage fill:#0a0a1a,stroke:#00f2ff,stroke-width:3px,color:#fff
    classDef dashboard fill:#0a0a1a,stroke:#ff00e6,stroke-width:3px,color:#fff
    class U1,U2,U3 user
    class R1,R2,R3 router
    class E1,E2,E3,E4,E5 engine
    class V1,V2,V3,V4,V5 viz
    class S1,S2,S3 storage
    class D1,D2,D3,D4 dashboard
```

<br>

<h3 align="center">State Machine — Analysis Lifecycle</h3>

```mermaid
stateDiagram-v2
    [*] --> IDLE
    IDLE --> UPLOADING: User Uploads File
    IDLE --> PASTING: User Pastes Code
    IDLE --> API_CALL: POST /api/analyze

    UPLOADING --> VALIDATING: File Received
    PASTING --> VALIDATING: Code Received
    API_CALL --> VALIDATING: JSON Parsed

    VALIDATING --> DETECTING: File Valid
    VALIDATING --> ERROR: Invalid File Type
    VALIDATING --> ERROR: Empty Content

    DETECTING --> PARSING: Language Confirmed
    DETECTING --> ERROR: Unknown Language

    PARSING --> ANALYZING: AST Generated
    PARSING --> ERROR: Syntax Error

    ANALYZING --> VISUALIZING: Metrics Computed
    ANALYZING --> ERROR: Analysis Failed

    VISUALIZING --> SAVING: Charts Rendered
    VISUALIZING --> ERROR: Render Failed

    SAVING --> DASHBOARD: JSON Saved
    SAVING --> ERROR: Write Failed

    DASHBOARD --> IDLE: User Navigates Away
    DASHBOARD --> REPORTING: User Clicks Export

    REPORTING --> COMPLETE: Report Generated
    REPORTING --> ERROR: Export Failed

    COMPLETE --> IDLE: Reset
    ERROR --> IDLE: Flash Message

    classDef idle fill:#0a0a1a,stroke:#00f2ff,stroke-width:2px,color:#fff
    classDef validate fill:#0a0a1a,stroke:#7000ff,stroke-width:2px,color:#fff
    classDef analyze fill:#0a0a1a,stroke:#ff00e6,stroke-width:2px,color:#fff
    classDef viz fill:#0a0a1a,stroke:#00ff88,stroke-width:2px,color:#fff
    classDef dash fill:#0a0a1a,stroke:#00f2ff,stroke-width:2px,color:#fff
    classDef error fill:#1a0000,stroke:#ff0044,stroke-width:2px,color:#fff
    classDef complete fill:#001a00,stroke:#00ff88,stroke-width:2px,color:#fff
    class IDLE idle
    class VALIDATING validate
    class ANALYZING analyze
    class VISUALIZING viz
    class DASHBOARD dash
    class ERROR error
    class COMPLETE complete
```

<br>

<h3 align="center">Decision Tree — Language Detection</h3>

```mermaid
flowchart TD
    START([Code Input]) --> EXT{Check File Extension}

    EXT -->|.py| PY[Python]
    EXT -->|.java| JAVA[Java]
    EXT -->|.c| C[C]
    EXT -->|.cpp / .hpp / .cc / .cxx| CPP[C++]
    EXT -->|.h| H{Header File}

    H -->|Contains C++ keywords| CPP
    H -->|Contains C keywords| C
    H -->|Ambiguous| HEUR[Content Heuristics]

    EXT -->|No Extension / Unknown| HEUR

    HEUR -->|Contains def / import / class with :| PY
    HEUR -->|Contains public class / package / import java| JAVA
    HEUR -->|Contains #include + std:: / class with :| CPP
    HEUR -->|Contains #include + printf / struct| C
    HEUR -->|Still Ambiguous| FALL[Fallback: Python]

    PY --> CONF{Confidence > 0.75?}
    JAVA --> CONF
    C --> CONF
    CPP --> CONF
    FALL --> CONF

    CONF -->|Yes| PARSE[Proceed to AST Parser]
    CONF -->|No| WARN[Warning: Low Confidence]

    WARN --> PARSE
    PARSE --> SUCCESS[Analysis Complete]

    classDef start fill:#0a0a1a,stroke:#00f2ff,stroke-width:3px,color:#fff
    classDef ext fill:#0a0a1a,stroke:#7000ff,stroke-width:2px,color:#fff
    classDef py fill:#001a1a,stroke:#00ff88,stroke-width:2px,color:#fff
    classDef java fill:#1a1a00,stroke:#ffcc00,stroke-width:2px,color:#fff
    classDef c fill:#1a0a00,stroke:#ff8800,stroke-width:2px,color:#fff
    classDef cpp fill:#1a001a,stroke:#ff00e6,stroke-width:2px,color:#fff
    classDef conf fill:#0a0a1a,stroke:#00f2ff,stroke-width:2px,color:#fff
    classDef success fill:#001a00,stroke:#00ff88,stroke-width:3px,color:#fff
    classDef warn fill:#1a1a00,stroke:#ffcc00,stroke-width:2px,color:#fff
    class START start
    class EXT ext
    class PY py
    class JAVA java
    class C c
    class CPP cpp
    class CONF conf
    class SUCCESS success
    class WARN warn
```

<br>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=rect&color=0:7000ff,50:00f2ff,100:ff00e6&height=3&section=footer&reversal=true"/>
</p>

<br>

<h1 align="center">
  <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Sparkles.png" width="35"/> 
  Feature Matrix
</h1>

<h3 align="center">Neural Feature Map</h3>

```mermaid
mindmap
  root((Programming Visualization))
    Core Analysis Engine
      AST Parsing
        Python ast Module
        Java javalang
        C pycparser
        C++ Advanced Regex
      Function Detection
        Name Extraction
        Parameter Mapping
        Return Type Inference
        Decorator Chain Analysis
        Async / Await Detection
      Class Extraction
        Inheritance Tree Builder
        Method Enumeration
        Attribute Catalog
        Access Modifier Mapping
        Abstract Class Detection
      Import Analysis
        Dependency Graph
        Library Mapping
        Version Tracking
        Circular Import Detection
        External vs Internal
      Control Flow
        Loop Detection
        Condition Branches
        Exception Handling
        Return Path Analysis
        Break / Continue Tracking
    Visualization Suite
      AST Tree
        Interactive D3.js
        Zoom and Pan
        Collapse / Expand
        Node Color Coding
        Path Highlighting
        Search and Filter
      Call Graph
        NetworkX Directed
        Force-Directed Layout
        Edge Weight Mapping
        Community Detection
        Cluster Coloring
      Flowcharts
        Mermaid SVG Engine
        Execution Paths
        Decision Diamonds
        Loop Cycles
        Parallel Branches
        Export to PNG / SVG
      Metrics Charts
        Plotly Interactive
        Complexity Bar Charts
        Code Composition Pie
        Language Distribution
        Sunburst Hierarchies
        3D Surface (Roadmap)
      Sunburst Charts
        Function Hierarchy
        Class Inheritance
        Module Dependencies
        Drill-Down Navigation
      Line-by-Line
        Execution Trace
        Variable State Changes
        Memory Allocation
        Time per Line
    Explanation Engine
      Beginner Level
        Simple Analogies
        Everyday Concepts
        Step-by-Step Walkthrough
        Visual Metaphors
      Intermediate Level
        Technical Terminology
        Design Patterns
        Code Smells
        Best Practices
      Advanced Level
        Complexity Theory
        Algorithm Analysis
        Architecture Deep Dive
        Optimization Strategies
      Line-by-Line Breakdown
        Every Line Explained
        Variable Purpose
        Side Effects
        Performance Impact
    Report Generation
      HTML Reports
        Styled Templates
        Embedded Charts
        Print Optimized
        Dark / Light Themes
      JSON Reports
        Machine Readable
        API Compatible
        Schema Validated
        Nested Structures
      TXT Reports
        Plain Text Summary
        Quick Export
        CLI Friendly
        Diff Compatible
      PDF Export
        Documentation Ready
        Printable Format
        Page Layout
        Table of Contents
    Platform Features
      Dark Mode
        Glassmorphism Cards
        Neon Accent Colors
        OLED Black Background
        Reduced Eye Strain
      Light Mode
        Clean White Theme
        Soft Shadows
        High Contrast
        Print Friendly
      Responsive Design
        Mobile First
        Tablet Optimized
        Desktop Enhanced
        Touch Gestures
      History and Persistence
        JSON File Storage
        Auto-Save Analysis
        Revisit Past Work
        Delete and Manage
      Theme System
        Session Persistence
        API Toggle
        Instant Switch
        Cookie Storage
    Security and Performance
      File Validation
        Extension Whitelist
        MIME Type Check
        Size Limit 16MB
        Malware Scanning
      Speed Optimization
        Lazy Loading
        Chart Caching
        Async Processing
        Memory Management
      Error Handling
        Graceful Degradation
        Flash Messages
        Logging System
        Traceback Capture
```

<br>

<h3 align="center">Feature Completeness Radar</h3>

```mermaid
pie showData
    title Language Support Distribution
    "Python" : 95
    "Java" : 30
    "C" : 15
    "C++" : 10
```

<br>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=rect&color=0:ff00e6,50:00ff88,100:00f2ff&height=3&section=footer&reversal=true"/>
</p>

<br>

<h1 align="center">
  <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Rocket.png" width="35"/> 
  Installation
</h1>

<h3 align="center">Deployment Architecture</h3>

```mermaid
graph TB
    subgraph DEV["DEVELOPMENT"]
        D1["Git Clone"]
        D2["Virtual Env"]
        D3["pip install"]
        D4["python app.py"]
        D5["localhost:5000"]
    end

    subgraph DOCKER["DOCKER"]
        DO1["docker build"]
        DO2["docker run"]
        DO3["localhost:7860"]
    end

    subgraph HF["HUGGING FACE"]
        H1["Create Space"]
        H2["Docker SDK"]
        H3["git push"]
        H4["Auto Deploy"]
    end

    subgraph CLOUD["CLOUD"]
        C1["AWS / GCP / Azure"]
        C2["Docker Container"]
        C3["Load Balancer"]
        C4["SSL / HTTPS"]
    end

    D1 --> D2 --> D3 --> D4 --> D5
    DO1 --> DO2 --> DO3
    H1 --> H2 --> H3 --> H4
    C1 --> C2 --> C3 --> C4

    classDef dev fill:#0a0a1a,stroke:#00f2ff,stroke-width:2px,color:#fff
    classDef docker fill:#0a0a1a,stroke:#00ff88,stroke-width:2px,color:#fff
    classDef hf fill:#0a0a1a,stroke:#ff00e6,stroke-width:2px,color:#fff
    classDef cloud fill:#0a0a1a,stroke:#7000ff,stroke-width:2px,color:#fff
    class D1,D2,D3,D4,D5 dev
    class DO1,DO2,DO3 docker
    class H1,H2,H3,H4 hf
    class C1,C2,C3,C4 cloud
```

<br>

<h3 align="center">Quick Start — One Command Install</h3>

```bash
# Clone the neural engine
git clone https://github.com/issu321/Programming-Visualization.git
cd Programming-Visualization

# Windows
install.bat

# Linux / Mac
chmod +x install.sh && ./install.sh

# Docker
docker build -t programming-visualization .
docker run -p 7860:7860 programming-visualization

# Open Browser
# http://localhost:5000   (Local)
# http://localhost:7860   (Docker)
```

<br>

<h3 align="center">Manual Installation Steps</h3>

```mermaid
journey
    title Installation Journey
    section Clone
      Clone Repo: 5: User
    section Environment
      Create Venv: 5: System
      Activate Venv: 5: User
    section Dependencies
      Install Requirements: 5: System
      Verify Packages: 4: System
    section Launch
      Run App: 5: User
      Open Browser: 5: User
    section Verify
      Test Analyzer: 5: User
      Check Dashboard: 5: User
```

<br>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=rect&color=0:00ff88,50:00f2ff,100:7000ff&height=3&section=footer&reversal=true"/>
</p>

<br>

<h1 align="center">
  <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Satellite%20Antenna.png" width="35"/> 
  API Documentation
</h1>

<h3 align="center">API Request / Response Lifecycle</h3>

```mermaid
sequenceDiagram
    autonumber
    participant CLIENT as Client / Browser
    participant FLASK as Flask Server
    participant ANALYZER as analyzers.py
    participant VIZ as visualizer.py
    participant JSON as JSON Storage

    rect rgb(10,10,26)
        Note over CLIENT,JSON: POST /api/analyze
    end

    CLIENT->>FLASK: POST /api/analyze
    FLASK->>FLASK: detect_language(code, filename)
    FLASK->>ANALYZER: analyze_code(code, filename)

    rect rgb(20,10,30)
        Note over ANALYZER: AST Parsing Phase
    end

    ANALYZER->>ANALYZER: Parse AST (Language Specific)
    ANALYZER->>ANALYZER: Extract Functions
    ANALYZER->>ANALYZER: Extract Classes
    ANALYZER->>ANALYZER: Calculate Complexity
    ANALYZER->>ANALYZER: Map Dependencies
    ANALYZER-->>FLASK: analysis_result

    rect rgb(10,26,10)
        Note over VIZ: Visualization Phase
    end

    FLASK->>VIZ: generate_all_visualizations()
    VIZ->>VIZ: Plotly Charts
    VIZ->>VIZ: NetworkX Graphs
    VIZ->>VIZ: Mermaid Flowcharts
    VIZ->>VIZ: D3.js AST Trees
    VIZ-->>FLASK: visualizations

    rect rgb(26,10,10)
        Note over JSON: Persistence Phase
    end

    FLASK->>JSON: _save_analysis()
    JSON-->>FLASK: analysis_id

    rect rgb(10,10,40)
        Note over CLIENT,FLASK: Response Delivery
    end

    FLASK-->>CLIENT: 200 OK JSON Response

    CLIENT->>FLASK: GET /visualization/42
    FLASK->>JSON: _get_analysis_by_id(42)
    JSON-->>FLASK: analysis
    FLASK-->>CLIENT: Render visualization.html
```

<br>

<h3 align="center">Endpoint Reference</h3>

| Method | Endpoint | Description | Auth |
|:------:|:---------|:------------|:----:|
| `GET` | `/` | Home Page with Stats | Public |
| `GET` | `/analyzer` | Code Input Interface | Public |
| `POST` | `/analyze` | Submit Code for Analysis | Public |
| `GET` | `/visualization/<id>` | View Analysis Results | Public |
| `GET` | `/dashboard` | Analysis History | Public |
| `GET` | `/reports` | Report Management | Public |
| `GET` | `/database` | Stats and Data View | Public |
| `POST` | `/api/analyze` | REST API Analysis | Public |
| `GET` | `/api/stats` | Platform Statistics | Public |
| `POST` | `/api/theme` | Toggle Theme | Public |

<br>

<h3 align="center">Sample API Request</h3>

```json
// REQUEST: POST /api/analyze
{
  "code": "def fibonacci(n):\n    if n <= 1:\n        return n\n    return fibonacci(n-1) + fibonacci(n-2)",
  "filename": "fibonacci.py"
}

// RESPONSE: 200 OK
{
  "success": true,
  "analysis_id": 42,
  "analysis": {
    "detected_language": "python",
    "functions": [
      {
        "name": "fibonacci",
        "parameters": ["n"],
        "return_type": "inferred",
        "complexity": "O(2^n)"
      }
    ],
    "classes": [],
    "complexity": {
      "cyclomatic": 2,
      "cognitive": 3
    }
  },
  "visualizations": {
    "ast_tree": { "nodes": [...], "edges": [...] },
    "call_graph": { "nodes": [...], "edges": [...] },
    "flowchart": "graph TD; A[Start] --> B{n <= 1}; ...",
    "complexity_chart": { "data": [{"x": ["fibonacci"], "y": [2], "type": "bar"}] }
  }
}
```

<br>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=rect&color=0:00f2ff,50:7000ff,100:ff00e6&height=3&section=footer&reversal=true"/>
</p>

<br>

<h1 align="center">
  <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/File%20Folder.png" width="35"/> 
  Project Structure
</h1>

<h3 align="center">File Tree with Neural Connections</h3>

```mermaid
graph TD
    ROOT["Programming-Visualization/"] --> APP["app.py - Flask Application"]
    ROOT --> ANA["analyzers.py - Code Analysis Engine"]
    ROOT --> VIZ["visualizer.py - Visualization Generator"]
    ROOT --> REQ["requirements.txt - Python Dependencies"]
    ROOT --> DOCK["Dockerfile - Container Config"]
    ROOT --> INST1["install.bat - Windows Installer"]
    ROOT --> INST2["install.sh - Linux Installer"]
    ROOT --> README["README.md - This File"]
    ROOT --> LICENSE["LICENSE - MIT License"]

    ROOT --> TEMPLATES["templates/ - Jinja2 HTML Templates"]
    ROOT --> STATIC["static/ - CSS / JS / Images"]
    ROOT --> UPLOADS["uploads/ - Uploaded Code Files"]
    ROOT --> REPORTS["reports/ - Generated Reports"]
    ROOT --> DATA["data/ - JSON Storage"]

    TEMPLATES --> T1["base.html - Base Layout"]
    TEMPLATES --> T2["home.html - Landing Page"]
    TEMPLATES --> T3["analyzer.html - Code Input"]
    TEMPLATES --> T4["visualization.html - Results and Charts"]
    TEMPLATES --> T5["dashboard.html - History and Stats"]
    TEMPLATES --> T6["reports.html - Report Manager"]
    TEMPLATES --> T7["database.html - Data View"]
    TEMPLATES --> T8["features.html - Feature Showcase"]
    TEMPLATES --> T9["contact.html - Contact Page"]

    STATIC --> CSS["css/"]
    STATIC --> JS["js/"]
    STATIC --> IMG["images/"]

    CSS --> C1["style.css - Glassmorphism + Neon Theme"]
    JS --> J1["main.js - Interactivity + Theme Toggle"]

    DATA --> D1["analyses.json - Analysis Results"]
    DATA --> D2["files.json - Upload Metadata"]
    DATA --> D3["reports.json - Report History"]

    APP --> TEMPLATES
    APP --> STATIC
    APP --> DATA
    ANA --> APP
    VIZ --> APP

    classDef root fill:#0a0a1a,stroke:#00f2ff,stroke-width:4px,color:#fff
    classDef app fill:#0a0a1a,stroke:#ff00e6,stroke-width:3px,color:#fff
    classDef ana fill:#0a0a1a,stroke:#7000ff,stroke-width:3px,color:#fff
    classDef viz fill:#0a0a1a,stroke:#00ff88,stroke-width:3px,color:#fff
    classDef templates fill:#0a0a1a,stroke:#00f2ff,stroke-width:2px,color:#fff
    classDef static fill:#0a0a1a,stroke:#ff00e6,stroke-width:2px,color:#fff
    classDef data fill:#0a0a1a,stroke:#00ff88,stroke-width:2px,color:#fff
    class ROOT root
    class APP app
    class ANA ana
    class VIZ viz
    class TEMPLATES templates
    class STATIC static
    class DATA data
```

<br>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=rect&color=0:ff00e6,50:00f2ff,100:7000ff&height=3&section=footer&reversal=true"/>
</p>

<br>

<h1 align="center">
  <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Floppy%20Disk.png" width="35"/> 
  Data Schema
</h1>

<h3 align="center">JSON Storage Entity Relationship</h3>

```mermaid
erDiagram
    ANALYSIS ||--o{ FILE : contains
    ANALYSIS ||--o{ REPORT : generates
    FILE ||--o{ ANALYSIS : triggers

    ANALYSIS {
        int id PK
        int user_id
        string filename
        string language
        string code
        json analysis_result
        json visualizations
        datetime created_at
    }

    FILE {
        int id PK
        int user_id
        string filename
        string filepath
        string language
        int file_size
        datetime uploaded_at
    }

    REPORT {
        int id PK
        int user_id
        int analysis_id FK
        string report_type
        string filepath
        datetime created_at
    }
```

<br>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=rect&color=0:7000ff,50:ff00e6,100:00ff88&height=3&section=footer&reversal=true"/>
</p>

<br>

<h1 align="center">
  <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Video%20Game.png" width="35"/> 
  Usage Guide
</h1>

<h3 align="center">User Journey Map</h3>

```mermaid
journey
    title Complete User Journey
    section Upload
      Paste Code: 5: User
      Upload File: 5: User
      Drag and Drop: 4: User
    section Analyze
      Auto Detect Language: 5: System
      Parse AST: 5: System
      Extract Metrics: 5: System
      Generate Visualizations: 5: System
    section Explore
      View AST Tree: 5: User
      Explore Call Graph: 4: User
      Check Flowchart: 5: User
      Read Explanations: 5: User
    section Export
      Download HTML Report: 5: User
      Download JSON Data: 4: User
      Download TXT Summary: 4: User
    section History
      Save to Dashboard: 5: System
      View Past Analyses: 5: User
      Compare Results: 3: User
```

<br>

<h3 align="center">Navigation Flowchart</h3>

```mermaid
flowchart TD
    HOME["Home /"] --> ANALYZER["Analyzer /analyzer"]
    HOME --> FEATURES["Features /features"]
    HOME --> CONTACT["Contact /contact"]

    ANALYZER --> ANALYZE["Analyze POST /analyze"]
    ANALYZE --> VISUALIZATION["Visualization /visualization/id"]

    VISUALIZATION --> DASHBOARD["Dashboard /dashboard"]
    VISUALIZATION --> REPORTS["Reports /reports"]
    VISUALIZATION --> API["API /api/analyze"]

    DASHBOARD --> DATABASE["Data View /database"]
    DASHBOARD --> ANALYZER

    REPORTS --> GENERATE["Generate /generate_report/id/type"]
    GENERATE --> DOWNLOAD["Download HTML / JSON / TXT"]

    API --> JSON_RESPONSE["JSON Response"]

    HOME --> THEME["Theme Toggle POST /api/theme"]
    THEME --> HOME

    classDef home fill:#0a0a1a,stroke:#00f2ff,stroke-width:3px,color:#fff
    classDef analyzer fill:#0a0a1a,stroke:#7000ff,stroke-width:2px,color:#fff
    classDef viz fill:#0a0a1a,stroke:#ff00e6,stroke-width:3px,color:#fff
    classDef dash fill:#0a0a1a,stroke:#00ff88,stroke-width:2px,color:#fff
    classDef reports fill:#0a0a1a,stroke:#00f2ff,stroke-width:2px,color:#fff
    classDef api fill:#0a0a1a,stroke:#ff00e6,stroke-width:2px,color:#fff
    class HOME home
    class ANALYZER analyzer
    class VISUALIZATION viz
    class DASHBOARD dash
    class REPORTS reports
    class API api
```

<br>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=rect&color=0:00ff88,50:7000ff,100:00f2ff&height=3&section=footer&reversal=true"/>
</p>

<br>

<h1 align="center">
  <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Hammer%20and%20Wrench.png" width="35"/> 
  Technology Stack
</h1>

<h3 align="center">Full Stack Neural Network</h3>

```mermaid
graph TB
    subgraph BACKEND["BACKEND CORE"]
        B1["Python 3.11+ - Core Language"]
        B2["Flask 3.0.0 - Web Framework"]
        B3["Werkzeug 3.0.1 - WSGI Utilities"]
        B4["Jinja2 - Template Engine"]
        B5["JSON Storage - File-based Persistence"]
    end

    subgraph PARSERS["LANGUAGE PARSERS"]
        P1["ast - Python Built-in AST Generation"]
        P2["javalang 0.13.0 - Java Parser"]
        P3["pycparser 2.21 - C Parser"]
        P4["Regex Engine - C++ Heuristics"]
    end

    subgraph VIZLIBS["VISUALIZATION LIBRARIES"]
        V1["Plotly 5.18.0 - Interactive Charts"]
        V2["NetworkX 3.2.1 - Graph Algorithms"]
        V3["Mermaid 10.x - Flowchart Engine"]
        V4["D3.js CDN - Tree Visualization"]
    end

    subgraph FRONTEND["FRONTEND"]
        F1["HTML5 - Semantic Structure"]
        F2["CSS3 - Glassmorphism + Neon Animations"]
        F3["JavaScript - Vanilla Interactivity"]
        F4["Font Awesome - Icon System"]
        F5["Google Fonts - JetBrains Mono Typography"]
    end

    subgraph DESIGN["DESIGN SYSTEM"]
        D1["Glassmorphism - Frosted Glass Backdrop Blur"]
        D2["Claymorphism - Soft 3D Shadows Rounded Depth"]
        D3["Neon Theme - Cyan #00f2ff + Magenta #ff00e6"]
        D4["Dark / Light Mode - Session Persistence Instant Toggle"]
    end

    B1 --> B2
    B2 --> B3
    B3 --> B4
    B4 --> B5
    B2 --> P1
    B2 --> P2
    B2 --> P3
    B2 --> P4
    P1 --> V1
    P2 --> V2
    P3 --> V3
    P4 --> V4
    V1 --> F1
    V2 --> F2
    V3 --> F3
    V4 --> F3
    F1 --> D1
    F2 --> D2
    F3 --> D3
    D1 --> D4
    D2 --> D4
    D3 --> D4

    classDef backend fill:#0a0a1a,stroke:#00f2ff,stroke-width:3px,color:#fff
    classDef parsers fill:#0a0a1a,stroke:#7000ff,stroke-width:3px,color:#fff
    classDef vizlibs fill:#0a0a1a,stroke:#ff00e6,stroke-width:3px,color:#fff
    classDef frontend fill:#0a0a1a,stroke:#00ff88,stroke-width:3px,color:#fff
    classDef design fill:#0a0a1a,stroke:#00f2ff,stroke-width:3px,color:#fff
    class B1,B2,B3,B4,B5 backend
    class P1,P2,P3,P4 parsers
    class V1,V2,V3,V4 vizlibs
    class F1,F2,F3,F4,F5 frontend
    class D1,D2,D3,D4 design
```

<br>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=rect&color=0:00f2ff,50:ff00e6,100:00ff88&height=3&section=footer&reversal=true"/>
</p>

<br>

<h1 align="center">
  <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Travel%20and%20places/Compass.png" width="35"/> 
  Roadmap
</h1>

<h3 align="center">Development Timeline</h3>

```mermaid
graph LR
    subgraph DONE["COMPLETED"]
        D1["Flask Backend"]
        D2["JSON Storage"]
        D3["Multi-Language Parser"]
        D4["Theme System"]
        D5["Plotly Charts"]
        D6["NetworkX Graphs"]
        D7["Mermaid Flowcharts"]
        D8["Docker Deploy"]
        D9["Hugging Face Spaces"]
    end

    subgraph ACTIVE["IN PROGRESS"]
        A1["D3.js AST Trees"]
        A2["Complexity Predictor"]
    end

    subgraph FUTURE["PLANNED"]
        F1["3D Code City"]
        F2["Code Smell Detector"]
        F3["Auto-Refactor Suggest"]
        F4["Natural Language Query"]
        F5["User Authentication"]
        F6["Cloud Scaling"]
    end

    D1 --> D2 --> D3 --> D4 --> D5 --> D6 --> D7 --> D8 --> D9
    D9 --> A1 --> A2
    A2 --> F1 --> F2 --> F3 --> F4 --> F5 --> F6

    classDef done fill:#001a00,stroke:#00ff88,stroke-width:2px,color:#fff
    classDef active fill:#1a1a00,stroke:#ffcc00,stroke-width:2px,color:#fff
    classDef future fill:#0a0a1a,stroke:#7000ff,stroke-width:2px,color:#fff
    class D1,D2,D3,D4,D5,D6,D7,D8,D9 done
    class A1,A2 active
    class F1,F2,F3,F4,F5,F6 future
```

<br>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=rect&color=0:ff00e6,50:7000ff,100:00f2ff&height=3&section=footer&reversal=true"/>
</p>

<br>

<h1 align="center">
  <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Handshake.png" width="35"/> 
  Contributing
</h1>

<h3 align="center">Contribution Workflow</h3>

```mermaid
graph LR
    subgraph FORK["FORK AND BRANCH"]
        F1["Fork Repository on GitHub"]
        F2["Clone Fork: git clone"]
        F3["Create Branch: feature/xyz"]
    end

    subgraph CODE["DEVELOP"]
        C1["Write Code"]
        C2["Run Tests"]
        C3["Commit: git commit -m"]
    end

    subgraph PUSH["SUBMIT"]
        P1["Push to Origin: git push"]
        P2["Open Pull Request"]
        P3["Code Review"]
    end

    subgraph MERGE["MERGE"]
        M1["Approve and Merge"]
        M2["Deploy to Production"]
        M3["Celebrate!"]
    end

    F1 --> F2 --> F3 --> C1 --> C2 --> C3 --> P1 --> P2 --> P3 --> M1 --> M2 --> M3

    classDef fork fill:#0a0a1a,stroke:#00f2ff,stroke-width:2px,color:#fff
    classDef code fill:#0a0a1a,stroke:#7000ff,stroke-width:2px,color:#fff
    classDef push fill:#0a0a1a,stroke:#ff00e6,stroke-width:2px,color:#fff
    classDef merge fill:#0a0a1a,stroke:#00ff88,stroke-width:2px,color:#fff
    class F1,F2,F3 fork
    class C1,C2,C3 code
    class P1,P2,P3 push
    class M1,M2,M3 merge
```

<br>

<h3 align="center">Git History Visualization</h3>

```mermaid
graph LR
    subgraph GIT["GIT BRANCHING MODEL"]
        MAIN["main"]
        F1["feature/ast-parser"]
        F2["feature/visualizations"]
        F3["feature/json-storage"]
        F4["feature/themes"]
    end

    MAIN --> C1["Initial Commit"]
    MAIN --> C2["Flask Setup"]
    C2 --> F1
    F1 --> C3["Python AST"]
    F1 --> C4["Java Parser"]
    F1 --> C5["C Parser"]
    C5 --> MR1["Merge AST"]
    MR1 --> MAIN2["main"]
    MAIN2 --> F2
    F2 --> C6["Plotly Charts"]
    F2 --> C7["NetworkX Graphs"]
    F2 --> C8["Mermaid Flowcharts"]
    C8 --> MR2["Merge Viz"]
    MR2 --> MAIN3["main"]
    MAIN3 --> F3
    F3 --> C9["Remove SQLite"]
    F3 --> C10["JSON Engine"]
    C10 --> MR3["Merge JSON"]
    MR3 --> MAIN4["main"]
    MAIN4 --> F4
    F4 --> C11["Dark Mode"]
    F4 --> C12["Light Mode"]
    C12 --> MR4["Merge Themes"]
    MR4 --> MAIN5["main"]
    MAIN5 --> C13["v1.0 Release"]

    classDef main fill:#0a0a1a,stroke:#00f2ff,stroke-width:3px,color:#fff
    classDef feat fill:#0a0a1a,stroke:#7000ff,stroke-width:2px,color:#fff
    classDef commit fill:#0a0a1a,stroke:#00ff88,stroke-width:2px,color:#fff
    classDef merge fill:#0a0a1a,stroke:#ff00e6,stroke-width:2px,color:#fff
    class MAIN,MAIN2,MAIN3,MAIN4,MAIN5 main
    class F1,F2,F3,F4 feat
    class C1,C2,C3,C4,C5,C6,C7,C8,C9,C10,C11,C12,C13 commit
    class MR1,MR2,MR3,MR4 merge
```

<br>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=rect&color=0:00f2ff,50:7000ff,100:ff00e6&height=3&section=footer&reversal=true"/>
</p>

<br>

<h1 align="center">
  <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Stopwatch.png" width="35"/> 
  Performance
</h1>

<h3 align="center">Benchmark Results</h3>

```mermaid
graph LR
    subgraph BENCH["PARSING SPEED BENCHMARKS"]
        B1["Python AST: ~50ms - Ultra Fast"]
        B2["Java Parse: ~120ms - Fast"]
        B3["C Parse: ~80ms - Fast"]
        B4["C++ Parse: ~150ms - Fast"]
        B5["Plotly Render: ~200ms - Smooth"]
        B6["NetworkX Graph: ~100ms - Smooth"]
        B7["Mermaid Flowchart: ~80ms - Ultra Fast"]
        B8["D3.js Tree: ~250ms - Smooth"]
    end

    classDef bench fill:#0a0a1a,stroke:#00ff88,stroke-width:3px,color:#fff
    class B1,B2,B3,B4,B5,B6,B7,B8 bench
```

<br>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=rect&color=0:7000ff,50:ff00e6,100:00ff88&height=3&section=footer&reversal=true"/>
</p>

<br>

<h1 align="center">
  <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Shield.png" width="35"/> 
  Security
</h1>

<h3 align="center">Security Architecture</h3>

```mermaid
graph TD
    subgraph SEC["SECURITY LAYERS"]
        S1["Input Validation: File Extension Whitelist, MIME Type Check, Size Limit 16MB"]
        S2["Secret Management: ENV Variables, Session Keys, CSRF Protection"]
        S3["File Sanitization: Secure Filename, UUID Prefix, Path Traversal Block"]
        S4["Error Handling: No Stack Trace Leak, Flash Messages, Logging Only"]
        S5["CORS and Headers: Content Security Policy, X-Frame-Options, Secure Cookies"]
    end

    classDef sec fill:#0a0a1a,stroke:#00f2ff,stroke-width:3px,color:#fff
    class S1,S2,S3,S4,S5 sec
```

<br>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=rect&color=0:00ff88,50:00f2ff,100:7000ff&height=3&section=footer&reversal=true"/>
</p>

<br>

<h1 align="center">
  <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Bug.png" width="35"/> 
  Error Handling
</h1>

<h3 align="center">Error Recovery Flow</h3>

```mermaid
flowchart TD
    START([User Action]) --> TRY{Try Block}

    TRY -->|Success| PROCESS[Process Request]
    PROCESS --> RETURN[Return Response]
    RETURN --> END([Success])

    TRY -->|Exception| CATCH{Catch Block}

    CATCH -->|ValueError| VAL_ERR["Invalid Input - Flash Warning"]
    CATCH -->|FileNotFound| FILE_ERR["File Missing - Flash Error"]
    CATCH -->|JSONDecode| JSON_ERR["Corrupt Data - Reset to Default"]
    CATCH -->|Unhandled| UNK_ERR["Server Error - Log Traceback"]

    VAL_ERR --> REDIRECT[Redirect to Safe Page]
    FILE_ERR --> REDIRECT
    JSON_ERR --> REDIRECT
    UNK_ERR --> REDIRECT

    REDIRECT --> END2([Recovery])

    classDef start fill:#0a0a1a,stroke:#00f2ff,stroke-width:2px,color:#fff
    classDef end fill:#001a00,stroke:#00ff88,stroke-width:3px,color:#fff
    classDef end2 fill:#1a1a00,stroke:#ffcc00,stroke-width:2px,color:#fff
    classDef val fill:#1a1a00,stroke:#ffcc00,stroke-width:2px,color:#fff
    classDef file fill:#1a0a00,stroke:#ff8800,stroke-width:2px,color:#fff
    classDef json fill:#1a001a,stroke:#ff00e6,stroke-width:2px,color:#fff
    classDef unk fill:#1a0000,stroke:#ff0044,stroke-width:2px,color:#fff
    class START start
    class END end
    class END2 end2
    class VAL_ERR val
    class FILE_ERR file
    class JSON_ERR json
    class UNK_ERR unk
```

<br>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=rect&color=0:00f2ff,50:ff00e6,100:7000ff&height=3&section=footer&reversal=true"/>
</p>

<br>

<h1 align="center">
  <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Scroll.png" width="35"/> 
  License
</h1>

<div align="center">

```
MIT License

Copyright (c) 2024 issu321 (Mohammed Usman)

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
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
```

</div>

<br>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=rect&color=0:7000ff,50:00f2ff,100:ff00e6&height=3&section=footer&reversal=true"/>
</p>

<br>

<h1 align="center">
  <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/People/Man%20Technologist.png" width="35"/> 
  Developer
</h1>

<div align="center">

<table>
  <tr>
    <td align="center" width="600">
      <br>
      <img src="https://img.shields.io/badge/issu321-00f2ff?style=for-the-badge&logo=github&logoColor=white&labelColor=0a0a1a"/><br>
      <img src="https://img.shields.io/badge/Mohammed%20Usman-ff00e6?style=for-the-badge&logo=linkedin&logoColor=white&labelColor=0a0a1a"/><br><br>
      <b style="font-size:20px; color:#00f2ff;">AI Developer &nbsp;&bull;&nbsp; Viz Engineer &nbsp;&bull;&nbsp; Open Source</b><br><br>
      <a href="https://github.com/issu321">
        <img src="https://img.shields.io/badge/GitHub-issu321-00f2ff?style=for-the-badge&logo=github&logoColor=white&labelColor=0a0a1a"/>
      </a>
      <a href="https://github.com/issu321/Programming-Visualization">
        <img src="https://img.shields.io/badge/Repo-Programming--Visualization-ff00e6?style=for-the-badge&logo=github&logoColor=white&labelColor=0a0a1a"/>
      </a>
      <br><br>
    </td>
  </tr>
</table>

<br>

<img src="https://github-readme-stats.vercel.app/api?username=issu321&show_icons=true&theme=radical&hide_border=true&bg_color=0a0a1a&title_color=00f2ff&text_color=ffffff&icon_color=ff00e6&border_radius=15" width="450"/>
<img src="https://github-readme-stats.vercel.app/api/top-langs/?username=issu321&layout=compact&theme=radical&hide_border=true&bg_color=0a0a1a&title_color=00f2ff&text_color=ffffff&icon_color=ff00e6&border_radius=15" width="350"/>

<br><br>

<img src="https://github-profile-trophy.vercel.app/?username=issu321&theme=radical&no-frame=true&no-bg=true&margin-w=10&column=7" width="800"/>

</div>

<br>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=rect&color=0:00f2ff,50:ff00e6,100:7000ff&height=3&section=footer&reversal=true"/>
</p>

<br>

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:00f2ff,50:7000ff,100:ff00e6&height=120&section=footer&text=Star%20this%20repo%20if%20you%20find%20it%20useful!&fontSize=20&fontColor=ffffff&fontAlignY=65&animation=twinkling"/>

<br><br>

**Built with love, fire, and a lot of coffee by Mohammed Usman**

*Transforming code into cognition, one visualization at a time.*

<br>

<p>
  <img src="https://img.shields.io/badge/Made%20with-Flask-00f2ff?style=for-the-badge&logo=flask&logoColor=white&labelColor=0a0a1a"/>
  <img src="https://img.shields.io/badge/Powered%20by-AI-ff00e6?style=for-the-badge&logo=openai&logoColor=white&labelColor=0a0a1a"/>
  <img src="https://img.shields.io/badge/Designed%20with-Love-00ff88?style=for-the-badge&logo=heart&logoColor=white&labelColor=0a0a1a"/>
</p>

<br><br>

<img src="https://komarev.com/ghpvc/?username=issu321&style=for-the-badge&color=00f2ff&label=Profile+Views&labelColor=0a0a1a"/>

<br><br>

<img src="https://raw.githubusercontent.com/issu321/issu321/output/github-contribution-grid-snake.svg" width="800"/>

</div>
