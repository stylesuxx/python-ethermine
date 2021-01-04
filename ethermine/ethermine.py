"""Ethermine API wrapper."""
import requests


class Ethermine:
    """Ethermine Class."""

    def __init__(self):
        """Initialize the class."""
        self.endpoint = "https://api.ethermine.org"

    def _get_data(self, endpoint: str) -> dict:
        url = "%s/%s" % (self.endpoint, endpoint)
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()["data"]

        return None

    def pool_stats(self) -> dict:
        """Get pool stats."""
        return self._get_data("poolStats")

    def blocks_history(self) -> dict:
        """Get blocks history."""
        return self._get_data("blocks/history")

    def network_stats(self) -> dict:
        """Get network stats."""
        return self._get_data("networkStats")

    def servers_history(self) -> dict:
        """Get server history."""
        return self._get_data("servers/history")

    def miner_dashboard(self, miner: str) -> dict:
        """Get miner dasboard."""
        endpoint = "miner/%s/dashboard" % miner
        return self._get_data(endpoint)

    def miner_history(self, miner: str) -> dict:
        """Get miner history."""
        endpoint = "miner/%s/history" % miner
        return self._get_data(endpoint)

    def miner_payouts(self, miner: str) -> dict:
        """Get miner payouts."""
        endpoint = "miner/%s/payouts" % miner
        return self._get_data(endpoint)

    def miner_rounds(self, miner: str) -> dict:
        """Get miner rounds."""
        endpoint = "miner/%s/rounds" % miner
        return self._get_data(endpoint)

    def miner_settings(self, miner: str) -> dict:
        """Get miner settings."""
        endpoint = "miner/%s/settings" % miner
        return self._get_data(endpoint)

    def miner_current_stats(self, miner: str) -> dict:
        """Get miner stats."""
        endpoint = "miner/%s/currentStats" % miner
        return self._get_data(endpoint)

    def miner_workers(self, miner: str) -> dict:
        """Get miner workers."""
        endpoint = "miner/%s/workers" % miner
        return self._get_data(endpoint)

    def miner_worker(self, miner: str, worker: str) -> dict:
        """Get miner workers."""
        endpoint = "miner/%s/worker/%s/history" % (miner, worker)
        return self._get_data(endpoint)

    def miner_worker_current_stats(self, miner: str, worker: str) -> dict:
        """Get miner worker stats."""
        endpoint = "miner/%s/worker/%s/currentStats" % (miner, worker)
        return self._get_data(endpoint)


'''
    def miner_worker_monitor(self, miner: str, worker: str) -> dict:
        """Get miner worker monitor."""
        endpoint = "miner/%s/worker/%s/monitor" % (miner, worker)
        return self._get_data(endpoint)
'''
