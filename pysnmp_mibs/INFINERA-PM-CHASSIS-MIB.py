#
# PySNMP MIB module INFINERA-PM-CHASSIS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/infinera/INFINERA-PM-CHASSIS-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:10:01 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
perfMon, = mibBuilder.importSymbols("INFINERA-REG-MIB", "perfMon")
FloatHundredths, InfnSampleDuration = mibBuilder.importSymbols("INFINERA-TC-MIB", "FloatHundredths", "InfnSampleDuration")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
chassisPmMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 51))
chassisPmMIB.setRevisions(('2015-05-18 00:00',))
if mibBuilder.loadTexts: chassisPmMIB.setLastUpdated('201505180000Z')
if mibBuilder.loadTexts: chassisPmMIB.setOrganization('Infinera')
chassisPmTable = MibTable((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 51, 2), )
if mibBuilder.loadTexts: chassisPmTable.setStatus('current')
chassisPmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 51, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "INFINERA-PM-CHASSIS-MIB", "chassisPmSampleDuration"), (0, "INFINERA-PM-CHASSIS-MIB", "chassisPmTimestamp"))
if mibBuilder.loadTexts: chassisPmEntry.setStatus('current')
chassisPmTimestamp = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 51, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: chassisPmTimestamp.setStatus('current')
chassisPmSampleDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 51, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("fifteenMinutes", 1), ("day", 2))))
if mibBuilder.loadTexts: chassisPmSampleDuration.setStatus('current')
chassisPmValidity = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 51, 2, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassisPmValidity.setStatus('current')
chassisPmInPMin = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 51, 2, 1, 4), FloatHundredths()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassisPmInPMin.setStatus('current')
chassisPmInPMax = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 51, 2, 1, 5), FloatHundredths()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassisPmInPMax.setStatus('current')
chassisPmInPAvg = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 51, 2, 1, 6), FloatHundredths()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassisPmInPAvg.setStatus('current')
chassisPmRealTable = MibTable((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 51, 1), )
if mibBuilder.loadTexts: chassisPmRealTable.setStatus('current')
chassisPmRealEntry = MibTableRow((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 51, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: chassisPmRealEntry.setStatus('current')
chassisPmRealInPRaw = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 51, 1, 1, 1), FloatHundredths()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassisPmRealInPRaw.setStatus('current')
chassisPmConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 51, 3))
chassisPmCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 51, 3, 1))
chassisPmGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 51, 3, 2))
chassisPmCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 51, 3, 1, 1)).setObjects(("INFINERA-PM-CHASSIS-MIB", "chassisPmGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    chassisPmCompliance = chassisPmCompliance.setStatus('current')
chassisPmRealCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 51, 3, 1, 2)).setObjects(("INFINERA-PM-CHASSIS-MIB", "chassisPmRealGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    chassisPmRealCompliance = chassisPmRealCompliance.setStatus('current')
chassisPmGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 51, 3, 2, 1)).setObjects(("INFINERA-PM-CHASSIS-MIB", "chassisPmTimestamp"), ("INFINERA-PM-CHASSIS-MIB", "chassisPmSampleDuration"), ("INFINERA-PM-CHASSIS-MIB", "chassisPmValidity"), ("INFINERA-PM-CHASSIS-MIB", "chassisPmInPMin"), ("INFINERA-PM-CHASSIS-MIB", "chassisPmInPMax"), ("INFINERA-PM-CHASSIS-MIB", "chassisPmInPAvg"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    chassisPmGroup = chassisPmGroup.setStatus('current')
chassisPmRealGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 51, 3, 2, 2)).setObjects(("INFINERA-PM-CHASSIS-MIB", "chassisPmRealInPRaw"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    chassisPmRealGroup = chassisPmRealGroup.setStatus('current')
mibBuilder.exportSymbols("INFINERA-PM-CHASSIS-MIB", chassisPmRealEntry=chassisPmRealEntry, chassisPmMIB=chassisPmMIB, chassisPmInPAvg=chassisPmInPAvg, chassisPmRealGroup=chassisPmRealGroup, chassisPmRealCompliance=chassisPmRealCompliance, chassisPmRealTable=chassisPmRealTable, chassisPmConformance=chassisPmConformance, chassisPmSampleDuration=chassisPmSampleDuration, chassisPmTable=chassisPmTable, PYSNMP_MODULE_ID=chassisPmMIB, chassisPmGroups=chassisPmGroups, chassisPmInPMin=chassisPmInPMin, chassisPmInPMax=chassisPmInPMax, chassisPmGroup=chassisPmGroup, chassisPmRealInPRaw=chassisPmRealInPRaw, chassisPmCompliances=chassisPmCompliances, chassisPmCompliance=chassisPmCompliance, chassisPmTimestamp=chassisPmTimestamp, chassisPmValidity=chassisPmValidity, chassisPmEntry=chassisPmEntry)
