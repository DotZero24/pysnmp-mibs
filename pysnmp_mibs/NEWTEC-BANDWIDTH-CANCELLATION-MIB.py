_e='ntcBwCConfGrpV1Standard'
_d='ntcBwCASNoLock'
_c='ntcBwCMonLocalSpectralInversion'
_b='ntcBwCMonLocalFreqOffset'
_a='ntcBwCMonLocalSymbolRate'
_Z='ntcBwCMonLocalLevel'
_Y='ntcBwCMonLocalToRemotePowerRatio'
_X='ntcBwCMonLocalToTotalPowerRatio'
_W='ntcBwCMonRoundTripDelay'
_V='ntcBwCMonState'
_U='ntcBwCCfgBandwidthMode'
_T='ntcBwCCfgLocalSpectralInversion'
_S='ntcBwCCfgLocalCenterFreqUncert'
_R='ntcBwCCfgLocalCenterFreqOffset'
_Q='ntcBwCCfgRoundTripDelayUncert'
_P='ntcBwCCfgExpRoundTripDelay'
_O='ntcBwCCfgEnable'
_N='ntcBwCAlarmNoLock'
_M='ntcBwCAlarmStateEntry'
_L='ntcBwCMonEntry'
_K='inverted'
_J='direct'
_I='ntcBwCCfgName'
_H='DisplayString'
_G='NtcEnable'
_F='Unsigned32'
_E='Integer32'
_D='read-write'
_C='read-only'
_B='NEWTEC-BANDWIDTH-CANCELLATION-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
Float32TC,=mibBuilder.importSymbols('FLOAT-TC-MIB','Float32TC')
ntcFunction,=mibBuilder.importSymbols('NEWTEC-MAIN-MIB','ntcFunction')
NtcAlarmState,NtcEnable=mibBuilder.importSymbols('NEWTEC-TC-MIB','NtcAlarmState',_G)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_H,'PhysAddress','TextualConvention')
ntcBandwidthCancellation=ModuleIdentity((1,3,6,1,4,1,5835,5,2,9100))
if mibBuilder.loadTexts:ntcBandwidthCancellation.setRevisions(('2016-02-01 11:00',))
_NtcBwCObjects_ObjectIdentity=ObjectIdentity
ntcBwCObjects=_NtcBwCObjects_ObjectIdentity((1,3,6,1,4,1,5835,5,2,9100,1))
if mibBuilder.loadTexts:ntcBwCObjects.setStatus(_A)
_NtcBwCAlarm_ObjectIdentity=ObjectIdentity
ntcBwCAlarm=_NtcBwCAlarm_ObjectIdentity((1,3,6,1,4,1,5835,5,2,9100,1,1))
if mibBuilder.loadTexts:ntcBwCAlarm.setStatus(_A)
_NtcBwCAlarmNoLock_Type=NtcAlarmState
_NtcBwCAlarmNoLock_Object=MibScalar
ntcBwCAlarmNoLock=_NtcBwCAlarmNoLock_Object((1,3,6,1,4,1,5835,5,2,9100,1,1,1),_NtcBwCAlarmNoLock_Type())
ntcBwCAlarmNoLock.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcBwCAlarmNoLock.setStatus(_A)
_NtcBwCCfgTable_Object=MibTable
ntcBwCCfgTable=_NtcBwCCfgTable_Object((1,3,6,1,4,1,5835,5,2,9100,1,2))
if mibBuilder.loadTexts:ntcBwCCfgTable.setStatus(_A)
_NtcBwCCfgEntry_Object=MibTableRow
ntcBwCCfgEntry=_NtcBwCCfgEntry_Object((1,3,6,1,4,1,5835,5,2,9100,1,2,1))
ntcBwCCfgEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:ntcBwCCfgEntry.setStatus(_A)
class _NtcBwCCfgName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_NtcBwCCfgName_Type.__name__=_H
_NtcBwCCfgName_Object=MibTableColumn
ntcBwCCfgName=_NtcBwCCfgName_Object((1,3,6,1,4,1,5835,5,2,9100,1,2,1,1),_NtcBwCCfgName_Type())
ntcBwCCfgName.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:ntcBwCCfgName.setStatus(_A)
class _NtcBwCCfgEnable_Type(NtcEnable):defaultValue=0
_NtcBwCCfgEnable_Type.__name__=_G
_NtcBwCCfgEnable_Object=MibTableColumn
ntcBwCCfgEnable=_NtcBwCCfgEnable_Object((1,3,6,1,4,1,5835,5,2,9100,1,2,1,2),_NtcBwCCfgEnable_Type())
ntcBwCCfgEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcBwCCfgEnable.setStatus(_A)
class _NtcBwCCfgExpRoundTripDelay_Type(Unsigned32):defaultValue=250;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,500))
_NtcBwCCfgExpRoundTripDelay_Type.__name__=_F
_NtcBwCCfgExpRoundTripDelay_Object=MibTableColumn
ntcBwCCfgExpRoundTripDelay=_NtcBwCCfgExpRoundTripDelay_Object((1,3,6,1,4,1,5835,5,2,9100,1,2,1,3),_NtcBwCCfgExpRoundTripDelay_Type())
ntcBwCCfgExpRoundTripDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcBwCCfgExpRoundTripDelay.setStatus(_A)
if mibBuilder.loadTexts:ntcBwCCfgExpRoundTripDelay.setUnits('ms')
class _NtcBwCCfgRoundTripDelayUncert_Type(Unsigned32):defaultValue=20;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_NtcBwCCfgRoundTripDelayUncert_Type.__name__=_F
_NtcBwCCfgRoundTripDelayUncert_Object=MibTableColumn
ntcBwCCfgRoundTripDelayUncert=_NtcBwCCfgRoundTripDelayUncert_Object((1,3,6,1,4,1,5835,5,2,9100,1,2,1,4),_NtcBwCCfgRoundTripDelayUncert_Type())
ntcBwCCfgRoundTripDelayUncert.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcBwCCfgRoundTripDelayUncert.setStatus(_A)
if mibBuilder.loadTexts:ntcBwCCfgRoundTripDelayUncert.setUnits('ms')
class _NtcBwCCfgLocalCenterFreqOffset_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-100000000,100000000))
_NtcBwCCfgLocalCenterFreqOffset_Type.__name__=_E
_NtcBwCCfgLocalCenterFreqOffset_Object=MibTableColumn
ntcBwCCfgLocalCenterFreqOffset=_NtcBwCCfgLocalCenterFreqOffset_Object((1,3,6,1,4,1,5835,5,2,9100,1,2,1,5),_NtcBwCCfgLocalCenterFreqOffset_Type())
ntcBwCCfgLocalCenterFreqOffset.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcBwCCfgLocalCenterFreqOffset.setStatus(_A)
if mibBuilder.loadTexts:ntcBwCCfgLocalCenterFreqOffset.setUnits('Hz')
class _NtcBwCCfgLocalCenterFreqUncert_Type(Unsigned32):defaultValue=50000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(50000,7500000))
_NtcBwCCfgLocalCenterFreqUncert_Type.__name__=_F
_NtcBwCCfgLocalCenterFreqUncert_Object=MibTableColumn
ntcBwCCfgLocalCenterFreqUncert=_NtcBwCCfgLocalCenterFreqUncert_Object((1,3,6,1,4,1,5835,5,2,9100,1,2,1,6),_NtcBwCCfgLocalCenterFreqUncert_Type())
ntcBwCCfgLocalCenterFreqUncert.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcBwCCfgLocalCenterFreqUncert.setStatus(_A)
if mibBuilder.loadTexts:ntcBwCCfgLocalCenterFreqUncert.setUnits('Hz')
class _NtcBwCCfgLocalSpectralInversion_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_J,0),(_K,1),('automatic',2)))
_NtcBwCCfgLocalSpectralInversion_Type.__name__=_E
_NtcBwCCfgLocalSpectralInversion_Object=MibTableColumn
ntcBwCCfgLocalSpectralInversion=_NtcBwCCfgLocalSpectralInversion_Object((1,3,6,1,4,1,5835,5,2,9100,1,2,1,7),_NtcBwCCfgLocalSpectralInversion_Type())
ntcBwCCfgLocalSpectralInversion.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcBwCCfgLocalSpectralInversion.setStatus(_A)
class _NtcBwCCfgBandwidthMode_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('normal',0),('robust',1),('fine',2)))
_NtcBwCCfgBandwidthMode_Type.__name__=_E
_NtcBwCCfgBandwidthMode_Object=MibTableColumn
ntcBwCCfgBandwidthMode=_NtcBwCCfgBandwidthMode_Object((1,3,6,1,4,1,5835,5,2,9100,1,2,1,8),_NtcBwCCfgBandwidthMode_Type())
ntcBwCCfgBandwidthMode.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcBwCCfgBandwidthMode.setStatus(_A)
_NtcBwCMonTable_Object=MibTable
ntcBwCMonTable=_NtcBwCMonTable_Object((1,3,6,1,4,1,5835,5,2,9100,1,3))
if mibBuilder.loadTexts:ntcBwCMonTable.setStatus(_A)
_NtcBwCMonEntry_Object=MibTableRow
ntcBwCMonEntry=_NtcBwCMonEntry_Object((1,3,6,1,4,1,5835,5,2,9100,1,3,1))
if mibBuilder.loadTexts:ntcBwCMonEntry.setStatus(_A)
class _NtcBwCMonState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('off',0),('searching',1),('locked',2)))
_NtcBwCMonState_Type.__name__=_E
_NtcBwCMonState_Object=MibTableColumn
ntcBwCMonState=_NtcBwCMonState_Object((1,3,6,1,4,1,5835,5,2,9100,1,3,1,1),_NtcBwCMonState_Type())
ntcBwCMonState.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcBwCMonState.setStatus(_A)
_NtcBwCMonRoundTripDelay_Type=Float32TC
_NtcBwCMonRoundTripDelay_Object=MibTableColumn
ntcBwCMonRoundTripDelay=_NtcBwCMonRoundTripDelay_Object((1,3,6,1,4,1,5835,5,2,9100,1,3,1,2),_NtcBwCMonRoundTripDelay_Type())
ntcBwCMonRoundTripDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcBwCMonRoundTripDelay.setStatus(_A)
if mibBuilder.loadTexts:ntcBwCMonRoundTripDelay.setUnits('ms')
_NtcBwCMonLocalToTotalPowerRatio_Type=Float32TC
_NtcBwCMonLocalToTotalPowerRatio_Object=MibTableColumn
ntcBwCMonLocalToTotalPowerRatio=_NtcBwCMonLocalToTotalPowerRatio_Object((1,3,6,1,4,1,5835,5,2,9100,1,3,1,3),_NtcBwCMonLocalToTotalPowerRatio_Type())
ntcBwCMonLocalToTotalPowerRatio.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcBwCMonLocalToTotalPowerRatio.setStatus(_A)
if mibBuilder.loadTexts:ntcBwCMonLocalToTotalPowerRatio.setUnits('dB')
_NtcBwCMonLocalToRemotePowerRatio_Type=Float32TC
_NtcBwCMonLocalToRemotePowerRatio_Object=MibTableColumn
ntcBwCMonLocalToRemotePowerRatio=_NtcBwCMonLocalToRemotePowerRatio_Object((1,3,6,1,4,1,5835,5,2,9100,1,3,1,4),_NtcBwCMonLocalToRemotePowerRatio_Type())
ntcBwCMonLocalToRemotePowerRatio.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcBwCMonLocalToRemotePowerRatio.setStatus(_A)
if mibBuilder.loadTexts:ntcBwCMonLocalToRemotePowerRatio.setUnits('dB')
_NtcBwCMonLocalLevel_Type=Float32TC
_NtcBwCMonLocalLevel_Object=MibTableColumn
ntcBwCMonLocalLevel=_NtcBwCMonLocalLevel_Object((1,3,6,1,4,1,5835,5,2,9100,1,3,1,5),_NtcBwCMonLocalLevel_Type())
ntcBwCMonLocalLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcBwCMonLocalLevel.setStatus(_A)
if mibBuilder.loadTexts:ntcBwCMonLocalLevel.setUnits('dBm')
class _NtcBwCMonLocalSymbolRate_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,133000000))
_NtcBwCMonLocalSymbolRate_Type.__name__=_F
_NtcBwCMonLocalSymbolRate_Object=MibTableColumn
ntcBwCMonLocalSymbolRate=_NtcBwCMonLocalSymbolRate_Object((1,3,6,1,4,1,5835,5,2,9100,1,3,1,6),_NtcBwCMonLocalSymbolRate_Type())
ntcBwCMonLocalSymbolRate.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcBwCMonLocalSymbolRate.setStatus(_A)
if mibBuilder.loadTexts:ntcBwCMonLocalSymbolRate.setUnits('baud')
_NtcBwCMonLocalFreqOffset_Type=Float32TC
_NtcBwCMonLocalFreqOffset_Object=MibTableColumn
ntcBwCMonLocalFreqOffset=_NtcBwCMonLocalFreqOffset_Object((1,3,6,1,4,1,5835,5,2,9100,1,3,1,7),_NtcBwCMonLocalFreqOffset_Type())
ntcBwCMonLocalFreqOffset.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcBwCMonLocalFreqOffset.setStatus(_A)
if mibBuilder.loadTexts:ntcBwCMonLocalFreqOffset.setUnits('Hz')
class _NtcBwCMonLocalSpectralInversion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_J,0),(_K,1),('unknown',2)))
_NtcBwCMonLocalSpectralInversion_Type.__name__=_E
_NtcBwCMonLocalSpectralInversion_Object=MibTableColumn
ntcBwCMonLocalSpectralInversion=_NtcBwCMonLocalSpectralInversion_Object((1,3,6,1,4,1,5835,5,2,9100,1,3,1,8),_NtcBwCMonLocalSpectralInversion_Type())
ntcBwCMonLocalSpectralInversion.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcBwCMonLocalSpectralInversion.setStatus(_A)
_NtcBwCAlarmStateTable_Object=MibTable
ntcBwCAlarmStateTable=_NtcBwCAlarmStateTable_Object((1,3,6,1,4,1,5835,5,2,9100,1,4))
if mibBuilder.loadTexts:ntcBwCAlarmStateTable.setStatus(_A)
_NtcBwCAlarmStateEntry_Object=MibTableRow
ntcBwCAlarmStateEntry=_NtcBwCAlarmStateEntry_Object((1,3,6,1,4,1,5835,5,2,9100,1,4,1))
if mibBuilder.loadTexts:ntcBwCAlarmStateEntry.setStatus(_A)
_NtcBwCASNoLock_Type=NtcAlarmState
_NtcBwCASNoLock_Object=MibTableColumn
ntcBwCASNoLock=_NtcBwCASNoLock_Object((1,3,6,1,4,1,5835,5,2,9100,1,4,1,1),_NtcBwCASNoLock_Type())
ntcBwCASNoLock.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcBwCASNoLock.setStatus(_A)
_NtcBwCConformance_ObjectIdentity=ObjectIdentity
ntcBwCConformance=_NtcBwCConformance_ObjectIdentity((1,3,6,1,4,1,5835,5,2,9100,2))
if mibBuilder.loadTexts:ntcBwCConformance.setStatus(_A)
_NtcBwCConfCompliance_ObjectIdentity=ObjectIdentity
ntcBwCConfCompliance=_NtcBwCConfCompliance_ObjectIdentity((1,3,6,1,4,1,5835,5,2,9100,2,1))
if mibBuilder.loadTexts:ntcBwCConfCompliance.setStatus(_A)
_NtcBwCConfGroup_ObjectIdentity=ObjectIdentity
ntcBwCConfGroup=_NtcBwCConfGroup_ObjectIdentity((1,3,6,1,4,1,5835,5,2,9100,2,2))
if mibBuilder.loadTexts:ntcBwCConfGroup.setStatus(_A)
ntcBwCCfgEntry.registerAugmentions((_B,_L))
ntcBwCMonEntry.setIndexNames(*ntcBwCCfgEntry.getIndexNames())
ntcBwCCfgEntry.registerAugmentions((_B,_M))
ntcBwCAlarmStateEntry.setIndexNames(*ntcBwCCfgEntry.getIndexNames())
ntcBwCConfGrpV1Standard=ObjectGroup((1,3,6,1,4,1,5835,5,2,9100,2,2,1))
ntcBwCConfGrpV1Standard.setObjects(*((_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d)))
if mibBuilder.loadTexts:ntcBwCConfGrpV1Standard.setStatus(_A)
ntcBwCConfCompV1Standard=ModuleCompliance((1,3,6,1,4,1,5835,5,2,9100,2,1,1))
ntcBwCConfCompV1Standard.setObjects((_B,_e))
if mibBuilder.loadTexts:ntcBwCConfCompV1Standard.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ntcBandwidthCancellation':ntcBandwidthCancellation,'ntcBwCObjects':ntcBwCObjects,'ntcBwCAlarm':ntcBwCAlarm,_N:ntcBwCAlarmNoLock,'ntcBwCCfgTable':ntcBwCCfgTable,'ntcBwCCfgEntry':ntcBwCCfgEntry,_I:ntcBwCCfgName,_O:ntcBwCCfgEnable,_P:ntcBwCCfgExpRoundTripDelay,_Q:ntcBwCCfgRoundTripDelayUncert,_R:ntcBwCCfgLocalCenterFreqOffset,_S:ntcBwCCfgLocalCenterFreqUncert,_T:ntcBwCCfgLocalSpectralInversion,_U:ntcBwCCfgBandwidthMode,'ntcBwCMonTable':ntcBwCMonTable,_L:ntcBwCMonEntry,_V:ntcBwCMonState,_W:ntcBwCMonRoundTripDelay,_X:ntcBwCMonLocalToTotalPowerRatio,_Y:ntcBwCMonLocalToRemotePowerRatio,_Z:ntcBwCMonLocalLevel,_a:ntcBwCMonLocalSymbolRate,_b:ntcBwCMonLocalFreqOffset,_c:ntcBwCMonLocalSpectralInversion,'ntcBwCAlarmStateTable':ntcBwCAlarmStateTable,_M:ntcBwCAlarmStateEntry,_d:ntcBwCASNoLock,'ntcBwCConformance':ntcBwCConformance,'ntcBwCConfCompliance':ntcBwCConfCompliance,'ntcBwCConfCompV1Standard':ntcBwCConfCompV1Standard,'ntcBwCConfGroup':ntcBwCConfGroup,_e:ntcBwCConfGrpV1Standard})