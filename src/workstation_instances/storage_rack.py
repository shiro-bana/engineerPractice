from workstation import WorkstationAbility
from sample import Sample
import random

# 置物架：
# 限制：
# 离心管架
# 离心管
# 离心管有1-10个
# 固液混合物或者液体
# 能力：静置
# 温度到20度
def storage_rack_constraints(sample: Sample):
    try:
        if sample.data['container']['container_name'] != "rack":
            raise Exception("容器必须是离心管架")
        if sample.data['container']['subcontainer']['subcontainer_name'] != "50ml_centrifuge_tube":
            raise Exception("离心管架上的物品必须是50ml离心管")
        if (sample.data['container']['subcontainer']['subcontainer_number'] is None or
            sample.data['container']['subcontainer']['subcontainer_number'] > 10 or
            sample.data['container']['subcontainer']['subcontainer_number'] < 1):
            raise Exception("总离心管数在1-10之间")
        if sample.data['container']['subcontainer']['subcontainer_phase'] not in ['liquid', 'slurry']:
            raise Exception("离心管内里得是液体或固液混合物")
    except Exception as e:
        print(e)
        return False
    return True
# 能力：静置
def storage_rack_ability(sample: Sample):
    sample.data['temperature'] = 20
    return sample

storage_rack = WorkstationAbility(
    name="storage_rack",
    constraints=storage_rack_constraints,
    ability=storage_rack_ability
)