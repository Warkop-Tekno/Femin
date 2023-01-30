import femin

## Geometry
node = 10

# Pellet Specification
id_pelet = [0.0]*node
od_pelet = [0.820]*node
p_pelet = [1.0]*node
enrch_pelet = [0.04]*node
den_pelet = [0.95]*node
ax_pelet = [10.0]*node

# Cladding Specification
id_clad = 0.83
od_clad = 0.97
mat_clad = 1  #

# Dish Specification
dish_dia = 0.6218
dish_depth = 0.021
dish_botDia = 0

# Plenum Specification
up_plenum = 8
gas_pressure = 1
He_comp = 1
Xe_comp = 0
Kr_comp = 0
N2_comp = 0
weight_pellet = 550
low_plenum = 0

## History Data
ax1 = [.62, .865, 1, 1.149, 1.19, 1.163, 1.005, .931, .786, .541]           # 8
ax2 = [.656, .903, 1.098, 1.167, 1.201, 1.174, 1.073, .959, .817, .581]     # 8
ax3 = [.798, 1.002, 1.104, 1.128, 1.122, 1.104, 1.086, 1.032, .912, .708]   # 6

# Power History Data
time = []*22
burnup = [    0,    10, 15000, 20000, 25000, 28000, 30000, 30500,\
          30501, 30510, 35000, 40000, 42000, 46000, 49000, 50000,\
          50010, 50110, 52000, 55000, 57000, 59900]       # MWd/tU

lin_heatrate = [.01, 114.5, 250, 270, 290, 270, 260, 100,\
                  1,   100, 200, 220, 210, 205, 190, 180,\
                  6,   170, 160, 150, 140, 110]           #W/cm

cool_temp = [558.15]*22     # Kelvin
cool_pressure = [15.4]*22  # MPa
cool_velocity = [3.04]*22   # m/s
fast_nFlux = []*22   # Default.....
IT = []*22
IP = [1, 0, 0, 0, 1, 0, 0, 0,\
      1, 0, 1, 0, 0, 0, 0, 0,\
      1, 1, 0, 0, 0, 1]          # 1 ON, 0 OFF
IS = []*22

# Create geometry
femin.create_pellet(id_pelet, od_pelet, p_pelet, den_pelet, enrch_pelet, ax_pelet)
femin.create_clad(mat_clad, id_clad, od_clad)
femin.create_plenum(up_plenum, low_plenum)
femin.create_gap(gas_pressure, He_comp, N2_comp, Kr_comp, Xe_comp)
femin.create_dish(dish_dia, dish_depth, dish_botDia)

# Create history data
femin.create_time_hist(time)
femin.create_bu_hist([burnup[:8], burnup[8:16], burnup[16:]])
femin.create_lhr_hist([lin_heatrate[:8], lin_heatrate[8:16], lin_heatrate[16:]])
femin.create_nflux_hist(fast_nFlux)

femin.create_coolpress_hist([cool_pressure[:8], cool_pressure[8:16], cool_pressure[16:]])
femin.create_coolvelocity_hist([cool_velocity[:8], cool_velocity[8:16], cool_velocity[16:]])
femin.create_cooltemp_hist([cool_temp[:8], cool_temp[8:16], cool_temp[16:]])

femin.create_iPrint_opt([IP[:8], IP[8:16], IP[16:]])
femin.create_iTime_opt(IT)
femin.create_iState_opt(IS)

femin.create_pf([ax1, ax2, ax3])


# Testing
# print("\nInput awal:")
# print("pellet\n", femin.pellet)
# print("clad\n", femin.clad)
# print("dish\n", femin.dish)
# print("plenum\n", femin.plenum)
# print("power history data\n", femin.pwr_hist)
# print("Axial Segment Peak Factor\n", femin.ax_seg_pf)
# femin.save("data.h5")

femin.load("data.h5")
# print("\n \n")
# print("Hasil load file:\n")
# print("pellet\n", femin.pellet)
# print("clad\n", femin.clad)
# print("dish\n", femin.dish)
# print("plenum\n", femin.plenum)
# print("power history data\n", femin.pwr_hist)
# print("Axial Segment Peak Factor\n", femin.ax_seg_pf)

# Preview
femin.preview()
femin.generate("tes_gen.txt")