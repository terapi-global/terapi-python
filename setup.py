from setuptools import setup, find_packages

setup(
    name="terapi-client",
    version="1.0.0",
    packages=find_packages(),
    author="Terapi Global",
    author_email="integrations@terapi.global",
    description="A Python client for easy integration with Terapi applications",
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.6",
)
