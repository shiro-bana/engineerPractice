from workstation import WorkstationAbility
from sample import Sample
import random

# 离心纯化工作站
# 限制：
# 必须是离心管架进样
# 离心管架上的容器可为50ml试管
# 总试管数在1-10之间的双数
# 容器里必须为悬浊液
# 容器必须要有盖子
# 容器内溶液不能超过30ml
def centrifugal_purification_workstation_constraints(sample: Sample):
    try:
        if sample.data['container']['container_name'] != "rack":
            raise Exception("必须是离心管架进样")
        if sample.data['container']['subcontainer']['subcontainer_name'] != "50ml_centrifuge_tube":
            raise Exception("离心管架上的容器应为50ml试管")
        if (sample.data['container']['subcontainer']['subcontainer_number'] is None or
            sample.data['container']['subcontainer']['subcontainer_number'] > 10 or
            sample.data['container']['subcontainer']['subcontainer_number'] < 1 or
            sample.data['container']['subcontainer']['subcontainer_number'] % 2 != 0):
            raise Exception("总试管数在1-10之间的双数")
        if sample.data['container']['subcontainer']['subcontainer_phase'] != 'suspension':
            raise Exception("容器里必须为悬浊液")
        if sample.data['container']['subcontainer']['covered'] is not True:
            raise Exception("容器必须要有盖子")
        if sample.data['container']['subcontainer']['subcontainer_volume'] > 30:
            raise Exception("容器内溶液不能超过30ml")
    except Exception as e:
        print(e)
        return False
    return True


# 1，保留清洗液：
# 输出：
# 容器内下层为固体，上层为液体
# 容器内体积不超过30ml
# 容器有盖子
# 2，不保留清洗液：
# 输出：
# 容器内为纯固体和微量的液体
# 容器有盖子
def centrifugal_purification_workstation_ability_with_wash_liquid(sample: Sample):
    # 设置体积为 5-30ml
    sample.data['container']['subcontainer']['subcontainer_volume'] = random.randint(5, 30)
    # 设置相态为下层固体，上层液体
    # sample.data['container']['subcontainer']['subcontainer_phase'] = 'solid_with_liquid_overlay'
    return sample

def centrifugal_purification_workstation_ability_without_wash_liquid(sample: Sample):
    # 设置体积为 2-5ml
    sample.data['container']['subcontainer']['subcontainer_volume'] = random.randint(2, 5)
    # 设置相态为纯固体和微量液体
    # sample.data['container']['subcontainer']['subcontainer_phase'] = 'solid_with_trace_liquid'
    return sample

centrifugal_purification_with_wash_liquid = WorkstationAbility(
    name="centrifugal_purification_with_wash_liquid",
    constraints=centrifugal_purification_workstation_constraints,
    ability=centrifugal_purification_workstation_ability_with_wash_liquid
)

centrifugal_purification_without_wash_liquid = WorkstationAbility(
    name="centrifugal_purification_without_wash_liquid",
    constraints=centrifugal_purification_workstation_constraints,
    ability=centrifugal_purification_workstation_ability_without_wash_liquid
)
