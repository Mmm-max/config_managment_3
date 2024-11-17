import unittest
from app import xml_to_custom_language as app
 

class TestApp(unittest.TestCase):

# тесттировние основных функций
    def test_array(self):
        xml = """
        <root>
            <array>
                <string>foo</string>
                <string>bar</string>
                <string>loss</string>
            </array>
        </root>
        """
        expected = "<< foo, bar, loss >>"
        self.assertEqual(app(xml), expected)
    
    def test_dictionary(self):
        xml = "<root><dictionary><entry name='key1'>value1</entry>\
            <entry name='key2'>value2</entry></dictionary></root>"
        expected = "table(\n  key1 => value1,\n  key2 => value2\n)"
        self.assertEqual(app(xml), expected)
        
    def test_string(self):
        xml = "<root><string>hello</string></root>"
        expected = "@\"hello\""
        self.assertEqual(app(xml), expected)
    
    def test_constant(self):
        xml = "<root><constant name='PI'>3.14</constant></root>"
        expected = "const PI = 3.14;"
        self.assertEqual(app(xml), expected)
    
    def test_comment(self):
        xml = "<root><comment>hello</comment></root>"
        expected = "{#\n hello\n#}"
        self.assertEqual(app(xml), expected)
    
    def test_compute(self):
        xml = "<root><compute><name>result</name></compute></root>"
        expected = "?result"
        self.assertEqual(app(xml), expected)
        
# тест ошибок
    def test_unknown_element(self):
        xml = "<root><unknown>...</unknown></root>"
        with self.assertRaises(ValueError):
            app(xml)
        
    def test_invalid_xml(self):
        xml = "<root><array><string>foo</array></root>"
        with self.assertRaises(ValueError):
            app(xml)
    