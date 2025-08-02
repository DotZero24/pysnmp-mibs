_G='not-accessible'
_F='zyTacacsAuthenticationServerIndex'
_E='Integer32'
_D='zyTacacsAccountingServerIndex'
_C='ZYXEL-TACACS-MIB'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
esMgmt,=mibBuilder.importSymbols('ZYXEL-ES-SMI','esMgmt')
zyxelTacacs=ModuleIdentity((1,3,6,1,4,1,890,1,15,3,83))
_ZyxelTacacsServerSetup_ObjectIdentity=ObjectIdentity
zyxelTacacsServerSetup=_ZyxelTacacsServerSetup_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,83,1))
_ZyxelTacacsAuthenticationServerSetup_ObjectIdentity=ObjectIdentity
zyxelTacacsAuthenticationServerSetup=_ZyxelTacacsAuthenticationServerSetup_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,83,1,1))
class _ZyTacacsAuthenticationServerMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('indexPriority',1),('roundRobin',2)))
_ZyTacacsAuthenticationServerMode_Type.__name__=_E
_ZyTacacsAuthenticationServerMode_Object=MibScalar
zyTacacsAuthenticationServerMode=_ZyTacacsAuthenticationServerMode_Object((1,3,6,1,4,1,890,1,15,3,83,1,1,1),_ZyTacacsAuthenticationServerMode_Type())
zyTacacsAuthenticationServerMode.setMaxAccess(_B)
if mibBuilder.loadTexts:zyTacacsAuthenticationServerMode.setStatus(_A)
_ZyTacacsAuthenticationServerTimeout_Type=Integer32
_ZyTacacsAuthenticationServerTimeout_Object=MibScalar
zyTacacsAuthenticationServerTimeout=_ZyTacacsAuthenticationServerTimeout_Object((1,3,6,1,4,1,890,1,15,3,83,1,1,2),_ZyTacacsAuthenticationServerTimeout_Type())
zyTacacsAuthenticationServerTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:zyTacacsAuthenticationServerTimeout.setStatus(_A)
_ZyxelTacacsAuthenticationServerTable_Object=MibTable
zyxelTacacsAuthenticationServerTable=_ZyxelTacacsAuthenticationServerTable_Object((1,3,6,1,4,1,890,1,15,3,83,1,1,3))
if mibBuilder.loadTexts:zyxelTacacsAuthenticationServerTable.setStatus(_A)
_ZyxelTacacsAuthenticationServerEntry_Object=MibTableRow
zyxelTacacsAuthenticationServerEntry=_ZyxelTacacsAuthenticationServerEntry_Object((1,3,6,1,4,1,890,1,15,3,83,1,1,3,1))
zyxelTacacsAuthenticationServerEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:zyxelTacacsAuthenticationServerEntry.setStatus(_A)
_ZyTacacsAuthenticationServerIndex_Type=Integer32
_ZyTacacsAuthenticationServerIndex_Object=MibTableColumn
zyTacacsAuthenticationServerIndex=_ZyTacacsAuthenticationServerIndex_Object((1,3,6,1,4,1,890,1,15,3,83,1,1,3,1,1),_ZyTacacsAuthenticationServerIndex_Type())
zyTacacsAuthenticationServerIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:zyTacacsAuthenticationServerIndex.setStatus(_A)
_ZyTacacsAuthenticationServerIpAddress_Type=IpAddress
_ZyTacacsAuthenticationServerIpAddress_Object=MibTableColumn
zyTacacsAuthenticationServerIpAddress=_ZyTacacsAuthenticationServerIpAddress_Object((1,3,6,1,4,1,890,1,15,3,83,1,1,3,1,2),_ZyTacacsAuthenticationServerIpAddress_Type())
zyTacacsAuthenticationServerIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:zyTacacsAuthenticationServerIpAddress.setStatus(_A)
_ZyTacacsAuthenticationServerTcpPort_Type=Integer32
_ZyTacacsAuthenticationServerTcpPort_Object=MibTableColumn
zyTacacsAuthenticationServerTcpPort=_ZyTacacsAuthenticationServerTcpPort_Object((1,3,6,1,4,1,890,1,15,3,83,1,1,3,1,3),_ZyTacacsAuthenticationServerTcpPort_Type())
zyTacacsAuthenticationServerTcpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:zyTacacsAuthenticationServerTcpPort.setStatus(_A)
_ZyTacacsAuthenticationServerSharedSecret_Type=DisplayString
_ZyTacacsAuthenticationServerSharedSecret_Object=MibTableColumn
zyTacacsAuthenticationServerSharedSecret=_ZyTacacsAuthenticationServerSharedSecret_Object((1,3,6,1,4,1,890,1,15,3,83,1,1,3,1,4),_ZyTacacsAuthenticationServerSharedSecret_Type())
zyTacacsAuthenticationServerSharedSecret.setMaxAccess(_B)
if mibBuilder.loadTexts:zyTacacsAuthenticationServerSharedSecret.setStatus(_A)
_ZyxelTacacsAccountingServerSetup_ObjectIdentity=ObjectIdentity
zyxelTacacsAccountingServerSetup=_ZyxelTacacsAccountingServerSetup_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,83,1,2))
_ZyTacacsAccountingServerTimeout_Type=Integer32
_ZyTacacsAccountingServerTimeout_Object=MibScalar
zyTacacsAccountingServerTimeout=_ZyTacacsAccountingServerTimeout_Object((1,3,6,1,4,1,890,1,15,3,83,1,2,1),_ZyTacacsAccountingServerTimeout_Type())
zyTacacsAccountingServerTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:zyTacacsAccountingServerTimeout.setStatus(_A)
_ZyxelTacacsAccountingServerTable_Object=MibTable
zyxelTacacsAccountingServerTable=_ZyxelTacacsAccountingServerTable_Object((1,3,6,1,4,1,890,1,15,3,83,1,2,2))
if mibBuilder.loadTexts:zyxelTacacsAccountingServerTable.setStatus(_A)
_ZyxelTacacsAccountingServerEntry_Object=MibTableRow
zyxelTacacsAccountingServerEntry=_ZyxelTacacsAccountingServerEntry_Object((1,3,6,1,4,1,890,1,15,3,83,1,2,2,1))
zyxelTacacsAccountingServerEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:zyxelTacacsAccountingServerEntry.setStatus(_A)
_ZyTacacsAccountingServerIndex_Type=Integer32
_ZyTacacsAccountingServerIndex_Object=MibTableColumn
zyTacacsAccountingServerIndex=_ZyTacacsAccountingServerIndex_Object((1,3,6,1,4,1,890,1,15,3,83,1,2,2,1,1),_ZyTacacsAccountingServerIndex_Type())
zyTacacsAccountingServerIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:zyTacacsAccountingServerIndex.setStatus(_A)
_ZyTacacsAccountingServerIpAddress_Type=IpAddress
_ZyTacacsAccountingServerIpAddress_Object=MibTableColumn
zyTacacsAccountingServerIpAddress=_ZyTacacsAccountingServerIpAddress_Object((1,3,6,1,4,1,890,1,15,3,83,1,2,2,1,2),_ZyTacacsAccountingServerIpAddress_Type())
zyTacacsAccountingServerIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:zyTacacsAccountingServerIpAddress.setStatus(_A)
_ZyTacacsAccountingServerTcpPort_Type=Integer32
_ZyTacacsAccountingServerTcpPort_Object=MibTableColumn
zyTacacsAccountingServerTcpPort=_ZyTacacsAccountingServerTcpPort_Object((1,3,6,1,4,1,890,1,15,3,83,1,2,2,1,3),_ZyTacacsAccountingServerTcpPort_Type())
zyTacacsAccountingServerTcpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:zyTacacsAccountingServerTcpPort.setStatus(_A)
_ZyTacacsAccountingServerSharedSecret_Type=DisplayString
_ZyTacacsAccountingServerSharedSecret_Object=MibTableColumn
zyTacacsAccountingServerSharedSecret=_ZyTacacsAccountingServerSharedSecret_Object((1,3,6,1,4,1,890,1,15,3,83,1,2,2,1,4),_ZyTacacsAccountingServerSharedSecret_Type())
zyTacacsAccountingServerSharedSecret.setMaxAccess(_B)
if mibBuilder.loadTexts:zyTacacsAccountingServerSharedSecret.setStatus(_A)
_ZyxelTacacsServerNotifications_ObjectIdentity=ObjectIdentity
zyxelTacacsServerNotifications=_ZyxelTacacsServerNotifications_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,83,2))
zyTacacsServerAuthenticationServerUnreachable=NotificationType((1,3,6,1,4,1,890,1,15,3,83,2,1))
zyTacacsServerAuthenticationServerUnreachable.setObjects((_C,_D))
if mibBuilder.loadTexts:zyTacacsServerAuthenticationServerUnreachable.setStatus(_A)
zyTacacsServerAccountingServerUnreachable=NotificationType((1,3,6,1,4,1,890,1,15,3,83,2,2))
zyTacacsServerAccountingServerUnreachable.setObjects((_C,_D))
if mibBuilder.loadTexts:zyTacacsServerAccountingServerUnreachable.setStatus(_A)
zyTacacsServerAuthenticationServerUnreachableRecovered=NotificationType((1,3,6,1,4,1,890,1,15,3,83,2,3))
zyTacacsServerAuthenticationServerUnreachableRecovered.setObjects((_C,_D))
if mibBuilder.loadTexts:zyTacacsServerAuthenticationServerUnreachableRecovered.setStatus(_A)
zyTacacsServerAccountingServerUnreachableRecovered=NotificationType((1,3,6,1,4,1,890,1,15,3,83,2,4))
zyTacacsServerAccountingServerUnreachableRecovered.setObjects((_C,_D))
if mibBuilder.loadTexts:zyTacacsServerAccountingServerUnreachableRecovered.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'zyxelTacacs':zyxelTacacs,'zyxelTacacsServerSetup':zyxelTacacsServerSetup,'zyxelTacacsAuthenticationServerSetup':zyxelTacacsAuthenticationServerSetup,'zyTacacsAuthenticationServerMode':zyTacacsAuthenticationServerMode,'zyTacacsAuthenticationServerTimeout':zyTacacsAuthenticationServerTimeout,'zyxelTacacsAuthenticationServerTable':zyxelTacacsAuthenticationServerTable,'zyxelTacacsAuthenticationServerEntry':zyxelTacacsAuthenticationServerEntry,_F:zyTacacsAuthenticationServerIndex,'zyTacacsAuthenticationServerIpAddress':zyTacacsAuthenticationServerIpAddress,'zyTacacsAuthenticationServerTcpPort':zyTacacsAuthenticationServerTcpPort,'zyTacacsAuthenticationServerSharedSecret':zyTacacsAuthenticationServerSharedSecret,'zyxelTacacsAccountingServerSetup':zyxelTacacsAccountingServerSetup,'zyTacacsAccountingServerTimeout':zyTacacsAccountingServerTimeout,'zyxelTacacsAccountingServerTable':zyxelTacacsAccountingServerTable,'zyxelTacacsAccountingServerEntry':zyxelTacacsAccountingServerEntry,_D:zyTacacsAccountingServerIndex,'zyTacacsAccountingServerIpAddress':zyTacacsAccountingServerIpAddress,'zyTacacsAccountingServerTcpPort':zyTacacsAccountingServerTcpPort,'zyTacacsAccountingServerSharedSecret':zyTacacsAccountingServerSharedSecret,'zyxelTacacsServerNotifications':zyxelTacacsServerNotifications,'zyTacacsServerAuthenticationServerUnreachable':zyTacacsServerAuthenticationServerUnreachable,'zyTacacsServerAccountingServerUnreachable':zyTacacsServerAccountingServerUnreachable,'zyTacacsServerAuthenticationServerUnreachableRecovered':zyTacacsServerAuthenticationServerUnreachableRecovered,'zyTacacsServerAccountingServerUnreachableRecovered':zyTacacsServerAccountingServerUnreachableRecovered})