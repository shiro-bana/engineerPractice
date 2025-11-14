from workstation import WorkstationAbility
from sample import Sample

def material_station_constraints(sample: Sample):
    try:
        # 物料站无额外限制（按常规兼容所有离心管架配置）
        if sample.data['container']['container_name'] != "rack":
            raise Exception("容器必须是离心管架")
        # 离心管有1-10个
        if (sample.data['container']['subcontainer']['subcontainer_number'] is None or
            sample.data['container']['subcontainer']['subcontainer_number'] > 10 or
            sample.data['container']['subcontainer']['subcontainer_number'] < 1):
            raise Exception("总离心管数在1-10之间")
        # 支持常见离心管类型
        if sample.data['container']['subcontainer']['subcontainer_name'] not in ['50ml_centrifuge_tube', '15ml_centrifuge_tube']:
            raise Exception("离心管架上的物品必须是常见离心管类型")
    except Exception as e:
        print(e)
        return False
    return True

def material_station_ability(sample: Sample):
    # 物料站能力：提供物料（不修改样品状态，仅完成流程衔接）
    return sample

material_station = WorkstationAbility(
    name="material_station",
    constraints=material_station_constraints,
    ability=material_station_ability
)