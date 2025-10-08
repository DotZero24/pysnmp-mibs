#
# PySNMP MIB module SCTE-HMS-HE-FAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/scte/SCTE-HMS-HE-FAN-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:35:38 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
heFans, HeFaultStatus, HeMilliAmp = mibBuilder.importSymbols("SCTE-HMS-HEADENDIDENT-MIB", "heFans", "HeFaultStatus", "HeMilliAmp")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
heFanModuleMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 5591, 1, 11, 2, 3, 1))
if mibBuilder.loadTexts: heFanModuleMIB.setLastUpdated('200403250410Z')
if mibBuilder.loadTexts: heFanModuleMIB.setOrganization('SCTE HMS Working Group')
heFanMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 5591, 1, 11, 2, 3, 1, 1))
heFanMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 5591, 1, 11, 2, 3, 1, 2))
heFanMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 5591, 1, 11, 2, 3, 1, 2, 1))
heFanMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 5591, 1, 11, 2, 3, 1, 2, 2))
heFanUnitTable = MibTable((1, 3, 6, 1, 4, 1, 5591, 1, 11, 2, 3, 1, 1, 1), )
if mibBuilder.loadTexts: heFanUnitTable.setStatus('current')
heFanUnitEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5591, 1, 11, 2, 3, 1, 1, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: heFanUnitEntry.setStatus('current')
heFanUnitAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 11, 2, 3, 1, 1, 1, 1, 1), HeFaultStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: heFanUnitAlarm.setStatus('current')
heFanStatusTable = MibTable((1, 3, 6, 1, 4, 1, 5591, 1, 11, 2, 3, 1, 1, 2), )
if mibBuilder.loadTexts: heFanStatusTable.setStatus('current')
heFanStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5591, 1, 11, 2, 3, 1, 1, 2, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"), (0, "SCTE-HMS-HE-FAN-MIB", "heFanStatusIndex"))
if mibBuilder.loadTexts: heFanStatusEntry.setStatus('current')
heFanStatusIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 11, 2, 3, 1, 1, 2, 1, 1), Unsigned32())
if mibBuilder.loadTexts: heFanStatusIndex.setStatus('current')
heFanStatusCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 11, 2, 3, 1, 1, 2, 1, 2), HeMilliAmp()).setUnits('milliamperes').setMaxAccess("readonly")
if mibBuilder.loadTexts: heFanStatusCurrent.setStatus('current')
heFanStatusAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 11, 2, 3, 1, 1, 2, 1, 3), HeFaultStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: heFanStatusAlarm.setStatus('current')
heFanCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 5591, 1, 11, 2, 3, 1, 2, 1, 1)).setObjects(("SCTE-HMS-HE-FAN-MIB", "heFanUnitMandatoryGroup"), ("SCTE-HMS-HE-FAN-MIB", "heFanStatusGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    heFanCompliance = heFanCompliance.setStatus('current')
heFanUnitMandatoryGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5591, 1, 11, 2, 3, 1, 2, 2, 1)).setObjects(("SCTE-HMS-HE-FAN-MIB", "heFanUnitAlarm"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    heFanUnitMandatoryGroup = heFanUnitMandatoryGroup.setStatus('current')
heFanStatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5591, 1, 11, 2, 3, 1, 2, 2, 2)).setObjects(("SCTE-HMS-HE-FAN-MIB", "heFanStatusAlarm"), ("SCTE-HMS-HE-FAN-MIB", "heFanStatusCurrent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    heFanStatusGroup = heFanStatusGroup.setStatus('current')
mibBuilder.exportSymbols("SCTE-HMS-HE-FAN-MIB", heFanMIBGroups=heFanMIBGroups, heFanStatusIndex=heFanStatusIndex, heFanMIBConformance=heFanMIBConformance, heFanUnitAlarm=heFanUnitAlarm, heFanStatusTable=heFanStatusTable, heFanModuleMIB=heFanModuleMIB, heFanUnitMandatoryGroup=heFanUnitMandatoryGroup, heFanMIBCompliances=heFanMIBCompliances, PYSNMP_MODULE_ID=heFanModuleMIB, heFanStatusCurrent=heFanStatusCurrent, heFanCompliance=heFanCompliance, heFanUnitTable=heFanUnitTable, heFanUnitEntry=heFanUnitEntry, heFanMIBObjects=heFanMIBObjects, heFanStatusAlarm=heFanStatusAlarm, heFanStatusGroup=heFanStatusGroup, heFanStatusEntry=heFanStatusEntry)
