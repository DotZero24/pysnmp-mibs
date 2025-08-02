_t='ciscoWanFrCllmStatsGroup'
_s='ciscoWanFrCllmGroup'
_r='ciscoWanFrLmiStatsGroup'
_q='ciscoWanFrLmiConfigGroup'
_p='cllmFailures'
_o='xmtBytesCLLM'
_n='xmtFramesCLLM'
_m='rcvBytesCLLM'
_l='rcvFramesCLLM'
_k='rcvCLLMStatusTimer'
_j='xmtCLLMStatusTimer'
_i='cllmEnable'
_h='nniSignalingTimeout'
_g='rcvNNISeqMismatch'
_f='rcvAsynchUpdate'
_e='rcvStatus'
_d='xmtStatusInquiry'
_c='uniSignalingTimeout'
_b='xmtAsynchUpdate'
_a='xmtStatus'
_Z='rcvUNISeqMismatch'
_Y='rcvInvalidRequest'
_X='rcvStatusInquiry'
_W='portLmiSigConfMethod'
_V='portFRF1Dot2Support'
_U='enhancedLmi'
_T='n393MonitoredEventCount'
_S='n392ErrorThreshold'
_R='n391FullStatusPollingCounter'
_Q='t392PollingVerificationTimer'
_P='t391LinkIntegrityTimer'
_O='asynchronousUpdates'
_N='signallingProtocolType'
_M='frames'
_L='seconds'
_K='cllmSigPortNum'
_J='lmiSigPortNum'
_I='cllmCnfPortNum'
_H='lmiCnfPortNum'
_G='enable'
_F='disable'
_E='read-write'
_D='Integer32'
_C='read-only'
_B='CISCO-WAN-FR-SIGNALING-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
frPortCnfSig,frPortCntSig=mibBuilder.importSymbols('BASIS-MIB','frPortCnfSig','frPortCntSig')
ciscoWan,=mibBuilder.importSymbols('CISCOWAN-SMI','ciscoWan')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoWanFrSignalingMIB=ModuleIdentity((1,3,6,1,4,1,351,150,46))
if mibBuilder.loadTexts:ciscoWanFrSignalingMIB.setRevisions(('2003-03-24 00:00','2002-09-04 00:00'))
_FrPortCnfSigLMIGrp_ObjectIdentity=ObjectIdentity
frPortCnfSigLMIGrp=_FrPortCnfSigLMIGrp_ObjectIdentity((1,3,6,1,4,1,351,110,5,1,1,1,2,1))
_FrPortCnfSigLMIGrpTable_Object=MibTable
frPortCnfSigLMIGrpTable=_FrPortCnfSigLMIGrpTable_Object((1,3,6,1,4,1,351,110,5,1,1,1,2,1,1))
if mibBuilder.loadTexts:frPortCnfSigLMIGrpTable.setStatus(_A)
_FrPortCnfSigLMIGrpEntry_Object=MibTableRow
frPortCnfSigLMIGrpEntry=_FrPortCnfSigLMIGrpEntry_Object((1,3,6,1,4,1,351,110,5,1,1,1,2,1,1,1))
frPortCnfSigLMIGrpEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:frPortCnfSigLMIGrpEntry.setStatus(_A)
class _LmiCnfPortNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_LmiCnfPortNum_Type.__name__=_D
_LmiCnfPortNum_Object=MibTableColumn
lmiCnfPortNum=_LmiCnfPortNum_Object((1,3,6,1,4,1,351,110,5,1,1,1,2,1,1,1,1),_LmiCnfPortNum_Type())
lmiCnfPortNum.setMaxAccess(_C)
if mibBuilder.loadTexts:lmiCnfPortNum.setStatus(_A)
class _SignallingProtocolType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('other',1),('noSignalling',2),('strataLMI',3),('annexAUNI',4),('annexDUNI',5),('annexANNI',6),('annexDNNI',7)))
_SignallingProtocolType_Type.__name__=_D
_SignallingProtocolType_Object=MibTableColumn
signallingProtocolType=_SignallingProtocolType_Object((1,3,6,1,4,1,351,110,5,1,1,1,2,1,1,1,2),_SignallingProtocolType_Type())
signallingProtocolType.setMaxAccess(_E)
if mibBuilder.loadTexts:signallingProtocolType.setStatus(_A)
class _AsynchronousUpdates_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_G,2),('fsenable',3),('updfsenable',4)))
_AsynchronousUpdates_Type.__name__=_D
_AsynchronousUpdates_Object=MibTableColumn
asynchronousUpdates=_AsynchronousUpdates_Object((1,3,6,1,4,1,351,110,5,1,1,1,2,1,1,1,3),_AsynchronousUpdates_Type())
asynchronousUpdates.setMaxAccess(_E)
if mibBuilder.loadTexts:asynchronousUpdates.setStatus(_A)
class _T391LinkIntegrityTimer_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,30))
_T391LinkIntegrityTimer_Type.__name__=_D
_T391LinkIntegrityTimer_Object=MibTableColumn
t391LinkIntegrityTimer=_T391LinkIntegrityTimer_Object((1,3,6,1,4,1,351,110,5,1,1,1,2,1,1,1,4),_T391LinkIntegrityTimer_Type())
t391LinkIntegrityTimer.setMaxAccess(_E)
if mibBuilder.loadTexts:t391LinkIntegrityTimer.setStatus(_A)
if mibBuilder.loadTexts:t391LinkIntegrityTimer.setUnits(_L)
class _T392PollingVerificationTimer_Type(Integer32):defaultValue=15;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,30))
_T392PollingVerificationTimer_Type.__name__=_D
_T392PollingVerificationTimer_Object=MibTableColumn
t392PollingVerificationTimer=_T392PollingVerificationTimer_Object((1,3,6,1,4,1,351,110,5,1,1,1,2,1,1,1,5),_T392PollingVerificationTimer_Type())
t392PollingVerificationTimer.setMaxAccess(_E)
if mibBuilder.loadTexts:t392PollingVerificationTimer.setStatus(_A)
if mibBuilder.loadTexts:t392PollingVerificationTimer.setUnits(_L)
class _N391FullStatusPollingCounter_Type(Integer32):defaultValue=6;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_N391FullStatusPollingCounter_Type.__name__=_D
_N391FullStatusPollingCounter_Object=MibTableColumn
n391FullStatusPollingCounter=_N391FullStatusPollingCounter_Object((1,3,6,1,4,1,351,110,5,1,1,1,2,1,1,1,6),_N391FullStatusPollingCounter_Type())
n391FullStatusPollingCounter.setMaxAccess(_E)
if mibBuilder.loadTexts:n391FullStatusPollingCounter.setStatus(_A)
if mibBuilder.loadTexts:n391FullStatusPollingCounter.setUnits('Polls')
class _N392ErrorThreshold_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_N392ErrorThreshold_Type.__name__=_D
_N392ErrorThreshold_Object=MibTableColumn
n392ErrorThreshold=_N392ErrorThreshold_Object((1,3,6,1,4,1,351,110,5,1,1,1,2,1,1,1,7),_N392ErrorThreshold_Type())
n392ErrorThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:n392ErrorThreshold.setStatus(_A)
class _N393MonitoredEventCount_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_N393MonitoredEventCount_Type.__name__=_D
_N393MonitoredEventCount_Object=MibTableColumn
n393MonitoredEventCount=_N393MonitoredEventCount_Object((1,3,6,1,4,1,351,110,5,1,1,1,2,1,1,1,8),_N393MonitoredEventCount_Type())
n393MonitoredEventCount.setMaxAccess(_E)
if mibBuilder.loadTexts:n393MonitoredEventCount.setStatus(_A)
if mibBuilder.loadTexts:n393MonitoredEventCount.setUnits('Events')
class _EnhancedLmi_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_EnhancedLmi_Type.__name__=_D
_EnhancedLmi_Object=MibTableColumn
enhancedLmi=_EnhancedLmi_Object((1,3,6,1,4,1,351,110,5,1,1,1,2,1,1,1,9),_EnhancedLmi_Type())
enhancedLmi.setMaxAccess(_E)
if mibBuilder.loadTexts:enhancedLmi.setStatus(_A)
class _PortFRF1Dot2Support_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_PortFRF1Dot2Support_Type.__name__=_D
_PortFRF1Dot2Support_Object=MibTableColumn
portFRF1Dot2Support=_PortFRF1Dot2Support_Object((1,3,6,1,4,1,351,110,5,1,1,1,2,1,1,1,10),_PortFRF1Dot2Support_Type())
portFRF1Dot2Support.setMaxAccess(_E)
if mibBuilder.loadTexts:portFRF1Dot2Support.setStatus(_A)
class _PortLmiSigConfMethod_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('manual',1),('autosense',2)))
_PortLmiSigConfMethod_Type.__name__=_D
_PortLmiSigConfMethod_Object=MibTableColumn
portLmiSigConfMethod=_PortLmiSigConfMethod_Object((1,3,6,1,4,1,351,110,5,1,1,1,2,1,1,1,11),_PortLmiSigConfMethod_Type())
portLmiSigConfMethod.setMaxAccess(_E)
if mibBuilder.loadTexts:portLmiSigConfMethod.setStatus(_A)
_FrPortCnfSigCLLMGrp_ObjectIdentity=ObjectIdentity
frPortCnfSigCLLMGrp=_FrPortCnfSigCLLMGrp_ObjectIdentity((1,3,6,1,4,1,351,110,5,1,1,1,2,2))
_FrPortCnfSigCLLMGrpTable_Object=MibTable
frPortCnfSigCLLMGrpTable=_FrPortCnfSigCLLMGrpTable_Object((1,3,6,1,4,1,351,110,5,1,1,1,2,2,1))
if mibBuilder.loadTexts:frPortCnfSigCLLMGrpTable.setStatus(_A)
_FrPortCnfSigCLLMGrpEntry_Object=MibTableRow
frPortCnfSigCLLMGrpEntry=_FrPortCnfSigCLLMGrpEntry_Object((1,3,6,1,4,1,351,110,5,1,1,1,2,2,1,1))
frPortCnfSigCLLMGrpEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:frPortCnfSigCLLMGrpEntry.setStatus(_A)
class _CllmCnfPortNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CllmCnfPortNum_Type.__name__=_D
_CllmCnfPortNum_Object=MibTableColumn
cllmCnfPortNum=_CllmCnfPortNum_Object((1,3,6,1,4,1,351,110,5,1,1,1,2,2,1,1,1),_CllmCnfPortNum_Type())
cllmCnfPortNum.setMaxAccess(_C)
if mibBuilder.loadTexts:cllmCnfPortNum.setStatus(_A)
class _CllmEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_CllmEnable_Type.__name__=_D
_CllmEnable_Object=MibTableColumn
cllmEnable=_CllmEnable_Object((1,3,6,1,4,1,351,110,5,1,1,1,2,2,1,1,2),_CllmEnable_Type())
cllmEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:cllmEnable.setStatus(_A)
class _XmtCLLMStatusTimer_Type(Integer32):defaultValue=40;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(40,5000))
_XmtCLLMStatusTimer_Type.__name__=_D
_XmtCLLMStatusTimer_Object=MibTableColumn
xmtCLLMStatusTimer=_XmtCLLMStatusTimer_Object((1,3,6,1,4,1,351,110,5,1,1,1,2,2,1,1,3),_XmtCLLMStatusTimer_Type())
xmtCLLMStatusTimer.setMaxAccess(_E)
if mibBuilder.loadTexts:xmtCLLMStatusTimer.setStatus(_A)
if mibBuilder.loadTexts:xmtCLLMStatusTimer.setUnits('milli-seconds')
class _RcvCLLMStatusTimer_Type(Integer32):defaultValue=1000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1000));namedValues=NamedValues(('rcvCLLMTimerValue',1000))
_RcvCLLMStatusTimer_Type.__name__=_D
_RcvCLLMStatusTimer_Object=MibTableColumn
rcvCLLMStatusTimer=_RcvCLLMStatusTimer_Object((1,3,6,1,4,1,351,110,5,1,1,1,2,2,1,1,4),_RcvCLLMStatusTimer_Type())
rcvCLLMStatusTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:rcvCLLMStatusTimer.setStatus(_A)
_FrPortCntSigLMIGrp_ObjectIdentity=ObjectIdentity
frPortCntSigLMIGrp=_FrPortCntSigLMIGrp_ObjectIdentity((1,3,6,1,4,1,351,110,5,1,1,2,2,1))
_FrPortCntSigLMIGrpTable_Object=MibTable
frPortCntSigLMIGrpTable=_FrPortCntSigLMIGrpTable_Object((1,3,6,1,4,1,351,110,5,1,1,2,2,1,1))
if mibBuilder.loadTexts:frPortCntSigLMIGrpTable.setStatus(_A)
_FrPortCntSigLMIGrpEntry_Object=MibTableRow
frPortCntSigLMIGrpEntry=_FrPortCntSigLMIGrpEntry_Object((1,3,6,1,4,1,351,110,5,1,1,2,2,1,1,1))
frPortCntSigLMIGrpEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:frPortCntSigLMIGrpEntry.setStatus(_A)
class _LmiSigPortNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_LmiSigPortNum_Type.__name__=_D
_LmiSigPortNum_Object=MibTableColumn
lmiSigPortNum=_LmiSigPortNum_Object((1,3,6,1,4,1,351,110,5,1,1,2,2,1,1,1,1),_LmiSigPortNum_Type())
lmiSigPortNum.setMaxAccess(_C)
if mibBuilder.loadTexts:lmiSigPortNum.setStatus(_A)
_RcvStatusInquiry_Type=Counter32
_RcvStatusInquiry_Object=MibTableColumn
rcvStatusInquiry=_RcvStatusInquiry_Object((1,3,6,1,4,1,351,110,5,1,1,2,2,1,1,1,2),_RcvStatusInquiry_Type())
rcvStatusInquiry.setMaxAccess(_C)
if mibBuilder.loadTexts:rcvStatusInquiry.setStatus(_A)
_RcvInvalidRequest_Type=Counter32
_RcvInvalidRequest_Object=MibTableColumn
rcvInvalidRequest=_RcvInvalidRequest_Object((1,3,6,1,4,1,351,110,5,1,1,2,2,1,1,1,3),_RcvInvalidRequest_Type())
rcvInvalidRequest.setMaxAccess(_C)
if mibBuilder.loadTexts:rcvInvalidRequest.setStatus(_A)
_RcvUNISeqMismatch_Type=Counter32
_RcvUNISeqMismatch_Object=MibTableColumn
rcvUNISeqMismatch=_RcvUNISeqMismatch_Object((1,3,6,1,4,1,351,110,5,1,1,2,2,1,1,1,4),_RcvUNISeqMismatch_Type())
rcvUNISeqMismatch.setMaxAccess(_C)
if mibBuilder.loadTexts:rcvUNISeqMismatch.setStatus(_A)
_XmtStatus_Type=Counter32
_XmtStatus_Object=MibTableColumn
xmtStatus=_XmtStatus_Object((1,3,6,1,4,1,351,110,5,1,1,2,2,1,1,1,5),_XmtStatus_Type())
xmtStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:xmtStatus.setStatus(_A)
_XmtAsynchUpdate_Type=Counter32
_XmtAsynchUpdate_Object=MibTableColumn
xmtAsynchUpdate=_XmtAsynchUpdate_Object((1,3,6,1,4,1,351,110,5,1,1,2,2,1,1,1,6),_XmtAsynchUpdate_Type())
xmtAsynchUpdate.setMaxAccess(_C)
if mibBuilder.loadTexts:xmtAsynchUpdate.setStatus(_A)
_UniSignalingTimeout_Type=Counter32
_UniSignalingTimeout_Object=MibTableColumn
uniSignalingTimeout=_UniSignalingTimeout_Object((1,3,6,1,4,1,351,110,5,1,1,2,2,1,1,1,7),_UniSignalingTimeout_Type())
uniSignalingTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:uniSignalingTimeout.setStatus(_A)
_XmtStatusInquiry_Type=Counter32
_XmtStatusInquiry_Object=MibTableColumn
xmtStatusInquiry=_XmtStatusInquiry_Object((1,3,6,1,4,1,351,110,5,1,1,2,2,1,1,1,8),_XmtStatusInquiry_Type())
xmtStatusInquiry.setMaxAccess(_C)
if mibBuilder.loadTexts:xmtStatusInquiry.setStatus(_A)
_RcvStatus_Type=Counter32
_RcvStatus_Object=MibTableColumn
rcvStatus=_RcvStatus_Object((1,3,6,1,4,1,351,110,5,1,1,2,2,1,1,1,9),_RcvStatus_Type())
rcvStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:rcvStatus.setStatus(_A)
_RcvAsynchUpdate_Type=Counter32
_RcvAsynchUpdate_Object=MibTableColumn
rcvAsynchUpdate=_RcvAsynchUpdate_Object((1,3,6,1,4,1,351,110,5,1,1,2,2,1,1,1,10),_RcvAsynchUpdate_Type())
rcvAsynchUpdate.setMaxAccess(_C)
if mibBuilder.loadTexts:rcvAsynchUpdate.setStatus(_A)
_RcvNNISeqMismatch_Type=Counter32
_RcvNNISeqMismatch_Object=MibTableColumn
rcvNNISeqMismatch=_RcvNNISeqMismatch_Object((1,3,6,1,4,1,351,110,5,1,1,2,2,1,1,1,11),_RcvNNISeqMismatch_Type())
rcvNNISeqMismatch.setMaxAccess(_C)
if mibBuilder.loadTexts:rcvNNISeqMismatch.setStatus(_A)
_NniSignalingTimeout_Type=Counter32
_NniSignalingTimeout_Object=MibTableColumn
nniSignalingTimeout=_NniSignalingTimeout_Object((1,3,6,1,4,1,351,110,5,1,1,2,2,1,1,1,12),_NniSignalingTimeout_Type())
nniSignalingTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:nniSignalingTimeout.setStatus(_A)
_FrPortCntSigCLLMGrp_ObjectIdentity=ObjectIdentity
frPortCntSigCLLMGrp=_FrPortCntSigCLLMGrp_ObjectIdentity((1,3,6,1,4,1,351,110,5,1,1,2,2,2))
_FrPortCntSigCLLMGrpTable_Object=MibTable
frPortCntSigCLLMGrpTable=_FrPortCntSigCLLMGrpTable_Object((1,3,6,1,4,1,351,110,5,1,1,2,2,2,1))
if mibBuilder.loadTexts:frPortCntSigCLLMGrpTable.setStatus(_A)
_FrPortCntSigCLLMGrpEntry_Object=MibTableRow
frPortCntSigCLLMGrpEntry=_FrPortCntSigCLLMGrpEntry_Object((1,3,6,1,4,1,351,110,5,1,1,2,2,2,1,1))
frPortCntSigCLLMGrpEntry.setIndexNames((0,_B,_K))
if mibBuilder.loadTexts:frPortCntSigCLLMGrpEntry.setStatus(_A)
class _CllmSigPortNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CllmSigPortNum_Type.__name__=_D
_CllmSigPortNum_Object=MibTableColumn
cllmSigPortNum=_CllmSigPortNum_Object((1,3,6,1,4,1,351,110,5,1,1,2,2,2,1,1,1),_CllmSigPortNum_Type())
cllmSigPortNum.setMaxAccess(_C)
if mibBuilder.loadTexts:cllmSigPortNum.setStatus(_A)
_RcvFramesCLLM_Type=Counter32
_RcvFramesCLLM_Object=MibTableColumn
rcvFramesCLLM=_RcvFramesCLLM_Object((1,3,6,1,4,1,351,110,5,1,1,2,2,2,1,1,2),_RcvFramesCLLM_Type())
rcvFramesCLLM.setMaxAccess(_C)
if mibBuilder.loadTexts:rcvFramesCLLM.setStatus(_A)
if mibBuilder.loadTexts:rcvFramesCLLM.setUnits(_M)
_RcvBytesCLLM_Type=Counter32
_RcvBytesCLLM_Object=MibTableColumn
rcvBytesCLLM=_RcvBytesCLLM_Object((1,3,6,1,4,1,351,110,5,1,1,2,2,2,1,1,3),_RcvBytesCLLM_Type())
rcvBytesCLLM.setMaxAccess(_C)
if mibBuilder.loadTexts:rcvBytesCLLM.setStatus(_A)
if mibBuilder.loadTexts:rcvBytesCLLM.setUnits('bytes')
_XmtFramesCLLM_Type=Counter32
_XmtFramesCLLM_Object=MibTableColumn
xmtFramesCLLM=_XmtFramesCLLM_Object((1,3,6,1,4,1,351,110,5,1,1,2,2,2,1,1,4),_XmtFramesCLLM_Type())
xmtFramesCLLM.setMaxAccess(_C)
if mibBuilder.loadTexts:xmtFramesCLLM.setStatus(_A)
if mibBuilder.loadTexts:xmtFramesCLLM.setUnits(_M)
_XmtBytesCLLM_Type=Counter32
_XmtBytesCLLM_Object=MibTableColumn
xmtBytesCLLM=_XmtBytesCLLM_Object((1,3,6,1,4,1,351,110,5,1,1,2,2,2,1,1,5),_XmtBytesCLLM_Type())
xmtBytesCLLM.setMaxAccess(_C)
if mibBuilder.loadTexts:xmtBytesCLLM.setStatus(_A)
if mibBuilder.loadTexts:xmtBytesCLLM.setUnits('bytes')
_CllmFailures_Type=Counter32
_CllmFailures_Object=MibTableColumn
cllmFailures=_CllmFailures_Object((1,3,6,1,4,1,351,110,5,1,1,2,2,2,1,1,6),_CllmFailures_Type())
cllmFailures.setMaxAccess(_C)
if mibBuilder.loadTexts:cllmFailures.setStatus(_A)
_CwfSignalingMIBConformance_ObjectIdentity=ObjectIdentity
cwfSignalingMIBConformance=_CwfSignalingMIBConformance_ObjectIdentity((1,3,6,1,4,1,351,150,46,2))
_CwfSignalingMIBGroups_ObjectIdentity=ObjectIdentity
cwfSignalingMIBGroups=_CwfSignalingMIBGroups_ObjectIdentity((1,3,6,1,4,1,351,150,46,2,1))
_CwfSignalingMIBCompliances_ObjectIdentity=ObjectIdentity
cwfSignalingMIBCompliances=_CwfSignalingMIBCompliances_ObjectIdentity((1,3,6,1,4,1,351,150,46,2,2))
ciscoWanFrLmiConfigGroup=ObjectGroup((1,3,6,1,4,1,351,150,46,2,1,1))
ciscoWanFrLmiConfigGroup.setObjects(*((_B,_H),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W)))
if mibBuilder.loadTexts:ciscoWanFrLmiConfigGroup.setStatus(_A)
ciscoWanFrLmiStatsGroup=ObjectGroup((1,3,6,1,4,1,351,150,46,2,1,2))
ciscoWanFrLmiStatsGroup.setObjects(*((_B,_J),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h)))
if mibBuilder.loadTexts:ciscoWanFrLmiStatsGroup.setStatus(_A)
ciscoWanFrCllmGroup=ObjectGroup((1,3,6,1,4,1,351,150,46,2,1,3))
ciscoWanFrCllmGroup.setObjects(*((_B,_I),(_B,_i),(_B,_j),(_B,_k)))
if mibBuilder.loadTexts:ciscoWanFrCllmGroup.setStatus(_A)
ciscoWanFrCllmStatsGroup=ObjectGroup((1,3,6,1,4,1,351,150,46,2,1,4))
ciscoWanFrCllmStatsGroup.setObjects(*((_B,_K),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p)))
if mibBuilder.loadTexts:ciscoWanFrCllmStatsGroup.setStatus(_A)
cwfSignalingMIBCompliance=ModuleCompliance((1,3,6,1,4,1,351,150,46,2,2,1))
cwfSignalingMIBCompliance.setObjects(*((_B,_q),(_B,_r),(_B,_s),(_B,_t)))
if mibBuilder.loadTexts:cwfSignalingMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'frPortCnfSigLMIGrp':frPortCnfSigLMIGrp,'frPortCnfSigLMIGrpTable':frPortCnfSigLMIGrpTable,'frPortCnfSigLMIGrpEntry':frPortCnfSigLMIGrpEntry,_H:lmiCnfPortNum,_N:signallingProtocolType,_O:asynchronousUpdates,_P:t391LinkIntegrityTimer,_Q:t392PollingVerificationTimer,_R:n391FullStatusPollingCounter,_S:n392ErrorThreshold,_T:n393MonitoredEventCount,_U:enhancedLmi,_V:portFRF1Dot2Support,_W:portLmiSigConfMethod,'frPortCnfSigCLLMGrp':frPortCnfSigCLLMGrp,'frPortCnfSigCLLMGrpTable':frPortCnfSigCLLMGrpTable,'frPortCnfSigCLLMGrpEntry':frPortCnfSigCLLMGrpEntry,_I:cllmCnfPortNum,_i:cllmEnable,_j:xmtCLLMStatusTimer,_k:rcvCLLMStatusTimer,'frPortCntSigLMIGrp':frPortCntSigLMIGrp,'frPortCntSigLMIGrpTable':frPortCntSigLMIGrpTable,'frPortCntSigLMIGrpEntry':frPortCntSigLMIGrpEntry,_J:lmiSigPortNum,_X:rcvStatusInquiry,_Y:rcvInvalidRequest,_Z:rcvUNISeqMismatch,_a:xmtStatus,_b:xmtAsynchUpdate,_c:uniSignalingTimeout,_d:xmtStatusInquiry,_e:rcvStatus,_f:rcvAsynchUpdate,_g:rcvNNISeqMismatch,_h:nniSignalingTimeout,'frPortCntSigCLLMGrp':frPortCntSigCLLMGrp,'frPortCntSigCLLMGrpTable':frPortCntSigCLLMGrpTable,'frPortCntSigCLLMGrpEntry':frPortCntSigCLLMGrpEntry,_K:cllmSigPortNum,_l:rcvFramesCLLM,_m:rcvBytesCLLM,_n:xmtFramesCLLM,_o:xmtBytesCLLM,_p:cllmFailures,'ciscoWanFrSignalingMIB':ciscoWanFrSignalingMIB,'cwfSignalingMIBConformance':cwfSignalingMIBConformance,'cwfSignalingMIBGroups':cwfSignalingMIBGroups,_q:ciscoWanFrLmiConfigGroup,_r:ciscoWanFrLmiStatsGroup,_s:ciscoWanFrCllmGroup,_t:ciscoWanFrCllmStatsGroup,'cwfSignalingMIBCompliances':cwfSignalingMIBCompliances,'cwfSignalingMIBCompliance':cwfSignalingMIBCompliance})