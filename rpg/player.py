from typing import Dict
from rpg.inventory import Inventory
from rpg.equipment import Equipment, EquipmentStatus


class Player:
    # CRT : 暴击率
    # HP:生命值 MP：法力值 AD：物理攻击 AP：法力攻击：AS:攻击速度 DEF：物理防御：MDEF：魔法防御
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

        self.player_inventory: Inventory = Inventory(6)
        # 根据装备栏这个类 创建属于玩家自己的装备栏

    def add_equipment(self, equipment: Equipment) -> None:
        # 添加装备 并且把该装备所包含的属性存放到status变量中
        status: EquipmentStatus = self.player_inventory.add_equipment(equipment)
        # 因为添加了装备 所以需要将该装备的属性传递作用到玩家自身
        self.apply_equipment_status(status, False)
        # 显示添加成功提示信息
        # print(f"{self.name}已获得{equipment.name}")
        # print(f"{equipment.name}的生命值为{equipment.HP}")
        # print(f"{equipment.name}的法力值为{equipment.MP}")
        print(f"{equipment.name}的物理攻击为{equipment.AD}")
        # print(f"{equipment.name}的魔法攻击为{equipment.AP}")
        # print(f"{equipment.name}的攻击速度为{equipment.AS}")
        # print(f"{equipment.name}的暴击率为{equipment.CRT}")
        # print(f"{equipment.name}的物理防御为{equipment.DEF}")
        # print(f"{equipment.name}的魔法防御为{equipment.MDEF}")

    def remove_equipment(self, equipment: Equipment) -> None:
        # 删除装备 并且把该装备所包含的属性存放到status变量中
        status: EquipmentStatus = self.player_inventory.remove_equipment(equipment)
        # 移除装备属性
        self.apply_equipment_status(status, True)

    def apply_equipment_status(self, status: EquipmentStatus, is_removed: bool) -> None:
        if is_removed:
            # 将装备属性从玩家自身移除
            self.HP -= status.HP
            self.MP -= status.MP
            self.AD -= status.AD
            self.AP -= status.AP
            self.AS -= status.AS
            self.CRT -= status.CRT
            self.DEF -= status.DEF
            self.MDEF -= status.MDEF

        # 应用装备属性到玩家自身
        self.HP += status.HP
        self.MP += status.MP
        self.AD += status.AD
        self.AP += status.AP
        self.AS += status.AS
        self.CRT += status.CRT
        self.DEF += status.DEF
        self.MDEF += status.MDEF
