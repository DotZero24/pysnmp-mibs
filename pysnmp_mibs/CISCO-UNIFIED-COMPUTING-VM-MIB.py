_W='cucsVmLifeCyclePolicyFsmStageInstanceId'
_V='cucsVmLifeCyclePolicyFsmInstanceId'
_U='cucsVmLifeCyclePolicyFsmTaskInstanceId'
_T='cucsVmComputeEpInstanceId'
_S='cucsVmVsanInstanceId'
_R='cucsVmVnicProfInstInstanceId'
_Q='cucsVmVnicProfClInstanceId'
_P='cucsVmVlanInstanceId'
_O='cucsVmVifInstanceId'
_N='cucsVmSwitchInstanceId'
_M='cucsVmOrgInstanceId'
_L='cucsVmNicInstanceId'
_K='cucsVmLifeCyclePolicyInstanceId'
_J='cucsVmInstanceInstanceId'
_I='cucsVmHvInstanceId'
_H='cucsVmHbaInstanceId'
_G='cucsVmEpInstanceId'
_F='cucsVmDCOrgInstanceId'
_E='cucsVmDCInstanceId'
_D='not-accessible'
_C='CISCO-UNIFIED-COMPUTING-VM-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CiscoAlarmSeverity,CiscoInetAddressMask,CiscoNetworkAddress,TimeIntervalSec,Unsigned64=mibBuilder.importSymbols('CISCO-TC','CiscoAlarmSeverity','CiscoInetAddressMask','CiscoNetworkAddress','TimeIntervalSec','Unsigned64')
CucsManagedObjectDn,CucsManagedObjectId,ciscoUnifiedComputingMIBObjects=mibBuilder.importSymbols('CISCO-UNIFIED-COMPUTING-MIB','CucsManagedObjectDn','CucsManagedObjectId','ciscoUnifiedComputingMIBObjects')
CucsAdaptorLinkState,CucsConditionRemoteInvRslt,CucsDcxOperState,CucsExtvmmOwnership,CucsFabricAVlanAssocPrimaryVlanSwitchId,CucsFabricAVlanSharing,CucsFabricAVlanTransport,CucsFabricAVlanType,CucsFabricAVsanTransport,CucsFabricAVsanType,CucsFabricVlanAssocPrimaryVlanState,CucsFabricVlanOperState,CucsFabricVlanOverlapState,CucsFabricVnetEpIfRole,CucsFabricVnetEpLocale,CucsFabricVnetEpPolicyOwner,CucsFabricVsanOperState,CucsFabricZoningState,CucsFsmCompletion,CucsFsmFlags,CucsFsmFsmStageStatus,CucsNetworkSwitchId,CucsNetworkVnetEpIfType,CucsOsOsType,CucsPolicyPolicyOwner,CucsVmAdaptorOwner,CucsVmComputeEpClInstType,CucsVmHbaType,CucsVmHvClInstType,CucsVmHvType,CucsVmInstType,CucsVmLifeCyclePolicyFsmCurrentFsm,CucsVmLifeCyclePolicyFsmStageName,CucsVmLifeCyclePolicyFsmTaskItem,CucsVmMgmtPlane,CucsVmNicType,CucsVmOsHvVendor,CucsVmStatus,CucsVmSwitchAdminState,CucsVmSwitchVendor,CucsVnicPortProfileType=mibBuilder.importSymbols('CISCO-UNIFIED-COMPUTING-TC-MIB','CucsAdaptorLinkState','CucsConditionRemoteInvRslt','CucsDcxOperState','CucsExtvmmOwnership','CucsFabricAVlanAssocPrimaryVlanSwitchId','CucsFabricAVlanSharing','CucsFabricAVlanTransport','CucsFabricAVlanType','CucsFabricAVsanTransport','CucsFabricAVsanType','CucsFabricVlanAssocPrimaryVlanState','CucsFabricVlanOperState','CucsFabricVlanOverlapState','CucsFabricVnetEpIfRole','CucsFabricVnetEpLocale','CucsFabricVnetEpPolicyOwner','CucsFabricVsanOperState','CucsFabricZoningState','CucsFsmCompletion','CucsFsmFlags','CucsFsmFsmStageStatus','CucsNetworkSwitchId','CucsNetworkVnetEpIfType','CucsOsOsType','CucsPolicyPolicyOwner','CucsVmAdaptorOwner','CucsVmComputeEpClInstType','CucsVmHbaType','CucsVmHvClInstType','CucsVmHvType','CucsVmInstType','CucsVmLifeCyclePolicyFsmCurrentFsm','CucsVmLifeCyclePolicyFsmStageName','CucsVmLifeCyclePolicyFsmTaskItem','CucsVmMgmtPlane','CucsVmNicType','CucsVmOsHvVendor','CucsVmStatus','CucsVmSwitchAdminState','CucsVmSwitchVendor','CucsVnicPortProfileType')
InetAddressIPv4,InetAddressIPv6=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressIPv4','InetAddressIPv6')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowPointer,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowPointer','TextualConvention','TimeInterval','TimeStamp','TruthValue')
cucsVmObjects=ModuleIdentity((1,3,6,1,4,1,9,9,719,1,52))
_CucsVmDCTable_Object=MibTable
cucsVmDCTable=_CucsVmDCTable_Object((1,3,6,1,4,1,9,9,719,1,52,1))
if mibBuilder.loadTexts:cucsVmDCTable.setStatus(_A)
_CucsVmDCEntry_Object=MibTableRow
cucsVmDCEntry=_CucsVmDCEntry_Object((1,3,6,1,4,1,9,9,719,1,52,1,1))
cucsVmDCEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:cucsVmDCEntry.setStatus(_A)
_CucsVmDCInstanceId_Type=CucsManagedObjectId
_CucsVmDCInstanceId_Object=MibTableColumn
cucsVmDCInstanceId=_CucsVmDCInstanceId_Object((1,3,6,1,4,1,9,9,719,1,52,1,1,1),_CucsVmDCInstanceId_Type())
cucsVmDCInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsVmDCInstanceId.setStatus(_A)
_CucsVmDCDn_Type=CucsManagedObjectDn
_CucsVmDCDn_Object=MibTableColumn
cucsVmDCDn=_CucsVmDCDn_Object((1,3,6,1,4,1,9,9,719,1,52,1,1,2),_CucsVmDCDn_Type())
cucsVmDCDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmDCDn.setStatus(_A)
_CucsVmDCRn_Type=SnmpAdminString
_CucsVmDCRn_Object=MibTableColumn
cucsVmDCRn=_CucsVmDCRn_Object((1,3,6,1,4,1,9,9,719,1,52,1,1,3),_CucsVmDCRn_Type())
cucsVmDCRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmDCRn.setStatus(_A)
_CucsVmDCDescr_Type=SnmpAdminString
_CucsVmDCDescr_Object=MibTableColumn
cucsVmDCDescr=_CucsVmDCDescr_Object((1,3,6,1,4,1,9,9,719,1,52,1,1,4),_CucsVmDCDescr_Type())
cucsVmDCDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmDCDescr.setStatus(_A)
_CucsVmDCIntId_Type=SnmpAdminString
_CucsVmDCIntId_Object=MibTableColumn
cucsVmDCIntId=_CucsVmDCIntId_Object((1,3,6,1,4,1,9,9,719,1,52,1,1,5),_CucsVmDCIntId_Type())
cucsVmDCIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmDCIntId.setStatus(_A)
_CucsVmDCName_Type=SnmpAdminString
_CucsVmDCName_Object=MibTableColumn
cucsVmDCName=_CucsVmDCName_Object((1,3,6,1,4,1,9,9,719,1,52,1,1,6),_CucsVmDCName_Type())
cucsVmDCName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmDCName.setStatus(_A)
_CucsVmDCOwn_Type=CucsExtvmmOwnership
_CucsVmDCOwn_Object=MibTableColumn
cucsVmDCOwn=_CucsVmDCOwn_Object((1,3,6,1,4,1,9,9,719,1,52,1,1,7),_CucsVmDCOwn_Type())
cucsVmDCOwn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmDCOwn.setStatus(_A)
_CucsVmDCUuid_Type=SnmpAdminString
_CucsVmDCUuid_Object=MibTableColumn
cucsVmDCUuid=_CucsVmDCUuid_Object((1,3,6,1,4,1,9,9,719,1,52,1,1,8),_CucsVmDCUuid_Type())
cucsVmDCUuid.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmDCUuid.setStatus(_A)
_CucsVmDCPolicyLevel_Type=Gauge32
_CucsVmDCPolicyLevel_Object=MibTableColumn
cucsVmDCPolicyLevel=_CucsVmDCPolicyLevel_Object((1,3,6,1,4,1,9,9,719,1,52,1,1,9),_CucsVmDCPolicyLevel_Type())
cucsVmDCPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmDCPolicyLevel.setStatus(_A)
_CucsVmDCPolicyOwner_Type=CucsPolicyPolicyOwner
_CucsVmDCPolicyOwner_Object=MibTableColumn
cucsVmDCPolicyOwner=_CucsVmDCPolicyOwner_Object((1,3,6,1,4,1,9,9,719,1,52,1,1,10),_CucsVmDCPolicyOwner_Type())
cucsVmDCPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmDCPolicyOwner.setStatus(_A)
_CucsVmDCOrgTable_Object=MibTable
cucsVmDCOrgTable=_CucsVmDCOrgTable_Object((1,3,6,1,4,1,9,9,719,1,52,2))
if mibBuilder.loadTexts:cucsVmDCOrgTable.setStatus(_A)
_CucsVmDCOrgEntry_Object=MibTableRow
cucsVmDCOrgEntry=_CucsVmDCOrgEntry_Object((1,3,6,1,4,1,9,9,719,1,52,2,1))
cucsVmDCOrgEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:cucsVmDCOrgEntry.setStatus(_A)
_CucsVmDCOrgInstanceId_Type=CucsManagedObjectId
_CucsVmDCOrgInstanceId_Object=MibTableColumn
cucsVmDCOrgInstanceId=_CucsVmDCOrgInstanceId_Object((1,3,6,1,4,1,9,9,719,1,52,2,1,1),_CucsVmDCOrgInstanceId_Type())
cucsVmDCOrgInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsVmDCOrgInstanceId.setStatus(_A)
_CucsVmDCOrgDn_Type=CucsManagedObjectDn
_CucsVmDCOrgDn_Object=MibTableColumn
cucsVmDCOrgDn=_CucsVmDCOrgDn_Object((1,3,6,1,4,1,9,9,719,1,52,2,1,2),_CucsVmDCOrgDn_Type())
cucsVmDCOrgDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmDCOrgDn.setStatus(_A)
_CucsVmDCOrgRn_Type=SnmpAdminString
_CucsVmDCOrgRn_Object=MibTableColumn
cucsVmDCOrgRn=_CucsVmDCOrgRn_Object((1,3,6,1,4,1,9,9,719,1,52,2,1,3),_CucsVmDCOrgRn_Type())
cucsVmDCOrgRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmDCOrgRn.setStatus(_A)
_CucsVmDCOrgDescr_Type=SnmpAdminString
_CucsVmDCOrgDescr_Object=MibTableColumn
cucsVmDCOrgDescr=_CucsVmDCOrgDescr_Object((1,3,6,1,4,1,9,9,719,1,52,2,1,4),_CucsVmDCOrgDescr_Type())
cucsVmDCOrgDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmDCOrgDescr.setStatus(_A)
_CucsVmDCOrgIntId_Type=SnmpAdminString
_CucsVmDCOrgIntId_Object=MibTableColumn
cucsVmDCOrgIntId=_CucsVmDCOrgIntId_Object((1,3,6,1,4,1,9,9,719,1,52,2,1,5),_CucsVmDCOrgIntId_Type())
cucsVmDCOrgIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmDCOrgIntId.setStatus(_A)
_CucsVmDCOrgName_Type=SnmpAdminString
_CucsVmDCOrgName_Object=MibTableColumn
cucsVmDCOrgName=_CucsVmDCOrgName_Object((1,3,6,1,4,1,9,9,719,1,52,2,1,6),_CucsVmDCOrgName_Type())
cucsVmDCOrgName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmDCOrgName.setStatus(_A)
_CucsVmDCOrgOwn_Type=CucsExtvmmOwnership
_CucsVmDCOrgOwn_Object=MibTableColumn
cucsVmDCOrgOwn=_CucsVmDCOrgOwn_Object((1,3,6,1,4,1,9,9,719,1,52,2,1,7),_CucsVmDCOrgOwn_Type())
cucsVmDCOrgOwn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmDCOrgOwn.setStatus(_A)
_CucsVmDCOrgUuid_Type=SnmpAdminString
_CucsVmDCOrgUuid_Object=MibTableColumn
cucsVmDCOrgUuid=_CucsVmDCOrgUuid_Object((1,3,6,1,4,1,9,9,719,1,52,2,1,8),_CucsVmDCOrgUuid_Type())
cucsVmDCOrgUuid.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmDCOrgUuid.setStatus(_A)
_CucsVmDCOrgPolicyLevel_Type=Gauge32
_CucsVmDCOrgPolicyLevel_Object=MibTableColumn
cucsVmDCOrgPolicyLevel=_CucsVmDCOrgPolicyLevel_Object((1,3,6,1,4,1,9,9,719,1,52,2,1,9),_CucsVmDCOrgPolicyLevel_Type())
cucsVmDCOrgPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmDCOrgPolicyLevel.setStatus(_A)
_CucsVmDCOrgPolicyOwner_Type=CucsPolicyPolicyOwner
_CucsVmDCOrgPolicyOwner_Object=MibTableColumn
cucsVmDCOrgPolicyOwner=_CucsVmDCOrgPolicyOwner_Object((1,3,6,1,4,1,9,9,719,1,52,2,1,10),_CucsVmDCOrgPolicyOwner_Type())
cucsVmDCOrgPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmDCOrgPolicyOwner.setStatus(_A)
_CucsVmEpTable_Object=MibTable
cucsVmEpTable=_CucsVmEpTable_Object((1,3,6,1,4,1,9,9,719,1,52,3))
if mibBuilder.loadTexts:cucsVmEpTable.setStatus(_A)
_CucsVmEpEntry_Object=MibTableRow
cucsVmEpEntry=_CucsVmEpEntry_Object((1,3,6,1,4,1,9,9,719,1,52,3,1))
cucsVmEpEntry.setIndexNames((0,_C,_G))
if mibBuilder.loadTexts:cucsVmEpEntry.setStatus(_A)
_CucsVmEpInstanceId_Type=CucsManagedObjectId
_CucsVmEpInstanceId_Object=MibTableColumn
cucsVmEpInstanceId=_CucsVmEpInstanceId_Object((1,3,6,1,4,1,9,9,719,1,52,3,1,1),_CucsVmEpInstanceId_Type())
cucsVmEpInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsVmEpInstanceId.setStatus(_A)
_CucsVmEpDn_Type=CucsManagedObjectDn
_CucsVmEpDn_Object=MibTableColumn
cucsVmEpDn=_CucsVmEpDn_Object((1,3,6,1,4,1,9,9,719,1,52,3,1,2),_CucsVmEpDn_Type())
cucsVmEpDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmEpDn.setStatus(_A)
_CucsVmEpRn_Type=SnmpAdminString
_CucsVmEpRn_Object=MibTableColumn
cucsVmEpRn=_CucsVmEpRn_Object((1,3,6,1,4,1,9,9,719,1,52,3,1,3),_CucsVmEpRn_Type())
cucsVmEpRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmEpRn.setStatus(_A)
_CucsVmHbaTable_Object=MibTable
cucsVmHbaTable=_CucsVmHbaTable_Object((1,3,6,1,4,1,9,9,719,1,52,4))
if mibBuilder.loadTexts:cucsVmHbaTable.setStatus(_A)
_CucsVmHbaEntry_Object=MibTableRow
cucsVmHbaEntry=_CucsVmHbaEntry_Object((1,3,6,1,4,1,9,9,719,1,52,4,1))
cucsVmHbaEntry.setIndexNames((0,_C,_H))
if mibBuilder.loadTexts:cucsVmHbaEntry.setStatus(_A)
_CucsVmHbaInstanceId_Type=CucsManagedObjectId
_CucsVmHbaInstanceId_Object=MibTableColumn
cucsVmHbaInstanceId=_CucsVmHbaInstanceId_Object((1,3,6,1,4,1,9,9,719,1,52,4,1,1),_CucsVmHbaInstanceId_Type())
cucsVmHbaInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsVmHbaInstanceId.setStatus(_A)
_CucsVmHbaDn_Type=CucsManagedObjectDn
_CucsVmHbaDn_Object=MibTableColumn
cucsVmHbaDn=_CucsVmHbaDn_Object((1,3,6,1,4,1,9,9,719,1,52,4,1,2),_CucsVmHbaDn_Type())
cucsVmHbaDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmHbaDn.setStatus(_A)
_CucsVmHbaRn_Type=SnmpAdminString
_CucsVmHbaRn_Object=MibTableColumn
cucsVmHbaRn=_CucsVmHbaRn_Object((1,3,6,1,4,1,9,9,719,1,52,4,1,3),_CucsVmHbaRn_Type())
cucsVmHbaRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmHbaRn.setStatus(_A)
_CucsVmHbaDvsPortId_Type=Gauge32
_CucsVmHbaDvsPortId_Object=MibTableColumn
cucsVmHbaDvsPortId=_CucsVmHbaDvsPortId_Object((1,3,6,1,4,1,9,9,719,1,52,4,1,4),_CucsVmHbaDvsPortId_Type())
cucsVmHbaDvsPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmHbaDvsPortId.setStatus(_A)
_CucsVmHbaDvsSwitchId_Type=Gauge32
_CucsVmHbaDvsSwitchId_Object=MibTableColumn
cucsVmHbaDvsSwitchId=_CucsVmHbaDvsSwitchId_Object((1,3,6,1,4,1,9,9,719,1,52,4,1,5),_CucsVmHbaDvsSwitchId_Type())
cucsVmHbaDvsSwitchId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmHbaDvsSwitchId.setStatus(_A)
_CucsVmHbaHostIfDn_Type=SnmpAdminString
_CucsVmHbaHostIfDn_Object=MibTableColumn
cucsVmHbaHostIfDn=_CucsVmHbaHostIfDn_Object((1,3,6,1,4,1,9,9,719,1,52,4,1,6),_CucsVmHbaHostIfDn_Type())
cucsVmHbaHostIfDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmHbaHostIfDn.setStatus(_A)
_CucsVmHbaName_Type=SnmpAdminString
_CucsVmHbaName_Object=MibTableColumn
cucsVmHbaName=_CucsVmHbaName_Object((1,3,6,1,4,1,9,9,719,1,52,4,1,7),_CucsVmHbaName_Type())
cucsVmHbaName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmHbaName.setStatus(_A)
_CucsVmHbaOwner_Type=CucsVmAdaptorOwner
_CucsVmHbaOwner_Object=MibTableColumn
cucsVmHbaOwner=_CucsVmHbaOwner_Object((1,3,6,1,4,1,9,9,719,1,52,4,1,8),_CucsVmHbaOwner_Type())
cucsVmHbaOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmHbaOwner.setStatus(_A)
_CucsVmHbaPhSwitchId_Type=CucsNetworkSwitchId
_CucsVmHbaPhSwitchId_Object=MibTableColumn
cucsVmHbaPhSwitchId=_CucsVmHbaPhSwitchId_Object((1,3,6,1,4,1,9,9,719,1,52,4,1,9),_CucsVmHbaPhSwitchId_Type())
cucsVmHbaPhSwitchId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmHbaPhSwitchId.setStatus(_A)
_CucsVmHbaProfileId_Type=Gauge32
_CucsVmHbaProfileId_Object=MibTableColumn
cucsVmHbaProfileId=_CucsVmHbaProfileId_Object((1,3,6,1,4,1,9,9,719,1,52,4,1,10),_CucsVmHbaProfileId_Type())
cucsVmHbaProfileId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmHbaProfileId.setStatus(_A)
_CucsVmHbaProfileName_Type=SnmpAdminString
_CucsVmHbaProfileName_Object=MibTableColumn
cucsVmHbaProfileName=_CucsVmHbaProfileName_Object((1,3,6,1,4,1,9,9,719,1,52,4,1,11),_CucsVmHbaProfileName_Type())
cucsVmHbaProfileName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmHbaProfileName.setStatus(_A)
_CucsVmHbaStatusChangeTs_Type=DateAndTime
_CucsVmHbaStatusChangeTs_Object=MibTableColumn
cucsVmHbaStatusChangeTs=_CucsVmHbaStatusChangeTs_Object((1,3,6,1,4,1,9,9,719,1,52,4,1,12),_CucsVmHbaStatusChangeTs_Type())
cucsVmHbaStatusChangeTs.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmHbaStatusChangeTs.setStatus(_A)
_CucsVmHbaSwitchId_Type=CucsNetworkSwitchId
_CucsVmHbaSwitchId_Object=MibTableColumn
cucsVmHbaSwitchId=_CucsVmHbaSwitchId_Object((1,3,6,1,4,1,9,9,719,1,52,4,1,13),_CucsVmHbaSwitchId_Type())
cucsVmHbaSwitchId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmHbaSwitchId.setStatus(_A)
_CucsVmHbaType_Type=CucsVmHbaType
_CucsVmHbaType_Object=MibTableColumn
cucsVmHbaType=_CucsVmHbaType_Object((1,3,6,1,4,1,9,9,719,1,52,4,1,14),_CucsVmHbaType_Type())
cucsVmHbaType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmHbaType.setStatus(_A)
_CucsVmHbaUuid_Type=SnmpAdminString
_CucsVmHbaUuid_Object=MibTableColumn
cucsVmHbaUuid=_CucsVmHbaUuid_Object((1,3,6,1,4,1,9,9,719,1,52,4,1,15),_CucsVmHbaUuid_Type())
cucsVmHbaUuid.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmHbaUuid.setStatus(_A)
_CucsVmHbaVStatus_Type=CucsVmStatus
_CucsVmHbaVStatus_Object=MibTableColumn
cucsVmHbaVStatus=_CucsVmHbaVStatus_Object((1,3,6,1,4,1,9,9,719,1,52,4,1,16),_CucsVmHbaVStatus_Type())
cucsVmHbaVStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmHbaVStatus.setStatus(_A)
_CucsVmHbaVcDn_Type=SnmpAdminString
_CucsVmHbaVcDn_Object=MibTableColumn
cucsVmHbaVcDn=_CucsVmHbaVcDn_Object((1,3,6,1,4,1,9,9,719,1,52,4,1,17),_CucsVmHbaVcDn_Type())
cucsVmHbaVcDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmHbaVcDn.setStatus(_A)
_CucsVmHbaVifId_Type=Gauge32
_CucsVmHbaVifId_Object=MibTableColumn
cucsVmHbaVifId=_CucsVmHbaVifId_Object((1,3,6,1,4,1,9,9,719,1,52,4,1,18),_CucsVmHbaVifId_Type())
cucsVmHbaVifId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmHbaVifId.setStatus(_A)
_CucsVmHbaVnicDn_Type=SnmpAdminString
_CucsVmHbaVnicDn_Object=MibTableColumn
cucsVmHbaVnicDn=_CucsVmHbaVnicDn_Object((1,3,6,1,4,1,9,9,719,1,52,4,1,19),_CucsVmHbaVnicDn_Type())
cucsVmHbaVnicDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmHbaVnicDn.setStatus(_A)
_CucsVmHbaWwnn_Type=Unsigned64
_CucsVmHbaWwnn_Object=MibTableColumn
cucsVmHbaWwnn=_CucsVmHbaWwnn_Object((1,3,6,1,4,1,9,9,719,1,52,4,1,20),_CucsVmHbaWwnn_Type())
cucsVmHbaWwnn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmHbaWwnn.setStatus(_A)
_CucsVmHbaWwpn_Type=Unsigned64
_CucsVmHbaWwpn_Object=MibTableColumn
cucsVmHbaWwpn=_CucsVmHbaWwpn_Object((1,3,6,1,4,1,9,9,719,1,52,4,1,21),_CucsVmHbaWwpn_Type())
cucsVmHbaWwpn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmHbaWwpn.setStatus(_A)
_CucsVmHbaDvsGenPortId_Type=SnmpAdminString
_CucsVmHbaDvsGenPortId_Object=MibTableColumn
cucsVmHbaDvsGenPortId=_CucsVmHbaDvsGenPortId_Object((1,3,6,1,4,1,9,9,719,1,52,4,1,22),_CucsVmHbaDvsGenPortId_Type())
cucsVmHbaDvsGenPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmHbaDvsGenPortId.setStatus(_A)
_CucsVmHbaVmndGuid_Type=SnmpAdminString
_CucsVmHbaVmndGuid_Object=MibTableColumn
cucsVmHbaVmndGuid=_CucsVmHbaVmndGuid_Object((1,3,6,1,4,1,9,9,719,1,52,4,1,24),_CucsVmHbaVmndGuid_Type())
cucsVmHbaVmndGuid.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmHbaVmndGuid.setStatus(_A)
_CucsVmHbaVmndName_Type=SnmpAdminString
_CucsVmHbaVmndName_Object=MibTableColumn
cucsVmHbaVmndName=_CucsVmHbaVmndName_Object((1,3,6,1,4,1,9,9,719,1,52,4,1,25),_CucsVmHbaVmndName_Type())
cucsVmHbaVmndName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmHbaVmndName.setStatus(_A)
_CucsVmHvTable_Object=MibTable
cucsVmHvTable=_CucsVmHvTable_Object((1,3,6,1,4,1,9,9,719,1,52,5))
if mibBuilder.loadTexts:cucsVmHvTable.setStatus(_A)
_CucsVmHvEntry_Object=MibTableRow
cucsVmHvEntry=_CucsVmHvEntry_Object((1,3,6,1,4,1,9,9,719,1,52,5,1))
cucsVmHvEntry.setIndexNames((0,_C,_I))
if mibBuilder.loadTexts:cucsVmHvEntry.setStatus(_A)
_CucsVmHvInstanceId_Type=CucsManagedObjectId
_CucsVmHvInstanceId_Object=MibTableColumn
cucsVmHvInstanceId=_CucsVmHvInstanceId_Object((1,3,6,1,4,1,9,9,719,1,52,5,1,1),_CucsVmHvInstanceId_Type())
cucsVmHvInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsVmHvInstanceId.setStatus(_A)
_CucsVmHvDn_Type=CucsManagedObjectDn
_CucsVmHvDn_Object=MibTableColumn
cucsVmHvDn=_CucsVmHvDn_Object((1,3,6,1,4,1,9,9,719,1,52,5,1,2),_CucsVmHvDn_Type())
cucsVmHvDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmHvDn.setStatus(_A)
_CucsVmHvRn_Type=SnmpAdminString
_CucsVmHvRn_Object=MibTableColumn
cucsVmHvRn=_CucsVmHvRn_Object((1,3,6,1,4,1,9,9,719,1,52,5,1,3),_CucsVmHvRn_Type())
cucsVmHvRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmHvRn.setStatus(_A)
_CucsVmHvDescr_Type=SnmpAdminString
_CucsVmHvDescr_Object=MibTableColumn
cucsVmHvDescr=_CucsVmHvDescr_Object((1,3,6,1,4,1,9,9,719,1,52,5,1,4),_CucsVmHvDescr_Type())
cucsVmHvDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmHvDescr.setStatus(_A)
_CucsVmHvDvsDn_Type=SnmpAdminString
_CucsVmHvDvsDn_Object=MibTableColumn
cucsVmHvDvsDn=_CucsVmHvDvsDn_Object((1,3,6,1,4,1,9,9,719,1,52,5,1,5),_CucsVmHvDvsDn_Type())
cucsVmHvDvsDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmHvDvsDn.setStatus(_A)
_CucsVmHvDvsName_Type=SnmpAdminString
_CucsVmHvDvsName_Object=MibTableColumn
cucsVmHvDvsName=_CucsVmHvDvsName_Object((1,3,6,1,4,1,9,9,719,1,52,5,1,6),_CucsVmHvDvsName_Type())
cucsVmHvDvsName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmHvDvsName.setStatus(_A)
_CucsVmHvFltAggr_Type=Unsigned64
_CucsVmHvFltAggr_Object=MibTableColumn
cucsVmHvFltAggr=_CucsVmHvFltAggr_Object((1,3,6,1,4,1,9,9,719,1,52,5,1,7),_CucsVmHvFltAggr_Type())
cucsVmHvFltAggr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmHvFltAggr.setStatus(_A)
_CucsVmHvIntId_Type=SnmpAdminString
_CucsVmHvIntId_Object=MibTableColumn
cucsVmHvIntId=_CucsVmHvIntId_Object((1,3,6,1,4,1,9,9,719,1,52,5,1,8),_CucsVmHvIntId_Type())
cucsVmHvIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmHvIntId.setStatus(_A)
_CucsVmHvLsDn_Type=SnmpAdminString
_CucsVmHvLsDn_Object=MibTableColumn
cucsVmHvLsDn=_CucsVmHvLsDn_Object((1,3,6,1,4,1,9,9,719,1,52,5,1,9),_CucsVmHvLsDn_Type())
cucsVmHvLsDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmHvLsDn.setStatus(_A)
_CucsVmHvName_Type=SnmpAdminString
_CucsVmHvName_Object=MibTableColumn
cucsVmHvName=_CucsVmHvName_Object((1,3,6,1,4,1,9,9,719,1,52,5,1,10),_CucsVmHvName_Type())
cucsVmHvName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmHvName.setStatus(_A)
_CucsVmHvPnDn_Type=SnmpAdminString
_CucsVmHvPnDn_Object=MibTableColumn
cucsVmHvPnDn=_CucsVmHvPnDn_Object((1,3,6,1,4,1,9,9,719,1,52,5,1,11),_CucsVmHvPnDn_Type())
cucsVmHvPnDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmHvPnDn.setStatus(_A)
_CucsVmHvStatusChangeTs_Type=DateAndTime
_CucsVmHvStatusChangeTs_Object=MibTableColumn
cucsVmHvStatusChangeTs=_CucsVmHvStatusChangeTs_Object((1,3,6,1,4,1,9,9,719,1,52,5,1,12),_CucsVmHvStatusChangeTs_Type())
cucsVmHvStatusChangeTs.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmHvStatusChangeTs.setStatus(_A)
_CucsVmHvUuid_Type=SnmpAdminString
_CucsVmHvUuid_Object=MibTableColumn
cucsVmHvUuid=_CucsVmHvUuid_Object((1,3,6,1,4,1,9,9,719,1,52,5,1,13),_CucsVmHvUuid_Type())
cucsVmHvUuid.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmHvUuid.setStatus(_A)
_CucsVmHvVStatus_Type=CucsVmStatus
_CucsVmHvVStatus_Object=MibTableColumn
cucsVmHvVStatus=_CucsVmHvVStatus_Object((1,3,6,1,4,1,9,9,719,1,52,5,1,14),_CucsVmHvVStatus_Type())
cucsVmHvVStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmHvVStatus.setStatus(_A)
_CucsVmHvClInstType_Type=CucsVmHvClInstType
_CucsVmHvClInstType_Object=MibTableColumn
cucsVmHvClInstType=_CucsVmHvClInstType_Object((1,3,6,1,4,1,9,9,719,1,52,5,1,15),_CucsVmHvClInstType_Type())
cucsVmHvClInstType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmHvClInstType.setStatus(_A)
_CucsVmHvHvType_Type=CucsVmHvType
_CucsVmHvHvType_Object=MibTableColumn
cucsVmHvHvType=_CucsVmHvHvType_Object((1,3,6,1,4,1,9,9,719,1,52,5,1,16),_CucsVmHvHvType_Type())
cucsVmHvHvType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmHvHvType.setStatus(_A)
_CucsVmHvModel_Type=CucsOsOsType
_CucsVmHvModel_Object=MibTableColumn
cucsVmHvModel=_CucsVmHvModel_Object((1,3,6,1,4,1,9,9,719,1,52,5,1,17),_CucsVmHvModel_Type())
cucsVmHvModel.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmHvModel.setStatus(_A)
_CucsVmHvVendor_Type=CucsVmOsHvVendor
_CucsVmHvVendor_Object=MibTableColumn
cucsVmHvVendor=_CucsVmHvVendor_Object((1,3,6,1,4,1,9,9,719,1,52,5,1,18),_CucsVmHvVendor_Type())
cucsVmHvVendor.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmHvVendor.setStatus(_A)
_CucsVmHvPolicyLevel_Type=Gauge32
_CucsVmHvPolicyLevel_Object=MibTableColumn
cucsVmHvPolicyLevel=_CucsVmHvPolicyLevel_Object((1,3,6,1,4,1,9,9,719,1,52,5,1,19),_CucsVmHvPolicyLevel_Type())
cucsVmHvPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmHvPolicyLevel.setStatus(_A)
_CucsVmHvPolicyOwner_Type=CucsPolicyPolicyOwner
_CucsVmHvPolicyOwner_Object=MibTableColumn
cucsVmHvPolicyOwner=_CucsVmHvPolicyOwner_Object((1,3,6,1,4,1,9,9,719,1,52,5,1,20),_CucsVmHvPolicyOwner_Type())
cucsVmHvPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmHvPolicyOwner.setStatus(_A)
_CucsVmInstanceTable_Object=MibTable
cucsVmInstanceTable=_CucsVmInstanceTable_Object((1,3,6,1,4,1,9,9,719,1,52,6))
if mibBuilder.loadTexts:cucsVmInstanceTable.setStatus(_A)
_CucsVmInstanceEntry_Object=MibTableRow
cucsVmInstanceEntry=_CucsVmInstanceEntry_Object((1,3,6,1,4,1,9,9,719,1,52,6,1))
cucsVmInstanceEntry.setIndexNames((0,_C,_J))
if mibBuilder.loadTexts:cucsVmInstanceEntry.setStatus(_A)
_CucsVmInstanceInstanceId_Type=CucsManagedObjectId
_CucsVmInstanceInstanceId_Object=MibTableColumn
cucsVmInstanceInstanceId=_CucsVmInstanceInstanceId_Object((1,3,6,1,4,1,9,9,719,1,52,6,1,1),_CucsVmInstanceInstanceId_Type())
cucsVmInstanceInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsVmInstanceInstanceId.setStatus(_A)
_CucsVmInstanceDn_Type=CucsManagedObjectDn
_CucsVmInstanceDn_Object=MibTableColumn
cucsVmInstanceDn=_CucsVmInstanceDn_Object((1,3,6,1,4,1,9,9,719,1,52,6,1,2),_CucsVmInstanceDn_Type())
cucsVmInstanceDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmInstanceDn.setStatus(_A)
_CucsVmInstanceRn_Type=SnmpAdminString
_CucsVmInstanceRn_Object=MibTableColumn
cucsVmInstanceRn=_CucsVmInstanceRn_Object((1,3,6,1,4,1,9,9,719,1,52,6,1,3),_CucsVmInstanceRn_Type())
cucsVmInstanceRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmInstanceRn.setStatus(_A)
_CucsVmInstanceDescr_Type=SnmpAdminString
_CucsVmInstanceDescr_Object=MibTableColumn
cucsVmInstanceDescr=_CucsVmInstanceDescr_Object((1,3,6,1,4,1,9,9,719,1,52,6,1,4),_CucsVmInstanceDescr_Type())
cucsVmInstanceDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmInstanceDescr.setStatus(_A)
_CucsVmInstanceDvsDn_Type=SnmpAdminString
_CucsVmInstanceDvsDn_Object=MibTableColumn
cucsVmInstanceDvsDn=_CucsVmInstanceDvsDn_Object((1,3,6,1,4,1,9,9,719,1,52,6,1,5),_CucsVmInstanceDvsDn_Type())
cucsVmInstanceDvsDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmInstanceDvsDn.setStatus(_A)
_CucsVmInstanceDvsName_Type=SnmpAdminString
_CucsVmInstanceDvsName_Object=MibTableColumn
cucsVmInstanceDvsName=_CucsVmInstanceDvsName_Object((1,3,6,1,4,1,9,9,719,1,52,6,1,6),_CucsVmInstanceDvsName_Type())
cucsVmInstanceDvsName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmInstanceDvsName.setStatus(_A)
_CucsVmInstanceFltAggr_Type=Unsigned64
_CucsVmInstanceFltAggr_Object=MibTableColumn
cucsVmInstanceFltAggr=_CucsVmInstanceFltAggr_Object((1,3,6,1,4,1,9,9,719,1,52,6,1,7),_CucsVmInstanceFltAggr_Type())
cucsVmInstanceFltAggr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmInstanceFltAggr.setStatus(_A)
_CucsVmInstanceHvDn_Type=SnmpAdminString
_CucsVmInstanceHvDn_Object=MibTableColumn
cucsVmInstanceHvDn=_CucsVmInstanceHvDn_Object((1,3,6,1,4,1,9,9,719,1,52,6,1,8),_CucsVmInstanceHvDn_Type())
cucsVmInstanceHvDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmInstanceHvDn.setStatus(_A)
_CucsVmInstanceHvUuid_Type=SnmpAdminString
_CucsVmInstanceHvUuid_Object=MibTableColumn
cucsVmInstanceHvUuid=_CucsVmInstanceHvUuid_Object((1,3,6,1,4,1,9,9,719,1,52,6,1,9),_CucsVmInstanceHvUuid_Type())
cucsVmInstanceHvUuid.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmInstanceHvUuid.setStatus(_A)
_CucsVmInstanceIntId_Type=SnmpAdminString
_CucsVmInstanceIntId_Object=MibTableColumn
cucsVmInstanceIntId=_CucsVmInstanceIntId_Object((1,3,6,1,4,1,9,9,719,1,52,6,1,10),_CucsVmInstanceIntId_Type())
cucsVmInstanceIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmInstanceIntId.setStatus(_A)
_CucsVmInstanceLsDn_Type=SnmpAdminString
_CucsVmInstanceLsDn_Object=MibTableColumn
cucsVmInstanceLsDn=_CucsVmInstanceLsDn_Object((1,3,6,1,4,1,9,9,719,1,52,6,1,11),_CucsVmInstanceLsDn_Type())
cucsVmInstanceLsDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmInstanceLsDn.setStatus(_A)
_CucsVmInstanceName_Type=SnmpAdminString
_CucsVmInstanceName_Object=MibTableColumn
cucsVmInstanceName=_CucsVmInstanceName_Object((1,3,6,1,4,1,9,9,719,1,52,6,1,12),_CucsVmInstanceName_Type())
cucsVmInstanceName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmInstanceName.setStatus(_A)
_CucsVmInstancePnDn_Type=SnmpAdminString
_CucsVmInstancePnDn_Object=MibTableColumn
cucsVmInstancePnDn=_CucsVmInstancePnDn_Object((1,3,6,1,4,1,9,9,719,1,52,6,1,13),_CucsVmInstancePnDn_Type())
cucsVmInstancePnDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmInstancePnDn.setStatus(_A)
_CucsVmInstanceStatusChangeTs_Type=DateAndTime
_CucsVmInstanceStatusChangeTs_Object=MibTableColumn
cucsVmInstanceStatusChangeTs=_CucsVmInstanceStatusChangeTs_Object((1,3,6,1,4,1,9,9,719,1,52,6,1,14),_CucsVmInstanceStatusChangeTs_Type())
cucsVmInstanceStatusChangeTs.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmInstanceStatusChangeTs.setStatus(_A)
_CucsVmInstanceUuid_Type=SnmpAdminString
_CucsVmInstanceUuid_Object=MibTableColumn
cucsVmInstanceUuid=_CucsVmInstanceUuid_Object((1,3,6,1,4,1,9,9,719,1,52,6,1,15),_CucsVmInstanceUuid_Type())
cucsVmInstanceUuid.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmInstanceUuid.setStatus(_A)
_CucsVmInstanceVStatus_Type=CucsVmStatus
_CucsVmInstanceVStatus_Object=MibTableColumn
cucsVmInstanceVStatus=_CucsVmInstanceVStatus_Object((1,3,6,1,4,1,9,9,719,1,52,6,1,16),_CucsVmInstanceVStatus_Type())
cucsVmInstanceVStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmInstanceVStatus.setStatus(_A)
_CucsVmInstanceClInstType_Type=CucsVmInstType
_CucsVmInstanceClInstType_Object=MibTableColumn
cucsVmInstanceClInstType=_CucsVmInstanceClInstType_Object((1,3,6,1,4,1,9,9,719,1,52,6,1,17),_CucsVmInstanceClInstType_Type())
cucsVmInstanceClInstType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmInstanceClInstType.setStatus(_A)
_CucsVmInstanceHvType_Type=CucsVmHvType
_CucsVmInstanceHvType_Object=MibTableColumn
cucsVmInstanceHvType=_CucsVmInstanceHvType_Object((1,3,6,1,4,1,9,9,719,1,52,6,1,18),_CucsVmInstanceHvType_Type())
cucsVmInstanceHvType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmInstanceHvType.setStatus(_A)
_CucsVmInstanceModel_Type=CucsOsOsType
_CucsVmInstanceModel_Object=MibTableColumn
cucsVmInstanceModel=_CucsVmInstanceModel_Object((1,3,6,1,4,1,9,9,719,1,52,6,1,19),_CucsVmInstanceModel_Type())
cucsVmInstanceModel.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmInstanceModel.setStatus(_A)
_CucsVmInstanceVendor_Type=CucsVmOsHvVendor
_CucsVmInstanceVendor_Object=MibTableColumn
cucsVmInstanceVendor=_CucsVmInstanceVendor_Object((1,3,6,1,4,1,9,9,719,1,52,6,1,20),_CucsVmInstanceVendor_Type())
cucsVmInstanceVendor.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmInstanceVendor.setStatus(_A)
_CucsVmInstancePolicyLevel_Type=Gauge32
_CucsVmInstancePolicyLevel_Object=MibTableColumn
cucsVmInstancePolicyLevel=_CucsVmInstancePolicyLevel_Object((1,3,6,1,4,1,9,9,719,1,52,6,1,21),_CucsVmInstancePolicyLevel_Type())
cucsVmInstancePolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmInstancePolicyLevel.setStatus(_A)
_CucsVmInstancePolicyOwner_Type=CucsPolicyPolicyOwner
_CucsVmInstancePolicyOwner_Object=MibTableColumn
cucsVmInstancePolicyOwner=_CucsVmInstancePolicyOwner_Object((1,3,6,1,4,1,9,9,719,1,52,6,1,22),_CucsVmInstancePolicyOwner_Type())
cucsVmInstancePolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmInstancePolicyOwner.setStatus(_A)
_CucsVmLifeCyclePolicyTable_Object=MibTable
cucsVmLifeCyclePolicyTable=_CucsVmLifeCyclePolicyTable_Object((1,3,6,1,4,1,9,9,719,1,52,7))
if mibBuilder.loadTexts:cucsVmLifeCyclePolicyTable.setStatus(_A)
_CucsVmLifeCyclePolicyEntry_Object=MibTableRow
cucsVmLifeCyclePolicyEntry=_CucsVmLifeCyclePolicyEntry_Object((1,3,6,1,4,1,9,9,719,1,52,7,1))
cucsVmLifeCyclePolicyEntry.setIndexNames((0,_C,_K))
if mibBuilder.loadTexts:cucsVmLifeCyclePolicyEntry.setStatus(_A)
_CucsVmLifeCyclePolicyInstanceId_Type=CucsManagedObjectId
_CucsVmLifeCyclePolicyInstanceId_Object=MibTableColumn
cucsVmLifeCyclePolicyInstanceId=_CucsVmLifeCyclePolicyInstanceId_Object((1,3,6,1,4,1,9,9,719,1,52,7,1,1),_CucsVmLifeCyclePolicyInstanceId_Type())
cucsVmLifeCyclePolicyInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsVmLifeCyclePolicyInstanceId.setStatus(_A)
_CucsVmLifeCyclePolicyDn_Type=CucsManagedObjectDn
_CucsVmLifeCyclePolicyDn_Object=MibTableColumn
cucsVmLifeCyclePolicyDn=_CucsVmLifeCyclePolicyDn_Object((1,3,6,1,4,1,9,9,719,1,52,7,1,2),_CucsVmLifeCyclePolicyDn_Type())
cucsVmLifeCyclePolicyDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmLifeCyclePolicyDn.setStatus(_A)
_CucsVmLifeCyclePolicyRn_Type=SnmpAdminString
_CucsVmLifeCyclePolicyRn_Object=MibTableColumn
cucsVmLifeCyclePolicyRn=_CucsVmLifeCyclePolicyRn_Object((1,3,6,1,4,1,9,9,719,1,52,7,1,3),_CucsVmLifeCyclePolicyRn_Type())
cucsVmLifeCyclePolicyRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmLifeCyclePolicyRn.setStatus(_A)
_CucsVmLifeCyclePolicyDescr_Type=SnmpAdminString
_CucsVmLifeCyclePolicyDescr_Object=MibTableColumn
cucsVmLifeCyclePolicyDescr=_CucsVmLifeCyclePolicyDescr_Object((1,3,6,1,4,1,9,9,719,1,52,7,1,4),_CucsVmLifeCyclePolicyDescr_Type())
cucsVmLifeCyclePolicyDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmLifeCyclePolicyDescr.setStatus(_A)
_CucsVmLifeCyclePolicyIntId_Type=SnmpAdminString
_CucsVmLifeCyclePolicyIntId_Object=MibTableColumn
cucsVmLifeCyclePolicyIntId=_CucsVmLifeCyclePolicyIntId_Object((1,3,6,1,4,1,9,9,719,1,52,7,1,5),_CucsVmLifeCyclePolicyIntId_Type())
cucsVmLifeCyclePolicyIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmLifeCyclePolicyIntId.setStatus(_A)
_CucsVmLifeCyclePolicyName_Type=SnmpAdminString
_CucsVmLifeCyclePolicyName_Object=MibTableColumn
cucsVmLifeCyclePolicyName=_CucsVmLifeCyclePolicyName_Object((1,3,6,1,4,1,9,9,719,1,52,7,1,6),_CucsVmLifeCyclePolicyName_Type())
cucsVmLifeCyclePolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmLifeCyclePolicyName.setStatus(_A)
_CucsVmLifeCyclePolicyVmRetention_Type=Gauge32
_CucsVmLifeCyclePolicyVmRetention_Object=MibTableColumn
cucsVmLifeCyclePolicyVmRetention=_CucsVmLifeCyclePolicyVmRetention_Object((1,3,6,1,4,1,9,9,719,1,52,7,1,7),_CucsVmLifeCyclePolicyVmRetention_Type())
cucsVmLifeCyclePolicyVmRetention.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmLifeCyclePolicyVmRetention.setStatus(_A)
_CucsVmLifeCyclePolicyVnicRetention_Type=Gauge32
_CucsVmLifeCyclePolicyVnicRetention_Object=MibTableColumn
cucsVmLifeCyclePolicyVnicRetention=_CucsVmLifeCyclePolicyVnicRetention_Object((1,3,6,1,4,1,9,9,719,1,52,7,1,8),_CucsVmLifeCyclePolicyVnicRetention_Type())
cucsVmLifeCyclePolicyVnicRetention.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmLifeCyclePolicyVnicRetention.setStatus(_A)
_CucsVmLifeCyclePolicyFsmDescr_Type=SnmpAdminString
_CucsVmLifeCyclePolicyFsmDescr_Object=MibTableColumn
cucsVmLifeCyclePolicyFsmDescr=_CucsVmLifeCyclePolicyFsmDescr_Object((1,3,6,1,4,1,9,9,719,1,52,7,1,9),_CucsVmLifeCyclePolicyFsmDescr_Type())
cucsVmLifeCyclePolicyFsmDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmLifeCyclePolicyFsmDescr.setStatus(_A)
_CucsVmLifeCyclePolicyFsmPrev_Type=SnmpAdminString
_CucsVmLifeCyclePolicyFsmPrev_Object=MibTableColumn
cucsVmLifeCyclePolicyFsmPrev=_CucsVmLifeCyclePolicyFsmPrev_Object((1,3,6,1,4,1,9,9,719,1,52,7,1,10),_CucsVmLifeCyclePolicyFsmPrev_Type())
cucsVmLifeCyclePolicyFsmPrev.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmLifeCyclePolicyFsmPrev.setStatus(_A)
_CucsVmLifeCyclePolicyFsmProgr_Type=Gauge32
_CucsVmLifeCyclePolicyFsmProgr_Object=MibTableColumn
cucsVmLifeCyclePolicyFsmProgr=_CucsVmLifeCyclePolicyFsmProgr_Object((1,3,6,1,4,1,9,9,719,1,52,7,1,11),_CucsVmLifeCyclePolicyFsmProgr_Type())
cucsVmLifeCyclePolicyFsmProgr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmLifeCyclePolicyFsmProgr.setStatus(_A)
_CucsVmLifeCyclePolicyFsmRmtInvErrCode_Type=Gauge32
_CucsVmLifeCyclePolicyFsmRmtInvErrCode_Object=MibTableColumn
cucsVmLifeCyclePolicyFsmRmtInvErrCode=_CucsVmLifeCyclePolicyFsmRmtInvErrCode_Object((1,3,6,1,4,1,9,9,719,1,52,7,1,12),_CucsVmLifeCyclePolicyFsmRmtInvErrCode_Type())
cucsVmLifeCyclePolicyFsmRmtInvErrCode.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmLifeCyclePolicyFsmRmtInvErrCode.setStatus(_A)
_CucsVmLifeCyclePolicyFsmRmtInvErrDescr_Type=SnmpAdminString
_CucsVmLifeCyclePolicyFsmRmtInvErrDescr_Object=MibTableColumn
cucsVmLifeCyclePolicyFsmRmtInvErrDescr=_CucsVmLifeCyclePolicyFsmRmtInvErrDescr_Object((1,3,6,1,4,1,9,9,719,1,52,7,1,13),_CucsVmLifeCyclePolicyFsmRmtInvErrDescr_Type())
cucsVmLifeCyclePolicyFsmRmtInvErrDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmLifeCyclePolicyFsmRmtInvErrDescr.setStatus(_A)
_CucsVmLifeCyclePolicyFsmRmtInvRslt_Type=CucsConditionRemoteInvRslt
_CucsVmLifeCyclePolicyFsmRmtInvRslt_Object=MibTableColumn
cucsVmLifeCyclePolicyFsmRmtInvRslt=_CucsVmLifeCyclePolicyFsmRmtInvRslt_Object((1,3,6,1,4,1,9,9,719,1,52,7,1,14),_CucsVmLifeCyclePolicyFsmRmtInvRslt_Type())
cucsVmLifeCyclePolicyFsmRmtInvRslt.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmLifeCyclePolicyFsmRmtInvRslt.setStatus(_A)
_CucsVmLifeCyclePolicyFsmStageDescr_Type=SnmpAdminString
_CucsVmLifeCyclePolicyFsmStageDescr_Object=MibTableColumn
cucsVmLifeCyclePolicyFsmStageDescr=_CucsVmLifeCyclePolicyFsmStageDescr_Object((1,3,6,1,4,1,9,9,719,1,52,7,1,15),_CucsVmLifeCyclePolicyFsmStageDescr_Type())
cucsVmLifeCyclePolicyFsmStageDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmLifeCyclePolicyFsmStageDescr.setStatus(_A)
_CucsVmLifeCyclePolicyFsmStamp_Type=DateAndTime
_CucsVmLifeCyclePolicyFsmStamp_Object=MibTableColumn
cucsVmLifeCyclePolicyFsmStamp=_CucsVmLifeCyclePolicyFsmStamp_Object((1,3,6,1,4,1,9,9,719,1,52,7,1,16),_CucsVmLifeCyclePolicyFsmStamp_Type())
cucsVmLifeCyclePolicyFsmStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmLifeCyclePolicyFsmStamp.setStatus(_A)
_CucsVmLifeCyclePolicyFsmStatus_Type=SnmpAdminString
_CucsVmLifeCyclePolicyFsmStatus_Object=MibTableColumn
cucsVmLifeCyclePolicyFsmStatus=_CucsVmLifeCyclePolicyFsmStatus_Object((1,3,6,1,4,1,9,9,719,1,52,7,1,17),_CucsVmLifeCyclePolicyFsmStatus_Type())
cucsVmLifeCyclePolicyFsmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmLifeCyclePolicyFsmStatus.setStatus(_A)
_CucsVmLifeCyclePolicyFsmTry_Type=Gauge32
_CucsVmLifeCyclePolicyFsmTry_Object=MibTableColumn
cucsVmLifeCyclePolicyFsmTry=_CucsVmLifeCyclePolicyFsmTry_Object((1,3,6,1,4,1,9,9,719,1,52,7,1,18),_CucsVmLifeCyclePolicyFsmTry_Type())
cucsVmLifeCyclePolicyFsmTry.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmLifeCyclePolicyFsmTry.setStatus(_A)
_CucsVmLifeCyclePolicyPolicyLevel_Type=Gauge32
_CucsVmLifeCyclePolicyPolicyLevel_Object=MibTableColumn
cucsVmLifeCyclePolicyPolicyLevel=_CucsVmLifeCyclePolicyPolicyLevel_Object((1,3,6,1,4,1,9,9,719,1,52,7,1,19),_CucsVmLifeCyclePolicyPolicyLevel_Type())
cucsVmLifeCyclePolicyPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmLifeCyclePolicyPolicyLevel.setStatus(_A)
_CucsVmLifeCyclePolicyPolicyOwner_Type=CucsPolicyPolicyOwner
_CucsVmLifeCyclePolicyPolicyOwner_Object=MibTableColumn
cucsVmLifeCyclePolicyPolicyOwner=_CucsVmLifeCyclePolicyPolicyOwner_Object((1,3,6,1,4,1,9,9,719,1,52,7,1,20),_CucsVmLifeCyclePolicyPolicyOwner_Type())
cucsVmLifeCyclePolicyPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmLifeCyclePolicyPolicyOwner.setStatus(_A)
_CucsVmNicTable_Object=MibTable
cucsVmNicTable=_CucsVmNicTable_Object((1,3,6,1,4,1,9,9,719,1,52,8))
if mibBuilder.loadTexts:cucsVmNicTable.setStatus(_A)
_CucsVmNicEntry_Object=MibTableRow
cucsVmNicEntry=_CucsVmNicEntry_Object((1,3,6,1,4,1,9,9,719,1,52,8,1))
cucsVmNicEntry.setIndexNames((0,_C,_L))
if mibBuilder.loadTexts:cucsVmNicEntry.setStatus(_A)
_CucsVmNicInstanceId_Type=CucsManagedObjectId
_CucsVmNicInstanceId_Object=MibTableColumn
cucsVmNicInstanceId=_CucsVmNicInstanceId_Object((1,3,6,1,4,1,9,9,719,1,52,8,1,1),_CucsVmNicInstanceId_Type())
cucsVmNicInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsVmNicInstanceId.setStatus(_A)
_CucsVmNicDn_Type=CucsManagedObjectDn
_CucsVmNicDn_Object=MibTableColumn
cucsVmNicDn=_CucsVmNicDn_Object((1,3,6,1,4,1,9,9,719,1,52,8,1,2),_CucsVmNicDn_Type())
cucsVmNicDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmNicDn.setStatus(_A)
_CucsVmNicRn_Type=SnmpAdminString
_CucsVmNicRn_Object=MibTableColumn
cucsVmNicRn=_CucsVmNicRn_Object((1,3,6,1,4,1,9,9,719,1,52,8,1,3),_CucsVmNicRn_Type())
cucsVmNicRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmNicRn.setStatus(_A)
_CucsVmNicDvsPortId_Type=Gauge32
_CucsVmNicDvsPortId_Object=MibTableColumn
cucsVmNicDvsPortId=_CucsVmNicDvsPortId_Object((1,3,6,1,4,1,9,9,719,1,52,8,1,4),_CucsVmNicDvsPortId_Type())
cucsVmNicDvsPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmNicDvsPortId.setStatus(_A)
_CucsVmNicDvsSwitchId_Type=Gauge32
_CucsVmNicDvsSwitchId_Object=MibTableColumn
cucsVmNicDvsSwitchId=_CucsVmNicDvsSwitchId_Object((1,3,6,1,4,1,9,9,719,1,52,8,1,5),_CucsVmNicDvsSwitchId_Type())
cucsVmNicDvsSwitchId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmNicDvsSwitchId.setStatus(_A)
_CucsVmNicHostIfDn_Type=SnmpAdminString
_CucsVmNicHostIfDn_Object=MibTableColumn
cucsVmNicHostIfDn=_CucsVmNicHostIfDn_Object((1,3,6,1,4,1,9,9,719,1,52,8,1,6),_CucsVmNicHostIfDn_Type())
cucsVmNicHostIfDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmNicHostIfDn.setStatus(_A)
_CucsVmNicMacAddr_Type=MacAddress
_CucsVmNicMacAddr_Object=MibTableColumn
cucsVmNicMacAddr=_CucsVmNicMacAddr_Object((1,3,6,1,4,1,9,9,719,1,52,8,1,7),_CucsVmNicMacAddr_Type())
cucsVmNicMacAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmNicMacAddr.setStatus(_A)
_CucsVmNicName_Type=SnmpAdminString
_CucsVmNicName_Object=MibTableColumn
cucsVmNicName=_CucsVmNicName_Object((1,3,6,1,4,1,9,9,719,1,52,8,1,8),_CucsVmNicName_Type())
cucsVmNicName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmNicName.setStatus(_A)
_CucsVmNicOwner_Type=CucsVmAdaptorOwner
_CucsVmNicOwner_Object=MibTableColumn
cucsVmNicOwner=_CucsVmNicOwner_Object((1,3,6,1,4,1,9,9,719,1,52,8,1,9),_CucsVmNicOwner_Type())
cucsVmNicOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmNicOwner.setStatus(_A)
_CucsVmNicPhSwitchId_Type=CucsNetworkSwitchId
_CucsVmNicPhSwitchId_Object=MibTableColumn
cucsVmNicPhSwitchId=_CucsVmNicPhSwitchId_Object((1,3,6,1,4,1,9,9,719,1,52,8,1,10),_CucsVmNicPhSwitchId_Type())
cucsVmNicPhSwitchId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmNicPhSwitchId.setStatus(_A)
_CucsVmNicProfileId_Type=Gauge32
_CucsVmNicProfileId_Object=MibTableColumn
cucsVmNicProfileId=_CucsVmNicProfileId_Object((1,3,6,1,4,1,9,9,719,1,52,8,1,11),_CucsVmNicProfileId_Type())
cucsVmNicProfileId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmNicProfileId.setStatus(_A)
_CucsVmNicProfileName_Type=SnmpAdminString
_CucsVmNicProfileName_Object=MibTableColumn
cucsVmNicProfileName=_CucsVmNicProfileName_Object((1,3,6,1,4,1,9,9,719,1,52,8,1,12),_CucsVmNicProfileName_Type())
cucsVmNicProfileName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmNicProfileName.setStatus(_A)
_CucsVmNicStatusChangeTs_Type=DateAndTime
_CucsVmNicStatusChangeTs_Object=MibTableColumn
cucsVmNicStatusChangeTs=_CucsVmNicStatusChangeTs_Object((1,3,6,1,4,1,9,9,719,1,52,8,1,13),_CucsVmNicStatusChangeTs_Type())
cucsVmNicStatusChangeTs.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmNicStatusChangeTs.setStatus(_A)
_CucsVmNicSwitchId_Type=CucsNetworkSwitchId
_CucsVmNicSwitchId_Object=MibTableColumn
cucsVmNicSwitchId=_CucsVmNicSwitchId_Object((1,3,6,1,4,1,9,9,719,1,52,8,1,14),_CucsVmNicSwitchId_Type())
cucsVmNicSwitchId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmNicSwitchId.setStatus(_A)
_CucsVmNicType_Type=CucsVmNicType
_CucsVmNicType_Object=MibTableColumn
cucsVmNicType=_CucsVmNicType_Object((1,3,6,1,4,1,9,9,719,1,52,8,1,15),_CucsVmNicType_Type())
cucsVmNicType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmNicType.setStatus(_A)
_CucsVmNicUuid_Type=SnmpAdminString
_CucsVmNicUuid_Object=MibTableColumn
cucsVmNicUuid=_CucsVmNicUuid_Object((1,3,6,1,4,1,9,9,719,1,52,8,1,16),_CucsVmNicUuid_Type())
cucsVmNicUuid.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmNicUuid.setStatus(_A)
_CucsVmNicVStatus_Type=CucsVmStatus
_CucsVmNicVStatus_Object=MibTableColumn
cucsVmNicVStatus=_CucsVmNicVStatus_Object((1,3,6,1,4,1,9,9,719,1,52,8,1,17),_CucsVmNicVStatus_Type())
cucsVmNicVStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmNicVStatus.setStatus(_A)
_CucsVmNicVcDn_Type=SnmpAdminString
_CucsVmNicVcDn_Object=MibTableColumn
cucsVmNicVcDn=_CucsVmNicVcDn_Object((1,3,6,1,4,1,9,9,719,1,52,8,1,18),_CucsVmNicVcDn_Type())
cucsVmNicVcDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmNicVcDn.setStatus(_A)
_CucsVmNicVifId_Type=Gauge32
_CucsVmNicVifId_Object=MibTableColumn
cucsVmNicVifId=_CucsVmNicVifId_Object((1,3,6,1,4,1,9,9,719,1,52,8,1,19),_CucsVmNicVifId_Type())
cucsVmNicVifId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmNicVifId.setStatus(_A)
_CucsVmNicVnicDn_Type=SnmpAdminString
_CucsVmNicVnicDn_Object=MibTableColumn
cucsVmNicVnicDn=_CucsVmNicVnicDn_Object((1,3,6,1,4,1,9,9,719,1,52,8,1,20),_CucsVmNicVnicDn_Type())
cucsVmNicVnicDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmNicVnicDn.setStatus(_A)
_CucsVmNicDvsGenPortId_Type=SnmpAdminString
_CucsVmNicDvsGenPortId_Object=MibTableColumn
cucsVmNicDvsGenPortId=_CucsVmNicDvsGenPortId_Object((1,3,6,1,4,1,9,9,719,1,52,8,1,21),_CucsVmNicDvsGenPortId_Type())
cucsVmNicDvsGenPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmNicDvsGenPortId.setStatus(_A)
_CucsVmNicVmndGuid_Type=SnmpAdminString
_CucsVmNicVmndGuid_Object=MibTableColumn
cucsVmNicVmndGuid=_CucsVmNicVmndGuid_Object((1,3,6,1,4,1,9,9,719,1,52,8,1,23),_CucsVmNicVmndGuid_Type())
cucsVmNicVmndGuid.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmNicVmndGuid.setStatus(_A)
_CucsVmNicVmndName_Type=SnmpAdminString
_CucsVmNicVmndName_Object=MibTableColumn
cucsVmNicVmndName=_CucsVmNicVmndName_Object((1,3,6,1,4,1,9,9,719,1,52,8,1,24),_CucsVmNicVmndName_Type())
cucsVmNicVmndName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmNicVmndName.setStatus(_A)
_CucsVmOrgTable_Object=MibTable
cucsVmOrgTable=_CucsVmOrgTable_Object((1,3,6,1,4,1,9,9,719,1,52,9))
if mibBuilder.loadTexts:cucsVmOrgTable.setStatus(_A)
_CucsVmOrgEntry_Object=MibTableRow
cucsVmOrgEntry=_CucsVmOrgEntry_Object((1,3,6,1,4,1,9,9,719,1,52,9,1))
cucsVmOrgEntry.setIndexNames((0,_C,_M))
if mibBuilder.loadTexts:cucsVmOrgEntry.setStatus(_A)
_CucsVmOrgInstanceId_Type=CucsManagedObjectId
_CucsVmOrgInstanceId_Object=MibTableColumn
cucsVmOrgInstanceId=_CucsVmOrgInstanceId_Object((1,3,6,1,4,1,9,9,719,1,52,9,1,1),_CucsVmOrgInstanceId_Type())
cucsVmOrgInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsVmOrgInstanceId.setStatus(_A)
_CucsVmOrgDn_Type=CucsManagedObjectDn
_CucsVmOrgDn_Object=MibTableColumn
cucsVmOrgDn=_CucsVmOrgDn_Object((1,3,6,1,4,1,9,9,719,1,52,9,1,2),_CucsVmOrgDn_Type())
cucsVmOrgDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmOrgDn.setStatus(_A)
_CucsVmOrgRn_Type=SnmpAdminString
_CucsVmOrgRn_Object=MibTableColumn
cucsVmOrgRn=_CucsVmOrgRn_Object((1,3,6,1,4,1,9,9,719,1,52,9,1,3),_CucsVmOrgRn_Type())
cucsVmOrgRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmOrgRn.setStatus(_A)
_CucsVmOrgDescr_Type=SnmpAdminString
_CucsVmOrgDescr_Object=MibTableColumn
cucsVmOrgDescr=_CucsVmOrgDescr_Object((1,3,6,1,4,1,9,9,719,1,52,9,1,4),_CucsVmOrgDescr_Type())
cucsVmOrgDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmOrgDescr.setStatus(_A)
_CucsVmOrgIntId_Type=SnmpAdminString
_CucsVmOrgIntId_Object=MibTableColumn
cucsVmOrgIntId=_CucsVmOrgIntId_Object((1,3,6,1,4,1,9,9,719,1,52,9,1,5),_CucsVmOrgIntId_Type())
cucsVmOrgIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmOrgIntId.setStatus(_A)
_CucsVmOrgName_Type=SnmpAdminString
_CucsVmOrgName_Object=MibTableColumn
cucsVmOrgName=_CucsVmOrgName_Object((1,3,6,1,4,1,9,9,719,1,52,9,1,6),_CucsVmOrgName_Type())
cucsVmOrgName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmOrgName.setStatus(_A)
_CucsVmOrgOwn_Type=CucsExtvmmOwnership
_CucsVmOrgOwn_Object=MibTableColumn
cucsVmOrgOwn=_CucsVmOrgOwn_Object((1,3,6,1,4,1,9,9,719,1,52,9,1,7),_CucsVmOrgOwn_Type())
cucsVmOrgOwn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmOrgOwn.setStatus(_A)
_CucsVmOrgUuid_Type=SnmpAdminString
_CucsVmOrgUuid_Object=MibTableColumn
cucsVmOrgUuid=_CucsVmOrgUuid_Object((1,3,6,1,4,1,9,9,719,1,52,9,1,8),_CucsVmOrgUuid_Type())
cucsVmOrgUuid.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmOrgUuid.setStatus(_A)
_CucsVmOrgPolicyLevel_Type=Gauge32
_CucsVmOrgPolicyLevel_Object=MibTableColumn
cucsVmOrgPolicyLevel=_CucsVmOrgPolicyLevel_Object((1,3,6,1,4,1,9,9,719,1,52,9,1,9),_CucsVmOrgPolicyLevel_Type())
cucsVmOrgPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmOrgPolicyLevel.setStatus(_A)
_CucsVmOrgPolicyOwner_Type=CucsPolicyPolicyOwner
_CucsVmOrgPolicyOwner_Object=MibTableColumn
cucsVmOrgPolicyOwner=_CucsVmOrgPolicyOwner_Object((1,3,6,1,4,1,9,9,719,1,52,9,1,10),_CucsVmOrgPolicyOwner_Type())
cucsVmOrgPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmOrgPolicyOwner.setStatus(_A)
_CucsVmSwitchTable_Object=MibTable
cucsVmSwitchTable=_CucsVmSwitchTable_Object((1,3,6,1,4,1,9,9,719,1,52,10))
if mibBuilder.loadTexts:cucsVmSwitchTable.setStatus(_A)
_CucsVmSwitchEntry_Object=MibTableRow
cucsVmSwitchEntry=_CucsVmSwitchEntry_Object((1,3,6,1,4,1,9,9,719,1,52,10,1))
cucsVmSwitchEntry.setIndexNames((0,_C,_N))
if mibBuilder.loadTexts:cucsVmSwitchEntry.setStatus(_A)
_CucsVmSwitchInstanceId_Type=CucsManagedObjectId
_CucsVmSwitchInstanceId_Object=MibTableColumn
cucsVmSwitchInstanceId=_CucsVmSwitchInstanceId_Object((1,3,6,1,4,1,9,9,719,1,52,10,1,1),_CucsVmSwitchInstanceId_Type())
cucsVmSwitchInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsVmSwitchInstanceId.setStatus(_A)
_CucsVmSwitchDn_Type=CucsManagedObjectDn
_CucsVmSwitchDn_Object=MibTableColumn
cucsVmSwitchDn=_CucsVmSwitchDn_Object((1,3,6,1,4,1,9,9,719,1,52,10,1,2),_CucsVmSwitchDn_Type())
cucsVmSwitchDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmSwitchDn.setStatus(_A)
_CucsVmSwitchRn_Type=SnmpAdminString
_CucsVmSwitchRn_Object=MibTableColumn
cucsVmSwitchRn=_CucsVmSwitchRn_Object((1,3,6,1,4,1,9,9,719,1,52,10,1,3),_CucsVmSwitchRn_Type())
cucsVmSwitchRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmSwitchRn.setStatus(_A)
_CucsVmSwitchAdminState_Type=CucsVmSwitchAdminState
_CucsVmSwitchAdminState_Object=MibTableColumn
cucsVmSwitchAdminState=_CucsVmSwitchAdminState_Object((1,3,6,1,4,1,9,9,719,1,52,10,1,4),_CucsVmSwitchAdminState_Type())
cucsVmSwitchAdminState.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmSwitchAdminState.setStatus(_A)
_CucsVmSwitchDescr_Type=SnmpAdminString
_CucsVmSwitchDescr_Object=MibTableColumn
cucsVmSwitchDescr=_CucsVmSwitchDescr_Object((1,3,6,1,4,1,9,9,719,1,52,10,1,5),_CucsVmSwitchDescr_Type())
cucsVmSwitchDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmSwitchDescr.setStatus(_A)
_CucsVmSwitchExtKey_Type=SnmpAdminString
_CucsVmSwitchExtKey_Object=MibTableColumn
cucsVmSwitchExtKey=_CucsVmSwitchExtKey_Object((1,3,6,1,4,1,9,9,719,1,52,10,1,6),_CucsVmSwitchExtKey_Type())
cucsVmSwitchExtKey.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmSwitchExtKey.setStatus(_A)
_CucsVmSwitchIntId_Type=SnmpAdminString
_CucsVmSwitchIntId_Object=MibTableColumn
cucsVmSwitchIntId=_CucsVmSwitchIntId_Object((1,3,6,1,4,1,9,9,719,1,52,10,1,7),_CucsVmSwitchIntId_Type())
cucsVmSwitchIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmSwitchIntId.setStatus(_A)
_CucsVmSwitchKeyInst_Type=Gauge32
_CucsVmSwitchKeyInst_Object=MibTableColumn
cucsVmSwitchKeyInst=_CucsVmSwitchKeyInst_Object((1,3,6,1,4,1,9,9,719,1,52,10,1,8),_CucsVmSwitchKeyInst_Type())
cucsVmSwitchKeyInst.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmSwitchKeyInst.setStatus(_A)
_CucsVmSwitchName_Type=SnmpAdminString
_CucsVmSwitchName_Object=MibTableColumn
cucsVmSwitchName=_CucsVmSwitchName_Object((1,3,6,1,4,1,9,9,719,1,52,10,1,9),_CucsVmSwitchName_Type())
cucsVmSwitchName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmSwitchName.setStatus(_A)
_CucsVmSwitchOwn_Type=CucsExtvmmOwnership
_CucsVmSwitchOwn_Object=MibTableColumn
cucsVmSwitchOwn=_CucsVmSwitchOwn_Object((1,3,6,1,4,1,9,9,719,1,52,10,1,10),_CucsVmSwitchOwn_Type())
cucsVmSwitchOwn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmSwitchOwn.setStatus(_A)
_CucsVmSwitchUuid_Type=SnmpAdminString
_CucsVmSwitchUuid_Object=MibTableColumn
cucsVmSwitchUuid=_CucsVmSwitchUuid_Object((1,3,6,1,4,1,9,9,719,1,52,10,1,11),_CucsVmSwitchUuid_Type())
cucsVmSwitchUuid.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmSwitchUuid.setStatus(_A)
_CucsVmSwitchId_Type=SnmpAdminString
_CucsVmSwitchId_Object=MibTableColumn
cucsVmSwitchId=_CucsVmSwitchId_Object((1,3,6,1,4,1,9,9,719,1,52,10,1,12),_CucsVmSwitchId_Type())
cucsVmSwitchId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmSwitchId.setStatus(_A)
_CucsVmSwitchManager_Type=CucsVmMgmtPlane
_CucsVmSwitchManager_Object=MibTableColumn
cucsVmSwitchManager=_CucsVmSwitchManager_Object((1,3,6,1,4,1,9,9,719,1,52,10,1,13),_CucsVmSwitchManager_Type())
cucsVmSwitchManager.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmSwitchManager.setStatus(_A)
_CucsVmSwitchPolicyLevel_Type=Gauge32
_CucsVmSwitchPolicyLevel_Object=MibTableColumn
cucsVmSwitchPolicyLevel=_CucsVmSwitchPolicyLevel_Object((1,3,6,1,4,1,9,9,719,1,52,10,1,14),_CucsVmSwitchPolicyLevel_Type())
cucsVmSwitchPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmSwitchPolicyLevel.setStatus(_A)
_CucsVmSwitchPolicyOwner_Type=CucsPolicyPolicyOwner
_CucsVmSwitchPolicyOwner_Object=MibTableColumn
cucsVmSwitchPolicyOwner=_CucsVmSwitchPolicyOwner_Object((1,3,6,1,4,1,9,9,719,1,52,10,1,15),_CucsVmSwitchPolicyOwner_Type())
cucsVmSwitchPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmSwitchPolicyOwner.setStatus(_A)
_CucsVmSwitchFltAggr_Type=Unsigned64
_CucsVmSwitchFltAggr_Object=MibTableColumn
cucsVmSwitchFltAggr=_CucsVmSwitchFltAggr_Object((1,3,6,1,4,1,9,9,719,1,52,10,1,16),_CucsVmSwitchFltAggr_Type())
cucsVmSwitchFltAggr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmSwitchFltAggr.setStatus(_A)
_CucsVmSwitchVendor_Type=CucsVmSwitchVendor
_CucsVmSwitchVendor_Object=MibTableColumn
cucsVmSwitchVendor=_CucsVmSwitchVendor_Object((1,3,6,1,4,1,9,9,719,1,52,10,1,17),_CucsVmSwitchVendor_Type())
cucsVmSwitchVendor.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmSwitchVendor.setStatus(_A)
_CucsVmVifTable_Object=MibTable
cucsVmVifTable=_CucsVmVifTable_Object((1,3,6,1,4,1,9,9,719,1,52,11))
if mibBuilder.loadTexts:cucsVmVifTable.setStatus(_A)
_CucsVmVifEntry_Object=MibTableRow
cucsVmVifEntry=_CucsVmVifEntry_Object((1,3,6,1,4,1,9,9,719,1,52,11,1))
cucsVmVifEntry.setIndexNames((0,_C,_O))
if mibBuilder.loadTexts:cucsVmVifEntry.setStatus(_A)
_CucsVmVifInstanceId_Type=CucsManagedObjectId
_CucsVmVifInstanceId_Object=MibTableColumn
cucsVmVifInstanceId=_CucsVmVifInstanceId_Object((1,3,6,1,4,1,9,9,719,1,52,11,1,1),_CucsVmVifInstanceId_Type())
cucsVmVifInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsVmVifInstanceId.setStatus(_A)
_CucsVmVifDn_Type=CucsManagedObjectDn
_CucsVmVifDn_Object=MibTableColumn
cucsVmVifDn=_CucsVmVifDn_Object((1,3,6,1,4,1,9,9,719,1,52,11,1,2),_CucsVmVifDn_Type())
cucsVmVifDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmVifDn.setStatus(_A)
_CucsVmVifRn_Type=SnmpAdminString
_CucsVmVifRn_Object=MibTableColumn
cucsVmVifRn=_CucsVmVifRn_Object((1,3,6,1,4,1,9,9,719,1,52,11,1,3),_CucsVmVifRn_Type())
cucsVmVifRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmVifRn.setStatus(_A)
_CucsVmVifCookie_Type=Gauge32
_CucsVmVifCookie_Object=MibTableColumn
cucsVmVifCookie=_CucsVmVifCookie_Object((1,3,6,1,4,1,9,9,719,1,52,11,1,4),_CucsVmVifCookie_Type())
cucsVmVifCookie.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmVifCookie.setStatus(_A)
_CucsVmVifPhSwitchId_Type=CucsNetworkSwitchId
_CucsVmVifPhSwitchId_Object=MibTableColumn
cucsVmVifPhSwitchId=_CucsVmVifPhSwitchId_Object((1,3,6,1,4,1,9,9,719,1,52,11,1,5),_CucsVmVifPhSwitchId_Type())
cucsVmVifPhSwitchId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmVifPhSwitchId.setStatus(_A)
_CucsVmVifPhsAccessCardId_Type=Gauge32
_CucsVmVifPhsAccessCardId_Object=MibTableColumn
cucsVmVifPhsAccessCardId=_CucsVmVifPhsAccessCardId_Object((1,3,6,1,4,1,9,9,719,1,52,11,1,6),_CucsVmVifPhsAccessCardId_Type())
cucsVmVifPhsAccessCardId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmVifPhsAccessCardId.setStatus(_A)
_CucsVmVifPhsAccessPortId_Type=Gauge32
_CucsVmVifPhsAccessPortId_Object=MibTableColumn
cucsVmVifPhsAccessPortId=_CucsVmVifPhsAccessPortId_Object((1,3,6,1,4,1,9,9,719,1,52,11,1,7),_CucsVmVifPhsAccessPortId_Type())
cucsVmVifPhsAccessPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmVifPhsAccessPortId.setStatus(_A)
_CucsVmVifPhsBorderCardId_Type=Gauge32
_CucsVmVifPhsBorderCardId_Object=MibTableColumn
cucsVmVifPhsBorderCardId=_CucsVmVifPhsBorderCardId_Object((1,3,6,1,4,1,9,9,719,1,52,11,1,8),_CucsVmVifPhsBorderCardId_Type())
cucsVmVifPhsBorderCardId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmVifPhsBorderCardId.setStatus(_A)
_CucsVmVifPhsBorderPortId_Type=Gauge32
_CucsVmVifPhsBorderPortId_Object=MibTableColumn
cucsVmVifPhsBorderPortId=_CucsVmVifPhsBorderPortId_Object((1,3,6,1,4,1,9,9,719,1,52,11,1,9),_CucsVmVifPhsBorderPortId_Type())
cucsVmVifPhsBorderPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmVifPhsBorderPortId.setStatus(_A)
_CucsVmVifStatusChangeTs_Type=DateAndTime
_CucsVmVifStatusChangeTs_Object=MibTableColumn
cucsVmVifStatusChangeTs=_CucsVmVifStatusChangeTs_Object((1,3,6,1,4,1,9,9,719,1,52,11,1,10),_CucsVmVifStatusChangeTs_Type())
cucsVmVifStatusChangeTs.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmVifStatusChangeTs.setStatus(_A)
_CucsVmVifVStatus_Type=CucsVmStatus
_CucsVmVifVStatus_Object=MibTableColumn
cucsVmVifVStatus=_CucsVmVifVStatus_Object((1,3,6,1,4,1,9,9,719,1,52,11,1,11),_CucsVmVifVStatus_Type())
cucsVmVifVStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmVifVStatus.setStatus(_A)
_CucsVmVifVcDn_Type=SnmpAdminString
_CucsVmVifVcDn_Object=MibTableColumn
cucsVmVifVcDn=_CucsVmVifVcDn_Object((1,3,6,1,4,1,9,9,719,1,52,11,1,12),_CucsVmVifVcDn_Type())
cucsVmVifVcDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmVifVcDn.setStatus(_A)
_CucsVmVifVifId_Type=Gauge32
_CucsVmVifVifId_Object=MibTableColumn
cucsVmVifVifId=_CucsVmVifVifId_Object((1,3,6,1,4,1,9,9,719,1,52,11,1,13),_CucsVmVifVifId_Type())
cucsVmVifVifId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmVifVifId.setStatus(_A)
_CucsVmVifAdpVifId_Type=Gauge32
_CucsVmVifAdpVifId_Object=MibTableColumn
cucsVmVifAdpVifId=_CucsVmVifAdpVifId_Object((1,3,6,1,4,1,9,9,719,1,52,11,1,14),_CucsVmVifAdpVifId_Type())
cucsVmVifAdpVifId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmVifAdpVifId.setStatus(_A)
_CucsVmVifLinkState_Type=CucsAdaptorLinkState
_CucsVmVifLinkState_Object=MibTableColumn
cucsVmVifLinkState=_CucsVmVifLinkState_Object((1,3,6,1,4,1,9,9,719,1,52,11,1,15),_CucsVmVifLinkState_Type())
cucsVmVifLinkState.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmVifLinkState.setStatus(_A)
_CucsVmVifOperState_Type=CucsDcxOperState
_CucsVmVifOperState_Object=MibTableColumn
cucsVmVifOperState=_CucsVmVifOperState_Object((1,3,6,1,4,1,9,9,719,1,52,11,1,16),_CucsVmVifOperState_Type())
cucsVmVifOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmVifOperState.setStatus(_A)
_CucsVmVifStateQual_Type=SnmpAdminString
_CucsVmVifStateQual_Object=MibTableColumn
cucsVmVifStateQual=_CucsVmVifStateQual_Object((1,3,6,1,4,1,9,9,719,1,52,11,1,17),_CucsVmVifStateQual_Type())
cucsVmVifStateQual.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmVifStateQual.setStatus(_A)
_CucsVmVifPhsAccessAggrPortId_Type=Gauge32
_CucsVmVifPhsAccessAggrPortId_Object=MibTableColumn
cucsVmVifPhsAccessAggrPortId=_CucsVmVifPhsAccessAggrPortId_Object((1,3,6,1,4,1,9,9,719,1,52,11,1,18),_CucsVmVifPhsAccessAggrPortId_Type())
cucsVmVifPhsAccessAggrPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmVifPhsAccessAggrPortId.setStatus(_A)
_CucsVmVifPhsBorderAggrPortId_Type=Gauge32
_CucsVmVifPhsBorderAggrPortId_Object=MibTableColumn
cucsVmVifPhsBorderAggrPortId=_CucsVmVifPhsBorderAggrPortId_Object((1,3,6,1,4,1,9,9,719,1,52,11,1,19),_CucsVmVifPhsBorderAggrPortId_Type())
cucsVmVifPhsBorderAggrPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmVifPhsBorderAggrPortId.setStatus(_A)
_CucsVmVlanTable_Object=MibTable
cucsVmVlanTable=_CucsVmVlanTable_Object((1,3,6,1,4,1,9,9,719,1,52,12))
if mibBuilder.loadTexts:cucsVmVlanTable.setStatus(_A)
_CucsVmVlanEntry_Object=MibTableRow
cucsVmVlanEntry=_CucsVmVlanEntry_Object((1,3,6,1,4,1,9,9,719,1,52,12,1))
cucsVmVlanEntry.setIndexNames((0,_C,_P))
if mibBuilder.loadTexts:cucsVmVlanEntry.setStatus(_A)
_CucsVmVlanInstanceId_Type=CucsManagedObjectId
_CucsVmVlanInstanceId_Object=MibTableColumn
cucsVmVlanInstanceId=_CucsVmVlanInstanceId_Object((1,3,6,1,4,1,9,9,719,1,52,12,1,1),_CucsVmVlanInstanceId_Type())
cucsVmVlanInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsVmVlanInstanceId.setStatus(_A)
_CucsVmVlanDn_Type=CucsManagedObjectDn
_CucsVmVlanDn_Object=MibTableColumn
cucsVmVlanDn=_CucsVmVlanDn_Object((1,3,6,1,4,1,9,9,719,1,52,12,1,2),_CucsVmVlanDn_Type())
cucsVmVlanDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmVlanDn.setStatus(_A)
_CucsVmVlanRn_Type=SnmpAdminString
_CucsVmVlanRn_Object=MibTableColumn
cucsVmVlanRn=_CucsVmVlanRn_Object((1,3,6,1,4,1,9,9,719,1,52,12,1,3),_CucsVmVlanRn_Type())
cucsVmVlanRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmVlanRn.setStatus(_A)
_CucsVmVlanEpDn_Type=SnmpAdminString
_CucsVmVlanEpDn_Object=MibTableColumn
cucsVmVlanEpDn=_CucsVmVlanEpDn_Object((1,3,6,1,4,1,9,9,719,1,52,12,1,4),_CucsVmVlanEpDn_Type())
cucsVmVlanEpDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmVlanEpDn.setStatus(_A)
_CucsVmVlanId_Type=Gauge32
_CucsVmVlanId_Object=MibTableColumn
cucsVmVlanId=_CucsVmVlanId_Object((1,3,6,1,4,1,9,9,719,1,52,12,1,5),_CucsVmVlanId_Type())
cucsVmVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmVlanId.setStatus(_A)
_CucsVmVlanIfRole_Type=CucsFabricVnetEpIfRole
_CucsVmVlanIfRole_Object=MibTableColumn
cucsVmVlanIfRole=_CucsVmVlanIfRole_Object((1,3,6,1,4,1,9,9,719,1,52,12,1,6),_CucsVmVlanIfRole_Type())
cucsVmVlanIfRole.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmVlanIfRole.setStatus(_A)
_CucsVmVlanIfType_Type=CucsNetworkVnetEpIfType
_CucsVmVlanIfType_Object=MibTableColumn
cucsVmVlanIfType=_CucsVmVlanIfType_Object((1,3,6,1,4,1,9,9,719,1,52,12,1,7),_CucsVmVlanIfType_Type())
cucsVmVlanIfType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmVlanIfType.setStatus(_A)
_CucsVmVlanLocale_Type=CucsFabricVnetEpLocale
_CucsVmVlanLocale_Object=MibTableColumn
cucsVmVlanLocale=_CucsVmVlanLocale_Object((1,3,6,1,4,1,9,9,719,1,52,12,1,8),_CucsVmVlanLocale_Type())
cucsVmVlanLocale.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmVlanLocale.setStatus(_A)
_CucsVmVlanName_Type=SnmpAdminString
_CucsVmVlanName_Object=MibTableColumn
cucsVmVlanName=_CucsVmVlanName_Object((1,3,6,1,4,1,9,9,719,1,52,12,1,9),_CucsVmVlanName_Type())
cucsVmVlanName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmVlanName.setStatus(_A)
_CucsVmVlanPeerDn_Type=SnmpAdminString
_CucsVmVlanPeerDn_Object=MibTableColumn
cucsVmVlanPeerDn=_CucsVmVlanPeerDn_Object((1,3,6,1,4,1,9,9,719,1,52,12,1,10),_CucsVmVlanPeerDn_Type())
cucsVmVlanPeerDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmVlanPeerDn.setStatus(_A)
_CucsVmVlanPubNwDn_Type=SnmpAdminString
_CucsVmVlanPubNwDn_Object=MibTableColumn
cucsVmVlanPubNwDn=_CucsVmVlanPubNwDn_Object((1,3,6,1,4,1,9,9,719,1,52,12,1,11),_CucsVmVlanPubNwDn_Type())
cucsVmVlanPubNwDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmVlanPubNwDn.setStatus(_A)
_CucsVmVlanPubNwId_Type=Gauge32
_CucsVmVlanPubNwId_Object=MibTableColumn
cucsVmVlanPubNwId=_CucsVmVlanPubNwId_Object((1,3,6,1,4,1,9,9,719,1,52,12,1,12),_CucsVmVlanPubNwId_Type())
cucsVmVlanPubNwId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmVlanPubNwId.setStatus(_A)
_CucsVmVlanPubNwName_Type=SnmpAdminString
_CucsVmVlanPubNwName_Object=MibTableColumn
cucsVmVlanPubNwName=_CucsVmVlanPubNwName_Object((1,3,6,1,4,1,9,9,719,1,52,12,1,13),_CucsVmVlanPubNwName_Type())
cucsVmVlanPubNwName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmVlanPubNwName.setStatus(_A)
_CucsVmVlanSharing_Type=CucsFabricAVlanSharing
_CucsVmVlanSharing_Object=MibTableColumn
cucsVmVlanSharing=_CucsVmVlanSharing_Object((1,3,6,1,4,1,9,9,719,1,52,12,1,14),_CucsVmVlanSharing_Type())
cucsVmVlanSharing.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmVlanSharing.setStatus(_A)
_CucsVmVlanSwitchId_Type=CucsNetworkSwitchId
_CucsVmVlanSwitchId_Object=MibTableColumn
cucsVmVlanSwitchId=_CucsVmVlanSwitchId_Object((1,3,6,1,4,1,9,9,719,1,52,12,1,15),_CucsVmVlanSwitchId_Type())
cucsVmVlanSwitchId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmVlanSwitchId.setStatus(_A)
_CucsVmVlanTransport_Type=CucsFabricAVlanTransport
_CucsVmVlanTransport_Object=MibTableColumn
cucsVmVlanTransport=_CucsVmVlanTransport_Object((1,3,6,1,4,1,9,9,719,1,52,12,1,16),_CucsVmVlanTransport_Type())
cucsVmVlanTransport.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmVlanTransport.setStatus(_A)
_CucsVmVlanType_Type=CucsFabricAVlanType
_CucsVmVlanType_Object=MibTableColumn
cucsVmVlanType=_CucsVmVlanType_Object((1,3,6,1,4,1,9,9,719,1,52,12,1,17),_CucsVmVlanType_Type())
cucsVmVlanType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmVlanType.setStatus(_A)
_CucsVmVlanOperState_Type=CucsFabricVlanOperState
_CucsVmVlanOperState_Object=MibTableColumn
cucsVmVlanOperState=_CucsVmVlanOperState_Object((1,3,6,1,4,1,9,9,719,1,52,12,1,18),_CucsVmVlanOperState_Type())
cucsVmVlanOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmVlanOperState.setStatus(_A)
_CucsVmVlanPolicyOwner_Type=CucsFabricVnetEpPolicyOwner
_CucsVmVlanPolicyOwner_Object=MibTableColumn
cucsVmVlanPolicyOwner=_CucsVmVlanPolicyOwner_Object((1,3,6,1,4,1,9,9,719,1,52,12,1,20),_CucsVmVlanPolicyOwner_Type())
cucsVmVlanPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmVlanPolicyOwner.setStatus(_A)
_CucsVmVlanAssocPrimaryVlanState_Type=CucsFabricVlanAssocPrimaryVlanState
_CucsVmVlanAssocPrimaryVlanState_Object=MibTableColumn
cucsVmVlanAssocPrimaryVlanState=_CucsVmVlanAssocPrimaryVlanState_Object((1,3,6,1,4,1,9,9,719,1,52,12,1,21),_CucsVmVlanAssocPrimaryVlanState_Type())
cucsVmVlanAssocPrimaryVlanState.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmVlanAssocPrimaryVlanState.setStatus(_A)
_CucsVmVlanAssocPrimaryVlanSwitchId_Type=CucsFabricAVlanAssocPrimaryVlanSwitchId
_CucsVmVlanAssocPrimaryVlanSwitchId_Object=MibTableColumn
cucsVmVlanAssocPrimaryVlanSwitchId=_CucsVmVlanAssocPrimaryVlanSwitchId_Object((1,3,6,1,4,1,9,9,719,1,52,12,1,22),_CucsVmVlanAssocPrimaryVlanSwitchId_Type())
cucsVmVlanAssocPrimaryVlanSwitchId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmVlanAssocPrimaryVlanSwitchId.setStatus(_A)
_CucsVmVlanOverlapStateForA_Type=CucsFabricVlanOverlapState
_CucsVmVlanOverlapStateForA_Object=MibTableColumn
cucsVmVlanOverlapStateForA=_CucsVmVlanOverlapStateForA_Object((1,3,6,1,4,1,9,9,719,1,52,12,1,23),_CucsVmVlanOverlapStateForA_Type())
cucsVmVlanOverlapStateForA.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmVlanOverlapStateForA.setStatus(_A)
_CucsVmVlanOverlapStateForB_Type=CucsFabricVlanOverlapState
_CucsVmVlanOverlapStateForB_Object=MibTableColumn
cucsVmVlanOverlapStateForB=_CucsVmVlanOverlapStateForB_Object((1,3,6,1,4,1,9,9,719,1,52,12,1,24),_CucsVmVlanOverlapStateForB_Type())
cucsVmVlanOverlapStateForB.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmVlanOverlapStateForB.setStatus(_A)
_CucsVmVnicProfClTable_Object=MibTable
cucsVmVnicProfClTable=_CucsVmVnicProfClTable_Object((1,3,6,1,4,1,9,9,719,1,52,13))
if mibBuilder.loadTexts:cucsVmVnicProfClTable.setStatus(_A)
_CucsVmVnicProfClEntry_Object=MibTableRow
cucsVmVnicProfClEntry=_CucsVmVnicProfClEntry_Object((1,3,6,1,4,1,9,9,719,1,52,13,1))
cucsVmVnicProfClEntry.setIndexNames((0,_C,_Q))
if mibBuilder.loadTexts:cucsVmVnicProfClEntry.setStatus(_A)
_CucsVmVnicProfClInstanceId_Type=CucsManagedObjectId
_CucsVmVnicProfClInstanceId_Object=MibTableColumn
cucsVmVnicProfClInstanceId=_CucsVmVnicProfClInstanceId_Object((1,3,6,1,4,1,9,9,719,1,52,13,1,1),_CucsVmVnicProfClInstanceId_Type())
cucsVmVnicProfClInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsVmVnicProfClInstanceId.setStatus(_A)
_CucsVmVnicProfClDn_Type=CucsManagedObjectDn
_CucsVmVnicProfClDn_Object=MibTableColumn
cucsVmVnicProfClDn=_CucsVmVnicProfClDn_Object((1,3,6,1,4,1,9,9,719,1,52,13,1,2),_CucsVmVnicProfClDn_Type())
cucsVmVnicProfClDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmVnicProfClDn.setStatus(_A)
_CucsVmVnicProfClRn_Type=SnmpAdminString
_CucsVmVnicProfClRn_Object=MibTableColumn
cucsVmVnicProfClRn=_CucsVmVnicProfClRn_Object((1,3,6,1,4,1,9,9,719,1,52,13,1,3),_CucsVmVnicProfClRn_Type())
cucsVmVnicProfClRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmVnicProfClRn.setStatus(_A)
_CucsVmVnicProfClDcName_Type=SnmpAdminString
_CucsVmVnicProfClDcName_Object=MibTableColumn
cucsVmVnicProfClDcName=_CucsVmVnicProfClDcName_Object((1,3,6,1,4,1,9,9,719,1,52,13,1,4),_CucsVmVnicProfClDcName_Type())
cucsVmVnicProfClDcName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmVnicProfClDcName.setStatus(_A)
_CucsVmVnicProfClDescr_Type=SnmpAdminString
_CucsVmVnicProfClDescr_Object=MibTableColumn
cucsVmVnicProfClDescr=_CucsVmVnicProfClDescr_Object((1,3,6,1,4,1,9,9,719,1,52,13,1,5),_CucsVmVnicProfClDescr_Type())
cucsVmVnicProfClDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmVnicProfClDescr.setStatus(_A)
_CucsVmVnicProfClIntId_Type=SnmpAdminString
_CucsVmVnicProfClIntId_Object=MibTableColumn
cucsVmVnicProfClIntId=_CucsVmVnicProfClIntId_Object((1,3,6,1,4,1,9,9,719,1,52,13,1,6),_CucsVmVnicProfClIntId_Type())
cucsVmVnicProfClIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmVnicProfClIntId.setStatus(_A)
_CucsVmVnicProfClName_Type=SnmpAdminString
_CucsVmVnicProfClName_Object=MibTableColumn
cucsVmVnicProfClName=_CucsVmVnicProfClName_Object((1,3,6,1,4,1,9,9,719,1,52,13,1,7),_CucsVmVnicProfClName_Type())
cucsVmVnicProfClName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmVnicProfClName.setStatus(_A)
_CucsVmVnicProfClOrgPath_Type=SnmpAdminString
_CucsVmVnicProfClOrgPath_Object=MibTableColumn
cucsVmVnicProfClOrgPath=_CucsVmVnicProfClOrgPath_Object((1,3,6,1,4,1,9,9,719,1,52,13,1,8),_CucsVmVnicProfClOrgPath_Type())
cucsVmVnicProfClOrgPath.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmVnicProfClOrgPath.setStatus(_A)
_CucsVmVnicProfClSwName_Type=SnmpAdminString
_CucsVmVnicProfClSwName_Object=MibTableColumn
cucsVmVnicProfClSwName=_CucsVmVnicProfClSwName_Object((1,3,6,1,4,1,9,9,719,1,52,13,1,9),_CucsVmVnicProfClSwName_Type())
cucsVmVnicProfClSwName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmVnicProfClSwName.setStatus(_A)
_CucsVmVnicProfClPolicyLevel_Type=Gauge32
_CucsVmVnicProfClPolicyLevel_Object=MibTableColumn
cucsVmVnicProfClPolicyLevel=_CucsVmVnicProfClPolicyLevel_Object((1,3,6,1,4,1,9,9,719,1,52,13,1,10),_CucsVmVnicProfClPolicyLevel_Type())
cucsVmVnicProfClPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmVnicProfClPolicyLevel.setStatus(_A)
_CucsVmVnicProfClPolicyOwner_Type=CucsPolicyPolicyOwner
_CucsVmVnicProfClPolicyOwner_Object=MibTableColumn
cucsVmVnicProfClPolicyOwner=_CucsVmVnicProfClPolicyOwner_Object((1,3,6,1,4,1,9,9,719,1,52,13,1,11),_CucsVmVnicProfClPolicyOwner_Type())
cucsVmVnicProfClPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmVnicProfClPolicyOwner.setStatus(_A)
_CucsVmVnicProfInstTable_Object=MibTable
cucsVmVnicProfInstTable=_CucsVmVnicProfInstTable_Object((1,3,6,1,4,1,9,9,719,1,52,14))
if mibBuilder.loadTexts:cucsVmVnicProfInstTable.setStatus(_A)
_CucsVmVnicProfInstEntry_Object=MibTableRow
cucsVmVnicProfInstEntry=_CucsVmVnicProfInstEntry_Object((1,3,6,1,4,1,9,9,719,1,52,14,1))
cucsVmVnicProfInstEntry.setIndexNames((0,_C,_R))
if mibBuilder.loadTexts:cucsVmVnicProfInstEntry.setStatus(_A)
_CucsVmVnicProfInstInstanceId_Type=CucsManagedObjectId
_CucsVmVnicProfInstInstanceId_Object=MibTableColumn
cucsVmVnicProfInstInstanceId=_CucsVmVnicProfInstInstanceId_Object((1,3,6,1,4,1,9,9,719,1,52,14,1,1),_CucsVmVnicProfInstInstanceId_Type())
cucsVmVnicProfInstInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsVmVnicProfInstInstanceId.setStatus(_A)
_CucsVmVnicProfInstDn_Type=CucsManagedObjectDn
_CucsVmVnicProfInstDn_Object=MibTableColumn
cucsVmVnicProfInstDn=_CucsVmVnicProfInstDn_Object((1,3,6,1,4,1,9,9,719,1,52,14,1,2),_CucsVmVnicProfInstDn_Type())
cucsVmVnicProfInstDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmVnicProfInstDn.setStatus(_A)
_CucsVmVnicProfInstRn_Type=SnmpAdminString
_CucsVmVnicProfInstRn_Object=MibTableColumn
cucsVmVnicProfInstRn=_CucsVmVnicProfInstRn_Object((1,3,6,1,4,1,9,9,719,1,52,14,1,3),_CucsVmVnicProfInstRn_Type())
cucsVmVnicProfInstRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmVnicProfInstRn.setStatus(_A)
_CucsVmVnicProfInstDescr_Type=SnmpAdminString
_CucsVmVnicProfInstDescr_Object=MibTableColumn
cucsVmVnicProfInstDescr=_CucsVmVnicProfInstDescr_Object((1,3,6,1,4,1,9,9,719,1,52,14,1,4),_CucsVmVnicProfInstDescr_Type())
cucsVmVnicProfInstDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmVnicProfInstDescr.setStatus(_A)
_CucsVmVnicProfInstIntId_Type=SnmpAdminString
_CucsVmVnicProfInstIntId_Object=MibTableColumn
cucsVmVnicProfInstIntId=_CucsVmVnicProfInstIntId_Object((1,3,6,1,4,1,9,9,719,1,52,14,1,5),_CucsVmVnicProfInstIntId_Type())
cucsVmVnicProfInstIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmVnicProfInstIntId.setStatus(_A)
_CucsVmVnicProfInstMaxPorts_Type=Gauge32
_CucsVmVnicProfInstMaxPorts_Object=MibTableColumn
cucsVmVnicProfInstMaxPorts=_CucsVmVnicProfInstMaxPorts_Object((1,3,6,1,4,1,9,9,719,1,52,14,1,6),_CucsVmVnicProfInstMaxPorts_Type())
cucsVmVnicProfInstMaxPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmVnicProfInstMaxPorts.setStatus(_A)
_CucsVmVnicProfInstName_Type=SnmpAdminString
_CucsVmVnicProfInstName_Object=MibTableColumn
cucsVmVnicProfInstName=_CucsVmVnicProfInstName_Object((1,3,6,1,4,1,9,9,719,1,52,14,1,7),_CucsVmVnicProfInstName_Type())
cucsVmVnicProfInstName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmVnicProfInstName.setStatus(_A)
_CucsVmVnicProfInstProfDn_Type=SnmpAdminString
_CucsVmVnicProfInstProfDn_Object=MibTableColumn
cucsVmVnicProfInstProfDn=_CucsVmVnicProfInstProfDn_Object((1,3,6,1,4,1,9,9,719,1,52,14,1,8),_CucsVmVnicProfInstProfDn_Type())
cucsVmVnicProfInstProfDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmVnicProfInstProfDn.setStatus(_A)
_CucsVmVnicProfInstPolicyLevel_Type=Gauge32
_CucsVmVnicProfInstPolicyLevel_Object=MibTableColumn
cucsVmVnicProfInstPolicyLevel=_CucsVmVnicProfInstPolicyLevel_Object((1,3,6,1,4,1,9,9,719,1,52,14,1,9),_CucsVmVnicProfInstPolicyLevel_Type())
cucsVmVnicProfInstPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmVnicProfInstPolicyLevel.setStatus(_A)
_CucsVmVnicProfInstPolicyOwner_Type=CucsPolicyPolicyOwner
_CucsVmVnicProfInstPolicyOwner_Object=MibTableColumn
cucsVmVnicProfInstPolicyOwner=_CucsVmVnicProfInstPolicyOwner_Object((1,3,6,1,4,1,9,9,719,1,52,14,1,10),_CucsVmVnicProfInstPolicyOwner_Type())
cucsVmVnicProfInstPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmVnicProfInstPolicyOwner.setStatus(_A)
_CucsVmVnicProfInstProfileType_Type=CucsVnicPortProfileType
_CucsVmVnicProfInstProfileType_Object=MibTableColumn
cucsVmVnicProfInstProfileType=_CucsVmVnicProfInstProfileType_Object((1,3,6,1,4,1,9,9,719,1,52,14,1,11),_CucsVmVnicProfInstProfileType_Type())
cucsVmVnicProfInstProfileType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmVnicProfInstProfileType.setStatus(_A)
_CucsVmVsanTable_Object=MibTable
cucsVmVsanTable=_CucsVmVsanTable_Object((1,3,6,1,4,1,9,9,719,1,52,15))
if mibBuilder.loadTexts:cucsVmVsanTable.setStatus(_A)
_CucsVmVsanEntry_Object=MibTableRow
cucsVmVsanEntry=_CucsVmVsanEntry_Object((1,3,6,1,4,1,9,9,719,1,52,15,1))
cucsVmVsanEntry.setIndexNames((0,_C,_S))
if mibBuilder.loadTexts:cucsVmVsanEntry.setStatus(_A)
_CucsVmVsanInstanceId_Type=CucsManagedObjectId
_CucsVmVsanInstanceId_Object=MibTableColumn
cucsVmVsanInstanceId=_CucsVmVsanInstanceId_Object((1,3,6,1,4,1,9,9,719,1,52,15,1,1),_CucsVmVsanInstanceId_Type())
cucsVmVsanInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsVmVsanInstanceId.setStatus(_A)
_CucsVmVsanDn_Type=CucsManagedObjectDn
_CucsVmVsanDn_Object=MibTableColumn
cucsVmVsanDn=_CucsVmVsanDn_Object((1,3,6,1,4,1,9,9,719,1,52,15,1,2),_CucsVmVsanDn_Type())
cucsVmVsanDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmVsanDn.setStatus(_A)
_CucsVmVsanRn_Type=SnmpAdminString
_CucsVmVsanRn_Object=MibTableColumn
cucsVmVsanRn=_CucsVmVsanRn_Object((1,3,6,1,4,1,9,9,719,1,52,15,1,3),_CucsVmVsanRn_Type())
cucsVmVsanRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmVsanRn.setStatus(_A)
_CucsVmVsanEpDn_Type=SnmpAdminString
_CucsVmVsanEpDn_Object=MibTableColumn
cucsVmVsanEpDn=_CucsVmVsanEpDn_Object((1,3,6,1,4,1,9,9,719,1,52,15,1,4),_CucsVmVsanEpDn_Type())
cucsVmVsanEpDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmVsanEpDn.setStatus(_A)
_CucsVmVsanFcoeVlan_Type=Gauge32
_CucsVmVsanFcoeVlan_Object=MibTableColumn
cucsVmVsanFcoeVlan=_CucsVmVsanFcoeVlan_Object((1,3,6,1,4,1,9,9,719,1,52,15,1,5),_CucsVmVsanFcoeVlan_Type())
cucsVmVsanFcoeVlan.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmVsanFcoeVlan.setStatus(_A)
_CucsVmVsanId_Type=Gauge32
_CucsVmVsanId_Object=MibTableColumn
cucsVmVsanId=_CucsVmVsanId_Object((1,3,6,1,4,1,9,9,719,1,52,15,1,6),_CucsVmVsanId_Type())
cucsVmVsanId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmVsanId.setStatus(_A)
_CucsVmVsanIfRole_Type=CucsFabricVnetEpIfRole
_CucsVmVsanIfRole_Object=MibTableColumn
cucsVmVsanIfRole=_CucsVmVsanIfRole_Object((1,3,6,1,4,1,9,9,719,1,52,15,1,7),_CucsVmVsanIfRole_Type())
cucsVmVsanIfRole.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmVsanIfRole.setStatus(_A)
_CucsVmVsanIfType_Type=CucsNetworkVnetEpIfType
_CucsVmVsanIfType_Object=MibTableColumn
cucsVmVsanIfType=_CucsVmVsanIfType_Object((1,3,6,1,4,1,9,9,719,1,52,15,1,8),_CucsVmVsanIfType_Type())
cucsVmVsanIfType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmVsanIfType.setStatus(_A)
_CucsVmVsanLocale_Type=CucsFabricVnetEpLocale
_CucsVmVsanLocale_Object=MibTableColumn
cucsVmVsanLocale=_CucsVmVsanLocale_Object((1,3,6,1,4,1,9,9,719,1,52,15,1,9),_CucsVmVsanLocale_Type())
cucsVmVsanLocale.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmVsanLocale.setStatus(_A)
_CucsVmVsanName_Type=SnmpAdminString
_CucsVmVsanName_Object=MibTableColumn
cucsVmVsanName=_CucsVmVsanName_Object((1,3,6,1,4,1,9,9,719,1,52,15,1,10),_CucsVmVsanName_Type())
cucsVmVsanName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmVsanName.setStatus(_A)
_CucsVmVsanPeerDn_Type=SnmpAdminString
_CucsVmVsanPeerDn_Object=MibTableColumn
cucsVmVsanPeerDn=_CucsVmVsanPeerDn_Object((1,3,6,1,4,1,9,9,719,1,52,15,1,11),_CucsVmVsanPeerDn_Type())
cucsVmVsanPeerDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmVsanPeerDn.setStatus(_A)
_CucsVmVsanSwitchId_Type=CucsNetworkSwitchId
_CucsVmVsanSwitchId_Object=MibTableColumn
cucsVmVsanSwitchId=_CucsVmVsanSwitchId_Object((1,3,6,1,4,1,9,9,719,1,52,15,1,12),_CucsVmVsanSwitchId_Type())
cucsVmVsanSwitchId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmVsanSwitchId.setStatus(_A)
_CucsVmVsanTransport_Type=CucsFabricAVsanTransport
_CucsVmVsanTransport_Object=MibTableColumn
cucsVmVsanTransport=_CucsVmVsanTransport_Object((1,3,6,1,4,1,9,9,719,1,52,15,1,13),_CucsVmVsanTransport_Type())
cucsVmVsanTransport.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmVsanTransport.setStatus(_A)
_CucsVmVsanType_Type=CucsFabricAVsanType
_CucsVmVsanType_Object=MibTableColumn
cucsVmVsanType=_CucsVmVsanType_Object((1,3,6,1,4,1,9,9,719,1,52,15,1,14),_CucsVmVsanType_Type())
cucsVmVsanType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmVsanType.setStatus(_A)
_CucsVmVsanOperState_Type=CucsFabricVsanOperState
_CucsVmVsanOperState_Object=MibTableColumn
cucsVmVsanOperState=_CucsVmVsanOperState_Object((1,3,6,1,4,1,9,9,719,1,52,15,1,15),_CucsVmVsanOperState_Type())
cucsVmVsanOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmVsanOperState.setStatus(_A)
_CucsVmVsanZoningState_Type=CucsFabricZoningState
_CucsVmVsanZoningState_Object=MibTableColumn
cucsVmVsanZoningState=_CucsVmVsanZoningState_Object((1,3,6,1,4,1,9,9,719,1,52,15,1,16),_CucsVmVsanZoningState_Type())
cucsVmVsanZoningState.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmVsanZoningState.setStatus(_A)
_CucsVmVsanPolicyOwner_Type=CucsFabricVnetEpPolicyOwner
_CucsVmVsanPolicyOwner_Object=MibTableColumn
cucsVmVsanPolicyOwner=_CucsVmVsanPolicyOwner_Object((1,3,6,1,4,1,9,9,719,1,52,15,1,18),_CucsVmVsanPolicyOwner_Type())
cucsVmVsanPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmVsanPolicyOwner.setStatus(_A)
_CucsVmComputeEpTable_Object=MibTable
cucsVmComputeEpTable=_CucsVmComputeEpTable_Object((1,3,6,1,4,1,9,9,719,1,52,16))
if mibBuilder.loadTexts:cucsVmComputeEpTable.setStatus(_A)
_CucsVmComputeEpEntry_Object=MibTableRow
cucsVmComputeEpEntry=_CucsVmComputeEpEntry_Object((1,3,6,1,4,1,9,9,719,1,52,16,1))
cucsVmComputeEpEntry.setIndexNames((0,_C,_T))
if mibBuilder.loadTexts:cucsVmComputeEpEntry.setStatus(_A)
_CucsVmComputeEpInstanceId_Type=CucsManagedObjectId
_CucsVmComputeEpInstanceId_Object=MibTableColumn
cucsVmComputeEpInstanceId=_CucsVmComputeEpInstanceId_Object((1,3,6,1,4,1,9,9,719,1,52,16,1,1),_CucsVmComputeEpInstanceId_Type())
cucsVmComputeEpInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsVmComputeEpInstanceId.setStatus(_A)
_CucsVmComputeEpDn_Type=CucsManagedObjectDn
_CucsVmComputeEpDn_Object=MibTableColumn
cucsVmComputeEpDn=_CucsVmComputeEpDn_Object((1,3,6,1,4,1,9,9,719,1,52,16,1,2),_CucsVmComputeEpDn_Type())
cucsVmComputeEpDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmComputeEpDn.setStatus(_A)
_CucsVmComputeEpRn_Type=SnmpAdminString
_CucsVmComputeEpRn_Object=MibTableColumn
cucsVmComputeEpRn=_CucsVmComputeEpRn_Object((1,3,6,1,4,1,9,9,719,1,52,16,1,3),_CucsVmComputeEpRn_Type())
cucsVmComputeEpRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmComputeEpRn.setStatus(_A)
_CucsVmComputeEpClInstType_Type=CucsVmComputeEpClInstType
_CucsVmComputeEpClInstType_Object=MibTableColumn
cucsVmComputeEpClInstType=_CucsVmComputeEpClInstType_Object((1,3,6,1,4,1,9,9,719,1,52,16,1,4),_CucsVmComputeEpClInstType_Type())
cucsVmComputeEpClInstType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmComputeEpClInstType.setStatus(_A)
_CucsVmComputeEpComputeEpVendor_Type=SnmpAdminString
_CucsVmComputeEpComputeEpVendor_Object=MibTableColumn
cucsVmComputeEpComputeEpVendor=_CucsVmComputeEpComputeEpVendor_Object((1,3,6,1,4,1,9,9,719,1,52,16,1,5),_CucsVmComputeEpComputeEpVendor_Type())
cucsVmComputeEpComputeEpVendor.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmComputeEpComputeEpVendor.setStatus(_A)
_CucsVmComputeEpDescr_Type=SnmpAdminString
_CucsVmComputeEpDescr_Object=MibTableColumn
cucsVmComputeEpDescr=_CucsVmComputeEpDescr_Object((1,3,6,1,4,1,9,9,719,1,52,16,1,6),_CucsVmComputeEpDescr_Type())
cucsVmComputeEpDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmComputeEpDescr.setStatus(_A)
_CucsVmComputeEpDvsDn_Type=SnmpAdminString
_CucsVmComputeEpDvsDn_Object=MibTableColumn
cucsVmComputeEpDvsDn=_CucsVmComputeEpDvsDn_Object((1,3,6,1,4,1,9,9,719,1,52,16,1,7),_CucsVmComputeEpDvsDn_Type())
cucsVmComputeEpDvsDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmComputeEpDvsDn.setStatus(_A)
_CucsVmComputeEpDvsName_Type=SnmpAdminString
_CucsVmComputeEpDvsName_Object=MibTableColumn
cucsVmComputeEpDvsName=_CucsVmComputeEpDvsName_Object((1,3,6,1,4,1,9,9,719,1,52,16,1,8),_CucsVmComputeEpDvsName_Type())
cucsVmComputeEpDvsName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmComputeEpDvsName.setStatus(_A)
_CucsVmComputeEpHostName_Type=SnmpAdminString
_CucsVmComputeEpHostName_Object=MibTableColumn
cucsVmComputeEpHostName=_CucsVmComputeEpHostName_Object((1,3,6,1,4,1,9,9,719,1,52,16,1,9),_CucsVmComputeEpHostName_Type())
cucsVmComputeEpHostName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmComputeEpHostName.setStatus(_A)
_CucsVmComputeEpIntId_Type=SnmpAdminString
_CucsVmComputeEpIntId_Object=MibTableColumn
cucsVmComputeEpIntId=_CucsVmComputeEpIntId_Object((1,3,6,1,4,1,9,9,719,1,52,16,1,10),_CucsVmComputeEpIntId_Type())
cucsVmComputeEpIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmComputeEpIntId.setStatus(_A)
_CucsVmComputeEpLsDn_Type=SnmpAdminString
_CucsVmComputeEpLsDn_Object=MibTableColumn
cucsVmComputeEpLsDn=_CucsVmComputeEpLsDn_Object((1,3,6,1,4,1,9,9,719,1,52,16,1,11),_CucsVmComputeEpLsDn_Type())
cucsVmComputeEpLsDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmComputeEpLsDn.setStatus(_A)
_CucsVmComputeEpModel_Type=CucsOsOsType
_CucsVmComputeEpModel_Object=MibTableColumn
cucsVmComputeEpModel=_CucsVmComputeEpModel_Object((1,3,6,1,4,1,9,9,719,1,52,16,1,12),_CucsVmComputeEpModel_Type())
cucsVmComputeEpModel.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmComputeEpModel.setStatus(_A)
_CucsVmComputeEpName_Type=SnmpAdminString
_CucsVmComputeEpName_Object=MibTableColumn
cucsVmComputeEpName=_CucsVmComputeEpName_Object((1,3,6,1,4,1,9,9,719,1,52,16,1,13),_CucsVmComputeEpName_Type())
cucsVmComputeEpName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmComputeEpName.setStatus(_A)
_CucsVmComputeEpPnDn_Type=SnmpAdminString
_CucsVmComputeEpPnDn_Object=MibTableColumn
cucsVmComputeEpPnDn=_CucsVmComputeEpPnDn_Object((1,3,6,1,4,1,9,9,719,1,52,16,1,14),_CucsVmComputeEpPnDn_Type())
cucsVmComputeEpPnDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmComputeEpPnDn.setStatus(_A)
_CucsVmComputeEpStatusChangeTs_Type=DateAndTime
_CucsVmComputeEpStatusChangeTs_Object=MibTableColumn
cucsVmComputeEpStatusChangeTs=_CucsVmComputeEpStatusChangeTs_Object((1,3,6,1,4,1,9,9,719,1,52,16,1,15),_CucsVmComputeEpStatusChangeTs_Type())
cucsVmComputeEpStatusChangeTs.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmComputeEpStatusChangeTs.setStatus(_A)
_CucsVmComputeEpUuid_Type=SnmpAdminString
_CucsVmComputeEpUuid_Object=MibTableColumn
cucsVmComputeEpUuid=_CucsVmComputeEpUuid_Object((1,3,6,1,4,1,9,9,719,1,52,16,1,16),_CucsVmComputeEpUuid_Type())
cucsVmComputeEpUuid.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmComputeEpUuid.setStatus(_A)
_CucsVmComputeEpVStatus_Type=CucsVmStatus
_CucsVmComputeEpVStatus_Object=MibTableColumn
cucsVmComputeEpVStatus=_CucsVmComputeEpVStatus_Object((1,3,6,1,4,1,9,9,719,1,52,16,1,17),_CucsVmComputeEpVStatus_Type())
cucsVmComputeEpVStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmComputeEpVStatus.setStatus(_A)
_CucsVmComputeEpVendor_Type=CucsVmOsHvVendor
_CucsVmComputeEpVendor_Object=MibTableColumn
cucsVmComputeEpVendor=_CucsVmComputeEpVendor_Object((1,3,6,1,4,1,9,9,719,1,52,16,1,18),_CucsVmComputeEpVendor_Type())
cucsVmComputeEpVendor.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmComputeEpVendor.setStatus(_A)
_CucsVmComputeEpPolicyLevel_Type=Gauge32
_CucsVmComputeEpPolicyLevel_Object=MibTableColumn
cucsVmComputeEpPolicyLevel=_CucsVmComputeEpPolicyLevel_Object((1,3,6,1,4,1,9,9,719,1,52,16,1,19),_CucsVmComputeEpPolicyLevel_Type())
cucsVmComputeEpPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmComputeEpPolicyLevel.setStatus(_A)
_CucsVmComputeEpPolicyOwner_Type=CucsPolicyPolicyOwner
_CucsVmComputeEpPolicyOwner_Object=MibTableColumn
cucsVmComputeEpPolicyOwner=_CucsVmComputeEpPolicyOwner_Object((1,3,6,1,4,1,9,9,719,1,52,16,1,20),_CucsVmComputeEpPolicyOwner_Type())
cucsVmComputeEpPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmComputeEpPolicyOwner.setStatus(_A)
_CucsVmLifeCyclePolicyFsmTaskTable_Object=MibTable
cucsVmLifeCyclePolicyFsmTaskTable=_CucsVmLifeCyclePolicyFsmTaskTable_Object((1,3,6,1,4,1,9,9,719,1,52,17))
if mibBuilder.loadTexts:cucsVmLifeCyclePolicyFsmTaskTable.setStatus(_A)
_CucsVmLifeCyclePolicyFsmTaskEntry_Object=MibTableRow
cucsVmLifeCyclePolicyFsmTaskEntry=_CucsVmLifeCyclePolicyFsmTaskEntry_Object((1,3,6,1,4,1,9,9,719,1,52,17,1))
cucsVmLifeCyclePolicyFsmTaskEntry.setIndexNames((0,_C,_U))
if mibBuilder.loadTexts:cucsVmLifeCyclePolicyFsmTaskEntry.setStatus(_A)
_CucsVmLifeCyclePolicyFsmTaskInstanceId_Type=CucsManagedObjectId
_CucsVmLifeCyclePolicyFsmTaskInstanceId_Object=MibTableColumn
cucsVmLifeCyclePolicyFsmTaskInstanceId=_CucsVmLifeCyclePolicyFsmTaskInstanceId_Object((1,3,6,1,4,1,9,9,719,1,52,17,1,1),_CucsVmLifeCyclePolicyFsmTaskInstanceId_Type())
cucsVmLifeCyclePolicyFsmTaskInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsVmLifeCyclePolicyFsmTaskInstanceId.setStatus(_A)
_CucsVmLifeCyclePolicyFsmTaskDn_Type=CucsManagedObjectDn
_CucsVmLifeCyclePolicyFsmTaskDn_Object=MibTableColumn
cucsVmLifeCyclePolicyFsmTaskDn=_CucsVmLifeCyclePolicyFsmTaskDn_Object((1,3,6,1,4,1,9,9,719,1,52,17,1,2),_CucsVmLifeCyclePolicyFsmTaskDn_Type())
cucsVmLifeCyclePolicyFsmTaskDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmLifeCyclePolicyFsmTaskDn.setStatus(_A)
_CucsVmLifeCyclePolicyFsmTaskRn_Type=SnmpAdminString
_CucsVmLifeCyclePolicyFsmTaskRn_Object=MibTableColumn
cucsVmLifeCyclePolicyFsmTaskRn=_CucsVmLifeCyclePolicyFsmTaskRn_Object((1,3,6,1,4,1,9,9,719,1,52,17,1,3),_CucsVmLifeCyclePolicyFsmTaskRn_Type())
cucsVmLifeCyclePolicyFsmTaskRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmLifeCyclePolicyFsmTaskRn.setStatus(_A)
_CucsVmLifeCyclePolicyFsmTaskCompletion_Type=CucsFsmCompletion
_CucsVmLifeCyclePolicyFsmTaskCompletion_Object=MibTableColumn
cucsVmLifeCyclePolicyFsmTaskCompletion=_CucsVmLifeCyclePolicyFsmTaskCompletion_Object((1,3,6,1,4,1,9,9,719,1,52,17,1,4),_CucsVmLifeCyclePolicyFsmTaskCompletion_Type())
cucsVmLifeCyclePolicyFsmTaskCompletion.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmLifeCyclePolicyFsmTaskCompletion.setStatus(_A)
_CucsVmLifeCyclePolicyFsmTaskFlags_Type=CucsFsmFlags
_CucsVmLifeCyclePolicyFsmTaskFlags_Object=MibTableColumn
cucsVmLifeCyclePolicyFsmTaskFlags=_CucsVmLifeCyclePolicyFsmTaskFlags_Object((1,3,6,1,4,1,9,9,719,1,52,17,1,5),_CucsVmLifeCyclePolicyFsmTaskFlags_Type())
cucsVmLifeCyclePolicyFsmTaskFlags.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmLifeCyclePolicyFsmTaskFlags.setStatus(_A)
_CucsVmLifeCyclePolicyFsmTaskItem_Type=CucsVmLifeCyclePolicyFsmTaskItem
_CucsVmLifeCyclePolicyFsmTaskItem_Object=MibTableColumn
cucsVmLifeCyclePolicyFsmTaskItem=_CucsVmLifeCyclePolicyFsmTaskItem_Object((1,3,6,1,4,1,9,9,719,1,52,17,1,6),_CucsVmLifeCyclePolicyFsmTaskItem_Type())
cucsVmLifeCyclePolicyFsmTaskItem.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmLifeCyclePolicyFsmTaskItem.setStatus(_A)
_CucsVmLifeCyclePolicyFsmTaskSeqId_Type=Gauge32
_CucsVmLifeCyclePolicyFsmTaskSeqId_Object=MibTableColumn
cucsVmLifeCyclePolicyFsmTaskSeqId=_CucsVmLifeCyclePolicyFsmTaskSeqId_Object((1,3,6,1,4,1,9,9,719,1,52,17,1,7),_CucsVmLifeCyclePolicyFsmTaskSeqId_Type())
cucsVmLifeCyclePolicyFsmTaskSeqId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmLifeCyclePolicyFsmTaskSeqId.setStatus(_A)
_CucsVmLifeCyclePolicyFsmTable_Object=MibTable
cucsVmLifeCyclePolicyFsmTable=_CucsVmLifeCyclePolicyFsmTable_Object((1,3,6,1,4,1,9,9,719,1,52,18))
if mibBuilder.loadTexts:cucsVmLifeCyclePolicyFsmTable.setStatus(_A)
_CucsVmLifeCyclePolicyFsmEntry_Object=MibTableRow
cucsVmLifeCyclePolicyFsmEntry=_CucsVmLifeCyclePolicyFsmEntry_Object((1,3,6,1,4,1,9,9,719,1,52,18,1))
cucsVmLifeCyclePolicyFsmEntry.setIndexNames((0,_C,_V))
if mibBuilder.loadTexts:cucsVmLifeCyclePolicyFsmEntry.setStatus(_A)
_CucsVmLifeCyclePolicyFsmInstanceId_Type=CucsManagedObjectId
_CucsVmLifeCyclePolicyFsmInstanceId_Object=MibTableColumn
cucsVmLifeCyclePolicyFsmInstanceId=_CucsVmLifeCyclePolicyFsmInstanceId_Object((1,3,6,1,4,1,9,9,719,1,52,18,1,1),_CucsVmLifeCyclePolicyFsmInstanceId_Type())
cucsVmLifeCyclePolicyFsmInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsVmLifeCyclePolicyFsmInstanceId.setStatus(_A)
_CucsVmLifeCyclePolicyFsmDn_Type=CucsManagedObjectDn
_CucsVmLifeCyclePolicyFsmDn_Object=MibTableColumn
cucsVmLifeCyclePolicyFsmDn=_CucsVmLifeCyclePolicyFsmDn_Object((1,3,6,1,4,1,9,9,719,1,52,18,1,2),_CucsVmLifeCyclePolicyFsmDn_Type())
cucsVmLifeCyclePolicyFsmDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmLifeCyclePolicyFsmDn.setStatus(_A)
_CucsVmLifeCyclePolicyFsmRn_Type=SnmpAdminString
_CucsVmLifeCyclePolicyFsmRn_Object=MibTableColumn
cucsVmLifeCyclePolicyFsmRn=_CucsVmLifeCyclePolicyFsmRn_Object((1,3,6,1,4,1,9,9,719,1,52,18,1,3),_CucsVmLifeCyclePolicyFsmRn_Type())
cucsVmLifeCyclePolicyFsmRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmLifeCyclePolicyFsmRn.setStatus(_A)
_CucsVmLifeCyclePolicyFsmCompletionTime_Type=DateAndTime
_CucsVmLifeCyclePolicyFsmCompletionTime_Object=MibTableColumn
cucsVmLifeCyclePolicyFsmCompletionTime=_CucsVmLifeCyclePolicyFsmCompletionTime_Object((1,3,6,1,4,1,9,9,719,1,52,18,1,4),_CucsVmLifeCyclePolicyFsmCompletionTime_Type())
cucsVmLifeCyclePolicyFsmCompletionTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmLifeCyclePolicyFsmCompletionTime.setStatus(_A)
_CucsVmLifeCyclePolicyFsmCurrentFsm_Type=CucsVmLifeCyclePolicyFsmCurrentFsm
_CucsVmLifeCyclePolicyFsmCurrentFsm_Object=MibTableColumn
cucsVmLifeCyclePolicyFsmCurrentFsm=_CucsVmLifeCyclePolicyFsmCurrentFsm_Object((1,3,6,1,4,1,9,9,719,1,52,18,1,5),_CucsVmLifeCyclePolicyFsmCurrentFsm_Type())
cucsVmLifeCyclePolicyFsmCurrentFsm.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmLifeCyclePolicyFsmCurrentFsm.setStatus(_A)
_CucsVmLifeCyclePolicyFsmDescrData_Type=SnmpAdminString
_CucsVmLifeCyclePolicyFsmDescrData_Object=MibTableColumn
cucsVmLifeCyclePolicyFsmDescrData=_CucsVmLifeCyclePolicyFsmDescrData_Object((1,3,6,1,4,1,9,9,719,1,52,18,1,6),_CucsVmLifeCyclePolicyFsmDescrData_Type())
cucsVmLifeCyclePolicyFsmDescrData.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmLifeCyclePolicyFsmDescrData.setStatus(_A)
_CucsVmLifeCyclePolicyFsmFsmStatus_Type=CucsFsmFsmStageStatus
_CucsVmLifeCyclePolicyFsmFsmStatus_Object=MibTableColumn
cucsVmLifeCyclePolicyFsmFsmStatus=_CucsVmLifeCyclePolicyFsmFsmStatus_Object((1,3,6,1,4,1,9,9,719,1,52,18,1,7),_CucsVmLifeCyclePolicyFsmFsmStatus_Type())
cucsVmLifeCyclePolicyFsmFsmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmLifeCyclePolicyFsmFsmStatus.setStatus(_A)
_CucsVmLifeCyclePolicyFsmProgress_Type=Gauge32
_CucsVmLifeCyclePolicyFsmProgress_Object=MibTableColumn
cucsVmLifeCyclePolicyFsmProgress=_CucsVmLifeCyclePolicyFsmProgress_Object((1,3,6,1,4,1,9,9,719,1,52,18,1,8),_CucsVmLifeCyclePolicyFsmProgress_Type())
cucsVmLifeCyclePolicyFsmProgress.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmLifeCyclePolicyFsmProgress.setStatus(_A)
_CucsVmLifeCyclePolicyFsmRmtErrCode_Type=Gauge32
_CucsVmLifeCyclePolicyFsmRmtErrCode_Object=MibTableColumn
cucsVmLifeCyclePolicyFsmRmtErrCode=_CucsVmLifeCyclePolicyFsmRmtErrCode_Object((1,3,6,1,4,1,9,9,719,1,52,18,1,9),_CucsVmLifeCyclePolicyFsmRmtErrCode_Type())
cucsVmLifeCyclePolicyFsmRmtErrCode.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmLifeCyclePolicyFsmRmtErrCode.setStatus(_A)
_CucsVmLifeCyclePolicyFsmRmtErrDescr_Type=SnmpAdminString
_CucsVmLifeCyclePolicyFsmRmtErrDescr_Object=MibTableColumn
cucsVmLifeCyclePolicyFsmRmtErrDescr=_CucsVmLifeCyclePolicyFsmRmtErrDescr_Object((1,3,6,1,4,1,9,9,719,1,52,18,1,10),_CucsVmLifeCyclePolicyFsmRmtErrDescr_Type())
cucsVmLifeCyclePolicyFsmRmtErrDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmLifeCyclePolicyFsmRmtErrDescr.setStatus(_A)
_CucsVmLifeCyclePolicyFsmRmtRslt_Type=CucsConditionRemoteInvRslt
_CucsVmLifeCyclePolicyFsmRmtRslt_Object=MibTableColumn
cucsVmLifeCyclePolicyFsmRmtRslt=_CucsVmLifeCyclePolicyFsmRmtRslt_Object((1,3,6,1,4,1,9,9,719,1,52,18,1,11),_CucsVmLifeCyclePolicyFsmRmtRslt_Type())
cucsVmLifeCyclePolicyFsmRmtRslt.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmLifeCyclePolicyFsmRmtRslt.setStatus(_A)
_CucsVmLifeCyclePolicyFsmStageTable_Object=MibTable
cucsVmLifeCyclePolicyFsmStageTable=_CucsVmLifeCyclePolicyFsmStageTable_Object((1,3,6,1,4,1,9,9,719,1,52,19))
if mibBuilder.loadTexts:cucsVmLifeCyclePolicyFsmStageTable.setStatus(_A)
_CucsVmLifeCyclePolicyFsmStageEntry_Object=MibTableRow
cucsVmLifeCyclePolicyFsmStageEntry=_CucsVmLifeCyclePolicyFsmStageEntry_Object((1,3,6,1,4,1,9,9,719,1,52,19,1))
cucsVmLifeCyclePolicyFsmStageEntry.setIndexNames((0,_C,_W))
if mibBuilder.loadTexts:cucsVmLifeCyclePolicyFsmStageEntry.setStatus(_A)
_CucsVmLifeCyclePolicyFsmStageInstanceId_Type=CucsManagedObjectId
_CucsVmLifeCyclePolicyFsmStageInstanceId_Object=MibTableColumn
cucsVmLifeCyclePolicyFsmStageInstanceId=_CucsVmLifeCyclePolicyFsmStageInstanceId_Object((1,3,6,1,4,1,9,9,719,1,52,19,1,1),_CucsVmLifeCyclePolicyFsmStageInstanceId_Type())
cucsVmLifeCyclePolicyFsmStageInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsVmLifeCyclePolicyFsmStageInstanceId.setStatus(_A)
_CucsVmLifeCyclePolicyFsmStageDn_Type=CucsManagedObjectDn
_CucsVmLifeCyclePolicyFsmStageDn_Object=MibTableColumn
cucsVmLifeCyclePolicyFsmStageDn=_CucsVmLifeCyclePolicyFsmStageDn_Object((1,3,6,1,4,1,9,9,719,1,52,19,1,2),_CucsVmLifeCyclePolicyFsmStageDn_Type())
cucsVmLifeCyclePolicyFsmStageDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmLifeCyclePolicyFsmStageDn.setStatus(_A)
_CucsVmLifeCyclePolicyFsmStageRn_Type=SnmpAdminString
_CucsVmLifeCyclePolicyFsmStageRn_Object=MibTableColumn
cucsVmLifeCyclePolicyFsmStageRn=_CucsVmLifeCyclePolicyFsmStageRn_Object((1,3,6,1,4,1,9,9,719,1,52,19,1,3),_CucsVmLifeCyclePolicyFsmStageRn_Type())
cucsVmLifeCyclePolicyFsmStageRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmLifeCyclePolicyFsmStageRn.setStatus(_A)
_CucsVmLifeCyclePolicyFsmStageDescrData_Type=SnmpAdminString
_CucsVmLifeCyclePolicyFsmStageDescrData_Object=MibTableColumn
cucsVmLifeCyclePolicyFsmStageDescrData=_CucsVmLifeCyclePolicyFsmStageDescrData_Object((1,3,6,1,4,1,9,9,719,1,52,19,1,4),_CucsVmLifeCyclePolicyFsmStageDescrData_Type())
cucsVmLifeCyclePolicyFsmStageDescrData.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmLifeCyclePolicyFsmStageDescrData.setStatus(_A)
_CucsVmLifeCyclePolicyFsmStageLastUpdateTime_Type=DateAndTime
_CucsVmLifeCyclePolicyFsmStageLastUpdateTime_Object=MibTableColumn
cucsVmLifeCyclePolicyFsmStageLastUpdateTime=_CucsVmLifeCyclePolicyFsmStageLastUpdateTime_Object((1,3,6,1,4,1,9,9,719,1,52,19,1,5),_CucsVmLifeCyclePolicyFsmStageLastUpdateTime_Type())
cucsVmLifeCyclePolicyFsmStageLastUpdateTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmLifeCyclePolicyFsmStageLastUpdateTime.setStatus(_A)
_CucsVmLifeCyclePolicyFsmStageName_Type=CucsVmLifeCyclePolicyFsmStageName
_CucsVmLifeCyclePolicyFsmStageName_Object=MibTableColumn
cucsVmLifeCyclePolicyFsmStageName=_CucsVmLifeCyclePolicyFsmStageName_Object((1,3,6,1,4,1,9,9,719,1,52,19,1,6),_CucsVmLifeCyclePolicyFsmStageName_Type())
cucsVmLifeCyclePolicyFsmStageName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmLifeCyclePolicyFsmStageName.setStatus(_A)
_CucsVmLifeCyclePolicyFsmStageOrder_Type=Gauge32
_CucsVmLifeCyclePolicyFsmStageOrder_Object=MibTableColumn
cucsVmLifeCyclePolicyFsmStageOrder=_CucsVmLifeCyclePolicyFsmStageOrder_Object((1,3,6,1,4,1,9,9,719,1,52,19,1,7),_CucsVmLifeCyclePolicyFsmStageOrder_Type())
cucsVmLifeCyclePolicyFsmStageOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmLifeCyclePolicyFsmStageOrder.setStatus(_A)
_CucsVmLifeCyclePolicyFsmStageRetry_Type=Gauge32
_CucsVmLifeCyclePolicyFsmStageRetry_Object=MibTableColumn
cucsVmLifeCyclePolicyFsmStageRetry=_CucsVmLifeCyclePolicyFsmStageRetry_Object((1,3,6,1,4,1,9,9,719,1,52,19,1,8),_CucsVmLifeCyclePolicyFsmStageRetry_Type())
cucsVmLifeCyclePolicyFsmStageRetry.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmLifeCyclePolicyFsmStageRetry.setStatus(_A)
_CucsVmLifeCyclePolicyFsmStageStageStatus_Type=CucsFsmFsmStageStatus
_CucsVmLifeCyclePolicyFsmStageStageStatus_Object=MibTableColumn
cucsVmLifeCyclePolicyFsmStageStageStatus=_CucsVmLifeCyclePolicyFsmStageStageStatus_Object((1,3,6,1,4,1,9,9,719,1,52,19,1,9),_CucsVmLifeCyclePolicyFsmStageStageStatus_Type())
cucsVmLifeCyclePolicyFsmStageStageStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVmLifeCyclePolicyFsmStageStageStatus.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'cucsVmObjects':cucsVmObjects,'cucsVmDCTable':cucsVmDCTable,'cucsVmDCEntry':cucsVmDCEntry,_E:cucsVmDCInstanceId,'cucsVmDCDn':cucsVmDCDn,'cucsVmDCRn':cucsVmDCRn,'cucsVmDCDescr':cucsVmDCDescr,'cucsVmDCIntId':cucsVmDCIntId,'cucsVmDCName':cucsVmDCName,'cucsVmDCOwn':cucsVmDCOwn,'cucsVmDCUuid':cucsVmDCUuid,'cucsVmDCPolicyLevel':cucsVmDCPolicyLevel,'cucsVmDCPolicyOwner':cucsVmDCPolicyOwner,'cucsVmDCOrgTable':cucsVmDCOrgTable,'cucsVmDCOrgEntry':cucsVmDCOrgEntry,_F:cucsVmDCOrgInstanceId,'cucsVmDCOrgDn':cucsVmDCOrgDn,'cucsVmDCOrgRn':cucsVmDCOrgRn,'cucsVmDCOrgDescr':cucsVmDCOrgDescr,'cucsVmDCOrgIntId':cucsVmDCOrgIntId,'cucsVmDCOrgName':cucsVmDCOrgName,'cucsVmDCOrgOwn':cucsVmDCOrgOwn,'cucsVmDCOrgUuid':cucsVmDCOrgUuid,'cucsVmDCOrgPolicyLevel':cucsVmDCOrgPolicyLevel,'cucsVmDCOrgPolicyOwner':cucsVmDCOrgPolicyOwner,'cucsVmEpTable':cucsVmEpTable,'cucsVmEpEntry':cucsVmEpEntry,_G:cucsVmEpInstanceId,'cucsVmEpDn':cucsVmEpDn,'cucsVmEpRn':cucsVmEpRn,'cucsVmHbaTable':cucsVmHbaTable,'cucsVmHbaEntry':cucsVmHbaEntry,_H:cucsVmHbaInstanceId,'cucsVmHbaDn':cucsVmHbaDn,'cucsVmHbaRn':cucsVmHbaRn,'cucsVmHbaDvsPortId':cucsVmHbaDvsPortId,'cucsVmHbaDvsSwitchId':cucsVmHbaDvsSwitchId,'cucsVmHbaHostIfDn':cucsVmHbaHostIfDn,'cucsVmHbaName':cucsVmHbaName,'cucsVmHbaOwner':cucsVmHbaOwner,'cucsVmHbaPhSwitchId':cucsVmHbaPhSwitchId,'cucsVmHbaProfileId':cucsVmHbaProfileId,'cucsVmHbaProfileName':cucsVmHbaProfileName,'cucsVmHbaStatusChangeTs':cucsVmHbaStatusChangeTs,'cucsVmHbaSwitchId':cucsVmHbaSwitchId,'cucsVmHbaType':cucsVmHbaType,'cucsVmHbaUuid':cucsVmHbaUuid,'cucsVmHbaVStatus':cucsVmHbaVStatus,'cucsVmHbaVcDn':cucsVmHbaVcDn,'cucsVmHbaVifId':cucsVmHbaVifId,'cucsVmHbaVnicDn':cucsVmHbaVnicDn,'cucsVmHbaWwnn':cucsVmHbaWwnn,'cucsVmHbaWwpn':cucsVmHbaWwpn,'cucsVmHbaDvsGenPortId':cucsVmHbaDvsGenPortId,'cucsVmHbaVmndGuid':cucsVmHbaVmndGuid,'cucsVmHbaVmndName':cucsVmHbaVmndName,'cucsVmHvTable':cucsVmHvTable,'cucsVmHvEntry':cucsVmHvEntry,_I:cucsVmHvInstanceId,'cucsVmHvDn':cucsVmHvDn,'cucsVmHvRn':cucsVmHvRn,'cucsVmHvDescr':cucsVmHvDescr,'cucsVmHvDvsDn':cucsVmHvDvsDn,'cucsVmHvDvsName':cucsVmHvDvsName,'cucsVmHvFltAggr':cucsVmHvFltAggr,'cucsVmHvIntId':cucsVmHvIntId,'cucsVmHvLsDn':cucsVmHvLsDn,'cucsVmHvName':cucsVmHvName,'cucsVmHvPnDn':cucsVmHvPnDn,'cucsVmHvStatusChangeTs':cucsVmHvStatusChangeTs,'cucsVmHvUuid':cucsVmHvUuid,'cucsVmHvVStatus':cucsVmHvVStatus,'cucsVmHvClInstType':cucsVmHvClInstType,'cucsVmHvHvType':cucsVmHvHvType,'cucsVmHvModel':cucsVmHvModel,'cucsVmHvVendor':cucsVmHvVendor,'cucsVmHvPolicyLevel':cucsVmHvPolicyLevel,'cucsVmHvPolicyOwner':cucsVmHvPolicyOwner,'cucsVmInstanceTable':cucsVmInstanceTable,'cucsVmInstanceEntry':cucsVmInstanceEntry,_J:cucsVmInstanceInstanceId,'cucsVmInstanceDn':cucsVmInstanceDn,'cucsVmInstanceRn':cucsVmInstanceRn,'cucsVmInstanceDescr':cucsVmInstanceDescr,'cucsVmInstanceDvsDn':cucsVmInstanceDvsDn,'cucsVmInstanceDvsName':cucsVmInstanceDvsName,'cucsVmInstanceFltAggr':cucsVmInstanceFltAggr,'cucsVmInstanceHvDn':cucsVmInstanceHvDn,'cucsVmInstanceHvUuid':cucsVmInstanceHvUuid,'cucsVmInstanceIntId':cucsVmInstanceIntId,'cucsVmInstanceLsDn':cucsVmInstanceLsDn,'cucsVmInstanceName':cucsVmInstanceName,'cucsVmInstancePnDn':cucsVmInstancePnDn,'cucsVmInstanceStatusChangeTs':cucsVmInstanceStatusChangeTs,'cucsVmInstanceUuid':cucsVmInstanceUuid,'cucsVmInstanceVStatus':cucsVmInstanceVStatus,'cucsVmInstanceClInstType':cucsVmInstanceClInstType,'cucsVmInstanceHvType':cucsVmInstanceHvType,'cucsVmInstanceModel':cucsVmInstanceModel,'cucsVmInstanceVendor':cucsVmInstanceVendor,'cucsVmInstancePolicyLevel':cucsVmInstancePolicyLevel,'cucsVmInstancePolicyOwner':cucsVmInstancePolicyOwner,'cucsVmLifeCyclePolicyTable':cucsVmLifeCyclePolicyTable,'cucsVmLifeCyclePolicyEntry':cucsVmLifeCyclePolicyEntry,_K:cucsVmLifeCyclePolicyInstanceId,'cucsVmLifeCyclePolicyDn':cucsVmLifeCyclePolicyDn,'cucsVmLifeCyclePolicyRn':cucsVmLifeCyclePolicyRn,'cucsVmLifeCyclePolicyDescr':cucsVmLifeCyclePolicyDescr,'cucsVmLifeCyclePolicyIntId':cucsVmLifeCyclePolicyIntId,'cucsVmLifeCyclePolicyName':cucsVmLifeCyclePolicyName,'cucsVmLifeCyclePolicyVmRetention':cucsVmLifeCyclePolicyVmRetention,'cucsVmLifeCyclePolicyVnicRetention':cucsVmLifeCyclePolicyVnicRetention,'cucsVmLifeCyclePolicyFsmDescr':cucsVmLifeCyclePolicyFsmDescr,'cucsVmLifeCyclePolicyFsmPrev':cucsVmLifeCyclePolicyFsmPrev,'cucsVmLifeCyclePolicyFsmProgr':cucsVmLifeCyclePolicyFsmProgr,'cucsVmLifeCyclePolicyFsmRmtInvErrCode':cucsVmLifeCyclePolicyFsmRmtInvErrCode,'cucsVmLifeCyclePolicyFsmRmtInvErrDescr':cucsVmLifeCyclePolicyFsmRmtInvErrDescr,'cucsVmLifeCyclePolicyFsmRmtInvRslt':cucsVmLifeCyclePolicyFsmRmtInvRslt,'cucsVmLifeCyclePolicyFsmStageDescr':cucsVmLifeCyclePolicyFsmStageDescr,'cucsVmLifeCyclePolicyFsmStamp':cucsVmLifeCyclePolicyFsmStamp,'cucsVmLifeCyclePolicyFsmStatus':cucsVmLifeCyclePolicyFsmStatus,'cucsVmLifeCyclePolicyFsmTry':cucsVmLifeCyclePolicyFsmTry,'cucsVmLifeCyclePolicyPolicyLevel':cucsVmLifeCyclePolicyPolicyLevel,'cucsVmLifeCyclePolicyPolicyOwner':cucsVmLifeCyclePolicyPolicyOwner,'cucsVmNicTable':cucsVmNicTable,'cucsVmNicEntry':cucsVmNicEntry,_L:cucsVmNicInstanceId,'cucsVmNicDn':cucsVmNicDn,'cucsVmNicRn':cucsVmNicRn,'cucsVmNicDvsPortId':cucsVmNicDvsPortId,'cucsVmNicDvsSwitchId':cucsVmNicDvsSwitchId,'cucsVmNicHostIfDn':cucsVmNicHostIfDn,'cucsVmNicMacAddr':cucsVmNicMacAddr,'cucsVmNicName':cucsVmNicName,'cucsVmNicOwner':cucsVmNicOwner,'cucsVmNicPhSwitchId':cucsVmNicPhSwitchId,'cucsVmNicProfileId':cucsVmNicProfileId,'cucsVmNicProfileName':cucsVmNicProfileName,'cucsVmNicStatusChangeTs':cucsVmNicStatusChangeTs,'cucsVmNicSwitchId':cucsVmNicSwitchId,'cucsVmNicType':cucsVmNicType,'cucsVmNicUuid':cucsVmNicUuid,'cucsVmNicVStatus':cucsVmNicVStatus,'cucsVmNicVcDn':cucsVmNicVcDn,'cucsVmNicVifId':cucsVmNicVifId,'cucsVmNicVnicDn':cucsVmNicVnicDn,'cucsVmNicDvsGenPortId':cucsVmNicDvsGenPortId,'cucsVmNicVmndGuid':cucsVmNicVmndGuid,'cucsVmNicVmndName':cucsVmNicVmndName,'cucsVmOrgTable':cucsVmOrgTable,'cucsVmOrgEntry':cucsVmOrgEntry,_M:cucsVmOrgInstanceId,'cucsVmOrgDn':cucsVmOrgDn,'cucsVmOrgRn':cucsVmOrgRn,'cucsVmOrgDescr':cucsVmOrgDescr,'cucsVmOrgIntId':cucsVmOrgIntId,'cucsVmOrgName':cucsVmOrgName,'cucsVmOrgOwn':cucsVmOrgOwn,'cucsVmOrgUuid':cucsVmOrgUuid,'cucsVmOrgPolicyLevel':cucsVmOrgPolicyLevel,'cucsVmOrgPolicyOwner':cucsVmOrgPolicyOwner,'cucsVmSwitchTable':cucsVmSwitchTable,'cucsVmSwitchEntry':cucsVmSwitchEntry,_N:cucsVmSwitchInstanceId,'cucsVmSwitchDn':cucsVmSwitchDn,'cucsVmSwitchRn':cucsVmSwitchRn,'cucsVmSwitchAdminState':cucsVmSwitchAdminState,'cucsVmSwitchDescr':cucsVmSwitchDescr,'cucsVmSwitchExtKey':cucsVmSwitchExtKey,'cucsVmSwitchIntId':cucsVmSwitchIntId,'cucsVmSwitchKeyInst':cucsVmSwitchKeyInst,'cucsVmSwitchName':cucsVmSwitchName,'cucsVmSwitchOwn':cucsVmSwitchOwn,'cucsVmSwitchUuid':cucsVmSwitchUuid,'cucsVmSwitchId':cucsVmSwitchId,'cucsVmSwitchManager':cucsVmSwitchManager,'cucsVmSwitchPolicyLevel':cucsVmSwitchPolicyLevel,'cucsVmSwitchPolicyOwner':cucsVmSwitchPolicyOwner,'cucsVmSwitchFltAggr':cucsVmSwitchFltAggr,'cucsVmSwitchVendor':cucsVmSwitchVendor,'cucsVmVifTable':cucsVmVifTable,'cucsVmVifEntry':cucsVmVifEntry,_O:cucsVmVifInstanceId,'cucsVmVifDn':cucsVmVifDn,'cucsVmVifRn':cucsVmVifRn,'cucsVmVifCookie':cucsVmVifCookie,'cucsVmVifPhSwitchId':cucsVmVifPhSwitchId,'cucsVmVifPhsAccessCardId':cucsVmVifPhsAccessCardId,'cucsVmVifPhsAccessPortId':cucsVmVifPhsAccessPortId,'cucsVmVifPhsBorderCardId':cucsVmVifPhsBorderCardId,'cucsVmVifPhsBorderPortId':cucsVmVifPhsBorderPortId,'cucsVmVifStatusChangeTs':cucsVmVifStatusChangeTs,'cucsVmVifVStatus':cucsVmVifVStatus,'cucsVmVifVcDn':cucsVmVifVcDn,'cucsVmVifVifId':cucsVmVifVifId,'cucsVmVifAdpVifId':cucsVmVifAdpVifId,'cucsVmVifLinkState':cucsVmVifLinkState,'cucsVmVifOperState':cucsVmVifOperState,'cucsVmVifStateQual':cucsVmVifStateQual,'cucsVmVifPhsAccessAggrPortId':cucsVmVifPhsAccessAggrPortId,'cucsVmVifPhsBorderAggrPortId':cucsVmVifPhsBorderAggrPortId,'cucsVmVlanTable':cucsVmVlanTable,'cucsVmVlanEntry':cucsVmVlanEntry,_P:cucsVmVlanInstanceId,'cucsVmVlanDn':cucsVmVlanDn,'cucsVmVlanRn':cucsVmVlanRn,'cucsVmVlanEpDn':cucsVmVlanEpDn,'cucsVmVlanId':cucsVmVlanId,'cucsVmVlanIfRole':cucsVmVlanIfRole,'cucsVmVlanIfType':cucsVmVlanIfType,'cucsVmVlanLocale':cucsVmVlanLocale,'cucsVmVlanName':cucsVmVlanName,'cucsVmVlanPeerDn':cucsVmVlanPeerDn,'cucsVmVlanPubNwDn':cucsVmVlanPubNwDn,'cucsVmVlanPubNwId':cucsVmVlanPubNwId,'cucsVmVlanPubNwName':cucsVmVlanPubNwName,'cucsVmVlanSharing':cucsVmVlanSharing,'cucsVmVlanSwitchId':cucsVmVlanSwitchId,'cucsVmVlanTransport':cucsVmVlanTransport,'cucsVmVlanType':cucsVmVlanType,'cucsVmVlanOperState':cucsVmVlanOperState,'cucsVmVlanPolicyOwner':cucsVmVlanPolicyOwner,'cucsVmVlanAssocPrimaryVlanState':cucsVmVlanAssocPrimaryVlanState,'cucsVmVlanAssocPrimaryVlanSwitchId':cucsVmVlanAssocPrimaryVlanSwitchId,'cucsVmVlanOverlapStateForA':cucsVmVlanOverlapStateForA,'cucsVmVlanOverlapStateForB':cucsVmVlanOverlapStateForB,'cucsVmVnicProfClTable':cucsVmVnicProfClTable,'cucsVmVnicProfClEntry':cucsVmVnicProfClEntry,_Q:cucsVmVnicProfClInstanceId,'cucsVmVnicProfClDn':cucsVmVnicProfClDn,'cucsVmVnicProfClRn':cucsVmVnicProfClRn,'cucsVmVnicProfClDcName':cucsVmVnicProfClDcName,'cucsVmVnicProfClDescr':cucsVmVnicProfClDescr,'cucsVmVnicProfClIntId':cucsVmVnicProfClIntId,'cucsVmVnicProfClName':cucsVmVnicProfClName,'cucsVmVnicProfClOrgPath':cucsVmVnicProfClOrgPath,'cucsVmVnicProfClSwName':cucsVmVnicProfClSwName,'cucsVmVnicProfClPolicyLevel':cucsVmVnicProfClPolicyLevel,'cucsVmVnicProfClPolicyOwner':cucsVmVnicProfClPolicyOwner,'cucsVmVnicProfInstTable':cucsVmVnicProfInstTable,'cucsVmVnicProfInstEntry':cucsVmVnicProfInstEntry,_R:cucsVmVnicProfInstInstanceId,'cucsVmVnicProfInstDn':cucsVmVnicProfInstDn,'cucsVmVnicProfInstRn':cucsVmVnicProfInstRn,'cucsVmVnicProfInstDescr':cucsVmVnicProfInstDescr,'cucsVmVnicProfInstIntId':cucsVmVnicProfInstIntId,'cucsVmVnicProfInstMaxPorts':cucsVmVnicProfInstMaxPorts,'cucsVmVnicProfInstName':cucsVmVnicProfInstName,'cucsVmVnicProfInstProfDn':cucsVmVnicProfInstProfDn,'cucsVmVnicProfInstPolicyLevel':cucsVmVnicProfInstPolicyLevel,'cucsVmVnicProfInstPolicyOwner':cucsVmVnicProfInstPolicyOwner,'cucsVmVnicProfInstProfileType':cucsVmVnicProfInstProfileType,'cucsVmVsanTable':cucsVmVsanTable,'cucsVmVsanEntry':cucsVmVsanEntry,_S:cucsVmVsanInstanceId,'cucsVmVsanDn':cucsVmVsanDn,'cucsVmVsanRn':cucsVmVsanRn,'cucsVmVsanEpDn':cucsVmVsanEpDn,'cucsVmVsanFcoeVlan':cucsVmVsanFcoeVlan,'cucsVmVsanId':cucsVmVsanId,'cucsVmVsanIfRole':cucsVmVsanIfRole,'cucsVmVsanIfType':cucsVmVsanIfType,'cucsVmVsanLocale':cucsVmVsanLocale,'cucsVmVsanName':cucsVmVsanName,'cucsVmVsanPeerDn':cucsVmVsanPeerDn,'cucsVmVsanSwitchId':cucsVmVsanSwitchId,'cucsVmVsanTransport':cucsVmVsanTransport,'cucsVmVsanType':cucsVmVsanType,'cucsVmVsanOperState':cucsVmVsanOperState,'cucsVmVsanZoningState':cucsVmVsanZoningState,'cucsVmVsanPolicyOwner':cucsVmVsanPolicyOwner,'cucsVmComputeEpTable':cucsVmComputeEpTable,'cucsVmComputeEpEntry':cucsVmComputeEpEntry,_T:cucsVmComputeEpInstanceId,'cucsVmComputeEpDn':cucsVmComputeEpDn,'cucsVmComputeEpRn':cucsVmComputeEpRn,'cucsVmComputeEpClInstType':cucsVmComputeEpClInstType,'cucsVmComputeEpComputeEpVendor':cucsVmComputeEpComputeEpVendor,'cucsVmComputeEpDescr':cucsVmComputeEpDescr,'cucsVmComputeEpDvsDn':cucsVmComputeEpDvsDn,'cucsVmComputeEpDvsName':cucsVmComputeEpDvsName,'cucsVmComputeEpHostName':cucsVmComputeEpHostName,'cucsVmComputeEpIntId':cucsVmComputeEpIntId,'cucsVmComputeEpLsDn':cucsVmComputeEpLsDn,'cucsVmComputeEpModel':cucsVmComputeEpModel,'cucsVmComputeEpName':cucsVmComputeEpName,'cucsVmComputeEpPnDn':cucsVmComputeEpPnDn,'cucsVmComputeEpStatusChangeTs':cucsVmComputeEpStatusChangeTs,'cucsVmComputeEpUuid':cucsVmComputeEpUuid,'cucsVmComputeEpVStatus':cucsVmComputeEpVStatus,'cucsVmComputeEpVendor':cucsVmComputeEpVendor,'cucsVmComputeEpPolicyLevel':cucsVmComputeEpPolicyLevel,'cucsVmComputeEpPolicyOwner':cucsVmComputeEpPolicyOwner,'cucsVmLifeCyclePolicyFsmTaskTable':cucsVmLifeCyclePolicyFsmTaskTable,'cucsVmLifeCyclePolicyFsmTaskEntry':cucsVmLifeCyclePolicyFsmTaskEntry,_U:cucsVmLifeCyclePolicyFsmTaskInstanceId,'cucsVmLifeCyclePolicyFsmTaskDn':cucsVmLifeCyclePolicyFsmTaskDn,'cucsVmLifeCyclePolicyFsmTaskRn':cucsVmLifeCyclePolicyFsmTaskRn,'cucsVmLifeCyclePolicyFsmTaskCompletion':cucsVmLifeCyclePolicyFsmTaskCompletion,'cucsVmLifeCyclePolicyFsmTaskFlags':cucsVmLifeCyclePolicyFsmTaskFlags,'cucsVmLifeCyclePolicyFsmTaskItem':cucsVmLifeCyclePolicyFsmTaskItem,'cucsVmLifeCyclePolicyFsmTaskSeqId':cucsVmLifeCyclePolicyFsmTaskSeqId,'cucsVmLifeCyclePolicyFsmTable':cucsVmLifeCyclePolicyFsmTable,'cucsVmLifeCyclePolicyFsmEntry':cucsVmLifeCyclePolicyFsmEntry,_V:cucsVmLifeCyclePolicyFsmInstanceId,'cucsVmLifeCyclePolicyFsmDn':cucsVmLifeCyclePolicyFsmDn,'cucsVmLifeCyclePolicyFsmRn':cucsVmLifeCyclePolicyFsmRn,'cucsVmLifeCyclePolicyFsmCompletionTime':cucsVmLifeCyclePolicyFsmCompletionTime,'cucsVmLifeCyclePolicyFsmCurrentFsm':cucsVmLifeCyclePolicyFsmCurrentFsm,'cucsVmLifeCyclePolicyFsmDescrData':cucsVmLifeCyclePolicyFsmDescrData,'cucsVmLifeCyclePolicyFsmFsmStatus':cucsVmLifeCyclePolicyFsmFsmStatus,'cucsVmLifeCyclePolicyFsmProgress':cucsVmLifeCyclePolicyFsmProgress,'cucsVmLifeCyclePolicyFsmRmtErrCode':cucsVmLifeCyclePolicyFsmRmtErrCode,'cucsVmLifeCyclePolicyFsmRmtErrDescr':cucsVmLifeCyclePolicyFsmRmtErrDescr,'cucsVmLifeCyclePolicyFsmRmtRslt':cucsVmLifeCyclePolicyFsmRmtRslt,'cucsVmLifeCyclePolicyFsmStageTable':cucsVmLifeCyclePolicyFsmStageTable,'cucsVmLifeCyclePolicyFsmStageEntry':cucsVmLifeCyclePolicyFsmStageEntry,_W:cucsVmLifeCyclePolicyFsmStageInstanceId,'cucsVmLifeCyclePolicyFsmStageDn':cucsVmLifeCyclePolicyFsmStageDn,'cucsVmLifeCyclePolicyFsmStageRn':cucsVmLifeCyclePolicyFsmStageRn,'cucsVmLifeCyclePolicyFsmStageDescrData':cucsVmLifeCyclePolicyFsmStageDescrData,'cucsVmLifeCyclePolicyFsmStageLastUpdateTime':cucsVmLifeCyclePolicyFsmStageLastUpdateTime,'cucsVmLifeCyclePolicyFsmStageName':cucsVmLifeCyclePolicyFsmStageName,'cucsVmLifeCyclePolicyFsmStageOrder':cucsVmLifeCyclePolicyFsmStageOrder,'cucsVmLifeCyclePolicyFsmStageRetry':cucsVmLifeCyclePolicyFsmStageRetry,'cucsVmLifeCyclePolicyFsmStageStageStatus':cucsVmLifeCyclePolicyFsmStageStageStatus})