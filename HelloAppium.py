import unittest
import HtmlTestRunner
from appium import webdriver

# desired_caps = {}
# desired_caps['platformName'] = 'Android'
# desired_caps['platformVersion'] = '7.1.1'
# desired_caps['deviceName'] = 'Android Emulator'
# # desired_caps['appPackage'] = 'com.android.dialer'
# # desired_caps['appActivity'] = 'DialtactsActivity'
# desired_caps['appPackage'] = 'com.android.calculator2'
# desired_caps['appActivity'] = '.Calculator'

# 筆記本
# driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
# driver.find_element_by_id('com.android.dialer:id/search_box_collapsed').click()
# search_box = driver.find_element_by_id('com.android.dialer:id/search_view')
# search_box.click()
# search_box.send_keys('Hellow Appium')
# driver.find_element_by_id('stop searching').click()
# driver.find_element_by_id('Call History').click()

#計算機
# driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
# driver.find_element_by_id('com.android.calculator2:id/digit_0').click()

class TestCalculator(unittest.TestCase):
    def setUp(self):
        print('Setup')
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.1.1'
        desired_caps['deviceName'] = 'Android Emulator'
        desired_caps['appPackage'] = 'com.android.calculator2'
        desired_caps['appActivity'] = '.Calculator'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        print('Teardown')
        self.driver.quit()

    def button(self, btn):
        # sleep(5)
        return 'com.android.calculator2:id/'+str(btn)

    def check(self, value):
        # sleep(5)
        return 'com.android.calculator2:id/'+str(value)

    #test number 0
    def test_01(self):
        print('test01')
        self.driver.find_element_by_id('com.android.calculator2:id/digit_0').click()
        self.assertEqual('0', self.driver.find_element_by_id('com.android.calculator2:id/formula').text)

    #test number 1
    def test_02(self):
        self.driver.find_element_by_id('com.android.calculator2:id/digit_1').click()
        self.assertEqual('1', self.driver.find_element_by_id('com.android.calculator2:id/formula').text)

    #test number 2
    def test_03(self):
        self.driver.find_element_by_id('com.android.calculator2:id/digit_2').click()
        self.assertEqual('2', self.driver.find_element_by_id('com.android.calculator2:id/formula').text)

    #test number 3
    def test_04(self):
        self.driver.find_element_by_id('com.android.calculator2:id/digit_3').click()
        self.assertEqual('3', self.driver.find_element_by_id('com.android.calculator2:id/formula').text)

    #test number 4
    def test_05(self):
        self.driver.find_element_by_id('com.android.calculator2:id/digit_4').click()
        self.assertEqual('4', self.driver.find_element_by_id('com.android.calculator2:id/formula').text)

    #test number 5
    def test_06(self):
        self.driver.find_element_by_id('com.android.calculator2:id/digit_5').click()
        self.assertEqual('5', self.driver.find_element_by_id('com.android.calculator2:id/formula').text)

    #test number 6
    def test_07(self):
        self.driver.find_element_by_id('com.android.calculator2:id/digit_6').click()
        self.assertEqual('6', self.driver.find_element_by_id('com.android.calculator2:id/formula').text)

    #test number 7
    def test_08(self):
        self.driver.find_element_by_id('com.android.calculator2:id/digit_7').click()
        self.assertEqual('7', self.driver.find_element_by_id('com.android.calculator2:id/formula').text)

    #test number 8
    def test_09(self):
        self.driver.find_element_by_id('com.android.calculator2:id/digit_8').click()
        self.assertEqual('8', self.driver.find_element_by_id('com.android.calculator2:id/formula').text)

    #test number 9
    def test_10(self):
        self.driver.find_element_by_id('com.android.calculator2:id/digit_9').click()
        self.assertEqual('9', self.driver.find_element_by_id('com.android.calculator2:id/formula').text)

    #test dec_point
    def test_11(self):
        self.driver.find_element_by_id('com.android.calculator2:id/dec_point').click()
        self.assertEqual('.', self.driver.find_element_by_id('com.android.calculator2:id/formula').text)

    #test equal
    def test_12(self):
        self.driver.find_element_by_id('com.android.calculator2:id/digit_0').click()
        self.driver.find_element_by_id('com.android.calculator2:id/eq').click()
        self.assertEqual('0', self.driver.find_element_by_id('com.android.calculator2:id/result').text)

    #test result text
    def test_13(self):
        self.driver.find_element_by_id('com.android.calculator2:id/digit_3').click()
        self.driver.find_element_by_id('com.android.calculator2:id/op_mul').click()
        self.driver.find_element_by_id('com.android.calculator2:id/digit_3').click()
        self.assertEqual('3×3', self.driver.find_element_by_id('com.android.calculator2:id/formula').text)
        self.assertEqual('9', self.driver.find_element_by_id('com.android.calculator2:id/result').text)
        self.driver.find_element_by_id('com.android.calculator2:id/eq').click()
        self.assertEqual('9', self.driver.find_element_by_id('com.android.calculator2:id/result').text)
        self.driver.find_element_by_id('com.android.calculator2:id/op_mul').click()
        self.assertEqual('9×', self.driver.find_element_by_id('com.android.calculator2:id/formula').text)
        self.assertEqual('', self.driver.find_element_by_id('com.android.calculator2:id/result').text)
        self.driver.find_element_by_id('com.android.calculator2:id/eq').click()
        self.assertEqual('9', self.driver.find_element_by_id('com.android.calculator2:id/result').text)
        self.driver.find_element_by_id('com.android.calculator2:id/dec_point').click()
        self.driver.find_element_by_id('com.android.calculator2:id/eq').click()
        self.assertEqual('.', self.driver.find_element_by_id('com.android.calculator2:id/formula').text)
        self.assertEqual('Bad expression', self.driver.find_element_by_id('com.android.calculator2:id/result').text)

    #test delete
    def test_14(self):
        self.driver.find_element_by_id('com.android.calculator2:id/digit_3').click()
        self.driver.find_element_by_id('com.android.calculator2:id/digit_3').click()
        self.driver.find_element_by_id('com.android.calculator2:id/digit_4').click()
        self.driver.find_element_by_id('com.android.calculator2:id/digit_5').click()
        self.driver.find_element_by_id('com.android.calculator2:id/digit_6').click()
        self.driver.find_element_by_id('com.android.calculator2:id/digit_7').click()
        self.driver.find_element_by_id('com.android.calculator2:id/digit_8').click()
        self.assertEqual('3345678', self.driver.find_element_by_id('com.android.calculator2:id/formula').text)
        self.driver.find_element_by_id('com.android.calculator2:id/del').click()
        self.driver.find_element_by_id('com.android.calculator2:id/del').click()
        self.driver.find_element_by_id('com.android.calculator2:id/del').click()
        self.assertEqual('3345', self.driver.find_element_by_id('com.android.calculator2:id/formula').text)
        self.driver.find_element_by_id('com.android.calculator2:id/op_add').click()
        self.assertEqual('3345+', self.driver.find_element_by_id('com.android.calculator2:id/formula').text)
        self.driver.find_element_by_id('com.android.calculator2:id/del').click()
        self.assertEqual('3345', self.driver.find_element_by_id('com.android.calculator2:id/formula').text)

    #test add
    def test_15(self):
        self.driver.find_element_by_id('com.android.calculator2:id/op_add').click()
        self.assertEqual('', self.driver.find_element_by_id('com.android.calculator2:id/formula').text)
        self.driver.find_element_by_id('com.android.calculator2:id/digit_1').click()
        self.driver.find_element_by_id('com.android.calculator2:id/op_add').click()
        self.driver.find_element_by_id('com.android.calculator2:id/digit_2').click()
        self.assertEqual('1+2', self.driver.find_element_by_id('com.android.calculator2:id/formula').text)
        self.assertEqual('3', self.driver.find_element_by_id('com.android.calculator2:id/result').text)
        self.driver.find_element_by_id('com.android.calculator2:id/op_add').click()
        self.driver.find_element_by_id('com.android.calculator2:id/digit_3').click()
        self.assertEqual('1+2+3', self.driver.find_element_by_id('com.android.calculator2:id/formula').text)
        self.assertEqual('6', self.driver.find_element_by_id('com.android.calculator2:id/result').text)

    #test sub
    def test_16(self):
        self.driver.find_element_by_id('com.android.calculator2:id/op_sub').click()
        self.assertEqual('−', self.driver.find_element_by_id('com.android.calculator2:id/formula').text)
        self.driver.find_element_by_id('com.android.calculator2:id/digit_1').click()
        self.driver.find_element_by_id('com.android.calculator2:id/op_sub').click()
        self.driver.find_element_by_id('com.android.calculator2:id/digit_2').click()
        self.assertEqual('−1−2', self.driver.find_element_by_id('com.android.calculator2:id/formula').text)
        self.assertEqual('−3', self.driver.find_element_by_id('com.android.calculator2:id/result').text)
        self.driver.find_element_by_id('com.android.calculator2:id/op_add').click()
        self.driver.find_element_by_id('com.android.calculator2:id/digit_6').click()
        self.driver.find_element_by_id('com.android.calculator2:id/op_sub').click()
        self.driver.find_element_by_id('com.android.calculator2:id/digit_2').click()
        self.assertEqual('−1−2+6−2', self.driver.find_element_by_id('com.android.calculator2:id/formula').text)
        self.assertEqual('1', self.driver.find_element_by_id('com.android.calculator2:id/result').text)

    #test mul
    def test_17(self):
        self.driver.find_element_by_id('com.android.calculator2:id/op_mul').click()
        self.assertEqual('', self.driver.find_element_by_id('com.android.calculator2:id/formula').text)
        self.driver.find_element_by_id('com.android.calculator2:id/digit_1').click()
        self.driver.find_element_by_id('com.android.calculator2:id/op_mul').click()
        self.driver.find_element_by_id('com.android.calculator2:id/digit_2').click()
        self.assertEqual('1×2', self.driver.find_element_by_id('com.android.calculator2:id/formula').text)
        self.assertEqual('2', self.driver.find_element_by_id('com.android.calculator2:id/result').text)
        self.driver.find_element_by_id('com.android.calculator2:id/op_mul').click()
        self.driver.find_element_by_id('com.android.calculator2:id/digit_6').click()
        self.assertEqual('1×2×6', self.driver.find_element_by_id('com.android.calculator2:id/formula').text)
        self.assertEqual('12', self.driver.find_element_by_id('com.android.calculator2:id/result').text)

    #test div
    def test_18(self):
        self.driver.find_element_by_id('com.android.calculator2:id/op_div').click()
        self.assertEqual('', self.driver.find_element_by_id('com.android.calculator2:id/formula').text)
        self.driver.find_element_by_id('com.android.calculator2:id/digit_1').click()
        self.driver.find_element_by_id('com.android.calculator2:id/op_div').click()
        self.driver.find_element_by_id('com.android.calculator2:id/digit_2').click()
        self.assertEqual('1÷2', self.driver.find_element_by_id('com.android.calculator2:id/formula').text)
        self.assertEqual('0.5', self.driver.find_element_by_id('com.android.calculator2:id/result').text)
        self.driver.find_element_by_id('com.android.calculator2:id/op_div').click()
        self.driver.find_element_by_id('com.android.calculator2:id/digit_5').click()
        self.assertEqual('1÷2÷5', self.driver.find_element_by_id('com.android.calculator2:id/formula').text)
        self.assertEqual('0.1', self.driver.find_element_by_id('com.android.calculator2:id/result').text)

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(combine_reports=True, report_name='Android_Cal_TestReport', report_title='Android Calculator Test Report', add_timestamp=False))
