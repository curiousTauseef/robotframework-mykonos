from mykonos.core.core import Core


class GlobalElement(Core):
    def __init__(self):
        self.device_mobile = self.device()
        self.get = GetConditions()

    def open_notification(self, **settings):
        """Open notification a device.

        This keywords is used to open notification of device

        **Example:**

        || Open notification      |

        """

        if 'device' in settings:
            device = settings['device']
            return device.open.notification()
        else:
            return self.device_mobile.open.notification()

    def open_quick_settings(self, **settings):
        """Open Quick Setting a device.

        This keywords is used to open setting of device

        **Example:**

        || Open Quick setting      |

        """
        if 'device' in settings:
            device = settings['device']
            return device.open.quick_settings()
        else:
            return self.device_mobile.open.quick_settings()

    def clear_text(self, *argument, **settings):
        """Clear text on the text field base on locator.

        This keywords is used to clear text field.

        **Example:**

        ||Clear Text        |  className=sample class
        """
        if 'locator' in settings:
            locator = settings['locator']
            return locator.clear_text()
        else:
            if 'device' in settings:
                device = settings['device']
                del settings['device']
                return device(*argument, **settings).clear_text()
            else:
                return self.device_mobile(*argument, **settings).clear_text()

    def input_text(self, *argument, **settings):
        """Input text on the text field base on locator.

        This keywords is used to input text into text field.

        **Example:**

        || Input Text        |  className=sample class    input=text

        """
        input = settings['input']
        del settings['input']

        if 'locator' in settings:
            locator = settings['locator']
            return locator.set_text(input)
        else:
            if 'device' in settings:
                device = settings['device']
                del settings['device']

                return device(*argument, **settings).set_text(input)
            else:
                return self.device_mobile(*argument, **settings).set_text(input)

    def count_elements(self, *argument, **settings):
        """Count total element from the page.

        This keywords is used to count total element on the device page.

        **Example:**

        || Count Elements          |  className=sample class

        **Return:**

        Total of elements (int)

        """
        if 'locator' in settings:
            locator = settings['locator']
            return locator.count
        elif 'watcher' in settings:
            watcher = settings['watcher']
            del settings['watcher']

            return watcher.count
        else:
            return self.device_mobile(*argument, **settings).count

    def turn_on_screen(self, **settings):
        """Turn on Screen Device.

        **Example:**

        ||  Turn On Screen

        **Return:**

         True or False
        """
        return self.device(**settings).screen.on()

    def turn_off_screen(self, **settings):
        """Turn off Screen Device.

        **Example:**

        ||  Turn Off Screen

        **Return:**

         True or False
        """
        return self.device(**settings).screen.off()

    def dump_xml(self, *args):
        """Dump hierarchy of ui and will be saved as hierarchy.xml.

        **Example:**

        ||  Dump Xml

        **Return:**

        xml file of device
        """
        return self.device().dump(*args)

    def capture_screen(self, file=None):
        """Capture screen of device testing.

        **Example:**

        ||  Capture Screen

        With file name:

        || Capture Screen        | file=sample

        **Return:**

        screen capture of device(*.png)
        """
        if file is not None:
            return self.device().screenshot(file+'.png')
        else:
            self.index += 1
            filename = 'mykonos-screenshot-%d.png' % self.index
            return self.device().screenshot(filename)


class Click(Core):

    def __init__(self):
        self.device_mobile = self.device()

    def click_element(self, *argument, **settings):
        """Click on UI base on locator.

        This keyword is used to click button or element of device.

        **Example:**

        ||  Click Element                    | className=sample class
        """
        if 'locator' in settings:
            locator = settings['locator']
            return locator.click()
        else:
            if 'device' in settings:
                device = settings['device']
                del settings['device']

                return device(*argument, **settings).click()
            elif 'watcher' in settings:
                watcher = settings['watcher']
                del settings['watcher']

                return watcher.click(*argument, **settings)
            else:
                return self.device_mobile(*argument, **settings).click()

    def long_click_element(self, *argument, **settings):
        """Long click on UI base on locator.

        This keyword is used to long click button or element of device.


        **Example:**

        ||  Long Click Element                 | className=sample class
        """
        if 'locator' in settings:
            locator = settings['locator']
            return locator.long_click()
        else:
            if 'device' in settings:
                device = settings['device']
                del settings['device']
                return device(*argument, **locator).long_click()
            else:
                return self.device_mobile(*argument, **settings).long_click()

    def click_a_point(self, *argument, **settings):
        """Click into pointer target location.

         This keyword is used to click location  based on pointer X and Y.

         **Example:**

         ||  CLick A Point      |x=10   |y=20

        """
        if 'x' in settings and 'y' in settings:
            x = settings['x']
            y = settings['y']
            del settings['x']
            del settings['y']
        else:
            raise ValueError('pointer x or y is refused')

        if 'device' in settings:
            device = settings['device']
            del settings['device']
            return device(*argument, **settings).click(x, y)
        else:
            return self.device_mobile().click(x, y)


