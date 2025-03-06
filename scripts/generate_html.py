import os
from jinja2 import Environment, FileSystemLoader

def generate_html(template_dir, output_dir, template_name, context):
    """
    Generates an HTML file from a Jinja2 template.
    """
    env = Environment(loader=FileSystemLoader(template_dir))
    template = env.get_template(template_name)
    output_path = os.path.join(output_dir, template_name.replace(".html", ".html"))  # Correct output path
    with open(output_path, "w") as f:
        f.write(template.render(context))
    print(f"Generated {output_path}")


if __name__ == "__main__":
    template_dir = "templates"
    output_dir = "."  # Output to the root directory
    context = {
        "title": "Teal Research Lab",
        "lab_name": "Teal Research Lab"
    }

    generate_html(template_dir, output_dir, "index.html", context)
    generate_html(template_dir, output_dir, "about.html", context)
    generate_html(template_dir, output_dir, "research.html", context)
    generate_html(template_dir, output_dir, "workshop.html", context)
    generate_html(template_dir, output_dir, "contact.html", context)