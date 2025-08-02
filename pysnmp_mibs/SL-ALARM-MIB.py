_N='read-write'
_M='Integer32'
_L='slAlarmTimeStamp'
_K='slAlarmText'
_J='slAlarmActive'
_I='slAlarmServiceAffect'
_H='slAlarmSeverity'
_G='slmTrapLogId'
_F='SL-MAIN-MIB'
_E='slAlarmType'
_D='slAlarmIfIndex'
_C='read-only'
_B='current'
_A='SL-ALARM-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
PerfCurrentCount,PerfIntervalCount,PerfTotalCount=mibBuilder.importSymbols('PerfHist-TC-MIB','PerfCurrentCount','PerfIntervalCount','PerfTotalCount')
slMain,slmTrapLogId=mibBuilder.importSymbols(_F,'slMain',_G)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_M,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeStamp','TruthValue')
slAlarmMib=ModuleIdentity((1,3,6,1,4,1,4515,1,3,20))
class SlAlarmType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,21,22,23,24,25,26,27,101,102,103,104,105,106,107,108,151,152,201,202,203,204,221,222,223,301,302,303,304,306,307,311,312,313,314,315,351,352,353,354,401,403,404,406,407,408,409,410,411,412,451,452,453,454,455,456,470,471,472,475,476,477,501,502,503,602,603,604,606,608,621,622,623,624,625,701,702,703,704,705,706,707,708,709,710,711,712,713,714,720,721,726,727,728,729,730,731,732,733,734,735,736,737,750,751,752,753,754,755,756,757,758,759,780,781,782,783,784,785,786,787,788,801,803,804,806,807,808,820,821,902,903,904,905,906,907,908,909,910,1001,1002,1003,1004)));namedValues=NamedValues(*(('losSonetAlarm',1),('lofSonetAlarm',2),('lopSonetAlarm',3),('aisLineSonetAlarm',4),('rfiLineSonetAlarm',5),('uneqSonetAlarm',6),('timLine',7),('slm',8),('sd',9),('sf',10),('hwfail',11),('aisPathSonetAlarm',12),('rfiPathSonetAlarm',13),('timPath',14),('uplinkTransmitMismatch',15),('uplinkClockSourceLol',16),('aisVtSonetAlarm',21),('lopVtSonetAlarm',22),('rfiVtSonetAlarm',23),('timVt',24),('slmVt',25),('uneqVtSonetAlarm',26),('lomVt',27),('vcgFarLossClientSignal',101),('vcgFarLossClientSync',102),('vcgLossAlignment',103),('vcgLossMultiframe',104),('vcgLossSequence',105),('vcgGfpLossSync',106),('vcgFarGfpLossSync',107),('vcgBadGidMember',108),('provUnequipped',151),('provMismatch',152),('ethConfigTransmitFault',201),('ethConfigLossOfSignal',202),('ethConfigLinkFail',203),('ethConfigPcsLossSync',204),('encAisFault',221),('encRdiFault',222),('encKeyExchangeFailed',223),('fcBxPortTransmitFault',301),('fcBxPortLossOfSignal',302),('fcBxPortNoLink',303),('fcBxPortLossOfSync',304),('fcBxPortTransmitMismatch',306),('fcBxPortPcsLossSync',307),('fcipLinkNoLink',311),('fcipLinkLossOfSync',312),('fcipSntpFailure',313),('fcipIpsecFailure',314),('fcipFarLossOfClient',315),('esconPortTransmitFault',351),('esconPortLossOfSignal',352),('esconPortNoLink',353),('esconPortLossOfSync',354),('edfaPumpTemperuture',401),('edfaHwFail',403),('edfaRvcSignalDetect',404),('edfaRcvPower',406),('edfaTemprature',407),('edfaEyeSafty',408),('edafGainFlatness',409),('edfaXmtPower',410),('edfaGain',411),('edfaEol',412),('muxAisPath',451),('muxLof',452),('muxRdi',453),('muxInbandFail',454),('muxTempLicense',455),('muxNoLicense',456),('oswHwFail',470),('oswLossOfSignal',471),('oswEdfaLossProp',472),('dcmTemp',475),('dcmTec',476),('dcmHwFault',477),('loopback',501),('apsForceActive',502),('apsManualActive',503),('cluHoldoverState',602),('cluFreerunState',603),('cluBelowLevel',604),('cluFail',606),('cluJittered',608),('channelLowDegrade',621),('channelHighDegrade',622),('channelLowFail',623),('channelHighFail',624),('unequalizedOuputPower',625),('sfpTransmitFault',701),('sfpRemoved',702),('sfpMuxWlMismatch',703),('sfpBitRateMismatch',704),('sfpLossOfLock',705),('sfpSfpWlMismatch',706),('sfpLossOfLight',707),('sfpLaserEndOfLife',708),('sfpMuxSpacingMismatch',709),('sfpHardwareFault',710),('sfpBlocked',711),('sfpLossPropagation',712),('sfpUnknownType',713),('sfpTxLossOfLock',714),('sfpHighTemp',720),('sfpLowTemp',721),('sfpHighTxPower',726),('sfpLowTxPower',727),('sfpHighRxPower',728),('sfpLowRxPower',729),('sfpHighLaserTemp',730),('sfpLowLaserTemp',731),('sfpHighLaserWl',732),('sfpLowLaserWl',733),('xfpTxNR',734),('xfpTxCdrNotLocked',735),('xfpRxNR',736),('xfpRxCdrNotLocked',737),('otnFecExc',750),('otnFecDeg',751),('otnOtuDeg',752),('otnOduDeg',753),('otnLos',754),('otnLof',755),('otnLom',756),('otuAis',757),('otuBdi',758),('otuTtim',759),('oduAis',780),('oduOci',781),('oduLck',782),('oduBdi',783),('oduTtim',784),('oduPtm',785),('oduApsMismatch',786),('otnOtuFail',787),('otnOduFail',788),('entityRemoved',801),('entityClockFail',803),('entityHwTxFail',804),('entitySwMismatch',806),('entitySwUpgrade',807),('entitySwInvalidBank',808),('entityIpLanPending',820),('entityIpOscPending',821),('nePowerFault',902),('neFanFault',903),('neLowVoltagePower',904),('entitySwUpgradeFail',905),('entityRadiusPrimFail',906),('entityRadiusSecFail',907),('entityDbRestoreFail',908),('entityDbRestoreInProgress',909),('entitySntpFail',910),('dcActive',1001),('lcpDown',1002),('ncpDown',1003),('rtcFailure',1004)))
_SlAlarmConfig_ObjectIdentity=ObjectIdentity
slAlarmConfig=_SlAlarmConfig_ObjectIdentity((1,3,6,1,4,1,4515,1,3,20,1))
_SlAlarmConfigTable_Object=MibTable
slAlarmConfigTable=_SlAlarmConfigTable_Object((1,3,6,1,4,1,4515,1,3,20,1,1))
if mibBuilder.loadTexts:slAlarmConfigTable.setStatus(_B)
_SlAlarmConfigEntry_Object=MibTableRow
slAlarmConfigEntry=_SlAlarmConfigEntry_Object((1,3,6,1,4,1,4515,1,3,20,1,1,1))
slAlarmConfigEntry.setIndexNames((0,_A,_D),(0,_A,_E))
if mibBuilder.loadTexts:slAlarmConfigEntry.setStatus(_B)
_SlAlarmIfIndex_Type=InterfaceIndex
_SlAlarmIfIndex_Object=MibTableColumn
slAlarmIfIndex=_SlAlarmIfIndex_Object((1,3,6,1,4,1,4515,1,3,20,1,1,1,1),_SlAlarmIfIndex_Type())
slAlarmIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:slAlarmIfIndex.setStatus(_B)
_SlAlarmType_Type=SlAlarmType
_SlAlarmType_Object=MibTableColumn
slAlarmType=_SlAlarmType_Object((1,3,6,1,4,1,4515,1,3,20,1,1,1,2),_SlAlarmType_Type())
slAlarmType.setMaxAccess(_C)
if mibBuilder.loadTexts:slAlarmType.setStatus(_B)
class _SlAlarmSeverity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('noAlarm',0),('critical',1),('major',2),('minor',3),('cleared',4),('notification',5)))
_SlAlarmSeverity_Type.__name__=_M
_SlAlarmSeverity_Object=MibTableColumn
slAlarmSeverity=_SlAlarmSeverity_Object((1,3,6,1,4,1,4515,1,3,20,1,1,1,3),_SlAlarmSeverity_Type())
slAlarmSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:slAlarmSeverity.setStatus(_B)
_SlAlarmServiceAffect_Type=TruthValue
_SlAlarmServiceAffect_Object=MibTableColumn
slAlarmServiceAffect=_SlAlarmServiceAffect_Object((1,3,6,1,4,1,4515,1,3,20,1,1,1,4),_SlAlarmServiceAffect_Type())
slAlarmServiceAffect.setMaxAccess(_C)
if mibBuilder.loadTexts:slAlarmServiceAffect.setStatus(_B)
_SlAlarmTimeStamp_Type=TimeStamp
_SlAlarmTimeStamp_Object=MibTableColumn
slAlarmTimeStamp=_SlAlarmTimeStamp_Object((1,3,6,1,4,1,4515,1,3,20,1,1,1,5),_SlAlarmTimeStamp_Type())
slAlarmTimeStamp.setMaxAccess(_C)
if mibBuilder.loadTexts:slAlarmTimeStamp.setStatus(_B)
_SlAlarmAcknowledged_Type=TruthValue
_SlAlarmAcknowledged_Object=MibTableColumn
slAlarmAcknowledged=_SlAlarmAcknowledged_Object((1,3,6,1,4,1,4515,1,3,20,1,1,1,6),_SlAlarmAcknowledged_Type())
slAlarmAcknowledged.setMaxAccess(_N)
if mibBuilder.loadTexts:slAlarmAcknowledged.setStatus(_B)
_SlAlarmAckUser_Type=DisplayString
_SlAlarmAckUser_Object=MibTableColumn
slAlarmAckUser=_SlAlarmAckUser_Object((1,3,6,1,4,1,4515,1,3,20,1,1,1,7),_SlAlarmAckUser_Type())
slAlarmAckUser.setMaxAccess(_N)
if mibBuilder.loadTexts:slAlarmAckUser.setStatus(_B)
_SlAlarmText_Type=DisplayString
_SlAlarmText_Object=MibTableColumn
slAlarmText=_SlAlarmText_Object((1,3,6,1,4,1,4515,1,3,20,1,1,1,8),_SlAlarmText_Type())
slAlarmText.setMaxAccess(_C)
if mibBuilder.loadTexts:slAlarmText.setStatus(_B)
_SlAlarmTraps_ObjectIdentity=ObjectIdentity
slAlarmTraps=_SlAlarmTraps_ObjectIdentity((1,3,6,1,4,1,4515,1,3,20,2))
_SlAlarmTraps0_ObjectIdentity=ObjectIdentity
slAlarmTraps0=_SlAlarmTraps0_ObjectIdentity((1,3,6,1,4,1,4515,1,3,20,2,0))
_SlAlarmActive_Type=TruthValue
_SlAlarmActive_Object=MibScalar
slAlarmActive=_SlAlarmActive_Object((1,3,6,1,4,1,4515,1,3,20,2,1),_SlAlarmActive_Type())
slAlarmActive.setMaxAccess(_C)
if mibBuilder.loadTexts:slAlarmActive.setStatus(_B)
slAlarmTrap0=NotificationType((1,3,6,1,4,1,4515,1,3,20,2,0,2))
slAlarmTrap0.setObjects(*((_A,_D),(_A,_E),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_F,_G)))
if mibBuilder.loadTexts:slAlarmTrap0.setStatus(_B)
slAlarmTrap=NotificationType((1,3,6,1,4,1,4515,1,3,20,2,2))
slAlarmTrap.setObjects(*((_A,_D),(_A,_E),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_F,_G)))
if mibBuilder.loadTexts:slAlarmTrap.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'SlAlarmType':SlAlarmType,'slAlarmMib':slAlarmMib,'slAlarmConfig':slAlarmConfig,'slAlarmConfigTable':slAlarmConfigTable,'slAlarmConfigEntry':slAlarmConfigEntry,_D:slAlarmIfIndex,_E:slAlarmType,_H:slAlarmSeverity,_I:slAlarmServiceAffect,_L:slAlarmTimeStamp,'slAlarmAcknowledged':slAlarmAcknowledged,'slAlarmAckUser':slAlarmAckUser,_K:slAlarmText,'slAlarmTraps':slAlarmTraps,'slAlarmTraps0':slAlarmTraps0,'slAlarmTrap0':slAlarmTrap0,_J:slAlarmActive,'slAlarmTrap':slAlarmTrap})