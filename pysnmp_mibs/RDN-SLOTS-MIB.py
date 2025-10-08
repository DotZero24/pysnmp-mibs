#
# PySNMP MIB module RDN-SLOTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/riverdelta/RDN-SLOTS-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:16:00 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
rdnDefinitions, = mibBuilder.importSymbols("RDN-DEFINITIONS-MIB", "rdnDefinitions")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
rdnSlots = ModuleIdentity((1, 3, 6, 1, 4, 1, 4981, 4, 3))
rdnSlots.setRevisions(('2008-08-08 00:00', '2003-11-05 00:00', '2003-04-29 00:00', '2001-04-18 00:00',))
if mibBuilder.loadTexts: rdnSlots.setLastUpdated('200808080000Z')
if mibBuilder.loadTexts: rdnSlots.setOrganization('Motorola')
rdnSlotsUnknown = MibIdentifier((1, 3, 6, 1, 4, 1, 4981, 4, 3, 0))
rdnSlotsBSR64000Master = MibIdentifier((1, 3, 6, 1, 4, 1, 4981, 4, 3, 1))
rdnSlotsBSR64000IO = MibIdentifier((1, 3, 6, 1, 4, 1, 4981, 4, 3, 2))
rdnSlotsBSR1000 = MibIdentifier((1, 3, 6, 1, 4, 1, 4981, 4, 3, 3))
rdnSlotsOSR2000 = MibIdentifier((1, 3, 6, 1, 4, 1, 4981, 4, 3, 4))
mibBuilder.exportSymbols("RDN-SLOTS-MIB", rdnSlotsUnknown=rdnSlotsUnknown, rdnSlotsBSR1000=rdnSlotsBSR1000, PYSNMP_MODULE_ID=rdnSlots, rdnSlotsBSR64000Master=rdnSlotsBSR64000Master, rdnSlotsBSR64000IO=rdnSlotsBSR64000IO, rdnSlots=rdnSlots, rdnSlotsOSR2000=rdnSlotsOSR2000)
