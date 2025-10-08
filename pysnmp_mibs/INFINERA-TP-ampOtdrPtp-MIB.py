#
# PySNMP MIB module INFINERA-TP-ampOtdrPtp-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/infinera/INFINERA-TP-ampOtdrPtp-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:20:13 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
terminationPoint, = mibBuilder.importSymbols("INFINERA-REG-MIB", "terminationPoint")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ampOtdrPtpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 49))
ampOtdrPtpMIB.setRevisions(('2013-10-20 00:00',))
if mibBuilder.loadTexts: ampOtdrPtpMIB.setLastUpdated('201310200000Z')
if mibBuilder.loadTexts: ampOtdrPtpMIB.setOrganization('Infinera')
ampOtdrPtpTable = MibTable((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 49, 1), )
if mibBuilder.loadTexts: ampOtdrPtpTable.setStatus('current')
ampOtdrPtpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 49, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: ampOtdrPtpEntry.setStatus('current')
ampOtdrPtpConnectivityState = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 49, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notVerified", 1), ("valid", 2), ("inValid", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ampOtdrPtpConnectivityState.setStatus('current')
ampOtdrPtpLstSuccConnValidationTime = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 49, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ampOtdrPtpLstSuccConnValidationTime.setStatus('current')
ampOtdrPtpExpectedNeighborPtp = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 49, 1, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ampOtdrPtpExpectedNeighborPtp.setStatus('current')
ampOtdrPtpConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 49, 3))
ampOtdrPtpCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 49, 3, 1))
ampOtdrPtpGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 49, 3, 2))
ampOtdrPtpCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 49, 3, 1, 1)).setObjects(("INFINERA-TP-ampOtdrPtp-MIB", "ampOtdrPtpGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ampOtdrPtpCompliance = ampOtdrPtpCompliance.setStatus('current')
ampOtdrPtpGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 49, 3, 2, 1)).setObjects(("INFINERA-TP-ampOtdrPtp-MIB", "ampOtdrPtpConnectivityState"), ("INFINERA-TP-ampOtdrPtp-MIB", "ampOtdrPtpLstSuccConnValidationTime"), ("INFINERA-TP-ampOtdrPtp-MIB", "ampOtdrPtpExpectedNeighborPtp"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ampOtdrPtpGroup = ampOtdrPtpGroup.setStatus('current')
mibBuilder.exportSymbols("INFINERA-TP-ampOtdrPtp-MIB", ampOtdrPtpTable=ampOtdrPtpTable, ampOtdrPtpGroup=ampOtdrPtpGroup, ampOtdrPtpMIB=ampOtdrPtpMIB, ampOtdrPtpConnectivityState=ampOtdrPtpConnectivityState, ampOtdrPtpConformance=ampOtdrPtpConformance, ampOtdrPtpCompliance=ampOtdrPtpCompliance, ampOtdrPtpExpectedNeighborPtp=ampOtdrPtpExpectedNeighborPtp, ampOtdrPtpEntry=ampOtdrPtpEntry, ampOtdrPtpCompliances=ampOtdrPtpCompliances, ampOtdrPtpGroups=ampOtdrPtpGroups, ampOtdrPtpLstSuccConnValidationTime=ampOtdrPtpLstSuccConnValidationTime, PYSNMP_MODULE_ID=ampOtdrPtpMIB)
