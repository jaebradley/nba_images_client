from setuptools import setup, find_packages
setup(
  name="nba_images_client",
  packages=find_packages(exclude=["tests*"]),
  install_requires=["requests", "Willow", "reportlab", "svglib"],
  version="0.0.1",
  description="NBA Images Client",
  author="Jae Bradley",
  author_email="jae.b.bradley@gmail.com",
  url="https://github.com/jaebradley/nba_images_client",
  download_url="https://github.com/jaebradley/nba_images_client/tarball/0.1",
  keywords=["NBA"],
  classifiers=[],
)