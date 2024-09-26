from rpg.inventory import Inventory


# 装备数值属性类，主要用于方便设置属性作用到角色身上
class EquipmentStatus:
    def __init__(
        self,
        AD: int = 0,
        AP: int = 0,
        HP: int = 0,
        MP: int = 0,
        DEF: int = 0,
        MDEF: int = 0,
        AS: int = 0,
        CRT: int = 0,
    ) -> None:
        self.AD = AD
        self.AP = AP
        self.HP = HP
        self.MP = MP
        self.DEF = DEF
        self.MDEF = MDEF
        self.AS = AS
        self.CRT = CRT


class Equipment(Inventory):
    def __init__(self, name: str) -> None:
        self.name = name

    def get_status():
        # 不写参数默认为全0值属性
        return EquipmentStatus()


# AD:物理攻击 AP:魔法攻击 AS:攻击速度  CRT:暴击率
class Weapon(Equipment):
    def __init__(
        self,
        name,
        AD: int = 0,
        AP: int = 0,
        AS: int = 0,
        CRT: int = 0,
    ) -> None:
        super().__init__(name)
        self.AD = AD
        self.AP = AP
        self.AS = AS
        self.CRT = CRT

    # 给装备设定会对玩家影响属性值，其余没设置的值则为0，也就表示不影响玩家属性
    def get_status(self) -> EquipmentStatus:
        return EquipmentStatus(AD=self.AD, AP=self.AP, AS=self.AS, CRT=self.CRT)


# Armor：防具 DEF:物理防御 MDEF:魔法防御
class Armor(Equipment):
    def __init__(
        self,
        name: str,
        HP: int = 0,
        DEF: int = 0,
        MDEF: int = 0,
    ) -> None:
        super().__init__(name)
        self.HP = HP
        self.DEF = DEF
        self.MDEF = MDEF

    # 给防具设定会对玩家影响属性值，其余没设置的值则为0，也就表示不影响玩家属性
    def get_status(self) -> EquipmentStatus:
        return EquipmentStatus(DEF=self.DEF, MDEF=self.MDEF)


# Potion:药水 HP:回血 MP：回蓝
class Potion(Equipment):
    def __init__(self, name: str, HP: int = 0, MP: int = 0) -> None:
        super().__init__(name)
        self.HP = HP
        self.MP = MP

    # 给药水设定会对玩家影响属性值，其余没设置的值则为0，也就表示不影响玩家属性
    def get_status(self) -> EquipmentStatus:
        return EquipmentStatus(HP=self.HP, MP=self.MP)
