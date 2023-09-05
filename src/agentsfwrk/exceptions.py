class InvalidInputError(ValueError):
    """Raised when the input is not a list of dictionaries."""

    pass


class APIResponseError(Exception):
    """Raised when the API response is empty or invalid."""

    pass


class MaxRetriesExceededError(Exception):
    """Raised when the maximum number of retries has been reached."""

    pass


class InvalidAPIKeyError(Exception):
    """Raised when the API key is missing or invalid."""

    pass


class InvalidContextOrInstructionError(TypeError):
    """Raised when the context or instruction is neither a string nor a dictionary."""

    pass
