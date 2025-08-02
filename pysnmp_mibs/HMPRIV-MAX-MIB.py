_AI='alarmIndex'
_AH='sringIndex'
_AG='igmpPortIndex'
_AF='igmpRouterIndex'
_AE='igmpGroupIndex'
_AD='magnumDeviceQosIndex'
_AC='portStatsIndex'
_AB='gvrpPortIndex'
_AA='sntpIndex'
_A9='magnumEventIndex'
_A8='forwarding'
_A7='listening'
_A6='magnumStpPort'
_A5='magnumBrStpIndex'
_A4='portIndex'
_A3='tvlanIndex'
_A2='pvlanIndex'
_A1='tagBasedVLAN'
_A0='portBasedVLAN'
_z='atPortIndex'
_y='psEntryIndex'
_x='psPortIndex'
_w='l3qqtDscpIndex'
_v='l3qqtPortIndex'
_u='l3qptPortIndex'
_t='priority7'
_s='priority6'
_r='priority5'
_q='priority4'
_p='priority3'
_o='priority2'
_n='priority1'
_m='priority0'
_l='normal'
_k='pqPortIndex'
_j='trapANDalarm'
_i='logANDalarm'
_h='logANDtrap'
_g='doNotExist'
_f='ptPortIndex'
_e='ptSlotIndex'
_d='slotIndex'
_c='Failed'
_b='NotConnected'
_a='NotSupported'
_Z='NotificationType'
_Y='magnumPortNumber'
_X='learning'
_W='alarm'
_V='trap'
_U='log'
_T='true'
_S='false'
_R='delete'
_Q='notApplicable'
_P='unknown'
_O='DisplayString'
_N='none'
_M='enabled'
_L='disabled'
_K='saveDone'
_J='save'
_I='high'
_H='low'
_G='enable'
_F='HMPRIV-MAX-MIB'
_E='disable'
_D='read-write'
_C='read-only'
_B='Integer32'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier',_Z,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_Z,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_O,'PhysAddress','TextualConvention')
_Hirschmann_ObjectIdentity=ObjectIdentity
hirschmann=_Hirschmann_ObjectIdentity((1,3,6,1,4,1,248))
_Max_ObjectIdentity=ObjectIdentity
max=_Max_ObjectIdentity((1,3,6,1,4,1,248,70))
_Basics_ObjectIdentity=ObjectIdentity
basics=_Basics_ObjectIdentity((1,3,6,1,4,1,248,70,1))
_SystemGroup_ObjectIdentity=ObjectIdentity
systemGroup=_SystemGroup_ObjectIdentity((1,3,6,1,4,1,248,70,1,1))
class _SystemName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SystemName_Type.__name__=_O
_SystemName_Object=MibScalar
systemName=_SystemName_Object((1,3,6,1,4,1,248,70,1,1,1),_SystemName_Type())
systemName.setMaxAccess(_C)
if mibBuilder.loadTexts:systemName.setStatus(_A)
class _SystemVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SystemVersion_Type.__name__=_O
_SystemVersion_Object=MibScalar
systemVersion=_SystemVersion_Object((1,3,6,1,4,1,248,70,1,1,2),_SystemVersion_Type())
systemVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:systemVersion.setStatus(_A)
class _SystemFirmwareVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SystemFirmwareVersion_Type.__name__=_O
_SystemFirmwareVersion_Object=MibScalar
systemFirmwareVersion=_SystemFirmwareVersion_Object((1,3,6,1,4,1,248,70,1,1,3),_SystemFirmwareVersion_Type())
systemFirmwareVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:systemFirmwareVersion.setStatus(_A)
_SystemMacAddress_Type=PhysAddress
_SystemMacAddress_Object=MibScalar
systemMacAddress=_SystemMacAddress_Object((1,3,6,1,4,1,248,70,1,1,4),_SystemMacAddress_Type())
systemMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:systemMacAddress.setStatus(_A)
class _DeviceReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('reset',1),('resetDone',2)))
_DeviceReset_Type.__name__=_B
_DeviceReset_Object=MibScalar
deviceReset=_DeviceReset_Object((1,3,6,1,4,1,248,70,1,1,5),_DeviceReset_Type())
deviceReset.setMaxAccess(_D)
if mibBuilder.loadTexts:deviceReset.setStatus(_A)
_SystemUpTime_Type=DisplayString
_SystemUpTime_Object=MibScalar
systemUpTime=_SystemUpTime_Object((1,3,6,1,4,1,248,70,1,1,6),_SystemUpTime_Type())
systemUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:systemUpTime.setStatus(_A)
_SystemLocation_Type=DisplayString
_SystemLocation_Object=MibScalar
systemLocation=_SystemLocation_Object((1,3,6,1,4,1,248,70,1,1,7),_SystemLocation_Type())
systemLocation.setMaxAccess(_D)
if mibBuilder.loadTexts:systemLocation.setStatus(_A)
_SystemContact_Type=DisplayString
_SystemContact_Object=MibScalar
systemContact=_SystemContact_Object((1,3,6,1,4,1,248,70,1,1,8),_SystemContact_Type())
systemContact.setMaxAccess(_D)
if mibBuilder.loadTexts:systemContact.setStatus(_A)
_SysIpAddress_Type=IpAddress
_SysIpAddress_Object=MibScalar
sysIpAddress=_SysIpAddress_Object((1,3,6,1,4,1,248,70,1,1,9),_SysIpAddress_Type())
sysIpAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:sysIpAddress.setStatus(_A)
_SysSubnet_Type=IpAddress
_SysSubnet_Object=MibScalar
sysSubnet=_SysSubnet_Object((1,3,6,1,4,1,248,70,1,1,10),_SysSubnet_Type())
sysSubnet.setMaxAccess(_D)
if mibBuilder.loadTexts:sysSubnet.setStatus(_A)
_SysGateway_Type=IpAddress
_SysGateway_Object=MibScalar
sysGateway=_SysGateway_Object((1,3,6,1,4,1,248,70,1,1,11),_SysGateway_Type())
sysGateway.setMaxAccess(_D)
if mibBuilder.loadTexts:sysGateway.setStatus(_A)
_SysSerial_Type=DisplayString
_SysSerial_Object=MibScalar
sysSerial=_SysSerial_Object((1,3,6,1,4,1,248,70,1,1,12),_SysSerial_Type())
sysSerial.setMaxAccess(_C)
if mibBuilder.loadTexts:sysSerial.setStatus(_A)
_SysOrderCode_Type=DisplayString
_SysOrderCode_Object=MibScalar
sysOrderCode=_SysOrderCode_Object((1,3,6,1,4,1,248,70,1,1,13),_SysOrderCode_Type())
sysOrderCode.setMaxAccess(_C)
if mibBuilder.loadTexts:sysOrderCode.setStatus(_A)
_SysTemperature_Type=Integer32
_SysTemperature_Object=MibScalar
sysTemperature=_SysTemperature_Object((1,3,6,1,4,1,248,70,1,1,14),_SysTemperature_Type())
sysTemperature.setMaxAccess(_C)
if mibBuilder.loadTexts:sysTemperature.setStatus(_A)
class _SysTempUnit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('fahrenheit',1),('celcius',2)))
_SysTempUnit_Type.__name__=_B
_SysTempUnit_Object=MibScalar
sysTempUnit=_SysTempUnit_Object((1,3,6,1,4,1,248,70,1,1,15),_SysTempUnit_Type())
sysTempUnit.setMaxAccess(_D)
if mibBuilder.loadTexts:sysTempUnit.setStatus(_A)
class _SysPS1Status_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_a,1),(_b,2),(_c,3),('Good',4)))
_SysPS1Status_Type.__name__=_B
_SysPS1Status_Object=MibScalar
sysPS1Status=_SysPS1Status_Object((1,3,6,1,4,1,248,70,1,1,16),_SysPS1Status_Type())
sysPS1Status.setMaxAccess(_D)
if mibBuilder.loadTexts:sysPS1Status.setStatus(_A)
class _SysPS2Status_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_a,1),(_b,2),(_c,3),('Good',4)))
_SysPS2Status_Type.__name__=_B
_SysPS2Status_Object=MibScalar
sysPS2Status=_SysPS2Status_Object((1,3,6,1,4,1,248,70,1,1,17),_SysPS2Status_Type())
sysPS2Status.setMaxAccess(_C)
if mibBuilder.loadTexts:sysPS2Status.setStatus(_A)
_SysCPUusage_Type=Integer32
_SysCPUusage_Object=MibScalar
sysCPUusage=_SysCPUusage_Object((1,3,6,1,4,1,248,70,1,1,18),_SysCPUusage_Type())
sysCPUusage.setMaxAccess(_C)
if mibBuilder.loadTexts:sysCPUusage.setStatus(_A)
_SysMemUsage_Type=Integer32
_SysMemUsage_Object=MibScalar
sysMemUsage=_SysMemUsage_Object((1,3,6,1,4,1,248,70,1,1,19),_SysMemUsage_Type())
sysMemUsage.setMaxAccess(_C)
if mibBuilder.loadTexts:sysMemUsage.setStatus(_A)
_SnmpGroup_ObjectIdentity=ObjectIdentity
snmpGroup=_SnmpGroup_ObjectIdentity((1,3,6,1,4,1,248,70,1,2))
class _MibsInfo_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MibsInfo_Type.__name__=_O
_MibsInfo_Object=MibScalar
mibsInfo=_MibsInfo_Object((1,3,6,1,4,1,248,70,1,2,1),_MibsInfo_Type())
mibsInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:mibsInfo.setStatus(_A)
_Switch_ObjectIdentity=ObjectIdentity
switch=_Switch_ObjectIdentity((1,3,6,1,4,1,248,70,12))
_Max25_ObjectIdentity=ObjectIdentity
max25=_Max25_ObjectIdentity((1,3,6,1,4,1,248,70,12,6))
_Generalmx_ObjectIdentity=ObjectIdentity
generalmx=_Generalmx_ObjectIdentity((1,3,6,1,4,1,248,70,12,6,1))
_SlotNumber_Type=Integer32
_SlotNumber_Object=MibScalar
slotNumber=_SlotNumber_Object((1,3,6,1,4,1,248,70,12,6,1,1),_SlotNumber_Type())
slotNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:slotNumber.setStatus(_A)
_PortNumber_Type=Integer32
_PortNumber_Object=MibScalar
portNumber=_PortNumber_Object((1,3,6,1,4,1,248,70,12,6,1,2),_PortNumber_Type())
portNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:portNumber.setStatus(_A)
_SlotTable_Object=MibTable
slotTable=_SlotTable_Object((1,3,6,1,4,1,248,70,12,6,2))
if mibBuilder.loadTexts:slotTable.setStatus(_A)
_SlotEntry_Object=MibTableRow
slotEntry=_SlotEntry_Object((1,3,6,1,4,1,248,70,12,6,2,1))
slotEntry.setIndexNames((0,_F,_d))
if mibBuilder.loadTexts:slotEntry.setStatus(_A)
class _SlotIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_SlotIndex_Type.__name__=_B
_SlotIndex_Object=MibTableColumn
slotIndex=_SlotIndex_Object((1,3,6,1,4,1,248,70,12,6,2,1,1),_SlotIndex_Type())
slotIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:slotIndex.setStatus(_A)
class _SlotName_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('slot1',1),('slot2',2),('slot3',3),('slot4',4),('slot5',5),('slot6',6),('slot7',7),('slot8',8),('slot9',9),('slot10',10)))
_SlotName_Type.__name__=_B
_SlotName_Object=MibTableColumn
slotName=_SlotName_Object((1,3,6,1,4,1,248,70,12,6,2,1,2),_SlotName_Type())
slotName.setMaxAccess(_C)
if mibBuilder.loadTexts:slotName.setStatus(_A)
class _ModuleId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,177,178,179,181,182,184,186,187,188,384,385,386,387,388,389,390,400,401,403,416,417,418,419,420,421,422,423,424,425,426,427,428,429,430,431,432,433,434,435,436,437,438,439,440,441,442,443,444)));namedValues=NamedValues(*((_P,0),('oneGiga',1),('eightTP',2),('fourTPandFour100mbFiber',3),('fourTPandTwo100mbFiber',4),('eight100mbFiber',5),('four100mbFiberandTwo100mbFiber',6),('fourTPandTwo10mbFiber',7),('four100mbFiberandTwo10mbFiber',8),('two10mbFiberandTwo100mbFiber',9),('four10mbFiber',10),('four100mbFiber',11),('twoGiga',12),('sixTPandTwo100mbFiber',13),('sixTPandOne100mbFiber',14),('oneGigaFourTp',15),('oneGigaFour100mbFiber',16),('oneGigaTwoTpTwo100mbFiber',17),('oneGigaTwoTpOne100mbFiber',18),('oneGigaTwo100mbFiber',19),('oneGigaTwo10mbFiber',20),('oneGigaFiveTp',21),('oneGigaOneTpFour100mbFiber',22),('oneGigaThreeTpTwo100mbFiber',23),('oneGigaThreeTpOne100mbFiber',24),('oneGigaOneTpTwo100mbFiber',25),('oneGigaOnetpTwo10mbFiber',26),('oneGigaOne100mbFiberFourTp',27),('oneGigaFive100mbFiber',28),('oneGigaTwoTpThree100mbFiber',29),('oneGigaTwoTpTwo100mbFibeExt',30),('oneGigaThree100mbFiber',31),('oneGigaOne100mbFiberTwo10mbFiber',32),('fixedTPModule',33),('eightTpMdix',34),('fourTpMdixandFour100mbFiber',35),('fourTpMdixandTwo100mbFiber',36),('eight100mbFiberAlt',37),('fourFiber100TwoFiber100Alt',38),('fourTpMdixandTwo10mbFiber',39),('four100mbFiberandTwo10mbFiberAlt',40),('two10mbFiberandTwo100mbFiberAlt',41),('four10mbFiberAlt',42),('four100mbFiberAlt',43),('twoGigaAlt',44),('sixTpMdixandTwo100mbFiber',45),('sixTpMdixandOne100mbFiber',46),('oneGigaFourTpMdix',47),('oneGigaFour100mbFiberAlt',48),('oneGigaTwoTpMdixTwo100mbFiber',49),('oneGigaTwoTpMdixOne100mbFiber',50),('oneGigaTwo100mbFiberAlt',51),('oneGigaTwo10mbFiberAlt',52),('oneGigaFiveTpMdix',53),('oneGigaOneTpMdixFour100mbFiber',54),('oneGigaThreeTpMdixTwo100mbFiber',55),('oneGigaThreeTpMdixOne100mbFiber',56),('oneGigaOneTpMdixTwo100mbFiber',57),('oneGigaOneTpMdixTwo10mbFiber',58),('oneGigaOne100mbFiberFourTpMdix',59),('oneGigaFive100mbFiberAlt',60),('oneGigaTwoTpMdixThree100mbFiber',61),('oneGigaTwoTpMdixTwo100mbFiberExt',62),('oneGigaThree100mbFiberAlt',63),('oneGigaOneFiber100TwoFiber10Alt',64),('oneGiga3SpdTFourTpMdix',65),('oneGiga1000TFourTpMdix',66),('twoGiga3Spd',67),('oneGiga3SpdOneGiga',68),('oneGiga3SpdOneGigaSFP',69),('oneGiga3SpdFour100mbfiber',70),('oneGiga3SpdTwoTpMdixTwoFiber100',71),('oneGiga3SpdTwoTpMdixOneFiber100',72),('oneGiga3SpdTwo100mbfiber',73),('oneGiga3SpdOne10mbfiber',74),('oneGigafourTpMdixPOE',75),('oneGigatwoTpMdixPOEtwoFiber100',76),('one3SpdfourTpMdixPOE',77),('one3SpdtwoTpMdixPOEtwoFiber100',78),('one3SpdtwoTpMdixPOEoneFiber100',79),('eightTpMdixPOE',80),('fourTpMdixPOEfourFiber100',81),('fourTpMdixPOEtwoFiber100',82),('fourTpMdixPOEtwoFiber10',83),('sixTpMdixPOEtwoFiber100',84),('sixTpMdixPOEoneFiber100',85),('one3SpdoneGigaSfp1000',86),('twoGigaSfp1000',87),('one3Spd',88),('oneGigaSfp1000',89),('fourTpMdixPOEfourTpMdix',90),('fourTpMdixPOEtwoTpMdixtwoFiber100',91),('twoTpMdix',92),('threeTpMdixOneFiber100',93),('threeTpMdixPOEoneFiber100',94),('threeFiber100oneTpMdix',95),('fourTpMdix',96),('fourFiber100fourTpMdix',97),('twoFiber100fourTpMdix',98),('fourFiber100',99),('twoFiber100',100),('twoFiber100twoFiber10',101),('fourTPMDIX',102),('fourFIBER100',103),('twoFIBER100',104),('twoFiber10',105),('twoTpMdixtwoFiber100',106),('twoTpMdixoneFiber100',107),('fourTpMdixPOE',108),('twoTpMdixPOEtwoFiber100',109),('twoTpMdixPOEoneFiber100',110),('oneFiber100',111),('oneFiber100fourTpMdix',112),('oneFiber100fourFiber100',113),('oneFiber100twoFiber100',114),('oneFiber100twoFiber10',115),('oneFiber100twoTpMdixtwoFiber100',116),('oneFiber100twoTpMdixoneFiber100',117),('twoFiber100twoTpMdixtwoFiber100',118),('twoFiber100twoTpMdixoneFiber100',119),('fourTPMDIXPOE',120),('oneFiber100threeTpMdix',121),('twoFiber100FourFiber100',122),('fourFiber100twoTPMDIXtwoFiber100',123),('fourFiber100twoTPMDIXoneFiber100',124),('twoTPMDIXfourFiber100',125),('twoFiber10twoTpMDIX',126),('fourFiber10',127),('fourTpMdixIEEE1588',177),('twoGiga3SpdIEEE1588',178),('twoGigaSfpIEEE1588',179),('fourFiber100IEEE1588',181),('fourFiber100SFP',182),('twoFiber100IEEE1588',184),('oneMultimediaIEEE1588',186),('twoMultimediaIEEE1588',187),('fourTPMDIXPOESparePair',188),('sixTpMdix',384),('sevenTpMdixoneFiber100',385),('fiveTpMdixthreeFiber1000',386),('sixTPMdixPOEtwoFiber100',387),('threeTPMdixOneFiber100',388),('threeTPMdixPOEOneFiber100',389),('threeTpMdixOneFiberThreeTpMdixOneFiber',390),('threeTpMDIXOneFiber100',400),('threeTPMdixPoeOneFiber100',401),('fourTpMdixThreeTpMdixPOEOneFiber100',403),('oneGiga3SpdSixTpMdix',416),('oneGiga3SpdFourFiber100TwoTpMdix',417),('oneGiga3SpdTwoFiber100FourTpMdix',418),('oneGiga3SpdOneFiber100FourTpMdix',419),('oneGiga3SpdTwoFiber100TwoTpMdix',420),('oneGiga3SpdTwoFiber10TwoTpMdix',421),('oneGiga3SpdTwoTpMdixFourTpMdixPoe',422),('oneGigaSfpSixTpMdix',423),('oneGigaSfpTwoTpMdixFourFiber100',424),('oneGigaSfpFourTpMdixTwoFiber100',425),('oneGigaSfpFourTpMdixOneFiber100',426),('oneGigaSfpTwoTpMdixTwoFiber100',427),('oneGigaSfpTwoTpMdixTwoFiber10',428),('oneGigaSfpTwoTpMdixFourTpMdixPOE',429),('oneGigaSfpSixFiber100',430),('oneGigaSfpFourFiber100',431),('oneGigaSFPFourTpMdixPOE',432),('fourTpMdixwithIEEE1588',433),('two3SpdwithIEEE1588',434),('twoGigaSfpwithIEEE1588',435),('fourTpMdixPOESlotWise',436),('fourFiber100withIEEE1588',437),('fourFiber100Sfp',438),('fourTpMdixPOEPortWise',439),('twoFiber100withIEEE1588',440),('fourTpMdixPOEPlus',441),('oneMultimediaWithIEEE1588',442),('twoMultimediaWithIEEE1588',443),('fourTpMdixPOESparePair',444)))
_ModuleId_Type.__name__=_B
_ModuleId_Object=MibTableColumn
moduleId=_ModuleId_Object((1,3,6,1,4,1,248,70,12,6,2,1,3),_ModuleId_Type())
moduleId.setMaxAccess(_C)
if mibBuilder.loadTexts:moduleId.setStatus(_A)
_ModuleName_Type=DisplayString
_ModuleName_Object=MibTableColumn
moduleName=_ModuleName_Object((1,3,6,1,4,1,248,70,12,6,2,1,4),_ModuleName_Type())
moduleName.setMaxAccess(_C)
if mibBuilder.loadTexts:moduleName.setStatus(_A)
_PortControl_ObjectIdentity=ObjectIdentity
portControl=_PortControl_ObjectIdentity((1,3,6,1,4,1,248,70,12,6,3))
class _SavePortControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_SavePortControl_Type.__name__=_B
_SavePortControl_Object=MibScalar
savePortControl=_SavePortControl_Object((1,3,6,1,4,1,248,70,12,6,3,1),_SavePortControl_Type())
savePortControl.setMaxAccess(_D)
if mibBuilder.loadTexts:savePortControl.setStatus(_A)
_PortTable_Object=MibTable
portTable=_PortTable_Object((1,3,6,1,4,1,248,70,12,6,3,2))
if mibBuilder.loadTexts:portTable.setStatus(_A)
_PortEntry_Object=MibTableRow
portEntry=_PortEntry_Object((1,3,6,1,4,1,248,70,12,6,3,2,1))
portEntry.setIndexNames((0,_F,_e),(0,_F,_f))
if mibBuilder.loadTexts:portEntry.setStatus(_A)
class _PtSlotIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_PtSlotIndex_Type.__name__=_B
_PtSlotIndex_Object=MibTableColumn
ptSlotIndex=_PtSlotIndex_Object((1,3,6,1,4,1,248,70,12,6,3,2,1,1),_PtSlotIndex_Type())
ptSlotIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ptSlotIndex.setStatus(_A)
class _PtPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_PtPortIndex_Type.__name__=_B
_PtPortIndex_Object=MibTableColumn
ptPortIndex=_PtPortIndex_Object((1,3,6,1,4,1,248,70,12,6,3,2,1,2),_PtPortIndex_Type())
ptPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ptPortIndex.setStatus(_A)
_PtIfIndex_Type=Integer32
_PtIfIndex_Object=MibTableColumn
ptIfIndex=_PtIfIndex_Object((1,3,6,1,4,1,248,70,12,6,3,2,1,3),_PtIfIndex_Type())
ptIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ptIfIndex.setStatus(_A)
_PtPortName_Type=DisplayString
_PtPortName_Object=MibTableColumn
ptPortName=_PtPortName_Object((1,3,6,1,4,1,248,70,12,6,3,2,1,4),_PtPortName_Type())
ptPortName.setMaxAccess(_D)
if mibBuilder.loadTexts:ptPortName.setStatus(_A)
class _PtPortControlStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4)));namedValues=NamedValues(*((_G,1),(_E,2),(_Q,4)))
_PtPortControlStatus_Type.__name__=_B
_PtPortControlStatus_Object=MibTableColumn
ptPortControlStatus=_PtPortControlStatus_Object((1,3,6,1,4,1,248,70,12,6,3,2,1,5),_PtPortControlStatus_Type())
ptPortControlStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:ptPortControlStatus.setStatus(_A)
class _PtPortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_M,1),(_L,2),('locked',3),(_g,4)))
_PtPortStatus_Type.__name__=_B
_PtPortStatus_Object=MibTableColumn
ptPortStatus=_PtPortStatus_Object((1,3,6,1,4,1,248,70,12,6,3,2,1,6),_PtPortStatus_Type())
ptPortStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ptPortStatus.setStatus(_A)
class _PtPortDuplexStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4)));namedValues=NamedValues(*(('halfDuplex',1),('fullDuplex',2),(_Q,4)))
_PtPortDuplexStatus_Type.__name__=_B
_PtPortDuplexStatus_Object=MibTableColumn
ptPortDuplexStatus=_PtPortDuplexStatus_Object((1,3,6,1,4,1,248,70,12,6,3,2,1,7),_PtPortDuplexStatus_Type())
ptPortDuplexStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:ptPortDuplexStatus.setStatus(_A)
class _PtPortMediaType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_g,1),('mediaType10F',2),('mediaType10T',3),('mediaType100Tx',4),('mediaType100Fx',5),('gigabit',6),('gigabitCu',7)))
_PtPortMediaType_Type.__name__=_B
_PtPortMediaType_Object=MibTableColumn
ptPortMediaType=_PtPortMediaType_Object((1,3,6,1,4,1,248,70,12,6,3,2,1,8),_PtPortMediaType_Type())
ptPortMediaType.setMaxAccess(_C)
if mibBuilder.loadTexts:ptPortMediaType.setStatus(_A)
class _PtPortLinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_PtPortLinkStatus_Type.__name__=_B
_PtPortLinkStatus_Object=MibTableColumn
ptPortLinkStatus=_PtPortLinkStatus_Object((1,3,6,1,4,1,248,70,12,6,3,2,1,9),_PtPortLinkStatus_Type())
ptPortLinkStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ptPortLinkStatus.setStatus(_A)
class _PtPortSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('speed10Mbps',1),('speed100Mbps',2),('speed1000Mbps',3),(_Q,4)))
_PtPortSpeed_Type.__name__=_B
_PtPortSpeed_Object=MibTableColumn
ptPortSpeed=_PtPortSpeed_Object((1,3,6,1,4,1,248,70,12,6,3,2,1,10),_PtPortSpeed_Type())
ptPortSpeed.setMaxAccess(_D)
if mibBuilder.loadTexts:ptPortSpeed.setStatus(_A)
class _PtPortPartitionState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4)));namedValues=NamedValues(*(('partitioned',1),('notPartitioned',2),(_Q,4)))
_PtPortPartitionState_Type.__name__=_B
_PtPortPartitionState_Object=MibTableColumn
ptPortPartitionState=_PtPortPartitionState_Object((1,3,6,1,4,1,248,70,12,6,3,2,1,11),_PtPortPartitionState_Type())
ptPortPartitionState.setMaxAccess(_C)
if mibBuilder.loadTexts:ptPortPartitionState.setStatus(_A)
_PtPortTraffic_Type=Integer32
_PtPortTraffic_Object=MibTableColumn
ptPortTraffic=_PtPortTraffic_Object((1,3,6,1,4,1,248,70,12,6,3,2,1,12),_PtPortTraffic_Type())
ptPortTraffic.setMaxAccess(_C)
if mibBuilder.loadTexts:ptPortTraffic.setStatus(_A)
class _PtPortAutoNegotiation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4)));namedValues=NamedValues(*((_G,1),(_E,2),(_Q,4)))
_PtPortAutoNegotiation_Type.__name__=_B
_PtPortAutoNegotiation_Object=MibTableColumn
ptPortAutoNegotiation=_PtPortAutoNegotiation_Object((1,3,6,1,4,1,248,70,12,6,3,2,1,13),_PtPortAutoNegotiation_Type())
ptPortAutoNegotiation.setMaxAccess(_D)
if mibBuilder.loadTexts:ptPortAutoNegotiation.setStatus(_A)
class _PtPortNotify_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_N,0),(_U,1),(_V,2),(_h,3),(_W,4),(_i,5),(_j,6),('all',7)))
_PtPortNotify_Type.__name__=_B
_PtPortNotify_Object=MibTableColumn
ptPortNotify=_PtPortNotify_Object((1,3,6,1,4,1,248,70,12,6,3,2,1,14),_PtPortNotify_Type())
ptPortNotify.setMaxAccess(_D)
if mibBuilder.loadTexts:ptPortNotify.setStatus(_A)
_PortMirroring_ObjectIdentity=ObjectIdentity
portMirroring=_PortMirroring_ObjectIdentity((1,3,6,1,4,1,248,70,12,6,4))
_MonitorPort_Type=Integer32
_MonitorPort_Object=MibScalar
monitorPort=_MonitorPort_Object((1,3,6,1,4,1,248,70,12,6,4,1),_MonitorPort_Type())
monitorPort.setMaxAccess(_D)
if mibBuilder.loadTexts:monitorPort.setStatus(_A)
_SnifferPort_Type=Integer32
_SnifferPort_Object=MibScalar
snifferPort=_SnifferPort_Object((1,3,6,1,4,1,248,70,12,6,4,2),_SnifferPort_Type())
snifferPort.setMaxAccess(_D)
if mibBuilder.loadTexts:snifferPort.setStatus(_A)
class _PortMirroringControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_E,2)))
_PortMirroringControl_Type.__name__=_B
_PortMirroringControl_Object=MibScalar
portMirroringControl=_PortMirroringControl_Object((1,3,6,1,4,1,248,70,12,6,4,3),_PortMirroringControl_Type())
portMirroringControl.setMaxAccess(_D)
if mibBuilder.loadTexts:portMirroringControl.setStatus(_A)
class _SavePortMirroring_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_SavePortMirroring_Type.__name__=_B
_SavePortMirroring_Object=MibScalar
savePortMirroring=_SavePortMirroring_Object((1,3,6,1,4,1,248,70,12,6,4,4),_SavePortMirroring_Type())
savePortMirroring.setMaxAccess(_D)
if mibBuilder.loadTexts:savePortMirroring.setStatus(_A)
_MonitorPortList_Type=DisplayString
_MonitorPortList_Object=MibScalar
monitorPortList=_MonitorPortList_Object((1,3,6,1,4,1,248,70,12,6,4,5),_MonitorPortList_Type())
monitorPortList.setMaxAccess(_D)
if mibBuilder.loadTexts:monitorPortList.setStatus(_A)
_PriorityQueuing_ObjectIdentity=ObjectIdentity
priorityQueuing=_PriorityQueuing_ObjectIdentity((1,3,6,1,4,1,248,70,12,6,5))
class _PriorityQueueControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_E,2)))
_PriorityQueueControl_Type.__name__=_B
_PriorityQueueControl_Object=MibScalar
priorityQueueControl=_PriorityQueueControl_Object((1,3,6,1,4,1,248,70,12,6,5,1),_PriorityQueueControl_Type())
priorityQueueControl.setMaxAccess(_D)
if mibBuilder.loadTexts:priorityQueueControl.setStatus(_A)
class _SavePriorityQueue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_SavePriorityQueue_Type.__name__=_B
_SavePriorityQueue_Object=MibScalar
savePriorityQueue=_SavePriorityQueue_Object((1,3,6,1,4,1,248,70,12,6,5,2),_SavePriorityQueue_Type())
savePriorityQueue.setMaxAccess(_D)
if mibBuilder.loadTexts:savePriorityQueue.setStatus(_A)
_PriorityQueueTable_Object=MibTable
priorityQueueTable=_PriorityQueueTable_Object((1,3,6,1,4,1,248,70,12,6,5,3))
if mibBuilder.loadTexts:priorityQueueTable.setStatus(_A)
_PriorityQueueEntry_Object=MibTableRow
priorityQueueEntry=_PriorityQueueEntry_Object((1,3,6,1,4,1,248,70,12,6,5,3,1))
priorityQueueEntry.setIndexNames((0,_F,_k))
if mibBuilder.loadTexts:priorityQueueEntry.setStatus(_A)
class _PqPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,48))
_PqPortIndex_Type.__name__=_B
_PqPortIndex_Object=MibTableColumn
pqPortIndex=_PqPortIndex_Object((1,3,6,1,4,1,248,70,12,6,5,3,1,1),_PqPortIndex_Type())
pqPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:pqPortIndex.setStatus(_A)
class _PqControlStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_E,2)))
_PqControlStatus_Type.__name__=_B
_PqControlStatus_Object=MibTableColumn
pqControlStatus=_PqControlStatus_Object((1,3,6,1,4,1,248,70,12,6,5,3,1,2),_PqControlStatus_Type())
pqControlStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:pqControlStatus.setStatus(_A)
class _PqDefaultQueue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_H,1),('medium',2),(_l,3),(_I,4),(_N,5)))
_PqDefaultQueue_Type.__name__=_B
_PqDefaultQueue_Object=MibTableColumn
pqDefaultQueue=_PqDefaultQueue_Object((1,3,6,1,4,1,248,70,12,6,5,3,1,3),_PqDefaultQueue_Type())
pqDefaultQueue.setMaxAccess(_D)
if mibBuilder.loadTexts:pqDefaultQueue.setStatus(_A)
class _PriorityForUntaggedPktsOnHighQ_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_m,0),(_n,1),(_o,2),(_p,3),(_q,4),(_r,5),(_s,6),(_t,7)))
_PriorityForUntaggedPktsOnHighQ_Type.__name__=_B
_PriorityForUntaggedPktsOnHighQ_Object=MibTableColumn
priorityForUntaggedPktsOnHighQ=_PriorityForUntaggedPktsOnHighQ_Object((1,3,6,1,4,1,248,70,12,6,5,3,1,4),_PriorityForUntaggedPktsOnHighQ_Type())
priorityForUntaggedPktsOnHighQ.setMaxAccess(_D)
if mibBuilder.loadTexts:priorityForUntaggedPktsOnHighQ.setStatus(_A)
class _PriorityForUntaggedPktsOnLowQ_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_m,0),(_n,1),(_o,2),(_p,3),(_q,4),(_r,5),(_s,6),(_t,7)))
_PriorityForUntaggedPktsOnLowQ_Type.__name__=_B
_PriorityForUntaggedPktsOnLowQ_Object=MibTableColumn
priorityForUntaggedPktsOnLowQ=_PriorityForUntaggedPktsOnLowQ_Object((1,3,6,1,4,1,248,70,12,6,5,3,1,5),_PriorityForUntaggedPktsOnLowQ_Type())
priorityForUntaggedPktsOnLowQ.setMaxAccess(_D)
if mibBuilder.loadTexts:priorityForUntaggedPktsOnLowQ.setStatus(_A)
class _QForPktsWithPriority0_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_QForPktsWithPriority0_Type.__name__=_B
_QForPktsWithPriority0_Object=MibTableColumn
qForPktsWithPriority0=_QForPktsWithPriority0_Object((1,3,6,1,4,1,248,70,12,6,5,3,1,6),_QForPktsWithPriority0_Type())
qForPktsWithPriority0.setMaxAccess(_D)
if mibBuilder.loadTexts:qForPktsWithPriority0.setStatus(_A)
class _QForPktsWithPriority1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_QForPktsWithPriority1_Type.__name__=_B
_QForPktsWithPriority1_Object=MibTableColumn
qForPktsWithPriority1=_QForPktsWithPriority1_Object((1,3,6,1,4,1,248,70,12,6,5,3,1,7),_QForPktsWithPriority1_Type())
qForPktsWithPriority1.setMaxAccess(_D)
if mibBuilder.loadTexts:qForPktsWithPriority1.setStatus(_A)
class _QForPktsWithPriority2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_QForPktsWithPriority2_Type.__name__=_B
_QForPktsWithPriority2_Object=MibTableColumn
qForPktsWithPriority2=_QForPktsWithPriority2_Object((1,3,6,1,4,1,248,70,12,6,5,3,1,8),_QForPktsWithPriority2_Type())
qForPktsWithPriority2.setMaxAccess(_D)
if mibBuilder.loadTexts:qForPktsWithPriority2.setStatus(_A)
class _QForPktsWithPriority3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_QForPktsWithPriority3_Type.__name__=_B
_QForPktsWithPriority3_Object=MibTableColumn
qForPktsWithPriority3=_QForPktsWithPriority3_Object((1,3,6,1,4,1,248,70,12,6,5,3,1,9),_QForPktsWithPriority3_Type())
qForPktsWithPriority3.setMaxAccess(_D)
if mibBuilder.loadTexts:qForPktsWithPriority3.setStatus(_A)
class _QForPktsWithPriority4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_QForPktsWithPriority4_Type.__name__=_B
_QForPktsWithPriority4_Object=MibTableColumn
qForPktsWithPriority4=_QForPktsWithPriority4_Object((1,3,6,1,4,1,248,70,12,6,5,3,1,10),_QForPktsWithPriority4_Type())
qForPktsWithPriority4.setMaxAccess(_D)
if mibBuilder.loadTexts:qForPktsWithPriority4.setStatus(_A)
class _QForPktsWithPriority5_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_QForPktsWithPriority5_Type.__name__=_B
_QForPktsWithPriority5_Object=MibTableColumn
qForPktsWithPriority5=_QForPktsWithPriority5_Object((1,3,6,1,4,1,248,70,12,6,5,3,1,11),_QForPktsWithPriority5_Type())
qForPktsWithPriority5.setMaxAccess(_D)
if mibBuilder.loadTexts:qForPktsWithPriority5.setStatus(_A)
class _QForPktsWithPriority6_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_QForPktsWithPriority6_Type.__name__=_B
_QForPktsWithPriority6_Object=MibTableColumn
qForPktsWithPriority6=_QForPktsWithPriority6_Object((1,3,6,1,4,1,248,70,12,6,5,3,1,12),_QForPktsWithPriority6_Type())
qForPktsWithPriority6.setMaxAccess(_D)
if mibBuilder.loadTexts:qForPktsWithPriority6.setStatus(_A)
class _QForPktsWithPriority7_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_QForPktsWithPriority7_Type.__name__=_B
_QForPktsWithPriority7_Object=MibTableColumn
qForPktsWithPriority7=_QForPktsWithPriority7_Object((1,3,6,1,4,1,248,70,12,6,5,3,1,13),_QForPktsWithPriority7_Type())
qForPktsWithPriority7.setMaxAccess(_D)
if mibBuilder.loadTexts:qForPktsWithPriority7.setStatus(_A)
_Layer3Qos_ObjectIdentity=ObjectIdentity
layer3Qos=_Layer3Qos_ObjectIdentity((1,3,6,1,4,1,248,70,12,6,6))
class _Layer3QosControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_E,2)))
_Layer3QosControl_Type.__name__=_B
_Layer3QosControl_Object=MibScalar
layer3QosControl=_Layer3QosControl_Object((1,3,6,1,4,1,248,70,12,6,6,1),_Layer3QosControl_Type())
layer3QosControl.setMaxAccess(_D)
if mibBuilder.loadTexts:layer3QosControl.setStatus(_A)
class _Savelayer3Qos_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_Savelayer3Qos_Type.__name__=_B
_Savelayer3Qos_Object=MibScalar
savelayer3Qos=_Savelayer3Qos_Object((1,3,6,1,4,1,248,70,12,6,6,2),_Savelayer3Qos_Type())
savelayer3Qos.setMaxAccess(_D)
if mibBuilder.loadTexts:savelayer3Qos.setStatus(_A)
_Layer3QosPortTable_Object=MibTable
layer3QosPortTable=_Layer3QosPortTable_Object((1,3,6,1,4,1,248,70,12,6,6,3))
if mibBuilder.loadTexts:layer3QosPortTable.setStatus(_A)
_Layer3QosPortEntry_Object=MibTableRow
layer3QosPortEntry=_Layer3QosPortEntry_Object((1,3,6,1,4,1,248,70,12,6,6,3,1))
layer3QosPortEntry.setIndexNames((0,_F,_u))
if mibBuilder.loadTexts:layer3QosPortEntry.setStatus(_A)
class _L3qptPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,48))
_L3qptPortIndex_Type.__name__=_B
_L3qptPortIndex_Object=MibTableColumn
l3qptPortIndex=_L3qptPortIndex_Object((1,3,6,1,4,1,248,70,12,6,6,3,1,1),_L3qptPortIndex_Type())
l3qptPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:l3qptPortIndex.setStatus(_A)
class _L3QosControlStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_E,2)))
_L3QosControlStatus_Type.__name__=_B
_L3QosControlStatus_Object=MibTableColumn
l3QosControlStatus=_L3QosControlStatus_Object((1,3,6,1,4,1,248,70,12,6,6,3,1,2),_L3QosControlStatus_Type())
l3QosControlStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:l3QosControlStatus.setStatus(_A)
_Layer3QosQueueTable_Object=MibTable
layer3QosQueueTable=_Layer3QosQueueTable_Object((1,3,6,1,4,1,248,70,12,6,6,4))
if mibBuilder.loadTexts:layer3QosQueueTable.setStatus(_A)
_Layer3QosQueueEntry_Object=MibTableRow
layer3QosQueueEntry=_Layer3QosQueueEntry_Object((1,3,6,1,4,1,248,70,12,6,6,4,1))
layer3QosQueueEntry.setIndexNames((0,_F,_v),(0,_F,_w))
if mibBuilder.loadTexts:layer3QosQueueEntry.setStatus(_A)
class _L3qqtPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,48))
_L3qqtPortIndex_Type.__name__=_B
_L3qqtPortIndex_Object=MibTableColumn
l3qqtPortIndex=_L3qqtPortIndex_Object((1,3,6,1,4,1,248,70,12,6,6,4,1,1),_L3qqtPortIndex_Type())
l3qqtPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:l3qqtPortIndex.setStatus(_A)
class _L3qqtDscpIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_L3qqtDscpIndex_Type.__name__=_B
_L3qqtDscpIndex_Object=MibTableColumn
l3qqtDscpIndex=_L3qqtDscpIndex_Object((1,3,6,1,4,1,248,70,12,6,6,4,1,2),_L3qqtDscpIndex_Type())
l3qqtDscpIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:l3qqtDscpIndex.setStatus(_A)
class _L3qqtQueueValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_L3qqtQueueValue_Type.__name__=_B
_L3qqtQueueValue_Object=MibTableColumn
l3qqtQueueValue=_L3qqtQueueValue_Object((1,3,6,1,4,1,248,70,12,6,6,4,1,3),_L3qqtQueueValue_Type())
l3qqtQueueValue.setMaxAccess(_D)
if mibBuilder.loadTexts:l3qqtQueueValue.setStatus(_A)
_PortSecurity_ObjectIdentity=ObjectIdentity
portSecurity=_PortSecurity_ObjectIdentity((1,3,6,1,4,1,248,70,12,6,7))
class _PortSecurityControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_E,2)))
_PortSecurityControl_Type.__name__=_B
_PortSecurityControl_Object=MibScalar
portSecurityControl=_PortSecurityControl_Object((1,3,6,1,4,1,248,70,12,6,7,1),_PortSecurityControl_Type())
portSecurityControl.setMaxAccess(_D)
if mibBuilder.loadTexts:portSecurityControl.setStatus(_A)
class _SaveportSecurity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_SaveportSecurity_Type.__name__=_B
_SaveportSecurity_Object=MibScalar
saveportSecurity=_SaveportSecurity_Object((1,3,6,1,4,1,248,70,12,6,7,2),_SaveportSecurity_Type())
saveportSecurity.setMaxAccess(_D)
if mibBuilder.loadTexts:saveportSecurity.setStatus(_A)
_PortSecurityTable_Object=MibTable
portSecurityTable=_PortSecurityTable_Object((1,3,6,1,4,1,248,70,12,6,7,3))
if mibBuilder.loadTexts:portSecurityTable.setStatus(_A)
_PortSecurityEntry_Object=MibTableRow
portSecurityEntry=_PortSecurityEntry_Object((1,3,6,1,4,1,248,70,12,6,7,3,1))
portSecurityEntry.setIndexNames((0,_F,_x),(0,_F,_y))
if mibBuilder.loadTexts:portSecurityEntry.setStatus(_A)
class _PsPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,48))
_PsPortIndex_Type.__name__=_B
_PsPortIndex_Object=MibTableColumn
psPortIndex=_PsPortIndex_Object((1,3,6,1,4,1,248,70,12,6,7,3,1,1),_PsPortIndex_Type())
psPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:psPortIndex.setStatus(_A)
class _PsEntryIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,500))
_PsEntryIndex_Type.__name__=_B
_PsEntryIndex_Object=MibTableColumn
psEntryIndex=_PsEntryIndex_Object((1,3,6,1,4,1,248,70,12,6,7,3,1,2),_PsEntryIndex_Type())
psEntryIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:psEntryIndex.setStatus(_A)
_PsMacAddress_Type=PhysAddress
_PsMacAddress_Object=MibTableColumn
psMacAddress=_PsMacAddress_Object((1,3,6,1,4,1,248,70,12,6,7,3,1,3),_PsMacAddress_Type())
psMacAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:psMacAddress.setStatus(_A)
class _PsEntryStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('include',1),('exclude',2)))
_PsEntryStatus_Type.__name__=_B
_PsEntryStatus_Object=MibTableColumn
psEntryStatus=_PsEntryStatus_Object((1,3,6,1,4,1,248,70,12,6,7,3,1,4),_PsEntryStatus_Type())
psEntryStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:psEntryStatus.setStatus(_A)
_ActionSignalTable_Object=MibTable
actionSignalTable=_ActionSignalTable_Object((1,3,6,1,4,1,248,70,12,6,7,4))
if mibBuilder.loadTexts:actionSignalTable.setStatus(_A)
_ActionSignalEntry_Object=MibTableRow
actionSignalEntry=_ActionSignalEntry_Object((1,3,6,1,4,1,248,70,12,6,7,4,1))
actionSignalEntry.setIndexNames((0,_F,_z))
if mibBuilder.loadTexts:actionSignalEntry.setStatus(_A)
class _AtPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,48))
_AtPortIndex_Type.__name__=_B
_AtPortIndex_Object=MibTableColumn
atPortIndex=_AtPortIndex_Object((1,3,6,1,4,1,248,70,12,6,7,4,1,1),_AtPortIndex_Type())
atPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:atPortIndex.setStatus(_A)
class _AtAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),('drop',2),(_N,3)))
_AtAction_Type.__name__=_B
_AtAction_Object=MibTableColumn
atAction=_AtAction_Object((1,3,6,1,4,1,248,70,12,6,7,4,1,2),_AtAction_Type())
atAction.setMaxAccess(_D)
if mibBuilder.loadTexts:atAction.setStatus(_A)
class _AtSignal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_U,1),(_V,2),('log-and-trap',3),(_N,4)))
_AtSignal_Type.__name__=_B
_AtSignal_Object=MibTableColumn
atSignal=_AtSignal_Object((1,3,6,1,4,1,248,70,12,6,7,4,1,3),_AtSignal_Type())
atSignal.setMaxAccess(_D)
if mibBuilder.loadTexts:atSignal.setStatus(_A)
class _AtLearnMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_E,2)))
_AtLearnMode_Type.__name__=_B
_AtLearnMode_Object=MibTableColumn
atLearnMode=_AtLearnMode_Object((1,3,6,1,4,1,248,70,12,6,7,4,1,4),_AtLearnMode_Type())
atLearnMode.setMaxAccess(_D)
if mibBuilder.loadTexts:atLearnMode.setStatus(_A)
_Vlan_ObjectIdentity=ObjectIdentity
vlan=_Vlan_ObjectIdentity((1,3,6,1,4,1,248,70,12,6,8))
class _VlanType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3,4)));namedValues=NamedValues(*((_A0,1),(_A1,3),(_N,4)))
_VlanType_Type.__name__=_B
_VlanType_Object=MibScalar
vlanType=_VlanType_Object((1,3,6,1,4,1,248,70,12,6,8,1),_VlanType_Type())
vlanType.setMaxAccess(_D)
if mibBuilder.loadTexts:vlanType.setStatus(_A)
_PortBasedVLAN_ObjectIdentity=ObjectIdentity
portBasedVLAN=_PortBasedVLAN_ObjectIdentity((1,3,6,1,4,1,248,70,12,6,8,2))
_MaxPVLAN_Type=Integer32
_MaxPVLAN_Object=MibScalar
maxPVLAN=_MaxPVLAN_Object((1,3,6,1,4,1,248,70,12,6,8,2,1),_MaxPVLAN_Type())
maxPVLAN.setMaxAccess(_C)
if mibBuilder.loadTexts:maxPVLAN.setStatus(_A)
_PvlansCreated_Type=Integer32
_PvlansCreated_Object=MibScalar
pvlansCreated=_PvlansCreated_Object((1,3,6,1,4,1,248,70,12,6,8,2,2),_PvlansCreated_Type())
pvlansCreated.setMaxAccess(_C)
if mibBuilder.loadTexts:pvlansCreated.setStatus(_A)
class _Savepvlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_Savepvlan_Type.__name__=_B
_Savepvlan_Object=MibScalar
savepvlan=_Savepvlan_Object((1,3,6,1,4,1,248,70,12,6,8,2,3),_Savepvlan_Type())
savepvlan.setMaxAccess(_D)
if mibBuilder.loadTexts:savepvlan.setStatus(_A)
class _PvlanControlStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('start',1),('stop',2)))
_PvlanControlStatus_Type.__name__=_B
_PvlanControlStatus_Object=MibScalar
pvlanControlStatus=_PvlanControlStatus_Object((1,3,6,1,4,1,248,70,12,6,8,2,4),_PvlanControlStatus_Type())
pvlanControlStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:pvlanControlStatus.setStatus(_A)
_PvlanTable_Object=MibTable
pvlanTable=_PvlanTable_Object((1,3,6,1,4,1,248,70,12,6,8,2,5))
if mibBuilder.loadTexts:pvlanTable.setStatus(_A)
_PvlanEntry_Object=MibTableRow
pvlanEntry=_PvlanEntry_Object((1,3,6,1,4,1,248,70,12,6,8,2,5,1))
pvlanEntry.setIndexNames((0,_F,_A2))
if mibBuilder.loadTexts:pvlanEntry.setStatus(_A)
class _PvlanIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,48))
_PvlanIndex_Type.__name__=_B
_PvlanIndex_Object=MibTableColumn
pvlanIndex=_PvlanIndex_Object((1,3,6,1,4,1,248,70,12,6,8,2,5,1,1),_PvlanIndex_Type())
pvlanIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:pvlanIndex.setStatus(_A)
_PvlanName_Type=DisplayString
_PvlanName_Object=MibTableColumn
pvlanName=_PvlanName_Object((1,3,6,1,4,1,248,70,12,6,8,2,5,1,2),_PvlanName_Type())
pvlanName.setMaxAccess(_D)
if mibBuilder.loadTexts:pvlanName.setStatus(_A)
_PvlanPortList_Type=DisplayString
_PvlanPortList_Object=MibTableColumn
pvlanPortList=_PvlanPortList_Object((1,3,6,1,4,1,248,70,12,6,8,2,5,1,3),_PvlanPortList_Type())
pvlanPortList.setMaxAccess(_D)
if mibBuilder.loadTexts:pvlanPortList.setStatus(_A)
class _PvlanEntryStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),(_E,2),(_R,3),('create',4)))
_PvlanEntryStatus_Type.__name__=_B
_PvlanEntryStatus_Object=MibTableColumn
pvlanEntryStatus=_PvlanEntryStatus_Object((1,3,6,1,4,1,248,70,12,6,8,2,5,1,4),_PvlanEntryStatus_Type())
pvlanEntryStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:pvlanEntryStatus.setStatus(_A)
_TagBasedVLAN_ObjectIdentity=ObjectIdentity
tagBasedVLAN=_TagBasedVLAN_ObjectIdentity((1,3,6,1,4,1,248,70,12,6,8,4))
_MaxTVLAN_Type=Integer32
_MaxTVLAN_Object=MibScalar
maxTVLAN=_MaxTVLAN_Object((1,3,6,1,4,1,248,70,12,6,8,4,1),_MaxTVLAN_Type())
maxTVLAN.setMaxAccess(_C)
if mibBuilder.loadTexts:maxTVLAN.setStatus(_A)
_TvlansCreated_Type=Integer32
_TvlansCreated_Object=MibScalar
tvlansCreated=_TvlansCreated_Object((1,3,6,1,4,1,248,70,12,6,8,4,2),_TvlansCreated_Type())
tvlansCreated.setMaxAccess(_C)
if mibBuilder.loadTexts:tvlansCreated.setStatus(_A)
class _Savetvlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_Savetvlan_Type.__name__=_B
_Savetvlan_Object=MibScalar
savetvlan=_Savetvlan_Object((1,3,6,1,4,1,248,70,12,6,8,4,3),_Savetvlan_Type())
savetvlan.setMaxAccess(_D)
if mibBuilder.loadTexts:savetvlan.setStatus(_A)
class _TvlanControlStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('start',1),('stop',2)))
_TvlanControlStatus_Type.__name__=_B
_TvlanControlStatus_Object=MibScalar
tvlanControlStatus=_TvlanControlStatus_Object((1,3,6,1,4,1,248,70,12,6,8,4,4),_TvlanControlStatus_Type())
tvlanControlStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:tvlanControlStatus.setStatus(_A)
_TvlanTable_Object=MibTable
tvlanTable=_TvlanTable_Object((1,3,6,1,4,1,248,70,12,6,8,4,5))
if mibBuilder.loadTexts:tvlanTable.setStatus(_A)
_TvlanEntry_Object=MibTableRow
tvlanEntry=_TvlanEntry_Object((1,3,6,1,4,1,248,70,12,6,8,4,5,1))
tvlanEntry.setIndexNames((0,_F,_A3))
if mibBuilder.loadTexts:tvlanEntry.setStatus(_A)
class _TvlanIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_TvlanIndex_Type.__name__=_B
_TvlanIndex_Object=MibTableColumn
tvlanIndex=_TvlanIndex_Object((1,3,6,1,4,1,248,70,12,6,8,4,5,1,1),_TvlanIndex_Type())
tvlanIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:tvlanIndex.setStatus(_A)
_TvlanName_Type=DisplayString
_TvlanName_Object=MibTableColumn
tvlanName=_TvlanName_Object((1,3,6,1,4,1,248,70,12,6,8,4,5,1,2),_TvlanName_Type())
tvlanName.setMaxAccess(_D)
if mibBuilder.loadTexts:tvlanName.setStatus(_A)
_TvlanPortList_Type=DisplayString
_TvlanPortList_Object=MibTableColumn
tvlanPortList=_TvlanPortList_Object((1,3,6,1,4,1,248,70,12,6,8,4,5,1,3),_TvlanPortList_Type())
tvlanPortList.setMaxAccess(_D)
if mibBuilder.loadTexts:tvlanPortList.setStatus(_A)
_TvlanEgressRules_Type=DisplayString
_TvlanEgressRules_Object=MibTableColumn
tvlanEgressRules=_TvlanEgressRules_Object((1,3,6,1,4,1,248,70,12,6,8,4,5,1,4),_TvlanEgressRules_Type())
tvlanEgressRules.setMaxAccess(_D)
if mibBuilder.loadTexts:tvlanEgressRules.setStatus(_A)
class _TvlanEntryStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),(_E,2),(_R,3),('create',4)))
_TvlanEntryStatus_Type.__name__=_B
_TvlanEntryStatus_Object=MibTableColumn
tvlanEntryStatus=_TvlanEntryStatus_Object((1,3,6,1,4,1,248,70,12,6,8,4,5,1,5),_TvlanEntryStatus_Type())
tvlanEntryStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:tvlanEntryStatus.setStatus(_A)
_IngressTable_Object=MibTable
ingressTable=_IngressTable_Object((1,3,6,1,4,1,248,70,12,6,8,4,6))
if mibBuilder.loadTexts:ingressTable.setStatus(_A)
_IngressEntry_Object=MibTableRow
ingressEntry=_IngressEntry_Object((1,3,6,1,4,1,248,70,12,6,8,4,6,1))
ingressEntry.setIndexNames((0,_F,_A4))
if mibBuilder.loadTexts:ingressEntry.setStatus(_A)
class _PortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,48))
_PortIndex_Type.__name__=_B
_PortIndex_Object=MibTableColumn
portIndex=_PortIndex_Object((1,3,6,1,4,1,248,70,12,6,8,4,6,1,1),_PortIndex_Type())
portIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:portIndex.setStatus(_A)
_PortDefaultId_Type=Integer32
_PortDefaultId_Object=MibTableColumn
portDefaultId=_PortDefaultId_Object((1,3,6,1,4,1,248,70,12,6,8,4,6,1,2),_PortDefaultId_Type())
portDefaultId.setMaxAccess(_D)
if mibBuilder.loadTexts:portDefaultId.setStatus(_A)
class _InCheck_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_G,1)))
_InCheck_Type.__name__=_B
_InCheck_Object=MibTableColumn
inCheck=_InCheck_Object((1,3,6,1,4,1,248,70,12,6,8,4,6,1,3),_InCheck_Type())
inCheck.setMaxAccess(_D)
if mibBuilder.loadTexts:inCheck.setStatus(_A)
_MagnumStpGroup_ObjectIdentity=ObjectIdentity
magnumStpGroup=_MagnumStpGroup_ObjectIdentity((1,3,6,1,4,1,248,70,12,6,9))
_MagnumBrStpTable_Object=MibTable
magnumBrStpTable=_MagnumBrStpTable_Object((1,3,6,1,4,1,248,70,12,6,9,1))
if mibBuilder.loadTexts:magnumBrStpTable.setStatus(_A)
_MagnumBrStpEntry_Object=MibTableRow
magnumBrStpEntry=_MagnumBrStpEntry_Object((1,3,6,1,4,1,248,70,12,6,9,1,1))
magnumBrStpEntry.setIndexNames((0,_F,_A5))
if mibBuilder.loadTexts:magnumBrStpEntry.setStatus(_A)
class _MagnumBrStpIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
_MagnumBrStpIndex_Type.__name__=_B
_MagnumBrStpIndex_Object=MibTableColumn
magnumBrStpIndex=_MagnumBrStpIndex_Object((1,3,6,1,4,1,248,70,12,6,9,1,1,1),_MagnumBrStpIndex_Type())
magnumBrStpIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:magnumBrStpIndex.setStatus(_A)
_MagnumBrStpDesignatedRoot_Type=DisplayString
_MagnumBrStpDesignatedRoot_Object=MibTableColumn
magnumBrStpDesignatedRoot=_MagnumBrStpDesignatedRoot_Object((1,3,6,1,4,1,248,70,12,6,9,1,1,2),_MagnumBrStpDesignatedRoot_Type())
magnumBrStpDesignatedRoot.setMaxAccess(_C)
if mibBuilder.loadTexts:magnumBrStpDesignatedRoot.setStatus(_A)
_MagnumBrStpRootPathCost_Type=Integer32
_MagnumBrStpRootPathCost_Object=MibTableColumn
magnumBrStpRootPathCost=_MagnumBrStpRootPathCost_Object((1,3,6,1,4,1,248,70,12,6,9,1,1,3),_MagnumBrStpRootPathCost_Type())
magnumBrStpRootPathCost.setMaxAccess(_C)
if mibBuilder.loadTexts:magnumBrStpRootPathCost.setStatus(_A)
_MagnumBrStpRootPort_Type=Integer32
_MagnumBrStpRootPort_Object=MibTableColumn
magnumBrStpRootPort=_MagnumBrStpRootPort_Object((1,3,6,1,4,1,248,70,12,6,9,1,1,4),_MagnumBrStpRootPort_Type())
magnumBrStpRootPort.setMaxAccess(_C)
if mibBuilder.loadTexts:magnumBrStpRootPort.setStatus(_A)
class _MagnumBrStpRootBridgeMaxAge_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,30))
_MagnumBrStpRootBridgeMaxAge_Type.__name__=_B
_MagnumBrStpRootBridgeMaxAge_Object=MibTableColumn
magnumBrStpRootBridgeMaxAge=_MagnumBrStpRootBridgeMaxAge_Object((1,3,6,1,4,1,248,70,12,6,9,1,1,5),_MagnumBrStpRootBridgeMaxAge_Type())
magnumBrStpRootBridgeMaxAge.setMaxAccess(_C)
if mibBuilder.loadTexts:magnumBrStpRootBridgeMaxAge.setStatus(_A)
class _MagnumBrStpRootBridgeHelloTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_MagnumBrStpRootBridgeHelloTime_Type.__name__=_B
_MagnumBrStpRootBridgeHelloTime_Object=MibTableColumn
magnumBrStpRootBridgeHelloTime=_MagnumBrStpRootBridgeHelloTime_Object((1,3,6,1,4,1,248,70,12,6,9,1,1,6),_MagnumBrStpRootBridgeHelloTime_Type())
magnumBrStpRootBridgeHelloTime.setMaxAccess(_C)
if mibBuilder.loadTexts:magnumBrStpRootBridgeHelloTime.setStatus(_A)
class _MagnumBrStpRootBridgeFwdDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,30))
_MagnumBrStpRootBridgeFwdDelay_Type.__name__=_B
_MagnumBrStpRootBridgeFwdDelay_Object=MibTableColumn
magnumBrStpRootBridgeFwdDelay=_MagnumBrStpRootBridgeFwdDelay_Object((1,3,6,1,4,1,248,70,12,6,9,1,1,7),_MagnumBrStpRootBridgeFwdDelay_Type())
magnumBrStpRootBridgeFwdDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:magnumBrStpRootBridgeFwdDelay.setStatus(_A)
_MagnumBrStpBridgeId_Type=DisplayString
_MagnumBrStpBridgeId_Object=MibTableColumn
magnumBrStpBridgeId=_MagnumBrStpBridgeId_Object((1,3,6,1,4,1,248,70,12,6,9,1,1,8),_MagnumBrStpBridgeId_Type())
magnumBrStpBridgeId.setMaxAccess(_C)
if mibBuilder.loadTexts:magnumBrStpBridgeId.setStatus(_A)
_MagnumBrStpBridgeMaxAge_Type=Integer32
_MagnumBrStpBridgeMaxAge_Object=MibTableColumn
magnumBrStpBridgeMaxAge=_MagnumBrStpBridgeMaxAge_Object((1,3,6,1,4,1,248,70,12,6,9,1,1,9),_MagnumBrStpBridgeMaxAge_Type())
magnumBrStpBridgeMaxAge.setMaxAccess(_D)
if mibBuilder.loadTexts:magnumBrStpBridgeMaxAge.setStatus(_A)
_MagnumBrStpBridgeHelloTime_Type=Integer32
_MagnumBrStpBridgeHelloTime_Object=MibTableColumn
magnumBrStpBridgeHelloTime=_MagnumBrStpBridgeHelloTime_Object((1,3,6,1,4,1,248,70,12,6,9,1,1,10),_MagnumBrStpBridgeHelloTime_Type())
magnumBrStpBridgeHelloTime.setMaxAccess(_D)
if mibBuilder.loadTexts:magnumBrStpBridgeHelloTime.setStatus(_A)
_MagnumBrStpBridgeFwdDelay_Type=Integer32
_MagnumBrStpBridgeFwdDelay_Object=MibTableColumn
magnumBrStpBridgeFwdDelay=_MagnumBrStpBridgeFwdDelay_Object((1,3,6,1,4,1,248,70,12,6,9,1,1,11),_MagnumBrStpBridgeFwdDelay_Type())
magnumBrStpBridgeFwdDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:magnumBrStpBridgeFwdDelay.setStatus(_A)
class _MagnumBrStpTopChangeDetected_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_S,0),(_T,1)))
_MagnumBrStpTopChangeDetected_Type.__name__=_B
_MagnumBrStpTopChangeDetected_Object=MibTableColumn
magnumBrStpTopChangeDetected=_MagnumBrStpTopChangeDetected_Object((1,3,6,1,4,1,248,70,12,6,9,1,1,12),_MagnumBrStpTopChangeDetected_Type())
magnumBrStpTopChangeDetected.setMaxAccess(_C)
if mibBuilder.loadTexts:magnumBrStpTopChangeDetected.setStatus(_A)
class _MagnumBrStpTopChange_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_S,0),(_T,1)))
_MagnumBrStpTopChange_Type.__name__=_B
_MagnumBrStpTopChange_Object=MibTableColumn
magnumBrStpTopChange=_MagnumBrStpTopChange_Object((1,3,6,1,4,1,248,70,12,6,9,1,1,13),_MagnumBrStpTopChange_Type())
magnumBrStpTopChange.setMaxAccess(_C)
if mibBuilder.loadTexts:magnumBrStpTopChange.setStatus(_A)
_MagnumBrStpHoldTime_Type=Integer32
_MagnumBrStpHoldTime_Object=MibTableColumn
magnumBrStpHoldTime=_MagnumBrStpHoldTime_Object((1,3,6,1,4,1,248,70,12,6,9,1,1,14),_MagnumBrStpHoldTime_Type())
magnumBrStpHoldTime.setMaxAccess(_C)
if mibBuilder.loadTexts:magnumBrStpHoldTime.setStatus(_A)
class _MagnumBrStpAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_L,2)))
_MagnumBrStpAdminStatus_Type.__name__=_B
_MagnumBrStpAdminStatus_Object=MibTableColumn
magnumBrStpAdminStatus=_MagnumBrStpAdminStatus_Object((1,3,6,1,4,1,248,70,12,6,9,1,1,15),_MagnumBrStpAdminStatus_Type())
magnumBrStpAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:magnumBrStpAdminStatus.setStatus(_A)
_MagnumStpPortTable_Object=MibTable
magnumStpPortTable=_MagnumStpPortTable_Object((1,3,6,1,4,1,248,70,12,6,9,2))
if mibBuilder.loadTexts:magnumStpPortTable.setStatus(_A)
_MagnumStpPortEntry_Object=MibTableRow
magnumStpPortEntry=_MagnumStpPortEntry_Object((1,3,6,1,4,1,248,70,12,6,9,2,1))
magnumStpPortEntry.setIndexNames((0,_F,_A6))
if mibBuilder.loadTexts:magnumStpPortEntry.setStatus(_A)
class _MagnumStpPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,48))
_MagnumStpPort_Type.__name__=_B
_MagnumStpPort_Object=MibTableColumn
magnumStpPort=_MagnumStpPort_Object((1,3,6,1,4,1,248,70,12,6,9,2,1,1),_MagnumStpPort_Type())
magnumStpPort.setMaxAccess(_C)
if mibBuilder.loadTexts:magnumStpPort.setStatus(_A)
class _MagnumStpPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_L,0),(_A7,1),(_X,2),(_A8,3),('blocking',4)))
_MagnumStpPortState_Type.__name__=_B
_MagnumStpPortState_Object=MibTableColumn
magnumStpPortState=_MagnumStpPortState_Object((1,3,6,1,4,1,248,70,12,6,9,2,1,2),_MagnumStpPortState_Type())
magnumStpPortState.setMaxAccess(_C)
if mibBuilder.loadTexts:magnumStpPortState.setStatus(_A)
_MagnumStpPortPathCost_Type=Integer32
_MagnumStpPortPathCost_Object=MibTableColumn
magnumStpPortPathCost=_MagnumStpPortPathCost_Object((1,3,6,1,4,1,248,70,12,6,9,2,1,3),_MagnumStpPortPathCost_Type())
magnumStpPortPathCost.setMaxAccess(_D)
if mibBuilder.loadTexts:magnumStpPortPathCost.setStatus(_A)
_MagnumStpPortDesignatedRoot_Type=DisplayString
_MagnumStpPortDesignatedRoot_Object=MibTableColumn
magnumStpPortDesignatedRoot=_MagnumStpPortDesignatedRoot_Object((1,3,6,1,4,1,248,70,12,6,9,2,1,4),_MagnumStpPortDesignatedRoot_Type())
magnumStpPortDesignatedRoot.setMaxAccess(_C)
if mibBuilder.loadTexts:magnumStpPortDesignatedRoot.setStatus(_A)
_MagnumStpPortDesignatedCost_Type=Integer32
_MagnumStpPortDesignatedCost_Object=MibTableColumn
magnumStpPortDesignatedCost=_MagnumStpPortDesignatedCost_Object((1,3,6,1,4,1,248,70,12,6,9,2,1,5),_MagnumStpPortDesignatedCost_Type())
magnumStpPortDesignatedCost.setMaxAccess(_C)
if mibBuilder.loadTexts:magnumStpPortDesignatedCost.setStatus(_A)
_MagnumStpPortDesignatedBridge_Type=DisplayString
_MagnumStpPortDesignatedBridge_Object=MibTableColumn
magnumStpPortDesignatedBridge=_MagnumStpPortDesignatedBridge_Object((1,3,6,1,4,1,248,70,12,6,9,2,1,6),_MagnumStpPortDesignatedBridge_Type())
magnumStpPortDesignatedBridge.setMaxAccess(_C)
if mibBuilder.loadTexts:magnumStpPortDesignatedBridge.setStatus(_A)
_MagnumStpPortDesignatedPort_Type=DisplayString
_MagnumStpPortDesignatedPort_Object=MibTableColumn
magnumStpPortDesignatedPort=_MagnumStpPortDesignatedPort_Object((1,3,6,1,4,1,248,70,12,6,9,2,1,7),_MagnumStpPortDesignatedPort_Type())
magnumStpPortDesignatedPort.setMaxAccess(_C)
if mibBuilder.loadTexts:magnumStpPortDesignatedPort.setStatus(_A)
class _MagnumStpTopChangeAck_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,255)));namedValues=NamedValues(*((_S,0),(_T,1),(_P,255)))
_MagnumStpTopChangeAck_Type.__name__=_B
_MagnumStpTopChangeAck_Object=MibTableColumn
magnumStpTopChangeAck=_MagnumStpTopChangeAck_Object((1,3,6,1,4,1,248,70,12,6,9,2,1,8),_MagnumStpTopChangeAck_Type())
magnumStpTopChangeAck.setMaxAccess(_C)
if mibBuilder.loadTexts:magnumStpTopChangeAck.setStatus(_A)
class _MagnumStpConfigPending_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,255)));namedValues=NamedValues(*((_S,0),(_T,1),(_P,255)))
_MagnumStpConfigPending_Type.__name__=_B
_MagnumStpConfigPending_Object=MibTableColumn
magnumStpConfigPending=_MagnumStpConfigPending_Object((1,3,6,1,4,1,248,70,12,6,9,2,1,9),_MagnumStpConfigPending_Type())
magnumStpConfigPending.setMaxAccess(_C)
if mibBuilder.loadTexts:magnumStpConfigPending.setStatus(_A)
class _MagnumStpPortPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_MagnumStpPortPriority_Type.__name__=_B
_MagnumStpPortPriority_Object=MibTableColumn
magnumStpPortPriority=_MagnumStpPortPriority_Object((1,3,6,1,4,1,248,70,12,6,9,2,1,10),_MagnumStpPortPriority_Type())
magnumStpPortPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:magnumStpPortPriority.setStatus(_A)
_MagnumBridgeGroup_ObjectIdentity=ObjectIdentity
magnumBridgeGroup=_MagnumBridgeGroup_ObjectIdentity((1,3,6,1,4,1,248,70,12,6,11))
_MagnumStpBridgeAgingTime_Type=Integer32
_MagnumStpBridgeAgingTime_Object=MibScalar
magnumStpBridgeAgingTime=_MagnumStpBridgeAgingTime_Object((1,3,6,1,4,1,248,70,12,6,11,1),_MagnumStpBridgeAgingTime_Type())
magnumStpBridgeAgingTime.setMaxAccess(_D)
if mibBuilder.loadTexts:magnumStpBridgeAgingTime.setStatus(_A)
_MagnumMgtBridgeTime_Type=Integer32
_MagnumMgtBridgeTime_Object=MibScalar
magnumMgtBridgeTime=_MagnumMgtBridgeTime_Object((1,3,6,1,4,1,248,70,12,6,11,2),_MagnumMgtBridgeTime_Type())
magnumMgtBridgeTime.setMaxAccess(_D)
if mibBuilder.loadTexts:magnumMgtBridgeTime.setStatus(_A)
_MagnumbridgeMacCount_Type=Integer32
_MagnumbridgeMacCount_Object=MibScalar
magnumbridgeMacCount=_MagnumbridgeMacCount_Object((1,3,6,1,4,1,248,70,12,6,11,3),_MagnumbridgeMacCount_Type())
magnumbridgeMacCount.setMaxAccess(_C)
if mibBuilder.loadTexts:magnumbridgeMacCount.setStatus(_A)
_MagnumEventMgrGroup_ObjectIdentity=ObjectIdentity
magnumEventMgrGroup=_MagnumEventMgrGroup_ObjectIdentity((1,3,6,1,4,1,248,70,12,6,12))
class _MagnumEventsRaised_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2500))
_MagnumEventsRaised_Type.__name__=_B
_MagnumEventsRaised_Object=MibScalar
magnumEventsRaised=_MagnumEventsRaised_Object((1,3,6,1,4,1,248,70,12,6,12,1),_MagnumEventsRaised_Type())
magnumEventsRaised.setMaxAccess(_C)
if mibBuilder.loadTexts:magnumEventsRaised.setStatus(_A)
class _MagnumSizeOfEventQueue_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2500))
_MagnumSizeOfEventQueue_Type.__name__=_B
_MagnumSizeOfEventQueue_Object=MibScalar
magnumSizeOfEventQueue=_MagnumSizeOfEventQueue_Object((1,3,6,1,4,1,248,70,12,6,12,2),_MagnumSizeOfEventQueue_Type())
magnumSizeOfEventQueue.setMaxAccess(_D)
if mibBuilder.loadTexts:magnumSizeOfEventQueue.setStatus(_A)
class _MagnumEventLogInvalidEvents_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2500))
_MagnumEventLogInvalidEvents_Type.__name__=_B
_MagnumEventLogInvalidEvents_Object=MibScalar
magnumEventLogInvalidEvents=_MagnumEventLogInvalidEvents_Object((1,3,6,1,4,1,248,70,12,6,12,3),_MagnumEventLogInvalidEvents_Type())
magnumEventLogInvalidEvents.setMaxAccess(_C)
if mibBuilder.loadTexts:magnumEventLogInvalidEvents.setStatus(_A)
class _MagnumEventLogCriticalEvents_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2500))
_MagnumEventLogCriticalEvents_Type.__name__=_B
_MagnumEventLogCriticalEvents_Object=MibScalar
magnumEventLogCriticalEvents=_MagnumEventLogCriticalEvents_Object((1,3,6,1,4,1,248,70,12,6,12,4),_MagnumEventLogCriticalEvents_Type())
magnumEventLogCriticalEvents.setMaxAccess(_C)
if mibBuilder.loadTexts:magnumEventLogCriticalEvents.setStatus(_A)
class _MagnumEventLogDebugEvents_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2500))
_MagnumEventLogDebugEvents_Type.__name__=_B
_MagnumEventLogDebugEvents_Object=MibScalar
magnumEventLogDebugEvents=_MagnumEventLogDebugEvents_Object((1,3,6,1,4,1,248,70,12,6,12,5),_MagnumEventLogDebugEvents_Type())
magnumEventLogDebugEvents.setMaxAccess(_C)
if mibBuilder.loadTexts:magnumEventLogDebugEvents.setStatus(_A)
class _MagnumEventLogFatalEvents_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2500))
_MagnumEventLogFatalEvents_Type.__name__=_B
_MagnumEventLogFatalEvents_Object=MibScalar
magnumEventLogFatalEvents=_MagnumEventLogFatalEvents_Object((1,3,6,1,4,1,248,70,12,6,12,6),_MagnumEventLogFatalEvents_Type())
magnumEventLogFatalEvents.setMaxAccess(_C)
if mibBuilder.loadTexts:magnumEventLogFatalEvents.setStatus(_A)
class _MagnumEventLogActivityEvents_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2500))
_MagnumEventLogActivityEvents_Type.__name__=_B
_MagnumEventLogActivityEvents_Object=MibScalar
magnumEventLogActivityEvents=_MagnumEventLogActivityEvents_Object((1,3,6,1,4,1,248,70,12,6,12,7),_MagnumEventLogActivityEvents_Type())
magnumEventLogActivityEvents.setMaxAccess(_C)
if mibBuilder.loadTexts:magnumEventLogActivityEvents.setStatus(_A)
_MagnumEventLogInfoEvents_Type=Integer32
_MagnumEventLogInfoEvents_Object=MibScalar
magnumEventLogInfoEvents=_MagnumEventLogInfoEvents_Object((1,3,6,1,4,1,248,70,12,6,12,8),_MagnumEventLogInfoEvents_Type())
magnumEventLogInfoEvents.setMaxAccess(_C)
if mibBuilder.loadTexts:magnumEventLogInfoEvents.setStatus(_A)
_MagnumEventTable_Object=MibTable
magnumEventTable=_MagnumEventTable_Object((1,3,6,1,4,1,248,70,12,6,12,9))
if mibBuilder.loadTexts:magnumEventTable.setStatus(_A)
_MagnumEventEntry_Object=MibTableRow
magnumEventEntry=_MagnumEventEntry_Object((1,3,6,1,4,1,248,70,12,6,12,9,1))
magnumEventEntry.setIndexNames((0,_F,_A9))
if mibBuilder.loadTexts:magnumEventEntry.setStatus(_A)
class _MagnumEventIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2500))
_MagnumEventIndex_Type.__name__=_B
_MagnumEventIndex_Object=MibTableColumn
magnumEventIndex=_MagnumEventIndex_Object((1,3,6,1,4,1,248,70,12,6,12,9,1,1),_MagnumEventIndex_Type())
magnumEventIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:magnumEventIndex.setStatus(_A)
_MagnumEventCode_Type=Integer32
_MagnumEventCode_Object=MibTableColumn
magnumEventCode=_MagnumEventCode_Object((1,3,6,1,4,1,248,70,12,6,12,9,1,2),_MagnumEventCode_Type())
magnumEventCode.setMaxAccess(_C)
if mibBuilder.loadTexts:magnumEventCode.setStatus(_A)
_MagnumEventModuleId_Type=Integer32
_MagnumEventModuleId_Object=MibTableColumn
magnumEventModuleId=_MagnumEventModuleId_Object((1,3,6,1,4,1,248,70,12,6,12,9,1,3),_MagnumEventModuleId_Type())
magnumEventModuleId.setMaxAccess(_C)
if mibBuilder.loadTexts:magnumEventModuleId.setStatus(_A)
class _MagnumEventSeverity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('fatal',0),('alert',1),('critical',2),('error',3),('warning',4),('notification',5),('information',6),('debug',7)))
_MagnumEventSeverity_Type.__name__=_B
_MagnumEventSeverity_Object=MibTableColumn
magnumEventSeverity=_MagnumEventSeverity_Object((1,3,6,1,4,1,248,70,12,6,12,9,1,4),_MagnumEventSeverity_Type())
magnumEventSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:magnumEventSeverity.setStatus(_A)
_MagnumEventTimeStamp_Type=DisplayString
_MagnumEventTimeStamp_Object=MibTableColumn
magnumEventTimeStamp=_MagnumEventTimeStamp_Object((1,3,6,1,4,1,248,70,12,6,12,9,1,5),_MagnumEventTimeStamp_Type())
magnumEventTimeStamp.setMaxAccess(_C)
if mibBuilder.loadTexts:magnumEventTimeStamp.setStatus(_A)
_MagnumTftpGroup_ObjectIdentity=ObjectIdentity
magnumTftpGroup=_MagnumTftpGroup_ObjectIdentity((1,3,6,1,4,1,248,70,12,6,13))
_MagnumTFTPSeverIpAddress_Type=IpAddress
_MagnumTFTPSeverIpAddress_Object=MibScalar
magnumTFTPSeverIpAddress=_MagnumTFTPSeverIpAddress_Object((1,3,6,1,4,1,248,70,12,6,13,1),_MagnumTFTPSeverIpAddress_Type())
magnumTFTPSeverIpAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:magnumTFTPSeverIpAddress.setStatus(_A)
class _MagnumTFTPRemoteFileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_MagnumTFTPRemoteFileName_Type.__name__=_O
_MagnumTFTPRemoteFileName_Object=MibScalar
magnumTFTPRemoteFileName=_MagnumTFTPRemoteFileName_Object((1,3,6,1,4,1,248,70,12,6,13,2),_MagnumTFTPRemoteFileName_Type())
magnumTFTPRemoteFileName.setMaxAccess(_D)
if mibBuilder.loadTexts:magnumTFTPRemoteFileName.setStatus(_A)
class _MagnumTFTPTransferType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_P,0),('octet',1),('nonascii',2)))
_MagnumTFTPTransferType_Type.__name__=_B
_MagnumTFTPTransferType_Object=MibScalar
magnumTFTPTransferType=_MagnumTFTPTransferType_Object((1,3,6,1,4,1,248,70,12,6,13,3),_MagnumTFTPTransferType_Type())
magnumTFTPTransferType.setMaxAccess(_C)
if mibBuilder.loadTexts:magnumTFTPTransferType.setStatus(_A)
class _MagnumTFTPAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_N,1),('downloadImage',2),('configUploadText',3),('configDownload',4),('configUploadEncrypted',5)))
_MagnumTFTPAction_Type.__name__=_B
_MagnumTFTPAction_Object=MibScalar
magnumTFTPAction=_MagnumTFTPAction_Object((1,3,6,1,4,1,248,70,12,6,13,4),_MagnumTFTPAction_Type())
magnumTFTPAction.setMaxAccess(_D)
if mibBuilder.loadTexts:magnumTFTPAction.setStatus(_A)
class _MagnumTFTPTrfrStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('other',0),('pending',1),('ok',2),('failed',3)))
_MagnumTFTPTrfrStatus_Type.__name__=_B
_MagnumTFTPTrfrStatus_Object=MibScalar
magnumTFTPTrfrStatus=_MagnumTFTPTrfrStatus_Object((1,3,6,1,4,1,248,70,12,6,13,5),_MagnumTFTPTrfrStatus_Type())
magnumTFTPTrfrStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:magnumTFTPTrfrStatus.setStatus(_A)
_MagnumSNTPGroup_ObjectIdentity=ObjectIdentity
magnumSNTPGroup=_MagnumSNTPGroup_ObjectIdentity((1,3,6,1,4,1,248,70,12,6,14))
class _SntpStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_G,1)))
_SntpStatus_Type.__name__=_B
_SntpStatus_Object=MibScalar
sntpStatus=_SntpStatus_Object((1,3,6,1,4,1,248,70,12,6,14,1),_SntpStatus_Type())
sntpStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:sntpStatus.setStatus(_A)
class _SntpTimeFormat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('hrs12',0),('hrs24',1)))
_SntpTimeFormat_Type.__name__=_B
_SntpTimeFormat_Object=MibScalar
sntpTimeFormat=_SntpTimeFormat_Object((1,3,6,1,4,1,248,70,12,6,14,2),_SntpTimeFormat_Type())
sntpTimeFormat.setMaxAccess(_D)
if mibBuilder.loadTexts:sntpTimeFormat.setStatus(_A)
class _SntpDateFormat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('mm-dd-yyyy',0),('dd-mm-yyyy',1),('yyyy-mm-dd',2)))
_SntpDateFormat_Type.__name__=_B
_SntpDateFormat_Object=MibScalar
sntpDateFormat=_SntpDateFormat_Object((1,3,6,1,4,1,248,70,12,6,14,3),_SntpDateFormat_Type())
sntpDateFormat.setMaxAccess(_D)
if mibBuilder.loadTexts:sntpDateFormat.setStatus(_A)
_SntpDisplayDate_Type=DisplayString
_SntpDisplayDate_Object=MibScalar
sntpDisplayDate=_SntpDisplayDate_Object((1,3,6,1,4,1,248,70,12,6,14,4),_SntpDisplayDate_Type())
sntpDisplayDate.setMaxAccess(_C)
if mibBuilder.loadTexts:sntpDisplayDate.setStatus(_A)
_SntpDisplayTime_Type=DisplayString
_SntpDisplayTime_Object=MibScalar
sntpDisplayTime=_SntpDisplayTime_Object((1,3,6,1,4,1,248,70,12,6,14,5),_SntpDisplayTime_Type())
sntpDisplayTime.setMaxAccess(_C)
if mibBuilder.loadTexts:sntpDisplayTime.setStatus(_A)
_SntpDisplayTimeZone_Type=DisplayString
_SntpDisplayTimeZone_Object=MibScalar
sntpDisplayTimeZone=_SntpDisplayTimeZone_Object((1,3,6,1,4,1,248,70,12,6,14,6),_SntpDisplayTimeZone_Type())
sntpDisplayTimeZone.setMaxAccess(_C)
if mibBuilder.loadTexts:sntpDisplayTimeZone.setStatus(_A)
_SntpDayLightSavings_Type=DisplayString
_SntpDayLightSavings_Object=MibScalar
sntpDayLightSavings=_SntpDayLightSavings_Object((1,3,6,1,4,1,248,70,12,6,14,7),_SntpDayLightSavings_Type())
sntpDayLightSavings.setMaxAccess(_D)
if mibBuilder.loadTexts:sntpDayLightSavings.setStatus(_A)
_MagnumSNTPTable_Object=MibTable
magnumSNTPTable=_MagnumSNTPTable_Object((1,3,6,1,4,1,248,70,12,6,14,8))
if mibBuilder.loadTexts:magnumSNTPTable.setStatus(_A)
_MagnumSNTPEntry_Object=MibTableRow
magnumSNTPEntry=_MagnumSNTPEntry_Object((1,3,6,1,4,1,248,70,12,6,14,8,1))
magnumSNTPEntry.setIndexNames((0,_F,_AA))
if mibBuilder.loadTexts:magnumSNTPEntry.setStatus(_A)
class _SntpIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_SntpIndex_Type.__name__=_B
_SntpIndex_Object=MibTableColumn
sntpIndex=_SntpIndex_Object((1,3,6,1,4,1,248,70,12,6,14,8,1,1),_SntpIndex_Type())
sntpIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:sntpIndex.setStatus(_A)
_SntpServerIp_Type=IpAddress
_SntpServerIp_Object=MibTableColumn
sntpServerIp=_SntpServerIp_Object((1,3,6,1,4,1,248,70,12,6,14,8,1,2),_SntpServerIp_Type())
sntpServerIp.setMaxAccess(_D)
if mibBuilder.loadTexts:sntpServerIp.setStatus(_A)
_SocketTimeout_Type=Integer32
_SocketTimeout_Object=MibTableColumn
socketTimeout=_SocketTimeout_Object((1,3,6,1,4,1,248,70,12,6,14,8,1,3),_SocketTimeout_Type())
socketTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:socketTimeout.setStatus(_A)
_NoOfRetries_Type=Integer32
_NoOfRetries_Object=MibTableColumn
noOfRetries=_NoOfRetries_Object((1,3,6,1,4,1,248,70,12,6,14,8,1,4),_NoOfRetries_Type())
noOfRetries.setMaxAccess(_D)
if mibBuilder.loadTexts:noOfRetries.setStatus(_A)
class _SntpOperation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('add',1),(_R,2),('modify',3),('update',4)))
_SntpOperation_Type.__name__=_B
_SntpOperation_Object=MibTableColumn
sntpOperation=_SntpOperation_Object((1,3,6,1,4,1,248,70,12,6,14,8,1,5),_SntpOperation_Type())
sntpOperation.setMaxAccess(_D)
if mibBuilder.loadTexts:sntpOperation.setStatus(_A)
_MagnumGVRPGroup_ObjectIdentity=ObjectIdentity
magnumGVRPGroup=_MagnumGVRPGroup_ObjectIdentity((1,3,6,1,4,1,248,70,12,6,15))
class _DeviceGVRPState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_E,2)))
_DeviceGVRPState_Type.__name__=_B
_DeviceGVRPState_Object=MibScalar
deviceGVRPState=_DeviceGVRPState_Object((1,3,6,1,4,1,248,70,12,6,15,1),_DeviceGVRPState_Type())
deviceGVRPState.setMaxAccess(_D)
if mibBuilder.loadTexts:deviceGVRPState.setStatus(_A)
_MagnumGVRPPortTable_Object=MibTable
magnumGVRPPortTable=_MagnumGVRPPortTable_Object((1,3,6,1,4,1,248,70,12,6,15,2))
if mibBuilder.loadTexts:magnumGVRPPortTable.setStatus(_A)
_MagnumGVRPPortEntry_Object=MibTableRow
magnumGVRPPortEntry=_MagnumGVRPPortEntry_Object((1,3,6,1,4,1,248,70,12,6,15,2,1))
magnumGVRPPortEntry.setIndexNames((0,_F,_AB))
if mibBuilder.loadTexts:magnumGVRPPortEntry.setStatus(_A)
class _GvrpPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,48))
_GvrpPortIndex_Type.__name__=_B
_GvrpPortIndex_Object=MibTableColumn
gvrpPortIndex=_GvrpPortIndex_Object((1,3,6,1,4,1,248,70,12,6,15,2,1,1),_GvrpPortIndex_Type())
gvrpPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:gvrpPortIndex.setStatus(_A)
class _GvrpPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('learn',1),('block',2),(_E,3)))
_GvrpPortState_Type.__name__=_B
_GvrpPortState_Object=MibTableColumn
gvrpPortState=_GvrpPortState_Object((1,3,6,1,4,1,248,70,12,6,15,2,1,2),_GvrpPortState_Type())
gvrpPortState.setMaxAccess(_D)
if mibBuilder.loadTexts:gvrpPortState.setStatus(_A)
_MagnumPortManagerGroup_ObjectIdentity=ObjectIdentity
magnumPortManagerGroup=_MagnumPortManagerGroup_ObjectIdentity((1,3,6,1,4,1,248,70,12,6,16))
_MagnumPortManagerTable_Object=MibTable
magnumPortManagerTable=_MagnumPortManagerTable_Object((1,3,6,1,4,1,248,70,12,6,16,1))
if mibBuilder.loadTexts:magnumPortManagerTable.setStatus(_A)
_MagnumPortManagerEntry_Object=MibTableRow
magnumPortManagerEntry=_MagnumPortManagerEntry_Object((1,3,6,1,4,1,248,70,12,6,16,1,1))
magnumPortManagerEntry.setIndexNames((0,_F,_Y))
if mibBuilder.loadTexts:magnumPortManagerEntry.setStatus(_A)
class _MagnumPortNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,48))
_MagnumPortNumber_Type.__name__=_B
_MagnumPortNumber_Object=MibTableColumn
magnumPortNumber=_MagnumPortNumber_Object((1,3,6,1,4,1,248,70,12,6,16,1,1,1),_MagnumPortNumber_Type())
magnumPortNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:magnumPortNumber.setStatus(_A)
_MagnumPortName_Type=DisplayString
_MagnumPortName_Object=MibTableColumn
magnumPortName=_MagnumPortName_Object((1,3,6,1,4,1,248,70,12,6,16,1,1,2),_MagnumPortName_Type())
magnumPortName.setMaxAccess(_D)
if mibBuilder.loadTexts:magnumPortName.setStatus(_A)
_MagnumPortSpeed_Type=Integer32
_MagnumPortSpeed_Object=MibTableColumn
magnumPortSpeed=_MagnumPortSpeed_Object((1,3,6,1,4,1,248,70,12,6,16,1,1,3),_MagnumPortSpeed_Type())
magnumPortSpeed.setMaxAccess(_D)
if mibBuilder.loadTexts:magnumPortSpeed.setStatus(_A)
class _MagnumPortDuplexMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('half',0),('full',1)))
_MagnumPortDuplexMode_Type.__name__=_B
_MagnumPortDuplexMode_Object=MibTableColumn
magnumPortDuplexMode=_MagnumPortDuplexMode_Object((1,3,6,1,4,1,248,70,12,6,16,1,1,4),_MagnumPortDuplexMode_Type())
magnumPortDuplexMode.setMaxAccess(_D)
if mibBuilder.loadTexts:magnumPortDuplexMode.setStatus(_A)
class _MagnumPortAutoNegotiationMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_G,1)))
_MagnumPortAutoNegotiationMode_Type.__name__=_B
_MagnumPortAutoNegotiationMode_Object=MibTableColumn
magnumPortAutoNegotiationMode=_MagnumPortAutoNegotiationMode_Object((1,3,6,1,4,1,248,70,12,6,16,1,1,5),_MagnumPortAutoNegotiationMode_Type())
magnumPortAutoNegotiationMode.setMaxAccess(_D)
if mibBuilder.loadTexts:magnumPortAutoNegotiationMode.setStatus(_A)
class _MagnumPortFlowControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_G,1)))
_MagnumPortFlowControl_Type.__name__=_B
_MagnumPortFlowControl_Object=MibTableColumn
magnumPortFlowControl=_MagnumPortFlowControl_Object((1,3,6,1,4,1,248,70,12,6,16,1,1,6),_MagnumPortFlowControl_Type())
magnumPortFlowControl.setMaxAccess(_D)
if mibBuilder.loadTexts:magnumPortFlowControl.setStatus(_A)
class _MagnumPortBackPressure_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_G,1)))
_MagnumPortBackPressure_Type.__name__=_B
_MagnumPortBackPressure_Object=MibTableColumn
magnumPortBackPressure=_MagnumPortBackPressure_Object((1,3,6,1,4,1,248,70,12,6,16,1,1,7),_MagnumPortBackPressure_Type())
magnumPortBackPressure.setMaxAccess(_D)
if mibBuilder.loadTexts:magnumPortBackPressure.setStatus(_A)
_MagnumPortVLANId_Type=Integer32
_MagnumPortVLANId_Object=MibTableColumn
magnumPortVLANId=_MagnumPortVLANId_Object((1,3,6,1,4,1,248,70,12,6,16,1,1,8),_MagnumPortVLANId_Type())
magnumPortVLANId.setMaxAccess(_C)
if mibBuilder.loadTexts:magnumPortVLANId.setStatus(_A)
class _MagnumPortGVRPstate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_G,1)))
_MagnumPortGVRPstate_Type.__name__=_B
_MagnumPortGVRPstate_Object=MibTableColumn
magnumPortGVRPstate=_MagnumPortGVRPstate_Object((1,3,6,1,4,1,248,70,12,6,16,1,1,9),_MagnumPortGVRPstate_Type())
magnumPortGVRPstate.setMaxAccess(_C)
if mibBuilder.loadTexts:magnumPortGVRPstate.setStatus(_A)
class _MagnumPortSTPstate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('blocking',0),(_E,1),(_A7,2),(_X,3),(_A8,4)))
_MagnumPortSTPstate_Type.__name__=_B
_MagnumPortSTPstate_Object=MibTableColumn
magnumPortSTPstate=_MagnumPortSTPstate_Object((1,3,6,1,4,1,248,70,12,6,16,1,1,10),_MagnumPortSTPstate_Type())
magnumPortSTPstate.setMaxAccess(_C)
if mibBuilder.loadTexts:magnumPortSTPstate.setStatus(_A)
class _MagnumPortLinkState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('down',0),('up',1)))
_MagnumPortLinkState_Type.__name__=_B
_MagnumPortLinkState_Object=MibTableColumn
magnumPortLinkState=_MagnumPortLinkState_Object((1,3,6,1,4,1,248,70,12,6,16,1,1,11),_MagnumPortLinkState_Type())
magnumPortLinkState.setMaxAccess(_C)
if mibBuilder.loadTexts:magnumPortLinkState.setStatus(_A)
_MagnumPortInterfaceType_Type=DisplayString
_MagnumPortInterfaceType_Object=MibTableColumn
magnumPortInterfaceType=_MagnumPortInterfaceType_Object((1,3,6,1,4,1,248,70,12,6,16,1,1,12),_MagnumPortInterfaceType_Type())
magnumPortInterfaceType.setMaxAccess(_C)
if mibBuilder.loadTexts:magnumPortInterfaceType.setStatus(_A)
class _MagnumPortSecurityState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_G,1)))
_MagnumPortSecurityState_Type.__name__=_B
_MagnumPortSecurityState_Object=MibTableColumn
magnumPortSecurityState=_MagnumPortSecurityState_Object((1,3,6,1,4,1,248,70,12,6,16,1,1,13),_MagnumPortSecurityState_Type())
magnumPortSecurityState.setMaxAccess(_C)
if mibBuilder.loadTexts:magnumPortSecurityState.setStatus(_A)
class _MagnumPortTaggingState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_G,1)))
_MagnumPortTaggingState_Type.__name__=_B
_MagnumPortTaggingState_Object=MibTableColumn
magnumPortTaggingState=_MagnumPortTaggingState_Object((1,3,6,1,4,1,248,70,12,6,16,1,1,14),_MagnumPortTaggingState_Type())
magnumPortTaggingState.setMaxAccess(_C)
if mibBuilder.loadTexts:magnumPortTaggingState.setStatus(_A)
class _MagnumPortNotifyState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_N,0),(_U,1),(_V,2),(_h,3),(_W,4),(_i,5),(_j,6),('all',7)))
_MagnumPortNotifyState_Type.__name__=_B
_MagnumPortNotifyState_Object=MibTableColumn
magnumPortNotifyState=_MagnumPortNotifyState_Object((1,3,6,1,4,1,248,70,12,6,16,1,1,15),_MagnumPortNotifyState_Type())
magnumPortNotifyState.setMaxAccess(_D)
if mibBuilder.loadTexts:magnumPortNotifyState.setStatus(_A)
_MagnumPortStatsTable_Object=MibTable
magnumPortStatsTable=_MagnumPortStatsTable_Object((1,3,6,1,4,1,248,70,12,6,16,2))
if mibBuilder.loadTexts:magnumPortStatsTable.setStatus(_A)
_MagnumPortStatsEntry_Object=MibTableRow
magnumPortStatsEntry=_MagnumPortStatsEntry_Object((1,3,6,1,4,1,248,70,12,6,16,2,1))
magnumPortStatsEntry.setIndexNames((0,_F,_AC))
if mibBuilder.loadTexts:magnumPortStatsEntry.setStatus(_A)
class _PortStatsIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,48))
_PortStatsIndex_Type.__name__=_B
_PortStatsIndex_Object=MibTableColumn
portStatsIndex=_PortStatsIndex_Object((1,3,6,1,4,1,248,70,12,6,16,2,1,1),_PortStatsIndex_Type())
portStatsIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:portStatsIndex.setStatus(_A)
_PortBytesReceived_Type=Integer32
_PortBytesReceived_Object=MibTableColumn
portBytesReceived=_PortBytesReceived_Object((1,3,6,1,4,1,248,70,12,6,16,2,1,2),_PortBytesReceived_Type())
portBytesReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:portBytesReceived.setStatus(_A)
_PortBytesSent_Type=Integer32
_PortBytesSent_Object=MibTableColumn
portBytesSent=_PortBytesSent_Object((1,3,6,1,4,1,248,70,12,6,16,2,1,3),_PortBytesSent_Type())
portBytesSent.setMaxAccess(_C)
if mibBuilder.loadTexts:portBytesSent.setStatus(_A)
_PortFramesReceived_Type=Integer32
_PortFramesReceived_Object=MibTableColumn
portFramesReceived=_PortFramesReceived_Object((1,3,6,1,4,1,248,70,12,6,16,2,1,4),_PortFramesReceived_Type())
portFramesReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:portFramesReceived.setStatus(_A)
_PortFramesSent_Type=Integer32
_PortFramesSent_Object=MibTableColumn
portFramesSent=_PortFramesSent_Object((1,3,6,1,4,1,248,70,12,6,16,2,1,5),_PortFramesSent_Type())
portFramesSent.setMaxAccess(_C)
if mibBuilder.loadTexts:portFramesSent.setStatus(_A)
_PortTotalBytesReceived_Type=Integer32
_PortTotalBytesReceived_Object=MibTableColumn
portTotalBytesReceived=_PortTotalBytesReceived_Object((1,3,6,1,4,1,248,70,12,6,16,2,1,6),_PortTotalBytesReceived_Type())
portTotalBytesReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:portTotalBytesReceived.setStatus(_A)
_PortTotalFramesReceived_Type=Integer32
_PortTotalFramesReceived_Object=MibTableColumn
portTotalFramesReceived=_PortTotalFramesReceived_Object((1,3,6,1,4,1,248,70,12,6,16,2,1,7),_PortTotalFramesReceived_Type())
portTotalFramesReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:portTotalFramesReceived.setStatus(_A)
_PortBroadcastFramesReceived_Type=Integer32
_PortBroadcastFramesReceived_Object=MibTableColumn
portBroadcastFramesReceived=_PortBroadcastFramesReceived_Object((1,3,6,1,4,1,248,70,12,6,16,2,1,8),_PortBroadcastFramesReceived_Type())
portBroadcastFramesReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:portBroadcastFramesReceived.setStatus(_A)
_PortMulticastFramesReceived_Type=Integer32
_PortMulticastFramesReceived_Object=MibTableColumn
portMulticastFramesReceived=_PortMulticastFramesReceived_Object((1,3,6,1,4,1,248,70,12,6,16,2,1,9),_PortMulticastFramesReceived_Type())
portMulticastFramesReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:portMulticastFramesReceived.setStatus(_A)
_PortCrcErrors_Type=Integer32
_PortCrcErrors_Object=MibTableColumn
portCrcErrors=_PortCrcErrors_Object((1,3,6,1,4,1,248,70,12,6,16,2,1,10),_PortCrcErrors_Type())
portCrcErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:portCrcErrors.setStatus(_A)
_PortOversizeFrames_Type=Integer32
_PortOversizeFrames_Object=MibTableColumn
portOversizeFrames=_PortOversizeFrames_Object((1,3,6,1,4,1,248,70,12,6,16,2,1,11),_PortOversizeFrames_Type())
portOversizeFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:portOversizeFrames.setStatus(_A)
_PortFragments_Type=Integer32
_PortFragments_Object=MibTableColumn
portFragments=_PortFragments_Object((1,3,6,1,4,1,248,70,12,6,16,2,1,12),_PortFragments_Type())
portFragments.setMaxAccess(_C)
if mibBuilder.loadTexts:portFragments.setStatus(_A)
_PortJabbers_Type=Integer32
_PortJabbers_Object=MibTableColumn
portJabbers=_PortJabbers_Object((1,3,6,1,4,1,248,70,12,6,16,2,1,13),_PortJabbers_Type())
portJabbers.setMaxAccess(_C)
if mibBuilder.loadTexts:portJabbers.setStatus(_A)
_PortCollissions_Type=Integer32
_PortCollissions_Object=MibTableColumn
portCollissions=_PortCollissions_Object((1,3,6,1,4,1,248,70,12,6,16,2,1,14),_PortCollissions_Type())
portCollissions.setMaxAccess(_C)
if mibBuilder.loadTexts:portCollissions.setStatus(_A)
_PortLateCollissions_Type=Integer32
_PortLateCollissions_Object=MibTableColumn
portLateCollissions=_PortLateCollissions_Object((1,3,6,1,4,1,248,70,12,6,16,2,1,15),_PortLateCollissions_Type())
portLateCollissions.setMaxAccess(_C)
if mibBuilder.loadTexts:portLateCollissions.setStatus(_A)
_PortFrames67_127_Type=Integer32
_PortFrames67_127_Object=MibTableColumn
portFrames67_127=_PortFrames67_127_Object((1,3,6,1,4,1,248,70,12,6,16,2,1,16),_PortFrames67_127_Type())
portFrames67_127.setMaxAccess(_C)
if mibBuilder.loadTexts:portFrames67_127.setStatus(_A)
_PortFrames128_255_Type=Integer32
_PortFrames128_255_Object=MibTableColumn
portFrames128_255=_PortFrames128_255_Object((1,3,6,1,4,1,248,70,12,6,16,2,1,17),_PortFrames128_255_Type())
portFrames128_255.setMaxAccess(_C)
if mibBuilder.loadTexts:portFrames128_255.setStatus(_A)
_PortFrames256_511_Type=Integer32
_PortFrames256_511_Object=MibTableColumn
portFrames256_511=_PortFrames256_511_Object((1,3,6,1,4,1,248,70,12,6,16,2,1,18),_PortFrames256_511_Type())
portFrames256_511.setMaxAccess(_C)
if mibBuilder.loadTexts:portFrames256_511.setStatus(_A)
_PortFrames512_1023_Type=Integer32
_PortFrames512_1023_Object=MibTableColumn
portFrames512_1023=_PortFrames512_1023_Object((1,3,6,1,4,1,248,70,12,6,16,2,1,19),_PortFrames512_1023_Type())
portFrames512_1023.setMaxAccess(_C)
if mibBuilder.loadTexts:portFrames512_1023.setStatus(_A)
_PortFrames1024_MaxSize_Type=Integer32
_PortFrames1024_MaxSize_Object=MibTableColumn
portFrames1024_MaxSize=_PortFrames1024_MaxSize_Object((1,3,6,1,4,1,248,70,12,6,16,2,1,20),_PortFrames1024_MaxSize_Type())
portFrames1024_MaxSize.setMaxAccess(_C)
if mibBuilder.loadTexts:portFrames1024_MaxSize.setStatus(_A)
_PortMacRxErrors_Type=Integer32
_PortMacRxErrors_Object=MibTableColumn
portMacRxErrors=_PortMacRxErrors_Object((1,3,6,1,4,1,248,70,12,6,16,2,1,21),_PortMacRxErrors_Type())
portMacRxErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:portMacRxErrors.setStatus(_A)
_PortDroppedFrames_Type=Integer32
_PortDroppedFrames_Object=MibTableColumn
portDroppedFrames=_PortDroppedFrames_Object((1,3,6,1,4,1,248,70,12,6,16,2,1,22),_PortDroppedFrames_Type())
portDroppedFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:portDroppedFrames.setStatus(_A)
_PortOutMulticastFrames_Type=Integer32
_PortOutMulticastFrames_Object=MibTableColumn
portOutMulticastFrames=_PortOutMulticastFrames_Object((1,3,6,1,4,1,248,70,12,6,16,2,1,23),_PortOutMulticastFrames_Type())
portOutMulticastFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:portOutMulticastFrames.setStatus(_A)
_PortOutBroadcastFrames_Type=Integer32
_PortOutBroadcastFrames_Object=MibTableColumn
portOutBroadcastFrames=_PortOutBroadcastFrames_Object((1,3,6,1,4,1,248,70,12,6,16,2,1,24),_PortOutBroadcastFrames_Type())
portOutBroadcastFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:portOutBroadcastFrames.setStatus(_A)
_PortUndersizeFrames_Type=Integer32
_PortUndersizeFrames_Object=MibTableColumn
portUndersizeFrames=_PortUndersizeFrames_Object((1,3,6,1,4,1,248,70,12,6,16,2,1,25),_PortUndersizeFrames_Type())
portUndersizeFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:portUndersizeFrames.setStatus(_A)
class _PortClearStatistics_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('clear',1))
_PortClearStatistics_Type.__name__=_B
_PortClearStatistics_Object=MibTableColumn
portClearStatistics=_PortClearStatistics_Object((1,3,6,1,4,1,248,70,12,6,16,2,1,26),_PortClearStatistics_Type())
portClearStatistics.setMaxAccess(_D)
if mibBuilder.loadTexts:portClearStatistics.setStatus(_A)
_MagnumPortQosTable_Object=MibTable
magnumPortQosTable=_MagnumPortQosTable_Object((1,3,6,1,4,1,248,70,12,6,16,3))
if mibBuilder.loadTexts:magnumPortQosTable.setStatus(_A)
_MagnumPortQosEntry_Object=MibTableRow
magnumPortQosEntry=_MagnumPortQosEntry_Object((1,3,6,1,4,1,248,70,12,6,16,3,1))
magnumPortQosEntry.setIndexNames((0,_F,_Y))
if mibBuilder.loadTexts:magnumPortQosEntry.setStatus(_A)
_MagnumPortQosIndex_Type=Integer32
_MagnumPortQosIndex_Object=MibTableColumn
magnumPortQosIndex=_MagnumPortQosIndex_Object((1,3,6,1,4,1,248,70,12,6,16,3,1,1),_MagnumPortQosIndex_Type())
magnumPortQosIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:magnumPortQosIndex.setStatus(_A)
class _MagnumPortQosPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_I,1)))
_MagnumPortQosPriority_Type.__name__=_B
_MagnumPortQosPriority_Object=MibTableColumn
magnumPortQosPriority=_MagnumPortQosPriority_Object((1,3,6,1,4,1,248,70,12,6,16,3,1,2),_MagnumPortQosPriority_Type())
magnumPortQosPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:magnumPortQosPriority.setStatus(_A)
_MagnumTypeOfService_Type=DisplayString
_MagnumTypeOfService_Object=MibTableColumn
magnumTypeOfService=_MagnumTypeOfService_Object((1,3,6,1,4,1,248,70,12,6,16,3,1,3),_MagnumTypeOfService_Type())
magnumTypeOfService.setMaxAccess(_D)
if mibBuilder.loadTexts:magnumTypeOfService.setStatus(_A)
_MagnumDeviceQosTable_Object=MibTable
magnumDeviceQosTable=_MagnumDeviceQosTable_Object((1,3,6,1,4,1,248,70,12,6,16,4))
if mibBuilder.loadTexts:magnumDeviceQosTable.setStatus(_A)
_MagnumDeviceQosEntry_Object=MibTableRow
magnumDeviceQosEntry=_MagnumDeviceQosEntry_Object((1,3,6,1,4,1,248,70,12,6,16,4,1))
magnumDeviceQosEntry.setIndexNames((0,_F,_AD))
if mibBuilder.loadTexts:magnumDeviceQosEntry.setStatus(_A)
class _MagnumDeviceQosIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,48))
_MagnumDeviceQosIndex_Type.__name__=_B
_MagnumDeviceQosIndex_Object=MibTableColumn
magnumDeviceQosIndex=_MagnumDeviceQosIndex_Object((1,3,6,1,4,1,248,70,12,6,16,4,1,1),_MagnumDeviceQosIndex_Type())
magnumDeviceQosIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:magnumDeviceQosIndex.setStatus(_A)
class _MagnumDefaultQos_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_G,1)))
_MagnumDefaultQos_Type.__name__=_B
_MagnumDefaultQos_Object=MibTableColumn
magnumDefaultQos=_MagnumDefaultQos_Object((1,3,6,1,4,1,248,70,12,6,16,4,1,2),_MagnumDefaultQos_Type())
magnumDefaultQos.setMaxAccess(_D)
if mibBuilder.loadTexts:magnumDefaultQos.setStatus(_A)
class _MagnumTagQos_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_G,1)))
_MagnumTagQos_Type.__name__=_B
_MagnumTagQos_Object=MibTableColumn
magnumTagQos=_MagnumTagQos_Object((1,3,6,1,4,1,248,70,12,6,16,4,1,3),_MagnumTagQos_Type())
magnumTagQos.setMaxAccess(_D)
if mibBuilder.loadTexts:magnumTagQos.setStatus(_A)
class _MagnumIpQos_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_G,1)))
_MagnumIpQos_Type.__name__=_B
_MagnumIpQos_Object=MibTableColumn
magnumIpQos=_MagnumIpQos_Object((1,3,6,1,4,1,248,70,12,6,16,4,1,4),_MagnumIpQos_Type())
magnumIpQos.setMaxAccess(_D)
if mibBuilder.loadTexts:magnumIpQos.setStatus(_A)
_MagnumConfigManagerGroup_ObjectIdentity=ObjectIdentity
magnumConfigManagerGroup=_MagnumConfigManagerGroup_ObjectIdentity((1,3,6,1,4,1,248,70,12,6,20))
class _SaveConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_SaveConfig_Type.__name__=_B
_SaveConfig_Object=MibScalar
saveConfig=_SaveConfig_Object((1,3,6,1,4,1,248,70,12,6,20,1),_SaveConfig_Type())
saveConfig.setMaxAccess(_D)
if mibBuilder.loadTexts:saveConfig.setStatus(_A)
_MagnumIGMPGroup_ObjectIdentity=ObjectIdentity
magnumIGMPGroup=_MagnumIGMPGroup_ObjectIdentity((1,3,6,1,4,1,248,70,12,6,21))
class _DeviceIGMPState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_E,2)))
_DeviceIGMPState_Type.__name__=_B
_DeviceIGMPState_Object=MibScalar
deviceIGMPState=_DeviceIGMPState_Object((1,3,6,1,4,1,248,70,12,6,21,1),_DeviceIGMPState_Type())
deviceIGMPState.setMaxAccess(_D)
if mibBuilder.loadTexts:deviceIGMPState.setStatus(_A)
class _ImmediateLeave_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_E,2)))
_ImmediateLeave_Type.__name__=_B
_ImmediateLeave_Object=MibScalar
immediateLeave=_ImmediateLeave_Object((1,3,6,1,4,1,248,70,12,6,21,2),_ImmediateLeave_Type())
immediateLeave.setMaxAccess(_D)
if mibBuilder.loadTexts:immediateLeave.setStatus(_A)
class _SwitchQuerier_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_E,2)))
_SwitchQuerier_Type.__name__=_B
_SwitchQuerier_Object=MibScalar
switchQuerier=_SwitchQuerier_Object((1,3,6,1,4,1,248,70,12,6,21,3),_SwitchQuerier_Type())
switchQuerier.setMaxAccess(_D)
if mibBuilder.loadTexts:switchQuerier.setStatus(_A)
_QueryInterval_Type=Integer32
_QueryInterval_Object=MibScalar
queryInterval=_QueryInterval_Object((1,3,6,1,4,1,248,70,12,6,21,4),_QueryInterval_Type())
queryInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:queryInterval.setStatus(_A)
_QueryResponseInterval_Type=Integer32
_QueryResponseInterval_Object=MibScalar
queryResponseInterval=_QueryResponseInterval_Object((1,3,6,1,4,1,248,70,12,6,21,5),_QueryResponseInterval_Type())
queryResponseInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:queryResponseInterval.setStatus(_A)
_MagnumIGMPGroupTable_Object=MibTable
magnumIGMPGroupTable=_MagnumIGMPGroupTable_Object((1,3,6,1,4,1,248,70,12,6,21,6))
if mibBuilder.loadTexts:magnumIGMPGroupTable.setStatus(_A)
_MagnumIGMPGroupEntry_Object=MibTableRow
magnumIGMPGroupEntry=_MagnumIGMPGroupEntry_Object((1,3,6,1,4,1,248,70,12,6,21,6,1))
magnumIGMPGroupEntry.setIndexNames((0,_F,_AE))
if mibBuilder.loadTexts:magnumIGMPGroupEntry.setStatus(_A)
class _IgmpGroupIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2000))
_IgmpGroupIndex_Type.__name__=_B
_IgmpGroupIndex_Object=MibTableColumn
igmpGroupIndex=_IgmpGroupIndex_Object((1,3,6,1,4,1,248,70,12,6,21,6,1,1),_IgmpGroupIndex_Type())
igmpGroupIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:igmpGroupIndex.setStatus(_A)
_IgmpGroupAddress_Type=IpAddress
_IgmpGroupAddress_Object=MibTableColumn
igmpGroupAddress=_IgmpGroupAddress_Object((1,3,6,1,4,1,248,70,12,6,21,6,1,2),_IgmpGroupAddress_Type())
igmpGroupAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:igmpGroupAddress.setStatus(_A)
_IgmpGroupPort_Type=Integer32
_IgmpGroupPort_Object=MibTableColumn
igmpGroupPort=_IgmpGroupPort_Object((1,3,6,1,4,1,248,70,12,6,21,6,1,3),_IgmpGroupPort_Type())
igmpGroupPort.setMaxAccess(_C)
if mibBuilder.loadTexts:igmpGroupPort.setStatus(_A)
_IgmpGroupTimer_Type=Integer32
_IgmpGroupTimer_Object=MibTableColumn
igmpGroupTimer=_IgmpGroupTimer_Object((1,3,6,1,4,1,248,70,12,6,21,6,1,4),_IgmpGroupTimer_Type())
igmpGroupTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:igmpGroupTimer.setStatus(_A)
_IgmpGroupLeaveP_Type=Integer32
_IgmpGroupLeaveP_Object=MibTableColumn
igmpGroupLeaveP=_IgmpGroupLeaveP_Object((1,3,6,1,4,1,248,70,12,6,21,6,1,5),_IgmpGroupLeaveP_Type())
igmpGroupLeaveP.setMaxAccess(_C)
if mibBuilder.loadTexts:igmpGroupLeaveP.setStatus(_A)
_MagnumIGMPRouterTable_Object=MibTable
magnumIGMPRouterTable=_MagnumIGMPRouterTable_Object((1,3,6,1,4,1,248,70,12,6,21,7))
if mibBuilder.loadTexts:magnumIGMPRouterTable.setStatus(_A)
_MagnumIGMPRouterEntry_Object=MibTableRow
magnumIGMPRouterEntry=_MagnumIGMPRouterEntry_Object((1,3,6,1,4,1,248,70,12,6,21,7,1))
magnumIGMPRouterEntry.setIndexNames((0,_F,_AF))
if mibBuilder.loadTexts:magnumIGMPRouterEntry.setStatus(_A)
class _IgmpRouterIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2000))
_IgmpRouterIndex_Type.__name__=_B
_IgmpRouterIndex_Object=MibTableColumn
igmpRouterIndex=_IgmpRouterIndex_Object((1,3,6,1,4,1,248,70,12,6,21,7,1,1),_IgmpRouterIndex_Type())
igmpRouterIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:igmpRouterIndex.setStatus(_A)
_IgmpRouterAddress_Type=IpAddress
_IgmpRouterAddress_Object=MibTableColumn
igmpRouterAddress=_IgmpRouterAddress_Object((1,3,6,1,4,1,248,70,12,6,21,7,1,2),_IgmpRouterAddress_Type())
igmpRouterAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:igmpRouterAddress.setStatus(_A)
_IgmpRouterPort_Type=Integer32
_IgmpRouterPort_Object=MibTableColumn
igmpRouterPort=_IgmpRouterPort_Object((1,3,6,1,4,1,248,70,12,6,21,7,1,3),_IgmpRouterPort_Type())
igmpRouterPort.setMaxAccess(_C)
if mibBuilder.loadTexts:igmpRouterPort.setStatus(_A)
_IgmpRouterTimer_Type=Integer32
_IgmpRouterTimer_Object=MibTableColumn
igmpRouterTimer=_IgmpRouterTimer_Object((1,3,6,1,4,1,248,70,12,6,21,7,1,4),_IgmpRouterTimer_Type())
igmpRouterTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:igmpRouterTimer.setStatus(_A)
_MagnumIGMPPortTable_Object=MibTable
magnumIGMPPortTable=_MagnumIGMPPortTable_Object((1,3,6,1,4,1,248,70,12,6,21,8))
if mibBuilder.loadTexts:magnumIGMPPortTable.setStatus(_A)
_MagnumIGMPPortEntry_Object=MibTableRow
magnumIGMPPortEntry=_MagnumIGMPPortEntry_Object((1,3,6,1,4,1,248,70,12,6,21,8,1))
magnumIGMPPortEntry.setIndexNames((0,_F,_AG))
if mibBuilder.loadTexts:magnumIGMPPortEntry.setStatus(_A)
class _IgmpPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,48))
_IgmpPortIndex_Type.__name__=_B
_IgmpPortIndex_Object=MibTableColumn
igmpPortIndex=_IgmpPortIndex_Object((1,3,6,1,4,1,248,70,12,6,21,8,1,1),_IgmpPortIndex_Type())
igmpPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:igmpPortIndex.setStatus(_A)
class _IgmpPortMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_P,0),('auto',1),('forward',2),('block',3)))
_IgmpPortMode_Type.__name__=_B
_IgmpPortMode_Object=MibTableColumn
igmpPortMode=_IgmpPortMode_Object((1,3,6,1,4,1,248,70,12,6,21,8,1,2),_IgmpPortMode_Type())
igmpPortMode.setMaxAccess(_D)
if mibBuilder.loadTexts:igmpPortMode.setStatus(_A)
class _UnknownMcast_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_E,2)))
_UnknownMcast_Type.__name__=_B
_UnknownMcast_Object=MibScalar
unknownMcast=_UnknownMcast_Object((1,3,6,1,4,1,248,70,12,6,21,9),_UnknownMcast_Type())
unknownMcast.setMaxAccess(_D)
if mibBuilder.loadTexts:unknownMcast.setStatus(_A)
_Sring_ObjectIdentity=ObjectIdentity
sring=_Sring_ObjectIdentity((1,3,6,1,4,1,248,70,12,6,22))
class _SringControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_L,0),(_M,1),(_X,2)))
_SringControl_Type.__name__=_B
_SringControl_Object=MibScalar
sringControl=_SringControl_Object((1,3,6,1,4,1,248,70,12,6,22,1),_SringControl_Type())
sringControl.setMaxAccess(_D)
if mibBuilder.loadTexts:sringControl.setStatus(_A)
_SringTable_Object=MibTable
sringTable=_SringTable_Object((1,3,6,1,4,1,248,70,12,6,22,2))
if mibBuilder.loadTexts:sringTable.setStatus(_A)
_SringEntry_Object=MibTableRow
sringEntry=_SringEntry_Object((1,3,6,1,4,1,248,70,12,6,22,2,1))
sringEntry.setIndexNames((0,_F,_AH))
if mibBuilder.loadTexts:sringEntry.setStatus(_A)
class _SringIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,24))
_SringIndex_Type.__name__=_B
_SringIndex_Object=MibTableColumn
sringIndex=_SringIndex_Object((1,3,6,1,4,1,248,70,12,6,22,2,1,1),_SringIndex_Type())
sringIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:sringIndex.setStatus(_A)
_SringPort1_Type=Integer32
_SringPort1_Object=MibTableColumn
sringPort1=_SringPort1_Object((1,3,6,1,4,1,248,70,12,6,22,2,1,2),_SringPort1_Type())
sringPort1.setMaxAccess(_D)
if mibBuilder.loadTexts:sringPort1.setStatus(_A)
_SringPort2_Type=Integer32
_SringPort2_Object=MibTableColumn
sringPort2=_SringPort2_Object((1,3,6,1,4,1,248,70,12,6,22,2,1,3),_SringPort2_Type())
sringPort2.setMaxAccess(_D)
if mibBuilder.loadTexts:sringPort2.setStatus(_A)
class _SringStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('initial',0),(_P,1),('closed',2),('open',3)))
_SringStatus_Type.__name__=_B
_SringStatus_Object=MibTableColumn
sringStatus=_SringStatus_Object((1,3,6,1,4,1,248,70,12,6,22,2,1,4),_SringStatus_Type())
sringStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:sringStatus.setStatus(_A)
_Lll_ObjectIdentity=ObjectIdentity
lll=_Lll_ObjectIdentity((1,3,6,1,4,1,248,70,12,6,23))
class _LllControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_L,0),(_M,1)))
_LllControl_Type.__name__=_B
_LllControl_Object=MibScalar
lllControl=_LllControl_Object((1,3,6,1,4,1,248,70,12,6,23,1),_LllControl_Type())
lllControl.setMaxAccess(_D)
if mibBuilder.loadTexts:lllControl.setStatus(_A)
_LllPortMap_Type=DisplayString
_LllPortMap_Object=MibScalar
lllPortMap=_LllPortMap_Object((1,3,6,1,4,1,248,70,12,6,23,2),_LllPortMap_Type())
lllPortMap.setMaxAccess(_D)
if mibBuilder.loadTexts:lllPortMap.setStatus(_A)
_Alarm_ObjectIdentity=ObjectIdentity
alarm=_Alarm_ObjectIdentity((1,3,6,1,4,1,248,70,12,6,24))
class _AlarmControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_L,2)))
_AlarmControl_Type.__name__=_B
_AlarmControl_Object=MibScalar
alarmControl=_AlarmControl_Object((1,3,6,1,4,1,248,70,12,6,24,1),_AlarmControl_Type())
alarmControl.setMaxAccess(_D)
if mibBuilder.loadTexts:alarmControl.setStatus(_A)
class _AlarmWidth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_AlarmWidth_Type.__name__=_B
_AlarmWidth_Object=MibScalar
alarmWidth=_AlarmWidth_Object((1,3,6,1,4,1,248,70,12,6,24,2),_AlarmWidth_Type())
alarmWidth.setMaxAccess(_D)
if mibBuilder.loadTexts:alarmWidth.setStatus(_A)
_AlarmTable_Object=MibTable
alarmTable=_AlarmTable_Object((1,3,6,1,4,1,248,70,12,6,24,3))
if mibBuilder.loadTexts:alarmTable.setStatus(_A)
_AlarmEntry_Object=MibTableRow
alarmEntry=_AlarmEntry_Object((1,3,6,1,4,1,248,70,12,6,24,3,1))
alarmEntry.setIndexNames((0,_F,_AI))
if mibBuilder.loadTexts:alarmEntry.setStatus(_A)
class _AlarmIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,50))
_AlarmIndex_Type.__name__=_B
_AlarmIndex_Object=MibTableColumn
alarmIndex=_AlarmIndex_Object((1,3,6,1,4,1,248,70,12,6,24,3,1,1),_AlarmIndex_Type())
alarmIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmIndex.setStatus(_A)
_AlarmEvent_Type=Integer32
_AlarmEvent_Object=MibTableColumn
alarmEvent=_AlarmEvent_Object((1,3,6,1,4,1,248,70,12,6,24,3,1,2),_AlarmEvent_Type())
alarmEvent.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmEvent.setStatus(_A)
class _AlarmType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('sustained',1),('momentary',2)))
_AlarmType_Type.__name__=_B
_AlarmType_Object=MibTableColumn
alarmType=_AlarmType_Object((1,3,6,1,4,1,248,70,12,6,24,3,1,3),_AlarmType_Type())
alarmType.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmType.setStatus(_A)
_AlarmDesc_Type=DisplayString
_AlarmDesc_Object=MibTableColumn
alarmDesc=_AlarmDesc_Object((1,3,6,1,4,1,248,70,12,6,24,3,1,4),_AlarmDesc_Type())
alarmDesc.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmDesc.setStatus(_A)
class _AlarmStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_L,2)))
_AlarmStatus_Type.__name__=_B
_AlarmStatus_Object=MibTableColumn
alarmStatus=_AlarmStatus_Object((1,3,6,1,4,1,248,70,12,6,24,3,1,5),_AlarmStatus_Type())
alarmStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:alarmStatus.setStatus(_A)
class _AlarmFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('set',1),('reset',2)))
_AlarmFlag_Type.__name__=_B
_AlarmFlag_Object=MibTableColumn
alarmFlag=_AlarmFlag_Object((1,3,6,1,4,1,248,70,12,6,24,3,1,6),_AlarmFlag_Type())
alarmFlag.setMaxAccess(_D)
if mibBuilder.loadTexts:alarmFlag.setStatus(_A)
_Dualhome_ObjectIdentity=ObjectIdentity
dualhome=_Dualhome_ObjectIdentity((1,3,6,1,4,1,248,70,12,6,25))
class _DhControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_L,0),(_M,1),(_R,2)))
_DhControl_Type.__name__=_B
_DhControl_Object=MibScalar
dhControl=_DhControl_Object((1,3,6,1,4,1,248,70,12,6,25,1),_DhControl_Type())
dhControl.setMaxAccess(_D)
if mibBuilder.loadTexts:dhControl.setStatus(_A)
class _DhMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_l,0),('primarySecondary',1)))
_DhMode_Type.__name__=_B
_DhMode_Object=MibScalar
dhMode=_DhMode_Object((1,3,6,1,4,1,248,70,12,6,25,2),_DhMode_Type())
dhMode.setMaxAccess(_D)
if mibBuilder.loadTexts:dhMode.setStatus(_A)
_DhActive_Type=Integer32
_DhActive_Object=MibScalar
dhActive=_DhActive_Object((1,3,6,1,4,1,248,70,12,6,25,3),_DhActive_Type())
dhActive.setMaxAccess(_C)
if mibBuilder.loadTexts:dhActive.setStatus(_A)
_DhPort1_Type=Integer32
_DhPort1_Object=MibScalar
dhPort1=_DhPort1_Object((1,3,6,1,4,1,248,70,12,6,25,4),_DhPort1_Type())
dhPort1.setMaxAccess(_D)
if mibBuilder.loadTexts:dhPort1.setStatus(_A)
_DhPort2_Type=Integer32
_DhPort2_Object=MibScalar
dhPort2=_DhPort2_Object((1,3,6,1,4,1,248,70,12,6,25,5),_DhPort2_Type())
dhPort2.setMaxAccess(_D)
if mibBuilder.loadTexts:dhPort2.setStatus(_A)
_Max16_ObjectIdentity=ObjectIdentity
max16=_Max16_ObjectIdentity((1,3,6,1,4,1,248,70,12,7))
_Max32_ObjectIdentity=ObjectIdentity
max32=_Max32_ObjectIdentity((1,3,6,1,4,1,248,70,12,8))
_Max8_ObjectIdentity=ObjectIdentity
max8=_Max8_ObjectIdentity((1,3,6,1,4,1,248,70,12,9))
_Max32t_ObjectIdentity=ObjectIdentity
max32t=_Max32t_ObjectIdentity((1,3,6,1,4,1,248,70,12,10))
_Maxq_ObjectIdentity=ObjectIdentity
maxq=_Maxq_ObjectIdentity((1,3,6,1,4,1,248,70,12,11))
_Mx_events_ObjectIdentity=ObjectIdentity
mx_events=_Mx_events_ObjectIdentity((1,3,6,1,4,1,248,70,12,12))
_UserAuthFail_ObjectIdentity=ObjectIdentity
userAuthFail=_UserAuthFail_ObjectIdentity((1,3,6,1,4,1,248,70,12,12,1))
class _Mode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('console',1),('telnet',2),('web',3)))
_Mode_Type.__name__=_B
_Mode_Object=MibScalar
mode=_Mode_Object((1,3,6,1,4,1,248,70,12,12,1,1),_Mode_Type())
mode.setMaxAccess(_C)
if mibBuilder.loadTexts:mode.setStatus(_A)
_UserIpAddress_Type=IpAddress
_UserIpAddress_Object=MibScalar
userIpAddress=_UserIpAddress_Object((1,3,6,1,4,1,248,70,12,12,1,2),_UserIpAddress_Type())
userIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:userIpAddress.setStatus(_A)
_PowerAlarm_ObjectIdentity=ObjectIdentity
powerAlarm=_PowerAlarm_ObjectIdentity((1,3,6,1,4,1,248,70,12,12,2))
class _PowerSupplyFailed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('powerSupplyA',1),('powerSupplyB',2)))
_PowerSupplyFailed_Type.__name__=_B
_PowerSupplyFailed_Object=MibScalar
powerSupplyFailed=_PowerSupplyFailed_Object((1,3,6,1,4,1,248,70,12,12,2,1),_PowerSupplyFailed_Type())
powerSupplyFailed.setMaxAccess(_C)
if mibBuilder.loadTexts:powerSupplyFailed.setStatus(_A)
_FanAlarm_ObjectIdentity=ObjectIdentity
fanAlarm=_FanAlarm_ObjectIdentity((1,3,6,1,4,1,248,70,12,12,3))
_FanNumber_Type=Integer32
_FanNumber_Object=MibScalar
fanNumber=_FanNumber_Object((1,3,6,1,4,1,248,70,12,12,3,1),_FanNumber_Type())
fanNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:fanNumber.setStatus(_A)
class _FanStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('on',1),('off',2),('faulted',3)))
_FanStatus_Type.__name__=_B
_FanStatus_Object=MibScalar
fanStatus=_FanStatus_Object((1,3,6,1,4,1,248,70,12,12,3,2),_FanStatus_Type())
fanStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fanStatus.setStatus(_A)
_Max25e_ObjectIdentity=ObjectIdentity
max25e=_Max25e_ObjectIdentity((1,3,6,1,4,1,248,70,12,13))
_Max32f_ObjectIdentity=ObjectIdentity
max32f=_Max32f_ObjectIdentity((1,3,6,1,4,1,248,70,12,14))
_Max32fc_ObjectIdentity=ObjectIdentity
max32fc=_Max32fc_ObjectIdentity((1,3,6,1,4,1,248,70,12,17))
_Maxqe_ObjectIdentity=ObjectIdentity
maxqe=_Maxqe_ObjectIdentity((1,3,6,1,4,1,248,70,12,18))
_Maxl_ObjectIdentity=ObjectIdentity
maxl=_Maxl_ObjectIdentity((1,3,6,1,4,1,248,70,12,19))
_Max1000_ObjectIdentity=ObjectIdentity
max1000=_Max1000_ObjectIdentity((1,3,6,1,4,1,248,70,12,20))
_Magnum10kt_ObjectIdentity=ObjectIdentity
magnum10kt=_Magnum10kt_ObjectIdentity((1,3,6,1,4,1,248,70,12,20))
_Maxm_ObjectIdentity=ObjectIdentity
maxm=_Maxm_ObjectIdentity((1,3,6,1,4,1,248,70,12,21))
_Max25m_ObjectIdentity=ObjectIdentity
max25m=_Max25m_ObjectIdentity((1,3,6,1,4,1,248,70,12,21))
_Magnum10kg_ObjectIdentity=ObjectIdentity
magnum10kg=_Magnum10kg_ObjectIdentity((1,3,6,1,4,1,248,70,12,22))
m6kIntruderTrap=NotificationType((1,3,6,1,4,1,248,70,12,12,0,1))
if mibBuilder.loadTexts:m6kIntruderTrap.setStatus('')
m6kSringOpenTrap=NotificationType((1,3,6,1,4,1,248,70,12,12,0,2))
if mibBuilder.loadTexts:m6kSringOpenTrap.setStatus('')
m6kSringClosedTrap=NotificationType((1,3,6,1,4,1,248,70,12,12,0,3))
if mibBuilder.loadTexts:m6kSringClosedTrap.setStatus('')
m6kLLLTrap=NotificationType((1,3,6,1,4,1,248,70,12,12,0,4))
if mibBuilder.loadTexts:m6kLLLTrap.setStatus('')
m6kPMPTrap=NotificationType((1,3,6,1,4,1,248,70,12,12,0,5))
if mibBuilder.loadTexts:m6kPMPTrap.setStatus('')
m6kUserAuthFailTrap=NotificationType((1,3,6,1,4,1,248,70,12,12,0,6))
if mibBuilder.loadTexts:m6kUserAuthFailTrap.setStatus('')
m6kPowerAlarmTrap=NotificationType((1,3,6,1,4,1,248,70,12,12,0,7))
if mibBuilder.loadTexts:m6kPowerAlarmTrap.setStatus('')
m6kSTPEnabledTrap=NotificationType((1,3,6,1,4,1,248,70,12,12,0,8))
if mibBuilder.loadTexts:m6kSTPEnabledTrap.setStatus('')
m6kRSTPEnabledTrap=NotificationType((1,3,6,1,4,1,248,70,12,12,0,9))
if mibBuilder.loadTexts:m6kRSTPEnabledTrap.setStatus('')
m6kSTPDisabledTrap=NotificationType((1,3,6,1,4,1,248,70,12,12,0,10))
if mibBuilder.loadTexts:m6kSTPDisabledTrap.setStatus('')
m6kRSTPDisabledTrap=NotificationType((1,3,6,1,4,1,248,70,12,12,0,11))
if mibBuilder.loadTexts:m6kRSTPDisabledTrap.setStatus('')
m6kFanAlarmTrap=NotificationType((1,3,6,1,4,1,248,70,12,12,0,12))
if mibBuilder.loadTexts:m6kFanAlarmTrap.setStatus('')
mibBuilder.exportSymbols(_F,**{'hirschmann':hirschmann,'max':max,'basics':basics,'systemGroup':systemGroup,'systemName':systemName,'systemVersion':systemVersion,'systemFirmwareVersion':systemFirmwareVersion,'systemMacAddress':systemMacAddress,'deviceReset':deviceReset,'systemUpTime':systemUpTime,'systemLocation':systemLocation,'systemContact':systemContact,'sysIpAddress':sysIpAddress,'sysSubnet':sysSubnet,'sysGateway':sysGateway,'sysSerial':sysSerial,'sysOrderCode':sysOrderCode,'sysTemperature':sysTemperature,'sysTempUnit':sysTempUnit,'sysPS1Status':sysPS1Status,'sysPS2Status':sysPS2Status,'sysCPUusage':sysCPUusage,'sysMemUsage':sysMemUsage,'snmpGroup':snmpGroup,'mibsInfo':mibsInfo,'switch':switch,'max25':max25,'generalmx':generalmx,'slotNumber':slotNumber,'portNumber':portNumber,'slotTable':slotTable,'slotEntry':slotEntry,_d:slotIndex,'slotName':slotName,'moduleId':moduleId,'moduleName':moduleName,'portControl':portControl,'savePortControl':savePortControl,'portTable':portTable,'portEntry':portEntry,_e:ptSlotIndex,_f:ptPortIndex,'ptIfIndex':ptIfIndex,'ptPortName':ptPortName,'ptPortControlStatus':ptPortControlStatus,'ptPortStatus':ptPortStatus,'ptPortDuplexStatus':ptPortDuplexStatus,'ptPortMediaType':ptPortMediaType,'ptPortLinkStatus':ptPortLinkStatus,'ptPortSpeed':ptPortSpeed,'ptPortPartitionState':ptPortPartitionState,'ptPortTraffic':ptPortTraffic,'ptPortAutoNegotiation':ptPortAutoNegotiation,'ptPortNotify':ptPortNotify,'portMirroring':portMirroring,'monitorPort':monitorPort,'snifferPort':snifferPort,'portMirroringControl':portMirroringControl,'savePortMirroring':savePortMirroring,'monitorPortList':monitorPortList,'priorityQueuing':priorityQueuing,'priorityQueueControl':priorityQueueControl,'savePriorityQueue':savePriorityQueue,'priorityQueueTable':priorityQueueTable,'priorityQueueEntry':priorityQueueEntry,_k:pqPortIndex,'pqControlStatus':pqControlStatus,'pqDefaultQueue':pqDefaultQueue,'priorityForUntaggedPktsOnHighQ':priorityForUntaggedPktsOnHighQ,'priorityForUntaggedPktsOnLowQ':priorityForUntaggedPktsOnLowQ,'qForPktsWithPriority0':qForPktsWithPriority0,'qForPktsWithPriority1':qForPktsWithPriority1,'qForPktsWithPriority2':qForPktsWithPriority2,'qForPktsWithPriority3':qForPktsWithPriority3,'qForPktsWithPriority4':qForPktsWithPriority4,'qForPktsWithPriority5':qForPktsWithPriority5,'qForPktsWithPriority6':qForPktsWithPriority6,'qForPktsWithPriority7':qForPktsWithPriority7,'layer3Qos':layer3Qos,'layer3QosControl':layer3QosControl,'savelayer3Qos':savelayer3Qos,'layer3QosPortTable':layer3QosPortTable,'layer3QosPortEntry':layer3QosPortEntry,_u:l3qptPortIndex,'l3QosControlStatus':l3QosControlStatus,'layer3QosQueueTable':layer3QosQueueTable,'layer3QosQueueEntry':layer3QosQueueEntry,_v:l3qqtPortIndex,_w:l3qqtDscpIndex,'l3qqtQueueValue':l3qqtQueueValue,'portSecurity':portSecurity,'portSecurityControl':portSecurityControl,'saveportSecurity':saveportSecurity,'portSecurityTable':portSecurityTable,'portSecurityEntry':portSecurityEntry,_x:psPortIndex,_y:psEntryIndex,'psMacAddress':psMacAddress,'psEntryStatus':psEntryStatus,'actionSignalTable':actionSignalTable,'actionSignalEntry':actionSignalEntry,_z:atPortIndex,'atAction':atAction,'atSignal':atSignal,'atLearnMode':atLearnMode,'vlan':vlan,'vlanType':vlanType,_A0:portBasedVLAN,'maxPVLAN':maxPVLAN,'pvlansCreated':pvlansCreated,'savepvlan':savepvlan,'pvlanControlStatus':pvlanControlStatus,'pvlanTable':pvlanTable,'pvlanEntry':pvlanEntry,_A2:pvlanIndex,'pvlanName':pvlanName,'pvlanPortList':pvlanPortList,'pvlanEntryStatus':pvlanEntryStatus,_A1:tagBasedVLAN,'maxTVLAN':maxTVLAN,'tvlansCreated':tvlansCreated,'savetvlan':savetvlan,'tvlanControlStatus':tvlanControlStatus,'tvlanTable':tvlanTable,'tvlanEntry':tvlanEntry,_A3:tvlanIndex,'tvlanName':tvlanName,'tvlanPortList':tvlanPortList,'tvlanEgressRules':tvlanEgressRules,'tvlanEntryStatus':tvlanEntryStatus,'ingressTable':ingressTable,'ingressEntry':ingressEntry,_A4:portIndex,'portDefaultId':portDefaultId,'inCheck':inCheck,'magnumStpGroup':magnumStpGroup,'magnumBrStpTable':magnumBrStpTable,'magnumBrStpEntry':magnumBrStpEntry,_A5:magnumBrStpIndex,'magnumBrStpDesignatedRoot':magnumBrStpDesignatedRoot,'magnumBrStpRootPathCost':magnumBrStpRootPathCost,'magnumBrStpRootPort':magnumBrStpRootPort,'magnumBrStpRootBridgeMaxAge':magnumBrStpRootBridgeMaxAge,'magnumBrStpRootBridgeHelloTime':magnumBrStpRootBridgeHelloTime,'magnumBrStpRootBridgeFwdDelay':magnumBrStpRootBridgeFwdDelay,'magnumBrStpBridgeId':magnumBrStpBridgeId,'magnumBrStpBridgeMaxAge':magnumBrStpBridgeMaxAge,'magnumBrStpBridgeHelloTime':magnumBrStpBridgeHelloTime,'magnumBrStpBridgeFwdDelay':magnumBrStpBridgeFwdDelay,'magnumBrStpTopChangeDetected':magnumBrStpTopChangeDetected,'magnumBrStpTopChange':magnumBrStpTopChange,'magnumBrStpHoldTime':magnumBrStpHoldTime,'magnumBrStpAdminStatus':magnumBrStpAdminStatus,'magnumStpPortTable':magnumStpPortTable,'magnumStpPortEntry':magnumStpPortEntry,_A6:magnumStpPort,'magnumStpPortState':magnumStpPortState,'magnumStpPortPathCost':magnumStpPortPathCost,'magnumStpPortDesignatedRoot':magnumStpPortDesignatedRoot,'magnumStpPortDesignatedCost':magnumStpPortDesignatedCost,'magnumStpPortDesignatedBridge':magnumStpPortDesignatedBridge,'magnumStpPortDesignatedPort':magnumStpPortDesignatedPort,'magnumStpTopChangeAck':magnumStpTopChangeAck,'magnumStpConfigPending':magnumStpConfigPending,'magnumStpPortPriority':magnumStpPortPriority,'magnumBridgeGroup':magnumBridgeGroup,'magnumStpBridgeAgingTime':magnumStpBridgeAgingTime,'magnumMgtBridgeTime':magnumMgtBridgeTime,'magnumbridgeMacCount':magnumbridgeMacCount,'magnumEventMgrGroup':magnumEventMgrGroup,'magnumEventsRaised':magnumEventsRaised,'magnumSizeOfEventQueue':magnumSizeOfEventQueue,'magnumEventLogInvalidEvents':magnumEventLogInvalidEvents,'magnumEventLogCriticalEvents':magnumEventLogCriticalEvents,'magnumEventLogDebugEvents':magnumEventLogDebugEvents,'magnumEventLogFatalEvents':magnumEventLogFatalEvents,'magnumEventLogActivityEvents':magnumEventLogActivityEvents,'magnumEventLogInfoEvents':magnumEventLogInfoEvents,'magnumEventTable':magnumEventTable,'magnumEventEntry':magnumEventEntry,_A9:magnumEventIndex,'magnumEventCode':magnumEventCode,'magnumEventModuleId':magnumEventModuleId,'magnumEventSeverity':magnumEventSeverity,'magnumEventTimeStamp':magnumEventTimeStamp,'magnumTftpGroup':magnumTftpGroup,'magnumTFTPSeverIpAddress':magnumTFTPSeverIpAddress,'magnumTFTPRemoteFileName':magnumTFTPRemoteFileName,'magnumTFTPTransferType':magnumTFTPTransferType,'magnumTFTPAction':magnumTFTPAction,'magnumTFTPTrfrStatus':magnumTFTPTrfrStatus,'magnumSNTPGroup':magnumSNTPGroup,'sntpStatus':sntpStatus,'sntpTimeFormat':sntpTimeFormat,'sntpDateFormat':sntpDateFormat,'sntpDisplayDate':sntpDisplayDate,'sntpDisplayTime':sntpDisplayTime,'sntpDisplayTimeZone':sntpDisplayTimeZone,'sntpDayLightSavings':sntpDayLightSavings,'magnumSNTPTable':magnumSNTPTable,'magnumSNTPEntry':magnumSNTPEntry,_AA:sntpIndex,'sntpServerIp':sntpServerIp,'socketTimeout':socketTimeout,'noOfRetries':noOfRetries,'sntpOperation':sntpOperation,'magnumGVRPGroup':magnumGVRPGroup,'deviceGVRPState':deviceGVRPState,'magnumGVRPPortTable':magnumGVRPPortTable,'magnumGVRPPortEntry':magnumGVRPPortEntry,_AB:gvrpPortIndex,'gvrpPortState':gvrpPortState,'magnumPortManagerGroup':magnumPortManagerGroup,'magnumPortManagerTable':magnumPortManagerTable,'magnumPortManagerEntry':magnumPortManagerEntry,_Y:magnumPortNumber,'magnumPortName':magnumPortName,'magnumPortSpeed':magnumPortSpeed,'magnumPortDuplexMode':magnumPortDuplexMode,'magnumPortAutoNegotiationMode':magnumPortAutoNegotiationMode,'magnumPortFlowControl':magnumPortFlowControl,'magnumPortBackPressure':magnumPortBackPressure,'magnumPortVLANId':magnumPortVLANId,'magnumPortGVRPstate':magnumPortGVRPstate,'magnumPortSTPstate':magnumPortSTPstate,'magnumPortLinkState':magnumPortLinkState,'magnumPortInterfaceType':magnumPortInterfaceType,'magnumPortSecurityState':magnumPortSecurityState,'magnumPortTaggingState':magnumPortTaggingState,'magnumPortNotifyState':magnumPortNotifyState,'magnumPortStatsTable':magnumPortStatsTable,'magnumPortStatsEntry':magnumPortStatsEntry,_AC:portStatsIndex,'portBytesReceived':portBytesReceived,'portBytesSent':portBytesSent,'portFramesReceived':portFramesReceived,'portFramesSent':portFramesSent,'portTotalBytesReceived':portTotalBytesReceived,'portTotalFramesReceived':portTotalFramesReceived,'portBroadcastFramesReceived':portBroadcastFramesReceived,'portMulticastFramesReceived':portMulticastFramesReceived,'portCrcErrors':portCrcErrors,'portOversizeFrames':portOversizeFrames,'portFragments':portFragments,'portJabbers':portJabbers,'portCollissions':portCollissions,'portLateCollissions':portLateCollissions,'portFrames67-127':portFrames67_127,'portFrames128-255':portFrames128_255,'portFrames256-511':portFrames256_511,'portFrames512-1023':portFrames512_1023,'portFrames1024-MaxSize':portFrames1024_MaxSize,'portMacRxErrors':portMacRxErrors,'portDroppedFrames':portDroppedFrames,'portOutMulticastFrames':portOutMulticastFrames,'portOutBroadcastFrames':portOutBroadcastFrames,'portUndersizeFrames':portUndersizeFrames,'portClearStatistics':portClearStatistics,'magnumPortQosTable':magnumPortQosTable,'magnumPortQosEntry':magnumPortQosEntry,'magnumPortQosIndex':magnumPortQosIndex,'magnumPortQosPriority':magnumPortQosPriority,'magnumTypeOfService':magnumTypeOfService,'magnumDeviceQosTable':magnumDeviceQosTable,'magnumDeviceQosEntry':magnumDeviceQosEntry,_AD:magnumDeviceQosIndex,'magnumDefaultQos':magnumDefaultQos,'magnumTagQos':magnumTagQos,'magnumIpQos':magnumIpQos,'magnumConfigManagerGroup':magnumConfigManagerGroup,'saveConfig':saveConfig,'magnumIGMPGroup':magnumIGMPGroup,'deviceIGMPState':deviceIGMPState,'immediateLeave':immediateLeave,'switchQuerier':switchQuerier,'queryInterval':queryInterval,'queryResponseInterval':queryResponseInterval,'magnumIGMPGroupTable':magnumIGMPGroupTable,'magnumIGMPGroupEntry':magnumIGMPGroupEntry,_AE:igmpGroupIndex,'igmpGroupAddress':igmpGroupAddress,'igmpGroupPort':igmpGroupPort,'igmpGroupTimer':igmpGroupTimer,'igmpGroupLeaveP':igmpGroupLeaveP,'magnumIGMPRouterTable':magnumIGMPRouterTable,'magnumIGMPRouterEntry':magnumIGMPRouterEntry,_AF:igmpRouterIndex,'igmpRouterAddress':igmpRouterAddress,'igmpRouterPort':igmpRouterPort,'igmpRouterTimer':igmpRouterTimer,'magnumIGMPPortTable':magnumIGMPPortTable,'magnumIGMPPortEntry':magnumIGMPPortEntry,_AG:igmpPortIndex,'igmpPortMode':igmpPortMode,'unknownMcast':unknownMcast,'sring':sring,'sringControl':sringControl,'sringTable':sringTable,'sringEntry':sringEntry,_AH:sringIndex,'sringPort1':sringPort1,'sringPort2':sringPort2,'sringStatus':sringStatus,'lll':lll,'lllControl':lllControl,'lllPortMap':lllPortMap,_W:alarm,'alarmControl':alarmControl,'alarmWidth':alarmWidth,'alarmTable':alarmTable,'alarmEntry':alarmEntry,_AI:alarmIndex,'alarmEvent':alarmEvent,'alarmType':alarmType,'alarmDesc':alarmDesc,'alarmStatus':alarmStatus,'alarmFlag':alarmFlag,'dualhome':dualhome,'dhControl':dhControl,'dhMode':dhMode,'dhActive':dhActive,'dhPort1':dhPort1,'dhPort2':dhPort2,'max16':max16,'max32':max32,'max8':max8,'max32t':max32t,'maxq':maxq,'mx-events':mx_events,'m6kIntruderTrap':m6kIntruderTrap,'m6kSringOpenTrap':m6kSringOpenTrap,'m6kSringClosedTrap':m6kSringClosedTrap,'m6kLLLTrap':m6kLLLTrap,'m6kPMPTrap':m6kPMPTrap,'m6kUserAuthFailTrap':m6kUserAuthFailTrap,'m6kPowerAlarmTrap':m6kPowerAlarmTrap,'m6kSTPEnabledTrap':m6kSTPEnabledTrap,'m6kRSTPEnabledTrap':m6kRSTPEnabledTrap,'m6kSTPDisabledTrap':m6kSTPDisabledTrap,'m6kRSTPDisabledTrap':m6kRSTPDisabledTrap,'m6kFanAlarmTrap':m6kFanAlarmTrap,'userAuthFail':userAuthFail,'mode':mode,'userIpAddress':userIpAddress,'powerAlarm':powerAlarm,'powerSupplyFailed':powerSupplyFailed,'fanAlarm':fanAlarm,'fanNumber':fanNumber,'fanStatus':fanStatus,'max25e':max25e,'max32f':max32f,'max32fc':max32fc,'maxqe':maxqe,'maxl':maxl,'max1000':max1000,'magnum10kt':magnum10kt,'maxm':maxm,'max25m':max25m,'magnum10kg':magnum10kg})