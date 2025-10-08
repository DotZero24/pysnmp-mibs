#
# PySNMP MIB module ZTE-DSL-IMA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/zte/ZTE-DSL-IMA-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:10:25 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
zxDslImaMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 3902, 1004, 30))
if mibBuilder.loadTexts: zxDslImaMib.setLastUpdated('200702141500Z')
if mibBuilder.loadTexts: zxDslImaMib.setOrganization('ZTE Corporation')
zte = MibIdentifier((1, 3, 6, 1, 4, 1, 3902))
zxDsl = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 1004))
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

zxDslImaGroupTable = MibTable((1, 3, 6, 1, 4, 1, 3902, 1004, 30, 1), )
if mibBuilder.loadTexts: zxDslImaGroupTable.setStatus('current')
zxDslImaGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3902, 1004, 30, 1, 1), ).setIndexNames((0, "ZTE-DSL-IMA-MIB", "zxDslImaGroupIfIndex"))
if mibBuilder.loadTexts: zxDslImaGroupEntry.setStatus('current')
zxDslImaGroupIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1004, 30, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: zxDslImaGroupIfIndex.setStatus('current')
zxDslImaGroupConfImaVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1004, 30, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("version10", 1), ("version11", 2))).clone('version11')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxDslImaGroupConfImaVersion.setStatus('current')
zxDslImaGroupActualImaVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1004, 30, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("version10", 1), ("version11", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxDslImaGroupActualImaVersion.setStatus('current')
zxDslImaGroupSymmetry = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1004, 30, 1, 1, 4), ImaGroupSymmetry().clone('symmetricOperation')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxDslImaGroupSymmetry.setStatus('current')
zxDslImaGroupM2SClkMode = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1004, 30, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("master", 1), ("slave", 2))).clone('master')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxDslImaGroupM2SClkMode.setStatus('current')
zxDslImaGroupNeTxClkMode = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1004, 30, 1, 1, 6), ImaGroupTxClkMode().clone('ctc')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxDslImaGroupNeTxClkMode.setStatus('current')
zxDslImaGroupFeTxClkMode = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1004, 30, 1, 1, 7), ImaGroupTxClkMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxDslImaGroupFeTxClkMode.setStatus('current')
zxDslImaGroupTxFrameLength = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1004, 30, 1, 1, 8), ImaFrameLength().clone('m128')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxDslImaGroupTxFrameLength.setStatus('current')
zxDslImaGroupRxFrameLength = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1004, 30, 1, 1, 9), ImaFrameLength()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxDslImaGroupRxFrameLength.setStatus('current')
zxDslImaGroupAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1004, 30, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("reset", 3))).clone('up')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxDslImaGroupAdminStatus.setStatus('current')
zxDslImaGroupOperstatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1004, 30, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxDslImaGroupOperstatus.setStatus('current')
zxDslImaGroupNeState = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1004, 30, 1, 1, 12), ImaGroupState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxDslImaGroupNeState.setStatus('current')
zxDslImaGroupFeState = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1004, 30, 1, 1, 13), ImaGroupState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxDslImaGroupFeState.setStatus('current')
zxDslImaGroupDsx1LineType = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1004, 30, 1, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(4, 6))).clone(namedValues=NamedValues(("dsx1E1", 4), ("dsx1E1MF", 6)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxDslImaGroupDsx1LineType.setStatus('current')
zxDslImaGroupDsx1LineCoding = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1004, 30, 1, 1, 15), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxDslImaGroupDsx1LineCoding.setStatus('current')
zxDslImaGroupDsx1TxClockSource = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1004, 30, 1, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("loopTiming", 1), ("localTiming", 2))).clone(2)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxDslImaGroupDsx1TxClockSource.setStatus('current')
zxDslImaGroupDsx1IdleCells = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1004, 30, 1, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("unassigned", 1), ("idle", 2))).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxDslImaGroupDsx1IdleCells.setStatus('current')
zxDslImaGroupDsx1RxScrambling = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1004, 30, 1, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("descrambling", 1), ("noDescrambling", 2))).clone('noDescrambling')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxDslImaGroupDsx1RxScrambling.setStatus('current')
zxDslImaGroupDsx1TxScrambling = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1004, 30, 1, 1, 19), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("scrambling", 1), ("noScrambling", 2))).clone('noScrambling')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxDslImaGroupDsx1TxScrambling.setStatus('current')
zxDslImaGroupRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1004, 30, 1, 1, 20), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxDslImaGroupRowStatus.setStatus('current')
zxDslImaLinkTable = MibTable((1, 3, 6, 1, 4, 1, 3902, 1004, 30, 2), )
if mibBuilder.loadTexts: zxDslImaLinkTable.setStatus('current')
zxDslImaLinkEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3902, 1004, 30, 2, 1), ).setIndexNames((0, "ZTE-DSL-IMA-MIB", "zxDslImaSlot"), (0, "ZTE-DSL-IMA-MIB", "zxDslImaLinkId"))
if mibBuilder.loadTexts: zxDslImaLinkEntry.setStatus('current')
zxDslImaSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1004, 30, 2, 1, 1), Integer32())
if mibBuilder.loadTexts: zxDslImaSlot.setStatus('current')
zxDslImaLinkId = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1004, 30, 2, 1, 2), Integer32())
if mibBuilder.loadTexts: zxDslImaLinkId.setStatus('current')
zxDslImaLinkGroupIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1004, 30, 2, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zxDslImaLinkGroupIfIndex.setStatus('current')
zxDslImaLinkNeTxAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1004, 30, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zxDslImaLinkNeTxAdminStatus.setStatus('current')
zxDslImaLinkNeRxAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1004, 30, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zxDslImaLinkNeRxAdminStatus.setStatus('current')
zxDslImaLinkNeRxState = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1004, 30, 2, 1, 8), ImaLinkState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxDslImaLinkNeRxState.setStatus('current')
zxDslImaLinkNeTxState = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1004, 30, 2, 1, 9), ImaLinkState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxDslImaLinkNeTxState.setStatus('current')
zxDslImaLinkFeRxState = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1004, 30, 2, 1, 10), ImaLinkState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxDslImaLinkFeRxState.setStatus('current')
zxDslImaLinkFeTxState = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1004, 30, 2, 1, 11), ImaLinkState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxDslImaLinkFeTxState.setStatus('current')
mibBuilder.exportSymbols("ZTE-DSL-IMA-MIB", zxDslImaGroupDsx1LineCoding=zxDslImaGroupDsx1LineCoding, zxDslImaGroupFeTxClkMode=zxDslImaGroupFeTxClkMode, zxDslImaSlot=zxDslImaSlot, zxDslImaGroupActualImaVersion=zxDslImaGroupActualImaVersion, ImaGroupSymmetry=ImaGroupSymmetry, zxDslImaGroupOperstatus=zxDslImaGroupOperstatus, zxDslImaGroupDsx1RxScrambling=zxDslImaGroupDsx1RxScrambling, zxDslImaGroupRowStatus=zxDslImaGroupRowStatus, zxDslImaMib=zxDslImaMib, ImaLinkState=ImaLinkState, ImaFrameLength=ImaFrameLength, zxDsl=zxDsl, ImaGroupTxClkMode=ImaGroupTxClkMode, zxDslImaGroupDsx1LineType=zxDslImaGroupDsx1LineType, zxDslImaLinkNeTxAdminStatus=zxDslImaLinkNeTxAdminStatus, zxDslImaGroupAdminStatus=zxDslImaGroupAdminStatus, zxDslImaLinkEntry=zxDslImaLinkEntry, zxDslImaGroupIfIndex=zxDslImaGroupIfIndex, zxDslImaLinkNeRxState=zxDslImaLinkNeRxState, zxDslImaGroupSymmetry=zxDslImaGroupSymmetry, zxDslImaLinkGroupIfIndex=zxDslImaLinkGroupIfIndex, zxDslImaLinkFeRxState=zxDslImaLinkFeRxState, zxDslImaGroupNeTxClkMode=zxDslImaGroupNeTxClkMode, zxDslImaGroupNeState=zxDslImaGroupNeState, zxDslImaGroupEntry=zxDslImaGroupEntry, zxDslImaLinkFeTxState=zxDslImaLinkFeTxState, zxDslImaGroupRxFrameLength=zxDslImaGroupRxFrameLength, zxDslImaGroupTable=zxDslImaGroupTable, zxDslImaGroupM2SClkMode=zxDslImaGroupM2SClkMode, zxDslImaLinkNeRxAdminStatus=zxDslImaLinkNeRxAdminStatus, zte=zte, zxDslImaLinkNeTxState=zxDslImaLinkNeTxState, zxDslImaGroupTxFrameLength=zxDslImaGroupTxFrameLength, zxDslImaGroupDsx1TxClockSource=zxDslImaGroupDsx1TxClockSource, PYSNMP_MODULE_ID=zxDslImaMib, zxDslImaLinkTable=zxDslImaLinkTable, zxDslImaGroupDsx1IdleCells=zxDslImaGroupDsx1IdleCells, zxDslImaGroupFeState=zxDslImaGroupFeState, zxDslImaGroupConfImaVersion=zxDslImaGroupConfImaVersion, zxDslImaGroupDsx1TxScrambling=zxDslImaGroupDsx1TxScrambling, zxDslImaLinkId=zxDslImaLinkId, ImaGroupState=ImaGroupState)
