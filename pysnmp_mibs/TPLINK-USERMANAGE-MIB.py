_F='userInfoUserName'
_E='TPLINK-USERMANAGE-MIB'
_D='Integer32'
_C='OctetString'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_C,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols('IF-MIB','ifIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
tplinkMgmt,=mibBuilder.importSymbols('TPLINK-MIB','tplinkMgmt')
TPRowStatus,=mibBuilder.importSymbols('TPLINK-TC-MIB','TPRowStatus')
tplinkUserInfoMIB=ModuleIdentity((1,3,6,1,4,1,11863,6,7))
if mibBuilder.loadTexts:tplinkUserInfoMIB.setRevisions(('1920-09-07 09:00',))
_TplinkUserManageMIBObjects_ObjectIdentity=ObjectIdentity
tplinkUserManageMIBObjects=_TplinkUserManageMIBObjects_ObjectIdentity((1,3,6,1,4,1,11863,6,7,1))
_UserInfoUserTable_Object=MibTable
userInfoUserTable=_UserInfoUserTable_Object((1,3,6,1,4,1,11863,6,7,1,1))
if mibBuilder.loadTexts:userInfoUserTable.setStatus(_A)
_UserInfoUserEntry_Object=MibTableRow
userInfoUserEntry=_UserInfoUserEntry_Object((1,3,6,1,4,1,11863,6,7,1,1,1))
userInfoUserEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:userInfoUserEntry.setStatus(_A)
class _UserInfoUserName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_UserInfoUserName_Type.__name__=_C
_UserInfoUserName_Object=MibTableColumn
userInfoUserName=_UserInfoUserName_Object((1,3,6,1,4,1,11863,6,7,1,1,1,1),_UserInfoUserName_Type())
userInfoUserName.setMaxAccess('read-only')
if mibBuilder.loadTexts:userInfoUserName.setStatus(_A)
class _UserInfoUserType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('user',0),('power-user',1),('operator',2),('admin',3)))
_UserInfoUserType_Type.__name__=_D
_UserInfoUserType_Object=MibTableColumn
userInfoUserType=_UserInfoUserType_Object((1,3,6,1,4,1,11863,6,7,1,1,1,2),_UserInfoUserType_Type())
userInfoUserType.setMaxAccess(_B)
if mibBuilder.loadTexts:userInfoUserType.setStatus(_A)
class _UserInfoPasswordSecret_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('cipher',0),('simple',1)))
_UserInfoPasswordSecret_Type.__name__=_D
_UserInfoPasswordSecret_Object=MibTableColumn
userInfoPasswordSecret=_UserInfoPasswordSecret_Object((1,3,6,1,4,1,11863,6,7,1,1,1,3),_UserInfoPasswordSecret_Type())
userInfoPasswordSecret.setMaxAccess(_B)
if mibBuilder.loadTexts:userInfoPasswordSecret.setStatus(_A)
class _UserInfoOldPassword_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_UserInfoOldPassword_Type.__name__=_C
_UserInfoOldPassword_Object=MibTableColumn
userInfoOldPassword=_UserInfoOldPassword_Object((1,3,6,1,4,1,11863,6,7,1,1,1,4),_UserInfoOldPassword_Type())
userInfoOldPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:userInfoOldPassword.setStatus(_A)
class _UserInfoPassword_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_UserInfoPassword_Type.__name__=_C
_UserInfoPassword_Object=MibTableColumn
userInfoPassword=_UserInfoPassword_Object((1,3,6,1,4,1,11863,6,7,1,1,1,5),_UserInfoPassword_Type())
userInfoPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:userInfoPassword.setStatus(_A)
class _UserInfoConfirmedPassword_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_UserInfoConfirmedPassword_Type.__name__=_C
_UserInfoConfirmedPassword_Object=MibTableColumn
userInfoConfirmedPassword=_UserInfoConfirmedPassword_Object((1,3,6,1,4,1,11863,6,7,1,1,1,6),_UserInfoConfirmedPassword_Type())
userInfoConfirmedPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:userInfoConfirmedPassword.setStatus(_A)
_UserInfoUserStatus_Type=TPRowStatus
_UserInfoUserStatus_Object=MibTableColumn
userInfoUserStatus=_UserInfoUserStatus_Object((1,3,6,1,4,1,11863,6,7,1,1,1,7),_UserInfoUserStatus_Type())
userInfoUserStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:userInfoUserStatus.setStatus(_A)
_TplinkUserManageMIBNotifications_ObjectIdentity=ObjectIdentity
tplinkUserManageMIBNotifications=_TplinkUserManageMIBNotifications_ObjectIdentity((1,3,6,1,4,1,11863,6,7,2))
mibBuilder.exportSymbols(_E,**{'tplinkUserInfoMIB':tplinkUserInfoMIB,'tplinkUserManageMIBObjects':tplinkUserManageMIBObjects,'userInfoUserTable':userInfoUserTable,'userInfoUserEntry':userInfoUserEntry,_F:userInfoUserName,'userInfoUserType':userInfoUserType,'userInfoPasswordSecret':userInfoPasswordSecret,'userInfoOldPassword':userInfoOldPassword,'userInfoPassword':userInfoPassword,'userInfoConfirmedPassword':userInfoConfirmedPassword,'userInfoUserStatus':userInfoUserStatus,'tplinkUserManageMIBNotifications':tplinkUserManageMIBNotifications})