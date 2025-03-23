from datetime import datetime, timezone


def get_utc_timestamp():
    """
    Returns the current UTC timestamp in ISO 8601 format.
    Example format: '2025-02-15T12:34:56Z'
    """
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


if __name__ == "__main__":
    print(get_utc_timestamp())
