from xml.etree import ElementTree

from markdown.extensions import Extension
from markdown.treeprocessors import Treeprocessor

Element = ElementTree.Element


GDS_TAG_CLASS = {
    "p": "govuk-body",
    "a": "govuk-link",
}


class GdsTreeprocessor(Treeprocessor):
    def run(self, root):
        for el in root.iter("*"):
            match el:
                case Element(tag="p"):
                    el.set("class", GDS_TAG_CLASS["p"])
                case Element(tag="a"):
                    el.set("class", GDS_TAG_CLASS["a"])

        return None


class GdsExtension(Extension):
    def extendMarkdown(self, md):
        # TODO: Figure out the right priority.
        md.treeprocessors.register(GdsTreeprocessor(md), name="gds", priority=5)
