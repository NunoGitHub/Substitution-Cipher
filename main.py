
import string
def SubstitutionCipher():
    alphabet = dict.fromkeys(string.ascii_uppercase, 0)
    nWords = 0
    cipherText = "HG UOVI UJJXUTV VI GI BX, NRG H UB CIG USUTX GQUG UCA MIBBRCHGA QUV U THKQG GI ZITMX UCIGQXT GI NX MHFHOHVXL. VI OICK UV GQX VRZZXTXTV NA GQX NUL OUS LI CIG HCFIPX UVVHVGUCMX ZTIB IGQXT MIBBRCHGHXV, H MUCCIG ULBHG GQUG JXTVICV XCGHTXOA RCMICCXMGXL SHGQ GQXB IRKQG GI VGXJ HC UCL TXYRHTX GQUG U MICLHGHIC IZ GQHCKV SHGQ SQHMQ UOO SQI UTX LHTXMGOA HCGXTXVGXL UJJXUT GI NX VUGHVZHXL, VQIROL NX JRG UC XCL GI NXMURVX HG HV U VMUCLUO GI JXTVICV VIBX GQIRVUCLV IZ BHOXV LHVGUCG, SQI QUFX CI JUTG IT MICMXTC HC HG. OXG GQXB VXCL BHVVHICUTHXV, HZ GQXA JOXUVX, GI JTXUMQ UKUHCVG HG; UCL OXG GQXB, NA UCA ZUHT BXUCV (IZ SQHMQ VHOXCMHCK GQX GXUMQXTV HV CIG ICX), IJJIVX GQX JTIKTXVV IZ VHBHOUT LIMGTHCXV UBICK GQXHT ISC JXIJOX. HZ MHFHOHVUGHIC QUV KIG GQX NXGGXT IZ NUTNUTHVB SQXC NUTNUTHVB QUL GQX SITOL GI HGVXOZ, HG HV GII BRMQ GI JTIZXVV GI NX UZTUHL OXVG NUTNUTHVB, UZGXT QUFHCK NXXC ZUHTOA KIG RCLXT, VQIROL TXFHFX UCL MICYRXT MHFHOHVUGHIC. U MHFHOHVUGHIC GQUG MUC GQRV VRMMRBN GI HGV FUCYRHVQXL XCXBA, BRVG ZHTVG QUFX NXMIBX VI LXKXCXTUGX, GQUG CXHGQXT HGV UJJIHCGXL JTHXVGV UCL GXUMQXTV, CIT UCANILA XOVX, QUV GQX MUJUMHGA, IT SHOO GUPX GQX GTIRNOX, GI VGUCL RJ ZIT HG. HZ GQHV NX VI, GQX VIICXT VRMQ U MHFHOHVUGHIC TXMXHFXV CIGHMX GI YRHG, GQX NXGGXT. HG MUC ICOA KI IC ZTIB NUL GI SITVX, RCGHO LXVGTIAXL UCL TXKXCXTUGXL (OHPX GQX SXVGXTC XBJHTX) NA XCXTKXGHM NUTNUTHUCV."
    #contar o numero de letras do cipher text
    for i in cipherText:
        if i in alphabet:
            alphabet[i] = alphabet[i] + 1
            nWords += 1

    bigrams=[]
    #for i, letter in cipherText
    #dividir as palavras numa lista
    for i in cipherText.split():
        if i.isalpha():
            bigrams.append(i)


    trigrams=bigrams.copy()
    i=0
    #criar remover todas as plavars com mais e menos de duas letras para criar bigramas
    while(len(bigrams)>i):
        if(len(bigrams[i]) >2  or len(bigrams[i]) <=1):
           bigrams.remove(bigrams[i])
           i=0
        i = i+1

    print(bigrams)

    auxBi = ""
    # to remove duplicated of bigrams
    # from list
    res = []
    for i in bigrams:
        if i not in res: #adiciona se não estiver na lista res
            res.append(i)

    print(res)
    #trasnformar os bigramas num dicionario
    cpyBi2 = dict.fromkeys(res,0)
    print(cpyBi2)

    #count number of bigrams
    nw=0
    for i in bigrams:
        if i in cpyBi2:
           cpyBi2[i] = cpyBi2[i] + 1
           nw += 1


    sortedCipherBig = sorted(cpyBi2.items(), key=lambda kv: kv[1])
    #print(sortedCipherBig)

    #trigrams
    #  remover todas as plavars com mais e menos de 3 letras para criar trigramas
    i=0
    while (len(trigrams) > i):
        if (len(trigrams[i]) > 3 or len(trigrams[i]) < 3):
            trigrams.remove(trigrams[i])
            i = 0
        else:
            i = i + 1

    print(trigrams)
    #remove duplicades
    removeDupli = []
    for i in trigrams:
        if i not in removeDupli:
            removeDupli.append(i)

    print(removeDupli)
    #convert to dict
    cpytr = dict.fromkeys(removeDupli,0)
    # count number of trigrams
    for i in trigrams:
        if i in cpytr:
            cpytr[i] = cpytr[i] + 1

    sortedCiphertri = sorted(cpytr.items(), key=lambda kv: kv[1])
    print(sortedCiphertri)


    key="YMNXJVTIOPGDCBLKHUWRASZEQF"
    index=0
    tenta=cipherText
    for indw, al in enumerate(cipherText):
        if(alphabet.__contains__(al)):
            tenta =  tenta[:indw] + key[(ord(al)-65)] + tenta[indw + 1:]


    print(tenta)



if __name__ == '__main__':
    SubstitutionCipher()

