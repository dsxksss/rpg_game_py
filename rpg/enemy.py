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

    def __str__(self):
        return f"""
    {self.name}属性面板：
    {'-'*25}
    生命值:\t{self.HP}
    法力值:\t{self.MP}
    物理攻击:\t{self.AD}
    魔法攻击:\t{self.AP}
    攻击速度:\t{self.AS}
    暴击率:\t{self.CRT}
    物理防御:\t{self.DEF}
    魔法防御:\t{self.MDEF}
    """

    def attact(self, target):
        damage = self.AD
        target.take_damage(damage)
        print(f"{self.name}对{target.name}造成了{damage}点伤害")

    def take_damage(self, damage):
        actual_damage = max(damage - self.DEF, 0)
        self.HP -= actual_damage
        print(f"{self.name}受到了{actual_damage}点伤害,剩余生命值{self.HP}")

    def is_alive(self):
        return self.HP > 0

    def __str__(self):
        return f"{self.name}(HP:{self.HP})"
