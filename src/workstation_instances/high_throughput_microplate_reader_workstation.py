from workstation import WorkstationAbility
from sample import Sample

# 高通量酶标仪工作站：
# 限制：
# 容器必须是24或者48或者96孔板
# 总容器数在1-24，1-48或1-96之间
# 容器内为微量液体
def high_throughput_microplate_reader_workstation_constraints(sample: Sample):
    try:
        if sample.data['container']['container_name'] not in ["24_hole_plate", "48_hole_plate", "96_hole_plate"]:
            raise Exception("容器必须是24或者48或者96孔板")
        if (sample.data['container']['subcontainer']['subcontainer_number'] is None or
            sample.data['container']['subcontainer']['subcontainer_number'] < 1):
            raise Exception("孔板总容器数不能小于1")
        if (sample.data['container']['container_name'] == "24_hole_plate" and
            sample.data['container']['subcontainer']['subcontainer_number'] > 24):
                raise Exception("24孔板总容器数在1-24之间")
        elif (sample.data['container']['container_name'] == "48_hole_plate" and
                sample.data['container']['subcontainer']['subcontainer_number'] > 48):
            raise Exception("48孔板总容器数在1-48之间")
        elif (sample.data['container']['container_name'] == "96_hole_plate" and
                sample.data['container']['subcontainer']['subcontainer_number'] > 96):
            raise Exception("96孔板总容器数在1-96之间")
        # 是否指代纯液体？悬浊液是否允许？
        if sample.data['container']['subcontainer']['subcontainer_phase'] not in ['liquid']:
            raise Exception("容器内应为液体")
        if (sample.data['container']['subcontainer']['subcontainer_volume'] is None or
            sample.data['container']['subcontainer']['subcontainer_volume'] <= 0 or
            sample.data['container']['subcontainer']['subcontainer_volume'] > 2):
            raise Exception("容器内液体容量应为微量")
    except Exception as e:
        print(e)
        return False
    return True

# 输出：
# 容器内为微量液体
# 体积不发生变化
def high_throughput_microplate_reader_workstation_ability(sample: Sample):

    return sample

high_throughput_microplate_reader_workstation = WorkstationAbility(
    name="high_throughput_microplate_reader_workstation",
    constraints=high_throughput_microplate_reader_workstation_constraints,
    ability=high_throughput_microplate_reader_workstation_ability
)
