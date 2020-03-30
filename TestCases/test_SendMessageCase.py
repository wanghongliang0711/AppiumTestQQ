"""
@author: wanghongliang
@file: test_SendMessageCase.py
@time: 2020/3/29 15:45 
"""
import pytest


class TestSendMessage(object):
    test_data = [("test1", "test1"), ("test2", "test2"), ("test3", "test3")]

    @pytest.mark.parametrize('message, expect', test_data)
    def test_send_message(self, ini_pages, message, expect):
        messages_page = ini_pages[1]
        chat_page = ini_pages[2]
        messages_page.select_message_item()
        chat_page.input_chat_message(message)
        chat_page.click_send_button()
        actual = chat_page.last_message_text()
        chat_page.click_back_button()
        assert actual == expect, f"失败 actual:{actual}, expect:{expect}"
