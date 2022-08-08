from textwrap import dedent

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
        (
            """
            - item 1
            - item 2
            - item 3
            """,
            '<ul class="govuk-list govuk-list--bullet">\n<li>item 1</li>\n<li>item 2</li>\n<li>item 3</li>\n</ul>',
        ),
        (
            """
            1. item 1
            2. item 2
            3. item 3
            """,
            '<ol class="govuk-list govuk-list--number">\n<li>item 1</li>\n<li>item 2</li>\n<li>item 3</li>\n</ol>',
        ),
    ],
)
def test_gds_extention(md, expected):
    assert markdown.markdown(dedent(md), extensions=[GdsExtension()]) == expected
