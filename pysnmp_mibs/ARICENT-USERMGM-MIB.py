_K='Password123#'
_J='not-accessible'
_I='fsusrMgmtAuthString'
_H='fsusrMgmtUserName'
_G='Integer32'
_F='ARICENT-USERMGM-MIB'
_E='read-only'
_D='DisplayString'
_C='Unsigned32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_C,'enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','RowStatus','TextualConvention')
fsusrMgmt=ModuleIdentity((1,3,6,1,4,1,29601,2,70))
if mibBuilder.loadTexts:fsusrMgmt.setRevisions(('2012-09-05 00:00',))
_FsusrMgmtStats_ObjectIdentity=ObjectIdentity
fsusrMgmtStats=_FsusrMgmtStats_ObjectIdentity((1,3,6,1,4,1,29601,2,70,1))
_FsusrMgmtStatsNumOfUsers_Type=Unsigned32
_FsusrMgmtStatsNumOfUsers_Object=MibScalar
fsusrMgmtStatsNumOfUsers=_FsusrMgmtStatsNumOfUsers_Object((1,3,6,1,4,1,29601,2,70,1,1),_FsusrMgmtStatsNumOfUsers_Type())
fsusrMgmtStatsNumOfUsers.setMaxAccess(_E)
if mibBuilder.loadTexts:fsusrMgmtStatsNumOfUsers.setStatus(_A)
_FsusrMgmtStatsActiveUsers_Type=Unsigned32
_FsusrMgmtStatsActiveUsers_Object=MibScalar
fsusrMgmtStatsActiveUsers=_FsusrMgmtStatsActiveUsers_Object((1,3,6,1,4,1,29601,2,70,1,2),_FsusrMgmtStatsActiveUsers_Type())
fsusrMgmtStatsActiveUsers.setMaxAccess(_E)
if mibBuilder.loadTexts:fsusrMgmtStatsActiveUsers.setStatus(_A)
class _FsusrMgmtMinPasswordLen_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(8,20))
_FsusrMgmtMinPasswordLen_Type.__name__=_C
_FsusrMgmtMinPasswordLen_Object=MibScalar
fsusrMgmtMinPasswordLen=_FsusrMgmtMinPasswordLen_Object((1,3,6,1,4,1,29601,2,70,1,3),_FsusrMgmtMinPasswordLen_Type())
fsusrMgmtMinPasswordLen.setMaxAccess(_B)
if mibBuilder.loadTexts:fsusrMgmtMinPasswordLen.setStatus(_A)
class _FsusrMgmtPasswdValidationChars_Type(Unsigned32):defaultValue=15;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_FsusrMgmtPasswdValidationChars_Type.__name__=_C
_FsusrMgmtPasswdValidationChars_Object=MibScalar
fsusrMgmtPasswdValidationChars=_FsusrMgmtPasswdValidationChars_Object((1,3,6,1,4,1,29601,2,70,1,4),_FsusrMgmtPasswdValidationChars_Type())
fsusrMgmtPasswdValidationChars.setMaxAccess(_B)
if mibBuilder.loadTexts:fsusrMgmtPasswdValidationChars.setStatus(_A)
class _FsusrMgmtPasswdValidateNoOfLowerCase_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,20))
_FsusrMgmtPasswdValidateNoOfLowerCase_Type.__name__=_C
_FsusrMgmtPasswdValidateNoOfLowerCase_Object=MibScalar
fsusrMgmtPasswdValidateNoOfLowerCase=_FsusrMgmtPasswdValidateNoOfLowerCase_Object((1,3,6,1,4,1,29601,2,70,1,5),_FsusrMgmtPasswdValidateNoOfLowerCase_Type())
fsusrMgmtPasswdValidateNoOfLowerCase.setMaxAccess(_B)
if mibBuilder.loadTexts:fsusrMgmtPasswdValidateNoOfLowerCase.setStatus(_A)
class _FsusrMgmtPasswdValidateNoOfUpperCase_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,20))
_FsusrMgmtPasswdValidateNoOfUpperCase_Type.__name__=_C
_FsusrMgmtPasswdValidateNoOfUpperCase_Object=MibScalar
fsusrMgmtPasswdValidateNoOfUpperCase=_FsusrMgmtPasswdValidateNoOfUpperCase_Object((1,3,6,1,4,1,29601,2,70,1,6),_FsusrMgmtPasswdValidateNoOfUpperCase_Type())
fsusrMgmtPasswdValidateNoOfUpperCase.setMaxAccess(_B)
if mibBuilder.loadTexts:fsusrMgmtPasswdValidateNoOfUpperCase.setStatus(_A)
class _FsusrMgmtPasswdValidateNoOfNumericals_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,20))
_FsusrMgmtPasswdValidateNoOfNumericals_Type.__name__=_C
_FsusrMgmtPasswdValidateNoOfNumericals_Object=MibScalar
fsusrMgmtPasswdValidateNoOfNumericals=_FsusrMgmtPasswdValidateNoOfNumericals_Object((1,3,6,1,4,1,29601,2,70,1,7),_FsusrMgmtPasswdValidateNoOfNumericals_Type())
fsusrMgmtPasswdValidateNoOfNumericals.setMaxAccess(_B)
if mibBuilder.loadTexts:fsusrMgmtPasswdValidateNoOfNumericals.setStatus(_A)
class _FsusrMgmtPasswdValidateNoOfSplChars_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,20))
_FsusrMgmtPasswdValidateNoOfSplChars_Type.__name__=_C
_FsusrMgmtPasswdValidateNoOfSplChars_Object=MibScalar
fsusrMgmtPasswdValidateNoOfSplChars=_FsusrMgmtPasswdValidateNoOfSplChars_Object((1,3,6,1,4,1,29601,2,70,1,8),_FsusrMgmtPasswdValidateNoOfSplChars_Type())
fsusrMgmtPasswdValidateNoOfSplChars.setMaxAccess(_B)
if mibBuilder.loadTexts:fsusrMgmtPasswdValidateNoOfSplChars.setStatus(_A)
class _FsusrMgmtPasswdMaxLifeTime_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,366))
_FsusrMgmtPasswdMaxLifeTime_Type.__name__=_C
_FsusrMgmtPasswdMaxLifeTime_Object=MibScalar
fsusrMgmtPasswdMaxLifeTime=_FsusrMgmtPasswdMaxLifeTime_Object((1,3,6,1,4,1,29601,2,70,1,9),_FsusrMgmtPasswdMaxLifeTime_Type())
fsusrMgmtPasswdMaxLifeTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsusrMgmtPasswdMaxLifeTime.setStatus(_A)
_FsusrMgmtStatsEnableUsers_Type=Unsigned32
_FsusrMgmtStatsEnableUsers_Object=MibScalar
fsusrMgmtStatsEnableUsers=_FsusrMgmtStatsEnableUsers_Object((1,3,6,1,4,1,29601,2,70,1,10),_FsusrMgmtStatsEnableUsers_Type())
fsusrMgmtStatsEnableUsers.setMaxAccess(_E)
if mibBuilder.loadTexts:fsusrMgmtStatsEnableUsers.setStatus(_A)
_FsusrMgmtStatsDisableUsers_Type=Unsigned32
_FsusrMgmtStatsDisableUsers_Object=MibScalar
fsusrMgmtStatsDisableUsers=_FsusrMgmtStatsDisableUsers_Object((1,3,6,1,4,1,29601,2,70,1,11),_FsusrMgmtStatsDisableUsers_Type())
fsusrMgmtStatsDisableUsers.setMaxAccess(_E)
if mibBuilder.loadTexts:fsusrMgmtStatsDisableUsers.setStatus(_A)
_FsusrMgmtUserList_ObjectIdentity=ObjectIdentity
fsusrMgmtUserList=_FsusrMgmtUserList_ObjectIdentity((1,3,6,1,4,1,29601,2,70,2))
_FsusrMgmtTable_Object=MibTable
fsusrMgmtTable=_FsusrMgmtTable_Object((1,3,6,1,4,1,29601,2,70,2,1))
if mibBuilder.loadTexts:fsusrMgmtTable.setStatus(_A)
_FsusrMgmtEntry_Object=MibTableRow
fsusrMgmtEntry=_FsusrMgmtEntry_Object((1,3,6,1,4,1,29601,2,70,2,1,1))
fsusrMgmtEntry.setIndexNames((0,_F,_H),(0,_F,_I))
if mibBuilder.loadTexts:fsusrMgmtEntry.setStatus(_A)
class _FsusrMgmtUserName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,20))
_FsusrMgmtUserName_Type.__name__=_D
_FsusrMgmtUserName_Object=MibTableColumn
fsusrMgmtUserName=_FsusrMgmtUserName_Object((1,3,6,1,4,1,29601,2,70,2,1,1,1),_FsusrMgmtUserName_Type())
fsusrMgmtUserName.setMaxAccess(_J)
if mibBuilder.loadTexts:fsusrMgmtUserName.setStatus(_A)
class _FsusrMgmtAuthString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,42))
_FsusrMgmtAuthString_Type.__name__=_D
_FsusrMgmtAuthString_Object=MibTableColumn
fsusrMgmtAuthString=_FsusrMgmtAuthString_Object((1,3,6,1,4,1,29601,2,70,2,1,1,2),_FsusrMgmtAuthString_Type())
fsusrMgmtAuthString.setMaxAccess(_J)
if mibBuilder.loadTexts:fsusrMgmtAuthString.setStatus(_A)
class _FsusrMgmtUserPassword_Type(DisplayString):defaultValue=OctetString(_K);subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,32))
_FsusrMgmtUserPassword_Type.__name__=_D
_FsusrMgmtUserPassword_Object=MibTableColumn
fsusrMgmtUserPassword=_FsusrMgmtUserPassword_Object((1,3,6,1,4,1,29601,2,70,2,1,1,3),_FsusrMgmtUserPassword_Type())
fsusrMgmtUserPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:fsusrMgmtUserPassword.setStatus(_A)
class _FsusrMgmtUserPrivilege_Type(Unsigned32):defaultValue=1
_FsusrMgmtUserPrivilege_Type.__name__=_C
_FsusrMgmtUserPrivilege_Object=MibTableColumn
fsusrMgmtUserPrivilege=_FsusrMgmtUserPrivilege_Object((1,3,6,1,4,1,29601,2,70,2,1,1,4),_FsusrMgmtUserPrivilege_Type())
fsusrMgmtUserPrivilege.setMaxAccess(_B)
if mibBuilder.loadTexts:fsusrMgmtUserPrivilege.setStatus(_A)
_FsusrMgmtUserLoginCount_Type=Integer32
_FsusrMgmtUserLoginCount_Object=MibTableColumn
fsusrMgmtUserLoginCount=_FsusrMgmtUserLoginCount_Object((1,3,6,1,4,1,29601,2,70,2,1,1,5),_FsusrMgmtUserLoginCount_Type())
fsusrMgmtUserLoginCount.setMaxAccess(_E)
if mibBuilder.loadTexts:fsusrMgmtUserLoginCount.setStatus(_A)
class _FsusrMgmtUserStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_FsusrMgmtUserStatus_Type.__name__=_G
_FsusrMgmtUserStatus_Object=MibTableColumn
fsusrMgmtUserStatus=_FsusrMgmtUserStatus_Object((1,3,6,1,4,1,29601,2,70,2,1,1,6),_FsusrMgmtUserStatus_Type())
fsusrMgmtUserStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsusrMgmtUserStatus.setStatus(_A)
class _FsusrMgmtUserLockRelTime_Type(Unsigned32):defaultValue=0
_FsusrMgmtUserLockRelTime_Type.__name__=_C
_FsusrMgmtUserLockRelTime_Object=MibTableColumn
fsusrMgmtUserLockRelTime=_FsusrMgmtUserLockRelTime_Object((1,3,6,1,4,1,29601,2,70,2,1,1,7),_FsusrMgmtUserLockRelTime_Type())
fsusrMgmtUserLockRelTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsusrMgmtUserLockRelTime.setStatus(_A)
_FsusrMgmtUserRowStatus_Type=RowStatus
_FsusrMgmtUserRowStatus_Object=MibTableColumn
fsusrMgmtUserRowStatus=_FsusrMgmtUserRowStatus_Object((1,3,6,1,4,1,29601,2,70,2,1,1,8),_FsusrMgmtUserRowStatus_Type())
fsusrMgmtUserRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsusrMgmtUserRowStatus.setStatus(_A)
class _FsusrMgmtUserConfirmPwd_Type(DisplayString):defaultValue=OctetString(_K);subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,32))
_FsusrMgmtUserConfirmPwd_Type.__name__=_D
_FsusrMgmtUserConfirmPwd_Object=MibTableColumn
fsusrMgmtUserConfirmPwd=_FsusrMgmtUserConfirmPwd_Object((1,3,6,1,4,1,29601,2,70,2,1,1,9),_FsusrMgmtUserConfirmPwd_Type())
fsusrMgmtUserConfirmPwd.setMaxAccess(_B)
if mibBuilder.loadTexts:fsusrMgmtUserConfirmPwd.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'fsusrMgmt':fsusrMgmt,'fsusrMgmtStats':fsusrMgmtStats,'fsusrMgmtStatsNumOfUsers':fsusrMgmtStatsNumOfUsers,'fsusrMgmtStatsActiveUsers':fsusrMgmtStatsActiveUsers,'fsusrMgmtMinPasswordLen':fsusrMgmtMinPasswordLen,'fsusrMgmtPasswdValidationChars':fsusrMgmtPasswdValidationChars,'fsusrMgmtPasswdValidateNoOfLowerCase':fsusrMgmtPasswdValidateNoOfLowerCase,'fsusrMgmtPasswdValidateNoOfUpperCase':fsusrMgmtPasswdValidateNoOfUpperCase,'fsusrMgmtPasswdValidateNoOfNumericals':fsusrMgmtPasswdValidateNoOfNumericals,'fsusrMgmtPasswdValidateNoOfSplChars':fsusrMgmtPasswdValidateNoOfSplChars,'fsusrMgmtPasswdMaxLifeTime':fsusrMgmtPasswdMaxLifeTime,'fsusrMgmtStatsEnableUsers':fsusrMgmtStatsEnableUsers,'fsusrMgmtStatsDisableUsers':fsusrMgmtStatsDisableUsers,'fsusrMgmtUserList':fsusrMgmtUserList,'fsusrMgmtTable':fsusrMgmtTable,'fsusrMgmtEntry':fsusrMgmtEntry,_H:fsusrMgmtUserName,_I:fsusrMgmtAuthString,'fsusrMgmtUserPassword':fsusrMgmtUserPassword,'fsusrMgmtUserPrivilege':fsusrMgmtUserPrivilege,'fsusrMgmtUserLoginCount':fsusrMgmtUserLoginCount,'fsusrMgmtUserStatus':fsusrMgmtUserStatus,'fsusrMgmtUserLockRelTime':fsusrMgmtUserLockRelTime,'fsusrMgmtUserRowStatus':fsusrMgmtUserRowStatus,'fsusrMgmtUserConfirmPwd':fsusrMgmtUserConfirmPwd})