from typing import Dict
from rpg.equipment import Equipment, EquipmentStatus


class Inventory:
    def __init__(self, max_size: int) -> None:
        # 装备栏最大格数
        self.size = max_size
        # 装备栏存储库
        # key为装备名称，value为装备对象
        self.equipment_bloc: Dict[str,Equipment] = {}

    # 添加装备
    def add_equipment(self, equipment: Equipment) -> EquipmentStatus:
        if len(self.equipment_bloc) < self.size:
            self.equipment_bloc[equipment.name] = equipment
            print(f"装备{equipment.name}已添加")
            # 返回装备的属性，用于后续作用到玩家属性身上
            return equipment.get_status()
        else:
            print(f"装备栏已满，装备{equipment.name}添加失败")
            # 返回装备的属性，用于后续作用到玩家属性身上
            # 因为失败了，所以返回一个空属性
            return EquipmentStatus()

    # 根据装备名称将装备从装备栏中移除
    def remove_equipment(self, equipment: Equipment) -> EquipmentStatus:
        if equipment.name in self.equipment_bloc:
            # pop可以移除一个字典中的值
            self.equipment_bloc.pop(equipment.name)
            print(f"装备{equipment.name}已移除")
            # 返回装备的属性，用于后续作用到玩家属性身上
            return equipment.get_status()
        else:
            print(f"装备栏中无装备{equipment.name}，移除失败")
            # 返回装备的属性，用于后续作用到玩家属性身上
            # 因为失败了，所以返回一个空属性
            return EquipmentStatus()
        