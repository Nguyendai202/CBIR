from fastapi import FastAPI, UploadFile, File
from evaluate import infer
from DB import Database
from edge import Edge
from HOG import HOG
import os 
import uvicorn
import imageio

app = FastAPI()

@app.post('/api')
async def process_image(image: UploadFile = File(...)):
    # Lưu hình ảnh vào thư mục tạm
    with open('temp_image.jpg', 'wb') as f:
        f.write(await image.read())

    # Tiến hành xử lý hình ảnh và trả về kết quả
    result = process_image_function('temp_image.jpg')

    # Xóa hình ảnh tạm sau khi xử lý
    os.remove('temp_image.jpg')

    # Trả về kết quả dưới dạng JSON
    return result

def process_image_function(image_path):
    db = Database()
    method = Edge()
    input = imageio.imread(image_path)
    query = method.histogram(input, stride=(2, 2), type='region', n_slice=10, normalize=True)
    samples = method.make_samples(db)
    # query = samples[0]
    result = infer(query, samples=samples, depth=depth, d_type=d_type)
    edge_result = result

    method = HOG()
    samples = method.make_samples(db)
    query2 = method.histogram(input, 10, type='region', n_slice=6, normalize=True)
    result = infer(query2, samples=samples, depth=depth, d_type=d_type)
    hog_result = result

    # Kết hợp kết quả từ cả hai phương pháp (edge và HOG) thành một đối tượng kết quả
    combined_result = {
        'edge_result': edge_result,
        'hog_result': hog_result
    }

    return combined_result

if __name__ == '__main__':
    depth = 2
    d_type = 'd1'
    uvicorn.run(app, host='127.0.0.1', port=8000)