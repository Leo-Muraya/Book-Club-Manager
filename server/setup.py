from setuptools import setup, find_packages

setup(
    name="bookclub",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'flask',
        'flask-sqlalchemy',
        'flask-jwt-extended',
        'flask-cors',
        'python-dotenv'
    ],
)