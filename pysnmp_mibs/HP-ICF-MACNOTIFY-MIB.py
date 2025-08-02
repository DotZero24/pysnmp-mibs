_q='hpicfMacNotifyStatsGroup2'
_p='hpicfMacNotifyConfigGroup2'
_o='hpicfMacCountNotifyNotifications'
_n='hpicfMacCountNotifyConfigGroup'
_m='hpicfMacNotifyStatsGroup'
_l='hpicfMacNotifyConfigGroup'
_k='hpicfMacNotifyPortMacAddressCount'
_j='hpicfMacNotifyMacAddressTableChange'
_i='hpicfMacNotifyAgedPortConfig'
_h='hpicfMacNotifyAgedCount'
_g='hpicfMacNotifyPortLearnedCountConfig'
_f='hpicfMacNotifyPortLearnedCountEnable'
_e='hpicfMacNotifyClearMacTableOnVlan'
_d='hpicfMacNotifyClearMacTableOnPorts'
_c='hpicfMacNotifyPortIndex'
_b='hpicfMacNotifyClearGroup'
_a='hpicfMacNotifyNotifications'
_Z='hpicfMacNotifyGlobalConfigGroup'
_Y='hpicfMacNotifyPortLearnedCount'
_X='hpicfMacNotifyCount'
_W='hpicfMacNotifyMoveCount'
_V='hpicfMacNotifyRemovedCount'
_U='hpicfMacNotifyLearnedCount'
_T='deprecated'
_S='hpicfMacNotifyRemovedPortConfig'
_R='hpicfMacNotifyLearnedPortConfig'
_Q='disable'
_P='enable'
_O='Unsigned32'
_N='hpicfMacNotifyFromPortId'
_M='hpicfMacNotifyAction'
_L='hpicfMacNotifyMoveEnable'
_K='hpicfMacNotifyTrapInterval'
_J='hpicfMacNotifyEnable'
_I='hpicfMacNotifyVlanId'
_H='hpicfMacNotifyToPortId'
_G='hpicfMacNotifyMacAddress'
_F='read-only'
_E='accessible-for-notify'
_D='Integer32'
_C='read-write'
_B='current'
_A='HP-ICF-MACNOTIFY-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpSwitch,=mibBuilder.importSymbols('HP-ICF-OID','hpSwitch')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
PortList,VlanId=mibBuilder.importSymbols('Q-BRIDGE-MIB','PortList','VlanId')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_O,'iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
hpicfMacNotifyMIB=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,5,1,66))
if mibBuilder.loadTexts:hpicfMacNotifyMIB.setRevisions(('2013-07-18 00:00','2011-07-21 00:00','2010-02-08 00:00','2009-12-11 10:00'))
_HpicfMacNotifyNotificationObjects_ObjectIdentity=ObjectIdentity
hpicfMacNotifyNotificationObjects=_HpicfMacNotifyNotificationObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,66,0))
_HpicfMacNotifyConfigObjects_ObjectIdentity=ObjectIdentity
hpicfMacNotifyConfigObjects=_HpicfMacNotifyConfigObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,66,1))
class _HpicfMacNotifyEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_Q,2)))
_HpicfMacNotifyEnable_Type.__name__=_D
_HpicfMacNotifyEnable_Object=MibScalar
hpicfMacNotifyEnable=_HpicfMacNotifyEnable_Object((1,3,6,1,4,1,11,2,14,11,5,1,66,1,1),_HpicfMacNotifyEnable_Type())
hpicfMacNotifyEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfMacNotifyEnable.setStatus(_B)
class _HpicfMacNotifyTrapInterval_Type(Unsigned32):defaultValue=30
_HpicfMacNotifyTrapInterval_Type.__name__=_O
_HpicfMacNotifyTrapInterval_Object=MibScalar
hpicfMacNotifyTrapInterval=_HpicfMacNotifyTrapInterval_Object((1,3,6,1,4,1,11,2,14,11,5,1,66,1,2),_HpicfMacNotifyTrapInterval_Type())
hpicfMacNotifyTrapInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfMacNotifyTrapInterval.setStatus(_B)
if mibBuilder.loadTexts:hpicfMacNotifyTrapInterval.setUnits('Seconds')
class _HpicfMacNotifyMoveEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_Q,2)))
_HpicfMacNotifyMoveEnable_Type.__name__=_D
_HpicfMacNotifyMoveEnable_Object=MibScalar
hpicfMacNotifyMoveEnable=_HpicfMacNotifyMoveEnable_Object((1,3,6,1,4,1,11,2,14,11,5,1,66,1,3),_HpicfMacNotifyMoveEnable_Type())
hpicfMacNotifyMoveEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfMacNotifyMoveEnable.setStatus(_B)
_HpicfMacNotifyLearnedPortConfig_Type=PortList
_HpicfMacNotifyLearnedPortConfig_Object=MibScalar
hpicfMacNotifyLearnedPortConfig=_HpicfMacNotifyLearnedPortConfig_Object((1,3,6,1,4,1,11,2,14,11,5,1,66,1,4),_HpicfMacNotifyLearnedPortConfig_Type())
hpicfMacNotifyLearnedPortConfig.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfMacNotifyLearnedPortConfig.setStatus(_B)
_HpicfMacNotifyRemovedPortConfig_Type=PortList
_HpicfMacNotifyRemovedPortConfig_Object=MibScalar
hpicfMacNotifyRemovedPortConfig=_HpicfMacNotifyRemovedPortConfig_Object((1,3,6,1,4,1,11,2,14,11,5,1,66,1,5),_HpicfMacNotifyRemovedPortConfig_Type())
hpicfMacNotifyRemovedPortConfig.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfMacNotifyRemovedPortConfig.setStatus(_B)
class _HpicfMacNotifyAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('learned',1),('moved',2),('removed',3),('aged',4)))
_HpicfMacNotifyAction_Type.__name__=_D
_HpicfMacNotifyAction_Object=MibScalar
hpicfMacNotifyAction=_HpicfMacNotifyAction_Object((1,3,6,1,4,1,11,2,14,11,5,1,66,1,6),_HpicfMacNotifyAction_Type())
hpicfMacNotifyAction.setMaxAccess(_E)
if mibBuilder.loadTexts:hpicfMacNotifyAction.setStatus(_B)
_HpicfMacNotifyMacAddress_Type=MacAddress
_HpicfMacNotifyMacAddress_Object=MibScalar
hpicfMacNotifyMacAddress=_HpicfMacNotifyMacAddress_Object((1,3,6,1,4,1,11,2,14,11,5,1,66,1,7),_HpicfMacNotifyMacAddress_Type())
hpicfMacNotifyMacAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:hpicfMacNotifyMacAddress.setStatus(_B)
_HpicfMacNotifyFromPortId_Type=Integer32
_HpicfMacNotifyFromPortId_Object=MibScalar
hpicfMacNotifyFromPortId=_HpicfMacNotifyFromPortId_Object((1,3,6,1,4,1,11,2,14,11,5,1,66,1,8),_HpicfMacNotifyFromPortId_Type())
hpicfMacNotifyFromPortId.setMaxAccess(_E)
if mibBuilder.loadTexts:hpicfMacNotifyFromPortId.setStatus(_B)
_HpicfMacNotifyToPortId_Type=Integer32
_HpicfMacNotifyToPortId_Object=MibScalar
hpicfMacNotifyToPortId=_HpicfMacNotifyToPortId_Object((1,3,6,1,4,1,11,2,14,11,5,1,66,1,9),_HpicfMacNotifyToPortId_Type())
hpicfMacNotifyToPortId.setMaxAccess(_E)
if mibBuilder.loadTexts:hpicfMacNotifyToPortId.setStatus(_B)
_HpicfMacNotifyVlanId_Type=Integer32
_HpicfMacNotifyVlanId_Object=MibScalar
hpicfMacNotifyVlanId=_HpicfMacNotifyVlanId_Object((1,3,6,1,4,1,11,2,14,11,5,1,66,1,10),_HpicfMacNotifyVlanId_Type())
hpicfMacNotifyVlanId.setMaxAccess(_E)
if mibBuilder.loadTexts:hpicfMacNotifyVlanId.setStatus(_B)
_HpicfMacNotifyAgedPortConfig_Type=PortList
_HpicfMacNotifyAgedPortConfig_Object=MibScalar
hpicfMacNotifyAgedPortConfig=_HpicfMacNotifyAgedPortConfig_Object((1,3,6,1,4,1,11,2,14,11,5,1,66,1,11),_HpicfMacNotifyAgedPortConfig_Type())
hpicfMacNotifyAgedPortConfig.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfMacNotifyAgedPortConfig.setStatus(_B)
_HpicfMacNotifyStats_ObjectIdentity=ObjectIdentity
hpicfMacNotifyStats=_HpicfMacNotifyStats_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,66,2))
_HpicfMacNotifyLearnedCount_Type=Counter32
_HpicfMacNotifyLearnedCount_Object=MibScalar
hpicfMacNotifyLearnedCount=_HpicfMacNotifyLearnedCount_Object((1,3,6,1,4,1,11,2,14,11,5,1,66,2,1),_HpicfMacNotifyLearnedCount_Type())
hpicfMacNotifyLearnedCount.setMaxAccess(_F)
if mibBuilder.loadTexts:hpicfMacNotifyLearnedCount.setStatus(_B)
_HpicfMacNotifyRemovedCount_Type=Counter32
_HpicfMacNotifyRemovedCount_Object=MibScalar
hpicfMacNotifyRemovedCount=_HpicfMacNotifyRemovedCount_Object((1,3,6,1,4,1,11,2,14,11,5,1,66,2,2),_HpicfMacNotifyRemovedCount_Type())
hpicfMacNotifyRemovedCount.setMaxAccess(_F)
if mibBuilder.loadTexts:hpicfMacNotifyRemovedCount.setStatus(_B)
_HpicfMacNotifyMoveCount_Type=Counter32
_HpicfMacNotifyMoveCount_Object=MibScalar
hpicfMacNotifyMoveCount=_HpicfMacNotifyMoveCount_Object((1,3,6,1,4,1,11,2,14,11,5,1,66,2,3),_HpicfMacNotifyMoveCount_Type())
hpicfMacNotifyMoveCount.setMaxAccess(_F)
if mibBuilder.loadTexts:hpicfMacNotifyMoveCount.setStatus(_B)
_HpicfMacNotifyCount_Type=Counter32
_HpicfMacNotifyCount_Object=MibScalar
hpicfMacNotifyCount=_HpicfMacNotifyCount_Object((1,3,6,1,4,1,11,2,14,11,5,1,66,2,4),_HpicfMacNotifyCount_Type())
hpicfMacNotifyCount.setMaxAccess(_F)
if mibBuilder.loadTexts:hpicfMacNotifyCount.setStatus(_B)
_HpicfMacNotifyAgedCount_Type=Counter32
_HpicfMacNotifyAgedCount_Object=MibScalar
hpicfMacNotifyAgedCount=_HpicfMacNotifyAgedCount_Object((1,3,6,1,4,1,11,2,14,11,5,1,66,2,5),_HpicfMacNotifyAgedCount_Type())
hpicfMacNotifyAgedCount.setMaxAccess(_F)
if mibBuilder.loadTexts:hpicfMacNotifyAgedCount.setStatus(_B)
_HpicfMacNotifyConformance_ObjectIdentity=ObjectIdentity
hpicfMacNotifyConformance=_HpicfMacNotifyConformance_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,66,3))
_HpicfMacNotifyCompliances_ObjectIdentity=ObjectIdentity
hpicfMacNotifyCompliances=_HpicfMacNotifyCompliances_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,66,3,1))
_HpicfMacNotifyGroups_ObjectIdentity=ObjectIdentity
hpicfMacNotifyGroups=_HpicfMacNotifyGroups_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,66,3,2))
_HpicfMacNotifyClearObjects_ObjectIdentity=ObjectIdentity
hpicfMacNotifyClearObjects=_HpicfMacNotifyClearObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,66,4))
_HpicfMacNotifyClearMacTableOnPorts_Type=PortList
_HpicfMacNotifyClearMacTableOnPorts_Object=MibScalar
hpicfMacNotifyClearMacTableOnPorts=_HpicfMacNotifyClearMacTableOnPorts_Object((1,3,6,1,4,1,11,2,14,11,5,1,66,4,1),_HpicfMacNotifyClearMacTableOnPorts_Type())
hpicfMacNotifyClearMacTableOnPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfMacNotifyClearMacTableOnPorts.setStatus(_B)
_HpicfMacNotifyClearMacTableOnVlan_Type=VlanId
_HpicfMacNotifyClearMacTableOnVlan_Object=MibScalar
hpicfMacNotifyClearMacTableOnVlan=_HpicfMacNotifyClearMacTableOnVlan_Object((1,3,6,1,4,1,11,2,14,11,5,1,66,4,2),_HpicfMacNotifyClearMacTableOnVlan_Type())
hpicfMacNotifyClearMacTableOnVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfMacNotifyClearMacTableOnVlan.setStatus(_B)
_HpicfMacCountNotifyConfigObjects_ObjectIdentity=ObjectIdentity
hpicfMacCountNotifyConfigObjects=_HpicfMacCountNotifyConfigObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,66,5))
class _HpicfMacNotifyPortLearnedCountEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_Q,2)))
_HpicfMacNotifyPortLearnedCountEnable_Type.__name__=_D
_HpicfMacNotifyPortLearnedCountEnable_Object=MibScalar
hpicfMacNotifyPortLearnedCountEnable=_HpicfMacNotifyPortLearnedCountEnable_Object((1,3,6,1,4,1,11,2,14,11,5,1,66,5,1),_HpicfMacNotifyPortLearnedCountEnable_Type())
hpicfMacNotifyPortLearnedCountEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfMacNotifyPortLearnedCountEnable.setStatus(_B)
_HpicfMacNotifyPortLearnedCountConfig_Type=PortList
_HpicfMacNotifyPortLearnedCountConfig_Object=MibScalar
hpicfMacNotifyPortLearnedCountConfig=_HpicfMacNotifyPortLearnedCountConfig_Object((1,3,6,1,4,1,11,2,14,11,5,1,66,5,2),_HpicfMacNotifyPortLearnedCountConfig_Type())
hpicfMacNotifyPortLearnedCountConfig.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfMacNotifyPortLearnedCountConfig.setStatus(_B)
_HpicfMacNotifyPortLearnedCountConfigTable_Object=MibTable
hpicfMacNotifyPortLearnedCountConfigTable=_HpicfMacNotifyPortLearnedCountConfigTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,66,5,3))
if mibBuilder.loadTexts:hpicfMacNotifyPortLearnedCountConfigTable.setStatus(_B)
_HpicfMacNotifyPortLearnedCountConfigEntry_Object=MibTableRow
hpicfMacNotifyPortLearnedCountConfigEntry=_HpicfMacNotifyPortLearnedCountConfigEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,66,5,3,1))
hpicfMacNotifyPortLearnedCountConfigEntry.setIndexNames((0,_A,_c))
if mibBuilder.loadTexts:hpicfMacNotifyPortLearnedCountConfigEntry.setStatus(_B)
_HpicfMacNotifyPortIndex_Type=InterfaceIndex
_HpicfMacNotifyPortIndex_Object=MibTableColumn
hpicfMacNotifyPortIndex=_HpicfMacNotifyPortIndex_Object((1,3,6,1,4,1,11,2,14,11,5,1,66,5,3,1,1),_HpicfMacNotifyPortIndex_Type())
hpicfMacNotifyPortIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:hpicfMacNotifyPortIndex.setStatus(_B)
class _HpicfMacNotifyPortLearnedCount_Type(Unsigned32):defaultValue=32;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_HpicfMacNotifyPortLearnedCount_Type.__name__=_O
_HpicfMacNotifyPortLearnedCount_Object=MibTableColumn
hpicfMacNotifyPortLearnedCount=_HpicfMacNotifyPortLearnedCount_Object((1,3,6,1,4,1,11,2,14,11,5,1,66,5,3,1,2),_HpicfMacNotifyPortLearnedCount_Type())
hpicfMacNotifyPortLearnedCount.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfMacNotifyPortLearnedCount.setStatus(_B)
hpicfMacNotifyGlobalConfigGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,66,3,2,1))
hpicfMacNotifyGlobalConfigGroup.setObjects(*((_A,_J),(_A,_K),(_A,_L)))
if mibBuilder.loadTexts:hpicfMacNotifyGlobalConfigGroup.setStatus(_B)
hpicfMacNotifyConfigGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,66,3,2,2))
hpicfMacNotifyConfigGroup.setObjects(*((_A,_J),(_A,_K),(_A,_L),(_A,_R),(_A,_S),(_A,_M),(_A,_G),(_A,_N),(_A,_H),(_A,_I)))
if mibBuilder.loadTexts:hpicfMacNotifyConfigGroup.setStatus(_T)
hpicfMacNotifyStatsGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,66,3,2,3))
hpicfMacNotifyStatsGroup.setObjects(*((_A,_U),(_A,_V),(_A,_W),(_A,_X)))
if mibBuilder.loadTexts:hpicfMacNotifyStatsGroup.setStatus(_T)
hpicfMacNotifyClearGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,66,3,2,5))
hpicfMacNotifyClearGroup.setObjects(*((_A,_d),(_A,_e)))
if mibBuilder.loadTexts:hpicfMacNotifyClearGroup.setStatus(_B)
hpicfMacCountNotifyConfigGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,66,3,2,6))
hpicfMacCountNotifyConfigGroup.setObjects(*((_A,_f),(_A,_g),(_A,_Y)))
if mibBuilder.loadTexts:hpicfMacCountNotifyConfigGroup.setStatus(_B)
hpicfMacNotifyStatsGroup2=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,66,3,2,8))
hpicfMacNotifyStatsGroup2.setObjects(*((_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_h)))
if mibBuilder.loadTexts:hpicfMacNotifyStatsGroup2.setStatus(_B)
hpicfMacNotifyConfigGroup2=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,66,3,2,9))
hpicfMacNotifyConfigGroup2.setObjects(*((_A,_J),(_A,_K),(_A,_L),(_A,_R),(_A,_S),(_A,_M),(_A,_G),(_A,_N),(_A,_H),(_A,_I),(_A,_i)))
if mibBuilder.loadTexts:hpicfMacNotifyConfigGroup2.setStatus(_B)
hpicfMacNotifyMacAddressTableChange=NotificationType((1,3,6,1,4,1,11,2,14,11,5,1,66,0,1))
hpicfMacNotifyMacAddressTableChange.setObjects(*((_A,_M),(_A,_G),(_A,_N),(_A,_H),(_A,_I)))
if mibBuilder.loadTexts:hpicfMacNotifyMacAddressTableChange.setStatus(_B)
hpicfMacNotifyPortMacAddressCount=NotificationType((1,3,6,1,4,1,11,2,14,11,5,1,66,0,2))
hpicfMacNotifyPortMacAddressCount.setObjects(*((_A,_H),(_A,_I),(_A,_Y),(_A,_G)))
if mibBuilder.loadTexts:hpicfMacNotifyPortMacAddressCount.setStatus(_B)
hpicfMacNotifyNotifications=NotificationGroup((1,3,6,1,4,1,11,2,14,11,5,1,66,3,2,4))
hpicfMacNotifyNotifications.setObjects((_A,_j))
if mibBuilder.loadTexts:hpicfMacNotifyNotifications.setStatus(_B)
hpicfMacCountNotifyNotifications=NotificationGroup((1,3,6,1,4,1,11,2,14,11,5,1,66,3,2,7))
hpicfMacCountNotifyNotifications.setObjects((_A,_k))
if mibBuilder.loadTexts:hpicfMacCountNotifyNotifications.setStatus(_B)
hpicfMacNotifyCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,66,3,1,1))
hpicfMacNotifyCompliance.setObjects(*((_A,_Z),(_A,_l),(_A,_m),(_A,_a),(_A,_b)))
if mibBuilder.loadTexts:hpicfMacNotifyCompliance.setStatus(_T)
hpicfMacCountNotifyCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,66,3,1,2))
hpicfMacCountNotifyCompliance.setObjects(*((_A,_n),(_A,_o)))
if mibBuilder.loadTexts:hpicfMacCountNotifyCompliance.setStatus(_B)
hpicfMacNotifyCompliance2=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,66,3,1,3))
hpicfMacNotifyCompliance2.setObjects(*((_A,_Z),(_A,_p),(_A,_q),(_A,_a),(_A,_b)))
if mibBuilder.loadTexts:hpicfMacNotifyCompliance2.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'hpicfMacNotifyMIB':hpicfMacNotifyMIB,'hpicfMacNotifyNotificationObjects':hpicfMacNotifyNotificationObjects,_j:hpicfMacNotifyMacAddressTableChange,_k:hpicfMacNotifyPortMacAddressCount,'hpicfMacNotifyConfigObjects':hpicfMacNotifyConfigObjects,_J:hpicfMacNotifyEnable,_K:hpicfMacNotifyTrapInterval,_L:hpicfMacNotifyMoveEnable,_R:hpicfMacNotifyLearnedPortConfig,_S:hpicfMacNotifyRemovedPortConfig,_M:hpicfMacNotifyAction,_G:hpicfMacNotifyMacAddress,_N:hpicfMacNotifyFromPortId,_H:hpicfMacNotifyToPortId,_I:hpicfMacNotifyVlanId,_i:hpicfMacNotifyAgedPortConfig,'hpicfMacNotifyStats':hpicfMacNotifyStats,_U:hpicfMacNotifyLearnedCount,_V:hpicfMacNotifyRemovedCount,_W:hpicfMacNotifyMoveCount,_X:hpicfMacNotifyCount,_h:hpicfMacNotifyAgedCount,'hpicfMacNotifyConformance':hpicfMacNotifyConformance,'hpicfMacNotifyCompliances':hpicfMacNotifyCompliances,'hpicfMacNotifyCompliance':hpicfMacNotifyCompliance,'hpicfMacCountNotifyCompliance':hpicfMacCountNotifyCompliance,'hpicfMacNotifyCompliance2':hpicfMacNotifyCompliance2,'hpicfMacNotifyGroups':hpicfMacNotifyGroups,_Z:hpicfMacNotifyGlobalConfigGroup,_l:hpicfMacNotifyConfigGroup,_m:hpicfMacNotifyStatsGroup,_a:hpicfMacNotifyNotifications,_b:hpicfMacNotifyClearGroup,_n:hpicfMacCountNotifyConfigGroup,_o:hpicfMacCountNotifyNotifications,_q:hpicfMacNotifyStatsGroup2,_p:hpicfMacNotifyConfigGroup2,'hpicfMacNotifyClearObjects':hpicfMacNotifyClearObjects,_d:hpicfMacNotifyClearMacTableOnPorts,_e:hpicfMacNotifyClearMacTableOnVlan,'hpicfMacCountNotifyConfigObjects':hpicfMacCountNotifyConfigObjects,_f:hpicfMacNotifyPortLearnedCountEnable,_g:hpicfMacNotifyPortLearnedCountConfig,'hpicfMacNotifyPortLearnedCountConfigTable':hpicfMacNotifyPortLearnedCountConfigTable,'hpicfMacNotifyPortLearnedCountConfigEntry':hpicfMacNotifyPortLearnedCountConfigEntry,_c:hpicfMacNotifyPortIndex,_Y:hpicfMacNotifyPortLearnedCount})