"""TDD DEMO!"""
from django.test import TestCase


# Create your tests here.
class DemoTests(TestCase):
    """Demonstrate basic testing in TDD!"""

    def test_ping_get(self):
        """GET ping"""
        response = self.client.get("/ping/")
        self.assertEqual(response.status_code, 200)

        self.assertEqual(
            response.content.decode("utf8"), "pong"
        )

    def test_ping_head(self):
        """HEAD ping"""
        response = self.client.head("/ping/")

        self.assertEqual(response.status_code, 200)

        self.assertEqual(response.content, b"")

        self.assertGreater(
            int(response["Content-Length"]), 0
        )

    def test_ping_options(self):
        """OPTIONS ping"""
        response = self.client.options("/ping/")

        self.assertEqual(response.status_code, 200)

        self.assertEqual(int(response["Content-Length"]), 0)

        for method in ["GET", "HEAD", "OPTIONS"]:
            with self.subTest(method=method):
                self.assertIn(
                    method,
                    response["Allow"],
                    f"{method} not in ALLOW header",
                )

    def test_ping_method_not_allowed(self):
        """Do we handle disallowed methods"""
        not_allowed = [
            "post",
            "put",
            "delete",
            "patch",
            "trace",
        ]

        for method in not_allowed:
            with self.subTest(mehtod=method):
                call_method = getattr(self.client, method)
                response = call_method("/ping/")

                self.assertEqual(response.status_code, 405)
