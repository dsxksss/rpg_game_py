class Enemy:
    # 创建一个Enemy类,包含敌人的基本属性(如生命值,攻击力,防御力等)
    def __init__(
        self,
        name: str,
        HP: int,
        MP: int,
        AD: int,
        AP: int,
        AS: int,
        CRT: int,
        DEF: int,
        MDEF: int,
    ):
        self.name = name
        self.HP = HP
        self.MP = MP
        self.AD = AD
        self.AP = AP
        self.AS = AS
        self.CRT = CRT
        self.DEF = DEF
        self.MDEF = MDEF
