# Checksum verifier

Use this helper only after obtaining the checksum through an independently authenticated publisher channel.

```bash
python3 checksum.py PATH/TO/FILE EXPECTED_SHA256
python3 checksum.py PATH/TO/FILE EXPECTED_SHA512 --algorithm sha512
```

Exit status `0` means the checksum matched, `1` means it did not match, and `2` means the input or file could not be validated.

A matching checksum proves byte equality with the expected value. It does not establish that the publisher or software is trustworthy.

