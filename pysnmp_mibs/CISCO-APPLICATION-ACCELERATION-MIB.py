_h='caaMIBNotifObjectGroup'
_g='caaMIBNotificationsGroup'
_f='caaMIBStatsGroup'
_e='caaStateChange'
_d='caaStateChangeNotifEnabled'
_c='caaDeltaAbandons'
_b='caaRequestSize'
_a='caaDirectRequests'
_Z='caaIMSMisses'
_Y='caaIMSHits'
_X='caaRefreshHits'
_W='caaStaticObjectMissSize'
_V='caaStaticObjectMisses'
_U='caaStaticObjectHitSize'
_T='caaStaticObjectHits'
_S='caaTransformedObjectIMSRequests'
_R='caaTransformedObjectRequests'
_Q='caaUntransformed'
_P='caaTransformed'
_O='caaLastRestartedTime'
_N='caaFinalResponseSize'
_M='caaRequestedObjectSize'
_L='caaNoncondensableRequests'
_K='caaRequests'
_J='transformations'
_I='caaPort'
_H='TruthValue'
_G='InetPortNumber'
_F='caaState'
_E='bytes'
_D='requests'
_C='read-only'
_B='CISCO-APPLICATION-ACCELERATION-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
InetPortNumber,=mibBuilder.importSymbols('INET-ADDRESS-MIB',_G)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention',_H)
ciscoApplicationAccelerationMIB=ModuleIdentity((1,3,6,1,4,1,9,9,594))
if mibBuilder.loadTexts:ciscoApplicationAccelerationMIB.setRevisions(('2006-10-30 00:00',))
class CaaState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('active',1),('impaired',2),('down',3)))
_CaaMIBNotifications_ObjectIdentity=ObjectIdentity
caaMIBNotifications=_CaaMIBNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,594,0))
_CaaMIBObjects_ObjectIdentity=ObjectIdentity
caaMIBObjects=_CaaMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,594,1))
_CaaStats_ObjectIdentity=ObjectIdentity
caaStats=_CaaStats_ObjectIdentity((1,3,6,1,4,1,9,9,594,1,1))
_CaaStatTable_Object=MibTable
caaStatTable=_CaaStatTable_Object((1,3,6,1,4,1,9,9,594,1,1,1))
if mibBuilder.loadTexts:caaStatTable.setStatus(_A)
_CaaStatEntry_Object=MibTableRow
caaStatEntry=_CaaStatEntry_Object((1,3,6,1,4,1,9,9,594,1,1,1,1))
caaStatEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:caaStatEntry.setStatus(_A)
class _CaaPort_Type(InetPortNumber):subtypeSpec=InetPortNumber.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CaaPort_Type.__name__=_G
_CaaPort_Object=MibTableColumn
caaPort=_CaaPort_Object((1,3,6,1,4,1,9,9,594,1,1,1,1,1),_CaaPort_Type())
caaPort.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:caaPort.setStatus(_A)
_CaaState_Type=CaaState
_CaaState_Object=MibTableColumn
caaState=_CaaState_Object((1,3,6,1,4,1,9,9,594,1,1,1,1,2),_CaaState_Type())
caaState.setMaxAccess(_C)
if mibBuilder.loadTexts:caaState.setStatus(_A)
_CaaRequests_Type=Counter32
_CaaRequests_Object=MibTableColumn
caaRequests=_CaaRequests_Object((1,3,6,1,4,1,9,9,594,1,1,1,1,3),_CaaRequests_Type())
caaRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:caaRequests.setStatus(_A)
if mibBuilder.loadTexts:caaRequests.setUnits(_D)
_CaaNoncondensableRequests_Type=Counter32
_CaaNoncondensableRequests_Object=MibTableColumn
caaNoncondensableRequests=_CaaNoncondensableRequests_Object((1,3,6,1,4,1,9,9,594,1,1,1,1,4),_CaaNoncondensableRequests_Type())
caaNoncondensableRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:caaNoncondensableRequests.setStatus(_A)
if mibBuilder.loadTexts:caaNoncondensableRequests.setUnits(_D)
_CaaRequestedObjectSize_Type=Counter32
_CaaRequestedObjectSize_Object=MibTableColumn
caaRequestedObjectSize=_CaaRequestedObjectSize_Object((1,3,6,1,4,1,9,9,594,1,1,1,1,5),_CaaRequestedObjectSize_Type())
caaRequestedObjectSize.setMaxAccess(_C)
if mibBuilder.loadTexts:caaRequestedObjectSize.setStatus(_A)
if mibBuilder.loadTexts:caaRequestedObjectSize.setUnits(_E)
_CaaFinalResponseSize_Type=Counter32
_CaaFinalResponseSize_Object=MibTableColumn
caaFinalResponseSize=_CaaFinalResponseSize_Object((1,3,6,1,4,1,9,9,594,1,1,1,1,6),_CaaFinalResponseSize_Type())
caaFinalResponseSize.setMaxAccess(_C)
if mibBuilder.loadTexts:caaFinalResponseSize.setStatus(_A)
if mibBuilder.loadTexts:caaFinalResponseSize.setUnits(_E)
_CaaLastRestartedTime_Type=DateAndTime
_CaaLastRestartedTime_Object=MibTableColumn
caaLastRestartedTime=_CaaLastRestartedTime_Object((1,3,6,1,4,1,9,9,594,1,1,1,1,7),_CaaLastRestartedTime_Type())
caaLastRestartedTime.setMaxAccess(_C)
if mibBuilder.loadTexts:caaLastRestartedTime.setStatus(_A)
_CaaTransformed_Type=Counter32
_CaaTransformed_Object=MibTableColumn
caaTransformed=_CaaTransformed_Object((1,3,6,1,4,1,9,9,594,1,1,1,1,8),_CaaTransformed_Type())
caaTransformed.setMaxAccess(_C)
if mibBuilder.loadTexts:caaTransformed.setStatus(_A)
if mibBuilder.loadTexts:caaTransformed.setUnits(_J)
_CaaUntransformed_Type=Counter32
_CaaUntransformed_Object=MibTableColumn
caaUntransformed=_CaaUntransformed_Object((1,3,6,1,4,1,9,9,594,1,1,1,1,9),_CaaUntransformed_Type())
caaUntransformed.setMaxAccess(_C)
if mibBuilder.loadTexts:caaUntransformed.setStatus(_A)
if mibBuilder.loadTexts:caaUntransformed.setUnits(_J)
_CaaTransformedObjectRequests_Type=Counter32
_CaaTransformedObjectRequests_Object=MibTableColumn
caaTransformedObjectRequests=_CaaTransformedObjectRequests_Object((1,3,6,1,4,1,9,9,594,1,1,1,1,10),_CaaTransformedObjectRequests_Type())
caaTransformedObjectRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:caaTransformedObjectRequests.setStatus(_A)
if mibBuilder.loadTexts:caaTransformedObjectRequests.setUnits(_D)
_CaaTransformedObjectIMSRequests_Type=Counter32
_CaaTransformedObjectIMSRequests_Object=MibTableColumn
caaTransformedObjectIMSRequests=_CaaTransformedObjectIMSRequests_Object((1,3,6,1,4,1,9,9,594,1,1,1,1,11),_CaaTransformedObjectIMSRequests_Type())
caaTransformedObjectIMSRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:caaTransformedObjectIMSRequests.setStatus(_A)
if mibBuilder.loadTexts:caaTransformedObjectIMSRequests.setUnits(_D)
_CaaStaticObjectHits_Type=Counter32
_CaaStaticObjectHits_Object=MibTableColumn
caaStaticObjectHits=_CaaStaticObjectHits_Object((1,3,6,1,4,1,9,9,594,1,1,1,1,12),_CaaStaticObjectHits_Type())
caaStaticObjectHits.setMaxAccess(_C)
if mibBuilder.loadTexts:caaStaticObjectHits.setStatus(_A)
if mibBuilder.loadTexts:caaStaticObjectHits.setUnits('cache-hits')
_CaaStaticObjectHitSize_Type=Counter32
_CaaStaticObjectHitSize_Object=MibTableColumn
caaStaticObjectHitSize=_CaaStaticObjectHitSize_Object((1,3,6,1,4,1,9,9,594,1,1,1,1,13),_CaaStaticObjectHitSize_Type())
caaStaticObjectHitSize.setMaxAccess(_C)
if mibBuilder.loadTexts:caaStaticObjectHitSize.setStatus(_A)
if mibBuilder.loadTexts:caaStaticObjectHitSize.setUnits(_E)
_CaaStaticObjectMisses_Type=Counter32
_CaaStaticObjectMisses_Object=MibTableColumn
caaStaticObjectMisses=_CaaStaticObjectMisses_Object((1,3,6,1,4,1,9,9,594,1,1,1,1,14),_CaaStaticObjectMisses_Type())
caaStaticObjectMisses.setMaxAccess(_C)
if mibBuilder.loadTexts:caaStaticObjectMisses.setStatus(_A)
if mibBuilder.loadTexts:caaStaticObjectMisses.setUnits('cache-misses')
_CaaStaticObjectMissSize_Type=Counter32
_CaaStaticObjectMissSize_Object=MibTableColumn
caaStaticObjectMissSize=_CaaStaticObjectMissSize_Object((1,3,6,1,4,1,9,9,594,1,1,1,1,15),_CaaStaticObjectMissSize_Type())
caaStaticObjectMissSize.setMaxAccess(_C)
if mibBuilder.loadTexts:caaStaticObjectMissSize.setStatus(_A)
if mibBuilder.loadTexts:caaStaticObjectMissSize.setUnits(_E)
_CaaRefreshHits_Type=Counter32
_CaaRefreshHits_Object=MibTableColumn
caaRefreshHits=_CaaRefreshHits_Object((1,3,6,1,4,1,9,9,594,1,1,1,1,16),_CaaRefreshHits_Type())
caaRefreshHits.setMaxAccess(_C)
if mibBuilder.loadTexts:caaRefreshHits.setStatus(_A)
if mibBuilder.loadTexts:caaRefreshHits.setUnits(_D)
_CaaIMSHits_Type=Counter32
_CaaIMSHits_Object=MibTableColumn
caaIMSHits=_CaaIMSHits_Object((1,3,6,1,4,1,9,9,594,1,1,1,1,17),_CaaIMSHits_Type())
caaIMSHits.setMaxAccess(_C)
if mibBuilder.loadTexts:caaIMSHits.setStatus(_A)
if mibBuilder.loadTexts:caaIMSHits.setUnits(_D)
_CaaIMSMisses_Type=Counter32
_CaaIMSMisses_Object=MibTableColumn
caaIMSMisses=_CaaIMSMisses_Object((1,3,6,1,4,1,9,9,594,1,1,1,1,18),_CaaIMSMisses_Type())
caaIMSMisses.setMaxAccess(_C)
if mibBuilder.loadTexts:caaIMSMisses.setStatus(_A)
if mibBuilder.loadTexts:caaIMSMisses.setUnits(_D)
_CaaDirectRequests_Type=Counter32
_CaaDirectRequests_Object=MibTableColumn
caaDirectRequests=_CaaDirectRequests_Object((1,3,6,1,4,1,9,9,594,1,1,1,1,19),_CaaDirectRequests_Type())
caaDirectRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:caaDirectRequests.setStatus(_A)
if mibBuilder.loadTexts:caaDirectRequests.setUnits(_D)
_CaaRequestSize_Type=Counter32
_CaaRequestSize_Object=MibTableColumn
caaRequestSize=_CaaRequestSize_Object((1,3,6,1,4,1,9,9,594,1,1,1,1,20),_CaaRequestSize_Type())
caaRequestSize.setMaxAccess(_C)
if mibBuilder.loadTexts:caaRequestSize.setStatus(_A)
if mibBuilder.loadTexts:caaRequestSize.setUnits(_E)
_CaaDeltaAbandons_Type=Counter32
_CaaDeltaAbandons_Object=MibTableColumn
caaDeltaAbandons=_CaaDeltaAbandons_Object((1,3,6,1,4,1,9,9,594,1,1,1,1,21),_CaaDeltaAbandons_Type())
caaDeltaAbandons.setMaxAccess(_C)
if mibBuilder.loadTexts:caaDeltaAbandons.setStatus(_A)
if mibBuilder.loadTexts:caaDeltaAbandons.setUnits(_D)
_CaaNotificationObjects_ObjectIdentity=ObjectIdentity
caaNotificationObjects=_CaaNotificationObjects_ObjectIdentity((1,3,6,1,4,1,9,9,594,1,2))
class _CaaStateChangeNotifEnabled_Type(TruthValue):defaultValue=2
_CaaStateChangeNotifEnabled_Type.__name__=_H
_CaaStateChangeNotifEnabled_Object=MibScalar
caaStateChangeNotifEnabled=_CaaStateChangeNotifEnabled_Object((1,3,6,1,4,1,9,9,594,1,2,1),_CaaStateChangeNotifEnabled_Type())
caaStateChangeNotifEnabled.setMaxAccess('read-write')
if mibBuilder.loadTexts:caaStateChangeNotifEnabled.setStatus(_A)
_CaaMIBConformance_ObjectIdentity=ObjectIdentity
caaMIBConformance=_CaaMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,594,2))
_CaaMIBCompliances_ObjectIdentity=ObjectIdentity
caaMIBCompliances=_CaaMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,594,2,1))
_CaaMIBGroups_ObjectIdentity=ObjectIdentity
caaMIBGroups=_CaaMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,594,2,2))
caaMIBStatsGroup=ObjectGroup((1,3,6,1,4,1,9,9,594,2,2,1))
caaMIBStatsGroup.setObjects(*((_B,_F),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c)))
if mibBuilder.loadTexts:caaMIBStatsGroup.setStatus(_A)
caaMIBNotifObjectGroup=ObjectGroup((1,3,6,1,4,1,9,9,594,2,2,3))
caaMIBNotifObjectGroup.setObjects((_B,_d))
if mibBuilder.loadTexts:caaMIBNotifObjectGroup.setStatus(_A)
caaStateChange=NotificationType((1,3,6,1,4,1,9,9,594,0,1))
caaStateChange.setObjects((_B,_F))
if mibBuilder.loadTexts:caaStateChange.setStatus(_A)
caaMIBNotificationsGroup=NotificationGroup((1,3,6,1,4,1,9,9,594,2,2,2))
caaMIBNotificationsGroup.setObjects((_B,_e))
if mibBuilder.loadTexts:caaMIBNotificationsGroup.setStatus(_A)
caaMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,594,2,1,1))
caaMIBCompliance.setObjects(*((_B,_f),(_B,_g),(_B,_h)))
if mibBuilder.loadTexts:caaMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'CaaState':CaaState,'ciscoApplicationAccelerationMIB':ciscoApplicationAccelerationMIB,'caaMIBNotifications':caaMIBNotifications,_e:caaStateChange,'caaMIBObjects':caaMIBObjects,'caaStats':caaStats,'caaStatTable':caaStatTable,'caaStatEntry':caaStatEntry,_I:caaPort,_F:caaState,_K:caaRequests,_L:caaNoncondensableRequests,_M:caaRequestedObjectSize,_N:caaFinalResponseSize,_O:caaLastRestartedTime,_P:caaTransformed,_Q:caaUntransformed,_R:caaTransformedObjectRequests,_S:caaTransformedObjectIMSRequests,_T:caaStaticObjectHits,_U:caaStaticObjectHitSize,_V:caaStaticObjectMisses,_W:caaStaticObjectMissSize,_X:caaRefreshHits,_Y:caaIMSHits,_Z:caaIMSMisses,_a:caaDirectRequests,_b:caaRequestSize,_c:caaDeltaAbandons,'caaNotificationObjects':caaNotificationObjects,_d:caaStateChangeNotifEnabled,'caaMIBConformance':caaMIBConformance,'caaMIBCompliances':caaMIBCompliances,'caaMIBCompliance':caaMIBCompliance,'caaMIBGroups':caaMIBGroups,_f:caaMIBStatsGroup,_g:caaMIBNotificationsGroup,_h:caaMIBNotifObjectGroup})