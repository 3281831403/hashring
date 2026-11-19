"""一致性哈希：虚拟节点、查找与副本：待实现的核心模块。"""


def hash_key(key):
    """稳定哈希到 32 位。"""
    raise NotImplementedError

def build_ring(nodes, vnodes):
    """构建虚拟节点环。"""
    raise NotImplementedError

def lookup(ring, key):
    """顺时针查找节点。"""
    raise NotImplementedError

def add_node(ring, node, vnodes):
    """加入节点并重排。"""
    raise NotImplementedError

def replicas(ring, key, count):
    """取 count 个不同副本。"""
    raise NotImplementedError
