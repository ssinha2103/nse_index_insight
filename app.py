from flask import Flask, jsonify, render_template
import pandas as pd
import requests
from io import StringIO

app = Flask(__name__)

broad_index_list = ['Nifty 50 Index',
                    'Nifty Next 50 Index',
                    'Nifty 100 Index',
                    'Nifty 200 Index',
                    'Nifty 500 Index',
                    'Nifty500 Multicap 50:25:25 Index',
                    'Nifty Midcap 150 Index',
                    'Nifty Midcap 50 Index',
                    'Nifty Midcap Select Index',
                    'Nifty Midcap 100 Index',
                    'Nifty Smallcap 250 Index',
                    'Nifty Smallcap 50 Index',
                    'Nifty Smallcap 100 Index',
                    'Nifty Microcap 250 Index',
                    'NIFTY LargeMidcap 250 Index',
                    'Nifty MidSmallcap 400 Index']

index_urls_endings = [
    'ind_nifty50list',
    'ind_niftynext50list',
    'ind_nifty100list',
    'ind_nifty200list',
    'ind_nifty500list',
    'ind_nifty500Multicap502525_list',
    'ind_niftymidcap150list',
    'ind_niftymidcap50list',
    'ind_niftymidcapselect_list',
    'ind_niftymidcap100list',
    'ind_niftysmallcap250list',
    'ind_niftysmallcap50list',
    'ind_niftysmallcap100list',
    'ind_niftymicrocap250_list',
    'ind_niftylargemidcap250list',
    'ind_niftymidsmallcap400list'
]

status = [
    'active',
    'active',
    'active',
    'active',
    'active',
    'active',
    'active',
    'waiting',
    'active',
    'active',
    'active',
    'active',
    'active',
    'active',
    'active',
    'waiting',
]


@app.route('/')
def home():
    index_data = []
    count = 0
    for i in range(len(broad_index_list)):
        count += 1
        index_info = {
            'count': count,
            'indexName': broad_index_list[i],
            'index_url_endings': index_urls_endings[i],
            'status': status[i]
        }
        index_data.append(index_info)
    return render_template('index.html', index_datas=index_data)


@app.route('/index/<end>')
def index(end):
    # site = "https://www1.nseindia.com/content/indices/ind_nifty50list.csv"
    site = 'https://www1.nseindia.com/content/indices/' + end + '.csv'
    hdr = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive'}
    req = requests.get(site, headers=hdr)
    data = StringIO(req.text)
    df = pd.read_csv(data)
    company_name = []
    [company_name.append(i) for i in df['Company Name']]
    industry_name = []
    [industry_name.append(i) for i in df['Industry']]
    symbol_name = []
    [symbol_name.append(i) for i in df['Symbol']]
    isin_code = []
    [isin_code.append(i) for i in df['ISIN Code']]
    company_data = []
    count = 0
    for i in range(len(company_name)):
        count += 1
        company_info = {
            'count': count,
            'company_name': company_name[i],
            'industry_name': industry_name[i],
            'symbol_name': symbol_name[i],
            'isin_code': isin_code[i],
        }
        company_data.append(company_info)
    return render_template('index2.html', company_datas=company_data, end=end)


if __name__ == '__main__':
    app.run()
