# CBIR
The project uses HOG and HISTOGRAM features to perform image queries
Dưới đây là một ví dụ README hướng dẫn chạy API này:

# Hướng dẫn chạy API

API này cho phép xử lý hình ảnh và trả về kết quả bằng cách sử dụng hai phương pháp: Edge và HOG.

## Cài đặt

1. Cài đặt Python (phiên bản 3.7 trở lên).

2. Cài đặt các thư viện cần thiết bằng lệnh sau:

   ```bash
   pip install requirements.txt
   ```

## Chạy API

1. Clone repository từ GitHub:

   ```bash
   git clone https://github.com/CBIR.git
   ```

2. Di chuyển vào thư mục chứa mã nguồn:

   ```bash
   cd your-repo
   ```

3. Chạy API bằng lệnh sau:

   ```bash
   python api.py
   ```

4. API sẽ chạy trên `http://127.0.0.1:8000`.
   bạn gõ thêm /docs ở phía sau api >> `http://127.0.0.1:8000/docs`

   

## Sử dụng API

API này chỉ có một endpoint `/api` nhận một hình ảnh làm tham số đầu vào.

### Request

- Phương thức: POST
- Endpoint: `http://127.0.0.1:8000/api`
- Header: không yêu cầu
- Body:
  - Loại: form-data
  - Key: `image`
  - Value: hình ảnh cần xử lý

### Response

Loại: JSON

Dữ liệu trả về sẽ bao gồm kết quả từ cả hai phương pháp (edge và HOG).
