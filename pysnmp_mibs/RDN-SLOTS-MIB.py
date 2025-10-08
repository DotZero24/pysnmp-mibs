#
# PySNMP MIB module RDN-SLOTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/riverdelta/RDN-SLOTS-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:07:14 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
rdnDefinitions, = mibBuilder.importSymbols("RDN-DEFINITIONS-MIB", "rdnDefinitions")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rdnSlots = ModuleIdentity((1, 3, 6, 1, 4, 1, 4981, 4, 3))
rdnSlots.setRevisions(('2008-08-08 00:00', '2003-11-05 00:00', '2003-04-29 00:00', '2001-04-18 00:00',))
if mibBuilder.loadTexts: rdnSlots.setLastUpdated('200808080000Z')
if mibBuilder.loadTexts: rdnSlots.setOrganization('Motorola')
rdnSlotsUnknown = MibIdentifier((1, 3, 6, 1, 4, 1, 4981, 4, 3, 0))
rdnSlotsBSR64000Master = MibIdentifier((1, 3, 6, 1, 4, 1, 4981, 4, 3, 1))
rdnSlotsBSR64000IO = MibIdentifier((1, 3, 6, 1, 4, 1, 4981, 4, 3, 2))
rdnSlotsBSR1000 = MibIdentifier((1, 3, 6, 1, 4, 1, 4981, 4, 3, 3))
rdnSlotsOSR2000 = MibIdentifier((1, 3, 6, 1, 4, 1, 4981, 4, 3, 4))
mibBuilder.exportSymbols("RDN-SLOTS-MIB", rdnSlotsBSR64000Master=rdnSlotsBSR64000Master, rdnSlotsBSR64000IO=rdnSlotsBSR64000IO, rdnSlotsOSR2000=rdnSlotsOSR2000, rdnSlotsUnknown=rdnSlotsUnknown, rdnSlots=rdnSlots, rdnSlotsBSR1000=rdnSlotsBSR1000, PYSNMP_MODULE_ID=rdnSlots)
