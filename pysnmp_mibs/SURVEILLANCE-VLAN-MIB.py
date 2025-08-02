_O='swSurveillanceVlanPortNumber'
_N='swSurveillanceVlanOuiAddr'
_M='network-storage'
_L='video-encoder'
_K='vms-client'
_J='swSurveillanceVlanDevAddr'
_I='swSurveillanceVlanDevPort'
_H='disabled'
_G='enabled'
_F='read-create'
_E='SURVEILLANCE-VLAN-MIB'
_D='read-write'
_C='read-only'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dlink_common_mgmt,=mibBuilder.importSymbols('DLINK-ID-REC-MIB','dlink-common-mgmt')
PortList,VlanIdOrNone=mibBuilder.importSymbols('Q-BRIDGE-MIB','PortList','VlanIdOrNone')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TimeInterval,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TimeInterval','TruthValue')
swSurveillanceVLANMIB=ModuleIdentity((1,3,6,1,4,1,171,12,102))
_SwSurveillanceVLANNotifications_ObjectIdentity=ObjectIdentity
swSurveillanceVLANNotifications=_SwSurveillanceVLANNotifications_ObjectIdentity((1,3,6,1,4,1,171,12,102,0))
_SwSurveillanceVLANMIBObjects_ObjectIdentity=ObjectIdentity
swSurveillanceVLANMIBObjects=_SwSurveillanceVLANMIBObjects_ObjectIdentity((1,3,6,1,4,1,171,12,102,1))
_SwSurveillanceVlanCtrl_ObjectIdentity=ObjectIdentity
swSurveillanceVlanCtrl=_SwSurveillanceVlanCtrl_ObjectIdentity((1,3,6,1,4,1,171,12,102,1,1))
_SwSurveillanceVlanId_Type=VlanIdOrNone
_SwSurveillanceVlanId_Object=MibScalar
swSurveillanceVlanId=_SwSurveillanceVlanId_Object((1,3,6,1,4,1,171,12,102,1,1,1),_SwSurveillanceVlanId_Type())
swSurveillanceVlanId.setMaxAccess(_D)
if mibBuilder.loadTexts:swSurveillanceVlanId.setStatus(_A)
class _SwSurveillanceVlanGlobalState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_SwSurveillanceVlanGlobalState_Type.__name__=_B
_SwSurveillanceVlanGlobalState_Object=MibScalar
swSurveillanceVlanGlobalState=_SwSurveillanceVlanGlobalState_Object((1,3,6,1,4,1,171,12,102,1,1,2),_SwSurveillanceVlanGlobalState_Type())
swSurveillanceVlanGlobalState.setMaxAccess(_D)
if mibBuilder.loadTexts:swSurveillanceVlanGlobalState.setStatus(_A)
class _SwSurveillanceVlanPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_SwSurveillanceVlanPriority_Type.__name__=_B
_SwSurveillanceVlanPriority_Object=MibScalar
swSurveillanceVlanPriority=_SwSurveillanceVlanPriority_Object((1,3,6,1,4,1,171,12,102,1,1,3),_SwSurveillanceVlanPriority_Type())
swSurveillanceVlanPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:swSurveillanceVlanPriority.setStatus(_A)
class _SwSurveillanceVlanAgingTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SwSurveillanceVlanAgingTime_Type.__name__=_B
_SwSurveillanceVlanAgingTime_Object=MibScalar
swSurveillanceVlanAgingTime=_SwSurveillanceVlanAgingTime_Object((1,3,6,1,4,1,171,12,102,1,1,4),_SwSurveillanceVlanAgingTime_Type())
swSurveillanceVlanAgingTime.setMaxAccess(_D)
if mibBuilder.loadTexts:swSurveillanceVlanAgingTime.setStatus(_A)
class _SwSurveillanceVlanLogState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_SwSurveillanceVlanLogState_Type.__name__=_B
_SwSurveillanceVlanLogState_Object=MibScalar
swSurveillanceVlanLogState=_SwSurveillanceVlanLogState_Object((1,3,6,1,4,1,171,12,102,1,1,5),_SwSurveillanceVlanLogState_Type())
swSurveillanceVlanLogState.setMaxAccess(_D)
if mibBuilder.loadTexts:swSurveillanceVlanLogState.setStatus(_A)
_SwSurveillanceVlanInfo_ObjectIdentity=ObjectIdentity
swSurveillanceVlanInfo=_SwSurveillanceVlanInfo_ObjectIdentity((1,3,6,1,4,1,171,12,102,1,2))
_SwSurveillanceVlanMemberPortlist_Type=PortList
_SwSurveillanceVlanMemberPortlist_Object=MibScalar
swSurveillanceVlanMemberPortlist=_SwSurveillanceVlanMemberPortlist_Object((1,3,6,1,4,1,171,12,102,1,2,1),_SwSurveillanceVlanMemberPortlist_Type())
swSurveillanceVlanMemberPortlist.setMaxAccess(_C)
if mibBuilder.loadTexts:swSurveillanceVlanMemberPortlist.setStatus(_A)
_SwSurveillanceVlanDynamicPortlist_Type=PortList
_SwSurveillanceVlanDynamicPortlist_Object=MibScalar
swSurveillanceVlanDynamicPortlist=_SwSurveillanceVlanDynamicPortlist_Object((1,3,6,1,4,1,171,12,102,1,2,2),_SwSurveillanceVlanDynamicPortlist_Type())
swSurveillanceVlanDynamicPortlist.setMaxAccess(_C)
if mibBuilder.loadTexts:swSurveillanceVlanDynamicPortlist.setStatus(_A)
_SwSurveillanceVlanDeviceTable_Object=MibTable
swSurveillanceVlanDeviceTable=_SwSurveillanceVlanDeviceTable_Object((1,3,6,1,4,1,171,12,102,1,2,3))
if mibBuilder.loadTexts:swSurveillanceVlanDeviceTable.setStatus(_A)
_SwSurveillanceVlanDeviceEntry_Object=MibTableRow
swSurveillanceVlanDeviceEntry=_SwSurveillanceVlanDeviceEntry_Object((1,3,6,1,4,1,171,12,102,1,2,3,1))
swSurveillanceVlanDeviceEntry.setIndexNames((0,_E,_I),(0,_E,_J))
if mibBuilder.loadTexts:swSurveillanceVlanDeviceEntry.setStatus(_A)
_SwSurveillanceVlanDevPort_Type=Integer32
_SwSurveillanceVlanDevPort_Object=MibTableColumn
swSurveillanceVlanDevPort=_SwSurveillanceVlanDevPort_Object((1,3,6,1,4,1,171,12,102,1,2,3,1,1),_SwSurveillanceVlanDevPort_Type())
swSurveillanceVlanDevPort.setMaxAccess(_C)
if mibBuilder.loadTexts:swSurveillanceVlanDevPort.setStatus(_A)
_SwSurveillanceVlanDevAddr_Type=MacAddress
_SwSurveillanceVlanDevAddr_Object=MibTableColumn
swSurveillanceVlanDevAddr=_SwSurveillanceVlanDevAddr_Object((1,3,6,1,4,1,171,12,102,1,2,3,1,2),_SwSurveillanceVlanDevAddr_Type())
swSurveillanceVlanDevAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:swSurveillanceVlanDevAddr.setStatus(_A)
class _SwSurveillanceVlanDevComponentType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('vms',1),(_K,2),(_L,3),(_M,4),('other',5)))
_SwSurveillanceVlanDevComponentType_Type.__name__=_B
_SwSurveillanceVlanDevComponentType_Object=MibTableColumn
swSurveillanceVlanDevComponentType=_SwSurveillanceVlanDevComponentType_Object((1,3,6,1,4,1,171,12,102,1,2,3,1,3),_SwSurveillanceVlanDevComponentType_Type())
swSurveillanceVlanDevComponentType.setMaxAccess(_F)
if mibBuilder.loadTexts:swSurveillanceVlanDevComponentType.setStatus(_A)
_SwSurveillanceVlanDevStartTime_Type=DateAndTime
_SwSurveillanceVlanDevStartTime_Object=MibTableColumn
swSurveillanceVlanDevStartTime=_SwSurveillanceVlanDevStartTime_Object((1,3,6,1,4,1,171,12,102,1,2,3,1,4),_SwSurveillanceVlanDevStartTime_Type())
swSurveillanceVlanDevStartTime.setMaxAccess(_C)
if mibBuilder.loadTexts:swSurveillanceVlanDevStartTime.setStatus(_A)
_SwSurveillanceVlanMgmt_ObjectIdentity=ObjectIdentity
swSurveillanceVlanMgmt=_SwSurveillanceVlanMgmt_ObjectIdentity((1,3,6,1,4,1,171,12,102,1,3))
_SwSurveillanceVlanOuiTable_Object=MibTable
swSurveillanceVlanOuiTable=_SwSurveillanceVlanOuiTable_Object((1,3,6,1,4,1,171,12,102,1,3,1))
if mibBuilder.loadTexts:swSurveillanceVlanOuiTable.setStatus(_A)
_SwSurveillanceVlanOuiEntry_Object=MibTableRow
swSurveillanceVlanOuiEntry=_SwSurveillanceVlanOuiEntry_Object((1,3,6,1,4,1,171,12,102,1,3,1,1))
swSurveillanceVlanOuiEntry.setIndexNames((0,_E,_N))
if mibBuilder.loadTexts:swSurveillanceVlanOuiEntry.setStatus(_A)
_SwSurveillanceVlanOuiAddr_Type=MacAddress
_SwSurveillanceVlanOuiAddr_Object=MibTableColumn
swSurveillanceVlanOuiAddr=_SwSurveillanceVlanOuiAddr_Object((1,3,6,1,4,1,171,12,102,1,3,1,1,1),_SwSurveillanceVlanOuiAddr_Type())
swSurveillanceVlanOuiAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:swSurveillanceVlanOuiAddr.setStatus(_A)
_SwSurveillanceVlanOuiMask_Type=MacAddress
_SwSurveillanceVlanOuiMask_Object=MibTableColumn
swSurveillanceVlanOuiMask=_SwSurveillanceVlanOuiMask_Object((1,3,6,1,4,1,171,12,102,1,3,1,1,2),_SwSurveillanceVlanOuiMask_Type())
swSurveillanceVlanOuiMask.setMaxAccess(_F)
if mibBuilder.loadTexts:swSurveillanceVlanOuiMask.setStatus(_A)
class _SwSurveillanceVlanOuiComponentType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('vms',1),(_K,2),(_L,3),(_M,4),('other',5)))
_SwSurveillanceVlanOuiComponentType_Type.__name__=_B
_SwSurveillanceVlanOuiComponentType_Object=MibTableColumn
swSurveillanceVlanOuiComponentType=_SwSurveillanceVlanOuiComponentType_Object((1,3,6,1,4,1,171,12,102,1,3,1,1,3),_SwSurveillanceVlanOuiComponentType_Type())
swSurveillanceVlanOuiComponentType.setMaxAccess(_F)
if mibBuilder.loadTexts:swSurveillanceVlanOuiComponentType.setStatus(_A)
_SwSurveillanceVlanOuiDes_Type=DisplayString
_SwSurveillanceVlanOuiDes_Object=MibTableColumn
swSurveillanceVlanOuiDes=_SwSurveillanceVlanOuiDes_Object((1,3,6,1,4,1,171,12,102,1,3,1,1,4),_SwSurveillanceVlanOuiDes_Type())
swSurveillanceVlanOuiDes.setMaxAccess(_F)
if mibBuilder.loadTexts:swSurveillanceVlanOuiDes.setStatus(_A)
_SwSurveillanceVlanOuiRowStatus_Type=RowStatus
_SwSurveillanceVlanOuiRowStatus_Object=MibTableColumn
swSurveillanceVlanOuiRowStatus=_SwSurveillanceVlanOuiRowStatus_Object((1,3,6,1,4,1,171,12,102,1,3,1,1,5),_SwSurveillanceVlanOuiRowStatus_Type())
swSurveillanceVlanOuiRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:swSurveillanceVlanOuiRowStatus.setStatus(_A)
_SwSurveillanceVlanPortTable_Object=MibTable
swSurveillanceVlanPortTable=_SwSurveillanceVlanPortTable_Object((1,3,6,1,4,1,171,12,102,1,3,2))
if mibBuilder.loadTexts:swSurveillanceVlanPortTable.setStatus(_A)
_SwSurveillanceVlanPortEntry_Object=MibTableRow
swSurveillanceVlanPortEntry=_SwSurveillanceVlanPortEntry_Object((1,3,6,1,4,1,171,12,102,1,3,2,1))
swSurveillanceVlanPortEntry.setIndexNames((0,_E,_O))
if mibBuilder.loadTexts:swSurveillanceVlanPortEntry.setStatus(_A)
_SwSurveillanceVlanPortNumber_Type=Integer32
_SwSurveillanceVlanPortNumber_Object=MibTableColumn
swSurveillanceVlanPortNumber=_SwSurveillanceVlanPortNumber_Object((1,3,6,1,4,1,171,12,102,1,3,2,1,1),_SwSurveillanceVlanPortNumber_Type())
swSurveillanceVlanPortNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:swSurveillanceVlanPortNumber.setStatus(_A)
class _SwSurveillanceVlanPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_SwSurveillanceVlanPortState_Type.__name__=_B
_SwSurveillanceVlanPortState_Object=MibTableColumn
swSurveillanceVlanPortState=_SwSurveillanceVlanPortState_Object((1,3,6,1,4,1,171,12,102,1,3,2,1,2),_SwSurveillanceVlanPortState_Type())
swSurveillanceVlanPortState.setMaxAccess(_D)
if mibBuilder.loadTexts:swSurveillanceVlanPortState.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'swSurveillanceVLANMIB':swSurveillanceVLANMIB,'swSurveillanceVLANNotifications':swSurveillanceVLANNotifications,'swSurveillanceVLANMIBObjects':swSurveillanceVLANMIBObjects,'swSurveillanceVlanCtrl':swSurveillanceVlanCtrl,'swSurveillanceVlanId':swSurveillanceVlanId,'swSurveillanceVlanGlobalState':swSurveillanceVlanGlobalState,'swSurveillanceVlanPriority':swSurveillanceVlanPriority,'swSurveillanceVlanAgingTime':swSurveillanceVlanAgingTime,'swSurveillanceVlanLogState':swSurveillanceVlanLogState,'swSurveillanceVlanInfo':swSurveillanceVlanInfo,'swSurveillanceVlanMemberPortlist':swSurveillanceVlanMemberPortlist,'swSurveillanceVlanDynamicPortlist':swSurveillanceVlanDynamicPortlist,'swSurveillanceVlanDeviceTable':swSurveillanceVlanDeviceTable,'swSurveillanceVlanDeviceEntry':swSurveillanceVlanDeviceEntry,_I:swSurveillanceVlanDevPort,_J:swSurveillanceVlanDevAddr,'swSurveillanceVlanDevComponentType':swSurveillanceVlanDevComponentType,'swSurveillanceVlanDevStartTime':swSurveillanceVlanDevStartTime,'swSurveillanceVlanMgmt':swSurveillanceVlanMgmt,'swSurveillanceVlanOuiTable':swSurveillanceVlanOuiTable,'swSurveillanceVlanOuiEntry':swSurveillanceVlanOuiEntry,_N:swSurveillanceVlanOuiAddr,'swSurveillanceVlanOuiMask':swSurveillanceVlanOuiMask,'swSurveillanceVlanOuiComponentType':swSurveillanceVlanOuiComponentType,'swSurveillanceVlanOuiDes':swSurveillanceVlanOuiDes,'swSurveillanceVlanOuiRowStatus':swSurveillanceVlanOuiRowStatus,'swSurveillanceVlanPortTable':swSurveillanceVlanPortTable,'swSurveillanceVlanPortEntry':swSurveillanceVlanPortEntry,_O:swSurveillanceVlanPortNumber,'swSurveillanceVlanPortState':swSurveillanceVlanPortState})