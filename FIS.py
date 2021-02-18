# %%
!pip install --upgrade gspread
# %%
from google.colab import auth
auth.authenticate_user()

import gspread
from oauth2client.client import GoogleCredentials

gc = gspread.authorize(GoogleCredentials.get_application_default())

#sh = gc.create('A new spreadsheet')

# Open our new sheet and add some data.
worksheet = gc.open('FIS').sheet1
rows = worksheet.get_all_values()
print(rows)

# %%
from nltk.chat.util import Chat, reflections

# %%
def func():
  deliveryID=input()
  status=""
  cell=worksheet.find(deliveryID)
  #print(cell)
  if cell:
    s=(cell.row,cell.col)
    s1=list(s)
    #print(s1) 
    status=status+worksheet.cell(s1[0],2).value
    #print(status)
    return status
    #print(status)
  else:
    status=status+'Please enter a valid Delivery ID'
    return status
    #print(status)

# %%