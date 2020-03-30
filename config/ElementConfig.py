# -*- coding: utf-8 -*-
# @Time    : 2020/3/30 15:28
# @File    : ElementConfig.py


class MessagesPageElements(object):
    """消息页面element"""
    message = ("id", "com.tencent.mobileqq:id/title")


class ChatPageElements(object):
    """聊天页面"""
    input_chat_message = ("id", "com.tencent.mobileqq:id/input")
    send_button = ("id", "com.tencent.mobileqq:id/fun_btn")
    back_button = ("id", "com.tencent.mobileqq:id/e89")
    message = ("id", "com.tencent.mobileqq:id/chat_item_content_layout")
