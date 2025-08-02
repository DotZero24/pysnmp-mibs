_j='fcPingNotifyGroup'
_i='fcPingStatsGroup'
_h='fcPingConfigGroup'
_g='fcPingCompletionNotify'
_f='fcPingNumTimeouts'
_e='fcPingMaxRtt'
_d='fcPingAvgRtt'
_c='fcPingMinRtt'
_b='fcPingRowStatus'
_a='fcPingTrapOnCompletion'
_Z='fcPingOperStatus'
_Y='fcPingAdminStatus'
_X='fcPingUsrPriority'
_W='fcPingAgeInterval'
_V='fcPingDelay'
_U='fcPingPacketTimeout'
_T='fcPingPayloadSize'
_S='fcPingPacketCount'
_R='fcPingAddressType'
_Q='fcPingVsanIndex'
_P='FcStartOper'
_O='milliseconds'
_N='TruthValue'
_M='VsanIndex'
_L='FcAddressType'
_K='fcPingRxPackets'
_J='fcPingTxPackets'
_I='fcPingAddress'
_H='microseconds'
_G='fcPingIndex'
_F='Unsigned32'
_E='read-only'
_D='Integer32'
_C='read-create'
_B='CISCO-FCPING-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
FcAddress,FcAddressType,VsanIndex=mibBuilder.importSymbols('CISCO-ST-TC','FcAddress',_L,_M)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_N)
ciscoFcPingMIB=ModuleIdentity((1,3,6,1,4,1,9,9,295))
if mibBuilder.loadTexts:ciscoFcPingMIB.setRevisions(('2002-10-07 00:00',))
class FcStartOper(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_CiscoFcPingMIBObjects_ObjectIdentity=ObjectIdentity
ciscoFcPingMIBObjects=_CiscoFcPingMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,295,1))
_FcPingConfiguration_ObjectIdentity=ObjectIdentity
fcPingConfiguration=_FcPingConfiguration_ObjectIdentity((1,3,6,1,4,1,9,9,295,1,1))
_FcPingTable_Object=MibTable
fcPingTable=_FcPingTable_Object((1,3,6,1,4,1,9,9,295,1,1,1))
if mibBuilder.loadTexts:fcPingTable.setStatus(_A)
_FcPingEntry_Object=MibTableRow
fcPingEntry=_FcPingEntry_Object((1,3,6,1,4,1,9,9,295,1,1,1,1))
fcPingEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:fcPingEntry.setStatus(_A)
class _FcPingIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_FcPingIndex_Type.__name__=_D
_FcPingIndex_Object=MibTableColumn
fcPingIndex=_FcPingIndex_Object((1,3,6,1,4,1,9,9,295,1,1,1,1,1),_FcPingIndex_Type())
fcPingIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:fcPingIndex.setStatus(_A)
class _FcPingVsanIndex_Type(VsanIndex):defaultValue=1
_FcPingVsanIndex_Type.__name__=_M
_FcPingVsanIndex_Object=MibTableColumn
fcPingVsanIndex=_FcPingVsanIndex_Object((1,3,6,1,4,1,9,9,295,1,1,1,1,2),_FcPingVsanIndex_Type())
fcPingVsanIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fcPingVsanIndex.setStatus(_A)
class _FcPingAddressType_Type(FcAddressType):defaultValue=1
_FcPingAddressType_Type.__name__=_L
_FcPingAddressType_Object=MibTableColumn
fcPingAddressType=_FcPingAddressType_Object((1,3,6,1,4,1,9,9,295,1,1,1,1,3),_FcPingAddressType_Type())
fcPingAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:fcPingAddressType.setStatus(_A)
_FcPingAddress_Type=FcAddress
_FcPingAddress_Object=MibTableColumn
fcPingAddress=_FcPingAddress_Object((1,3,6,1,4,1,9,9,295,1,1,1,1,4),_FcPingAddress_Type())
fcPingAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:fcPingAddress.setStatus(_A)
class _FcPingPacketCount_Type(Unsigned32):defaultValue=5;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_FcPingPacketCount_Type.__name__=_F
_FcPingPacketCount_Object=MibTableColumn
fcPingPacketCount=_FcPingPacketCount_Object((1,3,6,1,4,1,9,9,295,1,1,1,1,5),_FcPingPacketCount_Type())
fcPingPacketCount.setMaxAccess(_C)
if mibBuilder.loadTexts:fcPingPacketCount.setStatus(_A)
class _FcPingPayloadSize_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1884))
_FcPingPayloadSize_Type.__name__=_F
_FcPingPayloadSize_Object=MibTableColumn
fcPingPayloadSize=_FcPingPayloadSize_Object((1,3,6,1,4,1,9,9,295,1,1,1,1,6),_FcPingPayloadSize_Type())
fcPingPayloadSize.setMaxAccess(_C)
if mibBuilder.loadTexts:fcPingPayloadSize.setStatus(_A)
class _FcPingPacketTimeout_Type(Unsigned32):defaultValue=2;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_FcPingPacketTimeout_Type.__name__=_F
_FcPingPacketTimeout_Object=MibTableColumn
fcPingPacketTimeout=_FcPingPacketTimeout_Object((1,3,6,1,4,1,9,9,295,1,1,1,1,7),_FcPingPacketTimeout_Type())
fcPingPacketTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:fcPingPacketTimeout.setStatus(_A)
if mibBuilder.loadTexts:fcPingPacketTimeout.setUnits('seconds')
class _FcPingDelay_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600000))
_FcPingDelay_Type.__name__=_F
_FcPingDelay_Object=MibTableColumn
fcPingDelay=_FcPingDelay_Object((1,3,6,1,4,1,9,9,295,1,1,1,1,8),_FcPingDelay_Type())
fcPingDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:fcPingDelay.setStatus(_A)
if mibBuilder.loadTexts:fcPingDelay.setUnits(_O)
class _FcPingAgeInterval_Type(Unsigned32):defaultValue=500000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(500000,900000))
_FcPingAgeInterval_Type.__name__=_F
_FcPingAgeInterval_Object=MibTableColumn
fcPingAgeInterval=_FcPingAgeInterval_Object((1,3,6,1,4,1,9,9,295,1,1,1,1,9),_FcPingAgeInterval_Type())
fcPingAgeInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:fcPingAgeInterval.setStatus(_A)
if mibBuilder.loadTexts:fcPingAgeInterval.setUnits(_O)
class _FcPingUsrPriority_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('high',1),('low',2)))
_FcPingUsrPriority_Type.__name__=_D
_FcPingUsrPriority_Object=MibTableColumn
fcPingUsrPriority=_FcPingUsrPriority_Object((1,3,6,1,4,1,9,9,295,1,1,1,1,10),_FcPingUsrPriority_Type())
fcPingUsrPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:fcPingUsrPriority.setStatus(_A)
class _FcPingAdminStatus_Type(FcStartOper):defaultValue=2
_FcPingAdminStatus_Type.__name__=_P
_FcPingAdminStatus_Object=MibTableColumn
fcPingAdminStatus=_FcPingAdminStatus_Object((1,3,6,1,4,1,9,9,295,1,1,1,1,11),_FcPingAdminStatus_Type())
fcPingAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fcPingAdminStatus.setStatus(_A)
class _FcPingOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('inProgress',1),('complete',2),('disabled',3),('failure',4)))
_FcPingOperStatus_Type.__name__=_D
_FcPingOperStatus_Object=MibTableColumn
fcPingOperStatus=_FcPingOperStatus_Object((1,3,6,1,4,1,9,9,295,1,1,1,1,12),_FcPingOperStatus_Type())
fcPingOperStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:fcPingOperStatus.setStatus(_A)
class _FcPingTrapOnCompletion_Type(TruthValue):defaultValue=2
_FcPingTrapOnCompletion_Type.__name__=_N
_FcPingTrapOnCompletion_Object=MibTableColumn
fcPingTrapOnCompletion=_FcPingTrapOnCompletion_Object((1,3,6,1,4,1,9,9,295,1,1,1,1,13),_FcPingTrapOnCompletion_Type())
fcPingTrapOnCompletion.setMaxAccess(_C)
if mibBuilder.loadTexts:fcPingTrapOnCompletion.setStatus(_A)
_FcPingRowStatus_Type=RowStatus
_FcPingRowStatus_Object=MibTableColumn
fcPingRowStatus=_FcPingRowStatus_Object((1,3,6,1,4,1,9,9,295,1,1,1,1,14),_FcPingRowStatus_Type())
fcPingRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fcPingRowStatus.setStatus(_A)
_FcPingStats_ObjectIdentity=ObjectIdentity
fcPingStats=_FcPingStats_ObjectIdentity((1,3,6,1,4,1,9,9,295,1,2))
_FcPingStatsTable_Object=MibTable
fcPingStatsTable=_FcPingStatsTable_Object((1,3,6,1,4,1,9,9,295,1,2,1))
if mibBuilder.loadTexts:fcPingStatsTable.setStatus(_A)
_FcPingStatsEntry_Object=MibTableRow
fcPingStatsEntry=_FcPingStatsEntry_Object((1,3,6,1,4,1,9,9,295,1,2,1,1))
fcPingStatsEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:fcPingStatsEntry.setStatus(_A)
_FcPingTxPackets_Type=Gauge32
_FcPingTxPackets_Object=MibTableColumn
fcPingTxPackets=_FcPingTxPackets_Object((1,3,6,1,4,1,9,9,295,1,2,1,1,1),_FcPingTxPackets_Type())
fcPingTxPackets.setMaxAccess(_E)
if mibBuilder.loadTexts:fcPingTxPackets.setStatus(_A)
_FcPingRxPackets_Type=Gauge32
_FcPingRxPackets_Object=MibTableColumn
fcPingRxPackets=_FcPingRxPackets_Object((1,3,6,1,4,1,9,9,295,1,2,1,1,2),_FcPingRxPackets_Type())
fcPingRxPackets.setMaxAccess(_E)
if mibBuilder.loadTexts:fcPingRxPackets.setStatus(_A)
class _FcPingMinRtt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000000))
_FcPingMinRtt_Type.__name__=_D
_FcPingMinRtt_Object=MibTableColumn
fcPingMinRtt=_FcPingMinRtt_Object((1,3,6,1,4,1,9,9,295,1,2,1,1,3),_FcPingMinRtt_Type())
fcPingMinRtt.setMaxAccess(_E)
if mibBuilder.loadTexts:fcPingMinRtt.setStatus(_A)
if mibBuilder.loadTexts:fcPingMinRtt.setUnits(_H)
class _FcPingAvgRtt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000000))
_FcPingAvgRtt_Type.__name__=_D
_FcPingAvgRtt_Object=MibTableColumn
fcPingAvgRtt=_FcPingAvgRtt_Object((1,3,6,1,4,1,9,9,295,1,2,1,1,4),_FcPingAvgRtt_Type())
fcPingAvgRtt.setMaxAccess(_E)
if mibBuilder.loadTexts:fcPingAvgRtt.setStatus(_A)
if mibBuilder.loadTexts:fcPingAvgRtt.setUnits(_H)
class _FcPingMaxRtt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000000))
_FcPingMaxRtt_Type.__name__=_D
_FcPingMaxRtt_Object=MibTableColumn
fcPingMaxRtt=_FcPingMaxRtt_Object((1,3,6,1,4,1,9,9,295,1,2,1,1,5),_FcPingMaxRtt_Type())
fcPingMaxRtt.setMaxAccess(_E)
if mibBuilder.loadTexts:fcPingMaxRtt.setStatus(_A)
if mibBuilder.loadTexts:fcPingMaxRtt.setUnits(_H)
_FcPingNumTimeouts_Type=Gauge32
_FcPingNumTimeouts_Object=MibTableColumn
fcPingNumTimeouts=_FcPingNumTimeouts_Object((1,3,6,1,4,1,9,9,295,1,2,1,1,6),_FcPingNumTimeouts_Type())
fcPingNumTimeouts.setMaxAccess(_E)
if mibBuilder.loadTexts:fcPingNumTimeouts.setStatus(_A)
_FcPingNotification_ObjectIdentity=ObjectIdentity
fcPingNotification=_FcPingNotification_ObjectIdentity((1,3,6,1,4,1,9,9,295,1,3))
_FcPingNotifications_ObjectIdentity=ObjectIdentity
fcPingNotifications=_FcPingNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,295,1,3,0))
_FcPingMIBConformance_ObjectIdentity=ObjectIdentity
fcPingMIBConformance=_FcPingMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,295,2))
_FcPingMIBCompliances_ObjectIdentity=ObjectIdentity
fcPingMIBCompliances=_FcPingMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,295,2,1))
_FcPingMIBGroups_ObjectIdentity=ObjectIdentity
fcPingMIBGroups=_FcPingMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,295,2,2))
fcPingConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,295,2,2,1))
fcPingConfigGroup.setObjects(*((_B,_Q),(_B,_R),(_B,_I),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b)))
if mibBuilder.loadTexts:fcPingConfigGroup.setStatus(_A)
fcPingStatsGroup=ObjectGroup((1,3,6,1,4,1,9,9,295,2,2,2))
fcPingStatsGroup.setObjects(*((_B,_J),(_B,_K),(_B,_c),(_B,_d),(_B,_e),(_B,_f)))
if mibBuilder.loadTexts:fcPingStatsGroup.setStatus(_A)
fcPingCompletionNotify=NotificationType((1,3,6,1,4,1,9,9,295,1,3,0,1))
fcPingCompletionNotify.setObjects(*((_B,_I),(_B,_J),(_B,_K)))
if mibBuilder.loadTexts:fcPingCompletionNotify.setStatus(_A)
fcPingNotifyGroup=NotificationGroup((1,3,6,1,4,1,9,9,295,2,2,3))
fcPingNotifyGroup.setObjects((_B,_g))
if mibBuilder.loadTexts:fcPingNotifyGroup.setStatus(_A)
fcPingMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,295,2,1,1))
fcPingMIBCompliance.setObjects(*((_B,_h),(_B,_i),(_B,_j)))
if mibBuilder.loadTexts:fcPingMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_P:FcStartOper,'ciscoFcPingMIB':ciscoFcPingMIB,'ciscoFcPingMIBObjects':ciscoFcPingMIBObjects,'fcPingConfiguration':fcPingConfiguration,'fcPingTable':fcPingTable,'fcPingEntry':fcPingEntry,_G:fcPingIndex,_Q:fcPingVsanIndex,_R:fcPingAddressType,_I:fcPingAddress,_S:fcPingPacketCount,_T:fcPingPayloadSize,_U:fcPingPacketTimeout,_V:fcPingDelay,_W:fcPingAgeInterval,_X:fcPingUsrPriority,_Y:fcPingAdminStatus,_Z:fcPingOperStatus,_a:fcPingTrapOnCompletion,_b:fcPingRowStatus,'fcPingStats':fcPingStats,'fcPingStatsTable':fcPingStatsTable,'fcPingStatsEntry':fcPingStatsEntry,_J:fcPingTxPackets,_K:fcPingRxPackets,_c:fcPingMinRtt,_d:fcPingAvgRtt,_e:fcPingMaxRtt,_f:fcPingNumTimeouts,'fcPingNotification':fcPingNotification,'fcPingNotifications':fcPingNotifications,_g:fcPingCompletionNotify,'fcPingMIBConformance':fcPingMIBConformance,'fcPingMIBCompliances':fcPingMIBCompliances,'fcPingMIBCompliance':fcPingMIBCompliance,'fcPingMIBGroups':fcPingMIBGroups,_h:fcPingConfigGroup,_i:fcPingStatsGroup,_j:fcPingNotifyGroup})