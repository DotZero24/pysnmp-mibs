#
# PySNMP MIB module SNMP-TEST-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/radlan/SNMP-TEST-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:07:48 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
rlSnmpTestSimulatedVariables, = mibBuilder.importSymbols("RADLAN-rndApplications", "rlSnmpTestSimulatedVariables")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, Counter64, TimeTicks, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "Counter64", "TimeTicks", "ModuleIdentity", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class KeyBits(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("firstKey", 0), ("secondKey", 1), ("thirdKey", 2), ("fourthKey", 3), ("fifthKey", 4))

class FieldBits(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("firstField", 0), ("secondField", 1), ("thirdField", 2), ("fourthField", 3), ("fifthField", 4))

rlSnmpTestMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 89, 35, 2, 9, 9, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSnmpTestMibVersion.setStatus('current')
rlSetsTestTable = MibTable((1, 3, 6, 1, 4, 1, 89, 35, 2, 9, 9, 2), )
if mibBuilder.loadTexts: rlSetsTestTable.setStatus('current')
rlSetsTestEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 35, 2, 9, 9, 2, 1), ).setIndexNames((0, "SNMP-TEST-MIB", "rlSetsEntryBitsKey"), (0, "SNMP-TEST-MIB", "rlSetsEntryPortListKey"))
if mibBuilder.loadTexts: rlSetsTestEntry.setStatus('current')
rlSetsEntryBitsKey = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 35, 2, 9, 9, 2, 1, 1), KeyBits().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 4))).clone(namedValues=NamedValues(("firstKey", 0), ("secondKey", 1), ("thirdKey", 2), ("fifthKey", 4))))
if mibBuilder.loadTexts: rlSetsEntryBitsKey.setStatus('current')
rlSetsEntryPortListKey = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 35, 2, 9, 9, 2, 1, 2), PortList())
if mibBuilder.loadTexts: rlSetsEntryPortListKey.setStatus('current')
rlSetsEntryBitsField = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 35, 2, 9, 9, 2, 1, 3), FieldBits().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 4))).clone(namedValues=NamedValues(("firstField", 0), ("secondField", 1), ("thirdField", 2), ("fifthField", 4)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlSetsEntryBitsField.setStatus('current')
rlSetsEntryPortListField = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 35, 2, 9, 9, 2, 1, 4), PortList()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlSetsEntryPortListField.setStatus('current')
rlSetsEntryCounter64Field = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 35, 2, 9, 9, 2, 1, 5), Counter64()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlSetsEntryCounter64Field.setStatus('current')
mibBuilder.exportSymbols("SNMP-TEST-MIB", KeyBits=KeyBits, rlSetsEntryCounter64Field=rlSetsEntryCounter64Field, rlSetsTestEntry=rlSetsTestEntry, rlSetsEntryPortListField=rlSetsEntryPortListField, rlSetsTestTable=rlSetsTestTable, FieldBits=FieldBits, rlSetsEntryPortListKey=rlSetsEntryPortListKey, rlSnmpTestMibVersion=rlSnmpTestMibVersion, rlSetsEntryBitsKey=rlSetsEntryBitsKey, rlSetsEntryBitsField=rlSetsEntryBitsField)
