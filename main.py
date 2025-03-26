from barby import barby
from beit_hayotzer import beit_hayotzer
from guestroom import guestroom
from guitar_loft import guitar_loft
from haezor import haezor
from hameretz2 import hameretz2
from ivri import ivri
from levontin import levontin
from ozenbar import ozenbar
from shablul import shablul
from tassa import tassa
from tmuna import tmuna
from zappa import zappa
from amama import amama
import pandas as pd

def scrape():
    barby_df = barby()
    beit_hayotzer_df = beit_hayotzer()
    guestroom_df = guestroom()
    guitar_loft_df = guitar_loft()
    haezor_df = haezor()
    hameretz_df = hameretz2()
    ivri_df = ivri()
    levontin_df = levontin()
    ozenbar_df = ozenbar()
    shablul_df = shablul()
    tassa_df = tassa()
    tmuna_df = tmuna()
    zappa_df = zappa()
    amama_df = amama()
    
    dfs = [barby_df, beit_hayotzer_df, guestroom_df, guitar_loft_df, 
           haezor_df, hameretz_df, ivri_df, levontin_df, 
           ozenbar_df, shablul_df, tassa_df, tmuna_df, zappa_df, amama_df]
    
    events = pd.concat(dfs, ignore_index=True)
    return events
    