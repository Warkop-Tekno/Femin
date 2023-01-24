from . import geo
from . import hist_data
from . import string


def gfp_pellet():
    # Pellet
    tmp_key = 'pellet_keys = ["id", "od", "l_pellet", "chamf", "dish", "enrch", "den", "l_node"]\n'
    tmp_val = 'pellet = {\n'
    for key in geo.pellet:
        tmp_val += f'\t"{key}": ['
        try:
            for val in geo.pellet[key]:
                tmp_val += f'"{string.rounding(val)}", '
            tmp_val += "],\n"
        except TypeError:
            tmp_val += f'"{geo.pellet["weight"]}"], \n'

    # Chamfer
    tmp_val += '\t"chamf": ['
    for val in geo.pellet["id"]:
        if len(geo.chamfer) > 0:
            tmp_val += '"*", '
        else:
            tmp_val += '"", '
    tmp_val += "],\n"

    tmp_val += '\t"chamf_val": ['
    if len(geo.chamfer) > 0:
        tmp_val += '"' + string.rounding(geo.chamfer["wid"]) + '", "' + string.rounding(geo.chamfer["dep"]) + '", '
    else:
        tmp_val += '"-", "-", '
    tmp_val += "],\n"

    # Dish
    tmp_val += '\t"dish": ['
    for val in geo.pellet["id"]:
        if len(geo.dish) > 0:
            if geo.dish["bot"] > 0:
                tmp_val += '"**", '
            else:
                tmp_val += '"*", '
        else:
            tmp_val += '"", '
    tmp_val += "],\n"

    tmp_val += '\t"dish_val": ['
    if len(geo.dish) > 0:
        tmp_val += '"' + string.rounding(geo.dish["dia"]) + '", "' + string.rounding(geo.dish["dep"]) + '", "' \
                   + string.rounding(geo.dish["bot"]) + '"'
    else:
        tmp_val += '"-", "-", "-", '
    tmp_val += "],\n"

    tmp_val += '}\n'

    # Cladding
    tmp_val += 'clad_key = ['
    for key in geo.clad:
        tmp_val += f'"{key}",'
    tmp_val += ']\n'

    tmp_val += 'clad = {\n'
    for key in geo.clad:
        tmp_val += f'\t"{key}": [{geo.clad[key]}],\n'
    tmp_val += '}\n'

    # Plenum
    tmp_val += 'plenum_key = ['
    for key in geo.plenum:
        tmp_val += f'"{key}",'
    tmp_val += ']\n'

    tmp_val += 'plenum = {\n'
    for key in geo.plenum:
        tmp_val += f'\t"{key}": [{geo.plenum[key]}],\n'
    tmp_val += '}\n'

    # Gap
    tmp_val += 'gap_key = ['
    for key in geo.gap:
        tmp_val += f'"{key}",'
    tmp_val += ']\n'

    tmp_val += 'gap = {\n'
    for key in geo.gap:
        tmp_val += f'\t"{key}": [{geo.gap[key]}],\n'
    tmp_val += '}\n'

    # History data
    tmp_val += 'hist_keys = ['
    for var in hist_data.pwr_hist:
        tmp_val += f'"{var}",'
    tmp_val += ']\n'

    tmp_val += 'hist = {\n'
    for key in hist_data.pwr_hist:
        tmp_val += f'\t"{key}": ['
        for val in hist_data.pwr_hist[key]:
            tmp_val += f'"{string.rounding(val)}", '
        tmp_val += "],\n"
    tmp_val += '}\n'

    # Axial Segment Peaking Factor
    tmp_val += 'ax_keys = ['
    for var in hist_data.ax_seg_pf:
        tmp_val += f'"{var}",'
    tmp_val += ']\n'

    tmp_val += 'ax = {\n'
    for key in hist_data.ax_seg_pf:
        tmp_val += f'\t"{key}": ['
        for val in hist_data.ax_seg_pf[key]:
            tmp_val += f'"{string.rounding(val)}", '
        tmp_val += "],\n"
    tmp_val += '}\n'

    return tmp_key + tmp_val


def gen_for_preview():
    f = open("femin/view/load.js", "w")
    f.write(gfp_pellet())
    f.close()


def text(data, key_var, ax, point):
    try:
        var_list = data[key_var + str(ax + 1)][point]
        if point > 0:
            if var_list == data[key_var + str(ax + 1)][point - 1]:
                var_list = " "
        if ax > 0:
            if var_list == data[key_var + str(ax)][point]:
                var_list = " "
    except KeyError:
        var_list = " "
    except IndexError:
        var_list = " "
    return var_list


