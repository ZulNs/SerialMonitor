U
    w�y`�I  �                   @   sH  d Z ddlZddlmZ ddlmZ ddlmZ ddlZddl	m
  mZ ddlZddlZdd� Zdd	� Zd
d� Zdd� Zdd� Zdd� Zdd� Zdd� Zdd� Zdd� Zdd� Zdd� Zdd� Zd�d d!�Zd"d#� Zd$d%� Zd&d'� Zd(d)� Zd*d+� Z d,d-� Z!d.d/� Z"d0d1� Z#d2d3� Z$d4d5� Z%d6d7� Z&e'd8k�rDd9Z(d:Z)ej*ej+ej,ej-fZ.ej/ej0ej1ej2ej3fZ4d;Z5ej6ej7ej8fZ9d<d=� e�:� D �a;ej<dd>ddd?�Z=d@a>g a?da@dAaAdBaBdZCi ZDeE�FdCdD�d ZGdZHzeIeGdE �ZHe�JeH�ZDW n$ eKk
�r ZL zW 5 dZL[LX Y nX eH�reH�M�  e�N� ZOeO�Pe(� zejQeGdF dG�ZCW n   Y nX eC�r^eO�RdHeC� eO�SdIe"� e�T� ZUe�T� ZVe�T� ZWe�T� ZXejYjZeOddDdJ� ejYjZeOdDdKdJ� ejYjZeOdBdDdJ� ejYj[eOddDdJ� ejYj[eOdDdDdJ� ejYj[eOdBdDdJ� ejYj[eOdLdKdJ� ejYj[eOdMdDdJ� ejYj[eOdNdDdJ� ejYj[eOdOdDdJ� e�\eO�Z]e]j^dddOdMdPej_ej` dQ� e]�adRe� e]�adSe� e]�adTe� ejbeOdUdVejcdWdX� dY�Zdedj^ddOdMdMejedZ� ejfeOd[ejcd\ejgd]�Zhehj^dDdd^dMejid_� eh�adTe� ejjeOd`eUdAdHda�Zkekj^dBddMdMejldZ� eD�mdb�Znendk�r<eU�oen� ejjeOdceVdAdHda�Zpepj^dBdDdMdMejldZ� eD�mdd�Znendk�r�eV�oen� ejjeOdeeWdAdHda�Zqeqj^dBdBdMdMejldZ� eD�mdf�Znendk�r�eW�oen� ejreOdgdh�Zsesj^dBdLdMdMejtdZ� es�adie� eut;�esdj< evt;�dk�r*dkesdl< es�odm� nejcesdl< es�odn� ejreOdodkdp�Zwewj^dBdMdMdMejtdZ� dqewdj< eD�mdr�Znendk�r�ew�xen� n
ew�xd� ejreOdUdkdp�Zyeyj^dBdNdMdMejtdZ� ezdsdt� e)D ��eydj< ey�adie� eD�mdu�Znendk�rey�xen� e)en e=_{ney�xdM� e)dM e=_{ejbeOdUdvedw�Z|e|j^dBdOdMdMejtdZ� ej}e]ddx�Z~e~jdydzd{dX� d|� e~jd}d~ddX� d|� e~jd�d�d�dX� d|� ej}ehddx�Z�e�jd}d~d�dX� d|� e����  e�jd�e d�� e����  e�j�d�dAdHeXd�� e����  e�jd�e#d�� e����  e�jd�e!d�� e�  eO���  eO��� Z�eO��� Z�eO��� Z�eO��� Z�eO��e�d�� eO��e�� d�e�� d�e�e�e� dB �� d�e�e�e� dB �d� � �� d�Z�ee�dB� eD�md��Znendk�r�eX�oen� eD�md��Znendk�r�ene=_�eD�md��Znendk�r�ene=_�eD�md��Znendk�r�ene=_�eD�md��Znendk�r<end�k�r<eD�md��t;k�r<es�xen� ed� eO���  dS )�z=
Serial Monitor

Designed by ZulNs @Gorontalo, 13 April 2021
�    N)�ttk)�scrolledtext)�
messageboxc                 C   sb   t | �}d|kr|dks d|kr4|dkr,dS t|�S |dkr@dS |dkrLd	S |d
krXdS d�|�S )N�    �~   �   �\   z\\�	   �	�
   �
�   z\rz\x{:02x})�ord�chr�format)�chr_in_byte�cd� r   �serial_monitor.pyw�get_str_of_chr   s    r   c                 C   s0   t | �}d�|�}|dkr$|d7 }n|d7 }|S )Nz{:02X}r   r   � )r   r   )r   r   �str   r   r   �get_hexstr_of_chr   s    

r   c                 C   s0   d| kr| dkp.d| kr | dkp.d| ko.| dkS )N�   0�   9�   A�   F�   a�   fr   �Za_byter   r   r   �is_hex_digit(   s    r    c                 C   s   d| ko| dkS )Nr   �   7r   r   r   r   r   �is_oct_digit+   s    r"   c           
      C   s�  t dd� | D ��}d}d }d}|t|�k �r�|||d � }|dk�r�|d7 }|||d � }|dksv|dksv|dkr�||7 }�q�|d	kr�t||d |d
 � �s�|d7 }�q�|dkr�|d7 }�q�|dkr�|d7 }�q�|dkr�|d7 }�q�|dkr�|d7 }�q�|dk�r|d7 }�q�|dk�r*|d7 }�q�|dk�r@|d7 }�q�|dk�r�t||d |d
 � ��r�t||d
 |d � ��r�|t t||d |d � d�g�7 }|d7 }q|d |d d| |d |d � � d|d � �d�}�q�n�t|��r�d}t||d |d
 � ��r8|d7 }t||d
 |d � ��r8|d7 }t|||| � d �}|d!k�rh|d8 }|dL }|t |g�7 }||7 }qnH|�r�tt|��}|d }	nd"}|}	|d |	d#|� d$|d � �d�}�q�n||7 }|d7 }q||fS )%Nc                 S   s   g | ]}t |��qS r   )r   )�.0�cr   r   r   �
<listcomp>/   s     zdecode_esc.<locals>.<listcomp>�    r   �   �   \�   '�   "r   �   �    r   �   �   b�   �   t�   	�   n�   
�   v�   r   �   �   r�   �   x�   �   zValue Error: invalid z escape at position )�from�to�msg�   ��   � z(Syntax Error: invalid escape sequence '\z' at position )�bytes�lenr"   r    �intr   r   )
Z
str_of_chrZsbsZdbs�err�idxZbyZodZov�chr=   r   r   r   �
decode_esc.   st    
 



$4


 
rH   c                 C   sX  t t�� �}tt�}|dkr"t�  |dk�rTt|�\}}|r�t|d d d� t�|d � t�	|d |d � t�
|d � d S |dkr�t|d	  |ks�|dkr�t�|� tt�at�� d	kr�|d
7 }n*t�� dkr�|d7 }nt�� dkr�|d7 }t�|� t�� �rFt�� �r(d�dd� |D ��}nd�dd� |D ��}t|d	� t�dtj� d S )Nz{about}rA   r>   r   r+   r<   r=   r   r'   r3   r8   r:   s   
c                 S   s   g | ]}t t|g���qS r   )r   rB   �r#   �ir   r   r   r%   �   s     zsendCmd.<locals>.<listcomp>c                 S   s   g | ]}t t|g���qS r   )r   rB   rI   r   r   r   r%   �   s     )�str�txText�getrC   �	sentTexts�	showAboutrH   �writeConsoleZxviewZselection_rangeZicursor�append�sentTextsPtr�lineEndingCbo�current�currentPort�write�showSentTextVar�
dispHexVar�join�delete�tk�END)�event�txtZlstZbsrE   r   r   r   �sendCmdm   s8    
 






r_   c                 C   sL   t tt�krtt�� �at dkrHt d8 a t�dtj	� t�
tj	tt  � d S )Nr   r'   )rR   rC   rN   rK   rL   rM   �
lastTxTextrZ   r[   r\   �insert�r]   r   r   r   �upKeyCmd�   s    rc   c                 C   sT   t tt�k rPt d7 a t�dtj� t tt�kr>t�tjt� nt�tjtt  � d S )Nr'   r   )	rR   rC   rN   rL   rZ   r[   r\   ra   r`   rb   r   r   r   �
downKeyCmd�   s    rd   c                 C   s�   t �� tjkrd S t�  tjr4t��  ttd d� t �� t_t	tj atdt d d� t
��  zt��  W n0   t
�t� t �d� tdd� d t_Y nX tjr�t
�td t	tj  � t�  t�  tdd� d S )	N�	 closed.
r+   zOpening z...�Select portz
failed!!!
z: zdone.
)�portCborM   rU   �port�disableSending�is_open�closerP   �portDesc�ports�root�update�open�title�	APP_TITLE�set�enableSending�	rxPollingrb   r   r   r   �
changePort�   s,    




