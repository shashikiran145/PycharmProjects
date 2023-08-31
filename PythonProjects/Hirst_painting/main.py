import colorgram

colors = colorgram.extract('hirst_painting.jpg', 10)

rgb_colors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    color = (r, g, b)
    rgb_colors.append(color)

print(rgb_colors)







