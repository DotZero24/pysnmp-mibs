_d='sniBroadcastStormSuppressionPortIndex'
_c='sniBroadcastStormSuppressionCardIndex'
_b='sniBroadcastStormSuppressionDeviceIndex'
_a='sniMacAddrVlanIdIndex'
_Z='sniMacAddrIndex'
_Y='sniMacAddressManagementDeviceIndex'
_X='sniMirrorGroupIndex'
_W='sniTrunkGroupIndex'
_V='sniTrunkGroupConfigIndex'
_U='full-10000'
_T='full-1000'
_S='full-100'
_R='half-100'
_Q='full-10'
_P='half-10'
_O='auto-negotiate'
_N='sniAttributePortIndex'
_M='sniAttributeCardIndex'
_L='sniAttributeDeviceIndex'
_K='testing'
_J='down'
_I='up'
_H='pps'
_G='read-only'
_F='Integer32'
_E='read-create'
_D='not-accessible'
_C='NSCRTV-EPON-SNI-MIB'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
AutoNegotiationTechAbility,EponAlarmCode,EponAlarmInstance,EponCardIndex,EponDeviceIndex,EponPortIndex,EponSeverityType,EponStats15MinRecordType,EponStats24HourRecordType,EponStatsThresholdType,TAddress,sniObjects=mibBuilder.importSymbols('NSCRTV-EPONEOC-EPON-MIB','AutoNegotiationTechAbility','EponAlarmCode','EponAlarmInstance','EponCardIndex','EponDeviceIndex','EponPortIndex','EponSeverityType','EponStats15MinRecordType','EponStats24HourRecordType','EponStatsThresholdType','TAddress','sniObjects')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TimeStamp','TruthValue')
_SniAttributeTable_Object=MibTable
sniAttributeTable=_SniAttributeTable_Object((1,3,6,1,4,1,17409,2,3,2,1))
if mibBuilder.loadTexts:sniAttributeTable.setStatus(_A)
_SniAttributeEntry_Object=MibTableRow
sniAttributeEntry=_SniAttributeEntry_Object((1,3,6,1,4,1,17409,2,3,2,1,1))
sniAttributeEntry.setIndexNames((0,_C,_L),(0,_C,_M),(0,_C,_N))
if mibBuilder.loadTexts:sniAttributeEntry.setStatus(_A)
_SniAttributeDeviceIndex_Type=Integer32
_SniAttributeDeviceIndex_Object=MibTableColumn
sniAttributeDeviceIndex=_SniAttributeDeviceIndex_Object((1,3,6,1,4,1,17409,2,3,2,1,1,1),_SniAttributeDeviceIndex_Type())
sniAttributeDeviceIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:sniAttributeDeviceIndex.setStatus(_A)
_SniAttributeCardIndex_Type=EponCardIndex
_SniAttributeCardIndex_Object=MibTableColumn
sniAttributeCardIndex=_SniAttributeCardIndex_Object((1,3,6,1,4,1,17409,2,3,2,1,1,2),_SniAttributeCardIndex_Type())
sniAttributeCardIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:sniAttributeCardIndex.setStatus(_A)
_SniAttributePortIndex_Type=EponPortIndex
_SniAttributePortIndex_Object=MibTableColumn
sniAttributePortIndex=_SniAttributePortIndex_Object((1,3,6,1,4,1,17409,2,3,2,1,1,3),_SniAttributePortIndex_Type())
sniAttributePortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:sniAttributePortIndex.setStatus(_A)
_SniPortName_Type=DisplayString
_SniPortName_Object=MibTableColumn
sniPortName=_SniPortName_Object((1,3,6,1,4,1,17409,2,3,2,1,1,4),_SniPortName_Type())
sniPortName.setMaxAccess(_B)
if mibBuilder.loadTexts:sniPortName.setStatus(_A)
class _SniAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),(_J,2),(_K,3)))
_SniAdminStatus_Type.__name__=_F
_SniAdminStatus_Object=MibTableColumn
sniAdminStatus=_SniAdminStatus_Object((1,3,6,1,4,1,17409,2,3,2,1,1,5),_SniAdminStatus_Type())
sniAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sniAdminStatus.setStatus(_A)
class _SniOperationStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),(_J,2),(_K,3)))
_SniOperationStatus_Type.__name__=_F
_SniOperationStatus_Object=MibTableColumn
sniOperationStatus=_SniOperationStatus_Object((1,3,6,1,4,1,17409,2,3,2,1,1,6),_SniOperationStatus_Type())
sniOperationStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:sniOperationStatus.setStatus(_A)
class _SniMediaType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('twistedPair',1),('fiber',2),('other',3)))
_SniMediaType_Type.__name__=_F
_SniMediaType_Object=MibTableColumn
sniMediaType=_SniMediaType_Object((1,3,6,1,4,1,17409,2,3,2,1,1,7),_SniMediaType_Type())
sniMediaType.setMaxAccess(_G)
if mibBuilder.loadTexts:sniMediaType.setStatus(_A)
class _SniAutoNegotiationStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_O,1),(_P,2),(_Q,3),(_R,4),(_S,5),(_T,6),(_U,7),('unknown',8)))
_SniAutoNegotiationStatus_Type.__name__=_F
_SniAutoNegotiationStatus_Object=MibTableColumn
sniAutoNegotiationStatus=_SniAutoNegotiationStatus_Object((1,3,6,1,4,1,17409,2,3,2,1,1,8),_SniAutoNegotiationStatus_Type())
sniAutoNegotiationStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:sniAutoNegotiationStatus.setStatus(_A)
class _SniAutoNegotiationMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_O,1),(_P,2),(_Q,3),(_R,4),(_S,5),(_T,6),(_U,7)))
_SniAutoNegotiationMode_Type.__name__=_F
_SniAutoNegotiationMode_Object=MibTableColumn
sniAutoNegotiationMode=_SniAutoNegotiationMode_Object((1,3,6,1,4,1,17409,2,3,2,1,1,9),_SniAutoNegotiationMode_Type())
sniAutoNegotiationMode.setMaxAccess(_B)
if mibBuilder.loadTexts:sniAutoNegotiationMode.setStatus(_A)
_SniPerfStats15minuteEnable_Type=TruthValue
_SniPerfStats15minuteEnable_Object=MibTableColumn
sniPerfStats15minuteEnable=_SniPerfStats15minuteEnable_Object((1,3,6,1,4,1,17409,2,3,2,1,1,10),_SniPerfStats15minuteEnable_Type())
sniPerfStats15minuteEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:sniPerfStats15minuteEnable.setStatus(_A)
_SniPerfStats24hourEnable_Type=TruthValue
_SniPerfStats24hourEnable_Object=MibTableColumn
sniPerfStats24hourEnable=_SniPerfStats24hourEnable_Object((1,3,6,1,4,1,17409,2,3,2,1,1,11),_SniPerfStats24hourEnable_Type())
sniPerfStats24hourEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:sniPerfStats24hourEnable.setStatus(_A)
_SniLastStatusChangeTime_Type=TimeTicks
_SniLastStatusChangeTime_Object=MibTableColumn
sniLastStatusChangeTime=_SniLastStatusChangeTime_Object((1,3,6,1,4,1,17409,2,3,2,1,1,12),_SniLastStatusChangeTime_Type())
sniLastStatusChangeTime.setMaxAccess(_G)
if mibBuilder.loadTexts:sniLastStatusChangeTime.setStatus(_A)
_SniMacAddrLearnMaxNum_Type=Integer32
_SniMacAddrLearnMaxNum_Object=MibTableColumn
sniMacAddrLearnMaxNum=_SniMacAddrLearnMaxNum_Object((1,3,6,1,4,1,17409,2,3,2,1,1,13),_SniMacAddrLearnMaxNum_Type())
sniMacAddrLearnMaxNum.setMaxAccess(_B)
if mibBuilder.loadTexts:sniMacAddrLearnMaxNum.setStatus(_A)
_SniIsolationEnable_Type=TruthValue
_SniIsolationEnable_Object=MibTableColumn
sniIsolationEnable=_SniIsolationEnable_Object((1,3,6,1,4,1,17409,2,3,2,1,1,14),_SniIsolationEnable_Type())
sniIsolationEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:sniIsolationEnable.setStatus(_A)
_SniTrunkManagement_ObjectIdentity=ObjectIdentity
sniTrunkManagement=_SniTrunkManagement_ObjectIdentity((1,3,6,1,4,1,17409,2,3,2,2))
if mibBuilder.loadTexts:sniTrunkManagement.setStatus(_A)
_SniTrunkGroupConfigTable_Object=MibTable
sniTrunkGroupConfigTable=_SniTrunkGroupConfigTable_Object((1,3,6,1,4,1,17409,2,3,2,2,1))
if mibBuilder.loadTexts:sniTrunkGroupConfigTable.setStatus(_A)
_SniTrunkGroupConfigEntry_Object=MibTableRow
sniTrunkGroupConfigEntry=_SniTrunkGroupConfigEntry_Object((1,3,6,1,4,1,17409,2,3,2,2,1,1))
sniTrunkGroupConfigEntry.setIndexNames((0,_C,_V))
if mibBuilder.loadTexts:sniTrunkGroupConfigEntry.setStatus(_A)
_SniTrunkGroupConfigIndex_Type=Integer32
_SniTrunkGroupConfigIndex_Object=MibTableColumn
sniTrunkGroupConfigIndex=_SniTrunkGroupConfigIndex_Object((1,3,6,1,4,1,17409,2,3,2,2,1,1,1),_SniTrunkGroupConfigIndex_Type())
sniTrunkGroupConfigIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:sniTrunkGroupConfigIndex.setStatus(_A)
_SniTrunkGroupConfigName_Type=DisplayString
_SniTrunkGroupConfigName_Object=MibTableColumn
sniTrunkGroupConfigName=_SniTrunkGroupConfigName_Object((1,3,6,1,4,1,17409,2,3,2,2,1,1,2),_SniTrunkGroupConfigName_Type())
sniTrunkGroupConfigName.setMaxAccess(_E)
if mibBuilder.loadTexts:sniTrunkGroupConfigName.setStatus(_A)
_SniTrunkGroupConfigMember_Type=OctetString
_SniTrunkGroupConfigMember_Object=MibTableColumn
sniTrunkGroupConfigMember=_SniTrunkGroupConfigMember_Object((1,3,6,1,4,1,17409,2,3,2,2,1,1,3),_SniTrunkGroupConfigMember_Type())
sniTrunkGroupConfigMember.setMaxAccess(_E)
if mibBuilder.loadTexts:sniTrunkGroupConfigMember.setStatus(_A)
class _SniTrunkGroupConfigPolicy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('srcMac',1),('destMac',2),('srcMacNDestMac',3),('srcIp',4),('destIp',5),('srcIpNDestIp',6)))
_SniTrunkGroupConfigPolicy_Type.__name__=_F
_SniTrunkGroupConfigPolicy_Object=MibTableColumn
sniTrunkGroupConfigPolicy=_SniTrunkGroupConfigPolicy_Object((1,3,6,1,4,1,17409,2,3,2,2,1,1,4),_SniTrunkGroupConfigPolicy_Type())
sniTrunkGroupConfigPolicy.setMaxAccess(_E)
if mibBuilder.loadTexts:sniTrunkGroupConfigPolicy.setStatus(_A)
_SniTrunkGroupConfigRowstatus_Type=RowStatus
_SniTrunkGroupConfigRowstatus_Object=MibTableColumn
sniTrunkGroupConfigRowstatus=_SniTrunkGroupConfigRowstatus_Object((1,3,6,1,4,1,17409,2,3,2,2,1,1,5),_SniTrunkGroupConfigRowstatus_Type())
sniTrunkGroupConfigRowstatus.setMaxAccess(_E)
if mibBuilder.loadTexts:sniTrunkGroupConfigRowstatus.setStatus(_A)
_SniTrunkGroupTable_Object=MibTable
sniTrunkGroupTable=_SniTrunkGroupTable_Object((1,3,6,1,4,1,17409,2,3,2,2,2))
if mibBuilder.loadTexts:sniTrunkGroupTable.setStatus(_A)
_SniTrunkGroupEntry_Object=MibTableRow
sniTrunkGroupEntry=_SniTrunkGroupEntry_Object((1,3,6,1,4,1,17409,2,3,2,2,2,1))
sniTrunkGroupEntry.setIndexNames((0,_C,_W))
if mibBuilder.loadTexts:sniTrunkGroupEntry.setStatus(_A)
_SniTrunkGroupIndex_Type=Integer32
_SniTrunkGroupIndex_Object=MibTableColumn
sniTrunkGroupIndex=_SniTrunkGroupIndex_Object((1,3,6,1,4,1,17409,2,3,2,2,2,1,1),_SniTrunkGroupIndex_Type())
sniTrunkGroupIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:sniTrunkGroupIndex.setStatus(_A)
class _SniTrunkGroupOperationStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),(_J,2),(_K,3)))
_SniTrunkGroupOperationStatus_Type.__name__=_F
_SniTrunkGroupOperationStatus_Object=MibTableColumn
sniTrunkGroupOperationStatus=_SniTrunkGroupOperationStatus_Object((1,3,6,1,4,1,17409,2,3,2,2,2,1,2),_SniTrunkGroupOperationStatus_Type())
sniTrunkGroupOperationStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:sniTrunkGroupOperationStatus.setStatus(_A)
_SniTrunkGroupActualSpeed_Type=Integer32
_SniTrunkGroupActualSpeed_Object=MibTableColumn
sniTrunkGroupActualSpeed=_SniTrunkGroupActualSpeed_Object((1,3,6,1,4,1,17409,2,3,2,2,2,1,3),_SniTrunkGroupActualSpeed_Type())
sniTrunkGroupActualSpeed.setMaxAccess(_G)
if mibBuilder.loadTexts:sniTrunkGroupActualSpeed.setStatus(_A)
if mibBuilder.loadTexts:sniTrunkGroupActualSpeed.setUnits('Mbps')
class _SniTrunkGroupAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),(_J,2),(_K,3)))
_SniTrunkGroupAdminStatus_Type.__name__=_F
_SniTrunkGroupAdminStatus_Object=MibTableColumn
sniTrunkGroupAdminStatus=_SniTrunkGroupAdminStatus_Object((1,3,6,1,4,1,17409,2,3,2,2,2,1,4),_SniTrunkGroupAdminStatus_Type())
sniTrunkGroupAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sniTrunkGroupAdminStatus.setStatus(_A)
_SniMirrorTable_Object=MibTable
sniMirrorTable=_SniMirrorTable_Object((1,3,6,1,4,1,17409,2,3,2,3))
if mibBuilder.loadTexts:sniMirrorTable.setStatus(_A)
_SniMirrorEntry_Object=MibTableRow
sniMirrorEntry=_SniMirrorEntry_Object((1,3,6,1,4,1,17409,2,3,2,3,1))
sniMirrorEntry.setIndexNames((0,_C,_X))
if mibBuilder.loadTexts:sniMirrorEntry.setStatus(_A)
_SniMirrorGroupIndex_Type=Integer32
_SniMirrorGroupIndex_Object=MibTableColumn
sniMirrorGroupIndex=_SniMirrorGroupIndex_Object((1,3,6,1,4,1,17409,2,3,2,3,1,1),_SniMirrorGroupIndex_Type())
sniMirrorGroupIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:sniMirrorGroupIndex.setStatus(_A)
_SniMirrorGroupName_Type=DisplayString
_SniMirrorGroupName_Object=MibTableColumn
sniMirrorGroupName=_SniMirrorGroupName_Object((1,3,6,1,4,1,17409,2,3,2,3,1,2),_SniMirrorGroupName_Type())
sniMirrorGroupName.setMaxAccess(_E)
if mibBuilder.loadTexts:sniMirrorGroupName.setStatus(_A)
_SniMirrorGroupDstPortList_Type=OctetString
_SniMirrorGroupDstPortList_Object=MibTableColumn
sniMirrorGroupDstPortList=_SniMirrorGroupDstPortList_Object((1,3,6,1,4,1,17409,2,3,2,3,1,3),_SniMirrorGroupDstPortList_Type())
sniMirrorGroupDstPortList.setMaxAccess(_E)
if mibBuilder.loadTexts:sniMirrorGroupDstPortList.setStatus(_A)
_SniMirrorGroupSrcInPortList_Type=OctetString
_SniMirrorGroupSrcInPortList_Object=MibTableColumn
sniMirrorGroupSrcInPortList=_SniMirrorGroupSrcInPortList_Object((1,3,6,1,4,1,17409,2,3,2,3,1,4),_SniMirrorGroupSrcInPortList_Type())
sniMirrorGroupSrcInPortList.setMaxAccess(_E)
if mibBuilder.loadTexts:sniMirrorGroupSrcInPortList.setStatus(_A)
_SniMirrorGroupSrcOutPortList_Type=OctetString
_SniMirrorGroupSrcOutPortList_Object=MibTableColumn
sniMirrorGroupSrcOutPortList=_SniMirrorGroupSrcOutPortList_Object((1,3,6,1,4,1,17409,2,3,2,3,1,5),_SniMirrorGroupSrcOutPortList_Type())
sniMirrorGroupSrcOutPortList.setMaxAccess(_E)
if mibBuilder.loadTexts:sniMirrorGroupSrcOutPortList.setStatus(_A)
_SniMirrorGroupRowstatus_Type=RowStatus
_SniMirrorGroupRowstatus_Object=MibTableColumn
sniMirrorGroupRowstatus=_SniMirrorGroupRowstatus_Object((1,3,6,1,4,1,17409,2,3,2,3,1,6),_SniMirrorGroupRowstatus_Type())
sniMirrorGroupRowstatus.setMaxAccess(_E)
if mibBuilder.loadTexts:sniMirrorGroupRowstatus.setStatus(_A)
_SniMacAddressManagement_ObjectIdentity=ObjectIdentity
sniMacAddressManagement=_SniMacAddressManagement_ObjectIdentity((1,3,6,1,4,1,17409,2,3,2,4))
if mibBuilder.loadTexts:sniMacAddressManagement.setStatus(_A)
_SniMacAddressManagementTable_Object=MibTable
sniMacAddressManagementTable=_SniMacAddressManagementTable_Object((1,3,6,1,4,1,17409,2,3,2,4,1))
if mibBuilder.loadTexts:sniMacAddressManagementTable.setStatus(_A)
_SniMacAddressManagementEntry_Object=MibTableRow
sniMacAddressManagementEntry=_SniMacAddressManagementEntry_Object((1,3,6,1,4,1,17409,2,3,2,4,1,1))
sniMacAddressManagementEntry.setIndexNames((0,_C,_Y))
if mibBuilder.loadTexts:sniMacAddressManagementEntry.setStatus(_A)
_SniMacAddressManagementDeviceIndex_Type=Integer32
_SniMacAddressManagementDeviceIndex_Object=MibTableColumn
sniMacAddressManagementDeviceIndex=_SniMacAddressManagementDeviceIndex_Object((1,3,6,1,4,1,17409,2,3,2,4,1,1,1),_SniMacAddressManagementDeviceIndex_Type())
sniMacAddressManagementDeviceIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:sniMacAddressManagementDeviceIndex.setStatus(_A)
_SniMacAddrTableAgingTime_Type=Integer32
_SniMacAddrTableAgingTime_Object=MibTableColumn
sniMacAddrTableAgingTime=_SniMacAddrTableAgingTime_Object((1,3,6,1,4,1,17409,2,3,2,4,1,1,2),_SniMacAddrTableAgingTime_Type())
sniMacAddrTableAgingTime.setMaxAccess(_B)
if mibBuilder.loadTexts:sniMacAddrTableAgingTime.setStatus(_A)
if mibBuilder.loadTexts:sniMacAddrTableAgingTime.setUnits('Seconds')
class _SniMacAddrTableClear_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('allDynamic',1))
_SniMacAddrTableClear_Type.__name__=_F
_SniMacAddrTableClear_Object=MibTableColumn
sniMacAddrTableClear=_SniMacAddrTableClear_Object((1,3,6,1,4,1,17409,2,3,2,4,1,1,3),_SniMacAddrTableClear_Type())
sniMacAddrTableClear.setMaxAccess(_B)
if mibBuilder.loadTexts:sniMacAddrTableClear.setStatus(_A)
_SniMacAddressTable_Object=MibTable
sniMacAddressTable=_SniMacAddressTable_Object((1,3,6,1,4,1,17409,2,3,2,4,2))
if mibBuilder.loadTexts:sniMacAddressTable.setStatus(_A)
_SniMacAddressEntry_Object=MibTableRow
sniMacAddressEntry=_SniMacAddressEntry_Object((1,3,6,1,4,1,17409,2,3,2,4,2,1))
sniMacAddressEntry.setIndexNames((0,_C,_Z),(0,_C,_a))
if mibBuilder.loadTexts:sniMacAddressEntry.setStatus(_A)
_SniMacAddrIndex_Type=MacAddress
_SniMacAddrIndex_Object=MibTableColumn
sniMacAddrIndex=_SniMacAddrIndex_Object((1,3,6,1,4,1,17409,2,3,2,4,2,1,1),_SniMacAddrIndex_Type())
sniMacAddrIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:sniMacAddrIndex.setStatus(_A)
_SniMacAddrVlanIdIndex_Type=Integer32
_SniMacAddrVlanIdIndex_Object=MibTableColumn
sniMacAddrVlanIdIndex=_SniMacAddrVlanIdIndex_Object((1,3,6,1,4,1,17409,2,3,2,4,2,1,2),_SniMacAddrVlanIdIndex_Type())
sniMacAddrVlanIdIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:sniMacAddrVlanIdIndex.setStatus(_A)
class _SniMacAddrType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('static',1),('dynamic',2),('other',3)))
_SniMacAddrType_Type.__name__=_F
_SniMacAddrType_Object=MibTableColumn
sniMacAddrType=_SniMacAddrType_Object((1,3,6,1,4,1,17409,2,3,2,4,2,1,3),_SniMacAddrType_Type())
sniMacAddrType.setMaxAccess(_E)
if mibBuilder.loadTexts:sniMacAddrType.setStatus(_A)
_SniMacAddrPortId_Type=EponDeviceIndex
_SniMacAddrPortId_Object=MibTableColumn
sniMacAddrPortId=_SniMacAddrPortId_Object((1,3,6,1,4,1,17409,2,3,2,4,2,1,4),_SniMacAddrPortId_Type())
sniMacAddrPortId.setMaxAccess(_E)
if mibBuilder.loadTexts:sniMacAddrPortId.setStatus(_A)
_SniMacAddrRowStatus_Type=RowStatus
_SniMacAddrRowStatus_Object=MibTableColumn
sniMacAddrRowStatus=_SniMacAddrRowStatus_Object((1,3,6,1,4,1,17409,2,3,2,4,2,1,5),_SniMacAddrRowStatus_Type())
sniMacAddrRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:sniMacAddrRowStatus.setStatus(_A)
_SniBroadcastStormSuppressionTable_Object=MibTable
sniBroadcastStormSuppressionTable=_SniBroadcastStormSuppressionTable_Object((1,3,6,1,4,1,17409,2,3,2,5))
if mibBuilder.loadTexts:sniBroadcastStormSuppressionTable.setStatus(_A)
_SniBroadcastStormSuppressionEntry_Object=MibTableRow
sniBroadcastStormSuppressionEntry=_SniBroadcastStormSuppressionEntry_Object((1,3,6,1,4,1,17409,2,3,2,5,1))
sniBroadcastStormSuppressionEntry.setIndexNames((0,_C,_b),(0,_C,_c),(0,_C,_d))
if mibBuilder.loadTexts:sniBroadcastStormSuppressionEntry.setStatus(_A)
_SniBroadcastStormSuppressionDeviceIndex_Type=Integer32
_SniBroadcastStormSuppressionDeviceIndex_Object=MibTableColumn
sniBroadcastStormSuppressionDeviceIndex=_SniBroadcastStormSuppressionDeviceIndex_Object((1,3,6,1,4,1,17409,2,3,2,5,1,1),_SniBroadcastStormSuppressionDeviceIndex_Type())
sniBroadcastStormSuppressionDeviceIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:sniBroadcastStormSuppressionDeviceIndex.setStatus(_A)
_SniBroadcastStormSuppressionCardIndex_Type=EponCardIndex
_SniBroadcastStormSuppressionCardIndex_Object=MibTableColumn
sniBroadcastStormSuppressionCardIndex=_SniBroadcastStormSuppressionCardIndex_Object((1,3,6,1,4,1,17409,2,3,2,5,1,2),_SniBroadcastStormSuppressionCardIndex_Type())
sniBroadcastStormSuppressionCardIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:sniBroadcastStormSuppressionCardIndex.setStatus(_A)
_SniBroadcastStormSuppressionPortIndex_Type=EponPortIndex
_SniBroadcastStormSuppressionPortIndex_Object=MibTableColumn
sniBroadcastStormSuppressionPortIndex=_SniBroadcastStormSuppressionPortIndex_Object((1,3,6,1,4,1,17409,2,3,2,5,1,3),_SniBroadcastStormSuppressionPortIndex_Type())
sniBroadcastStormSuppressionPortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:sniBroadcastStormSuppressionPortIndex.setStatus(_A)
_SniUnicastStormEnable_Type=TruthValue
_SniUnicastStormEnable_Object=MibTableColumn
sniUnicastStormEnable=_SniUnicastStormEnable_Object((1,3,6,1,4,1,17409,2,3,2,5,1,4),_SniUnicastStormEnable_Type())
sniUnicastStormEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:sniUnicastStormEnable.setStatus(_A)
_SniUnicastStormInPacketRate_Type=Integer32
_SniUnicastStormInPacketRate_Object=MibTableColumn
sniUnicastStormInPacketRate=_SniUnicastStormInPacketRate_Object((1,3,6,1,4,1,17409,2,3,2,5,1,5),_SniUnicastStormInPacketRate_Type())
sniUnicastStormInPacketRate.setMaxAccess(_B)
if mibBuilder.loadTexts:sniUnicastStormInPacketRate.setStatus(_A)
if mibBuilder.loadTexts:sniUnicastStormInPacketRate.setUnits(_H)
_SniUnicastStormOutPacketRate_Type=Integer32
_SniUnicastStormOutPacketRate_Object=MibTableColumn
sniUnicastStormOutPacketRate=_SniUnicastStormOutPacketRate_Object((1,3,6,1,4,1,17409,2,3,2,5,1,6),_SniUnicastStormOutPacketRate_Type())
sniUnicastStormOutPacketRate.setMaxAccess(_B)
if mibBuilder.loadTexts:sniUnicastStormOutPacketRate.setStatus(_A)
if mibBuilder.loadTexts:sniUnicastStormOutPacketRate.setUnits(_H)
_SniMulticastStormEnable_Type=TruthValue
_SniMulticastStormEnable_Object=MibTableColumn
sniMulticastStormEnable=_SniMulticastStormEnable_Object((1,3,6,1,4,1,17409,2,3,2,5,1,7),_SniMulticastStormEnable_Type())
sniMulticastStormEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:sniMulticastStormEnable.setStatus(_A)
_SniMulticastStormInPacketRate_Type=Integer32
_SniMulticastStormInPacketRate_Object=MibTableColumn
sniMulticastStormInPacketRate=_SniMulticastStormInPacketRate_Object((1,3,6,1,4,1,17409,2,3,2,5,1,8),_SniMulticastStormInPacketRate_Type())
sniMulticastStormInPacketRate.setMaxAccess(_B)
if mibBuilder.loadTexts:sniMulticastStormInPacketRate.setStatus(_A)
if mibBuilder.loadTexts:sniMulticastStormInPacketRate.setUnits(_H)
_SniMulticastStormOutPacketRate_Type=Integer32
_SniMulticastStormOutPacketRate_Object=MibTableColumn
sniMulticastStormOutPacketRate=_SniMulticastStormOutPacketRate_Object((1,3,6,1,4,1,17409,2,3,2,5,1,9),_SniMulticastStormOutPacketRate_Type())
sniMulticastStormOutPacketRate.setMaxAccess(_B)
if mibBuilder.loadTexts:sniMulticastStormOutPacketRate.setStatus(_A)
if mibBuilder.loadTexts:sniMulticastStormOutPacketRate.setUnits(_H)
_SniBroadcastStormEnable_Type=TruthValue
_SniBroadcastStormEnable_Object=MibTableColumn
sniBroadcastStormEnable=_SniBroadcastStormEnable_Object((1,3,6,1,4,1,17409,2,3,2,5,1,10),_SniBroadcastStormEnable_Type())
sniBroadcastStormEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:sniBroadcastStormEnable.setStatus(_A)
_SniBroadcastStormInPacketRate_Type=Integer32
_SniBroadcastStormInPacketRate_Object=MibTableColumn
sniBroadcastStormInPacketRate=_SniBroadcastStormInPacketRate_Object((1,3,6,1,4,1,17409,2,3,2,5,1,11),_SniBroadcastStormInPacketRate_Type())
sniBroadcastStormInPacketRate.setMaxAccess(_B)
if mibBuilder.loadTexts:sniBroadcastStormInPacketRate.setStatus(_A)
if mibBuilder.loadTexts:sniBroadcastStormInPacketRate.setUnits(_H)
_SniBroadcastStormOutPacketRate_Type=Integer32
_SniBroadcastStormOutPacketRate_Object=MibTableColumn
sniBroadcastStormOutPacketRate=_SniBroadcastStormOutPacketRate_Object((1,3,6,1,4,1,17409,2,3,2,5,1,12),_SniBroadcastStormOutPacketRate_Type())
sniBroadcastStormOutPacketRate.setMaxAccess(_B)
if mibBuilder.loadTexts:sniBroadcastStormOutPacketRate.setStatus(_A)
if mibBuilder.loadTexts:sniBroadcastStormOutPacketRate.setUnits(_H)
mibBuilder.exportSymbols(_C,**{'sniAttributeTable':sniAttributeTable,'sniAttributeEntry':sniAttributeEntry,_L:sniAttributeDeviceIndex,_M:sniAttributeCardIndex,_N:sniAttributePortIndex,'sniPortName':sniPortName,'sniAdminStatus':sniAdminStatus,'sniOperationStatus':sniOperationStatus,'sniMediaType':sniMediaType,'sniAutoNegotiationStatus':sniAutoNegotiationStatus,'sniAutoNegotiationMode':sniAutoNegotiationMode,'sniPerfStats15minuteEnable':sniPerfStats15minuteEnable,'sniPerfStats24hourEnable':sniPerfStats24hourEnable,'sniLastStatusChangeTime':sniLastStatusChangeTime,'sniMacAddrLearnMaxNum':sniMacAddrLearnMaxNum,'sniIsolationEnable':sniIsolationEnable,'sniTrunkManagement':sniTrunkManagement,'sniTrunkGroupConfigTable':sniTrunkGroupConfigTable,'sniTrunkGroupConfigEntry':sniTrunkGroupConfigEntry,_V:sniTrunkGroupConfigIndex,'sniTrunkGroupConfigName':sniTrunkGroupConfigName,'sniTrunkGroupConfigMember':sniTrunkGroupConfigMember,'sniTrunkGroupConfigPolicy':sniTrunkGroupConfigPolicy,'sniTrunkGroupConfigRowstatus':sniTrunkGroupConfigRowstatus,'sniTrunkGroupTable':sniTrunkGroupTable,'sniTrunkGroupEntry':sniTrunkGroupEntry,_W:sniTrunkGroupIndex,'sniTrunkGroupOperationStatus':sniTrunkGroupOperationStatus,'sniTrunkGroupActualSpeed':sniTrunkGroupActualSpeed,'sniTrunkGroupAdminStatus':sniTrunkGroupAdminStatus,'sniMirrorTable':sniMirrorTable,'sniMirrorEntry':sniMirrorEntry,_X:sniMirrorGroupIndex,'sniMirrorGroupName':sniMirrorGroupName,'sniMirrorGroupDstPortList':sniMirrorGroupDstPortList,'sniMirrorGroupSrcInPortList':sniMirrorGroupSrcInPortList,'sniMirrorGroupSrcOutPortList':sniMirrorGroupSrcOutPortList,'sniMirrorGroupRowstatus':sniMirrorGroupRowstatus,'sniMacAddressManagement':sniMacAddressManagement,'sniMacAddressManagementTable':sniMacAddressManagementTable,'sniMacAddressManagementEntry':sniMacAddressManagementEntry,_Y:sniMacAddressManagementDeviceIndex,'sniMacAddrTableAgingTime':sniMacAddrTableAgingTime,'sniMacAddrTableClear':sniMacAddrTableClear,'sniMacAddressTable':sniMacAddressTable,'sniMacAddressEntry':sniMacAddressEntry,_Z:sniMacAddrIndex,_a:sniMacAddrVlanIdIndex,'sniMacAddrType':sniMacAddrType,'sniMacAddrPortId':sniMacAddrPortId,'sniMacAddrRowStatus':sniMacAddrRowStatus,'sniBroadcastStormSuppressionTable':sniBroadcastStormSuppressionTable,'sniBroadcastStormSuppressionEntry':sniBroadcastStormSuppressionEntry,_b:sniBroadcastStormSuppressionDeviceIndex,_c:sniBroadcastStormSuppressionCardIndex,_d:sniBroadcastStormSuppressionPortIndex,'sniUnicastStormEnable':sniUnicastStormEnable,'sniUnicastStormInPacketRate':sniUnicastStormInPacketRate,'sniUnicastStormOutPacketRate':sniUnicastStormOutPacketRate,'sniMulticastStormEnable':sniMulticastStormEnable,'sniMulticastStormInPacketRate':sniMulticastStormInPacketRate,'sniMulticastStormOutPacketRate':sniMulticastStormOutPacketRate,'sniBroadcastStormEnable':sniBroadcastStormEnable,'sniBroadcastStormInPacketRate':sniBroadcastStormInPacketRate,'sniBroadcastStormOutPacketRate':sniBroadcastStormOutPacketRate})