_H='wwpDnsServerIpAddr'
_G='WWP-APPLICATIONS-MIB'
_F='DisplayString'
_E='enable'
_D='disable'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','RowStatus','TextualConvention')
wwpModules,=mibBuilder.importSymbols('WWP-SMI','wwpModules')
wwpApplicationsMIB=ModuleIdentity((1,3,6,1,4,1,6141,2,6))
if mibBuilder.loadTexts:wwpApplicationsMIB.setRevisions(('2001-04-03 17:00',))
_WwpApplicationsMIBObjects_ObjectIdentity=ObjectIdentity
wwpApplicationsMIBObjects=_WwpApplicationsMIBObjects_ObjectIdentity((1,3,6,1,4,1,6141,2,6,1))
_WwpWeb_ObjectIdentity=ObjectIdentity
wwpWeb=_WwpWeb_ObjectIdentity((1,3,6,1,4,1,6141,2,6,1,2))
class _WwpWebEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_WwpWebEnable_Type.__name__=_C
_WwpWebEnable_Object=MibScalar
wwpWebEnable=_WwpWebEnable_Object((1,3,6,1,4,1,6141,2,6,1,2,1),_WwpWebEnable_Type())
wwpWebEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpWebEnable.setStatus(_A)
class _WwpWebMaxLogins_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5))
_WwpWebMaxLogins_Type.__name__=_C
_WwpWebMaxLogins_Object=MibScalar
wwpWebMaxLogins=_WwpWebMaxLogins_Object((1,3,6,1,4,1,6141,2,6,1,2,2),_WwpWebMaxLogins_Type())
wwpWebMaxLogins.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpWebMaxLogins.setStatus(_A)
class _WwpWebInactivityTimeout_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600))
_WwpWebInactivityTimeout_Type.__name__=_C
_WwpWebInactivityTimeout_Object=MibScalar
wwpWebInactivityTimeout=_WwpWebInactivityTimeout_Object((1,3,6,1,4,1,6141,2,6,1,2,3),_WwpWebInactivityTimeout_Type())
wwpWebInactivityTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpWebInactivityTimeout.setStatus(_A)
_WwpTelnet_ObjectIdentity=ObjectIdentity
wwpTelnet=_WwpTelnet_ObjectIdentity((1,3,6,1,4,1,6141,2,6,1,3))
class _WwpTelnetEnableServer_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_WwpTelnetEnableServer_Type.__name__=_C
_WwpTelnetEnableServer_Object=MibScalar
wwpTelnetEnableServer=_WwpTelnetEnableServer_Object((1,3,6,1,4,1,6141,2,6,1,3,1),_WwpTelnetEnableServer_Type())
wwpTelnetEnableServer.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpTelnetEnableServer.setStatus(_A)
class _WwpTelnetMaxConnections_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5))
_WwpTelnetMaxConnections_Type.__name__=_C
_WwpTelnetMaxConnections_Object=MibScalar
wwpTelnetMaxConnections=_WwpTelnetMaxConnections_Object((1,3,6,1,4,1,6141,2,6,1,3,2),_WwpTelnetMaxConnections_Type())
wwpTelnetMaxConnections.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpTelnetMaxConnections.setStatus(_A)
class _WwpTelnetTimeout_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1800))
_WwpTelnetTimeout_Type.__name__=_C
_WwpTelnetTimeout_Object=MibScalar
wwpTelnetTimeout=_WwpTelnetTimeout_Object((1,3,6,1,4,1,6141,2,6,1,3,3),_WwpTelnetTimeout_Type())
wwpTelnetTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpTelnetTimeout.setStatus(_A)
class _WwpTelnetEnableClient_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_WwpTelnetEnableClient_Type.__name__=_C
_WwpTelnetEnableClient_Object=MibScalar
wwpTelnetEnableClient=_WwpTelnetEnableClient_Object((1,3,6,1,4,1,6141,2,6,1,3,4),_WwpTelnetEnableClient_Type())
wwpTelnetEnableClient.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpTelnetEnableClient.setStatus(_A)
_WwpDns_ObjectIdentity=ObjectIdentity
wwpDns=_WwpDns_ObjectIdentity((1,3,6,1,4,1,6141,2,6,1,4))
class _WwpDnsEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_WwpDnsEnable_Type.__name__=_C
_WwpDnsEnable_Object=MibScalar
wwpDnsEnable=_WwpDnsEnable_Object((1,3,6,1,4,1,6141,2,6,1,4,1),_WwpDnsEnable_Type())
wwpDnsEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpDnsEnable.setStatus(_A)
class _WwpDnsDomainName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_WwpDnsDomainName_Type.__name__=_F
_WwpDnsDomainName_Object=MibScalar
wwpDnsDomainName=_WwpDnsDomainName_Object((1,3,6,1,4,1,6141,2,6,1,4,2),_WwpDnsDomainName_Type())
wwpDnsDomainName.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpDnsDomainName.setStatus(_A)
_WwpDnsServerTable_Object=MibTable
wwpDnsServerTable=_WwpDnsServerTable_Object((1,3,6,1,4,1,6141,2,6,1,4,3))
if mibBuilder.loadTexts:wwpDnsServerTable.setStatus(_A)
_WwpDnsServerEntry_Object=MibTableRow
wwpDnsServerEntry=_WwpDnsServerEntry_Object((1,3,6,1,4,1,6141,2,6,1,4,3,1))
wwpDnsServerEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:wwpDnsServerEntry.setStatus(_A)
_WwpDnsServerIpAddr_Type=IpAddress
_WwpDnsServerIpAddr_Object=MibTableColumn
wwpDnsServerIpAddr=_WwpDnsServerIpAddr_Object((1,3,6,1,4,1,6141,2,6,1,4,3,1,1),_WwpDnsServerIpAddr_Type())
wwpDnsServerIpAddr.setMaxAccess('read-only')
if mibBuilder.loadTexts:wwpDnsServerIpAddr.setStatus(_A)
class _WwpDnsServerPrimary_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('primary',1),('secondary',2)))
_WwpDnsServerPrimary_Type.__name__=_C
_WwpDnsServerPrimary_Object=MibTableColumn
wwpDnsServerPrimary=_WwpDnsServerPrimary_Object((1,3,6,1,4,1,6141,2,6,1,4,3,1,2),_WwpDnsServerPrimary_Type())
wwpDnsServerPrimary.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpDnsServerPrimary.setStatus(_A)
_WwpDnsServerRowStatus_Type=RowStatus
_WwpDnsServerRowStatus_Object=MibTableColumn
wwpDnsServerRowStatus=_WwpDnsServerRowStatus_Object((1,3,6,1,4,1,6141,2,6,1,4,3,1,3),_WwpDnsServerRowStatus_Type())
wwpDnsServerRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:wwpDnsServerRowStatus.setStatus(_A)
_WwpLog_ObjectIdentity=ObjectIdentity
wwpLog=_WwpLog_ObjectIdentity((1,3,6,1,4,1,6141,2,6,1,5))
_WwpLogServerAddr_Type=IpAddress
_WwpLogServerAddr_Object=MibScalar
wwpLogServerAddr=_WwpLogServerAddr_Object((1,3,6,1,4,1,6141,2,6,1,5,1),_WwpLogServerAddr_Type())
wwpLogServerAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLogServerAddr.setStatus(_A)
class _WwpLogServerPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpLogServerPort_Type.__name__=_C
_WwpLogServerPort_Object=MibScalar
wwpLogServerPort=_WwpLogServerPort_Object((1,3,6,1,4,1,6141,2,6,1,5,2),_WwpLogServerPort_Type())
wwpLogServerPort.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLogServerPort.setStatus(_A)
_WwpApplicationsMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
wwpApplicationsMIBNotificationPrefix=_WwpApplicationsMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,6141,2,6,2))
_WwpApplicationsMIBNotifications_ObjectIdentity=ObjectIdentity
wwpApplicationsMIBNotifications=_WwpApplicationsMIBNotifications_ObjectIdentity((1,3,6,1,4,1,6141,2,6,2,0))
_WwpApplicationsMIBConformance_ObjectIdentity=ObjectIdentity
wwpApplicationsMIBConformance=_WwpApplicationsMIBConformance_ObjectIdentity((1,3,6,1,4,1,6141,2,6,3))
_WwpApplicationsMIBCompliances_ObjectIdentity=ObjectIdentity
wwpApplicationsMIBCompliances=_WwpApplicationsMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6141,2,6,3,1))
_WwpApplicationsMIBGroups_ObjectIdentity=ObjectIdentity
wwpApplicationsMIBGroups=_WwpApplicationsMIBGroups_ObjectIdentity((1,3,6,1,4,1,6141,2,6,3,2))
mibBuilder.exportSymbols(_G,**{'wwpApplicationsMIB':wwpApplicationsMIB,'wwpApplicationsMIBObjects':wwpApplicationsMIBObjects,'wwpWeb':wwpWeb,'wwpWebEnable':wwpWebEnable,'wwpWebMaxLogins':wwpWebMaxLogins,'wwpWebInactivityTimeout':wwpWebInactivityTimeout,'wwpTelnet':wwpTelnet,'wwpTelnetEnableServer':wwpTelnetEnableServer,'wwpTelnetMaxConnections':wwpTelnetMaxConnections,'wwpTelnetTimeout':wwpTelnetTimeout,'wwpTelnetEnableClient':wwpTelnetEnableClient,'wwpDns':wwpDns,'wwpDnsEnable':wwpDnsEnable,'wwpDnsDomainName':wwpDnsDomainName,'wwpDnsServerTable':wwpDnsServerTable,'wwpDnsServerEntry':wwpDnsServerEntry,_H:wwpDnsServerIpAddr,'wwpDnsServerPrimary':wwpDnsServerPrimary,'wwpDnsServerRowStatus':wwpDnsServerRowStatus,'wwpLog':wwpLog,'wwpLogServerAddr':wwpLogServerAddr,'wwpLogServerPort':wwpLogServerPort,'wwpApplicationsMIBNotificationPrefix':wwpApplicationsMIBNotificationPrefix,'wwpApplicationsMIBNotifications':wwpApplicationsMIBNotifications,'wwpApplicationsMIBConformance':wwpApplicationsMIBConformance,'wwpApplicationsMIBCompliances':wwpApplicationsMIBCompliances,'wwpApplicationsMIBGroups':wwpApplicationsMIBGroups})