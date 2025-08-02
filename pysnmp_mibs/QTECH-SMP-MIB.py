_w='qtechSMPFrameRelayMibGroup'
_v='qtechSMPPolicyMibGroup'
_u='qtechSMPClientMibGroup'
_t='qtechSMPServerMibGroup'
_s='qtechSMPArpAttackInterfaceIndex'
_r='qtechSMPArpAttackMac'
_q='qtechSMPArpAttackCriticalStatus'
_p='qtechSMPArpAttackStatus'
_o='qtechSMPArpAttackFrameContent'
_n='qtechSMPArpAttackInterfaceVlanID'
_m='qtechSMPArpAttackInterfacePort'
_l='qtechSMPArpAttackInterfaceSlot'
_k='qtechSMPArpAttackSubnetIPNum'
_j='qtechSMPArpAttackSubnetIP'
_i='qtechSMPFrameContent'
_h='qtechSMPFrameContentLength'
_g='qtechSMPSwitchInterfaceVLANID'
_f='qtechSMPSwitchInterfaceID'
_e='qtechSMPSwitchIP'
_d='qtechSMPFrameRelayDestVlan'
_c='qtechSMPFrameRelayDestPort'
_b='qtechSMPFrameRelayLength'
_a='qtechSMPFrameRelayContent'
_Z='qtechSMPPolicyName'
_Y='qtechSMPPolicyMask'
_X='qtechSMPPolicyContent'
_W='qtechSMPPolicyType'
_V='qtechSMPPolicyInstallPort'
_U='qtechSMPPolicyStatus'
_T='qtechSMPPolicyChecksum'
_S='qtechSMPPolicyDelete'
_R='qtechSMPEventSendSlice'
_Q='qtechSMPServerKey'
_P='qtechSMPServer'
_O='qtechEGUserIpAddr'
_N='qtechEGUserIpAddrType'
_M='qtechSMPPolicyGroupIndex'
_L='qtechSMPGroupIndex'
_K='DisplayString'
_J='qtechSMPPolicyIndex'
_I='qtechSMPFrameRelayIndex'
_H='Integer32'
_G='read-only'
_F='OctetString'
_E='accessible-for-notify'
_D='read-create'
_C='read-write'
_B='QTECH-SMP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
VlanId,=mibBuilder.importSymbols('Q-BRIDGE-MIB','VlanId')
qtechMgmt,=mibBuilder.importSymbols('QTECH-SMI','qtechMgmt')
Community,=mibBuilder.importSymbols('QTECH-SNMP-AGENT-MIB','Community')
ConfigStatus,IfIndex=mibBuilder.importSymbols('QTECH-TC','ConfigStatus','IfIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_K,'MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
qtechSMPMIB=ModuleIdentity((1,3,6,1,4,1,27514,1,1,10,2,39))
if mibBuilder.loadTexts:qtechSMPMIB.setRevisions(('2004-09-09 00:00',))
_QtechSMPMIBObjects_ObjectIdentity=ObjectIdentity
qtechSMPMIBObjects=_QtechSMPMIBObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,39,1))
_QtechSMPServer_Type=IpAddress
_QtechSMPServer_Object=MibScalar
qtechSMPServer=_QtechSMPServer_Object((1,3,6,1,4,1,27514,1,1,10,2,39,1,1),_QtechSMPServer_Type())
qtechSMPServer.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechSMPServer.setStatus(_A)
_QtechSMPServerKey_Type=Community
_QtechSMPServerKey_Object=MibScalar
qtechSMPServerKey=_QtechSMPServerKey_Object((1,3,6,1,4,1,27514,1,1,10,2,39,1,2),_QtechSMPServerKey_Type())
qtechSMPServerKey.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechSMPServerKey.setStatus(_A)
_QtechSMPEventSendSlice_Type=Unsigned32
_QtechSMPEventSendSlice_Object=MibScalar
qtechSMPEventSendSlice=_QtechSMPEventSendSlice_Object((1,3,6,1,4,1,27514,1,1,10,2,39,1,3),_QtechSMPEventSendSlice_Type())
qtechSMPEventSendSlice.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechSMPEventSendSlice.setStatus(_A)
_QtechSMPPolicyDelete_Type=Integer32
_QtechSMPPolicyDelete_Object=MibScalar
qtechSMPPolicyDelete=_QtechSMPPolicyDelete_Object((1,3,6,1,4,1,27514,1,1,10,2,39,1,4),_QtechSMPPolicyDelete_Type())
qtechSMPPolicyDelete.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechSMPPolicyDelete.setStatus(_A)
class _QtechSMPPolicyChecksum_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_QtechSMPPolicyChecksum_Type.__name__=_F
_QtechSMPPolicyChecksum_Object=MibScalar
qtechSMPPolicyChecksum=_QtechSMPPolicyChecksum_Object((1,3,6,1,4,1,27514,1,1,10,2,39,1,5),_QtechSMPPolicyChecksum_Type())
qtechSMPPolicyChecksum.setMaxAccess(_G)
if mibBuilder.loadTexts:qtechSMPPolicyChecksum.setStatus(_A)
_QtechSMPPolicyTimeout_Type=Unsigned32
_QtechSMPPolicyTimeout_Object=MibScalar
qtechSMPPolicyTimeout=_QtechSMPPolicyTimeout_Object((1,3,6,1,4,1,27514,1,1,10,2,39,1,6),_QtechSMPPolicyTimeout_Type())
qtechSMPPolicyTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechSMPPolicyTimeout.setStatus(_A)
_QtechSMPFrameRelayTable_Object=MibTable
qtechSMPFrameRelayTable=_QtechSMPFrameRelayTable_Object((1,3,6,1,4,1,27514,1,1,10,2,39,1,7))
if mibBuilder.loadTexts:qtechSMPFrameRelayTable.setStatus(_A)
_QtechSMPFrameRelayEntry_Object=MibTableRow
qtechSMPFrameRelayEntry=_QtechSMPFrameRelayEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,39,1,7,1))
qtechSMPFrameRelayEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:qtechSMPFrameRelayEntry.setStatus(_A)
_QtechSMPFrameRelayIndex_Type=Unsigned32
_QtechSMPFrameRelayIndex_Object=MibTableColumn
qtechSMPFrameRelayIndex=_QtechSMPFrameRelayIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,39,1,7,1,1),_QtechSMPFrameRelayIndex_Type())
qtechSMPFrameRelayIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:qtechSMPFrameRelayIndex.setStatus(_A)
class _QtechSMPFrameRelayContent_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_QtechSMPFrameRelayContent_Type.__name__=_F
_QtechSMPFrameRelayContent_Object=MibTableColumn
qtechSMPFrameRelayContent=_QtechSMPFrameRelayContent_Object((1,3,6,1,4,1,27514,1,1,10,2,39,1,7,1,2),_QtechSMPFrameRelayContent_Type())
qtechSMPFrameRelayContent.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechSMPFrameRelayContent.setStatus(_A)
_QtechSMPFrameRelayLength_Type=Unsigned32
_QtechSMPFrameRelayLength_Object=MibTableColumn
qtechSMPFrameRelayLength=_QtechSMPFrameRelayLength_Object((1,3,6,1,4,1,27514,1,1,10,2,39,1,7,1,3),_QtechSMPFrameRelayLength_Type())
qtechSMPFrameRelayLength.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechSMPFrameRelayLength.setStatus(_A)
_QtechSMPFrameRelayDestPort_Type=IfIndex
_QtechSMPFrameRelayDestPort_Object=MibTableColumn
qtechSMPFrameRelayDestPort=_QtechSMPFrameRelayDestPort_Object((1,3,6,1,4,1,27514,1,1,10,2,39,1,7,1,4),_QtechSMPFrameRelayDestPort_Type())
qtechSMPFrameRelayDestPort.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechSMPFrameRelayDestPort.setStatus(_A)
_QtechSMPFrameRelayDestVlan_Type=VlanId
_QtechSMPFrameRelayDestVlan_Object=MibTableColumn
qtechSMPFrameRelayDestVlan=_QtechSMPFrameRelayDestVlan_Object((1,3,6,1,4,1,27514,1,1,10,2,39,1,7,1,5),_QtechSMPFrameRelayDestVlan_Type())
qtechSMPFrameRelayDestVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechSMPFrameRelayDestVlan.setStatus(_A)
_QtechSMPPolicyTable_Object=MibTable
qtechSMPPolicyTable=_QtechSMPPolicyTable_Object((1,3,6,1,4,1,27514,1,1,10,2,39,1,8))
if mibBuilder.loadTexts:qtechSMPPolicyTable.setStatus(_A)
_QtechSMPPolicyEntry_Object=MibTableRow
qtechSMPPolicyEntry=_QtechSMPPolicyEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,39,1,8,1))
qtechSMPPolicyEntry.setIndexNames((0,_B,_L),(0,_B,_J))
if mibBuilder.loadTexts:qtechSMPPolicyEntry.setStatus(_A)
_QtechSMPGroupIndex_Type=Unsigned32
_QtechSMPGroupIndex_Object=MibTableColumn
qtechSMPGroupIndex=_QtechSMPGroupIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,39,1,8,1,1),_QtechSMPGroupIndex_Type())
qtechSMPGroupIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:qtechSMPGroupIndex.setStatus(_A)
_QtechSMPPolicyIndex_Type=Unsigned32
_QtechSMPPolicyIndex_Object=MibTableColumn
qtechSMPPolicyIndex=_QtechSMPPolicyIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,39,1,8,1,2),_QtechSMPPolicyIndex_Type())
qtechSMPPolicyIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:qtechSMPPolicyIndex.setStatus(_A)
_QtechSMPPolicyStatus_Type=ConfigStatus
_QtechSMPPolicyStatus_Object=MibTableColumn
qtechSMPPolicyStatus=_QtechSMPPolicyStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,39,1,8,1,3),_QtechSMPPolicyStatus_Type())
qtechSMPPolicyStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechSMPPolicyStatus.setStatus(_A)
_QtechSMPPolicyNumber_Type=Unsigned32
_QtechSMPPolicyNumber_Object=MibTableColumn
qtechSMPPolicyNumber=_QtechSMPPolicyNumber_Object((1,3,6,1,4,1,27514,1,1,10,2,39,1,8,1,4),_QtechSMPPolicyNumber_Type())
qtechSMPPolicyNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechSMPPolicyNumber.setStatus(_A)
_QtechSMPPolicyInstallPort_Type=IfIndex
_QtechSMPPolicyInstallPort_Object=MibTableColumn
qtechSMPPolicyInstallPort=_QtechSMPPolicyInstallPort_Object((1,3,6,1,4,1,27514,1,1,10,2,39,1,8,1,5),_QtechSMPPolicyInstallPort_Type())
qtechSMPPolicyInstallPort.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechSMPPolicyInstallPort.setStatus(_A)
class _QtechSMPPolicyType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('hi-isolate',1),('isolate',2),('blocked',3),('addrBind',4)))
_QtechSMPPolicyType_Type.__name__=_H
_QtechSMPPolicyType_Object=MibTableColumn
qtechSMPPolicyType=_QtechSMPPolicyType_Object((1,3,6,1,4,1,27514,1,1,10,2,39,1,8,1,6),_QtechSMPPolicyType_Type())
qtechSMPPolicyType.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechSMPPolicyType.setStatus(_A)
class _QtechSMPPolicyContent_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(80,80));fixedLength=80
_QtechSMPPolicyContent_Type.__name__=_F
_QtechSMPPolicyContent_Object=MibTableColumn
qtechSMPPolicyContent=_QtechSMPPolicyContent_Object((1,3,6,1,4,1,27514,1,1,10,2,39,1,8,1,7),_QtechSMPPolicyContent_Type())
qtechSMPPolicyContent.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechSMPPolicyContent.setStatus(_A)
class _QtechSMPPolicyMask_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(80,80));fixedLength=80
_QtechSMPPolicyMask_Type.__name__=_F
_QtechSMPPolicyMask_Object=MibTableColumn
qtechSMPPolicyMask=_QtechSMPPolicyMask_Object((1,3,6,1,4,1,27514,1,1,10,2,39,1,8,1,8),_QtechSMPPolicyMask_Type())
qtechSMPPolicyMask.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechSMPPolicyMask.setStatus(_A)
class _QtechSMPPolicyName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_QtechSMPPolicyName_Type.__name__=_K
_QtechSMPPolicyName_Object=MibTableColumn
qtechSMPPolicyName=_QtechSMPPolicyName_Object((1,3,6,1,4,1,27514,1,1,10,2,39,1,8,1,9),_QtechSMPPolicyName_Type())
qtechSMPPolicyName.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechSMPPolicyName.setStatus(_A)
_QtechSMPPolicyGroupTable_Object=MibTable
qtechSMPPolicyGroupTable=_QtechSMPPolicyGroupTable_Object((1,3,6,1,4,1,27514,1,1,10,2,39,1,9))
if mibBuilder.loadTexts:qtechSMPPolicyGroupTable.setStatus(_A)
_QtechSMPPolicyGroupEntry_Object=MibTableRow
qtechSMPPolicyGroupEntry=_QtechSMPPolicyGroupEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,39,1,9,1))
qtechSMPPolicyGroupEntry.setIndexNames((0,_B,_M))
if mibBuilder.loadTexts:qtechSMPPolicyGroupEntry.setStatus(_A)
_QtechSMPPolicyGroupIndex_Type=Unsigned32
_QtechSMPPolicyGroupIndex_Object=MibTableColumn
qtechSMPPolicyGroupIndex=_QtechSMPPolicyGroupIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,39,1,9,1,1),_QtechSMPPolicyGroupIndex_Type())
qtechSMPPolicyGroupIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:qtechSMPPolicyGroupIndex.setStatus(_A)
_QtechSMPPolicyGroupCount_Type=Unsigned32
_QtechSMPPolicyGroupCount_Object=MibTableColumn
qtechSMPPolicyGroupCount=_QtechSMPPolicyGroupCount_Object((1,3,6,1,4,1,27514,1,1,10,2,39,1,9,1,2),_QtechSMPPolicyGroupCount_Type())
qtechSMPPolicyGroupCount.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechSMPPolicyGroupCount.setStatus(_A)
class _QtechSMPPolicyGroupChecksum_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_QtechSMPPolicyGroupChecksum_Type.__name__=_F
_QtechSMPPolicyGroupChecksum_Object=MibTableColumn
qtechSMPPolicyGroupChecksum=_QtechSMPPolicyGroupChecksum_Object((1,3,6,1,4,1,27514,1,1,10,2,39,1,9,1,3),_QtechSMPPolicyGroupChecksum_Type())
qtechSMPPolicyGroupChecksum.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechSMPPolicyGroupChecksum.setStatus(_A)
_QtechSMPPolicyGroupStatus_Type=RowStatus
_QtechSMPPolicyGroupStatus_Object=MibTableColumn
qtechSMPPolicyGroupStatus=_QtechSMPPolicyGroupStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,39,1,9,1,4),_QtechSMPPolicyGroupStatus_Type())
qtechSMPPolicyGroupStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechSMPPolicyGroupStatus.setStatus(_A)
_QtechEGMIBObjects_ObjectIdentity=ObjectIdentity
qtechEGMIBObjects=_QtechEGMIBObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,39,2))
_QtechEGUserTable_Object=MibTable
qtechEGUserTable=_QtechEGUserTable_Object((1,3,6,1,4,1,27514,1,1,10,2,39,2,1))
if mibBuilder.loadTexts:qtechEGUserTable.setStatus(_A)
_QtechEGUserEntry_Object=MibTableRow
qtechEGUserEntry=_QtechEGUserEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,39,2,1,1))
qtechEGUserEntry.setIndexNames((0,_B,_N),(0,_B,_O))
if mibBuilder.loadTexts:qtechEGUserEntry.setStatus(_A)
_QtechEGUserIpAddrType_Type=InetAddressType
_QtechEGUserIpAddrType_Object=MibTableColumn
qtechEGUserIpAddrType=_QtechEGUserIpAddrType_Object((1,3,6,1,4,1,27514,1,1,10,2,39,2,1,1,1),_QtechEGUserIpAddrType_Type())
qtechEGUserIpAddrType.setMaxAccess(_G)
if mibBuilder.loadTexts:qtechEGUserIpAddrType.setStatus(_A)
_QtechEGUserIpAddr_Type=InetAddress
_QtechEGUserIpAddr_Object=MibTableColumn
qtechEGUserIpAddr=_QtechEGUserIpAddr_Object((1,3,6,1,4,1,27514,1,1,10,2,39,2,1,1,2),_QtechEGUserIpAddr_Type())
qtechEGUserIpAddr.setMaxAccess(_G)
if mibBuilder.loadTexts:qtechEGUserIpAddr.setStatus(_A)
class _QtechEGUserId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_QtechEGUserId_Type.__name__=_F
_QtechEGUserId_Object=MibTableColumn
qtechEGUserId=_QtechEGUserId_Object((1,3,6,1,4,1,27514,1,1,10,2,39,2,1,1,3),_QtechEGUserId_Type())
qtechEGUserId.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechEGUserId.setStatus(_A)
class _QtechEGUserName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_QtechEGUserName_Type.__name__=_F
_QtechEGUserName_Object=MibTableColumn
qtechEGUserName=_QtechEGUserName_Object((1,3,6,1,4,1,27514,1,1,10,2,39,2,1,1,4),_QtechEGUserName_Type())
qtechEGUserName.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechEGUserName.setStatus(_A)
class _QtechEGUserGroupName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_QtechEGUserGroupName_Type.__name__=_F
_QtechEGUserGroupName_Object=MibTableColumn
qtechEGUserGroupName=_QtechEGUserGroupName_Object((1,3,6,1,4,1,27514,1,1,10,2,39,2,1,1,5),_QtechEGUserGroupName_Type())
qtechEGUserGroupName.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechEGUserGroupName.setStatus(_A)
_QtechEGUserMac_Type=MacAddress
_QtechEGUserMac_Object=MibTableColumn
qtechEGUserMac=_QtechEGUserMac_Object((1,3,6,1,4,1,27514,1,1,10,2,39,2,1,1,6),_QtechEGUserMac_Type())
qtechEGUserMac.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechEGUserMac.setStatus(_A)
_QtechEGNasIp_Type=InetAddress
_QtechEGNasIp_Object=MibTableColumn
qtechEGNasIp=_QtechEGNasIp_Object((1,3,6,1,4,1,27514,1,1,10,2,39,2,1,1,7),_QtechEGNasIp_Type())
qtechEGNasIp.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechEGNasIp.setStatus(_A)
_QtechEGNasPort_Type=Gauge32
_QtechEGNasPort_Object=MibTableColumn
qtechEGNasPort=_QtechEGNasPort_Object((1,3,6,1,4,1,27514,1,1,10,2,39,2,1,1,8),_QtechEGNasPort_Type())
qtechEGNasPort.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechEGNasPort.setStatus(_A)
_QtechEGGatewayIp_Type=InetAddress
_QtechEGGatewayIp_Object=MibTableColumn
qtechEGGatewayIp=_QtechEGGatewayIp_Object((1,3,6,1,4,1,27514,1,1,10,2,39,2,1,1,9),_QtechEGGatewayIp_Type())
qtechEGGatewayIp.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechEGGatewayIp.setStatus(_A)
_QtechEGVlanId_Type=Gauge32
_QtechEGVlanId_Object=MibTableColumn
qtechEGVlanId=_QtechEGVlanId_Object((1,3,6,1,4,1,27514,1,1,10,2,39,2,1,1,10),_QtechEGVlanId_Type())
qtechEGVlanId.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechEGVlanId.setStatus(_A)
_QtechEGLoginTime_Type=OctetString
_QtechEGLoginTime_Object=MibTableColumn
qtechEGLoginTime=_QtechEGLoginTime_Object((1,3,6,1,4,1,27514,1,1,10,2,39,2,1,1,11),_QtechEGLoginTime_Type())
qtechEGLoginTime.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechEGLoginTime.setStatus(_A)
_QtechEGLogoutTime_Type=OctetString
_QtechEGLogoutTime_Object=MibTableColumn
qtechEGLogoutTime=_QtechEGLogoutTime_Object((1,3,6,1,4,1,27514,1,1,10,2,39,2,1,1,12),_QtechEGLogoutTime_Type())
qtechEGLogoutTime.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechEGLogoutTime.setStatus(_A)
_QtechEGMessageType_Type=Gauge32
_QtechEGMessageType_Object=MibTableColumn
qtechEGMessageType=_QtechEGMessageType_Object((1,3,6,1,4,1,27514,1,1,10,2,39,2,1,1,13),_QtechEGMessageType_Type())
qtechEGMessageType.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechEGMessageType.setStatus(_A)
_QtechEGUserStatus_Type=RowStatus
_QtechEGUserStatus_Object=MibTableColumn
qtechEGUserStatus=_QtechEGUserStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,39,2,1,1,14),_QtechEGUserStatus_Type())
qtechEGUserStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechEGUserStatus.setStatus(_A)
_QtechEGUserDelete_Type=Integer32
_QtechEGUserDelete_Object=MibScalar
qtechEGUserDelete=_QtechEGUserDelete_Object((1,3,6,1,4,1,27514,1,1,10,2,39,2,2),_QtechEGUserDelete_Type())
qtechEGUserDelete.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechEGUserDelete.setStatus(_A)
_QtechSMPMIBConformance_ObjectIdentity=ObjectIdentity
qtechSMPMIBConformance=_QtechSMPMIBConformance_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,39,3))
_QtechSMPMIBCompliances_ObjectIdentity=ObjectIdentity
qtechSMPMIBCompliances=_QtechSMPMIBCompliances_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,39,3,1))
_QtechSMPMIBGroups_ObjectIdentity=ObjectIdentity
qtechSMPMIBGroups=_QtechSMPMIBGroups_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,39,3,2))
_QtechSMPTraps_ObjectIdentity=ObjectIdentity
qtechSMPTraps=_QtechSMPTraps_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,39,65535))
_QtechSMPSwitchIP_Type=IpAddress
_QtechSMPSwitchIP_Object=MibScalar
qtechSMPSwitchIP=_QtechSMPSwitchIP_Object((1,3,6,1,4,1,27514,1,1,10,2,39,65535,1),_QtechSMPSwitchIP_Type())
qtechSMPSwitchIP.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechSMPSwitchIP.setStatus(_A)
_QtechSMPSwitchInterfaceID_Type=IfIndex
_QtechSMPSwitchInterfaceID_Object=MibScalar
qtechSMPSwitchInterfaceID=_QtechSMPSwitchInterfaceID_Object((1,3,6,1,4,1,27514,1,1,10,2,39,65535,2),_QtechSMPSwitchInterfaceID_Type())
qtechSMPSwitchInterfaceID.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechSMPSwitchInterfaceID.setStatus(_A)
_QtechSMPSwitchInterfaceVLANID_Type=VlanId
_QtechSMPSwitchInterfaceVLANID_Object=MibScalar
qtechSMPSwitchInterfaceVLANID=_QtechSMPSwitchInterfaceVLANID_Object((1,3,6,1,4,1,27514,1,1,10,2,39,65535,3),_QtechSMPSwitchInterfaceVLANID_Type())
qtechSMPSwitchInterfaceVLANID.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechSMPSwitchInterfaceVLANID.setStatus(_A)
_QtechSMPFrameContentLength_Type=Unsigned32
_QtechSMPFrameContentLength_Object=MibScalar
qtechSMPFrameContentLength=_QtechSMPFrameContentLength_Object((1,3,6,1,4,1,27514,1,1,10,2,39,65535,4),_QtechSMPFrameContentLength_Type())
qtechSMPFrameContentLength.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechSMPFrameContentLength.setStatus(_A)
class _QtechSMPFrameContent_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_QtechSMPFrameContent_Type.__name__=_F
_QtechSMPFrameContent_Object=MibScalar
qtechSMPFrameContent=_QtechSMPFrameContent_Object((1,3,6,1,4,1,27514,1,1,10,2,39,65535,5),_QtechSMPFrameContent_Type())
qtechSMPFrameContent.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechSMPFrameContent.setStatus(_A)
class _QtechSMPArpAttackSubnetIP_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_QtechSMPArpAttackSubnetIP_Type.__name__=_F
_QtechSMPArpAttackSubnetIP_Object=MibScalar
qtechSMPArpAttackSubnetIP=_QtechSMPArpAttackSubnetIP_Object((1,3,6,1,4,1,27514,1,1,10,2,39,65535,7),_QtechSMPArpAttackSubnetIP_Type())
qtechSMPArpAttackSubnetIP.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechSMPArpAttackSubnetIP.setStatus(_A)
_QtechSMPArpAttackSubnetIPNum_Type=Integer32
_QtechSMPArpAttackSubnetIPNum_Object=MibScalar
qtechSMPArpAttackSubnetIPNum=_QtechSMPArpAttackSubnetIPNum_Object((1,3,6,1,4,1,27514,1,1,10,2,39,65535,8),_QtechSMPArpAttackSubnetIPNum_Type())
qtechSMPArpAttackSubnetIPNum.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechSMPArpAttackSubnetIPNum.setStatus(_A)
_QtechSMPArpAttackInterfaceSlot_Type=Integer32
_QtechSMPArpAttackInterfaceSlot_Object=MibScalar
qtechSMPArpAttackInterfaceSlot=_QtechSMPArpAttackInterfaceSlot_Object((1,3,6,1,4,1,27514,1,1,10,2,39,65535,9),_QtechSMPArpAttackInterfaceSlot_Type())
qtechSMPArpAttackInterfaceSlot.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechSMPArpAttackInterfaceSlot.setStatus(_A)
_QtechSMPArpAttackInterfacePort_Type=Integer32
_QtechSMPArpAttackInterfacePort_Object=MibScalar
qtechSMPArpAttackInterfacePort=_QtechSMPArpAttackInterfacePort_Object((1,3,6,1,4,1,27514,1,1,10,2,39,65535,10),_QtechSMPArpAttackInterfacePort_Type())
qtechSMPArpAttackInterfacePort.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechSMPArpAttackInterfacePort.setStatus(_A)
_QtechSMPArpAttackInterfaceVlanID_Type=VlanId
_QtechSMPArpAttackInterfaceVlanID_Object=MibScalar
qtechSMPArpAttackInterfaceVlanID=_QtechSMPArpAttackInterfaceVlanID_Object((1,3,6,1,4,1,27514,1,1,10,2,39,65535,11),_QtechSMPArpAttackInterfaceVlanID_Type())
qtechSMPArpAttackInterfaceVlanID.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechSMPArpAttackInterfaceVlanID.setStatus(_A)
class _QtechSMPArpAttackFrameContent_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_QtechSMPArpAttackFrameContent_Type.__name__=_F
_QtechSMPArpAttackFrameContent_Object=MibScalar
qtechSMPArpAttackFrameContent=_QtechSMPArpAttackFrameContent_Object((1,3,6,1,4,1,27514,1,1,10,2,39,65535,12),_QtechSMPArpAttackFrameContent_Type())
qtechSMPArpAttackFrameContent.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechSMPArpAttackFrameContent.setStatus(_A)
_QtechSMPArpAttackStatus_Type=TruthValue
_QtechSMPArpAttackStatus_Object=MibScalar
qtechSMPArpAttackStatus=_QtechSMPArpAttackStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,39,65535,13),_QtechSMPArpAttackStatus_Type())
qtechSMPArpAttackStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechSMPArpAttackStatus.setStatus(_A)
class _QtechSMPArpAttackCriticalStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('critical',1),('emergencies',2)))
_QtechSMPArpAttackCriticalStatus_Type.__name__=_H
_QtechSMPArpAttackCriticalStatus_Object=MibScalar
qtechSMPArpAttackCriticalStatus=_QtechSMPArpAttackCriticalStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,39,65535,14),_QtechSMPArpAttackCriticalStatus_Type())
qtechSMPArpAttackCriticalStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechSMPArpAttackCriticalStatus.setStatus(_A)
_QtechSMPArpAttackMac_Type=MacAddress
_QtechSMPArpAttackMac_Object=MibScalar
qtechSMPArpAttackMac=_QtechSMPArpAttackMac_Object((1,3,6,1,4,1,27514,1,1,10,2,39,65535,15),_QtechSMPArpAttackMac_Type())
qtechSMPArpAttackMac.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechSMPArpAttackMac.setStatus(_A)
_QtechSMPArpAttackInterfaceIndex_Type=Integer32
_QtechSMPArpAttackInterfaceIndex_Object=MibScalar
qtechSMPArpAttackInterfaceIndex=_QtechSMPArpAttackInterfaceIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,39,65535,16),_QtechSMPArpAttackInterfaceIndex_Type())
qtechSMPArpAttackInterfaceIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechSMPArpAttackInterfaceIndex.setStatus(_A)
qtechSMPServerMibGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,39,3,2,1))
qtechSMPServerMibGroup.setObjects(*((_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:qtechSMPServerMibGroup.setStatus(_A)
qtechSMPClientMibGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,39,3,2,2))
qtechSMPClientMibGroup.setObjects((_B,_R))
if mibBuilder.loadTexts:qtechSMPClientMibGroup.setStatus(_A)
qtechSMPPolicyMibGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,39,3,2,3))
qtechSMPPolicyMibGroup.setObjects(*((_B,_S),(_B,_T),(_B,_J),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z)))
if mibBuilder.loadTexts:qtechSMPPolicyMibGroup.setStatus(_A)
qtechSMPFrameRelayMibGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,39,3,2,4))
qtechSMPFrameRelayMibGroup.setObjects(*((_B,_I),(_B,_a),(_B,_b),(_B,_c),(_B,_d)))
if mibBuilder.loadTexts:qtechSMPFrameRelayMibGroup.setStatus(_A)
qtechSMPFrameRelayTrap=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,39,65535,6))
qtechSMPFrameRelayTrap.setObjects(*((_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i)))
if mibBuilder.loadTexts:qtechSMPFrameRelayTrap.setStatus(_A)
qtechSMPArpAttackTrap=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,39,65535,17))
qtechSMPArpAttackTrap.setObjects(*((_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s)))
if mibBuilder.loadTexts:qtechSMPArpAttackTrap.setStatus(_A)
qtechDeviceMIBCompliance=ModuleCompliance((1,3,6,1,4,1,27514,1,1,10,2,39,3,1,1))
qtechDeviceMIBCompliance.setObjects(*((_B,_t),(_B,_u),(_B,_v),(_B,_w)))
if mibBuilder.loadTexts:qtechDeviceMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'qtechSMPMIB':qtechSMPMIB,'qtechSMPMIBObjects':qtechSMPMIBObjects,_P:qtechSMPServer,_Q:qtechSMPServerKey,_R:qtechSMPEventSendSlice,_S:qtechSMPPolicyDelete,_T:qtechSMPPolicyChecksum,'qtechSMPPolicyTimeout':qtechSMPPolicyTimeout,'qtechSMPFrameRelayTable':qtechSMPFrameRelayTable,'qtechSMPFrameRelayEntry':qtechSMPFrameRelayEntry,_I:qtechSMPFrameRelayIndex,_a:qtechSMPFrameRelayContent,_b:qtechSMPFrameRelayLength,_c:qtechSMPFrameRelayDestPort,_d:qtechSMPFrameRelayDestVlan,'qtechSMPPolicyTable':qtechSMPPolicyTable,'qtechSMPPolicyEntry':qtechSMPPolicyEntry,_L:qtechSMPGroupIndex,_J:qtechSMPPolicyIndex,_U:qtechSMPPolicyStatus,'qtechSMPPolicyNumber':qtechSMPPolicyNumber,_V:qtechSMPPolicyInstallPort,_W:qtechSMPPolicyType,_X:qtechSMPPolicyContent,_Y:qtechSMPPolicyMask,_Z:qtechSMPPolicyName,'qtechSMPPolicyGroupTable':qtechSMPPolicyGroupTable,'qtechSMPPolicyGroupEntry':qtechSMPPolicyGroupEntry,_M:qtechSMPPolicyGroupIndex,'qtechSMPPolicyGroupCount':qtechSMPPolicyGroupCount,'qtechSMPPolicyGroupChecksum':qtechSMPPolicyGroupChecksum,'qtechSMPPolicyGroupStatus':qtechSMPPolicyGroupStatus,'qtechEGMIBObjects':qtechEGMIBObjects,'qtechEGUserTable':qtechEGUserTable,'qtechEGUserEntry':qtechEGUserEntry,_N:qtechEGUserIpAddrType,_O:qtechEGUserIpAddr,'qtechEGUserId':qtechEGUserId,'qtechEGUserName':qtechEGUserName,'qtechEGUserGroupName':qtechEGUserGroupName,'qtechEGUserMac':qtechEGUserMac,'qtechEGNasIp':qtechEGNasIp,'qtechEGNasPort':qtechEGNasPort,'qtechEGGatewayIp':qtechEGGatewayIp,'qtechEGVlanId':qtechEGVlanId,'qtechEGLoginTime':qtechEGLoginTime,'qtechEGLogoutTime':qtechEGLogoutTime,'qtechEGMessageType':qtechEGMessageType,'qtechEGUserStatus':qtechEGUserStatus,'qtechEGUserDelete':qtechEGUserDelete,'qtechSMPMIBConformance':qtechSMPMIBConformance,'qtechSMPMIBCompliances':qtechSMPMIBCompliances,'qtechDeviceMIBCompliance':qtechDeviceMIBCompliance,'qtechSMPMIBGroups':qtechSMPMIBGroups,_t:qtechSMPServerMibGroup,_u:qtechSMPClientMibGroup,_v:qtechSMPPolicyMibGroup,_w:qtechSMPFrameRelayMibGroup,'qtechSMPTraps':qtechSMPTraps,_e:qtechSMPSwitchIP,_f:qtechSMPSwitchInterfaceID,_g:qtechSMPSwitchInterfaceVLANID,_h:qtechSMPFrameContentLength,_i:qtechSMPFrameContent,'qtechSMPFrameRelayTrap':qtechSMPFrameRelayTrap,_j:qtechSMPArpAttackSubnetIP,_k:qtechSMPArpAttackSubnetIPNum,_l:qtechSMPArpAttackInterfaceSlot,_m:qtechSMPArpAttackInterfacePort,_n:qtechSMPArpAttackInterfaceVlanID,_o:qtechSMPArpAttackFrameContent,_p:qtechSMPArpAttackStatus,_q:qtechSMPArpAttackCriticalStatus,_r:qtechSMPArpAttackMac,_s:qtechSMPArpAttackInterfaceIndex,'qtechSMPArpAttackTrap':qtechSMPArpAttackTrap})