class Effect8380(BaseEffect):
    """
    solarFlareShipBonusSmallEnergyTurretDamageSAF

    Used by:
    Mohs	莫斯级
    """

    type = 'passive'

    @staticmethod
    def handler(fit, ship, context, projectionRange, **kwargs):
        #巨神兵级 514
        fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill('Small Energy Turret'),
                                      'damageMultiplier', ship.getModifiedItemAttr('shipBonusAF'),
                                      skill='Amarr Frigate', **kwargs)
        #(-参考相似的effects填入函数及参数，可以多条)

class Effect8381(BaseEffect):
    """
    solarFlareShipArmorResistanceBonusSAF

    Used by:
    Mohs	莫斯级
    """

    type = 'passive'

    @staticmethod
    def handler(fit, ship, context, projectionRange, **kwargs):
        #惩罚者级 1804 1805 1806 1807
        fit.ship.boostItemAttr('armorEmDamageResonance', ship.getModifiedItemAttr('shipBonusSAF'),
                               skill='Solarflare Frigate Operation', **kwargs)
        fit.ship.boostItemAttr('armorThermalDamageResonance', ship.getModifiedItemAttr('shipBonusSAF'),
                               skill='Solarflare Frigate Operation', **kwargs)
        fit.ship.boostItemAttr('armorKineticDamageResonance', ship.getModifiedItemAttr('shipBonusSAF'),
                               skill='Solarflare Frigate Operation', **kwargs)
        fit.ship.boostItemAttr('armorExplosiveDamageResonance', ship.getModifiedItemAttr('shipBonusSAF'),
                               skill='Solarflare Frigate Operation', **kwargs)
        #(-参考相似的effects填入函数及参数，可以多条)

class Effect8383(BaseEffect):
    """
    solarFlareShipBonusSmallEnergyTurretTrackingSpeed

    Used by:
    Mohs	莫斯级
    """

    type = 'passive'

    @staticmethod
    def handler(fit, ship, context, projectionRange, **kwargs):
        #魔女级 3489
        fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill('Small Energy Turret'),
                                      'trackingSpeed', ship.getModifiedItemAttr('shipBonusSAF2'),
                                      skill='Solarflare Frigate Operation', **kwargs)
        #(-参考相似的effects填入函数及参数，可以多条)

class Effect8386(BaseEffect):
    """
    solarFlareShipBonusLightMissileAndRocketROF

    Used by:
    Stadion	斯特迪亚级
    """

    type = 'passive'

    @staticmethod
    def handler(fit, ship, context, projectionRange, **kwargs):
        #探索级舰队型 11068
        fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill('Missile Launcher Operation'),
                                      'speed', ship.getModifiedItemAttr('shipBonusCF'),
                                      skill='Caldari Frigate', **kwargs)
        #(-参考相似的effects填入函数及参数，可以多条)

class Effect8387(BaseEffect):
    """
    solarFlareShipBonusShieldResistanceBonus

    Used by:
    Stadion	斯特迪亚级
    """

    type = 'passive'

    @staticmethod
    def handler(fit, ship, context, projectionRange, **kwargs):
        #小鹰级 1816 1817 1819 1820
        fit.ship.boostItemAttr('shieldEmDamageResonance', ship.getModifiedItemAttr('shipBonusSCF2'),
                               skill='Solarflare Frigate Operation', **kwargs)
        fit.ship.boostItemAttr('shieldThermalDamageResonance', ship.getModifiedItemAttr('shipBonusSCF2'),
                               skill='Solarflare Frigate Operation', **kwargs)
        fit.ship.boostItemAttr('shieldKineticDamageResonance', ship.getModifiedItemAttr('shipBonusSCF2'),
                               skill='Solarflare Frigate Operation', **kwargs)
        fit.ship.boostItemAttr('shieldExplosiveDamageResonance', ship.getModifiedItemAttr('shipBonusSCF2'),
                               skill='Solarflare Frigate Operation', **kwargs)
        #(-参考相似的effects填入函数及参数，可以多条)

class Effect8388(BaseEffect):
    """
    solarFlareShipBonusRocketAndLightMissileFlySpeedBonus

    Used by:
    Stadion	斯特迪亚级
    """

    type = 'passive'

    @staticmethod
    def handler(fit, ship, context, projectionRange, **kwargs):
        #茶隼级 5080
        fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill('Missile Launcher Operation'),
                                        'maxVelocity', ship.getModifiedItemAttr('shipBonusSCF'),
                                        skill='Solarflare Frigate Operation', **kwargs)
        #(-参考相似的effects填入函数及参数，可以多条)

