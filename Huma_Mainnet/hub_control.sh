#!/bin/bash
while true; do
    clear
    echo -e "\033[1;36m####################################################"
    echo -e "#     TUNAPAC HUMANLEDGER HUB: CONTROL CENTER      #"
    echo -e "#     MAINNET STATUS: MARCH 27, 2026               #"
    echo -e "####################################################\033[0m"
    echo -e "1) [START] Launch 3s Block Network (Background)"
    echo -e "2) [VIEW]  Monitor Live HUM- Protocol Feed"
    echo -e "3) [STOP]  Emergency Kill Switch (Offline)"
    echo -e "4) [EXIT]  Close Control Center"
    echo -e "----------------------------------------------------"
    read -p "ARCHITECT COMMAND [1-4]: " choice

    case $choice in
        1)
            nohup python3 huma_auto.py > /dev/null 2>&1 &
            echo -e "\033[1;32m[SUCCESS] HUMANLEDGER MAINNET IS LIVE.\033[0m"
            sleep 2
            ;;
        2)
            echo -e "\033[1;33m[MONITOR] PRESS CTRL+C TO RETURN TO MENU\033[0m"
            tail -f mainnet_live.log
            ;;
        3)
            pkill -f huma_auto.py
            echo -e "\033[1;31m[OFFLINE] NETWORK SUSPENDED.\033[0m"
            sleep 2
            ;;
        4)
            exit
            ;;
        *)
            echo "INVALID COMMAND."
            sleep 1
            ;;
    esac
done
