_Z='hwVoDigitalIfR2ABCDCfgGroupNumber'
_Y='hwVoDigitalIfR2ABCDCfgPortNumber'
_X='minpoll'
_W='maxpoll'
_V='hwVoDigitalIfR2CfgGroupNumber'
_U='hwVoDigitalIfR2CfgPortNumber'
_T='hwVoDigitalIfEMTimerGroupNumber'
_S='hwVoDigitalIfEMTimerPortNumber'
_R='hwVoDigitalIfEMABCDCfgGroupNumber'
_Q='hwVoDigitalIfEMABCDCfgPortNumber'
_P='hwVoDigitalIfEMCfgGroupNumber'
_O='hwVoDigitalIfEMCfgPortNumber'
_N='hwVoDigitalIfCfgGroupNumber'
_M='hwVoDigitalIfCfgPortNumber'
_L='0101'
_K='1001'
_J='1101'
_I='disable'
_H='enable'
_G='deprecated'
_F='HUAWEI-VO-DIGITAL-IF-MIB'
_E='read-only'
_D='OctetString'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
voice,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','voice')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
hwVoiceDigitalInterfaceMIB=ModuleIdentity((1,3,6,1,4,1,2011,5,25,1,4))
if mibBuilder.loadTexts:hwVoiceDigitalInterfaceMIB.setRevisions(('2004-04-08 13:45',))
_HwVoDigitalIfCommonObjects_ObjectIdentity=ObjectIdentity
hwVoDigitalIfCommonObjects=_HwVoDigitalIfCommonObjects_ObjectIdentity((1,3,6,1,4,1,2011,5,25,1,4,1))
_HwVoDigitalIfCommonCfgTable_Object=MibTable
hwVoDigitalIfCommonCfgTable=_HwVoDigitalIfCommonCfgTable_Object((1,3,6,1,4,1,2011,5,25,1,4,1,1))
if mibBuilder.loadTexts:hwVoDigitalIfCommonCfgTable.setStatus(_A)
_HwVoDigitalIfCommonCfgEntry_Object=MibTableRow
hwVoDigitalIfCommonCfgEntry=_HwVoDigitalIfCommonCfgEntry_Object((1,3,6,1,4,1,2011,5,25,1,4,1,1,1))
hwVoDigitalIfCommonCfgEntry.setIndexNames((0,_F,_M),(0,_F,_N))
if mibBuilder.loadTexts:hwVoDigitalIfCommonCfgEntry.setStatus(_A)
_HwVoDigitalIfCfgPortNumber_Type=Integer32
_HwVoDigitalIfCfgPortNumber_Object=MibTableColumn
hwVoDigitalIfCfgPortNumber=_HwVoDigitalIfCfgPortNumber_Object((1,3,6,1,4,1,2011,5,25,1,4,1,1,1,1),_HwVoDigitalIfCfgPortNumber_Type())
hwVoDigitalIfCfgPortNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:hwVoDigitalIfCfgPortNumber.setStatus(_A)
class _HwVoDigitalIfCfgGroupNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,30))
_HwVoDigitalIfCfgGroupNumber_Type.__name__=_C
_HwVoDigitalIfCfgGroupNumber_Object=MibTableColumn
hwVoDigitalIfCfgGroupNumber=_HwVoDigitalIfCfgGroupNumber_Object((1,3,6,1,4,1,2011,5,25,1,4,1,1,1,2),_HwVoDigitalIfCfgGroupNumber_Type())
hwVoDigitalIfCfgGroupNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:hwVoDigitalIfCfgGroupNumber.setStatus(_A)
class _HwVoDigitalIfCfgBoardType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('e1vi',1),('t1vi',2)))
_HwVoDigitalIfCfgBoardType_Type.__name__=_C
_HwVoDigitalIfCfgBoardType_Object=MibTableColumn
hwVoDigitalIfCfgBoardType=_HwVoDigitalIfCfgBoardType_Object((1,3,6,1,4,1,2011,5,25,1,4,1,1,1,3),_HwVoDigitalIfCfgBoardType_Type())
hwVoDigitalIfCfgBoardType.setMaxAccess(_E)
if mibBuilder.loadTexts:hwVoDigitalIfCfgBoardType.setStatus(_A)
class _HwVoDigitalIfCfgSignalType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('r2',1),('dss1',2),('em',3)))
_HwVoDigitalIfCfgSignalType_Type.__name__=_C
_HwVoDigitalIfCfgSignalType_Object=MibTableColumn
hwVoDigitalIfCfgSignalType=_HwVoDigitalIfCfgSignalType_Object((1,3,6,1,4,1,2011,5,25,1,4,1,1,1,4),_HwVoDigitalIfCfgSignalType_Type())
hwVoDigitalIfCfgSignalType.setMaxAccess(_E)
if mibBuilder.loadTexts:hwVoDigitalIfCfgSignalType.setStatus(_A)
class _HwVoDigitalIfCfgTimeSlotsConfigurable_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(24,24),ValueSizeConstraint(32,32))
_HwVoDigitalIfCfgTimeSlotsConfigurable_Type.__name__=_D
_HwVoDigitalIfCfgTimeSlotsConfigurable_Object=MibTableColumn
hwVoDigitalIfCfgTimeSlotsConfigurable=_HwVoDigitalIfCfgTimeSlotsConfigurable_Object((1,3,6,1,4,1,2011,5,25,1,4,1,1,1,5),_HwVoDigitalIfCfgTimeSlotsConfigurable_Type())
hwVoDigitalIfCfgTimeSlotsConfigurable.setMaxAccess(_E)
if mibBuilder.loadTexts:hwVoDigitalIfCfgTimeSlotsConfigurable.setStatus(_A)
_HwVoDigitalIfEMObjects_ObjectIdentity=ObjectIdentity
hwVoDigitalIfEMObjects=_HwVoDigitalIfEMObjects_ObjectIdentity((1,3,6,1,4,1,2011,5,25,1,4,2))
_HwVoDigitalIfEMCfgTable_Object=MibTable
hwVoDigitalIfEMCfgTable=_HwVoDigitalIfEMCfgTable_Object((1,3,6,1,4,1,2011,5,25,1,4,2,1))
if mibBuilder.loadTexts:hwVoDigitalIfEMCfgTable.setStatus(_A)
_HwVoDigitalIfEMCfgEntry_Object=MibTableRow
hwVoDigitalIfEMCfgEntry=_HwVoDigitalIfEMCfgEntry_Object((1,3,6,1,4,1,2011,5,25,1,4,2,1,1))
hwVoDigitalIfEMCfgEntry.setIndexNames((0,_F,_O),(0,_F,_P))
if mibBuilder.loadTexts:hwVoDigitalIfEMCfgEntry.setStatus(_A)
_HwVoDigitalIfEMCfgPortNumber_Type=Integer32
_HwVoDigitalIfEMCfgPortNumber_Object=MibTableColumn
hwVoDigitalIfEMCfgPortNumber=_HwVoDigitalIfEMCfgPortNumber_Object((1,3,6,1,4,1,2011,5,25,1,4,2,1,1,1),_HwVoDigitalIfEMCfgPortNumber_Type())
hwVoDigitalIfEMCfgPortNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:hwVoDigitalIfEMCfgPortNumber.setStatus(_A)
class _HwVoDigitalIfEMCfgGroupNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,30))
_HwVoDigitalIfEMCfgGroupNumber_Type.__name__=_C
_HwVoDigitalIfEMCfgGroupNumber_Object=MibTableColumn
hwVoDigitalIfEMCfgGroupNumber=_HwVoDigitalIfEMCfgGroupNumber_Object((1,3,6,1,4,1,2011,5,25,1,4,2,1,1,2),_HwVoDigitalIfEMCfgGroupNumber_Type())
hwVoDigitalIfEMCfgGroupNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:hwVoDigitalIfEMCfgGroupNumber.setStatus(_A)
class _HwVoDigitalIfEMCfgTimeoutInterDigits_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,120))
_HwVoDigitalIfEMCfgTimeoutInterDigits_Type.__name__=_C
_HwVoDigitalIfEMCfgTimeoutInterDigits_Object=MibTableColumn
hwVoDigitalIfEMCfgTimeoutInterDigits=_HwVoDigitalIfEMCfgTimeoutInterDigits_Object((1,3,6,1,4,1,2011,5,25,1,4,2,1,1,3),_HwVoDigitalIfEMCfgTimeoutInterDigits_Type())
hwVoDigitalIfEMCfgTimeoutInterDigits.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoDigitalIfEMCfgTimeoutInterDigits.setStatus(_A)
class _HwVoDigitalIfEMCfgTimeoutRinging_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,600),ValueRangeConstraint(65535,65535))
_HwVoDigitalIfEMCfgTimeoutRinging_Type.__name__=_C
_HwVoDigitalIfEMCfgTimeoutRinging_Object=MibTableColumn
hwVoDigitalIfEMCfgTimeoutRinging=_HwVoDigitalIfEMCfgTimeoutRinging_Object((1,3,6,1,4,1,2011,5,25,1,4,2,1,1,4),_HwVoDigitalIfEMCfgTimeoutRinging_Type())
hwVoDigitalIfEMCfgTimeoutRinging.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoDigitalIfEMCfgTimeoutRinging.setStatus(_A)
class _HwVoDigitalIfEMCfgTimeoutWaitDigit_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,600),ValueRangeConstraint(65535,65535))
_HwVoDigitalIfEMCfgTimeoutWaitDigit_Type.__name__=_C
_HwVoDigitalIfEMCfgTimeoutWaitDigit_Object=MibTableColumn
hwVoDigitalIfEMCfgTimeoutWaitDigit=_HwVoDigitalIfEMCfgTimeoutWaitDigit_Object((1,3,6,1,4,1,2011,5,25,1,4,2,1,1,5),_HwVoDigitalIfEMCfgTimeoutWaitDigit_Type())
hwVoDigitalIfEMCfgTimeoutWaitDigit.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoDigitalIfEMCfgTimeoutWaitDigit.setStatus(_A)
_HwVoDigitalIfEMABCDCfgTable_Object=MibTable
hwVoDigitalIfEMABCDCfgTable=_HwVoDigitalIfEMABCDCfgTable_Object((1,3,6,1,4,1,2011,5,25,1,4,2,2))
if mibBuilder.loadTexts:hwVoDigitalIfEMABCDCfgTable.setStatus(_A)
_HwVoDigitalIfEMABCDCfgEntry_Object=MibTableRow
hwVoDigitalIfEMABCDCfgEntry=_HwVoDigitalIfEMABCDCfgEntry_Object((1,3,6,1,4,1,2011,5,25,1,4,2,2,1))
hwVoDigitalIfEMABCDCfgEntry.setIndexNames((0,_F,_Q),(0,_F,_R))
if mibBuilder.loadTexts:hwVoDigitalIfEMABCDCfgEntry.setStatus(_A)
_HwVoDigitalIfEMABCDCfgPortNumber_Type=Integer32
_HwVoDigitalIfEMABCDCfgPortNumber_Object=MibTableColumn
hwVoDigitalIfEMABCDCfgPortNumber=_HwVoDigitalIfEMABCDCfgPortNumber_Object((1,3,6,1,4,1,2011,5,25,1,4,2,2,1,1),_HwVoDigitalIfEMABCDCfgPortNumber_Type())
hwVoDigitalIfEMABCDCfgPortNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:hwVoDigitalIfEMABCDCfgPortNumber.setStatus(_A)
class _HwVoDigitalIfEMABCDCfgGroupNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,30))
_HwVoDigitalIfEMABCDCfgGroupNumber_Type.__name__=_C
_HwVoDigitalIfEMABCDCfgGroupNumber_Object=MibTableColumn
hwVoDigitalIfEMABCDCfgGroupNumber=_HwVoDigitalIfEMABCDCfgGroupNumber_Object((1,3,6,1,4,1,2011,5,25,1,4,2,2,1,2),_HwVoDigitalIfEMABCDCfgGroupNumber_Type())
hwVoDigitalIfEMABCDCfgGroupNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:hwVoDigitalIfEMABCDCfgGroupNumber.setStatus(_A)
class _HwVoDigitalIfEMABCDRxIdle_Type(OctetString):defaultValue=OctetString(_J);subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_HwVoDigitalIfEMABCDRxIdle_Type.__name__=_D
_HwVoDigitalIfEMABCDRxIdle_Object=MibTableColumn
hwVoDigitalIfEMABCDRxIdle=_HwVoDigitalIfEMABCDRxIdle_Object((1,3,6,1,4,1,2011,5,25,1,4,2,2,1,3),_HwVoDigitalIfEMABCDRxIdle_Type())
hwVoDigitalIfEMABCDRxIdle.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoDigitalIfEMABCDRxIdle.setStatus(_A)
class _HwVoDigitalIfEMABCDRxSeize_Type(OctetString):defaultValue=OctetString(_L);subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_HwVoDigitalIfEMABCDRxSeize_Type.__name__=_D
_HwVoDigitalIfEMABCDRxSeize_Object=MibTableColumn
hwVoDigitalIfEMABCDRxSeize=_HwVoDigitalIfEMABCDRxSeize_Object((1,3,6,1,4,1,2011,5,25,1,4,2,2,1,4),_HwVoDigitalIfEMABCDRxSeize_Type())
hwVoDigitalIfEMABCDRxSeize.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoDigitalIfEMABCDRxSeize.setStatus(_A)
class _HwVoDigitalIfEMABCDTxIdle_Type(OctetString):defaultValue=OctetString(_J);subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_HwVoDigitalIfEMABCDTxIdle_Type.__name__=_D
_HwVoDigitalIfEMABCDTxIdle_Object=MibTableColumn
hwVoDigitalIfEMABCDTxIdle=_HwVoDigitalIfEMABCDTxIdle_Object((1,3,6,1,4,1,2011,5,25,1,4,2,2,1,5),_HwVoDigitalIfEMABCDTxIdle_Type())
hwVoDigitalIfEMABCDTxIdle.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoDigitalIfEMABCDTxIdle.setStatus(_A)
class _HwVoDigitalIfEMABCDTxSeize_Type(OctetString):defaultValue=OctetString(_L);subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_HwVoDigitalIfEMABCDTxSeize_Type.__name__=_D
_HwVoDigitalIfEMABCDTxSeize_Object=MibTableColumn
hwVoDigitalIfEMABCDTxSeize=_HwVoDigitalIfEMABCDTxSeize_Object((1,3,6,1,4,1,2011,5,25,1,4,2,2,1,6),_HwVoDigitalIfEMABCDTxSeize_Type())
hwVoDigitalIfEMABCDTxSeize.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoDigitalIfEMABCDTxSeize.setStatus(_A)
_HwVoDigitalIfEMTimerTable_Object=MibTable
hwVoDigitalIfEMTimerTable=_HwVoDigitalIfEMTimerTable_Object((1,3,6,1,4,1,2011,5,25,1,4,2,4))
if mibBuilder.loadTexts:hwVoDigitalIfEMTimerTable.setStatus(_A)
_HwVoDigitalIfEMTimerEntry_Object=MibTableRow
hwVoDigitalIfEMTimerEntry=_HwVoDigitalIfEMTimerEntry_Object((1,3,6,1,4,1,2011,5,25,1,4,2,4,1))
hwVoDigitalIfEMTimerEntry.setIndexNames((0,_F,_S),(0,_F,_T))
if mibBuilder.loadTexts:hwVoDigitalIfEMTimerEntry.setStatus(_A)
_HwVoDigitalIfEMTimerPortNumber_Type=Integer32
_HwVoDigitalIfEMTimerPortNumber_Object=MibTableColumn
hwVoDigitalIfEMTimerPortNumber=_HwVoDigitalIfEMTimerPortNumber_Object((1,3,6,1,4,1,2011,5,25,1,4,2,4,1,1),_HwVoDigitalIfEMTimerPortNumber_Type())
hwVoDigitalIfEMTimerPortNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:hwVoDigitalIfEMTimerPortNumber.setStatus(_A)
class _HwVoDigitalIfEMTimerGroupNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,30))
_HwVoDigitalIfEMTimerGroupNumber_Type.__name__=_C
_HwVoDigitalIfEMTimerGroupNumber_Object=MibTableColumn
hwVoDigitalIfEMTimerGroupNumber=_HwVoDigitalIfEMTimerGroupNumber_Object((1,3,6,1,4,1,2011,5,25,1,4,2,4,1,2),_HwVoDigitalIfEMTimerGroupNumber_Type())
hwVoDigitalIfEMTimerGroupNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:hwVoDigitalIfEMTimerGroupNumber.setStatus(_A)
class _HwVoDigitalIfEMTimerCallInterval_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(200,2000))
_HwVoDigitalIfEMTimerCallInterval_Type.__name__=_C
_HwVoDigitalIfEMTimerCallInterval_Object=MibTableColumn
hwVoDigitalIfEMTimerCallInterval=_HwVoDigitalIfEMTimerCallInterval_Object((1,3,6,1,4,1,2011,5,25,1,4,2,4,1,3),_HwVoDigitalIfEMTimerCallInterval_Type())
hwVoDigitalIfEMTimerCallInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoDigitalIfEMTimerCallInterval.setStatus(_A)
class _HwVoDigitalIfEMTimerSendWink_Type(Integer32):defaultValue=500;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,5000))
_HwVoDigitalIfEMTimerSendWink_Type.__name__=_C
_HwVoDigitalIfEMTimerSendWink_Object=MibTableColumn
hwVoDigitalIfEMTimerSendWink=_HwVoDigitalIfEMTimerSendWink_Object((1,3,6,1,4,1,2011,5,25,1,4,2,4,1,4),_HwVoDigitalIfEMTimerSendWink_Type())
hwVoDigitalIfEMTimerSendWink.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoDigitalIfEMTimerSendWink.setStatus(_A)
class _HwVoDigitalIfEMTimerWinkRising_Type(Integer32):defaultValue=1000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,5000))
_HwVoDigitalIfEMTimerWinkRising_Type.__name__=_C
_HwVoDigitalIfEMTimerWinkRising_Object=MibTableColumn
hwVoDigitalIfEMTimerWinkRising=_HwVoDigitalIfEMTimerWinkRising_Object((1,3,6,1,4,1,2011,5,25,1,4,2,4,1,5),_HwVoDigitalIfEMTimerWinkRising_Type())
hwVoDigitalIfEMTimerWinkRising.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoDigitalIfEMTimerWinkRising.setStatus(_A)
class _HwVoDigitalIfEMTimerWinkHold_Type(Integer32):defaultValue=500;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,3000))
_HwVoDigitalIfEMTimerWinkHold_Type.__name__=_C
_HwVoDigitalIfEMTimerWinkHold_Object=MibTableColumn
hwVoDigitalIfEMTimerWinkHold=_HwVoDigitalIfEMTimerWinkHold_Object((1,3,6,1,4,1,2011,5,25,1,4,2,4,1,6),_HwVoDigitalIfEMTimerWinkHold_Type())
hwVoDigitalIfEMTimerWinkHold.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoDigitalIfEMTimerWinkHold.setStatus(_A)
class _HwVoDigitalIfEMTimerDialoutDelay_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(50,5000))
_HwVoDigitalIfEMTimerDialoutDelay_Type.__name__=_C
_HwVoDigitalIfEMTimerDialoutDelay_Object=MibTableColumn
hwVoDigitalIfEMTimerDialoutDelay=_HwVoDigitalIfEMTimerDialoutDelay_Object((1,3,6,1,4,1,2011,5,25,1,4,2,4,1,7),_HwVoDigitalIfEMTimerDialoutDelay_Type())
hwVoDigitalIfEMTimerDialoutDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoDigitalIfEMTimerDialoutDelay.setStatus(_A)
class _HwVoDigitalIfEMTimerRising_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(20,2000))
_HwVoDigitalIfEMTimerRising_Type.__name__=_C
_HwVoDigitalIfEMTimerRising_Object=MibTableColumn
hwVoDigitalIfEMTimerRising=_HwVoDigitalIfEMTimerRising_Object((1,3,6,1,4,1,2011,5,25,1,4,2,4,1,8),_HwVoDigitalIfEMTimerRising_Type())
hwVoDigitalIfEMTimerRising.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoDigitalIfEMTimerRising.setStatus(_A)
class _HwVoDigitalIfEMTimerHold_Type(Integer32):defaultValue=400;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,5000))
_HwVoDigitalIfEMTimerHold_Type.__name__=_C
_HwVoDigitalIfEMTimerHold_Object=MibTableColumn
hwVoDigitalIfEMTimerHold=_HwVoDigitalIfEMTimerHold_Object((1,3,6,1,4,1,2011,5,25,1,4,2,4,1,9),_HwVoDigitalIfEMTimerHold_Type())
hwVoDigitalIfEMTimerHold.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoDigitalIfEMTimerHold.setStatus(_A)
class _HwVoDigitalIfEMTimerDtmf_Type(Integer32):defaultValue=120;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(50,500))
_HwVoDigitalIfEMTimerDtmf_Type.__name__=_C
_HwVoDigitalIfEMTimerDtmf_Object=MibTableColumn
hwVoDigitalIfEMTimerDtmf=_HwVoDigitalIfEMTimerDtmf_Object((1,3,6,1,4,1,2011,5,25,1,4,2,4,1,10),_HwVoDigitalIfEMTimerDtmf_Type())
hwVoDigitalIfEMTimerDtmf.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoDigitalIfEMTimerDtmf.setStatus(_A)
class _HwVoDigitalIfEMTimerDtmfInterval_Type(Integer32):defaultValue=120;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(50,500))
_HwVoDigitalIfEMTimerDtmfInterval_Type.__name__=_C
_HwVoDigitalIfEMTimerDtmfInterval_Object=MibTableColumn
hwVoDigitalIfEMTimerDtmfInterval=_HwVoDigitalIfEMTimerDtmfInterval_Object((1,3,6,1,4,1,2011,5,25,1,4,2,4,1,11),_HwVoDigitalIfEMTimerDtmfInterval_Type())
hwVoDigitalIfEMTimerDtmfInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoDigitalIfEMTimerDtmfInterval.setStatus(_A)
_HwVoDigitalIfR2Objects_ObjectIdentity=ObjectIdentity
hwVoDigitalIfR2Objects=_HwVoDigitalIfR2Objects_ObjectIdentity((1,3,6,1,4,1,2011,5,25,1,4,3))
_HwVoDigitalIfR2CfgTable_Object=MibTable
hwVoDigitalIfR2CfgTable=_HwVoDigitalIfR2CfgTable_Object((1,3,6,1,4,1,2011,5,25,1,4,3,1))
if mibBuilder.loadTexts:hwVoDigitalIfR2CfgTable.setStatus(_A)
_HwVoDigitalIfR2CfgEntry_Object=MibTableRow
hwVoDigitalIfR2CfgEntry=_HwVoDigitalIfR2CfgEntry_Object((1,3,6,1,4,1,2011,5,25,1,4,3,1,1))
hwVoDigitalIfR2CfgEntry.setIndexNames((0,_F,_U),(0,_F,_V))
if mibBuilder.loadTexts:hwVoDigitalIfR2CfgEntry.setStatus(_A)
_HwVoDigitalIfR2CfgPortNumber_Type=Integer32
_HwVoDigitalIfR2CfgPortNumber_Object=MibTableColumn
hwVoDigitalIfR2CfgPortNumber=_HwVoDigitalIfR2CfgPortNumber_Object((1,3,6,1,4,1,2011,5,25,1,4,3,1,1,1),_HwVoDigitalIfR2CfgPortNumber_Type())
hwVoDigitalIfR2CfgPortNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:hwVoDigitalIfR2CfgPortNumber.setStatus(_A)
class _HwVoDigitalIfR2CfgGroupNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,30))
_HwVoDigitalIfR2CfgGroupNumber_Type.__name__=_C
_HwVoDigitalIfR2CfgGroupNumber_Object=MibTableColumn
hwVoDigitalIfR2CfgGroupNumber=_HwVoDigitalIfR2CfgGroupNumber_Object((1,3,6,1,4,1,2011,5,25,1,4,3,1,1,2),_HwVoDigitalIfR2CfgGroupNumber_Type())
hwVoDigitalIfR2CfgGroupNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:hwVoDigitalIfR2CfgGroupNumber.setStatus(_A)
class _HwVoDigitalIfR2CfgAniSwitch_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_HwVoDigitalIfR2CfgAniSwitch_Type.__name__=_C
_HwVoDigitalIfR2CfgAniSwitch_Object=MibTableColumn
hwVoDigitalIfR2CfgAniSwitch=_HwVoDigitalIfR2CfgAniSwitch_Object((1,3,6,1,4,1,2011,5,25,1,4,3,1,1,3),_HwVoDigitalIfR2CfgAniSwitch_Type())
hwVoDigitalIfR2CfgAniSwitch.setMaxAccess(_E)
if mibBuilder.loadTexts:hwVoDigitalIfR2CfgAniSwitch.setStatus(_G)
class _HwVoDigitalIfR2CallerDigits_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_HwVoDigitalIfR2CallerDigits_Type.__name__=_C
_HwVoDigitalIfR2CallerDigits_Object=MibTableColumn
hwVoDigitalIfR2CallerDigits=_HwVoDigitalIfR2CallerDigits_Object((1,3,6,1,4,1,2011,5,25,1,4,3,1,1,4),_HwVoDigitalIfR2CallerDigits_Type())
hwVoDigitalIfR2CallerDigits.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoDigitalIfR2CallerDigits.setStatus(_G)
class _HwVoDigitalIfR2DebounceTime_Type(Integer32):defaultValue=40;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,40))
_HwVoDigitalIfR2DebounceTime_Type.__name__=_C
_HwVoDigitalIfR2DebounceTime_Object=MibTableColumn
hwVoDigitalIfR2DebounceTime=_HwVoDigitalIfR2DebounceTime_Object((1,3,6,1,4,1,2011,5,25,1,4,3,1,1,5),_HwVoDigitalIfR2DebounceTime_Type())
hwVoDigitalIfR2DebounceTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoDigitalIfR2DebounceTime.setStatus(_G)
class _HwVoDigitalIfR2Ka_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_HwVoDigitalIfR2Ka_Type.__name__=_C
_HwVoDigitalIfR2Ka_Object=MibTableColumn
hwVoDigitalIfR2Ka=_HwVoDigitalIfR2Ka_Object((1,3,6,1,4,1,2011,5,25,1,4,3,1,1,6),_HwVoDigitalIfR2Ka_Type())
hwVoDigitalIfR2Ka.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoDigitalIfR2Ka.setStatus(_G)
class _HwVoDigitalIfR2Kd_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_HwVoDigitalIfR2Kd_Type.__name__=_C
_HwVoDigitalIfR2Kd_Object=MibTableColumn
hwVoDigitalIfR2Kd=_HwVoDigitalIfR2Kd_Object((1,3,6,1,4,1,2011,5,25,1,4,3,1,1,7),_HwVoDigitalIfR2Kd_Type())
hwVoDigitalIfR2Kd.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoDigitalIfR2Kd.setStatus(_G)
class _HwVoDigitalIfR2SeizureAckTime_Type(Integer32):defaultValue=1000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(200,3000))
_HwVoDigitalIfR2SeizureAckTime_Type.__name__=_C
_HwVoDigitalIfR2SeizureAckTime_Object=MibTableColumn
hwVoDigitalIfR2SeizureAckTime=_HwVoDigitalIfR2SeizureAckTime_Object((1,3,6,1,4,1,2011,5,25,1,4,3,1,1,8),_HwVoDigitalIfR2SeizureAckTime_Type())
hwVoDigitalIfR2SeizureAckTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoDigitalIfR2SeizureAckTime.setStatus(_G)
class _HwVoDigitalIfR2SelectMode_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('max',1),(_W,2),('min',3),(_X,4)))
_HwVoDigitalIfR2SelectMode_Type.__name__=_C
_HwVoDigitalIfR2SelectMode_Object=MibTableColumn
hwVoDigitalIfR2SelectMode=_HwVoDigitalIfR2SelectMode_Object((1,3,6,1,4,1,2011,5,25,1,4,3,1,1,9),_HwVoDigitalIfR2SelectMode_Type())
hwVoDigitalIfR2SelectMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoDigitalIfR2SelectMode.setStatus(_G)
class _HwVoDigitalIfR2TimeoutKb_Type(Integer32):defaultValue=5000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1000,50000))
_HwVoDigitalIfR2TimeoutKb_Type.__name__=_C
_HwVoDigitalIfR2TimeoutKb_Object=MibTableColumn
hwVoDigitalIfR2TimeoutKb=_HwVoDigitalIfR2TimeoutKb_Object((1,3,6,1,4,1,2011,5,25,1,4,3,1,1,10),_HwVoDigitalIfR2TimeoutKb_Type())
hwVoDigitalIfR2TimeoutKb.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoDigitalIfR2TimeoutKb.setStatus(_G)
class _HwVoDigitalIfR2TimeoutKd_Type(Integer32):defaultValue=5000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1000,50000))
_HwVoDigitalIfR2TimeoutKd_Type.__name__=_C
_HwVoDigitalIfR2TimeoutKd_Object=MibTableColumn
hwVoDigitalIfR2TimeoutKd=_HwVoDigitalIfR2TimeoutKd_Object((1,3,6,1,4,1,2011,5,25,1,4,3,1,1,11),_HwVoDigitalIfR2TimeoutKd_Type())
hwVoDigitalIfR2TimeoutKd.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoDigitalIfR2TimeoutKd.setStatus(_G)
class _HwVoDigitalIfR2TimeoutNextNumber_Type(Integer32):defaultValue=5000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1000,50000))
_HwVoDigitalIfR2TimeoutNextNumber_Type.__name__=_C
_HwVoDigitalIfR2TimeoutNextNumber_Object=MibTableColumn
hwVoDigitalIfR2TimeoutNextNumber=_HwVoDigitalIfR2TimeoutNextNumber_Object((1,3,6,1,4,1,2011,5,25,1,4,3,1,1,12),_HwVoDigitalIfR2TimeoutNextNumber_Type())
hwVoDigitalIfR2TimeoutNextNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoDigitalIfR2TimeoutNextNumber.setStatus(_G)
class _HwVoDigitalIfR2TimeoutReleaseApprove_Type(Integer32):defaultValue=1000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(200,3000))
_HwVoDigitalIfR2TimeoutReleaseApprove_Type.__name__=_C
_HwVoDigitalIfR2TimeoutReleaseApprove_Object=MibTableColumn
hwVoDigitalIfR2TimeoutReleaseApprove=_HwVoDigitalIfR2TimeoutReleaseApprove_Object((1,3,6,1,4,1,2011,5,25,1,4,3,1,1,13),_HwVoDigitalIfR2TimeoutReleaseApprove_Type())
hwVoDigitalIfR2TimeoutReleaseApprove.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoDigitalIfR2TimeoutReleaseApprove.setStatus(_G)
class _HwVoDigitalIfR2TimeoutRing_Type(Integer32):defaultValue=30000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1000,240000))
_HwVoDigitalIfR2TimeoutRing_Type.__name__=_C
_HwVoDigitalIfR2TimeoutRing_Object=MibTableColumn
hwVoDigitalIfR2TimeoutRing=_HwVoDigitalIfR2TimeoutRing_Object((1,3,6,1,4,1,2011,5,25,1,4,3,1,1,14),_HwVoDigitalIfR2TimeoutRing_Type())
hwVoDigitalIfR2TimeoutRing.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoDigitalIfR2TimeoutRing.setStatus(_G)
class _HwVoDigitalIfR2TimeoutSendAnswer_Type(Integer32):defaultValue=500;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(50,1000))
_HwVoDigitalIfR2TimeoutSendAnswer_Type.__name__=_C
_HwVoDigitalIfR2TimeoutSendAnswer_Object=MibTableColumn
hwVoDigitalIfR2TimeoutSendAnswer=_HwVoDigitalIfR2TimeoutSendAnswer_Object((1,3,6,1,4,1,2011,5,25,1,4,3,1,1,15),_HwVoDigitalIfR2TimeoutSendAnswer_Type())
hwVoDigitalIfR2TimeoutSendAnswer.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoDigitalIfR2TimeoutSendAnswer.setStatus(_G)
class _HwVoDigitalIfR2CfgBillingCategory_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_HwVoDigitalIfR2CfgBillingCategory_Type.__name__=_C
_HwVoDigitalIfR2CfgBillingCategory_Object=MibTableColumn
hwVoDigitalIfR2CfgBillingCategory=_HwVoDigitalIfR2CfgBillingCategory_Object((1,3,6,1,4,1,2011,5,25,1,4,3,1,1,16),_HwVoDigitalIfR2CfgBillingCategory_Type())
hwVoDigitalIfR2CfgBillingCategory.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoDigitalIfR2CfgBillingCategory.setStatus(_A)
class _HwVoDigitalIfR2CfgCallingCategory_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_HwVoDigitalIfR2CfgCallingCategory_Type.__name__=_C
_HwVoDigitalIfR2CfgCallingCategory_Object=MibTableColumn
hwVoDigitalIfR2CfgCallingCategory=_HwVoDigitalIfR2CfgCallingCategory_Object((1,3,6,1,4,1,2011,5,25,1,4,3,1,1,17),_HwVoDigitalIfR2CfgCallingCategory_Type())
hwVoDigitalIfR2CfgCallingCategory.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoDigitalIfR2CfgCallingCategory.setStatus(_A)
class _HwVoDigitalIfR2CfgCongestion_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_HwVoDigitalIfR2CfgCongestion_Type.__name__=_C
_HwVoDigitalIfR2CfgCongestion_Object=MibTableColumn
hwVoDigitalIfR2CfgCongestion=_HwVoDigitalIfR2CfgCongestion_Object((1,3,6,1,4,1,2011,5,25,1,4,3,1,1,18),_HwVoDigitalIfR2CfgCongestion_Type())
hwVoDigitalIfR2CfgCongestion.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoDigitalIfR2CfgCongestion.setStatus(_A)
class _HwVoDigitalIfR2CfgDemandRefused_Type(Integer32):defaultValue=12;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_HwVoDigitalIfR2CfgDemandRefused_Type.__name__=_C
_HwVoDigitalIfR2CfgDemandRefused_Object=MibTableColumn
hwVoDigitalIfR2CfgDemandRefused=_HwVoDigitalIfR2CfgDemandRefused_Object((1,3,6,1,4,1,2011,5,25,1,4,3,1,1,19),_HwVoDigitalIfR2CfgDemandRefused_Type())
hwVoDigitalIfR2CfgDemandRefused.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoDigitalIfR2CfgDemandRefused.setStatus(_A)
class _HwVoDigitalIfR2CfgDigitEnd_Type(Integer32):defaultValue=15;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_HwVoDigitalIfR2CfgDigitEnd_Type.__name__=_C
_HwVoDigitalIfR2CfgDigitEnd_Object=MibTableColumn
hwVoDigitalIfR2CfgDigitEnd=_HwVoDigitalIfR2CfgDigitEnd_Object((1,3,6,1,4,1,2011,5,25,1,4,3,1,1,20),_HwVoDigitalIfR2CfgDigitEnd_Type())
hwVoDigitalIfR2CfgDigitEnd.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoDigitalIfR2CfgDigitEnd.setStatus(_A)
class _HwVoDigitalIfR2CfgNullnum_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_HwVoDigitalIfR2CfgNullnum_Type.__name__=_C
_HwVoDigitalIfR2CfgNullnum_Object=MibTableColumn
hwVoDigitalIfR2CfgNullnum=_HwVoDigitalIfR2CfgNullnum_Object((1,3,6,1,4,1,2011,5,25,1,4,3,1,1,21),_HwVoDigitalIfR2CfgNullnum_Type())
hwVoDigitalIfR2CfgNullnum.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoDigitalIfR2CfgNullnum.setStatus(_A)
class _HwVoDigitalIfR2CfgReqBillingCategory_Type(Integer32):defaultValue=16;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_HwVoDigitalIfR2CfgReqBillingCategory_Type.__name__=_C
_HwVoDigitalIfR2CfgReqBillingCategory_Object=MibTableColumn
hwVoDigitalIfR2CfgReqBillingCategory=_HwVoDigitalIfR2CfgReqBillingCategory_Object((1,3,6,1,4,1,2011,5,25,1,4,3,1,1,22),_HwVoDigitalIfR2CfgReqBillingCategory_Type())
hwVoDigitalIfR2CfgReqBillingCategory.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoDigitalIfR2CfgReqBillingCategory.setStatus(_A)
class _HwVoDigitalIfR2CfgReqCallingCategory_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_HwVoDigitalIfR2CfgReqCallingCategory_Type.__name__=_C
_HwVoDigitalIfR2CfgReqCallingCategory_Object=MibTableColumn
hwVoDigitalIfR2CfgReqCallingCategory=_HwVoDigitalIfR2CfgReqCallingCategory_Object((1,3,6,1,4,1,2011,5,25,1,4,3,1,1,23),_HwVoDigitalIfR2CfgReqCallingCategory_Type())
hwVoDigitalIfR2CfgReqCallingCategory.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoDigitalIfR2CfgReqCallingCategory.setStatus(_A)
class _HwVoDigitalIfR2CfgReqCurrentdigit_Type(Integer32):defaultValue=16;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_HwVoDigitalIfR2CfgReqCurrentdigit_Type.__name__=_C
_HwVoDigitalIfR2CfgReqCurrentdigit_Object=MibTableColumn
hwVoDigitalIfR2CfgReqCurrentdigit=_HwVoDigitalIfR2CfgReqCurrentdigit_Object((1,3,6,1,4,1,2011,5,25,1,4,3,1,1,24),_HwVoDigitalIfR2CfgReqCurrentdigit_Type())
hwVoDigitalIfR2CfgReqCurrentdigit.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoDigitalIfR2CfgReqCurrentdigit.setStatus(_A)
class _HwVoDigitalIfR2CfgReqFirstCallingnum_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_HwVoDigitalIfR2CfgReqFirstCallingnum_Type.__name__=_C
_HwVoDigitalIfR2CfgReqFirstCallingnum_Object=MibTableColumn
hwVoDigitalIfR2CfgReqFirstCallingnum=_HwVoDigitalIfR2CfgReqFirstCallingnum_Object((1,3,6,1,4,1,2011,5,25,1,4,3,1,1,25),_HwVoDigitalIfR2CfgReqFirstCallingnum_Type())
hwVoDigitalIfR2CfgReqFirstCallingnum.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoDigitalIfR2CfgReqFirstCallingnum.setStatus(_A)
class _HwVoDigitalIfR2CfgReqFirstDigit_Type(Integer32):defaultValue=16;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_HwVoDigitalIfR2CfgReqFirstDigit_Type.__name__=_C
_HwVoDigitalIfR2CfgReqFirstDigit_Object=MibTableColumn
hwVoDigitalIfR2CfgReqFirstDigit=_HwVoDigitalIfR2CfgReqFirstDigit_Object((1,3,6,1,4,1,2011,5,25,1,4,3,1,1,26),_HwVoDigitalIfR2CfgReqFirstDigit_Type())
hwVoDigitalIfR2CfgReqFirstDigit.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoDigitalIfR2CfgReqFirstDigit.setStatus(_A)
class _HwVoDigitalIfR2CfgReqNextCallednum_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_HwVoDigitalIfR2CfgReqNextCallednum_Type.__name__=_C
_HwVoDigitalIfR2CfgReqNextCallednum_Object=MibTableColumn
hwVoDigitalIfR2CfgReqNextCallednum=_HwVoDigitalIfR2CfgReqNextCallednum_Object((1,3,6,1,4,1,2011,5,25,1,4,3,1,1,27),_HwVoDigitalIfR2CfgReqNextCallednum_Type())
hwVoDigitalIfR2CfgReqNextCallednum.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoDigitalIfR2CfgReqNextCallednum.setStatus(_A)
class _HwVoDigitalIfR2CfgReqNextCallingnum_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_HwVoDigitalIfR2CfgReqNextCallingnum_Type.__name__=_C
_HwVoDigitalIfR2CfgReqNextCallingnum_Object=MibTableColumn
hwVoDigitalIfR2CfgReqNextCallingnum=_HwVoDigitalIfR2CfgReqNextCallingnum_Object((1,3,6,1,4,1,2011,5,25,1,4,3,1,1,28),_HwVoDigitalIfR2CfgReqNextCallingnum_Type())
hwVoDigitalIfR2CfgReqNextCallingnum.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoDigitalIfR2CfgReqNextCallingnum.setStatus(_A)
class _HwVoDigitalIfR2CfgReqLastFirstDigit_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_HwVoDigitalIfR2CfgReqLastFirstDigit_Type.__name__=_C
_HwVoDigitalIfR2CfgReqLastFirstDigit_Object=MibTableColumn
hwVoDigitalIfR2CfgReqLastFirstDigit=_HwVoDigitalIfR2CfgReqLastFirstDigit_Object((1,3,6,1,4,1,2011,5,25,1,4,3,1,1,29),_HwVoDigitalIfR2CfgReqLastFirstDigit_Type())
hwVoDigitalIfR2CfgReqLastFirstDigit.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoDigitalIfR2CfgReqLastFirstDigit.setStatus(_A)
class _HwVoDigitalIfR2CfgReqLastSecondDigit_Type(Integer32):defaultValue=7;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_HwVoDigitalIfR2CfgReqLastSecondDigit_Type.__name__=_C
_HwVoDigitalIfR2CfgReqLastSecondDigit_Object=MibTableColumn
hwVoDigitalIfR2CfgReqLastSecondDigit=_HwVoDigitalIfR2CfgReqLastSecondDigit_Object((1,3,6,1,4,1,2011,5,25,1,4,3,1,1,30),_HwVoDigitalIfR2CfgReqLastSecondDigit_Type())
hwVoDigitalIfR2CfgReqLastSecondDigit.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoDigitalIfR2CfgReqLastSecondDigit.setStatus(_A)
class _HwVoDigitalIfR2CfgReqLastThirdDigit_Type(Integer32):defaultValue=8;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_HwVoDigitalIfR2CfgReqLastThirdDigit_Type.__name__=_C
_HwVoDigitalIfR2CfgReqLastThirdDigit_Object=MibTableColumn
hwVoDigitalIfR2CfgReqLastThirdDigit=_HwVoDigitalIfR2CfgReqLastThirdDigit_Object((1,3,6,1,4,1,2011,5,25,1,4,3,1,1,31),_HwVoDigitalIfR2CfgReqLastThirdDigit_Type())
hwVoDigitalIfR2CfgReqLastThirdDigit.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoDigitalIfR2CfgReqLastThirdDigit.setStatus(_A)
class _HwVoDigitalIfR2CfgReqSwitchGroupB_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_HwVoDigitalIfR2CfgReqSwitchGroupB_Type.__name__=_C
_HwVoDigitalIfR2CfgReqSwitchGroupB_Object=MibTableColumn
hwVoDigitalIfR2CfgReqSwitchGroupB=_HwVoDigitalIfR2CfgReqSwitchGroupB_Object((1,3,6,1,4,1,2011,5,25,1,4,3,1,1,32),_HwVoDigitalIfR2CfgReqSwitchGroupB_Type())
hwVoDigitalIfR2CfgReqSwitchGroupB.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoDigitalIfR2CfgReqSwitchGroupB.setStatus(_A)
class _HwVoDigitalIfR2CfgSubscriberIdle_Type(Integer32):defaultValue=6;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_HwVoDigitalIfR2CfgSubscriberIdle_Type.__name__=_C
_HwVoDigitalIfR2CfgSubscriberIdle_Object=MibTableColumn
hwVoDigitalIfR2CfgSubscriberIdle=_HwVoDigitalIfR2CfgSubscriberIdle_Object((1,3,6,1,4,1,2011,5,25,1,4,3,1,1,33),_HwVoDigitalIfR2CfgSubscriberIdle_Type())
hwVoDigitalIfR2CfgSubscriberIdle.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoDigitalIfR2CfgSubscriberIdle.setStatus(_A)
class _HwVoDigitalIfR2CfgSubscriberBusy_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_HwVoDigitalIfR2CfgSubscriberBusy_Type.__name__=_C
_HwVoDigitalIfR2CfgSubscriberBusy_Object=MibTableColumn
hwVoDigitalIfR2CfgSubscriberBusy=_HwVoDigitalIfR2CfgSubscriberBusy_Object((1,3,6,1,4,1,2011,5,25,1,4,3,1,1,34),_HwVoDigitalIfR2CfgSubscriberBusy_Type())
hwVoDigitalIfR2CfgSubscriberBusy.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoDigitalIfR2CfgSubscriberBusy.setStatus(_A)
class _HwVoDigitalIfR2CfgDebounceTime_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,40))
_HwVoDigitalIfR2CfgDebounceTime_Type.__name__=_C
_HwVoDigitalIfR2CfgDebounceTime_Object=MibTableColumn
hwVoDigitalIfR2CfgDebounceTime=_HwVoDigitalIfR2CfgDebounceTime_Object((1,3,6,1,4,1,2011,5,25,1,4,3,1,1,35),_HwVoDigitalIfR2CfgDebounceTime_Type())
hwVoDigitalIfR2CfgDebounceTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoDigitalIfR2CfgDebounceTime.setStatus(_A)
class _HwVoDigitalIfR2CfgSendringBackTime_Type(Integer32):defaultValue=60000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1000,90000))
_HwVoDigitalIfR2CfgSendringBackTime_Type.__name__=_C
_HwVoDigitalIfR2CfgSendringBackTime_Object=MibTableColumn
hwVoDigitalIfR2CfgSendringBackTime=_HwVoDigitalIfR2CfgSendringBackTime_Object((1,3,6,1,4,1,2011,5,25,1,4,3,1,1,36),_HwVoDigitalIfR2CfgSendringBackTime_Type())
hwVoDigitalIfR2CfgSendringBackTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoDigitalIfR2CfgSendringBackTime.setStatus(_A)
class _HwVoDigitalIfR2CfgSendringBusyTime_Type(Integer32):defaultValue=30000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1000,90000))
_HwVoDigitalIfR2CfgSendringBusyTime_Type.__name__=_C
_HwVoDigitalIfR2CfgSendringBusyTime_Object=MibTableColumn
hwVoDigitalIfR2CfgSendringBusyTime=_HwVoDigitalIfR2CfgSendringBusyTime_Object((1,3,6,1,4,1,2011,5,25,1,4,3,1,1,37),_HwVoDigitalIfR2CfgSendringBusyTime_Type())
hwVoDigitalIfR2CfgSendringBusyTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoDigitalIfR2CfgSendringBusyTime.setStatus(_A)
class _HwVoDigitalIfR2CfgPulseSignalPersistenceTime_Type(Integer32):defaultValue=150;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(50,3000))
_HwVoDigitalIfR2CfgPulseSignalPersistenceTime_Type.__name__=_C
_HwVoDigitalIfR2CfgPulseSignalPersistenceTime_Object=MibTableColumn
hwVoDigitalIfR2CfgPulseSignalPersistenceTime=_HwVoDigitalIfR2CfgPulseSignalPersistenceTime_Object((1,3,6,1,4,1,2011,5,25,1,4,3,1,1,38),_HwVoDigitalIfR2CfgPulseSignalPersistenceTime_Type())
hwVoDigitalIfR2CfgPulseSignalPersistenceTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoDigitalIfR2CfgPulseSignalPersistenceTime.setStatus(_A)
class _HwVoDigitalIfR2CfgDlAnswerTime_Type(Integer32):defaultValue=60000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,120000))
_HwVoDigitalIfR2CfgDlAnswerTime_Type.__name__=_C
_HwVoDigitalIfR2CfgDlAnswerTime_Object=MibTableColumn
hwVoDigitalIfR2CfgDlAnswerTime=_HwVoDigitalIfR2CfgDlAnswerTime_Object((1,3,6,1,4,1,2011,5,25,1,4,3,1,1,39),_HwVoDigitalIfR2CfgDlAnswerTime_Type())
hwVoDigitalIfR2CfgDlAnswerTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoDigitalIfR2CfgDlAnswerTime.setStatus(_A)
class _HwVoDigitalIfR2CfgDlClearBackTime_Type(Integer32):defaultValue=1000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,60000))
_HwVoDigitalIfR2CfgDlClearBackTime_Type.__name__=_C
_HwVoDigitalIfR2CfgDlClearBackTime_Object=MibTableColumn
hwVoDigitalIfR2CfgDlClearBackTime=_HwVoDigitalIfR2CfgDlClearBackTime_Object((1,3,6,1,4,1,2011,5,25,1,4,3,1,1,40),_HwVoDigitalIfR2CfgDlClearBackTime_Type())
hwVoDigitalIfR2CfgDlClearBackTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoDigitalIfR2CfgDlClearBackTime.setStatus(_A)
class _HwVoDigitalIfR2CfgDlClearForwardTime_Type(Integer32):defaultValue=1000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,60000))
_HwVoDigitalIfR2CfgDlClearForwardTime_Type.__name__=_C
_HwVoDigitalIfR2CfgDlClearForwardTime_Object=MibTableColumn
hwVoDigitalIfR2CfgDlClearForwardTime=_HwVoDigitalIfR2CfgDlClearForwardTime_Object((1,3,6,1,4,1,2011,5,25,1,4,3,1,1,41),_HwVoDigitalIfR2CfgDlClearForwardTime_Type())
hwVoDigitalIfR2CfgDlClearForwardTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoDigitalIfR2CfgDlClearForwardTime.setStatus(_A)
class _HwVoDigitalIfR2CfgDlSeizureTime_Type(Integer32):defaultValue=1000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,5000))
_HwVoDigitalIfR2CfgDlSeizureTime_Type.__name__=_C
_HwVoDigitalIfR2CfgDlSeizureTime_Object=MibTableColumn
hwVoDigitalIfR2CfgDlSeizureTime=_HwVoDigitalIfR2CfgDlSeizureTime_Object((1,3,6,1,4,1,2011,5,25,1,4,3,1,1,42),_HwVoDigitalIfR2CfgDlSeizureTime_Type())
hwVoDigitalIfR2CfgDlSeizureTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoDigitalIfR2CfgDlSeizureTime.setStatus(_A)
class _HwVoDigitalIfR2CfgDlReanswerTime_Type(Integer32):defaultValue=1000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,60000))
_HwVoDigitalIfR2CfgDlReanswerTime_Type.__name__=_C
_HwVoDigitalIfR2CfgDlReanswerTime_Object=MibTableColumn
hwVoDigitalIfR2CfgDlReanswerTime=_HwVoDigitalIfR2CfgDlReanswerTime_Object((1,3,6,1,4,1,2011,5,25,1,4,3,1,1,43),_HwVoDigitalIfR2CfgDlReanswerTime_Type())
hwVoDigitalIfR2CfgDlReanswerTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoDigitalIfR2CfgDlReanswerTime.setStatus(_A)
class _HwVoDigitalIfR2CfgDlReleaseGuardTime_Type(Integer32):defaultValue=1000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,60000))
_HwVoDigitalIfR2CfgDlReleaseGuardTime_Type.__name__=_C
_HwVoDigitalIfR2CfgDlReleaseGuardTime_Object=MibTableColumn
hwVoDigitalIfR2CfgDlReleaseGuardTime=_HwVoDigitalIfR2CfgDlReleaseGuardTime_Object((1,3,6,1,4,1,2011,5,25,1,4,3,1,1,44),_HwVoDigitalIfR2CfgDlReleaseGuardTime_Type())
hwVoDigitalIfR2CfgDlReleaseGuardTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoDigitalIfR2CfgDlReleaseGuardTime.setStatus(_A)
class _HwVoDigitalIfR2CfgMfcGroupBTime_Type(Integer32):defaultValue=30000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,90000))
_HwVoDigitalIfR2CfgMfcGroupBTime_Type.__name__=_C
_HwVoDigitalIfR2CfgMfcGroupBTime_Object=MibTableColumn
hwVoDigitalIfR2CfgMfcGroupBTime=_HwVoDigitalIfR2CfgMfcGroupBTime_Object((1,3,6,1,4,1,2011,5,25,1,4,3,1,1,45),_HwVoDigitalIfR2CfgMfcGroupBTime_Type())
hwVoDigitalIfR2CfgMfcGroupBTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoDigitalIfR2CfgMfcGroupBTime.setStatus(_A)
class _HwVoDigitalIfR2CfgAniEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_HwVoDigitalIfR2CfgAniEnable_Type.__name__=_C
_HwVoDigitalIfR2CfgAniEnable_Object=MibTableColumn
hwVoDigitalIfR2CfgAniEnable=_HwVoDigitalIfR2CfgAniEnable_Object((1,3,6,1,4,1,2011,5,25,1,4,3,1,1,46),_HwVoDigitalIfR2CfgAniEnable_Type())
hwVoDigitalIfR2CfgAniEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoDigitalIfR2CfgAniEnable.setStatus(_A)
class _HwVoDigitalIfR2CfgGroupBEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_HwVoDigitalIfR2CfgGroupBEnable_Type.__name__=_C
_HwVoDigitalIfR2CfgGroupBEnable_Object=MibTableColumn
hwVoDigitalIfR2CfgGroupBEnable=_HwVoDigitalIfR2CfgGroupBEnable_Object((1,3,6,1,4,1,2011,5,25,1,4,3,1,1,47),_HwVoDigitalIfR2CfgGroupBEnable_Type())
hwVoDigitalIfR2CfgGroupBEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoDigitalIfR2CfgGroupBEnable.setStatus(_A)
class _HwVoDigitalIfR2CfgClearForwardAckEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_HwVoDigitalIfR2CfgClearForwardAckEnable_Type.__name__=_C
_HwVoDigitalIfR2CfgClearForwardAckEnable_Object=MibTableColumn
hwVoDigitalIfR2CfgClearForwardAckEnable=_HwVoDigitalIfR2CfgClearForwardAckEnable_Object((1,3,6,1,4,1,2011,5,25,1,4,3,1,1,48),_HwVoDigitalIfR2CfgClearForwardAckEnable_Type())
hwVoDigitalIfR2CfgClearForwardAckEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoDigitalIfR2CfgClearForwardAckEnable.setStatus(_A)
class _HwVoDigitalIfR2CfgDlSeizureAckEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_HwVoDigitalIfR2CfgDlSeizureAckEnable_Type.__name__=_C
_HwVoDigitalIfR2CfgDlSeizureAckEnable_Object=MibTableColumn
hwVoDigitalIfR2CfgDlSeizureAckEnable=_HwVoDigitalIfR2CfgDlSeizureAckEnable_Object((1,3,6,1,4,1,2011,5,25,1,4,3,1,1,49),_HwVoDigitalIfR2CfgDlSeizureAckEnable_Type())
hwVoDigitalIfR2CfgDlSeizureAckEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoDigitalIfR2CfgDlSeizureAckEnable.setStatus(_A)
class _HwVoDigitalIfR2CfgDTMFEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_HwVoDigitalIfR2CfgDTMFEnable_Type.__name__=_C
_HwVoDigitalIfR2CfgDTMFEnable_Object=MibTableColumn
hwVoDigitalIfR2CfgDTMFEnable=_HwVoDigitalIfR2CfgDTMFEnable_Object((1,3,6,1,4,1,2011,5,25,1,4,3,1,1,50),_HwVoDigitalIfR2CfgDTMFEnable_Type())
hwVoDigitalIfR2CfgDTMFEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoDigitalIfR2CfgDTMFEnable.setStatus(_A)
class _HwVoDigitalIfR2CfgAnswerEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_HwVoDigitalIfR2CfgAnswerEnable_Type.__name__=_C
_HwVoDigitalIfR2CfgAnswerEnable_Object=MibTableColumn
hwVoDigitalIfR2CfgAnswerEnable=_HwVoDigitalIfR2CfgAnswerEnable_Object((1,3,6,1,4,1,2011,5,25,1,4,3,1,1,51),_HwVoDigitalIfR2CfgAnswerEnable_Type())
hwVoDigitalIfR2CfgAnswerEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoDigitalIfR2CfgAnswerEnable.setStatus(_A)
class _HwVoDigitalIfR2CfgReanswerEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_HwVoDigitalIfR2CfgReanswerEnable_Type.__name__=_C
_HwVoDigitalIfR2CfgReanswerEnable_Object=MibTableColumn
hwVoDigitalIfR2CfgReanswerEnable=_HwVoDigitalIfR2CfgReanswerEnable_Object((1,3,6,1,4,1,2011,5,25,1,4,3,1,1,52),_HwVoDigitalIfR2CfgReanswerEnable_Type())
hwVoDigitalIfR2CfgReanswerEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoDigitalIfR2CfgReanswerEnable.setStatus(_A)
class _HwVoDigitalIfR2CfgFinalCallnumEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_HwVoDigitalIfR2CfgFinalCallnumEnable_Type.__name__=_C
_HwVoDigitalIfR2CfgFinalCallnumEnable_Object=MibTableColumn
hwVoDigitalIfR2CfgFinalCallnumEnable=_HwVoDigitalIfR2CfgFinalCallnumEnable_Object((1,3,6,1,4,1,2011,5,25,1,4,3,1,1,53),_HwVoDigitalIfR2CfgFinalCallnumEnable_Type())
hwVoDigitalIfR2CfgFinalCallnumEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoDigitalIfR2CfgFinalCallnumEnable.setStatus(_A)
class _HwVoDigitalIfR2CfgForceMeteringEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_HwVoDigitalIfR2CfgForceMeteringEnable_Type.__name__=_C
_HwVoDigitalIfR2CfgForceMeteringEnable_Object=MibTableColumn
hwVoDigitalIfR2CfgForceMeteringEnable=_HwVoDigitalIfR2CfgForceMeteringEnable_Object((1,3,6,1,4,1,2011,5,25,1,4,3,1,1,54),_HwVoDigitalIfR2CfgForceMeteringEnable_Type())
hwVoDigitalIfR2CfgForceMeteringEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoDigitalIfR2CfgForceMeteringEnable.setStatus(_A)
class _HwVoDigitalIfR2CfgSendRingBackEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_HwVoDigitalIfR2CfgSendRingBackEnable_Type.__name__=_C
_HwVoDigitalIfR2CfgSendRingBackEnable_Object=MibTableColumn
hwVoDigitalIfR2CfgSendRingBackEnable=_HwVoDigitalIfR2CfgSendRingBackEnable_Object((1,3,6,1,4,1,2011,5,25,1,4,3,1,1,55),_HwVoDigitalIfR2CfgSendRingBackEnable_Type())
hwVoDigitalIfR2CfgSendRingBackEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoDigitalIfR2CfgSendRingBackEnable.setStatus(_A)
class _HwVoDigitalIfR2CfgSendRingBusyEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_HwVoDigitalIfR2CfgSendRingBusyEnable_Type.__name__=_C
_HwVoDigitalIfR2CfgSendRingBusyEnable_Object=MibTableColumn
hwVoDigitalIfR2CfgSendRingBusyEnable=_HwVoDigitalIfR2CfgSendRingBusyEnable_Object((1,3,6,1,4,1,2011,5,25,1,4,3,1,1,56),_HwVoDigitalIfR2CfgSendRingBusyEnable_Type())
hwVoDigitalIfR2CfgSendRingBusyEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoDigitalIfR2CfgSendRingBusyEnable.setStatus(_A)
class _HwVoDigitalIfR2CfgReqCategoryOffset_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_HwVoDigitalIfR2CfgReqCategoryOffset_Type.__name__=_C
_HwVoDigitalIfR2CfgReqCategoryOffset_Object=MibTableColumn
hwVoDigitalIfR2CfgReqCategoryOffset=_HwVoDigitalIfR2CfgReqCategoryOffset_Object((1,3,6,1,4,1,2011,5,25,1,4,3,1,1,57),_HwVoDigitalIfR2CfgReqCategoryOffset_Type())
hwVoDigitalIfR2CfgReqCategoryOffset.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoDigitalIfR2CfgReqCategoryOffset.setStatus(_A)
class _HwVoDigitalIfR2CfgReqCallingnumOffset_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_HwVoDigitalIfR2CfgReqCallingnumOffset_Type.__name__=_C
_HwVoDigitalIfR2CfgReqCallingnumOffset_Object=MibTableColumn
hwVoDigitalIfR2CfgReqCallingnumOffset=_HwVoDigitalIfR2CfgReqCallingnumOffset_Object((1,3,6,1,4,1,2011,5,25,1,4,3,1,1,58),_HwVoDigitalIfR2CfgReqCallingnumOffset_Type())
hwVoDigitalIfR2CfgReqCallingnumOffset.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoDigitalIfR2CfgReqCallingnumOffset.setStatus(_A)
class _HwVoDigitalIfR2CfgCountryMode_Type(Integer32):defaultValue=9;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)));namedValues=NamedValues(*(('argentina',0),('australia',1),('bengal',2),('brazil',3),('china',4),('customer',5),('hongkong',6),('india',7),('indonesia',8),('itu-t',9),('korea',10),('malaysia',11),('mexico',12),('newzealand',13),('singapore',14),('thailand',15)))
_HwVoDigitalIfR2CfgCountryMode_Type.__name__=_C
_HwVoDigitalIfR2CfgCountryMode_Object=MibTableColumn
hwVoDigitalIfR2CfgCountryMode=_HwVoDigitalIfR2CfgCountryMode_Object((1,3,6,1,4,1,2011,5,25,1,4,3,1,1,59),_HwVoDigitalIfR2CfgCountryMode_Type())
hwVoDigitalIfR2CfgCountryMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoDigitalIfR2CfgCountryMode.setStatus(_A)
class _HwVoDigitalIfR2CfgSpecialCharacter_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,35,42,65,66,67,68)));namedValues=NamedValues(*(('null',0),('pound',35),('asterisk',42),('a',65),('b',66),('c',67),('d',68)))
_HwVoDigitalIfR2CfgSpecialCharacter_Type.__name__=_C
_HwVoDigitalIfR2CfgSpecialCharacter_Object=MibTableColumn
hwVoDigitalIfR2CfgSpecialCharacter=_HwVoDigitalIfR2CfgSpecialCharacter_Object((1,3,6,1,4,1,2011,5,25,1,4,3,1,1,60),_HwVoDigitalIfR2CfgSpecialCharacter_Type())
hwVoDigitalIfR2CfgSpecialCharacter.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoDigitalIfR2CfgSpecialCharacter.setStatus(_A)
class _HwVoDigitalIfR2CfgSpecialSignal_Type(Integer32):defaultValue=16;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(11,16))
_HwVoDigitalIfR2CfgSpecialSignal_Type.__name__=_C
_HwVoDigitalIfR2CfgSpecialSignal_Object=MibTableColumn
hwVoDigitalIfR2CfgSpecialSignal=_HwVoDigitalIfR2CfgSpecialSignal_Object((1,3,6,1,4,1,2011,5,25,1,4,3,1,1,61),_HwVoDigitalIfR2CfgSpecialSignal_Type())
hwVoDigitalIfR2CfgSpecialSignal.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoDigitalIfR2CfgSpecialSignal.setStatus(_A)
class _HwVoDigitalIfR2CfgSelectMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('min',1),('max',2),(_X,3),(_W,4)))
_HwVoDigitalIfR2CfgSelectMode_Type.__name__=_C
_HwVoDigitalIfR2CfgSelectMode_Object=MibTableColumn
hwVoDigitalIfR2CfgSelectMode=_HwVoDigitalIfR2CfgSelectMode_Object((1,3,6,1,4,1,2011,5,25,1,4,3,1,1,62),_HwVoDigitalIfR2CfgSelectMode_Type())
hwVoDigitalIfR2CfgSelectMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoDigitalIfR2CfgSelectMode.setStatus(_A)
class _HwVoDigitalIfR2CfgDTMFTime_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_HwVoDigitalIfR2CfgDTMFTime_Type.__name__=_C
_HwVoDigitalIfR2CfgDTMFTime_Object=MibTableColumn
hwVoDigitalIfR2CfgDTMFTime=_HwVoDigitalIfR2CfgDTMFTime_Object((1,3,6,1,4,1,2011,5,25,1,4,3,1,1,63),_HwVoDigitalIfR2CfgDTMFTime_Type())
hwVoDigitalIfR2CfgDTMFTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoDigitalIfR2CfgDTMFTime.setStatus(_A)
class _HwVoDigitalIfR2CfgReqCallCreate_Type(Integer32):defaultValue=6;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_HwVoDigitalIfR2CfgReqCallCreate_Type.__name__=_C
_HwVoDigitalIfR2CfgReqCallCreate_Object=MibTableColumn
hwVoDigitalIfR2CfgReqCallCreate=_HwVoDigitalIfR2CfgReqCallCreate_Object((1,3,6,1,4,1,2011,5,25,1,4,3,1,1,64),_HwVoDigitalIfR2CfgReqCallCreate_Type())
hwVoDigitalIfR2CfgReqCallCreate.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoDigitalIfR2CfgReqCallCreate.setStatus(_A)
_HwVoDigitalIfR2ABCDCfgTable_Object=MibTable
hwVoDigitalIfR2ABCDCfgTable=_HwVoDigitalIfR2ABCDCfgTable_Object((1,3,6,1,4,1,2011,5,25,1,4,3,2))
if mibBuilder.loadTexts:hwVoDigitalIfR2ABCDCfgTable.setStatus(_A)
_HwVoDigitalIfR2ABCDCfgEntry_Object=MibTableRow
hwVoDigitalIfR2ABCDCfgEntry=_HwVoDigitalIfR2ABCDCfgEntry_Object((1,3,6,1,4,1,2011,5,25,1,4,3,2,1))
hwVoDigitalIfR2ABCDCfgEntry.setIndexNames((0,_F,_Y),(0,_F,_Z))
if mibBuilder.loadTexts:hwVoDigitalIfR2ABCDCfgEntry.setStatus(_A)
_HwVoDigitalIfR2ABCDCfgPortNumber_Type=Integer32
_HwVoDigitalIfR2ABCDCfgPortNumber_Object=MibTableColumn
hwVoDigitalIfR2ABCDCfgPortNumber=_HwVoDigitalIfR2ABCDCfgPortNumber_Object((1,3,6,1,4,1,2011,5,25,1,4,3,2,1,1),_HwVoDigitalIfR2ABCDCfgPortNumber_Type())
hwVoDigitalIfR2ABCDCfgPortNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:hwVoDigitalIfR2ABCDCfgPortNumber.setStatus(_A)
class _HwVoDigitalIfR2ABCDCfgGroupNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,30))
_HwVoDigitalIfR2ABCDCfgGroupNumber_Type.__name__=_C
_HwVoDigitalIfR2ABCDCfgGroupNumber_Object=MibTableColumn
hwVoDigitalIfR2ABCDCfgGroupNumber=_HwVoDigitalIfR2ABCDCfgGroupNumber_Object((1,3,6,1,4,1,2011,5,25,1,4,3,2,1,2),_HwVoDigitalIfR2ABCDCfgGroupNumber_Type())
hwVoDigitalIfR2ABCDCfgGroupNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:hwVoDigitalIfR2ABCDCfgGroupNumber.setStatus(_A)
class _HwVoDigitalIfR2ABCDReverseABCD_Type(OctetString):defaultValue=OctetString('0000');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_HwVoDigitalIfR2ABCDReverseABCD_Type.__name__=_D
_HwVoDigitalIfR2ABCDReverseABCD_Object=MibTableColumn
hwVoDigitalIfR2ABCDReverseABCD=_HwVoDigitalIfR2ABCDReverseABCD_Object((1,3,6,1,4,1,2011,5,25,1,4,3,2,1,3),_HwVoDigitalIfR2ABCDReverseABCD_Type())
hwVoDigitalIfR2ABCDReverseABCD.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoDigitalIfR2ABCDReverseABCD.setStatus(_A)
class _HwVoDigitalIfR2ABCDRenewABCD_Type(OctetString):defaultValue=OctetString('1111');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_HwVoDigitalIfR2ABCDRenewABCD_Type.__name__=_D
_HwVoDigitalIfR2ABCDRenewABCD_Object=MibTableColumn
hwVoDigitalIfR2ABCDRenewABCD=_HwVoDigitalIfR2ABCDRenewABCD_Object((1,3,6,1,4,1,2011,5,25,1,4,3,2,1,4),_HwVoDigitalIfR2ABCDRenewABCD_Type())
hwVoDigitalIfR2ABCDRenewABCD.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoDigitalIfR2ABCDRenewABCD.setStatus(_A)
class _HwVoDigitalIfR2ABCDRxIdle_Type(OctetString):defaultValue=OctetString(_K);subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_HwVoDigitalIfR2ABCDRxIdle_Type.__name__=_D
_HwVoDigitalIfR2ABCDRxIdle_Object=MibTableColumn
hwVoDigitalIfR2ABCDRxIdle=_HwVoDigitalIfR2ABCDRxIdle_Object((1,3,6,1,4,1,2011,5,25,1,4,3,2,1,5),_HwVoDigitalIfR2ABCDRxIdle_Type())
hwVoDigitalIfR2ABCDRxIdle.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoDigitalIfR2ABCDRxIdle.setStatus(_A)
class _HwVoDigitalIfR2ABCDTxIdle_Type(OctetString):defaultValue=OctetString(_K);subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_HwVoDigitalIfR2ABCDTxIdle_Type.__name__=_D
_HwVoDigitalIfR2ABCDTxIdle_Object=MibTableColumn
hwVoDigitalIfR2ABCDTxIdle=_HwVoDigitalIfR2ABCDTxIdle_Object((1,3,6,1,4,1,2011,5,25,1,4,3,2,1,6),_HwVoDigitalIfR2ABCDTxIdle_Type())
hwVoDigitalIfR2ABCDTxIdle.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoDigitalIfR2ABCDTxIdle.setStatus(_A)
class _HwVoDigitalIfR2ABCDRxSeizure_Type(OctetString):defaultValue=OctetString('0001');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_HwVoDigitalIfR2ABCDRxSeizure_Type.__name__=_D
_HwVoDigitalIfR2ABCDRxSeizure_Object=MibTableColumn
hwVoDigitalIfR2ABCDRxSeizure=_HwVoDigitalIfR2ABCDRxSeizure_Object((1,3,6,1,4,1,2011,5,25,1,4,3,2,1,7),_HwVoDigitalIfR2ABCDRxSeizure_Type())
hwVoDigitalIfR2ABCDRxSeizure.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoDigitalIfR2ABCDRxSeizure.setStatus(_A)
class _HwVoDigitalIfR2ABCDTxSeizure_Type(OctetString):defaultValue=OctetString('0001');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_HwVoDigitalIfR2ABCDTxSeizure_Type.__name__=_D
_HwVoDigitalIfR2ABCDTxSeizure_Object=MibTableColumn
hwVoDigitalIfR2ABCDTxSeizure=_HwVoDigitalIfR2ABCDTxSeizure_Object((1,3,6,1,4,1,2011,5,25,1,4,3,2,1,8),_HwVoDigitalIfR2ABCDTxSeizure_Type())
hwVoDigitalIfR2ABCDTxSeizure.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoDigitalIfR2ABCDTxSeizure.setStatus(_A)
class _HwVoDigitalIfR2ABCDRxSeizureAck_Type(OctetString):defaultValue=OctetString(_J);subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_HwVoDigitalIfR2ABCDRxSeizureAck_Type.__name__=_D
_HwVoDigitalIfR2ABCDRxSeizureAck_Object=MibTableColumn
hwVoDigitalIfR2ABCDRxSeizureAck=_HwVoDigitalIfR2ABCDRxSeizureAck_Object((1,3,6,1,4,1,2011,5,25,1,4,3,2,1,9),_HwVoDigitalIfR2ABCDRxSeizureAck_Type())
hwVoDigitalIfR2ABCDRxSeizureAck.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoDigitalIfR2ABCDRxSeizureAck.setStatus(_A)
class _HwVoDigitalIfR2ABCDTxSeizureAck_Type(OctetString):defaultValue=OctetString(_J);subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_HwVoDigitalIfR2ABCDTxSeizureAck_Type.__name__=_D
_HwVoDigitalIfR2ABCDTxSeizureAck_Object=MibTableColumn
hwVoDigitalIfR2ABCDTxSeizureAck=_HwVoDigitalIfR2ABCDTxSeizureAck_Object((1,3,6,1,4,1,2011,5,25,1,4,3,2,1,10),_HwVoDigitalIfR2ABCDTxSeizureAck_Type())
hwVoDigitalIfR2ABCDTxSeizureAck.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoDigitalIfR2ABCDTxSeizureAck.setStatus(_A)
class _HwVoDigitalIfR2ABCDRxAnswer_Type(OctetString):defaultValue=OctetString(_L);subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_HwVoDigitalIfR2ABCDRxAnswer_Type.__name__=_D
_HwVoDigitalIfR2ABCDRxAnswer_Object=MibTableColumn
hwVoDigitalIfR2ABCDRxAnswer=_HwVoDigitalIfR2ABCDRxAnswer_Object((1,3,6,1,4,1,2011,5,25,1,4,3,2,1,11),_HwVoDigitalIfR2ABCDRxAnswer_Type())
hwVoDigitalIfR2ABCDRxAnswer.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoDigitalIfR2ABCDRxAnswer.setStatus(_A)
class _HwVoDigitalIfR2ABCDTxAnswer_Type(OctetString):defaultValue=OctetString(_L);subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_HwVoDigitalIfR2ABCDTxAnswer_Type.__name__=_D
_HwVoDigitalIfR2ABCDTxAnswer_Object=MibTableColumn
hwVoDigitalIfR2ABCDTxAnswer=_HwVoDigitalIfR2ABCDTxAnswer_Object((1,3,6,1,4,1,2011,5,25,1,4,3,2,1,12),_HwVoDigitalIfR2ABCDTxAnswer_Type())
hwVoDigitalIfR2ABCDTxAnswer.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoDigitalIfR2ABCDTxAnswer.setStatus(_A)
class _HwVoDigitalIfR2ABCDRxClearForward_Type(OctetString):defaultValue=OctetString(_K);subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_HwVoDigitalIfR2ABCDRxClearForward_Type.__name__=_D
_HwVoDigitalIfR2ABCDRxClearForward_Object=MibTableColumn
hwVoDigitalIfR2ABCDRxClearForward=_HwVoDigitalIfR2ABCDRxClearForward_Object((1,3,6,1,4,1,2011,5,25,1,4,3,2,1,13),_HwVoDigitalIfR2ABCDRxClearForward_Type())
hwVoDigitalIfR2ABCDRxClearForward.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoDigitalIfR2ABCDRxClearForward.setStatus(_A)
class _HwVoDigitalIfR2ABCDTxClearForward_Type(OctetString):defaultValue=OctetString(_K);subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_HwVoDigitalIfR2ABCDTxClearForward_Type.__name__=_D
_HwVoDigitalIfR2ABCDTxClearForward_Object=MibTableColumn
hwVoDigitalIfR2ABCDTxClearForward=_HwVoDigitalIfR2ABCDTxClearForward_Object((1,3,6,1,4,1,2011,5,25,1,4,3,2,1,14),_HwVoDigitalIfR2ABCDTxClearForward_Type())
hwVoDigitalIfR2ABCDTxClearForward.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoDigitalIfR2ABCDTxClearForward.setStatus(_A)
class _HwVoDigitalIfR2ABCDRxClearBack_Type(OctetString):defaultValue=OctetString(_J);subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_HwVoDigitalIfR2ABCDRxClearBack_Type.__name__=_D
_HwVoDigitalIfR2ABCDRxClearBack_Object=MibTableColumn
hwVoDigitalIfR2ABCDRxClearBack=_HwVoDigitalIfR2ABCDRxClearBack_Object((1,3,6,1,4,1,2011,5,25,1,4,3,2,1,15),_HwVoDigitalIfR2ABCDRxClearBack_Type())
hwVoDigitalIfR2ABCDRxClearBack.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoDigitalIfR2ABCDRxClearBack.setStatus(_A)
class _HwVoDigitalIfR2ABCDTxClearBack_Type(OctetString):defaultValue=OctetString(_J);subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_HwVoDigitalIfR2ABCDTxClearBack_Type.__name__=_D
_HwVoDigitalIfR2ABCDTxClearBack_Object=MibTableColumn
hwVoDigitalIfR2ABCDTxClearBack=_HwVoDigitalIfR2ABCDTxClearBack_Object((1,3,6,1,4,1,2011,5,25,1,4,3,2,1,16),_HwVoDigitalIfR2ABCDTxClearBack_Type())
hwVoDigitalIfR2ABCDTxClearBack.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoDigitalIfR2ABCDTxClearBack.setStatus(_A)
class _HwVoDigitalIfR2ABCDRxReleaseGuard_Type(OctetString):defaultValue=OctetString(_K);subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_HwVoDigitalIfR2ABCDRxReleaseGuard_Type.__name__=_D
_HwVoDigitalIfR2ABCDRxReleaseGuard_Object=MibTableColumn
hwVoDigitalIfR2ABCDRxReleaseGuard=_HwVoDigitalIfR2ABCDRxReleaseGuard_Object((1,3,6,1,4,1,2011,5,25,1,4,3,2,1,17),_HwVoDigitalIfR2ABCDRxReleaseGuard_Type())
hwVoDigitalIfR2ABCDRxReleaseGuard.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoDigitalIfR2ABCDRxReleaseGuard.setStatus(_A)
class _HwVoDigitalIfR2ABCDTxReleaseGuard_Type(OctetString):defaultValue=OctetString(_K);subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_HwVoDigitalIfR2ABCDTxReleaseGuard_Type.__name__=_D
_HwVoDigitalIfR2ABCDTxReleaseGuard_Object=MibTableColumn
hwVoDigitalIfR2ABCDTxReleaseGuard=_HwVoDigitalIfR2ABCDTxReleaseGuard_Object((1,3,6,1,4,1,2011,5,25,1,4,3,2,1,18),_HwVoDigitalIfR2ABCDTxReleaseGuard_Type())
hwVoDigitalIfR2ABCDTxReleaseGuard.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoDigitalIfR2ABCDTxReleaseGuard.setStatus(_A)
class _HwVoDigitalIfR2ABCDRxBlocking_Type(OctetString):defaultValue=OctetString(_J);subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_HwVoDigitalIfR2ABCDRxBlocking_Type.__name__=_D
_HwVoDigitalIfR2ABCDRxBlocking_Object=MibTableColumn
hwVoDigitalIfR2ABCDRxBlocking=_HwVoDigitalIfR2ABCDRxBlocking_Object((1,3,6,1,4,1,2011,5,25,1,4,3,2,1,19),_HwVoDigitalIfR2ABCDRxBlocking_Type())
hwVoDigitalIfR2ABCDRxBlocking.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoDigitalIfR2ABCDRxBlocking.setStatus(_A)
class _HwVoDigitalIfR2ABCDTxBlocking_Type(OctetString):defaultValue=OctetString(_J);subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_HwVoDigitalIfR2ABCDTxBlocking_Type.__name__=_D
_HwVoDigitalIfR2ABCDTxBlocking_Object=MibTableColumn
hwVoDigitalIfR2ABCDTxBlocking=_HwVoDigitalIfR2ABCDTxBlocking_Object((1,3,6,1,4,1,2011,5,25,1,4,3,2,1,20),_HwVoDigitalIfR2ABCDTxBlocking_Type())
hwVoDigitalIfR2ABCDTxBlocking.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoDigitalIfR2ABCDTxBlocking.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'hwVoiceDigitalInterfaceMIB':hwVoiceDigitalInterfaceMIB,'hwVoDigitalIfCommonObjects':hwVoDigitalIfCommonObjects,'hwVoDigitalIfCommonCfgTable':hwVoDigitalIfCommonCfgTable,'hwVoDigitalIfCommonCfgEntry':hwVoDigitalIfCommonCfgEntry,_M:hwVoDigitalIfCfgPortNumber,_N:hwVoDigitalIfCfgGroupNumber,'hwVoDigitalIfCfgBoardType':hwVoDigitalIfCfgBoardType,'hwVoDigitalIfCfgSignalType':hwVoDigitalIfCfgSignalType,'hwVoDigitalIfCfgTimeSlotsConfigurable':hwVoDigitalIfCfgTimeSlotsConfigurable,'hwVoDigitalIfEMObjects':hwVoDigitalIfEMObjects,'hwVoDigitalIfEMCfgTable':hwVoDigitalIfEMCfgTable,'hwVoDigitalIfEMCfgEntry':hwVoDigitalIfEMCfgEntry,_O:hwVoDigitalIfEMCfgPortNumber,_P:hwVoDigitalIfEMCfgGroupNumber,'hwVoDigitalIfEMCfgTimeoutInterDigits':hwVoDigitalIfEMCfgTimeoutInterDigits,'hwVoDigitalIfEMCfgTimeoutRinging':hwVoDigitalIfEMCfgTimeoutRinging,'hwVoDigitalIfEMCfgTimeoutWaitDigit':hwVoDigitalIfEMCfgTimeoutWaitDigit,'hwVoDigitalIfEMABCDCfgTable':hwVoDigitalIfEMABCDCfgTable,'hwVoDigitalIfEMABCDCfgEntry':hwVoDigitalIfEMABCDCfgEntry,_Q:hwVoDigitalIfEMABCDCfgPortNumber,_R:hwVoDigitalIfEMABCDCfgGroupNumber,'hwVoDigitalIfEMABCDRxIdle':hwVoDigitalIfEMABCDRxIdle,'hwVoDigitalIfEMABCDRxSeize':hwVoDigitalIfEMABCDRxSeize,'hwVoDigitalIfEMABCDTxIdle':hwVoDigitalIfEMABCDTxIdle,'hwVoDigitalIfEMABCDTxSeize':hwVoDigitalIfEMABCDTxSeize,'hwVoDigitalIfEMTimerTable':hwVoDigitalIfEMTimerTable,'hwVoDigitalIfEMTimerEntry':hwVoDigitalIfEMTimerEntry,_S:hwVoDigitalIfEMTimerPortNumber,_T:hwVoDigitalIfEMTimerGroupNumber,'hwVoDigitalIfEMTimerCallInterval':hwVoDigitalIfEMTimerCallInterval,'hwVoDigitalIfEMTimerSendWink':hwVoDigitalIfEMTimerSendWink,'hwVoDigitalIfEMTimerWinkRising':hwVoDigitalIfEMTimerWinkRising,'hwVoDigitalIfEMTimerWinkHold':hwVoDigitalIfEMTimerWinkHold,'hwVoDigitalIfEMTimerDialoutDelay':hwVoDigitalIfEMTimerDialoutDelay,'hwVoDigitalIfEMTimerRising':hwVoDigitalIfEMTimerRising,'hwVoDigitalIfEMTimerHold':hwVoDigitalIfEMTimerHold,'hwVoDigitalIfEMTimerDtmf':hwVoDigitalIfEMTimerDtmf,'hwVoDigitalIfEMTimerDtmfInterval':hwVoDigitalIfEMTimerDtmfInterval,'hwVoDigitalIfR2Objects':hwVoDigitalIfR2Objects,'hwVoDigitalIfR2CfgTable':hwVoDigitalIfR2CfgTable,'hwVoDigitalIfR2CfgEntry':hwVoDigitalIfR2CfgEntry,_U:hwVoDigitalIfR2CfgPortNumber,_V:hwVoDigitalIfR2CfgGroupNumber,'hwVoDigitalIfR2CfgAniSwitch':hwVoDigitalIfR2CfgAniSwitch,'hwVoDigitalIfR2CallerDigits':hwVoDigitalIfR2CallerDigits,'hwVoDigitalIfR2DebounceTime':hwVoDigitalIfR2DebounceTime,'hwVoDigitalIfR2Ka':hwVoDigitalIfR2Ka,'hwVoDigitalIfR2Kd':hwVoDigitalIfR2Kd,'hwVoDigitalIfR2SeizureAckTime':hwVoDigitalIfR2SeizureAckTime,'hwVoDigitalIfR2SelectMode':hwVoDigitalIfR2SelectMode,'hwVoDigitalIfR2TimeoutKb':hwVoDigitalIfR2TimeoutKb,'hwVoDigitalIfR2TimeoutKd':hwVoDigitalIfR2TimeoutKd,'hwVoDigitalIfR2TimeoutNextNumber':hwVoDigitalIfR2TimeoutNextNumber,'hwVoDigitalIfR2TimeoutReleaseApprove':hwVoDigitalIfR2TimeoutReleaseApprove,'hwVoDigitalIfR2TimeoutRing':hwVoDigitalIfR2TimeoutRing,'hwVoDigitalIfR2TimeoutSendAnswer':hwVoDigitalIfR2TimeoutSendAnswer,'hwVoDigitalIfR2CfgBillingCategory':hwVoDigitalIfR2CfgBillingCategory,'hwVoDigitalIfR2CfgCallingCategory':hwVoDigitalIfR2CfgCallingCategory,'hwVoDigitalIfR2CfgCongestion':hwVoDigitalIfR2CfgCongestion,'hwVoDigitalIfR2CfgDemandRefused':hwVoDigitalIfR2CfgDemandRefused,'hwVoDigitalIfR2CfgDigitEnd':hwVoDigitalIfR2CfgDigitEnd,'hwVoDigitalIfR2CfgNullnum':hwVoDigitalIfR2CfgNullnum,'hwVoDigitalIfR2CfgReqBillingCategory':hwVoDigitalIfR2CfgReqBillingCategory,'hwVoDigitalIfR2CfgReqCallingCategory':hwVoDigitalIfR2CfgReqCallingCategory,'hwVoDigitalIfR2CfgReqCurrentdigit':hwVoDigitalIfR2CfgReqCurrentdigit,'hwVoDigitalIfR2CfgReqFirstCallingnum':hwVoDigitalIfR2CfgReqFirstCallingnum,'hwVoDigitalIfR2CfgReqFirstDigit':hwVoDigitalIfR2CfgReqFirstDigit,'hwVoDigitalIfR2CfgReqNextCallednum':hwVoDigitalIfR2CfgReqNextCallednum,'hwVoDigitalIfR2CfgReqNextCallingnum':hwVoDigitalIfR2CfgReqNextCallingnum,'hwVoDigitalIfR2CfgReqLastFirstDigit':hwVoDigitalIfR2CfgReqLastFirstDigit,'hwVoDigitalIfR2CfgReqLastSecondDigit':hwVoDigitalIfR2CfgReqLastSecondDigit,'hwVoDigitalIfR2CfgReqLastThirdDigit':hwVoDigitalIfR2CfgReqLastThirdDigit,'hwVoDigitalIfR2CfgReqSwitchGroupB':hwVoDigitalIfR2CfgReqSwitchGroupB,'hwVoDigitalIfR2CfgSubscriberIdle':hwVoDigitalIfR2CfgSubscriberIdle,'hwVoDigitalIfR2CfgSubscriberBusy':hwVoDigitalIfR2CfgSubscriberBusy,'hwVoDigitalIfR2CfgDebounceTime':hwVoDigitalIfR2CfgDebounceTime,'hwVoDigitalIfR2CfgSendringBackTime':hwVoDigitalIfR2CfgSendringBackTime,'hwVoDigitalIfR2CfgSendringBusyTime':hwVoDigitalIfR2CfgSendringBusyTime,'hwVoDigitalIfR2CfgPulseSignalPersistenceTime':hwVoDigitalIfR2CfgPulseSignalPersistenceTime,'hwVoDigitalIfR2CfgDlAnswerTime':hwVoDigitalIfR2CfgDlAnswerTime,'hwVoDigitalIfR2CfgDlClearBackTime':hwVoDigitalIfR2CfgDlClearBackTime,'hwVoDigitalIfR2CfgDlClearForwardTime':hwVoDigitalIfR2CfgDlClearForwardTime,'hwVoDigitalIfR2CfgDlSeizureTime':hwVoDigitalIfR2CfgDlSeizureTime,'hwVoDigitalIfR2CfgDlReanswerTime':hwVoDigitalIfR2CfgDlReanswerTime,'hwVoDigitalIfR2CfgDlReleaseGuardTime':hwVoDigitalIfR2CfgDlReleaseGuardTime,'hwVoDigitalIfR2CfgMfcGroupBTime':hwVoDigitalIfR2CfgMfcGroupBTime,'hwVoDigitalIfR2CfgAniEnable':hwVoDigitalIfR2CfgAniEnable,'hwVoDigitalIfR2CfgGroupBEnable':hwVoDigitalIfR2CfgGroupBEnable,'hwVoDigitalIfR2CfgClearForwardAckEnable':hwVoDigitalIfR2CfgClearForwardAckEnable,'hwVoDigitalIfR2CfgDlSeizureAckEnable':hwVoDigitalIfR2CfgDlSeizureAckEnable,'hwVoDigitalIfR2CfgDTMFEnable':hwVoDigitalIfR2CfgDTMFEnable,'hwVoDigitalIfR2CfgAnswerEnable':hwVoDigitalIfR2CfgAnswerEnable,'hwVoDigitalIfR2CfgReanswerEnable':hwVoDigitalIfR2CfgReanswerEnable,'hwVoDigitalIfR2CfgFinalCallnumEnable':hwVoDigitalIfR2CfgFinalCallnumEnable,'hwVoDigitalIfR2CfgForceMeteringEnable':hwVoDigitalIfR2CfgForceMeteringEnable,'hwVoDigitalIfR2CfgSendRingBackEnable':hwVoDigitalIfR2CfgSendRingBackEnable,'hwVoDigitalIfR2CfgSendRingBusyEnable':hwVoDigitalIfR2CfgSendRingBusyEnable,'hwVoDigitalIfR2CfgReqCategoryOffset':hwVoDigitalIfR2CfgReqCategoryOffset,'hwVoDigitalIfR2CfgReqCallingnumOffset':hwVoDigitalIfR2CfgReqCallingnumOffset,'hwVoDigitalIfR2CfgCountryMode':hwVoDigitalIfR2CfgCountryMode,'hwVoDigitalIfR2CfgSpecialCharacter':hwVoDigitalIfR2CfgSpecialCharacter,'hwVoDigitalIfR2CfgSpecialSignal':hwVoDigitalIfR2CfgSpecialSignal,'hwVoDigitalIfR2CfgSelectMode':hwVoDigitalIfR2CfgSelectMode,'hwVoDigitalIfR2CfgDTMFTime':hwVoDigitalIfR2CfgDTMFTime,'hwVoDigitalIfR2CfgReqCallCreate':hwVoDigitalIfR2CfgReqCallCreate,'hwVoDigitalIfR2ABCDCfgTable':hwVoDigitalIfR2ABCDCfgTable,'hwVoDigitalIfR2ABCDCfgEntry':hwVoDigitalIfR2ABCDCfgEntry,_Y:hwVoDigitalIfR2ABCDCfgPortNumber,_Z:hwVoDigitalIfR2ABCDCfgGroupNumber,'hwVoDigitalIfR2ABCDReverseABCD':hwVoDigitalIfR2ABCDReverseABCD,'hwVoDigitalIfR2ABCDRenewABCD':hwVoDigitalIfR2ABCDRenewABCD,'hwVoDigitalIfR2ABCDRxIdle':hwVoDigitalIfR2ABCDRxIdle,'hwVoDigitalIfR2ABCDTxIdle':hwVoDigitalIfR2ABCDTxIdle,'hwVoDigitalIfR2ABCDRxSeizure':hwVoDigitalIfR2ABCDRxSeizure,'hwVoDigitalIfR2ABCDTxSeizure':hwVoDigitalIfR2ABCDTxSeizure,'hwVoDigitalIfR2ABCDRxSeizureAck':hwVoDigitalIfR2ABCDRxSeizureAck,'hwVoDigitalIfR2ABCDTxSeizureAck':hwVoDigitalIfR2ABCDTxSeizureAck,'hwVoDigitalIfR2ABCDRxAnswer':hwVoDigitalIfR2ABCDRxAnswer,'hwVoDigitalIfR2ABCDTxAnswer':hwVoDigitalIfR2ABCDTxAnswer,'hwVoDigitalIfR2ABCDRxClearForward':hwVoDigitalIfR2ABCDRxClearForward,'hwVoDigitalIfR2ABCDTxClearForward':hwVoDigitalIfR2ABCDTxClearForward,'hwVoDigitalIfR2ABCDRxClearBack':hwVoDigitalIfR2ABCDRxClearBack,'hwVoDigitalIfR2ABCDTxClearBack':hwVoDigitalIfR2ABCDTxClearBack,'hwVoDigitalIfR2ABCDRxReleaseGuard':hwVoDigitalIfR2ABCDRxReleaseGuard,'hwVoDigitalIfR2ABCDTxReleaseGuard':hwVoDigitalIfR2ABCDTxReleaseGuard,'hwVoDigitalIfR2ABCDRxBlocking':hwVoDigitalIfR2ABCDRxBlocking,'hwVoDigitalIfR2ABCDTxBlocking':hwVoDigitalIfR2ABCDTxBlocking})