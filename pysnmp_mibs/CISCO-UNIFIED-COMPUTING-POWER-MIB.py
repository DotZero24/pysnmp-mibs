_T='cucsPowerFexMemberInstanceId'
_S='cucsPowerFIMemberInstanceId'
_R='cucsPowerProfiledPowerInstanceId'
_Q='cucsPowerMgmtPolicyInstanceId'
_P='cucsPowerRackUnitMemberInstanceId'
_O='cucsPowerPrioWghtInstanceId'
_N='cucsPowerPolicyInstanceId'
_M='cucsPowerPlacementInstanceId'
_L='cucsPowerGroupStatsHistInstanceId'
_K='cucsPowerGroupStatsInstanceId'
_J='cucsPowerGroupQualInstanceId'
_I='cucsPowerGroupAdditionPolicyInstanceId'
_H='cucsPowerGroupInstanceId'
_G='cucsPowerEpInstanceId'
_F='cucsPowerChassisMemberInstanceId'
_E='cucsPowerBudgetInstanceId'
_D='not-accessible'
_C='CISCO-UNIFIED-COMPUTING-POWER-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CiscoAlarmSeverity,CiscoInetAddressMask,CiscoNetworkAddress,TimeIntervalSec,Unsigned64=mibBuilder.importSymbols('CISCO-TC','CiscoAlarmSeverity','CiscoInetAddressMask','CiscoNetworkAddress','TimeIntervalSec','Unsigned64')
CucsManagedObjectDn,CucsManagedObjectId,ciscoUnifiedComputingMIBObjects=mibBuilder.importSymbols('CISCO-UNIFIED-COMPUTING-MIB','CucsManagedObjectDn','CucsManagedObjectId','ciscoUnifiedComputingMIBObjects')
CucsNetworkSwitchId,CucsPolicyPolicyOwner,CucsPowerBudgetFanSpeed,CucsPowerCapAction,CucsPowerChThrAction,CucsPowerGroupState,CucsPowerGroupStatsHistThresholded,CucsPowerGroupStatsThresholded,CucsPowerLockState,CucsPowerMemberState,CucsPowerMgmtStyle,CucsPowerOperState,CucsPowerPolicyFanSpeed,CucsPowerPowerAvailState,CucsPowerPowerDeployState,CucsPowerPrioritySharing,CucsPowerProfilingMethod,CucsPowerPsuLineMode,CucsPowerPsuState,CucsPowerReallocation,CucsPowerReqConflict=mibBuilder.importSymbols('CISCO-UNIFIED-COMPUTING-TC-MIB','CucsNetworkSwitchId','CucsPolicyPolicyOwner','CucsPowerBudgetFanSpeed','CucsPowerCapAction','CucsPowerChThrAction','CucsPowerGroupState','CucsPowerGroupStatsHistThresholded','CucsPowerGroupStatsThresholded','CucsPowerLockState','CucsPowerMemberState','CucsPowerMgmtStyle','CucsPowerOperState','CucsPowerPolicyFanSpeed','CucsPowerPowerAvailState','CucsPowerPowerDeployState','CucsPowerPrioritySharing','CucsPowerProfilingMethod','CucsPowerPsuLineMode','CucsPowerPsuState','CucsPowerReallocation','CucsPowerReqConflict')
InetAddressIPv4,InetAddressIPv6=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressIPv4','InetAddressIPv6')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowPointer,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowPointer','TextualConvention','TimeInterval','TimeStamp','TruthValue')
cucsPowerObjects=ModuleIdentity((1,3,6,1,4,1,9,9,719,1,39))
_CucsPowerBudgetTable_Object=MibTable
cucsPowerBudgetTable=_CucsPowerBudgetTable_Object((1,3,6,1,4,1,9,9,719,1,39,1))
if mibBuilder.loadTexts:cucsPowerBudgetTable.setStatus(_A)
_CucsPowerBudgetEntry_Object=MibTableRow
cucsPowerBudgetEntry=_CucsPowerBudgetEntry_Object((1,3,6,1,4,1,9,9,719,1,39,1,1))
cucsPowerBudgetEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:cucsPowerBudgetEntry.setStatus(_A)
_CucsPowerBudgetInstanceId_Type=CucsManagedObjectId
_CucsPowerBudgetInstanceId_Object=MibTableColumn
cucsPowerBudgetInstanceId=_CucsPowerBudgetInstanceId_Object((1,3,6,1,4,1,9,9,719,1,39,1,1,1),_CucsPowerBudgetInstanceId_Type())
cucsPowerBudgetInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsPowerBudgetInstanceId.setStatus(_A)
_CucsPowerBudgetDn_Type=CucsManagedObjectDn
_CucsPowerBudgetDn_Object=MibTableColumn
cucsPowerBudgetDn=_CucsPowerBudgetDn_Object((1,3,6,1,4,1,9,9,719,1,39,1,1,2),_CucsPowerBudgetDn_Type())
cucsPowerBudgetDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerBudgetDn.setStatus(_A)
_CucsPowerBudgetRn_Type=SnmpAdminString
_CucsPowerBudgetRn_Object=MibTableColumn
cucsPowerBudgetRn=_CucsPowerBudgetRn_Object((1,3,6,1,4,1,9,9,719,1,39,1,1,3),_CucsPowerBudgetRn_Type())
cucsPowerBudgetRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerBudgetRn.setStatus(_A)
_CucsPowerBudgetAdminCommitted_Type=Gauge32
_CucsPowerBudgetAdminCommitted_Object=MibTableColumn
cucsPowerBudgetAdminCommitted=_CucsPowerBudgetAdminCommitted_Object((1,3,6,1,4,1,9,9,719,1,39,1,1,4),_CucsPowerBudgetAdminCommitted_Type())
cucsPowerBudgetAdminCommitted.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerBudgetAdminCommitted.setStatus(_A)
_CucsPowerBudgetAdminPeak_Type=Gauge32
_CucsPowerBudgetAdminPeak_Object=MibTableColumn
cucsPowerBudgetAdminPeak=_CucsPowerBudgetAdminPeak_Object((1,3,6,1,4,1,9,9,719,1,39,1,1,5),_CucsPowerBudgetAdminPeak_Type())
cucsPowerBudgetAdminPeak.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerBudgetAdminPeak.setStatus(_A)
_CucsPowerBudgetCurrentPower_Type=Gauge32
_CucsPowerBudgetCurrentPower_Object=MibTableColumn
cucsPowerBudgetCurrentPower=_CucsPowerBudgetCurrentPower_Object((1,3,6,1,4,1,9,9,719,1,39,1,1,6),_CucsPowerBudgetCurrentPower_Type())
cucsPowerBudgetCurrentPower.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerBudgetCurrentPower.setStatus(_A)
_CucsPowerBudgetGroupName_Type=SnmpAdminString
_CucsPowerBudgetGroupName_Object=MibTableColumn
cucsPowerBudgetGroupName=_CucsPowerBudgetGroupName_Object((1,3,6,1,4,1,9,9,719,1,39,1,1,7),_CucsPowerBudgetGroupName_Type())
cucsPowerBudgetGroupName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerBudgetGroupName.setStatus(_A)
_CucsPowerBudgetIdlePower_Type=Gauge32
_CucsPowerBudgetIdlePower_Object=MibTableColumn
cucsPowerBudgetIdlePower=_CucsPowerBudgetIdlePower_Object((1,3,6,1,4,1,9,9,719,1,39,1,1,8),_CucsPowerBudgetIdlePower_Type())
cucsPowerBudgetIdlePower.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerBudgetIdlePower.setStatus(_A)
_CucsPowerBudgetMaxPower_Type=Gauge32
_CucsPowerBudgetMaxPower_Object=MibTableColumn
cucsPowerBudgetMaxPower=_CucsPowerBudgetMaxPower_Object((1,3,6,1,4,1,9,9,719,1,39,1,1,9),_CucsPowerBudgetMaxPower_Type())
cucsPowerBudgetMaxPower.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerBudgetMaxPower.setStatus(_A)
_CucsPowerBudgetMinPower_Type=Gauge32
_CucsPowerBudgetMinPower_Object=MibTableColumn
cucsPowerBudgetMinPower=_CucsPowerBudgetMinPower_Object((1,3,6,1,4,1,9,9,719,1,39,1,1,10),_CucsPowerBudgetMinPower_Type())
cucsPowerBudgetMinPower.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerBudgetMinPower.setStatus(_A)
_CucsPowerBudgetOperCommitted_Type=Gauge32
_CucsPowerBudgetOperCommitted_Object=MibTableColumn
cucsPowerBudgetOperCommitted=_CucsPowerBudgetOperCommitted_Object((1,3,6,1,4,1,9,9,719,1,39,1,1,11),_CucsPowerBudgetOperCommitted_Type())
cucsPowerBudgetOperCommitted.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerBudgetOperCommitted.setStatus(_A)
_CucsPowerBudgetOperMin_Type=Gauge32
_CucsPowerBudgetOperMin_Object=MibTableColumn
cucsPowerBudgetOperMin=_CucsPowerBudgetOperMin_Object((1,3,6,1,4,1,9,9,719,1,39,1,1,12),_CucsPowerBudgetOperMin_Type())
cucsPowerBudgetOperMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerBudgetOperMin.setStatus(_A)
_CucsPowerBudgetOperPeak_Type=Gauge32
_CucsPowerBudgetOperPeak_Object=MibTableColumn
cucsPowerBudgetOperPeak=_CucsPowerBudgetOperPeak_Object((1,3,6,1,4,1,9,9,719,1,39,1,1,13),_CucsPowerBudgetOperPeak_Type())
cucsPowerBudgetOperPeak.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerBudgetOperPeak.setStatus(_A)
_CucsPowerBudgetScaledWt_Type=Gauge32
_CucsPowerBudgetScaledWt_Object=MibTableColumn
cucsPowerBudgetScaledWt=_CucsPowerBudgetScaledWt_Object((1,3,6,1,4,1,9,9,719,1,39,1,1,14),_CucsPowerBudgetScaledWt_Type())
cucsPowerBudgetScaledWt.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerBudgetScaledWt.setStatus(_A)
_CucsPowerBudgetOperState_Type=CucsPowerOperState
_CucsPowerBudgetOperState_Object=MibTableColumn
cucsPowerBudgetOperState=_CucsPowerBudgetOperState_Object((1,3,6,1,4,1,9,9,719,1,39,1,1,15),_CucsPowerBudgetOperState_Type())
cucsPowerBudgetOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerBudgetOperState.setStatus(_A)
_CucsPowerBudgetDynRealloc_Type=CucsPowerReallocation
_CucsPowerBudgetDynRealloc_Object=MibTableColumn
cucsPowerBudgetDynRealloc=_CucsPowerBudgetDynRealloc_Object((1,3,6,1,4,1,9,9,719,1,39,1,1,16),_CucsPowerBudgetDynRealloc_Type())
cucsPowerBudgetDynRealloc.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerBudgetDynRealloc.setStatus(_A)
_CucsPowerBudgetPrio_Type=Gauge32
_CucsPowerBudgetPrio_Object=MibTableColumn
cucsPowerBudgetPrio=_CucsPowerBudgetPrio_Object((1,3,6,1,4,1,9,9,719,1,39,1,1,17),_CucsPowerBudgetPrio_Type())
cucsPowerBudgetPrio.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerBudgetPrio.setStatus(_A)
_CucsPowerBudgetCatalogPower_Type=Gauge32
_CucsPowerBudgetCatalogPower_Object=MibTableColumn
cucsPowerBudgetCatalogPower=_CucsPowerBudgetCatalogPower_Object((1,3,6,1,4,1,9,9,719,1,39,1,1,18),_CucsPowerBudgetCatalogPower_Type())
cucsPowerBudgetCatalogPower.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerBudgetCatalogPower.setStatus(_A)
_CucsPowerBudgetUpdateTime_Type=DateAndTime
_CucsPowerBudgetUpdateTime_Object=MibTableColumn
cucsPowerBudgetUpdateTime=_CucsPowerBudgetUpdateTime_Object((1,3,6,1,4,1,9,9,719,1,39,1,1,19),_CucsPowerBudgetUpdateTime_Type())
cucsPowerBudgetUpdateTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerBudgetUpdateTime.setStatus(_A)
_CucsPowerBudgetCapAction_Type=CucsPowerCapAction
_CucsPowerBudgetCapAction_Object=MibTableColumn
cucsPowerBudgetCapAction=_CucsPowerBudgetCapAction_Object((1,3,6,1,4,1,9,9,719,1,39,1,1,20),_CucsPowerBudgetCapAction_Type())
cucsPowerBudgetCapAction.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerBudgetCapAction.setStatus(_A)
_CucsPowerBudgetWeight_Type=Gauge32
_CucsPowerBudgetWeight_Object=MibTableColumn
cucsPowerBudgetWeight=_CucsPowerBudgetWeight_Object((1,3,6,1,4,1,9,9,719,1,39,1,1,21),_CucsPowerBudgetWeight_Type())
cucsPowerBudgetWeight.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerBudgetWeight.setStatus(_A)
_CucsPowerBudgetPsuCapacity_Type=Gauge32
_CucsPowerBudgetPsuCapacity_Object=MibTableColumn
cucsPowerBudgetPsuCapacity=_CucsPowerBudgetPsuCapacity_Object((1,3,6,1,4,1,9,9,719,1,39,1,1,22),_CucsPowerBudgetPsuCapacity_Type())
cucsPowerBudgetPsuCapacity.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerBudgetPsuCapacity.setStatus(_A)
_CucsPowerBudgetPsuState_Type=CucsPowerPsuState
_CucsPowerBudgetPsuState_Object=MibTableColumn
cucsPowerBudgetPsuState=_CucsPowerBudgetPsuState_Object((1,3,6,1,4,1,9,9,719,1,39,1,1,23),_CucsPowerBudgetPsuState_Type())
cucsPowerBudgetPsuState.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerBudgetPsuState.setStatus(_A)
_CucsPowerBudgetStyle_Type=CucsPowerMgmtStyle
_CucsPowerBudgetStyle_Object=MibTableColumn
cucsPowerBudgetStyle=_CucsPowerBudgetStyle_Object((1,3,6,1,4,1,9,9,719,1,39,1,1,24),_CucsPowerBudgetStyle_Type())
cucsPowerBudgetStyle.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerBudgetStyle.setStatus(_A)
_CucsPowerBudgetAdminFPLockState_Type=CucsPowerLockState
_CucsPowerBudgetAdminFPLockState_Object=MibTableColumn
cucsPowerBudgetAdminFPLockState=_CucsPowerBudgetAdminFPLockState_Object((1,3,6,1,4,1,9,9,719,1,39,1,1,25),_CucsPowerBudgetAdminFPLockState_Type())
cucsPowerBudgetAdminFPLockState.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerBudgetAdminFPLockState.setStatus(_A)
_CucsPowerBudgetAdminPeakNew_Type=Gauge32
_CucsPowerBudgetAdminPeakNew_Object=MibTableColumn
cucsPowerBudgetAdminPeakNew=_CucsPowerBudgetAdminPeakNew_Object((1,3,6,1,4,1,9,9,719,1,39,1,1,26),_CucsPowerBudgetAdminPeakNew_Type())
cucsPowerBudgetAdminPeakNew.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerBudgetAdminPeakNew.setStatus(_A)
_CucsPowerBudgetBootPower_Type=Gauge32
_CucsPowerBudgetBootPower_Object=MibTableColumn
cucsPowerBudgetBootPower=_CucsPowerBudgetBootPower_Object((1,3,6,1,4,1,9,9,719,1,39,1,1,27),_CucsPowerBudgetBootPower_Type())
cucsPowerBudgetBootPower.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerBudgetBootPower.setStatus(_A)
_CucsPowerBudgetChRsrvdPower_Type=Gauge32
_CucsPowerBudgetChRsrvdPower_Object=MibTableColumn
cucsPowerBudgetChRsrvdPower=_CucsPowerBudgetChRsrvdPower_Object((1,3,6,1,4,1,9,9,719,1,39,1,1,28),_CucsPowerBudgetChRsrvdPower_Type())
cucsPowerBudgetChRsrvdPower.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerBudgetChRsrvdPower.setStatus(_A)
_CucsPowerBudgetOperFPLockState_Type=CucsPowerLockState
_CucsPowerBudgetOperFPLockState_Object=MibTableColumn
cucsPowerBudgetOperFPLockState=_CucsPowerBudgetOperFPLockState_Object((1,3,6,1,4,1,9,9,719,1,39,1,1,29),_CucsPowerBudgetOperFPLockState_Type())
cucsPowerBudgetOperFPLockState.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerBudgetOperFPLockState.setStatus(_A)
_CucsPowerBudgetOperProfMethod_Type=CucsPowerProfilingMethod
_CucsPowerBudgetOperProfMethod_Object=MibTableColumn
cucsPowerBudgetOperProfMethod=_CucsPowerBudgetOperProfMethod_Object((1,3,6,1,4,1,9,9,719,1,39,1,1,30),_CucsPowerBudgetOperProfMethod_Type())
cucsPowerBudgetOperProfMethod.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerBudgetOperProfMethod.setStatus(_A)
_CucsPowerBudgetProfMethod_Type=CucsPowerProfilingMethod
_CucsPowerBudgetProfMethod_Object=MibTableColumn
cucsPowerBudgetProfMethod=_CucsPowerBudgetProfMethod_Object((1,3,6,1,4,1,9,9,719,1,39,1,1,31),_CucsPowerBudgetProfMethod_Type())
cucsPowerBudgetProfMethod.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerBudgetProfMethod.setStatus(_A)
_CucsPowerBudgetProfiling_Type=TruthValue
_CucsPowerBudgetProfiling_Object=MibTableColumn
cucsPowerBudgetProfiling=_CucsPowerBudgetProfiling_Object((1,3,6,1,4,1,9,9,719,1,39,1,1,32),_CucsPowerBudgetProfiling_Type())
cucsPowerBudgetProfiling.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerBudgetProfiling.setStatus(_A)
_CucsPowerBudgetPsuLineMode_Type=CucsPowerPsuLineMode
_CucsPowerBudgetPsuLineMode_Object=MibTableColumn
cucsPowerBudgetPsuLineMode=_CucsPowerBudgetPsuLineMode_Object((1,3,6,1,4,1,9,9,719,1,39,1,1,33),_CucsPowerBudgetPsuLineMode_Type())
cucsPowerBudgetPsuLineMode.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerBudgetPsuLineMode.setStatus(_A)
_CucsPowerBudgetPowerAvailState_Type=CucsPowerPowerAvailState
_CucsPowerBudgetPowerAvailState_Object=MibTableColumn
cucsPowerBudgetPowerAvailState=_CucsPowerBudgetPowerAvailState_Object((1,3,6,1,4,1,9,9,719,1,39,1,1,34),_CucsPowerBudgetPowerAvailState_Type())
cucsPowerBudgetPowerAvailState.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerBudgetPowerAvailState.setStatus(_A)
_CucsPowerBudgetPowerDeployState_Type=CucsPowerPowerDeployState
_CucsPowerBudgetPowerDeployState_Object=MibTableColumn
cucsPowerBudgetPowerDeployState=_CucsPowerBudgetPowerDeployState_Object((1,3,6,1,4,1,9,9,719,1,39,1,1,35),_CucsPowerBudgetPowerDeployState_Type())
cucsPowerBudgetPowerDeployState.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerBudgetPowerDeployState.setStatus(_A)
_CucsPowerBudgetPowerOnDeploy_Type=TruthValue
_CucsPowerBudgetPowerOnDeploy_Object=MibTableColumn
cucsPowerBudgetPowerOnDeploy=_CucsPowerBudgetPowerOnDeploy_Object((1,3,6,1,4,1,9,9,719,1,39,1,1,36),_CucsPowerBudgetPowerOnDeploy_Type())
cucsPowerBudgetPowerOnDeploy.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerBudgetPowerOnDeploy.setStatus(_A)
_CucsPowerBudgetFanSpeed_Type=CucsPowerBudgetFanSpeed
_CucsPowerBudgetFanSpeed_Object=MibTableColumn
cucsPowerBudgetFanSpeed=_CucsPowerBudgetFanSpeed_Object((1,3,6,1,4,1,9,9,719,1,39,1,1,37),_CucsPowerBudgetFanSpeed_Type())
cucsPowerBudgetFanSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerBudgetFanSpeed.setStatus(_A)
_CucsPowerBudgetPowerCapSupportEnabled_Type=TruthValue
_CucsPowerBudgetPowerCapSupportEnabled_Object=MibTableColumn
cucsPowerBudgetPowerCapSupportEnabled=_CucsPowerBudgetPowerCapSupportEnabled_Object((1,3,6,1,4,1,9,9,719,1,39,1,1,38),_CucsPowerBudgetPowerCapSupportEnabled_Type())
cucsPowerBudgetPowerCapSupportEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerBudgetPowerCapSupportEnabled.setStatus(_A)
_CucsPowerChassisMemberTable_Object=MibTable
cucsPowerChassisMemberTable=_CucsPowerChassisMemberTable_Object((1,3,6,1,4,1,9,9,719,1,39,2))
if mibBuilder.loadTexts:cucsPowerChassisMemberTable.setStatus(_A)
_CucsPowerChassisMemberEntry_Object=MibTableRow
cucsPowerChassisMemberEntry=_CucsPowerChassisMemberEntry_Object((1,3,6,1,4,1,9,9,719,1,39,2,1))
cucsPowerChassisMemberEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:cucsPowerChassisMemberEntry.setStatus(_A)
_CucsPowerChassisMemberInstanceId_Type=CucsManagedObjectId
_CucsPowerChassisMemberInstanceId_Object=MibTableColumn
cucsPowerChassisMemberInstanceId=_CucsPowerChassisMemberInstanceId_Object((1,3,6,1,4,1,9,9,719,1,39,2,1,1),_CucsPowerChassisMemberInstanceId_Type())
cucsPowerChassisMemberInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsPowerChassisMemberInstanceId.setStatus(_A)
_CucsPowerChassisMemberDn_Type=CucsManagedObjectDn
_CucsPowerChassisMemberDn_Object=MibTableColumn
cucsPowerChassisMemberDn=_CucsPowerChassisMemberDn_Object((1,3,6,1,4,1,9,9,719,1,39,2,1,2),_CucsPowerChassisMemberDn_Type())
cucsPowerChassisMemberDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerChassisMemberDn.setStatus(_A)
_CucsPowerChassisMemberRn_Type=SnmpAdminString
_CucsPowerChassisMemberRn_Object=MibTableColumn
cucsPowerChassisMemberRn=_CucsPowerChassisMemberRn_Object((1,3,6,1,4,1,9,9,719,1,39,2,1,3),_CucsPowerChassisMemberRn_Type())
cucsPowerChassisMemberRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerChassisMemberRn.setStatus(_A)
_CucsPowerChassisMemberId_Type=Gauge32
_CucsPowerChassisMemberId_Object=MibTableColumn
cucsPowerChassisMemberId=_CucsPowerChassisMemberId_Object((1,3,6,1,4,1,9,9,719,1,39,2,1,4),_CucsPowerChassisMemberId_Type())
cucsPowerChassisMemberId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerChassisMemberId.setStatus(_A)
_CucsPowerChassisMemberOperState_Type=CucsPowerMemberState
_CucsPowerChassisMemberOperState_Object=MibTableColumn
cucsPowerChassisMemberOperState=_CucsPowerChassisMemberOperState_Object((1,3,6,1,4,1,9,9,719,1,39,2,1,5),_CucsPowerChassisMemberOperState_Type())
cucsPowerChassisMemberOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerChassisMemberOperState.setStatus(_A)
_CucsPowerEpTable_Object=MibTable
cucsPowerEpTable=_CucsPowerEpTable_Object((1,3,6,1,4,1,9,9,719,1,39,3))
if mibBuilder.loadTexts:cucsPowerEpTable.setStatus(_A)
_CucsPowerEpEntry_Object=MibTableRow
cucsPowerEpEntry=_CucsPowerEpEntry_Object((1,3,6,1,4,1,9,9,719,1,39,3,1))
cucsPowerEpEntry.setIndexNames((0,_C,_G))
if mibBuilder.loadTexts:cucsPowerEpEntry.setStatus(_A)
_CucsPowerEpInstanceId_Type=CucsManagedObjectId
_CucsPowerEpInstanceId_Object=MibTableColumn
cucsPowerEpInstanceId=_CucsPowerEpInstanceId_Object((1,3,6,1,4,1,9,9,719,1,39,3,1,1),_CucsPowerEpInstanceId_Type())
cucsPowerEpInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsPowerEpInstanceId.setStatus(_A)
_CucsPowerEpDn_Type=CucsManagedObjectDn
_CucsPowerEpDn_Object=MibTableColumn
cucsPowerEpDn=_CucsPowerEpDn_Object((1,3,6,1,4,1,9,9,719,1,39,3,1,2),_CucsPowerEpDn_Type())
cucsPowerEpDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerEpDn.setStatus(_A)
_CucsPowerEpRn_Type=SnmpAdminString
_CucsPowerEpRn_Object=MibTableColumn
cucsPowerEpRn=_CucsPowerEpRn_Object((1,3,6,1,4,1,9,9,719,1,39,3,1,3),_CucsPowerEpRn_Type())
cucsPowerEpRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerEpRn.setStatus(_A)
_CucsPowerGroupTable_Object=MibTable
cucsPowerGroupTable=_CucsPowerGroupTable_Object((1,3,6,1,4,1,9,9,719,1,39,4))
if mibBuilder.loadTexts:cucsPowerGroupTable.setStatus(_A)
_CucsPowerGroupEntry_Object=MibTableRow
cucsPowerGroupEntry=_CucsPowerGroupEntry_Object((1,3,6,1,4,1,9,9,719,1,39,4,1))
cucsPowerGroupEntry.setIndexNames((0,_C,_H))
if mibBuilder.loadTexts:cucsPowerGroupEntry.setStatus(_A)
_CucsPowerGroupInstanceId_Type=CucsManagedObjectId
_CucsPowerGroupInstanceId_Object=MibTableColumn
cucsPowerGroupInstanceId=_CucsPowerGroupInstanceId_Object((1,3,6,1,4,1,9,9,719,1,39,4,1,1),_CucsPowerGroupInstanceId_Type())
cucsPowerGroupInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsPowerGroupInstanceId.setStatus(_A)
_CucsPowerGroupDn_Type=CucsManagedObjectDn
_CucsPowerGroupDn_Object=MibTableColumn
cucsPowerGroupDn=_CucsPowerGroupDn_Object((1,3,6,1,4,1,9,9,719,1,39,4,1,2),_CucsPowerGroupDn_Type())
cucsPowerGroupDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerGroupDn.setStatus(_A)
_CucsPowerGroupRn_Type=SnmpAdminString
_CucsPowerGroupRn_Object=MibTableColumn
cucsPowerGroupRn=_CucsPowerGroupRn_Object((1,3,6,1,4,1,9,9,719,1,39,4,1,3),_CucsPowerGroupRn_Type())
cucsPowerGroupRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerGroupRn.setStatus(_A)
_CucsPowerGroupRealloc_Type=CucsPowerReallocation
_CucsPowerGroupRealloc_Object=MibTableColumn
cucsPowerGroupRealloc=_CucsPowerGroupRealloc_Object((1,3,6,1,4,1,9,9,719,1,39,4,1,4),_CucsPowerGroupRealloc_Type())
cucsPowerGroupRealloc.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerGroupRealloc.setStatus(_A)
_CucsPowerGroupAdminCommitted_Type=Gauge32
_CucsPowerGroupAdminCommitted_Object=MibTableColumn
cucsPowerGroupAdminCommitted=_CucsPowerGroupAdminCommitted_Object((1,3,6,1,4,1,9,9,719,1,39,4,1,5),_CucsPowerGroupAdminCommitted_Type())
cucsPowerGroupAdminCommitted.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerGroupAdminCommitted.setStatus(_A)
_CucsPowerGroupAdminPeak_Type=Gauge32
_CucsPowerGroupAdminPeak_Object=MibTableColumn
cucsPowerGroupAdminPeak=_CucsPowerGroupAdminPeak_Object((1,3,6,1,4,1,9,9,719,1,39,4,1,6),_CucsPowerGroupAdminPeak_Type())
cucsPowerGroupAdminPeak.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerGroupAdminPeak.setStatus(_A)
_CucsPowerGroupCurrentPower_Type=Gauge32
_CucsPowerGroupCurrentPower_Object=MibTableColumn
cucsPowerGroupCurrentPower=_CucsPowerGroupCurrentPower_Object((1,3,6,1,4,1,9,9,719,1,39,4,1,7),_CucsPowerGroupCurrentPower_Type())
cucsPowerGroupCurrentPower.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerGroupCurrentPower.setStatus(_A)
_CucsPowerGroupDescr_Type=SnmpAdminString
_CucsPowerGroupDescr_Object=MibTableColumn
cucsPowerGroupDescr=_CucsPowerGroupDescr_Object((1,3,6,1,4,1,9,9,719,1,39,4,1,8),_CucsPowerGroupDescr_Type())
cucsPowerGroupDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerGroupDescr.setStatus(_A)
_CucsPowerGroupFltAggr_Type=Unsigned64
_CucsPowerGroupFltAggr_Object=MibTableColumn
cucsPowerGroupFltAggr=_CucsPowerGroupFltAggr_Object((1,3,6,1,4,1,9,9,719,1,39,4,1,9),_CucsPowerGroupFltAggr_Type())
cucsPowerGroupFltAggr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerGroupFltAggr.setStatus(_A)
_CucsPowerGroupCurReqPower_Type=Gauge32
_CucsPowerGroupCurReqPower_Object=MibTableColumn
cucsPowerGroupCurReqPower=_CucsPowerGroupCurReqPower_Object((1,3,6,1,4,1,9,9,719,1,39,4,1,10),_CucsPowerGroupCurReqPower_Type())
cucsPowerGroupCurReqPower.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerGroupCurReqPower.setStatus(_A)
_CucsPowerGroupMinReqPower_Type=Gauge32
_CucsPowerGroupMinReqPower_Object=MibTableColumn
cucsPowerGroupMinReqPower=_CucsPowerGroupMinReqPower_Object((1,3,6,1,4,1,9,9,719,1,39,4,1,11),_CucsPowerGroupMinReqPower_Type())
cucsPowerGroupMinReqPower.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerGroupMinReqPower.setStatus(_A)
_CucsPowerGroupIntId_Type=SnmpAdminString
_CucsPowerGroupIntId_Object=MibTableColumn
cucsPowerGroupIntId=_CucsPowerGroupIntId_Object((1,3,6,1,4,1,9,9,719,1,39,4,1,12),_CucsPowerGroupIntId_Type())
cucsPowerGroupIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerGroupIntId.setStatus(_A)
_CucsPowerGroupName_Type=SnmpAdminString
_CucsPowerGroupName_Object=MibTableColumn
cucsPowerGroupName=_CucsPowerGroupName_Object((1,3,6,1,4,1,9,9,719,1,39,4,1,13),_CucsPowerGroupName_Type())
cucsPowerGroupName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerGroupName.setStatus(_A)
_CucsPowerGroupQualifier_Type=SnmpAdminString
_CucsPowerGroupQualifier_Object=MibTableColumn
cucsPowerGroupQualifier=_CucsPowerGroupQualifier_Object((1,3,6,1,4,1,9,9,719,1,39,4,1,14),_CucsPowerGroupQualifier_Type())
cucsPowerGroupQualifier.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerGroupQualifier.setStatus(_A)
_CucsPowerGroupOperCommitted_Type=Gauge32
_CucsPowerGroupOperCommitted_Object=MibTableColumn
cucsPowerGroupOperCommitted=_CucsPowerGroupOperCommitted_Object((1,3,6,1,4,1,9,9,719,1,39,4,1,15),_CucsPowerGroupOperCommitted_Type())
cucsPowerGroupOperCommitted.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerGroupOperCommitted.setStatus(_A)
_CucsPowerGroupOperPeak_Type=Gauge32
_CucsPowerGroupOperPeak_Object=MibTableColumn
cucsPowerGroupOperPeak=_CucsPowerGroupOperPeak_Object((1,3,6,1,4,1,9,9,719,1,39,4,1,16),_CucsPowerGroupOperPeak_Type())
cucsPowerGroupOperPeak.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerGroupOperPeak.setStatus(_A)
_CucsPowerGroupOperState_Type=CucsPowerGroupState
_CucsPowerGroupOperState_Object=MibTableColumn
cucsPowerGroupOperState=_CucsPowerGroupOperState_Object((1,3,6,1,4,1,9,9,719,1,39,4,1,17),_CucsPowerGroupOperState_Type())
cucsPowerGroupOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerGroupOperState.setStatus(_A)
_CucsPowerGroupPolicyLevel_Type=Gauge32
_CucsPowerGroupPolicyLevel_Object=MibTableColumn
cucsPowerGroupPolicyLevel=_CucsPowerGroupPolicyLevel_Object((1,3,6,1,4,1,9,9,719,1,39,4,1,18),_CucsPowerGroupPolicyLevel_Type())
cucsPowerGroupPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerGroupPolicyLevel.setStatus(_A)
_CucsPowerGroupPolicyOwner_Type=CucsPolicyPolicyOwner
_CucsPowerGroupPolicyOwner_Object=MibTableColumn
cucsPowerGroupPolicyOwner=_CucsPowerGroupPolicyOwner_Object((1,3,6,1,4,1,9,9,719,1,39,4,1,19),_CucsPowerGroupPolicyOwner_Type())
cucsPowerGroupPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerGroupPolicyOwner.setStatus(_A)
_CucsPowerGroupMaxReqPower_Type=Gauge32
_CucsPowerGroupMaxReqPower_Object=MibTableColumn
cucsPowerGroupMaxReqPower=_CucsPowerGroupMaxReqPower_Object((1,3,6,1,4,1,9,9,719,1,39,4,1,20),_CucsPowerGroupMaxReqPower_Type())
cucsPowerGroupMaxReqPower.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerGroupMaxReqPower.setStatus(_A)
_CucsPowerGroupAdditionPolicyTable_Object=MibTable
cucsPowerGroupAdditionPolicyTable=_CucsPowerGroupAdditionPolicyTable_Object((1,3,6,1,4,1,9,9,719,1,39,5))
if mibBuilder.loadTexts:cucsPowerGroupAdditionPolicyTable.setStatus(_A)
_CucsPowerGroupAdditionPolicyEntry_Object=MibTableRow
cucsPowerGroupAdditionPolicyEntry=_CucsPowerGroupAdditionPolicyEntry_Object((1,3,6,1,4,1,9,9,719,1,39,5,1))
cucsPowerGroupAdditionPolicyEntry.setIndexNames((0,_C,_I))
if mibBuilder.loadTexts:cucsPowerGroupAdditionPolicyEntry.setStatus(_A)
_CucsPowerGroupAdditionPolicyInstanceId_Type=CucsManagedObjectId
_CucsPowerGroupAdditionPolicyInstanceId_Object=MibTableColumn
cucsPowerGroupAdditionPolicyInstanceId=_CucsPowerGroupAdditionPolicyInstanceId_Object((1,3,6,1,4,1,9,9,719,1,39,5,1,1),_CucsPowerGroupAdditionPolicyInstanceId_Type())
cucsPowerGroupAdditionPolicyInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsPowerGroupAdditionPolicyInstanceId.setStatus(_A)
_CucsPowerGroupAdditionPolicyDn_Type=CucsManagedObjectDn
_CucsPowerGroupAdditionPolicyDn_Object=MibTableColumn
cucsPowerGroupAdditionPolicyDn=_CucsPowerGroupAdditionPolicyDn_Object((1,3,6,1,4,1,9,9,719,1,39,5,1,2),_CucsPowerGroupAdditionPolicyDn_Type())
cucsPowerGroupAdditionPolicyDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerGroupAdditionPolicyDn.setStatus(_A)
_CucsPowerGroupAdditionPolicyRn_Type=SnmpAdminString
_CucsPowerGroupAdditionPolicyRn_Object=MibTableColumn
cucsPowerGroupAdditionPolicyRn=_CucsPowerGroupAdditionPolicyRn_Object((1,3,6,1,4,1,9,9,719,1,39,5,1,3),_CucsPowerGroupAdditionPolicyRn_Type())
cucsPowerGroupAdditionPolicyRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerGroupAdditionPolicyRn.setStatus(_A)
_CucsPowerGroupAdditionPolicyAction_Type=CucsPowerChThrAction
_CucsPowerGroupAdditionPolicyAction_Object=MibTableColumn
cucsPowerGroupAdditionPolicyAction=_CucsPowerGroupAdditionPolicyAction_Object((1,3,6,1,4,1,9,9,719,1,39,5,1,4),_CucsPowerGroupAdditionPolicyAction_Type())
cucsPowerGroupAdditionPolicyAction.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerGroupAdditionPolicyAction.setStatus(_A)
_CucsPowerGroupAdditionPolicyDescr_Type=SnmpAdminString
_CucsPowerGroupAdditionPolicyDescr_Object=MibTableColumn
cucsPowerGroupAdditionPolicyDescr=_CucsPowerGroupAdditionPolicyDescr_Object((1,3,6,1,4,1,9,9,719,1,39,5,1,5),_CucsPowerGroupAdditionPolicyDescr_Type())
cucsPowerGroupAdditionPolicyDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerGroupAdditionPolicyDescr.setStatus(_A)
_CucsPowerGroupAdditionPolicyIntId_Type=SnmpAdminString
_CucsPowerGroupAdditionPolicyIntId_Object=MibTableColumn
cucsPowerGroupAdditionPolicyIntId=_CucsPowerGroupAdditionPolicyIntId_Object((1,3,6,1,4,1,9,9,719,1,39,5,1,6),_CucsPowerGroupAdditionPolicyIntId_Type())
cucsPowerGroupAdditionPolicyIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerGroupAdditionPolicyIntId.setStatus(_A)
_CucsPowerGroupAdditionPolicyName_Type=SnmpAdminString
_CucsPowerGroupAdditionPolicyName_Object=MibTableColumn
cucsPowerGroupAdditionPolicyName=_CucsPowerGroupAdditionPolicyName_Object((1,3,6,1,4,1,9,9,719,1,39,5,1,7),_CucsPowerGroupAdditionPolicyName_Type())
cucsPowerGroupAdditionPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerGroupAdditionPolicyName.setStatus(_A)
_CucsPowerGroupAdditionPolicyPolicyLevel_Type=Gauge32
_CucsPowerGroupAdditionPolicyPolicyLevel_Object=MibTableColumn
cucsPowerGroupAdditionPolicyPolicyLevel=_CucsPowerGroupAdditionPolicyPolicyLevel_Object((1,3,6,1,4,1,9,9,719,1,39,5,1,8),_CucsPowerGroupAdditionPolicyPolicyLevel_Type())
cucsPowerGroupAdditionPolicyPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerGroupAdditionPolicyPolicyLevel.setStatus(_A)
_CucsPowerGroupAdditionPolicyPolicyOwner_Type=CucsPolicyPolicyOwner
_CucsPowerGroupAdditionPolicyPolicyOwner_Object=MibTableColumn
cucsPowerGroupAdditionPolicyPolicyOwner=_CucsPowerGroupAdditionPolicyPolicyOwner_Object((1,3,6,1,4,1,9,9,719,1,39,5,1,9),_CucsPowerGroupAdditionPolicyPolicyOwner_Type())
cucsPowerGroupAdditionPolicyPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerGroupAdditionPolicyPolicyOwner.setStatus(_A)
_CucsPowerGroupQualTable_Object=MibTable
cucsPowerGroupQualTable=_CucsPowerGroupQualTable_Object((1,3,6,1,4,1,9,9,719,1,39,6))
if mibBuilder.loadTexts:cucsPowerGroupQualTable.setStatus(_A)
_CucsPowerGroupQualEntry_Object=MibTableRow
cucsPowerGroupQualEntry=_CucsPowerGroupQualEntry_Object((1,3,6,1,4,1,9,9,719,1,39,6,1))
cucsPowerGroupQualEntry.setIndexNames((0,_C,_J))
if mibBuilder.loadTexts:cucsPowerGroupQualEntry.setStatus(_A)
_CucsPowerGroupQualInstanceId_Type=CucsManagedObjectId
_CucsPowerGroupQualInstanceId_Object=MibTableColumn
cucsPowerGroupQualInstanceId=_CucsPowerGroupQualInstanceId_Object((1,3,6,1,4,1,9,9,719,1,39,6,1,1),_CucsPowerGroupQualInstanceId_Type())
cucsPowerGroupQualInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsPowerGroupQualInstanceId.setStatus(_A)
_CucsPowerGroupQualDn_Type=CucsManagedObjectDn
_CucsPowerGroupQualDn_Object=MibTableColumn
cucsPowerGroupQualDn=_CucsPowerGroupQualDn_Object((1,3,6,1,4,1,9,9,719,1,39,6,1,2),_CucsPowerGroupQualDn_Type())
cucsPowerGroupQualDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerGroupQualDn.setStatus(_A)
_CucsPowerGroupQualRn_Type=SnmpAdminString
_CucsPowerGroupQualRn_Object=MibTableColumn
cucsPowerGroupQualRn=_CucsPowerGroupQualRn_Object((1,3,6,1,4,1,9,9,719,1,39,6,1,3),_CucsPowerGroupQualRn_Type())
cucsPowerGroupQualRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerGroupQualRn.setStatus(_A)
_CucsPowerGroupQualGroupName_Type=SnmpAdminString
_CucsPowerGroupQualGroupName_Object=MibTableColumn
cucsPowerGroupQualGroupName=_CucsPowerGroupQualGroupName_Object((1,3,6,1,4,1,9,9,719,1,39,6,1,4),_CucsPowerGroupQualGroupName_Type())
cucsPowerGroupQualGroupName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerGroupQualGroupName.setStatus(_A)
_CucsPowerGroupStatsTable_Object=MibTable
cucsPowerGroupStatsTable=_CucsPowerGroupStatsTable_Object((1,3,6,1,4,1,9,9,719,1,39,7))
if mibBuilder.loadTexts:cucsPowerGroupStatsTable.setStatus(_A)
_CucsPowerGroupStatsEntry_Object=MibTableRow
cucsPowerGroupStatsEntry=_CucsPowerGroupStatsEntry_Object((1,3,6,1,4,1,9,9,719,1,39,7,1))
cucsPowerGroupStatsEntry.setIndexNames((0,_C,_K))
if mibBuilder.loadTexts:cucsPowerGroupStatsEntry.setStatus(_A)
_CucsPowerGroupStatsInstanceId_Type=CucsManagedObjectId
_CucsPowerGroupStatsInstanceId_Object=MibTableColumn
cucsPowerGroupStatsInstanceId=_CucsPowerGroupStatsInstanceId_Object((1,3,6,1,4,1,9,9,719,1,39,7,1,1),_CucsPowerGroupStatsInstanceId_Type())
cucsPowerGroupStatsInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsPowerGroupStatsInstanceId.setStatus(_A)
_CucsPowerGroupStatsDn_Type=CucsManagedObjectDn
_CucsPowerGroupStatsDn_Object=MibTableColumn
cucsPowerGroupStatsDn=_CucsPowerGroupStatsDn_Object((1,3,6,1,4,1,9,9,719,1,39,7,1,2),_CucsPowerGroupStatsDn_Type())
cucsPowerGroupStatsDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerGroupStatsDn.setStatus(_A)
_CucsPowerGroupStatsRn_Type=SnmpAdminString
_CucsPowerGroupStatsRn_Object=MibTableColumn
cucsPowerGroupStatsRn=_CucsPowerGroupStatsRn_Object((1,3,6,1,4,1,9,9,719,1,39,7,1,3),_CucsPowerGroupStatsRn_Type())
cucsPowerGroupStatsRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerGroupStatsRn.setStatus(_A)
_CucsPowerGroupStatsIntervals_Type=Gauge32
_CucsPowerGroupStatsIntervals_Object=MibTableColumn
cucsPowerGroupStatsIntervals=_CucsPowerGroupStatsIntervals_Object((1,3,6,1,4,1,9,9,719,1,39,7,1,4),_CucsPowerGroupStatsIntervals_Type())
cucsPowerGroupStatsIntervals.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerGroupStatsIntervals.setStatus(_A)
_CucsPowerGroupStatsPower_Type=Integer32
_CucsPowerGroupStatsPower_Object=MibTableColumn
cucsPowerGroupStatsPower=_CucsPowerGroupStatsPower_Object((1,3,6,1,4,1,9,9,719,1,39,7,1,5),_CucsPowerGroupStatsPower_Type())
cucsPowerGroupStatsPower.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerGroupStatsPower.setStatus(_A)
_CucsPowerGroupStatsPowerAvg_Type=Integer32
_CucsPowerGroupStatsPowerAvg_Object=MibTableColumn
cucsPowerGroupStatsPowerAvg=_CucsPowerGroupStatsPowerAvg_Object((1,3,6,1,4,1,9,9,719,1,39,7,1,6),_CucsPowerGroupStatsPowerAvg_Type())
cucsPowerGroupStatsPowerAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerGroupStatsPowerAvg.setStatus(_A)
_CucsPowerGroupStatsPowerMax_Type=Integer32
_CucsPowerGroupStatsPowerMax_Object=MibTableColumn
cucsPowerGroupStatsPowerMax=_CucsPowerGroupStatsPowerMax_Object((1,3,6,1,4,1,9,9,719,1,39,7,1,7),_CucsPowerGroupStatsPowerMax_Type())
cucsPowerGroupStatsPowerMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerGroupStatsPowerMax.setStatus(_A)
_CucsPowerGroupStatsPowerMin_Type=Integer32
_CucsPowerGroupStatsPowerMin_Object=MibTableColumn
cucsPowerGroupStatsPowerMin=_CucsPowerGroupStatsPowerMin_Object((1,3,6,1,4,1,9,9,719,1,39,7,1,8),_CucsPowerGroupStatsPowerMin_Type())
cucsPowerGroupStatsPowerMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerGroupStatsPowerMin.setStatus(_A)
_CucsPowerGroupStatsSuspect_Type=TruthValue
_CucsPowerGroupStatsSuspect_Object=MibTableColumn
cucsPowerGroupStatsSuspect=_CucsPowerGroupStatsSuspect_Object((1,3,6,1,4,1,9,9,719,1,39,7,1,9),_CucsPowerGroupStatsSuspect_Type())
cucsPowerGroupStatsSuspect.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerGroupStatsSuspect.setStatus(_A)
_CucsPowerGroupStatsThresholded_Type=CucsPowerGroupStatsThresholded
_CucsPowerGroupStatsThresholded_Object=MibTableColumn
cucsPowerGroupStatsThresholded=_CucsPowerGroupStatsThresholded_Object((1,3,6,1,4,1,9,9,719,1,39,7,1,10),_CucsPowerGroupStatsThresholded_Type())
cucsPowerGroupStatsThresholded.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerGroupStatsThresholded.setStatus(_A)
_CucsPowerGroupStatsTimeCollected_Type=DateAndTime
_CucsPowerGroupStatsTimeCollected_Object=MibTableColumn
cucsPowerGroupStatsTimeCollected=_CucsPowerGroupStatsTimeCollected_Object((1,3,6,1,4,1,9,9,719,1,39,7,1,11),_CucsPowerGroupStatsTimeCollected_Type())
cucsPowerGroupStatsTimeCollected.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerGroupStatsTimeCollected.setStatus(_A)
_CucsPowerGroupStatsUpdate_Type=Gauge32
_CucsPowerGroupStatsUpdate_Object=MibTableColumn
cucsPowerGroupStatsUpdate=_CucsPowerGroupStatsUpdate_Object((1,3,6,1,4,1,9,9,719,1,39,7,1,12),_CucsPowerGroupStatsUpdate_Type())
cucsPowerGroupStatsUpdate.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerGroupStatsUpdate.setStatus(_A)
_CucsPowerGroupStatsHistTable_Object=MibTable
cucsPowerGroupStatsHistTable=_CucsPowerGroupStatsHistTable_Object((1,3,6,1,4,1,9,9,719,1,39,8))
if mibBuilder.loadTexts:cucsPowerGroupStatsHistTable.setStatus(_A)
_CucsPowerGroupStatsHistEntry_Object=MibTableRow
cucsPowerGroupStatsHistEntry=_CucsPowerGroupStatsHistEntry_Object((1,3,6,1,4,1,9,9,719,1,39,8,1))
cucsPowerGroupStatsHistEntry.setIndexNames((0,_C,_L))
if mibBuilder.loadTexts:cucsPowerGroupStatsHistEntry.setStatus(_A)
_CucsPowerGroupStatsHistInstanceId_Type=CucsManagedObjectId
_CucsPowerGroupStatsHistInstanceId_Object=MibTableColumn
cucsPowerGroupStatsHistInstanceId=_CucsPowerGroupStatsHistInstanceId_Object((1,3,6,1,4,1,9,9,719,1,39,8,1,1),_CucsPowerGroupStatsHistInstanceId_Type())
cucsPowerGroupStatsHistInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsPowerGroupStatsHistInstanceId.setStatus(_A)
_CucsPowerGroupStatsHistDn_Type=CucsManagedObjectDn
_CucsPowerGroupStatsHistDn_Object=MibTableColumn
cucsPowerGroupStatsHistDn=_CucsPowerGroupStatsHistDn_Object((1,3,6,1,4,1,9,9,719,1,39,8,1,2),_CucsPowerGroupStatsHistDn_Type())
cucsPowerGroupStatsHistDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerGroupStatsHistDn.setStatus(_A)
_CucsPowerGroupStatsHistRn_Type=SnmpAdminString
_CucsPowerGroupStatsHistRn_Object=MibTableColumn
cucsPowerGroupStatsHistRn=_CucsPowerGroupStatsHistRn_Object((1,3,6,1,4,1,9,9,719,1,39,8,1,3),_CucsPowerGroupStatsHistRn_Type())
cucsPowerGroupStatsHistRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerGroupStatsHistRn.setStatus(_A)
_CucsPowerGroupStatsHistId_Type=Unsigned64
_CucsPowerGroupStatsHistId_Object=MibTableColumn
cucsPowerGroupStatsHistId=_CucsPowerGroupStatsHistId_Object((1,3,6,1,4,1,9,9,719,1,39,8,1,4),_CucsPowerGroupStatsHistId_Type())
cucsPowerGroupStatsHistId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerGroupStatsHistId.setStatus(_A)
_CucsPowerGroupStatsHistMostRecent_Type=TruthValue
_CucsPowerGroupStatsHistMostRecent_Object=MibTableColumn
cucsPowerGroupStatsHistMostRecent=_CucsPowerGroupStatsHistMostRecent_Object((1,3,6,1,4,1,9,9,719,1,39,8,1,5),_CucsPowerGroupStatsHistMostRecent_Type())
cucsPowerGroupStatsHistMostRecent.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerGroupStatsHistMostRecent.setStatus(_A)
_CucsPowerGroupStatsHistPower_Type=Integer32
_CucsPowerGroupStatsHistPower_Object=MibTableColumn
cucsPowerGroupStatsHistPower=_CucsPowerGroupStatsHistPower_Object((1,3,6,1,4,1,9,9,719,1,39,8,1,6),_CucsPowerGroupStatsHistPower_Type())
cucsPowerGroupStatsHistPower.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerGroupStatsHistPower.setStatus(_A)
_CucsPowerGroupStatsHistPowerAvg_Type=Integer32
_CucsPowerGroupStatsHistPowerAvg_Object=MibTableColumn
cucsPowerGroupStatsHistPowerAvg=_CucsPowerGroupStatsHistPowerAvg_Object((1,3,6,1,4,1,9,9,719,1,39,8,1,7),_CucsPowerGroupStatsHistPowerAvg_Type())
cucsPowerGroupStatsHistPowerAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerGroupStatsHistPowerAvg.setStatus(_A)
_CucsPowerGroupStatsHistPowerMax_Type=Integer32
_CucsPowerGroupStatsHistPowerMax_Object=MibTableColumn
cucsPowerGroupStatsHistPowerMax=_CucsPowerGroupStatsHistPowerMax_Object((1,3,6,1,4,1,9,9,719,1,39,8,1,8),_CucsPowerGroupStatsHistPowerMax_Type())
cucsPowerGroupStatsHistPowerMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerGroupStatsHistPowerMax.setStatus(_A)
_CucsPowerGroupStatsHistPowerMin_Type=Integer32
_CucsPowerGroupStatsHistPowerMin_Object=MibTableColumn
cucsPowerGroupStatsHistPowerMin=_CucsPowerGroupStatsHistPowerMin_Object((1,3,6,1,4,1,9,9,719,1,39,8,1,9),_CucsPowerGroupStatsHistPowerMin_Type())
cucsPowerGroupStatsHistPowerMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerGroupStatsHistPowerMin.setStatus(_A)
_CucsPowerGroupStatsHistSuspect_Type=TruthValue
_CucsPowerGroupStatsHistSuspect_Object=MibTableColumn
cucsPowerGroupStatsHistSuspect=_CucsPowerGroupStatsHistSuspect_Object((1,3,6,1,4,1,9,9,719,1,39,8,1,10),_CucsPowerGroupStatsHistSuspect_Type())
cucsPowerGroupStatsHistSuspect.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerGroupStatsHistSuspect.setStatus(_A)
_CucsPowerGroupStatsHistThresholded_Type=CucsPowerGroupStatsHistThresholded
_CucsPowerGroupStatsHistThresholded_Object=MibTableColumn
cucsPowerGroupStatsHistThresholded=_CucsPowerGroupStatsHistThresholded_Object((1,3,6,1,4,1,9,9,719,1,39,8,1,11),_CucsPowerGroupStatsHistThresholded_Type())
cucsPowerGroupStatsHistThresholded.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerGroupStatsHistThresholded.setStatus(_A)
_CucsPowerGroupStatsHistTimeCollected_Type=DateAndTime
_CucsPowerGroupStatsHistTimeCollected_Object=MibTableColumn
cucsPowerGroupStatsHistTimeCollected=_CucsPowerGroupStatsHistTimeCollected_Object((1,3,6,1,4,1,9,9,719,1,39,8,1,12),_CucsPowerGroupStatsHistTimeCollected_Type())
cucsPowerGroupStatsHistTimeCollected.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerGroupStatsHistTimeCollected.setStatus(_A)
_CucsPowerPlacementTable_Object=MibTable
cucsPowerPlacementTable=_CucsPowerPlacementTable_Object((1,3,6,1,4,1,9,9,719,1,39,9))
if mibBuilder.loadTexts:cucsPowerPlacementTable.setStatus(_A)
_CucsPowerPlacementEntry_Object=MibTableRow
cucsPowerPlacementEntry=_CucsPowerPlacementEntry_Object((1,3,6,1,4,1,9,9,719,1,39,9,1))
cucsPowerPlacementEntry.setIndexNames((0,_C,_M))
if mibBuilder.loadTexts:cucsPowerPlacementEntry.setStatus(_A)
_CucsPowerPlacementInstanceId_Type=CucsManagedObjectId
_CucsPowerPlacementInstanceId_Object=MibTableColumn
cucsPowerPlacementInstanceId=_CucsPowerPlacementInstanceId_Object((1,3,6,1,4,1,9,9,719,1,39,9,1,1),_CucsPowerPlacementInstanceId_Type())
cucsPowerPlacementInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsPowerPlacementInstanceId.setStatus(_A)
_CucsPowerPlacementDn_Type=CucsManagedObjectDn
_CucsPowerPlacementDn_Object=MibTableColumn
cucsPowerPlacementDn=_CucsPowerPlacementDn_Object((1,3,6,1,4,1,9,9,719,1,39,9,1,2),_CucsPowerPlacementDn_Type())
cucsPowerPlacementDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerPlacementDn.setStatus(_A)
_CucsPowerPlacementRn_Type=SnmpAdminString
_CucsPowerPlacementRn_Object=MibTableColumn
cucsPowerPlacementRn=_CucsPowerPlacementRn_Object((1,3,6,1,4,1,9,9,719,1,39,9,1,3),_CucsPowerPlacementRn_Type())
cucsPowerPlacementRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerPlacementRn.setStatus(_A)
_CucsPowerPlacementDescr_Type=SnmpAdminString
_CucsPowerPlacementDescr_Object=MibTableColumn
cucsPowerPlacementDescr=_CucsPowerPlacementDescr_Object((1,3,6,1,4,1,9,9,719,1,39,9,1,4),_CucsPowerPlacementDescr_Type())
cucsPowerPlacementDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerPlacementDescr.setStatus(_A)
_CucsPowerPlacementIntId_Type=SnmpAdminString
_CucsPowerPlacementIntId_Object=MibTableColumn
cucsPowerPlacementIntId=_CucsPowerPlacementIntId_Object((1,3,6,1,4,1,9,9,719,1,39,9,1,5),_CucsPowerPlacementIntId_Type())
cucsPowerPlacementIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerPlacementIntId.setStatus(_A)
_CucsPowerPlacementName_Type=SnmpAdminString
_CucsPowerPlacementName_Object=MibTableColumn
cucsPowerPlacementName=_CucsPowerPlacementName_Object((1,3,6,1,4,1,9,9,719,1,39,9,1,6),_CucsPowerPlacementName_Type())
cucsPowerPlacementName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerPlacementName.setStatus(_A)
_CucsPowerPlacementPeerReqConflict_Type=CucsPowerReqConflict
_CucsPowerPlacementPeerReqConflict_Object=MibTableColumn
cucsPowerPlacementPeerReqConflict=_CucsPowerPlacementPeerReqConflict_Object((1,3,6,1,4,1,9,9,719,1,39,9,1,7),_CucsPowerPlacementPeerReqConflict_Type())
cucsPowerPlacementPeerReqConflict.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerPlacementPeerReqConflict.setStatus(_A)
_CucsPowerPlacementPgName_Type=SnmpAdminString
_CucsPowerPlacementPgName_Object=MibTableColumn
cucsPowerPlacementPgName=_CucsPowerPlacementPgName_Object((1,3,6,1,4,1,9,9,719,1,39,9,1,8),_CucsPowerPlacementPgName_Type())
cucsPowerPlacementPgName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerPlacementPgName.setStatus(_A)
_CucsPowerPlacementPrioShare_Type=CucsPowerPrioritySharing
_CucsPowerPlacementPrioShare_Object=MibTableColumn
cucsPowerPlacementPrioShare=_CucsPowerPlacementPrioShare_Object((1,3,6,1,4,1,9,9,719,1,39,9,1,9),_CucsPowerPlacementPrioShare_Type())
cucsPowerPlacementPrioShare.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerPlacementPrioShare.setStatus(_A)
_CucsPowerPlacementSelfReqConflict_Type=CucsPowerReqConflict
_CucsPowerPlacementSelfReqConflict_Object=MibTableColumn
cucsPowerPlacementSelfReqConflict=_CucsPowerPlacementSelfReqConflict_Object((1,3,6,1,4,1,9,9,719,1,39,9,1,10),_CucsPowerPlacementSelfReqConflict_Type())
cucsPowerPlacementSelfReqConflict.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerPlacementSelfReqConflict.setStatus(_A)
_CucsPowerPlacementPolicyLevel_Type=Gauge32
_CucsPowerPlacementPolicyLevel_Object=MibTableColumn
cucsPowerPlacementPolicyLevel=_CucsPowerPlacementPolicyLevel_Object((1,3,6,1,4,1,9,9,719,1,39,9,1,11),_CucsPowerPlacementPolicyLevel_Type())
cucsPowerPlacementPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerPlacementPolicyLevel.setStatus(_A)
_CucsPowerPlacementPolicyOwner_Type=CucsPolicyPolicyOwner
_CucsPowerPlacementPolicyOwner_Object=MibTableColumn
cucsPowerPlacementPolicyOwner=_CucsPowerPlacementPolicyOwner_Object((1,3,6,1,4,1,9,9,719,1,39,9,1,12),_CucsPowerPlacementPolicyOwner_Type())
cucsPowerPlacementPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerPlacementPolicyOwner.setStatus(_A)
_CucsPowerPolicyTable_Object=MibTable
cucsPowerPolicyTable=_CucsPowerPolicyTable_Object((1,3,6,1,4,1,9,9,719,1,39,10))
if mibBuilder.loadTexts:cucsPowerPolicyTable.setStatus(_A)
_CucsPowerPolicyEntry_Object=MibTableRow
cucsPowerPolicyEntry=_CucsPowerPolicyEntry_Object((1,3,6,1,4,1,9,9,719,1,39,10,1))
cucsPowerPolicyEntry.setIndexNames((0,_C,_N))
if mibBuilder.loadTexts:cucsPowerPolicyEntry.setStatus(_A)
_CucsPowerPolicyInstanceId_Type=CucsManagedObjectId
_CucsPowerPolicyInstanceId_Object=MibTableColumn
cucsPowerPolicyInstanceId=_CucsPowerPolicyInstanceId_Object((1,3,6,1,4,1,9,9,719,1,39,10,1,1),_CucsPowerPolicyInstanceId_Type())
cucsPowerPolicyInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsPowerPolicyInstanceId.setStatus(_A)
_CucsPowerPolicyDn_Type=CucsManagedObjectDn
_CucsPowerPolicyDn_Object=MibTableColumn
cucsPowerPolicyDn=_CucsPowerPolicyDn_Object((1,3,6,1,4,1,9,9,719,1,39,10,1,2),_CucsPowerPolicyDn_Type())
cucsPowerPolicyDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerPolicyDn.setStatus(_A)
_CucsPowerPolicyRn_Type=SnmpAdminString
_CucsPowerPolicyRn_Object=MibTableColumn
cucsPowerPolicyRn=_CucsPowerPolicyRn_Object((1,3,6,1,4,1,9,9,719,1,39,10,1,3),_CucsPowerPolicyRn_Type())
cucsPowerPolicyRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerPolicyRn.setStatus(_A)
_CucsPowerPolicyDescr_Type=SnmpAdminString
_CucsPowerPolicyDescr_Object=MibTableColumn
cucsPowerPolicyDescr=_CucsPowerPolicyDescr_Object((1,3,6,1,4,1,9,9,719,1,39,10,1,4),_CucsPowerPolicyDescr_Type())
cucsPowerPolicyDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerPolicyDescr.setStatus(_A)
_CucsPowerPolicyIntId_Type=SnmpAdminString
_CucsPowerPolicyIntId_Object=MibTableColumn
cucsPowerPolicyIntId=_CucsPowerPolicyIntId_Object((1,3,6,1,4,1,9,9,719,1,39,10,1,5),_CucsPowerPolicyIntId_Type())
cucsPowerPolicyIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerPolicyIntId.setStatus(_A)
_CucsPowerPolicyName_Type=SnmpAdminString
_CucsPowerPolicyName_Object=MibTableColumn
cucsPowerPolicyName=_CucsPowerPolicyName_Object((1,3,6,1,4,1,9,9,719,1,39,10,1,6),_CucsPowerPolicyName_Type())
cucsPowerPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerPolicyName.setStatus(_A)
_CucsPowerPolicyOperPrio_Type=Gauge32
_CucsPowerPolicyOperPrio_Object=MibTableColumn
cucsPowerPolicyOperPrio=_CucsPowerPolicyOperPrio_Object((1,3,6,1,4,1,9,9,719,1,39,10,1,7),_CucsPowerPolicyOperPrio_Type())
cucsPowerPolicyOperPrio.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerPolicyOperPrio.setStatus(_A)
_CucsPowerPolicyPrio_Type=Gauge32
_CucsPowerPolicyPrio_Object=MibTableColumn
cucsPowerPolicyPrio=_CucsPowerPolicyPrio_Object((1,3,6,1,4,1,9,9,719,1,39,10,1,8),_CucsPowerPolicyPrio_Type())
cucsPowerPolicyPrio.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerPolicyPrio.setStatus(_A)
_CucsPowerPolicyPolicyLevel_Type=Gauge32
_CucsPowerPolicyPolicyLevel_Object=MibTableColumn
cucsPowerPolicyPolicyLevel=_CucsPowerPolicyPolicyLevel_Object((1,3,6,1,4,1,9,9,719,1,39,10,1,9),_CucsPowerPolicyPolicyLevel_Type())
cucsPowerPolicyPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerPolicyPolicyLevel.setStatus(_A)
_CucsPowerPolicyPolicyOwner_Type=CucsPolicyPolicyOwner
_CucsPowerPolicyPolicyOwner_Object=MibTableColumn
cucsPowerPolicyPolicyOwner=_CucsPowerPolicyPolicyOwner_Object((1,3,6,1,4,1,9,9,719,1,39,10,1,10),_CucsPowerPolicyPolicyOwner_Type())
cucsPowerPolicyPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerPolicyPolicyOwner.setStatus(_A)
_CucsPowerPolicyPropAcl_Type=Unsigned64
_CucsPowerPolicyPropAcl_Object=MibTableColumn
cucsPowerPolicyPropAcl=_CucsPowerPolicyPropAcl_Object((1,3,6,1,4,1,9,9,719,1,39,10,1,11),_CucsPowerPolicyPropAcl_Type())
cucsPowerPolicyPropAcl.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerPolicyPropAcl.setStatus(_A)
_CucsPowerPolicyFanSpeed_Type=CucsPowerPolicyFanSpeed
_CucsPowerPolicyFanSpeed_Object=MibTableColumn
cucsPowerPolicyFanSpeed=_CucsPowerPolicyFanSpeed_Object((1,3,6,1,4,1,9,9,719,1,39,10,1,12),_CucsPowerPolicyFanSpeed_Type())
cucsPowerPolicyFanSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerPolicyFanSpeed.setStatus(_A)
_CucsPowerPrioWghtTable_Object=MibTable
cucsPowerPrioWghtTable=_CucsPowerPrioWghtTable_Object((1,3,6,1,4,1,9,9,719,1,39,11))
if mibBuilder.loadTexts:cucsPowerPrioWghtTable.setStatus(_A)
_CucsPowerPrioWghtEntry_Object=MibTableRow
cucsPowerPrioWghtEntry=_CucsPowerPrioWghtEntry_Object((1,3,6,1,4,1,9,9,719,1,39,11,1))
cucsPowerPrioWghtEntry.setIndexNames((0,_C,_O))
if mibBuilder.loadTexts:cucsPowerPrioWghtEntry.setStatus(_A)
_CucsPowerPrioWghtInstanceId_Type=CucsManagedObjectId
_CucsPowerPrioWghtInstanceId_Object=MibTableColumn
cucsPowerPrioWghtInstanceId=_CucsPowerPrioWghtInstanceId_Object((1,3,6,1,4,1,9,9,719,1,39,11,1,1),_CucsPowerPrioWghtInstanceId_Type())
cucsPowerPrioWghtInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsPowerPrioWghtInstanceId.setStatus(_A)
_CucsPowerPrioWghtDn_Type=CucsManagedObjectDn
_CucsPowerPrioWghtDn_Object=MibTableColumn
cucsPowerPrioWghtDn=_CucsPowerPrioWghtDn_Object((1,3,6,1,4,1,9,9,719,1,39,11,1,2),_CucsPowerPrioWghtDn_Type())
cucsPowerPrioWghtDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerPrioWghtDn.setStatus(_A)
_CucsPowerPrioWghtRn_Type=SnmpAdminString
_CucsPowerPrioWghtRn_Object=MibTableColumn
cucsPowerPrioWghtRn=_CucsPowerPrioWghtRn_Object((1,3,6,1,4,1,9,9,719,1,39,11,1,3),_CucsPowerPrioWghtRn_Type())
cucsPowerPrioWghtRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerPrioWghtRn.setStatus(_A)
_CucsPowerPrioWghtPrio_Type=Gauge32
_CucsPowerPrioWghtPrio_Object=MibTableColumn
cucsPowerPrioWghtPrio=_CucsPowerPrioWghtPrio_Object((1,3,6,1,4,1,9,9,719,1,39,11,1,4),_CucsPowerPrioWghtPrio_Type())
cucsPowerPrioWghtPrio.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerPrioWghtPrio.setStatus(_A)
_CucsPowerPrioWghtWeight_Type=Gauge32
_CucsPowerPrioWghtWeight_Object=MibTableColumn
cucsPowerPrioWghtWeight=_CucsPowerPrioWghtWeight_Object((1,3,6,1,4,1,9,9,719,1,39,11,1,5),_CucsPowerPrioWghtWeight_Type())
cucsPowerPrioWghtWeight.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerPrioWghtWeight.setStatus(_A)
_CucsPowerRackUnitMemberTable_Object=MibTable
cucsPowerRackUnitMemberTable=_CucsPowerRackUnitMemberTable_Object((1,3,6,1,4,1,9,9,719,1,39,12))
if mibBuilder.loadTexts:cucsPowerRackUnitMemberTable.setStatus(_A)
_CucsPowerRackUnitMemberEntry_Object=MibTableRow
cucsPowerRackUnitMemberEntry=_CucsPowerRackUnitMemberEntry_Object((1,3,6,1,4,1,9,9,719,1,39,12,1))
cucsPowerRackUnitMemberEntry.setIndexNames((0,_C,_P))
if mibBuilder.loadTexts:cucsPowerRackUnitMemberEntry.setStatus(_A)
_CucsPowerRackUnitMemberInstanceId_Type=CucsManagedObjectId
_CucsPowerRackUnitMemberInstanceId_Object=MibTableColumn
cucsPowerRackUnitMemberInstanceId=_CucsPowerRackUnitMemberInstanceId_Object((1,3,6,1,4,1,9,9,719,1,39,12,1,1),_CucsPowerRackUnitMemberInstanceId_Type())
cucsPowerRackUnitMemberInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsPowerRackUnitMemberInstanceId.setStatus(_A)
_CucsPowerRackUnitMemberDn_Type=CucsManagedObjectDn
_CucsPowerRackUnitMemberDn_Object=MibTableColumn
cucsPowerRackUnitMemberDn=_CucsPowerRackUnitMemberDn_Object((1,3,6,1,4,1,9,9,719,1,39,12,1,2),_CucsPowerRackUnitMemberDn_Type())
cucsPowerRackUnitMemberDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerRackUnitMemberDn.setStatus(_A)
_CucsPowerRackUnitMemberRn_Type=SnmpAdminString
_CucsPowerRackUnitMemberRn_Object=MibTableColumn
cucsPowerRackUnitMemberRn=_CucsPowerRackUnitMemberRn_Object((1,3,6,1,4,1,9,9,719,1,39,12,1,3),_CucsPowerRackUnitMemberRn_Type())
cucsPowerRackUnitMemberRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerRackUnitMemberRn.setStatus(_A)
_CucsPowerRackUnitMemberId_Type=Gauge32
_CucsPowerRackUnitMemberId_Object=MibTableColumn
cucsPowerRackUnitMemberId=_CucsPowerRackUnitMemberId_Object((1,3,6,1,4,1,9,9,719,1,39,12,1,4),_CucsPowerRackUnitMemberId_Type())
cucsPowerRackUnitMemberId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerRackUnitMemberId.setStatus(_A)
_CucsPowerRackUnitMemberOperState_Type=CucsPowerMemberState
_CucsPowerRackUnitMemberOperState_Object=MibTableColumn
cucsPowerRackUnitMemberOperState=_CucsPowerRackUnitMemberOperState_Object((1,3,6,1,4,1,9,9,719,1,39,12,1,5),_CucsPowerRackUnitMemberOperState_Type())
cucsPowerRackUnitMemberOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerRackUnitMemberOperState.setStatus(_A)
_CucsPowerMgmtPolicyTable_Object=MibTable
cucsPowerMgmtPolicyTable=_CucsPowerMgmtPolicyTable_Object((1,3,6,1,4,1,9,9,719,1,39,13))
if mibBuilder.loadTexts:cucsPowerMgmtPolicyTable.setStatus(_A)
_CucsPowerMgmtPolicyEntry_Object=MibTableRow
cucsPowerMgmtPolicyEntry=_CucsPowerMgmtPolicyEntry_Object((1,3,6,1,4,1,9,9,719,1,39,13,1))
cucsPowerMgmtPolicyEntry.setIndexNames((0,_C,_Q))
if mibBuilder.loadTexts:cucsPowerMgmtPolicyEntry.setStatus(_A)
_CucsPowerMgmtPolicyInstanceId_Type=CucsManagedObjectId
_CucsPowerMgmtPolicyInstanceId_Object=MibTableColumn
cucsPowerMgmtPolicyInstanceId=_CucsPowerMgmtPolicyInstanceId_Object((1,3,6,1,4,1,9,9,719,1,39,13,1,1),_CucsPowerMgmtPolicyInstanceId_Type())
cucsPowerMgmtPolicyInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsPowerMgmtPolicyInstanceId.setStatus(_A)
_CucsPowerMgmtPolicyDn_Type=CucsManagedObjectDn
_CucsPowerMgmtPolicyDn_Object=MibTableColumn
cucsPowerMgmtPolicyDn=_CucsPowerMgmtPolicyDn_Object((1,3,6,1,4,1,9,9,719,1,39,13,1,2),_CucsPowerMgmtPolicyDn_Type())
cucsPowerMgmtPolicyDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerMgmtPolicyDn.setStatus(_A)
_CucsPowerMgmtPolicyRn_Type=SnmpAdminString
_CucsPowerMgmtPolicyRn_Object=MibTableColumn
cucsPowerMgmtPolicyRn=_CucsPowerMgmtPolicyRn_Object((1,3,6,1,4,1,9,9,719,1,39,13,1,3),_CucsPowerMgmtPolicyRn_Type())
cucsPowerMgmtPolicyRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerMgmtPolicyRn.setStatus(_A)
_CucsPowerMgmtPolicyDescr_Type=SnmpAdminString
_CucsPowerMgmtPolicyDescr_Object=MibTableColumn
cucsPowerMgmtPolicyDescr=_CucsPowerMgmtPolicyDescr_Object((1,3,6,1,4,1,9,9,719,1,39,13,1,4),_CucsPowerMgmtPolicyDescr_Type())
cucsPowerMgmtPolicyDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerMgmtPolicyDescr.setStatus(_A)
_CucsPowerMgmtPolicyIntId_Type=SnmpAdminString
_CucsPowerMgmtPolicyIntId_Object=MibTableColumn
cucsPowerMgmtPolicyIntId=_CucsPowerMgmtPolicyIntId_Object((1,3,6,1,4,1,9,9,719,1,39,13,1,5),_CucsPowerMgmtPolicyIntId_Type())
cucsPowerMgmtPolicyIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerMgmtPolicyIntId.setStatus(_A)
_CucsPowerMgmtPolicyName_Type=SnmpAdminString
_CucsPowerMgmtPolicyName_Object=MibTableColumn
cucsPowerMgmtPolicyName=_CucsPowerMgmtPolicyName_Object((1,3,6,1,4,1,9,9,719,1,39,13,1,6),_CucsPowerMgmtPolicyName_Type())
cucsPowerMgmtPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerMgmtPolicyName.setStatus(_A)
_CucsPowerMgmtPolicyStyle_Type=CucsPowerMgmtStyle
_CucsPowerMgmtPolicyStyle_Object=MibTableColumn
cucsPowerMgmtPolicyStyle=_CucsPowerMgmtPolicyStyle_Object((1,3,6,1,4,1,9,9,719,1,39,13,1,7),_CucsPowerMgmtPolicyStyle_Type())
cucsPowerMgmtPolicyStyle.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerMgmtPolicyStyle.setStatus(_A)
_CucsPowerMgmtPolicyPolicyLevel_Type=Gauge32
_CucsPowerMgmtPolicyPolicyLevel_Object=MibTableColumn
cucsPowerMgmtPolicyPolicyLevel=_CucsPowerMgmtPolicyPolicyLevel_Object((1,3,6,1,4,1,9,9,719,1,39,13,1,8),_CucsPowerMgmtPolicyPolicyLevel_Type())
cucsPowerMgmtPolicyPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerMgmtPolicyPolicyLevel.setStatus(_A)
_CucsPowerMgmtPolicyPolicyOwner_Type=CucsPolicyPolicyOwner
_CucsPowerMgmtPolicyPolicyOwner_Object=MibTableColumn
cucsPowerMgmtPolicyPolicyOwner=_CucsPowerMgmtPolicyPolicyOwner_Object((1,3,6,1,4,1,9,9,719,1,39,13,1,9),_CucsPowerMgmtPolicyPolicyOwner_Type())
cucsPowerMgmtPolicyPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerMgmtPolicyPolicyOwner.setStatus(_A)
_CucsPowerMgmtPolicyProfiling_Type=TruthValue
_CucsPowerMgmtPolicyProfiling_Object=MibTableColumn
cucsPowerMgmtPolicyProfiling=_CucsPowerMgmtPolicyProfiling_Object((1,3,6,1,4,1,9,9,719,1,39,13,1,10),_CucsPowerMgmtPolicyProfiling_Type())
cucsPowerMgmtPolicyProfiling.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerMgmtPolicyProfiling.setStatus(_A)
_CucsPowerMgmtPolicySkipPowerCheck_Type=TruthValue
_CucsPowerMgmtPolicySkipPowerCheck_Object=MibTableColumn
cucsPowerMgmtPolicySkipPowerCheck=_CucsPowerMgmtPolicySkipPowerCheck_Object((1,3,6,1,4,1,9,9,719,1,39,13,1,11),_CucsPowerMgmtPolicySkipPowerCheck_Type())
cucsPowerMgmtPolicySkipPowerCheck.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerMgmtPolicySkipPowerCheck.setStatus(_A)
_CucsPowerMgmtPolicySkipPowerDeployCheck_Type=TruthValue
_CucsPowerMgmtPolicySkipPowerDeployCheck_Object=MibTableColumn
cucsPowerMgmtPolicySkipPowerDeployCheck=_CucsPowerMgmtPolicySkipPowerDeployCheck_Object((1,3,6,1,4,1,9,9,719,1,39,13,1,12),_CucsPowerMgmtPolicySkipPowerDeployCheck_Type())
cucsPowerMgmtPolicySkipPowerDeployCheck.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerMgmtPolicySkipPowerDeployCheck.setStatus(_A)
_CucsPowerProfiledPowerTable_Object=MibTable
cucsPowerProfiledPowerTable=_CucsPowerProfiledPowerTable_Object((1,3,6,1,4,1,9,9,719,1,39,14))
if mibBuilder.loadTexts:cucsPowerProfiledPowerTable.setStatus(_A)
_CucsPowerProfiledPowerEntry_Object=MibTableRow
cucsPowerProfiledPowerEntry=_CucsPowerProfiledPowerEntry_Object((1,3,6,1,4,1,9,9,719,1,39,14,1))
cucsPowerProfiledPowerEntry.setIndexNames((0,_C,_R))
if mibBuilder.loadTexts:cucsPowerProfiledPowerEntry.setStatus(_A)
_CucsPowerProfiledPowerInstanceId_Type=CucsManagedObjectId
_CucsPowerProfiledPowerInstanceId_Object=MibTableColumn
cucsPowerProfiledPowerInstanceId=_CucsPowerProfiledPowerInstanceId_Object((1,3,6,1,4,1,9,9,719,1,39,14,1,1),_CucsPowerProfiledPowerInstanceId_Type())
cucsPowerProfiledPowerInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsPowerProfiledPowerInstanceId.setStatus(_A)
_CucsPowerProfiledPowerDn_Type=CucsManagedObjectDn
_CucsPowerProfiledPowerDn_Object=MibTableColumn
cucsPowerProfiledPowerDn=_CucsPowerProfiledPowerDn_Object((1,3,6,1,4,1,9,9,719,1,39,14,1,2),_CucsPowerProfiledPowerDn_Type())
cucsPowerProfiledPowerDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerProfiledPowerDn.setStatus(_A)
_CucsPowerProfiledPowerRn_Type=SnmpAdminString
_CucsPowerProfiledPowerRn_Object=MibTableColumn
cucsPowerProfiledPowerRn=_CucsPowerProfiledPowerRn_Object((1,3,6,1,4,1,9,9,719,1,39,14,1,3),_CucsPowerProfiledPowerRn_Type())
cucsPowerProfiledPowerRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerProfiledPowerRn.setStatus(_A)
_CucsPowerProfiledPowerAbsMinPostPower_Type=Gauge32
_CucsPowerProfiledPowerAbsMinPostPower_Object=MibTableColumn
cucsPowerProfiledPowerAbsMinPostPower=_CucsPowerProfiledPowerAbsMinPostPower_Object((1,3,6,1,4,1,9,9,719,1,39,14,1,4),_CucsPowerProfiledPowerAbsMinPostPower_Type())
cucsPowerProfiledPowerAbsMinPostPower.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerProfiledPowerAbsMinPostPower.setStatus(_A)
_CucsPowerProfiledPowerMaxAppPower_Type=Gauge32
_CucsPowerProfiledPowerMaxAppPower_Object=MibTableColumn
cucsPowerProfiledPowerMaxAppPower=_CucsPowerProfiledPowerMaxAppPower_Object((1,3,6,1,4,1,9,9,719,1,39,14,1,5),_CucsPowerProfiledPowerMaxAppPower_Type())
cucsPowerProfiledPowerMaxAppPower.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerProfiledPowerMaxAppPower.setStatus(_A)
_CucsPowerProfiledPowerMaxPostPower_Type=Gauge32
_CucsPowerProfiledPowerMaxPostPower_Object=MibTableColumn
cucsPowerProfiledPowerMaxPostPower=_CucsPowerProfiledPowerMaxPostPower_Object((1,3,6,1,4,1,9,9,719,1,39,14,1,6),_CucsPowerProfiledPowerMaxPostPower_Type())
cucsPowerProfiledPowerMaxPostPower.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerProfiledPowerMaxPostPower.setStatus(_A)
_CucsPowerProfiledPowerMinAppPower_Type=Gauge32
_CucsPowerProfiledPowerMinAppPower_Object=MibTableColumn
cucsPowerProfiledPowerMinAppPower=_CucsPowerProfiledPowerMinAppPower_Object((1,3,6,1,4,1,9,9,719,1,39,14,1,7),_CucsPowerProfiledPowerMinAppPower_Type())
cucsPowerProfiledPowerMinAppPower.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerProfiledPowerMinAppPower.setStatus(_A)
_CucsPowerProfiledPowerMinNormPostPower_Type=Gauge32
_CucsPowerProfiledPowerMinNormPostPower_Object=MibTableColumn
cucsPowerProfiledPowerMinNormPostPower=_CucsPowerProfiledPowerMinNormPostPower_Object((1,3,6,1,4,1,9,9,719,1,39,14,1,8),_CucsPowerProfiledPowerMinNormPostPower_Type())
cucsPowerProfiledPowerMinNormPostPower.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerProfiledPowerMinNormPostPower.setStatus(_A)
_CucsPowerProfiledPowerMinPostPower_Type=Gauge32
_CucsPowerProfiledPowerMinPostPower_Object=MibTableColumn
cucsPowerProfiledPowerMinPostPower=_CucsPowerProfiledPowerMinPostPower_Object((1,3,6,1,4,1,9,9,719,1,39,14,1,9),_CucsPowerProfiledPowerMinPostPower_Type())
cucsPowerProfiledPowerMinPostPower.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerProfiledPowerMinPostPower.setStatus(_A)
_CucsPowerProfiledPowerPreDiscoveryPower_Type=Gauge32
_CucsPowerProfiledPowerPreDiscoveryPower_Object=MibTableColumn
cucsPowerProfiledPowerPreDiscoveryPower=_CucsPowerProfiledPowerPreDiscoveryPower_Object((1,3,6,1,4,1,9,9,719,1,39,14,1,10),_CucsPowerProfiledPowerPreDiscoveryPower_Type())
cucsPowerProfiledPowerPreDiscoveryPower.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerProfiledPowerPreDiscoveryPower.setStatus(_A)
_CucsPowerProfiledPowerProfileRunTime_Type=Gauge32
_CucsPowerProfiledPowerProfileRunTime_Object=MibTableColumn
cucsPowerProfiledPowerProfileRunTime=_CucsPowerProfiledPowerProfileRunTime_Object((1,3,6,1,4,1,9,9,719,1,39,14,1,11),_CucsPowerProfiledPowerProfileRunTime_Type())
cucsPowerProfiledPowerProfileRunTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerProfiledPowerProfileRunTime.setStatus(_A)
_CucsPowerProfiledPowerProfiledBoot_Type=Gauge32
_CucsPowerProfiledPowerProfiledBoot_Object=MibTableColumn
cucsPowerProfiledPowerProfiledBoot=_CucsPowerProfiledPowerProfiledBoot_Object((1,3,6,1,4,1,9,9,719,1,39,14,1,12),_CucsPowerProfiledPowerProfiledBoot_Type())
cucsPowerProfiledPowerProfiledBoot.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerProfiledPowerProfiledBoot.setStatus(_A)
_CucsPowerProfiledPowerProfiledMax_Type=Gauge32
_CucsPowerProfiledPowerProfiledMax_Object=MibTableColumn
cucsPowerProfiledPowerProfiledMax=_CucsPowerProfiledPowerProfiledMax_Object((1,3,6,1,4,1,9,9,719,1,39,14,1,13),_CucsPowerProfiledPowerProfiledMax_Type())
cucsPowerProfiledPowerProfiledMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerProfiledPowerProfiledMax.setStatus(_A)
_CucsPowerProfiledPowerProfiledMin_Type=Gauge32
_CucsPowerProfiledPowerProfiledMin_Object=MibTableColumn
cucsPowerProfiledPowerProfiledMin=_CucsPowerProfiledPowerProfiledMin_Object((1,3,6,1,4,1,9,9,719,1,39,14,1,14),_CucsPowerProfiledPowerProfiledMin_Type())
cucsPowerProfiledPowerProfiledMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerProfiledPowerProfiledMin.setStatus(_A)
_CucsPowerProfiledPowerSkipProfiling_Type=TruthValue
_CucsPowerProfiledPowerSkipProfiling_Object=MibTableColumn
cucsPowerProfiledPowerSkipProfiling=_CucsPowerProfiledPowerSkipProfiling_Object((1,3,6,1,4,1,9,9,719,1,39,14,1,15),_CucsPowerProfiledPowerSkipProfiling_Type())
cucsPowerProfiledPowerSkipProfiling.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerProfiledPowerSkipProfiling.setStatus(_A)
_CucsPowerFIMemberTable_Object=MibTable
cucsPowerFIMemberTable=_CucsPowerFIMemberTable_Object((1,3,6,1,4,1,9,9,719,1,39,15))
if mibBuilder.loadTexts:cucsPowerFIMemberTable.setStatus(_A)
_CucsPowerFIMemberEntry_Object=MibTableRow
cucsPowerFIMemberEntry=_CucsPowerFIMemberEntry_Object((1,3,6,1,4,1,9,9,719,1,39,15,1))
cucsPowerFIMemberEntry.setIndexNames((0,_C,_S))
if mibBuilder.loadTexts:cucsPowerFIMemberEntry.setStatus(_A)
_CucsPowerFIMemberInstanceId_Type=CucsManagedObjectId
_CucsPowerFIMemberInstanceId_Object=MibTableColumn
cucsPowerFIMemberInstanceId=_CucsPowerFIMemberInstanceId_Object((1,3,6,1,4,1,9,9,719,1,39,15,1,1),_CucsPowerFIMemberInstanceId_Type())
cucsPowerFIMemberInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsPowerFIMemberInstanceId.setStatus(_A)
_CucsPowerFIMemberDn_Type=CucsManagedObjectDn
_CucsPowerFIMemberDn_Object=MibTableColumn
cucsPowerFIMemberDn=_CucsPowerFIMemberDn_Object((1,3,6,1,4,1,9,9,719,1,39,15,1,2),_CucsPowerFIMemberDn_Type())
cucsPowerFIMemberDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerFIMemberDn.setStatus(_A)
_CucsPowerFIMemberRn_Type=SnmpAdminString
_CucsPowerFIMemberRn_Object=MibTableColumn
cucsPowerFIMemberRn=_CucsPowerFIMemberRn_Object((1,3,6,1,4,1,9,9,719,1,39,15,1,3),_CucsPowerFIMemberRn_Type())
cucsPowerFIMemberRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerFIMemberRn.setStatus(_A)
_CucsPowerFIMemberFiId_Type=CucsNetworkSwitchId
_CucsPowerFIMemberFiId_Object=MibTableColumn
cucsPowerFIMemberFiId=_CucsPowerFIMemberFiId_Object((1,3,6,1,4,1,9,9,719,1,39,15,1,4),_CucsPowerFIMemberFiId_Type())
cucsPowerFIMemberFiId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerFIMemberFiId.setStatus(_A)
_CucsPowerFIMemberId_Type=Gauge32
_CucsPowerFIMemberId_Object=MibTableColumn
cucsPowerFIMemberId=_CucsPowerFIMemberId_Object((1,3,6,1,4,1,9,9,719,1,39,15,1,5),_CucsPowerFIMemberId_Type())
cucsPowerFIMemberId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerFIMemberId.setStatus(_A)
_CucsPowerFIMemberOperState_Type=CucsPowerMemberState
_CucsPowerFIMemberOperState_Object=MibTableColumn
cucsPowerFIMemberOperState=_CucsPowerFIMemberOperState_Object((1,3,6,1,4,1,9,9,719,1,39,15,1,6),_CucsPowerFIMemberOperState_Type())
cucsPowerFIMemberOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerFIMemberOperState.setStatus(_A)
_CucsPowerFexMemberTable_Object=MibTable
cucsPowerFexMemberTable=_CucsPowerFexMemberTable_Object((1,3,6,1,4,1,9,9,719,1,39,16))
if mibBuilder.loadTexts:cucsPowerFexMemberTable.setStatus(_A)
_CucsPowerFexMemberEntry_Object=MibTableRow
cucsPowerFexMemberEntry=_CucsPowerFexMemberEntry_Object((1,3,6,1,4,1,9,9,719,1,39,16,1))
cucsPowerFexMemberEntry.setIndexNames((0,_C,_T))
if mibBuilder.loadTexts:cucsPowerFexMemberEntry.setStatus(_A)
_CucsPowerFexMemberInstanceId_Type=CucsManagedObjectId
_CucsPowerFexMemberInstanceId_Object=MibTableColumn
cucsPowerFexMemberInstanceId=_CucsPowerFexMemberInstanceId_Object((1,3,6,1,4,1,9,9,719,1,39,16,1,1),_CucsPowerFexMemberInstanceId_Type())
cucsPowerFexMemberInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsPowerFexMemberInstanceId.setStatus(_A)
_CucsPowerFexMemberDn_Type=CucsManagedObjectDn
_CucsPowerFexMemberDn_Object=MibTableColumn
cucsPowerFexMemberDn=_CucsPowerFexMemberDn_Object((1,3,6,1,4,1,9,9,719,1,39,16,1,2),_CucsPowerFexMemberDn_Type())
cucsPowerFexMemberDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerFexMemberDn.setStatus(_A)
_CucsPowerFexMemberRn_Type=SnmpAdminString
_CucsPowerFexMemberRn_Object=MibTableColumn
cucsPowerFexMemberRn=_CucsPowerFexMemberRn_Object((1,3,6,1,4,1,9,9,719,1,39,16,1,3),_CucsPowerFexMemberRn_Type())
cucsPowerFexMemberRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerFexMemberRn.setStatus(_A)
_CucsPowerFexMemberId_Type=Gauge32
_CucsPowerFexMemberId_Object=MibTableColumn
cucsPowerFexMemberId=_CucsPowerFexMemberId_Object((1,3,6,1,4,1,9,9,719,1,39,16,1,4),_CucsPowerFexMemberId_Type())
cucsPowerFexMemberId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerFexMemberId.setStatus(_A)
_CucsPowerFexMemberOperState_Type=CucsPowerMemberState
_CucsPowerFexMemberOperState_Object=MibTableColumn
cucsPowerFexMemberOperState=_CucsPowerFexMemberOperState_Object((1,3,6,1,4,1,9,9,719,1,39,16,1,5),_CucsPowerFexMemberOperState_Type())
cucsPowerFexMemberOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsPowerFexMemberOperState.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'cucsPowerObjects':cucsPowerObjects,'cucsPowerBudgetTable':cucsPowerBudgetTable,'cucsPowerBudgetEntry':cucsPowerBudgetEntry,_E:cucsPowerBudgetInstanceId,'cucsPowerBudgetDn':cucsPowerBudgetDn,'cucsPowerBudgetRn':cucsPowerBudgetRn,'cucsPowerBudgetAdminCommitted':cucsPowerBudgetAdminCommitted,'cucsPowerBudgetAdminPeak':cucsPowerBudgetAdminPeak,'cucsPowerBudgetCurrentPower':cucsPowerBudgetCurrentPower,'cucsPowerBudgetGroupName':cucsPowerBudgetGroupName,'cucsPowerBudgetIdlePower':cucsPowerBudgetIdlePower,'cucsPowerBudgetMaxPower':cucsPowerBudgetMaxPower,'cucsPowerBudgetMinPower':cucsPowerBudgetMinPower,'cucsPowerBudgetOperCommitted':cucsPowerBudgetOperCommitted,'cucsPowerBudgetOperMin':cucsPowerBudgetOperMin,'cucsPowerBudgetOperPeak':cucsPowerBudgetOperPeak,'cucsPowerBudgetScaledWt':cucsPowerBudgetScaledWt,'cucsPowerBudgetOperState':cucsPowerBudgetOperState,'cucsPowerBudgetDynRealloc':cucsPowerBudgetDynRealloc,'cucsPowerBudgetPrio':cucsPowerBudgetPrio,'cucsPowerBudgetCatalogPower':cucsPowerBudgetCatalogPower,'cucsPowerBudgetUpdateTime':cucsPowerBudgetUpdateTime,'cucsPowerBudgetCapAction':cucsPowerBudgetCapAction,'cucsPowerBudgetWeight':cucsPowerBudgetWeight,'cucsPowerBudgetPsuCapacity':cucsPowerBudgetPsuCapacity,'cucsPowerBudgetPsuState':cucsPowerBudgetPsuState,'cucsPowerBudgetStyle':cucsPowerBudgetStyle,'cucsPowerBudgetAdminFPLockState':cucsPowerBudgetAdminFPLockState,'cucsPowerBudgetAdminPeakNew':cucsPowerBudgetAdminPeakNew,'cucsPowerBudgetBootPower':cucsPowerBudgetBootPower,'cucsPowerBudgetChRsrvdPower':cucsPowerBudgetChRsrvdPower,'cucsPowerBudgetOperFPLockState':cucsPowerBudgetOperFPLockState,'cucsPowerBudgetOperProfMethod':cucsPowerBudgetOperProfMethod,'cucsPowerBudgetProfMethod':cucsPowerBudgetProfMethod,'cucsPowerBudgetProfiling':cucsPowerBudgetProfiling,'cucsPowerBudgetPsuLineMode':cucsPowerBudgetPsuLineMode,'cucsPowerBudgetPowerAvailState':cucsPowerBudgetPowerAvailState,'cucsPowerBudgetPowerDeployState':cucsPowerBudgetPowerDeployState,'cucsPowerBudgetPowerOnDeploy':cucsPowerBudgetPowerOnDeploy,'cucsPowerBudgetFanSpeed':cucsPowerBudgetFanSpeed,'cucsPowerBudgetPowerCapSupportEnabled':cucsPowerBudgetPowerCapSupportEnabled,'cucsPowerChassisMemberTable':cucsPowerChassisMemberTable,'cucsPowerChassisMemberEntry':cucsPowerChassisMemberEntry,_F:cucsPowerChassisMemberInstanceId,'cucsPowerChassisMemberDn':cucsPowerChassisMemberDn,'cucsPowerChassisMemberRn':cucsPowerChassisMemberRn,'cucsPowerChassisMemberId':cucsPowerChassisMemberId,'cucsPowerChassisMemberOperState':cucsPowerChassisMemberOperState,'cucsPowerEpTable':cucsPowerEpTable,'cucsPowerEpEntry':cucsPowerEpEntry,_G:cucsPowerEpInstanceId,'cucsPowerEpDn':cucsPowerEpDn,'cucsPowerEpRn':cucsPowerEpRn,'cucsPowerGroupTable':cucsPowerGroupTable,'cucsPowerGroupEntry':cucsPowerGroupEntry,_H:cucsPowerGroupInstanceId,'cucsPowerGroupDn':cucsPowerGroupDn,'cucsPowerGroupRn':cucsPowerGroupRn,'cucsPowerGroupRealloc':cucsPowerGroupRealloc,'cucsPowerGroupAdminCommitted':cucsPowerGroupAdminCommitted,'cucsPowerGroupAdminPeak':cucsPowerGroupAdminPeak,'cucsPowerGroupCurrentPower':cucsPowerGroupCurrentPower,'cucsPowerGroupDescr':cucsPowerGroupDescr,'cucsPowerGroupFltAggr':cucsPowerGroupFltAggr,'cucsPowerGroupCurReqPower':cucsPowerGroupCurReqPower,'cucsPowerGroupMinReqPower':cucsPowerGroupMinReqPower,'cucsPowerGroupIntId':cucsPowerGroupIntId,'cucsPowerGroupName':cucsPowerGroupName,'cucsPowerGroupQualifier':cucsPowerGroupQualifier,'cucsPowerGroupOperCommitted':cucsPowerGroupOperCommitted,'cucsPowerGroupOperPeak':cucsPowerGroupOperPeak,'cucsPowerGroupOperState':cucsPowerGroupOperState,'cucsPowerGroupPolicyLevel':cucsPowerGroupPolicyLevel,'cucsPowerGroupPolicyOwner':cucsPowerGroupPolicyOwner,'cucsPowerGroupMaxReqPower':cucsPowerGroupMaxReqPower,'cucsPowerGroupAdditionPolicyTable':cucsPowerGroupAdditionPolicyTable,'cucsPowerGroupAdditionPolicyEntry':cucsPowerGroupAdditionPolicyEntry,_I:cucsPowerGroupAdditionPolicyInstanceId,'cucsPowerGroupAdditionPolicyDn':cucsPowerGroupAdditionPolicyDn,'cucsPowerGroupAdditionPolicyRn':cucsPowerGroupAdditionPolicyRn,'cucsPowerGroupAdditionPolicyAction':cucsPowerGroupAdditionPolicyAction,'cucsPowerGroupAdditionPolicyDescr':cucsPowerGroupAdditionPolicyDescr,'cucsPowerGroupAdditionPolicyIntId':cucsPowerGroupAdditionPolicyIntId,'cucsPowerGroupAdditionPolicyName':cucsPowerGroupAdditionPolicyName,'cucsPowerGroupAdditionPolicyPolicyLevel':cucsPowerGroupAdditionPolicyPolicyLevel,'cucsPowerGroupAdditionPolicyPolicyOwner':cucsPowerGroupAdditionPolicyPolicyOwner,'cucsPowerGroupQualTable':cucsPowerGroupQualTable,'cucsPowerGroupQualEntry':cucsPowerGroupQualEntry,_J:cucsPowerGroupQualInstanceId,'cucsPowerGroupQualDn':cucsPowerGroupQualDn,'cucsPowerGroupQualRn':cucsPowerGroupQualRn,'cucsPowerGroupQualGroupName':cucsPowerGroupQualGroupName,'cucsPowerGroupStatsTable':cucsPowerGroupStatsTable,'cucsPowerGroupStatsEntry':cucsPowerGroupStatsEntry,_K:cucsPowerGroupStatsInstanceId,'cucsPowerGroupStatsDn':cucsPowerGroupStatsDn,'cucsPowerGroupStatsRn':cucsPowerGroupStatsRn,'cucsPowerGroupStatsIntervals':cucsPowerGroupStatsIntervals,'cucsPowerGroupStatsPower':cucsPowerGroupStatsPower,'cucsPowerGroupStatsPowerAvg':cucsPowerGroupStatsPowerAvg,'cucsPowerGroupStatsPowerMax':cucsPowerGroupStatsPowerMax,'cucsPowerGroupStatsPowerMin':cucsPowerGroupStatsPowerMin,'cucsPowerGroupStatsSuspect':cucsPowerGroupStatsSuspect,'cucsPowerGroupStatsThresholded':cucsPowerGroupStatsThresholded,'cucsPowerGroupStatsTimeCollected':cucsPowerGroupStatsTimeCollected,'cucsPowerGroupStatsUpdate':cucsPowerGroupStatsUpdate,'cucsPowerGroupStatsHistTable':cucsPowerGroupStatsHistTable,'cucsPowerGroupStatsHistEntry':cucsPowerGroupStatsHistEntry,_L:cucsPowerGroupStatsHistInstanceId,'cucsPowerGroupStatsHistDn':cucsPowerGroupStatsHistDn,'cucsPowerGroupStatsHistRn':cucsPowerGroupStatsHistRn,'cucsPowerGroupStatsHistId':cucsPowerGroupStatsHistId,'cucsPowerGroupStatsHistMostRecent':cucsPowerGroupStatsHistMostRecent,'cucsPowerGroupStatsHistPower':cucsPowerGroupStatsHistPower,'cucsPowerGroupStatsHistPowerAvg':cucsPowerGroupStatsHistPowerAvg,'cucsPowerGroupStatsHistPowerMax':cucsPowerGroupStatsHistPowerMax,'cucsPowerGroupStatsHistPowerMin':cucsPowerGroupStatsHistPowerMin,'cucsPowerGroupStatsHistSuspect':cucsPowerGroupStatsHistSuspect,'cucsPowerGroupStatsHistThresholded':cucsPowerGroupStatsHistThresholded,'cucsPowerGroupStatsHistTimeCollected':cucsPowerGroupStatsHistTimeCollected,'cucsPowerPlacementTable':cucsPowerPlacementTable,'cucsPowerPlacementEntry':cucsPowerPlacementEntry,_M:cucsPowerPlacementInstanceId,'cucsPowerPlacementDn':cucsPowerPlacementDn,'cucsPowerPlacementRn':cucsPowerPlacementRn,'cucsPowerPlacementDescr':cucsPowerPlacementDescr,'cucsPowerPlacementIntId':cucsPowerPlacementIntId,'cucsPowerPlacementName':cucsPowerPlacementName,'cucsPowerPlacementPeerReqConflict':cucsPowerPlacementPeerReqConflict,'cucsPowerPlacementPgName':cucsPowerPlacementPgName,'cucsPowerPlacementPrioShare':cucsPowerPlacementPrioShare,'cucsPowerPlacementSelfReqConflict':cucsPowerPlacementSelfReqConflict,'cucsPowerPlacementPolicyLevel':cucsPowerPlacementPolicyLevel,'cucsPowerPlacementPolicyOwner':cucsPowerPlacementPolicyOwner,'cucsPowerPolicyTable':cucsPowerPolicyTable,'cucsPowerPolicyEntry':cucsPowerPolicyEntry,_N:cucsPowerPolicyInstanceId,'cucsPowerPolicyDn':cucsPowerPolicyDn,'cucsPowerPolicyRn':cucsPowerPolicyRn,'cucsPowerPolicyDescr':cucsPowerPolicyDescr,'cucsPowerPolicyIntId':cucsPowerPolicyIntId,'cucsPowerPolicyName':cucsPowerPolicyName,'cucsPowerPolicyOperPrio':cucsPowerPolicyOperPrio,'cucsPowerPolicyPrio':cucsPowerPolicyPrio,'cucsPowerPolicyPolicyLevel':cucsPowerPolicyPolicyLevel,'cucsPowerPolicyPolicyOwner':cucsPowerPolicyPolicyOwner,'cucsPowerPolicyPropAcl':cucsPowerPolicyPropAcl,'cucsPowerPolicyFanSpeed':cucsPowerPolicyFanSpeed,'cucsPowerPrioWghtTable':cucsPowerPrioWghtTable,'cucsPowerPrioWghtEntry':cucsPowerPrioWghtEntry,_O:cucsPowerPrioWghtInstanceId,'cucsPowerPrioWghtDn':cucsPowerPrioWghtDn,'cucsPowerPrioWghtRn':cucsPowerPrioWghtRn,'cucsPowerPrioWghtPrio':cucsPowerPrioWghtPrio,'cucsPowerPrioWghtWeight':cucsPowerPrioWghtWeight,'cucsPowerRackUnitMemberTable':cucsPowerRackUnitMemberTable,'cucsPowerRackUnitMemberEntry':cucsPowerRackUnitMemberEntry,_P:cucsPowerRackUnitMemberInstanceId,'cucsPowerRackUnitMemberDn':cucsPowerRackUnitMemberDn,'cucsPowerRackUnitMemberRn':cucsPowerRackUnitMemberRn,'cucsPowerRackUnitMemberId':cucsPowerRackUnitMemberId,'cucsPowerRackUnitMemberOperState':cucsPowerRackUnitMemberOperState,'cucsPowerMgmtPolicyTable':cucsPowerMgmtPolicyTable,'cucsPowerMgmtPolicyEntry':cucsPowerMgmtPolicyEntry,_Q:cucsPowerMgmtPolicyInstanceId,'cucsPowerMgmtPolicyDn':cucsPowerMgmtPolicyDn,'cucsPowerMgmtPolicyRn':cucsPowerMgmtPolicyRn,'cucsPowerMgmtPolicyDescr':cucsPowerMgmtPolicyDescr,'cucsPowerMgmtPolicyIntId':cucsPowerMgmtPolicyIntId,'cucsPowerMgmtPolicyName':cucsPowerMgmtPolicyName,'cucsPowerMgmtPolicyStyle':cucsPowerMgmtPolicyStyle,'cucsPowerMgmtPolicyPolicyLevel':cucsPowerMgmtPolicyPolicyLevel,'cucsPowerMgmtPolicyPolicyOwner':cucsPowerMgmtPolicyPolicyOwner,'cucsPowerMgmtPolicyProfiling':cucsPowerMgmtPolicyProfiling,'cucsPowerMgmtPolicySkipPowerCheck':cucsPowerMgmtPolicySkipPowerCheck,'cucsPowerMgmtPolicySkipPowerDeployCheck':cucsPowerMgmtPolicySkipPowerDeployCheck,'cucsPowerProfiledPowerTable':cucsPowerProfiledPowerTable,'cucsPowerProfiledPowerEntry':cucsPowerProfiledPowerEntry,_R:cucsPowerProfiledPowerInstanceId,'cucsPowerProfiledPowerDn':cucsPowerProfiledPowerDn,'cucsPowerProfiledPowerRn':cucsPowerProfiledPowerRn,'cucsPowerProfiledPowerAbsMinPostPower':cucsPowerProfiledPowerAbsMinPostPower,'cucsPowerProfiledPowerMaxAppPower':cucsPowerProfiledPowerMaxAppPower,'cucsPowerProfiledPowerMaxPostPower':cucsPowerProfiledPowerMaxPostPower,'cucsPowerProfiledPowerMinAppPower':cucsPowerProfiledPowerMinAppPower,'cucsPowerProfiledPowerMinNormPostPower':cucsPowerProfiledPowerMinNormPostPower,'cucsPowerProfiledPowerMinPostPower':cucsPowerProfiledPowerMinPostPower,'cucsPowerProfiledPowerPreDiscoveryPower':cucsPowerProfiledPowerPreDiscoveryPower,'cucsPowerProfiledPowerProfileRunTime':cucsPowerProfiledPowerProfileRunTime,'cucsPowerProfiledPowerProfiledBoot':cucsPowerProfiledPowerProfiledBoot,'cucsPowerProfiledPowerProfiledMax':cucsPowerProfiledPowerProfiledMax,'cucsPowerProfiledPowerProfiledMin':cucsPowerProfiledPowerProfiledMin,'cucsPowerProfiledPowerSkipProfiling':cucsPowerProfiledPowerSkipProfiling,'cucsPowerFIMemberTable':cucsPowerFIMemberTable,'cucsPowerFIMemberEntry':cucsPowerFIMemberEntry,_S:cucsPowerFIMemberInstanceId,'cucsPowerFIMemberDn':cucsPowerFIMemberDn,'cucsPowerFIMemberRn':cucsPowerFIMemberRn,'cucsPowerFIMemberFiId':cucsPowerFIMemberFiId,'cucsPowerFIMemberId':cucsPowerFIMemberId,'cucsPowerFIMemberOperState':cucsPowerFIMemberOperState,'cucsPowerFexMemberTable':cucsPowerFexMemberTable,'cucsPowerFexMemberEntry':cucsPowerFexMemberEntry,_T:cucsPowerFexMemberInstanceId,'cucsPowerFexMemberDn':cucsPowerFexMemberDn,'cucsPowerFexMemberRn':cucsPowerFexMemberRn,'cucsPowerFexMemberId':cucsPowerFexMemberId,'cucsPowerFexMemberOperState':cucsPowerFexMemberOperState})