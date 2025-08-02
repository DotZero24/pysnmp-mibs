_M='agentLdapSearchMapMode'
_L='agentLdapSearchMapName'
_K='read-create'
_J='agentLdapServerIpAddress'
_I='agentLdapServerIpAddrType'
_H='Integer32'
_G='TruthValue'
_F='Unsigned32'
_E='not-accessible'
_D='LANCOM-LDAP-CLIENT-MIB'
_C='SnmpAdminString'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
fastPath,=mibBuilder.importSymbols('LANCOM-REF-MIB','fastPath')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_C)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_G)
agentLdapClientMIB=ModuleIdentity((1,3,6,1,4,1,2356,16,1,73))
if mibBuilder.loadTexts:agentLdapClientMIB.setRevisions(('2017-12-15 12:00',))
_AgentLdapClientObjects_ObjectIdentity=ObjectIdentity
agentLdapClientObjects=_AgentLdapClientObjects_ObjectIdentity((1,3,6,1,4,1,2356,16,1,73,1))
_AgentLdapGlobalConfigGroup_ObjectIdentity=ObjectIdentity
agentLdapGlobalConfigGroup=_AgentLdapGlobalConfigGroup_ObjectIdentity((1,3,6,1,4,1,2356,16,1,73,1,1))
class _AgentLdapBindFirst_Type(TruthValue):defaultValue=2
_AgentLdapBindFirst_Type.__name__=_G
_AgentLdapBindFirst_Object=MibScalar
agentLdapBindFirst=_AgentLdapBindFirst_Object((1,3,6,1,4,1,2356,16,1,73,1,1,1),_AgentLdapBindFirst_Type())
agentLdapBindFirst.setMaxAccess(_B)
if mibBuilder.loadTexts:agentLdapBindFirst.setStatus(_A)
class _AgentLdapAppendWithBaseDN_Type(SnmpAdminString):defaultValue=OctetString('cn=$userid');subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_AgentLdapAppendWithBaseDN_Type.__name__=_C
_AgentLdapAppendWithBaseDN_Object=MibScalar
agentLdapAppendWithBaseDN=_AgentLdapAppendWithBaseDN_Object((1,3,6,1,4,1,2356,16,1,73,1,1,2),_AgentLdapAppendWithBaseDN_Type())
agentLdapAppendWithBaseDN.setMaxAccess(_B)
if mibBuilder.loadTexts:agentLdapAppendWithBaseDN.setStatus(_A)
_AgentLdapServerTable_Object=MibTable
agentLdapServerTable=_AgentLdapServerTable_Object((1,3,6,1,4,1,2356,16,1,73,1,2))
if mibBuilder.loadTexts:agentLdapServerTable.setStatus(_A)
_AgentLdapServerEntry_Object=MibTableRow
agentLdapServerEntry=_AgentLdapServerEntry_Object((1,3,6,1,4,1,2356,16,1,73,1,2,1))
agentLdapServerEntry.setIndexNames((0,_D,_I),(0,_D,_J))
if mibBuilder.loadTexts:agentLdapServerEntry.setStatus(_A)
_AgentLdapServerIpAddrType_Type=InetAddressType
_AgentLdapServerIpAddrType_Object=MibTableColumn
agentLdapServerIpAddrType=_AgentLdapServerIpAddrType_Object((1,3,6,1,4,1,2356,16,1,73,1,2,1,1),_AgentLdapServerIpAddrType_Type())
agentLdapServerIpAddrType.setMaxAccess(_E)
if mibBuilder.loadTexts:agentLdapServerIpAddrType.setStatus(_A)
_AgentLdapServerIpAddress_Type=InetAddress
_AgentLdapServerIpAddress_Object=MibTableColumn
agentLdapServerIpAddress=_AgentLdapServerIpAddress_Object((1,3,6,1,4,1,2356,16,1,73,1,2,1,2),_AgentLdapServerIpAddress_Type())
agentLdapServerIpAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:agentLdapServerIpAddress.setStatus(_A)
_AgentLdapServerStatus_Type=RowStatus
_AgentLdapServerStatus_Object=MibTableColumn
agentLdapServerStatus=_AgentLdapServerStatus_Object((1,3,6,1,4,1,2356,16,1,73,1,2,1,3),_AgentLdapServerStatus_Type())
agentLdapServerStatus.setMaxAccess(_K)
if mibBuilder.loadTexts:agentLdapServerStatus.setStatus(_A)
class _AgentLdapServerPort_Type(Unsigned32):defaultValue=389;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_AgentLdapServerPort_Type.__name__=_F
_AgentLdapServerPort_Object=MibTableColumn
agentLdapServerPort=_AgentLdapServerPort_Object((1,3,6,1,4,1,2356,16,1,73,1,2,1,4),_AgentLdapServerPort_Type())
agentLdapServerPort.setMaxAccess(_B)
if mibBuilder.loadTexts:agentLdapServerPort.setStatus(_A)
class _AgentLdapServerTimeOut_Type(Unsigned32):defaultValue=5;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_AgentLdapServerTimeOut_Type.__name__=_F
_AgentLdapServerTimeOut_Object=MibTableColumn
agentLdapServerTimeOut=_AgentLdapServerTimeOut_Object((1,3,6,1,4,1,2356,16,1,73,1,2,1,5),_AgentLdapServerTimeOut_Type())
agentLdapServerTimeOut.setMaxAccess(_B)
if mibBuilder.loadTexts:agentLdapServerTimeOut.setStatus(_A)
class _AgentLdapServerSSLMode_Type(TruthValue):defaultValue=2
_AgentLdapServerSSLMode_Type.__name__=_G
_AgentLdapServerSSLMode_Object=MibTableColumn
agentLdapServerSSLMode=_AgentLdapServerSSLMode_Object((1,3,6,1,4,1,2356,16,1,73,1,2,1,6),_AgentLdapServerSSLMode_Type())
agentLdapServerSSLMode.setMaxAccess(_B)
if mibBuilder.loadTexts:agentLdapServerSSLMode.setStatus(_A)
class _AgentLdapServerRootDN_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_AgentLdapServerRootDN_Type.__name__=_C
_AgentLdapServerRootDN_Object=MibTableColumn
agentLdapServerRootDN=_AgentLdapServerRootDN_Object((1,3,6,1,4,1,2356,16,1,73,1,2,1,7),_AgentLdapServerRootDN_Type())
agentLdapServerRootDN.setMaxAccess(_B)
if mibBuilder.loadTexts:agentLdapServerRootDN.setStatus(_A)
class _AgentLdapServerRootDNPassword_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_AgentLdapServerRootDNPassword_Type.__name__=_C
_AgentLdapServerRootDNPassword_Object=MibTableColumn
agentLdapServerRootDNPassword=_AgentLdapServerRootDNPassword_Object((1,3,6,1,4,1,2356,16,1,73,1,2,1,8),_AgentLdapServerRootDNPassword_Type())
agentLdapServerRootDNPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:agentLdapServerRootDNPassword.setStatus(_A)
_AgentLdapSearchMapTable_Object=MibTable
agentLdapSearchMapTable=_AgentLdapSearchMapTable_Object((1,3,6,1,4,1,2356,16,1,73,1,3))
if mibBuilder.loadTexts:agentLdapSearchMapTable.setStatus(_A)
_AgentLdapSearchMapEntry_Object=MibTableRow
agentLdapSearchMapEntry=_AgentLdapSearchMapEntry_Object((1,3,6,1,4,1,2356,16,1,73,1,3,1))
agentLdapSearchMapEntry.setIndexNames((0,_D,_L),(0,_D,_M))
if mibBuilder.loadTexts:agentLdapSearchMapEntry.setStatus(_A)
class _AgentLdapSearchMapName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_AgentLdapSearchMapName_Type.__name__=_C
_AgentLdapSearchMapName_Object=MibTableColumn
agentLdapSearchMapName=_AgentLdapSearchMapName_Object((1,3,6,1,4,1,2356,16,1,73,1,3,1,1),_AgentLdapSearchMapName_Type())
agentLdapSearchMapName.setMaxAccess(_E)
if mibBuilder.loadTexts:agentLdapSearchMapName.setStatus(_A)
class _AgentLdapSearchMapMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('userprofile',1))
_AgentLdapSearchMapMode_Type.__name__=_H
_AgentLdapSearchMapMode_Object=MibTableColumn
agentLdapSearchMapMode=_AgentLdapSearchMapMode_Object((1,3,6,1,4,1,2356,16,1,73,1,3,1,2),_AgentLdapSearchMapMode_Type())
agentLdapSearchMapMode.setMaxAccess(_E)
if mibBuilder.loadTexts:agentLdapSearchMapMode.setStatus(_A)
_AgentLdapSearchMapStatus_Type=RowStatus
_AgentLdapSearchMapStatus_Object=MibTableColumn
agentLdapSearchMapStatus=_AgentLdapSearchMapStatus_Object((1,3,6,1,4,1,2356,16,1,73,1,3,1,3),_AgentLdapSearchMapStatus_Type())
agentLdapSearchMapStatus.setMaxAccess(_K)
if mibBuilder.loadTexts:agentLdapSearchMapStatus.setStatus(_A)
class _AgentLdapSearchMapAttribute_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_AgentLdapSearchMapAttribute_Type.__name__=_C
_AgentLdapSearchMapAttribute_Object=MibTableColumn
agentLdapSearchMapAttribute=_AgentLdapSearchMapAttribute_Object((1,3,6,1,4,1,2356,16,1,73,1,3,1,4),_AgentLdapSearchMapAttribute_Type())
agentLdapSearchMapAttribute.setMaxAccess(_B)
if mibBuilder.loadTexts:agentLdapSearchMapAttribute.setStatus(_A)
class _AgentLdapSearchMapFilter_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_AgentLdapSearchMapFilter_Type.__name__=_C
_AgentLdapSearchMapFilter_Object=MibTableColumn
agentLdapSearchMapFilter=_AgentLdapSearchMapFilter_Object((1,3,6,1,4,1,2356,16,1,73,1,3,1,5),_AgentLdapSearchMapFilter_Type())
agentLdapSearchMapFilter.setMaxAccess(_B)
if mibBuilder.loadTexts:agentLdapSearchMapFilter.setStatus(_A)
class _AgentLdapSearchMapBaseDN_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_AgentLdapSearchMapBaseDN_Type.__name__=_C
_AgentLdapSearchMapBaseDN_Object=MibTableColumn
agentLdapSearchMapBaseDN=_AgentLdapSearchMapBaseDN_Object((1,3,6,1,4,1,2356,16,1,73,1,3,1,6),_AgentLdapSearchMapBaseDN_Type())
agentLdapSearchMapBaseDN.setMaxAccess(_B)
if mibBuilder.loadTexts:agentLdapSearchMapBaseDN.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'agentLdapClientMIB':agentLdapClientMIB,'agentLdapClientObjects':agentLdapClientObjects,'agentLdapGlobalConfigGroup':agentLdapGlobalConfigGroup,'agentLdapBindFirst':agentLdapBindFirst,'agentLdapAppendWithBaseDN':agentLdapAppendWithBaseDN,'agentLdapServerTable':agentLdapServerTable,'agentLdapServerEntry':agentLdapServerEntry,_I:agentLdapServerIpAddrType,_J:agentLdapServerIpAddress,'agentLdapServerStatus':agentLdapServerStatus,'agentLdapServerPort':agentLdapServerPort,'agentLdapServerTimeOut':agentLdapServerTimeOut,'agentLdapServerSSLMode':agentLdapServerSSLMode,'agentLdapServerRootDN':agentLdapServerRootDN,'agentLdapServerRootDNPassword':agentLdapServerRootDNPassword,'agentLdapSearchMapTable':agentLdapSearchMapTable,'agentLdapSearchMapEntry':agentLdapSearchMapEntry,_L:agentLdapSearchMapName,_M:agentLdapSearchMapMode,'agentLdapSearchMapStatus':agentLdapSearchMapStatus,'agentLdapSearchMapAttribute':agentLdapSearchMapAttribute,'agentLdapSearchMapFilter':agentLdapSearchMapFilter,'agentLdapSearchMapBaseDN':agentLdapSearchMapBaseDN})