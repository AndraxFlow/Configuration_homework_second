from dependency_graph_tool.parser import *
from dependency_graph_tool.analyzer import analyze_dependencies
from dependency_graph_tool.generator import generate_plantuml

def main():
    args = parse_arguments()
    dependencies = analyze_dependencies(args.package_name, args.max_depth)
    generate_plantuml(dependencies, args.output_file)

if __name__ == "__main__":
    main()
