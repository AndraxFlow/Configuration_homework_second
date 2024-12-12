from dependency_graph_tool.parser import parse_arguments
import pytest

def test_parse_arguments():
    args = [
        "--visualizer_path", "./plantuml.jar",
        "--package_name", "express",
        "--output_file", "output.puml"
    ]
    parsed = parse_arguments(args)

    assert parsed.visualizer_path ==  "./plantuml.jar"
    print('\n---\nvisualizer_path=',parsed.visualizer_path)
    assert parsed.package_name ==  "express"
    print('package_name=',parsed.package_name)
    assert parsed.output_file == "output.puml"
    print('output_file=',parsed.output_file, '\n---')
    assert parsed.max_depth ==  3 #(значение по умолчанию)
    