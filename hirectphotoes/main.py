import colorgram as cg

colors = cg.extract('images.jpg', 20)
colors_list = []
for item in colors:
    colors_list.append((item.rgb.r, item.rgb.g, item.rgb.b))


