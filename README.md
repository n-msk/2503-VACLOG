# vaccum log インストール手順

##1. Windowsの場合はWSL（Windows Subsystem for Linux）をインストールして以下の手順をふむか，対応する手順を何かしらで行う．
WSLをインストールする場合、[公式ガイド](https://learn.microsoft.com/ja-jp/windows/wsl/install)を参照


## 1. Gitのインストール
```sh
sudo apt update
sudo apt install git
```

## 2. Git LFSのインストール
```sh
sudo apt install git-lfs
git lfs install
```

あるいは[Git LFS](https://git-lfs.github.com/)


## 4. リポジトリのクローン
デフォルトではGit LFSの大容量ファイルをダウンロードせずにクローン

```sh
GIT_LFS_SKIP_SMUDGE=1 git clone https://github.com/2503-VACLOG/vaccum.git
```
この方法ではLFS管理ファイルはプレースホルダのみ取得し容量や通信量の節約

LFSファイル本体が必要な場合、クローン後に以下を実行

```sh
cd vaccum
git lfs pull
```

## 5. 環境構築
プロジェクトディレクトリで以下を実行し、環境をセットアップ

```sh
bash env_start.sh
```

## 6. 設定ファイルの編集
必要に応じて `vaccum/src/configs` 内の設定ファイルを編集．特に`EXPERIMENT`, `CHECKPOINT`はユニークな名称に設定．

## 7. プログラムの実行
`vaccum` ディレクトリで以下を実行

```sh
python -m src
```
