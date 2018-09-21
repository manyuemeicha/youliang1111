import pytest


def test_quit_browser(browser):
    '''关闭浏览器'''
    browser.quit()

if __name__ == "__main__":
    pytest.main()