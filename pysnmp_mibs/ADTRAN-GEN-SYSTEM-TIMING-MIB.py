_U='adGenSystemTimingCurrentSource'
_T='deprecated'
_S='disabled'
_R='enabled'
_Q='adGenSystemTimingExternalSourceId'
_P='adGenSystemTimingSource'
_O='externalSecondary'
_N='externalPrimary'
_M='internal'
_L='ifIndex'
_K='IF-MIB'
_J='ADTRAN-GEN-SYSTEM-TIMING-MIB'
_I='TruthValue'
_H='sysName'
_G='SNMPv2-MIB'
_F='adTrapInformSeqNum'
_E='ADTRAN-GENTRAPINFORM-MIB'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
adTrapInformSeqNum,=mibBuilder.importSymbols(_E,_F)
adGenSystemTiming,adGenSystemTimingID=mibBuilder.importSymbols('ADTRAN-SHARED-CND-SYSTEM-MIB','adGenSystemTiming','adGenSystemTimingID')
GenSystemInterfaceType,=mibBuilder.importSymbols('ADTRAN-SHARED-CND-SYSTEM-TC-MIB','GenSystemInterfaceType')
ifIndex,=mibBuilder.importSymbols(_K,_L)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
sysName,=mibBuilder.importSymbols(_G,_H)
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_I)
adGenSystemTimingMIB=ModuleIdentity((1,3,6,1,4,1,664,6,10000,70,13,1))
if mibBuilder.loadTexts:adGenSystemTimingMIB.setRevisions(('2018-01-09 00:00','2017-09-29 00:00','2017-07-25 00:00','2017-06-12 00:00','2013-09-09 00:00','2011-10-26 11:00','2011-09-02 00:00','2009-03-02 00:00'))
class AdGenTimingSource(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('primaryTimingSource',1),('secondaryTimingSource',2),('fallbackTimingSource',3)))
class AdGenTimingSourceSelection(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*((_M,1),(_N,2),(_O,3),('loopA',4),('loopB',5),('localPort',6),('fixedPort',7),('localPortSyncE',8),('fixedPortSyncE',9),('localPortPhy',10),('fixedPortPhy',11),('vdslUplinkNTR',12)))
class AdGenExternalSource(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_O,2)))
class AdGenTimingConfigurationStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('invalidConfiguration',1),('incompleteConfiguration',2),('okConfiguration',3)))
class AdGenExternalSourceType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('bitsD4',1),('bitsOD',2),('composite',3),('composite8kHz',4),('bitsG704',5),('bitsD5',6)))
class AdGenTimingSourceQuality(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,15)));namedValues=NamedValues(*(('stratum1',1),('synchronized',2),('stratum2',3),('transmitModeClock',4),('stratum3e',5),('stratum3',6),('sonetClock',7),('stratum4or4e',8),('doNotUseForSync',15)))
class AdGenSystemTimingSourceHealth(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_AdGenSystemTimingProv_ObjectIdentity=ObjectIdentity
adGenSystemTimingProv=_AdGenSystemTimingProv_ObjectIdentity((1,3,6,1,4,1,664,5,70,13,1))
_AdGenSystemTimingProvTable_Object=MibTable
adGenSystemTimingProvTable=_AdGenSystemTimingProvTable_Object((1,3,6,1,4,1,664,5,70,13,1,1))
if mibBuilder.loadTexts:adGenSystemTimingProvTable.setStatus(_A)
_AdGenSystemTimingProvEntry_Object=MibTableRow
adGenSystemTimingProvEntry=_AdGenSystemTimingProvEntry_Object((1,3,6,1,4,1,664,5,70,13,1,1,1))
adGenSystemTimingProvEntry.setIndexNames((0,_J,_P))
if mibBuilder.loadTexts:adGenSystemTimingProvEntry.setStatus(_A)
_AdGenSystemTimingSource_Type=AdGenTimingSource
_AdGenSystemTimingSource_Object=MibTableColumn
adGenSystemTimingSource=_AdGenSystemTimingSource_Object((1,3,6,1,4,1,664,5,70,13,1,1,1,1),_AdGenSystemTimingSource_Type())
adGenSystemTimingSource.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenSystemTimingSource.setStatus(_A)
_AdGenSystemTimingSelection_Type=AdGenTimingSourceSelection
_AdGenSystemTimingSelection_Object=MibTableColumn
adGenSystemTimingSelection=_AdGenSystemTimingSelection_Object((1,3,6,1,4,1,664,5,70,13,1,1,1,2),_AdGenSystemTimingSelection_Type())
adGenSystemTimingSelection.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenSystemTimingSelection.setStatus(_A)
_AdGenSystemTimingInterfaceType_Type=GenSystemInterfaceType
_AdGenSystemTimingInterfaceType_Object=MibTableColumn
adGenSystemTimingInterfaceType=_AdGenSystemTimingInterfaceType_Object((1,3,6,1,4,1,664,5,70,13,1,1,1,3),_AdGenSystemTimingInterfaceType_Type())
adGenSystemTimingInterfaceType.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenSystemTimingInterfaceType.setStatus(_A)
_AdGenSystemTimingShelf_Type=Integer32
_AdGenSystemTimingShelf_Object=MibTableColumn
adGenSystemTimingShelf=_AdGenSystemTimingShelf_Object((1,3,6,1,4,1,664,5,70,13,1,1,1,4),_AdGenSystemTimingShelf_Type())
adGenSystemTimingShelf.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenSystemTimingShelf.setStatus(_A)
_AdGenSystemTimingSlot_Type=Integer32
_AdGenSystemTimingSlot_Object=MibTableColumn
adGenSystemTimingSlot=_AdGenSystemTimingSlot_Object((1,3,6,1,4,1,664,5,70,13,1,1,1,5),_AdGenSystemTimingSlot_Type())
adGenSystemTimingSlot.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenSystemTimingSlot.setStatus(_A)
_AdGenSystemTimingPort_Type=Integer32
_AdGenSystemTimingPort_Object=MibTableColumn
adGenSystemTimingPort=_AdGenSystemTimingPort_Object((1,3,6,1,4,1,664,5,70,13,1,1,1,6),_AdGenSystemTimingPort_Type())
adGenSystemTimingPort.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenSystemTimingPort.setStatus(_A)
_AdGenSystemTimingConfigurationStatus_Type=AdGenTimingConfigurationStatus
_AdGenSystemTimingConfigurationStatus_Object=MibTableColumn
adGenSystemTimingConfigurationStatus=_AdGenSystemTimingConfigurationStatus_Object((1,3,6,1,4,1,664,5,70,13,1,1,1,7),_AdGenSystemTimingConfigurationStatus_Type())
adGenSystemTimingConfigurationStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenSystemTimingConfigurationStatus.setStatus(_A)
_AdGenSystemTimingExternalSourceProvTable_Object=MibTable
adGenSystemTimingExternalSourceProvTable=_AdGenSystemTimingExternalSourceProvTable_Object((1,3,6,1,4,1,664,5,70,13,1,2))
if mibBuilder.loadTexts:adGenSystemTimingExternalSourceProvTable.setStatus(_A)
_AdGenSystemTimingExternalSourceProvEntry_Object=MibTableRow
adGenSystemTimingExternalSourceProvEntry=_AdGenSystemTimingExternalSourceProvEntry_Object((1,3,6,1,4,1,664,5,70,13,1,2,1))
adGenSystemTimingExternalSourceProvEntry.setIndexNames((0,_J,_Q))
if mibBuilder.loadTexts:adGenSystemTimingExternalSourceProvEntry.setStatus(_A)
_AdGenSystemTimingExternalSourceId_Type=AdGenExternalSource
_AdGenSystemTimingExternalSourceId_Object=MibTableColumn
adGenSystemTimingExternalSourceId=_AdGenSystemTimingExternalSourceId_Object((1,3,6,1,4,1,664,5,70,13,1,2,1,1),_AdGenSystemTimingExternalSourceId_Type())
adGenSystemTimingExternalSourceId.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenSystemTimingExternalSourceId.setStatus(_A)
_AdGenSystemTimingExternalSourceType_Type=AdGenExternalSourceType
_AdGenSystemTimingExternalSourceType_Object=MibTableColumn
adGenSystemTimingExternalSourceType=_AdGenSystemTimingExternalSourceType_Object((1,3,6,1,4,1,664,5,70,13,1,2,1,2),_AdGenSystemTimingExternalSourceType_Type())
adGenSystemTimingExternalSourceType.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenSystemTimingExternalSourceType.setStatus(_A)
_AdGenSystemTimingExternalSourceQuality_Type=AdGenTimingSourceQuality
_AdGenSystemTimingExternalSourceQuality_Object=MibTableColumn
adGenSystemTimingExternalSourceQuality=_AdGenSystemTimingExternalSourceQuality_Object((1,3,6,1,4,1,664,5,70,13,1,2,1,3),_AdGenSystemTimingExternalSourceQuality_Type())
adGenSystemTimingExternalSourceQuality.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenSystemTimingExternalSourceQuality.setStatus(_A)
class _AdGenSystemTimingExternalSourcePriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AdGenSystemTimingExternalSourcePriority_Type.__name__=_C
_AdGenSystemTimingExternalSourcePriority_Object=MibTableColumn
adGenSystemTimingExternalSourcePriority=_AdGenSystemTimingExternalSourcePriority_Object((1,3,6,1,4,1,664,5,70,13,1,2,1,4),_AdGenSystemTimingExternalSourcePriority_Type())
adGenSystemTimingExternalSourcePriority.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenSystemTimingExternalSourcePriority.setStatus(_A)
class _AdGenSystemTimingExternalSourceHopCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AdGenSystemTimingExternalSourceHopCount_Type.__name__=_C
_AdGenSystemTimingExternalSourceHopCount_Object=MibTableColumn
adGenSystemTimingExternalSourceHopCount=_AdGenSystemTimingExternalSourceHopCount_Object((1,3,6,1,4,1,664,5,70,13,1,2,1,5),_AdGenSystemTimingExternalSourceHopCount_Type())
adGenSystemTimingExternalSourceHopCount.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenSystemTimingExternalSourceHopCount.setStatus(_A)
class _AdGenSystemTimingModeRevertive_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_R,1),(_S,2)))
_AdGenSystemTimingModeRevertive_Type.__name__=_C
_AdGenSystemTimingModeRevertive_Object=MibScalar
adGenSystemTimingModeRevertive=_AdGenSystemTimingModeRevertive_Object((1,3,6,1,4,1,664,5,70,13,1,3),_AdGenSystemTimingModeRevertive_Type())
adGenSystemTimingModeRevertive.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenSystemTimingModeRevertive.setStatus(_T)
class _AdGenSystemTimingForceClockFailover_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('failover',1),('notavailable',2)))
_AdGenSystemTimingForceClockFailover_Type.__name__=_C
_AdGenSystemTimingForceClockFailover_Object=MibScalar
adGenSystemTimingForceClockFailover=_AdGenSystemTimingForceClockFailover_Object((1,3,6,1,4,1,664,5,70,13,1,4),_AdGenSystemTimingForceClockFailover_Type())
adGenSystemTimingForceClockFailover.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenSystemTimingForceClockFailover.setStatus(_A)
class _AdGenSystemTimingUseHopCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_R,1),(_S,2)))
_AdGenSystemTimingUseHopCount_Type.__name__=_C
_AdGenSystemTimingUseHopCount_Object=MibScalar
adGenSystemTimingUseHopCount=_AdGenSystemTimingUseHopCount_Object((1,3,6,1,4,1,664,5,70,13,1,5),_AdGenSystemTimingUseHopCount_Type())
adGenSystemTimingUseHopCount.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenSystemTimingUseHopCount.setStatus(_T)
class _AdGenSystemTimingSrcSwitchAlarmEnable_Type(TruthValue):defaultValue=1
_AdGenSystemTimingSrcSwitchAlarmEnable_Type.__name__=_I
_AdGenSystemTimingSrcSwitchAlarmEnable_Object=MibScalar
adGenSystemTimingSrcSwitchAlarmEnable=_AdGenSystemTimingSrcSwitchAlarmEnable_Object((1,3,6,1,4,1,664,5,70,13,1,6),_AdGenSystemTimingSrcSwitchAlarmEnable_Type())
adGenSystemTimingSrcSwitchAlarmEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenSystemTimingSrcSwitchAlarmEnable.setStatus(_A)
class _AdGenSystemTimingPriSrcFailAlarmEnable_Type(TruthValue):defaultValue=1
_AdGenSystemTimingPriSrcFailAlarmEnable_Type.__name__=_I
_AdGenSystemTimingPriSrcFailAlarmEnable_Object=MibScalar
adGenSystemTimingPriSrcFailAlarmEnable=_AdGenSystemTimingPriSrcFailAlarmEnable_Object((1,3,6,1,4,1,664,5,70,13,1,7),_AdGenSystemTimingPriSrcFailAlarmEnable_Type())
adGenSystemTimingPriSrcFailAlarmEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenSystemTimingPriSrcFailAlarmEnable.setStatus(_A)
class _AdGenSystemTimingSecSrcFailAlarmEnable_Type(TruthValue):defaultValue=1
_AdGenSystemTimingSecSrcFailAlarmEnable_Type.__name__=_I
_AdGenSystemTimingSecSrcFailAlarmEnable_Object=MibScalar
adGenSystemTimingSecSrcFailAlarmEnable=_AdGenSystemTimingSecSrcFailAlarmEnable_Object((1,3,6,1,4,1,664,5,70,13,1,8),_AdGenSystemTimingSecSrcFailAlarmEnable_Type())
adGenSystemTimingSecSrcFailAlarmEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenSystemTimingSecSrcFailAlarmEnable.setStatus(_A)
class _AdGenSystemTimingSelectionMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('revertive',1),('nonRevertive',2),('useHopCount',3)))
_AdGenSystemTimingSelectionMode_Type.__name__=_C
_AdGenSystemTimingSelectionMode_Object=MibScalar
adGenSystemTimingSelectionMode=_AdGenSystemTimingSelectionMode_Object((1,3,6,1,4,1,664,5,70,13,1,9),_AdGenSystemTimingSelectionMode_Type())
adGenSystemTimingSelectionMode.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenSystemTimingSelectionMode.setStatus(_A)
_AdGenSystemTimingProvPortTable_Object=MibTable
adGenSystemTimingProvPortTable=_AdGenSystemTimingProvPortTable_Object((1,3,6,1,4,1,664,5,70,13,1,10))
if mibBuilder.loadTexts:adGenSystemTimingProvPortTable.setStatus(_A)
_AdGenSystemTimingProvPortEntry_Object=MibTableRow
adGenSystemTimingProvPortEntry=_AdGenSystemTimingProvPortEntry_Object((1,3,6,1,4,1,664,5,70,13,1,10,1))
adGenSystemTimingProvPortEntry.setIndexNames((0,_K,_L))
if mibBuilder.loadTexts:adGenSystemTimingProvPortEntry.setStatus(_A)
class _AdGenSystemTimingTransmitSSMEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_AdGenSystemTimingTransmitSSMEnable_Type.__name__=_C
_AdGenSystemTimingTransmitSSMEnable_Object=MibTableColumn
adGenSystemTimingTransmitSSMEnable=_AdGenSystemTimingTransmitSSMEnable_Object((1,3,6,1,4,1,664,5,70,13,1,10,1,1),_AdGenSystemTimingTransmitSSMEnable_Type())
adGenSystemTimingTransmitSSMEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenSystemTimingTransmitSSMEnable.setStatus(_A)
_AdGenSystemTimingStatus_ObjectIdentity=ObjectIdentity
adGenSystemTimingStatus=_AdGenSystemTimingStatus_ObjectIdentity((1,3,6,1,4,1,664,5,70,13,2))
class _AdGenSystemTimingCurrentSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('primary',1),('secondary',2),('fallback',3),('standby',4),(_M,5),('holdover',6)))
_AdGenSystemTimingCurrentSource_Type.__name__=_C
_AdGenSystemTimingCurrentSource_Object=MibScalar
adGenSystemTimingCurrentSource=_AdGenSystemTimingCurrentSource_Object((1,3,6,1,4,1,664,5,70,13,2,1),_AdGenSystemTimingCurrentSource_Type())
adGenSystemTimingCurrentSource.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenSystemTimingCurrentSource.setStatus(_A)
_AdGenSystemTimingLoopAClockHealth_Type=AdGenSystemTimingSourceHealth
_AdGenSystemTimingLoopAClockHealth_Object=MibScalar
adGenSystemTimingLoopAClockHealth=_AdGenSystemTimingLoopAClockHealth_Object((1,3,6,1,4,1,664,5,70,13,2,2),_AdGenSystemTimingLoopAClockHealth_Type())
adGenSystemTimingLoopAClockHealth.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenSystemTimingLoopAClockHealth.setStatus(_A)
_AdGenSystemTimingLoopBClockHealth_Type=AdGenSystemTimingSourceHealth
_AdGenSystemTimingLoopBClockHealth_Object=MibScalar
adGenSystemTimingLoopBClockHealth=_AdGenSystemTimingLoopBClockHealth_Object((1,3,6,1,4,1,664,5,70,13,2,3),_AdGenSystemTimingLoopBClockHealth_Type())
adGenSystemTimingLoopBClockHealth.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenSystemTimingLoopBClockHealth.setStatus(_A)
_AdGenSystemTimingBitsAClockHealth_Type=AdGenSystemTimingSourceHealth
_AdGenSystemTimingBitsAClockHealth_Object=MibScalar
adGenSystemTimingBitsAClockHealth=_AdGenSystemTimingBitsAClockHealth_Object((1,3,6,1,4,1,664,5,70,13,2,4),_AdGenSystemTimingBitsAClockHealth_Type())
adGenSystemTimingBitsAClockHealth.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenSystemTimingBitsAClockHealth.setStatus(_A)
_AdGenSystemTimingBitsBClockHealth_Type=AdGenSystemTimingSourceHealth
_AdGenSystemTimingBitsBClockHealth_Object=MibScalar
adGenSystemTimingBitsBClockHealth=_AdGenSystemTimingBitsBClockHealth_Object((1,3,6,1,4,1,664,5,70,13,2,5),_AdGenSystemTimingBitsBClockHealth_Type())
adGenSystemTimingBitsBClockHealth.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenSystemTimingBitsBClockHealth.setStatus(_A)
_AdGenSystemTimingPrimaryClockHealth_Type=AdGenSystemTimingSourceHealth
_AdGenSystemTimingPrimaryClockHealth_Object=MibScalar
adGenSystemTimingPrimaryClockHealth=_AdGenSystemTimingPrimaryClockHealth_Object((1,3,6,1,4,1,664,5,70,13,2,6),_AdGenSystemTimingPrimaryClockHealth_Type())
adGenSystemTimingPrimaryClockHealth.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenSystemTimingPrimaryClockHealth.setStatus(_A)
_AdGenSystemTimingSecondaryClockHealth_Type=AdGenSystemTimingSourceHealth
_AdGenSystemTimingSecondaryClockHealth_Object=MibScalar
adGenSystemTimingSecondaryClockHealth=_AdGenSystemTimingSecondaryClockHealth_Object((1,3,6,1,4,1,664,5,70,13,2,7),_AdGenSystemTimingSecondaryClockHealth_Type())
adGenSystemTimingSecondaryClockHealth.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenSystemTimingSecondaryClockHealth.setStatus(_A)
class _AdGenSystemTimingCurrentHopCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_AdGenSystemTimingCurrentHopCount_Type.__name__=_C
_AdGenSystemTimingCurrentHopCount_Object=MibScalar
adGenSystemTimingCurrentHopCount=_AdGenSystemTimingCurrentHopCount_Object((1,3,6,1,4,1,664,5,70,13,2,8),_AdGenSystemTimingCurrentHopCount_Type())
adGenSystemTimingCurrentHopCount.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenSystemTimingCurrentHopCount.setStatus(_A)
class _AdGenSystemTimingCurrentTimingSourcePriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AdGenSystemTimingCurrentTimingSourcePriority_Type.__name__=_C
_AdGenSystemTimingCurrentTimingSourcePriority_Object=MibScalar
adGenSystemTimingCurrentTimingSourcePriority=_AdGenSystemTimingCurrentTimingSourcePriority_Object((1,3,6,1,4,1,664,5,70,13,2,9),_AdGenSystemTimingCurrentTimingSourcePriority_Type())
adGenSystemTimingCurrentTimingSourcePriority.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenSystemTimingCurrentTimingSourcePriority.setStatus(_A)
_AdGenSystemTimingCurrentTimingSourceQuality_Type=AdGenTimingSourceQuality
_AdGenSystemTimingCurrentTimingSourceQuality_Object=MibScalar
adGenSystemTimingCurrentTimingSourceQuality=_AdGenSystemTimingCurrentTimingSourceQuality_Object((1,3,6,1,4,1,664,5,70,13,2,10),_AdGenSystemTimingCurrentTimingSourceQuality_Type())
adGenSystemTimingCurrentTimingSourceQuality.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenSystemTimingCurrentTimingSourceQuality.setStatus(_A)
class _AdGenSystemTimingPrimaryHopCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_AdGenSystemTimingPrimaryHopCount_Type.__name__=_C
_AdGenSystemTimingPrimaryHopCount_Object=MibScalar
adGenSystemTimingPrimaryHopCount=_AdGenSystemTimingPrimaryHopCount_Object((1,3,6,1,4,1,664,5,70,13,2,11),_AdGenSystemTimingPrimaryHopCount_Type())
adGenSystemTimingPrimaryHopCount.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenSystemTimingPrimaryHopCount.setStatus(_A)
class _AdGenSystemTimingPrimaryTimingSourcePriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AdGenSystemTimingPrimaryTimingSourcePriority_Type.__name__=_C
_AdGenSystemTimingPrimaryTimingSourcePriority_Object=MibScalar
adGenSystemTimingPrimaryTimingSourcePriority=_AdGenSystemTimingPrimaryTimingSourcePriority_Object((1,3,6,1,4,1,664,5,70,13,2,12),_AdGenSystemTimingPrimaryTimingSourcePriority_Type())
adGenSystemTimingPrimaryTimingSourcePriority.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenSystemTimingPrimaryTimingSourcePriority.setStatus(_A)
_AdGenSystemTimingPrimaryTimingSourceQuality_Type=AdGenTimingSourceQuality
_AdGenSystemTimingPrimaryTimingSourceQuality_Object=MibScalar
adGenSystemTimingPrimaryTimingSourceQuality=_AdGenSystemTimingPrimaryTimingSourceQuality_Object((1,3,6,1,4,1,664,5,70,13,2,13),_AdGenSystemTimingPrimaryTimingSourceQuality_Type())
adGenSystemTimingPrimaryTimingSourceQuality.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenSystemTimingPrimaryTimingSourceQuality.setStatus(_A)
class _AdGenSystemTimingSecondaryHopCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_AdGenSystemTimingSecondaryHopCount_Type.__name__=_C
_AdGenSystemTimingSecondaryHopCount_Object=MibScalar
adGenSystemTimingSecondaryHopCount=_AdGenSystemTimingSecondaryHopCount_Object((1,3,6,1,4,1,664,5,70,13,2,14),_AdGenSystemTimingSecondaryHopCount_Type())
adGenSystemTimingSecondaryHopCount.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenSystemTimingSecondaryHopCount.setStatus(_A)
class _AdGenSystemTimingSecondaryTimingSourcePriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AdGenSystemTimingSecondaryTimingSourcePriority_Type.__name__=_C
_AdGenSystemTimingSecondaryTimingSourcePriority_Object=MibScalar
adGenSystemTimingSecondaryTimingSourcePriority=_AdGenSystemTimingSecondaryTimingSourcePriority_Object((1,3,6,1,4,1,664,5,70,13,2,15),_AdGenSystemTimingSecondaryTimingSourcePriority_Type())
adGenSystemTimingSecondaryTimingSourcePriority.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenSystemTimingSecondaryTimingSourcePriority.setStatus(_A)
_AdGenSystemTimingSecondaryTimingSourceQuality_Type=AdGenTimingSourceQuality
_AdGenSystemTimingSecondaryTimingSourceQuality_Object=MibScalar
adGenSystemTimingSecondaryTimingSourceQuality=_AdGenSystemTimingSecondaryTimingSourceQuality_Object((1,3,6,1,4,1,664,5,70,13,2,16),_AdGenSystemTimingSecondaryTimingSourceQuality_Type())
adGenSystemTimingSecondaryTimingSourceQuality.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenSystemTimingSecondaryTimingSourceQuality.setStatus(_A)
class _AdGenSystemTimingFallbackHopCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_AdGenSystemTimingFallbackHopCount_Type.__name__=_C
_AdGenSystemTimingFallbackHopCount_Object=MibScalar
adGenSystemTimingFallbackHopCount=_AdGenSystemTimingFallbackHopCount_Object((1,3,6,1,4,1,664,5,70,13,2,17),_AdGenSystemTimingFallbackHopCount_Type())
adGenSystemTimingFallbackHopCount.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenSystemTimingFallbackHopCount.setStatus(_A)
class _AdGenSystemTimingFallbackTimingSourcePriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AdGenSystemTimingFallbackTimingSourcePriority_Type.__name__=_C
_AdGenSystemTimingFallbackTimingSourcePriority_Object=MibScalar
adGenSystemTimingFallbackTimingSourcePriority=_AdGenSystemTimingFallbackTimingSourcePriority_Object((1,3,6,1,4,1,664,5,70,13,2,18),_AdGenSystemTimingFallbackTimingSourcePriority_Type())
adGenSystemTimingFallbackTimingSourcePriority.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenSystemTimingFallbackTimingSourcePriority.setStatus(_A)
_AdGenSystemTimingFallbackTimingSourceQuality_Type=AdGenTimingSourceQuality
_AdGenSystemTimingFallbackTimingSourceQuality_Object=MibScalar
adGenSystemTimingFallbackTimingSourceQuality=_AdGenSystemTimingFallbackTimingSourceQuality_Object((1,3,6,1,4,1,664,5,70,13,2,19),_AdGenSystemTimingFallbackTimingSourceQuality_Type())
adGenSystemTimingFallbackTimingSourceQuality.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenSystemTimingFallbackTimingSourceQuality.setStatus(_A)
_AdGenSystemTimingAlarmPrefix_ObjectIdentity=ObjectIdentity
adGenSystemTimingAlarmPrefix=_AdGenSystemTimingAlarmPrefix_ObjectIdentity((1,3,6,1,4,1,664,5,70,13,3))
_AdGenSystemTimingAlarms_ObjectIdentity=ObjectIdentity
adGenSystemTimingAlarms=_AdGenSystemTimingAlarms_ObjectIdentity((1,3,6,1,4,1,664,5,70,13,3,0))
adGenSystemTimingSrcSwitch=NotificationType((1,3,6,1,4,1,664,5,70,13,3,0,1))
adGenSystemTimingSrcSwitch.setObjects(*((_E,_F),(_G,_H),(_J,_U)))
if mibBuilder.loadTexts:adGenSystemTimingSrcSwitch.setStatus(_A)
adGenSystemTimingPriSrcClear=NotificationType((1,3,6,1,4,1,664,5,70,13,3,0,2))
adGenSystemTimingPriSrcClear.setObjects(*((_E,_F),(_G,_H)))
if mibBuilder.loadTexts:adGenSystemTimingPriSrcClear.setStatus(_A)
adGenSystemTimingPriSrcFail=NotificationType((1,3,6,1,4,1,664,5,70,13,3,0,3))
adGenSystemTimingPriSrcFail.setObjects(*((_E,_F),(_G,_H)))
if mibBuilder.loadTexts:adGenSystemTimingPriSrcFail.setStatus(_A)
adGenSystemTimingSecSrcClear=NotificationType((1,3,6,1,4,1,664,5,70,13,3,0,4))
adGenSystemTimingSecSrcClear.setObjects(*((_E,_F),(_G,_H)))
if mibBuilder.loadTexts:adGenSystemTimingSecSrcClear.setStatus(_A)
adGenSystemTimingSecSrcFail=NotificationType((1,3,6,1,4,1,664,5,70,13,3,0,5))
adGenSystemTimingSecSrcFail.setObjects(*((_E,_F),(_G,_H)))
if mibBuilder.loadTexts:adGenSystemTimingSecSrcFail.setStatus(_A)
mibBuilder.exportSymbols(_J,**{'AdGenTimingSource':AdGenTimingSource,'AdGenTimingSourceSelection':AdGenTimingSourceSelection,'AdGenExternalSource':AdGenExternalSource,'AdGenTimingConfigurationStatus':AdGenTimingConfigurationStatus,'AdGenExternalSourceType':AdGenExternalSourceType,'AdGenTimingSourceQuality':AdGenTimingSourceQuality,'AdGenSystemTimingSourceHealth':AdGenSystemTimingSourceHealth,'adGenSystemTimingProv':adGenSystemTimingProv,'adGenSystemTimingProvTable':adGenSystemTimingProvTable,'adGenSystemTimingProvEntry':adGenSystemTimingProvEntry,_P:adGenSystemTimingSource,'adGenSystemTimingSelection':adGenSystemTimingSelection,'adGenSystemTimingInterfaceType':adGenSystemTimingInterfaceType,'adGenSystemTimingShelf':adGenSystemTimingShelf,'adGenSystemTimingSlot':adGenSystemTimingSlot,'adGenSystemTimingPort':adGenSystemTimingPort,'adGenSystemTimingConfigurationStatus':adGenSystemTimingConfigurationStatus,'adGenSystemTimingExternalSourceProvTable':adGenSystemTimingExternalSourceProvTable,'adGenSystemTimingExternalSourceProvEntry':adGenSystemTimingExternalSourceProvEntry,_Q:adGenSystemTimingExternalSourceId,'adGenSystemTimingExternalSourceType':adGenSystemTimingExternalSourceType,'adGenSystemTimingExternalSourceQuality':adGenSystemTimingExternalSourceQuality,'adGenSystemTimingExternalSourcePriority':adGenSystemTimingExternalSourcePriority,'adGenSystemTimingExternalSourceHopCount':adGenSystemTimingExternalSourceHopCount,'adGenSystemTimingModeRevertive':adGenSystemTimingModeRevertive,'adGenSystemTimingForceClockFailover':adGenSystemTimingForceClockFailover,'adGenSystemTimingUseHopCount':adGenSystemTimingUseHopCount,'adGenSystemTimingSrcSwitchAlarmEnable':adGenSystemTimingSrcSwitchAlarmEnable,'adGenSystemTimingPriSrcFailAlarmEnable':adGenSystemTimingPriSrcFailAlarmEnable,'adGenSystemTimingSecSrcFailAlarmEnable':adGenSystemTimingSecSrcFailAlarmEnable,'adGenSystemTimingSelectionMode':adGenSystemTimingSelectionMode,'adGenSystemTimingProvPortTable':adGenSystemTimingProvPortTable,'adGenSystemTimingProvPortEntry':adGenSystemTimingProvPortEntry,'adGenSystemTimingTransmitSSMEnable':adGenSystemTimingTransmitSSMEnable,'adGenSystemTimingStatus':adGenSystemTimingStatus,_U:adGenSystemTimingCurrentSource,'adGenSystemTimingLoopAClockHealth':adGenSystemTimingLoopAClockHealth,'adGenSystemTimingLoopBClockHealth':adGenSystemTimingLoopBClockHealth,'adGenSystemTimingBitsAClockHealth':adGenSystemTimingBitsAClockHealth,'adGenSystemTimingBitsBClockHealth':adGenSystemTimingBitsBClockHealth,'adGenSystemTimingPrimaryClockHealth':adGenSystemTimingPrimaryClockHealth,'adGenSystemTimingSecondaryClockHealth':adGenSystemTimingSecondaryClockHealth,'adGenSystemTimingCurrentHopCount':adGenSystemTimingCurrentHopCount,'adGenSystemTimingCurrentTimingSourcePriority':adGenSystemTimingCurrentTimingSourcePriority,'adGenSystemTimingCurrentTimingSourceQuality':adGenSystemTimingCurrentTimingSourceQuality,'adGenSystemTimingPrimaryHopCount':adGenSystemTimingPrimaryHopCount,'adGenSystemTimingPrimaryTimingSourcePriority':adGenSystemTimingPrimaryTimingSourcePriority,'adGenSystemTimingPrimaryTimingSourceQuality':adGenSystemTimingPrimaryTimingSourceQuality,'adGenSystemTimingSecondaryHopCount':adGenSystemTimingSecondaryHopCount,'adGenSystemTimingSecondaryTimingSourcePriority':adGenSystemTimingSecondaryTimingSourcePriority,'adGenSystemTimingSecondaryTimingSourceQuality':adGenSystemTimingSecondaryTimingSourceQuality,'adGenSystemTimingFallbackHopCount':adGenSystemTimingFallbackHopCount,'adGenSystemTimingFallbackTimingSourcePriority':adGenSystemTimingFallbackTimingSourcePriority,'adGenSystemTimingFallbackTimingSourceQuality':adGenSystemTimingFallbackTimingSourceQuality,'adGenSystemTimingAlarmPrefix':adGenSystemTimingAlarmPrefix,'adGenSystemTimingAlarms':adGenSystemTimingAlarms,'adGenSystemTimingSrcSwitch':adGenSystemTimingSrcSwitch,'adGenSystemTimingPriSrcClear':adGenSystemTimingPriSrcClear,'adGenSystemTimingPriSrcFail':adGenSystemTimingPriSrcFail,'adGenSystemTimingSecSrcClear':adGenSystemTimingSecSrcClear,'adGenSystemTimingSecSrcFail':adGenSystemTimingSecSrcFail,'adGenSystemTimingMIB':adGenSystemTimingMIB})