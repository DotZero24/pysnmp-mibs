_X='swMSMVlanGroupProfAddrEnd'
_W='swMSMVlanGroupProfAddrStart'
_V='swMSMVlanGroupProfAddrType'
_U='swMSMVlanID'
_T='swISMVlanGroupProfAddrEnd'
_S='swISMVlanGroupProfAddrStart'
_R='swISMVlanGroupProfAddrType'
_Q='member-port'
_P='source-port'
_O='not-replace'
_N='system-ip'
_M='user-configure'
_L='swISMVlanID'
_K='swMSMVlanGroupProfName'
_J='swISMVlanGroupProfName'
_I='DisplayString'
_H='disabled'
_G='enabled'
_F='read-only'
_E='MCAST-VLAN-MIB'
_D='read-create'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dlink_common_mgmt,=mibBuilder.importSymbols('DLINK-ID-REC-MIB','dlink-common-mgmt')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_I,'PhysAddress','RowStatus','TextualConvention')
swMcastVlanMIB=ModuleIdentity((1,3,6,1,4,1,171,12,64))
class PortList(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_SwMcastVlanCtrl_ObjectIdentity=ObjectIdentity
swMcastVlanCtrl=_SwMcastVlanCtrl_ObjectIdentity((1,3,6,1,4,1,171,12,64,1))
class _SwISMVlanGlobalState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_SwISMVlanGlobalState_Type.__name__=_C
_SwISMVlanGlobalState_Object=MibScalar
swISMVlanGlobalState=_SwISMVlanGlobalState_Object((1,3,6,1,4,1,171,12,64,1,1),_SwISMVlanGlobalState_Type())
swISMVlanGlobalState.setMaxAccess(_B)
if mibBuilder.loadTexts:swISMVlanGlobalState.setStatus(_A)
class _SwMSMVlanGlobalState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_SwMSMVlanGlobalState_Type.__name__=_C
_SwMSMVlanGlobalState_Object=MibScalar
swMSMVlanGlobalState=_SwMSMVlanGlobalState_Object((1,3,6,1,4,1,171,12,64,1,2),_SwMSMVlanGlobalState_Type())
swMSMVlanGlobalState.setMaxAccess(_B)
if mibBuilder.loadTexts:swMSMVlanGlobalState.setStatus(_A)
class _SwISMVlanForwardUnmatchedState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_SwISMVlanForwardUnmatchedState_Type.__name__=_C
_SwISMVlanForwardUnmatchedState_Object=MibScalar
swISMVlanForwardUnmatchedState=_SwISMVlanForwardUnmatchedState_Object((1,3,6,1,4,1,171,12,64,1,3),_SwISMVlanForwardUnmatchedState_Type())
swISMVlanForwardUnmatchedState.setMaxAccess(_B)
if mibBuilder.loadTexts:swISMVlanForwardUnmatchedState.setStatus(_A)
class _SwMSMVlanForwardUnmatchedState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_SwMSMVlanForwardUnmatchedState_Type.__name__=_C
_SwMSMVlanForwardUnmatchedState_Object=MibScalar
swMSMVlanForwardUnmatchedState=_SwMSMVlanForwardUnmatchedState_Object((1,3,6,1,4,1,171,12,64,1,4),_SwMSMVlanForwardUnmatchedState_Type())
swMSMVlanForwardUnmatchedState.setMaxAccess(_B)
if mibBuilder.loadTexts:swMSMVlanForwardUnmatchedState.setStatus(_A)
class _SwISMVlanAutoAssignVLANState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_SwISMVlanAutoAssignVLANState_Type.__name__=_C
_SwISMVlanAutoAssignVLANState_Object=MibScalar
swISMVlanAutoAssignVLANState=_SwISMVlanAutoAssignVLANState_Object((1,3,6,1,4,1,171,12,64,1,5),_SwISMVlanAutoAssignVLANState_Type())
swISMVlanAutoAssignVLANState.setMaxAccess(_B)
if mibBuilder.loadTexts:swISMVlanAutoAssignVLANState.setStatus(_A)
class _SwMSMVlanAutoAssignVLANState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_SwMSMVlanAutoAssignVLANState_Type.__name__=_C
_SwMSMVlanAutoAssignVLANState_Object=MibScalar
swMSMVlanAutoAssignVLANState=_SwMSMVlanAutoAssignVLANState_Object((1,3,6,1,4,1,171,12,64,1,6),_SwMSMVlanAutoAssignVLANState_Type())
swMSMVlanAutoAssignVLANState.setMaxAccess(_B)
if mibBuilder.loadTexts:swMSMVlanAutoAssignVLANState.setStatus(_A)
_SwMcastVlanInfo_ObjectIdentity=ObjectIdentity
swMcastVlanInfo=_SwMcastVlanInfo_ObjectIdentity((1,3,6,1,4,1,171,12,64,2))
_SwMcastVlanMgmt_ObjectIdentity=ObjectIdentity
swMcastVlanMgmt=_SwMcastVlanMgmt_ObjectIdentity((1,3,6,1,4,1,171,12,64,3))
_SwISMVlanTable_Object=MibTable
swISMVlanTable=_SwISMVlanTable_Object((1,3,6,1,4,1,171,12,64,3,1))
if mibBuilder.loadTexts:swISMVlanTable.setStatus(_A)
_SwISMVlanEntry_Object=MibTableRow
swISMVlanEntry=_SwISMVlanEntry_Object((1,3,6,1,4,1,171,12,64,3,1,1))
swISMVlanEntry.setIndexNames((0,_E,_L))
if mibBuilder.loadTexts:swISMVlanEntry.setStatus(_A)
class _SwISMVlanID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,4094))
_SwISMVlanID_Type.__name__=_C
_SwISMVlanID_Object=MibTableColumn
swISMVlanID=_SwISMVlanID_Object((1,3,6,1,4,1,171,12,64,3,1,1,1),_SwISMVlanID_Type())
swISMVlanID.setMaxAccess(_F)
if mibBuilder.loadTexts:swISMVlanID.setStatus(_A)
class _SwISMVlanName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SwISMVlanName_Type.__name__=_I
_SwISMVlanName_Object=MibTableColumn
swISMVlanName=_SwISMVlanName_Object((1,3,6,1,4,1,171,12,64,3,1,1,2),_SwISMVlanName_Type())
swISMVlanName.setMaxAccess(_D)
if mibBuilder.loadTexts:swISMVlanName.setStatus(_A)
_SwISMVlanSourcePort_Type=PortList
_SwISMVlanSourcePort_Object=MibTableColumn
swISMVlanSourcePort=_SwISMVlanSourcePort_Object((1,3,6,1,4,1,171,12,64,3,1,1,3),_SwISMVlanSourcePort_Type())
swISMVlanSourcePort.setMaxAccess(_B)
if mibBuilder.loadTexts:swISMVlanSourcePort.setStatus(_A)
_SwISMVlanMemberPort_Type=PortList
_SwISMVlanMemberPort_Object=MibTableColumn
swISMVlanMemberPort=_SwISMVlanMemberPort_Object((1,3,6,1,4,1,171,12,64,3,1,1,4),_SwISMVlanMemberPort_Type())
swISMVlanMemberPort.setMaxAccess(_B)
if mibBuilder.loadTexts:swISMVlanMemberPort.setStatus(_A)
_SwISMVlanTagMemberPort_Type=PortList
_SwISMVlanTagMemberPort_Object=MibTableColumn
swISMVlanTagMemberPort=_SwISMVlanTagMemberPort_Object((1,3,6,1,4,1,171,12,64,3,1,1,5),_SwISMVlanTagMemberPort_Type())
swISMVlanTagMemberPort.setMaxAccess(_B)
if mibBuilder.loadTexts:swISMVlanTagMemberPort.setStatus(_A)
_SwISMVlanUntagSourcePort_Type=PortList
_SwISMVlanUntagSourcePort_Object=MibTableColumn
swISMVlanUntagSourcePort=_SwISMVlanUntagSourcePort_Object((1,3,6,1,4,1,171,12,64,3,1,1,6),_SwISMVlanUntagSourcePort_Type())
swISMVlanUntagSourcePort.setMaxAccess(_B)
if mibBuilder.loadTexts:swISMVlanUntagSourcePort.setStatus(_A)
class _SwISMVlanState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_SwISMVlanState_Type.__name__=_C
_SwISMVlanState_Object=MibTableColumn
swISMVlanState=_SwISMVlanState_Object((1,3,6,1,4,1,171,12,64,3,1,1,7),_SwISMVlanState_Type())
swISMVlanState.setMaxAccess(_B)
if mibBuilder.loadTexts:swISMVlanState.setStatus(_A)
_SwISMVlanRepSourceAddrType_Type=InetAddressType
_SwISMVlanRepSourceAddrType_Object=MibTableColumn
swISMVlanRepSourceAddrType=_SwISMVlanRepSourceAddrType_Object((1,3,6,1,4,1,171,12,64,3,1,1,8),_SwISMVlanRepSourceAddrType_Type())
swISMVlanRepSourceAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:swISMVlanRepSourceAddrType.setStatus(_A)
_SwISMVlanRepSourceAddr_Type=InetAddress
_SwISMVlanRepSourceAddr_Object=MibTableColumn
swISMVlanRepSourceAddr=_SwISMVlanRepSourceAddr_Object((1,3,6,1,4,1,171,12,64,3,1,1,9),_SwISMVlanRepSourceAddr_Type())
swISMVlanRepSourceAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:swISMVlanRepSourceAddr.setStatus(_A)
class _SwISMVlanRemapPriority_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,7))
_SwISMVlanRemapPriority_Type.__name__=_C
_SwISMVlanRemapPriority_Object=MibTableColumn
swISMVlanRemapPriority=_SwISMVlanRemapPriority_Object((1,3,6,1,4,1,171,12,64,3,1,1,10),_SwISMVlanRemapPriority_Type())
swISMVlanRemapPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:swISMVlanRemapPriority.setStatus(_A)
class _SwISMVlanReplacePriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_SwISMVlanReplacePriority_Type.__name__=_C
_SwISMVlanReplacePriority_Object=MibTableColumn
swISMVlanReplacePriority=_SwISMVlanReplacePriority_Object((1,3,6,1,4,1,171,12,64,3,1,1,11),_SwISMVlanReplacePriority_Type())
swISMVlanReplacePriority.setMaxAccess(_D)
if mibBuilder.loadTexts:swISMVlanReplacePriority.setStatus(_A)
_SwISMVlanProfileIDList_Type=DisplayString
_SwISMVlanProfileIDList_Object=MibTableColumn
swISMVlanProfileIDList=_SwISMVlanProfileIDList_Object((1,3,6,1,4,1,171,12,64,3,1,1,12),_SwISMVlanProfileIDList_Type())
swISMVlanProfileIDList.setMaxAccess(_B)
if mibBuilder.loadTexts:swISMVlanProfileIDList.setStatus(_A)
_SwISMVlanRowStatus_Type=RowStatus
_SwISMVlanRowStatus_Object=MibTableColumn
swISMVlanRowStatus=_SwISMVlanRowStatus_Object((1,3,6,1,4,1,171,12,64,3,1,1,13),_SwISMVlanRowStatus_Type())
swISMVlanRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:swISMVlanRowStatus.setStatus(_A)
class _SwISMVlanRepSourceAddrActionType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_M,1),(_N,2),(_O,3)))
_SwISMVlanRepSourceAddrActionType_Type.__name__=_C
_SwISMVlanRepSourceAddrActionType_Object=MibTableColumn
swISMVlanRepSourceAddrActionType=_SwISMVlanRepSourceAddrActionType_Object((1,3,6,1,4,1,171,12,64,3,1,1,14),_SwISMVlanRepSourceAddrActionType_Type())
swISMVlanRepSourceAddrActionType.setMaxAccess(_D)
if mibBuilder.loadTexts:swISMVlanRepSourceAddrActionType.setStatus(_A)
class _SwISMVlanRepSourceAddrFromPorts_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_P,1),(_Q,2),('both',3)))
_SwISMVlanRepSourceAddrFromPorts_Type.__name__=_C
_SwISMVlanRepSourceAddrFromPorts_Object=MibTableColumn
swISMVlanRepSourceAddrFromPorts=_SwISMVlanRepSourceAddrFromPorts_Object((1,3,6,1,4,1,171,12,64,3,1,1,15),_SwISMVlanRepSourceAddrFromPorts_Type())
swISMVlanRepSourceAddrFromPorts.setMaxAccess(_D)
if mibBuilder.loadTexts:swISMVlanRepSourceAddrFromPorts.setStatus(_A)
class _SwISMVlanCustomerVlanID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_SwISMVlanCustomerVlanID_Type.__name__=_C
_SwISMVlanCustomerVlanID_Object=MibTableColumn
swISMVlanCustomerVlanID=_SwISMVlanCustomerVlanID_Object((1,3,6,1,4,1,171,12,64,3,1,1,16),_SwISMVlanCustomerVlanID_Type())
swISMVlanCustomerVlanID.setMaxAccess(_D)
if mibBuilder.loadTexts:swISMVlanCustomerVlanID.setStatus(_A)
_SwISMVlanGroupProfTable_Object=MibTable
swISMVlanGroupProfTable=_SwISMVlanGroupProfTable_Object((1,3,6,1,4,1,171,12,64,3,2))
if mibBuilder.loadTexts:swISMVlanGroupProfTable.setStatus(_A)
_SwISMVlanGroupProfEntry_Object=MibTableRow
swISMVlanGroupProfEntry=_SwISMVlanGroupProfEntry_Object((1,3,6,1,4,1,171,12,64,3,2,1))
swISMVlanGroupProfEntry.setIndexNames((0,_E,_J))
if mibBuilder.loadTexts:swISMVlanGroupProfEntry.setStatus(_A)
_SwISMVlanGroupProfName_Type=DisplayString
_SwISMVlanGroupProfName_Object=MibTableColumn
swISMVlanGroupProfName=_SwISMVlanGroupProfName_Object((1,3,6,1,4,1,171,12,64,3,2,1,1),_SwISMVlanGroupProfName_Type())
swISMVlanGroupProfName.setMaxAccess(_F)
if mibBuilder.loadTexts:swISMVlanGroupProfName.setStatus(_A)
_SwISMVlanGroupProfID_Type=Integer32
_SwISMVlanGroupProfID_Object=MibTableColumn
swISMVlanGroupProfID=_SwISMVlanGroupProfID_Object((1,3,6,1,4,1,171,12,64,3,2,1,2),_SwISMVlanGroupProfID_Type())
swISMVlanGroupProfID.setMaxAccess(_F)
if mibBuilder.loadTexts:swISMVlanGroupProfID.setStatus(_A)
_SwISMVlanGroupProfStatus_Type=RowStatus
_SwISMVlanGroupProfStatus_Object=MibTableColumn
swISMVlanGroupProfStatus=_SwISMVlanGroupProfStatus_Object((1,3,6,1,4,1,171,12,64,3,2,1,3),_SwISMVlanGroupProfStatus_Type())
swISMVlanGroupProfStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:swISMVlanGroupProfStatus.setStatus(_A)
_SwISMVlanGroupProfAddrTable_Object=MibTable
swISMVlanGroupProfAddrTable=_SwISMVlanGroupProfAddrTable_Object((1,3,6,1,4,1,171,12,64,3,3))
if mibBuilder.loadTexts:swISMVlanGroupProfAddrTable.setStatus(_A)
_SwISMVlanGroupProfAddrEntry_Object=MibTableRow
swISMVlanGroupProfAddrEntry=_SwISMVlanGroupProfAddrEntry_Object((1,3,6,1,4,1,171,12,64,3,3,1))
swISMVlanGroupProfAddrEntry.setIndexNames((0,_E,_J),(0,_E,_R),(0,_E,_S),(0,_E,_T))
if mibBuilder.loadTexts:swISMVlanGroupProfAddrEntry.setStatus(_A)
_SwISMVlanGroupProfAddrType_Type=InetAddressType
_SwISMVlanGroupProfAddrType_Object=MibTableColumn
swISMVlanGroupProfAddrType=_SwISMVlanGroupProfAddrType_Object((1,3,6,1,4,1,171,12,64,3,3,1,1),_SwISMVlanGroupProfAddrType_Type())
swISMVlanGroupProfAddrType.setMaxAccess(_F)
if mibBuilder.loadTexts:swISMVlanGroupProfAddrType.setStatus(_A)
_SwISMVlanGroupProfAddrStart_Type=InetAddress
_SwISMVlanGroupProfAddrStart_Object=MibTableColumn
swISMVlanGroupProfAddrStart=_SwISMVlanGroupProfAddrStart_Object((1,3,6,1,4,1,171,12,64,3,3,1,2),_SwISMVlanGroupProfAddrStart_Type())
swISMVlanGroupProfAddrStart.setMaxAccess(_F)
if mibBuilder.loadTexts:swISMVlanGroupProfAddrStart.setStatus(_A)
_SwISMVlanGroupProfAddrEnd_Type=InetAddress
_SwISMVlanGroupProfAddrEnd_Object=MibTableColumn
swISMVlanGroupProfAddrEnd=_SwISMVlanGroupProfAddrEnd_Object((1,3,6,1,4,1,171,12,64,3,3,1,3),_SwISMVlanGroupProfAddrEnd_Type())
swISMVlanGroupProfAddrEnd.setMaxAccess(_F)
if mibBuilder.loadTexts:swISMVlanGroupProfAddrEnd.setStatus(_A)
_SwISMVlanGroupProfAddrStatus_Type=RowStatus
_SwISMVlanGroupProfAddrStatus_Object=MibTableColumn
swISMVlanGroupProfAddrStatus=_SwISMVlanGroupProfAddrStatus_Object((1,3,6,1,4,1,171,12,64,3,3,1,4),_SwISMVlanGroupProfAddrStatus_Type())
swISMVlanGroupProfAddrStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:swISMVlanGroupProfAddrStatus.setStatus(_A)
_SwMSMVlanTable_Object=MibTable
swMSMVlanTable=_SwMSMVlanTable_Object((1,3,6,1,4,1,171,12,64,3,4))
if mibBuilder.loadTexts:swMSMVlanTable.setStatus(_A)
_SwMSMVlanEntry_Object=MibTableRow
swMSMVlanEntry=_SwMSMVlanEntry_Object((1,3,6,1,4,1,171,12,64,3,4,1))
swMSMVlanEntry.setIndexNames((0,_E,_U))
if mibBuilder.loadTexts:swMSMVlanEntry.setStatus(_A)
class _SwMSMVlanID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,4094))
_SwMSMVlanID_Type.__name__=_C
_SwMSMVlanID_Object=MibTableColumn
swMSMVlanID=_SwMSMVlanID_Object((1,3,6,1,4,1,171,12,64,3,4,1,1),_SwMSMVlanID_Type())
swMSMVlanID.setMaxAccess(_F)
if mibBuilder.loadTexts:swMSMVlanID.setStatus(_A)
class _SwMSMVlanName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SwMSMVlanName_Type.__name__=_I
_SwMSMVlanName_Object=MibTableColumn
swMSMVlanName=_SwMSMVlanName_Object((1,3,6,1,4,1,171,12,64,3,4,1,2),_SwMSMVlanName_Type())
swMSMVlanName.setMaxAccess(_D)
if mibBuilder.loadTexts:swMSMVlanName.setStatus(_A)
_SwMSMVlanSourcePort_Type=PortList
_SwMSMVlanSourcePort_Object=MibTableColumn
swMSMVlanSourcePort=_SwMSMVlanSourcePort_Object((1,3,6,1,4,1,171,12,64,3,4,1,3),_SwMSMVlanSourcePort_Type())
swMSMVlanSourcePort.setMaxAccess(_B)
if mibBuilder.loadTexts:swMSMVlanSourcePort.setStatus(_A)
_SwMSMVlanMemberPort_Type=PortList
_SwMSMVlanMemberPort_Object=MibTableColumn
swMSMVlanMemberPort=_SwMSMVlanMemberPort_Object((1,3,6,1,4,1,171,12,64,3,4,1,4),_SwMSMVlanMemberPort_Type())
swMSMVlanMemberPort.setMaxAccess(_B)
if mibBuilder.loadTexts:swMSMVlanMemberPort.setStatus(_A)
_SwMSMVlanTagMemberPort_Type=PortList
_SwMSMVlanTagMemberPort_Object=MibTableColumn
swMSMVlanTagMemberPort=_SwMSMVlanTagMemberPort_Object((1,3,6,1,4,1,171,12,64,3,4,1,5),_SwMSMVlanTagMemberPort_Type())
swMSMVlanTagMemberPort.setMaxAccess(_B)
if mibBuilder.loadTexts:swMSMVlanTagMemberPort.setStatus(_A)
_SwMSMVlanUntagSourcePort_Type=PortList
_SwMSMVlanUntagSourcePort_Object=MibTableColumn
swMSMVlanUntagSourcePort=_SwMSMVlanUntagSourcePort_Object((1,3,6,1,4,1,171,12,64,3,4,1,6),_SwMSMVlanUntagSourcePort_Type())
swMSMVlanUntagSourcePort.setMaxAccess(_B)
if mibBuilder.loadTexts:swMSMVlanUntagSourcePort.setStatus(_A)
class _SwMSMVlanState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_SwMSMVlanState_Type.__name__=_C
_SwMSMVlanState_Object=MibTableColumn
swMSMVlanState=_SwMSMVlanState_Object((1,3,6,1,4,1,171,12,64,3,4,1,7),_SwMSMVlanState_Type())
swMSMVlanState.setMaxAccess(_B)
if mibBuilder.loadTexts:swMSMVlanState.setStatus(_A)
_SwMSMVlanRepSourceAddrType_Type=InetAddressType
_SwMSMVlanRepSourceAddrType_Object=MibTableColumn
swMSMVlanRepSourceAddrType=_SwMSMVlanRepSourceAddrType_Object((1,3,6,1,4,1,171,12,64,3,4,1,8),_SwMSMVlanRepSourceAddrType_Type())
swMSMVlanRepSourceAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:swMSMVlanRepSourceAddrType.setStatus(_A)
_SwMSMVlanRepSourceAddr_Type=InetAddress
_SwMSMVlanRepSourceAddr_Object=MibTableColumn
swMSMVlanRepSourceAddr=_SwMSMVlanRepSourceAddr_Object((1,3,6,1,4,1,171,12,64,3,4,1,9),_SwMSMVlanRepSourceAddr_Type())
swMSMVlanRepSourceAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:swMSMVlanRepSourceAddr.setStatus(_A)
class _SwMSMVlanRemapPriority_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,7))
_SwMSMVlanRemapPriority_Type.__name__=_C
_SwMSMVlanRemapPriority_Object=MibTableColumn
swMSMVlanRemapPriority=_SwMSMVlanRemapPriority_Object((1,3,6,1,4,1,171,12,64,3,4,1,10),_SwMSMVlanRemapPriority_Type())
swMSMVlanRemapPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:swMSMVlanRemapPriority.setStatus(_A)
class _SwMSMVlanReplacePriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_SwMSMVlanReplacePriority_Type.__name__=_C
_SwMSMVlanReplacePriority_Object=MibTableColumn
swMSMVlanReplacePriority=_SwMSMVlanReplacePriority_Object((1,3,6,1,4,1,171,12,64,3,4,1,11),_SwMSMVlanReplacePriority_Type())
swMSMVlanReplacePriority.setMaxAccess(_D)
if mibBuilder.loadTexts:swMSMVlanReplacePriority.setStatus(_A)
_SwMSMVlanProfileIDList_Type=DisplayString
_SwMSMVlanProfileIDList_Object=MibTableColumn
swMSMVlanProfileIDList=_SwMSMVlanProfileIDList_Object((1,3,6,1,4,1,171,12,64,3,4,1,12),_SwMSMVlanProfileIDList_Type())
swMSMVlanProfileIDList.setMaxAccess(_B)
if mibBuilder.loadTexts:swMSMVlanProfileIDList.setStatus(_A)
_SwMSMVlanRowStatus_Type=RowStatus
_SwMSMVlanRowStatus_Object=MibTableColumn
swMSMVlanRowStatus=_SwMSMVlanRowStatus_Object((1,3,6,1,4,1,171,12,64,3,4,1,13),_SwMSMVlanRowStatus_Type())
swMSMVlanRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:swMSMVlanRowStatus.setStatus(_A)
class _SwMSMVlanRepSourceAddrActionType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_M,1),(_N,2),(_O,3)))
_SwMSMVlanRepSourceAddrActionType_Type.__name__=_C
_SwMSMVlanRepSourceAddrActionType_Object=MibTableColumn
swMSMVlanRepSourceAddrActionType=_SwMSMVlanRepSourceAddrActionType_Object((1,3,6,1,4,1,171,12,64,3,4,1,14),_SwMSMVlanRepSourceAddrActionType_Type())
swMSMVlanRepSourceAddrActionType.setMaxAccess(_D)
if mibBuilder.loadTexts:swMSMVlanRepSourceAddrActionType.setStatus(_A)
class _SwMSMVlanRepSourceAddrFromPorts_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_P,1),(_Q,2),('both',3)))
_SwMSMVlanRepSourceAddrFromPorts_Type.__name__=_C
_SwMSMVlanRepSourceAddrFromPorts_Object=MibTableColumn
swMSMVlanRepSourceAddrFromPorts=_SwMSMVlanRepSourceAddrFromPorts_Object((1,3,6,1,4,1,171,12,64,3,4,1,15),_SwMSMVlanRepSourceAddrFromPorts_Type())
swMSMVlanRepSourceAddrFromPorts.setMaxAccess(_D)
if mibBuilder.loadTexts:swMSMVlanRepSourceAddrFromPorts.setStatus(_A)
class _SwMSMVlanCustomerVlanID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_SwMSMVlanCustomerVlanID_Type.__name__=_C
_SwMSMVlanCustomerVlanID_Object=MibTableColumn
swMSMVlanCustomerVlanID=_SwMSMVlanCustomerVlanID_Object((1,3,6,1,4,1,171,12,64,3,4,1,16),_SwMSMVlanCustomerVlanID_Type())
swMSMVlanCustomerVlanID.setMaxAccess(_D)
if mibBuilder.loadTexts:swMSMVlanCustomerVlanID.setStatus(_A)
_SwMSMVlanGroupProfTable_Object=MibTable
swMSMVlanGroupProfTable=_SwMSMVlanGroupProfTable_Object((1,3,6,1,4,1,171,12,64,3,5))
if mibBuilder.loadTexts:swMSMVlanGroupProfTable.setStatus(_A)
_SwMSMVlanGroupProfEntry_Object=MibTableRow
swMSMVlanGroupProfEntry=_SwMSMVlanGroupProfEntry_Object((1,3,6,1,4,1,171,12,64,3,5,1))
swMSMVlanGroupProfEntry.setIndexNames((0,_E,_K))
if mibBuilder.loadTexts:swMSMVlanGroupProfEntry.setStatus(_A)
_SwMSMVlanGroupProfName_Type=DisplayString
_SwMSMVlanGroupProfName_Object=MibTableColumn
swMSMVlanGroupProfName=_SwMSMVlanGroupProfName_Object((1,3,6,1,4,1,171,12,64,3,5,1,1),_SwMSMVlanGroupProfName_Type())
swMSMVlanGroupProfName.setMaxAccess(_F)
if mibBuilder.loadTexts:swMSMVlanGroupProfName.setStatus(_A)
_SwMSMVlanGroupProfID_Type=Integer32
_SwMSMVlanGroupProfID_Object=MibTableColumn
swMSMVlanGroupProfID=_SwMSMVlanGroupProfID_Object((1,3,6,1,4,1,171,12,64,3,5,1,2),_SwMSMVlanGroupProfID_Type())
swMSMVlanGroupProfID.setMaxAccess(_F)
if mibBuilder.loadTexts:swMSMVlanGroupProfID.setStatus(_A)
_SwMSMVlanGroupProfStatus_Type=RowStatus
_SwMSMVlanGroupProfStatus_Object=MibTableColumn
swMSMVlanGroupProfStatus=_SwMSMVlanGroupProfStatus_Object((1,3,6,1,4,1,171,12,64,3,5,1,3),_SwMSMVlanGroupProfStatus_Type())
swMSMVlanGroupProfStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:swMSMVlanGroupProfStatus.setStatus(_A)
_SwMSMVlanGroupProfAddrTable_Object=MibTable
swMSMVlanGroupProfAddrTable=_SwMSMVlanGroupProfAddrTable_Object((1,3,6,1,4,1,171,12,64,3,6))
if mibBuilder.loadTexts:swMSMVlanGroupProfAddrTable.setStatus(_A)
_SwMSMVlanGroupProfAddrEntry_Object=MibTableRow
swMSMVlanGroupProfAddrEntry=_SwMSMVlanGroupProfAddrEntry_Object((1,3,6,1,4,1,171,12,64,3,6,1))
swMSMVlanGroupProfAddrEntry.setIndexNames((0,_E,_K),(0,_E,_V),(0,_E,_W),(0,_E,_X))
if mibBuilder.loadTexts:swMSMVlanGroupProfAddrEntry.setStatus(_A)
_SwMSMVlanGroupProfAddrType_Type=InetAddressType
_SwMSMVlanGroupProfAddrType_Object=MibTableColumn
swMSMVlanGroupProfAddrType=_SwMSMVlanGroupProfAddrType_Object((1,3,6,1,4,1,171,12,64,3,6,1,1),_SwMSMVlanGroupProfAddrType_Type())
swMSMVlanGroupProfAddrType.setMaxAccess(_F)
if mibBuilder.loadTexts:swMSMVlanGroupProfAddrType.setStatus(_A)
_SwMSMVlanGroupProfAddrStart_Type=InetAddress
_SwMSMVlanGroupProfAddrStart_Object=MibTableColumn
swMSMVlanGroupProfAddrStart=_SwMSMVlanGroupProfAddrStart_Object((1,3,6,1,4,1,171,12,64,3,6,1,2),_SwMSMVlanGroupProfAddrStart_Type())
swMSMVlanGroupProfAddrStart.setMaxAccess(_F)
if mibBuilder.loadTexts:swMSMVlanGroupProfAddrStart.setStatus(_A)
_SwMSMVlanGroupProfAddrEnd_Type=InetAddress
_SwMSMVlanGroupProfAddrEnd_Object=MibTableColumn
swMSMVlanGroupProfAddrEnd=_SwMSMVlanGroupProfAddrEnd_Object((1,3,6,1,4,1,171,12,64,3,6,1,3),_SwMSMVlanGroupProfAddrEnd_Type())
swMSMVlanGroupProfAddrEnd.setMaxAccess(_F)
if mibBuilder.loadTexts:swMSMVlanGroupProfAddrEnd.setStatus(_A)
_SwMSMVlanGroupProfAddrStatus_Type=RowStatus
_SwMSMVlanGroupProfAddrStatus_Object=MibTableColumn
swMSMVlanGroupProfAddrStatus=_SwMSMVlanGroupProfAddrStatus_Object((1,3,6,1,4,1,171,12,64,3,6,1,4),_SwMSMVlanGroupProfAddrStatus_Type())
swMSMVlanGroupProfAddrStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:swMSMVlanGroupProfAddrStatus.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'PortList':PortList,'swMcastVlanMIB':swMcastVlanMIB,'swMcastVlanCtrl':swMcastVlanCtrl,'swISMVlanGlobalState':swISMVlanGlobalState,'swMSMVlanGlobalState':swMSMVlanGlobalState,'swISMVlanForwardUnmatchedState':swISMVlanForwardUnmatchedState,'swMSMVlanForwardUnmatchedState':swMSMVlanForwardUnmatchedState,'swISMVlanAutoAssignVLANState':swISMVlanAutoAssignVLANState,'swMSMVlanAutoAssignVLANState':swMSMVlanAutoAssignVLANState,'swMcastVlanInfo':swMcastVlanInfo,'swMcastVlanMgmt':swMcastVlanMgmt,'swISMVlanTable':swISMVlanTable,'swISMVlanEntry':swISMVlanEntry,_L:swISMVlanID,'swISMVlanName':swISMVlanName,'swISMVlanSourcePort':swISMVlanSourcePort,'swISMVlanMemberPort':swISMVlanMemberPort,'swISMVlanTagMemberPort':swISMVlanTagMemberPort,'swISMVlanUntagSourcePort':swISMVlanUntagSourcePort,'swISMVlanState':swISMVlanState,'swISMVlanRepSourceAddrType':swISMVlanRepSourceAddrType,'swISMVlanRepSourceAddr':swISMVlanRepSourceAddr,'swISMVlanRemapPriority':swISMVlanRemapPriority,'swISMVlanReplacePriority':swISMVlanReplacePriority,'swISMVlanProfileIDList':swISMVlanProfileIDList,'swISMVlanRowStatus':swISMVlanRowStatus,'swISMVlanRepSourceAddrActionType':swISMVlanRepSourceAddrActionType,'swISMVlanRepSourceAddrFromPorts':swISMVlanRepSourceAddrFromPorts,'swISMVlanCustomerVlanID':swISMVlanCustomerVlanID,'swISMVlanGroupProfTable':swISMVlanGroupProfTable,'swISMVlanGroupProfEntry':swISMVlanGroupProfEntry,_J:swISMVlanGroupProfName,'swISMVlanGroupProfID':swISMVlanGroupProfID,'swISMVlanGroupProfStatus':swISMVlanGroupProfStatus,'swISMVlanGroupProfAddrTable':swISMVlanGroupProfAddrTable,'swISMVlanGroupProfAddrEntry':swISMVlanGroupProfAddrEntry,_R:swISMVlanGroupProfAddrType,_S:swISMVlanGroupProfAddrStart,_T:swISMVlanGroupProfAddrEnd,'swISMVlanGroupProfAddrStatus':swISMVlanGroupProfAddrStatus,'swMSMVlanTable':swMSMVlanTable,'swMSMVlanEntry':swMSMVlanEntry,_U:swMSMVlanID,'swMSMVlanName':swMSMVlanName,'swMSMVlanSourcePort':swMSMVlanSourcePort,'swMSMVlanMemberPort':swMSMVlanMemberPort,'swMSMVlanTagMemberPort':swMSMVlanTagMemberPort,'swMSMVlanUntagSourcePort':swMSMVlanUntagSourcePort,'swMSMVlanState':swMSMVlanState,'swMSMVlanRepSourceAddrType':swMSMVlanRepSourceAddrType,'swMSMVlanRepSourceAddr':swMSMVlanRepSourceAddr,'swMSMVlanRemapPriority':swMSMVlanRemapPriority,'swMSMVlanReplacePriority':swMSMVlanReplacePriority,'swMSMVlanProfileIDList':swMSMVlanProfileIDList,'swMSMVlanRowStatus':swMSMVlanRowStatus,'swMSMVlanRepSourceAddrActionType':swMSMVlanRepSourceAddrActionType,'swMSMVlanRepSourceAddrFromPorts':swMSMVlanRepSourceAddrFromPorts,'swMSMVlanCustomerVlanID':swMSMVlanCustomerVlanID,'swMSMVlanGroupProfTable':swMSMVlanGroupProfTable,'swMSMVlanGroupProfEntry':swMSMVlanGroupProfEntry,_K:swMSMVlanGroupProfName,'swMSMVlanGroupProfID':swMSMVlanGroupProfID,'swMSMVlanGroupProfStatus':swMSMVlanGroupProfStatus,'swMSMVlanGroupProfAddrTable':swMSMVlanGroupProfAddrTable,'swMSMVlanGroupProfAddrEntry':swMSMVlanGroupProfAddrEntry,_V:swMSMVlanGroupProfAddrType,_W:swMSMVlanGroupProfAddrStart,_X:swMSMVlanGroupProfAddrEnd,'swMSMVlanGroupProfAddrStatus':swMSMVlanGroupProfAddrStatus})