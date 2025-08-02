_l='ciscoVqeSNotifGroup'
_k='ciscoVqeSCapacityGroup'
_j='ciscoVqeSRCCGroup'
_i='ciscoVqeSERGroup'
_h='ciscoVqeSChannelGroup'
_g='ciscoVqeSControlGroup'
_f='cvqsChannelDown'
_e='cvqsChannelUp'
_d='cvqsRejectedRCCs'
_c='cvqsRejectedERs'
_b='cvqsRejectedRTCPs'
_a='cvqsTotalRTCPReceivers'
_Z='cvqsTotalRefusedRCCs'
_Y='cvqsTotalAcceptedRCCs'
_X='cvqsTotalReceivedRCCs'
_W='cvqsTotalSentERPkts'
_V='cvqsTotalReceivedERPkts'
_U='cvqsTotalReceivedInvalidERMsgs'
_T='cvqsTotalReceivedERMsgs'
_S='cvqsChannelMemberPopulation'
_R='cvqsChannelStatus'
_Q='cvqsLastUpdatedTime'
_P='cvqsActiveChannels'
_O='cvqsNumberofChannels'
_N='cvqsNotificationsEnable'
_M='ER packets'
_L='cvqsChannelIndex'
_K='TruthValue'
_J='Unsigned32'
_I='Integer32'
_H='ER requests'
_G='cvqsChannelMulticastPort'
_F='cvqsChannelMulticastIPAddr'
_E='cvqsChannelMulticastIPType'
_D='RCC requests'
_C='read-only'
_B='current'
_A='CISCO-VQES-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
InetAddress,InetAddressType,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType','InetPortNumber')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_I,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_J,'iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention',_K)
ciscoVqeSMIB=ModuleIdentity((1,3,6,1,4,1,9,9,942))
if mibBuilder.loadTexts:ciscoVqeSMIB.setRevisions(('2010-01-14 11:10',))
_CiscoVqeSMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoVqeSMIBNotifs=_CiscoVqeSMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,942,0))
_CiscoVqeSMIBObjects_ObjectIdentity=ObjectIdentity
ciscoVqeSMIBObjects=_CiscoVqeSMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,942,1))
_CvqsControlInfo_ObjectIdentity=ObjectIdentity
cvqsControlInfo=_CvqsControlInfo_ObjectIdentity((1,3,6,1,4,1,9,9,942,1,1))
class _CvqsNotificationsEnable_Type(TruthValue):defaultValue=2
_CvqsNotificationsEnable_Type.__name__=_K
_CvqsNotificationsEnable_Object=MibScalar
cvqsNotificationsEnable=_CvqsNotificationsEnable_Object((1,3,6,1,4,1,9,9,942,1,1,1),_CvqsNotificationsEnable_Type())
cvqsNotificationsEnable.setMaxAccess('read-write')
if mibBuilder.loadTexts:cvqsNotificationsEnable.setStatus(_B)
_CvqsChannelInfo_ObjectIdentity=ObjectIdentity
cvqsChannelInfo=_CvqsChannelInfo_ObjectIdentity((1,3,6,1,4,1,9,9,942,1,2))
_CvqsNumberofChannels_Type=Gauge32
_CvqsNumberofChannels_Object=MibScalar
cvqsNumberofChannels=_CvqsNumberofChannels_Object((1,3,6,1,4,1,9,9,942,1,2,1),_CvqsNumberofChannels_Type())
cvqsNumberofChannels.setMaxAccess(_C)
if mibBuilder.loadTexts:cvqsNumberofChannels.setStatus(_B)
_CvqsActiveChannels_Type=Gauge32
_CvqsActiveChannels_Object=MibScalar
cvqsActiveChannels=_CvqsActiveChannels_Object((1,3,6,1,4,1,9,9,942,1,2,2),_CvqsActiveChannels_Type())
cvqsActiveChannels.setMaxAccess(_C)
if mibBuilder.loadTexts:cvqsActiveChannels.setStatus(_B)
_CvqsLastUpdatedTime_Type=DateAndTime
_CvqsLastUpdatedTime_Object=MibScalar
cvqsLastUpdatedTime=_CvqsLastUpdatedTime_Object((1,3,6,1,4,1,9,9,942,1,2,3),_CvqsLastUpdatedTime_Type())
cvqsLastUpdatedTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cvqsLastUpdatedTime.setStatus(_B)
_CvqsChannelTable_Object=MibTable
cvqsChannelTable=_CvqsChannelTable_Object((1,3,6,1,4,1,9,9,942,1,2,4))
if mibBuilder.loadTexts:cvqsChannelTable.setStatus(_B)
_CvqsChannelTableEntry_Object=MibTableRow
cvqsChannelTableEntry=_CvqsChannelTableEntry_Object((1,3,6,1,4,1,9,9,942,1,2,4,1))
cvqsChannelTableEntry.setIndexNames((0,_A,_L))
if mibBuilder.loadTexts:cvqsChannelTableEntry.setStatus(_B)
class _CvqsChannelIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CvqsChannelIndex_Type.__name__=_J
_CvqsChannelIndex_Object=MibTableColumn
cvqsChannelIndex=_CvqsChannelIndex_Object((1,3,6,1,4,1,9,9,942,1,2,4,1,1),_CvqsChannelIndex_Type())
cvqsChannelIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:cvqsChannelIndex.setStatus(_B)
_CvqsChannelMulticastIPType_Type=InetAddressType
_CvqsChannelMulticastIPType_Object=MibTableColumn
cvqsChannelMulticastIPType=_CvqsChannelMulticastIPType_Object((1,3,6,1,4,1,9,9,942,1,2,4,1,2),_CvqsChannelMulticastIPType_Type())
cvqsChannelMulticastIPType.setMaxAccess(_C)
if mibBuilder.loadTexts:cvqsChannelMulticastIPType.setStatus(_B)
_CvqsChannelMulticastIPAddr_Type=InetAddress
_CvqsChannelMulticastIPAddr_Object=MibTableColumn
cvqsChannelMulticastIPAddr=_CvqsChannelMulticastIPAddr_Object((1,3,6,1,4,1,9,9,942,1,2,4,1,3),_CvqsChannelMulticastIPAddr_Type())
cvqsChannelMulticastIPAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:cvqsChannelMulticastIPAddr.setStatus(_B)
_CvqsChannelMulticastPort_Type=InetPortNumber
_CvqsChannelMulticastPort_Object=MibTableColumn
cvqsChannelMulticastPort=_CvqsChannelMulticastPort_Object((1,3,6,1,4,1,9,9,942,1,2,4,1,4),_CvqsChannelMulticastPort_Type())
cvqsChannelMulticastPort.setMaxAccess(_C)
if mibBuilder.loadTexts:cvqsChannelMulticastPort.setStatus(_B)
class _CvqsChannelStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('active',1),('inactive',2),('inoperative',3)))
_CvqsChannelStatus_Type.__name__=_I
_CvqsChannelStatus_Object=MibTableColumn
cvqsChannelStatus=_CvqsChannelStatus_Object((1,3,6,1,4,1,9,9,942,1,2,4,1,5),_CvqsChannelStatus_Type())
cvqsChannelStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cvqsChannelStatus.setStatus(_B)
_CvqsChannelMemberPopulation_Type=Gauge32
_CvqsChannelMemberPopulation_Object=MibTableColumn
cvqsChannelMemberPopulation=_CvqsChannelMemberPopulation_Object((1,3,6,1,4,1,9,9,942,1,2,4,1,6),_CvqsChannelMemberPopulation_Type())
cvqsChannelMemberPopulation.setMaxAccess(_C)
if mibBuilder.loadTexts:cvqsChannelMemberPopulation.setStatus(_B)
_CvqsErrorRepair_ObjectIdentity=ObjectIdentity
cvqsErrorRepair=_CvqsErrorRepair_ObjectIdentity((1,3,6,1,4,1,9,9,942,1,3))
_CvqsTotalReceivedERMsgs_Type=Counter64
_CvqsTotalReceivedERMsgs_Object=MibScalar
cvqsTotalReceivedERMsgs=_CvqsTotalReceivedERMsgs_Object((1,3,6,1,4,1,9,9,942,1,3,1),_CvqsTotalReceivedERMsgs_Type())
cvqsTotalReceivedERMsgs.setMaxAccess(_C)
if mibBuilder.loadTexts:cvqsTotalReceivedERMsgs.setStatus(_B)
if mibBuilder.loadTexts:cvqsTotalReceivedERMsgs.setUnits(_H)
_CvqsTotalReceivedInvalidERMsgs_Type=Counter64
_CvqsTotalReceivedInvalidERMsgs_Object=MibScalar
cvqsTotalReceivedInvalidERMsgs=_CvqsTotalReceivedInvalidERMsgs_Object((1,3,6,1,4,1,9,9,942,1,3,2),_CvqsTotalReceivedInvalidERMsgs_Type())
cvqsTotalReceivedInvalidERMsgs.setMaxAccess(_C)
if mibBuilder.loadTexts:cvqsTotalReceivedInvalidERMsgs.setStatus(_B)
if mibBuilder.loadTexts:cvqsTotalReceivedInvalidERMsgs.setUnits(_H)
_CvqsTotalReceivedERPkts_Type=Counter64
_CvqsTotalReceivedERPkts_Object=MibScalar
cvqsTotalReceivedERPkts=_CvqsTotalReceivedERPkts_Object((1,3,6,1,4,1,9,9,942,1,3,3),_CvqsTotalReceivedERPkts_Type())
cvqsTotalReceivedERPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cvqsTotalReceivedERPkts.setStatus(_B)
if mibBuilder.loadTexts:cvqsTotalReceivedERPkts.setUnits(_M)
_CvqsTotalSentERPkts_Type=Counter64
_CvqsTotalSentERPkts_Object=MibScalar
cvqsTotalSentERPkts=_CvqsTotalSentERPkts_Object((1,3,6,1,4,1,9,9,942,1,3,4),_CvqsTotalSentERPkts_Type())
cvqsTotalSentERPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cvqsTotalSentERPkts.setStatus(_B)
if mibBuilder.loadTexts:cvqsTotalSentERPkts.setUnits(_M)
_CvqsRCC_ObjectIdentity=ObjectIdentity
cvqsRCC=_CvqsRCC_ObjectIdentity((1,3,6,1,4,1,9,9,942,1,4))
_CvqsTotalReceivedRCCs_Type=Counter64
_CvqsTotalReceivedRCCs_Object=MibScalar
cvqsTotalReceivedRCCs=_CvqsTotalReceivedRCCs_Object((1,3,6,1,4,1,9,9,942,1,4,1),_CvqsTotalReceivedRCCs_Type())
cvqsTotalReceivedRCCs.setMaxAccess(_C)
if mibBuilder.loadTexts:cvqsTotalReceivedRCCs.setStatus(_B)
if mibBuilder.loadTexts:cvqsTotalReceivedRCCs.setUnits(_D)
_CvqsTotalAcceptedRCCs_Type=Counter64
_CvqsTotalAcceptedRCCs_Object=MibScalar
cvqsTotalAcceptedRCCs=_CvqsTotalAcceptedRCCs_Object((1,3,6,1,4,1,9,9,942,1,4,2),_CvqsTotalAcceptedRCCs_Type())
cvqsTotalAcceptedRCCs.setMaxAccess(_C)
if mibBuilder.loadTexts:cvqsTotalAcceptedRCCs.setStatus(_B)
if mibBuilder.loadTexts:cvqsTotalAcceptedRCCs.setUnits(_D)
_CvqsTotalRefusedRCCs_Type=Counter64
_CvqsTotalRefusedRCCs_Object=MibScalar
cvqsTotalRefusedRCCs=_CvqsTotalRefusedRCCs_Object((1,3,6,1,4,1,9,9,942,1,4,3),_CvqsTotalRefusedRCCs_Type())
cvqsTotalRefusedRCCs.setMaxAccess(_C)
if mibBuilder.loadTexts:cvqsTotalRefusedRCCs.setStatus(_B)
if mibBuilder.loadTexts:cvqsTotalRefusedRCCs.setUnits(_D)
_CvqsCapacity_ObjectIdentity=ObjectIdentity
cvqsCapacity=_CvqsCapacity_ObjectIdentity((1,3,6,1,4,1,9,9,942,1,5))
_CvqsTotalRTCPReceivers_Type=Gauge32
_CvqsTotalRTCPReceivers_Object=MibScalar
cvqsTotalRTCPReceivers=_CvqsTotalRTCPReceivers_Object((1,3,6,1,4,1,9,9,942,1,5,1),_CvqsTotalRTCPReceivers_Type())
cvqsTotalRTCPReceivers.setMaxAccess(_C)
if mibBuilder.loadTexts:cvqsTotalRTCPReceivers.setStatus(_B)
if mibBuilder.loadTexts:cvqsTotalRTCPReceivers.setUnits('RTCP receivers')
_CvqsRejectedRTCPs_Type=Counter64
_CvqsRejectedRTCPs_Object=MibScalar
cvqsRejectedRTCPs=_CvqsRejectedRTCPs_Object((1,3,6,1,4,1,9,9,942,1,5,2),_CvqsRejectedRTCPs_Type())
cvqsRejectedRTCPs.setMaxAccess(_C)
if mibBuilder.loadTexts:cvqsRejectedRTCPs.setStatus(_B)
if mibBuilder.loadTexts:cvqsRejectedRTCPs.setUnits('RTCP packets')
_CvqsRejectedERs_Type=Counter64
_CvqsRejectedERs_Object=MibScalar
cvqsRejectedERs=_CvqsRejectedERs_Object((1,3,6,1,4,1,9,9,942,1,5,3),_CvqsRejectedERs_Type())
cvqsRejectedERs.setMaxAccess(_C)
if mibBuilder.loadTexts:cvqsRejectedERs.setStatus(_B)
if mibBuilder.loadTexts:cvqsRejectedERs.setUnits(_H)
_CvqsRejectedRCCs_Type=Counter64
_CvqsRejectedRCCs_Object=MibScalar
cvqsRejectedRCCs=_CvqsRejectedRCCs_Object((1,3,6,1,4,1,9,9,942,1,5,4),_CvqsRejectedRCCs_Type())
cvqsRejectedRCCs.setMaxAccess(_C)
if mibBuilder.loadTexts:cvqsRejectedRCCs.setStatus(_B)
if mibBuilder.loadTexts:cvqsRejectedRCCs.setUnits(_D)
_CiscoVqeSMIBConform_ObjectIdentity=ObjectIdentity
ciscoVqeSMIBConform=_CiscoVqeSMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,942,2))
_CvqsMIBCompliances_ObjectIdentity=ObjectIdentity
cvqsMIBCompliances=_CvqsMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,942,2,1))
_CvqsMIBGroups_ObjectIdentity=ObjectIdentity
cvqsMIBGroups=_CvqsMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,942,2,2))
ciscoVqeSControlGroup=ObjectGroup((1,3,6,1,4,1,9,9,942,2,2,1))
ciscoVqeSControlGroup.setObjects((_A,_N))
if mibBuilder.loadTexts:ciscoVqeSControlGroup.setStatus(_B)
ciscoVqeSChannelGroup=ObjectGroup((1,3,6,1,4,1,9,9,942,2,2,2))
ciscoVqeSChannelGroup.setObjects(*((_A,_O),(_A,_P),(_A,_Q),(_A,_E),(_A,_F),(_A,_G),(_A,_R),(_A,_S)))
if mibBuilder.loadTexts:ciscoVqeSChannelGroup.setStatus(_B)
ciscoVqeSERGroup=ObjectGroup((1,3,6,1,4,1,9,9,942,2,2,3))
ciscoVqeSERGroup.setObjects(*((_A,_T),(_A,_U),(_A,_V),(_A,_W)))
if mibBuilder.loadTexts:ciscoVqeSERGroup.setStatus(_B)
ciscoVqeSRCCGroup=ObjectGroup((1,3,6,1,4,1,9,9,942,2,2,4))
ciscoVqeSRCCGroup.setObjects(*((_A,_X),(_A,_Y),(_A,_Z)))
if mibBuilder.loadTexts:ciscoVqeSRCCGroup.setStatus(_B)
ciscoVqeSCapacityGroup=ObjectGroup((1,3,6,1,4,1,9,9,942,2,2,5))
ciscoVqeSCapacityGroup.setObjects(*((_A,_a),(_A,_b),(_A,_c),(_A,_d)))
if mibBuilder.loadTexts:ciscoVqeSCapacityGroup.setStatus(_B)
cvqsChannelUp=NotificationType((1,3,6,1,4,1,9,9,942,0,1))
cvqsChannelUp.setObjects(*((_A,_E),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:cvqsChannelUp.setStatus(_B)
cvqsChannelDown=NotificationType((1,3,6,1,4,1,9,9,942,0,2))
cvqsChannelDown.setObjects(*((_A,_E),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:cvqsChannelDown.setStatus(_B)
ciscoVqeSNotifGroup=NotificationGroup((1,3,6,1,4,1,9,9,942,2,2,6))
ciscoVqeSNotifGroup.setObjects(*((_A,_e),(_A,_f)))
if mibBuilder.loadTexts:ciscoVqeSNotifGroup.setStatus(_B)
cvqsMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,942,2,1,1))
cvqsMIBCompliance.setObjects(*((_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l)))
if mibBuilder.loadTexts:cvqsMIBCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ciscoVqeSMIB':ciscoVqeSMIB,'ciscoVqeSMIBNotifs':ciscoVqeSMIBNotifs,_e:cvqsChannelUp,_f:cvqsChannelDown,'ciscoVqeSMIBObjects':ciscoVqeSMIBObjects,'cvqsControlInfo':cvqsControlInfo,_N:cvqsNotificationsEnable,'cvqsChannelInfo':cvqsChannelInfo,_O:cvqsNumberofChannels,_P:cvqsActiveChannels,_Q:cvqsLastUpdatedTime,'cvqsChannelTable':cvqsChannelTable,'cvqsChannelTableEntry':cvqsChannelTableEntry,_L:cvqsChannelIndex,_E:cvqsChannelMulticastIPType,_F:cvqsChannelMulticastIPAddr,_G:cvqsChannelMulticastPort,_R:cvqsChannelStatus,_S:cvqsChannelMemberPopulation,'cvqsErrorRepair':cvqsErrorRepair,_T:cvqsTotalReceivedERMsgs,_U:cvqsTotalReceivedInvalidERMsgs,_V:cvqsTotalReceivedERPkts,_W:cvqsTotalSentERPkts,'cvqsRCC':cvqsRCC,_X:cvqsTotalReceivedRCCs,_Y:cvqsTotalAcceptedRCCs,_Z:cvqsTotalRefusedRCCs,'cvqsCapacity':cvqsCapacity,_a:cvqsTotalRTCPReceivers,_b:cvqsRejectedRTCPs,_c:cvqsRejectedERs,_d:cvqsRejectedRCCs,'ciscoVqeSMIBConform':ciscoVqeSMIBConform,'cvqsMIBCompliances':cvqsMIBCompliances,'cvqsMIBCompliance':cvqsMIBCompliance,'cvqsMIBGroups':cvqsMIBGroups,_g:ciscoVqeSControlGroup,_h:ciscoVqeSChannelGroup,_i:ciscoVqeSERGroup,_j:ciscoVqeSRCCGroup,_k:ciscoVqeSCapacityGroup,_l:ciscoVqeSNotifGroup})