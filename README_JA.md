# Asian Workshop on Scientific Machine Learning 2027：編集・公開ガイド

2027年4月26〜28日にアクロス福岡で開催予定の国際会議向けに作成した、英語のJekyllサイトです。本文はMarkdown、共通情報はYAMLで編集します。テンプレートとCSSを分離しているため、通常の内容更新でHTMLを変更する必要はありません。

## 1. 内容の位置づけ

依頼時に指定された情報は、**会議名、開催予定日、会場**です。`Asian SciML 2027` はナビゲーション用の短い表記であり、公式略称として決められたものではありません。研究分野の4項目と会議概要文は編集案です。正式な開催趣旨に合わせて変更してください。

委員、主催・協賛団体、講演者、参加費、申込期限、募集形式、会議室は後日案内として扱っています。参加登録情報も後日掲載する旨を表示しています。初期のお知らせの日付は2026年10月20日です。実際の告知日に合わせて更新できます。

研究分野の掲載を保留する場合は、`_data/conference.yml` を次のようにします。

```yaml
show_topics: false
```

## 2. ローカルで表示する

Ruby 3.3系の新しいパッチ版とBundler 2.6.9を用意してください。同梱の`Gemfile.lock`はJekyll 4.4.1を使用し、依存ライブラリの条件から**Ruby 3.2以上の3.x系**が必要です。実際のビルド確認にはRuby 3.3.9を使用しました。Bundlerを実行するターミナルで`ruby -v`を確認してください。OS別の準備は[Jekyllの公式インストール案内](https://jekyllrb.com/docs/installation/)を参照できます。

解凍したプロジェクトのディレクトリで実行します。

```sh
gem install bundler -v 2.6.9
bundle _2.6.9_ install
bundle _2.6.9_ exec jekyll serve
```

ブラウザーで <http://localhost:4000/> を開きます。MarkdownやCSSの変更は保存後に再生成されます。`_config.yml`を変更した場合はサーバーを停止し、再起動してください。

公開用のHTMLを生成するコマンドは次のとおりです。

```sh
bundle exec jekyll build
```

生成物は`_site/`に入ります。`_site/`を直接編集しても、次のビルドで上書きされます。更新は必ず元のMarkdown・YAML・CSSに反映してください。

配布物に`preview/`が含まれている場合は、Rubyを導入する前に次の方法で完成時点の表示を確認できます。

```sh
python3 -m http.server 8000 --directory preview
```

<http://localhost:8000/> を開いてください。`/programme/`のようなディレクトリ形式のURLはHTTPサーバーで表示する前提です。`index.html`のダブルクリックによる`file://`では、すべてのリンクの動作を保証しません。`preview/`は同梱時点の静的な写しで、本文を変更した後の表示にはJekyllでの再生成が必要です。

### `public_suffix 7.0.5`のインストールで停止する場合

`An error occurred while installing public_suffix ...`の後に出る依存関係の一覧だけでは、直接の原因は確定できません。まず、同じターミナルで次を確認します。

```sh
ruby -v
gem --version
bundle -v
command -v ruby
command -v bundle
```

`public_suffix 7.0.5`と`sass-embedded 1.105.2`はいずれもRuby 3.2以上を要求します。使用中のRubyが3.1以前の場合は、Ruby 3.3系へ切り替え、そのRubyでBundlerをインストールしてください。`public_suffix`だけを6.xへ下げても、残りの依存関係がRuby 3.2を要求するため、このlockfile全体の互換性は解決しません。

rbenvとruby-buildを導入・設定済みの場合は、サイトのフォルダーで例えば次を実行できます。Ruby 3.3.12は2026年10月21日時点で公式リリース一覧に掲載されている3.3系のパッチ版です。

```sh
rbenv install -s 3.3.12
rbenv local 3.3.12
ruby -v
gem install bundler -v 2.6.9
bundle _2.6.9_ install
bundle _2.6.9_ exec jekyll serve
```

`ruby -v`が選択したバージョンになっていることを確認してから進めます。`rbenv install`が使えない場合は[rbenvの公式導入手順](https://github.com/rbenv/rbenv)を確認してください。別のRuby管理ツールを利用している場合は、そのツールでRubyを選択します。`Gemfile.lock`は保持して利用します。

Rubyがすでに3.2以上なら、依存関係の一覧より前に表示される最初のエラーを確認します。`requires Ruby version`ならバージョン条件、`Gem::FilePermissionError`や`EACCES`なら書き込み権限、`certificate verify failed`なら証明書の問題であり、それぞれ対処が異なります。原因を確認する際は、OS、上記コマンドの出力、最初のエラーの前後を共有してください。

`Gemfile`には`ruby ">= 3.2", "< 4.0"`を明示しています。この宣言は不適合なRubyを早い段階で検出するもので、Ruby本体を自動で更新・切り替える機能ではありません。

要件の出典：[public_suffix 7.0.5](https://rubygems.org/gems/public_suffix/versions/7.0.5)、[sass-embedded 1.105.2](https://rubygems.org/gems/sass-embedded/versions/1.105.2)、[Ruby公式リリース一覧](https://www.ruby-lang.org/en/downloads/releases/)。

## 3. 編集箇所の対応

| 更新する内容 | ファイル |
| --- | --- |
| トップページの会議概要 | `index.md` |
| プログラムの説明・詳細日程 | `programme.md` |
| 参加登録、発表募集、問い合わせ案内 | `participation.md` |
| 会場、交通、受付案内 | `venue.md` |
| ページが見つからない場合の案内 | `404.md` |
| 会議名、会期、会場などの共通情報 | `_data/conference.yml` |
| 日付別のプログラム概要 | `_data/programme.yml` |
| お知らせ | `_data/announcements.yml` |
| 研究分野の説明 | `_data/topics.yml` |
| メニュー | `_data/navigation.yml` |
| 写真の相対パス・代替テキスト・クレジット | `_data/photo.yml` |
| ブラウザーのタイトル、検索用説明、公開URL、`assets_path` | `_config.yml` |
| 色、書体、余白、スマートフォン・印刷表示 | `assets/css/main.css`（初期ディレクトリ） |
| 共通レイアウトと部分テンプレート | `_layouts/`、`_includes/` |
| ページ相対の内部リンク・素材URL | `_includes/local-url.html`、`_includes/asset-url.html` |
| カレンダーファイルの書式・説明文 | `assets/calendar/asian-sciml-2027.ics`（初期ディレクトリ） |

各Markdownの先頭にある`---`で囲まれた部分はfront matterです。`title`はページ見出し、`description`はページの説明、`permalink`は公開パスです。通常は`layout`と`nav_id`を変更せず、下の本文を編集します。

内部リンクには次の形式を使います。リンク先をサイト内のパスで指定すると、表示するページの深さに合わせた相対URLに変換します。

```liquid
[Programme]({% include local-url.html path='/programme/' %})
```

### 共通情報

`_data/conference.yml`の主な項目は次のとおりです。YAMLの字下げを保ち、日付の文字列は引用符で囲んでください。

| 項目 | 用途 |
| --- | --- |
| `name` | 正式な会議名 |
| `short_name`、`year` | 短い表記、開催年 |
| `dates_label` | 画面に表示する会期の文字列 |
| `start_date`、`end_date` | 開始日、最終日。ISO形式の文字列 |
| `city` | 都市・国の表示 |
| `venue.name`、`venue.address` | 会場名、住所 |
| `venue.website`、`venue.access_url` | 会場公式サイト、交通案内のURL |
| `contact_email` | 連絡先。空文字列ならサイドバーの連絡先欄を非表示 |
| `show_topics` | 研究分野の表示を`true`／`false`で切り替え |
| `last_updated` | サイトに表示する更新日 |
| `calendar_uid`、`calendar_updated_utc`、`calendar_end_exclusive` | カレンダー出力の管理情報 |

連絡先を設定したら、`participation.md`の「連絡先は後日掲載する」という本文も更新します。会議名や日程を変更した場合は、`_config.yml`の`title`・`description`、各ページの説明文、お知らせの文章も確認してください。

### お知らせ・プログラム・研究分野

`_data/announcements.yml`には次の形式で追記します。日付の新しい項目から表示されます。

```yaml
- date: "2027-01-15"
  title: "ここに実際のお知らせの見出し"
  text: "ここに確定したお知らせの本文"
```

これは書式例です。架空の日付や案内をそのまま公開しないでください。本文はプレーンテキストとして表示されます。

`_data/programme.yml`は`date`、`day`、`status`を持つ日付別の表です。時間別の詳細が決まったら、`programme.md`にMarkdownの表を追加できます。会議の時刻は日本時間であることを本文に記載すると分かりやすくなります。`_data/topics.yml`は`title`と`description`の組です。

## 4. 相対パスと素材フォルダーを設定する

通常のページでは、CSS、favicon、写真、カレンダー、メニューと本文の内部リンクを、表示ページからの相対パスで参照します。初期設定は次のとおりです。

```yaml
assets_path: "assets"
```

この場合、CSSへの参照はトップページで`./assets/css/main.css`、`/programme/`で`../assets/css/main.css`、2階層下のページで`../../assets/css/main.css`になります。ページと素材の相対的な位置関係を保てば、サイト全体を別のサブディレクトリに置いても通常ページの参照は追従します。

ディレクトリ型のページは`/programme/`のように末尾の`/`を付けるか、`/programme/index.html`で表示します。公開サーバーでも、`/programme`から`/programme/`へリダイレクトする通常のディレクトリ配信を利用してください。

`assets_path`は**生成されるサイトのルートから見た素材ディレクトリの相対パス**です。URLの参照先を指定する設定であり、実ファイルの移動・複製は行いません。素材フォルダーを`static/`に変更する場合は、ソースで次を実行します。

```sh
mv assets static
```

続けて`_config.yml`を変更し、再ビルドします。各テンプレートの修正は不要です。

```yaml
assets_path: "./static"
```

`static/`や`static/files`のような指定も使えます。`../shared/static`のようにサイトの外を参照する場合は、ビルド後の素材ファイルを、その相対位置に別途配置してください。特にカレンダーは、ソースのLiquid式を展開済みの生成ファイルを使います。

写真の`_data/photo.yml`では、`assets_path`内の相対名を指定します。素材フォルダーだけを改名する場合、この値は変更しません。

```yaml
path: images/acros-fukuoka-2011.jpg
```

新しい素材リンクには、例えば次のincludeを使えます。追加プラグインは不要です。

```liquid
![ACROS Fukuoka]({% include asset-url.html path='images/acros-fukuoka-2011.jpg' %})
```

通常ページのローカル参照に`baseurl`は使いません。一方、canonical・OGメタデータと404ページでは公開先の`url`・`baseurl`を使うため、これらは本番URLに合わせて設定します。`404.md`の`root_relative_urls: true`は、不明な深いURLで404ページが表示されたときもトップページや素材へ正しく戻れるようにする指定です。`_config.yml`を変更したら、実行中の`jekyll serve`を再起動してください。

## 5. カレンダーの日付を更新する

配布する`.ics`は終日の**暫定予定**です。4月26〜28日の3日間を表すため、終了日は1日後の**4月29日**に設定しています。

```yaml
start_date: "2027-04-26"
end_date: "2027-04-28"
calendar_end_exclusive: "2027-04-29"
```

会期を変えたら、表示用の`dates_label`と日程表もそろえて更新してください。`calendar_updated_utc`は更新日時をUTCの`YYYYMMDDTHHMMSSZ`形式で記録します。

`calendar_uid`は同じ予定を識別するための値です。公開前に所有ドメインなどを使った一意の値に変更して構いませんが、**配布後の更新では同じUIDを保ちます**。日程を正式確定に変更する場合は、`.ics`の`STATUS:TENTATIVE`を`STATUS:CONFIRMED`に直し、説明文も更新してください。会議名や会場を変更する場合は、`.ics`内の`SUMMARY`と`LOCATION`も編集します。カレンダーアプリへの再取込みの挙動はアプリによって異なります。

## 6. GitHub Pagesで公開する

同梱の`.github/workflows/pages.yml`が、JekyllのビルドとGitHub Pagesへの配置を行います。この配布物によってGitHubリポジトリが作成されることはありません。

1. 公開先のリポジトリを作成します。
2. プロジェクトの**中身**をリポジトリ直下に置きます。`_config.yml`が直下にあり、`.github/workflows/pages.yml`と`Gemfile.lock`も含まれている状態にします。
3. 既定ブランチを`main`にします。別の名前なら、ワークフローの`branches`を合わせます。
4. **Settings → Pages → Build and deployment → Source**で**GitHub Actions**を選択します。
5. `main`へのpush、または**Actions**タブの**Run workflow**で開始します。完了後、Pages設定に表示されるURLで確認します。

ワークフローはRuby 3.3と`Gemfile.lock`を使って`_site/`を生成します。`url`と`baseurl`はGitHub Pagesのメタデータから一時設定に書き出すため、ユーザーサイト、リポジトリ配下のサイト、GitHub Pages側で設定した独自ドメインに対応します。元の`_config.yml`は書き換えません。

組織の設定でActionsやPagesの使用が制限されている場合は、その管理設定に従ってください。手順の詳細は[GitHub公式のカスタムワークフロー案内](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages)を参照できます。

## 7. 既存の大学サーバー等で公開する

canonical・OGメタデータと404ページ用に、`_config.yml`に公開先を設定します。例えば`https://example.ac.jp/asian-sciml-2027/`なら次の値です。

```yaml
url: "https://example.ac.jp"
baseurl: "/asian-sciml-2027"
```

ドメインの直下に置く場合、`baseurl`は`""`です。`url`には末尾のスラッシュやパスを含めません。その後`bundle exec jekyll build`を実行し、`_site/`の**中身**を公開ディレクトリに転送してください。サーバー側にRubyは不要です。

ページと素材のディレクトリ構成を保って移動すれば、通常ページの相対リンクや素材参照は新しい配置先でも利用できます。本番の配置先を変更した場合は、メタデータと404ページの参照も一致するように`url`・`baseurl`を更新して再ビルドしてください。生成済みHTMLを直接書き換える必要はありません。

`noindex: true`は検索エンジン向けのインデックス抑制指定です。アクセス制限ではありません。通常の公開用初期設定は`false`です。`preview/`と`dist/`はJekyllの生成対象から除外しています。

## 8. 写真と参考資料

会場写真はKenta Mabuchi撮影の*ACROS Fukuoka 2011*です。**CC BY-SA 2.0**の条件で利用し、ページ内に撮影者・出典・ライセンスを表示しています。写真を残して公開する場合は、その表示とリンクも維持してください。詳細は[THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)にまとめています。

- [アクロス福岡公式サイト](https://www.acros.or.jp/english/)
- [公式アクセス案内](https://www.acros.or.jp/english/access/)
- [写真の出典：Wikimedia Commons](https://commons.wikimedia.org/wiki/File:ACROS_Fukuoka_2011.jpg)
- [写真のライセンス：CC BY-SA 2.0](https://creativecommons.org/licenses/by-sa/2.0/)
- [Jekyll公式ドキュメント](https://jekyllrb.com/docs/)
- [GitHub Pagesのカスタムワークフロー](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages)

表示にはシステム標準フォントを用い、外部フォントやJavaScriptに依存しません。スマートフォンでの表示と印刷用のスタイルも用意しています。
