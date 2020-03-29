"""
@author: wanghongliang
@file: RunTestCase.py
@time: 2020/3/29 15:11 
"""
import sys
import pytest
from config.conf import ROOT_DIR, HTML_NAME


def main():
    if ROOT_DIR not in sys.path:
        sys.path.append(ROOT_DIR)
    # 执行用例
    # args = ['--reruns', '1', '--html=' + './report/' + HTML_NAME, "--self-contained-html", "-s", "-v"]
    args = ['--html=' + './report/' + HTML_NAME, "--self-contained-html", "-s", "-v"]
    pytest.main(args)


if __name__ == '__main__':
    main()
