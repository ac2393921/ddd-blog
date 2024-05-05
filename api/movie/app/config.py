from pydantic_settings import BaseSettings


class MySQLSettings(BaseSettings):
    MYSQL_USER: str
    MYSQL_PASSWORD: str
    MYSQL_HOST: str
    MYSQL_DATABASE: str


mysql_settings = MySQLSettings()
