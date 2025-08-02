_A1='avstrTrackerMonitoringGroup'
_A0='avstrRtrMonitoringGroup'
_z='avstrTrackerConfigGroup'
_y='avstrRtrConfigGroup'
_x='avstrTrackerPtrsValue'
_w='avstrTrackerPtrsType'
_v='avstrTrackerPtrsDescription'
_u='avstrTrackerOperStateLastChange'
_t='avstrTrackerListThresholdDown'
_s='avstrTrackerListThresholdUp'
_r='avstrTrackerListObjsReverseState'
_q='avstrTrackerListObjsRowStatus'
_p='avstrTrackerRowStatus'
_o='avstrTrackerListType'
_n='avstrTrackerRtrId'
_m='avstrTrackerType'
_l='avstrRtrOperStateLastChange'
_k='avstrRtrOperState'
_j='avstrRtrDestIp'
_i='avstrRtrRowStatus'
_h='avstrRtrProbeNextHopIp'
_g='avstrRtrIfKpaliveBypass'
_f='avstrRtrDestPort'
_e='avstrRtrSchedule'
_d='avstrRtrProbeNextHopMac'
_c='avstrRtrProbeNextHopIf'
_b='avstrRtrProbeSrcIpAddr'
_a='avstrRtrProbeDscp'
_Z='avstrRtrSuccessRetries'
_Y='avstrRtrFailRetries'
_X='avstrRtrWaitIntervalMs'
_W='avstrRtrFrequencyMs'
_V='avstrRtrType'
_U='avstrTrackerPtrsIndex'
_T='avstrTrackerPtrsTrackId'
_S='avstrTrackerListObjsChildTrackId'
_R='avstrTrackerListObjsParentTrackId'
_Q='avstrTrackerId'
_P='inactive'
_O='00000000'
_N='avstrRtrId'
_M='MacAddress'
_L='avstrTrackerOperState'
_K='avstrTrackerDescription'
_J='IpAddress'
_I='TruthValue'
_H='DisplayString'
_G='not-accessible'
_F='Unsigned32'
_E='read-only'
_D='Integer32'
_C='read-write'
_B='AVAYA-SAA-TRACK-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
avGatewayMibs,=mibBuilder.importSymbols('AVAYAGEN-MIB','avGatewayMibs')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,_J,'ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_H,_M,'PhysAddress','RowStatus','TextualConvention',_I)
avayaSaaTrackMib=ModuleIdentity((1,3,6,1,4,1,6889,2,6,2))
if mibBuilder.loadTexts:avayaSaaTrackMib.setRevisions(('2007-01-08 16:57',))
_AvstrMIBObjects_ObjectIdentity=ObjectIdentity
avstrMIBObjects=_AvstrMIBObjects_ObjectIdentity((1,3,6,1,4,1,6889,2,6,2,1))
_AvstrRtrMIBObjects_ObjectIdentity=ObjectIdentity
avstrRtrMIBObjects=_AvstrRtrMIBObjects_ObjectIdentity((1,3,6,1,4,1,6889,2,6,2,1,1))
_AvstrRtrTable_Object=MibTable
avstrRtrTable=_AvstrRtrTable_Object((1,3,6,1,4,1,6889,2,6,2,1,1,1))
if mibBuilder.loadTexts:avstrRtrTable.setStatus(_A)
_AvstrRtrEntry_Object=MibTableRow
avstrRtrEntry=_AvstrRtrEntry_Object((1,3,6,1,4,1,6889,2,6,2,1,1,1,1))
avstrRtrEntry.setIndexNames((0,_B,_N))
if mibBuilder.loadTexts:avstrRtrEntry.setStatus(_A)
_AvstrRtrId_Type=Unsigned32
_AvstrRtrId_Object=MibTableColumn
avstrRtrId=_AvstrRtrId_Object((1,3,6,1,4,1,6889,2,6,2,1,1,1,1,1),_AvstrRtrId_Type())
avstrRtrId.setMaxAccess(_G)
if mibBuilder.loadTexts:avstrRtrId.setStatus(_A)
class _AvstrRtrType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('ipIcmpEcho',2),('tcpConnect',3)))
_AvstrRtrType_Type.__name__=_D
_AvstrRtrType_Object=MibTableColumn
avstrRtrType=_AvstrRtrType_Object((1,3,6,1,4,1,6889,2,6,2,1,1,1,1,2),_AvstrRtrType_Type())
avstrRtrType.setMaxAccess(_C)
if mibBuilder.loadTexts:avstrRtrType.setStatus(_A)
_AvstrRtrDestIp_Type=IpAddress
_AvstrRtrDestIp_Object=MibTableColumn
avstrRtrDestIp=_AvstrRtrDestIp_Object((1,3,6,1,4,1,6889,2,6,2,1,1,1,1,3),_AvstrRtrDestIp_Type())
avstrRtrDestIp.setMaxAccess(_C)
if mibBuilder.loadTexts:avstrRtrDestIp.setStatus(_A)
class _AvstrRtrDestPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AvstrRtrDestPort_Type.__name__=_D
_AvstrRtrDestPort_Object=MibTableColumn
avstrRtrDestPort=_AvstrRtrDestPort_Object((1,3,6,1,4,1,6889,2,6,2,1,1,1,1,4),_AvstrRtrDestPort_Type())
avstrRtrDestPort.setMaxAccess(_C)
if mibBuilder.loadTexts:avstrRtrDestPort.setStatus(_A)
class _AvstrRtrFrequencyMs_Type(Unsigned32):defaultValue=5000
_AvstrRtrFrequencyMs_Type.__name__=_F
_AvstrRtrFrequencyMs_Object=MibTableColumn
avstrRtrFrequencyMs=_AvstrRtrFrequencyMs_Object((1,3,6,1,4,1,6889,2,6,2,1,1,1,1,5),_AvstrRtrFrequencyMs_Type())
avstrRtrFrequencyMs.setMaxAccess(_C)
if mibBuilder.loadTexts:avstrRtrFrequencyMs.setStatus(_A)
class _AvstrRtrWaitIntervalMs_Type(Unsigned32):defaultValue=5000
_AvstrRtrWaitIntervalMs_Type.__name__=_F
_AvstrRtrWaitIntervalMs_Object=MibTableColumn
avstrRtrWaitIntervalMs=_AvstrRtrWaitIntervalMs_Object((1,3,6,1,4,1,6889,2,6,2,1,1,1,1,6),_AvstrRtrWaitIntervalMs_Type())
avstrRtrWaitIntervalMs.setMaxAccess(_C)
if mibBuilder.loadTexts:avstrRtrWaitIntervalMs.setStatus(_A)
class _AvstrRtrFailRetries_Type(Unsigned32):defaultValue=5
_AvstrRtrFailRetries_Type.__name__=_F
_AvstrRtrFailRetries_Object=MibTableColumn
avstrRtrFailRetries=_AvstrRtrFailRetries_Object((1,3,6,1,4,1,6889,2,6,2,1,1,1,1,7),_AvstrRtrFailRetries_Type())
avstrRtrFailRetries.setMaxAccess(_C)
if mibBuilder.loadTexts:avstrRtrFailRetries.setStatus(_A)
class _AvstrRtrSuccessRetries_Type(Unsigned32):defaultValue=1
_AvstrRtrSuccessRetries_Type.__name__=_F
_AvstrRtrSuccessRetries_Object=MibTableColumn
avstrRtrSuccessRetries=_AvstrRtrSuccessRetries_Object((1,3,6,1,4,1,6889,2,6,2,1,1,1,1,8),_AvstrRtrSuccessRetries_Type())
avstrRtrSuccessRetries.setMaxAccess(_C)
if mibBuilder.loadTexts:avstrRtrSuccessRetries.setStatus(_A)
class _AvstrRtrProbeDscp_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_AvstrRtrProbeDscp_Type.__name__=_F
_AvstrRtrProbeDscp_Object=MibTableColumn
avstrRtrProbeDscp=_AvstrRtrProbeDscp_Object((1,3,6,1,4,1,6889,2,6,2,1,1,1,1,9),_AvstrRtrProbeDscp_Type())
avstrRtrProbeDscp.setMaxAccess(_C)
if mibBuilder.loadTexts:avstrRtrProbeDscp.setStatus(_A)
class _AvstrRtrProbeSrcIpAddr_Type(IpAddress):defaultHexValue=_O
_AvstrRtrProbeSrcIpAddr_Type.__name__=_J
_AvstrRtrProbeSrcIpAddr_Object=MibTableColumn
avstrRtrProbeSrcIpAddr=_AvstrRtrProbeSrcIpAddr_Object((1,3,6,1,4,1,6889,2,6,2,1,1,1,1,10),_AvstrRtrProbeSrcIpAddr_Type())
avstrRtrProbeSrcIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:avstrRtrProbeSrcIpAddr.setStatus(_A)
_AvstrRtrProbeNextHopIf_Type=InterfaceIndex
_AvstrRtrProbeNextHopIf_Object=MibTableColumn
avstrRtrProbeNextHopIf=_AvstrRtrProbeNextHopIf_Object((1,3,6,1,4,1,6889,2,6,2,1,1,1,1,11),_AvstrRtrProbeNextHopIf_Type())
avstrRtrProbeNextHopIf.setMaxAccess(_C)
if mibBuilder.loadTexts:avstrRtrProbeNextHopIf.setStatus(_A)
class _AvstrRtrProbeNextHopMac_Type(MacAddress):defaultHexValue='000000000000'
_AvstrRtrProbeNextHopMac_Type.__name__=_M
_AvstrRtrProbeNextHopMac_Object=MibTableColumn
avstrRtrProbeNextHopMac=_AvstrRtrProbeNextHopMac_Object((1,3,6,1,4,1,6889,2,6,2,1,1,1,1,12),_AvstrRtrProbeNextHopMac_Type())
avstrRtrProbeNextHopMac.setMaxAccess(_C)
if mibBuilder.loadTexts:avstrRtrProbeNextHopMac.setStatus(_A)
class _AvstrRtrSchedule_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),('active',2)))
_AvstrRtrSchedule_Type.__name__=_D
_AvstrRtrSchedule_Object=MibTableColumn
avstrRtrSchedule=_AvstrRtrSchedule_Object((1,3,6,1,4,1,6889,2,6,2,1,1,1,1,13),_AvstrRtrSchedule_Type())
avstrRtrSchedule.setMaxAccess(_C)
if mibBuilder.loadTexts:avstrRtrSchedule.setStatus(_A)
class _AvstrRtrOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_P,1),('up',2),('down',3)))
_AvstrRtrOperState_Type.__name__=_D
_AvstrRtrOperState_Object=MibTableColumn
avstrRtrOperState=_AvstrRtrOperState_Object((1,3,6,1,4,1,6889,2,6,2,1,1,1,1,14),_AvstrRtrOperState_Type())
avstrRtrOperState.setMaxAccess(_E)
if mibBuilder.loadTexts:avstrRtrOperState.setStatus(_A)
_AvstrRtrOperStateLastChange_Type=TimeTicks
_AvstrRtrOperStateLastChange_Object=MibTableColumn
avstrRtrOperStateLastChange=_AvstrRtrOperStateLastChange_Object((1,3,6,1,4,1,6889,2,6,2,1,1,1,1,15),_AvstrRtrOperStateLastChange_Type())
avstrRtrOperStateLastChange.setMaxAccess(_E)
if mibBuilder.loadTexts:avstrRtrOperStateLastChange.setStatus(_A)
_AvstrRtrRowStatus_Type=RowStatus
_AvstrRtrRowStatus_Object=MibTableColumn
avstrRtrRowStatus=_AvstrRtrRowStatus_Object((1,3,6,1,4,1,6889,2,6,2,1,1,1,1,16),_AvstrRtrRowStatus_Type())
avstrRtrRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:avstrRtrRowStatus.setStatus(_A)
class _AvstrRtrProbeNextHopIp_Type(IpAddress):defaultHexValue=_O
_AvstrRtrProbeNextHopIp_Type.__name__=_J
_AvstrRtrProbeNextHopIp_Object=MibTableColumn
avstrRtrProbeNextHopIp=_AvstrRtrProbeNextHopIp_Object((1,3,6,1,4,1,6889,2,6,2,1,1,1,1,17),_AvstrRtrProbeNextHopIp_Type())
avstrRtrProbeNextHopIp.setMaxAccess(_C)
if mibBuilder.loadTexts:avstrRtrProbeNextHopIp.setStatus(_A)
class _AvstrRtrIfKpaliveBypass_Type(TruthValue):defaultValue=2
_AvstrRtrIfKpaliveBypass_Type.__name__=_I
_AvstrRtrIfKpaliveBypass_Object=MibTableColumn
avstrRtrIfKpaliveBypass=_AvstrRtrIfKpaliveBypass_Object((1,3,6,1,4,1,6889,2,6,2,1,1,1,1,18),_AvstrRtrIfKpaliveBypass_Type())
avstrRtrIfKpaliveBypass.setMaxAccess(_C)
if mibBuilder.loadTexts:avstrRtrIfKpaliveBypass.setStatus(_A)
class _AvstrRtrDestHostName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_AvstrRtrDestHostName_Type.__name__=_H
_AvstrRtrDestHostName_Object=MibTableColumn
avstrRtrDestHostName=_AvstrRtrDestHostName_Object((1,3,6,1,4,1,6889,2,6,2,1,1,1,1,19),_AvstrRtrDestHostName_Type())
avstrRtrDestHostName.setMaxAccess(_C)
if mibBuilder.loadTexts:avstrRtrDestHostName.setStatus(_A)
_AvstrRtrResolvedIp_Type=IpAddress
_AvstrRtrResolvedIp_Object=MibTableColumn
avstrRtrResolvedIp=_AvstrRtrResolvedIp_Object((1,3,6,1,4,1,6889,2,6,2,1,1,1,1,20),_AvstrRtrResolvedIp_Type())
avstrRtrResolvedIp.setMaxAccess(_E)
if mibBuilder.loadTexts:avstrRtrResolvedIp.setStatus(_A)
_AvstrTrackerMIBObjects_ObjectIdentity=ObjectIdentity
avstrTrackerMIBObjects=_AvstrTrackerMIBObjects_ObjectIdentity((1,3,6,1,4,1,6889,2,6,2,1,2))
_AvstrTrackerTable_Object=MibTable
avstrTrackerTable=_AvstrTrackerTable_Object((1,3,6,1,4,1,6889,2,6,2,1,2,1))
if mibBuilder.loadTexts:avstrTrackerTable.setStatus(_A)
_AvstrTrackerEntry_Object=MibTableRow
avstrTrackerEntry=_AvstrTrackerEntry_Object((1,3,6,1,4,1,6889,2,6,2,1,2,1,1))
avstrTrackerEntry.setIndexNames((0,_B,_Q))
if mibBuilder.loadTexts:avstrTrackerEntry.setStatus(_A)
_AvstrTrackerId_Type=Unsigned32
_AvstrTrackerId_Object=MibTableColumn
avstrTrackerId=_AvstrTrackerId_Object((1,3,6,1,4,1,6889,2,6,2,1,2,1,1,1),_AvstrTrackerId_Type())
avstrTrackerId.setMaxAccess(_G)
if mibBuilder.loadTexts:avstrTrackerId.setStatus(_A)
class _AvstrTrackerDescription_Type(DisplayString):defaultHexValue=''
_AvstrTrackerDescription_Type.__name__=_H
_AvstrTrackerDescription_Object=MibTableColumn
avstrTrackerDescription=_AvstrTrackerDescription_Object((1,3,6,1,4,1,6889,2,6,2,1,2,1,1,2),_AvstrTrackerDescription_Type())
avstrTrackerDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:avstrTrackerDescription.setStatus(_A)
class _AvstrTrackerType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('list',1),('rtr',2)))
_AvstrTrackerType_Type.__name__=_D
_AvstrTrackerType_Object=MibTableColumn
avstrTrackerType=_AvstrTrackerType_Object((1,3,6,1,4,1,6889,2,6,2,1,2,1,1,3),_AvstrTrackerType_Type())
avstrTrackerType.setMaxAccess(_C)
if mibBuilder.loadTexts:avstrTrackerType.setStatus(_A)
_AvstrTrackerRtrId_Type=Unsigned32
_AvstrTrackerRtrId_Object=MibTableColumn
avstrTrackerRtrId=_AvstrTrackerRtrId_Object((1,3,6,1,4,1,6889,2,6,2,1,2,1,1,4),_AvstrTrackerRtrId_Type())
avstrTrackerRtrId.setMaxAccess(_C)
if mibBuilder.loadTexts:avstrTrackerRtrId.setStatus(_A)
class _AvstrTrackerListType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('boolAnd',1),('boolOr',2),('threshCount',3)))
_AvstrTrackerListType_Type.__name__=_D
_AvstrTrackerListType_Object=MibTableColumn
avstrTrackerListType=_AvstrTrackerListType_Object((1,3,6,1,4,1,6889,2,6,2,1,2,1,1,5),_AvstrTrackerListType_Type())
avstrTrackerListType.setMaxAccess(_C)
if mibBuilder.loadTexts:avstrTrackerListType.setStatus(_A)
_AvstrTrackerListThresholdUp_Type=Unsigned32
_AvstrTrackerListThresholdUp_Object=MibTableColumn
avstrTrackerListThresholdUp=_AvstrTrackerListThresholdUp_Object((1,3,6,1,4,1,6889,2,6,2,1,2,1,1,6),_AvstrTrackerListThresholdUp_Type())
avstrTrackerListThresholdUp.setMaxAccess(_C)
if mibBuilder.loadTexts:avstrTrackerListThresholdUp.setStatus(_A)
_AvstrTrackerListThresholdDown_Type=Unsigned32
_AvstrTrackerListThresholdDown_Object=MibTableColumn
avstrTrackerListThresholdDown=_AvstrTrackerListThresholdDown_Object((1,3,6,1,4,1,6889,2,6,2,1,2,1,1,7),_AvstrTrackerListThresholdDown_Type())
avstrTrackerListThresholdDown.setMaxAccess(_C)
if mibBuilder.loadTexts:avstrTrackerListThresholdDown.setStatus(_A)
class _AvstrTrackerOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('reserved',1),('up',2),('down',3)))
_AvstrTrackerOperState_Type.__name__=_D
_AvstrTrackerOperState_Object=MibTableColumn
avstrTrackerOperState=_AvstrTrackerOperState_Object((1,3,6,1,4,1,6889,2,6,2,1,2,1,1,8),_AvstrTrackerOperState_Type())
avstrTrackerOperState.setMaxAccess(_E)
if mibBuilder.loadTexts:avstrTrackerOperState.setStatus(_A)
_AvstrTrackerOperStateLastChange_Type=TimeTicks
_AvstrTrackerOperStateLastChange_Object=MibTableColumn
avstrTrackerOperStateLastChange=_AvstrTrackerOperStateLastChange_Object((1,3,6,1,4,1,6889,2,6,2,1,2,1,1,9),_AvstrTrackerOperStateLastChange_Type())
avstrTrackerOperStateLastChange.setMaxAccess(_E)
if mibBuilder.loadTexts:avstrTrackerOperStateLastChange.setStatus(_A)
_AvstrTrackerRowStatus_Type=RowStatus
_AvstrTrackerRowStatus_Object=MibTableColumn
avstrTrackerRowStatus=_AvstrTrackerRowStatus_Object((1,3,6,1,4,1,6889,2,6,2,1,2,1,1,10),_AvstrTrackerRowStatus_Type())
avstrTrackerRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:avstrTrackerRowStatus.setStatus(_A)
class _AvstrTrackerPermanentTrackState_Type(TruthValue):defaultValue=2
_AvstrTrackerPermanentTrackState_Type.__name__=_I
_AvstrTrackerPermanentTrackState_Object=MibTableColumn
avstrTrackerPermanentTrackState=_AvstrTrackerPermanentTrackState_Object((1,3,6,1,4,1,6889,2,6,2,1,2,1,1,11),_AvstrTrackerPermanentTrackState_Type())
avstrTrackerPermanentTrackState.setMaxAccess(_C)
if mibBuilder.loadTexts:avstrTrackerPermanentTrackState.setStatus(_A)
_AvstrTrackerListObjsTable_Object=MibTable
avstrTrackerListObjsTable=_AvstrTrackerListObjsTable_Object((1,3,6,1,4,1,6889,2,6,2,1,2,2))
if mibBuilder.loadTexts:avstrTrackerListObjsTable.setStatus(_A)
_AvstrTrackerListObjsEntry_Object=MibTableRow
avstrTrackerListObjsEntry=_AvstrTrackerListObjsEntry_Object((1,3,6,1,4,1,6889,2,6,2,1,2,2,1))
avstrTrackerListObjsEntry.setIndexNames((0,_B,_R),(0,_B,_S))
if mibBuilder.loadTexts:avstrTrackerListObjsEntry.setStatus(_A)
_AvstrTrackerListObjsParentTrackId_Type=Unsigned32
_AvstrTrackerListObjsParentTrackId_Object=MibTableColumn
avstrTrackerListObjsParentTrackId=_AvstrTrackerListObjsParentTrackId_Object((1,3,6,1,4,1,6889,2,6,2,1,2,2,1,1),_AvstrTrackerListObjsParentTrackId_Type())
avstrTrackerListObjsParentTrackId.setMaxAccess(_G)
if mibBuilder.loadTexts:avstrTrackerListObjsParentTrackId.setStatus(_A)
_AvstrTrackerListObjsChildTrackId_Type=Unsigned32
_AvstrTrackerListObjsChildTrackId_Object=MibTableColumn
avstrTrackerListObjsChildTrackId=_AvstrTrackerListObjsChildTrackId_Object((1,3,6,1,4,1,6889,2,6,2,1,2,2,1,2),_AvstrTrackerListObjsChildTrackId_Type())
avstrTrackerListObjsChildTrackId.setMaxAccess(_G)
if mibBuilder.loadTexts:avstrTrackerListObjsChildTrackId.setStatus(_A)
_AvstrTrackerListObjsRowStatus_Type=RowStatus
_AvstrTrackerListObjsRowStatus_Object=MibTableColumn
avstrTrackerListObjsRowStatus=_AvstrTrackerListObjsRowStatus_Object((1,3,6,1,4,1,6889,2,6,2,1,2,2,1,3),_AvstrTrackerListObjsRowStatus_Type())
avstrTrackerListObjsRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:avstrTrackerListObjsRowStatus.setStatus(_A)
class _AvstrTrackerListObjsReverseState_Type(TruthValue):defaultValue=2
_AvstrTrackerListObjsReverseState_Type.__name__=_I
_AvstrTrackerListObjsReverseState_Object=MibTableColumn
avstrTrackerListObjsReverseState=_AvstrTrackerListObjsReverseState_Object((1,3,6,1,4,1,6889,2,6,2,1,2,2,1,4),_AvstrTrackerListObjsReverseState_Type())
avstrTrackerListObjsReverseState.setMaxAccess(_C)
if mibBuilder.loadTexts:avstrTrackerListObjsReverseState.setStatus(_A)
_AvstrTrackerPtrsTable_Object=MibTable
avstrTrackerPtrsTable=_AvstrTrackerPtrsTable_Object((1,3,6,1,4,1,6889,2,6,2,1,2,3))
if mibBuilder.loadTexts:avstrTrackerPtrsTable.setStatus(_A)
_AvstrTrackerPtrsEntry_Object=MibTableRow
avstrTrackerPtrsEntry=_AvstrTrackerPtrsEntry_Object((1,3,6,1,4,1,6889,2,6,2,1,2,3,1))
avstrTrackerPtrsEntry.setIndexNames((0,_B,_T),(0,_B,_U))
if mibBuilder.loadTexts:avstrTrackerPtrsEntry.setStatus(_A)
_AvstrTrackerPtrsTrackId_Type=Unsigned32
_AvstrTrackerPtrsTrackId_Object=MibTableColumn
avstrTrackerPtrsTrackId=_AvstrTrackerPtrsTrackId_Object((1,3,6,1,4,1,6889,2,6,2,1,2,3,1,1),_AvstrTrackerPtrsTrackId_Type())
avstrTrackerPtrsTrackId.setMaxAccess(_G)
if mibBuilder.loadTexts:avstrTrackerPtrsTrackId.setStatus(_A)
_AvstrTrackerPtrsIndex_Type=Unsigned32
_AvstrTrackerPtrsIndex_Object=MibTableColumn
avstrTrackerPtrsIndex=_AvstrTrackerPtrsIndex_Object((1,3,6,1,4,1,6889,2,6,2,1,2,3,1,2),_AvstrTrackerPtrsIndex_Type())
avstrTrackerPtrsIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:avstrTrackerPtrsIndex.setStatus(_A)
class _AvstrTrackerPtrsDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_AvstrTrackerPtrsDescription_Type.__name__=_H
_AvstrTrackerPtrsDescription_Object=MibTableColumn
avstrTrackerPtrsDescription=_AvstrTrackerPtrsDescription_Object((1,3,6,1,4,1,6889,2,6,2,1,2,3,1,3),_AvstrTrackerPtrsDescription_Type())
avstrTrackerPtrsDescription.setMaxAccess(_E)
if mibBuilder.loadTexts:avstrTrackerPtrsDescription.setStatus(_A)
class _AvstrTrackerPtrsType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('none',1),('trackerList',2),('ifIndex',3),('isakmpPeer',4),('ipStaticRoute',5),('ipPbrNhListEntry',6)))
_AvstrTrackerPtrsType_Type.__name__=_D
_AvstrTrackerPtrsType_Object=MibTableColumn
avstrTrackerPtrsType=_AvstrTrackerPtrsType_Object((1,3,6,1,4,1,6889,2,6,2,1,2,3,1,4),_AvstrTrackerPtrsType_Type())
avstrTrackerPtrsType.setMaxAccess(_E)
if mibBuilder.loadTexts:avstrTrackerPtrsType.setStatus(_A)
_AvstrTrackerPtrsValue_Type=OctetString
_AvstrTrackerPtrsValue_Object=MibTableColumn
avstrTrackerPtrsValue=_AvstrTrackerPtrsValue_Object((1,3,6,1,4,1,6889,2,6,2,1,2,3,1,5),_AvstrTrackerPtrsValue_Type())
avstrTrackerPtrsValue.setMaxAccess(_E)
if mibBuilder.loadTexts:avstrTrackerPtrsValue.setStatus(_A)
_AvstrMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
avstrMIBNotificationPrefix=_AvstrMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,6889,2,6,2,2))
_AvstrMIBNotifications_ObjectIdentity=ObjectIdentity
avstrMIBNotifications=_AvstrMIBNotifications_ObjectIdentity((1,3,6,1,4,1,6889,2,6,2,2,0))
_AvstrMIBConformance_ObjectIdentity=ObjectIdentity
avstrMIBConformance=_AvstrMIBConformance_ObjectIdentity((1,3,6,1,4,1,6889,2,6,2,3))
_AvstrMIBGroups_ObjectIdentity=ObjectIdentity
avstrMIBGroups=_AvstrMIBGroups_ObjectIdentity((1,3,6,1,4,1,6889,2,6,2,3,1))
_AvstrMIBCompliances_ObjectIdentity=ObjectIdentity
avstrMIBCompliances=_AvstrMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6889,2,6,2,3,2))
avstrRtrConfigGroup=ObjectGroup((1,3,6,1,4,1,6889,2,6,2,3,1,1))
avstrRtrConfigGroup.setObjects(*((_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j)))
if mibBuilder.loadTexts:avstrRtrConfigGroup.setStatus(_A)
avstrRtrMonitoringGroup=ObjectGroup((1,3,6,1,4,1,6889,2,6,2,3,1,2))
avstrRtrMonitoringGroup.setObjects(*((_B,_k),(_B,_l)))
if mibBuilder.loadTexts:avstrRtrMonitoringGroup.setStatus(_A)
avstrTrackerConfigGroup=ObjectGroup((1,3,6,1,4,1,6889,2,6,2,3,1,3))
avstrTrackerConfigGroup.setObjects(*((_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_K),(_B,_t)))
if mibBuilder.loadTexts:avstrTrackerConfigGroup.setStatus(_A)
avstrTrackerMonitoringGroup=ObjectGroup((1,3,6,1,4,1,6889,2,6,2,3,1,4))
avstrTrackerMonitoringGroup.setObjects(*((_B,_L),(_B,_u),(_B,_v),(_B,_w),(_B,_x)))
if mibBuilder.loadTexts:avstrTrackerMonitoringGroup.setStatus(_A)
avstrTrackerOperStateChangeNotification=NotificationType((1,3,6,1,4,1,6889,2,6,2,2,0,1))
avstrTrackerOperStateChangeNotification.setObjects(*((_B,_L),(_B,_K)))
if mibBuilder.loadTexts:avstrTrackerOperStateChangeNotification.setStatus(_A)
avstrMIBCompliance=ModuleCompliance((1,3,6,1,4,1,6889,2,6,2,3,2,1))
avstrMIBCompliance.setObjects(*((_B,_y),(_B,_z),(_B,_A0),(_B,_A1)))
if mibBuilder.loadTexts:avstrMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'avayaSaaTrackMib':avayaSaaTrackMib,'avstrMIBObjects':avstrMIBObjects,'avstrRtrMIBObjects':avstrRtrMIBObjects,'avstrRtrTable':avstrRtrTable,'avstrRtrEntry':avstrRtrEntry,_N:avstrRtrId,_V:avstrRtrType,_j:avstrRtrDestIp,_f:avstrRtrDestPort,_W:avstrRtrFrequencyMs,_X:avstrRtrWaitIntervalMs,_Y:avstrRtrFailRetries,_Z:avstrRtrSuccessRetries,_a:avstrRtrProbeDscp,_b:avstrRtrProbeSrcIpAddr,_c:avstrRtrProbeNextHopIf,_d:avstrRtrProbeNextHopMac,_e:avstrRtrSchedule,_k:avstrRtrOperState,_l:avstrRtrOperStateLastChange,_i:avstrRtrRowStatus,_h:avstrRtrProbeNextHopIp,_g:avstrRtrIfKpaliveBypass,'avstrRtrDestHostName':avstrRtrDestHostName,'avstrRtrResolvedIp':avstrRtrResolvedIp,'avstrTrackerMIBObjects':avstrTrackerMIBObjects,'avstrTrackerTable':avstrTrackerTable,'avstrTrackerEntry':avstrTrackerEntry,_Q:avstrTrackerId,_K:avstrTrackerDescription,_m:avstrTrackerType,_n:avstrTrackerRtrId,_o:avstrTrackerListType,_s:avstrTrackerListThresholdUp,_t:avstrTrackerListThresholdDown,_L:avstrTrackerOperState,_u:avstrTrackerOperStateLastChange,_p:avstrTrackerRowStatus,'avstrTrackerPermanentTrackState':avstrTrackerPermanentTrackState,'avstrTrackerListObjsTable':avstrTrackerListObjsTable,'avstrTrackerListObjsEntry':avstrTrackerListObjsEntry,_R:avstrTrackerListObjsParentTrackId,_S:avstrTrackerListObjsChildTrackId,_q:avstrTrackerListObjsRowStatus,_r:avstrTrackerListObjsReverseState,'avstrTrackerPtrsTable':avstrTrackerPtrsTable,'avstrTrackerPtrsEntry':avstrTrackerPtrsEntry,_T:avstrTrackerPtrsTrackId,_U:avstrTrackerPtrsIndex,_v:avstrTrackerPtrsDescription,_w:avstrTrackerPtrsType,_x:avstrTrackerPtrsValue,'avstrMIBNotificationPrefix':avstrMIBNotificationPrefix,'avstrMIBNotifications':avstrMIBNotifications,'avstrTrackerOperStateChangeNotification':avstrTrackerOperStateChangeNotification,'avstrMIBConformance':avstrMIBConformance,'avstrMIBGroups':avstrMIBGroups,_y:avstrRtrConfigGroup,_A0:avstrRtrMonitoringGroup,_z:avstrTrackerConfigGroup,_A1:avstrTrackerMonitoringGroup,'avstrMIBCompliances':avstrMIBCompliances,'avstrMIBCompliance':avstrMIBCompliance})