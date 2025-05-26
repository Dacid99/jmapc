Changelog
=========

This page tracks the changes and improvements made to jmapc over time.

For the most up-to-date changelog, please see the `releases page on GitHub <https://github.com/smkent/jmapc/releases>`_.

Version History
---------------

The project uses `semantic versioning <https://semver.org/>`_ and follows conventional commits for automated changelog generation.

Major changes include:

* **v0.x.x series**: Initial development and core JMAP functionality
* **Core JMAP support**: Basic request/response handling, authentication
* **Email operations**: Full support for Email/* methods
* **Mailbox operations**: Complete Mailbox/* method support
* **Identity management**: Identity/* methods for sender management
* **EventSource support**: Real-time change notifications
* **Fastmail extensions**: Support for Fastmail-specific features

Recent Changes
--------------

.. note::
   
   This documentation is generated from the latest development version.
   For specific release notes, please check the GitHub releases page.

The latest changes are automatically deployed to ReadTheDocs from the main branch.

Contributing to Changelog
--------------------------

Changelog entries are generated automatically from commit messages using conventional commits format:

* ``feat:`` for new features
* ``fix:`` for bug fixes  
* ``docs:`` for documentation changes
* ``chore:`` for maintenance tasks
* ``breaking:`` for breaking changes

Example commit message:

.. code-block:: text

   feat: add support for Email/copy method
   
   Implements the JMAP Email/copy method for copying emails
   between mailboxes with proper error handling.

Breaking Changes
----------------

Any breaking changes will be clearly documented in release notes. The project aims to maintain backward compatibility within major version releases. 