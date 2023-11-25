# -*- coding: utf-8 -*-

from __future__ import print_function
from evaluate import infer
from DB import Database
from edge import Edge
from HOG import HOG
depth = 5
d_type = 'd1'
query_idx = 0

if __name__ == '__main__':
    db = Database()
    method = Edge()
    samples = method.make_samples(db)
    # lấy ảnh đầu tiên (đã trích xuất đặc trưng và lưu lại để so sánh)
    query = samples[query_idx]
    _, result = infer(query, samples=samples, depth=depth, d_type=d_type)
    print(result)

    method = HOG()
    samples = method.make_samples(db)
    query = samples[query_idx]
    _, result = infer(query, samples=samples, depth=depth, d_type=d_type)
    print(result)
