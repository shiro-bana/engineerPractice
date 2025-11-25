from workstation import WorkstationAbility
from sample import Sample

# 光催化工作站：
# 限制：
# 必须以容器为西林瓶进样
# 总容器数在1-20之间
# 容器内为纯液体或悬浊液
# 液体量不超过15ml
def photocatalytic_workstation_constraints(sample: Sample):
    try:
        if sample.data['container']['container_name'] != "vial":
            raise Exception("容器必须是西林瓶")
        ##### 这里的总容器数是指光催化工作站的插槽数，不能使用sample的subcontainer_number来表示 #####
        if (sample.data['container']['subcontainer']['subcontainer_number'] is None or
            sample.data['container']['subcontainer']['subcontainer_number'] > 20 or
            sample.data['container']['subcontainer']['subcontainer_number'] < 1):
            raise Exception("总容器数在1-20之间")
        if sample.data['container']['subcontainer']['subcontainer_phase'] not in ['liquid', 'suspension']:
            raise Exception("容器内应为纯液体或悬浊液")
        if (sample.data['container']['subcontainer']['subcontainer_volume'] is None or
            sample.data['container']['subcontainer']['subcontainer_volume'] > 15):
            raise Exception("液体量不超过15ml")
    except Exception as e:
        print(e)
        return False
    return True

# 输出：
# 液体量不发生变化
def photocatalytic_workstation_ability(sample: Sample):
    return sample

photocatalytic_workstation = WorkstationAbility(
    name="photocatalytic_workstation",
    constraints=photocatalytic_workstation_constraints,
    ability=photocatalytic_workstation_ability
)
