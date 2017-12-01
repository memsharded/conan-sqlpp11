from conans import ConanFile, CMake
import os

class sqlpp11TestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def imports(self):
        self.copy("*.dll", "bin", "bin")
        self.copy("*.dylib", "bin", "bin")

    def test(self):
        os.chdir("bin")
        self.run(".%ssqlpp11_examples insert" % os.sep)
        self.run(".%ssqlpp11_examples update" % os.sep)
        self.run(".%ssqlpp11_examples select" % os.sep)
        self.run(".%ssqlpp11_examples remove" % os.sep)
