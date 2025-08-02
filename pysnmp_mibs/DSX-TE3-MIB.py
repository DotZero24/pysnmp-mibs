_A9='nndsxT3E3AlarmOffTrap'
_A8='nndsxT3E3AlarmOnTrap'
_A7='nndsxT3E3IfUserLifetimeStatsEntry'
_A6='nndsxT3E3IfUserCurrentStatsEntry'
_A5='nndsxT3E3IfIetfTotalStatsEntry'
_A4='nndsxT3E3IfIetfCurrentStatsEntry'
_A3='nndsxT3E3IfAnsiTotalStatsEntry'
_A2='nndsxT3E3IfAnsiCurrentStatsEntry'
_A1='nndsxT3E3IfErrorEventStatsEntry'
_A0='nndsxT3E3IfArchiveStatsValidIntervalsEntry'
_z='nndsxT3E3IfLastTestResultEntry'
_y='nndsxT3E3IfTestStatusEntry'
_x='nndsxT3E3IfAlarmStatusEntry'
_w='nndsxT3E3IfStatusEntry'
_v='nndsxT3E3IfTestConfigEntry'
_u='nndsxT3E3IfUserArchiveStatsInterval'
_t='nndsxT3E3IfIetfArchiveStatsInterval'
_s='nndsxT3E3IfAnsiArchiveStatsInterval'
_r='state-failed'
_q='state-passed'
_p='state-in-progress'
_o='state-relocked'
_n='state-locked'
_m='state-searching'
_l='state-idle'
_k='remote-lpdn'
_j='remote-lpup'
_i='testtype-pattern'
_h='other-loopback'
_g='int-loopback'
_f='local-loopback'
_e='line-loopback'
_d='payload-loopback'
_c='rcvTestCode'
_b='reserved11'
_a='reserved10'
_Z='reserved9'
_Y='reserved7'
_X='reserved6'
_W='reserved5'
_V='reserved4'
_U='reserved3'
_T='reserved2'
_S='reserved1'
_R='nndsxT3E3IfAlarmThresholdConfigIndex'
_Q='timing-internal'
_P='timing-line'
_O='DisplayString'
_N='nndsxT3E3AlarmType'
_M='nndsxT3E3Number'
_L='loopcode-feac'
_K='loopcode-none'
_J='no-test'
_I='accessible-for-notify'
_H='not-accessible'
_G='Bits'
_F='nndsxT3E3IfIndex'
_E='read-write'
_D='Integer32'
_C='DSX-TE3-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
LEDState,nndsxT3E3IfGroup=mibBuilder.importSymbols('DSX-TC-MIB','LEDState','nndsxT3E3IfGroup')
ntEnterpriseDataTasmanInterfaces,=mibBuilder.importSymbols('NT-ENTERPRISE-DATA-MIB','ntEnterpriseDataTasmanInterfaces')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_G,'Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_O,'PhysAddress','TextualConvention','TruthValue')
nndsxT3E3MIB=ModuleIdentity((1,3,6,1,4,1,562,73,1,1,2,1,3,1))
if mibBuilder.loadTexts:nndsxT3E3MIB.setRevisions(('1900-08-18 00:00',))
_NndsxT3E3IfConfigGroup_ObjectIdentity=ObjectIdentity
nndsxT3E3IfConfigGroup=_NndsxT3E3IfConfigGroup_ObjectIdentity((1,3,6,1,4,1,562,73,1,1,2,1,3,1,1))
_NndsxT3E3IfConfigLineTable_Object=MibTable
nndsxT3E3IfConfigLineTable=_NndsxT3E3IfConfigLineTable_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,1,1))
if mibBuilder.loadTexts:nndsxT3E3IfConfigLineTable.setStatus(_A)
_NndsxT3E3IfConfigLineEntry_Object=MibTableRow
nndsxT3E3IfConfigLineEntry=_NndsxT3E3IfConfigLineEntry_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,1,1,1))
nndsxT3E3IfConfigLineEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:nndsxT3E3IfConfigLineEntry.setStatus(_A)
_NndsxT3E3IfIndex_Type=Integer32
_NndsxT3E3IfIndex_Object=MibTableColumn
nndsxT3E3IfIndex=_NndsxT3E3IfIndex_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,1,1,1,1),_NndsxT3E3IfIndex_Type())
nndsxT3E3IfIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:nndsxT3E3IfIndex.setStatus(_A)
class _NndsxT3E3IfConfigLineType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,4)));namedValues=NamedValues(*(('linetype-m13',2),('linetype-cbitparity',4)))
_NndsxT3E3IfConfigLineType_Type.__name__=_D
_NndsxT3E3IfConfigLineType_Object=MibTableColumn
nndsxT3E3IfConfigLineType=_NndsxT3E3IfConfigLineType_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,1,1,1,2),_NndsxT3E3IfConfigLineType_Type())
nndsxT3E3IfConfigLineType.setMaxAccess(_E)
if mibBuilder.loadTexts:nndsxT3E3IfConfigLineType.setStatus(_A)
class _NndsxT3E3IfConfigLineCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*(('linecode-b3zs',2),('linecode-hdb3',3)))
_NndsxT3E3IfConfigLineCode_Type.__name__=_D
_NndsxT3E3IfConfigLineCode_Object=MibTableColumn
nndsxT3E3IfConfigLineCode=_NndsxT3E3IfConfigLineCode_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,1,1,1,3),_NndsxT3E3IfConfigLineCode_Type())
nndsxT3E3IfConfigLineCode.setMaxAccess(_B)
if mibBuilder.loadTexts:nndsxT3E3IfConfigLineCode.setStatus(_A)
class _NndsxT3E3IfConfigCableLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('cable-length-0-to-225',1),('cable-length-226-to-450',2)))
_NndsxT3E3IfConfigCableLength_Type.__name__=_D
_NndsxT3E3IfConfigCableLength_Object=MibTableColumn
nndsxT3E3IfConfigCableLength=_NndsxT3E3IfConfigCableLength_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,1,1,1,4),_NndsxT3E3IfConfigCableLength_Type())
nndsxT3E3IfConfigCableLength.setMaxAccess(_E)
if mibBuilder.loadTexts:nndsxT3E3IfConfigCableLength.setStatus(_A)
class _NndsxT3E3IfConfigTransmitClock_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_Q,2)))
_NndsxT3E3IfConfigTransmitClock_Type.__name__=_D
_NndsxT3E3IfConfigTransmitClock_Object=MibTableColumn
nndsxT3E3IfConfigTransmitClock=_NndsxT3E3IfConfigTransmitClock_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,1,1,1,5),_NndsxT3E3IfConfigTransmitClock_Type())
nndsxT3E3IfConfigTransmitClock.setMaxAccess(_E)
if mibBuilder.loadTexts:nndsxT3E3IfConfigTransmitClock.setStatus(_A)
_NndsxT3E3IfAlarmConfigGroup_ObjectIdentity=ObjectIdentity
nndsxT3E3IfAlarmConfigGroup=_NndsxT3E3IfAlarmConfigGroup_ObjectIdentity((1,3,6,1,4,1,562,73,1,1,2,1,3,1,1,3))
_NndsxT3E3IfAlarmThresholdConfigTable_Object=MibTable
nndsxT3E3IfAlarmThresholdConfigTable=_NndsxT3E3IfAlarmThresholdConfigTable_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,1,3,1))
if mibBuilder.loadTexts:nndsxT3E3IfAlarmThresholdConfigTable.setStatus(_A)
_NndsxT3E3IfAlarmThresholdConfigEntry_Object=MibTableRow
nndsxT3E3IfAlarmThresholdConfigEntry=_NndsxT3E3IfAlarmThresholdConfigEntry_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,1,3,1,1))
nndsxT3E3IfAlarmThresholdConfigEntry.setIndexNames((0,_C,_F),(0,_C,_R))
if mibBuilder.loadTexts:nndsxT3E3IfAlarmThresholdConfigEntry.setStatus(_A)
_NndsxT3E3IfAlarmThresholdConfigIndex_Type=Integer32
_NndsxT3E3IfAlarmThresholdConfigIndex_Object=MibTableColumn
nndsxT3E3IfAlarmThresholdConfigIndex=_NndsxT3E3IfAlarmThresholdConfigIndex_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,1,3,1,1,1),_NndsxT3E3IfAlarmThresholdConfigIndex_Type())
nndsxT3E3IfAlarmThresholdConfigIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:nndsxT3E3IfAlarmThresholdConfigIndex.setStatus(_A)
class _NndsxT3E3IfAlarmThresholdConfigObject_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('te3-object-lcv',1),('te3-object-fbe',2),('te3-object-pbe',3),('te3-object-cpbe',4),('te3-object-febe',5),('te3-object-exz',6),('te3-object-cofa',7)))
_NndsxT3E3IfAlarmThresholdConfigObject_Type.__name__=_D
_NndsxT3E3IfAlarmThresholdConfigObject_Object=MibTableColumn
nndsxT3E3IfAlarmThresholdConfigObject=_NndsxT3E3IfAlarmThresholdConfigObject_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,1,3,1,1,2),_NndsxT3E3IfAlarmThresholdConfigObject_Type())
nndsxT3E3IfAlarmThresholdConfigObject.setMaxAccess(_E)
if mibBuilder.loadTexts:nndsxT3E3IfAlarmThresholdConfigObject.setStatus(_A)
class _NndsxT3E3IfAlarmThresholdConfigSamplingInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_NndsxT3E3IfAlarmThresholdConfigSamplingInterval_Type.__name__=_D
_NndsxT3E3IfAlarmThresholdConfigSamplingInterval_Object=MibTableColumn
nndsxT3E3IfAlarmThresholdConfigSamplingInterval=_NndsxT3E3IfAlarmThresholdConfigSamplingInterval_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,1,3,1,1,3),_NndsxT3E3IfAlarmThresholdConfigSamplingInterval_Type())
nndsxT3E3IfAlarmThresholdConfigSamplingInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:nndsxT3E3IfAlarmThresholdConfigSamplingInterval.setStatus(_A)
class _NndsxT3E3IfAlarmThresholdConfigSampleType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('sample-absolute',1),('sample-delta',2)))
_NndsxT3E3IfAlarmThresholdConfigSampleType_Type.__name__=_D
_NndsxT3E3IfAlarmThresholdConfigSampleType_Object=MibTableColumn
nndsxT3E3IfAlarmThresholdConfigSampleType=_NndsxT3E3IfAlarmThresholdConfigSampleType_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,1,3,1,1,4),_NndsxT3E3IfAlarmThresholdConfigSampleType_Type())
nndsxT3E3IfAlarmThresholdConfigSampleType.setMaxAccess(_E)
if mibBuilder.loadTexts:nndsxT3E3IfAlarmThresholdConfigSampleType.setStatus(_A)
_NndsxT3E3IfAlarmThresholdConfigRisingThreshold_Type=Integer32
_NndsxT3E3IfAlarmThresholdConfigRisingThreshold_Object=MibTableColumn
nndsxT3E3IfAlarmThresholdConfigRisingThreshold=_NndsxT3E3IfAlarmThresholdConfigRisingThreshold_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,1,3,1,1,5),_NndsxT3E3IfAlarmThresholdConfigRisingThreshold_Type())
nndsxT3E3IfAlarmThresholdConfigRisingThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:nndsxT3E3IfAlarmThresholdConfigRisingThreshold.setStatus(_A)
_NndsxT3E3IfAlarmThresholdConfigFallingThreshold_Type=Integer32
_NndsxT3E3IfAlarmThresholdConfigFallingThreshold_Object=MibTableColumn
nndsxT3E3IfAlarmThresholdConfigFallingThreshold=_NndsxT3E3IfAlarmThresholdConfigFallingThreshold_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,1,3,1,1,6),_NndsxT3E3IfAlarmThresholdConfigFallingThreshold_Type())
nndsxT3E3IfAlarmThresholdConfigFallingThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:nndsxT3E3IfAlarmThresholdConfigFallingThreshold.setStatus(_A)
_NndsxT3E3IfAlarmThresholdConfigEnable_Type=TruthValue
_NndsxT3E3IfAlarmThresholdConfigEnable_Object=MibTableColumn
nndsxT3E3IfAlarmThresholdConfigEnable=_NndsxT3E3IfAlarmThresholdConfigEnable_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,1,3,1,1,7),_NndsxT3E3IfAlarmThresholdConfigEnable_Type())
nndsxT3E3IfAlarmThresholdConfigEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:nndsxT3E3IfAlarmThresholdConfigEnable.setStatus(_A)
_NndsxT3E3IfTestConfigTable_Object=MibTable
nndsxT3E3IfTestConfigTable=_NndsxT3E3IfTestConfigTable_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,1,4))
if mibBuilder.loadTexts:nndsxT3E3IfTestConfigTable.setStatus(_A)
_NndsxT3E3IfTestConfigEntry_Object=MibTableRow
nndsxT3E3IfTestConfigEntry=_NndsxT3E3IfTestConfigEntry_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,1,4,1))
if mibBuilder.loadTexts:nndsxT3E3IfTestConfigEntry.setStatus(_A)
class _NndsxT3E3IfTestConfigType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,7,8,9)));namedValues=NamedValues(*((_J,1),('payload-loopback-test',2),('line-loopback-test',3),('local-loopback-test',4),('internal-loopback-test',5),('pattern-test',7),('remote-lpup-test',8),('remote-lpdn-test',9)))
_NndsxT3E3IfTestConfigType_Type.__name__=_D
_NndsxT3E3IfTestConfigType_Object=MibTableColumn
nndsxT3E3IfTestConfigType=_NndsxT3E3IfTestConfigType_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,1,4,1,1),_NndsxT3E3IfTestConfigType_Type())
nndsxT3E3IfTestConfigType.setMaxAccess(_E)
if mibBuilder.loadTexts:nndsxT3E3IfTestConfigType.setStatus(_A)
class _NndsxT3E3IfTestConfigLoopCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_NndsxT3E3IfTestConfigLoopCode_Type.__name__=_D
_NndsxT3E3IfTestConfigLoopCode_Object=MibTableColumn
nndsxT3E3IfTestConfigLoopCode=_NndsxT3E3IfTestConfigLoopCode_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,1,4,1,2),_NndsxT3E3IfTestConfigLoopCode_Type())
nndsxT3E3IfTestConfigLoopCode.setMaxAccess(_E)
if mibBuilder.loadTexts:nndsxT3E3IfTestConfigLoopCode.setStatus(_A)
class _NndsxT3E3IfTestConfigPattern_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)));namedValues=NamedValues(*(('no-pattern',0),('pattern-all-ones',1),('pattern-all-zeros',2),(_S,3),(_T,4),(_U,5),(_V,6),(_W,7),(_X,8),(_Y,9),(_Z,10),(_a,11),(_b,12),('pattern-215minus1',13),('reserved12',14),('pattern-qrw',15),('pattern-223minus1',16)))
_NndsxT3E3IfTestConfigPattern_Type.__name__=_D
_NndsxT3E3IfTestConfigPattern_Object=MibTableColumn
nndsxT3E3IfTestConfigPattern=_NndsxT3E3IfTestConfigPattern_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,1,4,1,3),_NndsxT3E3IfTestConfigPattern_Type())
nndsxT3E3IfTestConfigPattern.setMaxAccess(_E)
if mibBuilder.loadTexts:nndsxT3E3IfTestConfigPattern.setStatus(_A)
_NndsxT3E3IfTestConfigTime_Type=Unsigned32
_NndsxT3E3IfTestConfigTime_Object=MibTableColumn
nndsxT3E3IfTestConfigTime=_NndsxT3E3IfTestConfigTime_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,1,4,1,4),_NndsxT3E3IfTestConfigTime_Type())
nndsxT3E3IfTestConfigTime.setMaxAccess(_E)
if mibBuilder.loadTexts:nndsxT3E3IfTestConfigTime.setStatus(_A)
_NndsxT3E3IfStatusGroup_ObjectIdentity=ObjectIdentity
nndsxT3E3IfStatusGroup=_NndsxT3E3IfStatusGroup_ObjectIdentity((1,3,6,1,4,1,562,73,1,1,2,1,3,1,2))
_NndsxT3E3IfStatusTable_Object=MibTable
nndsxT3E3IfStatusTable=_NndsxT3E3IfStatusTable_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,2,1))
if mibBuilder.loadTexts:nndsxT3E3IfStatusTable.setStatus(_A)
_NndsxT3E3IfStatusEntry_Object=MibTableRow
nndsxT3E3IfStatusEntry=_NndsxT3E3IfStatusEntry_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,2,1,1))
if mibBuilder.loadTexts:nndsxT3E3IfStatusEntry.setStatus(_A)
class _NndsxT3E3IfStatusLineStatus_Type(Bits):namedValues=NamedValues(*(('reserved',0),(_S,1),(_T,2),(_U,3),(_V,4),(_W,5),(_X,6),(_Y,7),('sendPattern',8),('sendTE3Code',9),('sendResetCode',10),('sendPayloadCode',11),('sendLineCode',12),('reserved8',13),('febeStatus',14),('pdeStatus',15),('lorcStatus',16),(_Z,17),(_a,18),('rfebeStatus',19),('risStatus',20),('rexzStatus',21),(_b,22),(_c,23),('loopbackStatus',24),('rlosStatus',25),('rlofStatus',26),('taisStatus',27),('raisStatus',28),('traiStatus',29),('rraiStatus',30),('no-alarm',31)))
_NndsxT3E3IfStatusLineStatus_Type.__name__=_G
_NndsxT3E3IfStatusLineStatus_Object=MibTableColumn
nndsxT3E3IfStatusLineStatus=_NndsxT3E3IfStatusLineStatus_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,2,1,1,1),_NndsxT3E3IfStatusLineStatus_Type())
nndsxT3E3IfStatusLineStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nndsxT3E3IfStatusLineStatus.setStatus(_A)
class _NndsxT3E3IfStatusTransmitClock_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_Q,2)))
_NndsxT3E3IfStatusTransmitClock_Type.__name__=_D
_NndsxT3E3IfStatusTransmitClock_Object=MibTableColumn
nndsxT3E3IfStatusTransmitClock=_NndsxT3E3IfStatusTransmitClock_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,2,1,1,2),_NndsxT3E3IfStatusTransmitClock_Type())
nndsxT3E3IfStatusTransmitClock.setMaxAccess(_B)
if mibBuilder.loadTexts:nndsxT3E3IfStatusTransmitClock.setStatus(_A)
_NndsxT3E3IfAlarmStatusTable_Object=MibTable
nndsxT3E3IfAlarmStatusTable=_NndsxT3E3IfAlarmStatusTable_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,2,2))
if mibBuilder.loadTexts:nndsxT3E3IfAlarmStatusTable.setStatus(_A)
_NndsxT3E3IfAlarmStatusEntry_Object=MibTableRow
nndsxT3E3IfAlarmStatusEntry=_NndsxT3E3IfAlarmStatusEntry_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,2,2,1))
if mibBuilder.loadTexts:nndsxT3E3IfAlarmStatusEntry.setStatus(_A)
class _NndsxT3E3IfAlarmStatusAlarmStatus_Type(Bits):namedValues=NamedValues(*(('rraiAlarm',0),('traiAlarm',1),('raisAlarm',2),('taisAlarm',3),('rlofAlarm',4),('rlosAlarm',5),('loopbackStateAlarm',6),(_c,7),('rbluAlarm',8),('risAlarm',9),('rexzAlarm',10),('rfbeAlarm',11),('rpeAlarm',12),('rcpeAlarm',13),('lorcAlarm',14),('tpdeAlarm',15),('tfebeAlarm',16)))
_NndsxT3E3IfAlarmStatusAlarmStatus_Type.__name__=_G
_NndsxT3E3IfAlarmStatusAlarmStatus_Object=MibTableColumn
nndsxT3E3IfAlarmStatusAlarmStatus=_NndsxT3E3IfAlarmStatusAlarmStatus_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,2,2,1,1),_NndsxT3E3IfAlarmStatusAlarmStatus_Type())
nndsxT3E3IfAlarmStatusAlarmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nndsxT3E3IfAlarmStatusAlarmStatus.setStatus(_A)
class _NndsxT3E3IfAlarmStatusThresholdStatus_Type(Bits):namedValues=NamedValues(*(('threshold1',0),('threshold2',1),('threshold3',2),('threshold4',3),('threshold5',4),('threshold6',5),('threshold7',6),('threshold8',7),('threshold9',8),('threshold10',9)))
_NndsxT3E3IfAlarmStatusThresholdStatus_Type.__name__=_G
_NndsxT3E3IfAlarmStatusThresholdStatus_Object=MibTableColumn
nndsxT3E3IfAlarmStatusThresholdStatus=_NndsxT3E3IfAlarmStatusThresholdStatus_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,2,2,1,2),_NndsxT3E3IfAlarmStatusThresholdStatus_Type())
nndsxT3E3IfAlarmStatusThresholdStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nndsxT3E3IfAlarmStatusThresholdStatus.setStatus(_A)
_NndsxT3E3IfTestStatusTable_Object=MibTable
nndsxT3E3IfTestStatusTable=_NndsxT3E3IfTestStatusTable_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,2,3))
if mibBuilder.loadTexts:nndsxT3E3IfTestStatusTable.setStatus(_A)
_NndsxT3E3IfTestStatusEntry_Object=MibTableRow
nndsxT3E3IfTestStatusEntry=_NndsxT3E3IfTestStatusEntry_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,2,3,1))
if mibBuilder.loadTexts:nndsxT3E3IfTestStatusEntry.setStatus(_A)
class _NndsxT3E3IfTestStatusTestType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_J,1),(_d,2),(_e,3),(_f,4),(_g,5),(_h,6),(_i,7),(_j,8),(_k,9)))
_NndsxT3E3IfTestStatusTestType_Type.__name__=_D
_NndsxT3E3IfTestStatusTestType_Object=MibTableColumn
nndsxT3E3IfTestStatusTestType=_NndsxT3E3IfTestStatusTestType_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,2,3,1,1),_NndsxT3E3IfTestStatusTestType_Type())
nndsxT3E3IfTestStatusTestType.setMaxAccess(_B)
if mibBuilder.loadTexts:nndsxT3E3IfTestStatusTestType.setStatus(_A)
class _NndsxT3E3IfTestStatusTestState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_l,1),(_m,2),(_n,3),(_o,4),(_p,5),(_q,6),(_r,7)))
_NndsxT3E3IfTestStatusTestState_Type.__name__=_D
_NndsxT3E3IfTestStatusTestState_Object=MibTableColumn
nndsxT3E3IfTestStatusTestState=_NndsxT3E3IfTestStatusTestState_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,2,3,1,2),_NndsxT3E3IfTestStatusTestState_Type())
nndsxT3E3IfTestStatusTestState.setMaxAccess(_B)
if mibBuilder.loadTexts:nndsxT3E3IfTestStatusTestState.setStatus(_A)
class _NndsxT3E3IfTestStatusLoopCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_NndsxT3E3IfTestStatusLoopCode_Type.__name__=_D
_NndsxT3E3IfTestStatusLoopCode_Object=MibTableColumn
nndsxT3E3IfTestStatusLoopCode=_NndsxT3E3IfTestStatusLoopCode_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,2,3,1,3),_NndsxT3E3IfTestStatusLoopCode_Type())
nndsxT3E3IfTestStatusLoopCode.setMaxAccess(_B)
if mibBuilder.loadTexts:nndsxT3E3IfTestStatusLoopCode.setStatus(_A)
_NndsxT3E3IfLastTestResultTable_Object=MibTable
nndsxT3E3IfLastTestResultTable=_NndsxT3E3IfLastTestResultTable_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,2,4))
if mibBuilder.loadTexts:nndsxT3E3IfLastTestResultTable.setStatus(_A)
_NndsxT3E3IfLastTestResultEntry_Object=MibTableRow
nndsxT3E3IfLastTestResultEntry=_NndsxT3E3IfLastTestResultEntry_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,2,4,1))
if mibBuilder.loadTexts:nndsxT3E3IfLastTestResultEntry.setStatus(_A)
class _NndsxT3E3IfLastTestResultTestType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_J,1),(_d,2),(_e,3),(_f,4),(_g,5),(_h,6),(_i,7),(_j,8),(_k,9)))
_NndsxT3E3IfLastTestResultTestType_Type.__name__=_D
_NndsxT3E3IfLastTestResultTestType_Object=MibTableColumn
nndsxT3E3IfLastTestResultTestType=_NndsxT3E3IfLastTestResultTestType_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,2,4,1,1),_NndsxT3E3IfLastTestResultTestType_Type())
nndsxT3E3IfLastTestResultTestType.setMaxAccess(_B)
if mibBuilder.loadTexts:nndsxT3E3IfLastTestResultTestType.setStatus(_A)
class _NndsxT3E3IfLastTestResultTestState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_l,1),(_m,2),(_n,3),(_o,4),(_p,5),(_q,6),(_r,7)))
_NndsxT3E3IfLastTestResultTestState_Type.__name__=_D
_NndsxT3E3IfLastTestResultTestState_Object=MibTableColumn
nndsxT3E3IfLastTestResultTestState=_NndsxT3E3IfLastTestResultTestState_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,2,4,1,2),_NndsxT3E3IfLastTestResultTestState_Type())
nndsxT3E3IfLastTestResultTestState.setMaxAccess(_B)
if mibBuilder.loadTexts:nndsxT3E3IfLastTestResultTestState.setStatus(_A)
class _NndsxT3E3IfLastTestResultLoopCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_NndsxT3E3IfLastTestResultLoopCode_Type.__name__=_D
_NndsxT3E3IfLastTestResultLoopCode_Object=MibTableColumn
nndsxT3E3IfLastTestResultLoopCode=_NndsxT3E3IfLastTestResultLoopCode_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,2,4,1,3),_NndsxT3E3IfLastTestResultLoopCode_Type())
nndsxT3E3IfLastTestResultLoopCode.setMaxAccess(_B)
if mibBuilder.loadTexts:nndsxT3E3IfLastTestResultLoopCode.setStatus(_A)
_NndsxT3E3IfStatsGroup_ObjectIdentity=ObjectIdentity
nndsxT3E3IfStatsGroup=_NndsxT3E3IfStatsGroup_ObjectIdentity((1,3,6,1,4,1,562,73,1,1,2,1,3,1,3))
_NndsxT3E3IfArchiveStatsValidIntervalsTable_Object=MibTable
nndsxT3E3IfArchiveStatsValidIntervalsTable=_NndsxT3E3IfArchiveStatsValidIntervalsTable_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,3,1))
if mibBuilder.loadTexts:nndsxT3E3IfArchiveStatsValidIntervalsTable.setStatus(_A)
_NndsxT3E3IfArchiveStatsValidIntervalsEntry_Object=MibTableRow
nndsxT3E3IfArchiveStatsValidIntervalsEntry=_NndsxT3E3IfArchiveStatsValidIntervalsEntry_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,3,1,1))
if mibBuilder.loadTexts:nndsxT3E3IfArchiveStatsValidIntervalsEntry.setStatus(_A)
_NndsxT3E3IfAnsiArchiveStatsValidIntervals_Type=Unsigned32
_NndsxT3E3IfAnsiArchiveStatsValidIntervals_Object=MibTableColumn
nndsxT3E3IfAnsiArchiveStatsValidIntervals=_NndsxT3E3IfAnsiArchiveStatsValidIntervals_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,3,1,1,1),_NndsxT3E3IfAnsiArchiveStatsValidIntervals_Type())
nndsxT3E3IfAnsiArchiveStatsValidIntervals.setMaxAccess(_B)
if mibBuilder.loadTexts:nndsxT3E3IfAnsiArchiveStatsValidIntervals.setStatus(_A)
_NndsxT3E3IfIetfArchiveStatsValidIntervals_Type=Unsigned32
_NndsxT3E3IfIetfArchiveStatsValidIntervals_Object=MibTableColumn
nndsxT3E3IfIetfArchiveStatsValidIntervals=_NndsxT3E3IfIetfArchiveStatsValidIntervals_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,3,1,1,2),_NndsxT3E3IfIetfArchiveStatsValidIntervals_Type())
nndsxT3E3IfIetfArchiveStatsValidIntervals.setMaxAccess(_B)
if mibBuilder.loadTexts:nndsxT3E3IfIetfArchiveStatsValidIntervals.setStatus(_A)
_NndsxT3E3IfUserTotalStatsValidDays_Type=Unsigned32
_NndsxT3E3IfUserTotalStatsValidDays_Object=MibTableColumn
nndsxT3E3IfUserTotalStatsValidDays=_NndsxT3E3IfUserTotalStatsValidDays_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,3,1,1,3),_NndsxT3E3IfUserTotalStatsValidDays_Type())
nndsxT3E3IfUserTotalStatsValidDays.setMaxAccess(_B)
if mibBuilder.loadTexts:nndsxT3E3IfUserTotalStatsValidDays.setStatus(_A)
_NndsxT3E3IfUserArchiveStatsValidIntervals_Type=Integer32
_NndsxT3E3IfUserArchiveStatsValidIntervals_Object=MibTableColumn
nndsxT3E3IfUserArchiveStatsValidIntervals=_NndsxT3E3IfUserArchiveStatsValidIntervals_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,3,1,1,4),_NndsxT3E3IfUserArchiveStatsValidIntervals_Type())
nndsxT3E3IfUserArchiveStatsValidIntervals.setMaxAccess(_E)
if mibBuilder.loadTexts:nndsxT3E3IfUserArchiveStatsValidIntervals.setStatus(_A)
_NndsxT3E3IfErrorEventStatsTable_Object=MibTable
nndsxT3E3IfErrorEventStatsTable=_NndsxT3E3IfErrorEventStatsTable_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,3,2))
if mibBuilder.loadTexts:nndsxT3E3IfErrorEventStatsTable.setStatus(_A)
_NndsxT3E3IfErrorEventStatsEntry_Object=MibTableRow
nndsxT3E3IfErrorEventStatsEntry=_NndsxT3E3IfErrorEventStatsEntry_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,3,2,1))
if mibBuilder.loadTexts:nndsxT3E3IfErrorEventStatsEntry.setStatus(_A)
_NndsxT3E3IfErrorEventStatsPBE_Type=Unsigned32
_NndsxT3E3IfErrorEventStatsPBE_Object=MibTableColumn
nndsxT3E3IfErrorEventStatsPBE=_NndsxT3E3IfErrorEventStatsPBE_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,3,2,1,2),_NndsxT3E3IfErrorEventStatsPBE_Type())
nndsxT3E3IfErrorEventStatsPBE.setMaxAccess(_B)
if mibBuilder.loadTexts:nndsxT3E3IfErrorEventStatsPBE.setStatus(_A)
_NndsxT3E3IfErrorEventStatsFEBE_Type=Unsigned32
_NndsxT3E3IfErrorEventStatsFEBE_Object=MibTableColumn
nndsxT3E3IfErrorEventStatsFEBE=_NndsxT3E3IfErrorEventStatsFEBE_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,3,2,1,3),_NndsxT3E3IfErrorEventStatsFEBE_Type())
nndsxT3E3IfErrorEventStatsFEBE.setMaxAccess(_B)
if mibBuilder.loadTexts:nndsxT3E3IfErrorEventStatsFEBE.setStatus(_A)
_NndsxT3E3IfAnsiStatsGroup_ObjectIdentity=ObjectIdentity
nndsxT3E3IfAnsiStatsGroup=_NndsxT3E3IfAnsiStatsGroup_ObjectIdentity((1,3,6,1,4,1,562,73,1,1,2,1,3,1,3,3))
_NndsxT3E3IfAnsiCurrentStatsTable_Object=MibTable
nndsxT3E3IfAnsiCurrentStatsTable=_NndsxT3E3IfAnsiCurrentStatsTable_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,3,3,1))
if mibBuilder.loadTexts:nndsxT3E3IfAnsiCurrentStatsTable.setStatus(_A)
_NndsxT3E3IfAnsiCurrentStatsEntry_Object=MibTableRow
nndsxT3E3IfAnsiCurrentStatsEntry=_NndsxT3E3IfAnsiCurrentStatsEntry_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,3,3,1,1))
if mibBuilder.loadTexts:nndsxT3E3IfAnsiCurrentStatsEntry.setStatus(_A)
_NndsxT3E3IfAnsiCurrentStatsUASState_Type=TruthValue
_NndsxT3E3IfAnsiCurrentStatsUASState_Object=MibTableColumn
nndsxT3E3IfAnsiCurrentStatsUASState=_NndsxT3E3IfAnsiCurrentStatsUASState_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,3,3,1,1,1),_NndsxT3E3IfAnsiCurrentStatsUASState_Type())
nndsxT3E3IfAnsiCurrentStatsUASState.setMaxAccess(_B)
if mibBuilder.loadTexts:nndsxT3E3IfAnsiCurrentStatsUASState.setStatus(_A)
_NndsxT3E3IfAnsiCurrentStatsTimeInCurrent_Type=Unsigned32
_NndsxT3E3IfAnsiCurrentStatsTimeInCurrent_Object=MibTableColumn
nndsxT3E3IfAnsiCurrentStatsTimeInCurrent=_NndsxT3E3IfAnsiCurrentStatsTimeInCurrent_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,3,3,1,1,2),_NndsxT3E3IfAnsiCurrentStatsTimeInCurrent_Type())
nndsxT3E3IfAnsiCurrentStatsTimeInCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:nndsxT3E3IfAnsiCurrentStatsTimeInCurrent.setStatus(_A)
_NndsxT3E3IfAnsiCurrentPathStatsCV_Type=Unsigned32
_NndsxT3E3IfAnsiCurrentPathStatsCV_Object=MibTableColumn
nndsxT3E3IfAnsiCurrentPathStatsCV=_NndsxT3E3IfAnsiCurrentPathStatsCV_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,3,3,1,1,3),_NndsxT3E3IfAnsiCurrentPathStatsCV_Type())
nndsxT3E3IfAnsiCurrentPathStatsCV.setMaxAccess(_B)
if mibBuilder.loadTexts:nndsxT3E3IfAnsiCurrentPathStatsCV.setStatus(_A)
_NndsxT3E3IfAnsiCurrentPathStatsES_Type=Unsigned32
_NndsxT3E3IfAnsiCurrentPathStatsES_Object=MibTableColumn
nndsxT3E3IfAnsiCurrentPathStatsES=_NndsxT3E3IfAnsiCurrentPathStatsES_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,3,3,1,1,4),_NndsxT3E3IfAnsiCurrentPathStatsES_Type())
nndsxT3E3IfAnsiCurrentPathStatsES.setMaxAccess(_B)
if mibBuilder.loadTexts:nndsxT3E3IfAnsiCurrentPathStatsES.setStatus(_A)
_NndsxT3E3IfAnsiCurrentPathStatsSES_Type=Unsigned32
_NndsxT3E3IfAnsiCurrentPathStatsSES_Object=MibTableColumn
nndsxT3E3IfAnsiCurrentPathStatsSES=_NndsxT3E3IfAnsiCurrentPathStatsSES_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,3,3,1,1,5),_NndsxT3E3IfAnsiCurrentPathStatsSES_Type())
nndsxT3E3IfAnsiCurrentPathStatsSES.setMaxAccess(_B)
if mibBuilder.loadTexts:nndsxT3E3IfAnsiCurrentPathStatsSES.setStatus(_A)
_NndsxT3E3IfAnsiCurrentPathStatsSAS_Type=Unsigned32
_NndsxT3E3IfAnsiCurrentPathStatsSAS_Object=MibTableColumn
nndsxT3E3IfAnsiCurrentPathStatsSAS=_NndsxT3E3IfAnsiCurrentPathStatsSAS_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,3,3,1,1,6),_NndsxT3E3IfAnsiCurrentPathStatsSAS_Type())
nndsxT3E3IfAnsiCurrentPathStatsSAS.setMaxAccess(_B)
if mibBuilder.loadTexts:nndsxT3E3IfAnsiCurrentPathStatsSAS.setStatus(_A)
_NndsxT3E3IfAnsiCurrentPathStatsUAS_Type=Unsigned32
_NndsxT3E3IfAnsiCurrentPathStatsUAS_Object=MibTableColumn
nndsxT3E3IfAnsiCurrentPathStatsUAS=_NndsxT3E3IfAnsiCurrentPathStatsUAS_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,3,3,1,1,7),_NndsxT3E3IfAnsiCurrentPathStatsUAS_Type())
nndsxT3E3IfAnsiCurrentPathStatsUAS.setMaxAccess(_B)
if mibBuilder.loadTexts:nndsxT3E3IfAnsiCurrentPathStatsUAS.setStatus(_A)
_NndsxT3E3IfAnsiCurrentLineStatsCV_Type=Unsigned32
_NndsxT3E3IfAnsiCurrentLineStatsCV_Object=MibTableColumn
nndsxT3E3IfAnsiCurrentLineStatsCV=_NndsxT3E3IfAnsiCurrentLineStatsCV_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,3,3,1,1,8),_NndsxT3E3IfAnsiCurrentLineStatsCV_Type())
nndsxT3E3IfAnsiCurrentLineStatsCV.setMaxAccess(_B)
if mibBuilder.loadTexts:nndsxT3E3IfAnsiCurrentLineStatsCV.setStatus(_A)
_NndsxT3E3IfAnsiCurrentLineStatsES_Type=Unsigned32
_NndsxT3E3IfAnsiCurrentLineStatsES_Object=MibTableColumn
nndsxT3E3IfAnsiCurrentLineStatsES=_NndsxT3E3IfAnsiCurrentLineStatsES_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,3,3,1,1,9),_NndsxT3E3IfAnsiCurrentLineStatsES_Type())
nndsxT3E3IfAnsiCurrentLineStatsES.setMaxAccess(_B)
if mibBuilder.loadTexts:nndsxT3E3IfAnsiCurrentLineStatsES.setStatus(_A)
_NndsxT3E3IfAnsiCurrentLineStatsSES_Type=Unsigned32
_NndsxT3E3IfAnsiCurrentLineStatsSES_Object=MibTableColumn
nndsxT3E3IfAnsiCurrentLineStatsSES=_NndsxT3E3IfAnsiCurrentLineStatsSES_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,3,3,1,1,10),_NndsxT3E3IfAnsiCurrentLineStatsSES_Type())
nndsxT3E3IfAnsiCurrentLineStatsSES.setMaxAccess(_B)
if mibBuilder.loadTexts:nndsxT3E3IfAnsiCurrentLineStatsSES.setStatus(_A)
_NndsxT3E3IfAnsiTotalStatsTable_Object=MibTable
nndsxT3E3IfAnsiTotalStatsTable=_NndsxT3E3IfAnsiTotalStatsTable_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,3,3,2))
if mibBuilder.loadTexts:nndsxT3E3IfAnsiTotalStatsTable.setStatus(_A)
_NndsxT3E3IfAnsiTotalStatsEntry_Object=MibTableRow
nndsxT3E3IfAnsiTotalStatsEntry=_NndsxT3E3IfAnsiTotalStatsEntry_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,3,3,2,1))
if mibBuilder.loadTexts:nndsxT3E3IfAnsiTotalStatsEntry.setStatus(_A)
_NndsxT3E3IfAnsiTotalPathStatsCV_Type=Unsigned32
_NndsxT3E3IfAnsiTotalPathStatsCV_Object=MibTableColumn
nndsxT3E3IfAnsiTotalPathStatsCV=_NndsxT3E3IfAnsiTotalPathStatsCV_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,3,3,2,1,1),_NndsxT3E3IfAnsiTotalPathStatsCV_Type())
nndsxT3E3IfAnsiTotalPathStatsCV.setMaxAccess(_B)
if mibBuilder.loadTexts:nndsxT3E3IfAnsiTotalPathStatsCV.setStatus(_A)
_NndsxT3E3IfAnsiTotalPathStatsES_Type=Unsigned32
_NndsxT3E3IfAnsiTotalPathStatsES_Object=MibTableColumn
nndsxT3E3IfAnsiTotalPathStatsES=_NndsxT3E3IfAnsiTotalPathStatsES_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,3,3,2,1,2),_NndsxT3E3IfAnsiTotalPathStatsES_Type())
nndsxT3E3IfAnsiTotalPathStatsES.setMaxAccess(_B)
if mibBuilder.loadTexts:nndsxT3E3IfAnsiTotalPathStatsES.setStatus(_A)
_NndsxT3E3IfAnsiTotalPathStatsSES_Type=Unsigned32
_NndsxT3E3IfAnsiTotalPathStatsSES_Object=MibTableColumn
nndsxT3E3IfAnsiTotalPathStatsSES=_NndsxT3E3IfAnsiTotalPathStatsSES_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,3,3,2,1,3),_NndsxT3E3IfAnsiTotalPathStatsSES_Type())
nndsxT3E3IfAnsiTotalPathStatsSES.setMaxAccess(_B)
if mibBuilder.loadTexts:nndsxT3E3IfAnsiTotalPathStatsSES.setStatus(_A)
_NndsxT3E3IfAnsiTotalPathStatsSAS_Type=Unsigned32
_NndsxT3E3IfAnsiTotalPathStatsSAS_Object=MibTableColumn
nndsxT3E3IfAnsiTotalPathStatsSAS=_NndsxT3E3IfAnsiTotalPathStatsSAS_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,3,3,2,1,4),_NndsxT3E3IfAnsiTotalPathStatsSAS_Type())
nndsxT3E3IfAnsiTotalPathStatsSAS.setMaxAccess(_B)
if mibBuilder.loadTexts:nndsxT3E3IfAnsiTotalPathStatsSAS.setStatus(_A)
_NndsxT3E3IfAnsiTotalPathStatsUAS_Type=Unsigned32
_NndsxT3E3IfAnsiTotalPathStatsUAS_Object=MibTableColumn
nndsxT3E3IfAnsiTotalPathStatsUAS=_NndsxT3E3IfAnsiTotalPathStatsUAS_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,3,3,2,1,5),_NndsxT3E3IfAnsiTotalPathStatsUAS_Type())
nndsxT3E3IfAnsiTotalPathStatsUAS.setMaxAccess(_B)
if mibBuilder.loadTexts:nndsxT3E3IfAnsiTotalPathStatsUAS.setStatus(_A)
_NndsxT3E3IfAnsiTotalLineStatsCV_Type=Unsigned32
_NndsxT3E3IfAnsiTotalLineStatsCV_Object=MibTableColumn
nndsxT3E3IfAnsiTotalLineStatsCV=_NndsxT3E3IfAnsiTotalLineStatsCV_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,3,3,2,1,6),_NndsxT3E3IfAnsiTotalLineStatsCV_Type())
nndsxT3E3IfAnsiTotalLineStatsCV.setMaxAccess(_B)
if mibBuilder.loadTexts:nndsxT3E3IfAnsiTotalLineStatsCV.setStatus(_A)
_NndsxT3E3IfAnsiTotalLineStatsES_Type=Unsigned32
_NndsxT3E3IfAnsiTotalLineStatsES_Object=MibTableColumn
nndsxT3E3IfAnsiTotalLineStatsES=_NndsxT3E3IfAnsiTotalLineStatsES_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,3,3,2,1,7),_NndsxT3E3IfAnsiTotalLineStatsES_Type())
nndsxT3E3IfAnsiTotalLineStatsES.setMaxAccess(_B)
if mibBuilder.loadTexts:nndsxT3E3IfAnsiTotalLineStatsES.setStatus(_A)
_NndsxT3E3IfAnsiTotalLineStatsSES_Type=Unsigned32
_NndsxT3E3IfAnsiTotalLineStatsSES_Object=MibTableColumn
nndsxT3E3IfAnsiTotalLineStatsSES=_NndsxT3E3IfAnsiTotalLineStatsSES_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,3,3,2,1,8),_NndsxT3E3IfAnsiTotalLineStatsSES_Type())
nndsxT3E3IfAnsiTotalLineStatsSES.setMaxAccess(_B)
if mibBuilder.loadTexts:nndsxT3E3IfAnsiTotalLineStatsSES.setStatus(_A)
_NndsxT3E3IfAnsiArchiveIntervalStatsTable_Object=MibTable
nndsxT3E3IfAnsiArchiveIntervalStatsTable=_NndsxT3E3IfAnsiArchiveIntervalStatsTable_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,3,3,3))
if mibBuilder.loadTexts:nndsxT3E3IfAnsiArchiveIntervalStatsTable.setStatus(_A)
_NndsxT3E3IfAnsiArchiveIntervalStatsEntry_Object=MibTableRow
nndsxT3E3IfAnsiArchiveIntervalStatsEntry=_NndsxT3E3IfAnsiArchiveIntervalStatsEntry_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,3,3,3,1))
nndsxT3E3IfAnsiArchiveIntervalStatsEntry.setIndexNames((0,_C,_F),(0,_C,_s))
if mibBuilder.loadTexts:nndsxT3E3IfAnsiArchiveIntervalStatsEntry.setStatus(_A)
_NndsxT3E3IfAnsiArchiveStatsInterval_Type=Unsigned32
_NndsxT3E3IfAnsiArchiveStatsInterval_Object=MibTableColumn
nndsxT3E3IfAnsiArchiveStatsInterval=_NndsxT3E3IfAnsiArchiveStatsInterval_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,3,3,3,1,1),_NndsxT3E3IfAnsiArchiveStatsInterval_Type())
nndsxT3E3IfAnsiArchiveStatsInterval.setMaxAccess(_H)
if mibBuilder.loadTexts:nndsxT3E3IfAnsiArchiveStatsInterval.setStatus(_A)
_NndsxT3E3IfAnsiArchiveIntervalPathStatsCV_Type=Unsigned32
_NndsxT3E3IfAnsiArchiveIntervalPathStatsCV_Object=MibTableColumn
nndsxT3E3IfAnsiArchiveIntervalPathStatsCV=_NndsxT3E3IfAnsiArchiveIntervalPathStatsCV_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,3,3,3,1,2),_NndsxT3E3IfAnsiArchiveIntervalPathStatsCV_Type())
nndsxT3E3IfAnsiArchiveIntervalPathStatsCV.setMaxAccess(_B)
if mibBuilder.loadTexts:nndsxT3E3IfAnsiArchiveIntervalPathStatsCV.setStatus(_A)
_NndsxT3E3IfAnsiArchiveIntervalPathStatsES_Type=Unsigned32
_NndsxT3E3IfAnsiArchiveIntervalPathStatsES_Object=MibTableColumn
nndsxT3E3IfAnsiArchiveIntervalPathStatsES=_NndsxT3E3IfAnsiArchiveIntervalPathStatsES_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,3,3,3,1,3),_NndsxT3E3IfAnsiArchiveIntervalPathStatsES_Type())
nndsxT3E3IfAnsiArchiveIntervalPathStatsES.setMaxAccess(_B)
if mibBuilder.loadTexts:nndsxT3E3IfAnsiArchiveIntervalPathStatsES.setStatus(_A)
_NndsxT3E3IfAnsiArchiveIntervalPathStatsSES_Type=Unsigned32
_NndsxT3E3IfAnsiArchiveIntervalPathStatsSES_Object=MibTableColumn
nndsxT3E3IfAnsiArchiveIntervalPathStatsSES=_NndsxT3E3IfAnsiArchiveIntervalPathStatsSES_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,3,3,3,1,4),_NndsxT3E3IfAnsiArchiveIntervalPathStatsSES_Type())
nndsxT3E3IfAnsiArchiveIntervalPathStatsSES.setMaxAccess(_B)
if mibBuilder.loadTexts:nndsxT3E3IfAnsiArchiveIntervalPathStatsSES.setStatus(_A)
_NndsxT3E3IfAnsiArchiveIntervalPathStatsSAS_Type=Unsigned32
_NndsxT3E3IfAnsiArchiveIntervalPathStatsSAS_Object=MibTableColumn
nndsxT3E3IfAnsiArchiveIntervalPathStatsSAS=_NndsxT3E3IfAnsiArchiveIntervalPathStatsSAS_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,3,3,3,1,5),_NndsxT3E3IfAnsiArchiveIntervalPathStatsSAS_Type())
nndsxT3E3IfAnsiArchiveIntervalPathStatsSAS.setMaxAccess(_B)
if mibBuilder.loadTexts:nndsxT3E3IfAnsiArchiveIntervalPathStatsSAS.setStatus(_A)
_NndsxT3E3IfAnsiArchiveIntervalPathStatsUAS_Type=Unsigned32
_NndsxT3E3IfAnsiArchiveIntervalPathStatsUAS_Object=MibTableColumn
nndsxT3E3IfAnsiArchiveIntervalPathStatsUAS=_NndsxT3E3IfAnsiArchiveIntervalPathStatsUAS_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,3,3,3,1,6),_NndsxT3E3IfAnsiArchiveIntervalPathStatsUAS_Type())
nndsxT3E3IfAnsiArchiveIntervalPathStatsUAS.setMaxAccess(_B)
if mibBuilder.loadTexts:nndsxT3E3IfAnsiArchiveIntervalPathStatsUAS.setStatus(_A)
_NndsxT3E3IfAnsiArchiveIntervalLineStatsCV_Type=Unsigned32
_NndsxT3E3IfAnsiArchiveIntervalLineStatsCV_Object=MibTableColumn
nndsxT3E3IfAnsiArchiveIntervalLineStatsCV=_NndsxT3E3IfAnsiArchiveIntervalLineStatsCV_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,3,3,3,1,7),_NndsxT3E3IfAnsiArchiveIntervalLineStatsCV_Type())
nndsxT3E3IfAnsiArchiveIntervalLineStatsCV.setMaxAccess(_B)
if mibBuilder.loadTexts:nndsxT3E3IfAnsiArchiveIntervalLineStatsCV.setStatus(_A)
_NndsxT3E3IfAnsiArchiveIntervalLineStatsES_Type=Unsigned32
_NndsxT3E3IfAnsiArchiveIntervalLineStatsES_Object=MibTableColumn
nndsxT3E3IfAnsiArchiveIntervalLineStatsES=_NndsxT3E3IfAnsiArchiveIntervalLineStatsES_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,3,3,3,1,8),_NndsxT3E3IfAnsiArchiveIntervalLineStatsES_Type())
nndsxT3E3IfAnsiArchiveIntervalLineStatsES.setMaxAccess(_B)
if mibBuilder.loadTexts:nndsxT3E3IfAnsiArchiveIntervalLineStatsES.setStatus(_A)
_NndsxT3E3IfAnsiArchiveIntervalLineStatsSES_Type=Unsigned32
_NndsxT3E3IfAnsiArchiveIntervalLineStatsSES_Object=MibTableColumn
nndsxT3E3IfAnsiArchiveIntervalLineStatsSES=_NndsxT3E3IfAnsiArchiveIntervalLineStatsSES_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,3,3,3,1,9),_NndsxT3E3IfAnsiArchiveIntervalLineStatsSES_Type())
nndsxT3E3IfAnsiArchiveIntervalLineStatsSES.setMaxAccess(_B)
if mibBuilder.loadTexts:nndsxT3E3IfAnsiArchiveIntervalLineStatsSES.setStatus(_A)
_NndsxT3E3IfIetfStatsGroup_ObjectIdentity=ObjectIdentity
nndsxT3E3IfIetfStatsGroup=_NndsxT3E3IfIetfStatsGroup_ObjectIdentity((1,3,6,1,4,1,562,73,1,1,2,1,3,1,3,4))
_NndsxT3E3IfIetfCurrentStatsTable_Object=MibTable
nndsxT3E3IfIetfCurrentStatsTable=_NndsxT3E3IfIetfCurrentStatsTable_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,3,4,1))
if mibBuilder.loadTexts:nndsxT3E3IfIetfCurrentStatsTable.setStatus(_A)
_NndsxT3E3IfIetfCurrentStatsEntry_Object=MibTableRow
nndsxT3E3IfIetfCurrentStatsEntry=_NndsxT3E3IfIetfCurrentStatsEntry_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,3,4,1,1))
if mibBuilder.loadTexts:nndsxT3E3IfIetfCurrentStatsEntry.setStatus(_A)
_NndsxT3E3IfIetfCurrentStatsUASState_Type=TruthValue
_NndsxT3E3IfIetfCurrentStatsUASState_Object=MibTableColumn
nndsxT3E3IfIetfCurrentStatsUASState=_NndsxT3E3IfIetfCurrentStatsUASState_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,3,4,1,1,1),_NndsxT3E3IfIetfCurrentStatsUASState_Type())
nndsxT3E3IfIetfCurrentStatsUASState.setMaxAccess(_B)
if mibBuilder.loadTexts:nndsxT3E3IfIetfCurrentStatsUASState.setStatus(_A)
_NndsxT3E3IfIetfCurrentStatsTimeInCurrent_Type=Unsigned32
_NndsxT3E3IfIetfCurrentStatsTimeInCurrent_Object=MibTableColumn
nndsxT3E3IfIetfCurrentStatsTimeInCurrent=_NndsxT3E3IfIetfCurrentStatsTimeInCurrent_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,3,4,1,1,2),_NndsxT3E3IfIetfCurrentStatsTimeInCurrent_Type())
nndsxT3E3IfIetfCurrentStatsTimeInCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:nndsxT3E3IfIetfCurrentStatsTimeInCurrent.setStatus(_A)
_NndsxT3E3IfIetfCurrentStatsPES_Type=Unsigned32
_NndsxT3E3IfIetfCurrentStatsPES_Object=MibTableColumn
nndsxT3E3IfIetfCurrentStatsPES=_NndsxT3E3IfIetfCurrentStatsPES_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,3,4,1,1,3),_NndsxT3E3IfIetfCurrentStatsPES_Type())
nndsxT3E3IfIetfCurrentStatsPES.setMaxAccess(_B)
if mibBuilder.loadTexts:nndsxT3E3IfIetfCurrentStatsPES.setStatus(_A)
_NndsxT3E3IfIetfCurrentStatsPSES_Type=Unsigned32
_NndsxT3E3IfIetfCurrentStatsPSES_Object=MibTableColumn
nndsxT3E3IfIetfCurrentStatsPSES=_NndsxT3E3IfIetfCurrentStatsPSES_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,3,4,1,1,4),_NndsxT3E3IfIetfCurrentStatsPSES_Type())
nndsxT3E3IfIetfCurrentStatsPSES.setMaxAccess(_B)
if mibBuilder.loadTexts:nndsxT3E3IfIetfCurrentStatsPSES.setStatus(_A)
_NndsxT3E3IfIetfCurrentStatsSEFS_Type=Unsigned32
_NndsxT3E3IfIetfCurrentStatsSEFS_Object=MibTableColumn
nndsxT3E3IfIetfCurrentStatsSEFS=_NndsxT3E3IfIetfCurrentStatsSEFS_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,3,4,1,1,5),_NndsxT3E3IfIetfCurrentStatsSEFS_Type())
nndsxT3E3IfIetfCurrentStatsSEFS.setMaxAccess(_B)
if mibBuilder.loadTexts:nndsxT3E3IfIetfCurrentStatsSEFS.setStatus(_A)
_NndsxT3E3IfIetfCurrentStatsUAS_Type=Unsigned32
_NndsxT3E3IfIetfCurrentStatsUAS_Object=MibTableColumn
nndsxT3E3IfIetfCurrentStatsUAS=_NndsxT3E3IfIetfCurrentStatsUAS_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,3,4,1,1,6),_NndsxT3E3IfIetfCurrentStatsUAS_Type())
nndsxT3E3IfIetfCurrentStatsUAS.setMaxAccess(_B)
if mibBuilder.loadTexts:nndsxT3E3IfIetfCurrentStatsUAS.setStatus(_A)
_NndsxT3E3IfIetfCurrentStatsLCV_Type=Unsigned32
_NndsxT3E3IfIetfCurrentStatsLCV_Object=MibTableColumn
nndsxT3E3IfIetfCurrentStatsLCV=_NndsxT3E3IfIetfCurrentStatsLCV_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,3,4,1,1,7),_NndsxT3E3IfIetfCurrentStatsLCV_Type())
nndsxT3E3IfIetfCurrentStatsLCV.setMaxAccess(_B)
if mibBuilder.loadTexts:nndsxT3E3IfIetfCurrentStatsLCV.setStatus(_A)
_NndsxT3E3IfIetfCurrentStatsPCV_Type=Unsigned32
_NndsxT3E3IfIetfCurrentStatsPCV_Object=MibTableColumn
nndsxT3E3IfIetfCurrentStatsPCV=_NndsxT3E3IfIetfCurrentStatsPCV_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,3,4,1,1,8),_NndsxT3E3IfIetfCurrentStatsPCV_Type())
nndsxT3E3IfIetfCurrentStatsPCV.setMaxAccess(_B)
if mibBuilder.loadTexts:nndsxT3E3IfIetfCurrentStatsPCV.setStatus(_A)
_NndsxT3E3IfIetfCurrentStatsLES_Type=Unsigned32
_NndsxT3E3IfIetfCurrentStatsLES_Object=MibTableColumn
nndsxT3E3IfIetfCurrentStatsLES=_NndsxT3E3IfIetfCurrentStatsLES_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,3,4,1,1,9),_NndsxT3E3IfIetfCurrentStatsLES_Type())
nndsxT3E3IfIetfCurrentStatsLES.setMaxAccess(_B)
if mibBuilder.loadTexts:nndsxT3E3IfIetfCurrentStatsLES.setStatus(_A)
_NndsxT3E3IfIetfCurrentStatsCCV_Type=Unsigned32
_NndsxT3E3IfIetfCurrentStatsCCV_Object=MibTableColumn
nndsxT3E3IfIetfCurrentStatsCCV=_NndsxT3E3IfIetfCurrentStatsCCV_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,3,4,1,1,10),_NndsxT3E3IfIetfCurrentStatsCCV_Type())
nndsxT3E3IfIetfCurrentStatsCCV.setMaxAccess(_B)
if mibBuilder.loadTexts:nndsxT3E3IfIetfCurrentStatsCCV.setStatus(_A)
_NndsxT3E3IfIetfCurrentStatsCES_Type=Unsigned32
_NndsxT3E3IfIetfCurrentStatsCES_Object=MibTableColumn
nndsxT3E3IfIetfCurrentStatsCES=_NndsxT3E3IfIetfCurrentStatsCES_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,3,4,1,1,11),_NndsxT3E3IfIetfCurrentStatsCES_Type())
nndsxT3E3IfIetfCurrentStatsCES.setMaxAccess(_B)
if mibBuilder.loadTexts:nndsxT3E3IfIetfCurrentStatsCES.setStatus(_A)
_NndsxT3E3IfIetfCurrentStatsCSES_Type=Unsigned32
_NndsxT3E3IfIetfCurrentStatsCSES_Object=MibTableColumn
nndsxT3E3IfIetfCurrentStatsCSES=_NndsxT3E3IfIetfCurrentStatsCSES_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,3,4,1,1,12),_NndsxT3E3IfIetfCurrentStatsCSES_Type())
nndsxT3E3IfIetfCurrentStatsCSES.setMaxAccess(_B)
if mibBuilder.loadTexts:nndsxT3E3IfIetfCurrentStatsCSES.setStatus(_A)
_NndsxT3E3IfIetfTotalStatsTable_Object=MibTable
nndsxT3E3IfIetfTotalStatsTable=_NndsxT3E3IfIetfTotalStatsTable_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,3,4,2))
if mibBuilder.loadTexts:nndsxT3E3IfIetfTotalStatsTable.setStatus(_A)
_NndsxT3E3IfIetfTotalStatsEntry_Object=MibTableRow
nndsxT3E3IfIetfTotalStatsEntry=_NndsxT3E3IfIetfTotalStatsEntry_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,3,4,2,1))
if mibBuilder.loadTexts:nndsxT3E3IfIetfTotalStatsEntry.setStatus(_A)
_NndsxT3E3IfIetfTotalStatsPES_Type=Unsigned32
_NndsxT3E3IfIetfTotalStatsPES_Object=MibTableColumn
nndsxT3E3IfIetfTotalStatsPES=_NndsxT3E3IfIetfTotalStatsPES_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,3,4,2,1,1),_NndsxT3E3IfIetfTotalStatsPES_Type())
nndsxT3E3IfIetfTotalStatsPES.setMaxAccess(_B)
if mibBuilder.loadTexts:nndsxT3E3IfIetfTotalStatsPES.setStatus(_A)
_NndsxT3E3IfIetfTotalStatsPSES_Type=Unsigned32
_NndsxT3E3IfIetfTotalStatsPSES_Object=MibTableColumn
nndsxT3E3IfIetfTotalStatsPSES=_NndsxT3E3IfIetfTotalStatsPSES_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,3,4,2,1,2),_NndsxT3E3IfIetfTotalStatsPSES_Type())
nndsxT3E3IfIetfTotalStatsPSES.setMaxAccess(_B)
if mibBuilder.loadTexts:nndsxT3E3IfIetfTotalStatsPSES.setStatus(_A)
_NndsxT3E3IfIetfTotalStatsSEFS_Type=Unsigned32
_NndsxT3E3IfIetfTotalStatsSEFS_Object=MibTableColumn
nndsxT3E3IfIetfTotalStatsSEFS=_NndsxT3E3IfIetfTotalStatsSEFS_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,3,4,2,1,3),_NndsxT3E3IfIetfTotalStatsSEFS_Type())
nndsxT3E3IfIetfTotalStatsSEFS.setMaxAccess(_B)
if mibBuilder.loadTexts:nndsxT3E3IfIetfTotalStatsSEFS.setStatus(_A)
_NndsxT3E3IfIetfTotalStatsUAS_Type=Unsigned32
_NndsxT3E3IfIetfTotalStatsUAS_Object=MibTableColumn
nndsxT3E3IfIetfTotalStatsUAS=_NndsxT3E3IfIetfTotalStatsUAS_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,3,4,2,1,4),_NndsxT3E3IfIetfTotalStatsUAS_Type())
nndsxT3E3IfIetfTotalStatsUAS.setMaxAccess(_B)
if mibBuilder.loadTexts:nndsxT3E3IfIetfTotalStatsUAS.setStatus(_A)
_NndsxT3E3IfIetfTotalStatsLCV_Type=Unsigned32
_NndsxT3E3IfIetfTotalStatsLCV_Object=MibTableColumn
nndsxT3E3IfIetfTotalStatsLCV=_NndsxT3E3IfIetfTotalStatsLCV_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,3,4,2,1,5),_NndsxT3E3IfIetfTotalStatsLCV_Type())
nndsxT3E3IfIetfTotalStatsLCV.setMaxAccess(_B)
if mibBuilder.loadTexts:nndsxT3E3IfIetfTotalStatsLCV.setStatus(_A)
_NndsxT3E3IfIetfTotalStatsPCV_Type=Unsigned32
_NndsxT3E3IfIetfTotalStatsPCV_Object=MibTableColumn
nndsxT3E3IfIetfTotalStatsPCV=_NndsxT3E3IfIetfTotalStatsPCV_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,3,4,2,1,6),_NndsxT3E3IfIetfTotalStatsPCV_Type())
nndsxT3E3IfIetfTotalStatsPCV.setMaxAccess(_B)
if mibBuilder.loadTexts:nndsxT3E3IfIetfTotalStatsPCV.setStatus(_A)
_NndsxT3E3IfIetfTotalStatsLES_Type=Unsigned32
_NndsxT3E3IfIetfTotalStatsLES_Object=MibTableColumn
nndsxT3E3IfIetfTotalStatsLES=_NndsxT3E3IfIetfTotalStatsLES_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,3,4,2,1,7),_NndsxT3E3IfIetfTotalStatsLES_Type())
nndsxT3E3IfIetfTotalStatsLES.setMaxAccess(_B)
if mibBuilder.loadTexts:nndsxT3E3IfIetfTotalStatsLES.setStatus(_A)
_NndsxT3E3IfIetfTotalStatsCCV_Type=Unsigned32
_NndsxT3E3IfIetfTotalStatsCCV_Object=MibTableColumn
nndsxT3E3IfIetfTotalStatsCCV=_NndsxT3E3IfIetfTotalStatsCCV_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,3,4,2,1,8),_NndsxT3E3IfIetfTotalStatsCCV_Type())
nndsxT3E3IfIetfTotalStatsCCV.setMaxAccess(_B)
if mibBuilder.loadTexts:nndsxT3E3IfIetfTotalStatsCCV.setStatus(_A)
_NndsxT3E3IfIetfTotalStatsCES_Type=Unsigned32
_NndsxT3E3IfIetfTotalStatsCES_Object=MibTableColumn
nndsxT3E3IfIetfTotalStatsCES=_NndsxT3E3IfIetfTotalStatsCES_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,3,4,2,1,9),_NndsxT3E3IfIetfTotalStatsCES_Type())
nndsxT3E3IfIetfTotalStatsCES.setMaxAccess(_B)
if mibBuilder.loadTexts:nndsxT3E3IfIetfTotalStatsCES.setStatus(_A)
_NndsxT3E3IfIetfTotalStatsCSES_Type=Unsigned32
_NndsxT3E3IfIetfTotalStatsCSES_Object=MibTableColumn
nndsxT3E3IfIetfTotalStatsCSES=_NndsxT3E3IfIetfTotalStatsCSES_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,3,4,2,1,10),_NndsxT3E3IfIetfTotalStatsCSES_Type())
nndsxT3E3IfIetfTotalStatsCSES.setMaxAccess(_B)
if mibBuilder.loadTexts:nndsxT3E3IfIetfTotalStatsCSES.setStatus(_A)
_NndsxT3E3IfIetfArchiveStatsTable_Object=MibTable
nndsxT3E3IfIetfArchiveStatsTable=_NndsxT3E3IfIetfArchiveStatsTable_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,3,4,3))
if mibBuilder.loadTexts:nndsxT3E3IfIetfArchiveStatsTable.setStatus(_A)
_NndsxT3E3IfIetfArchiveStatsEntry_Object=MibTableRow
nndsxT3E3IfIetfArchiveStatsEntry=_NndsxT3E3IfIetfArchiveStatsEntry_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,3,4,3,1))
nndsxT3E3IfIetfArchiveStatsEntry.setIndexNames((0,_C,_F),(0,_C,_t))
if mibBuilder.loadTexts:nndsxT3E3IfIetfArchiveStatsEntry.setStatus(_A)
_NndsxT3E3IfIetfArchiveStatsInterval_Type=Unsigned32
_NndsxT3E3IfIetfArchiveStatsInterval_Object=MibTableColumn
nndsxT3E3IfIetfArchiveStatsInterval=_NndsxT3E3IfIetfArchiveStatsInterval_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,3,4,3,1,1),_NndsxT3E3IfIetfArchiveStatsInterval_Type())
nndsxT3E3IfIetfArchiveStatsInterval.setMaxAccess(_H)
if mibBuilder.loadTexts:nndsxT3E3IfIetfArchiveStatsInterval.setStatus(_A)
_NndsxT3E3IfIetfArchiveStatsPES_Type=Unsigned32
_NndsxT3E3IfIetfArchiveStatsPES_Object=MibTableColumn
nndsxT3E3IfIetfArchiveStatsPES=_NndsxT3E3IfIetfArchiveStatsPES_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,3,4,3,1,2),_NndsxT3E3IfIetfArchiveStatsPES_Type())
nndsxT3E3IfIetfArchiveStatsPES.setMaxAccess(_B)
if mibBuilder.loadTexts:nndsxT3E3IfIetfArchiveStatsPES.setStatus(_A)
_NndsxT3E3IfIetfArchiveStatsPSES_Type=Unsigned32
_NndsxT3E3IfIetfArchiveStatsPSES_Object=MibTableColumn
nndsxT3E3IfIetfArchiveStatsPSES=_NndsxT3E3IfIetfArchiveStatsPSES_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,3,4,3,1,3),_NndsxT3E3IfIetfArchiveStatsPSES_Type())
nndsxT3E3IfIetfArchiveStatsPSES.setMaxAccess(_B)
if mibBuilder.loadTexts:nndsxT3E3IfIetfArchiveStatsPSES.setStatus(_A)
_NndsxT3E3IfIetfArchiveStatsSEFS_Type=Unsigned32
_NndsxT3E3IfIetfArchiveStatsSEFS_Object=MibTableColumn
nndsxT3E3IfIetfArchiveStatsSEFS=_NndsxT3E3IfIetfArchiveStatsSEFS_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,3,4,3,1,4),_NndsxT3E3IfIetfArchiveStatsSEFS_Type())
nndsxT3E3IfIetfArchiveStatsSEFS.setMaxAccess(_B)
if mibBuilder.loadTexts:nndsxT3E3IfIetfArchiveStatsSEFS.setStatus(_A)
_NndsxT3E3IfIetfArchiveStatsUAS_Type=Unsigned32
_NndsxT3E3IfIetfArchiveStatsUAS_Object=MibTableColumn
nndsxT3E3IfIetfArchiveStatsUAS=_NndsxT3E3IfIetfArchiveStatsUAS_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,3,4,3,1,5),_NndsxT3E3IfIetfArchiveStatsUAS_Type())
nndsxT3E3IfIetfArchiveStatsUAS.setMaxAccess(_B)
if mibBuilder.loadTexts:nndsxT3E3IfIetfArchiveStatsUAS.setStatus(_A)
_NndsxT3E3IfIetfArchiveStatsLCV_Type=Unsigned32
_NndsxT3E3IfIetfArchiveStatsLCV_Object=MibTableColumn
nndsxT3E3IfIetfArchiveStatsLCV=_NndsxT3E3IfIetfArchiveStatsLCV_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,3,4,3,1,6),_NndsxT3E3IfIetfArchiveStatsLCV_Type())
nndsxT3E3IfIetfArchiveStatsLCV.setMaxAccess(_B)
if mibBuilder.loadTexts:nndsxT3E3IfIetfArchiveStatsLCV.setStatus(_A)
_NndsxT3E3IfIetfArchiveStatsPCV_Type=Unsigned32
_NndsxT3E3IfIetfArchiveStatsPCV_Object=MibTableColumn
nndsxT3E3IfIetfArchiveStatsPCV=_NndsxT3E3IfIetfArchiveStatsPCV_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,3,4,3,1,7),_NndsxT3E3IfIetfArchiveStatsPCV_Type())
nndsxT3E3IfIetfArchiveStatsPCV.setMaxAccess(_B)
if mibBuilder.loadTexts:nndsxT3E3IfIetfArchiveStatsPCV.setStatus(_A)
_NndsxT3E3IfIetfArchiveStatsLES_Type=Unsigned32
_NndsxT3E3IfIetfArchiveStatsLES_Object=MibTableColumn
nndsxT3E3IfIetfArchiveStatsLES=_NndsxT3E3IfIetfArchiveStatsLES_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,3,4,3,1,8),_NndsxT3E3IfIetfArchiveStatsLES_Type())
nndsxT3E3IfIetfArchiveStatsLES.setMaxAccess(_B)
if mibBuilder.loadTexts:nndsxT3E3IfIetfArchiveStatsLES.setStatus(_A)
_NndsxT3E3IfIetfArchiveStatsCCV_Type=Unsigned32
_NndsxT3E3IfIetfArchiveStatsCCV_Object=MibTableColumn
nndsxT3E3IfIetfArchiveStatsCCV=_NndsxT3E3IfIetfArchiveStatsCCV_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,3,4,3,1,9),_NndsxT3E3IfIetfArchiveStatsCCV_Type())
nndsxT3E3IfIetfArchiveStatsCCV.setMaxAccess(_B)
if mibBuilder.loadTexts:nndsxT3E3IfIetfArchiveStatsCCV.setStatus(_A)
_NndsxT3E3IfIetfArchiveStatsCES_Type=Unsigned32
_NndsxT3E3IfIetfArchiveStatsCES_Object=MibTableColumn
nndsxT3E3IfIetfArchiveStatsCES=_NndsxT3E3IfIetfArchiveStatsCES_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,3,4,3,1,10),_NndsxT3E3IfIetfArchiveStatsCES_Type())
nndsxT3E3IfIetfArchiveStatsCES.setMaxAccess(_B)
if mibBuilder.loadTexts:nndsxT3E3IfIetfArchiveStatsCES.setStatus(_A)
_NndsxT3E3IfIetfArchiveStatsCSES_Type=Unsigned32
_NndsxT3E3IfIetfArchiveStatsCSES_Object=MibTableColumn
nndsxT3E3IfIetfArchiveStatsCSES=_NndsxT3E3IfIetfArchiveStatsCSES_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,3,4,3,1,11),_NndsxT3E3IfIetfArchiveStatsCSES_Type())
nndsxT3E3IfIetfArchiveStatsCSES.setMaxAccess(_B)
if mibBuilder.loadTexts:nndsxT3E3IfIetfArchiveStatsCSES.setStatus(_A)
_NndsxT3E3IfUserStatsGroup_ObjectIdentity=ObjectIdentity
nndsxT3E3IfUserStatsGroup=_NndsxT3E3IfUserStatsGroup_ObjectIdentity((1,3,6,1,4,1,562,73,1,1,2,1,3,1,3,5))
_NndsxT3E3IfUserCurrentStatsTable_Object=MibTable
nndsxT3E3IfUserCurrentStatsTable=_NndsxT3E3IfUserCurrentStatsTable_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,3,5,1))
if mibBuilder.loadTexts:nndsxT3E3IfUserCurrentStatsTable.setStatus(_A)
_NndsxT3E3IfUserCurrentStatsEntry_Object=MibTableRow
nndsxT3E3IfUserCurrentStatsEntry=_NndsxT3E3IfUserCurrentStatsEntry_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,3,5,1,1))
if mibBuilder.loadTexts:nndsxT3E3IfUserCurrentStatsEntry.setStatus(_A)
_NndsxT3E3IfUserCurrentStatsUASState_Type=TruthValue
_NndsxT3E3IfUserCurrentStatsUASState_Object=MibTableColumn
nndsxT3E3IfUserCurrentStatsUASState=_NndsxT3E3IfUserCurrentStatsUASState_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,3,5,1,1,1),_NndsxT3E3IfUserCurrentStatsUASState_Type())
nndsxT3E3IfUserCurrentStatsUASState.setMaxAccess(_B)
if mibBuilder.loadTexts:nndsxT3E3IfUserCurrentStatsUASState.setStatus(_A)
_NndsxT3E3IfUserCurrentStatsTimeInCurrent_Type=Unsigned32
_NndsxT3E3IfUserCurrentStatsTimeInCurrent_Object=MibTableColumn
nndsxT3E3IfUserCurrentStatsTimeInCurrent=_NndsxT3E3IfUserCurrentStatsTimeInCurrent_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,3,5,1,1,2),_NndsxT3E3IfUserCurrentStatsTimeInCurrent_Type())
nndsxT3E3IfUserCurrentStatsTimeInCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:nndsxT3E3IfUserCurrentStatsTimeInCurrent.setStatus(_A)
_NndsxT3E3IfUserCurrentStatsLCV_Type=Unsigned32
_NndsxT3E3IfUserCurrentStatsLCV_Object=MibTableColumn
nndsxT3E3IfUserCurrentStatsLCV=_NndsxT3E3IfUserCurrentStatsLCV_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,3,5,1,1,3),_NndsxT3E3IfUserCurrentStatsLCV_Type())
nndsxT3E3IfUserCurrentStatsLCV.setMaxAccess(_B)
if mibBuilder.loadTexts:nndsxT3E3IfUserCurrentStatsLCV.setStatus(_A)
_NndsxT3E3IfUserCurrentStatsFBE_Type=Unsigned32
_NndsxT3E3IfUserCurrentStatsFBE_Object=MibTableColumn
nndsxT3E3IfUserCurrentStatsFBE=_NndsxT3E3IfUserCurrentStatsFBE_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,3,5,1,1,4),_NndsxT3E3IfUserCurrentStatsFBE_Type())
nndsxT3E3IfUserCurrentStatsFBE.setMaxAccess(_B)
if mibBuilder.loadTexts:nndsxT3E3IfUserCurrentStatsFBE.setStatus(_A)
_NndsxT3E3IfUserCurrentStatsPBE_Type=Unsigned32
_NndsxT3E3IfUserCurrentStatsPBE_Object=MibTableColumn
nndsxT3E3IfUserCurrentStatsPBE=_NndsxT3E3IfUserCurrentStatsPBE_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,3,5,1,1,5),_NndsxT3E3IfUserCurrentStatsPBE_Type())
nndsxT3E3IfUserCurrentStatsPBE.setMaxAccess(_B)
if mibBuilder.loadTexts:nndsxT3E3IfUserCurrentStatsPBE.setStatus(_A)
_NndsxT3E3IfUserCurrentStatsCPBE_Type=Unsigned32
_NndsxT3E3IfUserCurrentStatsCPBE_Object=MibTableColumn
nndsxT3E3IfUserCurrentStatsCPBE=_NndsxT3E3IfUserCurrentStatsCPBE_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,3,5,1,1,6),_NndsxT3E3IfUserCurrentStatsCPBE_Type())
nndsxT3E3IfUserCurrentStatsCPBE.setMaxAccess(_B)
if mibBuilder.loadTexts:nndsxT3E3IfUserCurrentStatsCPBE.setStatus(_A)
_NndsxT3E3IfUserCurrentStatsFEBE_Type=Unsigned32
_NndsxT3E3IfUserCurrentStatsFEBE_Object=MibTableColumn
nndsxT3E3IfUserCurrentStatsFEBE=_NndsxT3E3IfUserCurrentStatsFEBE_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,3,5,1,1,7),_NndsxT3E3IfUserCurrentStatsFEBE_Type())
nndsxT3E3IfUserCurrentStatsFEBE.setMaxAccess(_B)
if mibBuilder.loadTexts:nndsxT3E3IfUserCurrentStatsFEBE.setStatus(_A)
_NndsxT3E3IfUserCurrentStatsCOFA_Type=Unsigned32
_NndsxT3E3IfUserCurrentStatsCOFA_Object=MibTableColumn
nndsxT3E3IfUserCurrentStatsCOFA=_NndsxT3E3IfUserCurrentStatsCOFA_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,3,5,1,1,9),_NndsxT3E3IfUserCurrentStatsCOFA_Type())
nndsxT3E3IfUserCurrentStatsCOFA.setMaxAccess(_B)
if mibBuilder.loadTexts:nndsxT3E3IfUserCurrentStatsCOFA.setStatus(_A)
_NndsxT3E3IfUserLifetimeStatsTable_Object=MibTable
nndsxT3E3IfUserLifetimeStatsTable=_NndsxT3E3IfUserLifetimeStatsTable_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,3,5,3))
if mibBuilder.loadTexts:nndsxT3E3IfUserLifetimeStatsTable.setStatus(_A)
_NndsxT3E3IfUserLifetimeStatsEntry_Object=MibTableRow
nndsxT3E3IfUserLifetimeStatsEntry=_NndsxT3E3IfUserLifetimeStatsEntry_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,3,5,3,1))
if mibBuilder.loadTexts:nndsxT3E3IfUserLifetimeStatsEntry.setStatus(_A)
_NndsxT3E3IfUserLifetimeStatsUAS_Type=Unsigned32
_NndsxT3E3IfUserLifetimeStatsUAS_Object=MibTableColumn
nndsxT3E3IfUserLifetimeStatsUAS=_NndsxT3E3IfUserLifetimeStatsUAS_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,3,5,3,1,4),_NndsxT3E3IfUserLifetimeStatsUAS_Type())
nndsxT3E3IfUserLifetimeStatsUAS.setMaxAccess(_B)
if mibBuilder.loadTexts:nndsxT3E3IfUserLifetimeStatsUAS.setStatus(_A)
_NndsxT3E3IfUserLifetimeStatsLCV_Type=Unsigned32
_NndsxT3E3IfUserLifetimeStatsLCV_Object=MibTableColumn
nndsxT3E3IfUserLifetimeStatsLCV=_NndsxT3E3IfUserLifetimeStatsLCV_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,3,5,3,1,5),_NndsxT3E3IfUserLifetimeStatsLCV_Type())
nndsxT3E3IfUserLifetimeStatsLCV.setMaxAccess(_B)
if mibBuilder.loadTexts:nndsxT3E3IfUserLifetimeStatsLCV.setStatus(_A)
_NndsxT3E3IfUserLifetimeStatsLES_Type=Unsigned32
_NndsxT3E3IfUserLifetimeStatsLES_Object=MibTableColumn
nndsxT3E3IfUserLifetimeStatsLES=_NndsxT3E3IfUserLifetimeStatsLES_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,3,5,3,1,7),_NndsxT3E3IfUserLifetimeStatsLES_Type())
nndsxT3E3IfUserLifetimeStatsLES.setMaxAccess(_B)
if mibBuilder.loadTexts:nndsxT3E3IfUserLifetimeStatsLES.setStatus(_A)
_NndsxT3E3IfUserLifetimeStatsFBE_Type=Unsigned32
_NndsxT3E3IfUserLifetimeStatsFBE_Object=MibTableColumn
nndsxT3E3IfUserLifetimeStatsFBE=_NndsxT3E3IfUserLifetimeStatsFBE_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,3,5,3,1,10),_NndsxT3E3IfUserLifetimeStatsFBE_Type())
nndsxT3E3IfUserLifetimeStatsFBE.setMaxAccess(_B)
if mibBuilder.loadTexts:nndsxT3E3IfUserLifetimeStatsFBE.setStatus(_A)
_NndsxT3E3IfUserLifetimeStatsPBE_Type=Unsigned32
_NndsxT3E3IfUserLifetimeStatsPBE_Object=MibTableColumn
nndsxT3E3IfUserLifetimeStatsPBE=_NndsxT3E3IfUserLifetimeStatsPBE_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,3,5,3,1,11),_NndsxT3E3IfUserLifetimeStatsPBE_Type())
nndsxT3E3IfUserLifetimeStatsPBE.setMaxAccess(_B)
if mibBuilder.loadTexts:nndsxT3E3IfUserLifetimeStatsPBE.setStatus(_A)
_NndsxT3E3IfUserLifetimeStatsCPBE_Type=Unsigned32
_NndsxT3E3IfUserLifetimeStatsCPBE_Object=MibTableColumn
nndsxT3E3IfUserLifetimeStatsCPBE=_NndsxT3E3IfUserLifetimeStatsCPBE_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,3,5,3,1,12),_NndsxT3E3IfUserLifetimeStatsCPBE_Type())
nndsxT3E3IfUserLifetimeStatsCPBE.setMaxAccess(_B)
if mibBuilder.loadTexts:nndsxT3E3IfUserLifetimeStatsCPBE.setStatus(_A)
_NndsxT3E3IfUserLifetimeStatsFEBE_Type=Unsigned32
_NndsxT3E3IfUserLifetimeStatsFEBE_Object=MibTableColumn
nndsxT3E3IfUserLifetimeStatsFEBE=_NndsxT3E3IfUserLifetimeStatsFEBE_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,3,5,3,1,13),_NndsxT3E3IfUserLifetimeStatsFEBE_Type())
nndsxT3E3IfUserLifetimeStatsFEBE.setMaxAccess(_B)
if mibBuilder.loadTexts:nndsxT3E3IfUserLifetimeStatsFEBE.setStatus(_A)
_NndsxT3E3IfUserLifetimeStatsCOFA_Type=Unsigned32
_NndsxT3E3IfUserLifetimeStatsCOFA_Object=MibTableColumn
nndsxT3E3IfUserLifetimeStatsCOFA=_NndsxT3E3IfUserLifetimeStatsCOFA_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,3,5,3,1,15),_NndsxT3E3IfUserLifetimeStatsCOFA_Type())
nndsxT3E3IfUserLifetimeStatsCOFA.setMaxAccess(_B)
if mibBuilder.loadTexts:nndsxT3E3IfUserLifetimeStatsCOFA.setStatus(_A)
_NndsxT3E3IfUserArchiveStatsTable_Object=MibTable
nndsxT3E3IfUserArchiveStatsTable=_NndsxT3E3IfUserArchiveStatsTable_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,3,5,4))
if mibBuilder.loadTexts:nndsxT3E3IfUserArchiveStatsTable.setStatus(_A)
_NndsxT3E3IfUserArchiveStatsEntry_Object=MibTableRow
nndsxT3E3IfUserArchiveStatsEntry=_NndsxT3E3IfUserArchiveStatsEntry_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,3,5,4,1))
nndsxT3E3IfUserArchiveStatsEntry.setIndexNames((0,_C,_F),(0,_C,_u))
if mibBuilder.loadTexts:nndsxT3E3IfUserArchiveStatsEntry.setStatus(_A)
_NndsxT3E3IfUserArchiveStatsInterval_Type=Unsigned32
_NndsxT3E3IfUserArchiveStatsInterval_Object=MibTableColumn
nndsxT3E3IfUserArchiveStatsInterval=_NndsxT3E3IfUserArchiveStatsInterval_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,3,5,4,1,1),_NndsxT3E3IfUserArchiveStatsInterval_Type())
nndsxT3E3IfUserArchiveStatsInterval.setMaxAccess(_H)
if mibBuilder.loadTexts:nndsxT3E3IfUserArchiveStatsInterval.setStatus(_A)
_NndsxT3E3IfUserArchiveStatsLCV_Type=Unsigned32
_NndsxT3E3IfUserArchiveStatsLCV_Object=MibTableColumn
nndsxT3E3IfUserArchiveStatsLCV=_NndsxT3E3IfUserArchiveStatsLCV_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,3,5,4,1,2),_NndsxT3E3IfUserArchiveStatsLCV_Type())
nndsxT3E3IfUserArchiveStatsLCV.setMaxAccess(_B)
if mibBuilder.loadTexts:nndsxT3E3IfUserArchiveStatsLCV.setStatus(_A)
_NndsxT3E3IfUserArchiveStatsFBE_Type=Unsigned32
_NndsxT3E3IfUserArchiveStatsFBE_Object=MibTableColumn
nndsxT3E3IfUserArchiveStatsFBE=_NndsxT3E3IfUserArchiveStatsFBE_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,3,5,4,1,3),_NndsxT3E3IfUserArchiveStatsFBE_Type())
nndsxT3E3IfUserArchiveStatsFBE.setMaxAccess(_B)
if mibBuilder.loadTexts:nndsxT3E3IfUserArchiveStatsFBE.setStatus(_A)
_NndsxT3E3IfUserArchiveStatsPBE_Type=Unsigned32
_NndsxT3E3IfUserArchiveStatsPBE_Object=MibTableColumn
nndsxT3E3IfUserArchiveStatsPBE=_NndsxT3E3IfUserArchiveStatsPBE_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,3,5,4,1,4),_NndsxT3E3IfUserArchiveStatsPBE_Type())
nndsxT3E3IfUserArchiveStatsPBE.setMaxAccess(_B)
if mibBuilder.loadTexts:nndsxT3E3IfUserArchiveStatsPBE.setStatus(_A)
_NndsxT3E3IfUserArchiveStatsCPBE_Type=Unsigned32
_NndsxT3E3IfUserArchiveStatsCPBE_Object=MibTableColumn
nndsxT3E3IfUserArchiveStatsCPBE=_NndsxT3E3IfUserArchiveStatsCPBE_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,3,5,4,1,5),_NndsxT3E3IfUserArchiveStatsCPBE_Type())
nndsxT3E3IfUserArchiveStatsCPBE.setMaxAccess(_B)
if mibBuilder.loadTexts:nndsxT3E3IfUserArchiveStatsCPBE.setStatus(_A)
_NndsxT3E3IfUserArchiveStatsFEBE_Type=Unsigned32
_NndsxT3E3IfUserArchiveStatsFEBE_Object=MibTableColumn
nndsxT3E3IfUserArchiveStatsFEBE=_NndsxT3E3IfUserArchiveStatsFEBE_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,3,5,4,1,6),_NndsxT3E3IfUserArchiveStatsFEBE_Type())
nndsxT3E3IfUserArchiveStatsFEBE.setMaxAccess(_B)
if mibBuilder.loadTexts:nndsxT3E3IfUserArchiveStatsFEBE.setStatus(_A)
_NndsxT3E3IfUserArchiveStatsCOFA_Type=Unsigned32
_NndsxT3E3IfUserArchiveStatsCOFA_Object=MibTableColumn
nndsxT3E3IfUserArchiveStatsCOFA=_NndsxT3E3IfUserArchiveStatsCOFA_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,1,3,5,4,1,8),_NndsxT3E3IfUserArchiveStatsCOFA_Type())
nndsxT3E3IfUserArchiveStatsCOFA.setMaxAccess(_B)
if mibBuilder.loadTexts:nndsxT3E3IfUserArchiveStatsCOFA.setStatus(_A)
_NndsxT3E3Traps_ObjectIdentity=ObjectIdentity
nndsxT3E3Traps=_NndsxT3E3Traps_ObjectIdentity((1,3,6,1,4,1,562,73,1,1,2,1,3,2))
_NndsxT3E3Notifications_ObjectIdentity=ObjectIdentity
nndsxT3E3Notifications=_NndsxT3E3Notifications_ObjectIdentity((1,3,6,1,4,1,562,73,1,1,2,1,3,2,0))
_NndsxT3E3TrapVariables_ObjectIdentity=ObjectIdentity
nndsxT3E3TrapVariables=_NndsxT3E3TrapVariables_ObjectIdentity((1,3,6,1,4,1,562,73,1,1,2,1,3,2,1))
class _NndsxT3E3Number_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_NndsxT3E3Number_Type.__name__=_O
_NndsxT3E3Number_Object=MibScalar
nndsxT3E3Number=_NndsxT3E3Number_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,2,1,1),_NndsxT3E3Number_Type())
nndsxT3E3Number.setMaxAccess(_I)
if mibBuilder.loadTexts:nndsxT3E3Number.setStatus(_A)
class _NndsxT3E3AlarmType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26)));namedValues=NamedValues(*(('te3-alarm-rais',1),('te3-alarm-roof',2),('te3-alarm-rrai',3),('te3-alarm-ris',4),('te3-alarm-rlos',5),('te3-alarm-rlof',6),('te3-alarm-rexz',7),('te3-alarm-rfebe',8),('te3-alarm-rpe',9),('te3-alarm-rcpe',10),('te3-alarm-lorc',11),('te3-alarm-tpde',12),('te3-alarm-tais',13),('te3-alarm-trai',14),('te3-alarm-tfebe',15),('te3-alarm-ibtest',16),('te1-alarm-threshold1',17),('te1-alarm-threshold2',18),('te1-alarm-threshold3',19),('te1-alarm-threshold4',20),('te1-alarm-threshold5',21),('te1-alarm-threshold6',22),('te1-alarm-threshold7',23),('te1-alarm-threshold8',24),('te1-alarm-threshold9',25),('te1-alarm-threshold10',26)))
_NndsxT3E3AlarmType_Type.__name__=_D
_NndsxT3E3AlarmType_Object=MibScalar
nndsxT3E3AlarmType=_NndsxT3E3AlarmType_Object((1,3,6,1,4,1,562,73,1,1,2,1,3,2,1,2),_NndsxT3E3AlarmType_Type())
nndsxT3E3AlarmType.setMaxAccess(_I)
if mibBuilder.loadTexts:nndsxT3E3AlarmType.setStatus(_A)
nndsxT3E3IfConfigLineEntry.registerAugmentions((_C,_v))
nndsxT3E3IfTestConfigEntry.setIndexNames(*nndsxT3E3IfConfigLineEntry.getIndexNames())
nndsxT3E3IfConfigLineEntry.registerAugmentions((_C,_w))
nndsxT3E3IfStatusEntry.setIndexNames(*nndsxT3E3IfConfigLineEntry.getIndexNames())
nndsxT3E3IfConfigLineEntry.registerAugmentions((_C,_x))
nndsxT3E3IfAlarmStatusEntry.setIndexNames(*nndsxT3E3IfConfigLineEntry.getIndexNames())
nndsxT3E3IfConfigLineEntry.registerAugmentions((_C,_y))
nndsxT3E3IfTestStatusEntry.setIndexNames(*nndsxT3E3IfConfigLineEntry.getIndexNames())
nndsxT3E3IfConfigLineEntry.registerAugmentions((_C,_z))
nndsxT3E3IfLastTestResultEntry.setIndexNames(*nndsxT3E3IfConfigLineEntry.getIndexNames())
nndsxT3E3IfConfigLineEntry.registerAugmentions((_C,_A0))
nndsxT3E3IfArchiveStatsValidIntervalsEntry.setIndexNames(*nndsxT3E3IfConfigLineEntry.getIndexNames())
nndsxT3E3IfConfigLineEntry.registerAugmentions((_C,_A1))
nndsxT3E3IfErrorEventStatsEntry.setIndexNames(*nndsxT3E3IfConfigLineEntry.getIndexNames())
nndsxT3E3IfConfigLineEntry.registerAugmentions((_C,_A2))
nndsxT3E3IfAnsiCurrentStatsEntry.setIndexNames(*nndsxT3E3IfConfigLineEntry.getIndexNames())
nndsxT3E3IfConfigLineEntry.registerAugmentions((_C,_A3))
nndsxT3E3IfAnsiTotalStatsEntry.setIndexNames(*nndsxT3E3IfConfigLineEntry.getIndexNames())
nndsxT3E3IfConfigLineEntry.registerAugmentions((_C,_A4))
nndsxT3E3IfIetfCurrentStatsEntry.setIndexNames(*nndsxT3E3IfConfigLineEntry.getIndexNames())
nndsxT3E3IfConfigLineEntry.registerAugmentions((_C,_A5))
nndsxT3E3IfIetfTotalStatsEntry.setIndexNames(*nndsxT3E3IfConfigLineEntry.getIndexNames())
nndsxT3E3IfConfigLineEntry.registerAugmentions((_C,_A6))
nndsxT3E3IfUserCurrentStatsEntry.setIndexNames(*nndsxT3E3IfConfigLineEntry.getIndexNames())
nndsxT3E3IfConfigLineEntry.registerAugmentions((_C,_A7))
nndsxT3E3IfUserLifetimeStatsEntry.setIndexNames(*nndsxT3E3IfConfigLineEntry.getIndexNames())
nndsxT3E3AlarmOnTrap=NotificationType((1,3,6,1,4,1,562,73,1,1,2,1,3,2,0,1))
nndsxT3E3AlarmOnTrap.setObjects(*((_C,_F),(_C,_M),(_C,_N)))
if mibBuilder.loadTexts:nndsxT3E3AlarmOnTrap.setStatus(_A)
nndsxT3E3AlarmOffTrap=NotificationType((1,3,6,1,4,1,562,73,1,1,2,1,3,2,0,2))
nndsxT3E3AlarmOffTrap.setObjects(*((_C,_F),(_C,_M),(_C,_N)))
if mibBuilder.loadTexts:nndsxT3E3AlarmOffTrap.setStatus(_A)
nndsxT3E3NotificationGroup=NotificationGroup((1,3,6,1,4,1,562,73,1,1,2,1,3,3))
nndsxT3E3NotificationGroup.setObjects(*((_C,_A8),(_C,_A9)))
if mibBuilder.loadTexts:nndsxT3E3NotificationGroup.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'nndsxT3E3MIB':nndsxT3E3MIB,'nndsxT3E3IfConfigGroup':nndsxT3E3IfConfigGroup,'nndsxT3E3IfConfigLineTable':nndsxT3E3IfConfigLineTable,'nndsxT3E3IfConfigLineEntry':nndsxT3E3IfConfigLineEntry,_F:nndsxT3E3IfIndex,'nndsxT3E3IfConfigLineType':nndsxT3E3IfConfigLineType,'nndsxT3E3IfConfigLineCode':nndsxT3E3IfConfigLineCode,'nndsxT3E3IfConfigCableLength':nndsxT3E3IfConfigCableLength,'nndsxT3E3IfConfigTransmitClock':nndsxT3E3IfConfigTransmitClock,'nndsxT3E3IfAlarmConfigGroup':nndsxT3E3IfAlarmConfigGroup,'nndsxT3E3IfAlarmThresholdConfigTable':nndsxT3E3IfAlarmThresholdConfigTable,'nndsxT3E3IfAlarmThresholdConfigEntry':nndsxT3E3IfAlarmThresholdConfigEntry,_R:nndsxT3E3IfAlarmThresholdConfigIndex,'nndsxT3E3IfAlarmThresholdConfigObject':nndsxT3E3IfAlarmThresholdConfigObject,'nndsxT3E3IfAlarmThresholdConfigSamplingInterval':nndsxT3E3IfAlarmThresholdConfigSamplingInterval,'nndsxT3E3IfAlarmThresholdConfigSampleType':nndsxT3E3IfAlarmThresholdConfigSampleType,'nndsxT3E3IfAlarmThresholdConfigRisingThreshold':nndsxT3E3IfAlarmThresholdConfigRisingThreshold,'nndsxT3E3IfAlarmThresholdConfigFallingThreshold':nndsxT3E3IfAlarmThresholdConfigFallingThreshold,'nndsxT3E3IfAlarmThresholdConfigEnable':nndsxT3E3IfAlarmThresholdConfigEnable,'nndsxT3E3IfTestConfigTable':nndsxT3E3IfTestConfigTable,_v:nndsxT3E3IfTestConfigEntry,'nndsxT3E3IfTestConfigType':nndsxT3E3IfTestConfigType,'nndsxT3E3IfTestConfigLoopCode':nndsxT3E3IfTestConfigLoopCode,'nndsxT3E3IfTestConfigPattern':nndsxT3E3IfTestConfigPattern,'nndsxT3E3IfTestConfigTime':nndsxT3E3IfTestConfigTime,'nndsxT3E3IfStatusGroup':nndsxT3E3IfStatusGroup,'nndsxT3E3IfStatusTable':nndsxT3E3IfStatusTable,_w:nndsxT3E3IfStatusEntry,'nndsxT3E3IfStatusLineStatus':nndsxT3E3IfStatusLineStatus,'nndsxT3E3IfStatusTransmitClock':nndsxT3E3IfStatusTransmitClock,'nndsxT3E3IfAlarmStatusTable':nndsxT3E3IfAlarmStatusTable,_x:nndsxT3E3IfAlarmStatusEntry,'nndsxT3E3IfAlarmStatusAlarmStatus':nndsxT3E3IfAlarmStatusAlarmStatus,'nndsxT3E3IfAlarmStatusThresholdStatus':nndsxT3E3IfAlarmStatusThresholdStatus,'nndsxT3E3IfTestStatusTable':nndsxT3E3IfTestStatusTable,_y:nndsxT3E3IfTestStatusEntry,'nndsxT3E3IfTestStatusTestType':nndsxT3E3IfTestStatusTestType,'nndsxT3E3IfTestStatusTestState':nndsxT3E3IfTestStatusTestState,'nndsxT3E3IfTestStatusLoopCode':nndsxT3E3IfTestStatusLoopCode,'nndsxT3E3IfLastTestResultTable':nndsxT3E3IfLastTestResultTable,_z:nndsxT3E3IfLastTestResultEntry,'nndsxT3E3IfLastTestResultTestType':nndsxT3E3IfLastTestResultTestType,'nndsxT3E3IfLastTestResultTestState':nndsxT3E3IfLastTestResultTestState,'nndsxT3E3IfLastTestResultLoopCode':nndsxT3E3IfLastTestResultLoopCode,'nndsxT3E3IfStatsGroup':nndsxT3E3IfStatsGroup,'nndsxT3E3IfArchiveStatsValidIntervalsTable':nndsxT3E3IfArchiveStatsValidIntervalsTable,_A0:nndsxT3E3IfArchiveStatsValidIntervalsEntry,'nndsxT3E3IfAnsiArchiveStatsValidIntervals':nndsxT3E3IfAnsiArchiveStatsValidIntervals,'nndsxT3E3IfIetfArchiveStatsValidIntervals':nndsxT3E3IfIetfArchiveStatsValidIntervals,'nndsxT3E3IfUserTotalStatsValidDays':nndsxT3E3IfUserTotalStatsValidDays,'nndsxT3E3IfUserArchiveStatsValidIntervals':nndsxT3E3IfUserArchiveStatsValidIntervals,'nndsxT3E3IfErrorEventStatsTable':nndsxT3E3IfErrorEventStatsTable,_A1:nndsxT3E3IfErrorEventStatsEntry,'nndsxT3E3IfErrorEventStatsPBE':nndsxT3E3IfErrorEventStatsPBE,'nndsxT3E3IfErrorEventStatsFEBE':nndsxT3E3IfErrorEventStatsFEBE,'nndsxT3E3IfAnsiStatsGroup':nndsxT3E3IfAnsiStatsGroup,'nndsxT3E3IfAnsiCurrentStatsTable':nndsxT3E3IfAnsiCurrentStatsTable,_A2:nndsxT3E3IfAnsiCurrentStatsEntry,'nndsxT3E3IfAnsiCurrentStatsUASState':nndsxT3E3IfAnsiCurrentStatsUASState,'nndsxT3E3IfAnsiCurrentStatsTimeInCurrent':nndsxT3E3IfAnsiCurrentStatsTimeInCurrent,'nndsxT3E3IfAnsiCurrentPathStatsCV':nndsxT3E3IfAnsiCurrentPathStatsCV,'nndsxT3E3IfAnsiCurrentPathStatsES':nndsxT3E3IfAnsiCurrentPathStatsES,'nndsxT3E3IfAnsiCurrentPathStatsSES':nndsxT3E3IfAnsiCurrentPathStatsSES,'nndsxT3E3IfAnsiCurrentPathStatsSAS':nndsxT3E3IfAnsiCurrentPathStatsSAS,'nndsxT3E3IfAnsiCurrentPathStatsUAS':nndsxT3E3IfAnsiCurrentPathStatsUAS,'nndsxT3E3IfAnsiCurrentLineStatsCV':nndsxT3E3IfAnsiCurrentLineStatsCV,'nndsxT3E3IfAnsiCurrentLineStatsES':nndsxT3E3IfAnsiCurrentLineStatsES,'nndsxT3E3IfAnsiCurrentLineStatsSES':nndsxT3E3IfAnsiCurrentLineStatsSES,'nndsxT3E3IfAnsiTotalStatsTable':nndsxT3E3IfAnsiTotalStatsTable,_A3:nndsxT3E3IfAnsiTotalStatsEntry,'nndsxT3E3IfAnsiTotalPathStatsCV':nndsxT3E3IfAnsiTotalPathStatsCV,'nndsxT3E3IfAnsiTotalPathStatsES':nndsxT3E3IfAnsiTotalPathStatsES,'nndsxT3E3IfAnsiTotalPathStatsSES':nndsxT3E3IfAnsiTotalPathStatsSES,'nndsxT3E3IfAnsiTotalPathStatsSAS':nndsxT3E3IfAnsiTotalPathStatsSAS,'nndsxT3E3IfAnsiTotalPathStatsUAS':nndsxT3E3IfAnsiTotalPathStatsUAS,'nndsxT3E3IfAnsiTotalLineStatsCV':nndsxT3E3IfAnsiTotalLineStatsCV,'nndsxT3E3IfAnsiTotalLineStatsES':nndsxT3E3IfAnsiTotalLineStatsES,'nndsxT3E3IfAnsiTotalLineStatsSES':nndsxT3E3IfAnsiTotalLineStatsSES,'nndsxT3E3IfAnsiArchiveIntervalStatsTable':nndsxT3E3IfAnsiArchiveIntervalStatsTable,'nndsxT3E3IfAnsiArchiveIntervalStatsEntry':nndsxT3E3IfAnsiArchiveIntervalStatsEntry,_s:nndsxT3E3IfAnsiArchiveStatsInterval,'nndsxT3E3IfAnsiArchiveIntervalPathStatsCV':nndsxT3E3IfAnsiArchiveIntervalPathStatsCV,'nndsxT3E3IfAnsiArchiveIntervalPathStatsES':nndsxT3E3IfAnsiArchiveIntervalPathStatsES,'nndsxT3E3IfAnsiArchiveIntervalPathStatsSES':nndsxT3E3IfAnsiArchiveIntervalPathStatsSES,'nndsxT3E3IfAnsiArchiveIntervalPathStatsSAS':nndsxT3E3IfAnsiArchiveIntervalPathStatsSAS,'nndsxT3E3IfAnsiArchiveIntervalPathStatsUAS':nndsxT3E3IfAnsiArchiveIntervalPathStatsUAS,'nndsxT3E3IfAnsiArchiveIntervalLineStatsCV':nndsxT3E3IfAnsiArchiveIntervalLineStatsCV,'nndsxT3E3IfAnsiArchiveIntervalLineStatsES':nndsxT3E3IfAnsiArchiveIntervalLineStatsES,'nndsxT3E3IfAnsiArchiveIntervalLineStatsSES':nndsxT3E3IfAnsiArchiveIntervalLineStatsSES,'nndsxT3E3IfIetfStatsGroup':nndsxT3E3IfIetfStatsGroup,'nndsxT3E3IfIetfCurrentStatsTable':nndsxT3E3IfIetfCurrentStatsTable,_A4:nndsxT3E3IfIetfCurrentStatsEntry,'nndsxT3E3IfIetfCurrentStatsUASState':nndsxT3E3IfIetfCurrentStatsUASState,'nndsxT3E3IfIetfCurrentStatsTimeInCurrent':nndsxT3E3IfIetfCurrentStatsTimeInCurrent,'nndsxT3E3IfIetfCurrentStatsPES':nndsxT3E3IfIetfCurrentStatsPES,'nndsxT3E3IfIetfCurrentStatsPSES':nndsxT3E3IfIetfCurrentStatsPSES,'nndsxT3E3IfIetfCurrentStatsSEFS':nndsxT3E3IfIetfCurrentStatsSEFS,'nndsxT3E3IfIetfCurrentStatsUAS':nndsxT3E3IfIetfCurrentStatsUAS,'nndsxT3E3IfIetfCurrentStatsLCV':nndsxT3E3IfIetfCurrentStatsLCV,'nndsxT3E3IfIetfCurrentStatsPCV':nndsxT3E3IfIetfCurrentStatsPCV,'nndsxT3E3IfIetfCurrentStatsLES':nndsxT3E3IfIetfCurrentStatsLES,'nndsxT3E3IfIetfCurrentStatsCCV':nndsxT3E3IfIetfCurrentStatsCCV,'nndsxT3E3IfIetfCurrentStatsCES':nndsxT3E3IfIetfCurrentStatsCES,'nndsxT3E3IfIetfCurrentStatsCSES':nndsxT3E3IfIetfCurrentStatsCSES,'nndsxT3E3IfIetfTotalStatsTable':nndsxT3E3IfIetfTotalStatsTable,_A5:nndsxT3E3IfIetfTotalStatsEntry,'nndsxT3E3IfIetfTotalStatsPES':nndsxT3E3IfIetfTotalStatsPES,'nndsxT3E3IfIetfTotalStatsPSES':nndsxT3E3IfIetfTotalStatsPSES,'nndsxT3E3IfIetfTotalStatsSEFS':nndsxT3E3IfIetfTotalStatsSEFS,'nndsxT3E3IfIetfTotalStatsUAS':nndsxT3E3IfIetfTotalStatsUAS,'nndsxT3E3IfIetfTotalStatsLCV':nndsxT3E3IfIetfTotalStatsLCV,'nndsxT3E3IfIetfTotalStatsPCV':nndsxT3E3IfIetfTotalStatsPCV,'nndsxT3E3IfIetfTotalStatsLES':nndsxT3E3IfIetfTotalStatsLES,'nndsxT3E3IfIetfTotalStatsCCV':nndsxT3E3IfIetfTotalStatsCCV,'nndsxT3E3IfIetfTotalStatsCES':nndsxT3E3IfIetfTotalStatsCES,'nndsxT3E3IfIetfTotalStatsCSES':nndsxT3E3IfIetfTotalStatsCSES,'nndsxT3E3IfIetfArchiveStatsTable':nndsxT3E3IfIetfArchiveStatsTable,'nndsxT3E3IfIetfArchiveStatsEntry':nndsxT3E3IfIetfArchiveStatsEntry,_t:nndsxT3E3IfIetfArchiveStatsInterval,'nndsxT3E3IfIetfArchiveStatsPES':nndsxT3E3IfIetfArchiveStatsPES,'nndsxT3E3IfIetfArchiveStatsPSES':nndsxT3E3IfIetfArchiveStatsPSES,'nndsxT3E3IfIetfArchiveStatsSEFS':nndsxT3E3IfIetfArchiveStatsSEFS,'nndsxT3E3IfIetfArchiveStatsUAS':nndsxT3E3IfIetfArchiveStatsUAS,'nndsxT3E3IfIetfArchiveStatsLCV':nndsxT3E3IfIetfArchiveStatsLCV,'nndsxT3E3IfIetfArchiveStatsPCV':nndsxT3E3IfIetfArchiveStatsPCV,'nndsxT3E3IfIetfArchiveStatsLES':nndsxT3E3IfIetfArchiveStatsLES,'nndsxT3E3IfIetfArchiveStatsCCV':nndsxT3E3IfIetfArchiveStatsCCV,'nndsxT3E3IfIetfArchiveStatsCES':nndsxT3E3IfIetfArchiveStatsCES,'nndsxT3E3IfIetfArchiveStatsCSES':nndsxT3E3IfIetfArchiveStatsCSES,'nndsxT3E3IfUserStatsGroup':nndsxT3E3IfUserStatsGroup,'nndsxT3E3IfUserCurrentStatsTable':nndsxT3E3IfUserCurrentStatsTable,_A6:nndsxT3E3IfUserCurrentStatsEntry,'nndsxT3E3IfUserCurrentStatsUASState':nndsxT3E3IfUserCurrentStatsUASState,'nndsxT3E3IfUserCurrentStatsTimeInCurrent':nndsxT3E3IfUserCurrentStatsTimeInCurrent,'nndsxT3E3IfUserCurrentStatsLCV':nndsxT3E3IfUserCurrentStatsLCV,'nndsxT3E3IfUserCurrentStatsFBE':nndsxT3E3IfUserCurrentStatsFBE,'nndsxT3E3IfUserCurrentStatsPBE':nndsxT3E3IfUserCurrentStatsPBE,'nndsxT3E3IfUserCurrentStatsCPBE':nndsxT3E3IfUserCurrentStatsCPBE,'nndsxT3E3IfUserCurrentStatsFEBE':nndsxT3E3IfUserCurrentStatsFEBE,'nndsxT3E3IfUserCurrentStatsCOFA':nndsxT3E3IfUserCurrentStatsCOFA,'nndsxT3E3IfUserLifetimeStatsTable':nndsxT3E3IfUserLifetimeStatsTable,_A7:nndsxT3E3IfUserLifetimeStatsEntry,'nndsxT3E3IfUserLifetimeStatsUAS':nndsxT3E3IfUserLifetimeStatsUAS,'nndsxT3E3IfUserLifetimeStatsLCV':nndsxT3E3IfUserLifetimeStatsLCV,'nndsxT3E3IfUserLifetimeStatsLES':nndsxT3E3IfUserLifetimeStatsLES,'nndsxT3E3IfUserLifetimeStatsFBE':nndsxT3E3IfUserLifetimeStatsFBE,'nndsxT3E3IfUserLifetimeStatsPBE':nndsxT3E3IfUserLifetimeStatsPBE,'nndsxT3E3IfUserLifetimeStatsCPBE':nndsxT3E3IfUserLifetimeStatsCPBE,'nndsxT3E3IfUserLifetimeStatsFEBE':nndsxT3E3IfUserLifetimeStatsFEBE,'nndsxT3E3IfUserLifetimeStatsCOFA':nndsxT3E3IfUserLifetimeStatsCOFA,'nndsxT3E3IfUserArchiveStatsTable':nndsxT3E3IfUserArchiveStatsTable,'nndsxT3E3IfUserArchiveStatsEntry':nndsxT3E3IfUserArchiveStatsEntry,_u:nndsxT3E3IfUserArchiveStatsInterval,'nndsxT3E3IfUserArchiveStatsLCV':nndsxT3E3IfUserArchiveStatsLCV,'nndsxT3E3IfUserArchiveStatsFBE':nndsxT3E3IfUserArchiveStatsFBE,'nndsxT3E3IfUserArchiveStatsPBE':nndsxT3E3IfUserArchiveStatsPBE,'nndsxT3E3IfUserArchiveStatsCPBE':nndsxT3E3IfUserArchiveStatsCPBE,'nndsxT3E3IfUserArchiveStatsFEBE':nndsxT3E3IfUserArchiveStatsFEBE,'nndsxT3E3IfUserArchiveStatsCOFA':nndsxT3E3IfUserArchiveStatsCOFA,'nndsxT3E3Traps':nndsxT3E3Traps,'nndsxT3E3Notifications':nndsxT3E3Notifications,_A8:nndsxT3E3AlarmOnTrap,_A9:nndsxT3E3AlarmOffTrap,'nndsxT3E3TrapVariables':nndsxT3E3TrapVariables,_M:nndsxT3E3Number,_N:nndsxT3E3AlarmType,'nndsxT3E3NotificationGroup':nndsxT3E3NotificationGroup})