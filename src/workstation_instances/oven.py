from workstation import WorkstationAbility
from sample import Sample
import random

# 烘箱
# （1）把溶剂烘干
# 限制：
# 离心管架进样
# 架子上有50ml离心管
# 离心管有1-10个
# 温度低于200度
# 没装满
# 没有盖子
# 离心管中是液体或者固液混合物
def oven_dry_constraints(sample: Sample):
    try:
        if sample.data['container']['container_name'] != "rack":
            return False
        if sample.data['container']['subcontainer']['subcontainer_name'] != "50ml_centrifuge_tube":
            return False
        if (sample.data['container']['subcontainer']['subcontainer_number'] > 10 or
                sample.data['container']['subcontainer']['subcontainer_number'] < 1):
            return False
        if sample.data['temperature'] >= 200:
            return False
        if sample.data['container']['subcontainer']['subcontainer_volume'] >= 50:
            return False
        if sample.data['container']['subcontainer']['covered'] is not False:
            return False
        if sample.data['container']['subcontainer']['subcontainer_phase'] not in ['liquid', 'slurry']:
            return False
    except Exception as e:
        print(e)
        return False
    return True

# 能力：
# 出来全都是固体
# 温度达到50～100度
# 容量减少
def oven_dry_ability(sample: Sample):
    sample.data['container']['subcontainer']['subcontainer_phase'] = 'solid'
    # 体积至少保有固体的体积，假设固体体积为原体积的30%
    sample.data['container']['subcontainer']['subcontainer_volume'] *= random.uniform(0.3, 0.5) 
    sample.data['temperature'] = random.randint(50, 100)
    return sample

# （2）升温反应加热：
# 离心管架进样
# 架子上有50ml离心管
# 离心管有1-10个
# 温度低于200度
# 没装满
# 有盖子
# 离心管中是液体或者固液混合物
def oven_heating_constraints(sample: Sample):
    try:
        if sample.data['container']['container_name'] != "rack":
            return False
        if sample.data['container']['subcontainer']['subcontainer_name'] != "50ml_centrifuge_tube":
            return False
        if (sample.data['container']['subcontainer']['subcontainer_number'] > 10 or
                sample.data['container']['subcontainer']['subcontainer_number'] < 1):
            return False
        if sample.data['temperature'] >= 200:
            return False
        if sample.data['container']['subcontainer']['subcontainer_volume'] >= 50:
            return False
        if sample.data['container']['subcontainer']['covered'] is not True:
            return False
        if sample.data['container']['subcontainer']['subcontainer_phase'] not in ['liquid', 'slurry']:
            return False
    except Exception as e:
        print(e)
        return False
    return True

# 能力：
# 把容器加热到100～200度
def oven_heating_ability(sample: Sample):
    sample.data['temperature'] = random.randint(100, 200)
    return sample

oven_dry = WorkstationAbility(
    name="oven_dry",
    constraints=oven_dry_constraints,
    ability=oven_dry_ability
)
oven_heating = WorkstationAbility(
    name="oven_heating",
    constraints=oven_heating_constraints,
    ability=oven_heating_ability
)