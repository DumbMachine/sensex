# SENSEX
A python package to scrap data from Money Control site. This can be used to scrape data for BSE/NSe stocks. 
Use at your own risk, I don't think they would allow people to scrap data of their site like this.
## Installation:
```python
git clone THISHIT
cd THISHIT
pip install -r requirements.txt
python setup.py install
```
from MultiStock import MultiStock
something = MultiStock("RAITN",['https://www.moneycontrol.com/india/stockpricequote/steellarge/jindalhisar/JSH','https://www.moneycontrol.com/india/stockpricequote/steellarge/jswsteel/JSW01','https://www.moneycontrol.com/india/stockpricequote/steellarge/manaksiasteels/MS27','https://www.moneycontrol.com/india/stockpricequote/steellarge/sail/SAI','https://www.moneycontrol.com/india/stockpricequote/steellarge/steelexchange/SEI02','https://www.moneycontrol.com/india/stockpricequote/steellarge/tatasteel/TIS'],threads=5,full_day = True)
something.bulk_get_data()# sensex
