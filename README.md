# conundrum

BlackMagic HyperDeck manual:
http://documents.blackmagicdesign.com/HyperDeck/HyperDeck_Manual_September_2014.pdf

the script currently sleeps for 10 seconds and then sends the command 'play: loop: true' as a TCP message to the HyperDeck.

it runs as a systemd service on boot:
http://www.diegoacuna.me/how-to-run-a-script-as-a-service-in-raspberry-pi-raspbian-jessie/
