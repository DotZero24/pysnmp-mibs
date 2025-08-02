_AG='cienaWsSoftwareGroup'
_AF='cwsSoftwareInstalledcomponentsBuildSize'
_AE='cwsSoftwareInstalledcomponentsBuildTimestamp'
_AD='cwsSoftwareInstalledcomponentsBuildTag'
_AC='cwsSoftwareInstalledcomponentsBuildNumber'
_AB='cwsSoftwareInstalledcomponentsVersion'
_AA='cwsSoftwareInstalledcomponentsName'
_A9='cwsSoftwareVersionsNumberOfComponents'
_A8='cwsSoftwareVersionsSize'
_A7='cwsSoftwareVersionsBuildDate'
_A6='cwsSoftwareVersionsBuildTag'
_A5='cwsSoftwareVersionsBuildNumber'
_A4='cwsSoftwareVersionsVersion'
_A3='cwsSoftwareBootPartitionListIntegrityCheck'
_A2='cwsSoftwareBootPartitionListState'
_A1='cwsSoftwareBootPartitionListDate'
_A0='cwsSoftwareBootPartitionListVersion'
_z='cwsSoftwareBootPartitionListName'
_y='cwsSoftwareActivecomponentsStatus'
_x='cwsSoftwareActivecomponentsBuildNumber'
_w='cwsSoftwareActivecomponentsVersion'
_v='cwsSoftwareActivecomponentsName'
_u='cwsSoftwareActiveSoftwareNumberOfComponents'
_t='cwsSoftwareActiveSoftwareCatalogName'
_s='cwsSoftwareActiveSoftwareBuildDate'
_r='cwsSoftwareActiveSoftwareBuildNumber'
_q='cwsSoftwareActiveSoftwareVersion'
_p='cwsSoftwareUpgradeLogListText'
_o='cwsSoftwareUpgradeLogListDateAndTime'
_n='cwsSoftwareUpgradeServerPassword'
_m='cwsSoftwareUpgradeServerLoginId'
_l='cwsSoftwareUpgradeServerRemotePath'
_k='cwsSoftwareUpgradeServerMode'
_j='cwsSoftwareUpgradeServerServer'
_i='cwsSoftwareUpgradeServerIndex'
_h='cwsSoftwareCheckStatusReportServiceInterruptionActivation'
_g='cwsSoftwareCheckStatusReportRequiredActivationType'
_f='cwsSoftwareCheckStatusReportCheckUpgradeState'
_e='cwsSoftwareCheckStatusReportCheckOperationalState'
_d='cwsSoftwareCheckStatusReportTimestamp'
_c='cwsSoftwareCheckStatusReportServerPath'
_b='cwsSoftwareCheckStatusReportServerHostname'
_a='cwsSoftwareCheckStatusReportLocalReleaseVersion'
_Z='cwsSoftwareCheckStatusReportServerReleaseVersion'
_Y='cwsSoftwareCheckStatusReportActiveReleaseVersion'
_X='cwsSoftwareStatusLastOperation'
_W='cwsSoftwareStatusUpgradeToVersion'
_V='cwsSoftwareStatusActiveVersion'
_U='cwsSoftwareStatusCommittedVersion'
_T='cwsSoftwareStatusUpgradeOperationalState'
_S='cwsSoftwareStatusSoftwareOperationalState'
_R='cwsSoftwareInstalledcomponentsComponentIndex'
_Q='cwsSoftwareBootPartitionListIndex'
_P='active'
_O='cwsSoftwareActivecomponentsComponentIndex'
_N='cwsSoftwareActiveSoftwareTableSnmpKey'
_M='cwsSoftwareUpgradeLogListLogIndex'
_L='cwsSoftwareUpgradeServerTableSnmpKey'
_K='cwsSoftwareCheckStatusReportTableSnmpKey'
_J='cwsSoftwareStatusTableSnmpKey'
_I='OctetString'
_H='cwsSoftwareVersionsIndex'
_G='read-write'
_F='unknown'
_E='not-accessible'
_D='Integer32'
_C='read-only'
_B='CIENA-WS-SOFTWARE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_I,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cienaWsConfig,=mibBuilder.importSymbols('CIENA-WS-MIB','cienaWsConfig')
StringMaxl128,StringMaxl256,StringMaxl32,StringMaxl64=mibBuilder.importSymbols('CIENA-WS-TYPEDEFS-MIB','StringMaxl128','StringMaxl256','StringMaxl32','StringMaxl64')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
cienaWsSoftwareMIB=ModuleIdentity((1,3,6,1,4,1,1271,3,4,14))
if mibBuilder.loadTexts:cienaWsSoftwareMIB.setRevisions(('2017-07-18 00:00','2017-03-02 00:00','2016-11-03 00:00','2016-06-14 00:00','2015-09-29 00:00'))
class SoftwareOpState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_F,0),('normal',1),('upgradeinprogress',2),('restartinprogress',3),('subsystemfailed',4),('systemloaderror',5)))
class SoftwareRtncode(TextualConvention,Unsigned32):status=_A
class UpgradeOpState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19)));namedValues=NamedValues(*((_F,0),('idle',1),('downloadinprogress',2),('downloadcomplete',3),('downloadfailed',4),('installationinprogress',5),('installationcomplete',6),('installationfailed',7),('activationinprogress',8),('activationcomplete',9),('activationfailed',10),('commitinprogress',11),('commitcomplete',12),('commitfailed',13),('cancelinprogress',14),('cancelcomplete',15),('cancelfailed',16),('manualcommit',17),('manualcancel',18),('coldrestartrequired',19)))
_CienaWsSoftwareObjects_ObjectIdentity=ObjectIdentity
cienaWsSoftwareObjects=_CienaWsSoftwareObjects_ObjectIdentity((1,3,6,1,4,1,1271,3,4,14,1))
_CienaWsSoftwareConformance_ObjectIdentity=ObjectIdentity
cienaWsSoftwareConformance=_CienaWsSoftwareConformance_ObjectIdentity((1,3,6,1,4,1,1271,3,4,14,2))
_CienaWsSoftwareGroups_ObjectIdentity=ObjectIdentity
cienaWsSoftwareGroups=_CienaWsSoftwareGroups_ObjectIdentity((1,3,6,1,4,1,1271,3,4,14,2,1))
_CienaWsSoftwareCompliances_ObjectIdentity=ObjectIdentity
cienaWsSoftwareCompliances=_CienaWsSoftwareCompliances_ObjectIdentity((1,3,6,1,4,1,1271,3,4,14,2,2))
_CwsSoftwareStatusTable_Object=MibTable
cwsSoftwareStatusTable=_CwsSoftwareStatusTable_Object((1,3,6,1,4,1,1271,3,4,14,3))
if mibBuilder.loadTexts:cwsSoftwareStatusTable.setStatus(_A)
_CwsSoftwareStatusEntry_Object=MibTableRow
cwsSoftwareStatusEntry=_CwsSoftwareStatusEntry_Object((1,3,6,1,4,1,1271,3,4,14,3,1))
cwsSoftwareStatusEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:cwsSoftwareStatusEntry.setStatus(_A)
class _CwsSoftwareStatusTableSnmpKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsSoftwareStatusTableSnmpKey_Type.__name__=_D
_CwsSoftwareStatusTableSnmpKey_Object=MibTableColumn
cwsSoftwareStatusTableSnmpKey=_CwsSoftwareStatusTableSnmpKey_Object((1,3,6,1,4,1,1271,3,4,14,3,1,1),_CwsSoftwareStatusTableSnmpKey_Type())
cwsSoftwareStatusTableSnmpKey.setMaxAccess(_E)
if mibBuilder.loadTexts:cwsSoftwareStatusTableSnmpKey.setStatus(_A)
_CwsSoftwareStatusSoftwareOperationalState_Type=SoftwareOpState
_CwsSoftwareStatusSoftwareOperationalState_Object=MibTableColumn
cwsSoftwareStatusSoftwareOperationalState=_CwsSoftwareStatusSoftwareOperationalState_Object((1,3,6,1,4,1,1271,3,4,14,3,1,2),_CwsSoftwareStatusSoftwareOperationalState_Type())
cwsSoftwareStatusSoftwareOperationalState.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsSoftwareStatusSoftwareOperationalState.setStatus(_A)
_CwsSoftwareStatusUpgradeOperationalState_Type=UpgradeOpState
_CwsSoftwareStatusUpgradeOperationalState_Object=MibTableColumn
cwsSoftwareStatusUpgradeOperationalState=_CwsSoftwareStatusUpgradeOperationalState_Object((1,3,6,1,4,1,1271,3,4,14,3,1,3),_CwsSoftwareStatusUpgradeOperationalState_Type())
cwsSoftwareStatusUpgradeOperationalState.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsSoftwareStatusUpgradeOperationalState.setStatus(_A)
_CwsSoftwareStatusCommittedVersion_Type=StringMaxl32
_CwsSoftwareStatusCommittedVersion_Object=MibTableColumn
cwsSoftwareStatusCommittedVersion=_CwsSoftwareStatusCommittedVersion_Object((1,3,6,1,4,1,1271,3,4,14,3,1,4),_CwsSoftwareStatusCommittedVersion_Type())
cwsSoftwareStatusCommittedVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsSoftwareStatusCommittedVersion.setStatus(_A)
_CwsSoftwareStatusActiveVersion_Type=StringMaxl32
_CwsSoftwareStatusActiveVersion_Object=MibTableColumn
cwsSoftwareStatusActiveVersion=_CwsSoftwareStatusActiveVersion_Object((1,3,6,1,4,1,1271,3,4,14,3,1,5),_CwsSoftwareStatusActiveVersion_Type())
cwsSoftwareStatusActiveVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsSoftwareStatusActiveVersion.setStatus(_A)
_CwsSoftwareStatusUpgradeToVersion_Type=StringMaxl32
_CwsSoftwareStatusUpgradeToVersion_Object=MibTableColumn
cwsSoftwareStatusUpgradeToVersion=_CwsSoftwareStatusUpgradeToVersion_Object((1,3,6,1,4,1,1271,3,4,14,3,1,6),_CwsSoftwareStatusUpgradeToVersion_Type())
cwsSoftwareStatusUpgradeToVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsSoftwareStatusUpgradeToVersion.setStatus(_A)
_CwsSoftwareStatusLastOperation_Type=StringMaxl128
_CwsSoftwareStatusLastOperation_Object=MibTableColumn
cwsSoftwareStatusLastOperation=_CwsSoftwareStatusLastOperation_Object((1,3,6,1,4,1,1271,3,4,14,3,1,7),_CwsSoftwareStatusLastOperation_Type())
cwsSoftwareStatusLastOperation.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsSoftwareStatusLastOperation.setStatus(_A)
_CwsSoftwareCheckStatusReportTable_Object=MibTable
cwsSoftwareCheckStatusReportTable=_CwsSoftwareCheckStatusReportTable_Object((1,3,6,1,4,1,1271,3,4,14,4))
if mibBuilder.loadTexts:cwsSoftwareCheckStatusReportTable.setStatus(_A)
_CwsSoftwareCheckStatusReportEntry_Object=MibTableRow
cwsSoftwareCheckStatusReportEntry=_CwsSoftwareCheckStatusReportEntry_Object((1,3,6,1,4,1,1271,3,4,14,4,1))
cwsSoftwareCheckStatusReportEntry.setIndexNames((0,_B,_K))
if mibBuilder.loadTexts:cwsSoftwareCheckStatusReportEntry.setStatus(_A)
class _CwsSoftwareCheckStatusReportTableSnmpKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsSoftwareCheckStatusReportTableSnmpKey_Type.__name__=_D
_CwsSoftwareCheckStatusReportTableSnmpKey_Object=MibTableColumn
cwsSoftwareCheckStatusReportTableSnmpKey=_CwsSoftwareCheckStatusReportTableSnmpKey_Object((1,3,6,1,4,1,1271,3,4,14,4,1,1),_CwsSoftwareCheckStatusReportTableSnmpKey_Type())
cwsSoftwareCheckStatusReportTableSnmpKey.setMaxAccess(_E)
if mibBuilder.loadTexts:cwsSoftwareCheckStatusReportTableSnmpKey.setStatus(_A)
_CwsSoftwareCheckStatusReportActiveReleaseVersion_Type=StringMaxl32
_CwsSoftwareCheckStatusReportActiveReleaseVersion_Object=MibTableColumn
cwsSoftwareCheckStatusReportActiveReleaseVersion=_CwsSoftwareCheckStatusReportActiveReleaseVersion_Object((1,3,6,1,4,1,1271,3,4,14,4,1,2),_CwsSoftwareCheckStatusReportActiveReleaseVersion_Type())
cwsSoftwareCheckStatusReportActiveReleaseVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsSoftwareCheckStatusReportActiveReleaseVersion.setStatus(_A)
_CwsSoftwareCheckStatusReportServerReleaseVersion_Type=StringMaxl32
_CwsSoftwareCheckStatusReportServerReleaseVersion_Object=MibTableColumn
cwsSoftwareCheckStatusReportServerReleaseVersion=_CwsSoftwareCheckStatusReportServerReleaseVersion_Object((1,3,6,1,4,1,1271,3,4,14,4,1,3),_CwsSoftwareCheckStatusReportServerReleaseVersion_Type())
cwsSoftwareCheckStatusReportServerReleaseVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsSoftwareCheckStatusReportServerReleaseVersion.setStatus(_A)
_CwsSoftwareCheckStatusReportLocalReleaseVersion_Type=StringMaxl32
_CwsSoftwareCheckStatusReportLocalReleaseVersion_Object=MibTableColumn
cwsSoftwareCheckStatusReportLocalReleaseVersion=_CwsSoftwareCheckStatusReportLocalReleaseVersion_Object((1,3,6,1,4,1,1271,3,4,14,4,1,4),_CwsSoftwareCheckStatusReportLocalReleaseVersion_Type())
cwsSoftwareCheckStatusReportLocalReleaseVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsSoftwareCheckStatusReportLocalReleaseVersion.setStatus(_A)
_CwsSoftwareCheckStatusReportServerHostname_Type=StringMaxl32
_CwsSoftwareCheckStatusReportServerHostname_Object=MibTableColumn
cwsSoftwareCheckStatusReportServerHostname=_CwsSoftwareCheckStatusReportServerHostname_Object((1,3,6,1,4,1,1271,3,4,14,4,1,5),_CwsSoftwareCheckStatusReportServerHostname_Type())
cwsSoftwareCheckStatusReportServerHostname.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsSoftwareCheckStatusReportServerHostname.setStatus(_A)
_CwsSoftwareCheckStatusReportServerPath_Type=StringMaxl256
_CwsSoftwareCheckStatusReportServerPath_Object=MibTableColumn
cwsSoftwareCheckStatusReportServerPath=_CwsSoftwareCheckStatusReportServerPath_Object((1,3,6,1,4,1,1271,3,4,14,4,1,6),_CwsSoftwareCheckStatusReportServerPath_Type())
cwsSoftwareCheckStatusReportServerPath.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsSoftwareCheckStatusReportServerPath.setStatus(_A)
_CwsSoftwareCheckStatusReportTimestamp_Type=StringMaxl128
_CwsSoftwareCheckStatusReportTimestamp_Object=MibTableColumn
cwsSoftwareCheckStatusReportTimestamp=_CwsSoftwareCheckStatusReportTimestamp_Object((1,3,6,1,4,1,1271,3,4,14,4,1,7),_CwsSoftwareCheckStatusReportTimestamp_Type())
cwsSoftwareCheckStatusReportTimestamp.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsSoftwareCheckStatusReportTimestamp.setStatus(_A)
_CwsSoftwareCheckStatusReportCheckOperationalState_Type=SoftwareOpState
_CwsSoftwareCheckStatusReportCheckOperationalState_Object=MibTableColumn
cwsSoftwareCheckStatusReportCheckOperationalState=_CwsSoftwareCheckStatusReportCheckOperationalState_Object((1,3,6,1,4,1,1271,3,4,14,4,1,8),_CwsSoftwareCheckStatusReportCheckOperationalState_Type())
cwsSoftwareCheckStatusReportCheckOperationalState.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsSoftwareCheckStatusReportCheckOperationalState.setStatus(_A)
_CwsSoftwareCheckStatusReportCheckUpgradeState_Type=UpgradeOpState
_CwsSoftwareCheckStatusReportCheckUpgradeState_Object=MibTableColumn
cwsSoftwareCheckStatusReportCheckUpgradeState=_CwsSoftwareCheckStatusReportCheckUpgradeState_Object((1,3,6,1,4,1,1271,3,4,14,4,1,9),_CwsSoftwareCheckStatusReportCheckUpgradeState_Type())
cwsSoftwareCheckStatusReportCheckUpgradeState.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsSoftwareCheckStatusReportCheckUpgradeState.setStatus(_A)
_CwsSoftwareCheckStatusReportRequiredActivationType_Type=StringMaxl32
_CwsSoftwareCheckStatusReportRequiredActivationType_Object=MibTableColumn
cwsSoftwareCheckStatusReportRequiredActivationType=_CwsSoftwareCheckStatusReportRequiredActivationType_Object((1,3,6,1,4,1,1271,3,4,14,4,1,10),_CwsSoftwareCheckStatusReportRequiredActivationType_Type())
cwsSoftwareCheckStatusReportRequiredActivationType.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsSoftwareCheckStatusReportRequiredActivationType.setStatus(_A)
_CwsSoftwareCheckStatusReportServiceInterruptionActivation_Type=TruthValue
_CwsSoftwareCheckStatusReportServiceInterruptionActivation_Object=MibTableColumn
cwsSoftwareCheckStatusReportServiceInterruptionActivation=_CwsSoftwareCheckStatusReportServiceInterruptionActivation_Object((1,3,6,1,4,1,1271,3,4,14,4,1,11),_CwsSoftwareCheckStatusReportServiceInterruptionActivation_Type())
cwsSoftwareCheckStatusReportServiceInterruptionActivation.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsSoftwareCheckStatusReportServiceInterruptionActivation.setStatus(_A)
_CwsSoftwareUpgradeServerTable_Object=MibTable
cwsSoftwareUpgradeServerTable=_CwsSoftwareUpgradeServerTable_Object((1,3,6,1,4,1,1271,3,4,14,5))
if mibBuilder.loadTexts:cwsSoftwareUpgradeServerTable.setStatus(_A)
_CwsSoftwareUpgradeServerEntry_Object=MibTableRow
cwsSoftwareUpgradeServerEntry=_CwsSoftwareUpgradeServerEntry_Object((1,3,6,1,4,1,1271,3,4,14,5,1))
cwsSoftwareUpgradeServerEntry.setIndexNames((0,_B,_L))
if mibBuilder.loadTexts:cwsSoftwareUpgradeServerEntry.setStatus(_A)
class _CwsSoftwareUpgradeServerTableSnmpKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsSoftwareUpgradeServerTableSnmpKey_Type.__name__=_D
_CwsSoftwareUpgradeServerTableSnmpKey_Object=MibTableColumn
cwsSoftwareUpgradeServerTableSnmpKey=_CwsSoftwareUpgradeServerTableSnmpKey_Object((1,3,6,1,4,1,1271,3,4,14,5,1,1),_CwsSoftwareUpgradeServerTableSnmpKey_Type())
cwsSoftwareUpgradeServerTableSnmpKey.setMaxAccess(_E)
if mibBuilder.loadTexts:cwsSoftwareUpgradeServerTableSnmpKey.setStatus(_A)
_CwsSoftwareUpgradeServerIndex_Type=Unsigned32
_CwsSoftwareUpgradeServerIndex_Object=MibTableColumn
cwsSoftwareUpgradeServerIndex=_CwsSoftwareUpgradeServerIndex_Object((1,3,6,1,4,1,1271,3,4,14,5,1,2),_CwsSoftwareUpgradeServerIndex_Type())
cwsSoftwareUpgradeServerIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:cwsSoftwareUpgradeServerIndex.setStatus(_A)
_CwsSoftwareUpgradeServerServer_Type=StringMaxl64
_CwsSoftwareUpgradeServerServer_Object=MibTableColumn
cwsSoftwareUpgradeServerServer=_CwsSoftwareUpgradeServerServer_Object((1,3,6,1,4,1,1271,3,4,14,5,1,3),_CwsSoftwareUpgradeServerServer_Type())
cwsSoftwareUpgradeServerServer.setMaxAccess(_G)
if mibBuilder.loadTexts:cwsSoftwareUpgradeServerServer.setStatus(_A)
class _CwsSoftwareUpgradeServerMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('tftp',0),('ftp',1),('sftp',2),('scp',3)))
_CwsSoftwareUpgradeServerMode_Type.__name__=_D
_CwsSoftwareUpgradeServerMode_Object=MibTableColumn
cwsSoftwareUpgradeServerMode=_CwsSoftwareUpgradeServerMode_Object((1,3,6,1,4,1,1271,3,4,14,5,1,4),_CwsSoftwareUpgradeServerMode_Type())
cwsSoftwareUpgradeServerMode.setMaxAccess(_G)
if mibBuilder.loadTexts:cwsSoftwareUpgradeServerMode.setStatus(_A)
class _CwsSoftwareUpgradeServerRemotePath_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_CwsSoftwareUpgradeServerRemotePath_Type.__name__=_I
_CwsSoftwareUpgradeServerRemotePath_Object=MibTableColumn
cwsSoftwareUpgradeServerRemotePath=_CwsSoftwareUpgradeServerRemotePath_Object((1,3,6,1,4,1,1271,3,4,14,5,1,5),_CwsSoftwareUpgradeServerRemotePath_Type())
cwsSoftwareUpgradeServerRemotePath.setMaxAccess(_G)
if mibBuilder.loadTexts:cwsSoftwareUpgradeServerRemotePath.setStatus(_A)
_CwsSoftwareUpgradeServerLoginId_Type=StringMaxl32
_CwsSoftwareUpgradeServerLoginId_Object=MibTableColumn
cwsSoftwareUpgradeServerLoginId=_CwsSoftwareUpgradeServerLoginId_Object((1,3,6,1,4,1,1271,3,4,14,5,1,6),_CwsSoftwareUpgradeServerLoginId_Type())
cwsSoftwareUpgradeServerLoginId.setMaxAccess(_G)
if mibBuilder.loadTexts:cwsSoftwareUpgradeServerLoginId.setStatus(_A)
_CwsSoftwareUpgradeServerPassword_Type=StringMaxl32
_CwsSoftwareUpgradeServerPassword_Object=MibTableColumn
cwsSoftwareUpgradeServerPassword=_CwsSoftwareUpgradeServerPassword_Object((1,3,6,1,4,1,1271,3,4,14,5,1,7),_CwsSoftwareUpgradeServerPassword_Type())
cwsSoftwareUpgradeServerPassword.setMaxAccess(_G)
if mibBuilder.loadTexts:cwsSoftwareUpgradeServerPassword.setStatus(_A)
_CwsSoftwareUpgradeLogListTable_Object=MibTable
cwsSoftwareUpgradeLogListTable=_CwsSoftwareUpgradeLogListTable_Object((1,3,6,1,4,1,1271,3,4,14,6))
if mibBuilder.loadTexts:cwsSoftwareUpgradeLogListTable.setStatus(_A)
_CwsSoftwareUpgradeLogListEntry_Object=MibTableRow
cwsSoftwareUpgradeLogListEntry=_CwsSoftwareUpgradeLogListEntry_Object((1,3,6,1,4,1,1271,3,4,14,6,1))
cwsSoftwareUpgradeLogListEntry.setIndexNames((0,_B,_M))
if mibBuilder.loadTexts:cwsSoftwareUpgradeLogListEntry.setStatus(_A)
class _CwsSoftwareUpgradeLogListLogIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsSoftwareUpgradeLogListLogIndex_Type.__name__=_D
_CwsSoftwareUpgradeLogListLogIndex_Object=MibTableColumn
cwsSoftwareUpgradeLogListLogIndex=_CwsSoftwareUpgradeLogListLogIndex_Object((1,3,6,1,4,1,1271,3,4,14,6,1,1),_CwsSoftwareUpgradeLogListLogIndex_Type())
cwsSoftwareUpgradeLogListLogIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:cwsSoftwareUpgradeLogListLogIndex.setStatus(_A)
_CwsSoftwareUpgradeLogListDateAndTime_Type=StringMaxl64
_CwsSoftwareUpgradeLogListDateAndTime_Object=MibTableColumn
cwsSoftwareUpgradeLogListDateAndTime=_CwsSoftwareUpgradeLogListDateAndTime_Object((1,3,6,1,4,1,1271,3,4,14,6,1,2),_CwsSoftwareUpgradeLogListDateAndTime_Type())
cwsSoftwareUpgradeLogListDateAndTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsSoftwareUpgradeLogListDateAndTime.setStatus(_A)
_CwsSoftwareUpgradeLogListText_Type=StringMaxl256
_CwsSoftwareUpgradeLogListText_Object=MibTableColumn
cwsSoftwareUpgradeLogListText=_CwsSoftwareUpgradeLogListText_Object((1,3,6,1,4,1,1271,3,4,14,6,1,3),_CwsSoftwareUpgradeLogListText_Type())
cwsSoftwareUpgradeLogListText.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsSoftwareUpgradeLogListText.setStatus(_A)
_CwsSoftwareActiveSoftwareTable_Object=MibTable
cwsSoftwareActiveSoftwareTable=_CwsSoftwareActiveSoftwareTable_Object((1,3,6,1,4,1,1271,3,4,14,7))
if mibBuilder.loadTexts:cwsSoftwareActiveSoftwareTable.setStatus(_A)
_CwsSoftwareActiveSoftwareEntry_Object=MibTableRow
cwsSoftwareActiveSoftwareEntry=_CwsSoftwareActiveSoftwareEntry_Object((1,3,6,1,4,1,1271,3,4,14,7,1))
cwsSoftwareActiveSoftwareEntry.setIndexNames((0,_B,_N))
if mibBuilder.loadTexts:cwsSoftwareActiveSoftwareEntry.setStatus(_A)
class _CwsSoftwareActiveSoftwareTableSnmpKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsSoftwareActiveSoftwareTableSnmpKey_Type.__name__=_D
_CwsSoftwareActiveSoftwareTableSnmpKey_Object=MibTableColumn
cwsSoftwareActiveSoftwareTableSnmpKey=_CwsSoftwareActiveSoftwareTableSnmpKey_Object((1,3,6,1,4,1,1271,3,4,14,7,1,1),_CwsSoftwareActiveSoftwareTableSnmpKey_Type())
cwsSoftwareActiveSoftwareTableSnmpKey.setMaxAccess(_E)
if mibBuilder.loadTexts:cwsSoftwareActiveSoftwareTableSnmpKey.setStatus(_A)
_CwsSoftwareActiveSoftwareVersion_Type=StringMaxl32
_CwsSoftwareActiveSoftwareVersion_Object=MibTableColumn
cwsSoftwareActiveSoftwareVersion=_CwsSoftwareActiveSoftwareVersion_Object((1,3,6,1,4,1,1271,3,4,14,7,1,2),_CwsSoftwareActiveSoftwareVersion_Type())
cwsSoftwareActiveSoftwareVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsSoftwareActiveSoftwareVersion.setStatus(_A)
_CwsSoftwareActiveSoftwareBuildNumber_Type=StringMaxl32
_CwsSoftwareActiveSoftwareBuildNumber_Object=MibTableColumn
cwsSoftwareActiveSoftwareBuildNumber=_CwsSoftwareActiveSoftwareBuildNumber_Object((1,3,6,1,4,1,1271,3,4,14,7,1,3),_CwsSoftwareActiveSoftwareBuildNumber_Type())
cwsSoftwareActiveSoftwareBuildNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsSoftwareActiveSoftwareBuildNumber.setStatus(_A)
_CwsSoftwareActiveSoftwareBuildDate_Type=StringMaxl32
_CwsSoftwareActiveSoftwareBuildDate_Object=MibTableColumn
cwsSoftwareActiveSoftwareBuildDate=_CwsSoftwareActiveSoftwareBuildDate_Object((1,3,6,1,4,1,1271,3,4,14,7,1,4),_CwsSoftwareActiveSoftwareBuildDate_Type())
cwsSoftwareActiveSoftwareBuildDate.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsSoftwareActiveSoftwareBuildDate.setStatus(_A)
_CwsSoftwareActiveSoftwareCatalogName_Type=StringMaxl64
_CwsSoftwareActiveSoftwareCatalogName_Object=MibTableColumn
cwsSoftwareActiveSoftwareCatalogName=_CwsSoftwareActiveSoftwareCatalogName_Object((1,3,6,1,4,1,1271,3,4,14,7,1,5),_CwsSoftwareActiveSoftwareCatalogName_Type())
cwsSoftwareActiveSoftwareCatalogName.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsSoftwareActiveSoftwareCatalogName.setStatus(_A)
_CwsSoftwareActiveSoftwareNumberOfComponents_Type=Unsigned32
_CwsSoftwareActiveSoftwareNumberOfComponents_Object=MibTableColumn
cwsSoftwareActiveSoftwareNumberOfComponents=_CwsSoftwareActiveSoftwareNumberOfComponents_Object((1,3,6,1,4,1,1271,3,4,14,7,1,6),_CwsSoftwareActiveSoftwareNumberOfComponents_Type())
cwsSoftwareActiveSoftwareNumberOfComponents.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsSoftwareActiveSoftwareNumberOfComponents.setStatus(_A)
_CwsSoftwareActivecomponentsTable_Object=MibTable
cwsSoftwareActivecomponentsTable=_CwsSoftwareActivecomponentsTable_Object((1,3,6,1,4,1,1271,3,4,14,8))
if mibBuilder.loadTexts:cwsSoftwareActivecomponentsTable.setStatus(_A)
_CwsSoftwareActivecomponentsEntry_Object=MibTableRow
cwsSoftwareActivecomponentsEntry=_CwsSoftwareActivecomponentsEntry_Object((1,3,6,1,4,1,1271,3,4,14,8,1))
cwsSoftwareActivecomponentsEntry.setIndexNames((0,_B,_O))
if mibBuilder.loadTexts:cwsSoftwareActivecomponentsEntry.setStatus(_A)
class _CwsSoftwareActivecomponentsComponentIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsSoftwareActivecomponentsComponentIndex_Type.__name__=_D
_CwsSoftwareActivecomponentsComponentIndex_Object=MibTableColumn
cwsSoftwareActivecomponentsComponentIndex=_CwsSoftwareActivecomponentsComponentIndex_Object((1,3,6,1,4,1,1271,3,4,14,8,1,1),_CwsSoftwareActivecomponentsComponentIndex_Type())
cwsSoftwareActivecomponentsComponentIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:cwsSoftwareActivecomponentsComponentIndex.setStatus(_A)
_CwsSoftwareActivecomponentsName_Type=StringMaxl32
_CwsSoftwareActivecomponentsName_Object=MibTableColumn
cwsSoftwareActivecomponentsName=_CwsSoftwareActivecomponentsName_Object((1,3,6,1,4,1,1271,3,4,14,8,1,2),_CwsSoftwareActivecomponentsName_Type())
cwsSoftwareActivecomponentsName.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsSoftwareActivecomponentsName.setStatus(_A)
_CwsSoftwareActivecomponentsVersion_Type=StringMaxl32
_CwsSoftwareActivecomponentsVersion_Object=MibTableColumn
cwsSoftwareActivecomponentsVersion=_CwsSoftwareActivecomponentsVersion_Object((1,3,6,1,4,1,1271,3,4,14,8,1,3),_CwsSoftwareActivecomponentsVersion_Type())
cwsSoftwareActivecomponentsVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsSoftwareActivecomponentsVersion.setStatus(_A)
_CwsSoftwareActivecomponentsBuildNumber_Type=StringMaxl32
_CwsSoftwareActivecomponentsBuildNumber_Object=MibTableColumn
cwsSoftwareActivecomponentsBuildNumber=_CwsSoftwareActivecomponentsBuildNumber_Object((1,3,6,1,4,1,1271,3,4,14,8,1,4),_CwsSoftwareActivecomponentsBuildNumber_Type())
cwsSoftwareActivecomponentsBuildNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsSoftwareActivecomponentsBuildNumber.setStatus(_A)
class _CwsSoftwareActivecomponentsStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_F,0),(_P,1),('failed',2),('pending',3),('restarting',4)))
_CwsSoftwareActivecomponentsStatus_Type.__name__=_D
_CwsSoftwareActivecomponentsStatus_Object=MibTableColumn
cwsSoftwareActivecomponentsStatus=_CwsSoftwareActivecomponentsStatus_Object((1,3,6,1,4,1,1271,3,4,14,8,1,5),_CwsSoftwareActivecomponentsStatus_Type())
cwsSoftwareActivecomponentsStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsSoftwareActivecomponentsStatus.setStatus(_A)
_CwsSoftwareBootPartitionListTable_Object=MibTable
cwsSoftwareBootPartitionListTable=_CwsSoftwareBootPartitionListTable_Object((1,3,6,1,4,1,1271,3,4,14,9))
if mibBuilder.loadTexts:cwsSoftwareBootPartitionListTable.setStatus(_A)
_CwsSoftwareBootPartitionListEntry_Object=MibTableRow
cwsSoftwareBootPartitionListEntry=_CwsSoftwareBootPartitionListEntry_Object((1,3,6,1,4,1,1271,3,4,14,9,1))
cwsSoftwareBootPartitionListEntry.setIndexNames((0,_B,_Q))
if mibBuilder.loadTexts:cwsSoftwareBootPartitionListEntry.setStatus(_A)
class _CwsSoftwareBootPartitionListIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsSoftwareBootPartitionListIndex_Type.__name__=_D
_CwsSoftwareBootPartitionListIndex_Object=MibTableColumn
cwsSoftwareBootPartitionListIndex=_CwsSoftwareBootPartitionListIndex_Object((1,3,6,1,4,1,1271,3,4,14,9,1,1),_CwsSoftwareBootPartitionListIndex_Type())
cwsSoftwareBootPartitionListIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:cwsSoftwareBootPartitionListIndex.setStatus(_A)
class _CwsSoftwareBootPartitionListName_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_F,0),('kernel0',1),('bootloader0',2),('kernel1',3),('bootloader1',4),('firmware0',5),('firmware1',6),('backupbl',7)))
_CwsSoftwareBootPartitionListName_Type.__name__=_D
_CwsSoftwareBootPartitionListName_Object=MibTableColumn
cwsSoftwareBootPartitionListName=_CwsSoftwareBootPartitionListName_Object((1,3,6,1,4,1,1271,3,4,14,9,1,2),_CwsSoftwareBootPartitionListName_Type())
cwsSoftwareBootPartitionListName.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsSoftwareBootPartitionListName.setStatus(_A)
_CwsSoftwareBootPartitionListVersion_Type=StringMaxl32
_CwsSoftwareBootPartitionListVersion_Object=MibTableColumn
cwsSoftwareBootPartitionListVersion=_CwsSoftwareBootPartitionListVersion_Object((1,3,6,1,4,1,1271,3,4,14,9,1,3),_CwsSoftwareBootPartitionListVersion_Type())
cwsSoftwareBootPartitionListVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsSoftwareBootPartitionListVersion.setStatus(_A)
_CwsSoftwareBootPartitionListDate_Type=StringMaxl32
_CwsSoftwareBootPartitionListDate_Object=MibTableColumn
cwsSoftwareBootPartitionListDate=_CwsSoftwareBootPartitionListDate_Object((1,3,6,1,4,1,1271,3,4,14,9,1,4),_CwsSoftwareBootPartitionListDate_Type())
cwsSoftwareBootPartitionListDate.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsSoftwareBootPartitionListDate.setStatus(_A)
class _CwsSoftwareBootPartitionListState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_F,0),(_P,1),('standby',2),('notapplicable',3)))
_CwsSoftwareBootPartitionListState_Type.__name__=_D
_CwsSoftwareBootPartitionListState_Object=MibTableColumn
cwsSoftwareBootPartitionListState=_CwsSoftwareBootPartitionListState_Object((1,3,6,1,4,1,1271,3,4,14,9,1,5),_CwsSoftwareBootPartitionListState_Type())
cwsSoftwareBootPartitionListState.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsSoftwareBootPartitionListState.setStatus(_A)
class _CwsSoftwareBootPartitionListIntegrityCheck_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_F,0),('pass',1),('invalid',2)))
_CwsSoftwareBootPartitionListIntegrityCheck_Type.__name__=_D
_CwsSoftwareBootPartitionListIntegrityCheck_Object=MibTableColumn
cwsSoftwareBootPartitionListIntegrityCheck=_CwsSoftwareBootPartitionListIntegrityCheck_Object((1,3,6,1,4,1,1271,3,4,14,9,1,6),_CwsSoftwareBootPartitionListIntegrityCheck_Type())
cwsSoftwareBootPartitionListIntegrityCheck.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsSoftwareBootPartitionListIntegrityCheck.setStatus(_A)
_CwsSoftwareVersionsTable_Object=MibTable
cwsSoftwareVersionsTable=_CwsSoftwareVersionsTable_Object((1,3,6,1,4,1,1271,3,4,14,10))
if mibBuilder.loadTexts:cwsSoftwareVersionsTable.setStatus(_A)
_CwsSoftwareVersionsEntry_Object=MibTableRow
cwsSoftwareVersionsEntry=_CwsSoftwareVersionsEntry_Object((1,3,6,1,4,1,1271,3,4,14,10,1))
cwsSoftwareVersionsEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:cwsSoftwareVersionsEntry.setStatus(_A)
class _CwsSoftwareVersionsIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsSoftwareVersionsIndex_Type.__name__=_D
_CwsSoftwareVersionsIndex_Object=MibTableColumn
cwsSoftwareVersionsIndex=_CwsSoftwareVersionsIndex_Object((1,3,6,1,4,1,1271,3,4,14,10,1,1),_CwsSoftwareVersionsIndex_Type())
cwsSoftwareVersionsIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:cwsSoftwareVersionsIndex.setStatus(_A)
_CwsSoftwareVersionsVersion_Type=StringMaxl32
_CwsSoftwareVersionsVersion_Object=MibTableColumn
cwsSoftwareVersionsVersion=_CwsSoftwareVersionsVersion_Object((1,3,6,1,4,1,1271,3,4,14,10,1,2),_CwsSoftwareVersionsVersion_Type())
cwsSoftwareVersionsVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsSoftwareVersionsVersion.setStatus(_A)
_CwsSoftwareVersionsBuildNumber_Type=StringMaxl32
_CwsSoftwareVersionsBuildNumber_Object=MibTableColumn
cwsSoftwareVersionsBuildNumber=_CwsSoftwareVersionsBuildNumber_Object((1,3,6,1,4,1,1271,3,4,14,10,1,3),_CwsSoftwareVersionsBuildNumber_Type())
cwsSoftwareVersionsBuildNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsSoftwareVersionsBuildNumber.setStatus(_A)
_CwsSoftwareVersionsBuildTag_Type=StringMaxl32
_CwsSoftwareVersionsBuildTag_Object=MibTableColumn
cwsSoftwareVersionsBuildTag=_CwsSoftwareVersionsBuildTag_Object((1,3,6,1,4,1,1271,3,4,14,10,1,4),_CwsSoftwareVersionsBuildTag_Type())
cwsSoftwareVersionsBuildTag.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsSoftwareVersionsBuildTag.setStatus(_A)
_CwsSoftwareVersionsBuildDate_Type=StringMaxl32
_CwsSoftwareVersionsBuildDate_Object=MibTableColumn
cwsSoftwareVersionsBuildDate=_CwsSoftwareVersionsBuildDate_Object((1,3,6,1,4,1,1271,3,4,14,10,1,5),_CwsSoftwareVersionsBuildDate_Type())
cwsSoftwareVersionsBuildDate.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsSoftwareVersionsBuildDate.setStatus(_A)
_CwsSoftwareVersionsSize_Type=Unsigned32
_CwsSoftwareVersionsSize_Object=MibTableColumn
cwsSoftwareVersionsSize=_CwsSoftwareVersionsSize_Object((1,3,6,1,4,1,1271,3,4,14,10,1,6),_CwsSoftwareVersionsSize_Type())
cwsSoftwareVersionsSize.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsSoftwareVersionsSize.setStatus(_A)
_CwsSoftwareVersionsNumberOfComponents_Type=Unsigned32
_CwsSoftwareVersionsNumberOfComponents_Object=MibTableColumn
cwsSoftwareVersionsNumberOfComponents=_CwsSoftwareVersionsNumberOfComponents_Object((1,3,6,1,4,1,1271,3,4,14,10,1,7),_CwsSoftwareVersionsNumberOfComponents_Type())
cwsSoftwareVersionsNumberOfComponents.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsSoftwareVersionsNumberOfComponents.setStatus(_A)
_CwsSoftwareInstalledcomponentsTable_Object=MibTable
cwsSoftwareInstalledcomponentsTable=_CwsSoftwareInstalledcomponentsTable_Object((1,3,6,1,4,1,1271,3,4,14,11))
if mibBuilder.loadTexts:cwsSoftwareInstalledcomponentsTable.setStatus(_A)
_CwsSoftwareInstalledcomponentsEntry_Object=MibTableRow
cwsSoftwareInstalledcomponentsEntry=_CwsSoftwareInstalledcomponentsEntry_Object((1,3,6,1,4,1,1271,3,4,14,11,1))
cwsSoftwareInstalledcomponentsEntry.setIndexNames((0,_B,_H),(0,_B,_R))
if mibBuilder.loadTexts:cwsSoftwareInstalledcomponentsEntry.setStatus(_A)
class _CwsSoftwareInstalledcomponentsComponentIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsSoftwareInstalledcomponentsComponentIndex_Type.__name__=_D
_CwsSoftwareInstalledcomponentsComponentIndex_Object=MibTableColumn
cwsSoftwareInstalledcomponentsComponentIndex=_CwsSoftwareInstalledcomponentsComponentIndex_Object((1,3,6,1,4,1,1271,3,4,14,11,1,1),_CwsSoftwareInstalledcomponentsComponentIndex_Type())
cwsSoftwareInstalledcomponentsComponentIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:cwsSoftwareInstalledcomponentsComponentIndex.setStatus(_A)
_CwsSoftwareInstalledcomponentsName_Type=StringMaxl32
_CwsSoftwareInstalledcomponentsName_Object=MibTableColumn
cwsSoftwareInstalledcomponentsName=_CwsSoftwareInstalledcomponentsName_Object((1,3,6,1,4,1,1271,3,4,14,11,1,2),_CwsSoftwareInstalledcomponentsName_Type())
cwsSoftwareInstalledcomponentsName.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsSoftwareInstalledcomponentsName.setStatus(_A)
_CwsSoftwareInstalledcomponentsVersion_Type=StringMaxl32
_CwsSoftwareInstalledcomponentsVersion_Object=MibTableColumn
cwsSoftwareInstalledcomponentsVersion=_CwsSoftwareInstalledcomponentsVersion_Object((1,3,6,1,4,1,1271,3,4,14,11,1,3),_CwsSoftwareInstalledcomponentsVersion_Type())
cwsSoftwareInstalledcomponentsVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsSoftwareInstalledcomponentsVersion.setStatus(_A)
_CwsSoftwareInstalledcomponentsBuildNumber_Type=StringMaxl32
_CwsSoftwareInstalledcomponentsBuildNumber_Object=MibTableColumn
cwsSoftwareInstalledcomponentsBuildNumber=_CwsSoftwareInstalledcomponentsBuildNumber_Object((1,3,6,1,4,1,1271,3,4,14,11,1,4),_CwsSoftwareInstalledcomponentsBuildNumber_Type())
cwsSoftwareInstalledcomponentsBuildNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsSoftwareInstalledcomponentsBuildNumber.setStatus(_A)
_CwsSoftwareInstalledcomponentsBuildTag_Type=StringMaxl32
_CwsSoftwareInstalledcomponentsBuildTag_Object=MibTableColumn
cwsSoftwareInstalledcomponentsBuildTag=_CwsSoftwareInstalledcomponentsBuildTag_Object((1,3,6,1,4,1,1271,3,4,14,11,1,5),_CwsSoftwareInstalledcomponentsBuildTag_Type())
cwsSoftwareInstalledcomponentsBuildTag.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsSoftwareInstalledcomponentsBuildTag.setStatus(_A)
_CwsSoftwareInstalledcomponentsBuildTimestamp_Type=StringMaxl32
_CwsSoftwareInstalledcomponentsBuildTimestamp_Object=MibTableColumn
cwsSoftwareInstalledcomponentsBuildTimestamp=_CwsSoftwareInstalledcomponentsBuildTimestamp_Object((1,3,6,1,4,1,1271,3,4,14,11,1,6),_CwsSoftwareInstalledcomponentsBuildTimestamp_Type())
cwsSoftwareInstalledcomponentsBuildTimestamp.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsSoftwareInstalledcomponentsBuildTimestamp.setStatus(_A)
_CwsSoftwareInstalledcomponentsBuildSize_Type=Unsigned32
_CwsSoftwareInstalledcomponentsBuildSize_Object=MibTableColumn
cwsSoftwareInstalledcomponentsBuildSize=_CwsSoftwareInstalledcomponentsBuildSize_Object((1,3,6,1,4,1,1271,3,4,14,11,1,7),_CwsSoftwareInstalledcomponentsBuildSize_Type())
cwsSoftwareInstalledcomponentsBuildSize.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsSoftwareInstalledcomponentsBuildSize.setStatus(_A)
cienaWsSoftwareGroup=ObjectGroup((1,3,6,1,4,1,1271,3,4,14,2,1,1))
cienaWsSoftwareGroup.setObjects(*((_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF)))
if mibBuilder.loadTexts:cienaWsSoftwareGroup.setStatus(_A)
cienaWsSoftwareCompliance=ModuleCompliance((1,3,6,1,4,1,1271,3,4,14,2,2,1))
cienaWsSoftwareCompliance.setObjects((_B,_AG))
if mibBuilder.loadTexts:cienaWsSoftwareCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'SoftwareOpState':SoftwareOpState,'SoftwareRtncode':SoftwareRtncode,'UpgradeOpState':UpgradeOpState,'cienaWsSoftwareMIB':cienaWsSoftwareMIB,'cienaWsSoftwareObjects':cienaWsSoftwareObjects,'cienaWsSoftwareConformance':cienaWsSoftwareConformance,'cienaWsSoftwareGroups':cienaWsSoftwareGroups,_AG:cienaWsSoftwareGroup,'cienaWsSoftwareCompliances':cienaWsSoftwareCompliances,'cienaWsSoftwareCompliance':cienaWsSoftwareCompliance,'cwsSoftwareStatusTable':cwsSoftwareStatusTable,'cwsSoftwareStatusEntry':cwsSoftwareStatusEntry,_J:cwsSoftwareStatusTableSnmpKey,_S:cwsSoftwareStatusSoftwareOperationalState,_T:cwsSoftwareStatusUpgradeOperationalState,_U:cwsSoftwareStatusCommittedVersion,_V:cwsSoftwareStatusActiveVersion,_W:cwsSoftwareStatusUpgradeToVersion,_X:cwsSoftwareStatusLastOperation,'cwsSoftwareCheckStatusReportTable':cwsSoftwareCheckStatusReportTable,'cwsSoftwareCheckStatusReportEntry':cwsSoftwareCheckStatusReportEntry,_K:cwsSoftwareCheckStatusReportTableSnmpKey,_Y:cwsSoftwareCheckStatusReportActiveReleaseVersion,_Z:cwsSoftwareCheckStatusReportServerReleaseVersion,_a:cwsSoftwareCheckStatusReportLocalReleaseVersion,_b:cwsSoftwareCheckStatusReportServerHostname,_c:cwsSoftwareCheckStatusReportServerPath,_d:cwsSoftwareCheckStatusReportTimestamp,_e:cwsSoftwareCheckStatusReportCheckOperationalState,_f:cwsSoftwareCheckStatusReportCheckUpgradeState,_g:cwsSoftwareCheckStatusReportRequiredActivationType,_h:cwsSoftwareCheckStatusReportServiceInterruptionActivation,'cwsSoftwareUpgradeServerTable':cwsSoftwareUpgradeServerTable,'cwsSoftwareUpgradeServerEntry':cwsSoftwareUpgradeServerEntry,_L:cwsSoftwareUpgradeServerTableSnmpKey,_i:cwsSoftwareUpgradeServerIndex,_j:cwsSoftwareUpgradeServerServer,_k:cwsSoftwareUpgradeServerMode,_l:cwsSoftwareUpgradeServerRemotePath,_m:cwsSoftwareUpgradeServerLoginId,_n:cwsSoftwareUpgradeServerPassword,'cwsSoftwareUpgradeLogListTable':cwsSoftwareUpgradeLogListTable,'cwsSoftwareUpgradeLogListEntry':cwsSoftwareUpgradeLogListEntry,_M:cwsSoftwareUpgradeLogListLogIndex,_o:cwsSoftwareUpgradeLogListDateAndTime,_p:cwsSoftwareUpgradeLogListText,'cwsSoftwareActiveSoftwareTable':cwsSoftwareActiveSoftwareTable,'cwsSoftwareActiveSoftwareEntry':cwsSoftwareActiveSoftwareEntry,_N:cwsSoftwareActiveSoftwareTableSnmpKey,_q:cwsSoftwareActiveSoftwareVersion,_r:cwsSoftwareActiveSoftwareBuildNumber,_s:cwsSoftwareActiveSoftwareBuildDate,_t:cwsSoftwareActiveSoftwareCatalogName,_u:cwsSoftwareActiveSoftwareNumberOfComponents,'cwsSoftwareActivecomponentsTable':cwsSoftwareActivecomponentsTable,'cwsSoftwareActivecomponentsEntry':cwsSoftwareActivecomponentsEntry,_O:cwsSoftwareActivecomponentsComponentIndex,_v:cwsSoftwareActivecomponentsName,_w:cwsSoftwareActivecomponentsVersion,_x:cwsSoftwareActivecomponentsBuildNumber,_y:cwsSoftwareActivecomponentsStatus,'cwsSoftwareBootPartitionListTable':cwsSoftwareBootPartitionListTable,'cwsSoftwareBootPartitionListEntry':cwsSoftwareBootPartitionListEntry,_Q:cwsSoftwareBootPartitionListIndex,_z:cwsSoftwareBootPartitionListName,_A0:cwsSoftwareBootPartitionListVersion,_A1:cwsSoftwareBootPartitionListDate,_A2:cwsSoftwareBootPartitionListState,_A3:cwsSoftwareBootPartitionListIntegrityCheck,'cwsSoftwareVersionsTable':cwsSoftwareVersionsTable,'cwsSoftwareVersionsEntry':cwsSoftwareVersionsEntry,_H:cwsSoftwareVersionsIndex,_A4:cwsSoftwareVersionsVersion,_A5:cwsSoftwareVersionsBuildNumber,_A6:cwsSoftwareVersionsBuildTag,_A7:cwsSoftwareVersionsBuildDate,_A8:cwsSoftwareVersionsSize,_A9:cwsSoftwareVersionsNumberOfComponents,'cwsSoftwareInstalledcomponentsTable':cwsSoftwareInstalledcomponentsTable,'cwsSoftwareInstalledcomponentsEntry':cwsSoftwareInstalledcomponentsEntry,_R:cwsSoftwareInstalledcomponentsComponentIndex,_AA:cwsSoftwareInstalledcomponentsName,_AB:cwsSoftwareInstalledcomponentsVersion,_AC:cwsSoftwareInstalledcomponentsBuildNumber,_AD:cwsSoftwareInstalledcomponentsBuildTag,_AE:cwsSoftwareInstalledcomponentsBuildTimestamp,_AF:cwsSoftwareInstalledcomponentsBuildSize})