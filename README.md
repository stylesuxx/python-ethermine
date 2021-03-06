# Python API wrapper for ehermine.org

[![Build Status](https://travis-ci.org/stylesuxx/python-ethermine.svg?branch=master)](https://travis-ci.org/stylesuxx/python-ethermine)

> Access Etherium related mining data in the [Ethermine mining pool](https://ethermine.org).

All publicly [available Ethermine API endpoints](https://ethermine.org/api/pool) are wrapped. All endpoints return dicts containing the API data or **None** if response status code was not 200. Check the tests or API documentation to see all available fields.

## Installation
Install via PIP:
```bash
pip install ethermine
```

## Usage
```python
from ethermine import Ethermine

ethermine = Ethermine()
```

### Pool
#### /poolStats

```python
stats = ethermine.pool_stats()
```

#### /blocks/history

```python
history = ethermine.blocks_history()
```

#### /networkStats

```python
stats = ethermine.network_stats()
```

#### /server/history

```python
history = ethermine.server_history()
```

### Miner

#### /miner/:miner/dashboard
```python
dashboard = ethermine.miner_dashboard("address")
```

#### /miner/:miner/history
```python
history = ethermine.miner_history("address")
```

#### /miner/:miner/payouts
```python
payouts = ethermine.miner_payouts("address")
```

#### /miner/:miner/rounds
```python
rounds = ethermine.miner_rounds("address")
```

#### /miner/:miner/settings
```python
settings = ethermine.miner_settings("address")
```

#### /miner/:miner/currentStats
```python
stats = ethermine.miner_current_stats("address")
```

### Worker
#### /miner/:miner/workers
```python
workers = ethermine.miner_workers("address")
```

#### /miner/:miner/worker/:worker/history
```python
history = ethermine.miner_worker("address", "worker")
```

#### /miner/:miner/worker/:worker/currentStats
```python
stats = ethermine.miner_worker_current_stats("address", "worker")
```

#### /miner/:miner/worker/:worker/monitor
```python
monitors = ethermine.miner_worker_monitor("address", "worker")
```

## Development
PR's are welcome - especially should the API change. Please also add tests - the tests should always represent the current state of the API including all fields.

## Building Dist Package
To build a distributable package run:
```bash
python setup.py sdist
```
