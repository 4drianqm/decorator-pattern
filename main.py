from fighter import Fighter
from wizard import Wizard
from sword import Sword
from shield import Shield

fighter = Fighter()
fighter_with_shield = Shield(fighter)
fighter_with_shield_and_sword = Sword(fighter_with_shield)

wizard = Wizard()
wizard_with_shield = Shield(wizard)

damage = fighter_with_shield_and_sword.calculate_damage()
print('fighter Damage: ', damage)

wizard_with_shield.receive_damage(damage)
print('Health points: ', wizard.life_points)
