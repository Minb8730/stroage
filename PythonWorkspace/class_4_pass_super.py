from random import*


class Unit: # 메딕 부모 클래스라 부르고 아래 상속 받는 클래스를 자식 클래스라고 부른다.
        def __init__(self, name, hp, speed):
            self.name = name
            self.hp = hp
            self.speed = speed
            print("{0} 유닛이 생성되었습니다.".format(name))

        def move(self, location):
            print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))
        
        def damaged(self, damage):
            print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
            self.hp -= damage
            print("{0} : 현재 체력은 {1} 입니다.".format(self.name, damage))
            if self.hp <= 0:
                print("{0} : 파괴되었습니다.".format(self.name))


# 상속
class AttackUnit(Unit): # 공격 유닛   위의 (Unit) 의 아랫부분이 중복되기 때문에 그대로 가져와서 받음 "상속"
        def __init__(self, name, hp, speed, damage):
            Unit.__init__(self, name, hp, speed)
            self.damage = damage
        
        def attack(self, location):
            print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
                .format(self.name, location, self.damage))

#마린
class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "마린", 40, 1, 5)

    def stimpack(self): #스팀팩 함수
        if self.hp > 10:
            self.hp -= 10
            print("{0} : 스팀팩을 사용합니다. (HP 10 감소)".format(self.name))
        else:
            print("{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다.".format(self.name))

#탱크
class Tank(AttackUnit):
    seize_developed = False
    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 1, 35)
        self.seize_mode = False

    def set_seize_mode(self):
        if Tank.seize_developed == False:
            return # 시즈 개발이 안됐을 때 코드를 나감


        if self.seize_mode == False:  # 현재 시즈모드가 아닐 때 -> 시즈모드 
            print("{0} : 시즈모드로 전환합니다.".format(self.name))
            self.damage *= 2
            self.seize_mode = True

        else :  # 현재 시즈모드 일 때 -> 시즈모드 해제
            print("{0} : 시즈모드로 해제합니다.".format(self.name))
            self.damage /= 2
            self.seize_mode = False





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
        self.fly(self.name, location)


class wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
        self.clocked = False # 클로킹 모드 해제 상태

    def clocking(self):
        if self.clocked == True:
            print("{0} : 클로킹 모드 해제합니다.".format(self.name))
            self.clocked = False
        else : #클로킹 모드 해제 -> 모드 설정
            print("{0} : 클로킹 모드 설정합니다.".format(self.name))
            self.clocked = True

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    print("player : gg")
    print("[player] 님이 게임에서 퇴장하셨습니다.")


#게임 시작
game_start()

m1 = Marine()
m2 = Marine()
m3 = Marine()

t1 = Tank()
t2 = Tank()

w1 = wraith()

#유닛 일괄 관리 (생성 된 모든 유닛 append)
attack_Units = []
attack_Units.append(m1)
attack_Units.append(m2)
attack_Units.append(m3)
attack_Units.append(t1)
attack_Units.append(t2)
attack_Units.append(w1)

# 전군 이동
for unit in attack_Units:
    unit.move("1시")

#탱크 시즈모드 개발
Tank.seize_developed = True
print("[알림] 탱크 시즈 모드 개발이 완료되었습니다.")

# 공격 모드 준비 (마린 : 스팀팩, 탱크 : 시즈모드 , 레이스 : 클로킹)
for unit in attack_Units:
    if isinstance(unit, Marine):
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.set_seize_mode()
    elif isinstance(unit, wraith):
        unit.clocking()


#전군 공격
for unit in attack_Units:
    unit.attack("1시")

#전군 피해
for unit in attack_Units:
    unit.damaged(randint(5, 20)) #공격은 랜덤으로 받음 (5~20)

# 게임 종료
game_over()



'''
#건물
class BuildingUnit(Unit):
    def __init__(self, name, hp, location) :
        #Unit.__init__(self, name, hp, 0) 또는 밑의 코드
        super().__init__(name, hp, 0) #부모 클래스의 초기화를 위해서 self 를 지워준다.
        self.location = location
        
'''
'''
#'서플라이 디팟
supply_depot = BuildingUnit("서플라이 디폿", 700, "7시")

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    pass #일단은 아무것도 하지 않고 완성된 것처럼 넘어간다.


game_start()
game_over()

'''