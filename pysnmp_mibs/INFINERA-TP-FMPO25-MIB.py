#
# PySNMP MIB module INFINERA-TP-FMPO25-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/infinera/INFINERA-TP-FMPO25-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:21:16 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
terminationPoint, = mibBuilder.importSymbols("INFINERA-REG-MIB", "terminationPoint")
FloatHundredths, InfnEnableDisable = mibBuilder.importSymbols("INFINERA-TC-MIB", "FloatHundredths", "InfnEnableDisable")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("INFINERA-TP-FMPO25-MIB", fmpo25PtpTable=fmpo25PtpTable, fmpo25PtpGroup=fmpo25PtpGroup, fmpo25PtpConformance=fmpo25PtpConformance, fmpo25PtpEntry=fmpo25PtpEntry, fmpo25PtpGroups=fmpo25PtpGroups, fmpo25PtpProvNbrTP=fmpo25PtpProvNbrTP, fmpo25PtpCompliance=fmpo25PtpCompliance, fmpo25PtpCompliances=fmpo25PtpCompliances, fmpo25PtpMIB=fmpo25PtpMIB, PYSNMP_MODULE_ID=fmpo25PtpMIB)
