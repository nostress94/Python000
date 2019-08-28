din_br = float (input('Quantos reais você tem na carteira? R$ '))
din_us = din_br / 4.15
din_eu = din_br / 4.33
din_lib = din_br / 4.81
print ('Com R$ {:.2f} você pode comprar {:.2f} doláres, {:.2f} euros ou {:.2f} libras.'.format (din_br,din_us,din_eu,din_lib))