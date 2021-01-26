class Unit: # 메딕 부모 클래스라 부르고 아래 상속 받는 클래스를 자식 클래스라고 부른다.
        def __init__(self, name, hp, speed):
            self.name = name
            self.hp = hp
            self.speed = speed

        def move(self, location):
            print("[지상 유닛 이동]")
            print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))


# 상속
class AttackUnit(Unit): # 공격 유닛   위의 (Unit) 의 아랫부분이 중복되기 때문에 그대로 가져와서 받음 "상속"
        def __init__(self, name, hp, speed, damage):
            Unit.__init__(self, name, hp, speed)
            self.damage = damage


# 드랍쉽
class Flyable : # 날 수 있는 기능을 가진 클래스
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))


# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) #지상 speed 0
        Flyable.__init__(self, flying_speed)
    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)
#벌쳐
vulture = AttackUnit("벌쳐", 80, 10, 20)

#배틀크루저
battlecruiser = FlyableAttackUnit("배틀크루져", 500, 25, 3)

vulture.move("11시")
# battlecruiser.fly(battlecruiser.name, "9시")
battlecruiser.move("9시")



