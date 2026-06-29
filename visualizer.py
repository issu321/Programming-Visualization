"""
Visualization Engine for Programming Visualization Platform
Generates interactive charts, graphs, flowcharts, and AST visualizations.
"""

import json
import base64
import io
import re
from typing import Dict, List, Any, Optional
import plotly.graph_objects as go
import plotly.express as px
from plotly.utils import PlotlyJSONEncoder
import networkx as nx


class CodeVisualizer:
    """Main visualization engine for code analysis results."""

    def __init__(self, analysis_result: Dict[str, Any]):
        self.result = analysis_result
        self.language = analysis_result.get('detected_language', 'unknown')

    def generate_all_visualizations(self) -> Dict[str, Any]:
        """Generate all available visualizations with error handling."""
        visualizations = {}

        viz_methods = [
            ("ast_tree", self.generate_ast_tree, lambda: self.language == "python" and self.result.get("ast_valid")),
            ("call_graph", self.generate_call_graph, None),
            ("function_hierarchy", self.generate_function_hierarchy, None),
            ("complexity_chart", self.generate_complexity_chart, None),
            ("metrics_chart", self.generate_metrics_chart, None),
            ("flowchart", self.generate_flowchart, None),
            ("dependency_graph", self.generate_dependency_graph, None),
            ("class_hierarchy", self.generate_class_hierarchy, lambda: bool(self.result.get("classes"))),
        ]

        for name, method, condition in viz_methods:
            try:
                if condition is not None and not condition():
                    continue
                visualizations[name] = method()
            except Exception as e:
                visualizations[name] = {"error": f"Visualization failed: {str(e)}"}

        return visualizations

    def generate_ast_tree(self) -> Dict[str, Any]:
        """Generate interactive AST tree visualization using Plotly."""
        try:
            import ast
            code = self.result.get('raw_code', '')
            if not code:
                return {'error': 'No code available'}

            tree = ast.parse(code)

            # Build tree structure for visualization
            nodes = []
            edges = []
            node_ids = {}
            counter = [0]

            def add_node(node, parent_id=None, depth=0):
                node_id = counter[0]
                counter[0] += 1
                node_ids[id(node)] = node_id

                label = type(node).__name__
                if isinstance(node, ast.Name):
                    label += f"\n({node.id})"
                elif isinstance(node, ast.Constant):
                    label += f"\n({repr(node.value)[:30]})"
                elif isinstance(node, ast.FunctionDef):
                    label += f"\n({node.name})"
                elif isinstance(node, ast.ClassDef):
                    label += f"\n({node.name})"

                nodes.append({
                    'id': node_id,
                    'label': label,
                    'depth': depth,
                    'type': type(node).__name__
                })

                if parent_id is not None:
                    edges.append({'source': parent_id, 'target': node_id})

                for child in ast.iter_child_nodes(node):
                    add_node(child, node_id, depth + 1)

            add_node(tree)

            # Create tree layout using NetworkX
            G = nx.DiGraph()
            for node in nodes:
                G.add_node(node['id'], label=node['label'])
            for edge in edges:
                G.add_edge(edge['source'], edge['target'])

            # Use hierarchical layout (fallback to spring if pygraphviz unavailable)
            try:
                pos = nx.nx_agraph.graphviz_layout(G, prog='dot')
            except Exception:
                pos = nx.spring_layout(G, k=2, iterations=50, seed=42)

            # Create Plotly figure
            edge_x = []
            edge_y = []
            for edge in edges:
                x0, y0 = pos[edge['source']]
                x1, y1 = pos[edge['target']]
                edge_x.extend([x0, x1, None])
                edge_y.extend([y0, y1, None])

            node_x = [pos[n['id']][0] for n in nodes]
            node_y = [pos[n['id']][1] for n in nodes]
            node_text = [n['label'] for n in nodes]
            node_colors = [n['depth'] for n in nodes]

            fig = go.Figure()

            fig.add_trace(go.Scatter(
                x=edge_x, y=edge_y,
                mode='lines',
                line=dict(color='#888', width=1),
                hoverinfo='none'
            ))

            fig.add_trace(go.Scatter(
                x=node_x, y=node_y,
                mode='markers+text',
                marker=dict(
                    size=30,
                    color=node_colors,
                    colorscale='Viridis',
                    showscale=True,
                    colorbar=dict(title='Depth')
                ),
                text=node_text,
                textposition="top center",
                textfont=dict(size=8),
                hovertemplate='%{text}<extra></extra>'
            ))

            fig.update_layout(
                title=dict(text='Abstract Syntax Tree', font=dict(color='#f1f5f9', size=16)),
                showlegend=False,
                xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                height=600,
                font=dict(color='#f1f5f9')
            )

            return json.loads(json.dumps(fig, cls=PlotlyJSONEncoder))

        except Exception as e:
            return {'error': str(e)}

    def generate_call_graph(self) -> Dict[str, Any]:
        """Generate function call graph using NetworkX and Plotly."""
        functions = self.result.get('functions', [])
        if not functions:
            return {'error': 'No functions found'}

        G = nx.DiGraph()

        # Add all functions as nodes
        for func in functions:
            G.add_node(func['name'], 
                      complexity=func.get('complexity', 1),
                      lines=func.get('body_lines', 0))

        # Add edges for function calls
        for func in functions:
            for call in func.get('calls', []):
                if call in G.nodes() and call != func['name']:
                    G.add_edge(func['name'], call)

        if len(G.nodes()) == 0:
            return {'error': 'No callable functions found'}

        # Layout
        pos = nx.spring_layout(G, k=2, iterations=50, seed=42)

        # Edge traces
        edge_x = []
        edge_y = []
        for edge in G.edges():
            x0, y0 = pos[edge[0]]
            x1, y1 = pos[edge[1]]
            edge_x.extend([x0, x1, None])
            edge_y.extend([y0, y1, None])

        # Node traces
        node_x = [pos[node][0] for node in G.nodes()]
        node_y = [pos[node][1] for node in G.nodes()]
        node_sizes = [G.nodes[node].get('complexity', 1) * 20 + 20 for node in G.nodes()]
        node_colors = [G.nodes[node].get('complexity', 1) for node in G.nodes()]

        fig = go.Figure()

        fig.add_trace(go.Scatter(
            x=edge_x, y=edge_y,
            mode='lines',
            line=dict(color='#7c3aed', width=2),
            hoverinfo='none'
        ))

        fig.add_trace(go.Scatter(
            x=node_x, y=node_y,
            mode='markers+text',
            marker=dict(
                size=node_sizes,
                color=node_colors,
                colorscale='Plasma',
                showscale=True,
                line=dict(width=2, color='white')
            ),
            text=list(G.nodes()),
            textposition="top center",
            hovertemplate='<b>%{text}</b><br>Complexity: %{marker.color}<extra></extra>'
        ))

        fig.update_layout(
            title=dict(text='Function Call Graph', font=dict(color='#f1f5f9', size=16)),
            showlegend=False,
            xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
            yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            height=500,
            font=dict(color='#f1f5f9')
        )

        return json.loads(json.dumps(fig, cls=PlotlyJSONEncoder))

    def generate_function_hierarchy(self) -> Dict[str, Any]:
        """Generate function hierarchy tree."""
        functions = self.result.get('functions', [])
        if not functions:
            return {'error': 'No functions found'}

        # Build hierarchy data
        hierarchy_data = []
        for func in functions:
            hierarchy_data.append({
                'name': func['name'],
                'parent': '',
                'value': func.get('complexity', 1),
                'lines': func.get('body_lines', 0)
            })
            for call in func.get('calls', []):
                if any(f['name'] == call for f in functions):
                    hierarchy_data.append({
                        'name': call,
                        'parent': func['name'],
                        'value': 1,
                        'lines': 0
                    })

        if not hierarchy_data:
            return {'error': 'No hierarchy data'}

        # Create sunburst chart
        fig = px.sunburst(
            hierarchy_data,
            names='name',
            parents='parent',
            values='value',
            color='value',
            color_continuous_scale='Viridis',
            title='Function Hierarchy'
        )

        fig.update_layout(
            title=dict(text='Function Hierarchy', font=dict(color='#f1f5f9', size=16)),
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            height=500,
            font=dict(color='#f1f5f9')
        )

        return json.loads(json.dumps(fig, cls=PlotlyJSONEncoder))

    def generate_complexity_chart(self) -> Dict[str, Any]:
        """Generate complexity comparison chart."""
        functions = self.result.get('functions', [])
        if not functions:
            return {'error': 'No functions found'}

        names = [f['name'] for f in functions]
        complexities = [f.get('complexity', 1) for f in functions]
        lines = [f.get('body_lines', 0) for f in functions]

        fig = go.Figure()

        fig.add_trace(go.Bar(
            x=names,
            y=complexities,
            name='Cyclomatic Complexity',
            marker_color='#2563eb'
        ))

        fig.add_trace(go.Bar(
            x=names,
            y=lines,
            name='Lines of Code',
            marker_color='#06b6d4'
        ))

        fig.update_layout(
            title=dict(text='Function Complexity Analysis', font=dict(color='#f1f5f9', size=16)),
            barmode='group',
            xaxis=dict(title=dict(text='Function', font=dict(color='#94a3b8')), tickfont=dict(color='#94a3b8'), gridcolor='rgba(255,255,255,0.05)'),
            yaxis=dict(title=dict(text='Count', font=dict(color='#94a3b8')), tickfont=dict(color='#94a3b8'), gridcolor='rgba(255,255,255,0.05)'),
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            height=400,
            font=dict(color='#f1f5f9')
        )

        return json.loads(json.dumps(fig, cls=PlotlyJSONEncoder))

    def generate_metrics_chart(self) -> Dict[str, Any]:
        """Generate code metrics pie chart."""
        metrics = {
            'Code Lines': self.result.get('code_lines', 0),
            'Comments': self.result.get('comment_lines', 0),
            'Blank Lines': self.result.get('blank_lines', 0)
        }

        fig = go.Figure(data=[go.Pie(
            labels=list(metrics.keys()),
            values=list(metrics.values()),
            hole=0.4,
            marker=dict(colors=['#2563eb', '#22c55e', '#94a3b8'])
        )])

        fig.update_layout(
            title=dict(text='Code Composition', font=dict(color='#f1f5f9', size=16)),
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            height=400,
            font=dict(color='#f1f5f9')
        )

        return json.loads(json.dumps(fig, cls=PlotlyJSONEncoder))

    def generate_flowchart(self) -> Dict[str, Any]:
        """Generate execution flowchart using Plotly shapes and annotations."""
        functions = self.result.get('functions', [])
        loops = self.result.get('loops', [])
        conditions = self.result.get('conditions', [])

        if not functions and not conditions and not loops:
            return {"error": "No flow elements found"}

        nodes = []
        edges = []

        # Start node
        nodes.append({"id": "start", "label": "Start", "type": "start", "x": 0, "y": 0})

        y_pos = 0
        x_pos = 0
        prev_id = "start"

        for i, func in enumerate(functions):
            y_pos -= 1.5
            node_id = f"func_{i}"
            label = func.get("name", "Function")
            if len(label) > 25:
                label = label[:22] + "..."
            label += "()"
            nodes.append({
                "id": node_id,
                "label": label,
                "type": "function",
                "x": x_pos,
                "y": y_pos
            })
            edges.append({"from": prev_id, "to": node_id})
            prev_id = node_id

            # Internal calls as side branches
            for j, call in enumerate(func.get("calls", [])[:2]):
                call_id = f"call_{i}_{j}"
                call_label = call
                if len(call_label) > 20:
                    call_label = call_label[:17] + "..."
                nodes.append({
                    "id": call_id,
                    "label": call_label,
                    "type": "call",
                    "x": x_pos + 2.5,
                    "y": y_pos + (j * 0.6)
                })
                edges.append({"from": node_id, "to": call_id})

        for i, cond in enumerate(conditions[:3]):
            y_pos -= 1.5
            node_id = f"cond_{i}"
            nodes.append({
                "id": node_id,
                "label": "Decision",
                "type": "decision",
                "x": x_pos,
                "y": y_pos
            })
            edges.append({"from": prev_id, "to": node_id})
            prev_id = node_id

        for i, loop in enumerate(loops[:2]):
            y_pos -= 1.5
            node_id = f"loop_{i}"
            nodes.append({
                "id": node_id,
                "label": "Loop",
                "type": "loop",
                "x": x_pos,
                "y": y_pos
            })
            edges.append({"from": prev_id, "to": node_id})
            prev_id = node_id

        # End node
        y_pos -= 1.5
        nodes.append({"id": "end", "label": "End", "type": "end", "x": x_pos, "y": y_pos})
        edges.append({"from": prev_id, "to": "end"})

        # Create Plotly figure
        shapes = []
        annotations = []

        node_colors = {
            "start": "#22c55e",
            "end": "#ef4444",
            "function": "#3b82f6",
            "call": "#a855f7",
            "decision": "#f59e0b",
            "loop": "#06b6d4"
        }

        for node in nodes:
            color = node_colors.get(node["type"], "#6b7280")
            nx, ny = node["x"], node["y"]

            if node["type"] == "decision":
                # Diamond shape
                shapes.append(dict(
                    type="path",
                    path=f"M {nx},{ny+0.5} L {nx+0.8},{ny} L {nx},{ny-0.5} L {nx-0.8},{ny} Z",
                    fillcolor=color,
                    line=dict(color="white", width=2),
                    opacity=0.85,
                    xref="x", yref="y"
                ))
            elif node["type"] in ("start", "end"):
                # Circle
                shapes.append(dict(
                    type="circle",
                    x0=nx-0.5, y0=ny-0.3,
                    x1=nx+0.5, y1=ny+0.3,
                    fillcolor=color,
                    line=dict(color="white", width=2),
                    opacity=0.85,
                    xref="x", yref="y"
                ))
            elif node["type"] == "loop":
                # Parallelogram
                shapes.append(dict(
                    type="path",
                    path=f"M {nx-0.6},{ny-0.35} L {nx+0.7},{ny-0.35} L {nx+0.5},{ny+0.35} L {nx-0.8},{ny+0.35} Z",
                    fillcolor=color,
                    line=dict(color="white", width=2),
                    opacity=0.85,
                    xref="x", yref="y"
                ))
            else:
                # Rectangle (function, call)
                shapes.append(dict(
                    type="rect",
                    x0=nx-0.7, y0=ny-0.3,
                    x1=nx+0.7, y1=ny+0.3,
                    fillcolor=color,
                    line=dict(color="white", width=2),
                    opacity=0.85,
                    xref="x", yref="y"
                ))

            annotations.append(dict(
                x=nx, y=ny,
                text=node["label"],
                showarrow=False,
                font=dict(color="white", size=11, family="Inter, sans-serif"),
                xanchor="center",
                yanchor="middle"
            ))

        # Add edge arrows
        for edge in edges:
            from_node = next(n for n in nodes if n["id"] == edge["from"])
            to_node = next(n for n in nodes if n["id"] == edge["to"])

            # Calculate connection points
            fx, fy = from_node["x"], from_node["y"]
            tx, ty = to_node["x"], to_node["y"]

            # Adjust start/end points based on relative positions
            if abs(tx - fx) < 0.1:  # Vertical
                ay = fy - 0.35
                ax = fx
                y = ty + 0.35
                x = tx
            elif tx > fx:  # To the right
                ay = fy
                ax = fx + 0.7
                y = ty
                x = tx - 0.5
            else:  # To the left
                ay = fy
                ax = fx - 0.7
                y = ty
                x = tx + 0.5

            annotations.append(dict(
                x=x, y=y,
                ax=ax, ay=ay,
                xref="x", yref="y",
                axref="x", ayref="y",
                showarrow=True,
                arrowhead=2,
                arrowsize=1,
                arrowwidth=2,
                arrowcolor="#94a3b8"
            ))

        fig = go.Figure()

        fig.update_layout(
            title=dict(text="Execution Flowchart", font=dict(color="#f1f5f9", size=16)),
            shapes=shapes,
            annotations=annotations,
            xaxis=dict(
                showgrid=False, zeroline=False, showticklabels=False,
                range=[min(n["x"] for n in nodes) - 1.5, max(n["x"] for n in nodes) + 1.5]
            ),
            yaxis=dict(
                showgrid=False, zeroline=False, showticklabels=False,
                range=[min(n["y"] for n in nodes) - 1, max(n["y"] for n in nodes) + 1]
            ),
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)",
            height=max(400, len(nodes) * 90),
            font=dict(color="#f1f5f9"),
            margin=dict(l=20, r=20, t=50, b=20),
            showlegend=False,
            hovermode=False
        )

        return json.loads(json.dumps(fig, cls=PlotlyJSONEncoder))

    def generate_dependency_graph(self) -> Dict[str, Any]:
        """Generate library dependency graph."""
        imports = self.result.get('imports', [])
        if not imports:
            return {'error': 'No imports found'}

        # Parse imports into hierarchy
        nodes = []
        edges = []
        node_set = set()

        for imp in imports:
            parts = imp.split('.')
            for i, part in enumerate(parts):
                node_id = '.'.join(parts[:i+1])
                if node_id not in node_set:
                    nodes.append({'id': node_id, 'label': part, 'level': i})
                    node_set.add(node_id)
                if i > 0:
                    parent = '.'.join(parts[:i])
                    edges.append({'source': parent, 'target': node_id})

        if not nodes:
            return {'error': 'No dependency data'}

        G = nx.DiGraph()
        for node in nodes:
            G.add_node(node['id'], label=node['label'], level=node['level'])
        for edge in edges:
            G.add_edge(edge['source'], edge['target'])

        pos = nx.spring_layout(G, k=1.5, iterations=50, seed=42)

        edge_x = []
        edge_y = []
        for edge in G.edges():
            x0, y0 = pos[edge[0]]
            x1, y1 = pos[edge[1]]
            edge_x.extend([x0, x1, None])
            edge_y.extend([y0, y1, None])

        node_x = [pos[node][0] for node in G.nodes()]
        node_y = [pos[node][1] for node in G.nodes()]
        node_labels = [G.nodes[node]['label'] for node in G.nodes()]
        node_levels = [G.nodes[node]['level'] for node in G.nodes()]

        fig = go.Figure()

        fig.add_trace(go.Scatter(
            x=edge_x, y=edge_y,
            mode='lines',
            line=dict(color='#06b6d4', width=2),
            hoverinfo='none'
        ))

        fig.add_trace(go.Scatter(
            x=node_x, y=node_y,
            mode='markers+text',
            marker=dict(
                size=25,
                color=node_levels,
                colorscale='Cividis',
                showscale=True,
                line=dict(width=2, color='white')
            ),
            text=node_labels,
            textposition="top center",
            hovertemplate='%{text}<extra></extra>'
        ))

        fig.update_layout(
            title=dict(text='Dependency Graph', font=dict(color='#f1f5f9', size=16)),
            showlegend=False,
            xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
            yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            height=500,
            font=dict(color='#f1f5f9')
        )

        return json.loads(json.dumps(fig, cls=PlotlyJSONEncoder))

    def generate_class_hierarchy(self) -> Dict[str, Any]:
        """Generate class hierarchy visualization."""
        classes = self.result.get('classes', [])
        if not classes:
            return {'error': 'No classes found'}

        G = nx.DiGraph()

        for cls in classes:
            G.add_node(cls['name'], methods=len(cls.get('methods', [])))
            for base in cls.get('bases', []):
                if base and base != 'object':
                    G.add_edge(base, cls['name'])

        pos = nx.spring_layout(G, k=2, iterations=50, seed=42)

        edge_x = []
        edge_y = []
        for edge in G.edges():
            x0, y0 = pos[edge[0]]
            x1, y1 = pos[edge[1]]
            edge_x.extend([x0, x1, None])
            edge_y.extend([y0, y1, None])

        node_x = [pos[node][0] for node in G.nodes()]
        node_y = [pos[node][1] for node in G.nodes()]
        node_methods = [G.nodes[node].get('methods', 0) for node in G.nodes()]

        fig = go.Figure()

        fig.add_trace(go.Scatter(
            x=edge_x, y=edge_y,
            mode='lines',
            line=dict(color='#22c55e', width=2),
            hoverinfo='none'
        ))

        fig.add_trace(go.Scatter(
            x=node_x, y=node_y,
            mode='markers+text',
            marker=dict(
                size=[m * 10 + 30 for m in node_methods],
                color=node_methods,
                colorscale='Greens',
                showscale=True,
                line=dict(width=2, color='white')
            ),
            text=list(G.nodes()),
            textposition="top center",
            hovertemplate='<b>%{text}</b><br>Methods: %{marker.color}<extra></extra>'
        ))

        fig.update_layout(
            title=dict(text='Class Hierarchy', font=dict(color='#f1f5f9', size=16)),
            showlegend=False,
            xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
            yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            height=500,
            font=dict(color='#f1f5f9')
        )

        return json.loads(json.dumps(fig, cls=PlotlyJSONEncoder))


