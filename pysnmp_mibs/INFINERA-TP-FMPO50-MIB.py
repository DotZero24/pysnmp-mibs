#
# PySNMP MIB module INFINERA-TP-FMPO50-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/infinera/INFINERA-TP-FMPO50-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:21:51 2025
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
mibBuilder.exportSymbols("INFINERA-TP-FMPO50-MIB", fmpo50PtpProvNbrTP=fmpo50PtpProvNbrTP, fmpo50PtpEntry=fmpo50PtpEntry, fmpo50PtpTable=fmpo50PtpTable, fmpo50PtpCompliances=fmpo50PtpCompliances, fmpo50PtpGroup=fmpo50PtpGroup, fmpo50PtpCompliance=fmpo50PtpCompliance, fmpo50PtpConformance=fmpo50PtpConformance, fmpo50PtpMIB=fmpo50PtpMIB, fmpo50PtpGroups=fmpo50PtpGroups, PYSNMP_MODULE_ID=fmpo50PtpMIB)
