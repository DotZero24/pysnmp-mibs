_N='cfprPkiTpAutoImportInstanceId'
_M='cfprPkiImporterInstanceId'
_L='cfprPkiCertRevokeInstanceId'
_K='cfprPkiTPInstanceId'
_J='cfprPkiKeyRingInstanceId'
_I='cfprPkiEpFsmTaskInstanceId'
_H='cfprPkiEpFsmStageInstanceId'
_G='cfprPkiEpFsmInstanceId'
_F='cfprPkiEpInstanceId'
_E='cfprPkiCertReqInstanceId'
_D='not-accessible'
_C='CISCO-FIREPOWER-PKI-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
CfprManagedObjectDn,CfprManagedObjectId,ciscoFirepowerMIBObjects=mibBuilder.importSymbols('CISCO-FIREPOWER-MIB','CfprManagedObjectDn','CfprManagedObjectId','ciscoFirepowerMIBObjects')
CfprAaaConfigState,CfprConditionRemoteInvRslt,CfprFsmCompletion,CfprFsmFlags,CfprFsmFsmStageStatus,CfprPkiCertRevokeMethod,CfprPkiCertStatus,CfprPkiEc,CfprPkiEpFsmCurrentFsm,CfprPkiEpFsmStageName,CfprPkiEpFsmTaskItem,CfprPkiImportActivity,CfprPkiKeyringState,CfprPkiModulus,CfprPkiTpAutoImportImportControlStatus,CfprPkiTransferState,CfprPkiTransport,CfprPkiTransportNoLocal,CfprPkiType,CfprPolicyPolicyOwner=mibBuilder.importSymbols('CISCO-FIREPOWER-TC-MIB','CfprAaaConfigState','CfprConditionRemoteInvRslt','CfprFsmCompletion','CfprFsmFlags','CfprFsmFsmStageStatus','CfprPkiCertRevokeMethod','CfprPkiCertStatus','CfprPkiEc','CfprPkiEpFsmCurrentFsm','CfprPkiEpFsmStageName','CfprPkiEpFsmTaskItem','CfprPkiImportActivity','CfprPkiKeyringState','CfprPkiModulus','CfprPkiTpAutoImportImportControlStatus','CfprPkiTransferState','CfprPkiTransport','CfprPkiTransportNoLocal','CfprPkiType','CfprPolicyPolicyOwner')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CiscoAlarmSeverity,CiscoInetAddressMask,CiscoNetworkAddress,TimeIntervalSec,Unsigned64=mibBuilder.importSymbols('CISCO-TC','CiscoAlarmSeverity','CiscoInetAddressMask','CiscoNetworkAddress','TimeIntervalSec','Unsigned64')
InetAddressIPv4,InetAddressIPv6=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressIPv4','InetAddressIPv6')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowPointer,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowPointer','TextualConvention','TimeInterval','TimeStamp','TruthValue')
cfprPkiObjects=ModuleIdentity((1,3,6,1,4,1,9,9,826,1,61))
_CfprPkiCertReqTable_Object=MibTable
cfprPkiCertReqTable=_CfprPkiCertReqTable_Object((1,3,6,1,4,1,9,9,826,1,61,1))
if mibBuilder.loadTexts:cfprPkiCertReqTable.setStatus(_A)
_CfprPkiCertReqEntry_Object=MibTableRow
cfprPkiCertReqEntry=_CfprPkiCertReqEntry_Object((1,3,6,1,4,1,9,9,826,1,61,1,1))
cfprPkiCertReqEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:cfprPkiCertReqEntry.setStatus(_A)
_CfprPkiCertReqInstanceId_Type=CfprManagedObjectId
_CfprPkiCertReqInstanceId_Object=MibTableColumn
cfprPkiCertReqInstanceId=_CfprPkiCertReqInstanceId_Object((1,3,6,1,4,1,9,9,826,1,61,1,1,1),_CfprPkiCertReqInstanceId_Type())
cfprPkiCertReqInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprPkiCertReqInstanceId.setStatus(_A)
_CfprPkiCertReqDn_Type=CfprManagedObjectDn
_CfprPkiCertReqDn_Object=MibTableColumn
cfprPkiCertReqDn=_CfprPkiCertReqDn_Object((1,3,6,1,4,1,9,9,826,1,61,1,1,2),_CfprPkiCertReqDn_Type())
cfprPkiCertReqDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiCertReqDn.setStatus(_A)
_CfprPkiCertReqRn_Type=SnmpAdminString
_CfprPkiCertReqRn_Object=MibTableColumn
cfprPkiCertReqRn=_CfprPkiCertReqRn_Object((1,3,6,1,4,1,9,9,826,1,61,1,1,3),_CfprPkiCertReqRn_Type())
cfprPkiCertReqRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiCertReqRn.setStatus(_A)
_CfprPkiCertReqCountry_Type=SnmpAdminString
_CfprPkiCertReqCountry_Object=MibTableColumn
cfprPkiCertReqCountry=_CfprPkiCertReqCountry_Object((1,3,6,1,4,1,9,9,826,1,61,1,1,4),_CfprPkiCertReqCountry_Type())
cfprPkiCertReqCountry.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiCertReqCountry.setStatus(_A)
_CfprPkiCertReqDns_Type=SnmpAdminString
_CfprPkiCertReqDns_Object=MibTableColumn
cfprPkiCertReqDns=_CfprPkiCertReqDns_Object((1,3,6,1,4,1,9,9,826,1,61,1,1,5),_CfprPkiCertReqDns_Type())
cfprPkiCertReqDns.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiCertReqDns.setStatus(_A)
_CfprPkiCertReqEmail_Type=SnmpAdminString
_CfprPkiCertReqEmail_Object=MibTableColumn
cfprPkiCertReqEmail=_CfprPkiCertReqEmail_Object((1,3,6,1,4,1,9,9,826,1,61,1,1,6),_CfprPkiCertReqEmail_Type())
cfprPkiCertReqEmail.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiCertReqEmail.setStatus(_A)
_CfprPkiCertReqIp_Type=SnmpAdminString
_CfprPkiCertReqIp_Object=MibTableColumn
cfprPkiCertReqIp=_CfprPkiCertReqIp_Object((1,3,6,1,4,1,9,9,826,1,61,1,1,7),_CfprPkiCertReqIp_Type())
cfprPkiCertReqIp.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiCertReqIp.setStatus(_A)
_CfprPkiCertReqIpA_Type=InetAddressIPv4
_CfprPkiCertReqIpA_Object=MibTableColumn
cfprPkiCertReqIpA=_CfprPkiCertReqIpA_Object((1,3,6,1,4,1,9,9,826,1,61,1,1,8),_CfprPkiCertReqIpA_Type())
cfprPkiCertReqIpA.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiCertReqIpA.setStatus(_A)
_CfprPkiCertReqIpB_Type=InetAddressIPv4
_CfprPkiCertReqIpB_Object=MibTableColumn
cfprPkiCertReqIpB=_CfprPkiCertReqIpB_Object((1,3,6,1,4,1,9,9,826,1,61,1,1,9),_CfprPkiCertReqIpB_Type())
cfprPkiCertReqIpB.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiCertReqIpB.setStatus(_A)
_CfprPkiCertReqIpv6_Type=SnmpAdminString
_CfprPkiCertReqIpv6_Object=MibTableColumn
cfprPkiCertReqIpv6=_CfprPkiCertReqIpv6_Object((1,3,6,1,4,1,9,9,826,1,61,1,1,10),_CfprPkiCertReqIpv6_Type())
cfprPkiCertReqIpv6.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiCertReqIpv6.setStatus(_A)
_CfprPkiCertReqIpv6A_Type=InetAddressIPv6
_CfprPkiCertReqIpv6A_Object=MibTableColumn
cfprPkiCertReqIpv6A=_CfprPkiCertReqIpv6A_Object((1,3,6,1,4,1,9,9,826,1,61,1,1,11),_CfprPkiCertReqIpv6A_Type())
cfprPkiCertReqIpv6A.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiCertReqIpv6A.setStatus(_A)
_CfprPkiCertReqIpv6B_Type=InetAddressIPv6
_CfprPkiCertReqIpv6B_Object=MibTableColumn
cfprPkiCertReqIpv6B=_CfprPkiCertReqIpv6B_Object((1,3,6,1,4,1,9,9,826,1,61,1,1,12),_CfprPkiCertReqIpv6B_Type())
cfprPkiCertReqIpv6B.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiCertReqIpv6B.setStatus(_A)
_CfprPkiCertReqLocality_Type=SnmpAdminString
_CfprPkiCertReqLocality_Object=MibTableColumn
cfprPkiCertReqLocality=_CfprPkiCertReqLocality_Object((1,3,6,1,4,1,9,9,826,1,61,1,1,13),_CfprPkiCertReqLocality_Type())
cfprPkiCertReqLocality.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiCertReqLocality.setStatus(_A)
_CfprPkiCertReqOrgName_Type=SnmpAdminString
_CfprPkiCertReqOrgName_Object=MibTableColumn
cfprPkiCertReqOrgName=_CfprPkiCertReqOrgName_Object((1,3,6,1,4,1,9,9,826,1,61,1,1,14),_CfprPkiCertReqOrgName_Type())
cfprPkiCertReqOrgName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiCertReqOrgName.setStatus(_A)
_CfprPkiCertReqOrgUnitName_Type=SnmpAdminString
_CfprPkiCertReqOrgUnitName_Object=MibTableColumn
cfprPkiCertReqOrgUnitName=_CfprPkiCertReqOrgUnitName_Object((1,3,6,1,4,1,9,9,826,1,61,1,1,15),_CfprPkiCertReqOrgUnitName_Type())
cfprPkiCertReqOrgUnitName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiCertReqOrgUnitName.setStatus(_A)
_CfprPkiCertReqPwd_Type=SnmpAdminString
_CfprPkiCertReqPwd_Object=MibTableColumn
cfprPkiCertReqPwd=_CfprPkiCertReqPwd_Object((1,3,6,1,4,1,9,9,826,1,61,1,1,16),_CfprPkiCertReqPwd_Type())
cfprPkiCertReqPwd.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiCertReqPwd.setStatus(_A)
_CfprPkiCertReqReq_Type=SnmpAdminString
_CfprPkiCertReqReq_Object=MibTableColumn
cfprPkiCertReqReq=_CfprPkiCertReqReq_Object((1,3,6,1,4,1,9,9,826,1,61,1,1,17),_CfprPkiCertReqReq_Type())
cfprPkiCertReqReq.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiCertReqReq.setStatus(_A)
_CfprPkiCertReqState_Type=SnmpAdminString
_CfprPkiCertReqState_Object=MibTableColumn
cfprPkiCertReqState=_CfprPkiCertReqState_Object((1,3,6,1,4,1,9,9,826,1,61,1,1,18),_CfprPkiCertReqState_Type())
cfprPkiCertReqState.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiCertReqState.setStatus(_A)
_CfprPkiCertReqSubjName_Type=SnmpAdminString
_CfprPkiCertReqSubjName_Object=MibTableColumn
cfprPkiCertReqSubjName=_CfprPkiCertReqSubjName_Object((1,3,6,1,4,1,9,9,826,1,61,1,1,19),_CfprPkiCertReqSubjName_Type())
cfprPkiCertReqSubjName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiCertReqSubjName.setStatus(_A)
_CfprPkiEpTable_Object=MibTable
cfprPkiEpTable=_CfprPkiEpTable_Object((1,3,6,1,4,1,9,9,826,1,61,2))
if mibBuilder.loadTexts:cfprPkiEpTable.setStatus(_A)
_CfprPkiEpEntry_Object=MibTableRow
cfprPkiEpEntry=_CfprPkiEpEntry_Object((1,3,6,1,4,1,9,9,826,1,61,2,1))
cfprPkiEpEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:cfprPkiEpEntry.setStatus(_A)
_CfprPkiEpInstanceId_Type=CfprManagedObjectId
_CfprPkiEpInstanceId_Object=MibTableColumn
cfprPkiEpInstanceId=_CfprPkiEpInstanceId_Object((1,3,6,1,4,1,9,9,826,1,61,2,1,1),_CfprPkiEpInstanceId_Type())
cfprPkiEpInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprPkiEpInstanceId.setStatus(_A)
_CfprPkiEpDn_Type=CfprManagedObjectDn
_CfprPkiEpDn_Object=MibTableColumn
cfprPkiEpDn=_CfprPkiEpDn_Object((1,3,6,1,4,1,9,9,826,1,61,2,1,2),_CfprPkiEpDn_Type())
cfprPkiEpDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiEpDn.setStatus(_A)
_CfprPkiEpRn_Type=SnmpAdminString
_CfprPkiEpRn_Object=MibTableColumn
cfprPkiEpRn=_CfprPkiEpRn_Object((1,3,6,1,4,1,9,9,826,1,61,2,1,3),_CfprPkiEpRn_Type())
cfprPkiEpRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiEpRn.setStatus(_A)
_CfprPkiEpDescr_Type=SnmpAdminString
_CfprPkiEpDescr_Object=MibTableColumn
cfprPkiEpDescr=_CfprPkiEpDescr_Object((1,3,6,1,4,1,9,9,826,1,61,2,1,4),_CfprPkiEpDescr_Type())
cfprPkiEpDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiEpDescr.setStatus(_A)
_CfprPkiEpFsmDescr_Type=SnmpAdminString
_CfprPkiEpFsmDescr_Object=MibTableColumn
cfprPkiEpFsmDescr=_CfprPkiEpFsmDescr_Object((1,3,6,1,4,1,9,9,826,1,61,2,1,5),_CfprPkiEpFsmDescr_Type())
cfprPkiEpFsmDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiEpFsmDescr.setStatus(_A)
_CfprPkiEpFsmPrev_Type=SnmpAdminString
_CfprPkiEpFsmPrev_Object=MibTableColumn
cfprPkiEpFsmPrev=_CfprPkiEpFsmPrev_Object((1,3,6,1,4,1,9,9,826,1,61,2,1,6),_CfprPkiEpFsmPrev_Type())
cfprPkiEpFsmPrev.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiEpFsmPrev.setStatus(_A)
_CfprPkiEpFsmProgr_Type=Gauge32
_CfprPkiEpFsmProgr_Object=MibTableColumn
cfprPkiEpFsmProgr=_CfprPkiEpFsmProgr_Object((1,3,6,1,4,1,9,9,826,1,61,2,1,7),_CfprPkiEpFsmProgr_Type())
cfprPkiEpFsmProgr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiEpFsmProgr.setStatus(_A)
_CfprPkiEpFsmRmtInvErrCode_Type=Gauge32
_CfprPkiEpFsmRmtInvErrCode_Object=MibTableColumn
cfprPkiEpFsmRmtInvErrCode=_CfprPkiEpFsmRmtInvErrCode_Object((1,3,6,1,4,1,9,9,826,1,61,2,1,8),_CfprPkiEpFsmRmtInvErrCode_Type())
cfprPkiEpFsmRmtInvErrCode.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiEpFsmRmtInvErrCode.setStatus(_A)
_CfprPkiEpFsmRmtInvErrDescr_Type=SnmpAdminString
_CfprPkiEpFsmRmtInvErrDescr_Object=MibTableColumn
cfprPkiEpFsmRmtInvErrDescr=_CfprPkiEpFsmRmtInvErrDescr_Object((1,3,6,1,4,1,9,9,826,1,61,2,1,9),_CfprPkiEpFsmRmtInvErrDescr_Type())
cfprPkiEpFsmRmtInvErrDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiEpFsmRmtInvErrDescr.setStatus(_A)
_CfprPkiEpFsmRmtInvRslt_Type=CfprConditionRemoteInvRslt
_CfprPkiEpFsmRmtInvRslt_Object=MibTableColumn
cfprPkiEpFsmRmtInvRslt=_CfprPkiEpFsmRmtInvRslt_Object((1,3,6,1,4,1,9,9,826,1,61,2,1,10),_CfprPkiEpFsmRmtInvRslt_Type())
cfprPkiEpFsmRmtInvRslt.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiEpFsmRmtInvRslt.setStatus(_A)
_CfprPkiEpFsmStageDescr_Type=SnmpAdminString
_CfprPkiEpFsmStageDescr_Object=MibTableColumn
cfprPkiEpFsmStageDescr=_CfprPkiEpFsmStageDescr_Object((1,3,6,1,4,1,9,9,826,1,61,2,1,11),_CfprPkiEpFsmStageDescr_Type())
cfprPkiEpFsmStageDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiEpFsmStageDescr.setStatus(_A)
_CfprPkiEpFsmStamp_Type=DateAndTime
_CfprPkiEpFsmStamp_Object=MibTableColumn
cfprPkiEpFsmStamp=_CfprPkiEpFsmStamp_Object((1,3,6,1,4,1,9,9,826,1,61,2,1,12),_CfprPkiEpFsmStamp_Type())
cfprPkiEpFsmStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiEpFsmStamp.setStatus(_A)
_CfprPkiEpFsmStatus_Type=SnmpAdminString
_CfprPkiEpFsmStatus_Object=MibTableColumn
cfprPkiEpFsmStatus=_CfprPkiEpFsmStatus_Object((1,3,6,1,4,1,9,9,826,1,61,2,1,13),_CfprPkiEpFsmStatus_Type())
cfprPkiEpFsmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiEpFsmStatus.setStatus(_A)
_CfprPkiEpFsmTry_Type=Gauge32
_CfprPkiEpFsmTry_Object=MibTableColumn
cfprPkiEpFsmTry=_CfprPkiEpFsmTry_Object((1,3,6,1,4,1,9,9,826,1,61,2,1,14),_CfprPkiEpFsmTry_Type())
cfprPkiEpFsmTry.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiEpFsmTry.setStatus(_A)
_CfprPkiEpIntId_Type=SnmpAdminString
_CfprPkiEpIntId_Object=MibTableColumn
cfprPkiEpIntId=_CfprPkiEpIntId_Object((1,3,6,1,4,1,9,9,826,1,61,2,1,15),_CfprPkiEpIntId_Type())
cfprPkiEpIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiEpIntId.setStatus(_A)
_CfprPkiEpName_Type=SnmpAdminString
_CfprPkiEpName_Object=MibTableColumn
cfprPkiEpName=_CfprPkiEpName_Object((1,3,6,1,4,1,9,9,826,1,61,2,1,16),_CfprPkiEpName_Type())
cfprPkiEpName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiEpName.setStatus(_A)
_CfprPkiEpPolicyLevel_Type=Gauge32
_CfprPkiEpPolicyLevel_Object=MibTableColumn
cfprPkiEpPolicyLevel=_CfprPkiEpPolicyLevel_Object((1,3,6,1,4,1,9,9,826,1,61,2,1,17),_CfprPkiEpPolicyLevel_Type())
cfprPkiEpPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiEpPolicyLevel.setStatus(_A)
_CfprPkiEpPolicyOwner_Type=CfprPolicyPolicyOwner
_CfprPkiEpPolicyOwner_Object=MibTableColumn
cfprPkiEpPolicyOwner=_CfprPkiEpPolicyOwner_Object((1,3,6,1,4,1,9,9,826,1,61,2,1,18),_CfprPkiEpPolicyOwner_Type())
cfprPkiEpPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiEpPolicyOwner.setStatus(_A)
_CfprPkiEpFsmTable_Object=MibTable
cfprPkiEpFsmTable=_CfprPkiEpFsmTable_Object((1,3,6,1,4,1,9,9,826,1,61,3))
if mibBuilder.loadTexts:cfprPkiEpFsmTable.setStatus(_A)
_CfprPkiEpFsmEntry_Object=MibTableRow
cfprPkiEpFsmEntry=_CfprPkiEpFsmEntry_Object((1,3,6,1,4,1,9,9,826,1,61,3,1))
cfprPkiEpFsmEntry.setIndexNames((0,_C,_G))
if mibBuilder.loadTexts:cfprPkiEpFsmEntry.setStatus(_A)
_CfprPkiEpFsmInstanceId_Type=CfprManagedObjectId
_CfprPkiEpFsmInstanceId_Object=MibTableColumn
cfprPkiEpFsmInstanceId=_CfprPkiEpFsmInstanceId_Object((1,3,6,1,4,1,9,9,826,1,61,3,1,1),_CfprPkiEpFsmInstanceId_Type())
cfprPkiEpFsmInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprPkiEpFsmInstanceId.setStatus(_A)
_CfprPkiEpFsmDn_Type=CfprManagedObjectDn
_CfprPkiEpFsmDn_Object=MibTableColumn
cfprPkiEpFsmDn=_CfprPkiEpFsmDn_Object((1,3,6,1,4,1,9,9,826,1,61,3,1,2),_CfprPkiEpFsmDn_Type())
cfprPkiEpFsmDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiEpFsmDn.setStatus(_A)
_CfprPkiEpFsmRn_Type=SnmpAdminString
_CfprPkiEpFsmRn_Object=MibTableColumn
cfprPkiEpFsmRn=_CfprPkiEpFsmRn_Object((1,3,6,1,4,1,9,9,826,1,61,3,1,3),_CfprPkiEpFsmRn_Type())
cfprPkiEpFsmRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiEpFsmRn.setStatus(_A)
_CfprPkiEpFsmCompletionTime_Type=DateAndTime
_CfprPkiEpFsmCompletionTime_Object=MibTableColumn
cfprPkiEpFsmCompletionTime=_CfprPkiEpFsmCompletionTime_Object((1,3,6,1,4,1,9,9,826,1,61,3,1,4),_CfprPkiEpFsmCompletionTime_Type())
cfprPkiEpFsmCompletionTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiEpFsmCompletionTime.setStatus(_A)
_CfprPkiEpFsmCurrentFsm_Type=CfprPkiEpFsmCurrentFsm
_CfprPkiEpFsmCurrentFsm_Object=MibTableColumn
cfprPkiEpFsmCurrentFsm=_CfprPkiEpFsmCurrentFsm_Object((1,3,6,1,4,1,9,9,826,1,61,3,1,5),_CfprPkiEpFsmCurrentFsm_Type())
cfprPkiEpFsmCurrentFsm.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiEpFsmCurrentFsm.setStatus(_A)
_CfprPkiEpFsmDescrData_Type=SnmpAdminString
_CfprPkiEpFsmDescrData_Object=MibTableColumn
cfprPkiEpFsmDescrData=_CfprPkiEpFsmDescrData_Object((1,3,6,1,4,1,9,9,826,1,61,3,1,6),_CfprPkiEpFsmDescrData_Type())
cfprPkiEpFsmDescrData.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiEpFsmDescrData.setStatus(_A)
_CfprPkiEpFsmFsmStatus_Type=CfprFsmFsmStageStatus
_CfprPkiEpFsmFsmStatus_Object=MibTableColumn
cfprPkiEpFsmFsmStatus=_CfprPkiEpFsmFsmStatus_Object((1,3,6,1,4,1,9,9,826,1,61,3,1,7),_CfprPkiEpFsmFsmStatus_Type())
cfprPkiEpFsmFsmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiEpFsmFsmStatus.setStatus(_A)
_CfprPkiEpFsmProgress_Type=Gauge32
_CfprPkiEpFsmProgress_Object=MibTableColumn
cfprPkiEpFsmProgress=_CfprPkiEpFsmProgress_Object((1,3,6,1,4,1,9,9,826,1,61,3,1,8),_CfprPkiEpFsmProgress_Type())
cfprPkiEpFsmProgress.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiEpFsmProgress.setStatus(_A)
_CfprPkiEpFsmRmtErrCode_Type=Gauge32
_CfprPkiEpFsmRmtErrCode_Object=MibTableColumn
cfprPkiEpFsmRmtErrCode=_CfprPkiEpFsmRmtErrCode_Object((1,3,6,1,4,1,9,9,826,1,61,3,1,9),_CfprPkiEpFsmRmtErrCode_Type())
cfprPkiEpFsmRmtErrCode.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiEpFsmRmtErrCode.setStatus(_A)
_CfprPkiEpFsmRmtErrDescr_Type=SnmpAdminString
_CfprPkiEpFsmRmtErrDescr_Object=MibTableColumn
cfprPkiEpFsmRmtErrDescr=_CfprPkiEpFsmRmtErrDescr_Object((1,3,6,1,4,1,9,9,826,1,61,3,1,10),_CfprPkiEpFsmRmtErrDescr_Type())
cfprPkiEpFsmRmtErrDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiEpFsmRmtErrDescr.setStatus(_A)
_CfprPkiEpFsmRmtRslt_Type=CfprConditionRemoteInvRslt
_CfprPkiEpFsmRmtRslt_Object=MibTableColumn
cfprPkiEpFsmRmtRslt=_CfprPkiEpFsmRmtRslt_Object((1,3,6,1,4,1,9,9,826,1,61,3,1,11),_CfprPkiEpFsmRmtRslt_Type())
cfprPkiEpFsmRmtRslt.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiEpFsmRmtRslt.setStatus(_A)
_CfprPkiEpFsmStageTable_Object=MibTable
cfprPkiEpFsmStageTable=_CfprPkiEpFsmStageTable_Object((1,3,6,1,4,1,9,9,826,1,61,4))
if mibBuilder.loadTexts:cfprPkiEpFsmStageTable.setStatus(_A)
_CfprPkiEpFsmStageEntry_Object=MibTableRow
cfprPkiEpFsmStageEntry=_CfprPkiEpFsmStageEntry_Object((1,3,6,1,4,1,9,9,826,1,61,4,1))
cfprPkiEpFsmStageEntry.setIndexNames((0,_C,_H))
if mibBuilder.loadTexts:cfprPkiEpFsmStageEntry.setStatus(_A)
_CfprPkiEpFsmStageInstanceId_Type=CfprManagedObjectId
_CfprPkiEpFsmStageInstanceId_Object=MibTableColumn
cfprPkiEpFsmStageInstanceId=_CfprPkiEpFsmStageInstanceId_Object((1,3,6,1,4,1,9,9,826,1,61,4,1,1),_CfprPkiEpFsmStageInstanceId_Type())
cfprPkiEpFsmStageInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprPkiEpFsmStageInstanceId.setStatus(_A)
_CfprPkiEpFsmStageDn_Type=CfprManagedObjectDn
_CfprPkiEpFsmStageDn_Object=MibTableColumn
cfprPkiEpFsmStageDn=_CfprPkiEpFsmStageDn_Object((1,3,6,1,4,1,9,9,826,1,61,4,1,2),_CfprPkiEpFsmStageDn_Type())
cfprPkiEpFsmStageDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiEpFsmStageDn.setStatus(_A)
_CfprPkiEpFsmStageRn_Type=SnmpAdminString
_CfprPkiEpFsmStageRn_Object=MibTableColumn
cfprPkiEpFsmStageRn=_CfprPkiEpFsmStageRn_Object((1,3,6,1,4,1,9,9,826,1,61,4,1,3),_CfprPkiEpFsmStageRn_Type())
cfprPkiEpFsmStageRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiEpFsmStageRn.setStatus(_A)
_CfprPkiEpFsmStageDescrData_Type=SnmpAdminString
_CfprPkiEpFsmStageDescrData_Object=MibTableColumn
cfprPkiEpFsmStageDescrData=_CfprPkiEpFsmStageDescrData_Object((1,3,6,1,4,1,9,9,826,1,61,4,1,4),_CfprPkiEpFsmStageDescrData_Type())
cfprPkiEpFsmStageDescrData.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiEpFsmStageDescrData.setStatus(_A)
_CfprPkiEpFsmStageLastUpdateTime_Type=DateAndTime
_CfprPkiEpFsmStageLastUpdateTime_Object=MibTableColumn
cfprPkiEpFsmStageLastUpdateTime=_CfprPkiEpFsmStageLastUpdateTime_Object((1,3,6,1,4,1,9,9,826,1,61,4,1,5),_CfprPkiEpFsmStageLastUpdateTime_Type())
cfprPkiEpFsmStageLastUpdateTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiEpFsmStageLastUpdateTime.setStatus(_A)
_CfprPkiEpFsmStageName_Type=CfprPkiEpFsmStageName
_CfprPkiEpFsmStageName_Object=MibTableColumn
cfprPkiEpFsmStageName=_CfprPkiEpFsmStageName_Object((1,3,6,1,4,1,9,9,826,1,61,4,1,6),_CfprPkiEpFsmStageName_Type())
cfprPkiEpFsmStageName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiEpFsmStageName.setStatus(_A)
_CfprPkiEpFsmStageOrder_Type=Gauge32
_CfprPkiEpFsmStageOrder_Object=MibTableColumn
cfprPkiEpFsmStageOrder=_CfprPkiEpFsmStageOrder_Object((1,3,6,1,4,1,9,9,826,1,61,4,1,7),_CfprPkiEpFsmStageOrder_Type())
cfprPkiEpFsmStageOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiEpFsmStageOrder.setStatus(_A)
_CfprPkiEpFsmStageRetry_Type=Gauge32
_CfprPkiEpFsmStageRetry_Object=MibTableColumn
cfprPkiEpFsmStageRetry=_CfprPkiEpFsmStageRetry_Object((1,3,6,1,4,1,9,9,826,1,61,4,1,8),_CfprPkiEpFsmStageRetry_Type())
cfprPkiEpFsmStageRetry.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiEpFsmStageRetry.setStatus(_A)
_CfprPkiEpFsmStageStageStatus_Type=CfprFsmFsmStageStatus
_CfprPkiEpFsmStageStageStatus_Object=MibTableColumn
cfprPkiEpFsmStageStageStatus=_CfprPkiEpFsmStageStageStatus_Object((1,3,6,1,4,1,9,9,826,1,61,4,1,9),_CfprPkiEpFsmStageStageStatus_Type())
cfprPkiEpFsmStageStageStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiEpFsmStageStageStatus.setStatus(_A)
_CfprPkiEpFsmTaskTable_Object=MibTable
cfprPkiEpFsmTaskTable=_CfprPkiEpFsmTaskTable_Object((1,3,6,1,4,1,9,9,826,1,61,5))
if mibBuilder.loadTexts:cfprPkiEpFsmTaskTable.setStatus(_A)
_CfprPkiEpFsmTaskEntry_Object=MibTableRow
cfprPkiEpFsmTaskEntry=_CfprPkiEpFsmTaskEntry_Object((1,3,6,1,4,1,9,9,826,1,61,5,1))
cfprPkiEpFsmTaskEntry.setIndexNames((0,_C,_I))
if mibBuilder.loadTexts:cfprPkiEpFsmTaskEntry.setStatus(_A)
_CfprPkiEpFsmTaskInstanceId_Type=CfprManagedObjectId
_CfprPkiEpFsmTaskInstanceId_Object=MibTableColumn
cfprPkiEpFsmTaskInstanceId=_CfprPkiEpFsmTaskInstanceId_Object((1,3,6,1,4,1,9,9,826,1,61,5,1,1),_CfprPkiEpFsmTaskInstanceId_Type())
cfprPkiEpFsmTaskInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprPkiEpFsmTaskInstanceId.setStatus(_A)
_CfprPkiEpFsmTaskDn_Type=CfprManagedObjectDn
_CfprPkiEpFsmTaskDn_Object=MibTableColumn
cfprPkiEpFsmTaskDn=_CfprPkiEpFsmTaskDn_Object((1,3,6,1,4,1,9,9,826,1,61,5,1,2),_CfprPkiEpFsmTaskDn_Type())
cfprPkiEpFsmTaskDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiEpFsmTaskDn.setStatus(_A)
_CfprPkiEpFsmTaskRn_Type=SnmpAdminString
_CfprPkiEpFsmTaskRn_Object=MibTableColumn
cfprPkiEpFsmTaskRn=_CfprPkiEpFsmTaskRn_Object((1,3,6,1,4,1,9,9,826,1,61,5,1,3),_CfprPkiEpFsmTaskRn_Type())
cfprPkiEpFsmTaskRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiEpFsmTaskRn.setStatus(_A)
_CfprPkiEpFsmTaskCompletion_Type=CfprFsmCompletion
_CfprPkiEpFsmTaskCompletion_Object=MibTableColumn
cfprPkiEpFsmTaskCompletion=_CfprPkiEpFsmTaskCompletion_Object((1,3,6,1,4,1,9,9,826,1,61,5,1,4),_CfprPkiEpFsmTaskCompletion_Type())
cfprPkiEpFsmTaskCompletion.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiEpFsmTaskCompletion.setStatus(_A)
_CfprPkiEpFsmTaskFlags_Type=CfprFsmFlags
_CfprPkiEpFsmTaskFlags_Object=MibTableColumn
cfprPkiEpFsmTaskFlags=_CfprPkiEpFsmTaskFlags_Object((1,3,6,1,4,1,9,9,826,1,61,5,1,5),_CfprPkiEpFsmTaskFlags_Type())
cfprPkiEpFsmTaskFlags.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiEpFsmTaskFlags.setStatus(_A)
_CfprPkiEpFsmTaskItem_Type=CfprPkiEpFsmTaskItem
_CfprPkiEpFsmTaskItem_Object=MibTableColumn
cfprPkiEpFsmTaskItem=_CfprPkiEpFsmTaskItem_Object((1,3,6,1,4,1,9,9,826,1,61,5,1,6),_CfprPkiEpFsmTaskItem_Type())
cfprPkiEpFsmTaskItem.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiEpFsmTaskItem.setStatus(_A)
_CfprPkiEpFsmTaskSeqId_Type=Gauge32
_CfprPkiEpFsmTaskSeqId_Object=MibTableColumn
cfprPkiEpFsmTaskSeqId=_CfprPkiEpFsmTaskSeqId_Object((1,3,6,1,4,1,9,9,826,1,61,5,1,7),_CfprPkiEpFsmTaskSeqId_Type())
cfprPkiEpFsmTaskSeqId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiEpFsmTaskSeqId.setStatus(_A)
_CfprPkiKeyRingTable_Object=MibTable
cfprPkiKeyRingTable=_CfprPkiKeyRingTable_Object((1,3,6,1,4,1,9,9,826,1,61,6))
if mibBuilder.loadTexts:cfprPkiKeyRingTable.setStatus(_A)
_CfprPkiKeyRingEntry_Object=MibTableRow
cfprPkiKeyRingEntry=_CfprPkiKeyRingEntry_Object((1,3,6,1,4,1,9,9,826,1,61,6,1))
cfprPkiKeyRingEntry.setIndexNames((0,_C,_J))
if mibBuilder.loadTexts:cfprPkiKeyRingEntry.setStatus(_A)
_CfprPkiKeyRingInstanceId_Type=CfprManagedObjectId
_CfprPkiKeyRingInstanceId_Object=MibTableColumn
cfprPkiKeyRingInstanceId=_CfprPkiKeyRingInstanceId_Object((1,3,6,1,4,1,9,9,826,1,61,6,1,1),_CfprPkiKeyRingInstanceId_Type())
cfprPkiKeyRingInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprPkiKeyRingInstanceId.setStatus(_A)
_CfprPkiKeyRingDn_Type=CfprManagedObjectDn
_CfprPkiKeyRingDn_Object=MibTableColumn
cfprPkiKeyRingDn=_CfprPkiKeyRingDn_Object((1,3,6,1,4,1,9,9,826,1,61,6,1,2),_CfprPkiKeyRingDn_Type())
cfprPkiKeyRingDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiKeyRingDn.setStatus(_A)
_CfprPkiKeyRingRn_Type=SnmpAdminString
_CfprPkiKeyRingRn_Object=MibTableColumn
cfprPkiKeyRingRn=_CfprPkiKeyRingRn_Object((1,3,6,1,4,1,9,9,826,1,61,6,1,3),_CfprPkiKeyRingRn_Type())
cfprPkiKeyRingRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiKeyRingRn.setStatus(_A)
_CfprPkiKeyRingAdminState_Type=CfprPkiKeyringState
_CfprPkiKeyRingAdminState_Object=MibTableColumn
cfprPkiKeyRingAdminState=_CfprPkiKeyRingAdminState_Object((1,3,6,1,4,1,9,9,826,1,61,6,1,4),_CfprPkiKeyRingAdminState_Type())
cfprPkiKeyRingAdminState.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiKeyRingAdminState.setStatus(_A)
_CfprPkiKeyRingCert_Type=SnmpAdminString
_CfprPkiKeyRingCert_Object=MibTableColumn
cfprPkiKeyRingCert=_CfprPkiKeyRingCert_Object((1,3,6,1,4,1,9,9,826,1,61,6,1,5),_CfprPkiKeyRingCert_Type())
cfprPkiKeyRingCert.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiKeyRingCert.setStatus(_A)
_CfprPkiKeyRingCertStatus_Type=CfprPkiCertStatus
_CfprPkiKeyRingCertStatus_Object=MibTableColumn
cfprPkiKeyRingCertStatus=_CfprPkiKeyRingCertStatus_Object((1,3,6,1,4,1,9,9,826,1,61,6,1,6),_CfprPkiKeyRingCertStatus_Type())
cfprPkiKeyRingCertStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiKeyRingCertStatus.setStatus(_A)
_CfprPkiKeyRingConfigState_Type=CfprAaaConfigState
_CfprPkiKeyRingConfigState_Object=MibTableColumn
cfprPkiKeyRingConfigState=_CfprPkiKeyRingConfigState_Object((1,3,6,1,4,1,9,9,826,1,61,6,1,7),_CfprPkiKeyRingConfigState_Type())
cfprPkiKeyRingConfigState.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiKeyRingConfigState.setStatus(_A)
_CfprPkiKeyRingConfigStatusMessage_Type=SnmpAdminString
_CfprPkiKeyRingConfigStatusMessage_Object=MibTableColumn
cfprPkiKeyRingConfigStatusMessage=_CfprPkiKeyRingConfigStatusMessage_Object((1,3,6,1,4,1,9,9,826,1,61,6,1,8),_CfprPkiKeyRingConfigStatusMessage_Type())
cfprPkiKeyRingConfigStatusMessage.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiKeyRingConfigStatusMessage.setStatus(_A)
_CfprPkiKeyRingDescr_Type=SnmpAdminString
_CfprPkiKeyRingDescr_Object=MibTableColumn
cfprPkiKeyRingDescr=_CfprPkiKeyRingDescr_Object((1,3,6,1,4,1,9,9,826,1,61,6,1,9),_CfprPkiKeyRingDescr_Type())
cfprPkiKeyRingDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiKeyRingDescr.setStatus(_A)
_CfprPkiKeyRingIntId_Type=SnmpAdminString
_CfprPkiKeyRingIntId_Object=MibTableColumn
cfprPkiKeyRingIntId=_CfprPkiKeyRingIntId_Object((1,3,6,1,4,1,9,9,826,1,61,6,1,10),_CfprPkiKeyRingIntId_Type())
cfprPkiKeyRingIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiKeyRingIntId.setStatus(_A)
_CfprPkiKeyRingKey_Type=SnmpAdminString
_CfprPkiKeyRingKey_Object=MibTableColumn
cfprPkiKeyRingKey=_CfprPkiKeyRingKey_Object((1,3,6,1,4,1,9,9,826,1,61,6,1,11),_CfprPkiKeyRingKey_Type())
cfprPkiKeyRingKey.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiKeyRingKey.setStatus(_A)
_CfprPkiKeyRingModulus_Type=CfprPkiModulus
_CfprPkiKeyRingModulus_Object=MibTableColumn
cfprPkiKeyRingModulus=_CfprPkiKeyRingModulus_Object((1,3,6,1,4,1,9,9,826,1,61,6,1,12),_CfprPkiKeyRingModulus_Type())
cfprPkiKeyRingModulus.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiKeyRingModulus.setStatus(_A)
_CfprPkiKeyRingName_Type=SnmpAdminString
_CfprPkiKeyRingName_Object=MibTableColumn
cfprPkiKeyRingName=_CfprPkiKeyRingName_Object((1,3,6,1,4,1,9,9,826,1,61,6,1,13),_CfprPkiKeyRingName_Type())
cfprPkiKeyRingName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiKeyRingName.setStatus(_A)
_CfprPkiKeyRingPolicyLevel_Type=Gauge32
_CfprPkiKeyRingPolicyLevel_Object=MibTableColumn
cfprPkiKeyRingPolicyLevel=_CfprPkiKeyRingPolicyLevel_Object((1,3,6,1,4,1,9,9,826,1,61,6,1,14),_CfprPkiKeyRingPolicyLevel_Type())
cfprPkiKeyRingPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiKeyRingPolicyLevel.setStatus(_A)
_CfprPkiKeyRingPolicyOwner_Type=CfprPolicyPolicyOwner
_CfprPkiKeyRingPolicyOwner_Object=MibTableColumn
cfprPkiKeyRingPolicyOwner=_CfprPkiKeyRingPolicyOwner_Object((1,3,6,1,4,1,9,9,826,1,61,6,1,15),_CfprPkiKeyRingPolicyOwner_Type())
cfprPkiKeyRingPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiKeyRingPolicyOwner.setStatus(_A)
_CfprPkiKeyRingRegen_Type=TruthValue
_CfprPkiKeyRingRegen_Object=MibTableColumn
cfprPkiKeyRingRegen=_CfprPkiKeyRingRegen_Object((1,3,6,1,4,1,9,9,826,1,61,6,1,16),_CfprPkiKeyRingRegen_Type())
cfprPkiKeyRingRegen.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiKeyRingRegen.setStatus(_A)
_CfprPkiKeyRingTp_Type=SnmpAdminString
_CfprPkiKeyRingTp_Object=MibTableColumn
cfprPkiKeyRingTp=_CfprPkiKeyRingTp_Object((1,3,6,1,4,1,9,9,826,1,61,6,1,17),_CfprPkiKeyRingTp_Type())
cfprPkiKeyRingTp.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiKeyRingTp.setStatus(_A)
_CfprPkiKeyRingZeroized_Type=TruthValue
_CfprPkiKeyRingZeroized_Object=MibTableColumn
cfprPkiKeyRingZeroized=_CfprPkiKeyRingZeroized_Object((1,3,6,1,4,1,9,9,826,1,61,6,1,18),_CfprPkiKeyRingZeroized_Type())
cfprPkiKeyRingZeroized.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiKeyRingZeroized.setStatus(_A)
_CfprPkiKeyRingEc_Type=CfprPkiEc
_CfprPkiKeyRingEc_Object=MibTableColumn
cfprPkiKeyRingEc=_CfprPkiKeyRingEc_Object((1,3,6,1,4,1,9,9,826,1,61,6,1,19),_CfprPkiKeyRingEc_Type())
cfprPkiKeyRingEc.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiKeyRingEc.setStatus(_A)
_CfprPkiKeyRingType_Type=CfprPkiType
_CfprPkiKeyRingType_Object=MibTableColumn
cfprPkiKeyRingType=_CfprPkiKeyRingType_Object((1,3,6,1,4,1,9,9,826,1,61,6,1,20),_CfprPkiKeyRingType_Type())
cfprPkiKeyRingType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiKeyRingType.setStatus(_A)
_CfprPkiTPTable_Object=MibTable
cfprPkiTPTable=_CfprPkiTPTable_Object((1,3,6,1,4,1,9,9,826,1,61,7))
if mibBuilder.loadTexts:cfprPkiTPTable.setStatus(_A)
_CfprPkiTPEntry_Object=MibTableRow
cfprPkiTPEntry=_CfprPkiTPEntry_Object((1,3,6,1,4,1,9,9,826,1,61,7,1))
cfprPkiTPEntry.setIndexNames((0,_C,_K))
if mibBuilder.loadTexts:cfprPkiTPEntry.setStatus(_A)
_CfprPkiTPInstanceId_Type=CfprManagedObjectId
_CfprPkiTPInstanceId_Object=MibTableColumn
cfprPkiTPInstanceId=_CfprPkiTPInstanceId_Object((1,3,6,1,4,1,9,9,826,1,61,7,1,1),_CfprPkiTPInstanceId_Type())
cfprPkiTPInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprPkiTPInstanceId.setStatus(_A)
_CfprPkiTPDn_Type=CfprManagedObjectDn
_CfprPkiTPDn_Object=MibTableColumn
cfprPkiTPDn=_CfprPkiTPDn_Object((1,3,6,1,4,1,9,9,826,1,61,7,1,2),_CfprPkiTPDn_Type())
cfprPkiTPDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiTPDn.setStatus(_A)
_CfprPkiTPRn_Type=SnmpAdminString
_CfprPkiTPRn_Object=MibTableColumn
cfprPkiTPRn=_CfprPkiTPRn_Object((1,3,6,1,4,1,9,9,826,1,61,7,1,3),_CfprPkiTPRn_Type())
cfprPkiTPRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiTPRn.setStatus(_A)
_CfprPkiTPCertChain_Type=SnmpAdminString
_CfprPkiTPCertChain_Object=MibTableColumn
cfprPkiTPCertChain=_CfprPkiTPCertChain_Object((1,3,6,1,4,1,9,9,826,1,61,7,1,4),_CfprPkiTPCertChain_Type())
cfprPkiTPCertChain.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiTPCertChain.setStatus(_A)
_CfprPkiTPCertStatus_Type=CfprPkiCertStatus
_CfprPkiTPCertStatus_Object=MibTableColumn
cfprPkiTPCertStatus=_CfprPkiTPCertStatus_Object((1,3,6,1,4,1,9,9,826,1,61,7,1,5),_CfprPkiTPCertStatus_Type())
cfprPkiTPCertStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiTPCertStatus.setStatus(_A)
_CfprPkiTPDescr_Type=SnmpAdminString
_CfprPkiTPDescr_Object=MibTableColumn
cfprPkiTPDescr=_CfprPkiTPDescr_Object((1,3,6,1,4,1,9,9,826,1,61,7,1,6),_CfprPkiTPDescr_Type())
cfprPkiTPDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiTPDescr.setStatus(_A)
_CfprPkiTPFp_Type=SnmpAdminString
_CfprPkiTPFp_Object=MibTableColumn
cfprPkiTPFp=_CfprPkiTPFp_Object((1,3,6,1,4,1,9,9,826,1,61,7,1,7),_CfprPkiTPFp_Type())
cfprPkiTPFp.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiTPFp.setStatus(_A)
_CfprPkiTPIntId_Type=SnmpAdminString
_CfprPkiTPIntId_Object=MibTableColumn
cfprPkiTPIntId=_CfprPkiTPIntId_Object((1,3,6,1,4,1,9,9,826,1,61,7,1,8),_CfprPkiTPIntId_Type())
cfprPkiTPIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiTPIntId.setStatus(_A)
_CfprPkiTPName_Type=SnmpAdminString
_CfprPkiTPName_Object=MibTableColumn
cfprPkiTPName=_CfprPkiTPName_Object((1,3,6,1,4,1,9,9,826,1,61,7,1,9),_CfprPkiTPName_Type())
cfprPkiTPName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiTPName.setStatus(_A)
_CfprPkiTPNumCerts_Type=Gauge32
_CfprPkiTPNumCerts_Object=MibTableColumn
cfprPkiTPNumCerts=_CfprPkiTPNumCerts_Object((1,3,6,1,4,1,9,9,826,1,61,7,1,10),_CfprPkiTPNumCerts_Type())
cfprPkiTPNumCerts.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiTPNumCerts.setStatus(_A)
_CfprPkiTPPolicyLevel_Type=Gauge32
_CfprPkiTPPolicyLevel_Object=MibTableColumn
cfprPkiTPPolicyLevel=_CfprPkiTPPolicyLevel_Object((1,3,6,1,4,1,9,9,826,1,61,7,1,11),_CfprPkiTPPolicyLevel_Type())
cfprPkiTPPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiTPPolicyLevel.setStatus(_A)
_CfprPkiTPPolicyOwner_Type=CfprPolicyPolicyOwner
_CfprPkiTPPolicyOwner_Object=MibTableColumn
cfprPkiTPPolicyOwner=_CfprPkiTPPolicyOwner_Object((1,3,6,1,4,1,9,9,826,1,61,7,1,12),_CfprPkiTPPolicyOwner_Type())
cfprPkiTPPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiTPPolicyOwner.setStatus(_A)
_CfprPkiTPCertChainDecode_Type=SnmpAdminString
_CfprPkiTPCertChainDecode_Object=MibTableColumn
cfprPkiTPCertChainDecode=_CfprPkiTPCertChainDecode_Object((1,3,6,1,4,1,9,9,826,1,61,7,1,13),_CfprPkiTPCertChainDecode_Type())
cfprPkiTPCertChainDecode.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiTPCertChainDecode.setStatus(_A)
_CfprPkiCertRevokeTable_Object=MibTable
cfprPkiCertRevokeTable=_CfprPkiCertRevokeTable_Object((1,3,6,1,4,1,9,9,826,1,61,8))
if mibBuilder.loadTexts:cfprPkiCertRevokeTable.setStatus(_A)
_CfprPkiCertRevokeEntry_Object=MibTableRow
cfprPkiCertRevokeEntry=_CfprPkiCertRevokeEntry_Object((1,3,6,1,4,1,9,9,826,1,61,8,1))
cfprPkiCertRevokeEntry.setIndexNames((0,_C,_L))
if mibBuilder.loadTexts:cfprPkiCertRevokeEntry.setStatus(_A)
_CfprPkiCertRevokeInstanceId_Type=CfprManagedObjectId
_CfprPkiCertRevokeInstanceId_Object=MibTableColumn
cfprPkiCertRevokeInstanceId=_CfprPkiCertRevokeInstanceId_Object((1,3,6,1,4,1,9,9,826,1,61,8,1,1),_CfprPkiCertRevokeInstanceId_Type())
cfprPkiCertRevokeInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprPkiCertRevokeInstanceId.setStatus(_A)
_CfprPkiCertRevokeDn_Type=CfprManagedObjectDn
_CfprPkiCertRevokeDn_Object=MibTableColumn
cfprPkiCertRevokeDn=_CfprPkiCertRevokeDn_Object((1,3,6,1,4,1,9,9,826,1,61,8,1,2),_CfprPkiCertRevokeDn_Type())
cfprPkiCertRevokeDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiCertRevokeDn.setStatus(_A)
_CfprPkiCertRevokeRn_Type=SnmpAdminString
_CfprPkiCertRevokeRn_Object=MibTableColumn
cfprPkiCertRevokeRn=_CfprPkiCertRevokeRn_Object((1,3,6,1,4,1,9,9,826,1,61,8,1,3),_CfprPkiCertRevokeRn_Type())
cfprPkiCertRevokeRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiCertRevokeRn.setStatus(_A)
_CfprPkiCertRevokeCertRevokeMethod_Type=CfprPkiCertRevokeMethod
_CfprPkiCertRevokeCertRevokeMethod_Object=MibTableColumn
cfprPkiCertRevokeCertRevokeMethod=_CfprPkiCertRevokeCertRevokeMethod_Object((1,3,6,1,4,1,9,9,826,1,61,8,1,4),_CfprPkiCertRevokeCertRevokeMethod_Type())
cfprPkiCertRevokeCertRevokeMethod.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiCertRevokeCertRevokeMethod.setStatus(_A)
_CfprPkiCertRevokeCertStatus_Type=CfprPkiCertStatus
_CfprPkiCertRevokeCertStatus_Object=MibTableColumn
cfprPkiCertRevokeCertStatus=_CfprPkiCertRevokeCertStatus_Object((1,3,6,1,4,1,9,9,826,1,61,8,1,5),_CfprPkiCertRevokeCertStatus_Type())
cfprPkiCertRevokeCertStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiCertRevokeCertStatus.setStatus(_A)
_CfprPkiCertRevokeCrl_Type=SnmpAdminString
_CfprPkiCertRevokeCrl_Object=MibTableColumn
cfprPkiCertRevokeCrl=_CfprPkiCertRevokeCrl_Object((1,3,6,1,4,1,9,9,826,1,61,8,1,6),_CfprPkiCertRevokeCrl_Type())
cfprPkiCertRevokeCrl.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiCertRevokeCrl.setStatus(_A)
_CfprPkiCertRevokeCrlPollCount_Type=Gauge32
_CfprPkiCertRevokeCrlPollCount_Object=MibTableColumn
cfprPkiCertRevokeCrlPollCount=_CfprPkiCertRevokeCrlPollCount_Object((1,3,6,1,4,1,9,9,826,1,61,8,1,7),_CfprPkiCertRevokeCrlPollCount_Type())
cfprPkiCertRevokeCrlPollCount.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiCertRevokeCrlPollCount.setStatus(_A)
_CfprPkiCertRevokeCrlPollFilename_Type=SnmpAdminString
_CfprPkiCertRevokeCrlPollFilename_Object=MibTableColumn
cfprPkiCertRevokeCrlPollFilename=_CfprPkiCertRevokeCrlPollFilename_Object((1,3,6,1,4,1,9,9,826,1,61,8,1,8),_CfprPkiCertRevokeCrlPollFilename_Type())
cfprPkiCertRevokeCrlPollFilename.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiCertRevokeCrlPollFilename.setStatus(_A)
_CfprPkiCertRevokeCrlPollPeriod_Type=Gauge32
_CfprPkiCertRevokeCrlPollPeriod_Object=MibTableColumn
cfprPkiCertRevokeCrlPollPeriod=_CfprPkiCertRevokeCrlPollPeriod_Object((1,3,6,1,4,1,9,9,826,1,61,8,1,9),_CfprPkiCertRevokeCrlPollPeriod_Type())
cfprPkiCertRevokeCrlPollPeriod.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiCertRevokeCrlPollPeriod.setStatus(_A)
_CfprPkiCertRevokeCrlPollPort_Type=Gauge32
_CfprPkiCertRevokeCrlPollPort_Object=MibTableColumn
cfprPkiCertRevokeCrlPollPort=_CfprPkiCertRevokeCrlPollPort_Object((1,3,6,1,4,1,9,9,826,1,61,8,1,10),_CfprPkiCertRevokeCrlPollPort_Type())
cfprPkiCertRevokeCrlPollPort.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiCertRevokeCrlPollPort.setStatus(_A)
_CfprPkiCertRevokeCrlPollProtocol_Type=CfprPkiTransportNoLocal
_CfprPkiCertRevokeCrlPollProtocol_Object=MibTableColumn
cfprPkiCertRevokeCrlPollProtocol=_CfprPkiCertRevokeCrlPollProtocol_Object((1,3,6,1,4,1,9,9,826,1,61,8,1,11),_CfprPkiCertRevokeCrlPollProtocol_Type())
cfprPkiCertRevokeCrlPollProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiCertRevokeCrlPollProtocol.setStatus(_A)
_CfprPkiCertRevokeCrlPollPwd_Type=SnmpAdminString
_CfprPkiCertRevokeCrlPollPwd_Object=MibTableColumn
cfprPkiCertRevokeCrlPollPwd=_CfprPkiCertRevokeCrlPollPwd_Object((1,3,6,1,4,1,9,9,826,1,61,8,1,12),_CfprPkiCertRevokeCrlPollPwd_Type())
cfprPkiCertRevokeCrlPollPwd.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiCertRevokeCrlPollPwd.setStatus(_A)
_CfprPkiCertRevokeCrlPollRemotePath_Type=SnmpAdminString
_CfprPkiCertRevokeCrlPollRemotePath_Object=MibTableColumn
cfprPkiCertRevokeCrlPollRemotePath=_CfprPkiCertRevokeCrlPollRemotePath_Object((1,3,6,1,4,1,9,9,826,1,61,8,1,13),_CfprPkiCertRevokeCrlPollRemotePath_Type())
cfprPkiCertRevokeCrlPollRemotePath.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiCertRevokeCrlPollRemotePath.setStatus(_A)
_CfprPkiCertRevokeCrlPollServer_Type=SnmpAdminString
_CfprPkiCertRevokeCrlPollServer_Object=MibTableColumn
cfprPkiCertRevokeCrlPollServer=_CfprPkiCertRevokeCrlPollServer_Object((1,3,6,1,4,1,9,9,826,1,61,8,1,14),_CfprPkiCertRevokeCrlPollServer_Type())
cfprPkiCertRevokeCrlPollServer.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiCertRevokeCrlPollServer.setStatus(_A)
_CfprPkiCertRevokeCrlPollUser_Type=SnmpAdminString
_CfprPkiCertRevokeCrlPollUser_Object=MibTableColumn
cfprPkiCertRevokeCrlPollUser=_CfprPkiCertRevokeCrlPollUser_Object((1,3,6,1,4,1,9,9,826,1,61,8,1,15),_CfprPkiCertRevokeCrlPollUser_Type())
cfprPkiCertRevokeCrlPollUser.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiCertRevokeCrlPollUser.setStatus(_A)
_CfprPkiCertRevokeDescr_Type=SnmpAdminString
_CfprPkiCertRevokeDescr_Object=MibTableColumn
cfprPkiCertRevokeDescr=_CfprPkiCertRevokeDescr_Object((1,3,6,1,4,1,9,9,826,1,61,8,1,16),_CfprPkiCertRevokeDescr_Type())
cfprPkiCertRevokeDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiCertRevokeDescr.setStatus(_A)
_CfprPkiCertRevokeIntId_Type=SnmpAdminString
_CfprPkiCertRevokeIntId_Object=MibTableColumn
cfprPkiCertRevokeIntId=_CfprPkiCertRevokeIntId_Object((1,3,6,1,4,1,9,9,826,1,61,8,1,17),_CfprPkiCertRevokeIntId_Type())
cfprPkiCertRevokeIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiCertRevokeIntId.setStatus(_A)
_CfprPkiCertRevokeName_Type=SnmpAdminString
_CfprPkiCertRevokeName_Object=MibTableColumn
cfprPkiCertRevokeName=_CfprPkiCertRevokeName_Object((1,3,6,1,4,1,9,9,826,1,61,8,1,18),_CfprPkiCertRevokeName_Type())
cfprPkiCertRevokeName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiCertRevokeName.setStatus(_A)
_CfprPkiCertRevokePolicyLevel_Type=Gauge32
_CfprPkiCertRevokePolicyLevel_Object=MibTableColumn
cfprPkiCertRevokePolicyLevel=_CfprPkiCertRevokePolicyLevel_Object((1,3,6,1,4,1,9,9,826,1,61,8,1,19),_CfprPkiCertRevokePolicyLevel_Type())
cfprPkiCertRevokePolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiCertRevokePolicyLevel.setStatus(_A)
_CfprPkiCertRevokePolicyOwner_Type=CfprPolicyPolicyOwner
_CfprPkiCertRevokePolicyOwner_Object=MibTableColumn
cfprPkiCertRevokePolicyOwner=_CfprPkiCertRevokePolicyOwner_Object((1,3,6,1,4,1,9,9,826,1,61,8,1,20),_CfprPkiCertRevokePolicyOwner_Type())
cfprPkiCertRevokePolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiCertRevokePolicyOwner.setStatus(_A)
_CfprPkiImporterTable_Object=MibTable
cfprPkiImporterTable=_CfprPkiImporterTable_Object((1,3,6,1,4,1,9,9,826,1,61,9))
if mibBuilder.loadTexts:cfprPkiImporterTable.setStatus(_A)
_CfprPkiImporterEntry_Object=MibTableRow
cfprPkiImporterEntry=_CfprPkiImporterEntry_Object((1,3,6,1,4,1,9,9,826,1,61,9,1))
cfprPkiImporterEntry.setIndexNames((0,_C,_M))
if mibBuilder.loadTexts:cfprPkiImporterEntry.setStatus(_A)
_CfprPkiImporterInstanceId_Type=CfprManagedObjectId
_CfprPkiImporterInstanceId_Object=MibTableColumn
cfprPkiImporterInstanceId=_CfprPkiImporterInstanceId_Object((1,3,6,1,4,1,9,9,826,1,61,9,1,1),_CfprPkiImporterInstanceId_Type())
cfprPkiImporterInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprPkiImporterInstanceId.setStatus(_A)
_CfprPkiImporterDn_Type=CfprManagedObjectDn
_CfprPkiImporterDn_Object=MibTableColumn
cfprPkiImporterDn=_CfprPkiImporterDn_Object((1,3,6,1,4,1,9,9,826,1,61,9,1,2),_CfprPkiImporterDn_Type())
cfprPkiImporterDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiImporterDn.setStatus(_A)
_CfprPkiImporterRn_Type=SnmpAdminString
_CfprPkiImporterRn_Object=MibTableColumn
cfprPkiImporterRn=_CfprPkiImporterRn_Object((1,3,6,1,4,1,9,9,826,1,61,9,1,3),_CfprPkiImporterRn_Type())
cfprPkiImporterRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiImporterRn.setStatus(_A)
_CfprPkiImporterAdminState_Type=CfprPkiImportActivity
_CfprPkiImporterAdminState_Object=MibTableColumn
cfprPkiImporterAdminState=_CfprPkiImporterAdminState_Object((1,3,6,1,4,1,9,9,826,1,61,9,1,4),_CfprPkiImporterAdminState_Type())
cfprPkiImporterAdminState.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiImporterAdminState.setStatus(_A)
_CfprPkiImporterCertStatus_Type=CfprPkiCertStatus
_CfprPkiImporterCertStatus_Object=MibTableColumn
cfprPkiImporterCertStatus=_CfprPkiImporterCertStatus_Object((1,3,6,1,4,1,9,9,826,1,61,9,1,5),_CfprPkiImporterCertStatus_Type())
cfprPkiImporterCertStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiImporterCertStatus.setStatus(_A)
_CfprPkiImporterCrlSize_Type=Gauge32
_CfprPkiImporterCrlSize_Object=MibTableColumn
cfprPkiImporterCrlSize=_CfprPkiImporterCrlSize_Object((1,3,6,1,4,1,9,9,826,1,61,9,1,6),_CfprPkiImporterCrlSize_Type())
cfprPkiImporterCrlSize.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiImporterCrlSize.setStatus(_A)
_CfprPkiImporterDescr_Type=SnmpAdminString
_CfprPkiImporterDescr_Object=MibTableColumn
cfprPkiImporterDescr=_CfprPkiImporterDescr_Object((1,3,6,1,4,1,9,9,826,1,61,9,1,7),_CfprPkiImporterDescr_Type())
cfprPkiImporterDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiImporterDescr.setStatus(_A)
_CfprPkiImporterFileName_Type=SnmpAdminString
_CfprPkiImporterFileName_Object=MibTableColumn
cfprPkiImporterFileName=_CfprPkiImporterFileName_Object((1,3,6,1,4,1,9,9,826,1,61,9,1,8),_CfprPkiImporterFileName_Type())
cfprPkiImporterFileName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiImporterFileName.setStatus(_A)
_CfprPkiImporterIntId_Type=SnmpAdminString
_CfprPkiImporterIntId_Object=MibTableColumn
cfprPkiImporterIntId=_CfprPkiImporterIntId_Object((1,3,6,1,4,1,9,9,826,1,61,9,1,9),_CfprPkiImporterIntId_Type())
cfprPkiImporterIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiImporterIntId.setStatus(_A)
_CfprPkiImporterName_Type=SnmpAdminString
_CfprPkiImporterName_Object=MibTableColumn
cfprPkiImporterName=_CfprPkiImporterName_Object((1,3,6,1,4,1,9,9,826,1,61,9,1,10),_CfprPkiImporterName_Type())
cfprPkiImporterName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiImporterName.setStatus(_A)
_CfprPkiImporterPolicyLevel_Type=Gauge32
_CfprPkiImporterPolicyLevel_Object=MibTableColumn
cfprPkiImporterPolicyLevel=_CfprPkiImporterPolicyLevel_Object((1,3,6,1,4,1,9,9,826,1,61,9,1,11),_CfprPkiImporterPolicyLevel_Type())
cfprPkiImporterPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiImporterPolicyLevel.setStatus(_A)
_CfprPkiImporterPolicyOwner_Type=CfprPolicyPolicyOwner
_CfprPkiImporterPolicyOwner_Object=MibTableColumn
cfprPkiImporterPolicyOwner=_CfprPkiImporterPolicyOwner_Object((1,3,6,1,4,1,9,9,826,1,61,9,1,12),_CfprPkiImporterPolicyOwner_Type())
cfprPkiImporterPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiImporterPolicyOwner.setStatus(_A)
_CfprPkiImporterPort_Type=Gauge32
_CfprPkiImporterPort_Object=MibTableColumn
cfprPkiImporterPort=_CfprPkiImporterPort_Object((1,3,6,1,4,1,9,9,826,1,61,9,1,13),_CfprPkiImporterPort_Type())
cfprPkiImporterPort.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiImporterPort.setStatus(_A)
_CfprPkiImporterProtocol_Type=CfprPkiTransport
_CfprPkiImporterProtocol_Object=MibTableColumn
cfprPkiImporterProtocol=_CfprPkiImporterProtocol_Object((1,3,6,1,4,1,9,9,826,1,61,9,1,14),_CfprPkiImporterProtocol_Type())
cfprPkiImporterProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiImporterProtocol.setStatus(_A)
_CfprPkiImporterPwd_Type=SnmpAdminString
_CfprPkiImporterPwd_Object=MibTableColumn
cfprPkiImporterPwd=_CfprPkiImporterPwd_Object((1,3,6,1,4,1,9,9,826,1,61,9,1,15),_CfprPkiImporterPwd_Type())
cfprPkiImporterPwd.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiImporterPwd.setStatus(_A)
_CfprPkiImporterRemotePath_Type=SnmpAdminString
_CfprPkiImporterRemotePath_Object=MibTableColumn
cfprPkiImporterRemotePath=_CfprPkiImporterRemotePath_Object((1,3,6,1,4,1,9,9,826,1,61,9,1,16),_CfprPkiImporterRemotePath_Type())
cfprPkiImporterRemotePath.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiImporterRemotePath.setStatus(_A)
_CfprPkiImporterServer_Type=SnmpAdminString
_CfprPkiImporterServer_Object=MibTableColumn
cfprPkiImporterServer=_CfprPkiImporterServer_Object((1,3,6,1,4,1,9,9,826,1,61,9,1,17),_CfprPkiImporterServer_Type())
cfprPkiImporterServer.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiImporterServer.setStatus(_A)
_CfprPkiImporterTimeStamp_Type=DateAndTime
_CfprPkiImporterTimeStamp_Object=MibTableColumn
cfprPkiImporterTimeStamp=_CfprPkiImporterTimeStamp_Object((1,3,6,1,4,1,9,9,826,1,61,9,1,18),_CfprPkiImporterTimeStamp_Type())
cfprPkiImporterTimeStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiImporterTimeStamp.setStatus(_A)
_CfprPkiImporterTransferRate_Type=Integer32
_CfprPkiImporterTransferRate_Object=MibTableColumn
cfprPkiImporterTransferRate=_CfprPkiImporterTransferRate_Object((1,3,6,1,4,1,9,9,826,1,61,9,1,19),_CfprPkiImporterTransferRate_Type())
cfprPkiImporterTransferRate.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiImporterTransferRate.setStatus(_A)
_CfprPkiImporterTransferState_Type=CfprPkiTransferState
_CfprPkiImporterTransferState_Object=MibTableColumn
cfprPkiImporterTransferState=_CfprPkiImporterTransferState_Object((1,3,6,1,4,1,9,9,826,1,61,9,1,20),_CfprPkiImporterTransferState_Type())
cfprPkiImporterTransferState.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiImporterTransferState.setStatus(_A)
_CfprPkiImporterUser_Type=SnmpAdminString
_CfprPkiImporterUser_Object=MibTableColumn
cfprPkiImporterUser=_CfprPkiImporterUser_Object((1,3,6,1,4,1,9,9,826,1,61,9,1,21),_CfprPkiImporterUser_Type())
cfprPkiImporterUser.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiImporterUser.setStatus(_A)
_CfprPkiTpAutoImportTable_Object=MibTable
cfprPkiTpAutoImportTable=_CfprPkiTpAutoImportTable_Object((1,3,6,1,4,1,9,9,826,1,61,10))
if mibBuilder.loadTexts:cfprPkiTpAutoImportTable.setStatus(_A)
_CfprPkiTpAutoImportEntry_Object=MibTableRow
cfprPkiTpAutoImportEntry=_CfprPkiTpAutoImportEntry_Object((1,3,6,1,4,1,9,9,826,1,61,10,1))
cfprPkiTpAutoImportEntry.setIndexNames((0,_C,_N))
if mibBuilder.loadTexts:cfprPkiTpAutoImportEntry.setStatus(_A)
_CfprPkiTpAutoImportInstanceId_Type=CfprManagedObjectId
_CfprPkiTpAutoImportInstanceId_Object=MibTableColumn
cfprPkiTpAutoImportInstanceId=_CfprPkiTpAutoImportInstanceId_Object((1,3,6,1,4,1,9,9,826,1,61,10,1,1),_CfprPkiTpAutoImportInstanceId_Type())
cfprPkiTpAutoImportInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprPkiTpAutoImportInstanceId.setStatus(_A)
_CfprPkiTpAutoImportDn_Type=CfprManagedObjectDn
_CfprPkiTpAutoImportDn_Object=MibTableColumn
cfprPkiTpAutoImportDn=_CfprPkiTpAutoImportDn_Object((1,3,6,1,4,1,9,9,826,1,61,10,1,2),_CfprPkiTpAutoImportDn_Type())
cfprPkiTpAutoImportDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiTpAutoImportDn.setStatus(_A)
_CfprPkiTpAutoImportRn_Type=SnmpAdminString
_CfprPkiTpAutoImportRn_Object=MibTableColumn
cfprPkiTpAutoImportRn=_CfprPkiTpAutoImportRn_Object((1,3,6,1,4,1,9,9,826,1,61,10,1,3),_CfprPkiTpAutoImportRn_Type())
cfprPkiTpAutoImportRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiTpAutoImportRn.setStatus(_A)
_CfprPkiTpAutoImportCertStatus_Type=CfprPkiCertStatus
_CfprPkiTpAutoImportCertStatus_Object=MibTableColumn
cfprPkiTpAutoImportCertStatus=_CfprPkiTpAutoImportCertStatus_Object((1,3,6,1,4,1,9,9,826,1,61,10,1,4),_CfprPkiTpAutoImportCertStatus_Type())
cfprPkiTpAutoImportCertStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiTpAutoImportCertStatus.setStatus(_A)
_CfprPkiTpAutoImportDayRun_Type=TruthValue
_CfprPkiTpAutoImportDayRun_Object=MibTableColumn
cfprPkiTpAutoImportDayRun=_CfprPkiTpAutoImportDayRun_Object((1,3,6,1,4,1,9,9,826,1,61,10,1,5),_CfprPkiTpAutoImportDayRun_Type())
cfprPkiTpAutoImportDayRun.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiTpAutoImportDayRun.setStatus(_A)
_CfprPkiTpAutoImportDescr_Type=SnmpAdminString
_CfprPkiTpAutoImportDescr_Object=MibTableColumn
cfprPkiTpAutoImportDescr=_CfprPkiTpAutoImportDescr_Object((1,3,6,1,4,1,9,9,826,1,61,10,1,6),_CfprPkiTpAutoImportDescr_Type())
cfprPkiTpAutoImportDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiTpAutoImportDescr.setStatus(_A)
_CfprPkiTpAutoImportImportControlStatus_Type=CfprPkiTpAutoImportImportControlStatus
_CfprPkiTpAutoImportImportControlStatus_Object=MibTableColumn
cfprPkiTpAutoImportImportControlStatus=_CfprPkiTpAutoImportImportControlStatus_Object((1,3,6,1,4,1,9,9,826,1,61,10,1,7),_CfprPkiTpAutoImportImportControlStatus_Type())
cfprPkiTpAutoImportImportControlStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiTpAutoImportImportControlStatus.setStatus(_A)
_CfprPkiTpAutoImportImportStatus_Type=TruthValue
_CfprPkiTpAutoImportImportStatus_Object=MibTableColumn
cfprPkiTpAutoImportImportStatus=_CfprPkiTpAutoImportImportStatus_Object((1,3,6,1,4,1,9,9,826,1,61,10,1,8),_CfprPkiTpAutoImportImportStatus_Type())
cfprPkiTpAutoImportImportStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiTpAutoImportImportStatus.setStatus(_A)
_CfprPkiTpAutoImportImportTimeHour_Type=Gauge32
_CfprPkiTpAutoImportImportTimeHour_Object=MibTableColumn
cfprPkiTpAutoImportImportTimeHour=_CfprPkiTpAutoImportImportTimeHour_Object((1,3,6,1,4,1,9,9,826,1,61,10,1,9),_CfprPkiTpAutoImportImportTimeHour_Type())
cfprPkiTpAutoImportImportTimeHour.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiTpAutoImportImportTimeHour.setStatus(_A)
_CfprPkiTpAutoImportImportTimeMin_Type=Gauge32
_CfprPkiTpAutoImportImportTimeMin_Object=MibTableColumn
cfprPkiTpAutoImportImportTimeMin=_CfprPkiTpAutoImportImportTimeMin_Object((1,3,6,1,4,1,9,9,826,1,61,10,1,10),_CfprPkiTpAutoImportImportTimeMin_Type())
cfprPkiTpAutoImportImportTimeMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiTpAutoImportImportTimeMin.setStatus(_A)
_CfprPkiTpAutoImportImportUrl_Type=SnmpAdminString
_CfprPkiTpAutoImportImportUrl_Object=MibTableColumn
cfprPkiTpAutoImportImportUrl=_CfprPkiTpAutoImportImportUrl_Object((1,3,6,1,4,1,9,9,826,1,61,10,1,11),_CfprPkiTpAutoImportImportUrl_Type())
cfprPkiTpAutoImportImportUrl.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiTpAutoImportImportUrl.setStatus(_A)
_CfprPkiTpAutoImportIntId_Type=SnmpAdminString
_CfprPkiTpAutoImportIntId_Object=MibTableColumn
cfprPkiTpAutoImportIntId=_CfprPkiTpAutoImportIntId_Object((1,3,6,1,4,1,9,9,826,1,61,10,1,12),_CfprPkiTpAutoImportIntId_Type())
cfprPkiTpAutoImportIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiTpAutoImportIntId.setStatus(_A)
_CfprPkiTpAutoImportName_Type=SnmpAdminString
_CfprPkiTpAutoImportName_Object=MibTableColumn
cfprPkiTpAutoImportName=_CfprPkiTpAutoImportName_Object((1,3,6,1,4,1,9,9,826,1,61,10,1,13),_CfprPkiTpAutoImportName_Type())
cfprPkiTpAutoImportName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiTpAutoImportName.setStatus(_A)
_CfprPkiTpAutoImportNumExtractedTpAutoImport_Type=Gauge32
_CfprPkiTpAutoImportNumExtractedTpAutoImport_Object=MibTableColumn
cfprPkiTpAutoImportNumExtractedTpAutoImport=_CfprPkiTpAutoImportNumExtractedTpAutoImport_Object((1,3,6,1,4,1,9,9,826,1,61,10,1,14),_CfprPkiTpAutoImportNumExtractedTpAutoImport_Type())
cfprPkiTpAutoImportNumExtractedTpAutoImport.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiTpAutoImportNumExtractedTpAutoImport.setStatus(_A)
_CfprPkiTpAutoImportNumTpAutoImport_Type=Gauge32
_CfprPkiTpAutoImportNumTpAutoImport_Object=MibTableColumn
cfprPkiTpAutoImportNumTpAutoImport=_CfprPkiTpAutoImportNumTpAutoImport_Object((1,3,6,1,4,1,9,9,826,1,61,10,1,15),_CfprPkiTpAutoImportNumTpAutoImport_Type())
cfprPkiTpAutoImportNumTpAutoImport.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiTpAutoImportNumTpAutoImport.setStatus(_A)
_CfprPkiTpAutoImportPolicyLevel_Type=Gauge32
_CfprPkiTpAutoImportPolicyLevel_Object=MibTableColumn
cfprPkiTpAutoImportPolicyLevel=_CfprPkiTpAutoImportPolicyLevel_Object((1,3,6,1,4,1,9,9,826,1,61,10,1,16),_CfprPkiTpAutoImportPolicyLevel_Type())
cfprPkiTpAutoImportPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiTpAutoImportPolicyLevel.setStatus(_A)
_CfprPkiTpAutoImportPolicyOwner_Type=CfprPolicyPolicyOwner
_CfprPkiTpAutoImportPolicyOwner_Object=MibTableColumn
cfprPkiTpAutoImportPolicyOwner=_CfprPkiTpAutoImportPolicyOwner_Object((1,3,6,1,4,1,9,9,826,1,61,10,1,17),_CfprPkiTpAutoImportPolicyOwner_Type())
cfprPkiTpAutoImportPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiTpAutoImportPolicyOwner.setStatus(_A)
_CfprPkiTpAutoImportRetryCount_Type=Gauge32
_CfprPkiTpAutoImportRetryCount_Object=MibTableColumn
cfprPkiTpAutoImportRetryCount=_CfprPkiTpAutoImportRetryCount_Object((1,3,6,1,4,1,9,9,826,1,61,10,1,18),_CfprPkiTpAutoImportRetryCount_Type())
cfprPkiTpAutoImportRetryCount.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiTpAutoImportRetryCount.setStatus(_A)
_CfprPkiTpAutoImportRetryDelay_Type=Gauge32
_CfprPkiTpAutoImportRetryDelay_Object=MibTableColumn
cfprPkiTpAutoImportRetryDelay=_CfprPkiTpAutoImportRetryDelay_Object((1,3,6,1,4,1,9,9,826,1,61,10,1,19),_CfprPkiTpAutoImportRetryDelay_Type())
cfprPkiTpAutoImportRetryDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiTpAutoImportRetryDelay.setStatus(_A)
_CfprPkiTpAutoImportTriggerRun_Type=TruthValue
_CfprPkiTpAutoImportTriggerRun_Object=MibTableColumn
cfprPkiTpAutoImportTriggerRun=_CfprPkiTpAutoImportTriggerRun_Object((1,3,6,1,4,1,9,9,826,1,61,10,1,20),_CfprPkiTpAutoImportTriggerRun_Type())
cfprPkiTpAutoImportTriggerRun.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprPkiTpAutoImportTriggerRun.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'cfprPkiObjects':cfprPkiObjects,'cfprPkiCertReqTable':cfprPkiCertReqTable,'cfprPkiCertReqEntry':cfprPkiCertReqEntry,_E:cfprPkiCertReqInstanceId,'cfprPkiCertReqDn':cfprPkiCertReqDn,'cfprPkiCertReqRn':cfprPkiCertReqRn,'cfprPkiCertReqCountry':cfprPkiCertReqCountry,'cfprPkiCertReqDns':cfprPkiCertReqDns,'cfprPkiCertReqEmail':cfprPkiCertReqEmail,'cfprPkiCertReqIp':cfprPkiCertReqIp,'cfprPkiCertReqIpA':cfprPkiCertReqIpA,'cfprPkiCertReqIpB':cfprPkiCertReqIpB,'cfprPkiCertReqIpv6':cfprPkiCertReqIpv6,'cfprPkiCertReqIpv6A':cfprPkiCertReqIpv6A,'cfprPkiCertReqIpv6B':cfprPkiCertReqIpv6B,'cfprPkiCertReqLocality':cfprPkiCertReqLocality,'cfprPkiCertReqOrgName':cfprPkiCertReqOrgName,'cfprPkiCertReqOrgUnitName':cfprPkiCertReqOrgUnitName,'cfprPkiCertReqPwd':cfprPkiCertReqPwd,'cfprPkiCertReqReq':cfprPkiCertReqReq,'cfprPkiCertReqState':cfprPkiCertReqState,'cfprPkiCertReqSubjName':cfprPkiCertReqSubjName,'cfprPkiEpTable':cfprPkiEpTable,'cfprPkiEpEntry':cfprPkiEpEntry,_F:cfprPkiEpInstanceId,'cfprPkiEpDn':cfprPkiEpDn,'cfprPkiEpRn':cfprPkiEpRn,'cfprPkiEpDescr':cfprPkiEpDescr,'cfprPkiEpFsmDescr':cfprPkiEpFsmDescr,'cfprPkiEpFsmPrev':cfprPkiEpFsmPrev,'cfprPkiEpFsmProgr':cfprPkiEpFsmProgr,'cfprPkiEpFsmRmtInvErrCode':cfprPkiEpFsmRmtInvErrCode,'cfprPkiEpFsmRmtInvErrDescr':cfprPkiEpFsmRmtInvErrDescr,'cfprPkiEpFsmRmtInvRslt':cfprPkiEpFsmRmtInvRslt,'cfprPkiEpFsmStageDescr':cfprPkiEpFsmStageDescr,'cfprPkiEpFsmStamp':cfprPkiEpFsmStamp,'cfprPkiEpFsmStatus':cfprPkiEpFsmStatus,'cfprPkiEpFsmTry':cfprPkiEpFsmTry,'cfprPkiEpIntId':cfprPkiEpIntId,'cfprPkiEpName':cfprPkiEpName,'cfprPkiEpPolicyLevel':cfprPkiEpPolicyLevel,'cfprPkiEpPolicyOwner':cfprPkiEpPolicyOwner,'cfprPkiEpFsmTable':cfprPkiEpFsmTable,'cfprPkiEpFsmEntry':cfprPkiEpFsmEntry,_G:cfprPkiEpFsmInstanceId,'cfprPkiEpFsmDn':cfprPkiEpFsmDn,'cfprPkiEpFsmRn':cfprPkiEpFsmRn,'cfprPkiEpFsmCompletionTime':cfprPkiEpFsmCompletionTime,'cfprPkiEpFsmCurrentFsm':cfprPkiEpFsmCurrentFsm,'cfprPkiEpFsmDescrData':cfprPkiEpFsmDescrData,'cfprPkiEpFsmFsmStatus':cfprPkiEpFsmFsmStatus,'cfprPkiEpFsmProgress':cfprPkiEpFsmProgress,'cfprPkiEpFsmRmtErrCode':cfprPkiEpFsmRmtErrCode,'cfprPkiEpFsmRmtErrDescr':cfprPkiEpFsmRmtErrDescr,'cfprPkiEpFsmRmtRslt':cfprPkiEpFsmRmtRslt,'cfprPkiEpFsmStageTable':cfprPkiEpFsmStageTable,'cfprPkiEpFsmStageEntry':cfprPkiEpFsmStageEntry,_H:cfprPkiEpFsmStageInstanceId,'cfprPkiEpFsmStageDn':cfprPkiEpFsmStageDn,'cfprPkiEpFsmStageRn':cfprPkiEpFsmStageRn,'cfprPkiEpFsmStageDescrData':cfprPkiEpFsmStageDescrData,'cfprPkiEpFsmStageLastUpdateTime':cfprPkiEpFsmStageLastUpdateTime,'cfprPkiEpFsmStageName':cfprPkiEpFsmStageName,'cfprPkiEpFsmStageOrder':cfprPkiEpFsmStageOrder,'cfprPkiEpFsmStageRetry':cfprPkiEpFsmStageRetry,'cfprPkiEpFsmStageStageStatus':cfprPkiEpFsmStageStageStatus,'cfprPkiEpFsmTaskTable':cfprPkiEpFsmTaskTable,'cfprPkiEpFsmTaskEntry':cfprPkiEpFsmTaskEntry,_I:cfprPkiEpFsmTaskInstanceId,'cfprPkiEpFsmTaskDn':cfprPkiEpFsmTaskDn,'cfprPkiEpFsmTaskRn':cfprPkiEpFsmTaskRn,'cfprPkiEpFsmTaskCompletion':cfprPkiEpFsmTaskCompletion,'cfprPkiEpFsmTaskFlags':cfprPkiEpFsmTaskFlags,'cfprPkiEpFsmTaskItem':cfprPkiEpFsmTaskItem,'cfprPkiEpFsmTaskSeqId':cfprPkiEpFsmTaskSeqId,'cfprPkiKeyRingTable':cfprPkiKeyRingTable,'cfprPkiKeyRingEntry':cfprPkiKeyRingEntry,_J:cfprPkiKeyRingInstanceId,'cfprPkiKeyRingDn':cfprPkiKeyRingDn,'cfprPkiKeyRingRn':cfprPkiKeyRingRn,'cfprPkiKeyRingAdminState':cfprPkiKeyRingAdminState,'cfprPkiKeyRingCert':cfprPkiKeyRingCert,'cfprPkiKeyRingCertStatus':cfprPkiKeyRingCertStatus,'cfprPkiKeyRingConfigState':cfprPkiKeyRingConfigState,'cfprPkiKeyRingConfigStatusMessage':cfprPkiKeyRingConfigStatusMessage,'cfprPkiKeyRingDescr':cfprPkiKeyRingDescr,'cfprPkiKeyRingIntId':cfprPkiKeyRingIntId,'cfprPkiKeyRingKey':cfprPkiKeyRingKey,'cfprPkiKeyRingModulus':cfprPkiKeyRingModulus,'cfprPkiKeyRingName':cfprPkiKeyRingName,'cfprPkiKeyRingPolicyLevel':cfprPkiKeyRingPolicyLevel,'cfprPkiKeyRingPolicyOwner':cfprPkiKeyRingPolicyOwner,'cfprPkiKeyRingRegen':cfprPkiKeyRingRegen,'cfprPkiKeyRingTp':cfprPkiKeyRingTp,'cfprPkiKeyRingZeroized':cfprPkiKeyRingZeroized,'cfprPkiKeyRingEc':cfprPkiKeyRingEc,'cfprPkiKeyRingType':cfprPkiKeyRingType,'cfprPkiTPTable':cfprPkiTPTable,'cfprPkiTPEntry':cfprPkiTPEntry,_K:cfprPkiTPInstanceId,'cfprPkiTPDn':cfprPkiTPDn,'cfprPkiTPRn':cfprPkiTPRn,'cfprPkiTPCertChain':cfprPkiTPCertChain,'cfprPkiTPCertStatus':cfprPkiTPCertStatus,'cfprPkiTPDescr':cfprPkiTPDescr,'cfprPkiTPFp':cfprPkiTPFp,'cfprPkiTPIntId':cfprPkiTPIntId,'cfprPkiTPName':cfprPkiTPName,'cfprPkiTPNumCerts':cfprPkiTPNumCerts,'cfprPkiTPPolicyLevel':cfprPkiTPPolicyLevel,'cfprPkiTPPolicyOwner':cfprPkiTPPolicyOwner,'cfprPkiTPCertChainDecode':cfprPkiTPCertChainDecode,'cfprPkiCertRevokeTable':cfprPkiCertRevokeTable,'cfprPkiCertRevokeEntry':cfprPkiCertRevokeEntry,_L:cfprPkiCertRevokeInstanceId,'cfprPkiCertRevokeDn':cfprPkiCertRevokeDn,'cfprPkiCertRevokeRn':cfprPkiCertRevokeRn,'cfprPkiCertRevokeCertRevokeMethod':cfprPkiCertRevokeCertRevokeMethod,'cfprPkiCertRevokeCertStatus':cfprPkiCertRevokeCertStatus,'cfprPkiCertRevokeCrl':cfprPkiCertRevokeCrl,'cfprPkiCertRevokeCrlPollCount':cfprPkiCertRevokeCrlPollCount,'cfprPkiCertRevokeCrlPollFilename':cfprPkiCertRevokeCrlPollFilename,'cfprPkiCertRevokeCrlPollPeriod':cfprPkiCertRevokeCrlPollPeriod,'cfprPkiCertRevokeCrlPollPort':cfprPkiCertRevokeCrlPollPort,'cfprPkiCertRevokeCrlPollProtocol':cfprPkiCertRevokeCrlPollProtocol,'cfprPkiCertRevokeCrlPollPwd':cfprPkiCertRevokeCrlPollPwd,'cfprPkiCertRevokeCrlPollRemotePath':cfprPkiCertRevokeCrlPollRemotePath,'cfprPkiCertRevokeCrlPollServer':cfprPkiCertRevokeCrlPollServer,'cfprPkiCertRevokeCrlPollUser':cfprPkiCertRevokeCrlPollUser,'cfprPkiCertRevokeDescr':cfprPkiCertRevokeDescr,'cfprPkiCertRevokeIntId':cfprPkiCertRevokeIntId,'cfprPkiCertRevokeName':cfprPkiCertRevokeName,'cfprPkiCertRevokePolicyLevel':cfprPkiCertRevokePolicyLevel,'cfprPkiCertRevokePolicyOwner':cfprPkiCertRevokePolicyOwner,'cfprPkiImporterTable':cfprPkiImporterTable,'cfprPkiImporterEntry':cfprPkiImporterEntry,_M:cfprPkiImporterInstanceId,'cfprPkiImporterDn':cfprPkiImporterDn,'cfprPkiImporterRn':cfprPkiImporterRn,'cfprPkiImporterAdminState':cfprPkiImporterAdminState,'cfprPkiImporterCertStatus':cfprPkiImporterCertStatus,'cfprPkiImporterCrlSize':cfprPkiImporterCrlSize,'cfprPkiImporterDescr':cfprPkiImporterDescr,'cfprPkiImporterFileName':cfprPkiImporterFileName,'cfprPkiImporterIntId':cfprPkiImporterIntId,'cfprPkiImporterName':cfprPkiImporterName,'cfprPkiImporterPolicyLevel':cfprPkiImporterPolicyLevel,'cfprPkiImporterPolicyOwner':cfprPkiImporterPolicyOwner,'cfprPkiImporterPort':cfprPkiImporterPort,'cfprPkiImporterProtocol':cfprPkiImporterProtocol,'cfprPkiImporterPwd':cfprPkiImporterPwd,'cfprPkiImporterRemotePath':cfprPkiImporterRemotePath,'cfprPkiImporterServer':cfprPkiImporterServer,'cfprPkiImporterTimeStamp':cfprPkiImporterTimeStamp,'cfprPkiImporterTransferRate':cfprPkiImporterTransferRate,'cfprPkiImporterTransferState':cfprPkiImporterTransferState,'cfprPkiImporterUser':cfprPkiImporterUser,'cfprPkiTpAutoImportTable':cfprPkiTpAutoImportTable,'cfprPkiTpAutoImportEntry':cfprPkiTpAutoImportEntry,_N:cfprPkiTpAutoImportInstanceId,'cfprPkiTpAutoImportDn':cfprPkiTpAutoImportDn,'cfprPkiTpAutoImportRn':cfprPkiTpAutoImportRn,'cfprPkiTpAutoImportCertStatus':cfprPkiTpAutoImportCertStatus,'cfprPkiTpAutoImportDayRun':cfprPkiTpAutoImportDayRun,'cfprPkiTpAutoImportDescr':cfprPkiTpAutoImportDescr,'cfprPkiTpAutoImportImportControlStatus':cfprPkiTpAutoImportImportControlStatus,'cfprPkiTpAutoImportImportStatus':cfprPkiTpAutoImportImportStatus,'cfprPkiTpAutoImportImportTimeHour':cfprPkiTpAutoImportImportTimeHour,'cfprPkiTpAutoImportImportTimeMin':cfprPkiTpAutoImportImportTimeMin,'cfprPkiTpAutoImportImportUrl':cfprPkiTpAutoImportImportUrl,'cfprPkiTpAutoImportIntId':cfprPkiTpAutoImportIntId,'cfprPkiTpAutoImportName':cfprPkiTpAutoImportName,'cfprPkiTpAutoImportNumExtractedTpAutoImport':cfprPkiTpAutoImportNumExtractedTpAutoImport,'cfprPkiTpAutoImportNumTpAutoImport':cfprPkiTpAutoImportNumTpAutoImport,'cfprPkiTpAutoImportPolicyLevel':cfprPkiTpAutoImportPolicyLevel,'cfprPkiTpAutoImportPolicyOwner':cfprPkiTpAutoImportPolicyOwner,'cfprPkiTpAutoImportRetryCount':cfprPkiTpAutoImportRetryCount,'cfprPkiTpAutoImportRetryDelay':cfprPkiTpAutoImportRetryDelay,'cfprPkiTpAutoImportTriggerRun':cfprPkiTpAutoImportTriggerRun})