volume = "#bse_volume > strong"
price = "#Bse_Prc_tick > strong"
percentage = "#b_changetext > span > strong"
PREV_CLOSE = "#b_prevclose > strong"
OPEN_PRICE = "#b_open > strong"
url = "http://www.moneycontrol.com/stocks/cptmarket/compsearchnew.php?search_data=&cid=&mbsearch_str=&topsearch_type=1&search_str={}".format("+".join(query.split()))
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'}
