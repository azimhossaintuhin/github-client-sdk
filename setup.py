from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="github-client-sdk",
    version="1.1.1",
    author="Azim Hossain Tuhin",
    author_email="codeocmmerze@example.com",
    description=(
        "Lightweight and easy-to-use Python SDK for seamless GitHub REST API integration, "
        "automation of GitHub Actions workflows, environment variable management, and OAuth authentication."
    ),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/azimhossaintuhin/github-client-sdk",
    project_urls={
        "Documentation": "https://github.com/azimhossaintuhin/github-client-sdk#readme",
        "Source": "https://github.com/azimhossaintuhin/github-client-sdk",
        "Tracker": "https://github.com/azimhossaintuhin/github-client-sdk/issues",
    },
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
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Software Distribution",
        "Topic :: Utilities",
    ],
    keywords=[
        "github",
        "github api",
        "github sdk",
        "python sdk",
        "api client",
        "rest api",
        "automation",
        "github client",
        "sdk",
        "python",
        "httpx",
        "github actions",
        "workflow management",
        "oauth authentication",
        "devops",
    ],
    python_requires=">=3.9",
)
