import argparse





def parse_arguments(args=None):
    parser = argparse.ArgumentParser(description="Visualize npm package dependencies.")
    parser.add_argument("--visualizer_path", required=True, help="Path to PlantUML jar.")
    parser.add_argument("--package_name", required=True, help="NPM package name.")
    parser.add_argument("--output_file", required=True, help="Output PlantUML file path.")
    parser.add_argument("--max_depth", type=int, default=3, help="Max depth of dependencies.")
    if args:
        return parser.parse_args(args)
    return parser.parse_args()