from conans import ConanFile, CMake, tools


class CxxoptsConan(ConanFile):
    name = "cxxopts"
    version = "2.0.0"
    license = "MIT"
    author = "Darlan Cavalcante Moreira (darcamo@gmail.com)"
    url = "https://github.com/darcamo/conan-recipes"
    description = "Lightweight C++ command line option parser."
    no_copy_source = True
    homepage = "https://github.com/jarro2783/cxxopts"

    def source(self):
        self.run("git clone https://github.com/jarro2783/cxxopts.git")
        self.run("cd cxxopts && git checkout v2.0.0")

    def package(self):
        self.copy("include/cxxopts.hpp", src="cxxopts")
