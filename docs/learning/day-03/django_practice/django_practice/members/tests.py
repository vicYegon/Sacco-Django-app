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

