from django.test import TestCase

# Create your tests here.
class SampleTestCase(TestCase):
    def test_sample(self):
        self.assertEquals(1+2, 3)