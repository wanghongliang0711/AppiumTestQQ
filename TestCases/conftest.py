# -*- coding: utf-8 -*-
# @Time    : 2020/3/30 15:44
# @File    : conftest.py
from Page.PageObject.MessagesPage import MessagesPage
from Page.PageObject.ChatPage import ChatPage
import pytest


@pytest.fixture(scope='class')
def ini_pages(driver):
    messages_page = MessagesPage(driver)
    chat_page = ChatPage(driver)
    print("********ini_pages(driver)********")
    yield driver, messages_page, chat_page
