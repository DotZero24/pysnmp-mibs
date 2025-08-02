_AO='cfprVnicWwpnHistoryInstanceId'
_AN='cfprVnicWwnnHistoryInstanceId'
_AM='cfprVnicVnicBehPolicyInstanceId'
_AL='cfprVnicVmqConPolicyRefInstanceId'
_AK='cfprVnicVmqConPolicyInstanceId'
_AJ='cfprVnicVlanInstanceId'
_AI='cfprVnicVhbaBehPolicyInstanceId'
_AH='cfprVnicUsnicConPolicyRefInstanceId'
_AG='cfprVnicUsnicConPolicyInstanceId'
_AF='cfprVnicScsiIfInstanceId'
_AE='cfprVnicScsiInstanceId'
_AD='cfprVnicSanConnTemplInstanceId'
_AC='cfprVnicSanConnPolicyInstanceId'
_AB='cfprVnicRackServerDiscoveryProfileInstanceId'
_AA='cfprVnicProfileSetFsmTaskInstanceId'
_A9='cfprVnicProfileSetFsmStageInstanceId'
_A8='cfprVnicProfileSetFsmInstanceId'
_A7='cfprVnicProfileSetInstanceId'
_A6='cfprVnicProfileRefInstanceId'
_A5='cfprVnicProfileAliasInstanceId'
_A4='cfprVnicProfileInstanceId'
_A3='cfprVnicOProfileAliasInstanceId'
_A2='cfprVnicMacHistoryInstanceId'
_A1='cfprVnicLunInstanceId'
_A0='cfprVnicLifVsanInstanceId'
_z='cfprVnicLifVlanInstanceId'
_y='cfprVnicLanConnTemplInstanceId'
_x='cfprVnicLanConnPolicyInstanceId'
_w='cfprVnicIqnHistoryInstanceId'
_v='cfprVnicIpcIfInstanceId'
_u='cfprVnicIpcInstanceId'
_t='cfprVnicIpV6StaticAddrInstanceId'
_s='cfprVnicIpV6MgmtPooledAddrInstanceId'
_r='cfprVnicIpV6HistoryInstanceId'
_q='cfprVnicIpV4StaticAddrInstanceId'
_p='cfprVnicIpV4ProfDerivedAddrInstanceId'
_o='cfprVnicIpV4PooledAddrInstanceId'
_n='cfprVnicIpV4MgmtPooledAddrInstanceId'
_m='cfprVnicIpV4HistoryInstanceId'
_l='cfprVnicInternalProfileInstanceId'
_k='cfprVnicIScsiStaticTargetIfInstanceId'
_j='cfprVnicIScsiNodeInstanceId'
_i='cfprVnicIScsiLCPInstanceId'
_h='cfprVnicIScsiBootVnicInstanceId'
_g='cfprVnicIScsiBootParamsInstanceId'
_f='cfprVnicIScsiAutoTargetIfInstanceId'
_e='cfprVnicIScsiInstanceId'
_d='cfprVnicIPv4StaticRouteInstanceId'
_c='cfprVnicIPv4PooledIscsiAddrInstanceId'
_b='cfprVnicIPv4IscsiAddrInstanceId'
_a='cfprVnicIPv4IfInstanceId'
_Z='cfprVnicIPv4DnsInstanceId'
_Y='cfprVnicIPv4DhcpInstanceId'
_X='cfprVnicFcOEIfInstanceId'
_W='cfprVnicFcNodeInstanceId'
_V='cfprVnicFcLifInstanceId'
_U='cfprVnicFcIfInstanceId'
_T='cfprVnicFcGroupTemplInstanceId'
_S='cfprVnicFcGroupDefInstanceId'
_R='cfprVnicFcInstanceId'
_Q='cfprVnicEtherIfInstanceId'
_P='cfprVnicEtherInstanceId'
_O='cfprVnicEthLifInstanceId'
_N='cfprVnicDynamicProviderEpInstanceId'
_M='cfprVnicDynamicProviderInstanceId'
_L='cfprVnicDynamicIdUniverseInstanceId'
_K='cfprVnicDynamicConPolicyRefInstanceId'
_J='cfprVnicDynamicConPolicyInstanceId'
_I='cfprVnicDynamicConInstanceId'
_H='cfprVnicDefBehInstanceId'
_G='cfprVnicConnDefInstanceId'
_F='cfprVnicBootTargetInstanceId'
_E='cfprVnicBootIpPolicyInstanceId'
_D='not-accessible'
_C='CISCO-FIREPOWER-VNIC-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
CfprManagedObjectDn,CfprManagedObjectId,ciscoFirepowerMIBObjects=mibBuilder.importSymbols('CISCO-FIREPOWER-MIB','CfprManagedObjectDn','CfprManagedObjectId','ciscoFirepowerMIBObjects')
CfprConditionRemoteInvRslt,CfprDpsecForgedTransmit,CfprFabricHostPortId,CfprFabricSSAPortType,CfprFabricVlanSharingType,CfprFsmCompletion,CfprFsmFlags,CfprFsmFsmStageStatus,CfprLsConfigState,CfprNetworkSwitchId,CfprNwctrlAdminState,CfprNwctrlLinkFailAction,CfprNwctrlRegistrationMode,CfprPolicyPolicyOwner,CfprVmMgmtPlane,CfprVnicAEtherIfType,CfprVnicAFcIfType,CfprVnicAIpcIfType,CfprVnicAScsiIfType,CfprVnicAppRole,CfprVnicConfigIssues,CfprVnicConnectionOwner,CfprVnicConnectionType,CfprVnicDefBehType,CfprVnicDefaultAction,CfprVnicDynamicConReqProtection,CfprVnicEtherBaseSwitchId,CfprVnicEtherType,CfprVnicExternalMgmtIPMode,CfprVnicFcBasePersBind,CfprVnicFcBaseType,CfprVnicFcNodeOwner,CfprVnicHostNwIOPerfPref,CfprVnicIPv4DnsPref,CfprVnicIScsiIfDefType,CfprVnicIScsiNodeOwner,CfprVnicIfOperState,CfprVnicInstantiation,CfprVnicIpcType,CfprVnicL2IfSwitchId,CfprVnicLanConnTemplSwitchId,CfprVnicLunId,CfprVnicPortProfileType,CfprVnicProfileConfigQualifier,CfprVnicProfileSetFsmCurrentFsm,CfprVnicProfileSetFsmStageName,CfprVnicProfileSetFsmTaskItem,CfprVnicSanConnTemplTarget,CfprVnicScsiType,CfprVnicTemplateTarget,CfprVnicTemplateType,CfprVnicVhbaBehPolicyType,CfprVnicVirtualizationPreferenceType,CfprVnicVnicBehPolicyType,CfprVnicVnicBootDev,CfprVnicVnicOperHostPort=mibBuilder.importSymbols('CISCO-FIREPOWER-TC-MIB','CfprConditionRemoteInvRslt','CfprDpsecForgedTransmit','CfprFabricHostPortId','CfprFabricSSAPortType','CfprFabricVlanSharingType','CfprFsmCompletion','CfprFsmFlags','CfprFsmFsmStageStatus','CfprLsConfigState','CfprNetworkSwitchId','CfprNwctrlAdminState','CfprNwctrlLinkFailAction','CfprNwctrlRegistrationMode','CfprPolicyPolicyOwner','CfprVmMgmtPlane','CfprVnicAEtherIfType','CfprVnicAFcIfType','CfprVnicAIpcIfType','CfprVnicAScsiIfType','CfprVnicAppRole','CfprVnicConfigIssues','CfprVnicConnectionOwner','CfprVnicConnectionType','CfprVnicDefBehType','CfprVnicDefaultAction','CfprVnicDynamicConReqProtection','CfprVnicEtherBaseSwitchId','CfprVnicEtherType','CfprVnicExternalMgmtIPMode','CfprVnicFcBasePersBind','CfprVnicFcBaseType','CfprVnicFcNodeOwner','CfprVnicHostNwIOPerfPref','CfprVnicIPv4DnsPref','CfprVnicIScsiIfDefType','CfprVnicIScsiNodeOwner','CfprVnicIfOperState','CfprVnicInstantiation','CfprVnicIpcType','CfprVnicL2IfSwitchId','CfprVnicLanConnTemplSwitchId','CfprVnicLunId','CfprVnicPortProfileType','CfprVnicProfileConfigQualifier','CfprVnicProfileSetFsmCurrentFsm','CfprVnicProfileSetFsmStageName','CfprVnicProfileSetFsmTaskItem','CfprVnicSanConnTemplTarget','CfprVnicScsiType','CfprVnicTemplateTarget','CfprVnicTemplateType','CfprVnicVhbaBehPolicyType','CfprVnicVirtualizationPreferenceType','CfprVnicVnicBehPolicyType','CfprVnicVnicBootDev','CfprVnicVnicOperHostPort')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CiscoAlarmSeverity,CiscoInetAddressMask,CiscoNetworkAddress,TimeIntervalSec,Unsigned64=mibBuilder.importSymbols('CISCO-TC','CiscoAlarmSeverity','CiscoInetAddressMask','CiscoNetworkAddress','TimeIntervalSec','Unsigned64')
InetAddressIPv4,InetAddressIPv6=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressIPv4','InetAddressIPv6')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowPointer,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowPointer','TextualConvention','TimeInterval','TimeStamp','TruthValue')
cfprVnicObjects=ModuleIdentity((1,3,6,1,4,1,9,9,826,1,83))
_CfprVnicBootIpPolicyTable_Object=MibTable
cfprVnicBootIpPolicyTable=_CfprVnicBootIpPolicyTable_Object((1,3,6,1,4,1,9,9,826,1,83,1))
if mibBuilder.loadTexts:cfprVnicBootIpPolicyTable.setStatus(_A)
_CfprVnicBootIpPolicyEntry_Object=MibTableRow
cfprVnicBootIpPolicyEntry=_CfprVnicBootIpPolicyEntry_Object((1,3,6,1,4,1,9,9,826,1,83,1,1))
cfprVnicBootIpPolicyEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:cfprVnicBootIpPolicyEntry.setStatus(_A)
_CfprVnicBootIpPolicyInstanceId_Type=CfprManagedObjectId
_CfprVnicBootIpPolicyInstanceId_Object=MibTableColumn
cfprVnicBootIpPolicyInstanceId=_CfprVnicBootIpPolicyInstanceId_Object((1,3,6,1,4,1,9,9,826,1,83,1,1,1),_CfprVnicBootIpPolicyInstanceId_Type())
cfprVnicBootIpPolicyInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprVnicBootIpPolicyInstanceId.setStatus(_A)
_CfprVnicBootIpPolicyDn_Type=CfprManagedObjectDn
_CfprVnicBootIpPolicyDn_Object=MibTableColumn
cfprVnicBootIpPolicyDn=_CfprVnicBootIpPolicyDn_Object((1,3,6,1,4,1,9,9,826,1,83,1,1,2),_CfprVnicBootIpPolicyDn_Type())
cfprVnicBootIpPolicyDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicBootIpPolicyDn.setStatus(_A)
_CfprVnicBootIpPolicyRn_Type=SnmpAdminString
_CfprVnicBootIpPolicyRn_Object=MibTableColumn
cfprVnicBootIpPolicyRn=_CfprVnicBootIpPolicyRn_Object((1,3,6,1,4,1,9,9,826,1,83,1,1,3),_CfprVnicBootIpPolicyRn_Type())
cfprVnicBootIpPolicyRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicBootIpPolicyRn.setStatus(_A)
_CfprVnicBootIpPolicyDescr_Type=SnmpAdminString
_CfprVnicBootIpPolicyDescr_Object=MibTableColumn
cfprVnicBootIpPolicyDescr=_CfprVnicBootIpPolicyDescr_Object((1,3,6,1,4,1,9,9,826,1,83,1,1,4),_CfprVnicBootIpPolicyDescr_Type())
cfprVnicBootIpPolicyDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicBootIpPolicyDescr.setStatus(_A)
_CfprVnicBootIpPolicyIntId_Type=SnmpAdminString
_CfprVnicBootIpPolicyIntId_Object=MibTableColumn
cfprVnicBootIpPolicyIntId=_CfprVnicBootIpPolicyIntId_Object((1,3,6,1,4,1,9,9,826,1,83,1,1,5),_CfprVnicBootIpPolicyIntId_Type())
cfprVnicBootIpPolicyIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicBootIpPolicyIntId.setStatus(_A)
_CfprVnicBootIpPolicyName_Type=SnmpAdminString
_CfprVnicBootIpPolicyName_Object=MibTableColumn
cfprVnicBootIpPolicyName=_CfprVnicBootIpPolicyName_Object((1,3,6,1,4,1,9,9,826,1,83,1,1,6),_CfprVnicBootIpPolicyName_Type())
cfprVnicBootIpPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicBootIpPolicyName.setStatus(_A)
_CfprVnicBootIpPolicyPolicyLevel_Type=Gauge32
_CfprVnicBootIpPolicyPolicyLevel_Object=MibTableColumn
cfprVnicBootIpPolicyPolicyLevel=_CfprVnicBootIpPolicyPolicyLevel_Object((1,3,6,1,4,1,9,9,826,1,83,1,1,7),_CfprVnicBootIpPolicyPolicyLevel_Type())
cfprVnicBootIpPolicyPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicBootIpPolicyPolicyLevel.setStatus(_A)
_CfprVnicBootIpPolicyPolicyOwner_Type=CfprPolicyPolicyOwner
_CfprVnicBootIpPolicyPolicyOwner_Object=MibTableColumn
cfprVnicBootIpPolicyPolicyOwner=_CfprVnicBootIpPolicyPolicyOwner_Object((1,3,6,1,4,1,9,9,826,1,83,1,1,8),_CfprVnicBootIpPolicyPolicyOwner_Type())
cfprVnicBootIpPolicyPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicBootIpPolicyPolicyOwner.setStatus(_A)
_CfprVnicBootIpPolicyPoolName_Type=SnmpAdminString
_CfprVnicBootIpPolicyPoolName_Object=MibTableColumn
cfprVnicBootIpPolicyPoolName=_CfprVnicBootIpPolicyPoolName_Object((1,3,6,1,4,1,9,9,826,1,83,1,1,9),_CfprVnicBootIpPolicyPoolName_Type())
cfprVnicBootIpPolicyPoolName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicBootIpPolicyPoolName.setStatus(_A)
_CfprVnicBootTargetTable_Object=MibTable
cfprVnicBootTargetTable=_CfprVnicBootTargetTable_Object((1,3,6,1,4,1,9,9,826,1,83,2))
if mibBuilder.loadTexts:cfprVnicBootTargetTable.setStatus(_A)
_CfprVnicBootTargetEntry_Object=MibTableRow
cfprVnicBootTargetEntry=_CfprVnicBootTargetEntry_Object((1,3,6,1,4,1,9,9,826,1,83,2,1))
cfprVnicBootTargetEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:cfprVnicBootTargetEntry.setStatus(_A)
_CfprVnicBootTargetInstanceId_Type=CfprManagedObjectId
_CfprVnicBootTargetInstanceId_Object=MibTableColumn
cfprVnicBootTargetInstanceId=_CfprVnicBootTargetInstanceId_Object((1,3,6,1,4,1,9,9,826,1,83,2,1,1),_CfprVnicBootTargetInstanceId_Type())
cfprVnicBootTargetInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprVnicBootTargetInstanceId.setStatus(_A)
_CfprVnicBootTargetDn_Type=CfprManagedObjectDn
_CfprVnicBootTargetDn_Object=MibTableColumn
cfprVnicBootTargetDn=_CfprVnicBootTargetDn_Object((1,3,6,1,4,1,9,9,826,1,83,2,1,2),_CfprVnicBootTargetDn_Type())
cfprVnicBootTargetDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicBootTargetDn.setStatus(_A)
_CfprVnicBootTargetRn_Type=SnmpAdminString
_CfprVnicBootTargetRn_Object=MibTableColumn
cfprVnicBootTargetRn=_CfprVnicBootTargetRn_Object((1,3,6,1,4,1,9,9,826,1,83,2,1,3),_CfprVnicBootTargetRn_Type())
cfprVnicBootTargetRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicBootTargetRn.setStatus(_A)
_CfprVnicBootTargetLun_Type=SnmpAdminString
_CfprVnicBootTargetLun_Object=MibTableColumn
cfprVnicBootTargetLun=_CfprVnicBootTargetLun_Object((1,3,6,1,4,1,9,9,826,1,83,2,1,4),_CfprVnicBootTargetLun_Type())
cfprVnicBootTargetLun.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicBootTargetLun.setStatus(_A)
_CfprVnicBootTargetWwn_Type=Unsigned64
_CfprVnicBootTargetWwn_Object=MibTableColumn
cfprVnicBootTargetWwn=_CfprVnicBootTargetWwn_Object((1,3,6,1,4,1,9,9,826,1,83,2,1,5),_CfprVnicBootTargetWwn_Type())
cfprVnicBootTargetWwn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicBootTargetWwn.setStatus(_A)
_CfprVnicConnDefTable_Object=MibTable
cfprVnicConnDefTable=_CfprVnicConnDefTable_Object((1,3,6,1,4,1,9,9,826,1,83,3))
if mibBuilder.loadTexts:cfprVnicConnDefTable.setStatus(_A)
_CfprVnicConnDefEntry_Object=MibTableRow
cfprVnicConnDefEntry=_CfprVnicConnDefEntry_Object((1,3,6,1,4,1,9,9,826,1,83,3,1))
cfprVnicConnDefEntry.setIndexNames((0,_C,_G))
if mibBuilder.loadTexts:cfprVnicConnDefEntry.setStatus(_A)
_CfprVnicConnDefInstanceId_Type=CfprManagedObjectId
_CfprVnicConnDefInstanceId_Object=MibTableColumn
cfprVnicConnDefInstanceId=_CfprVnicConnDefInstanceId_Object((1,3,6,1,4,1,9,9,826,1,83,3,1,1),_CfprVnicConnDefInstanceId_Type())
cfprVnicConnDefInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprVnicConnDefInstanceId.setStatus(_A)
_CfprVnicConnDefDn_Type=CfprManagedObjectDn
_CfprVnicConnDefDn_Object=MibTableColumn
cfprVnicConnDefDn=_CfprVnicConnDefDn_Object((1,3,6,1,4,1,9,9,826,1,83,3,1,2),_CfprVnicConnDefDn_Type())
cfprVnicConnDefDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicConnDefDn.setStatus(_A)
_CfprVnicConnDefRn_Type=SnmpAdminString
_CfprVnicConnDefRn_Object=MibTableColumn
cfprVnicConnDefRn=_CfprVnicConnDefRn_Object((1,3,6,1,4,1,9,9,826,1,83,3,1,3),_CfprVnicConnDefRn_Type())
cfprVnicConnDefRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicConnDefRn.setStatus(_A)
_CfprVnicConnDefFltAggr_Type=Unsigned64
_CfprVnicConnDefFltAggr_Object=MibTableColumn
cfprVnicConnDefFltAggr=_CfprVnicConnDefFltAggr_Object((1,3,6,1,4,1,9,9,826,1,83,3,1,4),_CfprVnicConnDefFltAggr_Type())
cfprVnicConnDefFltAggr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicConnDefFltAggr.setStatus(_A)
_CfprVnicConnDefLanConnPolicyName_Type=SnmpAdminString
_CfprVnicConnDefLanConnPolicyName_Object=MibTableColumn
cfprVnicConnDefLanConnPolicyName=_CfprVnicConnDefLanConnPolicyName_Object((1,3,6,1,4,1,9,9,826,1,83,3,1,5),_CfprVnicConnDefLanConnPolicyName_Type())
cfprVnicConnDefLanConnPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicConnDefLanConnPolicyName.setStatus(_A)
_CfprVnicConnDefOperLanConnPolicyName_Type=SnmpAdminString
_CfprVnicConnDefOperLanConnPolicyName_Object=MibTableColumn
cfprVnicConnDefOperLanConnPolicyName=_CfprVnicConnDefOperLanConnPolicyName_Object((1,3,6,1,4,1,9,9,826,1,83,3,1,6),_CfprVnicConnDefOperLanConnPolicyName_Type())
cfprVnicConnDefOperLanConnPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicConnDefOperLanConnPolicyName.setStatus(_A)
_CfprVnicConnDefOperSanConnPolicyName_Type=SnmpAdminString
_CfprVnicConnDefOperSanConnPolicyName_Object=MibTableColumn
cfprVnicConnDefOperSanConnPolicyName=_CfprVnicConnDefOperSanConnPolicyName_Object((1,3,6,1,4,1,9,9,826,1,83,3,1,7),_CfprVnicConnDefOperSanConnPolicyName_Type())
cfprVnicConnDefOperSanConnPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicConnDefOperSanConnPolicyName.setStatus(_A)
_CfprVnicConnDefSanConnPolicyName_Type=SnmpAdminString
_CfprVnicConnDefSanConnPolicyName_Object=MibTableColumn
cfprVnicConnDefSanConnPolicyName=_CfprVnicConnDefSanConnPolicyName_Object((1,3,6,1,4,1,9,9,826,1,83,3,1,8),_CfprVnicConnDefSanConnPolicyName_Type())
cfprVnicConnDefSanConnPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicConnDefSanConnPolicyName.setStatus(_A)
_CfprVnicDefBehTable_Object=MibTable
cfprVnicDefBehTable=_CfprVnicDefBehTable_Object((1,3,6,1,4,1,9,9,826,1,83,4))
if mibBuilder.loadTexts:cfprVnicDefBehTable.setStatus(_A)
_CfprVnicDefBehEntry_Object=MibTableRow
cfprVnicDefBehEntry=_CfprVnicDefBehEntry_Object((1,3,6,1,4,1,9,9,826,1,83,4,1))
cfprVnicDefBehEntry.setIndexNames((0,_C,_H))
if mibBuilder.loadTexts:cfprVnicDefBehEntry.setStatus(_A)
_CfprVnicDefBehInstanceId_Type=CfprManagedObjectId
_CfprVnicDefBehInstanceId_Object=MibTableColumn
cfprVnicDefBehInstanceId=_CfprVnicDefBehInstanceId_Object((1,3,6,1,4,1,9,9,826,1,83,4,1,1),_CfprVnicDefBehInstanceId_Type())
cfprVnicDefBehInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprVnicDefBehInstanceId.setStatus(_A)
_CfprVnicDefBehDn_Type=CfprManagedObjectDn
_CfprVnicDefBehDn_Object=MibTableColumn
cfprVnicDefBehDn=_CfprVnicDefBehDn_Object((1,3,6,1,4,1,9,9,826,1,83,4,1,2),_CfprVnicDefBehDn_Type())
cfprVnicDefBehDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicDefBehDn.setStatus(_A)
_CfprVnicDefBehRn_Type=SnmpAdminString
_CfprVnicDefBehRn_Object=MibTableColumn
cfprVnicDefBehRn=_CfprVnicDefBehRn_Object((1,3,6,1,4,1,9,9,826,1,83,4,1,3),_CfprVnicDefBehRn_Type())
cfprVnicDefBehRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicDefBehRn.setStatus(_A)
_CfprVnicDefBehAction_Type=CfprVnicDefaultAction
_CfprVnicDefBehAction_Object=MibTableColumn
cfprVnicDefBehAction=_CfprVnicDefBehAction_Object((1,3,6,1,4,1,9,9,826,1,83,4,1,4),_CfprVnicDefBehAction_Type())
cfprVnicDefBehAction.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicDefBehAction.setStatus(_A)
_CfprVnicDefBehDescr_Type=SnmpAdminString
_CfprVnicDefBehDescr_Object=MibTableColumn
cfprVnicDefBehDescr=_CfprVnicDefBehDescr_Object((1,3,6,1,4,1,9,9,826,1,83,4,1,5),_CfprVnicDefBehDescr_Type())
cfprVnicDefBehDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicDefBehDescr.setStatus(_A)
_CfprVnicDefBehIntId_Type=SnmpAdminString
_CfprVnicDefBehIntId_Object=MibTableColumn
cfprVnicDefBehIntId=_CfprVnicDefBehIntId_Object((1,3,6,1,4,1,9,9,826,1,83,4,1,6),_CfprVnicDefBehIntId_Type())
cfprVnicDefBehIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicDefBehIntId.setStatus(_A)
_CfprVnicDefBehName_Type=SnmpAdminString
_CfprVnicDefBehName_Object=MibTableColumn
cfprVnicDefBehName=_CfprVnicDefBehName_Object((1,3,6,1,4,1,9,9,826,1,83,4,1,7),_CfprVnicDefBehName_Type())
cfprVnicDefBehName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicDefBehName.setStatus(_A)
_CfprVnicDefBehNwTemplName_Type=SnmpAdminString
_CfprVnicDefBehNwTemplName_Object=MibTableColumn
cfprVnicDefBehNwTemplName=_CfprVnicDefBehNwTemplName_Object((1,3,6,1,4,1,9,9,826,1,83,4,1,8),_CfprVnicDefBehNwTemplName_Type())
cfprVnicDefBehNwTemplName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicDefBehNwTemplName.setStatus(_A)
_CfprVnicDefBehPolicyLevel_Type=Gauge32
_CfprVnicDefBehPolicyLevel_Object=MibTableColumn
cfprVnicDefBehPolicyLevel=_CfprVnicDefBehPolicyLevel_Object((1,3,6,1,4,1,9,9,826,1,83,4,1,9),_CfprVnicDefBehPolicyLevel_Type())
cfprVnicDefBehPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicDefBehPolicyLevel.setStatus(_A)
_CfprVnicDefBehPolicyOwner_Type=CfprPolicyPolicyOwner
_CfprVnicDefBehPolicyOwner_Object=MibTableColumn
cfprVnicDefBehPolicyOwner=_CfprVnicDefBehPolicyOwner_Object((1,3,6,1,4,1,9,9,826,1,83,4,1,10),_CfprVnicDefBehPolicyOwner_Type())
cfprVnicDefBehPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicDefBehPolicyOwner.setStatus(_A)
_CfprVnicDefBehType_Type=CfprVnicDefBehType
_CfprVnicDefBehType_Object=MibTableColumn
cfprVnicDefBehType=_CfprVnicDefBehType_Object((1,3,6,1,4,1,9,9,826,1,83,4,1,11),_CfprVnicDefBehType_Type())
cfprVnicDefBehType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicDefBehType.setStatus(_A)
_CfprVnicDynamicConTable_Object=MibTable
cfprVnicDynamicConTable=_CfprVnicDynamicConTable_Object((1,3,6,1,4,1,9,9,826,1,83,5))
if mibBuilder.loadTexts:cfprVnicDynamicConTable.setStatus(_A)
_CfprVnicDynamicConEntry_Object=MibTableRow
cfprVnicDynamicConEntry=_CfprVnicDynamicConEntry_Object((1,3,6,1,4,1,9,9,826,1,83,5,1))
cfprVnicDynamicConEntry.setIndexNames((0,_C,_I))
if mibBuilder.loadTexts:cfprVnicDynamicConEntry.setStatus(_A)
_CfprVnicDynamicConInstanceId_Type=CfprManagedObjectId
_CfprVnicDynamicConInstanceId_Object=MibTableColumn
cfprVnicDynamicConInstanceId=_CfprVnicDynamicConInstanceId_Object((1,3,6,1,4,1,9,9,826,1,83,5,1,1),_CfprVnicDynamicConInstanceId_Type())
cfprVnicDynamicConInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprVnicDynamicConInstanceId.setStatus(_A)
_CfprVnicDynamicConDn_Type=CfprManagedObjectDn
_CfprVnicDynamicConDn_Object=MibTableColumn
cfprVnicDynamicConDn=_CfprVnicDynamicConDn_Object((1,3,6,1,4,1,9,9,826,1,83,5,1,2),_CfprVnicDynamicConDn_Type())
cfprVnicDynamicConDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicDynamicConDn.setStatus(_A)
_CfprVnicDynamicConRn_Type=SnmpAdminString
_CfprVnicDynamicConRn_Object=MibTableColumn
cfprVnicDynamicConRn=_CfprVnicDynamicConRn_Object((1,3,6,1,4,1,9,9,826,1,83,5,1,3),_CfprVnicDynamicConRn_Type())
cfprVnicDynamicConRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicDynamicConRn.setStatus(_A)
_CfprVnicDynamicConAdaptorProfileName_Type=SnmpAdminString
_CfprVnicDynamicConAdaptorProfileName_Object=MibTableColumn
cfprVnicDynamicConAdaptorProfileName=_CfprVnicDynamicConAdaptorProfileName_Object((1,3,6,1,4,1,9,9,826,1,83,5,1,4),_CfprVnicDynamicConAdaptorProfileName_Type())
cfprVnicDynamicConAdaptorProfileName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicDynamicConAdaptorProfileName.setStatus(_A)
_CfprVnicDynamicConDescr_Type=SnmpAdminString
_CfprVnicDynamicConDescr_Object=MibTableColumn
cfprVnicDynamicConDescr=_CfprVnicDynamicConDescr_Object((1,3,6,1,4,1,9,9,826,1,83,5,1,5),_CfprVnicDynamicConDescr_Type())
cfprVnicDynamicConDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicDynamicConDescr.setStatus(_A)
_CfprVnicDynamicConDynamicEth_Type=Gauge32
_CfprVnicDynamicConDynamicEth_Object=MibTableColumn
cfprVnicDynamicConDynamicEth=_CfprVnicDynamicConDynamicEth_Object((1,3,6,1,4,1,9,9,826,1,83,5,1,6),_CfprVnicDynamicConDynamicEth_Type())
cfprVnicDynamicConDynamicEth.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicDynamicConDynamicEth.setStatus(_A)
_CfprVnicDynamicConIntId_Type=SnmpAdminString
_CfprVnicDynamicConIntId_Object=MibTableColumn
cfprVnicDynamicConIntId=_CfprVnicDynamicConIntId_Object((1,3,6,1,4,1,9,9,826,1,83,5,1,7),_CfprVnicDynamicConIntId_Type())
cfprVnicDynamicConIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicDynamicConIntId.setStatus(_A)
_CfprVnicDynamicConMtu_Type=Gauge32
_CfprVnicDynamicConMtu_Object=MibTableColumn
cfprVnicDynamicConMtu=_CfprVnicDynamicConMtu_Object((1,3,6,1,4,1,9,9,826,1,83,5,1,8),_CfprVnicDynamicConMtu_Type())
cfprVnicDynamicConMtu.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicDynamicConMtu.setStatus(_A)
_CfprVnicDynamicConName_Type=SnmpAdminString
_CfprVnicDynamicConName_Object=MibTableColumn
cfprVnicDynamicConName=_CfprVnicDynamicConName_Object((1,3,6,1,4,1,9,9,826,1,83,5,1,9),_CfprVnicDynamicConName_Type())
cfprVnicDynamicConName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicDynamicConName.setStatus(_A)
_CfprVnicDynamicConNamingPrefix_Type=SnmpAdminString
_CfprVnicDynamicConNamingPrefix_Object=MibTableColumn
cfprVnicDynamicConNamingPrefix=_CfprVnicDynamicConNamingPrefix_Object((1,3,6,1,4,1,9,9,826,1,83,5,1,10),_CfprVnicDynamicConNamingPrefix_Type())
cfprVnicDynamicConNamingPrefix.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicDynamicConNamingPrefix.setStatus(_A)
_CfprVnicDynamicConPolicyLevel_Type=Gauge32
_CfprVnicDynamicConPolicyLevel_Object=MibTableColumn
cfprVnicDynamicConPolicyLevel=_CfprVnicDynamicConPolicyLevel_Object((1,3,6,1,4,1,9,9,826,1,83,5,1,11),_CfprVnicDynamicConPolicyLevel_Type())
cfprVnicDynamicConPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicDynamicConPolicyLevel.setStatus(_A)
_CfprVnicDynamicConPolicyOwner_Type=CfprPolicyPolicyOwner
_CfprVnicDynamicConPolicyOwner_Object=MibTableColumn
cfprVnicDynamicConPolicyOwner=_CfprVnicDynamicConPolicyOwner_Object((1,3,6,1,4,1,9,9,826,1,83,5,1,12),_CfprVnicDynamicConPolicyOwner_Type())
cfprVnicDynamicConPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicDynamicConPolicyOwner.setStatus(_A)
_CfprVnicDynamicConProtection_Type=CfprVnicDynamicConReqProtection
_CfprVnicDynamicConProtection_Object=MibTableColumn
cfprVnicDynamicConProtection=_CfprVnicDynamicConProtection_Object((1,3,6,1,4,1,9,9,826,1,83,5,1,13),_CfprVnicDynamicConProtection_Type())
cfprVnicDynamicConProtection.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicDynamicConProtection.setStatus(_A)
_CfprVnicDynamicConPolicyTable_Object=MibTable
cfprVnicDynamicConPolicyTable=_CfprVnicDynamicConPolicyTable_Object((1,3,6,1,4,1,9,9,826,1,83,6))
if mibBuilder.loadTexts:cfprVnicDynamicConPolicyTable.setStatus(_A)
_CfprVnicDynamicConPolicyEntry_Object=MibTableRow
cfprVnicDynamicConPolicyEntry=_CfprVnicDynamicConPolicyEntry_Object((1,3,6,1,4,1,9,9,826,1,83,6,1))
cfprVnicDynamicConPolicyEntry.setIndexNames((0,_C,_J))
if mibBuilder.loadTexts:cfprVnicDynamicConPolicyEntry.setStatus(_A)
_CfprVnicDynamicConPolicyInstanceId_Type=CfprManagedObjectId
_CfprVnicDynamicConPolicyInstanceId_Object=MibTableColumn
cfprVnicDynamicConPolicyInstanceId=_CfprVnicDynamicConPolicyInstanceId_Object((1,3,6,1,4,1,9,9,826,1,83,6,1,1),_CfprVnicDynamicConPolicyInstanceId_Type())
cfprVnicDynamicConPolicyInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprVnicDynamicConPolicyInstanceId.setStatus(_A)
_CfprVnicDynamicConPolicyDn_Type=CfprManagedObjectDn
_CfprVnicDynamicConPolicyDn_Object=MibTableColumn
cfprVnicDynamicConPolicyDn=_CfprVnicDynamicConPolicyDn_Object((1,3,6,1,4,1,9,9,826,1,83,6,1,2),_CfprVnicDynamicConPolicyDn_Type())
cfprVnicDynamicConPolicyDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicDynamicConPolicyDn.setStatus(_A)
_CfprVnicDynamicConPolicyRn_Type=SnmpAdminString
_CfprVnicDynamicConPolicyRn_Object=MibTableColumn
cfprVnicDynamicConPolicyRn=_CfprVnicDynamicConPolicyRn_Object((1,3,6,1,4,1,9,9,826,1,83,6,1,3),_CfprVnicDynamicConPolicyRn_Type())
cfprVnicDynamicConPolicyRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicDynamicConPolicyRn.setStatus(_A)
_CfprVnicDynamicConPolicyAdaptorProfileName_Type=SnmpAdminString
_CfprVnicDynamicConPolicyAdaptorProfileName_Object=MibTableColumn
cfprVnicDynamicConPolicyAdaptorProfileName=_CfprVnicDynamicConPolicyAdaptorProfileName_Object((1,3,6,1,4,1,9,9,826,1,83,6,1,4),_CfprVnicDynamicConPolicyAdaptorProfileName_Type())
cfprVnicDynamicConPolicyAdaptorProfileName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicDynamicConPolicyAdaptorProfileName.setStatus(_A)
_CfprVnicDynamicConPolicyDescr_Type=SnmpAdminString
_CfprVnicDynamicConPolicyDescr_Object=MibTableColumn
cfprVnicDynamicConPolicyDescr=_CfprVnicDynamicConPolicyDescr_Object((1,3,6,1,4,1,9,9,826,1,83,6,1,5),_CfprVnicDynamicConPolicyDescr_Type())
cfprVnicDynamicConPolicyDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicDynamicConPolicyDescr.setStatus(_A)
_CfprVnicDynamicConPolicyDynamicEth_Type=Gauge32
_CfprVnicDynamicConPolicyDynamicEth_Object=MibTableColumn
cfprVnicDynamicConPolicyDynamicEth=_CfprVnicDynamicConPolicyDynamicEth_Object((1,3,6,1,4,1,9,9,826,1,83,6,1,6),_CfprVnicDynamicConPolicyDynamicEth_Type())
cfprVnicDynamicConPolicyDynamicEth.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicDynamicConPolicyDynamicEth.setStatus(_A)
_CfprVnicDynamicConPolicyIntId_Type=SnmpAdminString
_CfprVnicDynamicConPolicyIntId_Object=MibTableColumn
cfprVnicDynamicConPolicyIntId=_CfprVnicDynamicConPolicyIntId_Object((1,3,6,1,4,1,9,9,826,1,83,6,1,7),_CfprVnicDynamicConPolicyIntId_Type())
cfprVnicDynamicConPolicyIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicDynamicConPolicyIntId.setStatus(_A)
_CfprVnicDynamicConPolicyMtu_Type=Gauge32
_CfprVnicDynamicConPolicyMtu_Object=MibTableColumn
cfprVnicDynamicConPolicyMtu=_CfprVnicDynamicConPolicyMtu_Object((1,3,6,1,4,1,9,9,826,1,83,6,1,8),_CfprVnicDynamicConPolicyMtu_Type())
cfprVnicDynamicConPolicyMtu.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicDynamicConPolicyMtu.setStatus(_A)
_CfprVnicDynamicConPolicyName_Type=SnmpAdminString
_CfprVnicDynamicConPolicyName_Object=MibTableColumn
cfprVnicDynamicConPolicyName=_CfprVnicDynamicConPolicyName_Object((1,3,6,1,4,1,9,9,826,1,83,6,1,9),_CfprVnicDynamicConPolicyName_Type())
cfprVnicDynamicConPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicDynamicConPolicyName.setStatus(_A)
_CfprVnicDynamicConPolicyNamingPrefix_Type=SnmpAdminString
_CfprVnicDynamicConPolicyNamingPrefix_Object=MibTableColumn
cfprVnicDynamicConPolicyNamingPrefix=_CfprVnicDynamicConPolicyNamingPrefix_Object((1,3,6,1,4,1,9,9,826,1,83,6,1,10),_CfprVnicDynamicConPolicyNamingPrefix_Type())
cfprVnicDynamicConPolicyNamingPrefix.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicDynamicConPolicyNamingPrefix.setStatus(_A)
_CfprVnicDynamicConPolicyPolicyLevel_Type=Gauge32
_CfprVnicDynamicConPolicyPolicyLevel_Object=MibTableColumn
cfprVnicDynamicConPolicyPolicyLevel=_CfprVnicDynamicConPolicyPolicyLevel_Object((1,3,6,1,4,1,9,9,826,1,83,6,1,11),_CfprVnicDynamicConPolicyPolicyLevel_Type())
cfprVnicDynamicConPolicyPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicDynamicConPolicyPolicyLevel.setStatus(_A)
_CfprVnicDynamicConPolicyPolicyOwner_Type=CfprPolicyPolicyOwner
_CfprVnicDynamicConPolicyPolicyOwner_Object=MibTableColumn
cfprVnicDynamicConPolicyPolicyOwner=_CfprVnicDynamicConPolicyPolicyOwner_Object((1,3,6,1,4,1,9,9,826,1,83,6,1,12),_CfprVnicDynamicConPolicyPolicyOwner_Type())
cfprVnicDynamicConPolicyPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicDynamicConPolicyPolicyOwner.setStatus(_A)
_CfprVnicDynamicConPolicyProtection_Type=CfprVnicDynamicConReqProtection
_CfprVnicDynamicConPolicyProtection_Object=MibTableColumn
cfprVnicDynamicConPolicyProtection=_CfprVnicDynamicConPolicyProtection_Object((1,3,6,1,4,1,9,9,826,1,83,6,1,13),_CfprVnicDynamicConPolicyProtection_Type())
cfprVnicDynamicConPolicyProtection.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicDynamicConPolicyProtection.setStatus(_A)
_CfprVnicDynamicConPolicyRefTable_Object=MibTable
cfprVnicDynamicConPolicyRefTable=_CfprVnicDynamicConPolicyRefTable_Object((1,3,6,1,4,1,9,9,826,1,83,7))
if mibBuilder.loadTexts:cfprVnicDynamicConPolicyRefTable.setStatus(_A)
_CfprVnicDynamicConPolicyRefEntry_Object=MibTableRow
cfprVnicDynamicConPolicyRefEntry=_CfprVnicDynamicConPolicyRefEntry_Object((1,3,6,1,4,1,9,9,826,1,83,7,1))
cfprVnicDynamicConPolicyRefEntry.setIndexNames((0,_C,_K))
if mibBuilder.loadTexts:cfprVnicDynamicConPolicyRefEntry.setStatus(_A)
_CfprVnicDynamicConPolicyRefInstanceId_Type=CfprManagedObjectId
_CfprVnicDynamicConPolicyRefInstanceId_Object=MibTableColumn
cfprVnicDynamicConPolicyRefInstanceId=_CfprVnicDynamicConPolicyRefInstanceId_Object((1,3,6,1,4,1,9,9,826,1,83,7,1,1),_CfprVnicDynamicConPolicyRefInstanceId_Type())
cfprVnicDynamicConPolicyRefInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprVnicDynamicConPolicyRefInstanceId.setStatus(_A)
_CfprVnicDynamicConPolicyRefDn_Type=CfprManagedObjectDn
_CfprVnicDynamicConPolicyRefDn_Object=MibTableColumn
cfprVnicDynamicConPolicyRefDn=_CfprVnicDynamicConPolicyRefDn_Object((1,3,6,1,4,1,9,9,826,1,83,7,1,2),_CfprVnicDynamicConPolicyRefDn_Type())
cfprVnicDynamicConPolicyRefDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicDynamicConPolicyRefDn.setStatus(_A)
_CfprVnicDynamicConPolicyRefRn_Type=SnmpAdminString
_CfprVnicDynamicConPolicyRefRn_Object=MibTableColumn
cfprVnicDynamicConPolicyRefRn=_CfprVnicDynamicConPolicyRefRn_Object((1,3,6,1,4,1,9,9,826,1,83,7,1,3),_CfprVnicDynamicConPolicyRefRn_Type())
cfprVnicDynamicConPolicyRefRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicDynamicConPolicyRefRn.setStatus(_A)
_CfprVnicDynamicConPolicyRefConPolicyName_Type=SnmpAdminString
_CfprVnicDynamicConPolicyRefConPolicyName_Object=MibTableColumn
cfprVnicDynamicConPolicyRefConPolicyName=_CfprVnicDynamicConPolicyRefConPolicyName_Object((1,3,6,1,4,1,9,9,826,1,83,7,1,4),_CfprVnicDynamicConPolicyRefConPolicyName_Type())
cfprVnicDynamicConPolicyRefConPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicDynamicConPolicyRefConPolicyName.setStatus(_A)
_CfprVnicDynamicConPolicyRefOperConPolicyName_Type=SnmpAdminString
_CfprVnicDynamicConPolicyRefOperConPolicyName_Object=MibTableColumn
cfprVnicDynamicConPolicyRefOperConPolicyName=_CfprVnicDynamicConPolicyRefOperConPolicyName_Object((1,3,6,1,4,1,9,9,826,1,83,7,1,5),_CfprVnicDynamicConPolicyRefOperConPolicyName_Type())
cfprVnicDynamicConPolicyRefOperConPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicDynamicConPolicyRefOperConPolicyName.setStatus(_A)
_CfprVnicDynamicIdUniverseTable_Object=MibTable
cfprVnicDynamicIdUniverseTable=_CfprVnicDynamicIdUniverseTable_Object((1,3,6,1,4,1,9,9,826,1,83,8))
if mibBuilder.loadTexts:cfprVnicDynamicIdUniverseTable.setStatus(_A)
_CfprVnicDynamicIdUniverseEntry_Object=MibTableRow
cfprVnicDynamicIdUniverseEntry=_CfprVnicDynamicIdUniverseEntry_Object((1,3,6,1,4,1,9,9,826,1,83,8,1))
cfprVnicDynamicIdUniverseEntry.setIndexNames((0,_C,_L))
if mibBuilder.loadTexts:cfprVnicDynamicIdUniverseEntry.setStatus(_A)
_CfprVnicDynamicIdUniverseInstanceId_Type=CfprManagedObjectId
_CfprVnicDynamicIdUniverseInstanceId_Object=MibTableColumn
cfprVnicDynamicIdUniverseInstanceId=_CfprVnicDynamicIdUniverseInstanceId_Object((1,3,6,1,4,1,9,9,826,1,83,8,1,1),_CfprVnicDynamicIdUniverseInstanceId_Type())
cfprVnicDynamicIdUniverseInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprVnicDynamicIdUniverseInstanceId.setStatus(_A)
_CfprVnicDynamicIdUniverseDn_Type=CfprManagedObjectDn
_CfprVnicDynamicIdUniverseDn_Object=MibTableColumn
cfprVnicDynamicIdUniverseDn=_CfprVnicDynamicIdUniverseDn_Object((1,3,6,1,4,1,9,9,826,1,83,8,1,2),_CfprVnicDynamicIdUniverseDn_Type())
cfprVnicDynamicIdUniverseDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicDynamicIdUniverseDn.setStatus(_A)
_CfprVnicDynamicIdUniverseRn_Type=SnmpAdminString
_CfprVnicDynamicIdUniverseRn_Object=MibTableColumn
cfprVnicDynamicIdUniverseRn=_CfprVnicDynamicIdUniverseRn_Object((1,3,6,1,4,1,9,9,826,1,83,8,1,3),_CfprVnicDynamicIdUniverseRn_Type())
cfprVnicDynamicIdUniverseRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicDynamicIdUniverseRn.setStatus(_A)
_CfprVnicDynamicIdUniverseDescr_Type=SnmpAdminString
_CfprVnicDynamicIdUniverseDescr_Object=MibTableColumn
cfprVnicDynamicIdUniverseDescr=_CfprVnicDynamicIdUniverseDescr_Object((1,3,6,1,4,1,9,9,826,1,83,8,1,4),_CfprVnicDynamicIdUniverseDescr_Type())
cfprVnicDynamicIdUniverseDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicDynamicIdUniverseDescr.setStatus(_A)
_CfprVnicDynamicIdUniverseIntId_Type=SnmpAdminString
_CfprVnicDynamicIdUniverseIntId_Object=MibTableColumn
cfprVnicDynamicIdUniverseIntId=_CfprVnicDynamicIdUniverseIntId_Object((1,3,6,1,4,1,9,9,826,1,83,8,1,5),_CfprVnicDynamicIdUniverseIntId_Type())
cfprVnicDynamicIdUniverseIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicDynamicIdUniverseIntId.setStatus(_A)
_CfprVnicDynamicIdUniverseName_Type=SnmpAdminString
_CfprVnicDynamicIdUniverseName_Object=MibTableColumn
cfprVnicDynamicIdUniverseName=_CfprVnicDynamicIdUniverseName_Object((1,3,6,1,4,1,9,9,826,1,83,8,1,6),_CfprVnicDynamicIdUniverseName_Type())
cfprVnicDynamicIdUniverseName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicDynamicIdUniverseName.setStatus(_A)
_CfprVnicDynamicIdUniversePolicyLevel_Type=Gauge32
_CfprVnicDynamicIdUniversePolicyLevel_Object=MibTableColumn
cfprVnicDynamicIdUniversePolicyLevel=_CfprVnicDynamicIdUniversePolicyLevel_Object((1,3,6,1,4,1,9,9,826,1,83,8,1,7),_CfprVnicDynamicIdUniversePolicyLevel_Type())
cfprVnicDynamicIdUniversePolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicDynamicIdUniversePolicyLevel.setStatus(_A)
_CfprVnicDynamicIdUniversePolicyOwner_Type=CfprPolicyPolicyOwner
_CfprVnicDynamicIdUniversePolicyOwner_Object=MibTableColumn
cfprVnicDynamicIdUniversePolicyOwner=_CfprVnicDynamicIdUniversePolicyOwner_Object((1,3,6,1,4,1,9,9,826,1,83,8,1,8),_CfprVnicDynamicIdUniversePolicyOwner_Type())
cfprVnicDynamicIdUniversePolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicDynamicIdUniversePolicyOwner.setStatus(_A)
_CfprVnicDynamicProviderTable_Object=MibTable
cfprVnicDynamicProviderTable=_CfprVnicDynamicProviderTable_Object((1,3,6,1,4,1,9,9,826,1,83,9))
if mibBuilder.loadTexts:cfprVnicDynamicProviderTable.setStatus(_A)
_CfprVnicDynamicProviderEntry_Object=MibTableRow
cfprVnicDynamicProviderEntry=_CfprVnicDynamicProviderEntry_Object((1,3,6,1,4,1,9,9,826,1,83,9,1))
cfprVnicDynamicProviderEntry.setIndexNames((0,_C,_M))
if mibBuilder.loadTexts:cfprVnicDynamicProviderEntry.setStatus(_A)
_CfprVnicDynamicProviderInstanceId_Type=CfprManagedObjectId
_CfprVnicDynamicProviderInstanceId_Object=MibTableColumn
cfprVnicDynamicProviderInstanceId=_CfprVnicDynamicProviderInstanceId_Object((1,3,6,1,4,1,9,9,826,1,83,9,1,1),_CfprVnicDynamicProviderInstanceId_Type())
cfprVnicDynamicProviderInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprVnicDynamicProviderInstanceId.setStatus(_A)
_CfprVnicDynamicProviderDn_Type=CfprManagedObjectDn
_CfprVnicDynamicProviderDn_Object=MibTableColumn
cfprVnicDynamicProviderDn=_CfprVnicDynamicProviderDn_Object((1,3,6,1,4,1,9,9,826,1,83,9,1,2),_CfprVnicDynamicProviderDn_Type())
cfprVnicDynamicProviderDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicDynamicProviderDn.setStatus(_A)
_CfprVnicDynamicProviderRn_Type=SnmpAdminString
_CfprVnicDynamicProviderRn_Object=MibTableColumn
cfprVnicDynamicProviderRn=_CfprVnicDynamicProviderRn_Object((1,3,6,1,4,1,9,9,826,1,83,9,1,3),_CfprVnicDynamicProviderRn_Type())
cfprVnicDynamicProviderRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicDynamicProviderRn.setStatus(_A)
_CfprVnicDynamicProviderName_Type=SnmpAdminString
_CfprVnicDynamicProviderName_Object=MibTableColumn
cfprVnicDynamicProviderName=_CfprVnicDynamicProviderName_Object((1,3,6,1,4,1,9,9,826,1,83,9,1,4),_CfprVnicDynamicProviderName_Type())
cfprVnicDynamicProviderName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicDynamicProviderName.setStatus(_A)
_CfprVnicDynamicProviderEpTable_Object=MibTable
cfprVnicDynamicProviderEpTable=_CfprVnicDynamicProviderEpTable_Object((1,3,6,1,4,1,9,9,826,1,83,10))
if mibBuilder.loadTexts:cfprVnicDynamicProviderEpTable.setStatus(_A)
_CfprVnicDynamicProviderEpEntry_Object=MibTableRow
cfprVnicDynamicProviderEpEntry=_CfprVnicDynamicProviderEpEntry_Object((1,3,6,1,4,1,9,9,826,1,83,10,1))
cfprVnicDynamicProviderEpEntry.setIndexNames((0,_C,_N))
if mibBuilder.loadTexts:cfprVnicDynamicProviderEpEntry.setStatus(_A)
_CfprVnicDynamicProviderEpInstanceId_Type=CfprManagedObjectId
_CfprVnicDynamicProviderEpInstanceId_Object=MibTableColumn
cfprVnicDynamicProviderEpInstanceId=_CfprVnicDynamicProviderEpInstanceId_Object((1,3,6,1,4,1,9,9,826,1,83,10,1,1),_CfprVnicDynamicProviderEpInstanceId_Type())
cfprVnicDynamicProviderEpInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprVnicDynamicProviderEpInstanceId.setStatus(_A)
_CfprVnicDynamicProviderEpDn_Type=CfprManagedObjectDn
_CfprVnicDynamicProviderEpDn_Object=MibTableColumn
cfprVnicDynamicProviderEpDn=_CfprVnicDynamicProviderEpDn_Object((1,3,6,1,4,1,9,9,826,1,83,10,1,2),_CfprVnicDynamicProviderEpDn_Type())
cfprVnicDynamicProviderEpDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicDynamicProviderEpDn.setStatus(_A)
_CfprVnicDynamicProviderEpRn_Type=SnmpAdminString
_CfprVnicDynamicProviderEpRn_Object=MibTableColumn
cfprVnicDynamicProviderEpRn=_CfprVnicDynamicProviderEpRn_Object((1,3,6,1,4,1,9,9,826,1,83,10,1,3),_CfprVnicDynamicProviderEpRn_Type())
cfprVnicDynamicProviderEpRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicDynamicProviderEpRn.setStatus(_A)
_CfprVnicDynamicProviderEpChassisId_Type=Gauge32
_CfprVnicDynamicProviderEpChassisId_Object=MibTableColumn
cfprVnicDynamicProviderEpChassisId=_CfprVnicDynamicProviderEpChassisId_Object((1,3,6,1,4,1,9,9,826,1,83,10,1,4),_CfprVnicDynamicProviderEpChassisId_Type())
cfprVnicDynamicProviderEpChassisId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicDynamicProviderEpChassisId.setStatus(_A)
_CfprVnicDynamicProviderEpPortId_Type=Gauge32
_CfprVnicDynamicProviderEpPortId_Object=MibTableColumn
cfprVnicDynamicProviderEpPortId=_CfprVnicDynamicProviderEpPortId_Object((1,3,6,1,4,1,9,9,826,1,83,10,1,5),_CfprVnicDynamicProviderEpPortId_Type())
cfprVnicDynamicProviderEpPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicDynamicProviderEpPortId.setStatus(_A)
_CfprVnicDynamicProviderEpSlotId_Type=Gauge32
_CfprVnicDynamicProviderEpSlotId_Object=MibTableColumn
cfprVnicDynamicProviderEpSlotId=_CfprVnicDynamicProviderEpSlotId_Object((1,3,6,1,4,1,9,9,826,1,83,10,1,6),_CfprVnicDynamicProviderEpSlotId_Type())
cfprVnicDynamicProviderEpSlotId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicDynamicProviderEpSlotId.setStatus(_A)
_CfprVnicDynamicProviderEpSwitchId_Type=CfprNetworkSwitchId
_CfprVnicDynamicProviderEpSwitchId_Object=MibTableColumn
cfprVnicDynamicProviderEpSwitchId=_CfprVnicDynamicProviderEpSwitchId_Object((1,3,6,1,4,1,9,9,826,1,83,10,1,7),_CfprVnicDynamicProviderEpSwitchId_Type())
cfprVnicDynamicProviderEpSwitchId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicDynamicProviderEpSwitchId.setStatus(_A)
_CfprVnicEthLifTable_Object=MibTable
cfprVnicEthLifTable=_CfprVnicEthLifTable_Object((1,3,6,1,4,1,9,9,826,1,83,11))
if mibBuilder.loadTexts:cfprVnicEthLifTable.setStatus(_A)
_CfprVnicEthLifEntry_Object=MibTableRow
cfprVnicEthLifEntry=_CfprVnicEthLifEntry_Object((1,3,6,1,4,1,9,9,826,1,83,11,1))
cfprVnicEthLifEntry.setIndexNames((0,_C,_O))
if mibBuilder.loadTexts:cfprVnicEthLifEntry.setStatus(_A)
_CfprVnicEthLifInstanceId_Type=CfprManagedObjectId
_CfprVnicEthLifInstanceId_Object=MibTableColumn
cfprVnicEthLifInstanceId=_CfprVnicEthLifInstanceId_Object((1,3,6,1,4,1,9,9,826,1,83,11,1,1),_CfprVnicEthLifInstanceId_Type())
cfprVnicEthLifInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprVnicEthLifInstanceId.setStatus(_A)
_CfprVnicEthLifDn_Type=CfprManagedObjectDn
_CfprVnicEthLifDn_Object=MibTableColumn
cfprVnicEthLifDn=_CfprVnicEthLifDn_Object((1,3,6,1,4,1,9,9,826,1,83,11,1,2),_CfprVnicEthLifDn_Type())
cfprVnicEthLifDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicEthLifDn.setStatus(_A)
_CfprVnicEthLifRn_Type=SnmpAdminString
_CfprVnicEthLifRn_Object=MibTableColumn
cfprVnicEthLifRn=_CfprVnicEthLifRn_Object((1,3,6,1,4,1,9,9,826,1,83,11,1,3),_CfprVnicEthLifRn_Type())
cfprVnicEthLifRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicEthLifRn.setStatus(_A)
_CfprVnicEthLifAddr_Type=MacAddress
_CfprVnicEthLifAddr_Object=MibTableColumn
cfprVnicEthLifAddr=_CfprVnicEthLifAddr_Object((1,3,6,1,4,1,9,9,826,1,83,11,1,4),_CfprVnicEthLifAddr_Type())
cfprVnicEthLifAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicEthLifAddr.setStatus(_A)
_CfprVnicEthLifName_Type=SnmpAdminString
_CfprVnicEthLifName_Object=MibTableColumn
cfprVnicEthLifName=_CfprVnicEthLifName_Object((1,3,6,1,4,1,9,9,826,1,83,11,1,5),_CfprVnicEthLifName_Type())
cfprVnicEthLifName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicEthLifName.setStatus(_A)
_CfprVnicEthLifNicDn_Type=SnmpAdminString
_CfprVnicEthLifNicDn_Object=MibTableColumn
cfprVnicEthLifNicDn=_CfprVnicEthLifNicDn_Object((1,3,6,1,4,1,9,9,826,1,83,11,1,6),_CfprVnicEthLifNicDn_Type())
cfprVnicEthLifNicDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicEthLifNicDn.setStatus(_A)
_CfprVnicEthLifOwner_Type=CfprVnicConnectionOwner
_CfprVnicEthLifOwner_Object=MibTableColumn
cfprVnicEthLifOwner=_CfprVnicEthLifOwner_Object((1,3,6,1,4,1,9,9,826,1,83,11,1,7),_CfprVnicEthLifOwner_Type())
cfprVnicEthLifOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicEthLifOwner.setStatus(_A)
_CfprVnicEthLifSwitchId_Type=CfprNetworkSwitchId
_CfprVnicEthLifSwitchId_Object=MibTableColumn
cfprVnicEthLifSwitchId=_CfprVnicEthLifSwitchId_Object((1,3,6,1,4,1,9,9,826,1,83,11,1,8),_CfprVnicEthLifSwitchId_Type())
cfprVnicEthLifSwitchId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicEthLifSwitchId.setStatus(_A)
_CfprVnicEthLifType_Type=CfprVnicConnectionType
_CfprVnicEthLifType_Object=MibTableColumn
cfprVnicEthLifType=_CfprVnicEthLifType_Object((1,3,6,1,4,1,9,9,826,1,83,11,1,9),_CfprVnicEthLifType_Type())
cfprVnicEthLifType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicEthLifType.setStatus(_A)
_CfprVnicEthLifVnicDn_Type=SnmpAdminString
_CfprVnicEthLifVnicDn_Object=MibTableColumn
cfprVnicEthLifVnicDn=_CfprVnicEthLifVnicDn_Object((1,3,6,1,4,1,9,9,826,1,83,11,1,10),_CfprVnicEthLifVnicDn_Type())
cfprVnicEthLifVnicDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicEthLifVnicDn.setStatus(_A)
_CfprVnicEtherTable_Object=MibTable
cfprVnicEtherTable=_CfprVnicEtherTable_Object((1,3,6,1,4,1,9,9,826,1,83,12))
if mibBuilder.loadTexts:cfprVnicEtherTable.setStatus(_A)
_CfprVnicEtherEntry_Object=MibTableRow
cfprVnicEtherEntry=_CfprVnicEtherEntry_Object((1,3,6,1,4,1,9,9,826,1,83,12,1))
cfprVnicEtherEntry.setIndexNames((0,_C,_P))
if mibBuilder.loadTexts:cfprVnicEtherEntry.setStatus(_A)
_CfprVnicEtherInstanceId_Type=CfprManagedObjectId
_CfprVnicEtherInstanceId_Object=MibTableColumn
cfprVnicEtherInstanceId=_CfprVnicEtherInstanceId_Object((1,3,6,1,4,1,9,9,826,1,83,12,1,1),_CfprVnicEtherInstanceId_Type())
cfprVnicEtherInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprVnicEtherInstanceId.setStatus(_A)
_CfprVnicEtherDn_Type=CfprManagedObjectDn
_CfprVnicEtherDn_Object=MibTableColumn
cfprVnicEtherDn=_CfprVnicEtherDn_Object((1,3,6,1,4,1,9,9,826,1,83,12,1,2),_CfprVnicEtherDn_Type())
cfprVnicEtherDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicEtherDn.setStatus(_A)
_CfprVnicEtherRn_Type=SnmpAdminString
_CfprVnicEtherRn_Object=MibTableColumn
cfprVnicEtherRn=_CfprVnicEtherRn_Object((1,3,6,1,4,1,9,9,826,1,83,12,1,3),_CfprVnicEtherRn_Type())
cfprVnicEtherRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicEtherRn.setStatus(_A)
_CfprVnicEtherAdaptorProfileName_Type=SnmpAdminString
_CfprVnicEtherAdaptorProfileName_Object=MibTableColumn
cfprVnicEtherAdaptorProfileName=_CfprVnicEtherAdaptorProfileName_Object((1,3,6,1,4,1,9,9,826,1,83,12,1,4),_CfprVnicEtherAdaptorProfileName_Type())
cfprVnicEtherAdaptorProfileName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicEtherAdaptorProfileName.setStatus(_A)
_CfprVnicEtherAddr_Type=MacAddress
_CfprVnicEtherAddr_Object=MibTableColumn
cfprVnicEtherAddr=_CfprVnicEtherAddr_Object((1,3,6,1,4,1,9,9,826,1,83,12,1,5),_CfprVnicEtherAddr_Type())
cfprVnicEtherAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicEtherAddr.setStatus(_A)
_CfprVnicEtherAdminHostPort_Type=CfprFabricHostPortId
_CfprVnicEtherAdminHostPort_Object=MibTableColumn
cfprVnicEtherAdminHostPort=_CfprVnicEtherAdminHostPort_Object((1,3,6,1,4,1,9,9,826,1,83,12,1,6),_CfprVnicEtherAdminHostPort_Type())
cfprVnicEtherAdminHostPort.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicEtherAdminHostPort.setStatus(_A)
_CfprVnicEtherAdminVcon_Type=SnmpAdminString
_CfprVnicEtherAdminVcon_Object=MibTableColumn
cfprVnicEtherAdminVcon=_CfprVnicEtherAdminVcon_Object((1,3,6,1,4,1,9,9,826,1,83,12,1,7),_CfprVnicEtherAdminVcon_Type())
cfprVnicEtherAdminVcon.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicEtherAdminVcon.setStatus(_A)
_CfprVnicEtherAppInstId_Type=SnmpAdminString
_CfprVnicEtherAppInstId_Object=MibTableColumn
cfprVnicEtherAppInstId=_CfprVnicEtherAppInstId_Object((1,3,6,1,4,1,9,9,826,1,83,12,1,8),_CfprVnicEtherAppInstId_Type())
cfprVnicEtherAppInstId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicEtherAppInstId.setStatus(_A)
_CfprVnicEtherAppRole_Type=CfprVnicAppRole
_CfprVnicEtherAppRole_Object=MibTableColumn
cfprVnicEtherAppRole=_CfprVnicEtherAppRole_Object((1,3,6,1,4,1,9,9,826,1,83,12,1,9),_CfprVnicEtherAppRole_Type())
cfprVnicEtherAppRole.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicEtherAppRole.setStatus(_A)
_CfprVnicEtherBootDev_Type=CfprVnicVnicBootDev
_CfprVnicEtherBootDev_Object=MibTableColumn
cfprVnicEtherBootDev=_CfprVnicEtherBootDev_Object((1,3,6,1,4,1,9,9,826,1,83,12,1,10),_CfprVnicEtherBootDev_Type())
cfprVnicEtherBootDev.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicEtherBootDev.setStatus(_A)
_CfprVnicEtherConfigQualifier_Type=CfprVnicConfigIssues
_CfprVnicEtherConfigQualifier_Object=MibTableColumn
cfprVnicEtherConfigQualifier=_CfprVnicEtherConfigQualifier_Object((1,3,6,1,4,1,9,9,826,1,83,12,1,11),_CfprVnicEtherConfigQualifier_Type())
cfprVnicEtherConfigQualifier.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicEtherConfigQualifier.setStatus(_A)
_CfprVnicEtherConfigState_Type=CfprLsConfigState
_CfprVnicEtherConfigState_Object=MibTableColumn
cfprVnicEtherConfigState=_CfprVnicEtherConfigState_Object((1,3,6,1,4,1,9,9,826,1,83,12,1,12),_CfprVnicEtherConfigState_Type())
cfprVnicEtherConfigState.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicEtherConfigState.setStatus(_A)
_CfprVnicEtherDynamicId_Type=Gauge32
_CfprVnicEtherDynamicId_Object=MibTableColumn
cfprVnicEtherDynamicId=_CfprVnicEtherDynamicId_Object((1,3,6,1,4,1,9,9,826,1,83,12,1,13),_CfprVnicEtherDynamicId_Type())
cfprVnicEtherDynamicId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicEtherDynamicId.setStatus(_A)
_CfprVnicEtherEquipmentDn_Type=SnmpAdminString
_CfprVnicEtherEquipmentDn_Object=MibTableColumn
cfprVnicEtherEquipmentDn=_CfprVnicEtherEquipmentDn_Object((1,3,6,1,4,1,9,9,826,1,83,12,1,14),_CfprVnicEtherEquipmentDn_Type())
cfprVnicEtherEquipmentDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicEtherEquipmentDn.setStatus(_A)
_CfprVnicEtherFltAggr_Type=Unsigned64
_CfprVnicEtherFltAggr_Object=MibTableColumn
cfprVnicEtherFltAggr=_CfprVnicEtherFltAggr_Object((1,3,6,1,4,1,9,9,826,1,83,12,1,15),_CfprVnicEtherFltAggr_Type())
cfprVnicEtherFltAggr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicEtherFltAggr.setStatus(_A)
_CfprVnicEtherIdentPoolName_Type=SnmpAdminString
_CfprVnicEtherIdentPoolName_Object=MibTableColumn
cfprVnicEtherIdentPoolName=_CfprVnicEtherIdentPoolName_Object((1,3,6,1,4,1,9,9,826,1,83,12,1,16),_CfprVnicEtherIdentPoolName_Type())
cfprVnicEtherIdentPoolName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicEtherIdentPoolName.setStatus(_A)
_CfprVnicEtherInstType_Type=CfprVnicInstantiation
_CfprVnicEtherInstType_Object=MibTableColumn
cfprVnicEtherInstType=_CfprVnicEtherInstType_Object((1,3,6,1,4,1,9,9,826,1,83,12,1,17),_CfprVnicEtherInstType_Type())
cfprVnicEtherInstType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicEtherInstType.setStatus(_A)
_CfprVnicEtherIsAllocated_Type=TruthValue
_CfprVnicEtherIsAllocated_Object=MibTableColumn
cfprVnicEtherIsAllocated=_CfprVnicEtherIsAllocated_Object((1,3,6,1,4,1,9,9,826,1,83,12,1,18),_CfprVnicEtherIsAllocated_Type())
cfprVnicEtherIsAllocated.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicEtherIsAllocated.setStatus(_A)
_CfprVnicEtherMtu_Type=Gauge32
_CfprVnicEtherMtu_Object=MibTableColumn
cfprVnicEtherMtu=_CfprVnicEtherMtu_Object((1,3,6,1,4,1,9,9,826,1,83,12,1,19),_CfprVnicEtherMtu_Type())
cfprVnicEtherMtu.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicEtherMtu.setStatus(_A)
_CfprVnicEtherName_Type=SnmpAdminString
_CfprVnicEtherName_Object=MibTableColumn
cfprVnicEtherName=_CfprVnicEtherName_Object((1,3,6,1,4,1,9,9,826,1,83,12,1,20),_CfprVnicEtherName_Type())
cfprVnicEtherName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicEtherName.setStatus(_A)
_CfprVnicEtherNwCtrlPolicyName_Type=SnmpAdminString
_CfprVnicEtherNwCtrlPolicyName_Object=MibTableColumn
cfprVnicEtherNwCtrlPolicyName=_CfprVnicEtherNwCtrlPolicyName_Object((1,3,6,1,4,1,9,9,826,1,83,12,1,21),_CfprVnicEtherNwCtrlPolicyName_Type())
cfprVnicEtherNwCtrlPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicEtherNwCtrlPolicyName.setStatus(_A)
_CfprVnicEtherNwTemplName_Type=SnmpAdminString
_CfprVnicEtherNwTemplName_Object=MibTableColumn
cfprVnicEtherNwTemplName=_CfprVnicEtherNwTemplName_Object((1,3,6,1,4,1,9,9,826,1,83,12,1,22),_CfprVnicEtherNwTemplName_Type())
cfprVnicEtherNwTemplName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicEtherNwTemplName.setStatus(_A)
_CfprVnicEtherOperAdaptorProfileName_Type=SnmpAdminString
_CfprVnicEtherOperAdaptorProfileName_Object=MibTableColumn
cfprVnicEtherOperAdaptorProfileName=_CfprVnicEtherOperAdaptorProfileName_Object((1,3,6,1,4,1,9,9,826,1,83,12,1,23),_CfprVnicEtherOperAdaptorProfileName_Type())
cfprVnicEtherOperAdaptorProfileName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicEtherOperAdaptorProfileName.setStatus(_A)
_CfprVnicEtherOperHostPort_Type=CfprVnicVnicOperHostPort
_CfprVnicEtherOperHostPort_Object=MibTableColumn
cfprVnicEtherOperHostPort=_CfprVnicEtherOperHostPort_Object((1,3,6,1,4,1,9,9,826,1,83,12,1,24),_CfprVnicEtherOperHostPort_Type())
cfprVnicEtherOperHostPort.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicEtherOperHostPort.setStatus(_A)
_CfprVnicEtherOperIdentPoolName_Type=SnmpAdminString
_CfprVnicEtherOperIdentPoolName_Object=MibTableColumn
cfprVnicEtherOperIdentPoolName=_CfprVnicEtherOperIdentPoolName_Object((1,3,6,1,4,1,9,9,826,1,83,12,1,25),_CfprVnicEtherOperIdentPoolName_Type())
cfprVnicEtherOperIdentPoolName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicEtherOperIdentPoolName.setStatus(_A)
_CfprVnicEtherOperNwCtrlPolicyName_Type=SnmpAdminString
_CfprVnicEtherOperNwCtrlPolicyName_Object=MibTableColumn
cfprVnicEtherOperNwCtrlPolicyName=_CfprVnicEtherOperNwCtrlPolicyName_Object((1,3,6,1,4,1,9,9,826,1,83,12,1,26),_CfprVnicEtherOperNwCtrlPolicyName_Type())
cfprVnicEtherOperNwCtrlPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicEtherOperNwCtrlPolicyName.setStatus(_A)
_CfprVnicEtherOperNwTemplName_Type=SnmpAdminString
_CfprVnicEtherOperNwTemplName_Object=MibTableColumn
cfprVnicEtherOperNwTemplName=_CfprVnicEtherOperNwTemplName_Object((1,3,6,1,4,1,9,9,826,1,83,12,1,27),_CfprVnicEtherOperNwTemplName_Type())
cfprVnicEtherOperNwTemplName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicEtherOperNwTemplName.setStatus(_A)
_CfprVnicEtherOperOrder_Type=Gauge32
_CfprVnicEtherOperOrder_Object=MibTableColumn
cfprVnicEtherOperOrder=_CfprVnicEtherOperOrder_Object((1,3,6,1,4,1,9,9,826,1,83,12,1,28),_CfprVnicEtherOperOrder_Type())
cfprVnicEtherOperOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicEtherOperOrder.setStatus(_A)
_CfprVnicEtherOperPinToGroupName_Type=SnmpAdminString
_CfprVnicEtherOperPinToGroupName_Object=MibTableColumn
cfprVnicEtherOperPinToGroupName=_CfprVnicEtherOperPinToGroupName_Object((1,3,6,1,4,1,9,9,826,1,83,12,1,29),_CfprVnicEtherOperPinToGroupName_Type())
cfprVnicEtherOperPinToGroupName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicEtherOperPinToGroupName.setStatus(_A)
_CfprVnicEtherOperQosPolicyName_Type=SnmpAdminString
_CfprVnicEtherOperQosPolicyName_Object=MibTableColumn
cfprVnicEtherOperQosPolicyName=_CfprVnicEtherOperQosPolicyName_Object((1,3,6,1,4,1,9,9,826,1,83,12,1,30),_CfprVnicEtherOperQosPolicyName_Type())
cfprVnicEtherOperQosPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicEtherOperQosPolicyName.setStatus(_A)
_CfprVnicEtherOperSpeed_Type=Gauge32
_CfprVnicEtherOperSpeed_Object=MibTableColumn
cfprVnicEtherOperSpeed=_CfprVnicEtherOperSpeed_Object((1,3,6,1,4,1,9,9,826,1,83,12,1,31),_CfprVnicEtherOperSpeed_Type())
cfprVnicEtherOperSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicEtherOperSpeed.setStatus(_A)
_CfprVnicEtherOperStatsPolicyName_Type=SnmpAdminString
_CfprVnicEtherOperStatsPolicyName_Object=MibTableColumn
cfprVnicEtherOperStatsPolicyName=_CfprVnicEtherOperStatsPolicyName_Object((1,3,6,1,4,1,9,9,826,1,83,12,1,32),_CfprVnicEtherOperStatsPolicyName_Type())
cfprVnicEtherOperStatsPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicEtherOperStatsPolicyName.setStatus(_A)
_CfprVnicEtherOperVcon_Type=SnmpAdminString
_CfprVnicEtherOperVcon_Object=MibTableColumn
cfprVnicEtherOperVcon=_CfprVnicEtherOperVcon_Object((1,3,6,1,4,1,9,9,826,1,83,12,1,33),_CfprVnicEtherOperVcon_Type())
cfprVnicEtherOperVcon.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicEtherOperVcon.setStatus(_A)
_CfprVnicEtherOrder_Type=Gauge32
_CfprVnicEtherOrder_Object=MibTableColumn
cfprVnicEtherOrder=_CfprVnicEtherOrder_Object((1,3,6,1,4,1,9,9,826,1,83,12,1,34),_CfprVnicEtherOrder_Type())
cfprVnicEtherOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicEtherOrder.setStatus(_A)
_CfprVnicEtherOwner_Type=CfprVnicConnectionOwner
_CfprVnicEtherOwner_Object=MibTableColumn
cfprVnicEtherOwner=_CfprVnicEtherOwner_Object((1,3,6,1,4,1,9,9,826,1,83,12,1,35),_CfprVnicEtherOwner_Type())
cfprVnicEtherOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicEtherOwner.setStatus(_A)
_CfprVnicEtherPfDn_Type=SnmpAdminString
_CfprVnicEtherPfDn_Object=MibTableColumn
cfprVnicEtherPfDn=_CfprVnicEtherPfDn_Object((1,3,6,1,4,1,9,9,826,1,83,12,1,36),_CfprVnicEtherPfDn_Type())
cfprVnicEtherPfDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicEtherPfDn.setStatus(_A)
_CfprVnicEtherPinToGroupName_Type=SnmpAdminString
_CfprVnicEtherPinToGroupName_Object=MibTableColumn
cfprVnicEtherPinToGroupName=_CfprVnicEtherPinToGroupName_Object((1,3,6,1,4,1,9,9,826,1,83,12,1,37),_CfprVnicEtherPinToGroupName_Type())
cfprVnicEtherPinToGroupName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicEtherPinToGroupName.setStatus(_A)
_CfprVnicEtherQosPolicyName_Type=SnmpAdminString
_CfprVnicEtherQosPolicyName_Object=MibTableColumn
cfprVnicEtherQosPolicyName=_CfprVnicEtherQosPolicyName_Object((1,3,6,1,4,1,9,9,826,1,83,12,1,38),_CfprVnicEtherQosPolicyName_Type())
cfprVnicEtherQosPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicEtherQosPolicyName.setStatus(_A)
_CfprVnicEtherStatsPolicyName_Type=SnmpAdminString
_CfprVnicEtherStatsPolicyName_Object=MibTableColumn
cfprVnicEtherStatsPolicyName=_CfprVnicEtherStatsPolicyName_Object((1,3,6,1,4,1,9,9,826,1,83,12,1,39),_CfprVnicEtherStatsPolicyName_Type())
cfprVnicEtherStatsPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicEtherStatsPolicyName.setStatus(_A)
_CfprVnicEtherSwitchId_Type=CfprVnicEtherBaseSwitchId
_CfprVnicEtherSwitchId_Object=MibTableColumn
cfprVnicEtherSwitchId=_CfprVnicEtherSwitchId_Object((1,3,6,1,4,1,9,9,826,1,83,12,1,40),_CfprVnicEtherSwitchId_Type())
cfprVnicEtherSwitchId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicEtherSwitchId.setStatus(_A)
_CfprVnicEtherType_Type=CfprVnicEtherType
_CfprVnicEtherType_Object=MibTableColumn
cfprVnicEtherType=_CfprVnicEtherType_Object((1,3,6,1,4,1,9,9,826,1,83,12,1,41),_CfprVnicEtherType_Type())
cfprVnicEtherType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicEtherType.setStatus(_A)
_CfprVnicEtherVirtualizationPreference_Type=CfprVnicVirtualizationPreferenceType
_CfprVnicEtherVirtualizationPreference_Object=MibTableColumn
cfprVnicEtherVirtualizationPreference=_CfprVnicEtherVirtualizationPreference_Object((1,3,6,1,4,1,9,9,826,1,83,12,1,42),_CfprVnicEtherVirtualizationPreference_Type())
cfprVnicEtherVirtualizationPreference.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicEtherVirtualizationPreference.setStatus(_A)
_CfprVnicEtherPortType_Type=CfprFabricSSAPortType
_CfprVnicEtherPortType_Object=MibTableColumn
cfprVnicEtherPortType=_CfprVnicEtherPortType_Object((1,3,6,1,4,1,9,9,826,1,83,12,1,43),_CfprVnicEtherPortType_Type())
cfprVnicEtherPortType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicEtherPortType.setStatus(_A)
_CfprVnicEtherIfTable_Object=MibTable
cfprVnicEtherIfTable=_CfprVnicEtherIfTable_Object((1,3,6,1,4,1,9,9,826,1,83,13))
if mibBuilder.loadTexts:cfprVnicEtherIfTable.setStatus(_A)
_CfprVnicEtherIfEntry_Object=MibTableRow
cfprVnicEtherIfEntry=_CfprVnicEtherIfEntry_Object((1,3,6,1,4,1,9,9,826,1,83,13,1))
cfprVnicEtherIfEntry.setIndexNames((0,_C,_Q))
if mibBuilder.loadTexts:cfprVnicEtherIfEntry.setStatus(_A)
_CfprVnicEtherIfInstanceId_Type=CfprManagedObjectId
_CfprVnicEtherIfInstanceId_Object=MibTableColumn
cfprVnicEtherIfInstanceId=_CfprVnicEtherIfInstanceId_Object((1,3,6,1,4,1,9,9,826,1,83,13,1,1),_CfprVnicEtherIfInstanceId_Type())
cfprVnicEtherIfInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprVnicEtherIfInstanceId.setStatus(_A)
_CfprVnicEtherIfDn_Type=CfprManagedObjectDn
_CfprVnicEtherIfDn_Object=MibTableColumn
cfprVnicEtherIfDn=_CfprVnicEtherIfDn_Object((1,3,6,1,4,1,9,9,826,1,83,13,1,2),_CfprVnicEtherIfDn_Type())
cfprVnicEtherIfDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicEtherIfDn.setStatus(_A)
_CfprVnicEtherIfRn_Type=SnmpAdminString
_CfprVnicEtherIfRn_Object=MibTableColumn
cfprVnicEtherIfRn=_CfprVnicEtherIfRn_Object((1,3,6,1,4,1,9,9,826,1,83,13,1,3),_CfprVnicEtherIfRn_Type())
cfprVnicEtherIfRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicEtherIfRn.setStatus(_A)
_CfprVnicEtherIfAddr_Type=MacAddress
_CfprVnicEtherIfAddr_Object=MibTableColumn
cfprVnicEtherIfAddr=_CfprVnicEtherIfAddr_Object((1,3,6,1,4,1,9,9,826,1,83,13,1,4),_CfprVnicEtherIfAddr_Type())
cfprVnicEtherIfAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicEtherIfAddr.setStatus(_A)
_CfprVnicEtherIfConfigQualifier_Type=CfprVnicConfigIssues
_CfprVnicEtherIfConfigQualifier_Object=MibTableColumn
cfprVnicEtherIfConfigQualifier=_CfprVnicEtherIfConfigQualifier_Object((1,3,6,1,4,1,9,9,826,1,83,13,1,5),_CfprVnicEtherIfConfigQualifier_Type())
cfprVnicEtherIfConfigQualifier.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicEtherIfConfigQualifier.setStatus(_A)
_CfprVnicEtherIfDefaultNet_Type=TruthValue
_CfprVnicEtherIfDefaultNet_Object=MibTableColumn
cfprVnicEtherIfDefaultNet=_CfprVnicEtherIfDefaultNet_Object((1,3,6,1,4,1,9,9,826,1,83,13,1,6),_CfprVnicEtherIfDefaultNet_Type())
cfprVnicEtherIfDefaultNet.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicEtherIfDefaultNet.setStatus(_A)
_CfprVnicEtherIfFltAggr_Type=Unsigned64
_CfprVnicEtherIfFltAggr_Object=MibTableColumn
cfprVnicEtherIfFltAggr=_CfprVnicEtherIfFltAggr_Object((1,3,6,1,4,1,9,9,826,1,83,13,1,7),_CfprVnicEtherIfFltAggr_Type())
cfprVnicEtherIfFltAggr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicEtherIfFltAggr.setStatus(_A)
_CfprVnicEtherIfName_Type=SnmpAdminString
_CfprVnicEtherIfName_Object=MibTableColumn
cfprVnicEtherIfName=_CfprVnicEtherIfName_Object((1,3,6,1,4,1,9,9,826,1,83,13,1,8),_CfprVnicEtherIfName_Type())
cfprVnicEtherIfName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicEtherIfName.setStatus(_A)
_CfprVnicEtherIfOperState_Type=CfprVnicIfOperState
_CfprVnicEtherIfOperState_Object=MibTableColumn
cfprVnicEtherIfOperState=_CfprVnicEtherIfOperState_Object((1,3,6,1,4,1,9,9,826,1,83,13,1,9),_CfprVnicEtherIfOperState_Type())
cfprVnicEtherIfOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicEtherIfOperState.setStatus(_A)
_CfprVnicEtherIfOperVnetDn_Type=SnmpAdminString
_CfprVnicEtherIfOperVnetDn_Object=MibTableColumn
cfprVnicEtherIfOperVnetDn=_CfprVnicEtherIfOperVnetDn_Object((1,3,6,1,4,1,9,9,826,1,83,13,1,10),_CfprVnicEtherIfOperVnetDn_Type())
cfprVnicEtherIfOperVnetDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicEtherIfOperVnetDn.setStatus(_A)
_CfprVnicEtherIfOperVnetName_Type=SnmpAdminString
_CfprVnicEtherIfOperVnetName_Object=MibTableColumn
cfprVnicEtherIfOperVnetName=_CfprVnicEtherIfOperVnetName_Object((1,3,6,1,4,1,9,9,826,1,83,13,1,11),_CfprVnicEtherIfOperVnetName_Type())
cfprVnicEtherIfOperVnetName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicEtherIfOperVnetName.setStatus(_A)
_CfprVnicEtherIfOwner_Type=CfprVnicConnectionOwner
_CfprVnicEtherIfOwner_Object=MibTableColumn
cfprVnicEtherIfOwner=_CfprVnicEtherIfOwner_Object((1,3,6,1,4,1,9,9,826,1,83,13,1,12),_CfprVnicEtherIfOwner_Type())
cfprVnicEtherIfOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicEtherIfOwner.setStatus(_A)
_CfprVnicEtherIfPubNwId_Type=Gauge32
_CfprVnicEtherIfPubNwId_Object=MibTableColumn
cfprVnicEtherIfPubNwId=_CfprVnicEtherIfPubNwId_Object((1,3,6,1,4,1,9,9,826,1,83,13,1,13),_CfprVnicEtherIfPubNwId_Type())
cfprVnicEtherIfPubNwId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicEtherIfPubNwId.setStatus(_A)
_CfprVnicEtherIfSharing_Type=CfprFabricVlanSharingType
_CfprVnicEtherIfSharing_Object=MibTableColumn
cfprVnicEtherIfSharing=_CfprVnicEtherIfSharing_Object((1,3,6,1,4,1,9,9,826,1,83,13,1,14),_CfprVnicEtherIfSharing_Type())
cfprVnicEtherIfSharing.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicEtherIfSharing.setStatus(_A)
_CfprVnicEtherIfSwitchId_Type=CfprVnicL2IfSwitchId
_CfprVnicEtherIfSwitchId_Object=MibTableColumn
cfprVnicEtherIfSwitchId=_CfprVnicEtherIfSwitchId_Object((1,3,6,1,4,1,9,9,826,1,83,13,1,15),_CfprVnicEtherIfSwitchId_Type())
cfprVnicEtherIfSwitchId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicEtherIfSwitchId.setStatus(_A)
_CfprVnicEtherIfType_Type=CfprVnicAEtherIfType
_CfprVnicEtherIfType_Object=MibTableColumn
cfprVnicEtherIfType=_CfprVnicEtherIfType_Object((1,3,6,1,4,1,9,9,826,1,83,13,1,16),_CfprVnicEtherIfType_Type())
cfprVnicEtherIfType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicEtherIfType.setStatus(_A)
_CfprVnicEtherIfVnet_Type=Gauge32
_CfprVnicEtherIfVnet_Object=MibTableColumn
cfprVnicEtherIfVnet=_CfprVnicEtherIfVnet_Object((1,3,6,1,4,1,9,9,826,1,83,13,1,17),_CfprVnicEtherIfVnet_Type())
cfprVnicEtherIfVnet.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicEtherIfVnet.setStatus(_A)
_CfprVnicFcTable_Object=MibTable
cfprVnicFcTable=_CfprVnicFcTable_Object((1,3,6,1,4,1,9,9,826,1,83,14))
if mibBuilder.loadTexts:cfprVnicFcTable.setStatus(_A)
_CfprVnicFcEntry_Object=MibTableRow
cfprVnicFcEntry=_CfprVnicFcEntry_Object((1,3,6,1,4,1,9,9,826,1,83,14,1))
cfprVnicFcEntry.setIndexNames((0,_C,_R))
if mibBuilder.loadTexts:cfprVnicFcEntry.setStatus(_A)
_CfprVnicFcInstanceId_Type=CfprManagedObjectId
_CfprVnicFcInstanceId_Object=MibTableColumn
cfprVnicFcInstanceId=_CfprVnicFcInstanceId_Object((1,3,6,1,4,1,9,9,826,1,83,14,1,1),_CfprVnicFcInstanceId_Type())
cfprVnicFcInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprVnicFcInstanceId.setStatus(_A)
_CfprVnicFcDn_Type=CfprManagedObjectDn
_CfprVnicFcDn_Object=MibTableColumn
cfprVnicFcDn=_CfprVnicFcDn_Object((1,3,6,1,4,1,9,9,826,1,83,14,1,2),_CfprVnicFcDn_Type())
cfprVnicFcDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicFcDn.setStatus(_A)
_CfprVnicFcRn_Type=SnmpAdminString
_CfprVnicFcRn_Object=MibTableColumn
cfprVnicFcRn=_CfprVnicFcRn_Object((1,3,6,1,4,1,9,9,826,1,83,14,1,3),_CfprVnicFcRn_Type())
cfprVnicFcRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicFcRn.setStatus(_A)
_CfprVnicFcAdaptorProfileName_Type=SnmpAdminString
_CfprVnicFcAdaptorProfileName_Object=MibTableColumn
cfprVnicFcAdaptorProfileName=_CfprVnicFcAdaptorProfileName_Object((1,3,6,1,4,1,9,9,826,1,83,14,1,4),_CfprVnicFcAdaptorProfileName_Type())
cfprVnicFcAdaptorProfileName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicFcAdaptorProfileName.setStatus(_A)
_CfprVnicFcAddr_Type=Unsigned64
_CfprVnicFcAddr_Object=MibTableColumn
cfprVnicFcAddr=_CfprVnicFcAddr_Object((1,3,6,1,4,1,9,9,826,1,83,14,1,5),_CfprVnicFcAddr_Type())
cfprVnicFcAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicFcAddr.setStatus(_A)
_CfprVnicFcAdminHostPort_Type=CfprFabricHostPortId
_CfprVnicFcAdminHostPort_Object=MibTableColumn
cfprVnicFcAdminHostPort=_CfprVnicFcAdminHostPort_Object((1,3,6,1,4,1,9,9,826,1,83,14,1,6),_CfprVnicFcAdminHostPort_Type())
cfprVnicFcAdminHostPort.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicFcAdminHostPort.setStatus(_A)
_CfprVnicFcAdminVcon_Type=SnmpAdminString
_CfprVnicFcAdminVcon_Object=MibTableColumn
cfprVnicFcAdminVcon=_CfprVnicFcAdminVcon_Object((1,3,6,1,4,1,9,9,826,1,83,14,1,7),_CfprVnicFcAdminVcon_Type())
cfprVnicFcAdminVcon.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicFcAdminVcon.setStatus(_A)
_CfprVnicFcAppRole_Type=CfprVnicAppRole
_CfprVnicFcAppRole_Object=MibTableColumn
cfprVnicFcAppRole=_CfprVnicFcAppRole_Object((1,3,6,1,4,1,9,9,826,1,83,14,1,8),_CfprVnicFcAppRole_Type())
cfprVnicFcAppRole.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicFcAppRole.setStatus(_A)
_CfprVnicFcBootDev_Type=CfprVnicVnicBootDev
_CfprVnicFcBootDev_Object=MibTableColumn
cfprVnicFcBootDev=_CfprVnicFcBootDev_Object((1,3,6,1,4,1,9,9,826,1,83,14,1,9),_CfprVnicFcBootDev_Type())
cfprVnicFcBootDev.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicFcBootDev.setStatus(_A)
_CfprVnicFcConfigQualifier_Type=CfprVnicConfigIssues
_CfprVnicFcConfigQualifier_Object=MibTableColumn
cfprVnicFcConfigQualifier=_CfprVnicFcConfigQualifier_Object((1,3,6,1,4,1,9,9,826,1,83,14,1,10),_CfprVnicFcConfigQualifier_Type())
cfprVnicFcConfigQualifier.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicFcConfigQualifier.setStatus(_A)
_CfprVnicFcConfigState_Type=CfprLsConfigState
_CfprVnicFcConfigState_Object=MibTableColumn
cfprVnicFcConfigState=_CfprVnicFcConfigState_Object((1,3,6,1,4,1,9,9,826,1,83,14,1,11),_CfprVnicFcConfigState_Type())
cfprVnicFcConfigState.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicFcConfigState.setStatus(_A)
_CfprVnicFcEquipmentDn_Type=SnmpAdminString
_CfprVnicFcEquipmentDn_Object=MibTableColumn
cfprVnicFcEquipmentDn=_CfprVnicFcEquipmentDn_Object((1,3,6,1,4,1,9,9,826,1,83,14,1,12),_CfprVnicFcEquipmentDn_Type())
cfprVnicFcEquipmentDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicFcEquipmentDn.setStatus(_A)
_CfprVnicFcFltAggr_Type=Unsigned64
_CfprVnicFcFltAggr_Object=MibTableColumn
cfprVnicFcFltAggr=_CfprVnicFcFltAggr_Object((1,3,6,1,4,1,9,9,826,1,83,14,1,13),_CfprVnicFcFltAggr_Type())
cfprVnicFcFltAggr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicFcFltAggr.setStatus(_A)
_CfprVnicFcIdentPoolName_Type=SnmpAdminString
_CfprVnicFcIdentPoolName_Object=MibTableColumn
cfprVnicFcIdentPoolName=_CfprVnicFcIdentPoolName_Object((1,3,6,1,4,1,9,9,826,1,83,14,1,14),_CfprVnicFcIdentPoolName_Type())
cfprVnicFcIdentPoolName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicFcIdentPoolName.setStatus(_A)
_CfprVnicFcInstType_Type=CfprVnicInstantiation
_CfprVnicFcInstType_Object=MibTableColumn
cfprVnicFcInstType=_CfprVnicFcInstType_Object((1,3,6,1,4,1,9,9,826,1,83,14,1,15),_CfprVnicFcInstType_Type())
cfprVnicFcInstType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicFcInstType.setStatus(_A)
_CfprVnicFcMaxDataFieldSize_Type=Gauge32
_CfprVnicFcMaxDataFieldSize_Object=MibTableColumn
cfprVnicFcMaxDataFieldSize=_CfprVnicFcMaxDataFieldSize_Object((1,3,6,1,4,1,9,9,826,1,83,14,1,16),_CfprVnicFcMaxDataFieldSize_Type())
cfprVnicFcMaxDataFieldSize.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicFcMaxDataFieldSize.setStatus(_A)
_CfprVnicFcName_Type=SnmpAdminString
_CfprVnicFcName_Object=MibTableColumn
cfprVnicFcName=_CfprVnicFcName_Object((1,3,6,1,4,1,9,9,826,1,83,14,1,17),_CfprVnicFcName_Type())
cfprVnicFcName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicFcName.setStatus(_A)
_CfprVnicFcNodeAddr_Type=Unsigned64
_CfprVnicFcNodeAddr_Object=MibTableColumn
cfprVnicFcNodeAddr=_CfprVnicFcNodeAddr_Object((1,3,6,1,4,1,9,9,826,1,83,14,1,18),_CfprVnicFcNodeAddr_Type())
cfprVnicFcNodeAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicFcNodeAddr.setStatus(_A)
_CfprVnicFcNwTemplName_Type=SnmpAdminString
_CfprVnicFcNwTemplName_Object=MibTableColumn
cfprVnicFcNwTemplName=_CfprVnicFcNwTemplName_Object((1,3,6,1,4,1,9,9,826,1,83,14,1,19),_CfprVnicFcNwTemplName_Type())
cfprVnicFcNwTemplName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicFcNwTemplName.setStatus(_A)
_CfprVnicFcOperAdaptorProfileName_Type=SnmpAdminString
_CfprVnicFcOperAdaptorProfileName_Object=MibTableColumn
cfprVnicFcOperAdaptorProfileName=_CfprVnicFcOperAdaptorProfileName_Object((1,3,6,1,4,1,9,9,826,1,83,14,1,20),_CfprVnicFcOperAdaptorProfileName_Type())
cfprVnicFcOperAdaptorProfileName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicFcOperAdaptorProfileName.setStatus(_A)
_CfprVnicFcOperHostPort_Type=CfprVnicVnicOperHostPort
_CfprVnicFcOperHostPort_Object=MibTableColumn
cfprVnicFcOperHostPort=_CfprVnicFcOperHostPort_Object((1,3,6,1,4,1,9,9,826,1,83,14,1,21),_CfprVnicFcOperHostPort_Type())
cfprVnicFcOperHostPort.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicFcOperHostPort.setStatus(_A)
_CfprVnicFcOperIdentPoolName_Type=SnmpAdminString
_CfprVnicFcOperIdentPoolName_Object=MibTableColumn
cfprVnicFcOperIdentPoolName=_CfprVnicFcOperIdentPoolName_Object((1,3,6,1,4,1,9,9,826,1,83,14,1,22),_CfprVnicFcOperIdentPoolName_Type())
cfprVnicFcOperIdentPoolName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicFcOperIdentPoolName.setStatus(_A)
_CfprVnicFcOperNwTemplName_Type=SnmpAdminString
_CfprVnicFcOperNwTemplName_Object=MibTableColumn
cfprVnicFcOperNwTemplName=_CfprVnicFcOperNwTemplName_Object((1,3,6,1,4,1,9,9,826,1,83,14,1,23),_CfprVnicFcOperNwTemplName_Type())
cfprVnicFcOperNwTemplName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicFcOperNwTemplName.setStatus(_A)
_CfprVnicFcOperOrder_Type=Gauge32
_CfprVnicFcOperOrder_Object=MibTableColumn
cfprVnicFcOperOrder=_CfprVnicFcOperOrder_Object((1,3,6,1,4,1,9,9,826,1,83,14,1,24),_CfprVnicFcOperOrder_Type())
cfprVnicFcOperOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicFcOperOrder.setStatus(_A)
_CfprVnicFcOperPinToGroupName_Type=SnmpAdminString
_CfprVnicFcOperPinToGroupName_Object=MibTableColumn
cfprVnicFcOperPinToGroupName=_CfprVnicFcOperPinToGroupName_Object((1,3,6,1,4,1,9,9,826,1,83,14,1,25),_CfprVnicFcOperPinToGroupName_Type())
cfprVnicFcOperPinToGroupName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicFcOperPinToGroupName.setStatus(_A)
_CfprVnicFcOperQosPolicyName_Type=SnmpAdminString
_CfprVnicFcOperQosPolicyName_Object=MibTableColumn
cfprVnicFcOperQosPolicyName=_CfprVnicFcOperQosPolicyName_Object((1,3,6,1,4,1,9,9,826,1,83,14,1,26),_CfprVnicFcOperQosPolicyName_Type())
cfprVnicFcOperQosPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicFcOperQosPolicyName.setStatus(_A)
_CfprVnicFcOperSpeed_Type=Gauge32
_CfprVnicFcOperSpeed_Object=MibTableColumn
cfprVnicFcOperSpeed=_CfprVnicFcOperSpeed_Object((1,3,6,1,4,1,9,9,826,1,83,14,1,27),_CfprVnicFcOperSpeed_Type())
cfprVnicFcOperSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicFcOperSpeed.setStatus(_A)
_CfprVnicFcOperStatsPolicyName_Type=SnmpAdminString
_CfprVnicFcOperStatsPolicyName_Object=MibTableColumn
cfprVnicFcOperStatsPolicyName=_CfprVnicFcOperStatsPolicyName_Object((1,3,6,1,4,1,9,9,826,1,83,14,1,28),_CfprVnicFcOperStatsPolicyName_Type())
cfprVnicFcOperStatsPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicFcOperStatsPolicyName.setStatus(_A)
_CfprVnicFcOperVcon_Type=SnmpAdminString
_CfprVnicFcOperVcon_Object=MibTableColumn
cfprVnicFcOperVcon=_CfprVnicFcOperVcon_Object((1,3,6,1,4,1,9,9,826,1,83,14,1,29),_CfprVnicFcOperVcon_Type())
cfprVnicFcOperVcon.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicFcOperVcon.setStatus(_A)
_CfprVnicFcOrder_Type=Gauge32
_CfprVnicFcOrder_Object=MibTableColumn
cfprVnicFcOrder=_CfprVnicFcOrder_Object((1,3,6,1,4,1,9,9,826,1,83,14,1,30),_CfprVnicFcOrder_Type())
cfprVnicFcOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicFcOrder.setStatus(_A)
_CfprVnicFcOwner_Type=CfprVnicConnectionOwner
_CfprVnicFcOwner_Object=MibTableColumn
cfprVnicFcOwner=_CfprVnicFcOwner_Object((1,3,6,1,4,1,9,9,826,1,83,14,1,31),_CfprVnicFcOwner_Type())
cfprVnicFcOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicFcOwner.setStatus(_A)
_CfprVnicFcPersBind_Type=CfprVnicFcBasePersBind
_CfprVnicFcPersBind_Object=MibTableColumn
cfprVnicFcPersBind=_CfprVnicFcPersBind_Object((1,3,6,1,4,1,9,9,826,1,83,14,1,32),_CfprVnicFcPersBind_Type())
cfprVnicFcPersBind.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicFcPersBind.setStatus(_A)
_CfprVnicFcPersBindClear_Type=TruthValue
_CfprVnicFcPersBindClear_Object=MibTableColumn
cfprVnicFcPersBindClear=_CfprVnicFcPersBindClear_Object((1,3,6,1,4,1,9,9,826,1,83,14,1,33),_CfprVnicFcPersBindClear_Type())
cfprVnicFcPersBindClear.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicFcPersBindClear.setStatus(_A)
_CfprVnicFcPinToGroupName_Type=SnmpAdminString
_CfprVnicFcPinToGroupName_Object=MibTableColumn
cfprVnicFcPinToGroupName=_CfprVnicFcPinToGroupName_Object((1,3,6,1,4,1,9,9,826,1,83,14,1,34),_CfprVnicFcPinToGroupName_Type())
cfprVnicFcPinToGroupName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicFcPinToGroupName.setStatus(_A)
_CfprVnicFcQosPolicyName_Type=SnmpAdminString
_CfprVnicFcQosPolicyName_Object=MibTableColumn
cfprVnicFcQosPolicyName=_CfprVnicFcQosPolicyName_Object((1,3,6,1,4,1,9,9,826,1,83,14,1,35),_CfprVnicFcQosPolicyName_Type())
cfprVnicFcQosPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicFcQosPolicyName.setStatus(_A)
_CfprVnicFcStatsPolicyName_Type=SnmpAdminString
_CfprVnicFcStatsPolicyName_Object=MibTableColumn
cfprVnicFcStatsPolicyName=_CfprVnicFcStatsPolicyName_Object((1,3,6,1,4,1,9,9,826,1,83,14,1,36),_CfprVnicFcStatsPolicyName_Type())
cfprVnicFcStatsPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicFcStatsPolicyName.setStatus(_A)
_CfprVnicFcSwitchId_Type=CfprNetworkSwitchId
_CfprVnicFcSwitchId_Object=MibTableColumn
cfprVnicFcSwitchId=_CfprVnicFcSwitchId_Object((1,3,6,1,4,1,9,9,826,1,83,14,1,37),_CfprVnicFcSwitchId_Type())
cfprVnicFcSwitchId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicFcSwitchId.setStatus(_A)
_CfprVnicFcType_Type=CfprVnicFcBaseType
_CfprVnicFcType_Object=MibTableColumn
cfprVnicFcType=_CfprVnicFcType_Object((1,3,6,1,4,1,9,9,826,1,83,14,1,38),_CfprVnicFcType_Type())
cfprVnicFcType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicFcType.setStatus(_A)
_CfprVnicFcGroupDefTable_Object=MibTable
cfprVnicFcGroupDefTable=_CfprVnicFcGroupDefTable_Object((1,3,6,1,4,1,9,9,826,1,83,15))
if mibBuilder.loadTexts:cfprVnicFcGroupDefTable.setStatus(_A)
_CfprVnicFcGroupDefEntry_Object=MibTableRow
cfprVnicFcGroupDefEntry=_CfprVnicFcGroupDefEntry_Object((1,3,6,1,4,1,9,9,826,1,83,15,1))
cfprVnicFcGroupDefEntry.setIndexNames((0,_C,_S))
if mibBuilder.loadTexts:cfprVnicFcGroupDefEntry.setStatus(_A)
_CfprVnicFcGroupDefInstanceId_Type=CfprManagedObjectId
_CfprVnicFcGroupDefInstanceId_Object=MibTableColumn
cfprVnicFcGroupDefInstanceId=_CfprVnicFcGroupDefInstanceId_Object((1,3,6,1,4,1,9,9,826,1,83,15,1,1),_CfprVnicFcGroupDefInstanceId_Type())
cfprVnicFcGroupDefInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprVnicFcGroupDefInstanceId.setStatus(_A)
_CfprVnicFcGroupDefDn_Type=CfprManagedObjectDn
_CfprVnicFcGroupDefDn_Object=MibTableColumn
cfprVnicFcGroupDefDn=_CfprVnicFcGroupDefDn_Object((1,3,6,1,4,1,9,9,826,1,83,15,1,2),_CfprVnicFcGroupDefDn_Type())
cfprVnicFcGroupDefDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicFcGroupDefDn.setStatus(_A)
_CfprVnicFcGroupDefRn_Type=SnmpAdminString
_CfprVnicFcGroupDefRn_Object=MibTableColumn
cfprVnicFcGroupDefRn=_CfprVnicFcGroupDefRn_Object((1,3,6,1,4,1,9,9,826,1,83,15,1,3),_CfprVnicFcGroupDefRn_Type())
cfprVnicFcGroupDefRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicFcGroupDefRn.setStatus(_A)
_CfprVnicFcGroupDefAdaptorProfileName_Type=SnmpAdminString
_CfprVnicFcGroupDefAdaptorProfileName_Object=MibTableColumn
cfprVnicFcGroupDefAdaptorProfileName=_CfprVnicFcGroupDefAdaptorProfileName_Object((1,3,6,1,4,1,9,9,826,1,83,15,1,4),_CfprVnicFcGroupDefAdaptorProfileName_Type())
cfprVnicFcGroupDefAdaptorProfileName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicFcGroupDefAdaptorProfileName.setStatus(_A)
_CfprVnicFcGroupDefDescr_Type=SnmpAdminString
_CfprVnicFcGroupDefDescr_Object=MibTableColumn
cfprVnicFcGroupDefDescr=_CfprVnicFcGroupDefDescr_Object((1,3,6,1,4,1,9,9,826,1,83,15,1,5),_CfprVnicFcGroupDefDescr_Type())
cfprVnicFcGroupDefDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicFcGroupDefDescr.setStatus(_A)
_CfprVnicFcGroupDefIdentPoolName_Type=SnmpAdminString
_CfprVnicFcGroupDefIdentPoolName_Object=MibTableColumn
cfprVnicFcGroupDefIdentPoolName=_CfprVnicFcGroupDefIdentPoolName_Object((1,3,6,1,4,1,9,9,826,1,83,15,1,6),_CfprVnicFcGroupDefIdentPoolName_Type())
cfprVnicFcGroupDefIdentPoolName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicFcGroupDefIdentPoolName.setStatus(_A)
_CfprVnicFcGroupDefIntId_Type=SnmpAdminString
_CfprVnicFcGroupDefIntId_Object=MibTableColumn
cfprVnicFcGroupDefIntId=_CfprVnicFcGroupDefIntId_Object((1,3,6,1,4,1,9,9,826,1,83,15,1,7),_CfprVnicFcGroupDefIntId_Type())
cfprVnicFcGroupDefIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicFcGroupDefIntId.setStatus(_A)
_CfprVnicFcGroupDefMaxDataFieldSize_Type=Gauge32
_CfprVnicFcGroupDefMaxDataFieldSize_Object=MibTableColumn
cfprVnicFcGroupDefMaxDataFieldSize=_CfprVnicFcGroupDefMaxDataFieldSize_Object((1,3,6,1,4,1,9,9,826,1,83,15,1,8),_CfprVnicFcGroupDefMaxDataFieldSize_Type())
cfprVnicFcGroupDefMaxDataFieldSize.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicFcGroupDefMaxDataFieldSize.setStatus(_A)
_CfprVnicFcGroupDefName_Type=SnmpAdminString
_CfprVnicFcGroupDefName_Object=MibTableColumn
cfprVnicFcGroupDefName=_CfprVnicFcGroupDefName_Object((1,3,6,1,4,1,9,9,826,1,83,15,1,9),_CfprVnicFcGroupDefName_Type())
cfprVnicFcGroupDefName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicFcGroupDefName.setStatus(_A)
_CfprVnicFcGroupDefNwTemplName_Type=SnmpAdminString
_CfprVnicFcGroupDefNwTemplName_Object=MibTableColumn
cfprVnicFcGroupDefNwTemplName=_CfprVnicFcGroupDefNwTemplName_Object((1,3,6,1,4,1,9,9,826,1,83,15,1,10),_CfprVnicFcGroupDefNwTemplName_Type())
cfprVnicFcGroupDefNwTemplName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicFcGroupDefNwTemplName.setStatus(_A)
_CfprVnicFcGroupDefOperStatsPolicyName_Type=SnmpAdminString
_CfprVnicFcGroupDefOperStatsPolicyName_Object=MibTableColumn
cfprVnicFcGroupDefOperStatsPolicyName=_CfprVnicFcGroupDefOperStatsPolicyName_Object((1,3,6,1,4,1,9,9,826,1,83,15,1,11),_CfprVnicFcGroupDefOperStatsPolicyName_Type())
cfprVnicFcGroupDefOperStatsPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicFcGroupDefOperStatsPolicyName.setStatus(_A)
_CfprVnicFcGroupDefOperStorageConnPolicyName_Type=SnmpAdminString
_CfprVnicFcGroupDefOperStorageConnPolicyName_Object=MibTableColumn
cfprVnicFcGroupDefOperStorageConnPolicyName=_CfprVnicFcGroupDefOperStorageConnPolicyName_Object((1,3,6,1,4,1,9,9,826,1,83,15,1,12),_CfprVnicFcGroupDefOperStorageConnPolicyName_Type())
cfprVnicFcGroupDefOperStorageConnPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicFcGroupDefOperStorageConnPolicyName.setStatus(_A)
_CfprVnicFcGroupDefPolicyLevel_Type=Gauge32
_CfprVnicFcGroupDefPolicyLevel_Object=MibTableColumn
cfprVnicFcGroupDefPolicyLevel=_CfprVnicFcGroupDefPolicyLevel_Object((1,3,6,1,4,1,9,9,826,1,83,15,1,13),_CfprVnicFcGroupDefPolicyLevel_Type())
cfprVnicFcGroupDefPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicFcGroupDefPolicyLevel.setStatus(_A)
_CfprVnicFcGroupDefPolicyOwner_Type=CfprPolicyPolicyOwner
_CfprVnicFcGroupDefPolicyOwner_Object=MibTableColumn
cfprVnicFcGroupDefPolicyOwner=_CfprVnicFcGroupDefPolicyOwner_Object((1,3,6,1,4,1,9,9,826,1,83,15,1,14),_CfprVnicFcGroupDefPolicyOwner_Type())
cfprVnicFcGroupDefPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicFcGroupDefPolicyOwner.setStatus(_A)
_CfprVnicFcGroupDefQosPolicyName_Type=SnmpAdminString
_CfprVnicFcGroupDefQosPolicyName_Object=MibTableColumn
cfprVnicFcGroupDefQosPolicyName=_CfprVnicFcGroupDefQosPolicyName_Object((1,3,6,1,4,1,9,9,826,1,83,15,1,15),_CfprVnicFcGroupDefQosPolicyName_Type())
cfprVnicFcGroupDefQosPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicFcGroupDefQosPolicyName.setStatus(_A)
_CfprVnicFcGroupDefStatsPolicyName_Type=SnmpAdminString
_CfprVnicFcGroupDefStatsPolicyName_Object=MibTableColumn
cfprVnicFcGroupDefStatsPolicyName=_CfprVnicFcGroupDefStatsPolicyName_Object((1,3,6,1,4,1,9,9,826,1,83,15,1,16),_CfprVnicFcGroupDefStatsPolicyName_Type())
cfprVnicFcGroupDefStatsPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicFcGroupDefStatsPolicyName.setStatus(_A)
_CfprVnicFcGroupDefStorageConnPolicyName_Type=SnmpAdminString
_CfprVnicFcGroupDefStorageConnPolicyName_Object=MibTableColumn
cfprVnicFcGroupDefStorageConnPolicyName=_CfprVnicFcGroupDefStorageConnPolicyName_Object((1,3,6,1,4,1,9,9,826,1,83,15,1,17),_CfprVnicFcGroupDefStorageConnPolicyName_Type())
cfprVnicFcGroupDefStorageConnPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicFcGroupDefStorageConnPolicyName.setStatus(_A)
_CfprVnicFcGroupTemplTable_Object=MibTable
cfprVnicFcGroupTemplTable=_CfprVnicFcGroupTemplTable_Object((1,3,6,1,4,1,9,9,826,1,83,16))
if mibBuilder.loadTexts:cfprVnicFcGroupTemplTable.setStatus(_A)
_CfprVnicFcGroupTemplEntry_Object=MibTableRow
cfprVnicFcGroupTemplEntry=_CfprVnicFcGroupTemplEntry_Object((1,3,6,1,4,1,9,9,826,1,83,16,1))
cfprVnicFcGroupTemplEntry.setIndexNames((0,_C,_T))
if mibBuilder.loadTexts:cfprVnicFcGroupTemplEntry.setStatus(_A)
_CfprVnicFcGroupTemplInstanceId_Type=CfprManagedObjectId
_CfprVnicFcGroupTemplInstanceId_Object=MibTableColumn
cfprVnicFcGroupTemplInstanceId=_CfprVnicFcGroupTemplInstanceId_Object((1,3,6,1,4,1,9,9,826,1,83,16,1,1),_CfprVnicFcGroupTemplInstanceId_Type())
cfprVnicFcGroupTemplInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprVnicFcGroupTemplInstanceId.setStatus(_A)
_CfprVnicFcGroupTemplDn_Type=CfprManagedObjectDn
_CfprVnicFcGroupTemplDn_Object=MibTableColumn
cfprVnicFcGroupTemplDn=_CfprVnicFcGroupTemplDn_Object((1,3,6,1,4,1,9,9,826,1,83,16,1,2),_CfprVnicFcGroupTemplDn_Type())
cfprVnicFcGroupTemplDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicFcGroupTemplDn.setStatus(_A)
_CfprVnicFcGroupTemplRn_Type=SnmpAdminString
_CfprVnicFcGroupTemplRn_Object=MibTableColumn
cfprVnicFcGroupTemplRn=_CfprVnicFcGroupTemplRn_Object((1,3,6,1,4,1,9,9,826,1,83,16,1,3),_CfprVnicFcGroupTemplRn_Type())
cfprVnicFcGroupTemplRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicFcGroupTemplRn.setStatus(_A)
_CfprVnicFcGroupTemplAdaptorProfileName_Type=SnmpAdminString
_CfprVnicFcGroupTemplAdaptorProfileName_Object=MibTableColumn
cfprVnicFcGroupTemplAdaptorProfileName=_CfprVnicFcGroupTemplAdaptorProfileName_Object((1,3,6,1,4,1,9,9,826,1,83,16,1,4),_CfprVnicFcGroupTemplAdaptorProfileName_Type())
cfprVnicFcGroupTemplAdaptorProfileName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicFcGroupTemplAdaptorProfileName.setStatus(_A)
_CfprVnicFcGroupTemplDescr_Type=SnmpAdminString
_CfprVnicFcGroupTemplDescr_Object=MibTableColumn
cfprVnicFcGroupTemplDescr=_CfprVnicFcGroupTemplDescr_Object((1,3,6,1,4,1,9,9,826,1,83,16,1,5),_CfprVnicFcGroupTemplDescr_Type())
cfprVnicFcGroupTemplDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicFcGroupTemplDescr.setStatus(_A)
_CfprVnicFcGroupTemplIdentPoolName_Type=SnmpAdminString
_CfprVnicFcGroupTemplIdentPoolName_Object=MibTableColumn
cfprVnicFcGroupTemplIdentPoolName=_CfprVnicFcGroupTemplIdentPoolName_Object((1,3,6,1,4,1,9,9,826,1,83,16,1,6),_CfprVnicFcGroupTemplIdentPoolName_Type())
cfprVnicFcGroupTemplIdentPoolName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicFcGroupTemplIdentPoolName.setStatus(_A)
_CfprVnicFcGroupTemplIntId_Type=SnmpAdminString
_CfprVnicFcGroupTemplIntId_Object=MibTableColumn
cfprVnicFcGroupTemplIntId=_CfprVnicFcGroupTemplIntId_Object((1,3,6,1,4,1,9,9,826,1,83,16,1,7),_CfprVnicFcGroupTemplIntId_Type())
cfprVnicFcGroupTemplIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicFcGroupTemplIntId.setStatus(_A)
_CfprVnicFcGroupTemplMaxDataFieldSize_Type=Gauge32
_CfprVnicFcGroupTemplMaxDataFieldSize_Object=MibTableColumn
cfprVnicFcGroupTemplMaxDataFieldSize=_CfprVnicFcGroupTemplMaxDataFieldSize_Object((1,3,6,1,4,1,9,9,826,1,83,16,1,8),_CfprVnicFcGroupTemplMaxDataFieldSize_Type())
cfprVnicFcGroupTemplMaxDataFieldSize.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicFcGroupTemplMaxDataFieldSize.setStatus(_A)
_CfprVnicFcGroupTemplName_Type=SnmpAdminString
_CfprVnicFcGroupTemplName_Object=MibTableColumn
cfprVnicFcGroupTemplName=_CfprVnicFcGroupTemplName_Object((1,3,6,1,4,1,9,9,826,1,83,16,1,9),_CfprVnicFcGroupTemplName_Type())
cfprVnicFcGroupTemplName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicFcGroupTemplName.setStatus(_A)
_CfprVnicFcGroupTemplNwTemplName_Type=SnmpAdminString
_CfprVnicFcGroupTemplNwTemplName_Object=MibTableColumn
cfprVnicFcGroupTemplNwTemplName=_CfprVnicFcGroupTemplNwTemplName_Object((1,3,6,1,4,1,9,9,826,1,83,16,1,10),_CfprVnicFcGroupTemplNwTemplName_Type())
cfprVnicFcGroupTemplNwTemplName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicFcGroupTemplNwTemplName.setStatus(_A)
_CfprVnicFcGroupTemplOperStatsPolicyName_Type=SnmpAdminString
_CfprVnicFcGroupTemplOperStatsPolicyName_Object=MibTableColumn
cfprVnicFcGroupTemplOperStatsPolicyName=_CfprVnicFcGroupTemplOperStatsPolicyName_Object((1,3,6,1,4,1,9,9,826,1,83,16,1,11),_CfprVnicFcGroupTemplOperStatsPolicyName_Type())
cfprVnicFcGroupTemplOperStatsPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicFcGroupTemplOperStatsPolicyName.setStatus(_A)
_CfprVnicFcGroupTemplOperStorageConnPolicyName_Type=SnmpAdminString
_CfprVnicFcGroupTemplOperStorageConnPolicyName_Object=MibTableColumn
cfprVnicFcGroupTemplOperStorageConnPolicyName=_CfprVnicFcGroupTemplOperStorageConnPolicyName_Object((1,3,6,1,4,1,9,9,826,1,83,16,1,12),_CfprVnicFcGroupTemplOperStorageConnPolicyName_Type())
cfprVnicFcGroupTemplOperStorageConnPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicFcGroupTemplOperStorageConnPolicyName.setStatus(_A)
_CfprVnicFcGroupTemplPolicyLevel_Type=Gauge32
_CfprVnicFcGroupTemplPolicyLevel_Object=MibTableColumn
cfprVnicFcGroupTemplPolicyLevel=_CfprVnicFcGroupTemplPolicyLevel_Object((1,3,6,1,4,1,9,9,826,1,83,16,1,13),_CfprVnicFcGroupTemplPolicyLevel_Type())
cfprVnicFcGroupTemplPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicFcGroupTemplPolicyLevel.setStatus(_A)
_CfprVnicFcGroupTemplPolicyOwner_Type=CfprPolicyPolicyOwner
_CfprVnicFcGroupTemplPolicyOwner_Object=MibTableColumn
cfprVnicFcGroupTemplPolicyOwner=_CfprVnicFcGroupTemplPolicyOwner_Object((1,3,6,1,4,1,9,9,826,1,83,16,1,14),_CfprVnicFcGroupTemplPolicyOwner_Type())
cfprVnicFcGroupTemplPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicFcGroupTemplPolicyOwner.setStatus(_A)
_CfprVnicFcGroupTemplQosPolicyName_Type=SnmpAdminString
_CfprVnicFcGroupTemplQosPolicyName_Object=MibTableColumn
cfprVnicFcGroupTemplQosPolicyName=_CfprVnicFcGroupTemplQosPolicyName_Object((1,3,6,1,4,1,9,9,826,1,83,16,1,15),_CfprVnicFcGroupTemplQosPolicyName_Type())
cfprVnicFcGroupTemplQosPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicFcGroupTemplQosPolicyName.setStatus(_A)
_CfprVnicFcGroupTemplStatsPolicyName_Type=SnmpAdminString
_CfprVnicFcGroupTemplStatsPolicyName_Object=MibTableColumn
cfprVnicFcGroupTemplStatsPolicyName=_CfprVnicFcGroupTemplStatsPolicyName_Object((1,3,6,1,4,1,9,9,826,1,83,16,1,16),_CfprVnicFcGroupTemplStatsPolicyName_Type())
cfprVnicFcGroupTemplStatsPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicFcGroupTemplStatsPolicyName.setStatus(_A)
_CfprVnicFcGroupTemplStorageConnPolicyName_Type=SnmpAdminString
_CfprVnicFcGroupTemplStorageConnPolicyName_Object=MibTableColumn
cfprVnicFcGroupTemplStorageConnPolicyName=_CfprVnicFcGroupTemplStorageConnPolicyName_Object((1,3,6,1,4,1,9,9,826,1,83,16,1,17),_CfprVnicFcGroupTemplStorageConnPolicyName_Type())
cfprVnicFcGroupTemplStorageConnPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicFcGroupTemplStorageConnPolicyName.setStatus(_A)
_CfprVnicFcGroupTemplTemplType_Type=CfprVnicTemplateType
_CfprVnicFcGroupTemplTemplType_Object=MibTableColumn
cfprVnicFcGroupTemplTemplType=_CfprVnicFcGroupTemplTemplType_Object((1,3,6,1,4,1,9,9,826,1,83,16,1,18),_CfprVnicFcGroupTemplTemplType_Type())
cfprVnicFcGroupTemplTemplType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicFcGroupTemplTemplType.setStatus(_A)
_CfprVnicFcIfTable_Object=MibTable
cfprVnicFcIfTable=_CfprVnicFcIfTable_Object((1,3,6,1,4,1,9,9,826,1,83,17))
if mibBuilder.loadTexts:cfprVnicFcIfTable.setStatus(_A)
_CfprVnicFcIfEntry_Object=MibTableRow
cfprVnicFcIfEntry=_CfprVnicFcIfEntry_Object((1,3,6,1,4,1,9,9,826,1,83,17,1))
cfprVnicFcIfEntry.setIndexNames((0,_C,_U))
if mibBuilder.loadTexts:cfprVnicFcIfEntry.setStatus(_A)
_CfprVnicFcIfInstanceId_Type=CfprManagedObjectId
_CfprVnicFcIfInstanceId_Object=MibTableColumn
cfprVnicFcIfInstanceId=_CfprVnicFcIfInstanceId_Object((1,3,6,1,4,1,9,9,826,1,83,17,1,1),_CfprVnicFcIfInstanceId_Type())
cfprVnicFcIfInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprVnicFcIfInstanceId.setStatus(_A)
_CfprVnicFcIfDn_Type=CfprManagedObjectDn
_CfprVnicFcIfDn_Object=MibTableColumn
cfprVnicFcIfDn=_CfprVnicFcIfDn_Object((1,3,6,1,4,1,9,9,826,1,83,17,1,2),_CfprVnicFcIfDn_Type())
cfprVnicFcIfDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicFcIfDn.setStatus(_A)
_CfprVnicFcIfRn_Type=SnmpAdminString
_CfprVnicFcIfRn_Object=MibTableColumn
cfprVnicFcIfRn=_CfprVnicFcIfRn_Object((1,3,6,1,4,1,9,9,826,1,83,17,1,3),_CfprVnicFcIfRn_Type())
cfprVnicFcIfRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicFcIfRn.setStatus(_A)
_CfprVnicFcIfConfigQualifier_Type=CfprVnicConfigIssues
_CfprVnicFcIfConfigQualifier_Object=MibTableColumn
cfprVnicFcIfConfigQualifier=_CfprVnicFcIfConfigQualifier_Object((1,3,6,1,4,1,9,9,826,1,83,17,1,4),_CfprVnicFcIfConfigQualifier_Type())
cfprVnicFcIfConfigQualifier.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicFcIfConfigQualifier.setStatus(_A)
_CfprVnicFcIfInitiator_Type=Unsigned64
_CfprVnicFcIfInitiator_Object=MibTableColumn
cfprVnicFcIfInitiator=_CfprVnicFcIfInitiator_Object((1,3,6,1,4,1,9,9,826,1,83,17,1,5),_CfprVnicFcIfInitiator_Type())
cfprVnicFcIfInitiator.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicFcIfInitiator.setStatus(_A)
_CfprVnicFcIfName_Type=SnmpAdminString
_CfprVnicFcIfName_Object=MibTableColumn
cfprVnicFcIfName=_CfprVnicFcIfName_Object((1,3,6,1,4,1,9,9,826,1,83,17,1,6),_CfprVnicFcIfName_Type())
cfprVnicFcIfName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicFcIfName.setStatus(_A)
_CfprVnicFcIfOperState_Type=CfprVnicIfOperState
_CfprVnicFcIfOperState_Object=MibTableColumn
cfprVnicFcIfOperState=_CfprVnicFcIfOperState_Object((1,3,6,1,4,1,9,9,826,1,83,17,1,7),_CfprVnicFcIfOperState_Type())
cfprVnicFcIfOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicFcIfOperState.setStatus(_A)
_CfprVnicFcIfOperVnetDn_Type=SnmpAdminString
_CfprVnicFcIfOperVnetDn_Object=MibTableColumn
cfprVnicFcIfOperVnetDn=_CfprVnicFcIfOperVnetDn_Object((1,3,6,1,4,1,9,9,826,1,83,17,1,8),_CfprVnicFcIfOperVnetDn_Type())
cfprVnicFcIfOperVnetDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicFcIfOperVnetDn.setStatus(_A)
_CfprVnicFcIfOperVnetName_Type=SnmpAdminString
_CfprVnicFcIfOperVnetName_Object=MibTableColumn
cfprVnicFcIfOperVnetName=_CfprVnicFcIfOperVnetName_Object((1,3,6,1,4,1,9,9,826,1,83,17,1,9),_CfprVnicFcIfOperVnetName_Type())
cfprVnicFcIfOperVnetName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicFcIfOperVnetName.setStatus(_A)
_CfprVnicFcIfOwner_Type=CfprVnicConnectionOwner
_CfprVnicFcIfOwner_Object=MibTableColumn
cfprVnicFcIfOwner=_CfprVnicFcIfOwner_Object((1,3,6,1,4,1,9,9,826,1,83,17,1,10),_CfprVnicFcIfOwner_Type())
cfprVnicFcIfOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicFcIfOwner.setStatus(_A)
_CfprVnicFcIfPubNwId_Type=Gauge32
_CfprVnicFcIfPubNwId_Object=MibTableColumn
cfprVnicFcIfPubNwId=_CfprVnicFcIfPubNwId_Object((1,3,6,1,4,1,9,9,826,1,83,17,1,11),_CfprVnicFcIfPubNwId_Type())
cfprVnicFcIfPubNwId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicFcIfPubNwId.setStatus(_A)
_CfprVnicFcIfSharing_Type=CfprFabricVlanSharingType
_CfprVnicFcIfSharing_Object=MibTableColumn
cfprVnicFcIfSharing=_CfprVnicFcIfSharing_Object((1,3,6,1,4,1,9,9,826,1,83,17,1,12),_CfprVnicFcIfSharing_Type())
cfprVnicFcIfSharing.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicFcIfSharing.setStatus(_A)
_CfprVnicFcIfSwitchId_Type=CfprVnicL2IfSwitchId
_CfprVnicFcIfSwitchId_Object=MibTableColumn
cfprVnicFcIfSwitchId=_CfprVnicFcIfSwitchId_Object((1,3,6,1,4,1,9,9,826,1,83,17,1,13),_CfprVnicFcIfSwitchId_Type())
cfprVnicFcIfSwitchId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicFcIfSwitchId.setStatus(_A)
_CfprVnicFcIfType_Type=CfprVnicAFcIfType
_CfprVnicFcIfType_Object=MibTableColumn
cfprVnicFcIfType=_CfprVnicFcIfType_Object((1,3,6,1,4,1,9,9,826,1,83,17,1,14),_CfprVnicFcIfType_Type())
cfprVnicFcIfType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicFcIfType.setStatus(_A)
_CfprVnicFcIfVnet_Type=Gauge32
_CfprVnicFcIfVnet_Object=MibTableColumn
cfprVnicFcIfVnet=_CfprVnicFcIfVnet_Object((1,3,6,1,4,1,9,9,826,1,83,17,1,15),_CfprVnicFcIfVnet_Type())
cfprVnicFcIfVnet.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicFcIfVnet.setStatus(_A)
_CfprVnicFcLifTable_Object=MibTable
cfprVnicFcLifTable=_CfprVnicFcLifTable_Object((1,3,6,1,4,1,9,9,826,1,83,18))
if mibBuilder.loadTexts:cfprVnicFcLifTable.setStatus(_A)
_CfprVnicFcLifEntry_Object=MibTableRow
cfprVnicFcLifEntry=_CfprVnicFcLifEntry_Object((1,3,6,1,4,1,9,9,826,1,83,18,1))
cfprVnicFcLifEntry.setIndexNames((0,_C,_V))
if mibBuilder.loadTexts:cfprVnicFcLifEntry.setStatus(_A)
_CfprVnicFcLifInstanceId_Type=CfprManagedObjectId
_CfprVnicFcLifInstanceId_Object=MibTableColumn
cfprVnicFcLifInstanceId=_CfprVnicFcLifInstanceId_Object((1,3,6,1,4,1,9,9,826,1,83,18,1,1),_CfprVnicFcLifInstanceId_Type())
cfprVnicFcLifInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprVnicFcLifInstanceId.setStatus(_A)
_CfprVnicFcLifDn_Type=CfprManagedObjectDn
_CfprVnicFcLifDn_Object=MibTableColumn
cfprVnicFcLifDn=_CfprVnicFcLifDn_Object((1,3,6,1,4,1,9,9,826,1,83,18,1,2),_CfprVnicFcLifDn_Type())
cfprVnicFcLifDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicFcLifDn.setStatus(_A)
_CfprVnicFcLifRn_Type=SnmpAdminString
_CfprVnicFcLifRn_Object=MibTableColumn
cfprVnicFcLifRn=_CfprVnicFcLifRn_Object((1,3,6,1,4,1,9,9,826,1,83,18,1,3),_CfprVnicFcLifRn_Type())
cfprVnicFcLifRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicFcLifRn.setStatus(_A)
_CfprVnicFcLifAddr_Type=Unsigned64
_CfprVnicFcLifAddr_Object=MibTableColumn
cfprVnicFcLifAddr=_CfprVnicFcLifAddr_Object((1,3,6,1,4,1,9,9,826,1,83,18,1,4),_CfprVnicFcLifAddr_Type())
cfprVnicFcLifAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicFcLifAddr.setStatus(_A)
_CfprVnicFcLifName_Type=SnmpAdminString
_CfprVnicFcLifName_Object=MibTableColumn
cfprVnicFcLifName=_CfprVnicFcLifName_Object((1,3,6,1,4,1,9,9,826,1,83,18,1,5),_CfprVnicFcLifName_Type())
cfprVnicFcLifName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicFcLifName.setStatus(_A)
_CfprVnicFcLifNicDn_Type=SnmpAdminString
_CfprVnicFcLifNicDn_Object=MibTableColumn
cfprVnicFcLifNicDn=_CfprVnicFcLifNicDn_Object((1,3,6,1,4,1,9,9,826,1,83,18,1,6),_CfprVnicFcLifNicDn_Type())
cfprVnicFcLifNicDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicFcLifNicDn.setStatus(_A)
_CfprVnicFcLifOwner_Type=CfprVnicConnectionOwner
_CfprVnicFcLifOwner_Object=MibTableColumn
cfprVnicFcLifOwner=_CfprVnicFcLifOwner_Object((1,3,6,1,4,1,9,9,826,1,83,18,1,7),_CfprVnicFcLifOwner_Type())
cfprVnicFcLifOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicFcLifOwner.setStatus(_A)
_CfprVnicFcLifSwitchId_Type=CfprNetworkSwitchId
_CfprVnicFcLifSwitchId_Object=MibTableColumn
cfprVnicFcLifSwitchId=_CfprVnicFcLifSwitchId_Object((1,3,6,1,4,1,9,9,826,1,83,18,1,8),_CfprVnicFcLifSwitchId_Type())
cfprVnicFcLifSwitchId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicFcLifSwitchId.setStatus(_A)
_CfprVnicFcLifType_Type=CfprVnicConnectionType
_CfprVnicFcLifType_Object=MibTableColumn
cfprVnicFcLifType=_CfprVnicFcLifType_Object((1,3,6,1,4,1,9,9,826,1,83,18,1,9),_CfprVnicFcLifType_Type())
cfprVnicFcLifType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicFcLifType.setStatus(_A)
_CfprVnicFcLifVnicDn_Type=SnmpAdminString
_CfprVnicFcLifVnicDn_Object=MibTableColumn
cfprVnicFcLifVnicDn=_CfprVnicFcLifVnicDn_Object((1,3,6,1,4,1,9,9,826,1,83,18,1,10),_CfprVnicFcLifVnicDn_Type())
cfprVnicFcLifVnicDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicFcLifVnicDn.setStatus(_A)
_CfprVnicFcNodeTable_Object=MibTable
cfprVnicFcNodeTable=_CfprVnicFcNodeTable_Object((1,3,6,1,4,1,9,9,826,1,83,19))
if mibBuilder.loadTexts:cfprVnicFcNodeTable.setStatus(_A)
_CfprVnicFcNodeEntry_Object=MibTableRow
cfprVnicFcNodeEntry=_CfprVnicFcNodeEntry_Object((1,3,6,1,4,1,9,9,826,1,83,19,1))
cfprVnicFcNodeEntry.setIndexNames((0,_C,_W))
if mibBuilder.loadTexts:cfprVnicFcNodeEntry.setStatus(_A)
_CfprVnicFcNodeInstanceId_Type=CfprManagedObjectId
_CfprVnicFcNodeInstanceId_Object=MibTableColumn
cfprVnicFcNodeInstanceId=_CfprVnicFcNodeInstanceId_Object((1,3,6,1,4,1,9,9,826,1,83,19,1,1),_CfprVnicFcNodeInstanceId_Type())
cfprVnicFcNodeInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprVnicFcNodeInstanceId.setStatus(_A)
_CfprVnicFcNodeDn_Type=CfprManagedObjectDn
_CfprVnicFcNodeDn_Object=MibTableColumn
cfprVnicFcNodeDn=_CfprVnicFcNodeDn_Object((1,3,6,1,4,1,9,9,826,1,83,19,1,2),_CfprVnicFcNodeDn_Type())
cfprVnicFcNodeDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicFcNodeDn.setStatus(_A)
_CfprVnicFcNodeRn_Type=SnmpAdminString
_CfprVnicFcNodeRn_Object=MibTableColumn
cfprVnicFcNodeRn=_CfprVnicFcNodeRn_Object((1,3,6,1,4,1,9,9,826,1,83,19,1,3),_CfprVnicFcNodeRn_Type())
cfprVnicFcNodeRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicFcNodeRn.setStatus(_A)
_CfprVnicFcNodeAddrData_Type=Unsigned64
_CfprVnicFcNodeAddrData_Object=MibTableColumn
cfprVnicFcNodeAddrData=_CfprVnicFcNodeAddrData_Object((1,3,6,1,4,1,9,9,826,1,83,19,1,4),_CfprVnicFcNodeAddrData_Type())
cfprVnicFcNodeAddrData.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicFcNodeAddrData.setStatus(_A)
_CfprVnicFcNodeFltAggr_Type=Unsigned64
_CfprVnicFcNodeFltAggr_Object=MibTableColumn
cfprVnicFcNodeFltAggr=_CfprVnicFcNodeFltAggr_Object((1,3,6,1,4,1,9,9,826,1,83,19,1,5),_CfprVnicFcNodeFltAggr_Type())
cfprVnicFcNodeFltAggr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicFcNodeFltAggr.setStatus(_A)
_CfprVnicFcNodeIdentPoolName_Type=SnmpAdminString
_CfprVnicFcNodeIdentPoolName_Object=MibTableColumn
cfprVnicFcNodeIdentPoolName=_CfprVnicFcNodeIdentPoolName_Object((1,3,6,1,4,1,9,9,826,1,83,19,1,6),_CfprVnicFcNodeIdentPoolName_Type())
cfprVnicFcNodeIdentPoolName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicFcNodeIdentPoolName.setStatus(_A)
_CfprVnicFcNodeMaxDerivableWWPN_Type=Gauge32
_CfprVnicFcNodeMaxDerivableWWPN_Object=MibTableColumn
cfprVnicFcNodeMaxDerivableWWPN=_CfprVnicFcNodeMaxDerivableWWPN_Object((1,3,6,1,4,1,9,9,826,1,83,19,1,7),_CfprVnicFcNodeMaxDerivableWWPN_Type())
cfprVnicFcNodeMaxDerivableWWPN.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicFcNodeMaxDerivableWWPN.setStatus(_A)
_CfprVnicFcNodeOperIdentPoolName_Type=SnmpAdminString
_CfprVnicFcNodeOperIdentPoolName_Object=MibTableColumn
cfprVnicFcNodeOperIdentPoolName=_CfprVnicFcNodeOperIdentPoolName_Object((1,3,6,1,4,1,9,9,826,1,83,19,1,8),_CfprVnicFcNodeOperIdentPoolName_Type())
cfprVnicFcNodeOperIdentPoolName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicFcNodeOperIdentPoolName.setStatus(_A)
_CfprVnicFcNodeOwner_Type=CfprVnicFcNodeOwner
_CfprVnicFcNodeOwner_Object=MibTableColumn
cfprVnicFcNodeOwner=_CfprVnicFcNodeOwner_Object((1,3,6,1,4,1,9,9,826,1,83,19,1,9),_CfprVnicFcNodeOwner_Type())
cfprVnicFcNodeOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicFcNodeOwner.setStatus(_A)
_CfprVnicFcOEIfTable_Object=MibTable
cfprVnicFcOEIfTable=_CfprVnicFcOEIfTable_Object((1,3,6,1,4,1,9,9,826,1,83,20))
if mibBuilder.loadTexts:cfprVnicFcOEIfTable.setStatus(_A)
_CfprVnicFcOEIfEntry_Object=MibTableRow
cfprVnicFcOEIfEntry=_CfprVnicFcOEIfEntry_Object((1,3,6,1,4,1,9,9,826,1,83,20,1))
cfprVnicFcOEIfEntry.setIndexNames((0,_C,_X))
if mibBuilder.loadTexts:cfprVnicFcOEIfEntry.setStatus(_A)
_CfprVnicFcOEIfInstanceId_Type=CfprManagedObjectId
_CfprVnicFcOEIfInstanceId_Object=MibTableColumn
cfprVnicFcOEIfInstanceId=_CfprVnicFcOEIfInstanceId_Object((1,3,6,1,4,1,9,9,826,1,83,20,1,1),_CfprVnicFcOEIfInstanceId_Type())
cfprVnicFcOEIfInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprVnicFcOEIfInstanceId.setStatus(_A)
_CfprVnicFcOEIfDn_Type=CfprManagedObjectDn
_CfprVnicFcOEIfDn_Object=MibTableColumn
cfprVnicFcOEIfDn=_CfprVnicFcOEIfDn_Object((1,3,6,1,4,1,9,9,826,1,83,20,1,2),_CfprVnicFcOEIfDn_Type())
cfprVnicFcOEIfDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicFcOEIfDn.setStatus(_A)
_CfprVnicFcOEIfRn_Type=SnmpAdminString
_CfprVnicFcOEIfRn_Object=MibTableColumn
cfprVnicFcOEIfRn=_CfprVnicFcOEIfRn_Object((1,3,6,1,4,1,9,9,826,1,83,20,1,3),_CfprVnicFcOEIfRn_Type())
cfprVnicFcOEIfRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicFcOEIfRn.setStatus(_A)
_CfprVnicFcOEIfConfigQualifier_Type=CfprVnicConfigIssues
_CfprVnicFcOEIfConfigQualifier_Object=MibTableColumn
cfprVnicFcOEIfConfigQualifier=_CfprVnicFcOEIfConfigQualifier_Object((1,3,6,1,4,1,9,9,826,1,83,20,1,4),_CfprVnicFcOEIfConfigQualifier_Type())
cfprVnicFcOEIfConfigQualifier.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicFcOEIfConfigQualifier.setStatus(_A)
_CfprVnicFcOEIfInitiator_Type=Unsigned64
_CfprVnicFcOEIfInitiator_Object=MibTableColumn
cfprVnicFcOEIfInitiator=_CfprVnicFcOEIfInitiator_Object((1,3,6,1,4,1,9,9,826,1,83,20,1,5),_CfprVnicFcOEIfInitiator_Type())
cfprVnicFcOEIfInitiator.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicFcOEIfInitiator.setStatus(_A)
_CfprVnicFcOEIfName_Type=SnmpAdminString
_CfprVnicFcOEIfName_Object=MibTableColumn
cfprVnicFcOEIfName=_CfprVnicFcOEIfName_Object((1,3,6,1,4,1,9,9,826,1,83,20,1,6),_CfprVnicFcOEIfName_Type())
cfprVnicFcOEIfName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicFcOEIfName.setStatus(_A)
_CfprVnicFcOEIfOperState_Type=CfprVnicIfOperState
_CfprVnicFcOEIfOperState_Object=MibTableColumn
cfprVnicFcOEIfOperState=_CfprVnicFcOEIfOperState_Object((1,3,6,1,4,1,9,9,826,1,83,20,1,7),_CfprVnicFcOEIfOperState_Type())
cfprVnicFcOEIfOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicFcOEIfOperState.setStatus(_A)
_CfprVnicFcOEIfOperVnetDn_Type=SnmpAdminString
_CfprVnicFcOEIfOperVnetDn_Object=MibTableColumn
cfprVnicFcOEIfOperVnetDn=_CfprVnicFcOEIfOperVnetDn_Object((1,3,6,1,4,1,9,9,826,1,83,20,1,8),_CfprVnicFcOEIfOperVnetDn_Type())
cfprVnicFcOEIfOperVnetDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicFcOEIfOperVnetDn.setStatus(_A)
_CfprVnicFcOEIfOperVnetName_Type=SnmpAdminString
_CfprVnicFcOEIfOperVnetName_Object=MibTableColumn
cfprVnicFcOEIfOperVnetName=_CfprVnicFcOEIfOperVnetName_Object((1,3,6,1,4,1,9,9,826,1,83,20,1,9),_CfprVnicFcOEIfOperVnetName_Type())
cfprVnicFcOEIfOperVnetName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicFcOEIfOperVnetName.setStatus(_A)
_CfprVnicFcOEIfOwner_Type=CfprVnicConnectionOwner
_CfprVnicFcOEIfOwner_Object=MibTableColumn
cfprVnicFcOEIfOwner=_CfprVnicFcOEIfOwner_Object((1,3,6,1,4,1,9,9,826,1,83,20,1,10),_CfprVnicFcOEIfOwner_Type())
cfprVnicFcOEIfOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicFcOEIfOwner.setStatus(_A)
_CfprVnicFcOEIfPubNwId_Type=Gauge32
_CfprVnicFcOEIfPubNwId_Object=MibTableColumn
cfprVnicFcOEIfPubNwId=_CfprVnicFcOEIfPubNwId_Object((1,3,6,1,4,1,9,9,826,1,83,20,1,11),_CfprVnicFcOEIfPubNwId_Type())
cfprVnicFcOEIfPubNwId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicFcOEIfPubNwId.setStatus(_A)
_CfprVnicFcOEIfSharing_Type=CfprFabricVlanSharingType
_CfprVnicFcOEIfSharing_Object=MibTableColumn
cfprVnicFcOEIfSharing=_CfprVnicFcOEIfSharing_Object((1,3,6,1,4,1,9,9,826,1,83,20,1,12),_CfprVnicFcOEIfSharing_Type())
cfprVnicFcOEIfSharing.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicFcOEIfSharing.setStatus(_A)
_CfprVnicFcOEIfSwitchId_Type=CfprVnicL2IfSwitchId
_CfprVnicFcOEIfSwitchId_Object=MibTableColumn
cfprVnicFcOEIfSwitchId=_CfprVnicFcOEIfSwitchId_Object((1,3,6,1,4,1,9,9,826,1,83,20,1,13),_CfprVnicFcOEIfSwitchId_Type())
cfprVnicFcOEIfSwitchId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicFcOEIfSwitchId.setStatus(_A)
_CfprVnicFcOEIfType_Type=CfprVnicAFcIfType
_CfprVnicFcOEIfType_Object=MibTableColumn
cfprVnicFcOEIfType=_CfprVnicFcOEIfType_Object((1,3,6,1,4,1,9,9,826,1,83,20,1,14),_CfprVnicFcOEIfType_Type())
cfprVnicFcOEIfType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicFcOEIfType.setStatus(_A)
_CfprVnicFcOEIfVnet_Type=Gauge32
_CfprVnicFcOEIfVnet_Object=MibTableColumn
cfprVnicFcOEIfVnet=_CfprVnicFcOEIfVnet_Object((1,3,6,1,4,1,9,9,826,1,83,20,1,15),_CfprVnicFcOEIfVnet_Type())
cfprVnicFcOEIfVnet.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicFcOEIfVnet.setStatus(_A)
_CfprVnicIPv4DhcpTable_Object=MibTable
cfprVnicIPv4DhcpTable=_CfprVnicIPv4DhcpTable_Object((1,3,6,1,4,1,9,9,826,1,83,21))
if mibBuilder.loadTexts:cfprVnicIPv4DhcpTable.setStatus(_A)
_CfprVnicIPv4DhcpEntry_Object=MibTableRow
cfprVnicIPv4DhcpEntry=_CfprVnicIPv4DhcpEntry_Object((1,3,6,1,4,1,9,9,826,1,83,21,1))
cfprVnicIPv4DhcpEntry.setIndexNames((0,_C,_Y))
if mibBuilder.loadTexts:cfprVnicIPv4DhcpEntry.setStatus(_A)
_CfprVnicIPv4DhcpInstanceId_Type=CfprManagedObjectId
_CfprVnicIPv4DhcpInstanceId_Object=MibTableColumn
cfprVnicIPv4DhcpInstanceId=_CfprVnicIPv4DhcpInstanceId_Object((1,3,6,1,4,1,9,9,826,1,83,21,1,1),_CfprVnicIPv4DhcpInstanceId_Type())
cfprVnicIPv4DhcpInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprVnicIPv4DhcpInstanceId.setStatus(_A)
_CfprVnicIPv4DhcpDn_Type=CfprManagedObjectDn
_CfprVnicIPv4DhcpDn_Object=MibTableColumn
cfprVnicIPv4DhcpDn=_CfprVnicIPv4DhcpDn_Object((1,3,6,1,4,1,9,9,826,1,83,21,1,2),_CfprVnicIPv4DhcpDn_Type())
cfprVnicIPv4DhcpDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIPv4DhcpDn.setStatus(_A)
_CfprVnicIPv4DhcpRn_Type=SnmpAdminString
_CfprVnicIPv4DhcpRn_Object=MibTableColumn
cfprVnicIPv4DhcpRn=_CfprVnicIPv4DhcpRn_Object((1,3,6,1,4,1,9,9,826,1,83,21,1,3),_CfprVnicIPv4DhcpRn_Type())
cfprVnicIPv4DhcpRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIPv4DhcpRn.setStatus(_A)
_CfprVnicIPv4DhcpAddr_Type=InetAddressIPv4
_CfprVnicIPv4DhcpAddr_Object=MibTableColumn
cfprVnicIPv4DhcpAddr=_CfprVnicIPv4DhcpAddr_Object((1,3,6,1,4,1,9,9,826,1,83,21,1,4),_CfprVnicIPv4DhcpAddr_Type())
cfprVnicIPv4DhcpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIPv4DhcpAddr.setStatus(_A)
_CfprVnicIPv4DhcpDefGw_Type=InetAddressIPv4
_CfprVnicIPv4DhcpDefGw_Object=MibTableColumn
cfprVnicIPv4DhcpDefGw=_CfprVnicIPv4DhcpDefGw_Object((1,3,6,1,4,1,9,9,826,1,83,21,1,5),_CfprVnicIPv4DhcpDefGw_Type())
cfprVnicIPv4DhcpDefGw.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIPv4DhcpDefGw.setStatus(_A)
_CfprVnicIPv4DhcpSubnet_Type=InetAddressIPv4
_CfprVnicIPv4DhcpSubnet_Object=MibTableColumn
cfprVnicIPv4DhcpSubnet=_CfprVnicIPv4DhcpSubnet_Object((1,3,6,1,4,1,9,9,826,1,83,21,1,6),_CfprVnicIPv4DhcpSubnet_Type())
cfprVnicIPv4DhcpSubnet.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIPv4DhcpSubnet.setStatus(_A)
_CfprVnicIPv4DnsTable_Object=MibTable
cfprVnicIPv4DnsTable=_CfprVnicIPv4DnsTable_Object((1,3,6,1,4,1,9,9,826,1,83,22))
if mibBuilder.loadTexts:cfprVnicIPv4DnsTable.setStatus(_A)
_CfprVnicIPv4DnsEntry_Object=MibTableRow
cfprVnicIPv4DnsEntry=_CfprVnicIPv4DnsEntry_Object((1,3,6,1,4,1,9,9,826,1,83,22,1))
cfprVnicIPv4DnsEntry.setIndexNames((0,_C,_Z))
if mibBuilder.loadTexts:cfprVnicIPv4DnsEntry.setStatus(_A)
_CfprVnicIPv4DnsInstanceId_Type=CfprManagedObjectId
_CfprVnicIPv4DnsInstanceId_Object=MibTableColumn
cfprVnicIPv4DnsInstanceId=_CfprVnicIPv4DnsInstanceId_Object((1,3,6,1,4,1,9,9,826,1,83,22,1,1),_CfprVnicIPv4DnsInstanceId_Type())
cfprVnicIPv4DnsInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprVnicIPv4DnsInstanceId.setStatus(_A)
_CfprVnicIPv4DnsDn_Type=CfprManagedObjectDn
_CfprVnicIPv4DnsDn_Object=MibTableColumn
cfprVnicIPv4DnsDn=_CfprVnicIPv4DnsDn_Object((1,3,6,1,4,1,9,9,826,1,83,22,1,2),_CfprVnicIPv4DnsDn_Type())
cfprVnicIPv4DnsDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIPv4DnsDn.setStatus(_A)
_CfprVnicIPv4DnsRn_Type=SnmpAdminString
_CfprVnicIPv4DnsRn_Object=MibTableColumn
cfprVnicIPv4DnsRn=_CfprVnicIPv4DnsRn_Object((1,3,6,1,4,1,9,9,826,1,83,22,1,3),_CfprVnicIPv4DnsRn_Type())
cfprVnicIPv4DnsRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIPv4DnsRn.setStatus(_A)
_CfprVnicIPv4DnsAddr_Type=InetAddressIPv4
_CfprVnicIPv4DnsAddr_Object=MibTableColumn
cfprVnicIPv4DnsAddr=_CfprVnicIPv4DnsAddr_Object((1,3,6,1,4,1,9,9,826,1,83,22,1,4),_CfprVnicIPv4DnsAddr_Type())
cfprVnicIPv4DnsAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIPv4DnsAddr.setStatus(_A)
_CfprVnicIPv4DnsDefGw_Type=InetAddressIPv4
_CfprVnicIPv4DnsDefGw_Object=MibTableColumn
cfprVnicIPv4DnsDefGw=_CfprVnicIPv4DnsDefGw_Object((1,3,6,1,4,1,9,9,826,1,83,22,1,5),_CfprVnicIPv4DnsDefGw_Type())
cfprVnicIPv4DnsDefGw.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIPv4DnsDefGw.setStatus(_A)
_CfprVnicIPv4DnsPref_Type=CfprVnicIPv4DnsPref
_CfprVnicIPv4DnsPref_Object=MibTableColumn
cfprVnicIPv4DnsPref=_CfprVnicIPv4DnsPref_Object((1,3,6,1,4,1,9,9,826,1,83,22,1,6),_CfprVnicIPv4DnsPref_Type())
cfprVnicIPv4DnsPref.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIPv4DnsPref.setStatus(_A)
_CfprVnicIPv4DnsSubnet_Type=InetAddressIPv4
_CfprVnicIPv4DnsSubnet_Object=MibTableColumn
cfprVnicIPv4DnsSubnet=_CfprVnicIPv4DnsSubnet_Object((1,3,6,1,4,1,9,9,826,1,83,22,1,7),_CfprVnicIPv4DnsSubnet_Type())
cfprVnicIPv4DnsSubnet.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIPv4DnsSubnet.setStatus(_A)
_CfprVnicIPv4IfTable_Object=MibTable
cfprVnicIPv4IfTable=_CfprVnicIPv4IfTable_Object((1,3,6,1,4,1,9,9,826,1,83,23))
if mibBuilder.loadTexts:cfprVnicIPv4IfTable.setStatus(_A)
_CfprVnicIPv4IfEntry_Object=MibTableRow
cfprVnicIPv4IfEntry=_CfprVnicIPv4IfEntry_Object((1,3,6,1,4,1,9,9,826,1,83,23,1))
cfprVnicIPv4IfEntry.setIndexNames((0,_C,_a))
if mibBuilder.loadTexts:cfprVnicIPv4IfEntry.setStatus(_A)
_CfprVnicIPv4IfInstanceId_Type=CfprManagedObjectId
_CfprVnicIPv4IfInstanceId_Object=MibTableColumn
cfprVnicIPv4IfInstanceId=_CfprVnicIPv4IfInstanceId_Object((1,3,6,1,4,1,9,9,826,1,83,23,1,1),_CfprVnicIPv4IfInstanceId_Type())
cfprVnicIPv4IfInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprVnicIPv4IfInstanceId.setStatus(_A)
_CfprVnicIPv4IfDn_Type=CfprManagedObjectDn
_CfprVnicIPv4IfDn_Object=MibTableColumn
cfprVnicIPv4IfDn=_CfprVnicIPv4IfDn_Object((1,3,6,1,4,1,9,9,826,1,83,23,1,2),_CfprVnicIPv4IfDn_Type())
cfprVnicIPv4IfDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIPv4IfDn.setStatus(_A)
_CfprVnicIPv4IfRn_Type=SnmpAdminString
_CfprVnicIPv4IfRn_Object=MibTableColumn
cfprVnicIPv4IfRn=_CfprVnicIPv4IfRn_Object((1,3,6,1,4,1,9,9,826,1,83,23,1,3),_CfprVnicIPv4IfRn_Type())
cfprVnicIPv4IfRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIPv4IfRn.setStatus(_A)
_CfprVnicIPv4IfAddr_Type=InetAddressIPv4
_CfprVnicIPv4IfAddr_Object=MibTableColumn
cfprVnicIPv4IfAddr=_CfprVnicIPv4IfAddr_Object((1,3,6,1,4,1,9,9,826,1,83,23,1,4),_CfprVnicIPv4IfAddr_Type())
cfprVnicIPv4IfAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIPv4IfAddr.setStatus(_A)
_CfprVnicIPv4IfConfigQualifier_Type=CfprVnicConfigIssues
_CfprVnicIPv4IfConfigQualifier_Object=MibTableColumn
cfprVnicIPv4IfConfigQualifier=_CfprVnicIPv4IfConfigQualifier_Object((1,3,6,1,4,1,9,9,826,1,83,23,1,5),_CfprVnicIPv4IfConfigQualifier_Type())
cfprVnicIPv4IfConfigQualifier.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIPv4IfConfigQualifier.setStatus(_A)
_CfprVnicIPv4IfName_Type=SnmpAdminString
_CfprVnicIPv4IfName_Object=MibTableColumn
cfprVnicIPv4IfName=_CfprVnicIPv4IfName_Object((1,3,6,1,4,1,9,9,826,1,83,23,1,6),_CfprVnicIPv4IfName_Type())
cfprVnicIPv4IfName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIPv4IfName.setStatus(_A)
_CfprVnicIPv4IfOperState_Type=CfprVnicIfOperState
_CfprVnicIPv4IfOperState_Object=MibTableColumn
cfprVnicIPv4IfOperState=_CfprVnicIPv4IfOperState_Object((1,3,6,1,4,1,9,9,826,1,83,23,1,7),_CfprVnicIPv4IfOperState_Type())
cfprVnicIPv4IfOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIPv4IfOperState.setStatus(_A)
_CfprVnicIPv4IfOperVnetDn_Type=SnmpAdminString
_CfprVnicIPv4IfOperVnetDn_Object=MibTableColumn
cfprVnicIPv4IfOperVnetDn=_CfprVnicIPv4IfOperVnetDn_Object((1,3,6,1,4,1,9,9,826,1,83,23,1,8),_CfprVnicIPv4IfOperVnetDn_Type())
cfprVnicIPv4IfOperVnetDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIPv4IfOperVnetDn.setStatus(_A)
_CfprVnicIPv4IfOperVnetName_Type=SnmpAdminString
_CfprVnicIPv4IfOperVnetName_Object=MibTableColumn
cfprVnicIPv4IfOperVnetName=_CfprVnicIPv4IfOperVnetName_Object((1,3,6,1,4,1,9,9,826,1,83,23,1,9),_CfprVnicIPv4IfOperVnetName_Type())
cfprVnicIPv4IfOperVnetName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIPv4IfOperVnetName.setStatus(_A)
_CfprVnicIPv4IfOwner_Type=CfprVnicConnectionOwner
_CfprVnicIPv4IfOwner_Object=MibTableColumn
cfprVnicIPv4IfOwner=_CfprVnicIPv4IfOwner_Object((1,3,6,1,4,1,9,9,826,1,83,23,1,10),_CfprVnicIPv4IfOwner_Type())
cfprVnicIPv4IfOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIPv4IfOwner.setStatus(_A)
_CfprVnicIPv4IfPubNwId_Type=Gauge32
_CfprVnicIPv4IfPubNwId_Object=MibTableColumn
cfprVnicIPv4IfPubNwId=_CfprVnicIPv4IfPubNwId_Object((1,3,6,1,4,1,9,9,826,1,83,23,1,11),_CfprVnicIPv4IfPubNwId_Type())
cfprVnicIPv4IfPubNwId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIPv4IfPubNwId.setStatus(_A)
_CfprVnicIPv4IfSharing_Type=CfprFabricVlanSharingType
_CfprVnicIPv4IfSharing_Object=MibTableColumn
cfprVnicIPv4IfSharing=_CfprVnicIPv4IfSharing_Object((1,3,6,1,4,1,9,9,826,1,83,23,1,12),_CfprVnicIPv4IfSharing_Type())
cfprVnicIPv4IfSharing.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIPv4IfSharing.setStatus(_A)
_CfprVnicIPv4IfSwitchId_Type=CfprNetworkSwitchId
_CfprVnicIPv4IfSwitchId_Object=MibTableColumn
cfprVnicIPv4IfSwitchId=_CfprVnicIPv4IfSwitchId_Object((1,3,6,1,4,1,9,9,826,1,83,23,1,13),_CfprVnicIPv4IfSwitchId_Type())
cfprVnicIPv4IfSwitchId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIPv4IfSwitchId.setStatus(_A)
_CfprVnicIPv4IfType_Type=CfprVnicConnectionType
_CfprVnicIPv4IfType_Object=MibTableColumn
cfprVnicIPv4IfType=_CfprVnicIPv4IfType_Object((1,3,6,1,4,1,9,9,826,1,83,23,1,14),_CfprVnicIPv4IfType_Type())
cfprVnicIPv4IfType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIPv4IfType.setStatus(_A)
_CfprVnicIPv4IfVnet_Type=Gauge32
_CfprVnicIPv4IfVnet_Object=MibTableColumn
cfprVnicIPv4IfVnet=_CfprVnicIPv4IfVnet_Object((1,3,6,1,4,1,9,9,826,1,83,23,1,15),_CfprVnicIPv4IfVnet_Type())
cfprVnicIPv4IfVnet.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIPv4IfVnet.setStatus(_A)
_CfprVnicIPv4IscsiAddrTable_Object=MibTable
cfprVnicIPv4IscsiAddrTable=_CfprVnicIPv4IscsiAddrTable_Object((1,3,6,1,4,1,9,9,826,1,83,24))
if mibBuilder.loadTexts:cfprVnicIPv4IscsiAddrTable.setStatus(_A)
_CfprVnicIPv4IscsiAddrEntry_Object=MibTableRow
cfprVnicIPv4IscsiAddrEntry=_CfprVnicIPv4IscsiAddrEntry_Object((1,3,6,1,4,1,9,9,826,1,83,24,1))
cfprVnicIPv4IscsiAddrEntry.setIndexNames((0,_C,_b))
if mibBuilder.loadTexts:cfprVnicIPv4IscsiAddrEntry.setStatus(_A)
_CfprVnicIPv4IscsiAddrInstanceId_Type=CfprManagedObjectId
_CfprVnicIPv4IscsiAddrInstanceId_Object=MibTableColumn
cfprVnicIPv4IscsiAddrInstanceId=_CfprVnicIPv4IscsiAddrInstanceId_Object((1,3,6,1,4,1,9,9,826,1,83,24,1,1),_CfprVnicIPv4IscsiAddrInstanceId_Type())
cfprVnicIPv4IscsiAddrInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprVnicIPv4IscsiAddrInstanceId.setStatus(_A)
_CfprVnicIPv4IscsiAddrDn_Type=CfprManagedObjectDn
_CfprVnicIPv4IscsiAddrDn_Object=MibTableColumn
cfprVnicIPv4IscsiAddrDn=_CfprVnicIPv4IscsiAddrDn_Object((1,3,6,1,4,1,9,9,826,1,83,24,1,2),_CfprVnicIPv4IscsiAddrDn_Type())
cfprVnicIPv4IscsiAddrDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIPv4IscsiAddrDn.setStatus(_A)
_CfprVnicIPv4IscsiAddrRn_Type=SnmpAdminString
_CfprVnicIPv4IscsiAddrRn_Object=MibTableColumn
cfprVnicIPv4IscsiAddrRn=_CfprVnicIPv4IscsiAddrRn_Object((1,3,6,1,4,1,9,9,826,1,83,24,1,3),_CfprVnicIPv4IscsiAddrRn_Type())
cfprVnicIPv4IscsiAddrRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIPv4IscsiAddrRn.setStatus(_A)
_CfprVnicIPv4IscsiAddrAddr_Type=InetAddressIPv4
_CfprVnicIPv4IscsiAddrAddr_Object=MibTableColumn
cfprVnicIPv4IscsiAddrAddr=_CfprVnicIPv4IscsiAddrAddr_Object((1,3,6,1,4,1,9,9,826,1,83,24,1,4),_CfprVnicIPv4IscsiAddrAddr_Type())
cfprVnicIPv4IscsiAddrAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIPv4IscsiAddrAddr.setStatus(_A)
_CfprVnicIPv4IscsiAddrDefGw_Type=InetAddressIPv4
_CfprVnicIPv4IscsiAddrDefGw_Object=MibTableColumn
cfprVnicIPv4IscsiAddrDefGw=_CfprVnicIPv4IscsiAddrDefGw_Object((1,3,6,1,4,1,9,9,826,1,83,24,1,5),_CfprVnicIPv4IscsiAddrDefGw_Type())
cfprVnicIPv4IscsiAddrDefGw.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIPv4IscsiAddrDefGw.setStatus(_A)
_CfprVnicIPv4IscsiAddrPrimDns_Type=InetAddressIPv4
_CfprVnicIPv4IscsiAddrPrimDns_Object=MibTableColumn
cfprVnicIPv4IscsiAddrPrimDns=_CfprVnicIPv4IscsiAddrPrimDns_Object((1,3,6,1,4,1,9,9,826,1,83,24,1,6),_CfprVnicIPv4IscsiAddrPrimDns_Type())
cfprVnicIPv4IscsiAddrPrimDns.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIPv4IscsiAddrPrimDns.setStatus(_A)
_CfprVnicIPv4IscsiAddrSecDns_Type=InetAddressIPv4
_CfprVnicIPv4IscsiAddrSecDns_Object=MibTableColumn
cfprVnicIPv4IscsiAddrSecDns=_CfprVnicIPv4IscsiAddrSecDns_Object((1,3,6,1,4,1,9,9,826,1,83,24,1,7),_CfprVnicIPv4IscsiAddrSecDns_Type())
cfprVnicIPv4IscsiAddrSecDns.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIPv4IscsiAddrSecDns.setStatus(_A)
_CfprVnicIPv4IscsiAddrSubnet_Type=InetAddressIPv4
_CfprVnicIPv4IscsiAddrSubnet_Object=MibTableColumn
cfprVnicIPv4IscsiAddrSubnet=_CfprVnicIPv4IscsiAddrSubnet_Object((1,3,6,1,4,1,9,9,826,1,83,24,1,8),_CfprVnicIPv4IscsiAddrSubnet_Type())
cfprVnicIPv4IscsiAddrSubnet.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIPv4IscsiAddrSubnet.setStatus(_A)
_CfprVnicIPv4PooledIscsiAddrTable_Object=MibTable
cfprVnicIPv4PooledIscsiAddrTable=_CfprVnicIPv4PooledIscsiAddrTable_Object((1,3,6,1,4,1,9,9,826,1,83,25))
if mibBuilder.loadTexts:cfprVnicIPv4PooledIscsiAddrTable.setStatus(_A)
_CfprVnicIPv4PooledIscsiAddrEntry_Object=MibTableRow
cfprVnicIPv4PooledIscsiAddrEntry=_CfprVnicIPv4PooledIscsiAddrEntry_Object((1,3,6,1,4,1,9,9,826,1,83,25,1))
cfprVnicIPv4PooledIscsiAddrEntry.setIndexNames((0,_C,_c))
if mibBuilder.loadTexts:cfprVnicIPv4PooledIscsiAddrEntry.setStatus(_A)
_CfprVnicIPv4PooledIscsiAddrInstanceId_Type=CfprManagedObjectId
_CfprVnicIPv4PooledIscsiAddrInstanceId_Object=MibTableColumn
cfprVnicIPv4PooledIscsiAddrInstanceId=_CfprVnicIPv4PooledIscsiAddrInstanceId_Object((1,3,6,1,4,1,9,9,826,1,83,25,1,1),_CfprVnicIPv4PooledIscsiAddrInstanceId_Type())
cfprVnicIPv4PooledIscsiAddrInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprVnicIPv4PooledIscsiAddrInstanceId.setStatus(_A)
_CfprVnicIPv4PooledIscsiAddrDn_Type=CfprManagedObjectDn
_CfprVnicIPv4PooledIscsiAddrDn_Object=MibTableColumn
cfprVnicIPv4PooledIscsiAddrDn=_CfprVnicIPv4PooledIscsiAddrDn_Object((1,3,6,1,4,1,9,9,826,1,83,25,1,2),_CfprVnicIPv4PooledIscsiAddrDn_Type())
cfprVnicIPv4PooledIscsiAddrDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIPv4PooledIscsiAddrDn.setStatus(_A)
_CfprVnicIPv4PooledIscsiAddrRn_Type=SnmpAdminString
_CfprVnicIPv4PooledIscsiAddrRn_Object=MibTableColumn
cfprVnicIPv4PooledIscsiAddrRn=_CfprVnicIPv4PooledIscsiAddrRn_Object((1,3,6,1,4,1,9,9,826,1,83,25,1,3),_CfprVnicIPv4PooledIscsiAddrRn_Type())
cfprVnicIPv4PooledIscsiAddrRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIPv4PooledIscsiAddrRn.setStatus(_A)
_CfprVnicIPv4PooledIscsiAddrAddr_Type=InetAddressIPv4
_CfprVnicIPv4PooledIscsiAddrAddr_Object=MibTableColumn
cfprVnicIPv4PooledIscsiAddrAddr=_CfprVnicIPv4PooledIscsiAddrAddr_Object((1,3,6,1,4,1,9,9,826,1,83,25,1,4),_CfprVnicIPv4PooledIscsiAddrAddr_Type())
cfprVnicIPv4PooledIscsiAddrAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIPv4PooledIscsiAddrAddr.setStatus(_A)
_CfprVnicIPv4PooledIscsiAddrDefGw_Type=InetAddressIPv4
_CfprVnicIPv4PooledIscsiAddrDefGw_Object=MibTableColumn
cfprVnicIPv4PooledIscsiAddrDefGw=_CfprVnicIPv4PooledIscsiAddrDefGw_Object((1,3,6,1,4,1,9,9,826,1,83,25,1,5),_CfprVnicIPv4PooledIscsiAddrDefGw_Type())
cfprVnicIPv4PooledIscsiAddrDefGw.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIPv4PooledIscsiAddrDefGw.setStatus(_A)
_CfprVnicIPv4PooledIscsiAddrIdentPoolName_Type=SnmpAdminString
_CfprVnicIPv4PooledIscsiAddrIdentPoolName_Object=MibTableColumn
cfprVnicIPv4PooledIscsiAddrIdentPoolName=_CfprVnicIPv4PooledIscsiAddrIdentPoolName_Object((1,3,6,1,4,1,9,9,826,1,83,25,1,6),_CfprVnicIPv4PooledIscsiAddrIdentPoolName_Type())
cfprVnicIPv4PooledIscsiAddrIdentPoolName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIPv4PooledIscsiAddrIdentPoolName.setStatus(_A)
_CfprVnicIPv4PooledIscsiAddrOperIdentPoolName_Type=SnmpAdminString
_CfprVnicIPv4PooledIscsiAddrOperIdentPoolName_Object=MibTableColumn
cfprVnicIPv4PooledIscsiAddrOperIdentPoolName=_CfprVnicIPv4PooledIscsiAddrOperIdentPoolName_Object((1,3,6,1,4,1,9,9,826,1,83,25,1,7),_CfprVnicIPv4PooledIscsiAddrOperIdentPoolName_Type())
cfprVnicIPv4PooledIscsiAddrOperIdentPoolName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIPv4PooledIscsiAddrOperIdentPoolName.setStatus(_A)
_CfprVnicIPv4PooledIscsiAddrPrimDns_Type=InetAddressIPv4
_CfprVnicIPv4PooledIscsiAddrPrimDns_Object=MibTableColumn
cfprVnicIPv4PooledIscsiAddrPrimDns=_CfprVnicIPv4PooledIscsiAddrPrimDns_Object((1,3,6,1,4,1,9,9,826,1,83,25,1,8),_CfprVnicIPv4PooledIscsiAddrPrimDns_Type())
cfprVnicIPv4PooledIscsiAddrPrimDns.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIPv4PooledIscsiAddrPrimDns.setStatus(_A)
_CfprVnicIPv4PooledIscsiAddrSecDns_Type=InetAddressIPv4
_CfprVnicIPv4PooledIscsiAddrSecDns_Object=MibTableColumn
cfprVnicIPv4PooledIscsiAddrSecDns=_CfprVnicIPv4PooledIscsiAddrSecDns_Object((1,3,6,1,4,1,9,9,826,1,83,25,1,9),_CfprVnicIPv4PooledIscsiAddrSecDns_Type())
cfprVnicIPv4PooledIscsiAddrSecDns.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIPv4PooledIscsiAddrSecDns.setStatus(_A)
_CfprVnicIPv4PooledIscsiAddrSubnet_Type=InetAddressIPv4
_CfprVnicIPv4PooledIscsiAddrSubnet_Object=MibTableColumn
cfprVnicIPv4PooledIscsiAddrSubnet=_CfprVnicIPv4PooledIscsiAddrSubnet_Object((1,3,6,1,4,1,9,9,826,1,83,25,1,10),_CfprVnicIPv4PooledIscsiAddrSubnet_Type())
cfprVnicIPv4PooledIscsiAddrSubnet.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIPv4PooledIscsiAddrSubnet.setStatus(_A)
_CfprVnicIPv4StaticRouteTable_Object=MibTable
cfprVnicIPv4StaticRouteTable=_CfprVnicIPv4StaticRouteTable_Object((1,3,6,1,4,1,9,9,826,1,83,26))
if mibBuilder.loadTexts:cfprVnicIPv4StaticRouteTable.setStatus(_A)
_CfprVnicIPv4StaticRouteEntry_Object=MibTableRow
cfprVnicIPv4StaticRouteEntry=_CfprVnicIPv4StaticRouteEntry_Object((1,3,6,1,4,1,9,9,826,1,83,26,1))
cfprVnicIPv4StaticRouteEntry.setIndexNames((0,_C,_d))
if mibBuilder.loadTexts:cfprVnicIPv4StaticRouteEntry.setStatus(_A)
_CfprVnicIPv4StaticRouteInstanceId_Type=CfprManagedObjectId
_CfprVnicIPv4StaticRouteInstanceId_Object=MibTableColumn
cfprVnicIPv4StaticRouteInstanceId=_CfprVnicIPv4StaticRouteInstanceId_Object((1,3,6,1,4,1,9,9,826,1,83,26,1,1),_CfprVnicIPv4StaticRouteInstanceId_Type())
cfprVnicIPv4StaticRouteInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprVnicIPv4StaticRouteInstanceId.setStatus(_A)
_CfprVnicIPv4StaticRouteDn_Type=CfprManagedObjectDn
_CfprVnicIPv4StaticRouteDn_Object=MibTableColumn
cfprVnicIPv4StaticRouteDn=_CfprVnicIPv4StaticRouteDn_Object((1,3,6,1,4,1,9,9,826,1,83,26,1,2),_CfprVnicIPv4StaticRouteDn_Type())
cfprVnicIPv4StaticRouteDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIPv4StaticRouteDn.setStatus(_A)
_CfprVnicIPv4StaticRouteRn_Type=SnmpAdminString
_CfprVnicIPv4StaticRouteRn_Object=MibTableColumn
cfprVnicIPv4StaticRouteRn=_CfprVnicIPv4StaticRouteRn_Object((1,3,6,1,4,1,9,9,826,1,83,26,1,3),_CfprVnicIPv4StaticRouteRn_Type())
cfprVnicIPv4StaticRouteRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIPv4StaticRouteRn.setStatus(_A)
_CfprVnicIPv4StaticRouteAddr_Type=InetAddressIPv4
_CfprVnicIPv4StaticRouteAddr_Object=MibTableColumn
cfprVnicIPv4StaticRouteAddr=_CfprVnicIPv4StaticRouteAddr_Object((1,3,6,1,4,1,9,9,826,1,83,26,1,4),_CfprVnicIPv4StaticRouteAddr_Type())
cfprVnicIPv4StaticRouteAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIPv4StaticRouteAddr.setStatus(_A)
_CfprVnicIPv4StaticRouteDefGw_Type=InetAddressIPv4
_CfprVnicIPv4StaticRouteDefGw_Object=MibTableColumn
cfprVnicIPv4StaticRouteDefGw=_CfprVnicIPv4StaticRouteDefGw_Object((1,3,6,1,4,1,9,9,826,1,83,26,1,5),_CfprVnicIPv4StaticRouteDefGw_Type())
cfprVnicIPv4StaticRouteDefGw.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIPv4StaticRouteDefGw.setStatus(_A)
_CfprVnicIPv4StaticRouteGwAddr_Type=InetAddressIPv4
_CfprVnicIPv4StaticRouteGwAddr_Object=MibTableColumn
cfprVnicIPv4StaticRouteGwAddr=_CfprVnicIPv4StaticRouteGwAddr_Object((1,3,6,1,4,1,9,9,826,1,83,26,1,6),_CfprVnicIPv4StaticRouteGwAddr_Type())
cfprVnicIPv4StaticRouteGwAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIPv4StaticRouteGwAddr.setStatus(_A)
_CfprVnicIPv4StaticRouteGwSubnet_Type=InetAddressIPv4
_CfprVnicIPv4StaticRouteGwSubnet_Object=MibTableColumn
cfprVnicIPv4StaticRouteGwSubnet=_CfprVnicIPv4StaticRouteGwSubnet_Object((1,3,6,1,4,1,9,9,826,1,83,26,1,7),_CfprVnicIPv4StaticRouteGwSubnet_Type())
cfprVnicIPv4StaticRouteGwSubnet.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIPv4StaticRouteGwSubnet.setStatus(_A)
_CfprVnicIPv4StaticRouteSubnet_Type=InetAddressIPv4
_CfprVnicIPv4StaticRouteSubnet_Object=MibTableColumn
cfprVnicIPv4StaticRouteSubnet=_CfprVnicIPv4StaticRouteSubnet_Object((1,3,6,1,4,1,9,9,826,1,83,26,1,8),_CfprVnicIPv4StaticRouteSubnet_Type())
cfprVnicIPv4StaticRouteSubnet.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIPv4StaticRouteSubnet.setStatus(_A)
_CfprVnicIScsiTable_Object=MibTable
cfprVnicIScsiTable=_CfprVnicIScsiTable_Object((1,3,6,1,4,1,9,9,826,1,83,27))
if mibBuilder.loadTexts:cfprVnicIScsiTable.setStatus(_A)
_CfprVnicIScsiEntry_Object=MibTableRow
cfprVnicIScsiEntry=_CfprVnicIScsiEntry_Object((1,3,6,1,4,1,9,9,826,1,83,27,1))
cfprVnicIScsiEntry.setIndexNames((0,_C,_e))
if mibBuilder.loadTexts:cfprVnicIScsiEntry.setStatus(_A)
_CfprVnicIScsiInstanceId_Type=CfprManagedObjectId
_CfprVnicIScsiInstanceId_Object=MibTableColumn
cfprVnicIScsiInstanceId=_CfprVnicIScsiInstanceId_Object((1,3,6,1,4,1,9,9,826,1,83,27,1,1),_CfprVnicIScsiInstanceId_Type())
cfprVnicIScsiInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprVnicIScsiInstanceId.setStatus(_A)
_CfprVnicIScsiDn_Type=CfprManagedObjectDn
_CfprVnicIScsiDn_Object=MibTableColumn
cfprVnicIScsiDn=_CfprVnicIScsiDn_Object((1,3,6,1,4,1,9,9,826,1,83,27,1,2),_CfprVnicIScsiDn_Type())
cfprVnicIScsiDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIScsiDn.setStatus(_A)
_CfprVnicIScsiRn_Type=SnmpAdminString
_CfprVnicIScsiRn_Object=MibTableColumn
cfprVnicIScsiRn=_CfprVnicIScsiRn_Object((1,3,6,1,4,1,9,9,826,1,83,27,1,3),_CfprVnicIScsiRn_Type())
cfprVnicIScsiRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIScsiRn.setStatus(_A)
_CfprVnicIScsiAdaptorProfileName_Type=SnmpAdminString
_CfprVnicIScsiAdaptorProfileName_Object=MibTableColumn
cfprVnicIScsiAdaptorProfileName=_CfprVnicIScsiAdaptorProfileName_Object((1,3,6,1,4,1,9,9,826,1,83,27,1,4),_CfprVnicIScsiAdaptorProfileName_Type())
cfprVnicIScsiAdaptorProfileName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIScsiAdaptorProfileName.setStatus(_A)
_CfprVnicIScsiAddr_Type=MacAddress
_CfprVnicIScsiAddr_Object=MibTableColumn
cfprVnicIScsiAddr=_CfprVnicIScsiAddr_Object((1,3,6,1,4,1,9,9,826,1,83,27,1,5),_CfprVnicIScsiAddr_Type())
cfprVnicIScsiAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIScsiAddr.setStatus(_A)
_CfprVnicIScsiAdminHostPort_Type=CfprFabricHostPortId
_CfprVnicIScsiAdminHostPort_Object=MibTableColumn
cfprVnicIScsiAdminHostPort=_CfprVnicIScsiAdminHostPort_Object((1,3,6,1,4,1,9,9,826,1,83,27,1,6),_CfprVnicIScsiAdminHostPort_Type())
cfprVnicIScsiAdminHostPort.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIScsiAdminHostPort.setStatus(_A)
_CfprVnicIScsiAdminVcon_Type=SnmpAdminString
_CfprVnicIScsiAdminVcon_Object=MibTableColumn
cfprVnicIScsiAdminVcon=_CfprVnicIScsiAdminVcon_Object((1,3,6,1,4,1,9,9,826,1,83,27,1,7),_CfprVnicIScsiAdminVcon_Type())
cfprVnicIScsiAdminVcon.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIScsiAdminVcon.setStatus(_A)
_CfprVnicIScsiAppRole_Type=CfprVnicAppRole
_CfprVnicIScsiAppRole_Object=MibTableColumn
cfprVnicIScsiAppRole=_CfprVnicIScsiAppRole_Object((1,3,6,1,4,1,9,9,826,1,83,27,1,8),_CfprVnicIScsiAppRole_Type())
cfprVnicIScsiAppRole.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIScsiAppRole.setStatus(_A)
_CfprVnicIScsiAuthProfileName_Type=SnmpAdminString
_CfprVnicIScsiAuthProfileName_Object=MibTableColumn
cfprVnicIScsiAuthProfileName=_CfprVnicIScsiAuthProfileName_Object((1,3,6,1,4,1,9,9,826,1,83,27,1,9),_CfprVnicIScsiAuthProfileName_Type())
cfprVnicIScsiAuthProfileName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIScsiAuthProfileName.setStatus(_A)
_CfprVnicIScsiBootDev_Type=CfprVnicVnicBootDev
_CfprVnicIScsiBootDev_Object=MibTableColumn
cfprVnicIScsiBootDev=_CfprVnicIScsiBootDev_Object((1,3,6,1,4,1,9,9,826,1,83,27,1,10),_CfprVnicIScsiBootDev_Type())
cfprVnicIScsiBootDev.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIScsiBootDev.setStatus(_A)
_CfprVnicIScsiConfigQualifier_Type=CfprVnicConfigIssues
_CfprVnicIScsiConfigQualifier_Object=MibTableColumn
cfprVnicIScsiConfigQualifier=_CfprVnicIScsiConfigQualifier_Object((1,3,6,1,4,1,9,9,826,1,83,27,1,11),_CfprVnicIScsiConfigQualifier_Type())
cfprVnicIScsiConfigQualifier.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIScsiConfigQualifier.setStatus(_A)
_CfprVnicIScsiConfigState_Type=CfprLsConfigState
_CfprVnicIScsiConfigState_Object=MibTableColumn
cfprVnicIScsiConfigState=_CfprVnicIScsiConfigState_Object((1,3,6,1,4,1,9,9,826,1,83,27,1,12),_CfprVnicIScsiConfigState_Type())
cfprVnicIScsiConfigState.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIScsiConfigState.setStatus(_A)
_CfprVnicIScsiEquipmentDn_Type=SnmpAdminString
_CfprVnicIScsiEquipmentDn_Object=MibTableColumn
cfprVnicIScsiEquipmentDn=_CfprVnicIScsiEquipmentDn_Object((1,3,6,1,4,1,9,9,826,1,83,27,1,13),_CfprVnicIScsiEquipmentDn_Type())
cfprVnicIScsiEquipmentDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIScsiEquipmentDn.setStatus(_A)
_CfprVnicIScsiEthEpDn_Type=SnmpAdminString
_CfprVnicIScsiEthEpDn_Object=MibTableColumn
cfprVnicIScsiEthEpDn=_CfprVnicIScsiEthEpDn_Object((1,3,6,1,4,1,9,9,826,1,83,27,1,14),_CfprVnicIScsiEthEpDn_Type())
cfprVnicIScsiEthEpDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIScsiEthEpDn.setStatus(_A)
_CfprVnicIScsiExtIPState_Type=CfprVnicExternalMgmtIPMode
_CfprVnicIScsiExtIPState_Object=MibTableColumn
cfprVnicIScsiExtIPState=_CfprVnicIScsiExtIPState_Object((1,3,6,1,4,1,9,9,826,1,83,27,1,15),_CfprVnicIScsiExtIPState_Type())
cfprVnicIScsiExtIPState.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIScsiExtIPState.setStatus(_A)
_CfprVnicIScsiFltAggr_Type=Unsigned64
_CfprVnicIScsiFltAggr_Object=MibTableColumn
cfprVnicIScsiFltAggr=_CfprVnicIScsiFltAggr_Object((1,3,6,1,4,1,9,9,826,1,83,27,1,16),_CfprVnicIScsiFltAggr_Type())
cfprVnicIScsiFltAggr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIScsiFltAggr.setStatus(_A)
_CfprVnicIScsiIdentPoolName_Type=SnmpAdminString
_CfprVnicIScsiIdentPoolName_Object=MibTableColumn
cfprVnicIScsiIdentPoolName=_CfprVnicIScsiIdentPoolName_Object((1,3,6,1,4,1,9,9,826,1,83,27,1,17),_CfprVnicIScsiIdentPoolName_Type())
cfprVnicIScsiIdentPoolName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIScsiIdentPoolName.setStatus(_A)
_CfprVnicIScsiInitNameSuffix_Type=SnmpAdminString
_CfprVnicIScsiInitNameSuffix_Object=MibTableColumn
cfprVnicIScsiInitNameSuffix=_CfprVnicIScsiInitNameSuffix_Object((1,3,6,1,4,1,9,9,826,1,83,27,1,18),_CfprVnicIScsiInitNameSuffix_Type())
cfprVnicIScsiInitNameSuffix.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIScsiInitNameSuffix.setStatus(_A)
_CfprVnicIScsiInitiatorName_Type=SnmpAdminString
_CfprVnicIScsiInitiatorName_Object=MibTableColumn
cfprVnicIScsiInitiatorName=_CfprVnicIScsiInitiatorName_Object((1,3,6,1,4,1,9,9,826,1,83,27,1,19),_CfprVnicIScsiInitiatorName_Type())
cfprVnicIScsiInitiatorName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIScsiInitiatorName.setStatus(_A)
_CfprVnicIScsiInstType_Type=CfprVnicInstantiation
_CfprVnicIScsiInstType_Object=MibTableColumn
cfprVnicIScsiInstType=_CfprVnicIScsiInstType_Object((1,3,6,1,4,1,9,9,826,1,83,27,1,20),_CfprVnicIScsiInstType_Type())
cfprVnicIScsiInstType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIScsiInstType.setStatus(_A)
_CfprVnicIScsiIqnIdentPoolName_Type=SnmpAdminString
_CfprVnicIScsiIqnIdentPoolName_Object=MibTableColumn
cfprVnicIScsiIqnIdentPoolName=_CfprVnicIScsiIqnIdentPoolName_Object((1,3,6,1,4,1,9,9,826,1,83,27,1,21),_CfprVnicIScsiIqnIdentPoolName_Type())
cfprVnicIScsiIqnIdentPoolName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIScsiIqnIdentPoolName.setStatus(_A)
_CfprVnicIScsiName_Type=SnmpAdminString
_CfprVnicIScsiName_Object=MibTableColumn
cfprVnicIScsiName=_CfprVnicIScsiName_Object((1,3,6,1,4,1,9,9,826,1,83,27,1,22),_CfprVnicIScsiName_Type())
cfprVnicIScsiName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIScsiName.setStatus(_A)
_CfprVnicIScsiNwTemplName_Type=SnmpAdminString
_CfprVnicIScsiNwTemplName_Object=MibTableColumn
cfprVnicIScsiNwTemplName=_CfprVnicIScsiNwTemplName_Object((1,3,6,1,4,1,9,9,826,1,83,27,1,23),_CfprVnicIScsiNwTemplName_Type())
cfprVnicIScsiNwTemplName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIScsiNwTemplName.setStatus(_A)
_CfprVnicIScsiOperAdaptorProfileName_Type=SnmpAdminString
_CfprVnicIScsiOperAdaptorProfileName_Object=MibTableColumn
cfprVnicIScsiOperAdaptorProfileName=_CfprVnicIScsiOperAdaptorProfileName_Object((1,3,6,1,4,1,9,9,826,1,83,27,1,24),_CfprVnicIScsiOperAdaptorProfileName_Type())
cfprVnicIScsiOperAdaptorProfileName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIScsiOperAdaptorProfileName.setStatus(_A)
_CfprVnicIScsiOperAuthProfileName_Type=SnmpAdminString
_CfprVnicIScsiOperAuthProfileName_Object=MibTableColumn
cfprVnicIScsiOperAuthProfileName=_CfprVnicIScsiOperAuthProfileName_Object((1,3,6,1,4,1,9,9,826,1,83,27,1,25),_CfprVnicIScsiOperAuthProfileName_Type())
cfprVnicIScsiOperAuthProfileName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIScsiOperAuthProfileName.setStatus(_A)
_CfprVnicIScsiOperHostPort_Type=CfprVnicVnicOperHostPort
_CfprVnicIScsiOperHostPort_Object=MibTableColumn
cfprVnicIScsiOperHostPort=_CfprVnicIScsiOperHostPort_Object((1,3,6,1,4,1,9,9,826,1,83,27,1,26),_CfprVnicIScsiOperHostPort_Type())
cfprVnicIScsiOperHostPort.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIScsiOperHostPort.setStatus(_A)
_CfprVnicIScsiOperIdentPoolName_Type=SnmpAdminString
_CfprVnicIScsiOperIdentPoolName_Object=MibTableColumn
cfprVnicIScsiOperIdentPoolName=_CfprVnicIScsiOperIdentPoolName_Object((1,3,6,1,4,1,9,9,826,1,83,27,1,27),_CfprVnicIScsiOperIdentPoolName_Type())
cfprVnicIScsiOperIdentPoolName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIScsiOperIdentPoolName.setStatus(_A)
_CfprVnicIScsiOperIqnIdentPoolName_Type=SnmpAdminString
_CfprVnicIScsiOperIqnIdentPoolName_Object=MibTableColumn
cfprVnicIScsiOperIqnIdentPoolName=_CfprVnicIScsiOperIqnIdentPoolName_Object((1,3,6,1,4,1,9,9,826,1,83,27,1,28),_CfprVnicIScsiOperIqnIdentPoolName_Type())
cfprVnicIScsiOperIqnIdentPoolName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIScsiOperIqnIdentPoolName.setStatus(_A)
_CfprVnicIScsiOperOrder_Type=Gauge32
_CfprVnicIScsiOperOrder_Object=MibTableColumn
cfprVnicIScsiOperOrder=_CfprVnicIScsiOperOrder_Object((1,3,6,1,4,1,9,9,826,1,83,27,1,29),_CfprVnicIScsiOperOrder_Type())
cfprVnicIScsiOperOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIScsiOperOrder.setStatus(_A)
_CfprVnicIScsiOperSpeed_Type=Gauge32
_CfprVnicIScsiOperSpeed_Object=MibTableColumn
cfprVnicIScsiOperSpeed=_CfprVnicIScsiOperSpeed_Object((1,3,6,1,4,1,9,9,826,1,83,27,1,30),_CfprVnicIScsiOperSpeed_Type())
cfprVnicIScsiOperSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIScsiOperSpeed.setStatus(_A)
_CfprVnicIScsiOperStatsPolicyName_Type=SnmpAdminString
_CfprVnicIScsiOperStatsPolicyName_Object=MibTableColumn
cfprVnicIScsiOperStatsPolicyName=_CfprVnicIScsiOperStatsPolicyName_Object((1,3,6,1,4,1,9,9,826,1,83,27,1,31),_CfprVnicIScsiOperStatsPolicyName_Type())
cfprVnicIScsiOperStatsPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIScsiOperStatsPolicyName.setStatus(_A)
_CfprVnicIScsiOperVcon_Type=SnmpAdminString
_CfprVnicIScsiOperVcon_Object=MibTableColumn
cfprVnicIScsiOperVcon=_CfprVnicIScsiOperVcon_Object((1,3,6,1,4,1,9,9,826,1,83,27,1,32),_CfprVnicIScsiOperVcon_Type())
cfprVnicIScsiOperVcon.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIScsiOperVcon.setStatus(_A)
_CfprVnicIScsiOrder_Type=Gauge32
_CfprVnicIScsiOrder_Object=MibTableColumn
cfprVnicIScsiOrder=_CfprVnicIScsiOrder_Object((1,3,6,1,4,1,9,9,826,1,83,27,1,33),_CfprVnicIScsiOrder_Type())
cfprVnicIScsiOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIScsiOrder.setStatus(_A)
_CfprVnicIScsiOwner_Type=CfprVnicConnectionOwner
_CfprVnicIScsiOwner_Object=MibTableColumn
cfprVnicIScsiOwner=_CfprVnicIScsiOwner_Object((1,3,6,1,4,1,9,9,826,1,83,27,1,34),_CfprVnicIScsiOwner_Type())
cfprVnicIScsiOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIScsiOwner.setStatus(_A)
_CfprVnicIScsiPinToGroupName_Type=SnmpAdminString
_CfprVnicIScsiPinToGroupName_Object=MibTableColumn
cfprVnicIScsiPinToGroupName=_CfprVnicIScsiPinToGroupName_Object((1,3,6,1,4,1,9,9,826,1,83,27,1,35),_CfprVnicIScsiPinToGroupName_Type())
cfprVnicIScsiPinToGroupName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIScsiPinToGroupName.setStatus(_A)
_CfprVnicIScsiQosPolicyName_Type=SnmpAdminString
_CfprVnicIScsiQosPolicyName_Object=MibTableColumn
cfprVnicIScsiQosPolicyName=_CfprVnicIScsiQosPolicyName_Object((1,3,6,1,4,1,9,9,826,1,83,27,1,36),_CfprVnicIScsiQosPolicyName_Type())
cfprVnicIScsiQosPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIScsiQosPolicyName.setStatus(_A)
_CfprVnicIScsiStatsPolicyName_Type=SnmpAdminString
_CfprVnicIScsiStatsPolicyName_Object=MibTableColumn
cfprVnicIScsiStatsPolicyName=_CfprVnicIScsiStatsPolicyName_Object((1,3,6,1,4,1,9,9,826,1,83,27,1,37),_CfprVnicIScsiStatsPolicyName_Type())
cfprVnicIScsiStatsPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIScsiStatsPolicyName.setStatus(_A)
_CfprVnicIScsiSwitchId_Type=CfprNetworkSwitchId
_CfprVnicIScsiSwitchId_Object=MibTableColumn
cfprVnicIScsiSwitchId=_CfprVnicIScsiSwitchId_Object((1,3,6,1,4,1,9,9,826,1,83,27,1,38),_CfprVnicIScsiSwitchId_Type())
cfprVnicIScsiSwitchId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIScsiSwitchId.setStatus(_A)
_CfprVnicIScsiType_Type=CfprVnicConnectionType
_CfprVnicIScsiType_Object=MibTableColumn
cfprVnicIScsiType=_CfprVnicIScsiType_Object((1,3,6,1,4,1,9,9,826,1,83,27,1,39),_CfprVnicIScsiType_Type())
cfprVnicIScsiType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIScsiType.setStatus(_A)
_CfprVnicIScsiVnicDefType_Type=CfprVnicIScsiIfDefType
_CfprVnicIScsiVnicDefType_Object=MibTableColumn
cfprVnicIScsiVnicDefType=_CfprVnicIScsiVnicDefType_Object((1,3,6,1,4,1,9,9,826,1,83,27,1,40),_CfprVnicIScsiVnicDefType_Type())
cfprVnicIScsiVnicDefType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIScsiVnicDefType.setStatus(_A)
_CfprVnicIScsiVnicName_Type=SnmpAdminString
_CfprVnicIScsiVnicName_Object=MibTableColumn
cfprVnicIScsiVnicName=_CfprVnicIScsiVnicName_Object((1,3,6,1,4,1,9,9,826,1,83,27,1,41),_CfprVnicIScsiVnicName_Type())
cfprVnicIScsiVnicName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIScsiVnicName.setStatus(_A)
_CfprVnicIScsiAutoTargetIfTable_Object=MibTable
cfprVnicIScsiAutoTargetIfTable=_CfprVnicIScsiAutoTargetIfTable_Object((1,3,6,1,4,1,9,9,826,1,83,28))
if mibBuilder.loadTexts:cfprVnicIScsiAutoTargetIfTable.setStatus(_A)
_CfprVnicIScsiAutoTargetIfEntry_Object=MibTableRow
cfprVnicIScsiAutoTargetIfEntry=_CfprVnicIScsiAutoTargetIfEntry_Object((1,3,6,1,4,1,9,9,826,1,83,28,1))
cfprVnicIScsiAutoTargetIfEntry.setIndexNames((0,_C,_f))
if mibBuilder.loadTexts:cfprVnicIScsiAutoTargetIfEntry.setStatus(_A)
_CfprVnicIScsiAutoTargetIfInstanceId_Type=CfprManagedObjectId
_CfprVnicIScsiAutoTargetIfInstanceId_Object=MibTableColumn
cfprVnicIScsiAutoTargetIfInstanceId=_CfprVnicIScsiAutoTargetIfInstanceId_Object((1,3,6,1,4,1,9,9,826,1,83,28,1,1),_CfprVnicIScsiAutoTargetIfInstanceId_Type())
cfprVnicIScsiAutoTargetIfInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprVnicIScsiAutoTargetIfInstanceId.setStatus(_A)
_CfprVnicIScsiAutoTargetIfDn_Type=CfprManagedObjectDn
_CfprVnicIScsiAutoTargetIfDn_Object=MibTableColumn
cfprVnicIScsiAutoTargetIfDn=_CfprVnicIScsiAutoTargetIfDn_Object((1,3,6,1,4,1,9,9,826,1,83,28,1,2),_CfprVnicIScsiAutoTargetIfDn_Type())
cfprVnicIScsiAutoTargetIfDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIScsiAutoTargetIfDn.setStatus(_A)
_CfprVnicIScsiAutoTargetIfRn_Type=SnmpAdminString
_CfprVnicIScsiAutoTargetIfRn_Object=MibTableColumn
cfprVnicIScsiAutoTargetIfRn=_CfprVnicIScsiAutoTargetIfRn_Object((1,3,6,1,4,1,9,9,826,1,83,28,1,3),_CfprVnicIScsiAutoTargetIfRn_Type())
cfprVnicIScsiAutoTargetIfRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIScsiAutoTargetIfRn.setStatus(_A)
_CfprVnicIScsiAutoTargetIfDhcpVendorId_Type=SnmpAdminString
_CfprVnicIScsiAutoTargetIfDhcpVendorId_Object=MibTableColumn
cfprVnicIScsiAutoTargetIfDhcpVendorId=_CfprVnicIScsiAutoTargetIfDhcpVendorId_Object((1,3,6,1,4,1,9,9,826,1,83,28,1,4),_CfprVnicIScsiAutoTargetIfDhcpVendorId_Type())
cfprVnicIScsiAutoTargetIfDhcpVendorId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIScsiAutoTargetIfDhcpVendorId.setStatus(_A)
_CfprVnicIScsiBootParamsTable_Object=MibTable
cfprVnicIScsiBootParamsTable=_CfprVnicIScsiBootParamsTable_Object((1,3,6,1,4,1,9,9,826,1,83,29))
if mibBuilder.loadTexts:cfprVnicIScsiBootParamsTable.setStatus(_A)
_CfprVnicIScsiBootParamsEntry_Object=MibTableRow
cfprVnicIScsiBootParamsEntry=_CfprVnicIScsiBootParamsEntry_Object((1,3,6,1,4,1,9,9,826,1,83,29,1))
cfprVnicIScsiBootParamsEntry.setIndexNames((0,_C,_g))
if mibBuilder.loadTexts:cfprVnicIScsiBootParamsEntry.setStatus(_A)
_CfprVnicIScsiBootParamsInstanceId_Type=CfprManagedObjectId
_CfprVnicIScsiBootParamsInstanceId_Object=MibTableColumn
cfprVnicIScsiBootParamsInstanceId=_CfprVnicIScsiBootParamsInstanceId_Object((1,3,6,1,4,1,9,9,826,1,83,29,1,1),_CfprVnicIScsiBootParamsInstanceId_Type())
cfprVnicIScsiBootParamsInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprVnicIScsiBootParamsInstanceId.setStatus(_A)
_CfprVnicIScsiBootParamsDn_Type=CfprManagedObjectDn
_CfprVnicIScsiBootParamsDn_Object=MibTableColumn
cfprVnicIScsiBootParamsDn=_CfprVnicIScsiBootParamsDn_Object((1,3,6,1,4,1,9,9,826,1,83,29,1,2),_CfprVnicIScsiBootParamsDn_Type())
cfprVnicIScsiBootParamsDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIScsiBootParamsDn.setStatus(_A)
_CfprVnicIScsiBootParamsRn_Type=SnmpAdminString
_CfprVnicIScsiBootParamsRn_Object=MibTableColumn
cfprVnicIScsiBootParamsRn=_CfprVnicIScsiBootParamsRn_Object((1,3,6,1,4,1,9,9,826,1,83,29,1,3),_CfprVnicIScsiBootParamsRn_Type())
cfprVnicIScsiBootParamsRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIScsiBootParamsRn.setStatus(_A)
_CfprVnicIScsiBootParamsDescr_Type=SnmpAdminString
_CfprVnicIScsiBootParamsDescr_Object=MibTableColumn
cfprVnicIScsiBootParamsDescr=_CfprVnicIScsiBootParamsDescr_Object((1,3,6,1,4,1,9,9,826,1,83,29,1,4),_CfprVnicIScsiBootParamsDescr_Type())
cfprVnicIScsiBootParamsDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIScsiBootParamsDescr.setStatus(_A)
_CfprVnicIScsiBootParamsIntId_Type=SnmpAdminString
_CfprVnicIScsiBootParamsIntId_Object=MibTableColumn
cfprVnicIScsiBootParamsIntId=_CfprVnicIScsiBootParamsIntId_Object((1,3,6,1,4,1,9,9,826,1,83,29,1,5),_CfprVnicIScsiBootParamsIntId_Type())
cfprVnicIScsiBootParamsIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIScsiBootParamsIntId.setStatus(_A)
_CfprVnicIScsiBootParamsName_Type=SnmpAdminString
_CfprVnicIScsiBootParamsName_Object=MibTableColumn
cfprVnicIScsiBootParamsName=_CfprVnicIScsiBootParamsName_Object((1,3,6,1,4,1,9,9,826,1,83,29,1,6),_CfprVnicIScsiBootParamsName_Type())
cfprVnicIScsiBootParamsName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIScsiBootParamsName.setStatus(_A)
_CfprVnicIScsiBootParamsPolicyLevel_Type=Gauge32
_CfprVnicIScsiBootParamsPolicyLevel_Object=MibTableColumn
cfprVnicIScsiBootParamsPolicyLevel=_CfprVnicIScsiBootParamsPolicyLevel_Object((1,3,6,1,4,1,9,9,826,1,83,29,1,7),_CfprVnicIScsiBootParamsPolicyLevel_Type())
cfprVnicIScsiBootParamsPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIScsiBootParamsPolicyLevel.setStatus(_A)
_CfprVnicIScsiBootParamsPolicyOwner_Type=CfprPolicyPolicyOwner
_CfprVnicIScsiBootParamsPolicyOwner_Object=MibTableColumn
cfprVnicIScsiBootParamsPolicyOwner=_CfprVnicIScsiBootParamsPolicyOwner_Object((1,3,6,1,4,1,9,9,826,1,83,29,1,8),_CfprVnicIScsiBootParamsPolicyOwner_Type())
cfprVnicIScsiBootParamsPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIScsiBootParamsPolicyOwner.setStatus(_A)
_CfprVnicIScsiBootVnicTable_Object=MibTable
cfprVnicIScsiBootVnicTable=_CfprVnicIScsiBootVnicTable_Object((1,3,6,1,4,1,9,9,826,1,83,30))
if mibBuilder.loadTexts:cfprVnicIScsiBootVnicTable.setStatus(_A)
_CfprVnicIScsiBootVnicEntry_Object=MibTableRow
cfprVnicIScsiBootVnicEntry=_CfprVnicIScsiBootVnicEntry_Object((1,3,6,1,4,1,9,9,826,1,83,30,1))
cfprVnicIScsiBootVnicEntry.setIndexNames((0,_C,_h))
if mibBuilder.loadTexts:cfprVnicIScsiBootVnicEntry.setStatus(_A)
_CfprVnicIScsiBootVnicInstanceId_Type=CfprManagedObjectId
_CfprVnicIScsiBootVnicInstanceId_Object=MibTableColumn
cfprVnicIScsiBootVnicInstanceId=_CfprVnicIScsiBootVnicInstanceId_Object((1,3,6,1,4,1,9,9,826,1,83,30,1,1),_CfprVnicIScsiBootVnicInstanceId_Type())
cfprVnicIScsiBootVnicInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprVnicIScsiBootVnicInstanceId.setStatus(_A)
_CfprVnicIScsiBootVnicDn_Type=CfprManagedObjectDn
_CfprVnicIScsiBootVnicDn_Object=MibTableColumn
cfprVnicIScsiBootVnicDn=_CfprVnicIScsiBootVnicDn_Object((1,3,6,1,4,1,9,9,826,1,83,30,1,2),_CfprVnicIScsiBootVnicDn_Type())
cfprVnicIScsiBootVnicDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIScsiBootVnicDn.setStatus(_A)
_CfprVnicIScsiBootVnicRn_Type=SnmpAdminString
_CfprVnicIScsiBootVnicRn_Object=MibTableColumn
cfprVnicIScsiBootVnicRn=_CfprVnicIScsiBootVnicRn_Object((1,3,6,1,4,1,9,9,826,1,83,30,1,3),_CfprVnicIScsiBootVnicRn_Type())
cfprVnicIScsiBootVnicRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIScsiBootVnicRn.setStatus(_A)
_CfprVnicIScsiBootVnicAuthProfileName_Type=SnmpAdminString
_CfprVnicIScsiBootVnicAuthProfileName_Object=MibTableColumn
cfprVnicIScsiBootVnicAuthProfileName=_CfprVnicIScsiBootVnicAuthProfileName_Object((1,3,6,1,4,1,9,9,826,1,83,30,1,4),_CfprVnicIScsiBootVnicAuthProfileName_Type())
cfprVnicIScsiBootVnicAuthProfileName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIScsiBootVnicAuthProfileName.setStatus(_A)
_CfprVnicIScsiBootVnicDescr_Type=SnmpAdminString
_CfprVnicIScsiBootVnicDescr_Object=MibTableColumn
cfprVnicIScsiBootVnicDescr=_CfprVnicIScsiBootVnicDescr_Object((1,3,6,1,4,1,9,9,826,1,83,30,1,5),_CfprVnicIScsiBootVnicDescr_Type())
cfprVnicIScsiBootVnicDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIScsiBootVnicDescr.setStatus(_A)
_CfprVnicIScsiBootVnicInitiatorName_Type=SnmpAdminString
_CfprVnicIScsiBootVnicInitiatorName_Object=MibTableColumn
cfprVnicIScsiBootVnicInitiatorName=_CfprVnicIScsiBootVnicInitiatorName_Object((1,3,6,1,4,1,9,9,826,1,83,30,1,6),_CfprVnicIScsiBootVnicInitiatorName_Type())
cfprVnicIScsiBootVnicInitiatorName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIScsiBootVnicInitiatorName.setStatus(_A)
_CfprVnicIScsiBootVnicIntId_Type=SnmpAdminString
_CfprVnicIScsiBootVnicIntId_Object=MibTableColumn
cfprVnicIScsiBootVnicIntId=_CfprVnicIScsiBootVnicIntId_Object((1,3,6,1,4,1,9,9,826,1,83,30,1,7),_CfprVnicIScsiBootVnicIntId_Type())
cfprVnicIScsiBootVnicIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIScsiBootVnicIntId.setStatus(_A)
_CfprVnicIScsiBootVnicIqnIdentPoolName_Type=SnmpAdminString
_CfprVnicIScsiBootVnicIqnIdentPoolName_Object=MibTableColumn
cfprVnicIScsiBootVnicIqnIdentPoolName=_CfprVnicIScsiBootVnicIqnIdentPoolName_Object((1,3,6,1,4,1,9,9,826,1,83,30,1,8),_CfprVnicIScsiBootVnicIqnIdentPoolName_Type())
cfprVnicIScsiBootVnicIqnIdentPoolName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIScsiBootVnicIqnIdentPoolName.setStatus(_A)
_CfprVnicIScsiBootVnicName_Type=SnmpAdminString
_CfprVnicIScsiBootVnicName_Object=MibTableColumn
cfprVnicIScsiBootVnicName=_CfprVnicIScsiBootVnicName_Object((1,3,6,1,4,1,9,9,826,1,83,30,1,9),_CfprVnicIScsiBootVnicName_Type())
cfprVnicIScsiBootVnicName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIScsiBootVnicName.setStatus(_A)
_CfprVnicIScsiBootVnicOperAuthProfileName_Type=SnmpAdminString
_CfprVnicIScsiBootVnicOperAuthProfileName_Object=MibTableColumn
cfprVnicIScsiBootVnicOperAuthProfileName=_CfprVnicIScsiBootVnicOperAuthProfileName_Object((1,3,6,1,4,1,9,9,826,1,83,30,1,10),_CfprVnicIScsiBootVnicOperAuthProfileName_Type())
cfprVnicIScsiBootVnicOperAuthProfileName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIScsiBootVnicOperAuthProfileName.setStatus(_A)
_CfprVnicIScsiBootVnicOperIqnIdentPoolName_Type=SnmpAdminString
_CfprVnicIScsiBootVnicOperIqnIdentPoolName_Object=MibTableColumn
cfprVnicIScsiBootVnicOperIqnIdentPoolName=_CfprVnicIScsiBootVnicOperIqnIdentPoolName_Object((1,3,6,1,4,1,9,9,826,1,83,30,1,11),_CfprVnicIScsiBootVnicOperIqnIdentPoolName_Type())
cfprVnicIScsiBootVnicOperIqnIdentPoolName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIScsiBootVnicOperIqnIdentPoolName.setStatus(_A)
_CfprVnicIScsiBootVnicPolicyLevel_Type=Gauge32
_CfprVnicIScsiBootVnicPolicyLevel_Object=MibTableColumn
cfprVnicIScsiBootVnicPolicyLevel=_CfprVnicIScsiBootVnicPolicyLevel_Object((1,3,6,1,4,1,9,9,826,1,83,30,1,12),_CfprVnicIScsiBootVnicPolicyLevel_Type())
cfprVnicIScsiBootVnicPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIScsiBootVnicPolicyLevel.setStatus(_A)
_CfprVnicIScsiBootVnicPolicyOwner_Type=CfprPolicyPolicyOwner
_CfprVnicIScsiBootVnicPolicyOwner_Object=MibTableColumn
cfprVnicIScsiBootVnicPolicyOwner=_CfprVnicIScsiBootVnicPolicyOwner_Object((1,3,6,1,4,1,9,9,826,1,83,30,1,13),_CfprVnicIScsiBootVnicPolicyOwner_Type())
cfprVnicIScsiBootVnicPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIScsiBootVnicPolicyOwner.setStatus(_A)
_CfprVnicIScsiLCPTable_Object=MibTable
cfprVnicIScsiLCPTable=_CfprVnicIScsiLCPTable_Object((1,3,6,1,4,1,9,9,826,1,83,31))
if mibBuilder.loadTexts:cfprVnicIScsiLCPTable.setStatus(_A)
_CfprVnicIScsiLCPEntry_Object=MibTableRow
cfprVnicIScsiLCPEntry=_CfprVnicIScsiLCPEntry_Object((1,3,6,1,4,1,9,9,826,1,83,31,1))
cfprVnicIScsiLCPEntry.setIndexNames((0,_C,_i))
if mibBuilder.loadTexts:cfprVnicIScsiLCPEntry.setStatus(_A)
_CfprVnicIScsiLCPInstanceId_Type=CfprManagedObjectId
_CfprVnicIScsiLCPInstanceId_Object=MibTableColumn
cfprVnicIScsiLCPInstanceId=_CfprVnicIScsiLCPInstanceId_Object((1,3,6,1,4,1,9,9,826,1,83,31,1,1),_CfprVnicIScsiLCPInstanceId_Type())
cfprVnicIScsiLCPInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprVnicIScsiLCPInstanceId.setStatus(_A)
_CfprVnicIScsiLCPDn_Type=CfprManagedObjectDn
_CfprVnicIScsiLCPDn_Object=MibTableColumn
cfprVnicIScsiLCPDn=_CfprVnicIScsiLCPDn_Object((1,3,6,1,4,1,9,9,826,1,83,31,1,2),_CfprVnicIScsiLCPDn_Type())
cfprVnicIScsiLCPDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIScsiLCPDn.setStatus(_A)
_CfprVnicIScsiLCPRn_Type=SnmpAdminString
_CfprVnicIScsiLCPRn_Object=MibTableColumn
cfprVnicIScsiLCPRn=_CfprVnicIScsiLCPRn_Object((1,3,6,1,4,1,9,9,826,1,83,31,1,3),_CfprVnicIScsiLCPRn_Type())
cfprVnicIScsiLCPRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIScsiLCPRn.setStatus(_A)
_CfprVnicIScsiLCPAdaptorProfileName_Type=SnmpAdminString
_CfprVnicIScsiLCPAdaptorProfileName_Object=MibTableColumn
cfprVnicIScsiLCPAdaptorProfileName=_CfprVnicIScsiLCPAdaptorProfileName_Object((1,3,6,1,4,1,9,9,826,1,83,31,1,4),_CfprVnicIScsiLCPAdaptorProfileName_Type())
cfprVnicIScsiLCPAdaptorProfileName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIScsiLCPAdaptorProfileName.setStatus(_A)
_CfprVnicIScsiLCPAddr_Type=MacAddress
_CfprVnicIScsiLCPAddr_Object=MibTableColumn
cfprVnicIScsiLCPAddr=_CfprVnicIScsiLCPAddr_Object((1,3,6,1,4,1,9,9,826,1,83,31,1,5),_CfprVnicIScsiLCPAddr_Type())
cfprVnicIScsiLCPAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIScsiLCPAddr.setStatus(_A)
_CfprVnicIScsiLCPAdminHostPort_Type=CfprFabricHostPortId
_CfprVnicIScsiLCPAdminHostPort_Object=MibTableColumn
cfprVnicIScsiLCPAdminHostPort=_CfprVnicIScsiLCPAdminHostPort_Object((1,3,6,1,4,1,9,9,826,1,83,31,1,6),_CfprVnicIScsiLCPAdminHostPort_Type())
cfprVnicIScsiLCPAdminHostPort.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIScsiLCPAdminHostPort.setStatus(_A)
_CfprVnicIScsiLCPAdminVcon_Type=SnmpAdminString
_CfprVnicIScsiLCPAdminVcon_Object=MibTableColumn
cfprVnicIScsiLCPAdminVcon=_CfprVnicIScsiLCPAdminVcon_Object((1,3,6,1,4,1,9,9,826,1,83,31,1,7),_CfprVnicIScsiLCPAdminVcon_Type())
cfprVnicIScsiLCPAdminVcon.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIScsiLCPAdminVcon.setStatus(_A)
_CfprVnicIScsiLCPAppRole_Type=CfprVnicAppRole
_CfprVnicIScsiLCPAppRole_Object=MibTableColumn
cfprVnicIScsiLCPAppRole=_CfprVnicIScsiLCPAppRole_Object((1,3,6,1,4,1,9,9,826,1,83,31,1,8),_CfprVnicIScsiLCPAppRole_Type())
cfprVnicIScsiLCPAppRole.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIScsiLCPAppRole.setStatus(_A)
_CfprVnicIScsiLCPBootDev_Type=CfprVnicVnicBootDev
_CfprVnicIScsiLCPBootDev_Object=MibTableColumn
cfprVnicIScsiLCPBootDev=_CfprVnicIScsiLCPBootDev_Object((1,3,6,1,4,1,9,9,826,1,83,31,1,9),_CfprVnicIScsiLCPBootDev_Type())
cfprVnicIScsiLCPBootDev.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIScsiLCPBootDev.setStatus(_A)
_CfprVnicIScsiLCPConfigQualifier_Type=CfprVnicConfigIssues
_CfprVnicIScsiLCPConfigQualifier_Object=MibTableColumn
cfprVnicIScsiLCPConfigQualifier=_CfprVnicIScsiLCPConfigQualifier_Object((1,3,6,1,4,1,9,9,826,1,83,31,1,10),_CfprVnicIScsiLCPConfigQualifier_Type())
cfprVnicIScsiLCPConfigQualifier.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIScsiLCPConfigQualifier.setStatus(_A)
_CfprVnicIScsiLCPConfigState_Type=CfprLsConfigState
_CfprVnicIScsiLCPConfigState_Object=MibTableColumn
cfprVnicIScsiLCPConfigState=_CfprVnicIScsiLCPConfigState_Object((1,3,6,1,4,1,9,9,826,1,83,31,1,11),_CfprVnicIScsiLCPConfigState_Type())
cfprVnicIScsiLCPConfigState.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIScsiLCPConfigState.setStatus(_A)
_CfprVnicIScsiLCPEquipmentDn_Type=SnmpAdminString
_CfprVnicIScsiLCPEquipmentDn_Object=MibTableColumn
cfprVnicIScsiLCPEquipmentDn=_CfprVnicIScsiLCPEquipmentDn_Object((1,3,6,1,4,1,9,9,826,1,83,31,1,12),_CfprVnicIScsiLCPEquipmentDn_Type())
cfprVnicIScsiLCPEquipmentDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIScsiLCPEquipmentDn.setStatus(_A)
_CfprVnicIScsiLCPFltAggr_Type=Unsigned64
_CfprVnicIScsiLCPFltAggr_Object=MibTableColumn
cfprVnicIScsiLCPFltAggr=_CfprVnicIScsiLCPFltAggr_Object((1,3,6,1,4,1,9,9,826,1,83,31,1,13),_CfprVnicIScsiLCPFltAggr_Type())
cfprVnicIScsiLCPFltAggr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIScsiLCPFltAggr.setStatus(_A)
_CfprVnicIScsiLCPIdentPoolName_Type=SnmpAdminString
_CfprVnicIScsiLCPIdentPoolName_Object=MibTableColumn
cfprVnicIScsiLCPIdentPoolName=_CfprVnicIScsiLCPIdentPoolName_Object((1,3,6,1,4,1,9,9,826,1,83,31,1,14),_CfprVnicIScsiLCPIdentPoolName_Type())
cfprVnicIScsiLCPIdentPoolName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIScsiLCPIdentPoolName.setStatus(_A)
_CfprVnicIScsiLCPInstType_Type=CfprVnicInstantiation
_CfprVnicIScsiLCPInstType_Object=MibTableColumn
cfprVnicIScsiLCPInstType=_CfprVnicIScsiLCPInstType_Object((1,3,6,1,4,1,9,9,826,1,83,31,1,15),_CfprVnicIScsiLCPInstType_Type())
cfprVnicIScsiLCPInstType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIScsiLCPInstType.setStatus(_A)
_CfprVnicIScsiLCPName_Type=SnmpAdminString
_CfprVnicIScsiLCPName_Object=MibTableColumn
cfprVnicIScsiLCPName=_CfprVnicIScsiLCPName_Object((1,3,6,1,4,1,9,9,826,1,83,31,1,16),_CfprVnicIScsiLCPName_Type())
cfprVnicIScsiLCPName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIScsiLCPName.setStatus(_A)
_CfprVnicIScsiLCPNwTemplName_Type=SnmpAdminString
_CfprVnicIScsiLCPNwTemplName_Object=MibTableColumn
cfprVnicIScsiLCPNwTemplName=_CfprVnicIScsiLCPNwTemplName_Object((1,3,6,1,4,1,9,9,826,1,83,31,1,17),_CfprVnicIScsiLCPNwTemplName_Type())
cfprVnicIScsiLCPNwTemplName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIScsiLCPNwTemplName.setStatus(_A)
_CfprVnicIScsiLCPOperAdaptorProfileName_Type=SnmpAdminString
_CfprVnicIScsiLCPOperAdaptorProfileName_Object=MibTableColumn
cfprVnicIScsiLCPOperAdaptorProfileName=_CfprVnicIScsiLCPOperAdaptorProfileName_Object((1,3,6,1,4,1,9,9,826,1,83,31,1,18),_CfprVnicIScsiLCPOperAdaptorProfileName_Type())
cfprVnicIScsiLCPOperAdaptorProfileName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIScsiLCPOperAdaptorProfileName.setStatus(_A)
_CfprVnicIScsiLCPOperHostPort_Type=CfprVnicVnicOperHostPort
_CfprVnicIScsiLCPOperHostPort_Object=MibTableColumn
cfprVnicIScsiLCPOperHostPort=_CfprVnicIScsiLCPOperHostPort_Object((1,3,6,1,4,1,9,9,826,1,83,31,1,19),_CfprVnicIScsiLCPOperHostPort_Type())
cfprVnicIScsiLCPOperHostPort.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIScsiLCPOperHostPort.setStatus(_A)
_CfprVnicIScsiLCPOperIdentPoolName_Type=SnmpAdminString
_CfprVnicIScsiLCPOperIdentPoolName_Object=MibTableColumn
cfprVnicIScsiLCPOperIdentPoolName=_CfprVnicIScsiLCPOperIdentPoolName_Object((1,3,6,1,4,1,9,9,826,1,83,31,1,20),_CfprVnicIScsiLCPOperIdentPoolName_Type())
cfprVnicIScsiLCPOperIdentPoolName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIScsiLCPOperIdentPoolName.setStatus(_A)
_CfprVnicIScsiLCPOperOrder_Type=Gauge32
_CfprVnicIScsiLCPOperOrder_Object=MibTableColumn
cfprVnicIScsiLCPOperOrder=_CfprVnicIScsiLCPOperOrder_Object((1,3,6,1,4,1,9,9,826,1,83,31,1,21),_CfprVnicIScsiLCPOperOrder_Type())
cfprVnicIScsiLCPOperOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIScsiLCPOperOrder.setStatus(_A)
_CfprVnicIScsiLCPOperSpeed_Type=Gauge32
_CfprVnicIScsiLCPOperSpeed_Object=MibTableColumn
cfprVnicIScsiLCPOperSpeed=_CfprVnicIScsiLCPOperSpeed_Object((1,3,6,1,4,1,9,9,826,1,83,31,1,22),_CfprVnicIScsiLCPOperSpeed_Type())
cfprVnicIScsiLCPOperSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIScsiLCPOperSpeed.setStatus(_A)
_CfprVnicIScsiLCPOperStatsPolicyName_Type=SnmpAdminString
_CfprVnicIScsiLCPOperStatsPolicyName_Object=MibTableColumn
cfprVnicIScsiLCPOperStatsPolicyName=_CfprVnicIScsiLCPOperStatsPolicyName_Object((1,3,6,1,4,1,9,9,826,1,83,31,1,23),_CfprVnicIScsiLCPOperStatsPolicyName_Type())
cfprVnicIScsiLCPOperStatsPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIScsiLCPOperStatsPolicyName.setStatus(_A)
_CfprVnicIScsiLCPOperVcon_Type=SnmpAdminString
_CfprVnicIScsiLCPOperVcon_Object=MibTableColumn
cfprVnicIScsiLCPOperVcon=_CfprVnicIScsiLCPOperVcon_Object((1,3,6,1,4,1,9,9,826,1,83,31,1,24),_CfprVnicIScsiLCPOperVcon_Type())
cfprVnicIScsiLCPOperVcon.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIScsiLCPOperVcon.setStatus(_A)
_CfprVnicIScsiLCPOrder_Type=Gauge32
_CfprVnicIScsiLCPOrder_Object=MibTableColumn
cfprVnicIScsiLCPOrder=_CfprVnicIScsiLCPOrder_Object((1,3,6,1,4,1,9,9,826,1,83,31,1,25),_CfprVnicIScsiLCPOrder_Type())
cfprVnicIScsiLCPOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIScsiLCPOrder.setStatus(_A)
_CfprVnicIScsiLCPOwner_Type=CfprVnicConnectionOwner
_CfprVnicIScsiLCPOwner_Object=MibTableColumn
cfprVnicIScsiLCPOwner=_CfprVnicIScsiLCPOwner_Object((1,3,6,1,4,1,9,9,826,1,83,31,1,26),_CfprVnicIScsiLCPOwner_Type())
cfprVnicIScsiLCPOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIScsiLCPOwner.setStatus(_A)
_CfprVnicIScsiLCPPinToGroupName_Type=SnmpAdminString
_CfprVnicIScsiLCPPinToGroupName_Object=MibTableColumn
cfprVnicIScsiLCPPinToGroupName=_CfprVnicIScsiLCPPinToGroupName_Object((1,3,6,1,4,1,9,9,826,1,83,31,1,27),_CfprVnicIScsiLCPPinToGroupName_Type())
cfprVnicIScsiLCPPinToGroupName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIScsiLCPPinToGroupName.setStatus(_A)
_CfprVnicIScsiLCPQosPolicyName_Type=SnmpAdminString
_CfprVnicIScsiLCPQosPolicyName_Object=MibTableColumn
cfprVnicIScsiLCPQosPolicyName=_CfprVnicIScsiLCPQosPolicyName_Object((1,3,6,1,4,1,9,9,826,1,83,31,1,28),_CfprVnicIScsiLCPQosPolicyName_Type())
cfprVnicIScsiLCPQosPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIScsiLCPQosPolicyName.setStatus(_A)
_CfprVnicIScsiLCPStatsPolicyName_Type=SnmpAdminString
_CfprVnicIScsiLCPStatsPolicyName_Object=MibTableColumn
cfprVnicIScsiLCPStatsPolicyName=_CfprVnicIScsiLCPStatsPolicyName_Object((1,3,6,1,4,1,9,9,826,1,83,31,1,29),_CfprVnicIScsiLCPStatsPolicyName_Type())
cfprVnicIScsiLCPStatsPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIScsiLCPStatsPolicyName.setStatus(_A)
_CfprVnicIScsiLCPSwitchId_Type=CfprNetworkSwitchId
_CfprVnicIScsiLCPSwitchId_Object=MibTableColumn
cfprVnicIScsiLCPSwitchId=_CfprVnicIScsiLCPSwitchId_Object((1,3,6,1,4,1,9,9,826,1,83,31,1,30),_CfprVnicIScsiLCPSwitchId_Type())
cfprVnicIScsiLCPSwitchId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIScsiLCPSwitchId.setStatus(_A)
_CfprVnicIScsiLCPType_Type=CfprVnicConnectionType
_CfprVnicIScsiLCPType_Object=MibTableColumn
cfprVnicIScsiLCPType=_CfprVnicIScsiLCPType_Object((1,3,6,1,4,1,9,9,826,1,83,31,1,31),_CfprVnicIScsiLCPType_Type())
cfprVnicIScsiLCPType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIScsiLCPType.setStatus(_A)
_CfprVnicIScsiLCPVnicName_Type=SnmpAdminString
_CfprVnicIScsiLCPVnicName_Object=MibTableColumn
cfprVnicIScsiLCPVnicName=_CfprVnicIScsiLCPVnicName_Object((1,3,6,1,4,1,9,9,826,1,83,31,1,32),_CfprVnicIScsiLCPVnicName_Type())
cfprVnicIScsiLCPVnicName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIScsiLCPVnicName.setStatus(_A)
_CfprVnicIScsiNodeTable_Object=MibTable
cfprVnicIScsiNodeTable=_CfprVnicIScsiNodeTable_Object((1,3,6,1,4,1,9,9,826,1,83,32))
if mibBuilder.loadTexts:cfprVnicIScsiNodeTable.setStatus(_A)
_CfprVnicIScsiNodeEntry_Object=MibTableRow
cfprVnicIScsiNodeEntry=_CfprVnicIScsiNodeEntry_Object((1,3,6,1,4,1,9,9,826,1,83,32,1))
cfprVnicIScsiNodeEntry.setIndexNames((0,_C,_j))
if mibBuilder.loadTexts:cfprVnicIScsiNodeEntry.setStatus(_A)
_CfprVnicIScsiNodeInstanceId_Type=CfprManagedObjectId
_CfprVnicIScsiNodeInstanceId_Object=MibTableColumn
cfprVnicIScsiNodeInstanceId=_CfprVnicIScsiNodeInstanceId_Object((1,3,6,1,4,1,9,9,826,1,83,32,1,1),_CfprVnicIScsiNodeInstanceId_Type())
cfprVnicIScsiNodeInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprVnicIScsiNodeInstanceId.setStatus(_A)
_CfprVnicIScsiNodeDn_Type=CfprManagedObjectDn
_CfprVnicIScsiNodeDn_Object=MibTableColumn
cfprVnicIScsiNodeDn=_CfprVnicIScsiNodeDn_Object((1,3,6,1,4,1,9,9,826,1,83,32,1,2),_CfprVnicIScsiNodeDn_Type())
cfprVnicIScsiNodeDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIScsiNodeDn.setStatus(_A)
_CfprVnicIScsiNodeRn_Type=SnmpAdminString
_CfprVnicIScsiNodeRn_Object=MibTableColumn
cfprVnicIScsiNodeRn=_CfprVnicIScsiNodeRn_Object((1,3,6,1,4,1,9,9,826,1,83,32,1,3),_CfprVnicIScsiNodeRn_Type())
cfprVnicIScsiNodeRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIScsiNodeRn.setStatus(_A)
_CfprVnicIScsiNodeFltAggr_Type=Unsigned64
_CfprVnicIScsiNodeFltAggr_Object=MibTableColumn
cfprVnicIScsiNodeFltAggr=_CfprVnicIScsiNodeFltAggr_Object((1,3,6,1,4,1,9,9,826,1,83,32,1,4),_CfprVnicIScsiNodeFltAggr_Type())
cfprVnicIScsiNodeFltAggr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIScsiNodeFltAggr.setStatus(_A)
_CfprVnicIScsiNodeInitNameSuffix_Type=SnmpAdminString
_CfprVnicIScsiNodeInitNameSuffix_Object=MibTableColumn
cfprVnicIScsiNodeInitNameSuffix=_CfprVnicIScsiNodeInitNameSuffix_Object((1,3,6,1,4,1,9,9,826,1,83,32,1,5),_CfprVnicIScsiNodeInitNameSuffix_Type())
cfprVnicIScsiNodeInitNameSuffix.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIScsiNodeInitNameSuffix.setStatus(_A)
_CfprVnicIScsiNodeInitiatorName_Type=SnmpAdminString
_CfprVnicIScsiNodeInitiatorName_Object=MibTableColumn
cfprVnicIScsiNodeInitiatorName=_CfprVnicIScsiNodeInitiatorName_Object((1,3,6,1,4,1,9,9,826,1,83,32,1,6),_CfprVnicIScsiNodeInitiatorName_Type())
cfprVnicIScsiNodeInitiatorName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIScsiNodeInitiatorName.setStatus(_A)
_CfprVnicIScsiNodeIqnIdentPoolName_Type=SnmpAdminString
_CfprVnicIScsiNodeIqnIdentPoolName_Object=MibTableColumn
cfprVnicIScsiNodeIqnIdentPoolName=_CfprVnicIScsiNodeIqnIdentPoolName_Object((1,3,6,1,4,1,9,9,826,1,83,32,1,7),_CfprVnicIScsiNodeIqnIdentPoolName_Type())
cfprVnicIScsiNodeIqnIdentPoolName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIScsiNodeIqnIdentPoolName.setStatus(_A)
_CfprVnicIScsiNodeOperIqnIdentPoolName_Type=SnmpAdminString
_CfprVnicIScsiNodeOperIqnIdentPoolName_Object=MibTableColumn
cfprVnicIScsiNodeOperIqnIdentPoolName=_CfprVnicIScsiNodeOperIqnIdentPoolName_Object((1,3,6,1,4,1,9,9,826,1,83,32,1,8),_CfprVnicIScsiNodeOperIqnIdentPoolName_Type())
cfprVnicIScsiNodeOperIqnIdentPoolName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIScsiNodeOperIqnIdentPoolName.setStatus(_A)
_CfprVnicIScsiNodeOwner_Type=CfprVnicIScsiNodeOwner
_CfprVnicIScsiNodeOwner_Object=MibTableColumn
cfprVnicIScsiNodeOwner=_CfprVnicIScsiNodeOwner_Object((1,3,6,1,4,1,9,9,826,1,83,32,1,9),_CfprVnicIScsiNodeOwner_Type())
cfprVnicIScsiNodeOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIScsiNodeOwner.setStatus(_A)
_CfprVnicIScsiStaticTargetIfTable_Object=MibTable
cfprVnicIScsiStaticTargetIfTable=_CfprVnicIScsiStaticTargetIfTable_Object((1,3,6,1,4,1,9,9,826,1,83,33))
if mibBuilder.loadTexts:cfprVnicIScsiStaticTargetIfTable.setStatus(_A)
_CfprVnicIScsiStaticTargetIfEntry_Object=MibTableRow
cfprVnicIScsiStaticTargetIfEntry=_CfprVnicIScsiStaticTargetIfEntry_Object((1,3,6,1,4,1,9,9,826,1,83,33,1))
cfprVnicIScsiStaticTargetIfEntry.setIndexNames((0,_C,_k))
if mibBuilder.loadTexts:cfprVnicIScsiStaticTargetIfEntry.setStatus(_A)
_CfprVnicIScsiStaticTargetIfInstanceId_Type=CfprManagedObjectId
_CfprVnicIScsiStaticTargetIfInstanceId_Object=MibTableColumn
cfprVnicIScsiStaticTargetIfInstanceId=_CfprVnicIScsiStaticTargetIfInstanceId_Object((1,3,6,1,4,1,9,9,826,1,83,33,1,1),_CfprVnicIScsiStaticTargetIfInstanceId_Type())
cfprVnicIScsiStaticTargetIfInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprVnicIScsiStaticTargetIfInstanceId.setStatus(_A)
_CfprVnicIScsiStaticTargetIfDn_Type=CfprManagedObjectDn
_CfprVnicIScsiStaticTargetIfDn_Object=MibTableColumn
cfprVnicIScsiStaticTargetIfDn=_CfprVnicIScsiStaticTargetIfDn_Object((1,3,6,1,4,1,9,9,826,1,83,33,1,2),_CfprVnicIScsiStaticTargetIfDn_Type())
cfprVnicIScsiStaticTargetIfDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIScsiStaticTargetIfDn.setStatus(_A)
_CfprVnicIScsiStaticTargetIfRn_Type=SnmpAdminString
_CfprVnicIScsiStaticTargetIfRn_Object=MibTableColumn
cfprVnicIScsiStaticTargetIfRn=_CfprVnicIScsiStaticTargetIfRn_Object((1,3,6,1,4,1,9,9,826,1,83,33,1,3),_CfprVnicIScsiStaticTargetIfRn_Type())
cfprVnicIScsiStaticTargetIfRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIScsiStaticTargetIfRn.setStatus(_A)
_CfprVnicIScsiStaticTargetIfAuthProfileName_Type=SnmpAdminString
_CfprVnicIScsiStaticTargetIfAuthProfileName_Object=MibTableColumn
cfprVnicIScsiStaticTargetIfAuthProfileName=_CfprVnicIScsiStaticTargetIfAuthProfileName_Object((1,3,6,1,4,1,9,9,826,1,83,33,1,4),_CfprVnicIScsiStaticTargetIfAuthProfileName_Type())
cfprVnicIScsiStaticTargetIfAuthProfileName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIScsiStaticTargetIfAuthProfileName.setStatus(_A)
_CfprVnicIScsiStaticTargetIfIpAddress_Type=InetAddressIPv4
_CfprVnicIScsiStaticTargetIfIpAddress_Object=MibTableColumn
cfprVnicIScsiStaticTargetIfIpAddress=_CfprVnicIScsiStaticTargetIfIpAddress_Object((1,3,6,1,4,1,9,9,826,1,83,33,1,5),_CfprVnicIScsiStaticTargetIfIpAddress_Type())
cfprVnicIScsiStaticTargetIfIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIScsiStaticTargetIfIpAddress.setStatus(_A)
_CfprVnicIScsiStaticTargetIfName_Type=SnmpAdminString
_CfprVnicIScsiStaticTargetIfName_Object=MibTableColumn
cfprVnicIScsiStaticTargetIfName=_CfprVnicIScsiStaticTargetIfName_Object((1,3,6,1,4,1,9,9,826,1,83,33,1,6),_CfprVnicIScsiStaticTargetIfName_Type())
cfprVnicIScsiStaticTargetIfName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIScsiStaticTargetIfName.setStatus(_A)
_CfprVnicIScsiStaticTargetIfOperAuthProfileName_Type=SnmpAdminString
_CfprVnicIScsiStaticTargetIfOperAuthProfileName_Object=MibTableColumn
cfprVnicIScsiStaticTargetIfOperAuthProfileName=_CfprVnicIScsiStaticTargetIfOperAuthProfileName_Object((1,3,6,1,4,1,9,9,826,1,83,33,1,7),_CfprVnicIScsiStaticTargetIfOperAuthProfileName_Type())
cfprVnicIScsiStaticTargetIfOperAuthProfileName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIScsiStaticTargetIfOperAuthProfileName.setStatus(_A)
_CfprVnicIScsiStaticTargetIfPort_Type=Gauge32
_CfprVnicIScsiStaticTargetIfPort_Object=MibTableColumn
cfprVnicIScsiStaticTargetIfPort=_CfprVnicIScsiStaticTargetIfPort_Object((1,3,6,1,4,1,9,9,826,1,83,33,1,8),_CfprVnicIScsiStaticTargetIfPort_Type())
cfprVnicIScsiStaticTargetIfPort.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIScsiStaticTargetIfPort.setStatus(_A)
_CfprVnicIScsiStaticTargetIfPriority_Type=Gauge32
_CfprVnicIScsiStaticTargetIfPriority_Object=MibTableColumn
cfprVnicIScsiStaticTargetIfPriority=_CfprVnicIScsiStaticTargetIfPriority_Object((1,3,6,1,4,1,9,9,826,1,83,33,1,9),_CfprVnicIScsiStaticTargetIfPriority_Type())
cfprVnicIScsiStaticTargetIfPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIScsiStaticTargetIfPriority.setStatus(_A)
_CfprVnicInternalProfileTable_Object=MibTable
cfprVnicInternalProfileTable=_CfprVnicInternalProfileTable_Object((1,3,6,1,4,1,9,9,826,1,83,34))
if mibBuilder.loadTexts:cfprVnicInternalProfileTable.setStatus(_A)
_CfprVnicInternalProfileEntry_Object=MibTableRow
cfprVnicInternalProfileEntry=_CfprVnicInternalProfileEntry_Object((1,3,6,1,4,1,9,9,826,1,83,34,1))
cfprVnicInternalProfileEntry.setIndexNames((0,_C,_l))
if mibBuilder.loadTexts:cfprVnicInternalProfileEntry.setStatus(_A)
_CfprVnicInternalProfileInstanceId_Type=CfprManagedObjectId
_CfprVnicInternalProfileInstanceId_Object=MibTableColumn
cfprVnicInternalProfileInstanceId=_CfprVnicInternalProfileInstanceId_Object((1,3,6,1,4,1,9,9,826,1,83,34,1,1),_CfprVnicInternalProfileInstanceId_Type())
cfprVnicInternalProfileInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprVnicInternalProfileInstanceId.setStatus(_A)
_CfprVnicInternalProfileDn_Type=CfprManagedObjectDn
_CfprVnicInternalProfileDn_Object=MibTableColumn
cfprVnicInternalProfileDn=_CfprVnicInternalProfileDn_Object((1,3,6,1,4,1,9,9,826,1,83,34,1,2),_CfprVnicInternalProfileDn_Type())
cfprVnicInternalProfileDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicInternalProfileDn.setStatus(_A)
_CfprVnicInternalProfileRn_Type=SnmpAdminString
_CfprVnicInternalProfileRn_Object=MibTableColumn
cfprVnicInternalProfileRn=_CfprVnicInternalProfileRn_Object((1,3,6,1,4,1,9,9,826,1,83,34,1,3),_CfprVnicInternalProfileRn_Type())
cfprVnicInternalProfileRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicInternalProfileRn.setStatus(_A)
_CfprVnicInternalProfileDescr_Type=SnmpAdminString
_CfprVnicInternalProfileDescr_Object=MibTableColumn
cfprVnicInternalProfileDescr=_CfprVnicInternalProfileDescr_Object((1,3,6,1,4,1,9,9,826,1,83,34,1,4),_CfprVnicInternalProfileDescr_Type())
cfprVnicInternalProfileDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicInternalProfileDescr.setStatus(_A)
_CfprVnicInternalProfileIntId_Type=SnmpAdminString
_CfprVnicInternalProfileIntId_Object=MibTableColumn
cfprVnicInternalProfileIntId=_CfprVnicInternalProfileIntId_Object((1,3,6,1,4,1,9,9,826,1,83,34,1,5),_CfprVnicInternalProfileIntId_Type())
cfprVnicInternalProfileIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicInternalProfileIntId.setStatus(_A)
_CfprVnicInternalProfileMaxPorts_Type=Gauge32
_CfprVnicInternalProfileMaxPorts_Object=MibTableColumn
cfprVnicInternalProfileMaxPorts=_CfprVnicInternalProfileMaxPorts_Object((1,3,6,1,4,1,9,9,826,1,83,34,1,6),_CfprVnicInternalProfileMaxPorts_Type())
cfprVnicInternalProfileMaxPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicInternalProfileMaxPorts.setStatus(_A)
_CfprVnicInternalProfileName_Type=SnmpAdminString
_CfprVnicInternalProfileName_Object=MibTableColumn
cfprVnicInternalProfileName=_CfprVnicInternalProfileName_Object((1,3,6,1,4,1,9,9,826,1,83,34,1,7),_CfprVnicInternalProfileName_Type())
cfprVnicInternalProfileName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicInternalProfileName.setStatus(_A)
_CfprVnicInternalProfilePolicyLevel_Type=Gauge32
_CfprVnicInternalProfilePolicyLevel_Object=MibTableColumn
cfprVnicInternalProfilePolicyLevel=_CfprVnicInternalProfilePolicyLevel_Object((1,3,6,1,4,1,9,9,826,1,83,34,1,8),_CfprVnicInternalProfilePolicyLevel_Type())
cfprVnicInternalProfilePolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicInternalProfilePolicyLevel.setStatus(_A)
_CfprVnicInternalProfilePolicyOwner_Type=CfprPolicyPolicyOwner
_CfprVnicInternalProfilePolicyOwner_Object=MibTableColumn
cfprVnicInternalProfilePolicyOwner=_CfprVnicInternalProfilePolicyOwner_Object((1,3,6,1,4,1,9,9,826,1,83,34,1,9),_CfprVnicInternalProfilePolicyOwner_Type())
cfprVnicInternalProfilePolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicInternalProfilePolicyOwner.setStatus(_A)
_CfprVnicIpV4HistoryTable_Object=MibTable
cfprVnicIpV4HistoryTable=_CfprVnicIpV4HistoryTable_Object((1,3,6,1,4,1,9,9,826,1,83,35))
if mibBuilder.loadTexts:cfprVnicIpV4HistoryTable.setStatus(_A)
_CfprVnicIpV4HistoryEntry_Object=MibTableRow
cfprVnicIpV4HistoryEntry=_CfprVnicIpV4HistoryEntry_Object((1,3,6,1,4,1,9,9,826,1,83,35,1))
cfprVnicIpV4HistoryEntry.setIndexNames((0,_C,_m))
if mibBuilder.loadTexts:cfprVnicIpV4HistoryEntry.setStatus(_A)
_CfprVnicIpV4HistoryInstanceId_Type=CfprManagedObjectId
_CfprVnicIpV4HistoryInstanceId_Object=MibTableColumn
cfprVnicIpV4HistoryInstanceId=_CfprVnicIpV4HistoryInstanceId_Object((1,3,6,1,4,1,9,9,826,1,83,35,1,1),_CfprVnicIpV4HistoryInstanceId_Type())
cfprVnicIpV4HistoryInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprVnicIpV4HistoryInstanceId.setStatus(_A)
_CfprVnicIpV4HistoryDn_Type=CfprManagedObjectDn
_CfprVnicIpV4HistoryDn_Object=MibTableColumn
cfprVnicIpV4HistoryDn=_CfprVnicIpV4HistoryDn_Object((1,3,6,1,4,1,9,9,826,1,83,35,1,2),_CfprVnicIpV4HistoryDn_Type())
cfprVnicIpV4HistoryDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIpV4HistoryDn.setStatus(_A)
_CfprVnicIpV4HistoryRn_Type=SnmpAdminString
_CfprVnicIpV4HistoryRn_Object=MibTableColumn
cfprVnicIpV4HistoryRn=_CfprVnicIpV4HistoryRn_Object((1,3,6,1,4,1,9,9,826,1,83,35,1,3),_CfprVnicIpV4HistoryRn_Type())
cfprVnicIpV4HistoryRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIpV4HistoryRn.setStatus(_A)
_CfprVnicIpV4HistoryOldIpV4Addr_Type=InetAddressIPv4
_CfprVnicIpV4HistoryOldIpV4Addr_Object=MibTableColumn
cfprVnicIpV4HistoryOldIpV4Addr=_CfprVnicIpV4HistoryOldIpV4Addr_Object((1,3,6,1,4,1,9,9,826,1,83,35,1,4),_CfprVnicIpV4HistoryOldIpV4Addr_Type())
cfprVnicIpV4HistoryOldIpV4Addr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIpV4HistoryOldIpV4Addr.setStatus(_A)
_CfprVnicIpV4MgmtPooledAddrTable_Object=MibTable
cfprVnicIpV4MgmtPooledAddrTable=_CfprVnicIpV4MgmtPooledAddrTable_Object((1,3,6,1,4,1,9,9,826,1,83,36))
if mibBuilder.loadTexts:cfprVnicIpV4MgmtPooledAddrTable.setStatus(_A)
_CfprVnicIpV4MgmtPooledAddrEntry_Object=MibTableRow
cfprVnicIpV4MgmtPooledAddrEntry=_CfprVnicIpV4MgmtPooledAddrEntry_Object((1,3,6,1,4,1,9,9,826,1,83,36,1))
cfprVnicIpV4MgmtPooledAddrEntry.setIndexNames((0,_C,_n))
if mibBuilder.loadTexts:cfprVnicIpV4MgmtPooledAddrEntry.setStatus(_A)
_CfprVnicIpV4MgmtPooledAddrInstanceId_Type=CfprManagedObjectId
_CfprVnicIpV4MgmtPooledAddrInstanceId_Object=MibTableColumn
cfprVnicIpV4MgmtPooledAddrInstanceId=_CfprVnicIpV4MgmtPooledAddrInstanceId_Object((1,3,6,1,4,1,9,9,826,1,83,36,1,1),_CfprVnicIpV4MgmtPooledAddrInstanceId_Type())
cfprVnicIpV4MgmtPooledAddrInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprVnicIpV4MgmtPooledAddrInstanceId.setStatus(_A)
_CfprVnicIpV4MgmtPooledAddrDn_Type=CfprManagedObjectDn
_CfprVnicIpV4MgmtPooledAddrDn_Object=MibTableColumn
cfprVnicIpV4MgmtPooledAddrDn=_CfprVnicIpV4MgmtPooledAddrDn_Object((1,3,6,1,4,1,9,9,826,1,83,36,1,2),_CfprVnicIpV4MgmtPooledAddrDn_Type())
cfprVnicIpV4MgmtPooledAddrDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIpV4MgmtPooledAddrDn.setStatus(_A)
_CfprVnicIpV4MgmtPooledAddrRn_Type=SnmpAdminString
_CfprVnicIpV4MgmtPooledAddrRn_Object=MibTableColumn
cfprVnicIpV4MgmtPooledAddrRn=_CfprVnicIpV4MgmtPooledAddrRn_Object((1,3,6,1,4,1,9,9,826,1,83,36,1,3),_CfprVnicIpV4MgmtPooledAddrRn_Type())
cfprVnicIpV4MgmtPooledAddrRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIpV4MgmtPooledAddrRn.setStatus(_A)
_CfprVnicIpV4MgmtPooledAddrAddr_Type=InetAddressIPv4
_CfprVnicIpV4MgmtPooledAddrAddr_Object=MibTableColumn
cfprVnicIpV4MgmtPooledAddrAddr=_CfprVnicIpV4MgmtPooledAddrAddr_Object((1,3,6,1,4,1,9,9,826,1,83,36,1,4),_CfprVnicIpV4MgmtPooledAddrAddr_Type())
cfprVnicIpV4MgmtPooledAddrAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIpV4MgmtPooledAddrAddr.setStatus(_A)
_CfprVnicIpV4MgmtPooledAddrDefGw_Type=InetAddressIPv4
_CfprVnicIpV4MgmtPooledAddrDefGw_Object=MibTableColumn
cfprVnicIpV4MgmtPooledAddrDefGw=_CfprVnicIpV4MgmtPooledAddrDefGw_Object((1,3,6,1,4,1,9,9,826,1,83,36,1,5),_CfprVnicIpV4MgmtPooledAddrDefGw_Type())
cfprVnicIpV4MgmtPooledAddrDefGw.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIpV4MgmtPooledAddrDefGw.setStatus(_A)
_CfprVnicIpV4MgmtPooledAddrName_Type=SnmpAdminString
_CfprVnicIpV4MgmtPooledAddrName_Object=MibTableColumn
cfprVnicIpV4MgmtPooledAddrName=_CfprVnicIpV4MgmtPooledAddrName_Object((1,3,6,1,4,1,9,9,826,1,83,36,1,6),_CfprVnicIpV4MgmtPooledAddrName_Type())
cfprVnicIpV4MgmtPooledAddrName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIpV4MgmtPooledAddrName.setStatus(_A)
_CfprVnicIpV4MgmtPooledAddrOperName_Type=SnmpAdminString
_CfprVnicIpV4MgmtPooledAddrOperName_Object=MibTableColumn
cfprVnicIpV4MgmtPooledAddrOperName=_CfprVnicIpV4MgmtPooledAddrOperName_Object((1,3,6,1,4,1,9,9,826,1,83,36,1,7),_CfprVnicIpV4MgmtPooledAddrOperName_Type())
cfprVnicIpV4MgmtPooledAddrOperName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIpV4MgmtPooledAddrOperName.setStatus(_A)
_CfprVnicIpV4MgmtPooledAddrPrimDns_Type=InetAddressIPv4
_CfprVnicIpV4MgmtPooledAddrPrimDns_Object=MibTableColumn
cfprVnicIpV4MgmtPooledAddrPrimDns=_CfprVnicIpV4MgmtPooledAddrPrimDns_Object((1,3,6,1,4,1,9,9,826,1,83,36,1,8),_CfprVnicIpV4MgmtPooledAddrPrimDns_Type())
cfprVnicIpV4MgmtPooledAddrPrimDns.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIpV4MgmtPooledAddrPrimDns.setStatus(_A)
_CfprVnicIpV4MgmtPooledAddrSecDns_Type=InetAddressIPv4
_CfprVnicIpV4MgmtPooledAddrSecDns_Object=MibTableColumn
cfprVnicIpV4MgmtPooledAddrSecDns=_CfprVnicIpV4MgmtPooledAddrSecDns_Object((1,3,6,1,4,1,9,9,826,1,83,36,1,9),_CfprVnicIpV4MgmtPooledAddrSecDns_Type())
cfprVnicIpV4MgmtPooledAddrSecDns.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIpV4MgmtPooledAddrSecDns.setStatus(_A)
_CfprVnicIpV4MgmtPooledAddrSubnet_Type=InetAddressIPv4
_CfprVnicIpV4MgmtPooledAddrSubnet_Object=MibTableColumn
cfprVnicIpV4MgmtPooledAddrSubnet=_CfprVnicIpV4MgmtPooledAddrSubnet_Object((1,3,6,1,4,1,9,9,826,1,83,36,1,10),_CfprVnicIpV4MgmtPooledAddrSubnet_Type())
cfprVnicIpV4MgmtPooledAddrSubnet.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIpV4MgmtPooledAddrSubnet.setStatus(_A)
_CfprVnicIpV4PooledAddrTable_Object=MibTable
cfprVnicIpV4PooledAddrTable=_CfprVnicIpV4PooledAddrTable_Object((1,3,6,1,4,1,9,9,826,1,83,37))
if mibBuilder.loadTexts:cfprVnicIpV4PooledAddrTable.setStatus(_A)
_CfprVnicIpV4PooledAddrEntry_Object=MibTableRow
cfprVnicIpV4PooledAddrEntry=_CfprVnicIpV4PooledAddrEntry_Object((1,3,6,1,4,1,9,9,826,1,83,37,1))
cfprVnicIpV4PooledAddrEntry.setIndexNames((0,_C,_o))
if mibBuilder.loadTexts:cfprVnicIpV4PooledAddrEntry.setStatus(_A)
_CfprVnicIpV4PooledAddrInstanceId_Type=CfprManagedObjectId
_CfprVnicIpV4PooledAddrInstanceId_Object=MibTableColumn
cfprVnicIpV4PooledAddrInstanceId=_CfprVnicIpV4PooledAddrInstanceId_Object((1,3,6,1,4,1,9,9,826,1,83,37,1,1),_CfprVnicIpV4PooledAddrInstanceId_Type())
cfprVnicIpV4PooledAddrInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprVnicIpV4PooledAddrInstanceId.setStatus(_A)
_CfprVnicIpV4PooledAddrDn_Type=CfprManagedObjectDn
_CfprVnicIpV4PooledAddrDn_Object=MibTableColumn
cfprVnicIpV4PooledAddrDn=_CfprVnicIpV4PooledAddrDn_Object((1,3,6,1,4,1,9,9,826,1,83,37,1,2),_CfprVnicIpV4PooledAddrDn_Type())
cfprVnicIpV4PooledAddrDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIpV4PooledAddrDn.setStatus(_A)
_CfprVnicIpV4PooledAddrRn_Type=SnmpAdminString
_CfprVnicIpV4PooledAddrRn_Object=MibTableColumn
cfprVnicIpV4PooledAddrRn=_CfprVnicIpV4PooledAddrRn_Object((1,3,6,1,4,1,9,9,826,1,83,37,1,3),_CfprVnicIpV4PooledAddrRn_Type())
cfprVnicIpV4PooledAddrRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIpV4PooledAddrRn.setStatus(_A)
_CfprVnicIpV4PooledAddrAddr_Type=InetAddressIPv4
_CfprVnicIpV4PooledAddrAddr_Object=MibTableColumn
cfprVnicIpV4PooledAddrAddr=_CfprVnicIpV4PooledAddrAddr_Object((1,3,6,1,4,1,9,9,826,1,83,37,1,4),_CfprVnicIpV4PooledAddrAddr_Type())
cfprVnicIpV4PooledAddrAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIpV4PooledAddrAddr.setStatus(_A)
_CfprVnicIpV4PooledAddrDefGw_Type=InetAddressIPv4
_CfprVnicIpV4PooledAddrDefGw_Object=MibTableColumn
cfprVnicIpV4PooledAddrDefGw=_CfprVnicIpV4PooledAddrDefGw_Object((1,3,6,1,4,1,9,9,826,1,83,37,1,5),_CfprVnicIpV4PooledAddrDefGw_Type())
cfprVnicIpV4PooledAddrDefGw.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIpV4PooledAddrDefGw.setStatus(_A)
_CfprVnicIpV4PooledAddrName_Type=SnmpAdminString
_CfprVnicIpV4PooledAddrName_Object=MibTableColumn
cfprVnicIpV4PooledAddrName=_CfprVnicIpV4PooledAddrName_Object((1,3,6,1,4,1,9,9,826,1,83,37,1,6),_CfprVnicIpV4PooledAddrName_Type())
cfprVnicIpV4PooledAddrName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIpV4PooledAddrName.setStatus(_A)
_CfprVnicIpV4PooledAddrOperName_Type=SnmpAdminString
_CfprVnicIpV4PooledAddrOperName_Object=MibTableColumn
cfprVnicIpV4PooledAddrOperName=_CfprVnicIpV4PooledAddrOperName_Object((1,3,6,1,4,1,9,9,826,1,83,37,1,7),_CfprVnicIpV4PooledAddrOperName_Type())
cfprVnicIpV4PooledAddrOperName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIpV4PooledAddrOperName.setStatus(_A)
_CfprVnicIpV4PooledAddrPrimDns_Type=InetAddressIPv4
_CfprVnicIpV4PooledAddrPrimDns_Object=MibTableColumn
cfprVnicIpV4PooledAddrPrimDns=_CfprVnicIpV4PooledAddrPrimDns_Object((1,3,6,1,4,1,9,9,826,1,83,37,1,8),_CfprVnicIpV4PooledAddrPrimDns_Type())
cfprVnicIpV4PooledAddrPrimDns.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIpV4PooledAddrPrimDns.setStatus(_A)
_CfprVnicIpV4PooledAddrSecDns_Type=InetAddressIPv4
_CfprVnicIpV4PooledAddrSecDns_Object=MibTableColumn
cfprVnicIpV4PooledAddrSecDns=_CfprVnicIpV4PooledAddrSecDns_Object((1,3,6,1,4,1,9,9,826,1,83,37,1,9),_CfprVnicIpV4PooledAddrSecDns_Type())
cfprVnicIpV4PooledAddrSecDns.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIpV4PooledAddrSecDns.setStatus(_A)
_CfprVnicIpV4PooledAddrSubnet_Type=InetAddressIPv4
_CfprVnicIpV4PooledAddrSubnet_Object=MibTableColumn
cfprVnicIpV4PooledAddrSubnet=_CfprVnicIpV4PooledAddrSubnet_Object((1,3,6,1,4,1,9,9,826,1,83,37,1,10),_CfprVnicIpV4PooledAddrSubnet_Type())
cfprVnicIpV4PooledAddrSubnet.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIpV4PooledAddrSubnet.setStatus(_A)
_CfprVnicIpV4ProfDerivedAddrTable_Object=MibTable
cfprVnicIpV4ProfDerivedAddrTable=_CfprVnicIpV4ProfDerivedAddrTable_Object((1,3,6,1,4,1,9,9,826,1,83,38))
if mibBuilder.loadTexts:cfprVnicIpV4ProfDerivedAddrTable.setStatus(_A)
_CfprVnicIpV4ProfDerivedAddrEntry_Object=MibTableRow
cfprVnicIpV4ProfDerivedAddrEntry=_CfprVnicIpV4ProfDerivedAddrEntry_Object((1,3,6,1,4,1,9,9,826,1,83,38,1))
cfprVnicIpV4ProfDerivedAddrEntry.setIndexNames((0,_C,_p))
if mibBuilder.loadTexts:cfprVnicIpV4ProfDerivedAddrEntry.setStatus(_A)
_CfprVnicIpV4ProfDerivedAddrInstanceId_Type=CfprManagedObjectId
_CfprVnicIpV4ProfDerivedAddrInstanceId_Object=MibTableColumn
cfprVnicIpV4ProfDerivedAddrInstanceId=_CfprVnicIpV4ProfDerivedAddrInstanceId_Object((1,3,6,1,4,1,9,9,826,1,83,38,1,1),_CfprVnicIpV4ProfDerivedAddrInstanceId_Type())
cfprVnicIpV4ProfDerivedAddrInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprVnicIpV4ProfDerivedAddrInstanceId.setStatus(_A)
_CfprVnicIpV4ProfDerivedAddrDn_Type=CfprManagedObjectDn
_CfprVnicIpV4ProfDerivedAddrDn_Object=MibTableColumn
cfprVnicIpV4ProfDerivedAddrDn=_CfprVnicIpV4ProfDerivedAddrDn_Object((1,3,6,1,4,1,9,9,826,1,83,38,1,2),_CfprVnicIpV4ProfDerivedAddrDn_Type())
cfprVnicIpV4ProfDerivedAddrDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIpV4ProfDerivedAddrDn.setStatus(_A)
_CfprVnicIpV4ProfDerivedAddrRn_Type=SnmpAdminString
_CfprVnicIpV4ProfDerivedAddrRn_Object=MibTableColumn
cfprVnicIpV4ProfDerivedAddrRn=_CfprVnicIpV4ProfDerivedAddrRn_Object((1,3,6,1,4,1,9,9,826,1,83,38,1,3),_CfprVnicIpV4ProfDerivedAddrRn_Type())
cfprVnicIpV4ProfDerivedAddrRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIpV4ProfDerivedAddrRn.setStatus(_A)
_CfprVnicIpV4ProfDerivedAddrAddr_Type=InetAddressIPv4
_CfprVnicIpV4ProfDerivedAddrAddr_Object=MibTableColumn
cfprVnicIpV4ProfDerivedAddrAddr=_CfprVnicIpV4ProfDerivedAddrAddr_Object((1,3,6,1,4,1,9,9,826,1,83,38,1,4),_CfprVnicIpV4ProfDerivedAddrAddr_Type())
cfprVnicIpV4ProfDerivedAddrAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIpV4ProfDerivedAddrAddr.setStatus(_A)
_CfprVnicIpV4ProfDerivedAddrDefGw_Type=InetAddressIPv4
_CfprVnicIpV4ProfDerivedAddrDefGw_Object=MibTableColumn
cfprVnicIpV4ProfDerivedAddrDefGw=_CfprVnicIpV4ProfDerivedAddrDefGw_Object((1,3,6,1,4,1,9,9,826,1,83,38,1,5),_CfprVnicIpV4ProfDerivedAddrDefGw_Type())
cfprVnicIpV4ProfDerivedAddrDefGw.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIpV4ProfDerivedAddrDefGw.setStatus(_A)
_CfprVnicIpV4ProfDerivedAddrSubnet_Type=InetAddressIPv4
_CfprVnicIpV4ProfDerivedAddrSubnet_Object=MibTableColumn
cfprVnicIpV4ProfDerivedAddrSubnet=_CfprVnicIpV4ProfDerivedAddrSubnet_Object((1,3,6,1,4,1,9,9,826,1,83,38,1,6),_CfprVnicIpV4ProfDerivedAddrSubnet_Type())
cfprVnicIpV4ProfDerivedAddrSubnet.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIpV4ProfDerivedAddrSubnet.setStatus(_A)
_CfprVnicIpV4StaticAddrTable_Object=MibTable
cfprVnicIpV4StaticAddrTable=_CfprVnicIpV4StaticAddrTable_Object((1,3,6,1,4,1,9,9,826,1,83,39))
if mibBuilder.loadTexts:cfprVnicIpV4StaticAddrTable.setStatus(_A)
_CfprVnicIpV4StaticAddrEntry_Object=MibTableRow
cfprVnicIpV4StaticAddrEntry=_CfprVnicIpV4StaticAddrEntry_Object((1,3,6,1,4,1,9,9,826,1,83,39,1))
cfprVnicIpV4StaticAddrEntry.setIndexNames((0,_C,_q))
if mibBuilder.loadTexts:cfprVnicIpV4StaticAddrEntry.setStatus(_A)
_CfprVnicIpV4StaticAddrInstanceId_Type=CfprManagedObjectId
_CfprVnicIpV4StaticAddrInstanceId_Object=MibTableColumn
cfprVnicIpV4StaticAddrInstanceId=_CfprVnicIpV4StaticAddrInstanceId_Object((1,3,6,1,4,1,9,9,826,1,83,39,1,1),_CfprVnicIpV4StaticAddrInstanceId_Type())
cfprVnicIpV4StaticAddrInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprVnicIpV4StaticAddrInstanceId.setStatus(_A)
_CfprVnicIpV4StaticAddrDn_Type=CfprManagedObjectDn
_CfprVnicIpV4StaticAddrDn_Object=MibTableColumn
cfprVnicIpV4StaticAddrDn=_CfprVnicIpV4StaticAddrDn_Object((1,3,6,1,4,1,9,9,826,1,83,39,1,2),_CfprVnicIpV4StaticAddrDn_Type())
cfprVnicIpV4StaticAddrDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIpV4StaticAddrDn.setStatus(_A)
_CfprVnicIpV4StaticAddrRn_Type=SnmpAdminString
_CfprVnicIpV4StaticAddrRn_Object=MibTableColumn
cfprVnicIpV4StaticAddrRn=_CfprVnicIpV4StaticAddrRn_Object((1,3,6,1,4,1,9,9,826,1,83,39,1,3),_CfprVnicIpV4StaticAddrRn_Type())
cfprVnicIpV4StaticAddrRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIpV4StaticAddrRn.setStatus(_A)
_CfprVnicIpV4StaticAddrAddr_Type=InetAddressIPv4
_CfprVnicIpV4StaticAddrAddr_Object=MibTableColumn
cfprVnicIpV4StaticAddrAddr=_CfprVnicIpV4StaticAddrAddr_Object((1,3,6,1,4,1,9,9,826,1,83,39,1,4),_CfprVnicIpV4StaticAddrAddr_Type())
cfprVnicIpV4StaticAddrAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIpV4StaticAddrAddr.setStatus(_A)
_CfprVnicIpV4StaticAddrDefGw_Type=InetAddressIPv4
_CfprVnicIpV4StaticAddrDefGw_Object=MibTableColumn
cfprVnicIpV4StaticAddrDefGw=_CfprVnicIpV4StaticAddrDefGw_Object((1,3,6,1,4,1,9,9,826,1,83,39,1,5),_CfprVnicIpV4StaticAddrDefGw_Type())
cfprVnicIpV4StaticAddrDefGw.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIpV4StaticAddrDefGw.setStatus(_A)
_CfprVnicIpV4StaticAddrPrimDns_Type=InetAddressIPv4
_CfprVnicIpV4StaticAddrPrimDns_Object=MibTableColumn
cfprVnicIpV4StaticAddrPrimDns=_CfprVnicIpV4StaticAddrPrimDns_Object((1,3,6,1,4,1,9,9,826,1,83,39,1,6),_CfprVnicIpV4StaticAddrPrimDns_Type())
cfprVnicIpV4StaticAddrPrimDns.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIpV4StaticAddrPrimDns.setStatus(_A)
_CfprVnicIpV4StaticAddrSecDns_Type=InetAddressIPv4
_CfprVnicIpV4StaticAddrSecDns_Object=MibTableColumn
cfprVnicIpV4StaticAddrSecDns=_CfprVnicIpV4StaticAddrSecDns_Object((1,3,6,1,4,1,9,9,826,1,83,39,1,7),_CfprVnicIpV4StaticAddrSecDns_Type())
cfprVnicIpV4StaticAddrSecDns.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIpV4StaticAddrSecDns.setStatus(_A)
_CfprVnicIpV4StaticAddrSubnet_Type=InetAddressIPv4
_CfprVnicIpV4StaticAddrSubnet_Object=MibTableColumn
cfprVnicIpV4StaticAddrSubnet=_CfprVnicIpV4StaticAddrSubnet_Object((1,3,6,1,4,1,9,9,826,1,83,39,1,8),_CfprVnicIpV4StaticAddrSubnet_Type())
cfprVnicIpV4StaticAddrSubnet.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIpV4StaticAddrSubnet.setStatus(_A)
_CfprVnicIpV6HistoryTable_Object=MibTable
cfprVnicIpV6HistoryTable=_CfprVnicIpV6HistoryTable_Object((1,3,6,1,4,1,9,9,826,1,83,40))
if mibBuilder.loadTexts:cfprVnicIpV6HistoryTable.setStatus(_A)
_CfprVnicIpV6HistoryEntry_Object=MibTableRow
cfprVnicIpV6HistoryEntry=_CfprVnicIpV6HistoryEntry_Object((1,3,6,1,4,1,9,9,826,1,83,40,1))
cfprVnicIpV6HistoryEntry.setIndexNames((0,_C,_r))
if mibBuilder.loadTexts:cfprVnicIpV6HistoryEntry.setStatus(_A)
_CfprVnicIpV6HistoryInstanceId_Type=CfprManagedObjectId
_CfprVnicIpV6HistoryInstanceId_Object=MibTableColumn
cfprVnicIpV6HistoryInstanceId=_CfprVnicIpV6HistoryInstanceId_Object((1,3,6,1,4,1,9,9,826,1,83,40,1,1),_CfprVnicIpV6HistoryInstanceId_Type())
cfprVnicIpV6HistoryInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprVnicIpV6HistoryInstanceId.setStatus(_A)
_CfprVnicIpV6HistoryDn_Type=CfprManagedObjectDn
_CfprVnicIpV6HistoryDn_Object=MibTableColumn
cfprVnicIpV6HistoryDn=_CfprVnicIpV6HistoryDn_Object((1,3,6,1,4,1,9,9,826,1,83,40,1,2),_CfprVnicIpV6HistoryDn_Type())
cfprVnicIpV6HistoryDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIpV6HistoryDn.setStatus(_A)
_CfprVnicIpV6HistoryRn_Type=SnmpAdminString
_CfprVnicIpV6HistoryRn_Object=MibTableColumn
cfprVnicIpV6HistoryRn=_CfprVnicIpV6HistoryRn_Object((1,3,6,1,4,1,9,9,826,1,83,40,1,3),_CfprVnicIpV6HistoryRn_Type())
cfprVnicIpV6HistoryRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIpV6HistoryRn.setStatus(_A)
_CfprVnicIpV6HistoryOldIpV6Addr_Type=InetAddressIPv6
_CfprVnicIpV6HistoryOldIpV6Addr_Object=MibTableColumn
cfprVnicIpV6HistoryOldIpV6Addr=_CfprVnicIpV6HistoryOldIpV6Addr_Object((1,3,6,1,4,1,9,9,826,1,83,40,1,4),_CfprVnicIpV6HistoryOldIpV6Addr_Type())
cfprVnicIpV6HistoryOldIpV6Addr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIpV6HistoryOldIpV6Addr.setStatus(_A)
_CfprVnicIpV6MgmtPooledAddrTable_Object=MibTable
cfprVnicIpV6MgmtPooledAddrTable=_CfprVnicIpV6MgmtPooledAddrTable_Object((1,3,6,1,4,1,9,9,826,1,83,41))
if mibBuilder.loadTexts:cfprVnicIpV6MgmtPooledAddrTable.setStatus(_A)
_CfprVnicIpV6MgmtPooledAddrEntry_Object=MibTableRow
cfprVnicIpV6MgmtPooledAddrEntry=_CfprVnicIpV6MgmtPooledAddrEntry_Object((1,3,6,1,4,1,9,9,826,1,83,41,1))
cfprVnicIpV6MgmtPooledAddrEntry.setIndexNames((0,_C,_s))
if mibBuilder.loadTexts:cfprVnicIpV6MgmtPooledAddrEntry.setStatus(_A)
_CfprVnicIpV6MgmtPooledAddrInstanceId_Type=CfprManagedObjectId
_CfprVnicIpV6MgmtPooledAddrInstanceId_Object=MibTableColumn
cfprVnicIpV6MgmtPooledAddrInstanceId=_CfprVnicIpV6MgmtPooledAddrInstanceId_Object((1,3,6,1,4,1,9,9,826,1,83,41,1,1),_CfprVnicIpV6MgmtPooledAddrInstanceId_Type())
cfprVnicIpV6MgmtPooledAddrInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprVnicIpV6MgmtPooledAddrInstanceId.setStatus(_A)
_CfprVnicIpV6MgmtPooledAddrDn_Type=CfprManagedObjectDn
_CfprVnicIpV6MgmtPooledAddrDn_Object=MibTableColumn
cfprVnicIpV6MgmtPooledAddrDn=_CfprVnicIpV6MgmtPooledAddrDn_Object((1,3,6,1,4,1,9,9,826,1,83,41,1,2),_CfprVnicIpV6MgmtPooledAddrDn_Type())
cfprVnicIpV6MgmtPooledAddrDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIpV6MgmtPooledAddrDn.setStatus(_A)
_CfprVnicIpV6MgmtPooledAddrRn_Type=SnmpAdminString
_CfprVnicIpV6MgmtPooledAddrRn_Object=MibTableColumn
cfprVnicIpV6MgmtPooledAddrRn=_CfprVnicIpV6MgmtPooledAddrRn_Object((1,3,6,1,4,1,9,9,826,1,83,41,1,3),_CfprVnicIpV6MgmtPooledAddrRn_Type())
cfprVnicIpV6MgmtPooledAddrRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIpV6MgmtPooledAddrRn.setStatus(_A)
_CfprVnicIpV6MgmtPooledAddrAddr_Type=InetAddressIPv6
_CfprVnicIpV6MgmtPooledAddrAddr_Object=MibTableColumn
cfprVnicIpV6MgmtPooledAddrAddr=_CfprVnicIpV6MgmtPooledAddrAddr_Object((1,3,6,1,4,1,9,9,826,1,83,41,1,4),_CfprVnicIpV6MgmtPooledAddrAddr_Type())
cfprVnicIpV6MgmtPooledAddrAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIpV6MgmtPooledAddrAddr.setStatus(_A)
_CfprVnicIpV6MgmtPooledAddrDefGw_Type=InetAddressIPv6
_CfprVnicIpV6MgmtPooledAddrDefGw_Object=MibTableColumn
cfprVnicIpV6MgmtPooledAddrDefGw=_CfprVnicIpV6MgmtPooledAddrDefGw_Object((1,3,6,1,4,1,9,9,826,1,83,41,1,5),_CfprVnicIpV6MgmtPooledAddrDefGw_Type())
cfprVnicIpV6MgmtPooledAddrDefGw.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIpV6MgmtPooledAddrDefGw.setStatus(_A)
_CfprVnicIpV6MgmtPooledAddrName_Type=SnmpAdminString
_CfprVnicIpV6MgmtPooledAddrName_Object=MibTableColumn
cfprVnicIpV6MgmtPooledAddrName=_CfprVnicIpV6MgmtPooledAddrName_Object((1,3,6,1,4,1,9,9,826,1,83,41,1,6),_CfprVnicIpV6MgmtPooledAddrName_Type())
cfprVnicIpV6MgmtPooledAddrName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIpV6MgmtPooledAddrName.setStatus(_A)
_CfprVnicIpV6MgmtPooledAddrOperName_Type=SnmpAdminString
_CfprVnicIpV6MgmtPooledAddrOperName_Object=MibTableColumn
cfprVnicIpV6MgmtPooledAddrOperName=_CfprVnicIpV6MgmtPooledAddrOperName_Object((1,3,6,1,4,1,9,9,826,1,83,41,1,7),_CfprVnicIpV6MgmtPooledAddrOperName_Type())
cfprVnicIpV6MgmtPooledAddrOperName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIpV6MgmtPooledAddrOperName.setStatus(_A)
_CfprVnicIpV6MgmtPooledAddrPrefix_Type=Gauge32
_CfprVnicIpV6MgmtPooledAddrPrefix_Object=MibTableColumn
cfprVnicIpV6MgmtPooledAddrPrefix=_CfprVnicIpV6MgmtPooledAddrPrefix_Object((1,3,6,1,4,1,9,9,826,1,83,41,1,8),_CfprVnicIpV6MgmtPooledAddrPrefix_Type())
cfprVnicIpV6MgmtPooledAddrPrefix.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIpV6MgmtPooledAddrPrefix.setStatus(_A)
_CfprVnicIpV6MgmtPooledAddrPrimDns_Type=InetAddressIPv6
_CfprVnicIpV6MgmtPooledAddrPrimDns_Object=MibTableColumn
cfprVnicIpV6MgmtPooledAddrPrimDns=_CfprVnicIpV6MgmtPooledAddrPrimDns_Object((1,3,6,1,4,1,9,9,826,1,83,41,1,9),_CfprVnicIpV6MgmtPooledAddrPrimDns_Type())
cfprVnicIpV6MgmtPooledAddrPrimDns.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIpV6MgmtPooledAddrPrimDns.setStatus(_A)
_CfprVnicIpV6MgmtPooledAddrSecDns_Type=InetAddressIPv6
_CfprVnicIpV6MgmtPooledAddrSecDns_Object=MibTableColumn
cfprVnicIpV6MgmtPooledAddrSecDns=_CfprVnicIpV6MgmtPooledAddrSecDns_Object((1,3,6,1,4,1,9,9,826,1,83,41,1,10),_CfprVnicIpV6MgmtPooledAddrSecDns_Type())
cfprVnicIpV6MgmtPooledAddrSecDns.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIpV6MgmtPooledAddrSecDns.setStatus(_A)
_CfprVnicIpV6StaticAddrTable_Object=MibTable
cfprVnicIpV6StaticAddrTable=_CfprVnicIpV6StaticAddrTable_Object((1,3,6,1,4,1,9,9,826,1,83,42))
if mibBuilder.loadTexts:cfprVnicIpV6StaticAddrTable.setStatus(_A)
_CfprVnicIpV6StaticAddrEntry_Object=MibTableRow
cfprVnicIpV6StaticAddrEntry=_CfprVnicIpV6StaticAddrEntry_Object((1,3,6,1,4,1,9,9,826,1,83,42,1))
cfprVnicIpV6StaticAddrEntry.setIndexNames((0,_C,_t))
if mibBuilder.loadTexts:cfprVnicIpV6StaticAddrEntry.setStatus(_A)
_CfprVnicIpV6StaticAddrInstanceId_Type=CfprManagedObjectId
_CfprVnicIpV6StaticAddrInstanceId_Object=MibTableColumn
cfprVnicIpV6StaticAddrInstanceId=_CfprVnicIpV6StaticAddrInstanceId_Object((1,3,6,1,4,1,9,9,826,1,83,42,1,1),_CfprVnicIpV6StaticAddrInstanceId_Type())
cfprVnicIpV6StaticAddrInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprVnicIpV6StaticAddrInstanceId.setStatus(_A)
_CfprVnicIpV6StaticAddrDn_Type=CfprManagedObjectDn
_CfprVnicIpV6StaticAddrDn_Object=MibTableColumn
cfprVnicIpV6StaticAddrDn=_CfprVnicIpV6StaticAddrDn_Object((1,3,6,1,4,1,9,9,826,1,83,42,1,2),_CfprVnicIpV6StaticAddrDn_Type())
cfprVnicIpV6StaticAddrDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIpV6StaticAddrDn.setStatus(_A)
_CfprVnicIpV6StaticAddrRn_Type=SnmpAdminString
_CfprVnicIpV6StaticAddrRn_Object=MibTableColumn
cfprVnicIpV6StaticAddrRn=_CfprVnicIpV6StaticAddrRn_Object((1,3,6,1,4,1,9,9,826,1,83,42,1,3),_CfprVnicIpV6StaticAddrRn_Type())
cfprVnicIpV6StaticAddrRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIpV6StaticAddrRn.setStatus(_A)
_CfprVnicIpV6StaticAddrAddr_Type=InetAddressIPv6
_CfprVnicIpV6StaticAddrAddr_Object=MibTableColumn
cfprVnicIpV6StaticAddrAddr=_CfprVnicIpV6StaticAddrAddr_Object((1,3,6,1,4,1,9,9,826,1,83,42,1,4),_CfprVnicIpV6StaticAddrAddr_Type())
cfprVnicIpV6StaticAddrAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIpV6StaticAddrAddr.setStatus(_A)
_CfprVnicIpV6StaticAddrDefGw_Type=InetAddressIPv6
_CfprVnicIpV6StaticAddrDefGw_Object=MibTableColumn
cfprVnicIpV6StaticAddrDefGw=_CfprVnicIpV6StaticAddrDefGw_Object((1,3,6,1,4,1,9,9,826,1,83,42,1,5),_CfprVnicIpV6StaticAddrDefGw_Type())
cfprVnicIpV6StaticAddrDefGw.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIpV6StaticAddrDefGw.setStatus(_A)
_CfprVnicIpV6StaticAddrPrefix_Type=Gauge32
_CfprVnicIpV6StaticAddrPrefix_Object=MibTableColumn
cfprVnicIpV6StaticAddrPrefix=_CfprVnicIpV6StaticAddrPrefix_Object((1,3,6,1,4,1,9,9,826,1,83,42,1,6),_CfprVnicIpV6StaticAddrPrefix_Type())
cfprVnicIpV6StaticAddrPrefix.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIpV6StaticAddrPrefix.setStatus(_A)
_CfprVnicIpV6StaticAddrPrimDns_Type=InetAddressIPv6
_CfprVnicIpV6StaticAddrPrimDns_Object=MibTableColumn
cfprVnicIpV6StaticAddrPrimDns=_CfprVnicIpV6StaticAddrPrimDns_Object((1,3,6,1,4,1,9,9,826,1,83,42,1,7),_CfprVnicIpV6StaticAddrPrimDns_Type())
cfprVnicIpV6StaticAddrPrimDns.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIpV6StaticAddrPrimDns.setStatus(_A)
_CfprVnicIpV6StaticAddrSecDns_Type=InetAddressIPv6
_CfprVnicIpV6StaticAddrSecDns_Object=MibTableColumn
cfprVnicIpV6StaticAddrSecDns=_CfprVnicIpV6StaticAddrSecDns_Object((1,3,6,1,4,1,9,9,826,1,83,42,1,8),_CfprVnicIpV6StaticAddrSecDns_Type())
cfprVnicIpV6StaticAddrSecDns.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIpV6StaticAddrSecDns.setStatus(_A)
_CfprVnicIpcTable_Object=MibTable
cfprVnicIpcTable=_CfprVnicIpcTable_Object((1,3,6,1,4,1,9,9,826,1,83,43))
if mibBuilder.loadTexts:cfprVnicIpcTable.setStatus(_A)
_CfprVnicIpcEntry_Object=MibTableRow
cfprVnicIpcEntry=_CfprVnicIpcEntry_Object((1,3,6,1,4,1,9,9,826,1,83,43,1))
cfprVnicIpcEntry.setIndexNames((0,_C,_u))
if mibBuilder.loadTexts:cfprVnicIpcEntry.setStatus(_A)
_CfprVnicIpcInstanceId_Type=CfprManagedObjectId
_CfprVnicIpcInstanceId_Object=MibTableColumn
cfprVnicIpcInstanceId=_CfprVnicIpcInstanceId_Object((1,3,6,1,4,1,9,9,826,1,83,43,1,1),_CfprVnicIpcInstanceId_Type())
cfprVnicIpcInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprVnicIpcInstanceId.setStatus(_A)
_CfprVnicIpcDn_Type=CfprManagedObjectDn
_CfprVnicIpcDn_Object=MibTableColumn
cfprVnicIpcDn=_CfprVnicIpcDn_Object((1,3,6,1,4,1,9,9,826,1,83,43,1,2),_CfprVnicIpcDn_Type())
cfprVnicIpcDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIpcDn.setStatus(_A)
_CfprVnicIpcRn_Type=SnmpAdminString
_CfprVnicIpcRn_Object=MibTableColumn
cfprVnicIpcRn=_CfprVnicIpcRn_Object((1,3,6,1,4,1,9,9,826,1,83,43,1,3),_CfprVnicIpcRn_Type())
cfprVnicIpcRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIpcRn.setStatus(_A)
_CfprVnicIpcAdaptorProfileName_Type=SnmpAdminString
_CfprVnicIpcAdaptorProfileName_Object=MibTableColumn
cfprVnicIpcAdaptorProfileName=_CfprVnicIpcAdaptorProfileName_Object((1,3,6,1,4,1,9,9,826,1,83,43,1,4),_CfprVnicIpcAdaptorProfileName_Type())
cfprVnicIpcAdaptorProfileName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIpcAdaptorProfileName.setStatus(_A)
_CfprVnicIpcAddr_Type=MacAddress
_CfprVnicIpcAddr_Object=MibTableColumn
cfprVnicIpcAddr=_CfprVnicIpcAddr_Object((1,3,6,1,4,1,9,9,826,1,83,43,1,5),_CfprVnicIpcAddr_Type())
cfprVnicIpcAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIpcAddr.setStatus(_A)
_CfprVnicIpcAdminHostPort_Type=CfprFabricHostPortId
_CfprVnicIpcAdminHostPort_Object=MibTableColumn
cfprVnicIpcAdminHostPort=_CfprVnicIpcAdminHostPort_Object((1,3,6,1,4,1,9,9,826,1,83,43,1,6),_CfprVnicIpcAdminHostPort_Type())
cfprVnicIpcAdminHostPort.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIpcAdminHostPort.setStatus(_A)
_CfprVnicIpcAdminVcon_Type=SnmpAdminString
_CfprVnicIpcAdminVcon_Object=MibTableColumn
cfprVnicIpcAdminVcon=_CfprVnicIpcAdminVcon_Object((1,3,6,1,4,1,9,9,826,1,83,43,1,7),_CfprVnicIpcAdminVcon_Type())
cfprVnicIpcAdminVcon.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIpcAdminVcon.setStatus(_A)
_CfprVnicIpcAppRole_Type=CfprVnicAppRole
_CfprVnicIpcAppRole_Object=MibTableColumn
cfprVnicIpcAppRole=_CfprVnicIpcAppRole_Object((1,3,6,1,4,1,9,9,826,1,83,43,1,8),_CfprVnicIpcAppRole_Type())
cfprVnicIpcAppRole.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIpcAppRole.setStatus(_A)
_CfprVnicIpcBootDev_Type=CfprVnicVnicBootDev
_CfprVnicIpcBootDev_Object=MibTableColumn
cfprVnicIpcBootDev=_CfprVnicIpcBootDev_Object((1,3,6,1,4,1,9,9,826,1,83,43,1,9),_CfprVnicIpcBootDev_Type())
cfprVnicIpcBootDev.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIpcBootDev.setStatus(_A)
_CfprVnicIpcConfigQualifier_Type=CfprVnicConfigIssues
_CfprVnicIpcConfigQualifier_Object=MibTableColumn
cfprVnicIpcConfigQualifier=_CfprVnicIpcConfigQualifier_Object((1,3,6,1,4,1,9,9,826,1,83,43,1,10),_CfprVnicIpcConfigQualifier_Type())
cfprVnicIpcConfigQualifier.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIpcConfigQualifier.setStatus(_A)
_CfprVnicIpcConfigState_Type=CfprLsConfigState
_CfprVnicIpcConfigState_Object=MibTableColumn
cfprVnicIpcConfigState=_CfprVnicIpcConfigState_Object((1,3,6,1,4,1,9,9,826,1,83,43,1,11),_CfprVnicIpcConfigState_Type())
cfprVnicIpcConfigState.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIpcConfigState.setStatus(_A)
_CfprVnicIpcEquipmentDn_Type=SnmpAdminString
_CfprVnicIpcEquipmentDn_Object=MibTableColumn
cfprVnicIpcEquipmentDn=_CfprVnicIpcEquipmentDn_Object((1,3,6,1,4,1,9,9,826,1,83,43,1,12),_CfprVnicIpcEquipmentDn_Type())
cfprVnicIpcEquipmentDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIpcEquipmentDn.setStatus(_A)
_CfprVnicIpcIdentPoolName_Type=SnmpAdminString
_CfprVnicIpcIdentPoolName_Object=MibTableColumn
cfprVnicIpcIdentPoolName=_CfprVnicIpcIdentPoolName_Object((1,3,6,1,4,1,9,9,826,1,83,43,1,13),_CfprVnicIpcIdentPoolName_Type())
cfprVnicIpcIdentPoolName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIpcIdentPoolName.setStatus(_A)
_CfprVnicIpcInstType_Type=CfprVnicInstantiation
_CfprVnicIpcInstType_Object=MibTableColumn
cfprVnicIpcInstType=_CfprVnicIpcInstType_Object((1,3,6,1,4,1,9,9,826,1,83,43,1,14),_CfprVnicIpcInstType_Type())
cfprVnicIpcInstType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIpcInstType.setStatus(_A)
_CfprVnicIpcMtu_Type=Gauge32
_CfprVnicIpcMtu_Object=MibTableColumn
cfprVnicIpcMtu=_CfprVnicIpcMtu_Object((1,3,6,1,4,1,9,9,826,1,83,43,1,15),_CfprVnicIpcMtu_Type())
cfprVnicIpcMtu.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIpcMtu.setStatus(_A)
_CfprVnicIpcName_Type=SnmpAdminString
_CfprVnicIpcName_Object=MibTableColumn
cfprVnicIpcName=_CfprVnicIpcName_Object((1,3,6,1,4,1,9,9,826,1,83,43,1,16),_CfprVnicIpcName_Type())
cfprVnicIpcName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIpcName.setStatus(_A)
_CfprVnicIpcNwCtrlPolicyName_Type=SnmpAdminString
_CfprVnicIpcNwCtrlPolicyName_Object=MibTableColumn
cfprVnicIpcNwCtrlPolicyName=_CfprVnicIpcNwCtrlPolicyName_Object((1,3,6,1,4,1,9,9,826,1,83,43,1,17),_CfprVnicIpcNwCtrlPolicyName_Type())
cfprVnicIpcNwCtrlPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIpcNwCtrlPolicyName.setStatus(_A)
_CfprVnicIpcNwTemplName_Type=SnmpAdminString
_CfprVnicIpcNwTemplName_Object=MibTableColumn
cfprVnicIpcNwTemplName=_CfprVnicIpcNwTemplName_Object((1,3,6,1,4,1,9,9,826,1,83,43,1,18),_CfprVnicIpcNwTemplName_Type())
cfprVnicIpcNwTemplName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIpcNwTemplName.setStatus(_A)
_CfprVnicIpcOperAdaptorProfileName_Type=SnmpAdminString
_CfprVnicIpcOperAdaptorProfileName_Object=MibTableColumn
cfprVnicIpcOperAdaptorProfileName=_CfprVnicIpcOperAdaptorProfileName_Object((1,3,6,1,4,1,9,9,826,1,83,43,1,19),_CfprVnicIpcOperAdaptorProfileName_Type())
cfprVnicIpcOperAdaptorProfileName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIpcOperAdaptorProfileName.setStatus(_A)
_CfprVnicIpcOperHostPort_Type=CfprVnicVnicOperHostPort
_CfprVnicIpcOperHostPort_Object=MibTableColumn
cfprVnicIpcOperHostPort=_CfprVnicIpcOperHostPort_Object((1,3,6,1,4,1,9,9,826,1,83,43,1,20),_CfprVnicIpcOperHostPort_Type())
cfprVnicIpcOperHostPort.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIpcOperHostPort.setStatus(_A)
_CfprVnicIpcOperIdentPoolName_Type=SnmpAdminString
_CfprVnicIpcOperIdentPoolName_Object=MibTableColumn
cfprVnicIpcOperIdentPoolName=_CfprVnicIpcOperIdentPoolName_Object((1,3,6,1,4,1,9,9,826,1,83,43,1,21),_CfprVnicIpcOperIdentPoolName_Type())
cfprVnicIpcOperIdentPoolName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIpcOperIdentPoolName.setStatus(_A)
_CfprVnicIpcOperNwCtrlPolicyName_Type=SnmpAdminString
_CfprVnicIpcOperNwCtrlPolicyName_Object=MibTableColumn
cfprVnicIpcOperNwCtrlPolicyName=_CfprVnicIpcOperNwCtrlPolicyName_Object((1,3,6,1,4,1,9,9,826,1,83,43,1,22),_CfprVnicIpcOperNwCtrlPolicyName_Type())
cfprVnicIpcOperNwCtrlPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIpcOperNwCtrlPolicyName.setStatus(_A)
_CfprVnicIpcOperNwTemplName_Type=SnmpAdminString
_CfprVnicIpcOperNwTemplName_Object=MibTableColumn
cfprVnicIpcOperNwTemplName=_CfprVnicIpcOperNwTemplName_Object((1,3,6,1,4,1,9,9,826,1,83,43,1,23),_CfprVnicIpcOperNwTemplName_Type())
cfprVnicIpcOperNwTemplName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIpcOperNwTemplName.setStatus(_A)
_CfprVnicIpcOperOrder_Type=Gauge32
_CfprVnicIpcOperOrder_Object=MibTableColumn
cfprVnicIpcOperOrder=_CfprVnicIpcOperOrder_Object((1,3,6,1,4,1,9,9,826,1,83,43,1,24),_CfprVnicIpcOperOrder_Type())
cfprVnicIpcOperOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIpcOperOrder.setStatus(_A)
_CfprVnicIpcOperPinToGroupName_Type=SnmpAdminString
_CfprVnicIpcOperPinToGroupName_Object=MibTableColumn
cfprVnicIpcOperPinToGroupName=_CfprVnicIpcOperPinToGroupName_Object((1,3,6,1,4,1,9,9,826,1,83,43,1,25),_CfprVnicIpcOperPinToGroupName_Type())
cfprVnicIpcOperPinToGroupName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIpcOperPinToGroupName.setStatus(_A)
_CfprVnicIpcOperQosPolicyName_Type=SnmpAdminString
_CfprVnicIpcOperQosPolicyName_Object=MibTableColumn
cfprVnicIpcOperQosPolicyName=_CfprVnicIpcOperQosPolicyName_Object((1,3,6,1,4,1,9,9,826,1,83,43,1,26),_CfprVnicIpcOperQosPolicyName_Type())
cfprVnicIpcOperQosPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIpcOperQosPolicyName.setStatus(_A)
_CfprVnicIpcOperSpeed_Type=Gauge32
_CfprVnicIpcOperSpeed_Object=MibTableColumn
cfprVnicIpcOperSpeed=_CfprVnicIpcOperSpeed_Object((1,3,6,1,4,1,9,9,826,1,83,43,1,27),_CfprVnicIpcOperSpeed_Type())
cfprVnicIpcOperSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIpcOperSpeed.setStatus(_A)
_CfprVnicIpcOperStatsPolicyName_Type=SnmpAdminString
_CfprVnicIpcOperStatsPolicyName_Object=MibTableColumn
cfprVnicIpcOperStatsPolicyName=_CfprVnicIpcOperStatsPolicyName_Object((1,3,6,1,4,1,9,9,826,1,83,43,1,28),_CfprVnicIpcOperStatsPolicyName_Type())
cfprVnicIpcOperStatsPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIpcOperStatsPolicyName.setStatus(_A)
_CfprVnicIpcOperVcon_Type=SnmpAdminString
_CfprVnicIpcOperVcon_Object=MibTableColumn
cfprVnicIpcOperVcon=_CfprVnicIpcOperVcon_Object((1,3,6,1,4,1,9,9,826,1,83,43,1,29),_CfprVnicIpcOperVcon_Type())
cfprVnicIpcOperVcon.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIpcOperVcon.setStatus(_A)
_CfprVnicIpcOrder_Type=Gauge32
_CfprVnicIpcOrder_Object=MibTableColumn
cfprVnicIpcOrder=_CfprVnicIpcOrder_Object((1,3,6,1,4,1,9,9,826,1,83,43,1,30),_CfprVnicIpcOrder_Type())
cfprVnicIpcOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIpcOrder.setStatus(_A)
_CfprVnicIpcOwner_Type=CfprVnicConnectionOwner
_CfprVnicIpcOwner_Object=MibTableColumn
cfprVnicIpcOwner=_CfprVnicIpcOwner_Object((1,3,6,1,4,1,9,9,826,1,83,43,1,31),_CfprVnicIpcOwner_Type())
cfprVnicIpcOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIpcOwner.setStatus(_A)
_CfprVnicIpcPinToGroupName_Type=SnmpAdminString
_CfprVnicIpcPinToGroupName_Object=MibTableColumn
cfprVnicIpcPinToGroupName=_CfprVnicIpcPinToGroupName_Object((1,3,6,1,4,1,9,9,826,1,83,43,1,32),_CfprVnicIpcPinToGroupName_Type())
cfprVnicIpcPinToGroupName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIpcPinToGroupName.setStatus(_A)
_CfprVnicIpcQosPolicyName_Type=SnmpAdminString
_CfprVnicIpcQosPolicyName_Object=MibTableColumn
cfprVnicIpcQosPolicyName=_CfprVnicIpcQosPolicyName_Object((1,3,6,1,4,1,9,9,826,1,83,43,1,33),_CfprVnicIpcQosPolicyName_Type())
cfprVnicIpcQosPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIpcQosPolicyName.setStatus(_A)
_CfprVnicIpcStatsPolicyName_Type=SnmpAdminString
_CfprVnicIpcStatsPolicyName_Object=MibTableColumn
cfprVnicIpcStatsPolicyName=_CfprVnicIpcStatsPolicyName_Object((1,3,6,1,4,1,9,9,826,1,83,43,1,34),_CfprVnicIpcStatsPolicyName_Type())
cfprVnicIpcStatsPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIpcStatsPolicyName.setStatus(_A)
_CfprVnicIpcSwitchId_Type=CfprVnicEtherBaseSwitchId
_CfprVnicIpcSwitchId_Object=MibTableColumn
cfprVnicIpcSwitchId=_CfprVnicIpcSwitchId_Object((1,3,6,1,4,1,9,9,826,1,83,43,1,35),_CfprVnicIpcSwitchId_Type())
cfprVnicIpcSwitchId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIpcSwitchId.setStatus(_A)
_CfprVnicIpcType_Type=CfprVnicIpcType
_CfprVnicIpcType_Object=MibTableColumn
cfprVnicIpcType=_CfprVnicIpcType_Object((1,3,6,1,4,1,9,9,826,1,83,43,1,36),_CfprVnicIpcType_Type())
cfprVnicIpcType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIpcType.setStatus(_A)
_CfprVnicIpcIfTable_Object=MibTable
cfprVnicIpcIfTable=_CfprVnicIpcIfTable_Object((1,3,6,1,4,1,9,9,826,1,83,44))
if mibBuilder.loadTexts:cfprVnicIpcIfTable.setStatus(_A)
_CfprVnicIpcIfEntry_Object=MibTableRow
cfprVnicIpcIfEntry=_CfprVnicIpcIfEntry_Object((1,3,6,1,4,1,9,9,826,1,83,44,1))
cfprVnicIpcIfEntry.setIndexNames((0,_C,_v))
if mibBuilder.loadTexts:cfprVnicIpcIfEntry.setStatus(_A)
_CfprVnicIpcIfInstanceId_Type=CfprManagedObjectId
_CfprVnicIpcIfInstanceId_Object=MibTableColumn
cfprVnicIpcIfInstanceId=_CfprVnicIpcIfInstanceId_Object((1,3,6,1,4,1,9,9,826,1,83,44,1,1),_CfprVnicIpcIfInstanceId_Type())
cfprVnicIpcIfInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprVnicIpcIfInstanceId.setStatus(_A)
_CfprVnicIpcIfDn_Type=CfprManagedObjectDn
_CfprVnicIpcIfDn_Object=MibTableColumn
cfprVnicIpcIfDn=_CfprVnicIpcIfDn_Object((1,3,6,1,4,1,9,9,826,1,83,44,1,2),_CfprVnicIpcIfDn_Type())
cfprVnicIpcIfDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIpcIfDn.setStatus(_A)
_CfprVnicIpcIfRn_Type=SnmpAdminString
_CfprVnicIpcIfRn_Object=MibTableColumn
cfprVnicIpcIfRn=_CfprVnicIpcIfRn_Object((1,3,6,1,4,1,9,9,826,1,83,44,1,3),_CfprVnicIpcIfRn_Type())
cfprVnicIpcIfRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIpcIfRn.setStatus(_A)
_CfprVnicIpcIfAddr_Type=MacAddress
_CfprVnicIpcIfAddr_Object=MibTableColumn
cfprVnicIpcIfAddr=_CfprVnicIpcIfAddr_Object((1,3,6,1,4,1,9,9,826,1,83,44,1,4),_CfprVnicIpcIfAddr_Type())
cfprVnicIpcIfAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIpcIfAddr.setStatus(_A)
_CfprVnicIpcIfConfigQualifier_Type=CfprVnicConfigIssues
_CfprVnicIpcIfConfigQualifier_Object=MibTableColumn
cfprVnicIpcIfConfigQualifier=_CfprVnicIpcIfConfigQualifier_Object((1,3,6,1,4,1,9,9,826,1,83,44,1,5),_CfprVnicIpcIfConfigQualifier_Type())
cfprVnicIpcIfConfigQualifier.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIpcIfConfigQualifier.setStatus(_A)
_CfprVnicIpcIfDefaultNet_Type=TruthValue
_CfprVnicIpcIfDefaultNet_Object=MibTableColumn
cfprVnicIpcIfDefaultNet=_CfprVnicIpcIfDefaultNet_Object((1,3,6,1,4,1,9,9,826,1,83,44,1,6),_CfprVnicIpcIfDefaultNet_Type())
cfprVnicIpcIfDefaultNet.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIpcIfDefaultNet.setStatus(_A)
_CfprVnicIpcIfName_Type=SnmpAdminString
_CfprVnicIpcIfName_Object=MibTableColumn
cfprVnicIpcIfName=_CfprVnicIpcIfName_Object((1,3,6,1,4,1,9,9,826,1,83,44,1,7),_CfprVnicIpcIfName_Type())
cfprVnicIpcIfName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIpcIfName.setStatus(_A)
_CfprVnicIpcIfOperState_Type=CfprVnicIfOperState
_CfprVnicIpcIfOperState_Object=MibTableColumn
cfprVnicIpcIfOperState=_CfprVnicIpcIfOperState_Object((1,3,6,1,4,1,9,9,826,1,83,44,1,8),_CfprVnicIpcIfOperState_Type())
cfprVnicIpcIfOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIpcIfOperState.setStatus(_A)
_CfprVnicIpcIfOperVnetDn_Type=SnmpAdminString
_CfprVnicIpcIfOperVnetDn_Object=MibTableColumn
cfprVnicIpcIfOperVnetDn=_CfprVnicIpcIfOperVnetDn_Object((1,3,6,1,4,1,9,9,826,1,83,44,1,9),_CfprVnicIpcIfOperVnetDn_Type())
cfprVnicIpcIfOperVnetDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIpcIfOperVnetDn.setStatus(_A)
_CfprVnicIpcIfOperVnetName_Type=SnmpAdminString
_CfprVnicIpcIfOperVnetName_Object=MibTableColumn
cfprVnicIpcIfOperVnetName=_CfprVnicIpcIfOperVnetName_Object((1,3,6,1,4,1,9,9,826,1,83,44,1,10),_CfprVnicIpcIfOperVnetName_Type())
cfprVnicIpcIfOperVnetName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIpcIfOperVnetName.setStatus(_A)
_CfprVnicIpcIfOwner_Type=CfprVnicConnectionOwner
_CfprVnicIpcIfOwner_Object=MibTableColumn
cfprVnicIpcIfOwner=_CfprVnicIpcIfOwner_Object((1,3,6,1,4,1,9,9,826,1,83,44,1,11),_CfprVnicIpcIfOwner_Type())
cfprVnicIpcIfOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIpcIfOwner.setStatus(_A)
_CfprVnicIpcIfPubNwId_Type=Gauge32
_CfprVnicIpcIfPubNwId_Object=MibTableColumn
cfprVnicIpcIfPubNwId=_CfprVnicIpcIfPubNwId_Object((1,3,6,1,4,1,9,9,826,1,83,44,1,12),_CfprVnicIpcIfPubNwId_Type())
cfprVnicIpcIfPubNwId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIpcIfPubNwId.setStatus(_A)
_CfprVnicIpcIfSharing_Type=CfprFabricVlanSharingType
_CfprVnicIpcIfSharing_Object=MibTableColumn
cfprVnicIpcIfSharing=_CfprVnicIpcIfSharing_Object((1,3,6,1,4,1,9,9,826,1,83,44,1,13),_CfprVnicIpcIfSharing_Type())
cfprVnicIpcIfSharing.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIpcIfSharing.setStatus(_A)
_CfprVnicIpcIfSwitchId_Type=CfprVnicL2IfSwitchId
_CfprVnicIpcIfSwitchId_Object=MibTableColumn
cfprVnicIpcIfSwitchId=_CfprVnicIpcIfSwitchId_Object((1,3,6,1,4,1,9,9,826,1,83,44,1,14),_CfprVnicIpcIfSwitchId_Type())
cfprVnicIpcIfSwitchId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIpcIfSwitchId.setStatus(_A)
_CfprVnicIpcIfType_Type=CfprVnicAIpcIfType
_CfprVnicIpcIfType_Object=MibTableColumn
cfprVnicIpcIfType=_CfprVnicIpcIfType_Object((1,3,6,1,4,1,9,9,826,1,83,44,1,15),_CfprVnicIpcIfType_Type())
cfprVnicIpcIfType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIpcIfType.setStatus(_A)
_CfprVnicIpcIfVnet_Type=Gauge32
_CfprVnicIpcIfVnet_Object=MibTableColumn
cfprVnicIpcIfVnet=_CfprVnicIpcIfVnet_Object((1,3,6,1,4,1,9,9,826,1,83,44,1,16),_CfprVnicIpcIfVnet_Type())
cfprVnicIpcIfVnet.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIpcIfVnet.setStatus(_A)
_CfprVnicIqnHistoryTable_Object=MibTable
cfprVnicIqnHistoryTable=_CfprVnicIqnHistoryTable_Object((1,3,6,1,4,1,9,9,826,1,83,45))
if mibBuilder.loadTexts:cfprVnicIqnHistoryTable.setStatus(_A)
_CfprVnicIqnHistoryEntry_Object=MibTableRow
cfprVnicIqnHistoryEntry=_CfprVnicIqnHistoryEntry_Object((1,3,6,1,4,1,9,9,826,1,83,45,1))
cfprVnicIqnHistoryEntry.setIndexNames((0,_C,_w))
if mibBuilder.loadTexts:cfprVnicIqnHistoryEntry.setStatus(_A)
_CfprVnicIqnHistoryInstanceId_Type=CfprManagedObjectId
_CfprVnicIqnHistoryInstanceId_Object=MibTableColumn
cfprVnicIqnHistoryInstanceId=_CfprVnicIqnHistoryInstanceId_Object((1,3,6,1,4,1,9,9,826,1,83,45,1,1),_CfprVnicIqnHistoryInstanceId_Type())
cfprVnicIqnHistoryInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprVnicIqnHistoryInstanceId.setStatus(_A)
_CfprVnicIqnHistoryDn_Type=CfprManagedObjectDn
_CfprVnicIqnHistoryDn_Object=MibTableColumn
cfprVnicIqnHistoryDn=_CfprVnicIqnHistoryDn_Object((1,3,6,1,4,1,9,9,826,1,83,45,1,2),_CfprVnicIqnHistoryDn_Type())
cfprVnicIqnHistoryDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIqnHistoryDn.setStatus(_A)
_CfprVnicIqnHistoryRn_Type=SnmpAdminString
_CfprVnicIqnHistoryRn_Object=MibTableColumn
cfprVnicIqnHistoryRn=_CfprVnicIqnHistoryRn_Object((1,3,6,1,4,1,9,9,826,1,83,45,1,3),_CfprVnicIqnHistoryRn_Type())
cfprVnicIqnHistoryRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIqnHistoryRn.setStatus(_A)
_CfprVnicIqnHistoryOldInitiatorName_Type=SnmpAdminString
_CfprVnicIqnHistoryOldInitiatorName_Object=MibTableColumn
cfprVnicIqnHistoryOldInitiatorName=_CfprVnicIqnHistoryOldInitiatorName_Object((1,3,6,1,4,1,9,9,826,1,83,45,1,4),_CfprVnicIqnHistoryOldInitiatorName_Type())
cfprVnicIqnHistoryOldInitiatorName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicIqnHistoryOldInitiatorName.setStatus(_A)
_CfprVnicLanConnPolicyTable_Object=MibTable
cfprVnicLanConnPolicyTable=_CfprVnicLanConnPolicyTable_Object((1,3,6,1,4,1,9,9,826,1,83,46))
if mibBuilder.loadTexts:cfprVnicLanConnPolicyTable.setStatus(_A)
_CfprVnicLanConnPolicyEntry_Object=MibTableRow
cfprVnicLanConnPolicyEntry=_CfprVnicLanConnPolicyEntry_Object((1,3,6,1,4,1,9,9,826,1,83,46,1))
cfprVnicLanConnPolicyEntry.setIndexNames((0,_C,_x))
if mibBuilder.loadTexts:cfprVnicLanConnPolicyEntry.setStatus(_A)
_CfprVnicLanConnPolicyInstanceId_Type=CfprManagedObjectId
_CfprVnicLanConnPolicyInstanceId_Object=MibTableColumn
cfprVnicLanConnPolicyInstanceId=_CfprVnicLanConnPolicyInstanceId_Object((1,3,6,1,4,1,9,9,826,1,83,46,1,1),_CfprVnicLanConnPolicyInstanceId_Type())
cfprVnicLanConnPolicyInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprVnicLanConnPolicyInstanceId.setStatus(_A)
_CfprVnicLanConnPolicyDn_Type=CfprManagedObjectDn
_CfprVnicLanConnPolicyDn_Object=MibTableColumn
cfprVnicLanConnPolicyDn=_CfprVnicLanConnPolicyDn_Object((1,3,6,1,4,1,9,9,826,1,83,46,1,2),_CfprVnicLanConnPolicyDn_Type())
cfprVnicLanConnPolicyDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicLanConnPolicyDn.setStatus(_A)
_CfprVnicLanConnPolicyRn_Type=SnmpAdminString
_CfprVnicLanConnPolicyRn_Object=MibTableColumn
cfprVnicLanConnPolicyRn=_CfprVnicLanConnPolicyRn_Object((1,3,6,1,4,1,9,9,826,1,83,46,1,3),_CfprVnicLanConnPolicyRn_Type())
cfprVnicLanConnPolicyRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicLanConnPolicyRn.setStatus(_A)
_CfprVnicLanConnPolicyDescr_Type=SnmpAdminString
_CfprVnicLanConnPolicyDescr_Object=MibTableColumn
cfprVnicLanConnPolicyDescr=_CfprVnicLanConnPolicyDescr_Object((1,3,6,1,4,1,9,9,826,1,83,46,1,4),_CfprVnicLanConnPolicyDescr_Type())
cfprVnicLanConnPolicyDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicLanConnPolicyDescr.setStatus(_A)
_CfprVnicLanConnPolicyFltAggr_Type=Unsigned64
_CfprVnicLanConnPolicyFltAggr_Object=MibTableColumn
cfprVnicLanConnPolicyFltAggr=_CfprVnicLanConnPolicyFltAggr_Object((1,3,6,1,4,1,9,9,826,1,83,46,1,5),_CfprVnicLanConnPolicyFltAggr_Type())
cfprVnicLanConnPolicyFltAggr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicLanConnPolicyFltAggr.setStatus(_A)
_CfprVnicLanConnPolicyIntId_Type=SnmpAdminString
_CfprVnicLanConnPolicyIntId_Object=MibTableColumn
cfprVnicLanConnPolicyIntId=_CfprVnicLanConnPolicyIntId_Object((1,3,6,1,4,1,9,9,826,1,83,46,1,6),_CfprVnicLanConnPolicyIntId_Type())
cfprVnicLanConnPolicyIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicLanConnPolicyIntId.setStatus(_A)
_CfprVnicLanConnPolicyName_Type=SnmpAdminString
_CfprVnicLanConnPolicyName_Object=MibTableColumn
cfprVnicLanConnPolicyName=_CfprVnicLanConnPolicyName_Object((1,3,6,1,4,1,9,9,826,1,83,46,1,7),_CfprVnicLanConnPolicyName_Type())
cfprVnicLanConnPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicLanConnPolicyName.setStatus(_A)
_CfprVnicLanConnPolicyPolicyLevel_Type=Gauge32
_CfprVnicLanConnPolicyPolicyLevel_Object=MibTableColumn
cfprVnicLanConnPolicyPolicyLevel=_CfprVnicLanConnPolicyPolicyLevel_Object((1,3,6,1,4,1,9,9,826,1,83,46,1,8),_CfprVnicLanConnPolicyPolicyLevel_Type())
cfprVnicLanConnPolicyPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicLanConnPolicyPolicyLevel.setStatus(_A)
_CfprVnicLanConnPolicyPolicyOwner_Type=CfprPolicyPolicyOwner
_CfprVnicLanConnPolicyPolicyOwner_Object=MibTableColumn
cfprVnicLanConnPolicyPolicyOwner=_CfprVnicLanConnPolicyPolicyOwner_Object((1,3,6,1,4,1,9,9,826,1,83,46,1,9),_CfprVnicLanConnPolicyPolicyOwner_Type())
cfprVnicLanConnPolicyPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicLanConnPolicyPolicyOwner.setStatus(_A)
_CfprVnicLanConnTemplTable_Object=MibTable
cfprVnicLanConnTemplTable=_CfprVnicLanConnTemplTable_Object((1,3,6,1,4,1,9,9,826,1,83,47))
if mibBuilder.loadTexts:cfprVnicLanConnTemplTable.setStatus(_A)
_CfprVnicLanConnTemplEntry_Object=MibTableRow
cfprVnicLanConnTemplEntry=_CfprVnicLanConnTemplEntry_Object((1,3,6,1,4,1,9,9,826,1,83,47,1))
cfprVnicLanConnTemplEntry.setIndexNames((0,_C,_y))
if mibBuilder.loadTexts:cfprVnicLanConnTemplEntry.setStatus(_A)
_CfprVnicLanConnTemplInstanceId_Type=CfprManagedObjectId
_CfprVnicLanConnTemplInstanceId_Object=MibTableColumn
cfprVnicLanConnTemplInstanceId=_CfprVnicLanConnTemplInstanceId_Object((1,3,6,1,4,1,9,9,826,1,83,47,1,1),_CfprVnicLanConnTemplInstanceId_Type())
cfprVnicLanConnTemplInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprVnicLanConnTemplInstanceId.setStatus(_A)
_CfprVnicLanConnTemplDn_Type=CfprManagedObjectDn
_CfprVnicLanConnTemplDn_Object=MibTableColumn
cfprVnicLanConnTemplDn=_CfprVnicLanConnTemplDn_Object((1,3,6,1,4,1,9,9,826,1,83,47,1,2),_CfprVnicLanConnTemplDn_Type())
cfprVnicLanConnTemplDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicLanConnTemplDn.setStatus(_A)
_CfprVnicLanConnTemplRn_Type=SnmpAdminString
_CfprVnicLanConnTemplRn_Object=MibTableColumn
cfprVnicLanConnTemplRn=_CfprVnicLanConnTemplRn_Object((1,3,6,1,4,1,9,9,826,1,83,47,1,3),_CfprVnicLanConnTemplRn_Type())
cfprVnicLanConnTemplRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicLanConnTemplRn.setStatus(_A)
_CfprVnicLanConnTemplDescr_Type=SnmpAdminString
_CfprVnicLanConnTemplDescr_Object=MibTableColumn
cfprVnicLanConnTemplDescr=_CfprVnicLanConnTemplDescr_Object((1,3,6,1,4,1,9,9,826,1,83,47,1,4),_CfprVnicLanConnTemplDescr_Type())
cfprVnicLanConnTemplDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicLanConnTemplDescr.setStatus(_A)
_CfprVnicLanConnTemplIdentPoolName_Type=SnmpAdminString
_CfprVnicLanConnTemplIdentPoolName_Object=MibTableColumn
cfprVnicLanConnTemplIdentPoolName=_CfprVnicLanConnTemplIdentPoolName_Object((1,3,6,1,4,1,9,9,826,1,83,47,1,5),_CfprVnicLanConnTemplIdentPoolName_Type())
cfprVnicLanConnTemplIdentPoolName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicLanConnTemplIdentPoolName.setStatus(_A)
_CfprVnicLanConnTemplIntId_Type=SnmpAdminString
_CfprVnicLanConnTemplIntId_Object=MibTableColumn
cfprVnicLanConnTemplIntId=_CfprVnicLanConnTemplIntId_Object((1,3,6,1,4,1,9,9,826,1,83,47,1,6),_CfprVnicLanConnTemplIntId_Type())
cfprVnicLanConnTemplIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicLanConnTemplIntId.setStatus(_A)
_CfprVnicLanConnTemplMtu_Type=Gauge32
_CfprVnicLanConnTemplMtu_Object=MibTableColumn
cfprVnicLanConnTemplMtu=_CfprVnicLanConnTemplMtu_Object((1,3,6,1,4,1,9,9,826,1,83,47,1,7),_CfprVnicLanConnTemplMtu_Type())
cfprVnicLanConnTemplMtu.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicLanConnTemplMtu.setStatus(_A)
_CfprVnicLanConnTemplName_Type=SnmpAdminString
_CfprVnicLanConnTemplName_Object=MibTableColumn
cfprVnicLanConnTemplName=_CfprVnicLanConnTemplName_Object((1,3,6,1,4,1,9,9,826,1,83,47,1,8),_CfprVnicLanConnTemplName_Type())
cfprVnicLanConnTemplName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicLanConnTemplName.setStatus(_A)
_CfprVnicLanConnTemplNwCtrlPolicyName_Type=SnmpAdminString
_CfprVnicLanConnTemplNwCtrlPolicyName_Object=MibTableColumn
cfprVnicLanConnTemplNwCtrlPolicyName=_CfprVnicLanConnTemplNwCtrlPolicyName_Object((1,3,6,1,4,1,9,9,826,1,83,47,1,9),_CfprVnicLanConnTemplNwCtrlPolicyName_Type())
cfprVnicLanConnTemplNwCtrlPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicLanConnTemplNwCtrlPolicyName.setStatus(_A)
_CfprVnicLanConnTemplOperIdentPoolName_Type=SnmpAdminString
_CfprVnicLanConnTemplOperIdentPoolName_Object=MibTableColumn
cfprVnicLanConnTemplOperIdentPoolName=_CfprVnicLanConnTemplOperIdentPoolName_Object((1,3,6,1,4,1,9,9,826,1,83,47,1,10),_CfprVnicLanConnTemplOperIdentPoolName_Type())
cfprVnicLanConnTemplOperIdentPoolName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicLanConnTemplOperIdentPoolName.setStatus(_A)
_CfprVnicLanConnTemplOperNwCtrlPolicyName_Type=SnmpAdminString
_CfprVnicLanConnTemplOperNwCtrlPolicyName_Object=MibTableColumn
cfprVnicLanConnTemplOperNwCtrlPolicyName=_CfprVnicLanConnTemplOperNwCtrlPolicyName_Object((1,3,6,1,4,1,9,9,826,1,83,47,1,11),_CfprVnicLanConnTemplOperNwCtrlPolicyName_Type())
cfprVnicLanConnTemplOperNwCtrlPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicLanConnTemplOperNwCtrlPolicyName.setStatus(_A)
_CfprVnicLanConnTemplOperQosPolicyName_Type=SnmpAdminString
_CfprVnicLanConnTemplOperQosPolicyName_Object=MibTableColumn
cfprVnicLanConnTemplOperQosPolicyName=_CfprVnicLanConnTemplOperQosPolicyName_Object((1,3,6,1,4,1,9,9,826,1,83,47,1,12),_CfprVnicLanConnTemplOperQosPolicyName_Type())
cfprVnicLanConnTemplOperQosPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicLanConnTemplOperQosPolicyName.setStatus(_A)
_CfprVnicLanConnTemplOperStatsPolicyName_Type=SnmpAdminString
_CfprVnicLanConnTemplOperStatsPolicyName_Object=MibTableColumn
cfprVnicLanConnTemplOperStatsPolicyName=_CfprVnicLanConnTemplOperStatsPolicyName_Object((1,3,6,1,4,1,9,9,826,1,83,47,1,13),_CfprVnicLanConnTemplOperStatsPolicyName_Type())
cfprVnicLanConnTemplOperStatsPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicLanConnTemplOperStatsPolicyName.setStatus(_A)
_CfprVnicLanConnTemplPinToGroupName_Type=SnmpAdminString
_CfprVnicLanConnTemplPinToGroupName_Object=MibTableColumn
cfprVnicLanConnTemplPinToGroupName=_CfprVnicLanConnTemplPinToGroupName_Object((1,3,6,1,4,1,9,9,826,1,83,47,1,14),_CfprVnicLanConnTemplPinToGroupName_Type())
cfprVnicLanConnTemplPinToGroupName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicLanConnTemplPinToGroupName.setStatus(_A)
_CfprVnicLanConnTemplPolicyLevel_Type=Gauge32
_CfprVnicLanConnTemplPolicyLevel_Object=MibTableColumn
cfprVnicLanConnTemplPolicyLevel=_CfprVnicLanConnTemplPolicyLevel_Object((1,3,6,1,4,1,9,9,826,1,83,47,1,15),_CfprVnicLanConnTemplPolicyLevel_Type())
cfprVnicLanConnTemplPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicLanConnTemplPolicyLevel.setStatus(_A)
_CfprVnicLanConnTemplPolicyOwner_Type=CfprPolicyPolicyOwner
_CfprVnicLanConnTemplPolicyOwner_Object=MibTableColumn
cfprVnicLanConnTemplPolicyOwner=_CfprVnicLanConnTemplPolicyOwner_Object((1,3,6,1,4,1,9,9,826,1,83,47,1,16),_CfprVnicLanConnTemplPolicyOwner_Type())
cfprVnicLanConnTemplPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicLanConnTemplPolicyOwner.setStatus(_A)
_CfprVnicLanConnTemplQosPolicyName_Type=SnmpAdminString
_CfprVnicLanConnTemplQosPolicyName_Object=MibTableColumn
cfprVnicLanConnTemplQosPolicyName=_CfprVnicLanConnTemplQosPolicyName_Object((1,3,6,1,4,1,9,9,826,1,83,47,1,17),_CfprVnicLanConnTemplQosPolicyName_Type())
cfprVnicLanConnTemplQosPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicLanConnTemplQosPolicyName.setStatus(_A)
_CfprVnicLanConnTemplStatsPolicyName_Type=SnmpAdminString
_CfprVnicLanConnTemplStatsPolicyName_Object=MibTableColumn
cfprVnicLanConnTemplStatsPolicyName=_CfprVnicLanConnTemplStatsPolicyName_Object((1,3,6,1,4,1,9,9,826,1,83,47,1,18),_CfprVnicLanConnTemplStatsPolicyName_Type())
cfprVnicLanConnTemplStatsPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicLanConnTemplStatsPolicyName.setStatus(_A)
_CfprVnicLanConnTemplSwitchId_Type=CfprVnicLanConnTemplSwitchId
_CfprVnicLanConnTemplSwitchId_Object=MibTableColumn
cfprVnicLanConnTemplSwitchId=_CfprVnicLanConnTemplSwitchId_Object((1,3,6,1,4,1,9,9,826,1,83,47,1,19),_CfprVnicLanConnTemplSwitchId_Type())
cfprVnicLanConnTemplSwitchId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicLanConnTemplSwitchId.setStatus(_A)
_CfprVnicLanConnTemplTarget_Type=CfprVnicTemplateTarget
_CfprVnicLanConnTemplTarget_Object=MibTableColumn
cfprVnicLanConnTemplTarget=_CfprVnicLanConnTemplTarget_Object((1,3,6,1,4,1,9,9,826,1,83,47,1,20),_CfprVnicLanConnTemplTarget_Type())
cfprVnicLanConnTemplTarget.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicLanConnTemplTarget.setStatus(_A)
_CfprVnicLanConnTemplTemplType_Type=CfprVnicTemplateType
_CfprVnicLanConnTemplTemplType_Object=MibTableColumn
cfprVnicLanConnTemplTemplType=_CfprVnicLanConnTemplTemplType_Object((1,3,6,1,4,1,9,9,826,1,83,47,1,21),_CfprVnicLanConnTemplTemplType_Type())
cfprVnicLanConnTemplTemplType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicLanConnTemplTemplType.setStatus(_A)
_CfprVnicLifVlanTable_Object=MibTable
cfprVnicLifVlanTable=_CfprVnicLifVlanTable_Object((1,3,6,1,4,1,9,9,826,1,83,48))
if mibBuilder.loadTexts:cfprVnicLifVlanTable.setStatus(_A)
_CfprVnicLifVlanEntry_Object=MibTableRow
cfprVnicLifVlanEntry=_CfprVnicLifVlanEntry_Object((1,3,6,1,4,1,9,9,826,1,83,48,1))
cfprVnicLifVlanEntry.setIndexNames((0,_C,_z))
if mibBuilder.loadTexts:cfprVnicLifVlanEntry.setStatus(_A)
_CfprVnicLifVlanInstanceId_Type=CfprManagedObjectId
_CfprVnicLifVlanInstanceId_Object=MibTableColumn
cfprVnicLifVlanInstanceId=_CfprVnicLifVlanInstanceId_Object((1,3,6,1,4,1,9,9,826,1,83,48,1,1),_CfprVnicLifVlanInstanceId_Type())
cfprVnicLifVlanInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprVnicLifVlanInstanceId.setStatus(_A)
_CfprVnicLifVlanDn_Type=CfprManagedObjectDn
_CfprVnicLifVlanDn_Object=MibTableColumn
cfprVnicLifVlanDn=_CfprVnicLifVlanDn_Object((1,3,6,1,4,1,9,9,826,1,83,48,1,2),_CfprVnicLifVlanDn_Type())
cfprVnicLifVlanDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicLifVlanDn.setStatus(_A)
_CfprVnicLifVlanRn_Type=SnmpAdminString
_CfprVnicLifVlanRn_Object=MibTableColumn
cfprVnicLifVlanRn=_CfprVnicLifVlanRn_Object((1,3,6,1,4,1,9,9,826,1,83,48,1,3),_CfprVnicLifVlanRn_Type())
cfprVnicLifVlanRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicLifVlanRn.setStatus(_A)
_CfprVnicLifVlanAddr_Type=MacAddress
_CfprVnicLifVlanAddr_Object=MibTableColumn
cfprVnicLifVlanAddr=_CfprVnicLifVlanAddr_Object((1,3,6,1,4,1,9,9,826,1,83,48,1,4),_CfprVnicLifVlanAddr_Type())
cfprVnicLifVlanAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicLifVlanAddr.setStatus(_A)
_CfprVnicLifVlanConfigQualifier_Type=CfprVnicConfigIssues
_CfprVnicLifVlanConfigQualifier_Object=MibTableColumn
cfprVnicLifVlanConfigQualifier=_CfprVnicLifVlanConfigQualifier_Object((1,3,6,1,4,1,9,9,826,1,83,48,1,5),_CfprVnicLifVlanConfigQualifier_Type())
cfprVnicLifVlanConfigQualifier.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicLifVlanConfigQualifier.setStatus(_A)
_CfprVnicLifVlanDefaultNet_Type=TruthValue
_CfprVnicLifVlanDefaultNet_Object=MibTableColumn
cfprVnicLifVlanDefaultNet=_CfprVnicLifVlanDefaultNet_Object((1,3,6,1,4,1,9,9,826,1,83,48,1,6),_CfprVnicLifVlanDefaultNet_Type())
cfprVnicLifVlanDefaultNet.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicLifVlanDefaultNet.setStatus(_A)
_CfprVnicLifVlanName_Type=SnmpAdminString
_CfprVnicLifVlanName_Object=MibTableColumn
cfprVnicLifVlanName=_CfprVnicLifVlanName_Object((1,3,6,1,4,1,9,9,826,1,83,48,1,7),_CfprVnicLifVlanName_Type())
cfprVnicLifVlanName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicLifVlanName.setStatus(_A)
_CfprVnicLifVlanOperState_Type=CfprVnicIfOperState
_CfprVnicLifVlanOperState_Object=MibTableColumn
cfprVnicLifVlanOperState=_CfprVnicLifVlanOperState_Object((1,3,6,1,4,1,9,9,826,1,83,48,1,8),_CfprVnicLifVlanOperState_Type())
cfprVnicLifVlanOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicLifVlanOperState.setStatus(_A)
_CfprVnicLifVlanOperVnetDn_Type=SnmpAdminString
_CfprVnicLifVlanOperVnetDn_Object=MibTableColumn
cfprVnicLifVlanOperVnetDn=_CfprVnicLifVlanOperVnetDn_Object((1,3,6,1,4,1,9,9,826,1,83,48,1,9),_CfprVnicLifVlanOperVnetDn_Type())
cfprVnicLifVlanOperVnetDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicLifVlanOperVnetDn.setStatus(_A)
_CfprVnicLifVlanOperVnetName_Type=SnmpAdminString
_CfprVnicLifVlanOperVnetName_Object=MibTableColumn
cfprVnicLifVlanOperVnetName=_CfprVnicLifVlanOperVnetName_Object((1,3,6,1,4,1,9,9,826,1,83,48,1,10),_CfprVnicLifVlanOperVnetName_Type())
cfprVnicLifVlanOperVnetName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicLifVlanOperVnetName.setStatus(_A)
_CfprVnicLifVlanOwner_Type=CfprVnicConnectionOwner
_CfprVnicLifVlanOwner_Object=MibTableColumn
cfprVnicLifVlanOwner=_CfprVnicLifVlanOwner_Object((1,3,6,1,4,1,9,9,826,1,83,48,1,11),_CfprVnicLifVlanOwner_Type())
cfprVnicLifVlanOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicLifVlanOwner.setStatus(_A)
_CfprVnicLifVlanPubNwId_Type=Gauge32
_CfprVnicLifVlanPubNwId_Object=MibTableColumn
cfprVnicLifVlanPubNwId=_CfprVnicLifVlanPubNwId_Object((1,3,6,1,4,1,9,9,826,1,83,48,1,12),_CfprVnicLifVlanPubNwId_Type())
cfprVnicLifVlanPubNwId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicLifVlanPubNwId.setStatus(_A)
_CfprVnicLifVlanSharing_Type=CfprFabricVlanSharingType
_CfprVnicLifVlanSharing_Object=MibTableColumn
cfprVnicLifVlanSharing=_CfprVnicLifVlanSharing_Object((1,3,6,1,4,1,9,9,826,1,83,48,1,13),_CfprVnicLifVlanSharing_Type())
cfprVnicLifVlanSharing.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicLifVlanSharing.setStatus(_A)
_CfprVnicLifVlanSwitchId_Type=CfprVnicL2IfSwitchId
_CfprVnicLifVlanSwitchId_Object=MibTableColumn
cfprVnicLifVlanSwitchId=_CfprVnicLifVlanSwitchId_Object((1,3,6,1,4,1,9,9,826,1,83,48,1,14),_CfprVnicLifVlanSwitchId_Type())
cfprVnicLifVlanSwitchId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicLifVlanSwitchId.setStatus(_A)
_CfprVnicLifVlanType_Type=CfprVnicAEtherIfType
_CfprVnicLifVlanType_Object=MibTableColumn
cfprVnicLifVlanType=_CfprVnicLifVlanType_Object((1,3,6,1,4,1,9,9,826,1,83,48,1,15),_CfprVnicLifVlanType_Type())
cfprVnicLifVlanType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicLifVlanType.setStatus(_A)
_CfprVnicLifVlanVnet_Type=Gauge32
_CfprVnicLifVlanVnet_Object=MibTableColumn
cfprVnicLifVlanVnet=_CfprVnicLifVlanVnet_Object((1,3,6,1,4,1,9,9,826,1,83,48,1,16),_CfprVnicLifVlanVnet_Type())
cfprVnicLifVlanVnet.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicLifVlanVnet.setStatus(_A)
_CfprVnicLifVsanTable_Object=MibTable
cfprVnicLifVsanTable=_CfprVnicLifVsanTable_Object((1,3,6,1,4,1,9,9,826,1,83,49))
if mibBuilder.loadTexts:cfprVnicLifVsanTable.setStatus(_A)
_CfprVnicLifVsanEntry_Object=MibTableRow
cfprVnicLifVsanEntry=_CfprVnicLifVsanEntry_Object((1,3,6,1,4,1,9,9,826,1,83,49,1))
cfprVnicLifVsanEntry.setIndexNames((0,_C,_A0))
if mibBuilder.loadTexts:cfprVnicLifVsanEntry.setStatus(_A)
_CfprVnicLifVsanInstanceId_Type=CfprManagedObjectId
_CfprVnicLifVsanInstanceId_Object=MibTableColumn
cfprVnicLifVsanInstanceId=_CfprVnicLifVsanInstanceId_Object((1,3,6,1,4,1,9,9,826,1,83,49,1,1),_CfprVnicLifVsanInstanceId_Type())
cfprVnicLifVsanInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprVnicLifVsanInstanceId.setStatus(_A)
_CfprVnicLifVsanDn_Type=CfprManagedObjectDn
_CfprVnicLifVsanDn_Object=MibTableColumn
cfprVnicLifVsanDn=_CfprVnicLifVsanDn_Object((1,3,6,1,4,1,9,9,826,1,83,49,1,2),_CfprVnicLifVsanDn_Type())
cfprVnicLifVsanDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicLifVsanDn.setStatus(_A)
_CfprVnicLifVsanRn_Type=SnmpAdminString
_CfprVnicLifVsanRn_Object=MibTableColumn
cfprVnicLifVsanRn=_CfprVnicLifVsanRn_Object((1,3,6,1,4,1,9,9,826,1,83,49,1,3),_CfprVnicLifVsanRn_Type())
cfprVnicLifVsanRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicLifVsanRn.setStatus(_A)
_CfprVnicLifVsanConfigQualifier_Type=CfprVnicConfigIssues
_CfprVnicLifVsanConfigQualifier_Object=MibTableColumn
cfprVnicLifVsanConfigQualifier=_CfprVnicLifVsanConfigQualifier_Object((1,3,6,1,4,1,9,9,826,1,83,49,1,4),_CfprVnicLifVsanConfigQualifier_Type())
cfprVnicLifVsanConfigQualifier.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicLifVsanConfigQualifier.setStatus(_A)
_CfprVnicLifVsanInitiator_Type=Unsigned64
_CfprVnicLifVsanInitiator_Object=MibTableColumn
cfprVnicLifVsanInitiator=_CfprVnicLifVsanInitiator_Object((1,3,6,1,4,1,9,9,826,1,83,49,1,5),_CfprVnicLifVsanInitiator_Type())
cfprVnicLifVsanInitiator.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicLifVsanInitiator.setStatus(_A)
_CfprVnicLifVsanName_Type=SnmpAdminString
_CfprVnicLifVsanName_Object=MibTableColumn
cfprVnicLifVsanName=_CfprVnicLifVsanName_Object((1,3,6,1,4,1,9,9,826,1,83,49,1,6),_CfprVnicLifVsanName_Type())
cfprVnicLifVsanName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicLifVsanName.setStatus(_A)
_CfprVnicLifVsanOperState_Type=CfprVnicIfOperState
_CfprVnicLifVsanOperState_Object=MibTableColumn
cfprVnicLifVsanOperState=_CfprVnicLifVsanOperState_Object((1,3,6,1,4,1,9,9,826,1,83,49,1,7),_CfprVnicLifVsanOperState_Type())
cfprVnicLifVsanOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicLifVsanOperState.setStatus(_A)
_CfprVnicLifVsanOperVnetDn_Type=SnmpAdminString
_CfprVnicLifVsanOperVnetDn_Object=MibTableColumn
cfprVnicLifVsanOperVnetDn=_CfprVnicLifVsanOperVnetDn_Object((1,3,6,1,4,1,9,9,826,1,83,49,1,8),_CfprVnicLifVsanOperVnetDn_Type())
cfprVnicLifVsanOperVnetDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicLifVsanOperVnetDn.setStatus(_A)
_CfprVnicLifVsanOperVnetName_Type=SnmpAdminString
_CfprVnicLifVsanOperVnetName_Object=MibTableColumn
cfprVnicLifVsanOperVnetName=_CfprVnicLifVsanOperVnetName_Object((1,3,6,1,4,1,9,9,826,1,83,49,1,9),_CfprVnicLifVsanOperVnetName_Type())
cfprVnicLifVsanOperVnetName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicLifVsanOperVnetName.setStatus(_A)
_CfprVnicLifVsanOwner_Type=CfprVnicConnectionOwner
_CfprVnicLifVsanOwner_Object=MibTableColumn
cfprVnicLifVsanOwner=_CfprVnicLifVsanOwner_Object((1,3,6,1,4,1,9,9,826,1,83,49,1,10),_CfprVnicLifVsanOwner_Type())
cfprVnicLifVsanOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicLifVsanOwner.setStatus(_A)
_CfprVnicLifVsanPubNwId_Type=Gauge32
_CfprVnicLifVsanPubNwId_Object=MibTableColumn
cfprVnicLifVsanPubNwId=_CfprVnicLifVsanPubNwId_Object((1,3,6,1,4,1,9,9,826,1,83,49,1,11),_CfprVnicLifVsanPubNwId_Type())
cfprVnicLifVsanPubNwId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicLifVsanPubNwId.setStatus(_A)
_CfprVnicLifVsanSharing_Type=CfprFabricVlanSharingType
_CfprVnicLifVsanSharing_Object=MibTableColumn
cfprVnicLifVsanSharing=_CfprVnicLifVsanSharing_Object((1,3,6,1,4,1,9,9,826,1,83,49,1,12),_CfprVnicLifVsanSharing_Type())
cfprVnicLifVsanSharing.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicLifVsanSharing.setStatus(_A)
_CfprVnicLifVsanSwitchId_Type=CfprVnicL2IfSwitchId
_CfprVnicLifVsanSwitchId_Object=MibTableColumn
cfprVnicLifVsanSwitchId=_CfprVnicLifVsanSwitchId_Object((1,3,6,1,4,1,9,9,826,1,83,49,1,13),_CfprVnicLifVsanSwitchId_Type())
cfprVnicLifVsanSwitchId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicLifVsanSwitchId.setStatus(_A)
_CfprVnicLifVsanType_Type=CfprVnicAFcIfType
_CfprVnicLifVsanType_Object=MibTableColumn
cfprVnicLifVsanType=_CfprVnicLifVsanType_Object((1,3,6,1,4,1,9,9,826,1,83,49,1,14),_CfprVnicLifVsanType_Type())
cfprVnicLifVsanType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicLifVsanType.setStatus(_A)
_CfprVnicLifVsanVnet_Type=Gauge32
_CfprVnicLifVsanVnet_Object=MibTableColumn
cfprVnicLifVsanVnet=_CfprVnicLifVsanVnet_Object((1,3,6,1,4,1,9,9,826,1,83,49,1,15),_CfprVnicLifVsanVnet_Type())
cfprVnicLifVsanVnet.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicLifVsanVnet.setStatus(_A)
_CfprVnicLunTable_Object=MibTable
cfprVnicLunTable=_CfprVnicLunTable_Object((1,3,6,1,4,1,9,9,826,1,83,50))
if mibBuilder.loadTexts:cfprVnicLunTable.setStatus(_A)
_CfprVnicLunEntry_Object=MibTableRow
cfprVnicLunEntry=_CfprVnicLunEntry_Object((1,3,6,1,4,1,9,9,826,1,83,50,1))
cfprVnicLunEntry.setIndexNames((0,_C,_A1))
if mibBuilder.loadTexts:cfprVnicLunEntry.setStatus(_A)
_CfprVnicLunInstanceId_Type=CfprManagedObjectId
_CfprVnicLunInstanceId_Object=MibTableColumn
cfprVnicLunInstanceId=_CfprVnicLunInstanceId_Object((1,3,6,1,4,1,9,9,826,1,83,50,1,1),_CfprVnicLunInstanceId_Type())
cfprVnicLunInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprVnicLunInstanceId.setStatus(_A)
_CfprVnicLunDn_Type=CfprManagedObjectDn
_CfprVnicLunDn_Object=MibTableColumn
cfprVnicLunDn=_CfprVnicLunDn_Object((1,3,6,1,4,1,9,9,826,1,83,50,1,2),_CfprVnicLunDn_Type())
cfprVnicLunDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicLunDn.setStatus(_A)
_CfprVnicLunRn_Type=SnmpAdminString
_CfprVnicLunRn_Object=MibTableColumn
cfprVnicLunRn=_CfprVnicLunRn_Object((1,3,6,1,4,1,9,9,826,1,83,50,1,3),_CfprVnicLunRn_Type())
cfprVnicLunRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicLunRn.setStatus(_A)
_CfprVnicLunBootable_Type=TruthValue
_CfprVnicLunBootable_Object=MibTableColumn
cfprVnicLunBootable=_CfprVnicLunBootable_Object((1,3,6,1,4,1,9,9,826,1,83,50,1,4),_CfprVnicLunBootable_Type())
cfprVnicLunBootable.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicLunBootable.setStatus(_A)
_CfprVnicLunId_Type=CfprVnicLunId
_CfprVnicLunId_Object=MibTableColumn
cfprVnicLunId=_CfprVnicLunId_Object((1,3,6,1,4,1,9,9,826,1,83,50,1,5),_CfprVnicLunId_Type())
cfprVnicLunId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicLunId.setStatus(_A)
_CfprVnicMacHistoryTable_Object=MibTable
cfprVnicMacHistoryTable=_CfprVnicMacHistoryTable_Object((1,3,6,1,4,1,9,9,826,1,83,51))
if mibBuilder.loadTexts:cfprVnicMacHistoryTable.setStatus(_A)
_CfprVnicMacHistoryEntry_Object=MibTableRow
cfprVnicMacHistoryEntry=_CfprVnicMacHistoryEntry_Object((1,3,6,1,4,1,9,9,826,1,83,51,1))
cfprVnicMacHistoryEntry.setIndexNames((0,_C,_A2))
if mibBuilder.loadTexts:cfprVnicMacHistoryEntry.setStatus(_A)
_CfprVnicMacHistoryInstanceId_Type=CfprManagedObjectId
_CfprVnicMacHistoryInstanceId_Object=MibTableColumn
cfprVnicMacHistoryInstanceId=_CfprVnicMacHistoryInstanceId_Object((1,3,6,1,4,1,9,9,826,1,83,51,1,1),_CfprVnicMacHistoryInstanceId_Type())
cfprVnicMacHistoryInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprVnicMacHistoryInstanceId.setStatus(_A)
_CfprVnicMacHistoryDn_Type=CfprManagedObjectDn
_CfprVnicMacHistoryDn_Object=MibTableColumn
cfprVnicMacHistoryDn=_CfprVnicMacHistoryDn_Object((1,3,6,1,4,1,9,9,826,1,83,51,1,2),_CfprVnicMacHistoryDn_Type())
cfprVnicMacHistoryDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicMacHistoryDn.setStatus(_A)
_CfprVnicMacHistoryRn_Type=SnmpAdminString
_CfprVnicMacHistoryRn_Object=MibTableColumn
cfprVnicMacHistoryRn=_CfprVnicMacHistoryRn_Object((1,3,6,1,4,1,9,9,826,1,83,51,1,3),_CfprVnicMacHistoryRn_Type())
cfprVnicMacHistoryRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicMacHistoryRn.setStatus(_A)
_CfprVnicMacHistoryOldaddr_Type=MacAddress
_CfprVnicMacHistoryOldaddr_Object=MibTableColumn
cfprVnicMacHistoryOldaddr=_CfprVnicMacHistoryOldaddr_Object((1,3,6,1,4,1,9,9,826,1,83,51,1,4),_CfprVnicMacHistoryOldaddr_Type())
cfprVnicMacHistoryOldaddr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicMacHistoryOldaddr.setStatus(_A)
_CfprVnicOProfileAliasTable_Object=MibTable
cfprVnicOProfileAliasTable=_CfprVnicOProfileAliasTable_Object((1,3,6,1,4,1,9,9,826,1,83,52))
if mibBuilder.loadTexts:cfprVnicOProfileAliasTable.setStatus(_A)
_CfprVnicOProfileAliasEntry_Object=MibTableRow
cfprVnicOProfileAliasEntry=_CfprVnicOProfileAliasEntry_Object((1,3,6,1,4,1,9,9,826,1,83,52,1))
cfprVnicOProfileAliasEntry.setIndexNames((0,_C,_A3))
if mibBuilder.loadTexts:cfprVnicOProfileAliasEntry.setStatus(_A)
_CfprVnicOProfileAliasInstanceId_Type=CfprManagedObjectId
_CfprVnicOProfileAliasInstanceId_Object=MibTableColumn
cfprVnicOProfileAliasInstanceId=_CfprVnicOProfileAliasInstanceId_Object((1,3,6,1,4,1,9,9,826,1,83,52,1,1),_CfprVnicOProfileAliasInstanceId_Type())
cfprVnicOProfileAliasInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprVnicOProfileAliasInstanceId.setStatus(_A)
_CfprVnicOProfileAliasDn_Type=CfprManagedObjectDn
_CfprVnicOProfileAliasDn_Object=MibTableColumn
cfprVnicOProfileAliasDn=_CfprVnicOProfileAliasDn_Object((1,3,6,1,4,1,9,9,826,1,83,52,1,2),_CfprVnicOProfileAliasDn_Type())
cfprVnicOProfileAliasDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicOProfileAliasDn.setStatus(_A)
_CfprVnicOProfileAliasRn_Type=SnmpAdminString
_CfprVnicOProfileAliasRn_Object=MibTableColumn
cfprVnicOProfileAliasRn=_CfprVnicOProfileAliasRn_Object((1,3,6,1,4,1,9,9,826,1,83,52,1,3),_CfprVnicOProfileAliasRn_Type())
cfprVnicOProfileAliasRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicOProfileAliasRn.setStatus(_A)
_CfprVnicOProfileAliasAlias_Type=SnmpAdminString
_CfprVnicOProfileAliasAlias_Object=MibTableColumn
cfprVnicOProfileAliasAlias=_CfprVnicOProfileAliasAlias_Object((1,3,6,1,4,1,9,9,826,1,83,52,1,4),_CfprVnicOProfileAliasAlias_Type())
cfprVnicOProfileAliasAlias.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicOProfileAliasAlias.setStatus(_A)
_CfprVnicOProfileAliasMgmtPlane_Type=CfprVmMgmtPlane
_CfprVnicOProfileAliasMgmtPlane_Object=MibTableColumn
cfprVnicOProfileAliasMgmtPlane=_CfprVnicOProfileAliasMgmtPlane_Object((1,3,6,1,4,1,9,9,826,1,83,52,1,5),_CfprVnicOProfileAliasMgmtPlane_Type())
cfprVnicOProfileAliasMgmtPlane.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicOProfileAliasMgmtPlane.setStatus(_A)
_CfprVnicOProfileAliasVSwitchId_Type=SnmpAdminString
_CfprVnicOProfileAliasVSwitchId_Object=MibTableColumn
cfprVnicOProfileAliasVSwitchId=_CfprVnicOProfileAliasVSwitchId_Object((1,3,6,1,4,1,9,9,826,1,83,52,1,6),_CfprVnicOProfileAliasVSwitchId_Type())
cfprVnicOProfileAliasVSwitchId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicOProfileAliasVSwitchId.setStatus(_A)
_CfprVnicOProfileAliasVSwitchName_Type=SnmpAdminString
_CfprVnicOProfileAliasVSwitchName_Object=MibTableColumn
cfprVnicOProfileAliasVSwitchName=_CfprVnicOProfileAliasVSwitchName_Object((1,3,6,1,4,1,9,9,826,1,83,52,1,7),_CfprVnicOProfileAliasVSwitchName_Type())
cfprVnicOProfileAliasVSwitchName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicOProfileAliasVSwitchName.setStatus(_A)
_CfprVnicProfileTable_Object=MibTable
cfprVnicProfileTable=_CfprVnicProfileTable_Object((1,3,6,1,4,1,9,9,826,1,83,53))
if mibBuilder.loadTexts:cfprVnicProfileTable.setStatus(_A)
_CfprVnicProfileEntry_Object=MibTableRow
cfprVnicProfileEntry=_CfprVnicProfileEntry_Object((1,3,6,1,4,1,9,9,826,1,83,53,1))
cfprVnicProfileEntry.setIndexNames((0,_C,_A4))
if mibBuilder.loadTexts:cfprVnicProfileEntry.setStatus(_A)
_CfprVnicProfileInstanceId_Type=CfprManagedObjectId
_CfprVnicProfileInstanceId_Object=MibTableColumn
cfprVnicProfileInstanceId=_CfprVnicProfileInstanceId_Object((1,3,6,1,4,1,9,9,826,1,83,53,1,1),_CfprVnicProfileInstanceId_Type())
cfprVnicProfileInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprVnicProfileInstanceId.setStatus(_A)
_CfprVnicProfileDn_Type=CfprManagedObjectDn
_CfprVnicProfileDn_Object=MibTableColumn
cfprVnicProfileDn=_CfprVnicProfileDn_Object((1,3,6,1,4,1,9,9,826,1,83,53,1,2),_CfprVnicProfileDn_Type())
cfprVnicProfileDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicProfileDn.setStatus(_A)
_CfprVnicProfileRn_Type=SnmpAdminString
_CfprVnicProfileRn_Object=MibTableColumn
cfprVnicProfileRn=_CfprVnicProfileRn_Object((1,3,6,1,4,1,9,9,826,1,83,53,1,3),_CfprVnicProfileRn_Type())
cfprVnicProfileRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicProfileRn.setStatus(_A)
_CfprVnicProfileCdp_Type=CfprNwctrlAdminState
_CfprVnicProfileCdp_Object=MibTableColumn
cfprVnicProfileCdp=_CfprVnicProfileCdp_Object((1,3,6,1,4,1,9,9,826,1,83,53,1,4),_CfprVnicProfileCdp_Type())
cfprVnicProfileCdp.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicProfileCdp.setStatus(_A)
_CfprVnicProfileConfigQualifier_Type=CfprVnicProfileConfigQualifier
_CfprVnicProfileConfigQualifier_Object=MibTableColumn
cfprVnicProfileConfigQualifier=_CfprVnicProfileConfigQualifier_Object((1,3,6,1,4,1,9,9,826,1,83,53,1,5),_CfprVnicProfileConfigQualifier_Type())
cfprVnicProfileConfigQualifier.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicProfileConfigQualifier.setStatus(_A)
_CfprVnicProfileCos_Type=Gauge32
_CfprVnicProfileCos_Object=MibTableColumn
cfprVnicProfileCos=_CfprVnicProfileCos_Object((1,3,6,1,4,1,9,9,826,1,83,53,1,6),_CfprVnicProfileCos_Type())
cfprVnicProfileCos.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicProfileCos.setStatus(_A)
_CfprVnicProfileDescr_Type=SnmpAdminString
_CfprVnicProfileDescr_Object=MibTableColumn
cfprVnicProfileDescr=_CfprVnicProfileDescr_Object((1,3,6,1,4,1,9,9,826,1,83,53,1,7),_CfprVnicProfileDescr_Type())
cfprVnicProfileDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicProfileDescr.setStatus(_A)
_CfprVnicProfileForgeMac_Type=CfprDpsecForgedTransmit
_CfprVnicProfileForgeMac_Object=MibTableColumn
cfprVnicProfileForgeMac=_CfprVnicProfileForgeMac_Object((1,3,6,1,4,1,9,9,826,1,83,53,1,8),_CfprVnicProfileForgeMac_Type())
cfprVnicProfileForgeMac.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicProfileForgeMac.setStatus(_A)
_CfprVnicProfileHostNwIOPerf_Type=CfprVnicHostNwIOPerfPref
_CfprVnicProfileHostNwIOPerf_Object=MibTableColumn
cfprVnicProfileHostNwIOPerf=_CfprVnicProfileHostNwIOPerf_Object((1,3,6,1,4,1,9,9,826,1,83,53,1,9),_CfprVnicProfileHostNwIOPerf_Type())
cfprVnicProfileHostNwIOPerf.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicProfileHostNwIOPerf.setStatus(_A)
_CfprVnicProfileIntId_Type=SnmpAdminString
_CfprVnicProfileIntId_Object=MibTableColumn
cfprVnicProfileIntId=_CfprVnicProfileIntId_Object((1,3,6,1,4,1,9,9,826,1,83,53,1,10),_CfprVnicProfileIntId_Type())
cfprVnicProfileIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicProfileIntId.setStatus(_A)
_CfprVnicProfileMacRegisterMode_Type=CfprNwctrlRegistrationMode
_CfprVnicProfileMacRegisterMode_Object=MibTableColumn
cfprVnicProfileMacRegisterMode=_CfprVnicProfileMacRegisterMode_Object((1,3,6,1,4,1,9,9,826,1,83,53,1,11),_CfprVnicProfileMacRegisterMode_Type())
cfprVnicProfileMacRegisterMode.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicProfileMacRegisterMode.setStatus(_A)
_CfprVnicProfileMaxPorts_Type=Gauge32
_CfprVnicProfileMaxPorts_Object=MibTableColumn
cfprVnicProfileMaxPorts=_CfprVnicProfileMaxPorts_Object((1,3,6,1,4,1,9,9,826,1,83,53,1,12),_CfprVnicProfileMaxPorts_Type())
cfprVnicProfileMaxPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicProfileMaxPorts.setStatus(_A)
_CfprVnicProfileName_Type=SnmpAdminString
_CfprVnicProfileName_Object=MibTableColumn
cfprVnicProfileName=_CfprVnicProfileName_Object((1,3,6,1,4,1,9,9,826,1,83,53,1,13),_CfprVnicProfileName_Type())
cfprVnicProfileName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicProfileName.setStatus(_A)
_CfprVnicProfileNwCtrlPolicyName_Type=SnmpAdminString
_CfprVnicProfileNwCtrlPolicyName_Object=MibTableColumn
cfprVnicProfileNwCtrlPolicyName=_CfprVnicProfileNwCtrlPolicyName_Object((1,3,6,1,4,1,9,9,826,1,83,53,1,14),_CfprVnicProfileNwCtrlPolicyName_Type())
cfprVnicProfileNwCtrlPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicProfileNwCtrlPolicyName.setStatus(_A)
_CfprVnicProfileOperNwCtrlPolicyName_Type=SnmpAdminString
_CfprVnicProfileOperNwCtrlPolicyName_Object=MibTableColumn
cfprVnicProfileOperNwCtrlPolicyName=_CfprVnicProfileOperNwCtrlPolicyName_Object((1,3,6,1,4,1,9,9,826,1,83,53,1,15),_CfprVnicProfileOperNwCtrlPolicyName_Type())
cfprVnicProfileOperNwCtrlPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicProfileOperNwCtrlPolicyName.setStatus(_A)
_CfprVnicProfileOperQosPolicyName_Type=SnmpAdminString
_CfprVnicProfileOperQosPolicyName_Object=MibTableColumn
cfprVnicProfileOperQosPolicyName=_CfprVnicProfileOperQosPolicyName_Object((1,3,6,1,4,1,9,9,826,1,83,53,1,16),_CfprVnicProfileOperQosPolicyName_Type())
cfprVnicProfileOperQosPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicProfileOperQosPolicyName.setStatus(_A)
_CfprVnicProfilePinToGroupName_Type=SnmpAdminString
_CfprVnicProfilePinToGroupName_Object=MibTableColumn
cfprVnicProfilePinToGroupName=_CfprVnicProfilePinToGroupName_Object((1,3,6,1,4,1,9,9,826,1,83,53,1,17),_CfprVnicProfilePinToGroupName_Type())
cfprVnicProfilePinToGroupName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicProfilePinToGroupName.setStatus(_A)
_CfprVnicProfilePolicyLevel_Type=Gauge32
_CfprVnicProfilePolicyLevel_Object=MibTableColumn
cfprVnicProfilePolicyLevel=_CfprVnicProfilePolicyLevel_Object((1,3,6,1,4,1,9,9,826,1,83,53,1,18),_CfprVnicProfilePolicyLevel_Type())
cfprVnicProfilePolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicProfilePolicyLevel.setStatus(_A)
_CfprVnicProfilePolicyOwner_Type=CfprPolicyPolicyOwner
_CfprVnicProfilePolicyOwner_Object=MibTableColumn
cfprVnicProfilePolicyOwner=_CfprVnicProfilePolicyOwner_Object((1,3,6,1,4,1,9,9,826,1,83,53,1,19),_CfprVnicProfilePolicyOwner_Type())
cfprVnicProfilePolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicProfilePolicyOwner.setStatus(_A)
_CfprVnicProfilePortProfileUuid_Type=SnmpAdminString
_CfprVnicProfilePortProfileUuid_Object=MibTableColumn
cfprVnicProfilePortProfileUuid=_CfprVnicProfilePortProfileUuid_Object((1,3,6,1,4,1,9,9,826,1,83,53,1,20),_CfprVnicProfilePortProfileUuid_Type())
cfprVnicProfilePortProfileUuid.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicProfilePortProfileUuid.setStatus(_A)
_CfprVnicProfilePrimaryVlanId_Type=Gauge32
_CfprVnicProfilePrimaryVlanId_Object=MibTableColumn
cfprVnicProfilePrimaryVlanId=_CfprVnicProfilePrimaryVlanId_Object((1,3,6,1,4,1,9,9,826,1,83,53,1,21),_CfprVnicProfilePrimaryVlanId_Type())
cfprVnicProfilePrimaryVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicProfilePrimaryVlanId.setStatus(_A)
_CfprVnicProfileQosPolicyDn_Type=SnmpAdminString
_CfprVnicProfileQosPolicyDn_Object=MibTableColumn
cfprVnicProfileQosPolicyDn=_CfprVnicProfileQosPolicyDn_Object((1,3,6,1,4,1,9,9,826,1,83,53,1,22),_CfprVnicProfileQosPolicyDn_Type())
cfprVnicProfileQosPolicyDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicProfileQosPolicyDn.setStatus(_A)
_CfprVnicProfileQosPolicyId_Type=SnmpAdminString
_CfprVnicProfileQosPolicyId_Object=MibTableColumn
cfprVnicProfileQosPolicyId=_CfprVnicProfileQosPolicyId_Object((1,3,6,1,4,1,9,9,826,1,83,53,1,23),_CfprVnicProfileQosPolicyId_Type())
cfprVnicProfileQosPolicyId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicProfileQosPolicyId.setStatus(_A)
_CfprVnicProfileQosPolicyName_Type=SnmpAdminString
_CfprVnicProfileQosPolicyName_Object=MibTableColumn
cfprVnicProfileQosPolicyName=_CfprVnicProfileQosPolicyName_Object((1,3,6,1,4,1,9,9,826,1,83,53,1,24),_CfprVnicProfileQosPolicyName_Type())
cfprVnicProfileQosPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicProfileQosPolicyName.setStatus(_A)
_CfprVnicProfileSwABorderAggrPort_Type=Gauge32
_CfprVnicProfileSwABorderAggrPort_Object=MibTableColumn
cfprVnicProfileSwABorderAggrPort=_CfprVnicProfileSwABorderAggrPort_Object((1,3,6,1,4,1,9,9,826,1,83,53,1,25),_CfprVnicProfileSwABorderAggrPort_Type())
cfprVnicProfileSwABorderAggrPort.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicProfileSwABorderAggrPort.setStatus(_A)
_CfprVnicProfileSwABorderPort_Type=Gauge32
_CfprVnicProfileSwABorderPort_Object=MibTableColumn
cfprVnicProfileSwABorderPort=_CfprVnicProfileSwABorderPort_Object((1,3,6,1,4,1,9,9,826,1,83,53,1,26),_CfprVnicProfileSwABorderPort_Type())
cfprVnicProfileSwABorderPort.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicProfileSwABorderPort.setStatus(_A)
_CfprVnicProfileSwABorderSlot_Type=Gauge32
_CfprVnicProfileSwABorderSlot_Object=MibTableColumn
cfprVnicProfileSwABorderSlot=_CfprVnicProfileSwABorderSlot_Object((1,3,6,1,4,1,9,9,826,1,83,53,1,27),_CfprVnicProfileSwABorderSlot_Type())
cfprVnicProfileSwABorderSlot.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicProfileSwABorderSlot.setStatus(_A)
_CfprVnicProfileSwBBorderAggrPort_Type=Gauge32
_CfprVnicProfileSwBBorderAggrPort_Object=MibTableColumn
cfprVnicProfileSwBBorderAggrPort=_CfprVnicProfileSwBBorderAggrPort_Object((1,3,6,1,4,1,9,9,826,1,83,53,1,28),_CfprVnicProfileSwBBorderAggrPort_Type())
cfprVnicProfileSwBBorderAggrPort.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicProfileSwBBorderAggrPort.setStatus(_A)
_CfprVnicProfileSwBBorderPort_Type=Gauge32
_CfprVnicProfileSwBBorderPort_Object=MibTableColumn
cfprVnicProfileSwBBorderPort=_CfprVnicProfileSwBBorderPort_Object((1,3,6,1,4,1,9,9,826,1,83,53,1,29),_CfprVnicProfileSwBBorderPort_Type())
cfprVnicProfileSwBBorderPort.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicProfileSwBBorderPort.setStatus(_A)
_CfprVnicProfileSwBBorderSlot_Type=Gauge32
_CfprVnicProfileSwBBorderSlot_Object=MibTableColumn
cfprVnicProfileSwBBorderSlot=_CfprVnicProfileSwBBorderSlot_Object((1,3,6,1,4,1,9,9,826,1,83,53,1,30),_CfprVnicProfileSwBBorderSlot_Type())
cfprVnicProfileSwBBorderSlot.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicProfileSwBBorderSlot.setStatus(_A)
_CfprVnicProfileType_Type=CfprVnicPortProfileType
_CfprVnicProfileType_Object=MibTableColumn
cfprVnicProfileType=_CfprVnicProfileType_Object((1,3,6,1,4,1,9,9,826,1,83,53,1,31),_CfprVnicProfileType_Type())
cfprVnicProfileType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicProfileType.setStatus(_A)
_CfprVnicProfileUplinkFailAction_Type=CfprNwctrlLinkFailAction
_CfprVnicProfileUplinkFailAction_Object=MibTableColumn
cfprVnicProfileUplinkFailAction=_CfprVnicProfileUplinkFailAction_Object((1,3,6,1,4,1,9,9,826,1,83,53,1,32),_CfprVnicProfileUplinkFailAction_Type())
cfprVnicProfileUplinkFailAction.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicProfileUplinkFailAction.setStatus(_A)
_CfprVnicProfileAliasTable_Object=MibTable
cfprVnicProfileAliasTable=_CfprVnicProfileAliasTable_Object((1,3,6,1,4,1,9,9,826,1,83,54))
if mibBuilder.loadTexts:cfprVnicProfileAliasTable.setStatus(_A)
_CfprVnicProfileAliasEntry_Object=MibTableRow
cfprVnicProfileAliasEntry=_CfprVnicProfileAliasEntry_Object((1,3,6,1,4,1,9,9,826,1,83,54,1))
cfprVnicProfileAliasEntry.setIndexNames((0,_C,_A5))
if mibBuilder.loadTexts:cfprVnicProfileAliasEntry.setStatus(_A)
_CfprVnicProfileAliasInstanceId_Type=CfprManagedObjectId
_CfprVnicProfileAliasInstanceId_Object=MibTableColumn
cfprVnicProfileAliasInstanceId=_CfprVnicProfileAliasInstanceId_Object((1,3,6,1,4,1,9,9,826,1,83,54,1,1),_CfprVnicProfileAliasInstanceId_Type())
cfprVnicProfileAliasInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprVnicProfileAliasInstanceId.setStatus(_A)
_CfprVnicProfileAliasDn_Type=CfprManagedObjectDn
_CfprVnicProfileAliasDn_Object=MibTableColumn
cfprVnicProfileAliasDn=_CfprVnicProfileAliasDn_Object((1,3,6,1,4,1,9,9,826,1,83,54,1,2),_CfprVnicProfileAliasDn_Type())
cfprVnicProfileAliasDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicProfileAliasDn.setStatus(_A)
_CfprVnicProfileAliasRn_Type=SnmpAdminString
_CfprVnicProfileAliasRn_Object=MibTableColumn
cfprVnicProfileAliasRn=_CfprVnicProfileAliasRn_Object((1,3,6,1,4,1,9,9,826,1,83,54,1,3),_CfprVnicProfileAliasRn_Type())
cfprVnicProfileAliasRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicProfileAliasRn.setStatus(_A)
_CfprVnicProfileAliasAlias_Type=SnmpAdminString
_CfprVnicProfileAliasAlias_Object=MibTableColumn
cfprVnicProfileAliasAlias=_CfprVnicProfileAliasAlias_Object((1,3,6,1,4,1,9,9,826,1,83,54,1,4),_CfprVnicProfileAliasAlias_Type())
cfprVnicProfileAliasAlias.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicProfileAliasAlias.setStatus(_A)
_CfprVnicProfileAliasSwUuid_Type=SnmpAdminString
_CfprVnicProfileAliasSwUuid_Object=MibTableColumn
cfprVnicProfileAliasSwUuid=_CfprVnicProfileAliasSwUuid_Object((1,3,6,1,4,1,9,9,826,1,83,54,1,5),_CfprVnicProfileAliasSwUuid_Type())
cfprVnicProfileAliasSwUuid.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicProfileAliasSwUuid.setStatus(_A)
_CfprVnicProfileRefTable_Object=MibTable
cfprVnicProfileRefTable=_CfprVnicProfileRefTable_Object((1,3,6,1,4,1,9,9,826,1,83,55))
if mibBuilder.loadTexts:cfprVnicProfileRefTable.setStatus(_A)
_CfprVnicProfileRefEntry_Object=MibTableRow
cfprVnicProfileRefEntry=_CfprVnicProfileRefEntry_Object((1,3,6,1,4,1,9,9,826,1,83,55,1))
cfprVnicProfileRefEntry.setIndexNames((0,_C,_A6))
if mibBuilder.loadTexts:cfprVnicProfileRefEntry.setStatus(_A)
_CfprVnicProfileRefInstanceId_Type=CfprManagedObjectId
_CfprVnicProfileRefInstanceId_Object=MibTableColumn
cfprVnicProfileRefInstanceId=_CfprVnicProfileRefInstanceId_Object((1,3,6,1,4,1,9,9,826,1,83,55,1,1),_CfprVnicProfileRefInstanceId_Type())
cfprVnicProfileRefInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprVnicProfileRefInstanceId.setStatus(_A)
_CfprVnicProfileRefDn_Type=CfprManagedObjectDn
_CfprVnicProfileRefDn_Object=MibTableColumn
cfprVnicProfileRefDn=_CfprVnicProfileRefDn_Object((1,3,6,1,4,1,9,9,826,1,83,55,1,2),_CfprVnicProfileRefDn_Type())
cfprVnicProfileRefDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicProfileRefDn.setStatus(_A)
_CfprVnicProfileRefRn_Type=SnmpAdminString
_CfprVnicProfileRefRn_Object=MibTableColumn
cfprVnicProfileRefRn=_CfprVnicProfileRefRn_Object((1,3,6,1,4,1,9,9,826,1,83,55,1,3),_CfprVnicProfileRefRn_Type())
cfprVnicProfileRefRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicProfileRefRn.setStatus(_A)
_CfprVnicProfileRefName_Type=SnmpAdminString
_CfprVnicProfileRefName_Object=MibTableColumn
cfprVnicProfileRefName=_CfprVnicProfileRefName_Object((1,3,6,1,4,1,9,9,826,1,83,55,1,4),_CfprVnicProfileRefName_Type())
cfprVnicProfileRefName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicProfileRefName.setStatus(_A)
_CfprVnicProfileRefSourceDn_Type=SnmpAdminString
_CfprVnicProfileRefSourceDn_Object=MibTableColumn
cfprVnicProfileRefSourceDn=_CfprVnicProfileRefSourceDn_Object((1,3,6,1,4,1,9,9,826,1,83,55,1,5),_CfprVnicProfileRefSourceDn_Type())
cfprVnicProfileRefSourceDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicProfileRefSourceDn.setStatus(_A)
_CfprVnicProfileSetTable_Object=MibTable
cfprVnicProfileSetTable=_CfprVnicProfileSetTable_Object((1,3,6,1,4,1,9,9,826,1,83,56))
if mibBuilder.loadTexts:cfprVnicProfileSetTable.setStatus(_A)
_CfprVnicProfileSetEntry_Object=MibTableRow
cfprVnicProfileSetEntry=_CfprVnicProfileSetEntry_Object((1,3,6,1,4,1,9,9,826,1,83,56,1))
cfprVnicProfileSetEntry.setIndexNames((0,_C,_A7))
if mibBuilder.loadTexts:cfprVnicProfileSetEntry.setStatus(_A)
_CfprVnicProfileSetInstanceId_Type=CfprManagedObjectId
_CfprVnicProfileSetInstanceId_Object=MibTableColumn
cfprVnicProfileSetInstanceId=_CfprVnicProfileSetInstanceId_Object((1,3,6,1,4,1,9,9,826,1,83,56,1,1),_CfprVnicProfileSetInstanceId_Type())
cfprVnicProfileSetInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprVnicProfileSetInstanceId.setStatus(_A)
_CfprVnicProfileSetDn_Type=CfprManagedObjectDn
_CfprVnicProfileSetDn_Object=MibTableColumn
cfprVnicProfileSetDn=_CfprVnicProfileSetDn_Object((1,3,6,1,4,1,9,9,826,1,83,56,1,2),_CfprVnicProfileSetDn_Type())
cfprVnicProfileSetDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicProfileSetDn.setStatus(_A)
_CfprVnicProfileSetRn_Type=SnmpAdminString
_CfprVnicProfileSetRn_Object=MibTableColumn
cfprVnicProfileSetRn=_CfprVnicProfileSetRn_Object((1,3,6,1,4,1,9,9,826,1,83,56,1,3),_CfprVnicProfileSetRn_Type())
cfprVnicProfileSetRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicProfileSetRn.setStatus(_A)
_CfprVnicProfileSetFltAggr_Type=Unsigned64
_CfprVnicProfileSetFltAggr_Object=MibTableColumn
cfprVnicProfileSetFltAggr=_CfprVnicProfileSetFltAggr_Object((1,3,6,1,4,1,9,9,826,1,83,56,1,4),_CfprVnicProfileSetFltAggr_Type())
cfprVnicProfileSetFltAggr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicProfileSetFltAggr.setStatus(_A)
_CfprVnicProfileSetFsmDescr_Type=SnmpAdminString
_CfprVnicProfileSetFsmDescr_Object=MibTableColumn
cfprVnicProfileSetFsmDescr=_CfprVnicProfileSetFsmDescr_Object((1,3,6,1,4,1,9,9,826,1,83,56,1,5),_CfprVnicProfileSetFsmDescr_Type())
cfprVnicProfileSetFsmDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicProfileSetFsmDescr.setStatus(_A)
_CfprVnicProfileSetFsmPrev_Type=SnmpAdminString
_CfprVnicProfileSetFsmPrev_Object=MibTableColumn
cfprVnicProfileSetFsmPrev=_CfprVnicProfileSetFsmPrev_Object((1,3,6,1,4,1,9,9,826,1,83,56,1,6),_CfprVnicProfileSetFsmPrev_Type())
cfprVnicProfileSetFsmPrev.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicProfileSetFsmPrev.setStatus(_A)
_CfprVnicProfileSetFsmProgr_Type=Gauge32
_CfprVnicProfileSetFsmProgr_Object=MibTableColumn
cfprVnicProfileSetFsmProgr=_CfprVnicProfileSetFsmProgr_Object((1,3,6,1,4,1,9,9,826,1,83,56,1,7),_CfprVnicProfileSetFsmProgr_Type())
cfprVnicProfileSetFsmProgr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicProfileSetFsmProgr.setStatus(_A)
_CfprVnicProfileSetFsmRmtInvErrCode_Type=Gauge32
_CfprVnicProfileSetFsmRmtInvErrCode_Object=MibTableColumn
cfprVnicProfileSetFsmRmtInvErrCode=_CfprVnicProfileSetFsmRmtInvErrCode_Object((1,3,6,1,4,1,9,9,826,1,83,56,1,8),_CfprVnicProfileSetFsmRmtInvErrCode_Type())
cfprVnicProfileSetFsmRmtInvErrCode.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicProfileSetFsmRmtInvErrCode.setStatus(_A)
_CfprVnicProfileSetFsmRmtInvErrDescr_Type=SnmpAdminString
_CfprVnicProfileSetFsmRmtInvErrDescr_Object=MibTableColumn
cfprVnicProfileSetFsmRmtInvErrDescr=_CfprVnicProfileSetFsmRmtInvErrDescr_Object((1,3,6,1,4,1,9,9,826,1,83,56,1,9),_CfprVnicProfileSetFsmRmtInvErrDescr_Type())
cfprVnicProfileSetFsmRmtInvErrDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicProfileSetFsmRmtInvErrDescr.setStatus(_A)
_CfprVnicProfileSetFsmRmtInvRslt_Type=CfprConditionRemoteInvRslt
_CfprVnicProfileSetFsmRmtInvRslt_Object=MibTableColumn
cfprVnicProfileSetFsmRmtInvRslt=_CfprVnicProfileSetFsmRmtInvRslt_Object((1,3,6,1,4,1,9,9,826,1,83,56,1,10),_CfprVnicProfileSetFsmRmtInvRslt_Type())
cfprVnicProfileSetFsmRmtInvRslt.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicProfileSetFsmRmtInvRslt.setStatus(_A)
_CfprVnicProfileSetFsmStageDescr_Type=SnmpAdminString
_CfprVnicProfileSetFsmStageDescr_Object=MibTableColumn
cfprVnicProfileSetFsmStageDescr=_CfprVnicProfileSetFsmStageDescr_Object((1,3,6,1,4,1,9,9,826,1,83,56,1,11),_CfprVnicProfileSetFsmStageDescr_Type())
cfprVnicProfileSetFsmStageDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicProfileSetFsmStageDescr.setStatus(_A)
_CfprVnicProfileSetFsmStamp_Type=DateAndTime
_CfprVnicProfileSetFsmStamp_Object=MibTableColumn
cfprVnicProfileSetFsmStamp=_CfprVnicProfileSetFsmStamp_Object((1,3,6,1,4,1,9,9,826,1,83,56,1,12),_CfprVnicProfileSetFsmStamp_Type())
cfprVnicProfileSetFsmStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicProfileSetFsmStamp.setStatus(_A)
_CfprVnicProfileSetFsmStatus_Type=SnmpAdminString
_CfprVnicProfileSetFsmStatus_Object=MibTableColumn
cfprVnicProfileSetFsmStatus=_CfprVnicProfileSetFsmStatus_Object((1,3,6,1,4,1,9,9,826,1,83,56,1,13),_CfprVnicProfileSetFsmStatus_Type())
cfprVnicProfileSetFsmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicProfileSetFsmStatus.setStatus(_A)
_CfprVnicProfileSetFsmTry_Type=Gauge32
_CfprVnicProfileSetFsmTry_Object=MibTableColumn
cfprVnicProfileSetFsmTry=_CfprVnicProfileSetFsmTry_Object((1,3,6,1,4,1,9,9,826,1,83,56,1,14),_CfprVnicProfileSetFsmTry_Type())
cfprVnicProfileSetFsmTry.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicProfileSetFsmTry.setStatus(_A)
_CfprVnicProfileSetGenNum_Type=Gauge32
_CfprVnicProfileSetGenNum_Object=MibTableColumn
cfprVnicProfileSetGenNum=_CfprVnicProfileSetGenNum_Object((1,3,6,1,4,1,9,9,826,1,83,56,1,15),_CfprVnicProfileSetGenNum_Type())
cfprVnicProfileSetGenNum.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicProfileSetGenNum.setStatus(_A)
_CfprVnicProfileSetFsmTable_Object=MibTable
cfprVnicProfileSetFsmTable=_CfprVnicProfileSetFsmTable_Object((1,3,6,1,4,1,9,9,826,1,83,57))
if mibBuilder.loadTexts:cfprVnicProfileSetFsmTable.setStatus(_A)
_CfprVnicProfileSetFsmEntry_Object=MibTableRow
cfprVnicProfileSetFsmEntry=_CfprVnicProfileSetFsmEntry_Object((1,3,6,1,4,1,9,9,826,1,83,57,1))
cfprVnicProfileSetFsmEntry.setIndexNames((0,_C,_A8))
if mibBuilder.loadTexts:cfprVnicProfileSetFsmEntry.setStatus(_A)
_CfprVnicProfileSetFsmInstanceId_Type=CfprManagedObjectId
_CfprVnicProfileSetFsmInstanceId_Object=MibTableColumn
cfprVnicProfileSetFsmInstanceId=_CfprVnicProfileSetFsmInstanceId_Object((1,3,6,1,4,1,9,9,826,1,83,57,1,1),_CfprVnicProfileSetFsmInstanceId_Type())
cfprVnicProfileSetFsmInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprVnicProfileSetFsmInstanceId.setStatus(_A)
_CfprVnicProfileSetFsmDn_Type=CfprManagedObjectDn
_CfprVnicProfileSetFsmDn_Object=MibTableColumn
cfprVnicProfileSetFsmDn=_CfprVnicProfileSetFsmDn_Object((1,3,6,1,4,1,9,9,826,1,83,57,1,2),_CfprVnicProfileSetFsmDn_Type())
cfprVnicProfileSetFsmDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicProfileSetFsmDn.setStatus(_A)
_CfprVnicProfileSetFsmRn_Type=SnmpAdminString
_CfprVnicProfileSetFsmRn_Object=MibTableColumn
cfprVnicProfileSetFsmRn=_CfprVnicProfileSetFsmRn_Object((1,3,6,1,4,1,9,9,826,1,83,57,1,3),_CfprVnicProfileSetFsmRn_Type())
cfprVnicProfileSetFsmRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicProfileSetFsmRn.setStatus(_A)
_CfprVnicProfileSetFsmCompletionTime_Type=DateAndTime
_CfprVnicProfileSetFsmCompletionTime_Object=MibTableColumn
cfprVnicProfileSetFsmCompletionTime=_CfprVnicProfileSetFsmCompletionTime_Object((1,3,6,1,4,1,9,9,826,1,83,57,1,4),_CfprVnicProfileSetFsmCompletionTime_Type())
cfprVnicProfileSetFsmCompletionTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicProfileSetFsmCompletionTime.setStatus(_A)
_CfprVnicProfileSetFsmCurrentFsm_Type=CfprVnicProfileSetFsmCurrentFsm
_CfprVnicProfileSetFsmCurrentFsm_Object=MibTableColumn
cfprVnicProfileSetFsmCurrentFsm=_CfprVnicProfileSetFsmCurrentFsm_Object((1,3,6,1,4,1,9,9,826,1,83,57,1,5),_CfprVnicProfileSetFsmCurrentFsm_Type())
cfprVnicProfileSetFsmCurrentFsm.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicProfileSetFsmCurrentFsm.setStatus(_A)
_CfprVnicProfileSetFsmDescrData_Type=SnmpAdminString
_CfprVnicProfileSetFsmDescrData_Object=MibTableColumn
cfprVnicProfileSetFsmDescrData=_CfprVnicProfileSetFsmDescrData_Object((1,3,6,1,4,1,9,9,826,1,83,57,1,6),_CfprVnicProfileSetFsmDescrData_Type())
cfprVnicProfileSetFsmDescrData.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicProfileSetFsmDescrData.setStatus(_A)
_CfprVnicProfileSetFsmFsmStatus_Type=CfprFsmFsmStageStatus
_CfprVnicProfileSetFsmFsmStatus_Object=MibTableColumn
cfprVnicProfileSetFsmFsmStatus=_CfprVnicProfileSetFsmFsmStatus_Object((1,3,6,1,4,1,9,9,826,1,83,57,1,7),_CfprVnicProfileSetFsmFsmStatus_Type())
cfprVnicProfileSetFsmFsmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicProfileSetFsmFsmStatus.setStatus(_A)
_CfprVnicProfileSetFsmProgress_Type=Gauge32
_CfprVnicProfileSetFsmProgress_Object=MibTableColumn
cfprVnicProfileSetFsmProgress=_CfprVnicProfileSetFsmProgress_Object((1,3,6,1,4,1,9,9,826,1,83,57,1,8),_CfprVnicProfileSetFsmProgress_Type())
cfprVnicProfileSetFsmProgress.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicProfileSetFsmProgress.setStatus(_A)
_CfprVnicProfileSetFsmRmtErrCode_Type=Gauge32
_CfprVnicProfileSetFsmRmtErrCode_Object=MibTableColumn
cfprVnicProfileSetFsmRmtErrCode=_CfprVnicProfileSetFsmRmtErrCode_Object((1,3,6,1,4,1,9,9,826,1,83,57,1,9),_CfprVnicProfileSetFsmRmtErrCode_Type())
cfprVnicProfileSetFsmRmtErrCode.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicProfileSetFsmRmtErrCode.setStatus(_A)
_CfprVnicProfileSetFsmRmtErrDescr_Type=SnmpAdminString
_CfprVnicProfileSetFsmRmtErrDescr_Object=MibTableColumn
cfprVnicProfileSetFsmRmtErrDescr=_CfprVnicProfileSetFsmRmtErrDescr_Object((1,3,6,1,4,1,9,9,826,1,83,57,1,10),_CfprVnicProfileSetFsmRmtErrDescr_Type())
cfprVnicProfileSetFsmRmtErrDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicProfileSetFsmRmtErrDescr.setStatus(_A)
_CfprVnicProfileSetFsmRmtRslt_Type=CfprConditionRemoteInvRslt
_CfprVnicProfileSetFsmRmtRslt_Object=MibTableColumn
cfprVnicProfileSetFsmRmtRslt=_CfprVnicProfileSetFsmRmtRslt_Object((1,3,6,1,4,1,9,9,826,1,83,57,1,11),_CfprVnicProfileSetFsmRmtRslt_Type())
cfprVnicProfileSetFsmRmtRslt.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicProfileSetFsmRmtRslt.setStatus(_A)
_CfprVnicProfileSetFsmStageTable_Object=MibTable
cfprVnicProfileSetFsmStageTable=_CfprVnicProfileSetFsmStageTable_Object((1,3,6,1,4,1,9,9,826,1,83,58))
if mibBuilder.loadTexts:cfprVnicProfileSetFsmStageTable.setStatus(_A)
_CfprVnicProfileSetFsmStageEntry_Object=MibTableRow
cfprVnicProfileSetFsmStageEntry=_CfprVnicProfileSetFsmStageEntry_Object((1,3,6,1,4,1,9,9,826,1,83,58,1))
cfprVnicProfileSetFsmStageEntry.setIndexNames((0,_C,_A9))
if mibBuilder.loadTexts:cfprVnicProfileSetFsmStageEntry.setStatus(_A)
_CfprVnicProfileSetFsmStageInstanceId_Type=CfprManagedObjectId
_CfprVnicProfileSetFsmStageInstanceId_Object=MibTableColumn
cfprVnicProfileSetFsmStageInstanceId=_CfprVnicProfileSetFsmStageInstanceId_Object((1,3,6,1,4,1,9,9,826,1,83,58,1,1),_CfprVnicProfileSetFsmStageInstanceId_Type())
cfprVnicProfileSetFsmStageInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprVnicProfileSetFsmStageInstanceId.setStatus(_A)
_CfprVnicProfileSetFsmStageDn_Type=CfprManagedObjectDn
_CfprVnicProfileSetFsmStageDn_Object=MibTableColumn
cfprVnicProfileSetFsmStageDn=_CfprVnicProfileSetFsmStageDn_Object((1,3,6,1,4,1,9,9,826,1,83,58,1,2),_CfprVnicProfileSetFsmStageDn_Type())
cfprVnicProfileSetFsmStageDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicProfileSetFsmStageDn.setStatus(_A)
_CfprVnicProfileSetFsmStageRn_Type=SnmpAdminString
_CfprVnicProfileSetFsmStageRn_Object=MibTableColumn
cfprVnicProfileSetFsmStageRn=_CfprVnicProfileSetFsmStageRn_Object((1,3,6,1,4,1,9,9,826,1,83,58,1,3),_CfprVnicProfileSetFsmStageRn_Type())
cfprVnicProfileSetFsmStageRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicProfileSetFsmStageRn.setStatus(_A)
_CfprVnicProfileSetFsmStageDescrData_Type=SnmpAdminString
_CfprVnicProfileSetFsmStageDescrData_Object=MibTableColumn
cfprVnicProfileSetFsmStageDescrData=_CfprVnicProfileSetFsmStageDescrData_Object((1,3,6,1,4,1,9,9,826,1,83,58,1,4),_CfprVnicProfileSetFsmStageDescrData_Type())
cfprVnicProfileSetFsmStageDescrData.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicProfileSetFsmStageDescrData.setStatus(_A)
_CfprVnicProfileSetFsmStageLastUpdateTime_Type=DateAndTime
_CfprVnicProfileSetFsmStageLastUpdateTime_Object=MibTableColumn
cfprVnicProfileSetFsmStageLastUpdateTime=_CfprVnicProfileSetFsmStageLastUpdateTime_Object((1,3,6,1,4,1,9,9,826,1,83,58,1,5),_CfprVnicProfileSetFsmStageLastUpdateTime_Type())
cfprVnicProfileSetFsmStageLastUpdateTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicProfileSetFsmStageLastUpdateTime.setStatus(_A)
_CfprVnicProfileSetFsmStageName_Type=CfprVnicProfileSetFsmStageName
_CfprVnicProfileSetFsmStageName_Object=MibTableColumn
cfprVnicProfileSetFsmStageName=_CfprVnicProfileSetFsmStageName_Object((1,3,6,1,4,1,9,9,826,1,83,58,1,6),_CfprVnicProfileSetFsmStageName_Type())
cfprVnicProfileSetFsmStageName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicProfileSetFsmStageName.setStatus(_A)
_CfprVnicProfileSetFsmStageOrder_Type=Gauge32
_CfprVnicProfileSetFsmStageOrder_Object=MibTableColumn
cfprVnicProfileSetFsmStageOrder=_CfprVnicProfileSetFsmStageOrder_Object((1,3,6,1,4,1,9,9,826,1,83,58,1,7),_CfprVnicProfileSetFsmStageOrder_Type())
cfprVnicProfileSetFsmStageOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicProfileSetFsmStageOrder.setStatus(_A)
_CfprVnicProfileSetFsmStageRetry_Type=Gauge32
_CfprVnicProfileSetFsmStageRetry_Object=MibTableColumn
cfprVnicProfileSetFsmStageRetry=_CfprVnicProfileSetFsmStageRetry_Object((1,3,6,1,4,1,9,9,826,1,83,58,1,8),_CfprVnicProfileSetFsmStageRetry_Type())
cfprVnicProfileSetFsmStageRetry.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicProfileSetFsmStageRetry.setStatus(_A)
_CfprVnicProfileSetFsmStageStageStatus_Type=CfprFsmFsmStageStatus
_CfprVnicProfileSetFsmStageStageStatus_Object=MibTableColumn
cfprVnicProfileSetFsmStageStageStatus=_CfprVnicProfileSetFsmStageStageStatus_Object((1,3,6,1,4,1,9,9,826,1,83,58,1,9),_CfprVnicProfileSetFsmStageStageStatus_Type())
cfprVnicProfileSetFsmStageStageStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicProfileSetFsmStageStageStatus.setStatus(_A)
_CfprVnicProfileSetFsmTaskTable_Object=MibTable
cfprVnicProfileSetFsmTaskTable=_CfprVnicProfileSetFsmTaskTable_Object((1,3,6,1,4,1,9,9,826,1,83,59))
if mibBuilder.loadTexts:cfprVnicProfileSetFsmTaskTable.setStatus(_A)
_CfprVnicProfileSetFsmTaskEntry_Object=MibTableRow
cfprVnicProfileSetFsmTaskEntry=_CfprVnicProfileSetFsmTaskEntry_Object((1,3,6,1,4,1,9,9,826,1,83,59,1))
cfprVnicProfileSetFsmTaskEntry.setIndexNames((0,_C,_AA))
if mibBuilder.loadTexts:cfprVnicProfileSetFsmTaskEntry.setStatus(_A)
_CfprVnicProfileSetFsmTaskInstanceId_Type=CfprManagedObjectId
_CfprVnicProfileSetFsmTaskInstanceId_Object=MibTableColumn
cfprVnicProfileSetFsmTaskInstanceId=_CfprVnicProfileSetFsmTaskInstanceId_Object((1,3,6,1,4,1,9,9,826,1,83,59,1,1),_CfprVnicProfileSetFsmTaskInstanceId_Type())
cfprVnicProfileSetFsmTaskInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprVnicProfileSetFsmTaskInstanceId.setStatus(_A)
_CfprVnicProfileSetFsmTaskDn_Type=CfprManagedObjectDn
_CfprVnicProfileSetFsmTaskDn_Object=MibTableColumn
cfprVnicProfileSetFsmTaskDn=_CfprVnicProfileSetFsmTaskDn_Object((1,3,6,1,4,1,9,9,826,1,83,59,1,2),_CfprVnicProfileSetFsmTaskDn_Type())
cfprVnicProfileSetFsmTaskDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicProfileSetFsmTaskDn.setStatus(_A)
_CfprVnicProfileSetFsmTaskRn_Type=SnmpAdminString
_CfprVnicProfileSetFsmTaskRn_Object=MibTableColumn
cfprVnicProfileSetFsmTaskRn=_CfprVnicProfileSetFsmTaskRn_Object((1,3,6,1,4,1,9,9,826,1,83,59,1,3),_CfprVnicProfileSetFsmTaskRn_Type())
cfprVnicProfileSetFsmTaskRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicProfileSetFsmTaskRn.setStatus(_A)
_CfprVnicProfileSetFsmTaskCompletion_Type=CfprFsmCompletion
_CfprVnicProfileSetFsmTaskCompletion_Object=MibTableColumn
cfprVnicProfileSetFsmTaskCompletion=_CfprVnicProfileSetFsmTaskCompletion_Object((1,3,6,1,4,1,9,9,826,1,83,59,1,4),_CfprVnicProfileSetFsmTaskCompletion_Type())
cfprVnicProfileSetFsmTaskCompletion.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicProfileSetFsmTaskCompletion.setStatus(_A)
_CfprVnicProfileSetFsmTaskFlags_Type=CfprFsmFlags
_CfprVnicProfileSetFsmTaskFlags_Object=MibTableColumn
cfprVnicProfileSetFsmTaskFlags=_CfprVnicProfileSetFsmTaskFlags_Object((1,3,6,1,4,1,9,9,826,1,83,59,1,5),_CfprVnicProfileSetFsmTaskFlags_Type())
cfprVnicProfileSetFsmTaskFlags.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicProfileSetFsmTaskFlags.setStatus(_A)
_CfprVnicProfileSetFsmTaskItem_Type=CfprVnicProfileSetFsmTaskItem
_CfprVnicProfileSetFsmTaskItem_Object=MibTableColumn
cfprVnicProfileSetFsmTaskItem=_CfprVnicProfileSetFsmTaskItem_Object((1,3,6,1,4,1,9,9,826,1,83,59,1,6),_CfprVnicProfileSetFsmTaskItem_Type())
cfprVnicProfileSetFsmTaskItem.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicProfileSetFsmTaskItem.setStatus(_A)
_CfprVnicProfileSetFsmTaskSeqId_Type=Gauge32
_CfprVnicProfileSetFsmTaskSeqId_Object=MibTableColumn
cfprVnicProfileSetFsmTaskSeqId=_CfprVnicProfileSetFsmTaskSeqId_Object((1,3,6,1,4,1,9,9,826,1,83,59,1,7),_CfprVnicProfileSetFsmTaskSeqId_Type())
cfprVnicProfileSetFsmTaskSeqId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicProfileSetFsmTaskSeqId.setStatus(_A)
_CfprVnicRackServerDiscoveryProfileTable_Object=MibTable
cfprVnicRackServerDiscoveryProfileTable=_CfprVnicRackServerDiscoveryProfileTable_Object((1,3,6,1,4,1,9,9,826,1,83,60))
if mibBuilder.loadTexts:cfprVnicRackServerDiscoveryProfileTable.setStatus(_A)
_CfprVnicRackServerDiscoveryProfileEntry_Object=MibTableRow
cfprVnicRackServerDiscoveryProfileEntry=_CfprVnicRackServerDiscoveryProfileEntry_Object((1,3,6,1,4,1,9,9,826,1,83,60,1))
cfprVnicRackServerDiscoveryProfileEntry.setIndexNames((0,_C,_AB))
if mibBuilder.loadTexts:cfprVnicRackServerDiscoveryProfileEntry.setStatus(_A)
_CfprVnicRackServerDiscoveryProfileInstanceId_Type=CfprManagedObjectId
_CfprVnicRackServerDiscoveryProfileInstanceId_Object=MibTableColumn
cfprVnicRackServerDiscoveryProfileInstanceId=_CfprVnicRackServerDiscoveryProfileInstanceId_Object((1,3,6,1,4,1,9,9,826,1,83,60,1,1),_CfprVnicRackServerDiscoveryProfileInstanceId_Type())
cfprVnicRackServerDiscoveryProfileInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprVnicRackServerDiscoveryProfileInstanceId.setStatus(_A)
_CfprVnicRackServerDiscoveryProfileDn_Type=CfprManagedObjectDn
_CfprVnicRackServerDiscoveryProfileDn_Object=MibTableColumn
cfprVnicRackServerDiscoveryProfileDn=_CfprVnicRackServerDiscoveryProfileDn_Object((1,3,6,1,4,1,9,9,826,1,83,60,1,2),_CfprVnicRackServerDiscoveryProfileDn_Type())
cfprVnicRackServerDiscoveryProfileDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicRackServerDiscoveryProfileDn.setStatus(_A)
_CfprVnicRackServerDiscoveryProfileRn_Type=SnmpAdminString
_CfprVnicRackServerDiscoveryProfileRn_Object=MibTableColumn
cfprVnicRackServerDiscoveryProfileRn=_CfprVnicRackServerDiscoveryProfileRn_Object((1,3,6,1,4,1,9,9,826,1,83,60,1,3),_CfprVnicRackServerDiscoveryProfileRn_Type())
cfprVnicRackServerDiscoveryProfileRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicRackServerDiscoveryProfileRn.setStatus(_A)
_CfprVnicRackServerDiscoveryProfileDescr_Type=SnmpAdminString
_CfprVnicRackServerDiscoveryProfileDescr_Object=MibTableColumn
cfprVnicRackServerDiscoveryProfileDescr=_CfprVnicRackServerDiscoveryProfileDescr_Object((1,3,6,1,4,1,9,9,826,1,83,60,1,4),_CfprVnicRackServerDiscoveryProfileDescr_Type())
cfprVnicRackServerDiscoveryProfileDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicRackServerDiscoveryProfileDescr.setStatus(_A)
_CfprVnicRackServerDiscoveryProfileIntId_Type=SnmpAdminString
_CfprVnicRackServerDiscoveryProfileIntId_Object=MibTableColumn
cfprVnicRackServerDiscoveryProfileIntId=_CfprVnicRackServerDiscoveryProfileIntId_Object((1,3,6,1,4,1,9,9,826,1,83,60,1,5),_CfprVnicRackServerDiscoveryProfileIntId_Type())
cfprVnicRackServerDiscoveryProfileIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicRackServerDiscoveryProfileIntId.setStatus(_A)
_CfprVnicRackServerDiscoveryProfileMaxPorts_Type=Gauge32
_CfprVnicRackServerDiscoveryProfileMaxPorts_Object=MibTableColumn
cfprVnicRackServerDiscoveryProfileMaxPorts=_CfprVnicRackServerDiscoveryProfileMaxPorts_Object((1,3,6,1,4,1,9,9,826,1,83,60,1,6),_CfprVnicRackServerDiscoveryProfileMaxPorts_Type())
cfprVnicRackServerDiscoveryProfileMaxPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicRackServerDiscoveryProfileMaxPorts.setStatus(_A)
_CfprVnicRackServerDiscoveryProfileName_Type=SnmpAdminString
_CfprVnicRackServerDiscoveryProfileName_Object=MibTableColumn
cfprVnicRackServerDiscoveryProfileName=_CfprVnicRackServerDiscoveryProfileName_Object((1,3,6,1,4,1,9,9,826,1,83,60,1,7),_CfprVnicRackServerDiscoveryProfileName_Type())
cfprVnicRackServerDiscoveryProfileName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicRackServerDiscoveryProfileName.setStatus(_A)
_CfprVnicRackServerDiscoveryProfilePolicyLevel_Type=Gauge32
_CfprVnicRackServerDiscoveryProfilePolicyLevel_Object=MibTableColumn
cfprVnicRackServerDiscoveryProfilePolicyLevel=_CfprVnicRackServerDiscoveryProfilePolicyLevel_Object((1,3,6,1,4,1,9,9,826,1,83,60,1,8),_CfprVnicRackServerDiscoveryProfilePolicyLevel_Type())
cfprVnicRackServerDiscoveryProfilePolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicRackServerDiscoveryProfilePolicyLevel.setStatus(_A)
_CfprVnicRackServerDiscoveryProfilePolicyOwner_Type=CfprPolicyPolicyOwner
_CfprVnicRackServerDiscoveryProfilePolicyOwner_Object=MibTableColumn
cfprVnicRackServerDiscoveryProfilePolicyOwner=_CfprVnicRackServerDiscoveryProfilePolicyOwner_Object((1,3,6,1,4,1,9,9,826,1,83,60,1,9),_CfprVnicRackServerDiscoveryProfilePolicyOwner_Type())
cfprVnicRackServerDiscoveryProfilePolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicRackServerDiscoveryProfilePolicyOwner.setStatus(_A)
_CfprVnicSanConnPolicyTable_Object=MibTable
cfprVnicSanConnPolicyTable=_CfprVnicSanConnPolicyTable_Object((1,3,6,1,4,1,9,9,826,1,83,61))
if mibBuilder.loadTexts:cfprVnicSanConnPolicyTable.setStatus(_A)
_CfprVnicSanConnPolicyEntry_Object=MibTableRow
cfprVnicSanConnPolicyEntry=_CfprVnicSanConnPolicyEntry_Object((1,3,6,1,4,1,9,9,826,1,83,61,1))
cfprVnicSanConnPolicyEntry.setIndexNames((0,_C,_AC))
if mibBuilder.loadTexts:cfprVnicSanConnPolicyEntry.setStatus(_A)
_CfprVnicSanConnPolicyInstanceId_Type=CfprManagedObjectId
_CfprVnicSanConnPolicyInstanceId_Object=MibTableColumn
cfprVnicSanConnPolicyInstanceId=_CfprVnicSanConnPolicyInstanceId_Object((1,3,6,1,4,1,9,9,826,1,83,61,1,1),_CfprVnicSanConnPolicyInstanceId_Type())
cfprVnicSanConnPolicyInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprVnicSanConnPolicyInstanceId.setStatus(_A)
_CfprVnicSanConnPolicyDn_Type=CfprManagedObjectDn
_CfprVnicSanConnPolicyDn_Object=MibTableColumn
cfprVnicSanConnPolicyDn=_CfprVnicSanConnPolicyDn_Object((1,3,6,1,4,1,9,9,826,1,83,61,1,2),_CfprVnicSanConnPolicyDn_Type())
cfprVnicSanConnPolicyDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicSanConnPolicyDn.setStatus(_A)
_CfprVnicSanConnPolicyRn_Type=SnmpAdminString
_CfprVnicSanConnPolicyRn_Object=MibTableColumn
cfprVnicSanConnPolicyRn=_CfprVnicSanConnPolicyRn_Object((1,3,6,1,4,1,9,9,826,1,83,61,1,3),_CfprVnicSanConnPolicyRn_Type())
cfprVnicSanConnPolicyRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicSanConnPolicyRn.setStatus(_A)
_CfprVnicSanConnPolicyDescr_Type=SnmpAdminString
_CfprVnicSanConnPolicyDescr_Object=MibTableColumn
cfprVnicSanConnPolicyDescr=_CfprVnicSanConnPolicyDescr_Object((1,3,6,1,4,1,9,9,826,1,83,61,1,4),_CfprVnicSanConnPolicyDescr_Type())
cfprVnicSanConnPolicyDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicSanConnPolicyDescr.setStatus(_A)
_CfprVnicSanConnPolicyFltAggr_Type=Unsigned64
_CfprVnicSanConnPolicyFltAggr_Object=MibTableColumn
cfprVnicSanConnPolicyFltAggr=_CfprVnicSanConnPolicyFltAggr_Object((1,3,6,1,4,1,9,9,826,1,83,61,1,5),_CfprVnicSanConnPolicyFltAggr_Type())
cfprVnicSanConnPolicyFltAggr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicSanConnPolicyFltAggr.setStatus(_A)
_CfprVnicSanConnPolicyIntId_Type=SnmpAdminString
_CfprVnicSanConnPolicyIntId_Object=MibTableColumn
cfprVnicSanConnPolicyIntId=_CfprVnicSanConnPolicyIntId_Object((1,3,6,1,4,1,9,9,826,1,83,61,1,6),_CfprVnicSanConnPolicyIntId_Type())
cfprVnicSanConnPolicyIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicSanConnPolicyIntId.setStatus(_A)
_CfprVnicSanConnPolicyName_Type=SnmpAdminString
_CfprVnicSanConnPolicyName_Object=MibTableColumn
cfprVnicSanConnPolicyName=_CfprVnicSanConnPolicyName_Object((1,3,6,1,4,1,9,9,826,1,83,61,1,7),_CfprVnicSanConnPolicyName_Type())
cfprVnicSanConnPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicSanConnPolicyName.setStatus(_A)
_CfprVnicSanConnPolicyPolicyLevel_Type=Gauge32
_CfprVnicSanConnPolicyPolicyLevel_Object=MibTableColumn
cfprVnicSanConnPolicyPolicyLevel=_CfprVnicSanConnPolicyPolicyLevel_Object((1,3,6,1,4,1,9,9,826,1,83,61,1,8),_CfprVnicSanConnPolicyPolicyLevel_Type())
cfprVnicSanConnPolicyPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicSanConnPolicyPolicyLevel.setStatus(_A)
_CfprVnicSanConnPolicyPolicyOwner_Type=CfprPolicyPolicyOwner
_CfprVnicSanConnPolicyPolicyOwner_Object=MibTableColumn
cfprVnicSanConnPolicyPolicyOwner=_CfprVnicSanConnPolicyPolicyOwner_Object((1,3,6,1,4,1,9,9,826,1,83,61,1,9),_CfprVnicSanConnPolicyPolicyOwner_Type())
cfprVnicSanConnPolicyPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicSanConnPolicyPolicyOwner.setStatus(_A)
_CfprVnicSanConnTemplTable_Object=MibTable
cfprVnicSanConnTemplTable=_CfprVnicSanConnTemplTable_Object((1,3,6,1,4,1,9,9,826,1,83,62))
if mibBuilder.loadTexts:cfprVnicSanConnTemplTable.setStatus(_A)
_CfprVnicSanConnTemplEntry_Object=MibTableRow
cfprVnicSanConnTemplEntry=_CfprVnicSanConnTemplEntry_Object((1,3,6,1,4,1,9,9,826,1,83,62,1))
cfprVnicSanConnTemplEntry.setIndexNames((0,_C,_AD))
if mibBuilder.loadTexts:cfprVnicSanConnTemplEntry.setStatus(_A)
_CfprVnicSanConnTemplInstanceId_Type=CfprManagedObjectId
_CfprVnicSanConnTemplInstanceId_Object=MibTableColumn
cfprVnicSanConnTemplInstanceId=_CfprVnicSanConnTemplInstanceId_Object((1,3,6,1,4,1,9,9,826,1,83,62,1,1),_CfprVnicSanConnTemplInstanceId_Type())
cfprVnicSanConnTemplInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprVnicSanConnTemplInstanceId.setStatus(_A)
_CfprVnicSanConnTemplDn_Type=CfprManagedObjectDn
_CfprVnicSanConnTemplDn_Object=MibTableColumn
cfprVnicSanConnTemplDn=_CfprVnicSanConnTemplDn_Object((1,3,6,1,4,1,9,9,826,1,83,62,1,2),_CfprVnicSanConnTemplDn_Type())
cfprVnicSanConnTemplDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicSanConnTemplDn.setStatus(_A)
_CfprVnicSanConnTemplRn_Type=SnmpAdminString
_CfprVnicSanConnTemplRn_Object=MibTableColumn
cfprVnicSanConnTemplRn=_CfprVnicSanConnTemplRn_Object((1,3,6,1,4,1,9,9,826,1,83,62,1,3),_CfprVnicSanConnTemplRn_Type())
cfprVnicSanConnTemplRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicSanConnTemplRn.setStatus(_A)
_CfprVnicSanConnTemplDescr_Type=SnmpAdminString
_CfprVnicSanConnTemplDescr_Object=MibTableColumn
cfprVnicSanConnTemplDescr=_CfprVnicSanConnTemplDescr_Object((1,3,6,1,4,1,9,9,826,1,83,62,1,4),_CfprVnicSanConnTemplDescr_Type())
cfprVnicSanConnTemplDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicSanConnTemplDescr.setStatus(_A)
_CfprVnicSanConnTemplIdentPoolName_Type=SnmpAdminString
_CfprVnicSanConnTemplIdentPoolName_Object=MibTableColumn
cfprVnicSanConnTemplIdentPoolName=_CfprVnicSanConnTemplIdentPoolName_Object((1,3,6,1,4,1,9,9,826,1,83,62,1,5),_CfprVnicSanConnTemplIdentPoolName_Type())
cfprVnicSanConnTemplIdentPoolName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicSanConnTemplIdentPoolName.setStatus(_A)
_CfprVnicSanConnTemplIntId_Type=SnmpAdminString
_CfprVnicSanConnTemplIntId_Object=MibTableColumn
cfprVnicSanConnTemplIntId=_CfprVnicSanConnTemplIntId_Object((1,3,6,1,4,1,9,9,826,1,83,62,1,6),_CfprVnicSanConnTemplIntId_Type())
cfprVnicSanConnTemplIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicSanConnTemplIntId.setStatus(_A)
_CfprVnicSanConnTemplMaxDataFieldSize_Type=Gauge32
_CfprVnicSanConnTemplMaxDataFieldSize_Object=MibTableColumn
cfprVnicSanConnTemplMaxDataFieldSize=_CfprVnicSanConnTemplMaxDataFieldSize_Object((1,3,6,1,4,1,9,9,826,1,83,62,1,7),_CfprVnicSanConnTemplMaxDataFieldSize_Type())
cfprVnicSanConnTemplMaxDataFieldSize.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicSanConnTemplMaxDataFieldSize.setStatus(_A)
_CfprVnicSanConnTemplName_Type=SnmpAdminString
_CfprVnicSanConnTemplName_Object=MibTableColumn
cfprVnicSanConnTemplName=_CfprVnicSanConnTemplName_Object((1,3,6,1,4,1,9,9,826,1,83,62,1,8),_CfprVnicSanConnTemplName_Type())
cfprVnicSanConnTemplName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicSanConnTemplName.setStatus(_A)
_CfprVnicSanConnTemplNwCtrlPolicyName_Type=SnmpAdminString
_CfprVnicSanConnTemplNwCtrlPolicyName_Object=MibTableColumn
cfprVnicSanConnTemplNwCtrlPolicyName=_CfprVnicSanConnTemplNwCtrlPolicyName_Object((1,3,6,1,4,1,9,9,826,1,83,62,1,9),_CfprVnicSanConnTemplNwCtrlPolicyName_Type())
cfprVnicSanConnTemplNwCtrlPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicSanConnTemplNwCtrlPolicyName.setStatus(_A)
_CfprVnicSanConnTemplOperIdentPoolName_Type=SnmpAdminString
_CfprVnicSanConnTemplOperIdentPoolName_Object=MibTableColumn
cfprVnicSanConnTemplOperIdentPoolName=_CfprVnicSanConnTemplOperIdentPoolName_Object((1,3,6,1,4,1,9,9,826,1,83,62,1,10),_CfprVnicSanConnTemplOperIdentPoolName_Type())
cfprVnicSanConnTemplOperIdentPoolName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicSanConnTemplOperIdentPoolName.setStatus(_A)
_CfprVnicSanConnTemplOperQosPolicyName_Type=SnmpAdminString
_CfprVnicSanConnTemplOperQosPolicyName_Object=MibTableColumn
cfprVnicSanConnTemplOperQosPolicyName=_CfprVnicSanConnTemplOperQosPolicyName_Object((1,3,6,1,4,1,9,9,826,1,83,62,1,11),_CfprVnicSanConnTemplOperQosPolicyName_Type())
cfprVnicSanConnTemplOperQosPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicSanConnTemplOperQosPolicyName.setStatus(_A)
_CfprVnicSanConnTemplOperStatsPolicyName_Type=SnmpAdminString
_CfprVnicSanConnTemplOperStatsPolicyName_Object=MibTableColumn
cfprVnicSanConnTemplOperStatsPolicyName=_CfprVnicSanConnTemplOperStatsPolicyName_Object((1,3,6,1,4,1,9,9,826,1,83,62,1,12),_CfprVnicSanConnTemplOperStatsPolicyName_Type())
cfprVnicSanConnTemplOperStatsPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicSanConnTemplOperStatsPolicyName.setStatus(_A)
_CfprVnicSanConnTemplPinToGroupName_Type=SnmpAdminString
_CfprVnicSanConnTemplPinToGroupName_Object=MibTableColumn
cfprVnicSanConnTemplPinToGroupName=_CfprVnicSanConnTemplPinToGroupName_Object((1,3,6,1,4,1,9,9,826,1,83,62,1,13),_CfprVnicSanConnTemplPinToGroupName_Type())
cfprVnicSanConnTemplPinToGroupName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicSanConnTemplPinToGroupName.setStatus(_A)
_CfprVnicSanConnTemplPolicyLevel_Type=Gauge32
_CfprVnicSanConnTemplPolicyLevel_Object=MibTableColumn
cfprVnicSanConnTemplPolicyLevel=_CfprVnicSanConnTemplPolicyLevel_Object((1,3,6,1,4,1,9,9,826,1,83,62,1,14),_CfprVnicSanConnTemplPolicyLevel_Type())
cfprVnicSanConnTemplPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicSanConnTemplPolicyLevel.setStatus(_A)
_CfprVnicSanConnTemplPolicyOwner_Type=CfprPolicyPolicyOwner
_CfprVnicSanConnTemplPolicyOwner_Object=MibTableColumn
cfprVnicSanConnTemplPolicyOwner=_CfprVnicSanConnTemplPolicyOwner_Object((1,3,6,1,4,1,9,9,826,1,83,62,1,15),_CfprVnicSanConnTemplPolicyOwner_Type())
cfprVnicSanConnTemplPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicSanConnTemplPolicyOwner.setStatus(_A)
_CfprVnicSanConnTemplQosPolicyName_Type=SnmpAdminString
_CfprVnicSanConnTemplQosPolicyName_Object=MibTableColumn
cfprVnicSanConnTemplQosPolicyName=_CfprVnicSanConnTemplQosPolicyName_Object((1,3,6,1,4,1,9,9,826,1,83,62,1,16),_CfprVnicSanConnTemplQosPolicyName_Type())
cfprVnicSanConnTemplQosPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicSanConnTemplQosPolicyName.setStatus(_A)
_CfprVnicSanConnTemplStatsPolicyName_Type=SnmpAdminString
_CfprVnicSanConnTemplStatsPolicyName_Object=MibTableColumn
cfprVnicSanConnTemplStatsPolicyName=_CfprVnicSanConnTemplStatsPolicyName_Object((1,3,6,1,4,1,9,9,826,1,83,62,1,17),_CfprVnicSanConnTemplStatsPolicyName_Type())
cfprVnicSanConnTemplStatsPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicSanConnTemplStatsPolicyName.setStatus(_A)
_CfprVnicSanConnTemplSwitchId_Type=CfprNetworkSwitchId
_CfprVnicSanConnTemplSwitchId_Object=MibTableColumn
cfprVnicSanConnTemplSwitchId=_CfprVnicSanConnTemplSwitchId_Object((1,3,6,1,4,1,9,9,826,1,83,62,1,18),_CfprVnicSanConnTemplSwitchId_Type())
cfprVnicSanConnTemplSwitchId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicSanConnTemplSwitchId.setStatus(_A)
_CfprVnicSanConnTemplTarget_Type=CfprVnicSanConnTemplTarget
_CfprVnicSanConnTemplTarget_Object=MibTableColumn
cfprVnicSanConnTemplTarget=_CfprVnicSanConnTemplTarget_Object((1,3,6,1,4,1,9,9,826,1,83,62,1,19),_CfprVnicSanConnTemplTarget_Type())
cfprVnicSanConnTemplTarget.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicSanConnTemplTarget.setStatus(_A)
_CfprVnicSanConnTemplTemplType_Type=CfprVnicTemplateType
_CfprVnicSanConnTemplTemplType_Object=MibTableColumn
cfprVnicSanConnTemplTemplType=_CfprVnicSanConnTemplTemplType_Object((1,3,6,1,4,1,9,9,826,1,83,62,1,20),_CfprVnicSanConnTemplTemplType_Type())
cfprVnicSanConnTemplTemplType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicSanConnTemplTemplType.setStatus(_A)
_CfprVnicScsiTable_Object=MibTable
cfprVnicScsiTable=_CfprVnicScsiTable_Object((1,3,6,1,4,1,9,9,826,1,83,63))
if mibBuilder.loadTexts:cfprVnicScsiTable.setStatus(_A)
_CfprVnicScsiEntry_Object=MibTableRow
cfprVnicScsiEntry=_CfprVnicScsiEntry_Object((1,3,6,1,4,1,9,9,826,1,83,63,1))
cfprVnicScsiEntry.setIndexNames((0,_C,_AE))
if mibBuilder.loadTexts:cfprVnicScsiEntry.setStatus(_A)
_CfprVnicScsiInstanceId_Type=CfprManagedObjectId
_CfprVnicScsiInstanceId_Object=MibTableColumn
cfprVnicScsiInstanceId=_CfprVnicScsiInstanceId_Object((1,3,6,1,4,1,9,9,826,1,83,63,1,1),_CfprVnicScsiInstanceId_Type())
cfprVnicScsiInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprVnicScsiInstanceId.setStatus(_A)
_CfprVnicScsiDn_Type=CfprManagedObjectDn
_CfprVnicScsiDn_Object=MibTableColumn
cfprVnicScsiDn=_CfprVnicScsiDn_Object((1,3,6,1,4,1,9,9,826,1,83,63,1,2),_CfprVnicScsiDn_Type())
cfprVnicScsiDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicScsiDn.setStatus(_A)
_CfprVnicScsiRn_Type=SnmpAdminString
_CfprVnicScsiRn_Object=MibTableColumn
cfprVnicScsiRn=_CfprVnicScsiRn_Object((1,3,6,1,4,1,9,9,826,1,83,63,1,3),_CfprVnicScsiRn_Type())
cfprVnicScsiRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicScsiRn.setStatus(_A)
_CfprVnicScsiAdaptorProfileName_Type=SnmpAdminString
_CfprVnicScsiAdaptorProfileName_Object=MibTableColumn
cfprVnicScsiAdaptorProfileName=_CfprVnicScsiAdaptorProfileName_Object((1,3,6,1,4,1,9,9,826,1,83,63,1,4),_CfprVnicScsiAdaptorProfileName_Type())
cfprVnicScsiAdaptorProfileName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicScsiAdaptorProfileName.setStatus(_A)
_CfprVnicScsiAdminHostPort_Type=CfprFabricHostPortId
_CfprVnicScsiAdminHostPort_Object=MibTableColumn
cfprVnicScsiAdminHostPort=_CfprVnicScsiAdminHostPort_Object((1,3,6,1,4,1,9,9,826,1,83,63,1,5),_CfprVnicScsiAdminHostPort_Type())
cfprVnicScsiAdminHostPort.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicScsiAdminHostPort.setStatus(_A)
_CfprVnicScsiAdminVcon_Type=SnmpAdminString
_CfprVnicScsiAdminVcon_Object=MibTableColumn
cfprVnicScsiAdminVcon=_CfprVnicScsiAdminVcon_Object((1,3,6,1,4,1,9,9,826,1,83,63,1,6),_CfprVnicScsiAdminVcon_Type())
cfprVnicScsiAdminVcon.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicScsiAdminVcon.setStatus(_A)
_CfprVnicScsiAppRole_Type=CfprVnicAppRole
_CfprVnicScsiAppRole_Object=MibTableColumn
cfprVnicScsiAppRole=_CfprVnicScsiAppRole_Object((1,3,6,1,4,1,9,9,826,1,83,63,1,7),_CfprVnicScsiAppRole_Type())
cfprVnicScsiAppRole.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicScsiAppRole.setStatus(_A)
_CfprVnicScsiBootDev_Type=CfprVnicVnicBootDev
_CfprVnicScsiBootDev_Object=MibTableColumn
cfprVnicScsiBootDev=_CfprVnicScsiBootDev_Object((1,3,6,1,4,1,9,9,826,1,83,63,1,8),_CfprVnicScsiBootDev_Type())
cfprVnicScsiBootDev.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicScsiBootDev.setStatus(_A)
_CfprVnicScsiConfigQualifier_Type=CfprVnicConfigIssues
_CfprVnicScsiConfigQualifier_Object=MibTableColumn
cfprVnicScsiConfigQualifier=_CfprVnicScsiConfigQualifier_Object((1,3,6,1,4,1,9,9,826,1,83,63,1,9),_CfprVnicScsiConfigQualifier_Type())
cfprVnicScsiConfigQualifier.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicScsiConfigQualifier.setStatus(_A)
_CfprVnicScsiConfigState_Type=CfprLsConfigState
_CfprVnicScsiConfigState_Object=MibTableColumn
cfprVnicScsiConfigState=_CfprVnicScsiConfigState_Object((1,3,6,1,4,1,9,9,826,1,83,63,1,10),_CfprVnicScsiConfigState_Type())
cfprVnicScsiConfigState.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicScsiConfigState.setStatus(_A)
_CfprVnicScsiEquipmentDn_Type=SnmpAdminString
_CfprVnicScsiEquipmentDn_Object=MibTableColumn
cfprVnicScsiEquipmentDn=_CfprVnicScsiEquipmentDn_Object((1,3,6,1,4,1,9,9,826,1,83,63,1,11),_CfprVnicScsiEquipmentDn_Type())
cfprVnicScsiEquipmentDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicScsiEquipmentDn.setStatus(_A)
_CfprVnicScsiIdentPoolName_Type=SnmpAdminString
_CfprVnicScsiIdentPoolName_Object=MibTableColumn
cfprVnicScsiIdentPoolName=_CfprVnicScsiIdentPoolName_Object((1,3,6,1,4,1,9,9,826,1,83,63,1,12),_CfprVnicScsiIdentPoolName_Type())
cfprVnicScsiIdentPoolName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicScsiIdentPoolName.setStatus(_A)
_CfprVnicScsiInstType_Type=CfprVnicInstantiation
_CfprVnicScsiInstType_Object=MibTableColumn
cfprVnicScsiInstType=_CfprVnicScsiInstType_Object((1,3,6,1,4,1,9,9,826,1,83,63,1,13),_CfprVnicScsiInstType_Type())
cfprVnicScsiInstType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicScsiInstType.setStatus(_A)
_CfprVnicScsiName_Type=SnmpAdminString
_CfprVnicScsiName_Object=MibTableColumn
cfprVnicScsiName=_CfprVnicScsiName_Object((1,3,6,1,4,1,9,9,826,1,83,63,1,14),_CfprVnicScsiName_Type())
cfprVnicScsiName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicScsiName.setStatus(_A)
_CfprVnicScsiNwTemplName_Type=SnmpAdminString
_CfprVnicScsiNwTemplName_Object=MibTableColumn
cfprVnicScsiNwTemplName=_CfprVnicScsiNwTemplName_Object((1,3,6,1,4,1,9,9,826,1,83,63,1,15),_CfprVnicScsiNwTemplName_Type())
cfprVnicScsiNwTemplName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicScsiNwTemplName.setStatus(_A)
_CfprVnicScsiOperHostPort_Type=CfprVnicVnicOperHostPort
_CfprVnicScsiOperHostPort_Object=MibTableColumn
cfprVnicScsiOperHostPort=_CfprVnicScsiOperHostPort_Object((1,3,6,1,4,1,9,9,826,1,83,63,1,16),_CfprVnicScsiOperHostPort_Type())
cfprVnicScsiOperHostPort.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicScsiOperHostPort.setStatus(_A)
_CfprVnicScsiOperOrder_Type=Gauge32
_CfprVnicScsiOperOrder_Object=MibTableColumn
cfprVnicScsiOperOrder=_CfprVnicScsiOperOrder_Object((1,3,6,1,4,1,9,9,826,1,83,63,1,17),_CfprVnicScsiOperOrder_Type())
cfprVnicScsiOperOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicScsiOperOrder.setStatus(_A)
_CfprVnicScsiOperSpeed_Type=Gauge32
_CfprVnicScsiOperSpeed_Object=MibTableColumn
cfprVnicScsiOperSpeed=_CfprVnicScsiOperSpeed_Object((1,3,6,1,4,1,9,9,826,1,83,63,1,18),_CfprVnicScsiOperSpeed_Type())
cfprVnicScsiOperSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicScsiOperSpeed.setStatus(_A)
_CfprVnicScsiOperStatsPolicyName_Type=SnmpAdminString
_CfprVnicScsiOperStatsPolicyName_Object=MibTableColumn
cfprVnicScsiOperStatsPolicyName=_CfprVnicScsiOperStatsPolicyName_Object((1,3,6,1,4,1,9,9,826,1,83,63,1,19),_CfprVnicScsiOperStatsPolicyName_Type())
cfprVnicScsiOperStatsPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicScsiOperStatsPolicyName.setStatus(_A)
_CfprVnicScsiOperVcon_Type=SnmpAdminString
_CfprVnicScsiOperVcon_Object=MibTableColumn
cfprVnicScsiOperVcon=_CfprVnicScsiOperVcon_Object((1,3,6,1,4,1,9,9,826,1,83,63,1,20),_CfprVnicScsiOperVcon_Type())
cfprVnicScsiOperVcon.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicScsiOperVcon.setStatus(_A)
_CfprVnicScsiOrder_Type=Gauge32
_CfprVnicScsiOrder_Object=MibTableColumn
cfprVnicScsiOrder=_CfprVnicScsiOrder_Object((1,3,6,1,4,1,9,9,826,1,83,63,1,21),_CfprVnicScsiOrder_Type())
cfprVnicScsiOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicScsiOrder.setStatus(_A)
_CfprVnicScsiOwner_Type=CfprVnicConnectionOwner
_CfprVnicScsiOwner_Object=MibTableColumn
cfprVnicScsiOwner=_CfprVnicScsiOwner_Object((1,3,6,1,4,1,9,9,826,1,83,63,1,22),_CfprVnicScsiOwner_Type())
cfprVnicScsiOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicScsiOwner.setStatus(_A)
_CfprVnicScsiPinToGroupName_Type=SnmpAdminString
_CfprVnicScsiPinToGroupName_Object=MibTableColumn
cfprVnicScsiPinToGroupName=_CfprVnicScsiPinToGroupName_Object((1,3,6,1,4,1,9,9,826,1,83,63,1,23),_CfprVnicScsiPinToGroupName_Type())
cfprVnicScsiPinToGroupName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicScsiPinToGroupName.setStatus(_A)
_CfprVnicScsiQosPolicyName_Type=SnmpAdminString
_CfprVnicScsiQosPolicyName_Object=MibTableColumn
cfprVnicScsiQosPolicyName=_CfprVnicScsiQosPolicyName_Object((1,3,6,1,4,1,9,9,826,1,83,63,1,24),_CfprVnicScsiQosPolicyName_Type())
cfprVnicScsiQosPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicScsiQosPolicyName.setStatus(_A)
_CfprVnicScsiStatsPolicyName_Type=SnmpAdminString
_CfprVnicScsiStatsPolicyName_Object=MibTableColumn
cfprVnicScsiStatsPolicyName=_CfprVnicScsiStatsPolicyName_Object((1,3,6,1,4,1,9,9,826,1,83,63,1,25),_CfprVnicScsiStatsPolicyName_Type())
cfprVnicScsiStatsPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicScsiStatsPolicyName.setStatus(_A)
_CfprVnicScsiSwitchId_Type=CfprNetworkSwitchId
_CfprVnicScsiSwitchId_Object=MibTableColumn
cfprVnicScsiSwitchId=_CfprVnicScsiSwitchId_Object((1,3,6,1,4,1,9,9,826,1,83,63,1,26),_CfprVnicScsiSwitchId_Type())
cfprVnicScsiSwitchId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicScsiSwitchId.setStatus(_A)
_CfprVnicScsiType_Type=CfprVnicScsiType
_CfprVnicScsiType_Object=MibTableColumn
cfprVnicScsiType=_CfprVnicScsiType_Object((1,3,6,1,4,1,9,9,826,1,83,63,1,27),_CfprVnicScsiType_Type())
cfprVnicScsiType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicScsiType.setStatus(_A)
_CfprVnicScsiIfTable_Object=MibTable
cfprVnicScsiIfTable=_CfprVnicScsiIfTable_Object((1,3,6,1,4,1,9,9,826,1,83,64))
if mibBuilder.loadTexts:cfprVnicScsiIfTable.setStatus(_A)
_CfprVnicScsiIfEntry_Object=MibTableRow
cfprVnicScsiIfEntry=_CfprVnicScsiIfEntry_Object((1,3,6,1,4,1,9,9,826,1,83,64,1))
cfprVnicScsiIfEntry.setIndexNames((0,_C,_AF))
if mibBuilder.loadTexts:cfprVnicScsiIfEntry.setStatus(_A)
_CfprVnicScsiIfInstanceId_Type=CfprManagedObjectId
_CfprVnicScsiIfInstanceId_Object=MibTableColumn
cfprVnicScsiIfInstanceId=_CfprVnicScsiIfInstanceId_Object((1,3,6,1,4,1,9,9,826,1,83,64,1,1),_CfprVnicScsiIfInstanceId_Type())
cfprVnicScsiIfInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprVnicScsiIfInstanceId.setStatus(_A)
_CfprVnicScsiIfDn_Type=CfprManagedObjectDn
_CfprVnicScsiIfDn_Object=MibTableColumn
cfprVnicScsiIfDn=_CfprVnicScsiIfDn_Object((1,3,6,1,4,1,9,9,826,1,83,64,1,2),_CfprVnicScsiIfDn_Type())
cfprVnicScsiIfDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicScsiIfDn.setStatus(_A)
_CfprVnicScsiIfRn_Type=SnmpAdminString
_CfprVnicScsiIfRn_Object=MibTableColumn
cfprVnicScsiIfRn=_CfprVnicScsiIfRn_Object((1,3,6,1,4,1,9,9,826,1,83,64,1,3),_CfprVnicScsiIfRn_Type())
cfprVnicScsiIfRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicScsiIfRn.setStatus(_A)
_CfprVnicScsiIfAddr_Type=Unsigned64
_CfprVnicScsiIfAddr_Object=MibTableColumn
cfprVnicScsiIfAddr=_CfprVnicScsiIfAddr_Object((1,3,6,1,4,1,9,9,826,1,83,64,1,4),_CfprVnicScsiIfAddr_Type())
cfprVnicScsiIfAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicScsiIfAddr.setStatus(_A)
_CfprVnicScsiIfConfigQualifier_Type=CfprVnicConfigIssues
_CfprVnicScsiIfConfigQualifier_Object=MibTableColumn
cfprVnicScsiIfConfigQualifier=_CfprVnicScsiIfConfigQualifier_Object((1,3,6,1,4,1,9,9,826,1,83,64,1,5),_CfprVnicScsiIfConfigQualifier_Type())
cfprVnicScsiIfConfigQualifier.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicScsiIfConfigQualifier.setStatus(_A)
_CfprVnicScsiIfName_Type=SnmpAdminString
_CfprVnicScsiIfName_Object=MibTableColumn
cfprVnicScsiIfName=_CfprVnicScsiIfName_Object((1,3,6,1,4,1,9,9,826,1,83,64,1,6),_CfprVnicScsiIfName_Type())
cfprVnicScsiIfName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicScsiIfName.setStatus(_A)
_CfprVnicScsiIfOperState_Type=CfprVnicIfOperState
_CfprVnicScsiIfOperState_Object=MibTableColumn
cfprVnicScsiIfOperState=_CfprVnicScsiIfOperState_Object((1,3,6,1,4,1,9,9,826,1,83,64,1,7),_CfprVnicScsiIfOperState_Type())
cfprVnicScsiIfOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicScsiIfOperState.setStatus(_A)
_CfprVnicScsiIfOperVnetDn_Type=SnmpAdminString
_CfprVnicScsiIfOperVnetDn_Object=MibTableColumn
cfprVnicScsiIfOperVnetDn=_CfprVnicScsiIfOperVnetDn_Object((1,3,6,1,4,1,9,9,826,1,83,64,1,8),_CfprVnicScsiIfOperVnetDn_Type())
cfprVnicScsiIfOperVnetDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicScsiIfOperVnetDn.setStatus(_A)
_CfprVnicScsiIfOperVnetName_Type=SnmpAdminString
_CfprVnicScsiIfOperVnetName_Object=MibTableColumn
cfprVnicScsiIfOperVnetName=_CfprVnicScsiIfOperVnetName_Object((1,3,6,1,4,1,9,9,826,1,83,64,1,9),_CfprVnicScsiIfOperVnetName_Type())
cfprVnicScsiIfOperVnetName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicScsiIfOperVnetName.setStatus(_A)
_CfprVnicScsiIfOwner_Type=CfprVnicConnectionOwner
_CfprVnicScsiIfOwner_Object=MibTableColumn
cfprVnicScsiIfOwner=_CfprVnicScsiIfOwner_Object((1,3,6,1,4,1,9,9,826,1,83,64,1,10),_CfprVnicScsiIfOwner_Type())
cfprVnicScsiIfOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicScsiIfOwner.setStatus(_A)
_CfprVnicScsiIfPubNwId_Type=Gauge32
_CfprVnicScsiIfPubNwId_Object=MibTableColumn
cfprVnicScsiIfPubNwId=_CfprVnicScsiIfPubNwId_Object((1,3,6,1,4,1,9,9,826,1,83,64,1,11),_CfprVnicScsiIfPubNwId_Type())
cfprVnicScsiIfPubNwId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicScsiIfPubNwId.setStatus(_A)
_CfprVnicScsiIfSharing_Type=CfprFabricVlanSharingType
_CfprVnicScsiIfSharing_Object=MibTableColumn
cfprVnicScsiIfSharing=_CfprVnicScsiIfSharing_Object((1,3,6,1,4,1,9,9,826,1,83,64,1,12),_CfprVnicScsiIfSharing_Type())
cfprVnicScsiIfSharing.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicScsiIfSharing.setStatus(_A)
_CfprVnicScsiIfSwitchId_Type=CfprNetworkSwitchId
_CfprVnicScsiIfSwitchId_Object=MibTableColumn
cfprVnicScsiIfSwitchId=_CfprVnicScsiIfSwitchId_Object((1,3,6,1,4,1,9,9,826,1,83,64,1,13),_CfprVnicScsiIfSwitchId_Type())
cfprVnicScsiIfSwitchId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicScsiIfSwitchId.setStatus(_A)
_CfprVnicScsiIfType_Type=CfprVnicAScsiIfType
_CfprVnicScsiIfType_Object=MibTableColumn
cfprVnicScsiIfType=_CfprVnicScsiIfType_Object((1,3,6,1,4,1,9,9,826,1,83,64,1,14),_CfprVnicScsiIfType_Type())
cfprVnicScsiIfType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicScsiIfType.setStatus(_A)
_CfprVnicScsiIfVnet_Type=Gauge32
_CfprVnicScsiIfVnet_Object=MibTableColumn
cfprVnicScsiIfVnet=_CfprVnicScsiIfVnet_Object((1,3,6,1,4,1,9,9,826,1,83,64,1,15),_CfprVnicScsiIfVnet_Type())
cfprVnicScsiIfVnet.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicScsiIfVnet.setStatus(_A)
_CfprVnicUsnicConPolicyTable_Object=MibTable
cfprVnicUsnicConPolicyTable=_CfprVnicUsnicConPolicyTable_Object((1,3,6,1,4,1,9,9,826,1,83,65))
if mibBuilder.loadTexts:cfprVnicUsnicConPolicyTable.setStatus(_A)
_CfprVnicUsnicConPolicyEntry_Object=MibTableRow
cfprVnicUsnicConPolicyEntry=_CfprVnicUsnicConPolicyEntry_Object((1,3,6,1,4,1,9,9,826,1,83,65,1))
cfprVnicUsnicConPolicyEntry.setIndexNames((0,_C,_AG))
if mibBuilder.loadTexts:cfprVnicUsnicConPolicyEntry.setStatus(_A)
_CfprVnicUsnicConPolicyInstanceId_Type=CfprManagedObjectId
_CfprVnicUsnicConPolicyInstanceId_Object=MibTableColumn
cfprVnicUsnicConPolicyInstanceId=_CfprVnicUsnicConPolicyInstanceId_Object((1,3,6,1,4,1,9,9,826,1,83,65,1,1),_CfprVnicUsnicConPolicyInstanceId_Type())
cfprVnicUsnicConPolicyInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprVnicUsnicConPolicyInstanceId.setStatus(_A)
_CfprVnicUsnicConPolicyDn_Type=CfprManagedObjectDn
_CfprVnicUsnicConPolicyDn_Object=MibTableColumn
cfprVnicUsnicConPolicyDn=_CfprVnicUsnicConPolicyDn_Object((1,3,6,1,4,1,9,9,826,1,83,65,1,2),_CfprVnicUsnicConPolicyDn_Type())
cfprVnicUsnicConPolicyDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicUsnicConPolicyDn.setStatus(_A)
_CfprVnicUsnicConPolicyRn_Type=SnmpAdminString
_CfprVnicUsnicConPolicyRn_Object=MibTableColumn
cfprVnicUsnicConPolicyRn=_CfprVnicUsnicConPolicyRn_Object((1,3,6,1,4,1,9,9,826,1,83,65,1,3),_CfprVnicUsnicConPolicyRn_Type())
cfprVnicUsnicConPolicyRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicUsnicConPolicyRn.setStatus(_A)
_CfprVnicUsnicConPolicyAdaptorProfileName_Type=SnmpAdminString
_CfprVnicUsnicConPolicyAdaptorProfileName_Object=MibTableColumn
cfprVnicUsnicConPolicyAdaptorProfileName=_CfprVnicUsnicConPolicyAdaptorProfileName_Object((1,3,6,1,4,1,9,9,826,1,83,65,1,4),_CfprVnicUsnicConPolicyAdaptorProfileName_Type())
cfprVnicUsnicConPolicyAdaptorProfileName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicUsnicConPolicyAdaptorProfileName.setStatus(_A)
_CfprVnicUsnicConPolicyDescr_Type=SnmpAdminString
_CfprVnicUsnicConPolicyDescr_Object=MibTableColumn
cfprVnicUsnicConPolicyDescr=_CfprVnicUsnicConPolicyDescr_Object((1,3,6,1,4,1,9,9,826,1,83,65,1,5),_CfprVnicUsnicConPolicyDescr_Type())
cfprVnicUsnicConPolicyDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicUsnicConPolicyDescr.setStatus(_A)
_CfprVnicUsnicConPolicyIntId_Type=SnmpAdminString
_CfprVnicUsnicConPolicyIntId_Object=MibTableColumn
cfprVnicUsnicConPolicyIntId=_CfprVnicUsnicConPolicyIntId_Object((1,3,6,1,4,1,9,9,826,1,83,65,1,6),_CfprVnicUsnicConPolicyIntId_Type())
cfprVnicUsnicConPolicyIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicUsnicConPolicyIntId.setStatus(_A)
_CfprVnicUsnicConPolicyName_Type=SnmpAdminString
_CfprVnicUsnicConPolicyName_Object=MibTableColumn
cfprVnicUsnicConPolicyName=_CfprVnicUsnicConPolicyName_Object((1,3,6,1,4,1,9,9,826,1,83,65,1,7),_CfprVnicUsnicConPolicyName_Type())
cfprVnicUsnicConPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicUsnicConPolicyName.setStatus(_A)
_CfprVnicUsnicConPolicyPolicyLevel_Type=Gauge32
_CfprVnicUsnicConPolicyPolicyLevel_Object=MibTableColumn
cfprVnicUsnicConPolicyPolicyLevel=_CfprVnicUsnicConPolicyPolicyLevel_Object((1,3,6,1,4,1,9,9,826,1,83,65,1,8),_CfprVnicUsnicConPolicyPolicyLevel_Type())
cfprVnicUsnicConPolicyPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicUsnicConPolicyPolicyLevel.setStatus(_A)
_CfprVnicUsnicConPolicyPolicyOwner_Type=CfprPolicyPolicyOwner
_CfprVnicUsnicConPolicyPolicyOwner_Object=MibTableColumn
cfprVnicUsnicConPolicyPolicyOwner=_CfprVnicUsnicConPolicyPolicyOwner_Object((1,3,6,1,4,1,9,9,826,1,83,65,1,9),_CfprVnicUsnicConPolicyPolicyOwner_Type())
cfprVnicUsnicConPolicyPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicUsnicConPolicyPolicyOwner.setStatus(_A)
_CfprVnicUsnicConPolicyUsnicCount_Type=Gauge32
_CfprVnicUsnicConPolicyUsnicCount_Object=MibTableColumn
cfprVnicUsnicConPolicyUsnicCount=_CfprVnicUsnicConPolicyUsnicCount_Object((1,3,6,1,4,1,9,9,826,1,83,65,1,10),_CfprVnicUsnicConPolicyUsnicCount_Type())
cfprVnicUsnicConPolicyUsnicCount.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicUsnicConPolicyUsnicCount.setStatus(_A)
_CfprVnicUsnicConPolicyRefTable_Object=MibTable
cfprVnicUsnicConPolicyRefTable=_CfprVnicUsnicConPolicyRefTable_Object((1,3,6,1,4,1,9,9,826,1,83,66))
if mibBuilder.loadTexts:cfprVnicUsnicConPolicyRefTable.setStatus(_A)
_CfprVnicUsnicConPolicyRefEntry_Object=MibTableRow
cfprVnicUsnicConPolicyRefEntry=_CfprVnicUsnicConPolicyRefEntry_Object((1,3,6,1,4,1,9,9,826,1,83,66,1))
cfprVnicUsnicConPolicyRefEntry.setIndexNames((0,_C,_AH))
if mibBuilder.loadTexts:cfprVnicUsnicConPolicyRefEntry.setStatus(_A)
_CfprVnicUsnicConPolicyRefInstanceId_Type=CfprManagedObjectId
_CfprVnicUsnicConPolicyRefInstanceId_Object=MibTableColumn
cfprVnicUsnicConPolicyRefInstanceId=_CfprVnicUsnicConPolicyRefInstanceId_Object((1,3,6,1,4,1,9,9,826,1,83,66,1,1),_CfprVnicUsnicConPolicyRefInstanceId_Type())
cfprVnicUsnicConPolicyRefInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprVnicUsnicConPolicyRefInstanceId.setStatus(_A)
_CfprVnicUsnicConPolicyRefDn_Type=CfprManagedObjectDn
_CfprVnicUsnicConPolicyRefDn_Object=MibTableColumn
cfprVnicUsnicConPolicyRefDn=_CfprVnicUsnicConPolicyRefDn_Object((1,3,6,1,4,1,9,9,826,1,83,66,1,2),_CfprVnicUsnicConPolicyRefDn_Type())
cfprVnicUsnicConPolicyRefDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicUsnicConPolicyRefDn.setStatus(_A)
_CfprVnicUsnicConPolicyRefRn_Type=SnmpAdminString
_CfprVnicUsnicConPolicyRefRn_Object=MibTableColumn
cfprVnicUsnicConPolicyRefRn=_CfprVnicUsnicConPolicyRefRn_Object((1,3,6,1,4,1,9,9,826,1,83,66,1,3),_CfprVnicUsnicConPolicyRefRn_Type())
cfprVnicUsnicConPolicyRefRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicUsnicConPolicyRefRn.setStatus(_A)
_CfprVnicUsnicConPolicyRefConPolicyName_Type=SnmpAdminString
_CfprVnicUsnicConPolicyRefConPolicyName_Object=MibTableColumn
cfprVnicUsnicConPolicyRefConPolicyName=_CfprVnicUsnicConPolicyRefConPolicyName_Object((1,3,6,1,4,1,9,9,826,1,83,66,1,4),_CfprVnicUsnicConPolicyRefConPolicyName_Type())
cfprVnicUsnicConPolicyRefConPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicUsnicConPolicyRefConPolicyName.setStatus(_A)
_CfprVnicUsnicConPolicyRefOperConPolicyName_Type=SnmpAdminString
_CfprVnicUsnicConPolicyRefOperConPolicyName_Object=MibTableColumn
cfprVnicUsnicConPolicyRefOperConPolicyName=_CfprVnicUsnicConPolicyRefOperConPolicyName_Object((1,3,6,1,4,1,9,9,826,1,83,66,1,5),_CfprVnicUsnicConPolicyRefOperConPolicyName_Type())
cfprVnicUsnicConPolicyRefOperConPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicUsnicConPolicyRefOperConPolicyName.setStatus(_A)
_CfprVnicVhbaBehPolicyTable_Object=MibTable
cfprVnicVhbaBehPolicyTable=_CfprVnicVhbaBehPolicyTable_Object((1,3,6,1,4,1,9,9,826,1,83,67))
if mibBuilder.loadTexts:cfprVnicVhbaBehPolicyTable.setStatus(_A)
_CfprVnicVhbaBehPolicyEntry_Object=MibTableRow
cfprVnicVhbaBehPolicyEntry=_CfprVnicVhbaBehPolicyEntry_Object((1,3,6,1,4,1,9,9,826,1,83,67,1))
cfprVnicVhbaBehPolicyEntry.setIndexNames((0,_C,_AI))
if mibBuilder.loadTexts:cfprVnicVhbaBehPolicyEntry.setStatus(_A)
_CfprVnicVhbaBehPolicyInstanceId_Type=CfprManagedObjectId
_CfprVnicVhbaBehPolicyInstanceId_Object=MibTableColumn
cfprVnicVhbaBehPolicyInstanceId=_CfprVnicVhbaBehPolicyInstanceId_Object((1,3,6,1,4,1,9,9,826,1,83,67,1,1),_CfprVnicVhbaBehPolicyInstanceId_Type())
cfprVnicVhbaBehPolicyInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprVnicVhbaBehPolicyInstanceId.setStatus(_A)
_CfprVnicVhbaBehPolicyDn_Type=CfprManagedObjectDn
_CfprVnicVhbaBehPolicyDn_Object=MibTableColumn
cfprVnicVhbaBehPolicyDn=_CfprVnicVhbaBehPolicyDn_Object((1,3,6,1,4,1,9,9,826,1,83,67,1,2),_CfprVnicVhbaBehPolicyDn_Type())
cfprVnicVhbaBehPolicyDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicVhbaBehPolicyDn.setStatus(_A)
_CfprVnicVhbaBehPolicyRn_Type=SnmpAdminString
_CfprVnicVhbaBehPolicyRn_Object=MibTableColumn
cfprVnicVhbaBehPolicyRn=_CfprVnicVhbaBehPolicyRn_Object((1,3,6,1,4,1,9,9,826,1,83,67,1,3),_CfprVnicVhbaBehPolicyRn_Type())
cfprVnicVhbaBehPolicyRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicVhbaBehPolicyRn.setStatus(_A)
_CfprVnicVhbaBehPolicyAction_Type=CfprVnicDefaultAction
_CfprVnicVhbaBehPolicyAction_Object=MibTableColumn
cfprVnicVhbaBehPolicyAction=_CfprVnicVhbaBehPolicyAction_Object((1,3,6,1,4,1,9,9,826,1,83,67,1,4),_CfprVnicVhbaBehPolicyAction_Type())
cfprVnicVhbaBehPolicyAction.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicVhbaBehPolicyAction.setStatus(_A)
_CfprVnicVhbaBehPolicyDescr_Type=SnmpAdminString
_CfprVnicVhbaBehPolicyDescr_Object=MibTableColumn
cfprVnicVhbaBehPolicyDescr=_CfprVnicVhbaBehPolicyDescr_Object((1,3,6,1,4,1,9,9,826,1,83,67,1,5),_CfprVnicVhbaBehPolicyDescr_Type())
cfprVnicVhbaBehPolicyDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicVhbaBehPolicyDescr.setStatus(_A)
_CfprVnicVhbaBehPolicyIntId_Type=SnmpAdminString
_CfprVnicVhbaBehPolicyIntId_Object=MibTableColumn
cfprVnicVhbaBehPolicyIntId=_CfprVnicVhbaBehPolicyIntId_Object((1,3,6,1,4,1,9,9,826,1,83,67,1,6),_CfprVnicVhbaBehPolicyIntId_Type())
cfprVnicVhbaBehPolicyIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicVhbaBehPolicyIntId.setStatus(_A)
_CfprVnicVhbaBehPolicyName_Type=SnmpAdminString
_CfprVnicVhbaBehPolicyName_Object=MibTableColumn
cfprVnicVhbaBehPolicyName=_CfprVnicVhbaBehPolicyName_Object((1,3,6,1,4,1,9,9,826,1,83,67,1,7),_CfprVnicVhbaBehPolicyName_Type())
cfprVnicVhbaBehPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicVhbaBehPolicyName.setStatus(_A)
_CfprVnicVhbaBehPolicyNwTemplName_Type=SnmpAdminString
_CfprVnicVhbaBehPolicyNwTemplName_Object=MibTableColumn
cfprVnicVhbaBehPolicyNwTemplName=_CfprVnicVhbaBehPolicyNwTemplName_Object((1,3,6,1,4,1,9,9,826,1,83,67,1,8),_CfprVnicVhbaBehPolicyNwTemplName_Type())
cfprVnicVhbaBehPolicyNwTemplName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicVhbaBehPolicyNwTemplName.setStatus(_A)
_CfprVnicVhbaBehPolicyPolicyLevel_Type=Gauge32
_CfprVnicVhbaBehPolicyPolicyLevel_Object=MibTableColumn
cfprVnicVhbaBehPolicyPolicyLevel=_CfprVnicVhbaBehPolicyPolicyLevel_Object((1,3,6,1,4,1,9,9,826,1,83,67,1,9),_CfprVnicVhbaBehPolicyPolicyLevel_Type())
cfprVnicVhbaBehPolicyPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicVhbaBehPolicyPolicyLevel.setStatus(_A)
_CfprVnicVhbaBehPolicyPolicyOwner_Type=CfprPolicyPolicyOwner
_CfprVnicVhbaBehPolicyPolicyOwner_Object=MibTableColumn
cfprVnicVhbaBehPolicyPolicyOwner=_CfprVnicVhbaBehPolicyPolicyOwner_Object((1,3,6,1,4,1,9,9,826,1,83,67,1,10),_CfprVnicVhbaBehPolicyPolicyOwner_Type())
cfprVnicVhbaBehPolicyPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicVhbaBehPolicyPolicyOwner.setStatus(_A)
_CfprVnicVhbaBehPolicyType_Type=CfprVnicVhbaBehPolicyType
_CfprVnicVhbaBehPolicyType_Object=MibTableColumn
cfprVnicVhbaBehPolicyType=_CfprVnicVhbaBehPolicyType_Object((1,3,6,1,4,1,9,9,826,1,83,67,1,11),_CfprVnicVhbaBehPolicyType_Type())
cfprVnicVhbaBehPolicyType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicVhbaBehPolicyType.setStatus(_A)
_CfprVnicVlanTable_Object=MibTable
cfprVnicVlanTable=_CfprVnicVlanTable_Object((1,3,6,1,4,1,9,9,826,1,83,68))
if mibBuilder.loadTexts:cfprVnicVlanTable.setStatus(_A)
_CfprVnicVlanEntry_Object=MibTableRow
cfprVnicVlanEntry=_CfprVnicVlanEntry_Object((1,3,6,1,4,1,9,9,826,1,83,68,1))
cfprVnicVlanEntry.setIndexNames((0,_C,_AJ))
if mibBuilder.loadTexts:cfprVnicVlanEntry.setStatus(_A)
_CfprVnicVlanInstanceId_Type=CfprManagedObjectId
_CfprVnicVlanInstanceId_Object=MibTableColumn
cfprVnicVlanInstanceId=_CfprVnicVlanInstanceId_Object((1,3,6,1,4,1,9,9,826,1,83,68,1,1),_CfprVnicVlanInstanceId_Type())
cfprVnicVlanInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprVnicVlanInstanceId.setStatus(_A)
_CfprVnicVlanDn_Type=CfprManagedObjectDn
_CfprVnicVlanDn_Object=MibTableColumn
cfprVnicVlanDn=_CfprVnicVlanDn_Object((1,3,6,1,4,1,9,9,826,1,83,68,1,2),_CfprVnicVlanDn_Type())
cfprVnicVlanDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicVlanDn.setStatus(_A)
_CfprVnicVlanRn_Type=SnmpAdminString
_CfprVnicVlanRn_Object=MibTableColumn
cfprVnicVlanRn=_CfprVnicVlanRn_Object((1,3,6,1,4,1,9,9,826,1,83,68,1,3),_CfprVnicVlanRn_Type())
cfprVnicVlanRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicVlanRn.setStatus(_A)
_CfprVnicVlanConfigQualifier_Type=CfprVnicConfigIssues
_CfprVnicVlanConfigQualifier_Object=MibTableColumn
cfprVnicVlanConfigQualifier=_CfprVnicVlanConfigQualifier_Object((1,3,6,1,4,1,9,9,826,1,83,68,1,4),_CfprVnicVlanConfigQualifier_Type())
cfprVnicVlanConfigQualifier.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicVlanConfigQualifier.setStatus(_A)
_CfprVnicVlanFltAggr_Type=Unsigned64
_CfprVnicVlanFltAggr_Object=MibTableColumn
cfprVnicVlanFltAggr=_CfprVnicVlanFltAggr_Object((1,3,6,1,4,1,9,9,826,1,83,68,1,5),_CfprVnicVlanFltAggr_Type())
cfprVnicVlanFltAggr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicVlanFltAggr.setStatus(_A)
_CfprVnicVlanName_Type=SnmpAdminString
_CfprVnicVlanName_Object=MibTableColumn
cfprVnicVlanName=_CfprVnicVlanName_Object((1,3,6,1,4,1,9,9,826,1,83,68,1,6),_CfprVnicVlanName_Type())
cfprVnicVlanName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicVlanName.setStatus(_A)
_CfprVnicVlanOperState_Type=CfprVnicIfOperState
_CfprVnicVlanOperState_Object=MibTableColumn
cfprVnicVlanOperState=_CfprVnicVlanOperState_Object((1,3,6,1,4,1,9,9,826,1,83,68,1,7),_CfprVnicVlanOperState_Type())
cfprVnicVlanOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicVlanOperState.setStatus(_A)
_CfprVnicVlanOperVnetDn_Type=SnmpAdminString
_CfprVnicVlanOperVnetDn_Object=MibTableColumn
cfprVnicVlanOperVnetDn=_CfprVnicVlanOperVnetDn_Object((1,3,6,1,4,1,9,9,826,1,83,68,1,8),_CfprVnicVlanOperVnetDn_Type())
cfprVnicVlanOperVnetDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicVlanOperVnetDn.setStatus(_A)
_CfprVnicVlanOperVnetName_Type=SnmpAdminString
_CfprVnicVlanOperVnetName_Object=MibTableColumn
cfprVnicVlanOperVnetName=_CfprVnicVlanOperVnetName_Object((1,3,6,1,4,1,9,9,826,1,83,68,1,9),_CfprVnicVlanOperVnetName_Type())
cfprVnicVlanOperVnetName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicVlanOperVnetName.setStatus(_A)
_CfprVnicVlanOwner_Type=CfprVnicConnectionOwner
_CfprVnicVlanOwner_Object=MibTableColumn
cfprVnicVlanOwner=_CfprVnicVlanOwner_Object((1,3,6,1,4,1,9,9,826,1,83,68,1,10),_CfprVnicVlanOwner_Type())
cfprVnicVlanOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicVlanOwner.setStatus(_A)
_CfprVnicVlanPubNwId_Type=Gauge32
_CfprVnicVlanPubNwId_Object=MibTableColumn
cfprVnicVlanPubNwId=_CfprVnicVlanPubNwId_Object((1,3,6,1,4,1,9,9,826,1,83,68,1,11),_CfprVnicVlanPubNwId_Type())
cfprVnicVlanPubNwId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicVlanPubNwId.setStatus(_A)
_CfprVnicVlanSharing_Type=CfprFabricVlanSharingType
_CfprVnicVlanSharing_Object=MibTableColumn
cfprVnicVlanSharing=_CfprVnicVlanSharing_Object((1,3,6,1,4,1,9,9,826,1,83,68,1,12),_CfprVnicVlanSharing_Type())
cfprVnicVlanSharing.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicVlanSharing.setStatus(_A)
_CfprVnicVlanSwitchId_Type=CfprNetworkSwitchId
_CfprVnicVlanSwitchId_Object=MibTableColumn
cfprVnicVlanSwitchId=_CfprVnicVlanSwitchId_Object((1,3,6,1,4,1,9,9,826,1,83,68,1,13),_CfprVnicVlanSwitchId_Type())
cfprVnicVlanSwitchId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicVlanSwitchId.setStatus(_A)
_CfprVnicVlanType_Type=CfprVnicConnectionType
_CfprVnicVlanType_Object=MibTableColumn
cfprVnicVlanType=_CfprVnicVlanType_Object((1,3,6,1,4,1,9,9,826,1,83,68,1,14),_CfprVnicVlanType_Type())
cfprVnicVlanType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicVlanType.setStatus(_A)
_CfprVnicVlanVlanName_Type=SnmpAdminString
_CfprVnicVlanVlanName_Object=MibTableColumn
cfprVnicVlanVlanName=_CfprVnicVlanVlanName_Object((1,3,6,1,4,1,9,9,826,1,83,68,1,15),_CfprVnicVlanVlanName_Type())
cfprVnicVlanVlanName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicVlanVlanName.setStatus(_A)
_CfprVnicVlanVnet_Type=Gauge32
_CfprVnicVlanVnet_Object=MibTableColumn
cfprVnicVlanVnet=_CfprVnicVlanVnet_Object((1,3,6,1,4,1,9,9,826,1,83,68,1,16),_CfprVnicVlanVnet_Type())
cfprVnicVlanVnet.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicVlanVnet.setStatus(_A)
_CfprVnicVmqConPolicyTable_Object=MibTable
cfprVnicVmqConPolicyTable=_CfprVnicVmqConPolicyTable_Object((1,3,6,1,4,1,9,9,826,1,83,69))
if mibBuilder.loadTexts:cfprVnicVmqConPolicyTable.setStatus(_A)
_CfprVnicVmqConPolicyEntry_Object=MibTableRow
cfprVnicVmqConPolicyEntry=_CfprVnicVmqConPolicyEntry_Object((1,3,6,1,4,1,9,9,826,1,83,69,1))
cfprVnicVmqConPolicyEntry.setIndexNames((0,_C,_AK))
if mibBuilder.loadTexts:cfprVnicVmqConPolicyEntry.setStatus(_A)
_CfprVnicVmqConPolicyInstanceId_Type=CfprManagedObjectId
_CfprVnicVmqConPolicyInstanceId_Object=MibTableColumn
cfprVnicVmqConPolicyInstanceId=_CfprVnicVmqConPolicyInstanceId_Object((1,3,6,1,4,1,9,9,826,1,83,69,1,1),_CfprVnicVmqConPolicyInstanceId_Type())
cfprVnicVmqConPolicyInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprVnicVmqConPolicyInstanceId.setStatus(_A)
_CfprVnicVmqConPolicyDn_Type=CfprManagedObjectDn
_CfprVnicVmqConPolicyDn_Object=MibTableColumn
cfprVnicVmqConPolicyDn=_CfprVnicVmqConPolicyDn_Object((1,3,6,1,4,1,9,9,826,1,83,69,1,2),_CfprVnicVmqConPolicyDn_Type())
cfprVnicVmqConPolicyDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicVmqConPolicyDn.setStatus(_A)
_CfprVnicVmqConPolicyRn_Type=SnmpAdminString
_CfprVnicVmqConPolicyRn_Object=MibTableColumn
cfprVnicVmqConPolicyRn=_CfprVnicVmqConPolicyRn_Object((1,3,6,1,4,1,9,9,826,1,83,69,1,3),_CfprVnicVmqConPolicyRn_Type())
cfprVnicVmqConPolicyRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicVmqConPolicyRn.setStatus(_A)
_CfprVnicVmqConPolicyDescr_Type=SnmpAdminString
_CfprVnicVmqConPolicyDescr_Object=MibTableColumn
cfprVnicVmqConPolicyDescr=_CfprVnicVmqConPolicyDescr_Object((1,3,6,1,4,1,9,9,826,1,83,69,1,4),_CfprVnicVmqConPolicyDescr_Type())
cfprVnicVmqConPolicyDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicVmqConPolicyDescr.setStatus(_A)
_CfprVnicVmqConPolicyIntId_Type=SnmpAdminString
_CfprVnicVmqConPolicyIntId_Object=MibTableColumn
cfprVnicVmqConPolicyIntId=_CfprVnicVmqConPolicyIntId_Object((1,3,6,1,4,1,9,9,826,1,83,69,1,5),_CfprVnicVmqConPolicyIntId_Type())
cfprVnicVmqConPolicyIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicVmqConPolicyIntId.setStatus(_A)
_CfprVnicVmqConPolicyIntrCount_Type=Gauge32
_CfprVnicVmqConPolicyIntrCount_Object=MibTableColumn
cfprVnicVmqConPolicyIntrCount=_CfprVnicVmqConPolicyIntrCount_Object((1,3,6,1,4,1,9,9,826,1,83,69,1,6),_CfprVnicVmqConPolicyIntrCount_Type())
cfprVnicVmqConPolicyIntrCount.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicVmqConPolicyIntrCount.setStatus(_A)
_CfprVnicVmqConPolicyName_Type=SnmpAdminString
_CfprVnicVmqConPolicyName_Object=MibTableColumn
cfprVnicVmqConPolicyName=_CfprVnicVmqConPolicyName_Object((1,3,6,1,4,1,9,9,826,1,83,69,1,7),_CfprVnicVmqConPolicyName_Type())
cfprVnicVmqConPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicVmqConPolicyName.setStatus(_A)
_CfprVnicVmqConPolicyPolicyLevel_Type=Gauge32
_CfprVnicVmqConPolicyPolicyLevel_Object=MibTableColumn
cfprVnicVmqConPolicyPolicyLevel=_CfprVnicVmqConPolicyPolicyLevel_Object((1,3,6,1,4,1,9,9,826,1,83,69,1,8),_CfprVnicVmqConPolicyPolicyLevel_Type())
cfprVnicVmqConPolicyPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicVmqConPolicyPolicyLevel.setStatus(_A)
_CfprVnicVmqConPolicyPolicyOwner_Type=CfprPolicyPolicyOwner
_CfprVnicVmqConPolicyPolicyOwner_Object=MibTableColumn
cfprVnicVmqConPolicyPolicyOwner=_CfprVnicVmqConPolicyPolicyOwner_Object((1,3,6,1,4,1,9,9,826,1,83,69,1,9),_CfprVnicVmqConPolicyPolicyOwner_Type())
cfprVnicVmqConPolicyPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicVmqConPolicyPolicyOwner.setStatus(_A)
_CfprVnicVmqConPolicyVmqCount_Type=Gauge32
_CfprVnicVmqConPolicyVmqCount_Object=MibTableColumn
cfprVnicVmqConPolicyVmqCount=_CfprVnicVmqConPolicyVmqCount_Object((1,3,6,1,4,1,9,9,826,1,83,69,1,10),_CfprVnicVmqConPolicyVmqCount_Type())
cfprVnicVmqConPolicyVmqCount.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicVmqConPolicyVmqCount.setStatus(_A)
_CfprVnicVmqConPolicyRefTable_Object=MibTable
cfprVnicVmqConPolicyRefTable=_CfprVnicVmqConPolicyRefTable_Object((1,3,6,1,4,1,9,9,826,1,83,70))
if mibBuilder.loadTexts:cfprVnicVmqConPolicyRefTable.setStatus(_A)
_CfprVnicVmqConPolicyRefEntry_Object=MibTableRow
cfprVnicVmqConPolicyRefEntry=_CfprVnicVmqConPolicyRefEntry_Object((1,3,6,1,4,1,9,9,826,1,83,70,1))
cfprVnicVmqConPolicyRefEntry.setIndexNames((0,_C,_AL))
if mibBuilder.loadTexts:cfprVnicVmqConPolicyRefEntry.setStatus(_A)
_CfprVnicVmqConPolicyRefInstanceId_Type=CfprManagedObjectId
_CfprVnicVmqConPolicyRefInstanceId_Object=MibTableColumn
cfprVnicVmqConPolicyRefInstanceId=_CfprVnicVmqConPolicyRefInstanceId_Object((1,3,6,1,4,1,9,9,826,1,83,70,1,1),_CfprVnicVmqConPolicyRefInstanceId_Type())
cfprVnicVmqConPolicyRefInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprVnicVmqConPolicyRefInstanceId.setStatus(_A)
_CfprVnicVmqConPolicyRefDn_Type=CfprManagedObjectDn
_CfprVnicVmqConPolicyRefDn_Object=MibTableColumn
cfprVnicVmqConPolicyRefDn=_CfprVnicVmqConPolicyRefDn_Object((1,3,6,1,4,1,9,9,826,1,83,70,1,2),_CfprVnicVmqConPolicyRefDn_Type())
cfprVnicVmqConPolicyRefDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicVmqConPolicyRefDn.setStatus(_A)
_CfprVnicVmqConPolicyRefRn_Type=SnmpAdminString
_CfprVnicVmqConPolicyRefRn_Object=MibTableColumn
cfprVnicVmqConPolicyRefRn=_CfprVnicVmqConPolicyRefRn_Object((1,3,6,1,4,1,9,9,826,1,83,70,1,3),_CfprVnicVmqConPolicyRefRn_Type())
cfprVnicVmqConPolicyRefRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicVmqConPolicyRefRn.setStatus(_A)
_CfprVnicVmqConPolicyRefConPolicyName_Type=SnmpAdminString
_CfprVnicVmqConPolicyRefConPolicyName_Object=MibTableColumn
cfprVnicVmqConPolicyRefConPolicyName=_CfprVnicVmqConPolicyRefConPolicyName_Object((1,3,6,1,4,1,9,9,826,1,83,70,1,4),_CfprVnicVmqConPolicyRefConPolicyName_Type())
cfprVnicVmqConPolicyRefConPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicVmqConPolicyRefConPolicyName.setStatus(_A)
_CfprVnicVmqConPolicyRefOperConPolicyName_Type=SnmpAdminString
_CfprVnicVmqConPolicyRefOperConPolicyName_Object=MibTableColumn
cfprVnicVmqConPolicyRefOperConPolicyName=_CfprVnicVmqConPolicyRefOperConPolicyName_Object((1,3,6,1,4,1,9,9,826,1,83,70,1,5),_CfprVnicVmqConPolicyRefOperConPolicyName_Type())
cfprVnicVmqConPolicyRefOperConPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicVmqConPolicyRefOperConPolicyName.setStatus(_A)
_CfprVnicVnicBehPolicyTable_Object=MibTable
cfprVnicVnicBehPolicyTable=_CfprVnicVnicBehPolicyTable_Object((1,3,6,1,4,1,9,9,826,1,83,71))
if mibBuilder.loadTexts:cfprVnicVnicBehPolicyTable.setStatus(_A)
_CfprVnicVnicBehPolicyEntry_Object=MibTableRow
cfprVnicVnicBehPolicyEntry=_CfprVnicVnicBehPolicyEntry_Object((1,3,6,1,4,1,9,9,826,1,83,71,1))
cfprVnicVnicBehPolicyEntry.setIndexNames((0,_C,_AM))
if mibBuilder.loadTexts:cfprVnicVnicBehPolicyEntry.setStatus(_A)
_CfprVnicVnicBehPolicyInstanceId_Type=CfprManagedObjectId
_CfprVnicVnicBehPolicyInstanceId_Object=MibTableColumn
cfprVnicVnicBehPolicyInstanceId=_CfprVnicVnicBehPolicyInstanceId_Object((1,3,6,1,4,1,9,9,826,1,83,71,1,1),_CfprVnicVnicBehPolicyInstanceId_Type())
cfprVnicVnicBehPolicyInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprVnicVnicBehPolicyInstanceId.setStatus(_A)
_CfprVnicVnicBehPolicyDn_Type=CfprManagedObjectDn
_CfprVnicVnicBehPolicyDn_Object=MibTableColumn
cfprVnicVnicBehPolicyDn=_CfprVnicVnicBehPolicyDn_Object((1,3,6,1,4,1,9,9,826,1,83,71,1,2),_CfprVnicVnicBehPolicyDn_Type())
cfprVnicVnicBehPolicyDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicVnicBehPolicyDn.setStatus(_A)
_CfprVnicVnicBehPolicyRn_Type=SnmpAdminString
_CfprVnicVnicBehPolicyRn_Object=MibTableColumn
cfprVnicVnicBehPolicyRn=_CfprVnicVnicBehPolicyRn_Object((1,3,6,1,4,1,9,9,826,1,83,71,1,3),_CfprVnicVnicBehPolicyRn_Type())
cfprVnicVnicBehPolicyRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicVnicBehPolicyRn.setStatus(_A)
_CfprVnicVnicBehPolicyAction_Type=CfprVnicDefaultAction
_CfprVnicVnicBehPolicyAction_Object=MibTableColumn
cfprVnicVnicBehPolicyAction=_CfprVnicVnicBehPolicyAction_Object((1,3,6,1,4,1,9,9,826,1,83,71,1,4),_CfprVnicVnicBehPolicyAction_Type())
cfprVnicVnicBehPolicyAction.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicVnicBehPolicyAction.setStatus(_A)
_CfprVnicVnicBehPolicyDescr_Type=SnmpAdminString
_CfprVnicVnicBehPolicyDescr_Object=MibTableColumn
cfprVnicVnicBehPolicyDescr=_CfprVnicVnicBehPolicyDescr_Object((1,3,6,1,4,1,9,9,826,1,83,71,1,5),_CfprVnicVnicBehPolicyDescr_Type())
cfprVnicVnicBehPolicyDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicVnicBehPolicyDescr.setStatus(_A)
_CfprVnicVnicBehPolicyIntId_Type=SnmpAdminString
_CfprVnicVnicBehPolicyIntId_Object=MibTableColumn
cfprVnicVnicBehPolicyIntId=_CfprVnicVnicBehPolicyIntId_Object((1,3,6,1,4,1,9,9,826,1,83,71,1,6),_CfprVnicVnicBehPolicyIntId_Type())
cfprVnicVnicBehPolicyIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicVnicBehPolicyIntId.setStatus(_A)
_CfprVnicVnicBehPolicyName_Type=SnmpAdminString
_CfprVnicVnicBehPolicyName_Object=MibTableColumn
cfprVnicVnicBehPolicyName=_CfprVnicVnicBehPolicyName_Object((1,3,6,1,4,1,9,9,826,1,83,71,1,7),_CfprVnicVnicBehPolicyName_Type())
cfprVnicVnicBehPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicVnicBehPolicyName.setStatus(_A)
_CfprVnicVnicBehPolicyNwTemplName_Type=SnmpAdminString
_CfprVnicVnicBehPolicyNwTemplName_Object=MibTableColumn
cfprVnicVnicBehPolicyNwTemplName=_CfprVnicVnicBehPolicyNwTemplName_Object((1,3,6,1,4,1,9,9,826,1,83,71,1,8),_CfprVnicVnicBehPolicyNwTemplName_Type())
cfprVnicVnicBehPolicyNwTemplName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicVnicBehPolicyNwTemplName.setStatus(_A)
_CfprVnicVnicBehPolicyPolicyLevel_Type=Gauge32
_CfprVnicVnicBehPolicyPolicyLevel_Object=MibTableColumn
cfprVnicVnicBehPolicyPolicyLevel=_CfprVnicVnicBehPolicyPolicyLevel_Object((1,3,6,1,4,1,9,9,826,1,83,71,1,9),_CfprVnicVnicBehPolicyPolicyLevel_Type())
cfprVnicVnicBehPolicyPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicVnicBehPolicyPolicyLevel.setStatus(_A)
_CfprVnicVnicBehPolicyPolicyOwner_Type=CfprPolicyPolicyOwner
_CfprVnicVnicBehPolicyPolicyOwner_Object=MibTableColumn
cfprVnicVnicBehPolicyPolicyOwner=_CfprVnicVnicBehPolicyPolicyOwner_Object((1,3,6,1,4,1,9,9,826,1,83,71,1,10),_CfprVnicVnicBehPolicyPolicyOwner_Type())
cfprVnicVnicBehPolicyPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicVnicBehPolicyPolicyOwner.setStatus(_A)
_CfprVnicVnicBehPolicyType_Type=CfprVnicVnicBehPolicyType
_CfprVnicVnicBehPolicyType_Object=MibTableColumn
cfprVnicVnicBehPolicyType=_CfprVnicVnicBehPolicyType_Object((1,3,6,1,4,1,9,9,826,1,83,71,1,11),_CfprVnicVnicBehPolicyType_Type())
cfprVnicVnicBehPolicyType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicVnicBehPolicyType.setStatus(_A)
_CfprVnicWwnnHistoryTable_Object=MibTable
cfprVnicWwnnHistoryTable=_CfprVnicWwnnHistoryTable_Object((1,3,6,1,4,1,9,9,826,1,83,72))
if mibBuilder.loadTexts:cfprVnicWwnnHistoryTable.setStatus(_A)
_CfprVnicWwnnHistoryEntry_Object=MibTableRow
cfprVnicWwnnHistoryEntry=_CfprVnicWwnnHistoryEntry_Object((1,3,6,1,4,1,9,9,826,1,83,72,1))
cfprVnicWwnnHistoryEntry.setIndexNames((0,_C,_AN))
if mibBuilder.loadTexts:cfprVnicWwnnHistoryEntry.setStatus(_A)
_CfprVnicWwnnHistoryInstanceId_Type=CfprManagedObjectId
_CfprVnicWwnnHistoryInstanceId_Object=MibTableColumn
cfprVnicWwnnHistoryInstanceId=_CfprVnicWwnnHistoryInstanceId_Object((1,3,6,1,4,1,9,9,826,1,83,72,1,1),_CfprVnicWwnnHistoryInstanceId_Type())
cfprVnicWwnnHistoryInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprVnicWwnnHistoryInstanceId.setStatus(_A)
_CfprVnicWwnnHistoryDn_Type=CfprManagedObjectDn
_CfprVnicWwnnHistoryDn_Object=MibTableColumn
cfprVnicWwnnHistoryDn=_CfprVnicWwnnHistoryDn_Object((1,3,6,1,4,1,9,9,826,1,83,72,1,2),_CfprVnicWwnnHistoryDn_Type())
cfprVnicWwnnHistoryDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicWwnnHistoryDn.setStatus(_A)
_CfprVnicWwnnHistoryRn_Type=SnmpAdminString
_CfprVnicWwnnHistoryRn_Object=MibTableColumn
cfprVnicWwnnHistoryRn=_CfprVnicWwnnHistoryRn_Object((1,3,6,1,4,1,9,9,826,1,83,72,1,3),_CfprVnicWwnnHistoryRn_Type())
cfprVnicWwnnHistoryRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicWwnnHistoryRn.setStatus(_A)
_CfprVnicWwnnHistoryOldwwnn_Type=Unsigned64
_CfprVnicWwnnHistoryOldwwnn_Object=MibTableColumn
cfprVnicWwnnHistoryOldwwnn=_CfprVnicWwnnHistoryOldwwnn_Object((1,3,6,1,4,1,9,9,826,1,83,72,1,4),_CfprVnicWwnnHistoryOldwwnn_Type())
cfprVnicWwnnHistoryOldwwnn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicWwnnHistoryOldwwnn.setStatus(_A)
_CfprVnicWwpnHistoryTable_Object=MibTable
cfprVnicWwpnHistoryTable=_CfprVnicWwpnHistoryTable_Object((1,3,6,1,4,1,9,9,826,1,83,73))
if mibBuilder.loadTexts:cfprVnicWwpnHistoryTable.setStatus(_A)
_CfprVnicWwpnHistoryEntry_Object=MibTableRow
cfprVnicWwpnHistoryEntry=_CfprVnicWwpnHistoryEntry_Object((1,3,6,1,4,1,9,9,826,1,83,73,1))
cfprVnicWwpnHistoryEntry.setIndexNames((0,_C,_AO))
if mibBuilder.loadTexts:cfprVnicWwpnHistoryEntry.setStatus(_A)
_CfprVnicWwpnHistoryInstanceId_Type=CfprManagedObjectId
_CfprVnicWwpnHistoryInstanceId_Object=MibTableColumn
cfprVnicWwpnHistoryInstanceId=_CfprVnicWwpnHistoryInstanceId_Object((1,3,6,1,4,1,9,9,826,1,83,73,1,1),_CfprVnicWwpnHistoryInstanceId_Type())
cfprVnicWwpnHistoryInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprVnicWwpnHistoryInstanceId.setStatus(_A)
_CfprVnicWwpnHistoryDn_Type=CfprManagedObjectDn
_CfprVnicWwpnHistoryDn_Object=MibTableColumn
cfprVnicWwpnHistoryDn=_CfprVnicWwpnHistoryDn_Object((1,3,6,1,4,1,9,9,826,1,83,73,1,2),_CfprVnicWwpnHistoryDn_Type())
cfprVnicWwpnHistoryDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicWwpnHistoryDn.setStatus(_A)
_CfprVnicWwpnHistoryRn_Type=SnmpAdminString
_CfprVnicWwpnHistoryRn_Object=MibTableColumn
cfprVnicWwpnHistoryRn=_CfprVnicWwpnHistoryRn_Object((1,3,6,1,4,1,9,9,826,1,83,73,1,3),_CfprVnicWwpnHistoryRn_Type())
cfprVnicWwpnHistoryRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicWwpnHistoryRn.setStatus(_A)
_CfprVnicWwpnHistoryOldaddr_Type=Unsigned64
_CfprVnicWwpnHistoryOldaddr_Object=MibTableColumn
cfprVnicWwpnHistoryOldaddr=_CfprVnicWwpnHistoryOldaddr_Object((1,3,6,1,4,1,9,9,826,1,83,73,1,4),_CfprVnicWwpnHistoryOldaddr_Type())
cfprVnicWwpnHistoryOldaddr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprVnicWwpnHistoryOldaddr.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'cfprVnicObjects':cfprVnicObjects,'cfprVnicBootIpPolicyTable':cfprVnicBootIpPolicyTable,'cfprVnicBootIpPolicyEntry':cfprVnicBootIpPolicyEntry,_E:cfprVnicBootIpPolicyInstanceId,'cfprVnicBootIpPolicyDn':cfprVnicBootIpPolicyDn,'cfprVnicBootIpPolicyRn':cfprVnicBootIpPolicyRn,'cfprVnicBootIpPolicyDescr':cfprVnicBootIpPolicyDescr,'cfprVnicBootIpPolicyIntId':cfprVnicBootIpPolicyIntId,'cfprVnicBootIpPolicyName':cfprVnicBootIpPolicyName,'cfprVnicBootIpPolicyPolicyLevel':cfprVnicBootIpPolicyPolicyLevel,'cfprVnicBootIpPolicyPolicyOwner':cfprVnicBootIpPolicyPolicyOwner,'cfprVnicBootIpPolicyPoolName':cfprVnicBootIpPolicyPoolName,'cfprVnicBootTargetTable':cfprVnicBootTargetTable,'cfprVnicBootTargetEntry':cfprVnicBootTargetEntry,_F:cfprVnicBootTargetInstanceId,'cfprVnicBootTargetDn':cfprVnicBootTargetDn,'cfprVnicBootTargetRn':cfprVnicBootTargetRn,'cfprVnicBootTargetLun':cfprVnicBootTargetLun,'cfprVnicBootTargetWwn':cfprVnicBootTargetWwn,'cfprVnicConnDefTable':cfprVnicConnDefTable,'cfprVnicConnDefEntry':cfprVnicConnDefEntry,_G:cfprVnicConnDefInstanceId,'cfprVnicConnDefDn':cfprVnicConnDefDn,'cfprVnicConnDefRn':cfprVnicConnDefRn,'cfprVnicConnDefFltAggr':cfprVnicConnDefFltAggr,'cfprVnicConnDefLanConnPolicyName':cfprVnicConnDefLanConnPolicyName,'cfprVnicConnDefOperLanConnPolicyName':cfprVnicConnDefOperLanConnPolicyName,'cfprVnicConnDefOperSanConnPolicyName':cfprVnicConnDefOperSanConnPolicyName,'cfprVnicConnDefSanConnPolicyName':cfprVnicConnDefSanConnPolicyName,'cfprVnicDefBehTable':cfprVnicDefBehTable,'cfprVnicDefBehEntry':cfprVnicDefBehEntry,_H:cfprVnicDefBehInstanceId,'cfprVnicDefBehDn':cfprVnicDefBehDn,'cfprVnicDefBehRn':cfprVnicDefBehRn,'cfprVnicDefBehAction':cfprVnicDefBehAction,'cfprVnicDefBehDescr':cfprVnicDefBehDescr,'cfprVnicDefBehIntId':cfprVnicDefBehIntId,'cfprVnicDefBehName':cfprVnicDefBehName,'cfprVnicDefBehNwTemplName':cfprVnicDefBehNwTemplName,'cfprVnicDefBehPolicyLevel':cfprVnicDefBehPolicyLevel,'cfprVnicDefBehPolicyOwner':cfprVnicDefBehPolicyOwner,'cfprVnicDefBehType':cfprVnicDefBehType,'cfprVnicDynamicConTable':cfprVnicDynamicConTable,'cfprVnicDynamicConEntry':cfprVnicDynamicConEntry,_I:cfprVnicDynamicConInstanceId,'cfprVnicDynamicConDn':cfprVnicDynamicConDn,'cfprVnicDynamicConRn':cfprVnicDynamicConRn,'cfprVnicDynamicConAdaptorProfileName':cfprVnicDynamicConAdaptorProfileName,'cfprVnicDynamicConDescr':cfprVnicDynamicConDescr,'cfprVnicDynamicConDynamicEth':cfprVnicDynamicConDynamicEth,'cfprVnicDynamicConIntId':cfprVnicDynamicConIntId,'cfprVnicDynamicConMtu':cfprVnicDynamicConMtu,'cfprVnicDynamicConName':cfprVnicDynamicConName,'cfprVnicDynamicConNamingPrefix':cfprVnicDynamicConNamingPrefix,'cfprVnicDynamicConPolicyLevel':cfprVnicDynamicConPolicyLevel,'cfprVnicDynamicConPolicyOwner':cfprVnicDynamicConPolicyOwner,'cfprVnicDynamicConProtection':cfprVnicDynamicConProtection,'cfprVnicDynamicConPolicyTable':cfprVnicDynamicConPolicyTable,'cfprVnicDynamicConPolicyEntry':cfprVnicDynamicConPolicyEntry,_J:cfprVnicDynamicConPolicyInstanceId,'cfprVnicDynamicConPolicyDn':cfprVnicDynamicConPolicyDn,'cfprVnicDynamicConPolicyRn':cfprVnicDynamicConPolicyRn,'cfprVnicDynamicConPolicyAdaptorProfileName':cfprVnicDynamicConPolicyAdaptorProfileName,'cfprVnicDynamicConPolicyDescr':cfprVnicDynamicConPolicyDescr,'cfprVnicDynamicConPolicyDynamicEth':cfprVnicDynamicConPolicyDynamicEth,'cfprVnicDynamicConPolicyIntId':cfprVnicDynamicConPolicyIntId,'cfprVnicDynamicConPolicyMtu':cfprVnicDynamicConPolicyMtu,'cfprVnicDynamicConPolicyName':cfprVnicDynamicConPolicyName,'cfprVnicDynamicConPolicyNamingPrefix':cfprVnicDynamicConPolicyNamingPrefix,'cfprVnicDynamicConPolicyPolicyLevel':cfprVnicDynamicConPolicyPolicyLevel,'cfprVnicDynamicConPolicyPolicyOwner':cfprVnicDynamicConPolicyPolicyOwner,'cfprVnicDynamicConPolicyProtection':cfprVnicDynamicConPolicyProtection,'cfprVnicDynamicConPolicyRefTable':cfprVnicDynamicConPolicyRefTable,'cfprVnicDynamicConPolicyRefEntry':cfprVnicDynamicConPolicyRefEntry,_K:cfprVnicDynamicConPolicyRefInstanceId,'cfprVnicDynamicConPolicyRefDn':cfprVnicDynamicConPolicyRefDn,'cfprVnicDynamicConPolicyRefRn':cfprVnicDynamicConPolicyRefRn,'cfprVnicDynamicConPolicyRefConPolicyName':cfprVnicDynamicConPolicyRefConPolicyName,'cfprVnicDynamicConPolicyRefOperConPolicyName':cfprVnicDynamicConPolicyRefOperConPolicyName,'cfprVnicDynamicIdUniverseTable':cfprVnicDynamicIdUniverseTable,'cfprVnicDynamicIdUniverseEntry':cfprVnicDynamicIdUniverseEntry,_L:cfprVnicDynamicIdUniverseInstanceId,'cfprVnicDynamicIdUniverseDn':cfprVnicDynamicIdUniverseDn,'cfprVnicDynamicIdUniverseRn':cfprVnicDynamicIdUniverseRn,'cfprVnicDynamicIdUniverseDescr':cfprVnicDynamicIdUniverseDescr,'cfprVnicDynamicIdUniverseIntId':cfprVnicDynamicIdUniverseIntId,'cfprVnicDynamicIdUniverseName':cfprVnicDynamicIdUniverseName,'cfprVnicDynamicIdUniversePolicyLevel':cfprVnicDynamicIdUniversePolicyLevel,'cfprVnicDynamicIdUniversePolicyOwner':cfprVnicDynamicIdUniversePolicyOwner,'cfprVnicDynamicProviderTable':cfprVnicDynamicProviderTable,'cfprVnicDynamicProviderEntry':cfprVnicDynamicProviderEntry,_M:cfprVnicDynamicProviderInstanceId,'cfprVnicDynamicProviderDn':cfprVnicDynamicProviderDn,'cfprVnicDynamicProviderRn':cfprVnicDynamicProviderRn,'cfprVnicDynamicProviderName':cfprVnicDynamicProviderName,'cfprVnicDynamicProviderEpTable':cfprVnicDynamicProviderEpTable,'cfprVnicDynamicProviderEpEntry':cfprVnicDynamicProviderEpEntry,_N:cfprVnicDynamicProviderEpInstanceId,'cfprVnicDynamicProviderEpDn':cfprVnicDynamicProviderEpDn,'cfprVnicDynamicProviderEpRn':cfprVnicDynamicProviderEpRn,'cfprVnicDynamicProviderEpChassisId':cfprVnicDynamicProviderEpChassisId,'cfprVnicDynamicProviderEpPortId':cfprVnicDynamicProviderEpPortId,'cfprVnicDynamicProviderEpSlotId':cfprVnicDynamicProviderEpSlotId,'cfprVnicDynamicProviderEpSwitchId':cfprVnicDynamicProviderEpSwitchId,'cfprVnicEthLifTable':cfprVnicEthLifTable,'cfprVnicEthLifEntry':cfprVnicEthLifEntry,_O:cfprVnicEthLifInstanceId,'cfprVnicEthLifDn':cfprVnicEthLifDn,'cfprVnicEthLifRn':cfprVnicEthLifRn,'cfprVnicEthLifAddr':cfprVnicEthLifAddr,'cfprVnicEthLifName':cfprVnicEthLifName,'cfprVnicEthLifNicDn':cfprVnicEthLifNicDn,'cfprVnicEthLifOwner':cfprVnicEthLifOwner,'cfprVnicEthLifSwitchId':cfprVnicEthLifSwitchId,'cfprVnicEthLifType':cfprVnicEthLifType,'cfprVnicEthLifVnicDn':cfprVnicEthLifVnicDn,'cfprVnicEtherTable':cfprVnicEtherTable,'cfprVnicEtherEntry':cfprVnicEtherEntry,_P:cfprVnicEtherInstanceId,'cfprVnicEtherDn':cfprVnicEtherDn,'cfprVnicEtherRn':cfprVnicEtherRn,'cfprVnicEtherAdaptorProfileName':cfprVnicEtherAdaptorProfileName,'cfprVnicEtherAddr':cfprVnicEtherAddr,'cfprVnicEtherAdminHostPort':cfprVnicEtherAdminHostPort,'cfprVnicEtherAdminVcon':cfprVnicEtherAdminVcon,'cfprVnicEtherAppInstId':cfprVnicEtherAppInstId,'cfprVnicEtherAppRole':cfprVnicEtherAppRole,'cfprVnicEtherBootDev':cfprVnicEtherBootDev,'cfprVnicEtherConfigQualifier':cfprVnicEtherConfigQualifier,'cfprVnicEtherConfigState':cfprVnicEtherConfigState,'cfprVnicEtherDynamicId':cfprVnicEtherDynamicId,'cfprVnicEtherEquipmentDn':cfprVnicEtherEquipmentDn,'cfprVnicEtherFltAggr':cfprVnicEtherFltAggr,'cfprVnicEtherIdentPoolName':cfprVnicEtherIdentPoolName,'cfprVnicEtherInstType':cfprVnicEtherInstType,'cfprVnicEtherIsAllocated':cfprVnicEtherIsAllocated,'cfprVnicEtherMtu':cfprVnicEtherMtu,'cfprVnicEtherName':cfprVnicEtherName,'cfprVnicEtherNwCtrlPolicyName':cfprVnicEtherNwCtrlPolicyName,'cfprVnicEtherNwTemplName':cfprVnicEtherNwTemplName,'cfprVnicEtherOperAdaptorProfileName':cfprVnicEtherOperAdaptorProfileName,'cfprVnicEtherOperHostPort':cfprVnicEtherOperHostPort,'cfprVnicEtherOperIdentPoolName':cfprVnicEtherOperIdentPoolName,'cfprVnicEtherOperNwCtrlPolicyName':cfprVnicEtherOperNwCtrlPolicyName,'cfprVnicEtherOperNwTemplName':cfprVnicEtherOperNwTemplName,'cfprVnicEtherOperOrder':cfprVnicEtherOperOrder,'cfprVnicEtherOperPinToGroupName':cfprVnicEtherOperPinToGroupName,'cfprVnicEtherOperQosPolicyName':cfprVnicEtherOperQosPolicyName,'cfprVnicEtherOperSpeed':cfprVnicEtherOperSpeed,'cfprVnicEtherOperStatsPolicyName':cfprVnicEtherOperStatsPolicyName,'cfprVnicEtherOperVcon':cfprVnicEtherOperVcon,'cfprVnicEtherOrder':cfprVnicEtherOrder,'cfprVnicEtherOwner':cfprVnicEtherOwner,'cfprVnicEtherPfDn':cfprVnicEtherPfDn,'cfprVnicEtherPinToGroupName':cfprVnicEtherPinToGroupName,'cfprVnicEtherQosPolicyName':cfprVnicEtherQosPolicyName,'cfprVnicEtherStatsPolicyName':cfprVnicEtherStatsPolicyName,'cfprVnicEtherSwitchId':cfprVnicEtherSwitchId,'cfprVnicEtherType':cfprVnicEtherType,'cfprVnicEtherVirtualizationPreference':cfprVnicEtherVirtualizationPreference,'cfprVnicEtherPortType':cfprVnicEtherPortType,'cfprVnicEtherIfTable':cfprVnicEtherIfTable,'cfprVnicEtherIfEntry':cfprVnicEtherIfEntry,_Q:cfprVnicEtherIfInstanceId,'cfprVnicEtherIfDn':cfprVnicEtherIfDn,'cfprVnicEtherIfRn':cfprVnicEtherIfRn,'cfprVnicEtherIfAddr':cfprVnicEtherIfAddr,'cfprVnicEtherIfConfigQualifier':cfprVnicEtherIfConfigQualifier,'cfprVnicEtherIfDefaultNet':cfprVnicEtherIfDefaultNet,'cfprVnicEtherIfFltAggr':cfprVnicEtherIfFltAggr,'cfprVnicEtherIfName':cfprVnicEtherIfName,'cfprVnicEtherIfOperState':cfprVnicEtherIfOperState,'cfprVnicEtherIfOperVnetDn':cfprVnicEtherIfOperVnetDn,'cfprVnicEtherIfOperVnetName':cfprVnicEtherIfOperVnetName,'cfprVnicEtherIfOwner':cfprVnicEtherIfOwner,'cfprVnicEtherIfPubNwId':cfprVnicEtherIfPubNwId,'cfprVnicEtherIfSharing':cfprVnicEtherIfSharing,'cfprVnicEtherIfSwitchId':cfprVnicEtherIfSwitchId,'cfprVnicEtherIfType':cfprVnicEtherIfType,'cfprVnicEtherIfVnet':cfprVnicEtherIfVnet,'cfprVnicFcTable':cfprVnicFcTable,'cfprVnicFcEntry':cfprVnicFcEntry,_R:cfprVnicFcInstanceId,'cfprVnicFcDn':cfprVnicFcDn,'cfprVnicFcRn':cfprVnicFcRn,'cfprVnicFcAdaptorProfileName':cfprVnicFcAdaptorProfileName,'cfprVnicFcAddr':cfprVnicFcAddr,'cfprVnicFcAdminHostPort':cfprVnicFcAdminHostPort,'cfprVnicFcAdminVcon':cfprVnicFcAdminVcon,'cfprVnicFcAppRole':cfprVnicFcAppRole,'cfprVnicFcBootDev':cfprVnicFcBootDev,'cfprVnicFcConfigQualifier':cfprVnicFcConfigQualifier,'cfprVnicFcConfigState':cfprVnicFcConfigState,'cfprVnicFcEquipmentDn':cfprVnicFcEquipmentDn,'cfprVnicFcFltAggr':cfprVnicFcFltAggr,'cfprVnicFcIdentPoolName':cfprVnicFcIdentPoolName,'cfprVnicFcInstType':cfprVnicFcInstType,'cfprVnicFcMaxDataFieldSize':cfprVnicFcMaxDataFieldSize,'cfprVnicFcName':cfprVnicFcName,'cfprVnicFcNodeAddr':cfprVnicFcNodeAddr,'cfprVnicFcNwTemplName':cfprVnicFcNwTemplName,'cfprVnicFcOperAdaptorProfileName':cfprVnicFcOperAdaptorProfileName,'cfprVnicFcOperHostPort':cfprVnicFcOperHostPort,'cfprVnicFcOperIdentPoolName':cfprVnicFcOperIdentPoolName,'cfprVnicFcOperNwTemplName':cfprVnicFcOperNwTemplName,'cfprVnicFcOperOrder':cfprVnicFcOperOrder,'cfprVnicFcOperPinToGroupName':cfprVnicFcOperPinToGroupName,'cfprVnicFcOperQosPolicyName':cfprVnicFcOperQosPolicyName,'cfprVnicFcOperSpeed':cfprVnicFcOperSpeed,'cfprVnicFcOperStatsPolicyName':cfprVnicFcOperStatsPolicyName,'cfprVnicFcOperVcon':cfprVnicFcOperVcon,'cfprVnicFcOrder':cfprVnicFcOrder,'cfprVnicFcOwner':cfprVnicFcOwner,'cfprVnicFcPersBind':cfprVnicFcPersBind,'cfprVnicFcPersBindClear':cfprVnicFcPersBindClear,'cfprVnicFcPinToGroupName':cfprVnicFcPinToGroupName,'cfprVnicFcQosPolicyName':cfprVnicFcQosPolicyName,'cfprVnicFcStatsPolicyName':cfprVnicFcStatsPolicyName,'cfprVnicFcSwitchId':cfprVnicFcSwitchId,'cfprVnicFcType':cfprVnicFcType,'cfprVnicFcGroupDefTable':cfprVnicFcGroupDefTable,'cfprVnicFcGroupDefEntry':cfprVnicFcGroupDefEntry,_S:cfprVnicFcGroupDefInstanceId,'cfprVnicFcGroupDefDn':cfprVnicFcGroupDefDn,'cfprVnicFcGroupDefRn':cfprVnicFcGroupDefRn,'cfprVnicFcGroupDefAdaptorProfileName':cfprVnicFcGroupDefAdaptorProfileName,'cfprVnicFcGroupDefDescr':cfprVnicFcGroupDefDescr,'cfprVnicFcGroupDefIdentPoolName':cfprVnicFcGroupDefIdentPoolName,'cfprVnicFcGroupDefIntId':cfprVnicFcGroupDefIntId,'cfprVnicFcGroupDefMaxDataFieldSize':cfprVnicFcGroupDefMaxDataFieldSize,'cfprVnicFcGroupDefName':cfprVnicFcGroupDefName,'cfprVnicFcGroupDefNwTemplName':cfprVnicFcGroupDefNwTemplName,'cfprVnicFcGroupDefOperStatsPolicyName':cfprVnicFcGroupDefOperStatsPolicyName,'cfprVnicFcGroupDefOperStorageConnPolicyName':cfprVnicFcGroupDefOperStorageConnPolicyName,'cfprVnicFcGroupDefPolicyLevel':cfprVnicFcGroupDefPolicyLevel,'cfprVnicFcGroupDefPolicyOwner':cfprVnicFcGroupDefPolicyOwner,'cfprVnicFcGroupDefQosPolicyName':cfprVnicFcGroupDefQosPolicyName,'cfprVnicFcGroupDefStatsPolicyName':cfprVnicFcGroupDefStatsPolicyName,'cfprVnicFcGroupDefStorageConnPolicyName':cfprVnicFcGroupDefStorageConnPolicyName,'cfprVnicFcGroupTemplTable':cfprVnicFcGroupTemplTable,'cfprVnicFcGroupTemplEntry':cfprVnicFcGroupTemplEntry,_T:cfprVnicFcGroupTemplInstanceId,'cfprVnicFcGroupTemplDn':cfprVnicFcGroupTemplDn,'cfprVnicFcGroupTemplRn':cfprVnicFcGroupTemplRn,'cfprVnicFcGroupTemplAdaptorProfileName':cfprVnicFcGroupTemplAdaptorProfileName,'cfprVnicFcGroupTemplDescr':cfprVnicFcGroupTemplDescr,'cfprVnicFcGroupTemplIdentPoolName':cfprVnicFcGroupTemplIdentPoolName,'cfprVnicFcGroupTemplIntId':cfprVnicFcGroupTemplIntId,'cfprVnicFcGroupTemplMaxDataFieldSize':cfprVnicFcGroupTemplMaxDataFieldSize,'cfprVnicFcGroupTemplName':cfprVnicFcGroupTemplName,'cfprVnicFcGroupTemplNwTemplName':cfprVnicFcGroupTemplNwTemplName,'cfprVnicFcGroupTemplOperStatsPolicyName':cfprVnicFcGroupTemplOperStatsPolicyName,'cfprVnicFcGroupTemplOperStorageConnPolicyName':cfprVnicFcGroupTemplOperStorageConnPolicyName,'cfprVnicFcGroupTemplPolicyLevel':cfprVnicFcGroupTemplPolicyLevel,'cfprVnicFcGroupTemplPolicyOwner':cfprVnicFcGroupTemplPolicyOwner,'cfprVnicFcGroupTemplQosPolicyName':cfprVnicFcGroupTemplQosPolicyName,'cfprVnicFcGroupTemplStatsPolicyName':cfprVnicFcGroupTemplStatsPolicyName,'cfprVnicFcGroupTemplStorageConnPolicyName':cfprVnicFcGroupTemplStorageConnPolicyName,'cfprVnicFcGroupTemplTemplType':cfprVnicFcGroupTemplTemplType,'cfprVnicFcIfTable':cfprVnicFcIfTable,'cfprVnicFcIfEntry':cfprVnicFcIfEntry,_U:cfprVnicFcIfInstanceId,'cfprVnicFcIfDn':cfprVnicFcIfDn,'cfprVnicFcIfRn':cfprVnicFcIfRn,'cfprVnicFcIfConfigQualifier':cfprVnicFcIfConfigQualifier,'cfprVnicFcIfInitiator':cfprVnicFcIfInitiator,'cfprVnicFcIfName':cfprVnicFcIfName,'cfprVnicFcIfOperState':cfprVnicFcIfOperState,'cfprVnicFcIfOperVnetDn':cfprVnicFcIfOperVnetDn,'cfprVnicFcIfOperVnetName':cfprVnicFcIfOperVnetName,'cfprVnicFcIfOwner':cfprVnicFcIfOwner,'cfprVnicFcIfPubNwId':cfprVnicFcIfPubNwId,'cfprVnicFcIfSharing':cfprVnicFcIfSharing,'cfprVnicFcIfSwitchId':cfprVnicFcIfSwitchId,'cfprVnicFcIfType':cfprVnicFcIfType,'cfprVnicFcIfVnet':cfprVnicFcIfVnet,'cfprVnicFcLifTable':cfprVnicFcLifTable,'cfprVnicFcLifEntry':cfprVnicFcLifEntry,_V:cfprVnicFcLifInstanceId,'cfprVnicFcLifDn':cfprVnicFcLifDn,'cfprVnicFcLifRn':cfprVnicFcLifRn,'cfprVnicFcLifAddr':cfprVnicFcLifAddr,'cfprVnicFcLifName':cfprVnicFcLifName,'cfprVnicFcLifNicDn':cfprVnicFcLifNicDn,'cfprVnicFcLifOwner':cfprVnicFcLifOwner,'cfprVnicFcLifSwitchId':cfprVnicFcLifSwitchId,'cfprVnicFcLifType':cfprVnicFcLifType,'cfprVnicFcLifVnicDn':cfprVnicFcLifVnicDn,'cfprVnicFcNodeTable':cfprVnicFcNodeTable,'cfprVnicFcNodeEntry':cfprVnicFcNodeEntry,_W:cfprVnicFcNodeInstanceId,'cfprVnicFcNodeDn':cfprVnicFcNodeDn,'cfprVnicFcNodeRn':cfprVnicFcNodeRn,'cfprVnicFcNodeAddrData':cfprVnicFcNodeAddrData,'cfprVnicFcNodeFltAggr':cfprVnicFcNodeFltAggr,'cfprVnicFcNodeIdentPoolName':cfprVnicFcNodeIdentPoolName,'cfprVnicFcNodeMaxDerivableWWPN':cfprVnicFcNodeMaxDerivableWWPN,'cfprVnicFcNodeOperIdentPoolName':cfprVnicFcNodeOperIdentPoolName,'cfprVnicFcNodeOwner':cfprVnicFcNodeOwner,'cfprVnicFcOEIfTable':cfprVnicFcOEIfTable,'cfprVnicFcOEIfEntry':cfprVnicFcOEIfEntry,_X:cfprVnicFcOEIfInstanceId,'cfprVnicFcOEIfDn':cfprVnicFcOEIfDn,'cfprVnicFcOEIfRn':cfprVnicFcOEIfRn,'cfprVnicFcOEIfConfigQualifier':cfprVnicFcOEIfConfigQualifier,'cfprVnicFcOEIfInitiator':cfprVnicFcOEIfInitiator,'cfprVnicFcOEIfName':cfprVnicFcOEIfName,'cfprVnicFcOEIfOperState':cfprVnicFcOEIfOperState,'cfprVnicFcOEIfOperVnetDn':cfprVnicFcOEIfOperVnetDn,'cfprVnicFcOEIfOperVnetName':cfprVnicFcOEIfOperVnetName,'cfprVnicFcOEIfOwner':cfprVnicFcOEIfOwner,'cfprVnicFcOEIfPubNwId':cfprVnicFcOEIfPubNwId,'cfprVnicFcOEIfSharing':cfprVnicFcOEIfSharing,'cfprVnicFcOEIfSwitchId':cfprVnicFcOEIfSwitchId,'cfprVnicFcOEIfType':cfprVnicFcOEIfType,'cfprVnicFcOEIfVnet':cfprVnicFcOEIfVnet,'cfprVnicIPv4DhcpTable':cfprVnicIPv4DhcpTable,'cfprVnicIPv4DhcpEntry':cfprVnicIPv4DhcpEntry,_Y:cfprVnicIPv4DhcpInstanceId,'cfprVnicIPv4DhcpDn':cfprVnicIPv4DhcpDn,'cfprVnicIPv4DhcpRn':cfprVnicIPv4DhcpRn,'cfprVnicIPv4DhcpAddr':cfprVnicIPv4DhcpAddr,'cfprVnicIPv4DhcpDefGw':cfprVnicIPv4DhcpDefGw,'cfprVnicIPv4DhcpSubnet':cfprVnicIPv4DhcpSubnet,'cfprVnicIPv4DnsTable':cfprVnicIPv4DnsTable,'cfprVnicIPv4DnsEntry':cfprVnicIPv4DnsEntry,_Z:cfprVnicIPv4DnsInstanceId,'cfprVnicIPv4DnsDn':cfprVnicIPv4DnsDn,'cfprVnicIPv4DnsRn':cfprVnicIPv4DnsRn,'cfprVnicIPv4DnsAddr':cfprVnicIPv4DnsAddr,'cfprVnicIPv4DnsDefGw':cfprVnicIPv4DnsDefGw,'cfprVnicIPv4DnsPref':cfprVnicIPv4DnsPref,'cfprVnicIPv4DnsSubnet':cfprVnicIPv4DnsSubnet,'cfprVnicIPv4IfTable':cfprVnicIPv4IfTable,'cfprVnicIPv4IfEntry':cfprVnicIPv4IfEntry,_a:cfprVnicIPv4IfInstanceId,'cfprVnicIPv4IfDn':cfprVnicIPv4IfDn,'cfprVnicIPv4IfRn':cfprVnicIPv4IfRn,'cfprVnicIPv4IfAddr':cfprVnicIPv4IfAddr,'cfprVnicIPv4IfConfigQualifier':cfprVnicIPv4IfConfigQualifier,'cfprVnicIPv4IfName':cfprVnicIPv4IfName,'cfprVnicIPv4IfOperState':cfprVnicIPv4IfOperState,'cfprVnicIPv4IfOperVnetDn':cfprVnicIPv4IfOperVnetDn,'cfprVnicIPv4IfOperVnetName':cfprVnicIPv4IfOperVnetName,'cfprVnicIPv4IfOwner':cfprVnicIPv4IfOwner,'cfprVnicIPv4IfPubNwId':cfprVnicIPv4IfPubNwId,'cfprVnicIPv4IfSharing':cfprVnicIPv4IfSharing,'cfprVnicIPv4IfSwitchId':cfprVnicIPv4IfSwitchId,'cfprVnicIPv4IfType':cfprVnicIPv4IfType,'cfprVnicIPv4IfVnet':cfprVnicIPv4IfVnet,'cfprVnicIPv4IscsiAddrTable':cfprVnicIPv4IscsiAddrTable,'cfprVnicIPv4IscsiAddrEntry':cfprVnicIPv4IscsiAddrEntry,_b:cfprVnicIPv4IscsiAddrInstanceId,'cfprVnicIPv4IscsiAddrDn':cfprVnicIPv4IscsiAddrDn,'cfprVnicIPv4IscsiAddrRn':cfprVnicIPv4IscsiAddrRn,'cfprVnicIPv4IscsiAddrAddr':cfprVnicIPv4IscsiAddrAddr,'cfprVnicIPv4IscsiAddrDefGw':cfprVnicIPv4IscsiAddrDefGw,'cfprVnicIPv4IscsiAddrPrimDns':cfprVnicIPv4IscsiAddrPrimDns,'cfprVnicIPv4IscsiAddrSecDns':cfprVnicIPv4IscsiAddrSecDns,'cfprVnicIPv4IscsiAddrSubnet':cfprVnicIPv4IscsiAddrSubnet,'cfprVnicIPv4PooledIscsiAddrTable':cfprVnicIPv4PooledIscsiAddrTable,'cfprVnicIPv4PooledIscsiAddrEntry':cfprVnicIPv4PooledIscsiAddrEntry,_c:cfprVnicIPv4PooledIscsiAddrInstanceId,'cfprVnicIPv4PooledIscsiAddrDn':cfprVnicIPv4PooledIscsiAddrDn,'cfprVnicIPv4PooledIscsiAddrRn':cfprVnicIPv4PooledIscsiAddrRn,'cfprVnicIPv4PooledIscsiAddrAddr':cfprVnicIPv4PooledIscsiAddrAddr,'cfprVnicIPv4PooledIscsiAddrDefGw':cfprVnicIPv4PooledIscsiAddrDefGw,'cfprVnicIPv4PooledIscsiAddrIdentPoolName':cfprVnicIPv4PooledIscsiAddrIdentPoolName,'cfprVnicIPv4PooledIscsiAddrOperIdentPoolName':cfprVnicIPv4PooledIscsiAddrOperIdentPoolName,'cfprVnicIPv4PooledIscsiAddrPrimDns':cfprVnicIPv4PooledIscsiAddrPrimDns,'cfprVnicIPv4PooledIscsiAddrSecDns':cfprVnicIPv4PooledIscsiAddrSecDns,'cfprVnicIPv4PooledIscsiAddrSubnet':cfprVnicIPv4PooledIscsiAddrSubnet,'cfprVnicIPv4StaticRouteTable':cfprVnicIPv4StaticRouteTable,'cfprVnicIPv4StaticRouteEntry':cfprVnicIPv4StaticRouteEntry,_d:cfprVnicIPv4StaticRouteInstanceId,'cfprVnicIPv4StaticRouteDn':cfprVnicIPv4StaticRouteDn,'cfprVnicIPv4StaticRouteRn':cfprVnicIPv4StaticRouteRn,'cfprVnicIPv4StaticRouteAddr':cfprVnicIPv4StaticRouteAddr,'cfprVnicIPv4StaticRouteDefGw':cfprVnicIPv4StaticRouteDefGw,'cfprVnicIPv4StaticRouteGwAddr':cfprVnicIPv4StaticRouteGwAddr,'cfprVnicIPv4StaticRouteGwSubnet':cfprVnicIPv4StaticRouteGwSubnet,'cfprVnicIPv4StaticRouteSubnet':cfprVnicIPv4StaticRouteSubnet,'cfprVnicIScsiTable':cfprVnicIScsiTable,'cfprVnicIScsiEntry':cfprVnicIScsiEntry,_e:cfprVnicIScsiInstanceId,'cfprVnicIScsiDn':cfprVnicIScsiDn,'cfprVnicIScsiRn':cfprVnicIScsiRn,'cfprVnicIScsiAdaptorProfileName':cfprVnicIScsiAdaptorProfileName,'cfprVnicIScsiAddr':cfprVnicIScsiAddr,'cfprVnicIScsiAdminHostPort':cfprVnicIScsiAdminHostPort,'cfprVnicIScsiAdminVcon':cfprVnicIScsiAdminVcon,'cfprVnicIScsiAppRole':cfprVnicIScsiAppRole,'cfprVnicIScsiAuthProfileName':cfprVnicIScsiAuthProfileName,'cfprVnicIScsiBootDev':cfprVnicIScsiBootDev,'cfprVnicIScsiConfigQualifier':cfprVnicIScsiConfigQualifier,'cfprVnicIScsiConfigState':cfprVnicIScsiConfigState,'cfprVnicIScsiEquipmentDn':cfprVnicIScsiEquipmentDn,'cfprVnicIScsiEthEpDn':cfprVnicIScsiEthEpDn,'cfprVnicIScsiExtIPState':cfprVnicIScsiExtIPState,'cfprVnicIScsiFltAggr':cfprVnicIScsiFltAggr,'cfprVnicIScsiIdentPoolName':cfprVnicIScsiIdentPoolName,'cfprVnicIScsiInitNameSuffix':cfprVnicIScsiInitNameSuffix,'cfprVnicIScsiInitiatorName':cfprVnicIScsiInitiatorName,'cfprVnicIScsiInstType':cfprVnicIScsiInstType,'cfprVnicIScsiIqnIdentPoolName':cfprVnicIScsiIqnIdentPoolName,'cfprVnicIScsiName':cfprVnicIScsiName,'cfprVnicIScsiNwTemplName':cfprVnicIScsiNwTemplName,'cfprVnicIScsiOperAdaptorProfileName':cfprVnicIScsiOperAdaptorProfileName,'cfprVnicIScsiOperAuthProfileName':cfprVnicIScsiOperAuthProfileName,'cfprVnicIScsiOperHostPort':cfprVnicIScsiOperHostPort,'cfprVnicIScsiOperIdentPoolName':cfprVnicIScsiOperIdentPoolName,'cfprVnicIScsiOperIqnIdentPoolName':cfprVnicIScsiOperIqnIdentPoolName,'cfprVnicIScsiOperOrder':cfprVnicIScsiOperOrder,'cfprVnicIScsiOperSpeed':cfprVnicIScsiOperSpeed,'cfprVnicIScsiOperStatsPolicyName':cfprVnicIScsiOperStatsPolicyName,'cfprVnicIScsiOperVcon':cfprVnicIScsiOperVcon,'cfprVnicIScsiOrder':cfprVnicIScsiOrder,'cfprVnicIScsiOwner':cfprVnicIScsiOwner,'cfprVnicIScsiPinToGroupName':cfprVnicIScsiPinToGroupName,'cfprVnicIScsiQosPolicyName':cfprVnicIScsiQosPolicyName,'cfprVnicIScsiStatsPolicyName':cfprVnicIScsiStatsPolicyName,'cfprVnicIScsiSwitchId':cfprVnicIScsiSwitchId,'cfprVnicIScsiType':cfprVnicIScsiType,'cfprVnicIScsiVnicDefType':cfprVnicIScsiVnicDefType,'cfprVnicIScsiVnicName':cfprVnicIScsiVnicName,'cfprVnicIScsiAutoTargetIfTable':cfprVnicIScsiAutoTargetIfTable,'cfprVnicIScsiAutoTargetIfEntry':cfprVnicIScsiAutoTargetIfEntry,_f:cfprVnicIScsiAutoTargetIfInstanceId,'cfprVnicIScsiAutoTargetIfDn':cfprVnicIScsiAutoTargetIfDn,'cfprVnicIScsiAutoTargetIfRn':cfprVnicIScsiAutoTargetIfRn,'cfprVnicIScsiAutoTargetIfDhcpVendorId':cfprVnicIScsiAutoTargetIfDhcpVendorId,'cfprVnicIScsiBootParamsTable':cfprVnicIScsiBootParamsTable,'cfprVnicIScsiBootParamsEntry':cfprVnicIScsiBootParamsEntry,_g:cfprVnicIScsiBootParamsInstanceId,'cfprVnicIScsiBootParamsDn':cfprVnicIScsiBootParamsDn,'cfprVnicIScsiBootParamsRn':cfprVnicIScsiBootParamsRn,'cfprVnicIScsiBootParamsDescr':cfprVnicIScsiBootParamsDescr,'cfprVnicIScsiBootParamsIntId':cfprVnicIScsiBootParamsIntId,'cfprVnicIScsiBootParamsName':cfprVnicIScsiBootParamsName,'cfprVnicIScsiBootParamsPolicyLevel':cfprVnicIScsiBootParamsPolicyLevel,'cfprVnicIScsiBootParamsPolicyOwner':cfprVnicIScsiBootParamsPolicyOwner,'cfprVnicIScsiBootVnicTable':cfprVnicIScsiBootVnicTable,'cfprVnicIScsiBootVnicEntry':cfprVnicIScsiBootVnicEntry,_h:cfprVnicIScsiBootVnicInstanceId,'cfprVnicIScsiBootVnicDn':cfprVnicIScsiBootVnicDn,'cfprVnicIScsiBootVnicRn':cfprVnicIScsiBootVnicRn,'cfprVnicIScsiBootVnicAuthProfileName':cfprVnicIScsiBootVnicAuthProfileName,'cfprVnicIScsiBootVnicDescr':cfprVnicIScsiBootVnicDescr,'cfprVnicIScsiBootVnicInitiatorName':cfprVnicIScsiBootVnicInitiatorName,'cfprVnicIScsiBootVnicIntId':cfprVnicIScsiBootVnicIntId,'cfprVnicIScsiBootVnicIqnIdentPoolName':cfprVnicIScsiBootVnicIqnIdentPoolName,'cfprVnicIScsiBootVnicName':cfprVnicIScsiBootVnicName,'cfprVnicIScsiBootVnicOperAuthProfileName':cfprVnicIScsiBootVnicOperAuthProfileName,'cfprVnicIScsiBootVnicOperIqnIdentPoolName':cfprVnicIScsiBootVnicOperIqnIdentPoolName,'cfprVnicIScsiBootVnicPolicyLevel':cfprVnicIScsiBootVnicPolicyLevel,'cfprVnicIScsiBootVnicPolicyOwner':cfprVnicIScsiBootVnicPolicyOwner,'cfprVnicIScsiLCPTable':cfprVnicIScsiLCPTable,'cfprVnicIScsiLCPEntry':cfprVnicIScsiLCPEntry,_i:cfprVnicIScsiLCPInstanceId,'cfprVnicIScsiLCPDn':cfprVnicIScsiLCPDn,'cfprVnicIScsiLCPRn':cfprVnicIScsiLCPRn,'cfprVnicIScsiLCPAdaptorProfileName':cfprVnicIScsiLCPAdaptorProfileName,'cfprVnicIScsiLCPAddr':cfprVnicIScsiLCPAddr,'cfprVnicIScsiLCPAdminHostPort':cfprVnicIScsiLCPAdminHostPort,'cfprVnicIScsiLCPAdminVcon':cfprVnicIScsiLCPAdminVcon,'cfprVnicIScsiLCPAppRole':cfprVnicIScsiLCPAppRole,'cfprVnicIScsiLCPBootDev':cfprVnicIScsiLCPBootDev,'cfprVnicIScsiLCPConfigQualifier':cfprVnicIScsiLCPConfigQualifier,'cfprVnicIScsiLCPConfigState':cfprVnicIScsiLCPConfigState,'cfprVnicIScsiLCPEquipmentDn':cfprVnicIScsiLCPEquipmentDn,'cfprVnicIScsiLCPFltAggr':cfprVnicIScsiLCPFltAggr,'cfprVnicIScsiLCPIdentPoolName':cfprVnicIScsiLCPIdentPoolName,'cfprVnicIScsiLCPInstType':cfprVnicIScsiLCPInstType,'cfprVnicIScsiLCPName':cfprVnicIScsiLCPName,'cfprVnicIScsiLCPNwTemplName':cfprVnicIScsiLCPNwTemplName,'cfprVnicIScsiLCPOperAdaptorProfileName':cfprVnicIScsiLCPOperAdaptorProfileName,'cfprVnicIScsiLCPOperHostPort':cfprVnicIScsiLCPOperHostPort,'cfprVnicIScsiLCPOperIdentPoolName':cfprVnicIScsiLCPOperIdentPoolName,'cfprVnicIScsiLCPOperOrder':cfprVnicIScsiLCPOperOrder,'cfprVnicIScsiLCPOperSpeed':cfprVnicIScsiLCPOperSpeed,'cfprVnicIScsiLCPOperStatsPolicyName':cfprVnicIScsiLCPOperStatsPolicyName,'cfprVnicIScsiLCPOperVcon':cfprVnicIScsiLCPOperVcon,'cfprVnicIScsiLCPOrder':cfprVnicIScsiLCPOrder,'cfprVnicIScsiLCPOwner':cfprVnicIScsiLCPOwner,'cfprVnicIScsiLCPPinToGroupName':cfprVnicIScsiLCPPinToGroupName,'cfprVnicIScsiLCPQosPolicyName':cfprVnicIScsiLCPQosPolicyName,'cfprVnicIScsiLCPStatsPolicyName':cfprVnicIScsiLCPStatsPolicyName,'cfprVnicIScsiLCPSwitchId':cfprVnicIScsiLCPSwitchId,'cfprVnicIScsiLCPType':cfprVnicIScsiLCPType,'cfprVnicIScsiLCPVnicName':cfprVnicIScsiLCPVnicName,'cfprVnicIScsiNodeTable':cfprVnicIScsiNodeTable,'cfprVnicIScsiNodeEntry':cfprVnicIScsiNodeEntry,_j:cfprVnicIScsiNodeInstanceId,'cfprVnicIScsiNodeDn':cfprVnicIScsiNodeDn,'cfprVnicIScsiNodeRn':cfprVnicIScsiNodeRn,'cfprVnicIScsiNodeFltAggr':cfprVnicIScsiNodeFltAggr,'cfprVnicIScsiNodeInitNameSuffix':cfprVnicIScsiNodeInitNameSuffix,'cfprVnicIScsiNodeInitiatorName':cfprVnicIScsiNodeInitiatorName,'cfprVnicIScsiNodeIqnIdentPoolName':cfprVnicIScsiNodeIqnIdentPoolName,'cfprVnicIScsiNodeOperIqnIdentPoolName':cfprVnicIScsiNodeOperIqnIdentPoolName,'cfprVnicIScsiNodeOwner':cfprVnicIScsiNodeOwner,'cfprVnicIScsiStaticTargetIfTable':cfprVnicIScsiStaticTargetIfTable,'cfprVnicIScsiStaticTargetIfEntry':cfprVnicIScsiStaticTargetIfEntry,_k:cfprVnicIScsiStaticTargetIfInstanceId,'cfprVnicIScsiStaticTargetIfDn':cfprVnicIScsiStaticTargetIfDn,'cfprVnicIScsiStaticTargetIfRn':cfprVnicIScsiStaticTargetIfRn,'cfprVnicIScsiStaticTargetIfAuthProfileName':cfprVnicIScsiStaticTargetIfAuthProfileName,'cfprVnicIScsiStaticTargetIfIpAddress':cfprVnicIScsiStaticTargetIfIpAddress,'cfprVnicIScsiStaticTargetIfName':cfprVnicIScsiStaticTargetIfName,'cfprVnicIScsiStaticTargetIfOperAuthProfileName':cfprVnicIScsiStaticTargetIfOperAuthProfileName,'cfprVnicIScsiStaticTargetIfPort':cfprVnicIScsiStaticTargetIfPort,'cfprVnicIScsiStaticTargetIfPriority':cfprVnicIScsiStaticTargetIfPriority,'cfprVnicInternalProfileTable':cfprVnicInternalProfileTable,'cfprVnicInternalProfileEntry':cfprVnicInternalProfileEntry,_l:cfprVnicInternalProfileInstanceId,'cfprVnicInternalProfileDn':cfprVnicInternalProfileDn,'cfprVnicInternalProfileRn':cfprVnicInternalProfileRn,'cfprVnicInternalProfileDescr':cfprVnicInternalProfileDescr,'cfprVnicInternalProfileIntId':cfprVnicInternalProfileIntId,'cfprVnicInternalProfileMaxPorts':cfprVnicInternalProfileMaxPorts,'cfprVnicInternalProfileName':cfprVnicInternalProfileName,'cfprVnicInternalProfilePolicyLevel':cfprVnicInternalProfilePolicyLevel,'cfprVnicInternalProfilePolicyOwner':cfprVnicInternalProfilePolicyOwner,'cfprVnicIpV4HistoryTable':cfprVnicIpV4HistoryTable,'cfprVnicIpV4HistoryEntry':cfprVnicIpV4HistoryEntry,_m:cfprVnicIpV4HistoryInstanceId,'cfprVnicIpV4HistoryDn':cfprVnicIpV4HistoryDn,'cfprVnicIpV4HistoryRn':cfprVnicIpV4HistoryRn,'cfprVnicIpV4HistoryOldIpV4Addr':cfprVnicIpV4HistoryOldIpV4Addr,'cfprVnicIpV4MgmtPooledAddrTable':cfprVnicIpV4MgmtPooledAddrTable,'cfprVnicIpV4MgmtPooledAddrEntry':cfprVnicIpV4MgmtPooledAddrEntry,_n:cfprVnicIpV4MgmtPooledAddrInstanceId,'cfprVnicIpV4MgmtPooledAddrDn':cfprVnicIpV4MgmtPooledAddrDn,'cfprVnicIpV4MgmtPooledAddrRn':cfprVnicIpV4MgmtPooledAddrRn,'cfprVnicIpV4MgmtPooledAddrAddr':cfprVnicIpV4MgmtPooledAddrAddr,'cfprVnicIpV4MgmtPooledAddrDefGw':cfprVnicIpV4MgmtPooledAddrDefGw,'cfprVnicIpV4MgmtPooledAddrName':cfprVnicIpV4MgmtPooledAddrName,'cfprVnicIpV4MgmtPooledAddrOperName':cfprVnicIpV4MgmtPooledAddrOperName,'cfprVnicIpV4MgmtPooledAddrPrimDns':cfprVnicIpV4MgmtPooledAddrPrimDns,'cfprVnicIpV4MgmtPooledAddrSecDns':cfprVnicIpV4MgmtPooledAddrSecDns,'cfprVnicIpV4MgmtPooledAddrSubnet':cfprVnicIpV4MgmtPooledAddrSubnet,'cfprVnicIpV4PooledAddrTable':cfprVnicIpV4PooledAddrTable,'cfprVnicIpV4PooledAddrEntry':cfprVnicIpV4PooledAddrEntry,_o:cfprVnicIpV4PooledAddrInstanceId,'cfprVnicIpV4PooledAddrDn':cfprVnicIpV4PooledAddrDn,'cfprVnicIpV4PooledAddrRn':cfprVnicIpV4PooledAddrRn,'cfprVnicIpV4PooledAddrAddr':cfprVnicIpV4PooledAddrAddr,'cfprVnicIpV4PooledAddrDefGw':cfprVnicIpV4PooledAddrDefGw,'cfprVnicIpV4PooledAddrName':cfprVnicIpV4PooledAddrName,'cfprVnicIpV4PooledAddrOperName':cfprVnicIpV4PooledAddrOperName,'cfprVnicIpV4PooledAddrPrimDns':cfprVnicIpV4PooledAddrPrimDns,'cfprVnicIpV4PooledAddrSecDns':cfprVnicIpV4PooledAddrSecDns,'cfprVnicIpV4PooledAddrSubnet':cfprVnicIpV4PooledAddrSubnet,'cfprVnicIpV4ProfDerivedAddrTable':cfprVnicIpV4ProfDerivedAddrTable,'cfprVnicIpV4ProfDerivedAddrEntry':cfprVnicIpV4ProfDerivedAddrEntry,_p:cfprVnicIpV4ProfDerivedAddrInstanceId,'cfprVnicIpV4ProfDerivedAddrDn':cfprVnicIpV4ProfDerivedAddrDn,'cfprVnicIpV4ProfDerivedAddrRn':cfprVnicIpV4ProfDerivedAddrRn,'cfprVnicIpV4ProfDerivedAddrAddr':cfprVnicIpV4ProfDerivedAddrAddr,'cfprVnicIpV4ProfDerivedAddrDefGw':cfprVnicIpV4ProfDerivedAddrDefGw,'cfprVnicIpV4ProfDerivedAddrSubnet':cfprVnicIpV4ProfDerivedAddrSubnet,'cfprVnicIpV4StaticAddrTable':cfprVnicIpV4StaticAddrTable,'cfprVnicIpV4StaticAddrEntry':cfprVnicIpV4StaticAddrEntry,_q:cfprVnicIpV4StaticAddrInstanceId,'cfprVnicIpV4StaticAddrDn':cfprVnicIpV4StaticAddrDn,'cfprVnicIpV4StaticAddrRn':cfprVnicIpV4StaticAddrRn,'cfprVnicIpV4StaticAddrAddr':cfprVnicIpV4StaticAddrAddr,'cfprVnicIpV4StaticAddrDefGw':cfprVnicIpV4StaticAddrDefGw,'cfprVnicIpV4StaticAddrPrimDns':cfprVnicIpV4StaticAddrPrimDns,'cfprVnicIpV4StaticAddrSecDns':cfprVnicIpV4StaticAddrSecDns,'cfprVnicIpV4StaticAddrSubnet':cfprVnicIpV4StaticAddrSubnet,'cfprVnicIpV6HistoryTable':cfprVnicIpV6HistoryTable,'cfprVnicIpV6HistoryEntry':cfprVnicIpV6HistoryEntry,_r:cfprVnicIpV6HistoryInstanceId,'cfprVnicIpV6HistoryDn':cfprVnicIpV6HistoryDn,'cfprVnicIpV6HistoryRn':cfprVnicIpV6HistoryRn,'cfprVnicIpV6HistoryOldIpV6Addr':cfprVnicIpV6HistoryOldIpV6Addr,'cfprVnicIpV6MgmtPooledAddrTable':cfprVnicIpV6MgmtPooledAddrTable,'cfprVnicIpV6MgmtPooledAddrEntry':cfprVnicIpV6MgmtPooledAddrEntry,_s:cfprVnicIpV6MgmtPooledAddrInstanceId,'cfprVnicIpV6MgmtPooledAddrDn':cfprVnicIpV6MgmtPooledAddrDn,'cfprVnicIpV6MgmtPooledAddrRn':cfprVnicIpV6MgmtPooledAddrRn,'cfprVnicIpV6MgmtPooledAddrAddr':cfprVnicIpV6MgmtPooledAddrAddr,'cfprVnicIpV6MgmtPooledAddrDefGw':cfprVnicIpV6MgmtPooledAddrDefGw,'cfprVnicIpV6MgmtPooledAddrName':cfprVnicIpV6MgmtPooledAddrName,'cfprVnicIpV6MgmtPooledAddrOperName':cfprVnicIpV6MgmtPooledAddrOperName,'cfprVnicIpV6MgmtPooledAddrPrefix':cfprVnicIpV6MgmtPooledAddrPrefix,'cfprVnicIpV6MgmtPooledAddrPrimDns':cfprVnicIpV6MgmtPooledAddrPrimDns,'cfprVnicIpV6MgmtPooledAddrSecDns':cfprVnicIpV6MgmtPooledAddrSecDns,'cfprVnicIpV6StaticAddrTable':cfprVnicIpV6StaticAddrTable,'cfprVnicIpV6StaticAddrEntry':cfprVnicIpV6StaticAddrEntry,_t:cfprVnicIpV6StaticAddrInstanceId,'cfprVnicIpV6StaticAddrDn':cfprVnicIpV6StaticAddrDn,'cfprVnicIpV6StaticAddrRn':cfprVnicIpV6StaticAddrRn,'cfprVnicIpV6StaticAddrAddr':cfprVnicIpV6StaticAddrAddr,'cfprVnicIpV6StaticAddrDefGw':cfprVnicIpV6StaticAddrDefGw,'cfprVnicIpV6StaticAddrPrefix':cfprVnicIpV6StaticAddrPrefix,'cfprVnicIpV6StaticAddrPrimDns':cfprVnicIpV6StaticAddrPrimDns,'cfprVnicIpV6StaticAddrSecDns':cfprVnicIpV6StaticAddrSecDns,'cfprVnicIpcTable':cfprVnicIpcTable,'cfprVnicIpcEntry':cfprVnicIpcEntry,_u:cfprVnicIpcInstanceId,'cfprVnicIpcDn':cfprVnicIpcDn,'cfprVnicIpcRn':cfprVnicIpcRn,'cfprVnicIpcAdaptorProfileName':cfprVnicIpcAdaptorProfileName,'cfprVnicIpcAddr':cfprVnicIpcAddr,'cfprVnicIpcAdminHostPort':cfprVnicIpcAdminHostPort,'cfprVnicIpcAdminVcon':cfprVnicIpcAdminVcon,'cfprVnicIpcAppRole':cfprVnicIpcAppRole,'cfprVnicIpcBootDev':cfprVnicIpcBootDev,'cfprVnicIpcConfigQualifier':cfprVnicIpcConfigQualifier,'cfprVnicIpcConfigState':cfprVnicIpcConfigState,'cfprVnicIpcEquipmentDn':cfprVnicIpcEquipmentDn,'cfprVnicIpcIdentPoolName':cfprVnicIpcIdentPoolName,'cfprVnicIpcInstType':cfprVnicIpcInstType,'cfprVnicIpcMtu':cfprVnicIpcMtu,'cfprVnicIpcName':cfprVnicIpcName,'cfprVnicIpcNwCtrlPolicyName':cfprVnicIpcNwCtrlPolicyName,'cfprVnicIpcNwTemplName':cfprVnicIpcNwTemplName,'cfprVnicIpcOperAdaptorProfileName':cfprVnicIpcOperAdaptorProfileName,'cfprVnicIpcOperHostPort':cfprVnicIpcOperHostPort,'cfprVnicIpcOperIdentPoolName':cfprVnicIpcOperIdentPoolName,'cfprVnicIpcOperNwCtrlPolicyName':cfprVnicIpcOperNwCtrlPolicyName,'cfprVnicIpcOperNwTemplName':cfprVnicIpcOperNwTemplName,'cfprVnicIpcOperOrder':cfprVnicIpcOperOrder,'cfprVnicIpcOperPinToGroupName':cfprVnicIpcOperPinToGroupName,'cfprVnicIpcOperQosPolicyName':cfprVnicIpcOperQosPolicyName,'cfprVnicIpcOperSpeed':cfprVnicIpcOperSpeed,'cfprVnicIpcOperStatsPolicyName':cfprVnicIpcOperStatsPolicyName,'cfprVnicIpcOperVcon':cfprVnicIpcOperVcon,'cfprVnicIpcOrder':cfprVnicIpcOrder,'cfprVnicIpcOwner':cfprVnicIpcOwner,'cfprVnicIpcPinToGroupName':cfprVnicIpcPinToGroupName,'cfprVnicIpcQosPolicyName':cfprVnicIpcQosPolicyName,'cfprVnicIpcStatsPolicyName':cfprVnicIpcStatsPolicyName,'cfprVnicIpcSwitchId':cfprVnicIpcSwitchId,'cfprVnicIpcType':cfprVnicIpcType,'cfprVnicIpcIfTable':cfprVnicIpcIfTable,'cfprVnicIpcIfEntry':cfprVnicIpcIfEntry,_v:cfprVnicIpcIfInstanceId,'cfprVnicIpcIfDn':cfprVnicIpcIfDn,'cfprVnicIpcIfRn':cfprVnicIpcIfRn,'cfprVnicIpcIfAddr':cfprVnicIpcIfAddr,'cfprVnicIpcIfConfigQualifier':cfprVnicIpcIfConfigQualifier,'cfprVnicIpcIfDefaultNet':cfprVnicIpcIfDefaultNet,'cfprVnicIpcIfName':cfprVnicIpcIfName,'cfprVnicIpcIfOperState':cfprVnicIpcIfOperState,'cfprVnicIpcIfOperVnetDn':cfprVnicIpcIfOperVnetDn,'cfprVnicIpcIfOperVnetName':cfprVnicIpcIfOperVnetName,'cfprVnicIpcIfOwner':cfprVnicIpcIfOwner,'cfprVnicIpcIfPubNwId':cfprVnicIpcIfPubNwId,'cfprVnicIpcIfSharing':cfprVnicIpcIfSharing,'cfprVnicIpcIfSwitchId':cfprVnicIpcIfSwitchId,'cfprVnicIpcIfType':cfprVnicIpcIfType,'cfprVnicIpcIfVnet':cfprVnicIpcIfVnet,'cfprVnicIqnHistoryTable':cfprVnicIqnHistoryTable,'cfprVnicIqnHistoryEntry':cfprVnicIqnHistoryEntry,_w:cfprVnicIqnHistoryInstanceId,'cfprVnicIqnHistoryDn':cfprVnicIqnHistoryDn,'cfprVnicIqnHistoryRn':cfprVnicIqnHistoryRn,'cfprVnicIqnHistoryOldInitiatorName':cfprVnicIqnHistoryOldInitiatorName,'cfprVnicLanConnPolicyTable':cfprVnicLanConnPolicyTable,'cfprVnicLanConnPolicyEntry':cfprVnicLanConnPolicyEntry,_x:cfprVnicLanConnPolicyInstanceId,'cfprVnicLanConnPolicyDn':cfprVnicLanConnPolicyDn,'cfprVnicLanConnPolicyRn':cfprVnicLanConnPolicyRn,'cfprVnicLanConnPolicyDescr':cfprVnicLanConnPolicyDescr,'cfprVnicLanConnPolicyFltAggr':cfprVnicLanConnPolicyFltAggr,'cfprVnicLanConnPolicyIntId':cfprVnicLanConnPolicyIntId,'cfprVnicLanConnPolicyName':cfprVnicLanConnPolicyName,'cfprVnicLanConnPolicyPolicyLevel':cfprVnicLanConnPolicyPolicyLevel,'cfprVnicLanConnPolicyPolicyOwner':cfprVnicLanConnPolicyPolicyOwner,'cfprVnicLanConnTemplTable':cfprVnicLanConnTemplTable,'cfprVnicLanConnTemplEntry':cfprVnicLanConnTemplEntry,_y:cfprVnicLanConnTemplInstanceId,'cfprVnicLanConnTemplDn':cfprVnicLanConnTemplDn,'cfprVnicLanConnTemplRn':cfprVnicLanConnTemplRn,'cfprVnicLanConnTemplDescr':cfprVnicLanConnTemplDescr,'cfprVnicLanConnTemplIdentPoolName':cfprVnicLanConnTemplIdentPoolName,'cfprVnicLanConnTemplIntId':cfprVnicLanConnTemplIntId,'cfprVnicLanConnTemplMtu':cfprVnicLanConnTemplMtu,'cfprVnicLanConnTemplName':cfprVnicLanConnTemplName,'cfprVnicLanConnTemplNwCtrlPolicyName':cfprVnicLanConnTemplNwCtrlPolicyName,'cfprVnicLanConnTemplOperIdentPoolName':cfprVnicLanConnTemplOperIdentPoolName,'cfprVnicLanConnTemplOperNwCtrlPolicyName':cfprVnicLanConnTemplOperNwCtrlPolicyName,'cfprVnicLanConnTemplOperQosPolicyName':cfprVnicLanConnTemplOperQosPolicyName,'cfprVnicLanConnTemplOperStatsPolicyName':cfprVnicLanConnTemplOperStatsPolicyName,'cfprVnicLanConnTemplPinToGroupName':cfprVnicLanConnTemplPinToGroupName,'cfprVnicLanConnTemplPolicyLevel':cfprVnicLanConnTemplPolicyLevel,'cfprVnicLanConnTemplPolicyOwner':cfprVnicLanConnTemplPolicyOwner,'cfprVnicLanConnTemplQosPolicyName':cfprVnicLanConnTemplQosPolicyName,'cfprVnicLanConnTemplStatsPolicyName':cfprVnicLanConnTemplStatsPolicyName,'cfprVnicLanConnTemplSwitchId':cfprVnicLanConnTemplSwitchId,'cfprVnicLanConnTemplTarget':cfprVnicLanConnTemplTarget,'cfprVnicLanConnTemplTemplType':cfprVnicLanConnTemplTemplType,'cfprVnicLifVlanTable':cfprVnicLifVlanTable,'cfprVnicLifVlanEntry':cfprVnicLifVlanEntry,_z:cfprVnicLifVlanInstanceId,'cfprVnicLifVlanDn':cfprVnicLifVlanDn,'cfprVnicLifVlanRn':cfprVnicLifVlanRn,'cfprVnicLifVlanAddr':cfprVnicLifVlanAddr,'cfprVnicLifVlanConfigQualifier':cfprVnicLifVlanConfigQualifier,'cfprVnicLifVlanDefaultNet':cfprVnicLifVlanDefaultNet,'cfprVnicLifVlanName':cfprVnicLifVlanName,'cfprVnicLifVlanOperState':cfprVnicLifVlanOperState,'cfprVnicLifVlanOperVnetDn':cfprVnicLifVlanOperVnetDn,'cfprVnicLifVlanOperVnetName':cfprVnicLifVlanOperVnetName,'cfprVnicLifVlanOwner':cfprVnicLifVlanOwner,'cfprVnicLifVlanPubNwId':cfprVnicLifVlanPubNwId,'cfprVnicLifVlanSharing':cfprVnicLifVlanSharing,'cfprVnicLifVlanSwitchId':cfprVnicLifVlanSwitchId,'cfprVnicLifVlanType':cfprVnicLifVlanType,'cfprVnicLifVlanVnet':cfprVnicLifVlanVnet,'cfprVnicLifVsanTable':cfprVnicLifVsanTable,'cfprVnicLifVsanEntry':cfprVnicLifVsanEntry,_A0:cfprVnicLifVsanInstanceId,'cfprVnicLifVsanDn':cfprVnicLifVsanDn,'cfprVnicLifVsanRn':cfprVnicLifVsanRn,'cfprVnicLifVsanConfigQualifier':cfprVnicLifVsanConfigQualifier,'cfprVnicLifVsanInitiator':cfprVnicLifVsanInitiator,'cfprVnicLifVsanName':cfprVnicLifVsanName,'cfprVnicLifVsanOperState':cfprVnicLifVsanOperState,'cfprVnicLifVsanOperVnetDn':cfprVnicLifVsanOperVnetDn,'cfprVnicLifVsanOperVnetName':cfprVnicLifVsanOperVnetName,'cfprVnicLifVsanOwner':cfprVnicLifVsanOwner,'cfprVnicLifVsanPubNwId':cfprVnicLifVsanPubNwId,'cfprVnicLifVsanSharing':cfprVnicLifVsanSharing,'cfprVnicLifVsanSwitchId':cfprVnicLifVsanSwitchId,'cfprVnicLifVsanType':cfprVnicLifVsanType,'cfprVnicLifVsanVnet':cfprVnicLifVsanVnet,'cfprVnicLunTable':cfprVnicLunTable,'cfprVnicLunEntry':cfprVnicLunEntry,_A1:cfprVnicLunInstanceId,'cfprVnicLunDn':cfprVnicLunDn,'cfprVnicLunRn':cfprVnicLunRn,'cfprVnicLunBootable':cfprVnicLunBootable,'cfprVnicLunId':cfprVnicLunId,'cfprVnicMacHistoryTable':cfprVnicMacHistoryTable,'cfprVnicMacHistoryEntry':cfprVnicMacHistoryEntry,_A2:cfprVnicMacHistoryInstanceId,'cfprVnicMacHistoryDn':cfprVnicMacHistoryDn,'cfprVnicMacHistoryRn':cfprVnicMacHistoryRn,'cfprVnicMacHistoryOldaddr':cfprVnicMacHistoryOldaddr,'cfprVnicOProfileAliasTable':cfprVnicOProfileAliasTable,'cfprVnicOProfileAliasEntry':cfprVnicOProfileAliasEntry,_A3:cfprVnicOProfileAliasInstanceId,'cfprVnicOProfileAliasDn':cfprVnicOProfileAliasDn,'cfprVnicOProfileAliasRn':cfprVnicOProfileAliasRn,'cfprVnicOProfileAliasAlias':cfprVnicOProfileAliasAlias,'cfprVnicOProfileAliasMgmtPlane':cfprVnicOProfileAliasMgmtPlane,'cfprVnicOProfileAliasVSwitchId':cfprVnicOProfileAliasVSwitchId,'cfprVnicOProfileAliasVSwitchName':cfprVnicOProfileAliasVSwitchName,'cfprVnicProfileTable':cfprVnicProfileTable,'cfprVnicProfileEntry':cfprVnicProfileEntry,_A4:cfprVnicProfileInstanceId,'cfprVnicProfileDn':cfprVnicProfileDn,'cfprVnicProfileRn':cfprVnicProfileRn,'cfprVnicProfileCdp':cfprVnicProfileCdp,'cfprVnicProfileConfigQualifier':cfprVnicProfileConfigQualifier,'cfprVnicProfileCos':cfprVnicProfileCos,'cfprVnicProfileDescr':cfprVnicProfileDescr,'cfprVnicProfileForgeMac':cfprVnicProfileForgeMac,'cfprVnicProfileHostNwIOPerf':cfprVnicProfileHostNwIOPerf,'cfprVnicProfileIntId':cfprVnicProfileIntId,'cfprVnicProfileMacRegisterMode':cfprVnicProfileMacRegisterMode,'cfprVnicProfileMaxPorts':cfprVnicProfileMaxPorts,'cfprVnicProfileName':cfprVnicProfileName,'cfprVnicProfileNwCtrlPolicyName':cfprVnicProfileNwCtrlPolicyName,'cfprVnicProfileOperNwCtrlPolicyName':cfprVnicProfileOperNwCtrlPolicyName,'cfprVnicProfileOperQosPolicyName':cfprVnicProfileOperQosPolicyName,'cfprVnicProfilePinToGroupName':cfprVnicProfilePinToGroupName,'cfprVnicProfilePolicyLevel':cfprVnicProfilePolicyLevel,'cfprVnicProfilePolicyOwner':cfprVnicProfilePolicyOwner,'cfprVnicProfilePortProfileUuid':cfprVnicProfilePortProfileUuid,'cfprVnicProfilePrimaryVlanId':cfprVnicProfilePrimaryVlanId,'cfprVnicProfileQosPolicyDn':cfprVnicProfileQosPolicyDn,'cfprVnicProfileQosPolicyId':cfprVnicProfileQosPolicyId,'cfprVnicProfileQosPolicyName':cfprVnicProfileQosPolicyName,'cfprVnicProfileSwABorderAggrPort':cfprVnicProfileSwABorderAggrPort,'cfprVnicProfileSwABorderPort':cfprVnicProfileSwABorderPort,'cfprVnicProfileSwABorderSlot':cfprVnicProfileSwABorderSlot,'cfprVnicProfileSwBBorderAggrPort':cfprVnicProfileSwBBorderAggrPort,'cfprVnicProfileSwBBorderPort':cfprVnicProfileSwBBorderPort,'cfprVnicProfileSwBBorderSlot':cfprVnicProfileSwBBorderSlot,'cfprVnicProfileType':cfprVnicProfileType,'cfprVnicProfileUplinkFailAction':cfprVnicProfileUplinkFailAction,'cfprVnicProfileAliasTable':cfprVnicProfileAliasTable,'cfprVnicProfileAliasEntry':cfprVnicProfileAliasEntry,_A5:cfprVnicProfileAliasInstanceId,'cfprVnicProfileAliasDn':cfprVnicProfileAliasDn,'cfprVnicProfileAliasRn':cfprVnicProfileAliasRn,'cfprVnicProfileAliasAlias':cfprVnicProfileAliasAlias,'cfprVnicProfileAliasSwUuid':cfprVnicProfileAliasSwUuid,'cfprVnicProfileRefTable':cfprVnicProfileRefTable,'cfprVnicProfileRefEntry':cfprVnicProfileRefEntry,_A6:cfprVnicProfileRefInstanceId,'cfprVnicProfileRefDn':cfprVnicProfileRefDn,'cfprVnicProfileRefRn':cfprVnicProfileRefRn,'cfprVnicProfileRefName':cfprVnicProfileRefName,'cfprVnicProfileRefSourceDn':cfprVnicProfileRefSourceDn,'cfprVnicProfileSetTable':cfprVnicProfileSetTable,'cfprVnicProfileSetEntry':cfprVnicProfileSetEntry,_A7:cfprVnicProfileSetInstanceId,'cfprVnicProfileSetDn':cfprVnicProfileSetDn,'cfprVnicProfileSetRn':cfprVnicProfileSetRn,'cfprVnicProfileSetFltAggr':cfprVnicProfileSetFltAggr,'cfprVnicProfileSetFsmDescr':cfprVnicProfileSetFsmDescr,'cfprVnicProfileSetFsmPrev':cfprVnicProfileSetFsmPrev,'cfprVnicProfileSetFsmProgr':cfprVnicProfileSetFsmProgr,'cfprVnicProfileSetFsmRmtInvErrCode':cfprVnicProfileSetFsmRmtInvErrCode,'cfprVnicProfileSetFsmRmtInvErrDescr':cfprVnicProfileSetFsmRmtInvErrDescr,'cfprVnicProfileSetFsmRmtInvRslt':cfprVnicProfileSetFsmRmtInvRslt,'cfprVnicProfileSetFsmStageDescr':cfprVnicProfileSetFsmStageDescr,'cfprVnicProfileSetFsmStamp':cfprVnicProfileSetFsmStamp,'cfprVnicProfileSetFsmStatus':cfprVnicProfileSetFsmStatus,'cfprVnicProfileSetFsmTry':cfprVnicProfileSetFsmTry,'cfprVnicProfileSetGenNum':cfprVnicProfileSetGenNum,'cfprVnicProfileSetFsmTable':cfprVnicProfileSetFsmTable,'cfprVnicProfileSetFsmEntry':cfprVnicProfileSetFsmEntry,_A8:cfprVnicProfileSetFsmInstanceId,'cfprVnicProfileSetFsmDn':cfprVnicProfileSetFsmDn,'cfprVnicProfileSetFsmRn':cfprVnicProfileSetFsmRn,'cfprVnicProfileSetFsmCompletionTime':cfprVnicProfileSetFsmCompletionTime,'cfprVnicProfileSetFsmCurrentFsm':cfprVnicProfileSetFsmCurrentFsm,'cfprVnicProfileSetFsmDescrData':cfprVnicProfileSetFsmDescrData,'cfprVnicProfileSetFsmFsmStatus':cfprVnicProfileSetFsmFsmStatus,'cfprVnicProfileSetFsmProgress':cfprVnicProfileSetFsmProgress,'cfprVnicProfileSetFsmRmtErrCode':cfprVnicProfileSetFsmRmtErrCode,'cfprVnicProfileSetFsmRmtErrDescr':cfprVnicProfileSetFsmRmtErrDescr,'cfprVnicProfileSetFsmRmtRslt':cfprVnicProfileSetFsmRmtRslt,'cfprVnicProfileSetFsmStageTable':cfprVnicProfileSetFsmStageTable,'cfprVnicProfileSetFsmStageEntry':cfprVnicProfileSetFsmStageEntry,_A9:cfprVnicProfileSetFsmStageInstanceId,'cfprVnicProfileSetFsmStageDn':cfprVnicProfileSetFsmStageDn,'cfprVnicProfileSetFsmStageRn':cfprVnicProfileSetFsmStageRn,'cfprVnicProfileSetFsmStageDescrData':cfprVnicProfileSetFsmStageDescrData,'cfprVnicProfileSetFsmStageLastUpdateTime':cfprVnicProfileSetFsmStageLastUpdateTime,'cfprVnicProfileSetFsmStageName':cfprVnicProfileSetFsmStageName,'cfprVnicProfileSetFsmStageOrder':cfprVnicProfileSetFsmStageOrder,'cfprVnicProfileSetFsmStageRetry':cfprVnicProfileSetFsmStageRetry,'cfprVnicProfileSetFsmStageStageStatus':cfprVnicProfileSetFsmStageStageStatus,'cfprVnicProfileSetFsmTaskTable':cfprVnicProfileSetFsmTaskTable,'cfprVnicProfileSetFsmTaskEntry':cfprVnicProfileSetFsmTaskEntry,_AA:cfprVnicProfileSetFsmTaskInstanceId,'cfprVnicProfileSetFsmTaskDn':cfprVnicProfileSetFsmTaskDn,'cfprVnicProfileSetFsmTaskRn':cfprVnicProfileSetFsmTaskRn,'cfprVnicProfileSetFsmTaskCompletion':cfprVnicProfileSetFsmTaskCompletion,'cfprVnicProfileSetFsmTaskFlags':cfprVnicProfileSetFsmTaskFlags,'cfprVnicProfileSetFsmTaskItem':cfprVnicProfileSetFsmTaskItem,'cfprVnicProfileSetFsmTaskSeqId':cfprVnicProfileSetFsmTaskSeqId,'cfprVnicRackServerDiscoveryProfileTable':cfprVnicRackServerDiscoveryProfileTable,'cfprVnicRackServerDiscoveryProfileEntry':cfprVnicRackServerDiscoveryProfileEntry,_AB:cfprVnicRackServerDiscoveryProfileInstanceId,'cfprVnicRackServerDiscoveryProfileDn':cfprVnicRackServerDiscoveryProfileDn,'cfprVnicRackServerDiscoveryProfileRn':cfprVnicRackServerDiscoveryProfileRn,'cfprVnicRackServerDiscoveryProfileDescr':cfprVnicRackServerDiscoveryProfileDescr,'cfprVnicRackServerDiscoveryProfileIntId':cfprVnicRackServerDiscoveryProfileIntId,'cfprVnicRackServerDiscoveryProfileMaxPorts':cfprVnicRackServerDiscoveryProfileMaxPorts,'cfprVnicRackServerDiscoveryProfileName':cfprVnicRackServerDiscoveryProfileName,'cfprVnicRackServerDiscoveryProfilePolicyLevel':cfprVnicRackServerDiscoveryProfilePolicyLevel,'cfprVnicRackServerDiscoveryProfilePolicyOwner':cfprVnicRackServerDiscoveryProfilePolicyOwner,'cfprVnicSanConnPolicyTable':cfprVnicSanConnPolicyTable,'cfprVnicSanConnPolicyEntry':cfprVnicSanConnPolicyEntry,_AC:cfprVnicSanConnPolicyInstanceId,'cfprVnicSanConnPolicyDn':cfprVnicSanConnPolicyDn,'cfprVnicSanConnPolicyRn':cfprVnicSanConnPolicyRn,'cfprVnicSanConnPolicyDescr':cfprVnicSanConnPolicyDescr,'cfprVnicSanConnPolicyFltAggr':cfprVnicSanConnPolicyFltAggr,'cfprVnicSanConnPolicyIntId':cfprVnicSanConnPolicyIntId,'cfprVnicSanConnPolicyName':cfprVnicSanConnPolicyName,'cfprVnicSanConnPolicyPolicyLevel':cfprVnicSanConnPolicyPolicyLevel,'cfprVnicSanConnPolicyPolicyOwner':cfprVnicSanConnPolicyPolicyOwner,'cfprVnicSanConnTemplTable':cfprVnicSanConnTemplTable,'cfprVnicSanConnTemplEntry':cfprVnicSanConnTemplEntry,_AD:cfprVnicSanConnTemplInstanceId,'cfprVnicSanConnTemplDn':cfprVnicSanConnTemplDn,'cfprVnicSanConnTemplRn':cfprVnicSanConnTemplRn,'cfprVnicSanConnTemplDescr':cfprVnicSanConnTemplDescr,'cfprVnicSanConnTemplIdentPoolName':cfprVnicSanConnTemplIdentPoolName,'cfprVnicSanConnTemplIntId':cfprVnicSanConnTemplIntId,'cfprVnicSanConnTemplMaxDataFieldSize':cfprVnicSanConnTemplMaxDataFieldSize,'cfprVnicSanConnTemplName':cfprVnicSanConnTemplName,'cfprVnicSanConnTemplNwCtrlPolicyName':cfprVnicSanConnTemplNwCtrlPolicyName,'cfprVnicSanConnTemplOperIdentPoolName':cfprVnicSanConnTemplOperIdentPoolName,'cfprVnicSanConnTemplOperQosPolicyName':cfprVnicSanConnTemplOperQosPolicyName,'cfprVnicSanConnTemplOperStatsPolicyName':cfprVnicSanConnTemplOperStatsPolicyName,'cfprVnicSanConnTemplPinToGroupName':cfprVnicSanConnTemplPinToGroupName,'cfprVnicSanConnTemplPolicyLevel':cfprVnicSanConnTemplPolicyLevel,'cfprVnicSanConnTemplPolicyOwner':cfprVnicSanConnTemplPolicyOwner,'cfprVnicSanConnTemplQosPolicyName':cfprVnicSanConnTemplQosPolicyName,'cfprVnicSanConnTemplStatsPolicyName':cfprVnicSanConnTemplStatsPolicyName,'cfprVnicSanConnTemplSwitchId':cfprVnicSanConnTemplSwitchId,'cfprVnicSanConnTemplTarget':cfprVnicSanConnTemplTarget,'cfprVnicSanConnTemplTemplType':cfprVnicSanConnTemplTemplType,'cfprVnicScsiTable':cfprVnicScsiTable,'cfprVnicScsiEntry':cfprVnicScsiEntry,_AE:cfprVnicScsiInstanceId,'cfprVnicScsiDn':cfprVnicScsiDn,'cfprVnicScsiRn':cfprVnicScsiRn,'cfprVnicScsiAdaptorProfileName':cfprVnicScsiAdaptorProfileName,'cfprVnicScsiAdminHostPort':cfprVnicScsiAdminHostPort,'cfprVnicScsiAdminVcon':cfprVnicScsiAdminVcon,'cfprVnicScsiAppRole':cfprVnicScsiAppRole,'cfprVnicScsiBootDev':cfprVnicScsiBootDev,'cfprVnicScsiConfigQualifier':cfprVnicScsiConfigQualifier,'cfprVnicScsiConfigState':cfprVnicScsiConfigState,'cfprVnicScsiEquipmentDn':cfprVnicScsiEquipmentDn,'cfprVnicScsiIdentPoolName':cfprVnicScsiIdentPoolName,'cfprVnicScsiInstType':cfprVnicScsiInstType,'cfprVnicScsiName':cfprVnicScsiName,'cfprVnicScsiNwTemplName':cfprVnicScsiNwTemplName,'cfprVnicScsiOperHostPort':cfprVnicScsiOperHostPort,'cfprVnicScsiOperOrder':cfprVnicScsiOperOrder,'cfprVnicScsiOperSpeed':cfprVnicScsiOperSpeed,'cfprVnicScsiOperStatsPolicyName':cfprVnicScsiOperStatsPolicyName,'cfprVnicScsiOperVcon':cfprVnicScsiOperVcon,'cfprVnicScsiOrder':cfprVnicScsiOrder,'cfprVnicScsiOwner':cfprVnicScsiOwner,'cfprVnicScsiPinToGroupName':cfprVnicScsiPinToGroupName,'cfprVnicScsiQosPolicyName':cfprVnicScsiQosPolicyName,'cfprVnicScsiStatsPolicyName':cfprVnicScsiStatsPolicyName,'cfprVnicScsiSwitchId':cfprVnicScsiSwitchId,'cfprVnicScsiType':cfprVnicScsiType,'cfprVnicScsiIfTable':cfprVnicScsiIfTable,'cfprVnicScsiIfEntry':cfprVnicScsiIfEntry,_AF:cfprVnicScsiIfInstanceId,'cfprVnicScsiIfDn':cfprVnicScsiIfDn,'cfprVnicScsiIfRn':cfprVnicScsiIfRn,'cfprVnicScsiIfAddr':cfprVnicScsiIfAddr,'cfprVnicScsiIfConfigQualifier':cfprVnicScsiIfConfigQualifier,'cfprVnicScsiIfName':cfprVnicScsiIfName,'cfprVnicScsiIfOperState':cfprVnicScsiIfOperState,'cfprVnicScsiIfOperVnetDn':cfprVnicScsiIfOperVnetDn,'cfprVnicScsiIfOperVnetName':cfprVnicScsiIfOperVnetName,'cfprVnicScsiIfOwner':cfprVnicScsiIfOwner,'cfprVnicScsiIfPubNwId':cfprVnicScsiIfPubNwId,'cfprVnicScsiIfSharing':cfprVnicScsiIfSharing,'cfprVnicScsiIfSwitchId':cfprVnicScsiIfSwitchId,'cfprVnicScsiIfType':cfprVnicScsiIfType,'cfprVnicScsiIfVnet':cfprVnicScsiIfVnet,'cfprVnicUsnicConPolicyTable':cfprVnicUsnicConPolicyTable,'cfprVnicUsnicConPolicyEntry':cfprVnicUsnicConPolicyEntry,_AG:cfprVnicUsnicConPolicyInstanceId,'cfprVnicUsnicConPolicyDn':cfprVnicUsnicConPolicyDn,'cfprVnicUsnicConPolicyRn':cfprVnicUsnicConPolicyRn,'cfprVnicUsnicConPolicyAdaptorProfileName':cfprVnicUsnicConPolicyAdaptorProfileName,'cfprVnicUsnicConPolicyDescr':cfprVnicUsnicConPolicyDescr,'cfprVnicUsnicConPolicyIntId':cfprVnicUsnicConPolicyIntId,'cfprVnicUsnicConPolicyName':cfprVnicUsnicConPolicyName,'cfprVnicUsnicConPolicyPolicyLevel':cfprVnicUsnicConPolicyPolicyLevel,'cfprVnicUsnicConPolicyPolicyOwner':cfprVnicUsnicConPolicyPolicyOwner,'cfprVnicUsnicConPolicyUsnicCount':cfprVnicUsnicConPolicyUsnicCount,'cfprVnicUsnicConPolicyRefTable':cfprVnicUsnicConPolicyRefTable,'cfprVnicUsnicConPolicyRefEntry':cfprVnicUsnicConPolicyRefEntry,_AH:cfprVnicUsnicConPolicyRefInstanceId,'cfprVnicUsnicConPolicyRefDn':cfprVnicUsnicConPolicyRefDn,'cfprVnicUsnicConPolicyRefRn':cfprVnicUsnicConPolicyRefRn,'cfprVnicUsnicConPolicyRefConPolicyName':cfprVnicUsnicConPolicyRefConPolicyName,'cfprVnicUsnicConPolicyRefOperConPolicyName':cfprVnicUsnicConPolicyRefOperConPolicyName,'cfprVnicVhbaBehPolicyTable':cfprVnicVhbaBehPolicyTable,'cfprVnicVhbaBehPolicyEntry':cfprVnicVhbaBehPolicyEntry,_AI:cfprVnicVhbaBehPolicyInstanceId,'cfprVnicVhbaBehPolicyDn':cfprVnicVhbaBehPolicyDn,'cfprVnicVhbaBehPolicyRn':cfprVnicVhbaBehPolicyRn,'cfprVnicVhbaBehPolicyAction':cfprVnicVhbaBehPolicyAction,'cfprVnicVhbaBehPolicyDescr':cfprVnicVhbaBehPolicyDescr,'cfprVnicVhbaBehPolicyIntId':cfprVnicVhbaBehPolicyIntId,'cfprVnicVhbaBehPolicyName':cfprVnicVhbaBehPolicyName,'cfprVnicVhbaBehPolicyNwTemplName':cfprVnicVhbaBehPolicyNwTemplName,'cfprVnicVhbaBehPolicyPolicyLevel':cfprVnicVhbaBehPolicyPolicyLevel,'cfprVnicVhbaBehPolicyPolicyOwner':cfprVnicVhbaBehPolicyPolicyOwner,'cfprVnicVhbaBehPolicyType':cfprVnicVhbaBehPolicyType,'cfprVnicVlanTable':cfprVnicVlanTable,'cfprVnicVlanEntry':cfprVnicVlanEntry,_AJ:cfprVnicVlanInstanceId,'cfprVnicVlanDn':cfprVnicVlanDn,'cfprVnicVlanRn':cfprVnicVlanRn,'cfprVnicVlanConfigQualifier':cfprVnicVlanConfigQualifier,'cfprVnicVlanFltAggr':cfprVnicVlanFltAggr,'cfprVnicVlanName':cfprVnicVlanName,'cfprVnicVlanOperState':cfprVnicVlanOperState,'cfprVnicVlanOperVnetDn':cfprVnicVlanOperVnetDn,'cfprVnicVlanOperVnetName':cfprVnicVlanOperVnetName,'cfprVnicVlanOwner':cfprVnicVlanOwner,'cfprVnicVlanPubNwId':cfprVnicVlanPubNwId,'cfprVnicVlanSharing':cfprVnicVlanSharing,'cfprVnicVlanSwitchId':cfprVnicVlanSwitchId,'cfprVnicVlanType':cfprVnicVlanType,'cfprVnicVlanVlanName':cfprVnicVlanVlanName,'cfprVnicVlanVnet':cfprVnicVlanVnet,'cfprVnicVmqConPolicyTable':cfprVnicVmqConPolicyTable,'cfprVnicVmqConPolicyEntry':cfprVnicVmqConPolicyEntry,_AK:cfprVnicVmqConPolicyInstanceId,'cfprVnicVmqConPolicyDn':cfprVnicVmqConPolicyDn,'cfprVnicVmqConPolicyRn':cfprVnicVmqConPolicyRn,'cfprVnicVmqConPolicyDescr':cfprVnicVmqConPolicyDescr,'cfprVnicVmqConPolicyIntId':cfprVnicVmqConPolicyIntId,'cfprVnicVmqConPolicyIntrCount':cfprVnicVmqConPolicyIntrCount,'cfprVnicVmqConPolicyName':cfprVnicVmqConPolicyName,'cfprVnicVmqConPolicyPolicyLevel':cfprVnicVmqConPolicyPolicyLevel,'cfprVnicVmqConPolicyPolicyOwner':cfprVnicVmqConPolicyPolicyOwner,'cfprVnicVmqConPolicyVmqCount':cfprVnicVmqConPolicyVmqCount,'cfprVnicVmqConPolicyRefTable':cfprVnicVmqConPolicyRefTable,'cfprVnicVmqConPolicyRefEntry':cfprVnicVmqConPolicyRefEntry,_AL:cfprVnicVmqConPolicyRefInstanceId,'cfprVnicVmqConPolicyRefDn':cfprVnicVmqConPolicyRefDn,'cfprVnicVmqConPolicyRefRn':cfprVnicVmqConPolicyRefRn,'cfprVnicVmqConPolicyRefConPolicyName':cfprVnicVmqConPolicyRefConPolicyName,'cfprVnicVmqConPolicyRefOperConPolicyName':cfprVnicVmqConPolicyRefOperConPolicyName,'cfprVnicVnicBehPolicyTable':cfprVnicVnicBehPolicyTable,'cfprVnicVnicBehPolicyEntry':cfprVnicVnicBehPolicyEntry,_AM:cfprVnicVnicBehPolicyInstanceId,'cfprVnicVnicBehPolicyDn':cfprVnicVnicBehPolicyDn,'cfprVnicVnicBehPolicyRn':cfprVnicVnicBehPolicyRn,'cfprVnicVnicBehPolicyAction':cfprVnicVnicBehPolicyAction,'cfprVnicVnicBehPolicyDescr':cfprVnicVnicBehPolicyDescr,'cfprVnicVnicBehPolicyIntId':cfprVnicVnicBehPolicyIntId,'cfprVnicVnicBehPolicyName':cfprVnicVnicBehPolicyName,'cfprVnicVnicBehPolicyNwTemplName':cfprVnicVnicBehPolicyNwTemplName,'cfprVnicVnicBehPolicyPolicyLevel':cfprVnicVnicBehPolicyPolicyLevel,'cfprVnicVnicBehPolicyPolicyOwner':cfprVnicVnicBehPolicyPolicyOwner,'cfprVnicVnicBehPolicyType':cfprVnicVnicBehPolicyType,'cfprVnicWwnnHistoryTable':cfprVnicWwnnHistoryTable,'cfprVnicWwnnHistoryEntry':cfprVnicWwnnHistoryEntry,_AN:cfprVnicWwnnHistoryInstanceId,'cfprVnicWwnnHistoryDn':cfprVnicWwnnHistoryDn,'cfprVnicWwnnHistoryRn':cfprVnicWwnnHistoryRn,'cfprVnicWwnnHistoryOldwwnn':cfprVnicWwnnHistoryOldwwnn,'cfprVnicWwpnHistoryTable':cfprVnicWwpnHistoryTable,'cfprVnicWwpnHistoryEntry':cfprVnicWwpnHistoryEntry,_AO:cfprVnicWwpnHistoryInstanceId,'cfprVnicWwpnHistoryDn':cfprVnicWwpnHistoryDn,'cfprVnicWwpnHistoryRn':cfprVnicWwpnHistoryRn,'cfprVnicWwpnHistoryOldaddr':cfprVnicWwpnHistoryOldaddr})