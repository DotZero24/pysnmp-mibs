#
# PySNMP MIB module EXTREME-ENTITY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/extreme/EXTREME-ENTITY-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:58:53 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
extremeAgent, = mibBuilder.importSymbols("EXTREME-BASE-MIB", "extremeAgent")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("EXTREME-ENTITY-MIB", extremeEntityFRUOdometerUnit=extremeEntityFRUOdometerUnit, extremeEntityFRUTable=extremeEntityFRUTable, PYSNMP_MODULE_ID=extremeEntity, extremeEntity=extremeEntity, extremeEntityFRUEntry=extremeEntityFRUEntry, extremeEntityFRUStartTime=extremeEntityFRUStartTime, extremeEntityFRUOdometer=extremeEntityFRUOdometer)
