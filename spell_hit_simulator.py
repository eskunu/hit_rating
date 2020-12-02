import random
import matplotlib.pyplot as plt

def simulator(dmg_low, dmg_high, spellpower, hit_rating):
    base_spell_damage = random.randint(dmg_low, dmg_high)
    spc = spellpower / 3.5 * 3
    x = random.randint(0, 100) / 100
    if x <= hit_rating:
        damage_output = base_spell_damage + spc
    else:
        damage_output = 0
    return dmg_low, dmg_high, spellpower, hit_rating, damage_output

def output(rate, sp, casts, cap, pltlabel):
    damage = [simulator(482,538,sp,rate)[4] / 3 for i in range(casts)]
    average = sum(damage) / len(damage)
    print("Average:", average, "Top " + str(cap) + " average:", sum(damage[0:cap]) / len(damage[0:cap]))
    a = [sum(damage[0:i+1]) / len(damage[0:i+1]) for i in range(len(damage))]
    b = plt.plot(a, label=pltlabel)
    return a, b

output(.84, 400, 30, 1000, '.84 hit rating')
output(.99, 400, 30, 1000, '.99 hit rating')
output(.84, 550, 30, 1000, '.84 hit +175 sp')
plt.xlabel("Casts (Inclusive)")
plt.ylabel("Damage per second")
plt.grid()
plt.title("Hit Rating Comparison ")
plt.legend(loc="upper right")
plt.savefig("images/image9.png")
plt.show()