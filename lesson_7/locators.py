from typing import Tuple

# header
LOGO: tuple[str, str] = ('xpath', '(//a[contains(@class, "nav-link")])[1]')
EXPLORE_LIST_BUTTON: tuple[str, str] = ('xpath', '(//a[contains(@class, "nav-link")])[2]')
PRICING_BUTTON: tuple[str, str] = ('xpath', '(//a[contains(@class, "nav-link")])[3]')
FOR_BUSINESS_BUTTON: tuple[str, str] = ('xpath', '(//a[contains(@class, "nav-link")])[4]')
SIGN_IN_BUTTON: tuple[str, str] = ('xpath', '//button[contains(text(), " Sign in ")]')
START_FOR_FREE_BUTTON: tuple[str, str] = ('xpath', '//button[contains(text(), " Start for free ")]')
TITLE_TEXT: tuple[str, str] = ('xpath', '//h1')
SUBTITLE: tuple[str, str] = ('xpath', '//h2')
TEXT_UNDER_SUBTITLE: tuple[str, str] = ('xpath', '//p[@class="mb-4"]')
SECTIONS_LIST: tuple[str, str] = ('xpath', '//div[@data-component-name="TrackCategories"]')
COURSES_LIST: tuple[str, str] = ('xpath', 'class="row"')
