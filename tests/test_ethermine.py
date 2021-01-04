"""Unit tests for library."""
from ethermine import Ethermine

minerId = "97cf25aFdeb2de5A632e1ab9c73B5c28148d69E7"
workerId = "worker-1"
ethermine = Ethermine()


def test_init_class():
    """Test instance."""
    assert isinstance(ethermine, Ethermine)


def test_pool_stats():
    """Get pool stats."""
    stats = ethermine.pool_stats()
    assert isinstance(stats, dict)

    mined_blocks = stats["minedBlocks"]
    assert isinstance(mined_blocks, list)
    assert isinstance(mined_blocks[0], dict)
    assert isinstance(mined_blocks[0]["number"], int)
    assert isinstance(mined_blocks[0]["miner"], str)
    assert isinstance(mined_blocks[0]["time"], int)

    pool_stats = stats["poolStats"]
    assert isinstance(pool_stats, dict)
    assert isinstance(pool_stats["hashRate"], float)
    assert isinstance(pool_stats["miners"], int)
    assert isinstance(pool_stats["workers"], int)

    price = stats["price"]
    assert isinstance(price["usd"], float)
    assert isinstance(price["btc"], float)


def test_blocks_history():
    """Get block history."""
    history = ethermine.blocks_history()
    assert isinstance(history, list)
    assert isinstance(history[0], dict)
    assert isinstance(history[0]["difficulty"], int)
    assert isinstance(history[0]["nbrBlocks"], int)
    assert isinstance(history[0]["time"], int)


def test_network_stats():
    """Get network stats."""
    stats = ethermine.network_stats()
    assert isinstance(stats, dict)
    assert isinstance(stats["time"], int)
    assert isinstance(stats["blockTime"], float)
    assert isinstance(stats["difficulty"], int)
    assert isinstance(stats["hashrate"], int)
    assert isinstance(stats["usd"], float)
    assert isinstance(stats["btc"], float)


def test_servers_history():
    """Get server history."""
    histroy = ethermine.servers_history()
    assert isinstance(histroy, list)

    assert isinstance(histroy[0], dict)
    assert isinstance(histroy[0]["hashrate"], float)
    assert isinstance(histroy[0]["time"], int)
    assert isinstance(histroy[0]["server"], str)


def test_miner_dashboard():
    """Get server history."""
    miner = ethermine.miner_dashboard(minerId)
    assert isinstance(miner, dict)

    stats = miner["statistics"]
    assert isinstance(stats, list)
    assert isinstance(stats[0], dict)
    assert isinstance(stats[0]["time"], int)
    assert isinstance(stats[0]["reportedHashrate"], int)
    assert isinstance(stats[0]["currentHashrate"] + 0.0, float)
    assert isinstance(stats[0]["validShares"], int)
    assert isinstance(stats[0]["invalidShares"], int)
    assert isinstance(stats[0]["staleShares"], int)

    workers = miner["workers"]
    assert isinstance(workers, list)
    assert isinstance(workers[0], dict)
    assert isinstance(workers[0]["worker"], str)
    assert isinstance(workers[0]["time"], int)
    assert isinstance(workers[0]["lastSeen"], int)
    assert isinstance(workers[0]["reportedHashrate"], int)
    assert isinstance(workers[0]["currentHashrate"] + 0.0, float)
    assert isinstance(workers[0]["validShares"], int)
    assert isinstance(workers[0]["invalidShares"], int)
    assert isinstance(workers[0]["staleShares"], int)

    stats = miner["currentStatistics"]
    assert isinstance(stats, dict)
    assert isinstance(stats["time"], int)
    assert isinstance(stats["lastSeen"], int)
    assert isinstance(stats["reportedHashrate"], int)
    # assert isinstance(stats["averageHashrate"] + 0.0, float)
    assert isinstance(stats["currentHashrate"] + 0.0, float)
    assert isinstance(stats["validShares"], int)
    assert isinstance(stats["invalidShares"], int)
    assert isinstance(stats["staleShares"], int)
    assert isinstance(stats["activeWorkers"], int)
    assert isinstance(stats["unpaid"], int)
    # assert isinstance(stats["unconfirmed"], float)

    settings = miner["settings"]
    assert isinstance(settings, dict)
    assert isinstance(settings["email"], str)
    assert isinstance(settings["monitor"], int)
    assert isinstance(settings["minPayout"], int)


def test_miner_history():
    """Get miner history."""
    history = ethermine.miner_history(minerId)
    assert isinstance(history, list)
    assert isinstance(history[0], dict)
    assert isinstance(history[0]["reportedHashrate"], int)
    assert isinstance(history[0]["averageHashrate"] + 0.0, float)
    assert isinstance(history[0]["currentHashrate"] + 0.0, float)
    assert isinstance(history[0]["validShares"], int)
    assert isinstance(history[0]["invalidShares"], int)
    assert isinstance(history[0]["staleShares"], int)
    assert isinstance(history[0]["activeWorkers"], int)


