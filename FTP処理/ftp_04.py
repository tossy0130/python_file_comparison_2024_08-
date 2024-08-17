import os
import stat
import paramiko
import traceback

# SFTPサーバ情報
sftp_host = "192.168.254.204"
sftp_port = 22
sftp_user = "root"
sftp_password = "password"

# remote_file_path = "/home/tossy/sample.txt"  # リモートファイル パス
# local_file_path = "C:/Users/natsume/Desktop/file.txt"  # ローカルファイル パス

# ========= /data/

# ========= /html/
# css
remote_dir_path_css = "/home/jim/SaijoMEB/html/css/pc/"  # リモート /css/pc/
local_dir_path_css = "C:/Users/natsume/Desktop/SaijoMEB/html/css/pc/"  # ローカル /css/pc/

# js
remote_dir_path_js = "/home/jim/SaijoMEB/html/js/pc/"  # リモート /js/pc/
local_dir_path_js = "C:/Users/natsume/Desktop/SaijoMEB/html/js/pc/"  # ローカル /js/pc/

# .php
remote_dir_path_html = "/home/jim/SaijoMEB/html/"  # リモート /html/
local_dir_path_html = "C:/Users/natsume/Desktop/SaijoMEB/html/"  # ローカル /html/


def is_dir(mode):
    # 0o40000 => ディレクトリを示すビットマスク
    return mode & 0o40000 == 0o40000


def download_dir(sftp, remote_dir, local_dir):

    os.makedirs(local_dir, exist_ok=True)

    # ローカルディレクトリ　以下作成
    for item in sftp.listdir_attr(remote_dir):
        remote_path = os.path.join(remote_dir, item.filename)  # パスを作成

        try:
            # バイト列としてファイル名を取得し、適切なエンコーディングでデコードする
            if isinstance(item.filename, bytes):
                local_filename = item.filename.decode('latin1')
            else:
                local_filename = item.filename

            local_path = os.path.join(local_dir, local_filename)

            # フォルダの場合
            if is_dir(item.st_mode):
                download_dir(sftp, remote_path, local_path)
            else:
                sftp.get(remote_path, local_path)
                print(f"ファイルが {local_path} にダウンロードされました")

        except UnicodeDecodeError as e:
            print(f"UnicodeDecodeError: {e}")
            print("ファイル名のデコードに失敗しました。スキップします。")
        except Exception as e:
            print(f"エラーが発生しました: {e}")
            print(traceback.format_exc())


def download_files_from_server():
    # SSH クライアント作成
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())


def download_files_from_server():
    # SSHクライアントを作成
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # SFTPサーバーに接続
        ssh.connect(sftp_host, port=sftp_port,
                    username=sftp_user, password=sftp_password)
        print("SSH接続に成功しました")

        # SFTPセッションを開く
        sftp = ssh.open_sftp()
        print("SFTPセッションが開かれました")

        # ディレクトリのダウンロード
        download_dir(sftp, remote_dir_path_css, local_dir_path_css)  # css
        download_dir(sftp, remote_dir_path_css, local_dir_path_js)  # js
        download_dir(sftp, remote_dir_path_html,
                     local_dir_path_html)  # /html/  .php

    except paramiko.AuthenticationException:
        print("認証エラーが発生しました。ユーザー名やパスワードを確認してください。")
    except paramiko.SSHException as ssh_error:
        print(f"SSH接続に関するエラーが発生しました: {ssh_error}")
    except Exception as e:
        print("エラーが発生しました:")
        print(traceback.format_exc())  # エラーの詳細なスタックトレースを表示
    finally:
        # 接続を閉じる
        if 'sftp' in locals():
            sftp.close()
        if 'ssh' in locals():
            ssh.close()


if __name__ == "__main__":
    download_files_from_server()
