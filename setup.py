import setuptools


setuptools.setup(
    name="spacewar",
    version="0.0.1",
    author="millefalcon",
    author_email="hanish00192gmail.com",
    description="A small example package",
    url="",
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=['pygame'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        "console_scripts": [
            "spacewar = spacewar.run:main",
        ],
    }
)