rv   c                 C   s   t t��  t_d S �N)�
BAUD_RATES�baudrateCborT   rU   �baudraterb   r   r   r   �changeBaudrate�   s    r{   c                   C   s6   t jtjd� t �dtj� t jtjd� dadad S )N��statez1.0Tr+   )	�rxText�	configurer[   �NORMALrZ   r\   �DISABLED�	isEndByNL�lastUpdatedByr   r   r   r   �clearOutputCmd�   s
    r�   c                 C   s�   t �� rtj}ntj}td�D ]}tj||d� qzt�	�  tjdtjd� W n   tjdtjd� Y nX zt�| j| j� W 5 t�
�  X d S )Nr+   r|   )rL   Zselection_presentr[   r�   r�   �range�
txTextMenu�entryconfigurern   Zclipboard_get�grab_release�tk_popup�x_root�y_root)r]   ZstarJ   r   r   r   �showTxTextMenu�   s    r�   c                 C   s�   t t�tj��r"tjdtjd� ntjdtjd� t	�
� rLtjdtjd� ntjdtjd� zt�| j| j� W 5 t��  X d S )Nr   r|   r+   )rC   r~   Z
tag_rangesr[   ZSEL�
rxTextMenur�   r�   r�   rU   ZisOpenr�   r�   r�   r�   rb   r   r   r   �showRxTextMenu�   s    r�   c                 C   s�  d}d}|dkrBt �� rBt�d�tt�� ��d�d d d� ��}|s�tsNtsRtr�t	�� rpt �� rp|d| 7 }n"t	�� r�|d7 }nt �� r�||7 }|r�|d	7 }ts�d
| }nt|dkr�tdkr�ts�tdkr�t �� r�d| }nd}|d	7 }ts�d
| }n,|dk�rtdk�r d
}t�s |d
7 }nd S |dk�r<tdk�r<d
| }|| 7 }t
jtjd� t
�tj|� t�� �st|dk�r�t
�tj� t
jtjd� | d d
k�r�danda|ad S )NrA   r+   �%H:%M:%S.{}�.r'   r:   ZRX_ZRXz >> r   ZTX_ZTXr|   �����TF)�showTimestampVarrM   �time�strftimer   �repr�splitr�   r�   rW   r~   r   r[   r�   ra   r\   �autoscrollVarZseer�   )r^   Zupd�tmZadr   r   r   rP   �   sT    *






