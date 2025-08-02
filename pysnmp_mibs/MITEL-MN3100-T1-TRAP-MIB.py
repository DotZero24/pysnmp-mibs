_E='mitelMn3100dsx1LineSatusChangeNotif'
_D='MITEL-MN3100-T1-TRAP-MIB'
_C='current'
_B='dsx1LineStatus'
_A='RFC1406-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dsx1LineStatus,=mibBuilder.importSymbols(_A,_B)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
mitelDS1Extension=ModuleIdentity((1,3,6,1,4,1,1027,4,12))
if mibBuilder.loadTexts:mitelDS1Extension.setRevisions(('2003-03-24 01:41','2002-04-02 00:00'))
_Mitel_ObjectIdentity=ObjectIdentity
mitel=_Mitel_ObjectIdentity((1,3,6,1,4,1,1027))
_MitelIdentification_ObjectIdentity=ObjectIdentity
mitelIdentification=_MitelIdentification_ObjectIdentity((1,3,6,1,4,1,1027,1))
_MitelIdCallServers_ObjectIdentity=ObjectIdentity
mitelIdCallServers=_MitelIdCallServers_ObjectIdentity((1,3,6,1,4,1,1027,1,2))
_MitelIdCsIpera1000_ObjectIdentity=ObjectIdentity
mitelIdCsIpera1000=_MitelIdCsIpera1000_ObjectIdentity((1,3,6,1,4,1,1027,1,2,4))
_MitelProprietary_ObjectIdentity=ObjectIdentity
mitelProprietary=_MitelProprietary_ObjectIdentity((1,3,6,1,4,1,1027,4))
mitelMn3100dsx1LineSatusChangeNotif=NotificationType((1,3,6,1,4,1,1027,1,2,4,0,410))
mitelMn3100dsx1LineSatusChangeNotif.setObjects((_A,_B))
if mibBuilder.loadTexts:mitelMn3100dsx1LineSatusChangeNotif.setStatus(_C)
mitelIpera1000Notifications=NotificationGroup((1,3,6,1,4,1,1027,1,2,4,0))
mitelIpera1000Notifications.setObjects((_D,_E))
if mibBuilder.loadTexts:mitelIpera1000Notifications.setStatus(_C)
mibBuilder.exportSymbols(_D,**{'mitel':mitel,'mitelIdentification':mitelIdentification,'mitelIdCallServers':mitelIdCallServers,'mitelIdCsIpera1000':mitelIdCsIpera1000,'mitelIpera1000Notifications':mitelIpera1000Notifications,_E:mitelMn3100dsx1LineSatusChangeNotif,'mitelProprietary':mitelProprietary,'mitelDS1Extension':mitelDS1Extension})