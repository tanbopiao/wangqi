"""望气（WANGQI）算子单测：名帖完整、行为达标、只增不覆盖。"""
import unittest

from wangqi import Wangqi


class TestWangqi(unittest.TestCase):
    def setUp(self):
        self.op = Wangqi()

    def test_describe(self):
        d = self.op.describe()
        self.assertEqual(d["repo"], "wangqi")
        self.assertEqual(d["code"], "WANGQI")
        self.assertTrue(d["anchor"].startswith("Ω₀⊂⊙∞⊂Ω"))
        self.assertTrue(d["mingwen"])

    def test_embed_search(self):
        v1 = self.op.embed("昆仑 世界 模型")
        v2 = self.op.embed("昆仑 世界 观")
        self.op.embed("无关 内容")
        hits = self.op.search(v1, 2)
        self.assertEqual(len(hits), 2)
        self.assertEqual(hits[0]["text"], "昆仑 世界 模型")
        self.assertGreater(hits[0]["score"], hits[-1]["score"])
        self.assertEqual(len(v2), 16)
        with self.assertRaises(ValueError):
            self.op.search(v1, 0)


if __name__ == "__main__":
    unittest.main()
