from workstation import WorkstationAbility
from sample import Sample


# 限制：
# 必须是离心管架进样
# 离心管架上的容器可为50ml试管
# 总试管数在1-10之间的双数
# 容器里必须为悬浊液
# 容器必须要有盖子
# 容器内溶液不能超过30ml
def centrifuge_constraints(sample: Sample):
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

# 输出：
# 液体量不发生变化
# 固液分离，固体在下层、液体在上层
def centrifuge_ability(sample: Sample):
    # sample.data['container']['subcontainer']['subcontainer_phase'] = 'solid_with_liquid_overlay'
    return sample

centrifuge = WorkstationAbility(
    name="centrifuge",
    constraints=centrifuge_constraints,
    ability=centrifuge_ability
)