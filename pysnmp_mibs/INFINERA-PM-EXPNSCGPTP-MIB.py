#
# PySNMP MIB module INFINERA-PM-EXPNSCGPTP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/infinera/INFINERA-PM-EXPNSCGPTP-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:10:03 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
perfMon, = mibBuilder.importSymbols("INFINERA-REG-MIB", "perfMon")
FloatHundredths, = mibBuilder.importSymbols("INFINERA-TC-MIB", "FloatHundredths")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
expnScgPtpPmMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 48))
expnScgPtpPmMIB.setRevisions(('2013-10-08 00:00',))
if mibBuilder.loadTexts: expnScgPtpPmMIB.setLastUpdated('201310080000Z')
if mibBuilder.loadTexts: expnScgPtpPmMIB.setOrganization('Infinera')
expnScgPtpPmTable = MibTable((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 48, 2), )
if mibBuilder.loadTexts: expnScgPtpPmTable.setStatus('current')
expnScgPtpPmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 48, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: expnScgPtpPmEntry.setStatus('current')
expnScgPtpPmValidity = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 48, 2, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: expnScgPtpPmValidity.setStatus('current')
expnScgPtpPmCmnScgOptMin = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 48, 2, 1, 4), FloatHundredths()).setMaxAccess("readonly")
if mibBuilder.loadTexts: expnScgPtpPmCmnScgOptMin.setStatus('current')
expnScgPtpPmCmnScgOptMax = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 48, 2, 1, 5), FloatHundredths()).setMaxAccess("readonly")
if mibBuilder.loadTexts: expnScgPtpPmCmnScgOptMax.setStatus('current')
expnScgPtpPmCmnScgOptAve = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 48, 2, 1, 6), FloatHundredths()).setMaxAccess("readonly")
if mibBuilder.loadTexts: expnScgPtpPmCmnScgOptAve.setStatus('current')
expnScgPtpPmCmnScgOprMin = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 48, 2, 1, 7), FloatHundredths()).setMaxAccess("readonly")
if mibBuilder.loadTexts: expnScgPtpPmCmnScgOprMin.setStatus('current')
expnScgPtpPmCmnScgOprMax = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 48, 2, 1, 8), FloatHundredths()).setMaxAccess("readonly")
if mibBuilder.loadTexts: expnScgPtpPmCmnScgOprMax.setStatus('current')
expnScgPtpPmCmnScgOprAve = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 48, 2, 1, 9), FloatHundredths()).setMaxAccess("readonly")
if mibBuilder.loadTexts: expnScgPtpPmCmnScgOprAve.setStatus('current')
expnScgPtpPmRealTable = MibTable((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 48, 1), )
if mibBuilder.loadTexts: expnScgPtpPmRealTable.setStatus('current')
expnScgPtpPmRealEntry = MibTableRow((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 48, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: expnScgPtpPmRealEntry.setStatus('current')
expnScgPtpPmRealCmnScgOpt = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 48, 1, 1, 1), FloatHundredths()).setMaxAccess("readonly")
if mibBuilder.loadTexts: expnScgPtpPmRealCmnScgOpt.setStatus('current')
expnScgPtpPmRealCmnScgOpr = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 48, 1, 1, 2), FloatHundredths()).setMaxAccess("readonly")
if mibBuilder.loadTexts: expnScgPtpPmRealCmnScgOpr.setStatus('current')
expnScgPtpPmConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 48, 3))
expnScgPtpPmCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 48, 3, 1))
expnScgPtpPmGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 48, 3, 2))
expnScgPtpPmCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 48, 3, 1, 1)).setObjects(("INFINERA-PM-EXPNSCGPTP-MIB", "expnScgPtpPmGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    expnScgPtpPmCompliance = expnScgPtpPmCompliance.setStatus('current')
expnScgPtpPmRealCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 48, 3, 1, 2)).setObjects(("INFINERA-PM-EXPNSCGPTP-MIB", "expnScgPtpPmRealGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    expnScgPtpPmRealCompliance = expnScgPtpPmRealCompliance.setStatus('current')
expnScgPtpPmGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 48, 3, 2, 1)).setObjects(("INFINERA-PM-EXPNSCGPTP-MIB", "expnScgPtpPmValidity"), ("INFINERA-PM-EXPNSCGPTP-MIB", "expnScgPtpPmCmnScgOptMin"), ("INFINERA-PM-EXPNSCGPTP-MIB", "expnScgPtpPmCmnScgOptMax"), ("INFINERA-PM-EXPNSCGPTP-MIB", "expnScgPtpPmCmnScgOptAve"), ("INFINERA-PM-EXPNSCGPTP-MIB", "expnScgPtpPmCmnScgOprMin"), ("INFINERA-PM-EXPNSCGPTP-MIB", "expnScgPtpPmCmnScgOprMax"), ("INFINERA-PM-EXPNSCGPTP-MIB", "expnScgPtpPmCmnScgOprAve"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    expnScgPtpPmGroup = expnScgPtpPmGroup.setStatus('current')
expnScgPtpPmRealGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 48, 3, 2, 2)).setObjects(("INFINERA-PM-EXPNSCGPTP-MIB", "expnScgPtpPmRealCmnScgOpt"), ("INFINERA-PM-EXPNSCGPTP-MIB", "expnScgPtpPmRealCmnScgOpr"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    expnScgPtpPmRealGroup = expnScgPtpPmRealGroup.setStatus('current')
mibBuilder.exportSymbols("INFINERA-PM-EXPNSCGPTP-MIB", PYSNMP_MODULE_ID=expnScgPtpPmMIB, expnScgPtpPmCmnScgOprMin=expnScgPtpPmCmnScgOprMin, expnScgPtpPmGroup=expnScgPtpPmGroup, expnScgPtpPmMIB=expnScgPtpPmMIB, expnScgPtpPmRealCmnScgOpt=expnScgPtpPmRealCmnScgOpt, expnScgPtpPmRealCompliance=expnScgPtpPmRealCompliance, expnScgPtpPmEntry=expnScgPtpPmEntry, expnScgPtpPmRealTable=expnScgPtpPmRealTable, expnScgPtpPmRealEntry=expnScgPtpPmRealEntry, expnScgPtpPmConformance=expnScgPtpPmConformance, expnScgPtpPmCmnScgOprAve=expnScgPtpPmCmnScgOprAve, expnScgPtpPmCompliances=expnScgPtpPmCompliances, expnScgPtpPmCmnScgOptAve=expnScgPtpPmCmnScgOptAve, expnScgPtpPmCmnScgOprMax=expnScgPtpPmCmnScgOprMax, expnScgPtpPmValidity=expnScgPtpPmValidity, expnScgPtpPmTable=expnScgPtpPmTable, expnScgPtpPmRealCmnScgOpr=expnScgPtpPmRealCmnScgOpr, expnScgPtpPmRealGroup=expnScgPtpPmRealGroup, expnScgPtpPmGroups=expnScgPtpPmGroups, expnScgPtpPmCmnScgOptMin=expnScgPtpPmCmnScgOptMin, expnScgPtpPmCompliance=expnScgPtpPmCompliance, expnScgPtpPmCmnScgOptMax=expnScgPtpPmCmnScgOptMax)
