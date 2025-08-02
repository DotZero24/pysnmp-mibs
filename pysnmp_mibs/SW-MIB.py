_Ai='swNsNodeName'
_Ah='swEndDevicePortID'
_Ag='swDeviceStatus'
_Af='swFCPortSpecifier'
_Ae='swBrcdBitObjVal'
_Ad='swBrcdTrapBitMask'
_Ac='swPortList'
_Ab='swOperStatus'
_Aa='swDomainID'
_AZ='swPmgrEventDescr'
_AY='swPmgrEventTime'
_AX='swPmgrEventType'
_AW='swIPv6Status'
_AV='swIPv6Address'
_AU='swTrackChangesInfo'
_AT='swFwLastSeverityLevel'
_AS='swFwLastState'
_AR='swFwLastEvent'
_AQ='swFwLastEventTime'
_AP='swFwLastEventVal'
_AO='swFwLabel'
_AN='swEventDescr'
_AM='swEventRepeatCount'
_AL='swEventLevel'
_AK='swEventTimeInfo'
_AJ='swFCPortDisableReason'
_AI='swFCPortBrcdType'
_AH='swFCPortPrevType'
_AG='swFCPortWwn'
_AF='swFCPortOpStatus'
_AE='swSensorInfo'
_AD='swSensorValue'
_AC='swSensorType'
_AB='swSensorStatus'
_AA='swDiagResult'
_A9='swConnUnitPortStatEntry'
_A8='raslogandSnmp'
_A7='swTopTalkerMntIndex'
_A6='swTrunkGrpNumber'
_A5='swTrunkPortIndex'
_A4='swBlmPerfFltRefkey'
_A3='swBlmPerfFltPort'
_A2='swBlmPerfEERefKey'
_A1='swBlmPerfEEPort'
_A0='swBlmPerfAlpaIndx'
_z='swBlmPerfAlpaPort'
_y='swGroupMemWwn'
_x='swGroupId'
_w='swGroupIndex'
_v='swEndDeviceAlpa'
_u='swEndDevicePort'
_t='swNsEntryIndex'
_s='swAgtCmtyIdx'
_r='swFabricMemWwn'
_q='swNbIndex'
_p='d-port'
_o='ex-port'
_n='g-port'
_m='e-port'
_l='f-port'
_k='fl-port'
_j='swFwCorrupted'
_i='swCurrent'
_h='2014-10-04 13:10'
_g='swFCPortFlag'
_f='swFCPortName'
_e='swFwThresholdIndex'
_d='swEventIndex'
_c='swSensorIndex'
_b='debug'
_a='informational'
_Z='warning'
_Y='error'
_X='critical'
_W='swFwClassAreaIndex'
_V='swFCPortIndex'
_U='testing'
_T='offline'
_S='online'
_R='none'
_Q='other'
_P='faulty'
_O='enabled'
_N='disabled'
_M='deprecated'
_L='swSsn'
_K='swVfId'
_J='unknown'
_I='not-accessible'
_H='DisplayString'
_G='read-write'
_F='OctetString'
_E='Integer32'
_D='SW-MIB'
_C='obsolete'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
bcsiModules,fcSwitch=mibBuilder.importSymbols('Brocade-REG-MIB','bcsiModules','fcSwitch')
FcWwn,SwDomainIndex,SwNbIndex,SwPortIndex,SwSensorIndex,SwTrunkMaster=mibBuilder.importSymbols('Brocade-TC','FcWwn','SwDomainIndex','SwNbIndex','SwPortIndex','SwSensorIndex','SwTrunkMaster')
connUnitPortEntry,connUnitPortStatEntry=mibBuilder.importSymbols('FCMGMT-MIB','connUnitPortEntry','connUnitPortStatEntry')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_H,'PhysAddress','TextualConvention','TruthValue')
swMibModule=ModuleIdentity((1,3,6,1,4,1,1588,3,1,3))
if mibBuilder.loadTexts:swMibModule.setRevisions(('2003-01-13 14:30','2003-07-20 14:30','2004-04-15 10:30','2004-08-06 18:30','2005-04-29 20:16','2006-01-09 09:00','2006-05-17 09:00','2007-01-23 09:00','2007-06-08 12:00','2007-06-27 10:30','2007-08-01 12:20','2007-08-29 04:42','2008-01-29 07:59','2008-07-17 03:45','2008-07-24 02:32','2008-07-25 02:32','2008-09-09 09:00','2009-09-28 09:00','2009-02-21 09:00','2009-03-30 09:00','2009-06-25 12:00','2009-06-29 01:00','2009-06-30 13:06','2009-06-30 06:00','2009-10-30 05:00','2009-11-03 13:06','2009-11-05 12:00','2009-11-05 05:00','2009-11-06 11:30','2009-11-30 10:30','2009-12-03 17:30','2010-01-30 17:30','2010-07-08 11:30','2010-07-15 11:30','2010-07-21 11:30','2010-08-06 11:30','2010-08-20 10:30','2010-10-07 10:30','2010-10-09 10:30','2010-10-25 10:30','2010-11-01 06:00','2010-11-02 10:30','2010-12-02 10:30','2010-12-08 10:30','2010-12-20 10:00','2010-12-21 04:00','2010-12-22 10:00','2010-12-30 10:00','2011-01-06 10:30','2011-01-07 10:30','2011-02-18 06:00','2012-02-23 10:30','2012-03-05 03:33','2012-05-15 14:25','2012-06-04 17:20','2012-06-14 10:00','2012-06-29 15:20','2012-07-10 16:00','2012-09-26 14:00','2013-03-21 13:00','2013-04-04 17:48','2013-04-22 11:30','2013-04-25 18:03','2013-05-15 14:30','2013-06-05 16:00','2013-06-29 10:00','2013-09-12 10:00','2013-10-04 13:40','2014-01-16 16:37','2014-03-04 12:30','2014-03-31 17:30','2014-04-15 12:20','2014-05-09 11:13','2014-07-01 12:03','2014-08-21 14:47','2014-09-05 11:12',_h,_h,'2014-12-09 17:00'))
class SwFwActs(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63)));namedValues=NamedValues(*(('swFwNoAction',0),('swFwErrlog',1),('swFwSnmptrap',2),('swFwErrlogSnmptrap',3),('swFwPortloglock',4),('swFwErrlogPortloglock',5),('swFwSnmptrapPortloglock',6),('swFwErrlogSnmptrapPortloglock',7),('swFwRn',8),('swFwElRn',9),('swFwStRn',10),('swFwElStRn',11),('swFwPlRn',12),('swFwElPlRn',13),('swFwStPlRn',14),('swFwElStPlRn',15),('swFwMailAlert',16),('swFwMailAlertErrlog',17),('swFwMailAlertSnmptrap',18),('swFwMailAlertErrlogSnmptrap',19),('swFwMailAlertPortloglock',20),('swFwMailAlertErrlogPortloglock',21),('swFwMailAlertSnmptrapPortloglock',22),('swFwMailAlertErrlogSnmptrapPortloglock',23),('swFwMailAlertRn',24),('swFwElMailAlertRn',25),('swFwMailAlertStRn',26),('swFwMailAlertElStRn',27),('swFwMailAlertPlRn',28),('swFwMailAlertElPlRn',29),('swFwMailAlertStPlRn',30),('swFwMailAlertElStPlRn',31),('swFwPf',32),('swFwElPf',33),('swFwStPf',34),('swFwElStPf',35),('swFwPlPf',36),('swFwElPlPf',37),('swFwStPlPf',38),('swFwElStPlPf',39),('swFwRnPf',40),('swFwElRnPf',41),('swFwStRnPf',42),('swFwElStRnPf',43),('swFwPlRnPf',44),('swFwElPlRnPf',45),('swFwStPlRnPf',46),('swFwElStPlRnPf',47),('swFwMailAlertPf',48),('swFwMailAlertElPf',49),('swFwMailAlertStPf',50),('swFwMailAlertElStPf',51),('swFwMailAlertPlPf',52),('swFwMailAlertElPlPf',53),('swFwMailAlertStPlPf',54),('swFwMailAlertElStPlPf',55),('swFwMailAlertRnPf',56),('swFwMailAlertElRnPf',57),('swFwMailAlertStRnPf',58),('swFwMailAlertElStRnPf',59),('swFwMailAlertPlRnPf',60),('swFwMailAlertElPlRnPf',61),('swFwMailAlertStPlRnPf',62),('swFwMailAlertElStPlRnPf',63)))
class SwFwLevels(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('swFwReserved',1),('swFwDefault',2),('swFwCustom',3)))
class SwFwClassesAreas(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152)));namedValues=NamedValues(*(('swFwEnvTemp',1),('swFwEnvFan',2),('swFwEnvPs',3),('swFwTransceiverTemp',4),('swFwTransceiverRxp',5),('swFwTransceiverTxp',6),('swFwTransceiverCurrent',7),('swFwPortLink',8),('swFwPortSync',9),('swFwPortSignal',10),('swFwPortPe',11),('swFwPortWords',12),('swFwPortCrcs',13),('swFwPortRXPerf',14),('swFwPortTXPerf',15),('swFwPortState',16),('swFwFabricEd',17),('swFwFabricFr',18),('swFwFabricDi',19),('swFwFabricSc',20),('swFwFabricZc',21),('swFwFabricFq',22),('swFwFabricFl',23),('swFwFabricGs',24),('swFwEPortLink',25),('swFwEPortSync',26),('swFwEPortSignal',27),('swFwEPortPe',28),('swFwEPortWords',29),('swFwEPortCrcs',30),('swFwEPortRXPerf',31),('swFwEPortTXPerf',32),('swFwEPortState',33),('swFwFCUPortLink',34),('swFwFCUPortSync',35),('swFwFCUPortSignal',36),('swFwFCUPortPe',37),('swFwFCUPortWords',38),('swFwFCUPortCrcs',39),('swFwFCUPortRXPerf',40),('swFwFCUPortTXPerf',41),('swFwFCUPortState',42),('swFwFOPPortLink',43),('swFwFOPPortSync',44),('swFwFOPPortSignal',45),('swFwFOPPortPe',46),('swFwFOPPortWords',47),('swFwFOPPortCrcs',48),('swFwFOPPortRXPerf',49),('swFwFOPPortTXPerf',50),('swFwFOPPortState',51),('swFwPerfALPACRC',52),('swFwPerfEToECRC',53),('swFwPerfEToERxCnt',54),('swFwPerfEToETxCnt',55),('swFwPerffltCusDef',56),('swFwTransceiverVoltage',57),('swFwSecTelnetViolations',58),('swFwSecHTTPViolations',59),('swFwSecAPIViolations',60),('swFwSecRSNMPViolations',61),('swFwSecWSNMPViolations',62),('swFwSecSESViolations',63),('swFwSecMSViolations',64),('swFwSecSerialViolations',65),('swFwSecFPViolations',66),('swFwSecSCCViolations',67),('swFwSecDCCViolations',68),('swFwSecLoginViolations',69),('swFwSecInvalidTS',70),('swFwSecInvalidSign',71),('swFwSecInvalidCert',72),('swFwSecSlapFail',73),('swFwSecSlapBadPkt',74),('swFwSecTSOutSync',75),('swFwSecNoFcs',76),('swFwSecIncompDB',77),('swFwSecIllegalCmd',78),('swFwSAMTotalDownTime',79),('swFwSAMTotalUpTime',80),('swFwSAMDurationOfOccur',81),('swFwSAMFreqOfOccur',82),('swFwResourceFlash',83),('swFwEPortUtil',84),('swFwEPortPktl',85),('swFwPortLr',86),('swFwEPortLr',87),('swFwFCUPortLr',88),('swFwFOPPortLr',89),('swFwPortC3Discard',90),('swFwEPortC3Discard',91),('swFwFCUPortC3Discard',92),('swFwFOPPortC3Discard',93),('swFwVEPortStateChange',94),('swFwVEPortUtil',95),('swFwVEPortPktLoss',96),('swFwEPortTrunkUtil',97),('swFwFCUPortTrunkUtil',98),('swFwFOPPortTrunkUtil',99),('swFwCPUMemUsage',100),('filterFmCfg1',101),('filterFmCfg2',102),('filterFmCfg3',103),('filterFmCfg4',104),('filterFmCfg5',105),('filterFmCfg6',106),('filterFmCfg7',107),('filterFmCfg8',108),('filterFmCfg9',109),('filterFmCfg10',110),('filterFmCfg11',111),('filterFmCfg12',112),('filterFmCfg13',113),('filterFmCfg14',114),('filterFmCfg15',115),('filterFmCfg16',116),('filterFmCfg17',117),('filterFmCfg18',118),('filterFmCfg19',119),('filterFmCfg20',120),('filterFmCfg21',121),('filterFmCfg22',122),('filterFmCfg23',123),('filterFmCfg24',124),('filterFmCfg25',125),('filterFmCfg26',126),('filterFmCfg27',127),('filterFmCfg28',128),('filterFmCfg29',129),('filterFmCfg30',130),('filterFmCfg31',131),('filterFmCfg32',132),('filterFmCfg33',133),('filterFmCfg34',134),('filterFmCfg35',135),('filterFmCfg36',136),('filterFmCfg37',137),('filterFmCfg38',138),('filterFmCfg39',139),('filterFmCfg40',140),('filterFmCfg41',141),('filterFmCfg42',142),('filterFmCfg43',143),('filterFmCfg44',144),('filterFmCfg45',145),('filterFmCfg46',146),('filterFmCfg47',147),('filterFmCfg48',148),('filterFmCfg49',149),('filterFmCfg50',150),('filterFmCfg51',151),('swFwPowerOnHours',152)))
class SwFwWriteVals(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('swFwCancelWrite',1),('swFwApplyWrite',2)))
class SwFwTimebase(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('swFwTbNone',1),('swFwTbSec',2),('swFwTbMin',3),('swFwTbHour',4),('swFwTbDay',5)))
class SwFwStatus(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_O,2)))
class SwFwEvent(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('started',1),('changed',2),('exceeded',3),('below',4),('above',5),('inBetween',6),('lowBufferCrsd',7)))
class SwFwBehavior(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('triggered',1),('continuous',2)))
class SwFwState(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('swFwInformative',1),('swFwNormal',2),('swFwFaulty',3)))
class SwFwLicense(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('swFwLicensed',1),('swFwNotLicensed',2)))
class SwSevType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_R,0),(_X,1),(_Y,2),(_Z,3),(_a,4),(_b,5)))
class FcPortFlag(TextualConvention,Bits):status=_A;namedValues=NamedValues(*(('physical',0),('virtual',1)))
_Sw_ObjectIdentity=ObjectIdentity
sw=_Sw_ObjectIdentity((1,3,6,1,4,1,1588,2,1,1,1))
if mibBuilder.loadTexts:sw.setStatus(_A)
_SwTrapsV2_ObjectIdentity=ObjectIdentity
swTrapsV2=_SwTrapsV2_ObjectIdentity((1,3,6,1,4,1,1588,2,1,1,1,0))
if mibBuilder.loadTexts:swTrapsV2.setStatus(_A)
_SwSystem_ObjectIdentity=ObjectIdentity
swSystem=_SwSystem_ObjectIdentity((1,3,6,1,4,1,1588,2,1,1,1,1))
if mibBuilder.loadTexts:swSystem.setStatus(_A)
class _SwCurrentDate_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_SwCurrentDate_Type.__name__=_H
_SwCurrentDate_Object=MibScalar
swCurrentDate=_SwCurrentDate_Object((1,3,6,1,4,1,1588,2,1,1,1,1,1),_SwCurrentDate_Type())
swCurrentDate.setMaxAccess(_B)
if mibBuilder.loadTexts:swCurrentDate.setStatus(_A)
class _SwBootDate_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_SwBootDate_Type.__name__=_H
_SwBootDate_Object=MibScalar
swBootDate=_SwBootDate_Object((1,3,6,1,4,1,1588,2,1,1,1,1,2),_SwBootDate_Type())
swBootDate.setMaxAccess(_B)
if mibBuilder.loadTexts:swBootDate.setStatus(_A)
class _SwFWLastUpdated_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_SwFWLastUpdated_Type.__name__=_H
_SwFWLastUpdated_Object=MibScalar
swFWLastUpdated=_SwFWLastUpdated_Object((1,3,6,1,4,1,1588,2,1,1,1,1,3),_SwFWLastUpdated_Type())
swFWLastUpdated.setMaxAccess(_B)
if mibBuilder.loadTexts:swFWLastUpdated.setStatus(_C)
class _SwFlashLastUpdated_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_SwFlashLastUpdated_Type.__name__=_H
_SwFlashLastUpdated_Object=MibScalar
swFlashLastUpdated=_SwFlashLastUpdated_Object((1,3,6,1,4,1,1588,2,1,1,1,1,4),_SwFlashLastUpdated_Type())
swFlashLastUpdated.setMaxAccess(_B)
if mibBuilder.loadTexts:swFlashLastUpdated.setStatus(_A)
class _SwBootPromLastUpdated_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_SwBootPromLastUpdated_Type.__name__=_H
_SwBootPromLastUpdated_Object=MibScalar
swBootPromLastUpdated=_SwBootPromLastUpdated_Object((1,3,6,1,4,1,1588,2,1,1,1,1,5),_SwBootPromLastUpdated_Type())
swBootPromLastUpdated.setMaxAccess(_B)
if mibBuilder.loadTexts:swBootPromLastUpdated.setStatus(_A)
class _SwFirmwareVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,24))
_SwFirmwareVersion_Type.__name__=_H
_SwFirmwareVersion_Object=MibScalar
swFirmwareVersion=_SwFirmwareVersion_Object((1,3,6,1,4,1,1588,2,1,1,1,1,6),_SwFirmwareVersion_Type())
swFirmwareVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:swFirmwareVersion.setStatus(_A)
class _SwOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_S,1),(_T,2),(_U,3),(_P,4)))
_SwOperStatus_Type.__name__=_E
_SwOperStatus_Object=MibScalar
swOperStatus=_SwOperStatus_Object((1,3,6,1,4,1,1588,2,1,1,1,1,7),_SwOperStatus_Type())
swOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:swOperStatus.setStatus(_A)
class _SwAdmStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_S,1),(_T,2),(_U,3),(_P,4),('reboot',5),('fastboot',6)))
_SwAdmStatus_Type.__name__=_E
_SwAdmStatus_Object=MibScalar
swAdmStatus=_SwAdmStatus_Object((1,3,6,1,4,1,1588,2,1,1,1,1,8),_SwAdmStatus_Type())
swAdmStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:swAdmStatus.setStatus(_A)
class _SwTelnetShellAdmStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_J,0),('terminated',1)))
_SwTelnetShellAdmStatus_Type.__name__=_E
_SwTelnetShellAdmStatus_Object=MibScalar
swTelnetShellAdmStatus=_SwTelnetShellAdmStatus_Object((1,3,6,1,4,1,1588,2,1,1,1,1,9),_SwTelnetShellAdmStatus_Type())
swTelnetShellAdmStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:swTelnetShellAdmStatus.setStatus(_M)
class _SwSsn_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_SwSsn_Type.__name__=_H
_SwSsn_Object=MibScalar
swSsn=_SwSsn_Object((1,3,6,1,4,1,1588,2,1,1,1,1,10),_SwSsn_Type())
swSsn.setMaxAccess(_B)
if mibBuilder.loadTexts:swSsn.setStatus(_A)
class _SwFlashDLOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_J,0),(_i,1),('swFwUpgraded',2),('swCfUploaded',3),('swCfDownloaded',4),(_j,5)))
_SwFlashDLOperStatus_Type.__name__=_E
_SwFlashDLOperStatus_Object=MibScalar
swFlashDLOperStatus=_SwFlashDLOperStatus_Object((1,3,6,1,4,1,1588,2,1,1,1,1,11),_SwFlashDLOperStatus_Type())
swFlashDLOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:swFlashDLOperStatus.setStatus(_A)
class _SwFlashDLAdmStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_i,1),('swFwUpgrade',2),('swCfUpload',3),('swCfDownload',4),(_j,5)))
_SwFlashDLAdmStatus_Type.__name__=_E
_SwFlashDLAdmStatus_Object=MibScalar
swFlashDLAdmStatus=_SwFlashDLAdmStatus_Object((1,3,6,1,4,1,1588,2,1,1,1,1,12),_SwFlashDLAdmStatus_Type())
swFlashDLAdmStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:swFlashDLAdmStatus.setStatus(_A)
class _SwFlashDLHost_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_SwFlashDLHost_Type.__name__=_H
_SwFlashDLHost_Object=MibScalar
swFlashDLHost=_SwFlashDLHost_Object((1,3,6,1,4,1,1588,2,1,1,1,1,13),_SwFlashDLHost_Type())
swFlashDLHost.setMaxAccess(_G)
if mibBuilder.loadTexts:swFlashDLHost.setStatus(_A)
class _SwFlashDLUser_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_SwFlashDLUser_Type.__name__=_H
_SwFlashDLUser_Object=MibScalar
swFlashDLUser=_SwFlashDLUser_Object((1,3,6,1,4,1,1588,2,1,1,1,1,14),_SwFlashDLUser_Type())
swFlashDLUser.setMaxAccess(_G)
if mibBuilder.loadTexts:swFlashDLUser.setStatus(_A)
_SwFlashDLFile_Type=DisplayString
_SwFlashDLFile_Object=MibScalar
swFlashDLFile=_SwFlashDLFile_Object((1,3,6,1,4,1,1588,2,1,1,1,1,15),_SwFlashDLFile_Type())
swFlashDLFile.setMaxAccess(_G)
if mibBuilder.loadTexts:swFlashDLFile.setStatus(_A)
class _SwFlashDLPassword_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,100))
_SwFlashDLPassword_Type.__name__=_H
_SwFlashDLPassword_Object=MibScalar
swFlashDLPassword=_SwFlashDLPassword_Object((1,3,6,1,4,1,1588,2,1,1,1,1,16),_SwFlashDLPassword_Type())
swFlashDLPassword.setMaxAccess(_G)
if mibBuilder.loadTexts:swFlashDLPassword.setStatus(_A)
class _SwBeaconOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),('off',2)))
_SwBeaconOperStatus_Type.__name__=_E
_SwBeaconOperStatus_Object=MibScalar
swBeaconOperStatus=_SwBeaconOperStatus_Object((1,3,6,1,4,1,1588,2,1,1,1,1,18),_SwBeaconOperStatus_Type())
swBeaconOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:swBeaconOperStatus.setStatus(_A)
class _SwBeaconAdmStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),('off',2)))
_SwBeaconAdmStatus_Type.__name__=_E
_SwBeaconAdmStatus_Object=MibScalar
swBeaconAdmStatus=_SwBeaconAdmStatus_Object((1,3,6,1,4,1,1588,2,1,1,1,1,19),_SwBeaconAdmStatus_Type())
swBeaconAdmStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:swBeaconAdmStatus.setStatus(_A)
class _SwDiagResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('sw-ok',1),('sw-faulty',2),('sw-embedded-port-fault',3)))
_SwDiagResult_Type.__name__=_E
_SwDiagResult_Object=MibScalar
swDiagResult=_SwDiagResult_Object((1,3,6,1,4,1,1588,2,1,1,1,1,20),_SwDiagResult_Type())
swDiagResult.setMaxAccess(_B)
if mibBuilder.loadTexts:swDiagResult.setStatus(_A)
class _SwNumSensors_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_SwNumSensors_Type.__name__=_E
_SwNumSensors_Object=MibScalar
swNumSensors=_SwNumSensors_Object((1,3,6,1,4,1,1588,2,1,1,1,1,21),_SwNumSensors_Type())
swNumSensors.setMaxAccess(_B)
if mibBuilder.loadTexts:swNumSensors.setStatus(_A)
_SwSensorTable_Object=MibTable
swSensorTable=_SwSensorTable_Object((1,3,6,1,4,1,1588,2,1,1,1,1,22))
if mibBuilder.loadTexts:swSensorTable.setStatus(_A)
_SwSensorEntry_Object=MibTableRow
swSensorEntry=_SwSensorEntry_Object((1,3,6,1,4,1,1588,2,1,1,1,1,22,1))
swSensorEntry.setIndexNames((0,_D,_c))
if mibBuilder.loadTexts:swSensorEntry.setStatus(_A)
_SwSensorIndex_Type=SwSensorIndex
_SwSensorIndex_Object=MibTableColumn
swSensorIndex=_SwSensorIndex_Object((1,3,6,1,4,1,1588,2,1,1,1,1,22,1,1),_SwSensorIndex_Type())
swSensorIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:swSensorIndex.setStatus(_A)
class _SwSensorType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('temperature',1),('fan',2),('power-supply',3)))
_SwSensorType_Type.__name__=_E
_SwSensorType_Object=MibTableColumn
swSensorType=_SwSensorType_Object((1,3,6,1,4,1,1588,2,1,1,1,1,22,1,2),_SwSensorType_Type())
swSensorType.setMaxAccess(_B)
if mibBuilder.loadTexts:swSensorType.setStatus(_A)
class _SwSensorStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_J,1),(_P,2),('below-min',3),('nominal',4),('above-max',5),('absent',6)))
_SwSensorStatus_Type.__name__=_E
_SwSensorStatus_Object=MibTableColumn
swSensorStatus=_SwSensorStatus_Object((1,3,6,1,4,1,1588,2,1,1,1,1,22,1,3),_SwSensorStatus_Type())
swSensorStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:swSensorStatus.setStatus(_A)
_SwSensorValue_Type=Integer32
_SwSensorValue_Object=MibTableColumn
swSensorValue=_SwSensorValue_Object((1,3,6,1,4,1,1588,2,1,1,1,1,22,1,4),_SwSensorValue_Type())
swSensorValue.setMaxAccess(_B)
if mibBuilder.loadTexts:swSensorValue.setStatus(_A)
class _SwSensorInfo_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SwSensorInfo_Type.__name__=_H
_SwSensorInfo_Object=MibTableColumn
swSensorInfo=_SwSensorInfo_Object((1,3,6,1,4,1,1588,2,1,1,1,1,22,1,5),_SwSensorInfo_Type())
swSensorInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:swSensorInfo.setStatus(_A)
_SwTrackChangesInfo_Type=DisplayString
_SwTrackChangesInfo_Object=MibScalar
swTrackChangesInfo=_SwTrackChangesInfo_Object((1,3,6,1,4,1,1588,2,1,1,1,1,23),_SwTrackChangesInfo_Type())
swTrackChangesInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:swTrackChangesInfo.setStatus(_C)
_SwID_Type=Integer32
_SwID_Object=MibScalar
swID=_SwID_Object((1,3,6,1,4,1,1588,2,1,1,1,1,24),_SwID_Type())
swID.setMaxAccess(_B)
if mibBuilder.loadTexts:swID.setStatus(_A)
_SwEtherIPAddress_Type=IpAddress
_SwEtherIPAddress_Object=MibScalar
swEtherIPAddress=_SwEtherIPAddress_Object((1,3,6,1,4,1,1588,2,1,1,1,1,25),_SwEtherIPAddress_Type())
swEtherIPAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:swEtherIPAddress.setStatus(_A)
_SwEtherIPMask_Type=IpAddress
_SwEtherIPMask_Object=MibScalar
swEtherIPMask=_SwEtherIPMask_Object((1,3,6,1,4,1,1588,2,1,1,1,1,26),_SwEtherIPMask_Type())
swEtherIPMask.setMaxAccess(_B)
if mibBuilder.loadTexts:swEtherIPMask.setStatus(_A)
_SwFCIPAddress_Type=IpAddress
_SwFCIPAddress_Object=MibScalar
swFCIPAddress=_SwFCIPAddress_Object((1,3,6,1,4,1,1588,2,1,1,1,1,27),_SwFCIPAddress_Type())
swFCIPAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:swFCIPAddress.setStatus(_A)
_SwFCIPMask_Type=IpAddress
_SwFCIPMask_Object=MibScalar
swFCIPMask=_SwFCIPMask_Object((1,3,6,1,4,1,1588,2,1,1,1,1,28),_SwFCIPMask_Type())
swFCIPMask.setMaxAccess(_B)
if mibBuilder.loadTexts:swFCIPMask.setStatus(_A)
_SwIPv6Address_Type=DisplayString
_SwIPv6Address_Object=MibScalar
swIPv6Address=_SwIPv6Address_Object((1,3,6,1,4,1,1588,2,1,1,1,1,29),_SwIPv6Address_Type())
swIPv6Address.setMaxAccess(_I)
if mibBuilder.loadTexts:swIPv6Address.setStatus(_A)
class _SwIPv6Status_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('tentative',1),('preferred',2),('ipdeprecated',3),('inactive',4)))
_SwIPv6Status_Type.__name__=_E
_SwIPv6Status_Object=MibScalar
swIPv6Status=_SwIPv6Status_Object((1,3,6,1,4,1,1588,2,1,1,1,1,30),_SwIPv6Status_Type())
swIPv6Status.setMaxAccess(_I)
if mibBuilder.loadTexts:swIPv6Status.setStatus(_A)
class _SwModel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('switch7500',1),('switch7500E',2),(_Q,3)))
_SwModel_Type.__name__=_E
_SwModel_Object=MibScalar
swModel=_SwModel_Object((1,3,6,1,4,1,1588,2,1,1,1,1,31),_SwModel_Type())
swModel.setMaxAccess(_B)
if mibBuilder.loadTexts:swModel.setStatus(_A)
class _SwTestString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_SwTestString_Type.__name__=_H
_SwTestString_Object=MibScalar
swTestString=_SwTestString_Object((1,3,6,1,4,1,1588,2,1,1,1,1,32),_SwTestString_Type())
swTestString.setMaxAccess(_I)
if mibBuilder.loadTexts:swTestString.setStatus(_A)
_SwPortList_Type=OctetString
_SwPortList_Object=MibScalar
swPortList=_SwPortList_Object((1,3,6,1,4,1,1588,2,1,1,1,1,33),_SwPortList_Type())
swPortList.setMaxAccess(_I)
if mibBuilder.loadTexts:swPortList.setStatus(_A)
_SwBrcdTrapBitMask_Type=Integer32
_SwBrcdTrapBitMask_Object=MibScalar
swBrcdTrapBitMask=_SwBrcdTrapBitMask_Object((1,3,6,1,4,1,1588,2,1,1,1,1,34),_SwBrcdTrapBitMask_Type())
swBrcdTrapBitMask.setMaxAccess(_I)
if mibBuilder.loadTexts:swBrcdTrapBitMask.setStatus(_A)
class _SwFCPortPrevType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_J,1),(_Q,2),(_k,3),(_l,4),(_m,5),(_n,6),(_o,7),(_p,8)))
_SwFCPortPrevType_Type.__name__=_E
_SwFCPortPrevType_Object=MibScalar
swFCPortPrevType=_SwFCPortPrevType_Object((1,3,6,1,4,1,1588,2,1,1,1,1,35),_SwFCPortPrevType_Type())
swFCPortPrevType.setMaxAccess(_I)
if mibBuilder.loadTexts:swFCPortPrevType.setStatus(_A)
class _SwDeviceStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('login',1),('logout',2),(_J,3)))
_SwDeviceStatus_Type.__name__=_E
_SwDeviceStatus_Object=MibScalar
swDeviceStatus=_SwDeviceStatus_Object((1,3,6,1,4,1,1588,2,1,1,1,1,36),_SwDeviceStatus_Type())
swDeviceStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:swDeviceStatus.setStatus(_A)
_SwBrcdBitObjVal_Type=Integer32
_SwBrcdBitObjVal_Object=MibScalar
swBrcdBitObjVal=_SwBrcdBitObjVal_Object((1,3,6,1,4,1,1588,2,1,1,1,1,37),_SwBrcdBitObjVal_Type())
swBrcdBitObjVal.setMaxAccess(_I)
if mibBuilder.loadTexts:swBrcdBitObjVal.setStatus(_A)
class _SwIODState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_O,1),(_N,2),(_J,3)))
_SwIODState_Type.__name__=_E
_SwIODState_Object=MibScalar
swIODState=_SwIODState_Object((1,3,6,1,4,1,1588,2,1,1,1,1,38),_SwIODState_Type())
swIODState.setMaxAccess(_B)
if mibBuilder.loadTexts:swIODState.setStatus(_A)
_SwFabric_ObjectIdentity=ObjectIdentity
swFabric=_SwFabric_ObjectIdentity((1,3,6,1,4,1,1588,2,1,1,1,2))
if mibBuilder.loadTexts:swFabric.setStatus(_A)
_SwDomainID_Type=SwDomainIndex
_SwDomainID_Object=MibScalar
swDomainID=_SwDomainID_Object((1,3,6,1,4,1,1588,2,1,1,1,2,1),_SwDomainID_Type())
swDomainID.setMaxAccess(_G)
if mibBuilder.loadTexts:swDomainID.setStatus(_A)
class _SwPrincipalSwitch_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('yes',1),('no',2)))
_SwPrincipalSwitch_Type.__name__=_E
_SwPrincipalSwitch_Object=MibScalar
swPrincipalSwitch=_SwPrincipalSwitch_Object((1,3,6,1,4,1,1588,2,1,1,1,2,2),_SwPrincipalSwitch_Type())
swPrincipalSwitch.setMaxAccess(_B)
if mibBuilder.loadTexts:swPrincipalSwitch.setStatus(_A)
class _SwNumNbs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_SwNumNbs_Type.__name__=_E
_SwNumNbs_Object=MibScalar
swNumNbs=_SwNumNbs_Object((1,3,6,1,4,1,1588,2,1,1,1,2,8),_SwNumNbs_Type())
swNumNbs.setMaxAccess(_B)
if mibBuilder.loadTexts:swNumNbs.setStatus(_A)
_SwNbTable_Object=MibTable
swNbTable=_SwNbTable_Object((1,3,6,1,4,1,1588,2,1,1,1,2,9))
if mibBuilder.loadTexts:swNbTable.setStatus(_A)
_SwNbEntry_Object=MibTableRow
swNbEntry=_SwNbEntry_Object((1,3,6,1,4,1,1588,2,1,1,1,2,9,1))
swNbEntry.setIndexNames((0,_D,_q))
if mibBuilder.loadTexts:swNbEntry.setStatus(_A)
_SwNbIndex_Type=SwNbIndex
_SwNbIndex_Object=MibTableColumn
swNbIndex=_SwNbIndex_Object((1,3,6,1,4,1,1588,2,1,1,1,2,9,1,1),_SwNbIndex_Type())
swNbIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:swNbIndex.setStatus(_A)
_SwNbMyPort_Type=SwPortIndex
_SwNbMyPort_Object=MibTableColumn
swNbMyPort=_SwNbMyPort_Object((1,3,6,1,4,1,1588,2,1,1,1,2,9,1,2),_SwNbMyPort_Type())
swNbMyPort.setMaxAccess(_B)
if mibBuilder.loadTexts:swNbMyPort.setStatus(_A)
_SwNbRemDomain_Type=SwDomainIndex
_SwNbRemDomain_Object=MibTableColumn
swNbRemDomain=_SwNbRemDomain_Object((1,3,6,1,4,1,1588,2,1,1,1,2,9,1,3),_SwNbRemDomain_Type())
swNbRemDomain.setMaxAccess(_B)
if mibBuilder.loadTexts:swNbRemDomain.setStatus(_A)
_SwNbRemPort_Type=SwPortIndex
_SwNbRemPort_Object=MibTableColumn
swNbRemPort=_SwNbRemPort_Object((1,3,6,1,4,1,1588,2,1,1,1,2,9,1,4),_SwNbRemPort_Type())
swNbRemPort.setMaxAccess(_B)
if mibBuilder.loadTexts:swNbRemPort.setStatus(_A)
class _SwNbBaudRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4,8,16,32,64,128,256,512)));namedValues=NamedValues(*((_Q,1),('oneEighth',2),('quarter',4),('half',8),('full',16),('double',32),('quadruple',64),('octuple',128),('decuple',256),('sexdecuple',512)))
_SwNbBaudRate_Type.__name__=_E
_SwNbBaudRate_Object=MibTableColumn
swNbBaudRate=_SwNbBaudRate_Object((1,3,6,1,4,1,1588,2,1,1,1,2,9,1,5),_SwNbBaudRate_Type())
swNbBaudRate.setMaxAccess(_B)
if mibBuilder.loadTexts:swNbBaudRate.setStatus(_A)
class _SwNbIslState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('sw-down',0),('sw-init',1),('sw-internal2',2),('sw-internal3',3),('sw-internal4',4),('sw-active',5)))
_SwNbIslState_Type.__name__=_E
_SwNbIslState_Object=MibTableColumn
swNbIslState=_SwNbIslState_Object((1,3,6,1,4,1,1588,2,1,1,1,2,9,1,6),_SwNbIslState_Type())
swNbIslState.setMaxAccess(_B)
if mibBuilder.loadTexts:swNbIslState.setStatus(_A)
class _SwNbIslCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_SwNbIslCost_Type.__name__=_E
_SwNbIslCost_Object=MibTableColumn
swNbIslCost=_SwNbIslCost_Object((1,3,6,1,4,1,1588,2,1,1,1,2,9,1,7),_SwNbIslCost_Type())
swNbIslCost.setMaxAccess(_G)
if mibBuilder.loadTexts:swNbIslCost.setStatus(_A)
class _SwNbRemPortName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_SwNbRemPortName_Type.__name__=_F
_SwNbRemPortName_Object=MibTableColumn
swNbRemPortName=_SwNbRemPortName_Object((1,3,6,1,4,1,1588,2,1,1,1,2,9,1,8),_SwNbRemPortName_Type())
swNbRemPortName.setMaxAccess(_B)
if mibBuilder.loadTexts:swNbRemPortName.setStatus(_A)
_SwFabricMemTable_Object=MibTable
swFabricMemTable=_SwFabricMemTable_Object((1,3,6,1,4,1,1588,2,1,1,1,2,10))
if mibBuilder.loadTexts:swFabricMemTable.setStatus(_A)
_SwFabricMemEntry_Object=MibTableRow
swFabricMemEntry=_SwFabricMemEntry_Object((1,3,6,1,4,1,1588,2,1,1,1,2,10,1))
swFabricMemEntry.setIndexNames((0,_D,_r))
if mibBuilder.loadTexts:swFabricMemEntry.setStatus(_A)
_SwFabricMemWwn_Type=FcWwn
_SwFabricMemWwn_Object=MibTableColumn
swFabricMemWwn=_SwFabricMemWwn_Object((1,3,6,1,4,1,1588,2,1,1,1,2,10,1,1),_SwFabricMemWwn_Type())
swFabricMemWwn.setMaxAccess(_B)
if mibBuilder.loadTexts:swFabricMemWwn.setStatus(_A)
_SwFabricMemDid_Type=SwDomainIndex
_SwFabricMemDid_Object=MibTableColumn
swFabricMemDid=_SwFabricMemDid_Object((1,3,6,1,4,1,1588,2,1,1,1,2,10,1,2),_SwFabricMemDid_Type())
swFabricMemDid.setMaxAccess(_B)
if mibBuilder.loadTexts:swFabricMemDid.setStatus(_A)
class _SwFabricMemName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SwFabricMemName_Type.__name__=_H
_SwFabricMemName_Object=MibTableColumn
swFabricMemName=_SwFabricMemName_Object((1,3,6,1,4,1,1588,2,1,1,1,2,10,1,3),_SwFabricMemName_Type())
swFabricMemName.setMaxAccess(_B)
if mibBuilder.loadTexts:swFabricMemName.setStatus(_A)
_SwFabricMemEIP_Type=IpAddress
_SwFabricMemEIP_Object=MibTableColumn
swFabricMemEIP=_SwFabricMemEIP_Object((1,3,6,1,4,1,1588,2,1,1,1,2,10,1,4),_SwFabricMemEIP_Type())
swFabricMemEIP.setMaxAccess(_B)
if mibBuilder.loadTexts:swFabricMemEIP.setStatus(_A)
_SwFabricMemFCIP_Type=IpAddress
_SwFabricMemFCIP_Object=MibTableColumn
swFabricMemFCIP=_SwFabricMemFCIP_Object((1,3,6,1,4,1,1588,2,1,1,1,2,10,1,5),_SwFabricMemFCIP_Type())
swFabricMemFCIP.setMaxAccess(_B)
if mibBuilder.loadTexts:swFabricMemFCIP.setStatus(_A)
_SwFabricMemGWIP_Type=IpAddress
_SwFabricMemGWIP_Object=MibTableColumn
swFabricMemGWIP=_SwFabricMemGWIP_Object((1,3,6,1,4,1,1588,2,1,1,1,2,10,1,6),_SwFabricMemGWIP_Type())
swFabricMemGWIP.setMaxAccess(_B)
if mibBuilder.loadTexts:swFabricMemGWIP.setStatus(_A)
class _SwFabricMemType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_SwFabricMemType_Type.__name__=_E
_SwFabricMemType_Object=MibTableColumn
swFabricMemType=_SwFabricMemType_Object((1,3,6,1,4,1,1588,2,1,1,1,2,10,1,7),_SwFabricMemType_Type())
swFabricMemType.setMaxAccess(_B)
if mibBuilder.loadTexts:swFabricMemType.setStatus(_A)
class _SwFabricMemShortVersion_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,24))
_SwFabricMemShortVersion_Type.__name__=_F
_SwFabricMemShortVersion_Object=MibTableColumn
swFabricMemShortVersion=_SwFabricMemShortVersion_Object((1,3,6,1,4,1,1588,2,1,1,1,2,10,1,8),_SwFabricMemShortVersion_Type())
swFabricMemShortVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:swFabricMemShortVersion.setStatus(_A)
class _SwIDIDMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_O,1),(_N,2)))
_SwIDIDMode_Type.__name__=_E
_SwIDIDMode_Object=MibScalar
swIDIDMode=_SwIDIDMode_Object((1,3,6,1,4,1,1588,2,1,1,1,2,11),_SwIDIDMode_Type())
swIDIDMode.setMaxAccess(_B)
if mibBuilder.loadTexts:swIDIDMode.setStatus(_A)
class _SwPmgrEventType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,6)));namedValues=NamedValues(*(('create',0),('delete',1),('moveport',2),('fidchange',3),('basechange',4),('vfstatechange',6)))
_SwPmgrEventType_Type.__name__=_E
_SwPmgrEventType_Object=MibScalar
swPmgrEventType=_SwPmgrEventType_Object((1,3,6,1,4,1,1588,2,1,1,1,2,12),_SwPmgrEventType_Type())
swPmgrEventType.setMaxAccess(_I)
if mibBuilder.loadTexts:swPmgrEventType.setStatus(_A)
class _SwPmgrEventTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_SwPmgrEventTime_Type.__name__=_H
_SwPmgrEventTime_Object=MibScalar
swPmgrEventTime=_SwPmgrEventTime_Object((1,3,6,1,4,1,1588,2,1,1,1,2,13),_SwPmgrEventTime_Type())
swPmgrEventTime.setMaxAccess(_I)
if mibBuilder.loadTexts:swPmgrEventTime.setStatus(_A)
class _SwPmgrEventDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_SwPmgrEventDescr_Type.__name__=_H
_SwPmgrEventDescr_Object=MibScalar
swPmgrEventDescr=_SwPmgrEventDescr_Object((1,3,6,1,4,1,1588,2,1,1,1,2,14),_SwPmgrEventDescr_Type())
swPmgrEventDescr.setMaxAccess(_I)
if mibBuilder.loadTexts:swPmgrEventDescr.setStatus(_A)
class _SwVfId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_SwVfId_Type.__name__=_E
_SwVfId_Object=MibScalar
swVfId=_SwVfId_Object((1,3,6,1,4,1,1588,2,1,1,1,2,15),_SwVfId_Type())
swVfId.setMaxAccess(_B)
if mibBuilder.loadTexts:swVfId.setStatus(_A)
_SwVfName_Type=DisplayString
_SwVfName_Object=MibScalar
swVfName=_SwVfName_Object((1,3,6,1,4,1,1588,2,1,1,1,2,16),_SwVfName_Type())
swVfName.setMaxAccess(_B)
if mibBuilder.loadTexts:swVfName.setStatus(_A)
_SwModule_ObjectIdentity=ObjectIdentity
swModule=_SwModule_ObjectIdentity((1,3,6,1,4,1,1588,2,1,1,1,3))
if mibBuilder.loadTexts:swModule.setStatus(_A)
_SwAgtCfg_ObjectIdentity=ObjectIdentity
swAgtCfg=_SwAgtCfg_ObjectIdentity((1,3,6,1,4,1,1588,2,1,1,1,4))
if mibBuilder.loadTexts:swAgtCfg.setStatus(_A)
_SwAgtCmtyTable_Object=MibTable
swAgtCmtyTable=_SwAgtCmtyTable_Object((1,3,6,1,4,1,1588,2,1,1,1,4,11))
if mibBuilder.loadTexts:swAgtCmtyTable.setStatus(_M)
_SwAgtCmtyEntry_Object=MibTableRow
swAgtCmtyEntry=_SwAgtCmtyEntry_Object((1,3,6,1,4,1,1588,2,1,1,1,4,11,1))
swAgtCmtyEntry.setIndexNames((0,_D,_s))
if mibBuilder.loadTexts:swAgtCmtyEntry.setStatus(_M)
class _SwAgtCmtyIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,6))
_SwAgtCmtyIdx_Type.__name__=_E
_SwAgtCmtyIdx_Object=MibTableColumn
swAgtCmtyIdx=_SwAgtCmtyIdx_Object((1,3,6,1,4,1,1588,2,1,1,1,4,11,1,1),_SwAgtCmtyIdx_Type())
swAgtCmtyIdx.setMaxAccess(_B)
if mibBuilder.loadTexts:swAgtCmtyIdx.setStatus(_M)
class _SwAgtCmtyStr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,16))
_SwAgtCmtyStr_Type.__name__=_H
_SwAgtCmtyStr_Object=MibTableColumn
swAgtCmtyStr=_SwAgtCmtyStr_Object((1,3,6,1,4,1,1588,2,1,1,1,4,11,1,2),_SwAgtCmtyStr_Type())
swAgtCmtyStr.setMaxAccess(_G)
if mibBuilder.loadTexts:swAgtCmtyStr.setStatus(_M)
_SwAgtTrapRcp_Type=IpAddress
_SwAgtTrapRcp_Object=MibTableColumn
swAgtTrapRcp=_SwAgtTrapRcp_Object((1,3,6,1,4,1,1588,2,1,1,1,4,11,1,3),_SwAgtTrapRcp_Type())
swAgtTrapRcp.setMaxAccess(_G)
if mibBuilder.loadTexts:swAgtTrapRcp.setStatus(_M)
_SwAgtTrapSeverityLevel_Type=SwSevType
_SwAgtTrapSeverityLevel_Object=MibTableColumn
swAgtTrapSeverityLevel=_SwAgtTrapSeverityLevel_Object((1,3,6,1,4,1,1588,2,1,1,1,4,11,1,4),_SwAgtTrapSeverityLevel_Type())
swAgtTrapSeverityLevel.setMaxAccess(_G)
if mibBuilder.loadTexts:swAgtTrapSeverityLevel.setStatus(_M)
class _SwauthProtocolPassword_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_SwauthProtocolPassword_Type.__name__=_F
_SwauthProtocolPassword_Object=MibScalar
swauthProtocolPassword=_SwauthProtocolPassword_Object((1,3,6,1,4,1,1588,2,1,1,1,4,12),_SwauthProtocolPassword_Type())
swauthProtocolPassword.setMaxAccess(_G)
if mibBuilder.loadTexts:swauthProtocolPassword.setStatus(_A)
class _SwprivProtocolPassword_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_SwprivProtocolPassword_Type.__name__=_F
_SwprivProtocolPassword_Object=MibScalar
swprivProtocolPassword=_SwprivProtocolPassword_Object((1,3,6,1,4,1,1588,2,1,1,1,4,13),_SwprivProtocolPassword_Type())
swprivProtocolPassword.setMaxAccess(_G)
if mibBuilder.loadTexts:swprivProtocolPassword.setStatus(_A)
_SwFCport_ObjectIdentity=ObjectIdentity
swFCport=_SwFCport_ObjectIdentity((1,3,6,1,4,1,1588,2,1,1,1,6))
if mibBuilder.loadTexts:swFCport.setStatus(_A)
class _SwFCPortCapacity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_SwFCPortCapacity_Type.__name__=_E
_SwFCPortCapacity_Object=MibScalar
swFCPortCapacity=_SwFCPortCapacity_Object((1,3,6,1,4,1,1588,2,1,1,1,6,1),_SwFCPortCapacity_Type())
swFCPortCapacity.setMaxAccess(_B)
if mibBuilder.loadTexts:swFCPortCapacity.setStatus(_A)
_SwFCPortTable_Object=MibTable
swFCPortTable=_SwFCPortTable_Object((1,3,6,1,4,1,1588,2,1,1,1,6,2))
if mibBuilder.loadTexts:swFCPortTable.setStatus(_A)
_SwFCPortEntry_Object=MibTableRow
swFCPortEntry=_SwFCPortEntry_Object((1,3,6,1,4,1,1588,2,1,1,1,6,2,1))
swFCPortEntry.setIndexNames((0,_D,_V))
if mibBuilder.loadTexts:swFCPortEntry.setStatus(_A)
_SwFCPortIndex_Type=SwPortIndex
_SwFCPortIndex_Object=MibTableColumn
swFCPortIndex=_SwFCPortIndex_Object((1,3,6,1,4,1,1588,2,1,1,1,6,2,1,1),_SwFCPortIndex_Type())
swFCPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:swFCPortIndex.setStatus(_A)
class _SwFCPortType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('stitch',1),('flannel',2),('loom',3),('bloom',4),('rdbloom',5),('wormhole',6),(_Q,7),(_J,8)))
_SwFCPortType_Type.__name__=_E
_SwFCPortType_Object=MibTableColumn
swFCPortType=_SwFCPortType_Object((1,3,6,1,4,1,1588,2,1,1,1,6,2,1,2),_SwFCPortType_Type())
swFCPortType.setMaxAccess(_B)
if mibBuilder.loadTexts:swFCPortType.setStatus(_A)
class _SwFCPortPhyState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,14,255)));namedValues=NamedValues(*(('noCard',1),('noTransceiver',2),('laserFault',3),('noLight',4),('noSync',5),('inSync',6),('portFault',7),('diagFault',8),('lockRef',9),('validating',10),('invalidModule',11),('noSigDet',14),(_J,255)))
_SwFCPortPhyState_Type.__name__=_E
_SwFCPortPhyState_Object=MibTableColumn
swFCPortPhyState=_SwFCPortPhyState_Object((1,3,6,1,4,1,1588,2,1,1,1,6,2,1,3),_SwFCPortPhyState_Type())
swFCPortPhyState.setMaxAccess(_B)
if mibBuilder.loadTexts:swFCPortPhyState.setStatus(_A)
class _SwFCPortOpStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_J,0),(_S,1),(_T,2),(_U,3),(_P,4)))
_SwFCPortOpStatus_Type.__name__=_E
_SwFCPortOpStatus_Object=MibTableColumn
swFCPortOpStatus=_SwFCPortOpStatus_Object((1,3,6,1,4,1,1588,2,1,1,1,6,2,1,4),_SwFCPortOpStatus_Type())
swFCPortOpStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:swFCPortOpStatus.setStatus(_A)
class _SwFCPortAdmStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_S,1),(_T,2),(_U,3),(_P,4)))
_SwFCPortAdmStatus_Type.__name__=_E
_SwFCPortAdmStatus_Object=MibTableColumn
swFCPortAdmStatus=_SwFCPortAdmStatus_Object((1,3,6,1,4,1,1588,2,1,1,1,6,2,1,5),_SwFCPortAdmStatus_Type())
swFCPortAdmStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:swFCPortAdmStatus.setStatus(_A)
class _SwFCPortLinkState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_O,1),(_N,2),('loopback',3)))
_SwFCPortLinkState_Type.__name__=_E
_SwFCPortLinkState_Object=MibTableColumn
swFCPortLinkState=_SwFCPortLinkState_Object((1,3,6,1,4,1,1588,2,1,1,1,6,2,1,6),_SwFCPortLinkState_Type())
swFCPortLinkState.setMaxAccess(_G)
if mibBuilder.loadTexts:swFCPortLinkState.setStatus(_A)
class _SwFCPortTxType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_J,1),('lw',2),('sw',3),('ld',4),('cu',5)))
_SwFCPortTxType_Type.__name__=_E
_SwFCPortTxType_Object=MibTableColumn
swFCPortTxType=_SwFCPortTxType_Object((1,3,6,1,4,1,1588,2,1,1,1,6,2,1,7),_SwFCPortTxType_Type())
swFCPortTxType.setMaxAccess(_B)
if mibBuilder.loadTexts:swFCPortTxType.setStatus(_A)
_SwFCPortTxWords_Type=Counter32
_SwFCPortTxWords_Object=MibTableColumn
swFCPortTxWords=_SwFCPortTxWords_Object((1,3,6,1,4,1,1588,2,1,1,1,6,2,1,11),_SwFCPortTxWords_Type())
swFCPortTxWords.setMaxAccess(_B)
if mibBuilder.loadTexts:swFCPortTxWords.setStatus(_A)
_SwFCPortRxWords_Type=Counter32
_SwFCPortRxWords_Object=MibTableColumn
swFCPortRxWords=_SwFCPortRxWords_Object((1,3,6,1,4,1,1588,2,1,1,1,6,2,1,12),_SwFCPortRxWords_Type())
swFCPortRxWords.setMaxAccess(_B)
if mibBuilder.loadTexts:swFCPortRxWords.setStatus(_A)
_SwFCPortTxFrames_Type=Counter32
_SwFCPortTxFrames_Object=MibTableColumn
swFCPortTxFrames=_SwFCPortTxFrames_Object((1,3,6,1,4,1,1588,2,1,1,1,6,2,1,13),_SwFCPortTxFrames_Type())
swFCPortTxFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:swFCPortTxFrames.setStatus(_A)
_SwFCPortRxFrames_Type=Counter32
_SwFCPortRxFrames_Object=MibTableColumn
swFCPortRxFrames=_SwFCPortRxFrames_Object((1,3,6,1,4,1,1588,2,1,1,1,6,2,1,14),_SwFCPortRxFrames_Type())
swFCPortRxFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:swFCPortRxFrames.setStatus(_A)
_SwFCPortRxC2Frames_Type=Counter32
_SwFCPortRxC2Frames_Object=MibTableColumn
swFCPortRxC2Frames=_SwFCPortRxC2Frames_Object((1,3,6,1,4,1,1588,2,1,1,1,6,2,1,15),_SwFCPortRxC2Frames_Type())
swFCPortRxC2Frames.setMaxAccess(_B)
if mibBuilder.loadTexts:swFCPortRxC2Frames.setStatus(_A)
_SwFCPortRxC3Frames_Type=Counter32
_SwFCPortRxC3Frames_Object=MibTableColumn
swFCPortRxC3Frames=_SwFCPortRxC3Frames_Object((1,3,6,1,4,1,1588,2,1,1,1,6,2,1,16),_SwFCPortRxC3Frames_Type())
swFCPortRxC3Frames.setMaxAccess(_B)
if mibBuilder.loadTexts:swFCPortRxC3Frames.setStatus(_A)
_SwFCPortRxLCs_Type=Counter32
_SwFCPortRxLCs_Object=MibTableColumn
swFCPortRxLCs=_SwFCPortRxLCs_Object((1,3,6,1,4,1,1588,2,1,1,1,6,2,1,17),_SwFCPortRxLCs_Type())
swFCPortRxLCs.setMaxAccess(_B)
if mibBuilder.loadTexts:swFCPortRxLCs.setStatus(_A)
_SwFCPortRxMcasts_Type=Counter32
_SwFCPortRxMcasts_Object=MibTableColumn
swFCPortRxMcasts=_SwFCPortRxMcasts_Object((1,3,6,1,4,1,1588,2,1,1,1,6,2,1,18),_SwFCPortRxMcasts_Type())
swFCPortRxMcasts.setMaxAccess(_B)
if mibBuilder.loadTexts:swFCPortRxMcasts.setStatus(_A)
_SwFCPortTooManyRdys_Type=Counter32
_SwFCPortTooManyRdys_Object=MibTableColumn
swFCPortTooManyRdys=_SwFCPortTooManyRdys_Object((1,3,6,1,4,1,1588,2,1,1,1,6,2,1,19),_SwFCPortTooManyRdys_Type())
swFCPortTooManyRdys.setMaxAccess(_B)
if mibBuilder.loadTexts:swFCPortTooManyRdys.setStatus(_A)
_SwFCPortNoTxCredits_Type=Counter32
_SwFCPortNoTxCredits_Object=MibTableColumn
swFCPortNoTxCredits=_SwFCPortNoTxCredits_Object((1,3,6,1,4,1,1588,2,1,1,1,6,2,1,20),_SwFCPortNoTxCredits_Type())
swFCPortNoTxCredits.setMaxAccess(_B)
if mibBuilder.loadTexts:swFCPortNoTxCredits.setStatus(_A)
_SwFCPortRxEncInFrs_Type=Counter32
_SwFCPortRxEncInFrs_Object=MibTableColumn
swFCPortRxEncInFrs=_SwFCPortRxEncInFrs_Object((1,3,6,1,4,1,1588,2,1,1,1,6,2,1,21),_SwFCPortRxEncInFrs_Type())
swFCPortRxEncInFrs.setMaxAccess(_B)
if mibBuilder.loadTexts:swFCPortRxEncInFrs.setStatus(_A)
_SwFCPortRxCrcs_Type=Counter32
_SwFCPortRxCrcs_Object=MibTableColumn
swFCPortRxCrcs=_SwFCPortRxCrcs_Object((1,3,6,1,4,1,1588,2,1,1,1,6,2,1,22),_SwFCPortRxCrcs_Type())
swFCPortRxCrcs.setMaxAccess(_B)
if mibBuilder.loadTexts:swFCPortRxCrcs.setStatus(_A)
_SwFCPortRxTruncs_Type=Counter32
_SwFCPortRxTruncs_Object=MibTableColumn
swFCPortRxTruncs=_SwFCPortRxTruncs_Object((1,3,6,1,4,1,1588,2,1,1,1,6,2,1,23),_SwFCPortRxTruncs_Type())
swFCPortRxTruncs.setMaxAccess(_B)
if mibBuilder.loadTexts:swFCPortRxTruncs.setStatus(_A)
_SwFCPortRxTooLongs_Type=Counter32
_SwFCPortRxTooLongs_Object=MibTableColumn
swFCPortRxTooLongs=_SwFCPortRxTooLongs_Object((1,3,6,1,4,1,1588,2,1,1,1,6,2,1,24),_SwFCPortRxTooLongs_Type())
swFCPortRxTooLongs.setMaxAccess(_B)
if mibBuilder.loadTexts:swFCPortRxTooLongs.setStatus(_A)
_SwFCPortRxBadEofs_Type=Counter32
_SwFCPortRxBadEofs_Object=MibTableColumn
swFCPortRxBadEofs=_SwFCPortRxBadEofs_Object((1,3,6,1,4,1,1588,2,1,1,1,6,2,1,25),_SwFCPortRxBadEofs_Type())
swFCPortRxBadEofs.setMaxAccess(_B)
if mibBuilder.loadTexts:swFCPortRxBadEofs.setStatus(_A)
_SwFCPortRxEncOutFrs_Type=Counter32
_SwFCPortRxEncOutFrs_Object=MibTableColumn
swFCPortRxEncOutFrs=_SwFCPortRxEncOutFrs_Object((1,3,6,1,4,1,1588,2,1,1,1,6,2,1,26),_SwFCPortRxEncOutFrs_Type())
swFCPortRxEncOutFrs.setMaxAccess(_B)
if mibBuilder.loadTexts:swFCPortRxEncOutFrs.setStatus(_A)
_SwFCPortRxBadOs_Type=Counter32
_SwFCPortRxBadOs_Object=MibTableColumn
swFCPortRxBadOs=_SwFCPortRxBadOs_Object((1,3,6,1,4,1,1588,2,1,1,1,6,2,1,27),_SwFCPortRxBadOs_Type())
swFCPortRxBadOs.setMaxAccess(_B)
if mibBuilder.loadTexts:swFCPortRxBadOs.setStatus(_A)
_SwFCPortC3Discards_Type=Counter32
_SwFCPortC3Discards_Object=MibTableColumn
swFCPortC3Discards=_SwFCPortC3Discards_Object((1,3,6,1,4,1,1588,2,1,1,1,6,2,1,28),_SwFCPortC3Discards_Type())
swFCPortC3Discards.setMaxAccess(_B)
if mibBuilder.loadTexts:swFCPortC3Discards.setStatus(_A)
_SwFCPortMcastTimedOuts_Type=Counter32
_SwFCPortMcastTimedOuts_Object=MibTableColumn
swFCPortMcastTimedOuts=_SwFCPortMcastTimedOuts_Object((1,3,6,1,4,1,1588,2,1,1,1,6,2,1,29),_SwFCPortMcastTimedOuts_Type())
swFCPortMcastTimedOuts.setMaxAccess(_B)
if mibBuilder.loadTexts:swFCPortMcastTimedOuts.setStatus(_A)
_SwFCPortTxMcasts_Type=Counter32
_SwFCPortTxMcasts_Object=MibTableColumn
swFCPortTxMcasts=_SwFCPortTxMcasts_Object((1,3,6,1,4,1,1588,2,1,1,1,6,2,1,30),_SwFCPortTxMcasts_Type())
swFCPortTxMcasts.setMaxAccess(_B)
if mibBuilder.loadTexts:swFCPortTxMcasts.setStatus(_A)
_SwFCPortLipIns_Type=Counter32
_SwFCPortLipIns_Object=MibTableColumn
swFCPortLipIns=_SwFCPortLipIns_Object((1,3,6,1,4,1,1588,2,1,1,1,6,2,1,31),_SwFCPortLipIns_Type())
swFCPortLipIns.setMaxAccess(_B)
if mibBuilder.loadTexts:swFCPortLipIns.setStatus(_A)
_SwFCPortLipOuts_Type=Counter32
_SwFCPortLipOuts_Object=MibTableColumn
swFCPortLipOuts=_SwFCPortLipOuts_Object((1,3,6,1,4,1,1588,2,1,1,1,6,2,1,32),_SwFCPortLipOuts_Type())
swFCPortLipOuts.setMaxAccess(_B)
if mibBuilder.loadTexts:swFCPortLipOuts.setStatus(_A)
class _SwFCPortLipLastAlpa_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_SwFCPortLipLastAlpa_Type.__name__=_F
_SwFCPortLipLastAlpa_Object=MibTableColumn
swFCPortLipLastAlpa=_SwFCPortLipLastAlpa_Object((1,3,6,1,4,1,1588,2,1,1,1,6,2,1,33),_SwFCPortLipLastAlpa_Type())
swFCPortLipLastAlpa.setMaxAccess(_B)
if mibBuilder.loadTexts:swFCPortLipLastAlpa.setStatus(_A)
class _SwFCPortWwn_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_SwFCPortWwn_Type.__name__=_F
_SwFCPortWwn_Object=MibTableColumn
swFCPortWwn=_SwFCPortWwn_Object((1,3,6,1,4,1,1588,2,1,1,1,6,2,1,34),_SwFCPortWwn_Type())
swFCPortWwn.setMaxAccess(_B)
if mibBuilder.loadTexts:swFCPortWwn.setStatus(_A)
class _SwFCPortSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('one-GB',1),('two-GB',2),('auto-Negotiate',3),('four-GB',4),('eight-GB',5),('ten-GB',6),(_J,7),('sixteen-GB',8)))
_SwFCPortSpeed_Type.__name__=_E
_SwFCPortSpeed_Object=MibTableColumn
swFCPortSpeed=_SwFCPortSpeed_Object((1,3,6,1,4,1,1588,2,1,1,1,6,2,1,35),_SwFCPortSpeed_Type())
swFCPortSpeed.setMaxAccess(_G)
if mibBuilder.loadTexts:swFCPortSpeed.setStatus(_C)
class _SwFCPortName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SwFCPortName_Type.__name__=_H
_SwFCPortName_Object=MibTableColumn
swFCPortName=_SwFCPortName_Object((1,3,6,1,4,1,1588,2,1,1,1,6,2,1,36),_SwFCPortName_Type())
swFCPortName.setMaxAccess(_B)
if mibBuilder.loadTexts:swFCPortName.setStatus(_A)
_SwFCPortSpecifier_Type=DisplayString
_SwFCPortSpecifier_Object=MibTableColumn
swFCPortSpecifier=_SwFCPortSpecifier_Object((1,3,6,1,4,1,1588,2,1,1,1,6,2,1,37),_SwFCPortSpecifier_Type())
swFCPortSpecifier.setMaxAccess(_B)
if mibBuilder.loadTexts:swFCPortSpecifier.setStatus(_A)
_SwFCPortFlag_Type=FcPortFlag
_SwFCPortFlag_Object=MibTableColumn
swFCPortFlag=_SwFCPortFlag_Object((1,3,6,1,4,1,1588,2,1,1,1,6,2,1,38),_SwFCPortFlag_Type())
swFCPortFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:swFCPortFlag.setStatus(_A)
class _SwFCPortBrcdType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_J,1),(_Q,2),(_k,3),(_l,4),(_m,5),(_n,6),(_o,7),(_p,8)))
_SwFCPortBrcdType_Type.__name__=_E
_SwFCPortBrcdType_Object=MibTableColumn
swFCPortBrcdType=_SwFCPortBrcdType_Object((1,3,6,1,4,1,1588,2,1,1,1,6,2,1,39),_SwFCPortBrcdType_Type())
swFCPortBrcdType.setMaxAccess(_B)
if mibBuilder.loadTexts:swFCPortBrcdType.setStatus(_A)
class _SwFCPortDisableReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,193,194,195,196,197,198,199,200,201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226,227,228,229,230)));namedValues=NamedValues(*(('r-recover-fail',1),('r-invalid-reason',2),('r-forced',3),('r-sw-disabled',4),('r-bl-disabled',5),('r-slot-off',6),('r-sw-enabled',7),('r-bl-enabled',8),('r-slot-on',9),('r-persistid',10),('r-sw-violation',11),('r-prv-dev-violation',12),('r-pub-dev-violation',13),('r-port-data-fail',14),('r-online-incomplete',15),('r-online-route-fail',16),('r-inconsistent',17),('r-set-vcc-fail',18),('r-ecp-in-testing',19),('r-elp-in-testing',20),('r-ecp-retries-exceeded',21),('r-invalid-ecp-state',22),('r-bad-ecp-rcvd',23),('r-send-rtmark-fail',24),('r-send-ecp-fail',25),('r-save-link-rtt-fail',26),('r-em-incnst',27),('r-pci-attach-fail',28),('r-buf-starv',29),('r-elp-fctl-mismatch',30),('r-eport-disabled',31),('r-trunk-with-vcxlt',32),('r-sw-fl-port-not-ready',33),('r-link-reinit',34),('r-domain-id-change',35),('r-auth-rejected',36),('r-auth-timeout',37),('r-auth-fail-retry',38),('r-fcr-conf-mismatch1',39),('r-fcr-conf-mismatch2',40),('r-fcr-port-ld-mode-mismatch',41),('r-fcr-ld-credit-mismatch',42),('r-fcr-set-vcc-failed',43),('r-fcr-set-rtc-failed',44),('r-fcr-elp-ver-inconsis',45),('r-fcr-elp-fctl-mismatch',46),('r-fcr-pid-mismatch',47),('r-fcr-tov-mismatch',48),('r-fcr-ld-incompat',49),('r-fcr-isolated',50),('r-elp-retries-exceeded',51),('r-fcr-exports-exceeded',52),('r-fcr-license',53),('r-fcr-conf-ex',54),('r-fcr-ftag-over',55),('r-fcr-ftag-conflict',56),('r-fcr-fowner-conflict',57),('r-fcr-zone-resource',58),('r-fcr-port-state-to',59),('r-fcr-authn-reject',60),('r-fcr-sec-fcs-list',61),('r-fcr-sec-failure',62),('r-fcr-incompatible-mode',63),('r-fcr-sec-scc-list',64),('r-fcr-generic',65),('r-sw-ex-port-not-ready',66),('r-fcr-class-f-incompat',67),('r-fcr-class-n-incompat',68),('r-fcr-invalid-flow-rcvd',69),('r-fcr-state-disabled',70),('r-fdd-strict-exist',71),('r-last-port-disable-msg',72),('r-sw-l-port-not-support',73),('r-peer-port-in-di-zone',74),('r-zone-incompat',75),('r-sw-config-l-port-not-support',76),('r-sw-port-mirror-configured',77),('r-nportlogin-inprogress',78),('r-nonpiv',79),('r-nomapping',80),('r-unknowntype',81),('r-nportoffline',82),('r-flogifailed',83),('r-nportbusy',84),('r-noflogi',85),('r-noflogiresp',86),('r-flogidupalpa',87),('r-loopcfg',88),('r-noenclicense',89),('r-nofiportmapping',90),('r-brcdfabconn',91),('r-port-reset',92),('r-floginport',93),('r-fdd-strict-conflict',94),('r-fdd-cfg-conflict',95),('r-fdd-cfg-conflict-na-neigh',96),('r-fcr-insistent-front-did-mismatch',97),('r-fcr-fabric-binding-failure',98),('r-fcr-non-standard-domain-offset',99),('r-area-in-use',100),('r-mstr-diff-pg',101),('r-mstr-diff-area',102),('r-ta-not-supported',103),('r-eport-not-supported',104),('r-fport-not-supported',105),('r-cfg-not-supported',106),('r-port-ll-th-exceeded',107),('r-port-synl-th-exceeded',108),('r-port-pe-th-exceeded',109),('f-port-disable-no-trk-lic',110),('r-port-inw-th-exceeded',111),('r-port-crc-th-exceeded',112),('f-port-tr-disable-speed-not-ok',113),('r-port-auto-disable',114),('r-fcr-export-in-non-base-sw',115),('r-base-switch-supports-no-device',116),('r-port-trunk-proto-error',117),('r-no-area-avail',118),('r-cannot-unbind-existing-area',119),('r-cannot-use-10bit-area',120),('r-authentication-required',121),('r-port-lr-th-exceeded',122),('r-fcr-export-lf-conflict',123),('r-incompat',124),('r-did-overlap',125),('r-zone-conflict',126),('r-eport-seg',127),('r-no-license',128),('r-platform-db',129),('r-sec-incompat',130),('r-sec-violation',131),('r-ecp-longdist',132),('r-dup-wwn',133),('r-eport-isolated',134),('r-ad',135),('r-esc-did-offset',136),('r-esc-etiz',137),('r-esc-fid',138),('r-safe-zone',139),('r-vf',140),('r-vf-bs-incompat',141),('r-pers-pid-on-lport',142),('r-pers-pid-portaddr-collision',143),('r-pers-pid-port-on-same-area',144),('r-pers-pid-port-addr-bnd',145),('r-msfr',146),('r-sw-halfbw-lic',147),('r-1g-mode-incompat',148),('r-10g-mode-incompat',149),('r-dual-mode-incompat',150),('r-implict-plt-service-block',151),('r-port-st-th-exceeded',152),('r-port-c3txto-th-exceeded',153),('r-eport-not-supported-def-sw',154),('r-eport-ll-th-exceeded',155),('r-eport-synl-th-exceeded',156),('r-eport-pe-th-exceeded',157),('r-eport-inw-th-exceeded',158),('r-eport-crc-th-exceeded',159),('r-eport-lr-th-exceeded',160),('r-eport-st-th-exceeded',161),('r-eport-c3txto-th-exceeded',162),('r-fopport-ll-th-exceeded',163),('r-fopport-synl-th-exceeded',164),('r-fopport-pe-th-exceeded',165),('r-fopport-inw-th-exceeded',166),('r-fopport-crc-th-exceeded',167),('r-fopport-lr-th-exceeded',168),('r-fopport-st-th-exceeded',169),('r-fopport-c3txto-th-exceeded',170),('r-fcuport-ll-th-exceeded',171),('r-fcuport-synl-th-exceeded',172),('r-fcuport-pe-th-exceeded',173),('r-fcuport-inw-th-exceeded',174),('r-fcuport-crc-th-exceeded',175),('r-fcuport-lr-th-exceeded',176),('r-fcuport-st-th-exceeded',177),('r-fcuport-c3txto-th-exceeded',178),('r-port-no-area-avail-pers-disable',179),('r-eport-locked',180),('r-enh-tizone',181),('r-sw-port-swap-not-supported',182),('r-fport-slow-drain-condition',183),('r-esc-vlanid',184),('r-port-recov-state',185),('r-port-auto-disable-losn',186),('r-port-auto-disable-losg',187),('r-port-auto-disable-ols',188),('r-port-auto-disable-nos',189),('r-port-auto-disable-lip',190),('r-port-compression',191),('r-port-encryption',192),('r-port-enccomp-res',193),('r-port-decommissioned',194),('r-port-dportmode',195),('r-port-dport-incompat',196),('r-port-enc-comp-mismatch',197),('r-non-rcs-rem-dom',198),('r-port-fips-comp-mismatch',199),('r-port-non-fips-comp-mismatch',200),('r-port-enc-auth-disabled',201),('r-port-disable-on-zeroize',202),('r-cfgspeed-not-supported',203),('r-fcr-ex-port-not-allowed',204),('r-port-duplicate-pwwn',205),('r-fcr-trunk-master-sfid-not-set',206),('r-nportistrunkmem',207),('r-policynotsupported',208),('r-no-icl-license',209),('r-no-ten-gig-license',210),('r-fdd-strict-scc-conflict',211),('r-fdd-strict-dcc-conflict',212),('r-fdd-strict-fcs-conflict',213),('r-fdd-strict-fabwide-conflict',214),('r-fdd-strict-pwd-conflict',215),('r-fcr-interop-conf',216),('r-port-enc-interop-conflict',217),('r-port-comp-interop-conflict',218),('r-no-port-open-rsp',219),('r-no-eicl-license',220),('r-eicl-license-limited',221),('r-esc-base-sw',222),('r-sw-cpu-overload',223),('r-no-icl-pod2-license',224),('r-port-area-mismatch-pers-disable',225),('r-unauthorized-device',226),('r-max-flogi-reached',227),('r-auth-not-supported-in-switch',228),('r-icl-ex-on-non-vf',229),('r-user-disabled-reason',230)))
_SwFCPortDisableReason_Type.__name__=_E
_SwFCPortDisableReason_Object=MibTableColumn
swFCPortDisableReason=_SwFCPortDisableReason_Object((1,3,6,1,4,1,1588,2,1,1,1,6,2,1,40),_SwFCPortDisableReason_Type())
swFCPortDisableReason.setMaxAccess(_I)
if mibBuilder.loadTexts:swFCPortDisableReason.setStatus(_A)
_SwNs_ObjectIdentity=ObjectIdentity
swNs=_SwNs_ObjectIdentity((1,3,6,1,4,1,1588,2,1,1,1,7))
if mibBuilder.loadTexts:swNs.setStatus(_A)
class _SwNsLocalNumEntry_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_SwNsLocalNumEntry_Type.__name__=_E
_SwNsLocalNumEntry_Object=MibScalar
swNsLocalNumEntry=_SwNsLocalNumEntry_Object((1,3,6,1,4,1,1588,2,1,1,1,7,1),_SwNsLocalNumEntry_Type())
swNsLocalNumEntry.setMaxAccess(_B)
if mibBuilder.loadTexts:swNsLocalNumEntry.setStatus(_A)
_SwNsLocalTable_Object=MibTable
swNsLocalTable=_SwNsLocalTable_Object((1,3,6,1,4,1,1588,2,1,1,1,7,2))
if mibBuilder.loadTexts:swNsLocalTable.setStatus(_A)
_SwNsLocalEntry_Object=MibTableRow
swNsLocalEntry=_SwNsLocalEntry_Object((1,3,6,1,4,1,1588,2,1,1,1,7,2,1))
swNsLocalEntry.setIndexNames((0,_D,_t))
if mibBuilder.loadTexts:swNsLocalEntry.setStatus(_A)
class _SwNsEntryIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_SwNsEntryIndex_Type.__name__=_E
_SwNsEntryIndex_Object=MibTableColumn
swNsEntryIndex=_SwNsEntryIndex_Object((1,3,6,1,4,1,1588,2,1,1,1,7,2,1,1),_SwNsEntryIndex_Type())
swNsEntryIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:swNsEntryIndex.setStatus(_A)
class _SwNsPortID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_SwNsPortID_Type.__name__=_F
_SwNsPortID_Object=MibTableColumn
swNsPortID=_SwNsPortID_Object((1,3,6,1,4,1,1588,2,1,1,1,7,2,1,2),_SwNsPortID_Type())
swNsPortID.setMaxAccess(_B)
if mibBuilder.loadTexts:swNsPortID.setStatus(_A)
class _SwNsPortType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('nPort',1),('nlPort',2)))
_SwNsPortType_Type.__name__=_E
_SwNsPortType_Object=MibTableColumn
swNsPortType=_SwNsPortType_Object((1,3,6,1,4,1,1588,2,1,1,1,7,2,1,3),_SwNsPortType_Type())
swNsPortType.setMaxAccess(_B)
if mibBuilder.loadTexts:swNsPortType.setStatus(_A)
_SwNsPortName_Type=FcWwn
_SwNsPortName_Object=MibTableColumn
swNsPortName=_SwNsPortName_Object((1,3,6,1,4,1,1588,2,1,1,1,7,2,1,4),_SwNsPortName_Type())
swNsPortName.setMaxAccess(_B)
if mibBuilder.loadTexts:swNsPortName.setStatus(_A)
class _SwNsPortSymb_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SwNsPortSymb_Type.__name__=_F
_SwNsPortSymb_Object=MibTableColumn
swNsPortSymb=_SwNsPortSymb_Object((1,3,6,1,4,1,1588,2,1,1,1,7,2,1,5),_SwNsPortSymb_Type())
swNsPortSymb.setMaxAccess(_B)
if mibBuilder.loadTexts:swNsPortSymb.setStatus(_A)
_SwNsNodeName_Type=FcWwn
_SwNsNodeName_Object=MibTableColumn
swNsNodeName=_SwNsNodeName_Object((1,3,6,1,4,1,1588,2,1,1,1,7,2,1,6),_SwNsNodeName_Type())
swNsNodeName.setMaxAccess(_B)
if mibBuilder.loadTexts:swNsNodeName.setStatus(_A)
class _SwNsNodeSymb_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SwNsNodeSymb_Type.__name__=_F
_SwNsNodeSymb_Object=MibTableColumn
swNsNodeSymb=_SwNsNodeSymb_Object((1,3,6,1,4,1,1588,2,1,1,1,7,2,1,7),_SwNsNodeSymb_Type())
swNsNodeSymb.setMaxAccess(_B)
if mibBuilder.loadTexts:swNsNodeSymb.setStatus(_A)
class _SwNsIPA_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_SwNsIPA_Type.__name__=_F
_SwNsIPA_Object=MibTableColumn
swNsIPA=_SwNsIPA_Object((1,3,6,1,4,1,1588,2,1,1,1,7,2,1,8),_SwNsIPA_Type())
swNsIPA.setMaxAccess(_B)
if mibBuilder.loadTexts:swNsIPA.setStatus(_A)
class _SwNsIpAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_SwNsIpAddress_Type.__name__=_F
_SwNsIpAddress_Object=MibTableColumn
swNsIpAddress=_SwNsIpAddress_Object((1,3,6,1,4,1,1588,2,1,1,1,7,2,1,9),_SwNsIpAddress_Type())
swNsIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:swNsIpAddress.setStatus(_A)
class _SwNsCos_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)));namedValues=NamedValues(*(('class-F',1),('class-1',2),('class-F-1',3),('class-2',4),('class-F-2',5),('class-1-2',6),('class-F-1-2',7),('class-3',8),('class-F-3',9),('class-1-3',10),('class-F-1-3',11),('class-2-3',12),('class-F-2-3',13),('class-1-2-3',14),('class-F-1-2-3',15)))
_SwNsCos_Type.__name__=_E
_SwNsCos_Object=MibTableColumn
swNsCos=_SwNsCos_Object((1,3,6,1,4,1,1588,2,1,1,1,7,2,1,10),_SwNsCos_Type())
swNsCos.setMaxAccess(_B)
if mibBuilder.loadTexts:swNsCos.setStatus(_A)
class _SwNsFc4_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(32,32));fixedLength=32
_SwNsFc4_Type.__name__=_F
_SwNsFc4_Object=MibTableColumn
swNsFc4=_SwNsFc4_Object((1,3,6,1,4,1,1588,2,1,1,1,7,2,1,11),_SwNsFc4_Type())
swNsFc4.setMaxAccess(_B)
if mibBuilder.loadTexts:swNsFc4.setStatus(_A)
class _SwNsIpNxPort_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_SwNsIpNxPort_Type.__name__=_F
_SwNsIpNxPort_Object=MibTableColumn
swNsIpNxPort=_SwNsIpNxPort_Object((1,3,6,1,4,1,1588,2,1,1,1,7,2,1,12),_SwNsIpNxPort_Type())
swNsIpNxPort.setMaxAccess(_B)
if mibBuilder.loadTexts:swNsIpNxPort.setStatus(_A)
class _SwNsWwn_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_SwNsWwn_Type.__name__=_F
_SwNsWwn_Object=MibTableColumn
swNsWwn=_SwNsWwn_Object((1,3,6,1,4,1,1588,2,1,1,1,7,2,1,13),_SwNsWwn_Type())
swNsWwn.setMaxAccess(_B)
if mibBuilder.loadTexts:swNsWwn.setStatus(_A)
class _SwNsHardAddr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,3));fixedLength=3
_SwNsHardAddr_Type.__name__=_F
_SwNsHardAddr_Object=MibTableColumn
swNsHardAddr=_SwNsHardAddr_Object((1,3,6,1,4,1,1588,2,1,1,1,7,2,1,14),_SwNsHardAddr_Type())
swNsHardAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:swNsHardAddr.setStatus(_A)
_SwEvent_ObjectIdentity=ObjectIdentity
swEvent=_SwEvent_ObjectIdentity((1,3,6,1,4,1,1588,2,1,1,1,8))
if mibBuilder.loadTexts:swEvent.setStatus(_A)
class _SwEventTrapLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_R,0),(_X,1),(_Y,2),(_Z,3),(_a,4),(_b,5)))
_SwEventTrapLevel_Type.__name__=_E
_SwEventTrapLevel_Object=MibScalar
swEventTrapLevel=_SwEventTrapLevel_Object((1,3,6,1,4,1,1588,2,1,1,1,8,1),_SwEventTrapLevel_Type())
swEventTrapLevel.setMaxAccess(_G)
if mibBuilder.loadTexts:swEventTrapLevel.setStatus(_M)
class _SwEventNumEntries_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_SwEventNumEntries_Type.__name__=_E
_SwEventNumEntries_Object=MibScalar
swEventNumEntries=_SwEventNumEntries_Object((1,3,6,1,4,1,1588,2,1,1,1,8,4),_SwEventNumEntries_Type())
swEventNumEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:swEventNumEntries.setStatus(_A)
_SwEventTable_Object=MibTable
swEventTable=_SwEventTable_Object((1,3,6,1,4,1,1588,2,1,1,1,8,5))
if mibBuilder.loadTexts:swEventTable.setStatus(_A)
_SwEventEntry_Object=MibTableRow
swEventEntry=_SwEventEntry_Object((1,3,6,1,4,1,1588,2,1,1,1,8,5,1))
swEventEntry.setIndexNames((0,_D,_d))
if mibBuilder.loadTexts:swEventEntry.setStatus(_A)
class _SwEventIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_SwEventIndex_Type.__name__=_E
_SwEventIndex_Object=MibTableColumn
swEventIndex=_SwEventIndex_Object((1,3,6,1,4,1,1588,2,1,1,1,8,5,1,1),_SwEventIndex_Type())
swEventIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:swEventIndex.setStatus(_A)
class _SwEventTimeInfo_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_SwEventTimeInfo_Type.__name__=_H
_SwEventTimeInfo_Object=MibTableColumn
swEventTimeInfo=_SwEventTimeInfo_Object((1,3,6,1,4,1,1588,2,1,1,1,8,5,1,2),_SwEventTimeInfo_Type())
swEventTimeInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:swEventTimeInfo.setStatus(_A)
class _SwEventLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_X,1),(_Y,2),(_Z,3),(_a,4),(_b,5)))
_SwEventLevel_Type.__name__=_E
_SwEventLevel_Object=MibTableColumn
swEventLevel=_SwEventLevel_Object((1,3,6,1,4,1,1588,2,1,1,1,8,5,1,3),_SwEventLevel_Type())
swEventLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:swEventLevel.setStatus(_A)
class _SwEventRepeatCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_SwEventRepeatCount_Type.__name__=_E
_SwEventRepeatCount_Object=MibTableColumn
swEventRepeatCount=_SwEventRepeatCount_Object((1,3,6,1,4,1,1588,2,1,1,1,8,5,1,4),_SwEventRepeatCount_Type())
swEventRepeatCount.setMaxAccess(_B)
if mibBuilder.loadTexts:swEventRepeatCount.setStatus(_A)
_SwEventDescr_Type=DisplayString
_SwEventDescr_Object=MibTableColumn
swEventDescr=_SwEventDescr_Object((1,3,6,1,4,1,1588,2,1,1,1,8,5,1,5),_SwEventDescr_Type())
swEventDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:swEventDescr.setStatus(_A)
class _SwEventVfId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_SwEventVfId_Type.__name__=_E
_SwEventVfId_Object=MibTableColumn
swEventVfId=_SwEventVfId_Object((1,3,6,1,4,1,1588,2,1,1,1,8,5,1,6),_SwEventVfId_Type())
swEventVfId.setMaxAccess(_B)
if mibBuilder.loadTexts:swEventVfId.setStatus(_A)
_SwFwSystem_ObjectIdentity=ObjectIdentity
swFwSystem=_SwFwSystem_ObjectIdentity((1,3,6,1,4,1,1588,2,1,1,1,10))
if mibBuilder.loadTexts:swFwSystem.setStatus(_C)
_SwFwFabricWatchLicense_Type=SwFwLicense
_SwFwFabricWatchLicense_Object=MibScalar
swFwFabricWatchLicense=_SwFwFabricWatchLicense_Object((1,3,6,1,4,1,1588,2,1,1,1,10,1),_SwFwFabricWatchLicense_Type())
swFwFabricWatchLicense.setMaxAccess(_B)
if mibBuilder.loadTexts:swFwFabricWatchLicense.setStatus(_C)
_SwFwClassAreaTable_Object=MibTable
swFwClassAreaTable=_SwFwClassAreaTable_Object((1,3,6,1,4,1,1588,2,1,1,1,10,2))
if mibBuilder.loadTexts:swFwClassAreaTable.setStatus(_C)
_SwFwClassAreaEntry_Object=MibTableRow
swFwClassAreaEntry=_SwFwClassAreaEntry_Object((1,3,6,1,4,1,1588,2,1,1,1,10,2,1))
swFwClassAreaEntry.setIndexNames((0,_D,_W))
if mibBuilder.loadTexts:swFwClassAreaEntry.setStatus(_C)
_SwFwClassAreaIndex_Type=SwFwClassesAreas
_SwFwClassAreaIndex_Object=MibTableColumn
swFwClassAreaIndex=_SwFwClassAreaIndex_Object((1,3,6,1,4,1,1588,2,1,1,1,10,2,1,1),_SwFwClassAreaIndex_Type())
swFwClassAreaIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:swFwClassAreaIndex.setStatus(_C)
_SwFwWriteThVals_Type=SwFwWriteVals
_SwFwWriteThVals_Object=MibTableColumn
swFwWriteThVals=_SwFwWriteThVals_Object((1,3,6,1,4,1,1588,2,1,1,1,10,2,1,2),_SwFwWriteThVals_Type())
swFwWriteThVals.setMaxAccess(_G)
if mibBuilder.loadTexts:swFwWriteThVals.setStatus(_C)
_SwFwDefaultUnit_Type=DisplayString
_SwFwDefaultUnit_Object=MibTableColumn
swFwDefaultUnit=_SwFwDefaultUnit_Object((1,3,6,1,4,1,1588,2,1,1,1,10,2,1,3),_SwFwDefaultUnit_Type())
swFwDefaultUnit.setMaxAccess(_B)
if mibBuilder.loadTexts:swFwDefaultUnit.setStatus(_C)
_SwFwDefaultTimebase_Type=SwFwTimebase
_SwFwDefaultTimebase_Object=MibTableColumn
swFwDefaultTimebase=_SwFwDefaultTimebase_Object((1,3,6,1,4,1,1588,2,1,1,1,10,2,1,4),_SwFwDefaultTimebase_Type())
swFwDefaultTimebase.setMaxAccess(_B)
if mibBuilder.loadTexts:swFwDefaultTimebase.setStatus(_C)
class _SwFwDefaultLow_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_SwFwDefaultLow_Type.__name__=_E
_SwFwDefaultLow_Object=MibTableColumn
swFwDefaultLow=_SwFwDefaultLow_Object((1,3,6,1,4,1,1588,2,1,1,1,10,2,1,5),_SwFwDefaultLow_Type())
swFwDefaultLow.setMaxAccess(_B)
if mibBuilder.loadTexts:swFwDefaultLow.setStatus(_C)
class _SwFwDefaultHigh_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_SwFwDefaultHigh_Type.__name__=_E
_SwFwDefaultHigh_Object=MibTableColumn
swFwDefaultHigh=_SwFwDefaultHigh_Object((1,3,6,1,4,1,1588,2,1,1,1,10,2,1,6),_SwFwDefaultHigh_Type())
swFwDefaultHigh.setMaxAccess(_B)
if mibBuilder.loadTexts:swFwDefaultHigh.setStatus(_C)
class _SwFwDefaultBufSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_SwFwDefaultBufSize_Type.__name__=_E
_SwFwDefaultBufSize_Object=MibTableColumn
swFwDefaultBufSize=_SwFwDefaultBufSize_Object((1,3,6,1,4,1,1588,2,1,1,1,10,2,1,7),_SwFwDefaultBufSize_Type())
swFwDefaultBufSize.setMaxAccess(_B)
if mibBuilder.loadTexts:swFwDefaultBufSize.setStatus(_C)
_SwFwCustUnit_Type=DisplayString
_SwFwCustUnit_Object=MibTableColumn
swFwCustUnit=_SwFwCustUnit_Object((1,3,6,1,4,1,1588,2,1,1,1,10,2,1,8),_SwFwCustUnit_Type())
swFwCustUnit.setMaxAccess(_B)
if mibBuilder.loadTexts:swFwCustUnit.setStatus(_C)
_SwFwCustTimebase_Type=SwFwTimebase
_SwFwCustTimebase_Object=MibTableColumn
swFwCustTimebase=_SwFwCustTimebase_Object((1,3,6,1,4,1,1588,2,1,1,1,10,2,1,9),_SwFwCustTimebase_Type())
swFwCustTimebase.setMaxAccess(_G)
if mibBuilder.loadTexts:swFwCustTimebase.setStatus(_C)
class _SwFwCustLow_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_SwFwCustLow_Type.__name__=_E
_SwFwCustLow_Object=MibTableColumn
swFwCustLow=_SwFwCustLow_Object((1,3,6,1,4,1,1588,2,1,1,1,10,2,1,10),_SwFwCustLow_Type())
swFwCustLow.setMaxAccess(_G)
if mibBuilder.loadTexts:swFwCustLow.setStatus(_C)
class _SwFwCustHigh_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_SwFwCustHigh_Type.__name__=_E
_SwFwCustHigh_Object=MibTableColumn
swFwCustHigh=_SwFwCustHigh_Object((1,3,6,1,4,1,1588,2,1,1,1,10,2,1,11),_SwFwCustHigh_Type())
swFwCustHigh.setMaxAccess(_G)
if mibBuilder.loadTexts:swFwCustHigh.setStatus(_C)
class _SwFwCustBufSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_SwFwCustBufSize_Type.__name__=_E
_SwFwCustBufSize_Object=MibTableColumn
swFwCustBufSize=_SwFwCustBufSize_Object((1,3,6,1,4,1,1588,2,1,1,1,10,2,1,12),_SwFwCustBufSize_Type())
swFwCustBufSize.setMaxAccess(_G)
if mibBuilder.loadTexts:swFwCustBufSize.setStatus(_C)
_SwFwThLevel_Type=SwFwLevels
_SwFwThLevel_Object=MibTableColumn
swFwThLevel=_SwFwThLevel_Object((1,3,6,1,4,1,1588,2,1,1,1,10,2,1,13),_SwFwThLevel_Type())
swFwThLevel.setMaxAccess(_G)
if mibBuilder.loadTexts:swFwThLevel.setStatus(_C)
_SwFwWriteActVals_Type=SwFwWriteVals
_SwFwWriteActVals_Object=MibTableColumn
swFwWriteActVals=_SwFwWriteActVals_Object((1,3,6,1,4,1,1588,2,1,1,1,10,2,1,14),_SwFwWriteActVals_Type())
swFwWriteActVals.setMaxAccess(_G)
if mibBuilder.loadTexts:swFwWriteActVals.setStatus(_C)
_SwFwDefaultChangedActs_Type=SwFwActs
_SwFwDefaultChangedActs_Object=MibTableColumn
swFwDefaultChangedActs=_SwFwDefaultChangedActs_Object((1,3,6,1,4,1,1588,2,1,1,1,10,2,1,15),_SwFwDefaultChangedActs_Type())
swFwDefaultChangedActs.setMaxAccess(_B)
if mibBuilder.loadTexts:swFwDefaultChangedActs.setStatus(_C)
_SwFwDefaultExceededActs_Type=SwFwActs
_SwFwDefaultExceededActs_Object=MibTableColumn
swFwDefaultExceededActs=_SwFwDefaultExceededActs_Object((1,3,6,1,4,1,1588,2,1,1,1,10,2,1,16),_SwFwDefaultExceededActs_Type())
swFwDefaultExceededActs.setMaxAccess(_B)
if mibBuilder.loadTexts:swFwDefaultExceededActs.setStatus(_C)
_SwFwDefaultBelowActs_Type=SwFwActs
_SwFwDefaultBelowActs_Object=MibTableColumn
swFwDefaultBelowActs=_SwFwDefaultBelowActs_Object((1,3,6,1,4,1,1588,2,1,1,1,10,2,1,17),_SwFwDefaultBelowActs_Type())
swFwDefaultBelowActs.setMaxAccess(_B)
if mibBuilder.loadTexts:swFwDefaultBelowActs.setStatus(_C)
_SwFwDefaultAboveActs_Type=SwFwActs
_SwFwDefaultAboveActs_Object=MibTableColumn
swFwDefaultAboveActs=_SwFwDefaultAboveActs_Object((1,3,6,1,4,1,1588,2,1,1,1,10,2,1,18),_SwFwDefaultAboveActs_Type())
swFwDefaultAboveActs.setMaxAccess(_B)
if mibBuilder.loadTexts:swFwDefaultAboveActs.setStatus(_C)
_SwFwDefaultInBetweenActs_Type=SwFwActs
_SwFwDefaultInBetweenActs_Object=MibTableColumn
swFwDefaultInBetweenActs=_SwFwDefaultInBetweenActs_Object((1,3,6,1,4,1,1588,2,1,1,1,10,2,1,19),_SwFwDefaultInBetweenActs_Type())
swFwDefaultInBetweenActs.setMaxAccess(_B)
if mibBuilder.loadTexts:swFwDefaultInBetweenActs.setStatus(_C)
_SwFwCustChangedActs_Type=SwFwActs
_SwFwCustChangedActs_Object=MibTableColumn
swFwCustChangedActs=_SwFwCustChangedActs_Object((1,3,6,1,4,1,1588,2,1,1,1,10,2,1,20),_SwFwCustChangedActs_Type())
swFwCustChangedActs.setMaxAccess(_G)
if mibBuilder.loadTexts:swFwCustChangedActs.setStatus(_C)
_SwFwCustExceededActs_Type=SwFwActs
_SwFwCustExceededActs_Object=MibTableColumn
swFwCustExceededActs=_SwFwCustExceededActs_Object((1,3,6,1,4,1,1588,2,1,1,1,10,2,1,21),_SwFwCustExceededActs_Type())
swFwCustExceededActs.setMaxAccess(_G)
if mibBuilder.loadTexts:swFwCustExceededActs.setStatus(_C)
_SwFwCustBelowActs_Type=SwFwActs
_SwFwCustBelowActs_Object=MibTableColumn
swFwCustBelowActs=_SwFwCustBelowActs_Object((1,3,6,1,4,1,1588,2,1,1,1,10,2,1,22),_SwFwCustBelowActs_Type())
swFwCustBelowActs.setMaxAccess(_G)
if mibBuilder.loadTexts:swFwCustBelowActs.setStatus(_C)
_SwFwCustAboveActs_Type=SwFwActs
_SwFwCustAboveActs_Object=MibTableColumn
swFwCustAboveActs=_SwFwCustAboveActs_Object((1,3,6,1,4,1,1588,2,1,1,1,10,2,1,23),_SwFwCustAboveActs_Type())
swFwCustAboveActs.setMaxAccess(_G)
if mibBuilder.loadTexts:swFwCustAboveActs.setStatus(_C)
_SwFwCustInBetweenActs_Type=SwFwActs
_SwFwCustInBetweenActs_Object=MibTableColumn
swFwCustInBetweenActs=_SwFwCustInBetweenActs_Object((1,3,6,1,4,1,1588,2,1,1,1,10,2,1,24),_SwFwCustInBetweenActs_Type())
swFwCustInBetweenActs.setMaxAccess(_G)
if mibBuilder.loadTexts:swFwCustInBetweenActs.setStatus(_C)
_SwFwValidActs_Type=SwFwActs
_SwFwValidActs_Object=MibTableColumn
swFwValidActs=_SwFwValidActs_Object((1,3,6,1,4,1,1588,2,1,1,1,10,2,1,25),_SwFwValidActs_Type())
swFwValidActs.setMaxAccess(_B)
if mibBuilder.loadTexts:swFwValidActs.setStatus(_C)
_SwFwActLevel_Type=SwFwLevels
_SwFwActLevel_Object=MibTableColumn
swFwActLevel=_SwFwActLevel_Object((1,3,6,1,4,1,1588,2,1,1,1,10,2,1,26),_SwFwActLevel_Type())
swFwActLevel.setMaxAccess(_G)
if mibBuilder.loadTexts:swFwActLevel.setStatus(_C)
_SwFwThresholdTable_Object=MibTable
swFwThresholdTable=_SwFwThresholdTable_Object((1,3,6,1,4,1,1588,2,1,1,1,10,3))
if mibBuilder.loadTexts:swFwThresholdTable.setStatus(_C)
_SwFwThresholdEntry_Object=MibTableRow
swFwThresholdEntry=_SwFwThresholdEntry_Object((1,3,6,1,4,1,1588,2,1,1,1,10,3,1))
swFwThresholdEntry.setIndexNames((0,_D,_W),(0,_D,_e))
if mibBuilder.loadTexts:swFwThresholdEntry.setStatus(_C)
class _SwFwThresholdIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_SwFwThresholdIndex_Type.__name__=_E
_SwFwThresholdIndex_Object=MibTableColumn
swFwThresholdIndex=_SwFwThresholdIndex_Object((1,3,6,1,4,1,1588,2,1,1,1,10,3,1,1),_SwFwThresholdIndex_Type())
swFwThresholdIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:swFwThresholdIndex.setStatus(_C)
_SwFwStatus_Type=SwFwStatus
_SwFwStatus_Object=MibTableColumn
swFwStatus=_SwFwStatus_Object((1,3,6,1,4,1,1588,2,1,1,1,10,3,1,2),_SwFwStatus_Type())
swFwStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:swFwStatus.setStatus(_C)
class _SwFwName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SwFwName_Type.__name__=_H
_SwFwName_Object=MibTableColumn
swFwName=_SwFwName_Object((1,3,6,1,4,1,1588,2,1,1,1,10,3,1,3),_SwFwName_Type())
swFwName.setMaxAccess(_B)
if mibBuilder.loadTexts:swFwName.setStatus(_C)
class _SwFwLabel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,70))
_SwFwLabel_Type.__name__=_H
_SwFwLabel_Object=MibTableColumn
swFwLabel=_SwFwLabel_Object((1,3,6,1,4,1,1588,2,1,1,1,10,3,1,4),_SwFwLabel_Type())
swFwLabel.setMaxAccess(_B)
if mibBuilder.loadTexts:swFwLabel.setStatus(_C)
class _SwFwCurVal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_SwFwCurVal_Type.__name__=_E
_SwFwCurVal_Object=MibTableColumn
swFwCurVal=_SwFwCurVal_Object((1,3,6,1,4,1,1588,2,1,1,1,10,3,1,5),_SwFwCurVal_Type())
swFwCurVal.setMaxAccess(_B)
if mibBuilder.loadTexts:swFwCurVal.setStatus(_C)
_SwFwLastEvent_Type=SwFwEvent
_SwFwLastEvent_Object=MibTableColumn
swFwLastEvent=_SwFwLastEvent_Object((1,3,6,1,4,1,1588,2,1,1,1,10,3,1,6),_SwFwLastEvent_Type())
swFwLastEvent.setMaxAccess(_B)
if mibBuilder.loadTexts:swFwLastEvent.setStatus(_C)
class _SwFwLastEventVal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_SwFwLastEventVal_Type.__name__=_E
_SwFwLastEventVal_Object=MibTableColumn
swFwLastEventVal=_SwFwLastEventVal_Object((1,3,6,1,4,1,1588,2,1,1,1,10,3,1,7),_SwFwLastEventVal_Type())
swFwLastEventVal.setMaxAccess(_B)
if mibBuilder.loadTexts:swFwLastEventVal.setStatus(_C)
class _SwFwLastEventTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SwFwLastEventTime_Type.__name__=_H
_SwFwLastEventTime_Object=MibTableColumn
swFwLastEventTime=_SwFwLastEventTime_Object((1,3,6,1,4,1,1588,2,1,1,1,10,3,1,8),_SwFwLastEventTime_Type())
swFwLastEventTime.setMaxAccess(_B)
if mibBuilder.loadTexts:swFwLastEventTime.setStatus(_C)
_SwFwLastState_Type=SwFwState
_SwFwLastState_Object=MibTableColumn
swFwLastState=_SwFwLastState_Object((1,3,6,1,4,1,1588,2,1,1,1,10,3,1,9),_SwFwLastState_Type())
swFwLastState.setMaxAccess(_B)
if mibBuilder.loadTexts:swFwLastState.setStatus(_C)
_SwFwBehaviorType_Type=SwFwBehavior
_SwFwBehaviorType_Object=MibTableColumn
swFwBehaviorType=_SwFwBehaviorType_Object((1,3,6,1,4,1,1588,2,1,1,1,10,3,1,10),_SwFwBehaviorType_Type())
swFwBehaviorType.setMaxAccess(_G)
if mibBuilder.loadTexts:swFwBehaviorType.setStatus(_C)
class _SwFwBehaviorInt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_SwFwBehaviorInt_Type.__name__=_E
_SwFwBehaviorInt_Object=MibTableColumn
swFwBehaviorInt=_SwFwBehaviorInt_Object((1,3,6,1,4,1,1588,2,1,1,1,10,3,1,11),_SwFwBehaviorInt_Type())
swFwBehaviorInt.setMaxAccess(_G)
if mibBuilder.loadTexts:swFwBehaviorInt.setStatus(_C)
_SwFwLastSeverityLevel_Type=SwSevType
_SwFwLastSeverityLevel_Object=MibTableColumn
swFwLastSeverityLevel=_SwFwLastSeverityLevel_Object((1,3,6,1,4,1,1588,2,1,1,1,10,3,1,12),_SwFwLastSeverityLevel_Type())
swFwLastSeverityLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:swFwLastSeverityLevel.setStatus(_C)
_SwEndDevice_ObjectIdentity=ObjectIdentity
swEndDevice=_SwEndDevice_ObjectIdentity((1,3,6,1,4,1,1588,2,1,1,1,21))
if mibBuilder.loadTexts:swEndDevice.setStatus(_A)
_SwEndDeviceRlsTable_Object=MibTable
swEndDeviceRlsTable=_SwEndDeviceRlsTable_Object((1,3,6,1,4,1,1588,2,1,1,1,21,1))
if mibBuilder.loadTexts:swEndDeviceRlsTable.setStatus(_A)
_SwEndDeviceRlsEntry_Object=MibTableRow
swEndDeviceRlsEntry=_SwEndDeviceRlsEntry_Object((1,3,6,1,4,1,1588,2,1,1,1,21,1,1))
swEndDeviceRlsEntry.setIndexNames((0,_D,_u),(0,_D,_v))
if mibBuilder.loadTexts:swEndDeviceRlsEntry.setStatus(_A)
class _SwEndDevicePort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_SwEndDevicePort_Type.__name__=_E
_SwEndDevicePort_Object=MibTableColumn
swEndDevicePort=_SwEndDevicePort_Object((1,3,6,1,4,1,1588,2,1,1,1,21,1,1,1),_SwEndDevicePort_Type())
swEndDevicePort.setMaxAccess(_I)
if mibBuilder.loadTexts:swEndDevicePort.setStatus(_A)
class _SwEndDeviceAlpa_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_SwEndDeviceAlpa_Type.__name__=_E
_SwEndDeviceAlpa_Object=MibTableColumn
swEndDeviceAlpa=_SwEndDeviceAlpa_Object((1,3,6,1,4,1,1588,2,1,1,1,21,1,1,2),_SwEndDeviceAlpa_Type())
swEndDeviceAlpa.setMaxAccess(_I)
if mibBuilder.loadTexts:swEndDeviceAlpa.setStatus(_A)
class _SwEndDevicePortID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_SwEndDevicePortID_Type.__name__=_F
_SwEndDevicePortID_Object=MibTableColumn
swEndDevicePortID=_SwEndDevicePortID_Object((1,3,6,1,4,1,1588,2,1,1,1,21,1,1,3),_SwEndDevicePortID_Type())
swEndDevicePortID.setMaxAccess(_B)
if mibBuilder.loadTexts:swEndDevicePortID.setStatus(_A)
_SwEndDeviceLinkFailure_Type=Counter32
_SwEndDeviceLinkFailure_Object=MibTableColumn
swEndDeviceLinkFailure=_SwEndDeviceLinkFailure_Object((1,3,6,1,4,1,1588,2,1,1,1,21,1,1,4),_SwEndDeviceLinkFailure_Type())
swEndDeviceLinkFailure.setMaxAccess(_B)
if mibBuilder.loadTexts:swEndDeviceLinkFailure.setStatus(_A)
_SwEndDeviceSyncLoss_Type=Counter32
_SwEndDeviceSyncLoss_Object=MibTableColumn
swEndDeviceSyncLoss=_SwEndDeviceSyncLoss_Object((1,3,6,1,4,1,1588,2,1,1,1,21,1,1,5),_SwEndDeviceSyncLoss_Type())
swEndDeviceSyncLoss.setMaxAccess(_B)
if mibBuilder.loadTexts:swEndDeviceSyncLoss.setStatus(_A)
_SwEndDeviceSigLoss_Type=Counter32
_SwEndDeviceSigLoss_Object=MibTableColumn
swEndDeviceSigLoss=_SwEndDeviceSigLoss_Object((1,3,6,1,4,1,1588,2,1,1,1,21,1,1,6),_SwEndDeviceSigLoss_Type())
swEndDeviceSigLoss.setMaxAccess(_B)
if mibBuilder.loadTexts:swEndDeviceSigLoss.setStatus(_A)
_SwEndDeviceProtoErr_Type=Counter32
_SwEndDeviceProtoErr_Object=MibTableColumn
swEndDeviceProtoErr=_SwEndDeviceProtoErr_Object((1,3,6,1,4,1,1588,2,1,1,1,21,1,1,7),_SwEndDeviceProtoErr_Type())
swEndDeviceProtoErr.setMaxAccess(_B)
if mibBuilder.loadTexts:swEndDeviceProtoErr.setStatus(_A)
_SwEndDeviceInvalidWord_Type=Counter32
_SwEndDeviceInvalidWord_Object=MibTableColumn
swEndDeviceInvalidWord=_SwEndDeviceInvalidWord_Object((1,3,6,1,4,1,1588,2,1,1,1,21,1,1,8),_SwEndDeviceInvalidWord_Type())
swEndDeviceInvalidWord.setMaxAccess(_B)
if mibBuilder.loadTexts:swEndDeviceInvalidWord.setStatus(_A)
_SwEndDeviceInvalidCRC_Type=Counter32
_SwEndDeviceInvalidCRC_Object=MibTableColumn
swEndDeviceInvalidCRC=_SwEndDeviceInvalidCRC_Object((1,3,6,1,4,1,1588,2,1,1,1,21,1,1,9),_SwEndDeviceInvalidCRC_Type())
swEndDeviceInvalidCRC.setMaxAccess(_B)
if mibBuilder.loadTexts:swEndDeviceInvalidCRC.setStatus(_A)
_SwGroup_ObjectIdentity=ObjectIdentity
swGroup=_SwGroup_ObjectIdentity((1,3,6,1,4,1,1588,2,1,1,1,22))
if mibBuilder.loadTexts:swGroup.setStatus(_C)
_SwGroupTable_Object=MibTable
swGroupTable=_SwGroupTable_Object((1,3,6,1,4,1,1588,2,1,1,1,22,1))
if mibBuilder.loadTexts:swGroupTable.setStatus(_C)
_SwGroupEntry_Object=MibTableRow
swGroupEntry=_SwGroupEntry_Object((1,3,6,1,4,1,1588,2,1,1,1,22,1,1))
swGroupEntry.setIndexNames((0,_D,_w))
if mibBuilder.loadTexts:swGroupEntry.setStatus(_C)
class _SwGroupIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_SwGroupIndex_Type.__name__=_E
_SwGroupIndex_Object=MibTableColumn
swGroupIndex=_SwGroupIndex_Object((1,3,6,1,4,1,1588,2,1,1,1,22,1,1,1),_SwGroupIndex_Type())
swGroupIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:swGroupIndex.setStatus(_C)
class _SwGroupName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SwGroupName_Type.__name__=_F
_SwGroupName_Object=MibTableColumn
swGroupName=_SwGroupName_Object((1,3,6,1,4,1,1588,2,1,1,1,22,1,1,2),_SwGroupName_Type())
swGroupName.setMaxAccess(_B)
if mibBuilder.loadTexts:swGroupName.setStatus(_C)
class _SwGroupType_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_SwGroupType_Type.__name__=_F
_SwGroupType_Object=MibTableColumn
swGroupType=_SwGroupType_Object((1,3,6,1,4,1,1588,2,1,1,1,22,1,1,3),_SwGroupType_Type())
swGroupType.setMaxAccess(_B)
if mibBuilder.loadTexts:swGroupType.setStatus(_C)
_SwGroupMemTable_Object=MibTable
swGroupMemTable=_SwGroupMemTable_Object((1,3,6,1,4,1,1588,2,1,1,1,22,2))
if mibBuilder.loadTexts:swGroupMemTable.setStatus(_C)
_SwGroupMemEntry_Object=MibTableRow
swGroupMemEntry=_SwGroupMemEntry_Object((1,3,6,1,4,1,1588,2,1,1,1,22,2,1))
swGroupMemEntry.setIndexNames((0,_D,_x),(0,_D,_y))
if mibBuilder.loadTexts:swGroupMemEntry.setStatus(_C)
class _SwGroupId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_SwGroupId_Type.__name__=_E
_SwGroupId_Object=MibTableColumn
swGroupId=_SwGroupId_Object((1,3,6,1,4,1,1588,2,1,1,1,22,2,1,1),_SwGroupId_Type())
swGroupId.setMaxAccess(_B)
if mibBuilder.loadTexts:swGroupId.setStatus(_C)
_SwGroupMemWwn_Type=FcWwn
_SwGroupMemWwn_Object=MibTableColumn
swGroupMemWwn=_SwGroupMemWwn_Object((1,3,6,1,4,1,1588,2,1,1,1,22,2,1,2),_SwGroupMemWwn_Type())
swGroupMemWwn.setMaxAccess(_B)
if mibBuilder.loadTexts:swGroupMemWwn.setStatus(_C)
class _SwGroupMemPos_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_SwGroupMemPos_Type.__name__=_E
_SwGroupMemPos_Object=MibTableColumn
swGroupMemPos=_SwGroupMemPos_Object((1,3,6,1,4,1,1588,2,1,1,1,22,2,1,3),_SwGroupMemPos_Type())
swGroupMemPos.setMaxAccess(_B)
if mibBuilder.loadTexts:swGroupMemPos.setStatus(_C)
_SwBlmPerfMnt_ObjectIdentity=ObjectIdentity
swBlmPerfMnt=_SwBlmPerfMnt_ObjectIdentity((1,3,6,1,4,1,1588,2,1,1,1,23))
if mibBuilder.loadTexts:swBlmPerfMnt.setStatus(_C)
_SwBlmPerfALPAMntTable_Object=MibTable
swBlmPerfALPAMntTable=_SwBlmPerfALPAMntTable_Object((1,3,6,1,4,1,1588,2,1,1,1,23,1))
if mibBuilder.loadTexts:swBlmPerfALPAMntTable.setStatus(_C)
_SwBlmPerfALPAMntEntry_Object=MibTableRow
swBlmPerfALPAMntEntry=_SwBlmPerfALPAMntEntry_Object((1,3,6,1,4,1,1588,2,1,1,1,23,1,1))
swBlmPerfALPAMntEntry.setIndexNames((0,_D,_z),(0,_D,_A0))
if mibBuilder.loadTexts:swBlmPerfALPAMntEntry.setStatus(_C)
_SwBlmPerfAlpaPort_Type=SwPortIndex
_SwBlmPerfAlpaPort_Object=MibTableColumn
swBlmPerfAlpaPort=_SwBlmPerfAlpaPort_Object((1,3,6,1,4,1,1588,2,1,1,1,23,1,1,1),_SwBlmPerfAlpaPort_Type())
swBlmPerfAlpaPort.setMaxAccess(_B)
if mibBuilder.loadTexts:swBlmPerfAlpaPort.setStatus(_C)
class _SwBlmPerfAlpaIndx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,126))
_SwBlmPerfAlpaIndx_Type.__name__=_E
_SwBlmPerfAlpaIndx_Object=MibTableColumn
swBlmPerfAlpaIndx=_SwBlmPerfAlpaIndx_Object((1,3,6,1,4,1,1588,2,1,1,1,23,1,1,2),_SwBlmPerfAlpaIndx_Type())
swBlmPerfAlpaIndx.setMaxAccess(_B)
if mibBuilder.loadTexts:swBlmPerfAlpaIndx.setStatus(_C)
class _SwBlmPerfAlpa_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_SwBlmPerfAlpa_Type.__name__=_E
_SwBlmPerfAlpa_Object=MibTableColumn
swBlmPerfAlpa=_SwBlmPerfAlpa_Object((1,3,6,1,4,1,1588,2,1,1,1,23,1,1,3),_SwBlmPerfAlpa_Type())
swBlmPerfAlpa.setMaxAccess(_B)
if mibBuilder.loadTexts:swBlmPerfAlpa.setStatus(_C)
class _SwBlmPerfAlpaCRCCnt_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_SwBlmPerfAlpaCRCCnt_Type.__name__=_F
_SwBlmPerfAlpaCRCCnt_Object=MibTableColumn
swBlmPerfAlpaCRCCnt=_SwBlmPerfAlpaCRCCnt_Object((1,3,6,1,4,1,1588,2,1,1,1,23,1,1,4),_SwBlmPerfAlpaCRCCnt_Type())
swBlmPerfAlpaCRCCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:swBlmPerfAlpaCRCCnt.setStatus(_C)
_SwBlmPerfEEMntTable_Object=MibTable
swBlmPerfEEMntTable=_SwBlmPerfEEMntTable_Object((1,3,6,1,4,1,1588,2,1,1,1,23,2))
if mibBuilder.loadTexts:swBlmPerfEEMntTable.setStatus(_C)
_SwBlmPerfEEMntEntry_Object=MibTableRow
swBlmPerfEEMntEntry=_SwBlmPerfEEMntEntry_Object((1,3,6,1,4,1,1588,2,1,1,1,23,2,1))
swBlmPerfEEMntEntry.setIndexNames((0,_D,_A1),(0,_D,_A2))
if mibBuilder.loadTexts:swBlmPerfEEMntEntry.setStatus(_C)
_SwBlmPerfEEPort_Type=SwPortIndex
_SwBlmPerfEEPort_Object=MibTableColumn
swBlmPerfEEPort=_SwBlmPerfEEPort_Object((1,3,6,1,4,1,1588,2,1,1,1,23,2,1,1),_SwBlmPerfEEPort_Type())
swBlmPerfEEPort.setMaxAccess(_B)
if mibBuilder.loadTexts:swBlmPerfEEPort.setStatus(_C)
class _SwBlmPerfEERefKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_SwBlmPerfEERefKey_Type.__name__=_E
_SwBlmPerfEERefKey_Object=MibTableColumn
swBlmPerfEERefKey=_SwBlmPerfEERefKey_Object((1,3,6,1,4,1,1588,2,1,1,1,23,2,1,2),_SwBlmPerfEERefKey_Type())
swBlmPerfEERefKey.setMaxAccess(_B)
if mibBuilder.loadTexts:swBlmPerfEERefKey.setStatus(_C)
class _SwBlmPerfEECRC_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_SwBlmPerfEECRC_Type.__name__=_F
_SwBlmPerfEECRC_Object=MibTableColumn
swBlmPerfEECRC=_SwBlmPerfEECRC_Object((1,3,6,1,4,1,1588,2,1,1,1,23,2,1,3),_SwBlmPerfEECRC_Type())
swBlmPerfEECRC.setMaxAccess(_B)
if mibBuilder.loadTexts:swBlmPerfEECRC.setStatus(_C)
class _SwBlmPerfEEFCWRx_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_SwBlmPerfEEFCWRx_Type.__name__=_F
_SwBlmPerfEEFCWRx_Object=MibTableColumn
swBlmPerfEEFCWRx=_SwBlmPerfEEFCWRx_Object((1,3,6,1,4,1,1588,2,1,1,1,23,2,1,4),_SwBlmPerfEEFCWRx_Type())
swBlmPerfEEFCWRx.setMaxAccess(_B)
if mibBuilder.loadTexts:swBlmPerfEEFCWRx.setStatus(_C)
class _SwBlmPerfEEFCWTx_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_SwBlmPerfEEFCWTx_Type.__name__=_F
_SwBlmPerfEEFCWTx_Object=MibTableColumn
swBlmPerfEEFCWTx=_SwBlmPerfEEFCWTx_Object((1,3,6,1,4,1,1588,2,1,1,1,23,2,1,5),_SwBlmPerfEEFCWTx_Type())
swBlmPerfEEFCWTx.setMaxAccess(_B)
if mibBuilder.loadTexts:swBlmPerfEEFCWTx.setStatus(_C)
class _SwBlmPerfEESid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_SwBlmPerfEESid_Type.__name__=_E
_SwBlmPerfEESid_Object=MibTableColumn
swBlmPerfEESid=_SwBlmPerfEESid_Object((1,3,6,1,4,1,1588,2,1,1,1,23,2,1,6),_SwBlmPerfEESid_Type())
swBlmPerfEESid.setMaxAccess(_B)
if mibBuilder.loadTexts:swBlmPerfEESid.setStatus(_C)
class _SwBlmPerfEEDid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_SwBlmPerfEEDid_Type.__name__=_E
_SwBlmPerfEEDid_Object=MibTableColumn
swBlmPerfEEDid=_SwBlmPerfEEDid_Object((1,3,6,1,4,1,1588,2,1,1,1,23,2,1,7),_SwBlmPerfEEDid_Type())
swBlmPerfEEDid.setMaxAccess(_B)
if mibBuilder.loadTexts:swBlmPerfEEDid.setStatus(_C)
_SwBlmPerfFltMntTable_Object=MibTable
swBlmPerfFltMntTable=_SwBlmPerfFltMntTable_Object((1,3,6,1,4,1,1588,2,1,1,1,23,3))
if mibBuilder.loadTexts:swBlmPerfFltMntTable.setStatus(_C)
_SwBlmPerfFltMntEntry_Object=MibTableRow
swBlmPerfFltMntEntry=_SwBlmPerfFltMntEntry_Object((1,3,6,1,4,1,1588,2,1,1,1,23,3,1))
swBlmPerfFltMntEntry.setIndexNames((0,_D,_A3),(0,_D,_A4))
if mibBuilder.loadTexts:swBlmPerfFltMntEntry.setStatus(_C)
_SwBlmPerfFltPort_Type=SwPortIndex
_SwBlmPerfFltPort_Object=MibTableColumn
swBlmPerfFltPort=_SwBlmPerfFltPort_Object((1,3,6,1,4,1,1588,2,1,1,1,23,3,1,1),_SwBlmPerfFltPort_Type())
swBlmPerfFltPort.setMaxAccess(_B)
if mibBuilder.loadTexts:swBlmPerfFltPort.setStatus(_C)
class _SwBlmPerfFltRefkey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_SwBlmPerfFltRefkey_Type.__name__=_E
_SwBlmPerfFltRefkey_Object=MibTableColumn
swBlmPerfFltRefkey=_SwBlmPerfFltRefkey_Object((1,3,6,1,4,1,1588,2,1,1,1,23,3,1,2),_SwBlmPerfFltRefkey_Type())
swBlmPerfFltRefkey.setMaxAccess(_B)
if mibBuilder.loadTexts:swBlmPerfFltRefkey.setStatus(_C)
class _SwBlmPerfFltCnt_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_SwBlmPerfFltCnt_Type.__name__=_F
_SwBlmPerfFltCnt_Object=MibTableColumn
swBlmPerfFltCnt=_SwBlmPerfFltCnt_Object((1,3,6,1,4,1,1588,2,1,1,1,23,3,1,3),_SwBlmPerfFltCnt_Type())
swBlmPerfFltCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:swBlmPerfFltCnt.setStatus(_C)
class _SwBlmPerfFltAlias_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_SwBlmPerfFltAlias_Type.__name__=_H
_SwBlmPerfFltAlias_Object=MibTableColumn
swBlmPerfFltAlias=_SwBlmPerfFltAlias_Object((1,3,6,1,4,1,1588,2,1,1,1,23,3,1,4),_SwBlmPerfFltAlias_Type())
swBlmPerfFltAlias.setMaxAccess(_B)
if mibBuilder.loadTexts:swBlmPerfFltAlias.setStatus(_C)
_SwTrunk_ObjectIdentity=ObjectIdentity
swTrunk=_SwTrunk_ObjectIdentity((1,3,6,1,4,1,1588,2,1,1,1,24))
if mibBuilder.loadTexts:swTrunk.setStatus(_A)
class _SwSwitchTrunkable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,8)));namedValues=NamedValues(*(('no',0),('yes',8)))
_SwSwitchTrunkable_Type.__name__=_E
_SwSwitchTrunkable_Object=MibScalar
swSwitchTrunkable=_SwSwitchTrunkable_Object((1,3,6,1,4,1,1588,2,1,1,1,24,1),_SwSwitchTrunkable_Type())
swSwitchTrunkable.setMaxAccess(_B)
if mibBuilder.loadTexts:swSwitchTrunkable.setStatus(_A)
_SwTrunkTable_Object=MibTable
swTrunkTable=_SwTrunkTable_Object((1,3,6,1,4,1,1588,2,1,1,1,24,2))
if mibBuilder.loadTexts:swTrunkTable.setStatus(_A)
_SwTrunkEntry_Object=MibTableRow
swTrunkEntry=_SwTrunkEntry_Object((1,3,6,1,4,1,1588,2,1,1,1,24,2,1))
swTrunkEntry.setIndexNames((0,_D,_A5))
if mibBuilder.loadTexts:swTrunkEntry.setStatus(_A)
_SwTrunkPortIndex_Type=SwPortIndex
_SwTrunkPortIndex_Object=MibTableColumn
swTrunkPortIndex=_SwTrunkPortIndex_Object((1,3,6,1,4,1,1588,2,1,1,1,24,2,1,1),_SwTrunkPortIndex_Type())
swTrunkPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:swTrunkPortIndex.setStatus(_A)
class _SwTrunkGroupNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_SwTrunkGroupNumber_Type.__name__=_E
_SwTrunkGroupNumber_Object=MibTableColumn
swTrunkGroupNumber=_SwTrunkGroupNumber_Object((1,3,6,1,4,1,1588,2,1,1,1,24,2,1,2),_SwTrunkGroupNumber_Type())
swTrunkGroupNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:swTrunkGroupNumber.setStatus(_A)
_SwTrunkMaster_Type=SwTrunkMaster
_SwTrunkMaster_Object=MibTableColumn
swTrunkMaster=_SwTrunkMaster_Object((1,3,6,1,4,1,1588,2,1,1,1,24,2,1,3),_SwTrunkMaster_Type())
swTrunkMaster.setMaxAccess(_B)
if mibBuilder.loadTexts:swTrunkMaster.setStatus(_A)
class _SwPortTrunked_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_N,0),(_O,1)))
_SwPortTrunked_Type.__name__=_E
_SwPortTrunked_Object=MibTableColumn
swPortTrunked=_SwPortTrunked_Object((1,3,6,1,4,1,1588,2,1,1,1,24,2,1,4),_SwPortTrunked_Type())
swPortTrunked.setMaxAccess(_B)
if mibBuilder.loadTexts:swPortTrunked.setStatus(_A)
_SwTrunkGrpTable_Object=MibTable
swTrunkGrpTable=_SwTrunkGrpTable_Object((1,3,6,1,4,1,1588,2,1,1,1,24,3))
if mibBuilder.loadTexts:swTrunkGrpTable.setStatus(_A)
_SwTrunkGrpEntry_Object=MibTableRow
swTrunkGrpEntry=_SwTrunkGrpEntry_Object((1,3,6,1,4,1,1588,2,1,1,1,24,3,1))
swTrunkGrpEntry.setIndexNames((0,_D,_A6))
if mibBuilder.loadTexts:swTrunkGrpEntry.setStatus(_A)
class _SwTrunkGrpNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_SwTrunkGrpNumber_Type.__name__=_E
_SwTrunkGrpNumber_Object=MibTableColumn
swTrunkGrpNumber=_SwTrunkGrpNumber_Object((1,3,6,1,4,1,1588,2,1,1,1,24,3,1,1),_SwTrunkGrpNumber_Type())
swTrunkGrpNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:swTrunkGrpNumber.setStatus(_A)
_SwTrunkGrpMaster_Type=SwTrunkMaster
_SwTrunkGrpMaster_Object=MibTableColumn
swTrunkGrpMaster=_SwTrunkGrpMaster_Object((1,3,6,1,4,1,1588,2,1,1,1,24,3,1,2),_SwTrunkGrpMaster_Type())
swTrunkGrpMaster.setMaxAccess(_B)
if mibBuilder.loadTexts:swTrunkGrpMaster.setStatus(_A)
class _SwTrunkGrpTx_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_SwTrunkGrpTx_Type.__name__=_F
_SwTrunkGrpTx_Object=MibTableColumn
swTrunkGrpTx=_SwTrunkGrpTx_Object((1,3,6,1,4,1,1588,2,1,1,1,24,3,1,3),_SwTrunkGrpTx_Type())
swTrunkGrpTx.setMaxAccess(_B)
if mibBuilder.loadTexts:swTrunkGrpTx.setStatus(_A)
class _SwTrunkGrpRx_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_SwTrunkGrpRx_Type.__name__=_F
_SwTrunkGrpRx_Object=MibTableColumn
swTrunkGrpRx=_SwTrunkGrpRx_Object((1,3,6,1,4,1,1588,2,1,1,1,24,3,1,4),_SwTrunkGrpRx_Type())
swTrunkGrpRx.setMaxAccess(_B)
if mibBuilder.loadTexts:swTrunkGrpRx.setStatus(_A)
_SwTopTalker_ObjectIdentity=ObjectIdentity
swTopTalker=_SwTopTalker_ObjectIdentity((1,3,6,1,4,1,1588,2,1,1,1,25))
if mibBuilder.loadTexts:swTopTalker.setStatus(_C)
class _SwTopTalkerMntMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('fabricmode',1),('portmode',2)))
_SwTopTalkerMntMode_Type.__name__=_E
_SwTopTalkerMntMode_Object=MibScalar
swTopTalkerMntMode=_SwTopTalkerMntMode_Object((1,3,6,1,4,1,1588,2,1,1,1,25,1),_SwTopTalkerMntMode_Type())
swTopTalkerMntMode.setMaxAccess(_B)
if mibBuilder.loadTexts:swTopTalkerMntMode.setStatus(_C)
class _SwTopTalkerMntNumEntries_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_SwTopTalkerMntNumEntries_Type.__name__=_E
_SwTopTalkerMntNumEntries_Object=MibScalar
swTopTalkerMntNumEntries=_SwTopTalkerMntNumEntries_Object((1,3,6,1,4,1,1588,2,1,1,1,25,2),_SwTopTalkerMntNumEntries_Type())
swTopTalkerMntNumEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:swTopTalkerMntNumEntries.setStatus(_C)
_SwTopTalkerMntTable_Object=MibTable
swTopTalkerMntTable=_SwTopTalkerMntTable_Object((1,3,6,1,4,1,1588,2,1,1,1,25,3))
if mibBuilder.loadTexts:swTopTalkerMntTable.setStatus(_C)
_SwTopTalkerMntEntry_Object=MibTableRow
swTopTalkerMntEntry=_SwTopTalkerMntEntry_Object((1,3,6,1,4,1,1588,2,1,1,1,25,3,1))
swTopTalkerMntEntry.setIndexNames((0,_D,_A7))
if mibBuilder.loadTexts:swTopTalkerMntEntry.setStatus(_C)
class _SwTopTalkerMntIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_SwTopTalkerMntIndex_Type.__name__=_E
_SwTopTalkerMntIndex_Object=MibTableColumn
swTopTalkerMntIndex=_SwTopTalkerMntIndex_Object((1,3,6,1,4,1,1588,2,1,1,1,25,3,1,1),_SwTopTalkerMntIndex_Type())
swTopTalkerMntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:swTopTalkerMntIndex.setStatus(_C)
class _SwTopTalkerMntPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_SwTopTalkerMntPort_Type.__name__=_E
_SwTopTalkerMntPort_Object=MibTableColumn
swTopTalkerMntPort=_SwTopTalkerMntPort_Object((1,3,6,1,4,1,1588,2,1,1,1,25,3,1,2),_SwTopTalkerMntPort_Type())
swTopTalkerMntPort.setMaxAccess(_B)
if mibBuilder.loadTexts:swTopTalkerMntPort.setStatus(_C)
class _SwTopTalkerMntSpid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_SwTopTalkerMntSpid_Type.__name__=_E
_SwTopTalkerMntSpid_Object=MibTableColumn
swTopTalkerMntSpid=_SwTopTalkerMntSpid_Object((1,3,6,1,4,1,1588,2,1,1,1,25,3,1,3),_SwTopTalkerMntSpid_Type())
swTopTalkerMntSpid.setMaxAccess(_B)
if mibBuilder.loadTexts:swTopTalkerMntSpid.setStatus(_C)
class _SwTopTalkerMntDpid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_SwTopTalkerMntDpid_Type.__name__=_E
_SwTopTalkerMntDpid_Object=MibTableColumn
swTopTalkerMntDpid=_SwTopTalkerMntDpid_Object((1,3,6,1,4,1,1588,2,1,1,1,25,3,1,4),_SwTopTalkerMntDpid_Type())
swTopTalkerMntDpid.setMaxAccess(_B)
if mibBuilder.loadTexts:swTopTalkerMntDpid.setStatus(_C)
class _SwTopTalkerMntflow_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_SwTopTalkerMntflow_Type.__name__=_E
_SwTopTalkerMntflow_Object=MibTableColumn
swTopTalkerMntflow=_SwTopTalkerMntflow_Object((1,3,6,1,4,1,1588,2,1,1,1,25,3,1,5),_SwTopTalkerMntflow_Type())
swTopTalkerMntflow.setMaxAccess(_B)
if mibBuilder.loadTexts:swTopTalkerMntflow.setStatus(_C)
_SwTopTalkerMntSwwn_Type=FcWwn
_SwTopTalkerMntSwwn_Object=MibTableColumn
swTopTalkerMntSwwn=_SwTopTalkerMntSwwn_Object((1,3,6,1,4,1,1588,2,1,1,1,25,3,1,6),_SwTopTalkerMntSwwn_Type())
swTopTalkerMntSwwn.setMaxAccess(_B)
if mibBuilder.loadTexts:swTopTalkerMntSwwn.setStatus(_C)
_SwTopTalkerMntDwwn_Type=FcWwn
_SwTopTalkerMntDwwn_Object=MibTableColumn
swTopTalkerMntDwwn=_SwTopTalkerMntDwwn_Object((1,3,6,1,4,1,1588,2,1,1,1,25,3,1,7),_SwTopTalkerMntDwwn_Type())
swTopTalkerMntDwwn.setMaxAccess(_B)
if mibBuilder.loadTexts:swTopTalkerMntDwwn.setStatus(_C)
_SwCpuOrMemoryUsage_ObjectIdentity=ObjectIdentity
swCpuOrMemoryUsage=_SwCpuOrMemoryUsage_ObjectIdentity((1,3,6,1,4,1,1588,2,1,1,1,26))
if mibBuilder.loadTexts:swCpuOrMemoryUsage.setStatus(_A)
class _SwCpuUsage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_SwCpuUsage_Type.__name__=_E
_SwCpuUsage_Object=MibScalar
swCpuUsage=_SwCpuUsage_Object((1,3,6,1,4,1,1588,2,1,1,1,26,1),_SwCpuUsage_Type())
swCpuUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:swCpuUsage.setStatus(_A)
class _SwCpuNoOfRetries_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_SwCpuNoOfRetries_Type.__name__=_E
_SwCpuNoOfRetries_Object=MibScalar
swCpuNoOfRetries=_SwCpuNoOfRetries_Object((1,3,6,1,4,1,1588,2,1,1,1,26,2),_SwCpuNoOfRetries_Type())
swCpuNoOfRetries.setMaxAccess(_B)
if mibBuilder.loadTexts:swCpuNoOfRetries.setStatus(_A)
class _SwCpuUsageLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_SwCpuUsageLimit_Type.__name__=_E
_SwCpuUsageLimit_Object=MibScalar
swCpuUsageLimit=_SwCpuUsageLimit_Object((1,3,6,1,4,1,1588,2,1,1,1,26,3),_SwCpuUsageLimit_Type())
swCpuUsageLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:swCpuUsageLimit.setStatus(_A)
class _SwCpuPollingInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,3600))
_SwCpuPollingInterval_Type.__name__=_E
_SwCpuPollingInterval_Object=MibScalar
swCpuPollingInterval=_SwCpuPollingInterval_Object((1,3,6,1,4,1,1588,2,1,1,1,26,4),_SwCpuPollingInterval_Type())
swCpuPollingInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:swCpuPollingInterval.setStatus(_A)
if mibBuilder.loadTexts:swCpuPollingInterval.setUnits('seconds')
class _SwCpuAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_R,0),('raslog',1),('snmp',2),(_A8,3)))
_SwCpuAction_Type.__name__=_E
_SwCpuAction_Object=MibScalar
swCpuAction=_SwCpuAction_Object((1,3,6,1,4,1,1588,2,1,1,1,26,5),_SwCpuAction_Type())
swCpuAction.setMaxAccess(_B)
if mibBuilder.loadTexts:swCpuAction.setStatus(_A)
_SwMemUsage_Type=Integer32
_SwMemUsage_Object=MibScalar
swMemUsage=_SwMemUsage_Object((1,3,6,1,4,1,1588,2,1,1,1,26,6),_SwMemUsage_Type())
swMemUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:swMemUsage.setStatus(_A)
_SwMemNoOfRetries_Type=Integer32
_SwMemNoOfRetries_Object=MibScalar
swMemNoOfRetries=_SwMemNoOfRetries_Object((1,3,6,1,4,1,1588,2,1,1,1,26,7),_SwMemNoOfRetries_Type())
swMemNoOfRetries.setMaxAccess(_B)
if mibBuilder.loadTexts:swMemNoOfRetries.setStatus(_A)
_SwMemUsageLimit_Type=Integer32
_SwMemUsageLimit_Object=MibScalar
swMemUsageLimit=_SwMemUsageLimit_Object((1,3,6,1,4,1,1588,2,1,1,1,26,8),_SwMemUsageLimit_Type())
swMemUsageLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:swMemUsageLimit.setStatus(_A)
class _SwMemPollingInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,3600))
_SwMemPollingInterval_Type.__name__=_E
_SwMemPollingInterval_Object=MibScalar
swMemPollingInterval=_SwMemPollingInterval_Object((1,3,6,1,4,1,1588,2,1,1,1,26,9),_SwMemPollingInterval_Type())
swMemPollingInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:swMemPollingInterval.setStatus(_A)
if mibBuilder.loadTexts:swMemPollingInterval.setUnits('seconds')
class _SwMemAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_R,0),('raslog',1),('snmp',2),(_A8,3)))
_SwMemAction_Type.__name__=_E
_SwMemAction_Object=MibScalar
swMemAction=_SwMemAction_Object((1,3,6,1,4,1,1588,2,1,1,1,26,10),_SwMemAction_Type())
swMemAction.setMaxAccess(_B)
if mibBuilder.loadTexts:swMemAction.setStatus(_A)
_SwMemUsageLimit1_Type=Integer32
_SwMemUsageLimit1_Object=MibScalar
swMemUsageLimit1=_SwMemUsageLimit1_Object((1,3,6,1,4,1,1588,2,1,1,1,26,11),_SwMemUsageLimit1_Type())
swMemUsageLimit1.setMaxAccess(_B)
if mibBuilder.loadTexts:swMemUsageLimit1.setStatus(_A)
_SwMemUsageLimit3_Type=Integer32
_SwMemUsageLimit3_Object=MibScalar
swMemUsageLimit3=_SwMemUsageLimit3_Object((1,3,6,1,4,1,1588,2,1,1,1,26,12),_SwMemUsageLimit3_Type())
swMemUsageLimit3.setMaxAccess(_B)
if mibBuilder.loadTexts:swMemUsageLimit3.setStatus(_A)
_SwConnUnitPortStatExtentionTable_Object=MibTable
swConnUnitPortStatExtentionTable=_SwConnUnitPortStatExtentionTable_Object((1,3,6,1,4,1,1588,2,1,1,1,27))
if mibBuilder.loadTexts:swConnUnitPortStatExtentionTable.setStatus(_A)
_SwConnUnitPortStatEntry_Object=MibTableRow
swConnUnitPortStatEntry=_SwConnUnitPortStatEntry_Object((1,3,6,1,4,1,1588,2,1,1,1,27,1))
if mibBuilder.loadTexts:swConnUnitPortStatEntry.setStatus(_A)
class _SwConnUnitCRCWithBadEOF_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_SwConnUnitCRCWithBadEOF_Type.__name__=_F
_SwConnUnitCRCWithBadEOF_Object=MibTableColumn
swConnUnitCRCWithBadEOF=_SwConnUnitCRCWithBadEOF_Object((1,3,6,1,4,1,1588,2,1,1,1,27,1,1),_SwConnUnitCRCWithBadEOF_Type())
swConnUnitCRCWithBadEOF.setMaxAccess(_B)
if mibBuilder.loadTexts:swConnUnitCRCWithBadEOF.setStatus(_A)
class _SwConnUnitZeroTenancy_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_SwConnUnitZeroTenancy_Type.__name__=_F
_SwConnUnitZeroTenancy_Object=MibTableColumn
swConnUnitZeroTenancy=_SwConnUnitZeroTenancy_Object((1,3,6,1,4,1,1588,2,1,1,1,27,1,2),_SwConnUnitZeroTenancy_Type())
swConnUnitZeroTenancy.setMaxAccess(_B)
if mibBuilder.loadTexts:swConnUnitZeroTenancy.setStatus(_A)
class _SwConnUnitFLNumOfTenancy_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_SwConnUnitFLNumOfTenancy_Type.__name__=_F
_SwConnUnitFLNumOfTenancy_Object=MibTableColumn
swConnUnitFLNumOfTenancy=_SwConnUnitFLNumOfTenancy_Object((1,3,6,1,4,1,1588,2,1,1,1,27,1,3),_SwConnUnitFLNumOfTenancy_Type())
swConnUnitFLNumOfTenancy.setMaxAccess(_B)
if mibBuilder.loadTexts:swConnUnitFLNumOfTenancy.setStatus(_A)
class _SwConnUnitNLNumOfTenancy_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_SwConnUnitNLNumOfTenancy_Type.__name__=_F
_SwConnUnitNLNumOfTenancy_Object=MibTableColumn
swConnUnitNLNumOfTenancy=_SwConnUnitNLNumOfTenancy_Object((1,3,6,1,4,1,1588,2,1,1,1,27,1,4),_SwConnUnitNLNumOfTenancy_Type())
swConnUnitNLNumOfTenancy.setMaxAccess(_B)
if mibBuilder.loadTexts:swConnUnitNLNumOfTenancy.setStatus(_A)
class _SwConnUnitStopTenancyStarVation_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_SwConnUnitStopTenancyStarVation_Type.__name__=_F
_SwConnUnitStopTenancyStarVation_Object=MibTableColumn
swConnUnitStopTenancyStarVation=_SwConnUnitStopTenancyStarVation_Object((1,3,6,1,4,1,1588,2,1,1,1,27,1,5),_SwConnUnitStopTenancyStarVation_Type())
swConnUnitStopTenancyStarVation.setMaxAccess(_B)
if mibBuilder.loadTexts:swConnUnitStopTenancyStarVation.setStatus(_A)
class _SwConnUnitOpend_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_SwConnUnitOpend_Type.__name__=_F
_SwConnUnitOpend_Object=MibTableColumn
swConnUnitOpend=_SwConnUnitOpend_Object((1,3,6,1,4,1,1588,2,1,1,1,27,1,6),_SwConnUnitOpend_Type())
swConnUnitOpend.setMaxAccess(_B)
if mibBuilder.loadTexts:swConnUnitOpend.setStatus(_A)
class _SwConnUnitTransferConnection_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_SwConnUnitTransferConnection_Type.__name__=_F
_SwConnUnitTransferConnection_Object=MibTableColumn
swConnUnitTransferConnection=_SwConnUnitTransferConnection_Object((1,3,6,1,4,1,1588,2,1,1,1,27,1,7),_SwConnUnitTransferConnection_Type())
swConnUnitTransferConnection.setMaxAccess(_B)
if mibBuilder.loadTexts:swConnUnitTransferConnection.setStatus(_A)
class _SwConnUnitOpen_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_SwConnUnitOpen_Type.__name__=_F
_SwConnUnitOpen_Object=MibTableColumn
swConnUnitOpen=_SwConnUnitOpen_Object((1,3,6,1,4,1,1588,2,1,1,1,27,1,8),_SwConnUnitOpen_Type())
swConnUnitOpen.setMaxAccess(_B)
if mibBuilder.loadTexts:swConnUnitOpen.setStatus(_A)
class _SwConnUnitInvalidARB_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_SwConnUnitInvalidARB_Type.__name__=_F
_SwConnUnitInvalidARB_Object=MibTableColumn
swConnUnitInvalidARB=_SwConnUnitInvalidARB_Object((1,3,6,1,4,1,1588,2,1,1,1,27,1,9),_SwConnUnitInvalidARB_Type())
swConnUnitInvalidARB.setMaxAccess(_B)
if mibBuilder.loadTexts:swConnUnitInvalidARB.setStatus(_A)
class _SwConnUnitFTB1Miss_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_SwConnUnitFTB1Miss_Type.__name__=_F
_SwConnUnitFTB1Miss_Object=MibTableColumn
swConnUnitFTB1Miss=_SwConnUnitFTB1Miss_Object((1,3,6,1,4,1,1588,2,1,1,1,27,1,10),_SwConnUnitFTB1Miss_Type())
swConnUnitFTB1Miss.setMaxAccess(_B)
if mibBuilder.loadTexts:swConnUnitFTB1Miss.setStatus(_A)
class _SwConnUnitFTB2Miss_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_SwConnUnitFTB2Miss_Type.__name__=_F
_SwConnUnitFTB2Miss_Object=MibTableColumn
swConnUnitFTB2Miss=_SwConnUnitFTB2Miss_Object((1,3,6,1,4,1,1588,2,1,1,1,27,1,11),_SwConnUnitFTB2Miss_Type())
swConnUnitFTB2Miss.setMaxAccess(_B)
if mibBuilder.loadTexts:swConnUnitFTB2Miss.setStatus(_A)
class _SwConnUnitFTB6Miss_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_SwConnUnitFTB6Miss_Type.__name__=_F
_SwConnUnitFTB6Miss_Object=MibTableColumn
swConnUnitFTB6Miss=_SwConnUnitFTB6Miss_Object((1,3,6,1,4,1,1588,2,1,1,1,27,1,12),_SwConnUnitFTB6Miss_Type())
swConnUnitFTB6Miss.setMaxAccess(_B)
if mibBuilder.loadTexts:swConnUnitFTB6Miss.setStatus(_A)
class _SwConnUnitZoneMiss_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_SwConnUnitZoneMiss_Type.__name__=_F
_SwConnUnitZoneMiss_Object=MibTableColumn
swConnUnitZoneMiss=_SwConnUnitZoneMiss_Object((1,3,6,1,4,1,1588,2,1,1,1,27,1,13),_SwConnUnitZoneMiss_Type())
swConnUnitZoneMiss.setMaxAccess(_B)
if mibBuilder.loadTexts:swConnUnitZoneMiss.setStatus(_A)
class _SwConnUnitLunZoneMiss_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_SwConnUnitLunZoneMiss_Type.__name__=_F
_SwConnUnitLunZoneMiss_Object=MibTableColumn
swConnUnitLunZoneMiss=_SwConnUnitLunZoneMiss_Object((1,3,6,1,4,1,1588,2,1,1,1,27,1,14),_SwConnUnitLunZoneMiss_Type())
swConnUnitLunZoneMiss.setMaxAccess(_B)
if mibBuilder.loadTexts:swConnUnitLunZoneMiss.setStatus(_A)
class _SwConnUnitBadEOF_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_SwConnUnitBadEOF_Type.__name__=_F
_SwConnUnitBadEOF_Object=MibTableColumn
swConnUnitBadEOF=_SwConnUnitBadEOF_Object((1,3,6,1,4,1,1588,2,1,1,1,27,1,15),_SwConnUnitBadEOF_Type())
swConnUnitBadEOF.setMaxAccess(_B)
if mibBuilder.loadTexts:swConnUnitBadEOF.setStatus(_A)
class _SwConnUnitLCRX_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_SwConnUnitLCRX_Type.__name__=_F
_SwConnUnitLCRX_Object=MibTableColumn
swConnUnitLCRX=_SwConnUnitLCRX_Object((1,3,6,1,4,1,1588,2,1,1,1,27,1,16),_SwConnUnitLCRX_Type())
swConnUnitLCRX.setMaxAccess(_B)
if mibBuilder.loadTexts:swConnUnitLCRX.setStatus(_A)
class _SwConnUnitRDYPriority_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_SwConnUnitRDYPriority_Type.__name__=_F
_SwConnUnitRDYPriority_Object=MibTableColumn
swConnUnitRDYPriority=_SwConnUnitRDYPriority_Object((1,3,6,1,4,1,1588,2,1,1,1,27,1,17),_SwConnUnitRDYPriority_Type())
swConnUnitRDYPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:swConnUnitRDYPriority.setStatus(_A)
class _SwConnUnitLli_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_SwConnUnitLli_Type.__name__=_F
_SwConnUnitLli_Object=MibTableColumn
swConnUnitLli=_SwConnUnitLli_Object((1,3,6,1,4,1,1588,2,1,1,1,27,1,18),_SwConnUnitLli_Type())
swConnUnitLli.setMaxAccess(_B)
if mibBuilder.loadTexts:swConnUnitLli.setStatus(_A)
class _SwConnUnitInterrupts_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_SwConnUnitInterrupts_Type.__name__=_F
_SwConnUnitInterrupts_Object=MibTableColumn
swConnUnitInterrupts=_SwConnUnitInterrupts_Object((1,3,6,1,4,1,1588,2,1,1,1,27,1,19),_SwConnUnitInterrupts_Type())
swConnUnitInterrupts.setMaxAccess(_B)
if mibBuilder.loadTexts:swConnUnitInterrupts.setStatus(_A)
class _SwConnUnitUnknownInterrupts_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_SwConnUnitUnknownInterrupts_Type.__name__=_F
_SwConnUnitUnknownInterrupts_Object=MibTableColumn
swConnUnitUnknownInterrupts=_SwConnUnitUnknownInterrupts_Object((1,3,6,1,4,1,1588,2,1,1,1,27,1,20),_SwConnUnitUnknownInterrupts_Type())
swConnUnitUnknownInterrupts.setMaxAccess(_B)
if mibBuilder.loadTexts:swConnUnitUnknownInterrupts.setStatus(_A)
class _SwConnUnitTimedOut_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_SwConnUnitTimedOut_Type.__name__=_F
_SwConnUnitTimedOut_Object=MibTableColumn
swConnUnitTimedOut=_SwConnUnitTimedOut_Object((1,3,6,1,4,1,1588,2,1,1,1,27,1,21),_SwConnUnitTimedOut_Type())
swConnUnitTimedOut.setMaxAccess(_B)
if mibBuilder.loadTexts:swConnUnitTimedOut.setStatus(_A)
class _SwConnUnitProcRequired_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_SwConnUnitProcRequired_Type.__name__=_F
_SwConnUnitProcRequired_Object=MibTableColumn
swConnUnitProcRequired=_SwConnUnitProcRequired_Object((1,3,6,1,4,1,1588,2,1,1,1,27,1,22),_SwConnUnitProcRequired_Type())
swConnUnitProcRequired.setMaxAccess(_B)
if mibBuilder.loadTexts:swConnUnitProcRequired.setStatus(_A)
class _SwConnUnitTxBufferUnavailable_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_SwConnUnitTxBufferUnavailable_Type.__name__=_F
_SwConnUnitTxBufferUnavailable_Object=MibTableColumn
swConnUnitTxBufferUnavailable=_SwConnUnitTxBufferUnavailable_Object((1,3,6,1,4,1,1588,2,1,1,1,27,1,23),_SwConnUnitTxBufferUnavailable_Type())
swConnUnitTxBufferUnavailable.setMaxAccess(_B)
if mibBuilder.loadTexts:swConnUnitTxBufferUnavailable.setStatus(_A)
class _SwConnUnitStateChange_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_SwConnUnitStateChange_Type.__name__=_F
_SwConnUnitStateChange_Object=MibTableColumn
swConnUnitStateChange=_SwConnUnitStateChange_Object((1,3,6,1,4,1,1588,2,1,1,1,27,1,24),_SwConnUnitStateChange_Type())
swConnUnitStateChange.setMaxAccess(_B)
if mibBuilder.loadTexts:swConnUnitStateChange.setStatus(_A)
class _SwConnUnitC3DiscardDueToRXTimeout_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_SwConnUnitC3DiscardDueToRXTimeout_Type.__name__=_F
_SwConnUnitC3DiscardDueToRXTimeout_Object=MibTableColumn
swConnUnitC3DiscardDueToRXTimeout=_SwConnUnitC3DiscardDueToRXTimeout_Object((1,3,6,1,4,1,1588,2,1,1,1,27,1,25),_SwConnUnitC3DiscardDueToRXTimeout_Type())
swConnUnitC3DiscardDueToRXTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:swConnUnitC3DiscardDueToRXTimeout.setStatus(_A)
class _SwConnUnitC3DiscardDueToDestUnreachable_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_SwConnUnitC3DiscardDueToDestUnreachable_Type.__name__=_F
_SwConnUnitC3DiscardDueToDestUnreachable_Object=MibTableColumn
swConnUnitC3DiscardDueToDestUnreachable=_SwConnUnitC3DiscardDueToDestUnreachable_Object((1,3,6,1,4,1,1588,2,1,1,1,27,1,26),_SwConnUnitC3DiscardDueToDestUnreachable_Type())
swConnUnitC3DiscardDueToDestUnreachable.setMaxAccess(_B)
if mibBuilder.loadTexts:swConnUnitC3DiscardDueToDestUnreachable.setStatus(_A)
class _SwConnUnitC3DiscardDueToTXTimeout_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_SwConnUnitC3DiscardDueToTXTimeout_Type.__name__=_F
_SwConnUnitC3DiscardDueToTXTimeout_Object=MibTableColumn
swConnUnitC3DiscardDueToTXTimeout=_SwConnUnitC3DiscardDueToTXTimeout_Object((1,3,6,1,4,1,1588,2,1,1,1,27,1,27),_SwConnUnitC3DiscardDueToTXTimeout_Type())
swConnUnitC3DiscardDueToTXTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:swConnUnitC3DiscardDueToTXTimeout.setStatus(_A)
class _SwConnUnitC3DiscardOther_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_SwConnUnitC3DiscardOther_Type.__name__=_F
_SwConnUnitC3DiscardOther_Object=MibTableColumn
swConnUnitC3DiscardOther=_SwConnUnitC3DiscardOther_Object((1,3,6,1,4,1,1588,2,1,1,1,27,1,28),_SwConnUnitC3DiscardOther_Type())
swConnUnitC3DiscardOther.setMaxAccess(_B)
if mibBuilder.loadTexts:swConnUnitC3DiscardOther.setStatus(_A)
class _SwConnUnitPCSErrorCounter_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_SwConnUnitPCSErrorCounter_Type.__name__=_F
_SwConnUnitPCSErrorCounter_Object=MibTableColumn
swConnUnitPCSErrorCounter=_SwConnUnitPCSErrorCounter_Object((1,3,6,1,4,1,1588,2,1,1,1,27,1,29),_SwConnUnitPCSErrorCounter_Type())
swConnUnitPCSErrorCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:swConnUnitPCSErrorCounter.setStatus(_A)
class _SwConnUnitUnroutableFrameCounter_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_SwConnUnitUnroutableFrameCounter_Type.__name__=_F
_SwConnUnitUnroutableFrameCounter_Object=MibTableColumn
swConnUnitUnroutableFrameCounter=_SwConnUnitUnroutableFrameCounter_Object((1,3,6,1,4,1,1588,2,1,1,1,27,1,30),_SwConnUnitUnroutableFrameCounter_Type())
swConnUnitUnroutableFrameCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:swConnUnitUnroutableFrameCounter.setStatus(_A)
class _SwConnUnitFECCorrectedCounter_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(64,64));fixedLength=64
_SwConnUnitFECCorrectedCounter_Type.__name__=_F
_SwConnUnitFECCorrectedCounter_Object=MibTableColumn
swConnUnitFECCorrectedCounter=_SwConnUnitFECCorrectedCounter_Object((1,3,6,1,4,1,1588,2,1,1,1,27,1,31),_SwConnUnitFECCorrectedCounter_Type())
swConnUnitFECCorrectedCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:swConnUnitFECCorrectedCounter.setStatus(_A)
class _SwConnUnitFECUnCorrectedCounter_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(64,64));fixedLength=64
_SwConnUnitFECUnCorrectedCounter_Type.__name__=_F
_SwConnUnitFECUnCorrectedCounter_Object=MibTableColumn
swConnUnitFECUnCorrectedCounter=_SwConnUnitFECUnCorrectedCounter_Object((1,3,6,1,4,1,1588,2,1,1,1,27,1,32),_SwConnUnitFECUnCorrectedCounter_Type())
swConnUnitFECUnCorrectedCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:swConnUnitFECUnCorrectedCounter.setStatus(_A)
_Sw28k_ObjectIdentity=ObjectIdentity
sw28k=_Sw28k_ObjectIdentity((1,3,6,1,4,1,1588,2,1,1,2))
if mibBuilder.loadTexts:sw28k.setStatus(_A)
_Sw21kN24k_ObjectIdentity=ObjectIdentity
sw21kN24k=_Sw21kN24k_ObjectIdentity((1,3,6,1,4,1,1588,2,1,1,3))
if mibBuilder.loadTexts:sw21kN24k.setStatus(_A)
_Sw20x0_ObjectIdentity=ObjectIdentity
sw20x0=_Sw20x0_ObjectIdentity((1,3,6,1,4,1,1588,2,1,1,4))
if mibBuilder.loadTexts:sw20x0.setStatus(_A)
connUnitPortStatEntry.registerAugmentions((_D,_A9))
swConnUnitPortStatEntry.setIndexNames(*connUnitPortStatEntry.getIndexNames())
swFault=NotificationType((1,3,6,1,4,1,1588,2,1,1,1,0,1))
swFault.setObjects(*((_D,_AA),(_D,_L)))
if mibBuilder.loadTexts:swFault.setStatus(_C)
swSensorScn=NotificationType((1,3,6,1,4,1,1588,2,1,1,1,0,2))
swSensorScn.setObjects(*((_D,_AB),(_D,_c),(_D,_AC),(_D,_AD),(_D,_AE),(_D,_L)))
if mibBuilder.loadTexts:swSensorScn.setStatus(_A)
swFCPortScn=NotificationType((1,3,6,1,4,1,1588,2,1,1,1,0,3))
swFCPortScn.setObjects(*((_D,_AF),(_D,_V),(_D,_f),(_D,_AG),(_D,_AH),(_D,_AI),(_D,_L),(_D,_g),(_D,_AJ),(_D,_K)))
if mibBuilder.loadTexts:swFCPortScn.setStatus(_A)
swEventTrap=NotificationType((1,3,6,1,4,1,1588,2,1,1,1,0,4))
swEventTrap.setObjects(*((_D,_d),(_D,_AK),(_D,_AL),(_D,_AM),(_D,_AN),(_D,_L),(_D,_K)))
if mibBuilder.loadTexts:swEventTrap.setStatus(_A)
swFabricWatchTrap=NotificationType((1,3,6,1,4,1,1588,2,1,1,1,0,5))
swFabricWatchTrap.setObjects(*((_D,_W),(_D,_e),(_D,'swFwName'),(_D,_AO),(_D,_AP),(_D,_AQ),(_D,_AR),(_D,_AS),(_D,_AT),(_D,_L),(_D,_K)))
if mibBuilder.loadTexts:swFabricWatchTrap.setStatus(_C)
swTrackChangesTrap=NotificationType((1,3,6,1,4,1,1588,2,1,1,1,0,6))
swTrackChangesTrap.setObjects(*((_D,_AU),(_D,_L),(_D,_K)))
if mibBuilder.loadTexts:swTrackChangesTrap.setStatus(_C)
swIPv6ChangeTrap=NotificationType((1,3,6,1,4,1,1588,2,1,1,1,0,7))
swIPv6ChangeTrap.setObjects(*((_D,_AV),(_D,_AW)))
if mibBuilder.loadTexts:swIPv6ChangeTrap.setStatus(_A)
swPmgrEventTrap=NotificationType((1,3,6,1,4,1,1588,2,1,1,1,0,8))
swPmgrEventTrap.setObjects(*((_D,_AX),(_D,_AY),(_D,_AZ),(_D,_L),(_D,_K)))
if mibBuilder.loadTexts:swPmgrEventTrap.setStatus(_A)
swFabricReconfigTrap=NotificationType((1,3,6,1,4,1,1588,2,1,1,1,0,9))
swFabricReconfigTrap.setObjects((_D,_Aa))
if mibBuilder.loadTexts:swFabricReconfigTrap.setStatus(_A)
swFabricSegmentTrap=NotificationType((1,3,6,1,4,1,1588,2,1,1,1,0,10))
swFabricSegmentTrap.setObjects(*((_D,_V),(_D,_f),(_D,_L),(_D,_g),(_D,_K)))
if mibBuilder.loadTexts:swFabricSegmentTrap.setStatus(_A)
swExtTrap=NotificationType((1,3,6,1,4,1,1588,2,1,1,1,0,11))
if mibBuilder.loadTexts:swExtTrap.setStatus(_A)
swStateChangeTrap=NotificationType((1,3,6,1,4,1,1588,2,1,1,1,0,12))
swStateChangeTrap.setObjects(*((_D,_Ab),(_D,_K)))
if mibBuilder.loadTexts:swStateChangeTrap.setStatus(_A)
swPortMoveTrap=NotificationType((1,3,6,1,4,1,1588,2,1,1,1,0,13))
swPortMoveTrap.setObjects(*((_D,_Ac),(_D,_K)))
if mibBuilder.loadTexts:swPortMoveTrap.setStatus(_A)
swBrcdGenericTrap=NotificationType((1,3,6,1,4,1,1588,2,1,1,1,0,14))
swBrcdGenericTrap.setObjects(*((_D,_Ad),(_D,_Ae),(_D,_K)))
if mibBuilder.loadTexts:swBrcdGenericTrap.setStatus(_A)
swDeviceStatusTrap=NotificationType((1,3,6,1,4,1,1588,2,1,1,1,0,15))
swDeviceStatusTrap.setObjects(*((_D,_Af),(_D,_Ag),(_D,_Ah),(_D,_Ai)))
if mibBuilder.loadTexts:swDeviceStatusTrap.setStatus(_A)
swZoneConfigChangeTrap=NotificationType((1,3,6,1,4,1,1588,2,1,1,1,0,16))
swZoneConfigChangeTrap.setObjects((_D,_K))
if mibBuilder.loadTexts:swZoneConfigChangeTrap.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'SwSevType':SwSevType,'FcPortFlag':FcPortFlag,'SwFwActs':SwFwActs,'SwFwLevels':SwFwLevels,'SwFwClassesAreas':SwFwClassesAreas,'SwFwWriteVals':SwFwWriteVals,'SwFwTimebase':SwFwTimebase,'SwFwStatus':SwFwStatus,'SwFwEvent':SwFwEvent,'SwFwBehavior':SwFwBehavior,'SwFwState':SwFwState,'SwFwLicense':SwFwLicense,'sw':sw,'swTrapsV2':swTrapsV2,'swFault':swFault,'swSensorScn':swSensorScn,'swFCPortScn':swFCPortScn,'swEventTrap':swEventTrap,'swFabricWatchTrap':swFabricWatchTrap,'swTrackChangesTrap':swTrackChangesTrap,'swIPv6ChangeTrap':swIPv6ChangeTrap,'swPmgrEventTrap':swPmgrEventTrap,'swFabricReconfigTrap':swFabricReconfigTrap,'swFabricSegmentTrap':swFabricSegmentTrap,'swExtTrap':swExtTrap,'swStateChangeTrap':swStateChangeTrap,'swPortMoveTrap':swPortMoveTrap,'swBrcdGenericTrap':swBrcdGenericTrap,'swDeviceStatusTrap':swDeviceStatusTrap,'swZoneConfigChangeTrap':swZoneConfigChangeTrap,'swSystem':swSystem,'swCurrentDate':swCurrentDate,'swBootDate':swBootDate,'swFWLastUpdated':swFWLastUpdated,'swFlashLastUpdated':swFlashLastUpdated,'swBootPromLastUpdated':swBootPromLastUpdated,'swFirmwareVersion':swFirmwareVersion,_Ab:swOperStatus,'swAdmStatus':swAdmStatus,'swTelnetShellAdmStatus':swTelnetShellAdmStatus,_L:swSsn,'swFlashDLOperStatus':swFlashDLOperStatus,'swFlashDLAdmStatus':swFlashDLAdmStatus,'swFlashDLHost':swFlashDLHost,'swFlashDLUser':swFlashDLUser,'swFlashDLFile':swFlashDLFile,'swFlashDLPassword':swFlashDLPassword,'swBeaconOperStatus':swBeaconOperStatus,'swBeaconAdmStatus':swBeaconAdmStatus,_AA:swDiagResult,'swNumSensors':swNumSensors,'swSensorTable':swSensorTable,'swSensorEntry':swSensorEntry,_c:swSensorIndex,_AC:swSensorType,_AB:swSensorStatus,_AD:swSensorValue,_AE:swSensorInfo,_AU:swTrackChangesInfo,'swID':swID,'swEtherIPAddress':swEtherIPAddress,'swEtherIPMask':swEtherIPMask,'swFCIPAddress':swFCIPAddress,'swFCIPMask':swFCIPMask,_AV:swIPv6Address,_AW:swIPv6Status,'swModel':swModel,'swTestString':swTestString,_Ac:swPortList,_Ad:swBrcdTrapBitMask,_AH:swFCPortPrevType,_Ag:swDeviceStatus,_Ae:swBrcdBitObjVal,'swIODState':swIODState,'swFabric':swFabric,_Aa:swDomainID,'swPrincipalSwitch':swPrincipalSwitch,'swNumNbs':swNumNbs,'swNbTable':swNbTable,'swNbEntry':swNbEntry,_q:swNbIndex,'swNbMyPort':swNbMyPort,'swNbRemDomain':swNbRemDomain,'swNbRemPort':swNbRemPort,'swNbBaudRate':swNbBaudRate,'swNbIslState':swNbIslState,'swNbIslCost':swNbIslCost,'swNbRemPortName':swNbRemPortName,'swFabricMemTable':swFabricMemTable,'swFabricMemEntry':swFabricMemEntry,_r:swFabricMemWwn,'swFabricMemDid':swFabricMemDid,'swFabricMemName':swFabricMemName,'swFabricMemEIP':swFabricMemEIP,'swFabricMemFCIP':swFabricMemFCIP,'swFabricMemGWIP':swFabricMemGWIP,'swFabricMemType':swFabricMemType,'swFabricMemShortVersion':swFabricMemShortVersion,'swIDIDMode':swIDIDMode,_AX:swPmgrEventType,_AY:swPmgrEventTime,_AZ:swPmgrEventDescr,_K:swVfId,'swVfName':swVfName,'swModule':swModule,'swAgtCfg':swAgtCfg,'swAgtCmtyTable':swAgtCmtyTable,'swAgtCmtyEntry':swAgtCmtyEntry,_s:swAgtCmtyIdx,'swAgtCmtyStr':swAgtCmtyStr,'swAgtTrapRcp':swAgtTrapRcp,'swAgtTrapSeverityLevel':swAgtTrapSeverityLevel,'swauthProtocolPassword':swauthProtocolPassword,'swprivProtocolPassword':swprivProtocolPassword,'swFCport':swFCport,'swFCPortCapacity':swFCPortCapacity,'swFCPortTable':swFCPortTable,'swFCPortEntry':swFCPortEntry,_V:swFCPortIndex,'swFCPortType':swFCPortType,'swFCPortPhyState':swFCPortPhyState,_AF:swFCPortOpStatus,'swFCPortAdmStatus':swFCPortAdmStatus,'swFCPortLinkState':swFCPortLinkState,'swFCPortTxType':swFCPortTxType,'swFCPortTxWords':swFCPortTxWords,'swFCPortRxWords':swFCPortRxWords,'swFCPortTxFrames':swFCPortTxFrames,'swFCPortRxFrames':swFCPortRxFrames,'swFCPortRxC2Frames':swFCPortRxC2Frames,'swFCPortRxC3Frames':swFCPortRxC3Frames,'swFCPortRxLCs':swFCPortRxLCs,'swFCPortRxMcasts':swFCPortRxMcasts,'swFCPortTooManyRdys':swFCPortTooManyRdys,'swFCPortNoTxCredits':swFCPortNoTxCredits,'swFCPortRxEncInFrs':swFCPortRxEncInFrs,'swFCPortRxCrcs':swFCPortRxCrcs,'swFCPortRxTruncs':swFCPortRxTruncs,'swFCPortRxTooLongs':swFCPortRxTooLongs,'swFCPortRxBadEofs':swFCPortRxBadEofs,'swFCPortRxEncOutFrs':swFCPortRxEncOutFrs,'swFCPortRxBadOs':swFCPortRxBadOs,'swFCPortC3Discards':swFCPortC3Discards,'swFCPortMcastTimedOuts':swFCPortMcastTimedOuts,'swFCPortTxMcasts':swFCPortTxMcasts,'swFCPortLipIns':swFCPortLipIns,'swFCPortLipOuts':swFCPortLipOuts,'swFCPortLipLastAlpa':swFCPortLipLastAlpa,_AG:swFCPortWwn,'swFCPortSpeed':swFCPortSpeed,_f:swFCPortName,_Af:swFCPortSpecifier,_g:swFCPortFlag,_AI:swFCPortBrcdType,_AJ:swFCPortDisableReason,'swNs':swNs,'swNsLocalNumEntry':swNsLocalNumEntry,'swNsLocalTable':swNsLocalTable,'swNsLocalEntry':swNsLocalEntry,_t:swNsEntryIndex,'swNsPortID':swNsPortID,'swNsPortType':swNsPortType,'swNsPortName':swNsPortName,'swNsPortSymb':swNsPortSymb,_Ai:swNsNodeName,'swNsNodeSymb':swNsNodeSymb,'swNsIPA':swNsIPA,'swNsIpAddress':swNsIpAddress,'swNsCos':swNsCos,'swNsFc4':swNsFc4,'swNsIpNxPort':swNsIpNxPort,'swNsWwn':swNsWwn,'swNsHardAddr':swNsHardAddr,'swEvent':swEvent,'swEventTrapLevel':swEventTrapLevel,'swEventNumEntries':swEventNumEntries,'swEventTable':swEventTable,'swEventEntry':swEventEntry,_d:swEventIndex,_AK:swEventTimeInfo,_AL:swEventLevel,_AM:swEventRepeatCount,_AN:swEventDescr,'swEventVfId':swEventVfId,'swFwSystem':swFwSystem,'swFwFabricWatchLicense':swFwFabricWatchLicense,'swFwClassAreaTable':swFwClassAreaTable,'swFwClassAreaEntry':swFwClassAreaEntry,_W:swFwClassAreaIndex,'swFwWriteThVals':swFwWriteThVals,'swFwDefaultUnit':swFwDefaultUnit,'swFwDefaultTimebase':swFwDefaultTimebase,'swFwDefaultLow':swFwDefaultLow,'swFwDefaultHigh':swFwDefaultHigh,'swFwDefaultBufSize':swFwDefaultBufSize,'swFwCustUnit':swFwCustUnit,'swFwCustTimebase':swFwCustTimebase,'swFwCustLow':swFwCustLow,'swFwCustHigh':swFwCustHigh,'swFwCustBufSize':swFwCustBufSize,'swFwThLevel':swFwThLevel,'swFwWriteActVals':swFwWriteActVals,'swFwDefaultChangedActs':swFwDefaultChangedActs,'swFwDefaultExceededActs':swFwDefaultExceededActs,'swFwDefaultBelowActs':swFwDefaultBelowActs,'swFwDefaultAboveActs':swFwDefaultAboveActs,'swFwDefaultInBetweenActs':swFwDefaultInBetweenActs,'swFwCustChangedActs':swFwCustChangedActs,'swFwCustExceededActs':swFwCustExceededActs,'swFwCustBelowActs':swFwCustBelowActs,'swFwCustAboveActs':swFwCustAboveActs,'swFwCustInBetweenActs':swFwCustInBetweenActs,'swFwValidActs':swFwValidActs,'swFwActLevel':swFwActLevel,'swFwThresholdTable':swFwThresholdTable,'swFwThresholdEntry':swFwThresholdEntry,_e:swFwThresholdIndex,'swFwStatus':swFwStatus,'swFwName':swFwName,_AO:swFwLabel,'swFwCurVal':swFwCurVal,_AR:swFwLastEvent,_AP:swFwLastEventVal,_AQ:swFwLastEventTime,_AS:swFwLastState,'swFwBehaviorType':swFwBehaviorType,'swFwBehaviorInt':swFwBehaviorInt,_AT:swFwLastSeverityLevel,'swEndDevice':swEndDevice,'swEndDeviceRlsTable':swEndDeviceRlsTable,'swEndDeviceRlsEntry':swEndDeviceRlsEntry,_u:swEndDevicePort,_v:swEndDeviceAlpa,_Ah:swEndDevicePortID,'swEndDeviceLinkFailure':swEndDeviceLinkFailure,'swEndDeviceSyncLoss':swEndDeviceSyncLoss,'swEndDeviceSigLoss':swEndDeviceSigLoss,'swEndDeviceProtoErr':swEndDeviceProtoErr,'swEndDeviceInvalidWord':swEndDeviceInvalidWord,'swEndDeviceInvalidCRC':swEndDeviceInvalidCRC,'swGroup':swGroup,'swGroupTable':swGroupTable,'swGroupEntry':swGroupEntry,_w:swGroupIndex,'swGroupName':swGroupName,'swGroupType':swGroupType,'swGroupMemTable':swGroupMemTable,'swGroupMemEntry':swGroupMemEntry,_x:swGroupId,_y:swGroupMemWwn,'swGroupMemPos':swGroupMemPos,'swBlmPerfMnt':swBlmPerfMnt,'swBlmPerfALPAMntTable':swBlmPerfALPAMntTable,'swBlmPerfALPAMntEntry':swBlmPerfALPAMntEntry,_z:swBlmPerfAlpaPort,_A0:swBlmPerfAlpaIndx,'swBlmPerfAlpa':swBlmPerfAlpa,'swBlmPerfAlpaCRCCnt':swBlmPerfAlpaCRCCnt,'swBlmPerfEEMntTable':swBlmPerfEEMntTable,'swBlmPerfEEMntEntry':swBlmPerfEEMntEntry,_A1:swBlmPerfEEPort,_A2:swBlmPerfEERefKey,'swBlmPerfEECRC':swBlmPerfEECRC,'swBlmPerfEEFCWRx':swBlmPerfEEFCWRx,'swBlmPerfEEFCWTx':swBlmPerfEEFCWTx,'swBlmPerfEESid':swBlmPerfEESid,'swBlmPerfEEDid':swBlmPerfEEDid,'swBlmPerfFltMntTable':swBlmPerfFltMntTable,'swBlmPerfFltMntEntry':swBlmPerfFltMntEntry,_A3:swBlmPerfFltPort,_A4:swBlmPerfFltRefkey,'swBlmPerfFltCnt':swBlmPerfFltCnt,'swBlmPerfFltAlias':swBlmPerfFltAlias,'swTrunk':swTrunk,'swSwitchTrunkable':swSwitchTrunkable,'swTrunkTable':swTrunkTable,'swTrunkEntry':swTrunkEntry,_A5:swTrunkPortIndex,'swTrunkGroupNumber':swTrunkGroupNumber,'swTrunkMaster':swTrunkMaster,'swPortTrunked':swPortTrunked,'swTrunkGrpTable':swTrunkGrpTable,'swTrunkGrpEntry':swTrunkGrpEntry,_A6:swTrunkGrpNumber,'swTrunkGrpMaster':swTrunkGrpMaster,'swTrunkGrpTx':swTrunkGrpTx,'swTrunkGrpRx':swTrunkGrpRx,'swTopTalker':swTopTalker,'swTopTalkerMntMode':swTopTalkerMntMode,'swTopTalkerMntNumEntries':swTopTalkerMntNumEntries,'swTopTalkerMntTable':swTopTalkerMntTable,'swTopTalkerMntEntry':swTopTalkerMntEntry,_A7:swTopTalkerMntIndex,'swTopTalkerMntPort':swTopTalkerMntPort,'swTopTalkerMntSpid':swTopTalkerMntSpid,'swTopTalkerMntDpid':swTopTalkerMntDpid,'swTopTalkerMntflow':swTopTalkerMntflow,'swTopTalkerMntSwwn':swTopTalkerMntSwwn,'swTopTalkerMntDwwn':swTopTalkerMntDwwn,'swCpuOrMemoryUsage':swCpuOrMemoryUsage,'swCpuUsage':swCpuUsage,'swCpuNoOfRetries':swCpuNoOfRetries,'swCpuUsageLimit':swCpuUsageLimit,'swCpuPollingInterval':swCpuPollingInterval,'swCpuAction':swCpuAction,'swMemUsage':swMemUsage,'swMemNoOfRetries':swMemNoOfRetries,'swMemUsageLimit':swMemUsageLimit,'swMemPollingInterval':swMemPollingInterval,'swMemAction':swMemAction,'swMemUsageLimit1':swMemUsageLimit1,'swMemUsageLimit3':swMemUsageLimit3,'swConnUnitPortStatExtentionTable':swConnUnitPortStatExtentionTable,_A9:swConnUnitPortStatEntry,'swConnUnitCRCWithBadEOF':swConnUnitCRCWithBadEOF,'swConnUnitZeroTenancy':swConnUnitZeroTenancy,'swConnUnitFLNumOfTenancy':swConnUnitFLNumOfTenancy,'swConnUnitNLNumOfTenancy':swConnUnitNLNumOfTenancy,'swConnUnitStopTenancyStarVation':swConnUnitStopTenancyStarVation,'swConnUnitOpend':swConnUnitOpend,'swConnUnitTransferConnection':swConnUnitTransferConnection,'swConnUnitOpen':swConnUnitOpen,'swConnUnitInvalidARB':swConnUnitInvalidARB,'swConnUnitFTB1Miss':swConnUnitFTB1Miss,'swConnUnitFTB2Miss':swConnUnitFTB2Miss,'swConnUnitFTB6Miss':swConnUnitFTB6Miss,'swConnUnitZoneMiss':swConnUnitZoneMiss,'swConnUnitLunZoneMiss':swConnUnitLunZoneMiss,'swConnUnitBadEOF':swConnUnitBadEOF,'swConnUnitLCRX':swConnUnitLCRX,'swConnUnitRDYPriority':swConnUnitRDYPriority,'swConnUnitLli':swConnUnitLli,'swConnUnitInterrupts':swConnUnitInterrupts,'swConnUnitUnknownInterrupts':swConnUnitUnknownInterrupts,'swConnUnitTimedOut':swConnUnitTimedOut,'swConnUnitProcRequired':swConnUnitProcRequired,'swConnUnitTxBufferUnavailable':swConnUnitTxBufferUnavailable,'swConnUnitStateChange':swConnUnitStateChange,'swConnUnitC3DiscardDueToRXTimeout':swConnUnitC3DiscardDueToRXTimeout,'swConnUnitC3DiscardDueToDestUnreachable':swConnUnitC3DiscardDueToDestUnreachable,'swConnUnitC3DiscardDueToTXTimeout':swConnUnitC3DiscardDueToTXTimeout,'swConnUnitC3DiscardOther':swConnUnitC3DiscardOther,'swConnUnitPCSErrorCounter':swConnUnitPCSErrorCounter,'swConnUnitUnroutableFrameCounter':swConnUnitUnroutableFrameCounter,'swConnUnitFECCorrectedCounter':swConnUnitFECCorrectedCounter,'swConnUnitFECUnCorrectedCounter':swConnUnitFECUnCorrectedCounter,'sw28k':sw28k,'sw21kN24k':sw21kN24k,'sw20x0':sw20x0,'swMibModule':swMibModule})