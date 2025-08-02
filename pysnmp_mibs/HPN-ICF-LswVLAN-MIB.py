_S='hpnicfvLANMibHoldTimeEntry'
_R='hpnicfvLANMibSwitchCountEntry'
_Q='hpnicfPrimaryVlanID'
_P='hpnicfifSuperVlanID'
_O='hpnicfdot1qVlanBatchOperIndex'
_N='hpnicfVlanInterfaceIpAddr'
_M='hpnicfVlanInterfaceIpIfIndex'
_L='hpnicfifIsolatePrimaryVlanID'
_K='hpnicfVlanInterfaceID'
_J='hpnicfdot1qVlanIndex'
_I='TimeInterval'
_H='SnmpAdminString'
_G='read-create'
_F='OctetString'
_E='HPN-ICF-LswVLAN-MIB'
_D='Integer32'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
PortList,hpnicfifVLANTrunkStatusEntry=mibBuilder.importSymbols('HPN-ICF-LswINF-MIB','PortList','hpnicfifVLANTrunkStatusEntry')
hpnicflswCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicflswCommon')
ifEntry,=mibBuilder.importSymbols('IF-MIB','ifEntry')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_H)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeInterval,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_I,'TruthValue')
hpnicfLswVlan=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,8,35,2))
class HpnicfVlanIndex(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_HpnicfLswVlanMngObject_ObjectIdentity=ObjectIdentity
hpnicfLswVlanMngObject=_HpnicfLswVlanMngObject_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,8,35,2,1))
if mibBuilder.loadTexts:hpnicfLswVlanMngObject.setStatus(_A)
_Hpnicfdot1qVlanMIBTable_Object=MibTable
hpnicfdot1qVlanMIBTable=_Hpnicfdot1qVlanMIBTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,2,1,1))
if mibBuilder.loadTexts:hpnicfdot1qVlanMIBTable.setStatus(_A)
_Hpnicfdot1qVlanMIBEntry_Object=MibTableRow
hpnicfdot1qVlanMIBEntry=_Hpnicfdot1qVlanMIBEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,2,1,1,1))
hpnicfdot1qVlanMIBEntry.setIndexNames((0,_E,_J))
if mibBuilder.loadTexts:hpnicfdot1qVlanMIBEntry.setStatus(_A)
_Hpnicfdot1qVlanIndex_Type=HpnicfVlanIndex
_Hpnicfdot1qVlanIndex_Object=MibTableColumn
hpnicfdot1qVlanIndex=_Hpnicfdot1qVlanIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,2,1,1,1,1),_Hpnicfdot1qVlanIndex_Type())
hpnicfdot1qVlanIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdot1qVlanIndex.setStatus(_A)
class _Hpnicfdot1qVlanName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_Hpnicfdot1qVlanName_Type.__name__=_H
_Hpnicfdot1qVlanName_Object=MibTableColumn
hpnicfdot1qVlanName=_Hpnicfdot1qVlanName_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,2,1,1,1,2),_Hpnicfdot1qVlanName_Type())
hpnicfdot1qVlanName.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfdot1qVlanName.setStatus(_A)
_Hpnicfdot1qVlanPorts_Type=PortList
_Hpnicfdot1qVlanPorts_Object=MibTableColumn
hpnicfdot1qVlanPorts=_Hpnicfdot1qVlanPorts_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,2,1,1,1,3),_Hpnicfdot1qVlanPorts_Type())
hpnicfdot1qVlanPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfdot1qVlanPorts.setStatus(_A)
class _Hpnicfdot1qVlanType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('superVlan',1),('common-vlan',2),('sub-vlan',3),('isolate-user-vlan',4),('secondary-vlan',5),('primaryVlan',6)))
_Hpnicfdot1qVlanType_Type.__name__=_D
_Hpnicfdot1qVlanType_Object=MibTableColumn
hpnicfdot1qVlanType=_Hpnicfdot1qVlanType_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,2,1,1,1,4),_Hpnicfdot1qVlanType_Type())
hpnicfdot1qVlanType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfdot1qVlanType.setStatus(_A)
_Hpnicfdot1qVlanMacFilter_Type=TruthValue
_Hpnicfdot1qVlanMacFilter_Object=MibTableColumn
hpnicfdot1qVlanMacFilter=_Hpnicfdot1qVlanMacFilter_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,2,1,1,1,5),_Hpnicfdot1qVlanMacFilter_Type())
hpnicfdot1qVlanMacFilter.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdot1qVlanMacFilter.setStatus(_A)
_Hpnicfdot1qVlanMcastUnknownProtos_Type=TruthValue
_Hpnicfdot1qVlanMcastUnknownProtos_Object=MibTableColumn
hpnicfdot1qVlanMcastUnknownProtos=_Hpnicfdot1qVlanMcastUnknownProtos_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,2,1,1,1,6),_Hpnicfdot1qVlanMcastUnknownProtos_Type())
hpnicfdot1qVlanMcastUnknownProtos.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdot1qVlanMcastUnknownProtos.setStatus(_A)
_HpnicfExistInterface_Type=TruthValue
_HpnicfExistInterface_Object=MibTableColumn
hpnicfExistInterface=_HpnicfExistInterface_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,2,1,1,1,7),_HpnicfExistInterface_Type())
hpnicfExistInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfExistInterface.setStatus(_A)
_HpnicfVlanInterfaceIndex_Type=Integer32
_HpnicfVlanInterfaceIndex_Object=MibTableColumn
hpnicfVlanInterfaceIndex=_HpnicfVlanInterfaceIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,2,1,1,1,8),_HpnicfVlanInterfaceIndex_Type())
hpnicfVlanInterfaceIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfVlanInterfaceIndex.setStatus(_A)
_Hpnicfdot1qVlanMacLearn_Type=TruthValue
_Hpnicfdot1qVlanMacLearn_Object=MibTableColumn
hpnicfdot1qVlanMacLearn=_Hpnicfdot1qVlanMacLearn_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,2,1,1,1,9),_Hpnicfdot1qVlanMacLearn_Type())
hpnicfdot1qVlanMacLearn.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdot1qVlanMacLearn.setStatus(_A)
class _Hpnicfdot1qVlanStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('other',1),('static',2),('dynamic',3)))
_Hpnicfdot1qVlanStatus_Type.__name__=_D
_Hpnicfdot1qVlanStatus_Object=MibTableColumn
hpnicfdot1qVlanStatus=_Hpnicfdot1qVlanStatus_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,2,1,1,1,10),_Hpnicfdot1qVlanStatus_Type())
hpnicfdot1qVlanStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdot1qVlanStatus.setStatus(_A)
_Hpnicfdot1qVlanCreationTime_Type=TimeTicks
_Hpnicfdot1qVlanCreationTime_Object=MibTableColumn
hpnicfdot1qVlanCreationTime=_Hpnicfdot1qVlanCreationTime_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,2,1,1,1,11),_Hpnicfdot1qVlanCreationTime_Type())
hpnicfdot1qVlanCreationTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdot1qVlanCreationTime.setStatus(_A)
class _Hpnicfdot1qVlanPriority_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Hpnicfdot1qVlanPriority_Type.__name__=_D
_Hpnicfdot1qVlanPriority_Object=MibTableColumn
hpnicfdot1qVlanPriority=_Hpnicfdot1qVlanPriority_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,2,1,1,1,12),_Hpnicfdot1qVlanPriority_Type())
hpnicfdot1qVlanPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfdot1qVlanPriority.setStatus(_A)
_Hpnicfdot1qVlanRowStatus_Type=RowStatus
_Hpnicfdot1qVlanRowStatus_Object=MibTableColumn
hpnicfdot1qVlanRowStatus=_Hpnicfdot1qVlanRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,2,1,1,1,13),_Hpnicfdot1qVlanRowStatus_Type())
hpnicfdot1qVlanRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfdot1qVlanRowStatus.setStatus(_A)
class _Hpnicfdot1qVlanBroadcastSuppression_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_Hpnicfdot1qVlanBroadcastSuppression_Type.__name__=_D
_Hpnicfdot1qVlanBroadcastSuppression_Object=MibTableColumn
hpnicfdot1qVlanBroadcastSuppression=_Hpnicfdot1qVlanBroadcastSuppression_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,2,1,1,1,14),_Hpnicfdot1qVlanBroadcastSuppression_Type())
hpnicfdot1qVlanBroadcastSuppression.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfdot1qVlanBroadcastSuppression.setStatus(_A)
class _Hpnicfdot1qVlanBcastSuppressionPPS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,148800))
_Hpnicfdot1qVlanBcastSuppressionPPS_Type.__name__=_D
_Hpnicfdot1qVlanBcastSuppressionPPS_Object=MibTableColumn
hpnicfdot1qVlanBcastSuppressionPPS=_Hpnicfdot1qVlanBcastSuppressionPPS_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,2,1,1,1,15),_Hpnicfdot1qVlanBcastSuppressionPPS_Type())
hpnicfdot1qVlanBcastSuppressionPPS.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfdot1qVlanBcastSuppressionPPS.setStatus(_A)
class _Hpnicfdot1qVlanMulticast_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('disable',0),('enable',1)))
_Hpnicfdot1qVlanMulticast_Type.__name__=_D
_Hpnicfdot1qVlanMulticast_Object=MibTableColumn
hpnicfdot1qVlanMulticast=_Hpnicfdot1qVlanMulticast_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,2,1,1,1,16),_Hpnicfdot1qVlanMulticast_Type())
hpnicfdot1qVlanMulticast.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfdot1qVlanMulticast.setStatus(_A)
_Hpnicfdot1qVlanTaggedPorts_Type=PortList
_Hpnicfdot1qVlanTaggedPorts_Object=MibTableColumn
hpnicfdot1qVlanTaggedPorts=_Hpnicfdot1qVlanTaggedPorts_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,2,1,1,1,17),_Hpnicfdot1qVlanTaggedPorts_Type())
hpnicfdot1qVlanTaggedPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdot1qVlanTaggedPorts.setStatus(_A)
_Hpnicfdot1qVlanUntaggedPorts_Type=PortList
_Hpnicfdot1qVlanUntaggedPorts_Object=MibTableColumn
hpnicfdot1qVlanUntaggedPorts=_Hpnicfdot1qVlanUntaggedPorts_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,2,1,1,1,18),_Hpnicfdot1qVlanUntaggedPorts_Type())
hpnicfdot1qVlanUntaggedPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdot1qVlanUntaggedPorts.setStatus(_A)
_Hpnicfdot1qVlanPortIndexs_Type=OctetString
_Hpnicfdot1qVlanPortIndexs_Object=MibTableColumn
hpnicfdot1qVlanPortIndexs=_Hpnicfdot1qVlanPortIndexs_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,2,1,1,1,19),_Hpnicfdot1qVlanPortIndexs_Type())
hpnicfdot1qVlanPortIndexs.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfdot1qVlanPortIndexs.setStatus(_A)
_HpnicfVlanInterfaceTable_Object=MibTable
hpnicfVlanInterfaceTable=_HpnicfVlanInterfaceTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,2,1,2))
if mibBuilder.loadTexts:hpnicfVlanInterfaceTable.setStatus(_A)
_HpnicfVlanInterfaceEntry_Object=MibTableRow
hpnicfVlanInterfaceEntry=_HpnicfVlanInterfaceEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,2,1,2,1))
hpnicfVlanInterfaceEntry.setIndexNames((0,_E,_K))
if mibBuilder.loadTexts:hpnicfVlanInterfaceEntry.setStatus(_A)
_HpnicfVlanInterfaceID_Type=Integer32
_HpnicfVlanInterfaceID_Object=MibTableColumn
hpnicfVlanInterfaceID=_HpnicfVlanInterfaceID_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,2,1,2,1,1),_HpnicfVlanInterfaceID_Type())
hpnicfVlanInterfaceID.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfVlanInterfaceID.setStatus(_A)
_Hpnicfdot1qVlanID_Type=HpnicfVlanIndex
_Hpnicfdot1qVlanID_Object=MibTableColumn
hpnicfdot1qVlanID=_Hpnicfdot1qVlanID_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,2,1,2,1,2),_Hpnicfdot1qVlanID_Type())
hpnicfdot1qVlanID.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdot1qVlanID.setStatus(_A)
_Hpnicfdot1qVlanIpAddress_Type=IpAddress
_Hpnicfdot1qVlanIpAddress_Object=MibTableColumn
hpnicfdot1qVlanIpAddress=_Hpnicfdot1qVlanIpAddress_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,2,1,2,1,3),_Hpnicfdot1qVlanIpAddress_Type())
hpnicfdot1qVlanIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfdot1qVlanIpAddress.setStatus(_A)
_Hpnicfdot1qVlanIpAddressMask_Type=IpAddress
_Hpnicfdot1qVlanIpAddressMask_Object=MibTableColumn
hpnicfdot1qVlanIpAddressMask=_Hpnicfdot1qVlanIpAddressMask_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,2,1,2,1,4),_Hpnicfdot1qVlanIpAddressMask_Type())
hpnicfdot1qVlanIpAddressMask.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfdot1qVlanIpAddressMask.setStatus(_A)
class _HpnicfVlanInterfaceAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_HpnicfVlanInterfaceAdminStatus_Type.__name__=_D
_HpnicfVlanInterfaceAdminStatus_Object=MibTableColumn
hpnicfVlanInterfaceAdminStatus=_HpnicfVlanInterfaceAdminStatus_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,2,1,2,1,5),_HpnicfVlanInterfaceAdminStatus_Type())
hpnicfVlanInterfaceAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfVlanInterfaceAdminStatus.setStatus(_A)
class _HpnicfVlanInterfaceFrameType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('ethernet-ii',1),('ethernet-snap',2),('ethernet-8022',3),('ethernet-8023',4)))
_HpnicfVlanInterfaceFrameType_Type.__name__=_D
_HpnicfVlanInterfaceFrameType_Object=MibTableColumn
hpnicfVlanInterfaceFrameType=_HpnicfVlanInterfaceFrameType_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,2,1,2,1,6),_HpnicfVlanInterfaceFrameType_Type())
hpnicfVlanInterfaceFrameType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfVlanInterfaceFrameType.setStatus(_A)
_HpnicfInterfaceRowStatus_Type=RowStatus
_HpnicfInterfaceRowStatus_Object=MibTableColumn
hpnicfInterfaceRowStatus=_HpnicfInterfaceRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,2,1,2,1,7),_HpnicfInterfaceRowStatus_Type())
hpnicfInterfaceRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfInterfaceRowStatus.setStatus(_A)
class _HpnicfVlanInterfaceIpMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('assigned-ip',1),('dhcp-ip',2),('bootp-ip',3)))
_HpnicfVlanInterfaceIpMethod_Type.__name__=_D
_HpnicfVlanInterfaceIpMethod_Object=MibTableColumn
hpnicfVlanInterfaceIpMethod=_HpnicfVlanInterfaceIpMethod_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,2,1,2,1,8),_HpnicfVlanInterfaceIpMethod_Type())
hpnicfVlanInterfaceIpMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfVlanInterfaceIpMethod.setStatus(_A)
_HpnicfVlanInterfaceIfIndex_Type=Integer32
_HpnicfVlanInterfaceIfIndex_Object=MibTableColumn
hpnicfVlanInterfaceIfIndex=_HpnicfVlanInterfaceIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,2,1,2,1,9),_HpnicfVlanInterfaceIfIndex_Type())
hpnicfVlanInterfaceIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfVlanInterfaceIfIndex.setStatus(_A)
_HpnicfifIsolateMappingTable_Object=MibTable
hpnicfifIsolateMappingTable=_HpnicfifIsolateMappingTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,2,1,4))
if mibBuilder.loadTexts:hpnicfifIsolateMappingTable.setStatus(_A)
_HpnicfifIsolateMappingEntry_Object=MibTableRow
hpnicfifIsolateMappingEntry=_HpnicfifIsolateMappingEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,2,1,4,1))
hpnicfifIsolateMappingEntry.setIndexNames((0,_E,_L))
if mibBuilder.loadTexts:hpnicfifIsolateMappingEntry.setStatus(_A)
_HpnicfifIsolatePrimaryVlanID_Type=HpnicfVlanIndex
_HpnicfifIsolatePrimaryVlanID_Object=MibTableColumn
hpnicfifIsolatePrimaryVlanID=_HpnicfifIsolatePrimaryVlanID_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,2,1,4,1,1),_HpnicfifIsolatePrimaryVlanID_Type())
hpnicfifIsolatePrimaryVlanID.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfifIsolatePrimaryVlanID.setStatus(_A)
class _HpnicfifIsolateSecondaryVlanlistLow_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_HpnicfifIsolateSecondaryVlanlistLow_Type.__name__=_F
_HpnicfifIsolateSecondaryVlanlistLow_Object=MibTableColumn
hpnicfifIsolateSecondaryVlanlistLow=_HpnicfifIsolateSecondaryVlanlistLow_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,2,1,4,1,2),_HpnicfifIsolateSecondaryVlanlistLow_Type())
hpnicfifIsolateSecondaryVlanlistLow.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfifIsolateSecondaryVlanlistLow.setStatus(_A)
class _HpnicfifIsolateSecondaryVlanlistHigh_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_HpnicfifIsolateSecondaryVlanlistHigh_Type.__name__=_F
_HpnicfifIsolateSecondaryVlanlistHigh_Object=MibTableColumn
hpnicfifIsolateSecondaryVlanlistHigh=_HpnicfifIsolateSecondaryVlanlistHigh_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,2,1,4,1,3),_HpnicfifIsolateSecondaryVlanlistHigh_Type())
hpnicfifIsolateSecondaryVlanlistHigh.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfifIsolateSecondaryVlanlistHigh.setStatus(_A)
_HpnicfVlanInterfaceAddrTable_Object=MibTable
hpnicfVlanInterfaceAddrTable=_HpnicfVlanInterfaceAddrTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,2,1,5))
if mibBuilder.loadTexts:hpnicfVlanInterfaceAddrTable.setStatus(_A)
_HpnicfVlanInterfaceAddrEntry_Object=MibTableRow
hpnicfVlanInterfaceAddrEntry=_HpnicfVlanInterfaceAddrEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,2,1,5,1))
hpnicfVlanInterfaceAddrEntry.setIndexNames((0,_E,_M),(0,_E,_N))
if mibBuilder.loadTexts:hpnicfVlanInterfaceAddrEntry.setStatus(_A)
_HpnicfVlanInterfaceIpIfIndex_Type=Integer32
_HpnicfVlanInterfaceIpIfIndex_Object=MibTableColumn
hpnicfVlanInterfaceIpIfIndex=_HpnicfVlanInterfaceIpIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,2,1,5,1,1),_HpnicfVlanInterfaceIpIfIndex_Type())
hpnicfVlanInterfaceIpIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfVlanInterfaceIpIfIndex.setStatus(_A)
_HpnicfVlanInterfaceIpAddr_Type=IpAddress
_HpnicfVlanInterfaceIpAddr_Object=MibTableColumn
hpnicfVlanInterfaceIpAddr=_HpnicfVlanInterfaceIpAddr_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,2,1,5,1,2),_HpnicfVlanInterfaceIpAddr_Type())
hpnicfVlanInterfaceIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfVlanInterfaceIpAddr.setStatus(_A)
_HpnicfVlanInterfaceIpMask_Type=IpAddress
_HpnicfVlanInterfaceIpMask_Object=MibTableColumn
hpnicfVlanInterfaceIpMask=_HpnicfVlanInterfaceIpMask_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,2,1,5,1,3),_HpnicfVlanInterfaceIpMask_Type())
hpnicfVlanInterfaceIpMask.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfVlanInterfaceIpMask.setStatus(_A)
class _HpnicfVlanInterfaceIpType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('primary',1),('sub',2),('cluster',3),('vrrp',4)))
_HpnicfVlanInterfaceIpType_Type.__name__=_D
_HpnicfVlanInterfaceIpType_Object=MibTableColumn
hpnicfVlanInterfaceIpType=_HpnicfVlanInterfaceIpType_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,2,1,5,1,4),_HpnicfVlanInterfaceIpType_Type())
hpnicfVlanInterfaceIpType.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfVlanInterfaceIpType.setStatus(_A)
_HpnicfVlanInterfaceIpRowStatus_Type=RowStatus
_HpnicfVlanInterfaceIpRowStatus_Object=MibTableColumn
hpnicfVlanInterfaceIpRowStatus=_HpnicfVlanInterfaceIpRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,2,1,5,1,5),_HpnicfVlanInterfaceIpRowStatus_Type())
hpnicfVlanInterfaceIpRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfVlanInterfaceIpRowStatus.setStatus(_A)
_HpnicfDot1qVlanBatchMIBTable_Object=MibTable
hpnicfDot1qVlanBatchMIBTable=_HpnicfDot1qVlanBatchMIBTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,2,1,6))
if mibBuilder.loadTexts:hpnicfDot1qVlanBatchMIBTable.setStatus(_A)
_HpnicfDot1qVlanBatchMIBEntry_Object=MibTableRow
hpnicfDot1qVlanBatchMIBEntry=_HpnicfDot1qVlanBatchMIBEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,2,1,6,1))
hpnicfDot1qVlanBatchMIBEntry.setIndexNames((0,_E,_O))
if mibBuilder.loadTexts:hpnicfDot1qVlanBatchMIBEntry.setStatus(_A)
_Hpnicfdot1qVlanBatchOperIndex_Type=Integer32
_Hpnicfdot1qVlanBatchOperIndex_Object=MibTableColumn
hpnicfdot1qVlanBatchOperIndex=_Hpnicfdot1qVlanBatchOperIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,2,1,6,1,1),_Hpnicfdot1qVlanBatchOperIndex_Type())
hpnicfdot1qVlanBatchOperIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdot1qVlanBatchOperIndex.setStatus(_A)
_Hpnicfdot1qVlanBatchStartIndex_Type=HpnicfVlanIndex
_Hpnicfdot1qVlanBatchStartIndex_Object=MibTableColumn
hpnicfdot1qVlanBatchStartIndex=_Hpnicfdot1qVlanBatchStartIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,2,1,6,1,2),_Hpnicfdot1qVlanBatchStartIndex_Type())
hpnicfdot1qVlanBatchStartIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfdot1qVlanBatchStartIndex.setStatus(_A)
_Hpnicfdot1qVlanBatchEndIndex_Type=HpnicfVlanIndex
_Hpnicfdot1qVlanBatchEndIndex_Object=MibTableColumn
hpnicfdot1qVlanBatchEndIndex=_Hpnicfdot1qVlanBatchEndIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,2,1,6,1,3),_Hpnicfdot1qVlanBatchEndIndex_Type())
hpnicfdot1qVlanBatchEndIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfdot1qVlanBatchEndIndex.setStatus(_A)
class _Hpnicfdot1qVlanBatchOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('opInprogress',1),('opfailure',2),('opsuccess',3),('opsuccesspartial',4)))
_Hpnicfdot1qVlanBatchOperStatus_Type.__name__=_D
_Hpnicfdot1qVlanBatchOperStatus_Object=MibTableColumn
hpnicfdot1qVlanBatchOperStatus=_Hpnicfdot1qVlanBatchOperStatus_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,2,1,6,1,4),_Hpnicfdot1qVlanBatchOperStatus_Type())
hpnicfdot1qVlanBatchOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdot1qVlanBatchOperStatus.setStatus(_A)
_Hpnicfdot1qVlanBatchRowStatus_Type=RowStatus
_Hpnicfdot1qVlanBatchRowStatus_Object=MibTableColumn
hpnicfdot1qVlanBatchRowStatus=_Hpnicfdot1qVlanBatchRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,2,1,6,1,5),_Hpnicfdot1qVlanBatchRowStatus_Type())
hpnicfdot1qVlanBatchRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfdot1qVlanBatchRowStatus.setStatus(_A)
class _Hpnicfdot1qVlanBatchSetOperate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('create',1),('delete',2)))
_Hpnicfdot1qVlanBatchSetOperate_Type.__name__=_D
_Hpnicfdot1qVlanBatchSetOperate_Object=MibTableColumn
hpnicfdot1qVlanBatchSetOperate=_Hpnicfdot1qVlanBatchSetOperate_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,2,1,6,1,6),_Hpnicfdot1qVlanBatchSetOperate_Type())
hpnicfdot1qVlanBatchSetOperate.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfdot1qVlanBatchSetOperate.setStatus(_A)
_HpnicfifSuperVlanMappingTable_Object=MibTable
hpnicfifSuperVlanMappingTable=_HpnicfifSuperVlanMappingTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,2,1,7))
if mibBuilder.loadTexts:hpnicfifSuperVlanMappingTable.setStatus(_A)
_HpnicfifSuperVlanMappingEntry_Object=MibTableRow
hpnicfifSuperVlanMappingEntry=_HpnicfifSuperVlanMappingEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,2,1,7,1))
hpnicfifSuperVlanMappingEntry.setIndexNames((0,_E,_P))
if mibBuilder.loadTexts:hpnicfifSuperVlanMappingEntry.setStatus(_A)
_HpnicfifSuperVlanID_Type=HpnicfVlanIndex
_HpnicfifSuperVlanID_Object=MibTableColumn
hpnicfifSuperVlanID=_HpnicfifSuperVlanID_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,2,1,7,1,1),_HpnicfifSuperVlanID_Type())
hpnicfifSuperVlanID.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfifSuperVlanID.setStatus(_A)
class _HpnicfifSubVlanlistLow_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_HpnicfifSubVlanlistLow_Type.__name__=_F
_HpnicfifSubVlanlistLow_Object=MibTableColumn
hpnicfifSubVlanlistLow=_HpnicfifSubVlanlistLow_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,2,1,7,1,2),_HpnicfifSubVlanlistLow_Type())
hpnicfifSubVlanlistLow.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfifSubVlanlistLow.setStatus(_A)
class _HpnicfifSubVlanlistHigh_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_HpnicfifSubVlanlistHigh_Type.__name__=_F
_HpnicfifSubVlanlistHigh_Object=MibTableColumn
hpnicfifSubVlanlistHigh=_HpnicfifSubVlanlistHigh_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,2,1,7,1,3),_HpnicfifSubVlanlistHigh_Type())
hpnicfifSubVlanlistHigh.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfifSubVlanlistHigh.setStatus(_A)
_HpnicfPrivateVlanMappingTable_Object=MibTable
hpnicfPrivateVlanMappingTable=_HpnicfPrivateVlanMappingTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,2,1,8))
if mibBuilder.loadTexts:hpnicfPrivateVlanMappingTable.setStatus(_A)
_HpnicfPrivateVlanMappingEntry_Object=MibTableRow
hpnicfPrivateVlanMappingEntry=_HpnicfPrivateVlanMappingEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,2,1,8,1))
hpnicfPrivateVlanMappingEntry.setIndexNames((0,_E,_Q))
if mibBuilder.loadTexts:hpnicfPrivateVlanMappingEntry.setStatus(_A)
_HpnicfPrimaryVlanID_Type=HpnicfVlanIndex
_HpnicfPrimaryVlanID_Object=MibTableColumn
hpnicfPrimaryVlanID=_HpnicfPrimaryVlanID_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,2,1,8,1,1),_HpnicfPrimaryVlanID_Type())
hpnicfPrimaryVlanID.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfPrimaryVlanID.setStatus(_A)
class _HpnicfSecondaryVlanlistLow_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_HpnicfSecondaryVlanlistLow_Type.__name__=_F
_HpnicfSecondaryVlanlistLow_Object=MibTableColumn
hpnicfSecondaryVlanlistLow=_HpnicfSecondaryVlanlistLow_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,2,1,8,1,2),_HpnicfSecondaryVlanlistLow_Type())
hpnicfSecondaryVlanlistLow.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfSecondaryVlanlistLow.setStatus(_A)
class _HpnicfSecondaryVlanlistHigh_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_HpnicfSecondaryVlanlistHigh_Type.__name__=_F
_HpnicfSecondaryVlanlistHigh_Object=MibTableColumn
hpnicfSecondaryVlanlistHigh=_HpnicfSecondaryVlanlistHigh_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,2,1,8,1,3),_HpnicfSecondaryVlanlistHigh_Type())
hpnicfSecondaryVlanlistHigh.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfSecondaryVlanlistHigh.setStatus(_A)
_HpnicfLswVlanProtoObject_ObjectIdentity=ObjectIdentity
hpnicfLswVlanProtoObject=_HpnicfLswVlanProtoObject_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,8,35,2,2))
if mibBuilder.loadTexts:hpnicfLswVlanProtoObject.setStatus(_A)
class _HpnicfVLANMibGarpLeaveAllTime_Type(TimeInterval):defaultValue=1000
_HpnicfVLANMibGarpLeaveAllTime_Type.__name__=_I
_HpnicfVLANMibGarpLeaveAllTime_Object=MibScalar
hpnicfVLANMibGarpLeaveAllTime=_HpnicfVLANMibGarpLeaveAllTime_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,2,2,14),_HpnicfVLANMibGarpLeaveAllTime_Type())
hpnicfVLANMibGarpLeaveAllTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfVLANMibGarpLeaveAllTime.setStatus(_A)
_HpnicfvLANMibSwitchCountTable_Object=MibTable
hpnicfvLANMibSwitchCountTable=_HpnicfvLANMibSwitchCountTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,2,2,15))
if mibBuilder.loadTexts:hpnicfvLANMibSwitchCountTable.setStatus(_A)
_HpnicfvLANMibSwitchCountEntry_Object=MibTableRow
hpnicfvLANMibSwitchCountEntry=_HpnicfvLANMibSwitchCountEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,2,2,15,1))
if mibBuilder.loadTexts:hpnicfvLANMibSwitchCountEntry.setStatus(_A)
_HpnicfVLANMibSwitchGMRPRXPkt_Type=Counter32
_HpnicfVLANMibSwitchGMRPRXPkt_Object=MibTableColumn
hpnicfVLANMibSwitchGMRPRXPkt=_HpnicfVLANMibSwitchGMRPRXPkt_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,2,2,15,1,1),_HpnicfVLANMibSwitchGMRPRXPkt_Type())
hpnicfVLANMibSwitchGMRPRXPkt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfVLANMibSwitchGMRPRXPkt.setStatus(_A)
_HpnicfVLANMibSwitchGVRPRXPkt_Type=Counter32
_HpnicfVLANMibSwitchGVRPRXPkt_Object=MibTableColumn
hpnicfVLANMibSwitchGVRPRXPkt=_HpnicfVLANMibSwitchGVRPRXPkt_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,2,2,15,1,2),_HpnicfVLANMibSwitchGVRPRXPkt_Type())
hpnicfVLANMibSwitchGVRPRXPkt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfVLANMibSwitchGVRPRXPkt.setStatus(_A)
_HpnicfVLANMibSwitchGMRPTXPkt_Type=Counter32
_HpnicfVLANMibSwitchGMRPTXPkt_Object=MibTableColumn
hpnicfVLANMibSwitchGMRPTXPkt=_HpnicfVLANMibSwitchGMRPTXPkt_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,2,2,15,1,3),_HpnicfVLANMibSwitchGMRPTXPkt_Type())
hpnicfVLANMibSwitchGMRPTXPkt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfVLANMibSwitchGMRPTXPkt.setStatus(_A)
_HpnicfVLANMibSwitchGVRPTXPkt_Type=Counter32
_HpnicfVLANMibSwitchGVRPTXPkt_Object=MibTableColumn
hpnicfVLANMibSwitchGVRPTXPkt=_HpnicfVLANMibSwitchGVRPTXPkt_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,2,2,15,1,4),_HpnicfVLANMibSwitchGVRPTXPkt_Type())
hpnicfVLANMibSwitchGVRPTXPkt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfVLANMibSwitchGVRPTXPkt.setStatus(_A)
_HpnicfVLANMibSwitchDiscardedPkt_Type=Counter32
_HpnicfVLANMibSwitchDiscardedPkt_Object=MibTableColumn
hpnicfVLANMibSwitchDiscardedPkt=_HpnicfVLANMibSwitchDiscardedPkt_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,2,2,15,1,5),_HpnicfVLANMibSwitchDiscardedPkt_Type())
hpnicfVLANMibSwitchDiscardedPkt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfVLANMibSwitchDiscardedPkt.setStatus(_A)
class _HpnicfVLANMibSwitchGarpStatClear_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('clear',1))
_HpnicfVLANMibSwitchGarpStatClear_Type.__name__=_D
_HpnicfVLANMibSwitchGarpStatClear_Object=MibTableColumn
hpnicfVLANMibSwitchGarpStatClear=_HpnicfVLANMibSwitchGarpStatClear_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,2,2,15,1,6),_HpnicfVLANMibSwitchGarpStatClear_Type())
hpnicfVLANMibSwitchGarpStatClear.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfVLANMibSwitchGarpStatClear.setStatus(_A)
_HpnicfvLANMibHoldTimeTable_Object=MibTable
hpnicfvLANMibHoldTimeTable=_HpnicfvLANMibHoldTimeTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,2,2,16))
if mibBuilder.loadTexts:hpnicfvLANMibHoldTimeTable.setStatus(_A)
_HpnicfvLANMibHoldTimeEntry_Object=MibTableRow
hpnicfvLANMibHoldTimeEntry=_HpnicfvLANMibHoldTimeEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,2,2,16,1))
if mibBuilder.loadTexts:hpnicfvLANMibHoldTimeEntry.setStatus(_A)
class _HpnicfVLANMibHoldTime_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,32765))
_HpnicfVLANMibHoldTime_Type.__name__=_D
_HpnicfVLANMibHoldTime_Object=MibTableColumn
hpnicfVLANMibHoldTime=_HpnicfVLANMibHoldTime_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,2,2,16,1,1),_HpnicfVLANMibHoldTime_Type())
hpnicfVLANMibHoldTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfVLANMibHoldTime.setStatus(_A)
hpnicfifVLANTrunkStatusEntry.registerAugmentions((_E,_R))
hpnicfvLANMibSwitchCountEntry.setIndexNames(*hpnicfifVLANTrunkStatusEntry.getIndexNames())
ifEntry.registerAugmentions((_E,_S))
hpnicfvLANMibHoldTimeEntry.setIndexNames(*ifEntry.getIndexNames())
mibBuilder.exportSymbols(_E,**{'HpnicfVlanIndex':HpnicfVlanIndex,'hpnicfLswVlan':hpnicfLswVlan,'hpnicfLswVlanMngObject':hpnicfLswVlanMngObject,'hpnicfdot1qVlanMIBTable':hpnicfdot1qVlanMIBTable,'hpnicfdot1qVlanMIBEntry':hpnicfdot1qVlanMIBEntry,_J:hpnicfdot1qVlanIndex,'hpnicfdot1qVlanName':hpnicfdot1qVlanName,'hpnicfdot1qVlanPorts':hpnicfdot1qVlanPorts,'hpnicfdot1qVlanType':hpnicfdot1qVlanType,'hpnicfdot1qVlanMacFilter':hpnicfdot1qVlanMacFilter,'hpnicfdot1qVlanMcastUnknownProtos':hpnicfdot1qVlanMcastUnknownProtos,'hpnicfExistInterface':hpnicfExistInterface,'hpnicfVlanInterfaceIndex':hpnicfVlanInterfaceIndex,'hpnicfdot1qVlanMacLearn':hpnicfdot1qVlanMacLearn,'hpnicfdot1qVlanStatus':hpnicfdot1qVlanStatus,'hpnicfdot1qVlanCreationTime':hpnicfdot1qVlanCreationTime,'hpnicfdot1qVlanPriority':hpnicfdot1qVlanPriority,'hpnicfdot1qVlanRowStatus':hpnicfdot1qVlanRowStatus,'hpnicfdot1qVlanBroadcastSuppression':hpnicfdot1qVlanBroadcastSuppression,'hpnicfdot1qVlanBcastSuppressionPPS':hpnicfdot1qVlanBcastSuppressionPPS,'hpnicfdot1qVlanMulticast':hpnicfdot1qVlanMulticast,'hpnicfdot1qVlanTaggedPorts':hpnicfdot1qVlanTaggedPorts,'hpnicfdot1qVlanUntaggedPorts':hpnicfdot1qVlanUntaggedPorts,'hpnicfdot1qVlanPortIndexs':hpnicfdot1qVlanPortIndexs,'hpnicfVlanInterfaceTable':hpnicfVlanInterfaceTable,'hpnicfVlanInterfaceEntry':hpnicfVlanInterfaceEntry,_K:hpnicfVlanInterfaceID,'hpnicfdot1qVlanID':hpnicfdot1qVlanID,'hpnicfdot1qVlanIpAddress':hpnicfdot1qVlanIpAddress,'hpnicfdot1qVlanIpAddressMask':hpnicfdot1qVlanIpAddressMask,'hpnicfVlanInterfaceAdminStatus':hpnicfVlanInterfaceAdminStatus,'hpnicfVlanInterfaceFrameType':hpnicfVlanInterfaceFrameType,'hpnicfInterfaceRowStatus':hpnicfInterfaceRowStatus,'hpnicfVlanInterfaceIpMethod':hpnicfVlanInterfaceIpMethod,'hpnicfVlanInterfaceIfIndex':hpnicfVlanInterfaceIfIndex,'hpnicfifIsolateMappingTable':hpnicfifIsolateMappingTable,'hpnicfifIsolateMappingEntry':hpnicfifIsolateMappingEntry,_L:hpnicfifIsolatePrimaryVlanID,'hpnicfifIsolateSecondaryVlanlistLow':hpnicfifIsolateSecondaryVlanlistLow,'hpnicfifIsolateSecondaryVlanlistHigh':hpnicfifIsolateSecondaryVlanlistHigh,'hpnicfVlanInterfaceAddrTable':hpnicfVlanInterfaceAddrTable,'hpnicfVlanInterfaceAddrEntry':hpnicfVlanInterfaceAddrEntry,_M:hpnicfVlanInterfaceIpIfIndex,_N:hpnicfVlanInterfaceIpAddr,'hpnicfVlanInterfaceIpMask':hpnicfVlanInterfaceIpMask,'hpnicfVlanInterfaceIpType':hpnicfVlanInterfaceIpType,'hpnicfVlanInterfaceIpRowStatus':hpnicfVlanInterfaceIpRowStatus,'hpnicfDot1qVlanBatchMIBTable':hpnicfDot1qVlanBatchMIBTable,'hpnicfDot1qVlanBatchMIBEntry':hpnicfDot1qVlanBatchMIBEntry,_O:hpnicfdot1qVlanBatchOperIndex,'hpnicfdot1qVlanBatchStartIndex':hpnicfdot1qVlanBatchStartIndex,'hpnicfdot1qVlanBatchEndIndex':hpnicfdot1qVlanBatchEndIndex,'hpnicfdot1qVlanBatchOperStatus':hpnicfdot1qVlanBatchOperStatus,'hpnicfdot1qVlanBatchRowStatus':hpnicfdot1qVlanBatchRowStatus,'hpnicfdot1qVlanBatchSetOperate':hpnicfdot1qVlanBatchSetOperate,'hpnicfifSuperVlanMappingTable':hpnicfifSuperVlanMappingTable,'hpnicfifSuperVlanMappingEntry':hpnicfifSuperVlanMappingEntry,_P:hpnicfifSuperVlanID,'hpnicfifSubVlanlistLow':hpnicfifSubVlanlistLow,'hpnicfifSubVlanlistHigh':hpnicfifSubVlanlistHigh,'hpnicfPrivateVlanMappingTable':hpnicfPrivateVlanMappingTable,'hpnicfPrivateVlanMappingEntry':hpnicfPrivateVlanMappingEntry,_Q:hpnicfPrimaryVlanID,'hpnicfSecondaryVlanlistLow':hpnicfSecondaryVlanlistLow,'hpnicfSecondaryVlanlistHigh':hpnicfSecondaryVlanlistHigh,'hpnicfLswVlanProtoObject':hpnicfLswVlanProtoObject,'hpnicfVLANMibGarpLeaveAllTime':hpnicfVLANMibGarpLeaveAllTime,'hpnicfvLANMibSwitchCountTable':hpnicfvLANMibSwitchCountTable,_R:hpnicfvLANMibSwitchCountEntry,'hpnicfVLANMibSwitchGMRPRXPkt':hpnicfVLANMibSwitchGMRPRXPkt,'hpnicfVLANMibSwitchGVRPRXPkt':hpnicfVLANMibSwitchGVRPRXPkt,'hpnicfVLANMibSwitchGMRPTXPkt':hpnicfVLANMibSwitchGMRPTXPkt,'hpnicfVLANMibSwitchGVRPTXPkt':hpnicfVLANMibSwitchGVRPTXPkt,'hpnicfVLANMibSwitchDiscardedPkt':hpnicfVLANMibSwitchDiscardedPkt,'hpnicfVLANMibSwitchGarpStatClear':hpnicfVLANMibSwitchGarpStatClear,'hpnicfvLANMibHoldTimeTable':hpnicfvLANMibHoldTimeTable,_S:hpnicfvLANMibHoldTimeEntry,'hpnicfVLANMibHoldTime':hpnicfVLANMibHoldTime})