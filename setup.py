from setuptools import setup


def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="pyffuf",
    version="0.3",
    description="Simple and fast web fuzzer written in python.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/ScRiPt1337/pyffuf",
    author="script1337",
    author_email="anon42237@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["pyffuf"],
    include_package_data=True,
    install_requires=["aiohttp", "asyncio", "argparse", "clint", "beautifulsoup4", "datetime"],
    entry_points={
        "console_scripts": [
            "pyffuf=pyffuf.main:main",
        ]
    },
)
