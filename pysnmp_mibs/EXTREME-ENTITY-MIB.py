#
# PySNMP MIB module EXTREME-ENTITY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/extreme/EXTREME-ENTITY-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:01:58 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
extremeAgent, = mibBuilder.importSymbols("EXTREME-BASE-MIB", "extremeAgent")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
extremeEntity = ModuleIdentity((1, 3, 6, 1, 4, 1, 1916, 1, 31))
if mibBuilder.loadTexts: extremeEntity.setLastUpdated('200502140000Z')
if mibBuilder.loadTexts: extremeEntity.setOrganization('Extreme Networks, Inc.')
extremeEntityFRUTable = MibTable((1, 3, 6, 1, 4, 1, 1916, 1, 31, 1), )
if mibBuilder.loadTexts: extremeEntityFRUTable.setStatus('current')
extremeEntityFRUEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1916, 1, 31, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: extremeEntityFRUEntry.setStatus('current')
extremeEntityFRUStartTime = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 31, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeEntityFRUStartTime.setStatus('current')
extremeEntityFRUOdometer = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 31, 1, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeEntityFRUOdometer.setStatus('current')
extremeEntityFRUOdometerUnit = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 31, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("days", 1), ("seconds", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeEntityFRUOdometerUnit.setStatus('current')
mibBuilder.exportSymbols("EXTREME-ENTITY-MIB", extremeEntityFRUTable=extremeEntityFRUTable, extremeEntityFRUOdometerUnit=extremeEntityFRUOdometerUnit, extremeEntityFRUEntry=extremeEntityFRUEntry, PYSNMP_MODULE_ID=extremeEntity, extremeEntityFRUOdometer=extremeEntityFRUOdometer, extremeEntity=extremeEntity, extremeEntityFRUStartTime=extremeEntityFRUStartTime)
