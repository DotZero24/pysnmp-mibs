#
# PySNMP MIB module HIRSCHMANN-WAN-STATUS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/hirschmann/HIRSCHMANN-WAN-STATUS-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 09:55:47 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
hmWanMgmt, = mibBuilder.importSymbols("HIRSCHMANN-WAN-MIB", "hmWanMgmt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hmWanStatusMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 248, 40, 1, 3))
hmWanStatusMib.setRevisions(('2015-02-13 00:00',))
if mibBuilder.loadTexts: hmWanStatusMib.setLastUpdated('201502130000Z')
if mibBuilder.loadTexts: hmWanStatusMib.setOrganization('Hirschmann Automation and Control GmbH')
hmWanStatusMBusOverload1 = MibScalar((1, 3, 6, 1, 4, 1, 248, 40, 1, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("no", 0), ("yes", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmWanStatusMBusOverload1.setStatus('current')
hmWanStatusMBusOverload2 = MibScalar((1, 3, 6, 1, 4, 1, 248, 40, 1, 3, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("no", 0), ("yes", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmWanStatusMBusOverload2.setStatus('current')
hmWanStatusTemperature = MibScalar((1, 3, 6, 1, 4, 1, 248, 40, 1, 3, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmWanStatusTemperature.setStatus('current')
hmWanStatusVoltage = MibScalar((1, 3, 6, 1, 4, 1, 248, 40, 1, 3, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmWanStatusVoltage.setStatus('current')
mibBuilder.exportSymbols("HIRSCHMANN-WAN-STATUS-MIB", hmWanStatusTemperature=hmWanStatusTemperature, hmWanStatusMib=hmWanStatusMib, hmWanStatusMBusOverload1=hmWanStatusMBusOverload1, PYSNMP_MODULE_ID=hmWanStatusMib, hmWanStatusMBusOverload2=hmWanStatusMBusOverload2, hmWanStatusVoltage=hmWanStatusVoltage)
