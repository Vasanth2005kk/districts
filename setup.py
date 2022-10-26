import sys
from setuptools import setup, find_packages
import os


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


def main():
    setup(
        name = "package_template_districts",
        version = '0.0.1',
        author = "VGLUG",
        author_email = "vpmglug@gmail.com",
        description = "A package template",
        #long_description = file: README.md
        #long_description_content_type = text/markdown
        #url = https://github.com/sulochanaviji/districts/src/package_template_districts
        #project_urls = https://github.com/sulochanaviji/districts/src/package_template_districts/
        #Bug Tracker = https://github.com/sulochanaviji/districts/issues
        keywords=['districts','district','pydistricts','pydistrict'],
        classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",],
        #license = GPL v3
            #operating system :: OS Independent
        packages=find_packages(),

    )

if __name__ == '__main__':
    main()
