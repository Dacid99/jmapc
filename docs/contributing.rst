Contributing
============

Thank you for your interest in contributing to jmapc! This document provides guidelines for contributing to the project.

Development Setup
-----------------

1. **Fork and clone the repository:**

   .. code-block:: console

      git clone https://github.com/yourusername/jmapc.git
      cd jmapc

2. **Install Poetry** (if you haven't already):

   Via ``pipx``:

   .. code-block:: console

      pip install pipx
      pipx install poetry
      pipx inject poetry poetry-pre-commit-plugin

   Via ``pip``:

   .. code-block:: console

      pip install poetry
      poetry self add poetry-pre-commit-plugin

3. **Install dependencies:**

   .. code-block:: console

      poetry install

4. **Install pre-commit hooks:**

   .. code-block:: console

      poetry run pre-commit install

Running Tests
-------------

Run the full test suite:

.. code-block:: console

   poetry run poe test

This will run both linting and unit tests.

Individual commands:

.. code-block:: console

   # Run linting only
   poetry run poe lint

   # Run unit tests only
   poetry run poe pytest

   # Run specific tests
   poetry run pytest tests/test_specific.py

Code Style
----------

The project uses several tools to maintain code quality:

* **Black** for code formatting
* **isort** for import sorting
* **flake8** for linting
* **mypy** for type checking
* **bandit** for security analysis

All of these are run automatically via pre-commit hooks and in CI.

Writing Tests
-------------

* Write unit tests for all new functionality
* Aim for high test coverage (current target is 95%)
* Use pytest for testing
* Mock external dependencies appropriately
* Tests should be fast and isolated

Documentation
-------------

* Update documentation for any API changes
* Add docstrings to all public functions and classes
* Follow Google-style docstring format
* Update examples if adding new features

Submitting Changes
------------------

1. **Create a new branch** for your feature or bug fix:

   .. code-block:: console

      git checkout -b feature/my-new-feature

2. **Make your changes** and ensure tests pass:

   .. code-block:: console

      poetry run poe test

3. **Commit your changes** with descriptive commit messages:

   .. code-block:: console

      git commit -m "Add support for new JMAP feature"

4. **Push to your fork** and create a pull request:

   .. code-block:: console

      git push origin feature/my-new-feature

Pull Request Guidelines
-----------------------

* Include a clear description of the problem and solution
* Reference any related issues
* Ensure all tests pass
* Update documentation as needed
* Keep pull requests focused and atomic

Reporting Issues
----------------

When reporting issues, please include:

* A clear description of the problem
* Steps to reproduce the issue
* Expected vs actual behavior
* Python version and jmapc version
* Any relevant error messages or stack traces

Feature Requests
----------------

For feature requests:

* Check if the feature aligns with JMAP specifications
* Provide a clear use case
* Consider backward compatibility
* Be willing to help implement if possible

Release Process
---------------

Releases are handled by project maintainers:

1. Version is updated automatically using poetry-dynamic-versioning
2. Releases are tagged based on conventional commits
3. PyPI packages are published automatically via GitHub Actions
4. Documentation is updated on ReadTheDocs automatically

Questions?
----------

If you have questions about contributing, feel free to:

* Open an issue for discussion
* Check existing issues and discussions
* Reach out to the maintainers

Thank you for contributing to jmapc! 