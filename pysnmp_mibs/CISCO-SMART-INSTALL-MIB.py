_AL='ciscoSmartInstallNotifyVarsGroup'
_AK='ciscoSmartInstallNotificationsGroup'
_AJ='ciscoSmartInstallNotificationEnableGroup'
_AI='ciscoSmartInstallProfileGroup'
_AH='ciscoSmartInstallJoinWindowGroup'
_AG='ciscoSmartInstallConfigBackupGroup'
_AF='ciscoSmartInstallDeviceInformationGroup'
_AE='ciscoSmartInstallGlobalConfigGroup'
_AD='csiFileLoadFailed'
_AC='csiDeviceLost'
_AB='csiDeviceAdded'
_AA='csiOperationModeChange'
_A9='csiNotifEnable'
_A8='csiDeviceStatus'
_A7='csiDeviceSerialNum'
_A6='csiDevicePlatform'
_A5='csiDeviceImageVersion'
_A4='csiDeviceBackupConfigFileName'
_A3='csiMatchRowStatus'
_A2='csiMatchStorageType'
_A1='csiMatchMacAddress'
_A0='csiMatchHostInterface'
_z='csiMatchHostAddress'
_y='csiMatchHostAddressType'
_x='csiMatchSwitchProductId'
_w='csiMatchSwitchNum'
_v='csiMatchProductId'
_u='csiMatchGroupType'
_t='csiProfileRowStatus'
_s='csiProfileStorageType'
_r='csiProfileConfigUrl'
_q='csiProfileImageTwoUrl'
_p='csiProfileImageUrl'
_o='csiProfileGroupName'
_n='csiProfileNextFreeIndex'
_m='csiHostnamePrefix'
_l='csiConfigFileUrl'
_k='csiImageFileUrl'
_j='csiJoinWindowPeriodStorageType'
_i='csiJoinWindowPeriodRowStatus'
_h='csiJoinWindowPeriodExpirationDate'
_g='csiJoinWindowPeriodRecurrencePattern'
_f='csiJoinWindowPeriodInterval'
_e='csiJoinWindowPeriodStartTime'
_d='csiJoinWindowPeriodNextFreeIndex'
_c='csiJoinWindowConfigOperationMode'
_b='csiBackupHostUrl'
_a='csiBackupEnable'
_Z='csiManagementVlansSecond2K'
_Y='csiManagementVlansFirst2K'
_X='csiManagementVlan'
_W='csiDirectorIpAddress'
_V='csiDirectorIpAddressType'
_U='csiDeviceNum'
_T='csiMatchIndex'
_S='csiJoinWindowPeriodIndex'
_R='csiNotifOperationResult'
_Q='csiNotifOperationType'
_P='csiOperationMode'
_O='csiProfileIndex'
_N='Unsigned32'
_M='SnmpAdminString'
_L='not-accessible'
_K='StorageType'
_J='csiDeviceName'
_I='csiDeviceAddress'
_H='csiDeviceAddressType'
_G='csiDeviceMacAddress'
_F='Integer32'
_E='read-write'
_D='read-only'
_C='read-create'
_B='current'
_A='CISCO-SMART-INSTALL-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
Cisco2KVlanList,CiscoURLStringOrEmpty,TimeIntervalMin=mibBuilder.importSymbols('CISCO-TC','Cisco2KVlanList','CiscoURLStringOrEmpty','TimeIntervalMin')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_M)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_N,'iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,StorageType,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowStatus',_K,'TextualConvention','TruthValue')
ciscoSmartInstallMIB=ModuleIdentity((1,3,6,1,4,1,9,9,725))
if mibBuilder.loadTexts:ciscoSmartInstallMIB.setRevisions(('2010-04-30 00:00',))
_CiscoSmartInstallMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoSmartInstallMIBNotifs=_CiscoSmartInstallMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,725,0))
_CiscoSmartInstallMIBObjects_ObjectIdentity=ObjectIdentity
ciscoSmartInstallMIBObjects=_CiscoSmartInstallMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,725,1))
_CsiGlobalConfig_ObjectIdentity=ObjectIdentity
csiGlobalConfig=_CsiGlobalConfig_ObjectIdentity((1,3,6,1,4,1,9,9,725,1,1))
class _CsiOperationMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('disabled',1),('basic',2)))
_CsiOperationMode_Type.__name__=_F
_CsiOperationMode_Object=MibScalar
csiOperationMode=_CsiOperationMode_Object((1,3,6,1,4,1,9,9,725,1,1,1),_CsiOperationMode_Type())
csiOperationMode.setMaxAccess(_E)
if mibBuilder.loadTexts:csiOperationMode.setStatus(_B)
_CsiDirectorIpAddressType_Type=InetAddressType
_CsiDirectorIpAddressType_Object=MibScalar
csiDirectorIpAddressType=_CsiDirectorIpAddressType_Object((1,3,6,1,4,1,9,9,725,1,1,2),_CsiDirectorIpAddressType_Type())
csiDirectorIpAddressType.setMaxAccess(_E)
if mibBuilder.loadTexts:csiDirectorIpAddressType.setStatus(_B)
_CsiDirectorIpAddress_Type=InetAddress
_CsiDirectorIpAddress_Object=MibScalar
csiDirectorIpAddress=_CsiDirectorIpAddress_Object((1,3,6,1,4,1,9,9,725,1,1,3),_CsiDirectorIpAddress_Type())
csiDirectorIpAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:csiDirectorIpAddress.setStatus(_B)
_CsiManagementVlan_Type=TruthValue
_CsiManagementVlan_Object=MibScalar
csiManagementVlan=_CsiManagementVlan_Object((1,3,6,1,4,1,9,9,725,1,1,4),_CsiManagementVlan_Type())
csiManagementVlan.setMaxAccess(_D)
if mibBuilder.loadTexts:csiManagementVlan.setStatus(_B)
_CsiManagementVlansFirst2K_Type=Cisco2KVlanList
_CsiManagementVlansFirst2K_Object=MibScalar
csiManagementVlansFirst2K=_CsiManagementVlansFirst2K_Object((1,3,6,1,4,1,9,9,725,1,1,5),_CsiManagementVlansFirst2K_Type())
csiManagementVlansFirst2K.setMaxAccess(_E)
if mibBuilder.loadTexts:csiManagementVlansFirst2K.setStatus(_B)
_CsiManagementVlansSecond2K_Type=Cisco2KVlanList
_CsiManagementVlansSecond2K_Object=MibScalar
csiManagementVlansSecond2K=_CsiManagementVlansSecond2K_Object((1,3,6,1,4,1,9,9,725,1,1,6),_CsiManagementVlansSecond2K_Type())
csiManagementVlansSecond2K.setMaxAccess(_E)
if mibBuilder.loadTexts:csiManagementVlansSecond2K.setStatus(_B)
_CsiBackup_ObjectIdentity=ObjectIdentity
csiBackup=_CsiBackup_ObjectIdentity((1,3,6,1,4,1,9,9,725,1,1,7))
_CsiBackupHostUrl_Type=CiscoURLStringOrEmpty
_CsiBackupHostUrl_Object=MibScalar
csiBackupHostUrl=_CsiBackupHostUrl_Object((1,3,6,1,4,1,9,9,725,1,1,7,1),_CsiBackupHostUrl_Type())
csiBackupHostUrl.setMaxAccess(_E)
if mibBuilder.loadTexts:csiBackupHostUrl.setStatus(_B)
_CsiBackupEnable_Type=TruthValue
_CsiBackupEnable_Object=MibScalar
csiBackupEnable=_CsiBackupEnable_Object((1,3,6,1,4,1,9,9,725,1,1,7,2),_CsiBackupEnable_Type())
csiBackupEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:csiBackupEnable.setStatus(_B)
_CsiJoinWindow_ObjectIdentity=ObjectIdentity
csiJoinWindow=_CsiJoinWindow_ObjectIdentity((1,3,6,1,4,1,9,9,725,1,1,8))
class _CsiJoinWindowConfigOperationMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('closed',1),('auto',2),('manual',3)))
_CsiJoinWindowConfigOperationMode_Type.__name__=_F
_CsiJoinWindowConfigOperationMode_Object=MibScalar
csiJoinWindowConfigOperationMode=_CsiJoinWindowConfigOperationMode_Object((1,3,6,1,4,1,9,9,725,1,1,8,1),_CsiJoinWindowConfigOperationMode_Type())
csiJoinWindowConfigOperationMode.setMaxAccess(_E)
if mibBuilder.loadTexts:csiJoinWindowConfigOperationMode.setStatus(_B)
class _CsiJoinWindowPeriodNextFreeIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CsiJoinWindowPeriodNextFreeIndex_Type.__name__=_N
_CsiJoinWindowPeriodNextFreeIndex_Object=MibScalar
csiJoinWindowPeriodNextFreeIndex=_CsiJoinWindowPeriodNextFreeIndex_Object((1,3,6,1,4,1,9,9,725,1,1,8,2),_CsiJoinWindowPeriodNextFreeIndex_Type())
csiJoinWindowPeriodNextFreeIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:csiJoinWindowPeriodNextFreeIndex.setStatus(_B)
_CsiJoinWindowPeriodTable_Object=MibTable
csiJoinWindowPeriodTable=_CsiJoinWindowPeriodTable_Object((1,3,6,1,4,1,9,9,725,1,1,8,3))
if mibBuilder.loadTexts:csiJoinWindowPeriodTable.setStatus(_B)
_CsiJoinWindowPeriodEntry_Object=MibTableRow
csiJoinWindowPeriodEntry=_CsiJoinWindowPeriodEntry_Object((1,3,6,1,4,1,9,9,725,1,1,8,3,1))
csiJoinWindowPeriodEntry.setIndexNames((0,_A,_S))
if mibBuilder.loadTexts:csiJoinWindowPeriodEntry.setStatus(_B)
_CsiJoinWindowPeriodIndex_Type=Unsigned32
_CsiJoinWindowPeriodIndex_Object=MibTableColumn
csiJoinWindowPeriodIndex=_CsiJoinWindowPeriodIndex_Object((1,3,6,1,4,1,9,9,725,1,1,8,3,1,1),_CsiJoinWindowPeriodIndex_Type())
csiJoinWindowPeriodIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:csiJoinWindowPeriodIndex.setStatus(_B)
_CsiJoinWindowPeriodStartTime_Type=DateAndTime
_CsiJoinWindowPeriodStartTime_Object=MibTableColumn
csiJoinWindowPeriodStartTime=_CsiJoinWindowPeriodStartTime_Object((1,3,6,1,4,1,9,9,725,1,1,8,3,1,2),_CsiJoinWindowPeriodStartTime_Type())
csiJoinWindowPeriodStartTime.setMaxAccess(_C)
if mibBuilder.loadTexts:csiJoinWindowPeriodStartTime.setStatus(_B)
_CsiJoinWindowPeriodInterval_Type=TimeIntervalMin
_CsiJoinWindowPeriodInterval_Object=MibTableColumn
csiJoinWindowPeriodInterval=_CsiJoinWindowPeriodInterval_Object((1,3,6,1,4,1,9,9,725,1,1,8,3,1,3),_CsiJoinWindowPeriodInterval_Type())
csiJoinWindowPeriodInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:csiJoinWindowPeriodInterval.setStatus(_B)
class _CsiJoinWindowPeriodRecurrencePattern_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('none',1),('daily',2)))
_CsiJoinWindowPeriodRecurrencePattern_Type.__name__=_F
_CsiJoinWindowPeriodRecurrencePattern_Object=MibTableColumn
csiJoinWindowPeriodRecurrencePattern=_CsiJoinWindowPeriodRecurrencePattern_Object((1,3,6,1,4,1,9,9,725,1,1,8,3,1,4),_CsiJoinWindowPeriodRecurrencePattern_Type())
csiJoinWindowPeriodRecurrencePattern.setMaxAccess(_C)
if mibBuilder.loadTexts:csiJoinWindowPeriodRecurrencePattern.setStatus(_B)
_CsiJoinWindowPeriodExpirationDate_Type=DateAndTime
_CsiJoinWindowPeriodExpirationDate_Object=MibTableColumn
csiJoinWindowPeriodExpirationDate=_CsiJoinWindowPeriodExpirationDate_Object((1,3,6,1,4,1,9,9,725,1,1,8,3,1,5),_CsiJoinWindowPeriodExpirationDate_Type())
csiJoinWindowPeriodExpirationDate.setMaxAccess(_C)
if mibBuilder.loadTexts:csiJoinWindowPeriodExpirationDate.setStatus(_B)
class _CsiJoinWindowPeriodStorageType_Type(StorageType):defaultValue=2
_CsiJoinWindowPeriodStorageType_Type.__name__=_K
_CsiJoinWindowPeriodStorageType_Object=MibTableColumn
csiJoinWindowPeriodStorageType=_CsiJoinWindowPeriodStorageType_Object((1,3,6,1,4,1,9,9,725,1,1,8,3,1,6),_CsiJoinWindowPeriodStorageType_Type())
csiJoinWindowPeriodStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:csiJoinWindowPeriodStorageType.setStatus(_B)
_CsiJoinWindowPeriodRowStatus_Type=RowStatus
_CsiJoinWindowPeriodRowStatus_Object=MibTableColumn
csiJoinWindowPeriodRowStatus=_CsiJoinWindowPeriodRowStatus_Object((1,3,6,1,4,1,9,9,725,1,1,8,3,1,7),_CsiJoinWindowPeriodRowStatus_Type())
csiJoinWindowPeriodRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:csiJoinWindowPeriodRowStatus.setStatus(_B)
_CsiProfile_ObjectIdentity=ObjectIdentity
csiProfile=_CsiProfile_ObjectIdentity((1,3,6,1,4,1,9,9,725,1,2))
_CsiImageFileUrl_Type=CiscoURLStringOrEmpty
_CsiImageFileUrl_Object=MibScalar
csiImageFileUrl=_CsiImageFileUrl_Object((1,3,6,1,4,1,9,9,725,1,2,1),_CsiImageFileUrl_Type())
csiImageFileUrl.setMaxAccess(_E)
if mibBuilder.loadTexts:csiImageFileUrl.setStatus(_B)
_CsiConfigFileUrl_Type=CiscoURLStringOrEmpty
_CsiConfigFileUrl_Object=MibScalar
csiConfigFileUrl=_CsiConfigFileUrl_Object((1,3,6,1,4,1,9,9,725,1,2,2),_CsiConfigFileUrl_Type())
csiConfigFileUrl.setMaxAccess(_E)
if mibBuilder.loadTexts:csiConfigFileUrl.setStatus(_B)
class _CsiHostnamePrefix_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_CsiHostnamePrefix_Type.__name__=_M
_CsiHostnamePrefix_Object=MibScalar
csiHostnamePrefix=_CsiHostnamePrefix_Object((1,3,6,1,4,1,9,9,725,1,2,3),_CsiHostnamePrefix_Type())
csiHostnamePrefix.setMaxAccess(_E)
if mibBuilder.loadTexts:csiHostnamePrefix.setStatus(_B)
class _CsiProfileNextFreeIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(2,4294967295))
_CsiProfileNextFreeIndex_Type.__name__=_N
_CsiProfileNextFreeIndex_Object=MibScalar
csiProfileNextFreeIndex=_CsiProfileNextFreeIndex_Object((1,3,6,1,4,1,9,9,725,1,2,4),_CsiProfileNextFreeIndex_Type())
csiProfileNextFreeIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:csiProfileNextFreeIndex.setStatus(_B)
_CsiProfileTable_Object=MibTable
csiProfileTable=_CsiProfileTable_Object((1,3,6,1,4,1,9,9,725,1,2,5))
if mibBuilder.loadTexts:csiProfileTable.setStatus(_B)
_CsiProfileEntry_Object=MibTableRow
csiProfileEntry=_CsiProfileEntry_Object((1,3,6,1,4,1,9,9,725,1,2,5,1))
csiProfileEntry.setIndexNames((0,_A,_O))
if mibBuilder.loadTexts:csiProfileEntry.setStatus(_B)
_CsiProfileIndex_Type=Unsigned32
_CsiProfileIndex_Object=MibTableColumn
csiProfileIndex=_CsiProfileIndex_Object((1,3,6,1,4,1,9,9,725,1,2,5,1,1),_CsiProfileIndex_Type())
csiProfileIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:csiProfileIndex.setStatus(_B)
class _CsiProfileGroupName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CsiProfileGroupName_Type.__name__=_M
_CsiProfileGroupName_Object=MibTableColumn
csiProfileGroupName=_CsiProfileGroupName_Object((1,3,6,1,4,1,9,9,725,1,2,5,1,2),_CsiProfileGroupName_Type())
csiProfileGroupName.setMaxAccess(_C)
if mibBuilder.loadTexts:csiProfileGroupName.setStatus(_B)
_CsiProfileImageUrl_Type=CiscoURLStringOrEmpty
_CsiProfileImageUrl_Object=MibTableColumn
csiProfileImageUrl=_CsiProfileImageUrl_Object((1,3,6,1,4,1,9,9,725,1,2,5,1,3),_CsiProfileImageUrl_Type())
csiProfileImageUrl.setMaxAccess(_C)
if mibBuilder.loadTexts:csiProfileImageUrl.setStatus(_B)
_CsiProfileImageTwoUrl_Type=CiscoURLStringOrEmpty
_CsiProfileImageTwoUrl_Object=MibTableColumn
csiProfileImageTwoUrl=_CsiProfileImageTwoUrl_Object((1,3,6,1,4,1,9,9,725,1,2,5,1,4),_CsiProfileImageTwoUrl_Type())
csiProfileImageTwoUrl.setMaxAccess(_C)
if mibBuilder.loadTexts:csiProfileImageTwoUrl.setStatus(_B)
_CsiProfileConfigUrl_Type=CiscoURLStringOrEmpty
_CsiProfileConfigUrl_Object=MibTableColumn
csiProfileConfigUrl=_CsiProfileConfigUrl_Object((1,3,6,1,4,1,9,9,725,1,2,5,1,5),_CsiProfileConfigUrl_Type())
csiProfileConfigUrl.setMaxAccess(_C)
if mibBuilder.loadTexts:csiProfileConfigUrl.setStatus(_B)
class _CsiProfileStorageType_Type(StorageType):defaultValue=2
_CsiProfileStorageType_Type.__name__=_K
_CsiProfileStorageType_Object=MibTableColumn
csiProfileStorageType=_CsiProfileStorageType_Object((1,3,6,1,4,1,9,9,725,1,2,5,1,6),_CsiProfileStorageType_Type())
csiProfileStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:csiProfileStorageType.setStatus(_B)
_CsiProfileRowStatus_Type=RowStatus
_CsiProfileRowStatus_Object=MibTableColumn
csiProfileRowStatus=_CsiProfileRowStatus_Object((1,3,6,1,4,1,9,9,725,1,2,5,1,7),_CsiProfileRowStatus_Type())
csiProfileRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:csiProfileRowStatus.setStatus(_B)
_CsiMatchTable_Object=MibTable
csiMatchTable=_CsiMatchTable_Object((1,3,6,1,4,1,9,9,725,1,2,6))
if mibBuilder.loadTexts:csiMatchTable.setStatus(_B)
_CsiMatchEntry_Object=MibTableRow
csiMatchEntry=_CsiMatchEntry_Object((1,3,6,1,4,1,9,9,725,1,2,6,1))
csiMatchEntry.setIndexNames((0,_A,_O),(0,_A,_T))
if mibBuilder.loadTexts:csiMatchEntry.setStatus(_B)
_CsiMatchIndex_Type=Unsigned32
_CsiMatchIndex_Object=MibTableColumn
csiMatchIndex=_CsiMatchIndex_Object((1,3,6,1,4,1,9,9,725,1,2,6,1,1),_CsiMatchIndex_Type())
csiMatchIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:csiMatchIndex.setStatus(_B)
class _CsiMatchGroupType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('unknown',1),('mac',2),('connectivity',3),('product',4),('stack',5)))
_CsiMatchGroupType_Type.__name__=_F
_CsiMatchGroupType_Object=MibTableColumn
csiMatchGroupType=_CsiMatchGroupType_Object((1,3,6,1,4,1,9,9,725,1,2,6,1,2),_CsiMatchGroupType_Type())
csiMatchGroupType.setMaxAccess(_C)
if mibBuilder.loadTexts:csiMatchGroupType.setStatus(_B)
_CsiMatchMacAddress_Type=MacAddress
_CsiMatchMacAddress_Object=MibTableColumn
csiMatchMacAddress=_CsiMatchMacAddress_Object((1,3,6,1,4,1,9,9,725,1,2,6,1,3),_CsiMatchMacAddress_Type())
csiMatchMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:csiMatchMacAddress.setStatus(_B)
_CsiMatchHostAddressType_Type=InetAddressType
_CsiMatchHostAddressType_Object=MibTableColumn
csiMatchHostAddressType=_CsiMatchHostAddressType_Object((1,3,6,1,4,1,9,9,725,1,2,6,1,4),_CsiMatchHostAddressType_Type())
csiMatchHostAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:csiMatchHostAddressType.setStatus(_B)
_CsiMatchHostAddress_Type=InetAddress
_CsiMatchHostAddress_Object=MibTableColumn
csiMatchHostAddress=_CsiMatchHostAddress_Object((1,3,6,1,4,1,9,9,725,1,2,6,1,5),_CsiMatchHostAddress_Type())
csiMatchHostAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:csiMatchHostAddress.setStatus(_B)
_CsiMatchHostInterface_Type=SnmpAdminString
_CsiMatchHostInterface_Object=MibTableColumn
csiMatchHostInterface=_CsiMatchHostInterface_Object((1,3,6,1,4,1,9,9,725,1,2,6,1,6),_CsiMatchHostInterface_Type())
csiMatchHostInterface.setMaxAccess(_C)
if mibBuilder.loadTexts:csiMatchHostInterface.setStatus(_B)
_CsiMatchProductId_Type=SnmpAdminString
_CsiMatchProductId_Object=MibTableColumn
csiMatchProductId=_CsiMatchProductId_Object((1,3,6,1,4,1,9,9,725,1,2,6,1,7),_CsiMatchProductId_Type())
csiMatchProductId.setMaxAccess(_C)
if mibBuilder.loadTexts:csiMatchProductId.setStatus(_B)
_CsiMatchSwitchNum_Type=Unsigned32
_CsiMatchSwitchNum_Object=MibTableColumn
csiMatchSwitchNum=_CsiMatchSwitchNum_Object((1,3,6,1,4,1,9,9,725,1,2,6,1,8),_CsiMatchSwitchNum_Type())
csiMatchSwitchNum.setMaxAccess(_C)
if mibBuilder.loadTexts:csiMatchSwitchNum.setStatus(_B)
_CsiMatchSwitchProductId_Type=SnmpAdminString
_CsiMatchSwitchProductId_Object=MibTableColumn
csiMatchSwitchProductId=_CsiMatchSwitchProductId_Object((1,3,6,1,4,1,9,9,725,1,2,6,1,9),_CsiMatchSwitchProductId_Type())
csiMatchSwitchProductId.setMaxAccess(_C)
if mibBuilder.loadTexts:csiMatchSwitchProductId.setStatus(_B)
class _CsiMatchStorageType_Type(StorageType):defaultValue=2
_CsiMatchStorageType_Type.__name__=_K
_CsiMatchStorageType_Object=MibTableColumn
csiMatchStorageType=_CsiMatchStorageType_Object((1,3,6,1,4,1,9,9,725,1,2,6,1,10),_CsiMatchStorageType_Type())
csiMatchStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:csiMatchStorageType.setStatus(_B)
_CsiMatchRowStatus_Type=RowStatus
_CsiMatchRowStatus_Object=MibTableColumn
csiMatchRowStatus=_CsiMatchRowStatus_Object((1,3,6,1,4,1,9,9,725,1,2,6,1,11),_CsiMatchRowStatus_Type())
csiMatchRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:csiMatchRowStatus.setStatus(_B)
_CsiDeviceInfo_ObjectIdentity=ObjectIdentity
csiDeviceInfo=_CsiDeviceInfo_ObjectIdentity((1,3,6,1,4,1,9,9,725,1,3))
_CsiDeviceTable_Object=MibTable
csiDeviceTable=_CsiDeviceTable_Object((1,3,6,1,4,1,9,9,725,1,3,1))
if mibBuilder.loadTexts:csiDeviceTable.setStatus(_B)
_CsiDeviceEntry_Object=MibTableRow
csiDeviceEntry=_CsiDeviceEntry_Object((1,3,6,1,4,1,9,9,725,1,3,1,1))
csiDeviceEntry.setIndexNames((0,_A,_U))
if mibBuilder.loadTexts:csiDeviceEntry.setStatus(_B)
_CsiDeviceNum_Type=Unsigned32
_CsiDeviceNum_Object=MibTableColumn
csiDeviceNum=_CsiDeviceNum_Object((1,3,6,1,4,1,9,9,725,1,3,1,1,1),_CsiDeviceNum_Type())
csiDeviceNum.setMaxAccess(_L)
if mibBuilder.loadTexts:csiDeviceNum.setStatus(_B)
_CsiDeviceMacAddress_Type=MacAddress
_CsiDeviceMacAddress_Object=MibTableColumn
csiDeviceMacAddress=_CsiDeviceMacAddress_Object((1,3,6,1,4,1,9,9,725,1,3,1,1,2),_CsiDeviceMacAddress_Type())
csiDeviceMacAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:csiDeviceMacAddress.setStatus(_B)
_CsiDeviceAddressType_Type=InetAddressType
_CsiDeviceAddressType_Object=MibTableColumn
csiDeviceAddressType=_CsiDeviceAddressType_Object((1,3,6,1,4,1,9,9,725,1,3,1,1,3),_CsiDeviceAddressType_Type())
csiDeviceAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:csiDeviceAddressType.setStatus(_B)
_CsiDeviceAddress_Type=InetAddress
_CsiDeviceAddress_Object=MibTableColumn
csiDeviceAddress=_CsiDeviceAddress_Object((1,3,6,1,4,1,9,9,725,1,3,1,1,4),_CsiDeviceAddress_Type())
csiDeviceAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:csiDeviceAddress.setStatus(_B)
_CsiDeviceName_Type=SnmpAdminString
_CsiDeviceName_Object=MibTableColumn
csiDeviceName=_CsiDeviceName_Object((1,3,6,1,4,1,9,9,725,1,3,1,1,5),_CsiDeviceName_Type())
csiDeviceName.setMaxAccess(_D)
if mibBuilder.loadTexts:csiDeviceName.setStatus(_B)
_CsiDeviceBackupConfigFileName_Type=SnmpAdminString
_CsiDeviceBackupConfigFileName_Object=MibTableColumn
csiDeviceBackupConfigFileName=_CsiDeviceBackupConfigFileName_Object((1,3,6,1,4,1,9,9,725,1,3,1,1,6),_CsiDeviceBackupConfigFileName_Type())
csiDeviceBackupConfigFileName.setMaxAccess(_D)
if mibBuilder.loadTexts:csiDeviceBackupConfigFileName.setStatus(_B)
_CsiDeviceImageVersion_Type=SnmpAdminString
_CsiDeviceImageVersion_Object=MibTableColumn
csiDeviceImageVersion=_CsiDeviceImageVersion_Object((1,3,6,1,4,1,9,9,725,1,3,1,1,7),_CsiDeviceImageVersion_Type())
csiDeviceImageVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:csiDeviceImageVersion.setStatus(_B)
_CsiDevicePlatform_Type=SnmpAdminString
_CsiDevicePlatform_Object=MibTableColumn
csiDevicePlatform=_CsiDevicePlatform_Object((1,3,6,1,4,1,9,9,725,1,3,1,1,8),_CsiDevicePlatform_Type())
csiDevicePlatform.setMaxAccess(_D)
if mibBuilder.loadTexts:csiDevicePlatform.setStatus(_B)
_CsiDeviceSerialNum_Type=SnmpAdminString
_CsiDeviceSerialNum_Object=MibTableColumn
csiDeviceSerialNum=_CsiDeviceSerialNum_Object((1,3,6,1,4,1,9,9,725,1,3,1,1,9),_CsiDeviceSerialNum_Type())
csiDeviceSerialNum.setMaxAccess(_D)
if mibBuilder.loadTexts:csiDeviceSerialNum.setStatus(_B)
_CsiDeviceStatus_Type=SnmpAdminString
_CsiDeviceStatus_Object=MibTableColumn
csiDeviceStatus=_CsiDeviceStatus_Object((1,3,6,1,4,1,9,9,725,1,3,1,1,10),_CsiDeviceStatus_Type())
csiDeviceStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:csiDeviceStatus.setStatus(_B)
_CsiNotifObjects_ObjectIdentity=ObjectIdentity
csiNotifObjects=_CsiNotifObjects_ObjectIdentity((1,3,6,1,4,1,9,9,725,1,4))
class _CsiNotifEnable_Type(Bits):namedValues=NamedValues(*(('operationModeChange',0),('deviceAdded',1),('deviceLost',2),('fileLoadFailed',3)))
_CsiNotifEnable_Type.__name__='Bits'
_CsiNotifEnable_Object=MibScalar
csiNotifEnable=_CsiNotifEnable_Object((1,3,6,1,4,1,9,9,725,1,4,1),_CsiNotifEnable_Type())
csiNotifEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:csiNotifEnable.setStatus(_B)
class _CsiNotifOperationType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('other',1),('downloadConfig',2),('downloadImage',3),('uploadConfig',4)))
_CsiNotifOperationType_Type.__name__=_F
_CsiNotifOperationType_Object=MibScalar
csiNotifOperationType=_CsiNotifOperationType_Object((1,3,6,1,4,1,9,9,725,1,4,2),_CsiNotifOperationType_Type())
csiNotifOperationType.setMaxAccess(_D)
if mibBuilder.loadTexts:csiNotifOperationType.setStatus(_B)
_CsiNotifOperationResult_Type=SnmpAdminString
_CsiNotifOperationResult_Object=MibScalar
csiNotifOperationResult=_CsiNotifOperationResult_Object((1,3,6,1,4,1,9,9,725,1,4,3),_CsiNotifOperationResult_Type())
csiNotifOperationResult.setMaxAccess(_D)
if mibBuilder.loadTexts:csiNotifOperationResult.setStatus(_B)
_CiscoSmartInstallMIBConform_ObjectIdentity=ObjectIdentity
ciscoSmartInstallMIBConform=_CiscoSmartInstallMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,725,2))
_CiscoSmartInstallCompliances_ObjectIdentity=ObjectIdentity
ciscoSmartInstallCompliances=_CiscoSmartInstallCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,725,2,1))
_CiscoSmartInstallGroups_ObjectIdentity=ObjectIdentity
ciscoSmartInstallGroups=_CiscoSmartInstallGroups_ObjectIdentity((1,3,6,1,4,1,9,9,725,2,2))
ciscoSmartInstallGlobalConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,725,2,2,1))
ciscoSmartInstallGlobalConfigGroup.setObjects(*((_A,_P),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z)))
if mibBuilder.loadTexts:ciscoSmartInstallGlobalConfigGroup.setStatus(_B)
ciscoSmartInstallConfigBackupGroup=ObjectGroup((1,3,6,1,4,1,9,9,725,2,2,2))
ciscoSmartInstallConfigBackupGroup.setObjects(*((_A,_a),(_A,_b)))
if mibBuilder.loadTexts:ciscoSmartInstallConfigBackupGroup.setStatus(_B)
ciscoSmartInstallJoinWindowGroup=ObjectGroup((1,3,6,1,4,1,9,9,725,2,2,3))
ciscoSmartInstallJoinWindowGroup.setObjects(*((_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j)))
if mibBuilder.loadTexts:ciscoSmartInstallJoinWindowGroup.setStatus(_B)
ciscoSmartInstallProfileGroup=ObjectGroup((1,3,6,1,4,1,9,9,725,2,2,4))
ciscoSmartInstallProfileGroup.setObjects(*((_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3)))
if mibBuilder.loadTexts:ciscoSmartInstallProfileGroup.setStatus(_B)
ciscoSmartInstallDeviceInformationGroup=ObjectGroup((1,3,6,1,4,1,9,9,725,2,2,5))
ciscoSmartInstallDeviceInformationGroup.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_A4),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_A8)))
if mibBuilder.loadTexts:ciscoSmartInstallDeviceInformationGroup.setStatus(_B)
ciscoSmartInstallNotificationEnableGroup=ObjectGroup((1,3,6,1,4,1,9,9,725,2,2,6))
ciscoSmartInstallNotificationEnableGroup.setObjects((_A,_A9))
if mibBuilder.loadTexts:ciscoSmartInstallNotificationEnableGroup.setStatus(_B)
ciscoSmartInstallNotifyVarsGroup=ObjectGroup((1,3,6,1,4,1,9,9,725,2,2,8))
ciscoSmartInstallNotifyVarsGroup.setObjects(*((_A,_Q),(_A,_R)))
if mibBuilder.loadTexts:ciscoSmartInstallNotifyVarsGroup.setStatus(_B)
csiOperationModeChange=NotificationType((1,3,6,1,4,1,9,9,725,0,1))
csiOperationModeChange.setObjects((_A,_P))
if mibBuilder.loadTexts:csiOperationModeChange.setStatus(_B)
csiDeviceAdded=NotificationType((1,3,6,1,4,1,9,9,725,0,2))
csiDeviceAdded.setObjects(*((_A,_J),(_A,_H),(_A,_I),(_A,_G)))
if mibBuilder.loadTexts:csiDeviceAdded.setStatus(_B)
csiDeviceLost=NotificationType((1,3,6,1,4,1,9,9,725,0,3))
csiDeviceLost.setObjects(*((_A,_J),(_A,_H),(_A,_I),(_A,_G)))
if mibBuilder.loadTexts:csiDeviceLost.setStatus(_B)
csiFileLoadFailed=NotificationType((1,3,6,1,4,1,9,9,725,0,4))
csiFileLoadFailed.setObjects(*((_A,_J),(_A,_H),(_A,_I),(_A,_G),(_A,_Q),(_A,_R)))
if mibBuilder.loadTexts:csiFileLoadFailed.setStatus(_B)
ciscoSmartInstallNotificationsGroup=NotificationGroup((1,3,6,1,4,1,9,9,725,2,2,7))
ciscoSmartInstallNotificationsGroup.setObjects(*((_A,_AA),(_A,_AB),(_A,_AC),(_A,_AD)))
if mibBuilder.loadTexts:ciscoSmartInstallNotificationsGroup.setStatus(_B)
ciscoSmartInstallCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,725,2,1,1))
ciscoSmartInstallCompliance.setObjects(*((_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ),(_A,_AK),(_A,_AL)))
if mibBuilder.loadTexts:ciscoSmartInstallCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ciscoSmartInstallMIB':ciscoSmartInstallMIB,'ciscoSmartInstallMIBNotifs':ciscoSmartInstallMIBNotifs,_AA:csiOperationModeChange,_AB:csiDeviceAdded,_AC:csiDeviceLost,_AD:csiFileLoadFailed,'ciscoSmartInstallMIBObjects':ciscoSmartInstallMIBObjects,'csiGlobalConfig':csiGlobalConfig,_P:csiOperationMode,_V:csiDirectorIpAddressType,_W:csiDirectorIpAddress,_X:csiManagementVlan,_Y:csiManagementVlansFirst2K,_Z:csiManagementVlansSecond2K,'csiBackup':csiBackup,_b:csiBackupHostUrl,_a:csiBackupEnable,'csiJoinWindow':csiJoinWindow,_c:csiJoinWindowConfigOperationMode,_d:csiJoinWindowPeriodNextFreeIndex,'csiJoinWindowPeriodTable':csiJoinWindowPeriodTable,'csiJoinWindowPeriodEntry':csiJoinWindowPeriodEntry,_S:csiJoinWindowPeriodIndex,_e:csiJoinWindowPeriodStartTime,_f:csiJoinWindowPeriodInterval,_g:csiJoinWindowPeriodRecurrencePattern,_h:csiJoinWindowPeriodExpirationDate,_j:csiJoinWindowPeriodStorageType,_i:csiJoinWindowPeriodRowStatus,'csiProfile':csiProfile,_k:csiImageFileUrl,_l:csiConfigFileUrl,_m:csiHostnamePrefix,_n:csiProfileNextFreeIndex,'csiProfileTable':csiProfileTable,'csiProfileEntry':csiProfileEntry,_O:csiProfileIndex,_o:csiProfileGroupName,_p:csiProfileImageUrl,_q:csiProfileImageTwoUrl,_r:csiProfileConfigUrl,_s:csiProfileStorageType,_t:csiProfileRowStatus,'csiMatchTable':csiMatchTable,'csiMatchEntry':csiMatchEntry,_T:csiMatchIndex,_u:csiMatchGroupType,_A1:csiMatchMacAddress,_y:csiMatchHostAddressType,_z:csiMatchHostAddress,_A0:csiMatchHostInterface,_v:csiMatchProductId,_w:csiMatchSwitchNum,_x:csiMatchSwitchProductId,_A2:csiMatchStorageType,_A3:csiMatchRowStatus,'csiDeviceInfo':csiDeviceInfo,'csiDeviceTable':csiDeviceTable,'csiDeviceEntry':csiDeviceEntry,_U:csiDeviceNum,_G:csiDeviceMacAddress,_H:csiDeviceAddressType,_I:csiDeviceAddress,_J:csiDeviceName,_A4:csiDeviceBackupConfigFileName,_A5:csiDeviceImageVersion,_A6:csiDevicePlatform,_A7:csiDeviceSerialNum,_A8:csiDeviceStatus,'csiNotifObjects':csiNotifObjects,_A9:csiNotifEnable,_Q:csiNotifOperationType,_R:csiNotifOperationResult,'ciscoSmartInstallMIBConform':ciscoSmartInstallMIBConform,'ciscoSmartInstallCompliances':ciscoSmartInstallCompliances,'ciscoSmartInstallCompliance':ciscoSmartInstallCompliance,'ciscoSmartInstallGroups':ciscoSmartInstallGroups,_AE:ciscoSmartInstallGlobalConfigGroup,_AG:ciscoSmartInstallConfigBackupGroup,_AH:ciscoSmartInstallJoinWindowGroup,_AI:ciscoSmartInstallProfileGroup,_AF:ciscoSmartInstallDeviceInformationGroup,_AJ:ciscoSmartInstallNotificationEnableGroup,_AK:ciscoSmartInstallNotificationsGroup,_AL:ciscoSmartInstallNotifyVarsGroup})