class GetConditions(Core):
    def __init__(self):
        self.device_mobile = self.device()

    def get_text(self, *argument, **settings):
        """Get text from element base on locator.

        **Example:**

        ||  Get Text         |  className=sample class

        **Return:**
        String
        """
        if 'locator' in settings:
            locator = settings['locator']
            return locator.info['text']
        else:
            if 'device' in settings:
                device = settings['device']
                del settings['device']

                return device(*argument, **settings).info['text']
            else:
                return self.device_mobile(*argument, **settings).info['text']

    def get_element_attribute(self, *argument, **settings):
        """Get element attribute keyword of device.

        **List of Elements:**

         childCount, bounds, className, contentDescription,
         packageName, resourceName, text, visibleBounds,
         checkable, checked, clickable, enabled, focusable, disable,
         focused, longClickable, scrollable, selected

         **Example:**

         || Get Element Attribute         |  className=sample  element=text

         **Return:**

         Attribute from element device
        """
        element = settings['element']
        del settings['element']

        if 'locator' in settings:
            locator = settings['locator']
            return locator.info['element']
        else:
            if 'device' in settings:
                device = settings['device']
                del settings['device']

                return device(*argument, **settings).info[element]
            else:
                return self.device_mobile(*argument, **settings).info[element]

    def get_element(self, *argument, **settings):
        """Get element info of device .
        This keyword is used to get element info of device.

         **Example:**

        || Get Element    |

        **Return:**

        {'currentPackageName': 'com.google.android.apps.nexuslauncher',
         'displayHeight': 1794,
         'displayRotation': 0,
         'displaySizeDpX': 411,
         'displaySizeDpY': 731,
         'displayWidth': 1080,
         'productName': 'sdk_google_phone_x86',
         'screenOn': True,
         'sdkInt': 25,
         'naturalOrientation': True}
        """
        if 'device' in settings:
            device = settings['device']
            del settings['device']

            return device(*argument, **settings).info
        else:
            return self.device_mobile(*argument, **settings).info

    def get_element_by_coordinate_x(self, *argument, **settings):
        """Get element by coordinate X.
        This keyword is used to get coordinate X of device.

         **Example:**

        || Get Element By Coordinate X  |  className=sample class

        **Return:**

        Coordinate x(int)
        """
        bound = self.get_conditions.get_element_attribute(element='bounds', *argument, **settings)

        bottom = bound['bottom']
        top = bound['top']
        elm_x = (top+bottom)+top

        return elm_x

    def get_element_by_coordinate_y(self, *argument, **settings):
        """Get element by coordinate Y.

        This keyword is used to get coordinate Y of device.

         **Example:**

        || Get Element By Coordinate Y  |  className=sample class

        **Return:**

        Coordinate y(int)
        """
        bound = self.get_element_attribute(element='bounds', *argument, **settings)
        display_height = self.get_height()
        height = display_height
        left = bound['left']
        right = bound['right']
        elm_y = height-(right+left)
        return elm_y

    def get_width(self):
        """Get width from display of device.

        This keyword is used to get widh of device,

        **Example:**

        || Get Width

        **Return:**

        Width of device(int)
        """
        get_device = self.device()
        return get_device.info['displayWidth']

    def get_height(self):
        """Get height from display of device.

        This keyword is used to get widh of device.

        **Example:**

        || Get Height

        **Return:**

        Width of device(int)
        """
        get_device = self.device()
        return get_device.info['displayHeight']


