_i='f3EotdmObjectGroup'
_h='vcgMemberSkLcasState'
_g='vcgMemberSkLcasSendMst'
_f='vcgMemberSkLcasRecvCtrl'
_e='vcgMemberSkRecvExpectSeq'
_d='vcgMemberSkRecvSeq'
_c='vcgMemberSoLcasState'
_b='vcgMemberSoLcasRecvMst'
_a='vcgMemberSoLcasSendCtrl'
_Z='vcgMemberSoSendSeq'
_Y='vcgMemberRowStatus'
_X='vcgMemberIfIndex'
_W='vcgRowStatus'
_V='vcgClearWtrTimer'
_U='vcgHoldOffTimer'
_T='vcgWtrTimer'
_S='vcgLcasEnabled'
_R='vcgType'
_Q='vcgSecondaryState'
_P='vcgOperationalState'
_O='vcgAdminState'
_N='vcgAssociatedEthernetPort'
_M='vcgIfIndex'
_L='vcgMemberIndex'
_K='slotIndex'
_J='shelfIndex'
_I='neIndex'
_H='read-create'
_G='read-write'
_F='vcgIndex'
_E='Integer32'
_D='CM-ENTITY-MIB'
_C='read-only'
_B='F3-EOTDM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsp150cm,=mibBuilder.importSymbols('ADVA-MIB','fsp150cm')
AdminState,OperationalState,SecondaryState=mibBuilder.importSymbols('CM-COMMON-MIB','AdminState','OperationalState','SecondaryState')
neIndex,shelfIndex,slotIndex=mibBuilder.importSymbols(_D,_I,_J,_K)
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention,TruthValue,VariablePointer=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','StorageType','TextualConvention','TruthValue','VariablePointer')
f3EOTDMMIB=ModuleIdentity((1,3,6,1,4,1,2544,1,12,17))
if mibBuilder.loadTexts:f3EOTDMMIB.setRevisions(('2012-05-10 00:00',))
class VcgType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('none',0),('t1',1),('e1',2),('t3',3),('e3',4),('vc12',5),('vc3',6),('vc4',7),('vt15',8),('sts1',9),('sts3c',10)))
class WtrTime(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,12))
class HoldOffTime(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
class CtrlState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*(('ctrlNotAppl',0),('ctrlFixed',1),('ctrlAdd',2),('ctrlNorm',3),('ctrlEos',4),('ctrlIdle',5),('ctrlDnu',6)))
class LcasSoState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('srcNotAppl',0),('srcIdle',1),('srcAdd',2),('srcNorm',3),('srcDnu',4),('srcRemove',5)))
class MstState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('mstNotAppl',0),('mstOk',1),('mstFail',2)))
class LcasSkState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('sinkNotAppl',0),('sinkIdle',1),('sinkOk',2),('sinkFail',3)))
_F3EotdmObjects_ObjectIdentity=ObjectIdentity
f3EotdmObjects=_F3EotdmObjects_ObjectIdentity((1,3,6,1,4,1,2544,1,12,17,1))
_VcgTable_Object=MibTable
vcgTable=_VcgTable_Object((1,3,6,1,4,1,2544,1,12,17,1,1))
if mibBuilder.loadTexts:vcgTable.setStatus(_A)
_VcgEntry_Object=MibTableRow
vcgEntry=_VcgEntry_Object((1,3,6,1,4,1,2544,1,12,17,1,1,1))
vcgEntry.setIndexNames((0,_D,_I),(0,_D,_J),(0,_D,_K),(0,_B,_F))
if mibBuilder.loadTexts:vcgEntry.setStatus(_A)
class _VcgIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_VcgIndex_Type.__name__=_E
_VcgIndex_Object=MibTableColumn
vcgIndex=_VcgIndex_Object((1,3,6,1,4,1,2544,1,12,17,1,1,1,1),_VcgIndex_Type())
vcgIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:vcgIndex.setStatus(_A)
_VcgIfIndex_Type=InterfaceIndex
_VcgIfIndex_Object=MibTableColumn
vcgIfIndex=_VcgIfIndex_Object((1,3,6,1,4,1,2544,1,12,17,1,1,1,2),_VcgIfIndex_Type())
vcgIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:vcgIfIndex.setStatus(_A)
_VcgAssociatedEthernetPort_Type=VariablePointer
_VcgAssociatedEthernetPort_Object=MibTableColumn
vcgAssociatedEthernetPort=_VcgAssociatedEthernetPort_Object((1,3,6,1,4,1,2544,1,12,17,1,1,1,3),_VcgAssociatedEthernetPort_Type())
vcgAssociatedEthernetPort.setMaxAccess(_C)
if mibBuilder.loadTexts:vcgAssociatedEthernetPort.setStatus(_A)
_VcgAdminState_Type=AdminState
_VcgAdminState_Object=MibTableColumn
vcgAdminState=_VcgAdminState_Object((1,3,6,1,4,1,2544,1,12,17,1,1,1,4),_VcgAdminState_Type())
vcgAdminState.setMaxAccess(_G)
if mibBuilder.loadTexts:vcgAdminState.setStatus(_A)
_VcgOperationalState_Type=OperationalState
_VcgOperationalState_Object=MibTableColumn
vcgOperationalState=_VcgOperationalState_Object((1,3,6,1,4,1,2544,1,12,17,1,1,1,5),_VcgOperationalState_Type())
vcgOperationalState.setMaxAccess(_C)
if mibBuilder.loadTexts:vcgOperationalState.setStatus(_A)
_VcgSecondaryState_Type=SecondaryState
_VcgSecondaryState_Object=MibTableColumn
vcgSecondaryState=_VcgSecondaryState_Object((1,3,6,1,4,1,2544,1,12,17,1,1,1,6),_VcgSecondaryState_Type())
vcgSecondaryState.setMaxAccess(_C)
if mibBuilder.loadTexts:vcgSecondaryState.setStatus(_A)
_VcgType_Type=VcgType
_VcgType_Object=MibTableColumn
vcgType=_VcgType_Object((1,3,6,1,4,1,2544,1,12,17,1,1,1,7),_VcgType_Type())
vcgType.setMaxAccess(_C)
if mibBuilder.loadTexts:vcgType.setStatus(_A)
_VcgLcasEnabled_Type=TruthValue
_VcgLcasEnabled_Object=MibTableColumn
vcgLcasEnabled=_VcgLcasEnabled_Object((1,3,6,1,4,1,2544,1,12,17,1,1,1,8),_VcgLcasEnabled_Type())
vcgLcasEnabled.setMaxAccess(_G)
if mibBuilder.loadTexts:vcgLcasEnabled.setStatus(_A)
_VcgWtrTimer_Type=WtrTime
_VcgWtrTimer_Object=MibTableColumn
vcgWtrTimer=_VcgWtrTimer_Object((1,3,6,1,4,1,2544,1,12,17,1,1,1,9),_VcgWtrTimer_Type())
vcgWtrTimer.setMaxAccess(_G)
if mibBuilder.loadTexts:vcgWtrTimer.setStatus(_A)
_VcgHoldOffTimer_Type=HoldOffTime
_VcgHoldOffTimer_Object=MibTableColumn
vcgHoldOffTimer=_VcgHoldOffTimer_Object((1,3,6,1,4,1,2544,1,12,17,1,1,1,10),_VcgHoldOffTimer_Type())
vcgHoldOffTimer.setMaxAccess(_G)
if mibBuilder.loadTexts:vcgHoldOffTimer.setStatus(_A)
class _VcgClearWtrTimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_VcgClearWtrTimer_Type.__name__=_E
_VcgClearWtrTimer_Object=MibTableColumn
vcgClearWtrTimer=_VcgClearWtrTimer_Object((1,3,6,1,4,1,2544,1,12,17,1,1,1,11),_VcgClearWtrTimer_Type())
vcgClearWtrTimer.setMaxAccess(_H)
if mibBuilder.loadTexts:vcgClearWtrTimer.setStatus(_A)
_VcgRowStatus_Type=RowStatus
_VcgRowStatus_Object=MibTableColumn
vcgRowStatus=_VcgRowStatus_Object((1,3,6,1,4,1,2544,1,12,17,1,1,1,12),_VcgRowStatus_Type())
vcgRowStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:vcgRowStatus.setStatus(_A)
_VcgMemberTable_Object=MibTable
vcgMemberTable=_VcgMemberTable_Object((1,3,6,1,4,1,2544,1,12,17,1,2))
if mibBuilder.loadTexts:vcgMemberTable.setStatus(_A)
_VcgMemberEntry_Object=MibTableRow
vcgMemberEntry=_VcgMemberEntry_Object((1,3,6,1,4,1,2544,1,12,17,1,2,1))
vcgMemberEntry.setIndexNames((0,_D,_I),(0,_D,_J),(0,_D,_K),(0,_B,_F),(0,_B,_L))
if mibBuilder.loadTexts:vcgMemberEntry.setStatus(_A)
_VcgMemberIndex_Type=Integer32
_VcgMemberIndex_Object=MibTableColumn
vcgMemberIndex=_VcgMemberIndex_Object((1,3,6,1,4,1,2544,1,12,17,1,2,1,1),_VcgMemberIndex_Type())
vcgMemberIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:vcgMemberIndex.setStatus(_A)
_VcgMemberIfIndex_Type=InterfaceIndex
_VcgMemberIfIndex_Object=MibTableColumn
vcgMemberIfIndex=_VcgMemberIfIndex_Object((1,3,6,1,4,1,2544,1,12,17,1,2,1,2),_VcgMemberIfIndex_Type())
vcgMemberIfIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:vcgMemberIfIndex.setStatus(_A)
_VcgMemberRowStatus_Type=RowStatus
_VcgMemberRowStatus_Object=MibTableColumn
vcgMemberRowStatus=_VcgMemberRowStatus_Object((1,3,6,1,4,1,2544,1,12,17,1,2,1,3),_VcgMemberRowStatus_Type())
vcgMemberRowStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:vcgMemberRowStatus.setStatus(_A)
class _VcgMemberSoSendSeq_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,63))
_VcgMemberSoSendSeq_Type.__name__=_E
_VcgMemberSoSendSeq_Object=MibTableColumn
vcgMemberSoSendSeq=_VcgMemberSoSendSeq_Object((1,3,6,1,4,1,2544,1,12,17,1,2,1,4),_VcgMemberSoSendSeq_Type())
vcgMemberSoSendSeq.setMaxAccess(_C)
if mibBuilder.loadTexts:vcgMemberSoSendSeq.setStatus(_A)
_VcgMemberSoLcasSendCtrl_Type=CtrlState
_VcgMemberSoLcasSendCtrl_Object=MibTableColumn
vcgMemberSoLcasSendCtrl=_VcgMemberSoLcasSendCtrl_Object((1,3,6,1,4,1,2544,1,12,17,1,2,1,5),_VcgMemberSoLcasSendCtrl_Type())
vcgMemberSoLcasSendCtrl.setMaxAccess(_C)
if mibBuilder.loadTexts:vcgMemberSoLcasSendCtrl.setStatus(_A)
_VcgMemberSoLcasRecvMst_Type=MstState
_VcgMemberSoLcasRecvMst_Object=MibTableColumn
vcgMemberSoLcasRecvMst=_VcgMemberSoLcasRecvMst_Object((1,3,6,1,4,1,2544,1,12,17,1,2,1,6),_VcgMemberSoLcasRecvMst_Type())
vcgMemberSoLcasRecvMst.setMaxAccess(_C)
if mibBuilder.loadTexts:vcgMemberSoLcasRecvMst.setStatus(_A)
_VcgMemberSoLcasState_Type=LcasSoState
_VcgMemberSoLcasState_Object=MibTableColumn
vcgMemberSoLcasState=_VcgMemberSoLcasState_Object((1,3,6,1,4,1,2544,1,12,17,1,2,1,7),_VcgMemberSoLcasState_Type())
vcgMemberSoLcasState.setMaxAccess(_C)
if mibBuilder.loadTexts:vcgMemberSoLcasState.setStatus(_A)
class _VcgMemberSkRecvSeq_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,63))
_VcgMemberSkRecvSeq_Type.__name__=_E
_VcgMemberSkRecvSeq_Object=MibTableColumn
vcgMemberSkRecvSeq=_VcgMemberSkRecvSeq_Object((1,3,6,1,4,1,2544,1,12,17,1,2,1,8),_VcgMemberSkRecvSeq_Type())
vcgMemberSkRecvSeq.setMaxAccess(_C)
if mibBuilder.loadTexts:vcgMemberSkRecvSeq.setStatus(_A)
class _VcgMemberSkRecvExpectSeq_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,63))
_VcgMemberSkRecvExpectSeq_Type.__name__=_E
_VcgMemberSkRecvExpectSeq_Object=MibTableColumn
vcgMemberSkRecvExpectSeq=_VcgMemberSkRecvExpectSeq_Object((1,3,6,1,4,1,2544,1,12,17,1,2,1,9),_VcgMemberSkRecvExpectSeq_Type())
vcgMemberSkRecvExpectSeq.setMaxAccess(_C)
if mibBuilder.loadTexts:vcgMemberSkRecvExpectSeq.setStatus(_A)
_VcgMemberSkLcasRecvCtrl_Type=CtrlState
_VcgMemberSkLcasRecvCtrl_Object=MibTableColumn
vcgMemberSkLcasRecvCtrl=_VcgMemberSkLcasRecvCtrl_Object((1,3,6,1,4,1,2544,1,12,17,1,2,1,10),_VcgMemberSkLcasRecvCtrl_Type())
vcgMemberSkLcasRecvCtrl.setMaxAccess(_C)
if mibBuilder.loadTexts:vcgMemberSkLcasRecvCtrl.setStatus(_A)
_VcgMemberSkLcasSendMst_Type=MstState
_VcgMemberSkLcasSendMst_Object=MibTableColumn
vcgMemberSkLcasSendMst=_VcgMemberSkLcasSendMst_Object((1,3,6,1,4,1,2544,1,12,17,1,2,1,11),_VcgMemberSkLcasSendMst_Type())
vcgMemberSkLcasSendMst.setMaxAccess(_C)
if mibBuilder.loadTexts:vcgMemberSkLcasSendMst.setStatus(_A)
_VcgMemberSkLcasState_Type=LcasSkState
_VcgMemberSkLcasState_Object=MibTableColumn
vcgMemberSkLcasState=_VcgMemberSkLcasState_Object((1,3,6,1,4,1,2544,1,12,17,1,2,1,12),_VcgMemberSkLcasState_Type())
vcgMemberSkLcasState.setMaxAccess(_C)
if mibBuilder.loadTexts:vcgMemberSkLcasState.setStatus(_A)
_F3EotdmConformance_ObjectIdentity=ObjectIdentity
f3EotdmConformance=_F3EotdmConformance_ObjectIdentity((1,3,6,1,4,1,2544,1,12,17,2))
_F3EotdmCompliances_ObjectIdentity=ObjectIdentity
f3EotdmCompliances=_F3EotdmCompliances_ObjectIdentity((1,3,6,1,4,1,2544,1,12,17,2,1))
_F3EotdmGroups_ObjectIdentity=ObjectIdentity
f3EotdmGroups=_F3EotdmGroups_ObjectIdentity((1,3,6,1,4,1,2544,1,12,17,2,2))
f3EotdmObjectGroup=ObjectGroup((1,3,6,1,4,1,2544,1,12,17,2,2,1))
f3EotdmObjectGroup.setObjects(*((_B,_F),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_L),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h)))
if mibBuilder.loadTexts:f3EotdmObjectGroup.setStatus(_A)
f3EotdmCompliance=ModuleCompliance((1,3,6,1,4,1,2544,1,12,17,2,1,1))
f3EotdmCompliance.setObjects((_B,_i))
if mibBuilder.loadTexts:f3EotdmCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'VcgType':VcgType,'WtrTime':WtrTime,'HoldOffTime':HoldOffTime,'CtrlState':CtrlState,'LcasSoState':LcasSoState,'MstState':MstState,'LcasSkState':LcasSkState,'f3EOTDMMIB':f3EOTDMMIB,'f3EotdmObjects':f3EotdmObjects,'vcgTable':vcgTable,'vcgEntry':vcgEntry,_F:vcgIndex,_M:vcgIfIndex,_N:vcgAssociatedEthernetPort,_O:vcgAdminState,_P:vcgOperationalState,_Q:vcgSecondaryState,_R:vcgType,_S:vcgLcasEnabled,_T:vcgWtrTimer,_U:vcgHoldOffTimer,_V:vcgClearWtrTimer,_W:vcgRowStatus,'vcgMemberTable':vcgMemberTable,'vcgMemberEntry':vcgMemberEntry,_L:vcgMemberIndex,_X:vcgMemberIfIndex,_Y:vcgMemberRowStatus,_Z:vcgMemberSoSendSeq,_a:vcgMemberSoLcasSendCtrl,_b:vcgMemberSoLcasRecvMst,_c:vcgMemberSoLcasState,_d:vcgMemberSkRecvSeq,_e:vcgMemberSkRecvExpectSeq,_f:vcgMemberSkLcasRecvCtrl,_g:vcgMemberSkLcasSendMst,_h:vcgMemberSkLcasState,'f3EotdmConformance':f3EotdmConformance,'f3EotdmCompliances':f3EotdmCompliances,'f3EotdmCompliance':f3EotdmCompliance,'f3EotdmGroups':f3EotdmGroups,_i:f3EotdmObjectGroup})