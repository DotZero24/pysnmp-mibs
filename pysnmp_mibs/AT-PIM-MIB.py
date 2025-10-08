#
# PySNMP MIB module AT-PIM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/allied-old/AT-PIM-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:08:10 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
modules, = mibBuilder.importSymbols("AT-SMI-MIB", "modules")
pimInterfaceStatus, pimNeighborIfIndex = mibBuilder.importSymbols("PIM-MIB", "pimInterfaceStatus", "pimNeighborIfIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
pim4 = ModuleIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 97))
pim4.setRevisions(('2005-01-20 15:25',))
if mibBuilder.loadTexts: pim4.setLastUpdated('200501201525Z')
if mibBuilder.loadTexts: pim4.setOrganization('Allied Telesis, Inc')
pim4Events = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 97, 0))
pim4NeighbourAddedTrap = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 97, 0, 1)).setObjects(("PIM-MIB", "pimNeighborIfIndex"))
if mibBuilder.loadTexts: pim4NeighbourAddedTrap.setStatus('current')
pim4NeighbourDeletedTrap = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 97, 0, 2)).setObjects(("PIM-MIB", "pimNeighborIfIndex"))
if mibBuilder.loadTexts: pim4NeighbourDeletedTrap.setStatus('current')
pim4InterfaceUpTrap = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 97, 0, 3)).setObjects(("PIM-MIB", "pimInterfaceStatus"))
if mibBuilder.loadTexts: pim4InterfaceUpTrap.setStatus('current')
pim4InterfaceDownTrap = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 97, 0, 4)).setObjects(("PIM-MIB", "pimInterfaceStatus"))
if mibBuilder.loadTexts: pim4InterfaceDownTrap.setStatus('current')
pim4ErrorTrap = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 97, 0, 5)).setObjects(("AT-PIM-MIB", "pim4ErrorTrapType"))
if mibBuilder.loadTexts: pim4ErrorTrap.setStatus('current')
pim4ErrorTrapType = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 97, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("pim4InvalidPacket", 1), ("pim4InvalidDestinationError", 2), ("pim4FragmentError", 3), ("pim4LengthError", 4), ("pim4GroupaddressError", 5), ("pim4SourceaddressError", 6), ("pim4MissingOptionError", 7), ("pim4GeneralError", 8), ("pim4InternalError", 9), ("pim4RpaddressError", 10)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: pim4ErrorTrapType.setStatus('current')
mibBuilder.exportSymbols("AT-PIM-MIB", pim4=pim4, pim4ErrorTrapType=pim4ErrorTrapType, pim4NeighbourDeletedTrap=pim4NeighbourDeletedTrap, pim4ErrorTrap=pim4ErrorTrap, PYSNMP_MODULE_ID=pim4, pim4InterfaceDownTrap=pim4InterfaceDownTrap, pim4Events=pim4Events, pim4InterfaceUpTrap=pim4InterfaceUpTrap, pim4NeighbourAddedTrap=pim4NeighbourAddedTrap)
