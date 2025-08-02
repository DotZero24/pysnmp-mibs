_j='hpicfIpLockTrapsGroup'
_i='hpicfIpLockTrapObjectsGroup'
_h='hpicfIpLockBaseGroup'
_g='hpicfIpLockErrantNotify'
_f='hpicfIpLockOutOfResources'
_e='hpicfIpLockTrapCntl'
_d='hpicfIpLockTrapCtrl'
_c='hpicfIpLockResourceAvailable'
_b='hpicfIpLockPortOperStatus'
_a='hpicfIpLockPortEnable'
_Z='hpicfIpLockEnable'
_Y='obsolete'
_X='TruthValue'
_W='Integer32'
_V='hpicfIpLockNotifyPktCount'
_U='hpicfIpLockNotifyMacAddress'
_T='hpicfIpLockNotifyDstIpAddress'
_S='hpicfIpLockNotifyDstIpType'
_R='hpicfIpLockNotifySrcIpAddress'
_Q='hpicfIpLockNotifySrcIpType'
_P='hpicfIpLockNotifyPort'
_O='hpicfIpLockNotifyCount'
_N='hpicfIpLockOutOfResourceSource'
_M='hpicfIpLockAddrMacAddress'
_L='hpicfIpLockAddrVlan'
_K='hpicfIpLockAddrType'
_J='Bits'
_I='ifIndex'
_H='IF-MIB'
_G='hpicfIpLockAddrIpAddress'
_F='hpicfIpLockAddrPort'
_E='read-write'
_D='read-only'
_C='accessible-for-notify'
_B='current'
_A='HP-ICF-IP-LOCKDOWN-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpSwitch,=mibBuilder.importSymbols('HP-ICF-OID','hpSwitch')
InterfaceIndex,ifIndex=mibBuilder.importSymbols(_H,'InterfaceIndex',_I)
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
VlanIndex,=mibBuilder.importSymbols('Q-BRIDGE-MIB','VlanIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_J,'Counter32','Counter64','Gauge32',_W,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention',_X)
hpicfIpLockdown=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,5,1,39))
if mibBuilder.loadTexts:hpicfIpLockdown.setRevisions(('2008-03-16 05:24','2006-06-08 23:47'))
_HpicfIpLockTraps_ObjectIdentity=ObjectIdentity
hpicfIpLockTraps=_HpicfIpLockTraps_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,39,0))
_HpicfIpLockTrapsObjects_ObjectIdentity=ObjectIdentity
hpicfIpLockTrapsObjects=_HpicfIpLockTrapsObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,39,0,1))
class _HpicfIpLockOutOfResourceSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('dhcpsnooping',1),('iplockdown',2)))
_HpicfIpLockOutOfResourceSource_Type.__name__=_W
_HpicfIpLockOutOfResourceSource_Object=MibScalar
hpicfIpLockOutOfResourceSource=_HpicfIpLockOutOfResourceSource_Object((1,3,6,1,4,1,11,2,14,11,5,1,39,0,1,1),_HpicfIpLockOutOfResourceSource_Type())
hpicfIpLockOutOfResourceSource.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfIpLockOutOfResourceSource.setStatus(_B)
_HpicfIpLockErrantNotifyObjects_ObjectIdentity=ObjectIdentity
hpicfIpLockErrantNotifyObjects=_HpicfIpLockErrantNotifyObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,39,0,1,4))
_HpicfIpLockNotifyCount_Type=Counter32
_HpicfIpLockNotifyCount_Object=MibScalar
hpicfIpLockNotifyCount=_HpicfIpLockNotifyCount_Object((1,3,6,1,4,1,11,2,14,11,5,1,39,0,1,4,1),_HpicfIpLockNotifyCount_Type())
hpicfIpLockNotifyCount.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfIpLockNotifyCount.setStatus(_B)
_HpicfIpLockNotifyPort_Type=InterfaceIndex
_HpicfIpLockNotifyPort_Object=MibScalar
hpicfIpLockNotifyPort=_HpicfIpLockNotifyPort_Object((1,3,6,1,4,1,11,2,14,11,5,1,39,0,1,4,2),_HpicfIpLockNotifyPort_Type())
hpicfIpLockNotifyPort.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfIpLockNotifyPort.setStatus(_B)
_HpicfIpLockNotifySrcIpType_Type=InetAddressType
_HpicfIpLockNotifySrcIpType_Object=MibScalar
hpicfIpLockNotifySrcIpType=_HpicfIpLockNotifySrcIpType_Object((1,3,6,1,4,1,11,2,14,11,5,1,39,0,1,4,3),_HpicfIpLockNotifySrcIpType_Type())
hpicfIpLockNotifySrcIpType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfIpLockNotifySrcIpType.setStatus(_B)
_HpicfIpLockNotifySrcIpAddress_Type=InetAddress
_HpicfIpLockNotifySrcIpAddress_Object=MibScalar
hpicfIpLockNotifySrcIpAddress=_HpicfIpLockNotifySrcIpAddress_Object((1,3,6,1,4,1,11,2,14,11,5,1,39,0,1,4,4),_HpicfIpLockNotifySrcIpAddress_Type())
hpicfIpLockNotifySrcIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfIpLockNotifySrcIpAddress.setStatus(_B)
_HpicfIpLockNotifyDstIpType_Type=InetAddressType
_HpicfIpLockNotifyDstIpType_Object=MibScalar
hpicfIpLockNotifyDstIpType=_HpicfIpLockNotifyDstIpType_Object((1,3,6,1,4,1,11,2,14,11,5,1,39,0,1,4,5),_HpicfIpLockNotifyDstIpType_Type())
hpicfIpLockNotifyDstIpType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfIpLockNotifyDstIpType.setStatus(_B)
_HpicfIpLockNotifyDstIpAddress_Type=InetAddress
_HpicfIpLockNotifyDstIpAddress_Object=MibScalar
hpicfIpLockNotifyDstIpAddress=_HpicfIpLockNotifyDstIpAddress_Object((1,3,6,1,4,1,11,2,14,11,5,1,39,0,1,4,6),_HpicfIpLockNotifyDstIpAddress_Type())
hpicfIpLockNotifyDstIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfIpLockNotifyDstIpAddress.setStatus(_B)
_HpicfIpLockNotifyMacAddress_Type=MacAddress
_HpicfIpLockNotifyMacAddress_Object=MibScalar
hpicfIpLockNotifyMacAddress=_HpicfIpLockNotifyMacAddress_Object((1,3,6,1,4,1,11,2,14,11,5,1,39,0,1,4,7),_HpicfIpLockNotifyMacAddress_Type())
hpicfIpLockNotifyMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfIpLockNotifyMacAddress.setStatus(_B)
_HpicfIpLockNotifyPktCount_Type=Counter32
_HpicfIpLockNotifyPktCount_Object=MibScalar
hpicfIpLockNotifyPktCount=_HpicfIpLockNotifyPktCount_Object((1,3,6,1,4,1,11,2,14,11,5,1,39,0,1,4,8),_HpicfIpLockNotifyPktCount_Type())
hpicfIpLockNotifyPktCount.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfIpLockNotifyPktCount.setStatus(_B)
_HpicfIpLockObjects_ObjectIdentity=ObjectIdentity
hpicfIpLockObjects=_HpicfIpLockObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,39,1))
_HpicfIpLockConfig_ObjectIdentity=ObjectIdentity
hpicfIpLockConfig=_HpicfIpLockConfig_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,39,1,1))
_HpicfIpLockEnable_Type=TruthValue
_HpicfIpLockEnable_Object=MibScalar
hpicfIpLockEnable=_HpicfIpLockEnable_Object((1,3,6,1,4,1,11,2,14,11,5,1,39,1,1,1),_HpicfIpLockEnable_Type())
hpicfIpLockEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:hpicfIpLockEnable.setStatus(_B)
_HpicfIpLockPortTable_Object=MibTable
hpicfIpLockPortTable=_HpicfIpLockPortTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,39,1,1,2))
if mibBuilder.loadTexts:hpicfIpLockPortTable.setStatus(_B)
_HpicfIpLockPortEntry_Object=MibTableRow
hpicfIpLockPortEntry=_HpicfIpLockPortEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,39,1,1,2,1))
hpicfIpLockPortEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:hpicfIpLockPortEntry.setStatus(_B)
_HpicfIpLockPortEnable_Type=TruthValue
_HpicfIpLockPortEnable_Object=MibTableColumn
hpicfIpLockPortEnable=_HpicfIpLockPortEnable_Object((1,3,6,1,4,1,11,2,14,11,5,1,39,1,1,2,1,1),_HpicfIpLockPortEnable_Type())
hpicfIpLockPortEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:hpicfIpLockPortEnable.setStatus(_B)
class _HpicfIpLockTrapCntl_Type(Bits):namedValues=NamedValues(('outOfResource',0))
_HpicfIpLockTrapCntl_Type.__name__=_J
_HpicfIpLockTrapCntl_Object=MibScalar
hpicfIpLockTrapCntl=_HpicfIpLockTrapCntl_Object((1,3,6,1,4,1,11,2,14,11,5,1,39,1,1,3),_HpicfIpLockTrapCntl_Type())
hpicfIpLockTrapCntl.setMaxAccess(_E)
if mibBuilder.loadTexts:hpicfIpLockTrapCntl.setStatus(_Y)
class _HpicfIpLockTrapCtrl_Type(TruthValue):defaultValue=1
_HpicfIpLockTrapCtrl_Type.__name__=_X
_HpicfIpLockTrapCtrl_Object=MibScalar
hpicfIpLockTrapCtrl=_HpicfIpLockTrapCtrl_Object((1,3,6,1,4,1,11,2,14,11,5,1,39,1,1,4),_HpicfIpLockTrapCtrl_Type())
hpicfIpLockTrapCtrl.setMaxAccess(_E)
if mibBuilder.loadTexts:hpicfIpLockTrapCtrl.setStatus(_B)
_HpicfIpLockStatus_ObjectIdentity=ObjectIdentity
hpicfIpLockStatus=_HpicfIpLockStatus_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,39,1,2))
_HpicfIpLockPortStatusTable_Object=MibTable
hpicfIpLockPortStatusTable=_HpicfIpLockPortStatusTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,39,1,2,1))
if mibBuilder.loadTexts:hpicfIpLockPortStatusTable.setStatus(_B)
_HpicfIpLockPortStatusEntry_Object=MibTableRow
hpicfIpLockPortStatusEntry=_HpicfIpLockPortStatusEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,39,1,2,1,1))
hpicfIpLockPortStatusEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:hpicfIpLockPortStatusEntry.setStatus(_B)
class _HpicfIpLockPortOperStatus_Type(Bits):namedValues=NamedValues(*(('active',0),('noDsnoop',1),('trustedPort',2),('noSnoopingVlan',3)))
_HpicfIpLockPortOperStatus_Type.__name__=_J
_HpicfIpLockPortOperStatus_Object=MibTableColumn
hpicfIpLockPortOperStatus=_HpicfIpLockPortOperStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,39,1,2,1,1,1),_HpicfIpLockPortOperStatus_Type())
hpicfIpLockPortOperStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfIpLockPortOperStatus.setStatus(_B)
_HpicfIpLockAddrTable_Object=MibTable
hpicfIpLockAddrTable=_HpicfIpLockAddrTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,39,1,2,2))
if mibBuilder.loadTexts:hpicfIpLockAddrTable.setStatus(_B)
_HpicfIpLockAddrEntry_Object=MibTableRow
hpicfIpLockAddrEntry=_HpicfIpLockAddrEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,39,1,2,2,1))
hpicfIpLockAddrEntry.setIndexNames((0,_A,_F),(0,_A,_K),(0,_A,_G))
if mibBuilder.loadTexts:hpicfIpLockAddrEntry.setStatus(_B)
_HpicfIpLockAddrPort_Type=InterfaceIndex
_HpicfIpLockAddrPort_Object=MibTableColumn
hpicfIpLockAddrPort=_HpicfIpLockAddrPort_Object((1,3,6,1,4,1,11,2,14,11,5,1,39,1,2,2,1,1),_HpicfIpLockAddrPort_Type())
hpicfIpLockAddrPort.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfIpLockAddrPort.setStatus(_B)
_HpicfIpLockAddrType_Type=InetAddressType
_HpicfIpLockAddrType_Object=MibTableColumn
hpicfIpLockAddrType=_HpicfIpLockAddrType_Object((1,3,6,1,4,1,11,2,14,11,5,1,39,1,2,2,1,2),_HpicfIpLockAddrType_Type())
hpicfIpLockAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfIpLockAddrType.setStatus(_B)
_HpicfIpLockAddrIpAddress_Type=InetAddress
_HpicfIpLockAddrIpAddress_Object=MibTableColumn
hpicfIpLockAddrIpAddress=_HpicfIpLockAddrIpAddress_Object((1,3,6,1,4,1,11,2,14,11,5,1,39,1,2,2,1,3),_HpicfIpLockAddrIpAddress_Type())
hpicfIpLockAddrIpAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfIpLockAddrIpAddress.setStatus(_B)
_HpicfIpLockAddrVlan_Type=VlanIndex
_HpicfIpLockAddrVlan_Object=MibTableColumn
hpicfIpLockAddrVlan=_HpicfIpLockAddrVlan_Object((1,3,6,1,4,1,11,2,14,11,5,1,39,1,2,2,1,4),_HpicfIpLockAddrVlan_Type())
hpicfIpLockAddrVlan.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfIpLockAddrVlan.setStatus(_B)
_HpicfIpLockAddrMacAddress_Type=MacAddress
_HpicfIpLockAddrMacAddress_Object=MibTableColumn
hpicfIpLockAddrMacAddress=_HpicfIpLockAddrMacAddress_Object((1,3,6,1,4,1,11,2,14,11,5,1,39,1,2,2,1,5),_HpicfIpLockAddrMacAddress_Type())
hpicfIpLockAddrMacAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfIpLockAddrMacAddress.setStatus(_B)
_HpicfIpLockResourceAvailable_Type=TruthValue
_HpicfIpLockResourceAvailable_Object=MibTableColumn
hpicfIpLockResourceAvailable=_HpicfIpLockResourceAvailable_Object((1,3,6,1,4,1,11,2,14,11,5,1,39,1,2,2,1,6),_HpicfIpLockResourceAvailable_Type())
hpicfIpLockResourceAvailable.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfIpLockResourceAvailable.setStatus(_B)
_HpicfIpLockConformance_ObjectIdentity=ObjectIdentity
hpicfIpLockConformance=_HpicfIpLockConformance_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,39,2))
_HpicfIpLockGroups_ObjectIdentity=ObjectIdentity
hpicfIpLockGroups=_HpicfIpLockGroups_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,39,2,1))
_HpicfIpLockCompliances_ObjectIdentity=ObjectIdentity
hpicfIpLockCompliances=_HpicfIpLockCompliances_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,39,2,2))
hpicfIpLockBaseGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,39,2,1,1))
hpicfIpLockBaseGroup.setObjects(*((_A,_Z),(_A,_a),(_A,_b),(_A,_F),(_A,_K),(_A,_G),(_A,_L),(_A,_M),(_A,_c)))
if mibBuilder.loadTexts:hpicfIpLockBaseGroup.setStatus(_B)
hpicfIpLockTrapObjectsGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,39,2,1,3))
hpicfIpLockTrapObjectsGroup.setObjects(*((_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_d)))
if mibBuilder.loadTexts:hpicfIpLockTrapObjectsGroup.setStatus(_B)
hpicfIpLockObsoleteGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,39,2,1,4))
hpicfIpLockObsoleteGroup.setObjects((_A,_e))
if mibBuilder.loadTexts:hpicfIpLockObsoleteGroup.setStatus(_Y)
hpicfIpLockOutOfResources=NotificationType((1,3,6,1,4,1,11,2,14,11,5,1,39,0,1,2))
hpicfIpLockOutOfResources.setObjects(*((_A,_F),(_A,_M),(_A,_G),(_A,_L),(_A,_N)))
if mibBuilder.loadTexts:hpicfIpLockOutOfResources.setStatus(_B)
hpicfIpLockErrantNotify=NotificationType((1,3,6,1,4,1,11,2,14,11,5,1,39,0,1,3))
hpicfIpLockErrantNotify.setObjects(*((_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V)))
if mibBuilder.loadTexts:hpicfIpLockErrantNotify.setStatus(_B)
hpicfIpLockTrapsGroup=NotificationGroup((1,3,6,1,4,1,11,2,14,11,5,1,39,2,1,2))
hpicfIpLockTrapsGroup.setObjects(*((_A,_f),(_A,_g)))
if mibBuilder.loadTexts:hpicfIpLockTrapsGroup.setStatus(_B)
hpicfIpLockCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,39,2,2,1))
hpicfIpLockCompliance.setObjects((_A,_h))
if mibBuilder.loadTexts:hpicfIpLockCompliance.setStatus(_B)
hpicfIpLockTrapCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,39,2,2,2))
hpicfIpLockTrapCompliance.setObjects(*((_A,_i),(_A,_j)))
if mibBuilder.loadTexts:hpicfIpLockTrapCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'hpicfIpLockdown':hpicfIpLockdown,'hpicfIpLockTraps':hpicfIpLockTraps,'hpicfIpLockTrapsObjects':hpicfIpLockTrapsObjects,_N:hpicfIpLockOutOfResourceSource,_f:hpicfIpLockOutOfResources,_g:hpicfIpLockErrantNotify,'hpicfIpLockErrantNotifyObjects':hpicfIpLockErrantNotifyObjects,_O:hpicfIpLockNotifyCount,_P:hpicfIpLockNotifyPort,_Q:hpicfIpLockNotifySrcIpType,_R:hpicfIpLockNotifySrcIpAddress,_S:hpicfIpLockNotifyDstIpType,_T:hpicfIpLockNotifyDstIpAddress,_U:hpicfIpLockNotifyMacAddress,_V:hpicfIpLockNotifyPktCount,'hpicfIpLockObjects':hpicfIpLockObjects,'hpicfIpLockConfig':hpicfIpLockConfig,_Z:hpicfIpLockEnable,'hpicfIpLockPortTable':hpicfIpLockPortTable,'hpicfIpLockPortEntry':hpicfIpLockPortEntry,_a:hpicfIpLockPortEnable,_e:hpicfIpLockTrapCntl,_d:hpicfIpLockTrapCtrl,'hpicfIpLockStatus':hpicfIpLockStatus,'hpicfIpLockPortStatusTable':hpicfIpLockPortStatusTable,'hpicfIpLockPortStatusEntry':hpicfIpLockPortStatusEntry,_b:hpicfIpLockPortOperStatus,'hpicfIpLockAddrTable':hpicfIpLockAddrTable,'hpicfIpLockAddrEntry':hpicfIpLockAddrEntry,_F:hpicfIpLockAddrPort,_K:hpicfIpLockAddrType,_G:hpicfIpLockAddrIpAddress,_L:hpicfIpLockAddrVlan,_M:hpicfIpLockAddrMacAddress,_c:hpicfIpLockResourceAvailable,'hpicfIpLockConformance':hpicfIpLockConformance,'hpicfIpLockGroups':hpicfIpLockGroups,_h:hpicfIpLockBaseGroup,_j:hpicfIpLockTrapsGroup,_i:hpicfIpLockTrapObjectsGroup,'hpicfIpLockObsoleteGroup':hpicfIpLockObsoleteGroup,'hpicfIpLockCompliances':hpicfIpLockCompliances,'hpicfIpLockCompliance':hpicfIpLockCompliance,'hpicfIpLockTrapCompliance':hpicfIpLockTrapCompliance})