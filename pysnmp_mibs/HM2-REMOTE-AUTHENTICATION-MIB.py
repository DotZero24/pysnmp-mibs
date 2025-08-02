_P='hm2LdapClientServerStatus'
_O='hm2LdapRoleMappingIndex'
_N='accessible-for-notify'
_M='InetPortNumber'
_L='InetAddressType'
_K='InetAddress'
_J='HmEnabledStatus'
_I='Hm2TlsVersions'
_H='Hm2TlsCipherSuites'
_G='hm2LdapClientServerIndex'
_F='HM2-REMOTE-AUTHENTICATION-MIB'
_E='Integer32'
_D='SnmpAdminString'
_C='read-create'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
Hm2TlsCipherSuites,Hm2TlsVersions=mibBuilder.importSymbols('HM2-MGMTACCESS-MIB',_H,_I)
HmEnabledStatus,hm2ConfigurationMibs=mibBuilder.importSymbols('HM2-TC-MIB',_J,'hm2ConfigurationMibs')
Hm2UserAccessRoles,=mibBuilder.importSymbols('HM2-USERMGMT-MIB','Hm2UserAccessRoles')
InetAddress,InetAddressType,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB',_K,_L,_M)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_D)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
hm2RemoteAuthMib=ModuleIdentity((1,3,6,1,4,1,248,11,26))
if mibBuilder.loadTexts:hm2RemoteAuthMib.setRevisions(('2014-03-06 00:00',))
_Hm2RemoteAuthMibNotifications_ObjectIdentity=ObjectIdentity
hm2RemoteAuthMibNotifications=_Hm2RemoteAuthMibNotifications_ObjectIdentity((1,3,6,1,4,1,248,11,26,0))
_Hm2RemoteAuthMibObjects_ObjectIdentity=ObjectIdentity
hm2RemoteAuthMibObjects=_Hm2RemoteAuthMibObjects_ObjectIdentity((1,3,6,1,4,1,248,11,26,1))
_Hm2LdapGroup_ObjectIdentity=ObjectIdentity
hm2LdapGroup=_Hm2LdapGroup_ObjectIdentity((1,3,6,1,4,1,248,11,26,1,1))
_Hm2LdapConfigGroup_ObjectIdentity=ObjectIdentity
hm2LdapConfigGroup=_Hm2LdapConfigGroup_ObjectIdentity((1,3,6,1,4,1,248,11,26,1,1,10))
class _Hm2LdapClientAdminState_Type(HmEnabledStatus):defaultValue=2
_Hm2LdapClientAdminState_Type.__name__=_J
_Hm2LdapClientAdminState_Object=MibScalar
hm2LdapClientAdminState=_Hm2LdapClientAdminState_Object((1,3,6,1,4,1,248,11,26,1,1,10,1),_Hm2LdapClientAdminState_Type())
hm2LdapClientAdminState.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2LdapClientAdminState.setStatus(_A)
class _Hm2LdapClientCacheTimeout_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1440))
_Hm2LdapClientCacheTimeout_Type.__name__=_E
_Hm2LdapClientCacheTimeout_Object=MibScalar
hm2LdapClientCacheTimeout=_Hm2LdapClientCacheTimeout_Object((1,3,6,1,4,1,248,11,26,1,1,10,2),_Hm2LdapClientCacheTimeout_Type())
hm2LdapClientCacheTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2LdapClientCacheTimeout.setStatus(_A)
class _Hm2LdapClientServerBaseDN_Type(SnmpAdminString):defaultValue=OctetString('');subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_Hm2LdapClientServerBaseDN_Type.__name__=_D
_Hm2LdapClientServerBaseDN_Object=MibScalar
hm2LdapClientServerBaseDN=_Hm2LdapClientServerBaseDN_Object((1,3,6,1,4,1,248,11,26,1,1,10,3),_Hm2LdapClientServerBaseDN_Type())
hm2LdapClientServerBaseDN.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2LdapClientServerBaseDN.setStatus(_A)
class _Hm2LdapClientServerSearchAttribute_Type(SnmpAdminString):defaultValue=OctetString('userPrincipalName');subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_Hm2LdapClientServerSearchAttribute_Type.__name__=_D
_Hm2LdapClientServerSearchAttribute_Object=MibScalar
hm2LdapClientServerSearchAttribute=_Hm2LdapClientServerSearchAttribute_Object((1,3,6,1,4,1,248,11,26,1,1,10,4),_Hm2LdapClientServerSearchAttribute_Type())
hm2LdapClientServerSearchAttribute.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2LdapClientServerSearchAttribute.setStatus(_A)
class _Hm2LdapClientServerBindUser_Type(SnmpAdminString):defaultValue=OctetString('');subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_Hm2LdapClientServerBindUser_Type.__name__=_D
_Hm2LdapClientServerBindUser_Object=MibScalar
hm2LdapClientServerBindUser=_Hm2LdapClientServerBindUser_Object((1,3,6,1,4,1,248,11,26,1,1,10,5),_Hm2LdapClientServerBindUser_Type())
hm2LdapClientServerBindUser.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2LdapClientServerBindUser.setStatus(_A)
class _Hm2LdapClientServerBindUserPasswd_Type(SnmpAdminString):defaultValue=OctetString('');subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_Hm2LdapClientServerBindUserPasswd_Type.__name__=_D
_Hm2LdapClientServerBindUserPasswd_Object=MibScalar
hm2LdapClientServerBindUserPasswd=_Hm2LdapClientServerBindUserPasswd_Object((1,3,6,1,4,1,248,11,26,1,1,10,6),_Hm2LdapClientServerBindUserPasswd_Type())
hm2LdapClientServerBindUserPasswd.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2LdapClientServerBindUserPasswd.setStatus(_A)
class _Hm2LdapClientServerDefaultDomain_Type(SnmpAdminString):defaultValue=OctetString('');subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_Hm2LdapClientServerDefaultDomain_Type.__name__=_D
_Hm2LdapClientServerDefaultDomain_Object=MibScalar
hm2LdapClientServerDefaultDomain=_Hm2LdapClientServerDefaultDomain_Object((1,3,6,1,4,1,248,11,26,1,1,10,7),_Hm2LdapClientServerDefaultDomain_Type())
hm2LdapClientServerDefaultDomain.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2LdapClientServerDefaultDomain.setStatus(_A)
class _Hm2LdapClientTlsVersions_Type(Hm2TlsVersions):defaultBinValue='101'
_Hm2LdapClientTlsVersions_Type.__name__=_I
_Hm2LdapClientTlsVersions_Object=MibScalar
hm2LdapClientTlsVersions=_Hm2LdapClientTlsVersions_Object((1,3,6,1,4,1,248,11,26,1,1,10,8),_Hm2LdapClientTlsVersions_Type())
hm2LdapClientTlsVersions.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2LdapClientTlsVersions.setStatus(_A)
class _Hm2LdapClientTlsCipherSuites_Type(Hm2TlsCipherSuites):defaultBinValue='0010101'
_Hm2LdapClientTlsCipherSuites_Type.__name__=_H
_Hm2LdapClientTlsCipherSuites_Object=MibScalar
hm2LdapClientTlsCipherSuites=_Hm2LdapClientTlsCipherSuites_Object((1,3,6,1,4,1,248,11,26,1,1,10,9),_Hm2LdapClientTlsCipherSuites_Type())
hm2LdapClientTlsCipherSuites.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2LdapClientTlsCipherSuites.setStatus(_A)
_Hm2LdapClientServerAddrTable_Object=MibTable
hm2LdapClientServerAddrTable=_Hm2LdapClientServerAddrTable_Object((1,3,6,1,4,1,248,11,26,1,1,10,20))
if mibBuilder.loadTexts:hm2LdapClientServerAddrTable.setStatus(_A)
_Hm2LdapClientServerAddrEntry_Object=MibTableRow
hm2LdapClientServerAddrEntry=_Hm2LdapClientServerAddrEntry_Object((1,3,6,1,4,1,248,11,26,1,1,10,20,1))
hm2LdapClientServerAddrEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:hm2LdapClientServerAddrEntry.setStatus(_A)
class _Hm2LdapClientServerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_Hm2LdapClientServerIndex_Type.__name__=_E
_Hm2LdapClientServerIndex_Object=MibTableColumn
hm2LdapClientServerIndex=_Hm2LdapClientServerIndex_Object((1,3,6,1,4,1,248,11,26,1,1,10,20,1,1),_Hm2LdapClientServerIndex_Type())
hm2LdapClientServerIndex.setMaxAccess(_N)
if mibBuilder.loadTexts:hm2LdapClientServerIndex.setStatus(_A)
class _Hm2LdapClientServerDescr_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_Hm2LdapClientServerDescr_Type.__name__=_D
_Hm2LdapClientServerDescr_Object=MibTableColumn
hm2LdapClientServerDescr=_Hm2LdapClientServerDescr_Object((1,3,6,1,4,1,248,11,26,1,1,10,20,1,2),_Hm2LdapClientServerDescr_Type())
hm2LdapClientServerDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2LdapClientServerDescr.setStatus(_A)
class _Hm2LdapClientServerAddrType_Type(InetAddressType):defaultValue=1
_Hm2LdapClientServerAddrType_Type.__name__=_L
_Hm2LdapClientServerAddrType_Object=MibTableColumn
hm2LdapClientServerAddrType=_Hm2LdapClientServerAddrType_Object((1,3,6,1,4,1,248,11,26,1,1,10,20,1,3),_Hm2LdapClientServerAddrType_Type())
hm2LdapClientServerAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2LdapClientServerAddrType.setStatus(_A)
class _Hm2LdapClientServerAddr_Type(InetAddress):defaultHexValue='00000000'
_Hm2LdapClientServerAddr_Type.__name__=_K
_Hm2LdapClientServerAddr_Object=MibTableColumn
hm2LdapClientServerAddr=_Hm2LdapClientServerAddr_Object((1,3,6,1,4,1,248,11,26,1,1,10,20,1,4),_Hm2LdapClientServerAddr_Type())
hm2LdapClientServerAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2LdapClientServerAddr.setStatus(_A)
class _Hm2LdapClientServerPort_Type(InetPortNumber):defaultValue=389
_Hm2LdapClientServerPort_Type.__name__=_M
_Hm2LdapClientServerPort_Object=MibTableColumn
hm2LdapClientServerPort=_Hm2LdapClientServerPort_Object((1,3,6,1,4,1,248,11,26,1,1,10,20,1,5),_Hm2LdapClientServerPort_Type())
hm2LdapClientServerPort.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2LdapClientServerPort.setStatus(_A)
class _Hm2LdapClientServerSecurity_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('ssl',2),('startTLS',3)))
_Hm2LdapClientServerSecurity_Type.__name__=_E
_Hm2LdapClientServerSecurity_Object=MibTableColumn
hm2LdapClientServerSecurity=_Hm2LdapClientServerSecurity_Object((1,3,6,1,4,1,248,11,26,1,1,10,20,1,6),_Hm2LdapClientServerSecurity_Type())
hm2LdapClientServerSecurity.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2LdapClientServerSecurity.setStatus(_A)
class _Hm2LdapClientServerStatus_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ok',1),('unreachable',2),('other',3)))
_Hm2LdapClientServerStatus_Type.__name__=_E
_Hm2LdapClientServerStatus_Object=MibTableColumn
hm2LdapClientServerStatus=_Hm2LdapClientServerStatus_Object((1,3,6,1,4,1,248,11,26,1,1,10,20,1,7),_Hm2LdapClientServerStatus_Type())
hm2LdapClientServerStatus.setMaxAccess('read-only')
if mibBuilder.loadTexts:hm2LdapClientServerStatus.setStatus(_A)
_Hm2LdapClientServerRowStatus_Type=RowStatus
_Hm2LdapClientServerRowStatus_Object=MibTableColumn
hm2LdapClientServerRowStatus=_Hm2LdapClientServerRowStatus_Object((1,3,6,1,4,1,248,11,26,1,1,10,20,1,8),_Hm2LdapClientServerRowStatus_Type())
hm2LdapClientServerRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2LdapClientServerRowStatus.setStatus(_A)
_Hm2LdapMappingGroup_ObjectIdentity=ObjectIdentity
hm2LdapMappingGroup=_Hm2LdapMappingGroup_ObjectIdentity((1,3,6,1,4,1,248,11,26,1,1,20))
class _Hm2LdapRoleMatchingPolicy_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('highest',1),('first',2)))
_Hm2LdapRoleMatchingPolicy_Type.__name__=_E
_Hm2LdapRoleMatchingPolicy_Object=MibScalar
hm2LdapRoleMatchingPolicy=_Hm2LdapRoleMatchingPolicy_Object((1,3,6,1,4,1,248,11,26,1,1,20,1),_Hm2LdapRoleMatchingPolicy_Type())
hm2LdapRoleMatchingPolicy.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2LdapRoleMatchingPolicy.setStatus(_A)
_Hm2LdapRoleMappingTable_Object=MibTable
hm2LdapRoleMappingTable=_Hm2LdapRoleMappingTable_Object((1,3,6,1,4,1,248,11,26,1,1,20,10))
if mibBuilder.loadTexts:hm2LdapRoleMappingTable.setStatus(_A)
_Hm2LdapRoleMappingEntry_Object=MibTableRow
hm2LdapRoleMappingEntry=_Hm2LdapRoleMappingEntry_Object((1,3,6,1,4,1,248,11,26,1,1,20,10,1))
hm2LdapRoleMappingEntry.setIndexNames((0,_F,_O))
if mibBuilder.loadTexts:hm2LdapRoleMappingEntry.setStatus(_A)
class _Hm2LdapRoleMappingIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_Hm2LdapRoleMappingIndex_Type.__name__=_E
_Hm2LdapRoleMappingIndex_Object=MibTableColumn
hm2LdapRoleMappingIndex=_Hm2LdapRoleMappingIndex_Object((1,3,6,1,4,1,248,11,26,1,1,20,10,1,1),_Hm2LdapRoleMappingIndex_Type())
hm2LdapRoleMappingIndex.setMaxAccess(_N)
if mibBuilder.loadTexts:hm2LdapRoleMappingIndex.setStatus(_A)
_Hm2LdapRoleMappingAccessRole_Type=Hm2UserAccessRoles
_Hm2LdapRoleMappingAccessRole_Object=MibTableColumn
hm2LdapRoleMappingAccessRole=_Hm2LdapRoleMappingAccessRole_Object((1,3,6,1,4,1,248,11,26,1,1,20,10,1,2),_Hm2LdapRoleMappingAccessRole_Type())
hm2LdapRoleMappingAccessRole.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2LdapRoleMappingAccessRole.setStatus(_A)
class _Hm2LdapRoleMappingType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('attribute',1),('group',2)))
_Hm2LdapRoleMappingType_Type.__name__=_E
_Hm2LdapRoleMappingType_Object=MibTableColumn
hm2LdapRoleMappingType=_Hm2LdapRoleMappingType_Object((1,3,6,1,4,1,248,11,26,1,1,20,10,1,3),_Hm2LdapRoleMappingType_Type())
hm2LdapRoleMappingType.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2LdapRoleMappingType.setStatus(_A)
class _Hm2LdapRoleMappingParameter_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_Hm2LdapRoleMappingParameter_Type.__name__=_D
_Hm2LdapRoleMappingParameter_Object=MibTableColumn
hm2LdapRoleMappingParameter=_Hm2LdapRoleMappingParameter_Object((1,3,6,1,4,1,248,11,26,1,1,20,10,1,4),_Hm2LdapRoleMappingParameter_Type())
hm2LdapRoleMappingParameter.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2LdapRoleMappingParameter.setStatus(_A)
_Hm2LdapRoleMappingRowStatus_Type=RowStatus
_Hm2LdapRoleMappingRowStatus_Object=MibTableColumn
hm2LdapRoleMappingRowStatus=_Hm2LdapRoleMappingRowStatus_Object((1,3,6,1,4,1,248,11,26,1,1,20,10,1,5),_Hm2LdapRoleMappingRowStatus_Type())
hm2LdapRoleMappingRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2LdapRoleMappingRowStatus.setStatus(_A)
_Hm2RemoteAuthMibSNMPExtensionGroup_ObjectIdentity=ObjectIdentity
hm2RemoteAuthMibSNMPExtensionGroup=_Hm2RemoteAuthMibSNMPExtensionGroup_ObjectIdentity((1,3,6,1,4,1,248,11,26,3))
_Hm2LdapSESGroup_ObjectIdentity=ObjectIdentity
hm2LdapSESGroup=_Hm2LdapSESGroup_ObjectIdentity((1,3,6,1,4,1,248,11,26,3,1))
_Hm2LdapSESDuplicateIPorHost_ObjectIdentity=ObjectIdentity
hm2LdapSESDuplicateIPorHost=_Hm2LdapSESDuplicateIPorHost_ObjectIdentity((1,3,6,1,4,1,248,11,26,3,1,1))
if mibBuilder.loadTexts:hm2LdapSESDuplicateIPorHost.setStatus(_A)
hm2LdapConfigStatusTrap=NotificationType((1,3,6,1,4,1,248,11,26,0,1))
hm2LdapConfigStatusTrap.setObjects(*((_F,_G),(_F,_P)))
if mibBuilder.loadTexts:hm2LdapConfigStatusTrap.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'hm2RemoteAuthMib':hm2RemoteAuthMib,'hm2RemoteAuthMibNotifications':hm2RemoteAuthMibNotifications,'hm2LdapConfigStatusTrap':hm2LdapConfigStatusTrap,'hm2RemoteAuthMibObjects':hm2RemoteAuthMibObjects,'hm2LdapGroup':hm2LdapGroup,'hm2LdapConfigGroup':hm2LdapConfigGroup,'hm2LdapClientAdminState':hm2LdapClientAdminState,'hm2LdapClientCacheTimeout':hm2LdapClientCacheTimeout,'hm2LdapClientServerBaseDN':hm2LdapClientServerBaseDN,'hm2LdapClientServerSearchAttribute':hm2LdapClientServerSearchAttribute,'hm2LdapClientServerBindUser':hm2LdapClientServerBindUser,'hm2LdapClientServerBindUserPasswd':hm2LdapClientServerBindUserPasswd,'hm2LdapClientServerDefaultDomain':hm2LdapClientServerDefaultDomain,'hm2LdapClientTlsVersions':hm2LdapClientTlsVersions,'hm2LdapClientTlsCipherSuites':hm2LdapClientTlsCipherSuites,'hm2LdapClientServerAddrTable':hm2LdapClientServerAddrTable,'hm2LdapClientServerAddrEntry':hm2LdapClientServerAddrEntry,_G:hm2LdapClientServerIndex,'hm2LdapClientServerDescr':hm2LdapClientServerDescr,'hm2LdapClientServerAddrType':hm2LdapClientServerAddrType,'hm2LdapClientServerAddr':hm2LdapClientServerAddr,'hm2LdapClientServerPort':hm2LdapClientServerPort,'hm2LdapClientServerSecurity':hm2LdapClientServerSecurity,_P:hm2LdapClientServerStatus,'hm2LdapClientServerRowStatus':hm2LdapClientServerRowStatus,'hm2LdapMappingGroup':hm2LdapMappingGroup,'hm2LdapRoleMatchingPolicy':hm2LdapRoleMatchingPolicy,'hm2LdapRoleMappingTable':hm2LdapRoleMappingTable,'hm2LdapRoleMappingEntry':hm2LdapRoleMappingEntry,_O:hm2LdapRoleMappingIndex,'hm2LdapRoleMappingAccessRole':hm2LdapRoleMappingAccessRole,'hm2LdapRoleMappingType':hm2LdapRoleMappingType,'hm2LdapRoleMappingParameter':hm2LdapRoleMappingParameter,'hm2LdapRoleMappingRowStatus':hm2LdapRoleMappingRowStatus,'hm2RemoteAuthMibSNMPExtensionGroup':hm2RemoteAuthMibSNMPExtensionGroup,'hm2LdapSESGroup':hm2LdapSESGroup,'hm2LdapSESDuplicateIPorHost':hm2LdapSESDuplicateIPorHost})