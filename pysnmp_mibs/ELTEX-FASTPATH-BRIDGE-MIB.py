#
# PySNMP MIB module ELTEX-FASTPATH-BRIDGE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/eltex/ELTEX-FASTPATH-BRIDGE-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:04:19 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
dot1dBasePort, = mibBuilder.importSymbols("BRIDGE-MIB", "dot1dBasePort")
eltMesFastpath, = mibBuilder.importSymbols("ELTEX-MES-FASTPATH-MIB", "eltMesFastpath")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
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
mibBuilder.exportSymbols("ELTEX-FASTPATH-BRIDGE-MIB", efpBridgeConfigsStp=efpBridgeConfigsStp, efpBridgeObjects=efpBridgeObjects, efpBridgeNotificationsPrefix=efpBridgeNotificationsPrefix, efpBridgeConfigs=efpBridgeConfigs, efpBridgeNotifications=efpBridgeNotifications, efpBridgeStpConfigPortEntry=efpBridgeStpConfigPortEntry, eltFastpathBridgeMIB=eltFastpathBridgeMIB, PYSNMP_MODULE_ID=eltFastpathBridgeMIB, EfpBridgeStpGroupMacAddressType=EfpBridgeStpGroupMacAddressType, efpBridgeStpConfigPortGroupMacAddress=efpBridgeStpConfigPortGroupMacAddress, efpBridgeConformance=efpBridgeConformance, efpBridgeStpConfigPortTable=efpBridgeStpConfigPortTable)
