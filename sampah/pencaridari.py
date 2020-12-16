from trigonometri import *

def sin_αl():
    depan_α, samping_α = sin_α.split("/")
    depan_α=int(depan_α)
    samping_α=int(samping_α)
    return samping_α, depan_α, sin_α
    trigonometri.pencariSatu()
    
def cos_αl():
    miring_α, samping_α = cos_α.split("/")
    miring_α=int(miring_α)
    samping_α=int(samping_α)
    return samping_α, miring_α, cos_α
    pencariSatu()
    
def tan_αl():
    depan_α, miring_α = tan_α.split("/")
    depan_α=int(depan_α)
    miring_α=int(miring_α)
    return miring_α, depan_α, tan_α
    pencariSatu()
    
def cot_αl():
    miring_α, depan_α = cot_α.split("/")
    miring_α=int(miring_α)
    depan_α=int(depan_α)
    return miring_α, depan_α, cot_α
    pencariSatu()
    
def sec_αl():
    samping_α, miring_α = sec_α.split("/")
    samping_α=int(samping_α)
    miring_α=int(miring_α)
    return samping_α, miring_α, sec_α
    pencariSatu()
    
def csc_αl():
    samping_α, depan_α = csc_α.split("/")
    samping_α=int(samping_α)
    depan_α=int(depan_α)
    return samping_α, depan_α, csc_α
    pencariSatu()



if sin_α.find("/") > 0:
    sin_αl()
else :
    sin_α = False

if cos_α.find("/") > 0:
    cos_αl()
else :
    cos_α = False

if tan_α.find("/") > 0:
    tan_αl()
else :
    tan_α = False

if cot_α.find("/") > 0:
    cot_αl()
else :
    cot_α = False

if sec_α.find("/") > 0:
    sec_αl()
else :
    sec_α = False

if csc_α.find("/") > 0:
    csc_αl()
else :
    csc_α = False
