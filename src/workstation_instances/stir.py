from workstation import WorkstationAbility
from sample import Sample
import random

# 搅拌：
# 限制：
# 离心管架
# 50ml离心管
# 离心管有1-10个
# 液体或者固液混合
# 盖子没盖住
# 必须要有样品（3ml以上）
def stir_constraints(sample: Sample):
    try:
        if sample.data['container']['container_name'] != "rack":
            return False
        if sample.data['container']['subcontainer']['subcontainer_name'] != "50ml_centrifuge_tube":
            return False
        if (sample.data['container']['subcontainer']['subcontainer_number'] > 10 or
                sample.data['container']['subcontainer']['subcontainer_number'] < 1):
            return False
        if sample.data['container']['subcontainer']['subcontainer_phase'] not in ['liquid', 'slurry']:
            return False
        if sample.data['container']['subcontainer']['covered'] is not False:
            return False
        if sample.data['container']['subcontainer']['subcontainer_volume'] < 3:
            return False
    except Exception as e:
        print(e)
        return False
    return True

# 能力：
# 搅拌（不做任何处理）
def stir_ability(sample: Sample):
    return sample

stir = WorkstationAbility(
    name="stir",
    constraints=stir_constraints,
    ability=stir_ability
)
