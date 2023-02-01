import femin

## Geometry
node = 10   # Max 40
obj_seg = 5

# Pellet Specification
inner_diameter_pellet = [0.0] * node # cm
outer_diameter_pellet = [0.820] * node # cm
p_pelet = [1.0]*node # cm
enrichment_pellet = [0.04] * node
density_pellet = [0.97] * node # Theorical Density Ratio
ax_pelet = [10.0]*node  # panjang pada tiap 10 segment
#weight_pellet = 550  # gram
femin.create_pellet(obj_seg, inner_diameter_pellet, outer_diameter_pellet, p_pelet, \
                    density_pellet, enrichment_pellet, ax_pelet)#, weight_pellet)


# Cladding Specification
id_clad = 0.83 # cm
od_clad = 0.97 # cm
mat_clad = 0  # 0 = RA Material, 1 = SR Material
femin.create_clad(mat_clad, id_clad, od_clad)


# Dish Specification
dish_dia = 0.6 # cm
dish_depth = 0.02 # cm
dish_botDia = 0.6 # cm
femin.create_dish(dish_dia, dish_depth, dish_botDia)


# Plenum Specification
up_plenum = 5 # cm^3
low_plenum = 5 # cm^3
femin.create_plenum(up_plenum, low_plenum)


# Gap Specification
gas_pressure = 1 # MPa
He_comp = 0.94     # %
Xe_comp = 0.01     # %
Kr_comp = 0.03     # %
N2_comp = 0.02     # %
femin.create_gap(gas_pressure, He_comp, N2_comp, Kr_comp, Xe_comp)


## History Data
# Random Relative Power Profile
import random
ax = [[], []]
for array in ax:
    average = 1
    std_dev = 0.1
    avg = 0
    while avg < 1:
        array.clear()
        for point in range(node):
            array.append(abs(random.normalvariate(average, std_dev)))
        avg = sum(array)/len(array)
    array.sort()
    for num in range(1, int(len(array)/2)):
        array.insert(-num, array.pop(num))
    array.insert(int(len(array)/2), array.pop(-1))
femin.create_pf([ax[0], ax[1]])

# Random Run
import random
from math import floor
import time as tms

distburnup = [5000, 6000, 8000]
maxburnup1 = 30000
uncern_lhr = [-30, -20, -10, 0, 10]
time = []  # Hour
total_init = tms.time()
Iter = 0
for vardisr in distburnup:
    burnup = [0, 1000, 2000]
    lhr = [0.01, 130, 200]
    cool_temp = [558.15]  # Kelvin
    cool_pressure = [15.4]  # MPa
    cool_velocity = [3.04]  # m/s
    fast_nFlux = []  # n/cm^2 s
    IT = []  # # 1 ON, 0 OFF
    IS = []  # # 1 ON, 0 OFF
    IP_opt = [1, 0]
    Iter += 1

    while (vardisr + burnup[-1]) < maxburnup1:
        burnup.append(vardisr + burnup[-1])
        lhr.append(270 + random.choice(uncern_lhr))

    maxburnup2 = 60000
    burnup.extend([burnup[-1] + 10, burnup[-1] + 15, burnup[-1] + 1000])
    lhr.extend([10, 90, 170])

    while (vardisr + burnup[-1]) < maxburnup2:
        burnup.append(vardisr + burnup[-1])
        lhr.append(270 + random.choice(uncern_lhr))

    halfBU = floor(len(burnup) / 2)
    femin.create_bu_hist([burnup[:halfBU], burnup[halfBU:(2*halfBU)]])
    femin.create_lhr_hist([lhr[:halfBU], lhr[halfBU:(2*halfBU)]])
    femin.create_nflux_hist(fast_nFlux)
    femin.create_time_hist(time)

    cool_pressure *= int(halfBU * 2)
    cool_velocity *= int(halfBU * 2)
    cool_temp *= int(halfBU * 2)
    femin.create_coolpress_hist([cool_pressure[:halfBU], cool_pressure[halfBU:(2*halfBU)]])
    femin.create_coolvelocity_hist([cool_velocity[:halfBU], cool_velocity[halfBU:(2*halfBU)]])
    femin.create_cooltemp_hist([cool_temp[:halfBU], cool_temp[halfBU:(2*halfBU)]])

    IT *= halfBU
    IS *= halfBU
    IP = []
    for num in range(len(burnup)-1):
        if IP.count(1) > 3:
            IP.append(0)
        else:
            IP.append(random.choice(IP_opt))
    IP.append(1)
    femin.create_iPrint_opt([IP[:halfBU], IP[halfBU:(2*halfBU)]])
    femin.create_iTime_opt(IT)
    femin.create_iState_opt(IS)

    femin.preview()
    init = tms.time()
    femin.generate(f"Tes 2 Input {Iter}.txt")
    femin.run_femaxi6(f"Tes 2 Input {Iter}.txt", f"Tes 2 Output {Iter}.txt")
    end = tms.time()
    print(f"Calculated Time {Iter} ({vardisr})= {end - init}")
    del burnup, lhr, cool_velocity, cool_pressure, cool_temp, IP, IT, IS


total_end = tms.time()
print(f"Total calculated time = {total_end - total_init}")
