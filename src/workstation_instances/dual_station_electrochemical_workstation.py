from workstation import WorkstationAbility
from sample import Sample

# 双工位电化学工作站
# 限制：
# 必须是离心管架进样
# 离心管架上的容器为50ml试管
# 容器必须没有盖子
# 总容器数在1-10之间
# 容器内是混合均匀的悬浊液
# 容器内体积大于4ml
def dual_station_electrochemical_workstation_constraints(sample: Sample):
    try:
        if sample.data['container']['container_name'] != "rack":
            raise Exception("必须是离心管架进样")
        if sample.data['container']['subcontainer']['subcontainer_name'] != "50ml_centrifuge_tube":
            raise Exception("离心管架上的容器应为50ml试管")
        if sample.data['container']['subcontainer']['covered'] is True:
            raise Exception("容器必须没有盖子")
        if (sample.data['container']['subcontainer']['subcontainer_number'] is None or
            sample.data['container']['subcontainer']['subcontainer_number'] > 10 or
            sample.data['container']['subcontainer']['subcontainer_number'] < 1):
            raise Exception("总容器数在1-10之间")
        if sample.data['container']['subcontainer']['subcontainer_phase'] != 'suspension':
            raise Exception("容器内是混合均匀的悬浊液")
        if (sample.data['container']['subcontainer']['subcontainer_volume'] is None or
            sample.data['container']['subcontainer']['subcontainer_volume'] <= 4):
            raise Exception("容器内体积应该要大于4ml")
    except Exception as e:
        print(e)
        return False
    return True

# 输出：
# 容器内是悬浊液
# 容器内体积基本不变
def dual_station_electrochemical_workstation_ability(sample: Sample):
    return sample

dual_station_electrochemical_workstation = WorkstationAbility(
    name="dual_station_electrochemical_workstation",
    constraints=dual_station_electrochemical_workstation_constraints,
    ability=dual_station_electrochemical_workstation_ability
)