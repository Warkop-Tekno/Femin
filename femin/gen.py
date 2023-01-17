from . import geo
from . import string

def gfp_pellet():
    tmp_key = 'pellet_keys = ["id", "od", "l_pellet", "chamf", "dish", "enrch", "den", "l_node"]\n'
    tmp_val = 'pellet = {\n'
    for key in geo.pellet:
        tmp_val += f'\t"{key}": ['
        for val in geo.pellet[key]:
            tmp_val += f'"{string.rounding(val)}", '
        tmp_val += "],\n"
    

    tmp_val += '\t"chamf": ['
    for val in geo.pellet["id"]:
        if len(geo.chamfer)>0:
            tmp_val += '"*", '
        else:
            tmp_val += '"", '
    tmp_val += "],\n"

    tmp_val += '\t"chamf_val": ['
    if len(geo.chamfer)>0:
        tmp_val += '"'+string.rounding(geo.chamfer["wid"])+'", "'+string.rounding(geo.chamfer["dep"])+'", '
    else:
        tmp_val += '"-", "-", '
    tmp_val += "],\n"


    tmp_val += '\t"dish": ['
    for val in geo.pellet["id"]:
        if len(geo.dish)>0:
            if geo.dish["bot"]>0:
                tmp_val += '"**", '
            else:
                tmp_val += '"*", '
        else:
            tmp_val += '"", '
    tmp_val += "],\n"

    tmp_val += '\t"dish_val": ['
    if len(geo.dish)>0:
        tmp_val += '"'+string.rounding(geo.dish["dia"])+'", "'+string.rounding(geo.dish["dep"])+'", "' \
            +string.rounding(geo.dish["bot"])+'"'
    else:
        tmp_val += '"-", "-", "-", '
    tmp_val += "],\n"

    tmp_val += '}\n'
    return tmp_key+tmp_val

def gen_for_preview():
    f = open("femin/view/load.js", "w")
    f.write(gfp_pellet())
    f.close()

def gff_pellet():
    jml_node = len(geo.pellet["od"])
    obj = 6
    tmp_text = string.fill_char([[jml_node, 10], [obj, 10]])+"\n"
    tmp_text += string.fill_char([[geo.clad["mat"], 10], [geo.clad["id"], 10], [geo.clad["od"], 10]])+"\n"
    for i in range(len(geo.pellet["od"])):
        if len(geo.dish)>0:
            tmp_text += string.fill_char(2, 10)
        else:
            tmp_text += string.fill_char(0, 10)
        if len(geo.chamfer)>0:
            tmp_text += string.fill_char(1, 10)
        else:
            tmp_text += string.fill_char(0, 10)
        tmp_text += string.fill_char([[geo.pellet["id"][i], 10, "F"], [geo.pellet["od"][i], 10, "F"], [geo.pellet["l_pellet"][i], 10, "F"]])
        tmp_text += string.fill_char([[geo.pellet["enrch"][i], 10, "F"], [geo.pellet["den"][i], 10, "F"], [geo.pellet["l_node"][i], 10, "F"]])+"\n"
    
    if len(geo.dish)>0:
        tmp_text += string.fill_char([[geo.dish["dia"], 10, "F"], [geo.dish["dep"], 10, "F"], [geo.dish["bot"], 10, "F"]])+"\n"
    if len(geo.chamfer)>0:
        tmp_text += string.fill_char([[geo.chamfer["wid"], 10, "F"], [geo.chamfer["dep"], 10, "F"]])+"\n"

    return tmp_text

def gen_for_femaxi(file_name):
    f = open(file_name, "w")
    tmp_text = gff_pellet()
    f.write(tmp_text)
    f.close()