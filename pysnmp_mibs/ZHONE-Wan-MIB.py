_Z='zhoneLineStatusLastChange'
_Y='zhoneLineStatus'
_X='zhoneDs1ChannelNumber'
_W='zhoneFarEndTotalIndex'
_V='zhoneFarEndIntervalNumber'
_U='zhoneFarEndIntervalIndex'
_T='zhoneFarEndCurrentIndex'
_S='zhoneTotalIndex'
_R='zhoneIntervalNumber'
_Q='zhoneIntervalIndex'
_P='zhoneCurrentIndex'
_O='enabled'
_N='zhoneLineIndex'
_M='TruthValue'
_L='ifIndex'
_K='ifAlias'
_J='zhoneBertIndex'
_I='disabled'
_H='IF-MIB'
_G='other'
_F='not-accessible'
_E='ZHONE-Wan-MIB'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,ifAlias,ifIndex=mibBuilder.importSymbols(_H,'InterfaceIndex',_K,_L)
PerfCurrentCount,PerfIntervalCount,PerfTotalCount=mibBuilder.importSymbols('PerfHist-TC-MIB','PerfCurrentCount','PerfIntervalCount','PerfTotalCount')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeStamp',_M)
zhoneDsx,=mibBuilder.importSymbols('Zhone','zhoneDsx')
ZhoneAdminString,=mibBuilder.importSymbols('Zhone-TC','ZhoneAdminString')
zhoneDs1Mib=ModuleIdentity((1,3,6,1,4,1,5504,5,2,1))
if mibBuilder.loadTexts:zhoneDs1Mib.setRevisions(('2009-07-23 11:15','2009-05-12 07:38','2008-11-10 08:58','2006-05-12 12:46','2004-02-05 11:47','2004-01-21 15:36','2003-05-15 13:15','2003-02-04 13:12','2001-10-22 10:04','2001-08-22 13:50','2001-08-14 16:24','2001-08-09 10:07','2001-01-18 13:28','2001-01-04 11:19','2000-11-13 11:30','2000-09-21 10:27','2000-09-12 13:59'))
_ZhoneDs1Table_Object=MibTable
zhoneDs1Table=_ZhoneDs1Table_Object((1,3,6,1,4,1,5504,5,2,2))
if mibBuilder.loadTexts:zhoneDs1Table.setStatus(_A)
_ZhoneDs1Entry_Object=MibTableRow
zhoneDs1Entry=_ZhoneDs1Entry_Object((1,3,6,1,4,1,5504,5,2,2,1))
zhoneDs1Entry.setIndexNames((0,_E,_N))
if mibBuilder.loadTexts:zhoneDs1Entry.setStatus(_A)
_ZhoneLineIndex_Type=InterfaceIndex
_ZhoneLineIndex_Object=MibTableColumn
zhoneLineIndex=_ZhoneLineIndex_Object((1,3,6,1,4,1,5504,5,2,2,1,1),_ZhoneLineIndex_Type())
zhoneLineIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:zhoneLineIndex.setStatus(_A)
class _ZhoneTimeElapsed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,899))
_ZhoneTimeElapsed_Type.__name__=_C
_ZhoneTimeElapsed_Object=MibTableColumn
zhoneTimeElapsed=_ZhoneTimeElapsed_Object((1,3,6,1,4,1,5504,5,2,2,1,2),_ZhoneTimeElapsed_Type())
zhoneTimeElapsed.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneTimeElapsed.setStatus(_A)
class _ZhoneValidIntervals_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,96))
_ZhoneValidIntervals_Type.__name__=_C
_ZhoneValidIntervals_Object=MibTableColumn
zhoneValidIntervals=_ZhoneValidIntervals_Object((1,3,6,1,4,1,5504,5,2,2,1,3),_ZhoneValidIntervals_Type())
zhoneValidIntervals.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneValidIntervals.setStatus(_A)
class _ZhoneLineType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_G,1),('esf',2),('d4',3),('slc96',4),('e1',5),('e1Crc',6),('e1Mf',7),('e1CrcMf',8),('e1Unframed',9),('ds1Unframed',10)))
_ZhoneLineType_Type.__name__=_C
_ZhoneLineType_Object=MibTableColumn
zhoneLineType=_ZhoneLineType_Object((1,3,6,1,4,1,5504,5,2,2,1,4),_ZhoneLineType_Type())
zhoneLineType.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneLineType.setStatus(_A)
class _ZhoneLineCoding_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('jbzs',1),('b8zs',2),('hdb3',3),('zbtsi',4),('ami',5),(_G,6),('b6zs',7)))
_ZhoneLineCoding_Type.__name__=_C
_ZhoneLineCoding_Object=MibTableColumn
zhoneLineCoding=_ZhoneLineCoding_Object((1,3,6,1,4,1,5504,5,2,2,1,5),_ZhoneLineCoding_Type())
zhoneLineCoding.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneLineCoding.setStatus(_A)
class _ZhoneSendCode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19)));namedValues=NamedValues(*(('sendNoCode',1),('sendLineCode',2),('sendPayloadCode',3),('sendResetCode',4),('sendQRSSPattern',5),('send511Pattern',6),('send3in24Pattern',7),('sendOtherTestPattern',8),('send2047Pattern',9),('send1in2Pattern',10),('sendInbandCode',11),('sendInbandCodeOff',12),('sendLineCodeOff',13),('sendPayloadCodeOff',14),('send2ToPower9Minus1Pattern',15),('send2ToPower11Minus1Pattern',16),('send2ToPower15Minus1Pattern',17),('send2ToPower20Minus1Pattern',18),('send2ToPower23Minus1Pattern',19)))
_ZhoneSendCode_Type.__name__=_C
_ZhoneSendCode_Object=MibTableColumn
zhoneSendCode=_ZhoneSendCode_Object((1,3,6,1,4,1,5504,5,2,2,1,6),_ZhoneSendCode_Type())
zhoneSendCode.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneSendCode.setStatus(_A)
_ZhoneCircuitIdentifier_Type=ZhoneAdminString
_ZhoneCircuitIdentifier_Object=MibTableColumn
zhoneCircuitIdentifier=_ZhoneCircuitIdentifier_Object((1,3,6,1,4,1,5504,5,2,2,1,7),_ZhoneCircuitIdentifier_Type())
zhoneCircuitIdentifier.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneCircuitIdentifier.setStatus(_A)
class _ZhoneLoopbackConfig_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('noLoop',1),('lineLoop',2),('localLoop',3),('payloadLoop',4)))
_ZhoneLoopbackConfig_Type.__name__=_C
_ZhoneLoopbackConfig_Object=MibTableColumn
zhoneLoopbackConfig=_ZhoneLoopbackConfig_Object((1,3,6,1,4,1,5504,5,2,2,1,8),_ZhoneLoopbackConfig_Type())
zhoneLoopbackConfig.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneLoopbackConfig.setStatus(_A)
class _ZhoneLineStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65536))
_ZhoneLineStatus_Type.__name__=_C
_ZhoneLineStatus_Object=MibTableColumn
zhoneLineStatus=_ZhoneLineStatus_Object((1,3,6,1,4,1,5504,5,2,2,1,9),_ZhoneLineStatus_Type())
zhoneLineStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneLineStatus.setStatus(_A)
class _ZhoneSignalMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('none',1),('robbedBit',2),('bitOriented',3),('messageOriented',4),(_G,5)))
_ZhoneSignalMode_Type.__name__=_C
_ZhoneSignalMode_Object=MibTableColumn
zhoneSignalMode=_ZhoneSignalMode_Object((1,3,6,1,4,1,5504,5,2,2,1,10),_ZhoneSignalMode_Type())
zhoneSignalMode.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneSignalMode.setStatus(_A)
class _ZhoneTransmitClockSource_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('loopTiming',1),('localTiming',2),('throughTiming',3),('sonetThroughTiming',4)))
_ZhoneTransmitClockSource_Type.__name__=_C
_ZhoneTransmitClockSource_Object=MibTableColumn
zhoneTransmitClockSource=_ZhoneTransmitClockSource_Object((1,3,6,1,4,1,5504,5,2,2,1,11),_ZhoneTransmitClockSource_Type())
zhoneTransmitClockSource.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneTransmitClockSource.setStatus(_A)
class _ZhoneFdl_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),('ansiT1403',2),('att54016',3),('fdlNone',4)))
_ZhoneFdl_Type.__name__=_C
_ZhoneFdl_Object=MibTableColumn
zhoneFdl=_ZhoneFdl_Object((1,3,6,1,4,1,5504,5,2,2,1,12),_ZhoneFdl_Type())
zhoneFdl.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneFdl.setStatus(_A)
class _ZhoneInvalidIntervals_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,96))
_ZhoneInvalidIntervals_Type.__name__=_C
_ZhoneInvalidIntervals_Object=MibTableColumn
zhoneInvalidIntervals=_ZhoneInvalidIntervals_Object((1,3,6,1,4,1,5504,5,2,2,1,13),_ZhoneInvalidIntervals_Type())
zhoneInvalidIntervals.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneInvalidIntervals.setStatus(_A)
class _ZhoneDsxLineLength_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('dsx0',1),('dsx133',2),('dsx266',3),('dsx399',4),('dsx533',5),('dsx655',6)))
_ZhoneDsxLineLength_Type.__name__=_C
_ZhoneDsxLineLength_Object=MibTableColumn
zhoneDsxLineLength=_ZhoneDsxLineLength_Object((1,3,6,1,4,1,5504,5,2,2,1,14),_ZhoneDsxLineLength_Type())
zhoneDsxLineLength.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneDsxLineLength.setStatus(_A)
_ZhoneLineStatusLastChange_Type=TimeStamp
_ZhoneLineStatusLastChange_Object=MibTableColumn
zhoneLineStatusLastChange=_ZhoneLineStatusLastChange_Object((1,3,6,1,4,1,5504,5,2,2,1,15),_ZhoneLineStatusLastChange_Type())
zhoneLineStatusLastChange.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneLineStatusLastChange.setStatus(_A)
class _ZhoneLineStatusChangeTrapEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_O,1),(_I,2)))
_ZhoneLineStatusChangeTrapEnable_Type.__name__=_C
_ZhoneLineStatusChangeTrapEnable_Object=MibTableColumn
zhoneLineStatusChangeTrapEnable=_ZhoneLineStatusChangeTrapEnable_Object((1,3,6,1,4,1,5504,5,2,2,1,16),_ZhoneLineStatusChangeTrapEnable_Type())
zhoneLineStatusChangeTrapEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneLineStatusChangeTrapEnable.setStatus(_A)
class _ZhoneLoopbackStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,127))
_ZhoneLoopbackStatus_Type.__name__=_C
_ZhoneLoopbackStatus_Object=MibTableColumn
zhoneLoopbackStatus=_ZhoneLoopbackStatus_Object((1,3,6,1,4,1,5504,5,2,2,1,17),_ZhoneLoopbackStatus_Type())
zhoneLoopbackStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneLoopbackStatus.setStatus(_A)
class _ZhoneDs1ChannelNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,28))
_ZhoneDs1ChannelNumber_Type.__name__=_C
_ZhoneDs1ChannelNumber_Object=MibTableColumn
zhoneDs1ChannelNumber=_ZhoneDs1ChannelNumber_Object((1,3,6,1,4,1,5504,5,2,2,1,18),_ZhoneDs1ChannelNumber_Type())
zhoneDs1ChannelNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneDs1ChannelNumber.setStatus(_A)
class _ZhoneChannelization_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),('enabledDs0',2),('enabledDs1',3)))
_ZhoneChannelization_Type.__name__=_C
_ZhoneChannelization_Object=MibTableColumn
zhoneChannelization=_ZhoneChannelization_Object((1,3,6,1,4,1,5504,5,2,2,1,19),_ZhoneChannelization_Type())
zhoneChannelization.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneChannelization.setStatus(_A)
class _ZhoneDs1Mode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),('dsx',2),('csu',3)))
_ZhoneDs1Mode_Type.__name__=_C
_ZhoneDs1Mode_Object=MibTableColumn
zhoneDs1Mode=_ZhoneDs1Mode_Object((1,3,6,1,4,1,5504,5,2,2,1,20),_ZhoneDs1Mode_Type())
zhoneDs1Mode.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneDs1Mode.setStatus(_A)
class _ZhoneCsuLineLength_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('csu00',1),('csu75',2),('csu150',3),('csu225',4)))
_ZhoneCsuLineLength_Type.__name__=_C
_ZhoneCsuLineLength_Object=MibTableColumn
zhoneCsuLineLength=_ZhoneCsuLineLength_Object((1,3,6,1,4,1,5504,5,2,2,1,21),_ZhoneCsuLineLength_Type())
zhoneCsuLineLength.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneCsuLineLength.setStatus(_A)
class _ZhoneClockSourceEligibility_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('notEligible',1),('eligible',2)))
_ZhoneClockSourceEligibility_Type.__name__=_C
_ZhoneClockSourceEligibility_Object=MibTableColumn
zhoneClockSourceEligibility=_ZhoneClockSourceEligibility_Object((1,3,6,1,4,1,5504,5,2,2,1,22),_ZhoneClockSourceEligibility_Type())
zhoneClockSourceEligibility.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneClockSourceEligibility.setStatus(_A)
class _ZhoneCellScramble_Type(TruthValue):defaultValue=1
_ZhoneCellScramble_Type.__name__=_M
_ZhoneCellScramble_Object=MibTableColumn
zhoneCellScramble=_ZhoneCellScramble_Object((1,3,6,1,4,1,5504,5,2,2,1,23),_ZhoneCellScramble_Type())
zhoneCellScramble.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneCellScramble.setStatus(_A)
_ZhoneCosetPolynomial_Type=TruthValue
_ZhoneCosetPolynomial_Object=MibTableColumn
zhoneCosetPolynomial=_ZhoneCosetPolynomial_Object((1,3,6,1,4,1,5504,5,2,2,1,24),_ZhoneCosetPolynomial_Type())
zhoneCosetPolynomial.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneCosetPolynomial.setStatus(_A)
class _ZhoneDs1ProtocolEmulation_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('network',1),('cpe',2)))
_ZhoneDs1ProtocolEmulation_Type.__name__=_C
_ZhoneDs1ProtocolEmulation_Object=MibTableColumn
zhoneDs1ProtocolEmulation=_ZhoneDs1ProtocolEmulation_Object((1,3,6,1,4,1,5504,5,2,2,1,25),_ZhoneDs1ProtocolEmulation_Type())
zhoneDs1ProtocolEmulation.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneDs1ProtocolEmulation.setStatus(_A)
class _ZhoneDs1SignalType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('loopStart',1),('groundStart',2)))
_ZhoneDs1SignalType_Type.__name__=_C
_ZhoneDs1SignalType_Object=MibTableColumn
zhoneDs1SignalType=_ZhoneDs1SignalType_Object((1,3,6,1,4,1,5504,5,2,2,1,26),_ZhoneDs1SignalType_Type())
zhoneDs1SignalType.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneDs1SignalType.setStatus(_A)
class _ZhoneDs1GroupIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_ZhoneDs1GroupIndex_Type.__name__=_C
_ZhoneDs1GroupIndex_Object=MibTableColumn
zhoneDs1GroupIndex=_ZhoneDs1GroupIndex_Object((1,3,6,1,4,1,5504,5,2,2,1,27),_ZhoneDs1GroupIndex_Type())
zhoneDs1GroupIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneDs1GroupIndex.setStatus(_A)
class _ZhoneDs1LinePower_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_O,1),(_I,2)))
_ZhoneDs1LinePower_Type.__name__=_C
_ZhoneDs1LinePower_Object=MibTableColumn
zhoneDs1LinePower=_ZhoneDs1LinePower_Object((1,3,6,1,4,1,5504,5,2,2,1,28),_ZhoneDs1LinePower_Type())
zhoneDs1LinePower.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneDs1LinePower.setStatus(_A)
class _ZhoneDs1TimeslotAssignment_Type(Bits):namedValues=NamedValues(*(('ts0',0),('ts1',1),('ts2',2),('ts3',3),('ts4',4),('ts5',5),('ts6',6),('ts7',7),('ts8',8),('ts9',9),('ts10',10),('ts11',11),('ts12',12),('ts13',13),('ts14',14),('ts15',15),('ts16',16),('ts17',17),('ts18',18),('ts19',19),('ts20',20),('ts21',21),('ts22',22),('ts23',23),('ts24',24),('ts25',25),('ts26',26),('ts27',27),('ts28',28),('ts29',29),('ts30',30),('ts31',31)))
_ZhoneDs1TimeslotAssignment_Type.__name__='Bits'
_ZhoneDs1TimeslotAssignment_Object=MibTableColumn
zhoneDs1TimeslotAssignment=_ZhoneDs1TimeslotAssignment_Object((1,3,6,1,4,1,5504,5,2,2,1,29),_ZhoneDs1TimeslotAssignment_Type())
zhoneDs1TimeslotAssignment.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneDs1TimeslotAssignment.setStatus(_A)
class _ZhoneDs1TxClockRecovery_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('adaptive',2),('differential',3)))
_ZhoneDs1TxClockRecovery_Type.__name__=_C
_ZhoneDs1TxClockRecovery_Object=MibTableColumn
zhoneDs1TxClockRecovery=_ZhoneDs1TxClockRecovery_Object((1,3,6,1,4,1,5504,5,2,2,1,30),_ZhoneDs1TxClockRecovery_Type())
zhoneDs1TxClockRecovery.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneDs1TxClockRecovery.setStatus('obsolete')
class _ZhoneDs1TxClockAdaptiveQuality_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('stratum1',1),('stratum3',2),('stratum3e',3),('stratum4',4)))
_ZhoneDs1TxClockAdaptiveQuality_Type.__name__=_C
_ZhoneDs1TxClockAdaptiveQuality_Object=MibTableColumn
zhoneDs1TxClockAdaptiveQuality=_ZhoneDs1TxClockAdaptiveQuality_Object((1,3,6,1,4,1,5504,5,2,2,1,31),_ZhoneDs1TxClockAdaptiveQuality_Type())
zhoneDs1TxClockAdaptiveQuality.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneDs1TxClockAdaptiveQuality.setStatus(_A)
_ZhoneDs1CurrentTable_Object=MibTable
zhoneDs1CurrentTable=_ZhoneDs1CurrentTable_Object((1,3,6,1,4,1,5504,5,2,3))
if mibBuilder.loadTexts:zhoneDs1CurrentTable.setStatus(_A)
_ZhoneDs1CurrentEntry_Object=MibTableRow
zhoneDs1CurrentEntry=_ZhoneDs1CurrentEntry_Object((1,3,6,1,4,1,5504,5,2,3,1))
zhoneDs1CurrentEntry.setIndexNames((0,_E,_P))
if mibBuilder.loadTexts:zhoneDs1CurrentEntry.setStatus(_A)
_ZhoneCurrentIndex_Type=InterfaceIndex
_ZhoneCurrentIndex_Object=MibTableColumn
zhoneCurrentIndex=_ZhoneCurrentIndex_Object((1,3,6,1,4,1,5504,5,2,3,1,1),_ZhoneCurrentIndex_Type())
zhoneCurrentIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:zhoneCurrentIndex.setStatus(_A)
_ZhoneCurrentESs_Type=PerfCurrentCount
_ZhoneCurrentESs_Object=MibTableColumn
zhoneCurrentESs=_ZhoneCurrentESs_Object((1,3,6,1,4,1,5504,5,2,3,1,2),_ZhoneCurrentESs_Type())
zhoneCurrentESs.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneCurrentESs.setStatus(_A)
_ZhoneCurrentSESs_Type=PerfCurrentCount
_ZhoneCurrentSESs_Object=MibTableColumn
zhoneCurrentSESs=_ZhoneCurrentSESs_Object((1,3,6,1,4,1,5504,5,2,3,1,3),_ZhoneCurrentSESs_Type())
zhoneCurrentSESs.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneCurrentSESs.setStatus(_A)
_ZhoneCurrentSEFSs_Type=PerfCurrentCount
_ZhoneCurrentSEFSs_Object=MibTableColumn
zhoneCurrentSEFSs=_ZhoneCurrentSEFSs_Object((1,3,6,1,4,1,5504,5,2,3,1,4),_ZhoneCurrentSEFSs_Type())
zhoneCurrentSEFSs.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneCurrentSEFSs.setStatus(_A)
_ZhoneCurrentUASs_Type=PerfCurrentCount
_ZhoneCurrentUASs_Object=MibTableColumn
zhoneCurrentUASs=_ZhoneCurrentUASs_Object((1,3,6,1,4,1,5504,5,2,3,1,5),_ZhoneCurrentUASs_Type())
zhoneCurrentUASs.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneCurrentUASs.setStatus(_A)
_ZhoneCurrentCSSs_Type=PerfCurrentCount
_ZhoneCurrentCSSs_Object=MibTableColumn
zhoneCurrentCSSs=_ZhoneCurrentCSSs_Object((1,3,6,1,4,1,5504,5,2,3,1,6),_ZhoneCurrentCSSs_Type())
zhoneCurrentCSSs.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneCurrentCSSs.setStatus(_A)
_ZhoneCurrentPCVs_Type=PerfCurrentCount
_ZhoneCurrentPCVs_Object=MibTableColumn
zhoneCurrentPCVs=_ZhoneCurrentPCVs_Object((1,3,6,1,4,1,5504,5,2,3,1,7),_ZhoneCurrentPCVs_Type())
zhoneCurrentPCVs.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneCurrentPCVs.setStatus(_A)
_ZhoneCurrentLESs_Type=PerfCurrentCount
_ZhoneCurrentLESs_Object=MibTableColumn
zhoneCurrentLESs=_ZhoneCurrentLESs_Object((1,3,6,1,4,1,5504,5,2,3,1,8),_ZhoneCurrentLESs_Type())
zhoneCurrentLESs.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneCurrentLESs.setStatus(_A)
_ZhoneCurrentBESs_Type=PerfCurrentCount
_ZhoneCurrentBESs_Object=MibTableColumn
zhoneCurrentBESs=_ZhoneCurrentBESs_Object((1,3,6,1,4,1,5504,5,2,3,1,9),_ZhoneCurrentBESs_Type())
zhoneCurrentBESs.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneCurrentBESs.setStatus(_A)
_ZhoneCurrentDMs_Type=PerfCurrentCount
_ZhoneCurrentDMs_Object=MibTableColumn
zhoneCurrentDMs=_ZhoneCurrentDMs_Object((1,3,6,1,4,1,5504,5,2,3,1,10),_ZhoneCurrentDMs_Type())
zhoneCurrentDMs.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneCurrentDMs.setStatus(_A)
_ZhoneCurrentLCVs_Type=PerfCurrentCount
_ZhoneCurrentLCVs_Object=MibTableColumn
zhoneCurrentLCVs=_ZhoneCurrentLCVs_Object((1,3,6,1,4,1,5504,5,2,3,1,11),_ZhoneCurrentLCVs_Type())
zhoneCurrentLCVs.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneCurrentLCVs.setStatus(_A)
_ZhoneDs1IntervalTable_Object=MibTable
zhoneDs1IntervalTable=_ZhoneDs1IntervalTable_Object((1,3,6,1,4,1,5504,5,2,4))
if mibBuilder.loadTexts:zhoneDs1IntervalTable.setStatus(_A)
_ZhoneDs1IntervalEntry_Object=MibTableRow
zhoneDs1IntervalEntry=_ZhoneDs1IntervalEntry_Object((1,3,6,1,4,1,5504,5,2,4,1))
zhoneDs1IntervalEntry.setIndexNames((0,_E,_Q),(0,_E,_R))
if mibBuilder.loadTexts:zhoneDs1IntervalEntry.setStatus(_A)
_ZhoneIntervalIndex_Type=InterfaceIndex
_ZhoneIntervalIndex_Object=MibTableColumn
zhoneIntervalIndex=_ZhoneIntervalIndex_Object((1,3,6,1,4,1,5504,5,2,4,1,1),_ZhoneIntervalIndex_Type())
zhoneIntervalIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:zhoneIntervalIndex.setStatus(_A)
class _ZhoneIntervalNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,96))
_ZhoneIntervalNumber_Type.__name__=_C
_ZhoneIntervalNumber_Object=MibTableColumn
zhoneIntervalNumber=_ZhoneIntervalNumber_Object((1,3,6,1,4,1,5504,5,2,4,1,2),_ZhoneIntervalNumber_Type())
zhoneIntervalNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneIntervalNumber.setStatus(_A)
_ZhoneIntervalESs_Type=PerfIntervalCount
_ZhoneIntervalESs_Object=MibTableColumn
zhoneIntervalESs=_ZhoneIntervalESs_Object((1,3,6,1,4,1,5504,5,2,4,1,3),_ZhoneIntervalESs_Type())
zhoneIntervalESs.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneIntervalESs.setStatus(_A)
_ZhoneIntervalSESs_Type=PerfIntervalCount
_ZhoneIntervalSESs_Object=MibTableColumn
zhoneIntervalSESs=_ZhoneIntervalSESs_Object((1,3,6,1,4,1,5504,5,2,4,1,4),_ZhoneIntervalSESs_Type())
zhoneIntervalSESs.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneIntervalSESs.setStatus(_A)
_ZhoneIntervalSEFSs_Type=PerfIntervalCount
_ZhoneIntervalSEFSs_Object=MibTableColumn
zhoneIntervalSEFSs=_ZhoneIntervalSEFSs_Object((1,3,6,1,4,1,5504,5,2,4,1,5),_ZhoneIntervalSEFSs_Type())
zhoneIntervalSEFSs.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneIntervalSEFSs.setStatus(_A)
_ZhoneIntervalUASs_Type=PerfIntervalCount
_ZhoneIntervalUASs_Object=MibTableColumn
zhoneIntervalUASs=_ZhoneIntervalUASs_Object((1,3,6,1,4,1,5504,5,2,4,1,6),_ZhoneIntervalUASs_Type())
zhoneIntervalUASs.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneIntervalUASs.setStatus(_A)
_ZhoneIntervalCSSs_Type=PerfIntervalCount
_ZhoneIntervalCSSs_Object=MibTableColumn
zhoneIntervalCSSs=_ZhoneIntervalCSSs_Object((1,3,6,1,4,1,5504,5,2,4,1,7),_ZhoneIntervalCSSs_Type())
zhoneIntervalCSSs.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneIntervalCSSs.setStatus(_A)
_ZhoneIntervalPCVs_Type=PerfIntervalCount
_ZhoneIntervalPCVs_Object=MibTableColumn
zhoneIntervalPCVs=_ZhoneIntervalPCVs_Object((1,3,6,1,4,1,5504,5,2,4,1,8),_ZhoneIntervalPCVs_Type())
zhoneIntervalPCVs.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneIntervalPCVs.setStatus(_A)
_ZhoneIntervalLESs_Type=PerfIntervalCount
_ZhoneIntervalLESs_Object=MibTableColumn
zhoneIntervalLESs=_ZhoneIntervalLESs_Object((1,3,6,1,4,1,5504,5,2,4,1,9),_ZhoneIntervalLESs_Type())
zhoneIntervalLESs.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneIntervalLESs.setStatus(_A)
_ZhoneIntervalBESs_Type=PerfIntervalCount
_ZhoneIntervalBESs_Object=MibTableColumn
zhoneIntervalBESs=_ZhoneIntervalBESs_Object((1,3,6,1,4,1,5504,5,2,4,1,10),_ZhoneIntervalBESs_Type())
zhoneIntervalBESs.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneIntervalBESs.setStatus(_A)
_ZhoneIntervalDMs_Type=PerfIntervalCount
_ZhoneIntervalDMs_Object=MibTableColumn
zhoneIntervalDMs=_ZhoneIntervalDMs_Object((1,3,6,1,4,1,5504,5,2,4,1,11),_ZhoneIntervalDMs_Type())
zhoneIntervalDMs.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneIntervalDMs.setStatus(_A)
_ZhoneIntervalLCVs_Type=PerfIntervalCount
_ZhoneIntervalLCVs_Object=MibTableColumn
zhoneIntervalLCVs=_ZhoneIntervalLCVs_Object((1,3,6,1,4,1,5504,5,2,4,1,12),_ZhoneIntervalLCVs_Type())
zhoneIntervalLCVs.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneIntervalLCVs.setStatus(_A)
_ZhoneIntervalValidData_Type=TruthValue
_ZhoneIntervalValidData_Object=MibTableColumn
zhoneIntervalValidData=_ZhoneIntervalValidData_Object((1,3,6,1,4,1,5504,5,2,4,1,13),_ZhoneIntervalValidData_Type())
zhoneIntervalValidData.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneIntervalValidData.setStatus(_A)
_ZhoneDs1TotalTable_Object=MibTable
zhoneDs1TotalTable=_ZhoneDs1TotalTable_Object((1,3,6,1,4,1,5504,5,2,5))
if mibBuilder.loadTexts:zhoneDs1TotalTable.setStatus(_A)
_ZhoneDs1TotalEntry_Object=MibTableRow
zhoneDs1TotalEntry=_ZhoneDs1TotalEntry_Object((1,3,6,1,4,1,5504,5,2,5,1))
zhoneDs1TotalEntry.setIndexNames((0,_E,_S))
if mibBuilder.loadTexts:zhoneDs1TotalEntry.setStatus(_A)
_ZhoneTotalIndex_Type=InterfaceIndex
_ZhoneTotalIndex_Object=MibTableColumn
zhoneTotalIndex=_ZhoneTotalIndex_Object((1,3,6,1,4,1,5504,5,2,5,1,1),_ZhoneTotalIndex_Type())
zhoneTotalIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:zhoneTotalIndex.setStatus(_A)
_ZhoneTotalESs_Type=PerfTotalCount
_ZhoneTotalESs_Object=MibTableColumn
zhoneTotalESs=_ZhoneTotalESs_Object((1,3,6,1,4,1,5504,5,2,5,1,2),_ZhoneTotalESs_Type())
zhoneTotalESs.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneTotalESs.setStatus(_A)
_ZhoneTotalSESs_Type=PerfTotalCount
_ZhoneTotalSESs_Object=MibTableColumn
zhoneTotalSESs=_ZhoneTotalSESs_Object((1,3,6,1,4,1,5504,5,2,5,1,3),_ZhoneTotalSESs_Type())
zhoneTotalSESs.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneTotalSESs.setStatus(_A)
_ZhoneTotalSEFSs_Type=PerfTotalCount
_ZhoneTotalSEFSs_Object=MibTableColumn
zhoneTotalSEFSs=_ZhoneTotalSEFSs_Object((1,3,6,1,4,1,5504,5,2,5,1,4),_ZhoneTotalSEFSs_Type())
zhoneTotalSEFSs.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneTotalSEFSs.setStatus(_A)
_ZhoneTotalUASs_Type=PerfTotalCount
_ZhoneTotalUASs_Object=MibTableColumn
zhoneTotalUASs=_ZhoneTotalUASs_Object((1,3,6,1,4,1,5504,5,2,5,1,5),_ZhoneTotalUASs_Type())
zhoneTotalUASs.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneTotalUASs.setStatus(_A)
_ZhoneTotalCSSs_Type=PerfTotalCount
_ZhoneTotalCSSs_Object=MibTableColumn
zhoneTotalCSSs=_ZhoneTotalCSSs_Object((1,3,6,1,4,1,5504,5,2,5,1,6),_ZhoneTotalCSSs_Type())
zhoneTotalCSSs.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneTotalCSSs.setStatus(_A)
_ZhoneTotalPCVs_Type=PerfTotalCount
_ZhoneTotalPCVs_Object=MibTableColumn
zhoneTotalPCVs=_ZhoneTotalPCVs_Object((1,3,6,1,4,1,5504,5,2,5,1,7),_ZhoneTotalPCVs_Type())
zhoneTotalPCVs.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneTotalPCVs.setStatus(_A)
_ZhoneTotalLESs_Type=PerfTotalCount
_ZhoneTotalLESs_Object=MibTableColumn
zhoneTotalLESs=_ZhoneTotalLESs_Object((1,3,6,1,4,1,5504,5,2,5,1,8),_ZhoneTotalLESs_Type())
zhoneTotalLESs.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneTotalLESs.setStatus(_A)
_ZhoneTotalBESs_Type=PerfTotalCount
_ZhoneTotalBESs_Object=MibTableColumn
zhoneTotalBESs=_ZhoneTotalBESs_Object((1,3,6,1,4,1,5504,5,2,5,1,9),_ZhoneTotalBESs_Type())
zhoneTotalBESs.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneTotalBESs.setStatus(_A)
_ZhoneTotalDMs_Type=PerfTotalCount
_ZhoneTotalDMs_Object=MibTableColumn
zhoneTotalDMs=_ZhoneTotalDMs_Object((1,3,6,1,4,1,5504,5,2,5,1,10),_ZhoneTotalDMs_Type())
zhoneTotalDMs.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneTotalDMs.setStatus(_A)
_ZhoneTotalLCVs_Type=PerfTotalCount
_ZhoneTotalLCVs_Object=MibTableColumn
zhoneTotalLCVs=_ZhoneTotalLCVs_Object((1,3,6,1,4,1,5504,5,2,5,1,11),_ZhoneTotalLCVs_Type())
zhoneTotalLCVs.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneTotalLCVs.setStatus(_A)
_ZhoneDs1FarEndCurrentTable_Object=MibTable
zhoneDs1FarEndCurrentTable=_ZhoneDs1FarEndCurrentTable_Object((1,3,6,1,4,1,5504,5,2,6))
if mibBuilder.loadTexts:zhoneDs1FarEndCurrentTable.setStatus(_A)
_ZhoneDs1FarEndCurrentEntry_Object=MibTableRow
zhoneDs1FarEndCurrentEntry=_ZhoneDs1FarEndCurrentEntry_Object((1,3,6,1,4,1,5504,5,2,6,1))
zhoneDs1FarEndCurrentEntry.setIndexNames((0,_E,_T))
if mibBuilder.loadTexts:zhoneDs1FarEndCurrentEntry.setStatus(_A)
_ZhoneFarEndCurrentIndex_Type=InterfaceIndex
_ZhoneFarEndCurrentIndex_Object=MibTableColumn
zhoneFarEndCurrentIndex=_ZhoneFarEndCurrentIndex_Object((1,3,6,1,4,1,5504,5,2,6,1,1),_ZhoneFarEndCurrentIndex_Type())
zhoneFarEndCurrentIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:zhoneFarEndCurrentIndex.setStatus(_A)
class _ZhoneFarEndTimeElapsed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,899))
_ZhoneFarEndTimeElapsed_Type.__name__=_C
_ZhoneFarEndTimeElapsed_Object=MibTableColumn
zhoneFarEndTimeElapsed=_ZhoneFarEndTimeElapsed_Object((1,3,6,1,4,1,5504,5,2,6,1,2),_ZhoneFarEndTimeElapsed_Type())
zhoneFarEndTimeElapsed.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneFarEndTimeElapsed.setStatus(_A)
class _ZhoneFarEndValidIntervals_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,96))
_ZhoneFarEndValidIntervals_Type.__name__=_C
_ZhoneFarEndValidIntervals_Object=MibTableColumn
zhoneFarEndValidIntervals=_ZhoneFarEndValidIntervals_Object((1,3,6,1,4,1,5504,5,2,6,1,3),_ZhoneFarEndValidIntervals_Type())
zhoneFarEndValidIntervals.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneFarEndValidIntervals.setStatus(_A)
_ZhoneFarEndCurrentESs_Type=PerfCurrentCount
_ZhoneFarEndCurrentESs_Object=MibTableColumn
zhoneFarEndCurrentESs=_ZhoneFarEndCurrentESs_Object((1,3,6,1,4,1,5504,5,2,6,1,4),_ZhoneFarEndCurrentESs_Type())
zhoneFarEndCurrentESs.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneFarEndCurrentESs.setStatus(_A)
_ZhoneFarEndCurrentSESs_Type=PerfCurrentCount
_ZhoneFarEndCurrentSESs_Object=MibTableColumn
zhoneFarEndCurrentSESs=_ZhoneFarEndCurrentSESs_Object((1,3,6,1,4,1,5504,5,2,6,1,5),_ZhoneFarEndCurrentSESs_Type())
zhoneFarEndCurrentSESs.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneFarEndCurrentSESs.setStatus(_A)
_ZhoneFarEndCurrentSEFSs_Type=PerfCurrentCount
_ZhoneFarEndCurrentSEFSs_Object=MibTableColumn
zhoneFarEndCurrentSEFSs=_ZhoneFarEndCurrentSEFSs_Object((1,3,6,1,4,1,5504,5,2,6,1,6),_ZhoneFarEndCurrentSEFSs_Type())
zhoneFarEndCurrentSEFSs.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneFarEndCurrentSEFSs.setStatus(_A)
_ZhoneFarEndCurrentUASs_Type=PerfCurrentCount
_ZhoneFarEndCurrentUASs_Object=MibTableColumn
zhoneFarEndCurrentUASs=_ZhoneFarEndCurrentUASs_Object((1,3,6,1,4,1,5504,5,2,6,1,7),_ZhoneFarEndCurrentUASs_Type())
zhoneFarEndCurrentUASs.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneFarEndCurrentUASs.setStatus(_A)
_ZhoneFarEndCurrentCSSs_Type=PerfCurrentCount
_ZhoneFarEndCurrentCSSs_Object=MibTableColumn
zhoneFarEndCurrentCSSs=_ZhoneFarEndCurrentCSSs_Object((1,3,6,1,4,1,5504,5,2,6,1,8),_ZhoneFarEndCurrentCSSs_Type())
zhoneFarEndCurrentCSSs.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneFarEndCurrentCSSs.setStatus(_A)
_ZhoneFarEndCurrentLESs_Type=PerfCurrentCount
_ZhoneFarEndCurrentLESs_Object=MibTableColumn
zhoneFarEndCurrentLESs=_ZhoneFarEndCurrentLESs_Object((1,3,6,1,4,1,5504,5,2,6,1,9),_ZhoneFarEndCurrentLESs_Type())
zhoneFarEndCurrentLESs.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneFarEndCurrentLESs.setStatus(_A)
_ZhoneFarEndCurrentPCVs_Type=PerfCurrentCount
_ZhoneFarEndCurrentPCVs_Object=MibTableColumn
zhoneFarEndCurrentPCVs=_ZhoneFarEndCurrentPCVs_Object((1,3,6,1,4,1,5504,5,2,6,1,10),_ZhoneFarEndCurrentPCVs_Type())
zhoneFarEndCurrentPCVs.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneFarEndCurrentPCVs.setStatus(_A)
_ZhoneFarEndCurrentBESs_Type=PerfCurrentCount
_ZhoneFarEndCurrentBESs_Object=MibTableColumn
zhoneFarEndCurrentBESs=_ZhoneFarEndCurrentBESs_Object((1,3,6,1,4,1,5504,5,2,6,1,11),_ZhoneFarEndCurrentBESs_Type())
zhoneFarEndCurrentBESs.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneFarEndCurrentBESs.setStatus(_A)
_ZhoneFarEndCurrentDMs_Type=PerfCurrentCount
_ZhoneFarEndCurrentDMs_Object=MibTableColumn
zhoneFarEndCurrentDMs=_ZhoneFarEndCurrentDMs_Object((1,3,6,1,4,1,5504,5,2,6,1,12),_ZhoneFarEndCurrentDMs_Type())
zhoneFarEndCurrentDMs.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneFarEndCurrentDMs.setStatus(_A)
class _ZhoneFarEndInvalidIntervals_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,96))
_ZhoneFarEndInvalidIntervals_Type.__name__=_C
_ZhoneFarEndInvalidIntervals_Object=MibTableColumn
zhoneFarEndInvalidIntervals=_ZhoneFarEndInvalidIntervals_Object((1,3,6,1,4,1,5504,5,2,6,1,13),_ZhoneFarEndInvalidIntervals_Type())
zhoneFarEndInvalidIntervals.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneFarEndInvalidIntervals.setStatus(_A)
_ZhoneDs1FarEndIntervalTable_Object=MibTable
zhoneDs1FarEndIntervalTable=_ZhoneDs1FarEndIntervalTable_Object((1,3,6,1,4,1,5504,5,2,7))
if mibBuilder.loadTexts:zhoneDs1FarEndIntervalTable.setStatus(_A)
_ZhoneDs1FarEndIntervalEntry_Object=MibTableRow
zhoneDs1FarEndIntervalEntry=_ZhoneDs1FarEndIntervalEntry_Object((1,3,6,1,4,1,5504,5,2,7,1))
zhoneDs1FarEndIntervalEntry.setIndexNames((0,_E,_U),(0,_E,_V))
if mibBuilder.loadTexts:zhoneDs1FarEndIntervalEntry.setStatus(_A)
_ZhoneFarEndIntervalIndex_Type=InterfaceIndex
_ZhoneFarEndIntervalIndex_Object=MibTableColumn
zhoneFarEndIntervalIndex=_ZhoneFarEndIntervalIndex_Object((1,3,6,1,4,1,5504,5,2,7,1,1),_ZhoneFarEndIntervalIndex_Type())
zhoneFarEndIntervalIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:zhoneFarEndIntervalIndex.setStatus(_A)
class _ZhoneFarEndIntervalNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,96))
_ZhoneFarEndIntervalNumber_Type.__name__=_C
_ZhoneFarEndIntervalNumber_Object=MibTableColumn
zhoneFarEndIntervalNumber=_ZhoneFarEndIntervalNumber_Object((1,3,6,1,4,1,5504,5,2,7,1,2),_ZhoneFarEndIntervalNumber_Type())
zhoneFarEndIntervalNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneFarEndIntervalNumber.setStatus(_A)
_ZhoneFarEndIntervalESs_Type=PerfIntervalCount
_ZhoneFarEndIntervalESs_Object=MibTableColumn
zhoneFarEndIntervalESs=_ZhoneFarEndIntervalESs_Object((1,3,6,1,4,1,5504,5,2,7,1,3),_ZhoneFarEndIntervalESs_Type())
zhoneFarEndIntervalESs.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneFarEndIntervalESs.setStatus(_A)
_ZhoneFarEndIntervalSESs_Type=PerfIntervalCount
_ZhoneFarEndIntervalSESs_Object=MibTableColumn
zhoneFarEndIntervalSESs=_ZhoneFarEndIntervalSESs_Object((1,3,6,1,4,1,5504,5,2,7,1,4),_ZhoneFarEndIntervalSESs_Type())
zhoneFarEndIntervalSESs.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneFarEndIntervalSESs.setStatus(_A)
_ZhoneFarEndIntervalSEFSs_Type=PerfIntervalCount
_ZhoneFarEndIntervalSEFSs_Object=MibTableColumn
zhoneFarEndIntervalSEFSs=_ZhoneFarEndIntervalSEFSs_Object((1,3,6,1,4,1,5504,5,2,7,1,5),_ZhoneFarEndIntervalSEFSs_Type())
zhoneFarEndIntervalSEFSs.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneFarEndIntervalSEFSs.setStatus(_A)
_ZhoneFarEndIntervalUASs_Type=PerfIntervalCount
_ZhoneFarEndIntervalUASs_Object=MibTableColumn
zhoneFarEndIntervalUASs=_ZhoneFarEndIntervalUASs_Object((1,3,6,1,4,1,5504,5,2,7,1,6),_ZhoneFarEndIntervalUASs_Type())
zhoneFarEndIntervalUASs.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneFarEndIntervalUASs.setStatus(_A)
_ZhoneFarEndIntervalCSSs_Type=PerfIntervalCount
_ZhoneFarEndIntervalCSSs_Object=MibTableColumn
zhoneFarEndIntervalCSSs=_ZhoneFarEndIntervalCSSs_Object((1,3,6,1,4,1,5504,5,2,7,1,7),_ZhoneFarEndIntervalCSSs_Type())
zhoneFarEndIntervalCSSs.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneFarEndIntervalCSSs.setStatus(_A)
_ZhoneFarEndIntervalLESs_Type=PerfIntervalCount
_ZhoneFarEndIntervalLESs_Object=MibTableColumn
zhoneFarEndIntervalLESs=_ZhoneFarEndIntervalLESs_Object((1,3,6,1,4,1,5504,5,2,7,1,8),_ZhoneFarEndIntervalLESs_Type())
zhoneFarEndIntervalLESs.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneFarEndIntervalLESs.setStatus(_A)
_ZhoneFarEndIntervalPCVs_Type=PerfIntervalCount
_ZhoneFarEndIntervalPCVs_Object=MibTableColumn
zhoneFarEndIntervalPCVs=_ZhoneFarEndIntervalPCVs_Object((1,3,6,1,4,1,5504,5,2,7,1,9),_ZhoneFarEndIntervalPCVs_Type())
zhoneFarEndIntervalPCVs.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneFarEndIntervalPCVs.setStatus(_A)
_ZhoneFarEndIntervalBESs_Type=PerfIntervalCount
_ZhoneFarEndIntervalBESs_Object=MibTableColumn
zhoneFarEndIntervalBESs=_ZhoneFarEndIntervalBESs_Object((1,3,6,1,4,1,5504,5,2,7,1,10),_ZhoneFarEndIntervalBESs_Type())
zhoneFarEndIntervalBESs.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneFarEndIntervalBESs.setStatus(_A)
_ZhoneFarEndIntervalDMs_Type=PerfIntervalCount
_ZhoneFarEndIntervalDMs_Object=MibTableColumn
zhoneFarEndIntervalDMs=_ZhoneFarEndIntervalDMs_Object((1,3,6,1,4,1,5504,5,2,7,1,11),_ZhoneFarEndIntervalDMs_Type())
zhoneFarEndIntervalDMs.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneFarEndIntervalDMs.setStatus(_A)
_ZhoneFarEndIntervalValidData_Type=TruthValue
_ZhoneFarEndIntervalValidData_Object=MibTableColumn
zhoneFarEndIntervalValidData=_ZhoneFarEndIntervalValidData_Object((1,3,6,1,4,1,5504,5,2,7,1,12),_ZhoneFarEndIntervalValidData_Type())
zhoneFarEndIntervalValidData.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneFarEndIntervalValidData.setStatus(_A)
_ZhoneDs1FarEndTotalTable_Object=MibTable
zhoneDs1FarEndTotalTable=_ZhoneDs1FarEndTotalTable_Object((1,3,6,1,4,1,5504,5,2,8))
if mibBuilder.loadTexts:zhoneDs1FarEndTotalTable.setStatus(_A)
_ZhoneDs1FarEndTotalEntry_Object=MibTableRow
zhoneDs1FarEndTotalEntry=_ZhoneDs1FarEndTotalEntry_Object((1,3,6,1,4,1,5504,5,2,8,1))
zhoneDs1FarEndTotalEntry.setIndexNames((0,_E,_W))
if mibBuilder.loadTexts:zhoneDs1FarEndTotalEntry.setStatus(_A)
_ZhoneFarEndTotalIndex_Type=InterfaceIndex
_ZhoneFarEndTotalIndex_Object=MibTableColumn
zhoneFarEndTotalIndex=_ZhoneFarEndTotalIndex_Object((1,3,6,1,4,1,5504,5,2,8,1,1),_ZhoneFarEndTotalIndex_Type())
zhoneFarEndTotalIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:zhoneFarEndTotalIndex.setStatus(_A)
_ZhoneFarEndTotalESs_Type=PerfTotalCount
_ZhoneFarEndTotalESs_Object=MibTableColumn
zhoneFarEndTotalESs=_ZhoneFarEndTotalESs_Object((1,3,6,1,4,1,5504,5,2,8,1,2),_ZhoneFarEndTotalESs_Type())
zhoneFarEndTotalESs.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneFarEndTotalESs.setStatus(_A)
_ZhoneFarEndTotalSESs_Type=PerfTotalCount
_ZhoneFarEndTotalSESs_Object=MibTableColumn
zhoneFarEndTotalSESs=_ZhoneFarEndTotalSESs_Object((1,3,6,1,4,1,5504,5,2,8,1,3),_ZhoneFarEndTotalSESs_Type())
zhoneFarEndTotalSESs.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneFarEndTotalSESs.setStatus(_A)
_ZhoneFarEndTotalSEFSs_Type=PerfTotalCount
_ZhoneFarEndTotalSEFSs_Object=MibTableColumn
zhoneFarEndTotalSEFSs=_ZhoneFarEndTotalSEFSs_Object((1,3,6,1,4,1,5504,5,2,8,1,4),_ZhoneFarEndTotalSEFSs_Type())
zhoneFarEndTotalSEFSs.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneFarEndTotalSEFSs.setStatus(_A)
_ZhoneFarEndTotalUASs_Type=PerfTotalCount
_ZhoneFarEndTotalUASs_Object=MibTableColumn
zhoneFarEndTotalUASs=_ZhoneFarEndTotalUASs_Object((1,3,6,1,4,1,5504,5,2,8,1,5),_ZhoneFarEndTotalUASs_Type())
zhoneFarEndTotalUASs.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneFarEndTotalUASs.setStatus(_A)
_ZhoneFarEndTotalCSSs_Type=PerfTotalCount
_ZhoneFarEndTotalCSSs_Object=MibTableColumn
zhoneFarEndTotalCSSs=_ZhoneFarEndTotalCSSs_Object((1,3,6,1,4,1,5504,5,2,8,1,6),_ZhoneFarEndTotalCSSs_Type())
zhoneFarEndTotalCSSs.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneFarEndTotalCSSs.setStatus(_A)
_ZhoneFarEndTotalLESs_Type=PerfTotalCount
_ZhoneFarEndTotalLESs_Object=MibTableColumn
zhoneFarEndTotalLESs=_ZhoneFarEndTotalLESs_Object((1,3,6,1,4,1,5504,5,2,8,1,7),_ZhoneFarEndTotalLESs_Type())
zhoneFarEndTotalLESs.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneFarEndTotalLESs.setStatus(_A)
_ZhoneFarEndTotalPCVs_Type=PerfTotalCount
_ZhoneFarEndTotalPCVs_Object=MibTableColumn
zhoneFarEndTotalPCVs=_ZhoneFarEndTotalPCVs_Object((1,3,6,1,4,1,5504,5,2,8,1,8),_ZhoneFarEndTotalPCVs_Type())
zhoneFarEndTotalPCVs.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneFarEndTotalPCVs.setStatus(_A)
_ZhoneFarEndTotalBESs_Type=PerfTotalCount
_ZhoneFarEndTotalBESs_Object=MibTableColumn
zhoneFarEndTotalBESs=_ZhoneFarEndTotalBESs_Object((1,3,6,1,4,1,5504,5,2,8,1,9),_ZhoneFarEndTotalBESs_Type())
zhoneFarEndTotalBESs.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneFarEndTotalBESs.setStatus(_A)
_ZhoneFarEndTotalDMs_Type=PerfTotalCount
_ZhoneFarEndTotalDMs_Object=MibTableColumn
zhoneFarEndTotalDMs=_ZhoneFarEndTotalDMs_Object((1,3,6,1,4,1,5504,5,2,8,1,10),_ZhoneFarEndTotalDMs_Type())
zhoneFarEndTotalDMs.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneFarEndTotalDMs.setStatus(_A)
_ZhoneChanMappingTable_Object=MibTable
zhoneChanMappingTable=_ZhoneChanMappingTable_Object((1,3,6,1,4,1,5504,5,2,9))
if mibBuilder.loadTexts:zhoneChanMappingTable.setStatus(_A)
_ZhoneChanMappingEntry_Object=MibTableRow
zhoneChanMappingEntry=_ZhoneChanMappingEntry_Object((1,3,6,1,4,1,5504,5,2,9,1))
zhoneChanMappingEntry.setIndexNames((0,_H,_L),(0,_E,_X))
if mibBuilder.loadTexts:zhoneChanMappingEntry.setStatus(_A)
_ZhoneChanMappedIfIndex_Type=InterfaceIndex
_ZhoneChanMappedIfIndex_Object=MibTableColumn
zhoneChanMappedIfIndex=_ZhoneChanMappedIfIndex_Object((1,3,6,1,4,1,5504,5,2,9,1,1),_ZhoneChanMappedIfIndex_Type())
zhoneChanMappedIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneChanMappedIfIndex.setStatus(_A)
_ZhoneDsxTraps_ObjectIdentity=ObjectIdentity
zhoneDsxTraps=_ZhoneDsxTraps_ObjectIdentity((1,3,6,1,4,1,5504,5,2,10))
_ZhoneDsxTrapsV2_ObjectIdentity=ObjectIdentity
zhoneDsxTrapsV2=_ZhoneDsxTrapsV2_ObjectIdentity((1,3,6,1,4,1,5504,5,2,10,0))
_ZhoneDs1BertTable_Object=MibTable
zhoneDs1BertTable=_ZhoneDs1BertTable_Object((1,3,6,1,4,1,5504,5,2,13))
if mibBuilder.loadTexts:zhoneDs1BertTable.setStatus(_A)
_ZhoneDs1BertEntry_Object=MibTableRow
zhoneDs1BertEntry=_ZhoneDs1BertEntry_Object((1,3,6,1,4,1,5504,5,2,13,1))
zhoneDs1BertEntry.setIndexNames((0,_E,_J))
if mibBuilder.loadTexts:zhoneDs1BertEntry.setStatus(_A)
class _ZhoneBertIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,21))
_ZhoneBertIndex_Type.__name__=_C
_ZhoneBertIndex_Object=MibTableColumn
zhoneBertIndex=_ZhoneBertIndex_Object((1,3,6,1,4,1,5504,5,2,13,1,1),_ZhoneBertIndex_Type())
zhoneBertIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:zhoneBertIndex.setStatus(_A)
_ZhoneBertInterfaceIndex_Type=InterfaceIndex
_ZhoneBertInterfaceIndex_Object=MibTableColumn
zhoneBertInterfaceIndex=_ZhoneBertInterfaceIndex_Object((1,3,6,1,4,1,5504,5,2,13,1,2),_ZhoneBertInterfaceIndex_Type())
zhoneBertInterfaceIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneBertInterfaceIndex.setStatus(_A)
class _ZhoneBertRequest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('noOp',1),('start',2),('stop',3)))
_ZhoneBertRequest_Type.__name__=_C
_ZhoneBertRequest_Object=MibTableColumn
zhoneBertRequest=_ZhoneBertRequest_Object((1,3,6,1,4,1,5504,5,2,13,1,3),_ZhoneBertRequest_Type())
zhoneBertRequest.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneBertRequest.setStatus(_A)
class _ZhoneBertType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('qrss',1),('prbs215',2),('prbs220',3)))
_ZhoneBertType_Type.__name__=_C
_ZhoneBertType_Object=MibTableColumn
zhoneBertType=_ZhoneBertType_Object((1,3,6,1,4,1,5504,5,2,13,1,4),_ZhoneBertType_Type())
zhoneBertType.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneBertType.setStatus(_A)
class _ZhoneBertTestDuration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,300))
_ZhoneBertTestDuration_Type.__name__=_C
_ZhoneBertTestDuration_Object=MibTableColumn
zhoneBertTestDuration=_ZhoneBertTestDuration_Object((1,3,6,1,4,1,5504,5,2,13,1,5),_ZhoneBertTestDuration_Type())
zhoneBertTestDuration.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneBertTestDuration.setStatus(_A)
class _ZhoneBertLoopUp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('noloop',1),('lineloop',2),('payloadloop',3)))
_ZhoneBertLoopUp_Type.__name__=_C
_ZhoneBertLoopUp_Object=MibTableColumn
zhoneBertLoopUp=_ZhoneBertLoopUp_Object((1,3,6,1,4,1,5504,5,2,13,1,6),_ZhoneBertLoopUp_Type())
zhoneBertLoopUp.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneBertLoopUp.setStatus(_A)
_ZhoneDs1BertResultsTable_Object=MibTable
zhoneDs1BertResultsTable=_ZhoneDs1BertResultsTable_Object((1,3,6,1,4,1,5504,5,2,14))
if mibBuilder.loadTexts:zhoneDs1BertResultsTable.setStatus(_A)
_ZhoneDs1BertResultsEntry_Object=MibTableRow
zhoneDs1BertResultsEntry=_ZhoneDs1BertResultsEntry_Object((1,3,6,1,4,1,5504,5,2,14,1))
zhoneDs1BertResultsEntry.setIndexNames((0,_E,_J))
if mibBuilder.loadTexts:zhoneDs1BertResultsEntry.setStatus(_A)
class _ZhoneBertStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('inProgress',1),('abortInProgress',2),('complete',3),('noResults',4),('aborted',5),('unsupported',6),('portNotAdminTest',7),('failed',8)))
_ZhoneBertStatus_Type.__name__=_C
_ZhoneBertStatus_Object=MibTableColumn
zhoneBertStatus=_ZhoneBertStatus_Object((1,3,6,1,4,1,5504,5,2,14,1,1),_ZhoneBertStatus_Type())
zhoneBertStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneBertStatus.setStatus(_A)
class _ZhoneBertElapsedTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,300))
_ZhoneBertElapsedTime_Type.__name__=_C
_ZhoneBertElapsedTime_Object=MibTableColumn
zhoneBertElapsedTime=_ZhoneBertElapsedTime_Object((1,3,6,1,4,1,5504,5,2,14,1,2),_ZhoneBertElapsedTime_Type())
zhoneBertElapsedTime.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneBertElapsedTime.setStatus(_A)
class _ZhoneBertErroredSeconds_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,300))
_ZhoneBertErroredSeconds_Type.__name__=_C
_ZhoneBertErroredSeconds_Object=MibTableColumn
zhoneBertErroredSeconds=_ZhoneBertErroredSeconds_Object((1,3,6,1,4,1,5504,5,2,14,1,3),_ZhoneBertErroredSeconds_Type())
zhoneBertErroredSeconds.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneBertErroredSeconds.setStatus(_A)
class _ZhoneBertOutOfSynchSeconds_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,300))
_ZhoneBertOutOfSynchSeconds_Type.__name__=_C
_ZhoneBertOutOfSynchSeconds_Object=MibTableColumn
zhoneBertOutOfSynchSeconds=_ZhoneBertOutOfSynchSeconds_Object((1,3,6,1,4,1,5504,5,2,14,1,4),_ZhoneBertOutOfSynchSeconds_Type())
zhoneBertOutOfSynchSeconds.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneBertOutOfSynchSeconds.setStatus(_A)
class _ZhoneBertErrors_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_ZhoneBertErrors_Type.__name__=_C
_ZhoneBertErrors_Object=MibTableColumn
zhoneBertErrors=_ZhoneBertErrors_Object((1,3,6,1,4,1,5504,5,2,14,1,5),_ZhoneBertErrors_Type())
zhoneBertErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneBertErrors.setStatus(_A)
zhoneLineStatusChange=NotificationType((1,3,6,1,4,1,5504,5,2,10,0,1))
zhoneLineStatusChange.setObjects(*((_E,_Y),(_E,_Z),(_H,_K)))
if mibBuilder.loadTexts:zhoneLineStatusChange.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'zhoneDs1Mib':zhoneDs1Mib,'zhoneDs1Table':zhoneDs1Table,'zhoneDs1Entry':zhoneDs1Entry,_N:zhoneLineIndex,'zhoneTimeElapsed':zhoneTimeElapsed,'zhoneValidIntervals':zhoneValidIntervals,'zhoneLineType':zhoneLineType,'zhoneLineCoding':zhoneLineCoding,'zhoneSendCode':zhoneSendCode,'zhoneCircuitIdentifier':zhoneCircuitIdentifier,'zhoneLoopbackConfig':zhoneLoopbackConfig,_Y:zhoneLineStatus,'zhoneSignalMode':zhoneSignalMode,'zhoneTransmitClockSource':zhoneTransmitClockSource,'zhoneFdl':zhoneFdl,'zhoneInvalidIntervals':zhoneInvalidIntervals,'zhoneDsxLineLength':zhoneDsxLineLength,_Z:zhoneLineStatusLastChange,'zhoneLineStatusChangeTrapEnable':zhoneLineStatusChangeTrapEnable,'zhoneLoopbackStatus':zhoneLoopbackStatus,_X:zhoneDs1ChannelNumber,'zhoneChannelization':zhoneChannelization,'zhoneDs1Mode':zhoneDs1Mode,'zhoneCsuLineLength':zhoneCsuLineLength,'zhoneClockSourceEligibility':zhoneClockSourceEligibility,'zhoneCellScramble':zhoneCellScramble,'zhoneCosetPolynomial':zhoneCosetPolynomial,'zhoneDs1ProtocolEmulation':zhoneDs1ProtocolEmulation,'zhoneDs1SignalType':zhoneDs1SignalType,'zhoneDs1GroupIndex':zhoneDs1GroupIndex,'zhoneDs1LinePower':zhoneDs1LinePower,'zhoneDs1TimeslotAssignment':zhoneDs1TimeslotAssignment,'zhoneDs1TxClockRecovery':zhoneDs1TxClockRecovery,'zhoneDs1TxClockAdaptiveQuality':zhoneDs1TxClockAdaptiveQuality,'zhoneDs1CurrentTable':zhoneDs1CurrentTable,'zhoneDs1CurrentEntry':zhoneDs1CurrentEntry,_P:zhoneCurrentIndex,'zhoneCurrentESs':zhoneCurrentESs,'zhoneCurrentSESs':zhoneCurrentSESs,'zhoneCurrentSEFSs':zhoneCurrentSEFSs,'zhoneCurrentUASs':zhoneCurrentUASs,'zhoneCurrentCSSs':zhoneCurrentCSSs,'zhoneCurrentPCVs':zhoneCurrentPCVs,'zhoneCurrentLESs':zhoneCurrentLESs,'zhoneCurrentBESs':zhoneCurrentBESs,'zhoneCurrentDMs':zhoneCurrentDMs,'zhoneCurrentLCVs':zhoneCurrentLCVs,'zhoneDs1IntervalTable':zhoneDs1IntervalTable,'zhoneDs1IntervalEntry':zhoneDs1IntervalEntry,_Q:zhoneIntervalIndex,_R:zhoneIntervalNumber,'zhoneIntervalESs':zhoneIntervalESs,'zhoneIntervalSESs':zhoneIntervalSESs,'zhoneIntervalSEFSs':zhoneIntervalSEFSs,'zhoneIntervalUASs':zhoneIntervalUASs,'zhoneIntervalCSSs':zhoneIntervalCSSs,'zhoneIntervalPCVs':zhoneIntervalPCVs,'zhoneIntervalLESs':zhoneIntervalLESs,'zhoneIntervalBESs':zhoneIntervalBESs,'zhoneIntervalDMs':zhoneIntervalDMs,'zhoneIntervalLCVs':zhoneIntervalLCVs,'zhoneIntervalValidData':zhoneIntervalValidData,'zhoneDs1TotalTable':zhoneDs1TotalTable,'zhoneDs1TotalEntry':zhoneDs1TotalEntry,_S:zhoneTotalIndex,'zhoneTotalESs':zhoneTotalESs,'zhoneTotalSESs':zhoneTotalSESs,'zhoneTotalSEFSs':zhoneTotalSEFSs,'zhoneTotalUASs':zhoneTotalUASs,'zhoneTotalCSSs':zhoneTotalCSSs,'zhoneTotalPCVs':zhoneTotalPCVs,'zhoneTotalLESs':zhoneTotalLESs,'zhoneTotalBESs':zhoneTotalBESs,'zhoneTotalDMs':zhoneTotalDMs,'zhoneTotalLCVs':zhoneTotalLCVs,'zhoneDs1FarEndCurrentTable':zhoneDs1FarEndCurrentTable,'zhoneDs1FarEndCurrentEntry':zhoneDs1FarEndCurrentEntry,_T:zhoneFarEndCurrentIndex,'zhoneFarEndTimeElapsed':zhoneFarEndTimeElapsed,'zhoneFarEndValidIntervals':zhoneFarEndValidIntervals,'zhoneFarEndCurrentESs':zhoneFarEndCurrentESs,'zhoneFarEndCurrentSESs':zhoneFarEndCurrentSESs,'zhoneFarEndCurrentSEFSs':zhoneFarEndCurrentSEFSs,'zhoneFarEndCurrentUASs':zhoneFarEndCurrentUASs,'zhoneFarEndCurrentCSSs':zhoneFarEndCurrentCSSs,'zhoneFarEndCurrentLESs':zhoneFarEndCurrentLESs,'zhoneFarEndCurrentPCVs':zhoneFarEndCurrentPCVs,'zhoneFarEndCurrentBESs':zhoneFarEndCurrentBESs,'zhoneFarEndCurrentDMs':zhoneFarEndCurrentDMs,'zhoneFarEndInvalidIntervals':zhoneFarEndInvalidIntervals,'zhoneDs1FarEndIntervalTable':zhoneDs1FarEndIntervalTable,'zhoneDs1FarEndIntervalEntry':zhoneDs1FarEndIntervalEntry,_U:zhoneFarEndIntervalIndex,_V:zhoneFarEndIntervalNumber,'zhoneFarEndIntervalESs':zhoneFarEndIntervalESs,'zhoneFarEndIntervalSESs':zhoneFarEndIntervalSESs,'zhoneFarEndIntervalSEFSs':zhoneFarEndIntervalSEFSs,'zhoneFarEndIntervalUASs':zhoneFarEndIntervalUASs,'zhoneFarEndIntervalCSSs':zhoneFarEndIntervalCSSs,'zhoneFarEndIntervalLESs':zhoneFarEndIntervalLESs,'zhoneFarEndIntervalPCVs':zhoneFarEndIntervalPCVs,'zhoneFarEndIntervalBESs':zhoneFarEndIntervalBESs,'zhoneFarEndIntervalDMs':zhoneFarEndIntervalDMs,'zhoneFarEndIntervalValidData':zhoneFarEndIntervalValidData,'zhoneDs1FarEndTotalTable':zhoneDs1FarEndTotalTable,'zhoneDs1FarEndTotalEntry':zhoneDs1FarEndTotalEntry,_W:zhoneFarEndTotalIndex,'zhoneFarEndTotalESs':zhoneFarEndTotalESs,'zhoneFarEndTotalSESs':zhoneFarEndTotalSESs,'zhoneFarEndTotalSEFSs':zhoneFarEndTotalSEFSs,'zhoneFarEndTotalUASs':zhoneFarEndTotalUASs,'zhoneFarEndTotalCSSs':zhoneFarEndTotalCSSs,'zhoneFarEndTotalLESs':zhoneFarEndTotalLESs,'zhoneFarEndTotalPCVs':zhoneFarEndTotalPCVs,'zhoneFarEndTotalBESs':zhoneFarEndTotalBESs,'zhoneFarEndTotalDMs':zhoneFarEndTotalDMs,'zhoneChanMappingTable':zhoneChanMappingTable,'zhoneChanMappingEntry':zhoneChanMappingEntry,'zhoneChanMappedIfIndex':zhoneChanMappedIfIndex,'zhoneDsxTraps':zhoneDsxTraps,'zhoneDsxTrapsV2':zhoneDsxTrapsV2,'zhoneLineStatusChange':zhoneLineStatusChange,'zhoneDs1BertTable':zhoneDs1BertTable,'zhoneDs1BertEntry':zhoneDs1BertEntry,_J:zhoneBertIndex,'zhoneBertInterfaceIndex':zhoneBertInterfaceIndex,'zhoneBertRequest':zhoneBertRequest,'zhoneBertType':zhoneBertType,'zhoneBertTestDuration':zhoneBertTestDuration,'zhoneBertLoopUp':zhoneBertLoopUp,'zhoneDs1BertResultsTable':zhoneDs1BertResultsTable,'zhoneDs1BertResultsEntry':zhoneDs1BertResultsEntry,'zhoneBertStatus':zhoneBertStatus,'zhoneBertElapsedTime':zhoneBertElapsedTime,'zhoneBertErroredSeconds':zhoneBertErroredSeconds,'zhoneBertOutOfSynchSeconds':zhoneBertOutOfSynchSeconds,'zhoneBertErrors':zhoneBertErrors})