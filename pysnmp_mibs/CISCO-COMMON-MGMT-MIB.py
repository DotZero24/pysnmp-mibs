_h='ccmCacheTimeoutConfigGroup'
_g='ccmCommonUserCacheTimeout'
_f='ccmCommonUserRoleRowStatus'
_e='ccmCommonUserRoleStorageType'
_d='ccmCommonUserRowStatus'
_c='ccmCommonUserStorageType'
_b='ccmCommonUserCredType'
_a='ccmCommonUserSNMPPrivProtocol'
_Z='ccmCommonUserSNMPAuthProtocol'
_Y='ccmCommonUserSshKeyConfigured'
_X='ccmCommonUserSshKeyFilename'
_W='ccmCommonUserExpiryDate'
_V='ccmCommonUserPassword'
_U='ccmCommonUserLastChange'
_T='ccmCommonUsersGlobalEnforcePriv'
_S='ccmCommonUsers'
_R='ccmCommonMaxUsers'
_Q='ccmCommonUserRoleName'
_P='not-accessible'
_O='read-write'
_N='TruthValue'
_M='DisplayString'
_L='DateAndTime'
_K='Integer32'
_J='ccmConfigurationGroup'
_I='ccmCommonUserName'
_H='StorageType'
_G='AutonomousType'
_F='Unsigned32'
_E='SnmpAdminString'
_D='read-only'
_C='read-create'
_B='CISCO-COMMON-MGMT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_E)
usmNoAuthProtocol,usmNoPrivProtocol=mibBuilder.importSymbols('SNMP-USER-BASED-SM-MIB','usmNoAuthProtocol','usmNoPrivProtocol')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,dod,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_K,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'dod','iso')
AutonomousType,DateAndTime,DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_G,_L,_M,'PhysAddress','RowStatus',_H,'TextualConvention',_N)
ciscoCommonMgmtMIB=ModuleIdentity((1,3,6,1,4,1,9,9,443))
if mibBuilder.loadTexts:ciscoCommonMgmtMIB.setRevisions(('2008-06-13 00:00','2005-06-23 00:00'))
_CiscoCommonMgmtNotifs_ObjectIdentity=ObjectIdentity
ciscoCommonMgmtNotifs=_CiscoCommonMgmtNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,443,0))
_CiscoCommonMgmtMIBObjects_ObjectIdentity=ObjectIdentity
ciscoCommonMgmtMIBObjects=_CiscoCommonMgmtMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,443,1))
_CcmUserConfig_ObjectIdentity=ObjectIdentity
ccmUserConfig=_CcmUserConfig_ObjectIdentity((1,3,6,1,4,1,9,9,443,1,1))
class _CcmCommonMaxUsers_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CcmCommonMaxUsers_Type.__name__=_F
_CcmCommonMaxUsers_Object=MibScalar
ccmCommonMaxUsers=_CcmCommonMaxUsers_Object((1,3,6,1,4,1,9,9,443,1,1,1),_CcmCommonMaxUsers_Type())
ccmCommonMaxUsers.setMaxAccess(_D)
if mibBuilder.loadTexts:ccmCommonMaxUsers.setStatus(_A)
class _CcmCommonUsers_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CcmCommonUsers_Type.__name__=_F
_CcmCommonUsers_Object=MibScalar
ccmCommonUsers=_CcmCommonUsers_Object((1,3,6,1,4,1,9,9,443,1,1,2),_CcmCommonUsers_Type())
ccmCommonUsers.setMaxAccess(_D)
if mibBuilder.loadTexts:ccmCommonUsers.setStatus(_A)
class _CcmCommonUsersGlobalEnforcePriv_Type(TruthValue):defaultValue=2
_CcmCommonUsersGlobalEnforcePriv_Type.__name__=_N
_CcmCommonUsersGlobalEnforcePriv_Object=MibScalar
ccmCommonUsersGlobalEnforcePriv=_CcmCommonUsersGlobalEnforcePriv_Object((1,3,6,1,4,1,9,9,443,1,1,3),_CcmCommonUsersGlobalEnforcePriv_Type())
ccmCommonUsersGlobalEnforcePriv.setMaxAccess(_O)
if mibBuilder.loadTexts:ccmCommonUsersGlobalEnforcePriv.setStatus(_A)
_CcmCommonUserLastChange_Type=DateAndTime
_CcmCommonUserLastChange_Object=MibScalar
ccmCommonUserLastChange=_CcmCommonUserLastChange_Object((1,3,6,1,4,1,9,9,443,1,1,4),_CcmCommonUserLastChange_Type())
ccmCommonUserLastChange.setMaxAccess(_D)
if mibBuilder.loadTexts:ccmCommonUserLastChange.setStatus(_A)
_CcmCommonUserTable_Object=MibTable
ccmCommonUserTable=_CcmCommonUserTable_Object((1,3,6,1,4,1,9,9,443,1,1,5))
if mibBuilder.loadTexts:ccmCommonUserTable.setStatus(_A)
_CcmCommonUserEntry_Object=MibTableRow
ccmCommonUserEntry=_CcmCommonUserEntry_Object((1,3,6,1,4,1,9,9,443,1,1,5,1))
ccmCommonUserEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:ccmCommonUserEntry.setStatus(_A)
class _CcmCommonUserName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_CcmCommonUserName_Type.__name__=_E
_CcmCommonUserName_Object=MibTableColumn
ccmCommonUserName=_CcmCommonUserName_Object((1,3,6,1,4,1,9,9,443,1,1,5,1,1),_CcmCommonUserName_Type())
ccmCommonUserName.setMaxAccess(_P)
if mibBuilder.loadTexts:ccmCommonUserName.setStatus(_A)
class _CcmCommonUserPassword_Type(DisplayString):defaultHexValue=''
_CcmCommonUserPassword_Type.__name__=_M
_CcmCommonUserPassword_Object=MibTableColumn
ccmCommonUserPassword=_CcmCommonUserPassword_Object((1,3,6,1,4,1,9,9,443,1,1,5,1,2),_CcmCommonUserPassword_Type())
ccmCommonUserPassword.setMaxAccess(_C)
if mibBuilder.loadTexts:ccmCommonUserPassword.setStatus(_A)
class _CcmCommonUserExpiryDate_Type(DateAndTime):defaultHexValue='0000000000000000000000'
_CcmCommonUserExpiryDate_Type.__name__=_L
_CcmCommonUserExpiryDate_Object=MibTableColumn
ccmCommonUserExpiryDate=_CcmCommonUserExpiryDate_Object((1,3,6,1,4,1,9,9,443,1,1,5,1,3),_CcmCommonUserExpiryDate_Type())
ccmCommonUserExpiryDate.setMaxAccess(_C)
if mibBuilder.loadTexts:ccmCommonUserExpiryDate.setStatus(_A)
class _CcmCommonUserSshKeyFilename_Type(SnmpAdminString):defaultHexValue='';subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CcmCommonUserSshKeyFilename_Type.__name__=_E
_CcmCommonUserSshKeyFilename_Object=MibTableColumn
ccmCommonUserSshKeyFilename=_CcmCommonUserSshKeyFilename_Object((1,3,6,1,4,1,9,9,443,1,1,5,1,4),_CcmCommonUserSshKeyFilename_Type())
ccmCommonUserSshKeyFilename.setMaxAccess(_C)
if mibBuilder.loadTexts:ccmCommonUserSshKeyFilename.setStatus(_A)
_CcmCommonUserSshKeyConfigured_Type=TruthValue
_CcmCommonUserSshKeyConfigured_Object=MibTableColumn
ccmCommonUserSshKeyConfigured=_CcmCommonUserSshKeyConfigured_Object((1,3,6,1,4,1,9,9,443,1,1,5,1,5),_CcmCommonUserSshKeyConfigured_Type())
ccmCommonUserSshKeyConfigured.setMaxAccess(_D)
if mibBuilder.loadTexts:ccmCommonUserSshKeyConfigured.setStatus(_A)
class _CcmCommonUserSNMPAuthProtocol_Type(AutonomousType):defaultValue=1,3,6,1,6,3,10,1,1,1
_CcmCommonUserSNMPAuthProtocol_Type.__name__=_G
_CcmCommonUserSNMPAuthProtocol_Object=MibTableColumn
ccmCommonUserSNMPAuthProtocol=_CcmCommonUserSNMPAuthProtocol_Object((1,3,6,1,4,1,9,9,443,1,1,5,1,6),_CcmCommonUserSNMPAuthProtocol_Type())
ccmCommonUserSNMPAuthProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:ccmCommonUserSNMPAuthProtocol.setStatus(_A)
class _CcmCommonUserSNMPPrivProtocol_Type(AutonomousType):defaultValue=1,3,6,1,6,3,10,1,2,1
_CcmCommonUserSNMPPrivProtocol_Type.__name__=_G
_CcmCommonUserSNMPPrivProtocol_Object=MibTableColumn
ccmCommonUserSNMPPrivProtocol=_CcmCommonUserSNMPPrivProtocol_Object((1,3,6,1,4,1,9,9,443,1,1,5,1,7),_CcmCommonUserSNMPPrivProtocol_Type())
ccmCommonUserSNMPPrivProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:ccmCommonUserSNMPPrivProtocol.setStatus(_A)
class _CcmCommonUserCredType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('localCredentialStore',2),('remoteCredentialStore',3)))
_CcmCommonUserCredType_Type.__name__=_K
_CcmCommonUserCredType_Object=MibTableColumn
ccmCommonUserCredType=_CcmCommonUserCredType_Object((1,3,6,1,4,1,9,9,443,1,1,5,1,8),_CcmCommonUserCredType_Type())
ccmCommonUserCredType.setMaxAccess(_D)
if mibBuilder.loadTexts:ccmCommonUserCredType.setStatus(_A)
class _CcmCommonUserStorageType_Type(StorageType):defaultValue=3
_CcmCommonUserStorageType_Type.__name__=_H
_CcmCommonUserStorageType_Object=MibTableColumn
ccmCommonUserStorageType=_CcmCommonUserStorageType_Object((1,3,6,1,4,1,9,9,443,1,1,5,1,9),_CcmCommonUserStorageType_Type())
ccmCommonUserStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:ccmCommonUserStorageType.setStatus(_A)
_CcmCommonUserRowStatus_Type=RowStatus
_CcmCommonUserRowStatus_Object=MibTableColumn
ccmCommonUserRowStatus=_CcmCommonUserRowStatus_Object((1,3,6,1,4,1,9,9,443,1,1,5,1,10),_CcmCommonUserRowStatus_Type())
ccmCommonUserRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ccmCommonUserRowStatus.setStatus(_A)
_CcmCommonUserRoleTable_Object=MibTable
ccmCommonUserRoleTable=_CcmCommonUserRoleTable_Object((1,3,6,1,4,1,9,9,443,1,1,6))
if mibBuilder.loadTexts:ccmCommonUserRoleTable.setStatus(_A)
_CcmCommonUserRoleEntry_Object=MibTableRow
ccmCommonUserRoleEntry=_CcmCommonUserRoleEntry_Object((1,3,6,1,4,1,9,9,443,1,1,6,1))
ccmCommonUserRoleEntry.setIndexNames((0,_B,_I),(0,_B,_Q))
if mibBuilder.loadTexts:ccmCommonUserRoleEntry.setStatus(_A)
class _CcmCommonUserRoleName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_CcmCommonUserRoleName_Type.__name__=_E
_CcmCommonUserRoleName_Object=MibTableColumn
ccmCommonUserRoleName=_CcmCommonUserRoleName_Object((1,3,6,1,4,1,9,9,443,1,1,6,1,1),_CcmCommonUserRoleName_Type())
ccmCommonUserRoleName.setMaxAccess(_P)
if mibBuilder.loadTexts:ccmCommonUserRoleName.setStatus(_A)
class _CcmCommonUserRoleStorageType_Type(StorageType):defaultValue=3
_CcmCommonUserRoleStorageType_Type.__name__=_H
_CcmCommonUserRoleStorageType_Object=MibTableColumn
ccmCommonUserRoleStorageType=_CcmCommonUserRoleStorageType_Object((1,3,6,1,4,1,9,9,443,1,1,6,1,2),_CcmCommonUserRoleStorageType_Type())
ccmCommonUserRoleStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:ccmCommonUserRoleStorageType.setStatus(_A)
_CcmCommonUserRoleRowStatus_Type=RowStatus
_CcmCommonUserRoleRowStatus_Object=MibTableColumn
ccmCommonUserRoleRowStatus=_CcmCommonUserRoleRowStatus_Object((1,3,6,1,4,1,9,9,443,1,1,6,1,3),_CcmCommonUserRoleRowStatus_Type())
ccmCommonUserRoleRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ccmCommonUserRoleRowStatus.setStatus(_A)
class _CcmCommonUserCacheTimeout_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,86400))
_CcmCommonUserCacheTimeout_Type.__name__=_F
_CcmCommonUserCacheTimeout_Object=MibScalar
ccmCommonUserCacheTimeout=_CcmCommonUserCacheTimeout_Object((1,3,6,1,4,1,9,9,443,1,1,7),_CcmCommonUserCacheTimeout_Type())
ccmCommonUserCacheTimeout.setMaxAccess(_O)
if mibBuilder.loadTexts:ccmCommonUserCacheTimeout.setStatus(_A)
if mibBuilder.loadTexts:ccmCommonUserCacheTimeout.setUnits('seconds')
_CiscoCommonMgmtMIBConform_ObjectIdentity=ObjectIdentity
ciscoCommonMgmtMIBConform=_CiscoCommonMgmtMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,443,2))
_CiscoCommonMgmtMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoCommonMgmtMIBCompliances=_CiscoCommonMgmtMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,443,2,1))
_CiscoCommonMgmtMIBGroups_ObjectIdentity=ObjectIdentity
ciscoCommonMgmtMIBGroups=_CiscoCommonMgmtMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,443,2,2))
ccmConfigurationGroup=ObjectGroup((1,3,6,1,4,1,9,9,443,2,2,1))
ccmConfigurationGroup.setObjects(*((_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f)))
if mibBuilder.loadTexts:ccmConfigurationGroup.setStatus(_A)
ccmCacheTimeoutConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,443,2,2,2))
ccmCacheTimeoutConfigGroup.setObjects((_B,_g))
if mibBuilder.loadTexts:ccmCacheTimeoutConfigGroup.setStatus(_A)
ciscoCommonMgmtMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,443,2,1,1))
ciscoCommonMgmtMIBCompliance.setObjects((_B,_J))
if mibBuilder.loadTexts:ciscoCommonMgmtMIBCompliance.setStatus('obsolete')
ciscoCommonMgmtMIBCompliance1=ModuleCompliance((1,3,6,1,4,1,9,9,443,2,1,2))
ciscoCommonMgmtMIBCompliance1.setObjects(*((_B,_J),(_B,_h)))
if mibBuilder.loadTexts:ciscoCommonMgmtMIBCompliance1.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoCommonMgmtMIB':ciscoCommonMgmtMIB,'ciscoCommonMgmtNotifs':ciscoCommonMgmtNotifs,'ciscoCommonMgmtMIBObjects':ciscoCommonMgmtMIBObjects,'ccmUserConfig':ccmUserConfig,_R:ccmCommonMaxUsers,_S:ccmCommonUsers,_T:ccmCommonUsersGlobalEnforcePriv,_U:ccmCommonUserLastChange,'ccmCommonUserTable':ccmCommonUserTable,'ccmCommonUserEntry':ccmCommonUserEntry,_I:ccmCommonUserName,_V:ccmCommonUserPassword,_W:ccmCommonUserExpiryDate,_X:ccmCommonUserSshKeyFilename,_Y:ccmCommonUserSshKeyConfigured,_Z:ccmCommonUserSNMPAuthProtocol,_a:ccmCommonUserSNMPPrivProtocol,_b:ccmCommonUserCredType,_c:ccmCommonUserStorageType,_d:ccmCommonUserRowStatus,'ccmCommonUserRoleTable':ccmCommonUserRoleTable,'ccmCommonUserRoleEntry':ccmCommonUserRoleEntry,_Q:ccmCommonUserRoleName,_e:ccmCommonUserRoleStorageType,_f:ccmCommonUserRoleRowStatus,_g:ccmCommonUserCacheTimeout,'ciscoCommonMgmtMIBConform':ciscoCommonMgmtMIBConform,'ciscoCommonMgmtMIBCompliances':ciscoCommonMgmtMIBCompliances,'ciscoCommonMgmtMIBCompliance':ciscoCommonMgmtMIBCompliance,'ciscoCommonMgmtMIBCompliance1':ciscoCommonMgmtMIBCompliance1,'ciscoCommonMgmtMIBGroups':ciscoCommonMgmtMIBGroups,_J:ccmConfigurationGroup,_h:ccmCacheTimeoutConfigGroup})