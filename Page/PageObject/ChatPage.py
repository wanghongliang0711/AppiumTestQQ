# -*- coding: utf-8 -*-
# @Time    : 2020/3/30 16:00
# @File    : ChatPage.py
from Page.BasePage import BasePage
from config.ElementConfig import ChatPageElements


class ChatPage(BasePage):
    """聊天页面"""

    def input_chat_message(self, message):
        self.clear_chat_message()
        return self.send_keys(*ChatPageElements.input_chat_message, message)

    def clear_chat_message(self):
        return self.clear(*ChatPageElements.input_chat_message)

    def click_send_button(self):
        return self.click(*ChatPageElements.send_button)

    def click_back_button(self):
        return self.click(*ChatPageElements.back_button)

    def last_message_text(self):
        elements = self.find_elements(*ChatPageElements.message)
        return elements[-1].text
