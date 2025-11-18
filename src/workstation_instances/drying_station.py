from workstation import WorkstationAbility
from sample import Sample


# 限制：
# 容器必须是离心管架
# 离心管架上的容器可为50ml试管、聚四氟反应瓶、西林瓶
# 总容器数在1-10之间
# 容器里为纯液体或悬浊液或纯固体带有微量液体
# 容器内体积不超过30ml
def drying_station_constraints(sample: Sample):
    try:
        if sample.data['container']['container_name'] != "rack":
            raise Exception("容器必须是离心管架")
        if sample.data['container']['subcontainer']['subcontainer_name'] not in ["50ml_centrifuge_tube", "ptfe_reaction_bottle", "vial"]:
            raise Exception("离心管架上的容器应为50ml试管、聚四氟反应瓶或西林瓶")
        if (sample.data['container']['subcontainer']['subcontainer_number'] is None or
            sample.data['container']['subcontainer']['subcontainer_number'] > 10 or
            sample.data['container']['subcontainer']['subcontainer_number'] < 1):
            raise Exception("总容器数在1-10之间")
        if sample.data['container']['subcontainer']['subcontainer_phase'] not in ['liquid', 'suspension', 'solid']:
            raise Exception("容器里为纯液体或悬浊液或纯固体带有微量液体")
        if sample.data['container']['subcontainer']['subcontainer_volume'] > 30:
            raise Exception("容器内体积不超过30ml")
    except Exception as e:
        print(e)
        return False
    return True

# 1，容器有盖子
# 输出：
# 容器内为纯液体或悬浊液
# 容器内体积不会减少太多
# 2，容器没有盖子
# 输出：
# 容器内为纯固体
def drying_station_ability(sample: Sample):
    

    return sample

drying_station = WorkstationAbility(
    name="drying_station",
    constraints=drying_station_constraints,
    ability=drying_station_ability
)