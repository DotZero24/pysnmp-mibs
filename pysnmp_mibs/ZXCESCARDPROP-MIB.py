#
# PySNMP MIB module ZXCESCARDPROP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/zte/ZXCESCARDPROP-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:03:52 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, TextualConvention, PhysAddress = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention", "PhysAddress")
zxPwCETH, = mibBuilder.importSymbols("ZTE-MASTER-MIB", "zxPwCETH")
zxCesCardPropMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 3, 1, 1))
if mibBuilder.loadTexts: zxCesCardPropMIB.setLastUpdated('200609190000Z')
if mibBuilder.loadTexts: zxCesCardPropMIB.setOrganization('Zhongxing Telcom Co. Ltd.')
zxCesCardPropTable = MibTable((1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 3, 1, 1, 1), )
if mibBuilder.loadTexts: zxCesCardPropTable.setStatus('current')
zxCesCardPropEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 3, 1, 1, 1, 1), ).setIndexNames((0, "ZXCESCARDPROP-MIB", "zxCesCardIndex"))
if mibBuilder.loadTexts: zxCesCardPropEntry.setStatus('current')
zxCesCardIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 3, 1, 1, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: zxCesCardIndex.setStatus('current')
zxCesCardPhysAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 3, 1, 1, 1, 1, 2), PhysAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zxCesCardPhysAddress.setStatus('current')
zxCesCardAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 3, 1, 1, 1, 1, 3), InetAddressType().clone('ipv4')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zxCesCardAddrType.setStatus('current')
zxCesCardAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 3, 1, 1, 1, 1, 4), InetAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zxCesCardAddress.setStatus('current')
zxCesCardCfgInfoSend = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 3, 1, 1, 1, 1, 5), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zxCesCardCfgInfoSend.setStatus('current')
mibBuilder.exportSymbols("ZXCESCARDPROP-MIB", zxCesCardCfgInfoSend=zxCesCardCfgInfoSend, zxCesCardPhysAddress=zxCesCardPhysAddress, zxCesCardPropEntry=zxCesCardPropEntry, zxCesCardIndex=zxCesCardIndex, zxCesCardAddress=zxCesCardAddress, PYSNMP_MODULE_ID=zxCesCardPropMIB, zxCesCardAddrType=zxCesCardAddrType, zxCesCardPropTable=zxCesCardPropTable, zxCesCardPropMIB=zxCesCardPropMIB)
