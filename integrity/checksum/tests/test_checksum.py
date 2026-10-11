import hashlib
import tempfile
import unittest
from pathlib import Path

from integrity.checksum.checksum import digest_file, verify_file


class ChecksumTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.path = Path(self.directory.name) / "artifact.bin"
        self.path.write_bytes(b"reviewed artifact\n")

    def tearDown(self):
        self.directory.cleanup()

    def test_digest_matches_hashlib(self):
        expected = hashlib.sha256(self.path.read_bytes()).hexdigest()
        self.assertEqual(digest_file(self.path), expected)

    def test_verify_accepts_matching_digest(self):
        expected = hashlib.sha512(self.path.read_bytes()).hexdigest()
        self.assertTrue(verify_file(self.path, expected.upper(), "sha512"))

    def test_verify_rejects_mismatch(self):
        self.assertFalse(verify_file(self.path, "0" * 64))

    def test_verify_rejects_malformed_checksum(self):
        with self.assertRaises(ValueError):
            verify_file(self.path, "not-a-checksum")


if __name__ == "__main__":
    unittest.main()

