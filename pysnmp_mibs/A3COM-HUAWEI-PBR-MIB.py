#
# PySNMP MIB module A3COM-HUAWEI-PBR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/a3com/A3COM-HUAWEI-PBR-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:32:48 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
h3cCommon, = mibBuilder.importSymbols("A3COM-HUAWEI-OID-MIB", "h3cCommon")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
h3cPBR = ModuleIdentity((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 113))
h3cPBR.setRevisions(('2010-12-10 15:58',))
if mibBuilder.loadTexts: h3cPBR.setLastUpdated('201012101558Z')
if mibBuilder.loadTexts: h3cPBR.setOrganization('Hangzhou H3C Technologies Co., Ltd.')
h3cPBRObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 113, 1))
h3cPBRGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 113, 1, 1))
h3cPBRMibTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 113, 1, 2))
h3cPBRNexthopTrapEnabled = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 113, 1, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cPBRNexthopTrapEnabled.setStatus('current')
h3cPBRTrapObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 113, 1, 2, 1))
h3cPBRNexthopAddrType = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 113, 1, 2, 1, 1), InetAddressType()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: h3cPBRNexthopAddrType.setStatus('current')
h3cPBRNexthopAddr = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 113, 1, 2, 1, 2), InetAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: h3cPBRNexthopAddr.setStatus('current')
h3cPBRTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 113, 1, 2, 2))
h3cPBRTrapsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 113, 1, 2, 2, 0))
h3cPBRNexthopFailedTrap = NotificationType((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 113, 1, 2, 2, 0, 1)).setObjects(("A3COM-HUAWEI-PBR-MIB", "h3cPBRNexthopAddrType"), ("A3COM-HUAWEI-PBR-MIB", "h3cPBRNexthopAddr"))
if mibBuilder.loadTexts: h3cPBRNexthopFailedTrap.setStatus('current')
mibBuilder.exportSymbols("A3COM-HUAWEI-PBR-MIB", h3cPBRTrapObjects=h3cPBRTrapObjects, h3cPBRObjects=h3cPBRObjects, h3cPBRMibTrap=h3cPBRMibTrap, h3cPBRNexthopAddrType=h3cPBRNexthopAddrType, h3cPBRTrapsPrefix=h3cPBRTrapsPrefix, h3cPBR=h3cPBR, h3cPBRNexthopFailedTrap=h3cPBRNexthopFailedTrap, h3cPBRNexthopTrapEnabled=h3cPBRNexthopTrapEnabled, h3cPBRTraps=h3cPBRTraps, h3cPBRNexthopAddr=h3cPBRNexthopAddr, PYSNMP_MODULE_ID=h3cPBR, h3cPBRGlobal=h3cPBRGlobal)
