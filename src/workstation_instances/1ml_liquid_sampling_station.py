from workstation import WorkstationAbility
from sample import Sample
import random

# 限制：
# 必须是离心管架进样
# 离心管架上的容器可为50ml试管、聚四氟反应瓶、西林瓶
# 总容器数在1-10之间
# 容器内体积不超过30ml
# 容器内为纯液体或浑浊液或纯固体
def liquid_sampling_station_constraints(sample: Sample):
    try:
        if sample.data['container']['container_name'] != "rack":
            raise Exception("容器必须是离心管架")
        if sample.data['container']['subcontainer']['subcontainer_name'] not in ["50ml_centrifuge_tube", "ptfe_reaction_bottle", "vial"]:
            raise Exception("离心管架上的容器应为50ml试管、聚四氟反应瓶或西林瓶")
        if (sample.data['container']['subcontainer']['subcontainer_number'] is None or
            sample.data['container']['subcontainer']['subcontainer_number'] > 10 or
            sample.data['container']['subcontainer']['subcontainer_number'] < 1):
            raise Exception("总容器数在1-10之间")
        if (sample.data['container']['subcontainer']['subcontainer_volume'] is None or
            sample.data['container']['subcontainer']['subcontainer_volume'] > 30):
            raise Exception("容器内体积不超过30ml")
        if sample.data['container']['subcontainer']['subcontainer_phase'] not in ['liquid', 'suspension', 'solid']:
            raise Exception("容器内应为纯液体或浑浊液或纯固体")
    except Exception as e:
        print(e)
        return False
    return True

# 1，有盖-无盖
# 输出：
# 容器没有盖子
# 容器内体积不超过30ml
# 溶液量有一定程度增加
# 2，有盖-有盖
# 容器有盖子
# 容器内体积不超过30ml
# 溶液量有一定程度增加
# 3，无盖-无盖
# 容器没有盖子
# 容器内体积不超过30ml
# 溶液量有一定程度增加kkk
def liquid_sampling_station_ability(sample: Sample):
    # 增加 1ml 液体
    new_volume = sample.data['container']['subcontainer']['subcontainer_volume'] + 1
    sample.data['container']['subcontainer']['subcontainer_volume'] = min(new_volume, 30)

    return sample

liquid_sampling_station = WorkstationAbility(
    name="liquid_sampling_station",
    constraints=liquid_sampling_station_constraints,
    ability=liquid_sampling_station_ability
)



