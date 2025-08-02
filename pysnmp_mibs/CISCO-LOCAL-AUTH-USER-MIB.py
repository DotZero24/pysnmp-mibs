_r='clauMIBNotificationGroup2'
_q='clauUserInfoGroup'
_p='clauNotifControlGroup'
_o='clauMIBNotificationGroup1'
_n='clauUserLoggedOut1'
_m='clauUserLoggedIn1'
_l='clauUserDeleted1'
_k='clauUserAdded1'
_j='clauUserLoggedOut'
_i='clauUserLoggedIn'
_h='clauUserDeleted'
_g='clauUserAdded'
_f='clauUserConfigRowStatus'
_e='clauUserConfigStorageType'
_d='clauUserConfigDescription'
_c='clauUserConfigPassword'
_b='clauUserConfigLifetime'
_a='clauUserConfigCreationTime'
_Z='clauUserConfigType'
_Y='clauUserCreationTime'
_X='clauUserConfigName'
_W='seconds'
_V='guestUser'
_U='networkUser'
_T='managementUser'
_S='lobbyUser'
_R='defaultUser'
_Q='not-accessible'
_P='clauUserIndex'
_O='TruthValue'
_N='Unsigned32'
_M='OctetString'
_L='clauMIBNotificationGroup'
_K='clauMIBMainObjectGroup'
_J='clauNotifEnable'
_I='Integer32'
_H='clauUserLifetime'
_G='read-create'
_F='clauUserName'
_E='read-only'
_D='clauUserType'
_C='deprecated'
_B='current'
_A='CISCO-LOCAL-AUTH-USER-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_M,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_I,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_N,'iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','RowStatus','StorageType','TextualConvention',_O)
ciscoLocalAuthUserMIB=ModuleIdentity((1,3,6,1,4,1,9,9,798))
if mibBuilder.loadTexts:ciscoLocalAuthUserMIB.setRevisions(('2013-11-08 00:00','2013-05-09 00:00','2012-07-13 00:00'))
_CiscoLocalAuthUserMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoLocalAuthUserMIBNotifs=_CiscoLocalAuthUserMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,798,0))
_CiscoLocalAuthUserMIBObjects_ObjectIdentity=ObjectIdentity
ciscoLocalAuthUserMIBObjects=_CiscoLocalAuthUserMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,798,1))
class _ClauNotifEnable_Type(TruthValue):defaultValue=2
_ClauNotifEnable_Type.__name__=_O
_ClauNotifEnable_Object=MibScalar
clauNotifEnable=_ClauNotifEnable_Object((1,3,6,1,4,1,9,9,798,1,1),_ClauNotifEnable_Type())
clauNotifEnable.setMaxAccess('read-write')
if mibBuilder.loadTexts:clauNotifEnable.setStatus(_B)
_ClauUserTable_Object=MibTable
clauUserTable=_ClauUserTable_Object((1,3,6,1,4,1,9,9,798,1,2))
if mibBuilder.loadTexts:clauUserTable.setStatus(_C)
_ClauUserEntry_Object=MibTableRow
clauUserEntry=_ClauUserEntry_Object((1,3,6,1,4,1,9,9,798,1,2,1))
clauUserEntry.setIndexNames((0,_A,_P))
if mibBuilder.loadTexts:clauUserEntry.setStatus(_C)
class _ClauUserIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_ClauUserIndex_Type.__name__=_N
_ClauUserIndex_Object=MibTableColumn
clauUserIndex=_ClauUserIndex_Object((1,3,6,1,4,1,9,9,798,1,2,1,1),_ClauUserIndex_Type())
clauUserIndex.setMaxAccess(_Q)
if mibBuilder.loadTexts:clauUserIndex.setStatus(_C)
_ClauUserName_Type=SnmpAdminString
_ClauUserName_Object=MibTableColumn
clauUserName=_ClauUserName_Object((1,3,6,1,4,1,9,9,798,1,2,1,2),_ClauUserName_Type())
clauUserName.setMaxAccess(_E)
if mibBuilder.loadTexts:clauUserName.setStatus(_C)
class _ClauUserType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_R,1),(_S,2),(_T,3),(_U,4),(_V,5)))
_ClauUserType_Type.__name__=_I
_ClauUserType_Object=MibTableColumn
clauUserType=_ClauUserType_Object((1,3,6,1,4,1,9,9,798,1,2,1,3),_ClauUserType_Type())
clauUserType.setMaxAccess(_E)
if mibBuilder.loadTexts:clauUserType.setStatus(_C)
_ClauUserCreationTime_Type=DateAndTime
_ClauUserCreationTime_Object=MibTableColumn
clauUserCreationTime=_ClauUserCreationTime_Object((1,3,6,1,4,1,9,9,798,1,2,1,4),_ClauUserCreationTime_Type())
clauUserCreationTime.setMaxAccess(_E)
if mibBuilder.loadTexts:clauUserCreationTime.setStatus(_C)
_ClauUserLifetime_Type=Unsigned32
_ClauUserLifetime_Object=MibTableColumn
clauUserLifetime=_ClauUserLifetime_Object((1,3,6,1,4,1,9,9,798,1,2,1,5),_ClauUserLifetime_Type())
clauUserLifetime.setMaxAccess(_E)
if mibBuilder.loadTexts:clauUserLifetime.setStatus(_C)
if mibBuilder.loadTexts:clauUserLifetime.setUnits(_W)
_ClauUserConfigTable_Object=MibTable
clauUserConfigTable=_ClauUserConfigTable_Object((1,3,6,1,4,1,9,9,798,1,3))
if mibBuilder.loadTexts:clauUserConfigTable.setStatus(_B)
_ClauUserConfigEntry_Object=MibTableRow
clauUserConfigEntry=_ClauUserConfigEntry_Object((1,3,6,1,4,1,9,9,798,1,3,1))
clauUserConfigEntry.setIndexNames((0,_A,_X))
if mibBuilder.loadTexts:clauUserConfigEntry.setStatus(_B)
class _ClauUserConfigName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_ClauUserConfigName_Type.__name__=_M
_ClauUserConfigName_Object=MibTableColumn
clauUserConfigName=_ClauUserConfigName_Object((1,3,6,1,4,1,9,9,798,1,3,1,1),_ClauUserConfigName_Type())
clauUserConfigName.setMaxAccess(_Q)
if mibBuilder.loadTexts:clauUserConfigName.setStatus(_B)
class _ClauUserConfigType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_R,1),(_S,2),(_T,3),(_U,4),(_V,5)))
_ClauUserConfigType_Type.__name__=_I
_ClauUserConfigType_Object=MibTableColumn
clauUserConfigType=_ClauUserConfigType_Object((1,3,6,1,4,1,9,9,798,1,3,1,2),_ClauUserConfigType_Type())
clauUserConfigType.setMaxAccess(_E)
if mibBuilder.loadTexts:clauUserConfigType.setStatus(_B)
_ClauUserConfigCreationTime_Type=DateAndTime
_ClauUserConfigCreationTime_Object=MibTableColumn
clauUserConfigCreationTime=_ClauUserConfigCreationTime_Object((1,3,6,1,4,1,9,9,798,1,3,1,3),_ClauUserConfigCreationTime_Type())
clauUserConfigCreationTime.setMaxAccess(_E)
if mibBuilder.loadTexts:clauUserConfigCreationTime.setStatus(_B)
_ClauUserConfigLifetime_Type=Unsigned32
_ClauUserConfigLifetime_Object=MibTableColumn
clauUserConfigLifetime=_ClauUserConfigLifetime_Object((1,3,6,1,4,1,9,9,798,1,3,1,4),_ClauUserConfigLifetime_Type())
clauUserConfigLifetime.setMaxAccess(_G)
if mibBuilder.loadTexts:clauUserConfigLifetime.setStatus(_B)
if mibBuilder.loadTexts:clauUserConfigLifetime.setUnits(_W)
_ClauUserConfigPassword_Type=SnmpAdminString
_ClauUserConfigPassword_Object=MibTableColumn
clauUserConfigPassword=_ClauUserConfigPassword_Object((1,3,6,1,4,1,9,9,798,1,3,1,5),_ClauUserConfigPassword_Type())
clauUserConfigPassword.setMaxAccess(_G)
if mibBuilder.loadTexts:clauUserConfigPassword.setStatus(_B)
_ClauUserConfigDescription_Type=SnmpAdminString
_ClauUserConfigDescription_Object=MibTableColumn
clauUserConfigDescription=_ClauUserConfigDescription_Object((1,3,6,1,4,1,9,9,798,1,3,1,6),_ClauUserConfigDescription_Type())
clauUserConfigDescription.setMaxAccess(_G)
if mibBuilder.loadTexts:clauUserConfigDescription.setStatus(_B)
_ClauUserConfigStorageType_Type=StorageType
_ClauUserConfigStorageType_Object=MibTableColumn
clauUserConfigStorageType=_ClauUserConfigStorageType_Object((1,3,6,1,4,1,9,9,798,1,3,1,7),_ClauUserConfigStorageType_Type())
clauUserConfigStorageType.setMaxAccess(_G)
if mibBuilder.loadTexts:clauUserConfigStorageType.setStatus(_B)
_ClauUserConfigRowStatus_Type=RowStatus
_ClauUserConfigRowStatus_Object=MibTableColumn
clauUserConfigRowStatus=_ClauUserConfigRowStatus_Object((1,3,6,1,4,1,9,9,798,1,3,1,8),_ClauUserConfigRowStatus_Type())
clauUserConfigRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:clauUserConfigRowStatus.setStatus(_B)
_CiscoLocalAuthUserMIBConform_ObjectIdentity=ObjectIdentity
ciscoLocalAuthUserMIBConform=_CiscoLocalAuthUserMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,798,2))
_ClauMIBCompliances_ObjectIdentity=ObjectIdentity
clauMIBCompliances=_ClauMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,798,2,1))
_ClauMIBGroups_ObjectIdentity=ObjectIdentity
clauMIBGroups=_ClauMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,798,2,2))
clauMIBMainObjectGroup=ObjectGroup((1,3,6,1,4,1,9,9,798,2,2,1))
clauMIBMainObjectGroup.setObjects(*((_A,_J),(_A,_D),(_A,_Y),(_A,_H),(_A,_F)))
if mibBuilder.loadTexts:clauMIBMainObjectGroup.setStatus(_C)
clauNotifControlGroup=ObjectGroup((1,3,6,1,4,1,9,9,798,2,2,4))
clauNotifControlGroup.setObjects((_A,_J))
if mibBuilder.loadTexts:clauNotifControlGroup.setStatus(_B)
clauUserInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,798,2,2,5))
clauUserInfoGroup.setObjects(*((_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f)))
if mibBuilder.loadTexts:clauUserInfoGroup.setStatus(_B)
clauUserAdded=NotificationType((1,3,6,1,4,1,9,9,798,0,1))
clauUserAdded.setObjects(*((_A,_F),(_A,_D),(_A,_H)))
if mibBuilder.loadTexts:clauUserAdded.setStatus(_C)
clauUserDeleted=NotificationType((1,3,6,1,4,1,9,9,798,0,2))
clauUserDeleted.setObjects(*((_A,_F),(_A,_D)))
if mibBuilder.loadTexts:clauUserDeleted.setStatus(_C)
clauUserLoggedIn=NotificationType((1,3,6,1,4,1,9,9,798,0,3))
clauUserLoggedIn.setObjects(*((_A,_F),(_A,_D)))
if mibBuilder.loadTexts:clauUserLoggedIn.setStatus(_C)
clauUserLoggedOut=NotificationType((1,3,6,1,4,1,9,9,798,0,4))
clauUserLoggedOut.setObjects(*((_A,_F),(_A,_D)))
if mibBuilder.loadTexts:clauUserLoggedOut.setStatus(_C)
clauUserAdded1=NotificationType((1,3,6,1,4,1,9,9,798,0,5))
clauUserAdded1.setObjects(*((_A,_D),(_A,_H)))
if mibBuilder.loadTexts:clauUserAdded1.setStatus(_B)
clauUserDeleted1=NotificationType((1,3,6,1,4,1,9,9,798,0,6))
clauUserDeleted1.setObjects((_A,_D))
if mibBuilder.loadTexts:clauUserDeleted1.setStatus(_B)
clauUserLoggedIn1=NotificationType((1,3,6,1,4,1,9,9,798,0,7))
clauUserLoggedIn1.setObjects((_A,_D))
if mibBuilder.loadTexts:clauUserLoggedIn1.setStatus(_B)
clauUserLoggedOut1=NotificationType((1,3,6,1,4,1,9,9,798,0,8))
clauUserLoggedOut1.setObjects((_A,_D))
if mibBuilder.loadTexts:clauUserLoggedOut1.setStatus(_B)
clauMIBNotificationGroup=NotificationGroup((1,3,6,1,4,1,9,9,798,2,2,2))
clauMIBNotificationGroup.setObjects(*((_A,_g),(_A,_h)))
if mibBuilder.loadTexts:clauMIBNotificationGroup.setStatus(_C)
clauMIBNotificationGroup1=NotificationGroup((1,3,6,1,4,1,9,9,798,2,2,3))
clauMIBNotificationGroup1.setObjects(*((_A,_i),(_A,_j)))
if mibBuilder.loadTexts:clauMIBNotificationGroup1.setStatus(_C)
clauMIBNotificationGroup2=NotificationGroup((1,3,6,1,4,1,9,9,798,2,2,6))
clauMIBNotificationGroup2.setObjects(*((_A,_k),(_A,_l),(_A,_m),(_A,_n)))
if mibBuilder.loadTexts:clauMIBNotificationGroup2.setStatus(_B)
clauMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,798,2,1,1))
clauMIBCompliance.setObjects(*((_A,_K),(_A,_L)))
if mibBuilder.loadTexts:clauMIBCompliance.setStatus(_C)
clauMIBCompliance1=ModuleCompliance((1,3,6,1,4,1,9,9,798,2,1,2))
clauMIBCompliance1.setObjects(*((_A,_K),(_A,_L),(_A,_o)))
if mibBuilder.loadTexts:clauMIBCompliance1.setStatus(_C)
clauMIBCompliance2=ModuleCompliance((1,3,6,1,4,1,9,9,798,2,1,3))
clauMIBCompliance2.setObjects(*((_A,_p),(_A,_q),(_A,_r)))
if mibBuilder.loadTexts:clauMIBCompliance2.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ciscoLocalAuthUserMIB':ciscoLocalAuthUserMIB,'ciscoLocalAuthUserMIBNotifs':ciscoLocalAuthUserMIBNotifs,_g:clauUserAdded,_h:clauUserDeleted,_i:clauUserLoggedIn,_j:clauUserLoggedOut,_k:clauUserAdded1,_l:clauUserDeleted1,_m:clauUserLoggedIn1,_n:clauUserLoggedOut1,'ciscoLocalAuthUserMIBObjects':ciscoLocalAuthUserMIBObjects,_J:clauNotifEnable,'clauUserTable':clauUserTable,'clauUserEntry':clauUserEntry,_P:clauUserIndex,_F:clauUserName,_D:clauUserType,_Y:clauUserCreationTime,_H:clauUserLifetime,'clauUserConfigTable':clauUserConfigTable,'clauUserConfigEntry':clauUserConfigEntry,_X:clauUserConfigName,_Z:clauUserConfigType,_a:clauUserConfigCreationTime,_b:clauUserConfigLifetime,_c:clauUserConfigPassword,_d:clauUserConfigDescription,_e:clauUserConfigStorageType,_f:clauUserConfigRowStatus,'ciscoLocalAuthUserMIBConform':ciscoLocalAuthUserMIBConform,'clauMIBCompliances':clauMIBCompliances,'clauMIBCompliance':clauMIBCompliance,'clauMIBCompliance1':clauMIBCompliance1,'clauMIBCompliance2':clauMIBCompliance2,'clauMIBGroups':clauMIBGroups,_K:clauMIBMainObjectGroup,_L:clauMIBNotificationGroup,_o:clauMIBNotificationGroup1,_p:clauNotifControlGroup,_q:clauUserInfoGroup,_r:clauMIBNotificationGroup2})