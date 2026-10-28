# Lab 02 — Trả lời thảo luận

## Vì sao đồng bộ master trước khi PR?
Để kiểm tra tính năng với thay đổi vừa tích hợp, phát hiện xung đột và lỗi tương tác trước khi nhập vào nhánh chung. Trong bài này nhánh search khởi đầu tại 38e42b3, merge origin/master sau cart-print, chạy lại demo và kiểm tra tìm kiếm rồi mới tạo PR #5.

## Khi nào không được rebase?
Không rebase master, release/* hoặc nhánh đã chia sẻ mà người khác dựa vào: rebase viết lại SHA và có thể làm lịch sử các bản clone phân kỳ. Nhánh riêng chưa push có thể rebase để học hoặc làm gọn lịch sử. Nhánh đã chia sẻ dùng merge; bài này không force-push.

## feature/* khác topic/* như thế nào?
feature/* chứa thay đổi hành vi sản phẩm (cart-print, search-by-title); topic/* chứa một chủ đề hỗ trợ như PR template, sơ đồ use-case hoặc đáp án. Đây là quy ước đặt tên, cả hai đều ngắn hạn và tích hợp qua PR.

## Bằng chứng và giới hạn
- PR #3: template, merge commit; PR #4: cart-print, merge commit; PR #5: search, squash; PR #6: use-case, rebase merge.
- master bắt buộc PR, áp dụng cho admin, không force-push/xóa; push thử đã bị GH006 chặn.
- Làm cá nhân: 0 approvals theo PDF trang 29. Không có partner review thật nên không tuyên bố đạt vòng Changes requested → Approved trang 35. Hai worktree mô phỏng Dev1/Dev2 dùng cùng tài khoản, không chứng minh đóng góp hai người.
