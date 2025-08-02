_r='sleRouterMarkEntryChanged'
_q='sleRouterMarkEntryCreated'
_p='sleRouterMarkEntryDestroyed'
_o='sleInLIFMarkDscpChanged'
_n='sleInLIFMarkUpChanged'
_m='sleBridgePort2TCMarkChanged'
_l='sleMVQoS4InLIFMarkControlDSCP'
_k='sleMVQoS4InLIFMarkControlCoS'
_j='sleMVQoS4InLIFMarkControlPortIndex'
_i='sleMVQoS4InLIFMarkControlTimer'
_h='sleMVQoS4InLIFMarkControlStatus'
_g='sleMVQoS4RouterMarkControlCoS'
_f='sleMVQoS4RouterMarkControlDp'
_e='sleMVQoS4RouterMarkControlQueue'
_d='sleMVQoS4RouterMarkControlTimer'
_c='sleMVQoS4RouterMarkControlStatus'
_b='sleMVQoS4BridgePort2TCMarkControlQueue'
_a='sleMVQoS4BridgePort2TCMarkControlPortIndex'
_Z='sleMVQoS4BridgePort2TCMarkControlTimer'
_Y='sleMVQoS4BridgePort2TCMarkControlStatus'
_X='sleMVQoS4RouterMarkControlNextHop'
_W='sleMVQoS4BridgePort2TCMarkControlReqResult'
_V='sleMVQoS4BridgePort2TCMarkControlTmeStamp'
_U='sleMVQoS4BridgePort2TCMarkControlRequest'
_T='sleMVQoS4InLIFMarkDSCP'
_S='sleMVQoS4InLIFMarkCoS'
_R='sleMVQoS4BridgePort2TCMarkQueue'
_Q='sleMVQoS4RouterMarkNextHop'
_P='sleMVQoS4InLIFMarkPortIndex'
_O='sleMVQoS4BridgePort2TCMarkPortIndex'
_N='sleMVQoS4InLIFMarkControlReqResult'
_M='sleMVQoS4InLIFMarkControlTimeStamp'
_L='sleMVQoS4InLIFMarkControlRequest'
_K='sleMVQoS4RouterMarkCoS'
_J='sleMVQoS4RouterMarkDp'
_I='sleMVQoS4RouterMarkQueue'
_H='Integer32'
_G='sleMVQoS4RouterMarkControlReqResult'
_F='sleMVQoS4RouterMarkControlTimeStamp'
_E='sleMVQoS4RouterMarkControlRequest'
_D='read-only'
_C='read-write'
_B='current'
_A='SLE-MVQOS-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
sleMgmt,=mibBuilder.importSymbols('DASAN-SMI','sleMgmt')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
SleControlRequestResultType,SleControlStatusType=mibBuilder.importSymbols('SLE-TC-MIB','SleControlRequestResultType','SleControlStatusType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
sleMVQoS=ModuleIdentity((1,3,6,1,4,1,6296,101,14))
class IntQueue(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,7))
class IntQueueIndex(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
class IntEtherType(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,65535))
class IntEtherTypeIndex(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
class IntIpAddressMask(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,31))
class IntQueueDirection(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-1,1,2)));namedValues=NamedValues(*(('nothing',-1),('source',1),('destination',2)))
class IntCoS(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,7))
class IntCoSIndex(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
class IntDp(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,2))
class IntDSCP(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,63))
_SleMVQoSBase_ObjectIdentity=ObjectIdentity
sleMVQoSBase=_SleMVQoSBase_ObjectIdentity((1,3,6,1,4,1,6296,101,14,1))
_SleMVQoS4_ObjectIdentity=ObjectIdentity
sleMVQoS4=_SleMVQoS4_ObjectIdentity((1,3,6,1,4,1,6296,101,14,2))
_SleMVQoS4Base_ObjectIdentity=ObjectIdentity
sleMVQoS4Base=_SleMVQoS4Base_ObjectIdentity((1,3,6,1,4,1,6296,101,14,2,1))
_SleMVQoS4BridgeBase_ObjectIdentity=ObjectIdentity
sleMVQoS4BridgeBase=_SleMVQoS4BridgeBase_ObjectIdentity((1,3,6,1,4,1,6296,101,14,2,2))
_SleMVQoS4BridgePort2TCMark_ObjectIdentity=ObjectIdentity
sleMVQoS4BridgePort2TCMark=_SleMVQoS4BridgePort2TCMark_ObjectIdentity((1,3,6,1,4,1,6296,101,14,2,2,1))
_SleMVQoS4BridgePort2TCMarkTable_Object=MibTable
sleMVQoS4BridgePort2TCMarkTable=_SleMVQoS4BridgePort2TCMarkTable_Object((1,3,6,1,4,1,6296,101,14,2,2,1,1))
if mibBuilder.loadTexts:sleMVQoS4BridgePort2TCMarkTable.setStatus(_B)
_SleMVQoS4BridgePort2TCMarkEntry_Object=MibTableRow
sleMVQoS4BridgePort2TCMarkEntry=_SleMVQoS4BridgePort2TCMarkEntry_Object((1,3,6,1,4,1,6296,101,14,2,2,1,1,1))
sleMVQoS4BridgePort2TCMarkEntry.setIndexNames((0,_A,_O))
if mibBuilder.loadTexts:sleMVQoS4BridgePort2TCMarkEntry.setStatus(_B)
_SleMVQoS4BridgePort2TCMarkPortIndex_Type=InterfaceIndex
_SleMVQoS4BridgePort2TCMarkPortIndex_Object=MibTableColumn
sleMVQoS4BridgePort2TCMarkPortIndex=_SleMVQoS4BridgePort2TCMarkPortIndex_Object((1,3,6,1,4,1,6296,101,14,2,2,1,1,1,1),_SleMVQoS4BridgePort2TCMarkPortIndex_Type())
sleMVQoS4BridgePort2TCMarkPortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:sleMVQoS4BridgePort2TCMarkPortIndex.setStatus(_B)
_SleMVQoS4BridgePort2TCMarkQueue_Type=IntQueue
_SleMVQoS4BridgePort2TCMarkQueue_Object=MibTableColumn
sleMVQoS4BridgePort2TCMarkQueue=_SleMVQoS4BridgePort2TCMarkQueue_Object((1,3,6,1,4,1,6296,101,14,2,2,1,1,1,2),_SleMVQoS4BridgePort2TCMarkQueue_Type())
sleMVQoS4BridgePort2TCMarkQueue.setMaxAccess(_D)
if mibBuilder.loadTexts:sleMVQoS4BridgePort2TCMarkQueue.setStatus(_B)
_SleMVQoS4BridgePort2TCMarkControl_ObjectIdentity=ObjectIdentity
sleMVQoS4BridgePort2TCMarkControl=_SleMVQoS4BridgePort2TCMarkControl_ObjectIdentity((1,3,6,1,4,1,6296,101,14,2,2,1,2))
class _SleMVQoS4BridgePort2TCMarkControlRequest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('setBridgePort2TCMark',1))
_SleMVQoS4BridgePort2TCMarkControlRequest_Type.__name__=_H
_SleMVQoS4BridgePort2TCMarkControlRequest_Object=MibScalar
sleMVQoS4BridgePort2TCMarkControlRequest=_SleMVQoS4BridgePort2TCMarkControlRequest_Object((1,3,6,1,4,1,6296,101,14,2,2,1,2,1),_SleMVQoS4BridgePort2TCMarkControlRequest_Type())
sleMVQoS4BridgePort2TCMarkControlRequest.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMVQoS4BridgePort2TCMarkControlRequest.setStatus(_B)
_SleMVQoS4BridgePort2TCMarkControlStatus_Type=SleControlStatusType
_SleMVQoS4BridgePort2TCMarkControlStatus_Object=MibScalar
sleMVQoS4BridgePort2TCMarkControlStatus=_SleMVQoS4BridgePort2TCMarkControlStatus_Object((1,3,6,1,4,1,6296,101,14,2,2,1,2,2),_SleMVQoS4BridgePort2TCMarkControlStatus_Type())
sleMVQoS4BridgePort2TCMarkControlStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMVQoS4BridgePort2TCMarkControlStatus.setStatus(_B)
_SleMVQoS4BridgePort2TCMarkControlTimer_Type=Gauge32
_SleMVQoS4BridgePort2TCMarkControlTimer_Object=MibScalar
sleMVQoS4BridgePort2TCMarkControlTimer=_SleMVQoS4BridgePort2TCMarkControlTimer_Object((1,3,6,1,4,1,6296,101,14,2,2,1,2,3),_SleMVQoS4BridgePort2TCMarkControlTimer_Type())
sleMVQoS4BridgePort2TCMarkControlTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMVQoS4BridgePort2TCMarkControlTimer.setStatus(_B)
_SleMVQoS4BridgePort2TCMarkControlTmeStamp_Type=TimeTicks
_SleMVQoS4BridgePort2TCMarkControlTmeStamp_Object=MibScalar
sleMVQoS4BridgePort2TCMarkControlTmeStamp=_SleMVQoS4BridgePort2TCMarkControlTmeStamp_Object((1,3,6,1,4,1,6296,101,14,2,2,1,2,4),_SleMVQoS4BridgePort2TCMarkControlTmeStamp_Type())
sleMVQoS4BridgePort2TCMarkControlTmeStamp.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMVQoS4BridgePort2TCMarkControlTmeStamp.setStatus(_B)
_SleMVQoS4BridgePort2TCMarkControlReqResult_Type=SleControlRequestResultType
_SleMVQoS4BridgePort2TCMarkControlReqResult_Object=MibScalar
sleMVQoS4BridgePort2TCMarkControlReqResult=_SleMVQoS4BridgePort2TCMarkControlReqResult_Object((1,3,6,1,4,1,6296,101,14,2,2,1,2,5),_SleMVQoS4BridgePort2TCMarkControlReqResult_Type())
sleMVQoS4BridgePort2TCMarkControlReqResult.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMVQoS4BridgePort2TCMarkControlReqResult.setStatus(_B)
_SleMVQoS4BridgePort2TCMarkControlPortIndex_Type=InterfaceIndex
_SleMVQoS4BridgePort2TCMarkControlPortIndex_Object=MibScalar
sleMVQoS4BridgePort2TCMarkControlPortIndex=_SleMVQoS4BridgePort2TCMarkControlPortIndex_Object((1,3,6,1,4,1,6296,101,14,2,2,1,2,6),_SleMVQoS4BridgePort2TCMarkControlPortIndex_Type())
sleMVQoS4BridgePort2TCMarkControlPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMVQoS4BridgePort2TCMarkControlPortIndex.setStatus(_B)
_SleMVQoS4BridgePort2TCMarkControlQueue_Type=IntQueue
_SleMVQoS4BridgePort2TCMarkControlQueue_Object=MibScalar
sleMVQoS4BridgePort2TCMarkControlQueue=_SleMVQoS4BridgePort2TCMarkControlQueue_Object((1,3,6,1,4,1,6296,101,14,2,2,1,2,7),_SleMVQoS4BridgePort2TCMarkControlQueue_Type())
sleMVQoS4BridgePort2TCMarkControlQueue.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMVQoS4BridgePort2TCMarkControlQueue.setStatus(_B)
_SleMVQoS4BridgePort2TCMarkNotification_ObjectIdentity=ObjectIdentity
sleMVQoS4BridgePort2TCMarkNotification=_SleMVQoS4BridgePort2TCMarkNotification_ObjectIdentity((1,3,6,1,4,1,6296,101,14,2,2,1,3))
_SleMVQoS4InLIF_ObjectIdentity=ObjectIdentity
sleMVQoS4InLIF=_SleMVQoS4InLIF_ObjectIdentity((1,3,6,1,4,1,6296,101,14,2,3))
_SleMVQoS4InLIFMark_ObjectIdentity=ObjectIdentity
sleMVQoS4InLIFMark=_SleMVQoS4InLIFMark_ObjectIdentity((1,3,6,1,4,1,6296,101,14,2,3,1))
_SleMVQoS4InLIFMarkTable_Object=MibTable
sleMVQoS4InLIFMarkTable=_SleMVQoS4InLIFMarkTable_Object((1,3,6,1,4,1,6296,101,14,2,3,1,1))
if mibBuilder.loadTexts:sleMVQoS4InLIFMarkTable.setStatus(_B)
_SleMVQoS4InLIFMarkEntry_Object=MibTableRow
sleMVQoS4InLIFMarkEntry=_SleMVQoS4InLIFMarkEntry_Object((1,3,6,1,4,1,6296,101,14,2,3,1,1,1))
sleMVQoS4InLIFMarkEntry.setIndexNames((0,_A,_P))
if mibBuilder.loadTexts:sleMVQoS4InLIFMarkEntry.setStatus(_B)
_SleMVQoS4InLIFMarkPortIndex_Type=InterfaceIndex
_SleMVQoS4InLIFMarkPortIndex_Object=MibTableColumn
sleMVQoS4InLIFMarkPortIndex=_SleMVQoS4InLIFMarkPortIndex_Object((1,3,6,1,4,1,6296,101,14,2,3,1,1,1,1),_SleMVQoS4InLIFMarkPortIndex_Type())
sleMVQoS4InLIFMarkPortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:sleMVQoS4InLIFMarkPortIndex.setStatus(_B)
_SleMVQoS4InLIFMarkCoS_Type=IntCoS
_SleMVQoS4InLIFMarkCoS_Object=MibTableColumn
sleMVQoS4InLIFMarkCoS=_SleMVQoS4InLIFMarkCoS_Object((1,3,6,1,4,1,6296,101,14,2,3,1,1,1,2),_SleMVQoS4InLIFMarkCoS_Type())
sleMVQoS4InLIFMarkCoS.setMaxAccess(_D)
if mibBuilder.loadTexts:sleMVQoS4InLIFMarkCoS.setStatus(_B)
_SleMVQoS4InLIFMarkDSCP_Type=IntDSCP
_SleMVQoS4InLIFMarkDSCP_Object=MibTableColumn
sleMVQoS4InLIFMarkDSCP=_SleMVQoS4InLIFMarkDSCP_Object((1,3,6,1,4,1,6296,101,14,2,3,1,1,1,3),_SleMVQoS4InLIFMarkDSCP_Type())
sleMVQoS4InLIFMarkDSCP.setMaxAccess(_D)
if mibBuilder.loadTexts:sleMVQoS4InLIFMarkDSCP.setStatus(_B)
_SleMVQoS4InLIFMarkControl_ObjectIdentity=ObjectIdentity
sleMVQoS4InLIFMarkControl=_SleMVQoS4InLIFMarkControl_ObjectIdentity((1,3,6,1,4,1,6296,101,14,2,3,1,2))
class _SleMVQoS4InLIFMarkControlRequest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('setInLIFUp',1),('setInLIFDscp',2)))
_SleMVQoS4InLIFMarkControlRequest_Type.__name__=_H
_SleMVQoS4InLIFMarkControlRequest_Object=MibScalar
sleMVQoS4InLIFMarkControlRequest=_SleMVQoS4InLIFMarkControlRequest_Object((1,3,6,1,4,1,6296,101,14,2,3,1,2,1),_SleMVQoS4InLIFMarkControlRequest_Type())
sleMVQoS4InLIFMarkControlRequest.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMVQoS4InLIFMarkControlRequest.setStatus(_B)
_SleMVQoS4InLIFMarkControlStatus_Type=SleControlStatusType
_SleMVQoS4InLIFMarkControlStatus_Object=MibScalar
sleMVQoS4InLIFMarkControlStatus=_SleMVQoS4InLIFMarkControlStatus_Object((1,3,6,1,4,1,6296,101,14,2,3,1,2,2),_SleMVQoS4InLIFMarkControlStatus_Type())
sleMVQoS4InLIFMarkControlStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMVQoS4InLIFMarkControlStatus.setStatus(_B)
_SleMVQoS4InLIFMarkControlTimer_Type=Gauge32
_SleMVQoS4InLIFMarkControlTimer_Object=MibScalar
sleMVQoS4InLIFMarkControlTimer=_SleMVQoS4InLIFMarkControlTimer_Object((1,3,6,1,4,1,6296,101,14,2,3,1,2,3),_SleMVQoS4InLIFMarkControlTimer_Type())
sleMVQoS4InLIFMarkControlTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMVQoS4InLIFMarkControlTimer.setStatus(_B)
_SleMVQoS4InLIFMarkControlTimeStamp_Type=TimeTicks
_SleMVQoS4InLIFMarkControlTimeStamp_Object=MibScalar
sleMVQoS4InLIFMarkControlTimeStamp=_SleMVQoS4InLIFMarkControlTimeStamp_Object((1,3,6,1,4,1,6296,101,14,2,3,1,2,4),_SleMVQoS4InLIFMarkControlTimeStamp_Type())
sleMVQoS4InLIFMarkControlTimeStamp.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMVQoS4InLIFMarkControlTimeStamp.setStatus(_B)
_SleMVQoS4InLIFMarkControlReqResult_Type=SleControlRequestResultType
_SleMVQoS4InLIFMarkControlReqResult_Object=MibScalar
sleMVQoS4InLIFMarkControlReqResult=_SleMVQoS4InLIFMarkControlReqResult_Object((1,3,6,1,4,1,6296,101,14,2,3,1,2,5),_SleMVQoS4InLIFMarkControlReqResult_Type())
sleMVQoS4InLIFMarkControlReqResult.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMVQoS4InLIFMarkControlReqResult.setStatus(_B)
_SleMVQoS4InLIFMarkControlPortIndex_Type=InterfaceIndex
_SleMVQoS4InLIFMarkControlPortIndex_Object=MibScalar
sleMVQoS4InLIFMarkControlPortIndex=_SleMVQoS4InLIFMarkControlPortIndex_Object((1,3,6,1,4,1,6296,101,14,2,3,1,2,6),_SleMVQoS4InLIFMarkControlPortIndex_Type())
sleMVQoS4InLIFMarkControlPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMVQoS4InLIFMarkControlPortIndex.setStatus(_B)
_SleMVQoS4InLIFMarkControlCoS_Type=IntCoS
_SleMVQoS4InLIFMarkControlCoS_Object=MibScalar
sleMVQoS4InLIFMarkControlCoS=_SleMVQoS4InLIFMarkControlCoS_Object((1,3,6,1,4,1,6296,101,14,2,3,1,2,7),_SleMVQoS4InLIFMarkControlCoS_Type())
sleMVQoS4InLIFMarkControlCoS.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMVQoS4InLIFMarkControlCoS.setStatus(_B)
_SleMVQoS4InLIFMarkControlDSCP_Type=IntDSCP
_SleMVQoS4InLIFMarkControlDSCP_Object=MibScalar
sleMVQoS4InLIFMarkControlDSCP=_SleMVQoS4InLIFMarkControlDSCP_Object((1,3,6,1,4,1,6296,101,14,2,3,1,2,8),_SleMVQoS4InLIFMarkControlDSCP_Type())
sleMVQoS4InLIFMarkControlDSCP.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMVQoS4InLIFMarkControlDSCP.setStatus(_B)
_SleMVQoS4InLIFMarkNotification_ObjectIdentity=ObjectIdentity
sleMVQoS4InLIFMarkNotification=_SleMVQoS4InLIFMarkNotification_ObjectIdentity((1,3,6,1,4,1,6296,101,14,2,3,1,3))
_SleMVQoS4Router_ObjectIdentity=ObjectIdentity
sleMVQoS4Router=_SleMVQoS4Router_ObjectIdentity((1,3,6,1,4,1,6296,101,14,2,4))
_SleMVQoS4RouterMark_ObjectIdentity=ObjectIdentity
sleMVQoS4RouterMark=_SleMVQoS4RouterMark_ObjectIdentity((1,3,6,1,4,1,6296,101,14,2,4,1))
_SleMVQoS4RouterMarkTable_Object=MibTable
sleMVQoS4RouterMarkTable=_SleMVQoS4RouterMarkTable_Object((1,3,6,1,4,1,6296,101,14,2,4,1,1))
if mibBuilder.loadTexts:sleMVQoS4RouterMarkTable.setStatus(_B)
_SleMVQoS4RouterMarkEntry_Object=MibTableRow
sleMVQoS4RouterMarkEntry=_SleMVQoS4RouterMarkEntry_Object((1,3,6,1,4,1,6296,101,14,2,4,1,1,1))
sleMVQoS4RouterMarkEntry.setIndexNames((0,_A,_Q))
if mibBuilder.loadTexts:sleMVQoS4RouterMarkEntry.setStatus(_B)
_SleMVQoS4RouterMarkNextHop_Type=IpAddress
_SleMVQoS4RouterMarkNextHop_Object=MibTableColumn
sleMVQoS4RouterMarkNextHop=_SleMVQoS4RouterMarkNextHop_Object((1,3,6,1,4,1,6296,101,14,2,4,1,1,1,1),_SleMVQoS4RouterMarkNextHop_Type())
sleMVQoS4RouterMarkNextHop.setMaxAccess(_D)
if mibBuilder.loadTexts:sleMVQoS4RouterMarkNextHop.setStatus(_B)
_SleMVQoS4RouterMarkQueue_Type=IntQueue
_SleMVQoS4RouterMarkQueue_Object=MibTableColumn
sleMVQoS4RouterMarkQueue=_SleMVQoS4RouterMarkQueue_Object((1,3,6,1,4,1,6296,101,14,2,4,1,1,1,2),_SleMVQoS4RouterMarkQueue_Type())
sleMVQoS4RouterMarkQueue.setMaxAccess(_D)
if mibBuilder.loadTexts:sleMVQoS4RouterMarkQueue.setStatus(_B)
_SleMVQoS4RouterMarkDp_Type=IntDp
_SleMVQoS4RouterMarkDp_Object=MibTableColumn
sleMVQoS4RouterMarkDp=_SleMVQoS4RouterMarkDp_Object((1,3,6,1,4,1,6296,101,14,2,4,1,1,1,3),_SleMVQoS4RouterMarkDp_Type())
sleMVQoS4RouterMarkDp.setMaxAccess(_D)
if mibBuilder.loadTexts:sleMVQoS4RouterMarkDp.setStatus(_B)
_SleMVQoS4RouterMarkCoS_Type=IntCoS
_SleMVQoS4RouterMarkCoS_Object=MibTableColumn
sleMVQoS4RouterMarkCoS=_SleMVQoS4RouterMarkCoS_Object((1,3,6,1,4,1,6296,101,14,2,4,1,1,1,4),_SleMVQoS4RouterMarkCoS_Type())
sleMVQoS4RouterMarkCoS.setMaxAccess(_D)
if mibBuilder.loadTexts:sleMVQoS4RouterMarkCoS.setStatus(_B)
_SleMVQoS4RouterMarkControl_ObjectIdentity=ObjectIdentity
sleMVQoS4RouterMarkControl=_SleMVQoS4RouterMarkControl_ObjectIdentity((1,3,6,1,4,1,6296,101,14,2,4,1,2))
class _SleMVQoS4RouterMarkControlRequest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('createRouterMarkEntry',1),('setRouterMarkEntry',2),('destroyRouterMarkEntry',3)))
_SleMVQoS4RouterMarkControlRequest_Type.__name__=_H
_SleMVQoS4RouterMarkControlRequest_Object=MibScalar
sleMVQoS4RouterMarkControlRequest=_SleMVQoS4RouterMarkControlRequest_Object((1,3,6,1,4,1,6296,101,14,2,4,1,2,1),_SleMVQoS4RouterMarkControlRequest_Type())
sleMVQoS4RouterMarkControlRequest.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMVQoS4RouterMarkControlRequest.setStatus(_B)
_SleMVQoS4RouterMarkControlStatus_Type=SleControlStatusType
_SleMVQoS4RouterMarkControlStatus_Object=MibScalar
sleMVQoS4RouterMarkControlStatus=_SleMVQoS4RouterMarkControlStatus_Object((1,3,6,1,4,1,6296,101,14,2,4,1,2,2),_SleMVQoS4RouterMarkControlStatus_Type())
sleMVQoS4RouterMarkControlStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMVQoS4RouterMarkControlStatus.setStatus(_B)
_SleMVQoS4RouterMarkControlTimer_Type=Gauge32
_SleMVQoS4RouterMarkControlTimer_Object=MibScalar
sleMVQoS4RouterMarkControlTimer=_SleMVQoS4RouterMarkControlTimer_Object((1,3,6,1,4,1,6296,101,14,2,4,1,2,3),_SleMVQoS4RouterMarkControlTimer_Type())
sleMVQoS4RouterMarkControlTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMVQoS4RouterMarkControlTimer.setStatus(_B)
_SleMVQoS4RouterMarkControlTimeStamp_Type=TimeTicks
_SleMVQoS4RouterMarkControlTimeStamp_Object=MibScalar
sleMVQoS4RouterMarkControlTimeStamp=_SleMVQoS4RouterMarkControlTimeStamp_Object((1,3,6,1,4,1,6296,101,14,2,4,1,2,4),_SleMVQoS4RouterMarkControlTimeStamp_Type())
sleMVQoS4RouterMarkControlTimeStamp.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMVQoS4RouterMarkControlTimeStamp.setStatus(_B)
_SleMVQoS4RouterMarkControlReqResult_Type=SleControlRequestResultType
_SleMVQoS4RouterMarkControlReqResult_Object=MibScalar
sleMVQoS4RouterMarkControlReqResult=_SleMVQoS4RouterMarkControlReqResult_Object((1,3,6,1,4,1,6296,101,14,2,4,1,2,5),_SleMVQoS4RouterMarkControlReqResult_Type())
sleMVQoS4RouterMarkControlReqResult.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMVQoS4RouterMarkControlReqResult.setStatus(_B)
_SleMVQoS4RouterMarkControlNextHop_Type=IpAddress
_SleMVQoS4RouterMarkControlNextHop_Object=MibScalar
sleMVQoS4RouterMarkControlNextHop=_SleMVQoS4RouterMarkControlNextHop_Object((1,3,6,1,4,1,6296,101,14,2,4,1,2,6),_SleMVQoS4RouterMarkControlNextHop_Type())
sleMVQoS4RouterMarkControlNextHop.setMaxAccess(_D)
if mibBuilder.loadTexts:sleMVQoS4RouterMarkControlNextHop.setStatus(_B)
_SleMVQoS4RouterMarkControlQueue_Type=IntQueue
_SleMVQoS4RouterMarkControlQueue_Object=MibScalar
sleMVQoS4RouterMarkControlQueue=_SleMVQoS4RouterMarkControlQueue_Object((1,3,6,1,4,1,6296,101,14,2,4,1,2,7),_SleMVQoS4RouterMarkControlQueue_Type())
sleMVQoS4RouterMarkControlQueue.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMVQoS4RouterMarkControlQueue.setStatus(_B)
_SleMVQoS4RouterMarkControlDp_Type=IntDp
_SleMVQoS4RouterMarkControlDp_Object=MibScalar
sleMVQoS4RouterMarkControlDp=_SleMVQoS4RouterMarkControlDp_Object((1,3,6,1,4,1,6296,101,14,2,4,1,2,8),_SleMVQoS4RouterMarkControlDp_Type())
sleMVQoS4RouterMarkControlDp.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMVQoS4RouterMarkControlDp.setStatus(_B)
_SleMVQoS4RouterMarkControlCoS_Type=IntCoS
_SleMVQoS4RouterMarkControlCoS_Object=MibScalar
sleMVQoS4RouterMarkControlCoS=_SleMVQoS4RouterMarkControlCoS_Object((1,3,6,1,4,1,6296,101,14,2,4,1,2,9),_SleMVQoS4RouterMarkControlCoS_Type())
sleMVQoS4RouterMarkControlCoS.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMVQoS4RouterMarkControlCoS.setStatus(_B)
_SleMVQoS4RouterMarkNotification_ObjectIdentity=ObjectIdentity
sleMVQoS4RouterMarkNotification=_SleMVQoS4RouterMarkNotification_ObjectIdentity((1,3,6,1,4,1,6296,101,14,2,4,1,3))
_SleMVQoS6_ObjectIdentity=ObjectIdentity
sleMVQoS6=_SleMVQoS6_ObjectIdentity((1,3,6,1,4,1,6296,101,14,3))
sleMVQoSGroup=ObjectGroup((1,3,6,1,4,1,6296,101,14,4))
sleMVQoSGroup.setObjects(*((_A,_O),(_A,_R),(_A,_P),(_A,_S),(_A,_T),(_A,_Q),(_A,_I),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:sleMVQoSGroup.setStatus(_B)
sleMVQoSControlGroup=ObjectGroup((1,3,6,1,4,1,6296,101,14,5))
sleMVQoSControlGroup.setObjects(*((_A,_U),(_A,_Y),(_A,_Z),(_A,_V),(_A,_W),(_A,_a),(_A,_b),(_A,_E),(_A,_c),(_A,_d),(_A,_F),(_A,_G),(_A,_X),(_A,_e),(_A,_f),(_A,_g),(_A,_L),(_A,_h),(_A,_i),(_A,_M),(_A,_N),(_A,_j),(_A,_k),(_A,_l)))
if mibBuilder.loadTexts:sleMVQoSControlGroup.setStatus(_B)
sleBridgePort2TCMarkChanged=NotificationType((1,3,6,1,4,1,6296,101,14,2,2,1,3,1))
sleBridgePort2TCMarkChanged.setObjects(*((_A,_U),(_A,_V),(_A,_W),(_A,_R)))
if mibBuilder.loadTexts:sleBridgePort2TCMarkChanged.setStatus(_B)
sleInLIFMarkUpChanged=NotificationType((1,3,6,1,4,1,6296,101,14,2,3,1,3,1))
sleInLIFMarkUpChanged.setObjects(*((_A,_L),(_A,_M),(_A,_N),(_A,_S)))
if mibBuilder.loadTexts:sleInLIFMarkUpChanged.setStatus(_B)
sleInLIFMarkDscpChanged=NotificationType((1,3,6,1,4,1,6296,101,14,2,3,1,3,2))
sleInLIFMarkDscpChanged.setObjects(*((_A,_L),(_A,_M),(_A,_N),(_A,_T)))
if mibBuilder.loadTexts:sleInLIFMarkDscpChanged.setStatus(_B)
sleRouterMarkEntryCreated=NotificationType((1,3,6,1,4,1,6296,101,14,2,4,1,3,1))
sleRouterMarkEntryCreated.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_I),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:sleRouterMarkEntryCreated.setStatus(_B)
sleRouterMarkEntryChanged=NotificationType((1,3,6,1,4,1,6296,101,14,2,4,1,3,2))
sleRouterMarkEntryChanged.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_I),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:sleRouterMarkEntryChanged.setStatus(_B)
sleRouterMarkEntryDestroyed=NotificationType((1,3,6,1,4,1,6296,101,14,2,4,1,3,3))
sleRouterMarkEntryDestroyed.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_X)))
if mibBuilder.loadTexts:sleRouterMarkEntryDestroyed.setStatus(_B)
sleMVQoSNotificationGroup=NotificationGroup((1,3,6,1,4,1,6296,101,14,6))
sleMVQoSNotificationGroup.setObjects(*((_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r)))
if mibBuilder.loadTexts:sleMVQoSNotificationGroup.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'IntQueue':IntQueue,'IntQueueIndex':IntQueueIndex,'IntEtherType':IntEtherType,'IntEtherTypeIndex':IntEtherTypeIndex,'IntIpAddressMask':IntIpAddressMask,'IntQueueDirection':IntQueueDirection,'IntCoS':IntCoS,'IntCoSIndex':IntCoSIndex,'IntDp':IntDp,'IntDSCP':IntDSCP,'sleMVQoS':sleMVQoS,'sleMVQoSBase':sleMVQoSBase,'sleMVQoS4':sleMVQoS4,'sleMVQoS4Base':sleMVQoS4Base,'sleMVQoS4BridgeBase':sleMVQoS4BridgeBase,'sleMVQoS4BridgePort2TCMark':sleMVQoS4BridgePort2TCMark,'sleMVQoS4BridgePort2TCMarkTable':sleMVQoS4BridgePort2TCMarkTable,'sleMVQoS4BridgePort2TCMarkEntry':sleMVQoS4BridgePort2TCMarkEntry,_O:sleMVQoS4BridgePort2TCMarkPortIndex,_R:sleMVQoS4BridgePort2TCMarkQueue,'sleMVQoS4BridgePort2TCMarkControl':sleMVQoS4BridgePort2TCMarkControl,_U:sleMVQoS4BridgePort2TCMarkControlRequest,_Y:sleMVQoS4BridgePort2TCMarkControlStatus,_Z:sleMVQoS4BridgePort2TCMarkControlTimer,_V:sleMVQoS4BridgePort2TCMarkControlTmeStamp,_W:sleMVQoS4BridgePort2TCMarkControlReqResult,_a:sleMVQoS4BridgePort2TCMarkControlPortIndex,_b:sleMVQoS4BridgePort2TCMarkControlQueue,'sleMVQoS4BridgePort2TCMarkNotification':sleMVQoS4BridgePort2TCMarkNotification,_m:sleBridgePort2TCMarkChanged,'sleMVQoS4InLIF':sleMVQoS4InLIF,'sleMVQoS4InLIFMark':sleMVQoS4InLIFMark,'sleMVQoS4InLIFMarkTable':sleMVQoS4InLIFMarkTable,'sleMVQoS4InLIFMarkEntry':sleMVQoS4InLIFMarkEntry,_P:sleMVQoS4InLIFMarkPortIndex,_S:sleMVQoS4InLIFMarkCoS,_T:sleMVQoS4InLIFMarkDSCP,'sleMVQoS4InLIFMarkControl':sleMVQoS4InLIFMarkControl,_L:sleMVQoS4InLIFMarkControlRequest,_h:sleMVQoS4InLIFMarkControlStatus,_i:sleMVQoS4InLIFMarkControlTimer,_M:sleMVQoS4InLIFMarkControlTimeStamp,_N:sleMVQoS4InLIFMarkControlReqResult,_j:sleMVQoS4InLIFMarkControlPortIndex,_k:sleMVQoS4InLIFMarkControlCoS,_l:sleMVQoS4InLIFMarkControlDSCP,'sleMVQoS4InLIFMarkNotification':sleMVQoS4InLIFMarkNotification,_n:sleInLIFMarkUpChanged,_o:sleInLIFMarkDscpChanged,'sleMVQoS4Router':sleMVQoS4Router,'sleMVQoS4RouterMark':sleMVQoS4RouterMark,'sleMVQoS4RouterMarkTable':sleMVQoS4RouterMarkTable,'sleMVQoS4RouterMarkEntry':sleMVQoS4RouterMarkEntry,_Q:sleMVQoS4RouterMarkNextHop,_I:sleMVQoS4RouterMarkQueue,_J:sleMVQoS4RouterMarkDp,_K:sleMVQoS4RouterMarkCoS,'sleMVQoS4RouterMarkControl':sleMVQoS4RouterMarkControl,_E:sleMVQoS4RouterMarkControlRequest,_c:sleMVQoS4RouterMarkControlStatus,_d:sleMVQoS4RouterMarkControlTimer,_F:sleMVQoS4RouterMarkControlTimeStamp,_G:sleMVQoS4RouterMarkControlReqResult,_X:sleMVQoS4RouterMarkControlNextHop,_e:sleMVQoS4RouterMarkControlQueue,_f:sleMVQoS4RouterMarkControlDp,_g:sleMVQoS4RouterMarkControlCoS,'sleMVQoS4RouterMarkNotification':sleMVQoS4RouterMarkNotification,_q:sleRouterMarkEntryCreated,_r:sleRouterMarkEntryChanged,_p:sleRouterMarkEntryDestroyed,'sleMVQoS6':sleMVQoS6,'sleMVQoSGroup':sleMVQoSGroup,'sleMVQoSControlGroup':sleMVQoSControlGroup,'sleMVQoSNotificationGroup':sleMVQoSNotificationGroup})