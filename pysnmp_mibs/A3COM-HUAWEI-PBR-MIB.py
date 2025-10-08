#
# PySNMP MIB module A3COM-HUAWEI-PBR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/a3com/A3COM-HUAWEI-PBR-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:16:38 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
h3cCommon, = mibBuilder.importSymbols("A3COM-HUAWEI-OID-MIB", "h3cCommon")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
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
mibBuilder.exportSymbols("A3COM-HUAWEI-PBR-MIB", PYSNMP_MODULE_ID=h3cPBR, h3cPBRNexthopAddrType=h3cPBRNexthopAddrType, h3cPBRNexthopFailedTrap=h3cPBRNexthopFailedTrap, h3cPBRObjects=h3cPBRObjects, h3cPBRTraps=h3cPBRTraps, h3cPBRMibTrap=h3cPBRMibTrap, h3cPBRTrapsPrefix=h3cPBRTrapsPrefix, h3cPBRNexthopAddr=h3cPBRNexthopAddr, h3cPBRGlobal=h3cPBRGlobal, h3cPBR=h3cPBR, h3cPBRNexthopTrapEnabled=h3cPBRNexthopTrapEnabled, h3cPBRTrapObjects=h3cPBRTrapObjects)
