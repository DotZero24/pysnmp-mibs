_I='nsSetAuthCfgIdx'
_H='NETSCREEN-SET-AUTH-MIB'
_G='yes'
_F='no'
_E='DisplayString'
_D='mandatory'
_C='Integer32'
_B='current'
_A='read-only'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
netscreenSetting,netscreenSettingMibModule=mibBuilder.importSymbols('NETSCREEN-SMI','netscreenSetting','netscreenSettingMibModule')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','TextualConvention')
netscreenSetAuthMibModule=ModuleIdentity((1,3,6,1,4,1,3224,7,0,2))
if mibBuilder.loadTexts:netscreenSetAuthMibModule.setRevisions(('2004-05-03 00:00','2004-11-10 20:22','2004-03-03 00:00','2003-11-10 00:00','2002-04-27 00:00','2001-05-27 00:00'))
_NsSetAuth_ObjectIdentity=ObjectIdentity
nsSetAuth=_NsSetAuth_ObjectIdentity((1,3,6,1,4,1,3224,7,2))
_NsSetAuthCfgTable_Object=MibTable
nsSetAuthCfgTable=_NsSetAuthCfgTable_Object((1,3,6,1,4,1,3224,7,2,1))
if mibBuilder.loadTexts:nsSetAuthCfgTable.setStatus(_B)
_NsSetAuthCfgEntry_Object=MibTableRow
nsSetAuthCfgEntry=_NsSetAuthCfgEntry_Object((1,3,6,1,4,1,3224,7,2,1,1))
nsSetAuthCfgEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:nsSetAuthCfgEntry.setStatus(_B)
class _NsSetAuthCfgIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_NsSetAuthCfgIdx_Type.__name__=_C
_NsSetAuthCfgIdx_Object=MibTableColumn
nsSetAuthCfgIdx=_NsSetAuthCfgIdx_Object((1,3,6,1,4,1,3224,7,2,1,1,1),_NsSetAuthCfgIdx_Type())
nsSetAuthCfgIdx.setMaxAccess(_A)
if mibBuilder.loadTexts:nsSetAuthCfgIdx.setStatus(_B)
_NsSetAuthCfgVsys_Type=Integer32
_NsSetAuthCfgVsys_Object=MibTableColumn
nsSetAuthCfgVsys=_NsSetAuthCfgVsys_Object((1,3,6,1,4,1,3224,7,2,1,1,2),_NsSetAuthCfgVsys_Type())
nsSetAuthCfgVsys.setMaxAccess(_A)
if mibBuilder.loadTexts:nsSetAuthCfgVsys.setStatus(_B)
class _NsSetAuthCfgName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NsSetAuthCfgName_Type.__name__=_E
_NsSetAuthCfgName_Object=MibTableColumn
nsSetAuthCfgName=_NsSetAuthCfgName_Object((1,3,6,1,4,1,3224,7,2,1,1,3),_NsSetAuthCfgName_Type())
nsSetAuthCfgName.setMaxAccess(_A)
if mibBuilder.loadTexts:nsSetAuthCfgName.setStatus(_B)
class _NsSetAuthCfgPrimary_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NsSetAuthCfgPrimary_Type.__name__=_E
_NsSetAuthCfgPrimary_Object=MibTableColumn
nsSetAuthCfgPrimary=_NsSetAuthCfgPrimary_Object((1,3,6,1,4,1,3224,7,2,1,1,4),_NsSetAuthCfgPrimary_Type())
nsSetAuthCfgPrimary.setMaxAccess(_A)
if mibBuilder.loadTexts:nsSetAuthCfgPrimary.setStatus(_B)
class _NsSetAuthCfgBackup1_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NsSetAuthCfgBackup1_Type.__name__=_E
_NsSetAuthCfgBackup1_Object=MibTableColumn
nsSetAuthCfgBackup1=_NsSetAuthCfgBackup1_Object((1,3,6,1,4,1,3224,7,2,1,1,5),_NsSetAuthCfgBackup1_Type())
nsSetAuthCfgBackup1.setMaxAccess(_A)
if mibBuilder.loadTexts:nsSetAuthCfgBackup1.setStatus(_B)
class _NsSetAuthCfgBackup2_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NsSetAuthCfgBackup2_Type.__name__=_E
_NsSetAuthCfgBackup2_Object=MibTableColumn
nsSetAuthCfgBackup2=_NsSetAuthCfgBackup2_Object((1,3,6,1,4,1,3224,7,2,1,1,6),_NsSetAuthCfgBackup2_Type())
nsSetAuthCfgBackup2.setMaxAccess(_A)
if mibBuilder.loadTexts:nsSetAuthCfgBackup2.setStatus(_B)
_NsSetAuthCfgConnIdleTimeout_Type=Integer32
_NsSetAuthCfgConnIdleTimeout_Object=MibTableColumn
nsSetAuthCfgConnIdleTimeout=_NsSetAuthCfgConnIdleTimeout_Object((1,3,6,1,4,1,3224,7,2,1,1,7),_NsSetAuthCfgConnIdleTimeout_Type())
nsSetAuthCfgConnIdleTimeout.setMaxAccess(_A)
if mibBuilder.loadTexts:nsSetAuthCfgConnIdleTimeout.setStatus(_B)
class _NsSetAuthCfgAuthAccount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_NsSetAuthCfgAuthAccount_Type.__name__=_C
_NsSetAuthCfgAuthAccount_Object=MibTableColumn
nsSetAuthCfgAuthAccount=_NsSetAuthCfgAuthAccount_Object((1,3,6,1,4,1,3224,7,2,1,1,8),_NsSetAuthCfgAuthAccount_Type())
nsSetAuthCfgAuthAccount.setMaxAccess(_A)
if mibBuilder.loadTexts:nsSetAuthCfgAuthAccount.setStatus(_B)
class _NsSetAuthCfgIkeAccount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_NsSetAuthCfgIkeAccount_Type.__name__=_C
_NsSetAuthCfgIkeAccount_Object=MibTableColumn
nsSetAuthCfgIkeAccount=_NsSetAuthCfgIkeAccount_Object((1,3,6,1,4,1,3224,7,2,1,1,9),_NsSetAuthCfgIkeAccount_Type())
nsSetAuthCfgIkeAccount.setMaxAccess(_A)
if mibBuilder.loadTexts:nsSetAuthCfgIkeAccount.setStatus(_B)
class _NsSetAuthCfgL2tpAccount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_NsSetAuthCfgL2tpAccount_Type.__name__=_C
_NsSetAuthCfgL2tpAccount_Object=MibTableColumn
nsSetAuthCfgL2tpAccount=_NsSetAuthCfgL2tpAccount_Object((1,3,6,1,4,1,3224,7,2,1,1,10),_NsSetAuthCfgL2tpAccount_Type())
nsSetAuthCfgL2tpAccount.setMaxAccess(_A)
if mibBuilder.loadTexts:nsSetAuthCfgL2tpAccount.setStatus(_B)
class _NsSetAuthCfgAdminAccount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_NsSetAuthCfgAdminAccount_Type.__name__=_C
_NsSetAuthCfgAdminAccount_Object=MibTableColumn
nsSetAuthCfgAdminAccount=_NsSetAuthCfgAdminAccount_Object((1,3,6,1,4,1,3224,7,2,1,1,11),_NsSetAuthCfgAdminAccount_Type())
nsSetAuthCfgAdminAccount.setMaxAccess(_A)
if mibBuilder.loadTexts:nsSetAuthCfgAdminAccount.setStatus(_B)
class _NsSetAuthCfgXauthAccount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_NsSetAuthCfgXauthAccount_Type.__name__=_C
_NsSetAuthCfgXauthAccount_Object=MibTableColumn
nsSetAuthCfgXauthAccount=_NsSetAuthCfgXauthAccount_Object((1,3,6,1,4,1,3224,7,2,1,1,12),_NsSetAuthCfgXauthAccount_Type())
nsSetAuthCfgXauthAccount.setMaxAccess(_A)
if mibBuilder.loadTexts:nsSetAuthCfgXauthAccount.setStatus(_B)
class _NsSetAuthCfgMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('build-in-user-db',0),('radius-server',1),('secureId-server',2),('ldap-server',3)))
_NsSetAuthCfgMethod_Type.__name__=_C
_NsSetAuthCfgMethod_Object=MibTableColumn
nsSetAuthCfgMethod=_NsSetAuthCfgMethod_Object((1,3,6,1,4,1,3224,7,2,1,1,13),_NsSetAuthCfgMethod_Type())
nsSetAuthCfgMethod.setMaxAccess(_A)
if mibBuilder.loadTexts:nsSetAuthCfgMethod.setStatus(_B)
_NsSetAuthCfgPort_Type=Integer32
_NsSetAuthCfgPort_Object=MibTableColumn
nsSetAuthCfgPort=_NsSetAuthCfgPort_Object((1,3,6,1,4,1,3224,7,2,1,1,14),_NsSetAuthCfgPort_Type())
nsSetAuthCfgPort.setMaxAccess(_A)
if mibBuilder.loadTexts:nsSetAuthCfgPort.setStatus(_B)
_NsSetAuthCfgSecCliRetry_Type=Integer32
_NsSetAuthCfgSecCliRetry_Object=MibTableColumn
nsSetAuthCfgSecCliRetry=_NsSetAuthCfgSecCliRetry_Object((1,3,6,1,4,1,3224,7,2,1,1,15),_NsSetAuthCfgSecCliRetry_Type())
nsSetAuthCfgSecCliRetry.setMaxAccess(_A)
if mibBuilder.loadTexts:nsSetAuthCfgSecCliRetry.setStatus(_B)
_NsSetAuthCfgSecCliTimeout_Type=Integer32
_NsSetAuthCfgSecCliTimeout_Object=MibTableColumn
nsSetAuthCfgSecCliTimeout=_NsSetAuthCfgSecCliTimeout_Object((1,3,6,1,4,1,3224,7,2,1,1,16),_NsSetAuthCfgSecCliTimeout_Type())
nsSetAuthCfgSecCliTimeout.setMaxAccess(_A)
if mibBuilder.loadTexts:nsSetAuthCfgSecCliTimeout.setStatus(_B)
class _NsSetAuthCfgSecEncType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('sdi',0),('des',1)))
_NsSetAuthCfgSecEncType_Type.__name__=_C
_NsSetAuthCfgSecEncType_Object=MibTableColumn
nsSetAuthCfgSecEncType=_NsSetAuthCfgSecEncType_Object((1,3,6,1,4,1,3224,7,2,1,1,17),_NsSetAuthCfgSecEncType_Type())
nsSetAuthCfgSecEncType.setMaxAccess(_A)
if mibBuilder.loadTexts:nsSetAuthCfgSecEncType.setStatus(_B)
class _NsSetAuthCfgSecUseDuress_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_NsSetAuthCfgSecUseDuress_Type.__name__=_C
_NsSetAuthCfgSecUseDuress_Object=MibTableColumn
nsSetAuthCfgSecUseDuress=_NsSetAuthCfgSecUseDuress_Object((1,3,6,1,4,1,3224,7,2,1,1,18),_NsSetAuthCfgSecUseDuress_Type())
nsSetAuthCfgSecUseDuress.setMaxAccess(_A)
if mibBuilder.loadTexts:nsSetAuthCfgSecUseDuress.setStatus(_B)
class _NsSetAuthCfgLDAPCni_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,2))
_NsSetAuthCfgLDAPCni_Type.__name__=_E
_NsSetAuthCfgLDAPCni_Object=MibTableColumn
nsSetAuthCfgLDAPCni=_NsSetAuthCfgLDAPCni_Object((1,3,6,1,4,1,3224,7,2,1,1,19),_NsSetAuthCfgLDAPCni_Type())
nsSetAuthCfgLDAPCni.setMaxAccess(_A)
if mibBuilder.loadTexts:nsSetAuthCfgLDAPCni.setStatus(_B)
class _NsSetAuthCfgLDAPDn_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NsSetAuthCfgLDAPDn_Type.__name__=_E
_NsSetAuthCfgLDAPDn_Object=MibTableColumn
nsSetAuthCfgLDAPDn=_NsSetAuthCfgLDAPDn_Object((1,3,6,1,4,1,3224,7,2,1,1,20),_NsSetAuthCfgLDAPDn_Type())
nsSetAuthCfgLDAPDn.setMaxAccess(_A)
if mibBuilder.loadTexts:nsSetAuthCfgLDAPDn.setStatus(_B)
class _NsSetAuthCfgSepChar_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,2))
_NsSetAuthCfgSepChar_Type.__name__=_E
_NsSetAuthCfgSepChar_Object=MibTableColumn
nsSetAuthCfgSepChar=_NsSetAuthCfgSepChar_Object((1,3,6,1,4,1,3224,7,2,1,1,21),_NsSetAuthCfgSepChar_Type())
nsSetAuthCfgSepChar.setMaxAccess(_A)
if mibBuilder.loadTexts:nsSetAuthCfgSepChar.setStatus(_D)
_NsSetAuthCfgSepNumber_Type=Integer32
_NsSetAuthCfgSepNumber_Object=MibTableColumn
nsSetAuthCfgSepNumber=_NsSetAuthCfgSepNumber_Object((1,3,6,1,4,1,3224,7,2,1,1,22),_NsSetAuthCfgSepNumber_Type())
nsSetAuthCfgSepNumber.setMaxAccess(_A)
if mibBuilder.loadTexts:nsSetAuthCfgSepNumber.setStatus(_D)
_NsSetAuthCfgRevInterval_Type=Integer32
_NsSetAuthCfgRevInterval_Object=MibTableColumn
nsSetAuthCfgRevInterval=_NsSetAuthCfgRevInterval_Object((1,3,6,1,4,1,3224,7,2,1,1,23),_NsSetAuthCfgRevInterval_Type())
nsSetAuthCfgRevInterval.setMaxAccess(_A)
if mibBuilder.loadTexts:nsSetAuthCfgRevInterval.setStatus(_D)
_NsSetAuthCfgRadRetries_Type=Integer32
_NsSetAuthCfgRadRetries_Object=MibTableColumn
nsSetAuthCfgRadRetries=_NsSetAuthCfgRadRetries_Object((1,3,6,1,4,1,3224,7,2,1,1,24),_NsSetAuthCfgRadRetries_Type())
nsSetAuthCfgRadRetries.setMaxAccess(_A)
if mibBuilder.loadTexts:nsSetAuthCfgRadRetries.setStatus(_D)
class _NsSetAuthCfgEnableStnID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_NsSetAuthCfgEnableStnID_Type.__name__=_C
_NsSetAuthCfgEnableStnID_Object=MibTableColumn
nsSetAuthCfgEnableStnID=_NsSetAuthCfgEnableStnID_Object((1,3,6,1,4,1,3224,7,2,1,1,25),_NsSetAuthCfgEnableStnID_Type())
nsSetAuthCfgEnableStnID.setMaxAccess(_A)
if mibBuilder.loadTexts:nsSetAuthCfgEnableStnID.setStatus(_D)
class _NsSetAuthCfgDomainName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_NsSetAuthCfgDomainName_Type.__name__=_E
_NsSetAuthCfgDomainName_Object=MibTableColumn
nsSetAuthCfgDomainName=_NsSetAuthCfgDomainName_Object((1,3,6,1,4,1,3224,7,2,1,1,26),_NsSetAuthCfgDomainName_Type())
nsSetAuthCfgDomainName.setMaxAccess(_A)
if mibBuilder.loadTexts:nsSetAuthCfgDomainName.setStatus(_D)
_NsSetAuthCfgAcctSessIdLen_Type=Integer32
_NsSetAuthCfgAcctSessIdLen_Object=MibTableColumn
nsSetAuthCfgAcctSessIdLen=_NsSetAuthCfgAcctSessIdLen_Object((1,3,6,1,4,1,3224,7,2,1,1,27),_NsSetAuthCfgAcctSessIdLen_Type())
nsSetAuthCfgAcctSessIdLen.setMaxAccess(_A)
if mibBuilder.loadTexts:nsSetAuthCfgAcctSessIdLen.setStatus(_D)
class _NsSetAuthCfgRFC2138Compatibility_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_NsSetAuthCfgRFC2138Compatibility_Type.__name__=_C
_NsSetAuthCfgRFC2138Compatibility_Object=MibTableColumn
nsSetAuthCfgRFC2138Compatibility=_NsSetAuthCfgRFC2138Compatibility_Object((1,3,6,1,4,1,3224,7,2,1,1,28),_NsSetAuthCfgRFC2138Compatibility_Type())
nsSetAuthCfgRFC2138Compatibility.setMaxAccess(_A)
if mibBuilder.loadTexts:nsSetAuthCfgRFC2138Compatibility.setStatus(_D)
class _NsSetAuthCfgSourceIfName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_NsSetAuthCfgSourceIfName_Type.__name__=_E
_NsSetAuthCfgSourceIfName_Object=MibTableColumn
nsSetAuthCfgSourceIfName=_NsSetAuthCfgSourceIfName_Object((1,3,6,1,4,1,3224,7,2,1,1,29),_NsSetAuthCfgSourceIfName_Type())
nsSetAuthCfgSourceIfName.setMaxAccess(_A)
if mibBuilder.loadTexts:nsSetAuthCfgSourceIfName.setStatus(_D)
_NsSetAuthCfgAcctPort_Type=Integer32
_NsSetAuthCfgAcctPort_Object=MibTableColumn
nsSetAuthCfgAcctPort=_NsSetAuthCfgAcctPort_Object((1,3,6,1,4,1,3224,7,2,1,1,30),_NsSetAuthCfgAcctPort_Type())
nsSetAuthCfgAcctPort.setMaxAccess(_A)
if mibBuilder.loadTexts:nsSetAuthCfgAcctPort.setStatus(_D)
class _NsSetAuthCfgAcctListActn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('none',0),('cleanup-sess',1)))
_NsSetAuthCfgAcctListActn_Type.__name__=_C
_NsSetAuthCfgAcctListActn_Object=MibTableColumn
nsSetAuthCfgAcctListActn=_NsSetAuthCfgAcctListActn_Object((1,3,6,1,4,1,3224,7,2,1,1,31),_NsSetAuthCfgAcctListActn_Type())
nsSetAuthCfgAcctListActn.setMaxAccess(_A)
if mibBuilder.loadTexts:nsSetAuthCfgAcctListActn.setStatus(_D)
_NsSetAuthCfgSourceIfInfo_Type=Integer32
_NsSetAuthCfgSourceIfInfo_Object=MibTableColumn
nsSetAuthCfgSourceIfInfo=_NsSetAuthCfgSourceIfInfo_Object((1,3,6,1,4,1,3224,7,2,1,1,32),_NsSetAuthCfgSourceIfInfo_Type())
nsSetAuthCfgSourceIfInfo.setMaxAccess(_A)
if mibBuilder.loadTexts:nsSetAuthCfgSourceIfInfo.setStatus(_D)
mibBuilder.exportSymbols(_H,**{'netscreenSetAuthMibModule':netscreenSetAuthMibModule,'nsSetAuth':nsSetAuth,'nsSetAuthCfgTable':nsSetAuthCfgTable,'nsSetAuthCfgEntry':nsSetAuthCfgEntry,_I:nsSetAuthCfgIdx,'nsSetAuthCfgVsys':nsSetAuthCfgVsys,'nsSetAuthCfgName':nsSetAuthCfgName,'nsSetAuthCfgPrimary':nsSetAuthCfgPrimary,'nsSetAuthCfgBackup1':nsSetAuthCfgBackup1,'nsSetAuthCfgBackup2':nsSetAuthCfgBackup2,'nsSetAuthCfgConnIdleTimeout':nsSetAuthCfgConnIdleTimeout,'nsSetAuthCfgAuthAccount':nsSetAuthCfgAuthAccount,'nsSetAuthCfgIkeAccount':nsSetAuthCfgIkeAccount,'nsSetAuthCfgL2tpAccount':nsSetAuthCfgL2tpAccount,'nsSetAuthCfgAdminAccount':nsSetAuthCfgAdminAccount,'nsSetAuthCfgXauthAccount':nsSetAuthCfgXauthAccount,'nsSetAuthCfgMethod':nsSetAuthCfgMethod,'nsSetAuthCfgPort':nsSetAuthCfgPort,'nsSetAuthCfgSecCliRetry':nsSetAuthCfgSecCliRetry,'nsSetAuthCfgSecCliTimeout':nsSetAuthCfgSecCliTimeout,'nsSetAuthCfgSecEncType':nsSetAuthCfgSecEncType,'nsSetAuthCfgSecUseDuress':nsSetAuthCfgSecUseDuress,'nsSetAuthCfgLDAPCni':nsSetAuthCfgLDAPCni,'nsSetAuthCfgLDAPDn':nsSetAuthCfgLDAPDn,'nsSetAuthCfgSepChar':nsSetAuthCfgSepChar,'nsSetAuthCfgSepNumber':nsSetAuthCfgSepNumber,'nsSetAuthCfgRevInterval':nsSetAuthCfgRevInterval,'nsSetAuthCfgRadRetries':nsSetAuthCfgRadRetries,'nsSetAuthCfgEnableStnID':nsSetAuthCfgEnableStnID,'nsSetAuthCfgDomainName':nsSetAuthCfgDomainName,'nsSetAuthCfgAcctSessIdLen':nsSetAuthCfgAcctSessIdLen,'nsSetAuthCfgRFC2138Compatibility':nsSetAuthCfgRFC2138Compatibility,'nsSetAuthCfgSourceIfName':nsSetAuthCfgSourceIfName,'nsSetAuthCfgAcctPort':nsSetAuthCfgAcctPort,'nsSetAuthCfgAcctListActn':nsSetAuthCfgAcctListActn,'nsSetAuthCfgSourceIfInfo':nsSetAuthCfgSourceIfInfo})