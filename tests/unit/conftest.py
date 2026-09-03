# Copyright 2026 Canonical Ltd.
# See LICENSE file for licensing details.

"""Shared fixtures for charm unit tests."""

import pytest
from ops import testing

from charm import VaultlockerCharm


@pytest.fixture
def ctx() -> testing.Context:
    """Return a fresh charm context."""
    return testing.Context(
        VaultlockerCharm,
        meta={
            "name": "vaultlocker",
            "requires": {
                "vault-kv": {
                    "interface": "vault-kv",
                    "limit": 1,
                },
            },
        },
    )
