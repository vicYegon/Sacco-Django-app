import re

from rest_framework import serializers

from .models import Member

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member

        fields = ["id","full_name","phone_number","email",]

class MemberRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ["id", "full_name", "national_id", "phone_number", "email","age","monthly_contribution"]
        read_only_fields = ["id"]

    def validate_full_name(self, value):
        cleaned = " ".join(value.split())

        if len(cleaned.split(" ")) < 2:
            raise serializers.ValidationError(
                "Enter at least a first name and a last name."
            )

        return cleaned.title()

    def validate_national_id(self, value):
        cleaned = value.strip()

        if not cleaned.isdigit():
            raise serializers.ValidationError(
                "National ID must contain digits only."
            )

        if not 7 <= len(cleaned) <= 8:
            raise serializers.ValidationError(
                "National ID must be 7 or 8 digits."
            )

        return cleaned

    def validate_phone_number(self, value):
        cleaned = value.replace(" ", "").strip()

        if not re.fullmatch(r"(07|01)\d{8}", cleaned):
            raise serializers.ValidationError(
                "Phone number must be 10 digits and start with 07 or 01."
            )

        return cleaned

    def validate_age(self, value):
        if value < 18:
            raise serializers.ValidationError(
                "A member must be at least 18 years old."
            )

        if value > 120:
            raise serializers.ValidationError("Enter a valid age.")

        return value

    def validate_monthly_contribution(self, value):
        if value <= 0:
            raise serializers.ValidationError("Monthly contribution must be greater than zero.")

        return value