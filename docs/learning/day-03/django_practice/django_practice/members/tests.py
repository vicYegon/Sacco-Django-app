from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase

from django.test import TestCase
from django.db import IntegrityError, transaction

from decimal import Decimal

from .models import Member

# Create your tests here.
class MemberModelTests(TestCase):

    def test_create_member(self):
        member = Member.objects.create(
            full_name = "Victor Test",
            national_id = "12345678",
            phone_number = "0712345678",
            email = "vicyen@example.com",
            age = 34,
            monthly_contribution = Decimal("23000.00")
        )

        self.assertEqual(member.full_name, "Victor Test")
        self.assertEqual(member.national_id, "12345678")
        self.assertEqual(member.monthly_contribution, Decimal("23000.00"))

    #testing for duplicate national IDs
    def test_duplicate_national_id(self):
        Member.objects.create(
            full_name = "Victor Test",
            national_id = "12345678",
            phone_number = "0712345678",
            email = "vicyen@example.com",
            age = 34,
            monthly_contribution = Decimal("23000.00")
        )

        with self.assertRaises(IntegrityError):
            with transaction.atomic():
                Member.objects.create(
                    full_name = "Mary Test",
                    national_id = "12345678",
                    phone_number = "0723545678",
                    email = "mt@example.com",
                    age = 30,
                    monthly_contribution = Decimal("24000.00")
                )

    #testing member retrieval
    def test_retrieve_member(self):
        Member.objects.create(
            full_name = "Victor Test",
            national_id = "12345678",
            phone_number = "0712345678",
            email = "vicyen@example.com",
            age = 34,
            monthly_contribution = Decimal("23000.00")
        )

        member = Member.objects.get(
            national_id = "12345678"
        )

        self.assertEqual(member.full_name, "Victor Test")

class MemberAPITests(APITestCase):

    def setUp(self):
        self.url = "/members/api/"

        self.staff_user = User.objects.create_user(
            username="staff", password="testpass123", is_staff=True
        )
        self.normal_user = User.objects.create_user(
            username="normal", password="testpass123"
        )

        Member.objects.create(
            full_name = "Victor Test",
            national_id = "12345678",
            phone_number = "0712345678",
            email = "vicyen@example.com",
            age = 34,
            monthly_contribution = Decimal("23000.00")
        )

    def test_unauthenticated_user_is_refused(self):
        response = self.client.get(self.url)
        self.assertIn(
            response.status_code,
            [status.HTTP_401_UNAUTHORIZED, status.HTTP_403_FORBIDDEN],
        )

    def test_non_staff_user_is_refused(self):
        self.client.force_authenticate(user=self.normal_user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_staff_user_can_list_members(self):
        self.client.force_authenticate(user=self.staff_user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_response_contains_expected_fields(self):
        self.client.force_authenticate(user=self.staff_user)
        response = self.client.get(self.url)
        member = response.data[0]
        for field in ["id", "full_name", "phone_number", "email"]:
            self.assertIn(field, member)

    def test_post_method_not_allowed(self):
        self.client.force_authenticate(user=self.staff_user)
        response = self.client.post(self.url, {})
        self.assertEqual(
            response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED
        )