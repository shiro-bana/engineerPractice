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
            raise Exception("容器必须是离心管架")
        if sample.data['container']['subcontainer']['subcontainer_name'] != "50ml_centrifuge_tube":
            raise Exception("离心管架上的物品必须是50ml离心管")
        if (sample.data['container']['subcontainer']['subcontainer_number'] is None or
            sample.data['container']['subcontainer']['subcontainer_number'] > 10 or
            sample.data['container']['subcontainer']['subcontainer_number'] < 1):
            raise Exception("总离心管数在1-10之间")
        if sample.data['container']['subcontainer']['subcontainer_phase'] not in ['liquid', 'slurry']:
            raise Exception("离心管内里得是液体或固液混合物")
        if sample.data['container']['subcontainer']['covered'] is not False:
            raise Exception("离心管不能盖上盖子")
        if (sample.data['container']['subcontainer']['subcontainer_volume'] is None or
            sample.data['container']['subcontainer']['subcontainer_volume'] < 3 or 
            sample.data['container']['subcontainer']['subcontainer_volume'] >= 50):
            raise Exception("离心管内的液体不能少于3ml或超过50ml")
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
