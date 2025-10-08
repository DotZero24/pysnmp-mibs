#
# PySNMP MIB module INFINERA-TP-OLDPSCH-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/infinera/INFINERA-TP-OLDPSCH-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:21:18 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
terminationPoint, = mibBuilder.importSymbols("INFINERA-REG-MIB", "terminationPoint")
InfnMonitoringMode, InfnTimReptMode = mibBuilder.importSymbols("INFINERA-TC-MIB", "InfnMonitoringMode", "InfnTimReptMode")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("INFINERA-TP-OLDPSCH-MIB", oldpSchGroups=oldpSchGroups, oldpSchCompliances=oldpSchCompliances, expectedSAPI=expectedSAPI, recievedTTI=recievedTTI, oldpSchConformance=oldpSchConformance, oldpSchTable=oldpSchTable, oldpSchMIB=oldpSchMIB, timDetMode=timDetMode, oldpSchEntry=oldpSchEntry, oldpSchGroup=oldpSchGroup, oldpSchCompliance=oldpSchCompliance, PYSNMP_MODULE_ID=oldpSchMIB, expectedDAPI=expectedDAPI, monitoringMode=monitoringMode, transmitTTI=transmitTTI)
