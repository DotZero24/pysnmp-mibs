#
# PySNMP MIB module INFINERA-PM-BASESCGPTP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/infinera/INFINERA-PM-BASESCGPTP-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:20:42 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
perfMon, = mibBuilder.importSymbols("INFINERA-REG-MIB", "perfMon")
FloatHundredths, = mibBuilder.importSymbols("INFINERA-TC-MIB", "FloatHundredths")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
baseScgPtpPmMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 45))
baseScgPtpPmMIB.setRevisions(('2013-10-08 00:00',))
if mibBuilder.loadTexts: baseScgPtpPmMIB.setLastUpdated('201310080000Z')
if mibBuilder.loadTexts: baseScgPtpPmMIB.setOrganization('Infinera')
baseScgPtpPmTable = MibTable((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 45, 2), )
if mibBuilder.loadTexts: baseScgPtpPmTable.setStatus('current')
baseScgPtpPmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 45, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: baseScgPtpPmEntry.setStatus('current')
baseScgPtpPmValidity = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 45, 2, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: baseScgPtpPmValidity.setStatus('current')
baseScgPtpPmCmnScgOptMin = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 45, 2, 1, 4), FloatHundredths()).setMaxAccess("readonly")
if mibBuilder.loadTexts: baseScgPtpPmCmnScgOptMin.setStatus('current')
baseScgPtpPmCmnScgOptMax = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 45, 2, 1, 5), FloatHundredths()).setMaxAccess("readonly")
if mibBuilder.loadTexts: baseScgPtpPmCmnScgOptMax.setStatus('current')
baseScgPtpPmCmnScgOptAve = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 45, 2, 1, 6), FloatHundredths()).setMaxAccess("readonly")
if mibBuilder.loadTexts: baseScgPtpPmCmnScgOptAve.setStatus('current')
baseScgPtpPmCmnScgOprMin = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 45, 2, 1, 7), FloatHundredths()).setMaxAccess("readonly")
if mibBuilder.loadTexts: baseScgPtpPmCmnScgOprMin.setStatus('current')
baseScgPtpPmCmnScgOprMax = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 45, 2, 1, 8), FloatHundredths()).setMaxAccess("readonly")
if mibBuilder.loadTexts: baseScgPtpPmCmnScgOprMax.setStatus('current')
baseScgPtpPmCmnScgOprAve = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 45, 2, 1, 9), FloatHundredths()).setMaxAccess("readonly")
if mibBuilder.loadTexts: baseScgPtpPmCmnScgOprAve.setStatus('current')
baseScgPtpPmRealTable = MibTable((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 45, 1), )
if mibBuilder.loadTexts: baseScgPtpPmRealTable.setStatus('current')
baseScgPtpPmRealEntry = MibTableRow((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 45, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: baseScgPtpPmRealEntry.setStatus('current')
baseScgPtpPmRealCmnScgOpt = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 45, 1, 1, 1), FloatHundredths()).setMaxAccess("readonly")
if mibBuilder.loadTexts: baseScgPtpPmRealCmnScgOpt.setStatus('current')
baseScgPtpPmRealCmnScgOpr = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 45, 1, 1, 2), FloatHundredths()).setMaxAccess("readonly")
if mibBuilder.loadTexts: baseScgPtpPmRealCmnScgOpr.setStatus('current')
baseScgPtpPmConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 45, 3))
baseScgPtpPmCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 45, 3, 1))
baseScgPtpPmGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 45, 3, 2))
baseScgPtpPmCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 45, 3, 1, 1)).setObjects(("INFINERA-PM-BASESCGPTP-MIB", "baseScgPtpPmGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    baseScgPtpPmCompliance = baseScgPtpPmCompliance.setStatus('current')
baseScgPtpPmRealCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 45, 3, 1, 2)).setObjects(("INFINERA-PM-BASESCGPTP-MIB", "baseScgPtpPmRealGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    baseScgPtpPmRealCompliance = baseScgPtpPmRealCompliance.setStatus('current')
baseScgPtpPmGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 45, 3, 2, 1)).setObjects(("INFINERA-PM-BASESCGPTP-MIB", "baseScgPtpPmValidity"), ("INFINERA-PM-BASESCGPTP-MIB", "baseScgPtpPmCmnScgOptMin"), ("INFINERA-PM-BASESCGPTP-MIB", "baseScgPtpPmCmnScgOptMax"), ("INFINERA-PM-BASESCGPTP-MIB", "baseScgPtpPmCmnScgOptAve"), ("INFINERA-PM-BASESCGPTP-MIB", "baseScgPtpPmCmnScgOprMin"), ("INFINERA-PM-BASESCGPTP-MIB", "baseScgPtpPmCmnScgOprMax"), ("INFINERA-PM-BASESCGPTP-MIB", "baseScgPtpPmCmnScgOprAve"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    baseScgPtpPmGroup = baseScgPtpPmGroup.setStatus('current')
baseScgPtpPmRealGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 45, 3, 2, 2)).setObjects(("INFINERA-PM-BASESCGPTP-MIB", "baseScgPtpPmRealCmnScgOpt"), ("INFINERA-PM-BASESCGPTP-MIB", "baseScgPtpPmRealCmnScgOpr"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    baseScgPtpPmRealGroup = baseScgPtpPmRealGroup.setStatus('current')
mibBuilder.exportSymbols("INFINERA-PM-BASESCGPTP-MIB", baseScgPtpPmRealGroup=baseScgPtpPmRealGroup, baseScgPtpPmCmnScgOptMin=baseScgPtpPmCmnScgOptMin, baseScgPtpPmMIB=baseScgPtpPmMIB, baseScgPtpPmRealEntry=baseScgPtpPmRealEntry, baseScgPtpPmCmnScgOprMax=baseScgPtpPmCmnScgOprMax, baseScgPtpPmCmnScgOptMax=baseScgPtpPmCmnScgOptMax, baseScgPtpPmCompliance=baseScgPtpPmCompliance, baseScgPtpPmCompliances=baseScgPtpPmCompliances, baseScgPtpPmCmnScgOprAve=baseScgPtpPmCmnScgOprAve, baseScgPtpPmTable=baseScgPtpPmTable, baseScgPtpPmRealCmnScgOpt=baseScgPtpPmRealCmnScgOpt, baseScgPtpPmRealTable=baseScgPtpPmRealTable, baseScgPtpPmCmnScgOptAve=baseScgPtpPmCmnScgOptAve, baseScgPtpPmValidity=baseScgPtpPmValidity, baseScgPtpPmGroup=baseScgPtpPmGroup, baseScgPtpPmRealCompliance=baseScgPtpPmRealCompliance, baseScgPtpPmCmnScgOprMin=baseScgPtpPmCmnScgOprMin, PYSNMP_MODULE_ID=baseScgPtpPmMIB, baseScgPtpPmEntry=baseScgPtpPmEntry, baseScgPtpPmRealCmnScgOpr=baseScgPtpPmRealCmnScgOpr, baseScgPtpPmConformance=baseScgPtpPmConformance, baseScgPtpPmGroups=baseScgPtpPmGroups)
