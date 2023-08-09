sudo socat PTY,link=/dev/ttyV0,raw,echo=0,crnl PTY,link=/dev/ttyS0,raw,echo=0 &
sudo socat PTY,link=/dev/ttyS0,raw,echo=0 PTY,link=/dev/ttyV0,raw,echo=0 &
