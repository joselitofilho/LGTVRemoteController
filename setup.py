from setuptools import setup


LGTV_VERSION = 'v0.0.1'
LGTV_DOWNLOAD_URL = (
    'https://github.com/joselitofilho/LGTVRemoteControl/releases/tag/' + LGTV_VERSION
)

setup(
    name='LGTV',
    packages=['LGTV'],
    version=LGTV_VERSION,
    description='LGTV WebOS Remote Controller.',
    long_description='',
    license='MIT',
    author='Joselito Viveiros Nogueira Filho',
    author_email='joselitofilhoo@gmail.com',
    url='https://github.com/joselitofilho/LGTVRemoteControl',
    download_url=LGTV_DOWNLOAD_URL,
    entry_points={
        'console_scripts': [
            'lgtv=LGTV:main'
        ]
    },
    keywords=[
        'lg', 'tv', 'lgtv', 'webos', 'smarttv', 'remote', 'control'
    ],
    install_requires=[
        'wakeonlan',
        'ws4py',
        'requests',
        'getmac',
    ],
    data_files=[
        ('config', ['data/config.json'])
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.9',
        'Natural Language :: English',
    ],
)
