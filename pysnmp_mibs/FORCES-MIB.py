_W='forcesStatsGroup'
_V='forcesNotificationStatsGroup'
_U='forcesNotificationGroup'
_T='forcesMibGroup'
_S='forcesAssociationEntryDownStats'
_R='forcesAssociationEntryUpStats'
_Q='forcesAssociationEntryDown'
_P='forcesAssociationEntryUp'
_O='forcesLatestProtocolVersionSupported'
_N='not-accessible'
_M='forcesAssociationFEID'
_L='forcesAssociationCEID'
_K='forcesAssociationCounterDiscontinuityTime'
_J='forcesAssociationOperMsgReceived'
_I='forcesAssociationOperMsgSent'
_H='forcesAssociationHBMsgReceived'
_G='forcesAssociationHBMsgSent'
_F='forcesAssociationTimeDown'
_E='forcesAssociationTimeUp'
_D='forcesAssociationRunningProtocolVersion'
_C='read-only'
_B='current'
_A='FORCES-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ZeroBasedCounter32,=mibBuilder.importSymbols('RMON2-MIB','ZeroBasedCounter32')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','mib-2')
DisplayString,PhysAddress,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeStamp')
forcesMib=ModuleIdentity((1,3,6,1,2,1,187))
if mibBuilder.loadTexts:forcesMib.setRevisions(('2010-03-10 00:00',))
class ForcesID(TextualConvention,OctetString):status=_B;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
class ForcesProtocolVersion(TextualConvention,Integer32):status=_B;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_ForcesMibNotifications_ObjectIdentity=ObjectIdentity
forcesMibNotifications=_ForcesMibNotifications_ObjectIdentity((1,3,6,1,2,1,187,0))
_ForcesMibObjects_ObjectIdentity=ObjectIdentity
forcesMibObjects=_ForcesMibObjects_ObjectIdentity((1,3,6,1,2,1,187,1))
_ForcesLatestProtocolVersionSupported_Type=ForcesProtocolVersion
_ForcesLatestProtocolVersionSupported_Object=MibScalar
forcesLatestProtocolVersionSupported=_ForcesLatestProtocolVersionSupported_Object((1,3,6,1,2,1,187,1,1),_ForcesLatestProtocolVersionSupported_Type())
forcesLatestProtocolVersionSupported.setMaxAccess(_C)
if mibBuilder.loadTexts:forcesLatestProtocolVersionSupported.setStatus(_B)
_ForcesAssociations_ObjectIdentity=ObjectIdentity
forcesAssociations=_ForcesAssociations_ObjectIdentity((1,3,6,1,2,1,187,1,2))
_ForcesAssociationTable_Object=MibTable
forcesAssociationTable=_ForcesAssociationTable_Object((1,3,6,1,2,1,187,1,2,1))
if mibBuilder.loadTexts:forcesAssociationTable.setStatus(_B)
_ForcesAssociationEntry_Object=MibTableRow
forcesAssociationEntry=_ForcesAssociationEntry_Object((1,3,6,1,2,1,187,1,2,1,1))
forcesAssociationEntry.setIndexNames((0,_A,_L),(0,_A,_M))
if mibBuilder.loadTexts:forcesAssociationEntry.setStatus(_B)
_ForcesAssociationCEID_Type=ForcesID
_ForcesAssociationCEID_Object=MibTableColumn
forcesAssociationCEID=_ForcesAssociationCEID_Object((1,3,6,1,2,1,187,1,2,1,1,1),_ForcesAssociationCEID_Type())
forcesAssociationCEID.setMaxAccess(_N)
if mibBuilder.loadTexts:forcesAssociationCEID.setStatus(_B)
_ForcesAssociationFEID_Type=ForcesID
_ForcesAssociationFEID_Object=MibTableColumn
forcesAssociationFEID=_ForcesAssociationFEID_Object((1,3,6,1,2,1,187,1,2,1,1,2),_ForcesAssociationFEID_Type())
forcesAssociationFEID.setMaxAccess(_N)
if mibBuilder.loadTexts:forcesAssociationFEID.setStatus(_B)
_ForcesAssociationRunningProtocolVersion_Type=ForcesProtocolVersion
_ForcesAssociationRunningProtocolVersion_Object=MibTableColumn
forcesAssociationRunningProtocolVersion=_ForcesAssociationRunningProtocolVersion_Object((1,3,6,1,2,1,187,1,2,1,1,3),_ForcesAssociationRunningProtocolVersion_Type())
forcesAssociationRunningProtocolVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:forcesAssociationRunningProtocolVersion.setStatus(_B)
_ForcesAssociationTimeUp_Type=TimeStamp
_ForcesAssociationTimeUp_Object=MibTableColumn
forcesAssociationTimeUp=_ForcesAssociationTimeUp_Object((1,3,6,1,2,1,187,1,2,1,1,4),_ForcesAssociationTimeUp_Type())
forcesAssociationTimeUp.setMaxAccess(_C)
if mibBuilder.loadTexts:forcesAssociationTimeUp.setStatus(_B)
_ForcesAssociationTimeDown_Type=TimeStamp
_ForcesAssociationTimeDown_Object=MibTableColumn
forcesAssociationTimeDown=_ForcesAssociationTimeDown_Object((1,3,6,1,2,1,187,1,2,1,1,5),_ForcesAssociationTimeDown_Type())
forcesAssociationTimeDown.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:forcesAssociationTimeDown.setStatus(_B)
_ForcesAssociationHBMsgSent_Type=ZeroBasedCounter32
_ForcesAssociationHBMsgSent_Object=MibTableColumn
forcesAssociationHBMsgSent=_ForcesAssociationHBMsgSent_Object((1,3,6,1,2,1,187,1,2,1,1,6),_ForcesAssociationHBMsgSent_Type())
forcesAssociationHBMsgSent.setMaxAccess(_C)
if mibBuilder.loadTexts:forcesAssociationHBMsgSent.setStatus(_B)
_ForcesAssociationHBMsgReceived_Type=ZeroBasedCounter32
_ForcesAssociationHBMsgReceived_Object=MibTableColumn
forcesAssociationHBMsgReceived=_ForcesAssociationHBMsgReceived_Object((1,3,6,1,2,1,187,1,2,1,1,7),_ForcesAssociationHBMsgReceived_Type())
forcesAssociationHBMsgReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:forcesAssociationHBMsgReceived.setStatus(_B)
_ForcesAssociationOperMsgSent_Type=ZeroBasedCounter32
_ForcesAssociationOperMsgSent_Object=MibTableColumn
forcesAssociationOperMsgSent=_ForcesAssociationOperMsgSent_Object((1,3,6,1,2,1,187,1,2,1,1,8),_ForcesAssociationOperMsgSent_Type())
forcesAssociationOperMsgSent.setMaxAccess(_C)
if mibBuilder.loadTexts:forcesAssociationOperMsgSent.setStatus(_B)
_ForcesAssociationOperMsgReceived_Type=ZeroBasedCounter32
_ForcesAssociationOperMsgReceived_Object=MibTableColumn
forcesAssociationOperMsgReceived=_ForcesAssociationOperMsgReceived_Object((1,3,6,1,2,1,187,1,2,1,1,9),_ForcesAssociationOperMsgReceived_Type())
forcesAssociationOperMsgReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:forcesAssociationOperMsgReceived.setStatus(_B)
_ForcesAssociationCounterDiscontinuityTime_Type=TimeStamp
_ForcesAssociationCounterDiscontinuityTime_Object=MibTableColumn
forcesAssociationCounterDiscontinuityTime=_ForcesAssociationCounterDiscontinuityTime_Object((1,3,6,1,2,1,187,1,2,1,1,10),_ForcesAssociationCounterDiscontinuityTime_Type())
forcesAssociationCounterDiscontinuityTime.setMaxAccess(_C)
if mibBuilder.loadTexts:forcesAssociationCounterDiscontinuityTime.setStatus(_B)
_ForcesMibConformance_ObjectIdentity=ObjectIdentity
forcesMibConformance=_ForcesMibConformance_ObjectIdentity((1,3,6,1,2,1,187,2))
_ForcesMibCompliances_ObjectIdentity=ObjectIdentity
forcesMibCompliances=_ForcesMibCompliances_ObjectIdentity((1,3,6,1,2,1,187,2,1))
_ForcesMibGroups_ObjectIdentity=ObjectIdentity
forcesMibGroups=_ForcesMibGroups_ObjectIdentity((1,3,6,1,2,1,187,2,2))
forcesMibGroup=ObjectGroup((1,3,6,1,2,1,187,2,2,2))
forcesMibGroup.setObjects(*((_A,_O),(_A,_D)))
if mibBuilder.loadTexts:forcesMibGroup.setStatus(_B)
forcesStatsGroup=ObjectGroup((1,3,6,1,2,1,187,2,2,4))
forcesStatsGroup.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:forcesStatsGroup.setStatus(_B)
forcesAssociationEntryUp=NotificationType((1,3,6,1,2,1,187,0,1))
forcesAssociationEntryUp.setObjects((_A,_D))
if mibBuilder.loadTexts:forcesAssociationEntryUp.setStatus(_B)
forcesAssociationEntryDown=NotificationType((1,3,6,1,2,1,187,0,2))
forcesAssociationEntryDown.setObjects((_A,_D))
if mibBuilder.loadTexts:forcesAssociationEntryDown.setStatus(_B)
forcesAssociationEntryUpStats=NotificationType((1,3,6,1,2,1,187,0,3))
forcesAssociationEntryUpStats.setObjects(*((_A,_D),(_A,_E)))
if mibBuilder.loadTexts:forcesAssociationEntryUpStats.setStatus(_B)
forcesAssociationEntryDownStats=NotificationType((1,3,6,1,2,1,187,0,4))
forcesAssociationEntryDownStats.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:forcesAssociationEntryDownStats.setStatus(_B)
forcesNotificationGroup=NotificationGroup((1,3,6,1,2,1,187,2,2,1))
forcesNotificationGroup.setObjects(*((_A,_P),(_A,_Q)))
if mibBuilder.loadTexts:forcesNotificationGroup.setStatus(_B)
forcesNotificationStatsGroup=NotificationGroup((1,3,6,1,2,1,187,2,2,3))
forcesNotificationStatsGroup.setObjects(*((_A,_R),(_A,_S)))
if mibBuilder.loadTexts:forcesNotificationStatsGroup.setStatus(_B)
forcesMibCompliance=ModuleCompliance((1,3,6,1,2,1,187,2,1,1))
forcesMibCompliance.setObjects(*((_A,_T),(_A,_U),(_A,_V),(_A,_W)))
if mibBuilder.loadTexts:forcesMibCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ForcesID':ForcesID,'ForcesProtocolVersion':ForcesProtocolVersion,'forcesMib':forcesMib,'forcesMibNotifications':forcesMibNotifications,_P:forcesAssociationEntryUp,_Q:forcesAssociationEntryDown,_R:forcesAssociationEntryUpStats,_S:forcesAssociationEntryDownStats,'forcesMibObjects':forcesMibObjects,_O:forcesLatestProtocolVersionSupported,'forcesAssociations':forcesAssociations,'forcesAssociationTable':forcesAssociationTable,'forcesAssociationEntry':forcesAssociationEntry,_L:forcesAssociationCEID,_M:forcesAssociationFEID,_D:forcesAssociationRunningProtocolVersion,_E:forcesAssociationTimeUp,_F:forcesAssociationTimeDown,_G:forcesAssociationHBMsgSent,_H:forcesAssociationHBMsgReceived,_I:forcesAssociationOperMsgSent,_J:forcesAssociationOperMsgReceived,_K:forcesAssociationCounterDiscontinuityTime,'forcesMibConformance':forcesMibConformance,'forcesMibCompliances':forcesMibCompliances,'forcesMibCompliance':forcesMibCompliance,'forcesMibGroups':forcesMibGroups,_U:forcesNotificationGroup,_T:forcesMibGroup,_V:forcesNotificationStatsGroup,_W:forcesStatsGroup})