_b='uniExtAttributePortIndex'
_a='uniExtAttributeCardIndex'
_Z='uniBroadcastStormSuppressionPortIndex'
_Y='uniBroadcastStormSuppressionCardIndex'
_X='uniMirrorGroupIndex'
_W='Kbytes'
_V='uniPortRateLimitPortIndex'
_U='uniPortRateLimitCardIndex'
_T='uniPortRateLimitDeviceIndex'
_S='uniTrunkGroupIndex'
_R='uniTrunkGroupConfigIndex'
_Q='uniMacAddrVlanIdIndex'
_P='uniMacAddrIndex'
_O='uniAttributePortIndex'
_N='uniAttributeCardIndex'
_M='uniAttributeDeviceIndex'
_L='OctetString'
_K='testing'
_J='down'
_I='up'
_H='read-only'
_G='pps'
_F='Integer32'
_E='read-create'
_D='not-accessible'
_C='NSCRTV-EPON-UNI-MIB'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_L,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
AutoNegotiationTechAbility,EponAlarmCode,EponAlarmInstance,EponCardIndex,EponDeviceIndex,EponPortIndex,EponSeverityType,EponStats15MinRecordType,EponStats24HourRecordType,EponStatsThresholdType,TAddress,uniObjects=mibBuilder.importSymbols('NSCRTV-EPONEOC-EPON-MIB','AutoNegotiationTechAbility','EponAlarmCode','EponAlarmInstance','EponCardIndex','EponDeviceIndex','EponPortIndex','EponSeverityType','EponStats15MinRecordType','EponStats24HourRecordType','EponStatsThresholdType','TAddress','uniObjects')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TimeStamp','TruthValue')
_UniAttributeTable_Object=MibTable
uniAttributeTable=_UniAttributeTable_Object((1,3,6,1,4,1,17409,2,3,5,1))
if mibBuilder.loadTexts:uniAttributeTable.setStatus(_A)
_UniAttributeEntry_Object=MibTableRow
uniAttributeEntry=_UniAttributeEntry_Object((1,3,6,1,4,1,17409,2,3,5,1,1))
uniAttributeEntry.setIndexNames((0,_C,_M),(0,_C,_N),(0,_C,_O))
if mibBuilder.loadTexts:uniAttributeEntry.setStatus(_A)
_UniAttributeDeviceIndex_Type=EponDeviceIndex
_UniAttributeDeviceIndex_Object=MibTableColumn
uniAttributeDeviceIndex=_UniAttributeDeviceIndex_Object((1,3,6,1,4,1,17409,2,3,5,1,1,1),_UniAttributeDeviceIndex_Type())
uniAttributeDeviceIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:uniAttributeDeviceIndex.setStatus(_A)
_UniAttributeCardIndex_Type=EponCardIndex
_UniAttributeCardIndex_Object=MibTableColumn
uniAttributeCardIndex=_UniAttributeCardIndex_Object((1,3,6,1,4,1,17409,2,3,5,1,1,2),_UniAttributeCardIndex_Type())
uniAttributeCardIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:uniAttributeCardIndex.setStatus(_A)
_UniAttributePortIndex_Type=EponPortIndex
_UniAttributePortIndex_Object=MibTableColumn
uniAttributePortIndex=_UniAttributePortIndex_Object((1,3,6,1,4,1,17409,2,3,5,1,1,3),_UniAttributePortIndex_Type())
uniAttributePortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:uniAttributePortIndex.setStatus(_A)
class _UniAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),(_J,2),(_K,3)))
_UniAdminStatus_Type.__name__=_F
_UniAdminStatus_Object=MibTableColumn
uniAdminStatus=_UniAdminStatus_Object((1,3,6,1,4,1,17409,2,3,5,1,1,4),_UniAdminStatus_Type())
uniAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:uniAdminStatus.setStatus(_A)
class _UniOperationStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),(_J,2),(_K,3)))
_UniOperationStatus_Type.__name__=_F
_UniOperationStatus_Object=MibTableColumn
uniOperationStatus=_UniOperationStatus_Object((1,3,6,1,4,1,17409,2,3,5,1,1,5),_UniOperationStatus_Type())
uniOperationStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:uniOperationStatus.setStatus(_A)
_UniAutoNegotiationEnable_Type=TruthValue
_UniAutoNegotiationEnable_Object=MibTableColumn
uniAutoNegotiationEnable=_UniAutoNegotiationEnable_Object((1,3,6,1,4,1,17409,2,3,5,1,1,6),_UniAutoNegotiationEnable_Type())
uniAutoNegotiationEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:uniAutoNegotiationEnable.setStatus(_A)
_UniAutoNegotiationLocalTechAbility_Type=AutoNegotiationTechAbility
_UniAutoNegotiationLocalTechAbility_Object=MibTableColumn
uniAutoNegotiationLocalTechAbility=_UniAutoNegotiationLocalTechAbility_Object((1,3,6,1,4,1,17409,2,3,5,1,1,7),_UniAutoNegotiationLocalTechAbility_Type())
uniAutoNegotiationLocalTechAbility.setMaxAccess(_H)
if mibBuilder.loadTexts:uniAutoNegotiationLocalTechAbility.setStatus(_A)
class _UniAutoNegotiationRestart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('restart',1))
_UniAutoNegotiationRestart_Type.__name__=_F
_UniAutoNegotiationRestart_Object=MibTableColumn
uniAutoNegotiationRestart=_UniAutoNegotiationRestart_Object((1,3,6,1,4,1,17409,2,3,5,1,1,9),_UniAutoNegotiationRestart_Type())
uniAutoNegotiationRestart.setMaxAccess(_B)
if mibBuilder.loadTexts:uniAutoNegotiationRestart.setStatus(_A)
_UniMacAddressManagement_ObjectIdentity=ObjectIdentity
uniMacAddressManagement=_UniMacAddressManagement_ObjectIdentity((1,3,6,1,4,1,17409,2,3,5,2))
if mibBuilder.loadTexts:uniMacAddressManagement.setStatus(_A)
_UniMacAddressManagementNode_ObjectIdentity=ObjectIdentity
uniMacAddressManagementNode=_UniMacAddressManagementNode_ObjectIdentity((1,3,6,1,4,1,17409,2,3,5,2,1))
if mibBuilder.loadTexts:uniMacAddressManagementNode.setStatus(_A)
_UniMacAddrAgingTime_Type=Integer32
_UniMacAddrAgingTime_Object=MibScalar
uniMacAddrAgingTime=_UniMacAddrAgingTime_Object((1,3,6,1,4,1,17409,2,3,5,2,1,1),_UniMacAddrAgingTime_Type())
uniMacAddrAgingTime.setMaxAccess(_B)
if mibBuilder.loadTexts:uniMacAddrAgingTime.setStatus(_A)
if mibBuilder.loadTexts:uniMacAddrAgingTime.setUnits('Seconds')
class _UniMacAddrClear_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('allDynamic',1))
_UniMacAddrClear_Type.__name__=_F
_UniMacAddrClear_Object=MibScalar
uniMacAddrClear=_UniMacAddrClear_Object((1,3,6,1,4,1,17409,2,3,5,2,1,2),_UniMacAddrClear_Type())
uniMacAddrClear.setMaxAccess(_B)
if mibBuilder.loadTexts:uniMacAddrClear.setStatus(_A)
_UniMacAddressTable_Object=MibTable
uniMacAddressTable=_UniMacAddressTable_Object((1,3,6,1,4,1,17409,2,3,5,2,2))
if mibBuilder.loadTexts:uniMacAddressTable.setStatus(_A)
_UniMacAddressEntry_Object=MibTableRow
uniMacAddressEntry=_UniMacAddressEntry_Object((1,3,6,1,4,1,17409,2,3,5,2,2,1))
uniMacAddressEntry.setIndexNames((0,_C,_P),(0,_C,_Q))
if mibBuilder.loadTexts:uniMacAddressEntry.setStatus(_A)
_UniMacAddrIndex_Type=MacAddress
_UniMacAddrIndex_Object=MibTableColumn
uniMacAddrIndex=_UniMacAddrIndex_Object((1,3,6,1,4,1,17409,2,3,5,2,2,1,1),_UniMacAddrIndex_Type())
uniMacAddrIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:uniMacAddrIndex.setStatus(_A)
_UniMacAddrVlanIdIndex_Type=Integer32
_UniMacAddrVlanIdIndex_Object=MibTableColumn
uniMacAddrVlanIdIndex=_UniMacAddrVlanIdIndex_Object((1,3,6,1,4,1,17409,2,3,5,2,2,1,2),_UniMacAddrVlanIdIndex_Type())
uniMacAddrVlanIdIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:uniMacAddrVlanIdIndex.setStatus(_A)
class _UniMacAddrType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('static',1),('dynamic',2),('other',3)))
_UniMacAddrType_Type.__name__=_F
_UniMacAddrType_Object=MibTableColumn
uniMacAddrType=_UniMacAddrType_Object((1,3,6,1,4,1,17409,2,3,5,2,2,1,3),_UniMacAddrType_Type())
uniMacAddrType.setMaxAccess(_E)
if mibBuilder.loadTexts:uniMacAddrType.setStatus(_A)
class _UniMacAddrPortId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_UniMacAddrPortId_Type.__name__=_L
_UniMacAddrPortId_Object=MibTableColumn
uniMacAddrPortId=_UniMacAddrPortId_Object((1,3,6,1,4,1,17409,2,3,5,2,2,1,4),_UniMacAddrPortId_Type())
uniMacAddrPortId.setMaxAccess(_E)
if mibBuilder.loadTexts:uniMacAddrPortId.setStatus(_A)
_UniMacAddrRowStatus_Type=RowStatus
_UniMacAddrRowStatus_Object=MibTableColumn
uniMacAddrRowStatus=_UniMacAddrRowStatus_Object((1,3,6,1,4,1,17409,2,3,5,2,2,1,5),_UniMacAddrRowStatus_Type())
uniMacAddrRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:uniMacAddrRowStatus.setStatus(_A)
_UniTrunkManagement_ObjectIdentity=ObjectIdentity
uniTrunkManagement=_UniTrunkManagement_ObjectIdentity((1,3,6,1,4,1,17409,2,3,5,3))
if mibBuilder.loadTexts:uniTrunkManagement.setStatus(_A)
_UniTrunkGroupConfigTable_Object=MibTable
uniTrunkGroupConfigTable=_UniTrunkGroupConfigTable_Object((1,3,6,1,4,1,17409,2,3,5,3,1))
if mibBuilder.loadTexts:uniTrunkGroupConfigTable.setStatus(_A)
_UniTrunkGroupConfigEntry_Object=MibTableRow
uniTrunkGroupConfigEntry=_UniTrunkGroupConfigEntry_Object((1,3,6,1,4,1,17409,2,3,5,3,1,1))
uniTrunkGroupConfigEntry.setIndexNames((0,_C,_R))
if mibBuilder.loadTexts:uniTrunkGroupConfigEntry.setStatus(_A)
_UniTrunkGroupConfigIndex_Type=Integer32
_UniTrunkGroupConfigIndex_Object=MibTableColumn
uniTrunkGroupConfigIndex=_UniTrunkGroupConfigIndex_Object((1,3,6,1,4,1,17409,2,3,5,3,1,1,1),_UniTrunkGroupConfigIndex_Type())
uniTrunkGroupConfigIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:uniTrunkGroupConfigIndex.setStatus(_A)
_UniTrunkGroupConfigName_Type=DisplayString
_UniTrunkGroupConfigName_Object=MibTableColumn
uniTrunkGroupConfigName=_UniTrunkGroupConfigName_Object((1,3,6,1,4,1,17409,2,3,5,3,1,1,2),_UniTrunkGroupConfigName_Type())
uniTrunkGroupConfigName.setMaxAccess(_E)
if mibBuilder.loadTexts:uniTrunkGroupConfigName.setStatus(_A)
_UniTrunkGroupConfigMember_Type=OctetString
_UniTrunkGroupConfigMember_Object=MibTableColumn
uniTrunkGroupConfigMember=_UniTrunkGroupConfigMember_Object((1,3,6,1,4,1,17409,2,3,5,3,1,1,3),_UniTrunkGroupConfigMember_Type())
uniTrunkGroupConfigMember.setMaxAccess(_E)
if mibBuilder.loadTexts:uniTrunkGroupConfigMember.setStatus(_A)
class _UniTrunkGroupConfigPolicy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('srcMac',1),('destMac',2),('srcMacNDestMac',3),('srcIp',4),('destIp',5),('srcIpNDestIp',6)))
_UniTrunkGroupConfigPolicy_Type.__name__=_F
_UniTrunkGroupConfigPolicy_Object=MibTableColumn
uniTrunkGroupConfigPolicy=_UniTrunkGroupConfigPolicy_Object((1,3,6,1,4,1,17409,2,3,5,3,1,1,4),_UniTrunkGroupConfigPolicy_Type())
uniTrunkGroupConfigPolicy.setMaxAccess(_E)
if mibBuilder.loadTexts:uniTrunkGroupConfigPolicy.setStatus(_A)
_UniTrunkGroupConfigRowstatus_Type=RowStatus
_UniTrunkGroupConfigRowstatus_Object=MibTableColumn
uniTrunkGroupConfigRowstatus=_UniTrunkGroupConfigRowstatus_Object((1,3,6,1,4,1,17409,2,3,5,3,1,1,5),_UniTrunkGroupConfigRowstatus_Type())
uniTrunkGroupConfigRowstatus.setMaxAccess(_E)
if mibBuilder.loadTexts:uniTrunkGroupConfigRowstatus.setStatus(_A)
_UniTrunkGroupTable_Object=MibTable
uniTrunkGroupTable=_UniTrunkGroupTable_Object((1,3,6,1,4,1,17409,2,3,5,3,2))
if mibBuilder.loadTexts:uniTrunkGroupTable.setStatus(_A)
_UniTrunkGroupEntry_Object=MibTableRow
uniTrunkGroupEntry=_UniTrunkGroupEntry_Object((1,3,6,1,4,1,17409,2,3,5,3,2,1))
uniTrunkGroupEntry.setIndexNames((0,_C,_S))
if mibBuilder.loadTexts:uniTrunkGroupEntry.setStatus(_A)
_UniTrunkGroupIndex_Type=Integer32
_UniTrunkGroupIndex_Object=MibTableColumn
uniTrunkGroupIndex=_UniTrunkGroupIndex_Object((1,3,6,1,4,1,17409,2,3,5,3,2,1,1),_UniTrunkGroupIndex_Type())
uniTrunkGroupIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:uniTrunkGroupIndex.setStatus(_A)
class _UniTrunkGroupOperationStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),(_J,2),(_K,3)))
_UniTrunkGroupOperationStatus_Type.__name__=_F
_UniTrunkGroupOperationStatus_Object=MibTableColumn
uniTrunkGroupOperationStatus=_UniTrunkGroupOperationStatus_Object((1,3,6,1,4,1,17409,2,3,5,3,2,1,2),_UniTrunkGroupOperationStatus_Type())
uniTrunkGroupOperationStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:uniTrunkGroupOperationStatus.setStatus(_A)
_UniTrunkGroupActualSpeed_Type=Integer32
_UniTrunkGroupActualSpeed_Object=MibTableColumn
uniTrunkGroupActualSpeed=_UniTrunkGroupActualSpeed_Object((1,3,6,1,4,1,17409,2,3,5,3,2,1,3),_UniTrunkGroupActualSpeed_Type())
uniTrunkGroupActualSpeed.setMaxAccess(_H)
if mibBuilder.loadTexts:uniTrunkGroupActualSpeed.setStatus(_A)
if mibBuilder.loadTexts:uniTrunkGroupActualSpeed.setUnits('Mbps')
class _UniTrunkGroupAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),(_J,2),(_K,3)))
_UniTrunkGroupAdminStatus_Type.__name__=_F
_UniTrunkGroupAdminStatus_Object=MibTableColumn
uniTrunkGroupAdminStatus=_UniTrunkGroupAdminStatus_Object((1,3,6,1,4,1,17409,2,3,5,3,2,1,4),_UniTrunkGroupAdminStatus_Type())
uniTrunkGroupAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:uniTrunkGroupAdminStatus.setStatus(_A)
_UniPortRateLimitTable_Object=MibTable
uniPortRateLimitTable=_UniPortRateLimitTable_Object((1,3,6,1,4,1,17409,2,3,5,4))
if mibBuilder.loadTexts:uniPortRateLimitTable.setStatus(_A)
_UniPortRateLimitEntry_Object=MibTableRow
uniPortRateLimitEntry=_UniPortRateLimitEntry_Object((1,3,6,1,4,1,17409,2,3,5,4,1))
uniPortRateLimitEntry.setIndexNames((0,_C,_T),(0,_C,_U),(0,_C,_V))
if mibBuilder.loadTexts:uniPortRateLimitEntry.setStatus(_A)
_UniPortRateLimitDeviceIndex_Type=EponDeviceIndex
_UniPortRateLimitDeviceIndex_Object=MibTableColumn
uniPortRateLimitDeviceIndex=_UniPortRateLimitDeviceIndex_Object((1,3,6,1,4,1,17409,2,3,5,4,1,1),_UniPortRateLimitDeviceIndex_Type())
uniPortRateLimitDeviceIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:uniPortRateLimitDeviceIndex.setStatus(_A)
_UniPortRateLimitCardIndex_Type=EponCardIndex
_UniPortRateLimitCardIndex_Object=MibTableColumn
uniPortRateLimitCardIndex=_UniPortRateLimitCardIndex_Object((1,3,6,1,4,1,17409,2,3,5,4,1,2),_UniPortRateLimitCardIndex_Type())
uniPortRateLimitCardIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:uniPortRateLimitCardIndex.setStatus(_A)
_UniPortRateLimitPortIndex_Type=EponPortIndex
_UniPortRateLimitPortIndex_Object=MibTableColumn
uniPortRateLimitPortIndex=_UniPortRateLimitPortIndex_Object((1,3,6,1,4,1,17409,2,3,5,4,1,3),_UniPortRateLimitPortIndex_Type())
uniPortRateLimitPortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:uniPortRateLimitPortIndex.setStatus(_A)
_UniPortInCIR_Type=Integer32
_UniPortInCIR_Object=MibTableColumn
uniPortInCIR=_UniPortInCIR_Object((1,3,6,1,4,1,17409,2,3,5,4,1,4),_UniPortInCIR_Type())
uniPortInCIR.setMaxAccess(_B)
if mibBuilder.loadTexts:uniPortInCIR.setStatus(_A)
if mibBuilder.loadTexts:uniPortInCIR.setUnits('kbps')
_UniPortInCBS_Type=Integer32
_UniPortInCBS_Object=MibTableColumn
uniPortInCBS=_UniPortInCBS_Object((1,3,6,1,4,1,17409,2,3,5,4,1,5),_UniPortInCBS_Type())
uniPortInCBS.setMaxAccess(_B)
if mibBuilder.loadTexts:uniPortInCBS.setStatus(_A)
if mibBuilder.loadTexts:uniPortInCBS.setUnits(_W)
_UniPortInEBS_Type=Integer32
_UniPortInEBS_Object=MibTableColumn
uniPortInEBS=_UniPortInEBS_Object((1,3,6,1,4,1,17409,2,3,5,4,1,6),_UniPortInEBS_Type())
uniPortInEBS.setMaxAccess(_B)
if mibBuilder.loadTexts:uniPortInEBS.setStatus(_A)
if mibBuilder.loadTexts:uniPortInEBS.setUnits(_W)
_UniPortOutCIR_Type=Integer32
_UniPortOutCIR_Object=MibTableColumn
uniPortOutCIR=_UniPortOutCIR_Object((1,3,6,1,4,1,17409,2,3,5,4,1,7),_UniPortOutCIR_Type())
uniPortOutCIR.setMaxAccess(_B)
if mibBuilder.loadTexts:uniPortOutCIR.setStatus(_A)
if mibBuilder.loadTexts:uniPortOutCIR.setUnits('Kbps')
_UniPortOutPIR_Type=Integer32
_UniPortOutPIR_Object=MibTableColumn
uniPortOutPIR=_UniPortOutPIR_Object((1,3,6,1,4,1,17409,2,3,5,4,1,8),_UniPortOutPIR_Type())
uniPortOutPIR.setMaxAccess(_B)
if mibBuilder.loadTexts:uniPortOutPIR.setStatus(_A)
if mibBuilder.loadTexts:uniPortOutPIR.setUnits('Kbps')
_UniPortInRateLimitEnable_Type=TruthValue
_UniPortInRateLimitEnable_Object=MibTableColumn
uniPortInRateLimitEnable=_UniPortInRateLimitEnable_Object((1,3,6,1,4,1,17409,2,3,5,4,1,9),_UniPortInRateLimitEnable_Type())
uniPortInRateLimitEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:uniPortInRateLimitEnable.setStatus(_A)
_UniPortOutRateLimitEnable_Type=TruthValue
_UniPortOutRateLimitEnable_Object=MibTableColumn
uniPortOutRateLimitEnable=_UniPortOutRateLimitEnable_Object((1,3,6,1,4,1,17409,2,3,5,4,1,10),_UniPortOutRateLimitEnable_Type())
uniPortOutRateLimitEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:uniPortOutRateLimitEnable.setStatus(_A)
_UniMirrorTable_Object=MibTable
uniMirrorTable=_UniMirrorTable_Object((1,3,6,1,4,1,17409,2,3,5,5))
if mibBuilder.loadTexts:uniMirrorTable.setStatus(_A)
_UniMirrorEntry_Object=MibTableRow
uniMirrorEntry=_UniMirrorEntry_Object((1,3,6,1,4,1,17409,2,3,5,5,1))
uniMirrorEntry.setIndexNames((0,_C,_X))
if mibBuilder.loadTexts:uniMirrorEntry.setStatus(_A)
_UniMirrorGroupIndex_Type=Integer32
_UniMirrorGroupIndex_Object=MibTableColumn
uniMirrorGroupIndex=_UniMirrorGroupIndex_Object((1,3,6,1,4,1,17409,2,3,5,5,1,1),_UniMirrorGroupIndex_Type())
uniMirrorGroupIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:uniMirrorGroupIndex.setStatus(_A)
_UniMirrorGroupName_Type=DisplayString
_UniMirrorGroupName_Object=MibTableColumn
uniMirrorGroupName=_UniMirrorGroupName_Object((1,3,6,1,4,1,17409,2,3,5,5,1,2),_UniMirrorGroupName_Type())
uniMirrorGroupName.setMaxAccess(_E)
if mibBuilder.loadTexts:uniMirrorGroupName.setStatus(_A)
_UniMirrorGroupDstPortList_Type=OctetString
_UniMirrorGroupDstPortList_Object=MibTableColumn
uniMirrorGroupDstPortList=_UniMirrorGroupDstPortList_Object((1,3,6,1,4,1,17409,2,3,5,5,1,3),_UniMirrorGroupDstPortList_Type())
uniMirrorGroupDstPortList.setMaxAccess(_E)
if mibBuilder.loadTexts:uniMirrorGroupDstPortList.setStatus(_A)
_UniMirrorGroupSrcInPortList_Type=OctetString
_UniMirrorGroupSrcInPortList_Object=MibTableColumn
uniMirrorGroupSrcInPortList=_UniMirrorGroupSrcInPortList_Object((1,3,6,1,4,1,17409,2,3,5,5,1,4),_UniMirrorGroupSrcInPortList_Type())
uniMirrorGroupSrcInPortList.setMaxAccess(_E)
if mibBuilder.loadTexts:uniMirrorGroupSrcInPortList.setStatus(_A)
_UniMirrorGroupSrcOutPortList_Type=OctetString
_UniMirrorGroupSrcOutPortList_Object=MibTableColumn
uniMirrorGroupSrcOutPortList=_UniMirrorGroupSrcOutPortList_Object((1,3,6,1,4,1,17409,2,3,5,5,1,5),_UniMirrorGroupSrcOutPortList_Type())
uniMirrorGroupSrcOutPortList.setMaxAccess(_E)
if mibBuilder.loadTexts:uniMirrorGroupSrcOutPortList.setStatus(_A)
_UniMirrorGroupRowstatus_Type=RowStatus
_UniMirrorGroupRowstatus_Object=MibTableColumn
uniMirrorGroupRowstatus=_UniMirrorGroupRowstatus_Object((1,3,6,1,4,1,17409,2,3,5,5,1,6),_UniMirrorGroupRowstatus_Type())
uniMirrorGroupRowstatus.setMaxAccess(_E)
if mibBuilder.loadTexts:uniMirrorGroupRowstatus.setStatus(_A)
_UniBroadcastStormSuppressionTable_Object=MibTable
uniBroadcastStormSuppressionTable=_UniBroadcastStormSuppressionTable_Object((1,3,6,1,4,1,17409,2,3,5,6))
if mibBuilder.loadTexts:uniBroadcastStormSuppressionTable.setStatus(_A)
_UniBroadcastStormSuppressionEntry_Object=MibTableRow
uniBroadcastStormSuppressionEntry=_UniBroadcastStormSuppressionEntry_Object((1,3,6,1,4,1,17409,2,3,5,6,1))
uniBroadcastStormSuppressionEntry.setIndexNames((0,_C,_Y),(0,_C,_Z))
if mibBuilder.loadTexts:uniBroadcastStormSuppressionEntry.setStatus(_A)
_UniBroadcastStormSuppressionCardIndex_Type=EponCardIndex
_UniBroadcastStormSuppressionCardIndex_Object=MibTableColumn
uniBroadcastStormSuppressionCardIndex=_UniBroadcastStormSuppressionCardIndex_Object((1,3,6,1,4,1,17409,2,3,5,6,1,1),_UniBroadcastStormSuppressionCardIndex_Type())
uniBroadcastStormSuppressionCardIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:uniBroadcastStormSuppressionCardIndex.setStatus(_A)
_UniBroadcastStormSuppressionPortIndex_Type=EponPortIndex
_UniBroadcastStormSuppressionPortIndex_Object=MibTableColumn
uniBroadcastStormSuppressionPortIndex=_UniBroadcastStormSuppressionPortIndex_Object((1,3,6,1,4,1,17409,2,3,5,6,1,2),_UniBroadcastStormSuppressionPortIndex_Type())
uniBroadcastStormSuppressionPortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:uniBroadcastStormSuppressionPortIndex.setStatus(_A)
_UniUnicastStormEnable_Type=TruthValue
_UniUnicastStormEnable_Object=MibTableColumn
uniUnicastStormEnable=_UniUnicastStormEnable_Object((1,3,6,1,4,1,17409,2,3,5,6,1,3),_UniUnicastStormEnable_Type())
uniUnicastStormEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:uniUnicastStormEnable.setStatus(_A)
_UniUnicastStormInPacketRate_Type=Integer32
_UniUnicastStormInPacketRate_Object=MibTableColumn
uniUnicastStormInPacketRate=_UniUnicastStormInPacketRate_Object((1,3,6,1,4,1,17409,2,3,5,6,1,4),_UniUnicastStormInPacketRate_Type())
uniUnicastStormInPacketRate.setMaxAccess(_B)
if mibBuilder.loadTexts:uniUnicastStormInPacketRate.setStatus(_A)
if mibBuilder.loadTexts:uniUnicastStormInPacketRate.setUnits(_G)
_UniUnicastStormOutPacketRate_Type=Integer32
_UniUnicastStormOutPacketRate_Object=MibTableColumn
uniUnicastStormOutPacketRate=_UniUnicastStormOutPacketRate_Object((1,3,6,1,4,1,17409,2,3,5,6,1,5),_UniUnicastStormOutPacketRate_Type())
uniUnicastStormOutPacketRate.setMaxAccess(_B)
if mibBuilder.loadTexts:uniUnicastStormOutPacketRate.setStatus(_A)
if mibBuilder.loadTexts:uniUnicastStormOutPacketRate.setUnits(_G)
_UniMulticastStormEnable_Type=TruthValue
_UniMulticastStormEnable_Object=MibTableColumn
uniMulticastStormEnable=_UniMulticastStormEnable_Object((1,3,6,1,4,1,17409,2,3,5,6,1,6),_UniMulticastStormEnable_Type())
uniMulticastStormEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:uniMulticastStormEnable.setStatus(_A)
_UniMulticastStormInPacketRate_Type=Integer32
_UniMulticastStormInPacketRate_Object=MibTableColumn
uniMulticastStormInPacketRate=_UniMulticastStormInPacketRate_Object((1,3,6,1,4,1,17409,2,3,5,6,1,7),_UniMulticastStormInPacketRate_Type())
uniMulticastStormInPacketRate.setMaxAccess(_B)
if mibBuilder.loadTexts:uniMulticastStormInPacketRate.setStatus(_A)
if mibBuilder.loadTexts:uniMulticastStormInPacketRate.setUnits(_G)
_UniMulticastStormOutPacketRate_Type=Integer32
_UniMulticastStormOutPacketRate_Object=MibTableColumn
uniMulticastStormOutPacketRate=_UniMulticastStormOutPacketRate_Object((1,3,6,1,4,1,17409,2,3,5,6,1,8),_UniMulticastStormOutPacketRate_Type())
uniMulticastStormOutPacketRate.setMaxAccess(_B)
if mibBuilder.loadTexts:uniMulticastStormOutPacketRate.setStatus(_A)
if mibBuilder.loadTexts:uniMulticastStormOutPacketRate.setUnits(_G)
_UniBroadcastStormEnable_Type=TruthValue
_UniBroadcastStormEnable_Object=MibTableColumn
uniBroadcastStormEnable=_UniBroadcastStormEnable_Object((1,3,6,1,4,1,17409,2,3,5,6,1,9),_UniBroadcastStormEnable_Type())
uniBroadcastStormEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:uniBroadcastStormEnable.setStatus(_A)
_UniBroadcastStormInPacketRate_Type=Integer32
_UniBroadcastStormInPacketRate_Object=MibTableColumn
uniBroadcastStormInPacketRate=_UniBroadcastStormInPacketRate_Object((1,3,6,1,4,1,17409,2,3,5,6,1,10),_UniBroadcastStormInPacketRate_Type())
uniBroadcastStormInPacketRate.setMaxAccess(_B)
if mibBuilder.loadTexts:uniBroadcastStormInPacketRate.setStatus(_A)
if mibBuilder.loadTexts:uniBroadcastStormInPacketRate.setUnits(_G)
_UniBroadcastStormOutPacketRate_Type=Integer32
_UniBroadcastStormOutPacketRate_Object=MibTableColumn
uniBroadcastStormOutPacketRate=_UniBroadcastStormOutPacketRate_Object((1,3,6,1,4,1,17409,2,3,5,6,1,11),_UniBroadcastStormOutPacketRate_Type())
uniBroadcastStormOutPacketRate.setMaxAccess(_B)
if mibBuilder.loadTexts:uniBroadcastStormOutPacketRate.setStatus(_A)
if mibBuilder.loadTexts:uniBroadcastStormOutPacketRate.setUnits(_G)
_UniExtAttributeTable_Object=MibTable
uniExtAttributeTable=_UniExtAttributeTable_Object((1,3,6,1,4,1,17409,2,3,5,7))
if mibBuilder.loadTexts:uniExtAttributeTable.setStatus(_A)
_UniExtAttributeEntry_Object=MibTableRow
uniExtAttributeEntry=_UniExtAttributeEntry_Object((1,3,6,1,4,1,17409,2,3,5,7,1))
uniExtAttributeEntry.setIndexNames((0,_C,_a),(0,_C,_b))
if mibBuilder.loadTexts:uniExtAttributeEntry.setStatus(_A)
_UniExtAttributeCardIndex_Type=EponCardIndex
_UniExtAttributeCardIndex_Object=MibTableColumn
uniExtAttributeCardIndex=_UniExtAttributeCardIndex_Object((1,3,6,1,4,1,17409,2,3,5,7,1,1),_UniExtAttributeCardIndex_Type())
uniExtAttributeCardIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:uniExtAttributeCardIndex.setStatus(_A)
_UniExtAttributePortIndex_Type=EponPortIndex
_UniExtAttributePortIndex_Object=MibTableColumn
uniExtAttributePortIndex=_UniExtAttributePortIndex_Object((1,3,6,1,4,1,17409,2,3,5,7,1,2),_UniExtAttributePortIndex_Type())
uniExtAttributePortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:uniExtAttributePortIndex.setStatus(_A)
_UniPerfStats15minuteEnable_Type=TruthValue
_UniPerfStats15minuteEnable_Object=MibTableColumn
uniPerfStats15minuteEnable=_UniPerfStats15minuteEnable_Object((1,3,6,1,4,1,17409,2,3,5,7,1,3),_UniPerfStats15minuteEnable_Type())
uniPerfStats15minuteEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:uniPerfStats15minuteEnable.setStatus(_A)
_UniPerfStats24hourEnable_Type=TruthValue
_UniPerfStats24hourEnable_Object=MibTableColumn
uniPerfStats24hourEnable=_UniPerfStats24hourEnable_Object((1,3,6,1,4,1,17409,2,3,5,7,1,4),_UniPerfStats24hourEnable_Type())
uniPerfStats24hourEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:uniPerfStats24hourEnable.setStatus(_A)
_UniLastChangeTime_Type=TimeTicks
_UniLastChangeTime_Object=MibTableColumn
uniLastChangeTime=_UniLastChangeTime_Object((1,3,6,1,4,1,17409,2,3,5,7,1,5),_UniLastChangeTime_Type())
uniLastChangeTime.setMaxAccess(_H)
if mibBuilder.loadTexts:uniLastChangeTime.setStatus(_A)
_UniIsolationEnable_Type=TruthValue
_UniIsolationEnable_Object=MibTableColumn
uniIsolationEnable=_UniIsolationEnable_Object((1,3,6,1,4,1,17409,2,3,5,7,1,6),_UniIsolationEnable_Type())
uniIsolationEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:uniIsolationEnable.setStatus(_A)
_UniMacAddrLearnMaxNum_Type=Integer32
_UniMacAddrLearnMaxNum_Object=MibTableColumn
uniMacAddrLearnMaxNum=_UniMacAddrLearnMaxNum_Object((1,3,6,1,4,1,17409,2,3,5,7,1,7),_UniMacAddrLearnMaxNum_Type())
uniMacAddrLearnMaxNum.setMaxAccess(_B)
if mibBuilder.loadTexts:uniMacAddrLearnMaxNum.setStatus(_A)
_UniAutoNegotiationAdvertisedTechAbility_Type=AutoNegotiationTechAbility
_UniAutoNegotiationAdvertisedTechAbility_Object=MibTableColumn
uniAutoNegotiationAdvertisedTechAbility=_UniAutoNegotiationAdvertisedTechAbility_Object((1,3,6,1,4,1,17409,2,3,5,7,1,8),_UniAutoNegotiationAdvertisedTechAbility_Type())
uniAutoNegotiationAdvertisedTechAbility.setMaxAccess(_B)
if mibBuilder.loadTexts:uniAutoNegotiationAdvertisedTechAbility.setStatus(_A)
class _UniMacAddrClearByPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('clearDynamic',1))
_UniMacAddrClearByPort_Type.__name__=_F
_UniMacAddrClearByPort_Object=MibTableColumn
uniMacAddrClearByPort=_UniMacAddrClearByPort_Object((1,3,6,1,4,1,17409,2,3,5,7,1,9),_UniMacAddrClearByPort_Type())
uniMacAddrClearByPort.setMaxAccess(_B)
if mibBuilder.loadTexts:uniMacAddrClearByPort.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'uniAttributeTable':uniAttributeTable,'uniAttributeEntry':uniAttributeEntry,_M:uniAttributeDeviceIndex,_N:uniAttributeCardIndex,_O:uniAttributePortIndex,'uniAdminStatus':uniAdminStatus,'uniOperationStatus':uniOperationStatus,'uniAutoNegotiationEnable':uniAutoNegotiationEnable,'uniAutoNegotiationLocalTechAbility':uniAutoNegotiationLocalTechAbility,'uniAutoNegotiationRestart':uniAutoNegotiationRestart,'uniMacAddressManagement':uniMacAddressManagement,'uniMacAddressManagementNode':uniMacAddressManagementNode,'uniMacAddrAgingTime':uniMacAddrAgingTime,'uniMacAddrClear':uniMacAddrClear,'uniMacAddressTable':uniMacAddressTable,'uniMacAddressEntry':uniMacAddressEntry,_P:uniMacAddrIndex,_Q:uniMacAddrVlanIdIndex,'uniMacAddrType':uniMacAddrType,'uniMacAddrPortId':uniMacAddrPortId,'uniMacAddrRowStatus':uniMacAddrRowStatus,'uniTrunkManagement':uniTrunkManagement,'uniTrunkGroupConfigTable':uniTrunkGroupConfigTable,'uniTrunkGroupConfigEntry':uniTrunkGroupConfigEntry,_R:uniTrunkGroupConfigIndex,'uniTrunkGroupConfigName':uniTrunkGroupConfigName,'uniTrunkGroupConfigMember':uniTrunkGroupConfigMember,'uniTrunkGroupConfigPolicy':uniTrunkGroupConfigPolicy,'uniTrunkGroupConfigRowstatus':uniTrunkGroupConfigRowstatus,'uniTrunkGroupTable':uniTrunkGroupTable,'uniTrunkGroupEntry':uniTrunkGroupEntry,_S:uniTrunkGroupIndex,'uniTrunkGroupOperationStatus':uniTrunkGroupOperationStatus,'uniTrunkGroupActualSpeed':uniTrunkGroupActualSpeed,'uniTrunkGroupAdminStatus':uniTrunkGroupAdminStatus,'uniPortRateLimitTable':uniPortRateLimitTable,'uniPortRateLimitEntry':uniPortRateLimitEntry,_T:uniPortRateLimitDeviceIndex,_U:uniPortRateLimitCardIndex,_V:uniPortRateLimitPortIndex,'uniPortInCIR':uniPortInCIR,'uniPortInCBS':uniPortInCBS,'uniPortInEBS':uniPortInEBS,'uniPortOutCIR':uniPortOutCIR,'uniPortOutPIR':uniPortOutPIR,'uniPortInRateLimitEnable':uniPortInRateLimitEnable,'uniPortOutRateLimitEnable':uniPortOutRateLimitEnable,'uniMirrorTable':uniMirrorTable,'uniMirrorEntry':uniMirrorEntry,_X:uniMirrorGroupIndex,'uniMirrorGroupName':uniMirrorGroupName,'uniMirrorGroupDstPortList':uniMirrorGroupDstPortList,'uniMirrorGroupSrcInPortList':uniMirrorGroupSrcInPortList,'uniMirrorGroupSrcOutPortList':uniMirrorGroupSrcOutPortList,'uniMirrorGroupRowstatus':uniMirrorGroupRowstatus,'uniBroadcastStormSuppressionTable':uniBroadcastStormSuppressionTable,'uniBroadcastStormSuppressionEntry':uniBroadcastStormSuppressionEntry,_Y:uniBroadcastStormSuppressionCardIndex,_Z:uniBroadcastStormSuppressionPortIndex,'uniUnicastStormEnable':uniUnicastStormEnable,'uniUnicastStormInPacketRate':uniUnicastStormInPacketRate,'uniUnicastStormOutPacketRate':uniUnicastStormOutPacketRate,'uniMulticastStormEnable':uniMulticastStormEnable,'uniMulticastStormInPacketRate':uniMulticastStormInPacketRate,'uniMulticastStormOutPacketRate':uniMulticastStormOutPacketRate,'uniBroadcastStormEnable':uniBroadcastStormEnable,'uniBroadcastStormInPacketRate':uniBroadcastStormInPacketRate,'uniBroadcastStormOutPacketRate':uniBroadcastStormOutPacketRate,'uniExtAttributeTable':uniExtAttributeTable,'uniExtAttributeEntry':uniExtAttributeEntry,_a:uniExtAttributeCardIndex,_b:uniExtAttributePortIndex,'uniPerfStats15minuteEnable':uniPerfStats15minuteEnable,'uniPerfStats24hourEnable':uniPerfStats24hourEnable,'uniLastChangeTime':uniLastChangeTime,'uniIsolationEnable':uniIsolationEnable,'uniMacAddrLearnMaxNum':uniMacAddrLearnMaxNum,'uniAutoNegotiationAdvertisedTechAbility':uniAutoNegotiationAdvertisedTechAbility,'uniMacAddrClearByPort':uniMacAddrClearByPort})