class Effect8392(BaseEffect):
    """
    solarFlareShipBonusSmallHybridTurretDmg

    Used by:
    Doppler	多普勒级
    """

    type = 'passive'

    @staticmethod
    def handler(fit, ship, context, projectionRange, **kwargs):
        #因卡萨斯级 512
        fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill('Small Hybrid Turret'),
                                      'damageMultiplier', ship.getModifiedItemAttr('shipBonusGF'),
                                      skill='Gallente Frigate', **kwargs)
        #(-参考相似的effects填入函数及参数，可以多条)

class Effect8394(BaseEffect):
    """
    solarFlareShipBonusSmallHybridTurretTracking

    Used by:
    Doppler	多普勒级
    """

    type = 'passive'

    @staticmethod
    def handler(fit, ship, context, projectionRange, **kwargs):
        #特里斯坦级 2504
        fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill('Small Hybrid Turret'),
                                      'trackingSpeed', ship.getModifiedItemAttr('shipBonusSGF'),
                                      skill='Solarflare Frigate Operation', **kwargs)
        #(-参考相似的effects填入函数及参数，可以多条)

class Effect8398(BaseEffect):
    """
    solarFlareShipBonusSmallProjectileTurretDmg

    Used by:
    Roentgen	伦琴级
    """

    type = 'passive'

    @staticmethod
    def handler(fit, ship, context, projectionRange, **kwargs):
        #伐木者级 508
        fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill('Small Projectile Turret'),
                                      'damageMultiplier', ship.getModifiedItemAttr('shipBonusMF'),
                                      skill='Minmatar Frigate', **kwargs)
        #(-参考相似的effects填入函数及参数，可以多条)

class Effect8400(BaseEffect):
    """
    solarFlareShipBonusSmallProjectileTurretRoF

    Used by:
    Roentgen	伦琴级
    """

    type = 'passive'

    @staticmethod
    def handler(fit, ship, context, projectionRange, **kwargs):
        #裂谷级 7248
        fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill('Small Projectile Turret'),
                                      'speed', ship.getModifiedItemAttr('shipBonusSMF'), 
                                      skill='Solarflare Frigate Operation', **kwargs)
        #(-参考相似的effects填入函数及参数，可以多条)

class Effect8404(BaseEffect):
    """
    solarFlareShipBonusMedEnergyTurretDmg

    Used by:
    Celsius	摄尔修斯级
    """

    type = 'passive'

    @staticmethod
    def handler(fit, ship, context, projectionRange, **kwargs):
        #暴君级 5136
        fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill('Medium Energy Turret'),
                                      'damageMultiplier', ship.getModifiedItemAttr('shipBonusAC'),
                                      skill='Amarr Cruiser', **kwargs)
        #(-参考相似的effects填入函数及参数，可以多条)

class Effect8405(BaseEffect):
    """
    solarFlareShipBonusACruiserArmorResistance

    Used by:
    Celsius	摄尔修斯级
    """

    type = 'passive'

    @staticmethod
    def handler(fit, ship, context, projectionRange, **kwargs):
        #暴君级 958 959 960 961
        fit.ship.boostItemAttr('armorEmDamageResonance', ship.getModifiedItemAttr('shipBonusSAC'),
                               skill='Solarflare Cruiser Operation', **kwargs)
        fit.ship.boostItemAttr('armorExplosiveDamageResonance', ship.getModifiedItemAttr('shipBonusSAC'),
                               skill='Solarflare Cruiser Operation', **kwargs)
        fit.ship.boostItemAttr('armorKineticDamageResonance', ship.getModifiedItemAttr('shipBonusSAC'),
                               skill='Solarflare Cruiser Operation', **kwargs)
        fit.ship.boostItemAttr('armorThermalDamageResonance', ship.getModifiedItemAttr('shipBonusSAC'),
                               skill='Solarflare Cruiser Operation', **kwargs)
        #(-参考相似的effects填入函数及参数，可以多条)

class Effect8406(BaseEffect):
    """
    solarFlareShipBonusMedEnergyTurretCapCost

    Used by:
    Celsius	摄尔修斯级
    """

    type = 'passive'

    @staticmethod
    def handler(fit, ship, context, projectionRange, **kwargs):
        #启示级 516
        fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill('Medium Energy Turret'),
                                      'capacitorNeed', ship.getModifiedItemAttr('shipBonusAC2'),
                                      skill='Amarr Cruiser', **kwargs)
        #(-参考相似的effects填入函数及参数，可以多条)

