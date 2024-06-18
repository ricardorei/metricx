import setuptools

with open("README.md", "r") as fh:
  long_description = fh.read()

install_requires = [
    "transformers[torch]",
    "sentencepiece",
    "datasets",
]

setuptools.setup(
    name="metricx",
    version="0.1",
    author="Daniel Deutsch",
    description="Machine Translation Evaluation metric.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/google-research/metricx",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
    ],
    license="Apache 2.0",
    python_requires=">=3",
    install_requires=install_requires,
    dependency_links=[
        'https://github.com/google-research/mt-metrics-eval'
    ],
)
