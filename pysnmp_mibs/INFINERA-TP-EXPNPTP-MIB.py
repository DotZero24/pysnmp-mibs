#
# PySNMP MIB module INFINERA-TP-EXPNPTP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/infinera/INFINERA-TP-EXPNPTP-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:21:53 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
terminationPoint, = mibBuilder.importSymbols("INFINERA-REG-MIB", "terminationPoint")
FloatHundredths, InfnExpnPtpMode = mibBuilder.importSymbols("INFINERA-TC-MIB", "FloatHundredths", "InfnExpnPtpMode")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("INFINERA-TP-EXPNPTP-MIB", expnPtpEntry=expnPtpEntry, expnPtpConformance=expnPtpConformance, expnPtpCompliance=expnPtpCompliance, expnPtpGroup=expnPtpGroup, expnPtpMoId=expnPtpMoId, PYSNMP_MODULE_ID=expnPtpMIB, expnPtpMIB=expnPtpMIB, expnPtpMode=expnPtpMode, expnPtpCompliances=expnPtpCompliances, expnPtpGroups=expnPtpGroups, expnPtpExpectedNeighborPtp=expnPtpExpectedNeighborPtp, expnPtpTable=expnPtpTable)