class ExpectedConditions(Core):
    def __init__(self):
        self.device_mobile = self.device()
        self.get_conditions = GetConditions()

    def page_should_contain_element(self, *argument, **settings):
        """Page should contain element.
        The keyword is used to verify the page is contains locator element.

        **Example:**

        || Page Should Contain Element | className=sample class

        **Return:**

        True or False
        """
        element = self.get_conditions.get_element(*argument, **settings)

        if 'locator' in settings:
            locator = settings['locator']
            if locator[element].exists:
                return True
            else:
                raise ValueError('locator not found')
        else:
            if 'device' in settings:
                device = settings['device']
                del settings['device']
                return device(*argument, **settings).exists
            else:
                return self.device_mobile(*argument, **settings).exists

    def page_should_contain_text(self, *argument, **settings):
        """Page should contain text.
        The keyword is used to verify the page is contains text.

        **Example:**

        || Page Should Contain Text | text=sample text

        **Return:**

        True or False
        """
        text = settings['text']

        if 'device' in settings:
            device = settings['device']
            del settings['device']
            return device(*argument, **settings).exists
        else:
            return self.device_mobile(*argument, **settings).exists

    def __get_device_global(self, *argument, **settings):
        if 'locator' in settings:
            device = settings['locator']
        else:
            if 'device' in settings:
                device = settings['device']
                del settings['device']

                device = device(*argument, **settings)
            else:
                device = self.device_mobile(*argument, **settings)

        return device

    def page_should_not_contain_element(self, *argument, **settings):
        """Page should not contain element.

        The keyword is used to verify the page is not contains element.

        **Example:**

        || Page Should Not Contain Element | className=sample element

        **Return:**

        True or False
        """
        element = self.get_conditions.get_element(*argument, **settings)

        if 'locator' in settings:
            locator = settings['locator']
            found = locator[element].exists
            if found is False:
                return True
            else:
                return False
        else:
            if 'device' in settings:
                device = settings['device']
                del settings['device']
                found = self.__get_device_global(*argument, **settings).exists
                if found is True:
                    return False
                else:
                    raise True

    def page_should_not_contain_text(self, *argument, **settings):
        """Page should not contain text.

        The keyword is used to verify the page is not contains text.

        **Example:**

        || Page Should Contain Text | text=sample text

        **Return:**

        True or False

        """
        text = self.get_conditions.get_text(*argument, **settings)

        if 'locator' in settings:
            locator = settings['locator']
            found = locator[text].exists
            if found is False:
                return True
            else:
                return False
        else:
            if 'device' in settings:
                device = settings['device']
                del settings['device']
                return device(*argument, **settings).exists
            else:
                return self.device_mobile(*argument, **settings).exists

    def text_should_be_visible(self, *argument, **settings):
        """Text should be visible.

        The keyword is used to identify text visible.

        **Example:**

        || Text Should Be Visible | text=sample text

        **Return:**

        True or False
        """
        text = self.get_conditions.get_text(*argument, **settings)

        if 'locator' in settings:
            locator = settings['locator']
            if locator.info['visibleBounds'] is True:
                return True
            else:
                raise False
        else:
            if 'device' in settings:
                device = settings['device']
                del settings['device']
                return device(*argument, **settings).info['visibleBounds']
            else:
                return self.device_mobile(*argument, **settings).info['visibleBounds']

    def text_should_be_enabled(self, *argument, **settings):
        """Text should be enabled.

        The keyword is used to identify text enable.

        **Example:**

        || Element Should Be Enabled | text=sample text

        **Return:**

        True or False
        """
        element = self.get_conditions.get_element()
        enabled = element['enabled']
        if 'locator' in settings:
            locator = settings['locator']
            if locator.info['enabled'] is True:
                return True
            else:
                return False
        else:
            if 'device' in settings:
                device = settings['device']
                del settings['device']
                return device(*argument, **settings).enabled
            else:
                return self.device_mobile(*argument, **settings).enabled

    def text_should_be_disabled(self, *argument, **settings):
        """Text should be disabled.

        The keyword is used to identify text disabled.

        **Example:**

        || Element Should Be Disabled | text=sample text

        **Return:**

        True or False
        """
        element = self.get_conditions.get_element()
        enabled = element['enabled']
        if 'locator' in settings:
            locator = settings['locator']
            if locator.info['enabled'] is False:
                return True
            else:
                return False
        else:
            if 'device' in settings:
                device = settings['device']
                del settings['device']
                return device(*argument, **settings).enabled
            else:
                return self.device_mobile(*argument, **settings).enabled

    def element_should_contain_text(self, *argument, **settings):
        """Element should contain text.

        The keyword is used to identify text on element.

        **Example:**

        || Element Should Contain Text | className=class | text=sample text

        **Return:**

        True or False
        """
        if 'locator' in settings:
            locator = settings['locator']
            if locator.info['text'] is True:
                return True
            else:
                return False
        else:
            if 'device' in settings:
                device = settings['device']
                del settings['device']
                return self.device(*argument, **settings).info['text']
            else:
                return self.device_mobile(*argument, **settings).info['text']

    def element_should_not_contain_text(self, *argument, **settings):
        """Element should contain text.

        The keyword is used to identify text on element.

        **Example:**

        || Element Should Not Contain Text | className=class | text=sample text

        **Return:**

        True or False
        """
        if 'locator' in settings:
            locator = settings['locator']
            if locator.info['text'] is False:
                return True
            else:
                return False
        else:
            if 'device' in settings:
                device = settings['device']
                del settings['device']
                return self.device(*argument, **settings).info['text']
            else:
                return self.device_mobile(*argument, **settings).info['text']

    def check_element_visible(self, *argument, **settings):
        """Check element visible.

        The keyword is used to check element visible.

        **Example:**

        || Check Element Visible | className=sampleclassName

        **Return:**

        True or False
        """
        if 'locator' in settings:
            locator = settings['locator']
            if locator.info['visibleBounds'] is True:
                return True
            else:
                return False
        else:
            if 'device' in settings:
                device = settings['device']
                del settings['device']
                return self.device(*argument, **settings).info['visibleBounds']
            else:
                return self.device_mobile(*argument, **settings).info['visibleBounds']

    def check_element_non_visible(self, *argument, **settings):
        """Check element non visible.

        The keyword is used to check element non visible.

        **Example:**

        || Check Element Non Visible | className=sampleclassName

        **Return:**

        True or False
        """
        if 'locator' in settings:
            locator = settings['locator']
            if locator.info['visibleBounds'] is False:
                return True
            else:
                return False
        else:
            if 'device' in settings:
                device = settings['device']
                del settings['device']
                return self.device(*argument, **settings).info['visibleBounds']
            else:
                return self.device_mobile(*argument, **settings).info['visibleBounds']
