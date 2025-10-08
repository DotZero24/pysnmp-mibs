#
# PySNMP MIB module HIRSCHMANN-WAN-STATUS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/hirschmann/HIRSCHMANN-WAN-STATUS-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:55:57 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
hmWanMgmt, = mibBuilder.importSymbols("HIRSCHMANN-WAN-MIB", "hmWanMgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("HIRSCHMANN-WAN-STATUS-MIB", hmWanStatusMBusOverload1=hmWanStatusMBusOverload1, hmWanStatusMBusOverload2=hmWanStatusMBusOverload2, hmWanStatusVoltage=hmWanStatusVoltage, hmWanStatusTemperature=hmWanStatusTemperature, hmWanStatusMib=hmWanStatusMib, PYSNMP_MODULE_ID=hmWanStatusMib)
