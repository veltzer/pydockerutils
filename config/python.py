import config.project

package_name = config.project.project_name

console_scripts = [
    'pydockerutils=pydockerutils.main:main',
]

setup_requires = [
]

run_requires = [
    'pytconf',  # for command line parsing
    'pylogconf',  # for logging configuration
]

test_requires = [
    'pylint',  # to check for lint errors
    'pytest',  # for testing
    'pytest-cov',  # for test coverage
    'pyflakes',  # for testing
    'pyre-check',  # for type checking
]

dev_requires = [
    'pyclassifiers',  # for programmatic classifiers
    'pypitools',  # for upload etc
    'pydmt',  # for building
    'Sphinx',  # for the sphinx builder
    'pymakehelper',  # for the makefile
]

install_requires = list(setup_requires)
install_requires.extend(run_requires)

python_requires = ">=3.6"

extras_require = {
    # ':python_version == "2.7"': ['futures'],  # for python2.7 backport of concurrent.futures
}
