# Lab 03 — Thảo luận

## Merge base là gì?
Là tổ tiên chung tốt nhất của hai commit; Git dùng làm nền cho three-way merge. Hai nhánh sửa cùng dòng khác nhau từ cùng nền có thể tạo xung đột. Trong bài, hai nhánh sửa thông báo add_dvd; merge master vào show-added-title đã tạo conflict thật và được giải quyết bằng thông báo tiếng Việt chứa title.

## Vì sao master/release phải dùng revert?
Revert tạo commit đảo ngược, giữ nguyên các commit đã chia sẻ và bằng chứng PR/tag. Reset/rebase dời con trỏ hoặc viết lại SHA nên không dùng trên lịch sử chung. Revert merge dùng -m 1 để chọn parent master làm dòng chính.

## Bằng chứng
Issue #8 đóng qua PR #9; test d25a55a FAIL trước fix fce5344 PASS. PR bugfix discount có base feature/discount. Master có 4 tests. Reset soft/mixed/hard và reflog chỉ trên topic/undo-practice chưa push; rebase chỉ trên topic/private-rebase-demo chưa push. Nhánh chung chỉ dùng merge/revert qua PR. Hai worktree cùng danh tính không phải bằng chứng hai thành viên.
