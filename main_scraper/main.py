from scrapers import amama, barby, beit_hayotzer, guestroom, guitar_loft, haezor, hameretz2, ivri, levontin, ozenbar, shablul, tassa, tmuna
import pandas as pd
import time

def scrape():
    start = time.time()
    amama_df = amama.amama()
    print(f"amama() took {time.time() - start:.2f} seconds")

    start = time.time()
    barby_df = barby.barby()
    print(f"barby() took {time.time() - start:.2f} seconds")

    start = time.time()
    beit_hayotzer_df = beit_hayotzer.beit_hayotzer()
    print(f"beit_hayotzer() took {time.time() - start:.2f} seconds")

    start = time.time()
    guestroom_df = guestroom.guestroom()
    print(f"guestroom() took {time.time() - start:.2f} seconds")

    start = time.time()
    guitar_loft_df = guitar_loft.guitar_loft()
    print(f"guitar_loft() took {time.time() - start:.2f} seconds")

    start = time.time()
    haezor_df = haezor.haezor()
    print(f"haezor() took {time.time() - start:.2f} seconds")

    start = time.time()
    hameretz_df = hameretz2.hameretz2()
    print(f"hameretz2() took {time.time() - start:.2f} seconds")

    start = time.time()
    ivri_df = ivri.ivri()
    print(f"ivri() took {time.time() - start:.2f} seconds")

    start = time.time()
    levontin_df = levontin.levontin()
    print(f"levontin() took {time.time() - start:.2f} seconds")

    start = time.time()
    ozenbar_df = ozenbar.ozenbar()
    print(f"ozenbar() took {time.time() - start:.2f} seconds")

    start = time.time()
    shablul_df = shablul.shablul()
    print(f"shablul() took {time.time() - start:.2f} seconds")

    start = time.time()
    tassa_df = tassa.tassa()
    print(f"tassa() took {time.time() - start:.2f} seconds")

    start = time.time()
    tmuna_df = tmuna.tmuna()
    print(f"tmuna() took {time.time() - start:.2f} seconds")
    
    dfs = [amama_df, barby_df, beit_hayotzer_df, guestroom_df, guitar_loft_df, 
           haezor_df, hameretz_df, ivri_df, levontin_df, 
           ozenbar_df, shablul_df, tassa_df, tmuna_df]
    
    events = pd.concat(dfs, ignore_index=True)
    return events