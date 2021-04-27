# build.py
from setuptools import Extension

ext_modules = [Extension("example_project.application_b.pytestmodule", [
                         "src/example_project/application_b/pytestmodule.c"])]


def build(setup_kwargs):
    setup_kwargs.update(ext_modules=ext_modules)
