from selfdrive.car import dbc_dict

# Car button codes
class CruiseButtons:
  RES_ACCEL   = 4
  DECEL_SET   = 3
  CANCEL      = 2
  MAIN        = 1


#car chimes: enumeration from dbc file. Chimes are for alerts and warnings
class CM:
  MUTE = 0
  SINGLE = 3
  DOUBLE = 4
  REPEATED = 1
  CONTINUOUS = 2


#car beepss: enumeration from dbc file. Beeps are for activ and deactiv
class BP:
  MUTE = 0
  SINGLE = 3
  TRIPLE = 2
  REPEATED = 1

class AH:
  #[alert_idx, value]
  # See dbc files for info on values"
  NONE           = [0, 0]
  FCW            = [1, 1]  #2018.09.02 have
  STEER          = [2, 1]   #2018.09.02 TODO check alert values
  BRAKE_PRESSED  = [3, 10]  #2018.09.02 value does match
  GEAR_NOT_D     = [4, 6]  #2018.09.02 TODO this come from BO_927 0x39F from adas need to add in DBC
  SEATBELT       = [5, 5]  #2018.09.02 not find where it use
  SPEED_TOO_HIGH = [6, 8]  #2018.09.02 TODO this come from BO_927 0x39F from adas need to add in DBC


class CAR:
  SOUL = "KIA SOUL TEST" #Test Spoof johnwayneairobot 2018.09.02
  SOUL1 = "KIA SOUL TEST1" #Test Spoof johnwayneairobot 2018.09.03
  SOUL2 = "KIA SOUL TEST2" #Test Spoof johnwayneairobot 2018.09.03
  SOUL3 = "KIA SOUL TEST3" #Test Spoof johnwayneairobot 2018.09.03
  SOUL4 = "KIA SOUL TEST4" #Test Spoof johnwayneairobot 2018.09.03
  SOUL5 = "KIA SOUL TEST5" #Test Spoof johnwayneairobot 2018.09.03
  SOUL6 = "KIA SOUL TEST6" #Te #ret.genericToggle = self.CS.generic_togglest Spoof johnwayneairobot 2018.09.03
  SOUL7 = "KIA SOUL TEST7" #Test Spoof johnwayneairobot 2018.09.03
  SOUL8 = "KIA SOUL TEST8" #Test Spoof johnwayneairobot 2018.09.03
  SOUL9 = "KIA SOUL TEST9" #Test Spoof johnwayneairobot 2018.09.03
  SOUL10 = "KIA SOUL TEST10" #Test Spoof johnwayneairobot 2018.09.03
  SOUL11 = "KIA SOUL TEST11"  # Test Spoof johnwayneairobot 2018.09.03
  DUMMY = "DUMMY TEST SPOOF" #2018.09.03 test spoof


