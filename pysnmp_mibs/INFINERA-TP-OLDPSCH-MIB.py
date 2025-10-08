#
# PySNMP MIB module INFINERA-TP-OLDPSCH-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/infinera/INFINERA-TP-OLDPSCH-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:09:55 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
terminationPoint, = mibBuilder.importSymbols("INFINERA-REG-MIB", "terminationPoint")
InfnTimReptMode, InfnMonitoringMode = mibBuilder.importSymbols("INFINERA-TC-MIB", "InfnTimReptMode", "InfnMonitoringMode")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
oldpSchMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 58))
oldpSchMIB.setRevisions(('2016-08-29 00:00',))
if mibBuilder.loadTexts: oldpSchMIB.setLastUpdated('201608290000Z')
if mibBuilder.loadTexts: oldpSchMIB.setOrganization('Infinera')
oldpSchTable = MibTable((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 58, 1), )
if mibBuilder.loadTexts: oldpSchTable.setStatus('current')
oldpSchEntry = MibTableRow((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 58, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: oldpSchEntry.setStatus('current')
transmitTTI = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 58, 1, 1, 1), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: transmitTTI.setStatus('current')
recievedTTI = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 58, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: recievedTTI.setStatus('current')
expectedSAPI = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 58, 1, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: expectedSAPI.setStatus('current')
expectedDAPI = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 58, 1, 1, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: expectedDAPI.setStatus('current')
timDetMode = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 58, 1, 1, 5), InfnTimReptMode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: timDetMode.setStatus('current')
monitoringMode = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 58, 1, 1, 6), InfnMonitoringMode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: monitoringMode.setStatus('current')
oldpSchConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 58, 3))
oldpSchCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 58, 3, 1))
oldpSchGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 58, 3, 2))
oldpSchCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 58, 3, 1, 1)).setObjects(("INFINERA-TP-OLDPSCH-MIB", "oldpSchGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    oldpSchCompliance = oldpSchCompliance.setStatus('current')
oldpSchGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 58, 3, 2, 1)).setObjects(("INFINERA-TP-OLDPSCH-MIB", "transmitTTI"), ("INFINERA-TP-OLDPSCH-MIB", "recievedTTI"), ("INFINERA-TP-OLDPSCH-MIB", "expectedSAPI"), ("INFINERA-TP-OLDPSCH-MIB", "expectedDAPI"), ("INFINERA-TP-OLDPSCH-MIB", "timDetMode"), ("INFINERA-TP-OLDPSCH-MIB", "monitoringMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    oldpSchGroup = oldpSchGroup.setStatus('current')
mibBuilder.exportSymbols("INFINERA-TP-OLDPSCH-MIB", oldpSchGroup=oldpSchGroup, monitoringMode=monitoringMode, recievedTTI=recievedTTI, oldpSchEntry=oldpSchEntry, oldpSchTable=oldpSchTable, oldpSchGroups=oldpSchGroups, oldpSchCompliance=oldpSchCompliance, timDetMode=timDetMode, oldpSchConformance=oldpSchConformance, oldpSchCompliances=oldpSchCompliances, PYSNMP_MODULE_ID=oldpSchMIB, oldpSchMIB=oldpSchMIB, expectedSAPI=expectedSAPI, expectedDAPI=expectedDAPI, transmitTTI=transmitTTI)
