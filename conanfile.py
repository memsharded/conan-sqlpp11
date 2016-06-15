from conans import ConanFile, CMake, tools
import os


class sqlpp11Conan(ConanFile):
    name = "sqlpp11"
    version = "0.38"
    license = "BSD 2-Clause License"
    url = "https://github.com/memsharded/conan-sqlpp11"
    requires = "date/1.0.0@memsharded/testing"

    def source(self):
       self.run("git clone https://github.com/rbock/sqlpp11")
       self.run("cd sqlpp11 && git checkout 0.38")

    def package(self):
        self.copy("*.h", dst="include", src="sqlpp11/include")
        self.copy("*.h", dst="include", src="sqlpp11/connector_api")
