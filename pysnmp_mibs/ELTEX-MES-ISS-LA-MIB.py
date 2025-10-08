#
# PySNMP MIB module ELTEX-MES-ISS-LA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/eltex/ELTEX-MES-ISS-LA-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:04:19 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
eltMesIss, = mibBuilder.importSymbols("ELTEX-MES-ISS-MIB", "eltMesIss")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("ELTEX-MES-ISS-LA-MIB", PYSNMP_MODULE_ID=eltMesIssLaMIB, eltMesIssLaGlobals=eltMesIssLaGlobals, eltMesIssLaPortChannelSelectionPolicy=eltMesIssLaPortChannelSelectionPolicy, eltMesIssLaObjects=eltMesIssLaObjects, eltMesIssLaMIB=eltMesIssLaMIB, eltMesIssLaAlgorithmIdx=eltMesIssLaAlgorithmIdx, eltMesIssLaSelectionPolicyEntry=eltMesIssLaSelectionPolicyEntry, eltMesIssLaSelectionPolicyTable=eltMesIssLaSelectionPolicyTable)
