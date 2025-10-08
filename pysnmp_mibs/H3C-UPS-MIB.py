#
# PySNMP MIB module H3C-UPS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/h3c/H3C-UPS-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:10:43 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
h3cCommon, = mibBuilder.importSymbols("HUAWEI-3COM-OID-MIB", "h3cCommon")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Counter32, iso, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Counter32", "iso", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
h3cUps = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 10, 2, 82))
if mibBuilder.loadTexts: h3cUps.setLastUpdated('200709041452Z')
if mibBuilder.loadTexts: h3cUps.setOrganization('H3C Technologies Co., Ltd.')
h3cUpsMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 82, 1))
class H3cActionType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("action", 1), ("invalid", 2))

h3cUpsConfigEnable = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 82, 1, 1), H3cActionType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cUpsConfigEnable.setStatus('current')
h3cUpsConfigTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 82, 1, 2), )
if mibBuilder.loadTexts: h3cUpsConfigTable.setStatus('current')
h3cUpsConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 82, 1, 2, 1), ).setIndexNames((0, "H3C-UPS-MIB", "h3cUpsIndex"))
if mibBuilder.loadTexts: h3cUpsConfigEntry.setStatus('current')
h3cUpsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 82, 1, 2, 1, 1), Integer32())
if mibBuilder.loadTexts: h3cUpsIndex.setStatus('current')
h3cUpsType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 82, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("emersonUart", 1), ("mge", 2), ("common", 3), ("emersonEth", 4), ("liebert", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cUpsType.setStatus('current')
h3cUpsIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 82, 1, 2, 1, 3), InetAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cUpsIpAddress.setStatus('current')
h3cUpsIpAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 82, 1, 2, 1, 4), InetAddressType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cUpsIpAddressType.setStatus('current')
mibBuilder.exportSymbols("H3C-UPS-MIB", h3cUpsIpAddress=h3cUpsIpAddress, h3cUpsIpAddressType=h3cUpsIpAddressType, PYSNMP_MODULE_ID=h3cUps, h3cUpsConfigTable=h3cUpsConfigTable, H3cActionType=H3cActionType, h3cUpsIndex=h3cUpsIndex, h3cUpsConfigEnable=h3cUpsConfigEnable, h3cUpsType=h3cUpsType, h3cUpsMibObjects=h3cUpsMibObjects, h3cUps=h3cUps, h3cUpsConfigEntry=h3cUpsConfigEntry)
