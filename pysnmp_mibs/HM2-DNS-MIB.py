_P='deprecated'
_O='hm2DnsClientStaticIndex'
_N='read-only'
_M='hm2DnsClientServerDiagIndex'
_L='hm2DnsClientServerIndex'
_K='InetAddressType'
_J='InetAddress'
_I='HmActionValue'
_H='not-accessible'
_G='SnmpAdminString'
_F='HM2-DNS-MIB'
_E='read-create'
_D='HmEnabledStatus'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
HmActionValue,HmEnabledStatus,hm2ConfigurationMibs=mibBuilder.importSymbols('HM2-TC-MIB',_I,_D,'hm2ConfigurationMibs')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_J,_K)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_G)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
hm2DnsMib=ModuleIdentity((1,3,6,1,4,1,248,11,90))
if mibBuilder.loadTexts:hm2DnsMib.setRevisions(('2011-06-17 00:00',))
_Hm2DnsMibNotifications_ObjectIdentity=ObjectIdentity
hm2DnsMibNotifications=_Hm2DnsMibNotifications_ObjectIdentity((1,3,6,1,4,1,248,11,90,0))
_Hm2DnsMibObjects_ObjectIdentity=ObjectIdentity
hm2DnsMibObjects=_Hm2DnsMibObjects_ObjectIdentity((1,3,6,1,4,1,248,11,90,1))
_Hm2DnsClientGroup_ObjectIdentity=ObjectIdentity
hm2DnsClientGroup=_Hm2DnsClientGroup_ObjectIdentity((1,3,6,1,4,1,248,11,90,1,1))
class _Hm2DnsClientAdminState_Type(HmEnabledStatus):defaultValue=2
_Hm2DnsClientAdminState_Type.__name__=_D
_Hm2DnsClientAdminState_Object=MibScalar
hm2DnsClientAdminState=_Hm2DnsClientAdminState_Object((1,3,6,1,4,1,248,11,90,1,1,1),_Hm2DnsClientAdminState_Type())
hm2DnsClientAdminState.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DnsClientAdminState.setStatus(_A)
class _Hm2DnsClientConfigSource_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('user',1),('mgmt-dhcp',2),('provider',3)))
_Hm2DnsClientConfigSource_Type.__name__=_C
_Hm2DnsClientConfigSource_Object=MibScalar
hm2DnsClientConfigSource=_Hm2DnsClientConfigSource_Object((1,3,6,1,4,1,248,11,90,1,1,2),_Hm2DnsClientConfigSource_Type())
hm2DnsClientConfigSource.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DnsClientConfigSource.setStatus(_A)
_Hm2DnsClientServerCfgTable_Object=MibTable
hm2DnsClientServerCfgTable=_Hm2DnsClientServerCfgTable_Object((1,3,6,1,4,1,248,11,90,1,1,3))
if mibBuilder.loadTexts:hm2DnsClientServerCfgTable.setStatus(_A)
_Hm2DnsClientServerCfgEntry_Object=MibTableRow
hm2DnsClientServerCfgEntry=_Hm2DnsClientServerCfgEntry_Object((1,3,6,1,4,1,248,11,90,1,1,3,1))
hm2DnsClientServerCfgEntry.setIndexNames((0,_F,_L))
if mibBuilder.loadTexts:hm2DnsClientServerCfgEntry.setStatus(_A)
class _Hm2DnsClientServerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_Hm2DnsClientServerIndex_Type.__name__=_C
_Hm2DnsClientServerIndex_Object=MibTableColumn
hm2DnsClientServerIndex=_Hm2DnsClientServerIndex_Object((1,3,6,1,4,1,248,11,90,1,1,3,1,1),_Hm2DnsClientServerIndex_Type())
hm2DnsClientServerIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:hm2DnsClientServerIndex.setStatus(_A)
class _Hm2DnsClientServerAddressType_Type(InetAddressType):defaultValue=1
_Hm2DnsClientServerAddressType_Type.__name__=_K
_Hm2DnsClientServerAddressType_Object=MibTableColumn
hm2DnsClientServerAddressType=_Hm2DnsClientServerAddressType_Object((1,3,6,1,4,1,248,11,90,1,1,3,1,2),_Hm2DnsClientServerAddressType_Type())
hm2DnsClientServerAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DnsClientServerAddressType.setStatus(_A)
class _Hm2DnsClientServerAddress_Type(InetAddress):defaultHexValue='00000000'
_Hm2DnsClientServerAddress_Type.__name__=_J
_Hm2DnsClientServerAddress_Object=MibTableColumn
hm2DnsClientServerAddress=_Hm2DnsClientServerAddress_Object((1,3,6,1,4,1,248,11,90,1,1,3,1,3),_Hm2DnsClientServerAddress_Type())
hm2DnsClientServerAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DnsClientServerAddress.setStatus(_A)
_Hm2DnsClientServerRowStatus_Type=RowStatus
_Hm2DnsClientServerRowStatus_Object=MibTableColumn
hm2DnsClientServerRowStatus=_Hm2DnsClientServerRowStatus_Object((1,3,6,1,4,1,248,11,90,1,1,3,1,4),_Hm2DnsClientServerRowStatus_Type())
hm2DnsClientServerRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:hm2DnsClientServerRowStatus.setStatus(_A)
_Hm2DnsClientServerDiagTable_Object=MibTable
hm2DnsClientServerDiagTable=_Hm2DnsClientServerDiagTable_Object((1,3,6,1,4,1,248,11,90,1,1,4))
if mibBuilder.loadTexts:hm2DnsClientServerDiagTable.setStatus(_A)
_Hm2DnsClientServerDiagEntry_Object=MibTableRow
hm2DnsClientServerDiagEntry=_Hm2DnsClientServerDiagEntry_Object((1,3,6,1,4,1,248,11,90,1,1,4,1))
hm2DnsClientServerDiagEntry.setIndexNames((0,_F,_M))
if mibBuilder.loadTexts:hm2DnsClientServerDiagEntry.setStatus(_A)
class _Hm2DnsClientServerDiagIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_Hm2DnsClientServerDiagIndex_Type.__name__=_C
_Hm2DnsClientServerDiagIndex_Object=MibTableColumn
hm2DnsClientServerDiagIndex=_Hm2DnsClientServerDiagIndex_Object((1,3,6,1,4,1,248,11,90,1,1,4,1,1),_Hm2DnsClientServerDiagIndex_Type())
hm2DnsClientServerDiagIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:hm2DnsClientServerDiagIndex.setStatus(_A)
_Hm2DnsClientServerDiagAddressType_Type=InetAddressType
_Hm2DnsClientServerDiagAddressType_Object=MibTableColumn
hm2DnsClientServerDiagAddressType=_Hm2DnsClientServerDiagAddressType_Object((1,3,6,1,4,1,248,11,90,1,1,4,1,2),_Hm2DnsClientServerDiagAddressType_Type())
hm2DnsClientServerDiagAddressType.setMaxAccess(_N)
if mibBuilder.loadTexts:hm2DnsClientServerDiagAddressType.setStatus(_A)
_Hm2DnsClientServerDiagAddress_Type=InetAddress
_Hm2DnsClientServerDiagAddress_Object=MibTableColumn
hm2DnsClientServerDiagAddress=_Hm2DnsClientServerDiagAddress_Object((1,3,6,1,4,1,248,11,90,1,1,4,1,3),_Hm2DnsClientServerDiagAddress_Type())
hm2DnsClientServerDiagAddress.setMaxAccess(_N)
if mibBuilder.loadTexts:hm2DnsClientServerDiagAddress.setStatus(_A)
_Hm2DnsClientGlobalGroup_ObjectIdentity=ObjectIdentity
hm2DnsClientGlobalGroup=_Hm2DnsClientGlobalGroup_ObjectIdentity((1,3,6,1,4,1,248,11,90,1,1,5))
class _Hm2DnsClientDefaultDomainName_Type(SnmpAdminString):defaultValue=OctetString('');subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_Hm2DnsClientDefaultDomainName_Type.__name__=_G
_Hm2DnsClientDefaultDomainName_Object=MibScalar
hm2DnsClientDefaultDomainName=_Hm2DnsClientDefaultDomainName_Object((1,3,6,1,4,1,248,11,90,1,1,5,1),_Hm2DnsClientDefaultDomainName_Type())
hm2DnsClientDefaultDomainName.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DnsClientDefaultDomainName.setStatus(_A)
class _Hm2DnsClientRequestTimeout_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600))
_Hm2DnsClientRequestTimeout_Type.__name__=_C
_Hm2DnsClientRequestTimeout_Object=MibScalar
hm2DnsClientRequestTimeout=_Hm2DnsClientRequestTimeout_Object((1,3,6,1,4,1,248,11,90,1,1,5,2),_Hm2DnsClientRequestTimeout_Type())
hm2DnsClientRequestTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DnsClientRequestTimeout.setStatus(_A)
class _Hm2DnsClientRequestRetransmits_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_Hm2DnsClientRequestRetransmits_Type.__name__=_C
_Hm2DnsClientRequestRetransmits_Object=MibScalar
hm2DnsClientRequestRetransmits=_Hm2DnsClientRequestRetransmits_Object((1,3,6,1,4,1,248,11,90,1,1,5,3),_Hm2DnsClientRequestRetransmits_Type())
hm2DnsClientRequestRetransmits.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DnsClientRequestRetransmits.setStatus(_A)
class _Hm2DnsClientCacheAdminState_Type(HmEnabledStatus):defaultValue=1
_Hm2DnsClientCacheAdminState_Type.__name__=_D
_Hm2DnsClientCacheAdminState_Object=MibScalar
hm2DnsClientCacheAdminState=_Hm2DnsClientCacheAdminState_Object((1,3,6,1,4,1,248,11,90,1,1,5,4),_Hm2DnsClientCacheAdminState_Type())
hm2DnsClientCacheAdminState.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DnsClientCacheAdminState.setStatus(_A)
_Hm2DnsClientStaticHostConfigTable_Object=MibTable
hm2DnsClientStaticHostConfigTable=_Hm2DnsClientStaticHostConfigTable_Object((1,3,6,1,4,1,248,11,90,1,1,6))
if mibBuilder.loadTexts:hm2DnsClientStaticHostConfigTable.setStatus(_A)
_Hm2DnsClientStaticHostConfigEntry_Object=MibTableRow
hm2DnsClientStaticHostConfigEntry=_Hm2DnsClientStaticHostConfigEntry_Object((1,3,6,1,4,1,248,11,90,1,1,6,1))
hm2DnsClientStaticHostConfigEntry.setIndexNames((0,_F,_O))
if mibBuilder.loadTexts:hm2DnsClientStaticHostConfigEntry.setStatus(_A)
class _Hm2DnsClientStaticIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_Hm2DnsClientStaticIndex_Type.__name__=_C
_Hm2DnsClientStaticIndex_Object=MibTableColumn
hm2DnsClientStaticIndex=_Hm2DnsClientStaticIndex_Object((1,3,6,1,4,1,248,11,90,1,1,6,1,1),_Hm2DnsClientStaticIndex_Type())
hm2DnsClientStaticIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:hm2DnsClientStaticIndex.setStatus(_A)
class _Hm2DnsClientStaticHostName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_Hm2DnsClientStaticHostName_Type.__name__=_G
_Hm2DnsClientStaticHostName_Object=MibTableColumn
hm2DnsClientStaticHostName=_Hm2DnsClientStaticHostName_Object((1,3,6,1,4,1,248,11,90,1,1,6,1,2),_Hm2DnsClientStaticHostName_Type())
hm2DnsClientStaticHostName.setMaxAccess(_E)
if mibBuilder.loadTexts:hm2DnsClientStaticHostName.setStatus(_A)
_Hm2DnsClientStaticHostAddressType_Type=InetAddressType
_Hm2DnsClientStaticHostAddressType_Object=MibTableColumn
hm2DnsClientStaticHostAddressType=_Hm2DnsClientStaticHostAddressType_Object((1,3,6,1,4,1,248,11,90,1,1,6,1,3),_Hm2DnsClientStaticHostAddressType_Type())
hm2DnsClientStaticHostAddressType.setMaxAccess(_E)
if mibBuilder.loadTexts:hm2DnsClientStaticHostAddressType.setStatus(_A)
_Hm2DnsClientStaticHostIPAddress_Type=InetAddress
_Hm2DnsClientStaticHostIPAddress_Object=MibTableColumn
hm2DnsClientStaticHostIPAddress=_Hm2DnsClientStaticHostIPAddress_Object((1,3,6,1,4,1,248,11,90,1,1,6,1,4),_Hm2DnsClientStaticHostIPAddress_Type())
hm2DnsClientStaticHostIPAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:hm2DnsClientStaticHostIPAddress.setStatus(_A)
_Hm2DnsClientStaticHostStatus_Type=RowStatus
_Hm2DnsClientStaticHostStatus_Object=MibTableColumn
hm2DnsClientStaticHostStatus=_Hm2DnsClientStaticHostStatus_Object((1,3,6,1,4,1,248,11,90,1,1,6,1,5),_Hm2DnsClientStaticHostStatus_Type())
hm2DnsClientStaticHostStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:hm2DnsClientStaticHostStatus.setStatus(_A)
_Hm2DnsCacheGroup_ObjectIdentity=ObjectIdentity
hm2DnsCacheGroup=_Hm2DnsCacheGroup_ObjectIdentity((1,3,6,1,4,1,248,11,90,1,2))
class _Hm2DnsCacheAdminState_Type(HmEnabledStatus):defaultValue=1
_Hm2DnsCacheAdminState_Type.__name__=_D
_Hm2DnsCacheAdminState_Object=MibScalar
hm2DnsCacheAdminState=_Hm2DnsCacheAdminState_Object((1,3,6,1,4,1,248,11,90,1,2,1),_Hm2DnsCacheAdminState_Type())
hm2DnsCacheAdminState.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DnsCacheAdminState.setStatus(_P)
class _Hm2DnsCacheFlushAction_Type(HmActionValue):defaultValue=1
_Hm2DnsCacheFlushAction_Type.__name__=_I
_Hm2DnsCacheFlushAction_Object=MibScalar
hm2DnsCacheFlushAction=_Hm2DnsCacheFlushAction_Object((1,3,6,1,4,1,248,11,90,1,2,2),_Hm2DnsCacheFlushAction_Type())
hm2DnsCacheFlushAction.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DnsCacheFlushAction.setStatus(_P)
_Hm2DnsCachingServerGroup_ObjectIdentity=ObjectIdentity
hm2DnsCachingServerGroup=_Hm2DnsCachingServerGroup_ObjectIdentity((1,3,6,1,4,1,248,11,90,1,3))
_Hm2DnsCachingServerGlobalGroup_ObjectIdentity=ObjectIdentity
hm2DnsCachingServerGlobalGroup=_Hm2DnsCachingServerGlobalGroup_ObjectIdentity((1,3,6,1,4,1,248,11,90,1,3,1))
class _Hm2DnsCachingServerAdminState_Type(HmEnabledStatus):defaultValue=1
_Hm2DnsCachingServerAdminState_Type.__name__=_D
_Hm2DnsCachingServerAdminState_Object=MibScalar
hm2DnsCachingServerAdminState=_Hm2DnsCachingServerAdminState_Object((1,3,6,1,4,1,248,11,90,1,3,1,1),_Hm2DnsCachingServerAdminState_Type())
hm2DnsCachingServerAdminState.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DnsCachingServerAdminState.setStatus(_A)
_Hm2DnsMibSNMPExtensionGroup_ObjectIdentity=ObjectIdentity
hm2DnsMibSNMPExtensionGroup=_Hm2DnsMibSNMPExtensionGroup_ObjectIdentity((1,3,6,1,4,1,248,11,90,3))
_Hm2DnsCHHostNameAlreadyExistsSESError_ObjectIdentity=ObjectIdentity
hm2DnsCHHostNameAlreadyExistsSESError=_Hm2DnsCHHostNameAlreadyExistsSESError_ObjectIdentity((1,3,6,1,4,1,248,11,90,3,1))
if mibBuilder.loadTexts:hm2DnsCHHostNameAlreadyExistsSESError.setStatus(_A)
_Hm2DnsCHBadIpNotAcceptedSESError_ObjectIdentity=ObjectIdentity
hm2DnsCHBadIpNotAcceptedSESError=_Hm2DnsCHBadIpNotAcceptedSESError_ObjectIdentity((1,3,6,1,4,1,248,11,90,3,2))
if mibBuilder.loadTexts:hm2DnsCHBadIpNotAcceptedSESError.setStatus(_A)
_Hm2DnsCHBadRowCannotBeActivatedSESError_ObjectIdentity=ObjectIdentity
hm2DnsCHBadRowCannotBeActivatedSESError=_Hm2DnsCHBadRowCannotBeActivatedSESError_ObjectIdentity((1,3,6,1,4,1,248,11,90,3,3))
if mibBuilder.loadTexts:hm2DnsCHBadRowCannotBeActivatedSESError.setStatus(_A)
_Hm2DnsCHHostNameNotValidSESError_ObjectIdentity=ObjectIdentity
hm2DnsCHHostNameNotValidSESError=_Hm2DnsCHHostNameNotValidSESError_ObjectIdentity((1,3,6,1,4,1,248,11,90,3,4))
if mibBuilder.loadTexts:hm2DnsCHHostNameNotValidSESError.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'hm2DnsMib':hm2DnsMib,'hm2DnsMibNotifications':hm2DnsMibNotifications,'hm2DnsMibObjects':hm2DnsMibObjects,'hm2DnsClientGroup':hm2DnsClientGroup,'hm2DnsClientAdminState':hm2DnsClientAdminState,'hm2DnsClientConfigSource':hm2DnsClientConfigSource,'hm2DnsClientServerCfgTable':hm2DnsClientServerCfgTable,'hm2DnsClientServerCfgEntry':hm2DnsClientServerCfgEntry,_L:hm2DnsClientServerIndex,'hm2DnsClientServerAddressType':hm2DnsClientServerAddressType,'hm2DnsClientServerAddress':hm2DnsClientServerAddress,'hm2DnsClientServerRowStatus':hm2DnsClientServerRowStatus,'hm2DnsClientServerDiagTable':hm2DnsClientServerDiagTable,'hm2DnsClientServerDiagEntry':hm2DnsClientServerDiagEntry,_M:hm2DnsClientServerDiagIndex,'hm2DnsClientServerDiagAddressType':hm2DnsClientServerDiagAddressType,'hm2DnsClientServerDiagAddress':hm2DnsClientServerDiagAddress,'hm2DnsClientGlobalGroup':hm2DnsClientGlobalGroup,'hm2DnsClientDefaultDomainName':hm2DnsClientDefaultDomainName,'hm2DnsClientRequestTimeout':hm2DnsClientRequestTimeout,'hm2DnsClientRequestRetransmits':hm2DnsClientRequestRetransmits,'hm2DnsClientCacheAdminState':hm2DnsClientCacheAdminState,'hm2DnsClientStaticHostConfigTable':hm2DnsClientStaticHostConfigTable,'hm2DnsClientStaticHostConfigEntry':hm2DnsClientStaticHostConfigEntry,_O:hm2DnsClientStaticIndex,'hm2DnsClientStaticHostName':hm2DnsClientStaticHostName,'hm2DnsClientStaticHostAddressType':hm2DnsClientStaticHostAddressType,'hm2DnsClientStaticHostIPAddress':hm2DnsClientStaticHostIPAddress,'hm2DnsClientStaticHostStatus':hm2DnsClientStaticHostStatus,'hm2DnsCacheGroup':hm2DnsCacheGroup,'hm2DnsCacheAdminState':hm2DnsCacheAdminState,'hm2DnsCacheFlushAction':hm2DnsCacheFlushAction,'hm2DnsCachingServerGroup':hm2DnsCachingServerGroup,'hm2DnsCachingServerGlobalGroup':hm2DnsCachingServerGlobalGroup,'hm2DnsCachingServerAdminState':hm2DnsCachingServerAdminState,'hm2DnsMibSNMPExtensionGroup':hm2DnsMibSNMPExtensionGroup,'hm2DnsCHHostNameAlreadyExistsSESError':hm2DnsCHHostNameAlreadyExistsSESError,'hm2DnsCHBadIpNotAcceptedSESError':hm2DnsCHBadIpNotAcceptedSESError,'hm2DnsCHBadRowCannotBeActivatedSESError':hm2DnsCHBadRowCannotBeActivatedSESError,'hm2DnsCHHostNameNotValidSESError':hm2DnsCHHostNameNotValidSESError})