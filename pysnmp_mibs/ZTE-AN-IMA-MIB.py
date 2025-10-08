#
# PySNMP MIB module ZTE-AN-IMA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/zte/ZTE-AN-IMA-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:10:20 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
zxAn, ZxAnIfindex, ZxAnPortList, ZxAnIdList = mibBuilder.importSymbols("ZTE-AN-TC-MIB", "zxAn", "ZxAnIfindex", "ZxAnPortList", "ZxAnIdList")
zxAnImaMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 3902, 1015, 1005))
if mibBuilder.loadTexts: zxAnImaMib.setLastUpdated('200707101130Z')
if mibBuilder.loadTexts: zxAnImaMib.setOrganization('ZTE Corporation')
zxAnImaObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 1015, 1005, 1))
zxAnImaTrapObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 1015, 1005, 2))
class ImaLinkState(TextualConvention, Integer32):
    reference = 'ATM Forum IMA v1.1, Section 10.1.2 on page 48'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("notInGroup", 1), ("unusableNoGivenReason", 2), ("unusableFault", 3), ("unusableMisconnected", 4), ("unusableInhibited", 5), ("unusableFailed", 6), ("usable", 7), ("active", 8))

class ImaGroupState(TextualConvention, Integer32):
    reference = 'ATM Forum IMA v1.1, Section 10.2.1 on page 55'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    namedValues = NamedValues(("notConfigured", 1), ("startUp", 2), ("startUpAck", 3), ("configAbortUnsupportedM", 4), ("configAbortIncompatibleSymmetry", 5), ("configAbortOther", 6), ("insufficientLinks", 7), ("blocked", 8), ("operational", 9), ("configAbortUnsupportedImaVersion", 10))

class ImaGroupTxClkMode(TextualConvention, Integer32):
    reference = 'ATM Forum IMA v1.1, Section 7 on page 38'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("ctc", 1), ("itc", 2))

class ImaGroupSymmetry(TextualConvention, Integer32):
    reference = 'ATM Forum IMA v1.1, Section 5.2.2.7 on page 35'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("symmetricOperation", 1), ("asymmetricOperation", 2), ("asymmetricConfiguration", 3))

class ImaFrameLength(TextualConvention, Integer32):
    reference = 'ATM Forum IMA v1.1, Section 5.2.2.4.2 on page 34'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(32, 64, 128, 256))
    namedValues = NamedValues(("m32", 32), ("m64", 64), ("m128", 128), ("m256", 256))

