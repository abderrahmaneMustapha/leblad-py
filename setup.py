import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="leblad", # Replace with your own username
    version="0.0.4",
    author="Toumi abderrahmane",
    author_email="abderrahmanemustapha030898@gmail.com",
    description="the python version of leblad library,  provide a list of Algerian administrative areas with many useful APIs" 
+    "based on  dzcode-io/leblad",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/abderrahmaneMustapha/leblad-py",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
