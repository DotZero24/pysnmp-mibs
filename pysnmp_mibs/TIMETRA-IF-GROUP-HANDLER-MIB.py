_j='tmnxIfGroupHdlrNotificationGroup'
_i='tmnxIfGroupHandlerProtocolGroup'
_h='tmnxIfGroupHandlerMemberGroup'
_g='tmnxIfGroupHandlerConfigGroup'
_f='tmnxIfGroupHandlerTimeStampGroup'
_e='tmnxIfGroupHdlrMbrProtoOprChange'
_d='tmnxIfGroupHandlerProtoOprChange'
_c='tmnxIfGroupHdlrProtoUpTime'
_b='tmnxIfGroupHdlrMemberProtoUpTime'
_a='tmnxIfGrpHandlerMemberRowStatus'
_Z='tmnxIfGroupHandlerRowStatus'
_Y='tmnxIfGrpHndlrMbrTblLastChanged'
_X='tmnxIfGroupHandlerTimeStamp'
_W='tmnxIfGrpHndlrCfgTblLastChanged'
_V='tmnxIfGroupHdlrMemberProtoIndex'
_U='seconds'
_T='tmnxIfGroupHdlrProtoIndex'
_S='TmnxIfGroupHandlerIndex'
_R='TmnxAdminState'
_Q='Unsigned32'
_P='tmnxIfGroupHdlrProtoActLinks'
_O='tmnxIfGroupHdlrProtoStatus'
_N='tmnxIfGroupHdlrMemberProtoStatus'
_M='tmnxIfGroupHandlerAdminStatus'
_L='tmnxIfGroupHandlerThreshold'
_K='not-accessible'
_J='tmnxPortPortID'
_I='TIMETRA-PORT-MIB'
_H='Integer32'
_G='read-create'
_F='tmnxIfGroupHandlerIndex'
_E='tmnxChassisIndex'
_D='TIMETRA-CHASSIS-MIB'
_C='read-only'
_B='TIMETRA-IF-GROUP-HANDLER-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_Q,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TimeStamp')
tmnxChassisIndex,=mibBuilder.importSymbols(_D,_E)
timetraSRMIBModules,tmnxSRConfs,tmnxSRNotifyPrefix,tmnxSRObjs=mibBuilder.importSymbols('TIMETRA-GLOBAL-MIB','timetraSRMIBModules','tmnxSRConfs','tmnxSRNotifyPrefix','tmnxSRObjs')
tmnxPortPortID,=mibBuilder.importSymbols(_I,_J)
TmnxAdminState,=mibBuilder.importSymbols('TIMETRA-TC-MIB',_R)
timetraIfGroupMIBModule=ModuleIdentity((1,3,6,1,4,1,6527,1,1,3,69))
if mibBuilder.loadTexts:timetraIfGroupMIBModule.setRevisions(('2009-02-28 00:00',))
class TmnxIfGroupHandlerIndex(TextualConvention,Unsigned32):status=_A
class TmnxIfGroupProtocolIndex(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('ipcp',1),('ipv6cp',2),('mplscp',3),('osicp',4)))
_TmnxIfGroupConformance_ObjectIdentity=ObjectIdentity
tmnxIfGroupConformance=_TmnxIfGroupConformance_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,69))
_TmnxIfGroupCompliances_ObjectIdentity=ObjectIdentity
tmnxIfGroupCompliances=_TmnxIfGroupCompliances_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,69,1))
_TmnxIfGroupGroups_ObjectIdentity=ObjectIdentity
tmnxIfGroupGroups=_TmnxIfGroupGroups_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,69,2))
_TmnxIfGroupObjs_ObjectIdentity=ObjectIdentity
tmnxIfGroupObjs=_TmnxIfGroupObjs_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,69))
_TmnxIfGroupConfigTimeStamps_ObjectIdentity=ObjectIdentity
tmnxIfGroupConfigTimeStamps=_TmnxIfGroupConfigTimeStamps_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,69,0))
_TmnxIfGrpHndlrCfgTblLastChanged_Type=TimeStamp
_TmnxIfGrpHndlrCfgTblLastChanged_Object=MibScalar
tmnxIfGrpHndlrCfgTblLastChanged=_TmnxIfGrpHndlrCfgTblLastChanged_Object((1,3,6,1,4,1,6527,3,1,2,69,0,1),_TmnxIfGrpHndlrCfgTblLastChanged_Type())
tmnxIfGrpHndlrCfgTblLastChanged.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxIfGrpHndlrCfgTblLastChanged.setStatus(_A)
_TmnxIfGrpHndlrMbrTblLastChanged_Type=TimeStamp
_TmnxIfGrpHndlrMbrTblLastChanged_Object=MibScalar
tmnxIfGrpHndlrMbrTblLastChanged=_TmnxIfGrpHndlrMbrTblLastChanged_Object((1,3,6,1,4,1,6527,3,1,2,69,0,2),_TmnxIfGrpHndlrMbrTblLastChanged_Type())
tmnxIfGrpHndlrMbrTblLastChanged.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxIfGrpHndlrMbrTblLastChanged.setStatus(_A)
_TmnxIfGroupConfigurations_ObjectIdentity=ObjectIdentity
tmnxIfGroupConfigurations=_TmnxIfGroupConfigurations_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,69,1))
_TmnxIfGroupHandlerConfigTable_Object=MibTable
tmnxIfGroupHandlerConfigTable=_TmnxIfGroupHandlerConfigTable_Object((1,3,6,1,4,1,6527,3,1,2,69,1,1))
if mibBuilder.loadTexts:tmnxIfGroupHandlerConfigTable.setStatus(_A)
_TmnxIfGroupHandlerConfigEntry_Object=MibTableRow
tmnxIfGroupHandlerConfigEntry=_TmnxIfGroupHandlerConfigEntry_Object((1,3,6,1,4,1,6527,3,1,2,69,1,1,1))
tmnxIfGroupHandlerConfigEntry.setIndexNames((0,_D,_E),(0,_B,_F))
if mibBuilder.loadTexts:tmnxIfGroupHandlerConfigEntry.setStatus(_A)
class _TmnxIfGroupHandlerIndex_Type(TmnxIfGroupHandlerIndex):subtypeSpec=TmnxIfGroupHandlerIndex.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_TmnxIfGroupHandlerIndex_Type.__name__=_S
_TmnxIfGroupHandlerIndex_Object=MibTableColumn
tmnxIfGroupHandlerIndex=_TmnxIfGroupHandlerIndex_Object((1,3,6,1,4,1,6527,3,1,2,69,1,1,1,1),_TmnxIfGroupHandlerIndex_Type())
tmnxIfGroupHandlerIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:tmnxIfGroupHandlerIndex.setStatus(_A)
_TmnxIfGroupHandlerRowStatus_Type=RowStatus
_TmnxIfGroupHandlerRowStatus_Object=MibTableColumn
tmnxIfGroupHandlerRowStatus=_TmnxIfGroupHandlerRowStatus_Object((1,3,6,1,4,1,6527,3,1,2,69,1,1,1,2),_TmnxIfGroupHandlerRowStatus_Type())
tmnxIfGroupHandlerRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:tmnxIfGroupHandlerRowStatus.setStatus(_A)
_TmnxIfGroupHandlerTimeStamp_Type=TimeStamp
_TmnxIfGroupHandlerTimeStamp_Object=MibTableColumn
tmnxIfGroupHandlerTimeStamp=_TmnxIfGroupHandlerTimeStamp_Object((1,3,6,1,4,1,6527,3,1,2,69,1,1,1,3),_TmnxIfGroupHandlerTimeStamp_Type())
tmnxIfGroupHandlerTimeStamp.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxIfGroupHandlerTimeStamp.setStatus(_A)
class _TmnxIfGroupHandlerThreshold_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_TmnxIfGroupHandlerThreshold_Type.__name__=_Q
_TmnxIfGroupHandlerThreshold_Object=MibTableColumn
tmnxIfGroupHandlerThreshold=_TmnxIfGroupHandlerThreshold_Object((1,3,6,1,4,1,6527,3,1,2,69,1,1,1,4),_TmnxIfGroupHandlerThreshold_Type())
tmnxIfGroupHandlerThreshold.setMaxAccess(_G)
if mibBuilder.loadTexts:tmnxIfGroupHandlerThreshold.setStatus(_A)
class _TmnxIfGroupHandlerAdminStatus_Type(TmnxAdminState):defaultValue=3
_TmnxIfGroupHandlerAdminStatus_Type.__name__=_R
_TmnxIfGroupHandlerAdminStatus_Object=MibTableColumn
tmnxIfGroupHandlerAdminStatus=_TmnxIfGroupHandlerAdminStatus_Object((1,3,6,1,4,1,6527,3,1,2,69,1,1,1,5),_TmnxIfGroupHandlerAdminStatus_Type())
tmnxIfGroupHandlerAdminStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:tmnxIfGroupHandlerAdminStatus.setStatus(_A)
_TmnxIfGroupHandlerProtoTable_Object=MibTable
tmnxIfGroupHandlerProtoTable=_TmnxIfGroupHandlerProtoTable_Object((1,3,6,1,4,1,6527,3,1,2,69,1,2))
if mibBuilder.loadTexts:tmnxIfGroupHandlerProtoTable.setStatus(_A)
_TmnxIfGroupHandlerProtoEntry_Object=MibTableRow
tmnxIfGroupHandlerProtoEntry=_TmnxIfGroupHandlerProtoEntry_Object((1,3,6,1,4,1,6527,3,1,2,69,1,2,1))
tmnxIfGroupHandlerProtoEntry.setIndexNames((0,_D,_E),(0,_B,_F),(0,_B,_T))
if mibBuilder.loadTexts:tmnxIfGroupHandlerProtoEntry.setStatus(_A)
_TmnxIfGroupHdlrProtoIndex_Type=TmnxIfGroupProtocolIndex
_TmnxIfGroupHdlrProtoIndex_Object=MibTableColumn
tmnxIfGroupHdlrProtoIndex=_TmnxIfGroupHdlrProtoIndex_Object((1,3,6,1,4,1,6527,3,1,2,69,1,2,1,1),_TmnxIfGroupHdlrProtoIndex_Type())
tmnxIfGroupHdlrProtoIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:tmnxIfGroupHdlrProtoIndex.setStatus(_A)
class _TmnxIfGroupHdlrProtoStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('none',0),('blocked',1),('inhibited',2),('waiting',3),('pending',4),('up',5)))
_TmnxIfGroupHdlrProtoStatus_Type.__name__=_H
_TmnxIfGroupHdlrProtoStatus_Object=MibTableColumn
tmnxIfGroupHdlrProtoStatus=_TmnxIfGroupHdlrProtoStatus_Object((1,3,6,1,4,1,6527,3,1,2,69,1,2,1,2),_TmnxIfGroupHdlrProtoStatus_Type())
tmnxIfGroupHdlrProtoStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxIfGroupHdlrProtoStatus.setStatus(_A)
_TmnxIfGroupHdlrProtoActLinks_Type=Unsigned32
_TmnxIfGroupHdlrProtoActLinks_Object=MibTableColumn
tmnxIfGroupHdlrProtoActLinks=_TmnxIfGroupHdlrProtoActLinks_Object((1,3,6,1,4,1,6527,3,1,2,69,1,2,1,3),_TmnxIfGroupHdlrProtoActLinks_Type())
tmnxIfGroupHdlrProtoActLinks.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxIfGroupHdlrProtoActLinks.setStatus(_A)
_TmnxIfGroupHdlrProtoUpTime_Type=Unsigned32
_TmnxIfGroupHdlrProtoUpTime_Object=MibTableColumn
tmnxIfGroupHdlrProtoUpTime=_TmnxIfGroupHdlrProtoUpTime_Object((1,3,6,1,4,1,6527,3,1,2,69,1,2,1,4),_TmnxIfGroupHdlrProtoUpTime_Type())
tmnxIfGroupHdlrProtoUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxIfGroupHdlrProtoUpTime.setStatus(_A)
if mibBuilder.loadTexts:tmnxIfGroupHdlrProtoUpTime.setUnits(_U)
_TmnxIfGroupHandlerMemberTable_Object=MibTable
tmnxIfGroupHandlerMemberTable=_TmnxIfGroupHandlerMemberTable_Object((1,3,6,1,4,1,6527,3,1,2,69,1,3))
if mibBuilder.loadTexts:tmnxIfGroupHandlerMemberTable.setStatus(_A)
_TmnxIfGroupHandlerMemberEntry_Object=MibTableRow
tmnxIfGroupHandlerMemberEntry=_TmnxIfGroupHandlerMemberEntry_Object((1,3,6,1,4,1,6527,3,1,2,69,1,3,1))
tmnxIfGroupHandlerMemberEntry.setIndexNames((0,_D,_E),(0,_B,_F),(0,_I,_J))
if mibBuilder.loadTexts:tmnxIfGroupHandlerMemberEntry.setStatus(_A)
_TmnxIfGrpHandlerMemberRowStatus_Type=RowStatus
_TmnxIfGrpHandlerMemberRowStatus_Object=MibTableColumn
tmnxIfGrpHandlerMemberRowStatus=_TmnxIfGrpHandlerMemberRowStatus_Object((1,3,6,1,4,1,6527,3,1,2,69,1,3,1,1),_TmnxIfGrpHandlerMemberRowStatus_Type())
tmnxIfGrpHandlerMemberRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:tmnxIfGrpHandlerMemberRowStatus.setStatus(_A)
_TmnxIfGroupHdlrMemberProtoTable_Object=MibTable
tmnxIfGroupHdlrMemberProtoTable=_TmnxIfGroupHdlrMemberProtoTable_Object((1,3,6,1,4,1,6527,3,1,2,69,1,4))
if mibBuilder.loadTexts:tmnxIfGroupHdlrMemberProtoTable.setStatus(_A)
_TmnxIfGroupHdlrMemberProtoEntry_Object=MibTableRow
tmnxIfGroupHdlrMemberProtoEntry=_TmnxIfGroupHdlrMemberProtoEntry_Object((1,3,6,1,4,1,6527,3,1,2,69,1,4,1))
tmnxIfGroupHdlrMemberProtoEntry.setIndexNames((0,_D,_E),(0,_B,_F),(0,_I,_J),(0,_B,_V))
if mibBuilder.loadTexts:tmnxIfGroupHdlrMemberProtoEntry.setStatus(_A)
_TmnxIfGroupHdlrMemberProtoIndex_Type=TmnxIfGroupProtocolIndex
_TmnxIfGroupHdlrMemberProtoIndex_Object=MibTableColumn
tmnxIfGroupHdlrMemberProtoIndex=_TmnxIfGroupHdlrMemberProtoIndex_Object((1,3,6,1,4,1,6527,3,1,2,69,1,4,1,1),_TmnxIfGroupHdlrMemberProtoIndex_Type())
tmnxIfGroupHdlrMemberProtoIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:tmnxIfGroupHdlrMemberProtoIndex.setStatus(_A)
class _TmnxIfGroupHdlrMemberProtoStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('none',0),('down',1),('ready',2),('running',3),('operational',4),('up',5)))
_TmnxIfGroupHdlrMemberProtoStatus_Type.__name__=_H
_TmnxIfGroupHdlrMemberProtoStatus_Object=MibTableColumn
tmnxIfGroupHdlrMemberProtoStatus=_TmnxIfGroupHdlrMemberProtoStatus_Object((1,3,6,1,4,1,6527,3,1,2,69,1,4,1,2),_TmnxIfGroupHdlrMemberProtoStatus_Type())
tmnxIfGroupHdlrMemberProtoStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxIfGroupHdlrMemberProtoStatus.setStatus(_A)
_TmnxIfGroupHdlrMemberProtoUpTime_Type=Unsigned32
_TmnxIfGroupHdlrMemberProtoUpTime_Object=MibTableColumn
tmnxIfGroupHdlrMemberProtoUpTime=_TmnxIfGroupHdlrMemberProtoUpTime_Object((1,3,6,1,4,1,6527,3,1,2,69,1,4,1,3),_TmnxIfGroupHdlrMemberProtoUpTime_Type())
tmnxIfGroupHdlrMemberProtoUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxIfGroupHdlrMemberProtoUpTime.setStatus(_A)
if mibBuilder.loadTexts:tmnxIfGroupHdlrMemberProtoUpTime.setUnits(_U)
_TmnxIfGroupStatistics_ObjectIdentity=ObjectIdentity
tmnxIfGroupStatistics=_TmnxIfGroupStatistics_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,69,2))
_TmnxIfGroupNotifyPrefix_ObjectIdentity=ObjectIdentity
tmnxIfGroupNotifyPrefix=_TmnxIfGroupNotifyPrefix_ObjectIdentity((1,3,6,1,4,1,6527,3,1,3,69))
_TmnxIfGroupNotifications_ObjectIdentity=ObjectIdentity
tmnxIfGroupNotifications=_TmnxIfGroupNotifications_ObjectIdentity((1,3,6,1,4,1,6527,3,1,3,69,0))
tmnxIfGroupHandlerTimeStampGroup=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,69,2,1))
tmnxIfGroupHandlerTimeStampGroup.setObjects(*((_B,_W),(_B,_X),(_B,_Y)))
if mibBuilder.loadTexts:tmnxIfGroupHandlerTimeStampGroup.setStatus(_A)
tmnxIfGroupHandlerConfigGroup=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,69,2,2))
tmnxIfGroupHandlerConfigGroup.setObjects(*((_B,_Z),(_B,_L),(_B,_M)))
if mibBuilder.loadTexts:tmnxIfGroupHandlerConfigGroup.setStatus(_A)
tmnxIfGroupHandlerMemberGroup=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,69,2,3))
tmnxIfGroupHandlerMemberGroup.setObjects((_B,_a))
if mibBuilder.loadTexts:tmnxIfGroupHandlerMemberGroup.setStatus(_A)
tmnxIfGroupHandlerProtocolGroup=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,69,2,4))
tmnxIfGroupHandlerProtocolGroup.setObjects(*((_B,_N),(_B,_b),(_B,_O),(_B,_P),(_B,_c)))
if mibBuilder.loadTexts:tmnxIfGroupHandlerProtocolGroup.setStatus(_A)
tmnxIfGroupHandlerProtoOprChange=NotificationType((1,3,6,1,4,1,6527,3,1,3,69,0,1))
tmnxIfGroupHandlerProtoOprChange.setObjects(*((_B,_L),(_B,_M),(_B,_O),(_B,_P)))
if mibBuilder.loadTexts:tmnxIfGroupHandlerProtoOprChange.setStatus(_A)
tmnxIfGroupHdlrMbrProtoOprChange=NotificationType((1,3,6,1,4,1,6527,3,1,3,69,0,2))
tmnxIfGroupHdlrMbrProtoOprChange.setObjects((_B,_N))
if mibBuilder.loadTexts:tmnxIfGroupHdlrMbrProtoOprChange.setStatus(_A)
tmnxIfGroupHdlrNotificationGroup=NotificationGroup((1,3,6,1,4,1,6527,3,1,1,69,2,5))
tmnxIfGroupHdlrNotificationGroup.setObjects(*((_B,_d),(_B,_e)))
if mibBuilder.loadTexts:tmnxIfGroupHdlrNotificationGroup.setStatus(_A)
tmnxIfGroupHandlerCompliance=ModuleCompliance((1,3,6,1,4,1,6527,3,1,1,69,1,1))
tmnxIfGroupHandlerCompliance.setObjects(*((_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j)))
if mibBuilder.loadTexts:tmnxIfGroupHandlerCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_S:TmnxIfGroupHandlerIndex,'TmnxIfGroupProtocolIndex':TmnxIfGroupProtocolIndex,'timetraIfGroupMIBModule':timetraIfGroupMIBModule,'tmnxIfGroupConformance':tmnxIfGroupConformance,'tmnxIfGroupCompliances':tmnxIfGroupCompliances,'tmnxIfGroupHandlerCompliance':tmnxIfGroupHandlerCompliance,'tmnxIfGroupGroups':tmnxIfGroupGroups,_f:tmnxIfGroupHandlerTimeStampGroup,_g:tmnxIfGroupHandlerConfigGroup,_h:tmnxIfGroupHandlerMemberGroup,_i:tmnxIfGroupHandlerProtocolGroup,_j:tmnxIfGroupHdlrNotificationGroup,'tmnxIfGroupObjs':tmnxIfGroupObjs,'tmnxIfGroupConfigTimeStamps':tmnxIfGroupConfigTimeStamps,_W:tmnxIfGrpHndlrCfgTblLastChanged,_Y:tmnxIfGrpHndlrMbrTblLastChanged,'tmnxIfGroupConfigurations':tmnxIfGroupConfigurations,'tmnxIfGroupHandlerConfigTable':tmnxIfGroupHandlerConfigTable,'tmnxIfGroupHandlerConfigEntry':tmnxIfGroupHandlerConfigEntry,_F:tmnxIfGroupHandlerIndex,_Z:tmnxIfGroupHandlerRowStatus,_X:tmnxIfGroupHandlerTimeStamp,_L:tmnxIfGroupHandlerThreshold,_M:tmnxIfGroupHandlerAdminStatus,'tmnxIfGroupHandlerProtoTable':tmnxIfGroupHandlerProtoTable,'tmnxIfGroupHandlerProtoEntry':tmnxIfGroupHandlerProtoEntry,_T:tmnxIfGroupHdlrProtoIndex,_O:tmnxIfGroupHdlrProtoStatus,_P:tmnxIfGroupHdlrProtoActLinks,_c:tmnxIfGroupHdlrProtoUpTime,'tmnxIfGroupHandlerMemberTable':tmnxIfGroupHandlerMemberTable,'tmnxIfGroupHandlerMemberEntry':tmnxIfGroupHandlerMemberEntry,_a:tmnxIfGrpHandlerMemberRowStatus,'tmnxIfGroupHdlrMemberProtoTable':tmnxIfGroupHdlrMemberProtoTable,'tmnxIfGroupHdlrMemberProtoEntry':tmnxIfGroupHdlrMemberProtoEntry,_V:tmnxIfGroupHdlrMemberProtoIndex,_N:tmnxIfGroupHdlrMemberProtoStatus,_b:tmnxIfGroupHdlrMemberProtoUpTime,'tmnxIfGroupStatistics':tmnxIfGroupStatistics,'tmnxIfGroupNotifyPrefix':tmnxIfGroupNotifyPrefix,'tmnxIfGroupNotifications':tmnxIfGroupNotifications,_d:tmnxIfGroupHandlerProtoOprChange,_e:tmnxIfGroupHdlrMbrProtoOprChange})