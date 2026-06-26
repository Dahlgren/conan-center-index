from conan import ConanFile
from conan.errors import ConanInvalidConfiguration
from conan.tools.files import copy, get
from conan.tools.layout import basic_layout
import os

required_conan_version = ">=2.0"


class sse2neonConan(ConanFile):
    name = "sse2neon"
    description = "sse2neon is a C/C++ header file that converts Intel SSE intrinsics to Arm/Aarch64 NEON intrinsics"
    license = "MIT"
    url = "https://github.com/conan-io/conan-center-index"
    homepage = "https://github.com/DLTcollab/sse2neon"
    topics = ("sse", "sse2", "neon", "simd", "header-only")
    package_type = "header-library"
    settings = "os", "arch", "compiler", "build_type"
    no_copy_source = True

    def layout(self):
        basic_layout(self, src_folder="src")

    def package_id(self):
        self.info.clear()

    def source(self):
        get(self, **self.conan_data["sources"][self.version], strip_root=True)

    def package(self):
        copy(self, "sse2neon.h", src=self.source_folder, dst=os.path.join(self.package_folder, "include"))
        copy(self, "LICENSE", src=self.source_folder, dst=os.path.join(self.package_folder, "licenses"))

    def package_info(self):
        self.cpp_info.set_property("cmake_file_name", "sse2neon")
        self.cpp_info.set_property("cmake_target_name", "sse2neon")
        self.cpp_info.bindirs = []
        self.cpp_info.libdirs = []
