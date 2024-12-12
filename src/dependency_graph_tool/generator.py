def generate_plantuml(graph, output_file):
    lines = ["@startuml"]
    for pkg, deps in graph.items():
        for dep in deps:
            lines.append(f"{pkg} --> {dep}")
    lines.append("@enduml")
    with open(output_file, "w") as f:
        f.write("\n".join(lines))
