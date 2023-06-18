import unittest
from xml2Json import convert_xml_to_json

class XMLToJsonTestCase(unittest.TestCase):
    def test_convert_xml_to_json_easy(self):
        xml_string = '''
            <root>
                <person>
                    <name>John Doe</name>
                    <age>30</age>
                </person>
                <person>
                    <name>Jane Smith</name>
                    <age>25</age>
                </person>
            </root>
        '''

        expected_json = '''{"text":"","person":[{"text":"","name":{"text":"JohnDoe"},"age":{"text":"30"}},{"text":"","name":{"text":"JaneSmith"},"age":{"text":"25"}}]}'''
        json_data = convert_xml_to_json(xml_string).replace('\n', '').replace(" ", "")
        self.assertEqual(json_data, expected_json)

    def test_convert_xml_to_json_hard(self):
        xml_string = '''
            <root>
                <bookstore>
                    <book category="fiction">
                        <title>The Great Gatsby</title>
                        <author>F. Scott Fitzgerald</author>
                        <year>1925</year>
                        <price currency="USD">10.99</price>
                    </book>
                    <book category="fiction">
                        <title>To Kill a Mockingbird</title>
                        <author>Harper Lee</author>
                        <year>1960</year>
                        <price currency="USD">12.99</price>
                    </book>
                    <book category="nonfiction">
                        <title>The Elements of Style</title>
                        <author>William Strunk Jr.</author>
                        <year>1918</year>
                        <price currency="USD">9.99</price>
                    </book>
                </bookstore>
            </root>
        '''
        expected_json = '''{"text":"","bookstore":{"text":"","book":[{"@attributes":{"category":"fiction"},"text":"","title":{"text":"TheGreatGatsby"},"author":{"text":"F.ScottFitzgerald"},"year":{"text":"1925"},"price":{"@attributes":{"currency":"USD"},"text":"10.99"}},{"@attributes":{"category":"fiction"},"text":"","title":{"text":"ToKillaMockingbird"},"author":{"text":"HarperLee"},"year":{"text":"1960"},"price":{"@attributes":{"currency":"USD"},"text":"12.99"}},{"@attributes":{"category":"nonfiction"},"text":"","title":{"text":"TheElementsofStyle"},"author":{"text":"WilliamStrunkJr."},"year":{"text":"1918"},"price":{"@attributes":{"currency":"USD"},"text":"9.99"}}]}}'''
        json_data = convert_xml_to_json(xml_string).replace('\n', '').replace(" ", "")
        self.assertEqual(json_data, expected_json)

if __name__ == '__main__':
    unittest.main()
