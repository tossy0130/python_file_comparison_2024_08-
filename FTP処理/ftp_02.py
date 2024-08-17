from ftplib import FTP

# FTPサーバーの情報
ftp_server = "192.168.254.204"  # FTPサーバーのアドレス
ftp_user = "root"           # FTPユーザー名
ftp_password = "password"       # FTPパスワード
remote_file_path = "/path/to/remote/file.txt"  # リモートファイルのパス
local_file_path = "/path/to/local/file.txt"    # ダウンロードするローカルファイルのパス


def download_file():
    # FTPサーバーに接続
    ftp = FTP(ftp_server)
    ftp.login(user=ftp_user, passwd=ftp_password)

    # ファイルをバイナリモードでダウンロード
    with open(local_file_path, 'wb') as local_file:
        ftp.retrbinary(f'RETR {remote_file_path}', local_file.write)

    # 接続を閉じる
    ftp.quit()
    print(f"ファイルが {local_file_path} にダウンロードされました")


if __name__ == "__main__":
    download_file()
