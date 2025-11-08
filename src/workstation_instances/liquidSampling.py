from workstation import WorkstationAbility
from sample import Sample
import random


# 液体进样站：
# 限制：
# 容器必须是离心管架
# 离心管架上是50ml离心管
# 离心管有1-10个
# 少于30ml
def liquidSampling_constraints(sample: Sample):
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
        # 试管里得是液体或固体, 或者为空
        if (sample.data['container']['subcontainer']['subcontainer_volume'] != 0 and 
            sample.data['container']['subcontainer']['subcontainer_phase'] not in ['liquid', 'solid']):
            return False
        # 试管内溶液少于30ml
        if sample.data['container']['subcontainer']['subcontainer_volume'] >= 30:
            return False
    except Exception as e:
        print(e)
        return False
    return True

# 能力：
# （可以加盖子）
# 离心管出来是液体，可能是悬浊液，可能是纯液体
# 比原来多一点
# 出来之后要少于30ml
def liquidSampling_ability(sample: Sample):
    if sample.data['container']['subcontainer']['subcontainer_volume'] == 0:
        sample.data['container']['subcontainer']['subcontainer_phase'] = 'liquid'
    if sample.data['container']['subcontainer']['subcontainer_phase'] == 'solid':
        sample.data['container']['subcontainer']['subcontainer_phase'] = 'suspension'
    # 比原来的容量高一点，但不能超过30ml
    new_volume = sample.data['container']['subcontainer']['subcontainer_volume'] + random.randint(1, 5)
    sample.data['container']['subcontainer']['subcontainer_volume'] = min(new_volume, 30)
    return sample

liquidSampling = WorkstationAbility(
    name="liquidSampling",
    constraints=liquidSampling_constraints,
    ability=liquidSampling_ability
)