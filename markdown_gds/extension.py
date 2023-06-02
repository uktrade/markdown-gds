from xml.etree import ElementTree

from markdown.extensions import Extension
from markdown.treeprocessors import Treeprocessor

Element = ElementTree.Element


GDS_TAG_CLASS = {
    "p": "govuk-body",
    "a": "govuk-link",
    "ul": "govuk-list govuk-list--bullet",
    "ol": "govuk-list govuk-list--number",
    "h1": "govuk-heading-l",
    "h2": "govuk-heading-m",
    "h3": "govuk-heading-s",
}


class GdsTreeprocessor(Treeprocessor):
    def run(self, root):
        for el in root.iter("*"):
            match el:
                case Element(tag="p"):
                    el.set("class", GDS_TAG_CLASS["p"])
                case Element(tag="a"):
                    self.process_a(el)
                case Element(tag="ul"):
                    el.set("class", GDS_TAG_CLASS["ul"])
                case Element(tag="ol"):
                    el.set("class", GDS_TAG_CLASS["ol"])
                case Element(tag="h1"):
                    el.set("class", GDS_TAG_CLASS["h1"])
                case Element(tag="h2"):
                    el.set("class", GDS_TAG_CLASS["h2"])
                case Element(tag="h3"):
                    el.set("class", GDS_TAG_CLASS["h3"])

        return None

    def process_a(self, el):
        el.set("class", GDS_TAG_CLASS["a"])

        if self.config.get("open_links_in_new_tab", False):
            el.set("rel", "noreferrer noopener")
            el.set("target", "_blank")


class GdsExtension(Extension):
    def __init__(self, **kwargs):
        self.config = {
            "open_links_in_new_tab": [False, "Should links open in a new tab?"],
        }
        super().__init__(**kwargs)

    def extendMarkdown(self, md):
        gds_treeprocessor = GdsTreeprocessor(md)
        gds_treeprocessor.config = self.getConfigs()
        # TODO: Figure out the right priority.
        md.treeprocessors.register(gds_treeprocessor, name="gds", priority=5)
