class DomainException(Exception):
    """ドメインエラーを表すカスタム例外クラス"""

    def __init__(self, message: str = "ドメインエラーが発生しました。"):
        super().__init__(message)
        self.message = message
