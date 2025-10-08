#
# PySNMP MIB module INFINERA-PM-OSAPTP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/infinera/INFINERA-PM-OSAPTP-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:20:43 2025
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
osaPtpPmMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 19))
osaPtpPmMIB.setRevisions(('2008-10-20 00:00',))
if mibBuilder.loadTexts: osaPtpPmMIB.setLastUpdated('200810200000Z')
if mibBuilder.loadTexts: osaPtpPmMIB.setOrganization('Infinera')
osaPtpPmTable = MibTable((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 19, 2), )
if mibBuilder.loadTexts: osaPtpPmTable.setStatus('current')
osaPtpPmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 19, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "INFINERA-PM-OSAPTP-MIB", "osaPtpPmSampleDuration"), (0, "INFINERA-PM-OSAPTP-MIB", "osaPtpPmTimestamp"))
if mibBuilder.loadTexts: osaPtpPmEntry.setStatus('current')
osaPtpPmTimestamp = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 19, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: osaPtpPmTimestamp.setStatus('current')
osaPtpPmSampleDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 19, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("fifteenMinutes", 1), ("day", 2))))
if mibBuilder.loadTexts: osaPtpPmSampleDuration.setStatus('current')
osaPtpPmValidity = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 19, 2, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: osaPtpPmValidity.setStatus('current')
osaPtpPmOprMin = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 19, 2, 1, 4), FloatHundredths()).setMaxAccess("readonly")
if mibBuilder.loadTexts: osaPtpPmOprMin.setStatus('current')
osaPtpPmOprMax = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 19, 2, 1, 5), FloatHundredths()).setMaxAccess("readonly")
if mibBuilder.loadTexts: osaPtpPmOprMax.setStatus('current')
osaPtpPmOprAve = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 19, 2, 1, 6), FloatHundredths()).setMaxAccess("readonly")
if mibBuilder.loadTexts: osaPtpPmOprAve.setStatus('current')
osaPtpPmRealTable = MibTable((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 19, 1), )
if mibBuilder.loadTexts: osaPtpPmRealTable.setStatus('current')
osaPtpPmRealEntry = MibTableRow((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 19, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: osaPtpPmRealEntry.setStatus('current')
osaPtpPmRealOpr = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 19, 1, 1, 1), FloatHundredths()).setMaxAccess("readonly")
if mibBuilder.loadTexts: osaPtpPmRealOpr.setStatus('current')
osaOprOsaTapRatio = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 19, 1, 1, 2), FloatHundredths()).setMaxAccess("readonly")
if mibBuilder.loadTexts: osaOprOsaTapRatio.setStatus('current')
osaPtpPmConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 19, 3))
osaPtpPmCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 19, 3, 1))
osaPtpPmGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 19, 3, 2))
osaPtpPmCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 19, 3, 1, 1)).setObjects(("INFINERA-PM-OSAPTP-MIB", "osaPtpPmGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    osaPtpPmCompliance = osaPtpPmCompliance.setStatus('current')
osaPtpPmRealCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 19, 3, 1, 2)).setObjects(("INFINERA-PM-OSAPTP-MIB", "osaPtpPmRealGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    osaPtpPmRealCompliance = osaPtpPmRealCompliance.setStatus('current')
osaPtpPmGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 19, 3, 2, 1)).setObjects(("INFINERA-PM-OSAPTP-MIB", "osaPtpPmValidity"), ("INFINERA-PM-OSAPTP-MIB", "osaPtpPmOprMin"), ("INFINERA-PM-OSAPTP-MIB", "osaPtpPmOprMax"), ("INFINERA-PM-OSAPTP-MIB", "osaPtpPmOprAve"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    osaPtpPmGroup = osaPtpPmGroup.setStatus('current')
osaPtpPmRealGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 19, 3, 2, 2)).setObjects(("INFINERA-PM-OSAPTP-MIB", "osaPtpPmRealOpr"), ("INFINERA-PM-OSAPTP-MIB", "osaOprOsaTapRatio"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    osaPtpPmRealGroup = osaPtpPmRealGroup.setStatus('current')
mibBuilder.exportSymbols("INFINERA-PM-OSAPTP-MIB", osaPtpPmOprMin=osaPtpPmOprMin, osaPtpPmOprAve=osaPtpPmOprAve, osaPtpPmTable=osaPtpPmTable, osaPtpPmValidity=osaPtpPmValidity, osaPtpPmGroup=osaPtpPmGroup, osaPtpPmConformance=osaPtpPmConformance, osaPtpPmTimestamp=osaPtpPmTimestamp, osaPtpPmEntry=osaPtpPmEntry, osaPtpPmRealCompliance=osaPtpPmRealCompliance, osaPtpPmOprMax=osaPtpPmOprMax, osaPtpPmRealGroup=osaPtpPmRealGroup, osaPtpPmGroups=osaPtpPmGroups, osaPtpPmRealTable=osaPtpPmRealTable, osaPtpPmCompliances=osaPtpPmCompliances, osaPtpPmRealOpr=osaPtpPmRealOpr, PYSNMP_MODULE_ID=osaPtpPmMIB, osaPtpPmSampleDuration=osaPtpPmSampleDuration, osaOprOsaTapRatio=osaOprOsaTapRatio, osaPtpPmCompliance=osaPtpPmCompliance, osaPtpPmMIB=osaPtpPmMIB, osaPtpPmRealEntry=osaPtpPmRealEntry)
