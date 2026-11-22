"""望气（WANGQI）算子骨架单测：名帖完整、桩位齐整、只增不覆盖。"""
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

    def test_embed_stub(self):
        with self.assertRaises(NotImplementedError):
            self.op.embed(None)

    def test_search_stub(self):
        with self.assertRaises(NotImplementedError):
            self.op.search(None, None)


if __name__ == "__main__":
    unittest.main()
