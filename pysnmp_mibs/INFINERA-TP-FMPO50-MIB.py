#
# PySNMP MIB module INFINERA-TP-FMPO50-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/infinera/INFINERA-TP-FMPO50-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:10:12 2025
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
fmpo50PtpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 41))
fmpo50PtpMIB.setRevisions(('2013-10-20 00:00',))
if mibBuilder.loadTexts: fmpo50PtpMIB.setLastUpdated('201310200000Z')
if mibBuilder.loadTexts: fmpo50PtpMIB.setOrganization('Infinera')
fmpo50PtpTable = MibTable((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 41, 1), )
if mibBuilder.loadTexts: fmpo50PtpTable.setStatus('current')
fmpo50PtpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 41, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: fmpo50PtpEntry.setStatus('current')
fmpo50PtpProvNbrTP = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 41, 1, 1, 1), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fmpo50PtpProvNbrTP.setStatus('current')
fmpo50PtpConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 41, 3))
fmpo50PtpCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 41, 3, 1))
fmpo50PtpGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 41, 3, 2))
fmpo50PtpCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 41, 3, 1, 1)).setObjects(("INFINERA-TP-FMPO50-MIB", "fmpo50PtpGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fmpo50PtpCompliance = fmpo50PtpCompliance.setStatus('current')
fmpo50PtpGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 41, 3, 2, 1)).setObjects(("INFINERA-TP-FMPO50-MIB", "fmpo50PtpProvNbrTP"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fmpo50PtpGroup = fmpo50PtpGroup.setStatus('current')
mibBuilder.exportSymbols("INFINERA-TP-FMPO50-MIB", fmpo50PtpMIB=fmpo50PtpMIB, fmpo50PtpCompliance=fmpo50PtpCompliance, fmpo50PtpGroup=fmpo50PtpGroup, fmpo50PtpTable=fmpo50PtpTable, fmpo50PtpEntry=fmpo50PtpEntry, PYSNMP_MODULE_ID=fmpo50PtpMIB, fmpo50PtpCompliances=fmpo50PtpCompliances, fmpo50PtpGroups=fmpo50PtpGroups, fmpo50PtpProvNbrTP=fmpo50PtpProvNbrTP, fmpo50PtpConformance=fmpo50PtpConformance)
