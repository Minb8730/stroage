'''

# 마린
name = "마린"
hp = 40
damage = 5

print("{0} 유닛이 생성되었습니다.".format(name))
print("체력{0}, 공격력{1}\n".format(hp, damage))

tank_name = "탱크"
tank_hp = 150
tank_damage = 35

print("{0} 유닛이 생성되었습니다.".format(tank_name))
print("체력{0}, 공격력{1}\n".format(tank_hp, tank_damage))

tank2_name = "탱크"
tank2_hp = 150
tank2_damage = 35

print("{0} 유닛이 생성되었습니다.".format(tank2_name))
print("체력{0}, 공격력{1}\n".format(tank2_hp, tank2_damage))

def attack(name, location, damage):
    print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력[ {2}]".format(name, location, damage))

attack(name, "1시", damage)
attack(tank_name, "1시", tank_damage)
attack(tank2_name, "1시", tank2_damage) 
# 중복되는 수십, 수백개를 변수 지정하기 힘듦 ex) tank1 tank2 그렇기 때문에 class라는 변수를 사용하면 붕어빵 틀을 사용하듯 찍어낼 수 있음.
'''

# init 함수 : 파이썬에서 쓰이는 생성자. 객체를 자동으로 호출 Ex)marine 이나 tank 는 Unit class 의 instance
class Unit: # 일반 유닛
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))
'''
# marine1 = Unit("마린", 40, 5)
# marine2 = Unit("마린", 40, 5)
# tank = Unit("탱크", 150, 35)

wraith1 = Unit("레이스", 80, 5)    #클레스 외부에서 작성한 것도 출력 가능
print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))

wraith2 = Unit("빼앗은 레이스", 80, 5)
wraith2.clocking = True #객체에 추가로 변수를 설정 가능

if wraith2.clocking == True :
    print("{0}는 현재 클로킹 상태입니다.".format(wraith2.name))
'''

class AttackUnit: # 공격 유닛
        def __init__(self, name, hp, damage):
            self.name = name
            self.hp = hp
            self.damage = damage
        
        def attack(self, location):
            print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
                .format(self.name, location, self.damage))
        def damaged(self, damage):
            print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
            self.hp -= damage
            print("{0} : 현재 체력은 {1} 입니다.".format(self.name, damage))
            if self.hp <= 0:
                print("{0} : 파괴되었습니다.".format(self.name))

firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")

firebat1.damaged(25)
firebat1.damaged(25)



