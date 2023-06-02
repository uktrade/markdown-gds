# markdown-gds

## Getting started

### Installation

`markdown-gds` is published on PyPI and can be installed using `pip`:

```bash
pip install markdown-gds
```

### Usage

```python
import markdown
from markdown_gds import GdsExtension

markdown.markdown(some_text, extensions=[GdsExtension()])
```

## Contributing

Install the project locally using `poetry`:

```bash
poetry install
```

Then run the tests to ensure everything is working:

```bash
poetry run pytest
```
