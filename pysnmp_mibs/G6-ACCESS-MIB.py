_T='loginStatusIndex'
_S='unused'
_R='restrictionsIndex'
_Q='tacacsIndex'
_P='radiusIndex'
_O='patternIndex'
_N='viewIndex'
_M='groupIndex'
_L='readWrite'
_K='readOnly'
_J='noAccess'
_I='userIndex'
_H='enabled'
_G='disabled'
_F='not-accessible'
_E='G6-ACCESS-MIB'
_D='read-only'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
g6,=mibBuilder.importSymbols('MICROSENS-G6-MIB','g6')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
management=ModuleIdentity((1,3,6,1,4,1,3181,10,6,3))
if mibBuilder.loadTexts:management.setRevisions(('2018-02-12 16:19',))
_Access_ObjectIdentity=ObjectIdentity
access=_Access_ObjectIdentity((1,3,6,1,4,1,3181,10,6,3,76))
class _AccessAuthenticationMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*(('local',0),('localThenRadius',1),('radius',2),('localThenTacacs',3),('tacacs',4),('radiusThenLocal',5),('tacacsThenLocal',6)))
_AccessAuthenticationMode_Type.__name__=_C
_AccessAuthenticationMode_Object=MibScalar
accessAuthenticationMode=_AccessAuthenticationMode_Object((1,3,6,1,4,1,3181,10,6,3,76,1),_AccessAuthenticationMode_Type())
accessAuthenticationMode.setMaxAccess(_B)
if mibBuilder.loadTexts:accessAuthenticationMode.setStatus(_A)
_UserTable_Object=MibTable
userTable=_UserTable_Object((1,3,6,1,4,1,3181,10,6,3,76,2))
if mibBuilder.loadTexts:userTable.setStatus(_A)
_UserEntry_Object=MibTableRow
userEntry=_UserEntry_Object((1,3,6,1,4,1,3181,10,6,3,76,2,1))
userEntry.setIndexNames((0,_E,_I))
if mibBuilder.loadTexts:userEntry.setStatus(_A)
class _UserIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
_UserIndex_Type.__name__=_C
_UserIndex_Object=MibTableColumn
userIndex=_UserIndex_Object((1,3,6,1,4,1,3181,10,6,3,76,2,1,1),_UserIndex_Type())
userIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:userIndex.setStatus(_A)
_UserName_Type=DisplayString
_UserName_Object=MibTableColumn
userName=_UserName_Object((1,3,6,1,4,1,3181,10,6,3,76,2,1,2),_UserName_Type())
userName.setMaxAccess(_B)
if mibBuilder.loadTexts:userName.setStatus(_A)
_UserAssociatedGroups_Type=DisplayString
_UserAssociatedGroups_Object=MibTableColumn
userAssociatedGroups=_UserAssociatedGroups_Object((1,3,6,1,4,1,3181,10,6,3,76,2,1,3),_UserAssociatedGroups_Type())
userAssociatedGroups.setMaxAccess(_B)
if mibBuilder.loadTexts:userAssociatedGroups.setStatus(_A)
class _UserGeneralAccessRights_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_J,0),(_K,1),(_L,2)))
_UserGeneralAccessRights_Type.__name__=_C
_UserGeneralAccessRights_Object=MibTableColumn
userGeneralAccessRights=_UserGeneralAccessRights_Object((1,3,6,1,4,1,3181,10,6,3,76,2,1,4),_UserGeneralAccessRights_Type())
userGeneralAccessRights.setMaxAccess(_B)
if mibBuilder.loadTexts:userGeneralAccessRights.setStatus(_A)
class _UserEnableTelnetAccess_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_UserEnableTelnetAccess_Type.__name__=_C
_UserEnableTelnetAccess_Object=MibTableColumn
userEnableTelnetAccess=_UserEnableTelnetAccess_Object((1,3,6,1,4,1,3181,10,6,3,76,2,1,5),_UserEnableTelnetAccess_Type())
userEnableTelnetAccess.setMaxAccess(_B)
if mibBuilder.loadTexts:userEnableTelnetAccess.setStatus(_A)
class _UserEnableSshAccess_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_UserEnableSshAccess_Type.__name__=_C
_UserEnableSshAccess_Object=MibTableColumn
userEnableSshAccess=_UserEnableSshAccess_Object((1,3,6,1,4,1,3181,10,6,3,76,2,1,6),_UserEnableSshAccess_Type())
userEnableSshAccess.setMaxAccess(_B)
if mibBuilder.loadTexts:userEnableSshAccess.setStatus(_A)
class _UserEnableWebAccess_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_UserEnableWebAccess_Type.__name__=_C
_UserEnableWebAccess_Object=MibTableColumn
userEnableWebAccess=_UserEnableWebAccess_Object((1,3,6,1,4,1,3181,10,6,3,76,2,1,7),_UserEnableWebAccess_Type())
userEnableWebAccess.setMaxAccess(_B)
if mibBuilder.loadTexts:userEnableWebAccess.setStatus(_A)
class _UserEnableSnmpAccess_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_UserEnableSnmpAccess_Type.__name__=_C
_UserEnableSnmpAccess_Object=MibTableColumn
userEnableSnmpAccess=_UserEnableSnmpAccess_Object((1,3,6,1,4,1,3181,10,6,3,76,2,1,8),_UserEnableSnmpAccess_Type())
userEnableSnmpAccess.setMaxAccess(_B)
if mibBuilder.loadTexts:userEnableSnmpAccess.setStatus(_A)
class _UserEnableNmpAccess_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_UserEnableNmpAccess_Type.__name__=_C
_UserEnableNmpAccess_Object=MibTableColumn
userEnableNmpAccess=_UserEnableNmpAccess_Object((1,3,6,1,4,1,3181,10,6,3,76,2,1,9),_UserEnableNmpAccess_Type())
userEnableNmpAccess.setMaxAccess(_B)
if mibBuilder.loadTexts:userEnableNmpAccess.setStatus(_A)
class _UserEnableFtpAccess_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_UserEnableFtpAccess_Type.__name__=_C
_UserEnableFtpAccess_Object=MibTableColumn
userEnableFtpAccess=_UserEnableFtpAccess_Object((1,3,6,1,4,1,3181,10,6,3,76,2,1,10),_UserEnableFtpAccess_Type())
userEnableFtpAccess.setMaxAccess(_B)
if mibBuilder.loadTexts:userEnableFtpAccess.setStatus(_A)
_UserEnterPassword_Type=DisplayString
_UserEnterPassword_Object=MibTableColumn
userEnterPassword=_UserEnterPassword_Object((1,3,6,1,4,1,3181,10,6,3,76,2,1,11),_UserEnterPassword_Type())
userEnterPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:userEnterPassword.setStatus(_A)
_UserEncryptedAuthPassword_Type=DisplayString
_UserEncryptedAuthPassword_Object=MibTableColumn
userEncryptedAuthPassword=_UserEncryptedAuthPassword_Object((1,3,6,1,4,1,3181,10,6,3,76,2,1,12),_UserEncryptedAuthPassword_Type())
userEncryptedAuthPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:userEncryptedAuthPassword.setStatus(_A)
class _UserSnmpV3SecurityLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('noAuthNoPriv',0),('authNoPriv',1),('authPriv',2)))
_UserSnmpV3SecurityLevel_Type.__name__=_C
_UserSnmpV3SecurityLevel_Object=MibTableColumn
userSnmpV3SecurityLevel=_UserSnmpV3SecurityLevel_Object((1,3,6,1,4,1,3181,10,6,3,76,2,1,13),_UserSnmpV3SecurityLevel_Type())
userSnmpV3SecurityLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:userSnmpV3SecurityLevel.setStatus(_A)
class _UserSnmpV3AuthAlgorithm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('noAuthentication',0),('md5',1),('sha',2)))
_UserSnmpV3AuthAlgorithm_Type.__name__=_C
_UserSnmpV3AuthAlgorithm_Object=MibTableColumn
userSnmpV3AuthAlgorithm=_UserSnmpV3AuthAlgorithm_Object((1,3,6,1,4,1,3181,10,6,3,76,2,1,14),_UserSnmpV3AuthAlgorithm_Type())
userSnmpV3AuthAlgorithm.setMaxAccess(_B)
if mibBuilder.loadTexts:userSnmpV3AuthAlgorithm.setStatus(_A)
class _UserSnmpV3PrivacyAlgorithm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('noPrivacy',0),('des',1),('aes',2)))
_UserSnmpV3PrivacyAlgorithm_Type.__name__=_C
_UserSnmpV3PrivacyAlgorithm_Object=MibTableColumn
userSnmpV3PrivacyAlgorithm=_UserSnmpV3PrivacyAlgorithm_Object((1,3,6,1,4,1,3181,10,6,3,76,2,1,15),_UserSnmpV3PrivacyAlgorithm_Type())
userSnmpV3PrivacyAlgorithm.setMaxAccess(_B)
if mibBuilder.loadTexts:userSnmpV3PrivacyAlgorithm.setStatus(_A)
_UserEnterSnmpV3AuthPassword_Type=DisplayString
_UserEnterSnmpV3AuthPassword_Object=MibTableColumn
userEnterSnmpV3AuthPassword=_UserEnterSnmpV3AuthPassword_Object((1,3,6,1,4,1,3181,10,6,3,76,2,1,16),_UserEnterSnmpV3AuthPassword_Type())
userEnterSnmpV3AuthPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:userEnterSnmpV3AuthPassword.setStatus(_A)
_UserEncryptedSnmpAuthPassword_Type=DisplayString
_UserEncryptedSnmpAuthPassword_Object=MibTableColumn
userEncryptedSnmpAuthPassword=_UserEncryptedSnmpAuthPassword_Object((1,3,6,1,4,1,3181,10,6,3,76,2,1,17),_UserEncryptedSnmpAuthPassword_Type())
userEncryptedSnmpAuthPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:userEncryptedSnmpAuthPassword.setStatus(_A)
_UserEnterSnmpV3PrivacyPassword_Type=DisplayString
_UserEnterSnmpV3PrivacyPassword_Object=MibTableColumn
userEnterSnmpV3PrivacyPassword=_UserEnterSnmpV3PrivacyPassword_Object((1,3,6,1,4,1,3181,10,6,3,76,2,1,18),_UserEnterSnmpV3PrivacyPassword_Type())
userEnterSnmpV3PrivacyPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:userEnterSnmpV3PrivacyPassword.setStatus(_A)
_UserEncryptedSnmpPrivacyPassword_Type=DisplayString
_UserEncryptedSnmpPrivacyPassword_Object=MibTableColumn
userEncryptedSnmpPrivacyPassword=_UserEncryptedSnmpPrivacyPassword_Object((1,3,6,1,4,1,3181,10,6,3,76,2,1,19),_UserEncryptedSnmpPrivacyPassword_Type())
userEncryptedSnmpPrivacyPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:userEncryptedSnmpPrivacyPassword.setStatus(_A)
_GroupTable_Object=MibTable
groupTable=_GroupTable_Object((1,3,6,1,4,1,3181,10,6,3,76,3))
if mibBuilder.loadTexts:groupTable.setStatus(_A)
_GroupEntry_Object=MibTableRow
groupEntry=_GroupEntry_Object((1,3,6,1,4,1,3181,10,6,3,76,3,1))
groupEntry.setIndexNames((0,_E,_M))
if mibBuilder.loadTexts:groupEntry.setStatus(_A)
class _GroupIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_GroupIndex_Type.__name__=_C
_GroupIndex_Object=MibTableColumn
groupIndex=_GroupIndex_Object((1,3,6,1,4,1,3181,10,6,3,76,3,1,1),_GroupIndex_Type())
groupIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:groupIndex.setStatus(_A)
_GroupName_Type=DisplayString
_GroupName_Object=MibTableColumn
groupName=_GroupName_Object((1,3,6,1,4,1,3181,10,6,3,76,3,1,2),_GroupName_Type())
groupName.setMaxAccess(_B)
if mibBuilder.loadTexts:groupName.setStatus(_A)
_GroupAssociatedViews_Type=DisplayString
_GroupAssociatedViews_Object=MibTableColumn
groupAssociatedViews=_GroupAssociatedViews_Object((1,3,6,1,4,1,3181,10,6,3,76,3,1,3),_GroupAssociatedViews_Type())
groupAssociatedViews.setMaxAccess(_B)
if mibBuilder.loadTexts:groupAssociatedViews.setStatus(_A)
_ViewTable_Object=MibTable
viewTable=_ViewTable_Object((1,3,6,1,4,1,3181,10,6,3,76,4))
if mibBuilder.loadTexts:viewTable.setStatus(_A)
_ViewEntry_Object=MibTableRow
viewEntry=_ViewEntry_Object((1,3,6,1,4,1,3181,10,6,3,76,4,1))
viewEntry.setIndexNames((0,_E,_N))
if mibBuilder.loadTexts:viewEntry.setStatus(_A)
class _ViewIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_ViewIndex_Type.__name__=_C
_ViewIndex_Object=MibTableColumn
viewIndex=_ViewIndex_Object((1,3,6,1,4,1,3181,10,6,3,76,4,1,1),_ViewIndex_Type())
viewIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:viewIndex.setStatus(_A)
_ViewName_Type=DisplayString
_ViewName_Object=MibTableColumn
viewName=_ViewName_Object((1,3,6,1,4,1,3181,10,6,3,76,4,1,2),_ViewName_Type())
viewName.setMaxAccess(_B)
if mibBuilder.loadTexts:viewName.setStatus(_A)
_ViewAssociatedPattern_Type=DisplayString
_ViewAssociatedPattern_Object=MibTableColumn
viewAssociatedPattern=_ViewAssociatedPattern_Object((1,3,6,1,4,1,3181,10,6,3,76,4,1,3),_ViewAssociatedPattern_Type())
viewAssociatedPattern.setMaxAccess(_B)
if mibBuilder.loadTexts:viewAssociatedPattern.setStatus(_A)
_PatternTable_Object=MibTable
patternTable=_PatternTable_Object((1,3,6,1,4,1,3181,10,6,3,76,5))
if mibBuilder.loadTexts:patternTable.setStatus(_A)
_PatternEntry_Object=MibTableRow
patternEntry=_PatternEntry_Object((1,3,6,1,4,1,3181,10,6,3,76,5,1))
patternEntry.setIndexNames((0,_E,_O))
if mibBuilder.loadTexts:patternEntry.setStatus(_A)
class _PatternIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_PatternIndex_Type.__name__=_C
_PatternIndex_Object=MibTableColumn
patternIndex=_PatternIndex_Object((1,3,6,1,4,1,3181,10,6,3,76,5,1,1),_PatternIndex_Type())
patternIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:patternIndex.setStatus(_A)
_PatternName_Type=DisplayString
_PatternName_Object=MibTableColumn
patternName=_PatternName_Object((1,3,6,1,4,1,3181,10,6,3,76,5,1,2),_PatternName_Type())
patternName.setMaxAccess(_B)
if mibBuilder.loadTexts:patternName.setStatus(_A)
_PatternDotstring_Type=DisplayString
_PatternDotstring_Object=MibTableColumn
patternDotstring=_PatternDotstring_Object((1,3,6,1,4,1,3181,10,6,3,76,5,1,3),_PatternDotstring_Type())
patternDotstring.setMaxAccess(_B)
if mibBuilder.loadTexts:patternDotstring.setStatus(_A)
class _PatternAccessRights_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_J,0),(_K,1),(_L,2)))
_PatternAccessRights_Type.__name__=_C
_PatternAccessRights_Object=MibTableColumn
patternAccessRights=_PatternAccessRights_Object((1,3,6,1,4,1,3181,10,6,3,76,5,1,4),_PatternAccessRights_Type())
patternAccessRights.setMaxAccess(_B)
if mibBuilder.loadTexts:patternAccessRights.setStatus(_A)
_RadiusTable_Object=MibTable
radiusTable=_RadiusTable_Object((1,3,6,1,4,1,3181,10,6,3,76,6))
if mibBuilder.loadTexts:radiusTable.setStatus(_A)
_RadiusEntry_Object=MibTableRow
radiusEntry=_RadiusEntry_Object((1,3,6,1,4,1,3181,10,6,3,76,6,1))
radiusEntry.setIndexNames((0,_E,_P))
if mibBuilder.loadTexts:radiusEntry.setStatus(_A)
class _RadiusIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0))
_RadiusIndex_Type.__name__=_C
_RadiusIndex_Object=MibTableColumn
radiusIndex=_RadiusIndex_Object((1,3,6,1,4,1,3181,10,6,3,76,6,1,1),_RadiusIndex_Type())
radiusIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:radiusIndex.setStatus(_A)
_RadiusPrimaryAuthServerName_Type=DisplayString
_RadiusPrimaryAuthServerName_Object=MibTableColumn
radiusPrimaryAuthServerName=_RadiusPrimaryAuthServerName_Object((1,3,6,1,4,1,3181,10,6,3,76,6,1,2),_RadiusPrimaryAuthServerName_Type())
radiusPrimaryAuthServerName.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusPrimaryAuthServerName.setStatus(_A)
_RadiusFallbackAuthServerName_Type=DisplayString
_RadiusFallbackAuthServerName_Object=MibTableColumn
radiusFallbackAuthServerName=_RadiusFallbackAuthServerName_Object((1,3,6,1,4,1,3181,10,6,3,76,6,1,3),_RadiusFallbackAuthServerName_Type())
radiusFallbackAuthServerName.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusFallbackAuthServerName.setStatus(_A)
_TacacsTable_Object=MibTable
tacacsTable=_TacacsTable_Object((1,3,6,1,4,1,3181,10,6,3,76,7))
if mibBuilder.loadTexts:tacacsTable.setStatus(_A)
_TacacsEntry_Object=MibTableRow
tacacsEntry=_TacacsEntry_Object((1,3,6,1,4,1,3181,10,6,3,76,7,1))
tacacsEntry.setIndexNames((0,_E,_Q))
if mibBuilder.loadTexts:tacacsEntry.setStatus(_A)
class _TacacsIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0))
_TacacsIndex_Type.__name__=_C
_TacacsIndex_Object=MibTableColumn
tacacsIndex=_TacacsIndex_Object((1,3,6,1,4,1,3181,10,6,3,76,7,1,1),_TacacsIndex_Type())
tacacsIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:tacacsIndex.setStatus(_A)
_TacacsPrimaryAuthServerName_Type=DisplayString
_TacacsPrimaryAuthServerName_Object=MibTableColumn
tacacsPrimaryAuthServerName=_TacacsPrimaryAuthServerName_Object((1,3,6,1,4,1,3181,10,6,3,76,7,1,2),_TacacsPrimaryAuthServerName_Type())
tacacsPrimaryAuthServerName.setMaxAccess(_B)
if mibBuilder.loadTexts:tacacsPrimaryAuthServerName.setStatus(_A)
_TacacsFallbackAuthServerName_Type=DisplayString
_TacacsFallbackAuthServerName_Object=MibTableColumn
tacacsFallbackAuthServerName=_TacacsFallbackAuthServerName_Object((1,3,6,1,4,1,3181,10,6,3,76,7,1,3),_TacacsFallbackAuthServerName_Type())
tacacsFallbackAuthServerName.setMaxAccess(_B)
if mibBuilder.loadTexts:tacacsFallbackAuthServerName.setStatus(_A)
_TacacsPrivilegeLevel0User_Type=DisplayString
_TacacsPrivilegeLevel0User_Object=MibTableColumn
tacacsPrivilegeLevel0User=_TacacsPrivilegeLevel0User_Object((1,3,6,1,4,1,3181,10,6,3,76,7,1,4),_TacacsPrivilegeLevel0User_Type())
tacacsPrivilegeLevel0User.setMaxAccess(_B)
if mibBuilder.loadTexts:tacacsPrivilegeLevel0User.setStatus(_A)
_TacacsPrivilegeLevel1User_Type=DisplayString
_TacacsPrivilegeLevel1User_Object=MibTableColumn
tacacsPrivilegeLevel1User=_TacacsPrivilegeLevel1User_Object((1,3,6,1,4,1,3181,10,6,3,76,7,1,5),_TacacsPrivilegeLevel1User_Type())
tacacsPrivilegeLevel1User.setMaxAccess(_B)
if mibBuilder.loadTexts:tacacsPrivilegeLevel1User.setStatus(_A)
_TacacsPrivilegeLevel15User_Type=DisplayString
_TacacsPrivilegeLevel15User_Object=MibTableColumn
tacacsPrivilegeLevel15User=_TacacsPrivilegeLevel15User_Object((1,3,6,1,4,1,3181,10,6,3,76,7,1,6),_TacacsPrivilegeLevel15User_Type())
tacacsPrivilegeLevel15User.setMaxAccess(_B)
if mibBuilder.loadTexts:tacacsPrivilegeLevel15User.setStatus(_A)
_RestrictionsTable_Object=MibTable
restrictionsTable=_RestrictionsTable_Object((1,3,6,1,4,1,3181,10,6,3,76,8))
if mibBuilder.loadTexts:restrictionsTable.setStatus(_A)
_RestrictionsEntry_Object=MibTableRow
restrictionsEntry=_RestrictionsEntry_Object((1,3,6,1,4,1,3181,10,6,3,76,8,1))
restrictionsEntry.setIndexNames((0,_E,_R))
if mibBuilder.loadTexts:restrictionsEntry.setStatus(_A)
class _RestrictionsIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_RestrictionsIndex_Type.__name__=_C
_RestrictionsIndex_Object=MibTableColumn
restrictionsIndex=_RestrictionsIndex_Object((1,3,6,1,4,1,3181,10,6,3,76,8,1,1),_RestrictionsIndex_Type())
restrictionsIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:restrictionsIndex.setStatus(_A)
_RestrictionsName_Type=DisplayString
_RestrictionsName_Object=MibTableColumn
restrictionsName=_RestrictionsName_Object((1,3,6,1,4,1,3181,10,6,3,76,8,1,2),_RestrictionsName_Type())
restrictionsName.setMaxAccess(_B)
if mibBuilder.loadTexts:restrictionsName.setStatus(_A)
class _RestrictionsMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_S,0),('permit',1),('deny',2)))
_RestrictionsMode_Type.__name__=_C
_RestrictionsMode_Object=MibTableColumn
restrictionsMode=_RestrictionsMode_Object((1,3,6,1,4,1,3181,10,6,3,76,8,1,3),_RestrictionsMode_Type())
restrictionsMode.setMaxAccess(_B)
if mibBuilder.loadTexts:restrictionsMode.setStatus(_A)
_RestrictionsIpAddress_Type=DisplayString
_RestrictionsIpAddress_Object=MibTableColumn
restrictionsIpAddress=_RestrictionsIpAddress_Object((1,3,6,1,4,1,3181,10,6,3,76,8,1,4),_RestrictionsIpAddress_Type())
restrictionsIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:restrictionsIpAddress.setStatus(_A)
_AccessNumberOfLogins_Type=Unsigned32
_AccessNumberOfLogins_Object=MibScalar
accessNumberOfLogins=_AccessNumberOfLogins_Object((1,3,6,1,4,1,3181,10,6,3,76,100),_AccessNumberOfLogins_Type())
accessNumberOfLogins.setMaxAccess(_D)
if mibBuilder.loadTexts:accessNumberOfLogins.setStatus(_A)
_LoginStatusTable_Object=MibTable
loginStatusTable=_LoginStatusTable_Object((1,3,6,1,4,1,3181,10,6,3,76,101))
if mibBuilder.loadTexts:loginStatusTable.setStatus(_A)
_LoginStatusEntry_Object=MibTableRow
loginStatusEntry=_LoginStatusEntry_Object((1,3,6,1,4,1,3181,10,6,3,76,101,1))
loginStatusEntry.setIndexNames((0,_E,_T))
if mibBuilder.loadTexts:loginStatusEntry.setStatus(_A)
class _LoginStatusIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
_LoginStatusIndex_Type.__name__=_C
_LoginStatusIndex_Object=MibTableColumn
loginStatusIndex=_LoginStatusIndex_Object((1,3,6,1,4,1,3181,10,6,3,76,101,1,1),_LoginStatusIndex_Type())
loginStatusIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:loginStatusIndex.setStatus(_A)
class _LoginStatusState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_S,0),('loggedOff',1),('activeLogin',2)))
_LoginStatusState_Type.__name__=_C
_LoginStatusState_Object=MibTableColumn
loginStatusState=_LoginStatusState_Object((1,3,6,1,4,1,3181,10,6,3,76,101,1,2),_LoginStatusState_Type())
loginStatusState.setMaxAccess(_D)
if mibBuilder.loadTexts:loginStatusState.setStatus(_A)
_LoginStatusUserName_Type=DisplayString
_LoginStatusUserName_Object=MibTableColumn
loginStatusUserName=_LoginStatusUserName_Object((1,3,6,1,4,1,3181,10,6,3,76,101,1,3),_LoginStatusUserName_Type())
loginStatusUserName.setMaxAccess(_D)
if mibBuilder.loadTexts:loginStatusUserName.setStatus(_A)
_LoginStatusAuthName_Type=DisplayString
_LoginStatusAuthName_Object=MibTableColumn
loginStatusAuthName=_LoginStatusAuthName_Object((1,3,6,1,4,1,3181,10,6,3,76,101,1,4),_LoginStatusAuthName_Type())
loginStatusAuthName.setMaxAccess(_D)
if mibBuilder.loadTexts:loginStatusAuthName.setStatus(_A)
_LoginStatusLoginId_Type=Unsigned32
_LoginStatusLoginId_Object=MibTableColumn
loginStatusLoginId=_LoginStatusLoginId_Object((1,3,6,1,4,1,3181,10,6,3,76,101,1,5),_LoginStatusLoginId_Type())
loginStatusLoginId.setMaxAccess(_D)
if mibBuilder.loadTexts:loginStatusLoginId.setStatus(_A)
_LoginStatusLoginTimeStamp_Type=DisplayString
_LoginStatusLoginTimeStamp_Object=MibTableColumn
loginStatusLoginTimeStamp=_LoginStatusLoginTimeStamp_Object((1,3,6,1,4,1,3181,10,6,3,76,101,1,6),_LoginStatusLoginTimeStamp_Type())
loginStatusLoginTimeStamp.setMaxAccess(_D)
if mibBuilder.loadTexts:loginStatusLoginTimeStamp.setStatus(_A)
_LoginStatusLoginEpoch_Type=Unsigned32
_LoginStatusLoginEpoch_Object=MibTableColumn
loginStatusLoginEpoch=_LoginStatusLoginEpoch_Object((1,3,6,1,4,1,3181,10,6,3,76,101,1,7),_LoginStatusLoginEpoch_Type())
loginStatusLoginEpoch.setMaxAccess(_D)
if mibBuilder.loadTexts:loginStatusLoginEpoch.setStatus(_A)
_LoginStatusConnectTime_Type=Counter32
_LoginStatusConnectTime_Object=MibTableColumn
loginStatusConnectTime=_LoginStatusConnectTime_Object((1,3,6,1,4,1,3181,10,6,3,76,101,1,8),_LoginStatusConnectTime_Type())
loginStatusConnectTime.setMaxAccess(_D)
if mibBuilder.loadTexts:loginStatusConnectTime.setStatus(_A)
_LoginStatusService_Type=DisplayString
_LoginStatusService_Object=MibTableColumn
loginStatusService=_LoginStatusService_Object((1,3,6,1,4,1,3181,10,6,3,76,101,1,9),_LoginStatusService_Type())
loginStatusService.setMaxAccess(_D)
if mibBuilder.loadTexts:loginStatusService.setStatus(_A)
_LoginStatusRemoteHost_Type=DisplayString
_LoginStatusRemoteHost_Object=MibTableColumn
loginStatusRemoteHost=_LoginStatusRemoteHost_Object((1,3,6,1,4,1,3181,10,6,3,76,101,1,10),_LoginStatusRemoteHost_Type())
loginStatusRemoteHost.setMaxAccess(_D)
if mibBuilder.loadTexts:loginStatusRemoteHost.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'management':management,'access':access,'accessAuthenticationMode':accessAuthenticationMode,'userTable':userTable,'userEntry':userEntry,_I:userIndex,'userName':userName,'userAssociatedGroups':userAssociatedGroups,'userGeneralAccessRights':userGeneralAccessRights,'userEnableTelnetAccess':userEnableTelnetAccess,'userEnableSshAccess':userEnableSshAccess,'userEnableWebAccess':userEnableWebAccess,'userEnableSnmpAccess':userEnableSnmpAccess,'userEnableNmpAccess':userEnableNmpAccess,'userEnableFtpAccess':userEnableFtpAccess,'userEnterPassword':userEnterPassword,'userEncryptedAuthPassword':userEncryptedAuthPassword,'userSnmpV3SecurityLevel':userSnmpV3SecurityLevel,'userSnmpV3AuthAlgorithm':userSnmpV3AuthAlgorithm,'userSnmpV3PrivacyAlgorithm':userSnmpV3PrivacyAlgorithm,'userEnterSnmpV3AuthPassword':userEnterSnmpV3AuthPassword,'userEncryptedSnmpAuthPassword':userEncryptedSnmpAuthPassword,'userEnterSnmpV3PrivacyPassword':userEnterSnmpV3PrivacyPassword,'userEncryptedSnmpPrivacyPassword':userEncryptedSnmpPrivacyPassword,'groupTable':groupTable,'groupEntry':groupEntry,_M:groupIndex,'groupName':groupName,'groupAssociatedViews':groupAssociatedViews,'viewTable':viewTable,'viewEntry':viewEntry,_N:viewIndex,'viewName':viewName,'viewAssociatedPattern':viewAssociatedPattern,'patternTable':patternTable,'patternEntry':patternEntry,_O:patternIndex,'patternName':patternName,'patternDotstring':patternDotstring,'patternAccessRights':patternAccessRights,'radiusTable':radiusTable,'radiusEntry':radiusEntry,_P:radiusIndex,'radiusPrimaryAuthServerName':radiusPrimaryAuthServerName,'radiusFallbackAuthServerName':radiusFallbackAuthServerName,'tacacsTable':tacacsTable,'tacacsEntry':tacacsEntry,_Q:tacacsIndex,'tacacsPrimaryAuthServerName':tacacsPrimaryAuthServerName,'tacacsFallbackAuthServerName':tacacsFallbackAuthServerName,'tacacsPrivilegeLevel0User':tacacsPrivilegeLevel0User,'tacacsPrivilegeLevel1User':tacacsPrivilegeLevel1User,'tacacsPrivilegeLevel15User':tacacsPrivilegeLevel15User,'restrictionsTable':restrictionsTable,'restrictionsEntry':restrictionsEntry,_R:restrictionsIndex,'restrictionsName':restrictionsName,'restrictionsMode':restrictionsMode,'restrictionsIpAddress':restrictionsIpAddress,'accessNumberOfLogins':accessNumberOfLogins,'loginStatusTable':loginStatusTable,'loginStatusEntry':loginStatusEntry,_T:loginStatusIndex,'loginStatusState':loginStatusState,'loginStatusUserName':loginStatusUserName,'loginStatusAuthName':loginStatusAuthName,'loginStatusLoginId':loginStatusLoginId,'loginStatusLoginTimeStamp':loginStatusLoginTimeStamp,'loginStatusLoginEpoch':loginStatusLoginEpoch,'loginStatusConnectTime':loginStatusConnectTime,'loginStatusService':loginStatusService,'loginStatusRemoteHost':loginStatusRemoteHost})