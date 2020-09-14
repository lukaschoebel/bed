# RASPBERRY

## Useful Commands

Some useful commands to control the raspi by `ssh`'ing into a static IP.

```bash
# Transfer file
scp pi@<IP-ADRESS>:<PATH/TO/FILE> <FILE/DEST>

# Recursively transfer folder to raspi
scp -r pi@<IP-ADRESS>:<PATH/TO/FOLDER> <FOLDER/DEST>
```

## Launch script

```bash
# make it executable
chmod 755 launch.sh

# make log directory
mkdir /home/logs

# crontab
sudo crontab -e
@reboot sh /home/pi/bed/raspi/launch.sh >/home/pi/logs/cronlog 2>&1
sudo reboot now

# reboot and check if it worked, otherwise check logs
cd logs && cat cronlog
```

Other methods for starting a Python script at start can be found [here](https://www.dexterindustries.com/howto/run-a-program-on-your-raspberry-pi-at-startup/).