rP   c               
   C   s�   t js
d S t�� } z�t jdkr�t�� |  dk r�t �� }t�d�tt�� ��	d�d d d� ��}d}t
�� rz|t|�7 }n|t|�7 }t|� qW n< tjk
r� } zt�  t�td�t�� W 5 d }~X Y nX t�d	t� d S )
Nr   逄 r�   r�   r'   r:   rA   zCouldn't access the {} portr   )rU   rj   r�   �perf_counter_nsZ
in_waiting�readr�   r   r�   r�   rX   rM   r   r   rP   �serialZSerialException�	closePort�msgboxZ	showerrorrr   rl   rn   �afterru   )ZpresetrG   r�   r^   Zser   r   r   ru     s     *$ru   c                  C   s�   dd� t �� D �} t| �}|td kr~|td< tt�dkrTdtd< t�d� t�  n&t|�dkrztj	td< t�d� t
�  | at�d	t� d S )
Nc                 S   s   i | ]}|j |j�qS r   ��nameZdescription�r#   �pr   r   r   �
<dictcomp>*  s      z$listPortsPolling.<locals>.<dictcomp>�valuesr   �readonlyr}   rf   �No porti�  )�
list_ports�comports�sortedrg   rC   rm   rs   rt   r[   r�   ri   rn   r�   �listPortsPolling)ZpsZpnr   r   r   r�   (  s    


r�   c                   C   s   t jtd< t�d� d S �Nr}   �<Return>)r[   r�   �sendBtnrL   Zunbindr   r   r   r   ri   9  s    
ri   c                   C   s   t jtd< t�dt� d S r�   )r[   r�   r�   rL   �bindr_   r   r   r   r   rt   =  s    
rt   c                   C   s@   t jr<t ��  ttd d� d t _t�  t�d� t	�
t� d S )Nre   r+   rf   )rU   rj   rk   rP   rl   rh   ri   rg   rs   rn   rq   rr   r   r   r   r   r�   A  s    
r�   c                   C   s   t �td� d S )Nz+Designed by ZulNs
@Gorontalo, 13 April 2021)r�   Zshowinforr   r   r   r   r   rO   J  s    rO   c               	   C   s�   i } t �� | d< t�� | d< t�� | d< t�� | d< t�� | d< t�� | d< tj	| d< tj
| d< tj| d	< t�� | d
< t| d< ttd d��}tj| |dd� |��  W 5 Q R X t��  d S )N�
autoscroll�showtimestamp�showsenttext�
displayhex�
lineending�baudrateindex�databits�parity�stopbits�	portindex�portlist�.json�w�   )�indent)r�   rM   r�   rW   rX   rS   rT   ry   rU   �bytesizer�   r�   rg   rm   rp   �fname�json�dumprk   rn   �destroy)�data�jfiler   r   r   �exitRootM  s     


