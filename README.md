# Smart Bulk Phone Lookup

## Description:
Checks combinations for a given phone number which can potentially be used for vishing by resembling as the actual toll free number of large & respected institutions.
  
## Requirements:
  The code requires Python 3.x+ version installed in the system.
  
  Apart from that, the code utilises `requests`, `beautifulsoup4` & `prettytable` packages.

## Usage:
  Clone the repo using the following command and install the dependencies.
  ```bash
  $> git clone https://github.com/justan00b91/SBPL.git
  $> cd SBPL
  $> pip install -r requirements.txt
  $> python3 sbpl.py
  ```

## Working
  Initially the program converts the 11 digits toll free number into various combinations of 10 digit general phone numbers
  ```bash
  Example:
    1800-127-7892 -> 800-127-7892   [valid]
    1800-127-7892 -> 180-012-7789   [invalid]
  ```

  Then the program generates combinations of similar looking numbers in both fast (default) and exhaustive manner.
  
  This cobination defination is given by [ISMP](https://www.ismp.org/) and can be seen [here](https://www.ismp.org/sites/default/files/inline-images/20140605Table1.JPG)
  ```bash
  Example:
    0 -> 8
    3 -> 9
    3 -> 8
    4 -> 9
    5 -> 8
    5 -> 3
    6 -> 8
    7 -> 1
  ```

  Finally this entensive list is checked to see if the individual number exist or not.
  
## Output
  ```bash
  dumbermore@hogwarts:~/work/project/SBPL$ python3 sbpl.py 
  Enter a number: 18001277892       
  +----+------------+---------------------------------------+--------------------+------------------+-------------------+-----------------+----------------------------------------+--------------+
  | No |   Number   |                SIM card               |       State        |       IMEI       |      MAC addr     |     IP addr     |           Physical location            | Tracking No. |
  +----+------------+---------------------------------------+--------------------+------------------+-------------------+-----------------+----------------------------------------+--------------+
  | 0  | 1800127789 |                   -                   |         -          |        -         |         -         |        -        |                   -                    |      -       |
  | 1  | 8001277892 | Vodafone Idea (Vodafone Idea Limited) |    West Bengal     | 493861052873519  | 5e:8a:85:5e:57:2e |   63.169.75.82  |       Kulti, West Bengal, India        |  460B757730  |
  | 2  | 8001271892 | Vodafone Idea (Vodafone Idea Limited) |    West Bengal     | 5032763827415010 | 04:1a:0c:ed:ef:13 | 251.132.122.247 |     Darjeeling, West Bengal, India     |  9C104B9E43  |
  | 3  | 8001217892 | Vodafone Idea (Vodafone Idea Limited) |    West Bengal     | 011768032361999  | 21:b5:8a:c4:81:53 |  230.160.166.87 |      Farakka, West Bengal, India       |  F77BE66C50  |
  | 4  | 8001211892 | Vodafone Idea (Vodafone Idea Limited) |    West Bengal     | 101275680693989  | 6f:c6:23:4c:70:6d |  106.96.240.242 |      Gangtok, West Bengal, India       |  0E180AF011  |
  | 5  | 8081277892 |  Jio (Reliance Jio Infocomm Limited)  | Uttar Pradesh East | 860902293116337  | 47:a7:b1:99:d2:4d |  28.127.236.188 |    Allahabad, Uttar Pradesh, India     |  5AC6D2509B  |
  | 6  | 8081271892 |  Jio (Reliance Jio Infocomm Limited)  | Uttar Pradesh East | 910279755168308  | 59:ae:4c:12:aa:fe |  212.28.99.182  | Kagazipur, Uttar Pradesh 233303, India |  D99AC1E5A5  |
  | 7  | 8081217892 |  Jio (Reliance Jio Infocomm Limited)  | Uttar Pradesh East | 453129414620525  | ba:7a:c4:4f:71:26 |  80.77.141.207  |       Mau, Uttar Pradesh, India        |  14BBFBA617  |
  | 8  | 8081211892 |  Jio (Reliance Jio Infocomm Limited)  | Uttar Pradesh East | 492683063296519  | 0d:58:55:19:18:cb |   38.12.196.29  |   Farrukhabad, Uttar Pradesh, India    |  0EECF1565D  |
  | 9  | 8801277892 |  BSNL (Bharat Sanchar Nigam Limited)  |   Andhra Pradesh   | 991576689617017  | 7c:1c:a7:b3:14:23 |  253.169.100.33 |    Warangal, Andhra Pradesh, India     |  2CC30BF50D  |
  | 10 | 8801271892 |  BSNL (Bharat Sanchar Nigam Limited)  |   Andhra Pradesh   | 0120227686539910 | 1b:f4:af:db:21:73 |  119.120.72.72  |      Eluru, Andhra Pradesh, India      |  79327DD037  |
  | 11 | 8801217892 |  BSNL (Bharat Sanchar Nigam Limited)  |   Andhra Pradesh   | 513535448689492  | 41:32:e5:90:65:64 | 128.156.104.111 |    Proddutur, Andhra Pradesh, India    |  6732D43D1C  |
  | 12 | 8801211892 |  BSNL (Bharat Sanchar Nigam Limited)  |   Andhra Pradesh   | 524157732269456  | 8e:42:e3:31:54:4b | 192.158.237.174 |     Kurnool, Andhra Pradesh, India     |  9CAC05D79F  |
  | 13 | 8881277892 | Vodafone Idea (Vodafone Idea Limited) | Uttar Pradesh East | 442384413796537  | f1:e0:b8:b1:ee:32 |  138.255.162.49 |  Maudaha, Uttar Pradesh 210507, India  |  953D7D613F  |
  | 14 | 8881271892 | Vodafone Idea (Vodafone Idea Limited) | Uttar Pradesh East | 452876513208526  | a0:0d:8e:d1:d4:62 |   2.198.86.131  |      Jhansi, Uttar Pradesh, India      |  85B826418D  |
  | 15 | 8881217892 | Vodafone Idea (Vodafone Idea Limited) | Uttar Pradesh East | 980023048644104  | 25:a8:03:26:13:f3 |  3.224.159.144  |      Hardoi, Uttar Pradesh, India      |  3B4B09415C  |
  | 16 | 8881211892 | Vodafone Idea (Vodafone Idea Limited) | Uttar Pradesh East | 990607448600019  | be:af:06:27:9e:7f | 127.191.187.103 |    Allahabad, Uttar Pradesh, India     |  54A5B049FF  |
  +----+------------+---------------------------------------+--------------------+------------------+-------------------+-----------------+----------------------------------------+--------------+
  ```
