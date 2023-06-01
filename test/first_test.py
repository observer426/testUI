from datetime import time

import minium
from minium import Callback

class TestPage(minium.MiniTest):
    def test_get_system_info(self):
        sys_info = self.mini.get_system_info()
        self.assertIn("SDKVersion", sys_info)

    # http://124.71.99.48:8080/images/sustech_1.JPG
    def test_data(self):
        page = self.app.redirect_to("/pages/main/main")
        el = page.get_element("#view.news-item > .new-source > .new-title > .question-link").get_element("text")  # text_name
        print(el.text)
        self.assertDictEqual({
           "南方科技大学预约小程序上线"
        }, el.text, "data equal")
        el = page.get_element(".booking-text")
        print(el.text)
        self.assertEqual("个人预约参观", el.text, "data equal")

    def test_scroll_to(self):
        page = self.app.redirect_to("/pages/main/main")
        callback = Callback()
        # 监听滚动事件, 方便最后验证滚动结果
        self.app.hook_current_page_method("scroll", callback.callback)
        el = page.get_element("scroll-view")
        el.scroll_to(x=20)  # 横向滚动20像素
        self.assertTrue(callback.wait_called(timeout=10), "callback called")
        self.assertEqual(callback.get_callback_result()["detail"]["scrollLeft"], 20, "pick ok")

    def test_input(self):
        callback = Callback()
        page = self.app.navigate_to("/pages/user-page-detail/modify/modify")
        el = page.get_element("van-field[placeholder='请输入姓名']")
        self.app.hook_current_page_method("userNameInput", callback.callback)
        el.input("测试名")
        # time.sleep(3)
        self.assertTrue(callback.wait_called(timeout=10), "callback called")
        # 检验输入详情
        self.assertEqual(callback.get_callback_result()["detail"]["value"], "测试名", "input text ok")

