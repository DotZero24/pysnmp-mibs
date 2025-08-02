_G='pim4ErrorTrapType'
_F='AT-PIM-MIB'
_E='Integer32'
_D='pimNeighborIfIndex'
_C='pimInterfaceStatus'
_B='PIM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
modules,=mibBuilder.importSymbols('AT-SMI-MIB','modules')
pimInterfaceStatus,pimNeighborIfIndex=mibBuilder.importSymbols(_B,_C,_D)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
pim4=ModuleIdentity((1,3,6,1,4,1,207,8,4,4,4,97))
if mibBuilder.loadTexts:pim4.setRevisions(('2005-01-20 15:25',))
_Pim4Events_ObjectIdentity=ObjectIdentity
pim4Events=_Pim4Events_ObjectIdentity((1,3,6,1,4,1,207,8,4,4,4,97,0))
class _Pim4ErrorTrapType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('pim4InvalidPacket',1),('pim4InvalidDestinationError',2),('pim4FragmentError',3),('pim4LengthError',4),('pim4GroupaddressError',5),('pim4SourceaddressError',6),('pim4MissingOptionError',7),('pim4GeneralError',8),('pim4InternalError',9),('pim4RpaddressError',10)))
_Pim4ErrorTrapType_Type.__name__=_E
_Pim4ErrorTrapType_Object=MibScalar
pim4ErrorTrapType=_Pim4ErrorTrapType_Object((1,3,6,1,4,1,207,8,4,4,4,97,1),_Pim4ErrorTrapType_Type())
pim4ErrorTrapType.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:pim4ErrorTrapType.setStatus(_A)
pim4NeighbourAddedTrap=NotificationType((1,3,6,1,4,1,207,8,4,4,4,97,0,1))
pim4NeighbourAddedTrap.setObjects((_B,_D))
if mibBuilder.loadTexts:pim4NeighbourAddedTrap.setStatus(_A)
pim4NeighbourDeletedTrap=NotificationType((1,3,6,1,4,1,207,8,4,4,4,97,0,2))
pim4NeighbourDeletedTrap.setObjects((_B,_D))
if mibBuilder.loadTexts:pim4NeighbourDeletedTrap.setStatus(_A)
pim4InterfaceUpTrap=NotificationType((1,3,6,1,4,1,207,8,4,4,4,97,0,3))
pim4InterfaceUpTrap.setObjects((_B,_C))
if mibBuilder.loadTexts:pim4InterfaceUpTrap.setStatus(_A)
pim4InterfaceDownTrap=NotificationType((1,3,6,1,4,1,207,8,4,4,4,97,0,4))
pim4InterfaceDownTrap.setObjects((_B,_C))
if mibBuilder.loadTexts:pim4InterfaceDownTrap.setStatus(_A)
pim4ErrorTrap=NotificationType((1,3,6,1,4,1,207,8,4,4,4,97,0,5))
pim4ErrorTrap.setObjects((_F,_G))
if mibBuilder.loadTexts:pim4ErrorTrap.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'pim4':pim4,'pim4Events':pim4Events,'pim4NeighbourAddedTrap':pim4NeighbourAddedTrap,'pim4NeighbourDeletedTrap':pim4NeighbourDeletedTrap,'pim4InterfaceUpTrap':pim4InterfaceUpTrap,'pim4InterfaceDownTrap':pim4InterfaceDownTrap,'pim4ErrorTrap':pim4ErrorTrap,_G:pim4ErrorTrapType})