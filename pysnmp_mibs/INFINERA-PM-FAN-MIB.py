#
# PySNMP MIB module INFINERA-PM-FAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/infinera/INFINERA-PM-FAN-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:20:16 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
commonPerfMon, = mibBuilder.importSymbols("INFINERA-REG-MIB", "commonPerfMon")
FloatTenths, = mibBuilder.importSymbols("INFINERA-TC-MIB", "FloatTenths")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("INFINERA-PM-FAN-MIB", fanPmCompliance=fanPmCompliance, fanPmRealGroup=fanPmRealGroup, fanPmConformance=fanPmConformance, fanPmRealInRpmRaw=fanPmRealInRpmRaw, fanPmInRpmAvg=fanPmInRpmAvg, fanPmInRpmMax=fanPmInRpmMax, fanPmTimestamp=fanPmTimestamp, PYSNMP_MODULE_ID=fanPmMIB, fanPmRealEntry=fanPmRealEntry, fanPmCompliances=fanPmCompliances, fanPmEntry=fanPmEntry, fanPmValidity=fanPmValidity, fanPmInRpmMin=fanPmInRpmMin, fanPmRealCompliance=fanPmRealCompliance, fanPmRealTable=fanPmRealTable, fanPmTable=fanPmTable, fanPmGroup=fanPmGroup, fanPmGroups=fanPmGroups, fanPmSampleDuration=fanPmSampleDuration, fanPmMIB=fanPmMIB)
