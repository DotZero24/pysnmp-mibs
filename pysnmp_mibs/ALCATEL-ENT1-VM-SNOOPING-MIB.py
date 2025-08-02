_Ae='alaVMSnoopingStaticPolicyGroup'
_Ad='alaVMSnoopingLearntVMGroup'
_Ac='alaVMSnoopingTrapsObjGroup'
_Ab='alaVMSnoopingNotificationGroup'
_Aa='alaVMSnoopingFilterResourceGroup'
_AZ='alaVMSnoopingHardwareStatsGroup'
_AY='alaVMSnoopingDBGroup'
_AX='alaVMSnoopingPortGroup'
_AW='alaVMSnoopingUdpPortGroup'
_AV='alaVMSnoopingConfigGroup'
_AU='alaVMSnoopingReservedHwResourceLimitAlert'
_AT='alaVMSnoopingVMRemovedAlert'
_AS='alaVMSnoopingVMLearntAlert'
_AR='alaVMSnoopingStaticPolicyRowStatus'
_AQ='alaVMSnoopingLearntVMVlanId'
_AP='alaVMSnoopingFilterResourceUsed'
_AO='alaVMSnoopingFilterResourceMax'
_AN='alaVMSnoopingHardwareStatsNumOfBytes'
_AM='alaVMSnoopingHardwareStatsNumOfPackets'
_AL='alaVMSnoopingHardwareStatsPolicyrule'
_AK='alaVMSnoopingHardwareStatsPolicylist'
_AJ='alaVMSnoopingDBSamplingStatsPackets'
_AI='alaVMSnoopingDBPolicyList'
_AH='alaVMSnoopingDBPolicyRule'
_AG='alaVMSnoopingDBVInnerIPProtocol'
_AF='alaVMSnoopingDBVInnerL4DestPort'
_AE='alaVMSnoopingDBVInnerL4SrcPort'
_AD='alaVMSnoopingDBInnerDestIpAddr'
_AC='alaVMSnoopingDBInnerDestIpAddrType'
_AB='alaVMSnoopingDBInnerSrcIpAddr'
_AA='alaVMSnoopingDBInnerSrcIpAddrType'
_A9='alaVMSnoopingDBInnerVlan'
_A8='alaVMSnoopingDBInnerDestMacAddr'
_A7='alaVMSnoopingDBInnerSrcMacAddr'
_A6='alaVMSnoopingDBVtepDestIpAddr'
_A5='alaVMSnoopingDBVtepDestIpAddrType'
_A4='alaVMSnoopingDBVtepSrcIpAddr'
_A3='alaVMSnoopingDBVtepSrcIpAddrType'
_A2='alaVMSnoopingDBVtepVlan'
_A1='alaVMSnoopingDBVni'
_A0='alaVMSnoopingDBVxlanUdpDestPort'
_z='alaVMSnoopingDBIfIndex'
_y='alaVMSnoopingPortSamplingClearStats'
_x='alaVMSnoopingPortDBClear'
_w='alaVMSnoopingPortRowStatus'
_v='alaVMSnoopingPortIsVNP'
_u='alaVMSnoopingPortAdminStatus'
_t='alaVMSnoopingUdpRowStatus'
_s='alaVMSnoopingQosAllocationStatus'
_r='alaVMSnoopingLoggingThresholdFlows'
_q='alaVMSnoopingClearAllData'
_p='alaVMSnoopingFilteringResourceTrapThreshold'
_o='alaVMSnoopingAgingTimer'
_n='alaVMSnoopingSamplingRate'
_m='alaVMSnoopingTrapStatus'
_l='alaVMSnoopingVMTrafficTagged'
_k='alaVMSnoopingPolicyResource'
_j='alaVMSnoopingPolicyMode'
_i='alaVMSnoopingAdminStatus'
_h='alaVMSnoopingStaticPolicyListName'
_g='alaVMSnoopingStaticPolicyRuleName'
_f='alaVMSnoopingLearntVMSrcMac'
_e='alaVMSnoopingLearntVMIfIndex'
_d='alaVMSnoopingFilterResourceSlotNum'
_c='alaVMSnoopingFilterResourceChassisId'
_b='alaVMSnoopingHardwareStatsIndex'
_a='alaVMSnoopingDBFlowId'
_Z='alaVMSnoopingPortIndex'
_Y='alaVMSnoopingUdpPortIndex'
_X='Unsigned32'
_W='alaVMSnoopingHwResourceUsed'
_V='alaVMSnoopingHwResourceTotal'
_U='alaVMSnoopingNiSlot'
_T='alaVMSnoopingChassisId'
_S='alaVMSnoopingLearnedVxlanVni'
_R='alaVMSnoopingLearnedVxlanUdpPort'
_Q='yes'
_P='disable'
_O='enable'
_N='alaVMSnoopingLearnedMacAddress'
_M='ipv6'
_L='ipv4'
_K='InetAddressType'
_J='InetAddress'
_I='read-create'
_H='accessible-for-notify'
_G='SnmpAdminString'
_F='not-accessible'
_E='read-write'
_D='Integer32'
_C='read-only'
_B='ALCATEL-ENT1-VM-SNOOPING-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
softentIND1VMSnooping,=mibBuilder.importSymbols('ALCATEL-ENT1-BASE','softentIND1VMSnooping')
physicalIndex,=mibBuilder.importSymbols('ALCATEL-ENT1-CHASSIS-MIB','physicalIndex')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_J,_K)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_G)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_X,'iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention')
alaVMSnoopingMIB=ModuleIdentity((1,3,6,1,4,1,6486,801,1,2,1,84,1))
if mibBuilder.loadTexts:alaVMSnoopingMIB.setRevisions(('2014-07-01 00:00',))
_AlaVMSnoopingMIBNotifications_ObjectIdentity=ObjectIdentity
alaVMSnoopingMIBNotifications=_AlaVMSnoopingMIBNotifications_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,84,1,0))
_AlaVMSnoopingMIBObjects_ObjectIdentity=ObjectIdentity
alaVMSnoopingMIBObjects=_AlaVMSnoopingMIBObjects_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,84,1,1))
if mibBuilder.loadTexts:alaVMSnoopingMIBObjects.setStatus(_A)
_AlaVMSnoopingTrapsObj_ObjectIdentity=ObjectIdentity
alaVMSnoopingTrapsObj=_AlaVMSnoopingTrapsObj_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,84,1,1,1))
_AlaVMSnoopingLearnedMacAddress_Type=MacAddress
_AlaVMSnoopingLearnedMacAddress_Object=MibScalar
alaVMSnoopingLearnedMacAddress=_AlaVMSnoopingLearnedMacAddress_Object((1,3,6,1,4,1,6486,801,1,2,1,84,1,1,1,1),_AlaVMSnoopingLearnedMacAddress_Type())
alaVMSnoopingLearnedMacAddress.setMaxAccess(_H)
if mibBuilder.loadTexts:alaVMSnoopingLearnedMacAddress.setStatus(_A)
_AlaVMSnoopingLearnedVxlanUdpPort_Type=Integer32
_AlaVMSnoopingLearnedVxlanUdpPort_Object=MibScalar
alaVMSnoopingLearnedVxlanUdpPort=_AlaVMSnoopingLearnedVxlanUdpPort_Object((1,3,6,1,4,1,6486,801,1,2,1,84,1,1,1,2),_AlaVMSnoopingLearnedVxlanUdpPort_Type())
alaVMSnoopingLearnedVxlanUdpPort.setMaxAccess(_H)
if mibBuilder.loadTexts:alaVMSnoopingLearnedVxlanUdpPort.setStatus(_A)
_AlaVMSnoopingLearnedVxlanVni_Type=Integer32
_AlaVMSnoopingLearnedVxlanVni_Object=MibScalar
alaVMSnoopingLearnedVxlanVni=_AlaVMSnoopingLearnedVxlanVni_Object((1,3,6,1,4,1,6486,801,1,2,1,84,1,1,1,3),_AlaVMSnoopingLearnedVxlanVni_Type())
alaVMSnoopingLearnedVxlanVni.setMaxAccess(_H)
if mibBuilder.loadTexts:alaVMSnoopingLearnedVxlanVni.setStatus(_A)
_AlaVMSnoopingNiSlot_Type=Integer32
_AlaVMSnoopingNiSlot_Object=MibScalar
alaVMSnoopingNiSlot=_AlaVMSnoopingNiSlot_Object((1,3,6,1,4,1,6486,801,1,2,1,84,1,1,1,4),_AlaVMSnoopingNiSlot_Type())
alaVMSnoopingNiSlot.setMaxAccess(_H)
if mibBuilder.loadTexts:alaVMSnoopingNiSlot.setStatus(_A)
_AlaVMSnoopingHwResourceTotal_Type=Integer32
_AlaVMSnoopingHwResourceTotal_Object=MibScalar
alaVMSnoopingHwResourceTotal=_AlaVMSnoopingHwResourceTotal_Object((1,3,6,1,4,1,6486,801,1,2,1,84,1,1,1,5),_AlaVMSnoopingHwResourceTotal_Type())
alaVMSnoopingHwResourceTotal.setMaxAccess(_H)
if mibBuilder.loadTexts:alaVMSnoopingHwResourceTotal.setStatus(_A)
_AlaVMSnoopingHwResourceUsed_Type=Integer32
_AlaVMSnoopingHwResourceUsed_Object=MibScalar
alaVMSnoopingHwResourceUsed=_AlaVMSnoopingHwResourceUsed_Object((1,3,6,1,4,1,6486,801,1,2,1,84,1,1,1,6),_AlaVMSnoopingHwResourceUsed_Type())
alaVMSnoopingHwResourceUsed.setMaxAccess(_H)
if mibBuilder.loadTexts:alaVMSnoopingHwResourceUsed.setStatus(_A)
_AlaVMSnoopingChassisId_Type=Integer32
_AlaVMSnoopingChassisId_Object=MibScalar
alaVMSnoopingChassisId=_AlaVMSnoopingChassisId_Object((1,3,6,1,4,1,6486,801,1,2,1,84,1,1,1,7),_AlaVMSnoopingChassisId_Type())
alaVMSnoopingChassisId.setMaxAccess(_H)
if mibBuilder.loadTexts:alaVMSnoopingChassisId.setStatus(_A)
_AlaVMSnoopingConfig_ObjectIdentity=ObjectIdentity
alaVMSnoopingConfig=_AlaVMSnoopingConfig_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,84,1,1,2))
class _AlaVMSnoopingAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_O,1),(_P,2)))
_AlaVMSnoopingAdminStatus_Type.__name__=_D
_AlaVMSnoopingAdminStatus_Object=MibScalar
alaVMSnoopingAdminStatus=_AlaVMSnoopingAdminStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,84,1,1,2,1),_AlaVMSnoopingAdminStatus_Type())
alaVMSnoopingAdminStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:alaVMSnoopingAdminStatus.setStatus(_A)
class _AlaVMSnoopingPolicyMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('basic',1),('advance',2)))
_AlaVMSnoopingPolicyMode_Type.__name__=_D
_AlaVMSnoopingPolicyMode_Object=MibScalar
alaVMSnoopingPolicyMode=_AlaVMSnoopingPolicyMode_Object((1,3,6,1,4,1,6486,801,1,2,1,84,1,1,2,2),_AlaVMSnoopingPolicyMode_Type())
alaVMSnoopingPolicyMode.setMaxAccess(_E)
if mibBuilder.loadTexts:alaVMSnoopingPolicyMode.setStatus(_A)
class _AlaVMSnoopingPolicyResource_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('default',1),('extended',2)))
_AlaVMSnoopingPolicyResource_Type.__name__=_D
_AlaVMSnoopingPolicyResource_Object=MibScalar
alaVMSnoopingPolicyResource=_AlaVMSnoopingPolicyResource_Object((1,3,6,1,4,1,6486,801,1,2,1,84,1,1,2,3),_AlaVMSnoopingPolicyResource_Type())
alaVMSnoopingPolicyResource.setMaxAccess(_E)
if mibBuilder.loadTexts:alaVMSnoopingPolicyResource.setStatus(_A)
class _AlaVMSnoopingVMTrafficTagged_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('tagged',1),('untagged',2),('both',3)))
_AlaVMSnoopingVMTrafficTagged_Type.__name__=_D
_AlaVMSnoopingVMTrafficTagged_Object=MibScalar
alaVMSnoopingVMTrafficTagged=_AlaVMSnoopingVMTrafficTagged_Object((1,3,6,1,4,1,6486,801,1,2,1,84,1,1,2,4),_AlaVMSnoopingVMTrafficTagged_Type())
alaVMSnoopingVMTrafficTagged.setMaxAccess(_E)
if mibBuilder.loadTexts:alaVMSnoopingVMTrafficTagged.setStatus(_A)
class _AlaVMSnoopingTrapStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_O,1),(_P,2)))
_AlaVMSnoopingTrapStatus_Type.__name__=_D
_AlaVMSnoopingTrapStatus_Object=MibScalar
alaVMSnoopingTrapStatus=_AlaVMSnoopingTrapStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,84,1,1,2,5),_AlaVMSnoopingTrapStatus_Type())
alaVMSnoopingTrapStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:alaVMSnoopingTrapStatus.setStatus(_A)
class _AlaVMSnoopingSamplingRate_Type(Unsigned32):defaultValue=1000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967296))
_AlaVMSnoopingSamplingRate_Type.__name__=_X
_AlaVMSnoopingSamplingRate_Object=MibScalar
alaVMSnoopingSamplingRate=_AlaVMSnoopingSamplingRate_Object((1,3,6,1,4,1,6486,801,1,2,1,84,1,1,2,6),_AlaVMSnoopingSamplingRate_Type())
alaVMSnoopingSamplingRate.setMaxAccess(_E)
if mibBuilder.loadTexts:alaVMSnoopingSamplingRate.setStatus(_A)
class _AlaVMSnoopingAgingTimer_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,86400))
_AlaVMSnoopingAgingTimer_Type.__name__=_D
_AlaVMSnoopingAgingTimer_Object=MibScalar
alaVMSnoopingAgingTimer=_AlaVMSnoopingAgingTimer_Object((1,3,6,1,4,1,6486,801,1,2,1,84,1,1,2,7),_AlaVMSnoopingAgingTimer_Type())
alaVMSnoopingAgingTimer.setMaxAccess(_E)
if mibBuilder.loadTexts:alaVMSnoopingAgingTimer.setStatus(_A)
class _AlaVMSnoopingFilteringResourceTrapThreshold_Type(Integer32):defaultValue=80;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_AlaVMSnoopingFilteringResourceTrapThreshold_Type.__name__=_D
_AlaVMSnoopingFilteringResourceTrapThreshold_Object=MibScalar
alaVMSnoopingFilteringResourceTrapThreshold=_AlaVMSnoopingFilteringResourceTrapThreshold_Object((1,3,6,1,4,1,6486,801,1,2,1,84,1,1,2,8),_AlaVMSnoopingFilteringResourceTrapThreshold_Type())
alaVMSnoopingFilteringResourceTrapThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:alaVMSnoopingFilteringResourceTrapThreshold.setStatus(_A)
class _AlaVMSnoopingClearAllData_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('globalStats',1),('hardwareStats',2),('database',3),('none',4)))
_AlaVMSnoopingClearAllData_Type.__name__=_D
_AlaVMSnoopingClearAllData_Object=MibScalar
alaVMSnoopingClearAllData=_AlaVMSnoopingClearAllData_Object((1,3,6,1,4,1,6486,801,1,2,1,84,1,1,2,9),_AlaVMSnoopingClearAllData_Type())
alaVMSnoopingClearAllData.setMaxAccess(_E)
if mibBuilder.loadTexts:alaVMSnoopingClearAllData.setStatus(_A)
class _AlaVMSnoopingLoggingThresholdFlows_Type(Integer32):defaultValue=5000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1000,600000))
_AlaVMSnoopingLoggingThresholdFlows_Type.__name__=_D
_AlaVMSnoopingLoggingThresholdFlows_Object=MibScalar
alaVMSnoopingLoggingThresholdFlows=_AlaVMSnoopingLoggingThresholdFlows_Object((1,3,6,1,4,1,6486,801,1,2,1,84,1,1,2,10),_AlaVMSnoopingLoggingThresholdFlows_Type())
alaVMSnoopingLoggingThresholdFlows.setMaxAccess(_E)
if mibBuilder.loadTexts:alaVMSnoopingLoggingThresholdFlows.setStatus(_A)
class _AlaVMSnoopingQosAllocationStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('none',1),('inProgress',2),('success',3),('failed',4)))
_AlaVMSnoopingQosAllocationStatus_Type.__name__=_D
_AlaVMSnoopingQosAllocationStatus_Object=MibScalar
alaVMSnoopingQosAllocationStatus=_AlaVMSnoopingQosAllocationStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,84,1,1,2,11),_AlaVMSnoopingQosAllocationStatus_Type())
alaVMSnoopingQosAllocationStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:alaVMSnoopingQosAllocationStatus.setStatus(_A)
_AlaVMSnoopingUdpPortTable_Object=MibTable
alaVMSnoopingUdpPortTable=_AlaVMSnoopingUdpPortTable_Object((1,3,6,1,4,1,6486,801,1,2,1,84,1,1,3))
if mibBuilder.loadTexts:alaVMSnoopingUdpPortTable.setStatus(_A)
_AlaVMSnoopingUdpPortEntry_Object=MibTableRow
alaVMSnoopingUdpPortEntry=_AlaVMSnoopingUdpPortEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,84,1,1,3,1))
alaVMSnoopingUdpPortEntry.setIndexNames((0,_B,_Y))
if mibBuilder.loadTexts:alaVMSnoopingUdpPortEntry.setStatus(_A)
_AlaVMSnoopingUdpPortIndex_Type=Unsigned32
_AlaVMSnoopingUdpPortIndex_Object=MibTableColumn
alaVMSnoopingUdpPortIndex=_AlaVMSnoopingUdpPortIndex_Object((1,3,6,1,4,1,6486,801,1,2,1,84,1,1,3,1,1),_AlaVMSnoopingUdpPortIndex_Type())
alaVMSnoopingUdpPortIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:alaVMSnoopingUdpPortIndex.setStatus(_A)
_AlaVMSnoopingUdpRowStatus_Type=RowStatus
_AlaVMSnoopingUdpRowStatus_Object=MibTableColumn
alaVMSnoopingUdpRowStatus=_AlaVMSnoopingUdpRowStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,84,1,1,3,1,2),_AlaVMSnoopingUdpRowStatus_Type())
alaVMSnoopingUdpRowStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:alaVMSnoopingUdpRowStatus.setStatus(_A)
_AlaVMSnoopingPortTable_Object=MibTable
alaVMSnoopingPortTable=_AlaVMSnoopingPortTable_Object((1,3,6,1,4,1,6486,801,1,2,1,84,1,1,4))
if mibBuilder.loadTexts:alaVMSnoopingPortTable.setStatus(_A)
_AlaVMSnoopingPortEntry_Object=MibTableRow
alaVMSnoopingPortEntry=_AlaVMSnoopingPortEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,84,1,1,4,1))
alaVMSnoopingPortEntry.setIndexNames((0,_B,_Z))
if mibBuilder.loadTexts:alaVMSnoopingPortEntry.setStatus(_A)
_AlaVMSnoopingPortIndex_Type=InterfaceIndex
_AlaVMSnoopingPortIndex_Object=MibTableColumn
alaVMSnoopingPortIndex=_AlaVMSnoopingPortIndex_Object((1,3,6,1,4,1,6486,801,1,2,1,84,1,1,4,1,1),_AlaVMSnoopingPortIndex_Type())
alaVMSnoopingPortIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:alaVMSnoopingPortIndex.setStatus(_A)
class _AlaVMSnoopingPortAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_O,1),(_P,2)))
_AlaVMSnoopingPortAdminStatus_Type.__name__=_D
_AlaVMSnoopingPortAdminStatus_Object=MibTableColumn
alaVMSnoopingPortAdminStatus=_AlaVMSnoopingPortAdminStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,84,1,1,4,1,2),_AlaVMSnoopingPortAdminStatus_Type())
alaVMSnoopingPortAdminStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:alaVMSnoopingPortAdminStatus.setStatus(_A)
class _AlaVMSnoopingPortIsVNP_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),('no',2)))
_AlaVMSnoopingPortIsVNP_Type.__name__=_D
_AlaVMSnoopingPortIsVNP_Object=MibTableColumn
alaVMSnoopingPortIsVNP=_AlaVMSnoopingPortIsVNP_Object((1,3,6,1,4,1,6486,801,1,2,1,84,1,1,4,1,3),_AlaVMSnoopingPortIsVNP_Type())
alaVMSnoopingPortIsVNP.setMaxAccess(_C)
if mibBuilder.loadTexts:alaVMSnoopingPortIsVNP.setStatus(_A)
_AlaVMSnoopingPortRowStatus_Type=RowStatus
_AlaVMSnoopingPortRowStatus_Object=MibTableColumn
alaVMSnoopingPortRowStatus=_AlaVMSnoopingPortRowStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,84,1,1,4,1,4),_AlaVMSnoopingPortRowStatus_Type())
alaVMSnoopingPortRowStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:alaVMSnoopingPortRowStatus.setStatus(_A)
class _AlaVMSnoopingPortDBClear_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),('no',2)))
_AlaVMSnoopingPortDBClear_Type.__name__=_D
_AlaVMSnoopingPortDBClear_Object=MibTableColumn
alaVMSnoopingPortDBClear=_AlaVMSnoopingPortDBClear_Object((1,3,6,1,4,1,6486,801,1,2,1,84,1,1,4,1,5),_AlaVMSnoopingPortDBClear_Type())
alaVMSnoopingPortDBClear.setMaxAccess(_I)
if mibBuilder.loadTexts:alaVMSnoopingPortDBClear.setStatus(_A)
class _AlaVMSnoopingPortSamplingClearStats_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),('no',2)))
_AlaVMSnoopingPortSamplingClearStats_Type.__name__=_D
_AlaVMSnoopingPortSamplingClearStats_Object=MibTableColumn
alaVMSnoopingPortSamplingClearStats=_AlaVMSnoopingPortSamplingClearStats_Object((1,3,6,1,4,1,6486,801,1,2,1,84,1,1,4,1,6),_AlaVMSnoopingPortSamplingClearStats_Type())
alaVMSnoopingPortSamplingClearStats.setMaxAccess(_I)
if mibBuilder.loadTexts:alaVMSnoopingPortSamplingClearStats.setStatus(_A)
_AlaVMSnoopingDBTable_Object=MibTable
alaVMSnoopingDBTable=_AlaVMSnoopingDBTable_Object((1,3,6,1,4,1,6486,801,1,2,1,84,1,1,5))
if mibBuilder.loadTexts:alaVMSnoopingDBTable.setStatus(_A)
_AlaVMSnoopingDBEntry_Object=MibTableRow
alaVMSnoopingDBEntry=_AlaVMSnoopingDBEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,84,1,1,5,1))
alaVMSnoopingDBEntry.setIndexNames((0,_B,_a))
if mibBuilder.loadTexts:alaVMSnoopingDBEntry.setStatus(_A)
_AlaVMSnoopingDBFlowId_Type=Unsigned32
_AlaVMSnoopingDBFlowId_Object=MibTableColumn
alaVMSnoopingDBFlowId=_AlaVMSnoopingDBFlowId_Object((1,3,6,1,4,1,6486,801,1,2,1,84,1,1,5,1,1),_AlaVMSnoopingDBFlowId_Type())
alaVMSnoopingDBFlowId.setMaxAccess(_F)
if mibBuilder.loadTexts:alaVMSnoopingDBFlowId.setStatus(_A)
_AlaVMSnoopingDBIfIndex_Type=InterfaceIndex
_AlaVMSnoopingDBIfIndex_Object=MibTableColumn
alaVMSnoopingDBIfIndex=_AlaVMSnoopingDBIfIndex_Object((1,3,6,1,4,1,6486,801,1,2,1,84,1,1,5,1,2),_AlaVMSnoopingDBIfIndex_Type())
alaVMSnoopingDBIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:alaVMSnoopingDBIfIndex.setStatus(_A)
class _AlaVMSnoopingDBVxlanUdpDestPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AlaVMSnoopingDBVxlanUdpDestPort_Type.__name__=_D
_AlaVMSnoopingDBVxlanUdpDestPort_Object=MibTableColumn
alaVMSnoopingDBVxlanUdpDestPort=_AlaVMSnoopingDBVxlanUdpDestPort_Object((1,3,6,1,4,1,6486,801,1,2,1,84,1,1,5,1,3),_AlaVMSnoopingDBVxlanUdpDestPort_Type())
alaVMSnoopingDBVxlanUdpDestPort.setMaxAccess(_C)
if mibBuilder.loadTexts:alaVMSnoopingDBVxlanUdpDestPort.setStatus(_A)
class _AlaVMSnoopingDBVni_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AlaVMSnoopingDBVni_Type.__name__=_D
_AlaVMSnoopingDBVni_Object=MibTableColumn
alaVMSnoopingDBVni=_AlaVMSnoopingDBVni_Object((1,3,6,1,4,1,6486,801,1,2,1,84,1,1,5,1,4),_AlaVMSnoopingDBVni_Type())
alaVMSnoopingDBVni.setMaxAccess(_C)
if mibBuilder.loadTexts:alaVMSnoopingDBVni.setStatus(_A)
class _AlaVMSnoopingDBVtepVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AlaVMSnoopingDBVtepVlan_Type.__name__=_D
_AlaVMSnoopingDBVtepVlan_Object=MibTableColumn
alaVMSnoopingDBVtepVlan=_AlaVMSnoopingDBVtepVlan_Object((1,3,6,1,4,1,6486,801,1,2,1,84,1,1,5,1,5),_AlaVMSnoopingDBVtepVlan_Type())
alaVMSnoopingDBVtepVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:alaVMSnoopingDBVtepVlan.setStatus(_A)
class _AlaVMSnoopingDBVtepSrcIpAddrType_Type(InetAddressType):subtypeSpec=InetAddressType.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_AlaVMSnoopingDBVtepSrcIpAddrType_Type.__name__=_K
_AlaVMSnoopingDBVtepSrcIpAddrType_Object=MibTableColumn
alaVMSnoopingDBVtepSrcIpAddrType=_AlaVMSnoopingDBVtepSrcIpAddrType_Object((1,3,6,1,4,1,6486,801,1,2,1,84,1,1,5,1,6),_AlaVMSnoopingDBVtepSrcIpAddrType_Type())
alaVMSnoopingDBVtepSrcIpAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:alaVMSnoopingDBVtepSrcIpAddrType.setStatus(_A)
class _AlaVMSnoopingDBVtepSrcIpAddr_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_AlaVMSnoopingDBVtepSrcIpAddr_Type.__name__=_J
_AlaVMSnoopingDBVtepSrcIpAddr_Object=MibTableColumn
alaVMSnoopingDBVtepSrcIpAddr=_AlaVMSnoopingDBVtepSrcIpAddr_Object((1,3,6,1,4,1,6486,801,1,2,1,84,1,1,5,1,7),_AlaVMSnoopingDBVtepSrcIpAddr_Type())
alaVMSnoopingDBVtepSrcIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:alaVMSnoopingDBVtepSrcIpAddr.setStatus(_A)
class _AlaVMSnoopingDBVtepDestIpAddrType_Type(InetAddressType):subtypeSpec=InetAddressType.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_AlaVMSnoopingDBVtepDestIpAddrType_Type.__name__=_K
_AlaVMSnoopingDBVtepDestIpAddrType_Object=MibTableColumn
alaVMSnoopingDBVtepDestIpAddrType=_AlaVMSnoopingDBVtepDestIpAddrType_Object((1,3,6,1,4,1,6486,801,1,2,1,84,1,1,5,1,8),_AlaVMSnoopingDBVtepDestIpAddrType_Type())
alaVMSnoopingDBVtepDestIpAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:alaVMSnoopingDBVtepDestIpAddrType.setStatus(_A)
class _AlaVMSnoopingDBVtepDestIpAddr_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_AlaVMSnoopingDBVtepDestIpAddr_Type.__name__=_J
_AlaVMSnoopingDBVtepDestIpAddr_Object=MibTableColumn
alaVMSnoopingDBVtepDestIpAddr=_AlaVMSnoopingDBVtepDestIpAddr_Object((1,3,6,1,4,1,6486,801,1,2,1,84,1,1,5,1,9),_AlaVMSnoopingDBVtepDestIpAddr_Type())
alaVMSnoopingDBVtepDestIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:alaVMSnoopingDBVtepDestIpAddr.setStatus(_A)
_AlaVMSnoopingDBInnerSrcMacAddr_Type=MacAddress
_AlaVMSnoopingDBInnerSrcMacAddr_Object=MibTableColumn
alaVMSnoopingDBInnerSrcMacAddr=_AlaVMSnoopingDBInnerSrcMacAddr_Object((1,3,6,1,4,1,6486,801,1,2,1,84,1,1,5,1,10),_AlaVMSnoopingDBInnerSrcMacAddr_Type())
alaVMSnoopingDBInnerSrcMacAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:alaVMSnoopingDBInnerSrcMacAddr.setStatus(_A)
_AlaVMSnoopingDBInnerDestMacAddr_Type=MacAddress
_AlaVMSnoopingDBInnerDestMacAddr_Object=MibTableColumn
alaVMSnoopingDBInnerDestMacAddr=_AlaVMSnoopingDBInnerDestMacAddr_Object((1,3,6,1,4,1,6486,801,1,2,1,84,1,1,5,1,11),_AlaVMSnoopingDBInnerDestMacAddr_Type())
alaVMSnoopingDBInnerDestMacAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:alaVMSnoopingDBInnerDestMacAddr.setStatus(_A)
class _AlaVMSnoopingDBInnerVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AlaVMSnoopingDBInnerVlan_Type.__name__=_D
_AlaVMSnoopingDBInnerVlan_Object=MibTableColumn
alaVMSnoopingDBInnerVlan=_AlaVMSnoopingDBInnerVlan_Object((1,3,6,1,4,1,6486,801,1,2,1,84,1,1,5,1,12),_AlaVMSnoopingDBInnerVlan_Type())
alaVMSnoopingDBInnerVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:alaVMSnoopingDBInnerVlan.setStatus(_A)
class _AlaVMSnoopingDBInnerSrcIpAddrType_Type(InetAddressType):subtypeSpec=InetAddressType.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_AlaVMSnoopingDBInnerSrcIpAddrType_Type.__name__=_K
_AlaVMSnoopingDBInnerSrcIpAddrType_Object=MibTableColumn
alaVMSnoopingDBInnerSrcIpAddrType=_AlaVMSnoopingDBInnerSrcIpAddrType_Object((1,3,6,1,4,1,6486,801,1,2,1,84,1,1,5,1,13),_AlaVMSnoopingDBInnerSrcIpAddrType_Type())
alaVMSnoopingDBInnerSrcIpAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:alaVMSnoopingDBInnerSrcIpAddrType.setStatus(_A)
class _AlaVMSnoopingDBInnerSrcIpAddr_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_AlaVMSnoopingDBInnerSrcIpAddr_Type.__name__=_J
_AlaVMSnoopingDBInnerSrcIpAddr_Object=MibTableColumn
alaVMSnoopingDBInnerSrcIpAddr=_AlaVMSnoopingDBInnerSrcIpAddr_Object((1,3,6,1,4,1,6486,801,1,2,1,84,1,1,5,1,14),_AlaVMSnoopingDBInnerSrcIpAddr_Type())
alaVMSnoopingDBInnerSrcIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:alaVMSnoopingDBInnerSrcIpAddr.setStatus(_A)
class _AlaVMSnoopingDBInnerDestIpAddrType_Type(InetAddressType):subtypeSpec=InetAddressType.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_AlaVMSnoopingDBInnerDestIpAddrType_Type.__name__=_K
_AlaVMSnoopingDBInnerDestIpAddrType_Object=MibTableColumn
alaVMSnoopingDBInnerDestIpAddrType=_AlaVMSnoopingDBInnerDestIpAddrType_Object((1,3,6,1,4,1,6486,801,1,2,1,84,1,1,5,1,15),_AlaVMSnoopingDBInnerDestIpAddrType_Type())
alaVMSnoopingDBInnerDestIpAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:alaVMSnoopingDBInnerDestIpAddrType.setStatus(_A)
class _AlaVMSnoopingDBInnerDestIpAddr_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_AlaVMSnoopingDBInnerDestIpAddr_Type.__name__=_J
_AlaVMSnoopingDBInnerDestIpAddr_Object=MibTableColumn
alaVMSnoopingDBInnerDestIpAddr=_AlaVMSnoopingDBInnerDestIpAddr_Object((1,3,6,1,4,1,6486,801,1,2,1,84,1,1,5,1,16),_AlaVMSnoopingDBInnerDestIpAddr_Type())
alaVMSnoopingDBInnerDestIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:alaVMSnoopingDBInnerDestIpAddr.setStatus(_A)
class _AlaVMSnoopingDBVInnerL4SrcPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AlaVMSnoopingDBVInnerL4SrcPort_Type.__name__=_D
_AlaVMSnoopingDBVInnerL4SrcPort_Object=MibTableColumn
alaVMSnoopingDBVInnerL4SrcPort=_AlaVMSnoopingDBVInnerL4SrcPort_Object((1,3,6,1,4,1,6486,801,1,2,1,84,1,1,5,1,17),_AlaVMSnoopingDBVInnerL4SrcPort_Type())
alaVMSnoopingDBVInnerL4SrcPort.setMaxAccess(_C)
if mibBuilder.loadTexts:alaVMSnoopingDBVInnerL4SrcPort.setStatus(_A)
class _AlaVMSnoopingDBVInnerL4DestPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AlaVMSnoopingDBVInnerL4DestPort_Type.__name__=_D
_AlaVMSnoopingDBVInnerL4DestPort_Object=MibTableColumn
alaVMSnoopingDBVInnerL4DestPort=_AlaVMSnoopingDBVInnerL4DestPort_Object((1,3,6,1,4,1,6486,801,1,2,1,84,1,1,5,1,18),_AlaVMSnoopingDBVInnerL4DestPort_Type())
alaVMSnoopingDBVInnerL4DestPort.setMaxAccess(_C)
if mibBuilder.loadTexts:alaVMSnoopingDBVInnerL4DestPort.setStatus(_A)
class _AlaVMSnoopingDBVInnerIPProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AlaVMSnoopingDBVInnerIPProtocol_Type.__name__=_D
_AlaVMSnoopingDBVInnerIPProtocol_Object=MibTableColumn
alaVMSnoopingDBVInnerIPProtocol=_AlaVMSnoopingDBVInnerIPProtocol_Object((1,3,6,1,4,1,6486,801,1,2,1,84,1,1,5,1,19),_AlaVMSnoopingDBVInnerIPProtocol_Type())
alaVMSnoopingDBVInnerIPProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:alaVMSnoopingDBVInnerIPProtocol.setStatus(_A)
class _AlaVMSnoopingDBPolicyRule_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_AlaVMSnoopingDBPolicyRule_Type.__name__=_G
_AlaVMSnoopingDBPolicyRule_Object=MibTableColumn
alaVMSnoopingDBPolicyRule=_AlaVMSnoopingDBPolicyRule_Object((1,3,6,1,4,1,6486,801,1,2,1,84,1,1,5,1,20),_AlaVMSnoopingDBPolicyRule_Type())
alaVMSnoopingDBPolicyRule.setMaxAccess(_C)
if mibBuilder.loadTexts:alaVMSnoopingDBPolicyRule.setStatus(_A)
class _AlaVMSnoopingDBPolicyList_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_AlaVMSnoopingDBPolicyList_Type.__name__=_G
_AlaVMSnoopingDBPolicyList_Object=MibTableColumn
alaVMSnoopingDBPolicyList=_AlaVMSnoopingDBPolicyList_Object((1,3,6,1,4,1,6486,801,1,2,1,84,1,1,5,1,21),_AlaVMSnoopingDBPolicyList_Type())
alaVMSnoopingDBPolicyList.setMaxAccess(_C)
if mibBuilder.loadTexts:alaVMSnoopingDBPolicyList.setStatus(_A)
_AlaVMSnoopingDBSamplingStatsPackets_Type=Counter64
_AlaVMSnoopingDBSamplingStatsPackets_Object=MibTableColumn
alaVMSnoopingDBSamplingStatsPackets=_AlaVMSnoopingDBSamplingStatsPackets_Object((1,3,6,1,4,1,6486,801,1,2,1,84,1,1,5,1,22),_AlaVMSnoopingDBSamplingStatsPackets_Type())
alaVMSnoopingDBSamplingStatsPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:alaVMSnoopingDBSamplingStatsPackets.setStatus(_A)
_AlaVMSnoopingHardwareStatsTable_Object=MibTable
alaVMSnoopingHardwareStatsTable=_AlaVMSnoopingHardwareStatsTable_Object((1,3,6,1,4,1,6486,801,1,2,1,84,1,1,6))
if mibBuilder.loadTexts:alaVMSnoopingHardwareStatsTable.setStatus(_A)
_AlaVMSnoopingHardwareStatsEntry_Object=MibTableRow
alaVMSnoopingHardwareStatsEntry=_AlaVMSnoopingHardwareStatsEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,84,1,1,6,1))
alaVMSnoopingHardwareStatsEntry.setIndexNames((0,_B,_b))
if mibBuilder.loadTexts:alaVMSnoopingHardwareStatsEntry.setStatus(_A)
_AlaVMSnoopingHardwareStatsIndex_Type=Unsigned32
_AlaVMSnoopingHardwareStatsIndex_Object=MibTableColumn
alaVMSnoopingHardwareStatsIndex=_AlaVMSnoopingHardwareStatsIndex_Object((1,3,6,1,4,1,6486,801,1,2,1,84,1,1,6,1,1),_AlaVMSnoopingHardwareStatsIndex_Type())
alaVMSnoopingHardwareStatsIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:alaVMSnoopingHardwareStatsIndex.setStatus(_A)
class _AlaVMSnoopingHardwareStatsPolicylist_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_AlaVMSnoopingHardwareStatsPolicylist_Type.__name__=_G
_AlaVMSnoopingHardwareStatsPolicylist_Object=MibTableColumn
alaVMSnoopingHardwareStatsPolicylist=_AlaVMSnoopingHardwareStatsPolicylist_Object((1,3,6,1,4,1,6486,801,1,2,1,84,1,1,6,1,2),_AlaVMSnoopingHardwareStatsPolicylist_Type())
alaVMSnoopingHardwareStatsPolicylist.setMaxAccess(_C)
if mibBuilder.loadTexts:alaVMSnoopingHardwareStatsPolicylist.setStatus(_A)
class _AlaVMSnoopingHardwareStatsPolicyrule_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_AlaVMSnoopingHardwareStatsPolicyrule_Type.__name__=_G
_AlaVMSnoopingHardwareStatsPolicyrule_Object=MibTableColumn
alaVMSnoopingHardwareStatsPolicyrule=_AlaVMSnoopingHardwareStatsPolicyrule_Object((1,3,6,1,4,1,6486,801,1,2,1,84,1,1,6,1,3),_AlaVMSnoopingHardwareStatsPolicyrule_Type())
alaVMSnoopingHardwareStatsPolicyrule.setMaxAccess(_C)
if mibBuilder.loadTexts:alaVMSnoopingHardwareStatsPolicyrule.setStatus(_A)
_AlaVMSnoopingHardwareStatsNumOfPackets_Type=Counter64
_AlaVMSnoopingHardwareStatsNumOfPackets_Object=MibTableColumn
alaVMSnoopingHardwareStatsNumOfPackets=_AlaVMSnoopingHardwareStatsNumOfPackets_Object((1,3,6,1,4,1,6486,801,1,2,1,84,1,1,6,1,4),_AlaVMSnoopingHardwareStatsNumOfPackets_Type())
alaVMSnoopingHardwareStatsNumOfPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:alaVMSnoopingHardwareStatsNumOfPackets.setStatus(_A)
_AlaVMSnoopingHardwareStatsNumOfBytes_Type=Counter64
_AlaVMSnoopingHardwareStatsNumOfBytes_Object=MibTableColumn
alaVMSnoopingHardwareStatsNumOfBytes=_AlaVMSnoopingHardwareStatsNumOfBytes_Object((1,3,6,1,4,1,6486,801,1,2,1,84,1,1,6,1,5),_AlaVMSnoopingHardwareStatsNumOfBytes_Type())
alaVMSnoopingHardwareStatsNumOfBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:alaVMSnoopingHardwareStatsNumOfBytes.setStatus(_A)
_AlaVMSnoopingFilterResourceTable_Object=MibTable
alaVMSnoopingFilterResourceTable=_AlaVMSnoopingFilterResourceTable_Object((1,3,6,1,4,1,6486,801,1,2,1,84,1,1,7))
if mibBuilder.loadTexts:alaVMSnoopingFilterResourceTable.setStatus(_A)
_AlaVMSnoopingFilterResourceEntry_Object=MibTableRow
alaVMSnoopingFilterResourceEntry=_AlaVMSnoopingFilterResourceEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,84,1,1,7,1))
alaVMSnoopingFilterResourceEntry.setIndexNames((0,_B,_c),(0,_B,_d))
if mibBuilder.loadTexts:alaVMSnoopingFilterResourceEntry.setStatus(_A)
_AlaVMSnoopingFilterResourceChassisId_Type=Unsigned32
_AlaVMSnoopingFilterResourceChassisId_Object=MibTableColumn
alaVMSnoopingFilterResourceChassisId=_AlaVMSnoopingFilterResourceChassisId_Object((1,3,6,1,4,1,6486,801,1,2,1,84,1,1,7,1,1),_AlaVMSnoopingFilterResourceChassisId_Type())
alaVMSnoopingFilterResourceChassisId.setMaxAccess(_F)
if mibBuilder.loadTexts:alaVMSnoopingFilterResourceChassisId.setStatus(_A)
_AlaVMSnoopingFilterResourceSlotNum_Type=Unsigned32
_AlaVMSnoopingFilterResourceSlotNum_Object=MibTableColumn
alaVMSnoopingFilterResourceSlotNum=_AlaVMSnoopingFilterResourceSlotNum_Object((1,3,6,1,4,1,6486,801,1,2,1,84,1,1,7,1,2),_AlaVMSnoopingFilterResourceSlotNum_Type())
alaVMSnoopingFilterResourceSlotNum.setMaxAccess(_F)
if mibBuilder.loadTexts:alaVMSnoopingFilterResourceSlotNum.setStatus(_A)
_AlaVMSnoopingFilterResourceMax_Type=Integer32
_AlaVMSnoopingFilterResourceMax_Object=MibTableColumn
alaVMSnoopingFilterResourceMax=_AlaVMSnoopingFilterResourceMax_Object((1,3,6,1,4,1,6486,801,1,2,1,84,1,1,7,1,3),_AlaVMSnoopingFilterResourceMax_Type())
alaVMSnoopingFilterResourceMax.setMaxAccess(_C)
if mibBuilder.loadTexts:alaVMSnoopingFilterResourceMax.setStatus(_A)
_AlaVMSnoopingFilterResourceUsed_Type=Integer32
_AlaVMSnoopingFilterResourceUsed_Object=MibTableColumn
alaVMSnoopingFilterResourceUsed=_AlaVMSnoopingFilterResourceUsed_Object((1,3,6,1,4,1,6486,801,1,2,1,84,1,1,7,1,4),_AlaVMSnoopingFilterResourceUsed_Type())
alaVMSnoopingFilterResourceUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:alaVMSnoopingFilterResourceUsed.setStatus(_A)
_AlaVMSnoopingLearntVMTable_Object=MibTable
alaVMSnoopingLearntVMTable=_AlaVMSnoopingLearntVMTable_Object((1,3,6,1,4,1,6486,801,1,2,1,84,1,1,8))
if mibBuilder.loadTexts:alaVMSnoopingLearntVMTable.setStatus(_A)
_AlaVMSnoopingLearntVMEntry_Object=MibTableRow
alaVMSnoopingLearntVMEntry=_AlaVMSnoopingLearntVMEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,84,1,1,8,1))
alaVMSnoopingLearntVMEntry.setIndexNames((0,_B,_e),(0,_B,_f))
if mibBuilder.loadTexts:alaVMSnoopingLearntVMEntry.setStatus(_A)
_AlaVMSnoopingLearntVMIfIndex_Type=InterfaceIndex
_AlaVMSnoopingLearntVMIfIndex_Object=MibTableColumn
alaVMSnoopingLearntVMIfIndex=_AlaVMSnoopingLearntVMIfIndex_Object((1,3,6,1,4,1,6486,801,1,2,1,84,1,1,8,1,1),_AlaVMSnoopingLearntVMIfIndex_Type())
alaVMSnoopingLearntVMIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:alaVMSnoopingLearntVMIfIndex.setStatus(_A)
_AlaVMSnoopingLearntVMSrcMac_Type=MacAddress
_AlaVMSnoopingLearntVMSrcMac_Object=MibTableColumn
alaVMSnoopingLearntVMSrcMac=_AlaVMSnoopingLearntVMSrcMac_Object((1,3,6,1,4,1,6486,801,1,2,1,84,1,1,8,1,2),_AlaVMSnoopingLearntVMSrcMac_Type())
alaVMSnoopingLearntVMSrcMac.setMaxAccess(_F)
if mibBuilder.loadTexts:alaVMSnoopingLearntVMSrcMac.setStatus(_A)
_AlaVMSnoopingLearntVMVlanId_Type=Integer32
_AlaVMSnoopingLearntVMVlanId_Object=MibTableColumn
alaVMSnoopingLearntVMVlanId=_AlaVMSnoopingLearntVMVlanId_Object((1,3,6,1,4,1,6486,801,1,2,1,84,1,1,8,1,3),_AlaVMSnoopingLearntVMVlanId_Type())
alaVMSnoopingLearntVMVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:alaVMSnoopingLearntVMVlanId.setStatus(_A)
_AlaVMSnoopingStaticPolicyTable_Object=MibTable
alaVMSnoopingStaticPolicyTable=_AlaVMSnoopingStaticPolicyTable_Object((1,3,6,1,4,1,6486,801,1,2,1,84,1,1,9))
if mibBuilder.loadTexts:alaVMSnoopingStaticPolicyTable.setStatus(_A)
_AlaVMSnoopingStaticPolicyEntry_Object=MibTableRow
alaVMSnoopingStaticPolicyEntry=_AlaVMSnoopingStaticPolicyEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,84,1,1,9,1))
alaVMSnoopingStaticPolicyEntry.setIndexNames((0,_B,_g),(0,_B,_h))
if mibBuilder.loadTexts:alaVMSnoopingStaticPolicyEntry.setStatus(_A)
class _AlaVMSnoopingStaticPolicyRuleName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_AlaVMSnoopingStaticPolicyRuleName_Type.__name__=_G
_AlaVMSnoopingStaticPolicyRuleName_Object=MibTableColumn
alaVMSnoopingStaticPolicyRuleName=_AlaVMSnoopingStaticPolicyRuleName_Object((1,3,6,1,4,1,6486,801,1,2,1,84,1,1,9,1,1),_AlaVMSnoopingStaticPolicyRuleName_Type())
alaVMSnoopingStaticPolicyRuleName.setMaxAccess(_F)
if mibBuilder.loadTexts:alaVMSnoopingStaticPolicyRuleName.setStatus(_A)
class _AlaVMSnoopingStaticPolicyListName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_AlaVMSnoopingStaticPolicyListName_Type.__name__=_G
_AlaVMSnoopingStaticPolicyListName_Object=MibTableColumn
alaVMSnoopingStaticPolicyListName=_AlaVMSnoopingStaticPolicyListName_Object((1,3,6,1,4,1,6486,801,1,2,1,84,1,1,9,1,2),_AlaVMSnoopingStaticPolicyListName_Type())
alaVMSnoopingStaticPolicyListName.setMaxAccess(_F)
if mibBuilder.loadTexts:alaVMSnoopingStaticPolicyListName.setStatus(_A)
_AlaVMSnoopingStaticPolicyRowStatus_Type=RowStatus
_AlaVMSnoopingStaticPolicyRowStatus_Object=MibTableColumn
alaVMSnoopingStaticPolicyRowStatus=_AlaVMSnoopingStaticPolicyRowStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,84,1,1,9,1,3),_AlaVMSnoopingStaticPolicyRowStatus_Type())
alaVMSnoopingStaticPolicyRowStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:alaVMSnoopingStaticPolicyRowStatus.setStatus(_A)
_AlaVMSnoopingMIBConformance_ObjectIdentity=ObjectIdentity
alaVMSnoopingMIBConformance=_AlaVMSnoopingMIBConformance_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,84,1,2))
if mibBuilder.loadTexts:alaVMSnoopingMIBConformance.setStatus(_A)
_AlaVMSnoopingMIBGroups_ObjectIdentity=ObjectIdentity
alaVMSnoopingMIBGroups=_AlaVMSnoopingMIBGroups_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,84,1,2,1))
if mibBuilder.loadTexts:alaVMSnoopingMIBGroups.setStatus(_A)
_AlaVMSnoopingMIBCompliances_ObjectIdentity=ObjectIdentity
alaVMSnoopingMIBCompliances=_AlaVMSnoopingMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,84,1,2,2))
if mibBuilder.loadTexts:alaVMSnoopingMIBCompliances.setStatus(_A)
alaVMSnoopingConfigGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,84,1,2,1,1))
alaVMSnoopingConfigGroup.setObjects(*((_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s)))
if mibBuilder.loadTexts:alaVMSnoopingConfigGroup.setStatus(_A)
alaVMSnoopingUdpPortGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,84,1,2,1,2))
alaVMSnoopingUdpPortGroup.setObjects((_B,_t))
if mibBuilder.loadTexts:alaVMSnoopingUdpPortGroup.setStatus(_A)
alaVMSnoopingPortGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,84,1,2,1,3))
alaVMSnoopingPortGroup.setObjects(*((_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y)))
if mibBuilder.loadTexts:alaVMSnoopingPortGroup.setStatus(_A)
alaVMSnoopingDBGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,84,1,2,1,4))
alaVMSnoopingDBGroup.setObjects(*((_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ)))
if mibBuilder.loadTexts:alaVMSnoopingDBGroup.setStatus(_A)
alaVMSnoopingHardwareStatsGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,84,1,2,1,5))
alaVMSnoopingHardwareStatsGroup.setObjects(*((_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN)))
if mibBuilder.loadTexts:alaVMSnoopingHardwareStatsGroup.setStatus(_A)
alaVMSnoopingFilterResourceGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,84,1,2,1,6))
alaVMSnoopingFilterResourceGroup.setObjects(*((_B,_AO),(_B,_AP)))
if mibBuilder.loadTexts:alaVMSnoopingFilterResourceGroup.setStatus(_A)
alaVMSnoopingTrapsObjGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,84,1,2,1,8))
alaVMSnoopingTrapsObjGroup.setObjects(*((_B,_N),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W)))
if mibBuilder.loadTexts:alaVMSnoopingTrapsObjGroup.setStatus(_A)
alaVMSnoopingLearntVMGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,84,1,2,1,9))
alaVMSnoopingLearntVMGroup.setObjects((_B,_AQ))
if mibBuilder.loadTexts:alaVMSnoopingLearntVMGroup.setStatus(_A)
alaVMSnoopingStaticPolicyGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,84,1,2,1,10))
alaVMSnoopingStaticPolicyGroup.setObjects((_B,_AR))
if mibBuilder.loadTexts:alaVMSnoopingStaticPolicyGroup.setStatus(_A)
alaVMSnoopingVMLearntAlert=NotificationType((1,3,6,1,4,1,6486,801,1,2,1,84,1,0,1))
alaVMSnoopingVMLearntAlert.setObjects(*((_B,_N),(_B,_R),(_B,_S)))
if mibBuilder.loadTexts:alaVMSnoopingVMLearntAlert.setStatus(_A)
alaVMSnoopingVMRemovedAlert=NotificationType((1,3,6,1,4,1,6486,801,1,2,1,84,1,0,2))
alaVMSnoopingVMRemovedAlert.setObjects((_B,_N))
if mibBuilder.loadTexts:alaVMSnoopingVMRemovedAlert.setStatus(_A)
alaVMSnoopingReservedHwResourceLimitAlert=NotificationType((1,3,6,1,4,1,6486,801,1,2,1,84,1,0,3))
alaVMSnoopingReservedHwResourceLimitAlert.setObjects(*((_B,_T),(_B,_U),(_B,_V),(_B,_W)))
if mibBuilder.loadTexts:alaVMSnoopingReservedHwResourceLimitAlert.setStatus(_A)
alaVMSnoopingNotificationGroup=NotificationGroup((1,3,6,1,4,1,6486,801,1,2,1,84,1,2,1,7))
alaVMSnoopingNotificationGroup.setObjects(*((_B,_AS),(_B,_AT),(_B,_AU)))
if mibBuilder.loadTexts:alaVMSnoopingNotificationGroup.setStatus(_A)
alaVMSnoopingMIBCompliance=ModuleCompliance((1,3,6,1,4,1,6486,801,1,2,1,84,1,2,2,1))
alaVMSnoopingMIBCompliance.setObjects(*((_B,_AV),(_B,_AW),(_B,_AX),(_B,_AY),(_B,_AZ),(_B,_Aa),(_B,_Ab),(_B,_Ac),(_B,_Ad),(_B,_Ae)))
if mibBuilder.loadTexts:alaVMSnoopingMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'alaVMSnoopingMIB':alaVMSnoopingMIB,'alaVMSnoopingMIBNotifications':alaVMSnoopingMIBNotifications,_AS:alaVMSnoopingVMLearntAlert,_AT:alaVMSnoopingVMRemovedAlert,_AU:alaVMSnoopingReservedHwResourceLimitAlert,'alaVMSnoopingMIBObjects':alaVMSnoopingMIBObjects,'alaVMSnoopingTrapsObj':alaVMSnoopingTrapsObj,_N:alaVMSnoopingLearnedMacAddress,_R:alaVMSnoopingLearnedVxlanUdpPort,_S:alaVMSnoopingLearnedVxlanVni,_U:alaVMSnoopingNiSlot,_V:alaVMSnoopingHwResourceTotal,_W:alaVMSnoopingHwResourceUsed,_T:alaVMSnoopingChassisId,'alaVMSnoopingConfig':alaVMSnoopingConfig,_i:alaVMSnoopingAdminStatus,_j:alaVMSnoopingPolicyMode,_k:alaVMSnoopingPolicyResource,_l:alaVMSnoopingVMTrafficTagged,_m:alaVMSnoopingTrapStatus,_n:alaVMSnoopingSamplingRate,_o:alaVMSnoopingAgingTimer,_p:alaVMSnoopingFilteringResourceTrapThreshold,_q:alaVMSnoopingClearAllData,_r:alaVMSnoopingLoggingThresholdFlows,_s:alaVMSnoopingQosAllocationStatus,'alaVMSnoopingUdpPortTable':alaVMSnoopingUdpPortTable,'alaVMSnoopingUdpPortEntry':alaVMSnoopingUdpPortEntry,_Y:alaVMSnoopingUdpPortIndex,_t:alaVMSnoopingUdpRowStatus,'alaVMSnoopingPortTable':alaVMSnoopingPortTable,'alaVMSnoopingPortEntry':alaVMSnoopingPortEntry,_Z:alaVMSnoopingPortIndex,_u:alaVMSnoopingPortAdminStatus,_v:alaVMSnoopingPortIsVNP,_w:alaVMSnoopingPortRowStatus,_x:alaVMSnoopingPortDBClear,_y:alaVMSnoopingPortSamplingClearStats,'alaVMSnoopingDBTable':alaVMSnoopingDBTable,'alaVMSnoopingDBEntry':alaVMSnoopingDBEntry,_a:alaVMSnoopingDBFlowId,_z:alaVMSnoopingDBIfIndex,_A0:alaVMSnoopingDBVxlanUdpDestPort,_A1:alaVMSnoopingDBVni,_A2:alaVMSnoopingDBVtepVlan,_A3:alaVMSnoopingDBVtepSrcIpAddrType,_A4:alaVMSnoopingDBVtepSrcIpAddr,_A5:alaVMSnoopingDBVtepDestIpAddrType,_A6:alaVMSnoopingDBVtepDestIpAddr,_A7:alaVMSnoopingDBInnerSrcMacAddr,_A8:alaVMSnoopingDBInnerDestMacAddr,_A9:alaVMSnoopingDBInnerVlan,_AA:alaVMSnoopingDBInnerSrcIpAddrType,_AB:alaVMSnoopingDBInnerSrcIpAddr,_AC:alaVMSnoopingDBInnerDestIpAddrType,_AD:alaVMSnoopingDBInnerDestIpAddr,_AE:alaVMSnoopingDBVInnerL4SrcPort,_AF:alaVMSnoopingDBVInnerL4DestPort,_AG:alaVMSnoopingDBVInnerIPProtocol,_AH:alaVMSnoopingDBPolicyRule,_AI:alaVMSnoopingDBPolicyList,_AJ:alaVMSnoopingDBSamplingStatsPackets,'alaVMSnoopingHardwareStatsTable':alaVMSnoopingHardwareStatsTable,'alaVMSnoopingHardwareStatsEntry':alaVMSnoopingHardwareStatsEntry,_b:alaVMSnoopingHardwareStatsIndex,_AK:alaVMSnoopingHardwareStatsPolicylist,_AL:alaVMSnoopingHardwareStatsPolicyrule,_AM:alaVMSnoopingHardwareStatsNumOfPackets,_AN:alaVMSnoopingHardwareStatsNumOfBytes,'alaVMSnoopingFilterResourceTable':alaVMSnoopingFilterResourceTable,'alaVMSnoopingFilterResourceEntry':alaVMSnoopingFilterResourceEntry,_c:alaVMSnoopingFilterResourceChassisId,_d:alaVMSnoopingFilterResourceSlotNum,_AO:alaVMSnoopingFilterResourceMax,_AP:alaVMSnoopingFilterResourceUsed,'alaVMSnoopingLearntVMTable':alaVMSnoopingLearntVMTable,'alaVMSnoopingLearntVMEntry':alaVMSnoopingLearntVMEntry,_e:alaVMSnoopingLearntVMIfIndex,_f:alaVMSnoopingLearntVMSrcMac,_AQ:alaVMSnoopingLearntVMVlanId,'alaVMSnoopingStaticPolicyTable':alaVMSnoopingStaticPolicyTable,'alaVMSnoopingStaticPolicyEntry':alaVMSnoopingStaticPolicyEntry,_g:alaVMSnoopingStaticPolicyRuleName,_h:alaVMSnoopingStaticPolicyListName,_AR:alaVMSnoopingStaticPolicyRowStatus,'alaVMSnoopingMIBConformance':alaVMSnoopingMIBConformance,'alaVMSnoopingMIBGroups':alaVMSnoopingMIBGroups,_AV:alaVMSnoopingConfigGroup,_AW:alaVMSnoopingUdpPortGroup,_AX:alaVMSnoopingPortGroup,_AY:alaVMSnoopingDBGroup,_AZ:alaVMSnoopingHardwareStatsGroup,_Aa:alaVMSnoopingFilterResourceGroup,_Ab:alaVMSnoopingNotificationGroup,_Ac:alaVMSnoopingTrapsObjGroup,_Ad:alaVMSnoopingLearntVMGroup,_Ae:alaVMSnoopingStaticPolicyGroup,'alaVMSnoopingMIBCompliances':alaVMSnoopingMIBCompliances,'alaVMSnoopingMIBCompliance':alaVMSnoopingMIBCompliance})