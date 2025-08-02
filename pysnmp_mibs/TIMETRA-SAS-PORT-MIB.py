_Al='aluExtPethPsePortOperStatus'
_Ak='aluExtPethPsePortFaultReason'
_Aj='tmnxPortEtherNwAggRateLimit'
_Ai='tmnxPortLldpTnlNrstBrdgeDstMac'
_Ah='tmnxPortAccEgrSapQosMarking'
_Ag='tmnxPortLoopbckDstMacAddr'
_Af='tmnxPortLoopbckSrcMacAddr'
_Ae='tmnxPortLoopbckSapEncapVal'
_Ad='tmnxPortLoopbckSapPortId'
_Ac='tmnxPortLoopbckServId'
_Ab='tmnxPortEtherIpMTU'
_Aa='aluIntervalFreqOffsetStdDevPpb'
_AZ='aluIntervalFreqOffsetMeanPpb'
_AY='aluIntervalPhaseErrorMeanNs'
_AX='aluIntervalPhaseErrorStdDevNs'
_AW='aluIntervalPhaseErrorMeanPpb'
_AV='aluIntervalUpdateTime'
_AU='aluIntervalValidData'
_AT='aluCurrent1MinFreqOffsetStdDevPpb'
_AS='aluCurrent1MinFreqOffsetMeanPpb'
_AR='aluCurrent1MinPhaseErrorMeanNs'
_AQ='aluCurrent1MinPhaseErrorStdDevNs'
_AP='aluCurrent1MinPhaseErrorMeanPpb'
_AO='aluCurrent1MinValidData'
_AN='aluTotalShortIntervalMinutes'
_AM='aluMaxShortIntervalMinutes'
_AL='aluCurrent24HourFreqOffsetStdDevPpb'
_AK='aluCurrent24HourFreqOffsetMeanPpb'
_AJ='aluTotalMinutesIn24Hour'
_AI='aluLastUpdateTime'
_AH='tmnxPortEtherEgrSchedMode'
_AG='aluExtDS1PortLineImpedance'
_AF='tmnxPortEtherLoopback'
_AE='tmnxPortStatsQueue8PktsFwd'
_AD='tmnxPortStatsQueue7PktsFwd'
_AC='tmnxPortStatsQueue6PktsFwd'
_AB='tmnxPortStatsQueue5PktsFwd'
_AA='tmnxPortStatsQueue4PktsFwd'
_A9='tmnxPortStatsQueue3PktsFwd'
_A8='tmnxPortStatsQueue2PktsFwd'
_A7='tmnxPortStatsQueue1PktsFwd'
_A6='tmnxPortEtherEgressMaxBurst'
_A5='tmnxSASPortNetIngressFwdOutProfOcts'
_A4='tmnxSASPortNetIngressFwdInProfOcts'
_A3='tmnxSASPortNetIngressFwdOutProfPkts'
_A2='tmnxSASPortNetIngressFwdInProfPkts'
_A1='portShgLastMgmtChange'
_A0='portShgDescription'
_z='portShgInstanceId'
_y='portShgRowStatus'
_x='tmnxPortShgName'
_w='tmnxPortNetworkQoSPolicyId'
_v='tmnxPortAccessEgressQoSPolicyId'
_u='tmnxPortUplinkMode'
_t='aluExtPethPsePortEntry'
_s='aluExtTmnxDS1Entry'
_r='aluExtTmnxDS1PortEntry'
_q='sasTmnxPortEtherExtnEntry'
_p='sasTmnxPortExtnEntry'
_o='tmnxVirtualPortPortID'
_n='tmnxPortNetEgressQueueStatsIndex'
_m='tmnxPortAccessEgressQueueStatsIndex'
_l='read-create'
_k='portShgName'
_j='tmnxSASPortNetIngressMeterIndex'
_i='ServObjDesc'
_h='tmnxPortNotifyPortId'
_g='pethPsePortPowerClassifications'
_f='pethPsePortDetectionStatus'
_e='OctetString'
_d='tmnxPortEtherClockConfig'
_c='tmnxPortNetEgressQueueStatsOutProfDroOcts'
_b='tmnxPortNetEgressQueueStatsOutProfDroPkts'
_a='tmnxPortNetEgressQueueStatsInProfDroOcts'
_Z='tmnxPortNetEgressQueueStatsInProfDroPkts'
_Y='tmnxPortNetEgressQueueStatsDroOcts'
_X='tmnxPortNetEgressQueueStatsDroPkts'
_W='tmnxPortNetEgressQueueStatsFwdOcts'
_V='tmnxPortNetEgressQueueStatsFwdPkts'
_U='tmnxPortAccessEgressQueueStatsDroOcts'
_T='tmnxPortAccessEgressQueueStatsDroPkts'
_S='tmnxPortAccessEgressQueueStatsFwdOcts'
_R='tmnxPortAccessEgressQueueStatsFwdPkts'
_Q='aluIntervalNumber'
_P='notApplicable'
_O='none'
_N='TQueueId'
_M='POWER-ETHERNET-MIB'
_L='TruthValue'
_K='Unsigned32'
_J='not-accessible'
_I='tmnxPortPortID'
_H='TIMETRA-PORT-MIB'
_G='tmnxChassisIndex'
_F='TIMETRA-CHASSIS-MIB'
_E='Integer32'
_D='read-write'
_C='read-only'
_B='TIMETRA-SAS-PORT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_e,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
pethPsePortDetectionStatus,pethPsePortEntry,pethPsePortIndex,pethPsePortPowerClassifications=mibBuilder.importSymbols(_M,_f,'pethPsePortEntry','pethPsePortIndex',_g)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_K,'iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowPointer,RowStatus,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowPointer','RowStatus','TextualConvention','TimeInterval','TimeStamp',_L)
TmnxAlarmState,TmnxMDAChanType,TmnxPortAdminStatus,tmnxChassisIndex,tmnxChassisNotifyChassisId,tmnxHwConformance,tmnxHwNotification,tmnxHwObjs=mibBuilder.importSymbols(_F,'TmnxAlarmState','TmnxMDAChanType','TmnxPortAdminStatus',_G,'tmnxChassisNotifyChassisId','tmnxHwConformance','tmnxHwNotification','tmnxHwObjs')
timetraSRMIBModules,=mibBuilder.importSymbols('TIMETRA-GLOBAL-MIB','timetraSRMIBModules')
tmnxDS1Entry,tmnxDS1PortEntry,tmnxPortEntry,tmnxPortEtherEntry,tmnxPortNotifyPortId,tmnxPortPortID=mibBuilder.importSymbols(_H,'tmnxDS1Entry','tmnxDS1PortEntry','tmnxPortEntry','tmnxPortEtherEntry',_h,_I)
timetraSASConfs,timetraSASModules,timetraSASNotifyPrefix,timetraSASObjs=mibBuilder.importSymbols('TIMETRA-SAS-GLOBAL-MIB','timetraSASConfs','timetraSASModules','timetraSASNotifyPrefix','timetraSASObjs')
ServObjDesc,=mibBuilder.importSymbols('TIMETRA-SERV-MIB',_i)
TFCName,TItemDescription,TItemLongDescription,TNamedItem,TNamedItemOrEmpty,TNetworkIngressMeterId,TPortSchedulerCIR,TPortSchedulerPIR,TQueueId,TmnxActionType,TmnxEncapVal,TmnxOperState,TmnxPortID,TmnxServId=mibBuilder.importSymbols('TN-TC-MIB','TFCName','TItemDescription','TItemLongDescription','TNamedItem','TNamedItemOrEmpty','TNetworkIngressMeterId','TPortSchedulerCIR','TPortSchedulerPIR',_N,'TmnxActionType','TmnxEncapVal','TmnxOperState','TmnxPortID','TmnxServId')
tmnxSASPortMIBModule=ModuleIdentity((1,3,6,1,4,1,6527,6,2,1,1,6))
if mibBuilder.loadTexts:tmnxSASPortMIBModule.setRevisions(('1908-01-09 00:00',))
_TmnxSASPortConformance_ObjectIdentity=ObjectIdentity
tmnxSASPortConformance=_TmnxSASPortConformance_ObjectIdentity((1,3,6,1,4,1,6527,6,2,2,1,2))
_TmnxSASPortCompliances_ObjectIdentity=ObjectIdentity
tmnxSASPortCompliances=_TmnxSASPortCompliances_ObjectIdentity((1,3,6,1,4,1,6527,6,2,2,1,2,1))
_TmnxSASPortGroups_ObjectIdentity=ObjectIdentity
tmnxSASPortGroups=_TmnxSASPortGroups_ObjectIdentity((1,3,6,1,4,1,6527,6,2,2,1,2,2))
_TmnxSASPortObjs_ObjectIdentity=ObjectIdentity
tmnxSASPortObjs=_TmnxSASPortObjs_ObjectIdentity((1,3,6,1,4,1,6527,6,2,2,2,2))
_SasTmnxPortExtnTable_Object=MibTable
sasTmnxPortExtnTable=_SasTmnxPortExtnTable_Object((1,3,6,1,4,1,6527,6,2,2,2,2,2))
if mibBuilder.loadTexts:sasTmnxPortExtnTable.setStatus(_A)
_SasTmnxPortExtnEntry_Object=MibTableRow
sasTmnxPortExtnEntry=_SasTmnxPortExtnEntry_Object((1,3,6,1,4,1,6527,6,2,2,2,2,2,1))
if mibBuilder.loadTexts:sasTmnxPortExtnEntry.setStatus(_A)
_TmnxPortUplinkMode_Type=TruthValue
_TmnxPortUplinkMode_Object=MibTableColumn
tmnxPortUplinkMode=_TmnxPortUplinkMode_Object((1,3,6,1,4,1,6527,6,2,2,2,2,2,1,1),_TmnxPortUplinkMode_Type())
tmnxPortUplinkMode.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxPortUplinkMode.setStatus(_A)
class _TmnxPortAccessEgressQoSPolicyId_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_TmnxPortAccessEgressQoSPolicyId_Type.__name__=_K
_TmnxPortAccessEgressQoSPolicyId_Object=MibTableColumn
tmnxPortAccessEgressQoSPolicyId=_TmnxPortAccessEgressQoSPolicyId_Object((1,3,6,1,4,1,6527,6,2,2,2,2,2,1,2),_TmnxPortAccessEgressQoSPolicyId_Type())
tmnxPortAccessEgressQoSPolicyId.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxPortAccessEgressQoSPolicyId.setStatus(_A)
class _TmnxPortNetworkQoSPolicyId_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_TmnxPortNetworkQoSPolicyId_Type.__name__=_K
_TmnxPortNetworkQoSPolicyId_Object=MibTableColumn
tmnxPortNetworkQoSPolicyId=_TmnxPortNetworkQoSPolicyId_Object((1,3,6,1,4,1,6527,6,2,2,2,2,2,1,3),_TmnxPortNetworkQoSPolicyId_Type())
tmnxPortNetworkQoSPolicyId.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxPortNetworkQoSPolicyId.setStatus(_A)
_TmnxPortShgName_Type=TNamedItemOrEmpty
_TmnxPortShgName_Object=MibTableColumn
tmnxPortShgName=_TmnxPortShgName_Object((1,3,6,1,4,1,6527,6,2,2,2,2,2,1,4),_TmnxPortShgName_Type())
tmnxPortShgName.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxPortShgName.setStatus(_A)
class _TmnxPortUseDei_Type(TruthValue):defaultValue=2
_TmnxPortUseDei_Type.__name__=_L
_TmnxPortUseDei_Object=MibTableColumn
tmnxPortUseDei=_TmnxPortUseDei_Object((1,3,6,1,4,1,6527,6,2,2,2,2,2,1,5),_TmnxPortUseDei_Type())
tmnxPortUseDei.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxPortUseDei.setStatus(_A)
_TmnxPortOperGrpName_Type=TNamedItemOrEmpty
_TmnxPortOperGrpName_Object=MibTableColumn
tmnxPortOperGrpName=_TmnxPortOperGrpName_Object((1,3,6,1,4,1,6527,6,2,2,2,2,2,1,6),_TmnxPortOperGrpName_Type())
tmnxPortOperGrpName.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxPortOperGrpName.setStatus(_A)
_TmnxPortMonitorOperGrpName_Type=TNamedItemOrEmpty
_TmnxPortMonitorOperGrpName_Object=MibTableColumn
tmnxPortMonitorOperGrpName=_TmnxPortMonitorOperGrpName_Object((1,3,6,1,4,1,6527,6,2,2,2,2,2,1,7),_TmnxPortMonitorOperGrpName_Type())
tmnxPortMonitorOperGrpName.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxPortMonitorOperGrpName.setStatus(_A)
_TmnxSASPortNetIngressStatsTable_Object=MibTable
tmnxSASPortNetIngressStatsTable=_TmnxSASPortNetIngressStatsTable_Object((1,3,6,1,4,1,6527,6,2,2,2,2,3))
if mibBuilder.loadTexts:tmnxSASPortNetIngressStatsTable.setStatus(_A)
_TmnxSASPortNetIngressStatsEntry_Object=MibTableRow
tmnxSASPortNetIngressStatsEntry=_TmnxSASPortNetIngressStatsEntry_Object((1,3,6,1,4,1,6527,6,2,2,2,2,3,1))
tmnxSASPortNetIngressStatsEntry.setIndexNames((0,_F,_G),(0,_H,_I),(0,_B,_j))
if mibBuilder.loadTexts:tmnxSASPortNetIngressStatsEntry.setStatus(_A)
_TmnxSASPortNetIngressMeterIndex_Type=TNetworkIngressMeterId
_TmnxSASPortNetIngressMeterIndex_Object=MibTableColumn
tmnxSASPortNetIngressMeterIndex=_TmnxSASPortNetIngressMeterIndex_Object((1,3,6,1,4,1,6527,6,2,2,2,2,3,1,1),_TmnxSASPortNetIngressMeterIndex_Type())
tmnxSASPortNetIngressMeterIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:tmnxSASPortNetIngressMeterIndex.setStatus(_A)
_TmnxSASPortNetIngressFwdInProfPkts_Type=Counter64
_TmnxSASPortNetIngressFwdInProfPkts_Object=MibTableColumn
tmnxSASPortNetIngressFwdInProfPkts=_TmnxSASPortNetIngressFwdInProfPkts_Object((1,3,6,1,4,1,6527,6,2,2,2,2,3,1,2),_TmnxSASPortNetIngressFwdInProfPkts_Type())
tmnxSASPortNetIngressFwdInProfPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxSASPortNetIngressFwdInProfPkts.setStatus(_A)
_TmnxSASPortNetIngressFwdOutProfPkts_Type=Counter64
_TmnxSASPortNetIngressFwdOutProfPkts_Object=MibTableColumn
tmnxSASPortNetIngressFwdOutProfPkts=_TmnxSASPortNetIngressFwdOutProfPkts_Object((1,3,6,1,4,1,6527,6,2,2,2,2,3,1,3),_TmnxSASPortNetIngressFwdOutProfPkts_Type())
tmnxSASPortNetIngressFwdOutProfPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxSASPortNetIngressFwdOutProfPkts.setStatus(_A)
_TmnxSASPortNetIngressFwdInProfOcts_Type=Counter64
_TmnxSASPortNetIngressFwdInProfOcts_Object=MibTableColumn
tmnxSASPortNetIngressFwdInProfOcts=_TmnxSASPortNetIngressFwdInProfOcts_Object((1,3,6,1,4,1,6527,6,2,2,2,2,3,1,4),_TmnxSASPortNetIngressFwdInProfOcts_Type())
tmnxSASPortNetIngressFwdInProfOcts.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxSASPortNetIngressFwdInProfOcts.setStatus(_A)
_TmnxSASPortNetIngressFwdOutProfOcts_Type=Counter64
_TmnxSASPortNetIngressFwdOutProfOcts_Object=MibTableColumn
tmnxSASPortNetIngressFwdOutProfOcts=_TmnxSASPortNetIngressFwdOutProfOcts_Object((1,3,6,1,4,1,6527,6,2,2,2,2,3,1,5),_TmnxSASPortNetIngressFwdOutProfOcts_Type())
tmnxSASPortNetIngressFwdOutProfOcts.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxSASPortNetIngressFwdOutProfOcts.setStatus(_A)
_SasTmnxPortEtherExtnTable_Object=MibTable
sasTmnxPortEtherExtnTable=_SasTmnxPortEtherExtnTable_Object((1,3,6,1,4,1,6527,6,2,2,2,2,4))
if mibBuilder.loadTexts:sasTmnxPortEtherExtnTable.setStatus(_A)
_SasTmnxPortEtherExtnEntry_Object=MibTableRow
sasTmnxPortEtherExtnEntry=_SasTmnxPortEtherExtnEntry_Object((1,3,6,1,4,1,6527,6,2,2,2,2,4,1))
if mibBuilder.loadTexts:sasTmnxPortEtherExtnEntry.setStatus(_A)
class _TmnxPortEtherEgressMaxBurst_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(32,16384))
_TmnxPortEtherEgressMaxBurst_Type.__name__=_E
_TmnxPortEtherEgressMaxBurst_Object=MibTableColumn
tmnxPortEtherEgressMaxBurst=_TmnxPortEtherEgressMaxBurst_Object((1,3,6,1,4,1,6527,6,2,2,2,2,4,1,1),_TmnxPortEtherEgressMaxBurst_Type())
tmnxPortEtherEgressMaxBurst.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxPortEtherEgressMaxBurst.setStatus(_A)
_TmnxPortStatsQueue1PktsFwd_Type=TruthValue
_TmnxPortStatsQueue1PktsFwd_Object=MibTableColumn
tmnxPortStatsQueue1PktsFwd=_TmnxPortStatsQueue1PktsFwd_Object((1,3,6,1,4,1,6527,6,2,2,2,2,4,1,2),_TmnxPortStatsQueue1PktsFwd_Type())
tmnxPortStatsQueue1PktsFwd.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxPortStatsQueue1PktsFwd.setStatus(_A)
_TmnxPortStatsQueue2PktsFwd_Type=TruthValue
_TmnxPortStatsQueue2PktsFwd_Object=MibTableColumn
tmnxPortStatsQueue2PktsFwd=_TmnxPortStatsQueue2PktsFwd_Object((1,3,6,1,4,1,6527,6,2,2,2,2,4,1,3),_TmnxPortStatsQueue2PktsFwd_Type())
tmnxPortStatsQueue2PktsFwd.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxPortStatsQueue2PktsFwd.setStatus(_A)
_TmnxPortStatsQueue3PktsFwd_Type=TruthValue
_TmnxPortStatsQueue3PktsFwd_Object=MibTableColumn
tmnxPortStatsQueue3PktsFwd=_TmnxPortStatsQueue3PktsFwd_Object((1,3,6,1,4,1,6527,6,2,2,2,2,4,1,4),_TmnxPortStatsQueue3PktsFwd_Type())
tmnxPortStatsQueue3PktsFwd.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxPortStatsQueue3PktsFwd.setStatus(_A)
_TmnxPortStatsQueue4PktsFwd_Type=TruthValue
_TmnxPortStatsQueue4PktsFwd_Object=MibTableColumn
tmnxPortStatsQueue4PktsFwd=_TmnxPortStatsQueue4PktsFwd_Object((1,3,6,1,4,1,6527,6,2,2,2,2,4,1,5),_TmnxPortStatsQueue4PktsFwd_Type())
tmnxPortStatsQueue4PktsFwd.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxPortStatsQueue4PktsFwd.setStatus(_A)
_TmnxPortStatsQueue5PktsFwd_Type=TruthValue
_TmnxPortStatsQueue5PktsFwd_Object=MibTableColumn
tmnxPortStatsQueue5PktsFwd=_TmnxPortStatsQueue5PktsFwd_Object((1,3,6,1,4,1,6527,6,2,2,2,2,4,1,6),_TmnxPortStatsQueue5PktsFwd_Type())
tmnxPortStatsQueue5PktsFwd.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxPortStatsQueue5PktsFwd.setStatus(_A)
_TmnxPortStatsQueue6PktsFwd_Type=TruthValue
_TmnxPortStatsQueue6PktsFwd_Object=MibTableColumn
tmnxPortStatsQueue6PktsFwd=_TmnxPortStatsQueue6PktsFwd_Object((1,3,6,1,4,1,6527,6,2,2,2,2,4,1,7),_TmnxPortStatsQueue6PktsFwd_Type())
tmnxPortStatsQueue6PktsFwd.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxPortStatsQueue6PktsFwd.setStatus(_A)
_TmnxPortStatsQueue7PktsFwd_Type=TruthValue
_TmnxPortStatsQueue7PktsFwd_Object=MibTableColumn
tmnxPortStatsQueue7PktsFwd=_TmnxPortStatsQueue7PktsFwd_Object((1,3,6,1,4,1,6527,6,2,2,2,2,4,1,8),_TmnxPortStatsQueue7PktsFwd_Type())
tmnxPortStatsQueue7PktsFwd.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxPortStatsQueue7PktsFwd.setStatus(_A)
_TmnxPortStatsQueue8PktsFwd_Type=TruthValue
_TmnxPortStatsQueue8PktsFwd_Object=MibTableColumn
tmnxPortStatsQueue8PktsFwd=_TmnxPortStatsQueue8PktsFwd_Object((1,3,6,1,4,1,6527,6,2,2,2,2,4,1,9),_TmnxPortStatsQueue8PktsFwd_Type())
tmnxPortStatsQueue8PktsFwd.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxPortStatsQueue8PktsFwd.setStatus(_A)
class _TmnxPortEtherEgrSchedMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('fc-based',1),('sap-based',2)))
_TmnxPortEtherEgrSchedMode_Type.__name__=_E
_TmnxPortEtherEgrSchedMode_Object=MibTableColumn
tmnxPortEtherEgrSchedMode=_TmnxPortEtherEgrSchedMode_Object((1,3,6,1,4,1,6527,6,2,2,2,2,4,1,10),_TmnxPortEtherEgrSchedMode_Type())
tmnxPortEtherEgrSchedMode.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxPortEtherEgrSchedMode.setStatus(_A)
class _TmnxPortEtherLoopback_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,2)));namedValues=NamedValues(*((_O,0),('internal',2)))
_TmnxPortEtherLoopback_Type.__name__=_E
_TmnxPortEtherLoopback_Object=MibTableColumn
tmnxPortEtherLoopback=_TmnxPortEtherLoopback_Object((1,3,6,1,4,1,6527,6,2,2,2,2,4,1,11),_TmnxPortEtherLoopback_Type())
tmnxPortEtherLoopback.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxPortEtherLoopback.setStatus(_A)
class _TmnxPortEtherIpMTU_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(512,9000))
_TmnxPortEtherIpMTU_Type.__name__=_K
_TmnxPortEtherIpMTU_Object=MibTableColumn
tmnxPortEtherIpMTU=_TmnxPortEtherIpMTU_Object((1,3,6,1,4,1,6527,6,2,2,2,2,4,1,12),_TmnxPortEtherIpMTU_Type())
tmnxPortEtherIpMTU.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxPortEtherIpMTU.setStatus(_A)
if mibBuilder.loadTexts:tmnxPortEtherIpMTU.setUnits('bytes')
class _TmnxPortEtherClockConfig_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_P,0),('automatic',1),('manual-master',2),('manual-slave',3)))
_TmnxPortEtherClockConfig_Type.__name__=_E
_TmnxPortEtherClockConfig_Object=MibTableColumn
tmnxPortEtherClockConfig=_TmnxPortEtherClockConfig_Object((1,3,6,1,4,1,6527,6,2,2,2,2,4,1,13),_TmnxPortEtherClockConfig_Type())
tmnxPortEtherClockConfig.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxPortEtherClockConfig.setStatus(_A)
_TmnxPortLoopbckServId_Type=TmnxServId
_TmnxPortLoopbckServId_Object=MibTableColumn
tmnxPortLoopbckServId=_TmnxPortLoopbckServId_Object((1,3,6,1,4,1,6527,6,2,2,2,2,4,1,14),_TmnxPortLoopbckServId_Type())
tmnxPortLoopbckServId.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxPortLoopbckServId.setStatus(_A)
_TmnxPortLoopbckSapPortId_Type=TmnxPortID
_TmnxPortLoopbckSapPortId_Object=MibTableColumn
tmnxPortLoopbckSapPortId=_TmnxPortLoopbckSapPortId_Object((1,3,6,1,4,1,6527,6,2,2,2,2,4,1,15),_TmnxPortLoopbckSapPortId_Type())
tmnxPortLoopbckSapPortId.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxPortLoopbckSapPortId.setStatus(_A)
_TmnxPortLoopbckSapEncapVal_Type=TmnxEncapVal
_TmnxPortLoopbckSapEncapVal_Object=MibTableColumn
tmnxPortLoopbckSapEncapVal=_TmnxPortLoopbckSapEncapVal_Object((1,3,6,1,4,1,6527,6,2,2,2,2,4,1,16),_TmnxPortLoopbckSapEncapVal_Type())
tmnxPortLoopbckSapEncapVal.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxPortLoopbckSapEncapVal.setStatus(_A)
_TmnxPortLoopbckSrcMacAddr_Type=MacAddress
_TmnxPortLoopbckSrcMacAddr_Object=MibTableColumn
tmnxPortLoopbckSrcMacAddr=_TmnxPortLoopbckSrcMacAddr_Object((1,3,6,1,4,1,6527,6,2,2,2,2,4,1,17),_TmnxPortLoopbckSrcMacAddr_Type())
tmnxPortLoopbckSrcMacAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxPortLoopbckSrcMacAddr.setStatus(_A)
_TmnxPortLoopbckDstMacAddr_Type=MacAddress
_TmnxPortLoopbckDstMacAddr_Object=MibTableColumn
tmnxPortLoopbckDstMacAddr=_TmnxPortLoopbckDstMacAddr_Object((1,3,6,1,4,1,6527,6,2,2,2,2,4,1,18),_TmnxPortLoopbckDstMacAddr_Type())
tmnxPortLoopbckDstMacAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxPortLoopbckDstMacAddr.setStatus(_A)
class _TmnxPortAccEgrSapQosMarking_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_TmnxPortAccEgrSapQosMarking_Type.__name__=_E
_TmnxPortAccEgrSapQosMarking_Object=MibTableColumn
tmnxPortAccEgrSapQosMarking=_TmnxPortAccEgrSapQosMarking_Object((1,3,6,1,4,1,6527,6,2,2,2,2,4,1,19),_TmnxPortAccEgrSapQosMarking_Type())
tmnxPortAccEgrSapQosMarking.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxPortAccEgrSapQosMarking.setStatus(_A)
class _TmnxPortLldpTnlNrstBrdgeDstMac_Type(TruthValue):defaultValue=2
_TmnxPortLldpTnlNrstBrdgeDstMac_Type.__name__=_L
_TmnxPortLldpTnlNrstBrdgeDstMac_Object=MibTableColumn
tmnxPortLldpTnlNrstBrdgeDstMac=_TmnxPortLldpTnlNrstBrdgeDstMac_Object((1,3,6,1,4,1,6527,6,2,2,2,2,4,1,20),_TmnxPortLldpTnlNrstBrdgeDstMac_Type())
tmnxPortLldpTnlNrstBrdgeDstMac.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxPortLldpTnlNrstBrdgeDstMac.setStatus(_A)
class _TmnxPortEtherDe1OutProfile_Type(TruthValue):defaultValue=2
_TmnxPortEtherDe1OutProfile_Type.__name__=_L
_TmnxPortEtherDe1OutProfile_Object=MibTableColumn
tmnxPortEtherDe1OutProfile=_TmnxPortEtherDe1OutProfile_Object((1,3,6,1,4,1,6527,6,2,2,2,2,4,1,22),_TmnxPortEtherDe1OutProfile_Type())
tmnxPortEtherDe1OutProfile.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxPortEtherDe1OutProfile.setStatus(_A)
class _TmnxPortEtherNwAggRateLimit_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(1,100000000))
_TmnxPortEtherNwAggRateLimit_Type.__name__=_E
_TmnxPortEtherNwAggRateLimit_Object=MibTableColumn
tmnxPortEtherNwAggRateLimit=_TmnxPortEtherNwAggRateLimit_Object((1,3,6,1,4,1,6527,6,2,2,2,2,4,1,23),_TmnxPortEtherNwAggRateLimit_Type())
tmnxPortEtherNwAggRateLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxPortEtherNwAggRateLimit.setStatus(_A)
class _TmnxPortEtherNwAggRateLimitCir_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000000))
_TmnxPortEtherNwAggRateLimitCir_Type.__name__=_E
_TmnxPortEtherNwAggRateLimitCir_Object=MibTableColumn
tmnxPortEtherNwAggRateLimitCir=_TmnxPortEtherNwAggRateLimitCir_Object((1,3,6,1,4,1,6527,6,2,2,2,2,4,1,28),_TmnxPortEtherNwAggRateLimitCir_Type())
tmnxPortEtherNwAggRateLimitCir.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxPortEtherNwAggRateLimitCir.setStatus(_A)
class _TmnxPortEtherNwAggRateLimitPir_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(1,10000000))
_TmnxPortEtherNwAggRateLimitPir_Type.__name__=_E
_TmnxPortEtherNwAggRateLimitPir_Object=MibTableColumn
tmnxPortEtherNwAggRateLimitPir=_TmnxPortEtherNwAggRateLimitPir_Object((1,3,6,1,4,1,6527,6,2,2,2,2,4,1,29),_TmnxPortEtherNwAggRateLimitPir_Type())
tmnxPortEtherNwAggRateLimitPir.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxPortEtherNwAggRateLimitPir.setStatus(_A)
_TmnxPortEtherDcommStatus_Type=TruthValue
_TmnxPortEtherDcommStatus_Object=MibTableColumn
tmnxPortEtherDcommStatus=_TmnxPortEtherDcommStatus_Object((1,3,6,1,4,1,6527,6,2,2,2,2,4,1,30),_TmnxPortEtherDcommStatus_Type())
tmnxPortEtherDcommStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxPortEtherDcommStatus.setStatus(_A)
class _TmnxPortEtherMulticastIngress_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('l2-mc',1),('ip-mc',2)))
_TmnxPortEtherMulticastIngress_Type.__name__=_E
_TmnxPortEtherMulticastIngress_Object=MibTableColumn
tmnxPortEtherMulticastIngress=_TmnxPortEtherMulticastIngress_Object((1,3,6,1,4,1,6527,6,2,2,2,2,4,1,31),_TmnxPortEtherMulticastIngress_Type())
tmnxPortEtherMulticastIngress.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxPortEtherMulticastIngress.setStatus(_A)
_PortShgInfoTable_Object=MibTable
portShgInfoTable=_PortShgInfoTable_Object((1,3,6,1,4,1,6527,6,2,2,2,2,6))
if mibBuilder.loadTexts:portShgInfoTable.setStatus(_A)
_PortShgInfoEntry_Object=MibTableRow
portShgInfoEntry=_PortShgInfoEntry_Object((1,3,6,1,4,1,6527,6,2,2,2,2,6,1))
portShgInfoEntry.setIndexNames((1,_B,_k))
if mibBuilder.loadTexts:portShgInfoEntry.setStatus(_A)
_PortShgName_Type=TNamedItem
_PortShgName_Object=MibTableColumn
portShgName=_PortShgName_Object((1,3,6,1,4,1,6527,6,2,2,2,2,6,1,1),_PortShgName_Type())
portShgName.setMaxAccess(_J)
if mibBuilder.loadTexts:portShgName.setStatus(_A)
_PortShgRowStatus_Type=RowStatus
_PortShgRowStatus_Object=MibTableColumn
portShgRowStatus=_PortShgRowStatus_Object((1,3,6,1,4,1,6527,6,2,2,2,2,6,1,2),_PortShgRowStatus_Type())
portShgRowStatus.setMaxAccess(_l)
if mibBuilder.loadTexts:portShgRowStatus.setStatus(_A)
_PortShgInstanceId_Type=Unsigned32
_PortShgInstanceId_Object=MibTableColumn
portShgInstanceId=_PortShgInstanceId_Object((1,3,6,1,4,1,6527,6,2,2,2,2,6,1,3),_PortShgInstanceId_Type())
portShgInstanceId.setMaxAccess(_C)
if mibBuilder.loadTexts:portShgInstanceId.setStatus(_A)
class _PortShgDescription_Type(ServObjDesc):defaultValue=OctetString('')
_PortShgDescription_Type.__name__=_i
_PortShgDescription_Object=MibTableColumn
portShgDescription=_PortShgDescription_Object((1,3,6,1,4,1,6527,6,2,2,2,2,6,1,4),_PortShgDescription_Type())
portShgDescription.setMaxAccess(_l)
if mibBuilder.loadTexts:portShgDescription.setStatus(_A)
_PortShgLastMgmtChange_Type=TimeStamp
_PortShgLastMgmtChange_Object=MibTableColumn
portShgLastMgmtChange=_PortShgLastMgmtChange_Object((1,3,6,1,4,1,6527,6,2,2,2,2,6,1,5),_PortShgLastMgmtChange_Type())
portShgLastMgmtChange.setMaxAccess(_C)
if mibBuilder.loadTexts:portShgLastMgmtChange.setStatus(_A)
_TmnxPortAccessEgressQueueStatsTable_Object=MibTable
tmnxPortAccessEgressQueueStatsTable=_TmnxPortAccessEgressQueueStatsTable_Object((1,3,6,1,4,1,6527,6,2,2,2,2,7))
if mibBuilder.loadTexts:tmnxPortAccessEgressQueueStatsTable.setStatus(_A)
_TmnxPortAccessEgressQueueStatsEntry_Object=MibTableRow
tmnxPortAccessEgressQueueStatsEntry=_TmnxPortAccessEgressQueueStatsEntry_Object((1,3,6,1,4,1,6527,6,2,2,2,2,7,1))
tmnxPortAccessEgressQueueStatsEntry.setIndexNames((0,_F,_G),(0,_H,_I),(0,_B,_m))
if mibBuilder.loadTexts:tmnxPortAccessEgressQueueStatsEntry.setStatus(_A)
class _TmnxPortAccessEgressQueueStatsIndex_Type(TQueueId):subtypeSpec=TQueueId.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_TmnxPortAccessEgressQueueStatsIndex_Type.__name__=_N
_TmnxPortAccessEgressQueueStatsIndex_Object=MibTableColumn
tmnxPortAccessEgressQueueStatsIndex=_TmnxPortAccessEgressQueueStatsIndex_Object((1,3,6,1,4,1,6527,6,2,2,2,2,7,1,1),_TmnxPortAccessEgressQueueStatsIndex_Type())
tmnxPortAccessEgressQueueStatsIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:tmnxPortAccessEgressQueueStatsIndex.setStatus(_A)
_TmnxPortAccessEgressQueueStatsFwdPkts_Type=Counter64
_TmnxPortAccessEgressQueueStatsFwdPkts_Object=MibTableColumn
tmnxPortAccessEgressQueueStatsFwdPkts=_TmnxPortAccessEgressQueueStatsFwdPkts_Object((1,3,6,1,4,1,6527,6,2,2,2,2,7,1,2),_TmnxPortAccessEgressQueueStatsFwdPkts_Type())
tmnxPortAccessEgressQueueStatsFwdPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxPortAccessEgressQueueStatsFwdPkts.setStatus(_A)
_TmnxPortAccessEgressQueueStatsFwdOcts_Type=Counter64
_TmnxPortAccessEgressQueueStatsFwdOcts_Object=MibTableColumn
tmnxPortAccessEgressQueueStatsFwdOcts=_TmnxPortAccessEgressQueueStatsFwdOcts_Object((1,3,6,1,4,1,6527,6,2,2,2,2,7,1,3),_TmnxPortAccessEgressQueueStatsFwdOcts_Type())
tmnxPortAccessEgressQueueStatsFwdOcts.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxPortAccessEgressQueueStatsFwdOcts.setStatus(_A)
_TmnxPortAccessEgressQueueStatsDroPkts_Type=Counter64
_TmnxPortAccessEgressQueueStatsDroPkts_Object=MibTableColumn
tmnxPortAccessEgressQueueStatsDroPkts=_TmnxPortAccessEgressQueueStatsDroPkts_Object((1,3,6,1,4,1,6527,6,2,2,2,2,7,1,4),_TmnxPortAccessEgressQueueStatsDroPkts_Type())
tmnxPortAccessEgressQueueStatsDroPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxPortAccessEgressQueueStatsDroPkts.setStatus(_A)
_TmnxPortAccessEgressQueueStatsDroOcts_Type=Counter64
_TmnxPortAccessEgressQueueStatsDroOcts_Object=MibTableColumn
tmnxPortAccessEgressQueueStatsDroOcts=_TmnxPortAccessEgressQueueStatsDroOcts_Object((1,3,6,1,4,1,6527,6,2,2,2,2,7,1,5),_TmnxPortAccessEgressQueueStatsDroOcts_Type())
tmnxPortAccessEgressQueueStatsDroOcts.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxPortAccessEgressQueueStatsDroOcts.setStatus(_A)
_TmnxPortNetEgressQueueStatsTable_Object=MibTable
tmnxPortNetEgressQueueStatsTable=_TmnxPortNetEgressQueueStatsTable_Object((1,3,6,1,4,1,6527,6,2,2,2,2,8))
if mibBuilder.loadTexts:tmnxPortNetEgressQueueStatsTable.setStatus(_A)
_TmnxPortNetEgressQueueStatsEntry_Object=MibTableRow
tmnxPortNetEgressQueueStatsEntry=_TmnxPortNetEgressQueueStatsEntry_Object((1,3,6,1,4,1,6527,6,2,2,2,2,8,1))
tmnxPortNetEgressQueueStatsEntry.setIndexNames((0,_F,_G),(0,_H,_I),(0,_B,_n))
if mibBuilder.loadTexts:tmnxPortNetEgressQueueStatsEntry.setStatus(_A)
class _TmnxPortNetEgressQueueStatsIndex_Type(TQueueId):subtypeSpec=TQueueId.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_TmnxPortNetEgressQueueStatsIndex_Type.__name__=_N
_TmnxPortNetEgressQueueStatsIndex_Object=MibTableColumn
tmnxPortNetEgressQueueStatsIndex=_TmnxPortNetEgressQueueStatsIndex_Object((1,3,6,1,4,1,6527,6,2,2,2,2,8,1,1),_TmnxPortNetEgressQueueStatsIndex_Type())
tmnxPortNetEgressQueueStatsIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:tmnxPortNetEgressQueueStatsIndex.setStatus(_A)
_TmnxPortNetEgressQueueStatsFwdPkts_Type=Counter64
_TmnxPortNetEgressQueueStatsFwdPkts_Object=MibTableColumn
tmnxPortNetEgressQueueStatsFwdPkts=_TmnxPortNetEgressQueueStatsFwdPkts_Object((1,3,6,1,4,1,6527,6,2,2,2,2,8,1,2),_TmnxPortNetEgressQueueStatsFwdPkts_Type())
tmnxPortNetEgressQueueStatsFwdPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxPortNetEgressQueueStatsFwdPkts.setStatus(_A)
_TmnxPortNetEgressQueueStatsFwdOcts_Type=Counter64
_TmnxPortNetEgressQueueStatsFwdOcts_Object=MibTableColumn
tmnxPortNetEgressQueueStatsFwdOcts=_TmnxPortNetEgressQueueStatsFwdOcts_Object((1,3,6,1,4,1,6527,6,2,2,2,2,8,1,3),_TmnxPortNetEgressQueueStatsFwdOcts_Type())
tmnxPortNetEgressQueueStatsFwdOcts.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxPortNetEgressQueueStatsFwdOcts.setStatus(_A)
_TmnxPortNetEgressQueueStatsDroPkts_Type=Counter64
_TmnxPortNetEgressQueueStatsDroPkts_Object=MibTableColumn
tmnxPortNetEgressQueueStatsDroPkts=_TmnxPortNetEgressQueueStatsDroPkts_Object((1,3,6,1,4,1,6527,6,2,2,2,2,8,1,4),_TmnxPortNetEgressQueueStatsDroPkts_Type())
tmnxPortNetEgressQueueStatsDroPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxPortNetEgressQueueStatsDroPkts.setStatus(_A)
_TmnxPortNetEgressQueueStatsDroOcts_Type=Counter64
_TmnxPortNetEgressQueueStatsDroOcts_Object=MibTableColumn
tmnxPortNetEgressQueueStatsDroOcts=_TmnxPortNetEgressQueueStatsDroOcts_Object((1,3,6,1,4,1,6527,6,2,2,2,2,8,1,5),_TmnxPortNetEgressQueueStatsDroOcts_Type())
tmnxPortNetEgressQueueStatsDroOcts.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxPortNetEgressQueueStatsDroOcts.setStatus(_A)
_TmnxPortNetEgressQueueStatsInProfDroPkts_Type=Counter64
_TmnxPortNetEgressQueueStatsInProfDroPkts_Object=MibTableColumn
tmnxPortNetEgressQueueStatsInProfDroPkts=_TmnxPortNetEgressQueueStatsInProfDroPkts_Object((1,3,6,1,4,1,6527,6,2,2,2,2,8,1,6),_TmnxPortNetEgressQueueStatsInProfDroPkts_Type())
tmnxPortNetEgressQueueStatsInProfDroPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxPortNetEgressQueueStatsInProfDroPkts.setStatus(_A)
_TmnxPortNetEgressQueueStatsInProfDroOcts_Type=Counter64
_TmnxPortNetEgressQueueStatsInProfDroOcts_Object=MibTableColumn
tmnxPortNetEgressQueueStatsInProfDroOcts=_TmnxPortNetEgressQueueStatsInProfDroOcts_Object((1,3,6,1,4,1,6527,6,2,2,2,2,8,1,7),_TmnxPortNetEgressQueueStatsInProfDroOcts_Type())
tmnxPortNetEgressQueueStatsInProfDroOcts.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxPortNetEgressQueueStatsInProfDroOcts.setStatus(_A)
_TmnxPortNetEgressQueueStatsOutProfDroPkts_Type=Counter64
_TmnxPortNetEgressQueueStatsOutProfDroPkts_Object=MibTableColumn
tmnxPortNetEgressQueueStatsOutProfDroPkts=_TmnxPortNetEgressQueueStatsOutProfDroPkts_Object((1,3,6,1,4,1,6527,6,2,2,2,2,8,1,8),_TmnxPortNetEgressQueueStatsOutProfDroPkts_Type())
tmnxPortNetEgressQueueStatsOutProfDroPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxPortNetEgressQueueStatsOutProfDroPkts.setStatus(_A)
_TmnxPortNetEgressQueueStatsOutProfDroOcts_Type=Counter64
_TmnxPortNetEgressQueueStatsOutProfDroOcts_Object=MibTableColumn
tmnxPortNetEgressQueueStatsOutProfDroOcts=_TmnxPortNetEgressQueueStatsOutProfDroOcts_Object((1,3,6,1,4,1,6527,6,2,2,2,2,8,1,9),_TmnxPortNetEgressQueueStatsOutProfDroOcts_Type())
tmnxPortNetEgressQueueStatsOutProfDroOcts.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxPortNetEgressQueueStatsOutProfDroOcts.setStatus(_A)
_AluExtTmnxDS1PortTable_Object=MibTable
aluExtTmnxDS1PortTable=_AluExtTmnxDS1PortTable_Object((1,3,6,1,4,1,6527,6,2,2,2,2,9))
if mibBuilder.loadTexts:aluExtTmnxDS1PortTable.setStatus(_A)
_AluExtTmnxDS1PortEntry_Object=MibTableRow
aluExtTmnxDS1PortEntry=_AluExtTmnxDS1PortEntry_Object((1,3,6,1,4,1,6527,6,2,2,2,2,9,1))
if mibBuilder.loadTexts:aluExtTmnxDS1PortEntry.setStatus(_A)
class _AluExtDS1PortLineImpedance_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_P,0),('impedance75Ohms',1),('impedance100Ohms',2),('impedance120Ohms',3)))
_AluExtDS1PortLineImpedance_Type.__name__=_E
_AluExtDS1PortLineImpedance_Object=MibTableColumn
aluExtDS1PortLineImpedance=_AluExtDS1PortLineImpedance_Object((1,3,6,1,4,1,6527,6,2,2,2,2,9,1,1),_AluExtDS1PortLineImpedance_Type())
aluExtDS1PortLineImpedance.setMaxAccess(_D)
if mibBuilder.loadTexts:aluExtDS1PortLineImpedance.setStatus(_A)
_AluPortAcrClkStatsTable_Object=MibTable
aluPortAcrClkStatsTable=_AluPortAcrClkStatsTable_Object((1,3,6,1,4,1,6527,6,2,2,2,2,10))
if mibBuilder.loadTexts:aluPortAcrClkStatsTable.setStatus(_A)
_AluPortAcrClkStatsEntry_Object=MibTableRow
aluPortAcrClkStatsEntry=_AluPortAcrClkStatsEntry_Object((1,3,6,1,4,1,6527,6,2,2,2,2,10,1))
aluPortAcrClkStatsEntry.setIndexNames((0,_F,_G),(0,_H,_I))
if mibBuilder.loadTexts:aluPortAcrClkStatsEntry.setStatus(_A)
_AluLastUpdateTime_Type=TimeStamp
_AluLastUpdateTime_Object=MibTableColumn
aluLastUpdateTime=_AluLastUpdateTime_Object((1,3,6,1,4,1,6527,6,2,2,2,2,10,1,1),_AluLastUpdateTime_Type())
aluLastUpdateTime.setMaxAccess(_C)
if mibBuilder.loadTexts:aluLastUpdateTime.setStatus(_A)
_AluTotalMinutesIn24Hour_Type=Unsigned32
_AluTotalMinutesIn24Hour_Object=MibTableColumn
aluTotalMinutesIn24Hour=_AluTotalMinutesIn24Hour_Object((1,3,6,1,4,1,6527,6,2,2,2,2,10,1,2),_AluTotalMinutesIn24Hour_Type())
aluTotalMinutesIn24Hour.setMaxAccess(_C)
if mibBuilder.loadTexts:aluTotalMinutesIn24Hour.setStatus(_A)
_AluCurrent24HourFreqOffsetMeanPpb_Type=Integer32
_AluCurrent24HourFreqOffsetMeanPpb_Object=MibTableColumn
aluCurrent24HourFreqOffsetMeanPpb=_AluCurrent24HourFreqOffsetMeanPpb_Object((1,3,6,1,4,1,6527,6,2,2,2,2,10,1,3),_AluCurrent24HourFreqOffsetMeanPpb_Type())
aluCurrent24HourFreqOffsetMeanPpb.setMaxAccess(_C)
if mibBuilder.loadTexts:aluCurrent24HourFreqOffsetMeanPpb.setStatus(_A)
_AluCurrent24HourFreqOffsetStdDevPpb_Type=Unsigned32
_AluCurrent24HourFreqOffsetStdDevPpb_Object=MibTableColumn
aluCurrent24HourFreqOffsetStdDevPpb=_AluCurrent24HourFreqOffsetStdDevPpb_Object((1,3,6,1,4,1,6527,6,2,2,2,2,10,1,4),_AluCurrent24HourFreqOffsetStdDevPpb_Type())
aluCurrent24HourFreqOffsetStdDevPpb.setMaxAccess(_C)
if mibBuilder.loadTexts:aluCurrent24HourFreqOffsetStdDevPpb.setStatus(_A)
_AluMaxShortIntervalMinutes_Type=Unsigned32
_AluMaxShortIntervalMinutes_Object=MibTableColumn
aluMaxShortIntervalMinutes=_AluMaxShortIntervalMinutes_Object((1,3,6,1,4,1,6527,6,2,2,2,2,10,1,5),_AluMaxShortIntervalMinutes_Type())
aluMaxShortIntervalMinutes.setMaxAccess(_C)
if mibBuilder.loadTexts:aluMaxShortIntervalMinutes.setStatus(_A)
_AluTotalShortIntervalMinutes_Type=Unsigned32
_AluTotalShortIntervalMinutes_Object=MibTableColumn
aluTotalShortIntervalMinutes=_AluTotalShortIntervalMinutes_Object((1,3,6,1,4,1,6527,6,2,2,2,2,10,1,6),_AluTotalShortIntervalMinutes_Type())
aluTotalShortIntervalMinutes.setMaxAccess(_C)
if mibBuilder.loadTexts:aluTotalShortIntervalMinutes.setStatus(_A)
_AluCurrent1MinValidData_Type=TruthValue
_AluCurrent1MinValidData_Object=MibTableColumn
aluCurrent1MinValidData=_AluCurrent1MinValidData_Object((1,3,6,1,4,1,6527,6,2,2,2,2,10,1,7),_AluCurrent1MinValidData_Type())
aluCurrent1MinValidData.setMaxAccess(_C)
if mibBuilder.loadTexts:aluCurrent1MinValidData.setStatus(_A)
_AluCurrent1MinPhaseErrorMeanPpb_Type=Integer32
_AluCurrent1MinPhaseErrorMeanPpb_Object=MibTableColumn
aluCurrent1MinPhaseErrorMeanPpb=_AluCurrent1MinPhaseErrorMeanPpb_Object((1,3,6,1,4,1,6527,6,2,2,2,2,10,1,8),_AluCurrent1MinPhaseErrorMeanPpb_Type())
aluCurrent1MinPhaseErrorMeanPpb.setMaxAccess(_C)
if mibBuilder.loadTexts:aluCurrent1MinPhaseErrorMeanPpb.setStatus(_A)
_AluCurrent1MinPhaseErrorStdDevNs_Type=Unsigned32
_AluCurrent1MinPhaseErrorStdDevNs_Object=MibTableColumn
aluCurrent1MinPhaseErrorStdDevNs=_AluCurrent1MinPhaseErrorStdDevNs_Object((1,3,6,1,4,1,6527,6,2,2,2,2,10,1,9),_AluCurrent1MinPhaseErrorStdDevNs_Type())
aluCurrent1MinPhaseErrorStdDevNs.setMaxAccess(_C)
if mibBuilder.loadTexts:aluCurrent1MinPhaseErrorStdDevNs.setStatus(_A)
_AluCurrent1MinPhaseErrorMeanNs_Type=Integer32
_AluCurrent1MinPhaseErrorMeanNs_Object=MibTableColumn
aluCurrent1MinPhaseErrorMeanNs=_AluCurrent1MinPhaseErrorMeanNs_Object((1,3,6,1,4,1,6527,6,2,2,2,2,10,1,10),_AluCurrent1MinPhaseErrorMeanNs_Type())
aluCurrent1MinPhaseErrorMeanNs.setMaxAccess(_C)
if mibBuilder.loadTexts:aluCurrent1MinPhaseErrorMeanNs.setStatus(_A)
_AluCurrent1MinFreqOffsetMeanPpb_Type=Integer32
_AluCurrent1MinFreqOffsetMeanPpb_Object=MibTableColumn
aluCurrent1MinFreqOffsetMeanPpb=_AluCurrent1MinFreqOffsetMeanPpb_Object((1,3,6,1,4,1,6527,6,2,2,2,2,10,1,11),_AluCurrent1MinFreqOffsetMeanPpb_Type())
aluCurrent1MinFreqOffsetMeanPpb.setMaxAccess(_C)
if mibBuilder.loadTexts:aluCurrent1MinFreqOffsetMeanPpb.setStatus(_A)
_AluCurrent1MinFreqOffsetStdDevPpb_Type=Unsigned32
_AluCurrent1MinFreqOffsetStdDevPpb_Object=MibTableColumn
aluCurrent1MinFreqOffsetStdDevPpb=_AluCurrent1MinFreqOffsetStdDevPpb_Object((1,3,6,1,4,1,6527,6,2,2,2,2,10,1,12),_AluCurrent1MinFreqOffsetStdDevPpb_Type())
aluCurrent1MinFreqOffsetStdDevPpb.setMaxAccess(_C)
if mibBuilder.loadTexts:aluCurrent1MinFreqOffsetStdDevPpb.setStatus(_A)
_AluPortAcrClkStatsShortIntervalTable_Object=MibTable
aluPortAcrClkStatsShortIntervalTable=_AluPortAcrClkStatsShortIntervalTable_Object((1,3,6,1,4,1,6527,6,2,2,2,2,11))
if mibBuilder.loadTexts:aluPortAcrClkStatsShortIntervalTable.setStatus(_A)
_AluPortAcrClkStatsShortIntervalEntry_Object=MibTableRow
aluPortAcrClkStatsShortIntervalEntry=_AluPortAcrClkStatsShortIntervalEntry_Object((1,3,6,1,4,1,6527,6,2,2,2,2,11,1))
aluPortAcrClkStatsShortIntervalEntry.setIndexNames((0,_F,_G),(0,_H,_I),(0,_B,_Q))
if mibBuilder.loadTexts:aluPortAcrClkStatsShortIntervalEntry.setStatus(_A)
class _AluIntervalNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_AluIntervalNumber_Type.__name__=_E
_AluIntervalNumber_Object=MibTableColumn
aluIntervalNumber=_AluIntervalNumber_Object((1,3,6,1,4,1,6527,6,2,2,2,2,11,1,1),_AluIntervalNumber_Type())
aluIntervalNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:aluIntervalNumber.setStatus(_A)
_AluIntervalValidData_Type=TruthValue
_AluIntervalValidData_Object=MibTableColumn
aluIntervalValidData=_AluIntervalValidData_Object((1,3,6,1,4,1,6527,6,2,2,2,2,11,1,2),_AluIntervalValidData_Type())
aluIntervalValidData.setMaxAccess(_C)
if mibBuilder.loadTexts:aluIntervalValidData.setStatus(_A)
_AluIntervalUpdateTime_Type=TimeStamp
_AluIntervalUpdateTime_Object=MibTableColumn
aluIntervalUpdateTime=_AluIntervalUpdateTime_Object((1,3,6,1,4,1,6527,6,2,2,2,2,11,1,3),_AluIntervalUpdateTime_Type())
aluIntervalUpdateTime.setMaxAccess(_C)
if mibBuilder.loadTexts:aluIntervalUpdateTime.setStatus(_A)
_AluIntervalPhaseErrorMeanPpb_Type=Integer32
_AluIntervalPhaseErrorMeanPpb_Object=MibTableColumn
aluIntervalPhaseErrorMeanPpb=_AluIntervalPhaseErrorMeanPpb_Object((1,3,6,1,4,1,6527,6,2,2,2,2,11,1,4),_AluIntervalPhaseErrorMeanPpb_Type())
aluIntervalPhaseErrorMeanPpb.setMaxAccess(_C)
if mibBuilder.loadTexts:aluIntervalPhaseErrorMeanPpb.setStatus(_A)
_AluIntervalPhaseErrorStdDevNs_Type=Unsigned32
_AluIntervalPhaseErrorStdDevNs_Object=MibTableColumn
aluIntervalPhaseErrorStdDevNs=_AluIntervalPhaseErrorStdDevNs_Object((1,3,6,1,4,1,6527,6,2,2,2,2,11,1,5),_AluIntervalPhaseErrorStdDevNs_Type())
aluIntervalPhaseErrorStdDevNs.setMaxAccess(_C)
if mibBuilder.loadTexts:aluIntervalPhaseErrorStdDevNs.setStatus(_A)
_AluIntervalPhaseErrorMeanNs_Type=Integer32
_AluIntervalPhaseErrorMeanNs_Object=MibTableColumn
aluIntervalPhaseErrorMeanNs=_AluIntervalPhaseErrorMeanNs_Object((1,3,6,1,4,1,6527,6,2,2,2,2,11,1,6),_AluIntervalPhaseErrorMeanNs_Type())
aluIntervalPhaseErrorMeanNs.setMaxAccess(_C)
if mibBuilder.loadTexts:aluIntervalPhaseErrorMeanNs.setStatus(_A)
_AluIntervalFreqOffsetMeanPpb_Type=Integer32
_AluIntervalFreqOffsetMeanPpb_Object=MibTableColumn
aluIntervalFreqOffsetMeanPpb=_AluIntervalFreqOffsetMeanPpb_Object((1,3,6,1,4,1,6527,6,2,2,2,2,11,1,7),_AluIntervalFreqOffsetMeanPpb_Type())
aluIntervalFreqOffsetMeanPpb.setMaxAccess(_C)
if mibBuilder.loadTexts:aluIntervalFreqOffsetMeanPpb.setStatus(_A)
_AluIntervalFreqOffsetStdDevPpb_Type=Unsigned32
_AluIntervalFreqOffsetStdDevPpb_Object=MibTableColumn
aluIntervalFreqOffsetStdDevPpb=_AluIntervalFreqOffsetStdDevPpb_Object((1,3,6,1,4,1,6527,6,2,2,2,2,11,1,8),_AluIntervalFreqOffsetStdDevPpb_Type())
aluIntervalFreqOffsetStdDevPpb.setMaxAccess(_C)
if mibBuilder.loadTexts:aluIntervalFreqOffsetStdDevPpb.setStatus(_A)
_AluExtTmnxDS1Table_Object=MibTable
aluExtTmnxDS1Table=_AluExtTmnxDS1Table_Object((1,3,6,1,4,1,6527,6,2,2,2,2,12))
if mibBuilder.loadTexts:aluExtTmnxDS1Table.setStatus(_A)
_AluExtTmnxDS1Entry_Object=MibTableRow
aluExtTmnxDS1Entry=_AluExtTmnxDS1Entry_Object((1,3,6,1,4,1,6527,6,2,2,2,2,12,1))
if mibBuilder.loadTexts:aluExtTmnxDS1Entry.setStatus(_A)
class _AluExtDS1SignalBitsState_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(64,64));fixedLength=64
_AluExtDS1SignalBitsState_Type.__name__=_e
_AluExtDS1SignalBitsState_Object=MibTableColumn
aluExtDS1SignalBitsState=_AluExtDS1SignalBitsState_Object((1,3,6,1,4,1,6527,6,2,2,2,2,12,1,3),_AluExtDS1SignalBitsState_Type())
aluExtDS1SignalBitsState.setMaxAccess(_C)
if mibBuilder.loadTexts:aluExtDS1SignalBitsState.setStatus(_A)
_AluExtPethPsePortTable_Object=MibTable
aluExtPethPsePortTable=_AluExtPethPsePortTable_Object((1,3,6,1,4,1,6527,6,2,2,2,2,13))
if mibBuilder.loadTexts:aluExtPethPsePortTable.setStatus(_A)
_AluExtPethPsePortEntry_Object=MibTableRow
aluExtPethPsePortEntry=_AluExtPethPsePortEntry_Object((1,3,6,1,4,1,6527,6,2,2,2,2,13,1))
if mibBuilder.loadTexts:aluExtPethPsePortEntry.setStatus(_A)
class _AluExtPethPsePortFaultReason_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14)));namedValues=NamedValues(*((_O,1),('dcp',2),('hicap',3),('rlow',4),('detok',5),('rhigh',6),('open',7),('dcn',8),('tstart',9),('icv',10),('tcut',11),('dis',12),('sup',13),('pdeny',14)))
_AluExtPethPsePortFaultReason_Type.__name__=_E
_AluExtPethPsePortFaultReason_Object=MibTableColumn
aluExtPethPsePortFaultReason=_AluExtPethPsePortFaultReason_Object((1,3,6,1,4,1,6527,6,2,2,2,2,13,1,1),_AluExtPethPsePortFaultReason_Type())
aluExtPethPsePortFaultReason.setMaxAccess(_C)
if mibBuilder.loadTexts:aluExtPethPsePortFaultReason.setStatus(_A)
class _AluExtPethPsePortPowerLevel_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_O,1),('standard',2),('plus',3)))
_AluExtPethPsePortPowerLevel_Type.__name__=_E
_AluExtPethPsePortPowerLevel_Object=MibTableColumn
aluExtPethPsePortPowerLevel=_AluExtPethPsePortPowerLevel_Object((1,3,6,1,4,1,6527,6,2,2,2,2,13,1,2),_AluExtPethPsePortPowerLevel_Type())
aluExtPethPsePortPowerLevel.setMaxAccess(_D)
if mibBuilder.loadTexts:aluExtPethPsePortPowerLevel.setStatus(_A)
class _AluExtPethPsePortOperStatus_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_P,1),('on',2),('off',3)))
_AluExtPethPsePortOperStatus_Type.__name__=_E
_AluExtPethPsePortOperStatus_Object=MibTableColumn
aluExtPethPsePortOperStatus=_AluExtPethPsePortOperStatus_Object((1,3,6,1,4,1,6527,6,2,2,2,2,13,1,3),_AluExtPethPsePortOperStatus_Type())
aluExtPethPsePortOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:aluExtPethPsePortOperStatus.setStatus(_A)
_PethPsePortEventInfo_Type=OctetString
_PethPsePortEventInfo_Object=MibScalar
pethPsePortEventInfo=_PethPsePortEventInfo_Object((1,3,6,1,4,1,6527,6,2,2,2,2,14),_PethPsePortEventInfo_Type())
pethPsePortEventInfo.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:pethPsePortEventInfo.setStatus(_A)
_TmnxVirtualPortTable_Object=MibTable
tmnxVirtualPortTable=_TmnxVirtualPortTable_Object((1,3,6,1,4,1,6527,6,2,2,2,2,15))
if mibBuilder.loadTexts:tmnxVirtualPortTable.setStatus(_A)
_TmnxVirtualPortEntry_Object=MibTableRow
tmnxVirtualPortEntry=_TmnxVirtualPortEntry_Object((1,3,6,1,4,1,6527,6,2,2,2,2,15,1))
tmnxVirtualPortEntry.setIndexNames((0,_F,_G),(0,_B,_o))
if mibBuilder.loadTexts:tmnxVirtualPortEntry.setStatus(_A)
_TmnxVirtualPortPortID_Type=TmnxPortID
_TmnxVirtualPortPortID_Object=MibTableColumn
tmnxVirtualPortPortID=_TmnxVirtualPortPortID_Object((1,3,6,1,4,1,6527,6,2,2,2,2,15,1,1),_TmnxVirtualPortPortID_Type())
tmnxVirtualPortPortID.setMaxAccess(_J)
if mibBuilder.loadTexts:tmnxVirtualPortPortID.setStatus(_A)
class _TmnxVirtualPortInUse_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('not-in-use',1),('mirror',2),('macswap',3),('testhead',4)))
_TmnxVirtualPortInUse_Type.__name__=_E
_TmnxVirtualPortInUse_Object=MibTableColumn
tmnxVirtualPortInUse=_TmnxVirtualPortInUse_Object((1,3,6,1,4,1,6527,6,2,2,2,2,15,1,2),_TmnxVirtualPortInUse_Type())
tmnxVirtualPortInUse.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxVirtualPortInUse.setStatus(_A)
class _TmnxVirtualPortSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('one-gig',1),('ten-gig',2)))
_TmnxVirtualPortSpeed_Type.__name__=_E
_TmnxVirtualPortSpeed_Object=MibTableColumn
tmnxVirtualPortSpeed=_TmnxVirtualPortSpeed_Object((1,3,6,1,4,1,6527,6,2,2,2,2,15,1,3),_TmnxVirtualPortSpeed_Type())
tmnxVirtualPortSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxVirtualPortSpeed.setStatus(_A)
_TmnxSASPortNotificationObjects_ObjectIdentity=ObjectIdentity
tmnxSASPortNotificationObjects=_TmnxSASPortNotificationObjects_ObjectIdentity((1,3,6,1,4,1,6527,6,2,2,2,3))
_TmnxSASPortStatsObjs_ObjectIdentity=ObjectIdentity
tmnxSASPortStatsObjs=_TmnxSASPortStatsObjs_ObjectIdentity((1,3,6,1,4,1,6527,6,2,2,2,4))
tmnxPortEntry.registerAugmentions((_B,_p))
sasTmnxPortExtnEntry.setIndexNames(*tmnxPortEntry.getIndexNames())
tmnxPortEtherEntry.registerAugmentions((_B,_q))
sasTmnxPortEtherExtnEntry.setIndexNames(*tmnxPortEtherEntry.getIndexNames())
tmnxDS1PortEntry.registerAugmentions((_B,_r))
aluExtTmnxDS1PortEntry.setIndexNames(*tmnxDS1PortEntry.getIndexNames())
tmnxDS1Entry.registerAugmentions((_B,_s))
aluExtTmnxDS1Entry.setIndexNames(*tmnxDS1Entry.getIndexNames())
pethPsePortEntry.registerAugmentions((_B,_t))
aluExtPethPsePortEntry.setIndexNames(*pethPsePortEntry.getIndexNames())
tmnxSASPortV1v0Group=ObjectGroup((1,3,6,1,4,1,6527,6,2,2,1,2,2,1))
tmnxSASPortV1v0Group.setObjects(*((_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF)))
if mibBuilder.loadTexts:tmnxSASPortV1v0Group.setStatus(_A)
tmnxSASPortV1v1Group=ObjectGroup((1,3,6,1,4,1,6527,6,2,2,1,2,2,2))
tmnxSASPortV1v1Group.setObjects(*((_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c)))
if mibBuilder.loadTexts:tmnxSASPortV1v1Group.setStatus(_A)
tmnxSASPortV2v0Group=ObjectGroup((1,3,6,1,4,1,6527,6,2,2,1,2,2,3))
tmnxSASPortV2v0Group.setObjects(*((_B,_AG),(_B,_AH)))
if mibBuilder.loadTexts:tmnxSASPortV2v0Group.setStatus(_A)
aluPortAcrClkStatsGroup=ObjectGroup((1,3,6,1,4,1,6527,6,2,2,1,2,2,4))
aluPortAcrClkStatsGroup.setObjects(*((_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR),(_B,_AS),(_B,_AT),(_B,_Q),(_B,_AU),(_B,_AV),(_B,_AW),(_B,_AX),(_B,_AY),(_B,_AZ),(_B,_Aa)))
if mibBuilder.loadTexts:aluPortAcrClkStatsGroup.setStatus(_A)
tmnxSASPortV4v0Group=ObjectGroup((1,3,6,1,4,1,6527,6,2,2,1,2,2,5))
tmnxSASPortV4v0Group.setObjects(*((_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_Ab),(_B,_d),(_B,_Ac),(_B,_Ad),(_B,_Ae),(_B,_Af),(_B,_Ag),(_B,_Ah)))
if mibBuilder.loadTexts:tmnxSASPortV4v0Group.setStatus(_A)
tmnxSASPortV3v0Group=ObjectGroup((1,3,6,1,4,1,6527,6,2,2,1,2,2,6))
tmnxSASPortV3v0Group.setObjects((_B,_d))
if mibBuilder.loadTexts:tmnxSASPortV3v0Group.setStatus(_A)
tmnxSASPortV5v0Group=ObjectGroup((1,3,6,1,4,1,6527,6,2,2,1,2,2,7))
tmnxSASPortV5v0Group.setObjects((_B,_Ai))
if mibBuilder.loadTexts:tmnxSASPortV5v0Group.setStatus(_A)
tmnxSASPortV6v0Group=ObjectGroup((1,3,6,1,4,1,6527,6,2,2,1,2,2,8))
tmnxSASPortV6v0Group.setObjects((_B,_Aj))
if mibBuilder.loadTexts:tmnxSASPortV6v0Group.setStatus(_A)
aluExtPethPsePortStatusChange=NotificationType((1,3,6,1,4,1,6527,6,2,2,2,3,1))
aluExtPethPsePortStatusChange.setObjects(*((_M,_f),(_M,_g),(_B,_Ak),(_B,_Al),(_H,_h)))
if mibBuilder.loadTexts:aluExtPethPsePortStatusChange.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'tmnxSASPortMIBModule':tmnxSASPortMIBModule,'tmnxSASPortConformance':tmnxSASPortConformance,'tmnxSASPortCompliances':tmnxSASPortCompliances,'tmnxSASPortGroups':tmnxSASPortGroups,'tmnxSASPortV1v0Group':tmnxSASPortV1v0Group,'tmnxSASPortV1v1Group':tmnxSASPortV1v1Group,'tmnxSASPortV2v0Group':tmnxSASPortV2v0Group,'aluPortAcrClkStatsGroup':aluPortAcrClkStatsGroup,'tmnxSASPortV4v0Group':tmnxSASPortV4v0Group,'tmnxSASPortV3v0Group':tmnxSASPortV3v0Group,'tmnxSASPortV5v0Group':tmnxSASPortV5v0Group,'tmnxSASPortV6v0Group':tmnxSASPortV6v0Group,'tmnxSASPortObjs':tmnxSASPortObjs,'sasTmnxPortExtnTable':sasTmnxPortExtnTable,_p:sasTmnxPortExtnEntry,_u:tmnxPortUplinkMode,_v:tmnxPortAccessEgressQoSPolicyId,_w:tmnxPortNetworkQoSPolicyId,_x:tmnxPortShgName,'tmnxPortUseDei':tmnxPortUseDei,'tmnxPortOperGrpName':tmnxPortOperGrpName,'tmnxPortMonitorOperGrpName':tmnxPortMonitorOperGrpName,'tmnxSASPortNetIngressStatsTable':tmnxSASPortNetIngressStatsTable,'tmnxSASPortNetIngressStatsEntry':tmnxSASPortNetIngressStatsEntry,_j:tmnxSASPortNetIngressMeterIndex,_A2:tmnxSASPortNetIngressFwdInProfPkts,_A3:tmnxSASPortNetIngressFwdOutProfPkts,_A4:tmnxSASPortNetIngressFwdInProfOcts,_A5:tmnxSASPortNetIngressFwdOutProfOcts,'sasTmnxPortEtherExtnTable':sasTmnxPortEtherExtnTable,_q:sasTmnxPortEtherExtnEntry,_A6:tmnxPortEtherEgressMaxBurst,_A7:tmnxPortStatsQueue1PktsFwd,_A8:tmnxPortStatsQueue2PktsFwd,_A9:tmnxPortStatsQueue3PktsFwd,_AA:tmnxPortStatsQueue4PktsFwd,_AB:tmnxPortStatsQueue5PktsFwd,_AC:tmnxPortStatsQueue6PktsFwd,_AD:tmnxPortStatsQueue7PktsFwd,_AE:tmnxPortStatsQueue8PktsFwd,_AH:tmnxPortEtherEgrSchedMode,_AF:tmnxPortEtherLoopback,_Ab:tmnxPortEtherIpMTU,_d:tmnxPortEtherClockConfig,_Ac:tmnxPortLoopbckServId,_Ad:tmnxPortLoopbckSapPortId,_Ae:tmnxPortLoopbckSapEncapVal,_Af:tmnxPortLoopbckSrcMacAddr,_Ag:tmnxPortLoopbckDstMacAddr,_Ah:tmnxPortAccEgrSapQosMarking,_Ai:tmnxPortLldpTnlNrstBrdgeDstMac,'tmnxPortEtherDe1OutProfile':tmnxPortEtherDe1OutProfile,_Aj:tmnxPortEtherNwAggRateLimit,'tmnxPortEtherNwAggRateLimitCir':tmnxPortEtherNwAggRateLimitCir,'tmnxPortEtherNwAggRateLimitPir':tmnxPortEtherNwAggRateLimitPir,'tmnxPortEtherDcommStatus':tmnxPortEtherDcommStatus,'tmnxPortEtherMulticastIngress':tmnxPortEtherMulticastIngress,'portShgInfoTable':portShgInfoTable,'portShgInfoEntry':portShgInfoEntry,_k:portShgName,_y:portShgRowStatus,_z:portShgInstanceId,_A0:portShgDescription,_A1:portShgLastMgmtChange,'tmnxPortAccessEgressQueueStatsTable':tmnxPortAccessEgressQueueStatsTable,'tmnxPortAccessEgressQueueStatsEntry':tmnxPortAccessEgressQueueStatsEntry,_m:tmnxPortAccessEgressQueueStatsIndex,_R:tmnxPortAccessEgressQueueStatsFwdPkts,_S:tmnxPortAccessEgressQueueStatsFwdOcts,_T:tmnxPortAccessEgressQueueStatsDroPkts,_U:tmnxPortAccessEgressQueueStatsDroOcts,'tmnxPortNetEgressQueueStatsTable':tmnxPortNetEgressQueueStatsTable,'tmnxPortNetEgressQueueStatsEntry':tmnxPortNetEgressQueueStatsEntry,_n:tmnxPortNetEgressQueueStatsIndex,_V:tmnxPortNetEgressQueueStatsFwdPkts,_W:tmnxPortNetEgressQueueStatsFwdOcts,_X:tmnxPortNetEgressQueueStatsDroPkts,_Y:tmnxPortNetEgressQueueStatsDroOcts,_Z:tmnxPortNetEgressQueueStatsInProfDroPkts,_a:tmnxPortNetEgressQueueStatsInProfDroOcts,_b:tmnxPortNetEgressQueueStatsOutProfDroPkts,_c:tmnxPortNetEgressQueueStatsOutProfDroOcts,'aluExtTmnxDS1PortTable':aluExtTmnxDS1PortTable,_r:aluExtTmnxDS1PortEntry,_AG:aluExtDS1PortLineImpedance,'aluPortAcrClkStatsTable':aluPortAcrClkStatsTable,'aluPortAcrClkStatsEntry':aluPortAcrClkStatsEntry,_AI:aluLastUpdateTime,_AJ:aluTotalMinutesIn24Hour,_AK:aluCurrent24HourFreqOffsetMeanPpb,_AL:aluCurrent24HourFreqOffsetStdDevPpb,_AM:aluMaxShortIntervalMinutes,_AN:aluTotalShortIntervalMinutes,_AO:aluCurrent1MinValidData,_AP:aluCurrent1MinPhaseErrorMeanPpb,_AQ:aluCurrent1MinPhaseErrorStdDevNs,_AR:aluCurrent1MinPhaseErrorMeanNs,_AS:aluCurrent1MinFreqOffsetMeanPpb,_AT:aluCurrent1MinFreqOffsetStdDevPpb,'aluPortAcrClkStatsShortIntervalTable':aluPortAcrClkStatsShortIntervalTable,'aluPortAcrClkStatsShortIntervalEntry':aluPortAcrClkStatsShortIntervalEntry,_Q:aluIntervalNumber,_AU:aluIntervalValidData,_AV:aluIntervalUpdateTime,_AW:aluIntervalPhaseErrorMeanPpb,_AX:aluIntervalPhaseErrorStdDevNs,_AY:aluIntervalPhaseErrorMeanNs,_AZ:aluIntervalFreqOffsetMeanPpb,_Aa:aluIntervalFreqOffsetStdDevPpb,'aluExtTmnxDS1Table':aluExtTmnxDS1Table,_s:aluExtTmnxDS1Entry,'aluExtDS1SignalBitsState':aluExtDS1SignalBitsState,'aluExtPethPsePortTable':aluExtPethPsePortTable,_t:aluExtPethPsePortEntry,_Ak:aluExtPethPsePortFaultReason,'aluExtPethPsePortPowerLevel':aluExtPethPsePortPowerLevel,_Al:aluExtPethPsePortOperStatus,'pethPsePortEventInfo':pethPsePortEventInfo,'tmnxVirtualPortTable':tmnxVirtualPortTable,'tmnxVirtualPortEntry':tmnxVirtualPortEntry,_o:tmnxVirtualPortPortID,'tmnxVirtualPortInUse':tmnxVirtualPortInUse,'tmnxVirtualPortSpeed':tmnxVirtualPortSpeed,'tmnxSASPortNotificationObjects':tmnxSASPortNotificationObjects,'aluExtPethPsePortStatusChange':aluExtPethPsePortStatusChange,'tmnxSASPortStatsObjs':tmnxSASPortStatsObjs})