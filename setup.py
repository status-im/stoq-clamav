from setuptools import setup, find_packages

setup(
    name="clamav",
    version="2.0.0",
    author="Jakub Sokołowski (@jakubgs)",
    url="https://github.com/status-im/stoq-clamav",
    license="Apache License 2.0",
    description="ClamAV scanning worker",
    packages=find_packages(),
    include_package_data=True,
)
