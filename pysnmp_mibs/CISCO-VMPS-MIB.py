_w='ciscoVlanMemberPolicyServerRcpGroup2'
_v='ciscoVlanMemberPolicyServerRcpGroup'
_u='vmpsRcpRemoteUserName2'
_t='vmpsAutoBackupFileName'
_s='vmpsAutoBackupEnable'
_r='vmpsRcpRemoteUserName'
_q='vmpsVlanConfigStatus'
_p='vmpsMacConfigStatus'
_o='vmpsMacConfigLastResponseStatus'
_n='vmpsMacConfigLastRequestPortId'
_m='vmpsMacConfigLastRequestor'
_l='vmpsMacConfigLastAccessed'
_k='vmpsMacConfigVlan'
_j='vmpsRowStatus'
_i='vmpsManagementDomain'
_h='vmpsSecureMode'
_g='vmpsFallbackVlan'
_f='vmpsTriggerDownload'
_e='vmpsConfigFileName'
_d='vmpsDownloadServerAddress'
_c='vmpsAdminStatus'
_b='vmpsOperStatus'
_a='vmpsLastFailClient'
_Z='vmpsOutConfigFails'
_Y='vmpsInConfigErrors'
_X='vmpsInConfigReqs'
_W='vmpsLastRestart'
_V='vmpsStatsEntry'
_U='read-write'
_T='vmpsPortName'
_S='vmpsDeviceId'
_R='vmpsVlanName'
_Q='vmpsMacConfigAddress'
_P='VlanName'
_O='inactive'
_N='active'
_M='IpAddress'
_L='SnmpAdminString'
_K='ciscoVmpsAutoBackupGroup'
_J='DisplayString'
_I='ciscoVlanMemberPolicyServerGroup'
_H='deprecated'
_G='vmpsIndex'
_F='not-accessible'
_E='Integer32'
_D='read-only'
_C='read-create'
_B='CISCO-VMPS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_L)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,_M,'ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_J,'MacAddress','PhysAddress','RowStatus','TextualConvention','TimeStamp','TruthValue')
ciscoVmpsMIB=ModuleIdentity((1,3,6,1,4,1,9,9,53))
if mibBuilder.loadTexts:ciscoVmpsMIB.setRevisions(('2004-01-20 00:00','2003-10-16 10:00','2002-06-19 10:00','2002-04-04 10:00','2001-01-30 13:04'))
class VlanName(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CiscoVlanMemberPolicyServerMIBObjects_ObjectIdentity=ObjectIdentity
ciscoVlanMemberPolicyServerMIBObjects=_CiscoVlanMemberPolicyServerMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,53,1))
_VmpsInfo_ObjectIdentity=ObjectIdentity
vmpsInfo=_VmpsInfo_ObjectIdentity((1,3,6,1,4,1,9,9,53,1,1))
_VmpsConfigTable_Object=MibTable
vmpsConfigTable=_VmpsConfigTable_Object((1,3,6,1,4,1,9,9,53,1,1,1))
if mibBuilder.loadTexts:vmpsConfigTable.setStatus(_A)
_VmpsConfigEntry_Object=MibTableRow
vmpsConfigEntry=_VmpsConfigEntry_Object((1,3,6,1,4,1,9,9,53,1,1,1,1))
vmpsConfigEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:vmpsConfigEntry.setStatus(_A)
class _VmpsIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_VmpsIndex_Type.__name__=_E
_VmpsIndex_Object=MibTableColumn
vmpsIndex=_VmpsIndex_Object((1,3,6,1,4,1,9,9,53,1,1,1,1,1),_VmpsIndex_Type())
vmpsIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:vmpsIndex.setStatus(_A)
class _VmpsAdminStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_O,2)))
_VmpsAdminStatus_Type.__name__=_E
_VmpsAdminStatus_Object=MibTableColumn
vmpsAdminStatus=_VmpsAdminStatus_Object((1,3,6,1,4,1,9,9,53,1,1,1,1,2),_VmpsAdminStatus_Type())
vmpsAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:vmpsAdminStatus.setStatus(_A)
class _VmpsDownloadServerAddress_Type(IpAddress):defaultHexValue='00000000'
_VmpsDownloadServerAddress_Type.__name__=_M
_VmpsDownloadServerAddress_Object=MibTableColumn
vmpsDownloadServerAddress=_VmpsDownloadServerAddress_Object((1,3,6,1,4,1,9,9,53,1,1,1,1,3),_VmpsDownloadServerAddress_Type())
vmpsDownloadServerAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:vmpsDownloadServerAddress.setStatus(_A)
class _VmpsConfigFileName_Type(DisplayString):defaultHexValue=''
_VmpsConfigFileName_Type.__name__=_J
_VmpsConfigFileName_Object=MibTableColumn
vmpsConfigFileName=_VmpsConfigFileName_Object((1,3,6,1,4,1,9,9,53,1,1,1,1,4),_VmpsConfigFileName_Type())
vmpsConfigFileName.setMaxAccess(_C)
if mibBuilder.loadTexts:vmpsConfigFileName.setStatus(_A)
class _VmpsTriggerDownload_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('noOperation',1),('loadDatabase',2),('loadRcpDataBase',3)))
_VmpsTriggerDownload_Type.__name__=_E
_VmpsTriggerDownload_Object=MibTableColumn
vmpsTriggerDownload=_VmpsTriggerDownload_Object((1,3,6,1,4,1,9,9,53,1,1,1,1,5),_VmpsTriggerDownload_Type())
vmpsTriggerDownload.setMaxAccess(_C)
if mibBuilder.loadTexts:vmpsTriggerDownload.setStatus(_A)
class _VmpsFallbackVlan_Type(VlanName):defaultHexValue=''
_VmpsFallbackVlan_Type.__name__=_P
_VmpsFallbackVlan_Object=MibTableColumn
vmpsFallbackVlan=_VmpsFallbackVlan_Object((1,3,6,1,4,1,9,9,53,1,1,1,1,6),_VmpsFallbackVlan_Type())
vmpsFallbackVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:vmpsFallbackVlan.setStatus(_A)
class _VmpsSecureMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('secure',1),('open',2)))
_VmpsSecureMode_Type.__name__=_E
_VmpsSecureMode_Object=MibTableColumn
vmpsSecureMode=_VmpsSecureMode_Object((1,3,6,1,4,1,9,9,53,1,1,1,1,7),_VmpsSecureMode_Type())
vmpsSecureMode.setMaxAccess(_C)
if mibBuilder.loadTexts:vmpsSecureMode.setStatus(_A)
class _VmpsManagementDomain_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_VmpsManagementDomain_Type.__name__=_J
_VmpsManagementDomain_Object=MibTableColumn
vmpsManagementDomain=_VmpsManagementDomain_Object((1,3,6,1,4,1,9,9,53,1,1,1,1,8),_VmpsManagementDomain_Type())
vmpsManagementDomain.setMaxAccess(_C)
if mibBuilder.loadTexts:vmpsManagementDomain.setStatus(_A)
_VmpsRowStatus_Type=RowStatus
_VmpsRowStatus_Object=MibTableColumn
vmpsRowStatus=_VmpsRowStatus_Object((1,3,6,1,4,1,9,9,53,1,1,1,1,9),_VmpsRowStatus_Type())
vmpsRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:vmpsRowStatus.setStatus(_A)
class _VmpsRcpRemoteUserName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_VmpsRcpRemoteUserName_Type.__name__=_L
_VmpsRcpRemoteUserName_Object=MibTableColumn
vmpsRcpRemoteUserName=_VmpsRcpRemoteUserName_Object((1,3,6,1,4,1,9,9,53,1,1,1,1,10),_VmpsRcpRemoteUserName_Type())
vmpsRcpRemoteUserName.setMaxAccess(_C)
if mibBuilder.loadTexts:vmpsRcpRemoteUserName.setStatus(_H)
_VmpsRcpRemoteUserName2_Type=SnmpAdminString
_VmpsRcpRemoteUserName2_Object=MibTableColumn
vmpsRcpRemoteUserName2=_VmpsRcpRemoteUserName2_Object((1,3,6,1,4,1,9,9,53,1,1,1,1,11),_VmpsRcpRemoteUserName2_Type())
vmpsRcpRemoteUserName2.setMaxAccess(_C)
if mibBuilder.loadTexts:vmpsRcpRemoteUserName2.setStatus(_A)
_VmpsStatsTable_Object=MibTable
vmpsStatsTable=_VmpsStatsTable_Object((1,3,6,1,4,1,9,9,53,1,1,2))
if mibBuilder.loadTexts:vmpsStatsTable.setStatus(_A)
_VmpsStatsEntry_Object=MibTableRow
vmpsStatsEntry=_VmpsStatsEntry_Object((1,3,6,1,4,1,9,9,53,1,1,2,1))
if mibBuilder.loadTexts:vmpsStatsEntry.setStatus(_A)
_VmpsLastRestart_Type=TimeStamp
_VmpsLastRestart_Object=MibTableColumn
vmpsLastRestart=_VmpsLastRestart_Object((1,3,6,1,4,1,9,9,53,1,1,2,1,1),_VmpsLastRestart_Type())
vmpsLastRestart.setMaxAccess(_D)
if mibBuilder.loadTexts:vmpsLastRestart.setStatus(_A)
_VmpsInConfigReqs_Type=Counter32
_VmpsInConfigReqs_Object=MibTableColumn
vmpsInConfigReqs=_VmpsInConfigReqs_Object((1,3,6,1,4,1,9,9,53,1,1,2,1,2),_VmpsInConfigReqs_Type())
vmpsInConfigReqs.setMaxAccess(_D)
if mibBuilder.loadTexts:vmpsInConfigReqs.setStatus(_A)
_VmpsInConfigErrors_Type=Counter32
_VmpsInConfigErrors_Object=MibTableColumn
vmpsInConfigErrors=_VmpsInConfigErrors_Object((1,3,6,1,4,1,9,9,53,1,1,2,1,3),_VmpsInConfigErrors_Type())
vmpsInConfigErrors.setMaxAccess(_D)
if mibBuilder.loadTexts:vmpsInConfigErrors.setStatus(_A)
_VmpsOutConfigFails_Type=Counter32
_VmpsOutConfigFails_Object=MibTableColumn
vmpsOutConfigFails=_VmpsOutConfigFails_Object((1,3,6,1,4,1,9,9,53,1,1,2,1,4),_VmpsOutConfigFails_Type())
vmpsOutConfigFails.setMaxAccess(_D)
if mibBuilder.loadTexts:vmpsOutConfigFails.setStatus(_A)
_VmpsLastFailClient_Type=MacAddress
_VmpsLastFailClient_Object=MibTableColumn
vmpsLastFailClient=_VmpsLastFailClient_Object((1,3,6,1,4,1,9,9,53,1,1,2,1,5),_VmpsLastFailClient_Type())
vmpsLastFailClient.setMaxAccess(_D)
if mibBuilder.loadTexts:vmpsLastFailClient.setStatus(_A)
class _VmpsOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_N,1),(_O,2),('loading',3)))
_VmpsOperStatus_Type.__name__=_E
_VmpsOperStatus_Object=MibTableColumn
vmpsOperStatus=_VmpsOperStatus_Object((1,3,6,1,4,1,9,9,53,1,1,2,1,6),_VmpsOperStatus_Type())
vmpsOperStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:vmpsOperStatus.setStatus(_A)
_VmpsDatabase_ObjectIdentity=ObjectIdentity
vmpsDatabase=_VmpsDatabase_ObjectIdentity((1,3,6,1,4,1,9,9,53,1,2))
_VmpsMacConfigTable_Object=MibTable
vmpsMacConfigTable=_VmpsMacConfigTable_Object((1,3,6,1,4,1,9,9,53,1,2,1))
if mibBuilder.loadTexts:vmpsMacConfigTable.setStatus(_A)
_VmpsMacConfigEntry_Object=MibTableRow
vmpsMacConfigEntry=_VmpsMacConfigEntry_Object((1,3,6,1,4,1,9,9,53,1,2,1,1))
vmpsMacConfigEntry.setIndexNames((0,_B,_G),(0,_B,_Q))
if mibBuilder.loadTexts:vmpsMacConfigEntry.setStatus(_A)
_VmpsMacConfigAddress_Type=MacAddress
_VmpsMacConfigAddress_Object=MibTableColumn
vmpsMacConfigAddress=_VmpsMacConfigAddress_Object((1,3,6,1,4,1,9,9,53,1,2,1,1,1),_VmpsMacConfigAddress_Type())
vmpsMacConfigAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:vmpsMacConfigAddress.setStatus(_A)
_VmpsMacConfigVlan_Type=VlanName
_VmpsMacConfigVlan_Object=MibTableColumn
vmpsMacConfigVlan=_VmpsMacConfigVlan_Object((1,3,6,1,4,1,9,9,53,1,2,1,1,2),_VmpsMacConfigVlan_Type())
vmpsMacConfigVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:vmpsMacConfigVlan.setStatus(_A)
_VmpsMacConfigLastAccessed_Type=TimeStamp
_VmpsMacConfigLastAccessed_Object=MibTableColumn
vmpsMacConfigLastAccessed=_VmpsMacConfigLastAccessed_Object((1,3,6,1,4,1,9,9,53,1,2,1,1,3),_VmpsMacConfigLastAccessed_Type())
vmpsMacConfigLastAccessed.setMaxAccess(_D)
if mibBuilder.loadTexts:vmpsMacConfigLastAccessed.setStatus(_A)
_VmpsMacConfigLastRequestor_Type=IpAddress
_VmpsMacConfigLastRequestor_Object=MibTableColumn
vmpsMacConfigLastRequestor=_VmpsMacConfigLastRequestor_Object((1,3,6,1,4,1,9,9,53,1,2,1,1,4),_VmpsMacConfigLastRequestor_Type())
vmpsMacConfigLastRequestor.setMaxAccess(_D)
if mibBuilder.loadTexts:vmpsMacConfigLastRequestor.setStatus(_A)
_VmpsMacConfigLastRequestPortId_Type=DisplayString
_VmpsMacConfigLastRequestPortId_Object=MibTableColumn
vmpsMacConfigLastRequestPortId=_VmpsMacConfigLastRequestPortId_Object((1,3,6,1,4,1,9,9,53,1,2,1,1,5),_VmpsMacConfigLastRequestPortId_Type())
vmpsMacConfigLastRequestPortId.setMaxAccess(_D)
if mibBuilder.loadTexts:vmpsMacConfigLastRequestPortId.setStatus(_A)
class _VmpsMacConfigLastResponseStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('success',1),('versionNotSupported',2),('insufficientResources',3),('accessDenied',4),('portShutdown',5),('unknownManagementDomain',6)))
_VmpsMacConfigLastResponseStatus_Type.__name__=_E
_VmpsMacConfigLastResponseStatus_Object=MibTableColumn
vmpsMacConfigLastResponseStatus=_VmpsMacConfigLastResponseStatus_Object((1,3,6,1,4,1,9,9,53,1,2,1,1,6),_VmpsMacConfigLastResponseStatus_Type())
vmpsMacConfigLastResponseStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:vmpsMacConfigLastResponseStatus.setStatus(_A)
_VmpsMacConfigStatus_Type=RowStatus
_VmpsMacConfigStatus_Object=MibTableColumn
vmpsMacConfigStatus=_VmpsMacConfigStatus_Object((1,3,6,1,4,1,9,9,53,1,2,1,1,7),_VmpsMacConfigStatus_Type())
vmpsMacConfigStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:vmpsMacConfigStatus.setStatus(_A)
_VmpsVlanConfigTable_Object=MibTable
vmpsVlanConfigTable=_VmpsVlanConfigTable_Object((1,3,6,1,4,1,9,9,53,1,2,2))
if mibBuilder.loadTexts:vmpsVlanConfigTable.setStatus(_A)
_VmpsVlanConfigEntry_Object=MibTableRow
vmpsVlanConfigEntry=_VmpsVlanConfigEntry_Object((1,3,6,1,4,1,9,9,53,1,2,2,1))
vmpsVlanConfigEntry.setIndexNames((0,_B,_G),(0,_B,_R),(0,_B,_S),(0,_B,_T))
if mibBuilder.loadTexts:vmpsVlanConfigEntry.setStatus(_A)
_VmpsVlanName_Type=VlanName
_VmpsVlanName_Object=MibTableColumn
vmpsVlanName=_VmpsVlanName_Object((1,3,6,1,4,1,9,9,53,1,2,2,1,1),_VmpsVlanName_Type())
vmpsVlanName.setMaxAccess(_F)
if mibBuilder.loadTexts:vmpsVlanName.setStatus(_A)
_VmpsDeviceId_Type=IpAddress
_VmpsDeviceId_Object=MibTableColumn
vmpsDeviceId=_VmpsDeviceId_Object((1,3,6,1,4,1,9,9,53,1,2,2,1,2),_VmpsDeviceId_Type())
vmpsDeviceId.setMaxAccess(_F)
if mibBuilder.loadTexts:vmpsDeviceId.setStatus(_A)
_VmpsPortName_Type=DisplayString
_VmpsPortName_Object=MibTableColumn
vmpsPortName=_VmpsPortName_Object((1,3,6,1,4,1,9,9,53,1,2,2,1,3),_VmpsPortName_Type())
vmpsPortName.setMaxAccess(_F)
if mibBuilder.loadTexts:vmpsPortName.setStatus(_A)
_VmpsVlanConfigStatus_Type=RowStatus
_VmpsVlanConfigStatus_Object=MibTableColumn
vmpsVlanConfigStatus=_VmpsVlanConfigStatus_Object((1,3,6,1,4,1,9,9,53,1,2,2,1,4),_VmpsVlanConfigStatus_Type())
vmpsVlanConfigStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:vmpsVlanConfigStatus.setStatus(_A)
_VmpsGlobalConfig_ObjectIdentity=ObjectIdentity
vmpsGlobalConfig=_VmpsGlobalConfig_ObjectIdentity((1,3,6,1,4,1,9,9,53,1,3))
_VmpsAutoBackupEnable_Type=TruthValue
_VmpsAutoBackupEnable_Object=MibScalar
vmpsAutoBackupEnable=_VmpsAutoBackupEnable_Object((1,3,6,1,4,1,9,9,53,1,3,1),_VmpsAutoBackupEnable_Type())
vmpsAutoBackupEnable.setMaxAccess(_U)
if mibBuilder.loadTexts:vmpsAutoBackupEnable.setStatus(_A)
_VmpsAutoBackupFileName_Type=SnmpAdminString
_VmpsAutoBackupFileName_Object=MibScalar
vmpsAutoBackupFileName=_VmpsAutoBackupFileName_Object((1,3,6,1,4,1,9,9,53,1,3,2),_VmpsAutoBackupFileName_Type())
vmpsAutoBackupFileName.setMaxAccess(_U)
if mibBuilder.loadTexts:vmpsAutoBackupFileName.setStatus(_A)
_CiscoVlanMemberPolicyServerMIBNotifications_ObjectIdentity=ObjectIdentity
ciscoVlanMemberPolicyServerMIBNotifications=_CiscoVlanMemberPolicyServerMIBNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,53,2))
_CiscoVlanMemberPolicyServerMIBConformance_ObjectIdentity=ObjectIdentity
ciscoVlanMemberPolicyServerMIBConformance=_CiscoVlanMemberPolicyServerMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,53,3))
_CiscoVlanMemberPolicyServerMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoVlanMemberPolicyServerMIBCompliances=_CiscoVlanMemberPolicyServerMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,53,3,1))
_CiscoVlanMemberPolicyServerMIBGroups_ObjectIdentity=ObjectIdentity
ciscoVlanMemberPolicyServerMIBGroups=_CiscoVlanMemberPolicyServerMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,53,3,2))
vmpsConfigEntry.registerAugmentions((_B,_V))
vmpsStatsEntry.setIndexNames(*vmpsConfigEntry.getIndexNames())
ciscoVlanMemberPolicyServerGroup=ObjectGroup((1,3,6,1,4,1,9,9,53,3,2,1))
ciscoVlanMemberPolicyServerGroup.setObjects(*((_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q)))
if mibBuilder.loadTexts:ciscoVlanMemberPolicyServerGroup.setStatus(_A)
ciscoVlanMemberPolicyServerRcpGroup=ObjectGroup((1,3,6,1,4,1,9,9,53,3,2,2))
ciscoVlanMemberPolicyServerRcpGroup.setObjects((_B,_r))
if mibBuilder.loadTexts:ciscoVlanMemberPolicyServerRcpGroup.setStatus(_H)
ciscoVmpsAutoBackupGroup=ObjectGroup((1,3,6,1,4,1,9,9,53,3,2,3))
ciscoVmpsAutoBackupGroup.setObjects(*((_B,_s),(_B,_t)))
if mibBuilder.loadTexts:ciscoVmpsAutoBackupGroup.setStatus(_A)
ciscoVlanMemberPolicyServerRcpGroup2=ObjectGroup((1,3,6,1,4,1,9,9,53,3,2,4))
ciscoVlanMemberPolicyServerRcpGroup2.setObjects((_B,_u))
if mibBuilder.loadTexts:ciscoVlanMemberPolicyServerRcpGroup2.setStatus(_A)
ciscoVlanMemberPolicyServerMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,53,3,1,1))
ciscoVlanMemberPolicyServerMIBCompliance.setObjects((_B,_I))
if mibBuilder.loadTexts:ciscoVlanMemberPolicyServerMIBCompliance.setStatus(_H)
ciscoVmpsMIBCompliance2=ModuleCompliance((1,3,6,1,4,1,9,9,53,3,1,2))
ciscoVmpsMIBCompliance2.setObjects(*((_B,_I),(_B,_v),(_B,_K)))
if mibBuilder.loadTexts:ciscoVmpsMIBCompliance2.setStatus(_H)
ciscoVmpsMIBCompliance3=ModuleCompliance((1,3,6,1,4,1,9,9,53,3,1,3))
ciscoVmpsMIBCompliance3.setObjects(*((_B,_I),(_B,_K),(_B,_w)))
if mibBuilder.loadTexts:ciscoVmpsMIBCompliance3.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_P:VlanName,'ciscoVmpsMIB':ciscoVmpsMIB,'ciscoVlanMemberPolicyServerMIBObjects':ciscoVlanMemberPolicyServerMIBObjects,'vmpsInfo':vmpsInfo,'vmpsConfigTable':vmpsConfigTable,'vmpsConfigEntry':vmpsConfigEntry,_G:vmpsIndex,_c:vmpsAdminStatus,_d:vmpsDownloadServerAddress,_e:vmpsConfigFileName,_f:vmpsTriggerDownload,_g:vmpsFallbackVlan,_h:vmpsSecureMode,_i:vmpsManagementDomain,_j:vmpsRowStatus,_r:vmpsRcpRemoteUserName,_u:vmpsRcpRemoteUserName2,'vmpsStatsTable':vmpsStatsTable,_V:vmpsStatsEntry,_W:vmpsLastRestart,_X:vmpsInConfigReqs,_Y:vmpsInConfigErrors,_Z:vmpsOutConfigFails,_a:vmpsLastFailClient,_b:vmpsOperStatus,'vmpsDatabase':vmpsDatabase,'vmpsMacConfigTable':vmpsMacConfigTable,'vmpsMacConfigEntry':vmpsMacConfigEntry,_Q:vmpsMacConfigAddress,_k:vmpsMacConfigVlan,_l:vmpsMacConfigLastAccessed,_m:vmpsMacConfigLastRequestor,_n:vmpsMacConfigLastRequestPortId,_o:vmpsMacConfigLastResponseStatus,_p:vmpsMacConfigStatus,'vmpsVlanConfigTable':vmpsVlanConfigTable,'vmpsVlanConfigEntry':vmpsVlanConfigEntry,_R:vmpsVlanName,_S:vmpsDeviceId,_T:vmpsPortName,_q:vmpsVlanConfigStatus,'vmpsGlobalConfig':vmpsGlobalConfig,_s:vmpsAutoBackupEnable,_t:vmpsAutoBackupFileName,'ciscoVlanMemberPolicyServerMIBNotifications':ciscoVlanMemberPolicyServerMIBNotifications,'ciscoVlanMemberPolicyServerMIBConformance':ciscoVlanMemberPolicyServerMIBConformance,'ciscoVlanMemberPolicyServerMIBCompliances':ciscoVlanMemberPolicyServerMIBCompliances,'ciscoVlanMemberPolicyServerMIBCompliance':ciscoVlanMemberPolicyServerMIBCompliance,'ciscoVmpsMIBCompliance2':ciscoVmpsMIBCompliance2,'ciscoVmpsMIBCompliance3':ciscoVmpsMIBCompliance3,'ciscoVlanMemberPolicyServerMIBGroups':ciscoVlanMemberPolicyServerMIBGroups,_I:ciscoVlanMemberPolicyServerGroup,_v:ciscoVlanMemberPolicyServerRcpGroup,_K:ciscoVmpsAutoBackupGroup,_w:ciscoVlanMemberPolicyServerRcpGroup2})