from setuptools import setup, find_packages

setup(
    name='OneFormer',
    version='0.1',
    packages=find_packages(),
    url='https://github.com/SHI-Labs/OneFormer',
    author='linzy5',
    author_email='linzy5@xiaopeng.com',
    description='OneFormer: a transformer-based model for image processing',
    python_requires='>=3.8',
    install_requires=[
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
    ],
)