FINGERPRINTS = {
  # Soul Vehicle with Steering Gas and Throttle in disable state
  CAR.SOUL: [{115: 8, 131: 8, 147: 8, 185: 8, 357: 8, 544: 8, 688: 8, 790: 8, 809: 8, 880: 8, 1088: 8, 1200: 8, 1680: 8
  }], # from fingerprint.py
  CAR.SOUL1: [{115: 8, 131: 8, 147: 8, 185: 8, 357: 8, 422: 8, 544: 8, 688: 8, 790: 8, 809: 8, 880: 8, 1088: 8, 1200: 8, 1680: 8
  }], # Fingerprint and add 1A6 as startup
  CAR.SOUL2: [{115: 8, 131: 8, 147: 8, 185: 8, 357: 8, 422: 8, 544: 8, 790: 8, 809: 8, 880: 8, 1088: 8, 1200: 8, 1680: 8
  }], # from get_fingerprint.py and car already start 1A6
  CAR.SOUL3: [{544: 8, 131: 8, 147: 8, 688: 8, 115: 8, 185: 8
  }], #random2 from controlsd fingerprint
  CAR.SOUL4: [{544: 8, 1200: 8, 131: 8, 422: 8, 780: 8, 688: 8, 115: 8, 506: 8
  }], #random3
  CAR.SOUL5: [{544: 8, 880: 8, 115: 8, 131: 8, 357: 8, 422: 8, 1088: 8, 809: 8, 780: 8, 688: 8, 147: 8, 790: 8, 506: 8
  }], #random4
  CAR.SOUL6: [{1088: 8, 880: 8, 131: 8, 357: 8, 809: 8, 1200: 8, 115: 8, 147: 8, 790: 8, 544: 8, 185: 8, 688: 8
  }], # car off and on without 1A6 30C 33D 1FA
  CAR.SOUL7: [{1088: 8, 880: 8, 131: 8, 357: 8, 809: 8, 688: 8, 147: 8, 790: 8, 185: 8
  }], # car off and on without 1A6 30C 33D 1FA simulation
  CAR.SOUL8: [{1088: 8, 544: 8, 357: 8, 809: 8, 1200: 8, 880: 8, 115: 8, 790: 8, 185: 8, 688: 8
  }],  #at the same of turn on all system for CAN
  CAR.SOUL9: [{1088: 8, 880: 8, 131: 8, 357: 8, 809: 8, 1200: 8, 688: 8, 115: 8, 147: 8, 790: 8, 544: 8
  }], # car at the on same time try 2
  CAR.SOUL10: [{115: 8, 185: 8, 147: 8, 131: 8
  }], #controlsd short list
  CAR.SOUL11: [{544: 8, 115: 8, 147: 8
  }], #car not on just turn oscc kit on
  CAR.DUMMY: [{
    57: 3, 145: 8, 228: 5, 304: 8, 316: 8, 342: 6, 344: 8, 380: 8, 398: 3, 399: 7, 419: 8, 420: 8, 422: 8, 428: 8, 432: 7, 464: 8, 476: 4, 490: 8, 506: 8, 512: 6, 513: 6, 542: 7, 545: 4, 597: 8, 660: 8, 773: 7, 777: 8, 780: 8, 800: 8, 804: 8, 808: 8, 819: 7, 821: 5, 829: 5, 882: 2, 884: 7, 887: 8, 888: 8, 892: 8, 923: 2, 929: 4, 983: 8, 985: 3, 1024: 5, 1027: 5, 1029: 8, 1030: 5, 1034: 5, 1036: 8, 1039: 8, 1057: 5, 1064: 7, 1108: 8, 1365: 5,
  }],
}


DBC = {
  CAR.SOUL: dbc_dict('kia_soul_2016_pt_generated.dbc', 'acura_ilx_2016_nidec'), # 2018.09.03 johnwayneairobot change to generator.py dbc
  CAR.SOUL1: dbc_dict('kia_soul_2016_pt_generated.dbc', 'acura_ilx_2016_nidec'), # 2018.09.03 johnwayneairobot change to generator.py dbc
  CAR.SOUL2: dbc_dict('kia_soul_2016_pt_generated.dbc', 'acura_ilx_2016_nidec'), # 2018.09.03 johnwayneairobot change to generator.py dbc
  CAR.SOUL3: dbc_dict('kia_soul_2016_pt_generated.dbc', 'acura_ilx_2016_nidec'), # 2018.09.03 johnwayneairobot change to generator.py dbc
  CAR.SOUL4: dbc_dict('kia_soul_2016_pt_generated.dbc', 'acura_ilx_2016_nidec'), # 2018.09.03 johnwayneairobot change to generator.py dbc
  CAR.SOUL5: dbc_dict('kia_soul_2016_pt_generated.dbc', 'acura_ilx_2016_nidec'), # 2018.09.03 johnwayneairobot change to generator.py dbc
  CAR.SOUL6: dbc_dict('kia_soul_2016_pt_generated.dbc', 'acura_ilx_2016_nidec'), # 2018.09.03 johnwayneairobot change to generator.py dbc
  CAR.SOUL7: dbc_dict('kia_soul_2016_pt_generated.dbc', 'acura_ilx_2016_nidec'), # 2018.09.03 johnwayneairobot change to generator.py dbc
  CAR.SOUL8: dbc_dict('kia_soul_2016_pt_generated.dbc', 'acura_ilx_2016_nidec'), # 2018.09.03 johnwayneairobot change to generator.py dbc
  CAR.SOUL9: dbc_dict('kia_soul_2016_pt_generated.dbc', 'acura_ilx_2016_nidec'), # 2018.09.03 johnwayneairobot change to generator.py dbc
  CAR.SOUL10: dbc_dict('kia_soul_2016_pt_generated.dbc', 'acura_ilx_2016_nidec'), # 2018.09.03 johnwayneairobot change to generator.py dbc
  CAR.SOUL11: dbc_dict('kia_soul_2016_pt_generated.dbc', 'acura_ilx_2016_nidec'), # 2018.09.03 johnwayneairobot change to generator.py dbc
}


