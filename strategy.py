from abc import ABC, abstractmethod

class WeaponBehavior(ABC):
    
    @abstractmethod
    def use_weapon(self):
        pass

class KnifeBehavior(WeaponBehavior):
    
    def use_weapon(self):
        return "Stabbing with Knife..."
        
        
class AxeBehavior(WeaponBehavior):
    
    def use_weapon(self):
        return "Hacking with Axe..."
        
    
class BowAndArrowBehavior(WeaponBehavior):
    
    def use_weapon(self):
        return "Piercing with Bow and Arrow..."
        

class SwordBehavior(WeaponBehavior):
    
    def use_weapon(self):
        return "Slashing with Sword..."
        

class Character(ABC):
    def __init__(self, weapon: WeaponBehavior):
        self.weapon = weapon
        
    
    def fight(self):
        return self.weapon.use_weapon()
    
    def set_weapon(self, weapon : WeaponBehavior):
        self.weapon = weapon
        
    @abstractmethod
    def display(self):
        pass

class King(Character):
    def __init__(self):
        super().__init__(SwordBehavior())
        
    def display(self):
        return "I'm the King!"
    

class Queen(Character):
    def __init__(self):
        super().__init__(KnifeBehavior())
        
    def display(self):
        return "I'm the Queen!"
        
class Knight(Character):
    def __init__(self):
        super().__init__(BowAndArrowBehavior())
        
    def display(self):
        return "I'm a Knight!"
        
class Troll(Character):
    def __init__(self):
        super().__init__(AxeBehavior())
        
    def display(self):
        return "I'm the ugly Troll!"
        
def main():
    king = King()
    queen = Queen()
    knight = Knight()
    troll = Troll()
    
    print(f"{king.display()}, {king.fight()}")
    print(f"{queen.display()}, {queen.fight()}")
    print(f"{knight.display()}, {knight.fight()}")
    print(f"{troll.display()}, {troll.fight()}")
    
    print("")
    
    king.set_weapon(AxeBehavior())
    queen.set_weapon(BowAndArrowBehavior())
    knight.set_weapon(SwordBehavior())
    troll.set_weapon(KnifeBehavior())
    
    print(f"{king.display()}, {king.fight()}")
    print(f"{queen.display()}, {queen.fight()}")
    print(f"{knight.display()}, {knight.fight()}")
    print(f"{troll.display()}, {troll.fight()}")

if __name__ == '__main__':
    
    main()


    
