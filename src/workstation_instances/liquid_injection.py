from workstation import WorkstationAbility
from sample import Sample
import random


# 液体进样站：
# 限制：
# 容器必须是离心管架
# 离心管架上是50ml离心管
# 离心管有1-10个
# 少于30ml
def liquid_injection_constraints(sample: Sample):
    try:
        # 容器必须是离心管架
        if sample.data['container']['container_name'] != "rack":
            raise Exception("容器必须是离心管架")
        # 离心管架上的物品必须是50ml试管
        if sample.data['container']['subcontainer']['subcontainer_name'] != "50ml_centrifuge_tube":
            raise Exception("离心管架上的物品必须是50ml离心管")
        # 总试管数在1-10之间
        if (sample.data['container']['subcontainer']['subcontainer_number'] is None or
            sample.data['container']['subcontainer']['subcontainer_number'] > 10 or
            sample.data['container']['subcontainer']['subcontainer_number'] < 1):
            raise Exception("总离心管数在1-10之间")
        # 试管里得是液体或固体, 或者为空
        if (sample.data['container']['subcontainer']['subcontainer_volume'] != 0 and 
            sample.data['container']['subcontainer']['subcontainer_phase'] not in ['liquid', 'solid']):
            raise Exception("离心管内里得是液体或固体")
        # 试管内溶液少于30ml
        if sample.data['container']['subcontainer']['subcontainer_volume'] >= 30:
            raise Exception("离心管内溶液不能超过30ml")
    except Exception as e:
        print(e)
        return False
    return True

# 能力：
# （可以加盖子）
# 离心管出来是液体，可能是悬浊液，可能是纯液体
# 比原来多一点
# 出来之后要少于30ml
def liquid_injection_ability(sample: Sample):
    # sample.data['container']['subcontainer']['covered'] = True
    if sample.data['container']['subcontainer']['subcontainer_volume'] == 0:
        sample.data['container']['subcontainer']['subcontainer_phase'] = 'liquid'
    if sample.data['container']['subcontainer']['subcontainer_phase'] == 'solid':
        sample.data['container']['subcontainer']['subcontainer_phase'] = 'suspension'
    # sample.data['phase'] = sample.data['container']['subcontainer']['subcontainer_phase']
    # 比原来的容量高一点，但不能超过30ml
    new_volume = sample.data['container']['subcontainer']['subcontainer_volume'] + random.randint(1, 5)
    sample.data['container']['subcontainer']['subcontainer_volume'] = min(new_volume, 30)
    return sample

liquid_injection = WorkstationAbility(
    name="liquid_injection",
    constraints=liquid_injection_constraints,
    ability=liquid_injection_ability
)