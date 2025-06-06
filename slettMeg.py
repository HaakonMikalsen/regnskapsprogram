def konverter_tid(unixtid):
    startÅr = 1970
    
    heleMinutter = unixtid//60
    heleTimer = heleMinutter//60
    heleDøgn = heleTimer//24  
    heleMåneder =heleDøgn//30
    heleÅr = heleMåneder//12
    
    år = startÅr+heleÅr
    månede = heleMåneder-heleÅr*12
    dag = heleDøgn-heleMåneder*30 +1
    timer = heleTimer-heleDøgn*24
    minutter = heleMinutter-heleTimer*60
    sekundder = unixtid-heleMinutter*60
    
    return [år,månede,dag,timer,minutter,sekundder]

print(konverter_tid(3600))
