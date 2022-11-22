import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="transparent-background",
    version="0.1",
    author="Taehun Kim",
    author_email="taehoon1018@postech.ac.kr",
    description="Make images with transparent background",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/plemeri/transparent-background",
    packages=['transparent_background', 'transparent_background.modules', 'transparent_background.backbones'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=['torch', 'torchvision', 'opencv-python', 'timm', 'tqdm', 'kornia==0.5.4', 'requests'],
    entry_points={
        "console_scripts": [
            "transparent-background=transparent_background:console",
        ],
    },
)
