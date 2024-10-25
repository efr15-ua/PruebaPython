"""
import kkpaquete_Elias.suma as kps
print(kps.suma(3, 5))


from kkpaquete_Elias import suma
print(suma.suma(3,5))
"""

import kkpaquete_Elias as kp
import kkpaquete_Elias.extra as kpx
from math import sin

print(kp.suma(3, 5))
print(kp.resta(3, 5))
print(kpx.multiplica(3, 5))
print(kpx.divide(3, 5))
print(sin(kpx.pi))
