from setuptools import setup

setup(
    name='handwritedigits',
    version='1.0',
    package_dir={'': 'handwritedigits'},
    install_requires=[
        'tqdm==4.41.1',
        'mahotas==1.4.9'
    ],
    url='https://github.com/igormcsouza/handwrite-digits',
    author='Igor Souza',
    author_email='igormcsouza@gmail.com',
    description='Face-detection thru webcam'
)