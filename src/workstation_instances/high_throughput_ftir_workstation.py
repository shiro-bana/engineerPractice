from workstation import WorkstationAbility
from sample import Sample

# 高通量红外光谱工作站：
# 限制：
# 容器必须是离心管架
# 离心管架上的容器可为50ml试管
# 总容器数在1-10之间
# 容器没有盖子
# 容器内为悬浊液
# 溶液体积在5-30ml
def high_throughput_ftir_workstation_constaints(sample: Sample):
    try:
        if sample.data['container']['container_name'] != "rack":
            raise Exception("容器必须是离心管架")
        if sample.data['container']['subcontainer']['subcontainer'] not in ["50ml_centrifuge_tube"]:
            raise Exception("离心管架上的容器应为50ml试管")
        if (sample.data['container']['subcontainer']['subcontainer_number'] is None or
            sample.data['container']['subcontainer']['subcontainer_number'] > 10 or
            sample.data['container']['subcontainer']['subcontainer_number'] < 1):
            raise Exception("总容器数在1-10之间")
        if sample.data['container']['subcontainer']['covered'] is True:
            raise Exception("试管不能有盖子")
        if sample.data['container']['subcontainer']['subcontainer_phase'] is not "suspension":
            raise Exception("容器内应为悬浊液")
        if (sample.data['container']['subcontainer']['subcontainer_volume'] is None or
            sample.data['container']['subcontainer']['subcontainer_volume'] < 5 or
            sample.data['container']['subcontainer']['subcontainer_volume'] > 30):
            raise Exception("溶液体积应在5-30ml之间")
    except Exception as e:
        print(e)
        return False
    return True

# 输出：
# 容器内为悬浊液（状态未改变）
def high_throughput_ftir_workstation_ability(sample: Sample):
    return sample

high_throughput_ftir_workstation = WorkstationAbility(
    name="high_throughput_ftir_workstation",
    constraints=high_throughput_ftir_workstation_constaints,
    ability=high_throughput_ftir_workstation_ability
)