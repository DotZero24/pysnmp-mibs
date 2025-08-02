_R='hwvLANMibHoldTimeEntry'
_Q='hwvLANMibSwitchCountEntry'
_P='hwifSuperVlanID'
_O='hwdot1qVlanBatchOperIndex'
_N='hwVlanInterfaceIpAddr'
_M='hwVlanInterfaceIpIfIndex'
_L='hwifIsolatePrimaryVlanID'
_K='hwVlanInterfaceID'
_J='hwdot1qVlanIndex'
_I='TimeInterval'
_H='SnmpAdminString'
_G='read-create'
_F='OctetString'
_E='A3COM-HUAWEI-LswVLAN-MIB'
_D='Integer32'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
PortList,hwifVLANTrunkStatusEntry=mibBuilder.importSymbols('A3COM-HUAWEI-LswINF-MIB','PortList','hwifVLANTrunkStatusEntry')
lswCommon,=mibBuilder.importSymbols('A3COM-HUAWEI-OID-MIB','lswCommon')
ifEntry,=mibBuilder.importSymbols('IF-MIB','ifEntry')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_H)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeInterval,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_I,'TruthValue')
hwLswVlan=ModuleIdentity((1,3,6,1,4,1,43,45,1,2,23,1,2))
class HwVlanIndex(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_HwLswVlanMngObject_ObjectIdentity=ObjectIdentity
hwLswVlanMngObject=_HwLswVlanMngObject_ObjectIdentity((1,3,6,1,4,1,43,45,1,2,23,1,2,1))
if mibBuilder.loadTexts:hwLswVlanMngObject.setStatus(_A)
_Hwdot1qVlanMIBTable_Object=MibTable
hwdot1qVlanMIBTable=_Hwdot1qVlanMIBTable_Object((1,3,6,1,4,1,43,45,1,2,23,1,2,1,1))
if mibBuilder.loadTexts:hwdot1qVlanMIBTable.setStatus(_A)
_Hwdot1qVlanMIBEntry_Object=MibTableRow
hwdot1qVlanMIBEntry=_Hwdot1qVlanMIBEntry_Object((1,3,6,1,4,1,43,45,1,2,23,1,2,1,1,1))
hwdot1qVlanMIBEntry.setIndexNames((0,_E,_J))
if mibBuilder.loadTexts:hwdot1qVlanMIBEntry.setStatus(_A)
_Hwdot1qVlanIndex_Type=HwVlanIndex
_Hwdot1qVlanIndex_Object=MibTableColumn
hwdot1qVlanIndex=_Hwdot1qVlanIndex_Object((1,3,6,1,4,1,43,45,1,2,23,1,2,1,1,1,1),_Hwdot1qVlanIndex_Type())
hwdot1qVlanIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hwdot1qVlanIndex.setStatus(_A)
class _Hwdot1qVlanName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_Hwdot1qVlanName_Type.__name__=_H
_Hwdot1qVlanName_Object=MibTableColumn
hwdot1qVlanName=_Hwdot1qVlanName_Object((1,3,6,1,4,1,43,45,1,2,23,1,2,1,1,1,2),_Hwdot1qVlanName_Type())
hwdot1qVlanName.setMaxAccess(_C)
if mibBuilder.loadTexts:hwdot1qVlanName.setStatus(_A)
_Hwdot1qVlanPorts_Type=PortList
_Hwdot1qVlanPorts_Object=MibTableColumn
hwdot1qVlanPorts=_Hwdot1qVlanPorts_Object((1,3,6,1,4,1,43,45,1,2,23,1,2,1,1,1,3),_Hwdot1qVlanPorts_Type())
hwdot1qVlanPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:hwdot1qVlanPorts.setStatus(_A)
class _Hwdot1qVlanType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('superVlan',1),('common-vlan',2),('sub-vlan',3),('isolate-user-vlan',4),('secondary-vlan',5)))
_Hwdot1qVlanType_Type.__name__=_D
_Hwdot1qVlanType_Object=MibTableColumn
hwdot1qVlanType=_Hwdot1qVlanType_Object((1,3,6,1,4,1,43,45,1,2,23,1,2,1,1,1,4),_Hwdot1qVlanType_Type())
hwdot1qVlanType.setMaxAccess(_C)
if mibBuilder.loadTexts:hwdot1qVlanType.setStatus(_A)
_Hwdot1qVlanMacFilter_Type=TruthValue
_Hwdot1qVlanMacFilter_Object=MibTableColumn
hwdot1qVlanMacFilter=_Hwdot1qVlanMacFilter_Object((1,3,6,1,4,1,43,45,1,2,23,1,2,1,1,1,5),_Hwdot1qVlanMacFilter_Type())
hwdot1qVlanMacFilter.setMaxAccess(_B)
if mibBuilder.loadTexts:hwdot1qVlanMacFilter.setStatus(_A)
_Hwdot1qVlanMcastUnknownProtos_Type=TruthValue
_Hwdot1qVlanMcastUnknownProtos_Object=MibTableColumn
hwdot1qVlanMcastUnknownProtos=_Hwdot1qVlanMcastUnknownProtos_Object((1,3,6,1,4,1,43,45,1,2,23,1,2,1,1,1,6),_Hwdot1qVlanMcastUnknownProtos_Type())
hwdot1qVlanMcastUnknownProtos.setMaxAccess(_B)
if mibBuilder.loadTexts:hwdot1qVlanMcastUnknownProtos.setStatus(_A)
_HwExistInterface_Type=TruthValue
_HwExistInterface_Object=MibTableColumn
hwExistInterface=_HwExistInterface_Object((1,3,6,1,4,1,43,45,1,2,23,1,2,1,1,1,7),_HwExistInterface_Type())
hwExistInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:hwExistInterface.setStatus(_A)
_HwVlanInterfaceIndex_Type=Integer32
_HwVlanInterfaceIndex_Object=MibTableColumn
hwVlanInterfaceIndex=_HwVlanInterfaceIndex_Object((1,3,6,1,4,1,43,45,1,2,23,1,2,1,1,1,8),_HwVlanInterfaceIndex_Type())
hwVlanInterfaceIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVlanInterfaceIndex.setStatus(_A)
_Hwdot1qVlanMacLearn_Type=TruthValue
_Hwdot1qVlanMacLearn_Object=MibTableColumn
hwdot1qVlanMacLearn=_Hwdot1qVlanMacLearn_Object((1,3,6,1,4,1,43,45,1,2,23,1,2,1,1,1,9),_Hwdot1qVlanMacLearn_Type())
hwdot1qVlanMacLearn.setMaxAccess(_B)
if mibBuilder.loadTexts:hwdot1qVlanMacLearn.setStatus(_A)
class _Hwdot1qVlanStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('other',1),('static',2),('dynamic',3)))
_Hwdot1qVlanStatus_Type.__name__=_D
_Hwdot1qVlanStatus_Object=MibTableColumn
hwdot1qVlanStatus=_Hwdot1qVlanStatus_Object((1,3,6,1,4,1,43,45,1,2,23,1,2,1,1,1,10),_Hwdot1qVlanStatus_Type())
hwdot1qVlanStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hwdot1qVlanStatus.setStatus(_A)
_Hwdot1qVlanCreationTime_Type=TimeTicks
_Hwdot1qVlanCreationTime_Object=MibTableColumn
hwdot1qVlanCreationTime=_Hwdot1qVlanCreationTime_Object((1,3,6,1,4,1,43,45,1,2,23,1,2,1,1,1,11),_Hwdot1qVlanCreationTime_Type())
hwdot1qVlanCreationTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hwdot1qVlanCreationTime.setStatus(_A)
class _Hwdot1qVlanPriority_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Hwdot1qVlanPriority_Type.__name__=_D
_Hwdot1qVlanPriority_Object=MibTableColumn
hwdot1qVlanPriority=_Hwdot1qVlanPriority_Object((1,3,6,1,4,1,43,45,1,2,23,1,2,1,1,1,12),_Hwdot1qVlanPriority_Type())
hwdot1qVlanPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:hwdot1qVlanPriority.setStatus(_A)
_Hwdot1qVlanRowStatus_Type=RowStatus
_Hwdot1qVlanRowStatus_Object=MibTableColumn
hwdot1qVlanRowStatus=_Hwdot1qVlanRowStatus_Object((1,3,6,1,4,1,43,45,1,2,23,1,2,1,1,1,13),_Hwdot1qVlanRowStatus_Type())
hwdot1qVlanRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:hwdot1qVlanRowStatus.setStatus(_A)
class _Hwdot1qVlanBroadcastSuppression_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_Hwdot1qVlanBroadcastSuppression_Type.__name__=_D
_Hwdot1qVlanBroadcastSuppression_Object=MibTableColumn
hwdot1qVlanBroadcastSuppression=_Hwdot1qVlanBroadcastSuppression_Object((1,3,6,1,4,1,43,45,1,2,23,1,2,1,1,1,14),_Hwdot1qVlanBroadcastSuppression_Type())
hwdot1qVlanBroadcastSuppression.setMaxAccess(_C)
if mibBuilder.loadTexts:hwdot1qVlanBroadcastSuppression.setStatus(_A)
class _Hwdot1qVlanBcastSuppressionPPS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,148800))
_Hwdot1qVlanBcastSuppressionPPS_Type.__name__=_D
_Hwdot1qVlanBcastSuppressionPPS_Object=MibTableColumn
hwdot1qVlanBcastSuppressionPPS=_Hwdot1qVlanBcastSuppressionPPS_Object((1,3,6,1,4,1,43,45,1,2,23,1,2,1,1,1,15),_Hwdot1qVlanBcastSuppressionPPS_Type())
hwdot1qVlanBcastSuppressionPPS.setMaxAccess(_C)
if mibBuilder.loadTexts:hwdot1qVlanBcastSuppressionPPS.setStatus(_A)
class _Hwdot1qVlanMulticast_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('disable',0),('enable',1)))
_Hwdot1qVlanMulticast_Type.__name__=_D
_Hwdot1qVlanMulticast_Object=MibTableColumn
hwdot1qVlanMulticast=_Hwdot1qVlanMulticast_Object((1,3,6,1,4,1,43,45,1,2,23,1,2,1,1,1,16),_Hwdot1qVlanMulticast_Type())
hwdot1qVlanMulticast.setMaxAccess(_C)
if mibBuilder.loadTexts:hwdot1qVlanMulticast.setStatus(_A)
_Hwdot1qVlanTaggedPorts_Type=PortList
_Hwdot1qVlanTaggedPorts_Object=MibTableColumn
hwdot1qVlanTaggedPorts=_Hwdot1qVlanTaggedPorts_Object((1,3,6,1,4,1,43,45,1,2,23,1,2,1,1,1,17),_Hwdot1qVlanTaggedPorts_Type())
hwdot1qVlanTaggedPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:hwdot1qVlanTaggedPorts.setStatus(_A)
_Hwdot1qVlanUntaggedPorts_Type=PortList
_Hwdot1qVlanUntaggedPorts_Object=MibTableColumn
hwdot1qVlanUntaggedPorts=_Hwdot1qVlanUntaggedPorts_Object((1,3,6,1,4,1,43,45,1,2,23,1,2,1,1,1,18),_Hwdot1qVlanUntaggedPorts_Type())
hwdot1qVlanUntaggedPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:hwdot1qVlanUntaggedPorts.setStatus(_A)
_Hwdot1qVlanPortIndexs_Type=OctetString
_Hwdot1qVlanPortIndexs_Object=MibTableColumn
hwdot1qVlanPortIndexs=_Hwdot1qVlanPortIndexs_Object((1,3,6,1,4,1,43,45,1,2,23,1,2,1,1,1,19),_Hwdot1qVlanPortIndexs_Type())
hwdot1qVlanPortIndexs.setMaxAccess(_C)
if mibBuilder.loadTexts:hwdot1qVlanPortIndexs.setStatus(_A)
_HwVlanInterfaceTable_Object=MibTable
hwVlanInterfaceTable=_HwVlanInterfaceTable_Object((1,3,6,1,4,1,43,45,1,2,23,1,2,1,2))
if mibBuilder.loadTexts:hwVlanInterfaceTable.setStatus(_A)
_HwVlanInterfaceEntry_Object=MibTableRow
hwVlanInterfaceEntry=_HwVlanInterfaceEntry_Object((1,3,6,1,4,1,43,45,1,2,23,1,2,1,2,1))
hwVlanInterfaceEntry.setIndexNames((0,_E,_K))
if mibBuilder.loadTexts:hwVlanInterfaceEntry.setStatus(_A)
_HwVlanInterfaceID_Type=Integer32
_HwVlanInterfaceID_Object=MibTableColumn
hwVlanInterfaceID=_HwVlanInterfaceID_Object((1,3,6,1,4,1,43,45,1,2,23,1,2,1,2,1,1),_HwVlanInterfaceID_Type())
hwVlanInterfaceID.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVlanInterfaceID.setStatus(_A)
_Hwdot1qVlanID_Type=HwVlanIndex
_Hwdot1qVlanID_Object=MibTableColumn
hwdot1qVlanID=_Hwdot1qVlanID_Object((1,3,6,1,4,1,43,45,1,2,23,1,2,1,2,1,2),_Hwdot1qVlanID_Type())
hwdot1qVlanID.setMaxAccess(_B)
if mibBuilder.loadTexts:hwdot1qVlanID.setStatus(_A)
_Hwdot1qVlanIpAddress_Type=IpAddress
_Hwdot1qVlanIpAddress_Object=MibTableColumn
hwdot1qVlanIpAddress=_Hwdot1qVlanIpAddress_Object((1,3,6,1,4,1,43,45,1,2,23,1,2,1,2,1,3),_Hwdot1qVlanIpAddress_Type())
hwdot1qVlanIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:hwdot1qVlanIpAddress.setStatus(_A)
_Hwdot1qVlanIpAddressMask_Type=IpAddress
_Hwdot1qVlanIpAddressMask_Object=MibTableColumn
hwdot1qVlanIpAddressMask=_Hwdot1qVlanIpAddressMask_Object((1,3,6,1,4,1,43,45,1,2,23,1,2,1,2,1,4),_Hwdot1qVlanIpAddressMask_Type())
hwdot1qVlanIpAddressMask.setMaxAccess(_C)
if mibBuilder.loadTexts:hwdot1qVlanIpAddressMask.setStatus(_A)
class _HwVlanInterfaceAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_HwVlanInterfaceAdminStatus_Type.__name__=_D
_HwVlanInterfaceAdminStatus_Object=MibTableColumn
hwVlanInterfaceAdminStatus=_HwVlanInterfaceAdminStatus_Object((1,3,6,1,4,1,43,45,1,2,23,1,2,1,2,1,5),_HwVlanInterfaceAdminStatus_Type())
hwVlanInterfaceAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hwVlanInterfaceAdminStatus.setStatus(_A)
class _HwVlanInterfaceFrameType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('ethernet-ii',1),('ethernet-snap',2),('ethernet-8022',3),('ethernet-8023',4)))
_HwVlanInterfaceFrameType_Type.__name__=_D
_HwVlanInterfaceFrameType_Object=MibTableColumn
hwVlanInterfaceFrameType=_HwVlanInterfaceFrameType_Object((1,3,6,1,4,1,43,45,1,2,23,1,2,1,2,1,6),_HwVlanInterfaceFrameType_Type())
hwVlanInterfaceFrameType.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVlanInterfaceFrameType.setStatus(_A)
_HwInterfaceRowStatus_Type=RowStatus
_HwInterfaceRowStatus_Object=MibTableColumn
hwInterfaceRowStatus=_HwInterfaceRowStatus_Object((1,3,6,1,4,1,43,45,1,2,23,1,2,1,2,1,7),_HwInterfaceRowStatus_Type())
hwInterfaceRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:hwInterfaceRowStatus.setStatus(_A)
class _HwVlanInterfaceIpMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('assigned-ip',1),('dhcp-ip',2),('bootp-ip',3)))
_HwVlanInterfaceIpMethod_Type.__name__=_D
_HwVlanInterfaceIpMethod_Object=MibTableColumn
hwVlanInterfaceIpMethod=_HwVlanInterfaceIpMethod_Object((1,3,6,1,4,1,43,45,1,2,23,1,2,1,2,1,8),_HwVlanInterfaceIpMethod_Type())
hwVlanInterfaceIpMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:hwVlanInterfaceIpMethod.setStatus(_A)
_HwVlanInterfaceIfIndex_Type=Integer32
_HwVlanInterfaceIfIndex_Object=MibTableColumn
hwVlanInterfaceIfIndex=_HwVlanInterfaceIfIndex_Object((1,3,6,1,4,1,43,45,1,2,23,1,2,1,2,1,9),_HwVlanInterfaceIfIndex_Type())
hwVlanInterfaceIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVlanInterfaceIfIndex.setStatus(_A)
_HwifIsolateMappingTable_Object=MibTable
hwifIsolateMappingTable=_HwifIsolateMappingTable_Object((1,3,6,1,4,1,43,45,1,2,23,1,2,1,4))
if mibBuilder.loadTexts:hwifIsolateMappingTable.setStatus(_A)
_HwifIsolateMappingEntry_Object=MibTableRow
hwifIsolateMappingEntry=_HwifIsolateMappingEntry_Object((1,3,6,1,4,1,43,45,1,2,23,1,2,1,4,1))
hwifIsolateMappingEntry.setIndexNames((0,_E,_L))
if mibBuilder.loadTexts:hwifIsolateMappingEntry.setStatus(_A)
_HwifIsolatePrimaryVlanID_Type=HwVlanIndex
_HwifIsolatePrimaryVlanID_Object=MibTableColumn
hwifIsolatePrimaryVlanID=_HwifIsolatePrimaryVlanID_Object((1,3,6,1,4,1,43,45,1,2,23,1,2,1,4,1,1),_HwifIsolatePrimaryVlanID_Type())
hwifIsolatePrimaryVlanID.setMaxAccess(_B)
if mibBuilder.loadTexts:hwifIsolatePrimaryVlanID.setStatus(_A)
class _HwifIsolateSecondaryVlanlistLow_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_HwifIsolateSecondaryVlanlistLow_Type.__name__=_F
_HwifIsolateSecondaryVlanlistLow_Object=MibTableColumn
hwifIsolateSecondaryVlanlistLow=_HwifIsolateSecondaryVlanlistLow_Object((1,3,6,1,4,1,43,45,1,2,23,1,2,1,4,1,2),_HwifIsolateSecondaryVlanlistLow_Type())
hwifIsolateSecondaryVlanlistLow.setMaxAccess(_C)
if mibBuilder.loadTexts:hwifIsolateSecondaryVlanlistLow.setStatus(_A)
class _HwifIsolateSecondaryVlanlistHigh_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_HwifIsolateSecondaryVlanlistHigh_Type.__name__=_F
_HwifIsolateSecondaryVlanlistHigh_Object=MibTableColumn
hwifIsolateSecondaryVlanlistHigh=_HwifIsolateSecondaryVlanlistHigh_Object((1,3,6,1,4,1,43,45,1,2,23,1,2,1,4,1,3),_HwifIsolateSecondaryVlanlistHigh_Type())
hwifIsolateSecondaryVlanlistHigh.setMaxAccess(_C)
if mibBuilder.loadTexts:hwifIsolateSecondaryVlanlistHigh.setStatus(_A)
_HwVlanInterfaceAddrTable_Object=MibTable
hwVlanInterfaceAddrTable=_HwVlanInterfaceAddrTable_Object((1,3,6,1,4,1,43,45,1,2,23,1,2,1,5))
if mibBuilder.loadTexts:hwVlanInterfaceAddrTable.setStatus(_A)
_HwVlanInterfaceAddrEntry_Object=MibTableRow
hwVlanInterfaceAddrEntry=_HwVlanInterfaceAddrEntry_Object((1,3,6,1,4,1,43,45,1,2,23,1,2,1,5,1))
hwVlanInterfaceAddrEntry.setIndexNames((0,_E,_M),(0,_E,_N))
if mibBuilder.loadTexts:hwVlanInterfaceAddrEntry.setStatus(_A)
_HwVlanInterfaceIpIfIndex_Type=Integer32
_HwVlanInterfaceIpIfIndex_Object=MibTableColumn
hwVlanInterfaceIpIfIndex=_HwVlanInterfaceIpIfIndex_Object((1,3,6,1,4,1,43,45,1,2,23,1,2,1,5,1,1),_HwVlanInterfaceIpIfIndex_Type())
hwVlanInterfaceIpIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVlanInterfaceIpIfIndex.setStatus(_A)
_HwVlanInterfaceIpAddr_Type=IpAddress
_HwVlanInterfaceIpAddr_Object=MibTableColumn
hwVlanInterfaceIpAddr=_HwVlanInterfaceIpAddr_Object((1,3,6,1,4,1,43,45,1,2,23,1,2,1,5,1,2),_HwVlanInterfaceIpAddr_Type())
hwVlanInterfaceIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:hwVlanInterfaceIpAddr.setStatus(_A)
_HwVlanInterfaceIpMask_Type=IpAddress
_HwVlanInterfaceIpMask_Object=MibTableColumn
hwVlanInterfaceIpMask=_HwVlanInterfaceIpMask_Object((1,3,6,1,4,1,43,45,1,2,23,1,2,1,5,1,3),_HwVlanInterfaceIpMask_Type())
hwVlanInterfaceIpMask.setMaxAccess(_C)
if mibBuilder.loadTexts:hwVlanInterfaceIpMask.setStatus(_A)
class _HwVlanInterfaceIpType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('primary',1),('sub',2),('cluster',3),('vrrp',4)))
_HwVlanInterfaceIpType_Type.__name__=_D
_HwVlanInterfaceIpType_Object=MibTableColumn
hwVlanInterfaceIpType=_HwVlanInterfaceIpType_Object((1,3,6,1,4,1,43,45,1,2,23,1,2,1,5,1,4),_HwVlanInterfaceIpType_Type())
hwVlanInterfaceIpType.setMaxAccess(_C)
if mibBuilder.loadTexts:hwVlanInterfaceIpType.setStatus(_A)
_HwVlanInterfaceIpRowStatus_Type=RowStatus
_HwVlanInterfaceIpRowStatus_Object=MibTableColumn
hwVlanInterfaceIpRowStatus=_HwVlanInterfaceIpRowStatus_Object((1,3,6,1,4,1,43,45,1,2,23,1,2,1,5,1,5),_HwVlanInterfaceIpRowStatus_Type())
hwVlanInterfaceIpRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:hwVlanInterfaceIpRowStatus.setStatus(_A)
_Hwdot1qVlanBatchMIBTable_Object=MibTable
hwdot1qVlanBatchMIBTable=_Hwdot1qVlanBatchMIBTable_Object((1,3,6,1,4,1,43,45,1,2,23,1,2,1,6))
if mibBuilder.loadTexts:hwdot1qVlanBatchMIBTable.setStatus(_A)
_HwDot1qVlanBatchMIBEntry_Object=MibTableRow
hwDot1qVlanBatchMIBEntry=_HwDot1qVlanBatchMIBEntry_Object((1,3,6,1,4,1,43,45,1,2,23,1,2,1,6,1))
hwDot1qVlanBatchMIBEntry.setIndexNames((0,_E,_O))
if mibBuilder.loadTexts:hwDot1qVlanBatchMIBEntry.setStatus(_A)
_Hwdot1qVlanBatchOperIndex_Type=Integer32
_Hwdot1qVlanBatchOperIndex_Object=MibTableColumn
hwdot1qVlanBatchOperIndex=_Hwdot1qVlanBatchOperIndex_Object((1,3,6,1,4,1,43,45,1,2,23,1,2,1,6,1,1),_Hwdot1qVlanBatchOperIndex_Type())
hwdot1qVlanBatchOperIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hwdot1qVlanBatchOperIndex.setStatus(_A)
_Hwdot1qVlanBatchStartIndex_Type=HwVlanIndex
_Hwdot1qVlanBatchStartIndex_Object=MibTableColumn
hwdot1qVlanBatchStartIndex=_Hwdot1qVlanBatchStartIndex_Object((1,3,6,1,4,1,43,45,1,2,23,1,2,1,6,1,2),_Hwdot1qVlanBatchStartIndex_Type())
hwdot1qVlanBatchStartIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hwdot1qVlanBatchStartIndex.setStatus(_A)
_Hwdot1qVlanBatchEndIndex_Type=HwVlanIndex
_Hwdot1qVlanBatchEndIndex_Object=MibTableColumn
hwdot1qVlanBatchEndIndex=_Hwdot1qVlanBatchEndIndex_Object((1,3,6,1,4,1,43,45,1,2,23,1,2,1,6,1,3),_Hwdot1qVlanBatchEndIndex_Type())
hwdot1qVlanBatchEndIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hwdot1qVlanBatchEndIndex.setStatus(_A)
class _Hwdot1qVlanBatchOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('opInprogress',1),('opfailure',2),('opsuccess',3),('opsuccesspartial',4)))
_Hwdot1qVlanBatchOperStatus_Type.__name__=_D
_Hwdot1qVlanBatchOperStatus_Object=MibTableColumn
hwdot1qVlanBatchOperStatus=_Hwdot1qVlanBatchOperStatus_Object((1,3,6,1,4,1,43,45,1,2,23,1,2,1,6,1,4),_Hwdot1qVlanBatchOperStatus_Type())
hwdot1qVlanBatchOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hwdot1qVlanBatchOperStatus.setStatus(_A)
_Hwdot1qVlanBatchRowStatus_Type=RowStatus
_Hwdot1qVlanBatchRowStatus_Object=MibTableColumn
hwdot1qVlanBatchRowStatus=_Hwdot1qVlanBatchRowStatus_Object((1,3,6,1,4,1,43,45,1,2,23,1,2,1,6,1,5),_Hwdot1qVlanBatchRowStatus_Type())
hwdot1qVlanBatchRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:hwdot1qVlanBatchRowStatus.setStatus(_A)
class _Hwdot1qVlanBatchSetOperate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('create',1),('delete',2)))
_Hwdot1qVlanBatchSetOperate_Type.__name__=_D
_Hwdot1qVlanBatchSetOperate_Object=MibTableColumn
hwdot1qVlanBatchSetOperate=_Hwdot1qVlanBatchSetOperate_Object((1,3,6,1,4,1,43,45,1,2,23,1,2,1,6,1,6),_Hwdot1qVlanBatchSetOperate_Type())
hwdot1qVlanBatchSetOperate.setMaxAccess(_G)
if mibBuilder.loadTexts:hwdot1qVlanBatchSetOperate.setStatus(_A)
_HwifSuperVlanMappingTable_Object=MibTable
hwifSuperVlanMappingTable=_HwifSuperVlanMappingTable_Object((1,3,6,1,4,1,43,45,1,2,23,1,2,1,7))
if mibBuilder.loadTexts:hwifSuperVlanMappingTable.setStatus(_A)
_HwifSuperVlanMappingEntry_Object=MibTableRow
hwifSuperVlanMappingEntry=_HwifSuperVlanMappingEntry_Object((1,3,6,1,4,1,43,45,1,2,23,1,2,1,7,1))
hwifSuperVlanMappingEntry.setIndexNames((0,_E,_P))
if mibBuilder.loadTexts:hwifSuperVlanMappingEntry.setStatus(_A)
_HwifSuperVlanID_Type=HwVlanIndex
_HwifSuperVlanID_Object=MibTableColumn
hwifSuperVlanID=_HwifSuperVlanID_Object((1,3,6,1,4,1,43,45,1,2,23,1,2,1,7,1,1),_HwifSuperVlanID_Type())
hwifSuperVlanID.setMaxAccess(_B)
if mibBuilder.loadTexts:hwifSuperVlanID.setStatus(_A)
class _HwifSubVlanlistLow_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_HwifSubVlanlistLow_Type.__name__=_F
_HwifSubVlanlistLow_Object=MibTableColumn
hwifSubVlanlistLow=_HwifSubVlanlistLow_Object((1,3,6,1,4,1,43,45,1,2,23,1,2,1,7,1,2),_HwifSubVlanlistLow_Type())
hwifSubVlanlistLow.setMaxAccess(_C)
if mibBuilder.loadTexts:hwifSubVlanlistLow.setStatus(_A)
class _HwifSubVlanlistHigh_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_HwifSubVlanlistHigh_Type.__name__=_F
_HwifSubVlanlistHigh_Object=MibTableColumn
hwifSubVlanlistHigh=_HwifSubVlanlistHigh_Object((1,3,6,1,4,1,43,45,1,2,23,1,2,1,7,1,3),_HwifSubVlanlistHigh_Type())
hwifSubVlanlistHigh.setMaxAccess(_C)
if mibBuilder.loadTexts:hwifSubVlanlistHigh.setStatus(_A)
_HwLswVlanProtoObject_ObjectIdentity=ObjectIdentity
hwLswVlanProtoObject=_HwLswVlanProtoObject_ObjectIdentity((1,3,6,1,4,1,43,45,1,2,23,1,2,2))
if mibBuilder.loadTexts:hwLswVlanProtoObject.setStatus(_A)
class _HwVLANMibGarpLeaveAllTime_Type(TimeInterval):defaultValue=1000
_HwVLANMibGarpLeaveAllTime_Type.__name__=_I
_HwVLANMibGarpLeaveAllTime_Object=MibScalar
hwVLANMibGarpLeaveAllTime=_HwVLANMibGarpLeaveAllTime_Object((1,3,6,1,4,1,43,45,1,2,23,1,2,2,14),_HwVLANMibGarpLeaveAllTime_Type())
hwVLANMibGarpLeaveAllTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hwVLANMibGarpLeaveAllTime.setStatus(_A)
_HwvLANMibSwitchCountTable_Object=MibTable
hwvLANMibSwitchCountTable=_HwvLANMibSwitchCountTable_Object((1,3,6,1,4,1,43,45,1,2,23,1,2,2,15))
if mibBuilder.loadTexts:hwvLANMibSwitchCountTable.setStatus(_A)
_HwvLANMibSwitchCountEntry_Object=MibTableRow
hwvLANMibSwitchCountEntry=_HwvLANMibSwitchCountEntry_Object((1,3,6,1,4,1,43,45,1,2,23,1,2,2,15,1))
if mibBuilder.loadTexts:hwvLANMibSwitchCountEntry.setStatus(_A)
_HwVLANMibSwitchGMRPRXPkt_Type=Counter32
_HwVLANMibSwitchGMRPRXPkt_Object=MibTableColumn
hwVLANMibSwitchGMRPRXPkt=_HwVLANMibSwitchGMRPRXPkt_Object((1,3,6,1,4,1,43,45,1,2,23,1,2,2,15,1,1),_HwVLANMibSwitchGMRPRXPkt_Type())
hwVLANMibSwitchGMRPRXPkt.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVLANMibSwitchGMRPRXPkt.setStatus(_A)
_HwVLANMibSwitchGVRPRXPkt_Type=Counter32
_HwVLANMibSwitchGVRPRXPkt_Object=MibTableColumn
hwVLANMibSwitchGVRPRXPkt=_HwVLANMibSwitchGVRPRXPkt_Object((1,3,6,1,4,1,43,45,1,2,23,1,2,2,15,1,2),_HwVLANMibSwitchGVRPRXPkt_Type())
hwVLANMibSwitchGVRPRXPkt.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVLANMibSwitchGVRPRXPkt.setStatus(_A)
_HwVLANMibSwitchGMRPTXPkt_Type=Counter32
_HwVLANMibSwitchGMRPTXPkt_Object=MibTableColumn
hwVLANMibSwitchGMRPTXPkt=_HwVLANMibSwitchGMRPTXPkt_Object((1,3,6,1,4,1,43,45,1,2,23,1,2,2,15,1,3),_HwVLANMibSwitchGMRPTXPkt_Type())
hwVLANMibSwitchGMRPTXPkt.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVLANMibSwitchGMRPTXPkt.setStatus(_A)
_HwVLANMibSwitchGVRPTXPkt_Type=Counter32
_HwVLANMibSwitchGVRPTXPkt_Object=MibTableColumn
hwVLANMibSwitchGVRPTXPkt=_HwVLANMibSwitchGVRPTXPkt_Object((1,3,6,1,4,1,43,45,1,2,23,1,2,2,15,1,4),_HwVLANMibSwitchGVRPTXPkt_Type())
hwVLANMibSwitchGVRPTXPkt.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVLANMibSwitchGVRPTXPkt.setStatus(_A)
_HwVLANMibSwitchDiscardedPkt_Type=Counter32
_HwVLANMibSwitchDiscardedPkt_Object=MibTableColumn
hwVLANMibSwitchDiscardedPkt=_HwVLANMibSwitchDiscardedPkt_Object((1,3,6,1,4,1,43,45,1,2,23,1,2,2,15,1,5),_HwVLANMibSwitchDiscardedPkt_Type())
hwVLANMibSwitchDiscardedPkt.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVLANMibSwitchDiscardedPkt.setStatus(_A)
class _HwVLANMibSwitchGarpStatClear_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('clear',1))
_HwVLANMibSwitchGarpStatClear_Type.__name__=_D
_HwVLANMibSwitchGarpStatClear_Object=MibTableColumn
hwVLANMibSwitchGarpStatClear=_HwVLANMibSwitchGarpStatClear_Object((1,3,6,1,4,1,43,45,1,2,23,1,2,2,15,1,6),_HwVLANMibSwitchGarpStatClear_Type())
hwVLANMibSwitchGarpStatClear.setMaxAccess(_C)
if mibBuilder.loadTexts:hwVLANMibSwitchGarpStatClear.setStatus(_A)
_HwvLANMibHoldTimeTable_Object=MibTable
hwvLANMibHoldTimeTable=_HwvLANMibHoldTimeTable_Object((1,3,6,1,4,1,43,45,1,2,23,1,2,2,16))
if mibBuilder.loadTexts:hwvLANMibHoldTimeTable.setStatus(_A)
_HwvLANMibHoldTimeEntry_Object=MibTableRow
hwvLANMibHoldTimeEntry=_HwvLANMibHoldTimeEntry_Object((1,3,6,1,4,1,43,45,1,2,23,1,2,2,16,1))
if mibBuilder.loadTexts:hwvLANMibHoldTimeEntry.setStatus(_A)
class _HwVLANMibHoldTime_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,32765))
_HwVLANMibHoldTime_Type.__name__=_D
_HwVLANMibHoldTime_Object=MibTableColumn
hwVLANMibHoldTime=_HwVLANMibHoldTime_Object((1,3,6,1,4,1,43,45,1,2,23,1,2,2,16,1,1),_HwVLANMibHoldTime_Type())
hwVLANMibHoldTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hwVLANMibHoldTime.setStatus(_A)
hwifVLANTrunkStatusEntry.registerAugmentions((_E,_Q))
hwvLANMibSwitchCountEntry.setIndexNames(*hwifVLANTrunkStatusEntry.getIndexNames())
ifEntry.registerAugmentions((_E,_R))
hwvLANMibHoldTimeEntry.setIndexNames(*ifEntry.getIndexNames())
mibBuilder.exportSymbols(_E,**{'HwVlanIndex':HwVlanIndex,'hwLswVlan':hwLswVlan,'hwLswVlanMngObject':hwLswVlanMngObject,'hwdot1qVlanMIBTable':hwdot1qVlanMIBTable,'hwdot1qVlanMIBEntry':hwdot1qVlanMIBEntry,_J:hwdot1qVlanIndex,'hwdot1qVlanName':hwdot1qVlanName,'hwdot1qVlanPorts':hwdot1qVlanPorts,'hwdot1qVlanType':hwdot1qVlanType,'hwdot1qVlanMacFilter':hwdot1qVlanMacFilter,'hwdot1qVlanMcastUnknownProtos':hwdot1qVlanMcastUnknownProtos,'hwExistInterface':hwExistInterface,'hwVlanInterfaceIndex':hwVlanInterfaceIndex,'hwdot1qVlanMacLearn':hwdot1qVlanMacLearn,'hwdot1qVlanStatus':hwdot1qVlanStatus,'hwdot1qVlanCreationTime':hwdot1qVlanCreationTime,'hwdot1qVlanPriority':hwdot1qVlanPriority,'hwdot1qVlanRowStatus':hwdot1qVlanRowStatus,'hwdot1qVlanBroadcastSuppression':hwdot1qVlanBroadcastSuppression,'hwdot1qVlanBcastSuppressionPPS':hwdot1qVlanBcastSuppressionPPS,'hwdot1qVlanMulticast':hwdot1qVlanMulticast,'hwdot1qVlanTaggedPorts':hwdot1qVlanTaggedPorts,'hwdot1qVlanUntaggedPorts':hwdot1qVlanUntaggedPorts,'hwdot1qVlanPortIndexs':hwdot1qVlanPortIndexs,'hwVlanInterfaceTable':hwVlanInterfaceTable,'hwVlanInterfaceEntry':hwVlanInterfaceEntry,_K:hwVlanInterfaceID,'hwdot1qVlanID':hwdot1qVlanID,'hwdot1qVlanIpAddress':hwdot1qVlanIpAddress,'hwdot1qVlanIpAddressMask':hwdot1qVlanIpAddressMask,'hwVlanInterfaceAdminStatus':hwVlanInterfaceAdminStatus,'hwVlanInterfaceFrameType':hwVlanInterfaceFrameType,'hwInterfaceRowStatus':hwInterfaceRowStatus,'hwVlanInterfaceIpMethod':hwVlanInterfaceIpMethod,'hwVlanInterfaceIfIndex':hwVlanInterfaceIfIndex,'hwifIsolateMappingTable':hwifIsolateMappingTable,'hwifIsolateMappingEntry':hwifIsolateMappingEntry,_L:hwifIsolatePrimaryVlanID,'hwifIsolateSecondaryVlanlistLow':hwifIsolateSecondaryVlanlistLow,'hwifIsolateSecondaryVlanlistHigh':hwifIsolateSecondaryVlanlistHigh,'hwVlanInterfaceAddrTable':hwVlanInterfaceAddrTable,'hwVlanInterfaceAddrEntry':hwVlanInterfaceAddrEntry,_M:hwVlanInterfaceIpIfIndex,_N:hwVlanInterfaceIpAddr,'hwVlanInterfaceIpMask':hwVlanInterfaceIpMask,'hwVlanInterfaceIpType':hwVlanInterfaceIpType,'hwVlanInterfaceIpRowStatus':hwVlanInterfaceIpRowStatus,'hwdot1qVlanBatchMIBTable':hwdot1qVlanBatchMIBTable,'hwDot1qVlanBatchMIBEntry':hwDot1qVlanBatchMIBEntry,_O:hwdot1qVlanBatchOperIndex,'hwdot1qVlanBatchStartIndex':hwdot1qVlanBatchStartIndex,'hwdot1qVlanBatchEndIndex':hwdot1qVlanBatchEndIndex,'hwdot1qVlanBatchOperStatus':hwdot1qVlanBatchOperStatus,'hwdot1qVlanBatchRowStatus':hwdot1qVlanBatchRowStatus,'hwdot1qVlanBatchSetOperate':hwdot1qVlanBatchSetOperate,'hwifSuperVlanMappingTable':hwifSuperVlanMappingTable,'hwifSuperVlanMappingEntry':hwifSuperVlanMappingEntry,_P:hwifSuperVlanID,'hwifSubVlanlistLow':hwifSubVlanlistLow,'hwifSubVlanlistHigh':hwifSubVlanlistHigh,'hwLswVlanProtoObject':hwLswVlanProtoObject,'hwVLANMibGarpLeaveAllTime':hwVLANMibGarpLeaveAllTime,'hwvLANMibSwitchCountTable':hwvLANMibSwitchCountTable,_Q:hwvLANMibSwitchCountEntry,'hwVLANMibSwitchGMRPRXPkt':hwVLANMibSwitchGMRPRXPkt,'hwVLANMibSwitchGVRPRXPkt':hwVLANMibSwitchGVRPRXPkt,'hwVLANMibSwitchGMRPTXPkt':hwVLANMibSwitchGMRPTXPkt,'hwVLANMibSwitchGVRPTXPkt':hwVLANMibSwitchGVRPTXPkt,'hwVLANMibSwitchDiscardedPkt':hwVLANMibSwitchDiscardedPkt,'hwVLANMibSwitchGarpStatClear':hwVLANMibSwitchGarpStatClear,'hwvLANMibHoldTimeTable':hwvLANMibHoldTimeTable,_R:hwvLANMibHoldTimeEntry,'hwVLANMibHoldTime':hwVLANMibHoldTime})