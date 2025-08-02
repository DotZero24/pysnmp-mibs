_AN='sleSFlowCpDestroyed'
_AM='sleSFlowCpChanged'
_AL='sleSFlowCpCreated'
_AK='sleSFlowFsDestroyed'
_AJ='sleSFlowFsChanged'
_AI='sleSFlowFsCreated'
_AH='sleSFlowRcvrDestroyed'
_AG='sleSFlowRcvrChanged'
_AF='sleSFlowRcvrCreated'
_AE='sleSFlowAgentAddressChanged'
_AD='sleSFlowEnableChanged'
_AC='sleSFlowCpControlInterval'
_AB='sleSFlowCpControlReceiver'
_AA='sleSFlowCpControlTimer'
_A9='sleSFlowCpControlStatus'
_A8='sleSFlowFsControlMaxHeaderSize'
_A7='sleSFlowFsControlPacketSamplingRate'
_A6='sleSFlowFsControlReceiver'
_A5='sleSFlowFsControlTimer'
_A4='sleSFlowFsControlStatus'
_A3='sleSFlowRcvrControlPort'
_A2='sleSFlowRcvrControlAddress'
_A1='sleSFlowRcvrControlMaxDatagramSize'
_A0='sleSFlowRcvrControlTimeout'
_z='sleSFlowRcvrControlOwner'
_y='sleSFlowRcvrControlTimer'
_x='sleSFlowRcvrControlStatus'
_w='sleSFlowControlAgentAddress'
_v='sleSFlowControlEnable'
_u='sleSFlowControlTimer'
_t='sleSFlowControlStatus'
_s='sleSFlowMaxInstance'
_r='sleSFlowVersion'
_q='enable'
_p='disable'
_o='sleSFlowCpControlInstance'
_n='sleSFlowCpControlDataSource'
_m='sleSFlowFsControlInstance'
_l='sleSFlowFsControlDataSource'
_k='sleSFlowRcvrControlIndex'
_j='sleSFlowAgentAddress'
_i='sleSFlowEnable'
_h='sleSFlowCpInstance'
_g='sleSFlowCpDataSource'
_f='sleSFlowFsInstance'
_e='sleSFlowFsDataSource'
_d='sleSFlowRcvrIndex'
_c='OctetString'
_b='sleSFlowControlReqResult'
_a='sleSFlowControlTimeStamp'
_Z='sleSFlowControlRequest'
_Y='sleSFlowCpInterval'
_X='sleSFlowCpReceiver'
_W='sleSFlowFsMaxHeaderSize'
_V='sleSFlowFsPacketSamplingRate'
_U='sleSFlowFsReceiver'
_T='sleSFlowRcvrDatagramVersion'
_S='sleSFlowRcvrPort'
_R='sleSFlowRcvrAddress'
_Q='sleSFlowRcvrMaxDatagramSize'
_P='sleSFlowRcvrTimeout'
_O='sleSFlowRcvrOwner'
_N='sleSFlowCpControlReqResult'
_M='sleSFlowCpControlTimeStamp'
_L='sleSFlowCpControlRequest'
_K='sleSFlowFsControlReqResult'
_J='sleSFlowFsControlTimeStamp'
_I='sleSFlowFsControlRequest'
_H='sleSFlowRcvrControlReqResult'
_G='sleSFlowRcvrControlTimeStamp'
_F='sleSFlowRcvrControlRequest'
_E='read-only'
_D='Integer32'
_C='read-write'
_B='current'
_A='SLE-SFLOW-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_c,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
sleMgmt,=mibBuilder.importSymbols('DASAN-SMI','sleMgmt')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
SleControlRequestResultType,SleControlStatusType=mibBuilder.importSymbols('SLE-TC-MIB','SleControlRequestResultType','SleControlStatusType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
sleSFlow=ModuleIdentity((1,3,6,1,4,1,6296,101,21))
_SleSFlowBase_ObjectIdentity=ObjectIdentity
sleSFlowBase=_SleSFlowBase_ObjectIdentity((1,3,6,1,4,1,6296,101,21,1))
_SleSFlowInfo_ObjectIdentity=ObjectIdentity
sleSFlowInfo=_SleSFlowInfo_ObjectIdentity((1,3,6,1,4,1,6296,101,21,1,1))
class _SleSFlowEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_p,0),(_q,1)))
_SleSFlowEnable_Type.__name__=_D
_SleSFlowEnable_Object=MibScalar
sleSFlowEnable=_SleSFlowEnable_Object((1,3,6,1,4,1,6296,101,21,1,1,1),_SleSFlowEnable_Type())
sleSFlowEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:sleSFlowEnable.setStatus(_B)
_SleSFlowVersion_Type=OctetString
_SleSFlowVersion_Object=MibScalar
sleSFlowVersion=_SleSFlowVersion_Object((1,3,6,1,4,1,6296,101,21,1,1,2),_SleSFlowVersion_Type())
sleSFlowVersion.setMaxAccess(_E)
if mibBuilder.loadTexts:sleSFlowVersion.setStatus(_B)
_SleSFlowAgentAddress_Type=IpAddress
_SleSFlowAgentAddress_Object=MibScalar
sleSFlowAgentAddress=_SleSFlowAgentAddress_Object((1,3,6,1,4,1,6296,101,21,1,1,3),_SleSFlowAgentAddress_Type())
sleSFlowAgentAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:sleSFlowAgentAddress.setStatus(_B)
class _SleSFlowMaxInstance_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SleSFlowMaxInstance_Type.__name__=_D
_SleSFlowMaxInstance_Object=MibScalar
sleSFlowMaxInstance=_SleSFlowMaxInstance_Object((1,3,6,1,4,1,6296,101,21,1,1,4),_SleSFlowMaxInstance_Type())
sleSFlowMaxInstance.setMaxAccess(_E)
if mibBuilder.loadTexts:sleSFlowMaxInstance.setStatus(_B)
_SleSFlowControl_ObjectIdentity=ObjectIdentity
sleSFlowControl=_SleSFlowControl_ObjectIdentity((1,3,6,1,4,1,6296,101,21,1,2))
class _SleSFlowControlRequest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('setSFlowEnable',1),('setSFlowAgentAddress',2)))
_SleSFlowControlRequest_Type.__name__=_D
_SleSFlowControlRequest_Object=MibScalar
sleSFlowControlRequest=_SleSFlowControlRequest_Object((1,3,6,1,4,1,6296,101,21,1,2,1),_SleSFlowControlRequest_Type())
sleSFlowControlRequest.setMaxAccess(_C)
if mibBuilder.loadTexts:sleSFlowControlRequest.setStatus(_B)
_SleSFlowControlStatus_Type=SleControlStatusType
_SleSFlowControlStatus_Object=MibScalar
sleSFlowControlStatus=_SleSFlowControlStatus_Object((1,3,6,1,4,1,6296,101,21,1,2,2),_SleSFlowControlStatus_Type())
sleSFlowControlStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:sleSFlowControlStatus.setStatus(_B)
_SleSFlowControlTimer_Type=Gauge32
_SleSFlowControlTimer_Object=MibScalar
sleSFlowControlTimer=_SleSFlowControlTimer_Object((1,3,6,1,4,1,6296,101,21,1,2,3),_SleSFlowControlTimer_Type())
sleSFlowControlTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:sleSFlowControlTimer.setStatus(_B)
_SleSFlowControlTimeStamp_Type=TimeTicks
_SleSFlowControlTimeStamp_Object=MibScalar
sleSFlowControlTimeStamp=_SleSFlowControlTimeStamp_Object((1,3,6,1,4,1,6296,101,21,1,2,4),_SleSFlowControlTimeStamp_Type())
sleSFlowControlTimeStamp.setMaxAccess(_C)
if mibBuilder.loadTexts:sleSFlowControlTimeStamp.setStatus(_B)
_SleSFlowControlReqResult_Type=SleControlRequestResultType
_SleSFlowControlReqResult_Object=MibScalar
sleSFlowControlReqResult=_SleSFlowControlReqResult_Object((1,3,6,1,4,1,6296,101,21,1,2,5),_SleSFlowControlReqResult_Type())
sleSFlowControlReqResult.setMaxAccess(_C)
if mibBuilder.loadTexts:sleSFlowControlReqResult.setStatus(_B)
class _SleSFlowControlEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_p,0),(_q,1)))
_SleSFlowControlEnable_Type.__name__=_D
_SleSFlowControlEnable_Object=MibScalar
sleSFlowControlEnable=_SleSFlowControlEnable_Object((1,3,6,1,4,1,6296,101,21,1,2,6),_SleSFlowControlEnable_Type())
sleSFlowControlEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:sleSFlowControlEnable.setStatus(_B)
_SleSFlowControlAgentAddress_Type=IpAddress
_SleSFlowControlAgentAddress_Object=MibScalar
sleSFlowControlAgentAddress=_SleSFlowControlAgentAddress_Object((1,3,6,1,4,1,6296,101,21,1,2,7),_SleSFlowControlAgentAddress_Type())
sleSFlowControlAgentAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:sleSFlowControlAgentAddress.setStatus(_B)
_SleSFlowNotification_ObjectIdentity=ObjectIdentity
sleSFlowNotification=_SleSFlowNotification_ObjectIdentity((1,3,6,1,4,1,6296,101,21,1,3))
_SleSFlowRcvr_ObjectIdentity=ObjectIdentity
sleSFlowRcvr=_SleSFlowRcvr_ObjectIdentity((1,3,6,1,4,1,6296,101,21,2))
_SleSFlowRcvrTable_Object=MibTable
sleSFlowRcvrTable=_SleSFlowRcvrTable_Object((1,3,6,1,4,1,6296,101,21,2,1))
if mibBuilder.loadTexts:sleSFlowRcvrTable.setStatus(_B)
_SleSFlowRcvrEntry_Object=MibTableRow
sleSFlowRcvrEntry=_SleSFlowRcvrEntry_Object((1,3,6,1,4,1,6296,101,21,2,1,1))
sleSFlowRcvrEntry.setIndexNames((0,_A,_d))
if mibBuilder.loadTexts:sleSFlowRcvrEntry.setStatus(_B)
class _SleSFlowRcvrIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SleSFlowRcvrIndex_Type.__name__=_D
_SleSFlowRcvrIndex_Object=MibTableColumn
sleSFlowRcvrIndex=_SleSFlowRcvrIndex_Object((1,3,6,1,4,1,6296,101,21,2,1,1,1),_SleSFlowRcvrIndex_Type())
sleSFlowRcvrIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:sleSFlowRcvrIndex.setStatus(_B)
class _SleSFlowRcvrOwner_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_SleSFlowRcvrOwner_Type.__name__=_c
_SleSFlowRcvrOwner_Object=MibTableColumn
sleSFlowRcvrOwner=_SleSFlowRcvrOwner_Object((1,3,6,1,4,1,6296,101,21,2,1,1,2),_SleSFlowRcvrOwner_Type())
sleSFlowRcvrOwner.setMaxAccess(_E)
if mibBuilder.loadTexts:sleSFlowRcvrOwner.setStatus(_B)
class _SleSFlowRcvrTimeout_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_SleSFlowRcvrTimeout_Type.__name__=_D
_SleSFlowRcvrTimeout_Object=MibTableColumn
sleSFlowRcvrTimeout=_SleSFlowRcvrTimeout_Object((1,3,6,1,4,1,6296,101,21,2,1,1,3),_SleSFlowRcvrTimeout_Type())
sleSFlowRcvrTimeout.setMaxAccess(_E)
if mibBuilder.loadTexts:sleSFlowRcvrTimeout.setStatus(_B)
class _SleSFlowRcvrMaxDatagramSize_Type(Integer32):defaultValue=1400;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(256,1400))
_SleSFlowRcvrMaxDatagramSize_Type.__name__=_D
_SleSFlowRcvrMaxDatagramSize_Object=MibTableColumn
sleSFlowRcvrMaxDatagramSize=_SleSFlowRcvrMaxDatagramSize_Object((1,3,6,1,4,1,6296,101,21,2,1,1,4),_SleSFlowRcvrMaxDatagramSize_Type())
sleSFlowRcvrMaxDatagramSize.setMaxAccess(_E)
if mibBuilder.loadTexts:sleSFlowRcvrMaxDatagramSize.setStatus(_B)
_SleSFlowRcvrAddress_Type=IpAddress
_SleSFlowRcvrAddress_Object=MibTableColumn
sleSFlowRcvrAddress=_SleSFlowRcvrAddress_Object((1,3,6,1,4,1,6296,101,21,2,1,1,5),_SleSFlowRcvrAddress_Type())
sleSFlowRcvrAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:sleSFlowRcvrAddress.setStatus(_B)
class _SleSFlowRcvrPort_Type(Integer32):defaultValue=6343;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SleSFlowRcvrPort_Type.__name__=_D
_SleSFlowRcvrPort_Object=MibTableColumn
sleSFlowRcvrPort=_SleSFlowRcvrPort_Object((1,3,6,1,4,1,6296,101,21,2,1,1,6),_SleSFlowRcvrPort_Type())
sleSFlowRcvrPort.setMaxAccess(_E)
if mibBuilder.loadTexts:sleSFlowRcvrPort.setStatus(_B)
class _SleSFlowRcvrDatagramVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(5));namedValues=NamedValues(('version5',5))
_SleSFlowRcvrDatagramVersion_Type.__name__=_D
_SleSFlowRcvrDatagramVersion_Object=MibTableColumn
sleSFlowRcvrDatagramVersion=_SleSFlowRcvrDatagramVersion_Object((1,3,6,1,4,1,6296,101,21,2,1,1,7),_SleSFlowRcvrDatagramVersion_Type())
sleSFlowRcvrDatagramVersion.setMaxAccess(_E)
if mibBuilder.loadTexts:sleSFlowRcvrDatagramVersion.setStatus(_B)
_SleSFlowRcvrControl_ObjectIdentity=ObjectIdentity
sleSFlowRcvrControl=_SleSFlowRcvrControl_ObjectIdentity((1,3,6,1,4,1,6296,101,21,2,2))
class _SleSFlowRcvrControlRequest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('createSFlowRcvr',1),('setSFlowRcvr',2),('destroySFlowRcvr',3)))
_SleSFlowRcvrControlRequest_Type.__name__=_D
_SleSFlowRcvrControlRequest_Object=MibScalar
sleSFlowRcvrControlRequest=_SleSFlowRcvrControlRequest_Object((1,3,6,1,4,1,6296,101,21,2,2,1),_SleSFlowRcvrControlRequest_Type())
sleSFlowRcvrControlRequest.setMaxAccess(_C)
if mibBuilder.loadTexts:sleSFlowRcvrControlRequest.setStatus(_B)
_SleSFlowRcvrControlStatus_Type=SleControlStatusType
_SleSFlowRcvrControlStatus_Object=MibScalar
sleSFlowRcvrControlStatus=_SleSFlowRcvrControlStatus_Object((1,3,6,1,4,1,6296,101,21,2,2,2),_SleSFlowRcvrControlStatus_Type())
sleSFlowRcvrControlStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:sleSFlowRcvrControlStatus.setStatus(_B)
_SleSFlowRcvrControlTimer_Type=Gauge32
_SleSFlowRcvrControlTimer_Object=MibScalar
sleSFlowRcvrControlTimer=_SleSFlowRcvrControlTimer_Object((1,3,6,1,4,1,6296,101,21,2,2,3),_SleSFlowRcvrControlTimer_Type())
sleSFlowRcvrControlTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:sleSFlowRcvrControlTimer.setStatus(_B)
_SleSFlowRcvrControlTimeStamp_Type=TimeTicks
_SleSFlowRcvrControlTimeStamp_Object=MibScalar
sleSFlowRcvrControlTimeStamp=_SleSFlowRcvrControlTimeStamp_Object((1,3,6,1,4,1,6296,101,21,2,2,4),_SleSFlowRcvrControlTimeStamp_Type())
sleSFlowRcvrControlTimeStamp.setMaxAccess(_C)
if mibBuilder.loadTexts:sleSFlowRcvrControlTimeStamp.setStatus(_B)
_SleSFlowRcvrControlReqResult_Type=SleControlRequestResultType
_SleSFlowRcvrControlReqResult_Object=MibScalar
sleSFlowRcvrControlReqResult=_SleSFlowRcvrControlReqResult_Object((1,3,6,1,4,1,6296,101,21,2,2,5),_SleSFlowRcvrControlReqResult_Type())
sleSFlowRcvrControlReqResult.setMaxAccess(_C)
if mibBuilder.loadTexts:sleSFlowRcvrControlReqResult.setStatus(_B)
class _SleSFlowRcvrControlIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SleSFlowRcvrControlIndex_Type.__name__=_D
_SleSFlowRcvrControlIndex_Object=MibScalar
sleSFlowRcvrControlIndex=_SleSFlowRcvrControlIndex_Object((1,3,6,1,4,1,6296,101,21,2,2,6),_SleSFlowRcvrControlIndex_Type())
sleSFlowRcvrControlIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:sleSFlowRcvrControlIndex.setStatus(_B)
class _SleSFlowRcvrControlOwner_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_SleSFlowRcvrControlOwner_Type.__name__=_c
_SleSFlowRcvrControlOwner_Object=MibScalar
sleSFlowRcvrControlOwner=_SleSFlowRcvrControlOwner_Object((1,3,6,1,4,1,6296,101,21,2,2,7),_SleSFlowRcvrControlOwner_Type())
sleSFlowRcvrControlOwner.setMaxAccess(_C)
if mibBuilder.loadTexts:sleSFlowRcvrControlOwner.setStatus(_B)
class _SleSFlowRcvrControlTimeout_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_SleSFlowRcvrControlTimeout_Type.__name__=_D
_SleSFlowRcvrControlTimeout_Object=MibScalar
sleSFlowRcvrControlTimeout=_SleSFlowRcvrControlTimeout_Object((1,3,6,1,4,1,6296,101,21,2,2,8),_SleSFlowRcvrControlTimeout_Type())
sleSFlowRcvrControlTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:sleSFlowRcvrControlTimeout.setStatus(_B)
class _SleSFlowRcvrControlMaxDatagramSize_Type(Integer32):defaultValue=1400;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(256,1400))
_SleSFlowRcvrControlMaxDatagramSize_Type.__name__=_D
_SleSFlowRcvrControlMaxDatagramSize_Object=MibScalar
sleSFlowRcvrControlMaxDatagramSize=_SleSFlowRcvrControlMaxDatagramSize_Object((1,3,6,1,4,1,6296,101,21,2,2,9),_SleSFlowRcvrControlMaxDatagramSize_Type())
sleSFlowRcvrControlMaxDatagramSize.setMaxAccess(_C)
if mibBuilder.loadTexts:sleSFlowRcvrControlMaxDatagramSize.setStatus(_B)
_SleSFlowRcvrControlAddress_Type=IpAddress
_SleSFlowRcvrControlAddress_Object=MibScalar
sleSFlowRcvrControlAddress=_SleSFlowRcvrControlAddress_Object((1,3,6,1,4,1,6296,101,21,2,2,10),_SleSFlowRcvrControlAddress_Type())
sleSFlowRcvrControlAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:sleSFlowRcvrControlAddress.setStatus(_B)
class _SleSFlowRcvrControlPort_Type(Integer32):defaultValue=6343;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SleSFlowRcvrControlPort_Type.__name__=_D
_SleSFlowRcvrControlPort_Object=MibScalar
sleSFlowRcvrControlPort=_SleSFlowRcvrControlPort_Object((1,3,6,1,4,1,6296,101,21,2,2,11),_SleSFlowRcvrControlPort_Type())
sleSFlowRcvrControlPort.setMaxAccess(_E)
if mibBuilder.loadTexts:sleSFlowRcvrControlPort.setStatus(_B)
_SleSFlowRcvrNotification_ObjectIdentity=ObjectIdentity
sleSFlowRcvrNotification=_SleSFlowRcvrNotification_ObjectIdentity((1,3,6,1,4,1,6296,101,21,2,3))
_SleSFlowFs_ObjectIdentity=ObjectIdentity
sleSFlowFs=_SleSFlowFs_ObjectIdentity((1,3,6,1,4,1,6296,101,21,3))
_SleSFlowFsTable_Object=MibTable
sleSFlowFsTable=_SleSFlowFsTable_Object((1,3,6,1,4,1,6296,101,21,3,1))
if mibBuilder.loadTexts:sleSFlowFsTable.setStatus(_B)
_SleSFlowFsEntry_Object=MibTableRow
sleSFlowFsEntry=_SleSFlowFsEntry_Object((1,3,6,1,4,1,6296,101,21,3,1,1))
sleSFlowFsEntry.setIndexNames((0,_A,_e),(0,_A,_f))
if mibBuilder.loadTexts:sleSFlowFsEntry.setStatus(_B)
_SleSFlowFsDataSource_Type=InterfaceIndex
_SleSFlowFsDataSource_Object=MibTableColumn
sleSFlowFsDataSource=_SleSFlowFsDataSource_Object((1,3,6,1,4,1,6296,101,21,3,1,1,1),_SleSFlowFsDataSource_Type())
sleSFlowFsDataSource.setMaxAccess(_E)
if mibBuilder.loadTexts:sleSFlowFsDataSource.setStatus(_B)
class _SleSFlowFsInstance_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SleSFlowFsInstance_Type.__name__=_D
_SleSFlowFsInstance_Object=MibTableColumn
sleSFlowFsInstance=_SleSFlowFsInstance_Object((1,3,6,1,4,1,6296,101,21,3,1,1,2),_SleSFlowFsInstance_Type())
sleSFlowFsInstance.setMaxAccess(_E)
if mibBuilder.loadTexts:sleSFlowFsInstance.setStatus(_B)
class _SleSFlowFsReceiver_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SleSFlowFsReceiver_Type.__name__=_D
_SleSFlowFsReceiver_Object=MibTableColumn
sleSFlowFsReceiver=_SleSFlowFsReceiver_Object((1,3,6,1,4,1,6296,101,21,3,1,1,3),_SleSFlowFsReceiver_Type())
sleSFlowFsReceiver.setMaxAccess(_E)
if mibBuilder.loadTexts:sleSFlowFsReceiver.setStatus(_B)
class _SleSFlowFsPacketSamplingRate_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2000))
_SleSFlowFsPacketSamplingRate_Type.__name__=_D
_SleSFlowFsPacketSamplingRate_Object=MibTableColumn
sleSFlowFsPacketSamplingRate=_SleSFlowFsPacketSamplingRate_Object((1,3,6,1,4,1,6296,101,21,3,1,1,4),_SleSFlowFsPacketSamplingRate_Type())
sleSFlowFsPacketSamplingRate.setMaxAccess(_E)
if mibBuilder.loadTexts:sleSFlowFsPacketSamplingRate.setStatus(_B)
class _SleSFlowFsMaxHeaderSize_Type(Integer32):defaultValue=128;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(16,256))
_SleSFlowFsMaxHeaderSize_Type.__name__=_D
_SleSFlowFsMaxHeaderSize_Object=MibTableColumn
sleSFlowFsMaxHeaderSize=_SleSFlowFsMaxHeaderSize_Object((1,3,6,1,4,1,6296,101,21,3,1,1,5),_SleSFlowFsMaxHeaderSize_Type())
sleSFlowFsMaxHeaderSize.setMaxAccess(_E)
if mibBuilder.loadTexts:sleSFlowFsMaxHeaderSize.setStatus(_B)
_SleSFlowFsControl_ObjectIdentity=ObjectIdentity
sleSFlowFsControl=_SleSFlowFsControl_ObjectIdentity((1,3,6,1,4,1,6296,101,21,3,2))
class _SleSFlowFsControlRequest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('createSFlowFs',1),('setSFlowFs',2),('destroySFlowFs',3)))
_SleSFlowFsControlRequest_Type.__name__=_D
_SleSFlowFsControlRequest_Object=MibScalar
sleSFlowFsControlRequest=_SleSFlowFsControlRequest_Object((1,3,6,1,4,1,6296,101,21,3,2,1),_SleSFlowFsControlRequest_Type())
sleSFlowFsControlRequest.setMaxAccess(_C)
if mibBuilder.loadTexts:sleSFlowFsControlRequest.setStatus(_B)
_SleSFlowFsControlStatus_Type=SleControlStatusType
_SleSFlowFsControlStatus_Object=MibScalar
sleSFlowFsControlStatus=_SleSFlowFsControlStatus_Object((1,3,6,1,4,1,6296,101,21,3,2,2),_SleSFlowFsControlStatus_Type())
sleSFlowFsControlStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:sleSFlowFsControlStatus.setStatus(_B)
_SleSFlowFsControlTimer_Type=Gauge32
_SleSFlowFsControlTimer_Object=MibScalar
sleSFlowFsControlTimer=_SleSFlowFsControlTimer_Object((1,3,6,1,4,1,6296,101,21,3,2,3),_SleSFlowFsControlTimer_Type())
sleSFlowFsControlTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:sleSFlowFsControlTimer.setStatus(_B)
_SleSFlowFsControlTimeStamp_Type=TimeTicks
_SleSFlowFsControlTimeStamp_Object=MibScalar
sleSFlowFsControlTimeStamp=_SleSFlowFsControlTimeStamp_Object((1,3,6,1,4,1,6296,101,21,3,2,4),_SleSFlowFsControlTimeStamp_Type())
sleSFlowFsControlTimeStamp.setMaxAccess(_C)
if mibBuilder.loadTexts:sleSFlowFsControlTimeStamp.setStatus(_B)
_SleSFlowFsControlReqResult_Type=SleControlRequestResultType
_SleSFlowFsControlReqResult_Object=MibScalar
sleSFlowFsControlReqResult=_SleSFlowFsControlReqResult_Object((1,3,6,1,4,1,6296,101,21,3,2,5),_SleSFlowFsControlReqResult_Type())
sleSFlowFsControlReqResult.setMaxAccess(_C)
if mibBuilder.loadTexts:sleSFlowFsControlReqResult.setStatus(_B)
_SleSFlowFsControlDataSource_Type=InterfaceIndex
_SleSFlowFsControlDataSource_Object=MibScalar
sleSFlowFsControlDataSource=_SleSFlowFsControlDataSource_Object((1,3,6,1,4,1,6296,101,21,3,2,6),_SleSFlowFsControlDataSource_Type())
sleSFlowFsControlDataSource.setMaxAccess(_C)
if mibBuilder.loadTexts:sleSFlowFsControlDataSource.setStatus(_B)
class _SleSFlowFsControlInstance_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SleSFlowFsControlInstance_Type.__name__=_D
_SleSFlowFsControlInstance_Object=MibScalar
sleSFlowFsControlInstance=_SleSFlowFsControlInstance_Object((1,3,6,1,4,1,6296,101,21,3,2,7),_SleSFlowFsControlInstance_Type())
sleSFlowFsControlInstance.setMaxAccess(_C)
if mibBuilder.loadTexts:sleSFlowFsControlInstance.setStatus(_B)
class _SleSFlowFsControlReceiver_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SleSFlowFsControlReceiver_Type.__name__=_D
_SleSFlowFsControlReceiver_Object=MibScalar
sleSFlowFsControlReceiver=_SleSFlowFsControlReceiver_Object((1,3,6,1,4,1,6296,101,21,3,2,8),_SleSFlowFsControlReceiver_Type())
sleSFlowFsControlReceiver.setMaxAccess(_C)
if mibBuilder.loadTexts:sleSFlowFsControlReceiver.setStatus(_B)
class _SleSFlowFsControlPacketSamplingRate_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2000))
_SleSFlowFsControlPacketSamplingRate_Type.__name__=_D
_SleSFlowFsControlPacketSamplingRate_Object=MibScalar
sleSFlowFsControlPacketSamplingRate=_SleSFlowFsControlPacketSamplingRate_Object((1,3,6,1,4,1,6296,101,21,3,2,9),_SleSFlowFsControlPacketSamplingRate_Type())
sleSFlowFsControlPacketSamplingRate.setMaxAccess(_C)
if mibBuilder.loadTexts:sleSFlowFsControlPacketSamplingRate.setStatus(_B)
class _SleSFlowFsControlMaxHeaderSize_Type(Integer32):defaultValue=128;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(16,256))
_SleSFlowFsControlMaxHeaderSize_Type.__name__=_D
_SleSFlowFsControlMaxHeaderSize_Object=MibScalar
sleSFlowFsControlMaxHeaderSize=_SleSFlowFsControlMaxHeaderSize_Object((1,3,6,1,4,1,6296,101,21,3,2,10),_SleSFlowFsControlMaxHeaderSize_Type())
sleSFlowFsControlMaxHeaderSize.setMaxAccess(_C)
if mibBuilder.loadTexts:sleSFlowFsControlMaxHeaderSize.setStatus(_B)
_SleSFlowFsNotification_ObjectIdentity=ObjectIdentity
sleSFlowFsNotification=_SleSFlowFsNotification_ObjectIdentity((1,3,6,1,4,1,6296,101,21,3,3))
_SleSFlowCp_ObjectIdentity=ObjectIdentity
sleSFlowCp=_SleSFlowCp_ObjectIdentity((1,3,6,1,4,1,6296,101,21,4))
_SleSFlowCpTable_Object=MibTable
sleSFlowCpTable=_SleSFlowCpTable_Object((1,3,6,1,4,1,6296,101,21,4,1))
if mibBuilder.loadTexts:sleSFlowCpTable.setStatus(_B)
_SleSFlowCpEntry_Object=MibTableRow
sleSFlowCpEntry=_SleSFlowCpEntry_Object((1,3,6,1,4,1,6296,101,21,4,1,1))
sleSFlowCpEntry.setIndexNames((0,_A,_g),(0,_A,_h))
if mibBuilder.loadTexts:sleSFlowCpEntry.setStatus(_B)
_SleSFlowCpDataSource_Type=InterfaceIndex
_SleSFlowCpDataSource_Object=MibTableColumn
sleSFlowCpDataSource=_SleSFlowCpDataSource_Object((1,3,6,1,4,1,6296,101,21,4,1,1,1),_SleSFlowCpDataSource_Type())
sleSFlowCpDataSource.setMaxAccess(_E)
if mibBuilder.loadTexts:sleSFlowCpDataSource.setStatus(_B)
class _SleSFlowCpInstance_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SleSFlowCpInstance_Type.__name__=_D
_SleSFlowCpInstance_Object=MibTableColumn
sleSFlowCpInstance=_SleSFlowCpInstance_Object((1,3,6,1,4,1,6296,101,21,4,1,1,2),_SleSFlowCpInstance_Type())
sleSFlowCpInstance.setMaxAccess(_E)
if mibBuilder.loadTexts:sleSFlowCpInstance.setStatus(_B)
class _SleSFlowCpReceiver_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SleSFlowCpReceiver_Type.__name__=_D
_SleSFlowCpReceiver_Object=MibTableColumn
sleSFlowCpReceiver=_SleSFlowCpReceiver_Object((1,3,6,1,4,1,6296,101,21,4,1,1,3),_SleSFlowCpReceiver_Type())
sleSFlowCpReceiver.setMaxAccess(_E)
if mibBuilder.loadTexts:sleSFlowCpReceiver.setStatus(_B)
class _SleSFlowCpInterval_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_SleSFlowCpInterval_Type.__name__=_D
_SleSFlowCpInterval_Object=MibTableColumn
sleSFlowCpInterval=_SleSFlowCpInterval_Object((1,3,6,1,4,1,6296,101,21,4,1,1,4),_SleSFlowCpInterval_Type())
sleSFlowCpInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:sleSFlowCpInterval.setStatus(_B)
_SleSFlowCpControl_ObjectIdentity=ObjectIdentity
sleSFlowCpControl=_SleSFlowCpControl_ObjectIdentity((1,3,6,1,4,1,6296,101,21,4,2))
class _SleSFlowCpControlRequest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('createSFlowCp',1),('setSFlowCp',2),('destroySFlowCp',3)))
_SleSFlowCpControlRequest_Type.__name__=_D
_SleSFlowCpControlRequest_Object=MibScalar
sleSFlowCpControlRequest=_SleSFlowCpControlRequest_Object((1,3,6,1,4,1,6296,101,21,4,2,1),_SleSFlowCpControlRequest_Type())
sleSFlowCpControlRequest.setMaxAccess(_C)
if mibBuilder.loadTexts:sleSFlowCpControlRequest.setStatus(_B)
_SleSFlowCpControlStatus_Type=SleControlStatusType
_SleSFlowCpControlStatus_Object=MibScalar
sleSFlowCpControlStatus=_SleSFlowCpControlStatus_Object((1,3,6,1,4,1,6296,101,21,4,2,2),_SleSFlowCpControlStatus_Type())
sleSFlowCpControlStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:sleSFlowCpControlStatus.setStatus(_B)
_SleSFlowCpControlTimer_Type=Gauge32
_SleSFlowCpControlTimer_Object=MibScalar
sleSFlowCpControlTimer=_SleSFlowCpControlTimer_Object((1,3,6,1,4,1,6296,101,21,4,2,3),_SleSFlowCpControlTimer_Type())
sleSFlowCpControlTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:sleSFlowCpControlTimer.setStatus(_B)
_SleSFlowCpControlTimeStamp_Type=TimeTicks
_SleSFlowCpControlTimeStamp_Object=MibScalar
sleSFlowCpControlTimeStamp=_SleSFlowCpControlTimeStamp_Object((1,3,6,1,4,1,6296,101,21,4,2,4),_SleSFlowCpControlTimeStamp_Type())
sleSFlowCpControlTimeStamp.setMaxAccess(_C)
if mibBuilder.loadTexts:sleSFlowCpControlTimeStamp.setStatus(_B)
_SleSFlowCpControlReqResult_Type=SleControlRequestResultType
_SleSFlowCpControlReqResult_Object=MibScalar
sleSFlowCpControlReqResult=_SleSFlowCpControlReqResult_Object((1,3,6,1,4,1,6296,101,21,4,2,5),_SleSFlowCpControlReqResult_Type())
sleSFlowCpControlReqResult.setMaxAccess(_C)
if mibBuilder.loadTexts:sleSFlowCpControlReqResult.setStatus(_B)
_SleSFlowCpControlDataSource_Type=InterfaceIndex
_SleSFlowCpControlDataSource_Object=MibScalar
sleSFlowCpControlDataSource=_SleSFlowCpControlDataSource_Object((1,3,6,1,4,1,6296,101,21,4,2,6),_SleSFlowCpControlDataSource_Type())
sleSFlowCpControlDataSource.setMaxAccess(_C)
if mibBuilder.loadTexts:sleSFlowCpControlDataSource.setStatus(_B)
class _SleSFlowCpControlInstance_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SleSFlowCpControlInstance_Type.__name__=_D
_SleSFlowCpControlInstance_Object=MibScalar
sleSFlowCpControlInstance=_SleSFlowCpControlInstance_Object((1,3,6,1,4,1,6296,101,21,4,2,7),_SleSFlowCpControlInstance_Type())
sleSFlowCpControlInstance.setMaxAccess(_C)
if mibBuilder.loadTexts:sleSFlowCpControlInstance.setStatus(_B)
class _SleSFlowCpControlReceiver_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SleSFlowCpControlReceiver_Type.__name__=_D
_SleSFlowCpControlReceiver_Object=MibScalar
sleSFlowCpControlReceiver=_SleSFlowCpControlReceiver_Object((1,3,6,1,4,1,6296,101,21,4,2,8),_SleSFlowCpControlReceiver_Type())
sleSFlowCpControlReceiver.setMaxAccess(_C)
if mibBuilder.loadTexts:sleSFlowCpControlReceiver.setStatus(_B)
class _SleSFlowCpControlInterval_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_SleSFlowCpControlInterval_Type.__name__=_D
_SleSFlowCpControlInterval_Object=MibScalar
sleSFlowCpControlInterval=_SleSFlowCpControlInterval_Object((1,3,6,1,4,1,6296,101,21,4,2,9),_SleSFlowCpControlInterval_Type())
sleSFlowCpControlInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:sleSFlowCpControlInterval.setStatus(_B)
_SleSFlowCpNotification_ObjectIdentity=ObjectIdentity
sleSFlowCpNotification=_SleSFlowCpNotification_ObjectIdentity((1,3,6,1,4,1,6296,101,21,4,3))
sleSFlowGroup=ObjectGroup((1,3,6,1,4,1,6296,101,21,5))
sleSFlowGroup.setObjects(*((_A,_i),(_A,_r),(_A,_j),(_A,_s),(_A,_d),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_e),(_A,_f),(_A,_U),(_A,_V),(_A,_W),(_A,_g),(_A,_h),(_A,_X),(_A,_Y)))
if mibBuilder.loadTexts:sleSFlowGroup.setStatus(_B)
sleSFlowControlGroup=ObjectGroup((1,3,6,1,4,1,6296,101,21,6))
sleSFlowControlGroup.setObjects(*((_A,_Z),(_A,_t),(_A,_u),(_A,_a),(_A,_b),(_A,_v),(_A,_w),(_A,_F),(_A,_x),(_A,_y),(_A,_G),(_A,_H),(_A,_k),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_I),(_A,_A4),(_A,_A5),(_A,_J),(_A,_K),(_A,_l),(_A,_m),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_L),(_A,_A9),(_A,_AA),(_A,_M),(_A,_N),(_A,_n),(_A,_o),(_A,_AB),(_A,_AC)))
if mibBuilder.loadTexts:sleSFlowControlGroup.setStatus(_B)
sleSFlowEnableChanged=NotificationType((1,3,6,1,4,1,6296,101,21,1,3,1))
sleSFlowEnableChanged.setObjects(*((_A,_Z),(_A,_a),(_A,_b),(_A,_i)))
if mibBuilder.loadTexts:sleSFlowEnableChanged.setStatus(_B)
sleSFlowAgentAddressChanged=NotificationType((1,3,6,1,4,1,6296,101,21,1,3,2))
sleSFlowAgentAddressChanged.setObjects(*((_A,_Z),(_A,_a),(_A,_b),(_A,_j)))
if mibBuilder.loadTexts:sleSFlowAgentAddressChanged.setStatus(_B)
sleSFlowRcvrCreated=NotificationType((1,3,6,1,4,1,6296,101,21,2,3,1))
sleSFlowRcvrCreated.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T)))
if mibBuilder.loadTexts:sleSFlowRcvrCreated.setStatus(_B)
sleSFlowRcvrChanged=NotificationType((1,3,6,1,4,1,6296,101,21,2,3,2))
sleSFlowRcvrChanged.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T)))
if mibBuilder.loadTexts:sleSFlowRcvrChanged.setStatus(_B)
sleSFlowRcvrDestroyed=NotificationType((1,3,6,1,4,1,6296,101,21,2,3,3))
sleSFlowRcvrDestroyed.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_k)))
if mibBuilder.loadTexts:sleSFlowRcvrDestroyed.setStatus(_B)
sleSFlowFsCreated=NotificationType((1,3,6,1,4,1,6296,101,21,3,3,1))
sleSFlowFsCreated.setObjects(*((_A,_I),(_A,_J),(_A,_K),(_A,_U),(_A,_V),(_A,_W)))
if mibBuilder.loadTexts:sleSFlowFsCreated.setStatus(_B)
sleSFlowFsChanged=NotificationType((1,3,6,1,4,1,6296,101,21,3,3,2))
sleSFlowFsChanged.setObjects(*((_A,_I),(_A,_J),(_A,_K),(_A,_U),(_A,_V),(_A,_W)))
if mibBuilder.loadTexts:sleSFlowFsChanged.setStatus(_B)
sleSFlowFsDestroyed=NotificationType((1,3,6,1,4,1,6296,101,21,3,3,3))
sleSFlowFsDestroyed.setObjects(*((_A,_I),(_A,_J),(_A,_K),(_A,_l),(_A,_m)))
if mibBuilder.loadTexts:sleSFlowFsDestroyed.setStatus(_B)
sleSFlowCpCreated=NotificationType((1,3,6,1,4,1,6296,101,21,4,3,1))
sleSFlowCpCreated.setObjects(*((_A,_L),(_A,_M),(_A,_N),(_A,_X),(_A,_Y)))
if mibBuilder.loadTexts:sleSFlowCpCreated.setStatus(_B)
sleSFlowCpChanged=NotificationType((1,3,6,1,4,1,6296,101,21,4,3,2))
sleSFlowCpChanged.setObjects(*((_A,_L),(_A,_M),(_A,_N),(_A,_X),(_A,_Y)))
if mibBuilder.loadTexts:sleSFlowCpChanged.setStatus(_B)
sleSFlowCpDestroyed=NotificationType((1,3,6,1,4,1,6296,101,21,4,3,3))
sleSFlowCpDestroyed.setObjects(*((_A,_L),(_A,_M),(_A,_N),(_A,_n),(_A,_o)))
if mibBuilder.loadTexts:sleSFlowCpDestroyed.setStatus(_B)
sleSFlowNotificationGroup=NotificationGroup((1,3,6,1,4,1,6296,101,21,7))
sleSFlowNotificationGroup.setObjects(*((_A,_AD),(_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ),(_A,_AK),(_A,_AL),(_A,_AM),(_A,_AN)))
if mibBuilder.loadTexts:sleSFlowNotificationGroup.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'sleSFlow':sleSFlow,'sleSFlowBase':sleSFlowBase,'sleSFlowInfo':sleSFlowInfo,_i:sleSFlowEnable,_r:sleSFlowVersion,_j:sleSFlowAgentAddress,_s:sleSFlowMaxInstance,'sleSFlowControl':sleSFlowControl,_Z:sleSFlowControlRequest,_t:sleSFlowControlStatus,_u:sleSFlowControlTimer,_a:sleSFlowControlTimeStamp,_b:sleSFlowControlReqResult,_v:sleSFlowControlEnable,_w:sleSFlowControlAgentAddress,'sleSFlowNotification':sleSFlowNotification,_AD:sleSFlowEnableChanged,_AE:sleSFlowAgentAddressChanged,'sleSFlowRcvr':sleSFlowRcvr,'sleSFlowRcvrTable':sleSFlowRcvrTable,'sleSFlowRcvrEntry':sleSFlowRcvrEntry,_d:sleSFlowRcvrIndex,_O:sleSFlowRcvrOwner,_P:sleSFlowRcvrTimeout,_Q:sleSFlowRcvrMaxDatagramSize,_R:sleSFlowRcvrAddress,_S:sleSFlowRcvrPort,_T:sleSFlowRcvrDatagramVersion,'sleSFlowRcvrControl':sleSFlowRcvrControl,_F:sleSFlowRcvrControlRequest,_x:sleSFlowRcvrControlStatus,_y:sleSFlowRcvrControlTimer,_G:sleSFlowRcvrControlTimeStamp,_H:sleSFlowRcvrControlReqResult,_k:sleSFlowRcvrControlIndex,_z:sleSFlowRcvrControlOwner,_A0:sleSFlowRcvrControlTimeout,_A1:sleSFlowRcvrControlMaxDatagramSize,_A2:sleSFlowRcvrControlAddress,_A3:sleSFlowRcvrControlPort,'sleSFlowRcvrNotification':sleSFlowRcvrNotification,_AF:sleSFlowRcvrCreated,_AG:sleSFlowRcvrChanged,_AH:sleSFlowRcvrDestroyed,'sleSFlowFs':sleSFlowFs,'sleSFlowFsTable':sleSFlowFsTable,'sleSFlowFsEntry':sleSFlowFsEntry,_e:sleSFlowFsDataSource,_f:sleSFlowFsInstance,_U:sleSFlowFsReceiver,_V:sleSFlowFsPacketSamplingRate,_W:sleSFlowFsMaxHeaderSize,'sleSFlowFsControl':sleSFlowFsControl,_I:sleSFlowFsControlRequest,_A4:sleSFlowFsControlStatus,_A5:sleSFlowFsControlTimer,_J:sleSFlowFsControlTimeStamp,_K:sleSFlowFsControlReqResult,_l:sleSFlowFsControlDataSource,_m:sleSFlowFsControlInstance,_A6:sleSFlowFsControlReceiver,_A7:sleSFlowFsControlPacketSamplingRate,_A8:sleSFlowFsControlMaxHeaderSize,'sleSFlowFsNotification':sleSFlowFsNotification,_AI:sleSFlowFsCreated,_AJ:sleSFlowFsChanged,_AK:sleSFlowFsDestroyed,'sleSFlowCp':sleSFlowCp,'sleSFlowCpTable':sleSFlowCpTable,'sleSFlowCpEntry':sleSFlowCpEntry,_g:sleSFlowCpDataSource,_h:sleSFlowCpInstance,_X:sleSFlowCpReceiver,_Y:sleSFlowCpInterval,'sleSFlowCpControl':sleSFlowCpControl,_L:sleSFlowCpControlRequest,_A9:sleSFlowCpControlStatus,_AA:sleSFlowCpControlTimer,_M:sleSFlowCpControlTimeStamp,_N:sleSFlowCpControlReqResult,_n:sleSFlowCpControlDataSource,_o:sleSFlowCpControlInstance,_AB:sleSFlowCpControlReceiver,_AC:sleSFlowCpControlInterval,'sleSFlowCpNotification':sleSFlowCpNotification,_AL:sleSFlowCpCreated,_AM:sleSFlowCpChanged,_AN:sleSFlowCpDestroyed,'sleSFlowGroup':sleSFlowGroup,'sleSFlowControlGroup':sleSFlowControlGroup,'sleSFlowNotificationGroup':sleSFlowNotificationGroup})