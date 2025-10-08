#
# PySNMP MIB module INFINERA-PM-OPSM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/infinera/INFINERA-PM-OPSM-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:20:58 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
perfMon, = mibBuilder.importSymbols("INFINERA-REG-MIB", "perfMon")
FloatHundredths, InfnSampleDuration = mibBuilder.importSymbols("INFINERA-TC-MIB", "FloatHundredths", "InfnSampleDuration")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
opsmPmMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 50))
opsmPmMIB.setRevisions(('2015-05-18 00:00',))
if mibBuilder.loadTexts: opsmPmMIB.setLastUpdated('201505180000Z')
if mibBuilder.loadTexts: opsmPmMIB.setOrganization('Infinera')
opsmPmTable = MibTable((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 50, 2), )
if mibBuilder.loadTexts: opsmPmTable.setStatus('current')
opsmPmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 50, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "INFINERA-PM-OPSM-MIB", "opsmPmSampleDuration"), (0, "INFINERA-PM-OPSM-MIB", "opsmPmTimestamp"))
if mibBuilder.loadTexts: opsmPmEntry.setStatus('current')
opsmPmTimestamp = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 50, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: opsmPmTimestamp.setStatus('current')
opsmPmSampleDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 50, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("fifteenMinutes", 1), ("day", 2))))
if mibBuilder.loadTexts: opsmPmSampleDuration.setStatus('current')
opsmPmValidity = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 50, 2, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: opsmPmValidity.setStatus('current')
opsmPmOprMin = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 50, 2, 1, 4), FloatHundredths()).setMaxAccess("readonly")
if mibBuilder.loadTexts: opsmPmOprMin.setStatus('current')
opsmPmOprMax = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 50, 2, 1, 5), FloatHundredths()).setMaxAccess("readonly")
if mibBuilder.loadTexts: opsmPmOprMax.setStatus('current')
opsmPmOprAve = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 50, 2, 1, 6), FloatHundredths()).setMaxAccess("readonly")
if mibBuilder.loadTexts: opsmPmOprAve.setStatus('current')
opsmPmRealTable = MibTable((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 50, 1), )
if mibBuilder.loadTexts: opsmPmRealTable.setStatus('current')
opsmPmRealEntry = MibTableRow((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 50, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: opsmPmRealEntry.setStatus('current')
opsmPmRealOpr = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 50, 1, 1, 1), FloatHundredths()).setMaxAccess("readonly")
if mibBuilder.loadTexts: opsmPmRealOpr.setStatus('current')
opsmPmConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 50, 3))
opsmPmCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 50, 3, 1))
opsmPmGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 50, 3, 2))
opsmPmCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 50, 3, 1, 1)).setObjects(("INFINERA-PM-OPSM-MIB", "opsmPmGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    opsmPmCompliance = opsmPmCompliance.setStatus('current')
opsmPmRealCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 50, 3, 1, 2)).setObjects(("INFINERA-PM-OPSM-MIB", "opsmPmRealGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    opsmPmRealCompliance = opsmPmRealCompliance.setStatus('current')
opsmPmGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 50, 3, 2, 1)).setObjects(("INFINERA-PM-OPSM-MIB", "opsmPmTimestamp"), ("INFINERA-PM-OPSM-MIB", "opsmPmSampleDuration"), ("INFINERA-PM-OPSM-MIB", "opsmPmValidity"), ("INFINERA-PM-OPSM-MIB", "opsmPmOprMin"), ("INFINERA-PM-OPSM-MIB", "opsmPmOprMax"), ("INFINERA-PM-OPSM-MIB", "opsmPmOprAve"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    opsmPmGroup = opsmPmGroup.setStatus('current')
opsmPmRealGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 50, 3, 2, 2)).setObjects(("INFINERA-PM-OPSM-MIB", "opsmPmRealOpr"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    opsmPmRealGroup = opsmPmRealGroup.setStatus('current')
mibBuilder.exportSymbols("INFINERA-PM-OPSM-MIB", opsmPmTimestamp=opsmPmTimestamp, opsmPmRealOpr=opsmPmRealOpr, opsmPmCompliances=opsmPmCompliances, opsmPmGroups=opsmPmGroups, opsmPmRealTable=opsmPmRealTable, opsmPmConformance=opsmPmConformance, opsmPmEntry=opsmPmEntry, opsmPmOprMin=opsmPmOprMin, opsmPmValidity=opsmPmValidity, opsmPmRealGroup=opsmPmRealGroup, opsmPmOprAve=opsmPmOprAve, opsmPmGroup=opsmPmGroup, opsmPmOprMax=opsmPmOprMax, PYSNMP_MODULE_ID=opsmPmMIB, opsmPmTable=opsmPmTable, opsmPmRealCompliance=opsmPmRealCompliance, opsmPmCompliance=opsmPmCompliance, opsmPmRealEntry=opsmPmRealEntry, opsmPmSampleDuration=opsmPmSampleDuration, opsmPmMIB=opsmPmMIB)
