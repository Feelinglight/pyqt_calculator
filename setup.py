from setuptools import setup, find_packages

setup(
    name='pyqt-dark-calculator',
    version='0.0.1',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    description='PyQt5 dark calculator',
    url='https://github.com/yjg30737/pyqt-dark-calculator.git',
    install_requires=[
        'PyQt5>=5.8',
        'pyqt-resource-helper @ git+https://git@github.com/yjg30737/pyqt-resource-helper.git@main'
    ]
)