_AL='ciscoLesTokenRingGroup'
_AK='ciscoLesCntrlDistGroup'
_AJ='ciscoLesLecsGroup'
_AI='ciscoLesColocatedGroup'
_AH='ciscoLesSubIfGroup'
_AG='ciscoLesClientGroup'
_AF='ciscoLesStatsGroup'
_AE='ciscoLesGroup'
_AD='lesRDRegLecid'
_AC='lesRDRegAtmAddr'
_AB='lesSegmentID'
_AA='lesMacRegLecid'
_A9='lesMacRegAtmAddr'
_A8='lesClientStatus'
_A7='lesClientControlVci'
_A6='lesClientControlVpi'
_A5='lesClientIfIndex'
_A4='lesClientState'
_A3='lesClientAtmAddr'
_A2='lesSubIfNum'
_A1='lesInConfigFails'
_A0='lesInConfigResps'
_z='lesOutConfigReqs'
_y='lesLecsAtmAddr'
_x='lesColocBusAtmAddrActl'
_w='lesColocBusAtmAddrMask'
_v='lesColocBusAtmAddrSpec'
_u='lesInTopolReqs'
_t='lesInNarpReqs'
_s='lesInLearpResps'
_r='lesOutLearpFwd'
_q='lesInLearpBroadcasts'
_p='lesInLearpUcasts'
_o='lesInUnregReqs'
_n='lesRegisLastFailLec'
_m='lesRegisLastFailCause'
_l='lesOutRegisFails'
_k='lesInRegisReqs'
_j='lesJoinLastFailLec'
_i='lesJoinLastFailCause'
_h='lesOutJoinFails'
_g='lesInJoinReqs'
_f='lesInFlushReplies'
_e='lesInErrorLastLec'
_d='lesInErrors'
_c='lesStatus'
_b='lesAdminStatus'
_a='lesOperStatus'
_Z='lesJoinTimeout'
_Y='lesMaxFrm'
_X='lesLanType'
_W='lesUpTime'
_V='lesIfIndex'
_U='lesAtmAddrActual'
_T='lesAtmAddrMask'
_S='lesAtmAddrSpec'
_R='lesRDRegBridgeNum'
_Q='lesRDRegSegmentId'
_P='lesMacRegMacAddress'
_O='lesClientLecid'
_N='inactive'
_M='active'
_L='DisplayString'
_K='lesControlDistVci'
_J='lesControlDistVpi'
_I='OctetString'
_H='not-accessible'
_G='lesIndex'
_F='lesElanName'
_E='read-create'
_D='Integer32'
_C='read-only'
_B='CISCO-LES-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_I,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
CiscoVciInteger,CiscoVpiInteger=mibBuilder.importSymbols('CISCO-BUS-MIB','CiscoVciInteger','CiscoVpiInteger')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
AtmLaneAddress,=mibBuilder.importSymbols('LAN-EMULATION-CLIENT-MIB','AtmLaneAddress')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC',_L,'MacAddress','PhysAddress','RowStatus','TextualConvention','TimeStamp')
ciscoLesMIB=ModuleIdentity((1,3,6,1,4,1,9,9,39))
_CiscoLesMIBObjects_ObjectIdentity=ObjectIdentity
ciscoLesMIBObjects=_CiscoLesMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,39,1))
_Les_ObjectIdentity=ObjectIdentity
les=_Les_ObjectIdentity((1,3,6,1,4,1,9,9,39,1,1))
_LesTable_Object=MibTable
lesTable=_LesTable_Object((1,3,6,1,4,1,9,9,39,1,1,1))
if mibBuilder.loadTexts:lesTable.setStatus(_A)
_LesEntry_Object=MibTableRow
lesEntry=_LesEntry_Object((1,3,6,1,4,1,9,9,39,1,1,1,1))
lesEntry.setIndexNames((0,_B,_F),(0,_B,_G))
if mibBuilder.loadTexts:lesEntry.setStatus(_A)
class _LesElanName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_LesElanName_Type.__name__=_L
_LesElanName_Object=MibTableColumn
lesElanName=_LesElanName_Object((1,3,6,1,4,1,9,9,39,1,1,1,1,1),_LesElanName_Type())
lesElanName.setMaxAccess(_H)
if mibBuilder.loadTexts:lesElanName.setStatus(_A)
class _LesIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_LesIndex_Type.__name__=_D
_LesIndex_Object=MibTableColumn
lesIndex=_LesIndex_Object((1,3,6,1,4,1,9,9,39,1,1,1,1,2),_LesIndex_Type())
lesIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:lesIndex.setStatus(_A)
_LesAtmAddrSpec_Type=AtmLaneAddress
_LesAtmAddrSpec_Object=MibTableColumn
lesAtmAddrSpec=_LesAtmAddrSpec_Object((1,3,6,1,4,1,9,9,39,1,1,1,1,3),_LesAtmAddrSpec_Type())
lesAtmAddrSpec.setMaxAccess(_E)
if mibBuilder.loadTexts:lesAtmAddrSpec.setStatus(_A)
class _LesAtmAddrMask_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(20,20))
_LesAtmAddrMask_Type.__name__=_I
_LesAtmAddrMask_Object=MibTableColumn
lesAtmAddrMask=_LesAtmAddrMask_Object((1,3,6,1,4,1,9,9,39,1,1,1,1,4),_LesAtmAddrMask_Type())
lesAtmAddrMask.setMaxAccess(_E)
if mibBuilder.loadTexts:lesAtmAddrMask.setStatus(_A)
_LesAtmAddrActual_Type=AtmLaneAddress
_LesAtmAddrActual_Object=MibTableColumn
lesAtmAddrActual=_LesAtmAddrActual_Object((1,3,6,1,4,1,9,9,39,1,1,1,1,5),_LesAtmAddrActual_Type())
lesAtmAddrActual.setMaxAccess(_C)
if mibBuilder.loadTexts:lesAtmAddrActual.setStatus(_A)
_LesIfIndex_Type=Integer32
_LesIfIndex_Object=MibTableColumn
lesIfIndex=_LesIfIndex_Object((1,3,6,1,4,1,9,9,39,1,1,1,1,6),_LesIfIndex_Type())
lesIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:lesIfIndex.setStatus(_A)
_LesSubIfNum_Type=Integer32
_LesSubIfNum_Object=MibTableColumn
lesSubIfNum=_LesSubIfNum_Object((1,3,6,1,4,1,9,9,39,1,1,1,1,7),_LesSubIfNum_Type())
lesSubIfNum.setMaxAccess(_E)
if mibBuilder.loadTexts:lesSubIfNum.setStatus(_A)
_LesColocBusAtmAddrSpec_Type=AtmLaneAddress
_LesColocBusAtmAddrSpec_Object=MibTableColumn
lesColocBusAtmAddrSpec=_LesColocBusAtmAddrSpec_Object((1,3,6,1,4,1,9,9,39,1,1,1,1,8),_LesColocBusAtmAddrSpec_Type())
lesColocBusAtmAddrSpec.setMaxAccess(_E)
if mibBuilder.loadTexts:lesColocBusAtmAddrSpec.setStatus(_A)
class _LesColocBusAtmAddrMask_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(20,20))
_LesColocBusAtmAddrMask_Type.__name__=_I
_LesColocBusAtmAddrMask_Object=MibTableColumn
lesColocBusAtmAddrMask=_LesColocBusAtmAddrMask_Object((1,3,6,1,4,1,9,9,39,1,1,1,1,9),_LesColocBusAtmAddrMask_Type())
lesColocBusAtmAddrMask.setMaxAccess(_E)
if mibBuilder.loadTexts:lesColocBusAtmAddrMask.setStatus(_A)
_LesColocBusAtmAddrActl_Type=AtmLaneAddress
_LesColocBusAtmAddrActl_Object=MibTableColumn
lesColocBusAtmAddrActl=_LesColocBusAtmAddrActl_Object((1,3,6,1,4,1,9,9,39,1,1,1,1,10),_LesColocBusAtmAddrActl_Type())
lesColocBusAtmAddrActl.setMaxAccess(_C)
if mibBuilder.loadTexts:lesColocBusAtmAddrActl.setStatus(_A)
_LesUpTime_Type=TimeStamp
_LesUpTime_Object=MibTableColumn
lesUpTime=_LesUpTime_Object((1,3,6,1,4,1,9,9,39,1,1,1,1,11),_LesUpTime_Type())
lesUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:lesUpTime.setStatus(_A)
class _LesLanType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('dot3',1),('dot5',2)))
_LesLanType_Type.__name__=_D
_LesLanType_Object=MibTableColumn
lesLanType=_LesLanType_Object((1,3,6,1,4,1,9,9,39,1,1,1,1,12),_LesLanType_Type())
lesLanType.setMaxAccess(_E)
if mibBuilder.loadTexts:lesLanType.setStatus(_A)
class _LesMaxFrm_Type(Integer32):defaultValue=1516;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1516,4544,9234,18190)));namedValues=NamedValues(*(('dot3',1516),('tr4Mb',4544),('rfc1626',9234),('tr16Mb',18190)))
_LesMaxFrm_Type.__name__=_D
_LesMaxFrm_Object=MibTableColumn
lesMaxFrm=_LesMaxFrm_Object((1,3,6,1,4,1,9,9,39,1,1,1,1,13),_LesMaxFrm_Type())
lesMaxFrm.setMaxAccess(_E)
if mibBuilder.loadTexts:lesMaxFrm.setStatus(_A)
class _LesJoinTimeout_Type(Integer32):defaultValue=120;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,300))
_LesJoinTimeout_Type.__name__=_D
_LesJoinTimeout_Object=MibTableColumn
lesJoinTimeout=_LesJoinTimeout_Object((1,3,6,1,4,1,9,9,39,1,1,1,1,14),_LesJoinTimeout_Type())
lesJoinTimeout.setMaxAccess(_E)
if mibBuilder.loadTexts:lesJoinTimeout.setStatus(_A)
if mibBuilder.loadTexts:lesJoinTimeout.setUnits('seconds')
_LesLecsAtmAddr_Type=AtmLaneAddress
_LesLecsAtmAddr_Object=MibTableColumn
lesLecsAtmAddr=_LesLecsAtmAddr_Object((1,3,6,1,4,1,9,9,39,1,1,1,1,15),_LesLecsAtmAddr_Type())
lesLecsAtmAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:lesLecsAtmAddr.setStatus(_A)
_LesControlDistVpi_Type=CiscoVpiInteger
_LesControlDistVpi_Object=MibTableColumn
lesControlDistVpi=_LesControlDistVpi_Object((1,3,6,1,4,1,9,9,39,1,1,1,1,16),_LesControlDistVpi_Type())
lesControlDistVpi.setMaxAccess(_C)
if mibBuilder.loadTexts:lesControlDistVpi.setStatus(_A)
_LesControlDistVci_Type=CiscoVciInteger
_LesControlDistVci_Object=MibTableColumn
lesControlDistVci=_LesControlDistVci_Object((1,3,6,1,4,1,9,9,39,1,1,1,1,17),_LesControlDistVci_Type())
lesControlDistVci.setMaxAccess(_C)
if mibBuilder.loadTexts:lesControlDistVci.setStatus(_A)
class _LesOperStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_LesOperStatus_Type.__name__=_D
_LesOperStatus_Object=MibTableColumn
lesOperStatus=_LesOperStatus_Object((1,3,6,1,4,1,9,9,39,1,1,1,1,18),_LesOperStatus_Type())
lesOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:lesOperStatus.setStatus(_A)
class _LesAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_LesAdminStatus_Type.__name__=_D
_LesAdminStatus_Object=MibTableColumn
lesAdminStatus=_LesAdminStatus_Object((1,3,6,1,4,1,9,9,39,1,1,1,1,19),_LesAdminStatus_Type())
lesAdminStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:lesAdminStatus.setStatus(_A)
_LesStatus_Type=RowStatus
_LesStatus_Object=MibTableColumn
lesStatus=_LesStatus_Object((1,3,6,1,4,1,9,9,39,1,1,1,1,20),_LesStatus_Type())
lesStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:lesStatus.setStatus(_A)
class _LesSegmentID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_LesSegmentID_Type.__name__=_D
_LesSegmentID_Object=MibTableColumn
lesSegmentID=_LesSegmentID_Object((1,3,6,1,4,1,9,9,39,1,1,1,1,21),_LesSegmentID_Type())
lesSegmentID.setMaxAccess(_E)
if mibBuilder.loadTexts:lesSegmentID.setStatus(_A)
_LesStatsTable_Object=MibTable
lesStatsTable=_LesStatsTable_Object((1,3,6,1,4,1,9,9,39,1,1,2))
if mibBuilder.loadTexts:lesStatsTable.setStatus(_A)
_LesStatsEntry_Object=MibTableRow
lesStatsEntry=_LesStatsEntry_Object((1,3,6,1,4,1,9,9,39,1,1,2,1))
lesStatsEntry.setIndexNames((0,_B,_F),(0,_B,_G))
if mibBuilder.loadTexts:lesStatsEntry.setStatus(_A)
_LesInErrors_Type=Counter32
_LesInErrors_Object=MibTableColumn
lesInErrors=_LesInErrors_Object((1,3,6,1,4,1,9,9,39,1,1,2,1,1),_LesInErrors_Type())
lesInErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:lesInErrors.setStatus(_A)
_LesInErrorLastLec_Type=AtmLaneAddress
_LesInErrorLastLec_Object=MibTableColumn
lesInErrorLastLec=_LesInErrorLastLec_Object((1,3,6,1,4,1,9,9,39,1,1,2,1,2),_LesInErrorLastLec_Type())
lesInErrorLastLec.setMaxAccess(_C)
if mibBuilder.loadTexts:lesInErrorLastLec.setStatus(_A)
_LesInFlushReplies_Type=Counter32
_LesInFlushReplies_Object=MibTableColumn
lesInFlushReplies=_LesInFlushReplies_Object((1,3,6,1,4,1,9,9,39,1,1,2,1,3),_LesInFlushReplies_Type())
lesInFlushReplies.setMaxAccess(_C)
if mibBuilder.loadTexts:lesInFlushReplies.setStatus(_A)
_LesInJoinReqs_Type=Counter32
_LesInJoinReqs_Object=MibTableColumn
lesInJoinReqs=_LesInJoinReqs_Object((1,3,6,1,4,1,9,9,39,1,1,2,1,4),_LesInJoinReqs_Type())
lesInJoinReqs.setMaxAccess(_C)
if mibBuilder.loadTexts:lesInJoinReqs.setStatus(_A)
_LesOutJoinFails_Type=Counter32
_LesOutJoinFails_Object=MibTableColumn
lesOutJoinFails=_LesOutJoinFails_Object((1,3,6,1,4,1,9,9,39,1,1,2,1,5),_LesOutJoinFails_Type())
lesOutJoinFails.setMaxAccess(_C)
if mibBuilder.loadTexts:lesOutJoinFails.setStatus(_A)
_LesJoinLastFailCause_Type=Integer32
_LesJoinLastFailCause_Object=MibTableColumn
lesJoinLastFailCause=_LesJoinLastFailCause_Object((1,3,6,1,4,1,9,9,39,1,1,2,1,6),_LesJoinLastFailCause_Type())
lesJoinLastFailCause.setMaxAccess(_C)
if mibBuilder.loadTexts:lesJoinLastFailCause.setStatus(_A)
_LesJoinLastFailLec_Type=AtmLaneAddress
_LesJoinLastFailLec_Object=MibTableColumn
lesJoinLastFailLec=_LesJoinLastFailLec_Object((1,3,6,1,4,1,9,9,39,1,1,2,1,7),_LesJoinLastFailLec_Type())
lesJoinLastFailLec.setMaxAccess(_C)
if mibBuilder.loadTexts:lesJoinLastFailLec.setStatus(_A)
_LesOutConfigReqs_Type=Counter32
_LesOutConfigReqs_Object=MibTableColumn
lesOutConfigReqs=_LesOutConfigReqs_Object((1,3,6,1,4,1,9,9,39,1,1,2,1,8),_LesOutConfigReqs_Type())
lesOutConfigReqs.setMaxAccess(_C)
if mibBuilder.loadTexts:lesOutConfigReqs.setStatus(_A)
_LesInConfigResps_Type=Counter32
_LesInConfigResps_Object=MibTableColumn
lesInConfigResps=_LesInConfigResps_Object((1,3,6,1,4,1,9,9,39,1,1,2,1,9),_LesInConfigResps_Type())
lesInConfigResps.setMaxAccess(_C)
if mibBuilder.loadTexts:lesInConfigResps.setStatus(_A)
_LesInConfigFails_Type=Counter32
_LesInConfigFails_Object=MibTableColumn
lesInConfigFails=_LesInConfigFails_Object((1,3,6,1,4,1,9,9,39,1,1,2,1,10),_LesInConfigFails_Type())
lesInConfigFails.setMaxAccess(_C)
if mibBuilder.loadTexts:lesInConfigFails.setStatus(_A)
_LesInRegisReqs_Type=Counter32
_LesInRegisReqs_Object=MibTableColumn
lesInRegisReqs=_LesInRegisReqs_Object((1,3,6,1,4,1,9,9,39,1,1,2,1,11),_LesInRegisReqs_Type())
lesInRegisReqs.setMaxAccess(_C)
if mibBuilder.loadTexts:lesInRegisReqs.setStatus(_A)
_LesOutRegisFails_Type=Counter32
_LesOutRegisFails_Object=MibTableColumn
lesOutRegisFails=_LesOutRegisFails_Object((1,3,6,1,4,1,9,9,39,1,1,2,1,12),_LesOutRegisFails_Type())
lesOutRegisFails.setMaxAccess(_C)
if mibBuilder.loadTexts:lesOutRegisFails.setStatus(_A)
_LesRegisLastFailCause_Type=Integer32
_LesRegisLastFailCause_Object=MibTableColumn
lesRegisLastFailCause=_LesRegisLastFailCause_Object((1,3,6,1,4,1,9,9,39,1,1,2,1,13),_LesRegisLastFailCause_Type())
lesRegisLastFailCause.setMaxAccess(_C)
if mibBuilder.loadTexts:lesRegisLastFailCause.setStatus(_A)
_LesRegisLastFailLec_Type=AtmLaneAddress
_LesRegisLastFailLec_Object=MibTableColumn
lesRegisLastFailLec=_LesRegisLastFailLec_Object((1,3,6,1,4,1,9,9,39,1,1,2,1,14),_LesRegisLastFailLec_Type())
lesRegisLastFailLec.setMaxAccess(_C)
if mibBuilder.loadTexts:lesRegisLastFailLec.setStatus(_A)
_LesInUnregReqs_Type=Counter32
_LesInUnregReqs_Object=MibTableColumn
lesInUnregReqs=_LesInUnregReqs_Object((1,3,6,1,4,1,9,9,39,1,1,2,1,15),_LesInUnregReqs_Type())
lesInUnregReqs.setMaxAccess(_C)
if mibBuilder.loadTexts:lesInUnregReqs.setStatus(_A)
_LesInLearpUcasts_Type=Counter32
_LesInLearpUcasts_Object=MibTableColumn
lesInLearpUcasts=_LesInLearpUcasts_Object((1,3,6,1,4,1,9,9,39,1,1,2,1,16),_LesInLearpUcasts_Type())
lesInLearpUcasts.setMaxAccess(_C)
if mibBuilder.loadTexts:lesInLearpUcasts.setStatus(_A)
_LesInLearpBroadcasts_Type=Counter32
_LesInLearpBroadcasts_Object=MibTableColumn
lesInLearpBroadcasts=_LesInLearpBroadcasts_Object((1,3,6,1,4,1,9,9,39,1,1,2,1,17),_LesInLearpBroadcasts_Type())
lesInLearpBroadcasts.setMaxAccess(_C)
if mibBuilder.loadTexts:lesInLearpBroadcasts.setStatus(_A)
_LesOutLearpFwd_Type=Counter32
_LesOutLearpFwd_Object=MibTableColumn
lesOutLearpFwd=_LesOutLearpFwd_Object((1,3,6,1,4,1,9,9,39,1,1,2,1,18),_LesOutLearpFwd_Type())
lesOutLearpFwd.setMaxAccess(_C)
if mibBuilder.loadTexts:lesOutLearpFwd.setStatus(_A)
_LesInLearpResps_Type=Counter32
_LesInLearpResps_Object=MibTableColumn
lesInLearpResps=_LesInLearpResps_Object((1,3,6,1,4,1,9,9,39,1,1,2,1,19),_LesInLearpResps_Type())
lesInLearpResps.setMaxAccess(_C)
if mibBuilder.loadTexts:lesInLearpResps.setStatus(_A)
_LesInNarpReqs_Type=Counter32
_LesInNarpReqs_Object=MibTableColumn
lesInNarpReqs=_LesInNarpReqs_Object((1,3,6,1,4,1,9,9,39,1,1,2,1,20),_LesInNarpReqs_Type())
lesInNarpReqs.setMaxAccess(_C)
if mibBuilder.loadTexts:lesInNarpReqs.setStatus(_A)
_LesInTopolReqs_Type=Counter32
_LesInTopolReqs_Object=MibTableColumn
lesInTopolReqs=_LesInTopolReqs_Object((1,3,6,1,4,1,9,9,39,1,1,2,1,21),_LesInTopolReqs_Type())
lesInTopolReqs.setMaxAccess(_C)
if mibBuilder.loadTexts:lesInTopolReqs.setStatus(_A)
_LeClient_ObjectIdentity=ObjectIdentity
leClient=_LeClient_ObjectIdentity((1,3,6,1,4,1,9,9,39,1,2))
_LesClientTable_Object=MibTable
lesClientTable=_LesClientTable_Object((1,3,6,1,4,1,9,9,39,1,2,1))
if mibBuilder.loadTexts:lesClientTable.setStatus(_A)
_LesClientEntry_Object=MibTableRow
lesClientEntry=_LesClientEntry_Object((1,3,6,1,4,1,9,9,39,1,2,1,1))
lesClientEntry.setIndexNames((0,_B,_F),(0,_B,_G),(0,_B,_O))
if mibBuilder.loadTexts:lesClientEntry.setStatus(_A)
class _LesClientLecid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65279))
_LesClientLecid_Type.__name__=_D
_LesClientLecid_Object=MibTableColumn
lesClientLecid=_LesClientLecid_Object((1,3,6,1,4,1,9,9,39,1,2,1,1,1),_LesClientLecid_Type())
lesClientLecid.setMaxAccess(_H)
if mibBuilder.loadTexts:lesClientLecid.setStatus(_A)
_LesClientAtmAddr_Type=AtmLaneAddress
_LesClientAtmAddr_Object=MibTableColumn
lesClientAtmAddr=_LesClientAtmAddr_Object((1,3,6,1,4,1,9,9,39,1,2,1,1,2),_LesClientAtmAddr_Type())
lesClientAtmAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:lesClientAtmAddr.setStatus(_A)
class _LesClientState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('connected',1),('joinRecv',2),('verify',3),('addLec',4),('busConnect',5),('operational',6),('terminating',7)))
_LesClientState_Type.__name__=_D
_LesClientState_Object=MibTableColumn
lesClientState=_LesClientState_Object((1,3,6,1,4,1,9,9,39,1,2,1,1,3),_LesClientState_Type())
lesClientState.setMaxAccess(_C)
if mibBuilder.loadTexts:lesClientState.setStatus(_A)
_LesClientIfIndex_Type=Integer32
_LesClientIfIndex_Object=MibTableColumn
lesClientIfIndex=_LesClientIfIndex_Object((1,3,6,1,4,1,9,9,39,1,2,1,1,4),_LesClientIfIndex_Type())
lesClientIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:lesClientIfIndex.setStatus(_A)
_LesClientControlVpi_Type=CiscoVpiInteger
_LesClientControlVpi_Object=MibTableColumn
lesClientControlVpi=_LesClientControlVpi_Object((1,3,6,1,4,1,9,9,39,1,2,1,1,5),_LesClientControlVpi_Type())
lesClientControlVpi.setMaxAccess(_C)
if mibBuilder.loadTexts:lesClientControlVpi.setStatus(_A)
_LesClientControlVci_Type=CiscoVciInteger
_LesClientControlVci_Object=MibTableColumn
lesClientControlVci=_LesClientControlVci_Object((1,3,6,1,4,1,9,9,39,1,2,1,1,6),_LesClientControlVci_Type())
lesClientControlVci.setMaxAccess(_C)
if mibBuilder.loadTexts:lesClientControlVci.setStatus(_A)
_LesClientStatus_Type=RowStatus
_LesClientStatus_Object=MibTableColumn
lesClientStatus=_LesClientStatus_Object((1,3,6,1,4,1,9,9,39,1,2,1,1,7),_LesClientStatus_Type())
lesClientStatus.setMaxAccess('read-write')
if mibBuilder.loadTexts:lesClientStatus.setStatus(_A)
_Register_ObjectIdentity=ObjectIdentity
register=_Register_ObjectIdentity((1,3,6,1,4,1,9,9,39,1,3))
_LesMacRegTable_Object=MibTable
lesMacRegTable=_LesMacRegTable_Object((1,3,6,1,4,1,9,9,39,1,3,1))
if mibBuilder.loadTexts:lesMacRegTable.setStatus(_A)
_LesMacRegEntry_Object=MibTableRow
lesMacRegEntry=_LesMacRegEntry_Object((1,3,6,1,4,1,9,9,39,1,3,1,1))
lesMacRegEntry.setIndexNames((0,_B,_F),(0,_B,_G),(0,_B,_P))
if mibBuilder.loadTexts:lesMacRegEntry.setStatus(_A)
_LesMacRegMacAddress_Type=MacAddress
_LesMacRegMacAddress_Object=MibTableColumn
lesMacRegMacAddress=_LesMacRegMacAddress_Object((1,3,6,1,4,1,9,9,39,1,3,1,1,1),_LesMacRegMacAddress_Type())
lesMacRegMacAddress.setMaxAccess(_H)
if mibBuilder.loadTexts:lesMacRegMacAddress.setStatus(_A)
_LesMacRegAtmAddr_Type=AtmLaneAddress
_LesMacRegAtmAddr_Object=MibTableColumn
lesMacRegAtmAddr=_LesMacRegAtmAddr_Object((1,3,6,1,4,1,9,9,39,1,3,1,1,3),_LesMacRegAtmAddr_Type())
lesMacRegAtmAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:lesMacRegAtmAddr.setStatus(_A)
class _LesMacRegLecid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65279))
_LesMacRegLecid_Type.__name__=_D
_LesMacRegLecid_Object=MibTableColumn
lesMacRegLecid=_LesMacRegLecid_Object((1,3,6,1,4,1,9,9,39,1,3,1,1,4),_LesMacRegLecid_Type())
lesMacRegLecid.setMaxAccess(_C)
if mibBuilder.loadTexts:lesMacRegLecid.setStatus(_A)
_LesRDRegTable_Object=MibTable
lesRDRegTable=_LesRDRegTable_Object((1,3,6,1,4,1,9,9,39,1,3,2))
if mibBuilder.loadTexts:lesRDRegTable.setStatus(_A)
_LesRDRegEntry_Object=MibTableRow
lesRDRegEntry=_LesRDRegEntry_Object((1,3,6,1,4,1,9,9,39,1,3,2,1))
lesRDRegEntry.setIndexNames((0,_B,_F),(0,_B,_G),(0,_B,_Q),(0,_B,_R))
if mibBuilder.loadTexts:lesRDRegEntry.setStatus(_A)
class _LesRDRegSegmentId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_LesRDRegSegmentId_Type.__name__=_D
_LesRDRegSegmentId_Object=MibTableColumn
lesRDRegSegmentId=_LesRDRegSegmentId_Object((1,3,6,1,4,1,9,9,39,1,3,2,1,1),_LesRDRegSegmentId_Type())
lesRDRegSegmentId.setMaxAccess(_H)
if mibBuilder.loadTexts:lesRDRegSegmentId.setStatus(_A)
class _LesRDRegBridgeNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_LesRDRegBridgeNum_Type.__name__=_D
_LesRDRegBridgeNum_Object=MibTableColumn
lesRDRegBridgeNum=_LesRDRegBridgeNum_Object((1,3,6,1,4,1,9,9,39,1,3,2,1,2),_LesRDRegBridgeNum_Type())
lesRDRegBridgeNum.setMaxAccess(_H)
if mibBuilder.loadTexts:lesRDRegBridgeNum.setStatus(_A)
_LesRDRegAtmAddr_Type=AtmLaneAddress
_LesRDRegAtmAddr_Object=MibTableColumn
lesRDRegAtmAddr=_LesRDRegAtmAddr_Object((1,3,6,1,4,1,9,9,39,1,3,2,1,3),_LesRDRegAtmAddr_Type())
lesRDRegAtmAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:lesRDRegAtmAddr.setStatus(_A)
class _LesRDRegLecid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65279))
_LesRDRegLecid_Type.__name__=_D
_LesRDRegLecid_Object=MibTableColumn
lesRDRegLecid=_LesRDRegLecid_Object((1,3,6,1,4,1,9,9,39,1,3,2,1,4),_LesRDRegLecid_Type())
lesRDRegLecid.setMaxAccess(_C)
if mibBuilder.loadTexts:lesRDRegLecid.setStatus(_A)
_CiscoLesMIBConformance_ObjectIdentity=ObjectIdentity
ciscoLesMIBConformance=_CiscoLesMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,39,2))
_CiscoLesMIBGroups_ObjectIdentity=ObjectIdentity
ciscoLesMIBGroups=_CiscoLesMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,39,2,1))
_CiscoLesMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoLesMIBCompliances=_CiscoLesMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,39,2,2))
ciscoLesGroup=ObjectGroup((1,3,6,1,4,1,9,9,39,2,1,1))
ciscoLesGroup.setObjects(*((_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_J),(_B,_K),(_B,_a),(_B,_b),(_B,_c)))
if mibBuilder.loadTexts:ciscoLesGroup.setStatus(_A)
ciscoLesStatsGroup=ObjectGroup((1,3,6,1,4,1,9,9,39,2,1,2))
ciscoLesStatsGroup.setObjects(*((_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u)))
if mibBuilder.loadTexts:ciscoLesStatsGroup.setStatus(_A)
ciscoLesColocatedGroup=ObjectGroup((1,3,6,1,4,1,9,9,39,2,1,3))
ciscoLesColocatedGroup.setObjects(*((_B,_v),(_B,_w),(_B,_x)))
if mibBuilder.loadTexts:ciscoLesColocatedGroup.setStatus(_A)
ciscoLesLecsGroup=ObjectGroup((1,3,6,1,4,1,9,9,39,2,1,4))
ciscoLesLecsGroup.setObjects(*((_B,_y),(_B,_z),(_B,_A0),(_B,_A1)))
if mibBuilder.loadTexts:ciscoLesLecsGroup.setStatus(_A)
ciscoLesCntrlDistGroup=ObjectGroup((1,3,6,1,4,1,9,9,39,2,1,5))
ciscoLesCntrlDistGroup.setObjects(*((_B,_J),(_B,_K)))
if mibBuilder.loadTexts:ciscoLesCntrlDistGroup.setStatus(_A)
ciscoLesSubIfGroup=ObjectGroup((1,3,6,1,4,1,9,9,39,2,1,6))
ciscoLesSubIfGroup.setObjects((_B,_A2))
if mibBuilder.loadTexts:ciscoLesSubIfGroup.setStatus(_A)
ciscoLesClientGroup=ObjectGroup((1,3,6,1,4,1,9,9,39,2,1,7))
ciscoLesClientGroup.setObjects(*((_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA)))
if mibBuilder.loadTexts:ciscoLesClientGroup.setStatus(_A)
ciscoLesTokenRingGroup=ObjectGroup((1,3,6,1,4,1,9,9,39,2,1,8))
ciscoLesTokenRingGroup.setObjects(*((_B,_AB),(_B,_AC),(_B,_AD)))
if mibBuilder.loadTexts:ciscoLesTokenRingGroup.setStatus(_A)
ciscoLesMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,39,2,2,1))
ciscoLesMIBCompliance.setObjects(*((_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL)))
if mibBuilder.loadTexts:ciscoLesMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoLesMIB':ciscoLesMIB,'ciscoLesMIBObjects':ciscoLesMIBObjects,'les':les,'lesTable':lesTable,'lesEntry':lesEntry,_F:lesElanName,_G:lesIndex,_S:lesAtmAddrSpec,_T:lesAtmAddrMask,_U:lesAtmAddrActual,_V:lesIfIndex,_A2:lesSubIfNum,_v:lesColocBusAtmAddrSpec,_w:lesColocBusAtmAddrMask,_x:lesColocBusAtmAddrActl,_W:lesUpTime,_X:lesLanType,_Y:lesMaxFrm,_Z:lesJoinTimeout,_y:lesLecsAtmAddr,_J:lesControlDistVpi,_K:lesControlDistVci,_a:lesOperStatus,_b:lesAdminStatus,_c:lesStatus,_AB:lesSegmentID,'lesStatsTable':lesStatsTable,'lesStatsEntry':lesStatsEntry,_d:lesInErrors,_e:lesInErrorLastLec,_f:lesInFlushReplies,_g:lesInJoinReqs,_h:lesOutJoinFails,_i:lesJoinLastFailCause,_j:lesJoinLastFailLec,_z:lesOutConfigReqs,_A0:lesInConfigResps,_A1:lesInConfigFails,_k:lesInRegisReqs,_l:lesOutRegisFails,_m:lesRegisLastFailCause,_n:lesRegisLastFailLec,_o:lesInUnregReqs,_p:lesInLearpUcasts,_q:lesInLearpBroadcasts,_r:lesOutLearpFwd,_s:lesInLearpResps,_t:lesInNarpReqs,_u:lesInTopolReqs,'leClient':leClient,'lesClientTable':lesClientTable,'lesClientEntry':lesClientEntry,_O:lesClientLecid,_A3:lesClientAtmAddr,_A4:lesClientState,_A5:lesClientIfIndex,_A6:lesClientControlVpi,_A7:lesClientControlVci,_A8:lesClientStatus,'register':register,'lesMacRegTable':lesMacRegTable,'lesMacRegEntry':lesMacRegEntry,_P:lesMacRegMacAddress,_A9:lesMacRegAtmAddr,_AA:lesMacRegLecid,'lesRDRegTable':lesRDRegTable,'lesRDRegEntry':lesRDRegEntry,_Q:lesRDRegSegmentId,_R:lesRDRegBridgeNum,_AC:lesRDRegAtmAddr,_AD:lesRDRegLecid,'ciscoLesMIBConformance':ciscoLesMIBConformance,'ciscoLesMIBGroups':ciscoLesMIBGroups,_AE:ciscoLesGroup,_AF:ciscoLesStatsGroup,_AI:ciscoLesColocatedGroup,_AJ:ciscoLesLecsGroup,_AK:ciscoLesCntrlDistGroup,_AH:ciscoLesSubIfGroup,_AG:ciscoLesClientGroup,_AL:ciscoLesTokenRingGroup,'ciscoLesMIBCompliances':ciscoLesMIBCompliances,'ciscoLesMIBCompliance':ciscoLesMIBCompliance})