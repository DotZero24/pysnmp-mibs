_L='zyPoeAutoPdRecoveryPortMode'
_K='zyPoeTrapPsePowerSupplyFailedReason'
_J='zyPoePsePortTimeRangeName'
_I='read-only'
_H='ZYXEL-POWER-ETHERNET-MIB'
_G='dot1dBasePort'
_F='BRIDGE-MIB'
_E='ifIndex'
_D='IF-MIB'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dot1dBasePort,=mibBuilder.importSymbols(_F,_G)
ifIndex,=mibBuilder.importSymbols(_D,_E)
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB','EnabledStatus')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
esMgmt,=mibBuilder.importSymbols('ZYXEL-ES-SMI','esMgmt')
zyxelPoe=ModuleIdentity((1,3,6,1,4,1,890,1,15,3,59))
_ZyxelPoeSetup_ObjectIdentity=ObjectIdentity
zyxelPoeSetup=_ZyxelPoeSetup_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,59,1))
class _ZyPoeMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('consumption',0),('classification',1)))
_ZyPoeMode_Type.__name__=_C
_ZyPoeMode_Object=MibScalar
zyPoeMode=_ZyPoeMode_Object((1,3,6,1,4,1,890,1,15,3,59,1,1),_ZyPoeMode_Type())
zyPoeMode.setMaxAccess(_B)
if mibBuilder.loadTexts:zyPoeMode.setStatus(_A)
_ZyxelPoePsePortTable_Object=MibTable
zyxelPoePsePortTable=_ZyxelPoePsePortTable_Object((1,3,6,1,4,1,890,1,15,3,59,1,2))
if mibBuilder.loadTexts:zyxelPoePsePortTable.setStatus(_A)
_ZyxelPoePsePortEntry_Object=MibTableRow
zyxelPoePsePortEntry=_ZyxelPoePsePortEntry_Object((1,3,6,1,4,1,890,1,15,3,59,1,2,1))
zyxelPoePsePortEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:zyxelPoePsePortEntry.setStatus(_A)
_ZyPoePsePortMaxPower_Type=Integer32
_ZyPoePsePortMaxPower_Object=MibTableColumn
zyPoePsePortMaxPower=_ZyPoePsePortMaxPower_Object((1,3,6,1,4,1,890,1,15,3,59,1,2,1,1),_ZyPoePsePortMaxPower_Type())
zyPoePsePortMaxPower.setMaxAccess(_B)
if mibBuilder.loadTexts:zyPoePsePortMaxPower.setStatus(_A)
class _ZyPoePsePowerUp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*(('ieee802dot3af',0),('legacy',1),('preIeee802dot3at',2),('ieee802dot3at',3),('ieee802dot3bt',4),('preIeee802dot3bt',5),('forceIeee802dot3at',6)))
_ZyPoePsePowerUp_Type.__name__=_C
_ZyPoePsePowerUp_Object=MibTableColumn
zyPoePsePowerUp=_ZyPoePsePowerUp_Object((1,3,6,1,4,1,890,1,15,3,59,1,2,1,2),_ZyPoePsePowerUp_Type())
zyPoePsePowerUp.setMaxAccess(_B)
if mibBuilder.loadTexts:zyPoePsePowerUp.setStatus(_A)
_ZyPoePsePortTimeRange_Type=DisplayString
_ZyPoePsePortTimeRange_Object=MibTableColumn
zyPoePsePortTimeRange=_ZyPoePsePortTimeRange_Object((1,3,6,1,4,1,890,1,15,3,59,1,2,1,3),_ZyPoePsePortTimeRange_Type())
zyPoePsePortTimeRange.setMaxAccess(_B)
if mibBuilder.loadTexts:zyPoePsePortTimeRange.setStatus(_A)
_ZyPoePseWideRangeDetection_Type=EnabledStatus
_ZyPoePseWideRangeDetection_Object=MibTableColumn
zyPoePseWideRangeDetection=_ZyPoePseWideRangeDetection_Object((1,3,6,1,4,1,890,1,15,3,59,1,2,1,4),_ZyPoePseWideRangeDetection_Type())
zyPoePseWideRangeDetection.setMaxAccess(_B)
if mibBuilder.loadTexts:zyPoePseWideRangeDetection.setStatus(_A)
_ZyPoePreAllocate_Type=EnabledStatus
_ZyPoePreAllocate_Object=MibScalar
zyPoePreAllocate=_ZyPoePreAllocate_Object((1,3,6,1,4,1,890,1,15,3,59,1,3),_ZyPoePreAllocate_Type())
zyPoePreAllocate.setMaxAccess(_B)
if mibBuilder.loadTexts:zyPoePreAllocate.setStatus(_A)
_ZyPoeDualDetection_Type=EnabledStatus
_ZyPoeDualDetection_Object=MibScalar
zyPoeDualDetection=_ZyPoeDualDetection_Object((1,3,6,1,4,1,890,1,15,3,59,1,4),_ZyPoeDualDetection_Type())
zyPoeDualDetection.setMaxAccess(_B)
if mibBuilder.loadTexts:zyPoeDualDetection.setStatus(_A)
_ZyPoePowerSequenceDelay_Type=EnabledStatus
_ZyPoePowerSequenceDelay_Object=MibScalar
zyPoePowerSequenceDelay=_ZyPoePowerSequenceDelay_Object((1,3,6,1,4,1,890,1,15,3,59,1,5),_ZyPoePowerSequenceDelay_Type())
zyPoePowerSequenceDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:zyPoePowerSequenceDelay.setStatus(_A)
_ZyxelPoePsePortTimeRangeTable_Object=MibTable
zyxelPoePsePortTimeRangeTable=_ZyxelPoePsePortTimeRangeTable_Object((1,3,6,1,4,1,890,1,15,3,59,1,6))
if mibBuilder.loadTexts:zyxelPoePsePortTimeRangeTable.setStatus(_A)
_ZyxelPoePsePortTimeRangeEntry_Object=MibTableRow
zyxelPoePsePortTimeRangeEntry=_ZyxelPoePsePortTimeRangeEntry_Object((1,3,6,1,4,1,890,1,15,3,59,1,6,1))
zyxelPoePsePortTimeRangeEntry.setIndexNames((0,_F,_G),(0,_H,_J))
if mibBuilder.loadTexts:zyxelPoePsePortTimeRangeEntry.setStatus(_A)
_ZyPoePsePortTimeRangeName_Type=DisplayString
_ZyPoePsePortTimeRangeName_Object=MibTableColumn
zyPoePsePortTimeRangeName=_ZyPoePsePortTimeRangeName_Object((1,3,6,1,4,1,890,1,15,3,59,1,6,1,1),_ZyPoePsePortTimeRangeName_Type())
zyPoePsePortTimeRangeName.setMaxAccess(_I)
if mibBuilder.loadTexts:zyPoePsePortTimeRangeName.setStatus(_A)
_ZyPoePsePortTimeRangeRowStatus_Type=RowStatus
_ZyPoePsePortTimeRangeRowStatus_Object=MibTableColumn
zyPoePsePortTimeRangeRowStatus=_ZyPoePsePortTimeRangeRowStatus_Object((1,3,6,1,4,1,890,1,15,3,59,1,6,1,2),_ZyPoePsePortTimeRangeRowStatus_Type())
zyPoePsePortTimeRangeRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:zyPoePsePortTimeRangeRowStatus.setStatus(_A)
_ZyPoeContinuousPoE_Type=EnabledStatus
_ZyPoeContinuousPoE_Object=MibScalar
zyPoeContinuousPoE=_ZyPoeContinuousPoE_Object((1,3,6,1,4,1,890,1,15,3,59,1,7),_ZyPoeContinuousPoE_Type())
zyPoeContinuousPoE.setMaxAccess(_B)
if mibBuilder.loadTexts:zyPoeContinuousPoE.setStatus(_A)
_ZyxelPoeStatus_ObjectIdentity=ObjectIdentity
zyxelPoeStatus=_ZyxelPoeStatus_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,59,2))
_ZyxelPoePsePortInfoTable_Object=MibTable
zyxelPoePsePortInfoTable=_ZyxelPoePsePortInfoTable_Object((1,3,6,1,4,1,890,1,15,3,59,2,1))
if mibBuilder.loadTexts:zyxelPoePsePortInfoTable.setStatus(_A)
_ZyxelPoePsePortInfoEntry_Object=MibTableRow
zyxelPoePsePortInfoEntry=_ZyxelPoePsePortInfoEntry_Object((1,3,6,1,4,1,890,1,15,3,59,2,1,1))
zyxelPoePsePortInfoEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:zyxelPoePsePortInfoEntry.setStatus(_A)
_ZyPoePsePortInfoPowerConsumption_Type=Integer32
_ZyPoePsePortInfoPowerConsumption_Object=MibTableColumn
zyPoePsePortInfoPowerConsumption=_ZyPoePsePortInfoPowerConsumption_Object((1,3,6,1,4,1,890,1,15,3,59,2,1,1,1),_ZyPoePsePortInfoPowerConsumption_Type())
zyPoePsePortInfoPowerConsumption.setMaxAccess(_I)
if mibBuilder.loadTexts:zyPoePsePortInfoPowerConsumption.setStatus(_A)
class _ZyPoePsePortTimeRangeState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('none',0),('in',1),('out',2)))
_ZyPoePsePortTimeRangeState_Type.__name__=_C
_ZyPoePsePortTimeRangeState_Object=MibTableColumn
zyPoePsePortTimeRangeState=_ZyPoePsePortTimeRangeState_Object((1,3,6,1,4,1,890,1,15,3,59,2,1,1,2),_ZyPoePsePortTimeRangeState_Type())
zyPoePsePortTimeRangeState.setMaxAccess(_I)
if mibBuilder.loadTexts:zyPoePsePortTimeRangeState.setStatus(_A)
_ZyPoePsePortTimeRangeInProfile_Type=DisplayString
_ZyPoePsePortTimeRangeInProfile_Object=MibTableColumn
zyPoePsePortTimeRangeInProfile=_ZyPoePsePortTimeRangeInProfile_Object((1,3,6,1,4,1,890,1,15,3,59,2,1,1,3),_ZyPoePsePortTimeRangeInProfile_Type())
zyPoePsePortTimeRangeInProfile.setMaxAccess(_I)
if mibBuilder.loadTexts:zyPoePsePortTimeRangeInProfile.setStatus(_A)
_ZyxelPoeTrapInfoObject_ObjectIdentity=ObjectIdentity
zyxelPoeTrapInfoObject=_ZyxelPoeTrapInfoObject_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,59,3))
class _ZyPoeTrapPsePowerSupplyFailedReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('internalPowerSupplyForPoeFailed',0),('rpsForPoeFailed',1),('rpsFanFailed',2),('rpsOverTemperature',3)))
_ZyPoeTrapPsePowerSupplyFailedReason_Type.__name__=_C
_ZyPoeTrapPsePowerSupplyFailedReason_Object=MibScalar
zyPoeTrapPsePowerSupplyFailedReason=_ZyPoeTrapPsePowerSupplyFailedReason_Object((1,3,6,1,4,1,890,1,15,3,59,3,1),_ZyPoeTrapPsePowerSupplyFailedReason_Type())
zyPoeTrapPsePowerSupplyFailedReason.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:zyPoeTrapPsePowerSupplyFailedReason.setStatus(_A)
_ZyxelPoeNotifications_ObjectIdentity=ObjectIdentity
zyxelPoeNotifications=_ZyxelPoeNotifications_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,59,4))
_ZyxelPoeAutoPdRecoverySetup_ObjectIdentity=ObjectIdentity
zyxelPoeAutoPdRecoverySetup=_ZyxelPoeAutoPdRecoverySetup_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,59,5))
_ZyPoeAutoPdRecoveryState_Type=EnabledStatus
_ZyPoeAutoPdRecoveryState_Object=MibScalar
zyPoeAutoPdRecoveryState=_ZyPoeAutoPdRecoveryState_Object((1,3,6,1,4,1,890,1,15,3,59,5,1),_ZyPoeAutoPdRecoveryState_Type())
zyPoeAutoPdRecoveryState.setMaxAccess(_B)
if mibBuilder.loadTexts:zyPoeAutoPdRecoveryState.setStatus(_A)
_ZyxelPoeAutoPdRecoveryPortTable_Object=MibTable
zyxelPoeAutoPdRecoveryPortTable=_ZyxelPoeAutoPdRecoveryPortTable_Object((1,3,6,1,4,1,890,1,15,3,59,5,2))
if mibBuilder.loadTexts:zyxelPoeAutoPdRecoveryPortTable.setStatus(_A)
_ZyxelPoeAutoPdRecoveryPortEntry_Object=MibTableRow
zyxelPoeAutoPdRecoveryPortEntry=_ZyxelPoeAutoPdRecoveryPortEntry_Object((1,3,6,1,4,1,890,1,15,3,59,5,2,1))
zyxelPoeAutoPdRecoveryPortEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:zyxelPoeAutoPdRecoveryPortEntry.setStatus(_A)
_ZyPoeAutoPdRecoveryPortState_Type=EnabledStatus
_ZyPoeAutoPdRecoveryPortState_Object=MibTableColumn
zyPoeAutoPdRecoveryPortState=_ZyPoeAutoPdRecoveryPortState_Object((1,3,6,1,4,1,890,1,15,3,59,5,2,1,1),_ZyPoeAutoPdRecoveryPortState_Type())
zyPoeAutoPdRecoveryPortState.setMaxAccess(_B)
if mibBuilder.loadTexts:zyPoeAutoPdRecoveryPortState.setStatus(_A)
class _ZyPoeAutoPdRecoveryPortMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('lldp',1),('ping',2)))
_ZyPoeAutoPdRecoveryPortMode_Type.__name__=_C
_ZyPoeAutoPdRecoveryPortMode_Object=MibTableColumn
zyPoeAutoPdRecoveryPortMode=_ZyPoeAutoPdRecoveryPortMode_Object((1,3,6,1,4,1,890,1,15,3,59,5,2,1,2),_ZyPoeAutoPdRecoveryPortMode_Type())
zyPoeAutoPdRecoveryPortMode.setMaxAccess(_B)
if mibBuilder.loadTexts:zyPoeAutoPdRecoveryPortMode.setStatus(_A)
_ZyPoeAutoPdRecoveryPortIpAddressType_Type=InetAddressType
_ZyPoeAutoPdRecoveryPortIpAddressType_Object=MibTableColumn
zyPoeAutoPdRecoveryPortIpAddressType=_ZyPoeAutoPdRecoveryPortIpAddressType_Object((1,3,6,1,4,1,890,1,15,3,59,5,2,1,3),_ZyPoeAutoPdRecoveryPortIpAddressType_Type())
zyPoeAutoPdRecoveryPortIpAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:zyPoeAutoPdRecoveryPortIpAddressType.setStatus(_A)
_ZyPoeAutoPdRecoveryPortIpAddress_Type=InetAddress
_ZyPoeAutoPdRecoveryPortIpAddress_Object=MibTableColumn
zyPoeAutoPdRecoveryPortIpAddress=_ZyPoeAutoPdRecoveryPortIpAddress_Object((1,3,6,1,4,1,890,1,15,3,59,5,2,1,4),_ZyPoeAutoPdRecoveryPortIpAddress_Type())
zyPoeAutoPdRecoveryPortIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:zyPoeAutoPdRecoveryPortIpAddress.setStatus(_A)
class _ZyPoeAutoPdRecoveryPollingInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,300))
_ZyPoeAutoPdRecoveryPollingInterval_Type.__name__=_C
_ZyPoeAutoPdRecoveryPollingInterval_Object=MibTableColumn
zyPoeAutoPdRecoveryPollingInterval=_ZyPoeAutoPdRecoveryPollingInterval_Object((1,3,6,1,4,1,890,1,15,3,59,5,2,1,5),_ZyPoeAutoPdRecoveryPollingInterval_Type())
zyPoeAutoPdRecoveryPollingInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:zyPoeAutoPdRecoveryPollingInterval.setStatus(_A)
class _ZyPoeAutoPdRecoveryPortPollingCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,5))
_ZyPoeAutoPdRecoveryPortPollingCount_Type.__name__=_C
_ZyPoeAutoPdRecoveryPortPollingCount_Object=MibTableColumn
zyPoeAutoPdRecoveryPortPollingCount=_ZyPoeAutoPdRecoveryPortPollingCount_Object((1,3,6,1,4,1,890,1,15,3,59,5,2,1,6),_ZyPoeAutoPdRecoveryPortPollingCount_Type())
zyPoeAutoPdRecoveryPortPollingCount.setMaxAccess(_B)
if mibBuilder.loadTexts:zyPoeAutoPdRecoveryPortPollingCount.setStatus(_A)
class _ZyPoeAutoPdRecoveryPortAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('reboot-alarm',1),('alarm',2)))
_ZyPoeAutoPdRecoveryPortAction_Type.__name__=_C
_ZyPoeAutoPdRecoveryPortAction_Object=MibTableColumn
zyPoeAutoPdRecoveryPortAction=_ZyPoeAutoPdRecoveryPortAction_Object((1,3,6,1,4,1,890,1,15,3,59,5,2,1,7),_ZyPoeAutoPdRecoveryPortAction_Type())
zyPoeAutoPdRecoveryPortAction.setMaxAccess(_B)
if mibBuilder.loadTexts:zyPoeAutoPdRecoveryPortAction.setStatus(_A)
class _ZyPoeAutoPdRecoveryPortResumePollingInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,800))
_ZyPoeAutoPdRecoveryPortResumePollingInterval_Type.__name__=_C
_ZyPoeAutoPdRecoveryPortResumePollingInterval_Object=MibTableColumn
zyPoeAutoPdRecoveryPortResumePollingInterval=_ZyPoeAutoPdRecoveryPortResumePollingInterval_Object((1,3,6,1,4,1,890,1,15,3,59,5,2,1,8),_ZyPoeAutoPdRecoveryPortResumePollingInterval_Type())
zyPoeAutoPdRecoveryPortResumePollingInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:zyPoeAutoPdRecoveryPortResumePollingInterval.setStatus(_A)
class _ZyPoeAutoPdRecoveryPortPdRebootCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_ZyPoeAutoPdRecoveryPortPdRebootCount_Type.__name__=_C
_ZyPoeAutoPdRecoveryPortPdRebootCount_Object=MibTableColumn
zyPoeAutoPdRecoveryPortPdRebootCount=_ZyPoeAutoPdRecoveryPortPdRebootCount_Object((1,3,6,1,4,1,890,1,15,3,59,5,2,1,9),_ZyPoeAutoPdRecoveryPortPdRebootCount_Type())
zyPoeAutoPdRecoveryPortPdRebootCount.setMaxAccess(_B)
if mibBuilder.loadTexts:zyPoeAutoPdRecoveryPortPdRebootCount.setStatus(_A)
class _ZyPoeAutoPdRecoveryPortResumePowerInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,120))
_ZyPoeAutoPdRecoveryPortResumePowerInterval_Type.__name__=_C
_ZyPoeAutoPdRecoveryPortResumePowerInterval_Object=MibTableColumn
zyPoeAutoPdRecoveryPortResumePowerInterval=_ZyPoeAutoPdRecoveryPortResumePowerInterval_Object((1,3,6,1,4,1,890,1,15,3,59,5,2,1,10),_ZyPoeAutoPdRecoveryPortResumePowerInterval_Type())
zyPoeAutoPdRecoveryPortResumePowerInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:zyPoeAutoPdRecoveryPortResumePowerInterval.setStatus(_A)
zyPoePowerPortOverload=NotificationType((1,3,6,1,4,1,890,1,15,3,59,4,1))
zyPoePowerPortOverload.setObjects((_D,_E))
if mibBuilder.loadTexts:zyPoePowerPortOverload.setStatus(_A)
zyPoePowerPortShortCircuit=NotificationType((1,3,6,1,4,1,890,1,15,3,59,4,2))
zyPoePowerPortShortCircuit.setObjects((_D,_E))
if mibBuilder.loadTexts:zyPoePowerPortShortCircuit.setStatus(_A)
zyPoePowerPortOverSystemBudget=NotificationType((1,3,6,1,4,1,890,1,15,3,59,4,3))
zyPoePowerPortOverSystemBudget.setObjects((_D,_E))
if mibBuilder.loadTexts:zyPoePowerPortOverSystemBudget.setStatus(_A)
zyPoePsePowerSupplyFailed=NotificationType((1,3,6,1,4,1,890,1,15,3,59,4,4))
zyPoePsePowerSupplyFailed.setObjects((_H,_K))
if mibBuilder.loadTexts:zyPoePsePowerSupplyFailed.setStatus(_A)
zyPoePowerPortOverloadRecovered=NotificationType((1,3,6,1,4,1,890,1,15,3,59,4,5))
zyPoePowerPortOverloadRecovered.setObjects((_D,_E))
if mibBuilder.loadTexts:zyPoePowerPortOverloadRecovered.setStatus(_A)
zyPoePowerPortShortCircuitRecovered=NotificationType((1,3,6,1,4,1,890,1,15,3,59,4,6))
zyPoePowerPortShortCircuitRecovered.setObjects((_D,_E))
if mibBuilder.loadTexts:zyPoePowerPortShortCircuitRecovered.setStatus(_A)
zyPoePowerPortOverSystemBudgetRecovered=NotificationType((1,3,6,1,4,1,890,1,15,3,59,4,7))
zyPoePowerPortOverSystemBudgetRecovered.setObjects((_D,_E))
if mibBuilder.loadTexts:zyPoePowerPortOverSystemBudgetRecovered.setStatus(_A)
zyPoeAutoPdRecoveryAlarm=NotificationType((1,3,6,1,4,1,890,1,15,3,59,4,8))
zyPoeAutoPdRecoveryAlarm.setObjects(*((_D,_E),(_H,_L)))
if mibBuilder.loadTexts:zyPoeAutoPdRecoveryAlarm.setStatus(_A)
zyPoePowerPortOverStandard=NotificationType((1,3,6,1,4,1,890,1,15,3,59,4,9))
zyPoePowerPortOverStandard.setObjects((_D,_E))
if mibBuilder.loadTexts:zyPoePowerPortOverStandard.setStatus(_A)
mibBuilder.exportSymbols(_H,**{'zyxelPoe':zyxelPoe,'zyxelPoeSetup':zyxelPoeSetup,'zyPoeMode':zyPoeMode,'zyxelPoePsePortTable':zyxelPoePsePortTable,'zyxelPoePsePortEntry':zyxelPoePsePortEntry,'zyPoePsePortMaxPower':zyPoePsePortMaxPower,'zyPoePsePowerUp':zyPoePsePowerUp,'zyPoePsePortTimeRange':zyPoePsePortTimeRange,'zyPoePseWideRangeDetection':zyPoePseWideRangeDetection,'zyPoePreAllocate':zyPoePreAllocate,'zyPoeDualDetection':zyPoeDualDetection,'zyPoePowerSequenceDelay':zyPoePowerSequenceDelay,'zyxelPoePsePortTimeRangeTable':zyxelPoePsePortTimeRangeTable,'zyxelPoePsePortTimeRangeEntry':zyxelPoePsePortTimeRangeEntry,_J:zyPoePsePortTimeRangeName,'zyPoePsePortTimeRangeRowStatus':zyPoePsePortTimeRangeRowStatus,'zyPoeContinuousPoE':zyPoeContinuousPoE,'zyxelPoeStatus':zyxelPoeStatus,'zyxelPoePsePortInfoTable':zyxelPoePsePortInfoTable,'zyxelPoePsePortInfoEntry':zyxelPoePsePortInfoEntry,'zyPoePsePortInfoPowerConsumption':zyPoePsePortInfoPowerConsumption,'zyPoePsePortTimeRangeState':zyPoePsePortTimeRangeState,'zyPoePsePortTimeRangeInProfile':zyPoePsePortTimeRangeInProfile,'zyxelPoeTrapInfoObject':zyxelPoeTrapInfoObject,_K:zyPoeTrapPsePowerSupplyFailedReason,'zyxelPoeNotifications':zyxelPoeNotifications,'zyPoePowerPortOverload':zyPoePowerPortOverload,'zyPoePowerPortShortCircuit':zyPoePowerPortShortCircuit,'zyPoePowerPortOverSystemBudget':zyPoePowerPortOverSystemBudget,'zyPoePsePowerSupplyFailed':zyPoePsePowerSupplyFailed,'zyPoePowerPortOverloadRecovered':zyPoePowerPortOverloadRecovered,'zyPoePowerPortShortCircuitRecovered':zyPoePowerPortShortCircuitRecovered,'zyPoePowerPortOverSystemBudgetRecovered':zyPoePowerPortOverSystemBudgetRecovered,'zyPoeAutoPdRecoveryAlarm':zyPoeAutoPdRecoveryAlarm,'zyPoePowerPortOverStandard':zyPoePowerPortOverStandard,'zyxelPoeAutoPdRecoverySetup':zyxelPoeAutoPdRecoverySetup,'zyPoeAutoPdRecoveryState':zyPoeAutoPdRecoveryState,'zyxelPoeAutoPdRecoveryPortTable':zyxelPoeAutoPdRecoveryPortTable,'zyxelPoeAutoPdRecoveryPortEntry':zyxelPoeAutoPdRecoveryPortEntry,'zyPoeAutoPdRecoveryPortState':zyPoeAutoPdRecoveryPortState,_L:zyPoeAutoPdRecoveryPortMode,'zyPoeAutoPdRecoveryPortIpAddressType':zyPoeAutoPdRecoveryPortIpAddressType,'zyPoeAutoPdRecoveryPortIpAddress':zyPoeAutoPdRecoveryPortIpAddress,'zyPoeAutoPdRecoveryPollingInterval':zyPoeAutoPdRecoveryPollingInterval,'zyPoeAutoPdRecoveryPortPollingCount':zyPoeAutoPdRecoveryPortPollingCount,'zyPoeAutoPdRecoveryPortAction':zyPoeAutoPdRecoveryPortAction,'zyPoeAutoPdRecoveryPortResumePollingInterval':zyPoeAutoPdRecoveryPortResumePollingInterval,'zyPoeAutoPdRecoveryPortPdRebootCount':zyPoeAutoPdRecoveryPortPdRebootCount,'zyPoeAutoPdRecoveryPortResumePowerInterval':zyPoeAutoPdRecoveryPortResumePowerInterval})