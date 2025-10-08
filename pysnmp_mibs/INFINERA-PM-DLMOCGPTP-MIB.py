#
# PySNMP MIB module INFINERA-PM-DLMOCGPTP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/infinera/INFINERA-PM-DLMOCGPTP-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:09:39 2025
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
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
dlmOcgPtpPmMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 5))
dlmOcgPtpPmMIB.setRevisions(('2008-10-20 00:00',))
if mibBuilder.loadTexts: dlmOcgPtpPmMIB.setLastUpdated('200810200000Z')
if mibBuilder.loadTexts: dlmOcgPtpPmMIB.setOrganization('Infinera')
dlmOcgPtpPmRealTable = MibTable((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 5, 1), )
if mibBuilder.loadTexts: dlmOcgPtpPmRealTable.setStatus('current')
dlmOcgPtpPmRealEntry = MibTableRow((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 5, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: dlmOcgPtpPmRealEntry.setStatus('current')
dlmOcgPtpPmRealDlmOcgOpt = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 5, 1, 1, 1), FloatHundredths()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dlmOcgPtpPmRealDlmOcgOpt.setStatus('current')
dlmOcgPtpPmRealDlmOcgOpr = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 5, 1, 1, 2), FloatHundredths()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dlmOcgPtpPmRealDlmOcgOpr.setStatus('current')
dlmOcgPtpPmConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 5, 3))
dlmOcgPtpPmCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 5, 3, 1))
dlmOcgPtpPmGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 5, 3, 2))
dlmOcgPtpPmRealCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 5, 3, 1, 1)).setObjects(("INFINERA-PM-DLMOCGPTP-MIB", "dlmOcgPtpPmRealGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dlmOcgPtpPmRealCompliance = dlmOcgPtpPmRealCompliance.setStatus('current')
dlmOcgPtpPmRealGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 5, 3, 2, 1)).setObjects(("INFINERA-PM-DLMOCGPTP-MIB", "dlmOcgPtpPmRealDlmOcgOpt"), ("INFINERA-PM-DLMOCGPTP-MIB", "dlmOcgPtpPmRealDlmOcgOpr"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dlmOcgPtpPmRealGroup = dlmOcgPtpPmRealGroup.setStatus('current')
mibBuilder.exportSymbols("INFINERA-PM-DLMOCGPTP-MIB", dlmOcgPtpPmRealEntry=dlmOcgPtpPmRealEntry, dlmOcgPtpPmRealDlmOcgOpt=dlmOcgPtpPmRealDlmOcgOpt, dlmOcgPtpPmGroups=dlmOcgPtpPmGroups, dlmOcgPtpPmRealCompliance=dlmOcgPtpPmRealCompliance, PYSNMP_MODULE_ID=dlmOcgPtpPmMIB, dlmOcgPtpPmMIB=dlmOcgPtpPmMIB, dlmOcgPtpPmRealGroup=dlmOcgPtpPmRealGroup, dlmOcgPtpPmCompliances=dlmOcgPtpPmCompliances, dlmOcgPtpPmRealDlmOcgOpr=dlmOcgPtpPmRealDlmOcgOpr, dlmOcgPtpPmConformance=dlmOcgPtpPmConformance, dlmOcgPtpPmRealTable=dlmOcgPtpPmRealTable)
