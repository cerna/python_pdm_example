
import sys
from pathlib import Path
from cmake_build_extension import BuildExtension, CMakeExtension

ext_modules = [CMakeExtension(name='pytestmodule',
                              install_prefix="example_project/application_a",
                              source_dir=str(Path(".").absolute()),
                              cmake_configure_options=[
                                  f"-DPython3_ROOT_DIR={Path(sys.prefix)}",
                                  "-DBUILD_SHARED_LIBS:BOOL=OFF",
                              ])]

cmdclass = dict(build_ext=BuildExtension),


def build(setup_kwargs):
    setup_kwargs.update(ext_modules=ext_modules,
                        cmdclass=dict(build_ext=BuildExtension))
