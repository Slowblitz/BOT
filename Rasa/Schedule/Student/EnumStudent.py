from enum import Enum

class Promotion(Enum):
        L1 = "2-L1IN"
        L2 = "2-L2IN"
        L3 = "2-L3IN"
        M1_ILSEN = "2-M1IN"
        M1_SICOM = "2-M1S1"
        M1_IA = "2-M1IA"
        M2_ILSEN = "2-M2EN"
        M2_SICON = "2-M2S1"
        M2_IA = "2-M2IA"

class Groupe(Enum):
        #Groupe de L1
        L1G1 = "3260"
        L1G2 = "3261"
        L1G3 = "3262"
        L1G4 = "3263"
        L1G5 = "3264"
        L1G6 = "3265"
        
        #Groupe de L2
        L2G1 = "3674"
        L2G2 = "3675"
        L2G3 = "3676"
        L2G4 = "3677"
        
        #Groupe de L3
        L3E1 = "6157"
        L3E2 = "6158"
        L3E3 = "6159"
        L3G1 = "3940"
        L3G2 = "3941"
        L3G3 = "3942"
        L3G4 = "3943"
        L3G5 = "3944"
        
        #Groupe de master ilsen
        M1_ILSEN_ALT = "6443"
        M1_ILSEN_CLA = "6444"
        M2_ILSEN_ALT = "4132"
        M2_ILSEN_CLA = "4233"
        M2_APPLI1 = "4126"
        M2_APPLI2 = "4127"
        M2_APPLI3 = "4128"
        M2_APPLI4 = "4129"
        M2_ECOM = "4130"
        M2_INGEDOC = "4131"
        
        #Groupe de master sicon
        M1_SICOM_ALT = "4084"
        M1_SICON_CLA = "4085"
        M2_SICOM_ALT = "4166"
        M2_SICOM_CLA = "4167"
        
        #Groupe de master IA
        M1_IA_IL_ALT = "4062"
        M1_IA_IL_CLA = "4063"
        M1_IA_SICOM_ALT = "4064"
        M1_IA_SICOM_CLA = "4065"
        M2_IA_IL_ALT = "5615"
        M2_IA_IL_CLA = "5616"
        M2_IA_SICOM_ALT = "5617"
        M2_IA_SICOM_CLA = "5618"