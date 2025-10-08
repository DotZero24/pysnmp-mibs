#
# PySNMP MIB module TMESNMP2-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/papouch/TMESNMP2-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:50:28 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
tme, = mibBuilder.importSymbols("Papouch-SMI", "tme")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("TMESNMP2-MIB", vars=vars, warning_t=warning_t, int_temperature_t=int_temperature_t, device_name_t=device_name_t, device_name=device_name, string_temperature=string_temperature, string_temperature_t=string_temperature_t, int_temperature=int_temperature, traps=traps)
