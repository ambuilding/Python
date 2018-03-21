"""
Modify the following google_sector_report so that it returns a json
dump that contains the following information about each sector:
1. The sector name
2. The percentage change in sector value
3. The biggest gainer and the percentage change in the biggest gainer
4. The biggest loser and the percentage change in the biggest loser

The structure of the json is given in the assignment description on EdX.

Note:
To read files, use:

with open('filename') as f:
    lines = f.readlines()
"""
def get_sector_sum():
    from bs4 import BeautifulSoup
    
    with open("Google Finance.htm") as fp:
        soup = BeautifulSoup(fp, "lxml")
        
    sector = soup.find_all('div', id='secperf')
    trs = sector[0].find_all('tr')
    sum = {}
    
    for i in range(1,8,3):
        sector = trs[i].find('a').get_text()
        change = trs[i].find('span', class_="chr").get_text()[:-1]
        sum[sector] = float(change)
        
    return sum


def get_movers(file):
    movers = {}

    from bs4 import BeautifulSoup
    
    with open(file) as fp:
        soup = BeautifulSoup(fp, "lxml")

    try:
        topmovers = soup.find_all('table', class_='topmovers')
        trs = topmovers[0].find_all('tr')
        
        for tr in trs[1:6]:
            equity = tr.find('a').get_text()
            change = tr.find_all('span', class_="chg")[1].get_text()[1:][:-2]
            movers[equity] = float(change)

        for tr in trs[7:12]:
            equity = tr.find('a').get_text()
            change = tr.find_all('span', class_="chr")[1].get_text()[1:][:-2]
            movers[equity] = float(change)
            
        return movers
    except:
        return None


def get_biggest(sector):
    biggest_gainer = {}
    biggest_loser = {}
    file = sector + ".htm"
    movers = get_movers(file)
    
    biggest_gainer["equity"] = max(movers, key=movers.get)
    biggest_gainer["change"] = max(list(movers.values()))

    biggest_gainer["equity"] = min(movers, key=movers.get)
    biggest_loser["change"] = min(list(movers.values()))

    return [biggest_gainer, biggest_loser]


def google_sector_report():
    import json

    results = {}
    result = {}
    Energy = {}
    BasicMaterials = {}
    Industrials = {}

    Energy["biggest_gainer"] = get_biggest("Energy")[0]
    Energy["biggest_loser"] = get_biggest("Energy")[1]
    Energy["change"] = get_sector_sum()["Energy"]
    
    BasicMaterials["biggest_gainer"] = get_biggest("Basic Materials")[0]
    BasicMaterials["biggest_loser"] = get_biggest("Basic Materials")[1]
    BasicMaterials["change"] = get_sector_sum()["Basic Materials"]
    
    Industrials["biggest_gainer"] = get_biggest("Industrials")[0]
    Industrials["biggest_loser"] = get_biggest("Industrials")[1]
    Industrials["change"] = get_sector_sum()["Industrials"]

    result["Energy"] = Energy
    result["Basic Materials"] = BasicMaterials
    result["Industrials"] = Industrials
    results["result"] = result

    return json.dumps(results)
