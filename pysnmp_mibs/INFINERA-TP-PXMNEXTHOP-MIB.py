_F='pxmNextHopGroup'
_E='pxmNextHopMacAddress'
_D='ifIndex'
_C='IF-MIB'
_B='INFINERA-TP-PXMNEXTHOP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_C,_D)
terminationPoint,=mibBuilder.importSymbols('INFINERA-REG-MIB','terminationPoint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
pxmNextHopMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,2,68))
_PxmNextHopTable_Object=MibTable
pxmNextHopTable=_PxmNextHopTable_Object((1,3,6,1,4,1,21296,2,2,2,2,68,1))
if mibBuilder.loadTexts:pxmNextHopTable.setStatus(_A)
_PxmNextHopEntry_Object=MibTableRow
pxmNextHopEntry=_PxmNextHopEntry_Object((1,3,6,1,4,1,21296,2,2,2,2,68,1,1))
pxmNextHopEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:pxmNextHopEntry.setStatus(_A)
_PxmNextHopMacAddress_Type=DisplayString
_PxmNextHopMacAddress_Object=MibTableColumn
pxmNextHopMacAddress=_PxmNextHopMacAddress_Object((1,3,6,1,4,1,21296,2,2,2,2,68,1,1,1),_PxmNextHopMacAddress_Type())
pxmNextHopMacAddress.setMaxAccess('read-write')
if mibBuilder.loadTexts:pxmNextHopMacAddress.setStatus(_A)
_PxmNextHopConformance_ObjectIdentity=ObjectIdentity
pxmNextHopConformance=_PxmNextHopConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,68,3))
_PxmNextHopCompliances_ObjectIdentity=ObjectIdentity
pxmNextHopCompliances=_PxmNextHopCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,68,3,1))
_PxmNextHopGroups_ObjectIdentity=ObjectIdentity
pxmNextHopGroups=_PxmNextHopGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,68,3,2))
pxmNextHopGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,2,68,3,2,1))
pxmNextHopGroup.setObjects((_B,_E))
if mibBuilder.loadTexts:pxmNextHopGroup.setStatus(_A)
pxmNextHopCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,2,68,3,1,1))
pxmNextHopCompliance.setObjects((_B,_F))
if mibBuilder.loadTexts:pxmNextHopCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'pxmNextHopMIB':pxmNextHopMIB,'pxmNextHopTable':pxmNextHopTable,'pxmNextHopEntry':pxmNextHopEntry,_E:pxmNextHopMacAddress,'pxmNextHopConformance':pxmNextHopConformance,'pxmNextHopCompliances':pxmNextHopCompliances,'pxmNextHopCompliance':pxmNextHopCompliance,'pxmNextHopGroups':pxmNextHopGroups,_F:pxmNextHopGroup})