def generate_report(analysis_result: Dict[str, Any], report_type: str = 'html') -> str:
    """Generate analysis report in specified format."""
    if report_type == 'json':
        return json.dumps(analysis_result, indent=2, default=str)

    elif report_type == 'txt':
        lines = [
            "=" * 60,
            "CODE ANALYSIS REPORT",
            "=" * 60,
            f"Language: {analysis_result.get('detected_language', 'unknown').upper()}",
            f"Filename: {analysis_result.get('filename', 'N/A')}",
            "-" * 60,
            "METRICS",
            "-" * 60,
            f"Total Lines: {analysis_result.get('total_lines', 0)}",
            f"Code Lines: {analysis_result.get('code_lines', 0)}",
            f"Comments: {analysis_result.get('comment_lines', 0)}",
            f"Blank Lines: {analysis_result.get('blank_lines', 0)}",
            "-" * 60,
            "FUNCTIONS",
            "-" * 60,
        ]
        for func in analysis_result.get('functions', []):
            lines.append(f"  - {func['name']}() [Line {func.get('line', '?')}]")
            lines.append(f"    Args: {', '.join(func.get('args', [])) or 'None'}")
            lines.append(f"    Complexity: {func.get('complexity', 'N/A')}")

        lines.extend([
            "-" * 60,
            "CLASSES",
            "-" * 60,
        ])
        for cls in analysis_result.get('classes', []):
            lines.append(f"  - {cls['name']}")

        lines.extend([
            "-" * 60,
            "COMPLEXITY",
            "-" * 60,
            f"Time: {analysis_result.get('complexity', {}).get('time', 'N/A')}",
            f"Space: {analysis_result.get('complexity', {}).get('space', 'N/A')}",
            f"Description: {analysis_result.get('complexity', {}).get('description', 'N/A')}",
            "=" * 60,
        ])
        return "\n".join(lines)

    elif report_type == 'html':
        html = f"""
        <!DOCTYPE html>
        <html>
        <head><title>Code Analysis Report</title>
        <style>
            body {{ font-family: Arial, sans-serif; max-width: 900px; margin: 0 auto; padding: 20px; }}
            h1 {{ color: #2563eb; }} h2 {{ color: #7c3aed; border-bottom: 2px solid #e2e8f0; padding-bottom: 5px; }}
            .metric {{ background: #f1f5f9; padding: 10px; margin: 5px 0; border-radius: 8px; }}
            .function {{ background: #ede9fe; padding: 10px; margin: 5px 0; border-radius: 8px; }}
            .complexity {{ background: #dcfce7; padding: 15px; border-radius: 8px; font-weight: bold; }}
        </style></head>
        <body>
            <h1>Code Analysis Report</h1>
            <p><strong>Language:</strong> {analysis_result.get('detected_language', 'unknown').upper()}</p>
            <p><strong>Filename:</strong> {analysis_result.get('filename', 'N/A')}</p>

            <h2>Metrics</h2>
            <div class="metric">Total Lines: {analysis_result.get('total_lines', 0)}</div>
            <div class="metric">Code Lines: {analysis_result.get('code_lines', 0)}</div>
            <div class="metric">Comments: {analysis_result.get('comment_lines', 0)}</div>
            <div class="metric">Blank Lines: {analysis_result.get('blank_lines', 0)}</div>

            <h2>Functions ({len(analysis_result.get('functions', []))})</h2>
            {''.join([f'<div class="function"><strong>{f["name"]}()</strong> - Line {f.get("line", "?")}<br>Args: {", ".join(f.get("args", [])) or "None"}<br>Complexity: {f.get("complexity", "N/A")}</div>' for f in analysis_result.get('functions', [])])}

            <h2>Classes ({len(analysis_result.get('classes', []))})</h2>
            {''.join([f'<div class="function"><strong>{c["name"]}</strong></div>' for c in analysis_result.get('classes', [])])}

            <h2>Complexity Analysis</h2>
            <div class="complexity">
                Time: {analysis_result.get('complexity', {}).get('time', 'N/A')}<br>
                Space: {analysis_result.get('complexity', {}).get('space', 'N/A')}<br>
                {analysis_result.get('complexity', {}).get('description', '')}
            </div>
        </body></html>
        """
        return html

    return "Unsupported report type"
