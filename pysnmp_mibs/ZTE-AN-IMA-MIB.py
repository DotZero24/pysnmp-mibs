_Q='zxAnImaLinkId'
_P='ImaFrameLength'
_O='ImaGroupTxClkMode'
_N='ImaGroupSymmetry'
_M='version11'
_L='version10'
_K='zxAnImaGroupIndex'
_J='read-write'
_I='down'
_H='zxAnImaSlot'
_G='zxAnImaShelf'
_F='not-accessible'
_E='ZTE-AN-IMA-MIB'
_D='read-only'
_C='read-create'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
ZxAnIdList,ZxAnIfindex,ZxAnPortList,zxAn=mibBuilder.importSymbols('ZTE-AN-TC-MIB','ZxAnIdList','ZxAnIfindex','ZxAnPortList','zxAn')
zxAnImaMib=ModuleIdentity((1,3,6,1,4,1,3902,1015,1005))
class ImaLinkState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('notInGroup',1),('unusableNoGivenReason',2),('unusableFault',3),('unusableMisconnected',4),('unusableInhibited',5),('unusableFailed',6),('usable',7),('active',8)))
class ImaGroupState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('notConfigured',1),('startUp',2),('startUpAck',3),('configAbortUnsupportedM',4),('configAbortIncompatibleSymmetry',5),('configAbortOther',6),('insufficientLinks',7),('blocked',8),('operational',9),('configAbortUnsupportedImaVersion',10)))
class ImaGroupTxClkMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ctc',1),('itc',2)))
class ImaGroupSymmetry(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('symmetricOperation',1),('asymmetricOperation',2),('asymmetricConfiguration',3)))
class ImaFrameLength(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(32,64,128,256)));namedValues=NamedValues(*(('m32',32),('m64',64),('m128',128),('m256',256)))
_ZxAnImaObjects_ObjectIdentity=ObjectIdentity
zxAnImaObjects=_ZxAnImaObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,1005,1))
_ZxAnImaGroupTable_Object=MibTable
zxAnImaGroupTable=_ZxAnImaGroupTable_Object((1,3,6,1,4,1,3902,1015,1005,1,1))
if mibBuilder.loadTexts:zxAnImaGroupTable.setStatus(_A)
_ZxAnImaGroupEntry_Object=MibTableRow
zxAnImaGroupEntry=_ZxAnImaGroupEntry_Object((1,3,6,1,4,1,3902,1015,1005,1,1,1))
zxAnImaGroupEntry.setIndexNames((0,_E,_G),(0,_E,_H),(0,_E,_K))
if mibBuilder.loadTexts:zxAnImaGroupEntry.setStatus(_A)
_ZxAnImaShelf_Type=Integer32
_ZxAnImaShelf_Object=MibTableColumn
zxAnImaShelf=_ZxAnImaShelf_Object((1,3,6,1,4,1,3902,1015,1005,1,1,1,1),_ZxAnImaShelf_Type())
zxAnImaShelf.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnImaShelf.setStatus(_A)
_ZxAnImaSlot_Type=Integer32
_ZxAnImaSlot_Object=MibTableColumn
zxAnImaSlot=_ZxAnImaSlot_Object((1,3,6,1,4,1,3902,1015,1005,1,1,1,2),_ZxAnImaSlot_Type())
zxAnImaSlot.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnImaSlot.setStatus(_A)
class _ZxAnImaGroupIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_ZxAnImaGroupIndex_Type.__name__=_B
_ZxAnImaGroupIndex_Object=MibTableColumn
zxAnImaGroupIndex=_ZxAnImaGroupIndex_Object((1,3,6,1,4,1,3902,1015,1005,1,1,1,3),_ZxAnImaGroupIndex_Type())
zxAnImaGroupIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnImaGroupIndex.setStatus(_A)
class _ZxAnImaGroupConfImaVersion_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_ZxAnImaGroupConfImaVersion_Type.__name__=_B
_ZxAnImaGroupConfImaVersion_Object=MibTableColumn
zxAnImaGroupConfImaVersion=_ZxAnImaGroupConfImaVersion_Object((1,3,6,1,4,1,3902,1015,1005,1,1,1,4),_ZxAnImaGroupConfImaVersion_Type())
zxAnImaGroupConfImaVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnImaGroupConfImaVersion.setStatus(_A)
class _ZxAnImaGroupActualImaVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_ZxAnImaGroupActualImaVersion_Type.__name__=_B
_ZxAnImaGroupActualImaVersion_Object=MibTableColumn
zxAnImaGroupActualImaVersion=_ZxAnImaGroupActualImaVersion_Object((1,3,6,1,4,1,3902,1015,1005,1,1,1,5),_ZxAnImaGroupActualImaVersion_Type())
zxAnImaGroupActualImaVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnImaGroupActualImaVersion.setStatus(_A)
class _ZxAnImaGroupSymmetry_Type(ImaGroupSymmetry):defaultValue=1
_ZxAnImaGroupSymmetry_Type.__name__=_N
_ZxAnImaGroupSymmetry_Object=MibTableColumn
zxAnImaGroupSymmetry=_ZxAnImaGroupSymmetry_Object((1,3,6,1,4,1,3902,1015,1005,1,1,1,6),_ZxAnImaGroupSymmetry_Type())
zxAnImaGroupSymmetry.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnImaGroupSymmetry.setStatus(_A)
class _ZxAnImaGroupM2SClkMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('master',1),('slave',2)))
_ZxAnImaGroupM2SClkMode_Type.__name__=_B
_ZxAnImaGroupM2SClkMode_Object=MibTableColumn
zxAnImaGroupM2SClkMode=_ZxAnImaGroupM2SClkMode_Object((1,3,6,1,4,1,3902,1015,1005,1,1,1,7),_ZxAnImaGroupM2SClkMode_Type())
zxAnImaGroupM2SClkMode.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnImaGroupM2SClkMode.setStatus(_A)
class _ZxAnImaGroupNeTxClkMode_Type(ImaGroupTxClkMode):defaultValue=1
_ZxAnImaGroupNeTxClkMode_Type.__name__=_O
_ZxAnImaGroupNeTxClkMode_Object=MibTableColumn
zxAnImaGroupNeTxClkMode=_ZxAnImaGroupNeTxClkMode_Object((1,3,6,1,4,1,3902,1015,1005,1,1,1,8),_ZxAnImaGroupNeTxClkMode_Type())
zxAnImaGroupNeTxClkMode.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnImaGroupNeTxClkMode.setStatus(_A)
_ZxAnImaGroupFeTxClkMode_Type=ImaGroupTxClkMode
_ZxAnImaGroupFeTxClkMode_Object=MibTableColumn
zxAnImaGroupFeTxClkMode=_ZxAnImaGroupFeTxClkMode_Object((1,3,6,1,4,1,3902,1015,1005,1,1,1,9),_ZxAnImaGroupFeTxClkMode_Type())
zxAnImaGroupFeTxClkMode.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnImaGroupFeTxClkMode.setStatus(_A)
class _ZxAnImaGroupTxFrameLength_Type(ImaFrameLength):defaultValue=128
_ZxAnImaGroupTxFrameLength_Type.__name__=_P
_ZxAnImaGroupTxFrameLength_Object=MibTableColumn
zxAnImaGroupTxFrameLength=_ZxAnImaGroupTxFrameLength_Object((1,3,6,1,4,1,3902,1015,1005,1,1,1,10),_ZxAnImaGroupTxFrameLength_Type())
zxAnImaGroupTxFrameLength.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnImaGroupTxFrameLength.setStatus(_A)
_ZxAnImaGroupRxFrameLength_Type=ImaFrameLength
_ZxAnImaGroupRxFrameLength_Object=MibTableColumn
zxAnImaGroupRxFrameLength=_ZxAnImaGroupRxFrameLength_Object((1,3,6,1,4,1,3902,1015,1005,1,1,1,11),_ZxAnImaGroupRxFrameLength_Type())
zxAnImaGroupRxFrameLength.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnImaGroupRxFrameLength.setStatus(_A)
class _ZxAnImaGroupAdminStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('up',1),(_I,2),('reset',3)))
_ZxAnImaGroupAdminStatus_Type.__name__=_B
_ZxAnImaGroupAdminStatus_Object=MibTableColumn
zxAnImaGroupAdminStatus=_ZxAnImaGroupAdminStatus_Object((1,3,6,1,4,1,3902,1015,1005,1,1,1,12),_ZxAnImaGroupAdminStatus_Type())
zxAnImaGroupAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnImaGroupAdminStatus.setStatus(_A)
class _ZxAnImaGroupOperstatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),(_I,2)))
_ZxAnImaGroupOperstatus_Type.__name__=_B
_ZxAnImaGroupOperstatus_Object=MibTableColumn
zxAnImaGroupOperstatus=_ZxAnImaGroupOperstatus_Object((1,3,6,1,4,1,3902,1015,1005,1,1,1,13),_ZxAnImaGroupOperstatus_Type())
zxAnImaGroupOperstatus.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnImaGroupOperstatus.setStatus(_A)
_ZxAnImaGroupNeState_Type=ImaGroupState
_ZxAnImaGroupNeState_Object=MibTableColumn
zxAnImaGroupNeState=_ZxAnImaGroupNeState_Object((1,3,6,1,4,1,3902,1015,1005,1,1,1,14),_ZxAnImaGroupNeState_Type())
zxAnImaGroupNeState.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnImaGroupNeState.setStatus(_A)
_ZxAnImaGroupFeState_Type=ImaGroupState
_ZxAnImaGroupFeState_Object=MibTableColumn
zxAnImaGroupFeState=_ZxAnImaGroupFeState_Object((1,3,6,1,4,1,3902,1015,1005,1,1,1,15),_ZxAnImaGroupFeState_Type())
zxAnImaGroupFeState.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnImaGroupFeState.setStatus(_A)
class _ZxAnImaGroupDsx1LineType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(4,6)));namedValues=NamedValues(*(('dsx1E1',4),('dsx1E1MF',6)))
_ZxAnImaGroupDsx1LineType_Type.__name__=_B
_ZxAnImaGroupDsx1LineType_Object=MibTableColumn
zxAnImaGroupDsx1LineType=_ZxAnImaGroupDsx1LineType_Object((1,3,6,1,4,1,3902,1015,1005,1,1,1,16),_ZxAnImaGroupDsx1LineType_Type())
zxAnImaGroupDsx1LineType.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnImaGroupDsx1LineType.setStatus(_A)
class _ZxAnImaGroupDsx1LineCoding_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('singleRail',1),('hdb3',2),('b8zs',3),('ami',4)))
_ZxAnImaGroupDsx1LineCoding_Type.__name__=_B
_ZxAnImaGroupDsx1LineCoding_Object=MibTableColumn
zxAnImaGroupDsx1LineCoding=_ZxAnImaGroupDsx1LineCoding_Object((1,3,6,1,4,1,3902,1015,1005,1,1,1,17),_ZxAnImaGroupDsx1LineCoding_Type())
zxAnImaGroupDsx1LineCoding.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnImaGroupDsx1LineCoding.setStatus(_A)
class _ZxAnImaGroupDsx1TxClockSource_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('loopTiming',1),('localTiming',2)))
_ZxAnImaGroupDsx1TxClockSource_Type.__name__=_B
_ZxAnImaGroupDsx1TxClockSource_Object=MibTableColumn
zxAnImaGroupDsx1TxClockSource=_ZxAnImaGroupDsx1TxClockSource_Object((1,3,6,1,4,1,3902,1015,1005,1,1,1,18),_ZxAnImaGroupDsx1TxClockSource_Type())
zxAnImaGroupDsx1TxClockSource.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnImaGroupDsx1TxClockSource.setStatus(_A)
class _ZxAnImaGroupDsx1IdleCells_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('unassigned',1),('idle',2)))
_ZxAnImaGroupDsx1IdleCells_Type.__name__=_B
_ZxAnImaGroupDsx1IdleCells_Object=MibTableColumn
zxAnImaGroupDsx1IdleCells=_ZxAnImaGroupDsx1IdleCells_Object((1,3,6,1,4,1,3902,1015,1005,1,1,1,19),_ZxAnImaGroupDsx1IdleCells_Type())
zxAnImaGroupDsx1IdleCells.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnImaGroupDsx1IdleCells.setStatus(_A)
class _ZxAnImaGroupDsx1RxScrambling_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('descrambling',1),('noDescrambling',2)))
_ZxAnImaGroupDsx1RxScrambling_Type.__name__=_B
_ZxAnImaGroupDsx1RxScrambling_Object=MibTableColumn
zxAnImaGroupDsx1RxScrambling=_ZxAnImaGroupDsx1RxScrambling_Object((1,3,6,1,4,1,3902,1015,1005,1,1,1,20),_ZxAnImaGroupDsx1RxScrambling_Type())
zxAnImaGroupDsx1RxScrambling.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnImaGroupDsx1RxScrambling.setStatus(_A)
class _ZxAnImaGroupDsx1TxScrambling_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('scrambling',1),('noScrambling',2)))
_ZxAnImaGroupDsx1TxScrambling_Type.__name__=_B
_ZxAnImaGroupDsx1TxScrambling_Object=MibTableColumn
zxAnImaGroupDsx1TxScrambling=_ZxAnImaGroupDsx1TxScrambling_Object((1,3,6,1,4,1,3902,1015,1005,1,1,1,21),_ZxAnImaGroupDsx1TxScrambling_Type())
zxAnImaGroupDsx1TxScrambling.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnImaGroupDsx1TxScrambling.setStatus(_A)
_ZxAnImaGroupRowStatus_Type=RowStatus
_ZxAnImaGroupRowStatus_Object=MibTableColumn
zxAnImaGroupRowStatus=_ZxAnImaGroupRowStatus_Object((1,3,6,1,4,1,3902,1015,1005,1,1,1,22),_ZxAnImaGroupRowStatus_Type())
zxAnImaGroupRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnImaGroupRowStatus.setStatus(_A)
_ZxAnImaLinkTable_Object=MibTable
zxAnImaLinkTable=_ZxAnImaLinkTable_Object((1,3,6,1,4,1,3902,1015,1005,1,2))
if mibBuilder.loadTexts:zxAnImaLinkTable.setStatus(_A)
_ZxAnImaLinkEntry_Object=MibTableRow
zxAnImaLinkEntry=_ZxAnImaLinkEntry_Object((1,3,6,1,4,1,3902,1015,1005,1,2,1))
zxAnImaLinkEntry.setIndexNames((0,_E,_G),(0,_E,_H),(0,_E,_Q))
if mibBuilder.loadTexts:zxAnImaLinkEntry.setStatus(_A)
_ZxAnImaLinkId_Type=Integer32
_ZxAnImaLinkId_Object=MibTableColumn
zxAnImaLinkId=_ZxAnImaLinkId_Object((1,3,6,1,4,1,3902,1015,1005,1,2,1,1),_ZxAnImaLinkId_Type())
zxAnImaLinkId.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnImaLinkId.setStatus(_A)
class _ZxAnImaLinkGroupIndex_Type(Integer32):defaultValue=255
_ZxAnImaLinkGroupIndex_Type.__name__=_B
_ZxAnImaLinkGroupIndex_Object=MibTableColumn
zxAnImaLinkGroupIndex=_ZxAnImaLinkGroupIndex_Object((1,3,6,1,4,1,3902,1015,1005,1,2,1,2),_ZxAnImaLinkGroupIndex_Type())
zxAnImaLinkGroupIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:zxAnImaLinkGroupIndex.setStatus(_A)
class _ZxAnImaLinkNeTxAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),(_I,2)))
_ZxAnImaLinkNeTxAdminStatus_Type.__name__=_B
_ZxAnImaLinkNeTxAdminStatus_Object=MibTableColumn
zxAnImaLinkNeTxAdminStatus=_ZxAnImaLinkNeTxAdminStatus_Object((1,3,6,1,4,1,3902,1015,1005,1,2,1,3),_ZxAnImaLinkNeTxAdminStatus_Type())
zxAnImaLinkNeTxAdminStatus.setMaxAccess(_J)
if mibBuilder.loadTexts:zxAnImaLinkNeTxAdminStatus.setStatus(_A)
_ZxAnImaLinkNeRxState_Type=ImaLinkState
_ZxAnImaLinkNeRxState_Object=MibTableColumn
zxAnImaLinkNeRxState=_ZxAnImaLinkNeRxState_Object((1,3,6,1,4,1,3902,1015,1005,1,2,1,4),_ZxAnImaLinkNeRxState_Type())
zxAnImaLinkNeRxState.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnImaLinkNeRxState.setStatus(_A)
_ZxAnImaLinkNeTxState_Type=ImaLinkState
_ZxAnImaLinkNeTxState_Object=MibTableColumn
zxAnImaLinkNeTxState=_ZxAnImaLinkNeTxState_Object((1,3,6,1,4,1,3902,1015,1005,1,2,1,5),_ZxAnImaLinkNeTxState_Type())
zxAnImaLinkNeTxState.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnImaLinkNeTxState.setStatus(_A)
_ZxAnImaLinkFeRxState_Type=ImaLinkState
_ZxAnImaLinkFeRxState_Object=MibTableColumn
zxAnImaLinkFeRxState=_ZxAnImaLinkFeRxState_Object((1,3,6,1,4,1,3902,1015,1005,1,2,1,6),_ZxAnImaLinkFeRxState_Type())
zxAnImaLinkFeRxState.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnImaLinkFeRxState.setStatus(_A)
_ZxAnImaLinkFeTxState_Type=ImaLinkState
_ZxAnImaLinkFeTxState_Object=MibTableColumn
zxAnImaLinkFeTxState=_ZxAnImaLinkFeTxState_Object((1,3,6,1,4,1,3902,1015,1005,1,2,1,7),_ZxAnImaLinkFeTxState_Type())
zxAnImaLinkFeTxState.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnImaLinkFeTxState.setStatus(_A)
class _ZxAnImaLinkLoopback_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_ZxAnImaLinkLoopback_Type.__name__=_B
_ZxAnImaLinkLoopback_Object=MibTableColumn
zxAnImaLinkLoopback=_ZxAnImaLinkLoopback_Object((1,3,6,1,4,1,3902,1015,1005,1,2,1,8),_ZxAnImaLinkLoopback_Type())
zxAnImaLinkLoopback.setMaxAccess(_J)
if mibBuilder.loadTexts:zxAnImaLinkLoopback.setStatus(_A)
_ZxAnImaTrapObjects_ObjectIdentity=ObjectIdentity
zxAnImaTrapObjects=_ZxAnImaTrapObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,1005,2))
mibBuilder.exportSymbols(_E,**{'ImaLinkState':ImaLinkState,'ImaGroupState':ImaGroupState,_O:ImaGroupTxClkMode,_N:ImaGroupSymmetry,_P:ImaFrameLength,'zxAnImaMib':zxAnImaMib,'zxAnImaObjects':zxAnImaObjects,'zxAnImaGroupTable':zxAnImaGroupTable,'zxAnImaGroupEntry':zxAnImaGroupEntry,_G:zxAnImaShelf,_H:zxAnImaSlot,_K:zxAnImaGroupIndex,'zxAnImaGroupConfImaVersion':zxAnImaGroupConfImaVersion,'zxAnImaGroupActualImaVersion':zxAnImaGroupActualImaVersion,'zxAnImaGroupSymmetry':zxAnImaGroupSymmetry,'zxAnImaGroupM2SClkMode':zxAnImaGroupM2SClkMode,'zxAnImaGroupNeTxClkMode':zxAnImaGroupNeTxClkMode,'zxAnImaGroupFeTxClkMode':zxAnImaGroupFeTxClkMode,'zxAnImaGroupTxFrameLength':zxAnImaGroupTxFrameLength,'zxAnImaGroupRxFrameLength':zxAnImaGroupRxFrameLength,'zxAnImaGroupAdminStatus':zxAnImaGroupAdminStatus,'zxAnImaGroupOperstatus':zxAnImaGroupOperstatus,'zxAnImaGroupNeState':zxAnImaGroupNeState,'zxAnImaGroupFeState':zxAnImaGroupFeState,'zxAnImaGroupDsx1LineType':zxAnImaGroupDsx1LineType,'zxAnImaGroupDsx1LineCoding':zxAnImaGroupDsx1LineCoding,'zxAnImaGroupDsx1TxClockSource':zxAnImaGroupDsx1TxClockSource,'zxAnImaGroupDsx1IdleCells':zxAnImaGroupDsx1IdleCells,'zxAnImaGroupDsx1RxScrambling':zxAnImaGroupDsx1RxScrambling,'zxAnImaGroupDsx1TxScrambling':zxAnImaGroupDsx1TxScrambling,'zxAnImaGroupRowStatus':zxAnImaGroupRowStatus,'zxAnImaLinkTable':zxAnImaLinkTable,'zxAnImaLinkEntry':zxAnImaLinkEntry,_Q:zxAnImaLinkId,'zxAnImaLinkGroupIndex':zxAnImaLinkGroupIndex,'zxAnImaLinkNeTxAdminStatus':zxAnImaLinkNeTxAdminStatus,'zxAnImaLinkNeRxState':zxAnImaLinkNeRxState,'zxAnImaLinkNeTxState':zxAnImaLinkNeTxState,'zxAnImaLinkFeRxState':zxAnImaLinkFeRxState,'zxAnImaLinkFeTxState':zxAnImaLinkFeTxState,'zxAnImaLinkLoopback':zxAnImaLinkLoopback,'zxAnImaTrapObjects':zxAnImaTrapObjects})