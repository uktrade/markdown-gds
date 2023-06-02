from textwrap import dedent

import markdown
import pytest

from markdown_gds import GdsExtension


@pytest.mark.parametrize(
    ["md", "expected"],
    [
        # paragraph
        (
            "hello world",
            '<p class="govuk-body">hello world</p>',
        ),
        # link
        (
            "[example](https://example.com)",
            '<p class="govuk-body"><a class="govuk-link" href="https://example.com">example</a></p>',
        ),
        # unordered list
        (
            """
            - item 1
            - item 2
            - item 3
            """,
            '<ul class="govuk-list govuk-list--bullet">\n<li>item 1</li>\n<li>item 2</li>\n<li>item 3</li>\n</ul>',
        ),
        # ordered list
        (
            """
            1. item 1
            2. item 2
            3. item 3
            """,
            '<ol class="govuk-list govuk-list--number">\n<li>item 1</li>\n<li>item 2</li>\n<li>item 3</li>\n</ol>',
        ),
        # h1
        (
            "# hello world",
            '<h1 class="govuk-heading-l">hello world</h1>',
        ),
        # h2
        (
            "## hello world",
            '<h2 class="govuk-heading-m">hello world</h2>',
        ),
        # h3
        (
            "### hello world",
            '<h3 class="govuk-heading-s">hello world</h3>',
        ),
    ],
)
def test_gds_extention(md, expected):
    assert markdown.markdown(dedent(md), extensions=[GdsExtension()]) == expected


def test_open_links_in_new_tab():
    md = "[example](https://example.com)"
    expected = '<p class="govuk-body"><a class="govuk-link" href="https://example.com" rel="noreferrer noopener" target="_blank">example</a></p>'
    html = markdown.markdown(md, extensions=[GdsExtension(open_links_in_new_tab=True)])
    assert html == expected
