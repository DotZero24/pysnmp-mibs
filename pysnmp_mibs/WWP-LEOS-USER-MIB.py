_L='wwpLeosUserUid'
_K='wwpLeosUserWhoPid'
_J='wwpLeosUserAuthProviderPriority'
_I='none'
_H='not-accessible'
_G='WWP-LEOS-USER-MIB'
_F='read-create'
_E='read-only'
_D='DisplayString'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','RowStatus','TextualConvention','TruthValue')
wwpModulesLeos,=mibBuilder.importSymbols('WWP-SMI','wwpModulesLeos')
wwpLeosUserMIB=ModuleIdentity((1,3,6,1,4,1,6141,2,60,39))
if mibBuilder.loadTexts:wwpLeosUserMIB.setRevisions(('2012-07-11 00:00','2012-06-27 00:00','2011-07-06 00:00','2007-03-01 00:00'))
_WwpLeosUserMIBObjects_ObjectIdentity=ObjectIdentity
wwpLeosUserMIBObjects=_WwpLeosUserMIBObjects_ObjectIdentity((1,3,6,1,4,1,6141,2,60,39,1))
_WwpLeosUser_ObjectIdentity=ObjectIdentity
wwpLeosUser=_WwpLeosUser_ObjectIdentity((1,3,6,1,4,1,6141,2,60,39,1,1))
_WwpLeosUserAuthProviderTable_Object=MibTable
wwpLeosUserAuthProviderTable=_WwpLeosUserAuthProviderTable_Object((1,3,6,1,4,1,6141,2,60,39,1,1,1))
if mibBuilder.loadTexts:wwpLeosUserAuthProviderTable.setStatus(_A)
_WwpLeosUserAuthProviderEntry_Object=MibTableRow
wwpLeosUserAuthProviderEntry=_WwpLeosUserAuthProviderEntry_Object((1,3,6,1,4,1,6141,2,60,39,1,1,1,1))
wwpLeosUserAuthProviderEntry.setIndexNames((0,_G,_J))
if mibBuilder.loadTexts:wwpLeosUserAuthProviderEntry.setStatus(_A)
class _WwpLeosUserAuthProviderPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_WwpLeosUserAuthProviderPriority_Type.__name__=_C
_WwpLeosUserAuthProviderPriority_Object=MibTableColumn
wwpLeosUserAuthProviderPriority=_WwpLeosUserAuthProviderPriority_Object((1,3,6,1,4,1,6141,2,60,39,1,1,1,1,1),_WwpLeosUserAuthProviderPriority_Type())
wwpLeosUserAuthProviderPriority.setMaxAccess(_H)
if mibBuilder.loadTexts:wwpLeosUserAuthProviderPriority.setStatus(_A)
class _WwpLeosUserAuthProviderType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_I,1),('local',2),('radius',3),('tacacs',4)))
_WwpLeosUserAuthProviderType_Type.__name__=_C
_WwpLeosUserAuthProviderType_Object=MibTableColumn
wwpLeosUserAuthProviderType=_WwpLeosUserAuthProviderType_Object((1,3,6,1,4,1,6141,2,60,39,1,1,1,1,2),_WwpLeosUserAuthProviderType_Type())
wwpLeosUserAuthProviderType.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosUserAuthProviderType.setStatus(_A)
_WwpLeosUserAuthProviderCalled_Type=Unsigned32
_WwpLeosUserAuthProviderCalled_Object=MibTableColumn
wwpLeosUserAuthProviderCalled=_WwpLeosUserAuthProviderCalled_Object((1,3,6,1,4,1,6141,2,60,39,1,1,1,1,3),_WwpLeosUserAuthProviderCalled_Type())
wwpLeosUserAuthProviderCalled.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosUserAuthProviderCalled.setStatus(_A)
_WwpLeosUserAuthProviderSuccess_Type=Unsigned32
_WwpLeosUserAuthProviderSuccess_Object=MibTableColumn
wwpLeosUserAuthProviderSuccess=_WwpLeosUserAuthProviderSuccess_Object((1,3,6,1,4,1,6141,2,60,39,1,1,1,1,4),_WwpLeosUserAuthProviderSuccess_Type())
wwpLeosUserAuthProviderSuccess.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosUserAuthProviderSuccess.setStatus(_A)
_WwpLeosUserAuthProviderFailure_Type=Unsigned32
_WwpLeosUserAuthProviderFailure_Object=MibTableColumn
wwpLeosUserAuthProviderFailure=_WwpLeosUserAuthProviderFailure_Object((1,3,6,1,4,1,6141,2,60,39,1,1,1,1,5),_WwpLeosUserAuthProviderFailure_Type())
wwpLeosUserAuthProviderFailure.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosUserAuthProviderFailure.setStatus(_A)
_WwpLeosUserAuthProviderSkipped_Type=Unsigned32
_WwpLeosUserAuthProviderSkipped_Object=MibTableColumn
wwpLeosUserAuthProviderSkipped=_WwpLeosUserAuthProviderSkipped_Object((1,3,6,1,4,1,6141,2,60,39,1,1,1,1,6),_WwpLeosUserAuthProviderSkipped_Type())
wwpLeosUserAuthProviderSkipped.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosUserAuthProviderSkipped.setStatus(_A)
class _WwpLeosUserAuthProviderScope_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_I,0),('serial',1),('remote',2),('all',3)))
_WwpLeosUserAuthProviderScope_Type.__name__=_C
_WwpLeosUserAuthProviderScope_Object=MibTableColumn
wwpLeosUserAuthProviderScope=_WwpLeosUserAuthProviderScope_Object((1,3,6,1,4,1,6141,2,60,39,1,1,1,1,7),_WwpLeosUserAuthProviderScope_Type())
wwpLeosUserAuthProviderScope.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosUserAuthProviderScope.setStatus(_A)
_WwpLeosUserWhoTable_Object=MibTable
wwpLeosUserWhoTable=_WwpLeosUserWhoTable_Object((1,3,6,1,4,1,6141,2,60,39,1,1,2))
if mibBuilder.loadTexts:wwpLeosUserWhoTable.setStatus(_A)
_WwpLeosUserWhoEntry_Object=MibTableRow
wwpLeosUserWhoEntry=_WwpLeosUserWhoEntry_Object((1,3,6,1,4,1,6141,2,60,39,1,1,2,1))
wwpLeosUserWhoEntry.setIndexNames((0,_G,_K))
if mibBuilder.loadTexts:wwpLeosUserWhoEntry.setStatus(_A)
_WwpLeosUserWhoPid_Type=Unsigned32
_WwpLeosUserWhoPid_Object=MibTableColumn
wwpLeosUserWhoPid=_WwpLeosUserWhoPid_Object((1,3,6,1,4,1,6141,2,60,39,1,1,2,1,1),_WwpLeosUserWhoPid_Type())
wwpLeosUserWhoPid.setMaxAccess(_H)
if mibBuilder.loadTexts:wwpLeosUserWhoPid.setStatus(_A)
class _WwpLeosUserWhoUser_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_WwpLeosUserWhoUser_Type.__name__=_D
_WwpLeosUserWhoUser_Object=MibTableColumn
wwpLeosUserWhoUser=_WwpLeosUserWhoUser_Object((1,3,6,1,4,1,6141,2,60,39,1,1,2,1,2),_WwpLeosUserWhoUser_Type())
wwpLeosUserWhoUser.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosUserWhoUser.setStatus(_A)
class _WwpLeosUserWhoTerminal_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_WwpLeosUserWhoTerminal_Type.__name__=_D
_WwpLeosUserWhoTerminal_Object=MibTableColumn
wwpLeosUserWhoTerminal=_WwpLeosUserWhoTerminal_Object((1,3,6,1,4,1,6141,2,60,39,1,1,2,1,3),_WwpLeosUserWhoTerminal_Type())
wwpLeosUserWhoTerminal.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosUserWhoTerminal.setStatus(_A)
_WwpLeosUserWhoIdleTime_Type=Counter32
_WwpLeosUserWhoIdleTime_Object=MibTableColumn
wwpLeosUserWhoIdleTime=_WwpLeosUserWhoIdleTime_Object((1,3,6,1,4,1,6141,2,60,39,1,1,2,1,4),_WwpLeosUserWhoIdleTime_Type())
wwpLeosUserWhoIdleTime.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosUserWhoIdleTime.setStatus(_A)
_WwpLeosUserWhoStatus_Type=RowStatus
_WwpLeosUserWhoStatus_Object=MibTableColumn
wwpLeosUserWhoStatus=_WwpLeosUserWhoStatus_Object((1,3,6,1,4,1,6141,2,60,39,1,1,2,1,5),_WwpLeosUserWhoStatus_Type())
wwpLeosUserWhoStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosUserWhoStatus.setStatus(_A)
_WwpLeosUserTable_Object=MibTable
wwpLeosUserTable=_WwpLeosUserTable_Object((1,3,6,1,4,1,6141,2,60,39,1,1,3))
if mibBuilder.loadTexts:wwpLeosUserTable.setStatus(_A)
_WwpLeosUserEntry_Object=MibTableRow
wwpLeosUserEntry=_WwpLeosUserEntry_Object((1,3,6,1,4,1,6141,2,60,39,1,1,3,1))
wwpLeosUserEntry.setIndexNames((0,_G,_L))
if mibBuilder.loadTexts:wwpLeosUserEntry.setStatus(_A)
_WwpLeosUserUid_Type=Unsigned32
_WwpLeosUserUid_Object=MibTableColumn
wwpLeosUserUid=_WwpLeosUserUid_Object((1,3,6,1,4,1,6141,2,60,39,1,1,3,1,1),_WwpLeosUserUid_Type())
wwpLeosUserUid.setMaxAccess(_H)
if mibBuilder.loadTexts:wwpLeosUserUid.setStatus(_A)
class _WwpLeosUserName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_WwpLeosUserName_Type.__name__=_D
_WwpLeosUserName_Object=MibTableColumn
wwpLeosUserName=_WwpLeosUserName_Object((1,3,6,1,4,1,6141,2,60,39,1,1,3,1,2),_WwpLeosUserName_Type())
wwpLeosUserName.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosUserName.setStatus(_A)
class _WwpLeosUserPassword_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,34))
_WwpLeosUserPassword_Type.__name__=_D
_WwpLeosUserPassword_Object=MibTableColumn
wwpLeosUserPassword=_WwpLeosUserPassword_Object((1,3,6,1,4,1,6141,2,60,39,1,1,3,1,3),_WwpLeosUserPassword_Type())
wwpLeosUserPassword.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosUserPassword.setStatus(_A)
class _WwpLeosUserPrivLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_I,0),('limited',1),('admin',2),('super',3),('diag',4)))
_WwpLeosUserPrivLevel_Type.__name__=_C
_WwpLeosUserPrivLevel_Object=MibTableColumn
wwpLeosUserPrivLevel=_WwpLeosUserPrivLevel_Object((1,3,6,1,4,1,6141,2,60,39,1,1,3,1,4),_WwpLeosUserPrivLevel_Type())
wwpLeosUserPrivLevel.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosUserPrivLevel.setStatus(_A)
_WwpLeosUserIsDefault_Type=TruthValue
_WwpLeosUserIsDefault_Object=MibTableColumn
wwpLeosUserIsDefault=_WwpLeosUserIsDefault_Object((1,3,6,1,4,1,6141,2,60,39,1,1,3,1,5),_WwpLeosUserIsDefault_Type())
wwpLeosUserIsDefault.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosUserIsDefault.setStatus(_A)
_WwpLeosUserIsEncrypted_Type=TruthValue
_WwpLeosUserIsEncrypted_Object=MibTableColumn
wwpLeosUserIsEncrypted=_WwpLeosUserIsEncrypted_Object((1,3,6,1,4,1,6141,2,60,39,1,1,3,1,6),_WwpLeosUserIsEncrypted_Type())
wwpLeosUserIsEncrypted.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosUserIsEncrypted.setStatus(_A)
_WwpLeosUserIsModified_Type=TruthValue
_WwpLeosUserIsModified_Object=MibTableColumn
wwpLeosUserIsModified=_WwpLeosUserIsModified_Object((1,3,6,1,4,1,6141,2,60,39,1,1,3,1,7),_WwpLeosUserIsModified_Type())
wwpLeosUserIsModified.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosUserIsModified.setStatus(_A)
_WwpLeosUserStatus_Type=RowStatus
_WwpLeosUserStatus_Object=MibTableColumn
wwpLeosUserStatus=_WwpLeosUserStatus_Object((1,3,6,1,4,1,6141,2,60,39,1,1,3,1,8),_WwpLeosUserStatus_Type())
wwpLeosUserStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosUserStatus.setStatus(_A)
_WwpLeosUserMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
wwpLeosUserMIBNotificationPrefix=_WwpLeosUserMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,6141,2,60,39,2))
_WwpLeosUserMIBNotifications_ObjectIdentity=ObjectIdentity
wwpLeosUserMIBNotifications=_WwpLeosUserMIBNotifications_ObjectIdentity((1,3,6,1,4,1,6141,2,60,39,2,0))
_WwpLeosUserMIBConformance_ObjectIdentity=ObjectIdentity
wwpLeosUserMIBConformance=_WwpLeosUserMIBConformance_ObjectIdentity((1,3,6,1,4,1,6141,2,60,39,3))
_WwpLeosUserMIBCompliances_ObjectIdentity=ObjectIdentity
wwpLeosUserMIBCompliances=_WwpLeosUserMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6141,2,60,39,3,1))
_WwpLeosUserMIBGroups_ObjectIdentity=ObjectIdentity
wwpLeosUserMIBGroups=_WwpLeosUserMIBGroups_ObjectIdentity((1,3,6,1,4,1,6141,2,60,39,3,2))
mibBuilder.exportSymbols(_G,**{'wwpLeosUserMIB':wwpLeosUserMIB,'wwpLeosUserMIBObjects':wwpLeosUserMIBObjects,'wwpLeosUser':wwpLeosUser,'wwpLeosUserAuthProviderTable':wwpLeosUserAuthProviderTable,'wwpLeosUserAuthProviderEntry':wwpLeosUserAuthProviderEntry,_J:wwpLeosUserAuthProviderPriority,'wwpLeosUserAuthProviderType':wwpLeosUserAuthProviderType,'wwpLeosUserAuthProviderCalled':wwpLeosUserAuthProviderCalled,'wwpLeosUserAuthProviderSuccess':wwpLeosUserAuthProviderSuccess,'wwpLeosUserAuthProviderFailure':wwpLeosUserAuthProviderFailure,'wwpLeosUserAuthProviderSkipped':wwpLeosUserAuthProviderSkipped,'wwpLeosUserAuthProviderScope':wwpLeosUserAuthProviderScope,'wwpLeosUserWhoTable':wwpLeosUserWhoTable,'wwpLeosUserWhoEntry':wwpLeosUserWhoEntry,_K:wwpLeosUserWhoPid,'wwpLeosUserWhoUser':wwpLeosUserWhoUser,'wwpLeosUserWhoTerminal':wwpLeosUserWhoTerminal,'wwpLeosUserWhoIdleTime':wwpLeosUserWhoIdleTime,'wwpLeosUserWhoStatus':wwpLeosUserWhoStatus,'wwpLeosUserTable':wwpLeosUserTable,'wwpLeosUserEntry':wwpLeosUserEntry,_L:wwpLeosUserUid,'wwpLeosUserName':wwpLeosUserName,'wwpLeosUserPassword':wwpLeosUserPassword,'wwpLeosUserPrivLevel':wwpLeosUserPrivLevel,'wwpLeosUserIsDefault':wwpLeosUserIsDefault,'wwpLeosUserIsEncrypted':wwpLeosUserIsEncrypted,'wwpLeosUserIsModified':wwpLeosUserIsModified,'wwpLeosUserStatus':wwpLeosUserStatus,'wwpLeosUserMIBNotificationPrefix':wwpLeosUserMIBNotificationPrefix,'wwpLeosUserMIBNotifications':wwpLeosUserMIBNotifications,'wwpLeosUserMIBConformance':wwpLeosUserMIBConformance,'wwpLeosUserMIBCompliances':wwpLeosUserMIBCompliances,'wwpLeosUserMIBGroups':wwpLeosUserMIBGroups})