class Effect8407(BaseEffect):
    """
    solarFlareShipBonusMedEnergyTurretTrackingSpeed

    Used by:
    Celsius	摄尔修斯级
    """

    type = 'passive'

    @staticmethod
    def handler(fit, ship, context, projectionRange, **kwargs):
        #幽灵级 3484
        fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill('Medium Energy Turret'),
                                      'trackingSpeed', ship.getModifiedItemAttr('shipBonusSAC2'),
                                      skill='Solarflare Cruiser Operation', **kwargs)
        #(-参考相似的effects填入函数及参数，可以多条)

class Effect8410(BaseEffect):
    """
    solarFlareShipBonusLMHMHAMDmg

    Used by:
    Riemann	黎曼级
    """

    type = 'passive'

    @staticmethod
    def handler(fit, ship, context, projectionRange, **kwargs):
        #镰刀级舰队型 6088 6093 6096
        for damageType in ('em', 'explosive', 'kinetic', 'thermal'):
            fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill('Heavy Assault Missiles'),
                                            '{0}Damage'.format(damageType), ship.getModifiedItemAttr('shipBonusCC'),
                                            skill='Caldari Cruiser', **kwargs)
            fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill('Heavy Missiles'),
                                            '{0}Damage'.format(damageType), ship.getModifiedItemAttr('shipBonusCC'),
                                            skill='Caldari Cruiser', **kwargs)
            fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill('Light Missiles'),
                                            '{0}Damage'.format(damageType), ship.getModifiedItemAttr('shipBonusCC'),
                                            skill='Caldari Cruiser', **kwargs)
        #(-参考相似的effects填入函数及参数，可以多条)

class Effect8411(BaseEffect):
    """
    solarFlareShipBonusCCruiserShieldResistance

    Used by:
    Riemann	黎曼级
    """

    type = 'passive'

    @staticmethod
    def handler(fit, ship, context, projectionRange, **kwargs):
        #毒蜥级 1812 1813 1814 1815
        fit.ship.boostItemAttr('shieldEmDamageResonance', ship.getModifiedItemAttr('shipBonusSCC2'),
                               skill='Solarflare Cruiser Operation', **kwargs)
        fit.ship.boostItemAttr('shieldThermalDamageResonance', ship.getModifiedItemAttr('shipBonusSCC2'),
                               skill='Solarflare Cruiser Operation', **kwargs)
        fit.ship.boostItemAttr('shieldKineticDamageResonance', ship.getModifiedItemAttr('shipBonusSCC2'),
                               skill='Solarflare Cruiser Operation', **kwargs)
        fit.ship.boostItemAttr('shieldExplosiveDamageResonance', ship.getModifiedItemAttr('shipBonusSCC2'),
                               skill='Solarflare Cruiser Operation', **kwargs)
        #(-参考相似的effects填入函数及参数，可以多条)

class Effect8412(BaseEffect):
    """
    solarFlareShipBonusLMHMHAMFlightSpeed

    Used by:
    Riemann	黎曼级
    """

    type = 'passive'

    @staticmethod
    def handler(fit, ship, context, projectionRange, **kwargs):
        #狞獾级 1024 1025 2809
        fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill('Heavy Missiles'),
                                        'maxVelocity', ship.getModifiedItemAttr('shipBonusSCC'),
                                        skill='Solarflare Cruiser Operation', **kwargs)
        fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill('Light Missiles'),
                                        'maxVelocity', ship.getModifiedItemAttr('shipBonusSCC'),
                                        skill='Solarflare Cruiser Operation', **kwargs)
        fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill('Heavy Assault Missiles'),
                                        'maxVelocity', ship.getModifiedItemAttr('shipBonusSCC'),
                                        skill='Solarflare Cruiser Operation', **kwargs)
        #(-参考相似的effects填入函数及参数，可以多条)

class Effect8413(BaseEffect):
    """
    solarFlareShipBonusLMHMHAMExplosionRadius

    Used by:
    Riemann	黎曼级
    """

    type = 'passive'

    @staticmethod
    def handler(fit, ship, context, projectionRange, **kwargs):
        #狞獾级海军型 5387 5388
        fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill('Heavy Assault Missiles'),
                                        'aoeCloudSize', ship.getModifiedItemAttr('shipBonusCC2'),
                                        skill='Caldari Cruiser', **kwargs)
        fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill('Heavy Missiles'),
                                        'aoeCloudSize', ship.getModifiedItemAttr('shipBonusCC2'),
                                        skill='Caldari Cruiser', **kwargs)
        fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill('Light Missiles'),
                                        'aoeCloudSize', ship.getModifiedItemAttr('shipBonusCC2'),
                                        skill='Caldari Cruiser', **kwargs)
        #(-参考相似的effects填入函数及参数，可以多条)

