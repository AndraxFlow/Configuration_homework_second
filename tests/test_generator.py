from dependency_graph_tool.generator import generate_plantuml
import os

def test_generate_plantuml(tmp_path):
    graph = {"express": ["body-parser", "cookie-parser"]}
    output_file = tmp_path / "output.puml"
    generate_plantuml(graph, output_file)
    assert output_file.exists()
    print('\n---\nfile has been generated\n---')

