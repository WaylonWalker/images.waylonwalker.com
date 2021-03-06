from string import Template
from pathlib import Path

with open("template/index.html") as f:
    index_template = Template(f.read())
with open("template/image.html") as f:
    image_template = Template(f.read())
images = "".join(
    [
        image_template.safe_substitute(file=file.name)
        for file in Path("static/thumb").glob("*")
    ]
)

index = index_template.safe_substitute(images=images)

with open("static/index.html", "w+") as f:
    f.write(index)
