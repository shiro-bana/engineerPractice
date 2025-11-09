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
def storageRack_constraints(sample: Sample):
    try:
        if sample.data['container']['container_name'] != "rack":
            return False
        if sample.data['container']['subcontainer']['subcontainer_name'] != "50ml_centrifuge_tube":
            return False
        if (sample.data['container']['subcontainer']['subcontainer_number'] is None or
            sample.data['container']['subcontainer']['subcontainer_number'] > 10 or
            sample.data['container']['subcontainer']['subcontainer_number'] < 1):
            return False
        if sample.data['container']['subcontainer']['subcontainer_phase'] not in ['liquid', 'slurry']:
            return False
    except Exception as e:
        print(e)
        return False
    return True
# 能力：静置
def storageRack_ability(sample: Sample):
    sample.data['temperature'] = 20
    return sample

storageRack = WorkstationAbility(
    name="storageRack",
    constraints=storageRack_constraints,
    ability=storageRack_ability
)