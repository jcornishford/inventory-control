import pytest

from inventory_control import storage

def test_integration_storage():

    config = {'host': 'localhost', 'user': 'wce',
              'password': 'thispasswordisobjectivelyterrible',
              'db': 'inventory_control'}
    engine = storage.StorageEngine(config=config)
    result = engine.cursor.execute("SELECT COUNT(*) FROM test")
    assert result == 1
