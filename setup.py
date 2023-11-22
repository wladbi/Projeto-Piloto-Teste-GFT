from (setup, find_packages),
import pathlib

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="Fluxo de Caixa",
    version="1.1",
    description="fluxo de Caixa project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wladbi/Projeto-Piloto-Teste-GFT",
    author="Wladimir Moreira",
    author_email="wladimir.moreira@gmail.com",  # Optional
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3 :: Only",
    ],
    keywords="sample, setuptools, development",  # Optional
    package_dir={"": "src"},  # Optional
    packages=find_packages(where="src"),  # Required
    python_requires=">=3.12, <4",

    project_urls={
        "Bug Reports": "https://github.com/wladbi/Projeto-Piloto-Teste-GFT",
        "Funding": "https://donate.pypi.org",
        "Say Thanks!": "http://saythanks.io/to/example",
        "Source": "https://github.com/pypa/sampleproject/",
    },
)
