from workstation import WorkstationAbility
from sample import Sample

# 液相色谱仪
# 限制：
# 容器必须是色谱瓶
# 总容器数在1-54之间
# 容器没有盖子
# 容器内有微量液体
def liquid_chromatograph_constraints(sample: Sample):
    try:
        if sample.data['container']['container_name'] != "chromatography_vial":
            raise Exception("容器必须是色谱瓶")
        ###### 这里总容器数可能指代液相色谱仪的容量，可能无法用subcontainer_number指代 ######
        if (sample.data['container']['subcontainer']['subcontainer_number'] is None or
            sample.data['container']['subcontainer']['subcontainer_number'] > 54 or
            sample.data['container']['subcontainer']['subcontainer_number'] < 1):
            raise Exception("总容器数在1-54之间")
        if sample.data['container']['subcontainer']['covered'] is not False:
            raise Exception("容器必须没有盖子")
        if (sample.data['container']['subcontainer']['subcontainer_phase'] != 'liquid' or 
            sample.data['container']['subcontainer']['subcontainer_volume'] is None or
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
def liquid_chromatograph_ability(sample: Sample):
    # 液相色谱仪不改变样品，只进行分析
    return sample

liquid_chromatograph = WorkstationAbility(
    name="liquid_chromatograph",
    constraints=liquid_chromatograph_constraints,
    ability=liquid_chromatograph_ability
)
