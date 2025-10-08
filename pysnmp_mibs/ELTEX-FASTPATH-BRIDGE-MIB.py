#
# PySNMP MIB module ELTEX-FASTPATH-BRIDGE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/eltex/ELTEX-FASTPATH-BRIDGE-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:11:25 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
dot1dBasePort, = mibBuilder.importSymbols("BRIDGE-MIB", "dot1dBasePort")
eltMesFastpath, = mibBuilder.importSymbols("ELTEX-MES-FASTPATH-MIB", "eltMesFastpath")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
eltFastpathBridgeMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 35265, 1, 103, 3))
eltFastpathBridgeMIB.setRevisions(('2017-09-05 00:00',))
if mibBuilder.loadTexts: eltFastpathBridgeMIB.setLastUpdated('201709050000Z')
if mibBuilder.loadTexts: eltFastpathBridgeMIB.setOrganization('Eltex Enterprise Co, Ltd.')
efpBridgeObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 103, 3, 1))
efpBridgeConfigs = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 103, 3, 1, 2))
class EfpBridgeStpGroupMacAddressType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("dot1d", 1), ("dot1ad", 2), ("auto", 3))

efpBridgeConfigsStp = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 103, 3, 1, 2, 1))
efpBridgeStpConfigPortTable = MibTable((1, 3, 6, 1, 4, 1, 35265, 1, 103, 3, 1, 2, 1, 1), )
if mibBuilder.loadTexts: efpBridgeStpConfigPortTable.setStatus('current')
efpBridgeStpConfigPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 35265, 1, 103, 3, 1, 2, 1, 1, 1), ).setIndexNames((0, "BRIDGE-MIB", "dot1dBasePort"))
if mibBuilder.loadTexts: efpBridgeStpConfigPortEntry.setStatus('current')
efpBridgeStpConfigPortGroupMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 103, 3, 1, 2, 1, 1, 1, 1), EfpBridgeStpGroupMacAddressType().clone('dot1d')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: efpBridgeStpConfigPortGroupMacAddress.setStatus('current')
efpBridgeNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 103, 3, 2))
efpBridgeNotificationsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 103, 3, 2, 0))
efpBridgeConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 103, 3, 3))
mibBuilder.exportSymbols("ELTEX-FASTPATH-BRIDGE-MIB", efpBridgeNotifications=efpBridgeNotifications, efpBridgeConfigs=efpBridgeConfigs, efpBridgeConformance=efpBridgeConformance, PYSNMP_MODULE_ID=eltFastpathBridgeMIB, efpBridgeNotificationsPrefix=efpBridgeNotificationsPrefix, efpBridgeObjects=efpBridgeObjects, eltFastpathBridgeMIB=eltFastpathBridgeMIB, efpBridgeStpConfigPortEntry=efpBridgeStpConfigPortEntry, EfpBridgeStpGroupMacAddressType=EfpBridgeStpGroupMacAddressType, efpBridgeConfigsStp=efpBridgeConfigsStp, efpBridgeStpConfigPortTable=efpBridgeStpConfigPortTable, efpBridgeStpConfigPortGroupMacAddress=efpBridgeStpConfigPortGroupMacAddress)
