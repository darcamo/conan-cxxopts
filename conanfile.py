import shutil

from conans import CMake, ConanFile, tools


class CxxoptsConan(ConanFile):
    name = "cxxopts"
    version = "2.2.0"
    license = "MIT"
    author = "Darlan Cavalcante Moreira (darcamo@gmail.com)"
    url = "https://github.com/darcamo/conan-cxxopts"
    description = "Lightweight C++ command line option parser."
    no_copy_source = True
    homepage = "https://github.com/jarro2783/cxxopts"

    def source(self):
        tools.get("https://github.com/jarro2783/cxxopts/archive/v{}.zip".format(self.version))
        shutil.move("cxxopts-{}/".format(self.version), "sources")

    def package(self):
        self.copy("include/cxxopts.hpp", src="sources")

    def package_id(self):
        self.info.header_only()
