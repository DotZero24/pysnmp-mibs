_g='ciscoHAExceptionNotifGroup'
_f='ciscoHASwitchOverDataGroup'
_e='ciscoHAConfigDataGroup'
_d='carSwitchOverNotification'
_c='carMaxSwitchOverHistoryRecords'
_b='carTotalSwitchOvers'
_a='carLastSwitchOverTime'
_Z='carLastSwitchOverReason'
_Y='carNotificationEnabled'
_X='carRedundancyState'
_W='carRedundancyCheckInterval'
_V='carRedundancySyncInterval'
_U='carPeerAddress'
_T='carPeerAddressType'
_S='carMyAddress'
_R='carMyAddressType'
_Q='carVirtualAddress'
_P='carVirtualAddressType'
_O='carSWHistTableIndex'
_N='not-accessible'
_M='carHAAddrTableIndex'
_L='CarRedundancyState'
_K='TruthValue'
_J='carSWHistEventReason'
_I='carSWHistEventTime'
_H='carSWHistStandbyNodeAddress'
_G='carSWHistStandbyNodeAddressType'
_F='carSWHistActiveNodeAddress'
_E='carSWHistActiveNodeAddressType'
_D='Unsigned32'
_C='read-only'
_B='CISCO-APPLIANCE-REDUNDANCY-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB','InterfaceIndexOrZero')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention,TimeInterval,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention','TimeInterval',_K)
ciscoApplianceRedundancyMIB=ModuleIdentity((1,3,6,1,4,1,9,9,458))
class CarRedundancyState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('notConfigured',1),('starting',2),('active',3),('preStandby',4),('standby',5),('activeLostStandby',6),('activeLostNetwork',7),('standbyLostNetwork',8)))
class CarSwitchOverReason(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('lossConnWithActive',1),('forcedSwitchOver',2),('unknown',3)))
_CiscoApplRedundancyMIBObjects_ObjectIdentity=ObjectIdentity
ciscoApplRedundancyMIBObjects=_CiscoApplRedundancyMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,458,1))
_CarConfigObjects_ObjectIdentity=ObjectIdentity
carConfigObjects=_CarConfigObjects_ObjectIdentity((1,3,6,1,4,1,9,9,458,1,1))
_CarRedundancySyncInterval_Type=TimeInterval
_CarRedundancySyncInterval_Object=MibScalar
carRedundancySyncInterval=_CarRedundancySyncInterval_Object((1,3,6,1,4,1,9,9,458,1,1,1),_CarRedundancySyncInterval_Type())
carRedundancySyncInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:carRedundancySyncInterval.setStatus(_A)
_CarRedundancyCheckInterval_Type=TimeInterval
_CarRedundancyCheckInterval_Object=MibScalar
carRedundancyCheckInterval=_CarRedundancyCheckInterval_Object((1,3,6,1,4,1,9,9,458,1,1,2),_CarRedundancyCheckInterval_Type())
carRedundancyCheckInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:carRedundancyCheckInterval.setStatus(_A)
class _CarRedundancyState_Type(CarRedundancyState):defaultValue=1
_CarRedundancyState_Type.__name__=_L
_CarRedundancyState_Object=MibScalar
carRedundancyState=_CarRedundancyState_Object((1,3,6,1,4,1,9,9,458,1,1,3),_CarRedundancyState_Type())
carRedundancyState.setMaxAccess(_C)
if mibBuilder.loadTexts:carRedundancyState.setStatus(_A)
class _CarNotificationEnabled_Type(TruthValue):defaultValue=2
_CarNotificationEnabled_Type.__name__=_K
_CarNotificationEnabled_Object=MibScalar
carNotificationEnabled=_CarNotificationEnabled_Object((1,3,6,1,4,1,9,9,458,1,1,4),_CarNotificationEnabled_Type())
carNotificationEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:carNotificationEnabled.setStatus(_A)
_CarHAAddressTable_Object=MibTable
carHAAddressTable=_CarHAAddressTable_Object((1,3,6,1,4,1,9,9,458,1,1,5))
if mibBuilder.loadTexts:carHAAddressTable.setStatus(_A)
_CarHAAddressEntry_Object=MibTableRow
carHAAddressEntry=_CarHAAddressEntry_Object((1,3,6,1,4,1,9,9,458,1,1,5,1))
carHAAddressEntry.setIndexNames((0,_B,_M))
if mibBuilder.loadTexts:carHAAddressEntry.setStatus(_A)
_CarHAAddrTableIndex_Type=InterfaceIndexOrZero
_CarHAAddrTableIndex_Object=MibTableColumn
carHAAddrTableIndex=_CarHAAddrTableIndex_Object((1,3,6,1,4,1,9,9,458,1,1,5,1,1),_CarHAAddrTableIndex_Type())
carHAAddrTableIndex.setMaxAccess(_N)
if mibBuilder.loadTexts:carHAAddrTableIndex.setStatus(_A)
_CarVirtualAddressType_Type=InetAddressType
_CarVirtualAddressType_Object=MibTableColumn
carVirtualAddressType=_CarVirtualAddressType_Object((1,3,6,1,4,1,9,9,458,1,1,5,1,2),_CarVirtualAddressType_Type())
carVirtualAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:carVirtualAddressType.setStatus(_A)
_CarVirtualAddress_Type=InetAddress
_CarVirtualAddress_Object=MibTableColumn
carVirtualAddress=_CarVirtualAddress_Object((1,3,6,1,4,1,9,9,458,1,1,5,1,3),_CarVirtualAddress_Type())
carVirtualAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:carVirtualAddress.setStatus(_A)
_CarMyAddressType_Type=InetAddressType
_CarMyAddressType_Object=MibTableColumn
carMyAddressType=_CarMyAddressType_Object((1,3,6,1,4,1,9,9,458,1,1,5,1,4),_CarMyAddressType_Type())
carMyAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:carMyAddressType.setStatus(_A)
_CarMyAddress_Type=InetAddress
_CarMyAddress_Object=MibTableColumn
carMyAddress=_CarMyAddress_Object((1,3,6,1,4,1,9,9,458,1,1,5,1,5),_CarMyAddress_Type())
carMyAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:carMyAddress.setStatus(_A)
_CarPeerAddressType_Type=InetAddressType
_CarPeerAddressType_Object=MibTableColumn
carPeerAddressType=_CarPeerAddressType_Object((1,3,6,1,4,1,9,9,458,1,1,5,1,6),_CarPeerAddressType_Type())
carPeerAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:carPeerAddressType.setStatus(_A)
_CarPeerAddress_Type=InetAddress
_CarPeerAddress_Object=MibTableColumn
carPeerAddress=_CarPeerAddress_Object((1,3,6,1,4,1,9,9,458,1,1,5,1,7),_CarPeerAddress_Type())
carPeerAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:carPeerAddress.setStatus(_A)
_CarSwitchOverObjects_ObjectIdentity=ObjectIdentity
carSwitchOverObjects=_CarSwitchOverObjects_ObjectIdentity((1,3,6,1,4,1,9,9,458,1,2))
_CarLastSwitchOverReason_Type=CarSwitchOverReason
_CarLastSwitchOverReason_Object=MibScalar
carLastSwitchOverReason=_CarLastSwitchOverReason_Object((1,3,6,1,4,1,9,9,458,1,2,1),_CarLastSwitchOverReason_Type())
carLastSwitchOverReason.setMaxAccess(_C)
if mibBuilder.loadTexts:carLastSwitchOverReason.setStatus(_A)
_CarLastSwitchOverTime_Type=DateAndTime
_CarLastSwitchOverTime_Object=MibScalar
carLastSwitchOverTime=_CarLastSwitchOverTime_Object((1,3,6,1,4,1,9,9,458,1,2,2),_CarLastSwitchOverTime_Type())
carLastSwitchOverTime.setMaxAccess(_C)
if mibBuilder.loadTexts:carLastSwitchOverTime.setStatus(_A)
_CarTotalSwitchOvers_Type=Counter32
_CarTotalSwitchOvers_Object=MibScalar
carTotalSwitchOvers=_CarTotalSwitchOvers_Object((1,3,6,1,4,1,9,9,458,1,2,3),_CarTotalSwitchOvers_Type())
carTotalSwitchOvers.setMaxAccess(_C)
if mibBuilder.loadTexts:carTotalSwitchOvers.setStatus(_A)
class _CarMaxSwitchOverHistoryRecords_Type(Unsigned32):defaultValue=20;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1024))
_CarMaxSwitchOverHistoryRecords_Type.__name__=_D
_CarMaxSwitchOverHistoryRecords_Object=MibScalar
carMaxSwitchOverHistoryRecords=_CarMaxSwitchOverHistoryRecords_Object((1,3,6,1,4,1,9,9,458,1,2,4),_CarMaxSwitchOverHistoryRecords_Type())
carMaxSwitchOverHistoryRecords.setMaxAccess(_C)
if mibBuilder.loadTexts:carMaxSwitchOverHistoryRecords.setStatus(_A)
_CarSwitchOverHistoryTable_Object=MibTable
carSwitchOverHistoryTable=_CarSwitchOverHistoryTable_Object((1,3,6,1,4,1,9,9,458,1,2,5))
if mibBuilder.loadTexts:carSwitchOverHistoryTable.setStatus(_A)
_CarSwitchOverHistEntry_Object=MibTableRow
carSwitchOverHistEntry=_CarSwitchOverHistEntry_Object((1,3,6,1,4,1,9,9,458,1,2,5,1))
carSwitchOverHistEntry.setIndexNames((0,_B,_O))
if mibBuilder.loadTexts:carSwitchOverHistEntry.setStatus(_A)
class _CarSWHistTableIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CarSWHistTableIndex_Type.__name__=_D
_CarSWHistTableIndex_Object=MibTableColumn
carSWHistTableIndex=_CarSWHistTableIndex_Object((1,3,6,1,4,1,9,9,458,1,2,5,1,1),_CarSWHistTableIndex_Type())
carSWHistTableIndex.setMaxAccess(_N)
if mibBuilder.loadTexts:carSWHistTableIndex.setStatus(_A)
_CarSWHistActiveNodeAddressType_Type=InetAddressType
_CarSWHistActiveNodeAddressType_Object=MibTableColumn
carSWHistActiveNodeAddressType=_CarSWHistActiveNodeAddressType_Object((1,3,6,1,4,1,9,9,458,1,2,5,1,2),_CarSWHistActiveNodeAddressType_Type())
carSWHistActiveNodeAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:carSWHistActiveNodeAddressType.setStatus(_A)
_CarSWHistActiveNodeAddress_Type=InetAddress
_CarSWHistActiveNodeAddress_Object=MibTableColumn
carSWHistActiveNodeAddress=_CarSWHistActiveNodeAddress_Object((1,3,6,1,4,1,9,9,458,1,2,5,1,3),_CarSWHistActiveNodeAddress_Type())
carSWHistActiveNodeAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:carSWHistActiveNodeAddress.setStatus(_A)
_CarSWHistStandbyNodeAddressType_Type=InetAddressType
_CarSWHistStandbyNodeAddressType_Object=MibTableColumn
carSWHistStandbyNodeAddressType=_CarSWHistStandbyNodeAddressType_Object((1,3,6,1,4,1,9,9,458,1,2,5,1,4),_CarSWHistStandbyNodeAddressType_Type())
carSWHistStandbyNodeAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:carSWHistStandbyNodeAddressType.setStatus(_A)
_CarSWHistStandbyNodeAddress_Type=InetAddress
_CarSWHistStandbyNodeAddress_Object=MibTableColumn
carSWHistStandbyNodeAddress=_CarSWHistStandbyNodeAddress_Object((1,3,6,1,4,1,9,9,458,1,2,5,1,5),_CarSWHistStandbyNodeAddress_Type())
carSWHistStandbyNodeAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:carSWHistStandbyNodeAddress.setStatus(_A)
_CarSWHistEventTime_Type=DateAndTime
_CarSWHistEventTime_Object=MibTableColumn
carSWHistEventTime=_CarSWHistEventTime_Object((1,3,6,1,4,1,9,9,458,1,2,5,1,6),_CarSWHistEventTime_Type())
carSWHistEventTime.setMaxAccess(_C)
if mibBuilder.loadTexts:carSWHistEventTime.setStatus(_A)
_CarSWHistEventReason_Type=CarSwitchOverReason
_CarSWHistEventReason_Object=MibTableColumn
carSWHistEventReason=_CarSWHistEventReason_Object((1,3,6,1,4,1,9,9,458,1,2,5,1,7),_CarSWHistEventReason_Type())
carSWHistEventReason.setMaxAccess(_C)
if mibBuilder.loadTexts:carSWHistEventReason.setStatus(_A)
_CarHAMIBNotifPrefix_ObjectIdentity=ObjectIdentity
carHAMIBNotifPrefix=_CarHAMIBNotifPrefix_ObjectIdentity((1,3,6,1,4,1,9,9,458,2))
_CarHAMIBNotifications_ObjectIdentity=ObjectIdentity
carHAMIBNotifications=_CarHAMIBNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,458,2,0))
_CiscoHAMIBConformance_ObjectIdentity=ObjectIdentity
ciscoHAMIBConformance=_CiscoHAMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,458,3))
_CiscoHAMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoHAMIBCompliances=_CiscoHAMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,458,3,1))
_CiscoHAMIBGroups_ObjectIdentity=ObjectIdentity
ciscoHAMIBGroups=_CiscoHAMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,458,3,2))
ciscoHAConfigDataGroup=ObjectGroup((1,3,6,1,4,1,9,9,458,3,2,1))
ciscoHAConfigDataGroup.setObjects(*((_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y)))
if mibBuilder.loadTexts:ciscoHAConfigDataGroup.setStatus(_A)
ciscoHASwitchOverDataGroup=ObjectGroup((1,3,6,1,4,1,9,9,458,3,2,2))
ciscoHASwitchOverDataGroup.setObjects(*((_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_E),(_B,_F),(_B,_G),(_B,_H),(_B,_I),(_B,_J)))
if mibBuilder.loadTexts:ciscoHASwitchOverDataGroup.setStatus(_A)
carSwitchOverNotification=NotificationType((1,3,6,1,4,1,9,9,458,2,0,1))
carSwitchOverNotification.setObjects(*((_B,_I),(_B,_J),(_B,_E),(_B,_F),(_B,_G),(_B,_H)))
if mibBuilder.loadTexts:carSwitchOverNotification.setStatus(_A)
ciscoHAExceptionNotifGroup=NotificationGroup((1,3,6,1,4,1,9,9,458,3,2,3))
ciscoHAExceptionNotifGroup.setObjects((_B,_d))
if mibBuilder.loadTexts:ciscoHAExceptionNotifGroup.setStatus(_A)
ciscoHAMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,458,3,1,1))
ciscoHAMIBCompliance.setObjects(*((_B,_e),(_B,_f),(_B,_g)))
if mibBuilder.loadTexts:ciscoHAMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_L:CarRedundancyState,'CarSwitchOverReason':CarSwitchOverReason,'ciscoApplianceRedundancyMIB':ciscoApplianceRedundancyMIB,'ciscoApplRedundancyMIBObjects':ciscoApplRedundancyMIBObjects,'carConfigObjects':carConfigObjects,_V:carRedundancySyncInterval,_W:carRedundancyCheckInterval,_X:carRedundancyState,_Y:carNotificationEnabled,'carHAAddressTable':carHAAddressTable,'carHAAddressEntry':carHAAddressEntry,_M:carHAAddrTableIndex,_P:carVirtualAddressType,_Q:carVirtualAddress,_R:carMyAddressType,_S:carMyAddress,_T:carPeerAddressType,_U:carPeerAddress,'carSwitchOverObjects':carSwitchOverObjects,_Z:carLastSwitchOverReason,_a:carLastSwitchOverTime,_b:carTotalSwitchOvers,_c:carMaxSwitchOverHistoryRecords,'carSwitchOverHistoryTable':carSwitchOverHistoryTable,'carSwitchOverHistEntry':carSwitchOverHistEntry,_O:carSWHistTableIndex,_E:carSWHistActiveNodeAddressType,_F:carSWHistActiveNodeAddress,_G:carSWHistStandbyNodeAddressType,_H:carSWHistStandbyNodeAddress,_I:carSWHistEventTime,_J:carSWHistEventReason,'carHAMIBNotifPrefix':carHAMIBNotifPrefix,'carHAMIBNotifications':carHAMIBNotifications,_d:carSwitchOverNotification,'ciscoHAMIBConformance':ciscoHAMIBConformance,'ciscoHAMIBCompliances':ciscoHAMIBCompliances,'ciscoHAMIBCompliance':ciscoHAMIBCompliance,'ciscoHAMIBGroups':ciscoHAMIBGroups,_e:ciscoHAConfigDataGroup,_f:ciscoHASwitchOverDataGroup,_g:ciscoHAExceptionNotifGroup})