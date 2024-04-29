from app.database import engine
from app.models.movie import Movie, RentalType
from sqlalchemy.orm import sessionmaker

# セッションの作成（事前にエンジンを設定している必要があります）
Session = sessionmaker(bind=engine)
session = Session()

print(1)

# ダミーデータの作成
movies = [
    Movie(title="ショーシャンクの空に", rental_type=RentalType.OLD_RELEASE),
    Movie(title="ゴッドファーザー", rental_type=RentalType.OLD_RELEASE),
    Movie(title="ダークナイト", rental_type=RentalType.SEMI_NEW_RELEASE),
    Movie(title="パルプ・フィクション", rental_type=RentalType.OLD_RELEASE),
    Movie(
        title="ロード・オブ・ザ・リング 王の帰還", rental_type=RentalType.OLD_RELEASE
    ),
    Movie(title="続・夕陽のガンマン", rental_type=RentalType.OLD_RELEASE),
    Movie(title="フォレスト・ガンプ", rental_type=RentalType.OLD_RELEASE),
    Movie(title="インセプション", rental_type=RentalType.SEMI_NEW_RELEASE),
    Movie(title="マトリックス", rental_type=RentalType.OLD_RELEASE),
    Movie(title="グッドフェローズ", rental_type=RentalType.OLD_RELEASE),
    Movie(
        title="スター・ウォーズ エピソード5/帝国の逆襲",
        rental_type=RentalType.OLD_RELEASE,
    ),
    Movie(title="カッコーの巣の上で", rental_type=RentalType.OLD_RELEASE),
    Movie(title="パラサイト 半地下の家族", rental_type=RentalType.NEW_RELEASE),
    Movie(title="インターステラー", rental_type=RentalType.SEMI_NEW_RELEASE),
    Movie(title="シティ・オブ・ゴッド", rental_type=RentalType.OLD_RELEASE),
    Movie(title="千と千尋の神隠し", rental_type=RentalType.OLD_RELEASE),
    Movie(title="プライベート・ライアン", rental_type=RentalType.OLD_RELEASE),
    Movie(title="グリーンマイル", rental_type=RentalType.OLD_RELEASE),
    Movie(title="ライフ・イズ・ビューティフル", rental_type=RentalType.OLD_RELEASE),
    Movie(title="ピアニスト", rental_type=RentalType.OLD_RELEASE),
]

# データベースにダミーデータを追加
session.add_all(movies)
session.commit()
