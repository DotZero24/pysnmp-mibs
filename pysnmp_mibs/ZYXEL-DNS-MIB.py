_G='zyDnsNameServerIndex'
_F='not-accessible'
_E='zyDnsStaticNameServerPreference'
_D='Integer32'
_C='ZYXEL-DNS-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
esMgmt,=mibBuilder.importSymbols('ZYXEL-ES-SMI','esMgmt')
zyxelDns=ModuleIdentity((1,3,6,1,4,1,890,1,15,3,111))
_ZyxelDnsSetup_ObjectIdentity=ObjectIdentity
zyxelDnsSetup=_ZyxelDnsSetup_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,111,1))
_ZyxelDnsStaticNameServerTable_Object=MibTable
zyxelDnsStaticNameServerTable=_ZyxelDnsStaticNameServerTable_Object((1,3,6,1,4,1,890,1,15,3,111,1,1))
if mibBuilder.loadTexts:zyxelDnsStaticNameServerTable.setStatus(_A)
_ZyxelDnsStaticNameServerEntry_Object=MibTableRow
zyxelDnsStaticNameServerEntry=_ZyxelDnsStaticNameServerEntry_Object((1,3,6,1,4,1,890,1,15,3,111,1,1,1))
zyxelDnsStaticNameServerEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:zyxelDnsStaticNameServerEntry.setStatus(_A)
_ZyDnsStaticNameServerPreference_Type=Integer32
_ZyDnsStaticNameServerPreference_Object=MibTableColumn
zyDnsStaticNameServerPreference=_ZyDnsStaticNameServerPreference_Object((1,3,6,1,4,1,890,1,15,3,111,1,1,1,1),_ZyDnsStaticNameServerPreference_Type())
zyDnsStaticNameServerPreference.setMaxAccess(_F)
if mibBuilder.loadTexts:zyDnsStaticNameServerPreference.setStatus(_A)
_ZyDnsStaticNameServerInetAddressType_Type=InetAddressType
_ZyDnsStaticNameServerInetAddressType_Object=MibTableColumn
zyDnsStaticNameServerInetAddressType=_ZyDnsStaticNameServerInetAddressType_Object((1,3,6,1,4,1,890,1,15,3,111,1,1,1,2),_ZyDnsStaticNameServerInetAddressType_Type())
zyDnsStaticNameServerInetAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:zyDnsStaticNameServerInetAddressType.setStatus(_A)
_ZyDnsStaticNameServerInetAddress_Type=InetAddress
_ZyDnsStaticNameServerInetAddress_Object=MibTableColumn
zyDnsStaticNameServerInetAddress=_ZyDnsStaticNameServerInetAddress_Object((1,3,6,1,4,1,890,1,15,3,111,1,1,1,3),_ZyDnsStaticNameServerInetAddress_Type())
zyDnsStaticNameServerInetAddress.setMaxAccess('read-write')
if mibBuilder.loadTexts:zyDnsStaticNameServerInetAddress.setStatus(_A)
_ZyxelDnsStatus_ObjectIdentity=ObjectIdentity
zyxelDnsStatus=_ZyxelDnsStatus_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,111,2))
_ZyxelDnsNameServerTable_Object=MibTable
zyxelDnsNameServerTable=_ZyxelDnsNameServerTable_Object((1,3,6,1,4,1,890,1,15,3,111,2,1))
if mibBuilder.loadTexts:zyxelDnsNameServerTable.setStatus(_A)
_ZyxelDnsNameServerEntry_Object=MibTableRow
zyxelDnsNameServerEntry=_ZyxelDnsNameServerEntry_Object((1,3,6,1,4,1,890,1,15,3,111,2,1,1))
zyxelDnsNameServerEntry.setIndexNames((0,_C,_G))
if mibBuilder.loadTexts:zyxelDnsNameServerEntry.setStatus(_A)
_ZyDnsNameServerIndex_Type=Integer32
_ZyDnsNameServerIndex_Object=MibTableColumn
zyDnsNameServerIndex=_ZyDnsNameServerIndex_Object((1,3,6,1,4,1,890,1,15,3,111,2,1,1,1),_ZyDnsNameServerIndex_Type())
zyDnsNameServerIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:zyDnsNameServerIndex.setStatus(_A)
_ZyDnsNameServerInetAddressType_Type=InetAddressType
_ZyDnsNameServerInetAddressType_Object=MibTableColumn
zyDnsNameServerInetAddressType=_ZyDnsNameServerInetAddressType_Object((1,3,6,1,4,1,890,1,15,3,111,2,1,1,2),_ZyDnsNameServerInetAddressType_Type())
zyDnsNameServerInetAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:zyDnsNameServerInetAddressType.setStatus(_A)
_ZyDnsNameServerInetAddress_Type=InetAddress
_ZyDnsNameServerInetAddress_Object=MibTableColumn
zyDnsNameServerInetAddress=_ZyDnsNameServerInetAddress_Object((1,3,6,1,4,1,890,1,15,3,111,2,1,1,3),_ZyDnsNameServerInetAddress_Type())
zyDnsNameServerInetAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:zyDnsNameServerInetAddress.setStatus(_A)
class _ZyDnsNameServerSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('static',0),('dhcpv4',1),('dhcpv6',2)))
_ZyDnsNameServerSource_Type.__name__=_D
_ZyDnsNameServerSource_Object=MibTableColumn
zyDnsNameServerSource=_ZyDnsNameServerSource_Object((1,3,6,1,4,1,890,1,15,3,111,2,1,1,4),_ZyDnsNameServerSource_Type())
zyDnsNameServerSource.setMaxAccess(_B)
if mibBuilder.loadTexts:zyDnsNameServerSource.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'zyxelDns':zyxelDns,'zyxelDnsSetup':zyxelDnsSetup,'zyxelDnsStaticNameServerTable':zyxelDnsStaticNameServerTable,'zyxelDnsStaticNameServerEntry':zyxelDnsStaticNameServerEntry,_E:zyDnsStaticNameServerPreference,'zyDnsStaticNameServerInetAddressType':zyDnsStaticNameServerInetAddressType,'zyDnsStaticNameServerInetAddress':zyDnsStaticNameServerInetAddress,'zyxelDnsStatus':zyxelDnsStatus,'zyxelDnsNameServerTable':zyxelDnsNameServerTable,'zyxelDnsNameServerEntry':zyxelDnsNameServerEntry,_G:zyDnsNameServerIndex,'zyDnsNameServerInetAddressType':zyDnsNameServerInetAddressType,'zyDnsNameServerInetAddress':zyDnsNameServerInetAddress,'zyDnsNameServerSource':zyDnsNameServerSource})