from workstation import WorkstationAbility
from sample import Sample

# 气相色谱仪
# 限制：
# 容器必须是色谱瓶
# 总容器数在1-25之间
# 容器有盖子
# 容器内有微量液体
def gas_chromatograph_constraints(sample: Sample):
    try:
        if sample.data['container']['container_name'] != "chromatography_vial":
            raise Exception("容器必须是色谱瓶")
        ####### 这里的总容器数很可能指代气相色谱仪能处理的样品数量，不能用sample的subcontainer_number表示 ########
        if (sample.data['container']['subcontainer']['subcontainer_number'] is None or
            sample.data['container']['subcontainer']['subcontainer_number'] > 25 or
            sample.data['container']['subcontainer']['subcontainer_number'] < 1):
            raise Exception("总容器数在1-25之间")
        if sample.data['container']['subcontainer']['covered'] is not True:
            raise Exception("容器必须有盖子")
        # 这里的液体是否指纯液体？悬浊液是否允许？
        if sample.data['container']['subcontainer']['subcontainer_phase'] not in ['liquid']:
            raise Exception("容器内必须为液体")
        if (sample.data['container']['subcontainer']['subcontainer_volume'] is None or
            sample.data['container']['subcontainer']['subcontainer_volume'] <= 0 or
            sample.data['container']['subcontainer']['subcontainer_volume'] > 5):
            raise Exception("容器内必须有微量液体")
    except Exception as e:
        print(e)
        return False
    return True

# 输出：
# 容器内为微量液体
# 体积不发生变化
def gas_chromatograph_ability(sample: Sample):
    # 气相色谱仪不改变样品，只进行分析
    return sample

gas_chromatograph = WorkstationAbility(
    name="gas_chromatograph",
    constraints=gas_chromatograph_constraints,
    ability=gas_chromatograph_ability
)
