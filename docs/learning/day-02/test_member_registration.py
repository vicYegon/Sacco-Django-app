import unittest

from decimal import Decimal
from unittest.mock import patch


from member_registration import(
    Member,
    get_member_details,
    validate_age, 
    validate_phone,
    validate_name,
    validate_contribution,
    validate_email,
    validate_national_id,
    generate_membership_number,
    is_duplicate_national_id,
)

class TestMemberValidation(unittest.TestCase):
    #age validation test functions
    def test_valid_age(self):
        result = validate_age("30")
        self.assertEqual(result, 30)

    def test_underage_member(self):
        result = validate_age("17")
        self.assertIsNone(result)

    def test_invalid_age(self):
        result = validate_age("abc")
        self.assertIsNone(result)

    #monthly contribution test functions
    def test_valid_contribution(self):
        result = validate_contribution("5000.50")
        self.assertEqual(result, Decimal("5000.50"))

    def test_negative_contribution(self):
        result = validate_contribution("-500")
        self.assertIsNone(result)

    def test_invalid_contribution(self):
        result = validate_contribution("abc")
        self.assertIsNone(result)

    def test_excess_decimal_places(self):
        result = validate_contribution("5000.123")
        self.assertIsNone(result)

    def test_nan_contribution(self):
        result = validate_contribution("NaN")
        self.assertIsNone(result)

    #name test functions
    def test_valid_name(self):
        self.assertEqual(validate_name("Victor Test"), "Victor Test")

    def test_empty_name(self):
        self.assertIsNone(validate_name(""))

    def test_short_name(self):
        self.assertIsNone(validate_name("vic"))


    #phone_number test function
    def test_valid_phone(self):
        self.assertEqual(validate_phone("0712121212"), "0712121212")

    def test_invalid_phone(self):
        self.assertIsNone(validate_phone("0712121"))

    def test_phone_used_in_duplicate_registration(self):
        result = validate_phone("0723456789")

        self.assertEqual(result, "0723456789")

    #email test functions
    def test_valid_email(self):
        self.assertEqual(validate_email("vy@example.com"), "vy@example.com")

    def test_invalid_email(self):
        self.assertIsNone(validate_email("victor"))

    #national id test functions
    def test_valid_national_id(self):
        self.assertEqual(validate_national_id("12345678"), "12345678")

    def test_invalid_national_id(self):
        self.assertIsNone(validate_national_id("123abd"))

class TestMembershipNumber(unittest.TestCase):

    def test_first_membership_number(self):
        result = generate_membership_number(0)
        self.assertEqual(result, "SACCO-0001")

    def test_second_membership_number(self):
        result = generate_membership_number(1)
        self.assertEqual(result, "SACCO-0002")

    def test_tenth_membership_number(self):
        result = generate_membership_number(9)
        self.assertEqual(result, "SACCO-0010")

class TestDuplicateMember(unittest.TestCase):

    def test_duplicate_national_id(self):
        member = Member(
            membership_number = "SACCO-0001",
            full_name = "vic test",
            national_id = "12345678",
            phone_number = "0112345678",
            email = "vic@example.com",
            age = 30,
            monthly_contribution = Decimal("3500.00")
        )

        members = [member]

        result = is_duplicate_national_id("12345678", members)

        self.assertTrue(result)

    def test_unique_national_id(self):
        member = Member(
            membership_number = "SACCO-0001",
            full_name = "vic test",
            national_id = "12345678",
            phone_number = "0112345678",
            email = "vic@example.com",
            age = 30,
            monthly_contribution = Decimal("3500.00")
        )

        members = [member]

        result = is_duplicate_national_id("87654321", members)

        self.assertFalse(result)

class TestMemberClass(unittest.TestCase):

    def test_member_creation(self):
        member = Member(
            membership_number = "SACCO-0001",
            full_name = "vic test",
            national_id = "12345678",
            phone_number = "0112345678",
            email = "vic@example.com",
            age = 30,
            monthly_contribution = Decimal("3500.00")
        )

        self.assertEqual(member.membership_number, "SACCO-0001")
        self.assertEqual(member.full_name, "vic test")
        self.assertEqual(member.status, "ACTIVE")
        self.assertEqual(member.monthly_contribution, Decimal("3500.00"))

class TestRegistrationFlow(unittest.TestCase):

    @patch("builtins.input")
    def test_duplicate_id_prompts_again(self, mock_input):

        existing_member = Member(
            membership_number="SACCO-0001",
            full_name="vic test",
            national_id="12345678",
            phone_number="0112345678",
            email="vic@example.com",
            age=30,
            monthly_contribution=Decimal("3500.00")
        )

        members = [existing_member]

        mock_input.side_effect = [
            "Lynn Test",
            "12345678",
            "87654321",
            "0712345678",
            "lynn@example.com",
            "25",
            "3500.00"
        ]

        result = get_member_details(members)

        self.assertEqual(
            result["national_id"],
            "87654321"
        )

        self.assertEqual(
            mock_input.call_count,
            7
        )



        self.assertEqual(result["national_id"], "87654321")
        self.assertEqual(mock_input.call_count, 7)