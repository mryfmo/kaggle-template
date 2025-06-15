# {{ cookiecutter.project_name }}

## setup

```bash
export KAGGLE_USERNAME={YOUR_KAGGLE_USERNAME}
export KAGGLE_KEY={YOUR_KAGGLE_KEY}
```

```bash
uv sync
```

## download competition dataset

```bash
sh scripts/download_competition.sh
```

## submission flow

1. Create an experiment folder in `experiments`.

2. Conducting the experiment.

3. Upload the code and models you want to use in your submission using one of the following methods:

  - Running the code.

    ```python
    from src.kaggle_utils.customhub import dataset_upload, model_upload

    model_upload(
      handle=config.ARTIFACTS_HANDLE,
      local_model_dir=config.OUTPUT_DIR,
      update=False,
    )
    dataset_upload(
      handle=config.CODES_HANDLE,
      local_dataset_dir=config.ROOT_DIR,
      update=True,
    )
    ```

  - Running the script.

    ```bash
    sh scripts/push_experiment.sh 001
    ```

4. Push the required dependencies.

   ```sh
   sh scripts/push_deps.sh
   ```

5. submission

   ```sh
   sh scripts/push_sub.sh
   ```

## lint & format

```bash
uv run pre-commit run -a
```

## Reference

- [効率的なコードコンペティションの作業フロー](https://ho.lc/blog/kaggle_code_submission/)
- [Kaggleコンペ用のVScode拡張を開発した](https://ho.lc/blog/vscode_kaggle_extension/)
- [kaggle code competition 用のテンプレート作ってみた](https://osushinekotan.hatenablog.com/entry/2024/12/24/193145)
