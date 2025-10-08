#
# PySNMP MIB module AT-PIM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/allied-old/AT-PIM-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:41:09 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
modules, = mibBuilder.importSymbols("AT-SMI-MIB", "modules")
pimInterfaceStatus, pimNeighborIfIndex = mibBuilder.importSymbols("PIM-MIB", "pimInterfaceStatus", "pimNeighborIfIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("AT-PIM-MIB", pim4NeighbourDeletedTrap=pim4NeighbourDeletedTrap, pim4NeighbourAddedTrap=pim4NeighbourAddedTrap, pim4InterfaceUpTrap=pim4InterfaceUpTrap, PYSNMP_MODULE_ID=pim4, pim4InterfaceDownTrap=pim4InterfaceDownTrap, pim4ErrorTrapType=pim4ErrorTrapType, pim4Events=pim4Events, pim4ErrorTrap=pim4ErrorTrap, pim4=pim4)
