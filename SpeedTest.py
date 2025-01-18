from speedtest import Speedtest
wifi = Speedtest()
print("Getting Download Speed....")
download = wifi.download()
print(f"download: {download / 1024 / 1024:.2f} mbps")
print("Getting Upload Speed....")
upload = wifi.upload()
print(f"upload: {upload / 1024 / 1024:.2f} mbps")