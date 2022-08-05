import markdown
import pytest

from markdown_gds import GdsExtension


@pytest.mark.parametrize(
    ["md", "expected"],
    [
        (
            "[example](https://example.com)",
            '<p class="govuk-body"><a class="govuk-link" href="https://example.com">example</a></p>',
        ),
    ],
)
def test_gds_extention(md, expected):
    assert markdown.markdown(md, extensions=[GdsExtension()]) == expected
