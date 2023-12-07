from setuptools import setup, find_packages

setup(
    name='Adults_Income_Level_Analysis',
    version='0.2.1',
    description='Classes for technical analysis of building dataset.',
    long_description='A Python package for analyzing adults income levels.',
    author='Manoj Kumar Singade',
    author_email='msingade@mail.yu.edu',
    license='MIT',
    url='https://github.com/Manojkumar8899/Project-4',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    project_urls={
       
        'Source': 'https://github.com/Manojkumar8899/Project-4',
        
    },
    keywords='data-analysis machine-learning pandas scikit-learn',
    install_requires=[
        'matplotlib>=3.7.1',
        'numpy>=1.24.3',
        'pandas>=1.5.3',
        'seaborn>=0.12.2',
        'scikit-learn>=0.24.2',
    ],
)
