O = object
class D(O): pass
class E(O): pass
class F(O): pass
class B(D,E): pass
class C(F,D): pass
class A(B,C): pass

#print sequence of class's explode
print(A.__mro__)

"""
O
DO
EO
FO
BDEO
CFDO
ABC/DE/FD/O # There is D in backside, So first D dismiss
 - ABCFDEO
 - C3 liner norms
"""
