from pathlib import Path

from setuptools import setup, find_packages

here = Path(__file__).parent.resolve()

long_description = (here/'README.md').read_text(encoding='utf-8')

setup(
    name='tenscalc',
    version='0.1.1',
    author='David E. Lambert',
    author_email='david@davidelambert.com',
    description='Tension estimator for stringed instruments.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='GPLv3',
    url='https://github.com/davidelambert/tenscalc',
    project_urls={
        'Bug Reporting': 'https://github.com/davidelambert/tenscalc/issues',
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    ],
    packages=find_packages(),
    python_requires='>=3.7',
    entry_points={
        'console_scripts': [
            'tenscalc=tenscalc.cli:main'
        ]
    },
    package_data={
        'tenscalc': ['*.json', 'manual.1', 'manual.txt']
    }
)
