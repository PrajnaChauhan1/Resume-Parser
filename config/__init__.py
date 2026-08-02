from pathlib import Path

from dynaconf import Dynaconf


BASE_DIR = Path(__file__).parent.parent.absolute()
ENV_PATH = BASE_DIR / ".env"


settings = Dynaconf(
    envvar_prefix="RESUME",
    settings_files=["settings.toml"],
    load_dotenv=True,
    dotenv_path=ENV_PATH,
)
