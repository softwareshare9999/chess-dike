#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate values/strings.xml (Vietnamese default) and values-zh-rCN/strings.xml."""

from pathlib import Path

# (name, vietnamese, chinese)
STRINGS = [
    # App / common
    ("app_name", "Tượng Kỳ Dick", "象棋迪克"),
    ("ok", "OK", "确定"),
    ("cancel", "Hủy", "取消"),
    ("confirm", "Xác nhận", "确认"),
    ("close", "Đóng", "关闭"),
    ("confirm_q", "Xác nhận?", "确认?"),
    ("i_know", "Đã hiểu", "我知道了"),
    ("language", "Ngôn ngữ", "语言"),
    ("language_vietnamese", "Tiếng Việt", "越南语"),
    ("language_chinese", "Tiếng Trung", "中文"),
    ("language_changed_restart", "Đã đổi ngôn ngữ. Khởi động lại màn hình để áp dụng.", "语言已切换，请重新打开界面以生效。"),

    # Main menu
    ("menu_play", "Đối trận", "对弈"),
    ("menu_link", "Liên kết", "连线"),
    ("menu_manual", "Phân tích kỳ phổ", "打谱"),
    ("menu_help", "Trợ giúp", "帮助"),
    ("menu_about", "Giới thiệu", "关于"),

    # Disclaimer / about
    ("disclaimer_title", "Tuyên bố miễn trừ", "免责声明"),
    ("disclaimer_agree", "Đồng ý và tiếp tục", "同意并继续"),
    ("disclaimer_disagree", "Không đồng ý và thoát", "不同意并退出"),
    ("disclaimer_body",
     "Phần mềm này (Tượng Kỳ Dick) là công cụ hỗ trợ học tập cờ tướng, chỉ dùng cho học tập cá nhân, ôn tập và giao lưu kỹ thuật. Vui lòng đọc kỹ các điều khoản sau trước khi sử dụng:\\n\\n"
     "1. Phần mềm chỉ nhận diện màn hình qua quyền ghi màn hình hệ thống và hiển thị gợi ý nước đi trên cửa sổ nổi; không có tự động đi quân, tiêm cảm ứng, dịch vụ trợ năng, Root/Xposed. Mọi nước đi do người chơi thao tác thủ công.\\n\\n"
     "2. Nghiêm cấm dùng phần mềm này cho bất kỳ giải đấu chính thức, ván có hệ số Elo, nền tảng cờ mạng hoặc cờ bạc nào vi phạm quy tắc nền tảng và pháp luật; mọi hậu quả do người dùng tự chịu.\\n\\n"
     "3. Chỉ dùng để học tập nghiên cứu; vui lòng tự xóa trong vòng 24 giờ sau khi nhận được.\\n\\n"
     "4. Phần mềm được cung cấp “nguyên trạng”, không bảo đảm tính sẵn sàng hay độ chính xác, và không chịu trách nhiệm với bất kỳ thiệt hại trực tiếp hay gián tiếp nào do việc sử dụng.\\n\\n"
     "Nhấn “Đồng ý và tiếp tục” nghĩa là bạn đã đọc, hiểu và đồng ý với toàn bộ các điều khoản trên.",
     "本软件（象棋迪克）为象棋学习辅助工具，仅供个人学习、复盘研究与技术交流使用。请在使用前仔细阅读以下条款：\\n\\n"
     "一、本软件仅通过系统录屏授权识别画面并以悬浮窗显示走法建议，不包含自动走子、触摸注入、无障碍服务、Root/Xposed 等功能，所有着法均由玩家手动操作。\\n\\n"
     "二、严禁将本软件用于任何正式比赛、等级分对局、网络对局平台或赌博等违反平台规则与法律法规的场景；由此产生的一切后果由使用者本人承担。\\n\\n"
     "三、本软件仅供学习研究，请于获取后 24 小时内自行删除。\\n\\n"
     "四、本软件按\\\"现状\\\"提供，不对软件的可用性与准确性作任何保证，不对因使用本软件造成的任何直接或间接损失承担责任。\\n\\n"
     "点击\\\"同意并继续\\\"即表示您已阅读、理解并同意以上全部条款。"),
    ("credits_body",
     "Ghi nhận:\\n"
     "· Dự án dựa trên mã nguồn mở “象棋鱼” (tác giả zfdang, GitHub: zfdang/chinese-chess-android);\\n"
     "· Trọng số nhận diện quân YOLO từ dự án Vincentzyx/VinXiangQi;\\n"
     "· Engine nhận diện ONNX hai bước (RTMPose góc + phân loại Swin) từ dự án Shirakawa-Kotone/chinese-chess-helper;\\n"
     "· Nền tảng engine và khung đối trận: đội Pikafish và DroidFish (Peter Österlund), giấy phép GPL-3.0.",
     "鸣谢：\\n"
     "· 本项目基于开源项目\\\"象棋鱼\\\"（作者 zfdang，GitHub: zfdang/chinese-chess-android）二次开发；\\n"
     "· YOLO 棋子检测权重文件来自 Vincentzyx/VinXiangQi 项目；\\n"
     "· ONNX 两步式识别引擎（RTMPose 角点 + Swin 分类）的模型与算法来自 Shirakawa-Kotone/chinese-chess-helper 项目；\\n"
     "· 引擎与对弈框架基座：Pikafish 团队与 DroidFish（Peter Österlund），GPL-3.0 开源授权。"),
    ("about_title", "Giới thiệu · Tượng Kỳ Dick", "关于 · 象棋迪克"),
    ("about_body",
     "Tượng Kỳ Dick XQDK v%1$s\\n\\n"
     "Tính năng nổi bật:\\n"
     "· Đối trận đầy đủ (engine Pikafish, độ sâu cố định / thời gian cố định / khai cuộc / Hash) và phân tích kỳ phổ;\\n"
     "· Liên kết AI: nhận diện màn hình YOLO không cần hiệu chỉnh, tự nhận hướng, gợi ý nước đi thời gian thực trên cửa sổ nổi, tra cứu khai cuộc, đa ứng viên và chế độ chỉnh tay khẩn cấp (chỉ nhận diện và gợi ý, không tự đi quân).\\n\\n",
     "象棋迪克 XQDK v%1$s\\n\\n"
     "特色功能：\\n"
     "· 完整对弈（Pikafish 引擎，固定深度/固定时间/开局库/盘面调节）与打谱；\\n"
     "· AI 连线识别：YOLO 免校准屏幕识别、自动朝向、悬浮窗实时走法建议、开局库速查、多候选与紧急手动模式（只识别提示，不自动走子）。\\n\\n"),

    # Settings dialog
    ("settings_title", "Cài đặt trò chơi", "游戏设置"),
    ("settings_engine", "Engine", "引擎"),
    ("engine_label_prefix", "Engine: %1$s", "引擎: %1$s"),
    ("settings_use_openbook", "Dùng thư viện khai cuộc", "使用开局库"),
    ("settings_current_openbook", "(Thư viện hiện tại)", "(当前开局库)"),
    ("settings_sound", "Phát âm thanh", "播放音效"),
    ("settings_red_first", "Đỏ đi trước (áp dụng ván mới)", "红方先行 (新建游戏有效)"),
    ("settings_random_move", "Tăng tính ngẫu nhiên nước đi máy", "增加电脑走棋的随机性"),
    ("settings_history_moves", "Hiển thị lịch sử nước đi", "显示历史着法"),
    ("settings_hash_size", "Kích thước Hash (MB)", "Hash大小(M)"),
    ("settings_search", "Cài đặt tìm kiếm:", "搜索设置："),
    ("settings_search_depth", "Tìm theo độ sâu cố định (gợi ý 20)", "搜索固定深度 (建议20)"),
    ("settings_depth_label", "Độ sâu:", "深度："),
    ("settings_search_time", "Tìm theo thời gian cố định (gợi ý 3000 ms)", "搜索固定时间 (建议3000毫秒)"),
    ("settings_time_label", "Thời gian:", "时间："),
    ("settings_search_infinite", "Tìm vô hạn, cần chớp nước", "无限搜索，须闪电出着"),

    # Game activity
    ("wait_red_move", "Chờ bên Đỏ đi", "等待红方走棋"),
    ("wait_black_move", "Chờ bên Đen đi", "等待黑方走棋"),
    ("new_game_title", "Bắt đầu ván mới?", "确定开始新游戏?"),
    ("new_game_message", "Bạn có muốn bỏ ván hiện tại và bắt đầu ván mới không?", "你是否要放弃当前的游戏，开始新游戏呢?"),
    ("new_game_start", "Bắt đầu ván mới", "开始新游戏"),
    ("new_game_continue", "Tiếp tục ván hiện tại", "继续当前游戏"),
    ("new_game_red_first", "Ván mới, Đỏ đi trước", "新游戏，红方先行"),
    ("new_game_black_first", "Ván mới, Đen đi trước", "新游戏，黑方先行"),
    ("fen_new_game_title", "Bắt đầu ván mới từ chuỗi FEN", "从FEN串开始新游戏"),
    ("fen_new_game_message", "Nhập chuỗi FEN của thế cờ:", "请输入棋局的FEN串："),
    ("switch_computer_black", "Chuyển máy cầm Đen", "切换为电脑执黑棋"),
    ("switch_human_black", "Chuyển người cầm Đen", "切换为人工执黑棋"),
    ("auto_play_on", "Bật tự động đi", "开启自动走棋"),
    ("auto_play_pause", "Tạm dừng tự động đi", "暂停自动走棋"),
    ("fen_copied", "Đã sao chép FEN vào clipboard", "FEN串已复制到剪贴板"),
    ("searching_hint_moves", "Đang tìm nước gợi ý...", "正在搜索建议着法..."),
    ("show_eval_trend", "Hiển thị biểu đồ đánh giá", "显示评估趋势图"),
    ("show_move_history", "Hiển thị lịch sử nước đi", "显示走法历史"),
    ("select_pv_n", "Chọn nước số %1$d", "选择着数%1$d"),
    ("trend_dataset_label", "Đánh giá thế trận bên Đỏ", "红方局势评估"),

    # Manual activity
    ("manual_empty_title", "Kỳ phổ trống", "空棋谱"),
    ("manual_not_loaded", "Chưa tải kỳ phổ", "未加载棋谱"),
    ("manual_init_title", "Đang khởi tạo", "初始化中"),
    ("manual_init_message", "Lần chạy đầu đang khởi tạo kỳ phổ, có thể mất hơn 30 giây, vui lòng chờ...", "初次运行，正在初始化棋谱，时间较长(>30s)，请耐心等待..."),
    ("manual_init_done", "Khởi tạo xong", "初始化完成"),
    ("manual_select_branch_n", "Chọn nhánh %1$d", "选择分支%1$d"),
    ("manual_no_file", "Bạn chưa chọn tệp nào", "您未选取任何文件"),
    ("manual_load_ok", "Tải kỳ phổ thành công", "棋谱加载成功"),
    ("manual_load_fail", "Tải kỳ phổ thất bại", "棋谱加载失败"),

    # Webview
    ("current_version_label", "Phiên bản hiện tại:", "当前版本:"),
    ("current_version_build", "Phiên bản hiện tại: %1$d\\nThời gian biên dịch: %2$s", "当前版本: %1$d\\n编译时间: %2$s"),
    ("prompt_title", "Cửa sổ gỡ lỗi engine Pikafish", "Pikafish 引擎调试窗口"),

    # Assist activity
    ("assist_title", "Tượng Kỳ Dick · Hướng dẫn nhận diện liên kết", "象棋迪克 · 连线识别指导"),
    ("assist_subtitle", "Nhận diện màn hình app cờ tướng khác và gợi ý nước đi trên cửa sổ nổi.\\nChỉ nhận diện và gợi ý, không tự động đi quân (không trợ năng, không tiêm chạm).", "识别其他象棋App的画面，在悬浮窗给出走法建议。\\n本功能只识别、只提示，不会自动走子（无无障碍服务、无点击注入）。"),
    ("assist_steps", "Các bước (nhận diện tự động):\\n① Cấp cửa sổ nổi → ② Thông báo → ③ Cấp quyền ghi màn hình và khởi động → ④ Chuyển sang app cờ bất kỳ — tự tìm bàn, tự nhận hướng, cửa sổ nổi gợi ý cho bên ta theo thời gian thực", "使用步骤（全自动识别）：\\n① 授予悬浮窗 → ② 通知 → ③ 授权录屏并启动 → ④ 切到任意象棋 App 对局界面即可——自动找棋盘、自动识别方向，悬浮窗实时给出我方建议"),
    ("assist_status_not_started", "Trạng thái: chưa khởi động", "状态：尚未启动"),
    ("assist_btn_overlay", "① Cấp quyền cửa sổ nổi", "① 授予悬浮窗权限"),
    ("assist_btn_overlay_ok", "① Quyền cửa sổ nổi: đã cấp ✓", "① 悬浮窗权限：已授权 ✓"),
    ("assist_btn_notify", "② Quyền thông báo (Android 13+)", "② 通知权限（Android 13+）"),
    ("assist_btn_notify_hint", "② Cho phép thông báo (dịch vụ foreground)", "② 允许通知（前台服务提示）"),
    ("assist_btn_notify_ok", "② Quyền thông báo: sẵn sàng ✓", "② 通知权限：已就绪 ✓"),
    ("assist_btn_capture", "③ Bắt đầu nhận diện màn hình (tự động tìm bàn)", "③ 开始屏幕识别（全自动识别棋盘）"),
    ("assist_btn_capture_running", "③ Đang nhận diện màn hình ✓", "③ 屏幕识别运行中 ✓"),
    ("assist_btn_theme", "④ Chủ đề cửa sổ nổi: %1$s", "④ 悬浮窗主题：%1$s"),
    ("assist_engine_onnx", "⑤ Engine nhận diện: ONNX góc (mặc định, tổng quát tốt)", "⑤ 识别引擎：ONNX 角点式（默认，泛化好）"),
    ("assist_engine_yolo", "⑤ Engine nhận diện: YOLO phát hiện (dự phòng)", "⑤ 识别引擎：YOLO 检测式（回退）"),
    ("assist_compliance", "Tuyên bố tuân thủ: chức năng chỉ nhận diện màn hình qua quyền ghi màn hình hệ thống và hiển thị gợi ý nước đi; là công cụ học tập, chỉ dùng nghiên cứu, vui lòng tự xóa trong 24 giờ. Không gồm tự đi quân, tiêm chạm, trợ năng, Root/Xposed hay đọc dữ liệu app khác; mọi nước đi do người chơi thao tác thủ công.", "合规声明：本功能仅通过系统录屏授权做画面识别并显示走法建议，属于象棋学习辅助工具，仅供学习研究，请于获取后24小时内自行删除。不包含自动走子、触摸注入、无障碍服务、Root/Xposed 或读取其他应用数据；对局中的所有着法均由玩家手动操作。"),
    ("assist_capture_ok", "Đã cấp quyền ghi màn hình, dịch vụ nhận diện đã chạy", "录屏授权成功，识别服务已启动"),
    ("assist_capture_denied", "Chưa cấp quyền ghi màn hình, không thể nhận diện", "未授予录屏权限，无法识别"),
    ("assist_status_need_capture", "Trạng thái: chưa chạy, hãy bấm ③ để cấp quyền ghi màn hình", "状态：未启动，请点击③授权录屏"),
    ("assist_status_running", "Trạng thái: %1$s", "状态：%1$s"),

    # Overlay theme labels
    ("theme_dark_glass", "Kính tối", "深色玻璃"),
    ("theme_black_oled", "Đen OLED", "纯黑 OLED"),
    ("theme_light_paper", "Giấy sáng", "浅色纸感"),

    # Overlay panel
    ("overlay_occluded", "Che bàn cờ, nên dời đi", "挡住棋盘，建议移开"),
    ("overlay_recognizing", "Đang nhận diện", "识别中"),
    ("overlay_change_move", "Đổi nước", "变招"),
    ("overlay_multipv_n", "%1$d nhánh", "%1$d变"),
    ("overlay_undo", "Hối kỳ", "悔棋"),
    ("overlay_manual", "Chỉnh tay", "手动"),
    ("overlay_depth", "Độ sâu", "深度"),
    ("overlay_hash", "Hash", "哈希"),
    ("overlay_engine", "Engine", "引擎"),
    ("overlay_chip_placeholder", "%1$s —", "%1$s —"),
    ("overlay_update", "Cập nhật", "更新"),
    ("overlay_stop", "Dừng", "停止"),
    ("overlay_resume", "Tiếp tục", "继续"),
    ("overlay_close", "Đóng", "关闭"),

    # ScreenAssistService / notifications
    ("notif_channel_name", "Liên kết · Nhận diện màn hình", "连线·屏幕识别"),
    ("notif_channel_desc", "Đang chạy nhận diện màn hình và hướng dẫn cửa sổ nổi", "屏幕识别与悬浮窗指导运行中"),
    ("notif_title", "Tượng Kỳ Dick · Đang nhận diện liên kết", "象棋迪克·连线识别运行中"),
    ("notif_text_default", "Chỉ nhận diện thế cờ và gợi ý nước đi, không tự đi quân", "仅识别局面并给出走法建议，不会自动走子"),
    ("strength_fast", "Nhanh · độ sâu 12", "快速·深度12"),
    ("strength_normal", "Chuẩn · độ sâu 20", "标准·深度20"),
    ("strength_strong", "Mạnh · độ sâu 24", "强劲·深度24"),

    ("status_engine_init_fail", "Khởi tạo engine nhận diện thất bại: hãy thử khởi động lại app (cài lại có thể sửa)", "识别引擎初始化失败：请尝试重启应用（重装可修复）"),
    ("status_recognizing_board", "Đang nhận diện bàn cờ…\\nHãy để bàn đầy đủ, không bị che", "正在识别棋盘…\\n请让棋盘完整无遮挡"),
    ("status_unstable", "Nhận diện không ổn định\\nHãy để bàn đầy đủ, không bị che\\nỔn định sẽ tự khôi phục", "识别不稳定\\n请让棋盘完整无遮挡\\n画面稳定后自动恢复"),
    ("status_onnx_fail_yolo", "Tải engine ONNX thất bại\\nĐã chuyển về YOLO", "ONNX 引擎加载失败\\n已回退 YOLO 识别"),
    ("status_engine_warming", "Đang làm nóng engine…", "引擎预热中…"),
    ("status_engine_thinking", "Engine đang nghĩ…", "引擎思考中…"),
    ("status_engine_error", "Lỗi engine: %1$s", "引擎异常：%1$s"),
    ("status_paused", "Đã dừng hướng dẫn\\nBấm 『Tiếp tục』 để khôi phục", "已停止指导\\n点『继续』恢复"),
    ("status_resumed", "Tiếp tục hướng dẫn", "继续指导"),
    ("status_closed", "Đã đóng (nhận diện và ghi màn hình đã dừng; mở lại từ trang Liên kết)", "已关闭（识别与录屏均已停止，可在连线页重新启动）"),
    ("status_board_updated_me", "Đã cập nhật thế cờ\\nHiện đến lượt ta đi", "棋局已更新\\n现轮到我方走"),
    ("status_board_updated_opp", "Đã cập nhật thế cờ\\nHiện đến lượt đối phương", "棋局已更新\\n现轮到对方走"),
    ("status_switch_engine_onnx", "Đổi engine nhận diện: ONNX góc\\nSẽ xác nhận lại bàn cờ", "切换识别引擎：ONNX 角点式\\n切换后重新确认棋盘"),
    ("status_switch_engine_yolo", "Đổi engine nhận diện: YOLO phát hiện\\nSẽ xác nhận lại bàn cờ", "切换识别引擎：YOLO 检测式\\n切换后重新确认棋盘"),
    ("status_no_undo", "Không còn thế cờ để hối (tự tích lũy theo ván)", "没有可悔的局面（会随对弈自动积累）"),
    ("status_undone", "Đã hối một nước\\nBấm 『Tiếp tục』 để khôi phục", "已悔棋一步\\n点『继续』恢复"),
    ("status_manual_on", "Chế độ chỉnh tay (bấm lại để thoát)\\nChạm quân → chạm ô đích = đi\\nChạm lại quân đã chọn = xóa\\n『Cập nhật』 sửa lượt đi", "手动模式（再点手动退出）\\n点子选中→点目标格=走子\\n再点选中子=删除\\n『更新棋局』纠正轮次"),
    ("status_manual_off", "Đã thoát chế độ chỉnh tay\\nKhôi phục nhận diện tự động", "已退出手动模式\\n恢复自动识别"),
    ("status_manual_king", "Chế độ chỉnh tay\\nKhông thể xóa Soái/Tướng", "手动模式\\n帅/将不可删除"),
    ("status_strength", "Cường độ engine: %1$s", "引擎强度：%1$s"),
    ("status_hash", "Engine Hash: %1$dMB", "引擎 Hash：%1$dMB"),
    ("status_multipv_one", "Đổi nước: 1 nhánh (tính toán đầy đủ nhất)", "变招：1 路（算力最全）"),
    ("status_multipv_n", "Đổi nước: %1$d nhánh (thêm %2$d dự phòng, chia tải)", "变招：%1$d 路（附%2$d个备选，算力摊薄）"),
    ("status_not_started", "Chưa khởi động", "未启动"),
    ("state_manual", "Chỉnh tay", "手动模式"),
    ("state_stopped", "Đã dừng", "已停止"),
    ("state_engine_error", "Lỗi engine", "引擎异常"),
    ("state_recognizing", "Đang nhận diện", "识别中"),
    ("state_warming", "Đang làm nóng engine", "引擎预热中"),
    ("headline_recognizing", "Đang nhận diện", "识别中"),
    ("headline_paused", "Đã dừng hướng dẫn", "已停止指导"),
    ("headline_my_turn", "Đến lượt ta đi", "轮到我方走"),
    ("headline_opp_turn", "Đến lượt đối phương", "轮到对方走"),
    ("candidate_book", "Khai cuộc %1$s ✓", "开局库 %1$s ✓"),
    ("candidate_book_alt", "Khai cuộc dự phòng %1$d %2$s ✓", "开局库备选%1$d %2$s ✓"),
    ("candidate_winrate", "Tỷ lệ thắng khoảng %1$d%%", "胜率约 %1$d%%"),
    ("candidate_turn_mismatch", "Có thể nhận nhầm lượt\\nTự sửa sau một nước", "轮次可能识别有误\\n走一步后自动纠正"),
    ("candidate_suggest", "Gợi ý %1$s", "建议 %1$s"),
    ("candidate_alt", "Dự phòng %1$d %2$s", "备选%1$d %2$s"),
    ("candidate_tentative", "（tạm）", "（暂定）"),
    ("candidate_depth_score", "%1$s sâu %2$d", "%1$s 深%2$d"),
    ("candidate_if_opp", "Nếu đối phương đi %1$s\\nTa nên %2$s", "若对方走%1$s\\n我方应%2$s"),
    ("red_advantage", "Đỏ hơn %1$s", "红方优势 %1$s"),
    ("red_disadvantage", "Đỏ kém %1$s", "红方劣势 %1$s"),

    # GameController
    ("err_invalid_fen", "Chuỗi FEN không hợp lệ", "无效的FEN串"),
    ("info_fen_start", "Bắt đầu từ FEN", "从FEN开局"),
    ("err_searching_wait", "Đang tìm kiếm, vui lòng chờ...", "搜索中，请稍候..."),
    ("err_no_undo", "Không còn nước để hối", "无棋可悔"),
    ("err_red_to_move_piece", "Đến lượt Đỏ đi quân", "该红方出子"),
    ("err_searching_or_flash", "Đang tìm kiếm, vui lòng chờ hoặc chớp nước", "搜索中，请稍候或闪电出着"),
    ("info_openbook_lookup", "Đang tra khai cuộc...", "检索开局库..."),
    ("info_infinite_search", "Đang tìm vô hạn, cần chớp nước!", "无限搜索着法中, 须闪电出着!"),
    ("info_searching_moves", "Đang tìm nước đi...", "搜索着法中..."),
    ("err_searching_alt", "Đang tìm nước đổi, chờ hoặc chớp nước", "搜索变着中,请稍候或闪电出着"),
    ("err_computer_moving", "Máy đang đi, chờ hoặc chớp nước", "电脑正在出着,请稍候或闪电出着"),
    ("err_red_cannot_alt", "Đến lượt Đỏ, không thể đổi nước", "该红方出着，无法变着"),
    ("err_alt_only_black", "Chỉ đổi nước khi Đen đang đi", "黑方出招时方可变着"),
    ("info_infinite_alt", "Đang tìm đổi nước vô hạn, cần chớp nước!", "无限搜索变着中, 须闪电出着!"),
    ("info_searching_alt", "Đang tìm đổi nước...", "搜索变着中..."),
    ("err_seeking_help", "Đang xin trợ giúp, chờ hoặc chớp nước", "正在寻求帮助，请稍候或闪电出着"),
    ("err_help_own_turn", "Chỉ xin trợ giúp khi đến lượt mình", "己方出招时方可寻求帮助"),
    ("info_infinite_help", "Đang xin trợ giúp vô hạn, cần chớp nước!", "无限寻求帮助中, 须闪电出着!"),
    ("info_seeking_help", "Đang xin trợ giúp...", "寻求帮助中..."),
    ("err_eval_when_idle", "Chỉ đánh giá khi đang chờ đi", "等待出着时方可评估局面"),
    ("select_piece", "Chọn quân", "选择棋子"),
    ("deselect_piece", "Bỏ chọn quân", "取消选择棋子"),
    ("err_not_moving_state", "Không ở trạng thái đi quân, vui lòng chờ...", "非走棋状态，请稍候..."),
    ("err_red_to_move", "Đến lượt Đỏ đi", "该红方出着"),
    ("err_black_to_move", "Đến lượt Đen đi", "该黑方出着"),
    ("err_illegal_move", "Nước đi bất hợp lệ", "非法走法"),
    ("flash_moving", "Đang chớp nước...", "闪电出着中..."),
    ("stop_help", "Dừng xin trợ giúp...", "停止寻求帮助..."),
    ("err_no_search_task", "Không có tác vụ tìm kiếm", "无搜索任务"),
    ("lose_no_move", "Hết nước đi", "无路可走"),
    ("multipv_choose", "Chọn số hoặc đi quân trực tiếp:", "选择编号或直接移动棋子："),
    ("checkmate", "Chiếu bí!", "将死！"),
    ("check", "Chiếu tướng!", "将军！"),
    ("predicted_moves", "Nước dự đoán: ", "预测着法："),

    # ManualController
    ("manual_not_open", "Chưa mở kỳ phổ...", "未打开棋谱..."),
    ("manual_bad_state", "Trạng thái bất thường", "状态异常"),
    ("manual_choose_branch", "Hãy chọn nhánh: ", "请选择分支: "),
    ("manual_no_next", "Không còn nước tiếp", "没有下一步了"),
    ("manual_at_start", "Đã về thế khai cuộc", "已经到达开局"),
    ("manual_back_one", "Quay lại một nước", "回到上一步"),
    ("manual_red_first", "Đỏ đi trước", "红方先行"),
    ("manual_black_first", "Đen đi trước", "黑方先行"),
    ("manual_back_start", "Về khai cuộc", "回到开局"),
    ("manual_branch_n", "Nhánh %1$d: %2$s", "分支%1$d: %2$s"),
    ("manual_bad_branch", "Nhánh sai: %1$d", "错误的分支: %1$d"),

    # Move notation (Vietnamese names; Chinese kept in zh dictionary)
    # Board piece glyphs stay Chinese via Piece.pieceNameMap — these are for move text only.
    ("move_unknown", "Nước không rõ", "未知动作"),
    ("move_action_flat", "bình", "平"),
    ("move_action_advance", "tiến", "进"),
    ("move_action_retreat", "thoái", "退"),
    ("move_prefix_front", "Trước", "前"),
    ("move_prefix_back", "Sau", "后"),
    ("move_prefix_mid", "Giữa", "中"),
    ("move_piece_w_king", "Soái", "帅"),
    ("move_piece_w_advisor", "Sĩ", "仕"),
    ("move_piece_w_elephant", "Tượng", "相"),
    ("move_piece_w_horse", "Mã", "马"),
    ("move_piece_w_chariot", "Xe", "车"),
    ("move_piece_w_cannon", "Pháo", "炮"),
    ("move_piece_w_pawn", "Binh", "兵"),
    ("move_piece_b_king", "Tướng", "将"),
    ("move_piece_b_advisor", "Sĩ", "士"),
    ("move_piece_b_elephant", "Tượng", "象"),
    ("move_piece_b_horse", "Mã", "马"),
    ("move_piece_b_chariot", "Xe", "车"),
    ("move_piece_b_cannon", "Pháo", "炮"),
    ("move_piece_b_pawn", "Tốt", "卒"),
    ("num_1", "1", "一"),
    ("num_2", "2", "二"),
    ("num_3", "3", "三"),
    ("num_4", "4", "四"),
    ("num_5", "5", "五"),
    ("num_6", "6", "六"),
    ("num_7", "7", "七"),
    ("num_8", "8", "八"),
    ("num_9", "9", "九"),

    # Engine strings already present
    ("engine_terminated", "Engine đã dừng", "引擎终止"),
    ("uci_protocol_error", "Lỗi giao thức UCI", "UCI协议错误"),
    ("failed_to_start_engine", "Không khởi động được engine", "无法启动引擎"),
    ("title_activity_play", "PlayActivity", "游戏活动"),
    ("dummy_button", "Nút giả", "虚拟按钮"),
    ("dummy_content", "NỘI DUNG\\nGIẢ", "虚拟\\n内容"),
]

ROOT = Path(__file__).resolve().parents[1]
VI_PATH = ROOT / "app/src/main/res/values/strings.xml"
ZH_PATH = ROOT / "app/src/main/res/values-zh-rCN/strings.xml"


def esc(s: str) -> str:
    return (s.replace("&", "&amp;")
             .replace("<", "&lt;")
             .replace(">", "&gt;")
             .replace("'", "\\'")
             .replace('"', '\\"'))


def write_xml(path: Path, lang_index: int, header_comment: str):
    lines = ['<?xml version="1.0" encoding="utf-8"?>',
             "<resources>",
             f"    <!-- {header_comment} -->"]
    for name, vi, zh in STRINGS:
        text = vi if lang_index == 0 else zh
        lines.append(f'    <string name="{name}">{esc(text)}</string>')
    lines.append("</resources>")
    lines.append("")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {path} ({len(STRINGS)} strings)")


if __name__ == "__main__":
    write_xml(VI_PATH, 0, "Default language: Vietnamese")
    write_xml(ZH_PATH, 1, "Chinese (zh-rCN) dictionary")
