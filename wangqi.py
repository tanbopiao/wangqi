"""望气（WANGQI）· 向量语义检索

道统出处：元极恒一·道统构件定名册 V2 ｜ 第五批
体系锚：Ω₀⊂⊙∞⊂Ω｜DID-BR-000002

工程映射：向量语义检索。

边界：本件为算子 v1——骨架桩已按命名映射补齐实现；遵循元法第四条「只增不覆盖」，
方法只增不改名不删，行为变更走新版本；凭据不入档，宣称与事实分离。
"""

class Wangqi:
    """望气（WANGQI）算子 v1。"""

    ANCHOR = "Ω₀⊂⊙∞⊂Ω｜DID-BR-000002"
    CODE = "WANGQI"

    def __init__(self, config=None):
        self.config = dict(config or {})
        self.events = []  # 只增不覆盖：会话内事件留痕
        self.corpus = []

    def describe(self):
        """构件名帖：名、代号、职责、铭文、体系锚。"""
        return {
            "repo": "wangqi",
            "cn": "望气",
            "code": self.CODE,
            "duty": "向量语义检索",
            "mingwen": "望气察形，遥识同类",
            "anchor": self.ANCHOR,
        }

    def embed(self, text):
        """望气察形：定名哈希嵌入。"""
        import hashlib, math
        dims = int(self.config.get("dims", 16))
        vec = [0.0] * dims
        for token in str(text).split():
            h = int(hashlib.md5(token.encode()).hexdigest(), 16)
            vec[h % dims] += 1.0
        norm = math.sqrt(sum(v * v for v in vec)) or 1.0
        vec = [v / norm for v in vec]
        self.corpus.append({"text": text, "vector": vec})
        self.events.append({"event": "embed", "corpus": len(self.corpus)})
        return vec

    def search(self, vector, k):
        """遥识同类：余弦近邻检索。"""
        if k <= 0:
            raise ValueError("k 须为正")
        scored = []
        for item in self.corpus:
            score = sum(a * b for a, b in zip(vector, item["vector"]))
            scored.append((score, item["text"]))
        scored.sort(key=lambda p: -p[0])
        self.events.append({"event": "search", "k": k})
        return [{"text": t, "score": s} for s, t in scored[:k]]
