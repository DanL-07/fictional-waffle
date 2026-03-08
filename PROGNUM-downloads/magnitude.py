# Sirius data
apparentMagnitude = float(input ("Enter apparent magnitude: "))
absoluteMagnitude = float(input ("Enter absolute magnitude: "))

# The distance is related to the magnitudes as m-M=5.Log(d/10)
# 1 Parsec = 3.26164 ly

m = apparentMagnitude
M = absoluteMagnitude

print (f'distance is equal to = {10.0 * pow( 10.0, (m-M)/5.0 ) * 3.26164}pc')

