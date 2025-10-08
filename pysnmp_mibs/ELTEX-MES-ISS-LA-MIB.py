#
# PySNMP MIB module ELTEX-MES-ISS-LA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/eltex/ELTEX-MES-ISS-LA-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:11:26 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
eltMesIss, = mibBuilder.importSymbols("ELTEX-MES-ISS-MIB", "eltMesIss")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
eltMesIssLaMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 35265, 1, 139, 23))
eltMesIssLaMIB.setRevisions(('2020-12-28 00:00',))
if mibBuilder.loadTexts: eltMesIssLaMIB.setLastUpdated('202012280000Z')
if mibBuilder.loadTexts: eltMesIssLaMIB.setOrganization('Eltex Enterprise, Ltd.')
eltMesIssLaObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 139, 23, 1))
eltMesIssLaGlobals = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 139, 23, 1, 1))
eltMesIssLaSelectionPolicyTable = MibTable((1, 3, 6, 1, 4, 1, 35265, 1, 139, 23, 1, 1, 1), )
if mibBuilder.loadTexts: eltMesIssLaSelectionPolicyTable.setStatus('current')
eltMesIssLaSelectionPolicyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 35265, 1, 139, 23, 1, 1, 1, 1), ).setIndexNames((0, "ELTEX-MES-ISS-LA-MIB", "eltMesIssLaAlgorithmIdx"))
if mibBuilder.loadTexts: eltMesIssLaSelectionPolicyEntry.setStatus('current')
eltMesIssLaAlgorithmIdx = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 139, 23, 1, 1, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: eltMesIssLaAlgorithmIdx.setStatus('current')
eltMesIssLaPortChannelSelectionPolicy = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 139, 23, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("macSrc", 1), ("macDst", 2), ("macSrcDst", 3), ("ipSrc", 4), ("ipDst", 5), ("ipSrcDst", 6), ("macIpSrcDst", 7), ("macIpPortSrcDst", 8))).clone('macSrcDst')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltMesIssLaPortChannelSelectionPolicy.setStatus('current')
mibBuilder.exportSymbols("ELTEX-MES-ISS-LA-MIB", eltMesIssLaPortChannelSelectionPolicy=eltMesIssLaPortChannelSelectionPolicy, eltMesIssLaObjects=eltMesIssLaObjects, PYSNMP_MODULE_ID=eltMesIssLaMIB, eltMesIssLaSelectionPolicyTable=eltMesIssLaSelectionPolicyTable, eltMesIssLaSelectionPolicyEntry=eltMesIssLaSelectionPolicyEntry, eltMesIssLaAlgorithmIdx=eltMesIssLaAlgorithmIdx, eltMesIssLaMIB=eltMesIssLaMIB, eltMesIssLaGlobals=eltMesIssLaGlobals)