def gff_pellet():
    jml_node = len(geo.pellet["od"])
    obj = 6 ### input
    tmp_text = string.fill_char([[jml_node, 10], [obj, 10]]) + "\n"
    tmp_text += string.fill_char([[geo.clad["mat"], 10],
                                  [geo.clad["id"], 10],
                                  [geo.clad["od"], 10]]) + "\n"
    for i in range(len(geo.pellet["od"])):
        if len(geo.dish) > 0:
            tmp_text += string.fill_char(2, 10)
        else:
            tmp_text += string.fill_char(0, 10)
        if len(geo.chamfer) > 0:
            tmp_text += string.fill_char(1, 10)
        else:
            tmp_text += string.fill_char(0, 10)
        tmp_text += string.fill_char([[geo.pellet["id"][i], 10, "F"],
                                      [geo.pellet["od"][i], 10, "F"],
                                      [geo.pellet["l_pellet"][i], 10, "F"]])

        tmp_text += string.fill_char([[geo.pellet["enrch"][i], 10, "F"],
                                      [geo.pellet["den"][i], 10, "F"],
                                      [geo.pellet["l_node"][i], 10, "F"]]) + "\n"

    if len(geo.dish) > 0:
        tmp_text += string.fill_char([[geo.dish["dia"], 10, "F"],
                                      [geo.dish["dep"], 10, "F"],
                                      [geo.dish["bot"], 10, "F"]]) + "\n"
    if len(geo.chamfer) > 0:
        tmp_text += string.fill_char([[geo.chamfer["wid"], 10, "F"],
                                      [geo.chamfer["dep"], 10, "F"]]) + "\n"

    tmp_text += string.fill_char([[geo.plenum["up_vol"], 10, "F"],
                                  [geo.gap["init_gas_pressure"], 10, "F"],
                                  [geo.gap["init_He_comp"], 10, "F"],
                                  [geo.gap["init_N2_comp"], 10, "F"],
                                  [geo.gap["init_Kr_comp"], 10, "F"],
                                  [geo.gap["init_Xe_comp"], 10, "F"],
                                  [geo.pellet["weight"], 10, "F"],
                                  [geo.plenum["low_vol"], 10, "F"]]) + "\n"

    point = 0
    for key in hist_data.pwr_hist:
        if key[0:8] == "coolTemp":
            point += len(hist_data.pwr_hist[key])
    tmp_text += string.fill_char(point, 10) + "\n"


    for ax in range(len(hist_data.ax_seg_pf)):
        tmp_text += string.fill_char([[text(hist_data.pwr_hist, "time_", ax, 0), 10, "F"],
                                      [text(hist_data.pwr_hist, "burnup_", ax, 0), 10, "F"],
                                      [text(hist_data.pwr_hist, "lhr_", ax, 0), 10, "F"],
                                      [text(hist_data.pwr_hist, "nflux_", ax, 0), 10, "F"],
                                      [text(hist_data.pwr_hist, "coolTemp_", ax, 0), 10, "F"],
                                      [text(hist_data.pwr_hist, "coolPress_", ax, 0), 10, "F"],
                                      [text(hist_data.pwr_hist, "iTime opt_", ax, 0), 5],
                                      [text(hist_data.pwr_hist, "iPrint opt_", ax, 0), 5],
                                      [text(hist_data.pwr_hist, "iState opt_", ax, 0), 5],
                                      [text(hist_data.pwr_hist, "coolVelocity_", ax, 0), 5, "F"]]) + '\n'

        lim = 0
        for num_seg in range(len(hist_data.ax_seg_pf["ax_seg_1"])):
            lim += 1
            tmp_text += string.fill_char(text(hist_data.ax_seg_pf, "ax_seg_", ax, num_seg), 8, "F")
            if lim // 8:
                lim -= 8
                tmp_text += '\n'
        if lim < 8:
            tmp_text += (8 - lim) * ' ' * 8
        tmp_text += string.fill_char(len(hist_data.pwr_hist["coolTemp_" + str(ax + 1)]), 6) + '\n'


        for point in range(1, len(hist_data.pwr_hist["coolTemp_"+ str(ax+1)])):
            tmp_text += string.fill_char([[text(hist_data.pwr_hist, "time_", ax, point), 10, "F"],
                                          [text(hist_data.pwr_hist, "burnup_", ax, point), 10, "F"],
                                          [text(hist_data.pwr_hist, "lhr_", ax, point), 10, "F"],
                                          [text(hist_data.pwr_hist, "nflux_", ax, point), 10, "F"],
                                          [text(hist_data.pwr_hist, "coolTemp_", ax, point), 10, "F"],
                                          [text(hist_data.pwr_hist, "coolPress_", ax, point), 10, "F"],
                                          [text(hist_data.pwr_hist, "iTime opt_", ax, point), 5],
                                          [text(hist_data.pwr_hist, "iPrint opt_", ax, point), 5],
                                          [text(hist_data.pwr_hist, "iState opt_", ax, point), 5],
                                          [text(hist_data.pwr_hist, "coolVelocity_", ax, point), 5, "F"]])
            tmp_text += '\n'
    tmp_text += "STOP"
    return tmp_text


def gen_for_femaxi(file_name):
    f = open(file_name, "w")
    tmp_text = gff_pellet()
    f.write(tmp_text)
    f.close()
