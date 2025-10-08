#
# PySNMP MIB module TMESNMP2-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/papouch/TMESNMP2-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:27:55 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
tme, = mibBuilder.importSymbols("Papouch-SMI", "tme")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
vars = MibIdentifier((1, 3, 6, 1, 4, 1, 18248, 1, 1))
traps = MibIdentifier((1, 3, 6, 1, 4, 1, 18248, 1, 2))
int_temperature = MibScalar((1, 3, 6, 1, 4, 1, 18248, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: int_temperature.setStatus('current')
string_temperature = MibScalar((1, 3, 6, 1, 4, 1, 18248, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: string_temperature.setStatus('current')
device_name = MibScalar((1, 3, 6, 1, 4, 1, 18248, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: device_name.setStatus('current')
int_temperature_t = MibScalar((1, 3, 6, 1, 4, 1, 18248, 1, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: int_temperature_t.setStatus('current')
string_temperature_t = MibScalar((1, 3, 6, 1, 4, 1, 18248, 1, 2, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: string_temperature_t.setStatus('current')
device_name_t = MibScalar((1, 3, 6, 1, 4, 1, 18248, 1, 2, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: device_name_t.setStatus('current')
warning_t = MibScalar((1, 3, 6, 1, 4, 1, 18248, 1, 2, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: warning_t.setStatus('current')
mibBuilder.exportSymbols("TMESNMP2-MIB", device_name_t=device_name_t, int_temperature_t=int_temperature_t, string_temperature=string_temperature, int_temperature=int_temperature, device_name=device_name, traps=traps, string_temperature_t=string_temperature_t, warning_t=warning_t, vars=vars)
