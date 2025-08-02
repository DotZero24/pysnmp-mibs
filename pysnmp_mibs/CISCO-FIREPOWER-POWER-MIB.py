_R='cfprPowerRackUnitMemberInstanceId'
_Q='cfprPowerProfiledPowerInstanceId'
_P='cfprPowerPrioWghtInstanceId'
_O='cfprPowerPolicyInstanceId'
_N='cfprPowerPlacementInstanceId'
_M='cfprPowerMgmtPolicyInstanceId'
_L='cfprPowerGroupStatsHistInstanceId'
_K='cfprPowerGroupStatsInstanceId'
_J='cfprPowerGroupQualInstanceId'
_I='cfprPowerGroupAdditionPolicyInstanceId'
_H='cfprPowerGroupInstanceId'
_G='cfprPowerEpInstanceId'
_F='cfprPowerChassisMemberInstanceId'
_E='cfprPowerBudgetInstanceId'
_D='not-accessible'
_C='CISCO-FIREPOWER-POWER-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
CfprManagedObjectDn,CfprManagedObjectId,ciscoFirepowerMIBObjects=mibBuilder.importSymbols('CISCO-FIREPOWER-MIB','CfprManagedObjectDn','CfprManagedObjectId','ciscoFirepowerMIBObjects')
CfprPolicyPolicyOwner,CfprPowerCapAction,CfprPowerChThrAction,CfprPowerGroupState,CfprPowerGroupStatsHistThresholded,CfprPowerGroupStatsThresholded,CfprPowerLockState,CfprPowerMemberState,CfprPowerMgmtStyle,CfprPowerOperState,CfprPowerPrioritySharing,CfprPowerProfilingMethod,CfprPowerPsuLineMode,CfprPowerPsuState,CfprPowerReallocation,CfprPowerReqConflict=mibBuilder.importSymbols('CISCO-FIREPOWER-TC-MIB','CfprPolicyPolicyOwner','CfprPowerCapAction','CfprPowerChThrAction','CfprPowerGroupState','CfprPowerGroupStatsHistThresholded','CfprPowerGroupStatsThresholded','CfprPowerLockState','CfprPowerMemberState','CfprPowerMgmtStyle','CfprPowerOperState','CfprPowerPrioritySharing','CfprPowerProfilingMethod','CfprPowerPsuLineMode','CfprPowerPsuState','CfprPowerReallocation','CfprPowerReqConflict')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CiscoAlarmSeverity,CiscoInetAddressMask,CiscoNetworkAddress,TimeIntervalSec,Unsigned64=mibBuilder.importSymbols('CISCO-TC','CiscoAlarmSeverity','CiscoInetAddressMask','CiscoNetworkAddress','TimeIntervalSec','Unsigned64')
InetAddressIPv4,InetAddressIPv6=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressIPv4','InetAddressIPv6')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowPointer,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowPointer','TextualConvention','TimeInterval','TimeStamp','TruthValue')
cfprPowerObjects=ModuleIdentity((1,3,6,1,4,1,9,9,826,1,64))
_CfprPowerBudgetTable_Object=MibTable
cfprPowerBudgetTable=_CfprPowerBudgetTable_Object((1,3,6,1,4,1,9,9,826,1,64,1))
if mibBuilder.loadTexts:cfprPowerBudgetTable.setStatus(_A)
_CfprPowerBudgetEntry_Object=MibTableRow
cfprPowerBudgetEntry=_CfprPowerBudgetEntry_Object((1,3,6,1,4,1,9,9,826,1,64,1,1))
cfprPowerBudgetEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:cfprPowerBudgetEntry.setStatus(_A)
_CfprPowerBudgetInstanceId_Type=CfprManagedObjectId
_CfprPowerBudgetInstanceId_Object=MibTableColumn
cfprPowerBudgetInstanceId=_CfprPowerBudgetInstanceId_Object((1,3,6,1,4,1,9,9,826,1,64,1,1,1),_CfprPowerBudgetInstanceId_Type())
cfprPowerBudgetInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprPowerBudgetInstanceId.setStatus(_A)
_CfprPowerBudgetDn_Type=CfprManagedObjectDn
_CfprPowerBudgetDn_Object=MibTableColumn
cfprPowerBudgetDn=_CfprPowerBudgetDn_Object((1,3,6,1,4,1,9,9,826,1,64,1,1,2),_CfprPowerBudgetDn_Type())
cfprPowerBudgetDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerBudgetDn.setStatus(_A)
_CfprPowerBudgetRn_Type=SnmpAdminString
_CfprPowerBudgetRn_Object=MibTableColumn
cfprPowerBudgetRn=_CfprPowerBudgetRn_Object((1,3,6,1,4,1,9,9,826,1,64,1,1,3),_CfprPowerBudgetRn_Type())
cfprPowerBudgetRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerBudgetRn.setStatus(_A)
_CfprPowerBudgetAdminCommitted_Type=Gauge32
_CfprPowerBudgetAdminCommitted_Object=MibTableColumn
cfprPowerBudgetAdminCommitted=_CfprPowerBudgetAdminCommitted_Object((1,3,6,1,4,1,9,9,826,1,64,1,1,4),_CfprPowerBudgetAdminCommitted_Type())
cfprPowerBudgetAdminCommitted.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerBudgetAdminCommitted.setStatus(_A)
_CfprPowerBudgetAdminFPLockState_Type=CfprPowerLockState
_CfprPowerBudgetAdminFPLockState_Object=MibTableColumn
cfprPowerBudgetAdminFPLockState=_CfprPowerBudgetAdminFPLockState_Object((1,3,6,1,4,1,9,9,826,1,64,1,1,5),_CfprPowerBudgetAdminFPLockState_Type())
cfprPowerBudgetAdminFPLockState.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerBudgetAdminFPLockState.setStatus(_A)
_CfprPowerBudgetAdminPeak_Type=Gauge32
_CfprPowerBudgetAdminPeak_Object=MibTableColumn
cfprPowerBudgetAdminPeak=_CfprPowerBudgetAdminPeak_Object((1,3,6,1,4,1,9,9,826,1,64,1,1,6),_CfprPowerBudgetAdminPeak_Type())
cfprPowerBudgetAdminPeak.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerBudgetAdminPeak.setStatus(_A)
_CfprPowerBudgetAdminPeakNew_Type=Gauge32
_CfprPowerBudgetAdminPeakNew_Object=MibTableColumn
cfprPowerBudgetAdminPeakNew=_CfprPowerBudgetAdminPeakNew_Object((1,3,6,1,4,1,9,9,826,1,64,1,1,7),_CfprPowerBudgetAdminPeakNew_Type())
cfprPowerBudgetAdminPeakNew.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerBudgetAdminPeakNew.setStatus(_A)
_CfprPowerBudgetBootPower_Type=Gauge32
_CfprPowerBudgetBootPower_Object=MibTableColumn
cfprPowerBudgetBootPower=_CfprPowerBudgetBootPower_Object((1,3,6,1,4,1,9,9,826,1,64,1,1,8),_CfprPowerBudgetBootPower_Type())
cfprPowerBudgetBootPower.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerBudgetBootPower.setStatus(_A)
_CfprPowerBudgetCapAction_Type=CfprPowerCapAction
_CfprPowerBudgetCapAction_Object=MibTableColumn
cfprPowerBudgetCapAction=_CfprPowerBudgetCapAction_Object((1,3,6,1,4,1,9,9,826,1,64,1,1,9),_CfprPowerBudgetCapAction_Type())
cfprPowerBudgetCapAction.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerBudgetCapAction.setStatus(_A)
_CfprPowerBudgetCatalogPower_Type=Gauge32
_CfprPowerBudgetCatalogPower_Object=MibTableColumn
cfprPowerBudgetCatalogPower=_CfprPowerBudgetCatalogPower_Object((1,3,6,1,4,1,9,9,826,1,64,1,1,10),_CfprPowerBudgetCatalogPower_Type())
cfprPowerBudgetCatalogPower.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerBudgetCatalogPower.setStatus(_A)
_CfprPowerBudgetChRsrvdPower_Type=Gauge32
_CfprPowerBudgetChRsrvdPower_Object=MibTableColumn
cfprPowerBudgetChRsrvdPower=_CfprPowerBudgetChRsrvdPower_Object((1,3,6,1,4,1,9,9,826,1,64,1,1,11),_CfprPowerBudgetChRsrvdPower_Type())
cfprPowerBudgetChRsrvdPower.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerBudgetChRsrvdPower.setStatus(_A)
_CfprPowerBudgetCurrentPower_Type=Gauge32
_CfprPowerBudgetCurrentPower_Object=MibTableColumn
cfprPowerBudgetCurrentPower=_CfprPowerBudgetCurrentPower_Object((1,3,6,1,4,1,9,9,826,1,64,1,1,12),_CfprPowerBudgetCurrentPower_Type())
cfprPowerBudgetCurrentPower.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerBudgetCurrentPower.setStatus(_A)
_CfprPowerBudgetDynRealloc_Type=CfprPowerReallocation
_CfprPowerBudgetDynRealloc_Object=MibTableColumn
cfprPowerBudgetDynRealloc=_CfprPowerBudgetDynRealloc_Object((1,3,6,1,4,1,9,9,826,1,64,1,1,13),_CfprPowerBudgetDynRealloc_Type())
cfprPowerBudgetDynRealloc.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerBudgetDynRealloc.setStatus(_A)
_CfprPowerBudgetGroupName_Type=SnmpAdminString
_CfprPowerBudgetGroupName_Object=MibTableColumn
cfprPowerBudgetGroupName=_CfprPowerBudgetGroupName_Object((1,3,6,1,4,1,9,9,826,1,64,1,1,14),_CfprPowerBudgetGroupName_Type())
cfprPowerBudgetGroupName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerBudgetGroupName.setStatus(_A)
_CfprPowerBudgetIdlePower_Type=Gauge32
_CfprPowerBudgetIdlePower_Object=MibTableColumn
cfprPowerBudgetIdlePower=_CfprPowerBudgetIdlePower_Object((1,3,6,1,4,1,9,9,826,1,64,1,1,15),_CfprPowerBudgetIdlePower_Type())
cfprPowerBudgetIdlePower.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerBudgetIdlePower.setStatus(_A)
_CfprPowerBudgetMaxPower_Type=Gauge32
_CfprPowerBudgetMaxPower_Object=MibTableColumn
cfprPowerBudgetMaxPower=_CfprPowerBudgetMaxPower_Object((1,3,6,1,4,1,9,9,826,1,64,1,1,16),_CfprPowerBudgetMaxPower_Type())
cfprPowerBudgetMaxPower.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerBudgetMaxPower.setStatus(_A)
_CfprPowerBudgetMinPower_Type=Gauge32
_CfprPowerBudgetMinPower_Object=MibTableColumn
cfprPowerBudgetMinPower=_CfprPowerBudgetMinPower_Object((1,3,6,1,4,1,9,9,826,1,64,1,1,17),_CfprPowerBudgetMinPower_Type())
cfprPowerBudgetMinPower.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerBudgetMinPower.setStatus(_A)
_CfprPowerBudgetOperCommitted_Type=Gauge32
_CfprPowerBudgetOperCommitted_Object=MibTableColumn
cfprPowerBudgetOperCommitted=_CfprPowerBudgetOperCommitted_Object((1,3,6,1,4,1,9,9,826,1,64,1,1,18),_CfprPowerBudgetOperCommitted_Type())
cfprPowerBudgetOperCommitted.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerBudgetOperCommitted.setStatus(_A)
_CfprPowerBudgetOperFPLockState_Type=CfprPowerLockState
_CfprPowerBudgetOperFPLockState_Object=MibTableColumn
cfprPowerBudgetOperFPLockState=_CfprPowerBudgetOperFPLockState_Object((1,3,6,1,4,1,9,9,826,1,64,1,1,19),_CfprPowerBudgetOperFPLockState_Type())
cfprPowerBudgetOperFPLockState.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerBudgetOperFPLockState.setStatus(_A)
_CfprPowerBudgetOperMin_Type=Gauge32
_CfprPowerBudgetOperMin_Object=MibTableColumn
cfprPowerBudgetOperMin=_CfprPowerBudgetOperMin_Object((1,3,6,1,4,1,9,9,826,1,64,1,1,20),_CfprPowerBudgetOperMin_Type())
cfprPowerBudgetOperMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerBudgetOperMin.setStatus(_A)
_CfprPowerBudgetOperPeak_Type=Gauge32
_CfprPowerBudgetOperPeak_Object=MibTableColumn
cfprPowerBudgetOperPeak=_CfprPowerBudgetOperPeak_Object((1,3,6,1,4,1,9,9,826,1,64,1,1,21),_CfprPowerBudgetOperPeak_Type())
cfprPowerBudgetOperPeak.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerBudgetOperPeak.setStatus(_A)
_CfprPowerBudgetOperProfMethod_Type=CfprPowerProfilingMethod
_CfprPowerBudgetOperProfMethod_Object=MibTableColumn
cfprPowerBudgetOperProfMethod=_CfprPowerBudgetOperProfMethod_Object((1,3,6,1,4,1,9,9,826,1,64,1,1,22),_CfprPowerBudgetOperProfMethod_Type())
cfprPowerBudgetOperProfMethod.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerBudgetOperProfMethod.setStatus(_A)
_CfprPowerBudgetOperState_Type=CfprPowerOperState
_CfprPowerBudgetOperState_Object=MibTableColumn
cfprPowerBudgetOperState=_CfprPowerBudgetOperState_Object((1,3,6,1,4,1,9,9,826,1,64,1,1,23),_CfprPowerBudgetOperState_Type())
cfprPowerBudgetOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerBudgetOperState.setStatus(_A)
_CfprPowerBudgetPrio_Type=Gauge32
_CfprPowerBudgetPrio_Object=MibTableColumn
cfprPowerBudgetPrio=_CfprPowerBudgetPrio_Object((1,3,6,1,4,1,9,9,826,1,64,1,1,24),_CfprPowerBudgetPrio_Type())
cfprPowerBudgetPrio.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerBudgetPrio.setStatus(_A)
_CfprPowerBudgetProfMethod_Type=CfprPowerProfilingMethod
_CfprPowerBudgetProfMethod_Object=MibTableColumn
cfprPowerBudgetProfMethod=_CfprPowerBudgetProfMethod_Object((1,3,6,1,4,1,9,9,826,1,64,1,1,25),_CfprPowerBudgetProfMethod_Type())
cfprPowerBudgetProfMethod.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerBudgetProfMethod.setStatus(_A)
_CfprPowerBudgetProfiling_Type=TruthValue
_CfprPowerBudgetProfiling_Object=MibTableColumn
cfprPowerBudgetProfiling=_CfprPowerBudgetProfiling_Object((1,3,6,1,4,1,9,9,826,1,64,1,1,26),_CfprPowerBudgetProfiling_Type())
cfprPowerBudgetProfiling.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerBudgetProfiling.setStatus(_A)
_CfprPowerBudgetPsuCapacity_Type=Gauge32
_CfprPowerBudgetPsuCapacity_Object=MibTableColumn
cfprPowerBudgetPsuCapacity=_CfprPowerBudgetPsuCapacity_Object((1,3,6,1,4,1,9,9,826,1,64,1,1,27),_CfprPowerBudgetPsuCapacity_Type())
cfprPowerBudgetPsuCapacity.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerBudgetPsuCapacity.setStatus(_A)
_CfprPowerBudgetPsuLineMode_Type=CfprPowerPsuLineMode
_CfprPowerBudgetPsuLineMode_Object=MibTableColumn
cfprPowerBudgetPsuLineMode=_CfprPowerBudgetPsuLineMode_Object((1,3,6,1,4,1,9,9,826,1,64,1,1,28),_CfprPowerBudgetPsuLineMode_Type())
cfprPowerBudgetPsuLineMode.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerBudgetPsuLineMode.setStatus(_A)
_CfprPowerBudgetPsuState_Type=CfprPowerPsuState
_CfprPowerBudgetPsuState_Object=MibTableColumn
cfprPowerBudgetPsuState=_CfprPowerBudgetPsuState_Object((1,3,6,1,4,1,9,9,826,1,64,1,1,29),_CfprPowerBudgetPsuState_Type())
cfprPowerBudgetPsuState.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerBudgetPsuState.setStatus(_A)
_CfprPowerBudgetScaledWt_Type=Gauge32
_CfprPowerBudgetScaledWt_Object=MibTableColumn
cfprPowerBudgetScaledWt=_CfprPowerBudgetScaledWt_Object((1,3,6,1,4,1,9,9,826,1,64,1,1,30),_CfprPowerBudgetScaledWt_Type())
cfprPowerBudgetScaledWt.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerBudgetScaledWt.setStatus(_A)
_CfprPowerBudgetStyle_Type=CfprPowerMgmtStyle
_CfprPowerBudgetStyle_Object=MibTableColumn
cfprPowerBudgetStyle=_CfprPowerBudgetStyle_Object((1,3,6,1,4,1,9,9,826,1,64,1,1,31),_CfprPowerBudgetStyle_Type())
cfprPowerBudgetStyle.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerBudgetStyle.setStatus(_A)
_CfprPowerBudgetUpdateTime_Type=DateAndTime
_CfprPowerBudgetUpdateTime_Object=MibTableColumn
cfprPowerBudgetUpdateTime=_CfprPowerBudgetUpdateTime_Object((1,3,6,1,4,1,9,9,826,1,64,1,1,32),_CfprPowerBudgetUpdateTime_Type())
cfprPowerBudgetUpdateTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerBudgetUpdateTime.setStatus(_A)
_CfprPowerBudgetWeight_Type=Gauge32
_CfprPowerBudgetWeight_Object=MibTableColumn
cfprPowerBudgetWeight=_CfprPowerBudgetWeight_Object((1,3,6,1,4,1,9,9,826,1,64,1,1,33),_CfprPowerBudgetWeight_Type())
cfprPowerBudgetWeight.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerBudgetWeight.setStatus(_A)
_CfprPowerChassisMemberTable_Object=MibTable
cfprPowerChassisMemberTable=_CfprPowerChassisMemberTable_Object((1,3,6,1,4,1,9,9,826,1,64,2))
if mibBuilder.loadTexts:cfprPowerChassisMemberTable.setStatus(_A)
_CfprPowerChassisMemberEntry_Object=MibTableRow
cfprPowerChassisMemberEntry=_CfprPowerChassisMemberEntry_Object((1,3,6,1,4,1,9,9,826,1,64,2,1))
cfprPowerChassisMemberEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:cfprPowerChassisMemberEntry.setStatus(_A)
_CfprPowerChassisMemberInstanceId_Type=CfprManagedObjectId
_CfprPowerChassisMemberInstanceId_Object=MibTableColumn
cfprPowerChassisMemberInstanceId=_CfprPowerChassisMemberInstanceId_Object((1,3,6,1,4,1,9,9,826,1,64,2,1,1),_CfprPowerChassisMemberInstanceId_Type())
cfprPowerChassisMemberInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprPowerChassisMemberInstanceId.setStatus(_A)
_CfprPowerChassisMemberDn_Type=CfprManagedObjectDn
_CfprPowerChassisMemberDn_Object=MibTableColumn
cfprPowerChassisMemberDn=_CfprPowerChassisMemberDn_Object((1,3,6,1,4,1,9,9,826,1,64,2,1,2),_CfprPowerChassisMemberDn_Type())
cfprPowerChassisMemberDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerChassisMemberDn.setStatus(_A)
_CfprPowerChassisMemberRn_Type=SnmpAdminString
_CfprPowerChassisMemberRn_Object=MibTableColumn
cfprPowerChassisMemberRn=_CfprPowerChassisMemberRn_Object((1,3,6,1,4,1,9,9,826,1,64,2,1,3),_CfprPowerChassisMemberRn_Type())
cfprPowerChassisMemberRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerChassisMemberRn.setStatus(_A)
_CfprPowerChassisMemberId_Type=Gauge32
_CfprPowerChassisMemberId_Object=MibTableColumn
cfprPowerChassisMemberId=_CfprPowerChassisMemberId_Object((1,3,6,1,4,1,9,9,826,1,64,2,1,4),_CfprPowerChassisMemberId_Type())
cfprPowerChassisMemberId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerChassisMemberId.setStatus(_A)
_CfprPowerChassisMemberOperState_Type=CfprPowerMemberState
_CfprPowerChassisMemberOperState_Object=MibTableColumn
cfprPowerChassisMemberOperState=_CfprPowerChassisMemberOperState_Object((1,3,6,1,4,1,9,9,826,1,64,2,1,5),_CfprPowerChassisMemberOperState_Type())
cfprPowerChassisMemberOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerChassisMemberOperState.setStatus(_A)
_CfprPowerEpTable_Object=MibTable
cfprPowerEpTable=_CfprPowerEpTable_Object((1,3,6,1,4,1,9,9,826,1,64,3))
if mibBuilder.loadTexts:cfprPowerEpTable.setStatus(_A)
_CfprPowerEpEntry_Object=MibTableRow
cfprPowerEpEntry=_CfprPowerEpEntry_Object((1,3,6,1,4,1,9,9,826,1,64,3,1))
cfprPowerEpEntry.setIndexNames((0,_C,_G))
if mibBuilder.loadTexts:cfprPowerEpEntry.setStatus(_A)
_CfprPowerEpInstanceId_Type=CfprManagedObjectId
_CfprPowerEpInstanceId_Object=MibTableColumn
cfprPowerEpInstanceId=_CfprPowerEpInstanceId_Object((1,3,6,1,4,1,9,9,826,1,64,3,1,1),_CfprPowerEpInstanceId_Type())
cfprPowerEpInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprPowerEpInstanceId.setStatus(_A)
_CfprPowerEpDn_Type=CfprManagedObjectDn
_CfprPowerEpDn_Object=MibTableColumn
cfprPowerEpDn=_CfprPowerEpDn_Object((1,3,6,1,4,1,9,9,826,1,64,3,1,2),_CfprPowerEpDn_Type())
cfprPowerEpDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerEpDn.setStatus(_A)
_CfprPowerEpRn_Type=SnmpAdminString
_CfprPowerEpRn_Object=MibTableColumn
cfprPowerEpRn=_CfprPowerEpRn_Object((1,3,6,1,4,1,9,9,826,1,64,3,1,3),_CfprPowerEpRn_Type())
cfprPowerEpRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerEpRn.setStatus(_A)
_CfprPowerGroupTable_Object=MibTable
cfprPowerGroupTable=_CfprPowerGroupTable_Object((1,3,6,1,4,1,9,9,826,1,64,4))
if mibBuilder.loadTexts:cfprPowerGroupTable.setStatus(_A)
_CfprPowerGroupEntry_Object=MibTableRow
cfprPowerGroupEntry=_CfprPowerGroupEntry_Object((1,3,6,1,4,1,9,9,826,1,64,4,1))
cfprPowerGroupEntry.setIndexNames((0,_C,_H))
if mibBuilder.loadTexts:cfprPowerGroupEntry.setStatus(_A)
_CfprPowerGroupInstanceId_Type=CfprManagedObjectId
_CfprPowerGroupInstanceId_Object=MibTableColumn
cfprPowerGroupInstanceId=_CfprPowerGroupInstanceId_Object((1,3,6,1,4,1,9,9,826,1,64,4,1,1),_CfprPowerGroupInstanceId_Type())
cfprPowerGroupInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprPowerGroupInstanceId.setStatus(_A)
_CfprPowerGroupDn_Type=CfprManagedObjectDn
_CfprPowerGroupDn_Object=MibTableColumn
cfprPowerGroupDn=_CfprPowerGroupDn_Object((1,3,6,1,4,1,9,9,826,1,64,4,1,2),_CfprPowerGroupDn_Type())
cfprPowerGroupDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerGroupDn.setStatus(_A)
_CfprPowerGroupRn_Type=SnmpAdminString
_CfprPowerGroupRn_Object=MibTableColumn
cfprPowerGroupRn=_CfprPowerGroupRn_Object((1,3,6,1,4,1,9,9,826,1,64,4,1,3),_CfprPowerGroupRn_Type())
cfprPowerGroupRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerGroupRn.setStatus(_A)
_CfprPowerGroupAdminCommitted_Type=Gauge32
_CfprPowerGroupAdminCommitted_Object=MibTableColumn
cfprPowerGroupAdminCommitted=_CfprPowerGroupAdminCommitted_Object((1,3,6,1,4,1,9,9,826,1,64,4,1,4),_CfprPowerGroupAdminCommitted_Type())
cfprPowerGroupAdminCommitted.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerGroupAdminCommitted.setStatus(_A)
_CfprPowerGroupAdminPeak_Type=Gauge32
_CfprPowerGroupAdminPeak_Object=MibTableColumn
cfprPowerGroupAdminPeak=_CfprPowerGroupAdminPeak_Object((1,3,6,1,4,1,9,9,826,1,64,4,1,5),_CfprPowerGroupAdminPeak_Type())
cfprPowerGroupAdminPeak.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerGroupAdminPeak.setStatus(_A)
_CfprPowerGroupCurReqPower_Type=Gauge32
_CfprPowerGroupCurReqPower_Object=MibTableColumn
cfprPowerGroupCurReqPower=_CfprPowerGroupCurReqPower_Object((1,3,6,1,4,1,9,9,826,1,64,4,1,6),_CfprPowerGroupCurReqPower_Type())
cfprPowerGroupCurReqPower.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerGroupCurReqPower.setStatus(_A)
_CfprPowerGroupCurrentPower_Type=Gauge32
_CfprPowerGroupCurrentPower_Object=MibTableColumn
cfprPowerGroupCurrentPower=_CfprPowerGroupCurrentPower_Object((1,3,6,1,4,1,9,9,826,1,64,4,1,7),_CfprPowerGroupCurrentPower_Type())
cfprPowerGroupCurrentPower.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerGroupCurrentPower.setStatus(_A)
_CfprPowerGroupDescr_Type=SnmpAdminString
_CfprPowerGroupDescr_Object=MibTableColumn
cfprPowerGroupDescr=_CfprPowerGroupDescr_Object((1,3,6,1,4,1,9,9,826,1,64,4,1,8),_CfprPowerGroupDescr_Type())
cfprPowerGroupDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerGroupDescr.setStatus(_A)
_CfprPowerGroupFltAggr_Type=Unsigned64
_CfprPowerGroupFltAggr_Object=MibTableColumn
cfprPowerGroupFltAggr=_CfprPowerGroupFltAggr_Object((1,3,6,1,4,1,9,9,826,1,64,4,1,9),_CfprPowerGroupFltAggr_Type())
cfprPowerGroupFltAggr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerGroupFltAggr.setStatus(_A)
_CfprPowerGroupIntId_Type=SnmpAdminString
_CfprPowerGroupIntId_Object=MibTableColumn
cfprPowerGroupIntId=_CfprPowerGroupIntId_Object((1,3,6,1,4,1,9,9,826,1,64,4,1,10),_CfprPowerGroupIntId_Type())
cfprPowerGroupIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerGroupIntId.setStatus(_A)
_CfprPowerGroupMinReqPower_Type=Gauge32
_CfprPowerGroupMinReqPower_Object=MibTableColumn
cfprPowerGroupMinReqPower=_CfprPowerGroupMinReqPower_Object((1,3,6,1,4,1,9,9,826,1,64,4,1,11),_CfprPowerGroupMinReqPower_Type())
cfprPowerGroupMinReqPower.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerGroupMinReqPower.setStatus(_A)
_CfprPowerGroupName_Type=SnmpAdminString
_CfprPowerGroupName_Object=MibTableColumn
cfprPowerGroupName=_CfprPowerGroupName_Object((1,3,6,1,4,1,9,9,826,1,64,4,1,12),_CfprPowerGroupName_Type())
cfprPowerGroupName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerGroupName.setStatus(_A)
_CfprPowerGroupOperCommitted_Type=Gauge32
_CfprPowerGroupOperCommitted_Object=MibTableColumn
cfprPowerGroupOperCommitted=_CfprPowerGroupOperCommitted_Object((1,3,6,1,4,1,9,9,826,1,64,4,1,13),_CfprPowerGroupOperCommitted_Type())
cfprPowerGroupOperCommitted.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerGroupOperCommitted.setStatus(_A)
_CfprPowerGroupOperPeak_Type=Gauge32
_CfprPowerGroupOperPeak_Object=MibTableColumn
cfprPowerGroupOperPeak=_CfprPowerGroupOperPeak_Object((1,3,6,1,4,1,9,9,826,1,64,4,1,14),_CfprPowerGroupOperPeak_Type())
cfprPowerGroupOperPeak.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerGroupOperPeak.setStatus(_A)
_CfprPowerGroupOperState_Type=CfprPowerGroupState
_CfprPowerGroupOperState_Object=MibTableColumn
cfprPowerGroupOperState=_CfprPowerGroupOperState_Object((1,3,6,1,4,1,9,9,826,1,64,4,1,15),_CfprPowerGroupOperState_Type())
cfprPowerGroupOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerGroupOperState.setStatus(_A)
_CfprPowerGroupPolicyLevel_Type=Gauge32
_CfprPowerGroupPolicyLevel_Object=MibTableColumn
cfprPowerGroupPolicyLevel=_CfprPowerGroupPolicyLevel_Object((1,3,6,1,4,1,9,9,826,1,64,4,1,16),_CfprPowerGroupPolicyLevel_Type())
cfprPowerGroupPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerGroupPolicyLevel.setStatus(_A)
_CfprPowerGroupPolicyOwner_Type=CfprPolicyPolicyOwner
_CfprPowerGroupPolicyOwner_Object=MibTableColumn
cfprPowerGroupPolicyOwner=_CfprPowerGroupPolicyOwner_Object((1,3,6,1,4,1,9,9,826,1,64,4,1,17),_CfprPowerGroupPolicyOwner_Type())
cfprPowerGroupPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerGroupPolicyOwner.setStatus(_A)
_CfprPowerGroupQualifier_Type=SnmpAdminString
_CfprPowerGroupQualifier_Object=MibTableColumn
cfprPowerGroupQualifier=_CfprPowerGroupQualifier_Object((1,3,6,1,4,1,9,9,826,1,64,4,1,18),_CfprPowerGroupQualifier_Type())
cfprPowerGroupQualifier.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerGroupQualifier.setStatus(_A)
_CfprPowerGroupRealloc_Type=CfprPowerReallocation
_CfprPowerGroupRealloc_Object=MibTableColumn
cfprPowerGroupRealloc=_CfprPowerGroupRealloc_Object((1,3,6,1,4,1,9,9,826,1,64,4,1,19),_CfprPowerGroupRealloc_Type())
cfprPowerGroupRealloc.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerGroupRealloc.setStatus(_A)
_CfprPowerGroupAdditionPolicyTable_Object=MibTable
cfprPowerGroupAdditionPolicyTable=_CfprPowerGroupAdditionPolicyTable_Object((1,3,6,1,4,1,9,9,826,1,64,5))
if mibBuilder.loadTexts:cfprPowerGroupAdditionPolicyTable.setStatus(_A)
_CfprPowerGroupAdditionPolicyEntry_Object=MibTableRow
cfprPowerGroupAdditionPolicyEntry=_CfprPowerGroupAdditionPolicyEntry_Object((1,3,6,1,4,1,9,9,826,1,64,5,1))
cfprPowerGroupAdditionPolicyEntry.setIndexNames((0,_C,_I))
if mibBuilder.loadTexts:cfprPowerGroupAdditionPolicyEntry.setStatus(_A)
_CfprPowerGroupAdditionPolicyInstanceId_Type=CfprManagedObjectId
_CfprPowerGroupAdditionPolicyInstanceId_Object=MibTableColumn
cfprPowerGroupAdditionPolicyInstanceId=_CfprPowerGroupAdditionPolicyInstanceId_Object((1,3,6,1,4,1,9,9,826,1,64,5,1,1),_CfprPowerGroupAdditionPolicyInstanceId_Type())
cfprPowerGroupAdditionPolicyInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprPowerGroupAdditionPolicyInstanceId.setStatus(_A)
_CfprPowerGroupAdditionPolicyDn_Type=CfprManagedObjectDn
_CfprPowerGroupAdditionPolicyDn_Object=MibTableColumn
cfprPowerGroupAdditionPolicyDn=_CfprPowerGroupAdditionPolicyDn_Object((1,3,6,1,4,1,9,9,826,1,64,5,1,2),_CfprPowerGroupAdditionPolicyDn_Type())
cfprPowerGroupAdditionPolicyDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerGroupAdditionPolicyDn.setStatus(_A)
_CfprPowerGroupAdditionPolicyRn_Type=SnmpAdminString
_CfprPowerGroupAdditionPolicyRn_Object=MibTableColumn
cfprPowerGroupAdditionPolicyRn=_CfprPowerGroupAdditionPolicyRn_Object((1,3,6,1,4,1,9,9,826,1,64,5,1,3),_CfprPowerGroupAdditionPolicyRn_Type())
cfprPowerGroupAdditionPolicyRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerGroupAdditionPolicyRn.setStatus(_A)
_CfprPowerGroupAdditionPolicyAction_Type=CfprPowerChThrAction
_CfprPowerGroupAdditionPolicyAction_Object=MibTableColumn
cfprPowerGroupAdditionPolicyAction=_CfprPowerGroupAdditionPolicyAction_Object((1,3,6,1,4,1,9,9,826,1,64,5,1,4),_CfprPowerGroupAdditionPolicyAction_Type())
cfprPowerGroupAdditionPolicyAction.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerGroupAdditionPolicyAction.setStatus(_A)
_CfprPowerGroupAdditionPolicyDescr_Type=SnmpAdminString
_CfprPowerGroupAdditionPolicyDescr_Object=MibTableColumn
cfprPowerGroupAdditionPolicyDescr=_CfprPowerGroupAdditionPolicyDescr_Object((1,3,6,1,4,1,9,9,826,1,64,5,1,5),_CfprPowerGroupAdditionPolicyDescr_Type())
cfprPowerGroupAdditionPolicyDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerGroupAdditionPolicyDescr.setStatus(_A)
_CfprPowerGroupAdditionPolicyIntId_Type=SnmpAdminString
_CfprPowerGroupAdditionPolicyIntId_Object=MibTableColumn
cfprPowerGroupAdditionPolicyIntId=_CfprPowerGroupAdditionPolicyIntId_Object((1,3,6,1,4,1,9,9,826,1,64,5,1,6),_CfprPowerGroupAdditionPolicyIntId_Type())
cfprPowerGroupAdditionPolicyIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerGroupAdditionPolicyIntId.setStatus(_A)
_CfprPowerGroupAdditionPolicyName_Type=SnmpAdminString
_CfprPowerGroupAdditionPolicyName_Object=MibTableColumn
cfprPowerGroupAdditionPolicyName=_CfprPowerGroupAdditionPolicyName_Object((1,3,6,1,4,1,9,9,826,1,64,5,1,7),_CfprPowerGroupAdditionPolicyName_Type())
cfprPowerGroupAdditionPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerGroupAdditionPolicyName.setStatus(_A)
_CfprPowerGroupAdditionPolicyPolicyLevel_Type=Gauge32
_CfprPowerGroupAdditionPolicyPolicyLevel_Object=MibTableColumn
cfprPowerGroupAdditionPolicyPolicyLevel=_CfprPowerGroupAdditionPolicyPolicyLevel_Object((1,3,6,1,4,1,9,9,826,1,64,5,1,8),_CfprPowerGroupAdditionPolicyPolicyLevel_Type())
cfprPowerGroupAdditionPolicyPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerGroupAdditionPolicyPolicyLevel.setStatus(_A)
_CfprPowerGroupAdditionPolicyPolicyOwner_Type=CfprPolicyPolicyOwner
_CfprPowerGroupAdditionPolicyPolicyOwner_Object=MibTableColumn
cfprPowerGroupAdditionPolicyPolicyOwner=_CfprPowerGroupAdditionPolicyPolicyOwner_Object((1,3,6,1,4,1,9,9,826,1,64,5,1,9),_CfprPowerGroupAdditionPolicyPolicyOwner_Type())
cfprPowerGroupAdditionPolicyPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerGroupAdditionPolicyPolicyOwner.setStatus(_A)
_CfprPowerGroupQualTable_Object=MibTable
cfprPowerGroupQualTable=_CfprPowerGroupQualTable_Object((1,3,6,1,4,1,9,9,826,1,64,6))
if mibBuilder.loadTexts:cfprPowerGroupQualTable.setStatus(_A)
_CfprPowerGroupQualEntry_Object=MibTableRow
cfprPowerGroupQualEntry=_CfprPowerGroupQualEntry_Object((1,3,6,1,4,1,9,9,826,1,64,6,1))
cfprPowerGroupQualEntry.setIndexNames((0,_C,_J))
if mibBuilder.loadTexts:cfprPowerGroupQualEntry.setStatus(_A)
_CfprPowerGroupQualInstanceId_Type=CfprManagedObjectId
_CfprPowerGroupQualInstanceId_Object=MibTableColumn
cfprPowerGroupQualInstanceId=_CfprPowerGroupQualInstanceId_Object((1,3,6,1,4,1,9,9,826,1,64,6,1,1),_CfprPowerGroupQualInstanceId_Type())
cfprPowerGroupQualInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprPowerGroupQualInstanceId.setStatus(_A)
_CfprPowerGroupQualDn_Type=CfprManagedObjectDn
_CfprPowerGroupQualDn_Object=MibTableColumn
cfprPowerGroupQualDn=_CfprPowerGroupQualDn_Object((1,3,6,1,4,1,9,9,826,1,64,6,1,2),_CfprPowerGroupQualDn_Type())
cfprPowerGroupQualDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerGroupQualDn.setStatus(_A)
_CfprPowerGroupQualRn_Type=SnmpAdminString
_CfprPowerGroupQualRn_Object=MibTableColumn
cfprPowerGroupQualRn=_CfprPowerGroupQualRn_Object((1,3,6,1,4,1,9,9,826,1,64,6,1,3),_CfprPowerGroupQualRn_Type())
cfprPowerGroupQualRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerGroupQualRn.setStatus(_A)
_CfprPowerGroupQualGroupName_Type=SnmpAdminString
_CfprPowerGroupQualGroupName_Object=MibTableColumn
cfprPowerGroupQualGroupName=_CfprPowerGroupQualGroupName_Object((1,3,6,1,4,1,9,9,826,1,64,6,1,4),_CfprPowerGroupQualGroupName_Type())
cfprPowerGroupQualGroupName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerGroupQualGroupName.setStatus(_A)
_CfprPowerGroupStatsTable_Object=MibTable
cfprPowerGroupStatsTable=_CfprPowerGroupStatsTable_Object((1,3,6,1,4,1,9,9,826,1,64,7))
if mibBuilder.loadTexts:cfprPowerGroupStatsTable.setStatus(_A)
_CfprPowerGroupStatsEntry_Object=MibTableRow
cfprPowerGroupStatsEntry=_CfprPowerGroupStatsEntry_Object((1,3,6,1,4,1,9,9,826,1,64,7,1))
cfprPowerGroupStatsEntry.setIndexNames((0,_C,_K))
if mibBuilder.loadTexts:cfprPowerGroupStatsEntry.setStatus(_A)
_CfprPowerGroupStatsInstanceId_Type=CfprManagedObjectId
_CfprPowerGroupStatsInstanceId_Object=MibTableColumn
cfprPowerGroupStatsInstanceId=_CfprPowerGroupStatsInstanceId_Object((1,3,6,1,4,1,9,9,826,1,64,7,1,1),_CfprPowerGroupStatsInstanceId_Type())
cfprPowerGroupStatsInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprPowerGroupStatsInstanceId.setStatus(_A)
_CfprPowerGroupStatsDn_Type=CfprManagedObjectDn
_CfprPowerGroupStatsDn_Object=MibTableColumn
cfprPowerGroupStatsDn=_CfprPowerGroupStatsDn_Object((1,3,6,1,4,1,9,9,826,1,64,7,1,2),_CfprPowerGroupStatsDn_Type())
cfprPowerGroupStatsDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerGroupStatsDn.setStatus(_A)
_CfprPowerGroupStatsRn_Type=SnmpAdminString
_CfprPowerGroupStatsRn_Object=MibTableColumn
cfprPowerGroupStatsRn=_CfprPowerGroupStatsRn_Object((1,3,6,1,4,1,9,9,826,1,64,7,1,3),_CfprPowerGroupStatsRn_Type())
cfprPowerGroupStatsRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerGroupStatsRn.setStatus(_A)
_CfprPowerGroupStatsIntervals_Type=Gauge32
_CfprPowerGroupStatsIntervals_Object=MibTableColumn
cfprPowerGroupStatsIntervals=_CfprPowerGroupStatsIntervals_Object((1,3,6,1,4,1,9,9,826,1,64,7,1,4),_CfprPowerGroupStatsIntervals_Type())
cfprPowerGroupStatsIntervals.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerGroupStatsIntervals.setStatus(_A)
_CfprPowerGroupStatsPower_Type=Integer32
_CfprPowerGroupStatsPower_Object=MibTableColumn
cfprPowerGroupStatsPower=_CfprPowerGroupStatsPower_Object((1,3,6,1,4,1,9,9,826,1,64,7,1,5),_CfprPowerGroupStatsPower_Type())
cfprPowerGroupStatsPower.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerGroupStatsPower.setStatus(_A)
_CfprPowerGroupStatsPowerAvg_Type=Integer32
_CfprPowerGroupStatsPowerAvg_Object=MibTableColumn
cfprPowerGroupStatsPowerAvg=_CfprPowerGroupStatsPowerAvg_Object((1,3,6,1,4,1,9,9,826,1,64,7,1,6),_CfprPowerGroupStatsPowerAvg_Type())
cfprPowerGroupStatsPowerAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerGroupStatsPowerAvg.setStatus(_A)
_CfprPowerGroupStatsPowerMax_Type=Integer32
_CfprPowerGroupStatsPowerMax_Object=MibTableColumn
cfprPowerGroupStatsPowerMax=_CfprPowerGroupStatsPowerMax_Object((1,3,6,1,4,1,9,9,826,1,64,7,1,7),_CfprPowerGroupStatsPowerMax_Type())
cfprPowerGroupStatsPowerMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerGroupStatsPowerMax.setStatus(_A)
_CfprPowerGroupStatsPowerMin_Type=Integer32
_CfprPowerGroupStatsPowerMin_Object=MibTableColumn
cfprPowerGroupStatsPowerMin=_CfprPowerGroupStatsPowerMin_Object((1,3,6,1,4,1,9,9,826,1,64,7,1,8),_CfprPowerGroupStatsPowerMin_Type())
cfprPowerGroupStatsPowerMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerGroupStatsPowerMin.setStatus(_A)
_CfprPowerGroupStatsSuspect_Type=TruthValue
_CfprPowerGroupStatsSuspect_Object=MibTableColumn
cfprPowerGroupStatsSuspect=_CfprPowerGroupStatsSuspect_Object((1,3,6,1,4,1,9,9,826,1,64,7,1,9),_CfprPowerGroupStatsSuspect_Type())
cfprPowerGroupStatsSuspect.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerGroupStatsSuspect.setStatus(_A)
_CfprPowerGroupStatsThresholded_Type=CfprPowerGroupStatsThresholded
_CfprPowerGroupStatsThresholded_Object=MibTableColumn
cfprPowerGroupStatsThresholded=_CfprPowerGroupStatsThresholded_Object((1,3,6,1,4,1,9,9,826,1,64,7,1,10),_CfprPowerGroupStatsThresholded_Type())
cfprPowerGroupStatsThresholded.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerGroupStatsThresholded.setStatus(_A)
_CfprPowerGroupStatsTimeCollected_Type=DateAndTime
_CfprPowerGroupStatsTimeCollected_Object=MibTableColumn
cfprPowerGroupStatsTimeCollected=_CfprPowerGroupStatsTimeCollected_Object((1,3,6,1,4,1,9,9,826,1,64,7,1,11),_CfprPowerGroupStatsTimeCollected_Type())
cfprPowerGroupStatsTimeCollected.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerGroupStatsTimeCollected.setStatus(_A)
_CfprPowerGroupStatsUpdate_Type=Gauge32
_CfprPowerGroupStatsUpdate_Object=MibTableColumn
cfprPowerGroupStatsUpdate=_CfprPowerGroupStatsUpdate_Object((1,3,6,1,4,1,9,9,826,1,64,7,1,12),_CfprPowerGroupStatsUpdate_Type())
cfprPowerGroupStatsUpdate.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerGroupStatsUpdate.setStatus(_A)
_CfprPowerGroupStatsHistTable_Object=MibTable
cfprPowerGroupStatsHistTable=_CfprPowerGroupStatsHistTable_Object((1,3,6,1,4,1,9,9,826,1,64,8))
if mibBuilder.loadTexts:cfprPowerGroupStatsHistTable.setStatus(_A)
_CfprPowerGroupStatsHistEntry_Object=MibTableRow
cfprPowerGroupStatsHistEntry=_CfprPowerGroupStatsHistEntry_Object((1,3,6,1,4,1,9,9,826,1,64,8,1))
cfprPowerGroupStatsHistEntry.setIndexNames((0,_C,_L))
if mibBuilder.loadTexts:cfprPowerGroupStatsHistEntry.setStatus(_A)
_CfprPowerGroupStatsHistInstanceId_Type=CfprManagedObjectId
_CfprPowerGroupStatsHistInstanceId_Object=MibTableColumn
cfprPowerGroupStatsHistInstanceId=_CfprPowerGroupStatsHistInstanceId_Object((1,3,6,1,4,1,9,9,826,1,64,8,1,1),_CfprPowerGroupStatsHistInstanceId_Type())
cfprPowerGroupStatsHistInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprPowerGroupStatsHistInstanceId.setStatus(_A)
_CfprPowerGroupStatsHistDn_Type=CfprManagedObjectDn
_CfprPowerGroupStatsHistDn_Object=MibTableColumn
cfprPowerGroupStatsHistDn=_CfprPowerGroupStatsHistDn_Object((1,3,6,1,4,1,9,9,826,1,64,8,1,2),_CfprPowerGroupStatsHistDn_Type())
cfprPowerGroupStatsHistDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerGroupStatsHistDn.setStatus(_A)
_CfprPowerGroupStatsHistRn_Type=SnmpAdminString
_CfprPowerGroupStatsHistRn_Object=MibTableColumn
cfprPowerGroupStatsHistRn=_CfprPowerGroupStatsHistRn_Object((1,3,6,1,4,1,9,9,826,1,64,8,1,3),_CfprPowerGroupStatsHistRn_Type())
cfprPowerGroupStatsHistRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerGroupStatsHistRn.setStatus(_A)
_CfprPowerGroupStatsHistId_Type=Unsigned64
_CfprPowerGroupStatsHistId_Object=MibTableColumn
cfprPowerGroupStatsHistId=_CfprPowerGroupStatsHistId_Object((1,3,6,1,4,1,9,9,826,1,64,8,1,4),_CfprPowerGroupStatsHistId_Type())
cfprPowerGroupStatsHistId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerGroupStatsHistId.setStatus(_A)
_CfprPowerGroupStatsHistMostRecent_Type=TruthValue
_CfprPowerGroupStatsHistMostRecent_Object=MibTableColumn
cfprPowerGroupStatsHistMostRecent=_CfprPowerGroupStatsHistMostRecent_Object((1,3,6,1,4,1,9,9,826,1,64,8,1,5),_CfprPowerGroupStatsHistMostRecent_Type())
cfprPowerGroupStatsHistMostRecent.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerGroupStatsHistMostRecent.setStatus(_A)
_CfprPowerGroupStatsHistPower_Type=Integer32
_CfprPowerGroupStatsHistPower_Object=MibTableColumn
cfprPowerGroupStatsHistPower=_CfprPowerGroupStatsHistPower_Object((1,3,6,1,4,1,9,9,826,1,64,8,1,6),_CfprPowerGroupStatsHistPower_Type())
cfprPowerGroupStatsHistPower.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerGroupStatsHistPower.setStatus(_A)
_CfprPowerGroupStatsHistPowerAvg_Type=Integer32
_CfprPowerGroupStatsHistPowerAvg_Object=MibTableColumn
cfprPowerGroupStatsHistPowerAvg=_CfprPowerGroupStatsHistPowerAvg_Object((1,3,6,1,4,1,9,9,826,1,64,8,1,7),_CfprPowerGroupStatsHistPowerAvg_Type())
cfprPowerGroupStatsHistPowerAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerGroupStatsHistPowerAvg.setStatus(_A)
_CfprPowerGroupStatsHistPowerMax_Type=Integer32
_CfprPowerGroupStatsHistPowerMax_Object=MibTableColumn
cfprPowerGroupStatsHistPowerMax=_CfprPowerGroupStatsHistPowerMax_Object((1,3,6,1,4,1,9,9,826,1,64,8,1,8),_CfprPowerGroupStatsHistPowerMax_Type())
cfprPowerGroupStatsHistPowerMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerGroupStatsHistPowerMax.setStatus(_A)
_CfprPowerGroupStatsHistPowerMin_Type=Integer32
_CfprPowerGroupStatsHistPowerMin_Object=MibTableColumn
cfprPowerGroupStatsHistPowerMin=_CfprPowerGroupStatsHistPowerMin_Object((1,3,6,1,4,1,9,9,826,1,64,8,1,9),_CfprPowerGroupStatsHistPowerMin_Type())
cfprPowerGroupStatsHistPowerMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerGroupStatsHistPowerMin.setStatus(_A)
_CfprPowerGroupStatsHistSuspect_Type=TruthValue
_CfprPowerGroupStatsHistSuspect_Object=MibTableColumn
cfprPowerGroupStatsHistSuspect=_CfprPowerGroupStatsHistSuspect_Object((1,3,6,1,4,1,9,9,826,1,64,8,1,10),_CfprPowerGroupStatsHistSuspect_Type())
cfprPowerGroupStatsHistSuspect.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerGroupStatsHistSuspect.setStatus(_A)
_CfprPowerGroupStatsHistThresholded_Type=CfprPowerGroupStatsHistThresholded
_CfprPowerGroupStatsHistThresholded_Object=MibTableColumn
cfprPowerGroupStatsHistThresholded=_CfprPowerGroupStatsHistThresholded_Object((1,3,6,1,4,1,9,9,826,1,64,8,1,11),_CfprPowerGroupStatsHistThresholded_Type())
cfprPowerGroupStatsHistThresholded.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerGroupStatsHistThresholded.setStatus(_A)
_CfprPowerGroupStatsHistTimeCollected_Type=DateAndTime
_CfprPowerGroupStatsHistTimeCollected_Object=MibTableColumn
cfprPowerGroupStatsHistTimeCollected=_CfprPowerGroupStatsHistTimeCollected_Object((1,3,6,1,4,1,9,9,826,1,64,8,1,12),_CfprPowerGroupStatsHistTimeCollected_Type())
cfprPowerGroupStatsHistTimeCollected.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerGroupStatsHistTimeCollected.setStatus(_A)
_CfprPowerMgmtPolicyTable_Object=MibTable
cfprPowerMgmtPolicyTable=_CfprPowerMgmtPolicyTable_Object((1,3,6,1,4,1,9,9,826,1,64,9))
if mibBuilder.loadTexts:cfprPowerMgmtPolicyTable.setStatus(_A)
_CfprPowerMgmtPolicyEntry_Object=MibTableRow
cfprPowerMgmtPolicyEntry=_CfprPowerMgmtPolicyEntry_Object((1,3,6,1,4,1,9,9,826,1,64,9,1))
cfprPowerMgmtPolicyEntry.setIndexNames((0,_C,_M))
if mibBuilder.loadTexts:cfprPowerMgmtPolicyEntry.setStatus(_A)
_CfprPowerMgmtPolicyInstanceId_Type=CfprManagedObjectId
_CfprPowerMgmtPolicyInstanceId_Object=MibTableColumn
cfprPowerMgmtPolicyInstanceId=_CfprPowerMgmtPolicyInstanceId_Object((1,3,6,1,4,1,9,9,826,1,64,9,1,1),_CfprPowerMgmtPolicyInstanceId_Type())
cfprPowerMgmtPolicyInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprPowerMgmtPolicyInstanceId.setStatus(_A)
_CfprPowerMgmtPolicyDn_Type=CfprManagedObjectDn
_CfprPowerMgmtPolicyDn_Object=MibTableColumn
cfprPowerMgmtPolicyDn=_CfprPowerMgmtPolicyDn_Object((1,3,6,1,4,1,9,9,826,1,64,9,1,2),_CfprPowerMgmtPolicyDn_Type())
cfprPowerMgmtPolicyDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerMgmtPolicyDn.setStatus(_A)
_CfprPowerMgmtPolicyRn_Type=SnmpAdminString
_CfprPowerMgmtPolicyRn_Object=MibTableColumn
cfprPowerMgmtPolicyRn=_CfprPowerMgmtPolicyRn_Object((1,3,6,1,4,1,9,9,826,1,64,9,1,3),_CfprPowerMgmtPolicyRn_Type())
cfprPowerMgmtPolicyRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerMgmtPolicyRn.setStatus(_A)
_CfprPowerMgmtPolicyDescr_Type=SnmpAdminString
_CfprPowerMgmtPolicyDescr_Object=MibTableColumn
cfprPowerMgmtPolicyDescr=_CfprPowerMgmtPolicyDescr_Object((1,3,6,1,4,1,9,9,826,1,64,9,1,4),_CfprPowerMgmtPolicyDescr_Type())
cfprPowerMgmtPolicyDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerMgmtPolicyDescr.setStatus(_A)
_CfprPowerMgmtPolicyIntId_Type=SnmpAdminString
_CfprPowerMgmtPolicyIntId_Object=MibTableColumn
cfprPowerMgmtPolicyIntId=_CfprPowerMgmtPolicyIntId_Object((1,3,6,1,4,1,9,9,826,1,64,9,1,5),_CfprPowerMgmtPolicyIntId_Type())
cfprPowerMgmtPolicyIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerMgmtPolicyIntId.setStatus(_A)
_CfprPowerMgmtPolicyName_Type=SnmpAdminString
_CfprPowerMgmtPolicyName_Object=MibTableColumn
cfprPowerMgmtPolicyName=_CfprPowerMgmtPolicyName_Object((1,3,6,1,4,1,9,9,826,1,64,9,1,6),_CfprPowerMgmtPolicyName_Type())
cfprPowerMgmtPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerMgmtPolicyName.setStatus(_A)
_CfprPowerMgmtPolicyPolicyLevel_Type=Gauge32
_CfprPowerMgmtPolicyPolicyLevel_Object=MibTableColumn
cfprPowerMgmtPolicyPolicyLevel=_CfprPowerMgmtPolicyPolicyLevel_Object((1,3,6,1,4,1,9,9,826,1,64,9,1,7),_CfprPowerMgmtPolicyPolicyLevel_Type())
cfprPowerMgmtPolicyPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerMgmtPolicyPolicyLevel.setStatus(_A)
_CfprPowerMgmtPolicyPolicyOwner_Type=CfprPolicyPolicyOwner
_CfprPowerMgmtPolicyPolicyOwner_Object=MibTableColumn
cfprPowerMgmtPolicyPolicyOwner=_CfprPowerMgmtPolicyPolicyOwner_Object((1,3,6,1,4,1,9,9,826,1,64,9,1,8),_CfprPowerMgmtPolicyPolicyOwner_Type())
cfprPowerMgmtPolicyPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerMgmtPolicyPolicyOwner.setStatus(_A)
_CfprPowerMgmtPolicyProfiling_Type=TruthValue
_CfprPowerMgmtPolicyProfiling_Object=MibTableColumn
cfprPowerMgmtPolicyProfiling=_CfprPowerMgmtPolicyProfiling_Object((1,3,6,1,4,1,9,9,826,1,64,9,1,9),_CfprPowerMgmtPolicyProfiling_Type())
cfprPowerMgmtPolicyProfiling.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerMgmtPolicyProfiling.setStatus(_A)
_CfprPowerMgmtPolicyStyle_Type=CfprPowerMgmtStyle
_CfprPowerMgmtPolicyStyle_Object=MibTableColumn
cfprPowerMgmtPolicyStyle=_CfprPowerMgmtPolicyStyle_Object((1,3,6,1,4,1,9,9,826,1,64,9,1,10),_CfprPowerMgmtPolicyStyle_Type())
cfprPowerMgmtPolicyStyle.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerMgmtPolicyStyle.setStatus(_A)
_CfprPowerPlacementTable_Object=MibTable
cfprPowerPlacementTable=_CfprPowerPlacementTable_Object((1,3,6,1,4,1,9,9,826,1,64,10))
if mibBuilder.loadTexts:cfprPowerPlacementTable.setStatus(_A)
_CfprPowerPlacementEntry_Object=MibTableRow
cfprPowerPlacementEntry=_CfprPowerPlacementEntry_Object((1,3,6,1,4,1,9,9,826,1,64,10,1))
cfprPowerPlacementEntry.setIndexNames((0,_C,_N))
if mibBuilder.loadTexts:cfprPowerPlacementEntry.setStatus(_A)
_CfprPowerPlacementInstanceId_Type=CfprManagedObjectId
_CfprPowerPlacementInstanceId_Object=MibTableColumn
cfprPowerPlacementInstanceId=_CfprPowerPlacementInstanceId_Object((1,3,6,1,4,1,9,9,826,1,64,10,1,1),_CfprPowerPlacementInstanceId_Type())
cfprPowerPlacementInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprPowerPlacementInstanceId.setStatus(_A)
_CfprPowerPlacementDn_Type=CfprManagedObjectDn
_CfprPowerPlacementDn_Object=MibTableColumn
cfprPowerPlacementDn=_CfprPowerPlacementDn_Object((1,3,6,1,4,1,9,9,826,1,64,10,1,2),_CfprPowerPlacementDn_Type())
cfprPowerPlacementDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerPlacementDn.setStatus(_A)
_CfprPowerPlacementRn_Type=SnmpAdminString
_CfprPowerPlacementRn_Object=MibTableColumn
cfprPowerPlacementRn=_CfprPowerPlacementRn_Object((1,3,6,1,4,1,9,9,826,1,64,10,1,3),_CfprPowerPlacementRn_Type())
cfprPowerPlacementRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerPlacementRn.setStatus(_A)
_CfprPowerPlacementDescr_Type=SnmpAdminString
_CfprPowerPlacementDescr_Object=MibTableColumn
cfprPowerPlacementDescr=_CfprPowerPlacementDescr_Object((1,3,6,1,4,1,9,9,826,1,64,10,1,4),_CfprPowerPlacementDescr_Type())
cfprPowerPlacementDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerPlacementDescr.setStatus(_A)
_CfprPowerPlacementIntId_Type=SnmpAdminString
_CfprPowerPlacementIntId_Object=MibTableColumn
cfprPowerPlacementIntId=_CfprPowerPlacementIntId_Object((1,3,6,1,4,1,9,9,826,1,64,10,1,5),_CfprPowerPlacementIntId_Type())
cfprPowerPlacementIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerPlacementIntId.setStatus(_A)
_CfprPowerPlacementName_Type=SnmpAdminString
_CfprPowerPlacementName_Object=MibTableColumn
cfprPowerPlacementName=_CfprPowerPlacementName_Object((1,3,6,1,4,1,9,9,826,1,64,10,1,6),_CfprPowerPlacementName_Type())
cfprPowerPlacementName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerPlacementName.setStatus(_A)
_CfprPowerPlacementPeerReqConflict_Type=CfprPowerReqConflict
_CfprPowerPlacementPeerReqConflict_Object=MibTableColumn
cfprPowerPlacementPeerReqConflict=_CfprPowerPlacementPeerReqConflict_Object((1,3,6,1,4,1,9,9,826,1,64,10,1,7),_CfprPowerPlacementPeerReqConflict_Type())
cfprPowerPlacementPeerReqConflict.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerPlacementPeerReqConflict.setStatus(_A)
_CfprPowerPlacementPgName_Type=SnmpAdminString
_CfprPowerPlacementPgName_Object=MibTableColumn
cfprPowerPlacementPgName=_CfprPowerPlacementPgName_Object((1,3,6,1,4,1,9,9,826,1,64,10,1,8),_CfprPowerPlacementPgName_Type())
cfprPowerPlacementPgName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerPlacementPgName.setStatus(_A)
_CfprPowerPlacementPolicyLevel_Type=Gauge32
_CfprPowerPlacementPolicyLevel_Object=MibTableColumn
cfprPowerPlacementPolicyLevel=_CfprPowerPlacementPolicyLevel_Object((1,3,6,1,4,1,9,9,826,1,64,10,1,9),_CfprPowerPlacementPolicyLevel_Type())
cfprPowerPlacementPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerPlacementPolicyLevel.setStatus(_A)
_CfprPowerPlacementPolicyOwner_Type=CfprPolicyPolicyOwner
_CfprPowerPlacementPolicyOwner_Object=MibTableColumn
cfprPowerPlacementPolicyOwner=_CfprPowerPlacementPolicyOwner_Object((1,3,6,1,4,1,9,9,826,1,64,10,1,10),_CfprPowerPlacementPolicyOwner_Type())
cfprPowerPlacementPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerPlacementPolicyOwner.setStatus(_A)
_CfprPowerPlacementPrioShare_Type=CfprPowerPrioritySharing
_CfprPowerPlacementPrioShare_Object=MibTableColumn
cfprPowerPlacementPrioShare=_CfprPowerPlacementPrioShare_Object((1,3,6,1,4,1,9,9,826,1,64,10,1,11),_CfprPowerPlacementPrioShare_Type())
cfprPowerPlacementPrioShare.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerPlacementPrioShare.setStatus(_A)
_CfprPowerPlacementSelfReqConflict_Type=CfprPowerReqConflict
_CfprPowerPlacementSelfReqConflict_Object=MibTableColumn
cfprPowerPlacementSelfReqConflict=_CfprPowerPlacementSelfReqConflict_Object((1,3,6,1,4,1,9,9,826,1,64,10,1,12),_CfprPowerPlacementSelfReqConflict_Type())
cfprPowerPlacementSelfReqConflict.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerPlacementSelfReqConflict.setStatus(_A)
_CfprPowerPolicyTable_Object=MibTable
cfprPowerPolicyTable=_CfprPowerPolicyTable_Object((1,3,6,1,4,1,9,9,826,1,64,11))
if mibBuilder.loadTexts:cfprPowerPolicyTable.setStatus(_A)
_CfprPowerPolicyEntry_Object=MibTableRow
cfprPowerPolicyEntry=_CfprPowerPolicyEntry_Object((1,3,6,1,4,1,9,9,826,1,64,11,1))
cfprPowerPolicyEntry.setIndexNames((0,_C,_O))
if mibBuilder.loadTexts:cfprPowerPolicyEntry.setStatus(_A)
_CfprPowerPolicyInstanceId_Type=CfprManagedObjectId
_CfprPowerPolicyInstanceId_Object=MibTableColumn
cfprPowerPolicyInstanceId=_CfprPowerPolicyInstanceId_Object((1,3,6,1,4,1,9,9,826,1,64,11,1,1),_CfprPowerPolicyInstanceId_Type())
cfprPowerPolicyInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprPowerPolicyInstanceId.setStatus(_A)
_CfprPowerPolicyDn_Type=CfprManagedObjectDn
_CfprPowerPolicyDn_Object=MibTableColumn
cfprPowerPolicyDn=_CfprPowerPolicyDn_Object((1,3,6,1,4,1,9,9,826,1,64,11,1,2),_CfprPowerPolicyDn_Type())
cfprPowerPolicyDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerPolicyDn.setStatus(_A)
_CfprPowerPolicyRn_Type=SnmpAdminString
_CfprPowerPolicyRn_Object=MibTableColumn
cfprPowerPolicyRn=_CfprPowerPolicyRn_Object((1,3,6,1,4,1,9,9,826,1,64,11,1,3),_CfprPowerPolicyRn_Type())
cfprPowerPolicyRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerPolicyRn.setStatus(_A)
_CfprPowerPolicyDescr_Type=SnmpAdminString
_CfprPowerPolicyDescr_Object=MibTableColumn
cfprPowerPolicyDescr=_CfprPowerPolicyDescr_Object((1,3,6,1,4,1,9,9,826,1,64,11,1,4),_CfprPowerPolicyDescr_Type())
cfprPowerPolicyDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerPolicyDescr.setStatus(_A)
_CfprPowerPolicyIntId_Type=SnmpAdminString
_CfprPowerPolicyIntId_Object=MibTableColumn
cfprPowerPolicyIntId=_CfprPowerPolicyIntId_Object((1,3,6,1,4,1,9,9,826,1,64,11,1,5),_CfprPowerPolicyIntId_Type())
cfprPowerPolicyIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerPolicyIntId.setStatus(_A)
_CfprPowerPolicyName_Type=SnmpAdminString
_CfprPowerPolicyName_Object=MibTableColumn
cfprPowerPolicyName=_CfprPowerPolicyName_Object((1,3,6,1,4,1,9,9,826,1,64,11,1,6),_CfprPowerPolicyName_Type())
cfprPowerPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerPolicyName.setStatus(_A)
_CfprPowerPolicyOperPrio_Type=Gauge32
_CfprPowerPolicyOperPrio_Object=MibTableColumn
cfprPowerPolicyOperPrio=_CfprPowerPolicyOperPrio_Object((1,3,6,1,4,1,9,9,826,1,64,11,1,7),_CfprPowerPolicyOperPrio_Type())
cfprPowerPolicyOperPrio.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerPolicyOperPrio.setStatus(_A)
_CfprPowerPolicyPolicyLevel_Type=Gauge32
_CfprPowerPolicyPolicyLevel_Object=MibTableColumn
cfprPowerPolicyPolicyLevel=_CfprPowerPolicyPolicyLevel_Object((1,3,6,1,4,1,9,9,826,1,64,11,1,8),_CfprPowerPolicyPolicyLevel_Type())
cfprPowerPolicyPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerPolicyPolicyLevel.setStatus(_A)
_CfprPowerPolicyPolicyOwner_Type=CfprPolicyPolicyOwner
_CfprPowerPolicyPolicyOwner_Object=MibTableColumn
cfprPowerPolicyPolicyOwner=_CfprPowerPolicyPolicyOwner_Object((1,3,6,1,4,1,9,9,826,1,64,11,1,9),_CfprPowerPolicyPolicyOwner_Type())
cfprPowerPolicyPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerPolicyPolicyOwner.setStatus(_A)
_CfprPowerPolicyPrio_Type=Gauge32
_CfprPowerPolicyPrio_Object=MibTableColumn
cfprPowerPolicyPrio=_CfprPowerPolicyPrio_Object((1,3,6,1,4,1,9,9,826,1,64,11,1,10),_CfprPowerPolicyPrio_Type())
cfprPowerPolicyPrio.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerPolicyPrio.setStatus(_A)
_CfprPowerPrioWghtTable_Object=MibTable
cfprPowerPrioWghtTable=_CfprPowerPrioWghtTable_Object((1,3,6,1,4,1,9,9,826,1,64,12))
if mibBuilder.loadTexts:cfprPowerPrioWghtTable.setStatus(_A)
_CfprPowerPrioWghtEntry_Object=MibTableRow
cfprPowerPrioWghtEntry=_CfprPowerPrioWghtEntry_Object((1,3,6,1,4,1,9,9,826,1,64,12,1))
cfprPowerPrioWghtEntry.setIndexNames((0,_C,_P))
if mibBuilder.loadTexts:cfprPowerPrioWghtEntry.setStatus(_A)
_CfprPowerPrioWghtInstanceId_Type=CfprManagedObjectId
_CfprPowerPrioWghtInstanceId_Object=MibTableColumn
cfprPowerPrioWghtInstanceId=_CfprPowerPrioWghtInstanceId_Object((1,3,6,1,4,1,9,9,826,1,64,12,1,1),_CfprPowerPrioWghtInstanceId_Type())
cfprPowerPrioWghtInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprPowerPrioWghtInstanceId.setStatus(_A)
_CfprPowerPrioWghtDn_Type=CfprManagedObjectDn
_CfprPowerPrioWghtDn_Object=MibTableColumn
cfprPowerPrioWghtDn=_CfprPowerPrioWghtDn_Object((1,3,6,1,4,1,9,9,826,1,64,12,1,2),_CfprPowerPrioWghtDn_Type())
cfprPowerPrioWghtDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerPrioWghtDn.setStatus(_A)
_CfprPowerPrioWghtRn_Type=SnmpAdminString
_CfprPowerPrioWghtRn_Object=MibTableColumn
cfprPowerPrioWghtRn=_CfprPowerPrioWghtRn_Object((1,3,6,1,4,1,9,9,826,1,64,12,1,3),_CfprPowerPrioWghtRn_Type())
cfprPowerPrioWghtRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerPrioWghtRn.setStatus(_A)
_CfprPowerPrioWghtPrio_Type=Gauge32
_CfprPowerPrioWghtPrio_Object=MibTableColumn
cfprPowerPrioWghtPrio=_CfprPowerPrioWghtPrio_Object((1,3,6,1,4,1,9,9,826,1,64,12,1,4),_CfprPowerPrioWghtPrio_Type())
cfprPowerPrioWghtPrio.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerPrioWghtPrio.setStatus(_A)
_CfprPowerPrioWghtWeight_Type=Gauge32
_CfprPowerPrioWghtWeight_Object=MibTableColumn
cfprPowerPrioWghtWeight=_CfprPowerPrioWghtWeight_Object((1,3,6,1,4,1,9,9,826,1,64,12,1,5),_CfprPowerPrioWghtWeight_Type())
cfprPowerPrioWghtWeight.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerPrioWghtWeight.setStatus(_A)
_CfprPowerProfiledPowerTable_Object=MibTable
cfprPowerProfiledPowerTable=_CfprPowerProfiledPowerTable_Object((1,3,6,1,4,1,9,9,826,1,64,13))
if mibBuilder.loadTexts:cfprPowerProfiledPowerTable.setStatus(_A)
_CfprPowerProfiledPowerEntry_Object=MibTableRow
cfprPowerProfiledPowerEntry=_CfprPowerProfiledPowerEntry_Object((1,3,6,1,4,1,9,9,826,1,64,13,1))
cfprPowerProfiledPowerEntry.setIndexNames((0,_C,_Q))
if mibBuilder.loadTexts:cfprPowerProfiledPowerEntry.setStatus(_A)
_CfprPowerProfiledPowerInstanceId_Type=CfprManagedObjectId
_CfprPowerProfiledPowerInstanceId_Object=MibTableColumn
cfprPowerProfiledPowerInstanceId=_CfprPowerProfiledPowerInstanceId_Object((1,3,6,1,4,1,9,9,826,1,64,13,1,1),_CfprPowerProfiledPowerInstanceId_Type())
cfprPowerProfiledPowerInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprPowerProfiledPowerInstanceId.setStatus(_A)
_CfprPowerProfiledPowerDn_Type=CfprManagedObjectDn
_CfprPowerProfiledPowerDn_Object=MibTableColumn
cfprPowerProfiledPowerDn=_CfprPowerProfiledPowerDn_Object((1,3,6,1,4,1,9,9,826,1,64,13,1,2),_CfprPowerProfiledPowerDn_Type())
cfprPowerProfiledPowerDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerProfiledPowerDn.setStatus(_A)
_CfprPowerProfiledPowerRn_Type=SnmpAdminString
_CfprPowerProfiledPowerRn_Object=MibTableColumn
cfprPowerProfiledPowerRn=_CfprPowerProfiledPowerRn_Object((1,3,6,1,4,1,9,9,826,1,64,13,1,3),_CfprPowerProfiledPowerRn_Type())
cfprPowerProfiledPowerRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerProfiledPowerRn.setStatus(_A)
_CfprPowerProfiledPowerAbsMinPostPower_Type=Gauge32
_CfprPowerProfiledPowerAbsMinPostPower_Object=MibTableColumn
cfprPowerProfiledPowerAbsMinPostPower=_CfprPowerProfiledPowerAbsMinPostPower_Object((1,3,6,1,4,1,9,9,826,1,64,13,1,4),_CfprPowerProfiledPowerAbsMinPostPower_Type())
cfprPowerProfiledPowerAbsMinPostPower.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerProfiledPowerAbsMinPostPower.setStatus(_A)
_CfprPowerProfiledPowerMaxAppPower_Type=Gauge32
_CfprPowerProfiledPowerMaxAppPower_Object=MibTableColumn
cfprPowerProfiledPowerMaxAppPower=_CfprPowerProfiledPowerMaxAppPower_Object((1,3,6,1,4,1,9,9,826,1,64,13,1,5),_CfprPowerProfiledPowerMaxAppPower_Type())
cfprPowerProfiledPowerMaxAppPower.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerProfiledPowerMaxAppPower.setStatus(_A)
_CfprPowerProfiledPowerMaxPostPower_Type=Gauge32
_CfprPowerProfiledPowerMaxPostPower_Object=MibTableColumn
cfprPowerProfiledPowerMaxPostPower=_CfprPowerProfiledPowerMaxPostPower_Object((1,3,6,1,4,1,9,9,826,1,64,13,1,6),_CfprPowerProfiledPowerMaxPostPower_Type())
cfprPowerProfiledPowerMaxPostPower.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerProfiledPowerMaxPostPower.setStatus(_A)
_CfprPowerProfiledPowerMinAppPower_Type=Gauge32
_CfprPowerProfiledPowerMinAppPower_Object=MibTableColumn
cfprPowerProfiledPowerMinAppPower=_CfprPowerProfiledPowerMinAppPower_Object((1,3,6,1,4,1,9,9,826,1,64,13,1,7),_CfprPowerProfiledPowerMinAppPower_Type())
cfprPowerProfiledPowerMinAppPower.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerProfiledPowerMinAppPower.setStatus(_A)
_CfprPowerProfiledPowerMinNormPostPower_Type=Gauge32
_CfprPowerProfiledPowerMinNormPostPower_Object=MibTableColumn
cfprPowerProfiledPowerMinNormPostPower=_CfprPowerProfiledPowerMinNormPostPower_Object((1,3,6,1,4,1,9,9,826,1,64,13,1,8),_CfprPowerProfiledPowerMinNormPostPower_Type())
cfprPowerProfiledPowerMinNormPostPower.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerProfiledPowerMinNormPostPower.setStatus(_A)
_CfprPowerProfiledPowerMinPostPower_Type=Gauge32
_CfprPowerProfiledPowerMinPostPower_Object=MibTableColumn
cfprPowerProfiledPowerMinPostPower=_CfprPowerProfiledPowerMinPostPower_Object((1,3,6,1,4,1,9,9,826,1,64,13,1,9),_CfprPowerProfiledPowerMinPostPower_Type())
cfprPowerProfiledPowerMinPostPower.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerProfiledPowerMinPostPower.setStatus(_A)
_CfprPowerProfiledPowerPreDiscoveryPower_Type=Gauge32
_CfprPowerProfiledPowerPreDiscoveryPower_Object=MibTableColumn
cfprPowerProfiledPowerPreDiscoveryPower=_CfprPowerProfiledPowerPreDiscoveryPower_Object((1,3,6,1,4,1,9,9,826,1,64,13,1,10),_CfprPowerProfiledPowerPreDiscoveryPower_Type())
cfprPowerProfiledPowerPreDiscoveryPower.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerProfiledPowerPreDiscoveryPower.setStatus(_A)
_CfprPowerProfiledPowerProfileRunTime_Type=Gauge32
_CfprPowerProfiledPowerProfileRunTime_Object=MibTableColumn
cfprPowerProfiledPowerProfileRunTime=_CfprPowerProfiledPowerProfileRunTime_Object((1,3,6,1,4,1,9,9,826,1,64,13,1,11),_CfprPowerProfiledPowerProfileRunTime_Type())
cfprPowerProfiledPowerProfileRunTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerProfiledPowerProfileRunTime.setStatus(_A)
_CfprPowerProfiledPowerProfiledBoot_Type=Gauge32
_CfprPowerProfiledPowerProfiledBoot_Object=MibTableColumn
cfprPowerProfiledPowerProfiledBoot=_CfprPowerProfiledPowerProfiledBoot_Object((1,3,6,1,4,1,9,9,826,1,64,13,1,12),_CfprPowerProfiledPowerProfiledBoot_Type())
cfprPowerProfiledPowerProfiledBoot.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerProfiledPowerProfiledBoot.setStatus(_A)
_CfprPowerProfiledPowerProfiledMax_Type=Gauge32
_CfprPowerProfiledPowerProfiledMax_Object=MibTableColumn
cfprPowerProfiledPowerProfiledMax=_CfprPowerProfiledPowerProfiledMax_Object((1,3,6,1,4,1,9,9,826,1,64,13,1,13),_CfprPowerProfiledPowerProfiledMax_Type())
cfprPowerProfiledPowerProfiledMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerProfiledPowerProfiledMax.setStatus(_A)
_CfprPowerProfiledPowerProfiledMin_Type=Gauge32
_CfprPowerProfiledPowerProfiledMin_Object=MibTableColumn
cfprPowerProfiledPowerProfiledMin=_CfprPowerProfiledPowerProfiledMin_Object((1,3,6,1,4,1,9,9,826,1,64,13,1,14),_CfprPowerProfiledPowerProfiledMin_Type())
cfprPowerProfiledPowerProfiledMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerProfiledPowerProfiledMin.setStatus(_A)
_CfprPowerProfiledPowerSkipProfiling_Type=TruthValue
_CfprPowerProfiledPowerSkipProfiling_Object=MibTableColumn
cfprPowerProfiledPowerSkipProfiling=_CfprPowerProfiledPowerSkipProfiling_Object((1,3,6,1,4,1,9,9,826,1,64,13,1,15),_CfprPowerProfiledPowerSkipProfiling_Type())
cfprPowerProfiledPowerSkipProfiling.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerProfiledPowerSkipProfiling.setStatus(_A)
_CfprPowerRackUnitMemberTable_Object=MibTable
cfprPowerRackUnitMemberTable=_CfprPowerRackUnitMemberTable_Object((1,3,6,1,4,1,9,9,826,1,64,14))
if mibBuilder.loadTexts:cfprPowerRackUnitMemberTable.setStatus(_A)
_CfprPowerRackUnitMemberEntry_Object=MibTableRow
cfprPowerRackUnitMemberEntry=_CfprPowerRackUnitMemberEntry_Object((1,3,6,1,4,1,9,9,826,1,64,14,1))
cfprPowerRackUnitMemberEntry.setIndexNames((0,_C,_R))
if mibBuilder.loadTexts:cfprPowerRackUnitMemberEntry.setStatus(_A)
_CfprPowerRackUnitMemberInstanceId_Type=CfprManagedObjectId
_CfprPowerRackUnitMemberInstanceId_Object=MibTableColumn
cfprPowerRackUnitMemberInstanceId=_CfprPowerRackUnitMemberInstanceId_Object((1,3,6,1,4,1,9,9,826,1,64,14,1,1),_CfprPowerRackUnitMemberInstanceId_Type())
cfprPowerRackUnitMemberInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprPowerRackUnitMemberInstanceId.setStatus(_A)
_CfprPowerRackUnitMemberDn_Type=CfprManagedObjectDn
_CfprPowerRackUnitMemberDn_Object=MibTableColumn
cfprPowerRackUnitMemberDn=_CfprPowerRackUnitMemberDn_Object((1,3,6,1,4,1,9,9,826,1,64,14,1,2),_CfprPowerRackUnitMemberDn_Type())
cfprPowerRackUnitMemberDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerRackUnitMemberDn.setStatus(_A)
_CfprPowerRackUnitMemberRn_Type=SnmpAdminString
_CfprPowerRackUnitMemberRn_Object=MibTableColumn
cfprPowerRackUnitMemberRn=_CfprPowerRackUnitMemberRn_Object((1,3,6,1,4,1,9,9,826,1,64,14,1,3),_CfprPowerRackUnitMemberRn_Type())
cfprPowerRackUnitMemberRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerRackUnitMemberRn.setStatus(_A)
_CfprPowerRackUnitMemberId_Type=Gauge32
_CfprPowerRackUnitMemberId_Object=MibTableColumn
cfprPowerRackUnitMemberId=_CfprPowerRackUnitMemberId_Object((1,3,6,1,4,1,9,9,826,1,64,14,1,4),_CfprPowerRackUnitMemberId_Type())
cfprPowerRackUnitMemberId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerRackUnitMemberId.setStatus(_A)
_CfprPowerRackUnitMemberOperState_Type=CfprPowerMemberState
_CfprPowerRackUnitMemberOperState_Object=MibTableColumn
cfprPowerRackUnitMemberOperState=_CfprPowerRackUnitMemberOperState_Object((1,3,6,1,4,1,9,9,826,1,64,14,1,5),_CfprPowerRackUnitMemberOperState_Type())
cfprPowerRackUnitMemberOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPowerRackUnitMemberOperState.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'cfprPowerObjects':cfprPowerObjects,'cfprPowerBudgetTable':cfprPowerBudgetTable,'cfprPowerBudgetEntry':cfprPowerBudgetEntry,_E:cfprPowerBudgetInstanceId,'cfprPowerBudgetDn':cfprPowerBudgetDn,'cfprPowerBudgetRn':cfprPowerBudgetRn,'cfprPowerBudgetAdminCommitted':cfprPowerBudgetAdminCommitted,'cfprPowerBudgetAdminFPLockState':cfprPowerBudgetAdminFPLockState,'cfprPowerBudgetAdminPeak':cfprPowerBudgetAdminPeak,'cfprPowerBudgetAdminPeakNew':cfprPowerBudgetAdminPeakNew,'cfprPowerBudgetBootPower':cfprPowerBudgetBootPower,'cfprPowerBudgetCapAction':cfprPowerBudgetCapAction,'cfprPowerBudgetCatalogPower':cfprPowerBudgetCatalogPower,'cfprPowerBudgetChRsrvdPower':cfprPowerBudgetChRsrvdPower,'cfprPowerBudgetCurrentPower':cfprPowerBudgetCurrentPower,'cfprPowerBudgetDynRealloc':cfprPowerBudgetDynRealloc,'cfprPowerBudgetGroupName':cfprPowerBudgetGroupName,'cfprPowerBudgetIdlePower':cfprPowerBudgetIdlePower,'cfprPowerBudgetMaxPower':cfprPowerBudgetMaxPower,'cfprPowerBudgetMinPower':cfprPowerBudgetMinPower,'cfprPowerBudgetOperCommitted':cfprPowerBudgetOperCommitted,'cfprPowerBudgetOperFPLockState':cfprPowerBudgetOperFPLockState,'cfprPowerBudgetOperMin':cfprPowerBudgetOperMin,'cfprPowerBudgetOperPeak':cfprPowerBudgetOperPeak,'cfprPowerBudgetOperProfMethod':cfprPowerBudgetOperProfMethod,'cfprPowerBudgetOperState':cfprPowerBudgetOperState,'cfprPowerBudgetPrio':cfprPowerBudgetPrio,'cfprPowerBudgetProfMethod':cfprPowerBudgetProfMethod,'cfprPowerBudgetProfiling':cfprPowerBudgetProfiling,'cfprPowerBudgetPsuCapacity':cfprPowerBudgetPsuCapacity,'cfprPowerBudgetPsuLineMode':cfprPowerBudgetPsuLineMode,'cfprPowerBudgetPsuState':cfprPowerBudgetPsuState,'cfprPowerBudgetScaledWt':cfprPowerBudgetScaledWt,'cfprPowerBudgetStyle':cfprPowerBudgetStyle,'cfprPowerBudgetUpdateTime':cfprPowerBudgetUpdateTime,'cfprPowerBudgetWeight':cfprPowerBudgetWeight,'cfprPowerChassisMemberTable':cfprPowerChassisMemberTable,'cfprPowerChassisMemberEntry':cfprPowerChassisMemberEntry,_F:cfprPowerChassisMemberInstanceId,'cfprPowerChassisMemberDn':cfprPowerChassisMemberDn,'cfprPowerChassisMemberRn':cfprPowerChassisMemberRn,'cfprPowerChassisMemberId':cfprPowerChassisMemberId,'cfprPowerChassisMemberOperState':cfprPowerChassisMemberOperState,'cfprPowerEpTable':cfprPowerEpTable,'cfprPowerEpEntry':cfprPowerEpEntry,_G:cfprPowerEpInstanceId,'cfprPowerEpDn':cfprPowerEpDn,'cfprPowerEpRn':cfprPowerEpRn,'cfprPowerGroupTable':cfprPowerGroupTable,'cfprPowerGroupEntry':cfprPowerGroupEntry,_H:cfprPowerGroupInstanceId,'cfprPowerGroupDn':cfprPowerGroupDn,'cfprPowerGroupRn':cfprPowerGroupRn,'cfprPowerGroupAdminCommitted':cfprPowerGroupAdminCommitted,'cfprPowerGroupAdminPeak':cfprPowerGroupAdminPeak,'cfprPowerGroupCurReqPower':cfprPowerGroupCurReqPower,'cfprPowerGroupCurrentPower':cfprPowerGroupCurrentPower,'cfprPowerGroupDescr':cfprPowerGroupDescr,'cfprPowerGroupFltAggr':cfprPowerGroupFltAggr,'cfprPowerGroupIntId':cfprPowerGroupIntId,'cfprPowerGroupMinReqPower':cfprPowerGroupMinReqPower,'cfprPowerGroupName':cfprPowerGroupName,'cfprPowerGroupOperCommitted':cfprPowerGroupOperCommitted,'cfprPowerGroupOperPeak':cfprPowerGroupOperPeak,'cfprPowerGroupOperState':cfprPowerGroupOperState,'cfprPowerGroupPolicyLevel':cfprPowerGroupPolicyLevel,'cfprPowerGroupPolicyOwner':cfprPowerGroupPolicyOwner,'cfprPowerGroupQualifier':cfprPowerGroupQualifier,'cfprPowerGroupRealloc':cfprPowerGroupRealloc,'cfprPowerGroupAdditionPolicyTable':cfprPowerGroupAdditionPolicyTable,'cfprPowerGroupAdditionPolicyEntry':cfprPowerGroupAdditionPolicyEntry,_I:cfprPowerGroupAdditionPolicyInstanceId,'cfprPowerGroupAdditionPolicyDn':cfprPowerGroupAdditionPolicyDn,'cfprPowerGroupAdditionPolicyRn':cfprPowerGroupAdditionPolicyRn,'cfprPowerGroupAdditionPolicyAction':cfprPowerGroupAdditionPolicyAction,'cfprPowerGroupAdditionPolicyDescr':cfprPowerGroupAdditionPolicyDescr,'cfprPowerGroupAdditionPolicyIntId':cfprPowerGroupAdditionPolicyIntId,'cfprPowerGroupAdditionPolicyName':cfprPowerGroupAdditionPolicyName,'cfprPowerGroupAdditionPolicyPolicyLevel':cfprPowerGroupAdditionPolicyPolicyLevel,'cfprPowerGroupAdditionPolicyPolicyOwner':cfprPowerGroupAdditionPolicyPolicyOwner,'cfprPowerGroupQualTable':cfprPowerGroupQualTable,'cfprPowerGroupQualEntry':cfprPowerGroupQualEntry,_J:cfprPowerGroupQualInstanceId,'cfprPowerGroupQualDn':cfprPowerGroupQualDn,'cfprPowerGroupQualRn':cfprPowerGroupQualRn,'cfprPowerGroupQualGroupName':cfprPowerGroupQualGroupName,'cfprPowerGroupStatsTable':cfprPowerGroupStatsTable,'cfprPowerGroupStatsEntry':cfprPowerGroupStatsEntry,_K:cfprPowerGroupStatsInstanceId,'cfprPowerGroupStatsDn':cfprPowerGroupStatsDn,'cfprPowerGroupStatsRn':cfprPowerGroupStatsRn,'cfprPowerGroupStatsIntervals':cfprPowerGroupStatsIntervals,'cfprPowerGroupStatsPower':cfprPowerGroupStatsPower,'cfprPowerGroupStatsPowerAvg':cfprPowerGroupStatsPowerAvg,'cfprPowerGroupStatsPowerMax':cfprPowerGroupStatsPowerMax,'cfprPowerGroupStatsPowerMin':cfprPowerGroupStatsPowerMin,'cfprPowerGroupStatsSuspect':cfprPowerGroupStatsSuspect,'cfprPowerGroupStatsThresholded':cfprPowerGroupStatsThresholded,'cfprPowerGroupStatsTimeCollected':cfprPowerGroupStatsTimeCollected,'cfprPowerGroupStatsUpdate':cfprPowerGroupStatsUpdate,'cfprPowerGroupStatsHistTable':cfprPowerGroupStatsHistTable,'cfprPowerGroupStatsHistEntry':cfprPowerGroupStatsHistEntry,_L:cfprPowerGroupStatsHistInstanceId,'cfprPowerGroupStatsHistDn':cfprPowerGroupStatsHistDn,'cfprPowerGroupStatsHistRn':cfprPowerGroupStatsHistRn,'cfprPowerGroupStatsHistId':cfprPowerGroupStatsHistId,'cfprPowerGroupStatsHistMostRecent':cfprPowerGroupStatsHistMostRecent,'cfprPowerGroupStatsHistPower':cfprPowerGroupStatsHistPower,'cfprPowerGroupStatsHistPowerAvg':cfprPowerGroupStatsHistPowerAvg,'cfprPowerGroupStatsHistPowerMax':cfprPowerGroupStatsHistPowerMax,'cfprPowerGroupStatsHistPowerMin':cfprPowerGroupStatsHistPowerMin,'cfprPowerGroupStatsHistSuspect':cfprPowerGroupStatsHistSuspect,'cfprPowerGroupStatsHistThresholded':cfprPowerGroupStatsHistThresholded,'cfprPowerGroupStatsHistTimeCollected':cfprPowerGroupStatsHistTimeCollected,'cfprPowerMgmtPolicyTable':cfprPowerMgmtPolicyTable,'cfprPowerMgmtPolicyEntry':cfprPowerMgmtPolicyEntry,_M:cfprPowerMgmtPolicyInstanceId,'cfprPowerMgmtPolicyDn':cfprPowerMgmtPolicyDn,'cfprPowerMgmtPolicyRn':cfprPowerMgmtPolicyRn,'cfprPowerMgmtPolicyDescr':cfprPowerMgmtPolicyDescr,'cfprPowerMgmtPolicyIntId':cfprPowerMgmtPolicyIntId,'cfprPowerMgmtPolicyName':cfprPowerMgmtPolicyName,'cfprPowerMgmtPolicyPolicyLevel':cfprPowerMgmtPolicyPolicyLevel,'cfprPowerMgmtPolicyPolicyOwner':cfprPowerMgmtPolicyPolicyOwner,'cfprPowerMgmtPolicyProfiling':cfprPowerMgmtPolicyProfiling,'cfprPowerMgmtPolicyStyle':cfprPowerMgmtPolicyStyle,'cfprPowerPlacementTable':cfprPowerPlacementTable,'cfprPowerPlacementEntry':cfprPowerPlacementEntry,_N:cfprPowerPlacementInstanceId,'cfprPowerPlacementDn':cfprPowerPlacementDn,'cfprPowerPlacementRn':cfprPowerPlacementRn,'cfprPowerPlacementDescr':cfprPowerPlacementDescr,'cfprPowerPlacementIntId':cfprPowerPlacementIntId,'cfprPowerPlacementName':cfprPowerPlacementName,'cfprPowerPlacementPeerReqConflict':cfprPowerPlacementPeerReqConflict,'cfprPowerPlacementPgName':cfprPowerPlacementPgName,'cfprPowerPlacementPolicyLevel':cfprPowerPlacementPolicyLevel,'cfprPowerPlacementPolicyOwner':cfprPowerPlacementPolicyOwner,'cfprPowerPlacementPrioShare':cfprPowerPlacementPrioShare,'cfprPowerPlacementSelfReqConflict':cfprPowerPlacementSelfReqConflict,'cfprPowerPolicyTable':cfprPowerPolicyTable,'cfprPowerPolicyEntry':cfprPowerPolicyEntry,_O:cfprPowerPolicyInstanceId,'cfprPowerPolicyDn':cfprPowerPolicyDn,'cfprPowerPolicyRn':cfprPowerPolicyRn,'cfprPowerPolicyDescr':cfprPowerPolicyDescr,'cfprPowerPolicyIntId':cfprPowerPolicyIntId,'cfprPowerPolicyName':cfprPowerPolicyName,'cfprPowerPolicyOperPrio':cfprPowerPolicyOperPrio,'cfprPowerPolicyPolicyLevel':cfprPowerPolicyPolicyLevel,'cfprPowerPolicyPolicyOwner':cfprPowerPolicyPolicyOwner,'cfprPowerPolicyPrio':cfprPowerPolicyPrio,'cfprPowerPrioWghtTable':cfprPowerPrioWghtTable,'cfprPowerPrioWghtEntry':cfprPowerPrioWghtEntry,_P:cfprPowerPrioWghtInstanceId,'cfprPowerPrioWghtDn':cfprPowerPrioWghtDn,'cfprPowerPrioWghtRn':cfprPowerPrioWghtRn,'cfprPowerPrioWghtPrio':cfprPowerPrioWghtPrio,'cfprPowerPrioWghtWeight':cfprPowerPrioWghtWeight,'cfprPowerProfiledPowerTable':cfprPowerProfiledPowerTable,'cfprPowerProfiledPowerEntry':cfprPowerProfiledPowerEntry,_Q:cfprPowerProfiledPowerInstanceId,'cfprPowerProfiledPowerDn':cfprPowerProfiledPowerDn,'cfprPowerProfiledPowerRn':cfprPowerProfiledPowerRn,'cfprPowerProfiledPowerAbsMinPostPower':cfprPowerProfiledPowerAbsMinPostPower,'cfprPowerProfiledPowerMaxAppPower':cfprPowerProfiledPowerMaxAppPower,'cfprPowerProfiledPowerMaxPostPower':cfprPowerProfiledPowerMaxPostPower,'cfprPowerProfiledPowerMinAppPower':cfprPowerProfiledPowerMinAppPower,'cfprPowerProfiledPowerMinNormPostPower':cfprPowerProfiledPowerMinNormPostPower,'cfprPowerProfiledPowerMinPostPower':cfprPowerProfiledPowerMinPostPower,'cfprPowerProfiledPowerPreDiscoveryPower':cfprPowerProfiledPowerPreDiscoveryPower,'cfprPowerProfiledPowerProfileRunTime':cfprPowerProfiledPowerProfileRunTime,'cfprPowerProfiledPowerProfiledBoot':cfprPowerProfiledPowerProfiledBoot,'cfprPowerProfiledPowerProfiledMax':cfprPowerProfiledPowerProfiledMax,'cfprPowerProfiledPowerProfiledMin':cfprPowerProfiledPowerProfiledMin,'cfprPowerProfiledPowerSkipProfiling':cfprPowerProfiledPowerSkipProfiling,'cfprPowerRackUnitMemberTable':cfprPowerRackUnitMemberTable,'cfprPowerRackUnitMemberEntry':cfprPowerRackUnitMemberEntry,_R:cfprPowerRackUnitMemberInstanceId,'cfprPowerRackUnitMemberDn':cfprPowerRackUnitMemberDn,'cfprPowerRackUnitMemberRn':cfprPowerRackUnitMemberRn,'cfprPowerRackUnitMemberId':cfprPowerRackUnitMemberId,'cfprPowerRackUnitMemberOperState':cfprPowerRackUnitMemberOperState})