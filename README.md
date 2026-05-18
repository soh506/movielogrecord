# プルリクなどの一連の流れを経験する
## 2. issueを立てる（これが重要）
GitHubのIssuesタブで「やること」を先に書く。例えば：

- #1 READMEを追加する
- #2 映画にジャンルフィールドを追加する
- #3 一覧ページに検索機能をつける

## 3. ブランチを切って作業する
- bashgit checkout -b feature/add-readme   # issue #1 の作業
- 変更する
- git add .
- git commit -m "docs: READMEを追加 #1"
- git push origin feature/add-readme


## 4. GitHubでPRを作る
- pushするとGitHubに「Compare & pull request」ボタンが出る。説明を書いてPRを作成。


## 5. マージしてブランチを消す
- bashgit checkout main
- git pull
- git branch -d feature/add-readme

最初にやる改善ネタ（順番通りに）

- README追加——一番簡単、フロー体験だけが目的
- requirements.txt追加——pip freeze > requirements.txt
- モデルにフィールド追加——例：映画にrating（評価）を追加してマイグレーション
- テストを1本書く——python manage.py testが通る状態にする

これを4回繰り返すだけで、「issue → branch → commit → PR → merge」の筋肉がつきます。やってみますか？
