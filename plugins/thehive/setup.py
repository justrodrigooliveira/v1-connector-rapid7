# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
from setuptools import setup, find_packages


setup(name="thehive-rapid7-plugin",
      version="5.0.0",
      description="TheHive is a scalable, open source security incident response solution designed for SOCs & CERTs to collaborate, elaborate, analyze and get their job done",
      author="rapid7",
      author_email="",
      url="",
      packages=find_packages(),
      install_requires=['insightconnect-plugin-runtime'],  # Add third-party dependencies to requirements.txt, not here!
      scripts=['bin/komand_thehive']
      )