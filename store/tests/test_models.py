from django.test import TestCase
from django.contrib.auth.models import User
from ..models import Category, Products



class CategoryModelTest(TestCase):
    
    def setUp(self):
        Category.objects.create(name = 'software development', slug ='software development')
        
    def test_model_instance(self):
        dataInstance = Category.objects.get(id = 1)
        
        # tell me confidently if dataInstance is an instance or
        # subclass of the class Products
        self.assertIsInstance(dataInstance, Category) 
        
    def test_name_content(self):
        book = Category.objects.get(id = 1)
        expected_content =  f"{book.name}"
        
        #tell me if expected_content is the same or equal to software development
        self.assertEqual(expected_content, 'software development')
        self.assertEqual(str(book), 'software development')
        


class ProductsModelTest(TestCase):
    
    # because of the foreign key relations, we need to use the 
    # category and user models
     
    
    def setUp(self):
        Category.objects.create(name= 'django', slug = 'django')
        User.objects.create(username = 'root')
        self.data = Products.objects.create(category_id = 1, title='django for professionals', created_by_id = 1,
                                            slug = 'django-for-professionals', price = '20.00', image = 'django')
        
    def test_model_instance(self):
        dataInstance = self.data
        
        # tell me confidently if dataInstance is an instance or
        # subclass of the class Products
        self.assertIsInstance(dataInstance, Products) 
        self.assertEqual(str(dataInstance), 'django for professionals')
        #self.assert(isinstance(dataInstance, Product))
        
        
        

        
    
        