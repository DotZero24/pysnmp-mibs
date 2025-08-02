_g='alvarionPublicAccessRetentionNotificationGroup'
_f='alvarionPublicAccessRetentionPeriodicStatsMIBGroup'
_e='alvarionPublicAccessRetentionSessionsMIBGroup'
_d='publicAccessRetentionSessionMaxCountReachedTrap'
_c='publicAccessRetentionPeriodTotalSessionCount'
_b='publicAccessRetentionPeriodHighestSessionCount'
_a='publicAccessRetentionPeriodStopTime'
_Z='publicAccessRetentionPeriodStartTime'
_Y='publicAccessRetentionPeriodicStatsMaxCount'
_X='publicAccessRetentionPeriodicStatsDuration'
_W='publicAccessRetentionSessionSSID'
_V='publicAccessRetentionSessionBytesReceived'
_U='publicAccessRetentionSessionBytesSent'
_T='publicAccessRetentionSessionPacketsReceived'
_S='publicAccessRetentionSessionPacketsSent'
_R='publicAccessRetentionSessionStationIpAddress'
_Q='publicAccessRetentionSessionDuration'
_P='publicAccessRetentionSessionStartTime'
_O='publicAccessRetentionSessionUserName'
_N='publicAccessRetentionSessionState'
_M='publicAccessRetentionPeriodIndex'
_L='not-accessible'
_K='publicAccessRetentionSessionIndex'
_J='Unsigned32'
_I='OctetString'
_H='publicAccessRetentionSessionsMaxTime'
_G='publicAccessRetentionSessionsMaxCount'
_F='seconds'
_E='read-write'
_D='Integer32'
_C='read-only'
_B='ALVARION-PUBLIC-ACCESS-RETENTION-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_I,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
alvarionMgmtV2,=mibBuilder.importSymbols('ALVARION-SMI','alvarionMgmtV2')
AlvarionSSIDOrNone,=mibBuilder.importSymbols('ALVARION-TC','AlvarionSSIDOrNone')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_J,'iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention')
alvarionPublicAccessRetentionMIB=ModuleIdentity((1,3,6,1,4,1,12394,1,10,5,15))
_AlvarionPublicAccessRetentionMIBObjects_ObjectIdentity=ObjectIdentity
alvarionPublicAccessRetentionMIBObjects=_AlvarionPublicAccessRetentionMIBObjects_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,15,1))
_PublicAccessRetentionSessionsGroup_ObjectIdentity=ObjectIdentity
publicAccessRetentionSessionsGroup=_PublicAccessRetentionSessionsGroup_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,15,1,1))
class _PublicAccessRetentionSessionsMaxCount_Type(Unsigned32):defaultValue=0
_PublicAccessRetentionSessionsMaxCount_Type.__name__=_J
_PublicAccessRetentionSessionsMaxCount_Object=MibScalar
publicAccessRetentionSessionsMaxCount=_PublicAccessRetentionSessionsMaxCount_Object((1,3,6,1,4,1,12394,1,10,5,15,1,1,1),_PublicAccessRetentionSessionsMaxCount_Type())
publicAccessRetentionSessionsMaxCount.setMaxAccess(_E)
if mibBuilder.loadTexts:publicAccessRetentionSessionsMaxCount.setStatus(_A)
class _PublicAccessRetentionSessionsMaxTime_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(300,1200))
_PublicAccessRetentionSessionsMaxTime_Type.__name__=_D
_PublicAccessRetentionSessionsMaxTime_Object=MibScalar
publicAccessRetentionSessionsMaxTime=_PublicAccessRetentionSessionsMaxTime_Object((1,3,6,1,4,1,12394,1,10,5,15,1,1,2),_PublicAccessRetentionSessionsMaxTime_Type())
publicAccessRetentionSessionsMaxTime.setMaxAccess(_E)
if mibBuilder.loadTexts:publicAccessRetentionSessionsMaxTime.setStatus(_A)
if mibBuilder.loadTexts:publicAccessRetentionSessionsMaxTime.setUnits(_F)
_PublicAccessRetentionSessionTable_Object=MibTable
publicAccessRetentionSessionTable=_PublicAccessRetentionSessionTable_Object((1,3,6,1,4,1,12394,1,10,5,15,1,1,3))
if mibBuilder.loadTexts:publicAccessRetentionSessionTable.setStatus(_A)
_PublicAccessRetentionSessionEntry_Object=MibTableRow
publicAccessRetentionSessionEntry=_PublicAccessRetentionSessionEntry_Object((1,3,6,1,4,1,12394,1,10,5,15,1,1,3,1))
publicAccessRetentionSessionEntry.setIndexNames((0,_B,_K))
if mibBuilder.loadTexts:publicAccessRetentionSessionEntry.setStatus(_A)
class _PublicAccessRetentionSessionIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_PublicAccessRetentionSessionIndex_Type.__name__=_D
_PublicAccessRetentionSessionIndex_Object=MibTableColumn
publicAccessRetentionSessionIndex=_PublicAccessRetentionSessionIndex_Object((1,3,6,1,4,1,12394,1,10,5,15,1,1,3,1,1),_PublicAccessRetentionSessionIndex_Type())
publicAccessRetentionSessionIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:publicAccessRetentionSessionIndex.setStatus(_A)
class _PublicAccessRetentionSessionState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,2,3,4,5,6,7)));namedValues=NamedValues(*(('unassigned',0),('connected',2),('reconnecting',3),('disconnecting',4),('disconnected',5),('disconnectingAdministrative',6),('disconnectedAdministrative',7)))
_PublicAccessRetentionSessionState_Type.__name__=_D
_PublicAccessRetentionSessionState_Object=MibTableColumn
publicAccessRetentionSessionState=_PublicAccessRetentionSessionState_Object((1,3,6,1,4,1,12394,1,10,5,15,1,1,3,1,2),_PublicAccessRetentionSessionState_Type())
publicAccessRetentionSessionState.setMaxAccess(_C)
if mibBuilder.loadTexts:publicAccessRetentionSessionState.setStatus(_A)
class _PublicAccessRetentionSessionUserName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,253))
_PublicAccessRetentionSessionUserName_Type.__name__=_I
_PublicAccessRetentionSessionUserName_Object=MibTableColumn
publicAccessRetentionSessionUserName=_PublicAccessRetentionSessionUserName_Object((1,3,6,1,4,1,12394,1,10,5,15,1,1,3,1,3),_PublicAccessRetentionSessionUserName_Type())
publicAccessRetentionSessionUserName.setMaxAccess(_C)
if mibBuilder.loadTexts:publicAccessRetentionSessionUserName.setStatus(_A)
_PublicAccessRetentionSessionStartTime_Type=DateAndTime
_PublicAccessRetentionSessionStartTime_Object=MibTableColumn
publicAccessRetentionSessionStartTime=_PublicAccessRetentionSessionStartTime_Object((1,3,6,1,4,1,12394,1,10,5,15,1,1,3,1,4),_PublicAccessRetentionSessionStartTime_Type())
publicAccessRetentionSessionStartTime.setMaxAccess(_C)
if mibBuilder.loadTexts:publicAccessRetentionSessionStartTime.setStatus(_A)
_PublicAccessRetentionSessionDuration_Type=Counter32
_PublicAccessRetentionSessionDuration_Object=MibTableColumn
publicAccessRetentionSessionDuration=_PublicAccessRetentionSessionDuration_Object((1,3,6,1,4,1,12394,1,10,5,15,1,1,3,1,5),_PublicAccessRetentionSessionDuration_Type())
publicAccessRetentionSessionDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:publicAccessRetentionSessionDuration.setStatus(_A)
if mibBuilder.loadTexts:publicAccessRetentionSessionDuration.setUnits(_F)
_PublicAccessRetentionSessionStationIpAddress_Type=IpAddress
_PublicAccessRetentionSessionStationIpAddress_Object=MibTableColumn
publicAccessRetentionSessionStationIpAddress=_PublicAccessRetentionSessionStationIpAddress_Object((1,3,6,1,4,1,12394,1,10,5,15,1,1,3,1,6),_PublicAccessRetentionSessionStationIpAddress_Type())
publicAccessRetentionSessionStationIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:publicAccessRetentionSessionStationIpAddress.setStatus(_A)
_PublicAccessRetentionSessionPacketsSent_Type=Counter32
_PublicAccessRetentionSessionPacketsSent_Object=MibTableColumn
publicAccessRetentionSessionPacketsSent=_PublicAccessRetentionSessionPacketsSent_Object((1,3,6,1,4,1,12394,1,10,5,15,1,1,3,1,7),_PublicAccessRetentionSessionPacketsSent_Type())
publicAccessRetentionSessionPacketsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:publicAccessRetentionSessionPacketsSent.setStatus(_A)
_PublicAccessRetentionSessionPacketsReceived_Type=Counter32
_PublicAccessRetentionSessionPacketsReceived_Object=MibTableColumn
publicAccessRetentionSessionPacketsReceived=_PublicAccessRetentionSessionPacketsReceived_Object((1,3,6,1,4,1,12394,1,10,5,15,1,1,3,1,8),_PublicAccessRetentionSessionPacketsReceived_Type())
publicAccessRetentionSessionPacketsReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:publicAccessRetentionSessionPacketsReceived.setStatus(_A)
_PublicAccessRetentionSessionBytesSent_Type=Counter64
_PublicAccessRetentionSessionBytesSent_Object=MibTableColumn
publicAccessRetentionSessionBytesSent=_PublicAccessRetentionSessionBytesSent_Object((1,3,6,1,4,1,12394,1,10,5,15,1,1,3,1,9),_PublicAccessRetentionSessionBytesSent_Type())
publicAccessRetentionSessionBytesSent.setMaxAccess(_C)
if mibBuilder.loadTexts:publicAccessRetentionSessionBytesSent.setStatus(_A)
_PublicAccessRetentionSessionBytesReceived_Type=Counter64
_PublicAccessRetentionSessionBytesReceived_Object=MibTableColumn
publicAccessRetentionSessionBytesReceived=_PublicAccessRetentionSessionBytesReceived_Object((1,3,6,1,4,1,12394,1,10,5,15,1,1,3,1,10),_PublicAccessRetentionSessionBytesReceived_Type())
publicAccessRetentionSessionBytesReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:publicAccessRetentionSessionBytesReceived.setStatus(_A)
_PublicAccessRetentionSessionSSID_Type=AlvarionSSIDOrNone
_PublicAccessRetentionSessionSSID_Object=MibTableColumn
publicAccessRetentionSessionSSID=_PublicAccessRetentionSessionSSID_Object((1,3,6,1,4,1,12394,1,10,5,15,1,1,3,1,11),_PublicAccessRetentionSessionSSID_Type())
publicAccessRetentionSessionSSID.setMaxAccess(_C)
if mibBuilder.loadTexts:publicAccessRetentionSessionSSID.setStatus(_A)
_PublicAccessRetentionPeriodicStatsGroup_ObjectIdentity=ObjectIdentity
publicAccessRetentionPeriodicStatsGroup=_PublicAccessRetentionPeriodicStatsGroup_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,15,1,2))
class _PublicAccessRetentionPeriodicStatsMaxCount_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_PublicAccessRetentionPeriodicStatsMaxCount_Type.__name__=_D
_PublicAccessRetentionPeriodicStatsMaxCount_Object=MibScalar
publicAccessRetentionPeriodicStatsMaxCount=_PublicAccessRetentionPeriodicStatsMaxCount_Object((1,3,6,1,4,1,12394,1,10,5,15,1,2,1),_PublicAccessRetentionPeriodicStatsMaxCount_Type())
publicAccessRetentionPeriodicStatsMaxCount.setMaxAccess(_E)
if mibBuilder.loadTexts:publicAccessRetentionPeriodicStatsMaxCount.setStatus(_A)
class _PublicAccessRetentionPeriodicStatsDuration_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(300,1200))
_PublicAccessRetentionPeriodicStatsDuration_Type.__name__=_D
_PublicAccessRetentionPeriodicStatsDuration_Object=MibScalar
publicAccessRetentionPeriodicStatsDuration=_PublicAccessRetentionPeriodicStatsDuration_Object((1,3,6,1,4,1,12394,1,10,5,15,1,2,2),_PublicAccessRetentionPeriodicStatsDuration_Type())
publicAccessRetentionPeriodicStatsDuration.setMaxAccess(_E)
if mibBuilder.loadTexts:publicAccessRetentionPeriodicStatsDuration.setStatus(_A)
if mibBuilder.loadTexts:publicAccessRetentionPeriodicStatsDuration.setUnits(_F)
_PublicAccessRetentionPeriodTable_Object=MibTable
publicAccessRetentionPeriodTable=_PublicAccessRetentionPeriodTable_Object((1,3,6,1,4,1,12394,1,10,5,15,1,2,3))
if mibBuilder.loadTexts:publicAccessRetentionPeriodTable.setStatus(_A)
_PublicAccessRetentionPeriodEntry_Object=MibTableRow
publicAccessRetentionPeriodEntry=_PublicAccessRetentionPeriodEntry_Object((1,3,6,1,4,1,12394,1,10,5,15,1,2,3,1))
publicAccessRetentionPeriodEntry.setIndexNames((0,_B,_M))
if mibBuilder.loadTexts:publicAccessRetentionPeriodEntry.setStatus(_A)
class _PublicAccessRetentionPeriodIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,9999))
_PublicAccessRetentionPeriodIndex_Type.__name__=_D
_PublicAccessRetentionPeriodIndex_Object=MibTableColumn
publicAccessRetentionPeriodIndex=_PublicAccessRetentionPeriodIndex_Object((1,3,6,1,4,1,12394,1,10,5,15,1,2,3,1,1),_PublicAccessRetentionPeriodIndex_Type())
publicAccessRetentionPeriodIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:publicAccessRetentionPeriodIndex.setStatus(_A)
_PublicAccessRetentionPeriodStartTime_Type=DateAndTime
_PublicAccessRetentionPeriodStartTime_Object=MibTableColumn
publicAccessRetentionPeriodStartTime=_PublicAccessRetentionPeriodStartTime_Object((1,3,6,1,4,1,12394,1,10,5,15,1,2,3,1,2),_PublicAccessRetentionPeriodStartTime_Type())
publicAccessRetentionPeriodStartTime.setMaxAccess(_C)
if mibBuilder.loadTexts:publicAccessRetentionPeriodStartTime.setStatus(_A)
_PublicAccessRetentionPeriodStopTime_Type=DateAndTime
_PublicAccessRetentionPeriodStopTime_Object=MibTableColumn
publicAccessRetentionPeriodStopTime=_PublicAccessRetentionPeriodStopTime_Object((1,3,6,1,4,1,12394,1,10,5,15,1,2,3,1,3),_PublicAccessRetentionPeriodStopTime_Type())
publicAccessRetentionPeriodStopTime.setMaxAccess(_C)
if mibBuilder.loadTexts:publicAccessRetentionPeriodStopTime.setStatus(_A)
_PublicAccessRetentionPeriodHighestSessionCount_Type=Counter32
_PublicAccessRetentionPeriodHighestSessionCount_Object=MibTableColumn
publicAccessRetentionPeriodHighestSessionCount=_PublicAccessRetentionPeriodHighestSessionCount_Object((1,3,6,1,4,1,12394,1,10,5,15,1,2,3,1,4),_PublicAccessRetentionPeriodHighestSessionCount_Type())
publicAccessRetentionPeriodHighestSessionCount.setMaxAccess(_C)
if mibBuilder.loadTexts:publicAccessRetentionPeriodHighestSessionCount.setStatus(_A)
_PublicAccessRetentionPeriodTotalSessionCount_Type=Counter32
_PublicAccessRetentionPeriodTotalSessionCount_Object=MibTableColumn
publicAccessRetentionPeriodTotalSessionCount=_PublicAccessRetentionPeriodTotalSessionCount_Object((1,3,6,1,4,1,12394,1,10,5,15,1,2,3,1,5),_PublicAccessRetentionPeriodTotalSessionCount_Type())
publicAccessRetentionPeriodTotalSessionCount.setMaxAccess(_C)
if mibBuilder.loadTexts:publicAccessRetentionPeriodTotalSessionCount.setStatus(_A)
_PublicAccessRetentionMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
publicAccessRetentionMIBNotificationPrefix=_PublicAccessRetentionMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,15,2))
_PublicAccessRetentionMIBNotifications_ObjectIdentity=ObjectIdentity
publicAccessRetentionMIBNotifications=_PublicAccessRetentionMIBNotifications_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,15,2,0))
_AlvarionPublicAccessRetentionMIBConformance_ObjectIdentity=ObjectIdentity
alvarionPublicAccessRetentionMIBConformance=_AlvarionPublicAccessRetentionMIBConformance_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,15,3))
_AlvarionPublicAccessRetentionMIBCompliances_ObjectIdentity=ObjectIdentity
alvarionPublicAccessRetentionMIBCompliances=_AlvarionPublicAccessRetentionMIBCompliances_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,15,3,1))
_AlvarionPublicAccessRetentionMIBGroups_ObjectIdentity=ObjectIdentity
alvarionPublicAccessRetentionMIBGroups=_AlvarionPublicAccessRetentionMIBGroups_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,15,3,2))
alvarionPublicAccessRetentionSessionsMIBGroup=ObjectGroup((1,3,6,1,4,1,12394,1,10,5,15,3,2,1))
alvarionPublicAccessRetentionSessionsMIBGroup.setObjects(*((_B,_G),(_B,_H),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W)))
if mibBuilder.loadTexts:alvarionPublicAccessRetentionSessionsMIBGroup.setStatus(_A)
alvarionPublicAccessRetentionPeriodicStatsMIBGroup=ObjectGroup((1,3,6,1,4,1,12394,1,10,5,15,3,2,2))
alvarionPublicAccessRetentionPeriodicStatsMIBGroup.setObjects(*((_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c)))
if mibBuilder.loadTexts:alvarionPublicAccessRetentionPeriodicStatsMIBGroup.setStatus(_A)
publicAccessRetentionSessionMaxCountReachedTrap=NotificationType((1,3,6,1,4,1,12394,1,10,5,15,2,0,1))
publicAccessRetentionSessionMaxCountReachedTrap.setObjects(*((_B,_G),(_B,_H)))
if mibBuilder.loadTexts:publicAccessRetentionSessionMaxCountReachedTrap.setStatus(_A)
alvarionPublicAccessRetentionNotificationGroup=NotificationGroup((1,3,6,1,4,1,12394,1,10,5,15,3,2,3))
alvarionPublicAccessRetentionNotificationGroup.setObjects((_B,_d))
if mibBuilder.loadTexts:alvarionPublicAccessRetentionNotificationGroup.setStatus(_A)
alvarionPublicAccessRetentionMIBCompliance=ModuleCompliance((1,3,6,1,4,1,12394,1,10,5,15,3,1,1))
alvarionPublicAccessRetentionMIBCompliance.setObjects(*((_B,_e),(_B,_f),(_B,_g)))
if mibBuilder.loadTexts:alvarionPublicAccessRetentionMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'alvarionPublicAccessRetentionMIB':alvarionPublicAccessRetentionMIB,'alvarionPublicAccessRetentionMIBObjects':alvarionPublicAccessRetentionMIBObjects,'publicAccessRetentionSessionsGroup':publicAccessRetentionSessionsGroup,_G:publicAccessRetentionSessionsMaxCount,_H:publicAccessRetentionSessionsMaxTime,'publicAccessRetentionSessionTable':publicAccessRetentionSessionTable,'publicAccessRetentionSessionEntry':publicAccessRetentionSessionEntry,_K:publicAccessRetentionSessionIndex,_N:publicAccessRetentionSessionState,_O:publicAccessRetentionSessionUserName,_P:publicAccessRetentionSessionStartTime,_Q:publicAccessRetentionSessionDuration,_R:publicAccessRetentionSessionStationIpAddress,_S:publicAccessRetentionSessionPacketsSent,_T:publicAccessRetentionSessionPacketsReceived,_U:publicAccessRetentionSessionBytesSent,_V:publicAccessRetentionSessionBytesReceived,_W:publicAccessRetentionSessionSSID,'publicAccessRetentionPeriodicStatsGroup':publicAccessRetentionPeriodicStatsGroup,_Y:publicAccessRetentionPeriodicStatsMaxCount,_X:publicAccessRetentionPeriodicStatsDuration,'publicAccessRetentionPeriodTable':publicAccessRetentionPeriodTable,'publicAccessRetentionPeriodEntry':publicAccessRetentionPeriodEntry,_M:publicAccessRetentionPeriodIndex,_Z:publicAccessRetentionPeriodStartTime,_a:publicAccessRetentionPeriodStopTime,_b:publicAccessRetentionPeriodHighestSessionCount,_c:publicAccessRetentionPeriodTotalSessionCount,'publicAccessRetentionMIBNotificationPrefix':publicAccessRetentionMIBNotificationPrefix,'publicAccessRetentionMIBNotifications':publicAccessRetentionMIBNotifications,_d:publicAccessRetentionSessionMaxCountReachedTrap,'alvarionPublicAccessRetentionMIBConformance':alvarionPublicAccessRetentionMIBConformance,'alvarionPublicAccessRetentionMIBCompliances':alvarionPublicAccessRetentionMIBCompliances,'alvarionPublicAccessRetentionMIBCompliance':alvarionPublicAccessRetentionMIBCompliance,'alvarionPublicAccessRetentionMIBGroups':alvarionPublicAccessRetentionMIBGroups,_e:alvarionPublicAccessRetentionSessionsMIBGroup,_f:alvarionPublicAccessRetentionPeriodicStatsMIBGroup,_g:alvarionPublicAccessRetentionNotificationGroup})