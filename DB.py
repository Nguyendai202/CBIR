# -*- coding: utf-8 -*-

from __future__ import print_function# đảm bảo sự tương thích với các pb python
import pandas as pd
import os

DB_dir = 'database'
DB_csv = 'data_new.csv'

# ghi dữ liệu vào filecsv 
class Database(object):

  def __init__(self):
    self._gen_csv()
    self.data = pd.read_csv(DB_csv)
    self.classes = set(self.data["cls"])# set : chứa các dữ liệu duy nhất , ko lặp lại

  def _gen_csv(self):
    if os.path.exists(DB_csv):# néu đã tồn tại file csc thì thoát
      return
    with open(DB_csv, 'w', encoding='UTF-8') as f:
      f.write("img,cls")
      for root,floder, files in os.walk(DB_dir, topdown=False):# topdown: từ thư mục con lên cha , bỏ qua tệp tin 
        # root và floder trong th này giống nhau , đè nối từ thực mực cha đến con 
        cls = root.split('/')[-1]# loại bỏ đi tên file , còn đường dẫn cha đến con
        for name in files:
          if not name.endswith('.jpg'):
            continue
          img = os.path.join(root, name)
          f.write("\n{},{}".format(img, cls))

  def __len__(self):
    return len(self.data)

  def get_class(self):
    return self.classes

  def get_data(self):
    return self.data


if __name__ == "__main__":
  db = Database()
  data = db.get_data()
  classes = db.get_class()

  print("DB length:", len(db))
  # print(classes)
  print(db._gen_csv)
