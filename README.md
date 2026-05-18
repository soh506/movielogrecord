# movielogrecord

Django の仕組みを学ぶことを目的に作った映画視聴記録アプリ。  
観た映画のタイトル・監督・視聴日・感想を記録・管理できる。

## 機能

- 映画視聴一覧の表示
- 映画詳細（タイトル・監督・視聴日・感想）の表示
- 映画情報の登録・編集・削除（CRUD）

## 技術スタック

- Python 3.8.2
- Django 3.0.2
- SQLite3

## ディレクトリ構成

```
.
├── config/
│   ├── settings.py
│   └── urls.py
├── myapp/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── forms.py
├── templates/
│   └── myapp/
├── manage.py
└── .gitignore
```
## セットアップ

```bash
git clone https://github.com/soh506/movielogrecord.git
cd movielogrecord

python -m venv myenv
source myenv/bin/activate

pip install django

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

ブラウザで `http://127.0.0.1:8000` を開く。

## 参考記事

作成過程を Qiita にまとめています。

- [Django 初心者が簡単なアプリをつくる1](https://qiita.com/soh506/items/4035650d2ea19e82d8fd)
- [Django 初心者が簡単なアプリをつくる2](https://qiita.com/soh506/items/98239c6b1c6fbf737429)
- [Django 初心者が簡単なアプリをつくる3](https://qiita.com/soh506/items/34cef1d386e1aa1b4496)
- [Django 初心者が簡単なアプリをつくる4](https://qiita.com/soh506/items/ac9b2914f64839edac3b)
- [Django 初心者が簡単なアプリをつくる5](https://qiita.com/soh506/items/fc6b00ba728ac41fa3d1)
