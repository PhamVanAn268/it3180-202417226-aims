# Lab 04 — Thảo luận

## Vì sao release/* không merge nguyên nhánh vào master?
Release là baseline bảo trì, có thể mang version/changelog riêng. Trong flow bài này, sửa lỗi được lan truyền chọn lọc bằng cherry-pick -x; merge cả release có thể mang bump 1.0.1 vào master đang 1.1.0. Đây là chính sách bài thực hành, không phải quy luật cấm merge release trong mọi dự án.

## So sánh GitFlow
Bài này dùng master làm nhánh tích hợp và release/labXX làm baseline; feature/topic/bugfix vào master qua PR. GitFlow truyền thống có develop để tích hợp, master cho phát hành, release/hotfix thường được merge trở lại các dòng liên quan. Không đồng nhất hai quy trình.

## Vì sao 1.0.0 thay vì 0.4.0?
1.0.0 tuyên bố mốc hợp đồng chức năng đủ ổn định theo mục tiêu bài; không phải cứ Lab04 thì số minor=4. 0.y.z chỉ giai đoạn trước ổn định. Tag định danh commit bất biến; nhánh release có thể tiến khi nhận hotfix. Không di chuyển tag đã công bố.

## Kiểm toán
Chốt answers cùng PR chuẩn bị 1.0.0 trước tag. Sau đó sort chỉ phát triển trên master; không đưa vào release/lab04. Ngày changelog là ngày phiên làm việc Asia/Bangkok, không khẳng định giờ commit máy bằng ngày này.
