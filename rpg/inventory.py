from typing import Dict
from rpg.equipment import Equipment, EquipmentStatus


class Inventory:
    def __init__(self, max_size: int) -> None:
        # 设置装备栏最大值
        self.size = max_size
        # 一个装备栏存储库 key：装备名称 value：装备对象
        self.equipment_block: Dict[str, Equipment] = {}

    # 添加装备
    def add_equipment(self, equipment: Equipment) -> EquipmentStatus:
        # 当存储库里面的装备小于最大值时
        if len(self.equipment_block) < self.size:
            self.equipment_block[equipment.name] = equipment
            print(f"装备{equipment.name}已添加")
            return equipment.get_status()
        # 否则添加失败
        else:
            print(f"装备栏已满,装备{equipment.name}添加失败")
            # 如果添加成功就返回改装备对应的属性，否则返回空属性
            return EquipmentStatus()

    # 移除装备
    def remove_equipment(self, equipment: Equipment) -> EquipmentStatus:
        # 判断存储库里是否有这个装备,用pop方法来实现移除
        if equipment.name in self.equipment_block:
            self.equipment_block.pop(equipment.name)
            print(f"装备{equipment.name}已移除")
            return equipment.get_status()
        else:
            print(f"装备栏中无装备{equipment.name},移除失败")
            return EquipmentStatus()
