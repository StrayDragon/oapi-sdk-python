from distutils.core import setup

from setuptools import find_packages

with open("README.md", mode="r", encoding="utf-8") as f:
    readme = f.read()

setup(
    name="lark-oapi",
    version="1.0.10",
    description="Lark OpenAPI SDK for Python",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Wenbo Mao",
    author_email="maowenbo@bytedance.com",
    url="https://github.com/larksuite/oapi-sdk-python",
    packages=find_packages(),
    install_requires=["requests", "requests_toolbelt", "pycryptodome", "httpx", "attrs"],
    extras_require={
        "flask": ["Flask"]
    },
    python_requires=">=3.7",
    keywords=["Lark", "OpenAPI"],
    include_package_data=True,
    project_urls={
        "Source": "https://github.com/larksuite/oapi-sdk-python",
    },
)
