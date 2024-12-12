import os
import json

def analyze_dependencies(package_name, max_depth):
    dependencies = {}

    def fetch_dependencies(package, depth):
        if depth > max_depth:
            return

        package_path = os.path.join("node_modules", package, "package.json")
        if not os.path.exists(package_path):
            return

        with open(package_path) as f:
            data = json.load(f)

        deps = data.get("dependencies", {})
        dependencies[package] = list(deps.keys())

        for dep in deps:
            fetch_dependencies(dep, depth + 1)

    fetch_dependencies(package_name, 1)
    return dependencies
