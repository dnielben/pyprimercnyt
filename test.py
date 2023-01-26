import libcplx as cplx

passed =0
failed =0

c1 = (3,-8)
c2 = (4,6)
resp = cplx.sumacplx((3,-8),(4,6))
 
if resp[0] == 7 and resp[1] == -2:
    passed += 1
else:
    failed+=1 

print("passed:",passed,"failed:",failed)