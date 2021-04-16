# Python GUI Serial Monitor
### As an alternative to Arduino Serial Monitor, a GUI built with [*tkinter*](https://docs.python.org/3/library/tkinter.html).

## Dependencies
- [Python 3.8.6](https://www.python.org/downloads/release/python-386/)
- [pyserial v3.5](https://github.com/pyserial/pyserial)

## How to install pyserial
`python -m pip install pyserial`

## How to launch
`python serial_monitor.pyw`

## Key features
- Supports interactive display for both received and transmitted characters as well as show timestamp.
- Supports use of 8-bits escape sequence for both `\xXX` (hexadecimal `\x00` to `\xff`) and `\OOO` (octal `\000` to `\377`) to send to. Escape characters `\\`&nbsp;(backslash), `\'`&nbsp;(single quote), `\"`&nbsp;(double&nbsp;quote), `\0`&nbsp;(null), `\a`&nbsp;(bell), `\b`&nbsp;(backspace), `\t`&nbsp;(tab), `\n`&nbsp;(newline), `\v`&nbsp;(vertical tab), `\f`&nbsp;(form&nbsp;feed), and `\r`&nbsp;(carriage&nbsp;return) also supported. It also reports error on parsing with highlighted text.
- Maintains a history of texts you have sent. By using the up and down arrow keys, you can recall previously-entered texts from history list to the entry text line to send to.
- Supports display in hexadecimal code.
- Realtime port scanning and error reporting.
- A port can be selected from the list on the fly.
- All settings are maintained when closed, include current active port.

## Demo with pictures

&nbsp;

![pic1.png](./images/pic1.png)

***Fig. 1.*** *Serial Monitor in action.*

&nbsp;

![pic2.png](./images/pic2.png)

***Fig. 2.*** *Entry console right click floating menus.*

&nbsp;

![pic3.png](./images/pic3.png)

***Fig. 3.*** *Output console right click floating menus.*

&nbsp;

![pic4.png](./images/pic4.png)

***Fig. 4.*** *Port setting child window.*

&nbsp;

![pic5.png](./images/pic5.png)

***Fig. 5.*** *Error while parsing escape sequence character.*

&nbsp;

![pic6.png](./images/pic6.png)

***Fig. 6.*** *Error message box popup when the current active serial port detached.*
