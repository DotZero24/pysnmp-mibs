_L='testing'
_K='enabled'
_J='DisplayString'
_I='zxDsx1ClockStatus'
_H='disabled'
_G='other'
_F='zxDsx1LineIndex'
_E='ZXDS1-MIB'
_D='read-only'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_J,'PhysAddress','TextualConvention','TimeStamp','TruthValue')
zxPwCTDM,=mibBuilder.importSymbols('ZTE-MASTER-MIB','zxPwCTDM')
zxDs1=ModuleIdentity((1,3,6,1,4,1,3902,1015,1013,2,1,1))
_ZxDsx1ConfigTable_Object=MibTable
zxDsx1ConfigTable=_ZxDsx1ConfigTable_Object((1,3,6,1,4,1,3902,1015,1013,2,1,1,1))
if mibBuilder.loadTexts:zxDsx1ConfigTable.setStatus(_A)
_ZxDsx1ConfigEntry_Object=MibTableRow
zxDsx1ConfigEntry=_ZxDsx1ConfigEntry_Object((1,3,6,1,4,1,3902,1015,1013,2,1,1,1,1))
zxDsx1ConfigEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:zxDsx1ConfigEntry.setStatus(_A)
_ZxDsx1LineIndex_Type=InterfaceIndex
_ZxDsx1LineIndex_Object=MibTableColumn
zxDsx1LineIndex=_ZxDsx1LineIndex_Object((1,3,6,1,4,1,3902,1015,1013,2,1,1,1,1,1),_ZxDsx1LineIndex_Type())
zxDsx1LineIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:zxDsx1LineIndex.setStatus(_A)
_ZxDsx1IfIndex_Type=InterfaceIndex
_ZxDsx1IfIndex_Object=MibTableColumn
zxDsx1IfIndex=_ZxDsx1IfIndex_Object((1,3,6,1,4,1,3902,1015,1013,2,1,1,1,1,2),_ZxDsx1IfIndex_Type())
zxDsx1IfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:zxDsx1IfIndex.setStatus('deprecated')
class _ZxDsx1TimeElapsed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,899))
_ZxDsx1TimeElapsed_Type.__name__=_B
_ZxDsx1TimeElapsed_Object=MibTableColumn
zxDsx1TimeElapsed=_ZxDsx1TimeElapsed_Object((1,3,6,1,4,1,3902,1015,1013,2,1,1,1,1,3),_ZxDsx1TimeElapsed_Type())
zxDsx1TimeElapsed.setMaxAccess(_D)
if mibBuilder.loadTexts:zxDsx1TimeElapsed.setStatus(_A)
class _ZxDsx1ValidIntervals_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,96))
_ZxDsx1ValidIntervals_Type.__name__=_B
_ZxDsx1ValidIntervals_Object=MibTableColumn
zxDsx1ValidIntervals=_ZxDsx1ValidIntervals_Object((1,3,6,1,4,1,3902,1015,1013,2,1,1,1,1,4),_ZxDsx1ValidIntervals_Type())
zxDsx1ValidIntervals.setMaxAccess(_D)
if mibBuilder.loadTexts:zxDsx1ValidIntervals.setStatus(_A)
class _ZxDsx1LineType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13)));namedValues=NamedValues(*((_G,1),('dsx1ESF',2),('dsx1D4',3),('dsx1E1',4),('dsx1E1CRC',5),('dsx1E1MF',6),('dsx1E1CRCMF',7),('dsx1Unframed',8),('dsx1E1Unframed',9),('dsx1DS2M12',10),('dsx1E2',11),('dsx1E1Q50',12),('dsx1E1Q50CRC',13)))
_ZxDsx1LineType_Type.__name__=_B
_ZxDsx1LineType_Object=MibTableColumn
zxDsx1LineType=_ZxDsx1LineType_Object((1,3,6,1,4,1,3902,1015,1013,2,1,1,1,1,5),_ZxDsx1LineType_Type())
zxDsx1LineType.setMaxAccess(_C)
if mibBuilder.loadTexts:zxDsx1LineType.setStatus(_A)
class _ZxDsx1LineCoding_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('dsx1JBZS',1),('dsx1B8ZS',2),('dsx1HDB3',3),('dsx1ZBTSI',4),('dsx1AMI',5),(_G,6),('dsx1B6ZS',7)))
_ZxDsx1LineCoding_Type.__name__=_B
_ZxDsx1LineCoding_Object=MibTableColumn
zxDsx1LineCoding=_ZxDsx1LineCoding_Object((1,3,6,1,4,1,3902,1015,1013,2,1,1,1,1,6),_ZxDsx1LineCoding_Type())
zxDsx1LineCoding.setMaxAccess(_C)
if mibBuilder.loadTexts:zxDsx1LineCoding.setStatus(_A)
class _ZxDsx1SendCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('dsx1SendNoCode',1),('dsx1SendLineCode',2),('dsx1SendPayloadCode',3),('dsx1SendResetCode',4),('dsx1SendQRS',5),('dsx1Send511Pattern',6),('dsx1Send3in24Pattern',7),('dsx1SendOtherTestPattern',8)))
_ZxDsx1SendCode_Type.__name__=_B
_ZxDsx1SendCode_Object=MibTableColumn
zxDsx1SendCode=_ZxDsx1SendCode_Object((1,3,6,1,4,1,3902,1015,1013,2,1,1,1,1,7),_ZxDsx1SendCode_Type())
zxDsx1SendCode.setMaxAccess(_C)
if mibBuilder.loadTexts:zxDsx1SendCode.setStatus(_A)
class _ZxDsx1CircuitIdentifier_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_ZxDsx1CircuitIdentifier_Type.__name__=_J
_ZxDsx1CircuitIdentifier_Object=MibTableColumn
zxDsx1CircuitIdentifier=_ZxDsx1CircuitIdentifier_Object((1,3,6,1,4,1,3902,1015,1013,2,1,1,1,1,8),_ZxDsx1CircuitIdentifier_Type())
zxDsx1CircuitIdentifier.setMaxAccess(_C)
if mibBuilder.loadTexts:zxDsx1CircuitIdentifier.setStatus(_A)
class _ZxDsx1LoopbackConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('dsx1NoLoop',1),('dsx1PayloadLoop',2),('dsx1LineLoop',3),('dsx1OtherLoop',4),('dsx1InwardLoop',5),('dsx1DualLoop',6)))
_ZxDsx1LoopbackConfig_Type.__name__=_B
_ZxDsx1LoopbackConfig_Object=MibTableColumn
zxDsx1LoopbackConfig=_ZxDsx1LoopbackConfig_Object((1,3,6,1,4,1,3902,1015,1013,2,1,1,1,1,9),_ZxDsx1LoopbackConfig_Type())
zxDsx1LoopbackConfig.setMaxAccess(_C)
if mibBuilder.loadTexts:zxDsx1LoopbackConfig.setStatus(_A)
class _ZxDsx1LineStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,131071))
_ZxDsx1LineStatus_Type.__name__=_B
_ZxDsx1LineStatus_Object=MibTableColumn
zxDsx1LineStatus=_ZxDsx1LineStatus_Object((1,3,6,1,4,1,3902,1015,1013,2,1,1,1,1,10),_ZxDsx1LineStatus_Type())
zxDsx1LineStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:zxDsx1LineStatus.setStatus(_A)
class _ZxDsx1SignalMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('none',1),('robbedBit',2),('bitOriented',3),('messageOriented',4),(_G,5)))
_ZxDsx1SignalMode_Type.__name__=_B
_ZxDsx1SignalMode_Object=MibTableColumn
zxDsx1SignalMode=_ZxDsx1SignalMode_Object((1,3,6,1,4,1,3902,1015,1013,2,1,1,1,1,11),_ZxDsx1SignalMode_Type())
zxDsx1SignalMode.setMaxAccess(_C)
if mibBuilder.loadTexts:zxDsx1SignalMode.setStatus(_A)
class _ZxDsx1TransmitClockSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('loopTiming',1),('localTiming',2),('throughTiming',3),('adaptive',4),('enhancedAdaptive',5),('defferential',6)))
_ZxDsx1TransmitClockSource_Type.__name__=_B
_ZxDsx1TransmitClockSource_Object=MibTableColumn
zxDsx1TransmitClockSource=_ZxDsx1TransmitClockSource_Object((1,3,6,1,4,1,3902,1015,1013,2,1,1,1,1,12),_ZxDsx1TransmitClockSource_Type())
zxDsx1TransmitClockSource.setMaxAccess(_C)
if mibBuilder.loadTexts:zxDsx1TransmitClockSource.setStatus(_A)
class _ZxDsx1Fdl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_ZxDsx1Fdl_Type.__name__=_B
_ZxDsx1Fdl_Object=MibTableColumn
zxDsx1Fdl=_ZxDsx1Fdl_Object((1,3,6,1,4,1,3902,1015,1013,2,1,1,1,1,13),_ZxDsx1Fdl_Type())
zxDsx1Fdl.setMaxAccess(_C)
if mibBuilder.loadTexts:zxDsx1Fdl.setStatus(_A)
class _ZxDsx1InvalidIntervals_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,96))
_ZxDsx1InvalidIntervals_Type.__name__=_B
_ZxDsx1InvalidIntervals_Object=MibTableColumn
zxDsx1InvalidIntervals=_ZxDsx1InvalidIntervals_Object((1,3,6,1,4,1,3902,1015,1013,2,1,1,1,1,14),_ZxDsx1InvalidIntervals_Type())
zxDsx1InvalidIntervals.setMaxAccess(_D)
if mibBuilder.loadTexts:zxDsx1InvalidIntervals.setStatus(_A)
class _ZxDsx1LineLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,64000))
_ZxDsx1LineLength_Type.__name__=_B
_ZxDsx1LineLength_Object=MibTableColumn
zxDsx1LineLength=_ZxDsx1LineLength_Object((1,3,6,1,4,1,3902,1015,1013,2,1,1,1,1,15),_ZxDsx1LineLength_Type())
zxDsx1LineLength.setMaxAccess(_C)
if mibBuilder.loadTexts:zxDsx1LineLength.setStatus(_A)
if mibBuilder.loadTexts:zxDsx1LineLength.setUnits('meters')
_ZxDsx1LineStatusLastChange_Type=TimeStamp
_ZxDsx1LineStatusLastChange_Object=MibTableColumn
zxDsx1LineStatusLastChange=_ZxDsx1LineStatusLastChange_Object((1,3,6,1,4,1,3902,1015,1013,2,1,1,1,1,16),_ZxDsx1LineStatusLastChange_Type())
zxDsx1LineStatusLastChange.setMaxAccess(_D)
if mibBuilder.loadTexts:zxDsx1LineStatusLastChange.setStatus(_A)
class _ZxDsx1LineStatusChangeTrapEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_H,2)))
_ZxDsx1LineStatusChangeTrapEnable_Type.__name__=_B
_ZxDsx1LineStatusChangeTrapEnable_Object=MibTableColumn
zxDsx1LineStatusChangeTrapEnable=_ZxDsx1LineStatusChangeTrapEnable_Object((1,3,6,1,4,1,3902,1015,1013,2,1,1,1,1,17),_ZxDsx1LineStatusChangeTrapEnable_Type())
zxDsx1LineStatusChangeTrapEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:zxDsx1LineStatusChangeTrapEnable.setStatus(_A)
class _ZxDsx1LoopbackStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,127))
_ZxDsx1LoopbackStatus_Type.__name__=_B
_ZxDsx1LoopbackStatus_Object=MibTableColumn
zxDsx1LoopbackStatus=_ZxDsx1LoopbackStatus_Object((1,3,6,1,4,1,3902,1015,1013,2,1,1,1,1,18),_ZxDsx1LoopbackStatus_Type())
zxDsx1LoopbackStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:zxDsx1LoopbackStatus.setStatus(_A)
class _ZxDsx1Ds1ChannelNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,28))
_ZxDsx1Ds1ChannelNumber_Type.__name__=_B
_ZxDsx1Ds1ChannelNumber_Object=MibTableColumn
zxDsx1Ds1ChannelNumber=_ZxDsx1Ds1ChannelNumber_Object((1,3,6,1,4,1,3902,1015,1013,2,1,1,1,1,19),_ZxDsx1Ds1ChannelNumber_Type())
zxDsx1Ds1ChannelNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:zxDsx1Ds1ChannelNumber.setStatus(_A)
class _ZxDsx1Channelization_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),('enabledDs0',2),('enabledDs1',3)))
_ZxDsx1Channelization_Type.__name__=_B
_ZxDsx1Channelization_Object=MibTableColumn
zxDsx1Channelization=_ZxDsx1Channelization_Object((1,3,6,1,4,1,3902,1015,1013,2,1,1,1,1,20),_ZxDsx1Channelization_Type())
zxDsx1Channelization.setMaxAccess(_C)
if mibBuilder.loadTexts:zxDsx1Channelization.setStatus(_A)
class _ZxDsx1LineMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('csu',1),('dsu',2)))
_ZxDsx1LineMode_Type.__name__=_B
_ZxDsx1LineMode_Object=MibTableColumn
zxDsx1LineMode=_ZxDsx1LineMode_Object((1,3,6,1,4,1,3902,1015,1013,2,1,1,1,1,21),_ZxDsx1LineMode_Type())
zxDsx1LineMode.setMaxAccess(_C)
if mibBuilder.loadTexts:zxDsx1LineMode.setStatus(_A)
class _ZxDsx1LineBuildOut_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('notApplicable',1),('neg75dB',2),('neg15dB',3),('neg225dB',4),('zerodB',5)))
_ZxDsx1LineBuildOut_Type.__name__=_B
_ZxDsx1LineBuildOut_Object=MibTableColumn
zxDsx1LineBuildOut=_ZxDsx1LineBuildOut_Object((1,3,6,1,4,1,3902,1015,1013,2,1,1,1,1,22),_ZxDsx1LineBuildOut_Type())
zxDsx1LineBuildOut.setMaxAccess(_C)
if mibBuilder.loadTexts:zxDsx1LineBuildOut.setStatus(_A)
class _ZxDsx1AdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('up',1),('down',2),(_L,3)))
_ZxDsx1AdminStatus_Type.__name__=_B
_ZxDsx1AdminStatus_Object=MibTableColumn
zxDsx1AdminStatus=_ZxDsx1AdminStatus_Object((1,3,6,1,4,1,3902,1015,1013,2,1,1,1,1,23),_ZxDsx1AdminStatus_Type())
zxDsx1AdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:zxDsx1AdminStatus.setStatus(_A)
class _ZxDsx1OperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('up',1),('down',2),(_L,3)))
_ZxDsx1OperStatus_Type.__name__=_B
_ZxDsx1OperStatus_Object=MibTableColumn
zxDsx1OperStatus=_ZxDsx1OperStatus_Object((1,3,6,1,4,1,3902,1015,1013,2,1,1,1,1,24),_ZxDsx1OperStatus_Type())
zxDsx1OperStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:zxDsx1OperStatus.setStatus(_A)
class _ZxDsx1ClockStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,127))
_ZxDsx1ClockStatus_Type.__name__=_B
_ZxDsx1ClockStatus_Object=MibTableColumn
zxDsx1ClockStatus=_ZxDsx1ClockStatus_Object((1,3,6,1,4,1,3902,1015,1013,2,1,1,1,1,25),_ZxDsx1ClockStatus_Type())
zxDsx1ClockStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:zxDsx1ClockStatus.setStatus(_A)
_ZxDsx1CfgInfoSend_Type=TruthValue
_ZxDsx1CfgInfoSend_Object=MibTableColumn
zxDsx1CfgInfoSend=_ZxDsx1CfgInfoSend_Object((1,3,6,1,4,1,3902,1015,1013,2,1,1,1,1,26),_ZxDsx1CfgInfoSend_Type())
zxDsx1CfgInfoSend.setMaxAccess(_C)
if mibBuilder.loadTexts:zxDsx1CfgInfoSend.setStatus(_A)
_ZxDsx1Retiming_Type=TruthValue
_ZxDsx1Retiming_Object=MibTableColumn
zxDsx1Retiming=_ZxDsx1Retiming_Object((1,3,6,1,4,1,3902,1015,1013,2,1,1,1,1,27),_ZxDsx1Retiming_Type())
zxDsx1Retiming.setMaxAccess(_C)
if mibBuilder.loadTexts:zxDsx1Retiming.setStatus(_A)
_ZxDsx1Impedance_Type=Integer32
_ZxDsx1Impedance_Object=MibTableColumn
zxDsx1Impedance=_ZxDsx1Impedance_Object((1,3,6,1,4,1,3902,1015,1013,2,1,1,1,1,28),_ZxDsx1Impedance_Type())
zxDsx1Impedance.setMaxAccess(_C)
if mibBuilder.loadTexts:zxDsx1Impedance.setStatus(_A)
class _ZxDsx1FrameType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('unframe',1),('doubleframe',2),('multiframe',3)))
_ZxDsx1FrameType_Type.__name__=_B
_ZxDsx1FrameType_Object=MibTableColumn
zxDsx1FrameType=_ZxDsx1FrameType_Object((1,3,6,1,4,1,3902,1015,1013,2,1,1,1,1,29),_ZxDsx1FrameType_Type())
zxDsx1FrameType.setMaxAccess(_C)
if mibBuilder.loadTexts:zxDsx1FrameType.setStatus(_A)
class _ZxDsx1BER_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000000))
_ZxDsx1BER_Type.__name__=_B
_ZxDsx1BER_Object=MibTableColumn
zxDsx1BER=_ZxDsx1BER_Object((1,3,6,1,4,1,3902,1015,1013,2,1,1,1,1,30),_ZxDsx1BER_Type())
zxDsx1BER.setMaxAccess(_D)
if mibBuilder.loadTexts:zxDsx1BER.setStatus(_A)
class _ZxDsx1ClockStatusTrapEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_H,2)))
_ZxDsx1ClockStatusTrapEnable_Type.__name__=_B
_ZxDsx1ClockStatusTrapEnable_Object=MibTableColumn
zxDsx1ClockStatusTrapEnable=_ZxDsx1ClockStatusTrapEnable_Object((1,3,6,1,4,1,3902,1015,1013,2,1,1,1,1,31),_ZxDsx1ClockStatusTrapEnable_Type())
zxDsx1ClockStatusTrapEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:zxDsx1ClockStatusTrapEnable.setStatus(_A)
_ZxDsx1TrapObjects_ObjectIdentity=ObjectIdentity
zxDsx1TrapObjects=_ZxDsx1TrapObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,1013,2,1,100))
zxDsx1ClockStatusUnlock=NotificationType((1,3,6,1,4,1,3902,1015,1013,2,1,100,1))
zxDsx1ClockStatusUnlock.setObjects(*((_E,_F),(_E,_I)))
if mibBuilder.loadTexts:zxDsx1ClockStatusUnlock.setStatus(_A)
zxDsx1ClockStatusLock=NotificationType((1,3,6,1,4,1,3902,1015,1013,2,1,100,2))
zxDsx1ClockStatusLock.setObjects(*((_E,_F),(_E,_I)))
if mibBuilder.loadTexts:zxDsx1ClockStatusLock.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'zxDs1':zxDs1,'zxDsx1ConfigTable':zxDsx1ConfigTable,'zxDsx1ConfigEntry':zxDsx1ConfigEntry,_F:zxDsx1LineIndex,'zxDsx1IfIndex':zxDsx1IfIndex,'zxDsx1TimeElapsed':zxDsx1TimeElapsed,'zxDsx1ValidIntervals':zxDsx1ValidIntervals,'zxDsx1LineType':zxDsx1LineType,'zxDsx1LineCoding':zxDsx1LineCoding,'zxDsx1SendCode':zxDsx1SendCode,'zxDsx1CircuitIdentifier':zxDsx1CircuitIdentifier,'zxDsx1LoopbackConfig':zxDsx1LoopbackConfig,'zxDsx1LineStatus':zxDsx1LineStatus,'zxDsx1SignalMode':zxDsx1SignalMode,'zxDsx1TransmitClockSource':zxDsx1TransmitClockSource,'zxDsx1Fdl':zxDsx1Fdl,'zxDsx1InvalidIntervals':zxDsx1InvalidIntervals,'zxDsx1LineLength':zxDsx1LineLength,'zxDsx1LineStatusLastChange':zxDsx1LineStatusLastChange,'zxDsx1LineStatusChangeTrapEnable':zxDsx1LineStatusChangeTrapEnable,'zxDsx1LoopbackStatus':zxDsx1LoopbackStatus,'zxDsx1Ds1ChannelNumber':zxDsx1Ds1ChannelNumber,'zxDsx1Channelization':zxDsx1Channelization,'zxDsx1LineMode':zxDsx1LineMode,'zxDsx1LineBuildOut':zxDsx1LineBuildOut,'zxDsx1AdminStatus':zxDsx1AdminStatus,'zxDsx1OperStatus':zxDsx1OperStatus,_I:zxDsx1ClockStatus,'zxDsx1CfgInfoSend':zxDsx1CfgInfoSend,'zxDsx1Retiming':zxDsx1Retiming,'zxDsx1Impedance':zxDsx1Impedance,'zxDsx1FrameType':zxDsx1FrameType,'zxDsx1BER':zxDsx1BER,'zxDsx1ClockStatusTrapEnable':zxDsx1ClockStatusTrapEnable,'zxDsx1TrapObjects':zxDsx1TrapObjects,'zxDsx1ClockStatusUnlock':zxDsx1ClockStatusUnlock,'zxDsx1ClockStatusLock':zxDsx1ClockStatusLock})