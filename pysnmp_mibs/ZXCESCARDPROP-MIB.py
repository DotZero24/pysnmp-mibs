#
# PySNMP MIB module ZXCESCARDPROP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/zte/ZXCESCARDPROP-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:10:37 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, PhysAddress, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "PhysAddress", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("ZXCESCARDPROP-MIB", zxCesCardPhysAddress=zxCesCardPhysAddress, zxCesCardAddress=zxCesCardAddress, zxCesCardPropMIB=zxCesCardPropMIB, zxCesCardPropEntry=zxCesCardPropEntry, PYSNMP_MODULE_ID=zxCesCardPropMIB, zxCesCardAddrType=zxCesCardAddrType, zxCesCardPropTable=zxCesCardPropTable, zxCesCardIndex=zxCesCardIndex, zxCesCardCfgInfoSend=zxCesCardCfgInfoSend)
