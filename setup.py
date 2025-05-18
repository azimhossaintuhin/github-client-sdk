from setuptools import setup, find_packages

setup(
    name="github-client-sdk",
    version="0.1.0",
    author="Azim Hossain Tuhin",
    author_email="codeocmmerze@example.com",
    description="A Python SDK for interacting with the GitHub API",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/azimhossaintuhin/github-client-sdk/",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "httpx[http2]>=0.28.1,<0.29.0",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords=["github", "api", "sdk", "client"],
    python_requires=">=3.9",
)
