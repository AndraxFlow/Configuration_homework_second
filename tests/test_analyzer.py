from dependency_graph_tool.analyzer import analyze_dependencies

def test_analyze_dependencies():
    dependencies = analyze_dependencies("express", 2)
    assert "express" in dependencies
    print('\n---\nexpress is in dependencies\n---')
