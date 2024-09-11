from pydantic_settings import BaseSettings, SettingsConfigDict

class SettingEnvFile(BaseSettings):
    database_url: str
    project_name: str
    model_config = SettingsConfigDict(env_file= ".env")

settings = SettingEnvFile();


