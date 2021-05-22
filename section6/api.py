# google cloud platform
import gspread
from google.oauth2.service_account import Credentials
import os
from dotenv import load_dotenv
import pandas as pd
from gspread_dataframe import set_with_dataframe
from gspread_formatting import *

load_dotenv()

scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

credentials = Credentials.from_service_account_file(
    './section6/secret.json',
    scopes=scopes
)

gc = gspread.authorize(credentials)
# print(gc)


SP_SHEET_KEY = os.environ['SP_SHEET_KEY']
SP_SHEET = 'demo'

sh = gc.open_by_key(SP_SHEET_KEY)
# print(sh)
worksheet = sh.worksheet(SP_SHEET)
# print(worksheet)
data = worksheet.get_all_values()
# print(data)
df = pd.DataFrame(data[2:], columns=data[1])
df = df.drop(df.columns[[0]], axis=1)
# print(df)
# print(df.dtypes)
df = df.astype({'年齢': int, '社員ID': int})
# print(df.dtypes)
pvt_table = df.pivot_table(index=['所属'], values=['年齢'], aggfunc='mean')
# print(pvt_table)
pvt_table['年齢'] = pvt_table['年齢'].round()
# print(pvt_table)
new_worksheet = sh.add_worksheet(title='new', rows=100, cols=100)
# print(new_worksheet)
first_row = 2
first_col = 2
set_with_dataframe(new_worksheet, pvt_table.reset_index(),
                   row=first_row, col=first_col)

header_range = 'B2:C2'
index_range = 'B3:B8'
value_range = 'C3:C8'

header_fmt = cellFormat(
    backgroundColor=color(38/255, 166/255, 154/255),
    textFormat=textFormat(
        bold=True, foregroundColor=color(255/255, 255/255, 255/255)),
    horizontalAlignment='CENTER'
)

format_cell_range(new_worksheet, header_range, header_fmt)

border = Border('SOLID', Color(0, 0, 0, 0))
fmt = CellFormat(borders=Borders(
    top=border, bottom=border, left=border, right=border))
format_cell_range(new_worksheet, header_range, fmt)
format_cell_range(new_worksheet, index_range, fmt)
format_cell_range(new_worksheet, value_range, fmt)
