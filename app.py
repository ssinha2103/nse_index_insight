from flask import Flask, jsonify, render_template
import pandas as pd

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, Flask!"


ls = ['Nifty 50 Index',
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


@app.route('/nifty50')
def trial():
    df = pd.read_csv('https://www1.nseindia.com/content/indices/ind_nifty50list.csv')
    print(df.to_string())
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
    print(company_data)
    return render_template('index.html', company_datas=company_data)


if __name__ == '__main__':
    app.run()
