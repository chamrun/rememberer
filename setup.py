from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="rememberer",
    version="0.1.1",
    description="Rememberer is a tool to help your functions remember their previous results.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ChamRun/rememberer",
    author="ChamRun",
    author_email="chrm@aut.ac.ir",
    keywords="pickle, cache",
    packages=find_packages('src'),
    package_dir={"": "src"},
    python_requires=">=3.5",
    install_requires=["pickle5"],
    project_urls={
        "Organization": "https://chamrun.github.io/",
    },
)
