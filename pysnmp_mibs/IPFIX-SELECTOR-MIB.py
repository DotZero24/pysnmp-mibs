#
# PySNMP MIB module IPFIX-SELECTOR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/rfc/IPFIX-SELECTOR-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:50:24 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Gauge32, MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, mib_2 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "mib-2")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("IPFIX-SELECTOR-MIB", ipfixFuncSelectAll=ipfixFuncSelectAll, ipfixSelectorGroups=ipfixSelectorGroups, ipfixSelectorMIB=ipfixSelectorMIB, ipfixSelectorBasicGroup=ipfixSelectorBasicGroup, ipfixSelectorBasicCompliance=ipfixSelectorBasicCompliance, ipfixSelectorCompliances=ipfixSelectorCompliances, ipfixSelectorConformance=ipfixSelectorConformance, PYSNMP_MODULE_ID=ipfixSelectorMIB, ipfixSelectorObjects=ipfixSelectorObjects, ipfixFuncSelectAllAvail=ipfixFuncSelectAllAvail, ipfixSelectorFunctions=ipfixSelectorFunctions)
