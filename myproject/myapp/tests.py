from django.test import TestCase
from django.urls import reverse
from .models import Product

#  create all tests here
class ProductTests(TestCase):

    def setUp(self):
        Product.objects.create(name="Product 1", description="Description 1", price=19.99)

    def test_product_list_view(self):
        url = reverse('index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'product/product_list.html')
        self.assertContains(response, "Our Products", html=True)

    def test_product_detail_view(self):
        product = Product.objects.get(name="Product 1")
        url = reverse('detail', args=[product.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'product/product_detail.html')
        self.assertContains(response, "Product 1", html=True)
    
    def test_product_create_view(self):
        url = reverse('create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'product/product_form.html')
        self.assertContains(response, "Create Product", html=True)
    
    def test_product_update_view(self):
        product = Product.objects.get(name="Product 1")
        url = reverse('update', args=[product.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'product/product_form.html')
        self.assertContains(response, "Update Product", html=True)
    
    def test_product_delete_view(self):
        product = Product.objects.get(name="Product 1")
        url = reverse('delete', args=[product.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'product/product_delete.html')
        self.assertContains(response, "Are you sure you want to delete", html=True)
