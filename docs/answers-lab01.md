# Lab 01 – Discussion Answers

## 1. Vì sao sử dụng git mv?

Lệnh `git mv` được sử dụng để di chuyển hoặc đổi tên file đang được Git theo dõi.

Ưu điểm:
- Thực hiện di chuyển và cập nhật Staging Area trong một thao tác.
- Giúp tổ chức lại cấu trúc repository thuận tiện.
- Git có thể nhận diện file được đổi tên và theo dõi lịch sử thông qua `git log --follow`.

Trong Lab 01, sử dụng `git mv` để chuyển `dvd.py` và `cart.py` vào thư mục `aims/` mà không thay đổi chức năng chương trình.

## 2. release/lab01 có phải là baseline không?

Trong phạm vi bài thực hành, `release/lab01` được sử dụng làm baseline nộp bài, đại diện cho trạng thái mã nguồn đã được hoàn thành và thống nhất tại thời điểm tạo nhánh.

Nhánh này được tạo từ `master` sau khi các thay đổi được kiểm tra và merge thành công.

Tuy nhiên, nhánh Git vẫn có thể thay đổi. Để xác định một baseline bất biến và chính xác hơn, có thể sử dụng commit SHA hoặc Git tag.

## 3. Vì sao không commit trực tiếp lên master dù làm một mình?

Không commit trực tiếp lên `master` vì:

- Giữ nhánh chính ổn định.
- Tách biệt từng thay đổi theo mục đích.
- Có thể kiểm tra và review thông qua Pull Request.
- Dễ theo dõi lịch sử và hoàn tác khi có lỗi.
- Duy trì quy trình phát triển nhất quán khi chuyển sang làm việc nhóm.

Trong Lab 01, sử dụng nhánh `refactor/apply-release-flow` và Pull Request #1 để đưa các thay đổi vào `master`.