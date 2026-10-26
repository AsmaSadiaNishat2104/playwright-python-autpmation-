
import pytest
import allure

from playwright.sync_api import Page
from pages.login import LoginPage


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    setattr(item, "rep_" + report.when, report)


@pytest.fixture
def login_page(page: Page, request, tmp_path):
    # Start recording the trace
    page.context.tracing.start(
        screenshots=True,
        snapshots=True,
        sources=True
    )

    login = LoginPage(page)

    try:
        login.open()

        # Execute the test
        yield login

    finally:
        failed = (
            getattr(request.node, "rep_call", None) is not None
            and request.node.rep_call.failed
        )

        if failed:
            # Attach failure screenshot
            allure.attach(
                page.screenshot(full_page=True),
                name="Failure Screenshot",
                attachment_type=allure.attachment_type.PNG
            )

            # Save the trace
            trace_path = tmp_path / "trace.zip"

            page.context.tracing.stop(path=str(trace_path))

            # Attach trace ZIP to Allure
            allure.attach.file(
                str(trace_path),
                name="Playwright Trace",
                attachment_type="application/zip",
                extension="zip"
            )
        else:
            # Stop tracing without saving a ZIP
            page.context.tracing.stop()
