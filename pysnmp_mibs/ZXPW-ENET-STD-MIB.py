#
# PySNMP MIB module ZXPW-ENET-STD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/zte/ZXPW-ENET-STD-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:10:23 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
InterfaceIndexOrZero, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
StorageType, RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "StorageType", "RowStatus", "DisplayString", "TextualConvention")
zxAnCesMib, = mibBuilder.importSymbols("ZTE-MASTER-MIB", "zxAnCesMib")
zxPwIndex, = mibBuilder.importSymbols("ZXPW-STD-MIB", "zxPwIndex")
zxPwEnetStdMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 23))
if mibBuilder.loadTexts: zxPwEnetStdMIB.setLastUpdated('200905150000Z')
if mibBuilder.loadTexts: zxPwEnetStdMIB.setOrganization('Zhongxing Telcom Co. Ltd.')
zxPwEnetObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 23, 1))
zxPwEnetConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 23, 2))
class VlanIdOrAnyOrNone(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 4094), ValueRangeConstraint(4095, 4095), )
zxPwEnetTable = MibTable((1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 23, 1, 1), )
if mibBuilder.loadTexts: zxPwEnetTable.setStatus('current')
zxPwEnetEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 23, 1, 1, 1), ).setIndexNames((0, "ZXPW-STD-MIB", "zxPwIndex"), (0, "ZXPW-ENET-STD-MIB", "zxPwEnetPwInstance"))
if mibBuilder.loadTexts: zxPwEnetEntry.setStatus('current')
zxPwEnetPwInstance = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 23, 1, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: zxPwEnetPwInstance.setStatus('current')
zxPwEnetPwVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 23, 1, 1, 1, 2), VlanIdOrAnyOrNone()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxPwEnetPwVlan.setStatus('current')
zxPwEnetVlanMode = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 23, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("other", 0), ("portBased", 1), ("noChange", 2), ("changeVlan", 3), ("addVlan", 4), ("removeVlan", 5))).clone('noChange')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxPwEnetVlanMode.setStatus('current')
zxPwEnetPortVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 23, 1, 1, 1, 4), VlanIdOrAnyOrNone().clone(4095)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxPwEnetPortVlan.setStatus('current')
zxPwEnetPortIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 23, 1, 1, 1, 5), InterfaceIndexOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxPwEnetPortIfIndex.setStatus('current')
zxPwEnetPwIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 23, 1, 1, 1, 6), InterfaceIndexOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxPwEnetPwIfIndex.setStatus('current')
zxPwEnetRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 23, 1, 1, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxPwEnetRowStatus.setStatus('current')
zxPwEnetStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 23, 1, 1, 1, 8), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxPwEnetStorageType.setStatus('current')
mibBuilder.exportSymbols("ZXPW-ENET-STD-MIB", zxPwEnetTable=zxPwEnetTable, zxPwEnetConformance=zxPwEnetConformance, VlanIdOrAnyOrNone=VlanIdOrAnyOrNone, zxPwEnetPwInstance=zxPwEnetPwInstance, zxPwEnetPortIfIndex=zxPwEnetPortIfIndex, zxPwEnetRowStatus=zxPwEnetRowStatus, zxPwEnetPwVlan=zxPwEnetPwVlan, zxPwEnetStorageType=zxPwEnetStorageType, zxPwEnetPortVlan=zxPwEnetPortVlan, zxPwEnetStdMIB=zxPwEnetStdMIB, zxPwEnetPwIfIndex=zxPwEnetPwIfIndex, PYSNMP_MODULE_ID=zxPwEnetStdMIB, zxPwEnetVlanMode=zxPwEnetVlanMode, zxPwEnetEntry=zxPwEnetEntry, zxPwEnetObjects=zxPwEnetObjects)
