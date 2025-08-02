_V='me1200LoopProtectionNotificationInfoGroup'
_U='me1200LoopProtectionInterfaceStatusTableInfoGroup'
_T='me1200LoopProtectionInterfaceParamTableInfoGroup'
_S='me1200LoopProtectionGlobalsInfoGroup'
_R='me1200LoopProtectionNotificationLoopDetected'
_Q='me1200LoopProtectionInterfaceStatusLoopDetected'
_P='me1200LoopProtectionInterfaceStatusDisabled'
_O='me1200LoopProtectionInterfaceParamTransmit'
_N='me1200LoopProtectionInterfaceParamAction'
_M='me1200LoopProtectionInterfaceParamEnabled'
_L='me1200LoopProtectionGlobalsShutdownPeriod'
_K='me1200LoopProtectionGlobalsTransmitInterval'
_J='me1200LoopProtectionGlobalsEnabled'
_I='me1200LoopProtectionInterfaceStatusIfIndex'
_H='not-accessible'
_G='me1200LoopProtectionInterfaceParamIfIndex'
_F='me1200LoopProtectionInterfaceStatusLastLoop'
_E='me1200LoopProtectionInterfaceStatusLoopCount'
_D='read-only'
_C='read-write'
_B='ME1200-LOOP-PROTECTION-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
me1200SwitchMgmt,=mibBuilder.importSymbols('CISCOME1200-MIB','me1200SwitchMgmt')
ME1200InterfaceIndex,=mibBuilder.importSymbols('ME1200-TC','ME1200InterfaceIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
me1200LoopProtectionMib=ModuleIdentity((1,3,6,1,4,1,9,9,815,1,91))
if mibBuilder.loadTexts:me1200LoopProtectionMib.setRevisions(('2016-04-27 00:00','2014-03-11 00:00','2014-02-10 00:00','2014-01-29 00:00','2014-01-27 00:00','2014-01-24 00:00'))
class ME1200LoopProtectionAction(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('shutdown',0),('shutdownAndLogEvent',1),('logEvent',2)))
_Me1200LoopProtectionObjects_ObjectIdentity=ObjectIdentity
me1200LoopProtectionObjects=_Me1200LoopProtectionObjects_ObjectIdentity((1,3,6,1,4,1,9,9,815,1,91,1))
_Me1200LoopProtectionConfig_ObjectIdentity=ObjectIdentity
me1200LoopProtectionConfig=_Me1200LoopProtectionConfig_ObjectIdentity((1,3,6,1,4,1,9,9,815,1,91,1,2))
_Me1200LoopProtectionGlobals_ObjectIdentity=ObjectIdentity
me1200LoopProtectionGlobals=_Me1200LoopProtectionGlobals_ObjectIdentity((1,3,6,1,4,1,9,9,815,1,91,1,2,1))
_Me1200LoopProtectionGlobalsEnabled_Type=TruthValue
_Me1200LoopProtectionGlobalsEnabled_Object=MibScalar
me1200LoopProtectionGlobalsEnabled=_Me1200LoopProtectionGlobalsEnabled_Object((1,3,6,1,4,1,9,9,815,1,91,1,2,1,1),_Me1200LoopProtectionGlobalsEnabled_Type())
me1200LoopProtectionGlobalsEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:me1200LoopProtectionGlobalsEnabled.setStatus(_A)
_Me1200LoopProtectionGlobalsTransmitInterval_Type=Integer32
_Me1200LoopProtectionGlobalsTransmitInterval_Object=MibScalar
me1200LoopProtectionGlobalsTransmitInterval=_Me1200LoopProtectionGlobalsTransmitInterval_Object((1,3,6,1,4,1,9,9,815,1,91,1,2,1,2),_Me1200LoopProtectionGlobalsTransmitInterval_Type())
me1200LoopProtectionGlobalsTransmitInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:me1200LoopProtectionGlobalsTransmitInterval.setStatus(_A)
_Me1200LoopProtectionGlobalsShutdownPeriod_Type=Integer32
_Me1200LoopProtectionGlobalsShutdownPeriod_Object=MibScalar
me1200LoopProtectionGlobalsShutdownPeriod=_Me1200LoopProtectionGlobalsShutdownPeriod_Object((1,3,6,1,4,1,9,9,815,1,91,1,2,1,3),_Me1200LoopProtectionGlobalsShutdownPeriod_Type())
me1200LoopProtectionGlobalsShutdownPeriod.setMaxAccess(_C)
if mibBuilder.loadTexts:me1200LoopProtectionGlobalsShutdownPeriod.setStatus(_A)
_Me1200LoopProtectionConfigInterface_ObjectIdentity=ObjectIdentity
me1200LoopProtectionConfigInterface=_Me1200LoopProtectionConfigInterface_ObjectIdentity((1,3,6,1,4,1,9,9,815,1,91,1,2,2))
_Me1200LoopProtectionInterfaceParamTable_Object=MibTable
me1200LoopProtectionInterfaceParamTable=_Me1200LoopProtectionInterfaceParamTable_Object((1,3,6,1,4,1,9,9,815,1,91,1,2,2,1))
if mibBuilder.loadTexts:me1200LoopProtectionInterfaceParamTable.setStatus(_A)
_Me1200LoopProtectionInterfaceParamEntry_Object=MibTableRow
me1200LoopProtectionInterfaceParamEntry=_Me1200LoopProtectionInterfaceParamEntry_Object((1,3,6,1,4,1,9,9,815,1,91,1,2,2,1,1))
me1200LoopProtectionInterfaceParamEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:me1200LoopProtectionInterfaceParamEntry.setStatus(_A)
_Me1200LoopProtectionInterfaceParamIfIndex_Type=ME1200InterfaceIndex
_Me1200LoopProtectionInterfaceParamIfIndex_Object=MibTableColumn
me1200LoopProtectionInterfaceParamIfIndex=_Me1200LoopProtectionInterfaceParamIfIndex_Object((1,3,6,1,4,1,9,9,815,1,91,1,2,2,1,1,1),_Me1200LoopProtectionInterfaceParamIfIndex_Type())
me1200LoopProtectionInterfaceParamIfIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:me1200LoopProtectionInterfaceParamIfIndex.setStatus(_A)
_Me1200LoopProtectionInterfaceParamEnabled_Type=TruthValue
_Me1200LoopProtectionInterfaceParamEnabled_Object=MibTableColumn
me1200LoopProtectionInterfaceParamEnabled=_Me1200LoopProtectionInterfaceParamEnabled_Object((1,3,6,1,4,1,9,9,815,1,91,1,2,2,1,1,2),_Me1200LoopProtectionInterfaceParamEnabled_Type())
me1200LoopProtectionInterfaceParamEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:me1200LoopProtectionInterfaceParamEnabled.setStatus(_A)
_Me1200LoopProtectionInterfaceParamAction_Type=ME1200LoopProtectionAction
_Me1200LoopProtectionInterfaceParamAction_Object=MibTableColumn
me1200LoopProtectionInterfaceParamAction=_Me1200LoopProtectionInterfaceParamAction_Object((1,3,6,1,4,1,9,9,815,1,91,1,2,2,1,1,3),_Me1200LoopProtectionInterfaceParamAction_Type())
me1200LoopProtectionInterfaceParamAction.setMaxAccess(_C)
if mibBuilder.loadTexts:me1200LoopProtectionInterfaceParamAction.setStatus(_A)
_Me1200LoopProtectionInterfaceParamTransmit_Type=TruthValue
_Me1200LoopProtectionInterfaceParamTransmit_Object=MibTableColumn
me1200LoopProtectionInterfaceParamTransmit=_Me1200LoopProtectionInterfaceParamTransmit_Object((1,3,6,1,4,1,9,9,815,1,91,1,2,2,1,1,4),_Me1200LoopProtectionInterfaceParamTransmit_Type())
me1200LoopProtectionInterfaceParamTransmit.setMaxAccess(_C)
if mibBuilder.loadTexts:me1200LoopProtectionInterfaceParamTransmit.setStatus(_A)
_Me1200LoopProtectionStatus_ObjectIdentity=ObjectIdentity
me1200LoopProtectionStatus=_Me1200LoopProtectionStatus_ObjectIdentity((1,3,6,1,4,1,9,9,815,1,91,1,3))
_Me1200LoopProtectionStatusInterface_ObjectIdentity=ObjectIdentity
me1200LoopProtectionStatusInterface=_Me1200LoopProtectionStatusInterface_ObjectIdentity((1,3,6,1,4,1,9,9,815,1,91,1,3,2))
_Me1200LoopProtectionInterfaceStatusTable_Object=MibTable
me1200LoopProtectionInterfaceStatusTable=_Me1200LoopProtectionInterfaceStatusTable_Object((1,3,6,1,4,1,9,9,815,1,91,1,3,2,1))
if mibBuilder.loadTexts:me1200LoopProtectionInterfaceStatusTable.setStatus(_A)
_Me1200LoopProtectionInterfaceStatusEntry_Object=MibTableRow
me1200LoopProtectionInterfaceStatusEntry=_Me1200LoopProtectionInterfaceStatusEntry_Object((1,3,6,1,4,1,9,9,815,1,91,1,3,2,1,1))
me1200LoopProtectionInterfaceStatusEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:me1200LoopProtectionInterfaceStatusEntry.setStatus(_A)
_Me1200LoopProtectionInterfaceStatusIfIndex_Type=ME1200InterfaceIndex
_Me1200LoopProtectionInterfaceStatusIfIndex_Object=MibTableColumn
me1200LoopProtectionInterfaceStatusIfIndex=_Me1200LoopProtectionInterfaceStatusIfIndex_Object((1,3,6,1,4,1,9,9,815,1,91,1,3,2,1,1,1),_Me1200LoopProtectionInterfaceStatusIfIndex_Type())
me1200LoopProtectionInterfaceStatusIfIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:me1200LoopProtectionInterfaceStatusIfIndex.setStatus(_A)
_Me1200LoopProtectionInterfaceStatusDisabled_Type=TruthValue
_Me1200LoopProtectionInterfaceStatusDisabled_Object=MibTableColumn
me1200LoopProtectionInterfaceStatusDisabled=_Me1200LoopProtectionInterfaceStatusDisabled_Object((1,3,6,1,4,1,9,9,815,1,91,1,3,2,1,1,2),_Me1200LoopProtectionInterfaceStatusDisabled_Type())
me1200LoopProtectionInterfaceStatusDisabled.setMaxAccess(_D)
if mibBuilder.loadTexts:me1200LoopProtectionInterfaceStatusDisabled.setStatus(_A)
_Me1200LoopProtectionInterfaceStatusLoopDetected_Type=TruthValue
_Me1200LoopProtectionInterfaceStatusLoopDetected_Object=MibTableColumn
me1200LoopProtectionInterfaceStatusLoopDetected=_Me1200LoopProtectionInterfaceStatusLoopDetected_Object((1,3,6,1,4,1,9,9,815,1,91,1,3,2,1,1,3),_Me1200LoopProtectionInterfaceStatusLoopDetected_Type())
me1200LoopProtectionInterfaceStatusLoopDetected.setMaxAccess(_D)
if mibBuilder.loadTexts:me1200LoopProtectionInterfaceStatusLoopDetected.setStatus(_A)
_Me1200LoopProtectionInterfaceStatusLoopCount_Type=Unsigned32
_Me1200LoopProtectionInterfaceStatusLoopCount_Object=MibTableColumn
me1200LoopProtectionInterfaceStatusLoopCount=_Me1200LoopProtectionInterfaceStatusLoopCount_Object((1,3,6,1,4,1,9,9,815,1,91,1,3,2,1,1,4),_Me1200LoopProtectionInterfaceStatusLoopCount_Type())
me1200LoopProtectionInterfaceStatusLoopCount.setMaxAccess(_D)
if mibBuilder.loadTexts:me1200LoopProtectionInterfaceStatusLoopCount.setStatus(_A)
_Me1200LoopProtectionInterfaceStatusLastLoop_Type=Integer32
_Me1200LoopProtectionInterfaceStatusLastLoop_Object=MibTableColumn
me1200LoopProtectionInterfaceStatusLastLoop=_Me1200LoopProtectionInterfaceStatusLastLoop_Object((1,3,6,1,4,1,9,9,815,1,91,1,3,2,1,1,5),_Me1200LoopProtectionInterfaceStatusLastLoop_Type())
me1200LoopProtectionInterfaceStatusLastLoop.setMaxAccess(_D)
if mibBuilder.loadTexts:me1200LoopProtectionInterfaceStatusLastLoop.setStatus(_A)
_Me1200LoopProtectionNotificationPrefix_ObjectIdentity=ObjectIdentity
me1200LoopProtectionNotificationPrefix=_Me1200LoopProtectionNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,9,9,815,1,91,1,4))
_Me1200LoopProtectionNotification_ObjectIdentity=ObjectIdentity
me1200LoopProtectionNotification=_Me1200LoopProtectionNotification_ObjectIdentity((1,3,6,1,4,1,9,9,815,1,91,1,4,0))
_Me1200LoopProtectionMibConformance_ObjectIdentity=ObjectIdentity
me1200LoopProtectionMibConformance=_Me1200LoopProtectionMibConformance_ObjectIdentity((1,3,6,1,4,1,9,9,815,1,91,2))
_Me1200LoopProtectionMibCompliances_ObjectIdentity=ObjectIdentity
me1200LoopProtectionMibCompliances=_Me1200LoopProtectionMibCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,815,1,91,2,1))
_Me1200LoopProtectionMibGroups_ObjectIdentity=ObjectIdentity
me1200LoopProtectionMibGroups=_Me1200LoopProtectionMibGroups_ObjectIdentity((1,3,6,1,4,1,9,9,815,1,91,2,2))
me1200LoopProtectionGlobalsInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,815,1,91,2,2,1))
me1200LoopProtectionGlobalsInfoGroup.setObjects(*((_B,_J),(_B,_K),(_B,_L)))
if mibBuilder.loadTexts:me1200LoopProtectionGlobalsInfoGroup.setStatus(_A)
me1200LoopProtectionInterfaceParamTableInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,815,1,91,2,2,2))
me1200LoopProtectionInterfaceParamTableInfoGroup.setObjects(*((_B,_M),(_B,_N),(_B,_O)))
if mibBuilder.loadTexts:me1200LoopProtectionInterfaceParamTableInfoGroup.setStatus(_A)
me1200LoopProtectionInterfaceStatusTableInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,815,1,91,2,2,3))
me1200LoopProtectionInterfaceStatusTableInfoGroup.setObjects(*((_B,_P),(_B,_Q),(_B,_E),(_B,_F)))
if mibBuilder.loadTexts:me1200LoopProtectionInterfaceStatusTableInfoGroup.setStatus(_A)
me1200LoopProtectionNotificationLoopDetected=NotificationType((1,3,6,1,4,1,9,9,815,1,91,1,4,0,1))
me1200LoopProtectionNotificationLoopDetected.setObjects(*((_B,_E),(_B,_F)))
if mibBuilder.loadTexts:me1200LoopProtectionNotificationLoopDetected.setStatus(_A)
me1200LoopProtectionNotificationInfoGroup=NotificationGroup((1,3,6,1,4,1,9,9,815,1,91,2,2,4))
me1200LoopProtectionNotificationInfoGroup.setObjects((_B,_R))
if mibBuilder.loadTexts:me1200LoopProtectionNotificationInfoGroup.setStatus(_A)
me1200LoopProtectionMibCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,815,1,91,2,1,1))
me1200LoopProtectionMibCompliance.setObjects(*((_B,_S),(_B,_T),(_B,_U),(_B,_V)))
if mibBuilder.loadTexts:me1200LoopProtectionMibCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ME1200LoopProtectionAction':ME1200LoopProtectionAction,'me1200LoopProtectionMib':me1200LoopProtectionMib,'me1200LoopProtectionObjects':me1200LoopProtectionObjects,'me1200LoopProtectionConfig':me1200LoopProtectionConfig,'me1200LoopProtectionGlobals':me1200LoopProtectionGlobals,_J:me1200LoopProtectionGlobalsEnabled,_K:me1200LoopProtectionGlobalsTransmitInterval,_L:me1200LoopProtectionGlobalsShutdownPeriod,'me1200LoopProtectionConfigInterface':me1200LoopProtectionConfigInterface,'me1200LoopProtectionInterfaceParamTable':me1200LoopProtectionInterfaceParamTable,'me1200LoopProtectionInterfaceParamEntry':me1200LoopProtectionInterfaceParamEntry,_G:me1200LoopProtectionInterfaceParamIfIndex,_M:me1200LoopProtectionInterfaceParamEnabled,_N:me1200LoopProtectionInterfaceParamAction,_O:me1200LoopProtectionInterfaceParamTransmit,'me1200LoopProtectionStatus':me1200LoopProtectionStatus,'me1200LoopProtectionStatusInterface':me1200LoopProtectionStatusInterface,'me1200LoopProtectionInterfaceStatusTable':me1200LoopProtectionInterfaceStatusTable,'me1200LoopProtectionInterfaceStatusEntry':me1200LoopProtectionInterfaceStatusEntry,_I:me1200LoopProtectionInterfaceStatusIfIndex,_P:me1200LoopProtectionInterfaceStatusDisabled,_Q:me1200LoopProtectionInterfaceStatusLoopDetected,_E:me1200LoopProtectionInterfaceStatusLoopCount,_F:me1200LoopProtectionInterfaceStatusLastLoop,'me1200LoopProtectionNotificationPrefix':me1200LoopProtectionNotificationPrefix,'me1200LoopProtectionNotification':me1200LoopProtectionNotification,_R:me1200LoopProtectionNotificationLoopDetected,'me1200LoopProtectionMibConformance':me1200LoopProtectionMibConformance,'me1200LoopProtectionMibCompliances':me1200LoopProtectionMibCompliances,'me1200LoopProtectionMibCompliance':me1200LoopProtectionMibCompliance,'me1200LoopProtectionMibGroups':me1200LoopProtectionMibGroups,_S:me1200LoopProtectionGlobalsInfoGroup,_T:me1200LoopProtectionInterfaceParamTableInfoGroup,_U:me1200LoopProtectionInterfaceStatusTableInfoGroup,_V:me1200LoopProtectionNotificationInfoGroup})