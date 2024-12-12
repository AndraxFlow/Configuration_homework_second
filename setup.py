from setuptools import setup, find_packages

setup(
    name="dependency_graph_tool",
    version="1.0.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    entry_points={
        "console_scripts": [
            "dependency-graph-tool=dependency_graph_tool.main:main"
        ]
    },
    install_requires=[],
)
