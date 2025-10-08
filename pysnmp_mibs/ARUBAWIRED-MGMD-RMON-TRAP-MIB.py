#
# PySNMP MIB module ARUBAWIRED-MGMD-RMON-TRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/aruba/ARUBAWIRED-MGMD-RMON-TRAP-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:44:09 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
wndFeatures, = mibBuilder.importSymbols("ARUBAWIRED-NETWORKING-OID", "wndFeatures")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
eventIndex, eventDescription = mibBuilder.importSymbols("RMON-MIB", "eventIndex", "eventDescription")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
arubaWiredMgmdRmonTrapMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 4))
arubaWiredMgmdRmonTrapMIB.setRevisions(('2017-11-02 00:00',))
if mibBuilder.loadTexts: arubaWiredMgmdRmonTrapMIB.setLastUpdated('201711020000Z')
if mibBuilder.loadTexts: arubaWiredMgmdRmonTrapMIB.setOrganization('HPE/Aruba Networking Division')
arubaWiredMgmdRmonTrapNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 4, 1))
arubaWiredMgmdRmonTrapEvent = NotificationType((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 4, 1, 1)).setObjects(("RMON-MIB", "eventIndex"), ("RMON-MIB", "eventDescription"))
if mibBuilder.loadTexts: arubaWiredMgmdRmonTrapEvent.setStatus('current')
mibBuilder.exportSymbols("ARUBAWIRED-MGMD-RMON-TRAP-MIB", PYSNMP_MODULE_ID=arubaWiredMgmdRmonTrapMIB, arubaWiredMgmdRmonTrapEvent=arubaWiredMgmdRmonTrapEvent, arubaWiredMgmdRmonTrapMIB=arubaWiredMgmdRmonTrapMIB, arubaWiredMgmdRmonTrapNotifications=arubaWiredMgmdRmonTrapNotifications)
