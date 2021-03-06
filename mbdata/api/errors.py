# Copyright (C) 2013 Lukas Lalinsky
# Distributed under the MIT license, see the LICENSE file for details.

SUCCESS = 0
INVALID_FORMAT_ERROR = 1
MISSING_PARAMETER_ERROR = 2
NOT_FOUND_ERROR = 3
INCLUDE_DEPENDENCY_ERROR = 4
INVALID_PARAMETER_ERROR = 5

ERROR_STATUS_CODES = {
    SUCCESS: 200,
    NOT_FOUND_ERROR: 404,
}

ERROR_DEFAULT_STATUS_CODE = 400
