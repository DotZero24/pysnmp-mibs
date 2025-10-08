#
# PySNMP MIB module INFINERA-PM-FAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/infinera/INFINERA-PM-FAN-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:09:21 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
commonPerfMon, = mibBuilder.importSymbols("INFINERA-REG-MIB", "commonPerfMon")
FloatTenths, = mibBuilder.importSymbols("INFINERA-TC-MIB", "FloatTenths")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
fanPmMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 4))
fanPmMIB.setRevisions(('2015-02-06 00:00',))
if mibBuilder.loadTexts: fanPmMIB.setLastUpdated('201502060000Z')
if mibBuilder.loadTexts: fanPmMIB.setOrganization('Infinera')
fanPmRealTable = MibTable((1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 4, 1), )
if mibBuilder.loadTexts: fanPmRealTable.setStatus('current')
fanPmRealEntry = MibTableRow((1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 4, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: fanPmRealEntry.setStatus('current')
fanPmRealInRpmRaw = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 4, 1, 1, 1), FloatTenths()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fanPmRealInRpmRaw.setStatus('current')
fanPmTable = MibTable((1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 4, 2), )
if mibBuilder.loadTexts: fanPmTable.setStatus('current')
fanPmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 4, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "INFINERA-PM-FAN-MIB", "fanPmSampleDuration"), (0, "INFINERA-PM-FAN-MIB", "fanPmTimestamp"))
if mibBuilder.loadTexts: fanPmEntry.setStatus('current')
fanPmTimestamp = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 4, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: fanPmTimestamp.setStatus('current')
fanPmSampleDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 4, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("fifteenMinutes", 1), ("day", 2))))
if mibBuilder.loadTexts: fanPmSampleDuration.setStatus('current')
fanPmValidity = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 4, 2, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fanPmValidity.setStatus('current')
fanPmInRpmMin = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 4, 2, 1, 4), FloatTenths()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fanPmInRpmMin.setStatus('current')
fanPmInRpmMax = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 4, 2, 1, 5), FloatTenths()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fanPmInRpmMax.setStatus('current')
fanPmInRpmAvg = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 4, 2, 1, 6), FloatTenths()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fanPmInRpmAvg.setStatus('current')
fanPmConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 4, 3))
fanPmCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 4, 3, 1))
fanPmGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 4, 3, 2))
fanPmCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 4, 3, 1, 1)).setObjects(("INFINERA-PM-FAN-MIB", "fanPmRealGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fanPmCompliance = fanPmCompliance.setStatus('current')
fanPmRealCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 4, 3, 1, 2)).setObjects(("INFINERA-PM-FAN-MIB", "fanPmRealGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fanPmRealCompliance = fanPmRealCompliance.setStatus('current')
fanPmGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 4, 3, 2, 1)).setObjects(("INFINERA-PM-FAN-MIB", "fanPmValidity"), ("INFINERA-PM-FAN-MIB", "fanPmInRpmMin"), ("INFINERA-PM-FAN-MIB", "fanPmInRpmMax"), ("INFINERA-PM-FAN-MIB", "fanPmInRpmAvg"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fanPmGroup = fanPmGroup.setStatus('current')
fanPmRealGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 4, 3, 2, 2)).setObjects(("INFINERA-PM-FAN-MIB", "fanPmRealInRpmRaw"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fanPmRealGroup = fanPmRealGroup.setStatus('current')
mibBuilder.exportSymbols("INFINERA-PM-FAN-MIB", fanPmRealCompliance=fanPmRealCompliance, fanPmInRpmMin=fanPmInRpmMin, fanPmInRpmAvg=fanPmInRpmAvg, fanPmConformance=fanPmConformance, fanPmTable=fanPmTable, fanPmGroup=fanPmGroup, PYSNMP_MODULE_ID=fanPmMIB, fanPmCompliance=fanPmCompliance, fanPmRealGroup=fanPmRealGroup, fanPmValidity=fanPmValidity, fanPmTimestamp=fanPmTimestamp, fanPmSampleDuration=fanPmSampleDuration, fanPmInRpmMax=fanPmInRpmMax, fanPmEntry=fanPmEntry, fanPmRealTable=fanPmRealTable, fanPmRealInRpmRaw=fanPmRealInRpmRaw, fanPmCompliances=fanPmCompliances, fanPmMIB=fanPmMIB, fanPmRealEntry=fanPmRealEntry, fanPmGroups=fanPmGroups)
