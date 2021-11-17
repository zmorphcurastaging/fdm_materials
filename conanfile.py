import os
from conans import ConanFile

required_conan_version = ">=1.42"


class FDM_MaterialsConan(ConanFile):
    name = "fdm_materials"
    version = "4.13.0-alpha+001"
    license = "LGPL-3.0"
    author = "Ultimaker B.V."
    url = "https://github.com/Ultimaker/fdm_materials"
    description = "FDM Materials database"
    topics = ("conan", "cura", "3d-printing", "slicer")
    settings = "os", "compiler", "build_type", "arch"
    revision_mode = "scm"
    build_policy = "missing"
    default_user = "ultimaker"
    default_channel = "testing"
    exports = "LICENSE*"
    scm = {
        "type": "git",
        "subfolder": ".",
        "url": "auto",
        "revision": "auto"
    }

    def package(self):
        self.copy("*.fdm_material", src = ".", dst = os.path.join("res", "fmd_materials"))

    def package_id(self):
        self.info.header_only()
