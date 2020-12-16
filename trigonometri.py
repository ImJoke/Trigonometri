import math

# depan_α = "2"
# miring_α = ""
# samping_α = "3"



def pencariSatu():

#################################################
                                                #
    depan_α = input("\nNilai depan α = ")       #
    if depan_α.isdigit():                       #
        depan_α = int(depan_α)                  #
    else :                                      #
        depan_α = False                         #
                                                #
    miring_α = input("Nilai miring α = ")       #
    if miring_α.isdigit():                      #
        miring_α = int(miring_α)                #
    else :                                      #
        miring_α = False                        #
                                                #
    samping_α = input("Nilai samping α = ")     #
    if samping_α.isdigit():                     #
        samping_α = int(samping_α)              #
    else :                                      #
        samping_α = False                       #
                                                #
#################################################

    if depan_α == False:
        depan_α = (math.sqrt(miring_α**2-samping_α**2))
        print ("\nNilai depan α =", depan_α)
    if miring_α == False:
        miring_α = (math.sqrt(depan_α**2+samping_α**2))
        print ("\nNilai miring α =", miring_α)
    if samping_α == False:
        samping_α = (math.sqrt(miring_α**2-depan_α**2))
        print ("\nNilai samping α =",samping_α)# global sin_α,cos_α,tan_α,cot_α,sec_α,csc_α
    sin_α = depan_α/miring_α
    cos_α = samping_α/miring_α
    tan_α = depan_α/samping_α
    cot_α = samping_α/depan_α
    sec_α = miring_α/samping_α
    csc_α = miring_α/depan_α
    print ("\nsin α =",sin_α, "\ncos α =",cos_α, "\ntan α =",tan_α, "\ncot α =",cot_α, "\nsec α =",sec_α, "\ncsc α =",csc_α, end="\n\n")# depan_α=3 # miring_α=5 # samping_α=4
# def pencari_sctcscDariSisi():
print ("\n\nPencari sin, cos, tan, cot, sec, dan csc dari panjang sisi\n\nMinimal pengguna harus dapat mengatahui nilai samping, miring, dan depan",end="\n\n")

def pencariDua():
    sin_α = input("Masukkan nilai sin α = ")
    def sin_αl():
        depan_α, samping_α = sin_α.split("/")
        depan_α=int(depan_α)
        samping_α=int(samping_α)
        return samping_α, depan_α, sin_α
    if sin_α.find("/") > 0:
        sin_αl()
    else :
        pencariSatu()
        sin_α = False

    cos_α = input("Masukkan nilai cos α = ")
    def cos_αl():
        miring_α, samping_α = cos_α.split("/")
        miring_α=int(miring_α)
        samping_α=int(samping_α)
        return samping_α, miring_α, cos_α
        pencariSatu()
    if cos_α.find("/") > 0:
        cos_αl()
    else :
        cos_α = False

    tan_α = input("Masukkan nilai tan α = ")
    def tan_αl():
        depan_α, miring_α = tan_α.split("/")
        depan_α=int(depan_α)
        miring_α=int(miring_α)
        return miring_α, depan_α, tan_α
        pencariSatu()
    if tan_α.find("/") > 0:
        tan_αl()
    else :
        tan_α = False

    cot_α = input("Masukkan nilai cot α = ")
    def cot_αl():
        miring_α, depan_α = cot_α.split("/")
        depan_α=int(depan_α)
        return miring_α, depan_α, cot_α
        pencariSatu()
    if cot_α.find("/") > 0:
        cot_αl()
    else :
        cot_α = False

    sec_α = input("Masukkan nilai sec α = ")
    def sec_αl():
        samping_α, miring_α = sec_α.split("/")
        samping_α=int(samping_α)
        miring_α=int(miring_α)
        miring_α=int(miring_α)
        return samping_α, miring_α, sec_α
        pencariSatu()
    if sec_α.find("/") > 0:
        sec_αl()
    else :
        sec_α = False

    csc_α = input("Masukkan nilai csc α = ")
    def csc_αl():
        samping_α, depan_α = csc_α.split("/")
        samping_α=int(samping_α)
        depan_α=int(depan_α)
        return samping_α, depan_α, csc_α
        pencariSatu()
    if csc_α.find("/") > 0:
        csc_αl()
    else :
        csc_α = False
    # depan_α = False
    # miring_α = False
    # samping_α = False
#######################################################################
# pencari_sctcscDariSisi()
# # sin_α = "5/13"
# # cos_α = ""
# # tan_α = ""
# # cot_α = ""
# # sec_α = ""
# # csc_α = ""

# #depan  =depan_α
# #miring =miring_α
# #smping =samping_α

# sin_α = input("Masukkan nilai sin α")
# cos_α = input("Masukkan nilai cos α")
# tan_α = input("Masukkan nilai tan α")
# cot_α = input("Masukkan nilai cot α")
# sec_α = input("Masukkan nilai sec α")
# csc_α = input("Masukkan nilai csc α")

# depan_α, samping_α = sin_α.split("/")
# miring_α, samping_α = cos_α.split("/")
# depan_α, miring_α = tan_α.split("/")
# miring_α, depan_α = cot_α.split("/")
# samping_α, miring_α = sec_α.split("/")
# samping_α, depan_α = csc_α.split("/")

# print (depan_α,samping_α)



### Caller ###

# pencariDua()
pencariSatu()

