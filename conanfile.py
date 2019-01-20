from conans import ConanFile, CMake, tools
import shutil

class CxxoptsConan(ConanFile):
    name = "cxxopts"
    version = "2.1.2"
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
