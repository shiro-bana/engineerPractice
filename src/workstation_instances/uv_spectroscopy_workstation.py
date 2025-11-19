from workstation import WorkstationAbility
from sample import Sample
import random

# 紫外光谱工作站
# 必须以离心管架进样
# 离心管架上的容器可为50ml试管
# 总容器数在1-10之间
# 容器没有盖子
# 容器内为液体
# 容器内体积为8-30ml
def uv_spectroscopy_workstation_constraints(sample: Sample):
    try:
        if sample.data['container']['container_name'] != "rack":
            raise Exception("容器必须是离心管架")
        if sample.data['container']['subcontainer']['subcontainer_name'] not in ["50ml_centrifuge_tube"]:
            raise Exception("离心管架上的容器应为50ml试管")
        if (sample.data['container']['subcontainer']['subcontainer_number'] is None or
            sample.data['container']['subcontainer']['subcontainer_number'] > 10 or
            sample.data['container']['subcontainer']['subcontainer_number'] < 1):
            raise Exception("总容器数在1-10之间")
        if sample.data['container']['subcontainer']['covered'] is True:
            raise Exception("容器必须没有盖子")
        if sample.data['container']['subcontainer']['subcontainer_phase'] != 'liquid':
            raise Exception("容器内必须为液体")
        if (sample.data['container']['subcontainer']['subcontainer_volume'] is None or
            sample.data['container']['subcontainer']['subcontainer_volume'] < 8 or
            sample.data['container']['subcontainer']['subcontainer_volume'] > 30):
            raise Exception("容器内体积必须在8-30ml之间")
    except Exception as e:
        print(e)
        return False
    return True

# 输出：
# 容器内为液体
# 容器内体积小幅减少
def uv_spectroscopy_workstation_ability(sample: Sample):
    # 减少 1-3 ml 液体
    reduction = random.uniform(1, 3)
    sample.data['container']['subcontainer']['subcontainer_volume'] -= reduction
    return sample

uv_spectroscopy_workstation = WorkstationAbility(
    name="uv_spectroscopy_workstation",
    constraints=uv_spectroscopy_workstation_constraints,
    ability=uv_spectroscopy_workstation_ability
)
