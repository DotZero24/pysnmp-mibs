_t='cmvPortQbinStatsGroup'
_s='cmvPortQbinConfGroup'
_r='cmvPortStatsGroup'
_q='cmvPortConfGroup'
_p='vrtlIntrQbinDiscardedCellCnt'
_o='vrtlIntrQbinTxdCellCnt'
_n='vrtlIntrQbinRxdCellCnt'
_m='vrtlIntrQbinCurrentCellCnt'
_l='vrtlIntrQbinEfciThreshold'
_k='vrtlIntrQbinFrameDiscardThreshold'
_j='vrtlIntrQbinClpLoThreshold'
_i='vrtlIntrQbinClpHiThreshold'
_h='vrtlIntrQbinMaxThreshold'
_g='vrtlIntrQbinDiscardSelection'
_f='vrtlIntrQbinRate'
_e='vrtlIntrQbinPri'
_d='vrtlIntrQbinState'
_c='vrtlIntrXmtdClpTaggedCellCnt'
_b='vrtlIntrXmtdClpUntaggedCellCnt'
_a='vrtlIntrXmtdRmCellCnt'
_Z='vrtlIntrXmtdOAMCellCnt'
_Y='vrtlIntrRxdClpTaggedDiscardedCellCnt'
_X='vrtlIntrRxdClpUntaggedDiscardedCellCnt'
_W='vrtlIntrRxdClpTaggedCellCnt'
_V='vrtlIntrRxdClpUntaggedCellCnt'
_U='vrtlIntrRxdRmCellCnt'
_T='vrtlIntrRxdValidOAMCellCnt'
_S='vrtlIntrTotalQbinCellCnt'
_R='vrtlIntrTotalCellCnt'
_Q='vrtlIntrCurrConfigPaths'
_P='vrtlIntrMaxCellRate'
_O='vrtlIntrMinCellRate'
_N='vrtlIntrMaxQueMem'
_M='vrtlIntrState'
_L='vrtlIntrPortNum'
_K='queCounterVrtlIntrQbinNum'
_J='queConuterVrtlIntrNum'
_I='queConfigVrtlIntrQbinNum'
_H='queConfigVrtlIntrNum'
_G='countVrtlIntrNum'
_F='configVrtlIntrNum'
_E='read-write'
_D='Integer32'
_C='read-only'
_B='CISCO-MGX82XX-VIRTUAL-PORT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
virtualInterface,=mibBuilder.importSymbols('BASIS-MIB','virtualInterface')
ciscoWan,=mibBuilder.importSymbols('CISCOWAN-SMI','ciscoWan')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoMgx82xxVirtualPortMIB=ModuleIdentity((1,3,6,1,4,1,351,150,38))
if mibBuilder.loadTexts:ciscoMgx82xxVirtualPortMIB.setRevisions(('2002-08-30 00:00',))
_VirtualInterfaceCnf_ObjectIdentity=ObjectIdentity
virtualInterfaceCnf=_VirtualInterfaceCnf_ObjectIdentity((1,3,6,1,4,1,351,110,5,2,8,1))
_VrtlIntrConfigTable_Object=MibTable
vrtlIntrConfigTable=_VrtlIntrConfigTable_Object((1,3,6,1,4,1,351,110,5,2,8,1,1))
if mibBuilder.loadTexts:vrtlIntrConfigTable.setStatus(_A)
_VrtlIntrConfigEntry_Object=MibTableRow
vrtlIntrConfigEntry=_VrtlIntrConfigEntry_Object((1,3,6,1,4,1,351,110,5,2,8,1,1,1))
vrtlIntrConfigEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:vrtlIntrConfigEntry.setStatus(_A)
class _ConfigVrtlIntrNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_ConfigVrtlIntrNum_Type.__name__=_D
_ConfigVrtlIntrNum_Object=MibTableColumn
configVrtlIntrNum=_ConfigVrtlIntrNum_Object((1,3,6,1,4,1,351,110,5,2,8,1,1,1,1),_ConfigVrtlIntrNum_Type())
configVrtlIntrNum.setMaxAccess(_C)
if mibBuilder.loadTexts:configVrtlIntrNum.setStatus(_A)
class _VrtlIntrPortNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4))
_VrtlIntrPortNum_Type.__name__=_D
_VrtlIntrPortNum_Object=MibTableColumn
vrtlIntrPortNum=_VrtlIntrPortNum_Object((1,3,6,1,4,1,351,110,5,2,8,1,1,1,2),_VrtlIntrPortNum_Type())
vrtlIntrPortNum.setMaxAccess(_E)
if mibBuilder.loadTexts:vrtlIntrPortNum.setStatus(_A)
class _VrtlIntrState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('down',1),('up',2)))
_VrtlIntrState_Type.__name__=_D
_VrtlIntrState_Object=MibTableColumn
vrtlIntrState=_VrtlIntrState_Object((1,3,6,1,4,1,351,110,5,2,8,1,1,1,3),_VrtlIntrState_Type())
vrtlIntrState.setMaxAccess(_E)
if mibBuilder.loadTexts:vrtlIntrState.setStatus(_A)
class _VrtlIntrMaxQueMem_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_VrtlIntrMaxQueMem_Type.__name__=_D
_VrtlIntrMaxQueMem_Object=MibTableColumn
vrtlIntrMaxQueMem=_VrtlIntrMaxQueMem_Object((1,3,6,1,4,1,351,110,5,2,8,1,1,1,4),_VrtlIntrMaxQueMem_Type())
vrtlIntrMaxQueMem.setMaxAccess(_E)
if mibBuilder.loadTexts:vrtlIntrMaxQueMem.setStatus(_A)
class _VrtlIntrMinCellRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(103384,353208))
_VrtlIntrMinCellRate_Type.__name__=_D
_VrtlIntrMinCellRate_Object=MibTableColumn
vrtlIntrMinCellRate=_VrtlIntrMinCellRate_Object((1,3,6,1,4,1,351,110,5,2,8,1,1,1,5),_VrtlIntrMinCellRate_Type())
vrtlIntrMinCellRate.setMaxAccess(_E)
if mibBuilder.loadTexts:vrtlIntrMinCellRate.setStatus(_A)
class _VrtlIntrMaxCellRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(103384,353208))
_VrtlIntrMaxCellRate_Type.__name__=_D
_VrtlIntrMaxCellRate_Object=MibTableColumn
vrtlIntrMaxCellRate=_VrtlIntrMaxCellRate_Object((1,3,6,1,4,1,351,110,5,2,8,1,1,1,6),_VrtlIntrMaxCellRate_Type())
vrtlIntrMaxCellRate.setMaxAccess(_E)
if mibBuilder.loadTexts:vrtlIntrMaxCellRate.setStatus(_A)
_VrtlIntrCurrConfigPaths_Type=Integer32
_VrtlIntrCurrConfigPaths_Object=MibTableColumn
vrtlIntrCurrConfigPaths=_VrtlIntrCurrConfigPaths_Object((1,3,6,1,4,1,351,110,5,2,8,1,1,1,7),_VrtlIntrCurrConfigPaths_Type())
vrtlIntrCurrConfigPaths.setMaxAccess(_C)
if mibBuilder.loadTexts:vrtlIntrCurrConfigPaths.setStatus(_A)
_VirtualInterfaceCnt_ObjectIdentity=ObjectIdentity
virtualInterfaceCnt=_VirtualInterfaceCnt_ObjectIdentity((1,3,6,1,4,1,351,110,5,2,8,2))
_VrtlIntrCounterTable_Object=MibTable
vrtlIntrCounterTable=_VrtlIntrCounterTable_Object((1,3,6,1,4,1,351,110,5,2,8,2,1))
if mibBuilder.loadTexts:vrtlIntrCounterTable.setStatus(_A)
_VrtlIntrCounterEntry_Object=MibTableRow
vrtlIntrCounterEntry=_VrtlIntrCounterEntry_Object((1,3,6,1,4,1,351,110,5,2,8,2,1,1))
vrtlIntrCounterEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:vrtlIntrCounterEntry.setStatus(_A)
class _CountVrtlIntrNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_CountVrtlIntrNum_Type.__name__=_D
_CountVrtlIntrNum_Object=MibTableColumn
countVrtlIntrNum=_CountVrtlIntrNum_Object((1,3,6,1,4,1,351,110,5,2,8,2,1,1,1),_CountVrtlIntrNum_Type())
countVrtlIntrNum.setMaxAccess(_C)
if mibBuilder.loadTexts:countVrtlIntrNum.setStatus(_A)
_VrtlIntrTotalCellCnt_Type=Counter32
_VrtlIntrTotalCellCnt_Object=MibTableColumn
vrtlIntrTotalCellCnt=_VrtlIntrTotalCellCnt_Object((1,3,6,1,4,1,351,110,5,2,8,2,1,1,2),_VrtlIntrTotalCellCnt_Type())
vrtlIntrTotalCellCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:vrtlIntrTotalCellCnt.setStatus(_A)
_VrtlIntrTotalQbinCellCnt_Type=Counter32
_VrtlIntrTotalQbinCellCnt_Object=MibTableColumn
vrtlIntrTotalQbinCellCnt=_VrtlIntrTotalQbinCellCnt_Object((1,3,6,1,4,1,351,110,5,2,8,2,1,1,3),_VrtlIntrTotalQbinCellCnt_Type())
vrtlIntrTotalQbinCellCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:vrtlIntrTotalQbinCellCnt.setStatus(_A)
_VrtlIntrRxdValidOAMCellCnt_Type=Counter32
_VrtlIntrRxdValidOAMCellCnt_Object=MibTableColumn
vrtlIntrRxdValidOAMCellCnt=_VrtlIntrRxdValidOAMCellCnt_Object((1,3,6,1,4,1,351,110,5,2,8,2,1,1,4),_VrtlIntrRxdValidOAMCellCnt_Type())
vrtlIntrRxdValidOAMCellCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:vrtlIntrRxdValidOAMCellCnt.setStatus(_A)
_VrtlIntrRxdRmCellCnt_Type=Counter32
_VrtlIntrRxdRmCellCnt_Object=MibTableColumn
vrtlIntrRxdRmCellCnt=_VrtlIntrRxdRmCellCnt_Object((1,3,6,1,4,1,351,110,5,2,8,2,1,1,5),_VrtlIntrRxdRmCellCnt_Type())
vrtlIntrRxdRmCellCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:vrtlIntrRxdRmCellCnt.setStatus(_A)
_VrtlIntrRxdClpUntaggedCellCnt_Type=Counter32
_VrtlIntrRxdClpUntaggedCellCnt_Object=MibTableColumn
vrtlIntrRxdClpUntaggedCellCnt=_VrtlIntrRxdClpUntaggedCellCnt_Object((1,3,6,1,4,1,351,110,5,2,8,2,1,1,6),_VrtlIntrRxdClpUntaggedCellCnt_Type())
vrtlIntrRxdClpUntaggedCellCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:vrtlIntrRxdClpUntaggedCellCnt.setStatus(_A)
_VrtlIntrRxdClpTaggedCellCnt_Type=Counter32
_VrtlIntrRxdClpTaggedCellCnt_Object=MibTableColumn
vrtlIntrRxdClpTaggedCellCnt=_VrtlIntrRxdClpTaggedCellCnt_Object((1,3,6,1,4,1,351,110,5,2,8,2,1,1,7),_VrtlIntrRxdClpTaggedCellCnt_Type())
vrtlIntrRxdClpTaggedCellCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:vrtlIntrRxdClpTaggedCellCnt.setStatus(_A)
_VrtlIntrRxdClpUntaggedDiscardedCellCnt_Type=Counter32
_VrtlIntrRxdClpUntaggedDiscardedCellCnt_Object=MibTableColumn
vrtlIntrRxdClpUntaggedDiscardedCellCnt=_VrtlIntrRxdClpUntaggedDiscardedCellCnt_Object((1,3,6,1,4,1,351,110,5,2,8,2,1,1,8),_VrtlIntrRxdClpUntaggedDiscardedCellCnt_Type())
vrtlIntrRxdClpUntaggedDiscardedCellCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:vrtlIntrRxdClpUntaggedDiscardedCellCnt.setStatus(_A)
_VrtlIntrRxdClpTaggedDiscardedCellCnt_Type=Counter32
_VrtlIntrRxdClpTaggedDiscardedCellCnt_Object=MibTableColumn
vrtlIntrRxdClpTaggedDiscardedCellCnt=_VrtlIntrRxdClpTaggedDiscardedCellCnt_Object((1,3,6,1,4,1,351,110,5,2,8,2,1,1,9),_VrtlIntrRxdClpTaggedDiscardedCellCnt_Type())
vrtlIntrRxdClpTaggedDiscardedCellCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:vrtlIntrRxdClpTaggedDiscardedCellCnt.setStatus(_A)
_VrtlIntrXmtdOAMCellCnt_Type=Counter32
_VrtlIntrXmtdOAMCellCnt_Object=MibTableColumn
vrtlIntrXmtdOAMCellCnt=_VrtlIntrXmtdOAMCellCnt_Object((1,3,6,1,4,1,351,110,5,2,8,2,1,1,10),_VrtlIntrXmtdOAMCellCnt_Type())
vrtlIntrXmtdOAMCellCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:vrtlIntrXmtdOAMCellCnt.setStatus(_A)
_VrtlIntrXmtdRmCellCnt_Type=Counter32
_VrtlIntrXmtdRmCellCnt_Object=MibTableColumn
vrtlIntrXmtdRmCellCnt=_VrtlIntrXmtdRmCellCnt_Object((1,3,6,1,4,1,351,110,5,2,8,2,1,1,11),_VrtlIntrXmtdRmCellCnt_Type())
vrtlIntrXmtdRmCellCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:vrtlIntrXmtdRmCellCnt.setStatus(_A)
_VrtlIntrXmtdClpUntaggedCellCnt_Type=Counter32
_VrtlIntrXmtdClpUntaggedCellCnt_Object=MibTableColumn
vrtlIntrXmtdClpUntaggedCellCnt=_VrtlIntrXmtdClpUntaggedCellCnt_Object((1,3,6,1,4,1,351,110,5,2,8,2,1,1,12),_VrtlIntrXmtdClpUntaggedCellCnt_Type())
vrtlIntrXmtdClpUntaggedCellCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:vrtlIntrXmtdClpUntaggedCellCnt.setStatus(_A)
_VrtlIntrXmtdClpTaggedCellCnt_Type=Counter32
_VrtlIntrXmtdClpTaggedCellCnt_Object=MibTableColumn
vrtlIntrXmtdClpTaggedCellCnt=_VrtlIntrXmtdClpTaggedCellCnt_Object((1,3,6,1,4,1,351,110,5,2,8,2,1,1,13),_VrtlIntrXmtdClpTaggedCellCnt_Type())
vrtlIntrXmtdClpTaggedCellCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:vrtlIntrXmtdClpTaggedCellCnt.setStatus(_A)
_VirtualInterfaceQbinCnf_ObjectIdentity=ObjectIdentity
virtualInterfaceQbinCnf=_VirtualInterfaceQbinCnf_ObjectIdentity((1,3,6,1,4,1,351,110,5,2,8,3))
_VrtlIntrQbinConfigTable_Object=MibTable
vrtlIntrQbinConfigTable=_VrtlIntrQbinConfigTable_Object((1,3,6,1,4,1,351,110,5,2,8,3,1))
if mibBuilder.loadTexts:vrtlIntrQbinConfigTable.setStatus(_A)
_VrtlIntrQbinConfigEntry_Object=MibTableRow
vrtlIntrQbinConfigEntry=_VrtlIntrQbinConfigEntry_Object((1,3,6,1,4,1,351,110,5,2,8,3,1,1))
vrtlIntrQbinConfigEntry.setIndexNames((0,_B,_H),(0,_B,_I))
if mibBuilder.loadTexts:vrtlIntrQbinConfigEntry.setStatus(_A)
class _QueConfigVrtlIntrNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_QueConfigVrtlIntrNum_Type.__name__=_D
_QueConfigVrtlIntrNum_Object=MibTableColumn
queConfigVrtlIntrNum=_QueConfigVrtlIntrNum_Object((1,3,6,1,4,1,351,110,5,2,8,3,1,1,1),_QueConfigVrtlIntrNum_Type())
queConfigVrtlIntrNum.setMaxAccess(_C)
if mibBuilder.loadTexts:queConfigVrtlIntrNum.setStatus(_A)
class _QueConfigVrtlIntrQbinNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_QueConfigVrtlIntrQbinNum_Type.__name__=_D
_QueConfigVrtlIntrQbinNum_Object=MibTableColumn
queConfigVrtlIntrQbinNum=_QueConfigVrtlIntrQbinNum_Object((1,3,6,1,4,1,351,110,5,2,8,3,1,1,2),_QueConfigVrtlIntrQbinNum_Type())
queConfigVrtlIntrQbinNum.setMaxAccess(_C)
if mibBuilder.loadTexts:queConfigVrtlIntrQbinNum.setStatus(_A)
class _VrtlIntrQbinState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('down',1),('up',2)))
_VrtlIntrQbinState_Type.__name__=_D
_VrtlIntrQbinState_Object=MibTableColumn
vrtlIntrQbinState=_VrtlIntrQbinState_Object((1,3,6,1,4,1,351,110,5,2,8,3,1,1,3),_VrtlIntrQbinState_Type())
vrtlIntrQbinState.setMaxAccess(_E)
if mibBuilder.loadTexts:vrtlIntrQbinState.setStatus(_A)
class _VrtlIntrQbinPri_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_VrtlIntrQbinPri_Type.__name__=_D
_VrtlIntrQbinPri_Object=MibTableColumn
vrtlIntrQbinPri=_VrtlIntrQbinPri_Object((1,3,6,1,4,1,351,110,5,2,8,3,1,1,4),_VrtlIntrQbinPri_Type())
vrtlIntrQbinPri.setMaxAccess(_E)
if mibBuilder.loadTexts:vrtlIntrQbinPri.setStatus(_A)
class _VrtlIntrQbinRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,353208))
_VrtlIntrQbinRate_Type.__name__=_D
_VrtlIntrQbinRate_Object=MibTableColumn
vrtlIntrQbinRate=_VrtlIntrQbinRate_Object((1,3,6,1,4,1,351,110,5,2,8,3,1,1,5),_VrtlIntrQbinRate_Type())
vrtlIntrQbinRate.setMaxAccess(_E)
if mibBuilder.loadTexts:vrtlIntrQbinRate.setStatus(_A)
class _VrtlIntrQbinDiscardSelection_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3)));namedValues=NamedValues(*(('clpHysteresis',1),('frameDiscard',3)))
_VrtlIntrQbinDiscardSelection_Type.__name__=_D
_VrtlIntrQbinDiscardSelection_Object=MibTableColumn
vrtlIntrQbinDiscardSelection=_VrtlIntrQbinDiscardSelection_Object((1,3,6,1,4,1,351,110,5,2,8,3,1,1,6),_VrtlIntrQbinDiscardSelection_Type())
vrtlIntrQbinDiscardSelection.setMaxAccess(_E)
if mibBuilder.loadTexts:vrtlIntrQbinDiscardSelection.setStatus(_A)
class _VrtlIntrQbinMaxThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,512000))
_VrtlIntrQbinMaxThreshold_Type.__name__=_D
_VrtlIntrQbinMaxThreshold_Object=MibTableColumn
vrtlIntrQbinMaxThreshold=_VrtlIntrQbinMaxThreshold_Object((1,3,6,1,4,1,351,110,5,2,8,3,1,1,7),_VrtlIntrQbinMaxThreshold_Type())
vrtlIntrQbinMaxThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:vrtlIntrQbinMaxThreshold.setStatus(_A)
class _VrtlIntrQbinClpHiThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,512000))
_VrtlIntrQbinClpHiThreshold_Type.__name__=_D
_VrtlIntrQbinClpHiThreshold_Object=MibTableColumn
vrtlIntrQbinClpHiThreshold=_VrtlIntrQbinClpHiThreshold_Object((1,3,6,1,4,1,351,110,5,2,8,3,1,1,8),_VrtlIntrQbinClpHiThreshold_Type())
vrtlIntrQbinClpHiThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:vrtlIntrQbinClpHiThreshold.setStatus(_A)
class _VrtlIntrQbinClpLoThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,512000))
_VrtlIntrQbinClpLoThreshold_Type.__name__=_D
_VrtlIntrQbinClpLoThreshold_Object=MibTableColumn
vrtlIntrQbinClpLoThreshold=_VrtlIntrQbinClpLoThreshold_Object((1,3,6,1,4,1,351,110,5,2,8,3,1,1,9),_VrtlIntrQbinClpLoThreshold_Type())
vrtlIntrQbinClpLoThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:vrtlIntrQbinClpLoThreshold.setStatus(_A)
class _VrtlIntrQbinFrameDiscardThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,512000))
_VrtlIntrQbinFrameDiscardThreshold_Type.__name__=_D
_VrtlIntrQbinFrameDiscardThreshold_Object=MibTableColumn
vrtlIntrQbinFrameDiscardThreshold=_VrtlIntrQbinFrameDiscardThreshold_Object((1,3,6,1,4,1,351,110,5,2,8,3,1,1,10),_VrtlIntrQbinFrameDiscardThreshold_Type())
vrtlIntrQbinFrameDiscardThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:vrtlIntrQbinFrameDiscardThreshold.setStatus(_A)
class _VrtlIntrQbinEfciThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,512000))
_VrtlIntrQbinEfciThreshold_Type.__name__=_D
_VrtlIntrQbinEfciThreshold_Object=MibTableColumn
vrtlIntrQbinEfciThreshold=_VrtlIntrQbinEfciThreshold_Object((1,3,6,1,4,1,351,110,5,2,8,3,1,1,11),_VrtlIntrQbinEfciThreshold_Type())
vrtlIntrQbinEfciThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:vrtlIntrQbinEfciThreshold.setStatus(_A)
_VirtualInterfaceQbinCnt_ObjectIdentity=ObjectIdentity
virtualInterfaceQbinCnt=_VirtualInterfaceQbinCnt_ObjectIdentity((1,3,6,1,4,1,351,110,5,2,8,4))
_VrtlIntrQbinCounterTable_Object=MibTable
vrtlIntrQbinCounterTable=_VrtlIntrQbinCounterTable_Object((1,3,6,1,4,1,351,110,5,2,8,4,1))
if mibBuilder.loadTexts:vrtlIntrQbinCounterTable.setStatus(_A)
_VrtlIntrQbinCounterEntry_Object=MibTableRow
vrtlIntrQbinCounterEntry=_VrtlIntrQbinCounterEntry_Object((1,3,6,1,4,1,351,110,5,2,8,4,1,1))
vrtlIntrQbinCounterEntry.setIndexNames((0,_B,_J),(0,_B,_K))
if mibBuilder.loadTexts:vrtlIntrQbinCounterEntry.setStatus(_A)
class _QueConuterVrtlIntrNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_QueConuterVrtlIntrNum_Type.__name__=_D
_QueConuterVrtlIntrNum_Object=MibTableColumn
queConuterVrtlIntrNum=_QueConuterVrtlIntrNum_Object((1,3,6,1,4,1,351,110,5,2,8,4,1,1,1),_QueConuterVrtlIntrNum_Type())
queConuterVrtlIntrNum.setMaxAccess(_C)
if mibBuilder.loadTexts:queConuterVrtlIntrNum.setStatus(_A)
class _QueCounterVrtlIntrQbinNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_QueCounterVrtlIntrQbinNum_Type.__name__=_D
_QueCounterVrtlIntrQbinNum_Object=MibTableColumn
queCounterVrtlIntrQbinNum=_QueCounterVrtlIntrQbinNum_Object((1,3,6,1,4,1,351,110,5,2,8,4,1,1,2),_QueCounterVrtlIntrQbinNum_Type())
queCounterVrtlIntrQbinNum.setMaxAccess(_C)
if mibBuilder.loadTexts:queCounterVrtlIntrQbinNum.setStatus(_A)
_VrtlIntrQbinCurrentCellCnt_Type=Counter32
_VrtlIntrQbinCurrentCellCnt_Object=MibTableColumn
vrtlIntrQbinCurrentCellCnt=_VrtlIntrQbinCurrentCellCnt_Object((1,3,6,1,4,1,351,110,5,2,8,4,1,1,3),_VrtlIntrQbinCurrentCellCnt_Type())
vrtlIntrQbinCurrentCellCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:vrtlIntrQbinCurrentCellCnt.setStatus(_A)
_VrtlIntrQbinRxdCellCnt_Type=Counter32
_VrtlIntrQbinRxdCellCnt_Object=MibTableColumn
vrtlIntrQbinRxdCellCnt=_VrtlIntrQbinRxdCellCnt_Object((1,3,6,1,4,1,351,110,5,2,8,4,1,1,4),_VrtlIntrQbinRxdCellCnt_Type())
vrtlIntrQbinRxdCellCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:vrtlIntrQbinRxdCellCnt.setStatus(_A)
_VrtlIntrQbinTxdCellCnt_Type=Counter32
_VrtlIntrQbinTxdCellCnt_Object=MibTableColumn
vrtlIntrQbinTxdCellCnt=_VrtlIntrQbinTxdCellCnt_Object((1,3,6,1,4,1,351,110,5,2,8,4,1,1,5),_VrtlIntrQbinTxdCellCnt_Type())
vrtlIntrQbinTxdCellCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:vrtlIntrQbinTxdCellCnt.setStatus(_A)
_VrtlIntrQbinDiscardedCellCnt_Type=Counter32
_VrtlIntrQbinDiscardedCellCnt_Object=MibTableColumn
vrtlIntrQbinDiscardedCellCnt=_VrtlIntrQbinDiscardedCellCnt_Object((1,3,6,1,4,1,351,110,5,2,8,4,1,1,6),_VrtlIntrQbinDiscardedCellCnt_Type())
vrtlIntrQbinDiscardedCellCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:vrtlIntrQbinDiscardedCellCnt.setStatus(_A)
_CmvPortMIBConformance_ObjectIdentity=ObjectIdentity
cmvPortMIBConformance=_CmvPortMIBConformance_ObjectIdentity((1,3,6,1,4,1,351,150,38,2))
_CmvPortMIBGroups_ObjectIdentity=ObjectIdentity
cmvPortMIBGroups=_CmvPortMIBGroups_ObjectIdentity((1,3,6,1,4,1,351,150,38,2,1))
_CmvPortMIBCompliances_ObjectIdentity=ObjectIdentity
cmvPortMIBCompliances=_CmvPortMIBCompliances_ObjectIdentity((1,3,6,1,4,1,351,150,38,2,2))
cmvPortConfGroup=ObjectGroup((1,3,6,1,4,1,351,150,38,2,1,1))
cmvPortConfGroup.setObjects(*((_B,_F),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:cmvPortConfGroup.setStatus(_A)
cmvPortStatsGroup=ObjectGroup((1,3,6,1,4,1,351,150,38,2,1,2))
cmvPortStatsGroup.setObjects(*((_B,_G),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c)))
if mibBuilder.loadTexts:cmvPortStatsGroup.setStatus(_A)
cmvPortQbinConfGroup=ObjectGroup((1,3,6,1,4,1,351,150,38,2,1,3))
cmvPortQbinConfGroup.setObjects(*((_B,_H),(_B,_I),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l)))
if mibBuilder.loadTexts:cmvPortQbinConfGroup.setStatus(_A)
cmvPortQbinStatsGroup=ObjectGroup((1,3,6,1,4,1,351,150,38,2,1,4))
cmvPortQbinStatsGroup.setObjects(*((_B,_J),(_B,_K),(_B,_m),(_B,_n),(_B,_o),(_B,_p)))
if mibBuilder.loadTexts:cmvPortQbinStatsGroup.setStatus(_A)
cmvPortCompliance=ModuleCompliance((1,3,6,1,4,1,351,150,38,2,2,1))
cmvPortCompliance.setObjects(*((_B,_q),(_B,_r),(_B,_s),(_B,_t)))
if mibBuilder.loadTexts:cmvPortCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'virtualInterfaceCnf':virtualInterfaceCnf,'vrtlIntrConfigTable':vrtlIntrConfigTable,'vrtlIntrConfigEntry':vrtlIntrConfigEntry,_F:configVrtlIntrNum,_L:vrtlIntrPortNum,_M:vrtlIntrState,_N:vrtlIntrMaxQueMem,_O:vrtlIntrMinCellRate,_P:vrtlIntrMaxCellRate,_Q:vrtlIntrCurrConfigPaths,'virtualInterfaceCnt':virtualInterfaceCnt,'vrtlIntrCounterTable':vrtlIntrCounterTable,'vrtlIntrCounterEntry':vrtlIntrCounterEntry,_G:countVrtlIntrNum,_R:vrtlIntrTotalCellCnt,_S:vrtlIntrTotalQbinCellCnt,_T:vrtlIntrRxdValidOAMCellCnt,_U:vrtlIntrRxdRmCellCnt,_V:vrtlIntrRxdClpUntaggedCellCnt,_W:vrtlIntrRxdClpTaggedCellCnt,_X:vrtlIntrRxdClpUntaggedDiscardedCellCnt,_Y:vrtlIntrRxdClpTaggedDiscardedCellCnt,_Z:vrtlIntrXmtdOAMCellCnt,_a:vrtlIntrXmtdRmCellCnt,_b:vrtlIntrXmtdClpUntaggedCellCnt,_c:vrtlIntrXmtdClpTaggedCellCnt,'virtualInterfaceQbinCnf':virtualInterfaceQbinCnf,'vrtlIntrQbinConfigTable':vrtlIntrQbinConfigTable,'vrtlIntrQbinConfigEntry':vrtlIntrQbinConfigEntry,_H:queConfigVrtlIntrNum,_I:queConfigVrtlIntrQbinNum,_d:vrtlIntrQbinState,_e:vrtlIntrQbinPri,_f:vrtlIntrQbinRate,_g:vrtlIntrQbinDiscardSelection,_h:vrtlIntrQbinMaxThreshold,_i:vrtlIntrQbinClpHiThreshold,_j:vrtlIntrQbinClpLoThreshold,_k:vrtlIntrQbinFrameDiscardThreshold,_l:vrtlIntrQbinEfciThreshold,'virtualInterfaceQbinCnt':virtualInterfaceQbinCnt,'vrtlIntrQbinCounterTable':vrtlIntrQbinCounterTable,'vrtlIntrQbinCounterEntry':vrtlIntrQbinCounterEntry,_J:queConuterVrtlIntrNum,_K:queCounterVrtlIntrQbinNum,_m:vrtlIntrQbinCurrentCellCnt,_n:vrtlIntrQbinRxdCellCnt,_o:vrtlIntrQbinTxdCellCnt,_p:vrtlIntrQbinDiscardedCellCnt,'ciscoMgx82xxVirtualPortMIB':ciscoMgx82xxVirtualPortMIB,'cmvPortMIBConformance':cmvPortMIBConformance,'cmvPortMIBGroups':cmvPortMIBGroups,_q:cmvPortConfGroup,_r:cmvPortStatsGroup,_s:cmvPortQbinConfGroup,_t:cmvPortQbinStatsGroup,'cmvPortMIBCompliances':cmvPortMIBCompliances,'cmvPortCompliance':cmvPortCompliance})