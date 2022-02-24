import os
from pyln.testing.fixtures import *  # noqa: F401,F403
import pytest

plugin_path = os.path.join(os.path.dirname(__file__), "autopilot.py")
plugin_opt = {'plugin': plugin_path}


def test_starts(node_factory):
    l1 = node_factory.get_node(allow_broken_log=True)
    # Test dynamically
    l1.rpc.plugin_start(plugin_path)
    l1.rpc.plugin_stop(plugin_path)
    l1.rpc.plugin_start(plugin_path)
    l1.stop()
    # Then statically
    l1.daemon.opts["plugin"] = plugin_path
    l1.start()
