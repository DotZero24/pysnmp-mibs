_A2='rlBrgDynamicCmdKey'
_A1='rlBrgIpmFdbRefSourceAddress'
_A0='rlBrgIpmFdbRefSourceAddressType'
_z='rlBrgIpmFdbRefGroupAddress'
_y='rlBrgIpmFdbRefGroupAddressType'
_x='rlBrgIpmFdbRefVlanTag'
_w='rlBrgInetMulticastSourceAddress'
_v='rlBrgInetMulticastSourceAddressType'
_u='rlBrgInetMulticastGroupAddress'
_t='rlBrgInetMulticastGroupAddressType'
_s='rlBrgInetMulticastVlanTag'
_r='rlBrgStaticInetMulticastSourceAddress'
_q='rlBrgStaticInetMulticastSourceAddressType'
_p='rlBrgStaticInetMulticastGroupAddress'
_o='rlBrgStaticInetMulticastGroupAddressType'
_n='rlBrgStaticInetMulticastVlanTag'
_m='rlBrgIpMulticastSourceAddress'
_l='rlBrgIpMulticastGroupAddress'
_k='rlBrgIpMulticastVlanTag'
_j='rlBrgStaticIpMulticastSourceAddress'
_i='rlBrgStaticIpMulticastGroupAddress'
_h='rlBrgStaticIpMulticastVlanTag'
_g='rlIgmpMldSnoopQuerierVlanTag'
_f='rlIgmpMldSnoopMulticastTvGroup'
_e='rlIgmpMldSnoopMulticastTvGroupAddressType'
_d='rlIgmpMldSnoopMulticastTvVID'
_c='rlIgmpMldSnoopMulticastTvInetAddressType'
_b='rlIgmpMldSnoopVlanTag'
_a='rlIgmpMldSnoopVlanInetAddressType'
_Z='rlIgmpMldSnoopMembershipSourceIpAddress'
_Y='rlIgmpMldSnoopMembershipSourceIpAddressType'
_X='rlIgmpMldSnoopMembershipGroupIpAddress'
_W='rlIgmpMldSnoopMembershipGroupIpAddressType'
_V='rlIgmpMldSnoopMembershipVlanTag'
_U='rlIgmpSnoopQuerierVlanTag'
_T='rlIgmpSnoopMembershipSourceIpAddress'
_S='rlIgmpSnoopMembershipGroupIpAddress'
_R='rlIgmpSnoopMembershipVlanTag'
_Q='rlIgmpSnoopMulticastTvGroup'
_P='rlIgmpSnoopMulticastTvVID'
_O='rlIgmpSnoopVlanTag'
_N='TruthValue'
_M='rndErrorSeverity'
_L='rndErrorDesc'
_K='EDGECORE-DEVICEPARAMS-MIB'
_J='seconds'
_I='milliseconds'
_H='Integer32'
_G='not-accessible'
_F='Unsigned32'
_E='obsolete'
_D='EDGECORE-rlBrgMulticast-MIB'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
MacAddress,=mibBuilder.importSymbols('BRIDGE-MIB','MacAddress')
rndErrorDesc,rndErrorSeverity=mibBuilder.importSymbols(_K,_L,_M)
rlBrgMulticast,rlMacMulticast,rnd,rndNotifications=mibBuilder.importSymbols('EDGECORE-MIB','rlBrgMulticast','rlMacMulticast','rnd','rndNotifications')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
PortList,VlanIndex=mibBuilder.importSymbols('Q-BRIDGE-MIB','PortList','VlanIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_N)
class IgmpVersion(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('none',0),('v1',1),('v2',2),('v3',3)))
class DynamicCmdType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('createEntry',0),('deleteEntry',1),('addPorts',2),('deletePorts',3)))
_RlMacMulticastEnable_Type=TruthValue
_RlMacMulticastEnable_Object=MibScalar
rlMacMulticastEnable=_RlMacMulticastEnable_Object((1,3,6,1,4,1,259,10,1,14,89,55,1),_RlMacMulticastEnable_Type())
rlMacMulticastEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:rlMacMulticastEnable.setStatus(_A)
_RlIgmpSnoop_ObjectIdentity=ObjectIdentity
rlIgmpSnoop=_RlIgmpSnoop_ObjectIdentity((1,3,6,1,4,1,259,10,1,14,89,55,2))
_RlIgmpSnoopMibVersion_Type=Integer32
_RlIgmpSnoopMibVersion_Object=MibScalar
rlIgmpSnoopMibVersion=_RlIgmpSnoopMibVersion_Object((1,3,6,1,4,1,259,10,1,14,89,55,2,1),_RlIgmpSnoopMibVersion_Type())
rlIgmpSnoopMibVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:rlIgmpSnoopMibVersion.setStatus(_A)
_RlIgmpSnoopEnable_Type=TruthValue
_RlIgmpSnoopEnable_Object=MibScalar
rlIgmpSnoopEnable=_RlIgmpSnoopEnable_Object((1,3,6,1,4,1,259,10,1,14,89,55,2,2),_RlIgmpSnoopEnable_Type())
rlIgmpSnoopEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:rlIgmpSnoopEnable.setStatus(_A)
class _RlIgmpSnoopHostAgingTime_Type(Integer32):defaultValue=260;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_RlIgmpSnoopHostAgingTime_Type.__name__=_H
_RlIgmpSnoopHostAgingTime_Object=MibScalar
rlIgmpSnoopHostAgingTime=_RlIgmpSnoopHostAgingTime_Object((1,3,6,1,4,1,259,10,1,14,89,55,2,3),_RlIgmpSnoopHostAgingTime_Type())
rlIgmpSnoopHostAgingTime.setMaxAccess(_C)
if mibBuilder.loadTexts:rlIgmpSnoopHostAgingTime.setStatus(_E)
if mibBuilder.loadTexts:rlIgmpSnoopHostAgingTime.setUnits(_J)
class _RlIgmpSnoopRouterAgingTime_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_RlIgmpSnoopRouterAgingTime_Type.__name__=_H
_RlIgmpSnoopRouterAgingTime_Object=MibScalar
rlIgmpSnoopRouterAgingTime=_RlIgmpSnoopRouterAgingTime_Object((1,3,6,1,4,1,259,10,1,14,89,55,2,4),_RlIgmpSnoopRouterAgingTime_Type())
rlIgmpSnoopRouterAgingTime.setMaxAccess(_C)
if mibBuilder.loadTexts:rlIgmpSnoopRouterAgingTime.setStatus(_E)
if mibBuilder.loadTexts:rlIgmpSnoopRouterAgingTime.setUnits(_J)
_RlIgmpSnoopVlanTable_Object=MibTable
rlIgmpSnoopVlanTable=_RlIgmpSnoopVlanTable_Object((1,3,6,1,4,1,259,10,1,14,89,55,2,7))
if mibBuilder.loadTexts:rlIgmpSnoopVlanTable.setStatus(_E)
_RlIgmpSnoopVlanEntry_Object=MibTableRow
rlIgmpSnoopVlanEntry=_RlIgmpSnoopVlanEntry_Object((1,3,6,1,4,1,259,10,1,14,89,55,2,7,1))
rlIgmpSnoopVlanEntry.setIndexNames((0,_D,_O))
if mibBuilder.loadTexts:rlIgmpSnoopVlanEntry.setStatus(_E)
_RlIgmpSnoopVlanTag_Type=Integer32
_RlIgmpSnoopVlanTag_Object=MibTableColumn
rlIgmpSnoopVlanTag=_RlIgmpSnoopVlanTag_Object((1,3,6,1,4,1,259,10,1,14,89,55,2,7,1,1),_RlIgmpSnoopVlanTag_Type())
rlIgmpSnoopVlanTag.setMaxAccess(_B)
if mibBuilder.loadTexts:rlIgmpSnoopVlanTag.setStatus(_E)
_RlIgmpSnoopVlanEnable_Type=TruthValue
_RlIgmpSnoopVlanEnable_Object=MibTableColumn
rlIgmpSnoopVlanEnable=_RlIgmpSnoopVlanEnable_Object((1,3,6,1,4,1,259,10,1,14,89,55,2,7,1,2),_RlIgmpSnoopVlanEnable_Type())
rlIgmpSnoopVlanEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:rlIgmpSnoopVlanEnable.setStatus(_E)
_RlIgmpSnoopVlanRouterLearn_Type=TruthValue
_RlIgmpSnoopVlanRouterLearn_Object=MibTableColumn
rlIgmpSnoopVlanRouterLearn=_RlIgmpSnoopVlanRouterLearn_Object((1,3,6,1,4,1,259,10,1,14,89,55,2,7,1,3),_RlIgmpSnoopVlanRouterLearn_Type())
rlIgmpSnoopVlanRouterLearn.setMaxAccess(_C)
if mibBuilder.loadTexts:rlIgmpSnoopVlanRouterLearn.setStatus(_E)
class _RlIgmpSnoopVlanHostTimeOut_Type(Integer32):defaultValue=260;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_RlIgmpSnoopVlanHostTimeOut_Type.__name__=_H
_RlIgmpSnoopVlanHostTimeOut_Object=MibTableColumn
rlIgmpSnoopVlanHostTimeOut=_RlIgmpSnoopVlanHostTimeOut_Object((1,3,6,1,4,1,259,10,1,14,89,55,2,7,1,4),_RlIgmpSnoopVlanHostTimeOut_Type())
rlIgmpSnoopVlanHostTimeOut.setMaxAccess(_C)
if mibBuilder.loadTexts:rlIgmpSnoopVlanHostTimeOut.setStatus(_E)
if mibBuilder.loadTexts:rlIgmpSnoopVlanHostTimeOut.setUnits(_J)
class _RlIgmpSnoopVlanQuerierTimeOut_Type(Integer32):defaultValue=260;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_RlIgmpSnoopVlanQuerierTimeOut_Type.__name__=_H
_RlIgmpSnoopVlanQuerierTimeOut_Object=MibTableColumn
rlIgmpSnoopVlanQuerierTimeOut=_RlIgmpSnoopVlanQuerierTimeOut_Object((1,3,6,1,4,1,259,10,1,14,89,55,2,7,1,5),_RlIgmpSnoopVlanQuerierTimeOut_Type())
rlIgmpSnoopVlanQuerierTimeOut.setMaxAccess(_C)
if mibBuilder.loadTexts:rlIgmpSnoopVlanQuerierTimeOut.setStatus(_E)
if mibBuilder.loadTexts:rlIgmpSnoopVlanQuerierTimeOut.setUnits(_J)
class _RlIgmpSnoopVlanRouterTimeOut_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_RlIgmpSnoopVlanRouterTimeOut_Type.__name__=_H
_RlIgmpSnoopVlanRouterTimeOut_Object=MibTableColumn
rlIgmpSnoopVlanRouterTimeOut=_RlIgmpSnoopVlanRouterTimeOut_Object((1,3,6,1,4,1,259,10,1,14,89,55,2,7,1,6),_RlIgmpSnoopVlanRouterTimeOut_Type())
rlIgmpSnoopVlanRouterTimeOut.setMaxAccess(_C)
if mibBuilder.loadTexts:rlIgmpSnoopVlanRouterTimeOut.setStatus(_E)
if mibBuilder.loadTexts:rlIgmpSnoopVlanRouterTimeOut.setUnits(_J)
class _RlIgmpSnoopVlanLeaveTimeOut_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_RlIgmpSnoopVlanLeaveTimeOut_Type.__name__=_H
_RlIgmpSnoopVlanLeaveTimeOut_Object=MibTableColumn
rlIgmpSnoopVlanLeaveTimeOut=_RlIgmpSnoopVlanLeaveTimeOut_Object((1,3,6,1,4,1,259,10,1,14,89,55,2,7,1,7),_RlIgmpSnoopVlanLeaveTimeOut_Type())
rlIgmpSnoopVlanLeaveTimeOut.setMaxAccess(_C)
if mibBuilder.loadTexts:rlIgmpSnoopVlanLeaveTimeOut.setStatus(_E)
if mibBuilder.loadTexts:rlIgmpSnoopVlanLeaveTimeOut.setUnits(_J)
_RlIgmpSnoopVlanIgmpVersion_Type=IgmpVersion
_RlIgmpSnoopVlanIgmpVersion_Object=MibTableColumn
rlIgmpSnoopVlanIgmpVersion=_RlIgmpSnoopVlanIgmpVersion_Object((1,3,6,1,4,1,259,10,1,14,89,55,2,7,1,8),_RlIgmpSnoopVlanIgmpVersion_Type())
rlIgmpSnoopVlanIgmpVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:rlIgmpSnoopVlanIgmpVersion.setStatus(_E)
_RlIgmpSnoopVlanRouterPortlist_Type=PortList
_RlIgmpSnoopVlanRouterPortlist_Object=MibTableColumn
rlIgmpSnoopVlanRouterPortlist=_RlIgmpSnoopVlanRouterPortlist_Object((1,3,6,1,4,1,259,10,1,14,89,55,2,7,1,9),_RlIgmpSnoopVlanRouterPortlist_Type())
rlIgmpSnoopVlanRouterPortlist.setMaxAccess(_B)
if mibBuilder.loadTexts:rlIgmpSnoopVlanRouterPortlist.setStatus(_E)
class _RlIgmpSnoopIGMP224ReportsHandle_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('allow',1),('ignore',2)))
_RlIgmpSnoopIGMP224ReportsHandle_Type.__name__=_H
_RlIgmpSnoopIGMP224ReportsHandle_Object=MibScalar
rlIgmpSnoopIGMP224ReportsHandle=_RlIgmpSnoopIGMP224ReportsHandle_Object((1,3,6,1,4,1,259,10,1,14,89,55,2,8),_RlIgmpSnoopIGMP224ReportsHandle_Type())
rlIgmpSnoopIGMP224ReportsHandle.setMaxAccess(_C)
if mibBuilder.loadTexts:rlIgmpSnoopIGMP224ReportsHandle.setStatus(_A)
_RlIgmpSnoopMulticastTvTable_Object=MibTable
rlIgmpSnoopMulticastTvTable=_RlIgmpSnoopMulticastTvTable_Object((1,3,6,1,4,1,259,10,1,14,89,55,2,10))
if mibBuilder.loadTexts:rlIgmpSnoopMulticastTvTable.setStatus(_A)
_RlIgmpSnoopMulticastTvEntry_Object=MibTableRow
rlIgmpSnoopMulticastTvEntry=_RlIgmpSnoopMulticastTvEntry_Object((1,3,6,1,4,1,259,10,1,14,89,55,2,10,1))
rlIgmpSnoopMulticastTvEntry.setIndexNames((0,_D,_P),(0,_D,_Q))
if mibBuilder.loadTexts:rlIgmpSnoopMulticastTvEntry.setStatus(_A)
_RlIgmpSnoopMulticastTvVID_Type=VlanIndex
_RlIgmpSnoopMulticastTvVID_Object=MibTableColumn
rlIgmpSnoopMulticastTvVID=_RlIgmpSnoopMulticastTvVID_Object((1,3,6,1,4,1,259,10,1,14,89,55,2,10,1,1),_RlIgmpSnoopMulticastTvVID_Type())
rlIgmpSnoopMulticastTvVID.setMaxAccess(_B)
if mibBuilder.loadTexts:rlIgmpSnoopMulticastTvVID.setStatus(_A)
_RlIgmpSnoopMulticastTvGroup_Type=IpAddress
_RlIgmpSnoopMulticastTvGroup_Object=MibTableColumn
rlIgmpSnoopMulticastTvGroup=_RlIgmpSnoopMulticastTvGroup_Object((1,3,6,1,4,1,259,10,1,14,89,55,2,10,1,2),_RlIgmpSnoopMulticastTvGroup_Type())
rlIgmpSnoopMulticastTvGroup.setMaxAccess(_B)
if mibBuilder.loadTexts:rlIgmpSnoopMulticastTvGroup.setStatus(_A)
_RlIgmpSnoopMulticastTvStatus_Type=RowStatus
_RlIgmpSnoopMulticastTvStatus_Object=MibTableColumn
rlIgmpSnoopMulticastTvStatus=_RlIgmpSnoopMulticastTvStatus_Object((1,3,6,1,4,1,259,10,1,14,89,55,2,10,1,3),_RlIgmpSnoopMulticastTvStatus_Type())
rlIgmpSnoopMulticastTvStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:rlIgmpSnoopMulticastTvStatus.setStatus(_A)
_RlIgmpSnoopMembershipTable_Object=MibTable
rlIgmpSnoopMembershipTable=_RlIgmpSnoopMembershipTable_Object((1,3,6,1,4,1,259,10,1,14,89,55,2,11))
if mibBuilder.loadTexts:rlIgmpSnoopMembershipTable.setStatus(_A)
_RlIgmpSnoopMembershipEntry_Object=MibTableRow
rlIgmpSnoopMembershipEntry=_RlIgmpSnoopMembershipEntry_Object((1,3,6,1,4,1,259,10,1,14,89,55,2,11,1))
rlIgmpSnoopMembershipEntry.setIndexNames((0,_D,_R),(0,_D,_S),(0,_D,_T))
if mibBuilder.loadTexts:rlIgmpSnoopMembershipEntry.setStatus(_A)
_RlIgmpSnoopMembershipVlanTag_Type=VlanIndex
_RlIgmpSnoopMembershipVlanTag_Object=MibTableColumn
rlIgmpSnoopMembershipVlanTag=_RlIgmpSnoopMembershipVlanTag_Object((1,3,6,1,4,1,259,10,1,14,89,55,2,11,1,1),_RlIgmpSnoopMembershipVlanTag_Type())
rlIgmpSnoopMembershipVlanTag.setMaxAccess(_B)
if mibBuilder.loadTexts:rlIgmpSnoopMembershipVlanTag.setStatus(_A)
_RlIgmpSnoopMembershipGroupIpAddress_Type=IpAddress
_RlIgmpSnoopMembershipGroupIpAddress_Object=MibTableColumn
rlIgmpSnoopMembershipGroupIpAddress=_RlIgmpSnoopMembershipGroupIpAddress_Object((1,3,6,1,4,1,259,10,1,14,89,55,2,11,1,2),_RlIgmpSnoopMembershipGroupIpAddress_Type())
rlIgmpSnoopMembershipGroupIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:rlIgmpSnoopMembershipGroupIpAddress.setStatus(_A)
_RlIgmpSnoopMembershipSourceIpAddress_Type=IpAddress
_RlIgmpSnoopMembershipSourceIpAddress_Object=MibTableColumn
rlIgmpSnoopMembershipSourceIpAddress=_RlIgmpSnoopMembershipSourceIpAddress_Object((1,3,6,1,4,1,259,10,1,14,89,55,2,11,1,3),_RlIgmpSnoopMembershipSourceIpAddress_Type())
rlIgmpSnoopMembershipSourceIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:rlIgmpSnoopMembershipSourceIpAddress.setStatus(_A)
_RlIgmpSnoopMembershipIncPortlist_Type=PortList
_RlIgmpSnoopMembershipIncPortlist_Object=MibTableColumn
rlIgmpSnoopMembershipIncPortlist=_RlIgmpSnoopMembershipIncPortlist_Object((1,3,6,1,4,1,259,10,1,14,89,55,2,11,1,4),_RlIgmpSnoopMembershipIncPortlist_Type())
rlIgmpSnoopMembershipIncPortlist.setMaxAccess(_B)
if mibBuilder.loadTexts:rlIgmpSnoopMembershipIncPortlist.setStatus(_A)
_RlIgmpSnoopMembershipExcPortlist_Type=PortList
_RlIgmpSnoopMembershipExcPortlist_Object=MibTableColumn
rlIgmpSnoopMembershipExcPortlist=_RlIgmpSnoopMembershipExcPortlist_Object((1,3,6,1,4,1,259,10,1,14,89,55,2,11,1,5),_RlIgmpSnoopMembershipExcPortlist_Type())
rlIgmpSnoopMembershipExcPortlist.setMaxAccess(_B)
if mibBuilder.loadTexts:rlIgmpSnoopMembershipExcPortlist.setStatus(_A)
_RlIgmpSnoopMembershipExpiryTime_Type=Integer32
_RlIgmpSnoopMembershipExpiryTime_Object=MibTableColumn
rlIgmpSnoopMembershipExpiryTime=_RlIgmpSnoopMembershipExpiryTime_Object((1,3,6,1,4,1,259,10,1,14,89,55,2,11,1,6),_RlIgmpSnoopMembershipExpiryTime_Type())
rlIgmpSnoopMembershipExpiryTime.setMaxAccess(_B)
if mibBuilder.loadTexts:rlIgmpSnoopMembershipExpiryTime.setStatus(_E)
_RlIgmpSnoopMembershipCompatibilityMode_Type=IgmpVersion
_RlIgmpSnoopMembershipCompatibilityMode_Object=MibTableColumn
rlIgmpSnoopMembershipCompatibilityMode=_RlIgmpSnoopMembershipCompatibilityMode_Object((1,3,6,1,4,1,259,10,1,14,89,55,2,11,1,7),_RlIgmpSnoopMembershipCompatibilityMode_Type())
rlIgmpSnoopMembershipCompatibilityMode.setMaxAccess(_B)
if mibBuilder.loadTexts:rlIgmpSnoopMembershipCompatibilityMode.setStatus(_A)
_RlIgmpSnoopQuerierVlanTable_Object=MibTable
rlIgmpSnoopQuerierVlanTable=_RlIgmpSnoopQuerierVlanTable_Object((1,3,6,1,4,1,259,10,1,14,89,55,2,12))
if mibBuilder.loadTexts:rlIgmpSnoopQuerierVlanTable.setStatus(_A)
_RlIgmpSnoopQuerierVlanEntry_Object=MibTableRow
rlIgmpSnoopQuerierVlanEntry=_RlIgmpSnoopQuerierVlanEntry_Object((1,3,6,1,4,1,259,10,1,14,89,55,2,12,1))
rlIgmpSnoopQuerierVlanEntry.setIndexNames((0,_D,_U))
if mibBuilder.loadTexts:rlIgmpSnoopQuerierVlanEntry.setStatus(_A)
_RlIgmpSnoopQuerierVlanTag_Type=VlanIndex
_RlIgmpSnoopQuerierVlanTag_Object=MibTableColumn
rlIgmpSnoopQuerierVlanTag=_RlIgmpSnoopQuerierVlanTag_Object((1,3,6,1,4,1,259,10,1,14,89,55,2,12,1,1),_RlIgmpSnoopQuerierVlanTag_Type())
rlIgmpSnoopQuerierVlanTag.setMaxAccess(_B)
if mibBuilder.loadTexts:rlIgmpSnoopQuerierVlanTag.setStatus(_A)
_RlIgmpSnoopQuerierAdminEnable_Type=TruthValue
_RlIgmpSnoopQuerierAdminEnable_Object=MibTableColumn
rlIgmpSnoopQuerierAdminEnable=_RlIgmpSnoopQuerierAdminEnable_Object((1,3,6,1,4,1,259,10,1,14,89,55,2,12,1,2),_RlIgmpSnoopQuerierAdminEnable_Type())
rlIgmpSnoopQuerierAdminEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:rlIgmpSnoopQuerierAdminEnable.setStatus(_A)
_RlIgmpSnoopQuerierOperEnable_Type=TruthValue
_RlIgmpSnoopQuerierOperEnable_Object=MibTableColumn
rlIgmpSnoopQuerierOperEnable=_RlIgmpSnoopQuerierOperEnable_Object((1,3,6,1,4,1,259,10,1,14,89,55,2,12,1,3),_RlIgmpSnoopQuerierOperEnable_Type())
rlIgmpSnoopQuerierOperEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:rlIgmpSnoopQuerierOperEnable.setStatus(_A)
_RlIgmpSnoopQuerierAdminAddr_Type=IpAddress
_RlIgmpSnoopQuerierAdminAddr_Object=MibTableColumn
rlIgmpSnoopQuerierAdminAddr=_RlIgmpSnoopQuerierAdminAddr_Object((1,3,6,1,4,1,259,10,1,14,89,55,2,12,1,4),_RlIgmpSnoopQuerierAdminAddr_Type())
rlIgmpSnoopQuerierAdminAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:rlIgmpSnoopQuerierAdminAddr.setStatus(_A)
_RlIgmpSnoopQuerierOperAddr_Type=IpAddress
_RlIgmpSnoopQuerierOperAddr_Object=MibTableColumn
rlIgmpSnoopQuerierOperAddr=_RlIgmpSnoopQuerierOperAddr_Object((1,3,6,1,4,1,259,10,1,14,89,55,2,12,1,5),_RlIgmpSnoopQuerierOperAddr_Type())
rlIgmpSnoopQuerierOperAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:rlIgmpSnoopQuerierOperAddr.setStatus(_A)
_RlIgmpSnoopQuerierAdminVersionNumber_Type=IgmpVersion
_RlIgmpSnoopQuerierAdminVersionNumber_Object=MibTableColumn
rlIgmpSnoopQuerierAdminVersionNumber=_RlIgmpSnoopQuerierAdminVersionNumber_Object((1,3,6,1,4,1,259,10,1,14,89,55,2,12,1,6),_RlIgmpSnoopQuerierAdminVersionNumber_Type())
rlIgmpSnoopQuerierAdminVersionNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:rlIgmpSnoopQuerierAdminVersionNumber.setStatus(_A)
_RlIgmpSnoopQuerierOperVersionNumber_Type=IgmpVersion
_RlIgmpSnoopQuerierOperVersionNumber_Object=MibTableColumn
rlIgmpSnoopQuerierOperVersionNumber=_RlIgmpSnoopQuerierOperVersionNumber_Object((1,3,6,1,4,1,259,10,1,14,89,55,2,12,1,7),_RlIgmpSnoopQuerierOperVersionNumber_Type())
rlIgmpSnoopQuerierOperVersionNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:rlIgmpSnoopQuerierOperVersionNumber.setStatus(_A)
_RlMacMulticastMaxEntriesNum_Type=Integer32
_RlMacMulticastMaxEntriesNum_Object=MibScalar
rlMacMulticastMaxEntriesNum=_RlMacMulticastMaxEntriesNum_Object((1,3,6,1,4,1,259,10,1,14,89,55,3),_RlMacMulticastMaxEntriesNum_Type())
rlMacMulticastMaxEntriesNum.setMaxAccess(_B)
if mibBuilder.loadTexts:rlMacMulticastMaxEntriesNum.setStatus(_A)
_RlMacMulticastFilter_ObjectIdentity=ObjectIdentity
rlMacMulticastFilter=_RlMacMulticastFilter_ObjectIdentity((1,3,6,1,4,1,259,10,1,14,89,55,4))
_RlMacMulticastUnregFilterEnable_Type=PortList
_RlMacMulticastUnregFilterEnable_Object=MibScalar
rlMacMulticastUnregFilterEnable=_RlMacMulticastUnregFilterEnable_Object((1,3,6,1,4,1,259,10,1,14,89,55,4,1),_RlMacMulticastUnregFilterEnable_Type())
rlMacMulticastUnregFilterEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:rlMacMulticastUnregFilterEnable.setStatus(_A)
_RlMldSnoop_ObjectIdentity=ObjectIdentity
rlMldSnoop=_RlMldSnoop_ObjectIdentity((1,3,6,1,4,1,259,10,1,14,89,55,5))
_RlMldSnoopEnable_Type=TruthValue
_RlMldSnoopEnable_Object=MibScalar
rlMldSnoopEnable=_RlMldSnoopEnable_Object((1,3,6,1,4,1,259,10,1,14,89,55,5,1),_RlMldSnoopEnable_Type())
rlMldSnoopEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:rlMldSnoopEnable.setStatus(_A)
class _RlMldSnoopHostAgingTime_Type(Integer32):defaultValue=260;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,2147483647))
_RlMldSnoopHostAgingTime_Type.__name__=_H
_RlMldSnoopHostAgingTime_Object=MibScalar
rlMldSnoopHostAgingTime=_RlMldSnoopHostAgingTime_Object((1,3,6,1,4,1,259,10,1,14,89,55,5,2),_RlMldSnoopHostAgingTime_Type())
rlMldSnoopHostAgingTime.setMaxAccess(_C)
if mibBuilder.loadTexts:rlMldSnoopHostAgingTime.setStatus(_E)
if mibBuilder.loadTexts:rlMldSnoopHostAgingTime.setUnits(_J)
class _RlMldSnoopRouterAgingTime_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_RlMldSnoopRouterAgingTime_Type.__name__=_H
_RlMldSnoopRouterAgingTime_Object=MibScalar
rlMldSnoopRouterAgingTime=_RlMldSnoopRouterAgingTime_Object((1,3,6,1,4,1,259,10,1,14,89,55,5,3),_RlMldSnoopRouterAgingTime_Type())
rlMldSnoopRouterAgingTime.setMaxAccess(_C)
if mibBuilder.loadTexts:rlMldSnoopRouterAgingTime.setStatus(_E)
if mibBuilder.loadTexts:rlMldSnoopRouterAgingTime.setUnits(_J)
_RlIgmpMldSnoopMembershipTable_Object=MibTable
rlIgmpMldSnoopMembershipTable=_RlIgmpMldSnoopMembershipTable_Object((1,3,6,1,4,1,259,10,1,14,89,55,5,4))
if mibBuilder.loadTexts:rlIgmpMldSnoopMembershipTable.setStatus(_A)
_RlIgmpMldSnoopMembershipEntry_Object=MibTableRow
rlIgmpMldSnoopMembershipEntry=_RlIgmpMldSnoopMembershipEntry_Object((1,3,6,1,4,1,259,10,1,14,89,55,5,4,1))
rlIgmpMldSnoopMembershipEntry.setIndexNames((0,_D,_V),(0,_D,_W),(0,_D,_X),(0,_D,_Y),(0,_D,_Z))
if mibBuilder.loadTexts:rlIgmpMldSnoopMembershipEntry.setStatus(_A)
_RlIgmpMldSnoopMembershipVlanTag_Type=VlanIndex
_RlIgmpMldSnoopMembershipVlanTag_Object=MibTableColumn
rlIgmpMldSnoopMembershipVlanTag=_RlIgmpMldSnoopMembershipVlanTag_Object((1,3,6,1,4,1,259,10,1,14,89,55,5,4,1,1),_RlIgmpMldSnoopMembershipVlanTag_Type())
rlIgmpMldSnoopMembershipVlanTag.setMaxAccess(_B)
if mibBuilder.loadTexts:rlIgmpMldSnoopMembershipVlanTag.setStatus(_A)
_RlIgmpMldSnoopMembershipGroupIpAddressType_Type=InetAddressType
_RlIgmpMldSnoopMembershipGroupIpAddressType_Object=MibTableColumn
rlIgmpMldSnoopMembershipGroupIpAddressType=_RlIgmpMldSnoopMembershipGroupIpAddressType_Object((1,3,6,1,4,1,259,10,1,14,89,55,5,4,1,2),_RlIgmpMldSnoopMembershipGroupIpAddressType_Type())
rlIgmpMldSnoopMembershipGroupIpAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:rlIgmpMldSnoopMembershipGroupIpAddressType.setStatus(_A)
_RlIgmpMldSnoopMembershipGroupIpAddress_Type=InetAddress
_RlIgmpMldSnoopMembershipGroupIpAddress_Object=MibTableColumn
rlIgmpMldSnoopMembershipGroupIpAddress=_RlIgmpMldSnoopMembershipGroupIpAddress_Object((1,3,6,1,4,1,259,10,1,14,89,55,5,4,1,3),_RlIgmpMldSnoopMembershipGroupIpAddress_Type())
rlIgmpMldSnoopMembershipGroupIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:rlIgmpMldSnoopMembershipGroupIpAddress.setStatus(_A)
_RlIgmpMldSnoopMembershipSourceIpAddressType_Type=InetAddressType
_RlIgmpMldSnoopMembershipSourceIpAddressType_Object=MibTableColumn
rlIgmpMldSnoopMembershipSourceIpAddressType=_RlIgmpMldSnoopMembershipSourceIpAddressType_Object((1,3,6,1,4,1,259,10,1,14,89,55,5,4,1,4),_RlIgmpMldSnoopMembershipSourceIpAddressType_Type())
rlIgmpMldSnoopMembershipSourceIpAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:rlIgmpMldSnoopMembershipSourceIpAddressType.setStatus(_A)
_RlIgmpMldSnoopMembershipSourceIpAddress_Type=InetAddress
_RlIgmpMldSnoopMembershipSourceIpAddress_Object=MibTableColumn
rlIgmpMldSnoopMembershipSourceIpAddress=_RlIgmpMldSnoopMembershipSourceIpAddress_Object((1,3,6,1,4,1,259,10,1,14,89,55,5,4,1,5),_RlIgmpMldSnoopMembershipSourceIpAddress_Type())
rlIgmpMldSnoopMembershipSourceIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:rlIgmpMldSnoopMembershipSourceIpAddress.setStatus(_A)
_RlIgmpMldSnoopMembershipIncPortlist_Type=PortList
_RlIgmpMldSnoopMembershipIncPortlist_Object=MibTableColumn
rlIgmpMldSnoopMembershipIncPortlist=_RlIgmpMldSnoopMembershipIncPortlist_Object((1,3,6,1,4,1,259,10,1,14,89,55,5,4,1,6),_RlIgmpMldSnoopMembershipIncPortlist_Type())
rlIgmpMldSnoopMembershipIncPortlist.setMaxAccess(_B)
if mibBuilder.loadTexts:rlIgmpMldSnoopMembershipIncPortlist.setStatus(_A)
_RlIgmpMldSnoopMembershipExcPortlist_Type=PortList
_RlIgmpMldSnoopMembershipExcPortlist_Object=MibTableColumn
rlIgmpMldSnoopMembershipExcPortlist=_RlIgmpMldSnoopMembershipExcPortlist_Object((1,3,6,1,4,1,259,10,1,14,89,55,5,4,1,7),_RlIgmpMldSnoopMembershipExcPortlist_Type())
rlIgmpMldSnoopMembershipExcPortlist.setMaxAccess(_B)
if mibBuilder.loadTexts:rlIgmpMldSnoopMembershipExcPortlist.setStatus(_A)
_RlIgmpMldSnoopMembershipExpiryTime_Type=Integer32
_RlIgmpMldSnoopMembershipExpiryTime_Object=MibTableColumn
rlIgmpMldSnoopMembershipExpiryTime=_RlIgmpMldSnoopMembershipExpiryTime_Object((1,3,6,1,4,1,259,10,1,14,89,55,5,4,1,8),_RlIgmpMldSnoopMembershipExpiryTime_Type())
rlIgmpMldSnoopMembershipExpiryTime.setMaxAccess(_B)
if mibBuilder.loadTexts:rlIgmpMldSnoopMembershipExpiryTime.setStatus(_E)
_RlIgmpMldSnoopMembershipCompatibilityMode_Type=IgmpVersion
_RlIgmpMldSnoopMembershipCompatibilityMode_Object=MibTableColumn
rlIgmpMldSnoopMembershipCompatibilityMode=_RlIgmpMldSnoopMembershipCompatibilityMode_Object((1,3,6,1,4,1,259,10,1,14,89,55,5,4,1,9),_RlIgmpMldSnoopMembershipCompatibilityMode_Type())
rlIgmpMldSnoopMembershipCompatibilityMode.setMaxAccess(_B)
if mibBuilder.loadTexts:rlIgmpMldSnoopMembershipCompatibilityMode.setStatus(_A)
_RlIgmpMldSnoopVlanTable_Object=MibTable
rlIgmpMldSnoopVlanTable=_RlIgmpMldSnoopVlanTable_Object((1,3,6,1,4,1,259,10,1,14,89,55,5,5))
if mibBuilder.loadTexts:rlIgmpMldSnoopVlanTable.setStatus(_A)
_RlIgmpMldSnoopVlanEntry_Object=MibTableRow
rlIgmpMldSnoopVlanEntry=_RlIgmpMldSnoopVlanEntry_Object((1,3,6,1,4,1,259,10,1,14,89,55,5,5,1))
rlIgmpMldSnoopVlanEntry.setIndexNames((0,_D,_a),(0,_D,_b))
if mibBuilder.loadTexts:rlIgmpMldSnoopVlanEntry.setStatus(_A)
_RlIgmpMldSnoopVlanInetAddressType_Type=InetAddressType
_RlIgmpMldSnoopVlanInetAddressType_Object=MibTableColumn
rlIgmpMldSnoopVlanInetAddressType=_RlIgmpMldSnoopVlanInetAddressType_Object((1,3,6,1,4,1,259,10,1,14,89,55,5,5,1,1),_RlIgmpMldSnoopVlanInetAddressType_Type())
rlIgmpMldSnoopVlanInetAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:rlIgmpMldSnoopVlanInetAddressType.setStatus(_A)
_RlIgmpMldSnoopVlanTag_Type=Integer32
_RlIgmpMldSnoopVlanTag_Object=MibTableColumn
rlIgmpMldSnoopVlanTag=_RlIgmpMldSnoopVlanTag_Object((1,3,6,1,4,1,259,10,1,14,89,55,5,5,1,2),_RlIgmpMldSnoopVlanTag_Type())
rlIgmpMldSnoopVlanTag.setMaxAccess(_B)
if mibBuilder.loadTexts:rlIgmpMldSnoopVlanTag.setStatus(_A)
_RlIgmpMldSnoopVlanEnable_Type=TruthValue
_RlIgmpMldSnoopVlanEnable_Object=MibTableColumn
rlIgmpMldSnoopVlanEnable=_RlIgmpMldSnoopVlanEnable_Object((1,3,6,1,4,1,259,10,1,14,89,55,5,5,1,3),_RlIgmpMldSnoopVlanEnable_Type())
rlIgmpMldSnoopVlanEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:rlIgmpMldSnoopVlanEnable.setStatus(_A)
_RlIgmpMldSnoopVlanRouterLearn_Type=TruthValue
_RlIgmpMldSnoopVlanRouterLearn_Object=MibTableColumn
rlIgmpMldSnoopVlanRouterLearn=_RlIgmpMldSnoopVlanRouterLearn_Object((1,3,6,1,4,1,259,10,1,14,89,55,5,5,1,4),_RlIgmpMldSnoopVlanRouterLearn_Type())
rlIgmpMldSnoopVlanRouterLearn.setMaxAccess(_C)
if mibBuilder.loadTexts:rlIgmpMldSnoopVlanRouterLearn.setStatus(_A)
class _RlIgmpMldSnoopVlanHostTimeOut_Type(Integer32):defaultValue=260;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,2147483647))
_RlIgmpMldSnoopVlanHostTimeOut_Type.__name__=_H
_RlIgmpMldSnoopVlanHostTimeOut_Object=MibTableColumn
rlIgmpMldSnoopVlanHostTimeOut=_RlIgmpMldSnoopVlanHostTimeOut_Object((1,3,6,1,4,1,259,10,1,14,89,55,5,5,1,5),_RlIgmpMldSnoopVlanHostTimeOut_Type())
rlIgmpMldSnoopVlanHostTimeOut.setMaxAccess(_C)
if mibBuilder.loadTexts:rlIgmpMldSnoopVlanHostTimeOut.setStatus(_E)
if mibBuilder.loadTexts:rlIgmpMldSnoopVlanHostTimeOut.setUnits(_J)
class _RlIgmpMldSnoopVlanQuerierTimeOut_Type(Integer32):defaultValue=260;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_RlIgmpMldSnoopVlanQuerierTimeOut_Type.__name__=_H
_RlIgmpMldSnoopVlanQuerierTimeOut_Object=MibTableColumn
rlIgmpMldSnoopVlanQuerierTimeOut=_RlIgmpMldSnoopVlanQuerierTimeOut_Object((1,3,6,1,4,1,259,10,1,14,89,55,5,5,1,6),_RlIgmpMldSnoopVlanQuerierTimeOut_Type())
rlIgmpMldSnoopVlanQuerierTimeOut.setMaxAccess(_C)
if mibBuilder.loadTexts:rlIgmpMldSnoopVlanQuerierTimeOut.setStatus(_E)
if mibBuilder.loadTexts:rlIgmpMldSnoopVlanQuerierTimeOut.setUnits(_J)
class _RlIgmpMldSnoopVlanRouterTimeOut_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_RlIgmpMldSnoopVlanRouterTimeOut_Type.__name__=_H
_RlIgmpMldSnoopVlanRouterTimeOut_Object=MibTableColumn
rlIgmpMldSnoopVlanRouterTimeOut=_RlIgmpMldSnoopVlanRouterTimeOut_Object((1,3,6,1,4,1,259,10,1,14,89,55,5,5,1,7),_RlIgmpMldSnoopVlanRouterTimeOut_Type())
rlIgmpMldSnoopVlanRouterTimeOut.setMaxAccess(_C)
if mibBuilder.loadTexts:rlIgmpMldSnoopVlanRouterTimeOut.setStatus(_E)
if mibBuilder.loadTexts:rlIgmpMldSnoopVlanRouterTimeOut.setUnits(_J)
class _RlIgmpMldSnoopVlanLeaveTimeOut_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_RlIgmpMldSnoopVlanLeaveTimeOut_Type.__name__=_H
_RlIgmpMldSnoopVlanLeaveTimeOut_Object=MibTableColumn
rlIgmpMldSnoopVlanLeaveTimeOut=_RlIgmpMldSnoopVlanLeaveTimeOut_Object((1,3,6,1,4,1,259,10,1,14,89,55,5,5,1,8),_RlIgmpMldSnoopVlanLeaveTimeOut_Type())
rlIgmpMldSnoopVlanLeaveTimeOut.setMaxAccess(_C)
if mibBuilder.loadTexts:rlIgmpMldSnoopVlanLeaveTimeOut.setStatus(_E)
if mibBuilder.loadTexts:rlIgmpMldSnoopVlanLeaveTimeOut.setUnits(_J)
_RlIgmpMldSnoopVlanIgmpVersion_Type=IgmpVersion
_RlIgmpMldSnoopVlanIgmpVersion_Object=MibTableColumn
rlIgmpMldSnoopVlanIgmpVersion=_RlIgmpMldSnoopVlanIgmpVersion_Object((1,3,6,1,4,1,259,10,1,14,89,55,5,5,1,9),_RlIgmpMldSnoopVlanIgmpVersion_Type())
rlIgmpMldSnoopVlanIgmpVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:rlIgmpMldSnoopVlanIgmpVersion.setStatus(_A)
_RlIgmpMldSnoopVlanRouterPortlist_Type=PortList
_RlIgmpMldSnoopVlanRouterPortlist_Object=MibTableColumn
rlIgmpMldSnoopVlanRouterPortlist=_RlIgmpMldSnoopVlanRouterPortlist_Object((1,3,6,1,4,1,259,10,1,14,89,55,5,5,1,10),_RlIgmpMldSnoopVlanRouterPortlist_Type())
rlIgmpMldSnoopVlanRouterPortlist.setMaxAccess(_B)
if mibBuilder.loadTexts:rlIgmpMldSnoopVlanRouterPortlist.setStatus(_A)
_RlIgmpMldSnoopVlanRouterStaticPortlist_Type=PortList
_RlIgmpMldSnoopVlanRouterStaticPortlist_Object=MibTableColumn
rlIgmpMldSnoopVlanRouterStaticPortlist=_RlIgmpMldSnoopVlanRouterStaticPortlist_Object((1,3,6,1,4,1,259,10,1,14,89,55,5,5,1,11),_RlIgmpMldSnoopVlanRouterStaticPortlist_Type())
rlIgmpMldSnoopVlanRouterStaticPortlist.setMaxAccess(_C)
if mibBuilder.loadTexts:rlIgmpMldSnoopVlanRouterStaticPortlist.setStatus(_A)
_RlIgmpMldSnoopVlanRouterForbiddenPortlist_Type=PortList
_RlIgmpMldSnoopVlanRouterForbiddenPortlist_Object=MibTableColumn
rlIgmpMldSnoopVlanRouterForbiddenPortlist=_RlIgmpMldSnoopVlanRouterForbiddenPortlist_Object((1,3,6,1,4,1,259,10,1,14,89,55,5,5,1,12),_RlIgmpMldSnoopVlanRouterForbiddenPortlist_Type())
rlIgmpMldSnoopVlanRouterForbiddenPortlist.setMaxAccess(_C)
if mibBuilder.loadTexts:rlIgmpMldSnoopVlanRouterForbiddenPortlist.setStatus(_A)
_RlIgmpMldSnoopVlanQueryOverride_Type=TruthValue
_RlIgmpMldSnoopVlanQueryOverride_Object=MibTableColumn
rlIgmpMldSnoopVlanQueryOverride=_RlIgmpMldSnoopVlanQueryOverride_Object((1,3,6,1,4,1,259,10,1,14,89,55,5,5,1,13),_RlIgmpMldSnoopVlanQueryOverride_Type())
rlIgmpMldSnoopVlanQueryOverride.setMaxAccess(_C)
if mibBuilder.loadTexts:rlIgmpMldSnoopVlanQueryOverride.setStatus(_A)
class _RlIgmpMldSnoopVlanOperRobustness_Type(Unsigned32):defaultValue=2;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_RlIgmpMldSnoopVlanOperRobustness_Type.__name__=_F
_RlIgmpMldSnoopVlanOperRobustness_Object=MibTableColumn
rlIgmpMldSnoopVlanOperRobustness=_RlIgmpMldSnoopVlanOperRobustness_Object((1,3,6,1,4,1,259,10,1,14,89,55,5,5,1,14),_RlIgmpMldSnoopVlanOperRobustness_Type())
rlIgmpMldSnoopVlanOperRobustness.setMaxAccess(_B)
if mibBuilder.loadTexts:rlIgmpMldSnoopVlanOperRobustness.setStatus(_A)
class _RlIgmpMldSnoopVlanOperQueryInterval_Type(Unsigned32):defaultValue=125000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1000,31744000))
_RlIgmpMldSnoopVlanOperQueryInterval_Type.__name__=_F
_RlIgmpMldSnoopVlanOperQueryInterval_Object=MibTableColumn
rlIgmpMldSnoopVlanOperQueryInterval=_RlIgmpMldSnoopVlanOperQueryInterval_Object((1,3,6,1,4,1,259,10,1,14,89,55,5,5,1,15),_RlIgmpMldSnoopVlanOperQueryInterval_Type())
rlIgmpMldSnoopVlanOperQueryInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:rlIgmpMldSnoopVlanOperQueryInterval.setStatus(_A)
if mibBuilder.loadTexts:rlIgmpMldSnoopVlanOperQueryInterval.setUnits(_I)
class _RlIgmpMldSnoopVlanOperQueryMaxResponseTime_Type(Unsigned32):defaultValue=10000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8387584))
_RlIgmpMldSnoopVlanOperQueryMaxResponseTime_Type.__name__=_F
_RlIgmpMldSnoopVlanOperQueryMaxResponseTime_Object=MibTableColumn
rlIgmpMldSnoopVlanOperQueryMaxResponseTime=_RlIgmpMldSnoopVlanOperQueryMaxResponseTime_Object((1,3,6,1,4,1,259,10,1,14,89,55,5,5,1,16),_RlIgmpMldSnoopVlanOperQueryMaxResponseTime_Type())
rlIgmpMldSnoopVlanOperQueryMaxResponseTime.setMaxAccess(_B)
if mibBuilder.loadTexts:rlIgmpMldSnoopVlanOperQueryMaxResponseTime.setStatus(_A)
if mibBuilder.loadTexts:rlIgmpMldSnoopVlanOperQueryMaxResponseTime.setUnits(_I)
class _RlIgmpMldSnoopVlanOperLastMemberQueryInterval_Type(Unsigned32):defaultValue=1000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8387584))
_RlIgmpMldSnoopVlanOperLastMemberQueryInterval_Type.__name__=_F
_RlIgmpMldSnoopVlanOperLastMemberQueryInterval_Object=MibTableColumn
rlIgmpMldSnoopVlanOperLastMemberQueryInterval=_RlIgmpMldSnoopVlanOperLastMemberQueryInterval_Object((1,3,6,1,4,1,259,10,1,14,89,55,5,5,1,17),_RlIgmpMldSnoopVlanOperLastMemberQueryInterval_Type())
rlIgmpMldSnoopVlanOperLastMemberQueryInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:rlIgmpMldSnoopVlanOperLastMemberQueryInterval.setStatus(_A)
if mibBuilder.loadTexts:rlIgmpMldSnoopVlanOperLastMemberQueryInterval.setUnits(_I)
class _RlIgmpMldSnoopVlanOperLastMemberQueryCount_Type(Unsigned32):defaultValue=2;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_RlIgmpMldSnoopVlanOperLastMemberQueryCount_Type.__name__=_F
_RlIgmpMldSnoopVlanOperLastMemberQueryCount_Object=MibTableColumn
rlIgmpMldSnoopVlanOperLastMemberQueryCount=_RlIgmpMldSnoopVlanOperLastMemberQueryCount_Object((1,3,6,1,4,1,259,10,1,14,89,55,5,5,1,18),_RlIgmpMldSnoopVlanOperLastMemberQueryCount_Type())
rlIgmpMldSnoopVlanOperLastMemberQueryCount.setMaxAccess(_B)
if mibBuilder.loadTexts:rlIgmpMldSnoopVlanOperLastMemberQueryCount.setStatus(_A)
class _RlIgmpMldSnoopVlanOperStartupQueryInterval_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31744000))
_RlIgmpMldSnoopVlanOperStartupQueryInterval_Type.__name__=_F
_RlIgmpMldSnoopVlanOperStartupQueryInterval_Object=MibTableColumn
rlIgmpMldSnoopVlanOperStartupQueryInterval=_RlIgmpMldSnoopVlanOperStartupQueryInterval_Object((1,3,6,1,4,1,259,10,1,14,89,55,5,5,1,19),_RlIgmpMldSnoopVlanOperStartupQueryInterval_Type())
rlIgmpMldSnoopVlanOperStartupQueryInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:rlIgmpMldSnoopVlanOperStartupQueryInterval.setStatus(_A)
if mibBuilder.loadTexts:rlIgmpMldSnoopVlanOperStartupQueryInterval.setUnits(_I)
class _RlIgmpMldSnoopVlanOperStartupQueryCount_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_RlIgmpMldSnoopVlanOperStartupQueryCount_Type.__name__=_F
_RlIgmpMldSnoopVlanOperStartupQueryCount_Object=MibTableColumn
rlIgmpMldSnoopVlanOperStartupQueryCount=_RlIgmpMldSnoopVlanOperStartupQueryCount_Object((1,3,6,1,4,1,259,10,1,14,89,55,5,5,1,20),_RlIgmpMldSnoopVlanOperStartupQueryCount_Type())
rlIgmpMldSnoopVlanOperStartupQueryCount.setMaxAccess(_B)
if mibBuilder.loadTexts:rlIgmpMldSnoopVlanOperStartupQueryCount.setStatus(_A)
class _RlIgmpMldSnoopVlanOperHostTimeOut_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_RlIgmpMldSnoopVlanOperHostTimeOut_Type.__name__=_F
_RlIgmpMldSnoopVlanOperHostTimeOut_Object=MibTableColumn
rlIgmpMldSnoopVlanOperHostTimeOut=_RlIgmpMldSnoopVlanOperHostTimeOut_Object((1,3,6,1,4,1,259,10,1,14,89,55,5,5,1,21),_RlIgmpMldSnoopVlanOperHostTimeOut_Type())
rlIgmpMldSnoopVlanOperHostTimeOut.setMaxAccess(_B)
if mibBuilder.loadTexts:rlIgmpMldSnoopVlanOperHostTimeOut.setStatus(_A)
if mibBuilder.loadTexts:rlIgmpMldSnoopVlanOperHostTimeOut.setUnits(_I)
class _RlIgmpMldSnoopVlanOperRouterTimeOut_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_RlIgmpMldSnoopVlanOperRouterTimeOut_Type.__name__=_F
_RlIgmpMldSnoopVlanOperRouterTimeOut_Object=MibTableColumn
rlIgmpMldSnoopVlanOperRouterTimeOut=_RlIgmpMldSnoopVlanOperRouterTimeOut_Object((1,3,6,1,4,1,259,10,1,14,89,55,5,5,1,22),_RlIgmpMldSnoopVlanOperRouterTimeOut_Type())
rlIgmpMldSnoopVlanOperRouterTimeOut.setMaxAccess(_B)
if mibBuilder.loadTexts:rlIgmpMldSnoopVlanOperRouterTimeOut.setStatus(_A)
if mibBuilder.loadTexts:rlIgmpMldSnoopVlanOperRouterTimeOut.setUnits(_I)
class _RlIgmpMldSnoopVlanOperLeaveTimeOut_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_RlIgmpMldSnoopVlanOperLeaveTimeOut_Type.__name__=_F
_RlIgmpMldSnoopVlanOperLeaveTimeOut_Object=MibTableColumn
rlIgmpMldSnoopVlanOperLeaveTimeOut=_RlIgmpMldSnoopVlanOperLeaveTimeOut_Object((1,3,6,1,4,1,259,10,1,14,89,55,5,5,1,23),_RlIgmpMldSnoopVlanOperLeaveTimeOut_Type())
rlIgmpMldSnoopVlanOperLeaveTimeOut.setMaxAccess(_B)
if mibBuilder.loadTexts:rlIgmpMldSnoopVlanOperLeaveTimeOut.setStatus(_A)
if mibBuilder.loadTexts:rlIgmpMldSnoopVlanOperLeaveTimeOut.setUnits(_I)
class _RlIgmpMldSnoopVlanAdminRobustness_Type(Unsigned32):defaultValue=2;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,7))
_RlIgmpMldSnoopVlanAdminRobustness_Type.__name__=_F
_RlIgmpMldSnoopVlanAdminRobustness_Object=MibTableColumn
rlIgmpMldSnoopVlanAdminRobustness=_RlIgmpMldSnoopVlanAdminRobustness_Object((1,3,6,1,4,1,259,10,1,14,89,55,5,5,1,24),_RlIgmpMldSnoopVlanAdminRobustness_Type())
rlIgmpMldSnoopVlanAdminRobustness.setMaxAccess(_C)
if mibBuilder.loadTexts:rlIgmpMldSnoopVlanAdminRobustness.setStatus(_A)
class _RlIgmpMldSnoopVlanAdminQueryInterval_Type(Unsigned32):defaultValue=125000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1000,18000000))
_RlIgmpMldSnoopVlanAdminQueryInterval_Type.__name__=_F
_RlIgmpMldSnoopVlanAdminQueryInterval_Object=MibTableColumn
rlIgmpMldSnoopVlanAdminQueryInterval=_RlIgmpMldSnoopVlanAdminQueryInterval_Object((1,3,6,1,4,1,259,10,1,14,89,55,5,5,1,25),_RlIgmpMldSnoopVlanAdminQueryInterval_Type())
rlIgmpMldSnoopVlanAdminQueryInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:rlIgmpMldSnoopVlanAdminQueryInterval.setStatus(_A)
if mibBuilder.loadTexts:rlIgmpMldSnoopVlanAdminQueryInterval.setUnits(_I)
class _RlIgmpMldSnoopVlanAdminQueryMaxResponseTime_Type(Unsigned32):defaultValue=10000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1000,20000))
_RlIgmpMldSnoopVlanAdminQueryMaxResponseTime_Type.__name__=_F
_RlIgmpMldSnoopVlanAdminQueryMaxResponseTime_Object=MibTableColumn
rlIgmpMldSnoopVlanAdminQueryMaxResponseTime=_RlIgmpMldSnoopVlanAdminQueryMaxResponseTime_Object((1,3,6,1,4,1,259,10,1,14,89,55,5,5,1,26),_RlIgmpMldSnoopVlanAdminQueryMaxResponseTime_Type())
rlIgmpMldSnoopVlanAdminQueryMaxResponseTime.setMaxAccess(_C)
if mibBuilder.loadTexts:rlIgmpMldSnoopVlanAdminQueryMaxResponseTime.setStatus(_A)
if mibBuilder.loadTexts:rlIgmpMldSnoopVlanAdminQueryMaxResponseTime.setUnits(_I)
class _RlIgmpMldSnoopVlanAdminLastMemberQueryInterval_Type(Unsigned32):defaultValue=1000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,25500))
_RlIgmpMldSnoopVlanAdminLastMemberQueryInterval_Type.__name__=_F
_RlIgmpMldSnoopVlanAdminLastMemberQueryInterval_Object=MibTableColumn
rlIgmpMldSnoopVlanAdminLastMemberQueryInterval=_RlIgmpMldSnoopVlanAdminLastMemberQueryInterval_Object((1,3,6,1,4,1,259,10,1,14,89,55,5,5,1,27),_RlIgmpMldSnoopVlanAdminLastMemberQueryInterval_Type())
rlIgmpMldSnoopVlanAdminLastMemberQueryInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:rlIgmpMldSnoopVlanAdminLastMemberQueryInterval.setStatus(_A)
if mibBuilder.loadTexts:rlIgmpMldSnoopVlanAdminLastMemberQueryInterval.setUnits(_I)
class _RlIgmpMldSnoopVlanAdminLastMemberQueryCount_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,7))
_RlIgmpMldSnoopVlanAdminLastMemberQueryCount_Type.__name__=_F
_RlIgmpMldSnoopVlanAdminLastMemberQueryCount_Object=MibTableColumn
rlIgmpMldSnoopVlanAdminLastMemberQueryCount=_RlIgmpMldSnoopVlanAdminLastMemberQueryCount_Object((1,3,6,1,4,1,259,10,1,14,89,55,5,5,1,28),_RlIgmpMldSnoopVlanAdminLastMemberQueryCount_Type())
rlIgmpMldSnoopVlanAdminLastMemberQueryCount.setMaxAccess(_C)
if mibBuilder.loadTexts:rlIgmpMldSnoopVlanAdminLastMemberQueryCount.setStatus(_A)
class _RlIgmpMldSnoopVlanAdminStartupQueryInterval_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4500000))
_RlIgmpMldSnoopVlanAdminStartupQueryInterval_Type.__name__=_F
_RlIgmpMldSnoopVlanAdminStartupQueryInterval_Object=MibTableColumn
rlIgmpMldSnoopVlanAdminStartupQueryInterval=_RlIgmpMldSnoopVlanAdminStartupQueryInterval_Object((1,3,6,1,4,1,259,10,1,14,89,55,5,5,1,29),_RlIgmpMldSnoopVlanAdminStartupQueryInterval_Type())
rlIgmpMldSnoopVlanAdminStartupQueryInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:rlIgmpMldSnoopVlanAdminStartupQueryInterval.setStatus(_A)
if mibBuilder.loadTexts:rlIgmpMldSnoopVlanAdminStartupQueryInterval.setUnits(_I)
class _RlIgmpMldSnoopVlanAdminStartupQueryCount_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_RlIgmpMldSnoopVlanAdminStartupQueryCount_Type.__name__=_F
_RlIgmpMldSnoopVlanAdminStartupQueryCount_Object=MibTableColumn
rlIgmpMldSnoopVlanAdminStartupQueryCount=_RlIgmpMldSnoopVlanAdminStartupQueryCount_Object((1,3,6,1,4,1,259,10,1,14,89,55,5,5,1,30),_RlIgmpMldSnoopVlanAdminStartupQueryCount_Type())
rlIgmpMldSnoopVlanAdminStartupQueryCount.setMaxAccess(_C)
if mibBuilder.loadTexts:rlIgmpMldSnoopVlanAdminStartupQueryCount.setStatus(_A)
class _RlIgmpMldSnoopVlanAdminHostTimeOut_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_RlIgmpMldSnoopVlanAdminHostTimeOut_Type.__name__=_F
_RlIgmpMldSnoopVlanAdminHostTimeOut_Object=MibTableColumn
rlIgmpMldSnoopVlanAdminHostTimeOut=_RlIgmpMldSnoopVlanAdminHostTimeOut_Object((1,3,6,1,4,1,259,10,1,14,89,55,5,5,1,31),_RlIgmpMldSnoopVlanAdminHostTimeOut_Type())
rlIgmpMldSnoopVlanAdminHostTimeOut.setMaxAccess(_C)
if mibBuilder.loadTexts:rlIgmpMldSnoopVlanAdminHostTimeOut.setStatus(_E)
if mibBuilder.loadTexts:rlIgmpMldSnoopVlanAdminHostTimeOut.setUnits(_I)
class _RlIgmpMldSnoopVlanAdminRouterTimeOut_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_RlIgmpMldSnoopVlanAdminRouterTimeOut_Type.__name__=_F
_RlIgmpMldSnoopVlanAdminRouterTimeOut_Object=MibTableColumn
rlIgmpMldSnoopVlanAdminRouterTimeOut=_RlIgmpMldSnoopVlanAdminRouterTimeOut_Object((1,3,6,1,4,1,259,10,1,14,89,55,5,5,1,32),_RlIgmpMldSnoopVlanAdminRouterTimeOut_Type())
rlIgmpMldSnoopVlanAdminRouterTimeOut.setMaxAccess(_C)
if mibBuilder.loadTexts:rlIgmpMldSnoopVlanAdminRouterTimeOut.setStatus(_E)
if mibBuilder.loadTexts:rlIgmpMldSnoopVlanAdminRouterTimeOut.setUnits(_I)
class _RlIgmpMldSnoopVlanAdminLeaveTimeOut_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_RlIgmpMldSnoopVlanAdminLeaveTimeOut_Type.__name__=_F
_RlIgmpMldSnoopVlanAdminLeaveTimeOut_Object=MibTableColumn
rlIgmpMldSnoopVlanAdminLeaveTimeOut=_RlIgmpMldSnoopVlanAdminLeaveTimeOut_Object((1,3,6,1,4,1,259,10,1,14,89,55,5,5,1,33),_RlIgmpMldSnoopVlanAdminLeaveTimeOut_Type())
rlIgmpMldSnoopVlanAdminLeaveTimeOut.setMaxAccess(_C)
if mibBuilder.loadTexts:rlIgmpMldSnoopVlanAdminLeaveTimeOut.setStatus(_E)
if mibBuilder.loadTexts:rlIgmpMldSnoopVlanAdminLeaveTimeOut.setUnits(_I)
class _RlIgmpMldSnoopVlanIsImmediateLeave_Type(TruthValue):defaultValue=2
_RlIgmpMldSnoopVlanIsImmediateLeave_Type.__name__=_N
_RlIgmpMldSnoopVlanIsImmediateLeave_Object=MibTableColumn
rlIgmpMldSnoopVlanIsImmediateLeave=_RlIgmpMldSnoopVlanIsImmediateLeave_Object((1,3,6,1,4,1,259,10,1,14,89,55,5,5,1,34),_RlIgmpMldSnoopVlanIsImmediateLeave_Type())
rlIgmpMldSnoopVlanIsImmediateLeave.setMaxAccess(_C)
if mibBuilder.loadTexts:rlIgmpMldSnoopVlanIsImmediateLeave.setStatus(_A)
_RlIgmpMldSnoopMulticastTvTable_Object=MibTable
rlIgmpMldSnoopMulticastTvTable=_RlIgmpMldSnoopMulticastTvTable_Object((1,3,6,1,4,1,259,10,1,14,89,55,5,6))
if mibBuilder.loadTexts:rlIgmpMldSnoopMulticastTvTable.setStatus(_A)
_RlIgmpMldSnoopMulticastTvEntry_Object=MibTableRow
rlIgmpMldSnoopMulticastTvEntry=_RlIgmpMldSnoopMulticastTvEntry_Object((1,3,6,1,4,1,259,10,1,14,89,55,5,6,1))
rlIgmpMldSnoopMulticastTvEntry.setIndexNames((0,_D,_c),(0,_D,_d),(0,_D,_e),(0,_D,_f))
if mibBuilder.loadTexts:rlIgmpMldSnoopMulticastTvEntry.setStatus(_A)
_RlIgmpMldSnoopMulticastTvInetAddressType_Type=InetAddressType
_RlIgmpMldSnoopMulticastTvInetAddressType_Object=MibTableColumn
rlIgmpMldSnoopMulticastTvInetAddressType=_RlIgmpMldSnoopMulticastTvInetAddressType_Object((1,3,6,1,4,1,259,10,1,14,89,55,5,6,1,1),_RlIgmpMldSnoopMulticastTvInetAddressType_Type())
rlIgmpMldSnoopMulticastTvInetAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:rlIgmpMldSnoopMulticastTvInetAddressType.setStatus(_A)
_RlIgmpMldSnoopMulticastTvVID_Type=VlanIndex
_RlIgmpMldSnoopMulticastTvVID_Object=MibTableColumn
rlIgmpMldSnoopMulticastTvVID=_RlIgmpMldSnoopMulticastTvVID_Object((1,3,6,1,4,1,259,10,1,14,89,55,5,6,1,2),_RlIgmpMldSnoopMulticastTvVID_Type())
rlIgmpMldSnoopMulticastTvVID.setMaxAccess(_B)
if mibBuilder.loadTexts:rlIgmpMldSnoopMulticastTvVID.setStatus(_A)
_RlIgmpMldSnoopMulticastTvGroupAddressType_Type=InetAddressType
_RlIgmpMldSnoopMulticastTvGroupAddressType_Object=MibTableColumn
rlIgmpMldSnoopMulticastTvGroupAddressType=_RlIgmpMldSnoopMulticastTvGroupAddressType_Object((1,3,6,1,4,1,259,10,1,14,89,55,5,6,1,3),_RlIgmpMldSnoopMulticastTvGroupAddressType_Type())
rlIgmpMldSnoopMulticastTvGroupAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:rlIgmpMldSnoopMulticastTvGroupAddressType.setStatus(_A)
_RlIgmpMldSnoopMulticastTvGroup_Type=InetAddress
_RlIgmpMldSnoopMulticastTvGroup_Object=MibTableColumn
rlIgmpMldSnoopMulticastTvGroup=_RlIgmpMldSnoopMulticastTvGroup_Object((1,3,6,1,4,1,259,10,1,14,89,55,5,6,1,4),_RlIgmpMldSnoopMulticastTvGroup_Type())
rlIgmpMldSnoopMulticastTvGroup.setMaxAccess(_B)
if mibBuilder.loadTexts:rlIgmpMldSnoopMulticastTvGroup.setStatus(_A)
_RlIgmpMldSnoopMulticastTvStatus_Type=RowStatus
_RlIgmpMldSnoopMulticastTvStatus_Object=MibTableColumn
rlIgmpMldSnoopMulticastTvStatus=_RlIgmpMldSnoopMulticastTvStatus_Object((1,3,6,1,4,1,259,10,1,14,89,55,5,6,1,5),_RlIgmpMldSnoopMulticastTvStatus_Type())
rlIgmpMldSnoopMulticastTvStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:rlIgmpMldSnoopMulticastTvStatus.setStatus(_A)
_RlIgmpMldSnoopQuerierVlanTable_Object=MibTable
rlIgmpMldSnoopQuerierVlanTable=_RlIgmpMldSnoopQuerierVlanTable_Object((1,3,6,1,4,1,259,10,1,14,89,55,5,7))
if mibBuilder.loadTexts:rlIgmpMldSnoopQuerierVlanTable.setStatus(_A)
_RlIgmpMldSnoopQuerierVlanEntry_Object=MibTableRow
rlIgmpMldSnoopQuerierVlanEntry=_RlIgmpMldSnoopQuerierVlanEntry_Object((1,3,6,1,4,1,259,10,1,14,89,55,5,7,1))
rlIgmpMldSnoopQuerierVlanEntry.setIndexNames((0,_D,_g))
if mibBuilder.loadTexts:rlIgmpMldSnoopQuerierVlanEntry.setStatus(_A)
_RlIgmpMldSnoopQuerierVlanTag_Type=VlanIndex
_RlIgmpMldSnoopQuerierVlanTag_Object=MibTableColumn
rlIgmpMldSnoopQuerierVlanTag=_RlIgmpMldSnoopQuerierVlanTag_Object((1,3,6,1,4,1,259,10,1,14,89,55,5,7,1,1),_RlIgmpMldSnoopQuerierVlanTag_Type())
rlIgmpMldSnoopQuerierVlanTag.setMaxAccess(_B)
if mibBuilder.loadTexts:rlIgmpMldSnoopQuerierVlanTag.setStatus(_A)
_RlIgmpMldSnoopQuerierAdminEnable_Type=TruthValue
_RlIgmpMldSnoopQuerierAdminEnable_Object=MibTableColumn
rlIgmpMldSnoopQuerierAdminEnable=_RlIgmpMldSnoopQuerierAdminEnable_Object((1,3,6,1,4,1,259,10,1,14,89,55,5,7,1,2),_RlIgmpMldSnoopQuerierAdminEnable_Type())
rlIgmpMldSnoopQuerierAdminEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:rlIgmpMldSnoopQuerierAdminEnable.setStatus(_A)
_RlIgmpMldSnoopQuerierOperEnable_Type=TruthValue
_RlIgmpMldSnoopQuerierOperEnable_Object=MibTableColumn
rlIgmpMldSnoopQuerierOperEnable=_RlIgmpMldSnoopQuerierOperEnable_Object((1,3,6,1,4,1,259,10,1,14,89,55,5,7,1,3),_RlIgmpMldSnoopQuerierOperEnable_Type())
rlIgmpMldSnoopQuerierOperEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:rlIgmpMldSnoopQuerierOperEnable.setStatus(_A)
_RlIgmpMldSnoopQuerierAdminAddrInetAddressType_Type=InetAddressType
_RlIgmpMldSnoopQuerierAdminAddrInetAddressType_Object=MibTableColumn
rlIgmpMldSnoopQuerierAdminAddrInetAddressType=_RlIgmpMldSnoopQuerierAdminAddrInetAddressType_Object((1,3,6,1,4,1,259,10,1,14,89,55,5,7,1,4),_RlIgmpMldSnoopQuerierAdminAddrInetAddressType_Type())
rlIgmpMldSnoopQuerierAdminAddrInetAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:rlIgmpMldSnoopQuerierAdminAddrInetAddressType.setStatus(_A)
_RlIgmpMldSnoopQuerierAdminAddr_Type=InetAddress
_RlIgmpMldSnoopQuerierAdminAddr_Object=MibTableColumn
rlIgmpMldSnoopQuerierAdminAddr=_RlIgmpMldSnoopQuerierAdminAddr_Object((1,3,6,1,4,1,259,10,1,14,89,55,5,7,1,5),_RlIgmpMldSnoopQuerierAdminAddr_Type())
rlIgmpMldSnoopQuerierAdminAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:rlIgmpMldSnoopQuerierAdminAddr.setStatus(_A)
_RlIgmpMldSnoopQuerierOperAddrInetAddressType_Type=InetAddressType
_RlIgmpMldSnoopQuerierOperAddrInetAddressType_Object=MibTableColumn
rlIgmpMldSnoopQuerierOperAddrInetAddressType=_RlIgmpMldSnoopQuerierOperAddrInetAddressType_Object((1,3,6,1,4,1,259,10,1,14,89,55,5,7,1,6),_RlIgmpMldSnoopQuerierOperAddrInetAddressType_Type())
rlIgmpMldSnoopQuerierOperAddrInetAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:rlIgmpMldSnoopQuerierOperAddrInetAddressType.setStatus(_A)
_RlIgmpMldSnoopQuerierOperAddr_Type=InetAddress
_RlIgmpMldSnoopQuerierOperAddr_Object=MibTableColumn
rlIgmpMldSnoopQuerierOperAddr=_RlIgmpMldSnoopQuerierOperAddr_Object((1,3,6,1,4,1,259,10,1,14,89,55,5,7,1,7),_RlIgmpMldSnoopQuerierOperAddr_Type())
rlIgmpMldSnoopQuerierOperAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:rlIgmpMldSnoopQuerierOperAddr.setStatus(_A)
_RlIgmpMldSnoopQuerierAdminVersionNumber_Type=IgmpVersion
_RlIgmpMldSnoopQuerierAdminVersionNumber_Object=MibTableColumn
rlIgmpMldSnoopQuerierAdminVersionNumber=_RlIgmpMldSnoopQuerierAdminVersionNumber_Object((1,3,6,1,4,1,259,10,1,14,89,55,5,7,1,8),_RlIgmpMldSnoopQuerierAdminVersionNumber_Type())
rlIgmpMldSnoopQuerierAdminVersionNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:rlIgmpMldSnoopQuerierAdminVersionNumber.setStatus(_A)
_RlIgmpMldSnoopQuerierOperVersionNumber_Type=IgmpVersion
_RlIgmpMldSnoopQuerierOperVersionNumber_Object=MibTableColumn
rlIgmpMldSnoopQuerierOperVersionNumber=_RlIgmpMldSnoopQuerierOperVersionNumber_Object((1,3,6,1,4,1,259,10,1,14,89,55,5,7,1,9),_RlIgmpMldSnoopQuerierOperVersionNumber_Type())
rlIgmpMldSnoopQuerierOperVersionNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:rlIgmpMldSnoopQuerierOperVersionNumber.setStatus(_A)
_RlBrgMulticastMibVersion_Type=Integer32
_RlBrgMulticastMibVersion_Object=MibScalar
rlBrgMulticastMibVersion=_RlBrgMulticastMibVersion_Object((1,3,6,1,4,1,259,10,1,14,89,116,1),_RlBrgMulticastMibVersion_Type())
rlBrgMulticastMibVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:rlBrgMulticastMibVersion.setStatus(_A)
_RlBrgStaticIpMulticastTable_Object=MibTable
rlBrgStaticIpMulticastTable=_RlBrgStaticIpMulticastTable_Object((1,3,6,1,4,1,259,10,1,14,89,116,3))
if mibBuilder.loadTexts:rlBrgStaticIpMulticastTable.setStatus(_A)
_RlBrgStaticIpMulticastEntry_Object=MibTableRow
rlBrgStaticIpMulticastEntry=_RlBrgStaticIpMulticastEntry_Object((1,3,6,1,4,1,259,10,1,14,89,116,3,1))
rlBrgStaticIpMulticastEntry.setIndexNames((0,_D,_h),(0,_D,_i),(0,_D,_j))
if mibBuilder.loadTexts:rlBrgStaticIpMulticastEntry.setStatus(_A)
_RlBrgStaticIpMulticastVlanTag_Type=VlanIndex
_RlBrgStaticIpMulticastVlanTag_Object=MibTableColumn
rlBrgStaticIpMulticastVlanTag=_RlBrgStaticIpMulticastVlanTag_Object((1,3,6,1,4,1,259,10,1,14,89,116,3,1,1),_RlBrgStaticIpMulticastVlanTag_Type())
rlBrgStaticIpMulticastVlanTag.setMaxAccess(_G)
if mibBuilder.loadTexts:rlBrgStaticIpMulticastVlanTag.setStatus(_A)
_RlBrgStaticIpMulticastGroupAddress_Type=IpAddress
_RlBrgStaticIpMulticastGroupAddress_Object=MibTableColumn
rlBrgStaticIpMulticastGroupAddress=_RlBrgStaticIpMulticastGroupAddress_Object((1,3,6,1,4,1,259,10,1,14,89,116,3,1,2),_RlBrgStaticIpMulticastGroupAddress_Type())
rlBrgStaticIpMulticastGroupAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:rlBrgStaticIpMulticastGroupAddress.setStatus(_A)
_RlBrgStaticIpMulticastSourceAddress_Type=IpAddress
_RlBrgStaticIpMulticastSourceAddress_Object=MibTableColumn
rlBrgStaticIpMulticastSourceAddress=_RlBrgStaticIpMulticastSourceAddress_Object((1,3,6,1,4,1,259,10,1,14,89,116,3,1,3),_RlBrgStaticIpMulticastSourceAddress_Type())
rlBrgStaticIpMulticastSourceAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:rlBrgStaticIpMulticastSourceAddress.setStatus(_A)
_RlBrgStaticIpMulticastFrwPorts_Type=PortList
_RlBrgStaticIpMulticastFrwPorts_Object=MibTableColumn
rlBrgStaticIpMulticastFrwPorts=_RlBrgStaticIpMulticastFrwPorts_Object((1,3,6,1,4,1,259,10,1,14,89,116,3,1,4),_RlBrgStaticIpMulticastFrwPorts_Type())
rlBrgStaticIpMulticastFrwPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:rlBrgStaticIpMulticastFrwPorts.setStatus(_A)
_RlBrgStaticIpMulticastForbiddenPorts_Type=PortList
_RlBrgStaticIpMulticastForbiddenPorts_Object=MibTableColumn
rlBrgStaticIpMulticastForbiddenPorts=_RlBrgStaticIpMulticastForbiddenPorts_Object((1,3,6,1,4,1,259,10,1,14,89,116,3,1,5),_RlBrgStaticIpMulticastForbiddenPorts_Type())
rlBrgStaticIpMulticastForbiddenPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:rlBrgStaticIpMulticastForbiddenPorts.setStatus(_A)
_RlBrgStaticIpMulticastStatus_Type=RowStatus
_RlBrgStaticIpMulticastStatus_Object=MibTableColumn
rlBrgStaticIpMulticastStatus=_RlBrgStaticIpMulticastStatus_Object((1,3,6,1,4,1,259,10,1,14,89,116,3,1,6),_RlBrgStaticIpMulticastStatus_Type())
rlBrgStaticIpMulticastStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:rlBrgStaticIpMulticastStatus.setStatus(_A)
_RlBrgIpMulticastTable_Object=MibTable
rlBrgIpMulticastTable=_RlBrgIpMulticastTable_Object((1,3,6,1,4,1,259,10,1,14,89,116,4))
if mibBuilder.loadTexts:rlBrgIpMulticastTable.setStatus(_A)
_RlBrgIpMulticastEntry_Object=MibTableRow
rlBrgIpMulticastEntry=_RlBrgIpMulticastEntry_Object((1,3,6,1,4,1,259,10,1,14,89,116,4,1))
rlBrgIpMulticastEntry.setIndexNames((0,_D,_k),(0,_D,_l),(0,_D,_m))
if mibBuilder.loadTexts:rlBrgIpMulticastEntry.setStatus(_A)
_RlBrgIpMulticastVlanTag_Type=VlanIndex
_RlBrgIpMulticastVlanTag_Object=MibTableColumn
rlBrgIpMulticastVlanTag=_RlBrgIpMulticastVlanTag_Object((1,3,6,1,4,1,259,10,1,14,89,116,4,1,1),_RlBrgIpMulticastVlanTag_Type())
rlBrgIpMulticastVlanTag.setMaxAccess(_G)
if mibBuilder.loadTexts:rlBrgIpMulticastVlanTag.setStatus(_A)
_RlBrgIpMulticastGroupAddress_Type=IpAddress
_RlBrgIpMulticastGroupAddress_Object=MibTableColumn
rlBrgIpMulticastGroupAddress=_RlBrgIpMulticastGroupAddress_Object((1,3,6,1,4,1,259,10,1,14,89,116,4,1,2),_RlBrgIpMulticastGroupAddress_Type())
rlBrgIpMulticastGroupAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:rlBrgIpMulticastGroupAddress.setStatus(_A)
_RlBrgIpMulticastSourceAddress_Type=IpAddress
_RlBrgIpMulticastSourceAddress_Object=MibTableColumn
rlBrgIpMulticastSourceAddress=_RlBrgIpMulticastSourceAddress_Object((1,3,6,1,4,1,259,10,1,14,89,116,4,1,3),_RlBrgIpMulticastSourceAddress_Type())
rlBrgIpMulticastSourceAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:rlBrgIpMulticastSourceAddress.setStatus(_A)
_RlBrgIpMulticastEgressPorts_Type=PortList
_RlBrgIpMulticastEgressPorts_Object=MibTableColumn
rlBrgIpMulticastEgressPorts=_RlBrgIpMulticastEgressPorts_Object((1,3,6,1,4,1,259,10,1,14,89,116,4,1,4),_RlBrgIpMulticastEgressPorts_Type())
rlBrgIpMulticastEgressPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:rlBrgIpMulticastEgressPorts.setStatus(_A)
_RlBrgIpMulticastLearntPorts_Type=PortList
_RlBrgIpMulticastLearntPorts_Object=MibTableColumn
rlBrgIpMulticastLearntPorts=_RlBrgIpMulticastLearntPorts_Object((1,3,6,1,4,1,259,10,1,14,89,116,4,1,5),_RlBrgIpMulticastLearntPorts_Type())
rlBrgIpMulticastLearntPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:rlBrgIpMulticastLearntPorts.setStatus(_A)
_RlBrgStaticInetMulticastTable_Object=MibTable
rlBrgStaticInetMulticastTable=_RlBrgStaticInetMulticastTable_Object((1,3,6,1,4,1,259,10,1,14,89,116,5))
if mibBuilder.loadTexts:rlBrgStaticInetMulticastTable.setStatus(_A)
_RlBrgStaticInetMulticastEntry_Object=MibTableRow
rlBrgStaticInetMulticastEntry=_RlBrgStaticInetMulticastEntry_Object((1,3,6,1,4,1,259,10,1,14,89,116,5,1))
rlBrgStaticInetMulticastEntry.setIndexNames((0,_D,_n),(0,_D,_o),(0,_D,_p),(0,_D,_q),(0,_D,_r))
if mibBuilder.loadTexts:rlBrgStaticInetMulticastEntry.setStatus(_A)
_RlBrgStaticInetMulticastVlanTag_Type=VlanIndex
_RlBrgStaticInetMulticastVlanTag_Object=MibTableColumn
rlBrgStaticInetMulticastVlanTag=_RlBrgStaticInetMulticastVlanTag_Object((1,3,6,1,4,1,259,10,1,14,89,116,5,1,1),_RlBrgStaticInetMulticastVlanTag_Type())
rlBrgStaticInetMulticastVlanTag.setMaxAccess(_G)
if mibBuilder.loadTexts:rlBrgStaticInetMulticastVlanTag.setStatus(_A)
_RlBrgStaticInetMulticastGroupAddressType_Type=InetAddressType
_RlBrgStaticInetMulticastGroupAddressType_Object=MibTableColumn
rlBrgStaticInetMulticastGroupAddressType=_RlBrgStaticInetMulticastGroupAddressType_Object((1,3,6,1,4,1,259,10,1,14,89,116,5,1,2),_RlBrgStaticInetMulticastGroupAddressType_Type())
rlBrgStaticInetMulticastGroupAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:rlBrgStaticInetMulticastGroupAddressType.setStatus(_A)
_RlBrgStaticInetMulticastGroupAddress_Type=InetAddress
_RlBrgStaticInetMulticastGroupAddress_Object=MibTableColumn
rlBrgStaticInetMulticastGroupAddress=_RlBrgStaticInetMulticastGroupAddress_Object((1,3,6,1,4,1,259,10,1,14,89,116,5,1,3),_RlBrgStaticInetMulticastGroupAddress_Type())
rlBrgStaticInetMulticastGroupAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:rlBrgStaticInetMulticastGroupAddress.setStatus(_A)
_RlBrgStaticInetMulticastSourceAddressType_Type=InetAddressType
_RlBrgStaticInetMulticastSourceAddressType_Object=MibTableColumn
rlBrgStaticInetMulticastSourceAddressType=_RlBrgStaticInetMulticastSourceAddressType_Object((1,3,6,1,4,1,259,10,1,14,89,116,5,1,4),_RlBrgStaticInetMulticastSourceAddressType_Type())
rlBrgStaticInetMulticastSourceAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:rlBrgStaticInetMulticastSourceAddressType.setStatus(_A)
_RlBrgStaticInetMulticastSourceAddress_Type=InetAddress
_RlBrgStaticInetMulticastSourceAddress_Object=MibTableColumn
rlBrgStaticInetMulticastSourceAddress=_RlBrgStaticInetMulticastSourceAddress_Object((1,3,6,1,4,1,259,10,1,14,89,116,5,1,5),_RlBrgStaticInetMulticastSourceAddress_Type())
rlBrgStaticInetMulticastSourceAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:rlBrgStaticInetMulticastSourceAddress.setStatus(_A)
_RlBrgStaticInetMulticastFrwPorts_Type=PortList
_RlBrgStaticInetMulticastFrwPorts_Object=MibTableColumn
rlBrgStaticInetMulticastFrwPorts=_RlBrgStaticInetMulticastFrwPorts_Object((1,3,6,1,4,1,259,10,1,14,89,116,5,1,6),_RlBrgStaticInetMulticastFrwPorts_Type())
rlBrgStaticInetMulticastFrwPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:rlBrgStaticInetMulticastFrwPorts.setStatus(_A)
_RlBrgStaticInetMulticastForbiddenPorts_Type=PortList
_RlBrgStaticInetMulticastForbiddenPorts_Object=MibTableColumn
rlBrgStaticInetMulticastForbiddenPorts=_RlBrgStaticInetMulticastForbiddenPorts_Object((1,3,6,1,4,1,259,10,1,14,89,116,5,1,7),_RlBrgStaticInetMulticastForbiddenPorts_Type())
rlBrgStaticInetMulticastForbiddenPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:rlBrgStaticInetMulticastForbiddenPorts.setStatus(_A)
_RlBrgStaticInetMulticastStatus_Type=RowStatus
_RlBrgStaticInetMulticastStatus_Object=MibTableColumn
rlBrgStaticInetMulticastStatus=_RlBrgStaticInetMulticastStatus_Object((1,3,6,1,4,1,259,10,1,14,89,116,5,1,8),_RlBrgStaticInetMulticastStatus_Type())
rlBrgStaticInetMulticastStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:rlBrgStaticInetMulticastStatus.setStatus(_A)
_RlBrgInetMulticastTable_Object=MibTable
rlBrgInetMulticastTable=_RlBrgInetMulticastTable_Object((1,3,6,1,4,1,259,10,1,14,89,116,6))
if mibBuilder.loadTexts:rlBrgInetMulticastTable.setStatus(_A)
_RlBrgInetMulticastEntry_Object=MibTableRow
rlBrgInetMulticastEntry=_RlBrgInetMulticastEntry_Object((1,3,6,1,4,1,259,10,1,14,89,116,6,1))
rlBrgInetMulticastEntry.setIndexNames((0,_D,_s),(0,_D,_t),(0,_D,_u),(0,_D,_v),(0,_D,_w))
if mibBuilder.loadTexts:rlBrgInetMulticastEntry.setStatus(_A)
_RlBrgInetMulticastVlanTag_Type=VlanIndex
_RlBrgInetMulticastVlanTag_Object=MibTableColumn
rlBrgInetMulticastVlanTag=_RlBrgInetMulticastVlanTag_Object((1,3,6,1,4,1,259,10,1,14,89,116,6,1,1),_RlBrgInetMulticastVlanTag_Type())
rlBrgInetMulticastVlanTag.setMaxAccess(_G)
if mibBuilder.loadTexts:rlBrgInetMulticastVlanTag.setStatus(_A)
_RlBrgInetMulticastGroupAddressType_Type=InetAddressType
_RlBrgInetMulticastGroupAddressType_Object=MibTableColumn
rlBrgInetMulticastGroupAddressType=_RlBrgInetMulticastGroupAddressType_Object((1,3,6,1,4,1,259,10,1,14,89,116,6,1,2),_RlBrgInetMulticastGroupAddressType_Type())
rlBrgInetMulticastGroupAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:rlBrgInetMulticastGroupAddressType.setStatus(_A)
_RlBrgInetMulticastGroupAddress_Type=InetAddress
_RlBrgInetMulticastGroupAddress_Object=MibTableColumn
rlBrgInetMulticastGroupAddress=_RlBrgInetMulticastGroupAddress_Object((1,3,6,1,4,1,259,10,1,14,89,116,6,1,3),_RlBrgInetMulticastGroupAddress_Type())
rlBrgInetMulticastGroupAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:rlBrgInetMulticastGroupAddress.setStatus(_A)
_RlBrgInetMulticastSourceAddressType_Type=InetAddressType
_RlBrgInetMulticastSourceAddressType_Object=MibTableColumn
rlBrgInetMulticastSourceAddressType=_RlBrgInetMulticastSourceAddressType_Object((1,3,6,1,4,1,259,10,1,14,89,116,6,1,4),_RlBrgInetMulticastSourceAddressType_Type())
rlBrgInetMulticastSourceAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:rlBrgInetMulticastSourceAddressType.setStatus(_A)
_RlBrgInetMulticastSourceAddress_Type=InetAddress
_RlBrgInetMulticastSourceAddress_Object=MibTableColumn
rlBrgInetMulticastSourceAddress=_RlBrgInetMulticastSourceAddress_Object((1,3,6,1,4,1,259,10,1,14,89,116,6,1,5),_RlBrgInetMulticastSourceAddress_Type())
rlBrgInetMulticastSourceAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:rlBrgInetMulticastSourceAddress.setStatus(_A)
_RlBrgInetMulticastEgressPorts_Type=PortList
_RlBrgInetMulticastEgressPorts_Object=MibTableColumn
rlBrgInetMulticastEgressPorts=_RlBrgInetMulticastEgressPorts_Object((1,3,6,1,4,1,259,10,1,14,89,116,6,1,6),_RlBrgInetMulticastEgressPorts_Type())
rlBrgInetMulticastEgressPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:rlBrgInetMulticastEgressPorts.setStatus(_A)
_RlBrgInetMulticastLearntPorts_Type=PortList
_RlBrgInetMulticastLearntPorts_Object=MibTableColumn
rlBrgInetMulticastLearntPorts=_RlBrgInetMulticastLearntPorts_Object((1,3,6,1,4,1,259,10,1,14,89,116,6,1,7),_RlBrgInetMulticastLearntPorts_Type())
rlBrgInetMulticastLearntPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:rlBrgInetMulticastLearntPorts.setStatus(_A)
_RlBrgIpmFdbRefTable_Object=MibTable
rlBrgIpmFdbRefTable=_RlBrgIpmFdbRefTable_Object((1,3,6,1,4,1,259,10,1,14,89,116,7))
if mibBuilder.loadTexts:rlBrgIpmFdbRefTable.setStatus(_A)
_RlBrgIpmFdbRefEntry_Object=MibTableRow
rlBrgIpmFdbRefEntry=_RlBrgIpmFdbRefEntry_Object((1,3,6,1,4,1,259,10,1,14,89,116,7,1))
rlBrgIpmFdbRefEntry.setIndexNames((0,_D,_x),(0,_D,_y),(0,_D,_z),(0,_D,_A0),(0,_D,_A1))
if mibBuilder.loadTexts:rlBrgIpmFdbRefEntry.setStatus(_A)
_RlBrgIpmFdbRefVlanTag_Type=VlanIndex
_RlBrgIpmFdbRefVlanTag_Object=MibTableColumn
rlBrgIpmFdbRefVlanTag=_RlBrgIpmFdbRefVlanTag_Object((1,3,6,1,4,1,259,10,1,14,89,116,7,1,1),_RlBrgIpmFdbRefVlanTag_Type())
rlBrgIpmFdbRefVlanTag.setMaxAccess(_G)
if mibBuilder.loadTexts:rlBrgIpmFdbRefVlanTag.setStatus(_A)
_RlBrgIpmFdbRefGroupAddressType_Type=InetAddressType
_RlBrgIpmFdbRefGroupAddressType_Object=MibTableColumn
rlBrgIpmFdbRefGroupAddressType=_RlBrgIpmFdbRefGroupAddressType_Object((1,3,6,1,4,1,259,10,1,14,89,116,7,1,2),_RlBrgIpmFdbRefGroupAddressType_Type())
rlBrgIpmFdbRefGroupAddressType.setMaxAccess(_G)
if mibBuilder.loadTexts:rlBrgIpmFdbRefGroupAddressType.setStatus(_A)
_RlBrgIpmFdbRefGroupAddress_Type=InetAddress
_RlBrgIpmFdbRefGroupAddress_Object=MibTableColumn
rlBrgIpmFdbRefGroupAddress=_RlBrgIpmFdbRefGroupAddress_Object((1,3,6,1,4,1,259,10,1,14,89,116,7,1,3),_RlBrgIpmFdbRefGroupAddress_Type())
rlBrgIpmFdbRefGroupAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:rlBrgIpmFdbRefGroupAddress.setStatus(_A)
_RlBrgIpmFdbRefSourceAddressType_Type=InetAddressType
_RlBrgIpmFdbRefSourceAddressType_Object=MibTableColumn
rlBrgIpmFdbRefSourceAddressType=_RlBrgIpmFdbRefSourceAddressType_Object((1,3,6,1,4,1,259,10,1,14,89,116,7,1,4),_RlBrgIpmFdbRefSourceAddressType_Type())
rlBrgIpmFdbRefSourceAddressType.setMaxAccess(_G)
if mibBuilder.loadTexts:rlBrgIpmFdbRefSourceAddressType.setStatus(_A)
_RlBrgIpmFdbRefSourceAddress_Type=InetAddress
_RlBrgIpmFdbRefSourceAddress_Object=MibTableColumn
rlBrgIpmFdbRefSourceAddress=_RlBrgIpmFdbRefSourceAddress_Object((1,3,6,1,4,1,259,10,1,14,89,116,7,1,5),_RlBrgIpmFdbRefSourceAddress_Type())
rlBrgIpmFdbRefSourceAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:rlBrgIpmFdbRefSourceAddress.setStatus(_A)
_RlBrgIpmFdbRefPorts_Type=PortList
_RlBrgIpmFdbRefPorts_Object=MibTableColumn
rlBrgIpmFdbRefPorts=_RlBrgIpmFdbRefPorts_Object((1,3,6,1,4,1,259,10,1,14,89,116,7,1,6),_RlBrgIpmFdbRefPorts_Type())
rlBrgIpmFdbRefPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:rlBrgIpmFdbRefPorts.setStatus(_A)
_RlBrgDynamicCmdTable_Object=MibTable
rlBrgDynamicCmdTable=_RlBrgDynamicCmdTable_Object((1,3,6,1,4,1,259,10,1,14,89,116,8))
if mibBuilder.loadTexts:rlBrgDynamicCmdTable.setStatus(_A)
_RlBrgDynamicCmdEntry_Object=MibTableRow
rlBrgDynamicCmdEntry=_RlBrgDynamicCmdEntry_Object((1,3,6,1,4,1,259,10,1,14,89,116,8,1))
rlBrgDynamicCmdEntry.setIndexNames((0,_D,_A2))
if mibBuilder.loadTexts:rlBrgDynamicCmdEntry.setStatus(_A)
class _RlBrgDynamicCmdKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_RlBrgDynamicCmdKey_Type.__name__=_H
_RlBrgDynamicCmdKey_Object=MibTableColumn
rlBrgDynamicCmdKey=_RlBrgDynamicCmdKey_Object((1,3,6,1,4,1,259,10,1,14,89,116,8,1,1),_RlBrgDynamicCmdKey_Type())
rlBrgDynamicCmdKey.setMaxAccess(_G)
if mibBuilder.loadTexts:rlBrgDynamicCmdKey.setStatus(_A)
_RlBrgDynamicCmdVlanTag_Type=VlanIndex
_RlBrgDynamicCmdVlanTag_Object=MibTableColumn
rlBrgDynamicCmdVlanTag=_RlBrgDynamicCmdVlanTag_Object((1,3,6,1,4,1,259,10,1,14,89,116,8,1,2),_RlBrgDynamicCmdVlanTag_Type())
rlBrgDynamicCmdVlanTag.setMaxAccess(_C)
if mibBuilder.loadTexts:rlBrgDynamicCmdVlanTag.setStatus(_A)
_RlBrgDynamicCmdGroupAddressType_Type=InetAddressType
_RlBrgDynamicCmdGroupAddressType_Object=MibTableColumn
rlBrgDynamicCmdGroupAddressType=_RlBrgDynamicCmdGroupAddressType_Object((1,3,6,1,4,1,259,10,1,14,89,116,8,1,3),_RlBrgDynamicCmdGroupAddressType_Type())
rlBrgDynamicCmdGroupAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:rlBrgDynamicCmdGroupAddressType.setStatus(_A)
_RlBrgDynamicCmdGroupAddress_Type=InetAddress
_RlBrgDynamicCmdGroupAddress_Object=MibTableColumn
rlBrgDynamicCmdGroupAddress=_RlBrgDynamicCmdGroupAddress_Object((1,3,6,1,4,1,259,10,1,14,89,116,8,1,4),_RlBrgDynamicCmdGroupAddress_Type())
rlBrgDynamicCmdGroupAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:rlBrgDynamicCmdGroupAddress.setStatus(_A)
_RlBrgDynamicCmdSourceAddressType_Type=InetAddressType
_RlBrgDynamicCmdSourceAddressType_Object=MibTableColumn
rlBrgDynamicCmdSourceAddressType=_RlBrgDynamicCmdSourceAddressType_Object((1,3,6,1,4,1,259,10,1,14,89,116,8,1,5),_RlBrgDynamicCmdSourceAddressType_Type())
rlBrgDynamicCmdSourceAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:rlBrgDynamicCmdSourceAddressType.setStatus(_A)
_RlBrgDynamicCmdSourceAddress_Type=InetAddress
_RlBrgDynamicCmdSourceAddress_Object=MibTableColumn
rlBrgDynamicCmdSourceAddress=_RlBrgDynamicCmdSourceAddress_Object((1,3,6,1,4,1,259,10,1,14,89,116,8,1,6),_RlBrgDynamicCmdSourceAddress_Type())
rlBrgDynamicCmdSourceAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:rlBrgDynamicCmdSourceAddress.setStatus(_A)
_RlBrgDynamicCmdPorts_Type=PortList
_RlBrgDynamicCmdPorts_Object=MibTableColumn
rlBrgDynamicCmdPorts=_RlBrgDynamicCmdPorts_Object((1,3,6,1,4,1,259,10,1,14,89,116,8,1,7),_RlBrgDynamicCmdPorts_Type())
rlBrgDynamicCmdPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:rlBrgDynamicCmdPorts.setStatus(_A)
_RlBrgDynamicCmdType_Type=DynamicCmdType
_RlBrgDynamicCmdType_Object=MibTableColumn
rlBrgDynamicCmdType=_RlBrgDynamicCmdType_Object((1,3,6,1,4,1,259,10,1,14,89,116,8,1,8),_RlBrgDynamicCmdType_Type())
rlBrgDynamicCmdType.setMaxAccess(_C)
if mibBuilder.loadTexts:rlBrgDynamicCmdType.setStatus(_A)
rlMacMulticastUnregFilterFailed=NotificationType((1,3,6,1,4,1,259,10,1,14,89,0,1))
rlMacMulticastUnregFilterFailed.setObjects(*((_K,_L),(_K,_M)))
if mibBuilder.loadTexts:rlMacMulticastUnregFilterFailed.setStatus('')
rlIgmpMldSnoopTriplePlayPort=NotificationType((1,3,6,1,4,1,259,10,1,14,89,0,208))
rlIgmpMldSnoopTriplePlayPort.setObjects(*((_K,_L),(_K,_M)))
if mibBuilder.loadTexts:rlIgmpMldSnoopTriplePlayPort.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'IgmpVersion':IgmpVersion,'DynamicCmdType':DynamicCmdType,'rlMacMulticastUnregFilterFailed':rlMacMulticastUnregFilterFailed,'rlIgmpMldSnoopTriplePlayPort':rlIgmpMldSnoopTriplePlayPort,'rlMacMulticastEnable':rlMacMulticastEnable,'rlIgmpSnoop':rlIgmpSnoop,'rlIgmpSnoopMibVersion':rlIgmpSnoopMibVersion,'rlIgmpSnoopEnable':rlIgmpSnoopEnable,'rlIgmpSnoopHostAgingTime':rlIgmpSnoopHostAgingTime,'rlIgmpSnoopRouterAgingTime':rlIgmpSnoopRouterAgingTime,'rlIgmpSnoopVlanTable':rlIgmpSnoopVlanTable,'rlIgmpSnoopVlanEntry':rlIgmpSnoopVlanEntry,_O:rlIgmpSnoopVlanTag,'rlIgmpSnoopVlanEnable':rlIgmpSnoopVlanEnable,'rlIgmpSnoopVlanRouterLearn':rlIgmpSnoopVlanRouterLearn,'rlIgmpSnoopVlanHostTimeOut':rlIgmpSnoopVlanHostTimeOut,'rlIgmpSnoopVlanQuerierTimeOut':rlIgmpSnoopVlanQuerierTimeOut,'rlIgmpSnoopVlanRouterTimeOut':rlIgmpSnoopVlanRouterTimeOut,'rlIgmpSnoopVlanLeaveTimeOut':rlIgmpSnoopVlanLeaveTimeOut,'rlIgmpSnoopVlanIgmpVersion':rlIgmpSnoopVlanIgmpVersion,'rlIgmpSnoopVlanRouterPortlist':rlIgmpSnoopVlanRouterPortlist,'rlIgmpSnoopIGMP224ReportsHandle':rlIgmpSnoopIGMP224ReportsHandle,'rlIgmpSnoopMulticastTvTable':rlIgmpSnoopMulticastTvTable,'rlIgmpSnoopMulticastTvEntry':rlIgmpSnoopMulticastTvEntry,_P:rlIgmpSnoopMulticastTvVID,_Q:rlIgmpSnoopMulticastTvGroup,'rlIgmpSnoopMulticastTvStatus':rlIgmpSnoopMulticastTvStatus,'rlIgmpSnoopMembershipTable':rlIgmpSnoopMembershipTable,'rlIgmpSnoopMembershipEntry':rlIgmpSnoopMembershipEntry,_R:rlIgmpSnoopMembershipVlanTag,_S:rlIgmpSnoopMembershipGroupIpAddress,_T:rlIgmpSnoopMembershipSourceIpAddress,'rlIgmpSnoopMembershipIncPortlist':rlIgmpSnoopMembershipIncPortlist,'rlIgmpSnoopMembershipExcPortlist':rlIgmpSnoopMembershipExcPortlist,'rlIgmpSnoopMembershipExpiryTime':rlIgmpSnoopMembershipExpiryTime,'rlIgmpSnoopMembershipCompatibilityMode':rlIgmpSnoopMembershipCompatibilityMode,'rlIgmpSnoopQuerierVlanTable':rlIgmpSnoopQuerierVlanTable,'rlIgmpSnoopQuerierVlanEntry':rlIgmpSnoopQuerierVlanEntry,_U:rlIgmpSnoopQuerierVlanTag,'rlIgmpSnoopQuerierAdminEnable':rlIgmpSnoopQuerierAdminEnable,'rlIgmpSnoopQuerierOperEnable':rlIgmpSnoopQuerierOperEnable,'rlIgmpSnoopQuerierAdminAddr':rlIgmpSnoopQuerierAdminAddr,'rlIgmpSnoopQuerierOperAddr':rlIgmpSnoopQuerierOperAddr,'rlIgmpSnoopQuerierAdminVersionNumber':rlIgmpSnoopQuerierAdminVersionNumber,'rlIgmpSnoopQuerierOperVersionNumber':rlIgmpSnoopQuerierOperVersionNumber,'rlMacMulticastMaxEntriesNum':rlMacMulticastMaxEntriesNum,'rlMacMulticastFilter':rlMacMulticastFilter,'rlMacMulticastUnregFilterEnable':rlMacMulticastUnregFilterEnable,'rlMldSnoop':rlMldSnoop,'rlMldSnoopEnable':rlMldSnoopEnable,'rlMldSnoopHostAgingTime':rlMldSnoopHostAgingTime,'rlMldSnoopRouterAgingTime':rlMldSnoopRouterAgingTime,'rlIgmpMldSnoopMembershipTable':rlIgmpMldSnoopMembershipTable,'rlIgmpMldSnoopMembershipEntry':rlIgmpMldSnoopMembershipEntry,_V:rlIgmpMldSnoopMembershipVlanTag,_W:rlIgmpMldSnoopMembershipGroupIpAddressType,_X:rlIgmpMldSnoopMembershipGroupIpAddress,_Y:rlIgmpMldSnoopMembershipSourceIpAddressType,_Z:rlIgmpMldSnoopMembershipSourceIpAddress,'rlIgmpMldSnoopMembershipIncPortlist':rlIgmpMldSnoopMembershipIncPortlist,'rlIgmpMldSnoopMembershipExcPortlist':rlIgmpMldSnoopMembershipExcPortlist,'rlIgmpMldSnoopMembershipExpiryTime':rlIgmpMldSnoopMembershipExpiryTime,'rlIgmpMldSnoopMembershipCompatibilityMode':rlIgmpMldSnoopMembershipCompatibilityMode,'rlIgmpMldSnoopVlanTable':rlIgmpMldSnoopVlanTable,'rlIgmpMldSnoopVlanEntry':rlIgmpMldSnoopVlanEntry,_a:rlIgmpMldSnoopVlanInetAddressType,_b:rlIgmpMldSnoopVlanTag,'rlIgmpMldSnoopVlanEnable':rlIgmpMldSnoopVlanEnable,'rlIgmpMldSnoopVlanRouterLearn':rlIgmpMldSnoopVlanRouterLearn,'rlIgmpMldSnoopVlanHostTimeOut':rlIgmpMldSnoopVlanHostTimeOut,'rlIgmpMldSnoopVlanQuerierTimeOut':rlIgmpMldSnoopVlanQuerierTimeOut,'rlIgmpMldSnoopVlanRouterTimeOut':rlIgmpMldSnoopVlanRouterTimeOut,'rlIgmpMldSnoopVlanLeaveTimeOut':rlIgmpMldSnoopVlanLeaveTimeOut,'rlIgmpMldSnoopVlanIgmpVersion':rlIgmpMldSnoopVlanIgmpVersion,'rlIgmpMldSnoopVlanRouterPortlist':rlIgmpMldSnoopVlanRouterPortlist,'rlIgmpMldSnoopVlanRouterStaticPortlist':rlIgmpMldSnoopVlanRouterStaticPortlist,'rlIgmpMldSnoopVlanRouterForbiddenPortlist':rlIgmpMldSnoopVlanRouterForbiddenPortlist,'rlIgmpMldSnoopVlanQueryOverride':rlIgmpMldSnoopVlanQueryOverride,'rlIgmpMldSnoopVlanOperRobustness':rlIgmpMldSnoopVlanOperRobustness,'rlIgmpMldSnoopVlanOperQueryInterval':rlIgmpMldSnoopVlanOperQueryInterval,'rlIgmpMldSnoopVlanOperQueryMaxResponseTime':rlIgmpMldSnoopVlanOperQueryMaxResponseTime,'rlIgmpMldSnoopVlanOperLastMemberQueryInterval':rlIgmpMldSnoopVlanOperLastMemberQueryInterval,'rlIgmpMldSnoopVlanOperLastMemberQueryCount':rlIgmpMldSnoopVlanOperLastMemberQueryCount,'rlIgmpMldSnoopVlanOperStartupQueryInterval':rlIgmpMldSnoopVlanOperStartupQueryInterval,'rlIgmpMldSnoopVlanOperStartupQueryCount':rlIgmpMldSnoopVlanOperStartupQueryCount,'rlIgmpMldSnoopVlanOperHostTimeOut':rlIgmpMldSnoopVlanOperHostTimeOut,'rlIgmpMldSnoopVlanOperRouterTimeOut':rlIgmpMldSnoopVlanOperRouterTimeOut,'rlIgmpMldSnoopVlanOperLeaveTimeOut':rlIgmpMldSnoopVlanOperLeaveTimeOut,'rlIgmpMldSnoopVlanAdminRobustness':rlIgmpMldSnoopVlanAdminRobustness,'rlIgmpMldSnoopVlanAdminQueryInterval':rlIgmpMldSnoopVlanAdminQueryInterval,'rlIgmpMldSnoopVlanAdminQueryMaxResponseTime':rlIgmpMldSnoopVlanAdminQueryMaxResponseTime,'rlIgmpMldSnoopVlanAdminLastMemberQueryInterval':rlIgmpMldSnoopVlanAdminLastMemberQueryInterval,'rlIgmpMldSnoopVlanAdminLastMemberQueryCount':rlIgmpMldSnoopVlanAdminLastMemberQueryCount,'rlIgmpMldSnoopVlanAdminStartupQueryInterval':rlIgmpMldSnoopVlanAdminStartupQueryInterval,'rlIgmpMldSnoopVlanAdminStartupQueryCount':rlIgmpMldSnoopVlanAdminStartupQueryCount,'rlIgmpMldSnoopVlanAdminHostTimeOut':rlIgmpMldSnoopVlanAdminHostTimeOut,'rlIgmpMldSnoopVlanAdminRouterTimeOut':rlIgmpMldSnoopVlanAdminRouterTimeOut,'rlIgmpMldSnoopVlanAdminLeaveTimeOut':rlIgmpMldSnoopVlanAdminLeaveTimeOut,'rlIgmpMldSnoopVlanIsImmediateLeave':rlIgmpMldSnoopVlanIsImmediateLeave,'rlIgmpMldSnoopMulticastTvTable':rlIgmpMldSnoopMulticastTvTable,'rlIgmpMldSnoopMulticastTvEntry':rlIgmpMldSnoopMulticastTvEntry,_c:rlIgmpMldSnoopMulticastTvInetAddressType,_d:rlIgmpMldSnoopMulticastTvVID,_e:rlIgmpMldSnoopMulticastTvGroupAddressType,_f:rlIgmpMldSnoopMulticastTvGroup,'rlIgmpMldSnoopMulticastTvStatus':rlIgmpMldSnoopMulticastTvStatus,'rlIgmpMldSnoopQuerierVlanTable':rlIgmpMldSnoopQuerierVlanTable,'rlIgmpMldSnoopQuerierVlanEntry':rlIgmpMldSnoopQuerierVlanEntry,_g:rlIgmpMldSnoopQuerierVlanTag,'rlIgmpMldSnoopQuerierAdminEnable':rlIgmpMldSnoopQuerierAdminEnable,'rlIgmpMldSnoopQuerierOperEnable':rlIgmpMldSnoopQuerierOperEnable,'rlIgmpMldSnoopQuerierAdminAddrInetAddressType':rlIgmpMldSnoopQuerierAdminAddrInetAddressType,'rlIgmpMldSnoopQuerierAdminAddr':rlIgmpMldSnoopQuerierAdminAddr,'rlIgmpMldSnoopQuerierOperAddrInetAddressType':rlIgmpMldSnoopQuerierOperAddrInetAddressType,'rlIgmpMldSnoopQuerierOperAddr':rlIgmpMldSnoopQuerierOperAddr,'rlIgmpMldSnoopQuerierAdminVersionNumber':rlIgmpMldSnoopQuerierAdminVersionNumber,'rlIgmpMldSnoopQuerierOperVersionNumber':rlIgmpMldSnoopQuerierOperVersionNumber,'rlBrgMulticastMibVersion':rlBrgMulticastMibVersion,'rlBrgStaticIpMulticastTable':rlBrgStaticIpMulticastTable,'rlBrgStaticIpMulticastEntry':rlBrgStaticIpMulticastEntry,_h:rlBrgStaticIpMulticastVlanTag,_i:rlBrgStaticIpMulticastGroupAddress,_j:rlBrgStaticIpMulticastSourceAddress,'rlBrgStaticIpMulticastFrwPorts':rlBrgStaticIpMulticastFrwPorts,'rlBrgStaticIpMulticastForbiddenPorts':rlBrgStaticIpMulticastForbiddenPorts,'rlBrgStaticIpMulticastStatus':rlBrgStaticIpMulticastStatus,'rlBrgIpMulticastTable':rlBrgIpMulticastTable,'rlBrgIpMulticastEntry':rlBrgIpMulticastEntry,_k:rlBrgIpMulticastVlanTag,_l:rlBrgIpMulticastGroupAddress,_m:rlBrgIpMulticastSourceAddress,'rlBrgIpMulticastEgressPorts':rlBrgIpMulticastEgressPorts,'rlBrgIpMulticastLearntPorts':rlBrgIpMulticastLearntPorts,'rlBrgStaticInetMulticastTable':rlBrgStaticInetMulticastTable,'rlBrgStaticInetMulticastEntry':rlBrgStaticInetMulticastEntry,_n:rlBrgStaticInetMulticastVlanTag,_o:rlBrgStaticInetMulticastGroupAddressType,_p:rlBrgStaticInetMulticastGroupAddress,_q:rlBrgStaticInetMulticastSourceAddressType,_r:rlBrgStaticInetMulticastSourceAddress,'rlBrgStaticInetMulticastFrwPorts':rlBrgStaticInetMulticastFrwPorts,'rlBrgStaticInetMulticastForbiddenPorts':rlBrgStaticInetMulticastForbiddenPorts,'rlBrgStaticInetMulticastStatus':rlBrgStaticInetMulticastStatus,'rlBrgInetMulticastTable':rlBrgInetMulticastTable,'rlBrgInetMulticastEntry':rlBrgInetMulticastEntry,_s:rlBrgInetMulticastVlanTag,_t:rlBrgInetMulticastGroupAddressType,_u:rlBrgInetMulticastGroupAddress,_v:rlBrgInetMulticastSourceAddressType,_w:rlBrgInetMulticastSourceAddress,'rlBrgInetMulticastEgressPorts':rlBrgInetMulticastEgressPorts,'rlBrgInetMulticastLearntPorts':rlBrgInetMulticastLearntPorts,'rlBrgIpmFdbRefTable':rlBrgIpmFdbRefTable,'rlBrgIpmFdbRefEntry':rlBrgIpmFdbRefEntry,_x:rlBrgIpmFdbRefVlanTag,_y:rlBrgIpmFdbRefGroupAddressType,_z:rlBrgIpmFdbRefGroupAddress,_A0:rlBrgIpmFdbRefSourceAddressType,_A1:rlBrgIpmFdbRefSourceAddress,'rlBrgIpmFdbRefPorts':rlBrgIpmFdbRefPorts,'rlBrgDynamicCmdTable':rlBrgDynamicCmdTable,'rlBrgDynamicCmdEntry':rlBrgDynamicCmdEntry,_A2:rlBrgDynamicCmdKey,'rlBrgDynamicCmdVlanTag':rlBrgDynamicCmdVlanTag,'rlBrgDynamicCmdGroupAddressType':rlBrgDynamicCmdGroupAddressType,'rlBrgDynamicCmdGroupAddress':rlBrgDynamicCmdGroupAddress,'rlBrgDynamicCmdSourceAddressType':rlBrgDynamicCmdSourceAddressType,'rlBrgDynamicCmdSourceAddress':rlBrgDynamicCmdSourceAddress,'rlBrgDynamicCmdPorts':rlBrgDynamicCmdPorts,'rlBrgDynamicCmdType':rlBrgDynamicCmdType})