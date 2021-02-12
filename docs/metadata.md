# Metadata format

Metadata files are in [JSON](https://www.json.org/json-en.html) format.  JSON
provides a good compromise between able to store structured data and ease of
use.  Templates and a validator are provided.

## ``submitter.json``
This file contains information about the submitting group.  This is at the top
of the submitter's tree (see [Submission structure](submission.md)) and
applies to all submissions by the group.  See
[``submitter.json``](../examples/submitter.json) for an example.  An
empty template is also available:
[``submitter.json``](../templates/submitter.json).

* ``submitter_id`` - [symbolic identifer](submission.md#symbolic-identifiers) for the submitter, assigned when the user registers for LRGASP.
* ``group_name`` - name of the submitting lab
* ``group_url`` - URL of the submitting lab page (optional)
* ``notes`` - notes (optional)
* ``contacts`` - array of contacts, with the first entry considered the primary contact
  * ``name`` - name of the contact
  * ``email`` - e-mail of the contact, which can be an e-mail list
  * ``notes`` - notes about the contact (optional)

## ``submission.json``
This file describes the submission, specifying all data files.  One is created
in each submission directory (see [Submission structure](submission.md)).  Data
files are either in the submission directory or a sub-directories.  All files
paths in ``submission.json`` are relative to the directory containing  ``submission.json``.

See [``submission.json``](../examples/submission.json) for an example.
An empty template is also available: [``submission.json``](../templates/submission.json).

* ``submitter_id`` - must match the ``submitter_id`` in ``submitter.json``.
* ``submission_id`` - submitter-defined [symbolic identifer](submission.md#symbolic-identifiers), unique to that submitter.
* ``description`` - description of submission
* ``challenge_id`` - one of the valid [challenge symbolic identifers](metadata-identifiers.md#LRGASP-Challenge-identifiers).
* ``submission_type`` - one of ``model`` or ``expression``.
* ``model_submission_id`` - if an ``expression`` submission, the model ``submission_id`` for which the expressions were computed.
* ``notes`` - notes (optional)
* ```data_files`` - list of input data files supplied by the LRGASP
  * ``acc`` - accession (ENCODE or LRGASP) for input data files (optional if URL supplied)
  * ``url`` - URL to file; intended for non-LRGASP provided files (optional if acc supplied)
  * ``notes`` - notes about the file (optional)
* ``result_files`` - List of files descriptions for submitted files:
  * ``fname`` - name of file (without directory), compressed with required extensions.
  * ``ftype`` - type of file, one of:
    * ``model_GTF``- [Transcript model format](model-format.md)
    * ``read_model_map`` - [Read to transcript model map](read_model_map_format.md)
    * ``expression_matrix`` - [Transcript expression matrix format](expression_matrix_format.md)
  * ``md5`` - md5 sum of file, as a hexadecimal string (output from ``md5sum`` command)
  * ``units`` - Expression units for expression results matrix: ``RPM``, ``RPKM``, ``FPKM``, ``TPM``, ``counts``.
  * ``notes`` - notes about the file (optional)
* ``software`` - list of software used by the pipeline:
  * ``name`` - name of software package
  * ``description`` - description of software (optional)
  * ``version`` - version of software
  * ``url`` - URL to software repository
  * ``config`` - command line and/or configuration options (optional)
  * ``notes`` - notes about software or how it was used (optional)
  
## Open issues
- separate expression and matrix submission 
  - replicate
- updates: do we allow overwrite or keep all version
- version 
- target data set identifier
- add picture 
- add read-to transcript file
