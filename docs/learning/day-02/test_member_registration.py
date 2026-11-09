import unittest
from decimal import Decimal

from member_registration import(
    Member,
    validate_age, 
    validate_contribution,
    validate_email,
    validate_national_id,
    validate_email,
    generate_membership_number,
    is_duplicate_national_id,
)

