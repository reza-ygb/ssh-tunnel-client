#!/usr/bin/env python3
"""
SSH Tunnel Client Setup Script
Professional SSH tunneling application with GUI interface
"""

from setuptools import setup, find_packages
import os

# Read README for long description
def read_readme():
    with open("README.md", "r", encoding="utf-8") as fh:
        return fh.read()

# Read requirements
def read_requirements():
    with open("requirements.txt", "r", encoding="utf-8") as fh:
        return [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="ssh-tunnel-client",
    version="1.0.0",
    author="SSH Tunnel Client Team",
    author_email="info@ssh-tunnel-client.com",
    description="Professional SSH tunneling application with GUI interface",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/reza-ygb/ssh-tunnel-client",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: System Administrators",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Internet :: Proxy Servers",
        "Topic :: System :: Networking",
        "Topic :: Security",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: POSIX :: Linux",
        "Environment :: X11 Applications",
    ],
    python_requires=">=3.6",
    install_requires=read_requirements(),
    entry_points={
        "console_scripts": [
            "ssh-tunnel-client=ssh_tunnel_client:main",
        ],
    },
    keywords="ssh tunnel proxy vpn gui linux networking security",
    project_urls={
        "Bug Reports": "https://github.com/reza-ygb/ssh-tunnel-client/issues",
        "Source": "https://github.com/reza-ygb/ssh-tunnel-client",
        "Documentation": "https://github.com/reza-ygb/ssh-tunnel-client#readme",
    },
)
