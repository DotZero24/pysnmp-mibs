#
# PySNMP MIB module HPN-ICF-UPS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/hp/HPN-ICF-UPS-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:02:13 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
hpnicfCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfCommon")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Counter32, iso, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Counter32", "iso", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hpnicfUps = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 82))
if mibBuilder.loadTexts: hpnicfUps.setLastUpdated('200709041452Z')
if mibBuilder.loadTexts: hpnicfUps.setOrganization('')
hpnicfUpsMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 82, 1))
class HpnicfActionType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("action", 1), ("invalid", 2))

hpnicfUpsConfigEnable = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 82, 1, 1), HpnicfActionType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfUpsConfigEnable.setStatus('current')
hpnicfUpsConfigTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 82, 1, 2), )
if mibBuilder.loadTexts: hpnicfUpsConfigTable.setStatus('current')
hpnicfUpsConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 82, 1, 2, 1), ).setIndexNames((0, "HPN-ICF-UPS-MIB", "hpnicfUpsIndex"))
if mibBuilder.loadTexts: hpnicfUpsConfigEntry.setStatus('current')
hpnicfUpsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 82, 1, 2, 1, 1), Integer32())
if mibBuilder.loadTexts: hpnicfUpsIndex.setStatus('current')
hpnicfUpsType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 82, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("emersonUart", 1), ("mge", 2), ("common", 3), ("emersonEth", 4), ("liebert", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfUpsType.setStatus('current')
hpnicfUpsIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 82, 1, 2, 1, 3), InetAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfUpsIpAddress.setStatus('current')
hpnicfUpsIpAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 82, 1, 2, 1, 4), InetAddressType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfUpsIpAddressType.setStatus('current')
mibBuilder.exportSymbols("HPN-ICF-UPS-MIB", hpnicfUpsIpAddressType=hpnicfUpsIpAddressType, hpnicfUpsIpAddress=hpnicfUpsIpAddress, HpnicfActionType=HpnicfActionType, hpnicfUpsConfigEnable=hpnicfUpsConfigEnable, hpnicfUpsIndex=hpnicfUpsIndex, hpnicfUpsMibObjects=hpnicfUpsMibObjects, hpnicfUps=hpnicfUps, hpnicfUpsConfigTable=hpnicfUpsConfigTable, hpnicfUpsConfigEntry=hpnicfUpsConfigEntry, PYSNMP_MODULE_ID=hpnicfUps, hpnicfUpsType=hpnicfUpsType)
