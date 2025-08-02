_I='userConfigIndex'
_H='userInfoIndex'
_G='userInfoType'
_F='Integer32'
_E='not-accessible'
_D='AT-USER-MIB'
_C='Unsigned32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
sysinfo,=mibBuilder.importSymbols('AT-SMI-MIB','sysinfo')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_C,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
user=ModuleIdentity((1,3,6,1,4,1,207,8,4,4,3,20))
if mibBuilder.loadTexts:user.setRevisions(('2008-10-16 12:00','2008-08-26 00:00'))
_UserInfoTable_Object=MibTable
userInfoTable=_UserInfoTable_Object((1,3,6,1,4,1,207,8,4,4,3,20,1))
if mibBuilder.loadTexts:userInfoTable.setStatus(_A)
_UserInfoEntry_Object=MibTableRow
userInfoEntry=_UserInfoEntry_Object((1,3,6,1,4,1,207,8,4,4,3,20,1,1))
userInfoEntry.setIndexNames((0,_D,_G),(0,_D,_H))
if mibBuilder.loadTexts:userInfoEntry.setStatus(_A)
class _UserInfoType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('console',1),('aux',2),('telnet',3),('script',4),('stack',5)))
_UserInfoType_Type.__name__=_F
_UserInfoType_Object=MibTableColumn
userInfoType=_UserInfoType_Object((1,3,6,1,4,1,207,8,4,4,3,20,1,1,1),_UserInfoType_Type())
userInfoType.setMaxAccess(_E)
if mibBuilder.loadTexts:userInfoType.setStatus(_A)
class _UserInfoIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_UserInfoIndex_Type.__name__=_C
_UserInfoIndex_Object=MibTableColumn
userInfoIndex=_UserInfoIndex_Object((1,3,6,1,4,1,207,8,4,4,3,20,1,1,2),_UserInfoIndex_Type())
userInfoIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:userInfoIndex.setStatus(_A)
_UserInfoUserName_Type=DisplayString
_UserInfoUserName_Object=MibTableColumn
userInfoUserName=_UserInfoUserName_Object((1,3,6,1,4,1,207,8,4,4,3,20,1,1,3),_UserInfoUserName_Type())
userInfoUserName.setMaxAccess(_B)
if mibBuilder.loadTexts:userInfoUserName.setStatus(_A)
class _UserInfoPrivilegeLevel_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_UserInfoPrivilegeLevel_Type.__name__=_C
_UserInfoPrivilegeLevel_Object=MibTableColumn
userInfoPrivilegeLevel=_UserInfoPrivilegeLevel_Object((1,3,6,1,4,1,207,8,4,4,3,20,1,1,4),_UserInfoPrivilegeLevel_Type())
userInfoPrivilegeLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:userInfoPrivilegeLevel.setStatus(_A)
_UserInfoIdleTime_Type=DisplayString
_UserInfoIdleTime_Object=MibTableColumn
userInfoIdleTime=_UserInfoIdleTime_Object((1,3,6,1,4,1,207,8,4,4,3,20,1,1,5),_UserInfoIdleTime_Type())
userInfoIdleTime.setMaxAccess(_B)
if mibBuilder.loadTexts:userInfoIdleTime.setStatus(_A)
_UserInfoLocation_Type=DisplayString
_UserInfoLocation_Object=MibTableColumn
userInfoLocation=_UserInfoLocation_Object((1,3,6,1,4,1,207,8,4,4,3,20,1,1,6),_UserInfoLocation_Type())
userInfoLocation.setMaxAccess(_B)
if mibBuilder.loadTexts:userInfoLocation.setStatus(_A)
_UserConfigTable_Object=MibTable
userConfigTable=_UserConfigTable_Object((1,3,6,1,4,1,207,8,4,4,3,20,2))
if mibBuilder.loadTexts:userConfigTable.setStatus(_A)
_UserConfigEntry_Object=MibTableRow
userConfigEntry=_UserConfigEntry_Object((1,3,6,1,4,1,207,8,4,4,3,20,2,1))
userConfigEntry.setIndexNames((0,_D,_I))
if mibBuilder.loadTexts:userConfigEntry.setStatus(_A)
_UserConfigIndex_Type=Unsigned32
_UserConfigIndex_Object=MibTableColumn
userConfigIndex=_UserConfigIndex_Object((1,3,6,1,4,1,207,8,4,4,3,20,2,1,1),_UserConfigIndex_Type())
userConfigIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:userConfigIndex.setStatus(_A)
_UserConfigUsername_Type=DisplayString
_UserConfigUsername_Object=MibTableColumn
userConfigUsername=_UserConfigUsername_Object((1,3,6,1,4,1,207,8,4,4,3,20,2,1,2),_UserConfigUsername_Type())
userConfigUsername.setMaxAccess(_B)
if mibBuilder.loadTexts:userConfigUsername.setStatus(_A)
class _UserConfigPrivilegeLevel_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_UserConfigPrivilegeLevel_Type.__name__=_C
_UserConfigPrivilegeLevel_Object=MibTableColumn
userConfigPrivilegeLevel=_UserConfigPrivilegeLevel_Object((1,3,6,1,4,1,207,8,4,4,3,20,2,1,3),_UserConfigPrivilegeLevel_Type())
userConfigPrivilegeLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:userConfigPrivilegeLevel.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'user':user,'userInfoTable':userInfoTable,'userInfoEntry':userInfoEntry,_G:userInfoType,_H:userInfoIndex,'userInfoUserName':userInfoUserName,'userInfoPrivilegeLevel':userInfoPrivilegeLevel,'userInfoIdleTime':userInfoIdleTime,'userInfoLocation':userInfoLocation,'userConfigTable':userConfigTable,'userConfigEntry':userConfigEntry,_I:userConfigIndex,'userConfigUsername':userConfigUsername,'userConfigPrivilegeLevel':userConfigPrivilegeLevel})