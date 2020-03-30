# -*- coding: utf-8 -*-
# @Time    : 2020/3/30 13:55
# @File    : MessagesPage.py
from Page.BasePage import BasePage
from config.ElementConfig import MessagesPageElements


class MessagesPage(BasePage):
    """消息页面"""

    def select_message_item(self):
        return self.click(*MessagesPageElements.message)

    def select_message_item_text(self):
        return self.get_element_text(*MessagesPageElements.message)
