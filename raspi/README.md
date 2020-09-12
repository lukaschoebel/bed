# RASPBERRY

## Useful Commands

Some useful commands to control the raspi by `ssh`'ing into a static IP.

```bash
# Transfer file
scp pi@<IP-ADRESS>:<PATH/TO/FILE> <FILE/DEST>

# Recursively transfer folder to raspi
scp -r pi@<IP-ADRESS>:<PATH/TO/FOLDER> <FOLDER/DEST>
```
