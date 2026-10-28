# Lab 05 — Thảo luận (PDF trang 64)

## Upstream first so với release first
Upstream first sửa trên master trước rồi backport: giúp sửa không bị quên trên dòng phát triển chính, nhưng bản sửa có thể phụ thuộc code mới và khó áp dụng cho release cũ. Release first sửa trên bản cũ bị lỗi trước: cô lập bản vá tối thiểu, dễ kiểm chứng với khách hàng dùng bản cũ, nhưng phải chủ động lan truyền sang master và mọi release bị ảnh hưởng. Bài này dùng release first, tách commit code/test khỏi version/changelog để cherry-pick -x đúng phần cần thiết.

## Phát hiện quên đưa fix vào release/lab05
Vòng kiểm tra hành vi ở Phần F chạy trên v1.0.1, v1.1.0 và master sẽ in 0 ở dòng chưa sửa thay vì 1. Trước khi tag, chạy cùng phép kiểm tra trên origin/release/lab05. Log --all --grep theo chuỗi cherry picked from commit FIX_SHA sẽ thiếu một trong hai bản sao, nhưng số lượng log không thay thế kiểm tra hành vi. Có thể đối chiếu thêm git cherry giữa hai dòng để biết patch tương đương.

## Truy vết
Giữ tag bất biến, không xóa/tạo lại release/lab05; đưa sửa qua PR vào nhánh đã tồn tại. Issue chỉ tự đóng khi PR chứa Fixes #N được merge vào default branch. Số Issue thực phải lấy từ GitHub, không chép #20 trong ví dụ PDF.
