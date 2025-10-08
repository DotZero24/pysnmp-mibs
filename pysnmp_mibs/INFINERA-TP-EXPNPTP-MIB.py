#
# PySNMP MIB module INFINERA-TP-EXPNPTP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/infinera/INFINERA-TP-EXPNPTP-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:10:14 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
terminationPoint, = mibBuilder.importSymbols("INFINERA-REG-MIB", "terminationPoint")
InfnExpnPtpMode, FloatHundredths = mibBuilder.importSymbols("INFINERA-TC-MIB", "InfnExpnPtpMode", "FloatHundredths")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
expnPtpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 82))
expnPtpMIB.setRevisions(('2017-02-02 00:00',))
if mibBuilder.loadTexts: expnPtpMIB.setLastUpdated('201702020000Z')
if mibBuilder.loadTexts: expnPtpMIB.setOrganization('Infinera')
expnPtpTable = MibTable((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 82, 1), )
if mibBuilder.loadTexts: expnPtpTable.setStatus('current')
expnPtpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 82, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: expnPtpEntry.setStatus('current')
expnPtpMoId = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 82, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: expnPtpMoId.setStatus('current')
expnPtpExpectedNeighborPtp = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 82, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: expnPtpExpectedNeighborPtp.setStatus('current')
expnPtpMode = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 82, 1, 1, 3), InfnExpnPtpMode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: expnPtpMode.setStatus('current')
expnPtpConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 82, 3))
expnPtpCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 82, 3, 1))
expnPtpGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 82, 3, 2))
expnPtpCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 82, 3, 1, 1)).setObjects(("INFINERA-TP-EXPNPTP-MIB", "expnPtpGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    expnPtpCompliance = expnPtpCompliance.setStatus('current')
expnPtpGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 82, 3, 2, 1)).setObjects(("INFINERA-TP-EXPNPTP-MIB", "expnPtpMoId"), ("INFINERA-TP-EXPNPTP-MIB", "expnPtpExpectedNeighborPtp"), ("INFINERA-TP-EXPNPTP-MIB", "expnPtpMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    expnPtpGroup = expnPtpGroup.setStatus('current')
mibBuilder.exportSymbols("INFINERA-TP-EXPNPTP-MIB", expnPtpGroups=expnPtpGroups, expnPtpTable=expnPtpTable, expnPtpGroup=expnPtpGroup, PYSNMP_MODULE_ID=expnPtpMIB, expnPtpConformance=expnPtpConformance, expnPtpMIB=expnPtpMIB, expnPtpEntry=expnPtpEntry, expnPtpMoId=expnPtpMoId, expnPtpExpectedNeighborPtp=expnPtpExpectedNeighborPtp, expnPtpCompliance=expnPtpCompliance, expnPtpCompliances=expnPtpCompliances, expnPtpMode=expnPtpMode)
