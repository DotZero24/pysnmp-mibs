#
# PySNMP MIB module INFINERA-TP-ampOtdrPtp-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/infinera/INFINERA-TP-ampOtdrPtp-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:09:20 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
terminationPoint, = mibBuilder.importSymbols("INFINERA-REG-MIB", "terminationPoint")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("INFINERA-TP-ampOtdrPtp-MIB", PYSNMP_MODULE_ID=ampOtdrPtpMIB, ampOtdrPtpTable=ampOtdrPtpTable, ampOtdrPtpEntry=ampOtdrPtpEntry, ampOtdrPtpGroups=ampOtdrPtpGroups, ampOtdrPtpCompliance=ampOtdrPtpCompliance, ampOtdrPtpConformance=ampOtdrPtpConformance, ampOtdrPtpLstSuccConnValidationTime=ampOtdrPtpLstSuccConnValidationTime, ampOtdrPtpExpectedNeighborPtp=ampOtdrPtpExpectedNeighborPtp, ampOtdrPtpCompliances=ampOtdrPtpCompliances, ampOtdrPtpConnectivityState=ampOtdrPtpConnectivityState, ampOtdrPtpMIB=ampOtdrPtpMIB, ampOtdrPtpGroup=ampOtdrPtpGroup)