zxAnImaGroupTable = MibTable((1, 3, 6, 1, 4, 1, 3902, 1015, 1005, 1, 1), )
if mibBuilder.loadTexts: zxAnImaGroupTable.setStatus('current')
zxAnImaGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3902, 1015, 1005, 1, 1, 1), ).setIndexNames((0, "ZTE-AN-IMA-MIB", "zxAnImaShelf"), (0, "ZTE-AN-IMA-MIB", "zxAnImaSlot"), (0, "ZTE-AN-IMA-MIB", "zxAnImaGroupIndex"))
if mibBuilder.loadTexts: zxAnImaGroupEntry.setStatus('current')
zxAnImaShelf = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 1005, 1, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: zxAnImaShelf.setStatus('current')
zxAnImaSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 1005, 1, 1, 1, 2), Integer32())
if mibBuilder.loadTexts: zxAnImaSlot.setStatus('current')
zxAnImaGroupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 1005, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15)))
if mibBuilder.loadTexts: zxAnImaGroupIndex.setStatus('current')
zxAnImaGroupConfImaVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 1005, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("version10", 1), ("version11", 2))).clone('version11')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxAnImaGroupConfImaVersion.setStatus('current')
zxAnImaGroupActualImaVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 1005, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("version10", 1), ("version11", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxAnImaGroupActualImaVersion.setStatus('current')
zxAnImaGroupSymmetry = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 1005, 1, 1, 1, 6), ImaGroupSymmetry().clone('symmetricOperation')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxAnImaGroupSymmetry.setStatus('current')
zxAnImaGroupM2SClkMode = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 1005, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("master", 1), ("slave", 2))).clone('master')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxAnImaGroupM2SClkMode.setStatus('current')
zxAnImaGroupNeTxClkMode = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 1005, 1, 1, 1, 8), ImaGroupTxClkMode().clone('ctc')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxAnImaGroupNeTxClkMode.setStatus('current')
zxAnImaGroupFeTxClkMode = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 1005, 1, 1, 1, 9), ImaGroupTxClkMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxAnImaGroupFeTxClkMode.setStatus('current')
zxAnImaGroupTxFrameLength = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 1005, 1, 1, 1, 10), ImaFrameLength().clone('m128')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxAnImaGroupTxFrameLength.setStatus('current')
zxAnImaGroupRxFrameLength = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 1005, 1, 1, 1, 11), ImaFrameLength()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxAnImaGroupRxFrameLength.setStatus('current')
zxAnImaGroupAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 1005, 1, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("reset", 3))).clone('up')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxAnImaGroupAdminStatus.setStatus('current')
zxAnImaGroupOperstatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 1005, 1, 1, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxAnImaGroupOperstatus.setStatus('current')
zxAnImaGroupNeState = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 1005, 1, 1, 1, 14), ImaGroupState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxAnImaGroupNeState.setStatus('current')
zxAnImaGroupFeState = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 1005, 1, 1, 1, 15), ImaGroupState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxAnImaGroupFeState.setStatus('current')
zxAnImaGroupDsx1LineType = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 1005, 1, 1, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(4, 6))).clone(namedValues=NamedValues(("dsx1E1", 4), ("dsx1E1MF", 6)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxAnImaGroupDsx1LineType.setStatus('current')
zxAnImaGroupDsx1LineCoding = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 1005, 1, 1, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("singleRail", 1), ("hdb3", 2), ("b8zs", 3), ("ami", 4))).clone('hdb3')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxAnImaGroupDsx1LineCoding.setStatus('current')
zxAnImaGroupDsx1TxClockSource = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 1005, 1, 1, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("loopTiming", 1), ("localTiming", 2))).clone('localTiming')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxAnImaGroupDsx1TxClockSource.setStatus('current')
zxAnImaGroupDsx1IdleCells = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 1005, 1, 1, 1, 19), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("unassigned", 1), ("idle", 2))).clone('unassigned')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxAnImaGroupDsx1IdleCells.setStatus('current')
zxAnImaGroupDsx1RxScrambling = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 1005, 1, 1, 1, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("descrambling", 1), ("noDescrambling", 2))).clone('noDescrambling')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxAnImaGroupDsx1RxScrambling.setStatus('current')
zxAnImaGroupDsx1TxScrambling = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 1005, 1, 1, 1, 21), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("scrambling", 1), ("noScrambling", 2))).clone('noScrambling')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxAnImaGroupDsx1TxScrambling.setStatus('current')
zxAnImaGroupRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 1005, 1, 1, 1, 22), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxAnImaGroupRowStatus.setStatus('current')
zxAnImaLinkTable = MibTable((1, 3, 6, 1, 4, 1, 3902, 1015, 1005, 1, 2), )
if mibBuilder.loadTexts: zxAnImaLinkTable.setStatus('current')
zxAnImaLinkEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3902, 1015, 1005, 1, 2, 1), ).setIndexNames((0, "ZTE-AN-IMA-MIB", "zxAnImaShelf"), (0, "ZTE-AN-IMA-MIB", "zxAnImaSlot"), (0, "ZTE-AN-IMA-MIB", "zxAnImaLinkId"))
if mibBuilder.loadTexts: zxAnImaLinkEntry.setStatus('current')
zxAnImaLinkId = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 1005, 1, 2, 1, 1), Integer32())
if mibBuilder.loadTexts: zxAnImaLinkId.setStatus('current')
zxAnImaLinkGroupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 1005, 1, 2, 1, 2), Integer32().clone(255)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zxAnImaLinkGroupIndex.setStatus('current')
zxAnImaLinkNeTxAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 1005, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zxAnImaLinkNeTxAdminStatus.setStatus('current')
zxAnImaLinkNeRxState = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 1005, 1, 2, 1, 4), ImaLinkState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxAnImaLinkNeRxState.setStatus('current')
zxAnImaLinkNeTxState = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 1005, 1, 2, 1, 5), ImaLinkState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxAnImaLinkNeTxState.setStatus('current')
zxAnImaLinkFeRxState = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 1005, 1, 2, 1, 6), ImaLinkState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxAnImaLinkFeRxState.setStatus('current')
zxAnImaLinkFeTxState = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 1005, 1, 2, 1, 7), ImaLinkState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxAnImaLinkFeTxState.setStatus('current')
zxAnImaLinkLoopback = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 1005, 1, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zxAnImaLinkLoopback.setStatus('current')
mibBuilder.exportSymbols("ZTE-AN-IMA-MIB", zxAnImaGroupRxFrameLength=zxAnImaGroupRxFrameLength, zxAnImaGroupActualImaVersion=zxAnImaGroupActualImaVersion, zxAnImaGroupDsx1RxScrambling=zxAnImaGroupDsx1RxScrambling, ImaGroupSymmetry=ImaGroupSymmetry, zxAnImaLinkFeRxState=zxAnImaLinkFeRxState, ImaLinkState=ImaLinkState, ImaFrameLength=ImaFrameLength, zxAnImaLinkEntry=zxAnImaLinkEntry, ImaGroupTxClkMode=ImaGroupTxClkMode, zxAnImaLinkNeTxState=zxAnImaLinkNeTxState, zxAnImaGroupDsx1TxScrambling=zxAnImaGroupDsx1TxScrambling, zxAnImaGroupTxFrameLength=zxAnImaGroupTxFrameLength, zxAnImaLinkFeTxState=zxAnImaLinkFeTxState, zxAnImaGroupAdminStatus=zxAnImaGroupAdminStatus, zxAnImaLinkGroupIndex=zxAnImaLinkGroupIndex, zxAnImaLinkLoopback=zxAnImaLinkLoopback, zxAnImaGroupSymmetry=zxAnImaGroupSymmetry, PYSNMP_MODULE_ID=zxAnImaMib, zxAnImaObjects=zxAnImaObjects, zxAnImaGroupDsx1IdleCells=zxAnImaGroupDsx1IdleCells, zxAnImaGroupFeTxClkMode=zxAnImaGroupFeTxClkMode, zxAnImaLinkTable=zxAnImaLinkTable, zxAnImaGroupNeTxClkMode=zxAnImaGroupNeTxClkMode, zxAnImaGroupEntry=zxAnImaGroupEntry, zxAnImaGroupConfImaVersion=zxAnImaGroupConfImaVersion, zxAnImaGroupDsx1LineType=zxAnImaGroupDsx1LineType, zxAnImaGroupNeState=zxAnImaGroupNeState, zxAnImaLinkNeTxAdminStatus=zxAnImaLinkNeTxAdminStatus, zxAnImaTrapObjects=zxAnImaTrapObjects, zxAnImaMib=zxAnImaMib, zxAnImaGroupOperstatus=zxAnImaGroupOperstatus, zxAnImaGroupDsx1TxClockSource=zxAnImaGroupDsx1TxClockSource, zxAnImaGroupTable=zxAnImaGroupTable, zxAnImaLinkId=zxAnImaLinkId, zxAnImaShelf=zxAnImaShelf, zxAnImaGroupIndex=zxAnImaGroupIndex, zxAnImaGroupRowStatus=zxAnImaGroupRowStatus, zxAnImaGroupFeState=zxAnImaGroupFeState, zxAnImaLinkNeRxState=zxAnImaLinkNeRxState, zxAnImaSlot=zxAnImaSlot, zxAnImaGroupDsx1LineCoding=zxAnImaGroupDsx1LineCoding, zxAnImaGroupM2SClkMode=zxAnImaGroupM2SClkMode, ImaGroupState=ImaGroupState)
