#
# PySNMP MIB module SNMP-TEST-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/radlan/SNMP-TEST-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:40:50 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
rlSnmpTestSimulatedVariables, = mibBuilder.importSymbols("RADLAN-rndApplications", "rlSnmpTestSimulatedVariables")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
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
mibBuilder.exportSymbols("SNMP-TEST-MIB", FieldBits=FieldBits, KeyBits=KeyBits, rlSetsEntryCounter64Field=rlSetsEntryCounter64Field, rlSetsEntryBitsKey=rlSetsEntryBitsKey, rlSetsTestEntry=rlSetsTestEntry, rlSnmpTestMibVersion=rlSnmpTestMibVersion, rlSetsEntryBitsField=rlSetsEntryBitsField, rlSetsTestTable=rlSetsTestTable, rlSetsEntryPortListKey=rlSetsEntryPortListKey, rlSetsEntryPortListField=rlSetsEntryPortListField)
