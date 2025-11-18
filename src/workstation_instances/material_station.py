from workstation import WorkstationAbility
from sample import Sample

# 输出为离心管架
# 离心管架上的容器可为50ml试管、聚四氟反应瓶、西林瓶
# 总容器数在1-10之间
# 容器为空容器

def material_station_constraints(sample: Sample):
    
    return True

def material_station_ability(sample: Sample):
    
    return sample

material_station = WorkstationAbility(
    name="material_station",
    constraints=material_station_constraints,
    ability=material_station_ability
)