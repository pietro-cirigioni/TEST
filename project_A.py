from fredapi import Fred

fred = Fred(api_key = '21771c757702bbde46738ce0fa9f9c1f')
ten_year_treasuries = fred.get_series_latest_release('GS10') / 100

print(ten_year_treasuries.iloc[-1])