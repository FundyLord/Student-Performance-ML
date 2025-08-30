from setuptools import setup, find_packages

setup(
    name='student-performance-ml',
    version='0.1',
    author = 'Yash Jadhav',
    author_email = 'ygjadhav04@gmail.com',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'scikit-learn',
        'matplotlib',
        'seaborn'
    ]   
)