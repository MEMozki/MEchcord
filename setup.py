from setuptools import setup, find_packages

setup(
    name="MEchcord",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "aiohttp>=3.8.0",
        "asyncio>=3.4.3",
    ],
    author="MEMozki",
    author_email="memozki@bk.ru",
    description="A custom Discord API library",
    url="https://github.com/MEMozki/mechcord",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