r�   c                  C   s  t �� at�d� tr"t�dt� t jjtddd� t jjtddd� t jjtddd� t jjtddd� t jjtddd� t jjtddd� t jjtddd� t j	tdd	�j
dddd
t jd� t j	tdd	�j
ddddt jt j d� t j	tdd	�j
dddd
t jd� tjtddd�atj
ddd
d
t jd� ttd< t�tj� tjtddd�atj
ddd
dt jt j d� ttd< t�t�tj�� tjtddd�atj
ddd
d
t jd� ttd< t�tj� t jtddtd�j
ddd
dt jt j  d� t jtdddd� d�j
dddd
t j!d� t jtdddd� d�} | j
ddd
d
t j!d� t�"dt#� t�"dt$� t�%�  t&�'� }t&�(� }t&�)� }t&�*� }t�'� }t�(� }t�+|� d|� d|t,|| d � � d|t,|| d � � �� t�-||� t�.||� t�/dd� t�0�  | �1�  d S )NzPort SettingFr   r'   �Zweightr+   r:   z
Data bits:)�text�   ��row�column�padx�pady�stickyzParity:z
Stop bits:r   r�   ��widthr}   r�   ZDefault)r�   r�   �commandZOKc                   S   s   t d �S rw   )�setPortr   r   r   r   �<lambda>}  r&   zsetting.<locals>.<lambda>ZCancelc                   S   s   t d �S rw   )�hideSettingr   r   r   r   r�     r&   r�   z<Escape>�x�+)2r[   ZToplevel�
settingDlgrq   �ico�	iconphoto�Grid�rowconfigure�columnconfigureZLabel�grid�NEZNS�Er   �Combobox�dataBitsCbo�DATABITSrs   rU   r�   �	parityCbo�
PARITY_VALrT   �PARITY�indexr�   �stopBitsCbo�STOPBITSr�   �Button�defaultSetting�W�Sr�   r�   r�   ro   rn   �winfo_width�winfo_heightZwinfo_rootxZwinfo_rooty�geometryrD   �minsize�maxsizeZ	resizableZgrab_setZ	focus_set)Z	cancelBtn�rw�rhZrxZryZdwZdhr   r   r   �setting_  sr    
 &     
