from setuptools import setup, find_packages


VERSION = '0.1.1'
__version__ = VERSION

def parse_requirements_file(filename):
    with open(filename) as f:
        requires = [l.strip() for l in f.readlines() if not l.startswith("#")]
    return requires

setup(
    name='ClusterEnsembles',  
    version=__version__,  
    packages=find_packages(),  

    author='Takehiro Sano',  
    author_email='tsano430@gmail.com',  

    url='https://github.com/tsano430/ClusterEnsembles',  

    description='A Python package for cluster ensembles', 
    long_description=open('README.md').read(), 
    long_description_content_type='text/markdown',  

    python_requires='>=3.6, <4',
    
    classifiers=[  
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Operating System :: OS Independent',
    ],


    install_requires=parse_requirements_file('requirements.txt')
)
