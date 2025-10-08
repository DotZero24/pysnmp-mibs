#
# PySNMP MIB module IPFIX-SELECTOR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/rfc/IPFIX-SELECTOR-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:27:52 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, TimeTicks, MibIdentifier, Integer32, Bits, mib_2, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "TimeTicks", "MibIdentifier", "Integer32", "Bits", "mib-2", "IpAddress")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
ipfixSelectorMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 194))
ipfixSelectorMIB.setRevisions(('2012-06-11 00:00', '2010-03-15 00:00',))
if mibBuilder.loadTexts: ipfixSelectorMIB.setLastUpdated('201206110000Z')
if mibBuilder.loadTexts: ipfixSelectorMIB.setOrganization('IETF IPFIX Working Group')
ipfixSelectorObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 194, 1))
ipfixSelectorConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 194, 2))
ipfixSelectorFunctions = MibIdentifier((1, 3, 6, 1, 2, 1, 194, 1, 1))
ipfixFuncSelectAll = MibIdentifier((1, 3, 6, 1, 2, 1, 194, 1, 1, 1))
ipfixFuncSelectAllAvail = MibScalar((1, 3, 6, 1, 2, 1, 194, 1, 1, 1, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipfixFuncSelectAllAvail.setStatus('current')
ipfixSelectorCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 194, 2, 1))
ipfixSelectorGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 194, 2, 2))
ipfixSelectorBasicCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 194, 2, 1, 1)).setObjects(("IPFIX-SELECTOR-MIB", "ipfixSelectorBasicGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ipfixSelectorBasicCompliance = ipfixSelectorBasicCompliance.setStatus('current')
ipfixSelectorBasicGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 194, 2, 2, 1)).setObjects(("IPFIX-SELECTOR-MIB", "ipfixFuncSelectAllAvail"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ipfixSelectorBasicGroup = ipfixSelectorBasicGroup.setStatus('current')
mibBuilder.exportSymbols("IPFIX-SELECTOR-MIB", ipfixFuncSelectAllAvail=ipfixFuncSelectAllAvail, ipfixFuncSelectAll=ipfixFuncSelectAll, ipfixSelectorCompliances=ipfixSelectorCompliances, ipfixSelectorBasicCompliance=ipfixSelectorBasicCompliance, ipfixSelectorMIB=ipfixSelectorMIB, ipfixSelectorConformance=ipfixSelectorConformance, ipfixSelectorBasicGroup=ipfixSelectorBasicGroup, ipfixSelectorFunctions=ipfixSelectorFunctions, ipfixSelectorObjects=ipfixSelectorObjects, ipfixSelectorGroups=ipfixSelectorGroups, PYSNMP_MODULE_ID=ipfixSelectorMIB)