class Effect8416(BaseEffect):
    """
    solarFlareShipBonusMedHybridTurretDmg

    Used by:
    Schwarzschild	史瓦西级
    """

    type = 'passive'

    @staticmethod
    def handler(fit, ship, context, projectionRange, **kwargs):
        #托勒克斯级 562
        fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill('Medium Hybrid Turret'),
                                      'damageMultiplier', ship.getModifiedItemAttr('shipBonusGC'),
                                      skill='Gallente Cruiser', **kwargs)
        #(-参考相似的effects填入函数及参数，可以多条)

class Effect8417(BaseEffect):
    """
    solarFlareShipBonusMedHybridTurretOptRange

    Used by:
    Schwarzschild	史瓦西级
    """

    type = 'passive'

    @staticmethod
    def handler(fit, ship, context, projectionRange, **kwargs):
        #伏波斯级 5959
        fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill('Medium Hybrid Turret'),
                                      'maxRange', ship.getModifiedItemAttr('shipBonusGC2'),
                                      skill='Gallente Cruiser', **kwargs)
        #(-参考相似的effects填入函数及参数，可以多条)

class Effect8418(BaseEffect):
    """
    solarFlareShipBonusMedHybridTurretTrackingSpeed

    Used by:
    Schwarzschild	史瓦西级
    """

    type = 'passive'

    @staticmethod
    def handler(fit, ship, context, projectionRange, **kwargs):
        #托勒克斯级 919
        fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill('Medium Hybrid Turret'),
                                      'trackingSpeed', ship.getModifiedItemAttr('shipBonusSGC2'),
                                      skill='Solarflare Cruiser Operation', **kwargs)
        #shipBonusSGC=10 shipBonusSGC2=7.5
        #(-参考相似的effects填入函数及参数，可以多条)

class Effect8419(BaseEffect):
    """
    solarFlareShipBonusGCruiserArmorRepair

    Used by:
    Schwarzschild	史瓦西级
    """

    type = 'passive'

    @staticmethod
    def handler(fit, ship, context, projectionRange, **kwargs):
        #狂怒者级海军型 7231
        fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill('Repair Systems'),
                                      'armorDamageAmount', ship.getModifiedItemAttr('shipBonusSGC2'),
                                      skill='Solarflare Cruiser Operation', **kwargs)
        # shipBonusSGC=10 shipBonusSGC2=7.5
        #(-参考相似的effects填入函数及参数，可以多条)

class Effect8422(BaseEffect):
    """
    solarFlareShipBonusMedProjectileTurretDmg

    Used by:
    Paixhans	匹希斯级
    """

    type = 'passive'

    @staticmethod
    def handler(fit, ship, context, projectionRange, **kwargs):
        #塞纳波级 968
        fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill('Medium Projectile Turret'),
                                      'damageMultiplier', ship.getModifiedItemAttr('shipBonusMC'),
                                      skill='Minmatar Cruiser', **kwargs)
        #(-参考相似的effects填入函数及参数，可以多条)

class Effect8423(BaseEffect):
    """
    solarFlareShipBonusMedProjectileTurretFalloff

    Used by:
    Paixhans	匹希斯级
    """

    type = 'passive'

    @staticmethod
    def handler(fit, ship, context, projectionRange, **kwargs):
        #塞纳波级 4512
        fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill('Medium Projectile Turret'),
                                      'falloff', ship.getModifiedItemAttr('shipBonusMC2'),
                                      skill='Minmatar Cruiser', **kwargs)
        #(-参考相似的effects填入函数及参数，可以多条)

class Effect8424(BaseEffect):
    """
    solarFlareShipBonusMedProjectileTurretRoF

    Used by:
    Paixhans	匹希斯级
    """

    type = 'passive'

    @staticmethod
    def handler(fit, ship, context, projectionRange, **kwargs):
        #刺客级 602
        fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill('Medium Projectile Turret'),
                                      'speed', ship.getModifiedItemAttr('shipBonusSMC'),
                                      skill='Solarflare Cruiser Operation', **kwargs)
        #(-参考相似的effects填入函数及参数，可以多条)

class Effect8425(BaseEffect):
    """
    solarFlareShipBonusMCruiserShieldBooster

    Used by:
    Paixhans	匹希斯级
    """

    type = 'passive'

    @staticmethod
    def handler(fit, ship, context, projectionRange, **kwargs):
        #流浪级 5559
        fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill('Shield Operation'),
                                      'shieldBonus', ship.getModifiedItemAttr('shipBonusSMC2'),
                                      skill='Solarflare Cruiser Operation', **kwargs)
        #(-参考相似的effects填入函数及参数，可以多条)

