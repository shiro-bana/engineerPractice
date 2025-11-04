from workstation import WorkstationAbility
from sample import Sample
import random


def decentralization_constraints(sample: Sample):
    try:
        # 容器必须是离心管架
        if sample.data['container']['container_name'] != "rack":
            return False
        # 离心管架上的物品必须是50ml试管
        if sample.data['container']['subcontainer']['subcontainer_name'] != "50ml_centrifuge_tube":
            return False
        # 总试管数在1-10之间
        if (sample.data['container']['subcontainer']['subcontainer_number'] > 10 or
                sample.data['container']['subcontainer']['subcontainer_number'] < 1):
            return False
        # 试管里得是液体
        if sample.data['container']['subcontainer']['subcontainer_phase'] != 'liquid':
            return False
        # 试管要有盖子
        if sample.data['container']['subcontainer']['covered'] is not True:
            return False
        # 试管内溶液不能超过30ml
        if sample.data['container']['subcontainer']['subcontainer_volume'] > 30:
            return False
    except Exception as e:
        print(e)
        return False
    return True


def decentralization_ability_1(sample: Sample):
    # 保留清洗液，出来是液体
    sample.data['container']['subcontainer']['subcontainer_volume'] = random.randint(5, 30)
    return sample


def decentralization_ability_2(sample: Sample):
    # 不保留清洗液，出来是固体
    sample.data['container']['subcontainer']['subcontainer_volume'] = random.randint(2, 5)
    sample.data['container']['subcontainer']['subcontainer_phase'] = 'solid'
    return sample


decentralization = WorkstationAbility(
    name="decentralization",
    constraints=decentralization_constraints,
    ability=decentralization_ability_2
)
