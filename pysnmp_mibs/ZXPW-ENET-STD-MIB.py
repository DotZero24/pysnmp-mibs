#
# PySNMP MIB module ZXPW-ENET-STD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/zte/ZXPW-ENET-STD-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:03:45 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
InterfaceIndexOrZero, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention, RowStatus, StorageType = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus", "StorageType")
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
mibBuilder.exportSymbols("ZXPW-ENET-STD-MIB", zxPwEnetObjects=zxPwEnetObjects, zxPwEnetEntry=zxPwEnetEntry, PYSNMP_MODULE_ID=zxPwEnetStdMIB, zxPwEnetConformance=zxPwEnetConformance, zxPwEnetPwIfIndex=zxPwEnetPwIfIndex, zxPwEnetRowStatus=zxPwEnetRowStatus, zxPwEnetPwInstance=zxPwEnetPwInstance, zxPwEnetStdMIB=zxPwEnetStdMIB, zxPwEnetStorageType=zxPwEnetStorageType, zxPwEnetVlanMode=zxPwEnetVlanMode, zxPwEnetPortIfIndex=zxPwEnetPortIfIndex, VlanIdOrAnyOrNone=VlanIdOrAnyOrNone, zxPwEnetPwVlan=zxPwEnetPwVlan, zxPwEnetPortVlan=zxPwEnetPortVlan, zxPwEnetTable=zxPwEnetTable)
