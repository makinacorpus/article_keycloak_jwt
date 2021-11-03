from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from oidc_auth.test import AuthenticationTestCaseMixin, make_id_token


def make_jwt_header(sub, aud):
    """
    Create an authorization token and returns it in the form of a dict ready to be included as a HTTP header
    @param user: The user to authorize
    @return: A dict holding the JWT
    """
    auth = "jwt " + str(make_id_token(sub=str(sub), aud=aud, typ="Bearer"))
    header = {"HTTP_AUTHORIZATION": auth}
    return header


class AuthenticatedJwtTestCase(AuthenticationTestCaseMixin, TestCase):
    def setUp(self):
        _ = User.objects.create(
                username="henk"
        )  # Needed for AuthenticationTestCaseMixin to work
        super().setUp()


class TestPermissionView(AuthenticatedJwtTestCase):
    def setUp(self):
        super().setUp()

    def test_unlogged_user(self):
        """
        Test that an unlogged user can't access the protected view.
        """
        response = self.client.get(
                reverse(
                        "jwt_demo:my_api",
                ),
        )

        self.assertEqual(response.status_code, 401)

    def test_logged_user(self):
        user = User.objects.create(username="test_user")
        self.client.force_login(user)

        self.responder.set_response(
                "http://example.com/userinfo", {"sub": str(user.username)}
        )
        response = self.client.get(
                reverse(
                        "jwt_demo:my_api",
                ),
                **make_jwt_header(user.username, "my_api_client_id"),
        )

        self.assertEqual(response.status_code, 200)
