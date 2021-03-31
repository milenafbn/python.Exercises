print('conversão metro para cm e mm')
m = float(input('digite uma medida em metro: '))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000
print(' Para kilômetro: {}km\n Para hectômetro: {}hm\n Para Decâmetro: {}dam'.format(km, hm, dam))
print(' Para decímetro: {}dm\n Para centímetro: {}cm\n Para milímetro: {}mm'.format(dm, cm, mm))
