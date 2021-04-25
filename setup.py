import setuptools

setuptools.setup(
  name="fpcicd",
  version="0.0.0",
  description="python project run in docker",
  packages=setuptools.find_packages("src"),
  package_dir={"": "src"},
)
