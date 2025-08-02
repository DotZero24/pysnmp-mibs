_a='nbsStackVcdPortId'
_Z='supported'
_Y='notSupported'
_X='nbsStackMultiConPortConnectorNumber'
_W='nbsStackMultiConPortNumber'
_V='nbsStackMultiConPortId'
_U='nbsStackSlotSpecUplNumber'
_T='nbsStackSlotUplNumber'
_S='nbsStackSlotNumber'
_R='disabled'
_Q='enabled'
_P='unknown'
_O='nbsStackSlotIndex'
_N='nbsStackSlotSpecNumber'
_M='shortCable'
_L='openCable'
_K='impedanceMismatch'
_J='testFail'
_I='good'
_H='down'
_G='up'
_F='read-write'
_E='NSTACK-MIB'
_D='other'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
class PortsBitmap(OctetString):0
_Nbase_ObjectIdentity=ObjectIdentity
nbase=_Nbase_ObjectIdentity((1,3,6,1,4,1,629))
_NbSwitchG1_ObjectIdentity=ObjectIdentity
nbSwitchG1=_NbSwitchG1_ObjectIdentity((1,3,6,1,4,1,629,1))
_NbSwitchG1Il_ObjectIdentity=ObjectIdentity
nbSwitchG1Il=_NbSwitchG1Il_ObjectIdentity((1,3,6,1,4,1,629,1,50))
_NbsStackInfo_ObjectIdentity=ObjectIdentity
nbsStackInfo=_NbsStackInfo_ObjectIdentity((1,3,6,1,4,1,629,1,50,4))
_NbsStackSlotCapacity_Type=Integer32
_NbsStackSlotCapacity_Object=MibScalar
nbsStackSlotCapacity=_NbsStackSlotCapacity_Object((1,3,6,1,4,1,629,1,50,4,1),_NbsStackSlotCapacity_Type())
nbsStackSlotCapacity.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsStackSlotCapacity.setStatus(_A)
_NbsStackSlotsTableSize_Type=Integer32
_NbsStackSlotsTableSize_Object=MibScalar
nbsStackSlotsTableSize=_NbsStackSlotsTableSize_Object((1,3,6,1,4,1,629,1,50,4,2),_NbsStackSlotsTableSize_Type())
nbsStackSlotsTableSize.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsStackSlotsTableSize.setStatus(_A)
_NbsStackPortsCapacity_Type=Integer32
_NbsStackPortsCapacity_Object=MibScalar
nbsStackPortsCapacity=_NbsStackPortsCapacity_Object((1,3,6,1,4,1,629,1,50,4,3),_NbsStackPortsCapacity_Type())
nbsStackPortsCapacity.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsStackPortsCapacity.setStatus(_A)
_NbsStackSlotPortsCapacity_Type=Integer32
_NbsStackSlotPortsCapacity_Object=MibScalar
nbsStackSlotPortsCapacity=_NbsStackSlotPortsCapacity_Object((1,3,6,1,4,1,629,1,50,4,4),_NbsStackSlotPortsCapacity_Type())
nbsStackSlotPortsCapacity.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsStackSlotPortsCapacity.setStatus(_A)
_NbsStackSlotTable_Object=MibTable
nbsStackSlotTable=_NbsStackSlotTable_Object((1,3,6,1,4,1,629,1,50,4,5))
if mibBuilder.loadTexts:nbsStackSlotTable.setStatus(_A)
_NbsStackSlotEntry_Object=MibTableRow
nbsStackSlotEntry=_NbsStackSlotEntry_Object((1,3,6,1,4,1,629,1,50,4,5,1))
nbsStackSlotEntry.setIndexNames((0,_E,_O))
if mibBuilder.loadTexts:nbsStackSlotEntry.setStatus(_A)
_NbsStackSlotIndex_Type=Integer32
_NbsStackSlotIndex_Object=MibTableColumn
nbsStackSlotIndex=_NbsStackSlotIndex_Object((1,3,6,1,4,1,629,1,50,4,5,1,1),_NbsStackSlotIndex_Type())
nbsStackSlotIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsStackSlotIndex.setStatus(_A)
class _NbsStackSlotType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120)));namedValues=NamedValues(*(('empty',1),(_P,2),('standAlone',3),('universal',4),('eth20Ports10or100TP',5),('eth40Ports10TP',6),('eth10Ports100FO',7),('eth16Ports10or100TP',8),('eth4Ports1000FO',9),('agentSlot',10),('routingEngine',11),('eth8Ports10or100TP',12),('eth2Ports100FOMM',13),('eth2Ports100FOSM',14),('eth1Ports1000FOMM',15),('eth1Ports1000FOSM',16),('eth2Ports1000FOMM',17),('eth2Ports1000FOSM',18),('stackableSlotNoLink',19),('stackableSlotNH2025',20),('stackableSlotReserve1',21),('stackableSlotReserve2',22),('eth2Ports100FO',23),('eth2Ports1000FO',24),('eth4Ports100FOMM',25),('eth4Ports100FOSM',26),('eth4Ports100FO',27),('eth4Ports10or100TP',28),('eth4Ports100MTRJ',29),('eth8Ports100MTRJ',30),('eth4Ports100VF',31),('eth8Ports100VF',32),('ethGigaBitService',33),('eth4Ports100LC',34),('eth8Ports100LC',35),('eth2Ports10FL',36),('eth4Ports10FL',37),('eth1Port100or1000TP',38),('eth1Port1000FORED',39),('eth4Ports100TPand2Ports100FO',40),('eth4Ports100TPand1Port100FO',41),('eth0Ports100TPand2Ports100FO',42),('eth4Ports100TPand0Ports100FO',43),('eth1Ports1000MTRJ',44),('eth1StackPorts100or1000TP',45),('eth2PseudoMgmt10or100TP',46),('eth4Ports10HPNA',47),('eth8Ports10HPNA',48),('eth1Port1000AMP',49),('l3eth1Ports1000FO',50),('l3eth8Ports10or100TP',51),('l3eth4Ports100TPand1Port100FO',52),('l3eth8Ports100MTRJ',53),('l3eth4Ports100LC',54),('l3eth8Ports100LC',55),('l3eth2Ports10FL',56),('l3eth4Ports10FL',57),('l3eth4Ports100MTRJ',58),('l3eth0Ports100TPand2Ports100FO',59),('l3eth2Ports1000FO',60),('l3eth4Ports100FO',61),('l3eth4Ports100TPand0Ports100FO',62),('l3eth4Ports100VF',63),('l3eth8Ports100VF',64),('l3eth4Ports100TPand2Ports100FO',65),('l3eth1Port100or1000TP',66),('l3eth1Port1000FORED',67),('l3eth1Ports1000MTRJ',68),('l3eth1Port1000AMP',69),('l3eth4Ports10HPNA',70),('l3eth8Ports10HPNA',71),('l3eth2Ports10or100RC',72),('eth2Ports1000FOSM50Mcam16',73),('eth2Ports1000FOSM50Mcam32',74),('eth1Ports1000FOSM50Mcam16',75),('eth1Ports1000FOSM50Mcam32',76),('eth2Ports1000FOSM100Mcam16',77),('eth2Ports1000FOSM100Mcam32',78),('eth1Ports1000FOSM100Mcam16',79),('eth1Ports1000FOSM100Mcam32',80),('eth8singlePortsEoVL',81),('eth8singlePortsEoVN',82),('eth8singlePortsLEoVL',83),('eth8singlePortsLEoVN',84),('eth4PortsEoVand2Ports100FO',85),('eth4PortsEoVand2Ports10or100TP',86),('eth4singlePortsEoVL4PortsEoVN',87),('eth2Ports100FOPAL',88),('eth4PortsEoVand1Ports100FO',89),('eth4PortsEoVand1Ports10or100TP',90),('eth4PortsEoVand1Ports10or100TPand1Ports100FO',91),('l3eth8octalPortsEoVL',92),('l3eth1Port1000GBICSFP',93),('l3eth2Ports100FOPAL',94),('eth8octalPortsEoVSL',95),('l3eth8octalPortsEoVSL',96),('eth8octalPortsEoV7L',97),('l3eth8octalPortsEoV7L',98),('l3eth8PortVoice',99),('l3eth4PortVoice',100),('l3eth2PortVoiceand2PortsTPand1PortFO',101),('eth4Ports100TPand1PortSingleFO',102),('l3eth4Ports100TPand1PortSingleFO',103),('eth8octalPortsEoVL',104),('eth8singlePortsEoVED',105),('eth8singlePortsEoV4B',106),('l3eth1Port1000SFP',107),('eth1Port1000GERcam32',108),('eth1Port1000GERcam256',109),('eth1Port1000GERSFPcam32',110),('eth1Port1000GERSFPcam256',111),('eth1Port1000SFPcam32',112),('eth1Port1000SFPcam256',113),('eth6Ports100TPand2Ports100FO',114),('em2007eth1Port1000SFPcam32',115),('em2007eth1Port1000SFPcam256',116),('em2007eth8Ports10or100TP',117),('em2007eth8Ports100MTRJ',118),('em2007eth1Port1000GERSFPcam32',119),('eth6Ports100TPand1Ports100FO',120)))
_NbsStackSlotType_Type.__name__=_C
_NbsStackSlotType_Object=MibTableColumn
nbsStackSlotType=_NbsStackSlotType_Object((1,3,6,1,4,1,629,1,50,4,5,1,2),_NbsStackSlotType_Type())
nbsStackSlotType.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsStackSlotType.setStatus(_A)
class _NbsStackSlotMgmtStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('master',1),('slave',2)))
_NbsStackSlotMgmtStatus_Type.__name__=_C
_NbsStackSlotMgmtStatus_Object=MibTableColumn
nbsStackSlotMgmtStatus=_NbsStackSlotMgmtStatus_Object((1,3,6,1,4,1,629,1,50,4,5,1,3),_NbsStackSlotMgmtStatus_Type())
nbsStackSlotMgmtStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsStackSlotMgmtStatus.setStatus(_A)
_NbsStackSlotPortsMaxNumber_Type=Integer32
_NbsStackSlotPortsMaxNumber_Object=MibTableColumn
nbsStackSlotPortsMaxNumber=_NbsStackSlotPortsMaxNumber_Object((1,3,6,1,4,1,629,1,50,4,5,1,4),_NbsStackSlotPortsMaxNumber_Type())
nbsStackSlotPortsMaxNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsStackSlotPortsMaxNumber.setStatus(_A)
_NbsStackSlotPortsNumber_Type=Integer32
_NbsStackSlotPortsNumber_Object=MibTableColumn
nbsStackSlotPortsNumber=_NbsStackSlotPortsNumber_Object((1,3,6,1,4,1,629,1,50,4,5,1,5),_NbsStackSlotPortsNumber_Type())
nbsStackSlotPortsNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsStackSlotPortsNumber.setStatus(_A)
_NbsStackSlotFirstPort_Type=Integer32
_NbsStackSlotFirstPort_Object=MibTableColumn
nbsStackSlotFirstPort=_NbsStackSlotFirstPort_Object((1,3,6,1,4,1,629,1,50,4,5,1,6),_NbsStackSlotFirstPort_Type())
nbsStackSlotFirstPort.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsStackSlotFirstPort.setStatus(_A)
class _NbsStackSlotOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('switchedOff',1),(_Q,2),(_R,3),('changing',4)))
_NbsStackSlotOperStatus_Type.__name__=_C
_NbsStackSlotOperStatus_Object=MibTableColumn
nbsStackSlotOperStatus=_NbsStackSlotOperStatus_Object((1,3,6,1,4,1,629,1,50,4,5,1,7),_NbsStackSlotOperStatus_Type())
nbsStackSlotOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsStackSlotOperStatus.setStatus(_A)
class _NbsStackSlotAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_R,2)))
_NbsStackSlotAdminStatus_Type.__name__=_C
_NbsStackSlotAdminStatus_Object=MibTableColumn
nbsStackSlotAdminStatus=_NbsStackSlotAdminStatus_Object((1,3,6,1,4,1,629,1,50,4,5,1,8),_NbsStackSlotAdminStatus_Type())
nbsStackSlotAdminStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:nbsStackSlotAdminStatus.setStatus(_A)
class _NbsStackSlotRedundantPSMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('notConnected',1),('connected',2)))
_NbsStackSlotRedundantPSMode_Type.__name__=_C
_NbsStackSlotRedundantPSMode_Object=MibTableColumn
nbsStackSlotRedundantPSMode=_NbsStackSlotRedundantPSMode_Object((1,3,6,1,4,1,629,1,50,4,5,1,9),_NbsStackSlotRedundantPSMode_Type())
nbsStackSlotRedundantPSMode.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsStackSlotRedundantPSMode.setStatus(_A)
_NbsStackSlotUplinkModulesNumber_Type=Integer32
_NbsStackSlotUplinkModulesNumber_Object=MibTableColumn
nbsStackSlotUplinkModulesNumber=_NbsStackSlotUplinkModulesNumber_Object((1,3,6,1,4,1,629,1,50,4,5,1,10),_NbsStackSlotUplinkModulesNumber_Type())
nbsStackSlotUplinkModulesNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsStackSlotUplinkModulesNumber.setStatus(_A)
class _NbsStackSlotReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('running',1),('reset',2)))
_NbsStackSlotReset_Type.__name__=_C
_NbsStackSlotReset_Object=MibTableColumn
nbsStackSlotReset=_NbsStackSlotReset_Object((1,3,6,1,4,1,629,1,50,4,5,1,11),_NbsStackSlotReset_Type())
nbsStackSlotReset.setMaxAccess(_F)
if mibBuilder.loadTexts:nbsStackSlotReset.setStatus(_A)
_NbsStackSlotIp_Type=IpAddress
_NbsStackSlotIp_Object=MibTableColumn
nbsStackSlotIp=_NbsStackSlotIp_Object((1,3,6,1,4,1,629,1,50,4,5,1,12),_NbsStackSlotIp_Type())
nbsStackSlotIp.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsStackSlotIp.setStatus(_A)
_NbsStackSlotHwVers_Type=Integer32
_NbsStackSlotHwVers_Object=MibTableColumn
nbsStackSlotHwVers=_NbsStackSlotHwVers_Object((1,3,6,1,4,1,629,1,50,4,5,1,13),_NbsStackSlotHwVers_Type())
nbsStackSlotHwVers.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsStackSlotHwVers.setStatus(_A)
_NbsStackSlotSwVers_Type=Integer32
_NbsStackSlotSwVers_Object=MibTableColumn
nbsStackSlotSwVers=_NbsStackSlotSwVers_Object((1,3,6,1,4,1,629,1,50,4,5,1,14),_NbsStackSlotSwVers_Type())
nbsStackSlotSwVers.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsStackSlotSwVers.setStatus(_A)
_NbsStackSlotUplTable_Object=MibTable
nbsStackSlotUplTable=_NbsStackSlotUplTable_Object((1,3,6,1,4,1,629,1,50,4,6))
if mibBuilder.loadTexts:nbsStackSlotUplTable.setStatus(_A)
_NbsStackSlotUplEntry_Object=MibTableRow
nbsStackSlotUplEntry=_NbsStackSlotUplEntry_Object((1,3,6,1,4,1,629,1,50,4,6,1))
nbsStackSlotUplEntry.setIndexNames((0,_E,_S),(0,_E,_T))
if mibBuilder.loadTexts:nbsStackSlotUplEntry.setStatus(_A)
_NbsStackSlotNumber_Type=Integer32
_NbsStackSlotNumber_Object=MibTableColumn
nbsStackSlotNumber=_NbsStackSlotNumber_Object((1,3,6,1,4,1,629,1,50,4,6,1,1),_NbsStackSlotNumber_Type())
nbsStackSlotNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsStackSlotNumber.setStatus(_A)
_NbsStackSlotUplNumber_Type=Integer32
_NbsStackSlotUplNumber_Object=MibTableColumn
nbsStackSlotUplNumber=_NbsStackSlotUplNumber_Object((1,3,6,1,4,1,629,1,50,4,6,1,2),_NbsStackSlotUplNumber_Type())
nbsStackSlotUplNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsStackSlotUplNumber.setStatus(_A)
class _NbsStackSlotUplType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94)));namedValues=NamedValues(*(('uplAbsent',1),('uplUnknown',2),('upl1GigaMM',3),('upl1GigaSM',4),('upl2GigaMM',5),('upl2GigaSM',6),('upl1FO',7),('upl1TP',8),('upl2FOMM',9),('upl2FOSM',10),('upl4FOMM',11),('upl4FOSM',12),('upl8TP',13),('upl1ATM',14),('upl1FDDI',15),('uplStackModuleNoLink',16),('uplStackModuleNH2025',17),('uplStackModuleReserve1',18),('uplStackModuleReserve2',19),('upl4TP',20),('upl2FO',21),('upl2Giga',22),('upl4FO',23),('upl4MTRJ',24),('upl8MTRJ',25),('upl4VF',26),('upl8VF',27),('upl4LC',28),('upl8LC',29),('upl2FL',30),('upl4FL',31),('upl1GigaTP',32),('upl1GER',33),('upl4TP2FO',34),('upl4TP1FO',35),('upl0TP2FO',36),('upl4TP0FO',37),('upl1GigaMTRJ',38),('upl1GigaStackTP',39),('upl4Ports10HPNA',40),('upl8Ports10HPNA',41),('upl1Port1000AMP',42),('l3upl1Giga1000',43),('l3upl8TP',44),('l3upl4TP1FO',45),('l3upl8MTRJ',46),('l3upl4LC',47),('l3upl8LC',48),('l3upl2FL',49),('l3upl4FL',50),('l3upl4MTRJ',51),('l3upl0TP2FO',52),('l3upl2Giga',53),('l3upl4FO',54),('l3upl4TP0FO',55),('l3upl4VF',56),('l3upl8VF',57),('l3upl4TP2FO',58),('l3upl1Giga100or1000',59),('l3upl1GER',60),('l3upl1GigaMTRJ',61),('l3upl1Port1000AMP',62),('l3upl4Ports10HPNA',63),('l3upl8Ports10HPNA',64),('upl8singlePortsEoVL',65),('upl8singlePortsEoVN',66),('upl8singlePortsLEoVL',67),('upl8singlePortsLEoVN',68),('upl4PortsEoVand2FO',69),('upl4PortsEoVand2TP',70),('upl4singlePortsEoVL4PortsEoVN',71),('upl2Ports100FOPAL',72),('upl4PortsEoVand1Ports100FO',73),('upl4PortsEoVand1Ports10or100TP',74),('upl4PortsEoVand1Ports10or100TPand1Ports100FO',75),('l3upl8octalPortsEoVL',76),('l3upl1Port1000GBICSFP',77),('l3upl2Ports100FOPAL',78),('upl8octalPortsEoVSL',79),('upl8octalPortsEoV7L',80),('upl8octalPrtEoV7L',81),('l3upl8octalPortsEoV7L',82),('l3upl8PortVoice',83),('l3upl4PortVoice',84),('l3upl2PortVoiceand2PortsTPand1PortFO',85),('upl4TP1SingleFO',86),('l3upl4TP1SingleFO',87),('upl8octalPortsEoVL',88),('upl8singlePortsEoVED',89),('upl8singlePortsEoV4B',90),('upl9Ces',91),('upl9Ces4',92),('upl9kCes4',93),('upl9kCes',94)))
_NbsStackSlotUplType_Type.__name__=_C
_NbsStackSlotUplType_Object=MibTableColumn
nbsStackSlotUplType=_NbsStackSlotUplType_Object((1,3,6,1,4,1,629,1,50,4,6,1,3),_NbsStackSlotUplType_Type())
nbsStackSlotUplType.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsStackSlotUplType.setStatus(_A)
_NbsStackSlotUplSwVers_Type=Integer32
_NbsStackSlotUplSwVers_Object=MibTableColumn
nbsStackSlotUplSwVers=_NbsStackSlotUplSwVers_Object((1,3,6,1,4,1,629,1,50,4,6,1,4),_NbsStackSlotUplSwVers_Type())
nbsStackSlotUplSwVers.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsStackSlotUplSwVers.setStatus(_A)
_NbsStackSlotUplHwVers_Type=Integer32
_NbsStackSlotUplHwVers_Object=MibTableColumn
nbsStackSlotUplHwVers=_NbsStackSlotUplHwVers_Object((1,3,6,1,4,1,629,1,50,4,6,1,5),_NbsStackSlotUplHwVers_Type())
nbsStackSlotUplHwVers.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsStackSlotUplHwVers.setStatus(_A)
_NbsStackSlotUplNPorts_Type=Integer32
_NbsStackSlotUplNPorts_Object=MibTableColumn
nbsStackSlotUplNPorts=_NbsStackSlotUplNPorts_Object((1,3,6,1,4,1,629,1,50,4,6,1,6),_NbsStackSlotUplNPorts_Type())
nbsStackSlotUplNPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsStackSlotUplNPorts.setStatus(_A)
_NbsStackSlotUplFirstPort_Type=Integer32
_NbsStackSlotUplFirstPort_Object=MibTableColumn
nbsStackSlotUplFirstPort=_NbsStackSlotUplFirstPort_Object((1,3,6,1,4,1,629,1,50,4,6,1,7),_NbsStackSlotUplFirstPort_Type())
nbsStackSlotUplFirstPort.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsStackSlotUplFirstPort.setStatus(_A)
_NbsStackSlotUplPortsMask_Type=PortsBitmap
_NbsStackSlotUplPortsMask_Object=MibTableColumn
nbsStackSlotUplPortsMask=_NbsStackSlotUplPortsMask_Object((1,3,6,1,4,1,629,1,50,4,6,1,8),_NbsStackSlotUplPortsMask_Type())
nbsStackSlotUplPortsMask.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsStackSlotUplPortsMask.setStatus(_A)
class _NbsStackSlotUplStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_NbsStackSlotUplStatus_Type.__name__=_C
_NbsStackSlotUplStatus_Object=MibTableColumn
nbsStackSlotUplStatus=_NbsStackSlotUplStatus_Object((1,3,6,1,4,1,629,1,50,4,6,1,9),_NbsStackSlotUplStatus_Type())
nbsStackSlotUplStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsStackSlotUplStatus.setStatus(_A)
_NbsStackSlotUplHwDescr_Type=DisplayString
_NbsStackSlotUplHwDescr_Object=MibTableColumn
nbsStackSlotUplHwDescr=_NbsStackSlotUplHwDescr_Object((1,3,6,1,4,1,629,1,50,4,6,1,10),_NbsStackSlotUplHwDescr_Type())
nbsStackSlotUplHwDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsStackSlotUplHwDescr.setStatus(_A)
_NbsStackSlotUplSwDescr_Type=DisplayString
_NbsStackSlotUplSwDescr_Object=MibTableColumn
nbsStackSlotUplSwDescr=_NbsStackSlotUplSwDescr_Object((1,3,6,1,4,1,629,1,50,4,6,1,11),_NbsStackSlotUplSwDescr_Type())
nbsStackSlotUplSwDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsStackSlotUplSwDescr.setStatus(_A)
_NbsStackSpecSlotTable_Object=MibTable
nbsStackSpecSlotTable=_NbsStackSpecSlotTable_Object((1,3,6,1,4,1,629,1,50,4,7))
if mibBuilder.loadTexts:nbsStackSpecSlotTable.setStatus(_A)
_NbsStackSpecSlotEntry_Object=MibTableRow
nbsStackSpecSlotEntry=_NbsStackSpecSlotEntry_Object((1,3,6,1,4,1,629,1,50,4,7,1))
nbsStackSpecSlotEntry.setIndexNames((0,_E,_N),(0,_E,_U))
if mibBuilder.loadTexts:nbsStackSpecSlotEntry.setStatus(_A)
_NbsStackSlotSpecNumber_Type=Integer32
_NbsStackSlotSpecNumber_Object=MibTableColumn
nbsStackSlotSpecNumber=_NbsStackSlotSpecNumber_Object((1,3,6,1,4,1,629,1,50,4,7,1,1),_NbsStackSlotSpecNumber_Type())
nbsStackSlotSpecNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsStackSlotSpecNumber.setStatus(_A)
_NbsStackSlotSpecUplNumber_Type=Integer32
_NbsStackSlotSpecUplNumber_Object=MibTableColumn
nbsStackSlotSpecUplNumber=_NbsStackSlotSpecUplNumber_Object((1,3,6,1,4,1,629,1,50,4,7,1,2),_NbsStackSlotSpecUplNumber_Type())
nbsStackSlotSpecUplNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsStackSlotSpecUplNumber.setStatus(_A)
class _NbsStackSlotSpecUplRedundantMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_D,1),('specialRedundant',2),('autoRedundant',3),('manualLeftRedundant',4),('manualRightRedundant',5),('regularRedundant',6),('masterLeftRedundant',7),('masterRightRedundant',8)))
_NbsStackSlotSpecUplRedundantMode_Type.__name__=_C
_NbsStackSlotSpecUplRedundantMode_Object=MibTableColumn
nbsStackSlotSpecUplRedundantMode=_NbsStackSlotSpecUplRedundantMode_Object((1,3,6,1,4,1,629,1,50,4,7,1,3),_NbsStackSlotSpecUplRedundantMode_Type())
nbsStackSlotSpecUplRedundantMode.setMaxAccess(_F)
if mibBuilder.loadTexts:nbsStackSlotSpecUplRedundantMode.setStatus(_A)
class _NbsStackSlotSpecUplLeftLinkLed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_G,2),(_H,3)))
_NbsStackSlotSpecUplLeftLinkLed_Type.__name__=_C
_NbsStackSlotSpecUplLeftLinkLed_Object=MibTableColumn
nbsStackSlotSpecUplLeftLinkLed=_NbsStackSlotSpecUplLeftLinkLed_Object((1,3,6,1,4,1,629,1,50,4,7,1,4),_NbsStackSlotSpecUplLeftLinkLed_Type())
nbsStackSlotSpecUplLeftLinkLed.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsStackSlotSpecUplLeftLinkLed.setStatus(_A)
class _NbsStackSlotSpecUplLeftActivityLed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_G,2),(_H,3)))
_NbsStackSlotSpecUplLeftActivityLed_Type.__name__=_C
_NbsStackSlotSpecUplLeftActivityLed_Object=MibTableColumn
nbsStackSlotSpecUplLeftActivityLed=_NbsStackSlotSpecUplLeftActivityLed_Object((1,3,6,1,4,1,629,1,50,4,7,1,5),_NbsStackSlotSpecUplLeftActivityLed_Type())
nbsStackSlotSpecUplLeftActivityLed.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsStackSlotSpecUplLeftActivityLed.setStatus(_A)
class _NbsStackSlotSpecUplRightLinkLed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_G,2),(_H,3)))
_NbsStackSlotSpecUplRightLinkLed_Type.__name__=_C
_NbsStackSlotSpecUplRightLinkLed_Object=MibTableColumn
nbsStackSlotSpecUplRightLinkLed=_NbsStackSlotSpecUplRightLinkLed_Object((1,3,6,1,4,1,629,1,50,4,7,1,6),_NbsStackSlotSpecUplRightLinkLed_Type())
nbsStackSlotSpecUplRightLinkLed.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsStackSlotSpecUplRightLinkLed.setStatus(_A)
class _NbsStackSlotSpecUplRightActivityLed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_G,2),(_H,3)))
_NbsStackSlotSpecUplRightActivityLed_Type.__name__=_C
_NbsStackSlotSpecUplRightActivityLed_Object=MibTableColumn
nbsStackSlotSpecUplRightActivityLed=_NbsStackSlotSpecUplRightActivityLed_Object((1,3,6,1,4,1,629,1,50,4,7,1,7),_NbsStackSlotSpecUplRightActivityLed_Type())
nbsStackSlotSpecUplRightActivityLed.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsStackSlotSpecUplRightActivityLed.setStatus(_A)
class _NbsStackSlotSpecUplTestSemiAutoMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('readyForTest',1),('startTest',2)))
_NbsStackSlotSpecUplTestSemiAutoMode_Type.__name__=_C
_NbsStackSlotSpecUplTestSemiAutoMode_Object=MibTableColumn
nbsStackSlotSpecUplTestSemiAutoMode=_NbsStackSlotSpecUplTestSemiAutoMode_Object((1,3,6,1,4,1,629,1,50,4,7,1,8),_NbsStackSlotSpecUplTestSemiAutoMode_Type())
nbsStackSlotSpecUplTestSemiAutoMode.setMaxAccess(_F)
if mibBuilder.loadTexts:nbsStackSlotSpecUplTestSemiAutoMode.setStatus(_A)
_NbsStackMultiConPortGroup_ObjectIdentity=ObjectIdentity
nbsStackMultiConPortGroup=_NbsStackMultiConPortGroup_ObjectIdentity((1,3,6,1,4,1,629,1,50,4,10))
_NbsStackMultiConPortTable_Object=MibTable
nbsStackMultiConPortTable=_NbsStackMultiConPortTable_Object((1,3,6,1,4,1,629,1,50,4,10,5))
if mibBuilder.loadTexts:nbsStackMultiConPortTable.setStatus(_A)
_NbsStackMultiConPortEntry_Object=MibTableRow
nbsStackMultiConPortEntry=_NbsStackMultiConPortEntry_Object((1,3,6,1,4,1,629,1,50,4,10,5,1))
nbsStackMultiConPortEntry.setIndexNames((0,_E,_V))
if mibBuilder.loadTexts:nbsStackMultiConPortEntry.setStatus(_A)
_NbsStackMultiConPortId_Type=Integer32
_NbsStackMultiConPortId_Object=MibTableColumn
nbsStackMultiConPortId=_NbsStackMultiConPortId_Object((1,3,6,1,4,1,629,1,50,4,10,5,1,1),_NbsStackMultiConPortId_Type())
nbsStackMultiConPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsStackMultiConPortId.setStatus(_A)
_NbsStackMultiConPortConnectorsNumber_Type=Integer32
_NbsStackMultiConPortConnectorsNumber_Object=MibTableColumn
nbsStackMultiConPortConnectorsNumber=_NbsStackMultiConPortConnectorsNumber_Object((1,3,6,1,4,1,629,1,50,4,10,5,1,2),_NbsStackMultiConPortConnectorsNumber_Type())
nbsStackMultiConPortConnectorsNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsStackMultiConPortConnectorsNumber.setStatus(_A)
class _NbsStackMultiConPortForceMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),('auto',2),('force',3)))
_NbsStackMultiConPortForceMode_Type.__name__=_C
_NbsStackMultiConPortForceMode_Object=MibTableColumn
nbsStackMultiConPortForceMode=_NbsStackMultiConPortForceMode_Object((1,3,6,1,4,1,629,1,50,4,10,5,1,3),_NbsStackMultiConPortForceMode_Type())
nbsStackMultiConPortForceMode.setMaxAccess(_F)
if mibBuilder.loadTexts:nbsStackMultiConPortForceMode.setStatus(_A)
_NbsStackMultiConPortForcedConnector_Type=Integer32
_NbsStackMultiConPortForcedConnector_Object=MibTableColumn
nbsStackMultiConPortForcedConnector=_NbsStackMultiConPortForcedConnector_Object((1,3,6,1,4,1,629,1,50,4,10,5,1,4),_NbsStackMultiConPortForcedConnector_Type())
nbsStackMultiConPortForcedConnector.setMaxAccess(_F)
if mibBuilder.loadTexts:nbsStackMultiConPortForcedConnector.setStatus(_A)
_NbsStackMultiConPortConnectorTable_Object=MibTable
nbsStackMultiConPortConnectorTable=_NbsStackMultiConPortConnectorTable_Object((1,3,6,1,4,1,629,1,50,4,10,7))
if mibBuilder.loadTexts:nbsStackMultiConPortConnectorTable.setStatus(_A)
_NbsStackMultiConPortConnectorEntry_Object=MibTableRow
nbsStackMultiConPortConnectorEntry=_NbsStackMultiConPortConnectorEntry_Object((1,3,6,1,4,1,629,1,50,4,10,7,1))
nbsStackMultiConPortConnectorEntry.setIndexNames((0,_E,_W),(0,_E,_X))
if mibBuilder.loadTexts:nbsStackMultiConPortConnectorEntry.setStatus(_A)
_NbsStackMultiConPortNumber_Type=Integer32
_NbsStackMultiConPortNumber_Object=MibTableColumn
nbsStackMultiConPortNumber=_NbsStackMultiConPortNumber_Object((1,3,6,1,4,1,629,1,50,4,10,7,1,1),_NbsStackMultiConPortNumber_Type())
nbsStackMultiConPortNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsStackMultiConPortNumber.setStatus(_A)
_NbsStackMultiConPortConnectorNumber_Type=Integer32
_NbsStackMultiConPortConnectorNumber_Object=MibTableColumn
nbsStackMultiConPortConnectorNumber=_NbsStackMultiConPortConnectorNumber_Object((1,3,6,1,4,1,629,1,50,4,10,7,1,2),_NbsStackMultiConPortConnectorNumber_Type())
nbsStackMultiConPortConnectorNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsStackMultiConPortConnectorNumber.setStatus(_A)
class _NbsStackMultiConPortConnectorType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_D,1),('static',2),('gbic',3),('sfp',4),('xfp',5),('xfpe',6)))
_NbsStackMultiConPortConnectorType_Type.__name__=_C
_NbsStackMultiConPortConnectorType_Object=MibTableColumn
nbsStackMultiConPortConnectorType=_NbsStackMultiConPortConnectorType_Object((1,3,6,1,4,1,629,1,50,4,10,7,1,3),_NbsStackMultiConPortConnectorType_Type())
nbsStackMultiConPortConnectorType.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsStackMultiConPortConnectorType.setStatus(_A)
class _NbsStackMultiConPortConnectorSubType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_D,1),('rj45',2),('sc',3),('lc',4),('mtrj',5),('vf',6),('mu',7),('miniCoax',8),('mdiCx',9)))
_NbsStackMultiConPortConnectorSubType_Type.__name__=_C
_NbsStackMultiConPortConnectorSubType_Object=MibTableColumn
nbsStackMultiConPortConnectorSubType=_NbsStackMultiConPortConnectorSubType_Object((1,3,6,1,4,1,629,1,50,4,10,7,1,4),_NbsStackMultiConPortConnectorSubType_Type())
nbsStackMultiConPortConnectorSubType.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsStackMultiConPortConnectorSubType.setStatus(_A)
class _NbsStackMultiConPortConnectorLinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_D,1),('notLinked',2),('linked',3),('errorState',4),('blocked',5)))
_NbsStackMultiConPortConnectorLinkStatus_Type.__name__=_C
_NbsStackMultiConPortConnectorLinkStatus_Object=MibTableColumn
nbsStackMultiConPortConnectorLinkStatus=_NbsStackMultiConPortConnectorLinkStatus_Object((1,3,6,1,4,1,629,1,50,4,10,7,1,5),_NbsStackMultiConPortConnectorLinkStatus_Type())
nbsStackMultiConPortConnectorLinkStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsStackMultiConPortConnectorLinkStatus.setStatus(_A)
class _NbsStackMultiConPortConnectorRxLoss_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),('ok',2),('loss',3)))
_NbsStackMultiConPortConnectorRxLoss_Type.__name__=_C
_NbsStackMultiConPortConnectorRxLoss_Object=MibTableColumn
nbsStackMultiConPortConnectorRxLoss=_NbsStackMultiConPortConnectorRxLoss_Object((1,3,6,1,4,1,629,1,50,4,10,7,1,6),_NbsStackMultiConPortConnectorRxLoss_Type())
nbsStackMultiConPortConnectorRxLoss.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsStackMultiConPortConnectorRxLoss.setStatus(_A)
class _NbsStackMultiConPortConnectorTxFault_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),('ok',2),('fault',3)))
_NbsStackMultiConPortConnectorTxFault_Type.__name__=_C
_NbsStackMultiConPortConnectorTxFault_Object=MibTableColumn
nbsStackMultiConPortConnectorTxFault=_NbsStackMultiConPortConnectorTxFault_Object((1,3,6,1,4,1,629,1,50,4,10,7,1,7),_NbsStackMultiConPortConnectorTxFault_Type())
nbsStackMultiConPortConnectorTxFault.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsStackMultiConPortConnectorTxFault.setStatus(_A)
_NbsStackVcdGroup_ObjectIdentity=ObjectIdentity
nbsStackVcdGroup=_NbsStackVcdGroup_ObjectIdentity((1,3,6,1,4,1,629,1,50,4,12))
class _NbsStackVcdGenSupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Y,1),(_Z,2)))
_NbsStackVcdGenSupport_Type.__name__=_C
_NbsStackVcdGenSupport_Object=MibScalar
nbsStackVcdGenSupport=_NbsStackVcdGenSupport_Object((1,3,6,1,4,1,629,1,50,4,12,1),_NbsStackVcdGenSupport_Type())
nbsStackVcdGenSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsStackVcdGenSupport.setStatus(_A)
_NbsStackVcdPortTable_Object=MibTable
nbsStackVcdPortTable=_NbsStackVcdPortTable_Object((1,3,6,1,4,1,629,1,50,4,12,2))
if mibBuilder.loadTexts:nbsStackVcdPortTable.setStatus(_A)
_NbsStackVcdPortEntry_Object=MibTableRow
nbsStackVcdPortEntry=_NbsStackVcdPortEntry_Object((1,3,6,1,4,1,629,1,50,4,12,2,1))
nbsStackVcdPortEntry.setIndexNames((0,_E,_a))
if mibBuilder.loadTexts:nbsStackVcdPortEntry.setStatus(_A)
_NbsStackVcdPortId_Type=Integer32
_NbsStackVcdPortId_Object=MibTableColumn
nbsStackVcdPortId=_NbsStackVcdPortId_Object((1,3,6,1,4,1,629,1,50,4,12,2,1,1),_NbsStackVcdPortId_Type())
nbsStackVcdPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsStackVcdPortId.setStatus(_A)
class _NbsStackVcdPortTestRun_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('startVcdTest',1),('testIsRunning',2),('vcdTestCompletedOk',3),('vcdTestCompletedWithError',4),('vcdNotTested',5)))
_NbsStackVcdPortTestRun_Type.__name__=_C
_NbsStackVcdPortTestRun_Object=MibTableColumn
nbsStackVcdPortTestRun=_NbsStackVcdPortTestRun_Object((1,3,6,1,4,1,629,1,50,4,12,2,1,2),_NbsStackVcdPortTestRun_Type())
nbsStackVcdPortTestRun.setMaxAccess(_F)
if mibBuilder.loadTexts:nbsStackVcdPortTestRun.setStatus(_A)
_NbsStackVcdPortPair12Distance_Type=Integer32
_NbsStackVcdPortPair12Distance_Object=MibTableColumn
nbsStackVcdPortPair12Distance=_NbsStackVcdPortPair12Distance_Object((1,3,6,1,4,1,629,1,50,4,12,2,1,3),_NbsStackVcdPortPair12Distance_Type())
nbsStackVcdPortPair12Distance.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsStackVcdPortPair12Distance.setStatus(_A)
class _NbsStackVcdPortPair12TestStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_D,1),(_I,2),(_J,3),(_K,4),(_L,5),(_M,6)))
_NbsStackVcdPortPair12TestStatus_Type.__name__=_C
_NbsStackVcdPortPair12TestStatus_Object=MibTableColumn
nbsStackVcdPortPair12TestStatus=_NbsStackVcdPortPair12TestStatus_Object((1,3,6,1,4,1,629,1,50,4,12,2,1,4),_NbsStackVcdPortPair12TestStatus_Type())
nbsStackVcdPortPair12TestStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsStackVcdPortPair12TestStatus.setStatus(_A)
_NbsStackVcdPortPair36Distance_Type=Integer32
_NbsStackVcdPortPair36Distance_Object=MibTableColumn
nbsStackVcdPortPair36Distance=_NbsStackVcdPortPair36Distance_Object((1,3,6,1,4,1,629,1,50,4,12,2,1,5),_NbsStackVcdPortPair36Distance_Type())
nbsStackVcdPortPair36Distance.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsStackVcdPortPair36Distance.setStatus(_A)
class _NbsStackVcdPortPair36TestStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_D,1),(_I,2),(_J,3),(_K,4),(_L,5),(_M,6)))
_NbsStackVcdPortPair36TestStatus_Type.__name__=_C
_NbsStackVcdPortPair36TestStatus_Object=MibTableColumn
nbsStackVcdPortPair36TestStatus=_NbsStackVcdPortPair36TestStatus_Object((1,3,6,1,4,1,629,1,50,4,12,2,1,6),_NbsStackVcdPortPair36TestStatus_Type())
nbsStackVcdPortPair36TestStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsStackVcdPortPair36TestStatus.setStatus(_A)
_NbsStackVcdPortPair45Distance_Type=Integer32
_NbsStackVcdPortPair45Distance_Object=MibTableColumn
nbsStackVcdPortPair45Distance=_NbsStackVcdPortPair45Distance_Object((1,3,6,1,4,1,629,1,50,4,12,2,1,7),_NbsStackVcdPortPair45Distance_Type())
nbsStackVcdPortPair45Distance.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsStackVcdPortPair45Distance.setStatus(_A)
class _NbsStackVcdPortPair45TestStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_D,1),(_I,2),(_J,3),(_K,4),(_L,5),(_M,6)))
_NbsStackVcdPortPair45TestStatus_Type.__name__=_C
_NbsStackVcdPortPair45TestStatus_Object=MibTableColumn
nbsStackVcdPortPair45TestStatus=_NbsStackVcdPortPair45TestStatus_Object((1,3,6,1,4,1,629,1,50,4,12,2,1,8),_NbsStackVcdPortPair45TestStatus_Type())
nbsStackVcdPortPair45TestStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsStackVcdPortPair45TestStatus.setStatus(_A)
_NbsStackVcdPortPair78Distance_Type=Integer32
_NbsStackVcdPortPair78Distance_Object=MibTableColumn
nbsStackVcdPortPair78Distance=_NbsStackVcdPortPair78Distance_Object((1,3,6,1,4,1,629,1,50,4,12,2,1,9),_NbsStackVcdPortPair78Distance_Type())
nbsStackVcdPortPair78Distance.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsStackVcdPortPair78Distance.setStatus(_A)
class _NbsStackVcdPortPair78TestStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_D,1),(_I,2),(_J,3),(_K,4),(_L,5),(_M,6)))
_NbsStackVcdPortPair78TestStatus_Type.__name__=_C
_NbsStackVcdPortPair78TestStatus_Object=MibTableColumn
nbsStackVcdPortPair78TestStatus=_NbsStackVcdPortPair78TestStatus_Object((1,3,6,1,4,1,629,1,50,4,12,2,1,10),_NbsStackVcdPortPair78TestStatus_Type())
nbsStackVcdPortPair78TestStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsStackVcdPortPair78TestStatus.setStatus(_A)
class _NbsStackVcdPortSupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_Y,1),(_Z,2),(_P,3)))
_NbsStackVcdPortSupport_Type.__name__=_C
_NbsStackVcdPortSupport_Object=MibTableColumn
nbsStackVcdPortSupport=_NbsStackVcdPortSupport_Object((1,3,6,1,4,1,629,1,50,4,12,2,1,11),_NbsStackVcdPortSupport_Type())
nbsStackVcdPortSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsStackVcdPortSupport.setStatus(_A)
_NbsStackVcdPortTestTime_Type=TimeTicks
_NbsStackVcdPortTestTime_Object=MibTableColumn
nbsStackVcdPortTestTime=_NbsStackVcdPortTestTime_Object((1,3,6,1,4,1,629,1,50,4,12,2,1,12),_NbsStackVcdPortTestTime_Type())
nbsStackVcdPortTestTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsStackVcdPortTestTime.setStatus('current')
specSlotLinkChanged=NotificationType((1,3,6,1,4,1,629,1,50,4,0,22))
specSlotLinkChanged.setObjects((_E,_N))
if mibBuilder.loadTexts:specSlotLinkChanged.setStatus('')
mibBuilder.exportSymbols(_E,**{'PortsBitmap':PortsBitmap,'nbase':nbase,'nbSwitchG1':nbSwitchG1,'nbSwitchG1Il':nbSwitchG1Il,'nbsStackInfo':nbsStackInfo,'specSlotLinkChanged':specSlotLinkChanged,'nbsStackSlotCapacity':nbsStackSlotCapacity,'nbsStackSlotsTableSize':nbsStackSlotsTableSize,'nbsStackPortsCapacity':nbsStackPortsCapacity,'nbsStackSlotPortsCapacity':nbsStackSlotPortsCapacity,'nbsStackSlotTable':nbsStackSlotTable,'nbsStackSlotEntry':nbsStackSlotEntry,_O:nbsStackSlotIndex,'nbsStackSlotType':nbsStackSlotType,'nbsStackSlotMgmtStatus':nbsStackSlotMgmtStatus,'nbsStackSlotPortsMaxNumber':nbsStackSlotPortsMaxNumber,'nbsStackSlotPortsNumber':nbsStackSlotPortsNumber,'nbsStackSlotFirstPort':nbsStackSlotFirstPort,'nbsStackSlotOperStatus':nbsStackSlotOperStatus,'nbsStackSlotAdminStatus':nbsStackSlotAdminStatus,'nbsStackSlotRedundantPSMode':nbsStackSlotRedundantPSMode,'nbsStackSlotUplinkModulesNumber':nbsStackSlotUplinkModulesNumber,'nbsStackSlotReset':nbsStackSlotReset,'nbsStackSlotIp':nbsStackSlotIp,'nbsStackSlotHwVers':nbsStackSlotHwVers,'nbsStackSlotSwVers':nbsStackSlotSwVers,'nbsStackSlotUplTable':nbsStackSlotUplTable,'nbsStackSlotUplEntry':nbsStackSlotUplEntry,_S:nbsStackSlotNumber,_T:nbsStackSlotUplNumber,'nbsStackSlotUplType':nbsStackSlotUplType,'nbsStackSlotUplSwVers':nbsStackSlotUplSwVers,'nbsStackSlotUplHwVers':nbsStackSlotUplHwVers,'nbsStackSlotUplNPorts':nbsStackSlotUplNPorts,'nbsStackSlotUplFirstPort':nbsStackSlotUplFirstPort,'nbsStackSlotUplPortsMask':nbsStackSlotUplPortsMask,'nbsStackSlotUplStatus':nbsStackSlotUplStatus,'nbsStackSlotUplHwDescr':nbsStackSlotUplHwDescr,'nbsStackSlotUplSwDescr':nbsStackSlotUplSwDescr,'nbsStackSpecSlotTable':nbsStackSpecSlotTable,'nbsStackSpecSlotEntry':nbsStackSpecSlotEntry,_N:nbsStackSlotSpecNumber,_U:nbsStackSlotSpecUplNumber,'nbsStackSlotSpecUplRedundantMode':nbsStackSlotSpecUplRedundantMode,'nbsStackSlotSpecUplLeftLinkLed':nbsStackSlotSpecUplLeftLinkLed,'nbsStackSlotSpecUplLeftActivityLed':nbsStackSlotSpecUplLeftActivityLed,'nbsStackSlotSpecUplRightLinkLed':nbsStackSlotSpecUplRightLinkLed,'nbsStackSlotSpecUplRightActivityLed':nbsStackSlotSpecUplRightActivityLed,'nbsStackSlotSpecUplTestSemiAutoMode':nbsStackSlotSpecUplTestSemiAutoMode,'nbsStackMultiConPortGroup':nbsStackMultiConPortGroup,'nbsStackMultiConPortTable':nbsStackMultiConPortTable,'nbsStackMultiConPortEntry':nbsStackMultiConPortEntry,_V:nbsStackMultiConPortId,'nbsStackMultiConPortConnectorsNumber':nbsStackMultiConPortConnectorsNumber,'nbsStackMultiConPortForceMode':nbsStackMultiConPortForceMode,'nbsStackMultiConPortForcedConnector':nbsStackMultiConPortForcedConnector,'nbsStackMultiConPortConnectorTable':nbsStackMultiConPortConnectorTable,'nbsStackMultiConPortConnectorEntry':nbsStackMultiConPortConnectorEntry,_W:nbsStackMultiConPortNumber,_X:nbsStackMultiConPortConnectorNumber,'nbsStackMultiConPortConnectorType':nbsStackMultiConPortConnectorType,'nbsStackMultiConPortConnectorSubType':nbsStackMultiConPortConnectorSubType,'nbsStackMultiConPortConnectorLinkStatus':nbsStackMultiConPortConnectorLinkStatus,'nbsStackMultiConPortConnectorRxLoss':nbsStackMultiConPortConnectorRxLoss,'nbsStackMultiConPortConnectorTxFault':nbsStackMultiConPortConnectorTxFault,'nbsStackVcdGroup':nbsStackVcdGroup,'nbsStackVcdGenSupport':nbsStackVcdGenSupport,'nbsStackVcdPortTable':nbsStackVcdPortTable,'nbsStackVcdPortEntry':nbsStackVcdPortEntry,_a:nbsStackVcdPortId,'nbsStackVcdPortTestRun':nbsStackVcdPortTestRun,'nbsStackVcdPortPair12Distance':nbsStackVcdPortPair12Distance,'nbsStackVcdPortPair12TestStatus':nbsStackVcdPortPair12TestStatus,'nbsStackVcdPortPair36Distance':nbsStackVcdPortPair36Distance,'nbsStackVcdPortPair36TestStatus':nbsStackVcdPortPair36TestStatus,'nbsStackVcdPortPair45Distance':nbsStackVcdPortPair45Distance,'nbsStackVcdPortPair45TestStatus':nbsStackVcdPortPair45TestStatus,'nbsStackVcdPortPair78Distance':nbsStackVcdPortPair78Distance,'nbsStackVcdPortPair78TestStatus':nbsStackVcdPortPair78TestStatus,'nbsStackVcdPortSupport':nbsStackVcdPortSupport,'nbsStackVcdPortTestTime':nbsStackVcdPortTestTime})