from example_project.application_a.dependency_a import dependency_for_b


def cli() -> None:
    print("Hello from Project B!")
    print(f"Dependency from Project A: {dependency_for_b}")
