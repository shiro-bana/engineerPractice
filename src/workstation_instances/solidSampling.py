from workstation import WorkstationAbility
from sample import Sample
import random

# 固体进样站：
# 限制：
# 容器必须是50ml离心管
# 离心管没有盖子
# 没放满
def solidSampling_constraints(sample: Sample):
    try:
        # 容器必须是50ml离心管
        if sample.data['container']['container_name'] != "50ml_centrifuge_tube":
            return False
        # 离心管没有盖子
        if sample.data['container']['covered'] is not False:
            return False
        # 进样前为空或状态为固体
        if sample.data['container']['container_volume'] != 0 and sample.data['container']['container_phase'] != 'solid':
            return False 
        # 没放满
        if sample.data['container']['container_volume'] >= 50:
            return False
    except Exception as e:
        print(e)
        return False
    return True

# 能力：
# 离心管出来是固体
# 比原来的容量高一点
def solidSampling_ability(sample: Sample):
    # 离心管出来是固体
    sample.data['container']['container_phase'] = 'solid'
    # 比原来的容量高一点
    new_volume = sample.data['container']['container_volume'] + random.randint(1, 5)
    # 不能超过50ml容量
    sample.data['container']['container_volume'] = min(new_volume, 50)
    return sample

solidSampling = WorkstationAbility(
    name="solidSampling",
    constraints=solidSampling_constraints,
    ability=solidSampling_ability
)