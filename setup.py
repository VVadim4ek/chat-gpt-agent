from setuptools import find_packages, setup

setup(
    name="conversational-agents",
    version="0.1",
    description="microservices for conversational agents",
    packages=find_packages("src"),
    package_dir={"": "src"},
)
