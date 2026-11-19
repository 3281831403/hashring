# 一致性哈希：虚拟节点、查找与副本

扩缩容后缓存命中率骤降：哈希不是稳定摘要，虚拟节点没按节点分开，环没排序，查找没用顺时针第一个，加节点没有重排，副本数量没去重，空环没有兜底，批量迁移只成功一半。

## 目录结构

```
README.md
conftest.py
.gitignore
net/__init__.py
net/hashring.py
tests/test_hashring.py
```

## 当前状态

`net/hashring.py` 中所有函数只保留签名与文档字符串，函数体统一
`raise NotImplementedError`。`tests/test_hashring.py` 有 15 个参数化用例，
初始全部失败。

## 需要修复的 10 个问题

1. 稳定哈希摘要
2. 虚拟节点按节点生成
3. 环按哈希排序
4. 顺时针查找
5. 加节点重排
6. 副本去重
7. 空环兜底

## 验收

```bash
python -m pytest -q
```

初始应得到 `15 failed`，且没有 collection error。实现 `net/hashring.py`
后 15 条用例应全部通过。
