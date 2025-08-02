_G='not-accessible'
_F='Integer32'
_E='zyRadiusAccountingServerIndex'
_D='zyRadiusAuthenticationServerIndex'
_C='ZYXEL-RADIUS-MIB'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
esMgmt,=mibBuilder.importSymbols('ZYXEL-ES-SMI','esMgmt')
zyxelRadius=ModuleIdentity((1,3,6,1,4,1,890,1,15,3,71))
_ZyxelRadiusServerSetup_ObjectIdentity=ObjectIdentity
zyxelRadiusServerSetup=_ZyxelRadiusServerSetup_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,71,1))
_ZyxelRadiusAuthenticationServerSetup_ObjectIdentity=ObjectIdentity
zyxelRadiusAuthenticationServerSetup=_ZyxelRadiusAuthenticationServerSetup_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,71,1,1))
class _ZyRadiusAuthenticationServerMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('indexPriority',1),('roundRobin',2)))
_ZyRadiusAuthenticationServerMode_Type.__name__=_F
_ZyRadiusAuthenticationServerMode_Object=MibScalar
zyRadiusAuthenticationServerMode=_ZyRadiusAuthenticationServerMode_Object((1,3,6,1,4,1,890,1,15,3,71,1,1,1),_ZyRadiusAuthenticationServerMode_Type())
zyRadiusAuthenticationServerMode.setMaxAccess(_B)
if mibBuilder.loadTexts:zyRadiusAuthenticationServerMode.setStatus(_A)
_ZyRadiusAuthenticationServerTimeout_Type=Integer32
_ZyRadiusAuthenticationServerTimeout_Object=MibScalar
zyRadiusAuthenticationServerTimeout=_ZyRadiusAuthenticationServerTimeout_Object((1,3,6,1,4,1,890,1,15,3,71,1,1,2),_ZyRadiusAuthenticationServerTimeout_Type())
zyRadiusAuthenticationServerTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:zyRadiusAuthenticationServerTimeout.setStatus(_A)
_ZyxelRadiusAuthenticationServerTable_Object=MibTable
zyxelRadiusAuthenticationServerTable=_ZyxelRadiusAuthenticationServerTable_Object((1,3,6,1,4,1,890,1,15,3,71,1,1,3))
if mibBuilder.loadTexts:zyxelRadiusAuthenticationServerTable.setStatus(_A)
_ZyxelRadiusAuthenticationServerEntry_Object=MibTableRow
zyxelRadiusAuthenticationServerEntry=_ZyxelRadiusAuthenticationServerEntry_Object((1,3,6,1,4,1,890,1,15,3,71,1,1,3,1))
zyxelRadiusAuthenticationServerEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:zyxelRadiusAuthenticationServerEntry.setStatus(_A)
_ZyRadiusAuthenticationServerIndex_Type=Integer32
_ZyRadiusAuthenticationServerIndex_Object=MibTableColumn
zyRadiusAuthenticationServerIndex=_ZyRadiusAuthenticationServerIndex_Object((1,3,6,1,4,1,890,1,15,3,71,1,1,3,1,1),_ZyRadiusAuthenticationServerIndex_Type())
zyRadiusAuthenticationServerIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:zyRadiusAuthenticationServerIndex.setStatus(_A)
_ZyRadiusAuthenticationServerIpAddr_Type=IpAddress
_ZyRadiusAuthenticationServerIpAddr_Object=MibTableColumn
zyRadiusAuthenticationServerIpAddr=_ZyRadiusAuthenticationServerIpAddr_Object((1,3,6,1,4,1,890,1,15,3,71,1,1,3,1,2),_ZyRadiusAuthenticationServerIpAddr_Type())
zyRadiusAuthenticationServerIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:zyRadiusAuthenticationServerIpAddr.setStatus(_A)
_ZyRadiusAuthenticationServerUdpPort_Type=Integer32
_ZyRadiusAuthenticationServerUdpPort_Object=MibTableColumn
zyRadiusAuthenticationServerUdpPort=_ZyRadiusAuthenticationServerUdpPort_Object((1,3,6,1,4,1,890,1,15,3,71,1,1,3,1,3),_ZyRadiusAuthenticationServerUdpPort_Type())
zyRadiusAuthenticationServerUdpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:zyRadiusAuthenticationServerUdpPort.setStatus(_A)
_ZyRadiusAuthenticationServerSharedSecret_Type=DisplayString
_ZyRadiusAuthenticationServerSharedSecret_Object=MibTableColumn
zyRadiusAuthenticationServerSharedSecret=_ZyRadiusAuthenticationServerSharedSecret_Object((1,3,6,1,4,1,890,1,15,3,71,1,1,3,1,4),_ZyRadiusAuthenticationServerSharedSecret_Type())
zyRadiusAuthenticationServerSharedSecret.setMaxAccess(_B)
if mibBuilder.loadTexts:zyRadiusAuthenticationServerSharedSecret.setStatus(_A)
_ZyxelRadiusAccountingServerSetup_ObjectIdentity=ObjectIdentity
zyxelRadiusAccountingServerSetup=_ZyxelRadiusAccountingServerSetup_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,71,1,2))
_ZyRadiusAccountingServerTimeout_Type=Integer32
_ZyRadiusAccountingServerTimeout_Object=MibScalar
zyRadiusAccountingServerTimeout=_ZyRadiusAccountingServerTimeout_Object((1,3,6,1,4,1,890,1,15,3,71,1,2,1),_ZyRadiusAccountingServerTimeout_Type())
zyRadiusAccountingServerTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:zyRadiusAccountingServerTimeout.setStatus(_A)
_ZyxelRadiusAccountingServerTable_Object=MibTable
zyxelRadiusAccountingServerTable=_ZyxelRadiusAccountingServerTable_Object((1,3,6,1,4,1,890,1,15,3,71,1,2,2))
if mibBuilder.loadTexts:zyxelRadiusAccountingServerTable.setStatus(_A)
_ZyxelRadiusAccountingServerEntry_Object=MibTableRow
zyxelRadiusAccountingServerEntry=_ZyxelRadiusAccountingServerEntry_Object((1,3,6,1,4,1,890,1,15,3,71,1,2,2,1))
zyxelRadiusAccountingServerEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:zyxelRadiusAccountingServerEntry.setStatus(_A)
_ZyRadiusAccountingServerIndex_Type=Integer32
_ZyRadiusAccountingServerIndex_Object=MibTableColumn
zyRadiusAccountingServerIndex=_ZyRadiusAccountingServerIndex_Object((1,3,6,1,4,1,890,1,15,3,71,1,2,2,1,1),_ZyRadiusAccountingServerIndex_Type())
zyRadiusAccountingServerIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:zyRadiusAccountingServerIndex.setStatus(_A)
_ZyRadiusAccountingServerIpAddr_Type=IpAddress
_ZyRadiusAccountingServerIpAddr_Object=MibTableColumn
zyRadiusAccountingServerIpAddr=_ZyRadiusAccountingServerIpAddr_Object((1,3,6,1,4,1,890,1,15,3,71,1,2,2,1,2),_ZyRadiusAccountingServerIpAddr_Type())
zyRadiusAccountingServerIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:zyRadiusAccountingServerIpAddr.setStatus(_A)
_ZyRadiusAccountingServerUdpPort_Type=Integer32
_ZyRadiusAccountingServerUdpPort_Object=MibTableColumn
zyRadiusAccountingServerUdpPort=_ZyRadiusAccountingServerUdpPort_Object((1,3,6,1,4,1,890,1,15,3,71,1,2,2,1,3),_ZyRadiusAccountingServerUdpPort_Type())
zyRadiusAccountingServerUdpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:zyRadiusAccountingServerUdpPort.setStatus(_A)
_ZyRadiusAccountingServerSharedSecret_Type=DisplayString
_ZyRadiusAccountingServerSharedSecret_Object=MibTableColumn
zyRadiusAccountingServerSharedSecret=_ZyRadiusAccountingServerSharedSecret_Object((1,3,6,1,4,1,890,1,15,3,71,1,2,2,1,4),_ZyRadiusAccountingServerSharedSecret_Type())
zyRadiusAccountingServerSharedSecret.setMaxAccess(_B)
if mibBuilder.loadTexts:zyRadiusAccountingServerSharedSecret.setStatus(_A)
_ZyxelRadiusAttributeSetup_ObjectIdentity=ObjectIdentity
zyxelRadiusAttributeSetup=_ZyxelRadiusAttributeSetup_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,71,1,3))
_ZyRadiusAttributeNasIpAddress_Type=IpAddress
_ZyRadiusAttributeNasIpAddress_Object=MibScalar
zyRadiusAttributeNasIpAddress=_ZyRadiusAttributeNasIpAddress_Object((1,3,6,1,4,1,890,1,15,3,71,1,3,1),_ZyRadiusAttributeNasIpAddress_Type())
zyRadiusAttributeNasIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:zyRadiusAttributeNasIpAddress.setStatus(_A)
_ZyxelRadiusServerNotifications_ObjectIdentity=ObjectIdentity
zyxelRadiusServerNotifications=_ZyxelRadiusServerNotifications_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,71,2))
zyRadiusServerAuthenticationServerNotReachable=NotificationType((1,3,6,1,4,1,890,1,15,3,71,2,1))
zyRadiusServerAuthenticationServerNotReachable.setObjects((_C,_D))
if mibBuilder.loadTexts:zyRadiusServerAuthenticationServerNotReachable.setStatus(_A)
zyRadiusServerAccountingServerNotReachable=NotificationType((1,3,6,1,4,1,890,1,15,3,71,2,2))
zyRadiusServerAccountingServerNotReachable.setObjects((_C,_E))
if mibBuilder.loadTexts:zyRadiusServerAccountingServerNotReachable.setStatus(_A)
zyRadiusServerAuthenticationServerNotReachableRecovered=NotificationType((1,3,6,1,4,1,890,1,15,3,71,2,3))
zyRadiusServerAuthenticationServerNotReachableRecovered.setObjects((_C,_D))
if mibBuilder.loadTexts:zyRadiusServerAuthenticationServerNotReachableRecovered.setStatus(_A)
zyRadiusServerAccountingServerNotReachableRecovered=NotificationType((1,3,6,1,4,1,890,1,15,3,71,2,4))
zyRadiusServerAccountingServerNotReachableRecovered.setObjects((_C,_E))
if mibBuilder.loadTexts:zyRadiusServerAccountingServerNotReachableRecovered.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'zyxelRadius':zyxelRadius,'zyxelRadiusServerSetup':zyxelRadiusServerSetup,'zyxelRadiusAuthenticationServerSetup':zyxelRadiusAuthenticationServerSetup,'zyRadiusAuthenticationServerMode':zyRadiusAuthenticationServerMode,'zyRadiusAuthenticationServerTimeout':zyRadiusAuthenticationServerTimeout,'zyxelRadiusAuthenticationServerTable':zyxelRadiusAuthenticationServerTable,'zyxelRadiusAuthenticationServerEntry':zyxelRadiusAuthenticationServerEntry,_D:zyRadiusAuthenticationServerIndex,'zyRadiusAuthenticationServerIpAddr':zyRadiusAuthenticationServerIpAddr,'zyRadiusAuthenticationServerUdpPort':zyRadiusAuthenticationServerUdpPort,'zyRadiusAuthenticationServerSharedSecret':zyRadiusAuthenticationServerSharedSecret,'zyxelRadiusAccountingServerSetup':zyxelRadiusAccountingServerSetup,'zyRadiusAccountingServerTimeout':zyRadiusAccountingServerTimeout,'zyxelRadiusAccountingServerTable':zyxelRadiusAccountingServerTable,'zyxelRadiusAccountingServerEntry':zyxelRadiusAccountingServerEntry,_E:zyRadiusAccountingServerIndex,'zyRadiusAccountingServerIpAddr':zyRadiusAccountingServerIpAddr,'zyRadiusAccountingServerUdpPort':zyRadiusAccountingServerUdpPort,'zyRadiusAccountingServerSharedSecret':zyRadiusAccountingServerSharedSecret,'zyxelRadiusAttributeSetup':zyxelRadiusAttributeSetup,'zyRadiusAttributeNasIpAddress':zyRadiusAttributeNasIpAddress,'zyxelRadiusServerNotifications':zyxelRadiusServerNotifications,'zyRadiusServerAuthenticationServerNotReachable':zyRadiusServerAuthenticationServerNotReachable,'zyRadiusServerAccountingServerNotReachable':zyRadiusServerAccountingServerNotReachable,'zyRadiusServerAuthenticationServerNotReachableRecovered':zyRadiusServerAuthenticationServerNotReachableRecovered,'zyRadiusServerAccountingServerNotReachableRecovered':zyRadiusServerAccountingServerNotReachableRecovered})