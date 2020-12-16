def pencariDua():
    global sin_α
    sin_α = input("Masukkan nilai sin α = ")
    percabangan()

def sin_αl():
    global samping_α, depan_α, sin_α
    depan_α, samping_α = sin_α.split("/")
    depan_α=int(depan_α)
    samping_α=int(samping_α)

def percabangan():
    global sin_α
    if sin_α.find("/") > 0:
        sin_αl()
    else :
        # pencariSatu()
        sin_α = False

pencariDua()

print (sin_α)
print (depan_α)
print (samping_α)

print (type(sin_α))
print (type(depan_α))
print (type(samping_α))

