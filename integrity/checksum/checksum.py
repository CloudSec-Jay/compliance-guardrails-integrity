"""Verify a file against a publisher-provided cryptographic checksum."""

from __future__ import annotations

import argparse
import hashlib
import hmac
from pathlib import Path

ALGORITHMS = ("sha256", "sha512")


def digest_file(path: Path, algorithm: str = "sha256") -> str:
    """Return the hexadecimal digest for *path* using a supported algorithm."""
    if algorithm not in ALGORITHMS:
        raise ValueError(f"unsupported algorithm: {algorithm}")

    digest = hashlib.new(algorithm)
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def verify_file(path: Path, expected: str, algorithm: str = "sha256") -> bool:
    """Compare the normalized expected digest with the file digest."""
    candidate = expected.strip().lower()
    expected_length = hashlib.new(algorithm).digest_size * 2
    if len(candidate) != expected_length or any(char not in "0123456789abcdef" for char in candidate):
        raise ValueError(f"expected checksum must be {expected_length} hexadecimal characters")
    return hmac.compare_digest(digest_file(path, algorithm), candidate)


def main() -> int:
    parser = argparse.ArgumentParser(description="Verify a file with SHA-256 or SHA-512")
    parser.add_argument("file", type=Path)
    parser.add_argument("checksum", help="checksum obtained from an authenticated publisher channel")
    parser.add_argument("--algorithm", choices=ALGORITHMS, default="sha256")
    args = parser.parse_args()

    try:
        matched = verify_file(args.file, args.checksum, args.algorithm)
    except (OSError, ValueError) as error:
        parser.exit(2, f"verification error: {error}\n")

    if not matched:
        print("checksum mismatch")
        return 1
    print("checksum verified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