class Effect8458(BaseEffect):
    """
    solarFlareShipRoleBonusMedLaserOptRange

    Used by:
    Celsius	摄尔修斯级
    """

    type = 'passive'

    @staticmethod
    def handler(fit, ship, context, projectionRange, **kwargs):
        #启示级海军型 5382
        fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill('Medium Energy Turret'),
                                      'maxRange', ship.getModifiedItemAttr('roleBonus'), **kwargs)
        #(-参考相似的effects填入函数及参数，可以多条)

class Effect8459(BaseEffect):
    """
    solarFlareShipRoleBonusMissileReload

    Used by:
    Riemann	黎曼级
    """

    type = 'passive'

    @staticmethod
    def handler(fit, ship, context, projectionRange, **kwargs):
        #寒鸦级 6098
        fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill('Missile Launcher Operation'),
                                      'reloadTime', ship.getModifiedItemAttr('reloadTimeBonus'), **kwargs)
        #(-参考相似的effects填入函数及参数，可以多条)

class Effect8460(BaseEffect):
    """
    solarFlareShipRoleBonusMJDCoolDown

    Used by:
    Schwarzschild	史瓦西级
    """

    type = 'passive'

    @staticmethod
    def handler(fit, ship, context, projectionRange, **kwargs):
        #帕拉丁级 5560
        fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == 'Micro Jump Drive',
                                      'moduleReactivationDelay', ship.getModifiedItemAttr('roleBonus'), **kwargs)
        #(-参考相似的effects填入函数及参数，可以多条)

class Effect8461(BaseEffect):
    """
    solarFlareShipRoleBonusProjectileDamage

    Used by:
    Paixhans	匹希斯级
    """

    type = 'passive'

    @staticmethod
    def handler(fit, ship, context, projectionRange, **kwargs):
        # 塞纳波级 968
        fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill('Medium Projectile Turret'),
                                      'damageMultiplier', ship.getModifiedItemAttr('roleBonus'), **kwargs)
        #(-参考相似的effects填入函数及参数，可以多条)

class Effect8463(BaseEffect):
    """
    solarFlareShipRoleBonusABMWDOverloadSpeedBonus

    Used by:
    Mohs	莫斯级
    Stadion	斯特迪亚级
    Doppler	多普勒级
    Roentgen	伦琴级
    """

    type = 'passive'

    @staticmethod
    def handler(fit, ship, context, projectionRange, **kwargs):
        #十字军级 5889 5890
        fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill('Afterburner'),
                                      'overloadSpeedFactorBonus', ship.getModifiedItemAttr('roleBonus'), **kwargs)
        fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill('High Speed Maneuvering'),
                                      'overloadSpeedFactorBonus', ship.getModifiedItemAttr('roleBonus'), **kwargs)
        #(-参考相似的effects填入函数及参数，可以多条)

class Effect8464(BaseEffect):
    """
    solarFlareShipRoleBonusSmallHybridTurretDamageFixedBonus

    Used by:
    Doppler	多普勒级
    """

    type = 'passive'

    @staticmethod
    def handler(fit, ship, context, projectionRange, **kwargs):
        #夜魔侠级 1218
        fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill('Small Hybrid Turret'),
                                      'damageMultiplier', ship.getModifiedItemAttr('shipBonusRole1'), **kwargs)
        #(-参考相似的effects填入函数及参数，可以多条)

class Effect8465(BaseEffect):
    """
    solarFlareShipBonusMWDSigRadReductionSGF

    Used by:
    Doppler	多普勒级
    """

    type = 'passive'

    @staticmethod
    def handler(fit, ship, context, projectionRange, **kwargs):
        #十字军级 3766
        fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill('High Speed Maneuvering'),
                                      'signatureRadiusBonus', ship.getModifiedItemAttr('shipBonusSGF2'),
                                      skill='Solarflare Frigate Operation', **kwargs)
        #(-参考相似的effects填入函数及参数，可以多条)

class Effect8466(BaseEffect):
    """
    solarFlareShipBonusMWDSigRadReductionSMF

    Used by:
    Roentgen	伦琴级
    """

    type = 'passive'

    @staticmethod
    def handler(fit, ship, context, projectionRange, **kwargs):
        # 十字军级 3766
        fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill('High Speed Maneuvering'),
                                      'signatureRadiusBonus', ship.getModifiedItemAttr('shipBonusSMF2'),
                                      skill='Solarflare Frigate Operation', **kwargs)
        #(-参考相似的effects填入函数及参数，可以多条)