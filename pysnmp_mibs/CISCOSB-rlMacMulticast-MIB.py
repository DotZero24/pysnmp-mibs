_g='rlIgmpMldSnoopQuerierGlobalAddressIPVersion'
_f='rlMldSnoopQuerierVlanTag'
_e='rlIgmpMldSnoopMulticastTvGroup'
_d='rlIgmpMldSnoopMulticastTvGroupAddressType'
_c='rlIgmpMldSnoopMulticastTvVID'
_b='rlIgmpMldSnoopMulticastTvInetAddressType'
_a='rlIgmpMldSnoopVlanTag'
_Z='rlIgmpMldSnoopVlanInetAddressType'
_Y='rlIgmpMldSnoopMembershipSourceIpAddress'
_X='rlIgmpMldSnoopMembershipSourceIpAddressType'
_W='rlIgmpMldSnoopMembershipGroupIpAddress'
_V='rlIgmpMldSnoopMembershipGroupIpAddressType'
_U='rlIgmpMldSnoopMembershipVlanTag'
_T='rlIgmpSnoopQuerierVlanTag'
_S='rlIgmpSnoopMembershipSourceIpAddress'
_R='rlIgmpSnoopMembershipGroupIpAddress'
_Q='rlIgmpSnoopMembershipVlanTag'
_P='rlIgmpSnoopMulticastTvGroup'
_O='rlIgmpSnoopMulticastTvVID'
_N='rlIgmpSnoopVlanTag'
_M='TruthValue'
_L='rndErrorSeverity'
_K='rndErrorDesc'
_J='CISCOSB-DEVICEPARAMS-MIB'
_I='seconds'
_H='milliseconds'
_G='Integer32'
_F='CISCOSB-rlMacMulticast-MIB'
_E='Unsigned32'
_D='obsolete'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
rndErrorDesc,rndErrorSeverity=mibBuilder.importSymbols(_J,_K,_L)
rlMacMulticast,switch001=mibBuilder.importSymbols('CISCOSB-MIB','rlMacMulticast','switch001')
rndNotifications,=mibBuilder.importSymbols('CISCOSB-TRAPS-MIB','rndNotifications')
InetAddress,InetAddressType,InetVersion=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType','InetVersion')
PortList,VlanIndex=mibBuilder.importSymbols('Q-BRIDGE-MIB','PortList','VlanIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_M)
class IgmpVersion(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('none',0),('v1',1),('v2',2),('v3',3)))
class MldVersion(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('none',0),('v1',1),('v2',2)))
_RlMacMulticastEnable_Type=TruthValue
_RlMacMulticastEnable_Object=MibScalar
rlMacMulticastEnable=_RlMacMulticastEnable_Object((1,3,6,1,4,1,9,6,1,101,55,1),_RlMacMulticastEnable_Type())
rlMacMulticastEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:rlMacMulticastEnable.setStatus(_A)
_RlIgmpSnoop_ObjectIdentity=ObjectIdentity
rlIgmpSnoop=_RlIgmpSnoop_ObjectIdentity((1,3,6,1,4,1,9,6,1,101,55,2))
_RlIgmpSnoopMibVersion_Type=Integer32
_RlIgmpSnoopMibVersion_Object=MibScalar
rlIgmpSnoopMibVersion=_RlIgmpSnoopMibVersion_Object((1,3,6,1,4,1,9,6,1,101,55,2,1),_RlIgmpSnoopMibVersion_Type())
rlIgmpSnoopMibVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:rlIgmpSnoopMibVersion.setStatus(_A)
_RlIgmpSnoopEnable_Type=TruthValue
_RlIgmpSnoopEnable_Object=MibScalar
rlIgmpSnoopEnable=_RlIgmpSnoopEnable_Object((1,3,6,1,4,1,9,6,1,101,55,2,2),_RlIgmpSnoopEnable_Type())
rlIgmpSnoopEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:rlIgmpSnoopEnable.setStatus(_A)
class _RlIgmpSnoopHostAgingTime_Type(Integer32):defaultValue=260;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_RlIgmpSnoopHostAgingTime_Type.__name__=_G
_RlIgmpSnoopHostAgingTime_Object=MibScalar
rlIgmpSnoopHostAgingTime=_RlIgmpSnoopHostAgingTime_Object((1,3,6,1,4,1,9,6,1,101,55,2,3),_RlIgmpSnoopHostAgingTime_Type())
rlIgmpSnoopHostAgingTime.setMaxAccess(_C)
if mibBuilder.loadTexts:rlIgmpSnoopHostAgingTime.setStatus(_D)
if mibBuilder.loadTexts:rlIgmpSnoopHostAgingTime.setUnits(_I)
class _RlIgmpSnoopRouterAgingTime_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_RlIgmpSnoopRouterAgingTime_Type.__name__=_G
_RlIgmpSnoopRouterAgingTime_Object=MibScalar
rlIgmpSnoopRouterAgingTime=_RlIgmpSnoopRouterAgingTime_Object((1,3,6,1,4,1,9,6,1,101,55,2,4),_RlIgmpSnoopRouterAgingTime_Type())
rlIgmpSnoopRouterAgingTime.setMaxAccess(_C)
if mibBuilder.loadTexts:rlIgmpSnoopRouterAgingTime.setStatus(_D)
if mibBuilder.loadTexts:rlIgmpSnoopRouterAgingTime.setUnits(_I)
_RlIgmpSnoopVlanTable_Object=MibTable
rlIgmpSnoopVlanTable=_RlIgmpSnoopVlanTable_Object((1,3,6,1,4,1,9,6,1,101,55,2,7))
if mibBuilder.loadTexts:rlIgmpSnoopVlanTable.setStatus(_D)
_RlIgmpSnoopVlanEntry_Object=MibTableRow
rlIgmpSnoopVlanEntry=_RlIgmpSnoopVlanEntry_Object((1,3,6,1,4,1,9,6,1,101,55,2,7,1))
rlIgmpSnoopVlanEntry.setIndexNames((0,_F,_N))
if mibBuilder.loadTexts:rlIgmpSnoopVlanEntry.setStatus(_D)
_RlIgmpSnoopVlanTag_Type=Integer32
_RlIgmpSnoopVlanTag_Object=MibTableColumn
rlIgmpSnoopVlanTag=_RlIgmpSnoopVlanTag_Object((1,3,6,1,4,1,9,6,1,101,55,2,7,1,1),_RlIgmpSnoopVlanTag_Type())
rlIgmpSnoopVlanTag.setMaxAccess(_B)
if mibBuilder.loadTexts:rlIgmpSnoopVlanTag.setStatus(_D)
_RlIgmpSnoopVlanEnable_Type=TruthValue
_RlIgmpSnoopVlanEnable_Object=MibTableColumn
rlIgmpSnoopVlanEnable=_RlIgmpSnoopVlanEnable_Object((1,3,6,1,4,1,9,6,1,101,55,2,7,1,2),_RlIgmpSnoopVlanEnable_Type())
rlIgmpSnoopVlanEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:rlIgmpSnoopVlanEnable.setStatus(_D)
_RlIgmpSnoopVlanRouterLearn_Type=TruthValue
_RlIgmpSnoopVlanRouterLearn_Object=MibTableColumn
rlIgmpSnoopVlanRouterLearn=_RlIgmpSnoopVlanRouterLearn_Object((1,3,6,1,4,1,9,6,1,101,55,2,7,1,3),_RlIgmpSnoopVlanRouterLearn_Type())
rlIgmpSnoopVlanRouterLearn.setMaxAccess(_C)
if mibBuilder.loadTexts:rlIgmpSnoopVlanRouterLearn.setStatus(_D)
class _RlIgmpSnoopVlanHostTimeOut_Type(Integer32):defaultValue=260;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_RlIgmpSnoopVlanHostTimeOut_Type.__name__=_G
_RlIgmpSnoopVlanHostTimeOut_Object=MibTableColumn
rlIgmpSnoopVlanHostTimeOut=_RlIgmpSnoopVlanHostTimeOut_Object((1,3,6,1,4,1,9,6,1,101,55,2,7,1,4),_RlIgmpSnoopVlanHostTimeOut_Type())
rlIgmpSnoopVlanHostTimeOut.setMaxAccess(_C)
if mibBuilder.loadTexts:rlIgmpSnoopVlanHostTimeOut.setStatus(_D)
if mibBuilder.loadTexts:rlIgmpSnoopVlanHostTimeOut.setUnits(_I)
class _RlIgmpSnoopVlanQuerierTimeOut_Type(Integer32):defaultValue=260;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_RlIgmpSnoopVlanQuerierTimeOut_Type.__name__=_G
_RlIgmpSnoopVlanQuerierTimeOut_Object=MibTableColumn
rlIgmpSnoopVlanQuerierTimeOut=_RlIgmpSnoopVlanQuerierTimeOut_Object((1,3,6,1,4,1,9,6,1,101,55,2,7,1,5),_RlIgmpSnoopVlanQuerierTimeOut_Type())
rlIgmpSnoopVlanQuerierTimeOut.setMaxAccess(_C)
if mibBuilder.loadTexts:rlIgmpSnoopVlanQuerierTimeOut.setStatus(_D)
if mibBuilder.loadTexts:rlIgmpSnoopVlanQuerierTimeOut.setUnits(_I)
class _RlIgmpSnoopVlanRouterTimeOut_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_RlIgmpSnoopVlanRouterTimeOut_Type.__name__=_G
_RlIgmpSnoopVlanRouterTimeOut_Object=MibTableColumn
rlIgmpSnoopVlanRouterTimeOut=_RlIgmpSnoopVlanRouterTimeOut_Object((1,3,6,1,4,1,9,6,1,101,55,2,7,1,6),_RlIgmpSnoopVlanRouterTimeOut_Type())
rlIgmpSnoopVlanRouterTimeOut.setMaxAccess(_C)
if mibBuilder.loadTexts:rlIgmpSnoopVlanRouterTimeOut.setStatus(_D)
if mibBuilder.loadTexts:rlIgmpSnoopVlanRouterTimeOut.setUnits(_I)
class _RlIgmpSnoopVlanLeaveTimeOut_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_RlIgmpSnoopVlanLeaveTimeOut_Type.__name__=_G
_RlIgmpSnoopVlanLeaveTimeOut_Object=MibTableColumn
rlIgmpSnoopVlanLeaveTimeOut=_RlIgmpSnoopVlanLeaveTimeOut_Object((1,3,6,1,4,1,9,6,1,101,55,2,7,1,7),_RlIgmpSnoopVlanLeaveTimeOut_Type())
rlIgmpSnoopVlanLeaveTimeOut.setMaxAccess(_C)
if mibBuilder.loadTexts:rlIgmpSnoopVlanLeaveTimeOut.setStatus(_D)
if mibBuilder.loadTexts:rlIgmpSnoopVlanLeaveTimeOut.setUnits(_I)
_RlIgmpSnoopVlanIgmpVersion_Type=IgmpVersion
_RlIgmpSnoopVlanIgmpVersion_Object=MibTableColumn
rlIgmpSnoopVlanIgmpVersion=_RlIgmpSnoopVlanIgmpVersion_Object((1,3,6,1,4,1,9,6,1,101,55,2,7,1,8),_RlIgmpSnoopVlanIgmpVersion_Type())
rlIgmpSnoopVlanIgmpVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:rlIgmpSnoopVlanIgmpVersion.setStatus(_D)
_RlIgmpSnoopVlanRouterPortlist_Type=PortList
_RlIgmpSnoopVlanRouterPortlist_Object=MibTableColumn
rlIgmpSnoopVlanRouterPortlist=_RlIgmpSnoopVlanRouterPortlist_Object((1,3,6,1,4,1,9,6,1,101,55,2,7,1,9),_RlIgmpSnoopVlanRouterPortlist_Type())
rlIgmpSnoopVlanRouterPortlist.setMaxAccess(_B)
if mibBuilder.loadTexts:rlIgmpSnoopVlanRouterPortlist.setStatus(_D)
class _RlIgmpSnoopIGMP224ReportsHandle_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('allow',1),('ignore',2)))
_RlIgmpSnoopIGMP224ReportsHandle_Type.__name__=_G
_RlIgmpSnoopIGMP224ReportsHandle_Object=MibScalar
rlIgmpSnoopIGMP224ReportsHandle=_RlIgmpSnoopIGMP224ReportsHandle_Object((1,3,6,1,4,1,9,6,1,101,55,2,8),_RlIgmpSnoopIGMP224ReportsHandle_Type())
rlIgmpSnoopIGMP224ReportsHandle.setMaxAccess(_C)
if mibBuilder.loadTexts:rlIgmpSnoopIGMP224ReportsHandle.setStatus(_A)
_RlIgmpSnoopMulticastTvTable_Object=MibTable
rlIgmpSnoopMulticastTvTable=_RlIgmpSnoopMulticastTvTable_Object((1,3,6,1,4,1,9,6,1,101,55,2,10))
if mibBuilder.loadTexts:rlIgmpSnoopMulticastTvTable.setStatus(_A)
_RlIgmpSnoopMulticastTvEntry_Object=MibTableRow
rlIgmpSnoopMulticastTvEntry=_RlIgmpSnoopMulticastTvEntry_Object((1,3,6,1,4,1,9,6,1,101,55,2,10,1))
rlIgmpSnoopMulticastTvEntry.setIndexNames((0,_F,_O),(0,_F,_P))
if mibBuilder.loadTexts:rlIgmpSnoopMulticastTvEntry.setStatus(_A)
_RlIgmpSnoopMulticastTvVID_Type=VlanIndex
_RlIgmpSnoopMulticastTvVID_Object=MibTableColumn
rlIgmpSnoopMulticastTvVID=_RlIgmpSnoopMulticastTvVID_Object((1,3,6,1,4,1,9,6,1,101,55,2,10,1,1),_RlIgmpSnoopMulticastTvVID_Type())
rlIgmpSnoopMulticastTvVID.setMaxAccess(_B)
if mibBuilder.loadTexts:rlIgmpSnoopMulticastTvVID.setStatus(_A)
_RlIgmpSnoopMulticastTvGroup_Type=IpAddress
_RlIgmpSnoopMulticastTvGroup_Object=MibTableColumn
rlIgmpSnoopMulticastTvGroup=_RlIgmpSnoopMulticastTvGroup_Object((1,3,6,1,4,1,9,6,1,101,55,2,10,1,2),_RlIgmpSnoopMulticastTvGroup_Type())
rlIgmpSnoopMulticastTvGroup.setMaxAccess(_B)
if mibBuilder.loadTexts:rlIgmpSnoopMulticastTvGroup.setStatus(_A)
_RlIgmpSnoopMulticastTvStatus_Type=RowStatus
_RlIgmpSnoopMulticastTvStatus_Object=MibTableColumn
rlIgmpSnoopMulticastTvStatus=_RlIgmpSnoopMulticastTvStatus_Object((1,3,6,1,4,1,9,6,1,101,55,2,10,1,3),_RlIgmpSnoopMulticastTvStatus_Type())
rlIgmpSnoopMulticastTvStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:rlIgmpSnoopMulticastTvStatus.setStatus(_A)
class _RlIgmpSnoopMulticastTvCount_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,268435456))
_RlIgmpSnoopMulticastTvCount_Type.__name__=_G
_RlIgmpSnoopMulticastTvCount_Object=MibTableColumn
rlIgmpSnoopMulticastTvCount=_RlIgmpSnoopMulticastTvCount_Object((1,3,6,1,4,1,9,6,1,101,55,2,10,1,4),_RlIgmpSnoopMulticastTvCount_Type())
rlIgmpSnoopMulticastTvCount.setMaxAccess(_C)
if mibBuilder.loadTexts:rlIgmpSnoopMulticastTvCount.setStatus(_A)
_RlIgmpSnoopMembershipTable_Object=MibTable
rlIgmpSnoopMembershipTable=_RlIgmpSnoopMembershipTable_Object((1,3,6,1,4,1,9,6,1,101,55,2,11))
if mibBuilder.loadTexts:rlIgmpSnoopMembershipTable.setStatus(_A)
_RlIgmpSnoopMembershipEntry_Object=MibTableRow
rlIgmpSnoopMembershipEntry=_RlIgmpSnoopMembershipEntry_Object((1,3,6,1,4,1,9,6,1,101,55,2,11,1))
rlIgmpSnoopMembershipEntry.setIndexNames((0,_F,_Q),(0,_F,_R),(0,_F,_S))
if mibBuilder.loadTexts:rlIgmpSnoopMembershipEntry.setStatus(_A)
_RlIgmpSnoopMembershipVlanTag_Type=VlanIndex
_RlIgmpSnoopMembershipVlanTag_Object=MibTableColumn
rlIgmpSnoopMembershipVlanTag=_RlIgmpSnoopMembershipVlanTag_Object((1,3,6,1,4,1,9,6,1,101,55,2,11,1,1),_RlIgmpSnoopMembershipVlanTag_Type())
rlIgmpSnoopMembershipVlanTag.setMaxAccess(_B)
if mibBuilder.loadTexts:rlIgmpSnoopMembershipVlanTag.setStatus(_A)
_RlIgmpSnoopMembershipGroupIpAddress_Type=IpAddress
_RlIgmpSnoopMembershipGroupIpAddress_Object=MibTableColumn
rlIgmpSnoopMembershipGroupIpAddress=_RlIgmpSnoopMembershipGroupIpAddress_Object((1,3,6,1,4,1,9,6,1,101,55,2,11,1,2),_RlIgmpSnoopMembershipGroupIpAddress_Type())
rlIgmpSnoopMembershipGroupIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:rlIgmpSnoopMembershipGroupIpAddress.setStatus(_A)
_RlIgmpSnoopMembershipSourceIpAddress_Type=IpAddress
_RlIgmpSnoopMembershipSourceIpAddress_Object=MibTableColumn
rlIgmpSnoopMembershipSourceIpAddress=_RlIgmpSnoopMembershipSourceIpAddress_Object((1,3,6,1,4,1,9,6,1,101,55,2,11,1,3),_RlIgmpSnoopMembershipSourceIpAddress_Type())
rlIgmpSnoopMembershipSourceIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:rlIgmpSnoopMembershipSourceIpAddress.setStatus(_A)
_RlIgmpSnoopMembershipIncPortlist_Type=PortList
_RlIgmpSnoopMembershipIncPortlist_Object=MibTableColumn
rlIgmpSnoopMembershipIncPortlist=_RlIgmpSnoopMembershipIncPortlist_Object((1,3,6,1,4,1,9,6,1,101,55,2,11,1,4),_RlIgmpSnoopMembershipIncPortlist_Type())
rlIgmpSnoopMembershipIncPortlist.setMaxAccess(_B)
if mibBuilder.loadTexts:rlIgmpSnoopMembershipIncPortlist.setStatus(_A)
_RlIgmpSnoopMembershipExcPortlist_Type=PortList
_RlIgmpSnoopMembershipExcPortlist_Object=MibTableColumn
rlIgmpSnoopMembershipExcPortlist=_RlIgmpSnoopMembershipExcPortlist_Object((1,3,6,1,4,1,9,6,1,101,55,2,11,1,5),_RlIgmpSnoopMembershipExcPortlist_Type())
rlIgmpSnoopMembershipExcPortlist.setMaxAccess(_B)
if mibBuilder.loadTexts:rlIgmpSnoopMembershipExcPortlist.setStatus(_A)
_RlIgmpSnoopMembershipExpiryTime_Type=Integer32
_RlIgmpSnoopMembershipExpiryTime_Object=MibTableColumn
rlIgmpSnoopMembershipExpiryTime=_RlIgmpSnoopMembershipExpiryTime_Object((1,3,6,1,4,1,9,6,1,101,55,2,11,1,6),_RlIgmpSnoopMembershipExpiryTime_Type())
rlIgmpSnoopMembershipExpiryTime.setMaxAccess(_B)
if mibBuilder.loadTexts:rlIgmpSnoopMembershipExpiryTime.setStatus(_D)
_RlIgmpSnoopMembershipCompatibilityMode_Type=IgmpVersion
_RlIgmpSnoopMembershipCompatibilityMode_Object=MibTableColumn
rlIgmpSnoopMembershipCompatibilityMode=_RlIgmpSnoopMembershipCompatibilityMode_Object((1,3,6,1,4,1,9,6,1,101,55,2,11,1,7),_RlIgmpSnoopMembershipCompatibilityMode_Type())
rlIgmpSnoopMembershipCompatibilityMode.setMaxAccess(_B)
if mibBuilder.loadTexts:rlIgmpSnoopMembershipCompatibilityMode.setStatus(_A)
_RlIgmpSnoopQuerierVlanTable_Object=MibTable
rlIgmpSnoopQuerierVlanTable=_RlIgmpSnoopQuerierVlanTable_Object((1,3,6,1,4,1,9,6,1,101,55,2,12))
if mibBuilder.loadTexts:rlIgmpSnoopQuerierVlanTable.setStatus(_A)
_RlIgmpSnoopQuerierVlanEntry_Object=MibTableRow
rlIgmpSnoopQuerierVlanEntry=_RlIgmpSnoopQuerierVlanEntry_Object((1,3,6,1,4,1,9,6,1,101,55,2,12,1))
rlIgmpSnoopQuerierVlanEntry.setIndexNames((0,_F,_T))
if mibBuilder.loadTexts:rlIgmpSnoopQuerierVlanEntry.setStatus(_A)
_RlIgmpSnoopQuerierVlanTag_Type=VlanIndex
_RlIgmpSnoopQuerierVlanTag_Object=MibTableColumn
rlIgmpSnoopQuerierVlanTag=_RlIgmpSnoopQuerierVlanTag_Object((1,3,6,1,4,1,9,6,1,101,55,2,12,1,1),_RlIgmpSnoopQuerierVlanTag_Type())
rlIgmpSnoopQuerierVlanTag.setMaxAccess(_B)
if mibBuilder.loadTexts:rlIgmpSnoopQuerierVlanTag.setStatus(_A)
_RlIgmpSnoopQuerierAdminEnable_Type=TruthValue
_RlIgmpSnoopQuerierAdminEnable_Object=MibTableColumn
rlIgmpSnoopQuerierAdminEnable=_RlIgmpSnoopQuerierAdminEnable_Object((1,3,6,1,4,1,9,6,1,101,55,2,12,1,2),_RlIgmpSnoopQuerierAdminEnable_Type())
rlIgmpSnoopQuerierAdminEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:rlIgmpSnoopQuerierAdminEnable.setStatus(_A)
_RlIgmpSnoopQuerierOperEnable_Type=TruthValue
_RlIgmpSnoopQuerierOperEnable_Object=MibTableColumn
rlIgmpSnoopQuerierOperEnable=_RlIgmpSnoopQuerierOperEnable_Object((1,3,6,1,4,1,9,6,1,101,55,2,12,1,3),_RlIgmpSnoopQuerierOperEnable_Type())
rlIgmpSnoopQuerierOperEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:rlIgmpSnoopQuerierOperEnable.setStatus(_A)
_RlIgmpSnoopQuerierAdminAddr_Type=IpAddress
_RlIgmpSnoopQuerierAdminAddr_Object=MibTableColumn
rlIgmpSnoopQuerierAdminAddr=_RlIgmpSnoopQuerierAdminAddr_Object((1,3,6,1,4,1,9,6,1,101,55,2,12,1,4),_RlIgmpSnoopQuerierAdminAddr_Type())
rlIgmpSnoopQuerierAdminAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:rlIgmpSnoopQuerierAdminAddr.setStatus(_A)
_RlIgmpSnoopQuerierOperAddr_Type=IpAddress
_RlIgmpSnoopQuerierOperAddr_Object=MibTableColumn
rlIgmpSnoopQuerierOperAddr=_RlIgmpSnoopQuerierOperAddr_Object((1,3,6,1,4,1,9,6,1,101,55,2,12,1,5),_RlIgmpSnoopQuerierOperAddr_Type())
rlIgmpSnoopQuerierOperAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:rlIgmpSnoopQuerierOperAddr.setStatus(_A)
_RlIgmpSnoopQuerierAdminVersionNumber_Type=IgmpVersion
_RlIgmpSnoopQuerierAdminVersionNumber_Object=MibTableColumn
rlIgmpSnoopQuerierAdminVersionNumber=_RlIgmpSnoopQuerierAdminVersionNumber_Object((1,3,6,1,4,1,9,6,1,101,55,2,12,1,6),_RlIgmpSnoopQuerierAdminVersionNumber_Type())
rlIgmpSnoopQuerierAdminVersionNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:rlIgmpSnoopQuerierAdminVersionNumber.setStatus(_A)
_RlIgmpSnoopQuerierOperVersionNumber_Type=IgmpVersion
_RlIgmpSnoopQuerierOperVersionNumber_Object=MibTableColumn
rlIgmpSnoopQuerierOperVersionNumber=_RlIgmpSnoopQuerierOperVersionNumber_Object((1,3,6,1,4,1,9,6,1,101,55,2,12,1,7),_RlIgmpSnoopQuerierOperVersionNumber_Type())
rlIgmpSnoopQuerierOperVersionNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:rlIgmpSnoopQuerierOperVersionNumber.setStatus(_A)
_RlIgmpSnoopQuerierElectionEnable_Type=TruthValue
_RlIgmpSnoopQuerierElectionEnable_Object=MibTableColumn
rlIgmpSnoopQuerierElectionEnable=_RlIgmpSnoopQuerierElectionEnable_Object((1,3,6,1,4,1,9,6,1,101,55,2,12,1,8),_RlIgmpSnoopQuerierElectionEnable_Type())
rlIgmpSnoopQuerierElectionEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:rlIgmpSnoopQuerierElectionEnable.setStatus(_A)
_RlIgmpSnoopQuerierEnable_Type=TruthValue
_RlIgmpSnoopQuerierEnable_Object=MibScalar
rlIgmpSnoopQuerierEnable=_RlIgmpSnoopQuerierEnable_Object((1,3,6,1,4,1,9,6,1,101,55,2,13),_RlIgmpSnoopQuerierEnable_Type())
rlIgmpSnoopQuerierEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:rlIgmpSnoopQuerierEnable.setStatus(_A)
_RlMacMulticastMaxEntriesNum_Type=Integer32
_RlMacMulticastMaxEntriesNum_Object=MibScalar
rlMacMulticastMaxEntriesNum=_RlMacMulticastMaxEntriesNum_Object((1,3,6,1,4,1,9,6,1,101,55,3),_RlMacMulticastMaxEntriesNum_Type())
rlMacMulticastMaxEntriesNum.setMaxAccess(_B)
if mibBuilder.loadTexts:rlMacMulticastMaxEntriesNum.setStatus(_A)
_RlMacMulticastFilter_ObjectIdentity=ObjectIdentity
rlMacMulticastFilter=_RlMacMulticastFilter_ObjectIdentity((1,3,6,1,4,1,9,6,1,101,55,4))
_RlMacMulticastUnregFilterEnable_Type=PortList
_RlMacMulticastUnregFilterEnable_Object=MibScalar
rlMacMulticastUnregFilterEnable=_RlMacMulticastUnregFilterEnable_Object((1,3,6,1,4,1,9,6,1,101,55,4,1),_RlMacMulticastUnregFilterEnable_Type())
rlMacMulticastUnregFilterEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:rlMacMulticastUnregFilterEnable.setStatus(_A)
_RlMldSnoop_ObjectIdentity=ObjectIdentity
rlMldSnoop=_RlMldSnoop_ObjectIdentity((1,3,6,1,4,1,9,6,1,101,55,5))
_RlMldSnoopEnable_Type=TruthValue
_RlMldSnoopEnable_Object=MibScalar
rlMldSnoopEnable=_RlMldSnoopEnable_Object((1,3,6,1,4,1,9,6,1,101,55,5,1),_RlMldSnoopEnable_Type())
rlMldSnoopEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:rlMldSnoopEnable.setStatus(_A)
class _RlMldSnoopHostAgingTime_Type(Integer32):defaultValue=260;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,2147483647))
_RlMldSnoopHostAgingTime_Type.__name__=_G
_RlMldSnoopHostAgingTime_Object=MibScalar
rlMldSnoopHostAgingTime=_RlMldSnoopHostAgingTime_Object((1,3,6,1,4,1,9,6,1,101,55,5,2),_RlMldSnoopHostAgingTime_Type())
rlMldSnoopHostAgingTime.setMaxAccess(_C)
if mibBuilder.loadTexts:rlMldSnoopHostAgingTime.setStatus(_D)
if mibBuilder.loadTexts:rlMldSnoopHostAgingTime.setUnits(_I)
class _RlMldSnoopRouterAgingTime_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_RlMldSnoopRouterAgingTime_Type.__name__=_G
_RlMldSnoopRouterAgingTime_Object=MibScalar
rlMldSnoopRouterAgingTime=_RlMldSnoopRouterAgingTime_Object((1,3,6,1,4,1,9,6,1,101,55,5,3),_RlMldSnoopRouterAgingTime_Type())
rlMldSnoopRouterAgingTime.setMaxAccess(_C)
if mibBuilder.loadTexts:rlMldSnoopRouterAgingTime.setStatus(_D)
if mibBuilder.loadTexts:rlMldSnoopRouterAgingTime.setUnits(_I)
_RlIgmpMldSnoopMembershipTable_Object=MibTable
rlIgmpMldSnoopMembershipTable=_RlIgmpMldSnoopMembershipTable_Object((1,3,6,1,4,1,9,6,1,101,55,5,4))
if mibBuilder.loadTexts:rlIgmpMldSnoopMembershipTable.setStatus(_A)
_RlIgmpMldSnoopMembershipEntry_Object=MibTableRow
rlIgmpMldSnoopMembershipEntry=_RlIgmpMldSnoopMembershipEntry_Object((1,3,6,1,4,1,9,6,1,101,55,5,4,1))
rlIgmpMldSnoopMembershipEntry.setIndexNames((0,_F,_U),(0,_F,_V),(0,_F,_W),(0,_F,_X),(0,_F,_Y))
if mibBuilder.loadTexts:rlIgmpMldSnoopMembershipEntry.setStatus(_A)
_RlIgmpMldSnoopMembershipVlanTag_Type=VlanIndex
_RlIgmpMldSnoopMembershipVlanTag_Object=MibTableColumn
rlIgmpMldSnoopMembershipVlanTag=_RlIgmpMldSnoopMembershipVlanTag_Object((1,3,6,1,4,1,9,6,1,101,55,5,4,1,1),_RlIgmpMldSnoopMembershipVlanTag_Type())
rlIgmpMldSnoopMembershipVlanTag.setMaxAccess(_B)
if mibBuilder.loadTexts:rlIgmpMldSnoopMembershipVlanTag.setStatus(_A)
_RlIgmpMldSnoopMembershipGroupIpAddressType_Type=InetAddressType
_RlIgmpMldSnoopMembershipGroupIpAddressType_Object=MibTableColumn
rlIgmpMldSnoopMembershipGroupIpAddressType=_RlIgmpMldSnoopMembershipGroupIpAddressType_Object((1,3,6,1,4,1,9,6,1,101,55,5,4,1,2),_RlIgmpMldSnoopMembershipGroupIpAddressType_Type())
rlIgmpMldSnoopMembershipGroupIpAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:rlIgmpMldSnoopMembershipGroupIpAddressType.setStatus(_A)
_RlIgmpMldSnoopMembershipGroupIpAddress_Type=InetAddress
_RlIgmpMldSnoopMembershipGroupIpAddress_Object=MibTableColumn
rlIgmpMldSnoopMembershipGroupIpAddress=_RlIgmpMldSnoopMembershipGroupIpAddress_Object((1,3,6,1,4,1,9,6,1,101,55,5,4,1,3),_RlIgmpMldSnoopMembershipGroupIpAddress_Type())
rlIgmpMldSnoopMembershipGroupIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:rlIgmpMldSnoopMembershipGroupIpAddress.setStatus(_A)
_RlIgmpMldSnoopMembershipSourceIpAddressType_Type=InetAddressType
_RlIgmpMldSnoopMembershipSourceIpAddressType_Object=MibTableColumn
rlIgmpMldSnoopMembershipSourceIpAddressType=_RlIgmpMldSnoopMembershipSourceIpAddressType_Object((1,3,6,1,4,1,9,6,1,101,55,5,4,1,4),_RlIgmpMldSnoopMembershipSourceIpAddressType_Type())
rlIgmpMldSnoopMembershipSourceIpAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:rlIgmpMldSnoopMembershipSourceIpAddressType.setStatus(_A)
_RlIgmpMldSnoopMembershipSourceIpAddress_Type=InetAddress
_RlIgmpMldSnoopMembershipSourceIpAddress_Object=MibTableColumn
rlIgmpMldSnoopMembershipSourceIpAddress=_RlIgmpMldSnoopMembershipSourceIpAddress_Object((1,3,6,1,4,1,9,6,1,101,55,5,4,1,5),_RlIgmpMldSnoopMembershipSourceIpAddress_Type())
rlIgmpMldSnoopMembershipSourceIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:rlIgmpMldSnoopMembershipSourceIpAddress.setStatus(_A)
_RlIgmpMldSnoopMembershipIncPortlist_Type=PortList
_RlIgmpMldSnoopMembershipIncPortlist_Object=MibTableColumn
rlIgmpMldSnoopMembershipIncPortlist=_RlIgmpMldSnoopMembershipIncPortlist_Object((1,3,6,1,4,1,9,6,1,101,55,5,4,1,6),_RlIgmpMldSnoopMembershipIncPortlist_Type())
rlIgmpMldSnoopMembershipIncPortlist.setMaxAccess(_B)
if mibBuilder.loadTexts:rlIgmpMldSnoopMembershipIncPortlist.setStatus(_A)
_RlIgmpMldSnoopMembershipExcPortlist_Type=PortList
_RlIgmpMldSnoopMembershipExcPortlist_Object=MibTableColumn
rlIgmpMldSnoopMembershipExcPortlist=_RlIgmpMldSnoopMembershipExcPortlist_Object((1,3,6,1,4,1,9,6,1,101,55,5,4,1,7),_RlIgmpMldSnoopMembershipExcPortlist_Type())
rlIgmpMldSnoopMembershipExcPortlist.setMaxAccess(_B)
if mibBuilder.loadTexts:rlIgmpMldSnoopMembershipExcPortlist.setStatus(_A)
_RlIgmpMldSnoopMembershipExpiryTime_Type=Integer32
_RlIgmpMldSnoopMembershipExpiryTime_Object=MibTableColumn
rlIgmpMldSnoopMembershipExpiryTime=_RlIgmpMldSnoopMembershipExpiryTime_Object((1,3,6,1,4,1,9,6,1,101,55,5,4,1,8),_RlIgmpMldSnoopMembershipExpiryTime_Type())
rlIgmpMldSnoopMembershipExpiryTime.setMaxAccess(_B)
if mibBuilder.loadTexts:rlIgmpMldSnoopMembershipExpiryTime.setStatus(_D)
_RlIgmpMldSnoopMembershipCompatibilityMode_Type=IgmpVersion
_RlIgmpMldSnoopMembershipCompatibilityMode_Object=MibTableColumn
rlIgmpMldSnoopMembershipCompatibilityMode=_RlIgmpMldSnoopMembershipCompatibilityMode_Object((1,3,6,1,4,1,9,6,1,101,55,5,4,1,9),_RlIgmpMldSnoopMembershipCompatibilityMode_Type())
rlIgmpMldSnoopMembershipCompatibilityMode.setMaxAccess(_B)
if mibBuilder.loadTexts:rlIgmpMldSnoopMembershipCompatibilityMode.setStatus(_A)
_RlIgmpMldSnoopVlanTable_Object=MibTable
rlIgmpMldSnoopVlanTable=_RlIgmpMldSnoopVlanTable_Object((1,3,6,1,4,1,9,6,1,101,55,5,5))
if mibBuilder.loadTexts:rlIgmpMldSnoopVlanTable.setStatus(_A)
_RlIgmpMldSnoopVlanEntry_Object=MibTableRow
rlIgmpMldSnoopVlanEntry=_RlIgmpMldSnoopVlanEntry_Object((1,3,6,1,4,1,9,6,1,101,55,5,5,1))
rlIgmpMldSnoopVlanEntry.setIndexNames((0,_F,_Z),(0,_F,_a))
if mibBuilder.loadTexts:rlIgmpMldSnoopVlanEntry.setStatus(_A)
_RlIgmpMldSnoopVlanInetAddressType_Type=InetAddressType
_RlIgmpMldSnoopVlanInetAddressType_Object=MibTableColumn
rlIgmpMldSnoopVlanInetAddressType=_RlIgmpMldSnoopVlanInetAddressType_Object((1,3,6,1,4,1,9,6,1,101,55,5,5,1,1),_RlIgmpMldSnoopVlanInetAddressType_Type())
rlIgmpMldSnoopVlanInetAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:rlIgmpMldSnoopVlanInetAddressType.setStatus(_A)
_RlIgmpMldSnoopVlanTag_Type=Integer32
_RlIgmpMldSnoopVlanTag_Object=MibTableColumn
rlIgmpMldSnoopVlanTag=_RlIgmpMldSnoopVlanTag_Object((1,3,6,1,4,1,9,6,1,101,55,5,5,1,2),_RlIgmpMldSnoopVlanTag_Type())
rlIgmpMldSnoopVlanTag.setMaxAccess(_B)
if mibBuilder.loadTexts:rlIgmpMldSnoopVlanTag.setStatus(_A)
_RlIgmpMldSnoopVlanEnable_Type=TruthValue
_RlIgmpMldSnoopVlanEnable_Object=MibTableColumn
rlIgmpMldSnoopVlanEnable=_RlIgmpMldSnoopVlanEnable_Object((1,3,6,1,4,1,9,6,1,101,55,5,5,1,3),_RlIgmpMldSnoopVlanEnable_Type())
rlIgmpMldSnoopVlanEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:rlIgmpMldSnoopVlanEnable.setStatus(_A)
_RlIgmpMldSnoopVlanRouterLearn_Type=TruthValue
_RlIgmpMldSnoopVlanRouterLearn_Object=MibTableColumn
rlIgmpMldSnoopVlanRouterLearn=_RlIgmpMldSnoopVlanRouterLearn_Object((1,3,6,1,4,1,9,6,1,101,55,5,5,1,4),_RlIgmpMldSnoopVlanRouterLearn_Type())
rlIgmpMldSnoopVlanRouterLearn.setMaxAccess(_C)
if mibBuilder.loadTexts:rlIgmpMldSnoopVlanRouterLearn.setStatus(_A)
class _RlIgmpMldSnoopVlanHostTimeOut_Type(Integer32):defaultValue=260;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,2147483647))
_RlIgmpMldSnoopVlanHostTimeOut_Type.__name__=_G
_RlIgmpMldSnoopVlanHostTimeOut_Object=MibTableColumn
rlIgmpMldSnoopVlanHostTimeOut=_RlIgmpMldSnoopVlanHostTimeOut_Object((1,3,6,1,4,1,9,6,1,101,55,5,5,1,5),_RlIgmpMldSnoopVlanHostTimeOut_Type())
rlIgmpMldSnoopVlanHostTimeOut.setMaxAccess(_C)
if mibBuilder.loadTexts:rlIgmpMldSnoopVlanHostTimeOut.setStatus(_D)
if mibBuilder.loadTexts:rlIgmpMldSnoopVlanHostTimeOut.setUnits(_I)
class _RlIgmpMldSnoopVlanQuerierTimeOut_Type(Integer32):defaultValue=260;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_RlIgmpMldSnoopVlanQuerierTimeOut_Type.__name__=_G
_RlIgmpMldSnoopVlanQuerierTimeOut_Object=MibTableColumn
rlIgmpMldSnoopVlanQuerierTimeOut=_RlIgmpMldSnoopVlanQuerierTimeOut_Object((1,3,6,1,4,1,9,6,1,101,55,5,5,1,6),_RlIgmpMldSnoopVlanQuerierTimeOut_Type())
rlIgmpMldSnoopVlanQuerierTimeOut.setMaxAccess(_C)
if mibBuilder.loadTexts:rlIgmpMldSnoopVlanQuerierTimeOut.setStatus(_D)
if mibBuilder.loadTexts:rlIgmpMldSnoopVlanQuerierTimeOut.setUnits(_I)
class _RlIgmpMldSnoopVlanRouterTimeOut_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_RlIgmpMldSnoopVlanRouterTimeOut_Type.__name__=_G
_RlIgmpMldSnoopVlanRouterTimeOut_Object=MibTableColumn
rlIgmpMldSnoopVlanRouterTimeOut=_RlIgmpMldSnoopVlanRouterTimeOut_Object((1,3,6,1,4,1,9,6,1,101,55,5,5,1,7),_RlIgmpMldSnoopVlanRouterTimeOut_Type())
rlIgmpMldSnoopVlanRouterTimeOut.setMaxAccess(_C)
if mibBuilder.loadTexts:rlIgmpMldSnoopVlanRouterTimeOut.setStatus(_D)
if mibBuilder.loadTexts:rlIgmpMldSnoopVlanRouterTimeOut.setUnits(_I)
class _RlIgmpMldSnoopVlanLeaveTimeOut_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_RlIgmpMldSnoopVlanLeaveTimeOut_Type.__name__=_G
_RlIgmpMldSnoopVlanLeaveTimeOut_Object=MibTableColumn
rlIgmpMldSnoopVlanLeaveTimeOut=_RlIgmpMldSnoopVlanLeaveTimeOut_Object((1,3,6,1,4,1,9,6,1,101,55,5,5,1,8),_RlIgmpMldSnoopVlanLeaveTimeOut_Type())
rlIgmpMldSnoopVlanLeaveTimeOut.setMaxAccess(_C)
if mibBuilder.loadTexts:rlIgmpMldSnoopVlanLeaveTimeOut.setStatus(_D)
if mibBuilder.loadTexts:rlIgmpMldSnoopVlanLeaveTimeOut.setUnits(_I)
_RlIgmpMldSnoopVlanIgmpVersion_Type=IgmpVersion
_RlIgmpMldSnoopVlanIgmpVersion_Object=MibTableColumn
rlIgmpMldSnoopVlanIgmpVersion=_RlIgmpMldSnoopVlanIgmpVersion_Object((1,3,6,1,4,1,9,6,1,101,55,5,5,1,9),_RlIgmpMldSnoopVlanIgmpVersion_Type())
rlIgmpMldSnoopVlanIgmpVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:rlIgmpMldSnoopVlanIgmpVersion.setStatus(_A)
_RlIgmpMldSnoopVlanRouterPortlist_Type=PortList
_RlIgmpMldSnoopVlanRouterPortlist_Object=MibTableColumn
rlIgmpMldSnoopVlanRouterPortlist=_RlIgmpMldSnoopVlanRouterPortlist_Object((1,3,6,1,4,1,9,6,1,101,55,5,5,1,10),_RlIgmpMldSnoopVlanRouterPortlist_Type())
rlIgmpMldSnoopVlanRouterPortlist.setMaxAccess(_B)
if mibBuilder.loadTexts:rlIgmpMldSnoopVlanRouterPortlist.setStatus(_A)
_RlIgmpMldSnoopVlanRouterStaticPortlist_Type=PortList
_RlIgmpMldSnoopVlanRouterStaticPortlist_Object=MibTableColumn
rlIgmpMldSnoopVlanRouterStaticPortlist=_RlIgmpMldSnoopVlanRouterStaticPortlist_Object((1,3,6,1,4,1,9,6,1,101,55,5,5,1,11),_RlIgmpMldSnoopVlanRouterStaticPortlist_Type())
rlIgmpMldSnoopVlanRouterStaticPortlist.setMaxAccess(_C)
if mibBuilder.loadTexts:rlIgmpMldSnoopVlanRouterStaticPortlist.setStatus(_A)
_RlIgmpMldSnoopVlanRouterForbiddenPortlist_Type=PortList
_RlIgmpMldSnoopVlanRouterForbiddenPortlist_Object=MibTableColumn
rlIgmpMldSnoopVlanRouterForbiddenPortlist=_RlIgmpMldSnoopVlanRouterForbiddenPortlist_Object((1,3,6,1,4,1,9,6,1,101,55,5,5,1,12),_RlIgmpMldSnoopVlanRouterForbiddenPortlist_Type())
rlIgmpMldSnoopVlanRouterForbiddenPortlist.setMaxAccess(_C)
if mibBuilder.loadTexts:rlIgmpMldSnoopVlanRouterForbiddenPortlist.setStatus(_A)
_RlIgmpMldSnoopVlanQueryOverride_Type=TruthValue
_RlIgmpMldSnoopVlanQueryOverride_Object=MibTableColumn
rlIgmpMldSnoopVlanQueryOverride=_RlIgmpMldSnoopVlanQueryOverride_Object((1,3,6,1,4,1,9,6,1,101,55,5,5,1,13),_RlIgmpMldSnoopVlanQueryOverride_Type())
rlIgmpMldSnoopVlanQueryOverride.setMaxAccess(_C)
if mibBuilder.loadTexts:rlIgmpMldSnoopVlanQueryOverride.setStatus(_A)
class _RlIgmpMldSnoopVlanOperRobustness_Type(Unsigned32):defaultValue=2;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_RlIgmpMldSnoopVlanOperRobustness_Type.__name__=_E
_RlIgmpMldSnoopVlanOperRobustness_Object=MibTableColumn
rlIgmpMldSnoopVlanOperRobustness=_RlIgmpMldSnoopVlanOperRobustness_Object((1,3,6,1,4,1,9,6,1,101,55,5,5,1,14),_RlIgmpMldSnoopVlanOperRobustness_Type())
rlIgmpMldSnoopVlanOperRobustness.setMaxAccess(_B)
if mibBuilder.loadTexts:rlIgmpMldSnoopVlanOperRobustness.setStatus(_A)
class _RlIgmpMldSnoopVlanOperQueryInterval_Type(Unsigned32):defaultValue=125000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1000,31744000))
_RlIgmpMldSnoopVlanOperQueryInterval_Type.__name__=_E
_RlIgmpMldSnoopVlanOperQueryInterval_Object=MibTableColumn
rlIgmpMldSnoopVlanOperQueryInterval=_RlIgmpMldSnoopVlanOperQueryInterval_Object((1,3,6,1,4,1,9,6,1,101,55,5,5,1,15),_RlIgmpMldSnoopVlanOperQueryInterval_Type())
rlIgmpMldSnoopVlanOperQueryInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:rlIgmpMldSnoopVlanOperQueryInterval.setStatus(_A)
if mibBuilder.loadTexts:rlIgmpMldSnoopVlanOperQueryInterval.setUnits(_H)
class _RlIgmpMldSnoopVlanOperQueryMaxResponseTime_Type(Unsigned32):defaultValue=10000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8387584))
_RlIgmpMldSnoopVlanOperQueryMaxResponseTime_Type.__name__=_E
_RlIgmpMldSnoopVlanOperQueryMaxResponseTime_Object=MibTableColumn
rlIgmpMldSnoopVlanOperQueryMaxResponseTime=_RlIgmpMldSnoopVlanOperQueryMaxResponseTime_Object((1,3,6,1,4,1,9,6,1,101,55,5,5,1,16),_RlIgmpMldSnoopVlanOperQueryMaxResponseTime_Type())
rlIgmpMldSnoopVlanOperQueryMaxResponseTime.setMaxAccess(_B)
if mibBuilder.loadTexts:rlIgmpMldSnoopVlanOperQueryMaxResponseTime.setStatus(_A)
if mibBuilder.loadTexts:rlIgmpMldSnoopVlanOperQueryMaxResponseTime.setUnits(_H)
class _RlIgmpMldSnoopVlanOperLastMemberQueryInterval_Type(Unsigned32):defaultValue=1000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8387584))
_RlIgmpMldSnoopVlanOperLastMemberQueryInterval_Type.__name__=_E
_RlIgmpMldSnoopVlanOperLastMemberQueryInterval_Object=MibTableColumn
rlIgmpMldSnoopVlanOperLastMemberQueryInterval=_RlIgmpMldSnoopVlanOperLastMemberQueryInterval_Object((1,3,6,1,4,1,9,6,1,101,55,5,5,1,17),_RlIgmpMldSnoopVlanOperLastMemberQueryInterval_Type())
rlIgmpMldSnoopVlanOperLastMemberQueryInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:rlIgmpMldSnoopVlanOperLastMemberQueryInterval.setStatus(_A)
if mibBuilder.loadTexts:rlIgmpMldSnoopVlanOperLastMemberQueryInterval.setUnits(_H)
class _RlIgmpMldSnoopVlanOperLastMemberQueryCount_Type(Unsigned32):defaultValue=2;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_RlIgmpMldSnoopVlanOperLastMemberQueryCount_Type.__name__=_E
_RlIgmpMldSnoopVlanOperLastMemberQueryCount_Object=MibTableColumn
rlIgmpMldSnoopVlanOperLastMemberQueryCount=_RlIgmpMldSnoopVlanOperLastMemberQueryCount_Object((1,3,6,1,4,1,9,6,1,101,55,5,5,1,18),_RlIgmpMldSnoopVlanOperLastMemberQueryCount_Type())
rlIgmpMldSnoopVlanOperLastMemberQueryCount.setMaxAccess(_B)
if mibBuilder.loadTexts:rlIgmpMldSnoopVlanOperLastMemberQueryCount.setStatus(_A)
class _RlIgmpMldSnoopVlanOperStartupQueryInterval_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31744000))
_RlIgmpMldSnoopVlanOperStartupQueryInterval_Type.__name__=_E
_RlIgmpMldSnoopVlanOperStartupQueryInterval_Object=MibTableColumn
rlIgmpMldSnoopVlanOperStartupQueryInterval=_RlIgmpMldSnoopVlanOperStartupQueryInterval_Object((1,3,6,1,4,1,9,6,1,101,55,5,5,1,19),_RlIgmpMldSnoopVlanOperStartupQueryInterval_Type())
rlIgmpMldSnoopVlanOperStartupQueryInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:rlIgmpMldSnoopVlanOperStartupQueryInterval.setStatus(_A)
if mibBuilder.loadTexts:rlIgmpMldSnoopVlanOperStartupQueryInterval.setUnits(_H)
class _RlIgmpMldSnoopVlanOperStartupQueryCount_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_RlIgmpMldSnoopVlanOperStartupQueryCount_Type.__name__=_E
_RlIgmpMldSnoopVlanOperStartupQueryCount_Object=MibTableColumn
rlIgmpMldSnoopVlanOperStartupQueryCount=_RlIgmpMldSnoopVlanOperStartupQueryCount_Object((1,3,6,1,4,1,9,6,1,101,55,5,5,1,20),_RlIgmpMldSnoopVlanOperStartupQueryCount_Type())
rlIgmpMldSnoopVlanOperStartupQueryCount.setMaxAccess(_B)
if mibBuilder.loadTexts:rlIgmpMldSnoopVlanOperStartupQueryCount.setStatus(_A)
class _RlIgmpMldSnoopVlanOperHostTimeOut_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_RlIgmpMldSnoopVlanOperHostTimeOut_Type.__name__=_E
_RlIgmpMldSnoopVlanOperHostTimeOut_Object=MibTableColumn
rlIgmpMldSnoopVlanOperHostTimeOut=_RlIgmpMldSnoopVlanOperHostTimeOut_Object((1,3,6,1,4,1,9,6,1,101,55,5,5,1,21),_RlIgmpMldSnoopVlanOperHostTimeOut_Type())
rlIgmpMldSnoopVlanOperHostTimeOut.setMaxAccess(_B)
if mibBuilder.loadTexts:rlIgmpMldSnoopVlanOperHostTimeOut.setStatus(_A)
if mibBuilder.loadTexts:rlIgmpMldSnoopVlanOperHostTimeOut.setUnits(_H)
class _RlIgmpMldSnoopVlanOperRouterTimeOut_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_RlIgmpMldSnoopVlanOperRouterTimeOut_Type.__name__=_E
_RlIgmpMldSnoopVlanOperRouterTimeOut_Object=MibTableColumn
rlIgmpMldSnoopVlanOperRouterTimeOut=_RlIgmpMldSnoopVlanOperRouterTimeOut_Object((1,3,6,1,4,1,9,6,1,101,55,5,5,1,22),_RlIgmpMldSnoopVlanOperRouterTimeOut_Type())
rlIgmpMldSnoopVlanOperRouterTimeOut.setMaxAccess(_B)
if mibBuilder.loadTexts:rlIgmpMldSnoopVlanOperRouterTimeOut.setStatus(_A)
if mibBuilder.loadTexts:rlIgmpMldSnoopVlanOperRouterTimeOut.setUnits(_H)
class _RlIgmpMldSnoopVlanOperLeaveTimeOut_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_RlIgmpMldSnoopVlanOperLeaveTimeOut_Type.__name__=_E
_RlIgmpMldSnoopVlanOperLeaveTimeOut_Object=MibTableColumn
rlIgmpMldSnoopVlanOperLeaveTimeOut=_RlIgmpMldSnoopVlanOperLeaveTimeOut_Object((1,3,6,1,4,1,9,6,1,101,55,5,5,1,23),_RlIgmpMldSnoopVlanOperLeaveTimeOut_Type())
rlIgmpMldSnoopVlanOperLeaveTimeOut.setMaxAccess(_B)
if mibBuilder.loadTexts:rlIgmpMldSnoopVlanOperLeaveTimeOut.setStatus(_A)
if mibBuilder.loadTexts:rlIgmpMldSnoopVlanOperLeaveTimeOut.setUnits(_H)
class _RlIgmpMldSnoopVlanAdminRobustness_Type(Unsigned32):defaultValue=2;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,7))
_RlIgmpMldSnoopVlanAdminRobustness_Type.__name__=_E
_RlIgmpMldSnoopVlanAdminRobustness_Object=MibTableColumn
rlIgmpMldSnoopVlanAdminRobustness=_RlIgmpMldSnoopVlanAdminRobustness_Object((1,3,6,1,4,1,9,6,1,101,55,5,5,1,24),_RlIgmpMldSnoopVlanAdminRobustness_Type())
rlIgmpMldSnoopVlanAdminRobustness.setMaxAccess(_C)
if mibBuilder.loadTexts:rlIgmpMldSnoopVlanAdminRobustness.setStatus(_A)
class _RlIgmpMldSnoopVlanAdminQueryInterval_Type(Unsigned32):defaultValue=125000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1000,18000000))
_RlIgmpMldSnoopVlanAdminQueryInterval_Type.__name__=_E
_RlIgmpMldSnoopVlanAdminQueryInterval_Object=MibTableColumn
rlIgmpMldSnoopVlanAdminQueryInterval=_RlIgmpMldSnoopVlanAdminQueryInterval_Object((1,3,6,1,4,1,9,6,1,101,55,5,5,1,25),_RlIgmpMldSnoopVlanAdminQueryInterval_Type())
rlIgmpMldSnoopVlanAdminQueryInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:rlIgmpMldSnoopVlanAdminQueryInterval.setStatus(_A)
if mibBuilder.loadTexts:rlIgmpMldSnoopVlanAdminQueryInterval.setUnits(_H)
class _RlIgmpMldSnoopVlanAdminQueryMaxResponseTime_Type(Unsigned32):defaultValue=10000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1000,20000))
_RlIgmpMldSnoopVlanAdminQueryMaxResponseTime_Type.__name__=_E
_RlIgmpMldSnoopVlanAdminQueryMaxResponseTime_Object=MibTableColumn
rlIgmpMldSnoopVlanAdminQueryMaxResponseTime=_RlIgmpMldSnoopVlanAdminQueryMaxResponseTime_Object((1,3,6,1,4,1,9,6,1,101,55,5,5,1,26),_RlIgmpMldSnoopVlanAdminQueryMaxResponseTime_Type())
rlIgmpMldSnoopVlanAdminQueryMaxResponseTime.setMaxAccess(_C)
if mibBuilder.loadTexts:rlIgmpMldSnoopVlanAdminQueryMaxResponseTime.setStatus(_A)
if mibBuilder.loadTexts:rlIgmpMldSnoopVlanAdminQueryMaxResponseTime.setUnits(_H)
class _RlIgmpMldSnoopVlanAdminLastMemberQueryInterval_Type(Unsigned32):defaultValue=1000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,25500))
_RlIgmpMldSnoopVlanAdminLastMemberQueryInterval_Type.__name__=_E
_RlIgmpMldSnoopVlanAdminLastMemberQueryInterval_Object=MibTableColumn
rlIgmpMldSnoopVlanAdminLastMemberQueryInterval=_RlIgmpMldSnoopVlanAdminLastMemberQueryInterval_Object((1,3,6,1,4,1,9,6,1,101,55,5,5,1,27),_RlIgmpMldSnoopVlanAdminLastMemberQueryInterval_Type())
rlIgmpMldSnoopVlanAdminLastMemberQueryInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:rlIgmpMldSnoopVlanAdminLastMemberQueryInterval.setStatus(_A)
if mibBuilder.loadTexts:rlIgmpMldSnoopVlanAdminLastMemberQueryInterval.setUnits(_H)
class _RlIgmpMldSnoopVlanAdminLastMemberQueryCount_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_RlIgmpMldSnoopVlanAdminLastMemberQueryCount_Type.__name__=_E
_RlIgmpMldSnoopVlanAdminLastMemberQueryCount_Object=MibTableColumn
rlIgmpMldSnoopVlanAdminLastMemberQueryCount=_RlIgmpMldSnoopVlanAdminLastMemberQueryCount_Object((1,3,6,1,4,1,9,6,1,101,55,5,5,1,28),_RlIgmpMldSnoopVlanAdminLastMemberQueryCount_Type())
rlIgmpMldSnoopVlanAdminLastMemberQueryCount.setMaxAccess(_C)
if mibBuilder.loadTexts:rlIgmpMldSnoopVlanAdminLastMemberQueryCount.setStatus(_A)
class _RlIgmpMldSnoopVlanAdminStartupQueryInterval_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4500000))
_RlIgmpMldSnoopVlanAdminStartupQueryInterval_Type.__name__=_E
_RlIgmpMldSnoopVlanAdminStartupQueryInterval_Object=MibTableColumn
rlIgmpMldSnoopVlanAdminStartupQueryInterval=_RlIgmpMldSnoopVlanAdminStartupQueryInterval_Object((1,3,6,1,4,1,9,6,1,101,55,5,5,1,29),_RlIgmpMldSnoopVlanAdminStartupQueryInterval_Type())
rlIgmpMldSnoopVlanAdminStartupQueryInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:rlIgmpMldSnoopVlanAdminStartupQueryInterval.setStatus(_A)
if mibBuilder.loadTexts:rlIgmpMldSnoopVlanAdminStartupQueryInterval.setUnits(_H)
class _RlIgmpMldSnoopVlanAdminStartupQueryCount_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_RlIgmpMldSnoopVlanAdminStartupQueryCount_Type.__name__=_E
_RlIgmpMldSnoopVlanAdminStartupQueryCount_Object=MibTableColumn
rlIgmpMldSnoopVlanAdminStartupQueryCount=_RlIgmpMldSnoopVlanAdminStartupQueryCount_Object((1,3,6,1,4,1,9,6,1,101,55,5,5,1,30),_RlIgmpMldSnoopVlanAdminStartupQueryCount_Type())
rlIgmpMldSnoopVlanAdminStartupQueryCount.setMaxAccess(_C)
if mibBuilder.loadTexts:rlIgmpMldSnoopVlanAdminStartupQueryCount.setStatus(_A)
class _RlIgmpMldSnoopVlanAdminHostTimeOut_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_RlIgmpMldSnoopVlanAdminHostTimeOut_Type.__name__=_E
_RlIgmpMldSnoopVlanAdminHostTimeOut_Object=MibTableColumn
rlIgmpMldSnoopVlanAdminHostTimeOut=_RlIgmpMldSnoopVlanAdminHostTimeOut_Object((1,3,6,1,4,1,9,6,1,101,55,5,5,1,31),_RlIgmpMldSnoopVlanAdminHostTimeOut_Type())
rlIgmpMldSnoopVlanAdminHostTimeOut.setMaxAccess(_C)
if mibBuilder.loadTexts:rlIgmpMldSnoopVlanAdminHostTimeOut.setStatus(_D)
if mibBuilder.loadTexts:rlIgmpMldSnoopVlanAdminHostTimeOut.setUnits(_H)
class _RlIgmpMldSnoopVlanAdminRouterTimeOut_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_RlIgmpMldSnoopVlanAdminRouterTimeOut_Type.__name__=_E
_RlIgmpMldSnoopVlanAdminRouterTimeOut_Object=MibTableColumn
rlIgmpMldSnoopVlanAdminRouterTimeOut=_RlIgmpMldSnoopVlanAdminRouterTimeOut_Object((1,3,6,1,4,1,9,6,1,101,55,5,5,1,32),_RlIgmpMldSnoopVlanAdminRouterTimeOut_Type())
rlIgmpMldSnoopVlanAdminRouterTimeOut.setMaxAccess(_C)
if mibBuilder.loadTexts:rlIgmpMldSnoopVlanAdminRouterTimeOut.setStatus(_D)
if mibBuilder.loadTexts:rlIgmpMldSnoopVlanAdminRouterTimeOut.setUnits(_H)
class _RlIgmpMldSnoopVlanAdminLeaveTimeOut_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_RlIgmpMldSnoopVlanAdminLeaveTimeOut_Type.__name__=_E
_RlIgmpMldSnoopVlanAdminLeaveTimeOut_Object=MibTableColumn
rlIgmpMldSnoopVlanAdminLeaveTimeOut=_RlIgmpMldSnoopVlanAdminLeaveTimeOut_Object((1,3,6,1,4,1,9,6,1,101,55,5,5,1,33),_RlIgmpMldSnoopVlanAdminLeaveTimeOut_Type())
rlIgmpMldSnoopVlanAdminLeaveTimeOut.setMaxAccess(_C)
if mibBuilder.loadTexts:rlIgmpMldSnoopVlanAdminLeaveTimeOut.setStatus(_D)
if mibBuilder.loadTexts:rlIgmpMldSnoopVlanAdminLeaveTimeOut.setUnits(_H)
class _RlIgmpMldSnoopVlanIsImmediateLeave_Type(TruthValue):defaultValue=2
_RlIgmpMldSnoopVlanIsImmediateLeave_Type.__name__=_M
_RlIgmpMldSnoopVlanIsImmediateLeave_Object=MibTableColumn
rlIgmpMldSnoopVlanIsImmediateLeave=_RlIgmpMldSnoopVlanIsImmediateLeave_Object((1,3,6,1,4,1,9,6,1,101,55,5,5,1,34),_RlIgmpMldSnoopVlanIsImmediateLeave_Type())
rlIgmpMldSnoopVlanIsImmediateLeave.setMaxAccess(_C)
if mibBuilder.loadTexts:rlIgmpMldSnoopVlanIsImmediateLeave.setStatus(_A)
_RlIgmpMldSnoopMulticastTvTable_Object=MibTable
rlIgmpMldSnoopMulticastTvTable=_RlIgmpMldSnoopMulticastTvTable_Object((1,3,6,1,4,1,9,6,1,101,55,5,6))
if mibBuilder.loadTexts:rlIgmpMldSnoopMulticastTvTable.setStatus(_A)
_RlIgmpMldSnoopMulticastTvEntry_Object=MibTableRow
rlIgmpMldSnoopMulticastTvEntry=_RlIgmpMldSnoopMulticastTvEntry_Object((1,3,6,1,4,1,9,6,1,101,55,5,6,1))
rlIgmpMldSnoopMulticastTvEntry.setIndexNames((0,_F,_b),(0,_F,_c),(0,_F,_d),(0,_F,_e))
if mibBuilder.loadTexts:rlIgmpMldSnoopMulticastTvEntry.setStatus(_A)
_RlIgmpMldSnoopMulticastTvInetAddressType_Type=InetAddressType
_RlIgmpMldSnoopMulticastTvInetAddressType_Object=MibTableColumn
rlIgmpMldSnoopMulticastTvInetAddressType=_RlIgmpMldSnoopMulticastTvInetAddressType_Object((1,3,6,1,4,1,9,6,1,101,55,5,6,1,1),_RlIgmpMldSnoopMulticastTvInetAddressType_Type())
rlIgmpMldSnoopMulticastTvInetAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:rlIgmpMldSnoopMulticastTvInetAddressType.setStatus(_A)
_RlIgmpMldSnoopMulticastTvVID_Type=VlanIndex
_RlIgmpMldSnoopMulticastTvVID_Object=MibTableColumn
rlIgmpMldSnoopMulticastTvVID=_RlIgmpMldSnoopMulticastTvVID_Object((1,3,6,1,4,1,9,6,1,101,55,5,6,1,2),_RlIgmpMldSnoopMulticastTvVID_Type())
rlIgmpMldSnoopMulticastTvVID.setMaxAccess(_B)
if mibBuilder.loadTexts:rlIgmpMldSnoopMulticastTvVID.setStatus(_A)
_RlIgmpMldSnoopMulticastTvGroupAddressType_Type=InetAddressType
_RlIgmpMldSnoopMulticastTvGroupAddressType_Object=MibTableColumn
rlIgmpMldSnoopMulticastTvGroupAddressType=_RlIgmpMldSnoopMulticastTvGroupAddressType_Object((1,3,6,1,4,1,9,6,1,101,55,5,6,1,3),_RlIgmpMldSnoopMulticastTvGroupAddressType_Type())
rlIgmpMldSnoopMulticastTvGroupAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:rlIgmpMldSnoopMulticastTvGroupAddressType.setStatus(_A)
_RlIgmpMldSnoopMulticastTvGroup_Type=InetAddress
_RlIgmpMldSnoopMulticastTvGroup_Object=MibTableColumn
rlIgmpMldSnoopMulticastTvGroup=_RlIgmpMldSnoopMulticastTvGroup_Object((1,3,6,1,4,1,9,6,1,101,55,5,6,1,4),_RlIgmpMldSnoopMulticastTvGroup_Type())
rlIgmpMldSnoopMulticastTvGroup.setMaxAccess(_B)
if mibBuilder.loadTexts:rlIgmpMldSnoopMulticastTvGroup.setStatus(_A)
_RlIgmpMldSnoopMulticastTvStatus_Type=RowStatus
_RlIgmpMldSnoopMulticastTvStatus_Object=MibTableColumn
rlIgmpMldSnoopMulticastTvStatus=_RlIgmpMldSnoopMulticastTvStatus_Object((1,3,6,1,4,1,9,6,1,101,55,5,6,1,5),_RlIgmpMldSnoopMulticastTvStatus_Type())
rlIgmpMldSnoopMulticastTvStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:rlIgmpMldSnoopMulticastTvStatus.setStatus(_A)
_RlMldSnoopQuerierVlanTable_Object=MibTable
rlMldSnoopQuerierVlanTable=_RlMldSnoopQuerierVlanTable_Object((1,3,6,1,4,1,9,6,1,101,55,5,7))
if mibBuilder.loadTexts:rlMldSnoopQuerierVlanTable.setStatus(_A)
_RlMldSnoopQuerierVlanEntry_Object=MibTableRow
rlMldSnoopQuerierVlanEntry=_RlMldSnoopQuerierVlanEntry_Object((1,3,6,1,4,1,9,6,1,101,55,5,7,1))
rlMldSnoopQuerierVlanEntry.setIndexNames((0,_F,_f))
if mibBuilder.loadTexts:rlMldSnoopQuerierVlanEntry.setStatus(_A)
_RlMldSnoopQuerierVlanTag_Type=VlanIndex
_RlMldSnoopQuerierVlanTag_Object=MibTableColumn
rlMldSnoopQuerierVlanTag=_RlMldSnoopQuerierVlanTag_Object((1,3,6,1,4,1,9,6,1,101,55,5,7,1,1),_RlMldSnoopQuerierVlanTag_Type())
rlMldSnoopQuerierVlanTag.setMaxAccess(_B)
if mibBuilder.loadTexts:rlMldSnoopQuerierVlanTag.setStatus(_A)
_RlMldSnoopQuerierAdminEnable_Type=TruthValue
_RlMldSnoopQuerierAdminEnable_Object=MibTableColumn
rlMldSnoopQuerierAdminEnable=_RlMldSnoopQuerierAdminEnable_Object((1,3,6,1,4,1,9,6,1,101,55,5,7,1,2),_RlMldSnoopQuerierAdminEnable_Type())
rlMldSnoopQuerierAdminEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:rlMldSnoopQuerierAdminEnable.setStatus(_A)
_RlMldSnoopQuerierOperEnable_Type=TruthValue
_RlMldSnoopQuerierOperEnable_Object=MibTableColumn
rlMldSnoopQuerierOperEnable=_RlMldSnoopQuerierOperEnable_Object((1,3,6,1,4,1,9,6,1,101,55,5,7,1,3),_RlMldSnoopQuerierOperEnable_Type())
rlMldSnoopQuerierOperEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:rlMldSnoopQuerierOperEnable.setStatus(_A)
_RlMldSnoopQuerierAdminAddrInetAddressType_Type=InetAddressType
_RlMldSnoopQuerierAdminAddrInetAddressType_Object=MibTableColumn
rlMldSnoopQuerierAdminAddrInetAddressType=_RlMldSnoopQuerierAdminAddrInetAddressType_Object((1,3,6,1,4,1,9,6,1,101,55,5,7,1,4),_RlMldSnoopQuerierAdminAddrInetAddressType_Type())
rlMldSnoopQuerierAdminAddrInetAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:rlMldSnoopQuerierAdminAddrInetAddressType.setStatus(_A)
_RlMldSnoopQuerierAdminAddr_Type=InetAddress
_RlMldSnoopQuerierAdminAddr_Object=MibTableColumn
rlMldSnoopQuerierAdminAddr=_RlMldSnoopQuerierAdminAddr_Object((1,3,6,1,4,1,9,6,1,101,55,5,7,1,5),_RlMldSnoopQuerierAdminAddr_Type())
rlMldSnoopQuerierAdminAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:rlMldSnoopQuerierAdminAddr.setStatus(_A)
_RlMldSnoopQuerierOperAddrInetAddressType_Type=InetAddressType
_RlMldSnoopQuerierOperAddrInetAddressType_Object=MibTableColumn
rlMldSnoopQuerierOperAddrInetAddressType=_RlMldSnoopQuerierOperAddrInetAddressType_Object((1,3,6,1,4,1,9,6,1,101,55,5,7,1,6),_RlMldSnoopQuerierOperAddrInetAddressType_Type())
rlMldSnoopQuerierOperAddrInetAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:rlMldSnoopQuerierOperAddrInetAddressType.setStatus(_A)
_RlMldSnoopQuerierOperAddr_Type=InetAddress
_RlMldSnoopQuerierOperAddr_Object=MibTableColumn
rlMldSnoopQuerierOperAddr=_RlMldSnoopQuerierOperAddr_Object((1,3,6,1,4,1,9,6,1,101,55,5,7,1,7),_RlMldSnoopQuerierOperAddr_Type())
rlMldSnoopQuerierOperAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:rlMldSnoopQuerierOperAddr.setStatus(_A)
_RlMldSnoopQuerierAdminVersionNumber_Type=MldVersion
_RlMldSnoopQuerierAdminVersionNumber_Object=MibTableColumn
rlMldSnoopQuerierAdminVersionNumber=_RlMldSnoopQuerierAdminVersionNumber_Object((1,3,6,1,4,1,9,6,1,101,55,5,7,1,8),_RlMldSnoopQuerierAdminVersionNumber_Type())
rlMldSnoopQuerierAdminVersionNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:rlMldSnoopQuerierAdminVersionNumber.setStatus(_A)
_RlMldSnoopQuerierOperVersionNumber_Type=MldVersion
_RlMldSnoopQuerierOperVersionNumber_Object=MibTableColumn
rlMldSnoopQuerierOperVersionNumber=_RlMldSnoopQuerierOperVersionNumber_Object((1,3,6,1,4,1,9,6,1,101,55,5,7,1,9),_RlMldSnoopQuerierOperVersionNumber_Type())
rlMldSnoopQuerierOperVersionNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:rlMldSnoopQuerierOperVersionNumber.setStatus(_A)
_RlMldSnoopQuerierElectionEnable_Type=TruthValue
_RlMldSnoopQuerierElectionEnable_Object=MibTableColumn
rlMldSnoopQuerierElectionEnable=_RlMldSnoopQuerierElectionEnable_Object((1,3,6,1,4,1,9,6,1,101,55,5,7,1,10),_RlMldSnoopQuerierElectionEnable_Type())
rlMldSnoopQuerierElectionEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:rlMldSnoopQuerierElectionEnable.setStatus(_A)
_RlMldSnoopQuerierEnable_Type=TruthValue
_RlMldSnoopQuerierEnable_Object=MibScalar
rlMldSnoopQuerierEnable=_RlMldSnoopQuerierEnable_Object((1,3,6,1,4,1,9,6,1,101,55,5,8),_RlMldSnoopQuerierEnable_Type())
rlMldSnoopQuerierEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:rlMldSnoopQuerierEnable.setStatus(_A)
_RlIgmpMldSnoopQuerierGlobalAddressTable_Object=MibTable
rlIgmpMldSnoopQuerierGlobalAddressTable=_RlIgmpMldSnoopQuerierGlobalAddressTable_Object((1,3,6,1,4,1,9,6,1,101,55,5,9))
if mibBuilder.loadTexts:rlIgmpMldSnoopQuerierGlobalAddressTable.setStatus(_A)
_RlIgmpMldSnoopQuerierGlobalAddressEntry_Object=MibTableRow
rlIgmpMldSnoopQuerierGlobalAddressEntry=_RlIgmpMldSnoopQuerierGlobalAddressEntry_Object((1,3,6,1,4,1,9,6,1,101,55,5,9,1))
rlIgmpMldSnoopQuerierGlobalAddressEntry.setIndexNames((0,_F,_g))
if mibBuilder.loadTexts:rlIgmpMldSnoopQuerierGlobalAddressEntry.setStatus(_A)
_RlIgmpMldSnoopQuerierGlobalAddressIPVersion_Type=InetVersion
_RlIgmpMldSnoopQuerierGlobalAddressIPVersion_Object=MibTableColumn
rlIgmpMldSnoopQuerierGlobalAddressIPVersion=_RlIgmpMldSnoopQuerierGlobalAddressIPVersion_Object((1,3,6,1,4,1,9,6,1,101,55,5,9,1,1),_RlIgmpMldSnoopQuerierGlobalAddressIPVersion_Type())
rlIgmpMldSnoopQuerierGlobalAddressIPVersion.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:rlIgmpMldSnoopQuerierGlobalAddressIPVersion.setStatus(_A)
_RlIgmpMldSnoopQuerierGlobalAddressType_Type=InetAddressType
_RlIgmpMldSnoopQuerierGlobalAddressType_Object=MibTableColumn
rlIgmpMldSnoopQuerierGlobalAddressType=_RlIgmpMldSnoopQuerierGlobalAddressType_Object((1,3,6,1,4,1,9,6,1,101,55,5,9,1,2),_RlIgmpMldSnoopQuerierGlobalAddressType_Type())
rlIgmpMldSnoopQuerierGlobalAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:rlIgmpMldSnoopQuerierGlobalAddressType.setStatus(_A)
_RlIgmpMldSnoopQuerierGlobalAddress_Type=InetAddress
_RlIgmpMldSnoopQuerierGlobalAddress_Object=MibTableColumn
rlIgmpMldSnoopQuerierGlobalAddress=_RlIgmpMldSnoopQuerierGlobalAddress_Object((1,3,6,1,4,1,9,6,1,101,55,5,9,1,3),_RlIgmpMldSnoopQuerierGlobalAddress_Type())
rlIgmpMldSnoopQuerierGlobalAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:rlIgmpMldSnoopQuerierGlobalAddress.setStatus(_A)
rlMacMulticastUnregFilterFailed=NotificationType((1,3,6,1,4,1,9,6,1,101,0,1))
rlMacMulticastUnregFilterFailed.setObjects(*((_J,_K),(_J,_L)))
if mibBuilder.loadTexts:rlMacMulticastUnregFilterFailed.setStatus('')
rlIgmpMldSnoopTriplePlayPort=NotificationType((1,3,6,1,4,1,9,6,1,101,0,208))
rlIgmpMldSnoopTriplePlayPort.setObjects(*((_J,_K),(_J,_L)))
if mibBuilder.loadTexts:rlIgmpMldSnoopTriplePlayPort.setStatus(_A)
rlbrgIgmpSnoopQrrDuplicateIP=NotificationType((1,3,6,1,4,1,9,6,1,101,0,227))
rlbrgIgmpSnoopQrrDuplicateIP.setObjects(*((_J,_K),(_J,_L)))
if mibBuilder.loadTexts:rlbrgIgmpSnoopQrrDuplicateIP.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'IgmpVersion':IgmpVersion,'MldVersion':MldVersion,'rlMacMulticastUnregFilterFailed':rlMacMulticastUnregFilterFailed,'rlIgmpMldSnoopTriplePlayPort':rlIgmpMldSnoopTriplePlayPort,'rlbrgIgmpSnoopQrrDuplicateIP':rlbrgIgmpSnoopQrrDuplicateIP,'rlMacMulticastEnable':rlMacMulticastEnable,'rlIgmpSnoop':rlIgmpSnoop,'rlIgmpSnoopMibVersion':rlIgmpSnoopMibVersion,'rlIgmpSnoopEnable':rlIgmpSnoopEnable,'rlIgmpSnoopHostAgingTime':rlIgmpSnoopHostAgingTime,'rlIgmpSnoopRouterAgingTime':rlIgmpSnoopRouterAgingTime,'rlIgmpSnoopVlanTable':rlIgmpSnoopVlanTable,'rlIgmpSnoopVlanEntry':rlIgmpSnoopVlanEntry,_N:rlIgmpSnoopVlanTag,'rlIgmpSnoopVlanEnable':rlIgmpSnoopVlanEnable,'rlIgmpSnoopVlanRouterLearn':rlIgmpSnoopVlanRouterLearn,'rlIgmpSnoopVlanHostTimeOut':rlIgmpSnoopVlanHostTimeOut,'rlIgmpSnoopVlanQuerierTimeOut':rlIgmpSnoopVlanQuerierTimeOut,'rlIgmpSnoopVlanRouterTimeOut':rlIgmpSnoopVlanRouterTimeOut,'rlIgmpSnoopVlanLeaveTimeOut':rlIgmpSnoopVlanLeaveTimeOut,'rlIgmpSnoopVlanIgmpVersion':rlIgmpSnoopVlanIgmpVersion,'rlIgmpSnoopVlanRouterPortlist':rlIgmpSnoopVlanRouterPortlist,'rlIgmpSnoopIGMP224ReportsHandle':rlIgmpSnoopIGMP224ReportsHandle,'rlIgmpSnoopMulticastTvTable':rlIgmpSnoopMulticastTvTable,'rlIgmpSnoopMulticastTvEntry':rlIgmpSnoopMulticastTvEntry,_O:rlIgmpSnoopMulticastTvVID,_P:rlIgmpSnoopMulticastTvGroup,'rlIgmpSnoopMulticastTvStatus':rlIgmpSnoopMulticastTvStatus,'rlIgmpSnoopMulticastTvCount':rlIgmpSnoopMulticastTvCount,'rlIgmpSnoopMembershipTable':rlIgmpSnoopMembershipTable,'rlIgmpSnoopMembershipEntry':rlIgmpSnoopMembershipEntry,_Q:rlIgmpSnoopMembershipVlanTag,_R:rlIgmpSnoopMembershipGroupIpAddress,_S:rlIgmpSnoopMembershipSourceIpAddress,'rlIgmpSnoopMembershipIncPortlist':rlIgmpSnoopMembershipIncPortlist,'rlIgmpSnoopMembershipExcPortlist':rlIgmpSnoopMembershipExcPortlist,'rlIgmpSnoopMembershipExpiryTime':rlIgmpSnoopMembershipExpiryTime,'rlIgmpSnoopMembershipCompatibilityMode':rlIgmpSnoopMembershipCompatibilityMode,'rlIgmpSnoopQuerierVlanTable':rlIgmpSnoopQuerierVlanTable,'rlIgmpSnoopQuerierVlanEntry':rlIgmpSnoopQuerierVlanEntry,_T:rlIgmpSnoopQuerierVlanTag,'rlIgmpSnoopQuerierAdminEnable':rlIgmpSnoopQuerierAdminEnable,'rlIgmpSnoopQuerierOperEnable':rlIgmpSnoopQuerierOperEnable,'rlIgmpSnoopQuerierAdminAddr':rlIgmpSnoopQuerierAdminAddr,'rlIgmpSnoopQuerierOperAddr':rlIgmpSnoopQuerierOperAddr,'rlIgmpSnoopQuerierAdminVersionNumber':rlIgmpSnoopQuerierAdminVersionNumber,'rlIgmpSnoopQuerierOperVersionNumber':rlIgmpSnoopQuerierOperVersionNumber,'rlIgmpSnoopQuerierElectionEnable':rlIgmpSnoopQuerierElectionEnable,'rlIgmpSnoopQuerierEnable':rlIgmpSnoopQuerierEnable,'rlMacMulticastMaxEntriesNum':rlMacMulticastMaxEntriesNum,'rlMacMulticastFilter':rlMacMulticastFilter,'rlMacMulticastUnregFilterEnable':rlMacMulticastUnregFilterEnable,'rlMldSnoop':rlMldSnoop,'rlMldSnoopEnable':rlMldSnoopEnable,'rlMldSnoopHostAgingTime':rlMldSnoopHostAgingTime,'rlMldSnoopRouterAgingTime':rlMldSnoopRouterAgingTime,'rlIgmpMldSnoopMembershipTable':rlIgmpMldSnoopMembershipTable,'rlIgmpMldSnoopMembershipEntry':rlIgmpMldSnoopMembershipEntry,_U:rlIgmpMldSnoopMembershipVlanTag,_V:rlIgmpMldSnoopMembershipGroupIpAddressType,_W:rlIgmpMldSnoopMembershipGroupIpAddress,_X:rlIgmpMldSnoopMembershipSourceIpAddressType,_Y:rlIgmpMldSnoopMembershipSourceIpAddress,'rlIgmpMldSnoopMembershipIncPortlist':rlIgmpMldSnoopMembershipIncPortlist,'rlIgmpMldSnoopMembershipExcPortlist':rlIgmpMldSnoopMembershipExcPortlist,'rlIgmpMldSnoopMembershipExpiryTime':rlIgmpMldSnoopMembershipExpiryTime,'rlIgmpMldSnoopMembershipCompatibilityMode':rlIgmpMldSnoopMembershipCompatibilityMode,'rlIgmpMldSnoopVlanTable':rlIgmpMldSnoopVlanTable,'rlIgmpMldSnoopVlanEntry':rlIgmpMldSnoopVlanEntry,_Z:rlIgmpMldSnoopVlanInetAddressType,_a:rlIgmpMldSnoopVlanTag,'rlIgmpMldSnoopVlanEnable':rlIgmpMldSnoopVlanEnable,'rlIgmpMldSnoopVlanRouterLearn':rlIgmpMldSnoopVlanRouterLearn,'rlIgmpMldSnoopVlanHostTimeOut':rlIgmpMldSnoopVlanHostTimeOut,'rlIgmpMldSnoopVlanQuerierTimeOut':rlIgmpMldSnoopVlanQuerierTimeOut,'rlIgmpMldSnoopVlanRouterTimeOut':rlIgmpMldSnoopVlanRouterTimeOut,'rlIgmpMldSnoopVlanLeaveTimeOut':rlIgmpMldSnoopVlanLeaveTimeOut,'rlIgmpMldSnoopVlanIgmpVersion':rlIgmpMldSnoopVlanIgmpVersion,'rlIgmpMldSnoopVlanRouterPortlist':rlIgmpMldSnoopVlanRouterPortlist,'rlIgmpMldSnoopVlanRouterStaticPortlist':rlIgmpMldSnoopVlanRouterStaticPortlist,'rlIgmpMldSnoopVlanRouterForbiddenPortlist':rlIgmpMldSnoopVlanRouterForbiddenPortlist,'rlIgmpMldSnoopVlanQueryOverride':rlIgmpMldSnoopVlanQueryOverride,'rlIgmpMldSnoopVlanOperRobustness':rlIgmpMldSnoopVlanOperRobustness,'rlIgmpMldSnoopVlanOperQueryInterval':rlIgmpMldSnoopVlanOperQueryInterval,'rlIgmpMldSnoopVlanOperQueryMaxResponseTime':rlIgmpMldSnoopVlanOperQueryMaxResponseTime,'rlIgmpMldSnoopVlanOperLastMemberQueryInterval':rlIgmpMldSnoopVlanOperLastMemberQueryInterval,'rlIgmpMldSnoopVlanOperLastMemberQueryCount':rlIgmpMldSnoopVlanOperLastMemberQueryCount,'rlIgmpMldSnoopVlanOperStartupQueryInterval':rlIgmpMldSnoopVlanOperStartupQueryInterval,'rlIgmpMldSnoopVlanOperStartupQueryCount':rlIgmpMldSnoopVlanOperStartupQueryCount,'rlIgmpMldSnoopVlanOperHostTimeOut':rlIgmpMldSnoopVlanOperHostTimeOut,'rlIgmpMldSnoopVlanOperRouterTimeOut':rlIgmpMldSnoopVlanOperRouterTimeOut,'rlIgmpMldSnoopVlanOperLeaveTimeOut':rlIgmpMldSnoopVlanOperLeaveTimeOut,'rlIgmpMldSnoopVlanAdminRobustness':rlIgmpMldSnoopVlanAdminRobustness,'rlIgmpMldSnoopVlanAdminQueryInterval':rlIgmpMldSnoopVlanAdminQueryInterval,'rlIgmpMldSnoopVlanAdminQueryMaxResponseTime':rlIgmpMldSnoopVlanAdminQueryMaxResponseTime,'rlIgmpMldSnoopVlanAdminLastMemberQueryInterval':rlIgmpMldSnoopVlanAdminLastMemberQueryInterval,'rlIgmpMldSnoopVlanAdminLastMemberQueryCount':rlIgmpMldSnoopVlanAdminLastMemberQueryCount,'rlIgmpMldSnoopVlanAdminStartupQueryInterval':rlIgmpMldSnoopVlanAdminStartupQueryInterval,'rlIgmpMldSnoopVlanAdminStartupQueryCount':rlIgmpMldSnoopVlanAdminStartupQueryCount,'rlIgmpMldSnoopVlanAdminHostTimeOut':rlIgmpMldSnoopVlanAdminHostTimeOut,'rlIgmpMldSnoopVlanAdminRouterTimeOut':rlIgmpMldSnoopVlanAdminRouterTimeOut,'rlIgmpMldSnoopVlanAdminLeaveTimeOut':rlIgmpMldSnoopVlanAdminLeaveTimeOut,'rlIgmpMldSnoopVlanIsImmediateLeave':rlIgmpMldSnoopVlanIsImmediateLeave,'rlIgmpMldSnoopMulticastTvTable':rlIgmpMldSnoopMulticastTvTable,'rlIgmpMldSnoopMulticastTvEntry':rlIgmpMldSnoopMulticastTvEntry,_b:rlIgmpMldSnoopMulticastTvInetAddressType,_c:rlIgmpMldSnoopMulticastTvVID,_d:rlIgmpMldSnoopMulticastTvGroupAddressType,_e:rlIgmpMldSnoopMulticastTvGroup,'rlIgmpMldSnoopMulticastTvStatus':rlIgmpMldSnoopMulticastTvStatus,'rlMldSnoopQuerierVlanTable':rlMldSnoopQuerierVlanTable,'rlMldSnoopQuerierVlanEntry':rlMldSnoopQuerierVlanEntry,_f:rlMldSnoopQuerierVlanTag,'rlMldSnoopQuerierAdminEnable':rlMldSnoopQuerierAdminEnable,'rlMldSnoopQuerierOperEnable':rlMldSnoopQuerierOperEnable,'rlMldSnoopQuerierAdminAddrInetAddressType':rlMldSnoopQuerierAdminAddrInetAddressType,'rlMldSnoopQuerierAdminAddr':rlMldSnoopQuerierAdminAddr,'rlMldSnoopQuerierOperAddrInetAddressType':rlMldSnoopQuerierOperAddrInetAddressType,'rlMldSnoopQuerierOperAddr':rlMldSnoopQuerierOperAddr,'rlMldSnoopQuerierAdminVersionNumber':rlMldSnoopQuerierAdminVersionNumber,'rlMldSnoopQuerierOperVersionNumber':rlMldSnoopQuerierOperVersionNumber,'rlMldSnoopQuerierElectionEnable':rlMldSnoopQuerierElectionEnable,'rlMldSnoopQuerierEnable':rlMldSnoopQuerierEnable,'rlIgmpMldSnoopQuerierGlobalAddressTable':rlIgmpMldSnoopQuerierGlobalAddressTable,'rlIgmpMldSnoopQuerierGlobalAddressEntry':rlIgmpMldSnoopQuerierGlobalAddressEntry,_g:rlIgmpMldSnoopQuerierGlobalAddressIPVersion,'rlIgmpMldSnoopQuerierGlobalAddressType':rlIgmpMldSnoopQuerierGlobalAddressType,'rlIgmpMldSnoopQuerierGlobalAddress':rlIgmpMldSnoopQuerierGlobalAddress})