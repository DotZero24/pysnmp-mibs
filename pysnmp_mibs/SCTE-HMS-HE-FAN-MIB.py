#
# PySNMP MIB module SCTE-HMS-HE-FAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/scte/SCTE-HMS-HE-FAN-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:00:51 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
HeFaultStatus, heFans, HeMilliAmp = mibBuilder.importSymbols("SCTE-HMS-HEADENDIDENT-MIB", "HeFaultStatus", "heFans", "HeMilliAmp")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("SCTE-HMS-HE-FAN-MIB", heFanModuleMIB=heFanModuleMIB, heFanStatusAlarm=heFanStatusAlarm, heFanCompliance=heFanCompliance, heFanUnitEntry=heFanUnitEntry, heFanStatusCurrent=heFanStatusCurrent, heFanUnitAlarm=heFanUnitAlarm, heFanMIBObjects=heFanMIBObjects, heFanMIBConformance=heFanMIBConformance, heFanUnitMandatoryGroup=heFanUnitMandatoryGroup, heFanStatusTable=heFanStatusTable, heFanStatusEntry=heFanStatusEntry, heFanStatusIndex=heFanStatusIndex, PYSNMP_MODULE_ID=heFanModuleMIB, heFanMIBCompliances=heFanMIBCompliances, heFanUnitTable=heFanUnitTable, heFanStatusGroup=heFanStatusGroup, heFanMIBGroups=heFanMIBGroups)
