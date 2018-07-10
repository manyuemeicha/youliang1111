import pytest

def test_quit_browser(browser):
    browser.quit()

if __name__=="__main__":
    pytest.main()