_h='rdnPktRKSVersionID'
_g='rdnPktRKSPortSecondary'
_f='rdnPktRKSIPSecondary'
_e='rdnPktRKSPortPrimary'
_d='rdnPktRKSIPPrimary'
_c='rdnPktRKSTransID'
_b='rdnPktRKSReason'
_a='rdnPktESDFPortNum'
_Z='rdnPktESDFIpAddr'
_Y='rdnPktESReason'
_X='rdnPktDQoSEmergencyPreemptReason'
_W='rdnPktDQoSEmergencyReason'
_V='rdnPktDQoSResReqReason'
_U='rdnPktDQoSCopsCmsIpAddr'
_T='rdnPktDQoSCopsReason'
_S='rdnPktDQoSCopsHandle'
_R='rdnPktCMSIpAddressIndex'
_Q='rdnGateDirection'
_P='2006-05-24 00:00'
_O='rdnPktDQoSGateId'
_N='rdnPktDQoSClassName'
_M='rdnGateId'
_L='DisplayString'
_K='rdnPktDQoSCmMacAddr'
_J='not-accessible'
_I='enabled'
_H='disabled'
_G='obsolete'
_F='accessible-for-notify'
_E='read-write'
_D='Integer32'
_C='RDN-PKTCABLE-GROUP-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
riverdelta,=mibBuilder.importSymbols('RDN-MIB','riverdelta')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_L,'MacAddress','PhysAddress','TextualConvention','TruthValue')
rdnPacketCableGroup=ModuleIdentity((1,3,6,1,4,1,4981,7))
if mibBuilder.loadTexts:rdnPacketCableGroup.setRevisions(('2008-10-06 00:00','2008-08-08 00:00','2007-10-22 00:00',_P,_P,'2006-02-15 00:00','2006-01-24 00:00','2003-11-05 00:00','2003-10-24 00:00','2003-05-12 00:00','2002-09-06 00:00'))
class BcidDataArray(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,24))
_RdnPktDQoSConfigGroup_ObjectIdentity=ObjectIdentity
rdnPktDQoSConfigGroup=_RdnPktDQoSConfigGroup_ObjectIdentity((1,3,6,1,4,1,4981,7,1))
_RdnPktDQoSCOPSStatus_Type=TruthValue
_RdnPktDQoSCOPSStatus_Object=MibScalar
rdnPktDQoSCOPSStatus=_RdnPktDQoSCOPSStatus_Object((1,3,6,1,4,1,4981,7,1,1),_RdnPktDQoSCOPSStatus_Type())
rdnPktDQoSCOPSStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:rdnPktDQoSCOPSStatus.setStatus(_A)
_RdnPktDQoSCMTSIp_Type=IpAddress
_RdnPktDQoSCMTSIp_Object=MibScalar
rdnPktDQoSCMTSIp=_RdnPktDQoSCMTSIp_Object((1,3,6,1,4,1,4981,7,1,2),_RdnPktDQoSCMTSIp_Type())
rdnPktDQoSCMTSIp.setMaxAccess(_E)
if mibBuilder.loadTexts:rdnPktDQoSCMTSIp.setStatus(_A)
class _RdnPktDQoSPEPID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_RdnPktDQoSPEPID_Type.__name__=_L
_RdnPktDQoSPEPID_Object=MibScalar
rdnPktDQoSPEPID=_RdnPktDQoSPEPID_Object((1,3,6,1,4,1,4981,7,1,3),_RdnPktDQoSPEPID_Type())
rdnPktDQoSPEPID.setMaxAccess(_E)
if mibBuilder.loadTexts:rdnPktDQoSPEPID.setStatus(_A)
class _RdnPktDQoSClientAccpTimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3600000))
_RdnPktDQoSClientAccpTimer_Type.__name__=_D
_RdnPktDQoSClientAccpTimer_Object=MibScalar
rdnPktDQoSClientAccpTimer=_RdnPktDQoSClientAccpTimer_Object((1,3,6,1,4,1,4981,7,1,4),_RdnPktDQoSClientAccpTimer_Type())
rdnPktDQoSClientAccpTimer.setMaxAccess(_E)
if mibBuilder.loadTexts:rdnPktDQoSClientAccpTimer.setStatus(_A)
class _RdnPktDQoST0Timer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3600))
_RdnPktDQoST0Timer_Type.__name__=_D
_RdnPktDQoST0Timer_Object=MibScalar
rdnPktDQoST0Timer=_RdnPktDQoST0Timer_Object((1,3,6,1,4,1,4981,7,1,5),_RdnPktDQoST0Timer_Type())
rdnPktDQoST0Timer.setMaxAccess(_E)
if mibBuilder.loadTexts:rdnPktDQoST0Timer.setStatus(_A)
class _RdnPktDQoST1Timer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3600))
_RdnPktDQoST1Timer_Type.__name__=_D
_RdnPktDQoST1Timer_Object=MibScalar
rdnPktDQoST1Timer=_RdnPktDQoST1Timer_Object((1,3,6,1,4,1,4981,7,1,6),_RdnPktDQoST1Timer_Type())
rdnPktDQoST1Timer.setMaxAccess(_E)
if mibBuilder.loadTexts:rdnPktDQoST1Timer.setStatus(_A)
_RdnPktDQoST3Timer_Type=Integer32
_RdnPktDQoST3Timer_Object=MibScalar
rdnPktDQoST3Timer=_RdnPktDQoST3Timer_Object((1,3,6,1,4,1,4981,7,1,7),_RdnPktDQoST3Timer_Type())
rdnPktDQoST3Timer.setMaxAccess(_E)
if mibBuilder.loadTexts:rdnPktDQoST3Timer.setStatus(_A)
_RdnPktDQoST6Timer_Type=Integer32
_RdnPktDQoST6Timer_Object=MibScalar
rdnPktDQoST6Timer=_RdnPktDQoST6Timer_Object((1,3,6,1,4,1,4981,7,1,8),_RdnPktDQoST6Timer_Type())
rdnPktDQoST6Timer.setMaxAccess(_E)
if mibBuilder.loadTexts:rdnPktDQoST6Timer.setStatus(_A)
class _RdnPktDQoSCopsTrapEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_H,2)))
_RdnPktDQoSCopsTrapEnable_Type.__name__=_D
_RdnPktDQoSCopsTrapEnable_Object=MibScalar
rdnPktDQoSCopsTrapEnable=_RdnPktDQoSCopsTrapEnable_Object((1,3,6,1,4,1,4981,7,1,9),_RdnPktDQoSCopsTrapEnable_Type())
rdnPktDQoSCopsTrapEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:rdnPktDQoSCopsTrapEnable.setStatus(_A)
class _RdnPktDQoSResReqTrapEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_H,2)))
_RdnPktDQoSResReqTrapEnable_Type.__name__=_D
_RdnPktDQoSResReqTrapEnable_Object=MibScalar
rdnPktDQoSResReqTrapEnable=_RdnPktDQoSResReqTrapEnable_Object((1,3,6,1,4,1,4981,7,1,10),_RdnPktDQoSResReqTrapEnable_Type())
rdnPktDQoSResReqTrapEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:rdnPktDQoSResReqTrapEnable.setStatus(_A)
class _RdnPktESTrapEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_H,2)))
_RdnPktESTrapEnable_Type.__name__=_D
_RdnPktESTrapEnable_Object=MibScalar
rdnPktESTrapEnable=_RdnPktESTrapEnable_Object((1,3,6,1,4,1,4981,7,1,11),_RdnPktESTrapEnable_Type())
rdnPktESTrapEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:rdnPktESTrapEnable.setStatus(_A)
class _RdnPktESEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_H,2)))
_RdnPktESEnable_Type.__name__=_D
_RdnPktESEnable_Object=MibScalar
rdnPktESEnable=_RdnPktESEnable_Object((1,3,6,1,4,1,4981,7,1,12),_RdnPktESEnable_Type())
rdnPktESEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:rdnPktESEnable.setStatus(_A)
class _RdnPktDQoSEmergencyTrapEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_H,2)))
_RdnPktDQoSEmergencyTrapEnable_Type.__name__=_D
_RdnPktDQoSEmergencyTrapEnable_Object=MibScalar
rdnPktDQoSEmergencyTrapEnable=_RdnPktDQoSEmergencyTrapEnable_Object((1,3,6,1,4,1,4981,7,1,13),_RdnPktDQoSEmergencyTrapEnable_Type())
rdnPktDQoSEmergencyTrapEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:rdnPktDQoSEmergencyTrapEnable.setStatus(_A)
class _RdnPktDQoSEmergencyPreemption_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_H,0),('most-recent',1),('oldest',2),('random',3)))
_RdnPktDQoSEmergencyPreemption_Type.__name__=_D
_RdnPktDQoSEmergencyPreemption_Object=MibScalar
rdnPktDQoSEmergencyPreemption=_RdnPktDQoSEmergencyPreemption_Object((1,3,6,1,4,1,4981,7,1,14),_RdnPktDQoSEmergencyPreemption_Type())
rdnPktDQoSEmergencyPreemption.setMaxAccess(_E)
if mibBuilder.loadTexts:rdnPktDQoSEmergencyPreemption.setStatus(_A)
class _RdnPktEMRKSFailureTrapEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_H,2)))
_RdnPktEMRKSFailureTrapEnable_Type.__name__=_D
_RdnPktEMRKSFailureTrapEnable_Object=MibScalar
rdnPktEMRKSFailureTrapEnable=_RdnPktEMRKSFailureTrapEnable_Object((1,3,6,1,4,1,4981,7,1,15),_RdnPktEMRKSFailureTrapEnable_Type())
rdnPktEMRKSFailureTrapEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:rdnPktEMRKSFailureTrapEnable.setStatus(_A)
class _RdnPktDQoSDscp_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_RdnPktDQoSDscp_Type.__name__=_D
_RdnPktDQoSDscp_Object=MibScalar
rdnPktDQoSDscp=_RdnPktDQoSDscp_Object((1,3,6,1,4,1,4981,7,1,16),_RdnPktDQoSDscp_Type())
rdnPktDQoSDscp.setMaxAccess(_E)
if mibBuilder.loadTexts:rdnPktDQoSDscp.setStatus(_A)
class _RdnPktMMDscp_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_RdnPktMMDscp_Type.__name__=_D
_RdnPktMMDscp_Object=MibScalar
rdnPktMMDscp=_RdnPktMMDscp_Object((1,3,6,1,4,1,4981,7,1,17),_RdnPktMMDscp_Type())
rdnPktMMDscp.setMaxAccess(_E)
if mibBuilder.loadTexts:rdnPktMMDscp.setStatus(_A)
class _RdnPktEMDscp_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_RdnPktEMDscp_Type.__name__=_D
_RdnPktEMDscp_Object=MibScalar
rdnPktEMDscp=_RdnPktEMDscp_Object((1,3,6,1,4,1,4981,7,1,18),_RdnPktEMDscp_Type())
rdnPktEMDscp.setMaxAccess(_E)
if mibBuilder.loadTexts:rdnPktEMDscp.setStatus(_A)
class _RdnPktESCccDscp_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_RdnPktESCccDscp_Type.__name__=_D
_RdnPktESCccDscp_Object=MibScalar
rdnPktESCccDscp=_RdnPktESCccDscp_Object((1,3,6,1,4,1,4981,7,1,19),_RdnPktESCccDscp_Type())
rdnPktESCccDscp.setMaxAccess(_E)
if mibBuilder.loadTexts:rdnPktESCccDscp.setStatus(_A)
_RdnGateStatsTable_Object=MibTable
rdnGateStatsTable=_RdnGateStatsTable_Object((1,3,6,1,4,1,4981,7,2))
if mibBuilder.loadTexts:rdnGateStatsTable.setStatus(_A)
_RdnGateStatsEntry_Object=MibTableRow
rdnGateStatsEntry=_RdnGateStatsEntry_Object((1,3,6,1,4,1,4981,7,2,1))
rdnGateStatsEntry.setIndexNames((0,_C,_M))
if mibBuilder.loadTexts:rdnGateStatsEntry.setStatus(_A)
_RdnGateId_Type=Integer32
_RdnGateId_Object=MibTableColumn
rdnGateId=_RdnGateId_Object((1,3,6,1,4,1,4981,7,2,1,1),_RdnGateId_Type())
rdnGateId.setMaxAccess(_J)
if mibBuilder.loadTexts:rdnGateId.setStatus(_A)
class _RdnGateStatsState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,7,8,9)));namedValues=NamedValues(*(('idle',0),('start',1),('allocated',2),('authorized',3),('reserved',4),('committed',7),('committedRecovery',8),('numOfStates',9)))
_RdnGateStatsState_Type.__name__=_D
_RdnGateStatsState_Object=MibTableColumn
rdnGateStatsState=_RdnGateStatsState_Object((1,3,6,1,4,1,4981,7,2,1,2),_RdnGateStatsState_Type())
rdnGateStatsState.setMaxAccess(_B)
if mibBuilder.loadTexts:rdnGateStatsState.setStatus(_A)
_RdnGateStatsSubscriberIP_Type=IpAddress
_RdnGateStatsSubscriberIP_Object=MibTableColumn
rdnGateStatsSubscriberIP=_RdnGateStatsSubscriberIP_Object((1,3,6,1,4,1,4981,7,2,1,3),_RdnGateStatsSubscriberIP_Type())
rdnGateStatsSubscriberIP.setMaxAccess(_B)
if mibBuilder.loadTexts:rdnGateStatsSubscriberIP.setStatus(_A)
_RdnGateStatsRKSPrimaryAddr_Type=IpAddress
_RdnGateStatsRKSPrimaryAddr_Object=MibTableColumn
rdnGateStatsRKSPrimaryAddr=_RdnGateStatsRKSPrimaryAddr_Object((1,3,6,1,4,1,4981,7,2,1,4),_RdnGateStatsRKSPrimaryAddr_Type())
rdnGateStatsRKSPrimaryAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:rdnGateStatsRKSPrimaryAddr.setStatus(_A)
_RdnGateStatsRKSPrimaryPort_Type=Integer32
_RdnGateStatsRKSPrimaryPort_Object=MibTableColumn
rdnGateStatsRKSPrimaryPort=_RdnGateStatsRKSPrimaryPort_Object((1,3,6,1,4,1,4981,7,2,1,5),_RdnGateStatsRKSPrimaryPort_Type())
rdnGateStatsRKSPrimaryPort.setMaxAccess(_B)
if mibBuilder.loadTexts:rdnGateStatsRKSPrimaryPort.setStatus(_A)
_RdnGateStatsRKSSecondaryAddr_Type=IpAddress
_RdnGateStatsRKSSecondaryAddr_Object=MibTableColumn
rdnGateStatsRKSSecondaryAddr=_RdnGateStatsRKSSecondaryAddr_Object((1,3,6,1,4,1,4981,7,2,1,6),_RdnGateStatsRKSSecondaryAddr_Type())
rdnGateStatsRKSSecondaryAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:rdnGateStatsRKSSecondaryAddr.setStatus(_A)
_RdnGateStatsRKSSecondaryPort_Type=Integer32
_RdnGateStatsRKSSecondaryPort_Object=MibTableColumn
rdnGateStatsRKSSecondaryPort=_RdnGateStatsRKSSecondaryPort_Object((1,3,6,1,4,1,4981,7,2,1,7),_RdnGateStatsRKSSecondaryPort_Type())
rdnGateStatsRKSSecondaryPort.setMaxAccess(_B)
if mibBuilder.loadTexts:rdnGateStatsRKSSecondaryPort.setStatus(_A)
_RdnGateStatsEventFlag_Type=Integer32
_RdnGateStatsEventFlag_Object=MibTableColumn
rdnGateStatsEventFlag=_RdnGateStatsEventFlag_Object((1,3,6,1,4,1,4981,7,2,1,8),_RdnGateStatsEventFlag_Type())
rdnGateStatsEventFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:rdnGateStatsEventFlag.setStatus(_A)
_RdnGateStatsBillingCorrelationID_Type=BcidDataArray
_RdnGateStatsBillingCorrelationID_Object=MibTableColumn
rdnGateStatsBillingCorrelationID=_RdnGateStatsBillingCorrelationID_Object((1,3,6,1,4,1,4981,7,2,1,9),_RdnGateStatsBillingCorrelationID_Type())
rdnGateStatsBillingCorrelationID.setMaxAccess(_B)
if mibBuilder.loadTexts:rdnGateStatsBillingCorrelationID.setStatus(_A)
_RdnGateStatsDurationTime_Type=DisplayString
_RdnGateStatsDurationTime_Object=MibTableColumn
rdnGateStatsDurationTime=_RdnGateStatsDurationTime_Object((1,3,6,1,4,1,4981,7,2,1,10),_RdnGateStatsDurationTime_Type())
rdnGateStatsDurationTime.setMaxAccess(_B)
if mibBuilder.loadTexts:rdnGateStatsDurationTime.setStatus(_A)
_RdnGateStatsSlotNum_Type=Integer32
_RdnGateStatsSlotNum_Object=MibTableColumn
rdnGateStatsSlotNum=_RdnGateStatsSlotNum_Object((1,3,6,1,4,1,4981,7,2,1,11),_RdnGateStatsSlotNum_Type())
rdnGateStatsSlotNum.setMaxAccess(_B)
if mibBuilder.loadTexts:rdnGateStatsSlotNum.setStatus(_A)
_RdnGateStatsUpSfid_Type=Integer32
_RdnGateStatsUpSfid_Object=MibTableColumn
rdnGateStatsUpSfid=_RdnGateStatsUpSfid_Object((1,3,6,1,4,1,4981,7,2,1,12),_RdnGateStatsUpSfid_Type())
rdnGateStatsUpSfid.setMaxAccess(_B)
if mibBuilder.loadTexts:rdnGateStatsUpSfid.setStatus(_A)
_RdnGateStatsDnSfid_Type=Integer32
_RdnGateStatsDnSfid_Object=MibTableColumn
rdnGateStatsDnSfid=_RdnGateStatsDnSfid_Object((1,3,6,1,4,1,4981,7,2,1,13),_RdnGateStatsDnSfid_Type())
rdnGateStatsDnSfid.setMaxAccess(_B)
if mibBuilder.loadTexts:rdnGateStatsDnSfid.setStatus(_A)
_RdnGateStatsResourceID_Type=Integer32
_RdnGateStatsResourceID_Object=MibTableColumn
rdnGateStatsResourceID=_RdnGateStatsResourceID_Object((1,3,6,1,4,1,4981,7,2,1,14),_RdnGateStatsResourceID_Type())
rdnGateStatsResourceID.setMaxAccess(_B)
if mibBuilder.loadTexts:rdnGateStatsResourceID.setStatus(_A)
_RdnGateStatsESCDCAddr_Type=IpAddress
_RdnGateStatsESCDCAddr_Object=MibTableColumn
rdnGateStatsESCDCAddr=_RdnGateStatsESCDCAddr_Object((1,3,6,1,4,1,4981,7,2,1,15),_RdnGateStatsESCDCAddr_Type())
rdnGateStatsESCDCAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:rdnGateStatsESCDCAddr.setStatus(_A)
_RdnGateStatsESCDCPort_Type=Integer32
_RdnGateStatsESCDCPort_Object=MibTableColumn
rdnGateStatsESCDCPort=_RdnGateStatsESCDCPort_Object((1,3,6,1,4,1,4981,7,2,1,16),_RdnGateStatsESCDCPort_Type())
rdnGateStatsESCDCPort.setMaxAccess(_B)
if mibBuilder.loadTexts:rdnGateStatsESCDCPort.setStatus(_A)
_RdnGateStatsESFlag_Type=Integer32
_RdnGateStatsESFlag_Object=MibTableColumn
rdnGateStatsESFlag=_RdnGateStatsESFlag_Object((1,3,6,1,4,1,4981,7,2,1,17),_RdnGateStatsESFlag_Type())
rdnGateStatsESFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:rdnGateStatsESFlag.setStatus(_A)
_RdnGateStatsESCCCAddr_Type=IpAddress
_RdnGateStatsESCCCAddr_Object=MibTableColumn
rdnGateStatsESCCCAddr=_RdnGateStatsESCCCAddr_Object((1,3,6,1,4,1,4981,7,2,1,18),_RdnGateStatsESCCCAddr_Type())
rdnGateStatsESCCCAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:rdnGateStatsESCCCAddr.setStatus(_A)
_RdnGateStatsESCCCPort_Type=Integer32
_RdnGateStatsESCCCPort_Object=MibTableColumn
rdnGateStatsESCCCPort=_RdnGateStatsESCCCPort_Object((1,3,6,1,4,1,4981,7,2,1,19),_RdnGateStatsESCCCPort_Type())
rdnGateStatsESCCCPort.setMaxAccess(_B)
if mibBuilder.loadTexts:rdnGateStatsESCCCPort.setStatus(_A)
_RdnGateStatsESCCCId_Type=Integer32
_RdnGateStatsESCCCId_Object=MibTableColumn
rdnGateStatsESCCCId=_RdnGateStatsESCCCId_Object((1,3,6,1,4,1,4981,7,2,1,20),_RdnGateStatsESCCCId_Type())
rdnGateStatsESCCCId.setMaxAccess(_B)
if mibBuilder.loadTexts:rdnGateStatsESCCCId.setStatus(_A)
_RdnGateSpecTable_Object=MibTable
rdnGateSpecTable=_RdnGateSpecTable_Object((1,3,6,1,4,1,4981,7,3))
if mibBuilder.loadTexts:rdnGateSpecTable.setStatus(_A)
_RdnGateSpecEntry_Object=MibTableRow
rdnGateSpecEntry=_RdnGateSpecEntry_Object((1,3,6,1,4,1,4981,7,3,1))
rdnGateSpecEntry.setIndexNames((0,_C,_M),(0,_C,_Q))
if mibBuilder.loadTexts:rdnGateSpecEntry.setStatus(_A)
class _RdnGateDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('upstream',1),('downstream',2)))
_RdnGateDirection_Type.__name__=_D
_RdnGateDirection_Object=MibTableColumn
rdnGateDirection=_RdnGateDirection_Object((1,3,6,1,4,1,4981,7,3,1,2),_RdnGateDirection_Type())
rdnGateDirection.setMaxAccess(_J)
if mibBuilder.loadTexts:rdnGateDirection.setStatus(_A)
_RdnGateSpecProtocol_Type=Integer32
_RdnGateSpecProtocol_Object=MibTableColumn
rdnGateSpecProtocol=_RdnGateSpecProtocol_Object((1,3,6,1,4,1,4981,7,3,1,3),_RdnGateSpecProtocol_Type())
rdnGateSpecProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:rdnGateSpecProtocol.setStatus(_A)
_RdnGateSpecSourceIP_Type=IpAddress
_RdnGateSpecSourceIP_Object=MibTableColumn
rdnGateSpecSourceIP=_RdnGateSpecSourceIP_Object((1,3,6,1,4,1,4981,7,3,1,4),_RdnGateSpecSourceIP_Type())
rdnGateSpecSourceIP.setMaxAccess(_B)
if mibBuilder.loadTexts:rdnGateSpecSourceIP.setStatus(_A)
_RdnGateSpecSourcePort_Type=Integer32
_RdnGateSpecSourcePort_Object=MibTableColumn
rdnGateSpecSourcePort=_RdnGateSpecSourcePort_Object((1,3,6,1,4,1,4981,7,3,1,5),_RdnGateSpecSourcePort_Type())
rdnGateSpecSourcePort.setMaxAccess(_B)
if mibBuilder.loadTexts:rdnGateSpecSourcePort.setStatus(_A)
_RdnGateSpecDestIP_Type=IpAddress
_RdnGateSpecDestIP_Object=MibTableColumn
rdnGateSpecDestIP=_RdnGateSpecDestIP_Object((1,3,6,1,4,1,4981,7,3,1,6),_RdnGateSpecDestIP_Type())
rdnGateSpecDestIP.setMaxAccess(_B)
if mibBuilder.loadTexts:rdnGateSpecDestIP.setStatus(_A)
_RdnGateSpecDestPort_Type=Integer32
_RdnGateSpecDestPort_Object=MibTableColumn
rdnGateSpecDestPort=_RdnGateSpecDestPort_Object((1,3,6,1,4,1,4981,7,3,1,7),_RdnGateSpecDestPort_Type())
rdnGateSpecDestPort.setMaxAccess(_B)
if mibBuilder.loadTexts:rdnGateSpecDestPort.setStatus(_A)
_RdnGateSpecServiceFlowID_Type=Integer32
_RdnGateSpecServiceFlowID_Object=MibTableColumn
rdnGateSpecServiceFlowID=_RdnGateSpecServiceFlowID_Object((1,3,6,1,4,1,4981,7,3,1,8),_RdnGateSpecServiceFlowID_Type())
rdnGateSpecServiceFlowID.setMaxAccess(_B)
if mibBuilder.loadTexts:rdnGateSpecServiceFlowID.setStatus(_A)
class _RdnGateSpecFlags_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('autoCommit',1),('commitNotAllowed',2)))
_RdnGateSpecFlags_Type.__name__=_D
_RdnGateSpecFlags_Object=MibTableColumn
rdnGateSpecFlags=_RdnGateSpecFlags_Object((1,3,6,1,4,1,4981,7,3,1,9),_RdnGateSpecFlags_Type())
rdnGateSpecFlags.setMaxAccess(_B)
if mibBuilder.loadTexts:rdnGateSpecFlags.setStatus(_A)
class _RdnGateSpecSessionClass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*(('normalPriority',1),('highPriority',2),('unspecified',255)))
_RdnGateSpecSessionClass_Type.__name__=_D
_RdnGateSpecSessionClass_Object=MibTableColumn
rdnGateSpecSessionClass=_RdnGateSpecSessionClass_Object((1,3,6,1,4,1,4981,7,3,1,10),_RdnGateSpecSessionClass_Type())
rdnGateSpecSessionClass.setMaxAccess(_B)
if mibBuilder.loadTexts:rdnGateSpecSessionClass.setStatus(_A)
_RdnGateSpecDiffServCode_Type=Integer32
_RdnGateSpecDiffServCode_Object=MibTableColumn
rdnGateSpecDiffServCode=_RdnGateSpecDiffServCode_Object((1,3,6,1,4,1,4981,7,3,1,11),_RdnGateSpecDiffServCode_Type())
rdnGateSpecDiffServCode.setMaxAccess(_B)
if mibBuilder.loadTexts:rdnGateSpecDiffServCode.setStatus(_A)
_RdnGateSpecT1Timer_Type=Integer32
_RdnGateSpecT1Timer_Object=MibTableColumn
rdnGateSpecT1Timer=_RdnGateSpecT1Timer_Object((1,3,6,1,4,1,4981,7,3,1,12),_RdnGateSpecT1Timer_Type())
rdnGateSpecT1Timer.setMaxAccess(_B)
if mibBuilder.loadTexts:rdnGateSpecT1Timer.setStatus(_A)
_RdnGateSpecTokenBuckRate_Type=Integer32
_RdnGateSpecTokenBuckRate_Object=MibTableColumn
rdnGateSpecTokenBuckRate=_RdnGateSpecTokenBuckRate_Object((1,3,6,1,4,1,4981,7,3,1,13),_RdnGateSpecTokenBuckRate_Type())
rdnGateSpecTokenBuckRate.setMaxAccess(_B)
if mibBuilder.loadTexts:rdnGateSpecTokenBuckRate.setStatus(_A)
_RdnGateSpecBuckSize_Type=Integer32
_RdnGateSpecBuckSize_Object=MibTableColumn
rdnGateSpecBuckSize=_RdnGateSpecBuckSize_Object((1,3,6,1,4,1,4981,7,3,1,14),_RdnGateSpecBuckSize_Type())
rdnGateSpecBuckSize.setMaxAccess(_B)
if mibBuilder.loadTexts:rdnGateSpecBuckSize.setStatus(_A)
_RdnGateSpecPeakDataRate_Type=Integer32
_RdnGateSpecPeakDataRate_Object=MibTableColumn
rdnGateSpecPeakDataRate=_RdnGateSpecPeakDataRate_Object((1,3,6,1,4,1,4981,7,3,1,15),_RdnGateSpecPeakDataRate_Type())
rdnGateSpecPeakDataRate.setMaxAccess(_B)
if mibBuilder.loadTexts:rdnGateSpecPeakDataRate.setStatus(_A)
_RdnGateSpecMinPoliceUnit_Type=Integer32
_RdnGateSpecMinPoliceUnit_Object=MibTableColumn
rdnGateSpecMinPoliceUnit=_RdnGateSpecMinPoliceUnit_Object((1,3,6,1,4,1,4981,7,3,1,16),_RdnGateSpecMinPoliceUnit_Type())
rdnGateSpecMinPoliceUnit.setMaxAccess(_B)
if mibBuilder.loadTexts:rdnGateSpecMinPoliceUnit.setStatus(_A)
_RdnGateSpecMaxPacketSize_Type=Integer32
_RdnGateSpecMaxPacketSize_Object=MibTableColumn
rdnGateSpecMaxPacketSize=_RdnGateSpecMaxPacketSize_Object((1,3,6,1,4,1,4981,7,3,1,17),_RdnGateSpecMaxPacketSize_Type())
rdnGateSpecMaxPacketSize.setMaxAccess(_B)
if mibBuilder.loadTexts:rdnGateSpecMaxPacketSize.setStatus(_A)
_RdnGateSpecReserveRate_Type=Integer32
_RdnGateSpecReserveRate_Object=MibTableColumn
rdnGateSpecReserveRate=_RdnGateSpecReserveRate_Object((1,3,6,1,4,1,4981,7,3,1,18),_RdnGateSpecReserveRate_Type())
rdnGateSpecReserveRate.setMaxAccess(_B)
if mibBuilder.loadTexts:rdnGateSpecReserveRate.setStatus(_A)
_RdnGateSlackTerm_Type=Integer32
_RdnGateSlackTerm_Object=MibTableColumn
rdnGateSlackTerm=_RdnGateSlackTerm_Object((1,3,6,1,4,1,4981,7,3,1,19),_RdnGateSlackTerm_Type())
rdnGateSlackTerm.setMaxAccess(_B)
if mibBuilder.loadTexts:rdnGateSlackTerm.setStatus(_A)
_RdnPktCMSIpConfigTable_Object=MibTable
rdnPktCMSIpConfigTable=_RdnPktCMSIpConfigTable_Object((1,3,6,1,4,1,4981,7,4))
if mibBuilder.loadTexts:rdnPktCMSIpConfigTable.setStatus(_A)
_RdnPktCMSIpConfigEntry_Object=MibTableRow
rdnPktCMSIpConfigEntry=_RdnPktCMSIpConfigEntry_Object((1,3,6,1,4,1,4981,7,4,1))
rdnPktCMSIpConfigEntry.setIndexNames((0,_C,_R))
if mibBuilder.loadTexts:rdnPktCMSIpConfigEntry.setStatus(_A)
_RdnPktCMSIpAddressIndex_Type=Integer32
_RdnPktCMSIpAddressIndex_Object=MibTableColumn
rdnPktCMSIpAddressIndex=_RdnPktCMSIpAddressIndex_Object((1,3,6,1,4,1,4981,7,4,1,1),_RdnPktCMSIpAddressIndex_Type())
rdnPktCMSIpAddressIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:rdnPktCMSIpAddressIndex.setStatus(_A)
_RdnPktCMSIpAddress_Type=IpAddress
_RdnPktCMSIpAddress_Object=MibTableColumn
rdnPktCMSIpAddress=_RdnPktCMSIpAddress_Object((1,3,6,1,4,1,4981,7,4,1,2),_RdnPktCMSIpAddress_Type())
rdnPktCMSIpAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:rdnPktCMSIpAddress.setStatus(_A)
_RdnPktDQoSStatsTable_Object=MibTable
rdnPktDQoSStatsTable=_RdnPktDQoSStatsTable_Object((1,3,6,1,4,1,4981,7,6))
if mibBuilder.loadTexts:rdnPktDQoSStatsTable.setStatus(_A)
_RdnPktDQoSStatsEntry_Object=MibTableRow
rdnPktDQoSStatsEntry=_RdnPktDQoSStatsEntry_Object((1,3,6,1,4,1,4981,7,6,1))
rdnPktDQoSStatsEntry.setIndexNames((0,_C,_S))
if mibBuilder.loadTexts:rdnPktDQoSStatsEntry.setStatus(_A)
_RdnPktDQoSIpAddress_Type=IpAddress
_RdnPktDQoSIpAddress_Object=MibTableColumn
rdnPktDQoSIpAddress=_RdnPktDQoSIpAddress_Object((1,3,6,1,4,1,4981,7,6,1,1),_RdnPktDQoSIpAddress_Type())
rdnPktDQoSIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:rdnPktDQoSIpAddress.setStatus(_A)
_RdnPktDQoSCopsHandle_Type=Integer32
_RdnPktDQoSCopsHandle_Object=MibTableColumn
rdnPktDQoSCopsHandle=_RdnPktDQoSCopsHandle_Object((1,3,6,1,4,1,4981,7,6,1,2),_RdnPktDQoSCopsHandle_Type())
rdnPktDQoSCopsHandle.setMaxAccess(_J)
if mibBuilder.loadTexts:rdnPktDQoSCopsHandle.setStatus(_A)
class _RdnPktDQoSCopsStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('closed',0),('opening',1),('open',2)))
_RdnPktDQoSCopsStatus_Type.__name__=_D
_RdnPktDQoSCopsStatus_Object=MibTableColumn
rdnPktDQoSCopsStatus=_RdnPktDQoSCopsStatus_Object((1,3,6,1,4,1,4981,7,6,1,3),_RdnPktDQoSCopsStatus_Type())
rdnPktDQoSCopsStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rdnPktDQoSCopsStatus.setStatus(_A)
_RdnPktDQoSCopsConnected_Type=Integer32
_RdnPktDQoSCopsConnected_Object=MibTableColumn
rdnPktDQoSCopsConnected=_RdnPktDQoSCopsConnected_Object((1,3,6,1,4,1,4981,7,6,1,4),_RdnPktDQoSCopsConnected_Type())
rdnPktDQoSCopsConnected.setMaxAccess(_B)
if mibBuilder.loadTexts:rdnPktDQoSCopsConnected.setStatus(_A)
_RdnPktDQoSCopsTerminated_Type=Integer32
_RdnPktDQoSCopsTerminated_Object=MibTableColumn
rdnPktDQoSCopsTerminated=_RdnPktDQoSCopsTerminated_Object((1,3,6,1,4,1,4981,7,6,1,5),_RdnPktDQoSCopsTerminated_Type())
rdnPktDQoSCopsTerminated.setMaxAccess(_B)
if mibBuilder.loadTexts:rdnPktDQoSCopsTerminated.setStatus(_A)
_RdnPktDQoSCopsKASent_Type=Integer32
_RdnPktDQoSCopsKASent_Object=MibTableColumn
rdnPktDQoSCopsKASent=_RdnPktDQoSCopsKASent_Object((1,3,6,1,4,1,4981,7,6,1,6),_RdnPktDQoSCopsKASent_Type())
rdnPktDQoSCopsKASent.setMaxAccess(_B)
if mibBuilder.loadTexts:rdnPktDQoSCopsKASent.setStatus(_A)
_RdnPktDQoSCopsKARcvd_Type=Integer32
_RdnPktDQoSCopsKARcvd_Object=MibTableColumn
rdnPktDQoSCopsKARcvd=_RdnPktDQoSCopsKARcvd_Object((1,3,6,1,4,1,4981,7,6,1,7),_RdnPktDQoSCopsKARcvd_Type())
rdnPktDQoSCopsKARcvd.setMaxAccess(_B)
if mibBuilder.loadTexts:rdnPktDQoSCopsKARcvd.setStatus(_A)
_RdnPktDQoSKATimeout_Type=Integer32
_RdnPktDQoSKATimeout_Object=MibTableColumn
rdnPktDQoSKATimeout=_RdnPktDQoSKATimeout_Object((1,3,6,1,4,1,4981,7,6,1,8),_RdnPktDQoSKATimeout_Type())
rdnPktDQoSKATimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:rdnPktDQoSKATimeout.setStatus(_A)
_RdnPktDQoST0Timeout_Type=Integer32
_RdnPktDQoST0Timeout_Object=MibTableColumn
rdnPktDQoST0Timeout=_RdnPktDQoST0Timeout_Object((1,3,6,1,4,1,4981,7,6,1,9),_RdnPktDQoST0Timeout_Type())
rdnPktDQoST0Timeout.setMaxAccess(_B)
if mibBuilder.loadTexts:rdnPktDQoST0Timeout.setStatus(_A)
_RdnPktDQoST1Timeout_Type=Integer32
_RdnPktDQoST1Timeout_Object=MibTableColumn
rdnPktDQoST1Timeout=_RdnPktDQoST1Timeout_Object((1,3,6,1,4,1,4981,7,6,1,10),_RdnPktDQoST1Timeout_Type())
rdnPktDQoST1Timeout.setMaxAccess(_B)
if mibBuilder.loadTexts:rdnPktDQoST1Timeout.setStatus(_A)
_RdnPktDQoSGateAllocCount_Type=Integer32
_RdnPktDQoSGateAllocCount_Object=MibTableColumn
rdnPktDQoSGateAllocCount=_RdnPktDQoSGateAllocCount_Object((1,3,6,1,4,1,4981,7,6,1,11),_RdnPktDQoSGateAllocCount_Type())
rdnPktDQoSGateAllocCount.setMaxAccess(_B)
if mibBuilder.loadTexts:rdnPktDQoSGateAllocCount.setStatus(_A)
_RdnPktDQoSGateAllocAckCount_Type=Integer32
_RdnPktDQoSGateAllocAckCount_Object=MibTableColumn
rdnPktDQoSGateAllocAckCount=_RdnPktDQoSGateAllocAckCount_Object((1,3,6,1,4,1,4981,7,6,1,12),_RdnPktDQoSGateAllocAckCount_Type())
rdnPktDQoSGateAllocAckCount.setMaxAccess(_B)
if mibBuilder.loadTexts:rdnPktDQoSGateAllocAckCount.setStatus(_A)
_RdnPktDQoSGateAllocErrCount_Type=Integer32
_RdnPktDQoSGateAllocErrCount_Object=MibTableColumn
rdnPktDQoSGateAllocErrCount=_RdnPktDQoSGateAllocErrCount_Object((1,3,6,1,4,1,4981,7,6,1,13),_RdnPktDQoSGateAllocErrCount_Type())
rdnPktDQoSGateAllocErrCount.setMaxAccess(_B)
if mibBuilder.loadTexts:rdnPktDQoSGateAllocErrCount.setStatus(_A)
_RdnPktDQoSGateSetCount_Type=Integer32
_RdnPktDQoSGateSetCount_Object=MibTableColumn
rdnPktDQoSGateSetCount=_RdnPktDQoSGateSetCount_Object((1,3,6,1,4,1,4981,7,6,1,14),_RdnPktDQoSGateSetCount_Type())
rdnPktDQoSGateSetCount.setMaxAccess(_B)
if mibBuilder.loadTexts:rdnPktDQoSGateSetCount.setStatus(_A)
_RdnPktDQoSGateSetAckCount_Type=Integer32
_RdnPktDQoSGateSetAckCount_Object=MibTableColumn
rdnPktDQoSGateSetAckCount=_RdnPktDQoSGateSetAckCount_Object((1,3,6,1,4,1,4981,7,6,1,15),_RdnPktDQoSGateSetAckCount_Type())
rdnPktDQoSGateSetAckCount.setMaxAccess(_B)
if mibBuilder.loadTexts:rdnPktDQoSGateSetAckCount.setStatus(_A)
_RdnPktDQoSGateSetErrCount_Type=Integer32
_RdnPktDQoSGateSetErrCount_Object=MibTableColumn
rdnPktDQoSGateSetErrCount=_RdnPktDQoSGateSetErrCount_Object((1,3,6,1,4,1,4981,7,6,1,16),_RdnPktDQoSGateSetErrCount_Type())
rdnPktDQoSGateSetErrCount.setMaxAccess(_B)
if mibBuilder.loadTexts:rdnPktDQoSGateSetErrCount.setStatus(_A)
_RdnPktDQoSGateDeleteCount_Type=Integer32
_RdnPktDQoSGateDeleteCount_Object=MibTableColumn
rdnPktDQoSGateDeleteCount=_RdnPktDQoSGateDeleteCount_Object((1,3,6,1,4,1,4981,7,6,1,17),_RdnPktDQoSGateDeleteCount_Type())
rdnPktDQoSGateDeleteCount.setMaxAccess(_B)
if mibBuilder.loadTexts:rdnPktDQoSGateDeleteCount.setStatus(_A)
_RdnPktDQoSGateDeleteAckCount_Type=Integer32
_RdnPktDQoSGateDeleteAckCount_Object=MibTableColumn
rdnPktDQoSGateDeleteAckCount=_RdnPktDQoSGateDeleteAckCount_Object((1,3,6,1,4,1,4981,7,6,1,18),_RdnPktDQoSGateDeleteAckCount_Type())
rdnPktDQoSGateDeleteAckCount.setMaxAccess(_B)
if mibBuilder.loadTexts:rdnPktDQoSGateDeleteAckCount.setStatus(_A)
_RdnPktDQoSGateDeleteErrCount_Type=Integer32
_RdnPktDQoSGateDeleteErrCount_Object=MibTableColumn
rdnPktDQoSGateDeleteErrCount=_RdnPktDQoSGateDeleteErrCount_Object((1,3,6,1,4,1,4981,7,6,1,19),_RdnPktDQoSGateDeleteErrCount_Type())
rdnPktDQoSGateDeleteErrCount.setMaxAccess(_B)
if mibBuilder.loadTexts:rdnPktDQoSGateDeleteErrCount.setStatus(_A)
_RdnPktDQoSGateInfoCount_Type=Integer32
_RdnPktDQoSGateInfoCount_Object=MibTableColumn
rdnPktDQoSGateInfoCount=_RdnPktDQoSGateInfoCount_Object((1,3,6,1,4,1,4981,7,6,1,20),_RdnPktDQoSGateInfoCount_Type())
rdnPktDQoSGateInfoCount.setMaxAccess(_B)
if mibBuilder.loadTexts:rdnPktDQoSGateInfoCount.setStatus(_A)
_RdnPktDQoSGateInfoAckCount_Type=Integer32
_RdnPktDQoSGateInfoAckCount_Object=MibTableColumn
rdnPktDQoSGateInfoAckCount=_RdnPktDQoSGateInfoAckCount_Object((1,3,6,1,4,1,4981,7,6,1,21),_RdnPktDQoSGateInfoAckCount_Type())
rdnPktDQoSGateInfoAckCount.setMaxAccess(_B)
if mibBuilder.loadTexts:rdnPktDQoSGateInfoAckCount.setStatus(_A)
_RdnPktDQoSGateInfoErrCount_Type=Integer32
_RdnPktDQoSGateInfoErrCount_Object=MibTableColumn
rdnPktDQoSGateInfoErrCount=_RdnPktDQoSGateInfoErrCount_Object((1,3,6,1,4,1,4981,7,6,1,22),_RdnPktDQoSGateInfoErrCount_Type())
rdnPktDQoSGateInfoErrCount.setMaxAccess(_B)
if mibBuilder.loadTexts:rdnPktDQoSGateInfoErrCount.setStatus(_A)
_RdnPktDQoSGateOpenRcvd_Type=Integer32
_RdnPktDQoSGateOpenRcvd_Object=MibTableColumn
rdnPktDQoSGateOpenRcvd=_RdnPktDQoSGateOpenRcvd_Object((1,3,6,1,4,1,4981,7,6,1,23),_RdnPktDQoSGateOpenRcvd_Type())
rdnPktDQoSGateOpenRcvd.setMaxAccess(_B)
if mibBuilder.loadTexts:rdnPktDQoSGateOpenRcvd.setStatus(_G)
_RdnPktDQoSGateOpenAckSent_Type=Integer32
_RdnPktDQoSGateOpenAckSent_Object=MibTableColumn
rdnPktDQoSGateOpenAckSent=_RdnPktDQoSGateOpenAckSent_Object((1,3,6,1,4,1,4981,7,6,1,24),_RdnPktDQoSGateOpenAckSent_Type())
rdnPktDQoSGateOpenAckSent.setMaxAccess(_B)
if mibBuilder.loadTexts:rdnPktDQoSGateOpenAckSent.setStatus(_G)
_RdnPktDQoSGateOpenErrSent_Type=Integer32
_RdnPktDQoSGateOpenErrSent_Object=MibTableColumn
rdnPktDQoSGateOpenErrSent=_RdnPktDQoSGateOpenErrSent_Object((1,3,6,1,4,1,4981,7,6,1,25),_RdnPktDQoSGateOpenErrSent_Type())
rdnPktDQoSGateOpenErrSent.setMaxAccess(_B)
if mibBuilder.loadTexts:rdnPktDQoSGateOpenErrSent.setStatus(_G)
_RdnPktDQoSGateCloseRcvd_Type=Integer32
_RdnPktDQoSGateCloseRcvd_Object=MibTableColumn
rdnPktDQoSGateCloseRcvd=_RdnPktDQoSGateCloseRcvd_Object((1,3,6,1,4,1,4981,7,6,1,26),_RdnPktDQoSGateCloseRcvd_Type())
rdnPktDQoSGateCloseRcvd.setMaxAccess(_B)
if mibBuilder.loadTexts:rdnPktDQoSGateCloseRcvd.setStatus(_G)
_RdnPktDQoSGateCloseAckSent_Type=Integer32
_RdnPktDQoSGateCloseAckSent_Object=MibTableColumn
rdnPktDQoSGateCloseAckSent=_RdnPktDQoSGateCloseAckSent_Object((1,3,6,1,4,1,4981,7,6,1,27),_RdnPktDQoSGateCloseAckSent_Type())
rdnPktDQoSGateCloseAckSent.setMaxAccess(_B)
if mibBuilder.loadTexts:rdnPktDQoSGateCloseAckSent.setStatus(_G)
_RdnPktDQoSGateCloseErrSent_Type=Integer32
_RdnPktDQoSGateCloseErrSent_Object=MibTableColumn
rdnPktDQoSGateCloseErrSent=_RdnPktDQoSGateCloseErrSent_Object((1,3,6,1,4,1,4981,7,6,1,28),_RdnPktDQoSGateCloseErrSent_Type())
rdnPktDQoSGateCloseErrSent.setMaxAccess(_B)
if mibBuilder.loadTexts:rdnPktDQoSGateCloseErrSent.setStatus(_G)
_RdnPktDQoSGateOpenSent_Type=Integer32
_RdnPktDQoSGateOpenSent_Object=MibTableColumn
rdnPktDQoSGateOpenSent=_RdnPktDQoSGateOpenSent_Object((1,3,6,1,4,1,4981,7,6,1,29),_RdnPktDQoSGateOpenSent_Type())
rdnPktDQoSGateOpenSent.setMaxAccess(_B)
if mibBuilder.loadTexts:rdnPktDQoSGateOpenSent.setStatus(_A)
_RdnPktDQoSGateOpenAckRcvd_Type=Integer32
_RdnPktDQoSGateOpenAckRcvd_Object=MibTableColumn
rdnPktDQoSGateOpenAckRcvd=_RdnPktDQoSGateOpenAckRcvd_Object((1,3,6,1,4,1,4981,7,6,1,30),_RdnPktDQoSGateOpenAckRcvd_Type())
rdnPktDQoSGateOpenAckRcvd.setMaxAccess(_B)
if mibBuilder.loadTexts:rdnPktDQoSGateOpenAckRcvd.setStatus(_G)
_RdnPktDQoSGateOpenErrRcvd_Type=Integer32
_RdnPktDQoSGateOpenErrRcvd_Object=MibTableColumn
rdnPktDQoSGateOpenErrRcvd=_RdnPktDQoSGateOpenErrRcvd_Object((1,3,6,1,4,1,4981,7,6,1,31),_RdnPktDQoSGateOpenErrRcvd_Type())
rdnPktDQoSGateOpenErrRcvd.setMaxAccess(_B)
if mibBuilder.loadTexts:rdnPktDQoSGateOpenErrRcvd.setStatus(_G)
_RdnPktDQoSGateCloseSent_Type=Integer32
_RdnPktDQoSGateCloseSent_Object=MibTableColumn
rdnPktDQoSGateCloseSent=_RdnPktDQoSGateCloseSent_Object((1,3,6,1,4,1,4981,7,6,1,32),_RdnPktDQoSGateCloseSent_Type())
rdnPktDQoSGateCloseSent.setMaxAccess(_B)
if mibBuilder.loadTexts:rdnPktDQoSGateCloseSent.setStatus(_A)
_RdnPktDQoSGateCloseAckRcvd_Type=Integer32
_RdnPktDQoSGateCloseAckRcvd_Object=MibTableColumn
rdnPktDQoSGateCloseAckRcvd=_RdnPktDQoSGateCloseAckRcvd_Object((1,3,6,1,4,1,4981,7,6,1,33),_RdnPktDQoSGateCloseAckRcvd_Type())
rdnPktDQoSGateCloseAckRcvd.setMaxAccess(_B)
if mibBuilder.loadTexts:rdnPktDQoSGateCloseAckRcvd.setStatus(_G)
_RdnPktDQoSGateCloseErrRcvd_Type=Integer32
_RdnPktDQoSGateCloseErrRcvd_Object=MibTableColumn
rdnPktDQoSGateCloseErrRcvd=_RdnPktDQoSGateCloseErrRcvd_Object((1,3,6,1,4,1,4981,7,6,1,34),_RdnPktDQoSGateCloseErrRcvd_Type())
rdnPktDQoSGateCloseErrRcvd.setMaxAccess(_B)
if mibBuilder.loadTexts:rdnPktDQoSGateCloseErrRcvd.setStatus(_G)
_RdnPktDQoSGateOpenRetries_Type=Integer32
_RdnPktDQoSGateOpenRetries_Object=MibTableColumn
rdnPktDQoSGateOpenRetries=_RdnPktDQoSGateOpenRetries_Object((1,3,6,1,4,1,4981,7,6,1,35),_RdnPktDQoSGateOpenRetries_Type())
rdnPktDQoSGateOpenRetries.setMaxAccess(_B)
if mibBuilder.loadTexts:rdnPktDQoSGateOpenRetries.setStatus(_G)
_RdnPktDQoSGateCloseRetries_Type=Integer32
_RdnPktDQoSGateCloseRetries_Object=MibTableColumn
rdnPktDQoSGateCloseRetries=_RdnPktDQoSGateCloseRetries_Object((1,3,6,1,4,1,4981,7,6,1,36),_RdnPktDQoSGateCloseRetries_Type())
rdnPktDQoSGateCloseRetries.setMaxAccess(_B)
if mibBuilder.loadTexts:rdnPktDQoSGateCloseRetries.setStatus(_G)
_RdnPktDQoSGateOpenExhausted_Type=Integer32
_RdnPktDQoSGateOpenExhausted_Object=MibTableColumn
rdnPktDQoSGateOpenExhausted=_RdnPktDQoSGateOpenExhausted_Object((1,3,6,1,4,1,4981,7,6,1,37),_RdnPktDQoSGateOpenExhausted_Type())
rdnPktDQoSGateOpenExhausted.setMaxAccess(_B)
if mibBuilder.loadTexts:rdnPktDQoSGateOpenExhausted.setStatus(_G)
_RdnPktDQoSGateCloseExhausted_Type=Integer32
_RdnPktDQoSGateCloseExhausted_Object=MibTableColumn
rdnPktDQoSGateCloseExhausted=_RdnPktDQoSGateCloseExhausted_Object((1,3,6,1,4,1,4981,7,6,1,38),_RdnPktDQoSGateCloseExhausted_Type())
rdnPktDQoSGateCloseExhausted.setMaxAccess(_B)
if mibBuilder.loadTexts:rdnPktDQoSGateCloseExhausted.setStatus(_G)
_RdnPktDQoSCliOpenSent_Type=Integer32
_RdnPktDQoSCliOpenSent_Object=MibTableColumn
rdnPktDQoSCliOpenSent=_RdnPktDQoSCliOpenSent_Object((1,3,6,1,4,1,4981,7,6,1,39),_RdnPktDQoSCliOpenSent_Type())
rdnPktDQoSCliOpenSent.setMaxAccess(_B)
if mibBuilder.loadTexts:rdnPktDQoSCliOpenSent.setStatus(_A)
_RdnPktDQoSCliAcceptReceived_Type=Integer32
_RdnPktDQoSCliAcceptReceived_Object=MibTableColumn
rdnPktDQoSCliAcceptReceived=_RdnPktDQoSCliAcceptReceived_Object((1,3,6,1,4,1,4981,7,6,1,40),_RdnPktDQoSCliAcceptReceived_Type())
rdnPktDQoSCliAcceptReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:rdnPktDQoSCliAcceptReceived.setStatus(_A)
_RdnPktDQoSRequestSent_Type=Integer32
_RdnPktDQoSRequestSent_Object=MibTableColumn
rdnPktDQoSRequestSent=_RdnPktDQoSRequestSent_Object((1,3,6,1,4,1,4981,7,6,1,41),_RdnPktDQoSRequestSent_Type())
rdnPktDQoSRequestSent.setMaxAccess(_B)
if mibBuilder.loadTexts:rdnPktDQoSRequestSent.setStatus(_A)
_RdnPktDQoSCliCloseReceived_Type=Integer32
_RdnPktDQoSCliCloseReceived_Object=MibTableColumn
rdnPktDQoSCliCloseReceived=_RdnPktDQoSCliCloseReceived_Object((1,3,6,1,4,1,4981,7,6,1,42),_RdnPktDQoSCliCloseReceived_Type())
rdnPktDQoSCliCloseReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:rdnPktDQoSCliCloseReceived.setStatus(_A)
_RdnPktDQoSCliCloseSent_Type=Integer32
_RdnPktDQoSCliCloseSent_Object=MibTableColumn
rdnPktDQoSCliCloseSent=_RdnPktDQoSCliCloseSent_Object((1,3,6,1,4,1,4981,7,6,1,43),_RdnPktDQoSCliCloseSent_Type())
rdnPktDQoSCliCloseSent.setMaxAccess(_B)
if mibBuilder.loadTexts:rdnPktDQoSCliCloseSent.setStatus(_A)
_RdnPktDQoSSsqReceived_Type=Integer32
_RdnPktDQoSSsqReceived_Object=MibTableColumn
rdnPktDQoSSsqReceived=_RdnPktDQoSSsqReceived_Object((1,3,6,1,4,1,4981,7,6,1,44),_RdnPktDQoSSsqReceived_Type())
rdnPktDQoSSsqReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:rdnPktDQoSSsqReceived.setStatus(_A)
_RdnPktDQoSSscSent_Type=Integer32
_RdnPktDQoSSscSent_Object=MibTableColumn
rdnPktDQoSSscSent=_RdnPktDQoSSscSent_Object((1,3,6,1,4,1,4981,7,6,1,45),_RdnPktDQoSSscSent_Type())
rdnPktDQoSSscSent.setMaxAccess(_B)
if mibBuilder.loadTexts:rdnPktDQoSSscSent.setStatus(_A)
_RdnPktDQoSDrqSent_Type=Integer32
_RdnPktDQoSDrqSent_Object=MibTableColumn
rdnPktDQoSDrqSent=_RdnPktDQoSDrqSent_Object((1,3,6,1,4,1,4981,7,6,1,46),_RdnPktDQoSDrqSent_Type())
rdnPktDQoSDrqSent.setMaxAccess(_B)
if mibBuilder.loadTexts:rdnPktDQoSDrqSent.setStatus(_A)
_RdnPktDQoST7Timeout_Type=Integer32
_RdnPktDQoST7Timeout_Object=MibTableColumn
rdnPktDQoST7Timeout=_RdnPktDQoST7Timeout_Object((1,3,6,1,4,1,4981,7,6,1,47),_RdnPktDQoST7Timeout_Type())
rdnPktDQoST7Timeout.setMaxAccess(_B)
if mibBuilder.loadTexts:rdnPktDQoST7Timeout.setStatus(_A)
_RdnPktDQoST8Timeout_Type=Integer32
_RdnPktDQoST8Timeout_Object=MibTableColumn
rdnPktDQoST8Timeout=_RdnPktDQoST8Timeout_Object((1,3,6,1,4,1,4981,7,6,1,48),_RdnPktDQoST8Timeout_Type())
rdnPktDQoST8Timeout.setMaxAccess(_B)
if mibBuilder.loadTexts:rdnPktDQoST8Timeout.setStatus(_A)
_RdnPktDQoSGateCmDel_Type=Integer32
_RdnPktDQoSGateCmDel_Object=MibTableColumn
rdnPktDQoSGateCmDel=_RdnPktDQoSGateCmDel_Object((1,3,6,1,4,1,4981,7,6,1,49),_RdnPktDQoSGateCmDel_Type())
rdnPktDQoSGateCmDel.setMaxAccess(_B)
if mibBuilder.loadTexts:rdnPktDQoSGateCmDel.setStatus(_A)
_RdnPktDQoSGateCmDereg_Type=Integer32
_RdnPktDQoSGateCmDereg_Object=MibTableColumn
rdnPktDQoSGateCmDereg=_RdnPktDQoSGateCmDereg_Object((1,3,6,1,4,1,4981,7,6,1,50),_RdnPktDQoSGateCmDereg_Type())
rdnPktDQoSGateCmDereg.setMaxAccess(_B)
if mibBuilder.loadTexts:rdnPktDQoSGateCmDereg.setStatus(_A)
_RdnPktDQoSGateAdminDel_Type=Integer32
_RdnPktDQoSGateAdminDel_Object=MibTableColumn
rdnPktDQoSGateAdminDel=_RdnPktDQoSGateAdminDel_Object((1,3,6,1,4,1,4981,7,6,1,51),_RdnPktDQoSGateAdminDel_Type())
rdnPktDQoSGateAdminDel.setMaxAccess(_B)
if mibBuilder.loadTexts:rdnPktDQoSGateAdminDel.setStatus(_A)
_RdnPktDQoSGateResReassign_Type=Integer32
_RdnPktDQoSGateResReassign_Object=MibTableColumn
rdnPktDQoSGateResReassign=_RdnPktDQoSGateResReassign_Object((1,3,6,1,4,1,4981,7,6,1,52),_RdnPktDQoSGateResReassign_Type())
rdnPktDQoSGateResReassign.setMaxAccess(_B)
if mibBuilder.loadTexts:rdnPktDQoSGateResReassign.setStatus(_A)
_RdnPktDQoSNotificationObject_ObjectIdentity=ObjectIdentity
rdnPktDQoSNotificationObject=_RdnPktDQoSNotificationObject_ObjectIdentity((1,3,6,1,4,1,4981,7,7))
class _RdnPktDQoSCopsReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('copsConnectionEstablished',1),('cantEstablishCopsConnection',2),('unauthorizedCms',3),('copsConnectionClosed',4),('copsConnectionDisconnected',5),('keepAliveFailure',6)))
_RdnPktDQoSCopsReason_Type.__name__=_D
_RdnPktDQoSCopsReason_Object=MibScalar
rdnPktDQoSCopsReason=_RdnPktDQoSCopsReason_Object((1,3,6,1,4,1,4981,7,7,1),_RdnPktDQoSCopsReason_Type())
rdnPktDQoSCopsReason.setMaxAccess(_F)
if mibBuilder.loadTexts:rdnPktDQoSCopsReason.setStatus(_A)
_RdnPktDQoSCopsCmsIpAddr_Type=IpAddress
_RdnPktDQoSCopsCmsIpAddr_Object=MibScalar
rdnPktDQoSCopsCmsIpAddr=_RdnPktDQoSCopsCmsIpAddr_Object((1,3,6,1,4,1,4981,7,7,2),_RdnPktDQoSCopsCmsIpAddr_Type())
rdnPktDQoSCopsCmsIpAddr.setMaxAccess(_F)
if mibBuilder.loadTexts:rdnPktDQoSCopsCmsIpAddr.setStatus(_A)
_RdnPktDQoSCopsCmsPortNum_Type=Integer32
_RdnPktDQoSCopsCmsPortNum_Object=MibScalar
rdnPktDQoSCopsCmsPortNum=_RdnPktDQoSCopsCmsPortNum_Object((1,3,6,1,4,1,4981,7,7,3),_RdnPktDQoSCopsCmsPortNum_Type())
rdnPktDQoSCopsCmsPortNum.setMaxAccess(_F)
if mibBuilder.loadTexts:rdnPktDQoSCopsCmsPortNum.setStatus(_A)
_RdnPktDQoSCopsCmsHandleId_Type=Integer32
_RdnPktDQoSCopsCmsHandleId_Object=MibScalar
rdnPktDQoSCopsCmsHandleId=_RdnPktDQoSCopsCmsHandleId_Object((1,3,6,1,4,1,4981,7,7,4),_RdnPktDQoSCopsCmsHandleId_Type())
rdnPktDQoSCopsCmsHandleId.setMaxAccess(_F)
if mibBuilder.loadTexts:rdnPktDQoSCopsCmsHandleId.setStatus(_A)
class _RdnPktDQoSResReqReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('dsaReqResourceGreaterThanAuth',1),('dsaResReqWithoutGateId',2),('dsaResReqWithInvalidGateId',3),('dscReqResourceGreaterThanAuth',4),('dscResReqWithoutGateId',5),('dscResReqWithInvalidGateId',6)))
_RdnPktDQoSResReqReason_Type.__name__=_D
_RdnPktDQoSResReqReason_Object=MibScalar
rdnPktDQoSResReqReason=_RdnPktDQoSResReqReason_Object((1,3,6,1,4,1,4981,7,7,5),_RdnPktDQoSResReqReason_Type())
rdnPktDQoSResReqReason.setMaxAccess(_F)
if mibBuilder.loadTexts:rdnPktDQoSResReqReason.setStatus(_A)
_RdnPktDQoSCmMacAddr_Type=MacAddress
_RdnPktDQoSCmMacAddr_Object=MibScalar
rdnPktDQoSCmMacAddr=_RdnPktDQoSCmMacAddr_Object((1,3,6,1,4,1,4981,7,7,6),_RdnPktDQoSCmMacAddr_Type())
rdnPktDQoSCmMacAddr.setMaxAccess(_F)
if mibBuilder.loadTexts:rdnPktDQoSCmMacAddr.setStatus(_A)
class _RdnPktDQoSEmergencyReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('emergencyCallBeingRejected',1))
_RdnPktDQoSEmergencyReason_Type.__name__=_D
_RdnPktDQoSEmergencyReason_Object=MibScalar
rdnPktDQoSEmergencyReason=_RdnPktDQoSEmergencyReason_Object((1,3,6,1,4,1,4981,7,7,7),_RdnPktDQoSEmergencyReason_Type())
rdnPktDQoSEmergencyReason.setMaxAccess(_F)
if mibBuilder.loadTexts:rdnPktDQoSEmergencyReason.setStatus(_A)
class _RdnPktDQoSClassName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_RdnPktDQoSClassName_Type.__name__=_L
_RdnPktDQoSClassName_Object=MibScalar
rdnPktDQoSClassName=_RdnPktDQoSClassName_Object((1,3,6,1,4,1,4981,7,7,8),_RdnPktDQoSClassName_Type())
rdnPktDQoSClassName.setMaxAccess(_F)
if mibBuilder.loadTexts:rdnPktDQoSClassName.setStatus(_A)
_RdnPktDQoSGateId_Type=Integer32
_RdnPktDQoSGateId_Object=MibScalar
rdnPktDQoSGateId=_RdnPktDQoSGateId_Object((1,3,6,1,4,1,4981,7,7,9),_RdnPktDQoSGateId_Type())
rdnPktDQoSGateId.setMaxAccess(_F)
if mibBuilder.loadTexts:rdnPktDQoSGateId.setStatus(_A)
class _RdnPktDQoSEmergencyPreemptReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('emergencyPreemptedMostRecentCall',1),('emergencyPreemptedOldestCall',2),('emergencyPreemptedRandomCall',3)))
_RdnPktDQoSEmergencyPreemptReason_Type.__name__=_D
_RdnPktDQoSEmergencyPreemptReason_Object=MibScalar
rdnPktDQoSEmergencyPreemptReason=_RdnPktDQoSEmergencyPreemptReason_Object((1,3,6,1,4,1,4981,7,7,10),_RdnPktDQoSEmergencyPreemptReason_Type())
rdnPktDQoSEmergencyPreemptReason.setMaxAccess(_F)
if mibBuilder.loadTexts:rdnPktDQoSEmergencyPreemptReason.setStatus(_A)
_RdnPktDQoSNotificationTraps_ObjectIdentity=ObjectIdentity
rdnPktDQoSNotificationTraps=_RdnPktDQoSNotificationTraps_ObjectIdentity((1,3,6,1,4,1,4981,7,8))
_RdnPktDQoSNotificationTrapsPrefix_ObjectIdentity=ObjectIdentity
rdnPktDQoSNotificationTrapsPrefix=_RdnPktDQoSNotificationTrapsPrefix_ObjectIdentity((1,3,6,1,4,1,4981,7,8,0))
_RdnPktESNotificationObject_ObjectIdentity=ObjectIdentity
rdnPktESNotificationObject=_RdnPktESNotificationObject_ObjectIdentity((1,3,6,1,4,1,4981,7,9))
class _RdnPktESReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('cdcFailure',1))
_RdnPktESReason_Type.__name__=_D
_RdnPktESReason_Object=MibScalar
rdnPktESReason=_RdnPktESReason_Object((1,3,6,1,4,1,4981,7,9,1),_RdnPktESReason_Type())
rdnPktESReason.setMaxAccess(_F)
if mibBuilder.loadTexts:rdnPktESReason.setStatus(_A)
_RdnPktESDFIpAddr_Type=IpAddress
_RdnPktESDFIpAddr_Object=MibScalar
rdnPktESDFIpAddr=_RdnPktESDFIpAddr_Object((1,3,6,1,4,1,4981,7,9,2),_RdnPktESDFIpAddr_Type())
rdnPktESDFIpAddr.setMaxAccess(_F)
if mibBuilder.loadTexts:rdnPktESDFIpAddr.setStatus(_A)
_RdnPktESDFPortNum_Type=Integer32
_RdnPktESDFPortNum_Object=MibScalar
rdnPktESDFPortNum=_RdnPktESDFPortNum_Object((1,3,6,1,4,1,4981,7,9,3),_RdnPktESDFPortNum_Type())
rdnPktESDFPortNum.setMaxAccess(_F)
if mibBuilder.loadTexts:rdnPktESDFPortNum.setStatus(_A)
_RdnPktESNotificationTraps_ObjectIdentity=ObjectIdentity
rdnPktESNotificationTraps=_RdnPktESNotificationTraps_ObjectIdentity((1,3,6,1,4,1,4981,7,10))
_RdnPktESNotificationTrapsPrefix_ObjectIdentity=ObjectIdentity
rdnPktESNotificationTrapsPrefix=_RdnPktESNotificationTrapsPrefix_ObjectIdentity((1,3,6,1,4,1,4981,7,10,0))
_RdnPktRKSNotificationObject_ObjectIdentity=ObjectIdentity
rdnPktRKSNotificationObject=_RdnPktRKSNotificationObject_ObjectIdentity((1,3,6,1,4,1,4981,7,11))
class _RdnPktRKSReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('retriesExhausted',1))
_RdnPktRKSReason_Type.__name__=_D
_RdnPktRKSReason_Object=MibScalar
rdnPktRKSReason=_RdnPktRKSReason_Object((1,3,6,1,4,1,4981,7,11,1),_RdnPktRKSReason_Type())
rdnPktRKSReason.setMaxAccess(_F)
if mibBuilder.loadTexts:rdnPktRKSReason.setStatus(_A)
_RdnPktRKSTransID_Type=Integer32
_RdnPktRKSTransID_Object=MibScalar
rdnPktRKSTransID=_RdnPktRKSTransID_Object((1,3,6,1,4,1,4981,7,11,2),_RdnPktRKSTransID_Type())
rdnPktRKSTransID.setMaxAccess(_F)
if mibBuilder.loadTexts:rdnPktRKSTransID.setStatus(_A)
_RdnPktRKSIPPrimary_Type=IpAddress
_RdnPktRKSIPPrimary_Object=MibScalar
rdnPktRKSIPPrimary=_RdnPktRKSIPPrimary_Object((1,3,6,1,4,1,4981,7,11,3),_RdnPktRKSIPPrimary_Type())
rdnPktRKSIPPrimary.setMaxAccess(_F)
if mibBuilder.loadTexts:rdnPktRKSIPPrimary.setStatus(_A)
_RdnPktRKSPortPrimary_Type=Integer32
_RdnPktRKSPortPrimary_Object=MibScalar
rdnPktRKSPortPrimary=_RdnPktRKSPortPrimary_Object((1,3,6,1,4,1,4981,7,11,4),_RdnPktRKSPortPrimary_Type())
rdnPktRKSPortPrimary.setMaxAccess(_F)
if mibBuilder.loadTexts:rdnPktRKSPortPrimary.setStatus(_A)
_RdnPktRKSIPSecondary_Type=IpAddress
_RdnPktRKSIPSecondary_Object=MibScalar
rdnPktRKSIPSecondary=_RdnPktRKSIPSecondary_Object((1,3,6,1,4,1,4981,7,11,5),_RdnPktRKSIPSecondary_Type())
rdnPktRKSIPSecondary.setMaxAccess(_F)
if mibBuilder.loadTexts:rdnPktRKSIPSecondary.setStatus(_A)
_RdnPktRKSPortSecondary_Type=Integer32
_RdnPktRKSPortSecondary_Object=MibScalar
rdnPktRKSPortSecondary=_RdnPktRKSPortSecondary_Object((1,3,6,1,4,1,4981,7,11,6),_RdnPktRKSPortSecondary_Type())
rdnPktRKSPortSecondary.setMaxAccess(_F)
if mibBuilder.loadTexts:rdnPktRKSPortSecondary.setStatus(_A)
class _RdnPktRKSVersionID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('packetCable10',1),('packetCable11',2),('packetCableMultiMedia',3)))
_RdnPktRKSVersionID_Type.__name__=_D
_RdnPktRKSVersionID_Object=MibScalar
rdnPktRKSVersionID=_RdnPktRKSVersionID_Object((1,3,6,1,4,1,4981,7,11,7),_RdnPktRKSVersionID_Type())
rdnPktRKSVersionID.setMaxAccess(_F)
if mibBuilder.loadTexts:rdnPktRKSVersionID.setStatus(_A)
_RdnPktRKSNotificationTraps_ObjectIdentity=ObjectIdentity
rdnPktRKSNotificationTraps=_RdnPktRKSNotificationTraps_ObjectIdentity((1,3,6,1,4,1,4981,7,12))
_RdnPktRKSNotificationTrapsPrefix_ObjectIdentity=ObjectIdentity
rdnPktRKSNotificationTrapsPrefix=_RdnPktRKSNotificationTrapsPrefix_ObjectIdentity((1,3,6,1,4,1,4981,7,12,0))
rdnPktDQoSCopsTrap=NotificationType((1,3,6,1,4,1,4981,7,8,0,1))
rdnPktDQoSCopsTrap.setObjects(*((_C,_T),(_C,_U)))
if mibBuilder.loadTexts:rdnPktDQoSCopsTrap.setStatus(_A)
rdnPktDQoSResReqTrap=NotificationType((1,3,6,1,4,1,4981,7,8,0,2))
rdnPktDQoSResReqTrap.setObjects(*((_C,_V),(_C,_K)))
if mibBuilder.loadTexts:rdnPktDQoSResReqTrap.setStatus(_A)
rdnPktDQoSEmergencyTrap=NotificationType((1,3,6,1,4,1,4981,7,8,0,3))
rdnPktDQoSEmergencyTrap.setObjects(*((_C,_W),(_C,_K),(_C,_N),(_C,_O)))
if mibBuilder.loadTexts:rdnPktDQoSEmergencyTrap.setStatus(_A)
rdnPktDQoSEmergencyPreemptTrap=NotificationType((1,3,6,1,4,1,4981,7,8,0,4))
rdnPktDQoSEmergencyPreemptTrap.setObjects(*((_C,_X),(_C,_K),(_C,_N),(_C,_O)))
if mibBuilder.loadTexts:rdnPktDQoSEmergencyPreemptTrap.setStatus(_A)
rdnPktESTrap=NotificationType((1,3,6,1,4,1,4981,7,10,0,1))
rdnPktESTrap.setObjects(*((_C,_Y),(_C,_Z),(_C,_a)))
if mibBuilder.loadTexts:rdnPktESTrap.setStatus(_A)
rdnPktDQoSRKSTrap=NotificationType((1,3,6,1,4,1,4981,7,12,0,1))
rdnPktDQoSRKSTrap.setObjects(*((_C,_b),(_C,_c),(_C,_d),(_C,_e),(_C,_f),(_C,_g),(_C,_h)))
if mibBuilder.loadTexts:rdnPktDQoSRKSTrap.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'BcidDataArray':BcidDataArray,'rdnPacketCableGroup':rdnPacketCableGroup,'rdnPktDQoSConfigGroup':rdnPktDQoSConfigGroup,'rdnPktDQoSCOPSStatus':rdnPktDQoSCOPSStatus,'rdnPktDQoSCMTSIp':rdnPktDQoSCMTSIp,'rdnPktDQoSPEPID':rdnPktDQoSPEPID,'rdnPktDQoSClientAccpTimer':rdnPktDQoSClientAccpTimer,'rdnPktDQoST0Timer':rdnPktDQoST0Timer,'rdnPktDQoST1Timer':rdnPktDQoST1Timer,'rdnPktDQoST3Timer':rdnPktDQoST3Timer,'rdnPktDQoST6Timer':rdnPktDQoST6Timer,'rdnPktDQoSCopsTrapEnable':rdnPktDQoSCopsTrapEnable,'rdnPktDQoSResReqTrapEnable':rdnPktDQoSResReqTrapEnable,'rdnPktESTrapEnable':rdnPktESTrapEnable,'rdnPktESEnable':rdnPktESEnable,'rdnPktDQoSEmergencyTrapEnable':rdnPktDQoSEmergencyTrapEnable,'rdnPktDQoSEmergencyPreemption':rdnPktDQoSEmergencyPreemption,'rdnPktEMRKSFailureTrapEnable':rdnPktEMRKSFailureTrapEnable,'rdnPktDQoSDscp':rdnPktDQoSDscp,'rdnPktMMDscp':rdnPktMMDscp,'rdnPktEMDscp':rdnPktEMDscp,'rdnPktESCccDscp':rdnPktESCccDscp,'rdnGateStatsTable':rdnGateStatsTable,'rdnGateStatsEntry':rdnGateStatsEntry,_M:rdnGateId,'rdnGateStatsState':rdnGateStatsState,'rdnGateStatsSubscriberIP':rdnGateStatsSubscriberIP,'rdnGateStatsRKSPrimaryAddr':rdnGateStatsRKSPrimaryAddr,'rdnGateStatsRKSPrimaryPort':rdnGateStatsRKSPrimaryPort,'rdnGateStatsRKSSecondaryAddr':rdnGateStatsRKSSecondaryAddr,'rdnGateStatsRKSSecondaryPort':rdnGateStatsRKSSecondaryPort,'rdnGateStatsEventFlag':rdnGateStatsEventFlag,'rdnGateStatsBillingCorrelationID':rdnGateStatsBillingCorrelationID,'rdnGateStatsDurationTime':rdnGateStatsDurationTime,'rdnGateStatsSlotNum':rdnGateStatsSlotNum,'rdnGateStatsUpSfid':rdnGateStatsUpSfid,'rdnGateStatsDnSfid':rdnGateStatsDnSfid,'rdnGateStatsResourceID':rdnGateStatsResourceID,'rdnGateStatsESCDCAddr':rdnGateStatsESCDCAddr,'rdnGateStatsESCDCPort':rdnGateStatsESCDCPort,'rdnGateStatsESFlag':rdnGateStatsESFlag,'rdnGateStatsESCCCAddr':rdnGateStatsESCCCAddr,'rdnGateStatsESCCCPort':rdnGateStatsESCCCPort,'rdnGateStatsESCCCId':rdnGateStatsESCCCId,'rdnGateSpecTable':rdnGateSpecTable,'rdnGateSpecEntry':rdnGateSpecEntry,_Q:rdnGateDirection,'rdnGateSpecProtocol':rdnGateSpecProtocol,'rdnGateSpecSourceIP':rdnGateSpecSourceIP,'rdnGateSpecSourcePort':rdnGateSpecSourcePort,'rdnGateSpecDestIP':rdnGateSpecDestIP,'rdnGateSpecDestPort':rdnGateSpecDestPort,'rdnGateSpecServiceFlowID':rdnGateSpecServiceFlowID,'rdnGateSpecFlags':rdnGateSpecFlags,'rdnGateSpecSessionClass':rdnGateSpecSessionClass,'rdnGateSpecDiffServCode':rdnGateSpecDiffServCode,'rdnGateSpecT1Timer':rdnGateSpecT1Timer,'rdnGateSpecTokenBuckRate':rdnGateSpecTokenBuckRate,'rdnGateSpecBuckSize':rdnGateSpecBuckSize,'rdnGateSpecPeakDataRate':rdnGateSpecPeakDataRate,'rdnGateSpecMinPoliceUnit':rdnGateSpecMinPoliceUnit,'rdnGateSpecMaxPacketSize':rdnGateSpecMaxPacketSize,'rdnGateSpecReserveRate':rdnGateSpecReserveRate,'rdnGateSlackTerm':rdnGateSlackTerm,'rdnPktCMSIpConfigTable':rdnPktCMSIpConfigTable,'rdnPktCMSIpConfigEntry':rdnPktCMSIpConfigEntry,_R:rdnPktCMSIpAddressIndex,'rdnPktCMSIpAddress':rdnPktCMSIpAddress,'rdnPktDQoSStatsTable':rdnPktDQoSStatsTable,'rdnPktDQoSStatsEntry':rdnPktDQoSStatsEntry,'rdnPktDQoSIpAddress':rdnPktDQoSIpAddress,_S:rdnPktDQoSCopsHandle,'rdnPktDQoSCopsStatus':rdnPktDQoSCopsStatus,'rdnPktDQoSCopsConnected':rdnPktDQoSCopsConnected,'rdnPktDQoSCopsTerminated':rdnPktDQoSCopsTerminated,'rdnPktDQoSCopsKASent':rdnPktDQoSCopsKASent,'rdnPktDQoSCopsKARcvd':rdnPktDQoSCopsKARcvd,'rdnPktDQoSKATimeout':rdnPktDQoSKATimeout,'rdnPktDQoST0Timeout':rdnPktDQoST0Timeout,'rdnPktDQoST1Timeout':rdnPktDQoST1Timeout,'rdnPktDQoSGateAllocCount':rdnPktDQoSGateAllocCount,'rdnPktDQoSGateAllocAckCount':rdnPktDQoSGateAllocAckCount,'rdnPktDQoSGateAllocErrCount':rdnPktDQoSGateAllocErrCount,'rdnPktDQoSGateSetCount':rdnPktDQoSGateSetCount,'rdnPktDQoSGateSetAckCount':rdnPktDQoSGateSetAckCount,'rdnPktDQoSGateSetErrCount':rdnPktDQoSGateSetErrCount,'rdnPktDQoSGateDeleteCount':rdnPktDQoSGateDeleteCount,'rdnPktDQoSGateDeleteAckCount':rdnPktDQoSGateDeleteAckCount,'rdnPktDQoSGateDeleteErrCount':rdnPktDQoSGateDeleteErrCount,'rdnPktDQoSGateInfoCount':rdnPktDQoSGateInfoCount,'rdnPktDQoSGateInfoAckCount':rdnPktDQoSGateInfoAckCount,'rdnPktDQoSGateInfoErrCount':rdnPktDQoSGateInfoErrCount,'rdnPktDQoSGateOpenRcvd':rdnPktDQoSGateOpenRcvd,'rdnPktDQoSGateOpenAckSent':rdnPktDQoSGateOpenAckSent,'rdnPktDQoSGateOpenErrSent':rdnPktDQoSGateOpenErrSent,'rdnPktDQoSGateCloseRcvd':rdnPktDQoSGateCloseRcvd,'rdnPktDQoSGateCloseAckSent':rdnPktDQoSGateCloseAckSent,'rdnPktDQoSGateCloseErrSent':rdnPktDQoSGateCloseErrSent,'rdnPktDQoSGateOpenSent':rdnPktDQoSGateOpenSent,'rdnPktDQoSGateOpenAckRcvd':rdnPktDQoSGateOpenAckRcvd,'rdnPktDQoSGateOpenErrRcvd':rdnPktDQoSGateOpenErrRcvd,'rdnPktDQoSGateCloseSent':rdnPktDQoSGateCloseSent,'rdnPktDQoSGateCloseAckRcvd':rdnPktDQoSGateCloseAckRcvd,'rdnPktDQoSGateCloseErrRcvd':rdnPktDQoSGateCloseErrRcvd,'rdnPktDQoSGateOpenRetries':rdnPktDQoSGateOpenRetries,'rdnPktDQoSGateCloseRetries':rdnPktDQoSGateCloseRetries,'rdnPktDQoSGateOpenExhausted':rdnPktDQoSGateOpenExhausted,'rdnPktDQoSGateCloseExhausted':rdnPktDQoSGateCloseExhausted,'rdnPktDQoSCliOpenSent':rdnPktDQoSCliOpenSent,'rdnPktDQoSCliAcceptReceived':rdnPktDQoSCliAcceptReceived,'rdnPktDQoSRequestSent':rdnPktDQoSRequestSent,'rdnPktDQoSCliCloseReceived':rdnPktDQoSCliCloseReceived,'rdnPktDQoSCliCloseSent':rdnPktDQoSCliCloseSent,'rdnPktDQoSSsqReceived':rdnPktDQoSSsqReceived,'rdnPktDQoSSscSent':rdnPktDQoSSscSent,'rdnPktDQoSDrqSent':rdnPktDQoSDrqSent,'rdnPktDQoST7Timeout':rdnPktDQoST7Timeout,'rdnPktDQoST8Timeout':rdnPktDQoST8Timeout,'rdnPktDQoSGateCmDel':rdnPktDQoSGateCmDel,'rdnPktDQoSGateCmDereg':rdnPktDQoSGateCmDereg,'rdnPktDQoSGateAdminDel':rdnPktDQoSGateAdminDel,'rdnPktDQoSGateResReassign':rdnPktDQoSGateResReassign,'rdnPktDQoSNotificationObject':rdnPktDQoSNotificationObject,_T:rdnPktDQoSCopsReason,_U:rdnPktDQoSCopsCmsIpAddr,'rdnPktDQoSCopsCmsPortNum':rdnPktDQoSCopsCmsPortNum,'rdnPktDQoSCopsCmsHandleId':rdnPktDQoSCopsCmsHandleId,_V:rdnPktDQoSResReqReason,_K:rdnPktDQoSCmMacAddr,_W:rdnPktDQoSEmergencyReason,_N:rdnPktDQoSClassName,_O:rdnPktDQoSGateId,_X:rdnPktDQoSEmergencyPreemptReason,'rdnPktDQoSNotificationTraps':rdnPktDQoSNotificationTraps,'rdnPktDQoSNotificationTrapsPrefix':rdnPktDQoSNotificationTrapsPrefix,'rdnPktDQoSCopsTrap':rdnPktDQoSCopsTrap,'rdnPktDQoSResReqTrap':rdnPktDQoSResReqTrap,'rdnPktDQoSEmergencyTrap':rdnPktDQoSEmergencyTrap,'rdnPktDQoSEmergencyPreemptTrap':rdnPktDQoSEmergencyPreemptTrap,'rdnPktESNotificationObject':rdnPktESNotificationObject,_Y:rdnPktESReason,_Z:rdnPktESDFIpAddr,_a:rdnPktESDFPortNum,'rdnPktESNotificationTraps':rdnPktESNotificationTraps,'rdnPktESNotificationTrapsPrefix':rdnPktESNotificationTrapsPrefix,'rdnPktESTrap':rdnPktESTrap,'rdnPktRKSNotificationObject':rdnPktRKSNotificationObject,_b:rdnPktRKSReason,_c:rdnPktRKSTransID,_d:rdnPktRKSIPPrimary,_e:rdnPktRKSPortPrimary,_f:rdnPktRKSIPSecondary,_g:rdnPktRKSPortSecondary,_h:rdnPktRKSVersionID,'rdnPktRKSNotificationTraps':rdnPktRKSNotificationTraps,'rdnPktRKSNotificationTrapsPrefix':rdnPktRKSNotificationTrapsPrefix,'rdnPktDQoSRKSTrap':rdnPktDQoSRKSTrap})