def test_miner_payouts():
    """Get miner payouts."""
    history = ethermine.miner_payouts(minerId)
    assert isinstance(history, list)
    assert isinstance(history[0], dict)
    assert isinstance(history[0]["paidOn"], int)
    assert isinstance(history[0]["start"], int)
    assert isinstance(history[0]["end"], int)
    assert isinstance(history[0]["amount"], int)
    assert isinstance(history[0]["txHash"], str)


def test_miner_rounds():
    """Get miner rounds."""
    rounds = ethermine.miner_rounds(minerId)
    assert isinstance(rounds, list)
    assert isinstance(rounds[0], dict)
    assert isinstance(rounds[0]["block"], int)
    assert isinstance(rounds[0]["amount"], int)


def test_miner_settings():
    """Get miner settings."""
    settings = ethermine.miner_settings(minerId)
    assert isinstance(settings, dict)
    assert isinstance(settings["email"], str)
    assert isinstance(settings["monitor"], int)
    assert isinstance(settings["minPayout"], int)
    assert isinstance(settings["ip"], str)


def test_miner_stats():
    """Get miner stats."""
    stats = ethermine.miner_current_stats(minerId)
    assert isinstance(stats, dict)
    assert isinstance(stats["time"], int)
    assert isinstance(stats["lastSeen"], int)
    assert isinstance(stats["reportedHashrate"], int)
    assert isinstance(stats["averageHashrate"] + 0.0, float)
    assert isinstance(stats["currentHashrate"] + 0.0, float)
    assert isinstance(stats["validShares"], int)
    assert isinstance(stats["invalidShares"], int)
    assert isinstance(stats["staleShares"], int)
    assert isinstance(stats["activeWorkers"], int)
    assert isinstance(stats["unpaid"], int)
    # assert isinstance(stats["unconfirmed"], int)
    assert isinstance(stats["coinsPerMin"] + 0.0, float)
    assert isinstance(stats["usdPerMin"] + 0.0, float)
    assert isinstance(stats["btcPerMin"] + 0.0, float)


def test_miner_workers():
    """Get miner workers."""
    workers = ethermine.miner_workers(minerId)
    assert isinstance(workers, list)
    assert isinstance(workers[0], dict)
    assert isinstance(workers[0]["worker"], str)
    assert isinstance(workers[0]["time"], int)
    assert isinstance(workers[0]["lastSeen"], int)
    assert isinstance(workers[0]["reportedHashrate"], int)
    assert isinstance(workers[0]["currentHashrate"] + 0.0, float)
    assert isinstance(workers[0]["validShares"], int)
    assert isinstance(workers[0]["invalidShares"], int)
    assert isinstance(workers[0]["staleShares"], int)


def test_miner_worker():
    """Get miner workers."""
    history = ethermine.miner_worker(minerId, workerId)
    assert isinstance(history, list)
    assert isinstance(history[0], dict)
    assert isinstance(history[0]["time"], int)
    # assert isinstance(history[0]["lastSeen"], int)
    assert isinstance(history[0]["reportedHashrate"], int)
    assert isinstance(history[0]["averageHashrate"] + 0.0, float)
    assert isinstance(history[0]["currentHashrate"] + 0.0, float)
    assert isinstance(history[0]["validShares"], int)
    assert isinstance(history[0]["invalidShares"], int)
    assert isinstance(history[0]["staleShares"], int)


def test_miner_worker_stats():
    """Get miner worker statistics."""
    stats = ethermine.miner_worker_current_stats(minerId, workerId)
    assert isinstance(stats, dict)
    assert isinstance(stats["time"], int)
    assert isinstance(stats["lastSeen"], int)
    assert isinstance(stats["reportedHashrate"], int)
    assert isinstance(stats["averageHashrate"] + 0.0, float)
    assert isinstance(stats["currentHashrate"] + 0.0, float)
    assert isinstance(stats["validShares"], int)
    assert isinstance(stats["invalidShares"], int)
    assert isinstance(stats["staleShares"], int)


'''
def test_miner_worker_monitor():
    """Get miner worker monitor."""
    monitors = ethermine.miner_worker_monitor(minerId, workerId)
    assert isinstance(monitors, list)
    assert isinstance(monitors[0], dict)
    assert isinstance(monitors[0]["worker"], str)
    assert isinstance(monitors[0]["lastSeen"], int)
    assert isinstance(monitors[0]["currentHashrate"] + 0.0, float)
    assert isinstance(monitors[0]["validShares"], int)
    assert isinstance(monitors[0]["invalidShares"], int)
    assert isinstance(monitors[0]["staleShares"], int)
'''
