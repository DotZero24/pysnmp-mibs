_X='slePpppoeIARemoteIdChanged'
_W='slePpppoeIACircuitIdChanged'
_V='slePpppoeIAAccessnodeIdChanged'
_U='slePpppoeIAEnableStatuschanged'
_T='slePpppoeIAControlReqResult'
_S='slePpppoeIAControlTimer'
_R='slePpppoeIAControlStatus'
_Q='slePpppoeIARemoteId'
_P='slePpppoeIACircuitId'
_O='slePpppoeIAAccessNode'
_N='slePpppoeIAEnableStatus'
_M='disable'
_L='enable'
_K='slePpppoeIAControlRemoteId'
_J='slePpppoeIAControlCircuitId'
_I='slePpppoeIAControlAccessNode'
_H='slePpppoeIAControlEnableStatus'
_G='Integer32'
_F='slePpppoeIAControlTimeStamp'
_E='slePpppoeIAControlRequest'
_D='read-write'
_C='read-only'
_B='current'
_A='SLE-PPPOE-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
sleMgmt,=mibBuilder.importSymbols('DASAN-SMI','sleMgmt')
SleControlRequestResultType,SleControlStatusType=mibBuilder.importSymbols('SLE-TC-MIB','SleControlRequestResultType','SleControlStatusType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
slePppoe=ModuleIdentity((1,3,6,1,4,1,6296,101,24))
_SlePppoeBase_ObjectIdentity=ObjectIdentity
slePppoeBase=_SlePppoeBase_ObjectIdentity((1,3,6,1,4,1,6296,101,24,1))
_SlePppoeIntermediateAgent_ObjectIdentity=ObjectIdentity
slePppoeIntermediateAgent=_SlePppoeIntermediateAgent_ObjectIdentity((1,3,6,1,4,1,6296,101,24,2))
_SlePpppoeIABaseInfo_ObjectIdentity=ObjectIdentity
slePpppoeIABaseInfo=_SlePpppoeIABaseInfo_ObjectIdentity((1,3,6,1,4,1,6296,101,24,2,1))
class _SlePpppoeIAEnableStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_SlePpppoeIAEnableStatus_Type.__name__=_G
_SlePpppoeIAEnableStatus_Object=MibScalar
slePpppoeIAEnableStatus=_SlePpppoeIAEnableStatus_Object((1,3,6,1,4,1,6296,101,24,2,1,1),_SlePpppoeIAEnableStatus_Type())
slePpppoeIAEnableStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:slePpppoeIAEnableStatus.setStatus(_B)
_SlePpppoeIAAccessNode_Type=OctetString
_SlePpppoeIAAccessNode_Object=MibScalar
slePpppoeIAAccessNode=_SlePpppoeIAAccessNode_Object((1,3,6,1,4,1,6296,101,24,2,1,2),_SlePpppoeIAAccessNode_Type())
slePpppoeIAAccessNode.setMaxAccess(_C)
if mibBuilder.loadTexts:slePpppoeIAAccessNode.setStatus(_B)
_SlePpppoeIACircuitId_Type=OctetString
_SlePpppoeIACircuitId_Object=MibScalar
slePpppoeIACircuitId=_SlePpppoeIACircuitId_Object((1,3,6,1,4,1,6296,101,24,2,1,3),_SlePpppoeIACircuitId_Type())
slePpppoeIACircuitId.setMaxAccess(_C)
if mibBuilder.loadTexts:slePpppoeIACircuitId.setStatus(_B)
_SlePpppoeIARemoteId_Type=OctetString
_SlePpppoeIARemoteId_Object=MibScalar
slePpppoeIARemoteId=_SlePpppoeIARemoteId_Object((1,3,6,1,4,1,6296,101,24,2,1,4),_SlePpppoeIARemoteId_Type())
slePpppoeIARemoteId.setMaxAccess(_C)
if mibBuilder.loadTexts:slePpppoeIARemoteId.setStatus(_B)
_SlePpppoeIAControl_ObjectIdentity=ObjectIdentity
slePpppoeIAControl=_SlePpppoeIAControl_ObjectIdentity((1,3,6,1,4,1,6296,101,24,2,2))
class _SlePpppoeIAControlRequest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('setIntermediateAgentEnableStatus',1),('setFormatTypeAccessnodeId',2),('setFormatTypeCircuitId',3),('setFormatTypeRemoteId',4)))
_SlePpppoeIAControlRequest_Type.__name__=_G
_SlePpppoeIAControlRequest_Object=MibScalar
slePpppoeIAControlRequest=_SlePpppoeIAControlRequest_Object((1,3,6,1,4,1,6296,101,24,2,2,1),_SlePpppoeIAControlRequest_Type())
slePpppoeIAControlRequest.setMaxAccess(_D)
if mibBuilder.loadTexts:slePpppoeIAControlRequest.setStatus(_B)
_SlePpppoeIAControlStatus_Type=SleControlStatusType
_SlePpppoeIAControlStatus_Object=MibScalar
slePpppoeIAControlStatus=_SlePpppoeIAControlStatus_Object((1,3,6,1,4,1,6296,101,24,2,2,2),_SlePpppoeIAControlStatus_Type())
slePpppoeIAControlStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:slePpppoeIAControlStatus.setStatus(_B)
_SlePpppoeIAControlTimer_Type=Gauge32
_SlePpppoeIAControlTimer_Object=MibScalar
slePpppoeIAControlTimer=_SlePpppoeIAControlTimer_Object((1,3,6,1,4,1,6296,101,24,2,2,3),_SlePpppoeIAControlTimer_Type())
slePpppoeIAControlTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:slePpppoeIAControlTimer.setStatus(_B)
_SlePpppoeIAControlTimeStamp_Type=TimeTicks
_SlePpppoeIAControlTimeStamp_Object=MibScalar
slePpppoeIAControlTimeStamp=_SlePpppoeIAControlTimeStamp_Object((1,3,6,1,4,1,6296,101,24,2,2,4),_SlePpppoeIAControlTimeStamp_Type())
slePpppoeIAControlTimeStamp.setMaxAccess(_D)
if mibBuilder.loadTexts:slePpppoeIAControlTimeStamp.setStatus(_B)
_SlePpppoeIAControlReqResult_Type=SleControlRequestResultType
_SlePpppoeIAControlReqResult_Object=MibScalar
slePpppoeIAControlReqResult=_SlePpppoeIAControlReqResult_Object((1,3,6,1,4,1,6296,101,24,2,2,5),_SlePpppoeIAControlReqResult_Type())
slePpppoeIAControlReqResult.setMaxAccess(_D)
if mibBuilder.loadTexts:slePpppoeIAControlReqResult.setStatus(_B)
class _SlePpppoeIAControlEnableStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_SlePpppoeIAControlEnableStatus_Type.__name__=_G
_SlePpppoeIAControlEnableStatus_Object=MibScalar
slePpppoeIAControlEnableStatus=_SlePpppoeIAControlEnableStatus_Object((1,3,6,1,4,1,6296,101,24,2,2,6),_SlePpppoeIAControlEnableStatus_Type())
slePpppoeIAControlEnableStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:slePpppoeIAControlEnableStatus.setStatus(_B)
_SlePpppoeIAControlAccessNode_Type=OctetString
_SlePpppoeIAControlAccessNode_Object=MibScalar
slePpppoeIAControlAccessNode=_SlePpppoeIAControlAccessNode_Object((1,3,6,1,4,1,6296,101,24,2,2,7),_SlePpppoeIAControlAccessNode_Type())
slePpppoeIAControlAccessNode.setMaxAccess(_C)
if mibBuilder.loadTexts:slePpppoeIAControlAccessNode.setStatus(_B)
_SlePpppoeIAControlCircuitId_Type=OctetString
_SlePpppoeIAControlCircuitId_Object=MibScalar
slePpppoeIAControlCircuitId=_SlePpppoeIAControlCircuitId_Object((1,3,6,1,4,1,6296,101,24,2,2,8),_SlePpppoeIAControlCircuitId_Type())
slePpppoeIAControlCircuitId.setMaxAccess(_C)
if mibBuilder.loadTexts:slePpppoeIAControlCircuitId.setStatus(_B)
_SlePpppoeIAControlRemoteId_Type=OctetString
_SlePpppoeIAControlRemoteId_Object=MibScalar
slePpppoeIAControlRemoteId=_SlePpppoeIAControlRemoteId_Object((1,3,6,1,4,1,6296,101,24,2,2,9),_SlePpppoeIAControlRemoteId_Type())
slePpppoeIAControlRemoteId.setMaxAccess(_C)
if mibBuilder.loadTexts:slePpppoeIAControlRemoteId.setStatus(_B)
_SlePpppoeIANotification_ObjectIdentity=ObjectIdentity
slePpppoeIANotification=_SlePpppoeIANotification_ObjectIdentity((1,3,6,1,4,1,6296,101,24,2,3))
slePppoeGroup=ObjectGroup((1,3,6,1,4,1,6296,101,24,3))
slePppoeGroup.setObjects(*((_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_E),(_A,_R),(_A,_S),(_A,_F),(_A,_T),(_A,_H),(_A,_I),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:slePppoeGroup.setStatus(_B)
slePpppoeIAEnableStatuschanged=NotificationType((1,3,6,1,4,1,6296,101,24,2,3,1))
slePpppoeIAEnableStatuschanged.setObjects(*((_A,_E),(_A,_F),(_A,_H)))
if mibBuilder.loadTexts:slePpppoeIAEnableStatuschanged.setStatus(_B)
slePpppoeIAAccessnodeIdChanged=NotificationType((1,3,6,1,4,1,6296,101,24,2,3,2))
slePpppoeIAAccessnodeIdChanged.setObjects(*((_A,_E),(_A,_F),(_A,_I)))
if mibBuilder.loadTexts:slePpppoeIAAccessnodeIdChanged.setStatus(_B)
slePpppoeIACircuitIdChanged=NotificationType((1,3,6,1,4,1,6296,101,24,2,3,3))
slePpppoeIACircuitIdChanged.setObjects(*((_A,_E),(_A,_F),(_A,_J)))
if mibBuilder.loadTexts:slePpppoeIACircuitIdChanged.setStatus(_B)
slePpppoeIARemoteIdChanged=NotificationType((1,3,6,1,4,1,6296,101,24,2,3,4))
slePpppoeIARemoteIdChanged.setObjects(*((_A,_E),(_A,_F),(_A,_K)))
if mibBuilder.loadTexts:slePpppoeIARemoteIdChanged.setStatus(_B)
slePppoeNotificationGroup=NotificationGroup((1,3,6,1,4,1,6296,101,24,4))
slePppoeNotificationGroup.setObjects(*((_A,_U),(_A,_V),(_A,_W),(_A,_X)))
if mibBuilder.loadTexts:slePppoeNotificationGroup.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'slePppoe':slePppoe,'slePppoeBase':slePppoeBase,'slePppoeIntermediateAgent':slePppoeIntermediateAgent,'slePpppoeIABaseInfo':slePpppoeIABaseInfo,_N:slePpppoeIAEnableStatus,_O:slePpppoeIAAccessNode,_P:slePpppoeIACircuitId,_Q:slePpppoeIARemoteId,'slePpppoeIAControl':slePpppoeIAControl,_E:slePpppoeIAControlRequest,_R:slePpppoeIAControlStatus,_S:slePpppoeIAControlTimer,_F:slePpppoeIAControlTimeStamp,_T:slePpppoeIAControlReqResult,_H:slePpppoeIAControlEnableStatus,_I:slePpppoeIAControlAccessNode,_J:slePpppoeIAControlCircuitId,_K:slePpppoeIAControlRemoteId,'slePpppoeIANotification':slePpppoeIANotification,_U:slePpppoeIAEnableStatuschanged,_V:slePpppoeIAAccessnodeIdChanged,_W:slePpppoeIACircuitIdChanged,_X:slePpppoeIARemoteIdChanged,'slePppoeGroup':slePppoeGroup,'slePppoeNotificationGroup':slePppoeNotificationGroup})