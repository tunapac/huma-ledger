#!/bin/bash
# Path to your phone's internal Downloads folder
PHONE_STORAGE="/sdcard/Download"

echo -e "\033[1;33m[BACKUP] EXPORTING HUMANLEDGER HUB TO DEVICE STORAGE...\033[0m"

# Copying the core files
cp ~/Huma_Mainnet/huma.sh $PHONE_STORAGE/huma_backup.txt
cp ~/Huma_Mainnet/huma_telecom.py $PHONE_STORAGE/huma_telecom_backup.txt

echo -e "\033[1;32m[SUCCESS] GENESIS FILES SAVED TO: /Internal Storage/Download/\033[0m"
echo -e "[STATUS] IDENTITY tunapac4real247 IS NOW SECURE."
