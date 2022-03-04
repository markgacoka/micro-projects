'''
The rgb() method is incomplete. Complete the method so that passing in RGB decimal values will result in a hexadecimal representation being returned. The valid decimal values for RGB are 0 - 255. Any (r,g,b) argument values that fall out of that range should be rounded to the closest valid value.

The following are examples of expected output values:

rgb(255, 255, 255) # returns FFFFFF
rgb(255, 255, 300) # returns FFFFFF
rgb(0,0,0) # returns 000000
rgb(148, 0, 211) # returns 9400D3
'''

def rgb(r, g, b):
    colors = [r,g,b]
    for count, i in enumerate(colors):
        if i > 255:
            colors[count] = 255
        if i < 0:
            colors[count] = 0
            
    r,g,b = colors[0], colors[1], colors[2]
    return "{:02x}{:02x}{:02x}".format(r,g,b).upper()