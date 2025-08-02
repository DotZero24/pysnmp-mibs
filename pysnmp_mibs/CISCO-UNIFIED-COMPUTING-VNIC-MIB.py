_AS='cucsVnicIScsiInitAutoConfigPolicyInstanceId'
_AR='cucsVnicIScsiConfigInstanceId'
_AQ='cucsVnicIPv6IfInstanceId'
_AP='cucsVnicEthConfigInstanceId'
_AO='cucsVnicIpV6HistoryInstanceId'
_AN='cucsVnicVmqConPolicyRefInstanceId'
_AM='cucsVnicVmqConPolicyInstanceId'
_AL='cucsVnicUsnicConPolicyRefInstanceId'
_AK='cucsVnicUsnicConPolicyInstanceId'
_AJ='cucsVnicProfileRefInstanceId'
_AI='cucsVnicIpV6StaticAddrInstanceId'
_AH='cucsVnicIpV6MgmtPooledAddrInstanceId'
_AG='cucsVnicIpV4MgmtPooledAddrInstanceId'
_AF='cucsVnicWwpnHistoryInstanceId'
_AE='cucsVnicWwnnHistoryInstanceId'
_AD='cucsVnicMacHistoryInstanceId'
_AC='cucsVnicIqnHistoryInstanceId'
_AB='cucsVnicIpV4HistoryInstanceId'
_AA='cucsVnicVnicBehPolicyInstanceId'
_A9='cucsVnicVhbaBehPolicyInstanceId'
_A8='cucsVnicSanConnPolicyInstanceId'
_A7='cucsVnicRackServerDiscoveryProfileInstanceId'
_A6='cucsVnicProfileSetFsmStageInstanceId'
_A5='cucsVnicProfileSetFsmInstanceId'
_A4='cucsVnicLanConnPolicyInstanceId'
_A3='cucsVnicIScsiLCPInstanceId'
_A2='cucsVnicIScsiBootVnicInstanceId'
_A1='cucsVnicIScsiBootParamsInstanceId'
_A0='cucsVnicFcGroupTemplInstanceId'
_z='cucsVnicFcGroupDefInstanceId'
_y='cucsVnicDynamicConPolicyRefInstanceId'
_x='cucsVnicConnDefInstanceId'
_w='cucsVnicVlanInstanceId'
_v='cucsVnicOProfileAliasInstanceId'
_u='cucsVnicLunInstanceId'
_t='cucsVnicInternalProfileInstanceId'
_s='cucsVnicIScsiStaticTargetIfInstanceId'
_r='cucsVnicIScsiNodeInstanceId'
_q='cucsVnicIScsiAutoTargetIfInstanceId'
_p='cucsVnicIScsiInstanceId'
_o='cucsVnicIPv4PooledIscsiAddrInstanceId'
_n='cucsVnicIPv4IscsiAddrInstanceId'
_m='cucsVnicBootIpPolicyInstanceId'
_l='cucsVnicScsiIfInstanceId'
_k='cucsVnicScsiInstanceId'
_j='cucsVnicSanConnTemplInstanceId'
_i='cucsVnicProfileSetFsmTaskInstanceId'
_h='cucsVnicProfileSetInstanceId'
_g='cucsVnicProfileAliasInstanceId'
_f='cucsVnicProfileInstanceId'
_e='cucsVnicLifVsanInstanceId'
_d='cucsVnicLifVlanInstanceId'
_c='cucsVnicLanConnTemplInstanceId'
_b='cucsVnicIpcIfInstanceId'
_a='cucsVnicIpcInstanceId'
_Z='cucsVnicIpV4StaticAddrInstanceId'
_Y='cucsVnicIpV4ProfDerivedAddrInstanceId'
_X='cucsVnicIpV4PooledAddrInstanceId'
_W='cucsVnicIPv4StaticRouteInstanceId'
_V='cucsVnicIPv4IfInstanceId'
_U='cucsVnicIPv4DnsInstanceId'
_T='cucsVnicIPv4DhcpInstanceId'
_S='cucsVnicFcOEIfInstanceId'
_R='cucsVnicFcNodeInstanceId'
_Q='cucsVnicFcLifInstanceId'
_P='cucsVnicFcIfInstanceId'
_O='cucsVnicFcInstanceId'
_N='cucsVnicEtherIfInstanceId'
_M='cucsVnicEtherInstanceId'
_L='cucsVnicEthLifInstanceId'
_K='cucsVnicDynamicProviderEpInstanceId'
_J='cucsVnicDynamicProviderInstanceId'
_I='cucsVnicDynamicIdUniverseInstanceId'
_H='cucsVnicDynamicConPolicyInstanceId'
_G='cucsVnicDynamicConInstanceId'
_F='cucsVnicDefBehInstanceId'
_E='cucsVnicBootTargetInstanceId'
_D='not-accessible'
_C='CISCO-UNIFIED-COMPUTING-VNIC-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CiscoAlarmSeverity,CiscoInetAddressMask,CiscoNetworkAddress,TimeIntervalSec,Unsigned64=mibBuilder.importSymbols('CISCO-TC','CiscoAlarmSeverity','CiscoInetAddressMask','CiscoNetworkAddress','TimeIntervalSec','Unsigned64')
CucsManagedObjectDn,CucsManagedObjectId,ciscoUnifiedComputingMIBObjects=mibBuilder.importSymbols('CISCO-UNIFIED-COMPUTING-MIB','CucsManagedObjectDn','CucsManagedObjectId','ciscoUnifiedComputingMIBObjects')
CucsAdaptorPurpose,CucsConditionRemoteInvRslt,CucsDpsecForgedTransmit,CucsFabricHostPortId,CucsFabricVlanSharingType,CucsFsmCompletion,CucsFsmFlags,CucsFsmFsmStageStatus,CucsLsConfigState,CucsLsOwner,CucsNetworkSwitchId,CucsNwctrlAdminState,CucsNwctrlLinkFailAction,CucsNwctrlLldpAdminStateBitmask,CucsNwctrlRegistrationMode,CucsPolicyPolicyOwner,CucsVmMgmtPlane,CucsVnicAEtherIfType,CucsVnicAFcIfSwitchId,CucsVnicAFcIfType,CucsVnicAIpcIfType,CucsVnicAScsiIfType,CucsVnicCdnSource,CucsVnicConfigIssues,CucsVnicConnectionOwner,CucsVnicConnectionType,CucsVnicDefBehType,CucsVnicDefaultAction,CucsVnicDynamicConReqProtection,CucsVnicEtherBaseIfSwitchId,CucsVnicEtherBaseSwitchId,CucsVnicEtherType,CucsVnicExternalMgmtIPMode,CucsVnicFcBasePersBind,CucsVnicFcBaseType,CucsVnicFcNodeOwner,CucsVnicHostNwIOPerfPref,CucsVnicIPv4DnsPref,CucsVnicIScsiIfDefType,CucsVnicIScsiNodeOwner,CucsVnicIfOperState,CucsVnicInstantiation,CucsVnicIpPoolType,CucsVnicIpcType,CucsVnicLanConnTemplSwitchId,CucsVnicLunId,CucsVnicPortProfileType,CucsVnicProfileConfigQualifier,CucsVnicProfileSetFsmCurrentFsm,CucsVnicProfileSetFsmStageName,CucsVnicProfileSetFsmTaskItem,CucsVnicRedundancyPairType,CucsVnicSanConnTemplTarget,CucsVnicScsiType,CucsVnicTemplateTarget,CucsVnicTemplateType,CucsVnicVhbaBehPolicyType,CucsVnicVirtualizationPreferenceType,CucsVnicVlanGroupUpdate,CucsVnicVnicBehPolicyType,CucsVnicVnicBootDev,CucsVnicVnicOperHostPort=mibBuilder.importSymbols('CISCO-UNIFIED-COMPUTING-TC-MIB','CucsAdaptorPurpose','CucsConditionRemoteInvRslt','CucsDpsecForgedTransmit','CucsFabricHostPortId','CucsFabricVlanSharingType','CucsFsmCompletion','CucsFsmFlags','CucsFsmFsmStageStatus','CucsLsConfigState','CucsLsOwner','CucsNetworkSwitchId','CucsNwctrlAdminState','CucsNwctrlLinkFailAction','CucsNwctrlLldpAdminStateBitmask','CucsNwctrlRegistrationMode','CucsPolicyPolicyOwner','CucsVmMgmtPlane','CucsVnicAEtherIfType','CucsVnicAFcIfSwitchId','CucsVnicAFcIfType','CucsVnicAIpcIfType','CucsVnicAScsiIfType','CucsVnicCdnSource','CucsVnicConfigIssues','CucsVnicConnectionOwner','CucsVnicConnectionType','CucsVnicDefBehType','CucsVnicDefaultAction','CucsVnicDynamicConReqProtection','CucsVnicEtherBaseIfSwitchId','CucsVnicEtherBaseSwitchId','CucsVnicEtherType','CucsVnicExternalMgmtIPMode','CucsVnicFcBasePersBind','CucsVnicFcBaseType','CucsVnicFcNodeOwner','CucsVnicHostNwIOPerfPref','CucsVnicIPv4DnsPref','CucsVnicIScsiIfDefType','CucsVnicIScsiNodeOwner','CucsVnicIfOperState','CucsVnicInstantiation','CucsVnicIpPoolType','CucsVnicIpcType','CucsVnicLanConnTemplSwitchId','CucsVnicLunId','CucsVnicPortProfileType','CucsVnicProfileConfigQualifier','CucsVnicProfileSetFsmCurrentFsm','CucsVnicProfileSetFsmStageName','CucsVnicProfileSetFsmTaskItem','CucsVnicRedundancyPairType','CucsVnicSanConnTemplTarget','CucsVnicScsiType','CucsVnicTemplateTarget','CucsVnicTemplateType','CucsVnicVhbaBehPolicyType','CucsVnicVirtualizationPreferenceType','CucsVnicVlanGroupUpdate','CucsVnicVnicBehPolicyType','CucsVnicVnicBootDev','CucsVnicVnicOperHostPort')
InetAddressIPv4,InetAddressIPv6=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressIPv4','InetAddressIPv6')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowPointer,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowPointer','TextualConvention','TimeInterval','TimeStamp','TruthValue')
cucsVnicObjects=ModuleIdentity((1,3,6,1,4,1,9,9,719,1,53))
_CucsVnicBootTargetTable_Object=MibTable
cucsVnicBootTargetTable=_CucsVnicBootTargetTable_Object((1,3,6,1,4,1,9,9,719,1,53,1))
if mibBuilder.loadTexts:cucsVnicBootTargetTable.setStatus(_A)
_CucsVnicBootTargetEntry_Object=MibTableRow
cucsVnicBootTargetEntry=_CucsVnicBootTargetEntry_Object((1,3,6,1,4,1,9,9,719,1,53,1,1))
cucsVnicBootTargetEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:cucsVnicBootTargetEntry.setStatus(_A)
_CucsVnicBootTargetInstanceId_Type=CucsManagedObjectId
_CucsVnicBootTargetInstanceId_Object=MibTableColumn
cucsVnicBootTargetInstanceId=_CucsVnicBootTargetInstanceId_Object((1,3,6,1,4,1,9,9,719,1,53,1,1,1),_CucsVnicBootTargetInstanceId_Type())
cucsVnicBootTargetInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsVnicBootTargetInstanceId.setStatus(_A)
_CucsVnicBootTargetDn_Type=CucsManagedObjectDn
_CucsVnicBootTargetDn_Object=MibTableColumn
cucsVnicBootTargetDn=_CucsVnicBootTargetDn_Object((1,3,6,1,4,1,9,9,719,1,53,1,1,2),_CucsVnicBootTargetDn_Type())
cucsVnicBootTargetDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicBootTargetDn.setStatus(_A)
_CucsVnicBootTargetRn_Type=SnmpAdminString
_CucsVnicBootTargetRn_Object=MibTableColumn
cucsVnicBootTargetRn=_CucsVnicBootTargetRn_Object((1,3,6,1,4,1,9,9,719,1,53,1,1,3),_CucsVnicBootTargetRn_Type())
cucsVnicBootTargetRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicBootTargetRn.setStatus(_A)
_CucsVnicBootTargetLun_Type=SnmpAdminString
_CucsVnicBootTargetLun_Object=MibTableColumn
cucsVnicBootTargetLun=_CucsVnicBootTargetLun_Object((1,3,6,1,4,1,9,9,719,1,53,1,1,4),_CucsVnicBootTargetLun_Type())
cucsVnicBootTargetLun.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicBootTargetLun.setStatus(_A)
_CucsVnicBootTargetWwn_Type=Unsigned64
_CucsVnicBootTargetWwn_Object=MibTableColumn
cucsVnicBootTargetWwn=_CucsVnicBootTargetWwn_Object((1,3,6,1,4,1,9,9,719,1,53,1,1,5),_CucsVnicBootTargetWwn_Type())
cucsVnicBootTargetWwn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicBootTargetWwn.setStatus(_A)
_CucsVnicDefBehTable_Object=MibTable
cucsVnicDefBehTable=_CucsVnicDefBehTable_Object((1,3,6,1,4,1,9,9,719,1,53,2))
if mibBuilder.loadTexts:cucsVnicDefBehTable.setStatus(_A)
_CucsVnicDefBehEntry_Object=MibTableRow
cucsVnicDefBehEntry=_CucsVnicDefBehEntry_Object((1,3,6,1,4,1,9,9,719,1,53,2,1))
cucsVnicDefBehEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:cucsVnicDefBehEntry.setStatus(_A)
_CucsVnicDefBehInstanceId_Type=CucsManagedObjectId
_CucsVnicDefBehInstanceId_Object=MibTableColumn
cucsVnicDefBehInstanceId=_CucsVnicDefBehInstanceId_Object((1,3,6,1,4,1,9,9,719,1,53,2,1,1),_CucsVnicDefBehInstanceId_Type())
cucsVnicDefBehInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsVnicDefBehInstanceId.setStatus(_A)
_CucsVnicDefBehDn_Type=CucsManagedObjectDn
_CucsVnicDefBehDn_Object=MibTableColumn
cucsVnicDefBehDn=_CucsVnicDefBehDn_Object((1,3,6,1,4,1,9,9,719,1,53,2,1,2),_CucsVnicDefBehDn_Type())
cucsVnicDefBehDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicDefBehDn.setStatus(_A)
_CucsVnicDefBehRn_Type=SnmpAdminString
_CucsVnicDefBehRn_Object=MibTableColumn
cucsVnicDefBehRn=_CucsVnicDefBehRn_Object((1,3,6,1,4,1,9,9,719,1,53,2,1,3),_CucsVnicDefBehRn_Type())
cucsVnicDefBehRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicDefBehRn.setStatus(_A)
_CucsVnicDefBehAction_Type=CucsVnicDefaultAction
_CucsVnicDefBehAction_Object=MibTableColumn
cucsVnicDefBehAction=_CucsVnicDefBehAction_Object((1,3,6,1,4,1,9,9,719,1,53,2,1,4),_CucsVnicDefBehAction_Type())
cucsVnicDefBehAction.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicDefBehAction.setStatus(_A)
_CucsVnicDefBehNwTemplName_Type=SnmpAdminString
_CucsVnicDefBehNwTemplName_Object=MibTableColumn
cucsVnicDefBehNwTemplName=_CucsVnicDefBehNwTemplName_Object((1,3,6,1,4,1,9,9,719,1,53,2,1,5),_CucsVnicDefBehNwTemplName_Type())
cucsVnicDefBehNwTemplName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicDefBehNwTemplName.setStatus(_A)
_CucsVnicDefBehType_Type=CucsVnicDefBehType
_CucsVnicDefBehType_Object=MibTableColumn
cucsVnicDefBehType=_CucsVnicDefBehType_Object((1,3,6,1,4,1,9,9,719,1,53,2,1,6),_CucsVnicDefBehType_Type())
cucsVnicDefBehType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicDefBehType.setStatus(_A)
_CucsVnicDefBehDescr_Type=SnmpAdminString
_CucsVnicDefBehDescr_Object=MibTableColumn
cucsVnicDefBehDescr=_CucsVnicDefBehDescr_Object((1,3,6,1,4,1,9,9,719,1,53,2,1,7),_CucsVnicDefBehDescr_Type())
cucsVnicDefBehDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicDefBehDescr.setStatus(_A)
_CucsVnicDefBehIntId_Type=SnmpAdminString
_CucsVnicDefBehIntId_Object=MibTableColumn
cucsVnicDefBehIntId=_CucsVnicDefBehIntId_Object((1,3,6,1,4,1,9,9,719,1,53,2,1,8),_CucsVnicDefBehIntId_Type())
cucsVnicDefBehIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicDefBehIntId.setStatus(_A)
_CucsVnicDefBehName_Type=SnmpAdminString
_CucsVnicDefBehName_Object=MibTableColumn
cucsVnicDefBehName=_CucsVnicDefBehName_Object((1,3,6,1,4,1,9,9,719,1,53,2,1,9),_CucsVnicDefBehName_Type())
cucsVnicDefBehName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicDefBehName.setStatus(_A)
_CucsVnicDefBehPolicyLevel_Type=Gauge32
_CucsVnicDefBehPolicyLevel_Object=MibTableColumn
cucsVnicDefBehPolicyLevel=_CucsVnicDefBehPolicyLevel_Object((1,3,6,1,4,1,9,9,719,1,53,2,1,10),_CucsVnicDefBehPolicyLevel_Type())
cucsVnicDefBehPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicDefBehPolicyLevel.setStatus(_A)
_CucsVnicDefBehPolicyOwner_Type=CucsPolicyPolicyOwner
_CucsVnicDefBehPolicyOwner_Object=MibTableColumn
cucsVnicDefBehPolicyOwner=_CucsVnicDefBehPolicyOwner_Object((1,3,6,1,4,1,9,9,719,1,53,2,1,11),_CucsVnicDefBehPolicyOwner_Type())
cucsVnicDefBehPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicDefBehPolicyOwner.setStatus(_A)
_CucsVnicDynamicConTable_Object=MibTable
cucsVnicDynamicConTable=_CucsVnicDynamicConTable_Object((1,3,6,1,4,1,9,9,719,1,53,3))
if mibBuilder.loadTexts:cucsVnicDynamicConTable.setStatus(_A)
_CucsVnicDynamicConEntry_Object=MibTableRow
cucsVnicDynamicConEntry=_CucsVnicDynamicConEntry_Object((1,3,6,1,4,1,9,9,719,1,53,3,1))
cucsVnicDynamicConEntry.setIndexNames((0,_C,_G))
if mibBuilder.loadTexts:cucsVnicDynamicConEntry.setStatus(_A)
_CucsVnicDynamicConInstanceId_Type=CucsManagedObjectId
_CucsVnicDynamicConInstanceId_Object=MibTableColumn
cucsVnicDynamicConInstanceId=_CucsVnicDynamicConInstanceId_Object((1,3,6,1,4,1,9,9,719,1,53,3,1,1),_CucsVnicDynamicConInstanceId_Type())
cucsVnicDynamicConInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsVnicDynamicConInstanceId.setStatus(_A)
_CucsVnicDynamicConDn_Type=CucsManagedObjectDn
_CucsVnicDynamicConDn_Object=MibTableColumn
cucsVnicDynamicConDn=_CucsVnicDynamicConDn_Object((1,3,6,1,4,1,9,9,719,1,53,3,1,2),_CucsVnicDynamicConDn_Type())
cucsVnicDynamicConDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicDynamicConDn.setStatus(_A)
_CucsVnicDynamicConRn_Type=SnmpAdminString
_CucsVnicDynamicConRn_Object=MibTableColumn
cucsVnicDynamicConRn=_CucsVnicDynamicConRn_Object((1,3,6,1,4,1,9,9,719,1,53,3,1,3),_CucsVnicDynamicConRn_Type())
cucsVnicDynamicConRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicDynamicConRn.setStatus(_A)
_CucsVnicDynamicConAdaptorProfileName_Type=SnmpAdminString
_CucsVnicDynamicConAdaptorProfileName_Object=MibTableColumn
cucsVnicDynamicConAdaptorProfileName=_CucsVnicDynamicConAdaptorProfileName_Object((1,3,6,1,4,1,9,9,719,1,53,3,1,4),_CucsVnicDynamicConAdaptorProfileName_Type())
cucsVnicDynamicConAdaptorProfileName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicDynamicConAdaptorProfileName.setStatus(_A)
_CucsVnicDynamicConDescr_Type=SnmpAdminString
_CucsVnicDynamicConDescr_Object=MibTableColumn
cucsVnicDynamicConDescr=_CucsVnicDynamicConDescr_Object((1,3,6,1,4,1,9,9,719,1,53,3,1,5),_CucsVnicDynamicConDescr_Type())
cucsVnicDynamicConDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicDynamicConDescr.setStatus(_A)
_CucsVnicDynamicConDynamicEth_Type=Gauge32
_CucsVnicDynamicConDynamicEth_Object=MibTableColumn
cucsVnicDynamicConDynamicEth=_CucsVnicDynamicConDynamicEth_Object((1,3,6,1,4,1,9,9,719,1,53,3,1,6),_CucsVnicDynamicConDynamicEth_Type())
cucsVnicDynamicConDynamicEth.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicDynamicConDynamicEth.setStatus(_A)
_CucsVnicDynamicConIntId_Type=SnmpAdminString
_CucsVnicDynamicConIntId_Object=MibTableColumn
cucsVnicDynamicConIntId=_CucsVnicDynamicConIntId_Object((1,3,6,1,4,1,9,9,719,1,53,3,1,7),_CucsVnicDynamicConIntId_Type())
cucsVnicDynamicConIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicDynamicConIntId.setStatus(_A)
_CucsVnicDynamicConMtu_Type=Gauge32
_CucsVnicDynamicConMtu_Object=MibTableColumn
cucsVnicDynamicConMtu=_CucsVnicDynamicConMtu_Object((1,3,6,1,4,1,9,9,719,1,53,3,1,8),_CucsVnicDynamicConMtu_Type())
cucsVnicDynamicConMtu.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicDynamicConMtu.setStatus(_A)
_CucsVnicDynamicConName_Type=SnmpAdminString
_CucsVnicDynamicConName_Object=MibTableColumn
cucsVnicDynamicConName=_CucsVnicDynamicConName_Object((1,3,6,1,4,1,9,9,719,1,53,3,1,9),_CucsVnicDynamicConName_Type())
cucsVnicDynamicConName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicDynamicConName.setStatus(_A)
_CucsVnicDynamicConNamingPrefix_Type=SnmpAdminString
_CucsVnicDynamicConNamingPrefix_Object=MibTableColumn
cucsVnicDynamicConNamingPrefix=_CucsVnicDynamicConNamingPrefix_Object((1,3,6,1,4,1,9,9,719,1,53,3,1,10),_CucsVnicDynamicConNamingPrefix_Type())
cucsVnicDynamicConNamingPrefix.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicDynamicConNamingPrefix.setStatus(_A)
_CucsVnicDynamicConProtection_Type=CucsVnicDynamicConReqProtection
_CucsVnicDynamicConProtection_Object=MibTableColumn
cucsVnicDynamicConProtection=_CucsVnicDynamicConProtection_Object((1,3,6,1,4,1,9,9,719,1,53,3,1,11),_CucsVnicDynamicConProtection_Type())
cucsVnicDynamicConProtection.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicDynamicConProtection.setStatus(_A)
_CucsVnicDynamicConPolicyLevel_Type=Gauge32
_CucsVnicDynamicConPolicyLevel_Object=MibTableColumn
cucsVnicDynamicConPolicyLevel=_CucsVnicDynamicConPolicyLevel_Object((1,3,6,1,4,1,9,9,719,1,53,3,1,12),_CucsVnicDynamicConPolicyLevel_Type())
cucsVnicDynamicConPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicDynamicConPolicyLevel.setStatus(_A)
_CucsVnicDynamicConPolicyOwner_Type=CucsPolicyPolicyOwner
_CucsVnicDynamicConPolicyOwner_Object=MibTableColumn
cucsVnicDynamicConPolicyOwner=_CucsVnicDynamicConPolicyOwner_Object((1,3,6,1,4,1,9,9,719,1,53,3,1,13),_CucsVnicDynamicConPolicyOwner_Type())
cucsVnicDynamicConPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicDynamicConPolicyOwner.setStatus(_A)
_CucsVnicDynamicConPolicyTable_Object=MibTable
cucsVnicDynamicConPolicyTable=_CucsVnicDynamicConPolicyTable_Object((1,3,6,1,4,1,9,9,719,1,53,4))
if mibBuilder.loadTexts:cucsVnicDynamicConPolicyTable.setStatus(_A)
_CucsVnicDynamicConPolicyEntry_Object=MibTableRow
cucsVnicDynamicConPolicyEntry=_CucsVnicDynamicConPolicyEntry_Object((1,3,6,1,4,1,9,9,719,1,53,4,1))
cucsVnicDynamicConPolicyEntry.setIndexNames((0,_C,_H))
if mibBuilder.loadTexts:cucsVnicDynamicConPolicyEntry.setStatus(_A)
_CucsVnicDynamicConPolicyInstanceId_Type=CucsManagedObjectId
_CucsVnicDynamicConPolicyInstanceId_Object=MibTableColumn
cucsVnicDynamicConPolicyInstanceId=_CucsVnicDynamicConPolicyInstanceId_Object((1,3,6,1,4,1,9,9,719,1,53,4,1,1),_CucsVnicDynamicConPolicyInstanceId_Type())
cucsVnicDynamicConPolicyInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsVnicDynamicConPolicyInstanceId.setStatus(_A)
_CucsVnicDynamicConPolicyDn_Type=CucsManagedObjectDn
_CucsVnicDynamicConPolicyDn_Object=MibTableColumn
cucsVnicDynamicConPolicyDn=_CucsVnicDynamicConPolicyDn_Object((1,3,6,1,4,1,9,9,719,1,53,4,1,2),_CucsVnicDynamicConPolicyDn_Type())
cucsVnicDynamicConPolicyDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicDynamicConPolicyDn.setStatus(_A)
_CucsVnicDynamicConPolicyRn_Type=SnmpAdminString
_CucsVnicDynamicConPolicyRn_Object=MibTableColumn
cucsVnicDynamicConPolicyRn=_CucsVnicDynamicConPolicyRn_Object((1,3,6,1,4,1,9,9,719,1,53,4,1,3),_CucsVnicDynamicConPolicyRn_Type())
cucsVnicDynamicConPolicyRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicDynamicConPolicyRn.setStatus(_A)
_CucsVnicDynamicConPolicyAdaptorProfileName_Type=SnmpAdminString
_CucsVnicDynamicConPolicyAdaptorProfileName_Object=MibTableColumn
cucsVnicDynamicConPolicyAdaptorProfileName=_CucsVnicDynamicConPolicyAdaptorProfileName_Object((1,3,6,1,4,1,9,9,719,1,53,4,1,4),_CucsVnicDynamicConPolicyAdaptorProfileName_Type())
cucsVnicDynamicConPolicyAdaptorProfileName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicDynamicConPolicyAdaptorProfileName.setStatus(_A)
_CucsVnicDynamicConPolicyDescr_Type=SnmpAdminString
_CucsVnicDynamicConPolicyDescr_Object=MibTableColumn
cucsVnicDynamicConPolicyDescr=_CucsVnicDynamicConPolicyDescr_Object((1,3,6,1,4,1,9,9,719,1,53,4,1,5),_CucsVnicDynamicConPolicyDescr_Type())
cucsVnicDynamicConPolicyDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicDynamicConPolicyDescr.setStatus(_A)
_CucsVnicDynamicConPolicyDynamicEth_Type=Gauge32
_CucsVnicDynamicConPolicyDynamicEth_Object=MibTableColumn
cucsVnicDynamicConPolicyDynamicEth=_CucsVnicDynamicConPolicyDynamicEth_Object((1,3,6,1,4,1,9,9,719,1,53,4,1,6),_CucsVnicDynamicConPolicyDynamicEth_Type())
cucsVnicDynamicConPolicyDynamicEth.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicDynamicConPolicyDynamicEth.setStatus(_A)
_CucsVnicDynamicConPolicyIntId_Type=SnmpAdminString
_CucsVnicDynamicConPolicyIntId_Object=MibTableColumn
cucsVnicDynamicConPolicyIntId=_CucsVnicDynamicConPolicyIntId_Object((1,3,6,1,4,1,9,9,719,1,53,4,1,7),_CucsVnicDynamicConPolicyIntId_Type())
cucsVnicDynamicConPolicyIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicDynamicConPolicyIntId.setStatus(_A)
_CucsVnicDynamicConPolicyMtu_Type=Gauge32
_CucsVnicDynamicConPolicyMtu_Object=MibTableColumn
cucsVnicDynamicConPolicyMtu=_CucsVnicDynamicConPolicyMtu_Object((1,3,6,1,4,1,9,9,719,1,53,4,1,8),_CucsVnicDynamicConPolicyMtu_Type())
cucsVnicDynamicConPolicyMtu.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicDynamicConPolicyMtu.setStatus(_A)
_CucsVnicDynamicConPolicyName_Type=SnmpAdminString
_CucsVnicDynamicConPolicyName_Object=MibTableColumn
cucsVnicDynamicConPolicyName=_CucsVnicDynamicConPolicyName_Object((1,3,6,1,4,1,9,9,719,1,53,4,1,9),_CucsVnicDynamicConPolicyName_Type())
cucsVnicDynamicConPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicDynamicConPolicyName.setStatus(_A)
_CucsVnicDynamicConPolicyNamingPrefix_Type=SnmpAdminString
_CucsVnicDynamicConPolicyNamingPrefix_Object=MibTableColumn
cucsVnicDynamicConPolicyNamingPrefix=_CucsVnicDynamicConPolicyNamingPrefix_Object((1,3,6,1,4,1,9,9,719,1,53,4,1,10),_CucsVnicDynamicConPolicyNamingPrefix_Type())
cucsVnicDynamicConPolicyNamingPrefix.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicDynamicConPolicyNamingPrefix.setStatus(_A)
_CucsVnicDynamicConPolicyProtection_Type=CucsVnicDynamicConReqProtection
_CucsVnicDynamicConPolicyProtection_Object=MibTableColumn
cucsVnicDynamicConPolicyProtection=_CucsVnicDynamicConPolicyProtection_Object((1,3,6,1,4,1,9,9,719,1,53,4,1,11),_CucsVnicDynamicConPolicyProtection_Type())
cucsVnicDynamicConPolicyProtection.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicDynamicConPolicyProtection.setStatus(_A)
_CucsVnicDynamicConPolicyPolicyLevel_Type=Gauge32
_CucsVnicDynamicConPolicyPolicyLevel_Object=MibTableColumn
cucsVnicDynamicConPolicyPolicyLevel=_CucsVnicDynamicConPolicyPolicyLevel_Object((1,3,6,1,4,1,9,9,719,1,53,4,1,12),_CucsVnicDynamicConPolicyPolicyLevel_Type())
cucsVnicDynamicConPolicyPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicDynamicConPolicyPolicyLevel.setStatus(_A)
_CucsVnicDynamicConPolicyPolicyOwner_Type=CucsPolicyPolicyOwner
_CucsVnicDynamicConPolicyPolicyOwner_Object=MibTableColumn
cucsVnicDynamicConPolicyPolicyOwner=_CucsVnicDynamicConPolicyPolicyOwner_Object((1,3,6,1,4,1,9,9,719,1,53,4,1,13),_CucsVnicDynamicConPolicyPolicyOwner_Type())
cucsVnicDynamicConPolicyPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicDynamicConPolicyPolicyOwner.setStatus(_A)
_CucsVnicDynamicIdUniverseTable_Object=MibTable
cucsVnicDynamicIdUniverseTable=_CucsVnicDynamicIdUniverseTable_Object((1,3,6,1,4,1,9,9,719,1,53,5))
if mibBuilder.loadTexts:cucsVnicDynamicIdUniverseTable.setStatus(_A)
_CucsVnicDynamicIdUniverseEntry_Object=MibTableRow
cucsVnicDynamicIdUniverseEntry=_CucsVnicDynamicIdUniverseEntry_Object((1,3,6,1,4,1,9,9,719,1,53,5,1))
cucsVnicDynamicIdUniverseEntry.setIndexNames((0,_C,_I))
if mibBuilder.loadTexts:cucsVnicDynamicIdUniverseEntry.setStatus(_A)
_CucsVnicDynamicIdUniverseInstanceId_Type=CucsManagedObjectId
_CucsVnicDynamicIdUniverseInstanceId_Object=MibTableColumn
cucsVnicDynamicIdUniverseInstanceId=_CucsVnicDynamicIdUniverseInstanceId_Object((1,3,6,1,4,1,9,9,719,1,53,5,1,1),_CucsVnicDynamicIdUniverseInstanceId_Type())
cucsVnicDynamicIdUniverseInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsVnicDynamicIdUniverseInstanceId.setStatus(_A)
_CucsVnicDynamicIdUniverseDn_Type=CucsManagedObjectDn
_CucsVnicDynamicIdUniverseDn_Object=MibTableColumn
cucsVnicDynamicIdUniverseDn=_CucsVnicDynamicIdUniverseDn_Object((1,3,6,1,4,1,9,9,719,1,53,5,1,2),_CucsVnicDynamicIdUniverseDn_Type())
cucsVnicDynamicIdUniverseDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicDynamicIdUniverseDn.setStatus(_A)
_CucsVnicDynamicIdUniverseRn_Type=SnmpAdminString
_CucsVnicDynamicIdUniverseRn_Object=MibTableColumn
cucsVnicDynamicIdUniverseRn=_CucsVnicDynamicIdUniverseRn_Object((1,3,6,1,4,1,9,9,719,1,53,5,1,3),_CucsVnicDynamicIdUniverseRn_Type())
cucsVnicDynamicIdUniverseRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicDynamicIdUniverseRn.setStatus(_A)
_CucsVnicDynamicIdUniverseDescr_Type=SnmpAdminString
_CucsVnicDynamicIdUniverseDescr_Object=MibTableColumn
cucsVnicDynamicIdUniverseDescr=_CucsVnicDynamicIdUniverseDescr_Object((1,3,6,1,4,1,9,9,719,1,53,5,1,4),_CucsVnicDynamicIdUniverseDescr_Type())
cucsVnicDynamicIdUniverseDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicDynamicIdUniverseDescr.setStatus(_A)
_CucsVnicDynamicIdUniverseIntId_Type=SnmpAdminString
_CucsVnicDynamicIdUniverseIntId_Object=MibTableColumn
cucsVnicDynamicIdUniverseIntId=_CucsVnicDynamicIdUniverseIntId_Object((1,3,6,1,4,1,9,9,719,1,53,5,1,5),_CucsVnicDynamicIdUniverseIntId_Type())
cucsVnicDynamicIdUniverseIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicDynamicIdUniverseIntId.setStatus(_A)
_CucsVnicDynamicIdUniverseName_Type=SnmpAdminString
_CucsVnicDynamicIdUniverseName_Object=MibTableColumn
cucsVnicDynamicIdUniverseName=_CucsVnicDynamicIdUniverseName_Object((1,3,6,1,4,1,9,9,719,1,53,5,1,6),_CucsVnicDynamicIdUniverseName_Type())
cucsVnicDynamicIdUniverseName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicDynamicIdUniverseName.setStatus(_A)
_CucsVnicDynamicIdUniversePolicyLevel_Type=Gauge32
_CucsVnicDynamicIdUniversePolicyLevel_Object=MibTableColumn
cucsVnicDynamicIdUniversePolicyLevel=_CucsVnicDynamicIdUniversePolicyLevel_Object((1,3,6,1,4,1,9,9,719,1,53,5,1,7),_CucsVnicDynamicIdUniversePolicyLevel_Type())
cucsVnicDynamicIdUniversePolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicDynamicIdUniversePolicyLevel.setStatus(_A)
_CucsVnicDynamicIdUniversePolicyOwner_Type=CucsPolicyPolicyOwner
_CucsVnicDynamicIdUniversePolicyOwner_Object=MibTableColumn
cucsVnicDynamicIdUniversePolicyOwner=_CucsVnicDynamicIdUniversePolicyOwner_Object((1,3,6,1,4,1,9,9,719,1,53,5,1,8),_CucsVnicDynamicIdUniversePolicyOwner_Type())
cucsVnicDynamicIdUniversePolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicDynamicIdUniversePolicyOwner.setStatus(_A)
_CucsVnicDynamicProviderTable_Object=MibTable
cucsVnicDynamicProviderTable=_CucsVnicDynamicProviderTable_Object((1,3,6,1,4,1,9,9,719,1,53,6))
if mibBuilder.loadTexts:cucsVnicDynamicProviderTable.setStatus(_A)
_CucsVnicDynamicProviderEntry_Object=MibTableRow
cucsVnicDynamicProviderEntry=_CucsVnicDynamicProviderEntry_Object((1,3,6,1,4,1,9,9,719,1,53,6,1))
cucsVnicDynamicProviderEntry.setIndexNames((0,_C,_J))
if mibBuilder.loadTexts:cucsVnicDynamicProviderEntry.setStatus(_A)
_CucsVnicDynamicProviderInstanceId_Type=CucsManagedObjectId
_CucsVnicDynamicProviderInstanceId_Object=MibTableColumn
cucsVnicDynamicProviderInstanceId=_CucsVnicDynamicProviderInstanceId_Object((1,3,6,1,4,1,9,9,719,1,53,6,1,1),_CucsVnicDynamicProviderInstanceId_Type())
cucsVnicDynamicProviderInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsVnicDynamicProviderInstanceId.setStatus(_A)
_CucsVnicDynamicProviderDn_Type=CucsManagedObjectDn
_CucsVnicDynamicProviderDn_Object=MibTableColumn
cucsVnicDynamicProviderDn=_CucsVnicDynamicProviderDn_Object((1,3,6,1,4,1,9,9,719,1,53,6,1,2),_CucsVnicDynamicProviderDn_Type())
cucsVnicDynamicProviderDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicDynamicProviderDn.setStatus(_A)
_CucsVnicDynamicProviderRn_Type=SnmpAdminString
_CucsVnicDynamicProviderRn_Object=MibTableColumn
cucsVnicDynamicProviderRn=_CucsVnicDynamicProviderRn_Object((1,3,6,1,4,1,9,9,719,1,53,6,1,3),_CucsVnicDynamicProviderRn_Type())
cucsVnicDynamicProviderRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicDynamicProviderRn.setStatus(_A)
_CucsVnicDynamicProviderName_Type=SnmpAdminString
_CucsVnicDynamicProviderName_Object=MibTableColumn
cucsVnicDynamicProviderName=_CucsVnicDynamicProviderName_Object((1,3,6,1,4,1,9,9,719,1,53,6,1,4),_CucsVnicDynamicProviderName_Type())
cucsVnicDynamicProviderName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicDynamicProviderName.setStatus(_A)
_CucsVnicDynamicProviderEpTable_Object=MibTable
cucsVnicDynamicProviderEpTable=_CucsVnicDynamicProviderEpTable_Object((1,3,6,1,4,1,9,9,719,1,53,7))
if mibBuilder.loadTexts:cucsVnicDynamicProviderEpTable.setStatus(_A)
_CucsVnicDynamicProviderEpEntry_Object=MibTableRow
cucsVnicDynamicProviderEpEntry=_CucsVnicDynamicProviderEpEntry_Object((1,3,6,1,4,1,9,9,719,1,53,7,1))
cucsVnicDynamicProviderEpEntry.setIndexNames((0,_C,_K))
if mibBuilder.loadTexts:cucsVnicDynamicProviderEpEntry.setStatus(_A)
_CucsVnicDynamicProviderEpInstanceId_Type=CucsManagedObjectId
_CucsVnicDynamicProviderEpInstanceId_Object=MibTableColumn
cucsVnicDynamicProviderEpInstanceId=_CucsVnicDynamicProviderEpInstanceId_Object((1,3,6,1,4,1,9,9,719,1,53,7,1,1),_CucsVnicDynamicProviderEpInstanceId_Type())
cucsVnicDynamicProviderEpInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsVnicDynamicProviderEpInstanceId.setStatus(_A)
_CucsVnicDynamicProviderEpDn_Type=CucsManagedObjectDn
_CucsVnicDynamicProviderEpDn_Object=MibTableColumn
cucsVnicDynamicProviderEpDn=_CucsVnicDynamicProviderEpDn_Object((1,3,6,1,4,1,9,9,719,1,53,7,1,2),_CucsVnicDynamicProviderEpDn_Type())
cucsVnicDynamicProviderEpDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicDynamicProviderEpDn.setStatus(_A)
_CucsVnicDynamicProviderEpRn_Type=SnmpAdminString
_CucsVnicDynamicProviderEpRn_Object=MibTableColumn
cucsVnicDynamicProviderEpRn=_CucsVnicDynamicProviderEpRn_Object((1,3,6,1,4,1,9,9,719,1,53,7,1,3),_CucsVnicDynamicProviderEpRn_Type())
cucsVnicDynamicProviderEpRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicDynamicProviderEpRn.setStatus(_A)
_CucsVnicDynamicProviderEpChassisId_Type=Gauge32
_CucsVnicDynamicProviderEpChassisId_Object=MibTableColumn
cucsVnicDynamicProviderEpChassisId=_CucsVnicDynamicProviderEpChassisId_Object((1,3,6,1,4,1,9,9,719,1,53,7,1,4),_CucsVnicDynamicProviderEpChassisId_Type())
cucsVnicDynamicProviderEpChassisId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicDynamicProviderEpChassisId.setStatus(_A)
_CucsVnicDynamicProviderEpPortId_Type=Gauge32
_CucsVnicDynamicProviderEpPortId_Object=MibTableColumn
cucsVnicDynamicProviderEpPortId=_CucsVnicDynamicProviderEpPortId_Object((1,3,6,1,4,1,9,9,719,1,53,7,1,5),_CucsVnicDynamicProviderEpPortId_Type())
cucsVnicDynamicProviderEpPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicDynamicProviderEpPortId.setStatus(_A)
_CucsVnicDynamicProviderEpSlotId_Type=Gauge32
_CucsVnicDynamicProviderEpSlotId_Object=MibTableColumn
cucsVnicDynamicProviderEpSlotId=_CucsVnicDynamicProviderEpSlotId_Object((1,3,6,1,4,1,9,9,719,1,53,7,1,6),_CucsVnicDynamicProviderEpSlotId_Type())
cucsVnicDynamicProviderEpSlotId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicDynamicProviderEpSlotId.setStatus(_A)
_CucsVnicDynamicProviderEpSwitchId_Type=CucsNetworkSwitchId
_CucsVnicDynamicProviderEpSwitchId_Object=MibTableColumn
cucsVnicDynamicProviderEpSwitchId=_CucsVnicDynamicProviderEpSwitchId_Object((1,3,6,1,4,1,9,9,719,1,53,7,1,7),_CucsVnicDynamicProviderEpSwitchId_Type())
cucsVnicDynamicProviderEpSwitchId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicDynamicProviderEpSwitchId.setStatus(_A)
_CucsVnicEthLifTable_Object=MibTable
cucsVnicEthLifTable=_CucsVnicEthLifTable_Object((1,3,6,1,4,1,9,9,719,1,53,8))
if mibBuilder.loadTexts:cucsVnicEthLifTable.setStatus(_A)
_CucsVnicEthLifEntry_Object=MibTableRow
cucsVnicEthLifEntry=_CucsVnicEthLifEntry_Object((1,3,6,1,4,1,9,9,719,1,53,8,1))
cucsVnicEthLifEntry.setIndexNames((0,_C,_L))
if mibBuilder.loadTexts:cucsVnicEthLifEntry.setStatus(_A)
_CucsVnicEthLifInstanceId_Type=CucsManagedObjectId
_CucsVnicEthLifInstanceId_Object=MibTableColumn
cucsVnicEthLifInstanceId=_CucsVnicEthLifInstanceId_Object((1,3,6,1,4,1,9,9,719,1,53,8,1,1),_CucsVnicEthLifInstanceId_Type())
cucsVnicEthLifInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsVnicEthLifInstanceId.setStatus(_A)
_CucsVnicEthLifDn_Type=CucsManagedObjectDn
_CucsVnicEthLifDn_Object=MibTableColumn
cucsVnicEthLifDn=_CucsVnicEthLifDn_Object((1,3,6,1,4,1,9,9,719,1,53,8,1,2),_CucsVnicEthLifDn_Type())
cucsVnicEthLifDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicEthLifDn.setStatus(_A)
_CucsVnicEthLifRn_Type=SnmpAdminString
_CucsVnicEthLifRn_Object=MibTableColumn
cucsVnicEthLifRn=_CucsVnicEthLifRn_Object((1,3,6,1,4,1,9,9,719,1,53,8,1,3),_CucsVnicEthLifRn_Type())
cucsVnicEthLifRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicEthLifRn.setStatus(_A)
_CucsVnicEthLifAddr_Type=MacAddress
_CucsVnicEthLifAddr_Object=MibTableColumn
cucsVnicEthLifAddr=_CucsVnicEthLifAddr_Object((1,3,6,1,4,1,9,9,719,1,53,8,1,4),_CucsVnicEthLifAddr_Type())
cucsVnicEthLifAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicEthLifAddr.setStatus(_A)
_CucsVnicEthLifName_Type=SnmpAdminString
_CucsVnicEthLifName_Object=MibTableColumn
cucsVnicEthLifName=_CucsVnicEthLifName_Object((1,3,6,1,4,1,9,9,719,1,53,8,1,5),_CucsVnicEthLifName_Type())
cucsVnicEthLifName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicEthLifName.setStatus(_A)
_CucsVnicEthLifNicDn_Type=SnmpAdminString
_CucsVnicEthLifNicDn_Object=MibTableColumn
cucsVnicEthLifNicDn=_CucsVnicEthLifNicDn_Object((1,3,6,1,4,1,9,9,719,1,53,8,1,6),_CucsVnicEthLifNicDn_Type())
cucsVnicEthLifNicDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicEthLifNicDn.setStatus(_A)
_CucsVnicEthLifOwner_Type=CucsVnicConnectionOwner
_CucsVnicEthLifOwner_Object=MibTableColumn
cucsVnicEthLifOwner=_CucsVnicEthLifOwner_Object((1,3,6,1,4,1,9,9,719,1,53,8,1,7),_CucsVnicEthLifOwner_Type())
cucsVnicEthLifOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicEthLifOwner.setStatus(_A)
_CucsVnicEthLifSwitchId_Type=CucsNetworkSwitchId
_CucsVnicEthLifSwitchId_Object=MibTableColumn
cucsVnicEthLifSwitchId=_CucsVnicEthLifSwitchId_Object((1,3,6,1,4,1,9,9,719,1,53,8,1,8),_CucsVnicEthLifSwitchId_Type())
cucsVnicEthLifSwitchId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicEthLifSwitchId.setStatus(_A)
_CucsVnicEthLifType_Type=CucsVnicConnectionType
_CucsVnicEthLifType_Object=MibTableColumn
cucsVnicEthLifType=_CucsVnicEthLifType_Object((1,3,6,1,4,1,9,9,719,1,53,8,1,9),_CucsVnicEthLifType_Type())
cucsVnicEthLifType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicEthLifType.setStatus(_A)
_CucsVnicEthLifVnicDn_Type=SnmpAdminString
_CucsVnicEthLifVnicDn_Object=MibTableColumn
cucsVnicEthLifVnicDn=_CucsVnicEthLifVnicDn_Object((1,3,6,1,4,1,9,9,719,1,53,8,1,10),_CucsVnicEthLifVnicDn_Type())
cucsVnicEthLifVnicDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicEthLifVnicDn.setStatus(_A)
_CucsVnicEtherTable_Object=MibTable
cucsVnicEtherTable=_CucsVnicEtherTable_Object((1,3,6,1,4,1,9,9,719,1,53,9))
if mibBuilder.loadTexts:cucsVnicEtherTable.setStatus(_A)
_CucsVnicEtherEntry_Object=MibTableRow
cucsVnicEtherEntry=_CucsVnicEtherEntry_Object((1,3,6,1,4,1,9,9,719,1,53,9,1))
cucsVnicEtherEntry.setIndexNames((0,_C,_M))
if mibBuilder.loadTexts:cucsVnicEtherEntry.setStatus(_A)
_CucsVnicEtherInstanceId_Type=CucsManagedObjectId
_CucsVnicEtherInstanceId_Object=MibTableColumn
cucsVnicEtherInstanceId=_CucsVnicEtherInstanceId_Object((1,3,6,1,4,1,9,9,719,1,53,9,1,1),_CucsVnicEtherInstanceId_Type())
cucsVnicEtherInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsVnicEtherInstanceId.setStatus(_A)
_CucsVnicEtherDn_Type=CucsManagedObjectDn
_CucsVnicEtherDn_Object=MibTableColumn
cucsVnicEtherDn=_CucsVnicEtherDn_Object((1,3,6,1,4,1,9,9,719,1,53,9,1,2),_CucsVnicEtherDn_Type())
cucsVnicEtherDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicEtherDn.setStatus(_A)
_CucsVnicEtherRn_Type=SnmpAdminString
_CucsVnicEtherRn_Object=MibTableColumn
cucsVnicEtherRn=_CucsVnicEtherRn_Object((1,3,6,1,4,1,9,9,719,1,53,9,1,3),_CucsVnicEtherRn_Type())
cucsVnicEtherRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicEtherRn.setStatus(_A)
_CucsVnicEtherAdaptorProfileName_Type=SnmpAdminString
_CucsVnicEtherAdaptorProfileName_Object=MibTableColumn
cucsVnicEtherAdaptorProfileName=_CucsVnicEtherAdaptorProfileName_Object((1,3,6,1,4,1,9,9,719,1,53,9,1,4),_CucsVnicEtherAdaptorProfileName_Type())
cucsVnicEtherAdaptorProfileName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicEtherAdaptorProfileName.setStatus(_A)
_CucsVnicEtherAddr_Type=MacAddress
_CucsVnicEtherAddr_Object=MibTableColumn
cucsVnicEtherAddr=_CucsVnicEtherAddr_Object((1,3,6,1,4,1,9,9,719,1,53,9,1,5),_CucsVnicEtherAddr_Type())
cucsVnicEtherAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicEtherAddr.setStatus(_A)
_CucsVnicEtherAdminVcon_Type=SnmpAdminString
_CucsVnicEtherAdminVcon_Object=MibTableColumn
cucsVnicEtherAdminVcon=_CucsVnicEtherAdminVcon_Object((1,3,6,1,4,1,9,9,719,1,53,9,1,6),_CucsVnicEtherAdminVcon_Type())
cucsVnicEtherAdminVcon.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicEtherAdminVcon.setStatus(_A)
_CucsVnicEtherBootDev_Type=CucsVnicVnicBootDev
_CucsVnicEtherBootDev_Object=MibTableColumn
cucsVnicEtherBootDev=_CucsVnicEtherBootDev_Object((1,3,6,1,4,1,9,9,719,1,53,9,1,7),_CucsVnicEtherBootDev_Type())
cucsVnicEtherBootDev.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicEtherBootDev.setStatus(_A)
_CucsVnicEtherConfigState_Type=CucsLsConfigState
_CucsVnicEtherConfigState_Object=MibTableColumn
cucsVnicEtherConfigState=_CucsVnicEtherConfigState_Object((1,3,6,1,4,1,9,9,719,1,53,9,1,8),_CucsVnicEtherConfigState_Type())
cucsVnicEtherConfigState.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicEtherConfigState.setStatus(_A)
_CucsVnicEtherEquipmentDn_Type=SnmpAdminString
_CucsVnicEtherEquipmentDn_Object=MibTableColumn
cucsVnicEtherEquipmentDn=_CucsVnicEtherEquipmentDn_Object((1,3,6,1,4,1,9,9,719,1,53,9,1,9),_CucsVnicEtherEquipmentDn_Type())
cucsVnicEtherEquipmentDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicEtherEquipmentDn.setStatus(_A)
_CucsVnicEtherFltAggr_Type=Unsigned64
_CucsVnicEtherFltAggr_Object=MibTableColumn
cucsVnicEtherFltAggr=_CucsVnicEtherFltAggr_Object((1,3,6,1,4,1,9,9,719,1,53,9,1,10),_CucsVnicEtherFltAggr_Type())
cucsVnicEtherFltAggr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicEtherFltAggr.setStatus(_A)
_CucsVnicEtherIdentPoolName_Type=SnmpAdminString
_CucsVnicEtherIdentPoolName_Object=MibTableColumn
cucsVnicEtherIdentPoolName=_CucsVnicEtherIdentPoolName_Object((1,3,6,1,4,1,9,9,719,1,53,9,1,11),_CucsVnicEtherIdentPoolName_Type())
cucsVnicEtherIdentPoolName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicEtherIdentPoolName.setStatus(_A)
_CucsVnicEtherInstType_Type=CucsVnicInstantiation
_CucsVnicEtherInstType_Object=MibTableColumn
cucsVnicEtherInstType=_CucsVnicEtherInstType_Object((1,3,6,1,4,1,9,9,719,1,53,9,1,12),_CucsVnicEtherInstType_Type())
cucsVnicEtherInstType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicEtherInstType.setStatus(_A)
_CucsVnicEtherMtu_Type=Gauge32
_CucsVnicEtherMtu_Object=MibTableColumn
cucsVnicEtherMtu=_CucsVnicEtherMtu_Object((1,3,6,1,4,1,9,9,719,1,53,9,1,13),_CucsVnicEtherMtu_Type())
cucsVnicEtherMtu.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicEtherMtu.setStatus(_A)
_CucsVnicEtherName_Type=SnmpAdminString
_CucsVnicEtherName_Object=MibTableColumn
cucsVnicEtherName=_CucsVnicEtherName_Object((1,3,6,1,4,1,9,9,719,1,53,9,1,14),_CucsVnicEtherName_Type())
cucsVnicEtherName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicEtherName.setStatus(_A)
_CucsVnicEtherNwCtrlPolicyName_Type=SnmpAdminString
_CucsVnicEtherNwCtrlPolicyName_Object=MibTableColumn
cucsVnicEtherNwCtrlPolicyName=_CucsVnicEtherNwCtrlPolicyName_Object((1,3,6,1,4,1,9,9,719,1,53,9,1,15),_CucsVnicEtherNwCtrlPolicyName_Type())
cucsVnicEtherNwCtrlPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicEtherNwCtrlPolicyName.setStatus(_A)
_CucsVnicEtherNwTemplName_Type=SnmpAdminString
_CucsVnicEtherNwTemplName_Object=MibTableColumn
cucsVnicEtherNwTemplName=_CucsVnicEtherNwTemplName_Object((1,3,6,1,4,1,9,9,719,1,53,9,1,16),_CucsVnicEtherNwTemplName_Type())
cucsVnicEtherNwTemplName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicEtherNwTemplName.setStatus(_A)
_CucsVnicEtherOperAdaptorProfileName_Type=SnmpAdminString
_CucsVnicEtherOperAdaptorProfileName_Object=MibTableColumn
cucsVnicEtherOperAdaptorProfileName=_CucsVnicEtherOperAdaptorProfileName_Object((1,3,6,1,4,1,9,9,719,1,53,9,1,17),_CucsVnicEtherOperAdaptorProfileName_Type())
cucsVnicEtherOperAdaptorProfileName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicEtherOperAdaptorProfileName.setStatus(_A)
_CucsVnicEtherOperIdentPoolName_Type=SnmpAdminString
_CucsVnicEtherOperIdentPoolName_Object=MibTableColumn
cucsVnicEtherOperIdentPoolName=_CucsVnicEtherOperIdentPoolName_Object((1,3,6,1,4,1,9,9,719,1,53,9,1,18),_CucsVnicEtherOperIdentPoolName_Type())
cucsVnicEtherOperIdentPoolName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicEtherOperIdentPoolName.setStatus(_A)
_CucsVnicEtherOperNwCtrlPolicyName_Type=SnmpAdminString
_CucsVnicEtherOperNwCtrlPolicyName_Object=MibTableColumn
cucsVnicEtherOperNwCtrlPolicyName=_CucsVnicEtherOperNwCtrlPolicyName_Object((1,3,6,1,4,1,9,9,719,1,53,9,1,19),_CucsVnicEtherOperNwCtrlPolicyName_Type())
cucsVnicEtherOperNwCtrlPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicEtherOperNwCtrlPolicyName.setStatus(_A)
_CucsVnicEtherOperNwTemplName_Type=SnmpAdminString
_CucsVnicEtherOperNwTemplName_Object=MibTableColumn
cucsVnicEtherOperNwTemplName=_CucsVnicEtherOperNwTemplName_Object((1,3,6,1,4,1,9,9,719,1,53,9,1,20),_CucsVnicEtherOperNwTemplName_Type())
cucsVnicEtherOperNwTemplName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicEtherOperNwTemplName.setStatus(_A)
_CucsVnicEtherOperOrder_Type=Gauge32
_CucsVnicEtherOperOrder_Object=MibTableColumn
cucsVnicEtherOperOrder=_CucsVnicEtherOperOrder_Object((1,3,6,1,4,1,9,9,719,1,53,9,1,21),_CucsVnicEtherOperOrder_Type())
cucsVnicEtherOperOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicEtherOperOrder.setStatus(_A)
_CucsVnicEtherOperQosPolicyName_Type=SnmpAdminString
_CucsVnicEtherOperQosPolicyName_Object=MibTableColumn
cucsVnicEtherOperQosPolicyName=_CucsVnicEtherOperQosPolicyName_Object((1,3,6,1,4,1,9,9,719,1,53,9,1,22),_CucsVnicEtherOperQosPolicyName_Type())
cucsVnicEtherOperQosPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicEtherOperQosPolicyName.setStatus(_A)
_CucsVnicEtherOperSpeed_Type=Gauge32
_CucsVnicEtherOperSpeed_Object=MibTableColumn
cucsVnicEtherOperSpeed=_CucsVnicEtherOperSpeed_Object((1,3,6,1,4,1,9,9,719,1,53,9,1,23),_CucsVnicEtherOperSpeed_Type())
cucsVnicEtherOperSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicEtherOperSpeed.setStatus(_A)
_CucsVnicEtherOperStatsPolicyName_Type=SnmpAdminString
_CucsVnicEtherOperStatsPolicyName_Object=MibTableColumn
cucsVnicEtherOperStatsPolicyName=_CucsVnicEtherOperStatsPolicyName_Object((1,3,6,1,4,1,9,9,719,1,53,9,1,24),_CucsVnicEtherOperStatsPolicyName_Type())
cucsVnicEtherOperStatsPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicEtherOperStatsPolicyName.setStatus(_A)
_CucsVnicEtherOperVcon_Type=SnmpAdminString
_CucsVnicEtherOperVcon_Object=MibTableColumn
cucsVnicEtherOperVcon=_CucsVnicEtherOperVcon_Object((1,3,6,1,4,1,9,9,719,1,53,9,1,25),_CucsVnicEtherOperVcon_Type())
cucsVnicEtherOperVcon.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicEtherOperVcon.setStatus(_A)
_CucsVnicEtherOrder_Type=Gauge32
_CucsVnicEtherOrder_Object=MibTableColumn
cucsVnicEtherOrder=_CucsVnicEtherOrder_Object((1,3,6,1,4,1,9,9,719,1,53,9,1,26),_CucsVnicEtherOrder_Type())
cucsVnicEtherOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicEtherOrder.setStatus(_A)
_CucsVnicEtherOwner_Type=CucsVnicConnectionOwner
_CucsVnicEtherOwner_Object=MibTableColumn
cucsVnicEtherOwner=_CucsVnicEtherOwner_Object((1,3,6,1,4,1,9,9,719,1,53,9,1,27),_CucsVnicEtherOwner_Type())
cucsVnicEtherOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicEtherOwner.setStatus(_A)
_CucsVnicEtherPinToGroupName_Type=SnmpAdminString
_CucsVnicEtherPinToGroupName_Object=MibTableColumn
cucsVnicEtherPinToGroupName=_CucsVnicEtherPinToGroupName_Object((1,3,6,1,4,1,9,9,719,1,53,9,1,28),_CucsVnicEtherPinToGroupName_Type())
cucsVnicEtherPinToGroupName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicEtherPinToGroupName.setStatus(_A)
_CucsVnicEtherQosPolicyName_Type=SnmpAdminString
_CucsVnicEtherQosPolicyName_Object=MibTableColumn
cucsVnicEtherQosPolicyName=_CucsVnicEtherQosPolicyName_Object((1,3,6,1,4,1,9,9,719,1,53,9,1,29),_CucsVnicEtherQosPolicyName_Type())
cucsVnicEtherQosPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicEtherQosPolicyName.setStatus(_A)
_CucsVnicEtherStatsPolicyName_Type=SnmpAdminString
_CucsVnicEtherStatsPolicyName_Object=MibTableColumn
cucsVnicEtherStatsPolicyName=_CucsVnicEtherStatsPolicyName_Object((1,3,6,1,4,1,9,9,719,1,53,9,1,30),_CucsVnicEtherStatsPolicyName_Type())
cucsVnicEtherStatsPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicEtherStatsPolicyName.setStatus(_A)
_CucsVnicEtherSwitchId_Type=CucsVnicEtherBaseSwitchId
_CucsVnicEtherSwitchId_Object=MibTableColumn
cucsVnicEtherSwitchId=_CucsVnicEtherSwitchId_Object((1,3,6,1,4,1,9,9,719,1,53,9,1,31),_CucsVnicEtherSwitchId_Type())
cucsVnicEtherSwitchId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicEtherSwitchId.setStatus(_A)
_CucsVnicEtherType_Type=CucsVnicEtherType
_CucsVnicEtherType_Object=MibTableColumn
cucsVnicEtherType=_CucsVnicEtherType_Object((1,3,6,1,4,1,9,9,719,1,53,9,1,32),_CucsVnicEtherType_Type())
cucsVnicEtherType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicEtherType.setStatus(_A)
_CucsVnicEtherOperPinToGroupName_Type=SnmpAdminString
_CucsVnicEtherOperPinToGroupName_Object=MibTableColumn
cucsVnicEtherOperPinToGroupName=_CucsVnicEtherOperPinToGroupName_Object((1,3,6,1,4,1,9,9,719,1,53,9,1,33),_CucsVnicEtherOperPinToGroupName_Type())
cucsVnicEtherOperPinToGroupName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicEtherOperPinToGroupName.setStatus(_A)
_CucsVnicEtherConfigQualifier_Type=CucsVnicConfigIssues
_CucsVnicEtherConfigQualifier_Object=MibTableColumn
cucsVnicEtherConfigQualifier=_CucsVnicEtherConfigQualifier_Object((1,3,6,1,4,1,9,9,719,1,53,9,1,34),_CucsVnicEtherConfigQualifier_Type())
cucsVnicEtherConfigQualifier.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicEtherConfigQualifier.setStatus(_A)
_CucsVnicEtherDynamicId_Type=Gauge32
_CucsVnicEtherDynamicId_Object=MibTableColumn
cucsVnicEtherDynamicId=_CucsVnicEtherDynamicId_Object((1,3,6,1,4,1,9,9,719,1,53,9,1,35),_CucsVnicEtherDynamicId_Type())
cucsVnicEtherDynamicId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicEtherDynamicId.setStatus(_A)
_CucsVnicEtherPfDn_Type=SnmpAdminString
_CucsVnicEtherPfDn_Object=MibTableColumn
cucsVnicEtherPfDn=_CucsVnicEtherPfDn_Object((1,3,6,1,4,1,9,9,719,1,53,9,1,36),_CucsVnicEtherPfDn_Type())
cucsVnicEtherPfDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicEtherPfDn.setStatus(_A)
_CucsVnicEtherVirtualizationPreference_Type=CucsVnicVirtualizationPreferenceType
_CucsVnicEtherVirtualizationPreference_Object=MibTableColumn
cucsVnicEtherVirtualizationPreference=_CucsVnicEtherVirtualizationPreference_Object((1,3,6,1,4,1,9,9,719,1,53,9,1,37),_CucsVnicEtherVirtualizationPreference_Type())
cucsVnicEtherVirtualizationPreference.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicEtherVirtualizationPreference.setStatus(_A)
_CucsVnicEtherAdminHostPort_Type=CucsFabricHostPortId
_CucsVnicEtherAdminHostPort_Object=MibTableColumn
cucsVnicEtherAdminHostPort=_CucsVnicEtherAdminHostPort_Object((1,3,6,1,4,1,9,9,719,1,53,9,1,39),_CucsVnicEtherAdminHostPort_Type())
cucsVnicEtherAdminHostPort.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicEtherAdminHostPort.setStatus(_A)
_CucsVnicEtherOperHostPort_Type=CucsVnicVnicOperHostPort
_CucsVnicEtherOperHostPort_Object=MibTableColumn
cucsVnicEtherOperHostPort=_CucsVnicEtherOperHostPort_Object((1,3,6,1,4,1,9,9,719,1,53,9,1,40),_CucsVnicEtherOperHostPort_Type())
cucsVnicEtherOperHostPort.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicEtherOperHostPort.setStatus(_A)
_CucsVnicEtherPropAcl_Type=Unsigned64
_CucsVnicEtherPropAcl_Object=MibTableColumn
cucsVnicEtherPropAcl=_CucsVnicEtherPropAcl_Object((1,3,6,1,4,1,9,9,719,1,53,9,1,41),_CucsVnicEtherPropAcl_Type())
cucsVnicEtherPropAcl.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicEtherPropAcl.setStatus(_A)
_CucsVnicEtherPurpose_Type=CucsAdaptorPurpose
_CucsVnicEtherPurpose_Object=MibTableColumn
cucsVnicEtherPurpose=_CucsVnicEtherPurpose_Object((1,3,6,1,4,1,9,9,719,1,53,9,1,42),_CucsVnicEtherPurpose_Type())
cucsVnicEtherPurpose.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicEtherPurpose.setStatus(_A)
_CucsVnicEtherAdminCdnName_Type=SnmpAdminString
_CucsVnicEtherAdminCdnName_Object=MibTableColumn
cucsVnicEtherAdminCdnName=_CucsVnicEtherAdminCdnName_Object((1,3,6,1,4,1,9,9,719,1,53,9,1,43),_CucsVnicEtherAdminCdnName_Type())
cucsVnicEtherAdminCdnName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicEtherAdminCdnName.setStatus(_A)
_CucsVnicEtherOperCdnName_Type=SnmpAdminString
_CucsVnicEtherOperCdnName_Object=MibTableColumn
cucsVnicEtherOperCdnName=_CucsVnicEtherOperCdnName_Object((1,3,6,1,4,1,9,9,719,1,53,9,1,44),_CucsVnicEtherOperCdnName_Type())
cucsVnicEtherOperCdnName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicEtherOperCdnName.setStatus(_A)
_CucsVnicEtherCdnSource_Type=CucsVnicCdnSource
_CucsVnicEtherCdnSource_Object=MibTableColumn
cucsVnicEtherCdnSource=_CucsVnicEtherCdnSource_Object((1,3,6,1,4,1,9,9,719,1,53,9,1,45),_CucsVnicEtherCdnSource_Type())
cucsVnicEtherCdnSource.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicEtherCdnSource.setStatus(_A)
_CucsVnicEtherCdnPropInSync_Type=TruthValue
_CucsVnicEtherCdnPropInSync_Object=MibTableColumn
cucsVnicEtherCdnPropInSync=_CucsVnicEtherCdnPropInSync_Object((1,3,6,1,4,1,9,9,719,1,53,9,1,46),_CucsVnicEtherCdnPropInSync_Type())
cucsVnicEtherCdnPropInSync.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicEtherCdnPropInSync.setStatus(_A)
_CucsVnicEtherRedundancyPairType_Type=CucsVnicRedundancyPairType
_CucsVnicEtherRedundancyPairType_Object=MibTableColumn
cucsVnicEtherRedundancyPairType=_CucsVnicEtherRedundancyPairType_Object((1,3,6,1,4,1,9,9,719,1,53,9,1,47),_CucsVnicEtherRedundancyPairType_Type())
cucsVnicEtherRedundancyPairType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicEtherRedundancyPairType.setStatus(_A)
_CucsVnicEtherRedundancyPeer_Type=SnmpAdminString
_CucsVnicEtherRedundancyPeer_Object=MibTableColumn
cucsVnicEtherRedundancyPeer=_CucsVnicEtherRedundancyPeer_Object((1,3,6,1,4,1,9,9,719,1,53,9,1,48),_CucsVnicEtherRedundancyPeer_Type())
cucsVnicEtherRedundancyPeer.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicEtherRedundancyPeer.setStatus(_A)
_CucsVnicEtherIfTable_Object=MibTable
cucsVnicEtherIfTable=_CucsVnicEtherIfTable_Object((1,3,6,1,4,1,9,9,719,1,53,10))
if mibBuilder.loadTexts:cucsVnicEtherIfTable.setStatus(_A)
_CucsVnicEtherIfEntry_Object=MibTableRow
cucsVnicEtherIfEntry=_CucsVnicEtherIfEntry_Object((1,3,6,1,4,1,9,9,719,1,53,10,1))
cucsVnicEtherIfEntry.setIndexNames((0,_C,_N))
if mibBuilder.loadTexts:cucsVnicEtherIfEntry.setStatus(_A)
_CucsVnicEtherIfInstanceId_Type=CucsManagedObjectId
_CucsVnicEtherIfInstanceId_Object=MibTableColumn
cucsVnicEtherIfInstanceId=_CucsVnicEtherIfInstanceId_Object((1,3,6,1,4,1,9,9,719,1,53,10,1,1),_CucsVnicEtherIfInstanceId_Type())
cucsVnicEtherIfInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsVnicEtherIfInstanceId.setStatus(_A)
_CucsVnicEtherIfDn_Type=CucsManagedObjectDn
_CucsVnicEtherIfDn_Object=MibTableColumn
cucsVnicEtherIfDn=_CucsVnicEtherIfDn_Object((1,3,6,1,4,1,9,9,719,1,53,10,1,2),_CucsVnicEtherIfDn_Type())
cucsVnicEtherIfDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicEtherIfDn.setStatus(_A)
_CucsVnicEtherIfRn_Type=SnmpAdminString
_CucsVnicEtherIfRn_Object=MibTableColumn
cucsVnicEtherIfRn=_CucsVnicEtherIfRn_Object((1,3,6,1,4,1,9,9,719,1,53,10,1,3),_CucsVnicEtherIfRn_Type())
cucsVnicEtherIfRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicEtherIfRn.setStatus(_A)
_CucsVnicEtherIfAddr_Type=MacAddress
_CucsVnicEtherIfAddr_Object=MibTableColumn
cucsVnicEtherIfAddr=_CucsVnicEtherIfAddr_Object((1,3,6,1,4,1,9,9,719,1,53,10,1,4),_CucsVnicEtherIfAddr_Type())
cucsVnicEtherIfAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicEtherIfAddr.setStatus(_A)
_CucsVnicEtherIfDefaultNet_Type=TruthValue
_CucsVnicEtherIfDefaultNet_Object=MibTableColumn
cucsVnicEtherIfDefaultNet=_CucsVnicEtherIfDefaultNet_Object((1,3,6,1,4,1,9,9,719,1,53,10,1,5),_CucsVnicEtherIfDefaultNet_Type())
cucsVnicEtherIfDefaultNet.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicEtherIfDefaultNet.setStatus(_A)
_CucsVnicEtherIfName_Type=SnmpAdminString
_CucsVnicEtherIfName_Object=MibTableColumn
cucsVnicEtherIfName=_CucsVnicEtherIfName_Object((1,3,6,1,4,1,9,9,719,1,53,10,1,6),_CucsVnicEtherIfName_Type())
cucsVnicEtherIfName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicEtherIfName.setStatus(_A)
_CucsVnicEtherIfOperState_Type=CucsVnicIfOperState
_CucsVnicEtherIfOperState_Object=MibTableColumn
cucsVnicEtherIfOperState=_CucsVnicEtherIfOperState_Object((1,3,6,1,4,1,9,9,719,1,53,10,1,7),_CucsVnicEtherIfOperState_Type())
cucsVnicEtherIfOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicEtherIfOperState.setStatus(_A)
_CucsVnicEtherIfOwner_Type=CucsVnicConnectionOwner
_CucsVnicEtherIfOwner_Object=MibTableColumn
cucsVnicEtherIfOwner=_CucsVnicEtherIfOwner_Object((1,3,6,1,4,1,9,9,719,1,53,10,1,8),_CucsVnicEtherIfOwner_Type())
cucsVnicEtherIfOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicEtherIfOwner.setStatus(_A)
_CucsVnicEtherIfSwitchId_Type=CucsVnicEtherBaseIfSwitchId
_CucsVnicEtherIfSwitchId_Object=MibTableColumn
cucsVnicEtherIfSwitchId=_CucsVnicEtherIfSwitchId_Object((1,3,6,1,4,1,9,9,719,1,53,10,1,9),_CucsVnicEtherIfSwitchId_Type())
cucsVnicEtherIfSwitchId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicEtherIfSwitchId.setStatus(_A)
_CucsVnicEtherIfType_Type=CucsVnicAEtherIfType
_CucsVnicEtherIfType_Object=MibTableColumn
cucsVnicEtherIfType=_CucsVnicEtherIfType_Object((1,3,6,1,4,1,9,9,719,1,53,10,1,10),_CucsVnicEtherIfType_Type())
cucsVnicEtherIfType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicEtherIfType.setStatus(_A)
_CucsVnicEtherIfVnet_Type=Gauge32
_CucsVnicEtherIfVnet_Object=MibTableColumn
cucsVnicEtherIfVnet=_CucsVnicEtherIfVnet_Object((1,3,6,1,4,1,9,9,719,1,53,10,1,11),_CucsVnicEtherIfVnet_Type())
cucsVnicEtherIfVnet.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicEtherIfVnet.setStatus(_A)
_CucsVnicEtherIfOperVnetDn_Type=SnmpAdminString
_CucsVnicEtherIfOperVnetDn_Object=MibTableColumn
cucsVnicEtherIfOperVnetDn=_CucsVnicEtherIfOperVnetDn_Object((1,3,6,1,4,1,9,9,719,1,53,10,1,12),_CucsVnicEtherIfOperVnetDn_Type())
cucsVnicEtherIfOperVnetDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicEtherIfOperVnetDn.setStatus(_A)
_CucsVnicEtherIfOperVnetName_Type=SnmpAdminString
_CucsVnicEtherIfOperVnetName_Object=MibTableColumn
cucsVnicEtherIfOperVnetName=_CucsVnicEtherIfOperVnetName_Object((1,3,6,1,4,1,9,9,719,1,53,10,1,13),_CucsVnicEtherIfOperVnetName_Type())
cucsVnicEtherIfOperVnetName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicEtherIfOperVnetName.setStatus(_A)
_CucsVnicEtherIfConfigQualifier_Type=CucsVnicConfigIssues
_CucsVnicEtherIfConfigQualifier_Object=MibTableColumn
cucsVnicEtherIfConfigQualifier=_CucsVnicEtherIfConfigQualifier_Object((1,3,6,1,4,1,9,9,719,1,53,10,1,14),_CucsVnicEtherIfConfigQualifier_Type())
cucsVnicEtherIfConfigQualifier.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicEtherIfConfigQualifier.setStatus(_A)
_CucsVnicEtherIfFltAggr_Type=Unsigned64
_CucsVnicEtherIfFltAggr_Object=MibTableColumn
cucsVnicEtherIfFltAggr=_CucsVnicEtherIfFltAggr_Object((1,3,6,1,4,1,9,9,719,1,53,10,1,15),_CucsVnicEtherIfFltAggr_Type())
cucsVnicEtherIfFltAggr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicEtherIfFltAggr.setStatus(_A)
_CucsVnicEtherIfPubNwId_Type=Gauge32
_CucsVnicEtherIfPubNwId_Object=MibTableColumn
cucsVnicEtherIfPubNwId=_CucsVnicEtherIfPubNwId_Object((1,3,6,1,4,1,9,9,719,1,53,10,1,17),_CucsVnicEtherIfPubNwId_Type())
cucsVnicEtherIfPubNwId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicEtherIfPubNwId.setStatus(_A)
_CucsVnicEtherIfSharing_Type=CucsFabricVlanSharingType
_CucsVnicEtherIfSharing_Object=MibTableColumn
cucsVnicEtherIfSharing=_CucsVnicEtherIfSharing_Object((1,3,6,1,4,1,9,9,719,1,53,10,1,18),_CucsVnicEtherIfSharing_Type())
cucsVnicEtherIfSharing.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicEtherIfSharing.setStatus(_A)
_CucsVnicEtherIfPropAcl_Type=Unsigned64
_CucsVnicEtherIfPropAcl_Object=MibTableColumn
cucsVnicEtherIfPropAcl=_CucsVnicEtherIfPropAcl_Object((1,3,6,1,4,1,9,9,719,1,53,10,1,19),_CucsVnicEtherIfPropAcl_Type())
cucsVnicEtherIfPropAcl.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicEtherIfPropAcl.setStatus(_A)
_CucsVnicEtherIfOperPrimaryVnetDn_Type=SnmpAdminString
_CucsVnicEtherIfOperPrimaryVnetDn_Object=MibTableColumn
cucsVnicEtherIfOperPrimaryVnetDn=_CucsVnicEtherIfOperPrimaryVnetDn_Object((1,3,6,1,4,1,9,9,719,1,53,10,1,20),_CucsVnicEtherIfOperPrimaryVnetDn_Type())
cucsVnicEtherIfOperPrimaryVnetDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicEtherIfOperPrimaryVnetDn.setStatus(_A)
_CucsVnicEtherIfOperPrimaryVnetName_Type=SnmpAdminString
_CucsVnicEtherIfOperPrimaryVnetName_Object=MibTableColumn
cucsVnicEtherIfOperPrimaryVnetName=_CucsVnicEtherIfOperPrimaryVnetName_Object((1,3,6,1,4,1,9,9,719,1,53,10,1,21),_CucsVnicEtherIfOperPrimaryVnetName_Type())
cucsVnicEtherIfOperPrimaryVnetName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicEtherIfOperPrimaryVnetName.setStatus(_A)
_CucsVnicFcTable_Object=MibTable
cucsVnicFcTable=_CucsVnicFcTable_Object((1,3,6,1,4,1,9,9,719,1,53,11))
if mibBuilder.loadTexts:cucsVnicFcTable.setStatus(_A)
_CucsVnicFcEntry_Object=MibTableRow
cucsVnicFcEntry=_CucsVnicFcEntry_Object((1,3,6,1,4,1,9,9,719,1,53,11,1))
cucsVnicFcEntry.setIndexNames((0,_C,_O))
if mibBuilder.loadTexts:cucsVnicFcEntry.setStatus(_A)
_CucsVnicFcInstanceId_Type=CucsManagedObjectId
_CucsVnicFcInstanceId_Object=MibTableColumn
cucsVnicFcInstanceId=_CucsVnicFcInstanceId_Object((1,3,6,1,4,1,9,9,719,1,53,11,1,1),_CucsVnicFcInstanceId_Type())
cucsVnicFcInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsVnicFcInstanceId.setStatus(_A)
_CucsVnicFcDn_Type=CucsManagedObjectDn
_CucsVnicFcDn_Object=MibTableColumn
cucsVnicFcDn=_CucsVnicFcDn_Object((1,3,6,1,4,1,9,9,719,1,53,11,1,2),_CucsVnicFcDn_Type())
cucsVnicFcDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcDn.setStatus(_A)
_CucsVnicFcRn_Type=SnmpAdminString
_CucsVnicFcRn_Object=MibTableColumn
cucsVnicFcRn=_CucsVnicFcRn_Object((1,3,6,1,4,1,9,9,719,1,53,11,1,3),_CucsVnicFcRn_Type())
cucsVnicFcRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcRn.setStatus(_A)
_CucsVnicFcAdaptorProfileName_Type=SnmpAdminString
_CucsVnicFcAdaptorProfileName_Object=MibTableColumn
cucsVnicFcAdaptorProfileName=_CucsVnicFcAdaptorProfileName_Object((1,3,6,1,4,1,9,9,719,1,53,11,1,4),_CucsVnicFcAdaptorProfileName_Type())
cucsVnicFcAdaptorProfileName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcAdaptorProfileName.setStatus(_A)
_CucsVnicFcAddr_Type=Unsigned64
_CucsVnicFcAddr_Object=MibTableColumn
cucsVnicFcAddr=_CucsVnicFcAddr_Object((1,3,6,1,4,1,9,9,719,1,53,11,1,5),_CucsVnicFcAddr_Type())
cucsVnicFcAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcAddr.setStatus(_A)
_CucsVnicFcAdminVcon_Type=SnmpAdminString
_CucsVnicFcAdminVcon_Object=MibTableColumn
cucsVnicFcAdminVcon=_CucsVnicFcAdminVcon_Object((1,3,6,1,4,1,9,9,719,1,53,11,1,6),_CucsVnicFcAdminVcon_Type())
cucsVnicFcAdminVcon.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcAdminVcon.setStatus(_A)
_CucsVnicFcBootDev_Type=CucsVnicVnicBootDev
_CucsVnicFcBootDev_Object=MibTableColumn
cucsVnicFcBootDev=_CucsVnicFcBootDev_Object((1,3,6,1,4,1,9,9,719,1,53,11,1,7),_CucsVnicFcBootDev_Type())
cucsVnicFcBootDev.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcBootDev.setStatus(_A)
_CucsVnicFcConfigState_Type=CucsLsConfigState
_CucsVnicFcConfigState_Object=MibTableColumn
cucsVnicFcConfigState=_CucsVnicFcConfigState_Object((1,3,6,1,4,1,9,9,719,1,53,11,1,8),_CucsVnicFcConfigState_Type())
cucsVnicFcConfigState.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcConfigState.setStatus(_A)
_CucsVnicFcEquipmentDn_Type=SnmpAdminString
_CucsVnicFcEquipmentDn_Object=MibTableColumn
cucsVnicFcEquipmentDn=_CucsVnicFcEquipmentDn_Object((1,3,6,1,4,1,9,9,719,1,53,11,1,9),_CucsVnicFcEquipmentDn_Type())
cucsVnicFcEquipmentDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcEquipmentDn.setStatus(_A)
_CucsVnicFcFltAggr_Type=Unsigned64
_CucsVnicFcFltAggr_Object=MibTableColumn
cucsVnicFcFltAggr=_CucsVnicFcFltAggr_Object((1,3,6,1,4,1,9,9,719,1,53,11,1,10),_CucsVnicFcFltAggr_Type())
cucsVnicFcFltAggr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcFltAggr.setStatus(_A)
_CucsVnicFcIdentPoolName_Type=SnmpAdminString
_CucsVnicFcIdentPoolName_Object=MibTableColumn
cucsVnicFcIdentPoolName=_CucsVnicFcIdentPoolName_Object((1,3,6,1,4,1,9,9,719,1,53,11,1,11),_CucsVnicFcIdentPoolName_Type())
cucsVnicFcIdentPoolName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcIdentPoolName.setStatus(_A)
_CucsVnicFcInstType_Type=CucsVnicInstantiation
_CucsVnicFcInstType_Object=MibTableColumn
cucsVnicFcInstType=_CucsVnicFcInstType_Object((1,3,6,1,4,1,9,9,719,1,53,11,1,12),_CucsVnicFcInstType_Type())
cucsVnicFcInstType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcInstType.setStatus(_A)
_CucsVnicFcMaxDataFieldSize_Type=Gauge32
_CucsVnicFcMaxDataFieldSize_Object=MibTableColumn
cucsVnicFcMaxDataFieldSize=_CucsVnicFcMaxDataFieldSize_Object((1,3,6,1,4,1,9,9,719,1,53,11,1,13),_CucsVnicFcMaxDataFieldSize_Type())
cucsVnicFcMaxDataFieldSize.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcMaxDataFieldSize.setStatus(_A)
_CucsVnicFcName_Type=SnmpAdminString
_CucsVnicFcName_Object=MibTableColumn
cucsVnicFcName=_CucsVnicFcName_Object((1,3,6,1,4,1,9,9,719,1,53,11,1,14),_CucsVnicFcName_Type())
cucsVnicFcName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcName.setStatus(_A)
_CucsVnicFcNdAddr_Type=Unsigned64
_CucsVnicFcNdAddr_Object=MibTableColumn
cucsVnicFcNdAddr=_CucsVnicFcNdAddr_Object((1,3,6,1,4,1,9,9,719,1,53,11,1,15),_CucsVnicFcNdAddr_Type())
cucsVnicFcNdAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcNdAddr.setStatus(_A)
_CucsVnicFcNwTemplName_Type=SnmpAdminString
_CucsVnicFcNwTemplName_Object=MibTableColumn
cucsVnicFcNwTemplName=_CucsVnicFcNwTemplName_Object((1,3,6,1,4,1,9,9,719,1,53,11,1,16),_CucsVnicFcNwTemplName_Type())
cucsVnicFcNwTemplName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcNwTemplName.setStatus(_A)
_CucsVnicFcOperAdaptorProfileName_Type=SnmpAdminString
_CucsVnicFcOperAdaptorProfileName_Object=MibTableColumn
cucsVnicFcOperAdaptorProfileName=_CucsVnicFcOperAdaptorProfileName_Object((1,3,6,1,4,1,9,9,719,1,53,11,1,17),_CucsVnicFcOperAdaptorProfileName_Type())
cucsVnicFcOperAdaptorProfileName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcOperAdaptorProfileName.setStatus(_A)
_CucsVnicFcOperIdentPoolName_Type=SnmpAdminString
_CucsVnicFcOperIdentPoolName_Object=MibTableColumn
cucsVnicFcOperIdentPoolName=_CucsVnicFcOperIdentPoolName_Object((1,3,6,1,4,1,9,9,719,1,53,11,1,18),_CucsVnicFcOperIdentPoolName_Type())
cucsVnicFcOperIdentPoolName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcOperIdentPoolName.setStatus(_A)
_CucsVnicFcOperNwTemplName_Type=SnmpAdminString
_CucsVnicFcOperNwTemplName_Object=MibTableColumn
cucsVnicFcOperNwTemplName=_CucsVnicFcOperNwTemplName_Object((1,3,6,1,4,1,9,9,719,1,53,11,1,19),_CucsVnicFcOperNwTemplName_Type())
cucsVnicFcOperNwTemplName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcOperNwTemplName.setStatus(_A)
_CucsVnicFcOperOrder_Type=Gauge32
_CucsVnicFcOperOrder_Object=MibTableColumn
cucsVnicFcOperOrder=_CucsVnicFcOperOrder_Object((1,3,6,1,4,1,9,9,719,1,53,11,1,20),_CucsVnicFcOperOrder_Type())
cucsVnicFcOperOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcOperOrder.setStatus(_A)
_CucsVnicFcOperQosPolicyName_Type=SnmpAdminString
_CucsVnicFcOperQosPolicyName_Object=MibTableColumn
cucsVnicFcOperQosPolicyName=_CucsVnicFcOperQosPolicyName_Object((1,3,6,1,4,1,9,9,719,1,53,11,1,21),_CucsVnicFcOperQosPolicyName_Type())
cucsVnicFcOperQosPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcOperQosPolicyName.setStatus(_A)
_CucsVnicFcOperSpeed_Type=Gauge32
_CucsVnicFcOperSpeed_Object=MibTableColumn
cucsVnicFcOperSpeed=_CucsVnicFcOperSpeed_Object((1,3,6,1,4,1,9,9,719,1,53,11,1,22),_CucsVnicFcOperSpeed_Type())
cucsVnicFcOperSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcOperSpeed.setStatus(_A)
_CucsVnicFcOperStatsPolicyName_Type=SnmpAdminString
_CucsVnicFcOperStatsPolicyName_Object=MibTableColumn
cucsVnicFcOperStatsPolicyName=_CucsVnicFcOperStatsPolicyName_Object((1,3,6,1,4,1,9,9,719,1,53,11,1,23),_CucsVnicFcOperStatsPolicyName_Type())
cucsVnicFcOperStatsPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcOperStatsPolicyName.setStatus(_A)
_CucsVnicFcOperVcon_Type=SnmpAdminString
_CucsVnicFcOperVcon_Object=MibTableColumn
cucsVnicFcOperVcon=_CucsVnicFcOperVcon_Object((1,3,6,1,4,1,9,9,719,1,53,11,1,24),_CucsVnicFcOperVcon_Type())
cucsVnicFcOperVcon.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcOperVcon.setStatus(_A)
_CucsVnicFcOrder_Type=Gauge32
_CucsVnicFcOrder_Object=MibTableColumn
cucsVnicFcOrder=_CucsVnicFcOrder_Object((1,3,6,1,4,1,9,9,719,1,53,11,1,25),_CucsVnicFcOrder_Type())
cucsVnicFcOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcOrder.setStatus(_A)
_CucsVnicFcOwner_Type=CucsVnicConnectionOwner
_CucsVnicFcOwner_Object=MibTableColumn
cucsVnicFcOwner=_CucsVnicFcOwner_Object((1,3,6,1,4,1,9,9,719,1,53,11,1,26),_CucsVnicFcOwner_Type())
cucsVnicFcOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcOwner.setStatus(_A)
_CucsVnicFcPersBind_Type=CucsVnicFcBasePersBind
_CucsVnicFcPersBind_Object=MibTableColumn
cucsVnicFcPersBind=_CucsVnicFcPersBind_Object((1,3,6,1,4,1,9,9,719,1,53,11,1,27),_CucsVnicFcPersBind_Type())
cucsVnicFcPersBind.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcPersBind.setStatus(_A)
_CucsVnicFcPersBindClear_Type=TruthValue
_CucsVnicFcPersBindClear_Object=MibTableColumn
cucsVnicFcPersBindClear=_CucsVnicFcPersBindClear_Object((1,3,6,1,4,1,9,9,719,1,53,11,1,28),_CucsVnicFcPersBindClear_Type())
cucsVnicFcPersBindClear.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcPersBindClear.setStatus(_A)
_CucsVnicFcPinToGroupName_Type=SnmpAdminString
_CucsVnicFcPinToGroupName_Object=MibTableColumn
cucsVnicFcPinToGroupName=_CucsVnicFcPinToGroupName_Object((1,3,6,1,4,1,9,9,719,1,53,11,1,29),_CucsVnicFcPinToGroupName_Type())
cucsVnicFcPinToGroupName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcPinToGroupName.setStatus(_A)
_CucsVnicFcQosPolicyName_Type=SnmpAdminString
_CucsVnicFcQosPolicyName_Object=MibTableColumn
cucsVnicFcQosPolicyName=_CucsVnicFcQosPolicyName_Object((1,3,6,1,4,1,9,9,719,1,53,11,1,30),_CucsVnicFcQosPolicyName_Type())
cucsVnicFcQosPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcQosPolicyName.setStatus(_A)
_CucsVnicFcStatsPolicyName_Type=SnmpAdminString
_CucsVnicFcStatsPolicyName_Object=MibTableColumn
cucsVnicFcStatsPolicyName=_CucsVnicFcStatsPolicyName_Object((1,3,6,1,4,1,9,9,719,1,53,11,1,31),_CucsVnicFcStatsPolicyName_Type())
cucsVnicFcStatsPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcStatsPolicyName.setStatus(_A)
_CucsVnicFcSwitchId_Type=CucsNetworkSwitchId
_CucsVnicFcSwitchId_Object=MibTableColumn
cucsVnicFcSwitchId=_CucsVnicFcSwitchId_Object((1,3,6,1,4,1,9,9,719,1,53,11,1,32),_CucsVnicFcSwitchId_Type())
cucsVnicFcSwitchId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcSwitchId.setStatus(_A)
_CucsVnicFcType_Type=CucsVnicFcBaseType
_CucsVnicFcType_Object=MibTableColumn
cucsVnicFcType=_CucsVnicFcType_Object((1,3,6,1,4,1,9,9,719,1,53,11,1,33),_CucsVnicFcType_Type())
cucsVnicFcType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcType.setStatus(_A)
_CucsVnicFcOperPinToGroupName_Type=SnmpAdminString
_CucsVnicFcOperPinToGroupName_Object=MibTableColumn
cucsVnicFcOperPinToGroupName=_CucsVnicFcOperPinToGroupName_Object((1,3,6,1,4,1,9,9,719,1,53,11,1,34),_CucsVnicFcOperPinToGroupName_Type())
cucsVnicFcOperPinToGroupName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcOperPinToGroupName.setStatus(_A)
_CucsVnicFcConfigQualifier_Type=CucsVnicConfigIssues
_CucsVnicFcConfigQualifier_Object=MibTableColumn
cucsVnicFcConfigQualifier=_CucsVnicFcConfigQualifier_Object((1,3,6,1,4,1,9,9,719,1,53,11,1,35),_CucsVnicFcConfigQualifier_Type())
cucsVnicFcConfigQualifier.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcConfigQualifier.setStatus(_A)
_CucsVnicFcAdminHostPort_Type=CucsFabricHostPortId
_CucsVnicFcAdminHostPort_Object=MibTableColumn
cucsVnicFcAdminHostPort=_CucsVnicFcAdminHostPort_Object((1,3,6,1,4,1,9,9,719,1,53,11,1,37),_CucsVnicFcAdminHostPort_Type())
cucsVnicFcAdminHostPort.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcAdminHostPort.setStatus(_A)
_CucsVnicFcOperHostPort_Type=CucsVnicVnicOperHostPort
_CucsVnicFcOperHostPort_Object=MibTableColumn
cucsVnicFcOperHostPort=_CucsVnicFcOperHostPort_Object((1,3,6,1,4,1,9,9,719,1,53,11,1,38),_CucsVnicFcOperHostPort_Type())
cucsVnicFcOperHostPort.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcOperHostPort.setStatus(_A)
_CucsVnicFcAdminCdnName_Type=SnmpAdminString
_CucsVnicFcAdminCdnName_Object=MibTableColumn
cucsVnicFcAdminCdnName=_CucsVnicFcAdminCdnName_Object((1,3,6,1,4,1,9,9,719,1,53,11,1,39),_CucsVnicFcAdminCdnName_Type())
cucsVnicFcAdminCdnName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcAdminCdnName.setStatus(_A)
_CucsVnicFcOperCdnName_Type=SnmpAdminString
_CucsVnicFcOperCdnName_Object=MibTableColumn
cucsVnicFcOperCdnName=_CucsVnicFcOperCdnName_Object((1,3,6,1,4,1,9,9,719,1,53,11,1,40),_CucsVnicFcOperCdnName_Type())
cucsVnicFcOperCdnName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcOperCdnName.setStatus(_A)
_CucsVnicFcCdnSource_Type=CucsVnicCdnSource
_CucsVnicFcCdnSource_Object=MibTableColumn
cucsVnicFcCdnSource=_CucsVnicFcCdnSource_Object((1,3,6,1,4,1,9,9,719,1,53,11,1,41),_CucsVnicFcCdnSource_Type())
cucsVnicFcCdnSource.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcCdnSource.setStatus(_A)
_CucsVnicFcCdnPropInSync_Type=TruthValue
_CucsVnicFcCdnPropInSync_Object=MibTableColumn
cucsVnicFcCdnPropInSync=_CucsVnicFcCdnPropInSync_Object((1,3,6,1,4,1,9,9,719,1,53,11,1,42),_CucsVnicFcCdnPropInSync_Type())
cucsVnicFcCdnPropInSync.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcCdnPropInSync.setStatus(_A)
_CucsVnicFcRedundancyPairType_Type=CucsVnicRedundancyPairType
_CucsVnicFcRedundancyPairType_Object=MibTableColumn
cucsVnicFcRedundancyPairType=_CucsVnicFcRedundancyPairType_Object((1,3,6,1,4,1,9,9,719,1,53,11,1,43),_CucsVnicFcRedundancyPairType_Type())
cucsVnicFcRedundancyPairType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcRedundancyPairType.setStatus(_A)
_CucsVnicFcRedundancyPeer_Type=SnmpAdminString
_CucsVnicFcRedundancyPeer_Object=MibTableColumn
cucsVnicFcRedundancyPeer=_CucsVnicFcRedundancyPeer_Object((1,3,6,1,4,1,9,9,719,1,53,11,1,44),_CucsVnicFcRedundancyPeer_Type())
cucsVnicFcRedundancyPeer.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcRedundancyPeer.setStatus(_A)
_CucsVnicFcIfTable_Object=MibTable
cucsVnicFcIfTable=_CucsVnicFcIfTable_Object((1,3,6,1,4,1,9,9,719,1,53,12))
if mibBuilder.loadTexts:cucsVnicFcIfTable.setStatus(_A)
_CucsVnicFcIfEntry_Object=MibTableRow
cucsVnicFcIfEntry=_CucsVnicFcIfEntry_Object((1,3,6,1,4,1,9,9,719,1,53,12,1))
cucsVnicFcIfEntry.setIndexNames((0,_C,_P))
if mibBuilder.loadTexts:cucsVnicFcIfEntry.setStatus(_A)
_CucsVnicFcIfInstanceId_Type=CucsManagedObjectId
_CucsVnicFcIfInstanceId_Object=MibTableColumn
cucsVnicFcIfInstanceId=_CucsVnicFcIfInstanceId_Object((1,3,6,1,4,1,9,9,719,1,53,12,1,1),_CucsVnicFcIfInstanceId_Type())
cucsVnicFcIfInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsVnicFcIfInstanceId.setStatus(_A)
_CucsVnicFcIfDn_Type=CucsManagedObjectDn
_CucsVnicFcIfDn_Object=MibTableColumn
cucsVnicFcIfDn=_CucsVnicFcIfDn_Object((1,3,6,1,4,1,9,9,719,1,53,12,1,2),_CucsVnicFcIfDn_Type())
cucsVnicFcIfDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcIfDn.setStatus(_A)
_CucsVnicFcIfRn_Type=SnmpAdminString
_CucsVnicFcIfRn_Object=MibTableColumn
cucsVnicFcIfRn=_CucsVnicFcIfRn_Object((1,3,6,1,4,1,9,9,719,1,53,12,1,3),_CucsVnicFcIfRn_Type())
cucsVnicFcIfRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcIfRn.setStatus(_A)
_CucsVnicFcIfInitiator_Type=Unsigned64
_CucsVnicFcIfInitiator_Object=MibTableColumn
cucsVnicFcIfInitiator=_CucsVnicFcIfInitiator_Object((1,3,6,1,4,1,9,9,719,1,53,12,1,4),_CucsVnicFcIfInitiator_Type())
cucsVnicFcIfInitiator.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcIfInitiator.setStatus(_A)
_CucsVnicFcIfName_Type=SnmpAdminString
_CucsVnicFcIfName_Object=MibTableColumn
cucsVnicFcIfName=_CucsVnicFcIfName_Object((1,3,6,1,4,1,9,9,719,1,53,12,1,5),_CucsVnicFcIfName_Type())
cucsVnicFcIfName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcIfName.setStatus(_A)
_CucsVnicFcIfOperState_Type=CucsVnicIfOperState
_CucsVnicFcIfOperState_Object=MibTableColumn
cucsVnicFcIfOperState=_CucsVnicFcIfOperState_Object((1,3,6,1,4,1,9,9,719,1,53,12,1,6),_CucsVnicFcIfOperState_Type())
cucsVnicFcIfOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcIfOperState.setStatus(_A)
_CucsVnicFcIfOwner_Type=CucsVnicConnectionOwner
_CucsVnicFcIfOwner_Object=MibTableColumn
cucsVnicFcIfOwner=_CucsVnicFcIfOwner_Object((1,3,6,1,4,1,9,9,719,1,53,12,1,7),_CucsVnicFcIfOwner_Type())
cucsVnicFcIfOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcIfOwner.setStatus(_A)
_CucsVnicFcIfSwitchId_Type=CucsVnicAFcIfSwitchId
_CucsVnicFcIfSwitchId_Object=MibTableColumn
cucsVnicFcIfSwitchId=_CucsVnicFcIfSwitchId_Object((1,3,6,1,4,1,9,9,719,1,53,12,1,8),_CucsVnicFcIfSwitchId_Type())
cucsVnicFcIfSwitchId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcIfSwitchId.setStatus(_A)
_CucsVnicFcIfType_Type=CucsVnicAFcIfType
_CucsVnicFcIfType_Object=MibTableColumn
cucsVnicFcIfType=_CucsVnicFcIfType_Object((1,3,6,1,4,1,9,9,719,1,53,12,1,9),_CucsVnicFcIfType_Type())
cucsVnicFcIfType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcIfType.setStatus(_A)
_CucsVnicFcIfVnet_Type=Gauge32
_CucsVnicFcIfVnet_Object=MibTableColumn
cucsVnicFcIfVnet=_CucsVnicFcIfVnet_Object((1,3,6,1,4,1,9,9,719,1,53,12,1,10),_CucsVnicFcIfVnet_Type())
cucsVnicFcIfVnet.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcIfVnet.setStatus(_A)
_CucsVnicFcIfOperVnetDn_Type=SnmpAdminString
_CucsVnicFcIfOperVnetDn_Object=MibTableColumn
cucsVnicFcIfOperVnetDn=_CucsVnicFcIfOperVnetDn_Object((1,3,6,1,4,1,9,9,719,1,53,12,1,11),_CucsVnicFcIfOperVnetDn_Type())
cucsVnicFcIfOperVnetDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcIfOperVnetDn.setStatus(_A)
_CucsVnicFcIfOperVnetName_Type=SnmpAdminString
_CucsVnicFcIfOperVnetName_Object=MibTableColumn
cucsVnicFcIfOperVnetName=_CucsVnicFcIfOperVnetName_Object((1,3,6,1,4,1,9,9,719,1,53,12,1,12),_CucsVnicFcIfOperVnetName_Type())
cucsVnicFcIfOperVnetName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcIfOperVnetName.setStatus(_A)
_CucsVnicFcIfConfigQualifier_Type=CucsVnicConfigIssues
_CucsVnicFcIfConfigQualifier_Object=MibTableColumn
cucsVnicFcIfConfigQualifier=_CucsVnicFcIfConfigQualifier_Object((1,3,6,1,4,1,9,9,719,1,53,12,1,13),_CucsVnicFcIfConfigQualifier_Type())
cucsVnicFcIfConfigQualifier.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcIfConfigQualifier.setStatus(_A)
_CucsVnicFcIfPubNwId_Type=Gauge32
_CucsVnicFcIfPubNwId_Object=MibTableColumn
cucsVnicFcIfPubNwId=_CucsVnicFcIfPubNwId_Object((1,3,6,1,4,1,9,9,719,1,53,12,1,15),_CucsVnicFcIfPubNwId_Type())
cucsVnicFcIfPubNwId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcIfPubNwId.setStatus(_A)
_CucsVnicFcIfSharing_Type=CucsFabricVlanSharingType
_CucsVnicFcIfSharing_Object=MibTableColumn
cucsVnicFcIfSharing=_CucsVnicFcIfSharing_Object((1,3,6,1,4,1,9,9,719,1,53,12,1,16),_CucsVnicFcIfSharing_Type())
cucsVnicFcIfSharing.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcIfSharing.setStatus(_A)
_CucsVnicFcIfOperPrimaryVnetDn_Type=SnmpAdminString
_CucsVnicFcIfOperPrimaryVnetDn_Object=MibTableColumn
cucsVnicFcIfOperPrimaryVnetDn=_CucsVnicFcIfOperPrimaryVnetDn_Object((1,3,6,1,4,1,9,9,719,1,53,12,1,17),_CucsVnicFcIfOperPrimaryVnetDn_Type())
cucsVnicFcIfOperPrimaryVnetDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcIfOperPrimaryVnetDn.setStatus(_A)
_CucsVnicFcIfOperPrimaryVnetName_Type=SnmpAdminString
_CucsVnicFcIfOperPrimaryVnetName_Object=MibTableColumn
cucsVnicFcIfOperPrimaryVnetName=_CucsVnicFcIfOperPrimaryVnetName_Object((1,3,6,1,4,1,9,9,719,1,53,12,1,18),_CucsVnicFcIfOperPrimaryVnetName_Type())
cucsVnicFcIfOperPrimaryVnetName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcIfOperPrimaryVnetName.setStatus(_A)
_CucsVnicFcLifTable_Object=MibTable
cucsVnicFcLifTable=_CucsVnicFcLifTable_Object((1,3,6,1,4,1,9,9,719,1,53,13))
if mibBuilder.loadTexts:cucsVnicFcLifTable.setStatus(_A)
_CucsVnicFcLifEntry_Object=MibTableRow
cucsVnicFcLifEntry=_CucsVnicFcLifEntry_Object((1,3,6,1,4,1,9,9,719,1,53,13,1))
cucsVnicFcLifEntry.setIndexNames((0,_C,_Q))
if mibBuilder.loadTexts:cucsVnicFcLifEntry.setStatus(_A)
_CucsVnicFcLifInstanceId_Type=CucsManagedObjectId
_CucsVnicFcLifInstanceId_Object=MibTableColumn
cucsVnicFcLifInstanceId=_CucsVnicFcLifInstanceId_Object((1,3,6,1,4,1,9,9,719,1,53,13,1,1),_CucsVnicFcLifInstanceId_Type())
cucsVnicFcLifInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsVnicFcLifInstanceId.setStatus(_A)
_CucsVnicFcLifDn_Type=CucsManagedObjectDn
_CucsVnicFcLifDn_Object=MibTableColumn
cucsVnicFcLifDn=_CucsVnicFcLifDn_Object((1,3,6,1,4,1,9,9,719,1,53,13,1,2),_CucsVnicFcLifDn_Type())
cucsVnicFcLifDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcLifDn.setStatus(_A)
_CucsVnicFcLifRn_Type=SnmpAdminString
_CucsVnicFcLifRn_Object=MibTableColumn
cucsVnicFcLifRn=_CucsVnicFcLifRn_Object((1,3,6,1,4,1,9,9,719,1,53,13,1,3),_CucsVnicFcLifRn_Type())
cucsVnicFcLifRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcLifRn.setStatus(_A)
_CucsVnicFcLifAddr_Type=Unsigned64
_CucsVnicFcLifAddr_Object=MibTableColumn
cucsVnicFcLifAddr=_CucsVnicFcLifAddr_Object((1,3,6,1,4,1,9,9,719,1,53,13,1,4),_CucsVnicFcLifAddr_Type())
cucsVnicFcLifAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcLifAddr.setStatus(_A)
_CucsVnicFcLifName_Type=SnmpAdminString
_CucsVnicFcLifName_Object=MibTableColumn
cucsVnicFcLifName=_CucsVnicFcLifName_Object((1,3,6,1,4,1,9,9,719,1,53,13,1,5),_CucsVnicFcLifName_Type())
cucsVnicFcLifName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcLifName.setStatus(_A)
_CucsVnicFcLifNicDn_Type=SnmpAdminString
_CucsVnicFcLifNicDn_Object=MibTableColumn
cucsVnicFcLifNicDn=_CucsVnicFcLifNicDn_Object((1,3,6,1,4,1,9,9,719,1,53,13,1,6),_CucsVnicFcLifNicDn_Type())
cucsVnicFcLifNicDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcLifNicDn.setStatus(_A)
_CucsVnicFcLifOwner_Type=CucsVnicConnectionOwner
_CucsVnicFcLifOwner_Object=MibTableColumn
cucsVnicFcLifOwner=_CucsVnicFcLifOwner_Object((1,3,6,1,4,1,9,9,719,1,53,13,1,7),_CucsVnicFcLifOwner_Type())
cucsVnicFcLifOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcLifOwner.setStatus(_A)
_CucsVnicFcLifSwitchId_Type=CucsNetworkSwitchId
_CucsVnicFcLifSwitchId_Object=MibTableColumn
cucsVnicFcLifSwitchId=_CucsVnicFcLifSwitchId_Object((1,3,6,1,4,1,9,9,719,1,53,13,1,8),_CucsVnicFcLifSwitchId_Type())
cucsVnicFcLifSwitchId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcLifSwitchId.setStatus(_A)
_CucsVnicFcLifType_Type=CucsVnicConnectionType
_CucsVnicFcLifType_Object=MibTableColumn
cucsVnicFcLifType=_CucsVnicFcLifType_Object((1,3,6,1,4,1,9,9,719,1,53,13,1,9),_CucsVnicFcLifType_Type())
cucsVnicFcLifType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcLifType.setStatus(_A)
_CucsVnicFcLifVnicDn_Type=SnmpAdminString
_CucsVnicFcLifVnicDn_Object=MibTableColumn
cucsVnicFcLifVnicDn=_CucsVnicFcLifVnicDn_Object((1,3,6,1,4,1,9,9,719,1,53,13,1,10),_CucsVnicFcLifVnicDn_Type())
cucsVnicFcLifVnicDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcLifVnicDn.setStatus(_A)
_CucsVnicFcNodeTable_Object=MibTable
cucsVnicFcNodeTable=_CucsVnicFcNodeTable_Object((1,3,6,1,4,1,9,9,719,1,53,14))
if mibBuilder.loadTexts:cucsVnicFcNodeTable.setStatus(_A)
_CucsVnicFcNodeEntry_Object=MibTableRow
cucsVnicFcNodeEntry=_CucsVnicFcNodeEntry_Object((1,3,6,1,4,1,9,9,719,1,53,14,1))
cucsVnicFcNodeEntry.setIndexNames((0,_C,_R))
if mibBuilder.loadTexts:cucsVnicFcNodeEntry.setStatus(_A)
_CucsVnicFcNodeInstanceId_Type=CucsManagedObjectId
_CucsVnicFcNodeInstanceId_Object=MibTableColumn
cucsVnicFcNodeInstanceId=_CucsVnicFcNodeInstanceId_Object((1,3,6,1,4,1,9,9,719,1,53,14,1,1),_CucsVnicFcNodeInstanceId_Type())
cucsVnicFcNodeInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsVnicFcNodeInstanceId.setStatus(_A)
_CucsVnicFcNodeDn_Type=CucsManagedObjectDn
_CucsVnicFcNodeDn_Object=MibTableColumn
cucsVnicFcNodeDn=_CucsVnicFcNodeDn_Object((1,3,6,1,4,1,9,9,719,1,53,14,1,2),_CucsVnicFcNodeDn_Type())
cucsVnicFcNodeDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcNodeDn.setStatus(_A)
_CucsVnicFcNodeRn_Type=SnmpAdminString
_CucsVnicFcNodeRn_Object=MibTableColumn
cucsVnicFcNodeRn=_CucsVnicFcNodeRn_Object((1,3,6,1,4,1,9,9,719,1,53,14,1,3),_CucsVnicFcNodeRn_Type())
cucsVnicFcNodeRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcNodeRn.setStatus(_A)
_CucsVnicFcNodeAddr_Type=Unsigned64
_CucsVnicFcNodeAddr_Object=MibTableColumn
cucsVnicFcNodeAddr=_CucsVnicFcNodeAddr_Object((1,3,6,1,4,1,9,9,719,1,53,14,1,4),_CucsVnicFcNodeAddr_Type())
cucsVnicFcNodeAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcNodeAddr.setStatus(_A)
_CucsVnicFcNodeFltAggr_Type=Unsigned64
_CucsVnicFcNodeFltAggr_Object=MibTableColumn
cucsVnicFcNodeFltAggr=_CucsVnicFcNodeFltAggr_Object((1,3,6,1,4,1,9,9,719,1,53,14,1,5),_CucsVnicFcNodeFltAggr_Type())
cucsVnicFcNodeFltAggr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcNodeFltAggr.setStatus(_A)
_CucsVnicFcNodeIdentPoolName_Type=SnmpAdminString
_CucsVnicFcNodeIdentPoolName_Object=MibTableColumn
cucsVnicFcNodeIdentPoolName=_CucsVnicFcNodeIdentPoolName_Object((1,3,6,1,4,1,9,9,719,1,53,14,1,6),_CucsVnicFcNodeIdentPoolName_Type())
cucsVnicFcNodeIdentPoolName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcNodeIdentPoolName.setStatus(_A)
_CucsVnicFcNodeOperIdentPoolName_Type=SnmpAdminString
_CucsVnicFcNodeOperIdentPoolName_Object=MibTableColumn
cucsVnicFcNodeOperIdentPoolName=_CucsVnicFcNodeOperIdentPoolName_Object((1,3,6,1,4,1,9,9,719,1,53,14,1,7),_CucsVnicFcNodeOperIdentPoolName_Type())
cucsVnicFcNodeOperIdentPoolName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcNodeOperIdentPoolName.setStatus(_A)
_CucsVnicFcNodeMaxDerivableWWPN_Type=Gauge32
_CucsVnicFcNodeMaxDerivableWWPN_Object=MibTableColumn
cucsVnicFcNodeMaxDerivableWWPN=_CucsVnicFcNodeMaxDerivableWWPN_Object((1,3,6,1,4,1,9,9,719,1,53,14,1,8),_CucsVnicFcNodeMaxDerivableWWPN_Type())
cucsVnicFcNodeMaxDerivableWWPN.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcNodeMaxDerivableWWPN.setStatus(_A)
_CucsVnicFcNodeOwner_Type=CucsVnicFcNodeOwner
_CucsVnicFcNodeOwner_Object=MibTableColumn
cucsVnicFcNodeOwner=_CucsVnicFcNodeOwner_Object((1,3,6,1,4,1,9,9,719,1,53,14,1,9),_CucsVnicFcNodeOwner_Type())
cucsVnicFcNodeOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcNodeOwner.setStatus(_A)
_CucsVnicFcOEIfTable_Object=MibTable
cucsVnicFcOEIfTable=_CucsVnicFcOEIfTable_Object((1,3,6,1,4,1,9,9,719,1,53,15))
if mibBuilder.loadTexts:cucsVnicFcOEIfTable.setStatus(_A)
_CucsVnicFcOEIfEntry_Object=MibTableRow
cucsVnicFcOEIfEntry=_CucsVnicFcOEIfEntry_Object((1,3,6,1,4,1,9,9,719,1,53,15,1))
cucsVnicFcOEIfEntry.setIndexNames((0,_C,_S))
if mibBuilder.loadTexts:cucsVnicFcOEIfEntry.setStatus(_A)
_CucsVnicFcOEIfInstanceId_Type=CucsManagedObjectId
_CucsVnicFcOEIfInstanceId_Object=MibTableColumn
cucsVnicFcOEIfInstanceId=_CucsVnicFcOEIfInstanceId_Object((1,3,6,1,4,1,9,9,719,1,53,15,1,1),_CucsVnicFcOEIfInstanceId_Type())
cucsVnicFcOEIfInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsVnicFcOEIfInstanceId.setStatus(_A)
_CucsVnicFcOEIfDn_Type=CucsManagedObjectDn
_CucsVnicFcOEIfDn_Object=MibTableColumn
cucsVnicFcOEIfDn=_CucsVnicFcOEIfDn_Object((1,3,6,1,4,1,9,9,719,1,53,15,1,2),_CucsVnicFcOEIfDn_Type())
cucsVnicFcOEIfDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcOEIfDn.setStatus(_A)
_CucsVnicFcOEIfRn_Type=SnmpAdminString
_CucsVnicFcOEIfRn_Object=MibTableColumn
cucsVnicFcOEIfRn=_CucsVnicFcOEIfRn_Object((1,3,6,1,4,1,9,9,719,1,53,15,1,3),_CucsVnicFcOEIfRn_Type())
cucsVnicFcOEIfRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcOEIfRn.setStatus(_A)
_CucsVnicFcOEIfInitiator_Type=Unsigned64
_CucsVnicFcOEIfInitiator_Object=MibTableColumn
cucsVnicFcOEIfInitiator=_CucsVnicFcOEIfInitiator_Object((1,3,6,1,4,1,9,9,719,1,53,15,1,4),_CucsVnicFcOEIfInitiator_Type())
cucsVnicFcOEIfInitiator.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcOEIfInitiator.setStatus(_A)
_CucsVnicFcOEIfName_Type=SnmpAdminString
_CucsVnicFcOEIfName_Object=MibTableColumn
cucsVnicFcOEIfName=_CucsVnicFcOEIfName_Object((1,3,6,1,4,1,9,9,719,1,53,15,1,5),_CucsVnicFcOEIfName_Type())
cucsVnicFcOEIfName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcOEIfName.setStatus(_A)
_CucsVnicFcOEIfOperState_Type=CucsVnicIfOperState
_CucsVnicFcOEIfOperState_Object=MibTableColumn
cucsVnicFcOEIfOperState=_CucsVnicFcOEIfOperState_Object((1,3,6,1,4,1,9,9,719,1,53,15,1,6),_CucsVnicFcOEIfOperState_Type())
cucsVnicFcOEIfOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcOEIfOperState.setStatus(_A)
_CucsVnicFcOEIfOwner_Type=CucsVnicConnectionOwner
_CucsVnicFcOEIfOwner_Object=MibTableColumn
cucsVnicFcOEIfOwner=_CucsVnicFcOEIfOwner_Object((1,3,6,1,4,1,9,9,719,1,53,15,1,7),_CucsVnicFcOEIfOwner_Type())
cucsVnicFcOEIfOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcOEIfOwner.setStatus(_A)
_CucsVnicFcOEIfSwitchId_Type=CucsVnicAFcIfSwitchId
_CucsVnicFcOEIfSwitchId_Object=MibTableColumn
cucsVnicFcOEIfSwitchId=_CucsVnicFcOEIfSwitchId_Object((1,3,6,1,4,1,9,9,719,1,53,15,1,8),_CucsVnicFcOEIfSwitchId_Type())
cucsVnicFcOEIfSwitchId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcOEIfSwitchId.setStatus(_A)
_CucsVnicFcOEIfType_Type=CucsVnicAFcIfType
_CucsVnicFcOEIfType_Object=MibTableColumn
cucsVnicFcOEIfType=_CucsVnicFcOEIfType_Object((1,3,6,1,4,1,9,9,719,1,53,15,1,9),_CucsVnicFcOEIfType_Type())
cucsVnicFcOEIfType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcOEIfType.setStatus(_A)
_CucsVnicFcOEIfVnet_Type=Gauge32
_CucsVnicFcOEIfVnet_Object=MibTableColumn
cucsVnicFcOEIfVnet=_CucsVnicFcOEIfVnet_Object((1,3,6,1,4,1,9,9,719,1,53,15,1,10),_CucsVnicFcOEIfVnet_Type())
cucsVnicFcOEIfVnet.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcOEIfVnet.setStatus(_A)
_CucsVnicFcOEIfConfigQualifier_Type=CucsVnicConfigIssues
_CucsVnicFcOEIfConfigQualifier_Object=MibTableColumn
cucsVnicFcOEIfConfigQualifier=_CucsVnicFcOEIfConfigQualifier_Object((1,3,6,1,4,1,9,9,719,1,53,15,1,11),_CucsVnicFcOEIfConfigQualifier_Type())
cucsVnicFcOEIfConfigQualifier.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcOEIfConfigQualifier.setStatus(_A)
_CucsVnicFcOEIfOperVnetDn_Type=SnmpAdminString
_CucsVnicFcOEIfOperVnetDn_Object=MibTableColumn
cucsVnicFcOEIfOperVnetDn=_CucsVnicFcOEIfOperVnetDn_Object((1,3,6,1,4,1,9,9,719,1,53,15,1,13),_CucsVnicFcOEIfOperVnetDn_Type())
cucsVnicFcOEIfOperVnetDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcOEIfOperVnetDn.setStatus(_A)
_CucsVnicFcOEIfOperVnetName_Type=SnmpAdminString
_CucsVnicFcOEIfOperVnetName_Object=MibTableColumn
cucsVnicFcOEIfOperVnetName=_CucsVnicFcOEIfOperVnetName_Object((1,3,6,1,4,1,9,9,719,1,53,15,1,14),_CucsVnicFcOEIfOperVnetName_Type())
cucsVnicFcOEIfOperVnetName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcOEIfOperVnetName.setStatus(_A)
_CucsVnicFcOEIfPubNwId_Type=Gauge32
_CucsVnicFcOEIfPubNwId_Object=MibTableColumn
cucsVnicFcOEIfPubNwId=_CucsVnicFcOEIfPubNwId_Object((1,3,6,1,4,1,9,9,719,1,53,15,1,15),_CucsVnicFcOEIfPubNwId_Type())
cucsVnicFcOEIfPubNwId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcOEIfPubNwId.setStatus(_A)
_CucsVnicFcOEIfSharing_Type=CucsFabricVlanSharingType
_CucsVnicFcOEIfSharing_Object=MibTableColumn
cucsVnicFcOEIfSharing=_CucsVnicFcOEIfSharing_Object((1,3,6,1,4,1,9,9,719,1,53,15,1,16),_CucsVnicFcOEIfSharing_Type())
cucsVnicFcOEIfSharing.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcOEIfSharing.setStatus(_A)
_CucsVnicFcOEIfOperPrimaryVnetDn_Type=SnmpAdminString
_CucsVnicFcOEIfOperPrimaryVnetDn_Object=MibTableColumn
cucsVnicFcOEIfOperPrimaryVnetDn=_CucsVnicFcOEIfOperPrimaryVnetDn_Object((1,3,6,1,4,1,9,9,719,1,53,15,1,17),_CucsVnicFcOEIfOperPrimaryVnetDn_Type())
cucsVnicFcOEIfOperPrimaryVnetDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcOEIfOperPrimaryVnetDn.setStatus(_A)
_CucsVnicFcOEIfOperPrimaryVnetName_Type=SnmpAdminString
_CucsVnicFcOEIfOperPrimaryVnetName_Object=MibTableColumn
cucsVnicFcOEIfOperPrimaryVnetName=_CucsVnicFcOEIfOperPrimaryVnetName_Object((1,3,6,1,4,1,9,9,719,1,53,15,1,18),_CucsVnicFcOEIfOperPrimaryVnetName_Type())
cucsVnicFcOEIfOperPrimaryVnetName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcOEIfOperPrimaryVnetName.setStatus(_A)
_CucsVnicIPv4DhcpTable_Object=MibTable
cucsVnicIPv4DhcpTable=_CucsVnicIPv4DhcpTable_Object((1,3,6,1,4,1,9,9,719,1,53,16))
if mibBuilder.loadTexts:cucsVnicIPv4DhcpTable.setStatus(_A)
_CucsVnicIPv4DhcpEntry_Object=MibTableRow
cucsVnicIPv4DhcpEntry=_CucsVnicIPv4DhcpEntry_Object((1,3,6,1,4,1,9,9,719,1,53,16,1))
cucsVnicIPv4DhcpEntry.setIndexNames((0,_C,_T))
if mibBuilder.loadTexts:cucsVnicIPv4DhcpEntry.setStatus(_A)
_CucsVnicIPv4DhcpInstanceId_Type=CucsManagedObjectId
_CucsVnicIPv4DhcpInstanceId_Object=MibTableColumn
cucsVnicIPv4DhcpInstanceId=_CucsVnicIPv4DhcpInstanceId_Object((1,3,6,1,4,1,9,9,719,1,53,16,1,1),_CucsVnicIPv4DhcpInstanceId_Type())
cucsVnicIPv4DhcpInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsVnicIPv4DhcpInstanceId.setStatus(_A)
_CucsVnicIPv4DhcpDn_Type=CucsManagedObjectDn
_CucsVnicIPv4DhcpDn_Object=MibTableColumn
cucsVnicIPv4DhcpDn=_CucsVnicIPv4DhcpDn_Object((1,3,6,1,4,1,9,9,719,1,53,16,1,2),_CucsVnicIPv4DhcpDn_Type())
cucsVnicIPv4DhcpDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIPv4DhcpDn.setStatus(_A)
_CucsVnicIPv4DhcpRn_Type=SnmpAdminString
_CucsVnicIPv4DhcpRn_Object=MibTableColumn
cucsVnicIPv4DhcpRn=_CucsVnicIPv4DhcpRn_Object((1,3,6,1,4,1,9,9,719,1,53,16,1,3),_CucsVnicIPv4DhcpRn_Type())
cucsVnicIPv4DhcpRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIPv4DhcpRn.setStatus(_A)
_CucsVnicIPv4DhcpAddr_Type=InetAddressIPv4
_CucsVnicIPv4DhcpAddr_Object=MibTableColumn
cucsVnicIPv4DhcpAddr=_CucsVnicIPv4DhcpAddr_Object((1,3,6,1,4,1,9,9,719,1,53,16,1,4),_CucsVnicIPv4DhcpAddr_Type())
cucsVnicIPv4DhcpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIPv4DhcpAddr.setStatus(_A)
_CucsVnicIPv4DhcpDefGw_Type=InetAddressIPv4
_CucsVnicIPv4DhcpDefGw_Object=MibTableColumn
cucsVnicIPv4DhcpDefGw=_CucsVnicIPv4DhcpDefGw_Object((1,3,6,1,4,1,9,9,719,1,53,16,1,5),_CucsVnicIPv4DhcpDefGw_Type())
cucsVnicIPv4DhcpDefGw.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIPv4DhcpDefGw.setStatus(_A)
_CucsVnicIPv4DhcpSubnet_Type=InetAddressIPv4
_CucsVnicIPv4DhcpSubnet_Object=MibTableColumn
cucsVnicIPv4DhcpSubnet=_CucsVnicIPv4DhcpSubnet_Object((1,3,6,1,4,1,9,9,719,1,53,16,1,6),_CucsVnicIPv4DhcpSubnet_Type())
cucsVnicIPv4DhcpSubnet.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIPv4DhcpSubnet.setStatus(_A)
_CucsVnicIPv4DnsTable_Object=MibTable
cucsVnicIPv4DnsTable=_CucsVnicIPv4DnsTable_Object((1,3,6,1,4,1,9,9,719,1,53,17))
if mibBuilder.loadTexts:cucsVnicIPv4DnsTable.setStatus(_A)
_CucsVnicIPv4DnsEntry_Object=MibTableRow
cucsVnicIPv4DnsEntry=_CucsVnicIPv4DnsEntry_Object((1,3,6,1,4,1,9,9,719,1,53,17,1))
cucsVnicIPv4DnsEntry.setIndexNames((0,_C,_U))
if mibBuilder.loadTexts:cucsVnicIPv4DnsEntry.setStatus(_A)
_CucsVnicIPv4DnsInstanceId_Type=CucsManagedObjectId
_CucsVnicIPv4DnsInstanceId_Object=MibTableColumn
cucsVnicIPv4DnsInstanceId=_CucsVnicIPv4DnsInstanceId_Object((1,3,6,1,4,1,9,9,719,1,53,17,1,1),_CucsVnicIPv4DnsInstanceId_Type())
cucsVnicIPv4DnsInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsVnicIPv4DnsInstanceId.setStatus(_A)
_CucsVnicIPv4DnsDn_Type=CucsManagedObjectDn
_CucsVnicIPv4DnsDn_Object=MibTableColumn
cucsVnicIPv4DnsDn=_CucsVnicIPv4DnsDn_Object((1,3,6,1,4,1,9,9,719,1,53,17,1,2),_CucsVnicIPv4DnsDn_Type())
cucsVnicIPv4DnsDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIPv4DnsDn.setStatus(_A)
_CucsVnicIPv4DnsRn_Type=SnmpAdminString
_CucsVnicIPv4DnsRn_Object=MibTableColumn
cucsVnicIPv4DnsRn=_CucsVnicIPv4DnsRn_Object((1,3,6,1,4,1,9,9,719,1,53,17,1,3),_CucsVnicIPv4DnsRn_Type())
cucsVnicIPv4DnsRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIPv4DnsRn.setStatus(_A)
_CucsVnicIPv4DnsAddr_Type=InetAddressIPv4
_CucsVnicIPv4DnsAddr_Object=MibTableColumn
cucsVnicIPv4DnsAddr=_CucsVnicIPv4DnsAddr_Object((1,3,6,1,4,1,9,9,719,1,53,17,1,4),_CucsVnicIPv4DnsAddr_Type())
cucsVnicIPv4DnsAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIPv4DnsAddr.setStatus(_A)
_CucsVnicIPv4DnsDefGw_Type=InetAddressIPv4
_CucsVnicIPv4DnsDefGw_Object=MibTableColumn
cucsVnicIPv4DnsDefGw=_CucsVnicIPv4DnsDefGw_Object((1,3,6,1,4,1,9,9,719,1,53,17,1,5),_CucsVnicIPv4DnsDefGw_Type())
cucsVnicIPv4DnsDefGw.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIPv4DnsDefGw.setStatus(_A)
_CucsVnicIPv4DnsPref_Type=CucsVnicIPv4DnsPref
_CucsVnicIPv4DnsPref_Object=MibTableColumn
cucsVnicIPv4DnsPref=_CucsVnicIPv4DnsPref_Object((1,3,6,1,4,1,9,9,719,1,53,17,1,6),_CucsVnicIPv4DnsPref_Type())
cucsVnicIPv4DnsPref.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIPv4DnsPref.setStatus(_A)
_CucsVnicIPv4DnsSubnet_Type=InetAddressIPv4
_CucsVnicIPv4DnsSubnet_Object=MibTableColumn
cucsVnicIPv4DnsSubnet=_CucsVnicIPv4DnsSubnet_Object((1,3,6,1,4,1,9,9,719,1,53,17,1,7),_CucsVnicIPv4DnsSubnet_Type())
cucsVnicIPv4DnsSubnet.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIPv4DnsSubnet.setStatus(_A)
_CucsVnicIPv4IfTable_Object=MibTable
cucsVnicIPv4IfTable=_CucsVnicIPv4IfTable_Object((1,3,6,1,4,1,9,9,719,1,53,18))
if mibBuilder.loadTexts:cucsVnicIPv4IfTable.setStatus(_A)
_CucsVnicIPv4IfEntry_Object=MibTableRow
cucsVnicIPv4IfEntry=_CucsVnicIPv4IfEntry_Object((1,3,6,1,4,1,9,9,719,1,53,18,1))
cucsVnicIPv4IfEntry.setIndexNames((0,_C,_V))
if mibBuilder.loadTexts:cucsVnicIPv4IfEntry.setStatus(_A)
_CucsVnicIPv4IfInstanceId_Type=CucsManagedObjectId
_CucsVnicIPv4IfInstanceId_Object=MibTableColumn
cucsVnicIPv4IfInstanceId=_CucsVnicIPv4IfInstanceId_Object((1,3,6,1,4,1,9,9,719,1,53,18,1,1),_CucsVnicIPv4IfInstanceId_Type())
cucsVnicIPv4IfInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsVnicIPv4IfInstanceId.setStatus(_A)
_CucsVnicIPv4IfDn_Type=CucsManagedObjectDn
_CucsVnicIPv4IfDn_Object=MibTableColumn
cucsVnicIPv4IfDn=_CucsVnicIPv4IfDn_Object((1,3,6,1,4,1,9,9,719,1,53,18,1,2),_CucsVnicIPv4IfDn_Type())
cucsVnicIPv4IfDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIPv4IfDn.setStatus(_A)
_CucsVnicIPv4IfRn_Type=SnmpAdminString
_CucsVnicIPv4IfRn_Object=MibTableColumn
cucsVnicIPv4IfRn=_CucsVnicIPv4IfRn_Object((1,3,6,1,4,1,9,9,719,1,53,18,1,3),_CucsVnicIPv4IfRn_Type())
cucsVnicIPv4IfRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIPv4IfRn.setStatus(_A)
_CucsVnicIPv4IfAddr_Type=InetAddressIPv4
_CucsVnicIPv4IfAddr_Object=MibTableColumn
cucsVnicIPv4IfAddr=_CucsVnicIPv4IfAddr_Object((1,3,6,1,4,1,9,9,719,1,53,18,1,4),_CucsVnicIPv4IfAddr_Type())
cucsVnicIPv4IfAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIPv4IfAddr.setStatus(_A)
_CucsVnicIPv4IfName_Type=SnmpAdminString
_CucsVnicIPv4IfName_Object=MibTableColumn
cucsVnicIPv4IfName=_CucsVnicIPv4IfName_Object((1,3,6,1,4,1,9,9,719,1,53,18,1,5),_CucsVnicIPv4IfName_Type())
cucsVnicIPv4IfName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIPv4IfName.setStatus(_A)
_CucsVnicIPv4IfOperState_Type=CucsVnicIfOperState
_CucsVnicIPv4IfOperState_Object=MibTableColumn
cucsVnicIPv4IfOperState=_CucsVnicIPv4IfOperState_Object((1,3,6,1,4,1,9,9,719,1,53,18,1,6),_CucsVnicIPv4IfOperState_Type())
cucsVnicIPv4IfOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIPv4IfOperState.setStatus(_A)
_CucsVnicIPv4IfOwner_Type=CucsVnicConnectionOwner
_CucsVnicIPv4IfOwner_Object=MibTableColumn
cucsVnicIPv4IfOwner=_CucsVnicIPv4IfOwner_Object((1,3,6,1,4,1,9,9,719,1,53,18,1,7),_CucsVnicIPv4IfOwner_Type())
cucsVnicIPv4IfOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIPv4IfOwner.setStatus(_A)
_CucsVnicIPv4IfSwitchId_Type=CucsNetworkSwitchId
_CucsVnicIPv4IfSwitchId_Object=MibTableColumn
cucsVnicIPv4IfSwitchId=_CucsVnicIPv4IfSwitchId_Object((1,3,6,1,4,1,9,9,719,1,53,18,1,8),_CucsVnicIPv4IfSwitchId_Type())
cucsVnicIPv4IfSwitchId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIPv4IfSwitchId.setStatus(_A)
_CucsVnicIPv4IfType_Type=CucsVnicConnectionType
_CucsVnicIPv4IfType_Object=MibTableColumn
cucsVnicIPv4IfType=_CucsVnicIPv4IfType_Object((1,3,6,1,4,1,9,9,719,1,53,18,1,9),_CucsVnicIPv4IfType_Type())
cucsVnicIPv4IfType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIPv4IfType.setStatus(_A)
_CucsVnicIPv4IfVnet_Type=Gauge32
_CucsVnicIPv4IfVnet_Object=MibTableColumn
cucsVnicIPv4IfVnet=_CucsVnicIPv4IfVnet_Object((1,3,6,1,4,1,9,9,719,1,53,18,1,10),_CucsVnicIPv4IfVnet_Type())
cucsVnicIPv4IfVnet.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIPv4IfVnet.setStatus(_A)
_CucsVnicIPv4IfConfigQualifier_Type=CucsVnicConfigIssues
_CucsVnicIPv4IfConfigQualifier_Object=MibTableColumn
cucsVnicIPv4IfConfigQualifier=_CucsVnicIPv4IfConfigQualifier_Object((1,3,6,1,4,1,9,9,719,1,53,18,1,11),_CucsVnicIPv4IfConfigQualifier_Type())
cucsVnicIPv4IfConfigQualifier.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIPv4IfConfigQualifier.setStatus(_A)
_CucsVnicIPv4IfOperVnetDn_Type=SnmpAdminString
_CucsVnicIPv4IfOperVnetDn_Object=MibTableColumn
cucsVnicIPv4IfOperVnetDn=_CucsVnicIPv4IfOperVnetDn_Object((1,3,6,1,4,1,9,9,719,1,53,18,1,13),_CucsVnicIPv4IfOperVnetDn_Type())
cucsVnicIPv4IfOperVnetDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIPv4IfOperVnetDn.setStatus(_A)
_CucsVnicIPv4IfOperVnetName_Type=SnmpAdminString
_CucsVnicIPv4IfOperVnetName_Object=MibTableColumn
cucsVnicIPv4IfOperVnetName=_CucsVnicIPv4IfOperVnetName_Object((1,3,6,1,4,1,9,9,719,1,53,18,1,14),_CucsVnicIPv4IfOperVnetName_Type())
cucsVnicIPv4IfOperVnetName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIPv4IfOperVnetName.setStatus(_A)
_CucsVnicIPv4IfPubNwId_Type=Gauge32
_CucsVnicIPv4IfPubNwId_Object=MibTableColumn
cucsVnicIPv4IfPubNwId=_CucsVnicIPv4IfPubNwId_Object((1,3,6,1,4,1,9,9,719,1,53,18,1,15),_CucsVnicIPv4IfPubNwId_Type())
cucsVnicIPv4IfPubNwId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIPv4IfPubNwId.setStatus(_A)
_CucsVnicIPv4IfSharing_Type=CucsFabricVlanSharingType
_CucsVnicIPv4IfSharing_Object=MibTableColumn
cucsVnicIPv4IfSharing=_CucsVnicIPv4IfSharing_Object((1,3,6,1,4,1,9,9,719,1,53,18,1,16),_CucsVnicIPv4IfSharing_Type())
cucsVnicIPv4IfSharing.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIPv4IfSharing.setStatus(_A)
_CucsVnicIPv4IfPropAcl_Type=Unsigned64
_CucsVnicIPv4IfPropAcl_Object=MibTableColumn
cucsVnicIPv4IfPropAcl=_CucsVnicIPv4IfPropAcl_Object((1,3,6,1,4,1,9,9,719,1,53,18,1,17),_CucsVnicIPv4IfPropAcl_Type())
cucsVnicIPv4IfPropAcl.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIPv4IfPropAcl.setStatus(_A)
_CucsVnicIPv4IfOperPrimaryVnetDn_Type=SnmpAdminString
_CucsVnicIPv4IfOperPrimaryVnetDn_Object=MibTableColumn
cucsVnicIPv4IfOperPrimaryVnetDn=_CucsVnicIPv4IfOperPrimaryVnetDn_Object((1,3,6,1,4,1,9,9,719,1,53,18,1,18),_CucsVnicIPv4IfOperPrimaryVnetDn_Type())
cucsVnicIPv4IfOperPrimaryVnetDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIPv4IfOperPrimaryVnetDn.setStatus(_A)
_CucsVnicIPv4IfOperPrimaryVnetName_Type=SnmpAdminString
_CucsVnicIPv4IfOperPrimaryVnetName_Object=MibTableColumn
cucsVnicIPv4IfOperPrimaryVnetName=_CucsVnicIPv4IfOperPrimaryVnetName_Object((1,3,6,1,4,1,9,9,719,1,53,18,1,19),_CucsVnicIPv4IfOperPrimaryVnetName_Type())
cucsVnicIPv4IfOperPrimaryVnetName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIPv4IfOperPrimaryVnetName.setStatus(_A)
_CucsVnicIPv4StaticRouteTable_Object=MibTable
cucsVnicIPv4StaticRouteTable=_CucsVnicIPv4StaticRouteTable_Object((1,3,6,1,4,1,9,9,719,1,53,19))
if mibBuilder.loadTexts:cucsVnicIPv4StaticRouteTable.setStatus(_A)
_CucsVnicIPv4StaticRouteEntry_Object=MibTableRow
cucsVnicIPv4StaticRouteEntry=_CucsVnicIPv4StaticRouteEntry_Object((1,3,6,1,4,1,9,9,719,1,53,19,1))
cucsVnicIPv4StaticRouteEntry.setIndexNames((0,_C,_W))
if mibBuilder.loadTexts:cucsVnicIPv4StaticRouteEntry.setStatus(_A)
_CucsVnicIPv4StaticRouteInstanceId_Type=CucsManagedObjectId
_CucsVnicIPv4StaticRouteInstanceId_Object=MibTableColumn
cucsVnicIPv4StaticRouteInstanceId=_CucsVnicIPv4StaticRouteInstanceId_Object((1,3,6,1,4,1,9,9,719,1,53,19,1,1),_CucsVnicIPv4StaticRouteInstanceId_Type())
cucsVnicIPv4StaticRouteInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsVnicIPv4StaticRouteInstanceId.setStatus(_A)
_CucsVnicIPv4StaticRouteDn_Type=CucsManagedObjectDn
_CucsVnicIPv4StaticRouteDn_Object=MibTableColumn
cucsVnicIPv4StaticRouteDn=_CucsVnicIPv4StaticRouteDn_Object((1,3,6,1,4,1,9,9,719,1,53,19,1,2),_CucsVnicIPv4StaticRouteDn_Type())
cucsVnicIPv4StaticRouteDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIPv4StaticRouteDn.setStatus(_A)
_CucsVnicIPv4StaticRouteRn_Type=SnmpAdminString
_CucsVnicIPv4StaticRouteRn_Object=MibTableColumn
cucsVnicIPv4StaticRouteRn=_CucsVnicIPv4StaticRouteRn_Object((1,3,6,1,4,1,9,9,719,1,53,19,1,3),_CucsVnicIPv4StaticRouteRn_Type())
cucsVnicIPv4StaticRouteRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIPv4StaticRouteRn.setStatus(_A)
_CucsVnicIPv4StaticRouteAddr_Type=InetAddressIPv4
_CucsVnicIPv4StaticRouteAddr_Object=MibTableColumn
cucsVnicIPv4StaticRouteAddr=_CucsVnicIPv4StaticRouteAddr_Object((1,3,6,1,4,1,9,9,719,1,53,19,1,4),_CucsVnicIPv4StaticRouteAddr_Type())
cucsVnicIPv4StaticRouteAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIPv4StaticRouteAddr.setStatus(_A)
_CucsVnicIPv4StaticRouteDefGw_Type=InetAddressIPv4
_CucsVnicIPv4StaticRouteDefGw_Object=MibTableColumn
cucsVnicIPv4StaticRouteDefGw=_CucsVnicIPv4StaticRouteDefGw_Object((1,3,6,1,4,1,9,9,719,1,53,19,1,5),_CucsVnicIPv4StaticRouteDefGw_Type())
cucsVnicIPv4StaticRouteDefGw.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIPv4StaticRouteDefGw.setStatus(_A)
_CucsVnicIPv4StaticRouteGwAddr_Type=InetAddressIPv4
_CucsVnicIPv4StaticRouteGwAddr_Object=MibTableColumn
cucsVnicIPv4StaticRouteGwAddr=_CucsVnicIPv4StaticRouteGwAddr_Object((1,3,6,1,4,1,9,9,719,1,53,19,1,6),_CucsVnicIPv4StaticRouteGwAddr_Type())
cucsVnicIPv4StaticRouteGwAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIPv4StaticRouteGwAddr.setStatus(_A)
_CucsVnicIPv4StaticRouteGwSubnet_Type=InetAddressIPv4
_CucsVnicIPv4StaticRouteGwSubnet_Object=MibTableColumn
cucsVnicIPv4StaticRouteGwSubnet=_CucsVnicIPv4StaticRouteGwSubnet_Object((1,3,6,1,4,1,9,9,719,1,53,19,1,7),_CucsVnicIPv4StaticRouteGwSubnet_Type())
cucsVnicIPv4StaticRouteGwSubnet.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIPv4StaticRouteGwSubnet.setStatus(_A)
_CucsVnicIPv4StaticRouteSubnet_Type=InetAddressIPv4
_CucsVnicIPv4StaticRouteSubnet_Object=MibTableColumn
cucsVnicIPv4StaticRouteSubnet=_CucsVnicIPv4StaticRouteSubnet_Object((1,3,6,1,4,1,9,9,719,1,53,19,1,8),_CucsVnicIPv4StaticRouteSubnet_Type())
cucsVnicIPv4StaticRouteSubnet.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIPv4StaticRouteSubnet.setStatus(_A)
_CucsVnicIpV4PooledAddrTable_Object=MibTable
cucsVnicIpV4PooledAddrTable=_CucsVnicIpV4PooledAddrTable_Object((1,3,6,1,4,1,9,9,719,1,53,20))
if mibBuilder.loadTexts:cucsVnicIpV4PooledAddrTable.setStatus(_A)
_CucsVnicIpV4PooledAddrEntry_Object=MibTableRow
cucsVnicIpV4PooledAddrEntry=_CucsVnicIpV4PooledAddrEntry_Object((1,3,6,1,4,1,9,9,719,1,53,20,1))
cucsVnicIpV4PooledAddrEntry.setIndexNames((0,_C,_X))
if mibBuilder.loadTexts:cucsVnicIpV4PooledAddrEntry.setStatus(_A)
_CucsVnicIpV4PooledAddrInstanceId_Type=CucsManagedObjectId
_CucsVnicIpV4PooledAddrInstanceId_Object=MibTableColumn
cucsVnicIpV4PooledAddrInstanceId=_CucsVnicIpV4PooledAddrInstanceId_Object((1,3,6,1,4,1,9,9,719,1,53,20,1,1),_CucsVnicIpV4PooledAddrInstanceId_Type())
cucsVnicIpV4PooledAddrInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsVnicIpV4PooledAddrInstanceId.setStatus(_A)
_CucsVnicIpV4PooledAddrDn_Type=CucsManagedObjectDn
_CucsVnicIpV4PooledAddrDn_Object=MibTableColumn
cucsVnicIpV4PooledAddrDn=_CucsVnicIpV4PooledAddrDn_Object((1,3,6,1,4,1,9,9,719,1,53,20,1,2),_CucsVnicIpV4PooledAddrDn_Type())
cucsVnicIpV4PooledAddrDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIpV4PooledAddrDn.setStatus(_A)
_CucsVnicIpV4PooledAddrRn_Type=SnmpAdminString
_CucsVnicIpV4PooledAddrRn_Object=MibTableColumn
cucsVnicIpV4PooledAddrRn=_CucsVnicIpV4PooledAddrRn_Object((1,3,6,1,4,1,9,9,719,1,53,20,1,3),_CucsVnicIpV4PooledAddrRn_Type())
cucsVnicIpV4PooledAddrRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIpV4PooledAddrRn.setStatus(_A)
_CucsVnicIpV4PooledAddrAddr_Type=InetAddressIPv4
_CucsVnicIpV4PooledAddrAddr_Object=MibTableColumn
cucsVnicIpV4PooledAddrAddr=_CucsVnicIpV4PooledAddrAddr_Object((1,3,6,1,4,1,9,9,719,1,53,20,1,4),_CucsVnicIpV4PooledAddrAddr_Type())
cucsVnicIpV4PooledAddrAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIpV4PooledAddrAddr.setStatus(_A)
_CucsVnicIpV4PooledAddrDefGw_Type=InetAddressIPv4
_CucsVnicIpV4PooledAddrDefGw_Object=MibTableColumn
cucsVnicIpV4PooledAddrDefGw=_CucsVnicIpV4PooledAddrDefGw_Object((1,3,6,1,4,1,9,9,719,1,53,20,1,5),_CucsVnicIpV4PooledAddrDefGw_Type())
cucsVnicIpV4PooledAddrDefGw.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIpV4PooledAddrDefGw.setStatus(_A)
_CucsVnicIpV4PooledAddrName_Type=SnmpAdminString
_CucsVnicIpV4PooledAddrName_Object=MibTableColumn
cucsVnicIpV4PooledAddrName=_CucsVnicIpV4PooledAddrName_Object((1,3,6,1,4,1,9,9,719,1,53,20,1,6),_CucsVnicIpV4PooledAddrName_Type())
cucsVnicIpV4PooledAddrName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIpV4PooledAddrName.setStatus(_A)
_CucsVnicIpV4PooledAddrSubnet_Type=InetAddressIPv4
_CucsVnicIpV4PooledAddrSubnet_Object=MibTableColumn
cucsVnicIpV4PooledAddrSubnet=_CucsVnicIpV4PooledAddrSubnet_Object((1,3,6,1,4,1,9,9,719,1,53,20,1,7),_CucsVnicIpV4PooledAddrSubnet_Type())
cucsVnicIpV4PooledAddrSubnet.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIpV4PooledAddrSubnet.setStatus(_A)
_CucsVnicIpV4PooledAddrOperName_Type=SnmpAdminString
_CucsVnicIpV4PooledAddrOperName_Object=MibTableColumn
cucsVnicIpV4PooledAddrOperName=_CucsVnicIpV4PooledAddrOperName_Object((1,3,6,1,4,1,9,9,719,1,53,20,1,8),_CucsVnicIpV4PooledAddrOperName_Type())
cucsVnicIpV4PooledAddrOperName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIpV4PooledAddrOperName.setStatus(_A)
_CucsVnicIpV4PooledAddrPrimDns_Type=InetAddressIPv4
_CucsVnicIpV4PooledAddrPrimDns_Object=MibTableColumn
cucsVnicIpV4PooledAddrPrimDns=_CucsVnicIpV4PooledAddrPrimDns_Object((1,3,6,1,4,1,9,9,719,1,53,20,1,9),_CucsVnicIpV4PooledAddrPrimDns_Type())
cucsVnicIpV4PooledAddrPrimDns.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIpV4PooledAddrPrimDns.setStatus(_A)
_CucsVnicIpV4PooledAddrSecDns_Type=InetAddressIPv4
_CucsVnicIpV4PooledAddrSecDns_Object=MibTableColumn
cucsVnicIpV4PooledAddrSecDns=_CucsVnicIpV4PooledAddrSecDns_Object((1,3,6,1,4,1,9,9,719,1,53,20,1,10),_CucsVnicIpV4PooledAddrSecDns_Type())
cucsVnicIpV4PooledAddrSecDns.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIpV4PooledAddrSecDns.setStatus(_A)
_CucsVnicIpV4ProfDerivedAddrTable_Object=MibTable
cucsVnicIpV4ProfDerivedAddrTable=_CucsVnicIpV4ProfDerivedAddrTable_Object((1,3,6,1,4,1,9,9,719,1,53,21))
if mibBuilder.loadTexts:cucsVnicIpV4ProfDerivedAddrTable.setStatus(_A)
_CucsVnicIpV4ProfDerivedAddrEntry_Object=MibTableRow
cucsVnicIpV4ProfDerivedAddrEntry=_CucsVnicIpV4ProfDerivedAddrEntry_Object((1,3,6,1,4,1,9,9,719,1,53,21,1))
cucsVnicIpV4ProfDerivedAddrEntry.setIndexNames((0,_C,_Y))
if mibBuilder.loadTexts:cucsVnicIpV4ProfDerivedAddrEntry.setStatus(_A)
_CucsVnicIpV4ProfDerivedAddrInstanceId_Type=CucsManagedObjectId
_CucsVnicIpV4ProfDerivedAddrInstanceId_Object=MibTableColumn
cucsVnicIpV4ProfDerivedAddrInstanceId=_CucsVnicIpV4ProfDerivedAddrInstanceId_Object((1,3,6,1,4,1,9,9,719,1,53,21,1,1),_CucsVnicIpV4ProfDerivedAddrInstanceId_Type())
cucsVnicIpV4ProfDerivedAddrInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsVnicIpV4ProfDerivedAddrInstanceId.setStatus(_A)
_CucsVnicIpV4ProfDerivedAddrDn_Type=CucsManagedObjectDn
_CucsVnicIpV4ProfDerivedAddrDn_Object=MibTableColumn
cucsVnicIpV4ProfDerivedAddrDn=_CucsVnicIpV4ProfDerivedAddrDn_Object((1,3,6,1,4,1,9,9,719,1,53,21,1,2),_CucsVnicIpV4ProfDerivedAddrDn_Type())
cucsVnicIpV4ProfDerivedAddrDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIpV4ProfDerivedAddrDn.setStatus(_A)
_CucsVnicIpV4ProfDerivedAddrRn_Type=SnmpAdminString
_CucsVnicIpV4ProfDerivedAddrRn_Object=MibTableColumn
cucsVnicIpV4ProfDerivedAddrRn=_CucsVnicIpV4ProfDerivedAddrRn_Object((1,3,6,1,4,1,9,9,719,1,53,21,1,3),_CucsVnicIpV4ProfDerivedAddrRn_Type())
cucsVnicIpV4ProfDerivedAddrRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIpV4ProfDerivedAddrRn.setStatus(_A)
_CucsVnicIpV4ProfDerivedAddrAddr_Type=InetAddressIPv4
_CucsVnicIpV4ProfDerivedAddrAddr_Object=MibTableColumn
cucsVnicIpV4ProfDerivedAddrAddr=_CucsVnicIpV4ProfDerivedAddrAddr_Object((1,3,6,1,4,1,9,9,719,1,53,21,1,4),_CucsVnicIpV4ProfDerivedAddrAddr_Type())
cucsVnicIpV4ProfDerivedAddrAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIpV4ProfDerivedAddrAddr.setStatus(_A)
_CucsVnicIpV4ProfDerivedAddrDefGw_Type=InetAddressIPv4
_CucsVnicIpV4ProfDerivedAddrDefGw_Object=MibTableColumn
cucsVnicIpV4ProfDerivedAddrDefGw=_CucsVnicIpV4ProfDerivedAddrDefGw_Object((1,3,6,1,4,1,9,9,719,1,53,21,1,5),_CucsVnicIpV4ProfDerivedAddrDefGw_Type())
cucsVnicIpV4ProfDerivedAddrDefGw.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIpV4ProfDerivedAddrDefGw.setStatus(_A)
_CucsVnicIpV4ProfDerivedAddrSubnet_Type=InetAddressIPv4
_CucsVnicIpV4ProfDerivedAddrSubnet_Object=MibTableColumn
cucsVnicIpV4ProfDerivedAddrSubnet=_CucsVnicIpV4ProfDerivedAddrSubnet_Object((1,3,6,1,4,1,9,9,719,1,53,21,1,6),_CucsVnicIpV4ProfDerivedAddrSubnet_Type())
cucsVnicIpV4ProfDerivedAddrSubnet.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIpV4ProfDerivedAddrSubnet.setStatus(_A)
_CucsVnicIpV4StaticAddrTable_Object=MibTable
cucsVnicIpV4StaticAddrTable=_CucsVnicIpV4StaticAddrTable_Object((1,3,6,1,4,1,9,9,719,1,53,22))
if mibBuilder.loadTexts:cucsVnicIpV4StaticAddrTable.setStatus(_A)
_CucsVnicIpV4StaticAddrEntry_Object=MibTableRow
cucsVnicIpV4StaticAddrEntry=_CucsVnicIpV4StaticAddrEntry_Object((1,3,6,1,4,1,9,9,719,1,53,22,1))
cucsVnicIpV4StaticAddrEntry.setIndexNames((0,_C,_Z))
if mibBuilder.loadTexts:cucsVnicIpV4StaticAddrEntry.setStatus(_A)
_CucsVnicIpV4StaticAddrInstanceId_Type=CucsManagedObjectId
_CucsVnicIpV4StaticAddrInstanceId_Object=MibTableColumn
cucsVnicIpV4StaticAddrInstanceId=_CucsVnicIpV4StaticAddrInstanceId_Object((1,3,6,1,4,1,9,9,719,1,53,22,1,1),_CucsVnicIpV4StaticAddrInstanceId_Type())
cucsVnicIpV4StaticAddrInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsVnicIpV4StaticAddrInstanceId.setStatus(_A)
_CucsVnicIpV4StaticAddrDn_Type=CucsManagedObjectDn
_CucsVnicIpV4StaticAddrDn_Object=MibTableColumn
cucsVnicIpV4StaticAddrDn=_CucsVnicIpV4StaticAddrDn_Object((1,3,6,1,4,1,9,9,719,1,53,22,1,2),_CucsVnicIpV4StaticAddrDn_Type())
cucsVnicIpV4StaticAddrDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIpV4StaticAddrDn.setStatus(_A)
_CucsVnicIpV4StaticAddrRn_Type=SnmpAdminString
_CucsVnicIpV4StaticAddrRn_Object=MibTableColumn
cucsVnicIpV4StaticAddrRn=_CucsVnicIpV4StaticAddrRn_Object((1,3,6,1,4,1,9,9,719,1,53,22,1,3),_CucsVnicIpV4StaticAddrRn_Type())
cucsVnicIpV4StaticAddrRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIpV4StaticAddrRn.setStatus(_A)
_CucsVnicIpV4StaticAddrAddr_Type=InetAddressIPv4
_CucsVnicIpV4StaticAddrAddr_Object=MibTableColumn
cucsVnicIpV4StaticAddrAddr=_CucsVnicIpV4StaticAddrAddr_Object((1,3,6,1,4,1,9,9,719,1,53,22,1,4),_CucsVnicIpV4StaticAddrAddr_Type())
cucsVnicIpV4StaticAddrAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIpV4StaticAddrAddr.setStatus(_A)
_CucsVnicIpV4StaticAddrDefGw_Type=InetAddressIPv4
_CucsVnicIpV4StaticAddrDefGw_Object=MibTableColumn
cucsVnicIpV4StaticAddrDefGw=_CucsVnicIpV4StaticAddrDefGw_Object((1,3,6,1,4,1,9,9,719,1,53,22,1,5),_CucsVnicIpV4StaticAddrDefGw_Type())
cucsVnicIpV4StaticAddrDefGw.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIpV4StaticAddrDefGw.setStatus(_A)
_CucsVnicIpV4StaticAddrSubnet_Type=InetAddressIPv4
_CucsVnicIpV4StaticAddrSubnet_Object=MibTableColumn
cucsVnicIpV4StaticAddrSubnet=_CucsVnicIpV4StaticAddrSubnet_Object((1,3,6,1,4,1,9,9,719,1,53,22,1,6),_CucsVnicIpV4StaticAddrSubnet_Type())
cucsVnicIpV4StaticAddrSubnet.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIpV4StaticAddrSubnet.setStatus(_A)
_CucsVnicIpV4StaticAddrPrimDns_Type=InetAddressIPv4
_CucsVnicIpV4StaticAddrPrimDns_Object=MibTableColumn
cucsVnicIpV4StaticAddrPrimDns=_CucsVnicIpV4StaticAddrPrimDns_Object((1,3,6,1,4,1,9,9,719,1,53,22,1,7),_CucsVnicIpV4StaticAddrPrimDns_Type())
cucsVnicIpV4StaticAddrPrimDns.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIpV4StaticAddrPrimDns.setStatus(_A)
_CucsVnicIpV4StaticAddrSecDns_Type=InetAddressIPv4
_CucsVnicIpV4StaticAddrSecDns_Object=MibTableColumn
cucsVnicIpV4StaticAddrSecDns=_CucsVnicIpV4StaticAddrSecDns_Object((1,3,6,1,4,1,9,9,719,1,53,22,1,8),_CucsVnicIpV4StaticAddrSecDns_Type())
cucsVnicIpV4StaticAddrSecDns.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIpV4StaticAddrSecDns.setStatus(_A)
_CucsVnicIpcTable_Object=MibTable
cucsVnicIpcTable=_CucsVnicIpcTable_Object((1,3,6,1,4,1,9,9,719,1,53,23))
if mibBuilder.loadTexts:cucsVnicIpcTable.setStatus(_A)
_CucsVnicIpcEntry_Object=MibTableRow
cucsVnicIpcEntry=_CucsVnicIpcEntry_Object((1,3,6,1,4,1,9,9,719,1,53,23,1))
cucsVnicIpcEntry.setIndexNames((0,_C,_a))
if mibBuilder.loadTexts:cucsVnicIpcEntry.setStatus(_A)
_CucsVnicIpcInstanceId_Type=CucsManagedObjectId
_CucsVnicIpcInstanceId_Object=MibTableColumn
cucsVnicIpcInstanceId=_CucsVnicIpcInstanceId_Object((1,3,6,1,4,1,9,9,719,1,53,23,1,1),_CucsVnicIpcInstanceId_Type())
cucsVnicIpcInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsVnicIpcInstanceId.setStatus(_A)
_CucsVnicIpcDn_Type=CucsManagedObjectDn
_CucsVnicIpcDn_Object=MibTableColumn
cucsVnicIpcDn=_CucsVnicIpcDn_Object((1,3,6,1,4,1,9,9,719,1,53,23,1,2),_CucsVnicIpcDn_Type())
cucsVnicIpcDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIpcDn.setStatus(_A)
_CucsVnicIpcRn_Type=SnmpAdminString
_CucsVnicIpcRn_Object=MibTableColumn
cucsVnicIpcRn=_CucsVnicIpcRn_Object((1,3,6,1,4,1,9,9,719,1,53,23,1,3),_CucsVnicIpcRn_Type())
cucsVnicIpcRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIpcRn.setStatus(_A)
_CucsVnicIpcAdaptorProfileName_Type=SnmpAdminString
_CucsVnicIpcAdaptorProfileName_Object=MibTableColumn
cucsVnicIpcAdaptorProfileName=_CucsVnicIpcAdaptorProfileName_Object((1,3,6,1,4,1,9,9,719,1,53,23,1,4),_CucsVnicIpcAdaptorProfileName_Type())
cucsVnicIpcAdaptorProfileName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIpcAdaptorProfileName.setStatus(_A)
_CucsVnicIpcAddr_Type=MacAddress
_CucsVnicIpcAddr_Object=MibTableColumn
cucsVnicIpcAddr=_CucsVnicIpcAddr_Object((1,3,6,1,4,1,9,9,719,1,53,23,1,5),_CucsVnicIpcAddr_Type())
cucsVnicIpcAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIpcAddr.setStatus(_A)
_CucsVnicIpcAdminVcon_Type=SnmpAdminString
_CucsVnicIpcAdminVcon_Object=MibTableColumn
cucsVnicIpcAdminVcon=_CucsVnicIpcAdminVcon_Object((1,3,6,1,4,1,9,9,719,1,53,23,1,6),_CucsVnicIpcAdminVcon_Type())
cucsVnicIpcAdminVcon.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIpcAdminVcon.setStatus(_A)
_CucsVnicIpcBootDev_Type=CucsVnicVnicBootDev
_CucsVnicIpcBootDev_Object=MibTableColumn
cucsVnicIpcBootDev=_CucsVnicIpcBootDev_Object((1,3,6,1,4,1,9,9,719,1,53,23,1,7),_CucsVnicIpcBootDev_Type())
cucsVnicIpcBootDev.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIpcBootDev.setStatus(_A)
_CucsVnicIpcConfigState_Type=CucsLsConfigState
_CucsVnicIpcConfigState_Object=MibTableColumn
cucsVnicIpcConfigState=_CucsVnicIpcConfigState_Object((1,3,6,1,4,1,9,9,719,1,53,23,1,8),_CucsVnicIpcConfigState_Type())
cucsVnicIpcConfigState.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIpcConfigState.setStatus(_A)
_CucsVnicIpcEquipmentDn_Type=SnmpAdminString
_CucsVnicIpcEquipmentDn_Object=MibTableColumn
cucsVnicIpcEquipmentDn=_CucsVnicIpcEquipmentDn_Object((1,3,6,1,4,1,9,9,719,1,53,23,1,9),_CucsVnicIpcEquipmentDn_Type())
cucsVnicIpcEquipmentDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIpcEquipmentDn.setStatus(_A)
_CucsVnicIpcIdentPoolName_Type=SnmpAdminString
_CucsVnicIpcIdentPoolName_Object=MibTableColumn
cucsVnicIpcIdentPoolName=_CucsVnicIpcIdentPoolName_Object((1,3,6,1,4,1,9,9,719,1,53,23,1,10),_CucsVnicIpcIdentPoolName_Type())
cucsVnicIpcIdentPoolName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIpcIdentPoolName.setStatus(_A)
_CucsVnicIpcInstType_Type=CucsVnicInstantiation
_CucsVnicIpcInstType_Object=MibTableColumn
cucsVnicIpcInstType=_CucsVnicIpcInstType_Object((1,3,6,1,4,1,9,9,719,1,53,23,1,11),_CucsVnicIpcInstType_Type())
cucsVnicIpcInstType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIpcInstType.setStatus(_A)
_CucsVnicIpcMtu_Type=Gauge32
_CucsVnicIpcMtu_Object=MibTableColumn
cucsVnicIpcMtu=_CucsVnicIpcMtu_Object((1,3,6,1,4,1,9,9,719,1,53,23,1,12),_CucsVnicIpcMtu_Type())
cucsVnicIpcMtu.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIpcMtu.setStatus(_A)
_CucsVnicIpcName_Type=SnmpAdminString
_CucsVnicIpcName_Object=MibTableColumn
cucsVnicIpcName=_CucsVnicIpcName_Object((1,3,6,1,4,1,9,9,719,1,53,23,1,13),_CucsVnicIpcName_Type())
cucsVnicIpcName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIpcName.setStatus(_A)
_CucsVnicIpcNwCtrlPolicyName_Type=SnmpAdminString
_CucsVnicIpcNwCtrlPolicyName_Object=MibTableColumn
cucsVnicIpcNwCtrlPolicyName=_CucsVnicIpcNwCtrlPolicyName_Object((1,3,6,1,4,1,9,9,719,1,53,23,1,14),_CucsVnicIpcNwCtrlPolicyName_Type())
cucsVnicIpcNwCtrlPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIpcNwCtrlPolicyName.setStatus(_A)
_CucsVnicIpcNwTemplName_Type=SnmpAdminString
_CucsVnicIpcNwTemplName_Object=MibTableColumn
cucsVnicIpcNwTemplName=_CucsVnicIpcNwTemplName_Object((1,3,6,1,4,1,9,9,719,1,53,23,1,15),_CucsVnicIpcNwTemplName_Type())
cucsVnicIpcNwTemplName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIpcNwTemplName.setStatus(_A)
_CucsVnicIpcOperAdaptorProfileName_Type=SnmpAdminString
_CucsVnicIpcOperAdaptorProfileName_Object=MibTableColumn
cucsVnicIpcOperAdaptorProfileName=_CucsVnicIpcOperAdaptorProfileName_Object((1,3,6,1,4,1,9,9,719,1,53,23,1,16),_CucsVnicIpcOperAdaptorProfileName_Type())
cucsVnicIpcOperAdaptorProfileName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIpcOperAdaptorProfileName.setStatus(_A)
_CucsVnicIpcOperIdentPoolName_Type=SnmpAdminString
_CucsVnicIpcOperIdentPoolName_Object=MibTableColumn
cucsVnicIpcOperIdentPoolName=_CucsVnicIpcOperIdentPoolName_Object((1,3,6,1,4,1,9,9,719,1,53,23,1,17),_CucsVnicIpcOperIdentPoolName_Type())
cucsVnicIpcOperIdentPoolName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIpcOperIdentPoolName.setStatus(_A)
_CucsVnicIpcOperNwCtrlPolicyName_Type=SnmpAdminString
_CucsVnicIpcOperNwCtrlPolicyName_Object=MibTableColumn
cucsVnicIpcOperNwCtrlPolicyName=_CucsVnicIpcOperNwCtrlPolicyName_Object((1,3,6,1,4,1,9,9,719,1,53,23,1,18),_CucsVnicIpcOperNwCtrlPolicyName_Type())
cucsVnicIpcOperNwCtrlPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIpcOperNwCtrlPolicyName.setStatus(_A)
_CucsVnicIpcOperNwTemplName_Type=SnmpAdminString
_CucsVnicIpcOperNwTemplName_Object=MibTableColumn
cucsVnicIpcOperNwTemplName=_CucsVnicIpcOperNwTemplName_Object((1,3,6,1,4,1,9,9,719,1,53,23,1,19),_CucsVnicIpcOperNwTemplName_Type())
cucsVnicIpcOperNwTemplName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIpcOperNwTemplName.setStatus(_A)
_CucsVnicIpcOperOrder_Type=Gauge32
_CucsVnicIpcOperOrder_Object=MibTableColumn
cucsVnicIpcOperOrder=_CucsVnicIpcOperOrder_Object((1,3,6,1,4,1,9,9,719,1,53,23,1,20),_CucsVnicIpcOperOrder_Type())
cucsVnicIpcOperOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIpcOperOrder.setStatus(_A)
_CucsVnicIpcOperQosPolicyName_Type=SnmpAdminString
_CucsVnicIpcOperQosPolicyName_Object=MibTableColumn
cucsVnicIpcOperQosPolicyName=_CucsVnicIpcOperQosPolicyName_Object((1,3,6,1,4,1,9,9,719,1,53,23,1,21),_CucsVnicIpcOperQosPolicyName_Type())
cucsVnicIpcOperQosPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIpcOperQosPolicyName.setStatus(_A)
_CucsVnicIpcOperSpeed_Type=Gauge32
_CucsVnicIpcOperSpeed_Object=MibTableColumn
cucsVnicIpcOperSpeed=_CucsVnicIpcOperSpeed_Object((1,3,6,1,4,1,9,9,719,1,53,23,1,22),_CucsVnicIpcOperSpeed_Type())
cucsVnicIpcOperSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIpcOperSpeed.setStatus(_A)
_CucsVnicIpcOperStatsPolicyName_Type=SnmpAdminString
_CucsVnicIpcOperStatsPolicyName_Object=MibTableColumn
cucsVnicIpcOperStatsPolicyName=_CucsVnicIpcOperStatsPolicyName_Object((1,3,6,1,4,1,9,9,719,1,53,23,1,23),_CucsVnicIpcOperStatsPolicyName_Type())
cucsVnicIpcOperStatsPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIpcOperStatsPolicyName.setStatus(_A)
_CucsVnicIpcOperVcon_Type=SnmpAdminString
_CucsVnicIpcOperVcon_Object=MibTableColumn
cucsVnicIpcOperVcon=_CucsVnicIpcOperVcon_Object((1,3,6,1,4,1,9,9,719,1,53,23,1,24),_CucsVnicIpcOperVcon_Type())
cucsVnicIpcOperVcon.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIpcOperVcon.setStatus(_A)
_CucsVnicIpcOrder_Type=Gauge32
_CucsVnicIpcOrder_Object=MibTableColumn
cucsVnicIpcOrder=_CucsVnicIpcOrder_Object((1,3,6,1,4,1,9,9,719,1,53,23,1,25),_CucsVnicIpcOrder_Type())
cucsVnicIpcOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIpcOrder.setStatus(_A)
_CucsVnicIpcOwner_Type=CucsVnicConnectionOwner
_CucsVnicIpcOwner_Object=MibTableColumn
cucsVnicIpcOwner=_CucsVnicIpcOwner_Object((1,3,6,1,4,1,9,9,719,1,53,23,1,26),_CucsVnicIpcOwner_Type())
cucsVnicIpcOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIpcOwner.setStatus(_A)
_CucsVnicIpcPinToGroupName_Type=SnmpAdminString
_CucsVnicIpcPinToGroupName_Object=MibTableColumn
cucsVnicIpcPinToGroupName=_CucsVnicIpcPinToGroupName_Object((1,3,6,1,4,1,9,9,719,1,53,23,1,27),_CucsVnicIpcPinToGroupName_Type())
cucsVnicIpcPinToGroupName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIpcPinToGroupName.setStatus(_A)
_CucsVnicIpcQosPolicyName_Type=SnmpAdminString
_CucsVnicIpcQosPolicyName_Object=MibTableColumn
cucsVnicIpcQosPolicyName=_CucsVnicIpcQosPolicyName_Object((1,3,6,1,4,1,9,9,719,1,53,23,1,28),_CucsVnicIpcQosPolicyName_Type())
cucsVnicIpcQosPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIpcQosPolicyName.setStatus(_A)
_CucsVnicIpcStatsPolicyName_Type=SnmpAdminString
_CucsVnicIpcStatsPolicyName_Object=MibTableColumn
cucsVnicIpcStatsPolicyName=_CucsVnicIpcStatsPolicyName_Object((1,3,6,1,4,1,9,9,719,1,53,23,1,29),_CucsVnicIpcStatsPolicyName_Type())
cucsVnicIpcStatsPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIpcStatsPolicyName.setStatus(_A)
_CucsVnicIpcSwitchId_Type=CucsVnicEtherBaseSwitchId
_CucsVnicIpcSwitchId_Object=MibTableColumn
cucsVnicIpcSwitchId=_CucsVnicIpcSwitchId_Object((1,3,6,1,4,1,9,9,719,1,53,23,1,30),_CucsVnicIpcSwitchId_Type())
cucsVnicIpcSwitchId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIpcSwitchId.setStatus(_A)
_CucsVnicIpcType_Type=CucsVnicIpcType
_CucsVnicIpcType_Object=MibTableColumn
cucsVnicIpcType=_CucsVnicIpcType_Object((1,3,6,1,4,1,9,9,719,1,53,23,1,31),_CucsVnicIpcType_Type())
cucsVnicIpcType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIpcType.setStatus(_A)
_CucsVnicIpcOperPinToGroupName_Type=SnmpAdminString
_CucsVnicIpcOperPinToGroupName_Object=MibTableColumn
cucsVnicIpcOperPinToGroupName=_CucsVnicIpcOperPinToGroupName_Object((1,3,6,1,4,1,9,9,719,1,53,23,1,32),_CucsVnicIpcOperPinToGroupName_Type())
cucsVnicIpcOperPinToGroupName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIpcOperPinToGroupName.setStatus(_A)
_CucsVnicIpcConfigQualifier_Type=CucsVnicConfigIssues
_CucsVnicIpcConfigQualifier_Object=MibTableColumn
cucsVnicIpcConfigQualifier=_CucsVnicIpcConfigQualifier_Object((1,3,6,1,4,1,9,9,719,1,53,23,1,33),_CucsVnicIpcConfigQualifier_Type())
cucsVnicIpcConfigQualifier.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIpcConfigQualifier.setStatus(_A)
_CucsVnicIpcAdminHostPort_Type=CucsFabricHostPortId
_CucsVnicIpcAdminHostPort_Object=MibTableColumn
cucsVnicIpcAdminHostPort=_CucsVnicIpcAdminHostPort_Object((1,3,6,1,4,1,9,9,719,1,53,23,1,35),_CucsVnicIpcAdminHostPort_Type())
cucsVnicIpcAdminHostPort.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIpcAdminHostPort.setStatus(_A)
_CucsVnicIpcOperHostPort_Type=CucsVnicVnicOperHostPort
_CucsVnicIpcOperHostPort_Object=MibTableColumn
cucsVnicIpcOperHostPort=_CucsVnicIpcOperHostPort_Object((1,3,6,1,4,1,9,9,719,1,53,23,1,36),_CucsVnicIpcOperHostPort_Type())
cucsVnicIpcOperHostPort.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIpcOperHostPort.setStatus(_A)
_CucsVnicIpcPurpose_Type=CucsAdaptorPurpose
_CucsVnicIpcPurpose_Object=MibTableColumn
cucsVnicIpcPurpose=_CucsVnicIpcPurpose_Object((1,3,6,1,4,1,9,9,719,1,53,23,1,37),_CucsVnicIpcPurpose_Type())
cucsVnicIpcPurpose.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIpcPurpose.setStatus(_A)
_CucsVnicIpcAdminCdnName_Type=SnmpAdminString
_CucsVnicIpcAdminCdnName_Object=MibTableColumn
cucsVnicIpcAdminCdnName=_CucsVnicIpcAdminCdnName_Object((1,3,6,1,4,1,9,9,719,1,53,23,1,38),_CucsVnicIpcAdminCdnName_Type())
cucsVnicIpcAdminCdnName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIpcAdminCdnName.setStatus(_A)
_CucsVnicIpcOperCdnName_Type=SnmpAdminString
_CucsVnicIpcOperCdnName_Object=MibTableColumn
cucsVnicIpcOperCdnName=_CucsVnicIpcOperCdnName_Object((1,3,6,1,4,1,9,9,719,1,53,23,1,39),_CucsVnicIpcOperCdnName_Type())
cucsVnicIpcOperCdnName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIpcOperCdnName.setStatus(_A)
_CucsVnicIpcCdnPropInSync_Type=TruthValue
_CucsVnicIpcCdnPropInSync_Object=MibTableColumn
cucsVnicIpcCdnPropInSync=_CucsVnicIpcCdnPropInSync_Object((1,3,6,1,4,1,9,9,719,1,53,23,1,40),_CucsVnicIpcCdnPropInSync_Type())
cucsVnicIpcCdnPropInSync.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIpcCdnPropInSync.setStatus(_A)
_CucsVnicIpcCdnSource_Type=CucsVnicCdnSource
_CucsVnicIpcCdnSource_Object=MibTableColumn
cucsVnicIpcCdnSource=_CucsVnicIpcCdnSource_Object((1,3,6,1,4,1,9,9,719,1,53,23,1,41),_CucsVnicIpcCdnSource_Type())
cucsVnicIpcCdnSource.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIpcCdnSource.setStatus(_A)
_CucsVnicIpcRedundancyPairType_Type=CucsVnicRedundancyPairType
_CucsVnicIpcRedundancyPairType_Object=MibTableColumn
cucsVnicIpcRedundancyPairType=_CucsVnicIpcRedundancyPairType_Object((1,3,6,1,4,1,9,9,719,1,53,23,1,42),_CucsVnicIpcRedundancyPairType_Type())
cucsVnicIpcRedundancyPairType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIpcRedundancyPairType.setStatus(_A)
_CucsVnicIpcRedundancyPeer_Type=SnmpAdminString
_CucsVnicIpcRedundancyPeer_Object=MibTableColumn
cucsVnicIpcRedundancyPeer=_CucsVnicIpcRedundancyPeer_Object((1,3,6,1,4,1,9,9,719,1,53,23,1,43),_CucsVnicIpcRedundancyPeer_Type())
cucsVnicIpcRedundancyPeer.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIpcRedundancyPeer.setStatus(_A)
_CucsVnicIpcIfTable_Object=MibTable
cucsVnicIpcIfTable=_CucsVnicIpcIfTable_Object((1,3,6,1,4,1,9,9,719,1,53,24))
if mibBuilder.loadTexts:cucsVnicIpcIfTable.setStatus(_A)
_CucsVnicIpcIfEntry_Object=MibTableRow
cucsVnicIpcIfEntry=_CucsVnicIpcIfEntry_Object((1,3,6,1,4,1,9,9,719,1,53,24,1))
cucsVnicIpcIfEntry.setIndexNames((0,_C,_b))
if mibBuilder.loadTexts:cucsVnicIpcIfEntry.setStatus(_A)
_CucsVnicIpcIfInstanceId_Type=CucsManagedObjectId
_CucsVnicIpcIfInstanceId_Object=MibTableColumn
cucsVnicIpcIfInstanceId=_CucsVnicIpcIfInstanceId_Object((1,3,6,1,4,1,9,9,719,1,53,24,1,1),_CucsVnicIpcIfInstanceId_Type())
cucsVnicIpcIfInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsVnicIpcIfInstanceId.setStatus(_A)
_CucsVnicIpcIfDn_Type=CucsManagedObjectDn
_CucsVnicIpcIfDn_Object=MibTableColumn
cucsVnicIpcIfDn=_CucsVnicIpcIfDn_Object((1,3,6,1,4,1,9,9,719,1,53,24,1,2),_CucsVnicIpcIfDn_Type())
cucsVnicIpcIfDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIpcIfDn.setStatus(_A)
_CucsVnicIpcIfRn_Type=SnmpAdminString
_CucsVnicIpcIfRn_Object=MibTableColumn
cucsVnicIpcIfRn=_CucsVnicIpcIfRn_Object((1,3,6,1,4,1,9,9,719,1,53,24,1,3),_CucsVnicIpcIfRn_Type())
cucsVnicIpcIfRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIpcIfRn.setStatus(_A)
_CucsVnicIpcIfAddr_Type=MacAddress
_CucsVnicIpcIfAddr_Object=MibTableColumn
cucsVnicIpcIfAddr=_CucsVnicIpcIfAddr_Object((1,3,6,1,4,1,9,9,719,1,53,24,1,4),_CucsVnicIpcIfAddr_Type())
cucsVnicIpcIfAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIpcIfAddr.setStatus(_A)
_CucsVnicIpcIfDefaultNet_Type=TruthValue
_CucsVnicIpcIfDefaultNet_Object=MibTableColumn
cucsVnicIpcIfDefaultNet=_CucsVnicIpcIfDefaultNet_Object((1,3,6,1,4,1,9,9,719,1,53,24,1,5),_CucsVnicIpcIfDefaultNet_Type())
cucsVnicIpcIfDefaultNet.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIpcIfDefaultNet.setStatus(_A)
_CucsVnicIpcIfName_Type=SnmpAdminString
_CucsVnicIpcIfName_Object=MibTableColumn
cucsVnicIpcIfName=_CucsVnicIpcIfName_Object((1,3,6,1,4,1,9,9,719,1,53,24,1,6),_CucsVnicIpcIfName_Type())
cucsVnicIpcIfName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIpcIfName.setStatus(_A)
_CucsVnicIpcIfOperState_Type=CucsVnicIfOperState
_CucsVnicIpcIfOperState_Object=MibTableColumn
cucsVnicIpcIfOperState=_CucsVnicIpcIfOperState_Object((1,3,6,1,4,1,9,9,719,1,53,24,1,7),_CucsVnicIpcIfOperState_Type())
cucsVnicIpcIfOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIpcIfOperState.setStatus(_A)
_CucsVnicIpcIfOwner_Type=CucsVnicConnectionOwner
_CucsVnicIpcIfOwner_Object=MibTableColumn
cucsVnicIpcIfOwner=_CucsVnicIpcIfOwner_Object((1,3,6,1,4,1,9,9,719,1,53,24,1,8),_CucsVnicIpcIfOwner_Type())
cucsVnicIpcIfOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIpcIfOwner.setStatus(_A)
_CucsVnicIpcIfSwitchId_Type=CucsVnicEtherBaseIfSwitchId
_CucsVnicIpcIfSwitchId_Object=MibTableColumn
cucsVnicIpcIfSwitchId=_CucsVnicIpcIfSwitchId_Object((1,3,6,1,4,1,9,9,719,1,53,24,1,9),_CucsVnicIpcIfSwitchId_Type())
cucsVnicIpcIfSwitchId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIpcIfSwitchId.setStatus(_A)
_CucsVnicIpcIfType_Type=CucsVnicAIpcIfType
_CucsVnicIpcIfType_Object=MibTableColumn
cucsVnicIpcIfType=_CucsVnicIpcIfType_Object((1,3,6,1,4,1,9,9,719,1,53,24,1,10),_CucsVnicIpcIfType_Type())
cucsVnicIpcIfType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIpcIfType.setStatus(_A)
_CucsVnicIpcIfVnet_Type=Gauge32
_CucsVnicIpcIfVnet_Object=MibTableColumn
cucsVnicIpcIfVnet=_CucsVnicIpcIfVnet_Object((1,3,6,1,4,1,9,9,719,1,53,24,1,11),_CucsVnicIpcIfVnet_Type())
cucsVnicIpcIfVnet.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIpcIfVnet.setStatus(_A)
_CucsVnicIpcIfConfigQualifier_Type=CucsVnicConfigIssues
_CucsVnicIpcIfConfigQualifier_Object=MibTableColumn
cucsVnicIpcIfConfigQualifier=_CucsVnicIpcIfConfigQualifier_Object((1,3,6,1,4,1,9,9,719,1,53,24,1,12),_CucsVnicIpcIfConfigQualifier_Type())
cucsVnicIpcIfConfigQualifier.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIpcIfConfigQualifier.setStatus(_A)
_CucsVnicIpcIfOperVnetDn_Type=SnmpAdminString
_CucsVnicIpcIfOperVnetDn_Object=MibTableColumn
cucsVnicIpcIfOperVnetDn=_CucsVnicIpcIfOperVnetDn_Object((1,3,6,1,4,1,9,9,719,1,53,24,1,14),_CucsVnicIpcIfOperVnetDn_Type())
cucsVnicIpcIfOperVnetDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIpcIfOperVnetDn.setStatus(_A)
_CucsVnicIpcIfOperVnetName_Type=SnmpAdminString
_CucsVnicIpcIfOperVnetName_Object=MibTableColumn
cucsVnicIpcIfOperVnetName=_CucsVnicIpcIfOperVnetName_Object((1,3,6,1,4,1,9,9,719,1,53,24,1,15),_CucsVnicIpcIfOperVnetName_Type())
cucsVnicIpcIfOperVnetName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIpcIfOperVnetName.setStatus(_A)
_CucsVnicIpcIfPubNwId_Type=Gauge32
_CucsVnicIpcIfPubNwId_Object=MibTableColumn
cucsVnicIpcIfPubNwId=_CucsVnicIpcIfPubNwId_Object((1,3,6,1,4,1,9,9,719,1,53,24,1,16),_CucsVnicIpcIfPubNwId_Type())
cucsVnicIpcIfPubNwId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIpcIfPubNwId.setStatus(_A)
_CucsVnicIpcIfSharing_Type=CucsFabricVlanSharingType
_CucsVnicIpcIfSharing_Object=MibTableColumn
cucsVnicIpcIfSharing=_CucsVnicIpcIfSharing_Object((1,3,6,1,4,1,9,9,719,1,53,24,1,17),_CucsVnicIpcIfSharing_Type())
cucsVnicIpcIfSharing.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIpcIfSharing.setStatus(_A)
_CucsVnicIpcIfOperPrimaryVnetDn_Type=SnmpAdminString
_CucsVnicIpcIfOperPrimaryVnetDn_Object=MibTableColumn
cucsVnicIpcIfOperPrimaryVnetDn=_CucsVnicIpcIfOperPrimaryVnetDn_Object((1,3,6,1,4,1,9,9,719,1,53,24,1,18),_CucsVnicIpcIfOperPrimaryVnetDn_Type())
cucsVnicIpcIfOperPrimaryVnetDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIpcIfOperPrimaryVnetDn.setStatus(_A)
_CucsVnicIpcIfOperPrimaryVnetName_Type=SnmpAdminString
_CucsVnicIpcIfOperPrimaryVnetName_Object=MibTableColumn
cucsVnicIpcIfOperPrimaryVnetName=_CucsVnicIpcIfOperPrimaryVnetName_Object((1,3,6,1,4,1,9,9,719,1,53,24,1,19),_CucsVnicIpcIfOperPrimaryVnetName_Type())
cucsVnicIpcIfOperPrimaryVnetName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIpcIfOperPrimaryVnetName.setStatus(_A)
_CucsVnicLanConnTemplTable_Object=MibTable
cucsVnicLanConnTemplTable=_CucsVnicLanConnTemplTable_Object((1,3,6,1,4,1,9,9,719,1,53,25))
if mibBuilder.loadTexts:cucsVnicLanConnTemplTable.setStatus(_A)
_CucsVnicLanConnTemplEntry_Object=MibTableRow
cucsVnicLanConnTemplEntry=_CucsVnicLanConnTemplEntry_Object((1,3,6,1,4,1,9,9,719,1,53,25,1))
cucsVnicLanConnTemplEntry.setIndexNames((0,_C,_c))
if mibBuilder.loadTexts:cucsVnicLanConnTemplEntry.setStatus(_A)
_CucsVnicLanConnTemplInstanceId_Type=CucsManagedObjectId
_CucsVnicLanConnTemplInstanceId_Object=MibTableColumn
cucsVnicLanConnTemplInstanceId=_CucsVnicLanConnTemplInstanceId_Object((1,3,6,1,4,1,9,9,719,1,53,25,1,1),_CucsVnicLanConnTemplInstanceId_Type())
cucsVnicLanConnTemplInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsVnicLanConnTemplInstanceId.setStatus(_A)
_CucsVnicLanConnTemplDn_Type=CucsManagedObjectDn
_CucsVnicLanConnTemplDn_Object=MibTableColumn
cucsVnicLanConnTemplDn=_CucsVnicLanConnTemplDn_Object((1,3,6,1,4,1,9,9,719,1,53,25,1,2),_CucsVnicLanConnTemplDn_Type())
cucsVnicLanConnTemplDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicLanConnTemplDn.setStatus(_A)
_CucsVnicLanConnTemplRn_Type=SnmpAdminString
_CucsVnicLanConnTemplRn_Object=MibTableColumn
cucsVnicLanConnTemplRn=_CucsVnicLanConnTemplRn_Object((1,3,6,1,4,1,9,9,719,1,53,25,1,3),_CucsVnicLanConnTemplRn_Type())
cucsVnicLanConnTemplRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicLanConnTemplRn.setStatus(_A)
_CucsVnicLanConnTemplDescr_Type=SnmpAdminString
_CucsVnicLanConnTemplDescr_Object=MibTableColumn
cucsVnicLanConnTemplDescr=_CucsVnicLanConnTemplDescr_Object((1,3,6,1,4,1,9,9,719,1,53,25,1,4),_CucsVnicLanConnTemplDescr_Type())
cucsVnicLanConnTemplDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicLanConnTemplDescr.setStatus(_A)
_CucsVnicLanConnTemplIdentPoolName_Type=SnmpAdminString
_CucsVnicLanConnTemplIdentPoolName_Object=MibTableColumn
cucsVnicLanConnTemplIdentPoolName=_CucsVnicLanConnTemplIdentPoolName_Object((1,3,6,1,4,1,9,9,719,1,53,25,1,5),_CucsVnicLanConnTemplIdentPoolName_Type())
cucsVnicLanConnTemplIdentPoolName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicLanConnTemplIdentPoolName.setStatus(_A)
_CucsVnicLanConnTemplIntId_Type=SnmpAdminString
_CucsVnicLanConnTemplIntId_Object=MibTableColumn
cucsVnicLanConnTemplIntId=_CucsVnicLanConnTemplIntId_Object((1,3,6,1,4,1,9,9,719,1,53,25,1,6),_CucsVnicLanConnTemplIntId_Type())
cucsVnicLanConnTemplIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicLanConnTemplIntId.setStatus(_A)
_CucsVnicLanConnTemplMtu_Type=Gauge32
_CucsVnicLanConnTemplMtu_Object=MibTableColumn
cucsVnicLanConnTemplMtu=_CucsVnicLanConnTemplMtu_Object((1,3,6,1,4,1,9,9,719,1,53,25,1,7),_CucsVnicLanConnTemplMtu_Type())
cucsVnicLanConnTemplMtu.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicLanConnTemplMtu.setStatus(_A)
_CucsVnicLanConnTemplName_Type=SnmpAdminString
_CucsVnicLanConnTemplName_Object=MibTableColumn
cucsVnicLanConnTemplName=_CucsVnicLanConnTemplName_Object((1,3,6,1,4,1,9,9,719,1,53,25,1,8),_CucsVnicLanConnTemplName_Type())
cucsVnicLanConnTemplName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicLanConnTemplName.setStatus(_A)
_CucsVnicLanConnTemplNwCtrlPolicyName_Type=SnmpAdminString
_CucsVnicLanConnTemplNwCtrlPolicyName_Object=MibTableColumn
cucsVnicLanConnTemplNwCtrlPolicyName=_CucsVnicLanConnTemplNwCtrlPolicyName_Object((1,3,6,1,4,1,9,9,719,1,53,25,1,9),_CucsVnicLanConnTemplNwCtrlPolicyName_Type())
cucsVnicLanConnTemplNwCtrlPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicLanConnTemplNwCtrlPolicyName.setStatus(_A)
_CucsVnicLanConnTemplOperIdentPoolName_Type=SnmpAdminString
_CucsVnicLanConnTemplOperIdentPoolName_Object=MibTableColumn
cucsVnicLanConnTemplOperIdentPoolName=_CucsVnicLanConnTemplOperIdentPoolName_Object((1,3,6,1,4,1,9,9,719,1,53,25,1,10),_CucsVnicLanConnTemplOperIdentPoolName_Type())
cucsVnicLanConnTemplOperIdentPoolName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicLanConnTemplOperIdentPoolName.setStatus(_A)
_CucsVnicLanConnTemplOperNwCtrlPolicyName_Type=SnmpAdminString
_CucsVnicLanConnTemplOperNwCtrlPolicyName_Object=MibTableColumn
cucsVnicLanConnTemplOperNwCtrlPolicyName=_CucsVnicLanConnTemplOperNwCtrlPolicyName_Object((1,3,6,1,4,1,9,9,719,1,53,25,1,11),_CucsVnicLanConnTemplOperNwCtrlPolicyName_Type())
cucsVnicLanConnTemplOperNwCtrlPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicLanConnTemplOperNwCtrlPolicyName.setStatus(_A)
_CucsVnicLanConnTemplOperQosPolicyName_Type=SnmpAdminString
_CucsVnicLanConnTemplOperQosPolicyName_Object=MibTableColumn
cucsVnicLanConnTemplOperQosPolicyName=_CucsVnicLanConnTemplOperQosPolicyName_Object((1,3,6,1,4,1,9,9,719,1,53,25,1,12),_CucsVnicLanConnTemplOperQosPolicyName_Type())
cucsVnicLanConnTemplOperQosPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicLanConnTemplOperQosPolicyName.setStatus(_A)
_CucsVnicLanConnTemplOperStatsPolicyName_Type=SnmpAdminString
_CucsVnicLanConnTemplOperStatsPolicyName_Object=MibTableColumn
cucsVnicLanConnTemplOperStatsPolicyName=_CucsVnicLanConnTemplOperStatsPolicyName_Object((1,3,6,1,4,1,9,9,719,1,53,25,1,13),_CucsVnicLanConnTemplOperStatsPolicyName_Type())
cucsVnicLanConnTemplOperStatsPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicLanConnTemplOperStatsPolicyName.setStatus(_A)
_CucsVnicLanConnTemplPinToGroupName_Type=SnmpAdminString
_CucsVnicLanConnTemplPinToGroupName_Object=MibTableColumn
cucsVnicLanConnTemplPinToGroupName=_CucsVnicLanConnTemplPinToGroupName_Object((1,3,6,1,4,1,9,9,719,1,53,25,1,14),_CucsVnicLanConnTemplPinToGroupName_Type())
cucsVnicLanConnTemplPinToGroupName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicLanConnTemplPinToGroupName.setStatus(_A)
_CucsVnicLanConnTemplQosPolicyName_Type=SnmpAdminString
_CucsVnicLanConnTemplQosPolicyName_Object=MibTableColumn
cucsVnicLanConnTemplQosPolicyName=_CucsVnicLanConnTemplQosPolicyName_Object((1,3,6,1,4,1,9,9,719,1,53,25,1,15),_CucsVnicLanConnTemplQosPolicyName_Type())
cucsVnicLanConnTemplQosPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicLanConnTemplQosPolicyName.setStatus(_A)
_CucsVnicLanConnTemplStatsPolicyName_Type=SnmpAdminString
_CucsVnicLanConnTemplStatsPolicyName_Object=MibTableColumn
cucsVnicLanConnTemplStatsPolicyName=_CucsVnicLanConnTemplStatsPolicyName_Object((1,3,6,1,4,1,9,9,719,1,53,25,1,16),_CucsVnicLanConnTemplStatsPolicyName_Type())
cucsVnicLanConnTemplStatsPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicLanConnTemplStatsPolicyName.setStatus(_A)
_CucsVnicLanConnTemplSwitchId_Type=CucsVnicLanConnTemplSwitchId
_CucsVnicLanConnTemplSwitchId_Object=MibTableColumn
cucsVnicLanConnTemplSwitchId=_CucsVnicLanConnTemplSwitchId_Object((1,3,6,1,4,1,9,9,719,1,53,25,1,17),_CucsVnicLanConnTemplSwitchId_Type())
cucsVnicLanConnTemplSwitchId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicLanConnTemplSwitchId.setStatus(_A)
_CucsVnicLanConnTemplTarget_Type=CucsVnicTemplateTarget
_CucsVnicLanConnTemplTarget_Object=MibTableColumn
cucsVnicLanConnTemplTarget=_CucsVnicLanConnTemplTarget_Object((1,3,6,1,4,1,9,9,719,1,53,25,1,18),_CucsVnicLanConnTemplTarget_Type())
cucsVnicLanConnTemplTarget.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicLanConnTemplTarget.setStatus(_A)
_CucsVnicLanConnTemplTemplType_Type=CucsVnicTemplateType
_CucsVnicLanConnTemplTemplType_Object=MibTableColumn
cucsVnicLanConnTemplTemplType=_CucsVnicLanConnTemplTemplType_Object((1,3,6,1,4,1,9,9,719,1,53,25,1,19),_CucsVnicLanConnTemplTemplType_Type())
cucsVnicLanConnTemplTemplType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicLanConnTemplTemplType.setStatus(_A)
_CucsVnicLanConnTemplPolicyLevel_Type=Gauge32
_CucsVnicLanConnTemplPolicyLevel_Object=MibTableColumn
cucsVnicLanConnTemplPolicyLevel=_CucsVnicLanConnTemplPolicyLevel_Object((1,3,6,1,4,1,9,9,719,1,53,25,1,20),_CucsVnicLanConnTemplPolicyLevel_Type())
cucsVnicLanConnTemplPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicLanConnTemplPolicyLevel.setStatus(_A)
_CucsVnicLanConnTemplPolicyOwner_Type=CucsPolicyPolicyOwner
_CucsVnicLanConnTemplPolicyOwner_Object=MibTableColumn
cucsVnicLanConnTemplPolicyOwner=_CucsVnicLanConnTemplPolicyOwner_Object((1,3,6,1,4,1,9,9,719,1,53,25,1,21),_CucsVnicLanConnTemplPolicyOwner_Type())
cucsVnicLanConnTemplPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicLanConnTemplPolicyOwner.setStatus(_A)
_CucsVnicLanConnTemplAdminCdnName_Type=SnmpAdminString
_CucsVnicLanConnTemplAdminCdnName_Object=MibTableColumn
cucsVnicLanConnTemplAdminCdnName=_CucsVnicLanConnTemplAdminCdnName_Object((1,3,6,1,4,1,9,9,719,1,53,25,1,22),_CucsVnicLanConnTemplAdminCdnName_Type())
cucsVnicLanConnTemplAdminCdnName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicLanConnTemplAdminCdnName.setStatus(_A)
_CucsVnicLanConnTemplCdnSource_Type=CucsVnicCdnSource
_CucsVnicLanConnTemplCdnSource_Object=MibTableColumn
cucsVnicLanConnTemplCdnSource=_CucsVnicLanConnTemplCdnSource_Object((1,3,6,1,4,1,9,9,719,1,53,25,1,23),_CucsVnicLanConnTemplCdnSource_Type())
cucsVnicLanConnTemplCdnSource.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicLanConnTemplCdnSource.setStatus(_A)
_CucsVnicLanConnTemplOperPeerRedundancyTemplName_Type=SnmpAdminString
_CucsVnicLanConnTemplOperPeerRedundancyTemplName_Object=MibTableColumn
cucsVnicLanConnTemplOperPeerRedundancyTemplName=_CucsVnicLanConnTemplOperPeerRedundancyTemplName_Object((1,3,6,1,4,1,9,9,719,1,53,25,1,24),_CucsVnicLanConnTemplOperPeerRedundancyTemplName_Type())
cucsVnicLanConnTemplOperPeerRedundancyTemplName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicLanConnTemplOperPeerRedundancyTemplName.setStatus(_A)
_CucsVnicLanConnTemplPeerRedundancyTemplName_Type=SnmpAdminString
_CucsVnicLanConnTemplPeerRedundancyTemplName_Object=MibTableColumn
cucsVnicLanConnTemplPeerRedundancyTemplName=_CucsVnicLanConnTemplPeerRedundancyTemplName_Object((1,3,6,1,4,1,9,9,719,1,53,25,1,25),_CucsVnicLanConnTemplPeerRedundancyTemplName_Type())
cucsVnicLanConnTemplPeerRedundancyTemplName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicLanConnTemplPeerRedundancyTemplName.setStatus(_A)
_CucsVnicLanConnTemplRedundancyPairType_Type=CucsVnicRedundancyPairType
_CucsVnicLanConnTemplRedundancyPairType_Object=MibTableColumn
cucsVnicLanConnTemplRedundancyPairType=_CucsVnicLanConnTemplRedundancyPairType_Object((1,3,6,1,4,1,9,9,719,1,53,25,1,26),_CucsVnicLanConnTemplRedundancyPairType_Type())
cucsVnicLanConnTemplRedundancyPairType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicLanConnTemplRedundancyPairType.setStatus(_A)
_CucsVnicLifVlanTable_Object=MibTable
cucsVnicLifVlanTable=_CucsVnicLifVlanTable_Object((1,3,6,1,4,1,9,9,719,1,53,26))
if mibBuilder.loadTexts:cucsVnicLifVlanTable.setStatus(_A)
_CucsVnicLifVlanEntry_Object=MibTableRow
cucsVnicLifVlanEntry=_CucsVnicLifVlanEntry_Object((1,3,6,1,4,1,9,9,719,1,53,26,1))
cucsVnicLifVlanEntry.setIndexNames((0,_C,_d))
if mibBuilder.loadTexts:cucsVnicLifVlanEntry.setStatus(_A)
_CucsVnicLifVlanInstanceId_Type=CucsManagedObjectId
_CucsVnicLifVlanInstanceId_Object=MibTableColumn
cucsVnicLifVlanInstanceId=_CucsVnicLifVlanInstanceId_Object((1,3,6,1,4,1,9,9,719,1,53,26,1,1),_CucsVnicLifVlanInstanceId_Type())
cucsVnicLifVlanInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsVnicLifVlanInstanceId.setStatus(_A)
_CucsVnicLifVlanDn_Type=CucsManagedObjectDn
_CucsVnicLifVlanDn_Object=MibTableColumn
cucsVnicLifVlanDn=_CucsVnicLifVlanDn_Object((1,3,6,1,4,1,9,9,719,1,53,26,1,2),_CucsVnicLifVlanDn_Type())
cucsVnicLifVlanDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicLifVlanDn.setStatus(_A)
_CucsVnicLifVlanRn_Type=SnmpAdminString
_CucsVnicLifVlanRn_Object=MibTableColumn
cucsVnicLifVlanRn=_CucsVnicLifVlanRn_Object((1,3,6,1,4,1,9,9,719,1,53,26,1,3),_CucsVnicLifVlanRn_Type())
cucsVnicLifVlanRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicLifVlanRn.setStatus(_A)
_CucsVnicLifVlanAddr_Type=MacAddress
_CucsVnicLifVlanAddr_Object=MibTableColumn
cucsVnicLifVlanAddr=_CucsVnicLifVlanAddr_Object((1,3,6,1,4,1,9,9,719,1,53,26,1,4),_CucsVnicLifVlanAddr_Type())
cucsVnicLifVlanAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicLifVlanAddr.setStatus(_A)
_CucsVnicLifVlanDefaultNet_Type=TruthValue
_CucsVnicLifVlanDefaultNet_Object=MibTableColumn
cucsVnicLifVlanDefaultNet=_CucsVnicLifVlanDefaultNet_Object((1,3,6,1,4,1,9,9,719,1,53,26,1,5),_CucsVnicLifVlanDefaultNet_Type())
cucsVnicLifVlanDefaultNet.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicLifVlanDefaultNet.setStatus(_A)
_CucsVnicLifVlanName_Type=SnmpAdminString
_CucsVnicLifVlanName_Object=MibTableColumn
cucsVnicLifVlanName=_CucsVnicLifVlanName_Object((1,3,6,1,4,1,9,9,719,1,53,26,1,6),_CucsVnicLifVlanName_Type())
cucsVnicLifVlanName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicLifVlanName.setStatus(_A)
_CucsVnicLifVlanOperState_Type=CucsVnicIfOperState
_CucsVnicLifVlanOperState_Object=MibTableColumn
cucsVnicLifVlanOperState=_CucsVnicLifVlanOperState_Object((1,3,6,1,4,1,9,9,719,1,53,26,1,7),_CucsVnicLifVlanOperState_Type())
cucsVnicLifVlanOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicLifVlanOperState.setStatus(_A)
_CucsVnicLifVlanOwner_Type=CucsVnicConnectionOwner
_CucsVnicLifVlanOwner_Object=MibTableColumn
cucsVnicLifVlanOwner=_CucsVnicLifVlanOwner_Object((1,3,6,1,4,1,9,9,719,1,53,26,1,8),_CucsVnicLifVlanOwner_Type())
cucsVnicLifVlanOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicLifVlanOwner.setStatus(_A)
_CucsVnicLifVlanSwitchId_Type=CucsVnicEtherBaseIfSwitchId
_CucsVnicLifVlanSwitchId_Object=MibTableColumn
cucsVnicLifVlanSwitchId=_CucsVnicLifVlanSwitchId_Object((1,3,6,1,4,1,9,9,719,1,53,26,1,9),_CucsVnicLifVlanSwitchId_Type())
cucsVnicLifVlanSwitchId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicLifVlanSwitchId.setStatus(_A)
_CucsVnicLifVlanType_Type=CucsVnicAEtherIfType
_CucsVnicLifVlanType_Object=MibTableColumn
cucsVnicLifVlanType=_CucsVnicLifVlanType_Object((1,3,6,1,4,1,9,9,719,1,53,26,1,10),_CucsVnicLifVlanType_Type())
cucsVnicLifVlanType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicLifVlanType.setStatus(_A)
_CucsVnicLifVlanVnet_Type=Gauge32
_CucsVnicLifVlanVnet_Object=MibTableColumn
cucsVnicLifVlanVnet=_CucsVnicLifVlanVnet_Object((1,3,6,1,4,1,9,9,719,1,53,26,1,11),_CucsVnicLifVlanVnet_Type())
cucsVnicLifVlanVnet.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicLifVlanVnet.setStatus(_A)
_CucsVnicLifVlanConfigQualifier_Type=CucsVnicConfigIssues
_CucsVnicLifVlanConfigQualifier_Object=MibTableColumn
cucsVnicLifVlanConfigQualifier=_CucsVnicLifVlanConfigQualifier_Object((1,3,6,1,4,1,9,9,719,1,53,26,1,12),_CucsVnicLifVlanConfigQualifier_Type())
cucsVnicLifVlanConfigQualifier.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicLifVlanConfigQualifier.setStatus(_A)
_CucsVnicLifVlanOperVnetDn_Type=SnmpAdminString
_CucsVnicLifVlanOperVnetDn_Object=MibTableColumn
cucsVnicLifVlanOperVnetDn=_CucsVnicLifVlanOperVnetDn_Object((1,3,6,1,4,1,9,9,719,1,53,26,1,14),_CucsVnicLifVlanOperVnetDn_Type())
cucsVnicLifVlanOperVnetDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicLifVlanOperVnetDn.setStatus(_A)
_CucsVnicLifVlanOperVnetName_Type=SnmpAdminString
_CucsVnicLifVlanOperVnetName_Object=MibTableColumn
cucsVnicLifVlanOperVnetName=_CucsVnicLifVlanOperVnetName_Object((1,3,6,1,4,1,9,9,719,1,53,26,1,15),_CucsVnicLifVlanOperVnetName_Type())
cucsVnicLifVlanOperVnetName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicLifVlanOperVnetName.setStatus(_A)
_CucsVnicLifVlanPubNwId_Type=Gauge32
_CucsVnicLifVlanPubNwId_Object=MibTableColumn
cucsVnicLifVlanPubNwId=_CucsVnicLifVlanPubNwId_Object((1,3,6,1,4,1,9,9,719,1,53,26,1,16),_CucsVnicLifVlanPubNwId_Type())
cucsVnicLifVlanPubNwId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicLifVlanPubNwId.setStatus(_A)
_CucsVnicLifVlanSharing_Type=CucsFabricVlanSharingType
_CucsVnicLifVlanSharing_Object=MibTableColumn
cucsVnicLifVlanSharing=_CucsVnicLifVlanSharing_Object((1,3,6,1,4,1,9,9,719,1,53,26,1,17),_CucsVnicLifVlanSharing_Type())
cucsVnicLifVlanSharing.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicLifVlanSharing.setStatus(_A)
_CucsVnicLifVlanPropAcl_Type=Unsigned64
_CucsVnicLifVlanPropAcl_Object=MibTableColumn
cucsVnicLifVlanPropAcl=_CucsVnicLifVlanPropAcl_Object((1,3,6,1,4,1,9,9,719,1,53,26,1,18),_CucsVnicLifVlanPropAcl_Type())
cucsVnicLifVlanPropAcl.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicLifVlanPropAcl.setStatus(_A)
_CucsVnicLifVlanOperPrimaryVnetDn_Type=SnmpAdminString
_CucsVnicLifVlanOperPrimaryVnetDn_Object=MibTableColumn
cucsVnicLifVlanOperPrimaryVnetDn=_CucsVnicLifVlanOperPrimaryVnetDn_Object((1,3,6,1,4,1,9,9,719,1,53,26,1,19),_CucsVnicLifVlanOperPrimaryVnetDn_Type())
cucsVnicLifVlanOperPrimaryVnetDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicLifVlanOperPrimaryVnetDn.setStatus(_A)
_CucsVnicLifVlanOperPrimaryVnetName_Type=SnmpAdminString
_CucsVnicLifVlanOperPrimaryVnetName_Object=MibTableColumn
cucsVnicLifVlanOperPrimaryVnetName=_CucsVnicLifVlanOperPrimaryVnetName_Object((1,3,6,1,4,1,9,9,719,1,53,26,1,20),_CucsVnicLifVlanOperPrimaryVnetName_Type())
cucsVnicLifVlanOperPrimaryVnetName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicLifVlanOperPrimaryVnetName.setStatus(_A)
_CucsVnicLifVsanTable_Object=MibTable
cucsVnicLifVsanTable=_CucsVnicLifVsanTable_Object((1,3,6,1,4,1,9,9,719,1,53,27))
if mibBuilder.loadTexts:cucsVnicLifVsanTable.setStatus(_A)
_CucsVnicLifVsanEntry_Object=MibTableRow
cucsVnicLifVsanEntry=_CucsVnicLifVsanEntry_Object((1,3,6,1,4,1,9,9,719,1,53,27,1))
cucsVnicLifVsanEntry.setIndexNames((0,_C,_e))
if mibBuilder.loadTexts:cucsVnicLifVsanEntry.setStatus(_A)
_CucsVnicLifVsanInstanceId_Type=CucsManagedObjectId
_CucsVnicLifVsanInstanceId_Object=MibTableColumn
cucsVnicLifVsanInstanceId=_CucsVnicLifVsanInstanceId_Object((1,3,6,1,4,1,9,9,719,1,53,27,1,1),_CucsVnicLifVsanInstanceId_Type())
cucsVnicLifVsanInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsVnicLifVsanInstanceId.setStatus(_A)
_CucsVnicLifVsanDn_Type=CucsManagedObjectDn
_CucsVnicLifVsanDn_Object=MibTableColumn
cucsVnicLifVsanDn=_CucsVnicLifVsanDn_Object((1,3,6,1,4,1,9,9,719,1,53,27,1,2),_CucsVnicLifVsanDn_Type())
cucsVnicLifVsanDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicLifVsanDn.setStatus(_A)
_CucsVnicLifVsanRn_Type=SnmpAdminString
_CucsVnicLifVsanRn_Object=MibTableColumn
cucsVnicLifVsanRn=_CucsVnicLifVsanRn_Object((1,3,6,1,4,1,9,9,719,1,53,27,1,3),_CucsVnicLifVsanRn_Type())
cucsVnicLifVsanRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicLifVsanRn.setStatus(_A)
_CucsVnicLifVsanInitiator_Type=Unsigned64
_CucsVnicLifVsanInitiator_Object=MibTableColumn
cucsVnicLifVsanInitiator=_CucsVnicLifVsanInitiator_Object((1,3,6,1,4,1,9,9,719,1,53,27,1,4),_CucsVnicLifVsanInitiator_Type())
cucsVnicLifVsanInitiator.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicLifVsanInitiator.setStatus(_A)
_CucsVnicLifVsanName_Type=SnmpAdminString
_CucsVnicLifVsanName_Object=MibTableColumn
cucsVnicLifVsanName=_CucsVnicLifVsanName_Object((1,3,6,1,4,1,9,9,719,1,53,27,1,5),_CucsVnicLifVsanName_Type())
cucsVnicLifVsanName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicLifVsanName.setStatus(_A)
_CucsVnicLifVsanOperState_Type=CucsVnicIfOperState
_CucsVnicLifVsanOperState_Object=MibTableColumn
cucsVnicLifVsanOperState=_CucsVnicLifVsanOperState_Object((1,3,6,1,4,1,9,9,719,1,53,27,1,6),_CucsVnicLifVsanOperState_Type())
cucsVnicLifVsanOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicLifVsanOperState.setStatus(_A)
_CucsVnicLifVsanOwner_Type=CucsVnicConnectionOwner
_CucsVnicLifVsanOwner_Object=MibTableColumn
cucsVnicLifVsanOwner=_CucsVnicLifVsanOwner_Object((1,3,6,1,4,1,9,9,719,1,53,27,1,7),_CucsVnicLifVsanOwner_Type())
cucsVnicLifVsanOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicLifVsanOwner.setStatus(_A)
_CucsVnicLifVsanSwitchId_Type=CucsVnicAFcIfSwitchId
_CucsVnicLifVsanSwitchId_Object=MibTableColumn
cucsVnicLifVsanSwitchId=_CucsVnicLifVsanSwitchId_Object((1,3,6,1,4,1,9,9,719,1,53,27,1,8),_CucsVnicLifVsanSwitchId_Type())
cucsVnicLifVsanSwitchId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicLifVsanSwitchId.setStatus(_A)
_CucsVnicLifVsanType_Type=CucsVnicAFcIfType
_CucsVnicLifVsanType_Object=MibTableColumn
cucsVnicLifVsanType=_CucsVnicLifVsanType_Object((1,3,6,1,4,1,9,9,719,1,53,27,1,9),_CucsVnicLifVsanType_Type())
cucsVnicLifVsanType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicLifVsanType.setStatus(_A)
_CucsVnicLifVsanVnet_Type=Gauge32
_CucsVnicLifVsanVnet_Object=MibTableColumn
cucsVnicLifVsanVnet=_CucsVnicLifVsanVnet_Object((1,3,6,1,4,1,9,9,719,1,53,27,1,10),_CucsVnicLifVsanVnet_Type())
cucsVnicLifVsanVnet.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicLifVsanVnet.setStatus(_A)
_CucsVnicLifVsanConfigQualifier_Type=CucsVnicConfigIssues
_CucsVnicLifVsanConfigQualifier_Object=MibTableColumn
cucsVnicLifVsanConfigQualifier=_CucsVnicLifVsanConfigQualifier_Object((1,3,6,1,4,1,9,9,719,1,53,27,1,11),_CucsVnicLifVsanConfigQualifier_Type())
cucsVnicLifVsanConfigQualifier.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicLifVsanConfigQualifier.setStatus(_A)
_CucsVnicLifVsanOperVnetDn_Type=SnmpAdminString
_CucsVnicLifVsanOperVnetDn_Object=MibTableColumn
cucsVnicLifVsanOperVnetDn=_CucsVnicLifVsanOperVnetDn_Object((1,3,6,1,4,1,9,9,719,1,53,27,1,13),_CucsVnicLifVsanOperVnetDn_Type())
cucsVnicLifVsanOperVnetDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicLifVsanOperVnetDn.setStatus(_A)
_CucsVnicLifVsanOperVnetName_Type=SnmpAdminString
_CucsVnicLifVsanOperVnetName_Object=MibTableColumn
cucsVnicLifVsanOperVnetName=_CucsVnicLifVsanOperVnetName_Object((1,3,6,1,4,1,9,9,719,1,53,27,1,14),_CucsVnicLifVsanOperVnetName_Type())
cucsVnicLifVsanOperVnetName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicLifVsanOperVnetName.setStatus(_A)
_CucsVnicLifVsanPubNwId_Type=Gauge32
_CucsVnicLifVsanPubNwId_Object=MibTableColumn
cucsVnicLifVsanPubNwId=_CucsVnicLifVsanPubNwId_Object((1,3,6,1,4,1,9,9,719,1,53,27,1,15),_CucsVnicLifVsanPubNwId_Type())
cucsVnicLifVsanPubNwId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicLifVsanPubNwId.setStatus(_A)
_CucsVnicLifVsanSharing_Type=CucsFabricVlanSharingType
_CucsVnicLifVsanSharing_Object=MibTableColumn
cucsVnicLifVsanSharing=_CucsVnicLifVsanSharing_Object((1,3,6,1,4,1,9,9,719,1,53,27,1,16),_CucsVnicLifVsanSharing_Type())
cucsVnicLifVsanSharing.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicLifVsanSharing.setStatus(_A)
_CucsVnicLifVsanOperPrimaryVnetDn_Type=SnmpAdminString
_CucsVnicLifVsanOperPrimaryVnetDn_Object=MibTableColumn
cucsVnicLifVsanOperPrimaryVnetDn=_CucsVnicLifVsanOperPrimaryVnetDn_Object((1,3,6,1,4,1,9,9,719,1,53,27,1,17),_CucsVnicLifVsanOperPrimaryVnetDn_Type())
cucsVnicLifVsanOperPrimaryVnetDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicLifVsanOperPrimaryVnetDn.setStatus(_A)
_CucsVnicLifVsanOperPrimaryVnetName_Type=SnmpAdminString
_CucsVnicLifVsanOperPrimaryVnetName_Object=MibTableColumn
cucsVnicLifVsanOperPrimaryVnetName=_CucsVnicLifVsanOperPrimaryVnetName_Object((1,3,6,1,4,1,9,9,719,1,53,27,1,18),_CucsVnicLifVsanOperPrimaryVnetName_Type())
cucsVnicLifVsanOperPrimaryVnetName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicLifVsanOperPrimaryVnetName.setStatus(_A)
_CucsVnicProfileTable_Object=MibTable
cucsVnicProfileTable=_CucsVnicProfileTable_Object((1,3,6,1,4,1,9,9,719,1,53,28))
if mibBuilder.loadTexts:cucsVnicProfileTable.setStatus(_A)
_CucsVnicProfileEntry_Object=MibTableRow
cucsVnicProfileEntry=_CucsVnicProfileEntry_Object((1,3,6,1,4,1,9,9,719,1,53,28,1))
cucsVnicProfileEntry.setIndexNames((0,_C,_f))
if mibBuilder.loadTexts:cucsVnicProfileEntry.setStatus(_A)
_CucsVnicProfileInstanceId_Type=CucsManagedObjectId
_CucsVnicProfileInstanceId_Object=MibTableColumn
cucsVnicProfileInstanceId=_CucsVnicProfileInstanceId_Object((1,3,6,1,4,1,9,9,719,1,53,28,1,1),_CucsVnicProfileInstanceId_Type())
cucsVnicProfileInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsVnicProfileInstanceId.setStatus(_A)
_CucsVnicProfileDn_Type=CucsManagedObjectDn
_CucsVnicProfileDn_Object=MibTableColumn
cucsVnicProfileDn=_CucsVnicProfileDn_Object((1,3,6,1,4,1,9,9,719,1,53,28,1,2),_CucsVnicProfileDn_Type())
cucsVnicProfileDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicProfileDn.setStatus(_A)
_CucsVnicProfileRn_Type=SnmpAdminString
_CucsVnicProfileRn_Object=MibTableColumn
cucsVnicProfileRn=_CucsVnicProfileRn_Object((1,3,6,1,4,1,9,9,719,1,53,28,1,3),_CucsVnicProfileRn_Type())
cucsVnicProfileRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicProfileRn.setStatus(_A)
_CucsVnicProfileCdp_Type=CucsNwctrlAdminState
_CucsVnicProfileCdp_Object=MibTableColumn
cucsVnicProfileCdp=_CucsVnicProfileCdp_Object((1,3,6,1,4,1,9,9,719,1,53,28,1,5),_CucsVnicProfileCdp_Type())
cucsVnicProfileCdp.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicProfileCdp.setStatus(_A)
_CucsVnicProfileCos_Type=Gauge32
_CucsVnicProfileCos_Object=MibTableColumn
cucsVnicProfileCos=_CucsVnicProfileCos_Object((1,3,6,1,4,1,9,9,719,1,53,28,1,6),_CucsVnicProfileCos_Type())
cucsVnicProfileCos.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicProfileCos.setStatus(_A)
_CucsVnicProfileDescr_Type=SnmpAdminString
_CucsVnicProfileDescr_Object=MibTableColumn
cucsVnicProfileDescr=_CucsVnicProfileDescr_Object((1,3,6,1,4,1,9,9,719,1,53,28,1,7),_CucsVnicProfileDescr_Type())
cucsVnicProfileDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicProfileDescr.setStatus(_A)
_CucsVnicProfileForgeMac_Type=CucsDpsecForgedTransmit
_CucsVnicProfileForgeMac_Object=MibTableColumn
cucsVnicProfileForgeMac=_CucsVnicProfileForgeMac_Object((1,3,6,1,4,1,9,9,719,1,53,28,1,8),_CucsVnicProfileForgeMac_Type())
cucsVnicProfileForgeMac.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicProfileForgeMac.setStatus(_A)
_CucsVnicProfileIntId_Type=SnmpAdminString
_CucsVnicProfileIntId_Object=MibTableColumn
cucsVnicProfileIntId=_CucsVnicProfileIntId_Object((1,3,6,1,4,1,9,9,719,1,53,28,1,9),_CucsVnicProfileIntId_Type())
cucsVnicProfileIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicProfileIntId.setStatus(_A)
_CucsVnicProfileMaxPorts_Type=Gauge32
_CucsVnicProfileMaxPorts_Object=MibTableColumn
cucsVnicProfileMaxPorts=_CucsVnicProfileMaxPorts_Object((1,3,6,1,4,1,9,9,719,1,53,28,1,10),_CucsVnicProfileMaxPorts_Type())
cucsVnicProfileMaxPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicProfileMaxPorts.setStatus(_A)
_CucsVnicProfileName_Type=SnmpAdminString
_CucsVnicProfileName_Object=MibTableColumn
cucsVnicProfileName=_CucsVnicProfileName_Object((1,3,6,1,4,1,9,9,719,1,53,28,1,11),_CucsVnicProfileName_Type())
cucsVnicProfileName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicProfileName.setStatus(_A)
_CucsVnicProfileNwCtrlPolicyName_Type=SnmpAdminString
_CucsVnicProfileNwCtrlPolicyName_Object=MibTableColumn
cucsVnicProfileNwCtrlPolicyName=_CucsVnicProfileNwCtrlPolicyName_Object((1,3,6,1,4,1,9,9,719,1,53,28,1,12),_CucsVnicProfileNwCtrlPolicyName_Type())
cucsVnicProfileNwCtrlPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicProfileNwCtrlPolicyName.setStatus(_A)
_CucsVnicProfileOperNwCtrlPolicyName_Type=SnmpAdminString
_CucsVnicProfileOperNwCtrlPolicyName_Object=MibTableColumn
cucsVnicProfileOperNwCtrlPolicyName=_CucsVnicProfileOperNwCtrlPolicyName_Object((1,3,6,1,4,1,9,9,719,1,53,28,1,13),_CucsVnicProfileOperNwCtrlPolicyName_Type())
cucsVnicProfileOperNwCtrlPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicProfileOperNwCtrlPolicyName.setStatus(_A)
_CucsVnicProfileOperQosPolicyName_Type=SnmpAdminString
_CucsVnicProfileOperQosPolicyName_Object=MibTableColumn
cucsVnicProfileOperQosPolicyName=_CucsVnicProfileOperQosPolicyName_Object((1,3,6,1,4,1,9,9,719,1,53,28,1,14),_CucsVnicProfileOperQosPolicyName_Type())
cucsVnicProfileOperQosPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicProfileOperQosPolicyName.setStatus(_A)
_CucsVnicProfilePinToGroupName_Type=SnmpAdminString
_CucsVnicProfilePinToGroupName_Object=MibTableColumn
cucsVnicProfilePinToGroupName=_CucsVnicProfilePinToGroupName_Object((1,3,6,1,4,1,9,9,719,1,53,28,1,15),_CucsVnicProfilePinToGroupName_Type())
cucsVnicProfilePinToGroupName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicProfilePinToGroupName.setStatus(_A)
_CucsVnicProfileQosPolicyId_Type=SnmpAdminString
_CucsVnicProfileQosPolicyId_Object=MibTableColumn
cucsVnicProfileQosPolicyId=_CucsVnicProfileQosPolicyId_Object((1,3,6,1,4,1,9,9,719,1,53,28,1,16),_CucsVnicProfileQosPolicyId_Type())
cucsVnicProfileQosPolicyId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicProfileQosPolicyId.setStatus(_A)
_CucsVnicProfileQosPolicyName_Type=SnmpAdminString
_CucsVnicProfileQosPolicyName_Object=MibTableColumn
cucsVnicProfileQosPolicyName=_CucsVnicProfileQosPolicyName_Object((1,3,6,1,4,1,9,9,719,1,53,28,1,17),_CucsVnicProfileQosPolicyName_Type())
cucsVnicProfileQosPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicProfileQosPolicyName.setStatus(_A)
_CucsVnicProfileSwABorderPort_Type=Gauge32
_CucsVnicProfileSwABorderPort_Object=MibTableColumn
cucsVnicProfileSwABorderPort=_CucsVnicProfileSwABorderPort_Object((1,3,6,1,4,1,9,9,719,1,53,28,1,19),_CucsVnicProfileSwABorderPort_Type())
cucsVnicProfileSwABorderPort.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicProfileSwABorderPort.setStatus(_A)
_CucsVnicProfileSwABorderSlot_Type=Gauge32
_CucsVnicProfileSwABorderSlot_Object=MibTableColumn
cucsVnicProfileSwABorderSlot=_CucsVnicProfileSwABorderSlot_Object((1,3,6,1,4,1,9,9,719,1,53,28,1,20),_CucsVnicProfileSwABorderSlot_Type())
cucsVnicProfileSwABorderSlot.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicProfileSwABorderSlot.setStatus(_A)
_CucsVnicProfileSwBBorderPort_Type=Gauge32
_CucsVnicProfileSwBBorderPort_Object=MibTableColumn
cucsVnicProfileSwBBorderPort=_CucsVnicProfileSwBBorderPort_Object((1,3,6,1,4,1,9,9,719,1,53,28,1,21),_CucsVnicProfileSwBBorderPort_Type())
cucsVnicProfileSwBBorderPort.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicProfileSwBBorderPort.setStatus(_A)
_CucsVnicProfileSwBBorderSlot_Type=Gauge32
_CucsVnicProfileSwBBorderSlot_Object=MibTableColumn
cucsVnicProfileSwBBorderSlot=_CucsVnicProfileSwBBorderSlot_Object((1,3,6,1,4,1,9,9,719,1,53,28,1,22),_CucsVnicProfileSwBBorderSlot_Type())
cucsVnicProfileSwBBorderSlot.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicProfileSwBBorderSlot.setStatus(_A)
_CucsVnicProfileUplinkFailAction_Type=CucsNwctrlLinkFailAction
_CucsVnicProfileUplinkFailAction_Object=MibTableColumn
cucsVnicProfileUplinkFailAction=_CucsVnicProfileUplinkFailAction_Object((1,3,6,1,4,1,9,9,719,1,53,28,1,23),_CucsVnicProfileUplinkFailAction_Type())
cucsVnicProfileUplinkFailAction.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicProfileUplinkFailAction.setStatus(_A)
_CucsVnicProfileHostNwIOPerf_Type=CucsVnicHostNwIOPerfPref
_CucsVnicProfileHostNwIOPerf_Object=MibTableColumn
cucsVnicProfileHostNwIOPerf=_CucsVnicProfileHostNwIOPerf_Object((1,3,6,1,4,1,9,9,719,1,53,28,1,24),_CucsVnicProfileHostNwIOPerf_Type())
cucsVnicProfileHostNwIOPerf.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicProfileHostNwIOPerf.setStatus(_A)
_CucsVnicProfilePrimaryVlanId_Type=Gauge32
_CucsVnicProfilePrimaryVlanId_Object=MibTableColumn
cucsVnicProfilePrimaryVlanId=_CucsVnicProfilePrimaryVlanId_Object((1,3,6,1,4,1,9,9,719,1,53,28,1,25),_CucsVnicProfilePrimaryVlanId_Type())
cucsVnicProfilePrimaryVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicProfilePrimaryVlanId.setStatus(_A)
_CucsVnicProfileQosPolicyDn_Type=SnmpAdminString
_CucsVnicProfileQosPolicyDn_Object=MibTableColumn
cucsVnicProfileQosPolicyDn=_CucsVnicProfileQosPolicyDn_Object((1,3,6,1,4,1,9,9,719,1,53,28,1,26),_CucsVnicProfileQosPolicyDn_Type())
cucsVnicProfileQosPolicyDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicProfileQosPolicyDn.setStatus(_A)
_CucsVnicProfileConfigQualifier_Type=CucsVnicProfileConfigQualifier
_CucsVnicProfileConfigQualifier_Object=MibTableColumn
cucsVnicProfileConfigQualifier=_CucsVnicProfileConfigQualifier_Object((1,3,6,1,4,1,9,9,719,1,53,28,1,27),_CucsVnicProfileConfigQualifier_Type())
cucsVnicProfileConfigQualifier.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicProfileConfigQualifier.setStatus(_A)
_CucsVnicProfileMacRegisterMode_Type=CucsNwctrlRegistrationMode
_CucsVnicProfileMacRegisterMode_Object=MibTableColumn
cucsVnicProfileMacRegisterMode=_CucsVnicProfileMacRegisterMode_Object((1,3,6,1,4,1,9,9,719,1,53,28,1,28),_CucsVnicProfileMacRegisterMode_Type())
cucsVnicProfileMacRegisterMode.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicProfileMacRegisterMode.setStatus(_A)
_CucsVnicProfilePolicyLevel_Type=Gauge32
_CucsVnicProfilePolicyLevel_Object=MibTableColumn
cucsVnicProfilePolicyLevel=_CucsVnicProfilePolicyLevel_Object((1,3,6,1,4,1,9,9,719,1,53,28,1,29),_CucsVnicProfilePolicyLevel_Type())
cucsVnicProfilePolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicProfilePolicyLevel.setStatus(_A)
_CucsVnicProfilePolicyOwner_Type=CucsPolicyPolicyOwner
_CucsVnicProfilePolicyOwner_Object=MibTableColumn
cucsVnicProfilePolicyOwner=_CucsVnicProfilePolicyOwner_Object((1,3,6,1,4,1,9,9,719,1,53,28,1,30),_CucsVnicProfilePolicyOwner_Type())
cucsVnicProfilePolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicProfilePolicyOwner.setStatus(_A)
_CucsVnicProfilePortProfileUuid_Type=SnmpAdminString
_CucsVnicProfilePortProfileUuid_Object=MibTableColumn
cucsVnicProfilePortProfileUuid=_CucsVnicProfilePortProfileUuid_Object((1,3,6,1,4,1,9,9,719,1,53,28,1,31),_CucsVnicProfilePortProfileUuid_Type())
cucsVnicProfilePortProfileUuid.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicProfilePortProfileUuid.setStatus(_A)
_CucsVnicProfileType_Type=CucsVnicPortProfileType
_CucsVnicProfileType_Object=MibTableColumn
cucsVnicProfileType=_CucsVnicProfileType_Object((1,3,6,1,4,1,9,9,719,1,53,28,1,32),_CucsVnicProfileType_Type())
cucsVnicProfileType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicProfileType.setStatus(_A)
_CucsVnicProfileSwABorderAggrPort_Type=Gauge32
_CucsVnicProfileSwABorderAggrPort_Object=MibTableColumn
cucsVnicProfileSwABorderAggrPort=_CucsVnicProfileSwABorderAggrPort_Object((1,3,6,1,4,1,9,9,719,1,53,28,1,33),_CucsVnicProfileSwABorderAggrPort_Type())
cucsVnicProfileSwABorderAggrPort.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicProfileSwABorderAggrPort.setStatus(_A)
_CucsVnicProfileSwBBorderAggrPort_Type=Gauge32
_CucsVnicProfileSwBBorderAggrPort_Object=MibTableColumn
cucsVnicProfileSwBBorderAggrPort=_CucsVnicProfileSwBBorderAggrPort_Object((1,3,6,1,4,1,9,9,719,1,53,28,1,34),_CucsVnicProfileSwBBorderAggrPort_Type())
cucsVnicProfileSwBBorderAggrPort.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicProfileSwBBorderAggrPort.setStatus(_A)
_CucsVnicProfileLldp_Type=CucsNwctrlLldpAdminStateBitmask
_CucsVnicProfileLldp_Object=MibTableColumn
cucsVnicProfileLldp=_CucsVnicProfileLldp_Object((1,3,6,1,4,1,9,9,719,1,53,28,1,35),_CucsVnicProfileLldp_Type())
cucsVnicProfileLldp.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicProfileLldp.setStatus(_A)
_CucsVnicProfileAliasTable_Object=MibTable
cucsVnicProfileAliasTable=_CucsVnicProfileAliasTable_Object((1,3,6,1,4,1,9,9,719,1,53,29))
if mibBuilder.loadTexts:cucsVnicProfileAliasTable.setStatus(_A)
_CucsVnicProfileAliasEntry_Object=MibTableRow
cucsVnicProfileAliasEntry=_CucsVnicProfileAliasEntry_Object((1,3,6,1,4,1,9,9,719,1,53,29,1))
cucsVnicProfileAliasEntry.setIndexNames((0,_C,_g))
if mibBuilder.loadTexts:cucsVnicProfileAliasEntry.setStatus(_A)
_CucsVnicProfileAliasInstanceId_Type=CucsManagedObjectId
_CucsVnicProfileAliasInstanceId_Object=MibTableColumn
cucsVnicProfileAliasInstanceId=_CucsVnicProfileAliasInstanceId_Object((1,3,6,1,4,1,9,9,719,1,53,29,1,1),_CucsVnicProfileAliasInstanceId_Type())
cucsVnicProfileAliasInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsVnicProfileAliasInstanceId.setStatus(_A)
_CucsVnicProfileAliasDn_Type=CucsManagedObjectDn
_CucsVnicProfileAliasDn_Object=MibTableColumn
cucsVnicProfileAliasDn=_CucsVnicProfileAliasDn_Object((1,3,6,1,4,1,9,9,719,1,53,29,1,2),_CucsVnicProfileAliasDn_Type())
cucsVnicProfileAliasDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicProfileAliasDn.setStatus(_A)
_CucsVnicProfileAliasRn_Type=SnmpAdminString
_CucsVnicProfileAliasRn_Object=MibTableColumn
cucsVnicProfileAliasRn=_CucsVnicProfileAliasRn_Object((1,3,6,1,4,1,9,9,719,1,53,29,1,3),_CucsVnicProfileAliasRn_Type())
cucsVnicProfileAliasRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicProfileAliasRn.setStatus(_A)
_CucsVnicProfileAliasAlias_Type=SnmpAdminString
_CucsVnicProfileAliasAlias_Object=MibTableColumn
cucsVnicProfileAliasAlias=_CucsVnicProfileAliasAlias_Object((1,3,6,1,4,1,9,9,719,1,53,29,1,4),_CucsVnicProfileAliasAlias_Type())
cucsVnicProfileAliasAlias.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicProfileAliasAlias.setStatus(_A)
_CucsVnicProfileAliasSwUuid_Type=SnmpAdminString
_CucsVnicProfileAliasSwUuid_Object=MibTableColumn
cucsVnicProfileAliasSwUuid=_CucsVnicProfileAliasSwUuid_Object((1,3,6,1,4,1,9,9,719,1,53,29,1,5),_CucsVnicProfileAliasSwUuid_Type())
cucsVnicProfileAliasSwUuid.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicProfileAliasSwUuid.setStatus(_A)
_CucsVnicProfileSetTable_Object=MibTable
cucsVnicProfileSetTable=_CucsVnicProfileSetTable_Object((1,3,6,1,4,1,9,9,719,1,53,30))
if mibBuilder.loadTexts:cucsVnicProfileSetTable.setStatus(_A)
_CucsVnicProfileSetEntry_Object=MibTableRow
cucsVnicProfileSetEntry=_CucsVnicProfileSetEntry_Object((1,3,6,1,4,1,9,9,719,1,53,30,1))
cucsVnicProfileSetEntry.setIndexNames((0,_C,_h))
if mibBuilder.loadTexts:cucsVnicProfileSetEntry.setStatus(_A)
_CucsVnicProfileSetInstanceId_Type=CucsManagedObjectId
_CucsVnicProfileSetInstanceId_Object=MibTableColumn
cucsVnicProfileSetInstanceId=_CucsVnicProfileSetInstanceId_Object((1,3,6,1,4,1,9,9,719,1,53,30,1,1),_CucsVnicProfileSetInstanceId_Type())
cucsVnicProfileSetInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsVnicProfileSetInstanceId.setStatus(_A)
_CucsVnicProfileSetDn_Type=CucsManagedObjectDn
_CucsVnicProfileSetDn_Object=MibTableColumn
cucsVnicProfileSetDn=_CucsVnicProfileSetDn_Object((1,3,6,1,4,1,9,9,719,1,53,30,1,2),_CucsVnicProfileSetDn_Type())
cucsVnicProfileSetDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicProfileSetDn.setStatus(_A)
_CucsVnicProfileSetRn_Type=SnmpAdminString
_CucsVnicProfileSetRn_Object=MibTableColumn
cucsVnicProfileSetRn=_CucsVnicProfileSetRn_Object((1,3,6,1,4,1,9,9,719,1,53,30,1,3),_CucsVnicProfileSetRn_Type())
cucsVnicProfileSetRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicProfileSetRn.setStatus(_A)
_CucsVnicProfileSetFsmDescr_Type=SnmpAdminString
_CucsVnicProfileSetFsmDescr_Object=MibTableColumn
cucsVnicProfileSetFsmDescr=_CucsVnicProfileSetFsmDescr_Object((1,3,6,1,4,1,9,9,719,1,53,30,1,4),_CucsVnicProfileSetFsmDescr_Type())
cucsVnicProfileSetFsmDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicProfileSetFsmDescr.setStatus(_A)
_CucsVnicProfileSetFsmPrev_Type=SnmpAdminString
_CucsVnicProfileSetFsmPrev_Object=MibTableColumn
cucsVnicProfileSetFsmPrev=_CucsVnicProfileSetFsmPrev_Object((1,3,6,1,4,1,9,9,719,1,53,30,1,5),_CucsVnicProfileSetFsmPrev_Type())
cucsVnicProfileSetFsmPrev.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicProfileSetFsmPrev.setStatus(_A)
_CucsVnicProfileSetFsmProgr_Type=Gauge32
_CucsVnicProfileSetFsmProgr_Object=MibTableColumn
cucsVnicProfileSetFsmProgr=_CucsVnicProfileSetFsmProgr_Object((1,3,6,1,4,1,9,9,719,1,53,30,1,6),_CucsVnicProfileSetFsmProgr_Type())
cucsVnicProfileSetFsmProgr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicProfileSetFsmProgr.setStatus(_A)
_CucsVnicProfileSetFsmRmtInvErrCode_Type=Gauge32
_CucsVnicProfileSetFsmRmtInvErrCode_Object=MibTableColumn
cucsVnicProfileSetFsmRmtInvErrCode=_CucsVnicProfileSetFsmRmtInvErrCode_Object((1,3,6,1,4,1,9,9,719,1,53,30,1,7),_CucsVnicProfileSetFsmRmtInvErrCode_Type())
cucsVnicProfileSetFsmRmtInvErrCode.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicProfileSetFsmRmtInvErrCode.setStatus(_A)
_CucsVnicProfileSetFsmRmtInvErrDescr_Type=SnmpAdminString
_CucsVnicProfileSetFsmRmtInvErrDescr_Object=MibTableColumn
cucsVnicProfileSetFsmRmtInvErrDescr=_CucsVnicProfileSetFsmRmtInvErrDescr_Object((1,3,6,1,4,1,9,9,719,1,53,30,1,8),_CucsVnicProfileSetFsmRmtInvErrDescr_Type())
cucsVnicProfileSetFsmRmtInvErrDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicProfileSetFsmRmtInvErrDescr.setStatus(_A)
_CucsVnicProfileSetFsmRmtInvRslt_Type=CucsConditionRemoteInvRslt
_CucsVnicProfileSetFsmRmtInvRslt_Object=MibTableColumn
cucsVnicProfileSetFsmRmtInvRslt=_CucsVnicProfileSetFsmRmtInvRslt_Object((1,3,6,1,4,1,9,9,719,1,53,30,1,9),_CucsVnicProfileSetFsmRmtInvRslt_Type())
cucsVnicProfileSetFsmRmtInvRslt.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicProfileSetFsmRmtInvRslt.setStatus(_A)
_CucsVnicProfileSetFsmStageDescr_Type=SnmpAdminString
_CucsVnicProfileSetFsmStageDescr_Object=MibTableColumn
cucsVnicProfileSetFsmStageDescr=_CucsVnicProfileSetFsmStageDescr_Object((1,3,6,1,4,1,9,9,719,1,53,30,1,10),_CucsVnicProfileSetFsmStageDescr_Type())
cucsVnicProfileSetFsmStageDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicProfileSetFsmStageDescr.setStatus(_A)
_CucsVnicProfileSetFsmStamp_Type=DateAndTime
_CucsVnicProfileSetFsmStamp_Object=MibTableColumn
cucsVnicProfileSetFsmStamp=_CucsVnicProfileSetFsmStamp_Object((1,3,6,1,4,1,9,9,719,1,53,30,1,11),_CucsVnicProfileSetFsmStamp_Type())
cucsVnicProfileSetFsmStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicProfileSetFsmStamp.setStatus(_A)
_CucsVnicProfileSetFsmStatus_Type=SnmpAdminString
_CucsVnicProfileSetFsmStatus_Object=MibTableColumn
cucsVnicProfileSetFsmStatus=_CucsVnicProfileSetFsmStatus_Object((1,3,6,1,4,1,9,9,719,1,53,30,1,12),_CucsVnicProfileSetFsmStatus_Type())
cucsVnicProfileSetFsmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicProfileSetFsmStatus.setStatus(_A)
_CucsVnicProfileSetFsmTry_Type=Gauge32
_CucsVnicProfileSetFsmTry_Object=MibTableColumn
cucsVnicProfileSetFsmTry=_CucsVnicProfileSetFsmTry_Object((1,3,6,1,4,1,9,9,719,1,53,30,1,13),_CucsVnicProfileSetFsmTry_Type())
cucsVnicProfileSetFsmTry.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicProfileSetFsmTry.setStatus(_A)
_CucsVnicProfileSetFltAggr_Type=Unsigned64
_CucsVnicProfileSetFltAggr_Object=MibTableColumn
cucsVnicProfileSetFltAggr=_CucsVnicProfileSetFltAggr_Object((1,3,6,1,4,1,9,9,719,1,53,30,1,14),_CucsVnicProfileSetFltAggr_Type())
cucsVnicProfileSetFltAggr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicProfileSetFltAggr.setStatus(_A)
_CucsVnicProfileSetGenNum_Type=Gauge32
_CucsVnicProfileSetGenNum_Object=MibTableColumn
cucsVnicProfileSetGenNum=_CucsVnicProfileSetGenNum_Object((1,3,6,1,4,1,9,9,719,1,53,30,1,15),_CucsVnicProfileSetGenNum_Type())
cucsVnicProfileSetGenNum.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicProfileSetGenNum.setStatus(_A)
_CucsVnicProfileSetVlanGroupUpdate_Type=CucsVnicVlanGroupUpdate
_CucsVnicProfileSetVlanGroupUpdate_Object=MibTableColumn
cucsVnicProfileSetVlanGroupUpdate=_CucsVnicProfileSetVlanGroupUpdate_Object((1,3,6,1,4,1,9,9,719,1,53,30,1,16),_CucsVnicProfileSetVlanGroupUpdate_Type())
cucsVnicProfileSetVlanGroupUpdate.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicProfileSetVlanGroupUpdate.setStatus(_A)
_CucsVnicProfileSetFsmTaskTable_Object=MibTable
cucsVnicProfileSetFsmTaskTable=_CucsVnicProfileSetFsmTaskTable_Object((1,3,6,1,4,1,9,9,719,1,53,31))
if mibBuilder.loadTexts:cucsVnicProfileSetFsmTaskTable.setStatus(_A)
_CucsVnicProfileSetFsmTaskEntry_Object=MibTableRow
cucsVnicProfileSetFsmTaskEntry=_CucsVnicProfileSetFsmTaskEntry_Object((1,3,6,1,4,1,9,9,719,1,53,31,1))
cucsVnicProfileSetFsmTaskEntry.setIndexNames((0,_C,_i))
if mibBuilder.loadTexts:cucsVnicProfileSetFsmTaskEntry.setStatus(_A)
_CucsVnicProfileSetFsmTaskInstanceId_Type=CucsManagedObjectId
_CucsVnicProfileSetFsmTaskInstanceId_Object=MibTableColumn
cucsVnicProfileSetFsmTaskInstanceId=_CucsVnicProfileSetFsmTaskInstanceId_Object((1,3,6,1,4,1,9,9,719,1,53,31,1,1),_CucsVnicProfileSetFsmTaskInstanceId_Type())
cucsVnicProfileSetFsmTaskInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsVnicProfileSetFsmTaskInstanceId.setStatus(_A)
_CucsVnicProfileSetFsmTaskDn_Type=CucsManagedObjectDn
_CucsVnicProfileSetFsmTaskDn_Object=MibTableColumn
cucsVnicProfileSetFsmTaskDn=_CucsVnicProfileSetFsmTaskDn_Object((1,3,6,1,4,1,9,9,719,1,53,31,1,2),_CucsVnicProfileSetFsmTaskDn_Type())
cucsVnicProfileSetFsmTaskDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicProfileSetFsmTaskDn.setStatus(_A)
_CucsVnicProfileSetFsmTaskRn_Type=SnmpAdminString
_CucsVnicProfileSetFsmTaskRn_Object=MibTableColumn
cucsVnicProfileSetFsmTaskRn=_CucsVnicProfileSetFsmTaskRn_Object((1,3,6,1,4,1,9,9,719,1,53,31,1,3),_CucsVnicProfileSetFsmTaskRn_Type())
cucsVnicProfileSetFsmTaskRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicProfileSetFsmTaskRn.setStatus(_A)
_CucsVnicProfileSetFsmTaskCompletion_Type=CucsFsmCompletion
_CucsVnicProfileSetFsmTaskCompletion_Object=MibTableColumn
cucsVnicProfileSetFsmTaskCompletion=_CucsVnicProfileSetFsmTaskCompletion_Object((1,3,6,1,4,1,9,9,719,1,53,31,1,4),_CucsVnicProfileSetFsmTaskCompletion_Type())
cucsVnicProfileSetFsmTaskCompletion.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicProfileSetFsmTaskCompletion.setStatus(_A)
_CucsVnicProfileSetFsmTaskFlags_Type=CucsFsmFlags
_CucsVnicProfileSetFsmTaskFlags_Object=MibTableColumn
cucsVnicProfileSetFsmTaskFlags=_CucsVnicProfileSetFsmTaskFlags_Object((1,3,6,1,4,1,9,9,719,1,53,31,1,5),_CucsVnicProfileSetFsmTaskFlags_Type())
cucsVnicProfileSetFsmTaskFlags.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicProfileSetFsmTaskFlags.setStatus(_A)
_CucsVnicProfileSetFsmTaskItem_Type=CucsVnicProfileSetFsmTaskItem
_CucsVnicProfileSetFsmTaskItem_Object=MibTableColumn
cucsVnicProfileSetFsmTaskItem=_CucsVnicProfileSetFsmTaskItem_Object((1,3,6,1,4,1,9,9,719,1,53,31,1,6),_CucsVnicProfileSetFsmTaskItem_Type())
cucsVnicProfileSetFsmTaskItem.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicProfileSetFsmTaskItem.setStatus(_A)
_CucsVnicProfileSetFsmTaskSeqId_Type=Gauge32
_CucsVnicProfileSetFsmTaskSeqId_Object=MibTableColumn
cucsVnicProfileSetFsmTaskSeqId=_CucsVnicProfileSetFsmTaskSeqId_Object((1,3,6,1,4,1,9,9,719,1,53,31,1,7),_CucsVnicProfileSetFsmTaskSeqId_Type())
cucsVnicProfileSetFsmTaskSeqId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicProfileSetFsmTaskSeqId.setStatus(_A)
_CucsVnicSanConnTemplTable_Object=MibTable
cucsVnicSanConnTemplTable=_CucsVnicSanConnTemplTable_Object((1,3,6,1,4,1,9,9,719,1,53,32))
if mibBuilder.loadTexts:cucsVnicSanConnTemplTable.setStatus(_A)
_CucsVnicSanConnTemplEntry_Object=MibTableRow
cucsVnicSanConnTemplEntry=_CucsVnicSanConnTemplEntry_Object((1,3,6,1,4,1,9,9,719,1,53,32,1))
cucsVnicSanConnTemplEntry.setIndexNames((0,_C,_j))
if mibBuilder.loadTexts:cucsVnicSanConnTemplEntry.setStatus(_A)
_CucsVnicSanConnTemplInstanceId_Type=CucsManagedObjectId
_CucsVnicSanConnTemplInstanceId_Object=MibTableColumn
cucsVnicSanConnTemplInstanceId=_CucsVnicSanConnTemplInstanceId_Object((1,3,6,1,4,1,9,9,719,1,53,32,1,1),_CucsVnicSanConnTemplInstanceId_Type())
cucsVnicSanConnTemplInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsVnicSanConnTemplInstanceId.setStatus(_A)
_CucsVnicSanConnTemplDn_Type=CucsManagedObjectDn
_CucsVnicSanConnTemplDn_Object=MibTableColumn
cucsVnicSanConnTemplDn=_CucsVnicSanConnTemplDn_Object((1,3,6,1,4,1,9,9,719,1,53,32,1,2),_CucsVnicSanConnTemplDn_Type())
cucsVnicSanConnTemplDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicSanConnTemplDn.setStatus(_A)
_CucsVnicSanConnTemplRn_Type=SnmpAdminString
_CucsVnicSanConnTemplRn_Object=MibTableColumn
cucsVnicSanConnTemplRn=_CucsVnicSanConnTemplRn_Object((1,3,6,1,4,1,9,9,719,1,53,32,1,3),_CucsVnicSanConnTemplRn_Type())
cucsVnicSanConnTemplRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicSanConnTemplRn.setStatus(_A)
_CucsVnicSanConnTemplDescr_Type=SnmpAdminString
_CucsVnicSanConnTemplDescr_Object=MibTableColumn
cucsVnicSanConnTemplDescr=_CucsVnicSanConnTemplDescr_Object((1,3,6,1,4,1,9,9,719,1,53,32,1,4),_CucsVnicSanConnTemplDescr_Type())
cucsVnicSanConnTemplDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicSanConnTemplDescr.setStatus(_A)
_CucsVnicSanConnTemplIdentPoolName_Type=SnmpAdminString
_CucsVnicSanConnTemplIdentPoolName_Object=MibTableColumn
cucsVnicSanConnTemplIdentPoolName=_CucsVnicSanConnTemplIdentPoolName_Object((1,3,6,1,4,1,9,9,719,1,53,32,1,5),_CucsVnicSanConnTemplIdentPoolName_Type())
cucsVnicSanConnTemplIdentPoolName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicSanConnTemplIdentPoolName.setStatus(_A)
_CucsVnicSanConnTemplIntId_Type=SnmpAdminString
_CucsVnicSanConnTemplIntId_Object=MibTableColumn
cucsVnicSanConnTemplIntId=_CucsVnicSanConnTemplIntId_Object((1,3,6,1,4,1,9,9,719,1,53,32,1,6),_CucsVnicSanConnTemplIntId_Type())
cucsVnicSanConnTemplIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicSanConnTemplIntId.setStatus(_A)
_CucsVnicSanConnTemplMaxDataFieldSize_Type=Gauge32
_CucsVnicSanConnTemplMaxDataFieldSize_Object=MibTableColumn
cucsVnicSanConnTemplMaxDataFieldSize=_CucsVnicSanConnTemplMaxDataFieldSize_Object((1,3,6,1,4,1,9,9,719,1,53,32,1,7),_CucsVnicSanConnTemplMaxDataFieldSize_Type())
cucsVnicSanConnTemplMaxDataFieldSize.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicSanConnTemplMaxDataFieldSize.setStatus(_A)
_CucsVnicSanConnTemplName_Type=SnmpAdminString
_CucsVnicSanConnTemplName_Object=MibTableColumn
cucsVnicSanConnTemplName=_CucsVnicSanConnTemplName_Object((1,3,6,1,4,1,9,9,719,1,53,32,1,8),_CucsVnicSanConnTemplName_Type())
cucsVnicSanConnTemplName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicSanConnTemplName.setStatus(_A)
_CucsVnicSanConnTemplNwCtrlPolicyName_Type=SnmpAdminString
_CucsVnicSanConnTemplNwCtrlPolicyName_Object=MibTableColumn
cucsVnicSanConnTemplNwCtrlPolicyName=_CucsVnicSanConnTemplNwCtrlPolicyName_Object((1,3,6,1,4,1,9,9,719,1,53,32,1,9),_CucsVnicSanConnTemplNwCtrlPolicyName_Type())
cucsVnicSanConnTemplNwCtrlPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicSanConnTemplNwCtrlPolicyName.setStatus(_A)
_CucsVnicSanConnTemplOperIdentPoolName_Type=SnmpAdminString
_CucsVnicSanConnTemplOperIdentPoolName_Object=MibTableColumn
cucsVnicSanConnTemplOperIdentPoolName=_CucsVnicSanConnTemplOperIdentPoolName_Object((1,3,6,1,4,1,9,9,719,1,53,32,1,10),_CucsVnicSanConnTemplOperIdentPoolName_Type())
cucsVnicSanConnTemplOperIdentPoolName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicSanConnTemplOperIdentPoolName.setStatus(_A)
_CucsVnicSanConnTemplOperQosPolicyName_Type=SnmpAdminString
_CucsVnicSanConnTemplOperQosPolicyName_Object=MibTableColumn
cucsVnicSanConnTemplOperQosPolicyName=_CucsVnicSanConnTemplOperQosPolicyName_Object((1,3,6,1,4,1,9,9,719,1,53,32,1,11),_CucsVnicSanConnTemplOperQosPolicyName_Type())
cucsVnicSanConnTemplOperQosPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicSanConnTemplOperQosPolicyName.setStatus(_A)
_CucsVnicSanConnTemplOperStatsPolicyName_Type=SnmpAdminString
_CucsVnicSanConnTemplOperStatsPolicyName_Object=MibTableColumn
cucsVnicSanConnTemplOperStatsPolicyName=_CucsVnicSanConnTemplOperStatsPolicyName_Object((1,3,6,1,4,1,9,9,719,1,53,32,1,12),_CucsVnicSanConnTemplOperStatsPolicyName_Type())
cucsVnicSanConnTemplOperStatsPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicSanConnTemplOperStatsPolicyName.setStatus(_A)
_CucsVnicSanConnTemplPinToGroupName_Type=SnmpAdminString
_CucsVnicSanConnTemplPinToGroupName_Object=MibTableColumn
cucsVnicSanConnTemplPinToGroupName=_CucsVnicSanConnTemplPinToGroupName_Object((1,3,6,1,4,1,9,9,719,1,53,32,1,13),_CucsVnicSanConnTemplPinToGroupName_Type())
cucsVnicSanConnTemplPinToGroupName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicSanConnTemplPinToGroupName.setStatus(_A)
_CucsVnicSanConnTemplQosPolicyName_Type=SnmpAdminString
_CucsVnicSanConnTemplQosPolicyName_Object=MibTableColumn
cucsVnicSanConnTemplQosPolicyName=_CucsVnicSanConnTemplQosPolicyName_Object((1,3,6,1,4,1,9,9,719,1,53,32,1,14),_CucsVnicSanConnTemplQosPolicyName_Type())
cucsVnicSanConnTemplQosPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicSanConnTemplQosPolicyName.setStatus(_A)
_CucsVnicSanConnTemplStatsPolicyName_Type=SnmpAdminString
_CucsVnicSanConnTemplStatsPolicyName_Object=MibTableColumn
cucsVnicSanConnTemplStatsPolicyName=_CucsVnicSanConnTemplStatsPolicyName_Object((1,3,6,1,4,1,9,9,719,1,53,32,1,15),_CucsVnicSanConnTemplStatsPolicyName_Type())
cucsVnicSanConnTemplStatsPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicSanConnTemplStatsPolicyName.setStatus(_A)
_CucsVnicSanConnTemplSwitchId_Type=CucsNetworkSwitchId
_CucsVnicSanConnTemplSwitchId_Object=MibTableColumn
cucsVnicSanConnTemplSwitchId=_CucsVnicSanConnTemplSwitchId_Object((1,3,6,1,4,1,9,9,719,1,53,32,1,16),_CucsVnicSanConnTemplSwitchId_Type())
cucsVnicSanConnTemplSwitchId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicSanConnTemplSwitchId.setStatus(_A)
_CucsVnicSanConnTemplTarget_Type=CucsVnicSanConnTemplTarget
_CucsVnicSanConnTemplTarget_Object=MibTableColumn
cucsVnicSanConnTemplTarget=_CucsVnicSanConnTemplTarget_Object((1,3,6,1,4,1,9,9,719,1,53,32,1,17),_CucsVnicSanConnTemplTarget_Type())
cucsVnicSanConnTemplTarget.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicSanConnTemplTarget.setStatus(_A)
_CucsVnicSanConnTemplTemplType_Type=CucsVnicTemplateType
_CucsVnicSanConnTemplTemplType_Object=MibTableColumn
cucsVnicSanConnTemplTemplType=_CucsVnicSanConnTemplTemplType_Object((1,3,6,1,4,1,9,9,719,1,53,32,1,18),_CucsVnicSanConnTemplTemplType_Type())
cucsVnicSanConnTemplTemplType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicSanConnTemplTemplType.setStatus(_A)
_CucsVnicSanConnTemplPolicyLevel_Type=Gauge32
_CucsVnicSanConnTemplPolicyLevel_Object=MibTableColumn
cucsVnicSanConnTemplPolicyLevel=_CucsVnicSanConnTemplPolicyLevel_Object((1,3,6,1,4,1,9,9,719,1,53,32,1,19),_CucsVnicSanConnTemplPolicyLevel_Type())
cucsVnicSanConnTemplPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicSanConnTemplPolicyLevel.setStatus(_A)
_CucsVnicSanConnTemplPolicyOwner_Type=CucsPolicyPolicyOwner
_CucsVnicSanConnTemplPolicyOwner_Object=MibTableColumn
cucsVnicSanConnTemplPolicyOwner=_CucsVnicSanConnTemplPolicyOwner_Object((1,3,6,1,4,1,9,9,719,1,53,32,1,20),_CucsVnicSanConnTemplPolicyOwner_Type())
cucsVnicSanConnTemplPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicSanConnTemplPolicyOwner.setStatus(_A)
_CucsVnicSanConnTemplOperPeerRedundancyTemplName_Type=SnmpAdminString
_CucsVnicSanConnTemplOperPeerRedundancyTemplName_Object=MibTableColumn
cucsVnicSanConnTemplOperPeerRedundancyTemplName=_CucsVnicSanConnTemplOperPeerRedundancyTemplName_Object((1,3,6,1,4,1,9,9,719,1,53,32,1,21),_CucsVnicSanConnTemplOperPeerRedundancyTemplName_Type())
cucsVnicSanConnTemplOperPeerRedundancyTemplName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicSanConnTemplOperPeerRedundancyTemplName.setStatus(_A)
_CucsVnicSanConnTemplPeerRedundancyTemplName_Type=SnmpAdminString
_CucsVnicSanConnTemplPeerRedundancyTemplName_Object=MibTableColumn
cucsVnicSanConnTemplPeerRedundancyTemplName=_CucsVnicSanConnTemplPeerRedundancyTemplName_Object((1,3,6,1,4,1,9,9,719,1,53,32,1,22),_CucsVnicSanConnTemplPeerRedundancyTemplName_Type())
cucsVnicSanConnTemplPeerRedundancyTemplName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicSanConnTemplPeerRedundancyTemplName.setStatus(_A)
_CucsVnicSanConnTemplRedundancyPairType_Type=CucsVnicRedundancyPairType
_CucsVnicSanConnTemplRedundancyPairType_Object=MibTableColumn
cucsVnicSanConnTemplRedundancyPairType=_CucsVnicSanConnTemplRedundancyPairType_Object((1,3,6,1,4,1,9,9,719,1,53,32,1,23),_CucsVnicSanConnTemplRedundancyPairType_Type())
cucsVnicSanConnTemplRedundancyPairType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicSanConnTemplRedundancyPairType.setStatus(_A)
_CucsVnicScsiTable_Object=MibTable
cucsVnicScsiTable=_CucsVnicScsiTable_Object((1,3,6,1,4,1,9,9,719,1,53,33))
if mibBuilder.loadTexts:cucsVnicScsiTable.setStatus(_A)
_CucsVnicScsiEntry_Object=MibTableRow
cucsVnicScsiEntry=_CucsVnicScsiEntry_Object((1,3,6,1,4,1,9,9,719,1,53,33,1))
cucsVnicScsiEntry.setIndexNames((0,_C,_k))
if mibBuilder.loadTexts:cucsVnicScsiEntry.setStatus(_A)
_CucsVnicScsiInstanceId_Type=CucsManagedObjectId
_CucsVnicScsiInstanceId_Object=MibTableColumn
cucsVnicScsiInstanceId=_CucsVnicScsiInstanceId_Object((1,3,6,1,4,1,9,9,719,1,53,33,1,1),_CucsVnicScsiInstanceId_Type())
cucsVnicScsiInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsVnicScsiInstanceId.setStatus(_A)
_CucsVnicScsiDn_Type=CucsManagedObjectDn
_CucsVnicScsiDn_Object=MibTableColumn
cucsVnicScsiDn=_CucsVnicScsiDn_Object((1,3,6,1,4,1,9,9,719,1,53,33,1,2),_CucsVnicScsiDn_Type())
cucsVnicScsiDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicScsiDn.setStatus(_A)
_CucsVnicScsiRn_Type=SnmpAdminString
_CucsVnicScsiRn_Object=MibTableColumn
cucsVnicScsiRn=_CucsVnicScsiRn_Object((1,3,6,1,4,1,9,9,719,1,53,33,1,3),_CucsVnicScsiRn_Type())
cucsVnicScsiRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicScsiRn.setStatus(_A)
_CucsVnicScsiAdaptorProfileName_Type=SnmpAdminString
_CucsVnicScsiAdaptorProfileName_Object=MibTableColumn
cucsVnicScsiAdaptorProfileName=_CucsVnicScsiAdaptorProfileName_Object((1,3,6,1,4,1,9,9,719,1,53,33,1,4),_CucsVnicScsiAdaptorProfileName_Type())
cucsVnicScsiAdaptorProfileName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicScsiAdaptorProfileName.setStatus(_A)
_CucsVnicScsiAdminVcon_Type=SnmpAdminString
_CucsVnicScsiAdminVcon_Object=MibTableColumn
cucsVnicScsiAdminVcon=_CucsVnicScsiAdminVcon_Object((1,3,6,1,4,1,9,9,719,1,53,33,1,5),_CucsVnicScsiAdminVcon_Type())
cucsVnicScsiAdminVcon.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicScsiAdminVcon.setStatus(_A)
_CucsVnicScsiBootDev_Type=CucsVnicVnicBootDev
_CucsVnicScsiBootDev_Object=MibTableColumn
cucsVnicScsiBootDev=_CucsVnicScsiBootDev_Object((1,3,6,1,4,1,9,9,719,1,53,33,1,6),_CucsVnicScsiBootDev_Type())
cucsVnicScsiBootDev.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicScsiBootDev.setStatus(_A)
_CucsVnicScsiConfigState_Type=CucsLsConfigState
_CucsVnicScsiConfigState_Object=MibTableColumn
cucsVnicScsiConfigState=_CucsVnicScsiConfigState_Object((1,3,6,1,4,1,9,9,719,1,53,33,1,7),_CucsVnicScsiConfigState_Type())
cucsVnicScsiConfigState.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicScsiConfigState.setStatus(_A)
_CucsVnicScsiEquipmentDn_Type=SnmpAdminString
_CucsVnicScsiEquipmentDn_Object=MibTableColumn
cucsVnicScsiEquipmentDn=_CucsVnicScsiEquipmentDn_Object((1,3,6,1,4,1,9,9,719,1,53,33,1,8),_CucsVnicScsiEquipmentDn_Type())
cucsVnicScsiEquipmentDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicScsiEquipmentDn.setStatus(_A)
_CucsVnicScsiIdentPoolName_Type=SnmpAdminString
_CucsVnicScsiIdentPoolName_Object=MibTableColumn
cucsVnicScsiIdentPoolName=_CucsVnicScsiIdentPoolName_Object((1,3,6,1,4,1,9,9,719,1,53,33,1,9),_CucsVnicScsiIdentPoolName_Type())
cucsVnicScsiIdentPoolName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicScsiIdentPoolName.setStatus(_A)
_CucsVnicScsiInstType_Type=CucsVnicInstantiation
_CucsVnicScsiInstType_Object=MibTableColumn
cucsVnicScsiInstType=_CucsVnicScsiInstType_Object((1,3,6,1,4,1,9,9,719,1,53,33,1,10),_CucsVnicScsiInstType_Type())
cucsVnicScsiInstType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicScsiInstType.setStatus(_A)
_CucsVnicScsiName_Type=SnmpAdminString
_CucsVnicScsiName_Object=MibTableColumn
cucsVnicScsiName=_CucsVnicScsiName_Object((1,3,6,1,4,1,9,9,719,1,53,33,1,11),_CucsVnicScsiName_Type())
cucsVnicScsiName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicScsiName.setStatus(_A)
_CucsVnicScsiNwTemplName_Type=SnmpAdminString
_CucsVnicScsiNwTemplName_Object=MibTableColumn
cucsVnicScsiNwTemplName=_CucsVnicScsiNwTemplName_Object((1,3,6,1,4,1,9,9,719,1,53,33,1,12),_CucsVnicScsiNwTemplName_Type())
cucsVnicScsiNwTemplName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicScsiNwTemplName.setStatus(_A)
_CucsVnicScsiOperOrder_Type=Gauge32
_CucsVnicScsiOperOrder_Object=MibTableColumn
cucsVnicScsiOperOrder=_CucsVnicScsiOperOrder_Object((1,3,6,1,4,1,9,9,719,1,53,33,1,13),_CucsVnicScsiOperOrder_Type())
cucsVnicScsiOperOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicScsiOperOrder.setStatus(_A)
_CucsVnicScsiOperSpeed_Type=Gauge32
_CucsVnicScsiOperSpeed_Object=MibTableColumn
cucsVnicScsiOperSpeed=_CucsVnicScsiOperSpeed_Object((1,3,6,1,4,1,9,9,719,1,53,33,1,14),_CucsVnicScsiOperSpeed_Type())
cucsVnicScsiOperSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicScsiOperSpeed.setStatus(_A)
_CucsVnicScsiOperStatsPolicyName_Type=SnmpAdminString
_CucsVnicScsiOperStatsPolicyName_Object=MibTableColumn
cucsVnicScsiOperStatsPolicyName=_CucsVnicScsiOperStatsPolicyName_Object((1,3,6,1,4,1,9,9,719,1,53,33,1,15),_CucsVnicScsiOperStatsPolicyName_Type())
cucsVnicScsiOperStatsPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicScsiOperStatsPolicyName.setStatus(_A)
_CucsVnicScsiOperVcon_Type=SnmpAdminString
_CucsVnicScsiOperVcon_Object=MibTableColumn
cucsVnicScsiOperVcon=_CucsVnicScsiOperVcon_Object((1,3,6,1,4,1,9,9,719,1,53,33,1,16),_CucsVnicScsiOperVcon_Type())
cucsVnicScsiOperVcon.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicScsiOperVcon.setStatus(_A)
_CucsVnicScsiOrder_Type=Gauge32
_CucsVnicScsiOrder_Object=MibTableColumn
cucsVnicScsiOrder=_CucsVnicScsiOrder_Object((1,3,6,1,4,1,9,9,719,1,53,33,1,17),_CucsVnicScsiOrder_Type())
cucsVnicScsiOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicScsiOrder.setStatus(_A)
_CucsVnicScsiOwner_Type=CucsVnicConnectionOwner
_CucsVnicScsiOwner_Object=MibTableColumn
cucsVnicScsiOwner=_CucsVnicScsiOwner_Object((1,3,6,1,4,1,9,9,719,1,53,33,1,18),_CucsVnicScsiOwner_Type())
cucsVnicScsiOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicScsiOwner.setStatus(_A)
_CucsVnicScsiPinToGroupName_Type=SnmpAdminString
_CucsVnicScsiPinToGroupName_Object=MibTableColumn
cucsVnicScsiPinToGroupName=_CucsVnicScsiPinToGroupName_Object((1,3,6,1,4,1,9,9,719,1,53,33,1,19),_CucsVnicScsiPinToGroupName_Type())
cucsVnicScsiPinToGroupName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicScsiPinToGroupName.setStatus(_A)
_CucsVnicScsiQosPolicyName_Type=SnmpAdminString
_CucsVnicScsiQosPolicyName_Object=MibTableColumn
cucsVnicScsiQosPolicyName=_CucsVnicScsiQosPolicyName_Object((1,3,6,1,4,1,9,9,719,1,53,33,1,20),_CucsVnicScsiQosPolicyName_Type())
cucsVnicScsiQosPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicScsiQosPolicyName.setStatus(_A)
_CucsVnicScsiStatsPolicyName_Type=SnmpAdminString
_CucsVnicScsiStatsPolicyName_Object=MibTableColumn
cucsVnicScsiStatsPolicyName=_CucsVnicScsiStatsPolicyName_Object((1,3,6,1,4,1,9,9,719,1,53,33,1,21),_CucsVnicScsiStatsPolicyName_Type())
cucsVnicScsiStatsPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicScsiStatsPolicyName.setStatus(_A)
_CucsVnicScsiSwitchId_Type=CucsNetworkSwitchId
_CucsVnicScsiSwitchId_Object=MibTableColumn
cucsVnicScsiSwitchId=_CucsVnicScsiSwitchId_Object((1,3,6,1,4,1,9,9,719,1,53,33,1,22),_CucsVnicScsiSwitchId_Type())
cucsVnicScsiSwitchId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicScsiSwitchId.setStatus(_A)
_CucsVnicScsiType_Type=CucsVnicScsiType
_CucsVnicScsiType_Object=MibTableColumn
cucsVnicScsiType=_CucsVnicScsiType_Object((1,3,6,1,4,1,9,9,719,1,53,33,1,23),_CucsVnicScsiType_Type())
cucsVnicScsiType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicScsiType.setStatus(_A)
_CucsVnicScsiConfigQualifier_Type=CucsVnicConfigIssues
_CucsVnicScsiConfigQualifier_Object=MibTableColumn
cucsVnicScsiConfigQualifier=_CucsVnicScsiConfigQualifier_Object((1,3,6,1,4,1,9,9,719,1,53,33,1,25),_CucsVnicScsiConfigQualifier_Type())
cucsVnicScsiConfigQualifier.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicScsiConfigQualifier.setStatus(_A)
_CucsVnicScsiAdminHostPort_Type=CucsFabricHostPortId
_CucsVnicScsiAdminHostPort_Object=MibTableColumn
cucsVnicScsiAdminHostPort=_CucsVnicScsiAdminHostPort_Object((1,3,6,1,4,1,9,9,719,1,53,33,1,27),_CucsVnicScsiAdminHostPort_Type())
cucsVnicScsiAdminHostPort.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicScsiAdminHostPort.setStatus(_A)
_CucsVnicScsiOperHostPort_Type=CucsVnicVnicOperHostPort
_CucsVnicScsiOperHostPort_Object=MibTableColumn
cucsVnicScsiOperHostPort=_CucsVnicScsiOperHostPort_Object((1,3,6,1,4,1,9,9,719,1,53,33,1,28),_CucsVnicScsiOperHostPort_Type())
cucsVnicScsiOperHostPort.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicScsiOperHostPort.setStatus(_A)
_CucsVnicScsiAdminCdnName_Type=SnmpAdminString
_CucsVnicScsiAdminCdnName_Object=MibTableColumn
cucsVnicScsiAdminCdnName=_CucsVnicScsiAdminCdnName_Object((1,3,6,1,4,1,9,9,719,1,53,33,1,29),_CucsVnicScsiAdminCdnName_Type())
cucsVnicScsiAdminCdnName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicScsiAdminCdnName.setStatus(_A)
_CucsVnicScsiOperCdnName_Type=SnmpAdminString
_CucsVnicScsiOperCdnName_Object=MibTableColumn
cucsVnicScsiOperCdnName=_CucsVnicScsiOperCdnName_Object((1,3,6,1,4,1,9,9,719,1,53,33,1,30),_CucsVnicScsiOperCdnName_Type())
cucsVnicScsiOperCdnName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicScsiOperCdnName.setStatus(_A)
_CucsVnicScsiCdnPropInSync_Type=TruthValue
_CucsVnicScsiCdnPropInSync_Object=MibTableColumn
cucsVnicScsiCdnPropInSync=_CucsVnicScsiCdnPropInSync_Object((1,3,6,1,4,1,9,9,719,1,53,33,1,31),_CucsVnicScsiCdnPropInSync_Type())
cucsVnicScsiCdnPropInSync.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicScsiCdnPropInSync.setStatus(_A)
_CucsVnicScsiCdnSource_Type=CucsVnicCdnSource
_CucsVnicScsiCdnSource_Object=MibTableColumn
cucsVnicScsiCdnSource=_CucsVnicScsiCdnSource_Object((1,3,6,1,4,1,9,9,719,1,53,33,1,32),_CucsVnicScsiCdnSource_Type())
cucsVnicScsiCdnSource.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicScsiCdnSource.setStatus(_A)
_CucsVnicScsiRedundancyPairType_Type=CucsVnicRedundancyPairType
_CucsVnicScsiRedundancyPairType_Object=MibTableColumn
cucsVnicScsiRedundancyPairType=_CucsVnicScsiRedundancyPairType_Object((1,3,6,1,4,1,9,9,719,1,53,33,1,33),_CucsVnicScsiRedundancyPairType_Type())
cucsVnicScsiRedundancyPairType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicScsiRedundancyPairType.setStatus(_A)
_CucsVnicScsiRedundancyPeer_Type=SnmpAdminString
_CucsVnicScsiRedundancyPeer_Object=MibTableColumn
cucsVnicScsiRedundancyPeer=_CucsVnicScsiRedundancyPeer_Object((1,3,6,1,4,1,9,9,719,1,53,33,1,34),_CucsVnicScsiRedundancyPeer_Type())
cucsVnicScsiRedundancyPeer.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicScsiRedundancyPeer.setStatus(_A)
_CucsVnicScsiIfTable_Object=MibTable
cucsVnicScsiIfTable=_CucsVnicScsiIfTable_Object((1,3,6,1,4,1,9,9,719,1,53,34))
if mibBuilder.loadTexts:cucsVnicScsiIfTable.setStatus(_A)
_CucsVnicScsiIfEntry_Object=MibTableRow
cucsVnicScsiIfEntry=_CucsVnicScsiIfEntry_Object((1,3,6,1,4,1,9,9,719,1,53,34,1))
cucsVnicScsiIfEntry.setIndexNames((0,_C,_l))
if mibBuilder.loadTexts:cucsVnicScsiIfEntry.setStatus(_A)
_CucsVnicScsiIfInstanceId_Type=CucsManagedObjectId
_CucsVnicScsiIfInstanceId_Object=MibTableColumn
cucsVnicScsiIfInstanceId=_CucsVnicScsiIfInstanceId_Object((1,3,6,1,4,1,9,9,719,1,53,34,1,1),_CucsVnicScsiIfInstanceId_Type())
cucsVnicScsiIfInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsVnicScsiIfInstanceId.setStatus(_A)
_CucsVnicScsiIfDn_Type=CucsManagedObjectDn
_CucsVnicScsiIfDn_Object=MibTableColumn
cucsVnicScsiIfDn=_CucsVnicScsiIfDn_Object((1,3,6,1,4,1,9,9,719,1,53,34,1,2),_CucsVnicScsiIfDn_Type())
cucsVnicScsiIfDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicScsiIfDn.setStatus(_A)
_CucsVnicScsiIfRn_Type=SnmpAdminString
_CucsVnicScsiIfRn_Object=MibTableColumn
cucsVnicScsiIfRn=_CucsVnicScsiIfRn_Object((1,3,6,1,4,1,9,9,719,1,53,34,1,3),_CucsVnicScsiIfRn_Type())
cucsVnicScsiIfRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicScsiIfRn.setStatus(_A)
_CucsVnicScsiIfAddr_Type=Unsigned64
_CucsVnicScsiIfAddr_Object=MibTableColumn
cucsVnicScsiIfAddr=_CucsVnicScsiIfAddr_Object((1,3,6,1,4,1,9,9,719,1,53,34,1,4),_CucsVnicScsiIfAddr_Type())
cucsVnicScsiIfAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicScsiIfAddr.setStatus(_A)
_CucsVnicScsiIfName_Type=SnmpAdminString
_CucsVnicScsiIfName_Object=MibTableColumn
cucsVnicScsiIfName=_CucsVnicScsiIfName_Object((1,3,6,1,4,1,9,9,719,1,53,34,1,5),_CucsVnicScsiIfName_Type())
cucsVnicScsiIfName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicScsiIfName.setStatus(_A)
_CucsVnicScsiIfOperState_Type=CucsVnicIfOperState
_CucsVnicScsiIfOperState_Object=MibTableColumn
cucsVnicScsiIfOperState=_CucsVnicScsiIfOperState_Object((1,3,6,1,4,1,9,9,719,1,53,34,1,6),_CucsVnicScsiIfOperState_Type())
cucsVnicScsiIfOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicScsiIfOperState.setStatus(_A)
_CucsVnicScsiIfOwner_Type=CucsVnicConnectionOwner
_CucsVnicScsiIfOwner_Object=MibTableColumn
cucsVnicScsiIfOwner=_CucsVnicScsiIfOwner_Object((1,3,6,1,4,1,9,9,719,1,53,34,1,7),_CucsVnicScsiIfOwner_Type())
cucsVnicScsiIfOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicScsiIfOwner.setStatus(_A)
_CucsVnicScsiIfSwitchId_Type=CucsNetworkSwitchId
_CucsVnicScsiIfSwitchId_Object=MibTableColumn
cucsVnicScsiIfSwitchId=_CucsVnicScsiIfSwitchId_Object((1,3,6,1,4,1,9,9,719,1,53,34,1,8),_CucsVnicScsiIfSwitchId_Type())
cucsVnicScsiIfSwitchId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicScsiIfSwitchId.setStatus(_A)
_CucsVnicScsiIfType_Type=CucsVnicAScsiIfType
_CucsVnicScsiIfType_Object=MibTableColumn
cucsVnicScsiIfType=_CucsVnicScsiIfType_Object((1,3,6,1,4,1,9,9,719,1,53,34,1,9),_CucsVnicScsiIfType_Type())
cucsVnicScsiIfType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicScsiIfType.setStatus(_A)
_CucsVnicScsiIfVnet_Type=Gauge32
_CucsVnicScsiIfVnet_Object=MibTableColumn
cucsVnicScsiIfVnet=_CucsVnicScsiIfVnet_Object((1,3,6,1,4,1,9,9,719,1,53,34,1,10),_CucsVnicScsiIfVnet_Type())
cucsVnicScsiIfVnet.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicScsiIfVnet.setStatus(_A)
_CucsVnicScsiIfConfigQualifier_Type=CucsVnicConfigIssues
_CucsVnicScsiIfConfigQualifier_Object=MibTableColumn
cucsVnicScsiIfConfigQualifier=_CucsVnicScsiIfConfigQualifier_Object((1,3,6,1,4,1,9,9,719,1,53,34,1,11),_CucsVnicScsiIfConfigQualifier_Type())
cucsVnicScsiIfConfigQualifier.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicScsiIfConfigQualifier.setStatus(_A)
_CucsVnicScsiIfOperVnetDn_Type=SnmpAdminString
_CucsVnicScsiIfOperVnetDn_Object=MibTableColumn
cucsVnicScsiIfOperVnetDn=_CucsVnicScsiIfOperVnetDn_Object((1,3,6,1,4,1,9,9,719,1,53,34,1,13),_CucsVnicScsiIfOperVnetDn_Type())
cucsVnicScsiIfOperVnetDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicScsiIfOperVnetDn.setStatus(_A)
_CucsVnicScsiIfOperVnetName_Type=SnmpAdminString
_CucsVnicScsiIfOperVnetName_Object=MibTableColumn
cucsVnicScsiIfOperVnetName=_CucsVnicScsiIfOperVnetName_Object((1,3,6,1,4,1,9,9,719,1,53,34,1,14),_CucsVnicScsiIfOperVnetName_Type())
cucsVnicScsiIfOperVnetName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicScsiIfOperVnetName.setStatus(_A)
_CucsVnicScsiIfPubNwId_Type=Gauge32
_CucsVnicScsiIfPubNwId_Object=MibTableColumn
cucsVnicScsiIfPubNwId=_CucsVnicScsiIfPubNwId_Object((1,3,6,1,4,1,9,9,719,1,53,34,1,15),_CucsVnicScsiIfPubNwId_Type())
cucsVnicScsiIfPubNwId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicScsiIfPubNwId.setStatus(_A)
_CucsVnicScsiIfSharing_Type=CucsFabricVlanSharingType
_CucsVnicScsiIfSharing_Object=MibTableColumn
cucsVnicScsiIfSharing=_CucsVnicScsiIfSharing_Object((1,3,6,1,4,1,9,9,719,1,53,34,1,16),_CucsVnicScsiIfSharing_Type())
cucsVnicScsiIfSharing.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicScsiIfSharing.setStatus(_A)
_CucsVnicScsiIfOperPrimaryVnetDn_Type=SnmpAdminString
_CucsVnicScsiIfOperPrimaryVnetDn_Object=MibTableColumn
cucsVnicScsiIfOperPrimaryVnetDn=_CucsVnicScsiIfOperPrimaryVnetDn_Object((1,3,6,1,4,1,9,9,719,1,53,34,1,17),_CucsVnicScsiIfOperPrimaryVnetDn_Type())
cucsVnicScsiIfOperPrimaryVnetDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicScsiIfOperPrimaryVnetDn.setStatus(_A)
_CucsVnicScsiIfOperPrimaryVnetName_Type=SnmpAdminString
_CucsVnicScsiIfOperPrimaryVnetName_Object=MibTableColumn
cucsVnicScsiIfOperPrimaryVnetName=_CucsVnicScsiIfOperPrimaryVnetName_Object((1,3,6,1,4,1,9,9,719,1,53,34,1,18),_CucsVnicScsiIfOperPrimaryVnetName_Type())
cucsVnicScsiIfOperPrimaryVnetName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicScsiIfOperPrimaryVnetName.setStatus(_A)
_CucsVnicBootIpPolicyTable_Object=MibTable
cucsVnicBootIpPolicyTable=_CucsVnicBootIpPolicyTable_Object((1,3,6,1,4,1,9,9,719,1,53,35))
if mibBuilder.loadTexts:cucsVnicBootIpPolicyTable.setStatus(_A)
_CucsVnicBootIpPolicyEntry_Object=MibTableRow
cucsVnicBootIpPolicyEntry=_CucsVnicBootIpPolicyEntry_Object((1,3,6,1,4,1,9,9,719,1,53,35,1))
cucsVnicBootIpPolicyEntry.setIndexNames((0,_C,_m))
if mibBuilder.loadTexts:cucsVnicBootIpPolicyEntry.setStatus(_A)
_CucsVnicBootIpPolicyInstanceId_Type=CucsManagedObjectId
_CucsVnicBootIpPolicyInstanceId_Object=MibTableColumn
cucsVnicBootIpPolicyInstanceId=_CucsVnicBootIpPolicyInstanceId_Object((1,3,6,1,4,1,9,9,719,1,53,35,1,1),_CucsVnicBootIpPolicyInstanceId_Type())
cucsVnicBootIpPolicyInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsVnicBootIpPolicyInstanceId.setStatus(_A)
_CucsVnicBootIpPolicyDn_Type=CucsManagedObjectDn
_CucsVnicBootIpPolicyDn_Object=MibTableColumn
cucsVnicBootIpPolicyDn=_CucsVnicBootIpPolicyDn_Object((1,3,6,1,4,1,9,9,719,1,53,35,1,2),_CucsVnicBootIpPolicyDn_Type())
cucsVnicBootIpPolicyDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicBootIpPolicyDn.setStatus(_A)
_CucsVnicBootIpPolicyRn_Type=SnmpAdminString
_CucsVnicBootIpPolicyRn_Object=MibTableColumn
cucsVnicBootIpPolicyRn=_CucsVnicBootIpPolicyRn_Object((1,3,6,1,4,1,9,9,719,1,53,35,1,3),_CucsVnicBootIpPolicyRn_Type())
cucsVnicBootIpPolicyRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicBootIpPolicyRn.setStatus(_A)
_CucsVnicBootIpPolicyDescr_Type=SnmpAdminString
_CucsVnicBootIpPolicyDescr_Object=MibTableColumn
cucsVnicBootIpPolicyDescr=_CucsVnicBootIpPolicyDescr_Object((1,3,6,1,4,1,9,9,719,1,53,35,1,4),_CucsVnicBootIpPolicyDescr_Type())
cucsVnicBootIpPolicyDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicBootIpPolicyDescr.setStatus(_A)
_CucsVnicBootIpPolicyIntId_Type=SnmpAdminString
_CucsVnicBootIpPolicyIntId_Object=MibTableColumn
cucsVnicBootIpPolicyIntId=_CucsVnicBootIpPolicyIntId_Object((1,3,6,1,4,1,9,9,719,1,53,35,1,5),_CucsVnicBootIpPolicyIntId_Type())
cucsVnicBootIpPolicyIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicBootIpPolicyIntId.setStatus(_A)
_CucsVnicBootIpPolicyName_Type=SnmpAdminString
_CucsVnicBootIpPolicyName_Object=MibTableColumn
cucsVnicBootIpPolicyName=_CucsVnicBootIpPolicyName_Object((1,3,6,1,4,1,9,9,719,1,53,35,1,6),_CucsVnicBootIpPolicyName_Type())
cucsVnicBootIpPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicBootIpPolicyName.setStatus(_A)
_CucsVnicBootIpPolicyPoolName_Type=SnmpAdminString
_CucsVnicBootIpPolicyPoolName_Object=MibTableColumn
cucsVnicBootIpPolicyPoolName=_CucsVnicBootIpPolicyPoolName_Object((1,3,6,1,4,1,9,9,719,1,53,35,1,7),_CucsVnicBootIpPolicyPoolName_Type())
cucsVnicBootIpPolicyPoolName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicBootIpPolicyPoolName.setStatus(_A)
_CucsVnicBootIpPolicyPolicyLevel_Type=Gauge32
_CucsVnicBootIpPolicyPolicyLevel_Object=MibTableColumn
cucsVnicBootIpPolicyPolicyLevel=_CucsVnicBootIpPolicyPolicyLevel_Object((1,3,6,1,4,1,9,9,719,1,53,35,1,8),_CucsVnicBootIpPolicyPolicyLevel_Type())
cucsVnicBootIpPolicyPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicBootIpPolicyPolicyLevel.setStatus(_A)
_CucsVnicBootIpPolicyPolicyOwner_Type=CucsPolicyPolicyOwner
_CucsVnicBootIpPolicyPolicyOwner_Object=MibTableColumn
cucsVnicBootIpPolicyPolicyOwner=_CucsVnicBootIpPolicyPolicyOwner_Object((1,3,6,1,4,1,9,9,719,1,53,35,1,9),_CucsVnicBootIpPolicyPolicyOwner_Type())
cucsVnicBootIpPolicyPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicBootIpPolicyPolicyOwner.setStatus(_A)
_CucsVnicIPv4IscsiAddrTable_Object=MibTable
cucsVnicIPv4IscsiAddrTable=_CucsVnicIPv4IscsiAddrTable_Object((1,3,6,1,4,1,9,9,719,1,53,36))
if mibBuilder.loadTexts:cucsVnicIPv4IscsiAddrTable.setStatus(_A)
_CucsVnicIPv4IscsiAddrEntry_Object=MibTableRow
cucsVnicIPv4IscsiAddrEntry=_CucsVnicIPv4IscsiAddrEntry_Object((1,3,6,1,4,1,9,9,719,1,53,36,1))
cucsVnicIPv4IscsiAddrEntry.setIndexNames((0,_C,_n))
if mibBuilder.loadTexts:cucsVnicIPv4IscsiAddrEntry.setStatus(_A)
_CucsVnicIPv4IscsiAddrInstanceId_Type=CucsManagedObjectId
_CucsVnicIPv4IscsiAddrInstanceId_Object=MibTableColumn
cucsVnicIPv4IscsiAddrInstanceId=_CucsVnicIPv4IscsiAddrInstanceId_Object((1,3,6,1,4,1,9,9,719,1,53,36,1,1),_CucsVnicIPv4IscsiAddrInstanceId_Type())
cucsVnicIPv4IscsiAddrInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsVnicIPv4IscsiAddrInstanceId.setStatus(_A)
_CucsVnicIPv4IscsiAddrDn_Type=CucsManagedObjectDn
_CucsVnicIPv4IscsiAddrDn_Object=MibTableColumn
cucsVnicIPv4IscsiAddrDn=_CucsVnicIPv4IscsiAddrDn_Object((1,3,6,1,4,1,9,9,719,1,53,36,1,2),_CucsVnicIPv4IscsiAddrDn_Type())
cucsVnicIPv4IscsiAddrDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIPv4IscsiAddrDn.setStatus(_A)
_CucsVnicIPv4IscsiAddrRn_Type=SnmpAdminString
_CucsVnicIPv4IscsiAddrRn_Object=MibTableColumn
cucsVnicIPv4IscsiAddrRn=_CucsVnicIPv4IscsiAddrRn_Object((1,3,6,1,4,1,9,9,719,1,53,36,1,3),_CucsVnicIPv4IscsiAddrRn_Type())
cucsVnicIPv4IscsiAddrRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIPv4IscsiAddrRn.setStatus(_A)
_CucsVnicIPv4IscsiAddrAddr_Type=InetAddressIPv4
_CucsVnicIPv4IscsiAddrAddr_Object=MibTableColumn
cucsVnicIPv4IscsiAddrAddr=_CucsVnicIPv4IscsiAddrAddr_Object((1,3,6,1,4,1,9,9,719,1,53,36,1,4),_CucsVnicIPv4IscsiAddrAddr_Type())
cucsVnicIPv4IscsiAddrAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIPv4IscsiAddrAddr.setStatus(_A)
_CucsVnicIPv4IscsiAddrDefGw_Type=InetAddressIPv4
_CucsVnicIPv4IscsiAddrDefGw_Object=MibTableColumn
cucsVnicIPv4IscsiAddrDefGw=_CucsVnicIPv4IscsiAddrDefGw_Object((1,3,6,1,4,1,9,9,719,1,53,36,1,5),_CucsVnicIPv4IscsiAddrDefGw_Type())
cucsVnicIPv4IscsiAddrDefGw.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIPv4IscsiAddrDefGw.setStatus(_A)
_CucsVnicIPv4IscsiAddrPrimDns_Type=InetAddressIPv4
_CucsVnicIPv4IscsiAddrPrimDns_Object=MibTableColumn
cucsVnicIPv4IscsiAddrPrimDns=_CucsVnicIPv4IscsiAddrPrimDns_Object((1,3,6,1,4,1,9,9,719,1,53,36,1,6),_CucsVnicIPv4IscsiAddrPrimDns_Type())
cucsVnicIPv4IscsiAddrPrimDns.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIPv4IscsiAddrPrimDns.setStatus(_A)
_CucsVnicIPv4IscsiAddrSecDns_Type=InetAddressIPv4
_CucsVnicIPv4IscsiAddrSecDns_Object=MibTableColumn
cucsVnicIPv4IscsiAddrSecDns=_CucsVnicIPv4IscsiAddrSecDns_Object((1,3,6,1,4,1,9,9,719,1,53,36,1,7),_CucsVnicIPv4IscsiAddrSecDns_Type())
cucsVnicIPv4IscsiAddrSecDns.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIPv4IscsiAddrSecDns.setStatus(_A)
_CucsVnicIPv4IscsiAddrSubnet_Type=InetAddressIPv4
_CucsVnicIPv4IscsiAddrSubnet_Object=MibTableColumn
cucsVnicIPv4IscsiAddrSubnet=_CucsVnicIPv4IscsiAddrSubnet_Object((1,3,6,1,4,1,9,9,719,1,53,36,1,8),_CucsVnicIPv4IscsiAddrSubnet_Type())
cucsVnicIPv4IscsiAddrSubnet.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIPv4IscsiAddrSubnet.setStatus(_A)
_CucsVnicIPv4PooledIscsiAddrTable_Object=MibTable
cucsVnicIPv4PooledIscsiAddrTable=_CucsVnicIPv4PooledIscsiAddrTable_Object((1,3,6,1,4,1,9,9,719,1,53,37))
if mibBuilder.loadTexts:cucsVnicIPv4PooledIscsiAddrTable.setStatus(_A)
_CucsVnicIPv4PooledIscsiAddrEntry_Object=MibTableRow
cucsVnicIPv4PooledIscsiAddrEntry=_CucsVnicIPv4PooledIscsiAddrEntry_Object((1,3,6,1,4,1,9,9,719,1,53,37,1))
cucsVnicIPv4PooledIscsiAddrEntry.setIndexNames((0,_C,_o))
if mibBuilder.loadTexts:cucsVnicIPv4PooledIscsiAddrEntry.setStatus(_A)
_CucsVnicIPv4PooledIscsiAddrInstanceId_Type=CucsManagedObjectId
_CucsVnicIPv4PooledIscsiAddrInstanceId_Object=MibTableColumn
cucsVnicIPv4PooledIscsiAddrInstanceId=_CucsVnicIPv4PooledIscsiAddrInstanceId_Object((1,3,6,1,4,1,9,9,719,1,53,37,1,1),_CucsVnicIPv4PooledIscsiAddrInstanceId_Type())
cucsVnicIPv4PooledIscsiAddrInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsVnicIPv4PooledIscsiAddrInstanceId.setStatus(_A)
_CucsVnicIPv4PooledIscsiAddrDn_Type=CucsManagedObjectDn
_CucsVnicIPv4PooledIscsiAddrDn_Object=MibTableColumn
cucsVnicIPv4PooledIscsiAddrDn=_CucsVnicIPv4PooledIscsiAddrDn_Object((1,3,6,1,4,1,9,9,719,1,53,37,1,2),_CucsVnicIPv4PooledIscsiAddrDn_Type())
cucsVnicIPv4PooledIscsiAddrDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIPv4PooledIscsiAddrDn.setStatus(_A)
_CucsVnicIPv4PooledIscsiAddrRn_Type=SnmpAdminString
_CucsVnicIPv4PooledIscsiAddrRn_Object=MibTableColumn
cucsVnicIPv4PooledIscsiAddrRn=_CucsVnicIPv4PooledIscsiAddrRn_Object((1,3,6,1,4,1,9,9,719,1,53,37,1,3),_CucsVnicIPv4PooledIscsiAddrRn_Type())
cucsVnicIPv4PooledIscsiAddrRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIPv4PooledIscsiAddrRn.setStatus(_A)
_CucsVnicIPv4PooledIscsiAddrAddr_Type=InetAddressIPv4
_CucsVnicIPv4PooledIscsiAddrAddr_Object=MibTableColumn
cucsVnicIPv4PooledIscsiAddrAddr=_CucsVnicIPv4PooledIscsiAddrAddr_Object((1,3,6,1,4,1,9,9,719,1,53,37,1,4),_CucsVnicIPv4PooledIscsiAddrAddr_Type())
cucsVnicIPv4PooledIscsiAddrAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIPv4PooledIscsiAddrAddr.setStatus(_A)
_CucsVnicIPv4PooledIscsiAddrDefGw_Type=InetAddressIPv4
_CucsVnicIPv4PooledIscsiAddrDefGw_Object=MibTableColumn
cucsVnicIPv4PooledIscsiAddrDefGw=_CucsVnicIPv4PooledIscsiAddrDefGw_Object((1,3,6,1,4,1,9,9,719,1,53,37,1,5),_CucsVnicIPv4PooledIscsiAddrDefGw_Type())
cucsVnicIPv4PooledIscsiAddrDefGw.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIPv4PooledIscsiAddrDefGw.setStatus(_A)
_CucsVnicIPv4PooledIscsiAddrIdentPoolName_Type=SnmpAdminString
_CucsVnicIPv4PooledIscsiAddrIdentPoolName_Object=MibTableColumn
cucsVnicIPv4PooledIscsiAddrIdentPoolName=_CucsVnicIPv4PooledIscsiAddrIdentPoolName_Object((1,3,6,1,4,1,9,9,719,1,53,37,1,6),_CucsVnicIPv4PooledIscsiAddrIdentPoolName_Type())
cucsVnicIPv4PooledIscsiAddrIdentPoolName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIPv4PooledIscsiAddrIdentPoolName.setStatus(_A)
_CucsVnicIPv4PooledIscsiAddrOperIdentPoolName_Type=SnmpAdminString
_CucsVnicIPv4PooledIscsiAddrOperIdentPoolName_Object=MibTableColumn
cucsVnicIPv4PooledIscsiAddrOperIdentPoolName=_CucsVnicIPv4PooledIscsiAddrOperIdentPoolName_Object((1,3,6,1,4,1,9,9,719,1,53,37,1,7),_CucsVnicIPv4PooledIscsiAddrOperIdentPoolName_Type())
cucsVnicIPv4PooledIscsiAddrOperIdentPoolName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIPv4PooledIscsiAddrOperIdentPoolName.setStatus(_A)
_CucsVnicIPv4PooledIscsiAddrPrimDns_Type=InetAddressIPv4
_CucsVnicIPv4PooledIscsiAddrPrimDns_Object=MibTableColumn
cucsVnicIPv4PooledIscsiAddrPrimDns=_CucsVnicIPv4PooledIscsiAddrPrimDns_Object((1,3,6,1,4,1,9,9,719,1,53,37,1,8),_CucsVnicIPv4PooledIscsiAddrPrimDns_Type())
cucsVnicIPv4PooledIscsiAddrPrimDns.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIPv4PooledIscsiAddrPrimDns.setStatus(_A)
_CucsVnicIPv4PooledIscsiAddrSecDns_Type=InetAddressIPv4
_CucsVnicIPv4PooledIscsiAddrSecDns_Object=MibTableColumn
cucsVnicIPv4PooledIscsiAddrSecDns=_CucsVnicIPv4PooledIscsiAddrSecDns_Object((1,3,6,1,4,1,9,9,719,1,53,37,1,9),_CucsVnicIPv4PooledIscsiAddrSecDns_Type())
cucsVnicIPv4PooledIscsiAddrSecDns.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIPv4PooledIscsiAddrSecDns.setStatus(_A)
_CucsVnicIPv4PooledIscsiAddrSubnet_Type=InetAddressIPv4
_CucsVnicIPv4PooledIscsiAddrSubnet_Object=MibTableColumn
cucsVnicIPv4PooledIscsiAddrSubnet=_CucsVnicIPv4PooledIscsiAddrSubnet_Object((1,3,6,1,4,1,9,9,719,1,53,37,1,10),_CucsVnicIPv4PooledIscsiAddrSubnet_Type())
cucsVnicIPv4PooledIscsiAddrSubnet.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIPv4PooledIscsiAddrSubnet.setStatus(_A)
_CucsVnicIScsiTable_Object=MibTable
cucsVnicIScsiTable=_CucsVnicIScsiTable_Object((1,3,6,1,4,1,9,9,719,1,53,38))
if mibBuilder.loadTexts:cucsVnicIScsiTable.setStatus(_A)
_CucsVnicIScsiEntry_Object=MibTableRow
cucsVnicIScsiEntry=_CucsVnicIScsiEntry_Object((1,3,6,1,4,1,9,9,719,1,53,38,1))
cucsVnicIScsiEntry.setIndexNames((0,_C,_p))
if mibBuilder.loadTexts:cucsVnicIScsiEntry.setStatus(_A)
_CucsVnicIScsiInstanceId_Type=CucsManagedObjectId
_CucsVnicIScsiInstanceId_Object=MibTableColumn
cucsVnicIScsiInstanceId=_CucsVnicIScsiInstanceId_Object((1,3,6,1,4,1,9,9,719,1,53,38,1,1),_CucsVnicIScsiInstanceId_Type())
cucsVnicIScsiInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsVnicIScsiInstanceId.setStatus(_A)
_CucsVnicIScsiDn_Type=CucsManagedObjectDn
_CucsVnicIScsiDn_Object=MibTableColumn
cucsVnicIScsiDn=_CucsVnicIScsiDn_Object((1,3,6,1,4,1,9,9,719,1,53,38,1,2),_CucsVnicIScsiDn_Type())
cucsVnicIScsiDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiDn.setStatus(_A)
_CucsVnicIScsiRn_Type=SnmpAdminString
_CucsVnicIScsiRn_Object=MibTableColumn
cucsVnicIScsiRn=_CucsVnicIScsiRn_Object((1,3,6,1,4,1,9,9,719,1,53,38,1,3),_CucsVnicIScsiRn_Type())
cucsVnicIScsiRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiRn.setStatus(_A)
_CucsVnicIScsiAdaptorProfileName_Type=SnmpAdminString
_CucsVnicIScsiAdaptorProfileName_Object=MibTableColumn
cucsVnicIScsiAdaptorProfileName=_CucsVnicIScsiAdaptorProfileName_Object((1,3,6,1,4,1,9,9,719,1,53,38,1,4),_CucsVnicIScsiAdaptorProfileName_Type())
cucsVnicIScsiAdaptorProfileName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiAdaptorProfileName.setStatus(_A)
_CucsVnicIScsiAddr_Type=MacAddress
_CucsVnicIScsiAddr_Object=MibTableColumn
cucsVnicIScsiAddr=_CucsVnicIScsiAddr_Object((1,3,6,1,4,1,9,9,719,1,53,38,1,5),_CucsVnicIScsiAddr_Type())
cucsVnicIScsiAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiAddr.setStatus(_A)
_CucsVnicIScsiAdminVcon_Type=SnmpAdminString
_CucsVnicIScsiAdminVcon_Object=MibTableColumn
cucsVnicIScsiAdminVcon=_CucsVnicIScsiAdminVcon_Object((1,3,6,1,4,1,9,9,719,1,53,38,1,6),_CucsVnicIScsiAdminVcon_Type())
cucsVnicIScsiAdminVcon.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiAdminVcon.setStatus(_A)
_CucsVnicIScsiAuthProfileName_Type=SnmpAdminString
_CucsVnicIScsiAuthProfileName_Object=MibTableColumn
cucsVnicIScsiAuthProfileName=_CucsVnicIScsiAuthProfileName_Object((1,3,6,1,4,1,9,9,719,1,53,38,1,7),_CucsVnicIScsiAuthProfileName_Type())
cucsVnicIScsiAuthProfileName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiAuthProfileName.setStatus(_A)
_CucsVnicIScsiBootDev_Type=CucsVnicVnicBootDev
_CucsVnicIScsiBootDev_Object=MibTableColumn
cucsVnicIScsiBootDev=_CucsVnicIScsiBootDev_Object((1,3,6,1,4,1,9,9,719,1,53,38,1,8),_CucsVnicIScsiBootDev_Type())
cucsVnicIScsiBootDev.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiBootDev.setStatus(_A)
_CucsVnicIScsiConfigState_Type=CucsLsConfigState
_CucsVnicIScsiConfigState_Object=MibTableColumn
cucsVnicIScsiConfigState=_CucsVnicIScsiConfigState_Object((1,3,6,1,4,1,9,9,719,1,53,38,1,10),_CucsVnicIScsiConfigState_Type())
cucsVnicIScsiConfigState.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiConfigState.setStatus(_A)
_CucsVnicIScsiEquipmentDn_Type=SnmpAdminString
_CucsVnicIScsiEquipmentDn_Object=MibTableColumn
cucsVnicIScsiEquipmentDn=_CucsVnicIScsiEquipmentDn_Object((1,3,6,1,4,1,9,9,719,1,53,38,1,11),_CucsVnicIScsiEquipmentDn_Type())
cucsVnicIScsiEquipmentDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiEquipmentDn.setStatus(_A)
_CucsVnicIScsiEthEpDn_Type=SnmpAdminString
_CucsVnicIScsiEthEpDn_Object=MibTableColumn
cucsVnicIScsiEthEpDn=_CucsVnicIScsiEthEpDn_Object((1,3,6,1,4,1,9,9,719,1,53,38,1,12),_CucsVnicIScsiEthEpDn_Type())
cucsVnicIScsiEthEpDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiEthEpDn.setStatus(_A)
_CucsVnicIScsiExtIPState_Type=CucsVnicExternalMgmtIPMode
_CucsVnicIScsiExtIPState_Object=MibTableColumn
cucsVnicIScsiExtIPState=_CucsVnicIScsiExtIPState_Object((1,3,6,1,4,1,9,9,719,1,53,38,1,13),_CucsVnicIScsiExtIPState_Type())
cucsVnicIScsiExtIPState.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiExtIPState.setStatus(_A)
_CucsVnicIScsiFltAggr_Type=Unsigned64
_CucsVnicIScsiFltAggr_Object=MibTableColumn
cucsVnicIScsiFltAggr=_CucsVnicIScsiFltAggr_Object((1,3,6,1,4,1,9,9,719,1,53,38,1,14),_CucsVnicIScsiFltAggr_Type())
cucsVnicIScsiFltAggr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiFltAggr.setStatus(_A)
_CucsVnicIScsiIdentPoolName_Type=SnmpAdminString
_CucsVnicIScsiIdentPoolName_Object=MibTableColumn
cucsVnicIScsiIdentPoolName=_CucsVnicIScsiIdentPoolName_Object((1,3,6,1,4,1,9,9,719,1,53,38,1,15),_CucsVnicIScsiIdentPoolName_Type())
cucsVnicIScsiIdentPoolName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiIdentPoolName.setStatus(_A)
_CucsVnicIScsiInitiatorName_Type=SnmpAdminString
_CucsVnicIScsiInitiatorName_Object=MibTableColumn
cucsVnicIScsiInitiatorName=_CucsVnicIScsiInitiatorName_Object((1,3,6,1,4,1,9,9,719,1,53,38,1,16),_CucsVnicIScsiInitiatorName_Type())
cucsVnicIScsiInitiatorName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiInitiatorName.setStatus(_A)
_CucsVnicIScsiInstType_Type=CucsVnicInstantiation
_CucsVnicIScsiInstType_Object=MibTableColumn
cucsVnicIScsiInstType=_CucsVnicIScsiInstType_Object((1,3,6,1,4,1,9,9,719,1,53,38,1,17),_CucsVnicIScsiInstType_Type())
cucsVnicIScsiInstType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiInstType.setStatus(_A)
_CucsVnicIScsiIqnIdentPoolName_Type=SnmpAdminString
_CucsVnicIScsiIqnIdentPoolName_Object=MibTableColumn
cucsVnicIScsiIqnIdentPoolName=_CucsVnicIScsiIqnIdentPoolName_Object((1,3,6,1,4,1,9,9,719,1,53,38,1,18),_CucsVnicIScsiIqnIdentPoolName_Type())
cucsVnicIScsiIqnIdentPoolName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiIqnIdentPoolName.setStatus(_A)
_CucsVnicIScsiName_Type=SnmpAdminString
_CucsVnicIScsiName_Object=MibTableColumn
cucsVnicIScsiName=_CucsVnicIScsiName_Object((1,3,6,1,4,1,9,9,719,1,53,38,1,19),_CucsVnicIScsiName_Type())
cucsVnicIScsiName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiName.setStatus(_A)
_CucsVnicIScsiNwTemplName_Type=SnmpAdminString
_CucsVnicIScsiNwTemplName_Object=MibTableColumn
cucsVnicIScsiNwTemplName=_CucsVnicIScsiNwTemplName_Object((1,3,6,1,4,1,9,9,719,1,53,38,1,20),_CucsVnicIScsiNwTemplName_Type())
cucsVnicIScsiNwTemplName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiNwTemplName.setStatus(_A)
_CucsVnicIScsiOperAdaptorProfileName_Type=SnmpAdminString
_CucsVnicIScsiOperAdaptorProfileName_Object=MibTableColumn
cucsVnicIScsiOperAdaptorProfileName=_CucsVnicIScsiOperAdaptorProfileName_Object((1,3,6,1,4,1,9,9,719,1,53,38,1,21),_CucsVnicIScsiOperAdaptorProfileName_Type())
cucsVnicIScsiOperAdaptorProfileName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiOperAdaptorProfileName.setStatus(_A)
_CucsVnicIScsiOperAuthProfileName_Type=SnmpAdminString
_CucsVnicIScsiOperAuthProfileName_Object=MibTableColumn
cucsVnicIScsiOperAuthProfileName=_CucsVnicIScsiOperAuthProfileName_Object((1,3,6,1,4,1,9,9,719,1,53,38,1,22),_CucsVnicIScsiOperAuthProfileName_Type())
cucsVnicIScsiOperAuthProfileName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiOperAuthProfileName.setStatus(_A)
_CucsVnicIScsiOperIqnIdentPoolName_Type=SnmpAdminString
_CucsVnicIScsiOperIqnIdentPoolName_Object=MibTableColumn
cucsVnicIScsiOperIqnIdentPoolName=_CucsVnicIScsiOperIqnIdentPoolName_Object((1,3,6,1,4,1,9,9,719,1,53,38,1,24),_CucsVnicIScsiOperIqnIdentPoolName_Type())
cucsVnicIScsiOperIqnIdentPoolName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiOperIqnIdentPoolName.setStatus(_A)
_CucsVnicIScsiOperOrder_Type=Gauge32
_CucsVnicIScsiOperOrder_Object=MibTableColumn
cucsVnicIScsiOperOrder=_CucsVnicIScsiOperOrder_Object((1,3,6,1,4,1,9,9,719,1,53,38,1,25),_CucsVnicIScsiOperOrder_Type())
cucsVnicIScsiOperOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiOperOrder.setStatus(_A)
_CucsVnicIScsiOperSpeed_Type=Gauge32
_CucsVnicIScsiOperSpeed_Object=MibTableColumn
cucsVnicIScsiOperSpeed=_CucsVnicIScsiOperSpeed_Object((1,3,6,1,4,1,9,9,719,1,53,38,1,27),_CucsVnicIScsiOperSpeed_Type())
cucsVnicIScsiOperSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiOperSpeed.setStatus(_A)
_CucsVnicIScsiOperStatsPolicyName_Type=SnmpAdminString
_CucsVnicIScsiOperStatsPolicyName_Object=MibTableColumn
cucsVnicIScsiOperStatsPolicyName=_CucsVnicIScsiOperStatsPolicyName_Object((1,3,6,1,4,1,9,9,719,1,53,38,1,28),_CucsVnicIScsiOperStatsPolicyName_Type())
cucsVnicIScsiOperStatsPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiOperStatsPolicyName.setStatus(_A)
_CucsVnicIScsiOperVcon_Type=SnmpAdminString
_CucsVnicIScsiOperVcon_Object=MibTableColumn
cucsVnicIScsiOperVcon=_CucsVnicIScsiOperVcon_Object((1,3,6,1,4,1,9,9,719,1,53,38,1,29),_CucsVnicIScsiOperVcon_Type())
cucsVnicIScsiOperVcon.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiOperVcon.setStatus(_A)
_CucsVnicIScsiOrder_Type=Gauge32
_CucsVnicIScsiOrder_Object=MibTableColumn
cucsVnicIScsiOrder=_CucsVnicIScsiOrder_Object((1,3,6,1,4,1,9,9,719,1,53,38,1,30),_CucsVnicIScsiOrder_Type())
cucsVnicIScsiOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiOrder.setStatus(_A)
_CucsVnicIScsiOwner_Type=CucsVnicConnectionOwner
_CucsVnicIScsiOwner_Object=MibTableColumn
cucsVnicIScsiOwner=_CucsVnicIScsiOwner_Object((1,3,6,1,4,1,9,9,719,1,53,38,1,31),_CucsVnicIScsiOwner_Type())
cucsVnicIScsiOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiOwner.setStatus(_A)
_CucsVnicIScsiPinToGroupName_Type=SnmpAdminString
_CucsVnicIScsiPinToGroupName_Object=MibTableColumn
cucsVnicIScsiPinToGroupName=_CucsVnicIScsiPinToGroupName_Object((1,3,6,1,4,1,9,9,719,1,53,38,1,32),_CucsVnicIScsiPinToGroupName_Type())
cucsVnicIScsiPinToGroupName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiPinToGroupName.setStatus(_A)
_CucsVnicIScsiQosPolicyName_Type=SnmpAdminString
_CucsVnicIScsiQosPolicyName_Object=MibTableColumn
cucsVnicIScsiQosPolicyName=_CucsVnicIScsiQosPolicyName_Object((1,3,6,1,4,1,9,9,719,1,53,38,1,33),_CucsVnicIScsiQosPolicyName_Type())
cucsVnicIScsiQosPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiQosPolicyName.setStatus(_A)
_CucsVnicIScsiStatsPolicyName_Type=SnmpAdminString
_CucsVnicIScsiStatsPolicyName_Object=MibTableColumn
cucsVnicIScsiStatsPolicyName=_CucsVnicIScsiStatsPolicyName_Object((1,3,6,1,4,1,9,9,719,1,53,38,1,34),_CucsVnicIScsiStatsPolicyName_Type())
cucsVnicIScsiStatsPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiStatsPolicyName.setStatus(_A)
_CucsVnicIScsiSwitchId_Type=CucsNetworkSwitchId
_CucsVnicIScsiSwitchId_Object=MibTableColumn
cucsVnicIScsiSwitchId=_CucsVnicIScsiSwitchId_Object((1,3,6,1,4,1,9,9,719,1,53,38,1,35),_CucsVnicIScsiSwitchId_Type())
cucsVnicIScsiSwitchId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiSwitchId.setStatus(_A)
_CucsVnicIScsiType_Type=CucsVnicConnectionType
_CucsVnicIScsiType_Object=MibTableColumn
cucsVnicIScsiType=_CucsVnicIScsiType_Object((1,3,6,1,4,1,9,9,719,1,53,38,1,36),_CucsVnicIScsiType_Type())
cucsVnicIScsiType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiType.setStatus(_A)
_CucsVnicIScsiVnicDefType_Type=CucsVnicIScsiIfDefType
_CucsVnicIScsiVnicDefType_Object=MibTableColumn
cucsVnicIScsiVnicDefType=_CucsVnicIScsiVnicDefType_Object((1,3,6,1,4,1,9,9,719,1,53,38,1,37),_CucsVnicIScsiVnicDefType_Type())
cucsVnicIScsiVnicDefType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiVnicDefType.setStatus(_A)
_CucsVnicIScsiVnicName_Type=SnmpAdminString
_CucsVnicIScsiVnicName_Object=MibTableColumn
cucsVnicIScsiVnicName=_CucsVnicIScsiVnicName_Object((1,3,6,1,4,1,9,9,719,1,53,38,1,38),_CucsVnicIScsiVnicName_Type())
cucsVnicIScsiVnicName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiVnicName.setStatus(_A)
_CucsVnicIScsiConfigQualifier_Type=CucsVnicConfigIssues
_CucsVnicIScsiConfigQualifier_Object=MibTableColumn
cucsVnicIScsiConfigQualifier=_CucsVnicIScsiConfigQualifier_Object((1,3,6,1,4,1,9,9,719,1,53,38,1,39),_CucsVnicIScsiConfigQualifier_Type())
cucsVnicIScsiConfigQualifier.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiConfigQualifier.setStatus(_A)
_CucsVnicIScsiInitNameSuffix_Type=SnmpAdminString
_CucsVnicIScsiInitNameSuffix_Object=MibTableColumn
cucsVnicIScsiInitNameSuffix=_CucsVnicIScsiInitNameSuffix_Object((1,3,6,1,4,1,9,9,719,1,53,38,1,40),_CucsVnicIScsiInitNameSuffix_Type())
cucsVnicIScsiInitNameSuffix.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiInitNameSuffix.setStatus(_A)
_CucsVnicIScsiOperIdentPoolName_Type=SnmpAdminString
_CucsVnicIScsiOperIdentPoolName_Object=MibTableColumn
cucsVnicIScsiOperIdentPoolName=_CucsVnicIScsiOperIdentPoolName_Object((1,3,6,1,4,1,9,9,719,1,53,38,1,41),_CucsVnicIScsiOperIdentPoolName_Type())
cucsVnicIScsiOperIdentPoolName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiOperIdentPoolName.setStatus(_A)
_CucsVnicIScsiAdminHostPort_Type=CucsFabricHostPortId
_CucsVnicIScsiAdminHostPort_Object=MibTableColumn
cucsVnicIScsiAdminHostPort=_CucsVnicIScsiAdminHostPort_Object((1,3,6,1,4,1,9,9,719,1,53,38,1,43),_CucsVnicIScsiAdminHostPort_Type())
cucsVnicIScsiAdminHostPort.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiAdminHostPort.setStatus(_A)
_CucsVnicIScsiOperHostPort_Type=CucsVnicVnicOperHostPort
_CucsVnicIScsiOperHostPort_Object=MibTableColumn
cucsVnicIScsiOperHostPort=_CucsVnicIScsiOperHostPort_Object((1,3,6,1,4,1,9,9,719,1,53,38,1,44),_CucsVnicIScsiOperHostPort_Type())
cucsVnicIScsiOperHostPort.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiOperHostPort.setStatus(_A)
_CucsVnicIScsiPropAcl_Type=Unsigned64
_CucsVnicIScsiPropAcl_Object=MibTableColumn
cucsVnicIScsiPropAcl=_CucsVnicIScsiPropAcl_Object((1,3,6,1,4,1,9,9,719,1,53,38,1,45),_CucsVnicIScsiPropAcl_Type())
cucsVnicIScsiPropAcl.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiPropAcl.setStatus(_A)
_CucsVnicIScsiAdminCdnName_Type=SnmpAdminString
_CucsVnicIScsiAdminCdnName_Object=MibTableColumn
cucsVnicIScsiAdminCdnName=_CucsVnicIScsiAdminCdnName_Object((1,3,6,1,4,1,9,9,719,1,53,38,1,47),_CucsVnicIScsiAdminCdnName_Type())
cucsVnicIScsiAdminCdnName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiAdminCdnName.setStatus(_A)
_CucsVnicIScsiOperCdnName_Type=SnmpAdminString
_CucsVnicIScsiOperCdnName_Object=MibTableColumn
cucsVnicIScsiOperCdnName=_CucsVnicIScsiOperCdnName_Object((1,3,6,1,4,1,9,9,719,1,53,38,1,48),_CucsVnicIScsiOperCdnName_Type())
cucsVnicIScsiOperCdnName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiOperCdnName.setStatus(_A)
_CucsVnicIScsiCdnSource_Type=CucsVnicCdnSource
_CucsVnicIScsiCdnSource_Object=MibTableColumn
cucsVnicIScsiCdnSource=_CucsVnicIScsiCdnSource_Object((1,3,6,1,4,1,9,9,719,1,53,38,1,49),_CucsVnicIScsiCdnSource_Type())
cucsVnicIScsiCdnSource.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiCdnSource.setStatus(_A)
_CucsVnicIScsiCdnPropInSync_Type=TruthValue
_CucsVnicIScsiCdnPropInSync_Object=MibTableColumn
cucsVnicIScsiCdnPropInSync=_CucsVnicIScsiCdnPropInSync_Object((1,3,6,1,4,1,9,9,719,1,53,38,1,50),_CucsVnicIScsiCdnPropInSync_Type())
cucsVnicIScsiCdnPropInSync.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiCdnPropInSync.setStatus(_A)
_CucsVnicIScsiRedundancyPairType_Type=CucsVnicRedundancyPairType
_CucsVnicIScsiRedundancyPairType_Object=MibTableColumn
cucsVnicIScsiRedundancyPairType=_CucsVnicIScsiRedundancyPairType_Object((1,3,6,1,4,1,9,9,719,1,53,38,1,51),_CucsVnicIScsiRedundancyPairType_Type())
cucsVnicIScsiRedundancyPairType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiRedundancyPairType.setStatus(_A)
_CucsVnicIScsiRedundancyPeer_Type=SnmpAdminString
_CucsVnicIScsiRedundancyPeer_Object=MibTableColumn
cucsVnicIScsiRedundancyPeer=_CucsVnicIScsiRedundancyPeer_Object((1,3,6,1,4,1,9,9,719,1,53,38,1,52),_CucsVnicIScsiRedundancyPeer_Type())
cucsVnicIScsiRedundancyPeer.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiRedundancyPeer.setStatus(_A)
_CucsVnicIScsiAutoTargetIfTable_Object=MibTable
cucsVnicIScsiAutoTargetIfTable=_CucsVnicIScsiAutoTargetIfTable_Object((1,3,6,1,4,1,9,9,719,1,53,39))
if mibBuilder.loadTexts:cucsVnicIScsiAutoTargetIfTable.setStatus(_A)
_CucsVnicIScsiAutoTargetIfEntry_Object=MibTableRow
cucsVnicIScsiAutoTargetIfEntry=_CucsVnicIScsiAutoTargetIfEntry_Object((1,3,6,1,4,1,9,9,719,1,53,39,1))
cucsVnicIScsiAutoTargetIfEntry.setIndexNames((0,_C,_q))
if mibBuilder.loadTexts:cucsVnicIScsiAutoTargetIfEntry.setStatus(_A)
_CucsVnicIScsiAutoTargetIfInstanceId_Type=CucsManagedObjectId
_CucsVnicIScsiAutoTargetIfInstanceId_Object=MibTableColumn
cucsVnicIScsiAutoTargetIfInstanceId=_CucsVnicIScsiAutoTargetIfInstanceId_Object((1,3,6,1,4,1,9,9,719,1,53,39,1,1),_CucsVnicIScsiAutoTargetIfInstanceId_Type())
cucsVnicIScsiAutoTargetIfInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsVnicIScsiAutoTargetIfInstanceId.setStatus(_A)
_CucsVnicIScsiAutoTargetIfDn_Type=CucsManagedObjectDn
_CucsVnicIScsiAutoTargetIfDn_Object=MibTableColumn
cucsVnicIScsiAutoTargetIfDn=_CucsVnicIScsiAutoTargetIfDn_Object((1,3,6,1,4,1,9,9,719,1,53,39,1,2),_CucsVnicIScsiAutoTargetIfDn_Type())
cucsVnicIScsiAutoTargetIfDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiAutoTargetIfDn.setStatus(_A)
_CucsVnicIScsiAutoTargetIfRn_Type=SnmpAdminString
_CucsVnicIScsiAutoTargetIfRn_Object=MibTableColumn
cucsVnicIScsiAutoTargetIfRn=_CucsVnicIScsiAutoTargetIfRn_Object((1,3,6,1,4,1,9,9,719,1,53,39,1,3),_CucsVnicIScsiAutoTargetIfRn_Type())
cucsVnicIScsiAutoTargetIfRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiAutoTargetIfRn.setStatus(_A)
_CucsVnicIScsiAutoTargetIfDhcpVendorId_Type=SnmpAdminString
_CucsVnicIScsiAutoTargetIfDhcpVendorId_Object=MibTableColumn
cucsVnicIScsiAutoTargetIfDhcpVendorId=_CucsVnicIScsiAutoTargetIfDhcpVendorId_Object((1,3,6,1,4,1,9,9,719,1,53,39,1,4),_CucsVnicIScsiAutoTargetIfDhcpVendorId_Type())
cucsVnicIScsiAutoTargetIfDhcpVendorId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiAutoTargetIfDhcpVendorId.setStatus(_A)
_CucsVnicIScsiNodeTable_Object=MibTable
cucsVnicIScsiNodeTable=_CucsVnicIScsiNodeTable_Object((1,3,6,1,4,1,9,9,719,1,53,40))
if mibBuilder.loadTexts:cucsVnicIScsiNodeTable.setStatus(_A)
_CucsVnicIScsiNodeEntry_Object=MibTableRow
cucsVnicIScsiNodeEntry=_CucsVnicIScsiNodeEntry_Object((1,3,6,1,4,1,9,9,719,1,53,40,1))
cucsVnicIScsiNodeEntry.setIndexNames((0,_C,_r))
if mibBuilder.loadTexts:cucsVnicIScsiNodeEntry.setStatus(_A)
_CucsVnicIScsiNodeInstanceId_Type=CucsManagedObjectId
_CucsVnicIScsiNodeInstanceId_Object=MibTableColumn
cucsVnicIScsiNodeInstanceId=_CucsVnicIScsiNodeInstanceId_Object((1,3,6,1,4,1,9,9,719,1,53,40,1,1),_CucsVnicIScsiNodeInstanceId_Type())
cucsVnicIScsiNodeInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsVnicIScsiNodeInstanceId.setStatus(_A)
_CucsVnicIScsiNodeDn_Type=CucsManagedObjectDn
_CucsVnicIScsiNodeDn_Object=MibTableColumn
cucsVnicIScsiNodeDn=_CucsVnicIScsiNodeDn_Object((1,3,6,1,4,1,9,9,719,1,53,40,1,2),_CucsVnicIScsiNodeDn_Type())
cucsVnicIScsiNodeDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiNodeDn.setStatus(_A)
_CucsVnicIScsiNodeRn_Type=SnmpAdminString
_CucsVnicIScsiNodeRn_Object=MibTableColumn
cucsVnicIScsiNodeRn=_CucsVnicIScsiNodeRn_Object((1,3,6,1,4,1,9,9,719,1,53,40,1,3),_CucsVnicIScsiNodeRn_Type())
cucsVnicIScsiNodeRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiNodeRn.setStatus(_A)
_CucsVnicIScsiNodeFltAggr_Type=Unsigned64
_CucsVnicIScsiNodeFltAggr_Object=MibTableColumn
cucsVnicIScsiNodeFltAggr=_CucsVnicIScsiNodeFltAggr_Object((1,3,6,1,4,1,9,9,719,1,53,40,1,4),_CucsVnicIScsiNodeFltAggr_Type())
cucsVnicIScsiNodeFltAggr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiNodeFltAggr.setStatus(_A)
_CucsVnicIScsiNodeInitiatorName_Type=SnmpAdminString
_CucsVnicIScsiNodeInitiatorName_Object=MibTableColumn
cucsVnicIScsiNodeInitiatorName=_CucsVnicIScsiNodeInitiatorName_Object((1,3,6,1,4,1,9,9,719,1,53,40,1,5),_CucsVnicIScsiNodeInitiatorName_Type())
cucsVnicIScsiNodeInitiatorName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiNodeInitiatorName.setStatus(_A)
_CucsVnicIScsiNodeOwner_Type=CucsVnicIScsiNodeOwner
_CucsVnicIScsiNodeOwner_Object=MibTableColumn
cucsVnicIScsiNodeOwner=_CucsVnicIScsiNodeOwner_Object((1,3,6,1,4,1,9,9,719,1,53,40,1,6),_CucsVnicIScsiNodeOwner_Type())
cucsVnicIScsiNodeOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiNodeOwner.setStatus(_A)
_CucsVnicIScsiNodeInitNameSuffix_Type=SnmpAdminString
_CucsVnicIScsiNodeInitNameSuffix_Object=MibTableColumn
cucsVnicIScsiNodeInitNameSuffix=_CucsVnicIScsiNodeInitNameSuffix_Object((1,3,6,1,4,1,9,9,719,1,53,40,1,7),_CucsVnicIScsiNodeInitNameSuffix_Type())
cucsVnicIScsiNodeInitNameSuffix.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiNodeInitNameSuffix.setStatus(_A)
_CucsVnicIScsiNodeIqnIdentPoolName_Type=SnmpAdminString
_CucsVnicIScsiNodeIqnIdentPoolName_Object=MibTableColumn
cucsVnicIScsiNodeIqnIdentPoolName=_CucsVnicIScsiNodeIqnIdentPoolName_Object((1,3,6,1,4,1,9,9,719,1,53,40,1,8),_CucsVnicIScsiNodeIqnIdentPoolName_Type())
cucsVnicIScsiNodeIqnIdentPoolName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiNodeIqnIdentPoolName.setStatus(_A)
_CucsVnicIScsiNodeOperIqnIdentPoolName_Type=SnmpAdminString
_CucsVnicIScsiNodeOperIqnIdentPoolName_Object=MibTableColumn
cucsVnicIScsiNodeOperIqnIdentPoolName=_CucsVnicIScsiNodeOperIqnIdentPoolName_Object((1,3,6,1,4,1,9,9,719,1,53,40,1,9),_CucsVnicIScsiNodeOperIqnIdentPoolName_Type())
cucsVnicIScsiNodeOperIqnIdentPoolName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiNodeOperIqnIdentPoolName.setStatus(_A)
_CucsVnicIScsiNodeInitiatorPolicyName_Type=SnmpAdminString
_CucsVnicIScsiNodeInitiatorPolicyName_Object=MibTableColumn
cucsVnicIScsiNodeInitiatorPolicyName=_CucsVnicIScsiNodeInitiatorPolicyName_Object((1,3,6,1,4,1,9,9,719,1,53,40,1,10),_CucsVnicIScsiNodeInitiatorPolicyName_Type())
cucsVnicIScsiNodeInitiatorPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiNodeInitiatorPolicyName.setStatus(_A)
_CucsVnicIScsiNodeOperInitiatorPolicyName_Type=SnmpAdminString
_CucsVnicIScsiNodeOperInitiatorPolicyName_Object=MibTableColumn
cucsVnicIScsiNodeOperInitiatorPolicyName=_CucsVnicIScsiNodeOperInitiatorPolicyName_Object((1,3,6,1,4,1,9,9,719,1,53,40,1,11),_CucsVnicIScsiNodeOperInitiatorPolicyName_Type())
cucsVnicIScsiNodeOperInitiatorPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiNodeOperInitiatorPolicyName.setStatus(_A)
_CucsVnicIScsiNodePropAcl_Type=Unsigned64
_CucsVnicIScsiNodePropAcl_Object=MibTableColumn
cucsVnicIScsiNodePropAcl=_CucsVnicIScsiNodePropAcl_Object((1,3,6,1,4,1,9,9,719,1,53,40,1,12),_CucsVnicIScsiNodePropAcl_Type())
cucsVnicIScsiNodePropAcl.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiNodePropAcl.setStatus(_A)
_CucsVnicIScsiStaticTargetIfTable_Object=MibTable
cucsVnicIScsiStaticTargetIfTable=_CucsVnicIScsiStaticTargetIfTable_Object((1,3,6,1,4,1,9,9,719,1,53,41))
if mibBuilder.loadTexts:cucsVnicIScsiStaticTargetIfTable.setStatus(_A)
_CucsVnicIScsiStaticTargetIfEntry_Object=MibTableRow
cucsVnicIScsiStaticTargetIfEntry=_CucsVnicIScsiStaticTargetIfEntry_Object((1,3,6,1,4,1,9,9,719,1,53,41,1))
cucsVnicIScsiStaticTargetIfEntry.setIndexNames((0,_C,_s))
if mibBuilder.loadTexts:cucsVnicIScsiStaticTargetIfEntry.setStatus(_A)
_CucsVnicIScsiStaticTargetIfInstanceId_Type=CucsManagedObjectId
_CucsVnicIScsiStaticTargetIfInstanceId_Object=MibTableColumn
cucsVnicIScsiStaticTargetIfInstanceId=_CucsVnicIScsiStaticTargetIfInstanceId_Object((1,3,6,1,4,1,9,9,719,1,53,41,1,1),_CucsVnicIScsiStaticTargetIfInstanceId_Type())
cucsVnicIScsiStaticTargetIfInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsVnicIScsiStaticTargetIfInstanceId.setStatus(_A)
_CucsVnicIScsiStaticTargetIfDn_Type=CucsManagedObjectDn
_CucsVnicIScsiStaticTargetIfDn_Object=MibTableColumn
cucsVnicIScsiStaticTargetIfDn=_CucsVnicIScsiStaticTargetIfDn_Object((1,3,6,1,4,1,9,9,719,1,53,41,1,2),_CucsVnicIScsiStaticTargetIfDn_Type())
cucsVnicIScsiStaticTargetIfDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiStaticTargetIfDn.setStatus(_A)
_CucsVnicIScsiStaticTargetIfRn_Type=SnmpAdminString
_CucsVnicIScsiStaticTargetIfRn_Object=MibTableColumn
cucsVnicIScsiStaticTargetIfRn=_CucsVnicIScsiStaticTargetIfRn_Object((1,3,6,1,4,1,9,9,719,1,53,41,1,3),_CucsVnicIScsiStaticTargetIfRn_Type())
cucsVnicIScsiStaticTargetIfRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiStaticTargetIfRn.setStatus(_A)
_CucsVnicIScsiStaticTargetIfAuthProfileName_Type=SnmpAdminString
_CucsVnicIScsiStaticTargetIfAuthProfileName_Object=MibTableColumn
cucsVnicIScsiStaticTargetIfAuthProfileName=_CucsVnicIScsiStaticTargetIfAuthProfileName_Object((1,3,6,1,4,1,9,9,719,1,53,41,1,4),_CucsVnicIScsiStaticTargetIfAuthProfileName_Type())
cucsVnicIScsiStaticTargetIfAuthProfileName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiStaticTargetIfAuthProfileName.setStatus(_A)
_CucsVnicIScsiStaticTargetIfIpAddress_Type=InetAddressIPv4
_CucsVnicIScsiStaticTargetIfIpAddress_Object=MibTableColumn
cucsVnicIScsiStaticTargetIfIpAddress=_CucsVnicIScsiStaticTargetIfIpAddress_Object((1,3,6,1,4,1,9,9,719,1,53,41,1,5),_CucsVnicIScsiStaticTargetIfIpAddress_Type())
cucsVnicIScsiStaticTargetIfIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiStaticTargetIfIpAddress.setStatus(_A)
_CucsVnicIScsiStaticTargetIfName_Type=SnmpAdminString
_CucsVnicIScsiStaticTargetIfName_Object=MibTableColumn
cucsVnicIScsiStaticTargetIfName=_CucsVnicIScsiStaticTargetIfName_Object((1,3,6,1,4,1,9,9,719,1,53,41,1,6),_CucsVnicIScsiStaticTargetIfName_Type())
cucsVnicIScsiStaticTargetIfName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiStaticTargetIfName.setStatus(_A)
_CucsVnicIScsiStaticTargetIfOperAuthProfileName_Type=SnmpAdminString
_CucsVnicIScsiStaticTargetIfOperAuthProfileName_Object=MibTableColumn
cucsVnicIScsiStaticTargetIfOperAuthProfileName=_CucsVnicIScsiStaticTargetIfOperAuthProfileName_Object((1,3,6,1,4,1,9,9,719,1,53,41,1,7),_CucsVnicIScsiStaticTargetIfOperAuthProfileName_Type())
cucsVnicIScsiStaticTargetIfOperAuthProfileName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiStaticTargetIfOperAuthProfileName.setStatus(_A)
_CucsVnicIScsiStaticTargetIfPort_Type=Gauge32
_CucsVnicIScsiStaticTargetIfPort_Object=MibTableColumn
cucsVnicIScsiStaticTargetIfPort=_CucsVnicIScsiStaticTargetIfPort_Object((1,3,6,1,4,1,9,9,719,1,53,41,1,8),_CucsVnicIScsiStaticTargetIfPort_Type())
cucsVnicIScsiStaticTargetIfPort.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiStaticTargetIfPort.setStatus(_A)
_CucsVnicIScsiStaticTargetIfPriority_Type=Gauge32
_CucsVnicIScsiStaticTargetIfPriority_Object=MibTableColumn
cucsVnicIScsiStaticTargetIfPriority=_CucsVnicIScsiStaticTargetIfPriority_Object((1,3,6,1,4,1,9,9,719,1,53,41,1,9),_CucsVnicIScsiStaticTargetIfPriority_Type())
cucsVnicIScsiStaticTargetIfPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiStaticTargetIfPriority.setStatus(_A)
_CucsVnicIScsiStaticTargetIfPropAcl_Type=Unsigned64
_CucsVnicIScsiStaticTargetIfPropAcl_Object=MibTableColumn
cucsVnicIScsiStaticTargetIfPropAcl=_CucsVnicIScsiStaticTargetIfPropAcl_Object((1,3,6,1,4,1,9,9,719,1,53,41,1,11),_CucsVnicIScsiStaticTargetIfPropAcl_Type())
cucsVnicIScsiStaticTargetIfPropAcl.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiStaticTargetIfPropAcl.setStatus(_A)
_CucsVnicInternalProfileTable_Object=MibTable
cucsVnicInternalProfileTable=_CucsVnicInternalProfileTable_Object((1,3,6,1,4,1,9,9,719,1,53,42))
if mibBuilder.loadTexts:cucsVnicInternalProfileTable.setStatus(_A)
_CucsVnicInternalProfileEntry_Object=MibTableRow
cucsVnicInternalProfileEntry=_CucsVnicInternalProfileEntry_Object((1,3,6,1,4,1,9,9,719,1,53,42,1))
cucsVnicInternalProfileEntry.setIndexNames((0,_C,_t))
if mibBuilder.loadTexts:cucsVnicInternalProfileEntry.setStatus(_A)
_CucsVnicInternalProfileInstanceId_Type=CucsManagedObjectId
_CucsVnicInternalProfileInstanceId_Object=MibTableColumn
cucsVnicInternalProfileInstanceId=_CucsVnicInternalProfileInstanceId_Object((1,3,6,1,4,1,9,9,719,1,53,42,1,1),_CucsVnicInternalProfileInstanceId_Type())
cucsVnicInternalProfileInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsVnicInternalProfileInstanceId.setStatus(_A)
_CucsVnicInternalProfileDn_Type=CucsManagedObjectDn
_CucsVnicInternalProfileDn_Object=MibTableColumn
cucsVnicInternalProfileDn=_CucsVnicInternalProfileDn_Object((1,3,6,1,4,1,9,9,719,1,53,42,1,2),_CucsVnicInternalProfileDn_Type())
cucsVnicInternalProfileDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicInternalProfileDn.setStatus(_A)
_CucsVnicInternalProfileRn_Type=SnmpAdminString
_CucsVnicInternalProfileRn_Object=MibTableColumn
cucsVnicInternalProfileRn=_CucsVnicInternalProfileRn_Object((1,3,6,1,4,1,9,9,719,1,53,42,1,3),_CucsVnicInternalProfileRn_Type())
cucsVnicInternalProfileRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicInternalProfileRn.setStatus(_A)
_CucsVnicInternalProfileDescr_Type=SnmpAdminString
_CucsVnicInternalProfileDescr_Object=MibTableColumn
cucsVnicInternalProfileDescr=_CucsVnicInternalProfileDescr_Object((1,3,6,1,4,1,9,9,719,1,53,42,1,4),_CucsVnicInternalProfileDescr_Type())
cucsVnicInternalProfileDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicInternalProfileDescr.setStatus(_A)
_CucsVnicInternalProfileIntId_Type=SnmpAdminString
_CucsVnicInternalProfileIntId_Object=MibTableColumn
cucsVnicInternalProfileIntId=_CucsVnicInternalProfileIntId_Object((1,3,6,1,4,1,9,9,719,1,53,42,1,5),_CucsVnicInternalProfileIntId_Type())
cucsVnicInternalProfileIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicInternalProfileIntId.setStatus(_A)
_CucsVnicInternalProfileMaxPorts_Type=Gauge32
_CucsVnicInternalProfileMaxPorts_Object=MibTableColumn
cucsVnicInternalProfileMaxPorts=_CucsVnicInternalProfileMaxPorts_Object((1,3,6,1,4,1,9,9,719,1,53,42,1,6),_CucsVnicInternalProfileMaxPorts_Type())
cucsVnicInternalProfileMaxPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicInternalProfileMaxPorts.setStatus(_A)
_CucsVnicInternalProfileName_Type=SnmpAdminString
_CucsVnicInternalProfileName_Object=MibTableColumn
cucsVnicInternalProfileName=_CucsVnicInternalProfileName_Object((1,3,6,1,4,1,9,9,719,1,53,42,1,7),_CucsVnicInternalProfileName_Type())
cucsVnicInternalProfileName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicInternalProfileName.setStatus(_A)
_CucsVnicInternalProfilePolicyLevel_Type=Gauge32
_CucsVnicInternalProfilePolicyLevel_Object=MibTableColumn
cucsVnicInternalProfilePolicyLevel=_CucsVnicInternalProfilePolicyLevel_Object((1,3,6,1,4,1,9,9,719,1,53,42,1,8),_CucsVnicInternalProfilePolicyLevel_Type())
cucsVnicInternalProfilePolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicInternalProfilePolicyLevel.setStatus(_A)
_CucsVnicInternalProfilePolicyOwner_Type=CucsPolicyPolicyOwner
_CucsVnicInternalProfilePolicyOwner_Object=MibTableColumn
cucsVnicInternalProfilePolicyOwner=_CucsVnicInternalProfilePolicyOwner_Object((1,3,6,1,4,1,9,9,719,1,53,42,1,9),_CucsVnicInternalProfilePolicyOwner_Type())
cucsVnicInternalProfilePolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicInternalProfilePolicyOwner.setStatus(_A)
_CucsVnicLunTable_Object=MibTable
cucsVnicLunTable=_CucsVnicLunTable_Object((1,3,6,1,4,1,9,9,719,1,53,43))
if mibBuilder.loadTexts:cucsVnicLunTable.setStatus(_A)
_CucsVnicLunEntry_Object=MibTableRow
cucsVnicLunEntry=_CucsVnicLunEntry_Object((1,3,6,1,4,1,9,9,719,1,53,43,1))
cucsVnicLunEntry.setIndexNames((0,_C,_u))
if mibBuilder.loadTexts:cucsVnicLunEntry.setStatus(_A)
_CucsVnicLunInstanceId_Type=CucsManagedObjectId
_CucsVnicLunInstanceId_Object=MibTableColumn
cucsVnicLunInstanceId=_CucsVnicLunInstanceId_Object((1,3,6,1,4,1,9,9,719,1,53,43,1,1),_CucsVnicLunInstanceId_Type())
cucsVnicLunInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsVnicLunInstanceId.setStatus(_A)
_CucsVnicLunDn_Type=CucsManagedObjectDn
_CucsVnicLunDn_Object=MibTableColumn
cucsVnicLunDn=_CucsVnicLunDn_Object((1,3,6,1,4,1,9,9,719,1,53,43,1,2),_CucsVnicLunDn_Type())
cucsVnicLunDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicLunDn.setStatus(_A)
_CucsVnicLunRn_Type=SnmpAdminString
_CucsVnicLunRn_Object=MibTableColumn
cucsVnicLunRn=_CucsVnicLunRn_Object((1,3,6,1,4,1,9,9,719,1,53,43,1,3),_CucsVnicLunRn_Type())
cucsVnicLunRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicLunRn.setStatus(_A)
_CucsVnicLunBootable_Type=TruthValue
_CucsVnicLunBootable_Object=MibTableColumn
cucsVnicLunBootable=_CucsVnicLunBootable_Object((1,3,6,1,4,1,9,9,719,1,53,43,1,4),_CucsVnicLunBootable_Type())
cucsVnicLunBootable.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicLunBootable.setStatus(_A)
_CucsVnicLunId_Type=CucsVnicLunId
_CucsVnicLunId_Object=MibTableColumn
cucsVnicLunId=_CucsVnicLunId_Object((1,3,6,1,4,1,9,9,719,1,53,43,1,5),_CucsVnicLunId_Type())
cucsVnicLunId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicLunId.setStatus(_A)
_CucsVnicOProfileAliasTable_Object=MibTable
cucsVnicOProfileAliasTable=_CucsVnicOProfileAliasTable_Object((1,3,6,1,4,1,9,9,719,1,53,44))
if mibBuilder.loadTexts:cucsVnicOProfileAliasTable.setStatus(_A)
_CucsVnicOProfileAliasEntry_Object=MibTableRow
cucsVnicOProfileAliasEntry=_CucsVnicOProfileAliasEntry_Object((1,3,6,1,4,1,9,9,719,1,53,44,1))
cucsVnicOProfileAliasEntry.setIndexNames((0,_C,_v))
if mibBuilder.loadTexts:cucsVnicOProfileAliasEntry.setStatus(_A)
_CucsVnicOProfileAliasInstanceId_Type=CucsManagedObjectId
_CucsVnicOProfileAliasInstanceId_Object=MibTableColumn
cucsVnicOProfileAliasInstanceId=_CucsVnicOProfileAliasInstanceId_Object((1,3,6,1,4,1,9,9,719,1,53,44,1,1),_CucsVnicOProfileAliasInstanceId_Type())
cucsVnicOProfileAliasInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsVnicOProfileAliasInstanceId.setStatus(_A)
_CucsVnicOProfileAliasDn_Type=CucsManagedObjectDn
_CucsVnicOProfileAliasDn_Object=MibTableColumn
cucsVnicOProfileAliasDn=_CucsVnicOProfileAliasDn_Object((1,3,6,1,4,1,9,9,719,1,53,44,1,2),_CucsVnicOProfileAliasDn_Type())
cucsVnicOProfileAliasDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicOProfileAliasDn.setStatus(_A)
_CucsVnicOProfileAliasRn_Type=SnmpAdminString
_CucsVnicOProfileAliasRn_Object=MibTableColumn
cucsVnicOProfileAliasRn=_CucsVnicOProfileAliasRn_Object((1,3,6,1,4,1,9,9,719,1,53,44,1,3),_CucsVnicOProfileAliasRn_Type())
cucsVnicOProfileAliasRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicOProfileAliasRn.setStatus(_A)
_CucsVnicOProfileAliasAlias_Type=SnmpAdminString
_CucsVnicOProfileAliasAlias_Object=MibTableColumn
cucsVnicOProfileAliasAlias=_CucsVnicOProfileAliasAlias_Object((1,3,6,1,4,1,9,9,719,1,53,44,1,4),_CucsVnicOProfileAliasAlias_Type())
cucsVnicOProfileAliasAlias.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicOProfileAliasAlias.setStatus(_A)
_CucsVnicOProfileAliasMgmtPlane_Type=CucsVmMgmtPlane
_CucsVnicOProfileAliasMgmtPlane_Object=MibTableColumn
cucsVnicOProfileAliasMgmtPlane=_CucsVnicOProfileAliasMgmtPlane_Object((1,3,6,1,4,1,9,9,719,1,53,44,1,5),_CucsVnicOProfileAliasMgmtPlane_Type())
cucsVnicOProfileAliasMgmtPlane.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicOProfileAliasMgmtPlane.setStatus(_A)
_CucsVnicOProfileAliasVSwitchId_Type=SnmpAdminString
_CucsVnicOProfileAliasVSwitchId_Object=MibTableColumn
cucsVnicOProfileAliasVSwitchId=_CucsVnicOProfileAliasVSwitchId_Object((1,3,6,1,4,1,9,9,719,1,53,44,1,6),_CucsVnicOProfileAliasVSwitchId_Type())
cucsVnicOProfileAliasVSwitchId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicOProfileAliasVSwitchId.setStatus(_A)
_CucsVnicOProfileAliasVSwitchName_Type=SnmpAdminString
_CucsVnicOProfileAliasVSwitchName_Object=MibTableColumn
cucsVnicOProfileAliasVSwitchName=_CucsVnicOProfileAliasVSwitchName_Object((1,3,6,1,4,1,9,9,719,1,53,44,1,7),_CucsVnicOProfileAliasVSwitchName_Type())
cucsVnicOProfileAliasVSwitchName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicOProfileAliasVSwitchName.setStatus(_A)
_CucsVnicVlanTable_Object=MibTable
cucsVnicVlanTable=_CucsVnicVlanTable_Object((1,3,6,1,4,1,9,9,719,1,53,45))
if mibBuilder.loadTexts:cucsVnicVlanTable.setStatus(_A)
_CucsVnicVlanEntry_Object=MibTableRow
cucsVnicVlanEntry=_CucsVnicVlanEntry_Object((1,3,6,1,4,1,9,9,719,1,53,45,1))
cucsVnicVlanEntry.setIndexNames((0,_C,_w))
if mibBuilder.loadTexts:cucsVnicVlanEntry.setStatus(_A)
_CucsVnicVlanInstanceId_Type=CucsManagedObjectId
_CucsVnicVlanInstanceId_Object=MibTableColumn
cucsVnicVlanInstanceId=_CucsVnicVlanInstanceId_Object((1,3,6,1,4,1,9,9,719,1,53,45,1,1),_CucsVnicVlanInstanceId_Type())
cucsVnicVlanInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsVnicVlanInstanceId.setStatus(_A)
_CucsVnicVlanDn_Type=CucsManagedObjectDn
_CucsVnicVlanDn_Object=MibTableColumn
cucsVnicVlanDn=_CucsVnicVlanDn_Object((1,3,6,1,4,1,9,9,719,1,53,45,1,2),_CucsVnicVlanDn_Type())
cucsVnicVlanDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicVlanDn.setStatus(_A)
_CucsVnicVlanRn_Type=SnmpAdminString
_CucsVnicVlanRn_Object=MibTableColumn
cucsVnicVlanRn=_CucsVnicVlanRn_Object((1,3,6,1,4,1,9,9,719,1,53,45,1,3),_CucsVnicVlanRn_Type())
cucsVnicVlanRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicVlanRn.setStatus(_A)
_CucsVnicVlanFltAggr_Type=Unsigned64
_CucsVnicVlanFltAggr_Object=MibTableColumn
cucsVnicVlanFltAggr=_CucsVnicVlanFltAggr_Object((1,3,6,1,4,1,9,9,719,1,53,45,1,4),_CucsVnicVlanFltAggr_Type())
cucsVnicVlanFltAggr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicVlanFltAggr.setStatus(_A)
_CucsVnicVlanName_Type=SnmpAdminString
_CucsVnicVlanName_Object=MibTableColumn
cucsVnicVlanName=_CucsVnicVlanName_Object((1,3,6,1,4,1,9,9,719,1,53,45,1,5),_CucsVnicVlanName_Type())
cucsVnicVlanName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicVlanName.setStatus(_A)
_CucsVnicVlanOperState_Type=CucsVnicIfOperState
_CucsVnicVlanOperState_Object=MibTableColumn
cucsVnicVlanOperState=_CucsVnicVlanOperState_Object((1,3,6,1,4,1,9,9,719,1,53,45,1,6),_CucsVnicVlanOperState_Type())
cucsVnicVlanOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicVlanOperState.setStatus(_A)
_CucsVnicVlanOwner_Type=CucsVnicConnectionOwner
_CucsVnicVlanOwner_Object=MibTableColumn
cucsVnicVlanOwner=_CucsVnicVlanOwner_Object((1,3,6,1,4,1,9,9,719,1,53,45,1,7),_CucsVnicVlanOwner_Type())
cucsVnicVlanOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicVlanOwner.setStatus(_A)
_CucsVnicVlanSwitchId_Type=CucsNetworkSwitchId
_CucsVnicVlanSwitchId_Object=MibTableColumn
cucsVnicVlanSwitchId=_CucsVnicVlanSwitchId_Object((1,3,6,1,4,1,9,9,719,1,53,45,1,8),_CucsVnicVlanSwitchId_Type())
cucsVnicVlanSwitchId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicVlanSwitchId.setStatus(_A)
_CucsVnicVlanType_Type=CucsVnicConnectionType
_CucsVnicVlanType_Object=MibTableColumn
cucsVnicVlanType=_CucsVnicVlanType_Object((1,3,6,1,4,1,9,9,719,1,53,45,1,9),_CucsVnicVlanType_Type())
cucsVnicVlanType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicVlanType.setStatus(_A)
_CucsVnicVlanVlanName_Type=SnmpAdminString
_CucsVnicVlanVlanName_Object=MibTableColumn
cucsVnicVlanVlanName=_CucsVnicVlanVlanName_Object((1,3,6,1,4,1,9,9,719,1,53,45,1,10),_CucsVnicVlanVlanName_Type())
cucsVnicVlanVlanName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicVlanVlanName.setStatus(_A)
_CucsVnicVlanVnet_Type=Gauge32
_CucsVnicVlanVnet_Object=MibTableColumn
cucsVnicVlanVnet=_CucsVnicVlanVnet_Object((1,3,6,1,4,1,9,9,719,1,53,45,1,11),_CucsVnicVlanVnet_Type())
cucsVnicVlanVnet.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicVlanVnet.setStatus(_A)
_CucsVnicVlanConfigQualifier_Type=CucsVnicConfigIssues
_CucsVnicVlanConfigQualifier_Object=MibTableColumn
cucsVnicVlanConfigQualifier=_CucsVnicVlanConfigQualifier_Object((1,3,6,1,4,1,9,9,719,1,53,45,1,12),_CucsVnicVlanConfigQualifier_Type())
cucsVnicVlanConfigQualifier.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicVlanConfigQualifier.setStatus(_A)
_CucsVnicVlanOperVnetDn_Type=SnmpAdminString
_CucsVnicVlanOperVnetDn_Object=MibTableColumn
cucsVnicVlanOperVnetDn=_CucsVnicVlanOperVnetDn_Object((1,3,6,1,4,1,9,9,719,1,53,45,1,14),_CucsVnicVlanOperVnetDn_Type())
cucsVnicVlanOperVnetDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicVlanOperVnetDn.setStatus(_A)
_CucsVnicVlanOperVnetName_Type=SnmpAdminString
_CucsVnicVlanOperVnetName_Object=MibTableColumn
cucsVnicVlanOperVnetName=_CucsVnicVlanOperVnetName_Object((1,3,6,1,4,1,9,9,719,1,53,45,1,15),_CucsVnicVlanOperVnetName_Type())
cucsVnicVlanOperVnetName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicVlanOperVnetName.setStatus(_A)
_CucsVnicVlanPubNwId_Type=Gauge32
_CucsVnicVlanPubNwId_Object=MibTableColumn
cucsVnicVlanPubNwId=_CucsVnicVlanPubNwId_Object((1,3,6,1,4,1,9,9,719,1,53,45,1,16),_CucsVnicVlanPubNwId_Type())
cucsVnicVlanPubNwId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicVlanPubNwId.setStatus(_A)
_CucsVnicVlanSharing_Type=CucsFabricVlanSharingType
_CucsVnicVlanSharing_Object=MibTableColumn
cucsVnicVlanSharing=_CucsVnicVlanSharing_Object((1,3,6,1,4,1,9,9,719,1,53,45,1,17),_CucsVnicVlanSharing_Type())
cucsVnicVlanSharing.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicVlanSharing.setStatus(_A)
_CucsVnicVlanOperPrimaryVnetDn_Type=SnmpAdminString
_CucsVnicVlanOperPrimaryVnetDn_Object=MibTableColumn
cucsVnicVlanOperPrimaryVnetDn=_CucsVnicVlanOperPrimaryVnetDn_Object((1,3,6,1,4,1,9,9,719,1,53,45,1,18),_CucsVnicVlanOperPrimaryVnetDn_Type())
cucsVnicVlanOperPrimaryVnetDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicVlanOperPrimaryVnetDn.setStatus(_A)
_CucsVnicVlanOperPrimaryVnetName_Type=SnmpAdminString
_CucsVnicVlanOperPrimaryVnetName_Object=MibTableColumn
cucsVnicVlanOperPrimaryVnetName=_CucsVnicVlanOperPrimaryVnetName_Object((1,3,6,1,4,1,9,9,719,1,53,45,1,19),_CucsVnicVlanOperPrimaryVnetName_Type())
cucsVnicVlanOperPrimaryVnetName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicVlanOperPrimaryVnetName.setStatus(_A)
_CucsVnicConnDefTable_Object=MibTable
cucsVnicConnDefTable=_CucsVnicConnDefTable_Object((1,3,6,1,4,1,9,9,719,1,53,46))
if mibBuilder.loadTexts:cucsVnicConnDefTable.setStatus(_A)
_CucsVnicConnDefEntry_Object=MibTableRow
cucsVnicConnDefEntry=_CucsVnicConnDefEntry_Object((1,3,6,1,4,1,9,9,719,1,53,46,1))
cucsVnicConnDefEntry.setIndexNames((0,_C,_x))
if mibBuilder.loadTexts:cucsVnicConnDefEntry.setStatus(_A)
_CucsVnicConnDefInstanceId_Type=CucsManagedObjectId
_CucsVnicConnDefInstanceId_Object=MibTableColumn
cucsVnicConnDefInstanceId=_CucsVnicConnDefInstanceId_Object((1,3,6,1,4,1,9,9,719,1,53,46,1,1),_CucsVnicConnDefInstanceId_Type())
cucsVnicConnDefInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsVnicConnDefInstanceId.setStatus(_A)
_CucsVnicConnDefDn_Type=CucsManagedObjectDn
_CucsVnicConnDefDn_Object=MibTableColumn
cucsVnicConnDefDn=_CucsVnicConnDefDn_Object((1,3,6,1,4,1,9,9,719,1,53,46,1,2),_CucsVnicConnDefDn_Type())
cucsVnicConnDefDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicConnDefDn.setStatus(_A)
_CucsVnicConnDefRn_Type=SnmpAdminString
_CucsVnicConnDefRn_Object=MibTableColumn
cucsVnicConnDefRn=_CucsVnicConnDefRn_Object((1,3,6,1,4,1,9,9,719,1,53,46,1,3),_CucsVnicConnDefRn_Type())
cucsVnicConnDefRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicConnDefRn.setStatus(_A)
_CucsVnicConnDefFltAggr_Type=Unsigned64
_CucsVnicConnDefFltAggr_Object=MibTableColumn
cucsVnicConnDefFltAggr=_CucsVnicConnDefFltAggr_Object((1,3,6,1,4,1,9,9,719,1,53,46,1,4),_CucsVnicConnDefFltAggr_Type())
cucsVnicConnDefFltAggr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicConnDefFltAggr.setStatus(_A)
_CucsVnicConnDefLanConnPolicyName_Type=SnmpAdminString
_CucsVnicConnDefLanConnPolicyName_Object=MibTableColumn
cucsVnicConnDefLanConnPolicyName=_CucsVnicConnDefLanConnPolicyName_Object((1,3,6,1,4,1,9,9,719,1,53,46,1,5),_CucsVnicConnDefLanConnPolicyName_Type())
cucsVnicConnDefLanConnPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicConnDefLanConnPolicyName.setStatus(_A)
_CucsVnicConnDefOperLanConnPolicyName_Type=SnmpAdminString
_CucsVnicConnDefOperLanConnPolicyName_Object=MibTableColumn
cucsVnicConnDefOperLanConnPolicyName=_CucsVnicConnDefOperLanConnPolicyName_Object((1,3,6,1,4,1,9,9,719,1,53,46,1,6),_CucsVnicConnDefOperLanConnPolicyName_Type())
cucsVnicConnDefOperLanConnPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicConnDefOperLanConnPolicyName.setStatus(_A)
_CucsVnicConnDefOperSanConnPolicyName_Type=SnmpAdminString
_CucsVnicConnDefOperSanConnPolicyName_Object=MibTableColumn
cucsVnicConnDefOperSanConnPolicyName=_CucsVnicConnDefOperSanConnPolicyName_Object((1,3,6,1,4,1,9,9,719,1,53,46,1,7),_CucsVnicConnDefOperSanConnPolicyName_Type())
cucsVnicConnDefOperSanConnPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicConnDefOperSanConnPolicyName.setStatus(_A)
_CucsVnicConnDefSanConnPolicyName_Type=SnmpAdminString
_CucsVnicConnDefSanConnPolicyName_Object=MibTableColumn
cucsVnicConnDefSanConnPolicyName=_CucsVnicConnDefSanConnPolicyName_Object((1,3,6,1,4,1,9,9,719,1,53,46,1,8),_CucsVnicConnDefSanConnPolicyName_Type())
cucsVnicConnDefSanConnPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicConnDefSanConnPolicyName.setStatus(_A)
_CucsVnicConnDefPropAcl_Type=Unsigned64
_CucsVnicConnDefPropAcl_Object=MibTableColumn
cucsVnicConnDefPropAcl=_CucsVnicConnDefPropAcl_Object((1,3,6,1,4,1,9,9,719,1,53,46,1,9),_CucsVnicConnDefPropAcl_Type())
cucsVnicConnDefPropAcl.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicConnDefPropAcl.setStatus(_A)
_CucsVnicDynamicConPolicyRefTable_Object=MibTable
cucsVnicDynamicConPolicyRefTable=_CucsVnicDynamicConPolicyRefTable_Object((1,3,6,1,4,1,9,9,719,1,53,47))
if mibBuilder.loadTexts:cucsVnicDynamicConPolicyRefTable.setStatus(_A)
_CucsVnicDynamicConPolicyRefEntry_Object=MibTableRow
cucsVnicDynamicConPolicyRefEntry=_CucsVnicDynamicConPolicyRefEntry_Object((1,3,6,1,4,1,9,9,719,1,53,47,1))
cucsVnicDynamicConPolicyRefEntry.setIndexNames((0,_C,_y))
if mibBuilder.loadTexts:cucsVnicDynamicConPolicyRefEntry.setStatus(_A)
_CucsVnicDynamicConPolicyRefInstanceId_Type=CucsManagedObjectId
_CucsVnicDynamicConPolicyRefInstanceId_Object=MibTableColumn
cucsVnicDynamicConPolicyRefInstanceId=_CucsVnicDynamicConPolicyRefInstanceId_Object((1,3,6,1,4,1,9,9,719,1,53,47,1,1),_CucsVnicDynamicConPolicyRefInstanceId_Type())
cucsVnicDynamicConPolicyRefInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsVnicDynamicConPolicyRefInstanceId.setStatus(_A)
_CucsVnicDynamicConPolicyRefDn_Type=CucsManagedObjectDn
_CucsVnicDynamicConPolicyRefDn_Object=MibTableColumn
cucsVnicDynamicConPolicyRefDn=_CucsVnicDynamicConPolicyRefDn_Object((1,3,6,1,4,1,9,9,719,1,53,47,1,2),_CucsVnicDynamicConPolicyRefDn_Type())
cucsVnicDynamicConPolicyRefDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicDynamicConPolicyRefDn.setStatus(_A)
_CucsVnicDynamicConPolicyRefRn_Type=SnmpAdminString
_CucsVnicDynamicConPolicyRefRn_Object=MibTableColumn
cucsVnicDynamicConPolicyRefRn=_CucsVnicDynamicConPolicyRefRn_Object((1,3,6,1,4,1,9,9,719,1,53,47,1,3),_CucsVnicDynamicConPolicyRefRn_Type())
cucsVnicDynamicConPolicyRefRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicDynamicConPolicyRefRn.setStatus(_A)
_CucsVnicDynamicConPolicyRefConPolicyName_Type=SnmpAdminString
_CucsVnicDynamicConPolicyRefConPolicyName_Object=MibTableColumn
cucsVnicDynamicConPolicyRefConPolicyName=_CucsVnicDynamicConPolicyRefConPolicyName_Object((1,3,6,1,4,1,9,9,719,1,53,47,1,4),_CucsVnicDynamicConPolicyRefConPolicyName_Type())
cucsVnicDynamicConPolicyRefConPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicDynamicConPolicyRefConPolicyName.setStatus(_A)
_CucsVnicDynamicConPolicyRefOperConPolicyName_Type=SnmpAdminString
_CucsVnicDynamicConPolicyRefOperConPolicyName_Object=MibTableColumn
cucsVnicDynamicConPolicyRefOperConPolicyName=_CucsVnicDynamicConPolicyRefOperConPolicyName_Object((1,3,6,1,4,1,9,9,719,1,53,47,1,5),_CucsVnicDynamicConPolicyRefOperConPolicyName_Type())
cucsVnicDynamicConPolicyRefOperConPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicDynamicConPolicyRefOperConPolicyName.setStatus(_A)
_CucsVnicFcGroupDefTable_Object=MibTable
cucsVnicFcGroupDefTable=_CucsVnicFcGroupDefTable_Object((1,3,6,1,4,1,9,9,719,1,53,48))
if mibBuilder.loadTexts:cucsVnicFcGroupDefTable.setStatus(_A)
_CucsVnicFcGroupDefEntry_Object=MibTableRow
cucsVnicFcGroupDefEntry=_CucsVnicFcGroupDefEntry_Object((1,3,6,1,4,1,9,9,719,1,53,48,1))
cucsVnicFcGroupDefEntry.setIndexNames((0,_C,_z))
if mibBuilder.loadTexts:cucsVnicFcGroupDefEntry.setStatus(_A)
_CucsVnicFcGroupDefInstanceId_Type=CucsManagedObjectId
_CucsVnicFcGroupDefInstanceId_Object=MibTableColumn
cucsVnicFcGroupDefInstanceId=_CucsVnicFcGroupDefInstanceId_Object((1,3,6,1,4,1,9,9,719,1,53,48,1,1),_CucsVnicFcGroupDefInstanceId_Type())
cucsVnicFcGroupDefInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsVnicFcGroupDefInstanceId.setStatus(_A)
_CucsVnicFcGroupDefDn_Type=CucsManagedObjectDn
_CucsVnicFcGroupDefDn_Object=MibTableColumn
cucsVnicFcGroupDefDn=_CucsVnicFcGroupDefDn_Object((1,3,6,1,4,1,9,9,719,1,53,48,1,2),_CucsVnicFcGroupDefDn_Type())
cucsVnicFcGroupDefDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcGroupDefDn.setStatus(_A)
_CucsVnicFcGroupDefRn_Type=SnmpAdminString
_CucsVnicFcGroupDefRn_Object=MibTableColumn
cucsVnicFcGroupDefRn=_CucsVnicFcGroupDefRn_Object((1,3,6,1,4,1,9,9,719,1,53,48,1,3),_CucsVnicFcGroupDefRn_Type())
cucsVnicFcGroupDefRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcGroupDefRn.setStatus(_A)
_CucsVnicFcGroupDefAdaptorProfileName_Type=SnmpAdminString
_CucsVnicFcGroupDefAdaptorProfileName_Object=MibTableColumn
cucsVnicFcGroupDefAdaptorProfileName=_CucsVnicFcGroupDefAdaptorProfileName_Object((1,3,6,1,4,1,9,9,719,1,53,48,1,4),_CucsVnicFcGroupDefAdaptorProfileName_Type())
cucsVnicFcGroupDefAdaptorProfileName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcGroupDefAdaptorProfileName.setStatus(_A)
_CucsVnicFcGroupDefDescr_Type=SnmpAdminString
_CucsVnicFcGroupDefDescr_Object=MibTableColumn
cucsVnicFcGroupDefDescr=_CucsVnicFcGroupDefDescr_Object((1,3,6,1,4,1,9,9,719,1,53,48,1,5),_CucsVnicFcGroupDefDescr_Type())
cucsVnicFcGroupDefDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcGroupDefDescr.setStatus(_A)
_CucsVnicFcGroupDefIdentPoolName_Type=SnmpAdminString
_CucsVnicFcGroupDefIdentPoolName_Object=MibTableColumn
cucsVnicFcGroupDefIdentPoolName=_CucsVnicFcGroupDefIdentPoolName_Object((1,3,6,1,4,1,9,9,719,1,53,48,1,6),_CucsVnicFcGroupDefIdentPoolName_Type())
cucsVnicFcGroupDefIdentPoolName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcGroupDefIdentPoolName.setStatus(_A)
_CucsVnicFcGroupDefIntId_Type=SnmpAdminString
_CucsVnicFcGroupDefIntId_Object=MibTableColumn
cucsVnicFcGroupDefIntId=_CucsVnicFcGroupDefIntId_Object((1,3,6,1,4,1,9,9,719,1,53,48,1,7),_CucsVnicFcGroupDefIntId_Type())
cucsVnicFcGroupDefIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcGroupDefIntId.setStatus(_A)
_CucsVnicFcGroupDefMaxDataFieldSize_Type=Gauge32
_CucsVnicFcGroupDefMaxDataFieldSize_Object=MibTableColumn
cucsVnicFcGroupDefMaxDataFieldSize=_CucsVnicFcGroupDefMaxDataFieldSize_Object((1,3,6,1,4,1,9,9,719,1,53,48,1,8),_CucsVnicFcGroupDefMaxDataFieldSize_Type())
cucsVnicFcGroupDefMaxDataFieldSize.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcGroupDefMaxDataFieldSize.setStatus(_A)
_CucsVnicFcGroupDefName_Type=SnmpAdminString
_CucsVnicFcGroupDefName_Object=MibTableColumn
cucsVnicFcGroupDefName=_CucsVnicFcGroupDefName_Object((1,3,6,1,4,1,9,9,719,1,53,48,1,9),_CucsVnicFcGroupDefName_Type())
cucsVnicFcGroupDefName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcGroupDefName.setStatus(_A)
_CucsVnicFcGroupDefNwTemplName_Type=SnmpAdminString
_CucsVnicFcGroupDefNwTemplName_Object=MibTableColumn
cucsVnicFcGroupDefNwTemplName=_CucsVnicFcGroupDefNwTemplName_Object((1,3,6,1,4,1,9,9,719,1,53,48,1,10),_CucsVnicFcGroupDefNwTemplName_Type())
cucsVnicFcGroupDefNwTemplName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcGroupDefNwTemplName.setStatus(_A)
_CucsVnicFcGroupDefOperStatsPolicyName_Type=SnmpAdminString
_CucsVnicFcGroupDefOperStatsPolicyName_Object=MibTableColumn
cucsVnicFcGroupDefOperStatsPolicyName=_CucsVnicFcGroupDefOperStatsPolicyName_Object((1,3,6,1,4,1,9,9,719,1,53,48,1,11),_CucsVnicFcGroupDefOperStatsPolicyName_Type())
cucsVnicFcGroupDefOperStatsPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcGroupDefOperStatsPolicyName.setStatus(_A)
_CucsVnicFcGroupDefOperStorageConnPolicyName_Type=SnmpAdminString
_CucsVnicFcGroupDefOperStorageConnPolicyName_Object=MibTableColumn
cucsVnicFcGroupDefOperStorageConnPolicyName=_CucsVnicFcGroupDefOperStorageConnPolicyName_Object((1,3,6,1,4,1,9,9,719,1,53,48,1,12),_CucsVnicFcGroupDefOperStorageConnPolicyName_Type())
cucsVnicFcGroupDefOperStorageConnPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcGroupDefOperStorageConnPolicyName.setStatus(_A)
_CucsVnicFcGroupDefPolicyLevel_Type=Gauge32
_CucsVnicFcGroupDefPolicyLevel_Object=MibTableColumn
cucsVnicFcGroupDefPolicyLevel=_CucsVnicFcGroupDefPolicyLevel_Object((1,3,6,1,4,1,9,9,719,1,53,48,1,13),_CucsVnicFcGroupDefPolicyLevel_Type())
cucsVnicFcGroupDefPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcGroupDefPolicyLevel.setStatus(_A)
_CucsVnicFcGroupDefPolicyOwner_Type=CucsPolicyPolicyOwner
_CucsVnicFcGroupDefPolicyOwner_Object=MibTableColumn
cucsVnicFcGroupDefPolicyOwner=_CucsVnicFcGroupDefPolicyOwner_Object((1,3,6,1,4,1,9,9,719,1,53,48,1,14),_CucsVnicFcGroupDefPolicyOwner_Type())
cucsVnicFcGroupDefPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcGroupDefPolicyOwner.setStatus(_A)
_CucsVnicFcGroupDefQosPolicyName_Type=SnmpAdminString
_CucsVnicFcGroupDefQosPolicyName_Object=MibTableColumn
cucsVnicFcGroupDefQosPolicyName=_CucsVnicFcGroupDefQosPolicyName_Object((1,3,6,1,4,1,9,9,719,1,53,48,1,15),_CucsVnicFcGroupDefQosPolicyName_Type())
cucsVnicFcGroupDefQosPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcGroupDefQosPolicyName.setStatus(_A)
_CucsVnicFcGroupDefStatsPolicyName_Type=SnmpAdminString
_CucsVnicFcGroupDefStatsPolicyName_Object=MibTableColumn
cucsVnicFcGroupDefStatsPolicyName=_CucsVnicFcGroupDefStatsPolicyName_Object((1,3,6,1,4,1,9,9,719,1,53,48,1,16),_CucsVnicFcGroupDefStatsPolicyName_Type())
cucsVnicFcGroupDefStatsPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcGroupDefStatsPolicyName.setStatus(_A)
_CucsVnicFcGroupDefStorageConnPolicyName_Type=SnmpAdminString
_CucsVnicFcGroupDefStorageConnPolicyName_Object=MibTableColumn
cucsVnicFcGroupDefStorageConnPolicyName=_CucsVnicFcGroupDefStorageConnPolicyName_Object((1,3,6,1,4,1,9,9,719,1,53,48,1,17),_CucsVnicFcGroupDefStorageConnPolicyName_Type())
cucsVnicFcGroupDefStorageConnPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcGroupDefStorageConnPolicyName.setStatus(_A)
_CucsVnicFcGroupTemplTable_Object=MibTable
cucsVnicFcGroupTemplTable=_CucsVnicFcGroupTemplTable_Object((1,3,6,1,4,1,9,9,719,1,53,49))
if mibBuilder.loadTexts:cucsVnicFcGroupTemplTable.setStatus(_A)
_CucsVnicFcGroupTemplEntry_Object=MibTableRow
cucsVnicFcGroupTemplEntry=_CucsVnicFcGroupTemplEntry_Object((1,3,6,1,4,1,9,9,719,1,53,49,1))
cucsVnicFcGroupTemplEntry.setIndexNames((0,_C,_A0))
if mibBuilder.loadTexts:cucsVnicFcGroupTemplEntry.setStatus(_A)
_CucsVnicFcGroupTemplInstanceId_Type=CucsManagedObjectId
_CucsVnicFcGroupTemplInstanceId_Object=MibTableColumn
cucsVnicFcGroupTemplInstanceId=_CucsVnicFcGroupTemplInstanceId_Object((1,3,6,1,4,1,9,9,719,1,53,49,1,1),_CucsVnicFcGroupTemplInstanceId_Type())
cucsVnicFcGroupTemplInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsVnicFcGroupTemplInstanceId.setStatus(_A)
_CucsVnicFcGroupTemplDn_Type=CucsManagedObjectDn
_CucsVnicFcGroupTemplDn_Object=MibTableColumn
cucsVnicFcGroupTemplDn=_CucsVnicFcGroupTemplDn_Object((1,3,6,1,4,1,9,9,719,1,53,49,1,2),_CucsVnicFcGroupTemplDn_Type())
cucsVnicFcGroupTemplDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcGroupTemplDn.setStatus(_A)
_CucsVnicFcGroupTemplRn_Type=SnmpAdminString
_CucsVnicFcGroupTemplRn_Object=MibTableColumn
cucsVnicFcGroupTemplRn=_CucsVnicFcGroupTemplRn_Object((1,3,6,1,4,1,9,9,719,1,53,49,1,3),_CucsVnicFcGroupTemplRn_Type())
cucsVnicFcGroupTemplRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcGroupTemplRn.setStatus(_A)
_CucsVnicFcGroupTemplAdaptorProfileName_Type=SnmpAdminString
_CucsVnicFcGroupTemplAdaptorProfileName_Object=MibTableColumn
cucsVnicFcGroupTemplAdaptorProfileName=_CucsVnicFcGroupTemplAdaptorProfileName_Object((1,3,6,1,4,1,9,9,719,1,53,49,1,4),_CucsVnicFcGroupTemplAdaptorProfileName_Type())
cucsVnicFcGroupTemplAdaptorProfileName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcGroupTemplAdaptorProfileName.setStatus(_A)
_CucsVnicFcGroupTemplDescr_Type=SnmpAdminString
_CucsVnicFcGroupTemplDescr_Object=MibTableColumn
cucsVnicFcGroupTemplDescr=_CucsVnicFcGroupTemplDescr_Object((1,3,6,1,4,1,9,9,719,1,53,49,1,5),_CucsVnicFcGroupTemplDescr_Type())
cucsVnicFcGroupTemplDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcGroupTemplDescr.setStatus(_A)
_CucsVnicFcGroupTemplIdentPoolName_Type=SnmpAdminString
_CucsVnicFcGroupTemplIdentPoolName_Object=MibTableColumn
cucsVnicFcGroupTemplIdentPoolName=_CucsVnicFcGroupTemplIdentPoolName_Object((1,3,6,1,4,1,9,9,719,1,53,49,1,6),_CucsVnicFcGroupTemplIdentPoolName_Type())
cucsVnicFcGroupTemplIdentPoolName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcGroupTemplIdentPoolName.setStatus(_A)
_CucsVnicFcGroupTemplIntId_Type=SnmpAdminString
_CucsVnicFcGroupTemplIntId_Object=MibTableColumn
cucsVnicFcGroupTemplIntId=_CucsVnicFcGroupTemplIntId_Object((1,3,6,1,4,1,9,9,719,1,53,49,1,7),_CucsVnicFcGroupTemplIntId_Type())
cucsVnicFcGroupTemplIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcGroupTemplIntId.setStatus(_A)
_CucsVnicFcGroupTemplMaxDataFieldSize_Type=Gauge32
_CucsVnicFcGroupTemplMaxDataFieldSize_Object=MibTableColumn
cucsVnicFcGroupTemplMaxDataFieldSize=_CucsVnicFcGroupTemplMaxDataFieldSize_Object((1,3,6,1,4,1,9,9,719,1,53,49,1,8),_CucsVnicFcGroupTemplMaxDataFieldSize_Type())
cucsVnicFcGroupTemplMaxDataFieldSize.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcGroupTemplMaxDataFieldSize.setStatus(_A)
_CucsVnicFcGroupTemplName_Type=SnmpAdminString
_CucsVnicFcGroupTemplName_Object=MibTableColumn
cucsVnicFcGroupTemplName=_CucsVnicFcGroupTemplName_Object((1,3,6,1,4,1,9,9,719,1,53,49,1,9),_CucsVnicFcGroupTemplName_Type())
cucsVnicFcGroupTemplName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcGroupTemplName.setStatus(_A)
_CucsVnicFcGroupTemplNwTemplName_Type=SnmpAdminString
_CucsVnicFcGroupTemplNwTemplName_Object=MibTableColumn
cucsVnicFcGroupTemplNwTemplName=_CucsVnicFcGroupTemplNwTemplName_Object((1,3,6,1,4,1,9,9,719,1,53,49,1,10),_CucsVnicFcGroupTemplNwTemplName_Type())
cucsVnicFcGroupTemplNwTemplName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcGroupTemplNwTemplName.setStatus(_A)
_CucsVnicFcGroupTemplOperStatsPolicyName_Type=SnmpAdminString
_CucsVnicFcGroupTemplOperStatsPolicyName_Object=MibTableColumn
cucsVnicFcGroupTemplOperStatsPolicyName=_CucsVnicFcGroupTemplOperStatsPolicyName_Object((1,3,6,1,4,1,9,9,719,1,53,49,1,11),_CucsVnicFcGroupTemplOperStatsPolicyName_Type())
cucsVnicFcGroupTemplOperStatsPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcGroupTemplOperStatsPolicyName.setStatus(_A)
_CucsVnicFcGroupTemplOperStorageConnPolicyName_Type=SnmpAdminString
_CucsVnicFcGroupTemplOperStorageConnPolicyName_Object=MibTableColumn
cucsVnicFcGroupTemplOperStorageConnPolicyName=_CucsVnicFcGroupTemplOperStorageConnPolicyName_Object((1,3,6,1,4,1,9,9,719,1,53,49,1,12),_CucsVnicFcGroupTemplOperStorageConnPolicyName_Type())
cucsVnicFcGroupTemplOperStorageConnPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcGroupTemplOperStorageConnPolicyName.setStatus(_A)
_CucsVnicFcGroupTemplPolicyLevel_Type=Gauge32
_CucsVnicFcGroupTemplPolicyLevel_Object=MibTableColumn
cucsVnicFcGroupTemplPolicyLevel=_CucsVnicFcGroupTemplPolicyLevel_Object((1,3,6,1,4,1,9,9,719,1,53,49,1,13),_CucsVnicFcGroupTemplPolicyLevel_Type())
cucsVnicFcGroupTemplPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcGroupTemplPolicyLevel.setStatus(_A)
_CucsVnicFcGroupTemplPolicyOwner_Type=CucsPolicyPolicyOwner
_CucsVnicFcGroupTemplPolicyOwner_Object=MibTableColumn
cucsVnicFcGroupTemplPolicyOwner=_CucsVnicFcGroupTemplPolicyOwner_Object((1,3,6,1,4,1,9,9,719,1,53,49,1,14),_CucsVnicFcGroupTemplPolicyOwner_Type())
cucsVnicFcGroupTemplPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcGroupTemplPolicyOwner.setStatus(_A)
_CucsVnicFcGroupTemplQosPolicyName_Type=SnmpAdminString
_CucsVnicFcGroupTemplQosPolicyName_Object=MibTableColumn
cucsVnicFcGroupTemplQosPolicyName=_CucsVnicFcGroupTemplQosPolicyName_Object((1,3,6,1,4,1,9,9,719,1,53,49,1,15),_CucsVnicFcGroupTemplQosPolicyName_Type())
cucsVnicFcGroupTemplQosPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcGroupTemplQosPolicyName.setStatus(_A)
_CucsVnicFcGroupTemplStatsPolicyName_Type=SnmpAdminString
_CucsVnicFcGroupTemplStatsPolicyName_Object=MibTableColumn
cucsVnicFcGroupTemplStatsPolicyName=_CucsVnicFcGroupTemplStatsPolicyName_Object((1,3,6,1,4,1,9,9,719,1,53,49,1,16),_CucsVnicFcGroupTemplStatsPolicyName_Type())
cucsVnicFcGroupTemplStatsPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcGroupTemplStatsPolicyName.setStatus(_A)
_CucsVnicFcGroupTemplStorageConnPolicyName_Type=SnmpAdminString
_CucsVnicFcGroupTemplStorageConnPolicyName_Object=MibTableColumn
cucsVnicFcGroupTemplStorageConnPolicyName=_CucsVnicFcGroupTemplStorageConnPolicyName_Object((1,3,6,1,4,1,9,9,719,1,53,49,1,17),_CucsVnicFcGroupTemplStorageConnPolicyName_Type())
cucsVnicFcGroupTemplStorageConnPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcGroupTemplStorageConnPolicyName.setStatus(_A)
_CucsVnicFcGroupTemplTemplType_Type=CucsVnicTemplateType
_CucsVnicFcGroupTemplTemplType_Object=MibTableColumn
cucsVnicFcGroupTemplTemplType=_CucsVnicFcGroupTemplTemplType_Object((1,3,6,1,4,1,9,9,719,1,53,49,1,18),_CucsVnicFcGroupTemplTemplType_Type())
cucsVnicFcGroupTemplTemplType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcGroupTemplTemplType.setStatus(_A)
_CucsVnicFcGroupTemplRedundancyPairType_Type=CucsVnicRedundancyPairType
_CucsVnicFcGroupTemplRedundancyPairType_Object=MibTableColumn
cucsVnicFcGroupTemplRedundancyPairType=_CucsVnicFcGroupTemplRedundancyPairType_Object((1,3,6,1,4,1,9,9,719,1,53,49,1,19),_CucsVnicFcGroupTemplRedundancyPairType_Type())
cucsVnicFcGroupTemplRedundancyPairType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicFcGroupTemplRedundancyPairType.setStatus(_A)
_CucsVnicIScsiBootParamsTable_Object=MibTable
cucsVnicIScsiBootParamsTable=_CucsVnicIScsiBootParamsTable_Object((1,3,6,1,4,1,9,9,719,1,53,50))
if mibBuilder.loadTexts:cucsVnicIScsiBootParamsTable.setStatus(_A)
_CucsVnicIScsiBootParamsEntry_Object=MibTableRow
cucsVnicIScsiBootParamsEntry=_CucsVnicIScsiBootParamsEntry_Object((1,3,6,1,4,1,9,9,719,1,53,50,1))
cucsVnicIScsiBootParamsEntry.setIndexNames((0,_C,_A1))
if mibBuilder.loadTexts:cucsVnicIScsiBootParamsEntry.setStatus(_A)
_CucsVnicIScsiBootParamsInstanceId_Type=CucsManagedObjectId
_CucsVnicIScsiBootParamsInstanceId_Object=MibTableColumn
cucsVnicIScsiBootParamsInstanceId=_CucsVnicIScsiBootParamsInstanceId_Object((1,3,6,1,4,1,9,9,719,1,53,50,1,1),_CucsVnicIScsiBootParamsInstanceId_Type())
cucsVnicIScsiBootParamsInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsVnicIScsiBootParamsInstanceId.setStatus(_A)
_CucsVnicIScsiBootParamsDn_Type=CucsManagedObjectDn
_CucsVnicIScsiBootParamsDn_Object=MibTableColumn
cucsVnicIScsiBootParamsDn=_CucsVnicIScsiBootParamsDn_Object((1,3,6,1,4,1,9,9,719,1,53,50,1,2),_CucsVnicIScsiBootParamsDn_Type())
cucsVnicIScsiBootParamsDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiBootParamsDn.setStatus(_A)
_CucsVnicIScsiBootParamsRn_Type=SnmpAdminString
_CucsVnicIScsiBootParamsRn_Object=MibTableColumn
cucsVnicIScsiBootParamsRn=_CucsVnicIScsiBootParamsRn_Object((1,3,6,1,4,1,9,9,719,1,53,50,1,3),_CucsVnicIScsiBootParamsRn_Type())
cucsVnicIScsiBootParamsRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiBootParamsRn.setStatus(_A)
_CucsVnicIScsiBootParamsDescr_Type=SnmpAdminString
_CucsVnicIScsiBootParamsDescr_Object=MibTableColumn
cucsVnicIScsiBootParamsDescr=_CucsVnicIScsiBootParamsDescr_Object((1,3,6,1,4,1,9,9,719,1,53,50,1,4),_CucsVnicIScsiBootParamsDescr_Type())
cucsVnicIScsiBootParamsDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiBootParamsDescr.setStatus(_A)
_CucsVnicIScsiBootParamsIntId_Type=SnmpAdminString
_CucsVnicIScsiBootParamsIntId_Object=MibTableColumn
cucsVnicIScsiBootParamsIntId=_CucsVnicIScsiBootParamsIntId_Object((1,3,6,1,4,1,9,9,719,1,53,50,1,5),_CucsVnicIScsiBootParamsIntId_Type())
cucsVnicIScsiBootParamsIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiBootParamsIntId.setStatus(_A)
_CucsVnicIScsiBootParamsName_Type=SnmpAdminString
_CucsVnicIScsiBootParamsName_Object=MibTableColumn
cucsVnicIScsiBootParamsName=_CucsVnicIScsiBootParamsName_Object((1,3,6,1,4,1,9,9,719,1,53,50,1,6),_CucsVnicIScsiBootParamsName_Type())
cucsVnicIScsiBootParamsName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiBootParamsName.setStatus(_A)
_CucsVnicIScsiBootParamsPolicyLevel_Type=Gauge32
_CucsVnicIScsiBootParamsPolicyLevel_Object=MibTableColumn
cucsVnicIScsiBootParamsPolicyLevel=_CucsVnicIScsiBootParamsPolicyLevel_Object((1,3,6,1,4,1,9,9,719,1,53,50,1,7),_CucsVnicIScsiBootParamsPolicyLevel_Type())
cucsVnicIScsiBootParamsPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiBootParamsPolicyLevel.setStatus(_A)
_CucsVnicIScsiBootParamsPolicyOwner_Type=CucsPolicyPolicyOwner
_CucsVnicIScsiBootParamsPolicyOwner_Object=MibTableColumn
cucsVnicIScsiBootParamsPolicyOwner=_CucsVnicIScsiBootParamsPolicyOwner_Object((1,3,6,1,4,1,9,9,719,1,53,50,1,8),_CucsVnicIScsiBootParamsPolicyOwner_Type())
cucsVnicIScsiBootParamsPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiBootParamsPolicyOwner.setStatus(_A)
_CucsVnicIScsiBootParamsOwner_Type=CucsLsOwner
_CucsVnicIScsiBootParamsOwner_Object=MibTableColumn
cucsVnicIScsiBootParamsOwner=_CucsVnicIScsiBootParamsOwner_Object((1,3,6,1,4,1,9,9,719,1,53,50,1,9),_CucsVnicIScsiBootParamsOwner_Type())
cucsVnicIScsiBootParamsOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiBootParamsOwner.setStatus(_A)
_CucsVnicIScsiBootParamsPropAcl_Type=Unsigned64
_CucsVnicIScsiBootParamsPropAcl_Object=MibTableColumn
cucsVnicIScsiBootParamsPropAcl=_CucsVnicIScsiBootParamsPropAcl_Object((1,3,6,1,4,1,9,9,719,1,53,50,1,10),_CucsVnicIScsiBootParamsPropAcl_Type())
cucsVnicIScsiBootParamsPropAcl.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiBootParamsPropAcl.setStatus(_A)
_CucsVnicIScsiBootVnicTable_Object=MibTable
cucsVnicIScsiBootVnicTable=_CucsVnicIScsiBootVnicTable_Object((1,3,6,1,4,1,9,9,719,1,53,51))
if mibBuilder.loadTexts:cucsVnicIScsiBootVnicTable.setStatus(_A)
_CucsVnicIScsiBootVnicEntry_Object=MibTableRow
cucsVnicIScsiBootVnicEntry=_CucsVnicIScsiBootVnicEntry_Object((1,3,6,1,4,1,9,9,719,1,53,51,1))
cucsVnicIScsiBootVnicEntry.setIndexNames((0,_C,_A2))
if mibBuilder.loadTexts:cucsVnicIScsiBootVnicEntry.setStatus(_A)
_CucsVnicIScsiBootVnicInstanceId_Type=CucsManagedObjectId
_CucsVnicIScsiBootVnicInstanceId_Object=MibTableColumn
cucsVnicIScsiBootVnicInstanceId=_CucsVnicIScsiBootVnicInstanceId_Object((1,3,6,1,4,1,9,9,719,1,53,51,1,1),_CucsVnicIScsiBootVnicInstanceId_Type())
cucsVnicIScsiBootVnicInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsVnicIScsiBootVnicInstanceId.setStatus(_A)
_CucsVnicIScsiBootVnicDn_Type=CucsManagedObjectDn
_CucsVnicIScsiBootVnicDn_Object=MibTableColumn
cucsVnicIScsiBootVnicDn=_CucsVnicIScsiBootVnicDn_Object((1,3,6,1,4,1,9,9,719,1,53,51,1,2),_CucsVnicIScsiBootVnicDn_Type())
cucsVnicIScsiBootVnicDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiBootVnicDn.setStatus(_A)
_CucsVnicIScsiBootVnicRn_Type=SnmpAdminString
_CucsVnicIScsiBootVnicRn_Object=MibTableColumn
cucsVnicIScsiBootVnicRn=_CucsVnicIScsiBootVnicRn_Object((1,3,6,1,4,1,9,9,719,1,53,51,1,3),_CucsVnicIScsiBootVnicRn_Type())
cucsVnicIScsiBootVnicRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiBootVnicRn.setStatus(_A)
_CucsVnicIScsiBootVnicAuthProfileName_Type=SnmpAdminString
_CucsVnicIScsiBootVnicAuthProfileName_Object=MibTableColumn
cucsVnicIScsiBootVnicAuthProfileName=_CucsVnicIScsiBootVnicAuthProfileName_Object((1,3,6,1,4,1,9,9,719,1,53,51,1,4),_CucsVnicIScsiBootVnicAuthProfileName_Type())
cucsVnicIScsiBootVnicAuthProfileName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiBootVnicAuthProfileName.setStatus(_A)
_CucsVnicIScsiBootVnicDescr_Type=SnmpAdminString
_CucsVnicIScsiBootVnicDescr_Object=MibTableColumn
cucsVnicIScsiBootVnicDescr=_CucsVnicIScsiBootVnicDescr_Object((1,3,6,1,4,1,9,9,719,1,53,51,1,5),_CucsVnicIScsiBootVnicDescr_Type())
cucsVnicIScsiBootVnicDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiBootVnicDescr.setStatus(_A)
_CucsVnicIScsiBootVnicInitiatorName_Type=SnmpAdminString
_CucsVnicIScsiBootVnicInitiatorName_Object=MibTableColumn
cucsVnicIScsiBootVnicInitiatorName=_CucsVnicIScsiBootVnicInitiatorName_Object((1,3,6,1,4,1,9,9,719,1,53,51,1,6),_CucsVnicIScsiBootVnicInitiatorName_Type())
cucsVnicIScsiBootVnicInitiatorName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiBootVnicInitiatorName.setStatus(_A)
_CucsVnicIScsiBootVnicIntId_Type=SnmpAdminString
_CucsVnicIScsiBootVnicIntId_Object=MibTableColumn
cucsVnicIScsiBootVnicIntId=_CucsVnicIScsiBootVnicIntId_Object((1,3,6,1,4,1,9,9,719,1,53,51,1,7),_CucsVnicIScsiBootVnicIntId_Type())
cucsVnicIScsiBootVnicIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiBootVnicIntId.setStatus(_A)
_CucsVnicIScsiBootVnicIqnIdentPoolName_Type=SnmpAdminString
_CucsVnicIScsiBootVnicIqnIdentPoolName_Object=MibTableColumn
cucsVnicIScsiBootVnicIqnIdentPoolName=_CucsVnicIScsiBootVnicIqnIdentPoolName_Object((1,3,6,1,4,1,9,9,719,1,53,51,1,8),_CucsVnicIScsiBootVnicIqnIdentPoolName_Type())
cucsVnicIScsiBootVnicIqnIdentPoolName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiBootVnicIqnIdentPoolName.setStatus(_A)
_CucsVnicIScsiBootVnicName_Type=SnmpAdminString
_CucsVnicIScsiBootVnicName_Object=MibTableColumn
cucsVnicIScsiBootVnicName=_CucsVnicIScsiBootVnicName_Object((1,3,6,1,4,1,9,9,719,1,53,51,1,9),_CucsVnicIScsiBootVnicName_Type())
cucsVnicIScsiBootVnicName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiBootVnicName.setStatus(_A)
_CucsVnicIScsiBootVnicOperAuthProfileName_Type=SnmpAdminString
_CucsVnicIScsiBootVnicOperAuthProfileName_Object=MibTableColumn
cucsVnicIScsiBootVnicOperAuthProfileName=_CucsVnicIScsiBootVnicOperAuthProfileName_Object((1,3,6,1,4,1,9,9,719,1,53,51,1,10),_CucsVnicIScsiBootVnicOperAuthProfileName_Type())
cucsVnicIScsiBootVnicOperAuthProfileName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiBootVnicOperAuthProfileName.setStatus(_A)
_CucsVnicIScsiBootVnicOperIqnIdentPoolName_Type=SnmpAdminString
_CucsVnicIScsiBootVnicOperIqnIdentPoolName_Object=MibTableColumn
cucsVnicIScsiBootVnicOperIqnIdentPoolName=_CucsVnicIScsiBootVnicOperIqnIdentPoolName_Object((1,3,6,1,4,1,9,9,719,1,53,51,1,11),_CucsVnicIScsiBootVnicOperIqnIdentPoolName_Type())
cucsVnicIScsiBootVnicOperIqnIdentPoolName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiBootVnicOperIqnIdentPoolName.setStatus(_A)
_CucsVnicIScsiBootVnicPolicyLevel_Type=Gauge32
_CucsVnicIScsiBootVnicPolicyLevel_Object=MibTableColumn
cucsVnicIScsiBootVnicPolicyLevel=_CucsVnicIScsiBootVnicPolicyLevel_Object((1,3,6,1,4,1,9,9,719,1,53,51,1,12),_CucsVnicIScsiBootVnicPolicyLevel_Type())
cucsVnicIScsiBootVnicPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiBootVnicPolicyLevel.setStatus(_A)
_CucsVnicIScsiBootVnicPolicyOwner_Type=CucsPolicyPolicyOwner
_CucsVnicIScsiBootVnicPolicyOwner_Object=MibTableColumn
cucsVnicIScsiBootVnicPolicyOwner=_CucsVnicIScsiBootVnicPolicyOwner_Object((1,3,6,1,4,1,9,9,719,1,53,51,1,13),_CucsVnicIScsiBootVnicPolicyOwner_Type())
cucsVnicIScsiBootVnicPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiBootVnicPolicyOwner.setStatus(_A)
_CucsVnicIScsiLCPTable_Object=MibTable
cucsVnicIScsiLCPTable=_CucsVnicIScsiLCPTable_Object((1,3,6,1,4,1,9,9,719,1,53,52))
if mibBuilder.loadTexts:cucsVnicIScsiLCPTable.setStatus(_A)
_CucsVnicIScsiLCPEntry_Object=MibTableRow
cucsVnicIScsiLCPEntry=_CucsVnicIScsiLCPEntry_Object((1,3,6,1,4,1,9,9,719,1,53,52,1))
cucsVnicIScsiLCPEntry.setIndexNames((0,_C,_A3))
if mibBuilder.loadTexts:cucsVnicIScsiLCPEntry.setStatus(_A)
_CucsVnicIScsiLCPInstanceId_Type=CucsManagedObjectId
_CucsVnicIScsiLCPInstanceId_Object=MibTableColumn
cucsVnicIScsiLCPInstanceId=_CucsVnicIScsiLCPInstanceId_Object((1,3,6,1,4,1,9,9,719,1,53,52,1,1),_CucsVnicIScsiLCPInstanceId_Type())
cucsVnicIScsiLCPInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsVnicIScsiLCPInstanceId.setStatus(_A)
_CucsVnicIScsiLCPDn_Type=CucsManagedObjectDn
_CucsVnicIScsiLCPDn_Object=MibTableColumn
cucsVnicIScsiLCPDn=_CucsVnicIScsiLCPDn_Object((1,3,6,1,4,1,9,9,719,1,53,52,1,2),_CucsVnicIScsiLCPDn_Type())
cucsVnicIScsiLCPDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiLCPDn.setStatus(_A)
_CucsVnicIScsiLCPRn_Type=SnmpAdminString
_CucsVnicIScsiLCPRn_Object=MibTableColumn
cucsVnicIScsiLCPRn=_CucsVnicIScsiLCPRn_Object((1,3,6,1,4,1,9,9,719,1,53,52,1,3),_CucsVnicIScsiLCPRn_Type())
cucsVnicIScsiLCPRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiLCPRn.setStatus(_A)
_CucsVnicIScsiLCPAdaptorProfileName_Type=SnmpAdminString
_CucsVnicIScsiLCPAdaptorProfileName_Object=MibTableColumn
cucsVnicIScsiLCPAdaptorProfileName=_CucsVnicIScsiLCPAdaptorProfileName_Object((1,3,6,1,4,1,9,9,719,1,53,52,1,4),_CucsVnicIScsiLCPAdaptorProfileName_Type())
cucsVnicIScsiLCPAdaptorProfileName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiLCPAdaptorProfileName.setStatus(_A)
_CucsVnicIScsiLCPAddr_Type=MacAddress
_CucsVnicIScsiLCPAddr_Object=MibTableColumn
cucsVnicIScsiLCPAddr=_CucsVnicIScsiLCPAddr_Object((1,3,6,1,4,1,9,9,719,1,53,52,1,5),_CucsVnicIScsiLCPAddr_Type())
cucsVnicIScsiLCPAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiLCPAddr.setStatus(_A)
_CucsVnicIScsiLCPAdminVcon_Type=SnmpAdminString
_CucsVnicIScsiLCPAdminVcon_Object=MibTableColumn
cucsVnicIScsiLCPAdminVcon=_CucsVnicIScsiLCPAdminVcon_Object((1,3,6,1,4,1,9,9,719,1,53,52,1,6),_CucsVnicIScsiLCPAdminVcon_Type())
cucsVnicIScsiLCPAdminVcon.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiLCPAdminVcon.setStatus(_A)
_CucsVnicIScsiLCPBootDev_Type=CucsVnicVnicBootDev
_CucsVnicIScsiLCPBootDev_Object=MibTableColumn
cucsVnicIScsiLCPBootDev=_CucsVnicIScsiLCPBootDev_Object((1,3,6,1,4,1,9,9,719,1,53,52,1,7),_CucsVnicIScsiLCPBootDev_Type())
cucsVnicIScsiLCPBootDev.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiLCPBootDev.setStatus(_A)
_CucsVnicIScsiLCPConfigQualifier_Type=CucsVnicConfigIssues
_CucsVnicIScsiLCPConfigQualifier_Object=MibTableColumn
cucsVnicIScsiLCPConfigQualifier=_CucsVnicIScsiLCPConfigQualifier_Object((1,3,6,1,4,1,9,9,719,1,53,52,1,8),_CucsVnicIScsiLCPConfigQualifier_Type())
cucsVnicIScsiLCPConfigQualifier.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiLCPConfigQualifier.setStatus(_A)
_CucsVnicIScsiLCPConfigState_Type=CucsLsConfigState
_CucsVnicIScsiLCPConfigState_Object=MibTableColumn
cucsVnicIScsiLCPConfigState=_CucsVnicIScsiLCPConfigState_Object((1,3,6,1,4,1,9,9,719,1,53,52,1,9),_CucsVnicIScsiLCPConfigState_Type())
cucsVnicIScsiLCPConfigState.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiLCPConfigState.setStatus(_A)
_CucsVnicIScsiLCPEquipmentDn_Type=SnmpAdminString
_CucsVnicIScsiLCPEquipmentDn_Object=MibTableColumn
cucsVnicIScsiLCPEquipmentDn=_CucsVnicIScsiLCPEquipmentDn_Object((1,3,6,1,4,1,9,9,719,1,53,52,1,10),_CucsVnicIScsiLCPEquipmentDn_Type())
cucsVnicIScsiLCPEquipmentDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiLCPEquipmentDn.setStatus(_A)
_CucsVnicIScsiLCPFltAggr_Type=Unsigned64
_CucsVnicIScsiLCPFltAggr_Object=MibTableColumn
cucsVnicIScsiLCPFltAggr=_CucsVnicIScsiLCPFltAggr_Object((1,3,6,1,4,1,9,9,719,1,53,52,1,11),_CucsVnicIScsiLCPFltAggr_Type())
cucsVnicIScsiLCPFltAggr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiLCPFltAggr.setStatus(_A)
_CucsVnicIScsiLCPIdentPoolName_Type=SnmpAdminString
_CucsVnicIScsiLCPIdentPoolName_Object=MibTableColumn
cucsVnicIScsiLCPIdentPoolName=_CucsVnicIScsiLCPIdentPoolName_Object((1,3,6,1,4,1,9,9,719,1,53,52,1,12),_CucsVnicIScsiLCPIdentPoolName_Type())
cucsVnicIScsiLCPIdentPoolName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiLCPIdentPoolName.setStatus(_A)
_CucsVnicIScsiLCPInstType_Type=CucsVnicInstantiation
_CucsVnicIScsiLCPInstType_Object=MibTableColumn
cucsVnicIScsiLCPInstType=_CucsVnicIScsiLCPInstType_Object((1,3,6,1,4,1,9,9,719,1,53,52,1,13),_CucsVnicIScsiLCPInstType_Type())
cucsVnicIScsiLCPInstType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiLCPInstType.setStatus(_A)
_CucsVnicIScsiLCPName_Type=SnmpAdminString
_CucsVnicIScsiLCPName_Object=MibTableColumn
cucsVnicIScsiLCPName=_CucsVnicIScsiLCPName_Object((1,3,6,1,4,1,9,9,719,1,53,52,1,14),_CucsVnicIScsiLCPName_Type())
cucsVnicIScsiLCPName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiLCPName.setStatus(_A)
_CucsVnicIScsiLCPNwTemplName_Type=SnmpAdminString
_CucsVnicIScsiLCPNwTemplName_Object=MibTableColumn
cucsVnicIScsiLCPNwTemplName=_CucsVnicIScsiLCPNwTemplName_Object((1,3,6,1,4,1,9,9,719,1,53,52,1,15),_CucsVnicIScsiLCPNwTemplName_Type())
cucsVnicIScsiLCPNwTemplName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiLCPNwTemplName.setStatus(_A)
_CucsVnicIScsiLCPOperAdaptorProfileName_Type=SnmpAdminString
_CucsVnicIScsiLCPOperAdaptorProfileName_Object=MibTableColumn
cucsVnicIScsiLCPOperAdaptorProfileName=_CucsVnicIScsiLCPOperAdaptorProfileName_Object((1,3,6,1,4,1,9,9,719,1,53,52,1,16),_CucsVnicIScsiLCPOperAdaptorProfileName_Type())
cucsVnicIScsiLCPOperAdaptorProfileName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiLCPOperAdaptorProfileName.setStatus(_A)
_CucsVnicIScsiLCPOperIdentPoolName_Type=SnmpAdminString
_CucsVnicIScsiLCPOperIdentPoolName_Object=MibTableColumn
cucsVnicIScsiLCPOperIdentPoolName=_CucsVnicIScsiLCPOperIdentPoolName_Object((1,3,6,1,4,1,9,9,719,1,53,52,1,17),_CucsVnicIScsiLCPOperIdentPoolName_Type())
cucsVnicIScsiLCPOperIdentPoolName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiLCPOperIdentPoolName.setStatus(_A)
_CucsVnicIScsiLCPOperOrder_Type=Gauge32
_CucsVnicIScsiLCPOperOrder_Object=MibTableColumn
cucsVnicIScsiLCPOperOrder=_CucsVnicIScsiLCPOperOrder_Object((1,3,6,1,4,1,9,9,719,1,53,52,1,18),_CucsVnicIScsiLCPOperOrder_Type())
cucsVnicIScsiLCPOperOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiLCPOperOrder.setStatus(_A)
_CucsVnicIScsiLCPOperSpeed_Type=Gauge32
_CucsVnicIScsiLCPOperSpeed_Object=MibTableColumn
cucsVnicIScsiLCPOperSpeed=_CucsVnicIScsiLCPOperSpeed_Object((1,3,6,1,4,1,9,9,719,1,53,52,1,19),_CucsVnicIScsiLCPOperSpeed_Type())
cucsVnicIScsiLCPOperSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiLCPOperSpeed.setStatus(_A)
_CucsVnicIScsiLCPOperStatsPolicyName_Type=SnmpAdminString
_CucsVnicIScsiLCPOperStatsPolicyName_Object=MibTableColumn
cucsVnicIScsiLCPOperStatsPolicyName=_CucsVnicIScsiLCPOperStatsPolicyName_Object((1,3,6,1,4,1,9,9,719,1,53,52,1,20),_CucsVnicIScsiLCPOperStatsPolicyName_Type())
cucsVnicIScsiLCPOperStatsPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiLCPOperStatsPolicyName.setStatus(_A)
_CucsVnicIScsiLCPOperVcon_Type=SnmpAdminString
_CucsVnicIScsiLCPOperVcon_Object=MibTableColumn
cucsVnicIScsiLCPOperVcon=_CucsVnicIScsiLCPOperVcon_Object((1,3,6,1,4,1,9,9,719,1,53,52,1,21),_CucsVnicIScsiLCPOperVcon_Type())
cucsVnicIScsiLCPOperVcon.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiLCPOperVcon.setStatus(_A)
_CucsVnicIScsiLCPOrder_Type=Gauge32
_CucsVnicIScsiLCPOrder_Object=MibTableColumn
cucsVnicIScsiLCPOrder=_CucsVnicIScsiLCPOrder_Object((1,3,6,1,4,1,9,9,719,1,53,52,1,22),_CucsVnicIScsiLCPOrder_Type())
cucsVnicIScsiLCPOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiLCPOrder.setStatus(_A)
_CucsVnicIScsiLCPOwner_Type=CucsVnicConnectionOwner
_CucsVnicIScsiLCPOwner_Object=MibTableColumn
cucsVnicIScsiLCPOwner=_CucsVnicIScsiLCPOwner_Object((1,3,6,1,4,1,9,9,719,1,53,52,1,23),_CucsVnicIScsiLCPOwner_Type())
cucsVnicIScsiLCPOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiLCPOwner.setStatus(_A)
_CucsVnicIScsiLCPPinToGroupName_Type=SnmpAdminString
_CucsVnicIScsiLCPPinToGroupName_Object=MibTableColumn
cucsVnicIScsiLCPPinToGroupName=_CucsVnicIScsiLCPPinToGroupName_Object((1,3,6,1,4,1,9,9,719,1,53,52,1,24),_CucsVnicIScsiLCPPinToGroupName_Type())
cucsVnicIScsiLCPPinToGroupName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiLCPPinToGroupName.setStatus(_A)
_CucsVnicIScsiLCPQosPolicyName_Type=SnmpAdminString
_CucsVnicIScsiLCPQosPolicyName_Object=MibTableColumn
cucsVnicIScsiLCPQosPolicyName=_CucsVnicIScsiLCPQosPolicyName_Object((1,3,6,1,4,1,9,9,719,1,53,52,1,25),_CucsVnicIScsiLCPQosPolicyName_Type())
cucsVnicIScsiLCPQosPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiLCPQosPolicyName.setStatus(_A)
_CucsVnicIScsiLCPStatsPolicyName_Type=SnmpAdminString
_CucsVnicIScsiLCPStatsPolicyName_Object=MibTableColumn
cucsVnicIScsiLCPStatsPolicyName=_CucsVnicIScsiLCPStatsPolicyName_Object((1,3,6,1,4,1,9,9,719,1,53,52,1,26),_CucsVnicIScsiLCPStatsPolicyName_Type())
cucsVnicIScsiLCPStatsPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiLCPStatsPolicyName.setStatus(_A)
_CucsVnicIScsiLCPSwitchId_Type=CucsNetworkSwitchId
_CucsVnicIScsiLCPSwitchId_Object=MibTableColumn
cucsVnicIScsiLCPSwitchId=_CucsVnicIScsiLCPSwitchId_Object((1,3,6,1,4,1,9,9,719,1,53,52,1,27),_CucsVnicIScsiLCPSwitchId_Type())
cucsVnicIScsiLCPSwitchId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiLCPSwitchId.setStatus(_A)
_CucsVnicIScsiLCPType_Type=CucsVnicConnectionType
_CucsVnicIScsiLCPType_Object=MibTableColumn
cucsVnicIScsiLCPType=_CucsVnicIScsiLCPType_Object((1,3,6,1,4,1,9,9,719,1,53,52,1,28),_CucsVnicIScsiLCPType_Type())
cucsVnicIScsiLCPType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiLCPType.setStatus(_A)
_CucsVnicIScsiLCPVnicName_Type=SnmpAdminString
_CucsVnicIScsiLCPVnicName_Object=MibTableColumn
cucsVnicIScsiLCPVnicName=_CucsVnicIScsiLCPVnicName_Object((1,3,6,1,4,1,9,9,719,1,53,52,1,29),_CucsVnicIScsiLCPVnicName_Type())
cucsVnicIScsiLCPVnicName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiLCPVnicName.setStatus(_A)
_CucsVnicIScsiLCPAdminHostPort_Type=CucsFabricHostPortId
_CucsVnicIScsiLCPAdminHostPort_Object=MibTableColumn
cucsVnicIScsiLCPAdminHostPort=_CucsVnicIScsiLCPAdminHostPort_Object((1,3,6,1,4,1,9,9,719,1,53,52,1,31),_CucsVnicIScsiLCPAdminHostPort_Type())
cucsVnicIScsiLCPAdminHostPort.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiLCPAdminHostPort.setStatus(_A)
_CucsVnicIScsiLCPOperHostPort_Type=CucsVnicVnicOperHostPort
_CucsVnicIScsiLCPOperHostPort_Object=MibTableColumn
cucsVnicIScsiLCPOperHostPort=_CucsVnicIScsiLCPOperHostPort_Object((1,3,6,1,4,1,9,9,719,1,53,52,1,32),_CucsVnicIScsiLCPOperHostPort_Type())
cucsVnicIScsiLCPOperHostPort.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiLCPOperHostPort.setStatus(_A)
_CucsVnicIScsiLCPAdminCdnName_Type=SnmpAdminString
_CucsVnicIScsiLCPAdminCdnName_Object=MibTableColumn
cucsVnicIScsiLCPAdminCdnName=_CucsVnicIScsiLCPAdminCdnName_Object((1,3,6,1,4,1,9,9,719,1,53,52,1,33),_CucsVnicIScsiLCPAdminCdnName_Type())
cucsVnicIScsiLCPAdminCdnName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiLCPAdminCdnName.setStatus(_A)
_CucsVnicIScsiLCPOperCdnName_Type=SnmpAdminString
_CucsVnicIScsiLCPOperCdnName_Object=MibTableColumn
cucsVnicIScsiLCPOperCdnName=_CucsVnicIScsiLCPOperCdnName_Object((1,3,6,1,4,1,9,9,719,1,53,52,1,34),_CucsVnicIScsiLCPOperCdnName_Type())
cucsVnicIScsiLCPOperCdnName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiLCPOperCdnName.setStatus(_A)
_CucsVnicIScsiLCPCdnSource_Type=CucsVnicCdnSource
_CucsVnicIScsiLCPCdnSource_Object=MibTableColumn
cucsVnicIScsiLCPCdnSource=_CucsVnicIScsiLCPCdnSource_Object((1,3,6,1,4,1,9,9,719,1,53,52,1,35),_CucsVnicIScsiLCPCdnSource_Type())
cucsVnicIScsiLCPCdnSource.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiLCPCdnSource.setStatus(_A)
_CucsVnicIScsiLCPCdnPropInSync_Type=TruthValue
_CucsVnicIScsiLCPCdnPropInSync_Object=MibTableColumn
cucsVnicIScsiLCPCdnPropInSync=_CucsVnicIScsiLCPCdnPropInSync_Object((1,3,6,1,4,1,9,9,719,1,53,52,1,36),_CucsVnicIScsiLCPCdnPropInSync_Type())
cucsVnicIScsiLCPCdnPropInSync.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiLCPCdnPropInSync.setStatus(_A)
_CucsVnicIScsiLCPRedundancyPairType_Type=CucsVnicRedundancyPairType
_CucsVnicIScsiLCPRedundancyPairType_Object=MibTableColumn
cucsVnicIScsiLCPRedundancyPairType=_CucsVnicIScsiLCPRedundancyPairType_Object((1,3,6,1,4,1,9,9,719,1,53,52,1,37),_CucsVnicIScsiLCPRedundancyPairType_Type())
cucsVnicIScsiLCPRedundancyPairType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiLCPRedundancyPairType.setStatus(_A)
_CucsVnicIScsiLCPRedundancyPeer_Type=SnmpAdminString
_CucsVnicIScsiLCPRedundancyPeer_Object=MibTableColumn
cucsVnicIScsiLCPRedundancyPeer=_CucsVnicIScsiLCPRedundancyPeer_Object((1,3,6,1,4,1,9,9,719,1,53,52,1,38),_CucsVnicIScsiLCPRedundancyPeer_Type())
cucsVnicIScsiLCPRedundancyPeer.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiLCPRedundancyPeer.setStatus(_A)
_CucsVnicLanConnPolicyTable_Object=MibTable
cucsVnicLanConnPolicyTable=_CucsVnicLanConnPolicyTable_Object((1,3,6,1,4,1,9,9,719,1,53,53))
if mibBuilder.loadTexts:cucsVnicLanConnPolicyTable.setStatus(_A)
_CucsVnicLanConnPolicyEntry_Object=MibTableRow
cucsVnicLanConnPolicyEntry=_CucsVnicLanConnPolicyEntry_Object((1,3,6,1,4,1,9,9,719,1,53,53,1))
cucsVnicLanConnPolicyEntry.setIndexNames((0,_C,_A4))
if mibBuilder.loadTexts:cucsVnicLanConnPolicyEntry.setStatus(_A)
_CucsVnicLanConnPolicyInstanceId_Type=CucsManagedObjectId
_CucsVnicLanConnPolicyInstanceId_Object=MibTableColumn
cucsVnicLanConnPolicyInstanceId=_CucsVnicLanConnPolicyInstanceId_Object((1,3,6,1,4,1,9,9,719,1,53,53,1,1),_CucsVnicLanConnPolicyInstanceId_Type())
cucsVnicLanConnPolicyInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsVnicLanConnPolicyInstanceId.setStatus(_A)
_CucsVnicLanConnPolicyDn_Type=CucsManagedObjectDn
_CucsVnicLanConnPolicyDn_Object=MibTableColumn
cucsVnicLanConnPolicyDn=_CucsVnicLanConnPolicyDn_Object((1,3,6,1,4,1,9,9,719,1,53,53,1,2),_CucsVnicLanConnPolicyDn_Type())
cucsVnicLanConnPolicyDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicLanConnPolicyDn.setStatus(_A)
_CucsVnicLanConnPolicyRn_Type=SnmpAdminString
_CucsVnicLanConnPolicyRn_Object=MibTableColumn
cucsVnicLanConnPolicyRn=_CucsVnicLanConnPolicyRn_Object((1,3,6,1,4,1,9,9,719,1,53,53,1,3),_CucsVnicLanConnPolicyRn_Type())
cucsVnicLanConnPolicyRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicLanConnPolicyRn.setStatus(_A)
_CucsVnicLanConnPolicyDescr_Type=SnmpAdminString
_CucsVnicLanConnPolicyDescr_Object=MibTableColumn
cucsVnicLanConnPolicyDescr=_CucsVnicLanConnPolicyDescr_Object((1,3,6,1,4,1,9,9,719,1,53,53,1,4),_CucsVnicLanConnPolicyDescr_Type())
cucsVnicLanConnPolicyDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicLanConnPolicyDescr.setStatus(_A)
_CucsVnicLanConnPolicyFltAggr_Type=Unsigned64
_CucsVnicLanConnPolicyFltAggr_Object=MibTableColumn
cucsVnicLanConnPolicyFltAggr=_CucsVnicLanConnPolicyFltAggr_Object((1,3,6,1,4,1,9,9,719,1,53,53,1,5),_CucsVnicLanConnPolicyFltAggr_Type())
cucsVnicLanConnPolicyFltAggr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicLanConnPolicyFltAggr.setStatus(_A)
_CucsVnicLanConnPolicyIntId_Type=SnmpAdminString
_CucsVnicLanConnPolicyIntId_Object=MibTableColumn
cucsVnicLanConnPolicyIntId=_CucsVnicLanConnPolicyIntId_Object((1,3,6,1,4,1,9,9,719,1,53,53,1,6),_CucsVnicLanConnPolicyIntId_Type())
cucsVnicLanConnPolicyIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicLanConnPolicyIntId.setStatus(_A)
_CucsVnicLanConnPolicyName_Type=SnmpAdminString
_CucsVnicLanConnPolicyName_Object=MibTableColumn
cucsVnicLanConnPolicyName=_CucsVnicLanConnPolicyName_Object((1,3,6,1,4,1,9,9,719,1,53,53,1,7),_CucsVnicLanConnPolicyName_Type())
cucsVnicLanConnPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicLanConnPolicyName.setStatus(_A)
_CucsVnicLanConnPolicyPolicyLevel_Type=Gauge32
_CucsVnicLanConnPolicyPolicyLevel_Object=MibTableColumn
cucsVnicLanConnPolicyPolicyLevel=_CucsVnicLanConnPolicyPolicyLevel_Object((1,3,6,1,4,1,9,9,719,1,53,53,1,8),_CucsVnicLanConnPolicyPolicyLevel_Type())
cucsVnicLanConnPolicyPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicLanConnPolicyPolicyLevel.setStatus(_A)
_CucsVnicLanConnPolicyPolicyOwner_Type=CucsPolicyPolicyOwner
_CucsVnicLanConnPolicyPolicyOwner_Object=MibTableColumn
cucsVnicLanConnPolicyPolicyOwner=_CucsVnicLanConnPolicyPolicyOwner_Object((1,3,6,1,4,1,9,9,719,1,53,53,1,9),_CucsVnicLanConnPolicyPolicyOwner_Type())
cucsVnicLanConnPolicyPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicLanConnPolicyPolicyOwner.setStatus(_A)
_CucsVnicProfileSetFsmTable_Object=MibTable
cucsVnicProfileSetFsmTable=_CucsVnicProfileSetFsmTable_Object((1,3,6,1,4,1,9,9,719,1,53,54))
if mibBuilder.loadTexts:cucsVnicProfileSetFsmTable.setStatus(_A)
_CucsVnicProfileSetFsmEntry_Object=MibTableRow
cucsVnicProfileSetFsmEntry=_CucsVnicProfileSetFsmEntry_Object((1,3,6,1,4,1,9,9,719,1,53,54,1))
cucsVnicProfileSetFsmEntry.setIndexNames((0,_C,_A5))
if mibBuilder.loadTexts:cucsVnicProfileSetFsmEntry.setStatus(_A)
_CucsVnicProfileSetFsmInstanceId_Type=CucsManagedObjectId
_CucsVnicProfileSetFsmInstanceId_Object=MibTableColumn
cucsVnicProfileSetFsmInstanceId=_CucsVnicProfileSetFsmInstanceId_Object((1,3,6,1,4,1,9,9,719,1,53,54,1,1),_CucsVnicProfileSetFsmInstanceId_Type())
cucsVnicProfileSetFsmInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsVnicProfileSetFsmInstanceId.setStatus(_A)
_CucsVnicProfileSetFsmDn_Type=CucsManagedObjectDn
_CucsVnicProfileSetFsmDn_Object=MibTableColumn
cucsVnicProfileSetFsmDn=_CucsVnicProfileSetFsmDn_Object((1,3,6,1,4,1,9,9,719,1,53,54,1,2),_CucsVnicProfileSetFsmDn_Type())
cucsVnicProfileSetFsmDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicProfileSetFsmDn.setStatus(_A)
_CucsVnicProfileSetFsmRn_Type=SnmpAdminString
_CucsVnicProfileSetFsmRn_Object=MibTableColumn
cucsVnicProfileSetFsmRn=_CucsVnicProfileSetFsmRn_Object((1,3,6,1,4,1,9,9,719,1,53,54,1,3),_CucsVnicProfileSetFsmRn_Type())
cucsVnicProfileSetFsmRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicProfileSetFsmRn.setStatus(_A)
_CucsVnicProfileSetFsmCompletionTime_Type=DateAndTime
_CucsVnicProfileSetFsmCompletionTime_Object=MibTableColumn
cucsVnicProfileSetFsmCompletionTime=_CucsVnicProfileSetFsmCompletionTime_Object((1,3,6,1,4,1,9,9,719,1,53,54,1,4),_CucsVnicProfileSetFsmCompletionTime_Type())
cucsVnicProfileSetFsmCompletionTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicProfileSetFsmCompletionTime.setStatus(_A)
_CucsVnicProfileSetFsmCurrentFsm_Type=CucsVnicProfileSetFsmCurrentFsm
_CucsVnicProfileSetFsmCurrentFsm_Object=MibTableColumn
cucsVnicProfileSetFsmCurrentFsm=_CucsVnicProfileSetFsmCurrentFsm_Object((1,3,6,1,4,1,9,9,719,1,53,54,1,5),_CucsVnicProfileSetFsmCurrentFsm_Type())
cucsVnicProfileSetFsmCurrentFsm.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicProfileSetFsmCurrentFsm.setStatus(_A)
_CucsVnicProfileSetFsmDescrData_Type=SnmpAdminString
_CucsVnicProfileSetFsmDescrData_Object=MibTableColumn
cucsVnicProfileSetFsmDescrData=_CucsVnicProfileSetFsmDescrData_Object((1,3,6,1,4,1,9,9,719,1,53,54,1,6),_CucsVnicProfileSetFsmDescrData_Type())
cucsVnicProfileSetFsmDescrData.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicProfileSetFsmDescrData.setStatus(_A)
_CucsVnicProfileSetFsmFsmStatus_Type=CucsFsmFsmStageStatus
_CucsVnicProfileSetFsmFsmStatus_Object=MibTableColumn
cucsVnicProfileSetFsmFsmStatus=_CucsVnicProfileSetFsmFsmStatus_Object((1,3,6,1,4,1,9,9,719,1,53,54,1,7),_CucsVnicProfileSetFsmFsmStatus_Type())
cucsVnicProfileSetFsmFsmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicProfileSetFsmFsmStatus.setStatus(_A)
_CucsVnicProfileSetFsmProgress_Type=Gauge32
_CucsVnicProfileSetFsmProgress_Object=MibTableColumn
cucsVnicProfileSetFsmProgress=_CucsVnicProfileSetFsmProgress_Object((1,3,6,1,4,1,9,9,719,1,53,54,1,8),_CucsVnicProfileSetFsmProgress_Type())
cucsVnicProfileSetFsmProgress.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicProfileSetFsmProgress.setStatus(_A)
_CucsVnicProfileSetFsmRmtErrCode_Type=Gauge32
_CucsVnicProfileSetFsmRmtErrCode_Object=MibTableColumn
cucsVnicProfileSetFsmRmtErrCode=_CucsVnicProfileSetFsmRmtErrCode_Object((1,3,6,1,4,1,9,9,719,1,53,54,1,9),_CucsVnicProfileSetFsmRmtErrCode_Type())
cucsVnicProfileSetFsmRmtErrCode.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicProfileSetFsmRmtErrCode.setStatus(_A)
_CucsVnicProfileSetFsmRmtErrDescr_Type=SnmpAdminString
_CucsVnicProfileSetFsmRmtErrDescr_Object=MibTableColumn
cucsVnicProfileSetFsmRmtErrDescr=_CucsVnicProfileSetFsmRmtErrDescr_Object((1,3,6,1,4,1,9,9,719,1,53,54,1,10),_CucsVnicProfileSetFsmRmtErrDescr_Type())
cucsVnicProfileSetFsmRmtErrDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicProfileSetFsmRmtErrDescr.setStatus(_A)
_CucsVnicProfileSetFsmRmtRslt_Type=CucsConditionRemoteInvRslt
_CucsVnicProfileSetFsmRmtRslt_Object=MibTableColumn
cucsVnicProfileSetFsmRmtRslt=_CucsVnicProfileSetFsmRmtRslt_Object((1,3,6,1,4,1,9,9,719,1,53,54,1,11),_CucsVnicProfileSetFsmRmtRslt_Type())
cucsVnicProfileSetFsmRmtRslt.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicProfileSetFsmRmtRslt.setStatus(_A)
_CucsVnicProfileSetFsmStageTable_Object=MibTable
cucsVnicProfileSetFsmStageTable=_CucsVnicProfileSetFsmStageTable_Object((1,3,6,1,4,1,9,9,719,1,53,55))
if mibBuilder.loadTexts:cucsVnicProfileSetFsmStageTable.setStatus(_A)
_CucsVnicProfileSetFsmStageEntry_Object=MibTableRow
cucsVnicProfileSetFsmStageEntry=_CucsVnicProfileSetFsmStageEntry_Object((1,3,6,1,4,1,9,9,719,1,53,55,1))
cucsVnicProfileSetFsmStageEntry.setIndexNames((0,_C,_A6))
if mibBuilder.loadTexts:cucsVnicProfileSetFsmStageEntry.setStatus(_A)
_CucsVnicProfileSetFsmStageInstanceId_Type=CucsManagedObjectId
_CucsVnicProfileSetFsmStageInstanceId_Object=MibTableColumn
cucsVnicProfileSetFsmStageInstanceId=_CucsVnicProfileSetFsmStageInstanceId_Object((1,3,6,1,4,1,9,9,719,1,53,55,1,1),_CucsVnicProfileSetFsmStageInstanceId_Type())
cucsVnicProfileSetFsmStageInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsVnicProfileSetFsmStageInstanceId.setStatus(_A)
_CucsVnicProfileSetFsmStageDn_Type=CucsManagedObjectDn
_CucsVnicProfileSetFsmStageDn_Object=MibTableColumn
cucsVnicProfileSetFsmStageDn=_CucsVnicProfileSetFsmStageDn_Object((1,3,6,1,4,1,9,9,719,1,53,55,1,2),_CucsVnicProfileSetFsmStageDn_Type())
cucsVnicProfileSetFsmStageDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicProfileSetFsmStageDn.setStatus(_A)
_CucsVnicProfileSetFsmStageRn_Type=SnmpAdminString
_CucsVnicProfileSetFsmStageRn_Object=MibTableColumn
cucsVnicProfileSetFsmStageRn=_CucsVnicProfileSetFsmStageRn_Object((1,3,6,1,4,1,9,9,719,1,53,55,1,3),_CucsVnicProfileSetFsmStageRn_Type())
cucsVnicProfileSetFsmStageRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicProfileSetFsmStageRn.setStatus(_A)
_CucsVnicProfileSetFsmStageDescrData_Type=SnmpAdminString
_CucsVnicProfileSetFsmStageDescrData_Object=MibTableColumn
cucsVnicProfileSetFsmStageDescrData=_CucsVnicProfileSetFsmStageDescrData_Object((1,3,6,1,4,1,9,9,719,1,53,55,1,4),_CucsVnicProfileSetFsmStageDescrData_Type())
cucsVnicProfileSetFsmStageDescrData.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicProfileSetFsmStageDescrData.setStatus(_A)
_CucsVnicProfileSetFsmStageLastUpdateTime_Type=DateAndTime
_CucsVnicProfileSetFsmStageLastUpdateTime_Object=MibTableColumn
cucsVnicProfileSetFsmStageLastUpdateTime=_CucsVnicProfileSetFsmStageLastUpdateTime_Object((1,3,6,1,4,1,9,9,719,1,53,55,1,5),_CucsVnicProfileSetFsmStageLastUpdateTime_Type())
cucsVnicProfileSetFsmStageLastUpdateTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicProfileSetFsmStageLastUpdateTime.setStatus(_A)
_CucsVnicProfileSetFsmStageName_Type=CucsVnicProfileSetFsmStageName
_CucsVnicProfileSetFsmStageName_Object=MibTableColumn
cucsVnicProfileSetFsmStageName=_CucsVnicProfileSetFsmStageName_Object((1,3,6,1,4,1,9,9,719,1,53,55,1,6),_CucsVnicProfileSetFsmStageName_Type())
cucsVnicProfileSetFsmStageName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicProfileSetFsmStageName.setStatus(_A)
_CucsVnicProfileSetFsmStageOrder_Type=Gauge32
_CucsVnicProfileSetFsmStageOrder_Object=MibTableColumn
cucsVnicProfileSetFsmStageOrder=_CucsVnicProfileSetFsmStageOrder_Object((1,3,6,1,4,1,9,9,719,1,53,55,1,7),_CucsVnicProfileSetFsmStageOrder_Type())
cucsVnicProfileSetFsmStageOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicProfileSetFsmStageOrder.setStatus(_A)
_CucsVnicProfileSetFsmStageRetry_Type=Gauge32
_CucsVnicProfileSetFsmStageRetry_Object=MibTableColumn
cucsVnicProfileSetFsmStageRetry=_CucsVnicProfileSetFsmStageRetry_Object((1,3,6,1,4,1,9,9,719,1,53,55,1,8),_CucsVnicProfileSetFsmStageRetry_Type())
cucsVnicProfileSetFsmStageRetry.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicProfileSetFsmStageRetry.setStatus(_A)
_CucsVnicProfileSetFsmStageStageStatus_Type=CucsFsmFsmStageStatus
_CucsVnicProfileSetFsmStageStageStatus_Object=MibTableColumn
cucsVnicProfileSetFsmStageStageStatus=_CucsVnicProfileSetFsmStageStageStatus_Object((1,3,6,1,4,1,9,9,719,1,53,55,1,9),_CucsVnicProfileSetFsmStageStageStatus_Type())
cucsVnicProfileSetFsmStageStageStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicProfileSetFsmStageStageStatus.setStatus(_A)
_CucsVnicRackServerDiscoveryProfileTable_Object=MibTable
cucsVnicRackServerDiscoveryProfileTable=_CucsVnicRackServerDiscoveryProfileTable_Object((1,3,6,1,4,1,9,9,719,1,53,56))
if mibBuilder.loadTexts:cucsVnicRackServerDiscoveryProfileTable.setStatus(_A)
_CucsVnicRackServerDiscoveryProfileEntry_Object=MibTableRow
cucsVnicRackServerDiscoveryProfileEntry=_CucsVnicRackServerDiscoveryProfileEntry_Object((1,3,6,1,4,1,9,9,719,1,53,56,1))
cucsVnicRackServerDiscoveryProfileEntry.setIndexNames((0,_C,_A7))
if mibBuilder.loadTexts:cucsVnicRackServerDiscoveryProfileEntry.setStatus(_A)
_CucsVnicRackServerDiscoveryProfileInstanceId_Type=CucsManagedObjectId
_CucsVnicRackServerDiscoveryProfileInstanceId_Object=MibTableColumn
cucsVnicRackServerDiscoveryProfileInstanceId=_CucsVnicRackServerDiscoveryProfileInstanceId_Object((1,3,6,1,4,1,9,9,719,1,53,56,1,1),_CucsVnicRackServerDiscoveryProfileInstanceId_Type())
cucsVnicRackServerDiscoveryProfileInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsVnicRackServerDiscoveryProfileInstanceId.setStatus(_A)
_CucsVnicRackServerDiscoveryProfileDn_Type=CucsManagedObjectDn
_CucsVnicRackServerDiscoveryProfileDn_Object=MibTableColumn
cucsVnicRackServerDiscoveryProfileDn=_CucsVnicRackServerDiscoveryProfileDn_Object((1,3,6,1,4,1,9,9,719,1,53,56,1,2),_CucsVnicRackServerDiscoveryProfileDn_Type())
cucsVnicRackServerDiscoveryProfileDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicRackServerDiscoveryProfileDn.setStatus(_A)
_CucsVnicRackServerDiscoveryProfileRn_Type=SnmpAdminString
_CucsVnicRackServerDiscoveryProfileRn_Object=MibTableColumn
cucsVnicRackServerDiscoveryProfileRn=_CucsVnicRackServerDiscoveryProfileRn_Object((1,3,6,1,4,1,9,9,719,1,53,56,1,3),_CucsVnicRackServerDiscoveryProfileRn_Type())
cucsVnicRackServerDiscoveryProfileRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicRackServerDiscoveryProfileRn.setStatus(_A)
_CucsVnicRackServerDiscoveryProfileDescr_Type=SnmpAdminString
_CucsVnicRackServerDiscoveryProfileDescr_Object=MibTableColumn
cucsVnicRackServerDiscoveryProfileDescr=_CucsVnicRackServerDiscoveryProfileDescr_Object((1,3,6,1,4,1,9,9,719,1,53,56,1,4),_CucsVnicRackServerDiscoveryProfileDescr_Type())
cucsVnicRackServerDiscoveryProfileDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicRackServerDiscoveryProfileDescr.setStatus(_A)
_CucsVnicRackServerDiscoveryProfileIntId_Type=SnmpAdminString
_CucsVnicRackServerDiscoveryProfileIntId_Object=MibTableColumn
cucsVnicRackServerDiscoveryProfileIntId=_CucsVnicRackServerDiscoveryProfileIntId_Object((1,3,6,1,4,1,9,9,719,1,53,56,1,5),_CucsVnicRackServerDiscoveryProfileIntId_Type())
cucsVnicRackServerDiscoveryProfileIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicRackServerDiscoveryProfileIntId.setStatus(_A)
_CucsVnicRackServerDiscoveryProfileMaxPorts_Type=Gauge32
_CucsVnicRackServerDiscoveryProfileMaxPorts_Object=MibTableColumn
cucsVnicRackServerDiscoveryProfileMaxPorts=_CucsVnicRackServerDiscoveryProfileMaxPorts_Object((1,3,6,1,4,1,9,9,719,1,53,56,1,6),_CucsVnicRackServerDiscoveryProfileMaxPorts_Type())
cucsVnicRackServerDiscoveryProfileMaxPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicRackServerDiscoveryProfileMaxPorts.setStatus(_A)
_CucsVnicRackServerDiscoveryProfileName_Type=SnmpAdminString
_CucsVnicRackServerDiscoveryProfileName_Object=MibTableColumn
cucsVnicRackServerDiscoveryProfileName=_CucsVnicRackServerDiscoveryProfileName_Object((1,3,6,1,4,1,9,9,719,1,53,56,1,7),_CucsVnicRackServerDiscoveryProfileName_Type())
cucsVnicRackServerDiscoveryProfileName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicRackServerDiscoveryProfileName.setStatus(_A)
_CucsVnicRackServerDiscoveryProfilePolicyLevel_Type=Gauge32
_CucsVnicRackServerDiscoveryProfilePolicyLevel_Object=MibTableColumn
cucsVnicRackServerDiscoveryProfilePolicyLevel=_CucsVnicRackServerDiscoveryProfilePolicyLevel_Object((1,3,6,1,4,1,9,9,719,1,53,56,1,8),_CucsVnicRackServerDiscoveryProfilePolicyLevel_Type())
cucsVnicRackServerDiscoveryProfilePolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicRackServerDiscoveryProfilePolicyLevel.setStatus(_A)
_CucsVnicRackServerDiscoveryProfilePolicyOwner_Type=CucsPolicyPolicyOwner
_CucsVnicRackServerDiscoveryProfilePolicyOwner_Object=MibTableColumn
cucsVnicRackServerDiscoveryProfilePolicyOwner=_CucsVnicRackServerDiscoveryProfilePolicyOwner_Object((1,3,6,1,4,1,9,9,719,1,53,56,1,9),_CucsVnicRackServerDiscoveryProfilePolicyOwner_Type())
cucsVnicRackServerDiscoveryProfilePolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicRackServerDiscoveryProfilePolicyOwner.setStatus(_A)
_CucsVnicSanConnPolicyTable_Object=MibTable
cucsVnicSanConnPolicyTable=_CucsVnicSanConnPolicyTable_Object((1,3,6,1,4,1,9,9,719,1,53,57))
if mibBuilder.loadTexts:cucsVnicSanConnPolicyTable.setStatus(_A)
_CucsVnicSanConnPolicyEntry_Object=MibTableRow
cucsVnicSanConnPolicyEntry=_CucsVnicSanConnPolicyEntry_Object((1,3,6,1,4,1,9,9,719,1,53,57,1))
cucsVnicSanConnPolicyEntry.setIndexNames((0,_C,_A8))
if mibBuilder.loadTexts:cucsVnicSanConnPolicyEntry.setStatus(_A)
_CucsVnicSanConnPolicyInstanceId_Type=CucsManagedObjectId
_CucsVnicSanConnPolicyInstanceId_Object=MibTableColumn
cucsVnicSanConnPolicyInstanceId=_CucsVnicSanConnPolicyInstanceId_Object((1,3,6,1,4,1,9,9,719,1,53,57,1,1),_CucsVnicSanConnPolicyInstanceId_Type())
cucsVnicSanConnPolicyInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsVnicSanConnPolicyInstanceId.setStatus(_A)
_CucsVnicSanConnPolicyDn_Type=CucsManagedObjectDn
_CucsVnicSanConnPolicyDn_Object=MibTableColumn
cucsVnicSanConnPolicyDn=_CucsVnicSanConnPolicyDn_Object((1,3,6,1,4,1,9,9,719,1,53,57,1,2),_CucsVnicSanConnPolicyDn_Type())
cucsVnicSanConnPolicyDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicSanConnPolicyDn.setStatus(_A)
_CucsVnicSanConnPolicyRn_Type=SnmpAdminString
_CucsVnicSanConnPolicyRn_Object=MibTableColumn
cucsVnicSanConnPolicyRn=_CucsVnicSanConnPolicyRn_Object((1,3,6,1,4,1,9,9,719,1,53,57,1,3),_CucsVnicSanConnPolicyRn_Type())
cucsVnicSanConnPolicyRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicSanConnPolicyRn.setStatus(_A)
_CucsVnicSanConnPolicyDescr_Type=SnmpAdminString
_CucsVnicSanConnPolicyDescr_Object=MibTableColumn
cucsVnicSanConnPolicyDescr=_CucsVnicSanConnPolicyDescr_Object((1,3,6,1,4,1,9,9,719,1,53,57,1,4),_CucsVnicSanConnPolicyDescr_Type())
cucsVnicSanConnPolicyDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicSanConnPolicyDescr.setStatus(_A)
_CucsVnicSanConnPolicyFltAggr_Type=Unsigned64
_CucsVnicSanConnPolicyFltAggr_Object=MibTableColumn
cucsVnicSanConnPolicyFltAggr=_CucsVnicSanConnPolicyFltAggr_Object((1,3,6,1,4,1,9,9,719,1,53,57,1,5),_CucsVnicSanConnPolicyFltAggr_Type())
cucsVnicSanConnPolicyFltAggr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicSanConnPolicyFltAggr.setStatus(_A)
_CucsVnicSanConnPolicyIntId_Type=SnmpAdminString
_CucsVnicSanConnPolicyIntId_Object=MibTableColumn
cucsVnicSanConnPolicyIntId=_CucsVnicSanConnPolicyIntId_Object((1,3,6,1,4,1,9,9,719,1,53,57,1,6),_CucsVnicSanConnPolicyIntId_Type())
cucsVnicSanConnPolicyIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicSanConnPolicyIntId.setStatus(_A)
_CucsVnicSanConnPolicyName_Type=SnmpAdminString
_CucsVnicSanConnPolicyName_Object=MibTableColumn
cucsVnicSanConnPolicyName=_CucsVnicSanConnPolicyName_Object((1,3,6,1,4,1,9,9,719,1,53,57,1,7),_CucsVnicSanConnPolicyName_Type())
cucsVnicSanConnPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicSanConnPolicyName.setStatus(_A)
_CucsVnicSanConnPolicyPolicyLevel_Type=Gauge32
_CucsVnicSanConnPolicyPolicyLevel_Object=MibTableColumn
cucsVnicSanConnPolicyPolicyLevel=_CucsVnicSanConnPolicyPolicyLevel_Object((1,3,6,1,4,1,9,9,719,1,53,57,1,8),_CucsVnicSanConnPolicyPolicyLevel_Type())
cucsVnicSanConnPolicyPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicSanConnPolicyPolicyLevel.setStatus(_A)
_CucsVnicSanConnPolicyPolicyOwner_Type=CucsPolicyPolicyOwner
_CucsVnicSanConnPolicyPolicyOwner_Object=MibTableColumn
cucsVnicSanConnPolicyPolicyOwner=_CucsVnicSanConnPolicyPolicyOwner_Object((1,3,6,1,4,1,9,9,719,1,53,57,1,9),_CucsVnicSanConnPolicyPolicyOwner_Type())
cucsVnicSanConnPolicyPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicSanConnPolicyPolicyOwner.setStatus(_A)
_CucsVnicVhbaBehPolicyTable_Object=MibTable
cucsVnicVhbaBehPolicyTable=_CucsVnicVhbaBehPolicyTable_Object((1,3,6,1,4,1,9,9,719,1,53,58))
if mibBuilder.loadTexts:cucsVnicVhbaBehPolicyTable.setStatus(_A)
_CucsVnicVhbaBehPolicyEntry_Object=MibTableRow
cucsVnicVhbaBehPolicyEntry=_CucsVnicVhbaBehPolicyEntry_Object((1,3,6,1,4,1,9,9,719,1,53,58,1))
cucsVnicVhbaBehPolicyEntry.setIndexNames((0,_C,_A9))
if mibBuilder.loadTexts:cucsVnicVhbaBehPolicyEntry.setStatus(_A)
_CucsVnicVhbaBehPolicyInstanceId_Type=CucsManagedObjectId
_CucsVnicVhbaBehPolicyInstanceId_Object=MibTableColumn
cucsVnicVhbaBehPolicyInstanceId=_CucsVnicVhbaBehPolicyInstanceId_Object((1,3,6,1,4,1,9,9,719,1,53,58,1,1),_CucsVnicVhbaBehPolicyInstanceId_Type())
cucsVnicVhbaBehPolicyInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsVnicVhbaBehPolicyInstanceId.setStatus(_A)
_CucsVnicVhbaBehPolicyDn_Type=CucsManagedObjectDn
_CucsVnicVhbaBehPolicyDn_Object=MibTableColumn
cucsVnicVhbaBehPolicyDn=_CucsVnicVhbaBehPolicyDn_Object((1,3,6,1,4,1,9,9,719,1,53,58,1,2),_CucsVnicVhbaBehPolicyDn_Type())
cucsVnicVhbaBehPolicyDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicVhbaBehPolicyDn.setStatus(_A)
_CucsVnicVhbaBehPolicyRn_Type=SnmpAdminString
_CucsVnicVhbaBehPolicyRn_Object=MibTableColumn
cucsVnicVhbaBehPolicyRn=_CucsVnicVhbaBehPolicyRn_Object((1,3,6,1,4,1,9,9,719,1,53,58,1,3),_CucsVnicVhbaBehPolicyRn_Type())
cucsVnicVhbaBehPolicyRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicVhbaBehPolicyRn.setStatus(_A)
_CucsVnicVhbaBehPolicyAction_Type=CucsVnicDefaultAction
_CucsVnicVhbaBehPolicyAction_Object=MibTableColumn
cucsVnicVhbaBehPolicyAction=_CucsVnicVhbaBehPolicyAction_Object((1,3,6,1,4,1,9,9,719,1,53,58,1,4),_CucsVnicVhbaBehPolicyAction_Type())
cucsVnicVhbaBehPolicyAction.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicVhbaBehPolicyAction.setStatus(_A)
_CucsVnicVhbaBehPolicyDescr_Type=SnmpAdminString
_CucsVnicVhbaBehPolicyDescr_Object=MibTableColumn
cucsVnicVhbaBehPolicyDescr=_CucsVnicVhbaBehPolicyDescr_Object((1,3,6,1,4,1,9,9,719,1,53,58,1,5),_CucsVnicVhbaBehPolicyDescr_Type())
cucsVnicVhbaBehPolicyDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicVhbaBehPolicyDescr.setStatus(_A)
_CucsVnicVhbaBehPolicyIntId_Type=SnmpAdminString
_CucsVnicVhbaBehPolicyIntId_Object=MibTableColumn
cucsVnicVhbaBehPolicyIntId=_CucsVnicVhbaBehPolicyIntId_Object((1,3,6,1,4,1,9,9,719,1,53,58,1,6),_CucsVnicVhbaBehPolicyIntId_Type())
cucsVnicVhbaBehPolicyIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicVhbaBehPolicyIntId.setStatus(_A)
_CucsVnicVhbaBehPolicyName_Type=SnmpAdminString
_CucsVnicVhbaBehPolicyName_Object=MibTableColumn
cucsVnicVhbaBehPolicyName=_CucsVnicVhbaBehPolicyName_Object((1,3,6,1,4,1,9,9,719,1,53,58,1,7),_CucsVnicVhbaBehPolicyName_Type())
cucsVnicVhbaBehPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicVhbaBehPolicyName.setStatus(_A)
_CucsVnicVhbaBehPolicyNwTemplName_Type=SnmpAdminString
_CucsVnicVhbaBehPolicyNwTemplName_Object=MibTableColumn
cucsVnicVhbaBehPolicyNwTemplName=_CucsVnicVhbaBehPolicyNwTemplName_Object((1,3,6,1,4,1,9,9,719,1,53,58,1,8),_CucsVnicVhbaBehPolicyNwTemplName_Type())
cucsVnicVhbaBehPolicyNwTemplName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicVhbaBehPolicyNwTemplName.setStatus(_A)
_CucsVnicVhbaBehPolicyPolicyLevel_Type=Gauge32
_CucsVnicVhbaBehPolicyPolicyLevel_Object=MibTableColumn
cucsVnicVhbaBehPolicyPolicyLevel=_CucsVnicVhbaBehPolicyPolicyLevel_Object((1,3,6,1,4,1,9,9,719,1,53,58,1,9),_CucsVnicVhbaBehPolicyPolicyLevel_Type())
cucsVnicVhbaBehPolicyPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicVhbaBehPolicyPolicyLevel.setStatus(_A)
_CucsVnicVhbaBehPolicyPolicyOwner_Type=CucsPolicyPolicyOwner
_CucsVnicVhbaBehPolicyPolicyOwner_Object=MibTableColumn
cucsVnicVhbaBehPolicyPolicyOwner=_CucsVnicVhbaBehPolicyPolicyOwner_Object((1,3,6,1,4,1,9,9,719,1,53,58,1,10),_CucsVnicVhbaBehPolicyPolicyOwner_Type())
cucsVnicVhbaBehPolicyPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicVhbaBehPolicyPolicyOwner.setStatus(_A)
_CucsVnicVhbaBehPolicyType_Type=CucsVnicVhbaBehPolicyType
_CucsVnicVhbaBehPolicyType_Object=MibTableColumn
cucsVnicVhbaBehPolicyType=_CucsVnicVhbaBehPolicyType_Object((1,3,6,1,4,1,9,9,719,1,53,58,1,11),_CucsVnicVhbaBehPolicyType_Type())
cucsVnicVhbaBehPolicyType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicVhbaBehPolicyType.setStatus(_A)
_CucsVnicVnicBehPolicyTable_Object=MibTable
cucsVnicVnicBehPolicyTable=_CucsVnicVnicBehPolicyTable_Object((1,3,6,1,4,1,9,9,719,1,53,59))
if mibBuilder.loadTexts:cucsVnicVnicBehPolicyTable.setStatus(_A)
_CucsVnicVnicBehPolicyEntry_Object=MibTableRow
cucsVnicVnicBehPolicyEntry=_CucsVnicVnicBehPolicyEntry_Object((1,3,6,1,4,1,9,9,719,1,53,59,1))
cucsVnicVnicBehPolicyEntry.setIndexNames((0,_C,_AA))
if mibBuilder.loadTexts:cucsVnicVnicBehPolicyEntry.setStatus(_A)
_CucsVnicVnicBehPolicyInstanceId_Type=CucsManagedObjectId
_CucsVnicVnicBehPolicyInstanceId_Object=MibTableColumn
cucsVnicVnicBehPolicyInstanceId=_CucsVnicVnicBehPolicyInstanceId_Object((1,3,6,1,4,1,9,9,719,1,53,59,1,1),_CucsVnicVnicBehPolicyInstanceId_Type())
cucsVnicVnicBehPolicyInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsVnicVnicBehPolicyInstanceId.setStatus(_A)
_CucsVnicVnicBehPolicyDn_Type=CucsManagedObjectDn
_CucsVnicVnicBehPolicyDn_Object=MibTableColumn
cucsVnicVnicBehPolicyDn=_CucsVnicVnicBehPolicyDn_Object((1,3,6,1,4,1,9,9,719,1,53,59,1,2),_CucsVnicVnicBehPolicyDn_Type())
cucsVnicVnicBehPolicyDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicVnicBehPolicyDn.setStatus(_A)
_CucsVnicVnicBehPolicyRn_Type=SnmpAdminString
_CucsVnicVnicBehPolicyRn_Object=MibTableColumn
cucsVnicVnicBehPolicyRn=_CucsVnicVnicBehPolicyRn_Object((1,3,6,1,4,1,9,9,719,1,53,59,1,3),_CucsVnicVnicBehPolicyRn_Type())
cucsVnicVnicBehPolicyRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicVnicBehPolicyRn.setStatus(_A)
_CucsVnicVnicBehPolicyAction_Type=CucsVnicDefaultAction
_CucsVnicVnicBehPolicyAction_Object=MibTableColumn
cucsVnicVnicBehPolicyAction=_CucsVnicVnicBehPolicyAction_Object((1,3,6,1,4,1,9,9,719,1,53,59,1,4),_CucsVnicVnicBehPolicyAction_Type())
cucsVnicVnicBehPolicyAction.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicVnicBehPolicyAction.setStatus(_A)
_CucsVnicVnicBehPolicyDescr_Type=SnmpAdminString
_CucsVnicVnicBehPolicyDescr_Object=MibTableColumn
cucsVnicVnicBehPolicyDescr=_CucsVnicVnicBehPolicyDescr_Object((1,3,6,1,4,1,9,9,719,1,53,59,1,5),_CucsVnicVnicBehPolicyDescr_Type())
cucsVnicVnicBehPolicyDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicVnicBehPolicyDescr.setStatus(_A)
_CucsVnicVnicBehPolicyIntId_Type=SnmpAdminString
_CucsVnicVnicBehPolicyIntId_Object=MibTableColumn
cucsVnicVnicBehPolicyIntId=_CucsVnicVnicBehPolicyIntId_Object((1,3,6,1,4,1,9,9,719,1,53,59,1,6),_CucsVnicVnicBehPolicyIntId_Type())
cucsVnicVnicBehPolicyIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicVnicBehPolicyIntId.setStatus(_A)
_CucsVnicVnicBehPolicyName_Type=SnmpAdminString
_CucsVnicVnicBehPolicyName_Object=MibTableColumn
cucsVnicVnicBehPolicyName=_CucsVnicVnicBehPolicyName_Object((1,3,6,1,4,1,9,9,719,1,53,59,1,7),_CucsVnicVnicBehPolicyName_Type())
cucsVnicVnicBehPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicVnicBehPolicyName.setStatus(_A)
_CucsVnicVnicBehPolicyNwTemplName_Type=SnmpAdminString
_CucsVnicVnicBehPolicyNwTemplName_Object=MibTableColumn
cucsVnicVnicBehPolicyNwTemplName=_CucsVnicVnicBehPolicyNwTemplName_Object((1,3,6,1,4,1,9,9,719,1,53,59,1,8),_CucsVnicVnicBehPolicyNwTemplName_Type())
cucsVnicVnicBehPolicyNwTemplName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicVnicBehPolicyNwTemplName.setStatus(_A)
_CucsVnicVnicBehPolicyPolicyLevel_Type=Gauge32
_CucsVnicVnicBehPolicyPolicyLevel_Object=MibTableColumn
cucsVnicVnicBehPolicyPolicyLevel=_CucsVnicVnicBehPolicyPolicyLevel_Object((1,3,6,1,4,1,9,9,719,1,53,59,1,9),_CucsVnicVnicBehPolicyPolicyLevel_Type())
cucsVnicVnicBehPolicyPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicVnicBehPolicyPolicyLevel.setStatus(_A)
_CucsVnicVnicBehPolicyPolicyOwner_Type=CucsPolicyPolicyOwner
_CucsVnicVnicBehPolicyPolicyOwner_Object=MibTableColumn
cucsVnicVnicBehPolicyPolicyOwner=_CucsVnicVnicBehPolicyPolicyOwner_Object((1,3,6,1,4,1,9,9,719,1,53,59,1,10),_CucsVnicVnicBehPolicyPolicyOwner_Type())
cucsVnicVnicBehPolicyPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicVnicBehPolicyPolicyOwner.setStatus(_A)
_CucsVnicVnicBehPolicyType_Type=CucsVnicVnicBehPolicyType
_CucsVnicVnicBehPolicyType_Object=MibTableColumn
cucsVnicVnicBehPolicyType=_CucsVnicVnicBehPolicyType_Object((1,3,6,1,4,1,9,9,719,1,53,59,1,11),_CucsVnicVnicBehPolicyType_Type())
cucsVnicVnicBehPolicyType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicVnicBehPolicyType.setStatus(_A)
_CucsVnicIpV4HistoryTable_Object=MibTable
cucsVnicIpV4HistoryTable=_CucsVnicIpV4HistoryTable_Object((1,3,6,1,4,1,9,9,719,1,53,60))
if mibBuilder.loadTexts:cucsVnicIpV4HistoryTable.setStatus(_A)
_CucsVnicIpV4HistoryEntry_Object=MibTableRow
cucsVnicIpV4HistoryEntry=_CucsVnicIpV4HistoryEntry_Object((1,3,6,1,4,1,9,9,719,1,53,60,1))
cucsVnicIpV4HistoryEntry.setIndexNames((0,_C,_AB))
if mibBuilder.loadTexts:cucsVnicIpV4HistoryEntry.setStatus(_A)
_CucsVnicIpV4HistoryInstanceId_Type=CucsManagedObjectId
_CucsVnicIpV4HistoryInstanceId_Object=MibTableColumn
cucsVnicIpV4HistoryInstanceId=_CucsVnicIpV4HistoryInstanceId_Object((1,3,6,1,4,1,9,9,719,1,53,60,1,1),_CucsVnicIpV4HistoryInstanceId_Type())
cucsVnicIpV4HistoryInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsVnicIpV4HistoryInstanceId.setStatus(_A)
_CucsVnicIpV4HistoryDn_Type=CucsManagedObjectDn
_CucsVnicIpV4HistoryDn_Object=MibTableColumn
cucsVnicIpV4HistoryDn=_CucsVnicIpV4HistoryDn_Object((1,3,6,1,4,1,9,9,719,1,53,60,1,2),_CucsVnicIpV4HistoryDn_Type())
cucsVnicIpV4HistoryDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIpV4HistoryDn.setStatus(_A)
_CucsVnicIpV4HistoryRn_Type=SnmpAdminString
_CucsVnicIpV4HistoryRn_Object=MibTableColumn
cucsVnicIpV4HistoryRn=_CucsVnicIpV4HistoryRn_Object((1,3,6,1,4,1,9,9,719,1,53,60,1,3),_CucsVnicIpV4HistoryRn_Type())
cucsVnicIpV4HistoryRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIpV4HistoryRn.setStatus(_A)
_CucsVnicIpV4HistoryOldIpV4Addr_Type=InetAddressIPv4
_CucsVnicIpV4HistoryOldIpV4Addr_Object=MibTableColumn
cucsVnicIpV4HistoryOldIpV4Addr=_CucsVnicIpV4HistoryOldIpV4Addr_Object((1,3,6,1,4,1,9,9,719,1,53,60,1,4),_CucsVnicIpV4HistoryOldIpV4Addr_Type())
cucsVnicIpV4HistoryOldIpV4Addr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIpV4HistoryOldIpV4Addr.setStatus(_A)
_CucsVnicIqnHistoryTable_Object=MibTable
cucsVnicIqnHistoryTable=_CucsVnicIqnHistoryTable_Object((1,3,6,1,4,1,9,9,719,1,53,61))
if mibBuilder.loadTexts:cucsVnicIqnHistoryTable.setStatus(_A)
_CucsVnicIqnHistoryEntry_Object=MibTableRow
cucsVnicIqnHistoryEntry=_CucsVnicIqnHistoryEntry_Object((1,3,6,1,4,1,9,9,719,1,53,61,1))
cucsVnicIqnHistoryEntry.setIndexNames((0,_C,_AC))
if mibBuilder.loadTexts:cucsVnicIqnHistoryEntry.setStatus(_A)
_CucsVnicIqnHistoryInstanceId_Type=CucsManagedObjectId
_CucsVnicIqnHistoryInstanceId_Object=MibTableColumn
cucsVnicIqnHistoryInstanceId=_CucsVnicIqnHistoryInstanceId_Object((1,3,6,1,4,1,9,9,719,1,53,61,1,1),_CucsVnicIqnHistoryInstanceId_Type())
cucsVnicIqnHistoryInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsVnicIqnHistoryInstanceId.setStatus(_A)
_CucsVnicIqnHistoryDn_Type=CucsManagedObjectDn
_CucsVnicIqnHistoryDn_Object=MibTableColumn
cucsVnicIqnHistoryDn=_CucsVnicIqnHistoryDn_Object((1,3,6,1,4,1,9,9,719,1,53,61,1,2),_CucsVnicIqnHistoryDn_Type())
cucsVnicIqnHistoryDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIqnHistoryDn.setStatus(_A)
_CucsVnicIqnHistoryRn_Type=SnmpAdminString
_CucsVnicIqnHistoryRn_Object=MibTableColumn
cucsVnicIqnHistoryRn=_CucsVnicIqnHistoryRn_Object((1,3,6,1,4,1,9,9,719,1,53,61,1,3),_CucsVnicIqnHistoryRn_Type())
cucsVnicIqnHistoryRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIqnHistoryRn.setStatus(_A)
_CucsVnicIqnHistoryOldInitiatorName_Type=SnmpAdminString
_CucsVnicIqnHistoryOldInitiatorName_Object=MibTableColumn
cucsVnicIqnHistoryOldInitiatorName=_CucsVnicIqnHistoryOldInitiatorName_Object((1,3,6,1,4,1,9,9,719,1,53,61,1,4),_CucsVnicIqnHistoryOldInitiatorName_Type())
cucsVnicIqnHistoryOldInitiatorName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIqnHistoryOldInitiatorName.setStatus(_A)
_CucsVnicMacHistoryTable_Object=MibTable
cucsVnicMacHistoryTable=_CucsVnicMacHistoryTable_Object((1,3,6,1,4,1,9,9,719,1,53,62))
if mibBuilder.loadTexts:cucsVnicMacHistoryTable.setStatus(_A)
_CucsVnicMacHistoryEntry_Object=MibTableRow
cucsVnicMacHistoryEntry=_CucsVnicMacHistoryEntry_Object((1,3,6,1,4,1,9,9,719,1,53,62,1))
cucsVnicMacHistoryEntry.setIndexNames((0,_C,_AD))
if mibBuilder.loadTexts:cucsVnicMacHistoryEntry.setStatus(_A)
_CucsVnicMacHistoryInstanceId_Type=CucsManagedObjectId
_CucsVnicMacHistoryInstanceId_Object=MibTableColumn
cucsVnicMacHistoryInstanceId=_CucsVnicMacHistoryInstanceId_Object((1,3,6,1,4,1,9,9,719,1,53,62,1,1),_CucsVnicMacHistoryInstanceId_Type())
cucsVnicMacHistoryInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsVnicMacHistoryInstanceId.setStatus(_A)
_CucsVnicMacHistoryDn_Type=CucsManagedObjectDn
_CucsVnicMacHistoryDn_Object=MibTableColumn
cucsVnicMacHistoryDn=_CucsVnicMacHistoryDn_Object((1,3,6,1,4,1,9,9,719,1,53,62,1,2),_CucsVnicMacHistoryDn_Type())
cucsVnicMacHistoryDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicMacHistoryDn.setStatus(_A)
_CucsVnicMacHistoryRn_Type=SnmpAdminString
_CucsVnicMacHistoryRn_Object=MibTableColumn
cucsVnicMacHistoryRn=_CucsVnicMacHistoryRn_Object((1,3,6,1,4,1,9,9,719,1,53,62,1,3),_CucsVnicMacHistoryRn_Type())
cucsVnicMacHistoryRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicMacHistoryRn.setStatus(_A)
_CucsVnicMacHistoryOldaddr_Type=MacAddress
_CucsVnicMacHistoryOldaddr_Object=MibTableColumn
cucsVnicMacHistoryOldaddr=_CucsVnicMacHistoryOldaddr_Object((1,3,6,1,4,1,9,9,719,1,53,62,1,4),_CucsVnicMacHistoryOldaddr_Type())
cucsVnicMacHistoryOldaddr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicMacHistoryOldaddr.setStatus(_A)
_CucsVnicWwnnHistoryTable_Object=MibTable
cucsVnicWwnnHistoryTable=_CucsVnicWwnnHistoryTable_Object((1,3,6,1,4,1,9,9,719,1,53,63))
if mibBuilder.loadTexts:cucsVnicWwnnHistoryTable.setStatus(_A)
_CucsVnicWwnnHistoryEntry_Object=MibTableRow
cucsVnicWwnnHistoryEntry=_CucsVnicWwnnHistoryEntry_Object((1,3,6,1,4,1,9,9,719,1,53,63,1))
cucsVnicWwnnHistoryEntry.setIndexNames((0,_C,_AE))
if mibBuilder.loadTexts:cucsVnicWwnnHistoryEntry.setStatus(_A)
_CucsVnicWwnnHistoryInstanceId_Type=CucsManagedObjectId
_CucsVnicWwnnHistoryInstanceId_Object=MibTableColumn
cucsVnicWwnnHistoryInstanceId=_CucsVnicWwnnHistoryInstanceId_Object((1,3,6,1,4,1,9,9,719,1,53,63,1,1),_CucsVnicWwnnHistoryInstanceId_Type())
cucsVnicWwnnHistoryInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsVnicWwnnHistoryInstanceId.setStatus(_A)
_CucsVnicWwnnHistoryDn_Type=CucsManagedObjectDn
_CucsVnicWwnnHistoryDn_Object=MibTableColumn
cucsVnicWwnnHistoryDn=_CucsVnicWwnnHistoryDn_Object((1,3,6,1,4,1,9,9,719,1,53,63,1,2),_CucsVnicWwnnHistoryDn_Type())
cucsVnicWwnnHistoryDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicWwnnHistoryDn.setStatus(_A)
_CucsVnicWwnnHistoryRn_Type=SnmpAdminString
_CucsVnicWwnnHistoryRn_Object=MibTableColumn
cucsVnicWwnnHistoryRn=_CucsVnicWwnnHistoryRn_Object((1,3,6,1,4,1,9,9,719,1,53,63,1,3),_CucsVnicWwnnHistoryRn_Type())
cucsVnicWwnnHistoryRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicWwnnHistoryRn.setStatus(_A)
_CucsVnicWwnnHistoryOldwwnn_Type=Unsigned64
_CucsVnicWwnnHistoryOldwwnn_Object=MibTableColumn
cucsVnicWwnnHistoryOldwwnn=_CucsVnicWwnnHistoryOldwwnn_Object((1,3,6,1,4,1,9,9,719,1,53,63,1,4),_CucsVnicWwnnHistoryOldwwnn_Type())
cucsVnicWwnnHistoryOldwwnn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicWwnnHistoryOldwwnn.setStatus(_A)
_CucsVnicWwpnHistoryTable_Object=MibTable
cucsVnicWwpnHistoryTable=_CucsVnicWwpnHistoryTable_Object((1,3,6,1,4,1,9,9,719,1,53,64))
if mibBuilder.loadTexts:cucsVnicWwpnHistoryTable.setStatus(_A)
_CucsVnicWwpnHistoryEntry_Object=MibTableRow
cucsVnicWwpnHistoryEntry=_CucsVnicWwpnHistoryEntry_Object((1,3,6,1,4,1,9,9,719,1,53,64,1))
cucsVnicWwpnHistoryEntry.setIndexNames((0,_C,_AF))
if mibBuilder.loadTexts:cucsVnicWwpnHistoryEntry.setStatus(_A)
_CucsVnicWwpnHistoryInstanceId_Type=CucsManagedObjectId
_CucsVnicWwpnHistoryInstanceId_Object=MibTableColumn
cucsVnicWwpnHistoryInstanceId=_CucsVnicWwpnHistoryInstanceId_Object((1,3,6,1,4,1,9,9,719,1,53,64,1,1),_CucsVnicWwpnHistoryInstanceId_Type())
cucsVnicWwpnHistoryInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsVnicWwpnHistoryInstanceId.setStatus(_A)
_CucsVnicWwpnHistoryDn_Type=CucsManagedObjectDn
_CucsVnicWwpnHistoryDn_Object=MibTableColumn
cucsVnicWwpnHistoryDn=_CucsVnicWwpnHistoryDn_Object((1,3,6,1,4,1,9,9,719,1,53,64,1,2),_CucsVnicWwpnHistoryDn_Type())
cucsVnicWwpnHistoryDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicWwpnHistoryDn.setStatus(_A)
_CucsVnicWwpnHistoryRn_Type=SnmpAdminString
_CucsVnicWwpnHistoryRn_Object=MibTableColumn
cucsVnicWwpnHistoryRn=_CucsVnicWwpnHistoryRn_Object((1,3,6,1,4,1,9,9,719,1,53,64,1,3),_CucsVnicWwpnHistoryRn_Type())
cucsVnicWwpnHistoryRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicWwpnHistoryRn.setStatus(_A)
_CucsVnicWwpnHistoryOldaddr_Type=Unsigned64
_CucsVnicWwpnHistoryOldaddr_Object=MibTableColumn
cucsVnicWwpnHistoryOldaddr=_CucsVnicWwpnHistoryOldaddr_Object((1,3,6,1,4,1,9,9,719,1,53,64,1,4),_CucsVnicWwpnHistoryOldaddr_Type())
cucsVnicWwpnHistoryOldaddr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicWwpnHistoryOldaddr.setStatus(_A)
_CucsVnicIpV4MgmtPooledAddrTable_Object=MibTable
cucsVnicIpV4MgmtPooledAddrTable=_CucsVnicIpV4MgmtPooledAddrTable_Object((1,3,6,1,4,1,9,9,719,1,53,65))
if mibBuilder.loadTexts:cucsVnicIpV4MgmtPooledAddrTable.setStatus(_A)
_CucsVnicIpV4MgmtPooledAddrEntry_Object=MibTableRow
cucsVnicIpV4MgmtPooledAddrEntry=_CucsVnicIpV4MgmtPooledAddrEntry_Object((1,3,6,1,4,1,9,9,719,1,53,65,1))
cucsVnicIpV4MgmtPooledAddrEntry.setIndexNames((0,_C,_AG))
if mibBuilder.loadTexts:cucsVnicIpV4MgmtPooledAddrEntry.setStatus(_A)
_CucsVnicIpV4MgmtPooledAddrInstanceId_Type=CucsManagedObjectId
_CucsVnicIpV4MgmtPooledAddrInstanceId_Object=MibTableColumn
cucsVnicIpV4MgmtPooledAddrInstanceId=_CucsVnicIpV4MgmtPooledAddrInstanceId_Object((1,3,6,1,4,1,9,9,719,1,53,65,1,1),_CucsVnicIpV4MgmtPooledAddrInstanceId_Type())
cucsVnicIpV4MgmtPooledAddrInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsVnicIpV4MgmtPooledAddrInstanceId.setStatus(_A)
_CucsVnicIpV4MgmtPooledAddrDn_Type=CucsManagedObjectDn
_CucsVnicIpV4MgmtPooledAddrDn_Object=MibTableColumn
cucsVnicIpV4MgmtPooledAddrDn=_CucsVnicIpV4MgmtPooledAddrDn_Object((1,3,6,1,4,1,9,9,719,1,53,65,1,2),_CucsVnicIpV4MgmtPooledAddrDn_Type())
cucsVnicIpV4MgmtPooledAddrDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIpV4MgmtPooledAddrDn.setStatus(_A)
_CucsVnicIpV4MgmtPooledAddrRn_Type=SnmpAdminString
_CucsVnicIpV4MgmtPooledAddrRn_Object=MibTableColumn
cucsVnicIpV4MgmtPooledAddrRn=_CucsVnicIpV4MgmtPooledAddrRn_Object((1,3,6,1,4,1,9,9,719,1,53,65,1,3),_CucsVnicIpV4MgmtPooledAddrRn_Type())
cucsVnicIpV4MgmtPooledAddrRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIpV4MgmtPooledAddrRn.setStatus(_A)
_CucsVnicIpV4MgmtPooledAddrAddr_Type=InetAddressIPv4
_CucsVnicIpV4MgmtPooledAddrAddr_Object=MibTableColumn
cucsVnicIpV4MgmtPooledAddrAddr=_CucsVnicIpV4MgmtPooledAddrAddr_Object((1,3,6,1,4,1,9,9,719,1,53,65,1,4),_CucsVnicIpV4MgmtPooledAddrAddr_Type())
cucsVnicIpV4MgmtPooledAddrAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIpV4MgmtPooledAddrAddr.setStatus(_A)
_CucsVnicIpV4MgmtPooledAddrDefGw_Type=InetAddressIPv4
_CucsVnicIpV4MgmtPooledAddrDefGw_Object=MibTableColumn
cucsVnicIpV4MgmtPooledAddrDefGw=_CucsVnicIpV4MgmtPooledAddrDefGw_Object((1,3,6,1,4,1,9,9,719,1,53,65,1,5),_CucsVnicIpV4MgmtPooledAddrDefGw_Type())
cucsVnicIpV4MgmtPooledAddrDefGw.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIpV4MgmtPooledAddrDefGw.setStatus(_A)
_CucsVnicIpV4MgmtPooledAddrName_Type=SnmpAdminString
_CucsVnicIpV4MgmtPooledAddrName_Object=MibTableColumn
cucsVnicIpV4MgmtPooledAddrName=_CucsVnicIpV4MgmtPooledAddrName_Object((1,3,6,1,4,1,9,9,719,1,53,65,1,6),_CucsVnicIpV4MgmtPooledAddrName_Type())
cucsVnicIpV4MgmtPooledAddrName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIpV4MgmtPooledAddrName.setStatus(_A)
_CucsVnicIpV4MgmtPooledAddrOperName_Type=SnmpAdminString
_CucsVnicIpV4MgmtPooledAddrOperName_Object=MibTableColumn
cucsVnicIpV4MgmtPooledAddrOperName=_CucsVnicIpV4MgmtPooledAddrOperName_Object((1,3,6,1,4,1,9,9,719,1,53,65,1,7),_CucsVnicIpV4MgmtPooledAddrOperName_Type())
cucsVnicIpV4MgmtPooledAddrOperName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIpV4MgmtPooledAddrOperName.setStatus(_A)
_CucsVnicIpV4MgmtPooledAddrSubnet_Type=InetAddressIPv4
_CucsVnicIpV4MgmtPooledAddrSubnet_Object=MibTableColumn
cucsVnicIpV4MgmtPooledAddrSubnet=_CucsVnicIpV4MgmtPooledAddrSubnet_Object((1,3,6,1,4,1,9,9,719,1,53,65,1,8),_CucsVnicIpV4MgmtPooledAddrSubnet_Type())
cucsVnicIpV4MgmtPooledAddrSubnet.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIpV4MgmtPooledAddrSubnet.setStatus(_A)
_CucsVnicIpV4MgmtPooledAddrPrimDns_Type=InetAddressIPv4
_CucsVnicIpV4MgmtPooledAddrPrimDns_Object=MibTableColumn
cucsVnicIpV4MgmtPooledAddrPrimDns=_CucsVnicIpV4MgmtPooledAddrPrimDns_Object((1,3,6,1,4,1,9,9,719,1,53,65,1,9),_CucsVnicIpV4MgmtPooledAddrPrimDns_Type())
cucsVnicIpV4MgmtPooledAddrPrimDns.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIpV4MgmtPooledAddrPrimDns.setStatus(_A)
_CucsVnicIpV4MgmtPooledAddrSecDns_Type=InetAddressIPv4
_CucsVnicIpV4MgmtPooledAddrSecDns_Object=MibTableColumn
cucsVnicIpV4MgmtPooledAddrSecDns=_CucsVnicIpV4MgmtPooledAddrSecDns_Object((1,3,6,1,4,1,9,9,719,1,53,65,1,10),_CucsVnicIpV4MgmtPooledAddrSecDns_Type())
cucsVnicIpV4MgmtPooledAddrSecDns.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIpV4MgmtPooledAddrSecDns.setStatus(_A)
_CucsVnicIpV6MgmtPooledAddrTable_Object=MibTable
cucsVnicIpV6MgmtPooledAddrTable=_CucsVnicIpV6MgmtPooledAddrTable_Object((1,3,6,1,4,1,9,9,719,1,53,66))
if mibBuilder.loadTexts:cucsVnicIpV6MgmtPooledAddrTable.setStatus(_A)
_CucsVnicIpV6MgmtPooledAddrEntry_Object=MibTableRow
cucsVnicIpV6MgmtPooledAddrEntry=_CucsVnicIpV6MgmtPooledAddrEntry_Object((1,3,6,1,4,1,9,9,719,1,53,66,1))
cucsVnicIpV6MgmtPooledAddrEntry.setIndexNames((0,_C,_AH))
if mibBuilder.loadTexts:cucsVnicIpV6MgmtPooledAddrEntry.setStatus(_A)
_CucsVnicIpV6MgmtPooledAddrInstanceId_Type=CucsManagedObjectId
_CucsVnicIpV6MgmtPooledAddrInstanceId_Object=MibTableColumn
cucsVnicIpV6MgmtPooledAddrInstanceId=_CucsVnicIpV6MgmtPooledAddrInstanceId_Object((1,3,6,1,4,1,9,9,719,1,53,66,1,1),_CucsVnicIpV6MgmtPooledAddrInstanceId_Type())
cucsVnicIpV6MgmtPooledAddrInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsVnicIpV6MgmtPooledAddrInstanceId.setStatus(_A)
_CucsVnicIpV6MgmtPooledAddrDn_Type=CucsManagedObjectDn
_CucsVnicIpV6MgmtPooledAddrDn_Object=MibTableColumn
cucsVnicIpV6MgmtPooledAddrDn=_CucsVnicIpV6MgmtPooledAddrDn_Object((1,3,6,1,4,1,9,9,719,1,53,66,1,2),_CucsVnicIpV6MgmtPooledAddrDn_Type())
cucsVnicIpV6MgmtPooledAddrDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIpV6MgmtPooledAddrDn.setStatus(_A)
_CucsVnicIpV6MgmtPooledAddrRn_Type=SnmpAdminString
_CucsVnicIpV6MgmtPooledAddrRn_Object=MibTableColumn
cucsVnicIpV6MgmtPooledAddrRn=_CucsVnicIpV6MgmtPooledAddrRn_Object((1,3,6,1,4,1,9,9,719,1,53,66,1,3),_CucsVnicIpV6MgmtPooledAddrRn_Type())
cucsVnicIpV6MgmtPooledAddrRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIpV6MgmtPooledAddrRn.setStatus(_A)
_CucsVnicIpV6MgmtPooledAddrAddr_Type=InetAddressIPv6
_CucsVnicIpV6MgmtPooledAddrAddr_Object=MibTableColumn
cucsVnicIpV6MgmtPooledAddrAddr=_CucsVnicIpV6MgmtPooledAddrAddr_Object((1,3,6,1,4,1,9,9,719,1,53,66,1,4),_CucsVnicIpV6MgmtPooledAddrAddr_Type())
cucsVnicIpV6MgmtPooledAddrAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIpV6MgmtPooledAddrAddr.setStatus(_A)
_CucsVnicIpV6MgmtPooledAddrDefGw_Type=InetAddressIPv6
_CucsVnicIpV6MgmtPooledAddrDefGw_Object=MibTableColumn
cucsVnicIpV6MgmtPooledAddrDefGw=_CucsVnicIpV6MgmtPooledAddrDefGw_Object((1,3,6,1,4,1,9,9,719,1,53,66,1,5),_CucsVnicIpV6MgmtPooledAddrDefGw_Type())
cucsVnicIpV6MgmtPooledAddrDefGw.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIpV6MgmtPooledAddrDefGw.setStatus(_A)
_CucsVnicIpV6MgmtPooledAddrName_Type=SnmpAdminString
_CucsVnicIpV6MgmtPooledAddrName_Object=MibTableColumn
cucsVnicIpV6MgmtPooledAddrName=_CucsVnicIpV6MgmtPooledAddrName_Object((1,3,6,1,4,1,9,9,719,1,53,66,1,6),_CucsVnicIpV6MgmtPooledAddrName_Type())
cucsVnicIpV6MgmtPooledAddrName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIpV6MgmtPooledAddrName.setStatus(_A)
_CucsVnicIpV6MgmtPooledAddrOperName_Type=SnmpAdminString
_CucsVnicIpV6MgmtPooledAddrOperName_Object=MibTableColumn
cucsVnicIpV6MgmtPooledAddrOperName=_CucsVnicIpV6MgmtPooledAddrOperName_Object((1,3,6,1,4,1,9,9,719,1,53,66,1,7),_CucsVnicIpV6MgmtPooledAddrOperName_Type())
cucsVnicIpV6MgmtPooledAddrOperName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIpV6MgmtPooledAddrOperName.setStatus(_A)
_CucsVnicIpV6MgmtPooledAddrPrefix_Type=Gauge32
_CucsVnicIpV6MgmtPooledAddrPrefix_Object=MibTableColumn
cucsVnicIpV6MgmtPooledAddrPrefix=_CucsVnicIpV6MgmtPooledAddrPrefix_Object((1,3,6,1,4,1,9,9,719,1,53,66,1,8),_CucsVnicIpV6MgmtPooledAddrPrefix_Type())
cucsVnicIpV6MgmtPooledAddrPrefix.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIpV6MgmtPooledAddrPrefix.setStatus(_A)
_CucsVnicIpV6MgmtPooledAddrPrimDns_Type=InetAddressIPv6
_CucsVnicIpV6MgmtPooledAddrPrimDns_Object=MibTableColumn
cucsVnicIpV6MgmtPooledAddrPrimDns=_CucsVnicIpV6MgmtPooledAddrPrimDns_Object((1,3,6,1,4,1,9,9,719,1,53,66,1,9),_CucsVnicIpV6MgmtPooledAddrPrimDns_Type())
cucsVnicIpV6MgmtPooledAddrPrimDns.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIpV6MgmtPooledAddrPrimDns.setStatus(_A)
_CucsVnicIpV6MgmtPooledAddrSecDns_Type=InetAddressIPv6
_CucsVnicIpV6MgmtPooledAddrSecDns_Object=MibTableColumn
cucsVnicIpV6MgmtPooledAddrSecDns=_CucsVnicIpV6MgmtPooledAddrSecDns_Object((1,3,6,1,4,1,9,9,719,1,53,66,1,10),_CucsVnicIpV6MgmtPooledAddrSecDns_Type())
cucsVnicIpV6MgmtPooledAddrSecDns.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIpV6MgmtPooledAddrSecDns.setStatus(_A)
_CucsVnicIpV6StaticAddrTable_Object=MibTable
cucsVnicIpV6StaticAddrTable=_CucsVnicIpV6StaticAddrTable_Object((1,3,6,1,4,1,9,9,719,1,53,67))
if mibBuilder.loadTexts:cucsVnicIpV6StaticAddrTable.setStatus(_A)
_CucsVnicIpV6StaticAddrEntry_Object=MibTableRow
cucsVnicIpV6StaticAddrEntry=_CucsVnicIpV6StaticAddrEntry_Object((1,3,6,1,4,1,9,9,719,1,53,67,1))
cucsVnicIpV6StaticAddrEntry.setIndexNames((0,_C,_AI))
if mibBuilder.loadTexts:cucsVnicIpV6StaticAddrEntry.setStatus(_A)
_CucsVnicIpV6StaticAddrInstanceId_Type=CucsManagedObjectId
_CucsVnicIpV6StaticAddrInstanceId_Object=MibTableColumn
cucsVnicIpV6StaticAddrInstanceId=_CucsVnicIpV6StaticAddrInstanceId_Object((1,3,6,1,4,1,9,9,719,1,53,67,1,1),_CucsVnicIpV6StaticAddrInstanceId_Type())
cucsVnicIpV6StaticAddrInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsVnicIpV6StaticAddrInstanceId.setStatus(_A)
_CucsVnicIpV6StaticAddrDn_Type=CucsManagedObjectDn
_CucsVnicIpV6StaticAddrDn_Object=MibTableColumn
cucsVnicIpV6StaticAddrDn=_CucsVnicIpV6StaticAddrDn_Object((1,3,6,1,4,1,9,9,719,1,53,67,1,2),_CucsVnicIpV6StaticAddrDn_Type())
cucsVnicIpV6StaticAddrDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIpV6StaticAddrDn.setStatus(_A)
_CucsVnicIpV6StaticAddrRn_Type=SnmpAdminString
_CucsVnicIpV6StaticAddrRn_Object=MibTableColumn
cucsVnicIpV6StaticAddrRn=_CucsVnicIpV6StaticAddrRn_Object((1,3,6,1,4,1,9,9,719,1,53,67,1,3),_CucsVnicIpV6StaticAddrRn_Type())
cucsVnicIpV6StaticAddrRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIpV6StaticAddrRn.setStatus(_A)
_CucsVnicIpV6StaticAddrAddr_Type=InetAddressIPv6
_CucsVnicIpV6StaticAddrAddr_Object=MibTableColumn
cucsVnicIpV6StaticAddrAddr=_CucsVnicIpV6StaticAddrAddr_Object((1,3,6,1,4,1,9,9,719,1,53,67,1,4),_CucsVnicIpV6StaticAddrAddr_Type())
cucsVnicIpV6StaticAddrAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIpV6StaticAddrAddr.setStatus(_A)
_CucsVnicIpV6StaticAddrDefGw_Type=InetAddressIPv6
_CucsVnicIpV6StaticAddrDefGw_Object=MibTableColumn
cucsVnicIpV6StaticAddrDefGw=_CucsVnicIpV6StaticAddrDefGw_Object((1,3,6,1,4,1,9,9,719,1,53,67,1,5),_CucsVnicIpV6StaticAddrDefGw_Type())
cucsVnicIpV6StaticAddrDefGw.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIpV6StaticAddrDefGw.setStatus(_A)
_CucsVnicIpV6StaticAddrPrefix_Type=Gauge32
_CucsVnicIpV6StaticAddrPrefix_Object=MibTableColumn
cucsVnicIpV6StaticAddrPrefix=_CucsVnicIpV6StaticAddrPrefix_Object((1,3,6,1,4,1,9,9,719,1,53,67,1,6),_CucsVnicIpV6StaticAddrPrefix_Type())
cucsVnicIpV6StaticAddrPrefix.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIpV6StaticAddrPrefix.setStatus(_A)
_CucsVnicIpV6StaticAddrPrimDns_Type=InetAddressIPv6
_CucsVnicIpV6StaticAddrPrimDns_Object=MibTableColumn
cucsVnicIpV6StaticAddrPrimDns=_CucsVnicIpV6StaticAddrPrimDns_Object((1,3,6,1,4,1,9,9,719,1,53,67,1,7),_CucsVnicIpV6StaticAddrPrimDns_Type())
cucsVnicIpV6StaticAddrPrimDns.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIpV6StaticAddrPrimDns.setStatus(_A)
_CucsVnicIpV6StaticAddrSecDns_Type=InetAddressIPv6
_CucsVnicIpV6StaticAddrSecDns_Object=MibTableColumn
cucsVnicIpV6StaticAddrSecDns=_CucsVnicIpV6StaticAddrSecDns_Object((1,3,6,1,4,1,9,9,719,1,53,67,1,8),_CucsVnicIpV6StaticAddrSecDns_Type())
cucsVnicIpV6StaticAddrSecDns.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIpV6StaticAddrSecDns.setStatus(_A)
_CucsVnicProfileRefTable_Object=MibTable
cucsVnicProfileRefTable=_CucsVnicProfileRefTable_Object((1,3,6,1,4,1,9,9,719,1,53,68))
if mibBuilder.loadTexts:cucsVnicProfileRefTable.setStatus(_A)
_CucsVnicProfileRefEntry_Object=MibTableRow
cucsVnicProfileRefEntry=_CucsVnicProfileRefEntry_Object((1,3,6,1,4,1,9,9,719,1,53,68,1))
cucsVnicProfileRefEntry.setIndexNames((0,_C,_AJ))
if mibBuilder.loadTexts:cucsVnicProfileRefEntry.setStatus(_A)
_CucsVnicProfileRefInstanceId_Type=CucsManagedObjectId
_CucsVnicProfileRefInstanceId_Object=MibTableColumn
cucsVnicProfileRefInstanceId=_CucsVnicProfileRefInstanceId_Object((1,3,6,1,4,1,9,9,719,1,53,68,1,1),_CucsVnicProfileRefInstanceId_Type())
cucsVnicProfileRefInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsVnicProfileRefInstanceId.setStatus(_A)
_CucsVnicProfileRefDn_Type=CucsManagedObjectDn
_CucsVnicProfileRefDn_Object=MibTableColumn
cucsVnicProfileRefDn=_CucsVnicProfileRefDn_Object((1,3,6,1,4,1,9,9,719,1,53,68,1,2),_CucsVnicProfileRefDn_Type())
cucsVnicProfileRefDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicProfileRefDn.setStatus(_A)
_CucsVnicProfileRefRn_Type=SnmpAdminString
_CucsVnicProfileRefRn_Object=MibTableColumn
cucsVnicProfileRefRn=_CucsVnicProfileRefRn_Object((1,3,6,1,4,1,9,9,719,1,53,68,1,3),_CucsVnicProfileRefRn_Type())
cucsVnicProfileRefRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicProfileRefRn.setStatus(_A)
_CucsVnicProfileRefName_Type=SnmpAdminString
_CucsVnicProfileRefName_Object=MibTableColumn
cucsVnicProfileRefName=_CucsVnicProfileRefName_Object((1,3,6,1,4,1,9,9,719,1,53,68,1,4),_CucsVnicProfileRefName_Type())
cucsVnicProfileRefName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicProfileRefName.setStatus(_A)
_CucsVnicProfileRefSourceDn_Type=SnmpAdminString
_CucsVnicProfileRefSourceDn_Object=MibTableColumn
cucsVnicProfileRefSourceDn=_CucsVnicProfileRefSourceDn_Object((1,3,6,1,4,1,9,9,719,1,53,68,1,5),_CucsVnicProfileRefSourceDn_Type())
cucsVnicProfileRefSourceDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicProfileRefSourceDn.setStatus(_A)
_CucsVnicUsnicConPolicyTable_Object=MibTable
cucsVnicUsnicConPolicyTable=_CucsVnicUsnicConPolicyTable_Object((1,3,6,1,4,1,9,9,719,1,53,69))
if mibBuilder.loadTexts:cucsVnicUsnicConPolicyTable.setStatus(_A)
_CucsVnicUsnicConPolicyEntry_Object=MibTableRow
cucsVnicUsnicConPolicyEntry=_CucsVnicUsnicConPolicyEntry_Object((1,3,6,1,4,1,9,9,719,1,53,69,1))
cucsVnicUsnicConPolicyEntry.setIndexNames((0,_C,_AK))
if mibBuilder.loadTexts:cucsVnicUsnicConPolicyEntry.setStatus(_A)
_CucsVnicUsnicConPolicyInstanceId_Type=CucsManagedObjectId
_CucsVnicUsnicConPolicyInstanceId_Object=MibTableColumn
cucsVnicUsnicConPolicyInstanceId=_CucsVnicUsnicConPolicyInstanceId_Object((1,3,6,1,4,1,9,9,719,1,53,69,1,1),_CucsVnicUsnicConPolicyInstanceId_Type())
cucsVnicUsnicConPolicyInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsVnicUsnicConPolicyInstanceId.setStatus(_A)
_CucsVnicUsnicConPolicyDn_Type=CucsManagedObjectDn
_CucsVnicUsnicConPolicyDn_Object=MibTableColumn
cucsVnicUsnicConPolicyDn=_CucsVnicUsnicConPolicyDn_Object((1,3,6,1,4,1,9,9,719,1,53,69,1,2),_CucsVnicUsnicConPolicyDn_Type())
cucsVnicUsnicConPolicyDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicUsnicConPolicyDn.setStatus(_A)
_CucsVnicUsnicConPolicyRn_Type=SnmpAdminString
_CucsVnicUsnicConPolicyRn_Object=MibTableColumn
cucsVnicUsnicConPolicyRn=_CucsVnicUsnicConPolicyRn_Object((1,3,6,1,4,1,9,9,719,1,53,69,1,3),_CucsVnicUsnicConPolicyRn_Type())
cucsVnicUsnicConPolicyRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicUsnicConPolicyRn.setStatus(_A)
_CucsVnicUsnicConPolicyAdaptorProfileName_Type=SnmpAdminString
_CucsVnicUsnicConPolicyAdaptorProfileName_Object=MibTableColumn
cucsVnicUsnicConPolicyAdaptorProfileName=_CucsVnicUsnicConPolicyAdaptorProfileName_Object((1,3,6,1,4,1,9,9,719,1,53,69,1,4),_CucsVnicUsnicConPolicyAdaptorProfileName_Type())
cucsVnicUsnicConPolicyAdaptorProfileName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicUsnicConPolicyAdaptorProfileName.setStatus(_A)
_CucsVnicUsnicConPolicyDescr_Type=SnmpAdminString
_CucsVnicUsnicConPolicyDescr_Object=MibTableColumn
cucsVnicUsnicConPolicyDescr=_CucsVnicUsnicConPolicyDescr_Object((1,3,6,1,4,1,9,9,719,1,53,69,1,5),_CucsVnicUsnicConPolicyDescr_Type())
cucsVnicUsnicConPolicyDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicUsnicConPolicyDescr.setStatus(_A)
_CucsVnicUsnicConPolicyIntId_Type=SnmpAdminString
_CucsVnicUsnicConPolicyIntId_Object=MibTableColumn
cucsVnicUsnicConPolicyIntId=_CucsVnicUsnicConPolicyIntId_Object((1,3,6,1,4,1,9,9,719,1,53,69,1,6),_CucsVnicUsnicConPolicyIntId_Type())
cucsVnicUsnicConPolicyIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicUsnicConPolicyIntId.setStatus(_A)
_CucsVnicUsnicConPolicyName_Type=SnmpAdminString
_CucsVnicUsnicConPolicyName_Object=MibTableColumn
cucsVnicUsnicConPolicyName=_CucsVnicUsnicConPolicyName_Object((1,3,6,1,4,1,9,9,719,1,53,69,1,7),_CucsVnicUsnicConPolicyName_Type())
cucsVnicUsnicConPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicUsnicConPolicyName.setStatus(_A)
_CucsVnicUsnicConPolicyPolicyLevel_Type=Gauge32
_CucsVnicUsnicConPolicyPolicyLevel_Object=MibTableColumn
cucsVnicUsnicConPolicyPolicyLevel=_CucsVnicUsnicConPolicyPolicyLevel_Object((1,3,6,1,4,1,9,9,719,1,53,69,1,8),_CucsVnicUsnicConPolicyPolicyLevel_Type())
cucsVnicUsnicConPolicyPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicUsnicConPolicyPolicyLevel.setStatus(_A)
_CucsVnicUsnicConPolicyPolicyOwner_Type=CucsPolicyPolicyOwner
_CucsVnicUsnicConPolicyPolicyOwner_Object=MibTableColumn
cucsVnicUsnicConPolicyPolicyOwner=_CucsVnicUsnicConPolicyPolicyOwner_Object((1,3,6,1,4,1,9,9,719,1,53,69,1,9),_CucsVnicUsnicConPolicyPolicyOwner_Type())
cucsVnicUsnicConPolicyPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicUsnicConPolicyPolicyOwner.setStatus(_A)
_CucsVnicUsnicConPolicyUsnicCount_Type=Gauge32
_CucsVnicUsnicConPolicyUsnicCount_Object=MibTableColumn
cucsVnicUsnicConPolicyUsnicCount=_CucsVnicUsnicConPolicyUsnicCount_Object((1,3,6,1,4,1,9,9,719,1,53,69,1,10),_CucsVnicUsnicConPolicyUsnicCount_Type())
cucsVnicUsnicConPolicyUsnicCount.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicUsnicConPolicyUsnicCount.setStatus(_A)
_CucsVnicUsnicConPolicyRefTable_Object=MibTable
cucsVnicUsnicConPolicyRefTable=_CucsVnicUsnicConPolicyRefTable_Object((1,3,6,1,4,1,9,9,719,1,53,70))
if mibBuilder.loadTexts:cucsVnicUsnicConPolicyRefTable.setStatus(_A)
_CucsVnicUsnicConPolicyRefEntry_Object=MibTableRow
cucsVnicUsnicConPolicyRefEntry=_CucsVnicUsnicConPolicyRefEntry_Object((1,3,6,1,4,1,9,9,719,1,53,70,1))
cucsVnicUsnicConPolicyRefEntry.setIndexNames((0,_C,_AL))
if mibBuilder.loadTexts:cucsVnicUsnicConPolicyRefEntry.setStatus(_A)
_CucsVnicUsnicConPolicyRefInstanceId_Type=CucsManagedObjectId
_CucsVnicUsnicConPolicyRefInstanceId_Object=MibTableColumn
cucsVnicUsnicConPolicyRefInstanceId=_CucsVnicUsnicConPolicyRefInstanceId_Object((1,3,6,1,4,1,9,9,719,1,53,70,1,1),_CucsVnicUsnicConPolicyRefInstanceId_Type())
cucsVnicUsnicConPolicyRefInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsVnicUsnicConPolicyRefInstanceId.setStatus(_A)
_CucsVnicUsnicConPolicyRefDn_Type=CucsManagedObjectDn
_CucsVnicUsnicConPolicyRefDn_Object=MibTableColumn
cucsVnicUsnicConPolicyRefDn=_CucsVnicUsnicConPolicyRefDn_Object((1,3,6,1,4,1,9,9,719,1,53,70,1,2),_CucsVnicUsnicConPolicyRefDn_Type())
cucsVnicUsnicConPolicyRefDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicUsnicConPolicyRefDn.setStatus(_A)
_CucsVnicUsnicConPolicyRefRn_Type=SnmpAdminString
_CucsVnicUsnicConPolicyRefRn_Object=MibTableColumn
cucsVnicUsnicConPolicyRefRn=_CucsVnicUsnicConPolicyRefRn_Object((1,3,6,1,4,1,9,9,719,1,53,70,1,3),_CucsVnicUsnicConPolicyRefRn_Type())
cucsVnicUsnicConPolicyRefRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicUsnicConPolicyRefRn.setStatus(_A)
_CucsVnicUsnicConPolicyRefConPolicyName_Type=SnmpAdminString
_CucsVnicUsnicConPolicyRefConPolicyName_Object=MibTableColumn
cucsVnicUsnicConPolicyRefConPolicyName=_CucsVnicUsnicConPolicyRefConPolicyName_Object((1,3,6,1,4,1,9,9,719,1,53,70,1,4),_CucsVnicUsnicConPolicyRefConPolicyName_Type())
cucsVnicUsnicConPolicyRefConPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicUsnicConPolicyRefConPolicyName.setStatus(_A)
_CucsVnicUsnicConPolicyRefOperConPolicyName_Type=SnmpAdminString
_CucsVnicUsnicConPolicyRefOperConPolicyName_Object=MibTableColumn
cucsVnicUsnicConPolicyRefOperConPolicyName=_CucsVnicUsnicConPolicyRefOperConPolicyName_Object((1,3,6,1,4,1,9,9,719,1,53,70,1,5),_CucsVnicUsnicConPolicyRefOperConPolicyName_Type())
cucsVnicUsnicConPolicyRefOperConPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicUsnicConPolicyRefOperConPolicyName.setStatus(_A)
_CucsVnicVmqConPolicyTable_Object=MibTable
cucsVnicVmqConPolicyTable=_CucsVnicVmqConPolicyTable_Object((1,3,6,1,4,1,9,9,719,1,53,71))
if mibBuilder.loadTexts:cucsVnicVmqConPolicyTable.setStatus(_A)
_CucsVnicVmqConPolicyEntry_Object=MibTableRow
cucsVnicVmqConPolicyEntry=_CucsVnicVmqConPolicyEntry_Object((1,3,6,1,4,1,9,9,719,1,53,71,1))
cucsVnicVmqConPolicyEntry.setIndexNames((0,_C,_AM))
if mibBuilder.loadTexts:cucsVnicVmqConPolicyEntry.setStatus(_A)
_CucsVnicVmqConPolicyInstanceId_Type=CucsManagedObjectId
_CucsVnicVmqConPolicyInstanceId_Object=MibTableColumn
cucsVnicVmqConPolicyInstanceId=_CucsVnicVmqConPolicyInstanceId_Object((1,3,6,1,4,1,9,9,719,1,53,71,1,1),_CucsVnicVmqConPolicyInstanceId_Type())
cucsVnicVmqConPolicyInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsVnicVmqConPolicyInstanceId.setStatus(_A)
_CucsVnicVmqConPolicyDn_Type=CucsManagedObjectDn
_CucsVnicVmqConPolicyDn_Object=MibTableColumn
cucsVnicVmqConPolicyDn=_CucsVnicVmqConPolicyDn_Object((1,3,6,1,4,1,9,9,719,1,53,71,1,2),_CucsVnicVmqConPolicyDn_Type())
cucsVnicVmqConPolicyDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicVmqConPolicyDn.setStatus(_A)
_CucsVnicVmqConPolicyRn_Type=SnmpAdminString
_CucsVnicVmqConPolicyRn_Object=MibTableColumn
cucsVnicVmqConPolicyRn=_CucsVnicVmqConPolicyRn_Object((1,3,6,1,4,1,9,9,719,1,53,71,1,3),_CucsVnicVmqConPolicyRn_Type())
cucsVnicVmqConPolicyRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicVmqConPolicyRn.setStatus(_A)
_CucsVnicVmqConPolicyDescr_Type=SnmpAdminString
_CucsVnicVmqConPolicyDescr_Object=MibTableColumn
cucsVnicVmqConPolicyDescr=_CucsVnicVmqConPolicyDescr_Object((1,3,6,1,4,1,9,9,719,1,53,71,1,4),_CucsVnicVmqConPolicyDescr_Type())
cucsVnicVmqConPolicyDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicVmqConPolicyDescr.setStatus(_A)
_CucsVnicVmqConPolicyIntId_Type=SnmpAdminString
_CucsVnicVmqConPolicyIntId_Object=MibTableColumn
cucsVnicVmqConPolicyIntId=_CucsVnicVmqConPolicyIntId_Object((1,3,6,1,4,1,9,9,719,1,53,71,1,5),_CucsVnicVmqConPolicyIntId_Type())
cucsVnicVmqConPolicyIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicVmqConPolicyIntId.setStatus(_A)
_CucsVnicVmqConPolicyIntrCount_Type=Gauge32
_CucsVnicVmqConPolicyIntrCount_Object=MibTableColumn
cucsVnicVmqConPolicyIntrCount=_CucsVnicVmqConPolicyIntrCount_Object((1,3,6,1,4,1,9,9,719,1,53,71,1,6),_CucsVnicVmqConPolicyIntrCount_Type())
cucsVnicVmqConPolicyIntrCount.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicVmqConPolicyIntrCount.setStatus(_A)
_CucsVnicVmqConPolicyName_Type=SnmpAdminString
_CucsVnicVmqConPolicyName_Object=MibTableColumn
cucsVnicVmqConPolicyName=_CucsVnicVmqConPolicyName_Object((1,3,6,1,4,1,9,9,719,1,53,71,1,7),_CucsVnicVmqConPolicyName_Type())
cucsVnicVmqConPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicVmqConPolicyName.setStatus(_A)
_CucsVnicVmqConPolicyPolicyLevel_Type=Gauge32
_CucsVnicVmqConPolicyPolicyLevel_Object=MibTableColumn
cucsVnicVmqConPolicyPolicyLevel=_CucsVnicVmqConPolicyPolicyLevel_Object((1,3,6,1,4,1,9,9,719,1,53,71,1,8),_CucsVnicVmqConPolicyPolicyLevel_Type())
cucsVnicVmqConPolicyPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicVmqConPolicyPolicyLevel.setStatus(_A)
_CucsVnicVmqConPolicyPolicyOwner_Type=CucsPolicyPolicyOwner
_CucsVnicVmqConPolicyPolicyOwner_Object=MibTableColumn
cucsVnicVmqConPolicyPolicyOwner=_CucsVnicVmqConPolicyPolicyOwner_Object((1,3,6,1,4,1,9,9,719,1,53,71,1,9),_CucsVnicVmqConPolicyPolicyOwner_Type())
cucsVnicVmqConPolicyPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicVmqConPolicyPolicyOwner.setStatus(_A)
_CucsVnicVmqConPolicyVmqCount_Type=Gauge32
_CucsVnicVmqConPolicyVmqCount_Object=MibTableColumn
cucsVnicVmqConPolicyVmqCount=_CucsVnicVmqConPolicyVmqCount_Object((1,3,6,1,4,1,9,9,719,1,53,71,1,10),_CucsVnicVmqConPolicyVmqCount_Type())
cucsVnicVmqConPolicyVmqCount.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicVmqConPolicyVmqCount.setStatus(_A)
_CucsVnicVmqConPolicyRefTable_Object=MibTable
cucsVnicVmqConPolicyRefTable=_CucsVnicVmqConPolicyRefTable_Object((1,3,6,1,4,1,9,9,719,1,53,72))
if mibBuilder.loadTexts:cucsVnicVmqConPolicyRefTable.setStatus(_A)
_CucsVnicVmqConPolicyRefEntry_Object=MibTableRow
cucsVnicVmqConPolicyRefEntry=_CucsVnicVmqConPolicyRefEntry_Object((1,3,6,1,4,1,9,9,719,1,53,72,1))
cucsVnicVmqConPolicyRefEntry.setIndexNames((0,_C,_AN))
if mibBuilder.loadTexts:cucsVnicVmqConPolicyRefEntry.setStatus(_A)
_CucsVnicVmqConPolicyRefInstanceId_Type=CucsManagedObjectId
_CucsVnicVmqConPolicyRefInstanceId_Object=MibTableColumn
cucsVnicVmqConPolicyRefInstanceId=_CucsVnicVmqConPolicyRefInstanceId_Object((1,3,6,1,4,1,9,9,719,1,53,72,1,1),_CucsVnicVmqConPolicyRefInstanceId_Type())
cucsVnicVmqConPolicyRefInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsVnicVmqConPolicyRefInstanceId.setStatus(_A)
_CucsVnicVmqConPolicyRefDn_Type=CucsManagedObjectDn
_CucsVnicVmqConPolicyRefDn_Object=MibTableColumn
cucsVnicVmqConPolicyRefDn=_CucsVnicVmqConPolicyRefDn_Object((1,3,6,1,4,1,9,9,719,1,53,72,1,2),_CucsVnicVmqConPolicyRefDn_Type())
cucsVnicVmqConPolicyRefDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicVmqConPolicyRefDn.setStatus(_A)
_CucsVnicVmqConPolicyRefRn_Type=SnmpAdminString
_CucsVnicVmqConPolicyRefRn_Object=MibTableColumn
cucsVnicVmqConPolicyRefRn=_CucsVnicVmqConPolicyRefRn_Object((1,3,6,1,4,1,9,9,719,1,53,72,1,3),_CucsVnicVmqConPolicyRefRn_Type())
cucsVnicVmqConPolicyRefRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicVmqConPolicyRefRn.setStatus(_A)
_CucsVnicVmqConPolicyRefConPolicyName_Type=SnmpAdminString
_CucsVnicVmqConPolicyRefConPolicyName_Object=MibTableColumn
cucsVnicVmqConPolicyRefConPolicyName=_CucsVnicVmqConPolicyRefConPolicyName_Object((1,3,6,1,4,1,9,9,719,1,53,72,1,4),_CucsVnicVmqConPolicyRefConPolicyName_Type())
cucsVnicVmqConPolicyRefConPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicVmqConPolicyRefConPolicyName.setStatus(_A)
_CucsVnicVmqConPolicyRefOperConPolicyName_Type=SnmpAdminString
_CucsVnicVmqConPolicyRefOperConPolicyName_Object=MibTableColumn
cucsVnicVmqConPolicyRefOperConPolicyName=_CucsVnicVmqConPolicyRefOperConPolicyName_Object((1,3,6,1,4,1,9,9,719,1,53,72,1,5),_CucsVnicVmqConPolicyRefOperConPolicyName_Type())
cucsVnicVmqConPolicyRefOperConPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicVmqConPolicyRefOperConPolicyName.setStatus(_A)
_CucsVnicIpV6HistoryTable_Object=MibTable
cucsVnicIpV6HistoryTable=_CucsVnicIpV6HistoryTable_Object((1,3,6,1,4,1,9,9,719,1,53,73))
if mibBuilder.loadTexts:cucsVnicIpV6HistoryTable.setStatus(_A)
_CucsVnicIpV6HistoryEntry_Object=MibTableRow
cucsVnicIpV6HistoryEntry=_CucsVnicIpV6HistoryEntry_Object((1,3,6,1,4,1,9,9,719,1,53,73,1))
cucsVnicIpV6HistoryEntry.setIndexNames((0,_C,_AO))
if mibBuilder.loadTexts:cucsVnicIpV6HistoryEntry.setStatus(_A)
_CucsVnicIpV6HistoryInstanceId_Type=CucsManagedObjectId
_CucsVnicIpV6HistoryInstanceId_Object=MibTableColumn
cucsVnicIpV6HistoryInstanceId=_CucsVnicIpV6HistoryInstanceId_Object((1,3,6,1,4,1,9,9,719,1,53,73,1,1),_CucsVnicIpV6HistoryInstanceId_Type())
cucsVnicIpV6HistoryInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsVnicIpV6HistoryInstanceId.setStatus(_A)
_CucsVnicIpV6HistoryDn_Type=CucsManagedObjectDn
_CucsVnicIpV6HistoryDn_Object=MibTableColumn
cucsVnicIpV6HistoryDn=_CucsVnicIpV6HistoryDn_Object((1,3,6,1,4,1,9,9,719,1,53,73,1,2),_CucsVnicIpV6HistoryDn_Type())
cucsVnicIpV6HistoryDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIpV6HistoryDn.setStatus(_A)
_CucsVnicIpV6HistoryRn_Type=SnmpAdminString
_CucsVnicIpV6HistoryRn_Object=MibTableColumn
cucsVnicIpV6HistoryRn=_CucsVnicIpV6HistoryRn_Object((1,3,6,1,4,1,9,9,719,1,53,73,1,3),_CucsVnicIpV6HistoryRn_Type())
cucsVnicIpV6HistoryRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIpV6HistoryRn.setStatus(_A)
_CucsVnicIpV6HistoryOldIpV6Addr_Type=InetAddressIPv6
_CucsVnicIpV6HistoryOldIpV6Addr_Object=MibTableColumn
cucsVnicIpV6HistoryOldIpV6Addr=_CucsVnicIpV6HistoryOldIpV6Addr_Object((1,3,6,1,4,1,9,9,719,1,53,73,1,4),_CucsVnicIpV6HistoryOldIpV6Addr_Type())
cucsVnicIpV6HistoryOldIpV6Addr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIpV6HistoryOldIpV6Addr.setStatus(_A)
_CucsVnicEthConfigTable_Object=MibTable
cucsVnicEthConfigTable=_CucsVnicEthConfigTable_Object((1,3,6,1,4,1,9,9,719,1,53,74))
if mibBuilder.loadTexts:cucsVnicEthConfigTable.setStatus(_A)
_CucsVnicEthConfigEntry_Object=MibTableRow
cucsVnicEthConfigEntry=_CucsVnicEthConfigEntry_Object((1,3,6,1,4,1,9,9,719,1,53,74,1))
cucsVnicEthConfigEntry.setIndexNames((0,_C,_AP))
if mibBuilder.loadTexts:cucsVnicEthConfigEntry.setStatus(_A)
_CucsVnicEthConfigInstanceId_Type=CucsManagedObjectId
_CucsVnicEthConfigInstanceId_Object=MibTableColumn
cucsVnicEthConfigInstanceId=_CucsVnicEthConfigInstanceId_Object((1,3,6,1,4,1,9,9,719,1,53,74,1,1),_CucsVnicEthConfigInstanceId_Type())
cucsVnicEthConfigInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsVnicEthConfigInstanceId.setStatus(_A)
_CucsVnicEthConfigDn_Type=CucsManagedObjectDn
_CucsVnicEthConfigDn_Object=MibTableColumn
cucsVnicEthConfigDn=_CucsVnicEthConfigDn_Object((1,3,6,1,4,1,9,9,719,1,53,74,1,2),_CucsVnicEthConfigDn_Type())
cucsVnicEthConfigDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicEthConfigDn.setStatus(_A)
_CucsVnicEthConfigRn_Type=SnmpAdminString
_CucsVnicEthConfigRn_Object=MibTableColumn
cucsVnicEthConfigRn=_CucsVnicEthConfigRn_Object((1,3,6,1,4,1,9,9,719,1,53,74,1,3),_CucsVnicEthConfigRn_Type())
cucsVnicEthConfigRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicEthConfigRn.setStatus(_A)
_CucsVnicEthConfigAdaptorProfileName_Type=SnmpAdminString
_CucsVnicEthConfigAdaptorProfileName_Object=MibTableColumn
cucsVnicEthConfigAdaptorProfileName=_CucsVnicEthConfigAdaptorProfileName_Object((1,3,6,1,4,1,9,9,719,1,53,74,1,4),_CucsVnicEthConfigAdaptorProfileName_Type())
cucsVnicEthConfigAdaptorProfileName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicEthConfigAdaptorProfileName.setStatus(_A)
_CucsVnicEthConfigMacPoolName_Type=SnmpAdminString
_CucsVnicEthConfigMacPoolName_Object=MibTableColumn
cucsVnicEthConfigMacPoolName=_CucsVnicEthConfigMacPoolName_Object((1,3,6,1,4,1,9,9,719,1,53,74,1,5),_CucsVnicEthConfigMacPoolName_Type())
cucsVnicEthConfigMacPoolName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicEthConfigMacPoolName.setStatus(_A)
_CucsVnicEthConfigNwCtrlPolicyName_Type=SnmpAdminString
_CucsVnicEthConfigNwCtrlPolicyName_Object=MibTableColumn
cucsVnicEthConfigNwCtrlPolicyName=_CucsVnicEthConfigNwCtrlPolicyName_Object((1,3,6,1,4,1,9,9,719,1,53,74,1,6),_CucsVnicEthConfigNwCtrlPolicyName_Type())
cucsVnicEthConfigNwCtrlPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicEthConfigNwCtrlPolicyName.setStatus(_A)
_CucsVnicEthConfigOperAdaptorProfileName_Type=SnmpAdminString
_CucsVnicEthConfigOperAdaptorProfileName_Object=MibTableColumn
cucsVnicEthConfigOperAdaptorProfileName=_CucsVnicEthConfigOperAdaptorProfileName_Object((1,3,6,1,4,1,9,9,719,1,53,74,1,7),_CucsVnicEthConfigOperAdaptorProfileName_Type())
cucsVnicEthConfigOperAdaptorProfileName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicEthConfigOperAdaptorProfileName.setStatus(_A)
_CucsVnicEthConfigOperMacPoolName_Type=SnmpAdminString
_CucsVnicEthConfigOperMacPoolName_Object=MibTableColumn
cucsVnicEthConfigOperMacPoolName=_CucsVnicEthConfigOperMacPoolName_Object((1,3,6,1,4,1,9,9,719,1,53,74,1,8),_CucsVnicEthConfigOperMacPoolName_Type())
cucsVnicEthConfigOperMacPoolName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicEthConfigOperMacPoolName.setStatus(_A)
_CucsVnicEthConfigOperNwCtrlPolicyName_Type=SnmpAdminString
_CucsVnicEthConfigOperNwCtrlPolicyName_Object=MibTableColumn
cucsVnicEthConfigOperNwCtrlPolicyName=_CucsVnicEthConfigOperNwCtrlPolicyName_Object((1,3,6,1,4,1,9,9,719,1,53,74,1,9),_CucsVnicEthConfigOperNwCtrlPolicyName_Type())
cucsVnicEthConfigOperNwCtrlPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicEthConfigOperNwCtrlPolicyName.setStatus(_A)
_CucsVnicEthConfigOperStatsPolicyName_Type=SnmpAdminString
_CucsVnicEthConfigOperStatsPolicyName_Object=MibTableColumn
cucsVnicEthConfigOperStatsPolicyName=_CucsVnicEthConfigOperStatsPolicyName_Object((1,3,6,1,4,1,9,9,719,1,53,74,1,10),_CucsVnicEthConfigOperStatsPolicyName_Type())
cucsVnicEthConfigOperStatsPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicEthConfigOperStatsPolicyName.setStatus(_A)
_CucsVnicEthConfigStatsPolicyName_Type=SnmpAdminString
_CucsVnicEthConfigStatsPolicyName_Object=MibTableColumn
cucsVnicEthConfigStatsPolicyName=_CucsVnicEthConfigStatsPolicyName_Object((1,3,6,1,4,1,9,9,719,1,53,74,1,11),_CucsVnicEthConfigStatsPolicyName_Type())
cucsVnicEthConfigStatsPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicEthConfigStatsPolicyName.setStatus(_A)
_CucsVnicIPv6IfTable_Object=MibTable
cucsVnicIPv6IfTable=_CucsVnicIPv6IfTable_Object((1,3,6,1,4,1,9,9,719,1,53,75))
if mibBuilder.loadTexts:cucsVnicIPv6IfTable.setStatus(_A)
_CucsVnicIPv6IfEntry_Object=MibTableRow
cucsVnicIPv6IfEntry=_CucsVnicIPv6IfEntry_Object((1,3,6,1,4,1,9,9,719,1,53,75,1))
cucsVnicIPv6IfEntry.setIndexNames((0,_C,_AQ))
if mibBuilder.loadTexts:cucsVnicIPv6IfEntry.setStatus(_A)
_CucsVnicIPv6IfInstanceId_Type=CucsManagedObjectId
_CucsVnicIPv6IfInstanceId_Object=MibTableColumn
cucsVnicIPv6IfInstanceId=_CucsVnicIPv6IfInstanceId_Object((1,3,6,1,4,1,9,9,719,1,53,75,1,1),_CucsVnicIPv6IfInstanceId_Type())
cucsVnicIPv6IfInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsVnicIPv6IfInstanceId.setStatus(_A)
_CucsVnicIPv6IfDn_Type=CucsManagedObjectDn
_CucsVnicIPv6IfDn_Object=MibTableColumn
cucsVnicIPv6IfDn=_CucsVnicIPv6IfDn_Object((1,3,6,1,4,1,9,9,719,1,53,75,1,2),_CucsVnicIPv6IfDn_Type())
cucsVnicIPv6IfDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIPv6IfDn.setStatus(_A)
_CucsVnicIPv6IfRn_Type=SnmpAdminString
_CucsVnicIPv6IfRn_Object=MibTableColumn
cucsVnicIPv6IfRn=_CucsVnicIPv6IfRn_Object((1,3,6,1,4,1,9,9,719,1,53,75,1,3),_CucsVnicIPv6IfRn_Type())
cucsVnicIPv6IfRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIPv6IfRn.setStatus(_A)
_CucsVnicIPv6IfAddr_Type=InetAddressIPv6
_CucsVnicIPv6IfAddr_Object=MibTableColumn
cucsVnicIPv6IfAddr=_CucsVnicIPv6IfAddr_Object((1,3,6,1,4,1,9,9,719,1,53,75,1,4),_CucsVnicIPv6IfAddr_Type())
cucsVnicIPv6IfAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIPv6IfAddr.setStatus(_A)
_CucsVnicIPv6IfConfigQualifier_Type=CucsVnicConfigIssues
_CucsVnicIPv6IfConfigQualifier_Object=MibTableColumn
cucsVnicIPv6IfConfigQualifier=_CucsVnicIPv6IfConfigQualifier_Object((1,3,6,1,4,1,9,9,719,1,53,75,1,5),_CucsVnicIPv6IfConfigQualifier_Type())
cucsVnicIPv6IfConfigQualifier.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIPv6IfConfigQualifier.setStatus(_A)
_CucsVnicIPv6IfName_Type=SnmpAdminString
_CucsVnicIPv6IfName_Object=MibTableColumn
cucsVnicIPv6IfName=_CucsVnicIPv6IfName_Object((1,3,6,1,4,1,9,9,719,1,53,75,1,6),_CucsVnicIPv6IfName_Type())
cucsVnicIPv6IfName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIPv6IfName.setStatus(_A)
_CucsVnicIPv6IfOperState_Type=CucsVnicIfOperState
_CucsVnicIPv6IfOperState_Object=MibTableColumn
cucsVnicIPv6IfOperState=_CucsVnicIPv6IfOperState_Object((1,3,6,1,4,1,9,9,719,1,53,75,1,7),_CucsVnicIPv6IfOperState_Type())
cucsVnicIPv6IfOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIPv6IfOperState.setStatus(_A)
_CucsVnicIPv6IfOperVnetDn_Type=SnmpAdminString
_CucsVnicIPv6IfOperVnetDn_Object=MibTableColumn
cucsVnicIPv6IfOperVnetDn=_CucsVnicIPv6IfOperVnetDn_Object((1,3,6,1,4,1,9,9,719,1,53,75,1,8),_CucsVnicIPv6IfOperVnetDn_Type())
cucsVnicIPv6IfOperVnetDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIPv6IfOperVnetDn.setStatus(_A)
_CucsVnicIPv6IfOperVnetName_Type=SnmpAdminString
_CucsVnicIPv6IfOperVnetName_Object=MibTableColumn
cucsVnicIPv6IfOperVnetName=_CucsVnicIPv6IfOperVnetName_Object((1,3,6,1,4,1,9,9,719,1,53,75,1,9),_CucsVnicIPv6IfOperVnetName_Type())
cucsVnicIPv6IfOperVnetName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIPv6IfOperVnetName.setStatus(_A)
_CucsVnicIPv6IfOwner_Type=CucsVnicConnectionOwner
_CucsVnicIPv6IfOwner_Object=MibTableColumn
cucsVnicIPv6IfOwner=_CucsVnicIPv6IfOwner_Object((1,3,6,1,4,1,9,9,719,1,53,75,1,10),_CucsVnicIPv6IfOwner_Type())
cucsVnicIPv6IfOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIPv6IfOwner.setStatus(_A)
_CucsVnicIPv6IfPubNwId_Type=Gauge32
_CucsVnicIPv6IfPubNwId_Object=MibTableColumn
cucsVnicIPv6IfPubNwId=_CucsVnicIPv6IfPubNwId_Object((1,3,6,1,4,1,9,9,719,1,53,75,1,11),_CucsVnicIPv6IfPubNwId_Type())
cucsVnicIPv6IfPubNwId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIPv6IfPubNwId.setStatus(_A)
_CucsVnicIPv6IfSharing_Type=CucsFabricVlanSharingType
_CucsVnicIPv6IfSharing_Object=MibTableColumn
cucsVnicIPv6IfSharing=_CucsVnicIPv6IfSharing_Object((1,3,6,1,4,1,9,9,719,1,53,75,1,12),_CucsVnicIPv6IfSharing_Type())
cucsVnicIPv6IfSharing.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIPv6IfSharing.setStatus(_A)
_CucsVnicIPv6IfSwitchId_Type=CucsNetworkSwitchId
_CucsVnicIPv6IfSwitchId_Object=MibTableColumn
cucsVnicIPv6IfSwitchId=_CucsVnicIPv6IfSwitchId_Object((1,3,6,1,4,1,9,9,719,1,53,75,1,13),_CucsVnicIPv6IfSwitchId_Type())
cucsVnicIPv6IfSwitchId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIPv6IfSwitchId.setStatus(_A)
_CucsVnicIPv6IfType_Type=CucsVnicConnectionType
_CucsVnicIPv6IfType_Object=MibTableColumn
cucsVnicIPv6IfType=_CucsVnicIPv6IfType_Object((1,3,6,1,4,1,9,9,719,1,53,75,1,14),_CucsVnicIPv6IfType_Type())
cucsVnicIPv6IfType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIPv6IfType.setStatus(_A)
_CucsVnicIPv6IfVnet_Type=Gauge32
_CucsVnicIPv6IfVnet_Object=MibTableColumn
cucsVnicIPv6IfVnet=_CucsVnicIPv6IfVnet_Object((1,3,6,1,4,1,9,9,719,1,53,75,1,15),_CucsVnicIPv6IfVnet_Type())
cucsVnicIPv6IfVnet.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIPv6IfVnet.setStatus(_A)
_CucsVnicIPv6IfOperPrimaryVnetDn_Type=SnmpAdminString
_CucsVnicIPv6IfOperPrimaryVnetDn_Object=MibTableColumn
cucsVnicIPv6IfOperPrimaryVnetDn=_CucsVnicIPv6IfOperPrimaryVnetDn_Object((1,3,6,1,4,1,9,9,719,1,53,75,1,16),_CucsVnicIPv6IfOperPrimaryVnetDn_Type())
cucsVnicIPv6IfOperPrimaryVnetDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIPv6IfOperPrimaryVnetDn.setStatus(_A)
_CucsVnicIPv6IfOperPrimaryVnetName_Type=SnmpAdminString
_CucsVnicIPv6IfOperPrimaryVnetName_Object=MibTableColumn
cucsVnicIPv6IfOperPrimaryVnetName=_CucsVnicIPv6IfOperPrimaryVnetName_Object((1,3,6,1,4,1,9,9,719,1,53,75,1,17),_CucsVnicIPv6IfOperPrimaryVnetName_Type())
cucsVnicIPv6IfOperPrimaryVnetName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIPv6IfOperPrimaryVnetName.setStatus(_A)
_CucsVnicIScsiConfigTable_Object=MibTable
cucsVnicIScsiConfigTable=_CucsVnicIScsiConfigTable_Object((1,3,6,1,4,1,9,9,719,1,53,76))
if mibBuilder.loadTexts:cucsVnicIScsiConfigTable.setStatus(_A)
_CucsVnicIScsiConfigEntry_Object=MibTableRow
cucsVnicIScsiConfigEntry=_CucsVnicIScsiConfigEntry_Object((1,3,6,1,4,1,9,9,719,1,53,76,1))
cucsVnicIScsiConfigEntry.setIndexNames((0,_C,_AR))
if mibBuilder.loadTexts:cucsVnicIScsiConfigEntry.setStatus(_A)
_CucsVnicIScsiConfigInstanceId_Type=CucsManagedObjectId
_CucsVnicIScsiConfigInstanceId_Object=MibTableColumn
cucsVnicIScsiConfigInstanceId=_CucsVnicIScsiConfigInstanceId_Object((1,3,6,1,4,1,9,9,719,1,53,76,1,1),_CucsVnicIScsiConfigInstanceId_Type())
cucsVnicIScsiConfigInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsVnicIScsiConfigInstanceId.setStatus(_A)
_CucsVnicIScsiConfigDn_Type=CucsManagedObjectDn
_CucsVnicIScsiConfigDn_Object=MibTableColumn
cucsVnicIScsiConfigDn=_CucsVnicIScsiConfigDn_Object((1,3,6,1,4,1,9,9,719,1,53,76,1,2),_CucsVnicIScsiConfigDn_Type())
cucsVnicIScsiConfigDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiConfigDn.setStatus(_A)
_CucsVnicIScsiConfigRn_Type=SnmpAdminString
_CucsVnicIScsiConfigRn_Object=MibTableColumn
cucsVnicIScsiConfigRn=_CucsVnicIScsiConfigRn_Object((1,3,6,1,4,1,9,9,719,1,53,76,1,3),_CucsVnicIScsiConfigRn_Type())
cucsVnicIScsiConfigRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiConfigRn.setStatus(_A)
_CucsVnicIScsiConfigAdaptorProfileName_Type=SnmpAdminString
_CucsVnicIScsiConfigAdaptorProfileName_Object=MibTableColumn
cucsVnicIScsiConfigAdaptorProfileName=_CucsVnicIScsiConfigAdaptorProfileName_Object((1,3,6,1,4,1,9,9,719,1,53,76,1,4),_CucsVnicIScsiConfigAdaptorProfileName_Type())
cucsVnicIScsiConfigAdaptorProfileName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiConfigAdaptorProfileName.setStatus(_A)
_CucsVnicIScsiConfigIpPoolName_Type=SnmpAdminString
_CucsVnicIScsiConfigIpPoolName_Object=MibTableColumn
cucsVnicIScsiConfigIpPoolName=_CucsVnicIScsiConfigIpPoolName_Object((1,3,6,1,4,1,9,9,719,1,53,76,1,5),_CucsVnicIScsiConfigIpPoolName_Type())
cucsVnicIScsiConfigIpPoolName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiConfigIpPoolName.setStatus(_A)
_CucsVnicIScsiConfigIpPoolNameFabricB_Type=SnmpAdminString
_CucsVnicIScsiConfigIpPoolNameFabricB_Object=MibTableColumn
cucsVnicIScsiConfigIpPoolNameFabricB=_CucsVnicIScsiConfigIpPoolNameFabricB_Object((1,3,6,1,4,1,9,9,719,1,53,76,1,6),_CucsVnicIScsiConfigIpPoolNameFabricB_Type())
cucsVnicIScsiConfigIpPoolNameFabricB.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiConfigIpPoolNameFabricB.setStatus(_A)
_CucsVnicIScsiConfigIpPoolType_Type=CucsVnicIpPoolType
_CucsVnicIScsiConfigIpPoolType_Object=MibTableColumn
cucsVnicIScsiConfigIpPoolType=_CucsVnicIScsiConfigIpPoolType_Object((1,3,6,1,4,1,9,9,719,1,53,76,1,7),_CucsVnicIScsiConfigIpPoolType_Type())
cucsVnicIScsiConfigIpPoolType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiConfigIpPoolType.setStatus(_A)
_CucsVnicIScsiConfigIqnPoolName_Type=SnmpAdminString
_CucsVnicIScsiConfigIqnPoolName_Object=MibTableColumn
cucsVnicIScsiConfigIqnPoolName=_CucsVnicIScsiConfigIqnPoolName_Object((1,3,6,1,4,1,9,9,719,1,53,76,1,8),_CucsVnicIScsiConfigIqnPoolName_Type())
cucsVnicIScsiConfigIqnPoolName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiConfigIqnPoolName.setStatus(_A)
_CucsVnicIScsiConfigOperAdaptorProfileName_Type=SnmpAdminString
_CucsVnicIScsiConfigOperAdaptorProfileName_Object=MibTableColumn
cucsVnicIScsiConfigOperAdaptorProfileName=_CucsVnicIScsiConfigOperAdaptorProfileName_Object((1,3,6,1,4,1,9,9,719,1,53,76,1,9),_CucsVnicIScsiConfigOperAdaptorProfileName_Type())
cucsVnicIScsiConfigOperAdaptorProfileName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiConfigOperAdaptorProfileName.setStatus(_A)
_CucsVnicIScsiConfigOperIpPoolName_Type=SnmpAdminString
_CucsVnicIScsiConfigOperIpPoolName_Object=MibTableColumn
cucsVnicIScsiConfigOperIpPoolName=_CucsVnicIScsiConfigOperIpPoolName_Object((1,3,6,1,4,1,9,9,719,1,53,76,1,10),_CucsVnicIScsiConfigOperIpPoolName_Type())
cucsVnicIScsiConfigOperIpPoolName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiConfigOperIpPoolName.setStatus(_A)
_CucsVnicIScsiConfigOperIpPoolNameFabricB_Type=SnmpAdminString
_CucsVnicIScsiConfigOperIpPoolNameFabricB_Object=MibTableColumn
cucsVnicIScsiConfigOperIpPoolNameFabricB=_CucsVnicIScsiConfigOperIpPoolNameFabricB_Object((1,3,6,1,4,1,9,9,719,1,53,76,1,11),_CucsVnicIScsiConfigOperIpPoolNameFabricB_Type())
cucsVnicIScsiConfigOperIpPoolNameFabricB.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiConfigOperIpPoolNameFabricB.setStatus(_A)
_CucsVnicIScsiConfigOperIqnPoolName_Type=SnmpAdminString
_CucsVnicIScsiConfigOperIqnPoolName_Object=MibTableColumn
cucsVnicIScsiConfigOperIqnPoolName=_CucsVnicIScsiConfigOperIqnPoolName_Object((1,3,6,1,4,1,9,9,719,1,53,76,1,12),_CucsVnicIScsiConfigOperIqnPoolName_Type())
cucsVnicIScsiConfigOperIqnPoolName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiConfigOperIqnPoolName.setStatus(_A)
_CucsVnicIScsiInitAutoConfigPolicyTable_Object=MibTable
cucsVnicIScsiInitAutoConfigPolicyTable=_CucsVnicIScsiInitAutoConfigPolicyTable_Object((1,3,6,1,4,1,9,9,719,1,53,77))
if mibBuilder.loadTexts:cucsVnicIScsiInitAutoConfigPolicyTable.setStatus(_A)
_CucsVnicIScsiInitAutoConfigPolicyEntry_Object=MibTableRow
cucsVnicIScsiInitAutoConfigPolicyEntry=_CucsVnicIScsiInitAutoConfigPolicyEntry_Object((1,3,6,1,4,1,9,9,719,1,53,77,1))
cucsVnicIScsiInitAutoConfigPolicyEntry.setIndexNames((0,_C,_AS))
if mibBuilder.loadTexts:cucsVnicIScsiInitAutoConfigPolicyEntry.setStatus(_A)
_CucsVnicIScsiInitAutoConfigPolicyInstanceId_Type=CucsManagedObjectId
_CucsVnicIScsiInitAutoConfigPolicyInstanceId_Object=MibTableColumn
cucsVnicIScsiInitAutoConfigPolicyInstanceId=_CucsVnicIScsiInitAutoConfigPolicyInstanceId_Object((1,3,6,1,4,1,9,9,719,1,53,77,1,1),_CucsVnicIScsiInitAutoConfigPolicyInstanceId_Type())
cucsVnicIScsiInitAutoConfigPolicyInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsVnicIScsiInitAutoConfigPolicyInstanceId.setStatus(_A)
_CucsVnicIScsiInitAutoConfigPolicyDn_Type=CucsManagedObjectDn
_CucsVnicIScsiInitAutoConfigPolicyDn_Object=MibTableColumn
cucsVnicIScsiInitAutoConfigPolicyDn=_CucsVnicIScsiInitAutoConfigPolicyDn_Object((1,3,6,1,4,1,9,9,719,1,53,77,1,2),_CucsVnicIScsiInitAutoConfigPolicyDn_Type())
cucsVnicIScsiInitAutoConfigPolicyDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiInitAutoConfigPolicyDn.setStatus(_A)
_CucsVnicIScsiInitAutoConfigPolicyRn_Type=SnmpAdminString
_CucsVnicIScsiInitAutoConfigPolicyRn_Object=MibTableColumn
cucsVnicIScsiInitAutoConfigPolicyRn=_CucsVnicIScsiInitAutoConfigPolicyRn_Object((1,3,6,1,4,1,9,9,719,1,53,77,1,3),_CucsVnicIScsiInitAutoConfigPolicyRn_Type())
cucsVnicIScsiInitAutoConfigPolicyRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiInitAutoConfigPolicyRn.setStatus(_A)
_CucsVnicIScsiInitAutoConfigPolicyDescr_Type=SnmpAdminString
_CucsVnicIScsiInitAutoConfigPolicyDescr_Object=MibTableColumn
cucsVnicIScsiInitAutoConfigPolicyDescr=_CucsVnicIScsiInitAutoConfigPolicyDescr_Object((1,3,6,1,4,1,9,9,719,1,53,77,1,4),_CucsVnicIScsiInitAutoConfigPolicyDescr_Type())
cucsVnicIScsiInitAutoConfigPolicyDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiInitAutoConfigPolicyDescr.setStatus(_A)
_CucsVnicIScsiInitAutoConfigPolicyFabricPath_Type=SnmpAdminString
_CucsVnicIScsiInitAutoConfigPolicyFabricPath_Object=MibTableColumn
cucsVnicIScsiInitAutoConfigPolicyFabricPath=_CucsVnicIScsiInitAutoConfigPolicyFabricPath_Object((1,3,6,1,4,1,9,9,719,1,53,77,1,5),_CucsVnicIScsiInitAutoConfigPolicyFabricPath_Type())
cucsVnicIScsiInitAutoConfigPolicyFabricPath.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiInitAutoConfigPolicyFabricPath.setStatus(_A)
_CucsVnicIScsiInitAutoConfigPolicyIntId_Type=SnmpAdminString
_CucsVnicIScsiInitAutoConfigPolicyIntId_Object=MibTableColumn
cucsVnicIScsiInitAutoConfigPolicyIntId=_CucsVnicIScsiInitAutoConfigPolicyIntId_Object((1,3,6,1,4,1,9,9,719,1,53,77,1,6),_CucsVnicIScsiInitAutoConfigPolicyIntId_Type())
cucsVnicIScsiInitAutoConfigPolicyIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiInitAutoConfigPolicyIntId.setStatus(_A)
_CucsVnicIScsiInitAutoConfigPolicyName_Type=SnmpAdminString
_CucsVnicIScsiInitAutoConfigPolicyName_Object=MibTableColumn
cucsVnicIScsiInitAutoConfigPolicyName=_CucsVnicIScsiInitAutoConfigPolicyName_Object((1,3,6,1,4,1,9,9,719,1,53,77,1,7),_CucsVnicIScsiInitAutoConfigPolicyName_Type())
cucsVnicIScsiInitAutoConfigPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiInitAutoConfigPolicyName.setStatus(_A)
_CucsVnicIScsiInitAutoConfigPolicyPolicyLevel_Type=Gauge32
_CucsVnicIScsiInitAutoConfigPolicyPolicyLevel_Object=MibTableColumn
cucsVnicIScsiInitAutoConfigPolicyPolicyLevel=_CucsVnicIScsiInitAutoConfigPolicyPolicyLevel_Object((1,3,6,1,4,1,9,9,719,1,53,77,1,8),_CucsVnicIScsiInitAutoConfigPolicyPolicyLevel_Type())
cucsVnicIScsiInitAutoConfigPolicyPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiInitAutoConfigPolicyPolicyLevel.setStatus(_A)
_CucsVnicIScsiInitAutoConfigPolicyPolicyOwner_Type=CucsPolicyPolicyOwner
_CucsVnicIScsiInitAutoConfigPolicyPolicyOwner_Object=MibTableColumn
cucsVnicIScsiInitAutoConfigPolicyPolicyOwner=_CucsVnicIScsiInitAutoConfigPolicyPolicyOwner_Object((1,3,6,1,4,1,9,9,719,1,53,77,1,9),_CucsVnicIScsiInitAutoConfigPolicyPolicyOwner_Type())
cucsVnicIScsiInitAutoConfigPolicyPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsVnicIScsiInitAutoConfigPolicyPolicyOwner.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'cucsVnicObjects':cucsVnicObjects,'cucsVnicBootTargetTable':cucsVnicBootTargetTable,'cucsVnicBootTargetEntry':cucsVnicBootTargetEntry,_E:cucsVnicBootTargetInstanceId,'cucsVnicBootTargetDn':cucsVnicBootTargetDn,'cucsVnicBootTargetRn':cucsVnicBootTargetRn,'cucsVnicBootTargetLun':cucsVnicBootTargetLun,'cucsVnicBootTargetWwn':cucsVnicBootTargetWwn,'cucsVnicDefBehTable':cucsVnicDefBehTable,'cucsVnicDefBehEntry':cucsVnicDefBehEntry,_F:cucsVnicDefBehInstanceId,'cucsVnicDefBehDn':cucsVnicDefBehDn,'cucsVnicDefBehRn':cucsVnicDefBehRn,'cucsVnicDefBehAction':cucsVnicDefBehAction,'cucsVnicDefBehNwTemplName':cucsVnicDefBehNwTemplName,'cucsVnicDefBehType':cucsVnicDefBehType,'cucsVnicDefBehDescr':cucsVnicDefBehDescr,'cucsVnicDefBehIntId':cucsVnicDefBehIntId,'cucsVnicDefBehName':cucsVnicDefBehName,'cucsVnicDefBehPolicyLevel':cucsVnicDefBehPolicyLevel,'cucsVnicDefBehPolicyOwner':cucsVnicDefBehPolicyOwner,'cucsVnicDynamicConTable':cucsVnicDynamicConTable,'cucsVnicDynamicConEntry':cucsVnicDynamicConEntry,_G:cucsVnicDynamicConInstanceId,'cucsVnicDynamicConDn':cucsVnicDynamicConDn,'cucsVnicDynamicConRn':cucsVnicDynamicConRn,'cucsVnicDynamicConAdaptorProfileName':cucsVnicDynamicConAdaptorProfileName,'cucsVnicDynamicConDescr':cucsVnicDynamicConDescr,'cucsVnicDynamicConDynamicEth':cucsVnicDynamicConDynamicEth,'cucsVnicDynamicConIntId':cucsVnicDynamicConIntId,'cucsVnicDynamicConMtu':cucsVnicDynamicConMtu,'cucsVnicDynamicConName':cucsVnicDynamicConName,'cucsVnicDynamicConNamingPrefix':cucsVnicDynamicConNamingPrefix,'cucsVnicDynamicConProtection':cucsVnicDynamicConProtection,'cucsVnicDynamicConPolicyLevel':cucsVnicDynamicConPolicyLevel,'cucsVnicDynamicConPolicyOwner':cucsVnicDynamicConPolicyOwner,'cucsVnicDynamicConPolicyTable':cucsVnicDynamicConPolicyTable,'cucsVnicDynamicConPolicyEntry':cucsVnicDynamicConPolicyEntry,_H:cucsVnicDynamicConPolicyInstanceId,'cucsVnicDynamicConPolicyDn':cucsVnicDynamicConPolicyDn,'cucsVnicDynamicConPolicyRn':cucsVnicDynamicConPolicyRn,'cucsVnicDynamicConPolicyAdaptorProfileName':cucsVnicDynamicConPolicyAdaptorProfileName,'cucsVnicDynamicConPolicyDescr':cucsVnicDynamicConPolicyDescr,'cucsVnicDynamicConPolicyDynamicEth':cucsVnicDynamicConPolicyDynamicEth,'cucsVnicDynamicConPolicyIntId':cucsVnicDynamicConPolicyIntId,'cucsVnicDynamicConPolicyMtu':cucsVnicDynamicConPolicyMtu,'cucsVnicDynamicConPolicyName':cucsVnicDynamicConPolicyName,'cucsVnicDynamicConPolicyNamingPrefix':cucsVnicDynamicConPolicyNamingPrefix,'cucsVnicDynamicConPolicyProtection':cucsVnicDynamicConPolicyProtection,'cucsVnicDynamicConPolicyPolicyLevel':cucsVnicDynamicConPolicyPolicyLevel,'cucsVnicDynamicConPolicyPolicyOwner':cucsVnicDynamicConPolicyPolicyOwner,'cucsVnicDynamicIdUniverseTable':cucsVnicDynamicIdUniverseTable,'cucsVnicDynamicIdUniverseEntry':cucsVnicDynamicIdUniverseEntry,_I:cucsVnicDynamicIdUniverseInstanceId,'cucsVnicDynamicIdUniverseDn':cucsVnicDynamicIdUniverseDn,'cucsVnicDynamicIdUniverseRn':cucsVnicDynamicIdUniverseRn,'cucsVnicDynamicIdUniverseDescr':cucsVnicDynamicIdUniverseDescr,'cucsVnicDynamicIdUniverseIntId':cucsVnicDynamicIdUniverseIntId,'cucsVnicDynamicIdUniverseName':cucsVnicDynamicIdUniverseName,'cucsVnicDynamicIdUniversePolicyLevel':cucsVnicDynamicIdUniversePolicyLevel,'cucsVnicDynamicIdUniversePolicyOwner':cucsVnicDynamicIdUniversePolicyOwner,'cucsVnicDynamicProviderTable':cucsVnicDynamicProviderTable,'cucsVnicDynamicProviderEntry':cucsVnicDynamicProviderEntry,_J:cucsVnicDynamicProviderInstanceId,'cucsVnicDynamicProviderDn':cucsVnicDynamicProviderDn,'cucsVnicDynamicProviderRn':cucsVnicDynamicProviderRn,'cucsVnicDynamicProviderName':cucsVnicDynamicProviderName,'cucsVnicDynamicProviderEpTable':cucsVnicDynamicProviderEpTable,'cucsVnicDynamicProviderEpEntry':cucsVnicDynamicProviderEpEntry,_K:cucsVnicDynamicProviderEpInstanceId,'cucsVnicDynamicProviderEpDn':cucsVnicDynamicProviderEpDn,'cucsVnicDynamicProviderEpRn':cucsVnicDynamicProviderEpRn,'cucsVnicDynamicProviderEpChassisId':cucsVnicDynamicProviderEpChassisId,'cucsVnicDynamicProviderEpPortId':cucsVnicDynamicProviderEpPortId,'cucsVnicDynamicProviderEpSlotId':cucsVnicDynamicProviderEpSlotId,'cucsVnicDynamicProviderEpSwitchId':cucsVnicDynamicProviderEpSwitchId,'cucsVnicEthLifTable':cucsVnicEthLifTable,'cucsVnicEthLifEntry':cucsVnicEthLifEntry,_L:cucsVnicEthLifInstanceId,'cucsVnicEthLifDn':cucsVnicEthLifDn,'cucsVnicEthLifRn':cucsVnicEthLifRn,'cucsVnicEthLifAddr':cucsVnicEthLifAddr,'cucsVnicEthLifName':cucsVnicEthLifName,'cucsVnicEthLifNicDn':cucsVnicEthLifNicDn,'cucsVnicEthLifOwner':cucsVnicEthLifOwner,'cucsVnicEthLifSwitchId':cucsVnicEthLifSwitchId,'cucsVnicEthLifType':cucsVnicEthLifType,'cucsVnicEthLifVnicDn':cucsVnicEthLifVnicDn,'cucsVnicEtherTable':cucsVnicEtherTable,'cucsVnicEtherEntry':cucsVnicEtherEntry,_M:cucsVnicEtherInstanceId,'cucsVnicEtherDn':cucsVnicEtherDn,'cucsVnicEtherRn':cucsVnicEtherRn,'cucsVnicEtherAdaptorProfileName':cucsVnicEtherAdaptorProfileName,'cucsVnicEtherAddr':cucsVnicEtherAddr,'cucsVnicEtherAdminVcon':cucsVnicEtherAdminVcon,'cucsVnicEtherBootDev':cucsVnicEtherBootDev,'cucsVnicEtherConfigState':cucsVnicEtherConfigState,'cucsVnicEtherEquipmentDn':cucsVnicEtherEquipmentDn,'cucsVnicEtherFltAggr':cucsVnicEtherFltAggr,'cucsVnicEtherIdentPoolName':cucsVnicEtherIdentPoolName,'cucsVnicEtherInstType':cucsVnicEtherInstType,'cucsVnicEtherMtu':cucsVnicEtherMtu,'cucsVnicEtherName':cucsVnicEtherName,'cucsVnicEtherNwCtrlPolicyName':cucsVnicEtherNwCtrlPolicyName,'cucsVnicEtherNwTemplName':cucsVnicEtherNwTemplName,'cucsVnicEtherOperAdaptorProfileName':cucsVnicEtherOperAdaptorProfileName,'cucsVnicEtherOperIdentPoolName':cucsVnicEtherOperIdentPoolName,'cucsVnicEtherOperNwCtrlPolicyName':cucsVnicEtherOperNwCtrlPolicyName,'cucsVnicEtherOperNwTemplName':cucsVnicEtherOperNwTemplName,'cucsVnicEtherOperOrder':cucsVnicEtherOperOrder,'cucsVnicEtherOperQosPolicyName':cucsVnicEtherOperQosPolicyName,'cucsVnicEtherOperSpeed':cucsVnicEtherOperSpeed,'cucsVnicEtherOperStatsPolicyName':cucsVnicEtherOperStatsPolicyName,'cucsVnicEtherOperVcon':cucsVnicEtherOperVcon,'cucsVnicEtherOrder':cucsVnicEtherOrder,'cucsVnicEtherOwner':cucsVnicEtherOwner,'cucsVnicEtherPinToGroupName':cucsVnicEtherPinToGroupName,'cucsVnicEtherQosPolicyName':cucsVnicEtherQosPolicyName,'cucsVnicEtherStatsPolicyName':cucsVnicEtherStatsPolicyName,'cucsVnicEtherSwitchId':cucsVnicEtherSwitchId,'cucsVnicEtherType':cucsVnicEtherType,'cucsVnicEtherOperPinToGroupName':cucsVnicEtherOperPinToGroupName,'cucsVnicEtherConfigQualifier':cucsVnicEtherConfigQualifier,'cucsVnicEtherDynamicId':cucsVnicEtherDynamicId,'cucsVnicEtherPfDn':cucsVnicEtherPfDn,'cucsVnicEtherVirtualizationPreference':cucsVnicEtherVirtualizationPreference,'cucsVnicEtherAdminHostPort':cucsVnicEtherAdminHostPort,'cucsVnicEtherOperHostPort':cucsVnicEtherOperHostPort,'cucsVnicEtherPropAcl':cucsVnicEtherPropAcl,'cucsVnicEtherPurpose':cucsVnicEtherPurpose,'cucsVnicEtherAdminCdnName':cucsVnicEtherAdminCdnName,'cucsVnicEtherOperCdnName':cucsVnicEtherOperCdnName,'cucsVnicEtherCdnSource':cucsVnicEtherCdnSource,'cucsVnicEtherCdnPropInSync':cucsVnicEtherCdnPropInSync,'cucsVnicEtherRedundancyPairType':cucsVnicEtherRedundancyPairType,'cucsVnicEtherRedundancyPeer':cucsVnicEtherRedundancyPeer,'cucsVnicEtherIfTable':cucsVnicEtherIfTable,'cucsVnicEtherIfEntry':cucsVnicEtherIfEntry,_N:cucsVnicEtherIfInstanceId,'cucsVnicEtherIfDn':cucsVnicEtherIfDn,'cucsVnicEtherIfRn':cucsVnicEtherIfRn,'cucsVnicEtherIfAddr':cucsVnicEtherIfAddr,'cucsVnicEtherIfDefaultNet':cucsVnicEtherIfDefaultNet,'cucsVnicEtherIfName':cucsVnicEtherIfName,'cucsVnicEtherIfOperState':cucsVnicEtherIfOperState,'cucsVnicEtherIfOwner':cucsVnicEtherIfOwner,'cucsVnicEtherIfSwitchId':cucsVnicEtherIfSwitchId,'cucsVnicEtherIfType':cucsVnicEtherIfType,'cucsVnicEtherIfVnet':cucsVnicEtherIfVnet,'cucsVnicEtherIfOperVnetDn':cucsVnicEtherIfOperVnetDn,'cucsVnicEtherIfOperVnetName':cucsVnicEtherIfOperVnetName,'cucsVnicEtherIfConfigQualifier':cucsVnicEtherIfConfigQualifier,'cucsVnicEtherIfFltAggr':cucsVnicEtherIfFltAggr,'cucsVnicEtherIfPubNwId':cucsVnicEtherIfPubNwId,'cucsVnicEtherIfSharing':cucsVnicEtherIfSharing,'cucsVnicEtherIfPropAcl':cucsVnicEtherIfPropAcl,'cucsVnicEtherIfOperPrimaryVnetDn':cucsVnicEtherIfOperPrimaryVnetDn,'cucsVnicEtherIfOperPrimaryVnetName':cucsVnicEtherIfOperPrimaryVnetName,'cucsVnicFcTable':cucsVnicFcTable,'cucsVnicFcEntry':cucsVnicFcEntry,_O:cucsVnicFcInstanceId,'cucsVnicFcDn':cucsVnicFcDn,'cucsVnicFcRn':cucsVnicFcRn,'cucsVnicFcAdaptorProfileName':cucsVnicFcAdaptorProfileName,'cucsVnicFcAddr':cucsVnicFcAddr,'cucsVnicFcAdminVcon':cucsVnicFcAdminVcon,'cucsVnicFcBootDev':cucsVnicFcBootDev,'cucsVnicFcConfigState':cucsVnicFcConfigState,'cucsVnicFcEquipmentDn':cucsVnicFcEquipmentDn,'cucsVnicFcFltAggr':cucsVnicFcFltAggr,'cucsVnicFcIdentPoolName':cucsVnicFcIdentPoolName,'cucsVnicFcInstType':cucsVnicFcInstType,'cucsVnicFcMaxDataFieldSize':cucsVnicFcMaxDataFieldSize,'cucsVnicFcName':cucsVnicFcName,'cucsVnicFcNdAddr':cucsVnicFcNdAddr,'cucsVnicFcNwTemplName':cucsVnicFcNwTemplName,'cucsVnicFcOperAdaptorProfileName':cucsVnicFcOperAdaptorProfileName,'cucsVnicFcOperIdentPoolName':cucsVnicFcOperIdentPoolName,'cucsVnicFcOperNwTemplName':cucsVnicFcOperNwTemplName,'cucsVnicFcOperOrder':cucsVnicFcOperOrder,'cucsVnicFcOperQosPolicyName':cucsVnicFcOperQosPolicyName,'cucsVnicFcOperSpeed':cucsVnicFcOperSpeed,'cucsVnicFcOperStatsPolicyName':cucsVnicFcOperStatsPolicyName,'cucsVnicFcOperVcon':cucsVnicFcOperVcon,'cucsVnicFcOrder':cucsVnicFcOrder,'cucsVnicFcOwner':cucsVnicFcOwner,'cucsVnicFcPersBind':cucsVnicFcPersBind,'cucsVnicFcPersBindClear':cucsVnicFcPersBindClear,'cucsVnicFcPinToGroupName':cucsVnicFcPinToGroupName,'cucsVnicFcQosPolicyName':cucsVnicFcQosPolicyName,'cucsVnicFcStatsPolicyName':cucsVnicFcStatsPolicyName,'cucsVnicFcSwitchId':cucsVnicFcSwitchId,'cucsVnicFcType':cucsVnicFcType,'cucsVnicFcOperPinToGroupName':cucsVnicFcOperPinToGroupName,'cucsVnicFcConfigQualifier':cucsVnicFcConfigQualifier,'cucsVnicFcAdminHostPort':cucsVnicFcAdminHostPort,'cucsVnicFcOperHostPort':cucsVnicFcOperHostPort,'cucsVnicFcAdminCdnName':cucsVnicFcAdminCdnName,'cucsVnicFcOperCdnName':cucsVnicFcOperCdnName,'cucsVnicFcCdnSource':cucsVnicFcCdnSource,'cucsVnicFcCdnPropInSync':cucsVnicFcCdnPropInSync,'cucsVnicFcRedundancyPairType':cucsVnicFcRedundancyPairType,'cucsVnicFcRedundancyPeer':cucsVnicFcRedundancyPeer,'cucsVnicFcIfTable':cucsVnicFcIfTable,'cucsVnicFcIfEntry':cucsVnicFcIfEntry,_P:cucsVnicFcIfInstanceId,'cucsVnicFcIfDn':cucsVnicFcIfDn,'cucsVnicFcIfRn':cucsVnicFcIfRn,'cucsVnicFcIfInitiator':cucsVnicFcIfInitiator,'cucsVnicFcIfName':cucsVnicFcIfName,'cucsVnicFcIfOperState':cucsVnicFcIfOperState,'cucsVnicFcIfOwner':cucsVnicFcIfOwner,'cucsVnicFcIfSwitchId':cucsVnicFcIfSwitchId,'cucsVnicFcIfType':cucsVnicFcIfType,'cucsVnicFcIfVnet':cucsVnicFcIfVnet,'cucsVnicFcIfOperVnetDn':cucsVnicFcIfOperVnetDn,'cucsVnicFcIfOperVnetName':cucsVnicFcIfOperVnetName,'cucsVnicFcIfConfigQualifier':cucsVnicFcIfConfigQualifier,'cucsVnicFcIfPubNwId':cucsVnicFcIfPubNwId,'cucsVnicFcIfSharing':cucsVnicFcIfSharing,'cucsVnicFcIfOperPrimaryVnetDn':cucsVnicFcIfOperPrimaryVnetDn,'cucsVnicFcIfOperPrimaryVnetName':cucsVnicFcIfOperPrimaryVnetName,'cucsVnicFcLifTable':cucsVnicFcLifTable,'cucsVnicFcLifEntry':cucsVnicFcLifEntry,_Q:cucsVnicFcLifInstanceId,'cucsVnicFcLifDn':cucsVnicFcLifDn,'cucsVnicFcLifRn':cucsVnicFcLifRn,'cucsVnicFcLifAddr':cucsVnicFcLifAddr,'cucsVnicFcLifName':cucsVnicFcLifName,'cucsVnicFcLifNicDn':cucsVnicFcLifNicDn,'cucsVnicFcLifOwner':cucsVnicFcLifOwner,'cucsVnicFcLifSwitchId':cucsVnicFcLifSwitchId,'cucsVnicFcLifType':cucsVnicFcLifType,'cucsVnicFcLifVnicDn':cucsVnicFcLifVnicDn,'cucsVnicFcNodeTable':cucsVnicFcNodeTable,'cucsVnicFcNodeEntry':cucsVnicFcNodeEntry,_R:cucsVnicFcNodeInstanceId,'cucsVnicFcNodeDn':cucsVnicFcNodeDn,'cucsVnicFcNodeRn':cucsVnicFcNodeRn,'cucsVnicFcNodeAddr':cucsVnicFcNodeAddr,'cucsVnicFcNodeFltAggr':cucsVnicFcNodeFltAggr,'cucsVnicFcNodeIdentPoolName':cucsVnicFcNodeIdentPoolName,'cucsVnicFcNodeOperIdentPoolName':cucsVnicFcNodeOperIdentPoolName,'cucsVnicFcNodeMaxDerivableWWPN':cucsVnicFcNodeMaxDerivableWWPN,'cucsVnicFcNodeOwner':cucsVnicFcNodeOwner,'cucsVnicFcOEIfTable':cucsVnicFcOEIfTable,'cucsVnicFcOEIfEntry':cucsVnicFcOEIfEntry,_S:cucsVnicFcOEIfInstanceId,'cucsVnicFcOEIfDn':cucsVnicFcOEIfDn,'cucsVnicFcOEIfRn':cucsVnicFcOEIfRn,'cucsVnicFcOEIfInitiator':cucsVnicFcOEIfInitiator,'cucsVnicFcOEIfName':cucsVnicFcOEIfName,'cucsVnicFcOEIfOperState':cucsVnicFcOEIfOperState,'cucsVnicFcOEIfOwner':cucsVnicFcOEIfOwner,'cucsVnicFcOEIfSwitchId':cucsVnicFcOEIfSwitchId,'cucsVnicFcOEIfType':cucsVnicFcOEIfType,'cucsVnicFcOEIfVnet':cucsVnicFcOEIfVnet,'cucsVnicFcOEIfConfigQualifier':cucsVnicFcOEIfConfigQualifier,'cucsVnicFcOEIfOperVnetDn':cucsVnicFcOEIfOperVnetDn,'cucsVnicFcOEIfOperVnetName':cucsVnicFcOEIfOperVnetName,'cucsVnicFcOEIfPubNwId':cucsVnicFcOEIfPubNwId,'cucsVnicFcOEIfSharing':cucsVnicFcOEIfSharing,'cucsVnicFcOEIfOperPrimaryVnetDn':cucsVnicFcOEIfOperPrimaryVnetDn,'cucsVnicFcOEIfOperPrimaryVnetName':cucsVnicFcOEIfOperPrimaryVnetName,'cucsVnicIPv4DhcpTable':cucsVnicIPv4DhcpTable,'cucsVnicIPv4DhcpEntry':cucsVnicIPv4DhcpEntry,_T:cucsVnicIPv4DhcpInstanceId,'cucsVnicIPv4DhcpDn':cucsVnicIPv4DhcpDn,'cucsVnicIPv4DhcpRn':cucsVnicIPv4DhcpRn,'cucsVnicIPv4DhcpAddr':cucsVnicIPv4DhcpAddr,'cucsVnicIPv4DhcpDefGw':cucsVnicIPv4DhcpDefGw,'cucsVnicIPv4DhcpSubnet':cucsVnicIPv4DhcpSubnet,'cucsVnicIPv4DnsTable':cucsVnicIPv4DnsTable,'cucsVnicIPv4DnsEntry':cucsVnicIPv4DnsEntry,_U:cucsVnicIPv4DnsInstanceId,'cucsVnicIPv4DnsDn':cucsVnicIPv4DnsDn,'cucsVnicIPv4DnsRn':cucsVnicIPv4DnsRn,'cucsVnicIPv4DnsAddr':cucsVnicIPv4DnsAddr,'cucsVnicIPv4DnsDefGw':cucsVnicIPv4DnsDefGw,'cucsVnicIPv4DnsPref':cucsVnicIPv4DnsPref,'cucsVnicIPv4DnsSubnet':cucsVnicIPv4DnsSubnet,'cucsVnicIPv4IfTable':cucsVnicIPv4IfTable,'cucsVnicIPv4IfEntry':cucsVnicIPv4IfEntry,_V:cucsVnicIPv4IfInstanceId,'cucsVnicIPv4IfDn':cucsVnicIPv4IfDn,'cucsVnicIPv4IfRn':cucsVnicIPv4IfRn,'cucsVnicIPv4IfAddr':cucsVnicIPv4IfAddr,'cucsVnicIPv4IfName':cucsVnicIPv4IfName,'cucsVnicIPv4IfOperState':cucsVnicIPv4IfOperState,'cucsVnicIPv4IfOwner':cucsVnicIPv4IfOwner,'cucsVnicIPv4IfSwitchId':cucsVnicIPv4IfSwitchId,'cucsVnicIPv4IfType':cucsVnicIPv4IfType,'cucsVnicIPv4IfVnet':cucsVnicIPv4IfVnet,'cucsVnicIPv4IfConfigQualifier':cucsVnicIPv4IfConfigQualifier,'cucsVnicIPv4IfOperVnetDn':cucsVnicIPv4IfOperVnetDn,'cucsVnicIPv4IfOperVnetName':cucsVnicIPv4IfOperVnetName,'cucsVnicIPv4IfPubNwId':cucsVnicIPv4IfPubNwId,'cucsVnicIPv4IfSharing':cucsVnicIPv4IfSharing,'cucsVnicIPv4IfPropAcl':cucsVnicIPv4IfPropAcl,'cucsVnicIPv4IfOperPrimaryVnetDn':cucsVnicIPv4IfOperPrimaryVnetDn,'cucsVnicIPv4IfOperPrimaryVnetName':cucsVnicIPv4IfOperPrimaryVnetName,'cucsVnicIPv4StaticRouteTable':cucsVnicIPv4StaticRouteTable,'cucsVnicIPv4StaticRouteEntry':cucsVnicIPv4StaticRouteEntry,_W:cucsVnicIPv4StaticRouteInstanceId,'cucsVnicIPv4StaticRouteDn':cucsVnicIPv4StaticRouteDn,'cucsVnicIPv4StaticRouteRn':cucsVnicIPv4StaticRouteRn,'cucsVnicIPv4StaticRouteAddr':cucsVnicIPv4StaticRouteAddr,'cucsVnicIPv4StaticRouteDefGw':cucsVnicIPv4StaticRouteDefGw,'cucsVnicIPv4StaticRouteGwAddr':cucsVnicIPv4StaticRouteGwAddr,'cucsVnicIPv4StaticRouteGwSubnet':cucsVnicIPv4StaticRouteGwSubnet,'cucsVnicIPv4StaticRouteSubnet':cucsVnicIPv4StaticRouteSubnet,'cucsVnicIpV4PooledAddrTable':cucsVnicIpV4PooledAddrTable,'cucsVnicIpV4PooledAddrEntry':cucsVnicIpV4PooledAddrEntry,_X:cucsVnicIpV4PooledAddrInstanceId,'cucsVnicIpV4PooledAddrDn':cucsVnicIpV4PooledAddrDn,'cucsVnicIpV4PooledAddrRn':cucsVnicIpV4PooledAddrRn,'cucsVnicIpV4PooledAddrAddr':cucsVnicIpV4PooledAddrAddr,'cucsVnicIpV4PooledAddrDefGw':cucsVnicIpV4PooledAddrDefGw,'cucsVnicIpV4PooledAddrName':cucsVnicIpV4PooledAddrName,'cucsVnicIpV4PooledAddrSubnet':cucsVnicIpV4PooledAddrSubnet,'cucsVnicIpV4PooledAddrOperName':cucsVnicIpV4PooledAddrOperName,'cucsVnicIpV4PooledAddrPrimDns':cucsVnicIpV4PooledAddrPrimDns,'cucsVnicIpV4PooledAddrSecDns':cucsVnicIpV4PooledAddrSecDns,'cucsVnicIpV4ProfDerivedAddrTable':cucsVnicIpV4ProfDerivedAddrTable,'cucsVnicIpV4ProfDerivedAddrEntry':cucsVnicIpV4ProfDerivedAddrEntry,_Y:cucsVnicIpV4ProfDerivedAddrInstanceId,'cucsVnicIpV4ProfDerivedAddrDn':cucsVnicIpV4ProfDerivedAddrDn,'cucsVnicIpV4ProfDerivedAddrRn':cucsVnicIpV4ProfDerivedAddrRn,'cucsVnicIpV4ProfDerivedAddrAddr':cucsVnicIpV4ProfDerivedAddrAddr,'cucsVnicIpV4ProfDerivedAddrDefGw':cucsVnicIpV4ProfDerivedAddrDefGw,'cucsVnicIpV4ProfDerivedAddrSubnet':cucsVnicIpV4ProfDerivedAddrSubnet,'cucsVnicIpV4StaticAddrTable':cucsVnicIpV4StaticAddrTable,'cucsVnicIpV4StaticAddrEntry':cucsVnicIpV4StaticAddrEntry,_Z:cucsVnicIpV4StaticAddrInstanceId,'cucsVnicIpV4StaticAddrDn':cucsVnicIpV4StaticAddrDn,'cucsVnicIpV4StaticAddrRn':cucsVnicIpV4StaticAddrRn,'cucsVnicIpV4StaticAddrAddr':cucsVnicIpV4StaticAddrAddr,'cucsVnicIpV4StaticAddrDefGw':cucsVnicIpV4StaticAddrDefGw,'cucsVnicIpV4StaticAddrSubnet':cucsVnicIpV4StaticAddrSubnet,'cucsVnicIpV4StaticAddrPrimDns':cucsVnicIpV4StaticAddrPrimDns,'cucsVnicIpV4StaticAddrSecDns':cucsVnicIpV4StaticAddrSecDns,'cucsVnicIpcTable':cucsVnicIpcTable,'cucsVnicIpcEntry':cucsVnicIpcEntry,_a:cucsVnicIpcInstanceId,'cucsVnicIpcDn':cucsVnicIpcDn,'cucsVnicIpcRn':cucsVnicIpcRn,'cucsVnicIpcAdaptorProfileName':cucsVnicIpcAdaptorProfileName,'cucsVnicIpcAddr':cucsVnicIpcAddr,'cucsVnicIpcAdminVcon':cucsVnicIpcAdminVcon,'cucsVnicIpcBootDev':cucsVnicIpcBootDev,'cucsVnicIpcConfigState':cucsVnicIpcConfigState,'cucsVnicIpcEquipmentDn':cucsVnicIpcEquipmentDn,'cucsVnicIpcIdentPoolName':cucsVnicIpcIdentPoolName,'cucsVnicIpcInstType':cucsVnicIpcInstType,'cucsVnicIpcMtu':cucsVnicIpcMtu,'cucsVnicIpcName':cucsVnicIpcName,'cucsVnicIpcNwCtrlPolicyName':cucsVnicIpcNwCtrlPolicyName,'cucsVnicIpcNwTemplName':cucsVnicIpcNwTemplName,'cucsVnicIpcOperAdaptorProfileName':cucsVnicIpcOperAdaptorProfileName,'cucsVnicIpcOperIdentPoolName':cucsVnicIpcOperIdentPoolName,'cucsVnicIpcOperNwCtrlPolicyName':cucsVnicIpcOperNwCtrlPolicyName,'cucsVnicIpcOperNwTemplName':cucsVnicIpcOperNwTemplName,'cucsVnicIpcOperOrder':cucsVnicIpcOperOrder,'cucsVnicIpcOperQosPolicyName':cucsVnicIpcOperQosPolicyName,'cucsVnicIpcOperSpeed':cucsVnicIpcOperSpeed,'cucsVnicIpcOperStatsPolicyName':cucsVnicIpcOperStatsPolicyName,'cucsVnicIpcOperVcon':cucsVnicIpcOperVcon,'cucsVnicIpcOrder':cucsVnicIpcOrder,'cucsVnicIpcOwner':cucsVnicIpcOwner,'cucsVnicIpcPinToGroupName':cucsVnicIpcPinToGroupName,'cucsVnicIpcQosPolicyName':cucsVnicIpcQosPolicyName,'cucsVnicIpcStatsPolicyName':cucsVnicIpcStatsPolicyName,'cucsVnicIpcSwitchId':cucsVnicIpcSwitchId,'cucsVnicIpcType':cucsVnicIpcType,'cucsVnicIpcOperPinToGroupName':cucsVnicIpcOperPinToGroupName,'cucsVnicIpcConfigQualifier':cucsVnicIpcConfigQualifier,'cucsVnicIpcAdminHostPort':cucsVnicIpcAdminHostPort,'cucsVnicIpcOperHostPort':cucsVnicIpcOperHostPort,'cucsVnicIpcPurpose':cucsVnicIpcPurpose,'cucsVnicIpcAdminCdnName':cucsVnicIpcAdminCdnName,'cucsVnicIpcOperCdnName':cucsVnicIpcOperCdnName,'cucsVnicIpcCdnPropInSync':cucsVnicIpcCdnPropInSync,'cucsVnicIpcCdnSource':cucsVnicIpcCdnSource,'cucsVnicIpcRedundancyPairType':cucsVnicIpcRedundancyPairType,'cucsVnicIpcRedundancyPeer':cucsVnicIpcRedundancyPeer,'cucsVnicIpcIfTable':cucsVnicIpcIfTable,'cucsVnicIpcIfEntry':cucsVnicIpcIfEntry,_b:cucsVnicIpcIfInstanceId,'cucsVnicIpcIfDn':cucsVnicIpcIfDn,'cucsVnicIpcIfRn':cucsVnicIpcIfRn,'cucsVnicIpcIfAddr':cucsVnicIpcIfAddr,'cucsVnicIpcIfDefaultNet':cucsVnicIpcIfDefaultNet,'cucsVnicIpcIfName':cucsVnicIpcIfName,'cucsVnicIpcIfOperState':cucsVnicIpcIfOperState,'cucsVnicIpcIfOwner':cucsVnicIpcIfOwner,'cucsVnicIpcIfSwitchId':cucsVnicIpcIfSwitchId,'cucsVnicIpcIfType':cucsVnicIpcIfType,'cucsVnicIpcIfVnet':cucsVnicIpcIfVnet,'cucsVnicIpcIfConfigQualifier':cucsVnicIpcIfConfigQualifier,'cucsVnicIpcIfOperVnetDn':cucsVnicIpcIfOperVnetDn,'cucsVnicIpcIfOperVnetName':cucsVnicIpcIfOperVnetName,'cucsVnicIpcIfPubNwId':cucsVnicIpcIfPubNwId,'cucsVnicIpcIfSharing':cucsVnicIpcIfSharing,'cucsVnicIpcIfOperPrimaryVnetDn':cucsVnicIpcIfOperPrimaryVnetDn,'cucsVnicIpcIfOperPrimaryVnetName':cucsVnicIpcIfOperPrimaryVnetName,'cucsVnicLanConnTemplTable':cucsVnicLanConnTemplTable,'cucsVnicLanConnTemplEntry':cucsVnicLanConnTemplEntry,_c:cucsVnicLanConnTemplInstanceId,'cucsVnicLanConnTemplDn':cucsVnicLanConnTemplDn,'cucsVnicLanConnTemplRn':cucsVnicLanConnTemplRn,'cucsVnicLanConnTemplDescr':cucsVnicLanConnTemplDescr,'cucsVnicLanConnTemplIdentPoolName':cucsVnicLanConnTemplIdentPoolName,'cucsVnicLanConnTemplIntId':cucsVnicLanConnTemplIntId,'cucsVnicLanConnTemplMtu':cucsVnicLanConnTemplMtu,'cucsVnicLanConnTemplName':cucsVnicLanConnTemplName,'cucsVnicLanConnTemplNwCtrlPolicyName':cucsVnicLanConnTemplNwCtrlPolicyName,'cucsVnicLanConnTemplOperIdentPoolName':cucsVnicLanConnTemplOperIdentPoolName,'cucsVnicLanConnTemplOperNwCtrlPolicyName':cucsVnicLanConnTemplOperNwCtrlPolicyName,'cucsVnicLanConnTemplOperQosPolicyName':cucsVnicLanConnTemplOperQosPolicyName,'cucsVnicLanConnTemplOperStatsPolicyName':cucsVnicLanConnTemplOperStatsPolicyName,'cucsVnicLanConnTemplPinToGroupName':cucsVnicLanConnTemplPinToGroupName,'cucsVnicLanConnTemplQosPolicyName':cucsVnicLanConnTemplQosPolicyName,'cucsVnicLanConnTemplStatsPolicyName':cucsVnicLanConnTemplStatsPolicyName,'cucsVnicLanConnTemplSwitchId':cucsVnicLanConnTemplSwitchId,'cucsVnicLanConnTemplTarget':cucsVnicLanConnTemplTarget,'cucsVnicLanConnTemplTemplType':cucsVnicLanConnTemplTemplType,'cucsVnicLanConnTemplPolicyLevel':cucsVnicLanConnTemplPolicyLevel,'cucsVnicLanConnTemplPolicyOwner':cucsVnicLanConnTemplPolicyOwner,'cucsVnicLanConnTemplAdminCdnName':cucsVnicLanConnTemplAdminCdnName,'cucsVnicLanConnTemplCdnSource':cucsVnicLanConnTemplCdnSource,'cucsVnicLanConnTemplOperPeerRedundancyTemplName':cucsVnicLanConnTemplOperPeerRedundancyTemplName,'cucsVnicLanConnTemplPeerRedundancyTemplName':cucsVnicLanConnTemplPeerRedundancyTemplName,'cucsVnicLanConnTemplRedundancyPairType':cucsVnicLanConnTemplRedundancyPairType,'cucsVnicLifVlanTable':cucsVnicLifVlanTable,'cucsVnicLifVlanEntry':cucsVnicLifVlanEntry,_d:cucsVnicLifVlanInstanceId,'cucsVnicLifVlanDn':cucsVnicLifVlanDn,'cucsVnicLifVlanRn':cucsVnicLifVlanRn,'cucsVnicLifVlanAddr':cucsVnicLifVlanAddr,'cucsVnicLifVlanDefaultNet':cucsVnicLifVlanDefaultNet,'cucsVnicLifVlanName':cucsVnicLifVlanName,'cucsVnicLifVlanOperState':cucsVnicLifVlanOperState,'cucsVnicLifVlanOwner':cucsVnicLifVlanOwner,'cucsVnicLifVlanSwitchId':cucsVnicLifVlanSwitchId,'cucsVnicLifVlanType':cucsVnicLifVlanType,'cucsVnicLifVlanVnet':cucsVnicLifVlanVnet,'cucsVnicLifVlanConfigQualifier':cucsVnicLifVlanConfigQualifier,'cucsVnicLifVlanOperVnetDn':cucsVnicLifVlanOperVnetDn,'cucsVnicLifVlanOperVnetName':cucsVnicLifVlanOperVnetName,'cucsVnicLifVlanPubNwId':cucsVnicLifVlanPubNwId,'cucsVnicLifVlanSharing':cucsVnicLifVlanSharing,'cucsVnicLifVlanPropAcl':cucsVnicLifVlanPropAcl,'cucsVnicLifVlanOperPrimaryVnetDn':cucsVnicLifVlanOperPrimaryVnetDn,'cucsVnicLifVlanOperPrimaryVnetName':cucsVnicLifVlanOperPrimaryVnetName,'cucsVnicLifVsanTable':cucsVnicLifVsanTable,'cucsVnicLifVsanEntry':cucsVnicLifVsanEntry,_e:cucsVnicLifVsanInstanceId,'cucsVnicLifVsanDn':cucsVnicLifVsanDn,'cucsVnicLifVsanRn':cucsVnicLifVsanRn,'cucsVnicLifVsanInitiator':cucsVnicLifVsanInitiator,'cucsVnicLifVsanName':cucsVnicLifVsanName,'cucsVnicLifVsanOperState':cucsVnicLifVsanOperState,'cucsVnicLifVsanOwner':cucsVnicLifVsanOwner,'cucsVnicLifVsanSwitchId':cucsVnicLifVsanSwitchId,'cucsVnicLifVsanType':cucsVnicLifVsanType,'cucsVnicLifVsanVnet':cucsVnicLifVsanVnet,'cucsVnicLifVsanConfigQualifier':cucsVnicLifVsanConfigQualifier,'cucsVnicLifVsanOperVnetDn':cucsVnicLifVsanOperVnetDn,'cucsVnicLifVsanOperVnetName':cucsVnicLifVsanOperVnetName,'cucsVnicLifVsanPubNwId':cucsVnicLifVsanPubNwId,'cucsVnicLifVsanSharing':cucsVnicLifVsanSharing,'cucsVnicLifVsanOperPrimaryVnetDn':cucsVnicLifVsanOperPrimaryVnetDn,'cucsVnicLifVsanOperPrimaryVnetName':cucsVnicLifVsanOperPrimaryVnetName,'cucsVnicProfileTable':cucsVnicProfileTable,'cucsVnicProfileEntry':cucsVnicProfileEntry,_f:cucsVnicProfileInstanceId,'cucsVnicProfileDn':cucsVnicProfileDn,'cucsVnicProfileRn':cucsVnicProfileRn,'cucsVnicProfileCdp':cucsVnicProfileCdp,'cucsVnicProfileCos':cucsVnicProfileCos,'cucsVnicProfileDescr':cucsVnicProfileDescr,'cucsVnicProfileForgeMac':cucsVnicProfileForgeMac,'cucsVnicProfileIntId':cucsVnicProfileIntId,'cucsVnicProfileMaxPorts':cucsVnicProfileMaxPorts,'cucsVnicProfileName':cucsVnicProfileName,'cucsVnicProfileNwCtrlPolicyName':cucsVnicProfileNwCtrlPolicyName,'cucsVnicProfileOperNwCtrlPolicyName':cucsVnicProfileOperNwCtrlPolicyName,'cucsVnicProfileOperQosPolicyName':cucsVnicProfileOperQosPolicyName,'cucsVnicProfilePinToGroupName':cucsVnicProfilePinToGroupName,'cucsVnicProfileQosPolicyId':cucsVnicProfileQosPolicyId,'cucsVnicProfileQosPolicyName':cucsVnicProfileQosPolicyName,'cucsVnicProfileSwABorderPort':cucsVnicProfileSwABorderPort,'cucsVnicProfileSwABorderSlot':cucsVnicProfileSwABorderSlot,'cucsVnicProfileSwBBorderPort':cucsVnicProfileSwBBorderPort,'cucsVnicProfileSwBBorderSlot':cucsVnicProfileSwBBorderSlot,'cucsVnicProfileUplinkFailAction':cucsVnicProfileUplinkFailAction,'cucsVnicProfileHostNwIOPerf':cucsVnicProfileHostNwIOPerf,'cucsVnicProfilePrimaryVlanId':cucsVnicProfilePrimaryVlanId,'cucsVnicProfileQosPolicyDn':cucsVnicProfileQosPolicyDn,'cucsVnicProfileConfigQualifier':cucsVnicProfileConfigQualifier,'cucsVnicProfileMacRegisterMode':cucsVnicProfileMacRegisterMode,'cucsVnicProfilePolicyLevel':cucsVnicProfilePolicyLevel,'cucsVnicProfilePolicyOwner':cucsVnicProfilePolicyOwner,'cucsVnicProfilePortProfileUuid':cucsVnicProfilePortProfileUuid,'cucsVnicProfileType':cucsVnicProfileType,'cucsVnicProfileSwABorderAggrPort':cucsVnicProfileSwABorderAggrPort,'cucsVnicProfileSwBBorderAggrPort':cucsVnicProfileSwBBorderAggrPort,'cucsVnicProfileLldp':cucsVnicProfileLldp,'cucsVnicProfileAliasTable':cucsVnicProfileAliasTable,'cucsVnicProfileAliasEntry':cucsVnicProfileAliasEntry,_g:cucsVnicProfileAliasInstanceId,'cucsVnicProfileAliasDn':cucsVnicProfileAliasDn,'cucsVnicProfileAliasRn':cucsVnicProfileAliasRn,'cucsVnicProfileAliasAlias':cucsVnicProfileAliasAlias,'cucsVnicProfileAliasSwUuid':cucsVnicProfileAliasSwUuid,'cucsVnicProfileSetTable':cucsVnicProfileSetTable,'cucsVnicProfileSetEntry':cucsVnicProfileSetEntry,_h:cucsVnicProfileSetInstanceId,'cucsVnicProfileSetDn':cucsVnicProfileSetDn,'cucsVnicProfileSetRn':cucsVnicProfileSetRn,'cucsVnicProfileSetFsmDescr':cucsVnicProfileSetFsmDescr,'cucsVnicProfileSetFsmPrev':cucsVnicProfileSetFsmPrev,'cucsVnicProfileSetFsmProgr':cucsVnicProfileSetFsmProgr,'cucsVnicProfileSetFsmRmtInvErrCode':cucsVnicProfileSetFsmRmtInvErrCode,'cucsVnicProfileSetFsmRmtInvErrDescr':cucsVnicProfileSetFsmRmtInvErrDescr,'cucsVnicProfileSetFsmRmtInvRslt':cucsVnicProfileSetFsmRmtInvRslt,'cucsVnicProfileSetFsmStageDescr':cucsVnicProfileSetFsmStageDescr,'cucsVnicProfileSetFsmStamp':cucsVnicProfileSetFsmStamp,'cucsVnicProfileSetFsmStatus':cucsVnicProfileSetFsmStatus,'cucsVnicProfileSetFsmTry':cucsVnicProfileSetFsmTry,'cucsVnicProfileSetFltAggr':cucsVnicProfileSetFltAggr,'cucsVnicProfileSetGenNum':cucsVnicProfileSetGenNum,'cucsVnicProfileSetVlanGroupUpdate':cucsVnicProfileSetVlanGroupUpdate,'cucsVnicProfileSetFsmTaskTable':cucsVnicProfileSetFsmTaskTable,'cucsVnicProfileSetFsmTaskEntry':cucsVnicProfileSetFsmTaskEntry,_i:cucsVnicProfileSetFsmTaskInstanceId,'cucsVnicProfileSetFsmTaskDn':cucsVnicProfileSetFsmTaskDn,'cucsVnicProfileSetFsmTaskRn':cucsVnicProfileSetFsmTaskRn,'cucsVnicProfileSetFsmTaskCompletion':cucsVnicProfileSetFsmTaskCompletion,'cucsVnicProfileSetFsmTaskFlags':cucsVnicProfileSetFsmTaskFlags,'cucsVnicProfileSetFsmTaskItem':cucsVnicProfileSetFsmTaskItem,'cucsVnicProfileSetFsmTaskSeqId':cucsVnicProfileSetFsmTaskSeqId,'cucsVnicSanConnTemplTable':cucsVnicSanConnTemplTable,'cucsVnicSanConnTemplEntry':cucsVnicSanConnTemplEntry,_j:cucsVnicSanConnTemplInstanceId,'cucsVnicSanConnTemplDn':cucsVnicSanConnTemplDn,'cucsVnicSanConnTemplRn':cucsVnicSanConnTemplRn,'cucsVnicSanConnTemplDescr':cucsVnicSanConnTemplDescr,'cucsVnicSanConnTemplIdentPoolName':cucsVnicSanConnTemplIdentPoolName,'cucsVnicSanConnTemplIntId':cucsVnicSanConnTemplIntId,'cucsVnicSanConnTemplMaxDataFieldSize':cucsVnicSanConnTemplMaxDataFieldSize,'cucsVnicSanConnTemplName':cucsVnicSanConnTemplName,'cucsVnicSanConnTemplNwCtrlPolicyName':cucsVnicSanConnTemplNwCtrlPolicyName,'cucsVnicSanConnTemplOperIdentPoolName':cucsVnicSanConnTemplOperIdentPoolName,'cucsVnicSanConnTemplOperQosPolicyName':cucsVnicSanConnTemplOperQosPolicyName,'cucsVnicSanConnTemplOperStatsPolicyName':cucsVnicSanConnTemplOperStatsPolicyName,'cucsVnicSanConnTemplPinToGroupName':cucsVnicSanConnTemplPinToGroupName,'cucsVnicSanConnTemplQosPolicyName':cucsVnicSanConnTemplQosPolicyName,'cucsVnicSanConnTemplStatsPolicyName':cucsVnicSanConnTemplStatsPolicyName,'cucsVnicSanConnTemplSwitchId':cucsVnicSanConnTemplSwitchId,'cucsVnicSanConnTemplTarget':cucsVnicSanConnTemplTarget,'cucsVnicSanConnTemplTemplType':cucsVnicSanConnTemplTemplType,'cucsVnicSanConnTemplPolicyLevel':cucsVnicSanConnTemplPolicyLevel,'cucsVnicSanConnTemplPolicyOwner':cucsVnicSanConnTemplPolicyOwner,'cucsVnicSanConnTemplOperPeerRedundancyTemplName':cucsVnicSanConnTemplOperPeerRedundancyTemplName,'cucsVnicSanConnTemplPeerRedundancyTemplName':cucsVnicSanConnTemplPeerRedundancyTemplName,'cucsVnicSanConnTemplRedundancyPairType':cucsVnicSanConnTemplRedundancyPairType,'cucsVnicScsiTable':cucsVnicScsiTable,'cucsVnicScsiEntry':cucsVnicScsiEntry,_k:cucsVnicScsiInstanceId,'cucsVnicScsiDn':cucsVnicScsiDn,'cucsVnicScsiRn':cucsVnicScsiRn,'cucsVnicScsiAdaptorProfileName':cucsVnicScsiAdaptorProfileName,'cucsVnicScsiAdminVcon':cucsVnicScsiAdminVcon,'cucsVnicScsiBootDev':cucsVnicScsiBootDev,'cucsVnicScsiConfigState':cucsVnicScsiConfigState,'cucsVnicScsiEquipmentDn':cucsVnicScsiEquipmentDn,'cucsVnicScsiIdentPoolName':cucsVnicScsiIdentPoolName,'cucsVnicScsiInstType':cucsVnicScsiInstType,'cucsVnicScsiName':cucsVnicScsiName,'cucsVnicScsiNwTemplName':cucsVnicScsiNwTemplName,'cucsVnicScsiOperOrder':cucsVnicScsiOperOrder,'cucsVnicScsiOperSpeed':cucsVnicScsiOperSpeed,'cucsVnicScsiOperStatsPolicyName':cucsVnicScsiOperStatsPolicyName,'cucsVnicScsiOperVcon':cucsVnicScsiOperVcon,'cucsVnicScsiOrder':cucsVnicScsiOrder,'cucsVnicScsiOwner':cucsVnicScsiOwner,'cucsVnicScsiPinToGroupName':cucsVnicScsiPinToGroupName,'cucsVnicScsiQosPolicyName':cucsVnicScsiQosPolicyName,'cucsVnicScsiStatsPolicyName':cucsVnicScsiStatsPolicyName,'cucsVnicScsiSwitchId':cucsVnicScsiSwitchId,'cucsVnicScsiType':cucsVnicScsiType,'cucsVnicScsiConfigQualifier':cucsVnicScsiConfigQualifier,'cucsVnicScsiAdminHostPort':cucsVnicScsiAdminHostPort,'cucsVnicScsiOperHostPort':cucsVnicScsiOperHostPort,'cucsVnicScsiAdminCdnName':cucsVnicScsiAdminCdnName,'cucsVnicScsiOperCdnName':cucsVnicScsiOperCdnName,'cucsVnicScsiCdnPropInSync':cucsVnicScsiCdnPropInSync,'cucsVnicScsiCdnSource':cucsVnicScsiCdnSource,'cucsVnicScsiRedundancyPairType':cucsVnicScsiRedundancyPairType,'cucsVnicScsiRedundancyPeer':cucsVnicScsiRedundancyPeer,'cucsVnicScsiIfTable':cucsVnicScsiIfTable,'cucsVnicScsiIfEntry':cucsVnicScsiIfEntry,_l:cucsVnicScsiIfInstanceId,'cucsVnicScsiIfDn':cucsVnicScsiIfDn,'cucsVnicScsiIfRn':cucsVnicScsiIfRn,'cucsVnicScsiIfAddr':cucsVnicScsiIfAddr,'cucsVnicScsiIfName':cucsVnicScsiIfName,'cucsVnicScsiIfOperState':cucsVnicScsiIfOperState,'cucsVnicScsiIfOwner':cucsVnicScsiIfOwner,'cucsVnicScsiIfSwitchId':cucsVnicScsiIfSwitchId,'cucsVnicScsiIfType':cucsVnicScsiIfType,'cucsVnicScsiIfVnet':cucsVnicScsiIfVnet,'cucsVnicScsiIfConfigQualifier':cucsVnicScsiIfConfigQualifier,'cucsVnicScsiIfOperVnetDn':cucsVnicScsiIfOperVnetDn,'cucsVnicScsiIfOperVnetName':cucsVnicScsiIfOperVnetName,'cucsVnicScsiIfPubNwId':cucsVnicScsiIfPubNwId,'cucsVnicScsiIfSharing':cucsVnicScsiIfSharing,'cucsVnicScsiIfOperPrimaryVnetDn':cucsVnicScsiIfOperPrimaryVnetDn,'cucsVnicScsiIfOperPrimaryVnetName':cucsVnicScsiIfOperPrimaryVnetName,'cucsVnicBootIpPolicyTable':cucsVnicBootIpPolicyTable,'cucsVnicBootIpPolicyEntry':cucsVnicBootIpPolicyEntry,_m:cucsVnicBootIpPolicyInstanceId,'cucsVnicBootIpPolicyDn':cucsVnicBootIpPolicyDn,'cucsVnicBootIpPolicyRn':cucsVnicBootIpPolicyRn,'cucsVnicBootIpPolicyDescr':cucsVnicBootIpPolicyDescr,'cucsVnicBootIpPolicyIntId':cucsVnicBootIpPolicyIntId,'cucsVnicBootIpPolicyName':cucsVnicBootIpPolicyName,'cucsVnicBootIpPolicyPoolName':cucsVnicBootIpPolicyPoolName,'cucsVnicBootIpPolicyPolicyLevel':cucsVnicBootIpPolicyPolicyLevel,'cucsVnicBootIpPolicyPolicyOwner':cucsVnicBootIpPolicyPolicyOwner,'cucsVnicIPv4IscsiAddrTable':cucsVnicIPv4IscsiAddrTable,'cucsVnicIPv4IscsiAddrEntry':cucsVnicIPv4IscsiAddrEntry,_n:cucsVnicIPv4IscsiAddrInstanceId,'cucsVnicIPv4IscsiAddrDn':cucsVnicIPv4IscsiAddrDn,'cucsVnicIPv4IscsiAddrRn':cucsVnicIPv4IscsiAddrRn,'cucsVnicIPv4IscsiAddrAddr':cucsVnicIPv4IscsiAddrAddr,'cucsVnicIPv4IscsiAddrDefGw':cucsVnicIPv4IscsiAddrDefGw,'cucsVnicIPv4IscsiAddrPrimDns':cucsVnicIPv4IscsiAddrPrimDns,'cucsVnicIPv4IscsiAddrSecDns':cucsVnicIPv4IscsiAddrSecDns,'cucsVnicIPv4IscsiAddrSubnet':cucsVnicIPv4IscsiAddrSubnet,'cucsVnicIPv4PooledIscsiAddrTable':cucsVnicIPv4PooledIscsiAddrTable,'cucsVnicIPv4PooledIscsiAddrEntry':cucsVnicIPv4PooledIscsiAddrEntry,_o:cucsVnicIPv4PooledIscsiAddrInstanceId,'cucsVnicIPv4PooledIscsiAddrDn':cucsVnicIPv4PooledIscsiAddrDn,'cucsVnicIPv4PooledIscsiAddrRn':cucsVnicIPv4PooledIscsiAddrRn,'cucsVnicIPv4PooledIscsiAddrAddr':cucsVnicIPv4PooledIscsiAddrAddr,'cucsVnicIPv4PooledIscsiAddrDefGw':cucsVnicIPv4PooledIscsiAddrDefGw,'cucsVnicIPv4PooledIscsiAddrIdentPoolName':cucsVnicIPv4PooledIscsiAddrIdentPoolName,'cucsVnicIPv4PooledIscsiAddrOperIdentPoolName':cucsVnicIPv4PooledIscsiAddrOperIdentPoolName,'cucsVnicIPv4PooledIscsiAddrPrimDns':cucsVnicIPv4PooledIscsiAddrPrimDns,'cucsVnicIPv4PooledIscsiAddrSecDns':cucsVnicIPv4PooledIscsiAddrSecDns,'cucsVnicIPv4PooledIscsiAddrSubnet':cucsVnicIPv4PooledIscsiAddrSubnet,'cucsVnicIScsiTable':cucsVnicIScsiTable,'cucsVnicIScsiEntry':cucsVnicIScsiEntry,_p:cucsVnicIScsiInstanceId,'cucsVnicIScsiDn':cucsVnicIScsiDn,'cucsVnicIScsiRn':cucsVnicIScsiRn,'cucsVnicIScsiAdaptorProfileName':cucsVnicIScsiAdaptorProfileName,'cucsVnicIScsiAddr':cucsVnicIScsiAddr,'cucsVnicIScsiAdminVcon':cucsVnicIScsiAdminVcon,'cucsVnicIScsiAuthProfileName':cucsVnicIScsiAuthProfileName,'cucsVnicIScsiBootDev':cucsVnicIScsiBootDev,'cucsVnicIScsiConfigState':cucsVnicIScsiConfigState,'cucsVnicIScsiEquipmentDn':cucsVnicIScsiEquipmentDn,'cucsVnicIScsiEthEpDn':cucsVnicIScsiEthEpDn,'cucsVnicIScsiExtIPState':cucsVnicIScsiExtIPState,'cucsVnicIScsiFltAggr':cucsVnicIScsiFltAggr,'cucsVnicIScsiIdentPoolName':cucsVnicIScsiIdentPoolName,'cucsVnicIScsiInitiatorName':cucsVnicIScsiInitiatorName,'cucsVnicIScsiInstType':cucsVnicIScsiInstType,'cucsVnicIScsiIqnIdentPoolName':cucsVnicIScsiIqnIdentPoolName,'cucsVnicIScsiName':cucsVnicIScsiName,'cucsVnicIScsiNwTemplName':cucsVnicIScsiNwTemplName,'cucsVnicIScsiOperAdaptorProfileName':cucsVnicIScsiOperAdaptorProfileName,'cucsVnicIScsiOperAuthProfileName':cucsVnicIScsiOperAuthProfileName,'cucsVnicIScsiOperIqnIdentPoolName':cucsVnicIScsiOperIqnIdentPoolName,'cucsVnicIScsiOperOrder':cucsVnicIScsiOperOrder,'cucsVnicIScsiOperSpeed':cucsVnicIScsiOperSpeed,'cucsVnicIScsiOperStatsPolicyName':cucsVnicIScsiOperStatsPolicyName,'cucsVnicIScsiOperVcon':cucsVnicIScsiOperVcon,'cucsVnicIScsiOrder':cucsVnicIScsiOrder,'cucsVnicIScsiOwner':cucsVnicIScsiOwner,'cucsVnicIScsiPinToGroupName':cucsVnicIScsiPinToGroupName,'cucsVnicIScsiQosPolicyName':cucsVnicIScsiQosPolicyName,'cucsVnicIScsiStatsPolicyName':cucsVnicIScsiStatsPolicyName,'cucsVnicIScsiSwitchId':cucsVnicIScsiSwitchId,'cucsVnicIScsiType':cucsVnicIScsiType,'cucsVnicIScsiVnicDefType':cucsVnicIScsiVnicDefType,'cucsVnicIScsiVnicName':cucsVnicIScsiVnicName,'cucsVnicIScsiConfigQualifier':cucsVnicIScsiConfigQualifier,'cucsVnicIScsiInitNameSuffix':cucsVnicIScsiInitNameSuffix,'cucsVnicIScsiOperIdentPoolName':cucsVnicIScsiOperIdentPoolName,'cucsVnicIScsiAdminHostPort':cucsVnicIScsiAdminHostPort,'cucsVnicIScsiOperHostPort':cucsVnicIScsiOperHostPort,'cucsVnicIScsiPropAcl':cucsVnicIScsiPropAcl,'cucsVnicIScsiAdminCdnName':cucsVnicIScsiAdminCdnName,'cucsVnicIScsiOperCdnName':cucsVnicIScsiOperCdnName,'cucsVnicIScsiCdnSource':cucsVnicIScsiCdnSource,'cucsVnicIScsiCdnPropInSync':cucsVnicIScsiCdnPropInSync,'cucsVnicIScsiRedundancyPairType':cucsVnicIScsiRedundancyPairType,'cucsVnicIScsiRedundancyPeer':cucsVnicIScsiRedundancyPeer,'cucsVnicIScsiAutoTargetIfTable':cucsVnicIScsiAutoTargetIfTable,'cucsVnicIScsiAutoTargetIfEntry':cucsVnicIScsiAutoTargetIfEntry,_q:cucsVnicIScsiAutoTargetIfInstanceId,'cucsVnicIScsiAutoTargetIfDn':cucsVnicIScsiAutoTargetIfDn,'cucsVnicIScsiAutoTargetIfRn':cucsVnicIScsiAutoTargetIfRn,'cucsVnicIScsiAutoTargetIfDhcpVendorId':cucsVnicIScsiAutoTargetIfDhcpVendorId,'cucsVnicIScsiNodeTable':cucsVnicIScsiNodeTable,'cucsVnicIScsiNodeEntry':cucsVnicIScsiNodeEntry,_r:cucsVnicIScsiNodeInstanceId,'cucsVnicIScsiNodeDn':cucsVnicIScsiNodeDn,'cucsVnicIScsiNodeRn':cucsVnicIScsiNodeRn,'cucsVnicIScsiNodeFltAggr':cucsVnicIScsiNodeFltAggr,'cucsVnicIScsiNodeInitiatorName':cucsVnicIScsiNodeInitiatorName,'cucsVnicIScsiNodeOwner':cucsVnicIScsiNodeOwner,'cucsVnicIScsiNodeInitNameSuffix':cucsVnicIScsiNodeInitNameSuffix,'cucsVnicIScsiNodeIqnIdentPoolName':cucsVnicIScsiNodeIqnIdentPoolName,'cucsVnicIScsiNodeOperIqnIdentPoolName':cucsVnicIScsiNodeOperIqnIdentPoolName,'cucsVnicIScsiNodeInitiatorPolicyName':cucsVnicIScsiNodeInitiatorPolicyName,'cucsVnicIScsiNodeOperInitiatorPolicyName':cucsVnicIScsiNodeOperInitiatorPolicyName,'cucsVnicIScsiNodePropAcl':cucsVnicIScsiNodePropAcl,'cucsVnicIScsiStaticTargetIfTable':cucsVnicIScsiStaticTargetIfTable,'cucsVnicIScsiStaticTargetIfEntry':cucsVnicIScsiStaticTargetIfEntry,_s:cucsVnicIScsiStaticTargetIfInstanceId,'cucsVnicIScsiStaticTargetIfDn':cucsVnicIScsiStaticTargetIfDn,'cucsVnicIScsiStaticTargetIfRn':cucsVnicIScsiStaticTargetIfRn,'cucsVnicIScsiStaticTargetIfAuthProfileName':cucsVnicIScsiStaticTargetIfAuthProfileName,'cucsVnicIScsiStaticTargetIfIpAddress':cucsVnicIScsiStaticTargetIfIpAddress,'cucsVnicIScsiStaticTargetIfName':cucsVnicIScsiStaticTargetIfName,'cucsVnicIScsiStaticTargetIfOperAuthProfileName':cucsVnicIScsiStaticTargetIfOperAuthProfileName,'cucsVnicIScsiStaticTargetIfPort':cucsVnicIScsiStaticTargetIfPort,'cucsVnicIScsiStaticTargetIfPriority':cucsVnicIScsiStaticTargetIfPriority,'cucsVnicIScsiStaticTargetIfPropAcl':cucsVnicIScsiStaticTargetIfPropAcl,'cucsVnicInternalProfileTable':cucsVnicInternalProfileTable,'cucsVnicInternalProfileEntry':cucsVnicInternalProfileEntry,_t:cucsVnicInternalProfileInstanceId,'cucsVnicInternalProfileDn':cucsVnicInternalProfileDn,'cucsVnicInternalProfileRn':cucsVnicInternalProfileRn,'cucsVnicInternalProfileDescr':cucsVnicInternalProfileDescr,'cucsVnicInternalProfileIntId':cucsVnicInternalProfileIntId,'cucsVnicInternalProfileMaxPorts':cucsVnicInternalProfileMaxPorts,'cucsVnicInternalProfileName':cucsVnicInternalProfileName,'cucsVnicInternalProfilePolicyLevel':cucsVnicInternalProfilePolicyLevel,'cucsVnicInternalProfilePolicyOwner':cucsVnicInternalProfilePolicyOwner,'cucsVnicLunTable':cucsVnicLunTable,'cucsVnicLunEntry':cucsVnicLunEntry,_u:cucsVnicLunInstanceId,'cucsVnicLunDn':cucsVnicLunDn,'cucsVnicLunRn':cucsVnicLunRn,'cucsVnicLunBootable':cucsVnicLunBootable,'cucsVnicLunId':cucsVnicLunId,'cucsVnicOProfileAliasTable':cucsVnicOProfileAliasTable,'cucsVnicOProfileAliasEntry':cucsVnicOProfileAliasEntry,_v:cucsVnicOProfileAliasInstanceId,'cucsVnicOProfileAliasDn':cucsVnicOProfileAliasDn,'cucsVnicOProfileAliasRn':cucsVnicOProfileAliasRn,'cucsVnicOProfileAliasAlias':cucsVnicOProfileAliasAlias,'cucsVnicOProfileAliasMgmtPlane':cucsVnicOProfileAliasMgmtPlane,'cucsVnicOProfileAliasVSwitchId':cucsVnicOProfileAliasVSwitchId,'cucsVnicOProfileAliasVSwitchName':cucsVnicOProfileAliasVSwitchName,'cucsVnicVlanTable':cucsVnicVlanTable,'cucsVnicVlanEntry':cucsVnicVlanEntry,_w:cucsVnicVlanInstanceId,'cucsVnicVlanDn':cucsVnicVlanDn,'cucsVnicVlanRn':cucsVnicVlanRn,'cucsVnicVlanFltAggr':cucsVnicVlanFltAggr,'cucsVnicVlanName':cucsVnicVlanName,'cucsVnicVlanOperState':cucsVnicVlanOperState,'cucsVnicVlanOwner':cucsVnicVlanOwner,'cucsVnicVlanSwitchId':cucsVnicVlanSwitchId,'cucsVnicVlanType':cucsVnicVlanType,'cucsVnicVlanVlanName':cucsVnicVlanVlanName,'cucsVnicVlanVnet':cucsVnicVlanVnet,'cucsVnicVlanConfigQualifier':cucsVnicVlanConfigQualifier,'cucsVnicVlanOperVnetDn':cucsVnicVlanOperVnetDn,'cucsVnicVlanOperVnetName':cucsVnicVlanOperVnetName,'cucsVnicVlanPubNwId':cucsVnicVlanPubNwId,'cucsVnicVlanSharing':cucsVnicVlanSharing,'cucsVnicVlanOperPrimaryVnetDn':cucsVnicVlanOperPrimaryVnetDn,'cucsVnicVlanOperPrimaryVnetName':cucsVnicVlanOperPrimaryVnetName,'cucsVnicConnDefTable':cucsVnicConnDefTable,'cucsVnicConnDefEntry':cucsVnicConnDefEntry,_x:cucsVnicConnDefInstanceId,'cucsVnicConnDefDn':cucsVnicConnDefDn,'cucsVnicConnDefRn':cucsVnicConnDefRn,'cucsVnicConnDefFltAggr':cucsVnicConnDefFltAggr,'cucsVnicConnDefLanConnPolicyName':cucsVnicConnDefLanConnPolicyName,'cucsVnicConnDefOperLanConnPolicyName':cucsVnicConnDefOperLanConnPolicyName,'cucsVnicConnDefOperSanConnPolicyName':cucsVnicConnDefOperSanConnPolicyName,'cucsVnicConnDefSanConnPolicyName':cucsVnicConnDefSanConnPolicyName,'cucsVnicConnDefPropAcl':cucsVnicConnDefPropAcl,'cucsVnicDynamicConPolicyRefTable':cucsVnicDynamicConPolicyRefTable,'cucsVnicDynamicConPolicyRefEntry':cucsVnicDynamicConPolicyRefEntry,_y:cucsVnicDynamicConPolicyRefInstanceId,'cucsVnicDynamicConPolicyRefDn':cucsVnicDynamicConPolicyRefDn,'cucsVnicDynamicConPolicyRefRn':cucsVnicDynamicConPolicyRefRn,'cucsVnicDynamicConPolicyRefConPolicyName':cucsVnicDynamicConPolicyRefConPolicyName,'cucsVnicDynamicConPolicyRefOperConPolicyName':cucsVnicDynamicConPolicyRefOperConPolicyName,'cucsVnicFcGroupDefTable':cucsVnicFcGroupDefTable,'cucsVnicFcGroupDefEntry':cucsVnicFcGroupDefEntry,_z:cucsVnicFcGroupDefInstanceId,'cucsVnicFcGroupDefDn':cucsVnicFcGroupDefDn,'cucsVnicFcGroupDefRn':cucsVnicFcGroupDefRn,'cucsVnicFcGroupDefAdaptorProfileName':cucsVnicFcGroupDefAdaptorProfileName,'cucsVnicFcGroupDefDescr':cucsVnicFcGroupDefDescr,'cucsVnicFcGroupDefIdentPoolName':cucsVnicFcGroupDefIdentPoolName,'cucsVnicFcGroupDefIntId':cucsVnicFcGroupDefIntId,'cucsVnicFcGroupDefMaxDataFieldSize':cucsVnicFcGroupDefMaxDataFieldSize,'cucsVnicFcGroupDefName':cucsVnicFcGroupDefName,'cucsVnicFcGroupDefNwTemplName':cucsVnicFcGroupDefNwTemplName,'cucsVnicFcGroupDefOperStatsPolicyName':cucsVnicFcGroupDefOperStatsPolicyName,'cucsVnicFcGroupDefOperStorageConnPolicyName':cucsVnicFcGroupDefOperStorageConnPolicyName,'cucsVnicFcGroupDefPolicyLevel':cucsVnicFcGroupDefPolicyLevel,'cucsVnicFcGroupDefPolicyOwner':cucsVnicFcGroupDefPolicyOwner,'cucsVnicFcGroupDefQosPolicyName':cucsVnicFcGroupDefQosPolicyName,'cucsVnicFcGroupDefStatsPolicyName':cucsVnicFcGroupDefStatsPolicyName,'cucsVnicFcGroupDefStorageConnPolicyName':cucsVnicFcGroupDefStorageConnPolicyName,'cucsVnicFcGroupTemplTable':cucsVnicFcGroupTemplTable,'cucsVnicFcGroupTemplEntry':cucsVnicFcGroupTemplEntry,_A0:cucsVnicFcGroupTemplInstanceId,'cucsVnicFcGroupTemplDn':cucsVnicFcGroupTemplDn,'cucsVnicFcGroupTemplRn':cucsVnicFcGroupTemplRn,'cucsVnicFcGroupTemplAdaptorProfileName':cucsVnicFcGroupTemplAdaptorProfileName,'cucsVnicFcGroupTemplDescr':cucsVnicFcGroupTemplDescr,'cucsVnicFcGroupTemplIdentPoolName':cucsVnicFcGroupTemplIdentPoolName,'cucsVnicFcGroupTemplIntId':cucsVnicFcGroupTemplIntId,'cucsVnicFcGroupTemplMaxDataFieldSize':cucsVnicFcGroupTemplMaxDataFieldSize,'cucsVnicFcGroupTemplName':cucsVnicFcGroupTemplName,'cucsVnicFcGroupTemplNwTemplName':cucsVnicFcGroupTemplNwTemplName,'cucsVnicFcGroupTemplOperStatsPolicyName':cucsVnicFcGroupTemplOperStatsPolicyName,'cucsVnicFcGroupTemplOperStorageConnPolicyName':cucsVnicFcGroupTemplOperStorageConnPolicyName,'cucsVnicFcGroupTemplPolicyLevel':cucsVnicFcGroupTemplPolicyLevel,'cucsVnicFcGroupTemplPolicyOwner':cucsVnicFcGroupTemplPolicyOwner,'cucsVnicFcGroupTemplQosPolicyName':cucsVnicFcGroupTemplQosPolicyName,'cucsVnicFcGroupTemplStatsPolicyName':cucsVnicFcGroupTemplStatsPolicyName,'cucsVnicFcGroupTemplStorageConnPolicyName':cucsVnicFcGroupTemplStorageConnPolicyName,'cucsVnicFcGroupTemplTemplType':cucsVnicFcGroupTemplTemplType,'cucsVnicFcGroupTemplRedundancyPairType':cucsVnicFcGroupTemplRedundancyPairType,'cucsVnicIScsiBootParamsTable':cucsVnicIScsiBootParamsTable,'cucsVnicIScsiBootParamsEntry':cucsVnicIScsiBootParamsEntry,_A1:cucsVnicIScsiBootParamsInstanceId,'cucsVnicIScsiBootParamsDn':cucsVnicIScsiBootParamsDn,'cucsVnicIScsiBootParamsRn':cucsVnicIScsiBootParamsRn,'cucsVnicIScsiBootParamsDescr':cucsVnicIScsiBootParamsDescr,'cucsVnicIScsiBootParamsIntId':cucsVnicIScsiBootParamsIntId,'cucsVnicIScsiBootParamsName':cucsVnicIScsiBootParamsName,'cucsVnicIScsiBootParamsPolicyLevel':cucsVnicIScsiBootParamsPolicyLevel,'cucsVnicIScsiBootParamsPolicyOwner':cucsVnicIScsiBootParamsPolicyOwner,'cucsVnicIScsiBootParamsOwner':cucsVnicIScsiBootParamsOwner,'cucsVnicIScsiBootParamsPropAcl':cucsVnicIScsiBootParamsPropAcl,'cucsVnicIScsiBootVnicTable':cucsVnicIScsiBootVnicTable,'cucsVnicIScsiBootVnicEntry':cucsVnicIScsiBootVnicEntry,_A2:cucsVnicIScsiBootVnicInstanceId,'cucsVnicIScsiBootVnicDn':cucsVnicIScsiBootVnicDn,'cucsVnicIScsiBootVnicRn':cucsVnicIScsiBootVnicRn,'cucsVnicIScsiBootVnicAuthProfileName':cucsVnicIScsiBootVnicAuthProfileName,'cucsVnicIScsiBootVnicDescr':cucsVnicIScsiBootVnicDescr,'cucsVnicIScsiBootVnicInitiatorName':cucsVnicIScsiBootVnicInitiatorName,'cucsVnicIScsiBootVnicIntId':cucsVnicIScsiBootVnicIntId,'cucsVnicIScsiBootVnicIqnIdentPoolName':cucsVnicIScsiBootVnicIqnIdentPoolName,'cucsVnicIScsiBootVnicName':cucsVnicIScsiBootVnicName,'cucsVnicIScsiBootVnicOperAuthProfileName':cucsVnicIScsiBootVnicOperAuthProfileName,'cucsVnicIScsiBootVnicOperIqnIdentPoolName':cucsVnicIScsiBootVnicOperIqnIdentPoolName,'cucsVnicIScsiBootVnicPolicyLevel':cucsVnicIScsiBootVnicPolicyLevel,'cucsVnicIScsiBootVnicPolicyOwner':cucsVnicIScsiBootVnicPolicyOwner,'cucsVnicIScsiLCPTable':cucsVnicIScsiLCPTable,'cucsVnicIScsiLCPEntry':cucsVnicIScsiLCPEntry,_A3:cucsVnicIScsiLCPInstanceId,'cucsVnicIScsiLCPDn':cucsVnicIScsiLCPDn,'cucsVnicIScsiLCPRn':cucsVnicIScsiLCPRn,'cucsVnicIScsiLCPAdaptorProfileName':cucsVnicIScsiLCPAdaptorProfileName,'cucsVnicIScsiLCPAddr':cucsVnicIScsiLCPAddr,'cucsVnicIScsiLCPAdminVcon':cucsVnicIScsiLCPAdminVcon,'cucsVnicIScsiLCPBootDev':cucsVnicIScsiLCPBootDev,'cucsVnicIScsiLCPConfigQualifier':cucsVnicIScsiLCPConfigQualifier,'cucsVnicIScsiLCPConfigState':cucsVnicIScsiLCPConfigState,'cucsVnicIScsiLCPEquipmentDn':cucsVnicIScsiLCPEquipmentDn,'cucsVnicIScsiLCPFltAggr':cucsVnicIScsiLCPFltAggr,'cucsVnicIScsiLCPIdentPoolName':cucsVnicIScsiLCPIdentPoolName,'cucsVnicIScsiLCPInstType':cucsVnicIScsiLCPInstType,'cucsVnicIScsiLCPName':cucsVnicIScsiLCPName,'cucsVnicIScsiLCPNwTemplName':cucsVnicIScsiLCPNwTemplName,'cucsVnicIScsiLCPOperAdaptorProfileName':cucsVnicIScsiLCPOperAdaptorProfileName,'cucsVnicIScsiLCPOperIdentPoolName':cucsVnicIScsiLCPOperIdentPoolName,'cucsVnicIScsiLCPOperOrder':cucsVnicIScsiLCPOperOrder,'cucsVnicIScsiLCPOperSpeed':cucsVnicIScsiLCPOperSpeed,'cucsVnicIScsiLCPOperStatsPolicyName':cucsVnicIScsiLCPOperStatsPolicyName,'cucsVnicIScsiLCPOperVcon':cucsVnicIScsiLCPOperVcon,'cucsVnicIScsiLCPOrder':cucsVnicIScsiLCPOrder,'cucsVnicIScsiLCPOwner':cucsVnicIScsiLCPOwner,'cucsVnicIScsiLCPPinToGroupName':cucsVnicIScsiLCPPinToGroupName,'cucsVnicIScsiLCPQosPolicyName':cucsVnicIScsiLCPQosPolicyName,'cucsVnicIScsiLCPStatsPolicyName':cucsVnicIScsiLCPStatsPolicyName,'cucsVnicIScsiLCPSwitchId':cucsVnicIScsiLCPSwitchId,'cucsVnicIScsiLCPType':cucsVnicIScsiLCPType,'cucsVnicIScsiLCPVnicName':cucsVnicIScsiLCPVnicName,'cucsVnicIScsiLCPAdminHostPort':cucsVnicIScsiLCPAdminHostPort,'cucsVnicIScsiLCPOperHostPort':cucsVnicIScsiLCPOperHostPort,'cucsVnicIScsiLCPAdminCdnName':cucsVnicIScsiLCPAdminCdnName,'cucsVnicIScsiLCPOperCdnName':cucsVnicIScsiLCPOperCdnName,'cucsVnicIScsiLCPCdnSource':cucsVnicIScsiLCPCdnSource,'cucsVnicIScsiLCPCdnPropInSync':cucsVnicIScsiLCPCdnPropInSync,'cucsVnicIScsiLCPRedundancyPairType':cucsVnicIScsiLCPRedundancyPairType,'cucsVnicIScsiLCPRedundancyPeer':cucsVnicIScsiLCPRedundancyPeer,'cucsVnicLanConnPolicyTable':cucsVnicLanConnPolicyTable,'cucsVnicLanConnPolicyEntry':cucsVnicLanConnPolicyEntry,_A4:cucsVnicLanConnPolicyInstanceId,'cucsVnicLanConnPolicyDn':cucsVnicLanConnPolicyDn,'cucsVnicLanConnPolicyRn':cucsVnicLanConnPolicyRn,'cucsVnicLanConnPolicyDescr':cucsVnicLanConnPolicyDescr,'cucsVnicLanConnPolicyFltAggr':cucsVnicLanConnPolicyFltAggr,'cucsVnicLanConnPolicyIntId':cucsVnicLanConnPolicyIntId,'cucsVnicLanConnPolicyName':cucsVnicLanConnPolicyName,'cucsVnicLanConnPolicyPolicyLevel':cucsVnicLanConnPolicyPolicyLevel,'cucsVnicLanConnPolicyPolicyOwner':cucsVnicLanConnPolicyPolicyOwner,'cucsVnicProfileSetFsmTable':cucsVnicProfileSetFsmTable,'cucsVnicProfileSetFsmEntry':cucsVnicProfileSetFsmEntry,_A5:cucsVnicProfileSetFsmInstanceId,'cucsVnicProfileSetFsmDn':cucsVnicProfileSetFsmDn,'cucsVnicProfileSetFsmRn':cucsVnicProfileSetFsmRn,'cucsVnicProfileSetFsmCompletionTime':cucsVnicProfileSetFsmCompletionTime,'cucsVnicProfileSetFsmCurrentFsm':cucsVnicProfileSetFsmCurrentFsm,'cucsVnicProfileSetFsmDescrData':cucsVnicProfileSetFsmDescrData,'cucsVnicProfileSetFsmFsmStatus':cucsVnicProfileSetFsmFsmStatus,'cucsVnicProfileSetFsmProgress':cucsVnicProfileSetFsmProgress,'cucsVnicProfileSetFsmRmtErrCode':cucsVnicProfileSetFsmRmtErrCode,'cucsVnicProfileSetFsmRmtErrDescr':cucsVnicProfileSetFsmRmtErrDescr,'cucsVnicProfileSetFsmRmtRslt':cucsVnicProfileSetFsmRmtRslt,'cucsVnicProfileSetFsmStageTable':cucsVnicProfileSetFsmStageTable,'cucsVnicProfileSetFsmStageEntry':cucsVnicProfileSetFsmStageEntry,_A6:cucsVnicProfileSetFsmStageInstanceId,'cucsVnicProfileSetFsmStageDn':cucsVnicProfileSetFsmStageDn,'cucsVnicProfileSetFsmStageRn':cucsVnicProfileSetFsmStageRn,'cucsVnicProfileSetFsmStageDescrData':cucsVnicProfileSetFsmStageDescrData,'cucsVnicProfileSetFsmStageLastUpdateTime':cucsVnicProfileSetFsmStageLastUpdateTime,'cucsVnicProfileSetFsmStageName':cucsVnicProfileSetFsmStageName,'cucsVnicProfileSetFsmStageOrder':cucsVnicProfileSetFsmStageOrder,'cucsVnicProfileSetFsmStageRetry':cucsVnicProfileSetFsmStageRetry,'cucsVnicProfileSetFsmStageStageStatus':cucsVnicProfileSetFsmStageStageStatus,'cucsVnicRackServerDiscoveryProfileTable':cucsVnicRackServerDiscoveryProfileTable,'cucsVnicRackServerDiscoveryProfileEntry':cucsVnicRackServerDiscoveryProfileEntry,_A7:cucsVnicRackServerDiscoveryProfileInstanceId,'cucsVnicRackServerDiscoveryProfileDn':cucsVnicRackServerDiscoveryProfileDn,'cucsVnicRackServerDiscoveryProfileRn':cucsVnicRackServerDiscoveryProfileRn,'cucsVnicRackServerDiscoveryProfileDescr':cucsVnicRackServerDiscoveryProfileDescr,'cucsVnicRackServerDiscoveryProfileIntId':cucsVnicRackServerDiscoveryProfileIntId,'cucsVnicRackServerDiscoveryProfileMaxPorts':cucsVnicRackServerDiscoveryProfileMaxPorts,'cucsVnicRackServerDiscoveryProfileName':cucsVnicRackServerDiscoveryProfileName,'cucsVnicRackServerDiscoveryProfilePolicyLevel':cucsVnicRackServerDiscoveryProfilePolicyLevel,'cucsVnicRackServerDiscoveryProfilePolicyOwner':cucsVnicRackServerDiscoveryProfilePolicyOwner,'cucsVnicSanConnPolicyTable':cucsVnicSanConnPolicyTable,'cucsVnicSanConnPolicyEntry':cucsVnicSanConnPolicyEntry,_A8:cucsVnicSanConnPolicyInstanceId,'cucsVnicSanConnPolicyDn':cucsVnicSanConnPolicyDn,'cucsVnicSanConnPolicyRn':cucsVnicSanConnPolicyRn,'cucsVnicSanConnPolicyDescr':cucsVnicSanConnPolicyDescr,'cucsVnicSanConnPolicyFltAggr':cucsVnicSanConnPolicyFltAggr,'cucsVnicSanConnPolicyIntId':cucsVnicSanConnPolicyIntId,'cucsVnicSanConnPolicyName':cucsVnicSanConnPolicyName,'cucsVnicSanConnPolicyPolicyLevel':cucsVnicSanConnPolicyPolicyLevel,'cucsVnicSanConnPolicyPolicyOwner':cucsVnicSanConnPolicyPolicyOwner,'cucsVnicVhbaBehPolicyTable':cucsVnicVhbaBehPolicyTable,'cucsVnicVhbaBehPolicyEntry':cucsVnicVhbaBehPolicyEntry,_A9:cucsVnicVhbaBehPolicyInstanceId,'cucsVnicVhbaBehPolicyDn':cucsVnicVhbaBehPolicyDn,'cucsVnicVhbaBehPolicyRn':cucsVnicVhbaBehPolicyRn,'cucsVnicVhbaBehPolicyAction':cucsVnicVhbaBehPolicyAction,'cucsVnicVhbaBehPolicyDescr':cucsVnicVhbaBehPolicyDescr,'cucsVnicVhbaBehPolicyIntId':cucsVnicVhbaBehPolicyIntId,'cucsVnicVhbaBehPolicyName':cucsVnicVhbaBehPolicyName,'cucsVnicVhbaBehPolicyNwTemplName':cucsVnicVhbaBehPolicyNwTemplName,'cucsVnicVhbaBehPolicyPolicyLevel':cucsVnicVhbaBehPolicyPolicyLevel,'cucsVnicVhbaBehPolicyPolicyOwner':cucsVnicVhbaBehPolicyPolicyOwner,'cucsVnicVhbaBehPolicyType':cucsVnicVhbaBehPolicyType,'cucsVnicVnicBehPolicyTable':cucsVnicVnicBehPolicyTable,'cucsVnicVnicBehPolicyEntry':cucsVnicVnicBehPolicyEntry,_AA:cucsVnicVnicBehPolicyInstanceId,'cucsVnicVnicBehPolicyDn':cucsVnicVnicBehPolicyDn,'cucsVnicVnicBehPolicyRn':cucsVnicVnicBehPolicyRn,'cucsVnicVnicBehPolicyAction':cucsVnicVnicBehPolicyAction,'cucsVnicVnicBehPolicyDescr':cucsVnicVnicBehPolicyDescr,'cucsVnicVnicBehPolicyIntId':cucsVnicVnicBehPolicyIntId,'cucsVnicVnicBehPolicyName':cucsVnicVnicBehPolicyName,'cucsVnicVnicBehPolicyNwTemplName':cucsVnicVnicBehPolicyNwTemplName,'cucsVnicVnicBehPolicyPolicyLevel':cucsVnicVnicBehPolicyPolicyLevel,'cucsVnicVnicBehPolicyPolicyOwner':cucsVnicVnicBehPolicyPolicyOwner,'cucsVnicVnicBehPolicyType':cucsVnicVnicBehPolicyType,'cucsVnicIpV4HistoryTable':cucsVnicIpV4HistoryTable,'cucsVnicIpV4HistoryEntry':cucsVnicIpV4HistoryEntry,_AB:cucsVnicIpV4HistoryInstanceId,'cucsVnicIpV4HistoryDn':cucsVnicIpV4HistoryDn,'cucsVnicIpV4HistoryRn':cucsVnicIpV4HistoryRn,'cucsVnicIpV4HistoryOldIpV4Addr':cucsVnicIpV4HistoryOldIpV4Addr,'cucsVnicIqnHistoryTable':cucsVnicIqnHistoryTable,'cucsVnicIqnHistoryEntry':cucsVnicIqnHistoryEntry,_AC:cucsVnicIqnHistoryInstanceId,'cucsVnicIqnHistoryDn':cucsVnicIqnHistoryDn,'cucsVnicIqnHistoryRn':cucsVnicIqnHistoryRn,'cucsVnicIqnHistoryOldInitiatorName':cucsVnicIqnHistoryOldInitiatorName,'cucsVnicMacHistoryTable':cucsVnicMacHistoryTable,'cucsVnicMacHistoryEntry':cucsVnicMacHistoryEntry,_AD:cucsVnicMacHistoryInstanceId,'cucsVnicMacHistoryDn':cucsVnicMacHistoryDn,'cucsVnicMacHistoryRn':cucsVnicMacHistoryRn,'cucsVnicMacHistoryOldaddr':cucsVnicMacHistoryOldaddr,'cucsVnicWwnnHistoryTable':cucsVnicWwnnHistoryTable,'cucsVnicWwnnHistoryEntry':cucsVnicWwnnHistoryEntry,_AE:cucsVnicWwnnHistoryInstanceId,'cucsVnicWwnnHistoryDn':cucsVnicWwnnHistoryDn,'cucsVnicWwnnHistoryRn':cucsVnicWwnnHistoryRn,'cucsVnicWwnnHistoryOldwwnn':cucsVnicWwnnHistoryOldwwnn,'cucsVnicWwpnHistoryTable':cucsVnicWwpnHistoryTable,'cucsVnicWwpnHistoryEntry':cucsVnicWwpnHistoryEntry,_AF:cucsVnicWwpnHistoryInstanceId,'cucsVnicWwpnHistoryDn':cucsVnicWwpnHistoryDn,'cucsVnicWwpnHistoryRn':cucsVnicWwpnHistoryRn,'cucsVnicWwpnHistoryOldaddr':cucsVnicWwpnHistoryOldaddr,'cucsVnicIpV4MgmtPooledAddrTable':cucsVnicIpV4MgmtPooledAddrTable,'cucsVnicIpV4MgmtPooledAddrEntry':cucsVnicIpV4MgmtPooledAddrEntry,_AG:cucsVnicIpV4MgmtPooledAddrInstanceId,'cucsVnicIpV4MgmtPooledAddrDn':cucsVnicIpV4MgmtPooledAddrDn,'cucsVnicIpV4MgmtPooledAddrRn':cucsVnicIpV4MgmtPooledAddrRn,'cucsVnicIpV4MgmtPooledAddrAddr':cucsVnicIpV4MgmtPooledAddrAddr,'cucsVnicIpV4MgmtPooledAddrDefGw':cucsVnicIpV4MgmtPooledAddrDefGw,'cucsVnicIpV4MgmtPooledAddrName':cucsVnicIpV4MgmtPooledAddrName,'cucsVnicIpV4MgmtPooledAddrOperName':cucsVnicIpV4MgmtPooledAddrOperName,'cucsVnicIpV4MgmtPooledAddrSubnet':cucsVnicIpV4MgmtPooledAddrSubnet,'cucsVnicIpV4MgmtPooledAddrPrimDns':cucsVnicIpV4MgmtPooledAddrPrimDns,'cucsVnicIpV4MgmtPooledAddrSecDns':cucsVnicIpV4MgmtPooledAddrSecDns,'cucsVnicIpV6MgmtPooledAddrTable':cucsVnicIpV6MgmtPooledAddrTable,'cucsVnicIpV6MgmtPooledAddrEntry':cucsVnicIpV6MgmtPooledAddrEntry,_AH:cucsVnicIpV6MgmtPooledAddrInstanceId,'cucsVnicIpV6MgmtPooledAddrDn':cucsVnicIpV6MgmtPooledAddrDn,'cucsVnicIpV6MgmtPooledAddrRn':cucsVnicIpV6MgmtPooledAddrRn,'cucsVnicIpV6MgmtPooledAddrAddr':cucsVnicIpV6MgmtPooledAddrAddr,'cucsVnicIpV6MgmtPooledAddrDefGw':cucsVnicIpV6MgmtPooledAddrDefGw,'cucsVnicIpV6MgmtPooledAddrName':cucsVnicIpV6MgmtPooledAddrName,'cucsVnicIpV6MgmtPooledAddrOperName':cucsVnicIpV6MgmtPooledAddrOperName,'cucsVnicIpV6MgmtPooledAddrPrefix':cucsVnicIpV6MgmtPooledAddrPrefix,'cucsVnicIpV6MgmtPooledAddrPrimDns':cucsVnicIpV6MgmtPooledAddrPrimDns,'cucsVnicIpV6MgmtPooledAddrSecDns':cucsVnicIpV6MgmtPooledAddrSecDns,'cucsVnicIpV6StaticAddrTable':cucsVnicIpV6StaticAddrTable,'cucsVnicIpV6StaticAddrEntry':cucsVnicIpV6StaticAddrEntry,_AI:cucsVnicIpV6StaticAddrInstanceId,'cucsVnicIpV6StaticAddrDn':cucsVnicIpV6StaticAddrDn,'cucsVnicIpV6StaticAddrRn':cucsVnicIpV6StaticAddrRn,'cucsVnicIpV6StaticAddrAddr':cucsVnicIpV6StaticAddrAddr,'cucsVnicIpV6StaticAddrDefGw':cucsVnicIpV6StaticAddrDefGw,'cucsVnicIpV6StaticAddrPrefix':cucsVnicIpV6StaticAddrPrefix,'cucsVnicIpV6StaticAddrPrimDns':cucsVnicIpV6StaticAddrPrimDns,'cucsVnicIpV6StaticAddrSecDns':cucsVnicIpV6StaticAddrSecDns,'cucsVnicProfileRefTable':cucsVnicProfileRefTable,'cucsVnicProfileRefEntry':cucsVnicProfileRefEntry,_AJ:cucsVnicProfileRefInstanceId,'cucsVnicProfileRefDn':cucsVnicProfileRefDn,'cucsVnicProfileRefRn':cucsVnicProfileRefRn,'cucsVnicProfileRefName':cucsVnicProfileRefName,'cucsVnicProfileRefSourceDn':cucsVnicProfileRefSourceDn,'cucsVnicUsnicConPolicyTable':cucsVnicUsnicConPolicyTable,'cucsVnicUsnicConPolicyEntry':cucsVnicUsnicConPolicyEntry,_AK:cucsVnicUsnicConPolicyInstanceId,'cucsVnicUsnicConPolicyDn':cucsVnicUsnicConPolicyDn,'cucsVnicUsnicConPolicyRn':cucsVnicUsnicConPolicyRn,'cucsVnicUsnicConPolicyAdaptorProfileName':cucsVnicUsnicConPolicyAdaptorProfileName,'cucsVnicUsnicConPolicyDescr':cucsVnicUsnicConPolicyDescr,'cucsVnicUsnicConPolicyIntId':cucsVnicUsnicConPolicyIntId,'cucsVnicUsnicConPolicyName':cucsVnicUsnicConPolicyName,'cucsVnicUsnicConPolicyPolicyLevel':cucsVnicUsnicConPolicyPolicyLevel,'cucsVnicUsnicConPolicyPolicyOwner':cucsVnicUsnicConPolicyPolicyOwner,'cucsVnicUsnicConPolicyUsnicCount':cucsVnicUsnicConPolicyUsnicCount,'cucsVnicUsnicConPolicyRefTable':cucsVnicUsnicConPolicyRefTable,'cucsVnicUsnicConPolicyRefEntry':cucsVnicUsnicConPolicyRefEntry,_AL:cucsVnicUsnicConPolicyRefInstanceId,'cucsVnicUsnicConPolicyRefDn':cucsVnicUsnicConPolicyRefDn,'cucsVnicUsnicConPolicyRefRn':cucsVnicUsnicConPolicyRefRn,'cucsVnicUsnicConPolicyRefConPolicyName':cucsVnicUsnicConPolicyRefConPolicyName,'cucsVnicUsnicConPolicyRefOperConPolicyName':cucsVnicUsnicConPolicyRefOperConPolicyName,'cucsVnicVmqConPolicyTable':cucsVnicVmqConPolicyTable,'cucsVnicVmqConPolicyEntry':cucsVnicVmqConPolicyEntry,_AM:cucsVnicVmqConPolicyInstanceId,'cucsVnicVmqConPolicyDn':cucsVnicVmqConPolicyDn,'cucsVnicVmqConPolicyRn':cucsVnicVmqConPolicyRn,'cucsVnicVmqConPolicyDescr':cucsVnicVmqConPolicyDescr,'cucsVnicVmqConPolicyIntId':cucsVnicVmqConPolicyIntId,'cucsVnicVmqConPolicyIntrCount':cucsVnicVmqConPolicyIntrCount,'cucsVnicVmqConPolicyName':cucsVnicVmqConPolicyName,'cucsVnicVmqConPolicyPolicyLevel':cucsVnicVmqConPolicyPolicyLevel,'cucsVnicVmqConPolicyPolicyOwner':cucsVnicVmqConPolicyPolicyOwner,'cucsVnicVmqConPolicyVmqCount':cucsVnicVmqConPolicyVmqCount,'cucsVnicVmqConPolicyRefTable':cucsVnicVmqConPolicyRefTable,'cucsVnicVmqConPolicyRefEntry':cucsVnicVmqConPolicyRefEntry,_AN:cucsVnicVmqConPolicyRefInstanceId,'cucsVnicVmqConPolicyRefDn':cucsVnicVmqConPolicyRefDn,'cucsVnicVmqConPolicyRefRn':cucsVnicVmqConPolicyRefRn,'cucsVnicVmqConPolicyRefConPolicyName':cucsVnicVmqConPolicyRefConPolicyName,'cucsVnicVmqConPolicyRefOperConPolicyName':cucsVnicVmqConPolicyRefOperConPolicyName,'cucsVnicIpV6HistoryTable':cucsVnicIpV6HistoryTable,'cucsVnicIpV6HistoryEntry':cucsVnicIpV6HistoryEntry,_AO:cucsVnicIpV6HistoryInstanceId,'cucsVnicIpV6HistoryDn':cucsVnicIpV6HistoryDn,'cucsVnicIpV6HistoryRn':cucsVnicIpV6HistoryRn,'cucsVnicIpV6HistoryOldIpV6Addr':cucsVnicIpV6HistoryOldIpV6Addr,'cucsVnicEthConfigTable':cucsVnicEthConfigTable,'cucsVnicEthConfigEntry':cucsVnicEthConfigEntry,_AP:cucsVnicEthConfigInstanceId,'cucsVnicEthConfigDn':cucsVnicEthConfigDn,'cucsVnicEthConfigRn':cucsVnicEthConfigRn,'cucsVnicEthConfigAdaptorProfileName':cucsVnicEthConfigAdaptorProfileName,'cucsVnicEthConfigMacPoolName':cucsVnicEthConfigMacPoolName,'cucsVnicEthConfigNwCtrlPolicyName':cucsVnicEthConfigNwCtrlPolicyName,'cucsVnicEthConfigOperAdaptorProfileName':cucsVnicEthConfigOperAdaptorProfileName,'cucsVnicEthConfigOperMacPoolName':cucsVnicEthConfigOperMacPoolName,'cucsVnicEthConfigOperNwCtrlPolicyName':cucsVnicEthConfigOperNwCtrlPolicyName,'cucsVnicEthConfigOperStatsPolicyName':cucsVnicEthConfigOperStatsPolicyName,'cucsVnicEthConfigStatsPolicyName':cucsVnicEthConfigStatsPolicyName,'cucsVnicIPv6IfTable':cucsVnicIPv6IfTable,'cucsVnicIPv6IfEntry':cucsVnicIPv6IfEntry,_AQ:cucsVnicIPv6IfInstanceId,'cucsVnicIPv6IfDn':cucsVnicIPv6IfDn,'cucsVnicIPv6IfRn':cucsVnicIPv6IfRn,'cucsVnicIPv6IfAddr':cucsVnicIPv6IfAddr,'cucsVnicIPv6IfConfigQualifier':cucsVnicIPv6IfConfigQualifier,'cucsVnicIPv6IfName':cucsVnicIPv6IfName,'cucsVnicIPv6IfOperState':cucsVnicIPv6IfOperState,'cucsVnicIPv6IfOperVnetDn':cucsVnicIPv6IfOperVnetDn,'cucsVnicIPv6IfOperVnetName':cucsVnicIPv6IfOperVnetName,'cucsVnicIPv6IfOwner':cucsVnicIPv6IfOwner,'cucsVnicIPv6IfPubNwId':cucsVnicIPv6IfPubNwId,'cucsVnicIPv6IfSharing':cucsVnicIPv6IfSharing,'cucsVnicIPv6IfSwitchId':cucsVnicIPv6IfSwitchId,'cucsVnicIPv6IfType':cucsVnicIPv6IfType,'cucsVnicIPv6IfVnet':cucsVnicIPv6IfVnet,'cucsVnicIPv6IfOperPrimaryVnetDn':cucsVnicIPv6IfOperPrimaryVnetDn,'cucsVnicIPv6IfOperPrimaryVnetName':cucsVnicIPv6IfOperPrimaryVnetName,'cucsVnicIScsiConfigTable':cucsVnicIScsiConfigTable,'cucsVnicIScsiConfigEntry':cucsVnicIScsiConfigEntry,_AR:cucsVnicIScsiConfigInstanceId,'cucsVnicIScsiConfigDn':cucsVnicIScsiConfigDn,'cucsVnicIScsiConfigRn':cucsVnicIScsiConfigRn,'cucsVnicIScsiConfigAdaptorProfileName':cucsVnicIScsiConfigAdaptorProfileName,'cucsVnicIScsiConfigIpPoolName':cucsVnicIScsiConfigIpPoolName,'cucsVnicIScsiConfigIpPoolNameFabricB':cucsVnicIScsiConfigIpPoolNameFabricB,'cucsVnicIScsiConfigIpPoolType':cucsVnicIScsiConfigIpPoolType,'cucsVnicIScsiConfigIqnPoolName':cucsVnicIScsiConfigIqnPoolName,'cucsVnicIScsiConfigOperAdaptorProfileName':cucsVnicIScsiConfigOperAdaptorProfileName,'cucsVnicIScsiConfigOperIpPoolName':cucsVnicIScsiConfigOperIpPoolName,'cucsVnicIScsiConfigOperIpPoolNameFabricB':cucsVnicIScsiConfigOperIpPoolNameFabricB,'cucsVnicIScsiConfigOperIqnPoolName':cucsVnicIScsiConfigOperIqnPoolName,'cucsVnicIScsiInitAutoConfigPolicyTable':cucsVnicIScsiInitAutoConfigPolicyTable,'cucsVnicIScsiInitAutoConfigPolicyEntry':cucsVnicIScsiInitAutoConfigPolicyEntry,_AS:cucsVnicIScsiInitAutoConfigPolicyInstanceId,'cucsVnicIScsiInitAutoConfigPolicyDn':cucsVnicIScsiInitAutoConfigPolicyDn,'cucsVnicIScsiInitAutoConfigPolicyRn':cucsVnicIScsiInitAutoConfigPolicyRn,'cucsVnicIScsiInitAutoConfigPolicyDescr':cucsVnicIScsiInitAutoConfigPolicyDescr,'cucsVnicIScsiInitAutoConfigPolicyFabricPath':cucsVnicIScsiInitAutoConfigPolicyFabricPath,'cucsVnicIScsiInitAutoConfigPolicyIntId':cucsVnicIScsiInitAutoConfigPolicyIntId,'cucsVnicIScsiInitAutoConfigPolicyName':cucsVnicIScsiInitAutoConfigPolicyName,'cucsVnicIScsiInitAutoConfigPolicyPolicyLevel':cucsVnicIScsiInitAutoConfigPolicyPolicyLevel,'cucsVnicIScsiInitAutoConfigPolicyPolicyOwner':cucsVnicIScsiInitAutoConfigPolicyPolicyOwner})