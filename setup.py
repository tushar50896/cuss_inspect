import setuptools

with open("README.md") as f:
  long_description = f.read()

setuptools.setup(
  name="cuss_inspect",
  version="1.0.1b",
  author="Tushar, Lalit, Gurwinder",
  author_email="tushar50896@gmail.com, lalitsharma2395@gmail.com,sgurwinderr@gmail.com",
  description="A basic and simple yet powerful Python library to detect toxicity/profanity of a review or list of reveiws.",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url="https://github.com/tushar50896/cuss_inspect",
  packages=setuptools.find_packages(),
  install_requires=['scikit-learn>=0.23.2','pandas==1.1.3','numpy==1.19.2'],
  include_package_data=True,
  package_data={ 'cuss_inspect': ['data/logitclfv3.lgst', 'data/vectorizerv3.lgst'] },
  python_requires='>=3.6',
  classifiers=[
    "Development Status :: 4 - Beta",
    "Natural Language :: English",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Topic :: Utilities",
  ],
)
