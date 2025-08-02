_Z='ipadPPPStartAuthFailureCount'
_Y='ipadPPPStartIPCPHistoryIndex'
_X='ipadPPPStartAuthHistoryIndex'
_W='ipadPPPStartLCPHistoryIndex'
_V='ipadPPPStartService'
_U='DisplayString'
_T='disabled'
_S='enabled'
_R='other'
_Q='unknown'
_P='ipadServiceIndex'
_O='IPADv2-MIB'
_N='opened'
_M='ackSent'
_L='ackRcvd'
_K='reqSent'
_J='stopping'
_I='closing'
_H='stopped'
_G='closed'
_F='starting'
_E='initial'
_D='IPAD-IPSTART-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ipadPPP,ipadServiceIndex,ipadTrapsPrefix=mibBuilder.importSymbols(_O,'ipadPPP',_P,'ipadTrapsPrefix')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_U,'PhysAddress','TextualConvention')
ipadIPStart=ModuleIdentity((1,3,6,1,4,1,321,100,1,7,4))
_IpadPPPStartTable_Object=MibTable
ipadPPPStartTable=_IpadPPPStartTable_Object((1,3,6,1,4,1,321,100,1,7,4,1))
if mibBuilder.loadTexts:ipadPPPStartTable.setStatus(_A)
_IpadPPPStartTableEntry_Object=MibTableRow
ipadPPPStartTableEntry=_IpadPPPStartTableEntry_Object((1,3,6,1,4,1,321,100,1,7,4,1,1))
ipadPPPStartTableEntry.setIndexNames((0,_D,_V))
if mibBuilder.loadTexts:ipadPPPStartTableEntry.setStatus(_A)
_IpadPPPStartService_Type=Integer32
_IpadPPPStartService_Object=MibTableColumn
ipadPPPStartService=_IpadPPPStartService_Object((1,3,6,1,4,1,321,100,1,7,4,1,1,1),_IpadPPPStartService_Type())
ipadPPPStartService.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadPPPStartService.setStatus(_A)
class _IpadPPPStartLCPState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3),(_H,4),(_I,5),(_J,6),(_K,7),(_L,8),(_M,9),(_N,10)))
_IpadPPPStartLCPState_Type.__name__=_C
_IpadPPPStartLCPState_Object=MibTableColumn
ipadPPPStartLCPState=_IpadPPPStartLCPState_Object((1,3,6,1,4,1,321,100,1,7,4,1,1,2),_IpadPPPStartLCPState_Type())
ipadPPPStartLCPState.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadPPPStartLCPState.setStatus(_A)
_IpadPPPStartLCPStateTime_Type=Integer32
_IpadPPPStartLCPStateTime_Object=MibTableColumn
ipadPPPStartLCPStateTime=_IpadPPPStartLCPStateTime_Object((1,3,6,1,4,1,321,100,1,7,4,1,1,3),_IpadPPPStartLCPStateTime_Type())
ipadPPPStartLCPStateTime.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadPPPStartLCPStateTime.setStatus(_A)
_IpadPPPStartLCPStateChanges_Type=Integer32
_IpadPPPStartLCPStateChanges_Object=MibTableColumn
ipadPPPStartLCPStateChanges=_IpadPPPStartLCPStateChanges_Object((1,3,6,1,4,1,321,100,1,7,4,1,1,4),_IpadPPPStartLCPStateChanges_Type())
ipadPPPStartLCPStateChanges.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadPPPStartLCPStateChanges.setStatus(_A)
_IpadPPPStartLCPMRU_Type=Integer32
_IpadPPPStartLCPMRU_Object=MibTableColumn
ipadPPPStartLCPMRU=_IpadPPPStartLCPMRU_Object((1,3,6,1,4,1,321,100,1,7,4,1,1,5),_IpadPPPStartLCPMRU_Type())
ipadPPPStartLCPMRU.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadPPPStartLCPMRU.setStatus(_A)
class _IpadPPPStartLCPAsyncCCM_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_IpadPPPStartLCPAsyncCCM_Type.__name__=_U
_IpadPPPStartLCPAsyncCCM_Object=MibTableColumn
ipadPPPStartLCPAsyncCCM=_IpadPPPStartLCPAsyncCCM_Object((1,3,6,1,4,1,321,100,1,7,4,1,1,6),_IpadPPPStartLCPAsyncCCM_Type())
ipadPPPStartLCPAsyncCCM.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadPPPStartLCPAsyncCCM.setStatus(_A)
class _IpadPPPStartLCPAuthProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_Q,1),(_R,2),('pap',3),('chap',4),('spap',5),('eap',6)))
_IpadPPPStartLCPAuthProtocol_Type.__name__=_C
_IpadPPPStartLCPAuthProtocol_Object=MibTableColumn
ipadPPPStartLCPAuthProtocol=_IpadPPPStartLCPAuthProtocol_Object((1,3,6,1,4,1,321,100,1,7,4,1,1,7),_IpadPPPStartLCPAuthProtocol_Type())
ipadPPPStartLCPAuthProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadPPPStartLCPAuthProtocol.setStatus(_A)
class _IpadPPPStartLCPQualityProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_Q,1),(_R,2),('lqr',3)))
_IpadPPPStartLCPQualityProtocol_Type.__name__=_C
_IpadPPPStartLCPQualityProtocol_Object=MibTableColumn
ipadPPPStartLCPQualityProtocol=_IpadPPPStartLCPQualityProtocol_Object((1,3,6,1,4,1,321,100,1,7,4,1,1,8),_IpadPPPStartLCPQualityProtocol_Type())
ipadPPPStartLCPQualityProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadPPPStartLCPQualityProtocol.setStatus(_A)
class _IpadPPPStartLCPMagicNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_IpadPPPStartLCPMagicNumber_Type.__name__=_U
_IpadPPPStartLCPMagicNumber_Object=MibTableColumn
ipadPPPStartLCPMagicNumber=_IpadPPPStartLCPMagicNumber_Object((1,3,6,1,4,1,321,100,1,7,4,1,1,9),_IpadPPPStartLCPMagicNumber_Type())
ipadPPPStartLCPMagicNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadPPPStartLCPMagicNumber.setStatus(_A)
class _IpadPPPStartLCPPFC_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_S,1),(_T,2)))
_IpadPPPStartLCPPFC_Type.__name__=_C
_IpadPPPStartLCPPFC_Object=MibTableColumn
ipadPPPStartLCPPFC=_IpadPPPStartLCPPFC_Object((1,3,6,1,4,1,321,100,1,7,4,1,1,10),_IpadPPPStartLCPPFC_Type())
ipadPPPStartLCPPFC.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadPPPStartLCPPFC.setStatus(_A)
class _IpadPPPStartLCPACFC_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_S,1),(_T,2)))
_IpadPPPStartLCPACFC_Type.__name__=_C
_IpadPPPStartLCPACFC_Object=MibTableColumn
ipadPPPStartLCPACFC=_IpadPPPStartLCPACFC_Object((1,3,6,1,4,1,321,100,1,7,4,1,1,11),_IpadPPPStartLCPACFC_Type())
ipadPPPStartLCPACFC.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadPPPStartLCPACFC.setStatus(_A)
class _IpadPPPStartLCPFCSAlternatives_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_Q,1),(_R,2),('nullFCS',3),('ccitt16bitFCS',4),('ccitt32bitFCS',5)))
_IpadPPPStartLCPFCSAlternatives_Type.__name__=_C
_IpadPPPStartLCPFCSAlternatives_Object=MibTableColumn
ipadPPPStartLCPFCSAlternatives=_IpadPPPStartLCPFCSAlternatives_Object((1,3,6,1,4,1,321,100,1,7,4,1,1,12),_IpadPPPStartLCPFCSAlternatives_Type())
ipadPPPStartLCPFCSAlternatives.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadPPPStartLCPFCSAlternatives.setStatus(_A)
_IpadPPPStartLCPSDP_Type=Integer32
_IpadPPPStartLCPSDP_Object=MibTableColumn
ipadPPPStartLCPSDP=_IpadPPPStartLCPSDP_Object((1,3,6,1,4,1,321,100,1,7,4,1,1,13),_IpadPPPStartLCPSDP_Type())
ipadPPPStartLCPSDP.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadPPPStartLCPSDP.setStatus(_A)
class _IpadPPPStartLCPCompoundFrames_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_S,1),(_T,2)))
_IpadPPPStartLCPCompoundFrames_Type.__name__=_C
_IpadPPPStartLCPCompoundFrames_Object=MibTableColumn
ipadPPPStartLCPCompoundFrames=_IpadPPPStartLCPCompoundFrames_Object((1,3,6,1,4,1,321,100,1,7,4,1,1,14),_IpadPPPStartLCPCompoundFrames_Type())
ipadPPPStartLCPCompoundFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadPPPStartLCPCompoundFrames.setStatus(_A)
class _IpadPPPStartAuthState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3),(_H,4),(_I,5),(_J,6),(_K,7),(_L,8),(_M,9),(_N,10)))
_IpadPPPStartAuthState_Type.__name__=_C
_IpadPPPStartAuthState_Object=MibTableColumn
ipadPPPStartAuthState=_IpadPPPStartAuthState_Object((1,3,6,1,4,1,321,100,1,7,4,1,1,15),_IpadPPPStartAuthState_Type())
ipadPPPStartAuthState.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadPPPStartAuthState.setStatus(_A)
_IpadPPPStartAuthStateTime_Type=Integer32
_IpadPPPStartAuthStateTime_Object=MibTableColumn
ipadPPPStartAuthStateTime=_IpadPPPStartAuthStateTime_Object((1,3,6,1,4,1,321,100,1,7,4,1,1,16),_IpadPPPStartAuthStateTime_Type())
ipadPPPStartAuthStateTime.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadPPPStartAuthStateTime.setStatus(_A)
_IpadPPPStartAuthStateChanges_Type=Integer32
_IpadPPPStartAuthStateChanges_Object=MibTableColumn
ipadPPPStartAuthStateChanges=_IpadPPPStartAuthStateChanges_Object((1,3,6,1,4,1,321,100,1,7,4,1,1,17),_IpadPPPStartAuthStateChanges_Type())
ipadPPPStartAuthStateChanges.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadPPPStartAuthStateChanges.setStatus(_A)
_IpadPPPStartAuthFailureCount_Type=Integer32
_IpadPPPStartAuthFailureCount_Object=MibTableColumn
ipadPPPStartAuthFailureCount=_IpadPPPStartAuthFailureCount_Object((1,3,6,1,4,1,321,100,1,7,4,1,1,18),_IpadPPPStartAuthFailureCount_Type())
ipadPPPStartAuthFailureCount.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadPPPStartAuthFailureCount.setStatus(_A)
class _IpadPPPStartAuthFailureTrapEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_S,1),(_T,2)))
_IpadPPPStartAuthFailureTrapEnable_Type.__name__=_C
_IpadPPPStartAuthFailureTrapEnable_Object=MibTableColumn
ipadPPPStartAuthFailureTrapEnable=_IpadPPPStartAuthFailureTrapEnable_Object((1,3,6,1,4,1,321,100,1,7,4,1,1,19),_IpadPPPStartAuthFailureTrapEnable_Type())
ipadPPPStartAuthFailureTrapEnable.setMaxAccess('read-write')
if mibBuilder.loadTexts:ipadPPPStartAuthFailureTrapEnable.setStatus(_A)
class _IpadPPPStartIPCPState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3),(_H,4),(_I,5),(_J,6),(_K,7),(_L,8),(_M,9),(_N,10)))
_IpadPPPStartIPCPState_Type.__name__=_C
_IpadPPPStartIPCPState_Object=MibTableColumn
ipadPPPStartIPCPState=_IpadPPPStartIPCPState_Object((1,3,6,1,4,1,321,100,1,7,4,1,1,20),_IpadPPPStartIPCPState_Type())
ipadPPPStartIPCPState.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadPPPStartIPCPState.setStatus(_A)
_IpadPPPStartIPCPStateTime_Type=Integer32
_IpadPPPStartIPCPStateTime_Object=MibTableColumn
ipadPPPStartIPCPStateTime=_IpadPPPStartIPCPStateTime_Object((1,3,6,1,4,1,321,100,1,7,4,1,1,21),_IpadPPPStartIPCPStateTime_Type())
ipadPPPStartIPCPStateTime.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadPPPStartIPCPStateTime.setStatus(_A)
_IpadPPPStartIPCPStateChanges_Type=Integer32
_IpadPPPStartIPCPStateChanges_Object=MibTableColumn
ipadPPPStartIPCPStateChanges=_IpadPPPStartIPCPStateChanges_Object((1,3,6,1,4,1,321,100,1,7,4,1,1,22),_IpadPPPStartIPCPStateChanges_Type())
ipadPPPStartIPCPStateChanges.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadPPPStartIPCPStateChanges.setStatus(_A)
_IpadPPPStartIPCPIPSource_Type=IpAddress
_IpadPPPStartIPCPIPSource_Object=MibTableColumn
ipadPPPStartIPCPIPSource=_IpadPPPStartIPCPIPSource_Object((1,3,6,1,4,1,321,100,1,7,4,1,1,23),_IpadPPPStartIPCPIPSource_Type())
ipadPPPStartIPCPIPSource.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadPPPStartIPCPIPSource.setStatus(_A)
_IpadPPPStartIPCPIPDestAddress_Type=IpAddress
_IpadPPPStartIPCPIPDestAddress_Object=MibTableColumn
ipadPPPStartIPCPIPDestAddress=_IpadPPPStartIPCPIPDestAddress_Object((1,3,6,1,4,1,321,100,1,7,4,1,1,24),_IpadPPPStartIPCPIPDestAddress_Type())
ipadPPPStartIPCPIPDestAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadPPPStartIPCPIPDestAddress.setStatus(_A)
class _IpadPPPStartIPCPCompressionProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_Q,1),(_R,2),('regularIPdata',3),('compressedTCP',4),('uncompressedTCP',5)))
_IpadPPPStartIPCPCompressionProtocol_Type.__name__=_C
_IpadPPPStartIPCPCompressionProtocol_Object=MibTableColumn
ipadPPPStartIPCPCompressionProtocol=_IpadPPPStartIPCPCompressionProtocol_Object((1,3,6,1,4,1,321,100,1,7,4,1,1,25),_IpadPPPStartIPCPCompressionProtocol_Type())
ipadPPPStartIPCPCompressionProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadPPPStartIPCPCompressionProtocol.setStatus(_A)
_IpadPPPStartLCPHistoryTable_Object=MibTable
ipadPPPStartLCPHistoryTable=_IpadPPPStartLCPHistoryTable_Object((1,3,6,1,4,1,321,100,1,7,4,2))
if mibBuilder.loadTexts:ipadPPPStartLCPHistoryTable.setStatus(_A)
_IpadPPPStartLCPHistoryTableEntry_Object=MibTableRow
ipadPPPStartLCPHistoryTableEntry=_IpadPPPStartLCPHistoryTableEntry_Object((1,3,6,1,4,1,321,100,1,7,4,2,1))
ipadPPPStartLCPHistoryTableEntry.setIndexNames((0,_O,_P),(0,_D,_W))
if mibBuilder.loadTexts:ipadPPPStartLCPHistoryTableEntry.setStatus(_A)
_IpadPPPStartLCPHistoryIndex_Type=Integer32
_IpadPPPStartLCPHistoryIndex_Object=MibTableColumn
ipadPPPStartLCPHistoryIndex=_IpadPPPStartLCPHistoryIndex_Object((1,3,6,1,4,1,321,100,1,7,4,2,1,1),_IpadPPPStartLCPHistoryIndex_Type())
ipadPPPStartLCPHistoryIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadPPPStartLCPHistoryIndex.setStatus(_A)
class _IpadPPPStartLCPHistoryState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3),(_H,4),(_I,5),(_J,6),(_K,7),(_L,8),(_M,9),(_N,10)))
_IpadPPPStartLCPHistoryState_Type.__name__=_C
_IpadPPPStartLCPHistoryState_Object=MibTableColumn
ipadPPPStartLCPHistoryState=_IpadPPPStartLCPHistoryState_Object((1,3,6,1,4,1,321,100,1,7,4,2,1,2),_IpadPPPStartLCPHistoryState_Type())
ipadPPPStartLCPHistoryState.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadPPPStartLCPHistoryState.setStatus(_A)
_IpadPPPStartLCPHistoryStateTime_Type=Integer32
_IpadPPPStartLCPHistoryStateTime_Object=MibTableColumn
ipadPPPStartLCPHistoryStateTime=_IpadPPPStartLCPHistoryStateTime_Object((1,3,6,1,4,1,321,100,1,7,4,2,1,3),_IpadPPPStartLCPHistoryStateTime_Type())
ipadPPPStartLCPHistoryStateTime.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadPPPStartLCPHistoryStateTime.setStatus(_A)
_IpadPPPStartAuthHistoryTable_Object=MibTable
ipadPPPStartAuthHistoryTable=_IpadPPPStartAuthHistoryTable_Object((1,3,6,1,4,1,321,100,1,7,4,3))
if mibBuilder.loadTexts:ipadPPPStartAuthHistoryTable.setStatus(_A)
_IpadPPPStartAuthHistoryTableEntry_Object=MibTableRow
ipadPPPStartAuthHistoryTableEntry=_IpadPPPStartAuthHistoryTableEntry_Object((1,3,6,1,4,1,321,100,1,7,4,3,1))
ipadPPPStartAuthHistoryTableEntry.setIndexNames((0,_O,_P),(0,_D,_X))
if mibBuilder.loadTexts:ipadPPPStartAuthHistoryTableEntry.setStatus(_A)
_IpadPPPStartAuthHistoryIndex_Type=Integer32
_IpadPPPStartAuthHistoryIndex_Object=MibTableColumn
ipadPPPStartAuthHistoryIndex=_IpadPPPStartAuthHistoryIndex_Object((1,3,6,1,4,1,321,100,1,7,4,3,1,1),_IpadPPPStartAuthHistoryIndex_Type())
ipadPPPStartAuthHistoryIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadPPPStartAuthHistoryIndex.setStatus(_A)
class _IpadPPPStartAuthHistoryState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3),(_H,4),(_I,5),(_J,6),(_K,7),(_L,8),(_M,9),(_N,10)))
_IpadPPPStartAuthHistoryState_Type.__name__=_C
_IpadPPPStartAuthHistoryState_Object=MibTableColumn
ipadPPPStartAuthHistoryState=_IpadPPPStartAuthHistoryState_Object((1,3,6,1,4,1,321,100,1,7,4,3,1,2),_IpadPPPStartAuthHistoryState_Type())
ipadPPPStartAuthHistoryState.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadPPPStartAuthHistoryState.setStatus(_A)
_IpadPPPStartAuthHistoryStateTime_Type=Integer32
_IpadPPPStartAuthHistoryStateTime_Object=MibTableColumn
ipadPPPStartAuthHistoryStateTime=_IpadPPPStartAuthHistoryStateTime_Object((1,3,6,1,4,1,321,100,1,7,4,3,1,3),_IpadPPPStartAuthHistoryStateTime_Type())
ipadPPPStartAuthHistoryStateTime.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadPPPStartAuthHistoryStateTime.setStatus(_A)
_IpadPPPStartIPCPHistoryTable_Object=MibTable
ipadPPPStartIPCPHistoryTable=_IpadPPPStartIPCPHistoryTable_Object((1,3,6,1,4,1,321,100,1,7,4,4))
if mibBuilder.loadTexts:ipadPPPStartIPCPHistoryTable.setStatus(_A)
_IpadPPPStartIPCPHistoryTableEntry_Object=MibTableRow
ipadPPPStartIPCPHistoryTableEntry=_IpadPPPStartIPCPHistoryTableEntry_Object((1,3,6,1,4,1,321,100,1,7,4,4,1))
ipadPPPStartIPCPHistoryTableEntry.setIndexNames((0,_O,_P),(0,_D,_Y))
if mibBuilder.loadTexts:ipadPPPStartIPCPHistoryTableEntry.setStatus(_A)
_IpadPPPStartIPCPHistoryIndex_Type=Integer32
_IpadPPPStartIPCPHistoryIndex_Object=MibTableColumn
ipadPPPStartIPCPHistoryIndex=_IpadPPPStartIPCPHistoryIndex_Object((1,3,6,1,4,1,321,100,1,7,4,4,1,1),_IpadPPPStartIPCPHistoryIndex_Type())
ipadPPPStartIPCPHistoryIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadPPPStartIPCPHistoryIndex.setStatus(_A)
class _IpadPPPStartIPCPHistoryState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3),(_H,4),(_I,5),(_J,6),(_K,7),(_L,8),(_M,9),(_N,10)))
_IpadPPPStartIPCPHistoryState_Type.__name__=_C
_IpadPPPStartIPCPHistoryState_Object=MibTableColumn
ipadPPPStartIPCPHistoryState=_IpadPPPStartIPCPHistoryState_Object((1,3,6,1,4,1,321,100,1,7,4,4,1,2),_IpadPPPStartIPCPHistoryState_Type())
ipadPPPStartIPCPHistoryState.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadPPPStartIPCPHistoryState.setStatus(_A)
_IpadPPPStartIPCPHistoryStateTime_Type=Integer32
_IpadPPPStartIPCPHistoryStateTime_Object=MibTableColumn
ipadPPPStartIPCPHistoryStateTime=_IpadPPPStartIPCPHistoryStateTime_Object((1,3,6,1,4,1,321,100,1,7,4,4,1,3),_IpadPPPStartIPCPHistoryStateTime_Type())
ipadPPPStartIPCPHistoryStateTime.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadPPPStartIPCPHistoryStateTime.setStatus(_A)
ipadPPPStartAuthFailureTrap=NotificationType((1,3,6,1,4,1,321,100,1,999,0,25050))
ipadPPPStartAuthFailureTrap.setObjects((_D,_Z))
if mibBuilder.loadTexts:ipadPPPStartAuthFailureTrap.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'ipadIPStart':ipadIPStart,'ipadPPPStartTable':ipadPPPStartTable,'ipadPPPStartTableEntry':ipadPPPStartTableEntry,_V:ipadPPPStartService,'ipadPPPStartLCPState':ipadPPPStartLCPState,'ipadPPPStartLCPStateTime':ipadPPPStartLCPStateTime,'ipadPPPStartLCPStateChanges':ipadPPPStartLCPStateChanges,'ipadPPPStartLCPMRU':ipadPPPStartLCPMRU,'ipadPPPStartLCPAsyncCCM':ipadPPPStartLCPAsyncCCM,'ipadPPPStartLCPAuthProtocol':ipadPPPStartLCPAuthProtocol,'ipadPPPStartLCPQualityProtocol':ipadPPPStartLCPQualityProtocol,'ipadPPPStartLCPMagicNumber':ipadPPPStartLCPMagicNumber,'ipadPPPStartLCPPFC':ipadPPPStartLCPPFC,'ipadPPPStartLCPACFC':ipadPPPStartLCPACFC,'ipadPPPStartLCPFCSAlternatives':ipadPPPStartLCPFCSAlternatives,'ipadPPPStartLCPSDP':ipadPPPStartLCPSDP,'ipadPPPStartLCPCompoundFrames':ipadPPPStartLCPCompoundFrames,'ipadPPPStartAuthState':ipadPPPStartAuthState,'ipadPPPStartAuthStateTime':ipadPPPStartAuthStateTime,'ipadPPPStartAuthStateChanges':ipadPPPStartAuthStateChanges,_Z:ipadPPPStartAuthFailureCount,'ipadPPPStartAuthFailureTrapEnable':ipadPPPStartAuthFailureTrapEnable,'ipadPPPStartIPCPState':ipadPPPStartIPCPState,'ipadPPPStartIPCPStateTime':ipadPPPStartIPCPStateTime,'ipadPPPStartIPCPStateChanges':ipadPPPStartIPCPStateChanges,'ipadPPPStartIPCPIPSource':ipadPPPStartIPCPIPSource,'ipadPPPStartIPCPIPDestAddress':ipadPPPStartIPCPIPDestAddress,'ipadPPPStartIPCPCompressionProtocol':ipadPPPStartIPCPCompressionProtocol,'ipadPPPStartLCPHistoryTable':ipadPPPStartLCPHistoryTable,'ipadPPPStartLCPHistoryTableEntry':ipadPPPStartLCPHistoryTableEntry,_W:ipadPPPStartLCPHistoryIndex,'ipadPPPStartLCPHistoryState':ipadPPPStartLCPHistoryState,'ipadPPPStartLCPHistoryStateTime':ipadPPPStartLCPHistoryStateTime,'ipadPPPStartAuthHistoryTable':ipadPPPStartAuthHistoryTable,'ipadPPPStartAuthHistoryTableEntry':ipadPPPStartAuthHistoryTableEntry,_X:ipadPPPStartAuthHistoryIndex,'ipadPPPStartAuthHistoryState':ipadPPPStartAuthHistoryState,'ipadPPPStartAuthHistoryStateTime':ipadPPPStartAuthHistoryStateTime,'ipadPPPStartIPCPHistoryTable':ipadPPPStartIPCPHistoryTable,'ipadPPPStartIPCPHistoryTableEntry':ipadPPPStartIPCPHistoryTableEntry,_Y:ipadPPPStartIPCPHistoryIndex,'ipadPPPStartIPCPHistoryState':ipadPPPStartIPCPHistoryState,'ipadPPPStartIPCPHistoryStateTime':ipadPPPStartIPCPHistoryStateTime,'ipadPPPStartAuthFailureTrap':ipadPPPStartAuthFailureTrap})