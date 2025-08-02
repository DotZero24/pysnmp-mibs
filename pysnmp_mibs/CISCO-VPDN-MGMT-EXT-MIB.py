_t='cvpdnTunnelExtGroupV2'
_s='cvpdnTunnelExtGroup'
_r='cvpdnTunnelBytesOut64'
_q='cvpdnTunnelBytesIn64'
_p='cvpdnSessionZLBTime'
_o='cvpdnSessionPktProcessingDelay'
_n='cvpdnSessionRoundTripTime'
_m='cvpdnSessionAdaptiveTimeOut'
_l='cvpdnSessionCalculationType'
_k='cvpdnSessionOutGoingQueueSize'
_j='cvpdnSessionATOTimeouts'
_i='cvpdnSessionMinimumWindowSize'
_h='cvpdnSessionCurrentWindowSize'
_g='cvpdnSessionRemoteWindowSize'
_f='cvpdnSessionLocalWindowSize'
_e='cvpdnSessionRecvRBits'
_d='cvpdnSessionSentRBits'
_c='cvpdnSessionRecvZLB'
_b='cvpdnSessionSentZLB'
_a='cvpdnSessionOutOfOrderPackets'
_Z='cvpdnSessionRemoteRecvSequence'
_Y='cvpdnSessionRemoteSendSequence'
_X='cvpdnSessionRecvSequence'
_W='cvpdnSessionSendSequence'
_V='cvpdnSessionSequencing'
_U='cvpdnSessionLastChange'
_T='cvpdnSessionInterfaceName'
_S='cvpdnSessionRemoteId'
_R='cvpdnTunnelBytesOut'
_Q='cvpdnTunnelBytesIn'
_P='cvpdnSessionExtEntry'
_O='cvpdnTunnelExtEntry'
_N='DisplayString'
_M='cvpdnSessionExtGroup'
_L='cvpdnTunnelPacketsOut'
_K='cvpdnTunnelPacketsIn'
_J='cvpdnTunnelLastChange'
_I='cvpdnTunnelRemotePort'
_H='cvpdnTunnelLocalPort'
_G='msecs'
_F='deprecated'
_E='packets'
_D='Integer32'
_C='read-only'
_B='current'
_A='CISCO-VPDN-MGMT-EXT-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoExperiment,=mibBuilder.importSymbols('CISCO-SMI','ciscoExperiment')
cvpdnSessionAttrEntry,cvpdnTunnelAttrEntry=mibBuilder.importSymbols('CISCO-VPDN-MGMT-MIB','cvpdnSessionAttrEntry','cvpdnTunnelAttrEntry')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_N,'PhysAddress','TextualConvention','TruthValue')
ciscoVpdnMgmtExtMIB=ModuleIdentity((1,3,6,1,4,1,9,10,51))
if mibBuilder.loadTexts:ciscoVpdnMgmtExtMIB.setRevisions(('2011-12-01 00:00','2007-06-04 00:00','1999-04-14 00:00'))
_CiscoVpdnMgmtExtMIBObjects_ObjectIdentity=ObjectIdentity
ciscoVpdnMgmtExtMIBObjects=_CiscoVpdnMgmtExtMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,10,51,1))
_CvpdnTunnelExtInfo_ObjectIdentity=ObjectIdentity
cvpdnTunnelExtInfo=_CvpdnTunnelExtInfo_ObjectIdentity((1,3,6,1,4,1,9,10,51,1,1))
_CvpdnTunnelExtTable_Object=MibTable
cvpdnTunnelExtTable=_CvpdnTunnelExtTable_Object((1,3,6,1,4,1,9,10,51,1,1,1))
if mibBuilder.loadTexts:cvpdnTunnelExtTable.setStatus(_B)
_CvpdnTunnelExtEntry_Object=MibTableRow
cvpdnTunnelExtEntry=_CvpdnTunnelExtEntry_Object((1,3,6,1,4,1,9,10,51,1,1,1,1))
if mibBuilder.loadTexts:cvpdnTunnelExtEntry.setStatus(_B)
class _CvpdnTunnelLocalPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CvpdnTunnelLocalPort_Type.__name__=_D
_CvpdnTunnelLocalPort_Object=MibTableColumn
cvpdnTunnelLocalPort=_CvpdnTunnelLocalPort_Object((1,3,6,1,4,1,9,10,51,1,1,1,1,1),_CvpdnTunnelLocalPort_Type())
cvpdnTunnelLocalPort.setMaxAccess(_C)
if mibBuilder.loadTexts:cvpdnTunnelLocalPort.setStatus(_B)
class _CvpdnTunnelRemotePort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CvpdnTunnelRemotePort_Type.__name__=_D
_CvpdnTunnelRemotePort_Object=MibTableColumn
cvpdnTunnelRemotePort=_CvpdnTunnelRemotePort_Object((1,3,6,1,4,1,9,10,51,1,1,1,1,2),_CvpdnTunnelRemotePort_Type())
cvpdnTunnelRemotePort.setMaxAccess(_C)
if mibBuilder.loadTexts:cvpdnTunnelRemotePort.setStatus(_B)
_CvpdnTunnelLastChange_Type=TimeTicks
_CvpdnTunnelLastChange_Object=MibTableColumn
cvpdnTunnelLastChange=_CvpdnTunnelLastChange_Object((1,3,6,1,4,1,9,10,51,1,1,1,1,3),_CvpdnTunnelLastChange_Type())
cvpdnTunnelLastChange.setMaxAccess(_C)
if mibBuilder.loadTexts:cvpdnTunnelLastChange.setStatus(_B)
_CvpdnTunnelPacketsOut_Type=Counter32
_CvpdnTunnelPacketsOut_Object=MibTableColumn
cvpdnTunnelPacketsOut=_CvpdnTunnelPacketsOut_Object((1,3,6,1,4,1,9,10,51,1,1,1,1,4),_CvpdnTunnelPacketsOut_Type())
cvpdnTunnelPacketsOut.setMaxAccess(_C)
if mibBuilder.loadTexts:cvpdnTunnelPacketsOut.setStatus(_B)
if mibBuilder.loadTexts:cvpdnTunnelPacketsOut.setUnits(_E)
_CvpdnTunnelBytesOut_Type=Counter32
_CvpdnTunnelBytesOut_Object=MibTableColumn
cvpdnTunnelBytesOut=_CvpdnTunnelBytesOut_Object((1,3,6,1,4,1,9,10,51,1,1,1,1,5),_CvpdnTunnelBytesOut_Type())
cvpdnTunnelBytesOut.setMaxAccess(_C)
if mibBuilder.loadTexts:cvpdnTunnelBytesOut.setStatus(_F)
if mibBuilder.loadTexts:cvpdnTunnelBytesOut.setUnits('bytes')
_CvpdnTunnelPacketsIn_Type=Counter32
_CvpdnTunnelPacketsIn_Object=MibTableColumn
cvpdnTunnelPacketsIn=_CvpdnTunnelPacketsIn_Object((1,3,6,1,4,1,9,10,51,1,1,1,1,6),_CvpdnTunnelPacketsIn_Type())
cvpdnTunnelPacketsIn.setMaxAccess(_C)
if mibBuilder.loadTexts:cvpdnTunnelPacketsIn.setStatus(_B)
if mibBuilder.loadTexts:cvpdnTunnelPacketsIn.setUnits(_E)
_CvpdnTunnelBytesIn_Type=Counter32
_CvpdnTunnelBytesIn_Object=MibTableColumn
cvpdnTunnelBytesIn=_CvpdnTunnelBytesIn_Object((1,3,6,1,4,1,9,10,51,1,1,1,1,7),_CvpdnTunnelBytesIn_Type())
cvpdnTunnelBytesIn.setMaxAccess(_C)
if mibBuilder.loadTexts:cvpdnTunnelBytesIn.setStatus(_F)
if mibBuilder.loadTexts:cvpdnTunnelBytesIn.setUnits('bytes')
_CvpdnTunnelBytesIn64_Type=Counter64
_CvpdnTunnelBytesIn64_Object=MibTableColumn
cvpdnTunnelBytesIn64=_CvpdnTunnelBytesIn64_Object((1,3,6,1,4,1,9,10,51,1,1,1,1,8),_CvpdnTunnelBytesIn64_Type())
cvpdnTunnelBytesIn64.setMaxAccess(_C)
if mibBuilder.loadTexts:cvpdnTunnelBytesIn64.setStatus(_B)
_CvpdnTunnelBytesOut64_Type=Counter64
_CvpdnTunnelBytesOut64_Object=MibTableColumn
cvpdnTunnelBytesOut64=_CvpdnTunnelBytesOut64_Object((1,3,6,1,4,1,9,10,51,1,1,1,1,9),_CvpdnTunnelBytesOut64_Type())
cvpdnTunnelBytesOut64.setMaxAccess(_C)
if mibBuilder.loadTexts:cvpdnTunnelBytesOut64.setStatus(_B)
_CvpdnSessionExtInfo_ObjectIdentity=ObjectIdentity
cvpdnSessionExtInfo=_CvpdnSessionExtInfo_ObjectIdentity((1,3,6,1,4,1,9,10,51,1,2))
_CvpdnSessionExtTable_Object=MibTable
cvpdnSessionExtTable=_CvpdnSessionExtTable_Object((1,3,6,1,4,1,9,10,51,1,2,1))
if mibBuilder.loadTexts:cvpdnSessionExtTable.setStatus(_B)
_CvpdnSessionExtEntry_Object=MibTableRow
cvpdnSessionExtEntry=_CvpdnSessionExtEntry_Object((1,3,6,1,4,1,9,10,51,1,2,1,1))
if mibBuilder.loadTexts:cvpdnSessionExtEntry.setStatus(_B)
class _CvpdnSessionRemoteId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CvpdnSessionRemoteId_Type.__name__=_D
_CvpdnSessionRemoteId_Object=MibTableColumn
cvpdnSessionRemoteId=_CvpdnSessionRemoteId_Object((1,3,6,1,4,1,9,10,51,1,2,1,1,1),_CvpdnSessionRemoteId_Type())
cvpdnSessionRemoteId.setMaxAccess(_C)
if mibBuilder.loadTexts:cvpdnSessionRemoteId.setStatus(_B)
class _CvpdnSessionInterfaceName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_CvpdnSessionInterfaceName_Type.__name__=_N
_CvpdnSessionInterfaceName_Object=MibTableColumn
cvpdnSessionInterfaceName=_CvpdnSessionInterfaceName_Object((1,3,6,1,4,1,9,10,51,1,2,1,1,2),_CvpdnSessionInterfaceName_Type())
cvpdnSessionInterfaceName.setMaxAccess(_C)
if mibBuilder.loadTexts:cvpdnSessionInterfaceName.setStatus(_B)
_CvpdnSessionLastChange_Type=TimeTicks
_CvpdnSessionLastChange_Object=MibTableColumn
cvpdnSessionLastChange=_CvpdnSessionLastChange_Object((1,3,6,1,4,1,9,10,51,1,2,1,1,3),_CvpdnSessionLastChange_Type())
cvpdnSessionLastChange.setMaxAccess(_C)
if mibBuilder.loadTexts:cvpdnSessionLastChange.setStatus(_B)
_CvpdnSessionOutOfOrderPackets_Type=Counter32
_CvpdnSessionOutOfOrderPackets_Object=MibTableColumn
cvpdnSessionOutOfOrderPackets=_CvpdnSessionOutOfOrderPackets_Object((1,3,6,1,4,1,9,10,51,1,2,1,1,4),_CvpdnSessionOutOfOrderPackets_Type())
cvpdnSessionOutOfOrderPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:cvpdnSessionOutOfOrderPackets.setStatus(_B)
if mibBuilder.loadTexts:cvpdnSessionOutOfOrderPackets.setUnits(_E)
_CvpdnSessionSequencing_Type=TruthValue
_CvpdnSessionSequencing_Object=MibTableColumn
cvpdnSessionSequencing=_CvpdnSessionSequencing_Object((1,3,6,1,4,1,9,10,51,1,2,1,1,5),_CvpdnSessionSequencing_Type())
cvpdnSessionSequencing.setMaxAccess(_C)
if mibBuilder.loadTexts:cvpdnSessionSequencing.setStatus(_B)
class _CvpdnSessionSendSequence_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CvpdnSessionSendSequence_Type.__name__=_D
_CvpdnSessionSendSequence_Object=MibTableColumn
cvpdnSessionSendSequence=_CvpdnSessionSendSequence_Object((1,3,6,1,4,1,9,10,51,1,2,1,1,6),_CvpdnSessionSendSequence_Type())
cvpdnSessionSendSequence.setMaxAccess(_C)
if mibBuilder.loadTexts:cvpdnSessionSendSequence.setStatus(_B)
class _CvpdnSessionRecvSequence_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CvpdnSessionRecvSequence_Type.__name__=_D
_CvpdnSessionRecvSequence_Object=MibTableColumn
cvpdnSessionRecvSequence=_CvpdnSessionRecvSequence_Object((1,3,6,1,4,1,9,10,51,1,2,1,1,7),_CvpdnSessionRecvSequence_Type())
cvpdnSessionRecvSequence.setMaxAccess(_C)
if mibBuilder.loadTexts:cvpdnSessionRecvSequence.setStatus(_B)
class _CvpdnSessionRemoteSendSequence_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CvpdnSessionRemoteSendSequence_Type.__name__=_D
_CvpdnSessionRemoteSendSequence_Object=MibTableColumn
cvpdnSessionRemoteSendSequence=_CvpdnSessionRemoteSendSequence_Object((1,3,6,1,4,1,9,10,51,1,2,1,1,8),_CvpdnSessionRemoteSendSequence_Type())
cvpdnSessionRemoteSendSequence.setMaxAccess(_C)
if mibBuilder.loadTexts:cvpdnSessionRemoteSendSequence.setStatus(_B)
class _CvpdnSessionRemoteRecvSequence_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CvpdnSessionRemoteRecvSequence_Type.__name__=_D
_CvpdnSessionRemoteRecvSequence_Object=MibTableColumn
cvpdnSessionRemoteRecvSequence=_CvpdnSessionRemoteRecvSequence_Object((1,3,6,1,4,1,9,10,51,1,2,1,1,9),_CvpdnSessionRemoteRecvSequence_Type())
cvpdnSessionRemoteRecvSequence.setMaxAccess(_C)
if mibBuilder.loadTexts:cvpdnSessionRemoteRecvSequence.setStatus(_B)
_CvpdnSessionSentZLB_Type=Counter32
_CvpdnSessionSentZLB_Object=MibTableColumn
cvpdnSessionSentZLB=_CvpdnSessionSentZLB_Object((1,3,6,1,4,1,9,10,51,1,2,1,1,10),_CvpdnSessionSentZLB_Type())
cvpdnSessionSentZLB.setMaxAccess(_C)
if mibBuilder.loadTexts:cvpdnSessionSentZLB.setStatus(_B)
_CvpdnSessionRecvZLB_Type=Counter32
_CvpdnSessionRecvZLB_Object=MibTableColumn
cvpdnSessionRecvZLB=_CvpdnSessionRecvZLB_Object((1,3,6,1,4,1,9,10,51,1,2,1,1,11),_CvpdnSessionRecvZLB_Type())
cvpdnSessionRecvZLB.setMaxAccess(_C)
if mibBuilder.loadTexts:cvpdnSessionRecvZLB.setStatus(_B)
_CvpdnSessionSentRBits_Type=Counter32
_CvpdnSessionSentRBits_Object=MibTableColumn
cvpdnSessionSentRBits=_CvpdnSessionSentRBits_Object((1,3,6,1,4,1,9,10,51,1,2,1,1,12),_CvpdnSessionSentRBits_Type())
cvpdnSessionSentRBits.setMaxAccess(_C)
if mibBuilder.loadTexts:cvpdnSessionSentRBits.setStatus(_B)
_CvpdnSessionRecvRBits_Type=Counter32
_CvpdnSessionRecvRBits_Object=MibTableColumn
cvpdnSessionRecvRBits=_CvpdnSessionRecvRBits_Object((1,3,6,1,4,1,9,10,51,1,2,1,1,13),_CvpdnSessionRecvRBits_Type())
cvpdnSessionRecvRBits.setMaxAccess(_C)
if mibBuilder.loadTexts:cvpdnSessionRecvRBits.setStatus(_B)
class _CvpdnSessionLocalWindowSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CvpdnSessionLocalWindowSize_Type.__name__=_D
_CvpdnSessionLocalWindowSize_Object=MibTableColumn
cvpdnSessionLocalWindowSize=_CvpdnSessionLocalWindowSize_Object((1,3,6,1,4,1,9,10,51,1,2,1,1,14),_CvpdnSessionLocalWindowSize_Type())
cvpdnSessionLocalWindowSize.setMaxAccess(_C)
if mibBuilder.loadTexts:cvpdnSessionLocalWindowSize.setStatus(_B)
class _CvpdnSessionRemoteWindowSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CvpdnSessionRemoteWindowSize_Type.__name__=_D
_CvpdnSessionRemoteWindowSize_Object=MibTableColumn
cvpdnSessionRemoteWindowSize=_CvpdnSessionRemoteWindowSize_Object((1,3,6,1,4,1,9,10,51,1,2,1,1,15),_CvpdnSessionRemoteWindowSize_Type())
cvpdnSessionRemoteWindowSize.setMaxAccess(_C)
if mibBuilder.loadTexts:cvpdnSessionRemoteWindowSize.setStatus(_B)
class _CvpdnSessionCurrentWindowSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CvpdnSessionCurrentWindowSize_Type.__name__=_D
_CvpdnSessionCurrentWindowSize_Object=MibTableColumn
cvpdnSessionCurrentWindowSize=_CvpdnSessionCurrentWindowSize_Object((1,3,6,1,4,1,9,10,51,1,2,1,1,16),_CvpdnSessionCurrentWindowSize_Type())
cvpdnSessionCurrentWindowSize.setMaxAccess(_C)
if mibBuilder.loadTexts:cvpdnSessionCurrentWindowSize.setStatus(_B)
class _CvpdnSessionMinimumWindowSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CvpdnSessionMinimumWindowSize_Type.__name__=_D
_CvpdnSessionMinimumWindowSize_Object=MibTableColumn
cvpdnSessionMinimumWindowSize=_CvpdnSessionMinimumWindowSize_Object((1,3,6,1,4,1,9,10,51,1,2,1,1,17),_CvpdnSessionMinimumWindowSize_Type())
cvpdnSessionMinimumWindowSize.setMaxAccess(_C)
if mibBuilder.loadTexts:cvpdnSessionMinimumWindowSize.setStatus(_B)
class _CvpdnSessionATOTimeouts_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CvpdnSessionATOTimeouts_Type.__name__=_D
_CvpdnSessionATOTimeouts_Object=MibTableColumn
cvpdnSessionATOTimeouts=_CvpdnSessionATOTimeouts_Object((1,3,6,1,4,1,9,10,51,1,2,1,1,18),_CvpdnSessionATOTimeouts_Type())
cvpdnSessionATOTimeouts.setMaxAccess(_C)
if mibBuilder.loadTexts:cvpdnSessionATOTimeouts.setStatus(_B)
if mibBuilder.loadTexts:cvpdnSessionATOTimeouts.setUnits(_G)
class _CvpdnSessionOutGoingQueueSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CvpdnSessionOutGoingQueueSize_Type.__name__=_D
_CvpdnSessionOutGoingQueueSize_Object=MibTableColumn
cvpdnSessionOutGoingQueueSize=_CvpdnSessionOutGoingQueueSize_Object((1,3,6,1,4,1,9,10,51,1,2,1,1,19),_CvpdnSessionOutGoingQueueSize_Type())
cvpdnSessionOutGoingQueueSize.setMaxAccess(_C)
if mibBuilder.loadTexts:cvpdnSessionOutGoingQueueSize.setStatus(_B)
class _CvpdnSessionCalculationType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('manual',1),('adaptive',2)))
_CvpdnSessionCalculationType_Type.__name__=_D
_CvpdnSessionCalculationType_Object=MibTableColumn
cvpdnSessionCalculationType=_CvpdnSessionCalculationType_Object((1,3,6,1,4,1,9,10,51,1,2,1,1,20),_CvpdnSessionCalculationType_Type())
cvpdnSessionCalculationType.setMaxAccess(_C)
if mibBuilder.loadTexts:cvpdnSessionCalculationType.setStatus(_B)
class _CvpdnSessionAdaptiveTimeOut_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CvpdnSessionAdaptiveTimeOut_Type.__name__=_D
_CvpdnSessionAdaptiveTimeOut_Object=MibTableColumn
cvpdnSessionAdaptiveTimeOut=_CvpdnSessionAdaptiveTimeOut_Object((1,3,6,1,4,1,9,10,51,1,2,1,1,21),_CvpdnSessionAdaptiveTimeOut_Type())
cvpdnSessionAdaptiveTimeOut.setMaxAccess(_C)
if mibBuilder.loadTexts:cvpdnSessionAdaptiveTimeOut.setStatus(_B)
if mibBuilder.loadTexts:cvpdnSessionAdaptiveTimeOut.setUnits(_G)
class _CvpdnSessionRoundTripTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CvpdnSessionRoundTripTime_Type.__name__=_D
_CvpdnSessionRoundTripTime_Object=MibTableColumn
cvpdnSessionRoundTripTime=_CvpdnSessionRoundTripTime_Object((1,3,6,1,4,1,9,10,51,1,2,1,1,22),_CvpdnSessionRoundTripTime_Type())
cvpdnSessionRoundTripTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cvpdnSessionRoundTripTime.setStatus(_B)
if mibBuilder.loadTexts:cvpdnSessionRoundTripTime.setUnits(_G)
class _CvpdnSessionPktProcessingDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CvpdnSessionPktProcessingDelay_Type.__name__=_D
_CvpdnSessionPktProcessingDelay_Object=MibTableColumn
cvpdnSessionPktProcessingDelay=_CvpdnSessionPktProcessingDelay_Object((1,3,6,1,4,1,9,10,51,1,2,1,1,23),_CvpdnSessionPktProcessingDelay_Type())
cvpdnSessionPktProcessingDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:cvpdnSessionPktProcessingDelay.setStatus(_B)
if mibBuilder.loadTexts:cvpdnSessionPktProcessingDelay.setUnits(_E)
class _CvpdnSessionZLBTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CvpdnSessionZLBTime_Type.__name__=_D
_CvpdnSessionZLBTime_Object=MibTableColumn
cvpdnSessionZLBTime=_CvpdnSessionZLBTime_Object((1,3,6,1,4,1,9,10,51,1,2,1,1,24),_CvpdnSessionZLBTime_Type())
cvpdnSessionZLBTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cvpdnSessionZLBTime.setStatus(_B)
if mibBuilder.loadTexts:cvpdnSessionZLBTime.setUnits(_G)
_CiscoVpdnMgtExtMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
ciscoVpdnMgtExtMIBNotificationPrefix=_CiscoVpdnMgtExtMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,9,10,51,2))
_CiscoVpdnMgmtExtMIBConformance_ObjectIdentity=ObjectIdentity
ciscoVpdnMgmtExtMIBConformance=_CiscoVpdnMgmtExtMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,10,51,3))
_CiscoVpdnMgmtExtMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoVpdnMgmtExtMIBCompliances=_CiscoVpdnMgmtExtMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,10,51,3,1))
_CiscoVpdnMgmtExtMIBGroups_ObjectIdentity=ObjectIdentity
ciscoVpdnMgmtExtMIBGroups=_CiscoVpdnMgmtExtMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,10,51,3,2))
cvpdnTunnelAttrEntry.registerAugmentions((_A,_O))
cvpdnTunnelExtEntry.setIndexNames(*cvpdnTunnelAttrEntry.getIndexNames())
cvpdnSessionAttrEntry.registerAugmentions((_A,_P))
cvpdnSessionExtEntry.setIndexNames(*cvpdnSessionAttrEntry.getIndexNames())
cvpdnTunnelExtGroup=ObjectGroup((1,3,6,1,4,1,9,10,51,3,2,1))
cvpdnTunnelExtGroup.setObjects(*((_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_Q),(_A,_R)))
if mibBuilder.loadTexts:cvpdnTunnelExtGroup.setStatus(_F)
cvpdnSessionExtGroup=ObjectGroup((1,3,6,1,4,1,9,10,51,3,2,2))
cvpdnSessionExtGroup.setObjects(*((_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p)))
if mibBuilder.loadTexts:cvpdnSessionExtGroup.setStatus(_B)
cvpdnTunnelExtGroupV2=ObjectGroup((1,3,6,1,4,1,9,10,51,3,2,3))
cvpdnTunnelExtGroupV2.setObjects(*((_A,_H),(_A,_I),(_A,_J),(_A,_L),(_A,_K),(_A,_q),(_A,_r)))
if mibBuilder.loadTexts:cvpdnTunnelExtGroupV2.setStatus(_B)
ciscoVpdnMgmtExtMIBBasicCompliance=ModuleCompliance((1,3,6,1,4,1,9,10,51,3,1,1))
ciscoVpdnMgmtExtMIBBasicCompliance.setObjects(*((_A,_s),(_A,_M)))
if mibBuilder.loadTexts:ciscoVpdnMgmtExtMIBBasicCompliance.setStatus(_F)
ciscoVpdnMgmtExtMIBBasicComplianceV2=ModuleCompliance((1,3,6,1,4,1,9,10,51,3,1,2))
ciscoVpdnMgmtExtMIBBasicComplianceV2.setObjects(*((_A,_M),(_A,_t)))
if mibBuilder.loadTexts:ciscoVpdnMgmtExtMIBBasicComplianceV2.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ciscoVpdnMgmtExtMIB':ciscoVpdnMgmtExtMIB,'ciscoVpdnMgmtExtMIBObjects':ciscoVpdnMgmtExtMIBObjects,'cvpdnTunnelExtInfo':cvpdnTunnelExtInfo,'cvpdnTunnelExtTable':cvpdnTunnelExtTable,_O:cvpdnTunnelExtEntry,_H:cvpdnTunnelLocalPort,_I:cvpdnTunnelRemotePort,_J:cvpdnTunnelLastChange,_L:cvpdnTunnelPacketsOut,_R:cvpdnTunnelBytesOut,_K:cvpdnTunnelPacketsIn,_Q:cvpdnTunnelBytesIn,_q:cvpdnTunnelBytesIn64,_r:cvpdnTunnelBytesOut64,'cvpdnSessionExtInfo':cvpdnSessionExtInfo,'cvpdnSessionExtTable':cvpdnSessionExtTable,_P:cvpdnSessionExtEntry,_S:cvpdnSessionRemoteId,_T:cvpdnSessionInterfaceName,_U:cvpdnSessionLastChange,_a:cvpdnSessionOutOfOrderPackets,_V:cvpdnSessionSequencing,_W:cvpdnSessionSendSequence,_X:cvpdnSessionRecvSequence,_Y:cvpdnSessionRemoteSendSequence,_Z:cvpdnSessionRemoteRecvSequence,_b:cvpdnSessionSentZLB,_c:cvpdnSessionRecvZLB,_d:cvpdnSessionSentRBits,_e:cvpdnSessionRecvRBits,_f:cvpdnSessionLocalWindowSize,_g:cvpdnSessionRemoteWindowSize,_h:cvpdnSessionCurrentWindowSize,_i:cvpdnSessionMinimumWindowSize,_j:cvpdnSessionATOTimeouts,_k:cvpdnSessionOutGoingQueueSize,_l:cvpdnSessionCalculationType,_m:cvpdnSessionAdaptiveTimeOut,_n:cvpdnSessionRoundTripTime,_o:cvpdnSessionPktProcessingDelay,_p:cvpdnSessionZLBTime,'ciscoVpdnMgtExtMIBNotificationPrefix':ciscoVpdnMgtExtMIBNotificationPrefix,'ciscoVpdnMgmtExtMIBConformance':ciscoVpdnMgmtExtMIBConformance,'ciscoVpdnMgmtExtMIBCompliances':ciscoVpdnMgmtExtMIBCompliances,'ciscoVpdnMgmtExtMIBBasicCompliance':ciscoVpdnMgmtExtMIBBasicCompliance,'ciscoVpdnMgmtExtMIBBasicComplianceV2':ciscoVpdnMgmtExtMIBBasicComplianceV2,'ciscoVpdnMgmtExtMIBGroups':ciscoVpdnMgmtExtMIBGroups,_s:cvpdnTunnelExtGroup,_M:cvpdnSessionExtGroup,_t:cvpdnTunnelExtGroupV2})