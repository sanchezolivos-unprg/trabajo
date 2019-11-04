#19 arma de guerra:
cadena: arma
real: calibre, peso, longitud, cadencia_de_tiro
entero: cantidad_balas
booleano: es_inofensivo

arma= "ak_47"
calibre= 7.62
peso= 4.3
cantidad_balas= 600
es_inofensivo= False
longitud= (peso+calibre)/5
cadencia_de_tiro= (cantidad_balas*calibre)/60+(peso)