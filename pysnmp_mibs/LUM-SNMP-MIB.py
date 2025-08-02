_y='snmpUserGroupV2'
_x='snmpGeneralGroupV6'
_w='snmpGeneralGroup'
_v='snmpUserPrivProtocol'
_u='snmpUserChangePrivPassword'
_t='snmpUserPrivKey'
_s='snmpGeneralSecurityPolicy'
_r='snmpInformSinkMib2Notifications'
_q='public'
_p='snmpGeneralGroupV5'
_o='snmpGeneralGroupV4'
_n='snmpInformSinkGroupV2'
_m='snmpGeneralGroupV3'
_l='snmpGeneralGroupV2'
_k='snmpGeneralResetEngineIDCommand'
_j='snmpInformSinkOtherNotifications'
_i='snmpInformSinkPerformanceNotifications'
_h='snmpInformSinkAlarmNotifications'
_g='snmpInformSinkStorageType'
_f='snmpUserAuthKey'
_e='snmpUserEngineId'
_d='snmpUserChangePassword'
_c='snmpUserName'
_b='CommandString'
_a='snmpGeneralUserTableSize'
_Z='snmpGeneralInformSinkTableSize'
_Y='snmpInformSinkRowStatus'
_X='snmpInformSinkCommunity'
_W='snmpInformSinkPort'
_V='snmpInformSinkAddr'
_U='snmpInformSinkName'
_T='snmpUserIndex'
_S='on'
_R='off'
_Q='Unsigned32'
_P='snmpInformSinkGroupV3'
_O='snmpInformSinkGroup'
_N='snmpGeneralCommunity'
_M='read-create'
_L='snmpInformSinkIndex'
_K='DisplayString'
_J='snmpGeneralEngineID'
_I='snmpGeneralConfigLastChangeTime'
_H='snmpGeneralLastChangeTime'
_G='Integer32'
_F='snmpUserGroup'
_E='read-write'
_D='read-only'
_C='deprecated'
_B='current'
_A='LUM-SNMP-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
lumModules,lumSnmpMIB=mibBuilder.importSymbols('LUM-REG','lumModules','lumSnmpMIB')
CommandString,=mibBuilder.importSymbols('LUM-TC',_b)
SnmpEngineID,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpEngineID')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_Q,'iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_K,'PhysAddress','RowStatus','StorageType','TextualConvention')
lumSnmpMIBModule=ModuleIdentity((1,3,6,1,4,1,8708,1,1,18))
if mibBuilder.loadTexts:lumSnmpMIBModule.setRevisions(('2018-04-13 00:00','2017-06-15 00:00','2014-12-09 00:00','2008-06-05 00:00','2004-10-01 00:00','2004-06-23 00:00','2003-09-30 00:00','2002-05-30 00:00'))
_LumSnmpConfs_ObjectIdentity=ObjectIdentity
lumSnmpConfs=_LumSnmpConfs_ObjectIdentity((1,3,6,1,4,1,8708,2,17,1))
_LumSnmpGroups_ObjectIdentity=ObjectIdentity
lumSnmpGroups=_LumSnmpGroups_ObjectIdentity((1,3,6,1,4,1,8708,2,17,1,1))
_LumSnmpCompl_ObjectIdentity=ObjectIdentity
lumSnmpCompl=_LumSnmpCompl_ObjectIdentity((1,3,6,1,4,1,8708,2,17,1,2))
_LumSnmpMIBObjects_ObjectIdentity=ObjectIdentity
lumSnmpMIBObjects=_LumSnmpMIBObjects_ObjectIdentity((1,3,6,1,4,1,8708,2,17,2))
_SnmpInformSinkList_ObjectIdentity=ObjectIdentity
snmpInformSinkList=_SnmpInformSinkList_ObjectIdentity((1,3,6,1,4,1,8708,2,17,2,1))
_SnmpInformSinkTable_Object=MibTable
snmpInformSinkTable=_SnmpInformSinkTable_Object((1,3,6,1,4,1,8708,2,17,2,1,1))
if mibBuilder.loadTexts:snmpInformSinkTable.setStatus(_B)
_SnmpInformSinkEntry_Object=MibTableRow
snmpInformSinkEntry=_SnmpInformSinkEntry_Object((1,3,6,1,4,1,8708,2,17,2,1,1,1))
snmpInformSinkEntry.setIndexNames((0,_A,_L))
if mibBuilder.loadTexts:snmpInformSinkEntry.setStatus(_B)
class _SnmpInformSinkIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_SnmpInformSinkIndex_Type.__name__=_Q
_SnmpInformSinkIndex_Object=MibTableColumn
snmpInformSinkIndex=_SnmpInformSinkIndex_Object((1,3,6,1,4,1,8708,2,17,2,1,1,1,1),_SnmpInformSinkIndex_Type())
snmpInformSinkIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:snmpInformSinkIndex.setStatus(_B)
class _SnmpInformSinkName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SnmpInformSinkName_Type.__name__=_K
_SnmpInformSinkName_Object=MibTableColumn
snmpInformSinkName=_SnmpInformSinkName_Object((1,3,6,1,4,1,8708,2,17,2,1,1,1,2),_SnmpInformSinkName_Type())
snmpInformSinkName.setMaxAccess(_D)
if mibBuilder.loadTexts:snmpInformSinkName.setStatus(_B)
_SnmpInformSinkAddr_Type=IpAddress
_SnmpInformSinkAddr_Object=MibTableColumn
snmpInformSinkAddr=_SnmpInformSinkAddr_Object((1,3,6,1,4,1,8708,2,17,2,1,1,1,3),_SnmpInformSinkAddr_Type())
snmpInformSinkAddr.setMaxAccess(_M)
if mibBuilder.loadTexts:snmpInformSinkAddr.setStatus(_B)
class _SnmpInformSinkPort_Type(Unsigned32):defaultValue=162;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SnmpInformSinkPort_Type.__name__=_Q
_SnmpInformSinkPort_Object=MibTableColumn
snmpInformSinkPort=_SnmpInformSinkPort_Object((1,3,6,1,4,1,8708,2,17,2,1,1,1,4),_SnmpInformSinkPort_Type())
snmpInformSinkPort.setMaxAccess(_M)
if mibBuilder.loadTexts:snmpInformSinkPort.setStatus(_B)
class _SnmpInformSinkCommunity_Type(DisplayString):defaultValue=OctetString(_q);subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SnmpInformSinkCommunity_Type.__name__=_K
_SnmpInformSinkCommunity_Object=MibTableColumn
snmpInformSinkCommunity=_SnmpInformSinkCommunity_Object((1,3,6,1,4,1,8708,2,17,2,1,1,1,5),_SnmpInformSinkCommunity_Type())
snmpInformSinkCommunity.setMaxAccess(_E)
if mibBuilder.loadTexts:snmpInformSinkCommunity.setStatus(_B)
_SnmpInformSinkRowStatus_Type=RowStatus
_SnmpInformSinkRowStatus_Object=MibTableColumn
snmpInformSinkRowStatus=_SnmpInformSinkRowStatus_Object((1,3,6,1,4,1,8708,2,17,2,1,1,1,6),_SnmpInformSinkRowStatus_Type())
snmpInformSinkRowStatus.setMaxAccess(_M)
if mibBuilder.loadTexts:snmpInformSinkRowStatus.setStatus(_B)
_SnmpInformSinkStorageType_Type=StorageType
_SnmpInformSinkStorageType_Object=MibTableColumn
snmpInformSinkStorageType=_SnmpInformSinkStorageType_Object((1,3,6,1,4,1,8708,2,17,2,1,1,1,7),_SnmpInformSinkStorageType_Type())
snmpInformSinkStorageType.setMaxAccess(_M)
if mibBuilder.loadTexts:snmpInformSinkStorageType.setStatus(_B)
class _SnmpInformSinkAlarmNotifications_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_R,1),(_S,2)))
_SnmpInformSinkAlarmNotifications_Type.__name__=_G
_SnmpInformSinkAlarmNotifications_Object=MibTableColumn
snmpInformSinkAlarmNotifications=_SnmpInformSinkAlarmNotifications_Object((1,3,6,1,4,1,8708,2,17,2,1,1,1,8),_SnmpInformSinkAlarmNotifications_Type())
snmpInformSinkAlarmNotifications.setMaxAccess(_E)
if mibBuilder.loadTexts:snmpInformSinkAlarmNotifications.setStatus(_B)
class _SnmpInformSinkPerformanceNotifications_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_R,1),(_S,2)))
_SnmpInformSinkPerformanceNotifications_Type.__name__=_G
_SnmpInformSinkPerformanceNotifications_Object=MibTableColumn
snmpInformSinkPerformanceNotifications=_SnmpInformSinkPerformanceNotifications_Object((1,3,6,1,4,1,8708,2,17,2,1,1,1,9),_SnmpInformSinkPerformanceNotifications_Type())
snmpInformSinkPerformanceNotifications.setMaxAccess(_E)
if mibBuilder.loadTexts:snmpInformSinkPerformanceNotifications.setStatus(_B)
class _SnmpInformSinkOtherNotifications_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_R,1),(_S,2)))
_SnmpInformSinkOtherNotifications_Type.__name__=_G
_SnmpInformSinkOtherNotifications_Object=MibTableColumn
snmpInformSinkOtherNotifications=_SnmpInformSinkOtherNotifications_Object((1,3,6,1,4,1,8708,2,17,2,1,1,1,10),_SnmpInformSinkOtherNotifications_Type())
snmpInformSinkOtherNotifications.setMaxAccess(_E)
if mibBuilder.loadTexts:snmpInformSinkOtherNotifications.setStatus(_B)
class _SnmpInformSinkMib2Notifications_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_R,1),(_S,2)))
_SnmpInformSinkMib2Notifications_Type.__name__=_G
_SnmpInformSinkMib2Notifications_Object=MibTableColumn
snmpInformSinkMib2Notifications=_SnmpInformSinkMib2Notifications_Object((1,3,6,1,4,1,8708,2,17,2,1,1,1,11),_SnmpInformSinkMib2Notifications_Type())
snmpInformSinkMib2Notifications.setMaxAccess(_E)
if mibBuilder.loadTexts:snmpInformSinkMib2Notifications.setStatus(_B)
_SnmpGeneral_ObjectIdentity=ObjectIdentity
snmpGeneral=_SnmpGeneral_ObjectIdentity((1,3,6,1,4,1,8708,2,17,2,2))
_SnmpGeneralLastChangeTime_Type=DateAndTime
_SnmpGeneralLastChangeTime_Object=MibScalar
snmpGeneralLastChangeTime=_SnmpGeneralLastChangeTime_Object((1,3,6,1,4,1,8708,2,17,2,2,1),_SnmpGeneralLastChangeTime_Type())
snmpGeneralLastChangeTime.setMaxAccess(_D)
if mibBuilder.loadTexts:snmpGeneralLastChangeTime.setStatus(_B)
_SnmpGeneralConfigLastChangeTime_Type=DateAndTime
_SnmpGeneralConfigLastChangeTime_Object=MibScalar
snmpGeneralConfigLastChangeTime=_SnmpGeneralConfigLastChangeTime_Object((1,3,6,1,4,1,8708,2,17,2,2,2),_SnmpGeneralConfigLastChangeTime_Type())
snmpGeneralConfigLastChangeTime.setMaxAccess(_D)
if mibBuilder.loadTexts:snmpGeneralConfigLastChangeTime.setStatus(_B)
_SnmpGeneralEngineID_Type=SnmpEngineID
_SnmpGeneralEngineID_Object=MibScalar
snmpGeneralEngineID=_SnmpGeneralEngineID_Object((1,3,6,1,4,1,8708,2,17,2,2,3),_SnmpGeneralEngineID_Type())
snmpGeneralEngineID.setMaxAccess(_D)
if mibBuilder.loadTexts:snmpGeneralEngineID.setStatus(_B)
class _SnmpGeneralCommunity_Type(DisplayString):defaultValue=OctetString(_q);subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,33))
_SnmpGeneralCommunity_Type.__name__=_K
_SnmpGeneralCommunity_Object=MibScalar
snmpGeneralCommunity=_SnmpGeneralCommunity_Object((1,3,6,1,4,1,8708,2,17,2,2,4),_SnmpGeneralCommunity_Type())
snmpGeneralCommunity.setMaxAccess(_E)
if mibBuilder.loadTexts:snmpGeneralCommunity.setStatus(_B)
_SnmpGeneralInformSinkTableSize_Type=Unsigned32
_SnmpGeneralInformSinkTableSize_Object=MibScalar
snmpGeneralInformSinkTableSize=_SnmpGeneralInformSinkTableSize_Object((1,3,6,1,4,1,8708,2,17,2,2,5),_SnmpGeneralInformSinkTableSize_Type())
snmpGeneralInformSinkTableSize.setMaxAccess(_D)
if mibBuilder.loadTexts:snmpGeneralInformSinkTableSize.setStatus(_B)
_SnmpGeneralUserTableSize_Type=Unsigned32
_SnmpGeneralUserTableSize_Object=MibScalar
snmpGeneralUserTableSize=_SnmpGeneralUserTableSize_Object((1,3,6,1,4,1,8708,2,17,2,2,6),_SnmpGeneralUserTableSize_Type())
snmpGeneralUserTableSize.setMaxAccess(_D)
if mibBuilder.loadTexts:snmpGeneralUserTableSize.setStatus(_B)
_SnmpGeneralResetEngineIDCommand_Type=CommandString
_SnmpGeneralResetEngineIDCommand_Object=MibScalar
snmpGeneralResetEngineIDCommand=_SnmpGeneralResetEngineIDCommand_Object((1,3,6,1,4,1,8708,2,17,2,2,7),_SnmpGeneralResetEngineIDCommand_Type())
snmpGeneralResetEngineIDCommand.setMaxAccess(_D)
if mibBuilder.loadTexts:snmpGeneralResetEngineIDCommand.setStatus(_B)
class _SnmpGeneralSecurityPolicy_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('basic',1),('authentication',2),('authAndPrivacy',3)))
_SnmpGeneralSecurityPolicy_Type.__name__=_G
_SnmpGeneralSecurityPolicy_Object=MibScalar
snmpGeneralSecurityPolicy=_SnmpGeneralSecurityPolicy_Object((1,3,6,1,4,1,8708,2,17,2,2,8),_SnmpGeneralSecurityPolicy_Type())
snmpGeneralSecurityPolicy.setMaxAccess(_D)
if mibBuilder.loadTexts:snmpGeneralSecurityPolicy.setStatus(_B)
_SnmpUserList_ObjectIdentity=ObjectIdentity
snmpUserList=_SnmpUserList_ObjectIdentity((1,3,6,1,4,1,8708,2,17,2,3))
_SnmpUserTable_Object=MibTable
snmpUserTable=_SnmpUserTable_Object((1,3,6,1,4,1,8708,2,17,2,3,1))
if mibBuilder.loadTexts:snmpUserTable.setStatus(_B)
_SnmpUserEntry_Object=MibTableRow
snmpUserEntry=_SnmpUserEntry_Object((1,3,6,1,4,1,8708,2,17,2,3,1,1))
snmpUserEntry.setIndexNames((0,_A,_T))
if mibBuilder.loadTexts:snmpUserEntry.setStatus(_B)
class _SnmpUserIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_SnmpUserIndex_Type.__name__=_Q
_SnmpUserIndex_Object=MibTableColumn
snmpUserIndex=_SnmpUserIndex_Object((1,3,6,1,4,1,8708,2,17,2,3,1,1,1),_SnmpUserIndex_Type())
snmpUserIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:snmpUserIndex.setStatus(_B)
class _SnmpUserName_Type(DisplayString):defaultValue=OctetString('oper');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SnmpUserName_Type.__name__=_K
_SnmpUserName_Object=MibTableColumn
snmpUserName=_SnmpUserName_Object((1,3,6,1,4,1,8708,2,17,2,3,1,1,2),_SnmpUserName_Type())
snmpUserName.setMaxAccess(_M)
if mibBuilder.loadTexts:snmpUserName.setStatus(_B)
class _SnmpUserChangePassword_Type(CommandString):defaultValue=OctetString('1234567890')
_SnmpUserChangePassword_Type.__name__=_b
_SnmpUserChangePassword_Object=MibTableColumn
snmpUserChangePassword=_SnmpUserChangePassword_Object((1,3,6,1,4,1,8708,2,17,2,3,1,1,3),_SnmpUserChangePassword_Type())
snmpUserChangePassword.setMaxAccess(_E)
if mibBuilder.loadTexts:snmpUserChangePassword.setStatus(_B)
_SnmpUserEngineId_Type=SnmpEngineID
_SnmpUserEngineId_Object=MibTableColumn
snmpUserEngineId=_SnmpUserEngineId_Object((1,3,6,1,4,1,8708,2,17,2,3,1,1,4),_SnmpUserEngineId_Type())
snmpUserEngineId.setMaxAccess(_E)
if mibBuilder.loadTexts:snmpUserEngineId.setStatus(_B)
_SnmpUserAuthKey_Type=OctetString
_SnmpUserAuthKey_Object=MibTableColumn
snmpUserAuthKey=_SnmpUserAuthKey_Object((1,3,6,1,4,1,8708,2,17,2,3,1,1,5),_SnmpUserAuthKey_Type())
snmpUserAuthKey.setMaxAccess(_E)
if mibBuilder.loadTexts:snmpUserAuthKey.setStatus(_B)
_SnmpUserPrivKey_Type=OctetString
_SnmpUserPrivKey_Object=MibTableColumn
snmpUserPrivKey=_SnmpUserPrivKey_Object((1,3,6,1,4,1,8708,2,17,2,3,1,1,6),_SnmpUserPrivKey_Type())
snmpUserPrivKey.setMaxAccess(_E)
if mibBuilder.loadTexts:snmpUserPrivKey.setStatus(_B)
class _SnmpUserChangePrivPassword_Type(CommandString):defaultValue=OctetString('')
_SnmpUserChangePrivPassword_Type.__name__=_b
_SnmpUserChangePrivPassword_Object=MibTableColumn
snmpUserChangePrivPassword=_SnmpUserChangePrivPassword_Object((1,3,6,1,4,1,8708,2,17,2,3,1,1,7),_SnmpUserChangePrivPassword_Type())
snmpUserChangePrivPassword.setMaxAccess(_E)
if mibBuilder.loadTexts:snmpUserChangePrivPassword.setStatus(_B)
class _SnmpUserPrivProtocol_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('none',1),('aes128',2)))
_SnmpUserPrivProtocol_Type.__name__=_G
_SnmpUserPrivProtocol_Object=MibTableColumn
snmpUserPrivProtocol=_SnmpUserPrivProtocol_Object((1,3,6,1,4,1,8708,2,17,2,3,1,1,8),_SnmpUserPrivProtocol_Type())
snmpUserPrivProtocol.setMaxAccess(_D)
if mibBuilder.loadTexts:snmpUserPrivProtocol.setStatus(_B)
snmpInformSinkGroup=ObjectGroup((1,3,6,1,4,1,8708,2,17,1,1,1))
snmpInformSinkGroup.setObjects(*((_A,_L),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y)))
if mibBuilder.loadTexts:snmpInformSinkGroup.setStatus(_C)
snmpGeneralGroup=ObjectGroup((1,3,6,1,4,1,8708,2,17,1,1,2))
snmpGeneralGroup.setObjects(*((_A,_H),(_A,_I)))
if mibBuilder.loadTexts:snmpGeneralGroup.setStatus(_C)
snmpGeneralGroupV2=ObjectGroup((1,3,6,1,4,1,8708,2,17,1,1,3))
snmpGeneralGroupV2.setObjects(*((_A,_H),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:snmpGeneralGroupV2.setStatus(_C)
snmpUserGroup=ObjectGroup((1,3,6,1,4,1,8708,2,17,1,1,4))
snmpUserGroup.setObjects(*((_A,_T),(_A,_c),(_A,_d),(_A,_e),(_A,_f)))
if mibBuilder.loadTexts:snmpUserGroup.setStatus(_C)
snmpGeneralGroupV3=ObjectGroup((1,3,6,1,4,1,8708,2,17,1,1,5))
snmpGeneralGroupV3.setObjects(*((_A,_H),(_A,_I),(_A,_J),(_A,_N)))
if mibBuilder.loadTexts:snmpGeneralGroupV3.setStatus(_C)
snmpInformSinkGroupV2=ObjectGroup((1,3,6,1,4,1,8708,2,17,1,1,6))
snmpInformSinkGroupV2.setObjects(*((_A,_L),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_g),(_A,_h),(_A,_i),(_A,_j)))
if mibBuilder.loadTexts:snmpInformSinkGroupV2.setStatus(_C)
snmpGeneralGroupV4=ObjectGroup((1,3,6,1,4,1,8708,2,17,1,1,7))
snmpGeneralGroupV4.setObjects(*((_A,_H),(_A,_I),(_A,_J),(_A,_N),(_A,_Z),(_A,_a)))
if mibBuilder.loadTexts:snmpGeneralGroupV4.setStatus(_C)
snmpInformSinkGroupV3=ObjectGroup((1,3,6,1,4,1,8708,2,17,1,1,8))
snmpInformSinkGroupV3.setObjects(*((_A,_L),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_r)))
if mibBuilder.loadTexts:snmpInformSinkGroupV3.setStatus(_B)
snmpGeneralGroupV5=ObjectGroup((1,3,6,1,4,1,8708,2,17,1,1,9))
snmpGeneralGroupV5.setObjects(*((_A,_H),(_A,_I),(_A,_J),(_A,_N),(_A,_Z),(_A,_a),(_A,_k)))
if mibBuilder.loadTexts:snmpGeneralGroupV5.setStatus(_C)
snmpGeneralGroupV6=ObjectGroup((1,3,6,1,4,1,8708,2,17,1,1,10))
snmpGeneralGroupV6.setObjects(*((_A,_H),(_A,_I),(_A,_J),(_A,_N),(_A,_Z),(_A,_a),(_A,_k),(_A,_s)))
if mibBuilder.loadTexts:snmpGeneralGroupV6.setStatus(_B)
snmpUserGroupV2=ObjectGroup((1,3,6,1,4,1,8708,2,17,1,1,11))
snmpUserGroupV2.setObjects(*((_A,_T),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_t),(_A,_u),(_A,_v)))
if mibBuilder.loadTexts:snmpUserGroupV2.setStatus(_B)
lumSnmpBasicComplV1=ModuleCompliance((1,3,6,1,4,1,8708,2,17,1,2,1))
lumSnmpBasicComplV1.setObjects(*((_A,_O),(_A,_w)))
if mibBuilder.loadTexts:lumSnmpBasicComplV1.setStatus(_C)
lumSnmpBasicComplV2=ModuleCompliance((1,3,6,1,4,1,8708,2,17,1,2,2))
lumSnmpBasicComplV2.setObjects(*((_A,_O),(_A,_l),(_A,_F)))
if mibBuilder.loadTexts:lumSnmpBasicComplV2.setStatus(_C)
lumSnmpBasicComplV3=ModuleCompliance((1,3,6,1,4,1,8708,2,17,1,2,3))
lumSnmpBasicComplV3.setObjects(*((_A,_O),(_A,_l),(_A,_F)))
if mibBuilder.loadTexts:lumSnmpBasicComplV3.setStatus(_C)
lumSnmpBasicComplV4=ModuleCompliance((1,3,6,1,4,1,8708,2,17,1,2,4))
lumSnmpBasicComplV4.setObjects(*((_A,_O),(_A,_m),(_A,_F)))
if mibBuilder.loadTexts:lumSnmpBasicComplV4.setStatus(_C)
lumSnmpBasicComplV5=ModuleCompliance((1,3,6,1,4,1,8708,2,17,1,2,5))
lumSnmpBasicComplV5.setObjects(*((_A,_n),(_A,_m),(_A,_F)))
if mibBuilder.loadTexts:lumSnmpBasicComplV5.setStatus(_C)
lumSnmpBasicComplV6=ModuleCompliance((1,3,6,1,4,1,8708,2,17,1,2,6))
lumSnmpBasicComplV6.setObjects(*((_A,_n),(_A,_o),(_A,_F)))
if mibBuilder.loadTexts:lumSnmpBasicComplV6.setStatus(_C)
lumSnmpBasicComplV7=ModuleCompliance((1,3,6,1,4,1,8708,2,17,1,2,7))
lumSnmpBasicComplV7.setObjects(*((_A,_P),(_A,_o),(_A,_F)))
if mibBuilder.loadTexts:lumSnmpBasicComplV7.setStatus(_C)
lumSnmpBasicComplV8=ModuleCompliance((1,3,6,1,4,1,8708,2,17,1,2,8))
lumSnmpBasicComplV8.setObjects(*((_A,_P),(_A,_p),(_A,_F)))
if mibBuilder.loadTexts:lumSnmpBasicComplV8.setStatus(_C)
lumSnmpBasicComplV9=ModuleCompliance((1,3,6,1,4,1,8708,2,17,1,2,9))
lumSnmpBasicComplV9.setObjects(*((_A,_P),(_A,_p),(_A,_F)))
if mibBuilder.loadTexts:lumSnmpBasicComplV9.setStatus(_C)
lumSnmpBasicComplV10=ModuleCompliance((1,3,6,1,4,1,8708,2,17,1,2,10))
lumSnmpBasicComplV10.setObjects(*((_A,_P),(_A,_x),(_A,_y)))
if mibBuilder.loadTexts:lumSnmpBasicComplV10.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'lumSnmpMIBModule':lumSnmpMIBModule,'lumSnmpConfs':lumSnmpConfs,'lumSnmpGroups':lumSnmpGroups,_O:snmpInformSinkGroup,_w:snmpGeneralGroup,_l:snmpGeneralGroupV2,_F:snmpUserGroup,_m:snmpGeneralGroupV3,_n:snmpInformSinkGroupV2,_o:snmpGeneralGroupV4,_P:snmpInformSinkGroupV3,_p:snmpGeneralGroupV5,_x:snmpGeneralGroupV6,_y:snmpUserGroupV2,'lumSnmpCompl':lumSnmpCompl,'lumSnmpBasicComplV1':lumSnmpBasicComplV1,'lumSnmpBasicComplV2':lumSnmpBasicComplV2,'lumSnmpBasicComplV3':lumSnmpBasicComplV3,'lumSnmpBasicComplV4':lumSnmpBasicComplV4,'lumSnmpBasicComplV5':lumSnmpBasicComplV5,'lumSnmpBasicComplV6':lumSnmpBasicComplV6,'lumSnmpBasicComplV7':lumSnmpBasicComplV7,'lumSnmpBasicComplV8':lumSnmpBasicComplV8,'lumSnmpBasicComplV9':lumSnmpBasicComplV9,'lumSnmpBasicComplV10':lumSnmpBasicComplV10,'lumSnmpMIBObjects':lumSnmpMIBObjects,'snmpInformSinkList':snmpInformSinkList,'snmpInformSinkTable':snmpInformSinkTable,'snmpInformSinkEntry':snmpInformSinkEntry,_L:snmpInformSinkIndex,_U:snmpInformSinkName,_V:snmpInformSinkAddr,_W:snmpInformSinkPort,_X:snmpInformSinkCommunity,_Y:snmpInformSinkRowStatus,_g:snmpInformSinkStorageType,_h:snmpInformSinkAlarmNotifications,_i:snmpInformSinkPerformanceNotifications,_j:snmpInformSinkOtherNotifications,_r:snmpInformSinkMib2Notifications,'snmpGeneral':snmpGeneral,_H:snmpGeneralLastChangeTime,_I:snmpGeneralConfigLastChangeTime,_J:snmpGeneralEngineID,_N:snmpGeneralCommunity,_Z:snmpGeneralInformSinkTableSize,_a:snmpGeneralUserTableSize,_k:snmpGeneralResetEngineIDCommand,_s:snmpGeneralSecurityPolicy,'snmpUserList':snmpUserList,'snmpUserTable':snmpUserTable,'snmpUserEntry':snmpUserEntry,_T:snmpUserIndex,_c:snmpUserName,_d:snmpUserChangePassword,_e:snmpUserEngineId,_f:snmpUserAuthKey,_t:snmpUserPrivKey,_u:snmpUserChangePrivPassword,_v:snmpUserPrivProtocol})