# A-manager - Alcatel LTE router helper utility
This script is designed to help with diagnosctis of LTE connection provided by the Alcatel router.

It was build and tested on Alcatel Link Hub LTE cat. 7 (HH71) model, however looking at other scripts available on the internet, it _should_ also operate on other models.

## Installation and configuration
The script was written in Python 3 and it is its main requirement.

1. Clone the repository
2. Copy `config_teplate.json` file to `config.json`
3. Provide username, password and URL to the router in `config.json` file

## Usage
1. Start the app:
```
python3 poc.py
```
2. The app should start printing information about LTE connection. A sample output:
```
NetworkName     CellId          RSSI  RSRQ  SINR  RSRP  LTE_state  Band
Orange          71698198        -55   -15   -1    -91   5177345    120
Orange          71698198        -58   -14   -1    -92   5177345    120
Orange          71698198        -58   -14   -1    -92   5177345    120
Orange          71698198        -58   -15   1     -92   5177345    120
Orange          71698198        -58   -15   1     -92   5177345    120
Orange          71698198        -58   -15   0     -91   5177345    120
```

### Output decription
Aside from basic information like RSSI, RSRQ and other signal parameters, there are two interesting parameters `LTE_state` and `Band`. Based on my observations the latter contains used band in some form. The former seem to be change as Band changes as well so I believe it should contain this information as well.

Here are noted down observed values of `Band` parameter and my _current_ understanding what they mean:
- `145` - LTE 800 band
- `120` - LTE 2100 band
- `126` - LTE 2600 band
- `3175` - ???
- `6350` - ???
Not sure what question marked values mean - maybe that's some form of link aggregation?
