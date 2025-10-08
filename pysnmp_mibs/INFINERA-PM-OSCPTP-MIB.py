#
# PySNMP MIB module INFINERA-PM-OSCPTP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/infinera/INFINERA-PM-OSCPTP-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:09:33 2025
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
ModuleIdentity, Integer32, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Counter64, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Integer32", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Counter64", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
oscPtpPmMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 34))
oscPtpPmMIB.setRevisions(('2012-10-20 00:00',))
if mibBuilder.loadTexts: oscPtpPmMIB.setLastUpdated('201210200000Z')
if mibBuilder.loadTexts: oscPtpPmMIB.setOrganization('Infinera')
oscPtpPmTable = MibTable((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 34, 2), )
if mibBuilder.loadTexts: oscPtpPmTable.setStatus('current')
oscPtpPmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 34, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "INFINERA-PM-OSCPTP-MIB", "oscPtpPmSampleDuration"), (0, "INFINERA-PM-OSCPTP-MIB", "oscPtpPmTimestamp"))
if mibBuilder.loadTexts: oscPtpPmEntry.setStatus('current')
oscPtpPmTimestamp = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 34, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: oscPtpPmTimestamp.setStatus('current')
oscPtpPmSampleDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 34, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("fifteenMinutes", 1), ("day", 2))))
if mibBuilder.loadTexts: oscPtpPmSampleDuration.setStatus('current')
oscPtpPmOscOPRMin = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 34, 2, 1, 3), FloatHundredths()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oscPtpPmOscOPRMin.setStatus('current')
oscPtpPmOscOPRMax = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 34, 2, 1, 4), FloatHundredths()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oscPtpPmOscOPRMax.setStatus('current')
oscPtpPmOscOPRAve = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 34, 2, 1, 5), FloatHundredths()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oscPtpPmOscOPRAve.setStatus('current')
oscPtpPmRealTable = MibTable((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 34, 1), )
if mibBuilder.loadTexts: oscPtpPmRealTable.setStatus('current')
oscPtpPmRealEntry = MibTableRow((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 34, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: oscPtpPmRealEntry.setStatus('current')
oscPtpPmRealOscOPR = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 34, 1, 1, 1), FloatHundredths()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oscPtpPmRealOscOPR.setStatus('current')
oscPtpPmConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 34, 3))
oscPtpPmCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 34, 3, 1))
oscPtpPmGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 34, 3, 2))
oscPtpPmCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 34, 3, 1, 1)).setObjects(("INFINERA-PM-OSCPTP-MIB", "oscPtpPmGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    oscPtpPmCompliance = oscPtpPmCompliance.setStatus('current')
oscPtpPmRealCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 34, 3, 1, 2)).setObjects(("INFINERA-PM-OSCPTP-MIB", "oscPtpPmRealGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    oscPtpPmRealCompliance = oscPtpPmRealCompliance.setStatus('current')
oscPtpPmGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 34, 3, 2, 1)).setObjects(("INFINERA-PM-OSCPTP-MIB", "oscPtpPmOscOPRMin"), ("INFINERA-PM-OSCPTP-MIB", "oscPtpPmOscOPRMax"), ("INFINERA-PM-OSCPTP-MIB", "oscPtpPmOscOPRAve"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    oscPtpPmGroup = oscPtpPmGroup.setStatus('current')
oscPtpPmRealGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 34, 3, 2, 2)).setObjects(("INFINERA-PM-OSCPTP-MIB", "oscPtpPmRealOscOPR"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    oscPtpPmRealGroup = oscPtpPmRealGroup.setStatus('current')
mibBuilder.exportSymbols("INFINERA-PM-OSCPTP-MIB", oscPtpPmOscOPRAve=oscPtpPmOscOPRAve, oscPtpPmRealCompliance=oscPtpPmRealCompliance, oscPtpPmGroup=oscPtpPmGroup, oscPtpPmOscOPRMin=oscPtpPmOscOPRMin, oscPtpPmTimestamp=oscPtpPmTimestamp, oscPtpPmCompliances=oscPtpPmCompliances, PYSNMP_MODULE_ID=oscPtpPmMIB, oscPtpPmRealOscOPR=oscPtpPmRealOscOPR, oscPtpPmTable=oscPtpPmTable, oscPtpPmGroups=oscPtpPmGroups, oscPtpPmRealEntry=oscPtpPmRealEntry, oscPtpPmMIB=oscPtpPmMIB, oscPtpPmOscOPRMax=oscPtpPmOscOPRMax, oscPtpPmRealTable=oscPtpPmRealTable, oscPtpPmRealGroup=oscPtpPmRealGroup, oscPtpPmConformance=oscPtpPmConformance, oscPtpPmCompliance=oscPtpPmCompliance, oscPtpPmEntry=oscPtpPmEntry, oscPtpPmSampleDuration=oscPtpPmSampleDuration)
