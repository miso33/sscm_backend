import pytest
from django.test import TestCase

from .admin import OriginalMemberAdmin
from .models import OriginalMember
from django.contrib.admin import AdminSite
from .factories import OriginalMemberFactory
from ..profiles.factories import IndividualProfileFactory, GroupProfileFactory


class OriginalDataTestCase(TestCase):

    @pytest.mark.original_data_admin
    def test_is_registered_individual_true(self):
        original_member = OriginalMemberFactory.create_batch(10)
        first_original_member = original_member[0]
        IndividualProfileFactory(
            first_name=first_original_member.firstname,
            last_name=first_original_member.surname,
            birth_date=first_original_member.datum_nar,
        )
        self.assertTrue(
            OriginalMemberAdmin(
                model=OriginalMember,
                admin_site=AdminSite
            ).is_registered(first_original_member)
        )

    @pytest.mark.original_data_admin
    def test_is_registered_individual_false(self):
        original_member = OriginalMemberFactory.create_batch(10)
        first_original_member = original_member[0]
        self.assertFalse(
            OriginalMemberAdmin(
                model=OriginalMember,
                admin_site=AdminSite
            ).is_registered(first_original_member)
        )

    @pytest.mark.original_data_admin
    def test_is_registered_group_true(self):
        original_member = OriginalMemberFactory.create_batch(10, firstname="x")
        first_original_member = original_member[0]
        GroupProfileFactory(
            name=first_original_member.surname,
        )
        self.assertTrue(
            OriginalMemberAdmin(
                model=OriginalMember,
                admin_site=AdminSite
            ).is_registered(first_original_member)
        )

    @pytest.mark.original_data_admin
    def test_is_registered_group_false(self):
        original_member = OriginalMemberFactory.create_batch(10, firstname="x")
        first_original_member = original_member[0]
        self.assertFalse(
            OriginalMemberAdmin(
                model=OriginalMember,
                admin_site=AdminSite
            ).is_registered(first_original_member)
        )
