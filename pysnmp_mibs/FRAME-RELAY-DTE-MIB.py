_A5='frTrapGroup0'
_A4='frErrGroup0'
_A3='frCircuitGroup0'
_A2='frPortGroup0'
_A1='frTrapGroup'
_A0='frErrGroup'
_z='frCircuitGroup'
_y='frPortGroup'
_x='frDLCIStatusChange'
_w='frErrFaultTime'
_v='frErrFaults'
_u='frTrapMaxRate'
_t='frCircuitRowStatus'
_s='frCircuitLogicalIfIndex'
_r='frCircuitSentDEs'
_q='frCircuitReceivedDEs'
_p='frCircuitDiscards'
_o='frCircuitType'
_n='frCircuitMulticast'
_m='frDlcmiRowStatus'
_l='frDlcmiStatus'
_k='read-write'
_j='OctetString'
_i='frNotificationGroup'
_h='frErrTime'
_g='frErrData'
_f='frErrType'
_e='frTrapState'
_d='frCircuitThroughput'
_c='frCircuitExcessBurst'
_b='frCircuitCommittedBurst'
_a='frCircuitLastTimeChange'
_Z='frCircuitCreationTime'
_Y='frCircuitReceivedOctets'
_X='frCircuitReceivedFrames'
_W='frCircuitSentOctets'
_V='frCircuitSentFrames'
_U='frCircuitReceivedBECNs'
_T='frCircuitReceivedFECNs'
_S='frDlcmiMulticast'
_R='frDlcmiMaxSupportedVCs'
_Q='frDlcmiMonitoredEvents'
_P='frDlcmiErrorThreshold'
_O='frDlcmiFullEnquiryInterval'
_N='frDlcmiPollingInterval'
_M='frDlcmiAddressLen'
_L='frDlcmiAddress'
_K='frDlcmiState'
_J='frCircuitState'
_I='frErrIfIndex'
_H='frCircuitDlci'
_G='frCircuitIfIndex'
_F='frDlcmiIfIndex'
_E='read-create'
_D='Integer32'
_C='read-only'
_B='current'
_A='FRAME-RELAY-DTE-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_j,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,transmission=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','transmission')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TimeStamp')
frameRelayDTE=ModuleIdentity((1,3,6,1,2,1,10,32))
if mibBuilder.loadTexts:frameRelayDTE.setRevisions(('1997-05-01 02:29','1992-04-01 00:00'))
class DLCI(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8388607))
_FrameRelayTraps_ObjectIdentity=ObjectIdentity
frameRelayTraps=_FrameRelayTraps_ObjectIdentity((1,3,6,1,2,1,10,32,0))
_FrDlcmiTable_Object=MibTable
frDlcmiTable=_FrDlcmiTable_Object((1,3,6,1,2,1,10,32,1))
if mibBuilder.loadTexts:frDlcmiTable.setStatus(_B)
_FrDlcmiEntry_Object=MibTableRow
frDlcmiEntry=_FrDlcmiEntry_Object((1,3,6,1,2,1,10,32,1,1))
frDlcmiEntry.setIndexNames((0,_A,_F))
if mibBuilder.loadTexts:frDlcmiEntry.setStatus(_B)
_FrDlcmiIfIndex_Type=InterfaceIndex
_FrDlcmiIfIndex_Object=MibTableColumn
frDlcmiIfIndex=_FrDlcmiIfIndex_Object((1,3,6,1,2,1,10,32,1,1,1),_FrDlcmiIfIndex_Type())
frDlcmiIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:frDlcmiIfIndex.setStatus(_B)
class _FrDlcmiState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('noLmiConfigured',1),('lmiRev1',2),('ansiT1617D',3),('ansiT1617B',4),('itut933A',5),('ansiT1617D1994',6)))
_FrDlcmiState_Type.__name__=_D
_FrDlcmiState_Object=MibTableColumn
frDlcmiState=_FrDlcmiState_Object((1,3,6,1,2,1,10,32,1,1,2),_FrDlcmiState_Type())
frDlcmiState.setMaxAccess(_E)
if mibBuilder.loadTexts:frDlcmiState.setStatus(_B)
class _FrDlcmiAddress_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('q921',1),('q922March90',2),('q922November90',3),('q922',4)))
_FrDlcmiAddress_Type.__name__=_D
_FrDlcmiAddress_Object=MibTableColumn
frDlcmiAddress=_FrDlcmiAddress_Object((1,3,6,1,2,1,10,32,1,1,3),_FrDlcmiAddress_Type())
frDlcmiAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:frDlcmiAddress.setStatus(_B)
class _FrDlcmiAddressLen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4)));namedValues=NamedValues(*(('twoOctets',2),('threeOctets',3),('fourOctets',4)))
_FrDlcmiAddressLen_Type.__name__=_D
_FrDlcmiAddressLen_Object=MibTableColumn
frDlcmiAddressLen=_FrDlcmiAddressLen_Object((1,3,6,1,2,1,10,32,1,1,4),_FrDlcmiAddressLen_Type())
frDlcmiAddressLen.setMaxAccess(_E)
if mibBuilder.loadTexts:frDlcmiAddressLen.setStatus(_B)
class _FrDlcmiPollingInterval_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,30))
_FrDlcmiPollingInterval_Type.__name__=_D
_FrDlcmiPollingInterval_Object=MibTableColumn
frDlcmiPollingInterval=_FrDlcmiPollingInterval_Object((1,3,6,1,2,1,10,32,1,1,5),_FrDlcmiPollingInterval_Type())
frDlcmiPollingInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:frDlcmiPollingInterval.setStatus(_B)
if mibBuilder.loadTexts:frDlcmiPollingInterval.setUnits('seconds')
class _FrDlcmiFullEnquiryInterval_Type(Integer32):defaultValue=6;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_FrDlcmiFullEnquiryInterval_Type.__name__=_D
_FrDlcmiFullEnquiryInterval_Object=MibTableColumn
frDlcmiFullEnquiryInterval=_FrDlcmiFullEnquiryInterval_Object((1,3,6,1,2,1,10,32,1,1,6),_FrDlcmiFullEnquiryInterval_Type())
frDlcmiFullEnquiryInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:frDlcmiFullEnquiryInterval.setStatus(_B)
class _FrDlcmiErrorThreshold_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_FrDlcmiErrorThreshold_Type.__name__=_D
_FrDlcmiErrorThreshold_Object=MibTableColumn
frDlcmiErrorThreshold=_FrDlcmiErrorThreshold_Object((1,3,6,1,2,1,10,32,1,1,7),_FrDlcmiErrorThreshold_Type())
frDlcmiErrorThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:frDlcmiErrorThreshold.setStatus(_B)
class _FrDlcmiMonitoredEvents_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_FrDlcmiMonitoredEvents_Type.__name__=_D
_FrDlcmiMonitoredEvents_Object=MibTableColumn
frDlcmiMonitoredEvents=_FrDlcmiMonitoredEvents_Object((1,3,6,1,2,1,10,32,1,1,8),_FrDlcmiMonitoredEvents_Type())
frDlcmiMonitoredEvents.setMaxAccess(_E)
if mibBuilder.loadTexts:frDlcmiMonitoredEvents.setStatus(_B)
_FrDlcmiMaxSupportedVCs_Type=DLCI
_FrDlcmiMaxSupportedVCs_Object=MibTableColumn
frDlcmiMaxSupportedVCs=_FrDlcmiMaxSupportedVCs_Object((1,3,6,1,2,1,10,32,1,1,9),_FrDlcmiMaxSupportedVCs_Type())
frDlcmiMaxSupportedVCs.setMaxAccess(_E)
if mibBuilder.loadTexts:frDlcmiMaxSupportedVCs.setStatus(_B)
class _FrDlcmiMulticast_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('nonBroadcast',1),('broadcast',2)))
_FrDlcmiMulticast_Type.__name__=_D
_FrDlcmiMulticast_Object=MibTableColumn
frDlcmiMulticast=_FrDlcmiMulticast_Object((1,3,6,1,2,1,10,32,1,1,10),_FrDlcmiMulticast_Type())
frDlcmiMulticast.setMaxAccess(_E)
if mibBuilder.loadTexts:frDlcmiMulticast.setStatus(_B)
class _FrDlcmiStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('running',1),('fault',2),('initializing',3)))
_FrDlcmiStatus_Type.__name__=_D
_FrDlcmiStatus_Object=MibTableColumn
frDlcmiStatus=_FrDlcmiStatus_Object((1,3,6,1,2,1,10,32,1,1,11),_FrDlcmiStatus_Type())
frDlcmiStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:frDlcmiStatus.setStatus(_B)
_FrDlcmiRowStatus_Type=RowStatus
_FrDlcmiRowStatus_Object=MibTableColumn
frDlcmiRowStatus=_FrDlcmiRowStatus_Object((1,3,6,1,2,1,10,32,1,1,12),_FrDlcmiRowStatus_Type())
frDlcmiRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:frDlcmiRowStatus.setStatus(_B)
_FrCircuitTable_Object=MibTable
frCircuitTable=_FrCircuitTable_Object((1,3,6,1,2,1,10,32,2))
if mibBuilder.loadTexts:frCircuitTable.setStatus(_B)
_FrCircuitEntry_Object=MibTableRow
frCircuitEntry=_FrCircuitEntry_Object((1,3,6,1,2,1,10,32,2,1))
frCircuitEntry.setIndexNames((0,_A,_G),(0,_A,_H))
if mibBuilder.loadTexts:frCircuitEntry.setStatus(_B)
_FrCircuitIfIndex_Type=InterfaceIndex
_FrCircuitIfIndex_Object=MibTableColumn
frCircuitIfIndex=_FrCircuitIfIndex_Object((1,3,6,1,2,1,10,32,2,1,1),_FrCircuitIfIndex_Type())
frCircuitIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:frCircuitIfIndex.setStatus(_B)
_FrCircuitDlci_Type=DLCI
_FrCircuitDlci_Object=MibTableColumn
frCircuitDlci=_FrCircuitDlci_Object((1,3,6,1,2,1,10,32,2,1,2),_FrCircuitDlci_Type())
frCircuitDlci.setMaxAccess(_C)
if mibBuilder.loadTexts:frCircuitDlci.setStatus(_B)
class _FrCircuitState_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('invalid',1),('active',2),('inactive',3)))
_FrCircuitState_Type.__name__=_D
_FrCircuitState_Object=MibTableColumn
frCircuitState=_FrCircuitState_Object((1,3,6,1,2,1,10,32,2,1,3),_FrCircuitState_Type())
frCircuitState.setMaxAccess(_E)
if mibBuilder.loadTexts:frCircuitState.setStatus(_B)
_FrCircuitReceivedFECNs_Type=Counter32
_FrCircuitReceivedFECNs_Object=MibTableColumn
frCircuitReceivedFECNs=_FrCircuitReceivedFECNs_Object((1,3,6,1,2,1,10,32,2,1,4),_FrCircuitReceivedFECNs_Type())
frCircuitReceivedFECNs.setMaxAccess(_C)
if mibBuilder.loadTexts:frCircuitReceivedFECNs.setStatus(_B)
_FrCircuitReceivedBECNs_Type=Counter32
_FrCircuitReceivedBECNs_Object=MibTableColumn
frCircuitReceivedBECNs=_FrCircuitReceivedBECNs_Object((1,3,6,1,2,1,10,32,2,1,5),_FrCircuitReceivedBECNs_Type())
frCircuitReceivedBECNs.setMaxAccess(_C)
if mibBuilder.loadTexts:frCircuitReceivedBECNs.setStatus(_B)
_FrCircuitSentFrames_Type=Counter32
_FrCircuitSentFrames_Object=MibTableColumn
frCircuitSentFrames=_FrCircuitSentFrames_Object((1,3,6,1,2,1,10,32,2,1,6),_FrCircuitSentFrames_Type())
frCircuitSentFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:frCircuitSentFrames.setStatus(_B)
_FrCircuitSentOctets_Type=Counter32
_FrCircuitSentOctets_Object=MibTableColumn
frCircuitSentOctets=_FrCircuitSentOctets_Object((1,3,6,1,2,1,10,32,2,1,7),_FrCircuitSentOctets_Type())
frCircuitSentOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:frCircuitSentOctets.setStatus(_B)
_FrCircuitReceivedFrames_Type=Counter32
_FrCircuitReceivedFrames_Object=MibTableColumn
frCircuitReceivedFrames=_FrCircuitReceivedFrames_Object((1,3,6,1,2,1,10,32,2,1,8),_FrCircuitReceivedFrames_Type())
frCircuitReceivedFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:frCircuitReceivedFrames.setStatus(_B)
_FrCircuitReceivedOctets_Type=Counter32
_FrCircuitReceivedOctets_Object=MibTableColumn
frCircuitReceivedOctets=_FrCircuitReceivedOctets_Object((1,3,6,1,2,1,10,32,2,1,9),_FrCircuitReceivedOctets_Type())
frCircuitReceivedOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:frCircuitReceivedOctets.setStatus(_B)
_FrCircuitCreationTime_Type=TimeStamp
_FrCircuitCreationTime_Object=MibTableColumn
frCircuitCreationTime=_FrCircuitCreationTime_Object((1,3,6,1,2,1,10,32,2,1,10),_FrCircuitCreationTime_Type())
frCircuitCreationTime.setMaxAccess(_C)
if mibBuilder.loadTexts:frCircuitCreationTime.setStatus(_B)
_FrCircuitLastTimeChange_Type=TimeStamp
_FrCircuitLastTimeChange_Object=MibTableColumn
frCircuitLastTimeChange=_FrCircuitLastTimeChange_Object((1,3,6,1,2,1,10,32,2,1,11),_FrCircuitLastTimeChange_Type())
frCircuitLastTimeChange.setMaxAccess(_C)
if mibBuilder.loadTexts:frCircuitLastTimeChange.setStatus(_B)
class _FrCircuitCommittedBurst_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_FrCircuitCommittedBurst_Type.__name__=_D
_FrCircuitCommittedBurst_Object=MibTableColumn
frCircuitCommittedBurst=_FrCircuitCommittedBurst_Object((1,3,6,1,2,1,10,32,2,1,12),_FrCircuitCommittedBurst_Type())
frCircuitCommittedBurst.setMaxAccess(_E)
if mibBuilder.loadTexts:frCircuitCommittedBurst.setStatus(_B)
class _FrCircuitExcessBurst_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_FrCircuitExcessBurst_Type.__name__=_D
_FrCircuitExcessBurst_Object=MibTableColumn
frCircuitExcessBurst=_FrCircuitExcessBurst_Object((1,3,6,1,2,1,10,32,2,1,13),_FrCircuitExcessBurst_Type())
frCircuitExcessBurst.setMaxAccess(_E)
if mibBuilder.loadTexts:frCircuitExcessBurst.setStatus(_B)
class _FrCircuitThroughput_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_FrCircuitThroughput_Type.__name__=_D
_FrCircuitThroughput_Object=MibTableColumn
frCircuitThroughput=_FrCircuitThroughput_Object((1,3,6,1,2,1,10,32,2,1,14),_FrCircuitThroughput_Type())
frCircuitThroughput.setMaxAccess(_E)
if mibBuilder.loadTexts:frCircuitThroughput.setStatus(_B)
class _FrCircuitMulticast_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('unicast',1),('oneWay',2),('twoWay',3),('nWay',4)))
_FrCircuitMulticast_Type.__name__=_D
_FrCircuitMulticast_Object=MibTableColumn
frCircuitMulticast=_FrCircuitMulticast_Object((1,3,6,1,2,1,10,32,2,1,15),_FrCircuitMulticast_Type())
frCircuitMulticast.setMaxAccess(_E)
if mibBuilder.loadTexts:frCircuitMulticast.setStatus(_B)
class _FrCircuitType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('static',1),('dynamic',2)))
_FrCircuitType_Type.__name__=_D
_FrCircuitType_Object=MibTableColumn
frCircuitType=_FrCircuitType_Object((1,3,6,1,2,1,10,32,2,1,16),_FrCircuitType_Type())
frCircuitType.setMaxAccess(_C)
if mibBuilder.loadTexts:frCircuitType.setStatus(_B)
_FrCircuitDiscards_Type=Counter32
_FrCircuitDiscards_Object=MibTableColumn
frCircuitDiscards=_FrCircuitDiscards_Object((1,3,6,1,2,1,10,32,2,1,17),_FrCircuitDiscards_Type())
frCircuitDiscards.setMaxAccess(_C)
if mibBuilder.loadTexts:frCircuitDiscards.setStatus(_B)
_FrCircuitReceivedDEs_Type=Counter32
_FrCircuitReceivedDEs_Object=MibTableColumn
frCircuitReceivedDEs=_FrCircuitReceivedDEs_Object((1,3,6,1,2,1,10,32,2,1,18),_FrCircuitReceivedDEs_Type())
frCircuitReceivedDEs.setMaxAccess(_C)
if mibBuilder.loadTexts:frCircuitReceivedDEs.setStatus(_B)
_FrCircuitSentDEs_Type=Counter32
_FrCircuitSentDEs_Object=MibTableColumn
frCircuitSentDEs=_FrCircuitSentDEs_Object((1,3,6,1,2,1,10,32,2,1,19),_FrCircuitSentDEs_Type())
frCircuitSentDEs.setMaxAccess(_C)
if mibBuilder.loadTexts:frCircuitSentDEs.setStatus(_B)
_FrCircuitLogicalIfIndex_Type=InterfaceIndex
_FrCircuitLogicalIfIndex_Object=MibTableColumn
frCircuitLogicalIfIndex=_FrCircuitLogicalIfIndex_Object((1,3,6,1,2,1,10,32,2,1,20),_FrCircuitLogicalIfIndex_Type())
frCircuitLogicalIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:frCircuitLogicalIfIndex.setStatus(_B)
_FrCircuitRowStatus_Type=RowStatus
_FrCircuitRowStatus_Object=MibTableColumn
frCircuitRowStatus=_FrCircuitRowStatus_Object((1,3,6,1,2,1,10,32,2,1,21),_FrCircuitRowStatus_Type())
frCircuitRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:frCircuitRowStatus.setStatus(_B)
_FrErrTable_Object=MibTable
frErrTable=_FrErrTable_Object((1,3,6,1,2,1,10,32,3))
if mibBuilder.loadTexts:frErrTable.setStatus(_B)
_FrErrEntry_Object=MibTableRow
frErrEntry=_FrErrEntry_Object((1,3,6,1,2,1,10,32,3,1))
frErrEntry.setIndexNames((0,_A,_I))
if mibBuilder.loadTexts:frErrEntry.setStatus(_B)
_FrErrIfIndex_Type=InterfaceIndex
_FrErrIfIndex_Object=MibTableColumn
frErrIfIndex=_FrErrIfIndex_Object((1,3,6,1,2,1,10,32,3,1,1),_FrErrIfIndex_Type())
frErrIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:frErrIfIndex.setStatus(_B)
class _FrErrType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('unknownError',1),('receiveShort',2),('receiveLong',3),('illegalAddress',4),('unknownAddress',5),('dlcmiProtoErr',6),('dlcmiUnknownIE',7),('dlcmiSequenceErr',8),('dlcmiUnknownRpt',9),('noErrorSinceReset',10)))
_FrErrType_Type.__name__=_D
_FrErrType_Object=MibTableColumn
frErrType=_FrErrType_Object((1,3,6,1,2,1,10,32,3,1,2),_FrErrType_Type())
frErrType.setMaxAccess(_C)
if mibBuilder.loadTexts:frErrType.setStatus(_B)
class _FrErrData_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1600))
_FrErrData_Type.__name__=_j
_FrErrData_Object=MibTableColumn
frErrData=_FrErrData_Object((1,3,6,1,2,1,10,32,3,1,3),_FrErrData_Type())
frErrData.setMaxAccess(_C)
if mibBuilder.loadTexts:frErrData.setStatus(_B)
_FrErrTime_Type=TimeStamp
_FrErrTime_Object=MibTableColumn
frErrTime=_FrErrTime_Object((1,3,6,1,2,1,10,32,3,1,4),_FrErrTime_Type())
frErrTime.setMaxAccess(_C)
if mibBuilder.loadTexts:frErrTime.setStatus(_B)
_FrErrFaults_Type=Counter32
_FrErrFaults_Object=MibTableColumn
frErrFaults=_FrErrFaults_Object((1,3,6,1,2,1,10,32,3,1,5),_FrErrFaults_Type())
frErrFaults.setMaxAccess(_C)
if mibBuilder.loadTexts:frErrFaults.setStatus(_B)
_FrErrFaultTime_Type=TimeStamp
_FrErrFaultTime_Object=MibTableColumn
frErrFaultTime=_FrErrFaultTime_Object((1,3,6,1,2,1,10,32,3,1,6),_FrErrFaultTime_Type())
frErrFaultTime.setMaxAccess(_C)
if mibBuilder.loadTexts:frErrFaultTime.setStatus(_B)
_FrameRelayTrapControl_ObjectIdentity=ObjectIdentity
frameRelayTrapControl=_FrameRelayTrapControl_ObjectIdentity((1,3,6,1,2,1,10,32,4))
class _FrTrapState_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_FrTrapState_Type.__name__=_D
_FrTrapState_Object=MibScalar
frTrapState=_FrTrapState_Object((1,3,6,1,2,1,10,32,4,1),_FrTrapState_Type())
frTrapState.setMaxAccess(_k)
if mibBuilder.loadTexts:frTrapState.setStatus(_B)
class _FrTrapMaxRate_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600000))
_FrTrapMaxRate_Type.__name__=_D
_FrTrapMaxRate_Object=MibScalar
frTrapMaxRate=_FrTrapMaxRate_Object((1,3,6,1,2,1,10,32,4,2),_FrTrapMaxRate_Type())
frTrapMaxRate.setMaxAccess(_k)
if mibBuilder.loadTexts:frTrapMaxRate.setStatus(_B)
_FrConformance_ObjectIdentity=ObjectIdentity
frConformance=_FrConformance_ObjectIdentity((1,3,6,1,2,1,10,32,6))
_FrGroups_ObjectIdentity=ObjectIdentity
frGroups=_FrGroups_ObjectIdentity((1,3,6,1,2,1,10,32,6,1))
_FrCompliances_ObjectIdentity=ObjectIdentity
frCompliances=_FrCompliances_ObjectIdentity((1,3,6,1,2,1,10,32,6,2))
frPortGroup=ObjectGroup((1,3,6,1,2,1,10,32,6,1,1))
frPortGroup.setObjects(*((_A,_F),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_l),(_A,_m)))
if mibBuilder.loadTexts:frPortGroup.setStatus(_B)
frCircuitGroup=ObjectGroup((1,3,6,1,2,1,10,32,6,1,2))
frCircuitGroup.setObjects(*((_A,_G),(_A,_H),(_A,_J),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t)))
if mibBuilder.loadTexts:frCircuitGroup.setStatus(_B)
frTrapGroup=ObjectGroup((1,3,6,1,2,1,10,32,6,1,3))
frTrapGroup.setObjects(*((_A,_e),(_A,_u)))
if mibBuilder.loadTexts:frTrapGroup.setStatus(_B)
frErrGroup=ObjectGroup((1,3,6,1,2,1,10,32,6,1,4))
frErrGroup.setObjects(*((_A,_I),(_A,_f),(_A,_g),(_A,_h),(_A,_v),(_A,_w)))
if mibBuilder.loadTexts:frErrGroup.setStatus(_B)
frPortGroup0=ObjectGroup((1,3,6,1,2,1,10,32,6,1,6))
frPortGroup0.setObjects(*((_A,_F),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S)))
if mibBuilder.loadTexts:frPortGroup0.setStatus(_B)
frCircuitGroup0=ObjectGroup((1,3,6,1,2,1,10,32,6,1,7))
frCircuitGroup0.setObjects(*((_A,_G),(_A,_H),(_A,_J),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d)))
if mibBuilder.loadTexts:frCircuitGroup0.setStatus(_B)
frErrGroup0=ObjectGroup((1,3,6,1,2,1,10,32,6,1,8))
frErrGroup0.setObjects(*((_A,_I),(_A,_f),(_A,_g),(_A,_h)))
if mibBuilder.loadTexts:frErrGroup0.setStatus(_B)
frTrapGroup0=ObjectGroup((1,3,6,1,2,1,10,32,6,1,9))
frTrapGroup0.setObjects((_A,_e))
if mibBuilder.loadTexts:frTrapGroup0.setStatus(_B)
frDLCIStatusChange=NotificationType((1,3,6,1,2,1,10,32,0,1))
frDLCIStatusChange.setObjects((_A,_J))
if mibBuilder.loadTexts:frDLCIStatusChange.setStatus(_B)
frNotificationGroup=NotificationGroup((1,3,6,1,2,1,10,32,6,1,5))
frNotificationGroup.setObjects((_A,_x))
if mibBuilder.loadTexts:frNotificationGroup.setStatus(_B)
frCompliance=ModuleCompliance((1,3,6,1,2,1,10,32,6,2,1))
frCompliance.setObjects(*((_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_i)))
if mibBuilder.loadTexts:frCompliance.setStatus(_B)
frCompliance0=ModuleCompliance((1,3,6,1,2,1,10,32,6,2,2))
frCompliance0.setObjects(*((_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_i)))
if mibBuilder.loadTexts:frCompliance0.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'DLCI':DLCI,'frameRelayDTE':frameRelayDTE,'frameRelayTraps':frameRelayTraps,_x:frDLCIStatusChange,'frDlcmiTable':frDlcmiTable,'frDlcmiEntry':frDlcmiEntry,_F:frDlcmiIfIndex,_K:frDlcmiState,_L:frDlcmiAddress,_M:frDlcmiAddressLen,_N:frDlcmiPollingInterval,_O:frDlcmiFullEnquiryInterval,_P:frDlcmiErrorThreshold,_Q:frDlcmiMonitoredEvents,_R:frDlcmiMaxSupportedVCs,_S:frDlcmiMulticast,_l:frDlcmiStatus,_m:frDlcmiRowStatus,'frCircuitTable':frCircuitTable,'frCircuitEntry':frCircuitEntry,_G:frCircuitIfIndex,_H:frCircuitDlci,_J:frCircuitState,_T:frCircuitReceivedFECNs,_U:frCircuitReceivedBECNs,_V:frCircuitSentFrames,_W:frCircuitSentOctets,_X:frCircuitReceivedFrames,_Y:frCircuitReceivedOctets,_Z:frCircuitCreationTime,_a:frCircuitLastTimeChange,_b:frCircuitCommittedBurst,_c:frCircuitExcessBurst,_d:frCircuitThroughput,_n:frCircuitMulticast,_o:frCircuitType,_p:frCircuitDiscards,_q:frCircuitReceivedDEs,_r:frCircuitSentDEs,_s:frCircuitLogicalIfIndex,_t:frCircuitRowStatus,'frErrTable':frErrTable,'frErrEntry':frErrEntry,_I:frErrIfIndex,_f:frErrType,_g:frErrData,_h:frErrTime,_v:frErrFaults,_w:frErrFaultTime,'frameRelayTrapControl':frameRelayTrapControl,_e:frTrapState,_u:frTrapMaxRate,'frConformance':frConformance,'frGroups':frGroups,_y:frPortGroup,_z:frCircuitGroup,_A1:frTrapGroup,_A0:frErrGroup,_i:frNotificationGroup,_A2:frPortGroup0,_A3:frCircuitGroup0,_A4:frErrGroup0,_A5:frTrapGroup0,'frCompliances':frCompliances,'frCompliance':frCompliance,'frCompliance0':frCompliance0})