�    �@r�   c                   C   s.   t �tj� t�t�tj�� t	�tj
� d S rw   )r�   rs   r�   �	EIGHTBITSr�   rT   r�   r�   �PARITY_NONEr�   �STOPBITS_ONEr   r   r   r   r�   �  s    r�   c                 C   s6   t t��  t_tt��  t_tt	��  t_
t��  d S rw   )r�   r�   rT   rU   r�   r�   r�   r�   r�   r�   r�   r�   r�   rb   r   r   r   r�   �  s    r�   c                 C   s   t ��  d S rw   )r�   r�   rb   r   r   r   r�   �  s    r�   �__main__zSerial Monitor)i,  i�  i`	  i�  �%  i K  i �  i �  i , i � i Z  i � i@B r�   )ZEvenZOdd�NoneZMarkZSpacec                 C   s   i | ]}|j |j�qS r   r�   r�   r   r   r   r�   �  s      r�   r�   )rh   rz   ZtimeoutZwrite_timeoutrA   Tr+   r�   r'   r�   z.png)�fileFZWM_DELETE_WINDOWr�   i�  r:   r�   �   �   r?   )r�   r�   �
columnspanr�   r�   r�   z<Up>z<Down>z
<Button-3>r�   ZSendc                   C   s   t d �S rw   )r_   r   r   r   r   r�   �  r&   r�   )r�   r�   r}   r�   r�   �   )ZCourierr   )Zheightr}   ZfontZwrap�   )r�   r�   r�   r�   r�   Z
Autoscroll)r�   �variable�onvalue�offvaluer�   zShow timestampr�   zShow sent textr�   r   )r�   z<<ComboboxSelected>>r�   r�   r}   rf   r�   �   r�   )zNo line endingZNewlinezCarriage returnzBoth CR & NLr�   c                 c   s   | ]}t |�d  V  qdS )z baudN)rK   )r#   �br   r   r   �	<genexpr>
  s     r  r�   zClear output)r�   r�   r�   )ZtearoffZCutzCtrl+Xc                   C   s
   t �d�S )Nz<<Cut>>�rL   �event_generater   r   r   r   r�     r&   )�labelZacceleratorr�   ZCopyzCtrl+Cc                   C   s
   t �d�S �Nz<<Copy>>r  r   r   r   r   r�     r&   ZPastezCtrl+Vc                   C   s
   t �d�S )Nz	<<Paste>>r  r   r   r   r   r�     r&   c                   C   s
   t �d�S r  )r~   r	  r   r   r   r   r�     r&   zClose active port)r
  r�   zDisplay in hexadecimal code)r
  r  r  r  zPort settingZAbout��   r�   r�   �   a�  
************************************************************************************
* Welcome to Python GUI Serial Monitor as an alternative to Arduino Serial Monitor *
*                                                                                  *
* Use up and down arrow keys to select previously-entered text from history list.  *
* Right click on output console for additional menus.                              *
*                                                                                  *
* Designed by ZulNs @Gorontalo, 13 April 2021                                      *
************************************************************************************

r�   r�   r�   r�   r�   r�   r�   )r   )��__doc__Ztkinterr[   r   r   Ztkscrollr   r�   r�   Zserial.tools.list_portsZtoolsr�   r�   r�   r   r   r    r"   rH   r_   rc   rd   rv   r{   r�   r�   r�   rP   ru   r�   ri   rt   r�   rO   r�   r�   r�   r�   r�   �__name__rr   rx   ZFIVEBITSZSIXBITSZ	SEVENBITSr�   r�   ZPARITY_EVENZ
PARITY_ODDr�   ZPARITY_MARKZPARITY_SPACEr�   r�   r�   ZSTOPBITS_ONE_POINT_FIVEZSTOPBITS_TWOr�   r�   rm   ZSerialrU   rl   rN   rR   r�   r�   r�   r�   �__file__�rsplitr�   r�   rp   �load�FileNotFoundErrorZfnferk   ZTkrn   rq   Z
PhotoImager�   ZprotocolZ
BooleanVarr�   r�   rW   rX   r�   r�   r�   ZEntryrL   r�   �NZEWr�   r�   r�   r�   r�   ZScrolledTextZWORDr~   ZNSEWZCheckbuttonZautoscrollCbtZSWrM   Zdirs   ZshowTimestampCbtZshowSentTextCbtr�   rg   ZSEr�   rC   rS   rT   ry   �listrz   ZclearBtnZMenur�   Zadd_commandr�   Zadd_separatorZadd_checkbuttonro   Zwinfo_screenwidth�swZwinfo_screenheightZshr�   r�   r�   r�   r�   r�   rD   Zwtxr�   r�   r�   Zmainloopr   r   r   r   �<module>   s`  	? 	

0	2





















<�










$
