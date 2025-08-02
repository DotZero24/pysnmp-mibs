_I='read-create'
_H='read-write'
_G='entPhysicalIndex'
_F='ENTITY-MIB'
_E='Integer32'
_D='unknown'
_C='DisplayString'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
entPhysicalIndex,=mibBuilder.importSymbols(_F,_G)
ome6500,=mibBuilder.importSymbols('NORTEL-OPTICAL-OME6500-MIB','ome6500')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_C,'PhysAddress','RowStatus','TextualConvention')
nnOme6500Equipments=ModuleIdentity((1,3,6,1,4,1,562,68,11,2))
if mibBuilder.loadTexts:nnOme6500Equipments.setRevisions(('2007-08-10 00:00','2008-02-07 00:00','2008-02-21 00:00','2008-03-10 00:00','2008-03-27 00:00','2008-07-30 00:00','2008-08-20 00:00','2009-04-19 00:00','2009-05-05 00:00','2009-08-05 00:00','2010-06-30 00:00','2010-11-01 00:00','2010-12-07 00:00','2011-01-18 00:00','2011-03-18 00:00','2011-03-28 00:00','2011-08-03 00:00','2011-08-19 00:00','2011-08-30 00:00','2012-02-22 00:00','2012-03-23 00:00','2012-05-08 00:00','2012-07-26 00:00','2012-09-11 00:00','2012-10-05 00:00','2012-12-04 00:00','2013-01-23 00:00','2013-04-02 00:00','2013-06-09 00:00','2013-08-01 00:00','2013-10-30 00:00','2013-11-19 00:00','2014-01-14 00:00','2014-05-06 00:00','2014-05-15 00:00','2014-05-29 00:00','2014-06-03 00:00','2014-06-23 00:00','2014-07-22 00:00','2014-08-27 00:00','2014-10-20 00:00'))
class Boolean(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('false',0),('true',1)))
class AdminState(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_D,0),('is',1),('oos',2)))
class PrimaryState(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*((_D,0),('is',1),('is-anr',2),('oos-au',3),('oos-ma',4),('oos-auma',5),('oos-maanr',6)))
class EquipmentType(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,193,194,195,196,197,198,199,200,201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226,227,228,229,230,231,232,233,234,235,236,237,238,239,240,241,242,243,244,245,246,247,248,249,250,251,252,253,254,255,256,257,258,259,260,261,262,263,264,265,266,267,268,269,270,271,272,273,274,275,276,277,278,279,280,281,282,283,284,285,286,287,288,289,290,291,292,293,294,295,296,297,298,299,300,301,302,303,304,305,306)));namedValues=NamedValues(*(('eNil',0),('eEMPTY',1),('eUNKNOWN',2),('eILAN',3),('eODU2',4),('eDS1',5),('eDS3',6),('eOC3',7),('eXC',8),('eSP',9),('eFC100',10),('eOC12',11),('eSTS1DS3',12),('eSTS1E3',13),('eVT1DS1',14),('eVT2E1',15),('eSMUX',16),('eFC200',17),('eEC1',18),('eE1WAN',19),('eFC400',20),('eVCE-ETH10G',21),('eVCEMAP-ETH10G',22),('e40GMUX',23),('e20GL2SS',24),('eDS1WAN',25),('eEIO',26),('eE3WAN',27),('e40GOCI',28),('e40GOCLD',29),('eDS3V',30),('eDS3WAN',31),('eE1',32),('eP10GSOELFC',33),('eOTS',34),('eWSSOPM',35),('e155ME',36),('e155MEP',37),('eOC48',38),('ePWR',39),('eFILLED-IO',40),('eBNC-IO',41),('eFAN',42),('eE1DS3',43),('eE1E3',44),('eVT2DS3',45),('eVT2E3',46),('ePGE',47),('ePGEFC200',48),('eDS1TM',49),('eDSMBP',50),('eDSMOAMEX',51),('eDSMFANX3',52),('eDSMIO',53),('eDSM',54),('eCMD44',55),('eDINPIO',56),('eBackplane',57),('e1GFOSFC',58),('eFILLED',59),('eFC1200',60),('eOC192',61),('eSLOT',62),('eMIC',63),('eAP',64),('eFILLER',65),('eFANHOUSING',66),('e155622M',67),('e2G5',68),('e10G',69),('e1GFOS',70),('eP155622M',71),('eP2G5',72),('eP2G5W',73),('ePGEFC',74),('eETH',75),('eFC',76),('eWAN',77),('eSTS1',78),('eSTS3c',79),('eSTS12c',80),('eSTS24c',81),('eSTS48c',82),('eSTS192c',83),('eVT15',84),('eVT2',85),('eVT6',86),('e2G5W',87),('e10GW',88),('eBITSIN',89),('eBITSOUT',90),('eDS3EC1',91),('eE1PSM-IO',92),('eE1CNV-IO',93),('eGMD',94),('eDOSC',95),('eCMD4',96),('eLIM',97),('eSLA',98),('eMLA',99),('eVOA',100),('eEDFA',101),('eOPTMON',102),('eOSC',103),('eDOC',104),('eP155M',105),('eP622M',106),('eADJ',107),('eDS3EC1P',108),('eE1P',109),('eCOLAN',110),('eWAYSIDE',111),('eADJTX',112),('eADJRX',113),('eADJLN',114),('eNC',115),('eVT15AU4',116),('eVT2AU4',117),('eVT6AU4',118),('eSTS1AU4',119),('eDSCM',120),('eSHELF',121),('eSWT',122),('eOST',123),('eOPM',124),('eWB',125),('e10GOCWT',126),('e10GELWT',127),('eOC768',128),('e2G5MX',129),('eOTM1',130),('eOTM2',131),('eOTM3',132),('eETH10G',133),('ePUNKNOWN',134),('eP155Me',135),('eSTM1e',136),('eL2SS',137),('eLAN',138),('eENV',139),('eCONT',140),('e1FN-BNC-IO',141),('eDEST',142),('eUOSC',143),('eCMD8',144),('eWSS',145),('eCHC',146),('eSCO',147),('eVCS',148),('eVCE',149),('eVCE-ETH',150),('eVCE-WAN',151),('eVCE-LAG',152),('eVCEMAP',153),('eVCEMAP-ETH',154),('eVCEMAP-WAN',155),('eVCEMAP-LAG',156),('eBWPRF',157),('eDMPRF',158),('eCFPRF',159),('eFE',160),('ePFE',161),('eP10GS',162),('eP10GEL',163),('eP10GSEL',164),('eP10GSOEL',165),('e10GOCLD',166),('e2xOSC',167),('e10GOTR',168),('eTMUX',169),('eDS1DS3',170),('eVT1DS3',171),('eSE',172),('eRPR',173),('eMXC',174),('eCOSST',175),('eCOSBR',176),('eCOSSL',177),('eCOSGD',178),('eCOSPL',179),('eCOSPR',180),('eCOSNT',181),('eCOSCR',182),('eLAG',183),('eETH100',184),('eCHMON',185),('eE1MIO75P',186),('eE1MIO120P',187),('eE1MIO75U',188),('eE1MIO120U',189),('eTNS',190),('eTNE',191),('eTNE-ETH',192),('eTNE-WAN',193),('eTNE-RPR',194),('eTNE-LAG',195),('eTNEMAP',196),('eTNEMAP-ETH',197),('eTNEMAP-WAN',198),('eTNEMAP-RPR',199),('eTNEMAP-LAG',200),('eVCE-RPR',201),('eVCEMAP-RPR',202),('eRPR-RING',203),('eRPR-RINGLET',204),('eCOS',205),('eRPR-STATION',206),('e10GOTNWT',207),('eLNGRP',208),('eWTGRP',209),('eFE-IO',210),('eOCH',211),('ePRTSCHED',212),('eHOP',213),('eE3',214),('e10GOTSC',215),('eFDB',216),('eFDBSTATIC',217),('eCOSA',218),('eCOSBC',219),('eCOSBE',220),('eCOSC',221),('eXGE',222),('eDRA',223),('eRAMAN',224),('eVCEA',225),('eVCEBC',226),('eVCEBE',227),('eVCEC',228),('eTNEA',229),('eTNEBC',230),('eTNEBE',231),('eTNEC',232),('ePCWDMS',233),('eSCHPRF',234),('eVCEST',235),('eVCESL',236),('eVCEGD',237),('eVCEPR',238),('eVCENT',239),('eTNEST',240),('eTNESL',241),('eTNEGD',242),('eTNEPR',243),('eTNENT',244),('ePFC400',245),('eDISP',246),('eHEXOCN',247),('eODU3',248),('eCMDA',249),('e10GWT',250),('e2G5MOTR',251),('eGENERIC',252),('eDS3E3EC1',253),('eDS3E3EC1P',254),('eGE',255),('eL2RPR',256),('eMRO',257),('eOTSC',258),('eMRO2',259),('eL2MOTR',260),('eTPT',261),('eOMX',262),('e40GXCIF',263),('e100GOCLD',264),('e100GOCI',265),('e100GMUX',266),('e40GUMUX',267),('e40GUOCLD',268),('eOSIC',269),('eFLEXMOTR',270),('ePCFP',271),('ePSFP',272),('eOTNFMOTR',273),('eSPOTNFMOTR',274),('eCCMD12',275),('eSMD',276),('eOTNFLEX',277),('eOTNXCIF',278),('eSLIC',279),('ePPC6',280),('eBS',281),('eOMDF4',282),('eOMDF8',283),('eOSCF',284),('eFGA',285),('ePXFP',286),('eOPS',287),('eEVOA',288),('eEMOTR',289),('ePKTFLEX',290),('eSRA',291),('eSAM',292),('eESAM',293),('eXLA',294),('eISS',295),('ePQSFP',296),('eOTR',297),('ePKTOTN',298),('ePKTOTNXCIF',299),('eCCMD8X16',300),('ePCXM',301),('eFIM',302),('eBMD',303),('eGMD10',304),('eMOTR',305),('eMAX',306)))
class SecondaryState(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94)));namedValues=NamedValues(*((_D,0),('nil',1),('act',2),('idle',3),('sgeo',4),('psi',5),('flt',6),('mea',7),('stbyh',8),('ts',9),('ueq',10),('wrk',11),('wrksync',12),('wrktraf',13),('faf',14),('meaAndFlt',15),('actAndFlt',16),('actAndWrksync',17),('actAndFltAndWrksync',18),('idleAndFlt',19),('idleAndWrksync',20),('idleAndFltAndWrksync',21),('wrktrafAndWrksync',22),('ains',23),('actAndAins',24),('ainsAndIdle',25),('ainsAndSgeo',26),('ainsAndPsi',27),('ainsAndFlt',28),('ainsAndMea',29),('ainsAndStbyh',30),('ainsAndTs',31),('ainsAndUeq',32),('ainsAndWrk',33),('ainsAndWrksync',34),('ainsAndWrktraf',35),('ainsAndFaf',36),('ainsAndMeaAndFlt',37),('actAndAinsAndFlt',38),('actAndAinsAndWrksync',39),('actAndAinsAndFltAndWrksync',40),('ainsAndIdleAndFlt',41),('ainsAndIdleAndWrksync',42),('ainsAndIdleAndFltAndWrksync',43),('ainsAndWrktrafAndWrksync',44),('idleAndUeq',45),('fltAndWrksync',46),('wrkctrl',47),('actAndWrkctrl',48),('idleAndWrkctrl',49),('ainsAndWrkctrl',50),('fltAndWrkctrl',51),('actAndFltAndWrkctrl',52),('idleAndFltAndWrkctrl',53),('actAndAinsAndWrkctrl',54),('actAndAinsAndFltAndWrkctrl',55),('ainsAndIdleAndWrkctrl',56),('ainsAndIdleAndFltAndWrkctrl',57),('wrktrafAndWrksyncAndWrkctrl',58),('ainsAndWrktrafAndWrksyncAndWrkctrl',59),('ueqAndStbyh',60),('ainsAndUeqAndStbyh',61),('meaAndStbyh',62),('fltAndStbyh',63),('fltAndWrktrafAndWrksync',64),('meaAndWrksync',65),('ueqAndWrksync',66),('actAndWrk',67),('idleAndWrk',68),('actAndStbyh',69),('idleAndStbyh',70),('stbys',71),('ainsAndStbys',72),('ueqAndStbys',73),('ainsAndUeqAndStbys',74),('meaAndStbys',75),('fltAndStbys',76),('actAndStbys',77),('idleAndStbys',78),('fltAndWrk',79),('fltAndUeq',80),('fltAndWrktraf',81),('fltAndWrktrafAndWrksyncAndWrkctrl',82),('fltAndSgeo',83),('idleAndSgeo',84),('idleAndWrkAndUeq',85),('idleAndStbysAndUeq',86),('idleAndStbysAndFlt',87),('idleAndStbyhAndUeq',88),('idleAndStbyhAndFlt',89),('wrktrafAndWrkctrl',90),('wrksyncAndWrkctrl',91),('actAndUeq',92),('wrkAndMea',93),('idleAndMea',94)))
class EquipmentMode(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14)));namedValues=NamedValues(*((_D,0),('nil',1),('internal',2),('mated',3),('xconnect',4),('internal-mated',5),('internal-xconnect',6),('mated-xconnect',7),('internal-mated-xconnect',8),('matedsym',9),('internal-matedsym',10),('matedsym-xc',11),('internal-matedsym-xconnect',12),('mate-pending',13),('mate-pending-xconnect',14)))
_NnEqptProv_ObjectIdentity=ObjectIdentity
nnEqptProv=_NnEqptProv_ObjectIdentity((1,3,6,1,4,1,562,68,11,2,1))
_NnEqptProvTable_Object=MibTable
nnEqptProvTable=_NnEqptProvTable_Object((1,3,6,1,4,1,562,68,11,2,1,1))
if mibBuilder.loadTexts:nnEqptProvTable.setStatus(_A)
_NnEqptProvEntry_Object=MibTableRow
nnEqptProvEntry=_NnEqptProvEntry_Object((1,3,6,1,4,1,562,68,11,2,1,1,1))
nnEqptProvEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:nnEqptProvEntry.setStatus(_A)
_ProvEqptType_Type=EquipmentType
_ProvEqptType_Object=MibTableColumn
provEqptType=_ProvEqptType_Object((1,3,6,1,4,1,562,68,11,2,1,1,1,1),_ProvEqptType_Type())
provEqptType.setMaxAccess(_I)
if mibBuilder.loadTexts:provEqptType.setStatus(_A)
_ProvCardType_Type=DisplayString
_ProvCardType_Object=MibTableColumn
provCardType=_ProvCardType_Object((1,3,6,1,4,1,562,68,11,2,1,1,1,2),_ProvCardType_Type())
provCardType.setMaxAccess(_B)
if mibBuilder.loadTexts:provCardType.setStatus(_A)
_ProvEqptAID_Type=DisplayString
_ProvEqptAID_Object=MibTableColumn
provEqptAID=_ProvEqptAID_Object((1,3,6,1,4,1,562,68,11,2,1,1,1,3),_ProvEqptAID_Type())
provEqptAID.setMaxAccess(_B)
if mibBuilder.loadTexts:provEqptAID.setStatus(_A)
class _ProvPec_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,22))
_ProvPec_Type.__name__=_C
_ProvPec_Object=MibTableColumn
provPec=_ProvPec_Object((1,3,6,1,4,1,562,68,11,2,1,1,1,4),_ProvPec_Type())
provPec.setMaxAccess(_I)
if mibBuilder.loadTexts:provPec.setStatus(_A)
_AdminState_Type=AdminState
_AdminState_Object=MibTableColumn
adminState=_AdminState_Object((1,3,6,1,4,1,562,68,11,2,1,1,1,5),_AdminState_Type())
adminState.setMaxAccess(_H)
if mibBuilder.loadTexts:adminState.setStatus(_A)
_PrimaryState_Type=PrimaryState
_PrimaryState_Object=MibTableColumn
primaryState=_PrimaryState_Object((1,3,6,1,4,1,562,68,11,2,1,1,1,6),_PrimaryState_Type())
primaryState.setMaxAccess(_B)
if mibBuilder.loadTexts:primaryState.setStatus(_A)
_SecondaryState_Type=SecondaryState
_SecondaryState_Object=MibTableColumn
secondaryState=_SecondaryState_Object((1,3,6,1,4,1,562,68,11,2,1,1,1,7),_SecondaryState_Type())
secondaryState.setMaxAccess(_B)
if mibBuilder.loadTexts:secondaryState.setStatus(_A)
_EqptMode_Type=EquipmentMode
_EqptMode_Object=MibTableColumn
eqptMode=_EqptMode_Object((1,3,6,1,4,1,562,68,11,2,1,1,1,8),_EqptMode_Type())
eqptMode.setMaxAccess(_B)
if mibBuilder.loadTexts:eqptMode.setStatus(_A)
_MateEqpt1_Type=DisplayString
_MateEqpt1_Object=MibTableColumn
mateEqpt1=_MateEqpt1_Object((1,3,6,1,4,1,562,68,11,2,1,1,1,9),_MateEqpt1_Type())
mateEqpt1.setMaxAccess(_B)
if mibBuilder.loadTexts:mateEqpt1.setStatus(_A)
_MateEqpt2_Type=DisplayString
_MateEqpt2_Object=MibTableColumn
mateEqpt2=_MateEqpt2_Object((1,3,6,1,4,1,562,68,11,2,1,1,1,10),_MateEqpt2_Type())
mateEqpt2.setMaxAccess(_B)
if mibBuilder.loadTexts:mateEqpt2.setStatus(_A)
_MateEqpt3_Type=DisplayString
_MateEqpt3_Object=MibTableColumn
mateEqpt3=_MateEqpt3_Object((1,3,6,1,4,1,562,68,11,2,1,1,1,11),_MateEqpt3_Type())
mateEqpt3.setMaxAccess(_B)
if mibBuilder.loadTexts:mateEqpt3.setStatus(_A)
_RowStatus_Type=RowStatus
_RowStatus_Object=MibTableColumn
rowStatus=_RowStatus_Object((1,3,6,1,4,1,562,68,11,2,1,1,1,12),_RowStatus_Type())
rowStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:rowStatus.setStatus(_A)
class _MapMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_D,0),('au3-vt15',1),('au4-vt2',2)))
_MapMode_Type.__name__=_E
_MapMode_Object=MibTableColumn
mapMode=_MapMode_Object((1,3,6,1,4,1,562,68,11,2,1,1,1,13),_MapMode_Type())
mapMode.setMaxAccess(_B)
if mibBuilder.loadTexts:mapMode.setStatus(_A)
_TimingGroupId_Type=DisplayString
_TimingGroupId_Object=MibTableColumn
timingGroupId=_TimingGroupId_Object((1,3,6,1,4,1,562,68,11,2,1,1,1,14),_TimingGroupId_Type())
timingGroupId.setMaxAccess(_B)
if mibBuilder.loadTexts:timingGroupId.setStatus(_A)
class _DsmSiteAddress_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_DsmSiteAddress_Type.__name__=_C
_DsmSiteAddress_Object=MibTableColumn
dsmSiteAddress=_DsmSiteAddress_Object((1,3,6,1,4,1,562,68,11,2,1,1,1,15),_DsmSiteAddress_Type())
dsmSiteAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:dsmSiteAddress.setStatus(_A)
_NnInventory_ObjectIdentity=ObjectIdentity
nnInventory=_NnInventory_ObjectIdentity((1,3,6,1,4,1,562,68,11,2,2))
_NnInventoryTable_Object=MibTable
nnInventoryTable=_NnInventoryTable_Object((1,3,6,1,4,1,562,68,11,2,2,1))
if mibBuilder.loadTexts:nnInventoryTable.setStatus(_A)
_NnInventoryEntry_Object=MibTableRow
nnInventoryEntry=_NnInventoryEntry_Object((1,3,6,1,4,1,562,68,11,2,2,1,1))
nnInventoryEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:nnInventoryEntry.setStatus(_A)
_ActualEqptType_Type=EquipmentType
_ActualEqptType_Object=MibTableColumn
actualEqptType=_ActualEqptType_Object((1,3,6,1,4,1,562,68,11,2,2,1,1,1),_ActualEqptType_Type())
actualEqptType.setMaxAccess(_B)
if mibBuilder.loadTexts:actualEqptType.setStatus(_A)
_ActualCardType_Type=DisplayString
_ActualCardType_Object=MibTableColumn
actualCardType=_ActualCardType_Object((1,3,6,1,4,1,562,68,11,2,2,1,1,2),_ActualCardType_Type())
actualCardType.setMaxAccess(_B)
if mibBuilder.loadTexts:actualCardType.setStatus(_A)
_InventoryAID_Type=DisplayString
_InventoryAID_Object=MibTableColumn
inventoryAID=_InventoryAID_Object((1,3,6,1,4,1,562,68,11,2,2,1,1,3),_InventoryAID_Type())
inventoryAID.setMaxAccess(_B)
if mibBuilder.loadTexts:inventoryAID.setStatus(_A)
class _ProductEqptCode_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_ProductEqptCode_Type.__name__=_C
_ProductEqptCode_Object=MibTableColumn
productEqptCode=_ProductEqptCode_Object((1,3,6,1,4,1,562,68,11,2,2,1,1,4),_ProductEqptCode_Type())
productEqptCode.setMaxAccess(_B)
if mibBuilder.loadTexts:productEqptCode.setStatus(_A)
_ReleaseLevel_Type=DisplayString
_ReleaseLevel_Object=MibTableColumn
releaseLevel=_ReleaseLevel_Object((1,3,6,1,4,1,562,68,11,2,2,1,1,5),_ReleaseLevel_Type())
releaseLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:releaseLevel.setStatus(_A)
class _Clei_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_Clei_Type.__name__=_C
_Clei_Object=MibTableColumn
clei=_Clei_Object((1,3,6,1,4,1,562,68,11,2,2,1,1,6),_Clei_Type())
clei.setMaxAccess(_B)
if mibBuilder.loadTexts:clei.setStatus(_A)
class _SerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,25))
_SerialNumber_Type.__name__=_C
_SerialNumber_Object=MibTableColumn
serialNumber=_SerialNumber_Object((1,3,6,1,4,1,562,68,11,2,2,1,1,7),_SerialNumber_Type())
serialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:serialNumber.setStatus(_A)
_ManufactureDate_Type=DisplayString
_ManufactureDate_Object=MibTableColumn
manufactureDate=_ManufactureDate_Object((1,3,6,1,4,1,562,68,11,2,2,1,1,8),_ManufactureDate_Type())
manufactureDate.setMaxAccess(_B)
if mibBuilder.loadTexts:manufactureDate.setStatus(_A)
_InServiceAge_Type=DisplayString
_InServiceAge_Object=MibTableColumn
inServiceAge=_InServiceAge_Object((1,3,6,1,4,1,562,68,11,2,2,1,1,9),_InServiceAge_Type())
inServiceAge.setMaxAccess(_B)
if mibBuilder.loadTexts:inServiceAge.setStatus(_A)
_OnSince_Type=DisplayString
_OnSince_Object=MibTableColumn
onSince=_OnSince_Object((1,3,6,1,4,1,562,68,11,2,2,1,1,10),_OnSince_Type())
onSince.setMaxAccess(_B)
if mibBuilder.loadTexts:onSince.setStatus(_A)
_PhysicallyPresent_Type=Boolean
_PhysicallyPresent_Object=MibTableColumn
physicallyPresent=_PhysicallyPresent_Object((1,3,6,1,4,1,562,68,11,2,2,1,1,11),_PhysicallyPresent_Type())
physicallyPresent.setMaxAccess(_B)
if mibBuilder.loadTexts:physicallyPresent.setStatus(_A)
class _RestartCard_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_D,0),('cold',1),('warm',2)))
_RestartCard_Type.__name__=_E
_RestartCard_Object=MibTableColumn
restartCard=_RestartCard_Object((1,3,6,1,4,1,562,68,11,2,2,1,1,12),_RestartCard_Type())
restartCard.setMaxAccess(_H)
if mibBuilder.loadTexts:restartCard.setStatus(_A)
class _DsmMate_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,25))
_DsmMate_Type.__name__=_C
_DsmMate_Object=MibTableColumn
dsmMate=_DsmMate_Object((1,3,6,1,4,1,562,68,11,2,2,1,1,13),_DsmMate_Type())
dsmMate.setMaxAccess(_B)
if mibBuilder.loadTexts:dsmMate.setStatus(_A)
class _DsmConn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_D,0),('direct',1),('indirect',2)))
_DsmConn_Type.__name__=_E
_DsmConn_Object=MibTableColumn
dsmConn=_DsmConn_Object((1,3,6,1,4,1,562,68,11,2,2,1,1,14),_DsmConn_Type())
dsmConn.setMaxAccess(_B)
if mibBuilder.loadTexts:dsmConn.setStatus(_A)
mibBuilder.exportSymbols('NORTEL-OME6500-EQPT-MIB',**{'Boolean':Boolean,'AdminState':AdminState,'PrimaryState':PrimaryState,'EquipmentType':EquipmentType,'SecondaryState':SecondaryState,'EquipmentMode':EquipmentMode,'nnOme6500Equipments':nnOme6500Equipments,'nnEqptProv':nnEqptProv,'nnEqptProvTable':nnEqptProvTable,'nnEqptProvEntry':nnEqptProvEntry,'provEqptType':provEqptType,'provCardType':provCardType,'provEqptAID':provEqptAID,'provPec':provPec,'adminState':adminState,'primaryState':primaryState,'secondaryState':secondaryState,'eqptMode':eqptMode,'mateEqpt1':mateEqpt1,'mateEqpt2':mateEqpt2,'mateEqpt3':mateEqpt3,'rowStatus':rowStatus,'mapMode':mapMode,'timingGroupId':timingGroupId,'dsmSiteAddress':dsmSiteAddress,'nnInventory':nnInventory,'nnInventoryTable':nnInventoryTable,'nnInventoryEntry':nnInventoryEntry,'actualEqptType':actualEqptType,'actualCardType':actualCardType,'inventoryAID':inventoryAID,'productEqptCode':productEqptCode,'releaseLevel':releaseLevel,'clei':clei,'serialNumber':serialNumber,'manufactureDate':manufactureDate,'inServiceAge':inServiceAge,'onSince':onSince,'physicallyPresent':physicallyPresent,'restartCard':restartCard,'dsmMate':dsmMate,'dsmConn':dsmConn})