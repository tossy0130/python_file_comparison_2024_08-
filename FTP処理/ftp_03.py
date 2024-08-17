import paramiko

# SFTPサーバ情報
sftp_host = "192.168.254.204"
sftp_port = 22
sftp_user = "root"
sftp_password = "password"

remote_file_path = "/home/tossy/sample.txt"  # リモートファイルのパス
local_file_path = "C:/Users/natsume/Desktop/file.txt"  # ダウンロードするローカルファイルのパス


def download_file():
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

        # ファイルをダウンロード
        sftp.get(remote_file_path, local_file_path)
        print(f"ファイルが {local_file_path} にダウンロードされました")

    except paramiko.AuthenticationException:
        print("認証エラーが発生しました。ユーザー名やパスワードを確認してください。")
    except paramiko.SSHException as ssh_error:
        print(f"SSH接続に関するエラーが発生しました: {ssh_error}")
    except Exception as e:
        print(f"エラーが発生しました: {e}")
    finally:
        # 接続を閉じる
        if 'sftp' in locals():
            sftp.close()
        if 'ssh' in locals():
            ssh.close()


if __name__ == "__main__":
    download_file()