STEER_THRESHOLD = {
  CAR.SOUL: 0, #2018.09.02 johnwayneairobot steering override from OSCC car in carstate.py when 1 is override
  CAR.SOUL1: 0, #2018.09.02 johnwayneairobot steering override from OSCC car in carstate.py when 1 is override
  CAR.SOUL3: 0, #2018.09.02 johnwayneairobot steering override from OSCC car in carstate.py when 1 is override
  CAR.SOUL4: 0, #2018.09.02 johnwayneairobot steering override from OSCC car in carstate.py when 1 is override
  CAR.SOUL5: 0, #2018.09.02 johnwayneairobot steering override from OSCC car in carstate.py when 1 is override
  CAR.SOUL6: 0, #2018.09.02 johnwayneairobot steering override from OSCC car in carstate.py when 1 is override
  CAR.SOUL7: 0, #2018.09.02 johnwayneairobot steering override from OSCC car in carstate.py when 1 is override
  CAR.SOUL8: 0, #2018.09.02 johnwayneairobot steering override from OSCC car in carstate.py when 1 is override
  CAR.SOUL9: 0, #2018.09.02 johnwayneairobot steering override from OSCC car in carstate.py when 1 is override
  CAR.SOUL10: 0, #2018.09.02 johnwayneairobot steering override from OSCC car in carstate.py when 1 is override
  CAR.SOUL11: 0, #2018.09.02 johnwayneairobot steering override from OSCC car in carstate.py when 1 is override
}

SPEED_FACTOR = {
  CAR.SOUL: 1., #2018.09.02 johnwayneairobot add Soul vehicle for test
  CAR.SOUL1: 1., #2018.09.02 johnwayneairobot add Soul vehicle for test
  CAR.SOUL2: 1., #2018.09.02 johnwayneairobot add Soul vehicle for test
  CAR.SOUL3: 1., #2018.09.02 johnwayneairobot add Soul vehicle for test
  CAR.SOUL4: 1., #2018.09.02 johnwayneairobot add Soul vehicle for test
  CAR.SOUL5: 1., #2018.09.02 johnwayneairobot add Soul vehicle for test
  CAR.SOUL6: 1., #2018.09.02 johnwayneairobot add Soul vehicle for test
  CAR.SOUL7: 1., #2018.09.02 johnwayneairobot add Soul vehicle for test
  CAR.SOUL8: 1., #2018.09.02 johnwayneairobot add Soul vehicle for test
  CAR.SOUL9: 1., #2018.09.02 johnwayneairobot add Soul vehicle for test
  CAR.SOUL10: 1., #2018.09.02 johnwayneairobot add Soul vehicle for test
  CAR.SOUL11: 1., #2018.09.02 johnwayneairobot add Soul vehicle for test

}

# TODO: get these from dbc file
HONDA_BOSCH = [CAR.DUMMY]   #2018.09.03 Define car dummy for test
