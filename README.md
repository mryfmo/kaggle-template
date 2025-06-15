# Kaggle Template

A template for the Kaggle code competition using cookiecutter.

## Quickstart

**install cookiecutter**

```bash
pip install cookiecutter
```

**Create a project**

1. If you create the entire project root directory:

    ```bash
    cookiecutter https://github.com/osushinekotan/kaggle-template.git
    ```

2. If you want to use a project root directory that you have already created (such as a cloned repository):

    ```bash
    cd {project_dir}
    cookiecutter https://github.com/osushinekotan/kaggle-template.git -f -o ../
    ```

    - `project_slug` and `{projet_dir}` have the same name, and you create a template by overwriting it.
    - Use cookicutter's [CL options](https://cookiecutter.readthedocs.io/en/1.7.0/advanced/cli_options.html).

**cookiecutter parameters**

- `competition_name`: The name of the Kaggle competition. Use the name in the competition URL or the name specified with `kaggle competitions download -c {competition_name}` here.
- `project_name`: The name of your project.
- `project_slug`: The name of the directory to be created.
- `project_description`: Project description.
- `kaggle_username`: Your kaggle username
- `python_version`: The python version to use. Specify it as `3.11` or `3.12`.

## Reference

- [kaggle code competition 用のテンプレート作ってみた](https://osushinekotan.hatenablog.com/entry/2024/12/24/193145)
