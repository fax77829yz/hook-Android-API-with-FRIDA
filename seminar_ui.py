import tkinter as tk
import os

HEIGHT = 500
WIDTH = 600
TOP = 25

details =('Package\nName', 'IMEI', 'IMSI', 'Phone\nNumber', 'Sim\nOperator', 'Serial', 'Hardware',
  'Brand', 'Model', 'Tags', 'Battery', 'Wi-Fi')

init_values =('com.example.myapplication', '000000000000000',
  '000000000000000','123456789','T-Mobile',
  'unkonwn','vbox86','Android', 'Google Pixel 3',
  'test-keys','100', '7C-57-23-06-C4-11')

feature = ('$PACKAGENAME', '$IMEI', '$IMSI','$PHONENUMBER', '$SIMOPERATORNAME',
 '$SERIAL', '$HARDWARE', '$BRAND', '$MODEL', '$TAGS', '$BATTERY', '$WIFI')


def check_value(data, num) :
  """
  檢查修改的資料有沒有錯誤
  :param data: 輸入單個到entry object內的資料
  :param num: list中第幾個
  """
  s = data.get()
  if s is '' or not correct_syntax(s, num):
    err_var.set('data error')
    return False
  return True

def correct_syntax(s, num) :
  """
  檢查修改的資料有沒有格式上的錯誤
  :param s: 要檢查的字串
  :param num: list中第幾個
  """
  if num == 0: return True
  elif num == 1 and s.isdigit() and len(s) == 15: return True
  elif num == 2 and s.isdigit() and len(s) == 15: return True
  elif num == 3 and s.isdigit(): return True
  elif num == 4 or num == 5 or num == 6 or num == 7 or num == 8 or num == 9: return True
  elif num == 10 and s.isdigit(): return True
  elif num == 11 and '-' in s : 
    tmp = s.split('-')
    if len(tmp) is 6:
      for hex in tmp:
        if len(hex) is not 2 or not is_hex(hex) : return False
      return True

    return False
  else :return False

def is_hex(ch2) :
  """
  判斷是否為16進制
  :param ch2: 要檢查是否為16進制的字串
  """
  for i in range(len(ch2)) :
    if ('0' > ch2[i] or ch2[i] > '9') and ('A' > ch2[i] or ch2[i] > 'F') and \
      ('a' > ch2[i] or ch2[i] > 'f') :
      return False
  return True

def modified_value(data_list) :
  """
  檢查修改的資料有沒有格式錯誤
  :param data_list: 由所有輸入到entry object內的資料所組成的list
  """
  mod_values = []
  err_var.set('')
  sus_var.set('')
  i = 0
  while i in range(len(data_list)):
    if not check_value(data_list[i], i):
      return 

    mod_values.append(data_list[i].get())
    i+= 1
  
  alter('hookAPI_template.py', 'hookAPI.py', feature, mod_values, True)
  alter('hookAPI_template.js', 'hookAPI.js', feature, mod_values, False)
 # os.system("python hookAPI.py")    #執行py檔
  sus_var.set('executed')

def alter(template, new_file, old_str, mod_list, is_py):
    """
    將替換的字串寫到一個新的檔案中，然後將原檔案刪除，新檔案改為原來檔案的名字
    :param template: 檔案路徑
    :param new_file: 修改後的檔名
    :param old_str: 需要替換的字串
    :param new_str: 替換的字串
    :is_py: 判斷是不是要生成py檔
    """
    with open(template, "r", encoding="utf-8") as f1, \
      open(new_file, "w", encoding="utf-8") as f2:
        if is_py: index = 0
        else: index = 1
        for line in f1:           
            if any(s in line for s in old_str):
                line = line.replace(old_str[index], mod_list[index])
                index += 1
            f2.write(line)

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_label = tk.Label(root, bg= 'gray')
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root)
frame.place(relx=0.05, rely=0.05,relwidth=0.9, relheight=0.9)

i = j = num = 0
values = []
while num < len(details):
  lb = tk.Label(frame, text=details[num], justify = 'left')
  lb.place(x = j*275, y = TOP+i*45)
  values.append(tk.Entry(frame))
  values[num].insert(0, init_values[num])
  values[num].place(x = 70 + j*275, y = TOP+i*45)
  i += 1
  num += 1
  if i == 9:
    j += 1
    i = 0


err_var = tk.StringVar()
sus_var = tk.StringVar()
error_label = tk.Label(frame, textvariable=err_var, font=('Arial', 18), justify = 'left', fg = 'red')
error_label.place(relx=0.83, rely=0.85)
success_label = tk.Label(frame, textvariable=sus_var, font=('Arial', 18), justify = 'left', fg = 'green')
success_label.place(relx=0.82, rely=0.85)
button = tk.Button(frame, text="start", font=('Arial', 18), command=lambda: modified_value(values))
button.place(relx=0.9, rely=0.9, relheight = 0.1, relwidth = 0.1)

root.mainloop()