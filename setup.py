from setuptools import find_packages,setup

setup(name="e-commerce-bot",
       version="0.0.1",
       author="Shubham Prajapati",
       author_email="shubhamprajapati7748@gmail.com",
       packages=find_packages(),
       install_requires=['langchain-astradb','langchain'])