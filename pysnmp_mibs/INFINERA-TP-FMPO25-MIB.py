#
# PySNMP MIB module INFINERA-TP-FMPO25-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/infinera/INFINERA-TP-FMPO25-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:09:54 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
terminationPoint, = mibBuilder.importSymbols("INFINERA-REG-MIB", "terminationPoint")
FloatHundredths, InfnEnableDisable = mibBuilder.importSymbols("INFINERA-TC-MIB", "FloatHundredths", "InfnEnableDisable")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
fmpo25PtpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 40))
fmpo25PtpMIB.setRevisions(('2013-10-20 00:00',))
if mibBuilder.loadTexts: fmpo25PtpMIB.setLastUpdated('201310200000Z')
if mibBuilder.loadTexts: fmpo25PtpMIB.setOrganization('Infinera')
fmpo25PtpTable = MibTable((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 40, 1), )
if mibBuilder.loadTexts: fmpo25PtpTable.setStatus('current')
fmpo25PtpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 40, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: fmpo25PtpEntry.setStatus('current')
fmpo25PtpProvNbrTP = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 40, 1, 1, 1), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fmpo25PtpProvNbrTP.setStatus('current')
fmpo25PtpConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 40, 3))
fmpo25PtpCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 40, 3, 1))
fmpo25PtpGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 40, 3, 2))
fmpo25PtpCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 40, 3, 1, 1)).setObjects(("INFINERA-TP-FMPO25-MIB", "fmpo25PtpGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fmpo25PtpCompliance = fmpo25PtpCompliance.setStatus('current')
fmpo25PtpGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 40, 3, 2, 1)).setObjects(("INFINERA-TP-FMPO25-MIB", "fmpo25PtpProvNbrTP"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fmpo25PtpGroup = fmpo25PtpGroup.setStatus('current')
mibBuilder.exportSymbols("INFINERA-TP-FMPO25-MIB", fmpo25PtpProvNbrTP=fmpo25PtpProvNbrTP, fmpo25PtpTable=fmpo25PtpTable, fmpo25PtpCompliances=fmpo25PtpCompliances, PYSNMP_MODULE_ID=fmpo25PtpMIB, fmpo25PtpCompliance=fmpo25PtpCompliance, fmpo25PtpMIB=fmpo25PtpMIB, fmpo25PtpGroup=fmpo25PtpGroup, fmpo25PtpEntry=fmpo25PtpEntry, fmpo25PtpGroups=fmpo25PtpGroups, fmpo25PtpConformance=fmpo25PtpConformance)
