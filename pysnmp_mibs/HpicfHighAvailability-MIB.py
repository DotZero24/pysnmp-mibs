_h='hpicfHAConfigGroup1'
_g='hpicfHAMgmtModuleGroup1'
_f='hpicfHAMgmtModuleGroup'
_e='hpicfHAConfigGroup'
_d='hpicfHAPreferredActiveManagement'
_c='hpicfHAMgmtModuleBackUpState'
_b='hpicfHAFailOverReason'
_a='hpicfHAFailOverTime'
_Z='hpicfHAFailOverState'
_Y='hpicfHAFailOverMgmtModule'
_X='hpicfHALastFailoverTime'
_W='hpicfHAMgmtFailovers'
_V='hpicfHAMgmtRedundancyFailureReason'
_U='active'
_T='unknown'
_S='hpicfHAFailOverIndex'
_R='warmStandby'
_Q='Unsigned32'
_P='entPhysicalIndex'
_O='ENTITY-MIB'
_N='hpicfHAFailOverGroup'
_M='hpicfHAStatusGroup'
_L='hpicfHAMgmtModuleRedundancyState'
_K='hpicfHAMgmtModuleStateSince'
_J='hpicfHAMgmtModuleCardUpSince'
_I='hpicfHAMgmtModuleState'
_H='hpicfHAContinuousFwdingTime'
_G='hpicfHARedundancyManagementModuleMode'
_F='read-write'
_E='deprecated'
_D='Integer32'
_C='read-only'
_B='current'
_A='HpicfHighAvailability-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
PhysicalIndex,entPhysicalIndex=mibBuilder.importSymbols(_O,'PhysicalIndex',_P)
EntityStandbyStatus,=mibBuilder.importSymbols('ENTITY-STATE-MIB','EntityStandbyStatus')
hpicfCommon,=mibBuilder.importSymbols('HP-ICF-OID','hpicfCommon')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_Q,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
hpicfHighAvailability=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,1,11))
if mibBuilder.loadTexts:hpicfHighAvailability.setRevisions(('2017-01-05 00:00','2012-05-15 00:00','2009-10-18 00:00','2009-09-06 00:00','2009-08-21 00:00','2006-09-05 00:00'))
_HpicfHAConfigObjects_ObjectIdentity=ObjectIdentity
hpicfHAConfigObjects=_HpicfHAConfigObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,1,11,1))
class _HpicfHARedundancyManagementModuleMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('enable',1),('disable',2),(_R,3)))
_HpicfHARedundancyManagementModuleMode_Type.__name__=_D
_HpicfHARedundancyManagementModuleMode_Object=MibScalar
hpicfHARedundancyManagementModuleMode=_HpicfHARedundancyManagementModuleMode_Object((1,3,6,1,4,1,11,2,14,11,1,11,1,1),_HpicfHARedundancyManagementModuleMode_Type())
hpicfHARedundancyManagementModuleMode.setMaxAccess(_F)
if mibBuilder.loadTexts:hpicfHARedundancyManagementModuleMode.setStatus(_B)
class _HpicfHAContinuousFwdingTime_Type(Unsigned32):defaultValue=300
_HpicfHAContinuousFwdingTime_Type.__name__=_Q
_HpicfHAContinuousFwdingTime_Object=MibScalar
hpicfHAContinuousFwdingTime=_HpicfHAContinuousFwdingTime_Object((1,3,6,1,4,1,11,2,14,11,1,11,1,2),_HpicfHAContinuousFwdingTime_Type())
hpicfHAContinuousFwdingTime.setMaxAccess(_F)
if mibBuilder.loadTexts:hpicfHAContinuousFwdingTime.setStatus(_B)
if mibBuilder.loadTexts:hpicfHAContinuousFwdingTime.setUnits('seconds')
class _HpicfHAPreferredActiveManagement_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('none',0),('management-module1',1),('management-module2',2)))
_HpicfHAPreferredActiveManagement_Type.__name__=_D
_HpicfHAPreferredActiveManagement_Object=MibScalar
hpicfHAPreferredActiveManagement=_HpicfHAPreferredActiveManagement_Object((1,3,6,1,4,1,11,2,14,11,1,11,1,3),_HpicfHAPreferredActiveManagement_Type())
hpicfHAPreferredActiveManagement.setMaxAccess(_F)
if mibBuilder.loadTexts:hpicfHAPreferredActiveManagement.setStatus(_B)
_HpicfHAStatusObjects_ObjectIdentity=ObjectIdentity
hpicfHAStatusObjects=_HpicfHAStatusObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,1,11,2))
class _HpicfHAMgmtRedundancyFailureReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('noRedundantModule',1),('noFailure',2),('unknownReason',3),('mismatchOS',4),('failedSelftest',5),('communicationFailure',6),('redundancyDisable',7)))
_HpicfHAMgmtRedundancyFailureReason_Type.__name__=_D
_HpicfHAMgmtRedundancyFailureReason_Object=MibScalar
hpicfHAMgmtRedundancyFailureReason=_HpicfHAMgmtRedundancyFailureReason_Object((1,3,6,1,4,1,11,2,14,11,1,11,2,1),_HpicfHAMgmtRedundancyFailureReason_Type())
hpicfHAMgmtRedundancyFailureReason.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfHAMgmtRedundancyFailureReason.setStatus(_B)
_HpicfHAMgmtFailovers_Type=Counter32
_HpicfHAMgmtFailovers_Object=MibScalar
hpicfHAMgmtFailovers=_HpicfHAMgmtFailovers_Object((1,3,6,1,4,1,11,2,14,11,1,11,2,2),_HpicfHAMgmtFailovers_Type())
hpicfHAMgmtFailovers.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfHAMgmtFailovers.setStatus(_B)
_HpicfHALastFailoverTime_Type=TimeTicks
_HpicfHALastFailoverTime_Object=MibScalar
hpicfHALastFailoverTime=_HpicfHALastFailoverTime_Object((1,3,6,1,4,1,11,2,14,11,1,11,2,3),_HpicfHALastFailoverTime_Type())
hpicfHALastFailoverTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfHALastFailoverTime.setStatus(_B)
_HpicfHAFailOverLogTable_Object=MibTable
hpicfHAFailOverLogTable=_HpicfHAFailOverLogTable_Object((1,3,6,1,4,1,11,2,14,11,1,11,2,4))
if mibBuilder.loadTexts:hpicfHAFailOverLogTable.setStatus(_B)
_HpicfHAFailOverLogEntry_Object=MibTableRow
hpicfHAFailOverLogEntry=_HpicfHAFailOverLogEntry_Object((1,3,6,1,4,1,11,2,14,11,1,11,2,4,1))
hpicfHAFailOverLogEntry.setIndexNames((0,_A,_S))
if mibBuilder.loadTexts:hpicfHAFailOverLogEntry.setStatus(_B)
class _HpicfHAFailOverIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpicfHAFailOverIndex_Type.__name__=_D
_HpicfHAFailOverIndex_Object=MibTableColumn
hpicfHAFailOverIndex=_HpicfHAFailOverIndex_Object((1,3,6,1,4,1,11,2,14,11,1,11,2,4,1,1),_HpicfHAFailOverIndex_Type())
hpicfHAFailOverIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:hpicfHAFailOverIndex.setStatus(_B)
_HpicfHAFailOverMgmtModule_Type=PhysicalIndex
_HpicfHAFailOverMgmtModule_Object=MibTableColumn
hpicfHAFailOverMgmtModule=_HpicfHAFailOverMgmtModule_Object((1,3,6,1,4,1,11,2,14,11,1,11,2,4,1,2),_HpicfHAFailOverMgmtModule_Type())
hpicfHAFailOverMgmtModule.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfHAFailOverMgmtModule.setStatus(_B)
class _HpicfHAFailOverState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_T,1),(_U,2),('standby',3)))
_HpicfHAFailOverState_Type.__name__=_D
_HpicfHAFailOverState_Object=MibTableColumn
hpicfHAFailOverState=_HpicfHAFailOverState_Object((1,3,6,1,4,1,11,2,14,11,1,11,2,4,1,3),_HpicfHAFailOverState_Type())
hpicfHAFailOverState.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfHAFailOverState.setStatus(_B)
_HpicfHAFailOverTime_Type=Integer32
_HpicfHAFailOverTime_Object=MibTableColumn
hpicfHAFailOverTime=_HpicfHAFailOverTime_Object((1,3,6,1,4,1,11,2,14,11,1,11,2,4,1,4),_HpicfHAFailOverTime_Type())
hpicfHAFailOverTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfHAFailOverTime.setStatus(_B)
class _HpicfHAFailOverReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('invalid',0),('switchoverReq',1),('buttonReq',2),('crashReq',3),('activeReset',4),('altReset',5)))
_HpicfHAFailOverReason_Type.__name__=_D
_HpicfHAFailOverReason_Object=MibTableColumn
hpicfHAFailOverReason=_HpicfHAFailOverReason_Object((1,3,6,1,4,1,11,2,14,11,1,11,2,4,1,5),_HpicfHAFailOverReason_Type())
hpicfHAFailOverReason.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfHAFailOverReason.setStatus(_B)
_HpicfHAMgmtModuleTable_Object=MibTable
hpicfHAMgmtModuleTable=_HpicfHAMgmtModuleTable_Object((1,3,6,1,4,1,11,2,14,11,1,11,2,5))
if mibBuilder.loadTexts:hpicfHAMgmtModuleTable.setStatus(_B)
_HpicfHAMgmtModuleEntry_Object=MibTableRow
hpicfHAMgmtModuleEntry=_HpicfHAMgmtModuleEntry_Object((1,3,6,1,4,1,11,2,14,11,1,11,2,5,1))
hpicfHAMgmtModuleEntry.setIndexNames((0,_O,_P))
if mibBuilder.loadTexts:hpicfHAMgmtModuleEntry.setStatus(_B)
_HpicfHAMgmtModuleState_Type=EntityStandbyStatus
_HpicfHAMgmtModuleState_Object=MibTableColumn
hpicfHAMgmtModuleState=_HpicfHAMgmtModuleState_Object((1,3,6,1,4,1,11,2,14,11,1,11,2,5,1,1),_HpicfHAMgmtModuleState_Type())
hpicfHAMgmtModuleState.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfHAMgmtModuleState.setStatus(_B)
_HpicfHAMgmtModuleCardUpSince_Type=Integer32
_HpicfHAMgmtModuleCardUpSince_Object=MibTableColumn
hpicfHAMgmtModuleCardUpSince=_HpicfHAMgmtModuleCardUpSince_Object((1,3,6,1,4,1,11,2,14,11,1,11,2,5,1,2),_HpicfHAMgmtModuleCardUpSince_Type())
hpicfHAMgmtModuleCardUpSince.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfHAMgmtModuleCardUpSince.setStatus(_B)
_HpicfHAMgmtModuleStateSince_Type=Integer32
_HpicfHAMgmtModuleStateSince_Object=MibTableColumn
hpicfHAMgmtModuleStateSince=_HpicfHAMgmtModuleStateSince_Object((1,3,6,1,4,1,11,2,14,11,1,11,2,5,1,3),_HpicfHAMgmtModuleStateSince_Type())
hpicfHAMgmtModuleStateSince.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfHAMgmtModuleStateSince.setStatus(_B)
class _HpicfHAMgmtModuleRedundancyState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('unavailable',1),(_U,2),('disabled',3),('syncing',4),(_R,5),('hitless',6)))
_HpicfHAMgmtModuleRedundancyState_Type.__name__=_D
_HpicfHAMgmtModuleRedundancyState_Object=MibTableColumn
hpicfHAMgmtModuleRedundancyState=_HpicfHAMgmtModuleRedundancyState_Object((1,3,6,1,4,1,11,2,14,11,1,11,2,5,1,4),_HpicfHAMgmtModuleRedundancyState_Type())
hpicfHAMgmtModuleRedundancyState.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfHAMgmtModuleRedundancyState.setStatus(_B)
class _HpicfHAMgmtModuleBackUpState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('failed',0),(_T,1),('waiting',2),('realtimeBackupToSlot',3),('slotIsAbsent',4),('batchBackup',5),('receivingRealtimeData',6),('offline',7)))
_HpicfHAMgmtModuleBackUpState_Type.__name__=_D
_HpicfHAMgmtModuleBackUpState_Object=MibTableColumn
hpicfHAMgmtModuleBackUpState=_HpicfHAMgmtModuleBackUpState_Object((1,3,6,1,4,1,11,2,14,11,1,11,2,5,1,5),_HpicfHAMgmtModuleBackUpState_Type())
hpicfHAMgmtModuleBackUpState.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfHAMgmtModuleBackUpState.setStatus(_B)
_HpicfHAConformance_ObjectIdentity=ObjectIdentity
hpicfHAConformance=_HpicfHAConformance_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,1,11,3))
_HpicfHACompliances_ObjectIdentity=ObjectIdentity
hpicfHACompliances=_HpicfHACompliances_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,1,11,3,1))
_HpicfHAGroups_ObjectIdentity=ObjectIdentity
hpicfHAGroups=_HpicfHAGroups_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,1,11,3,2))
hpicfHAConfigGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,1,11,3,2,1))
hpicfHAConfigGroup.setObjects(*((_A,_G),(_A,_H)))
if mibBuilder.loadTexts:hpicfHAConfigGroup.setStatus(_E)
hpicfHAStatusGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,1,11,3,2,2))
hpicfHAStatusGroup.setObjects(*((_A,_V),(_A,_W),(_A,_X)))
if mibBuilder.loadTexts:hpicfHAStatusGroup.setStatus(_B)
hpicfHAFailOverGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,1,11,3,2,3))
hpicfHAFailOverGroup.setObjects(*((_A,_Y),(_A,_Z),(_A,_a),(_A,_b)))
if mibBuilder.loadTexts:hpicfHAFailOverGroup.setStatus(_B)
hpicfHAMgmtModuleGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,1,11,3,2,4))
hpicfHAMgmtModuleGroup.setObjects(*((_A,_I),(_A,_J),(_A,_K),(_A,_L)))
if mibBuilder.loadTexts:hpicfHAMgmtModuleGroup.setStatus(_E)
hpicfHAMgmtModuleGroup1=ObjectGroup((1,3,6,1,4,1,11,2,14,11,1,11,3,2,5))
hpicfHAMgmtModuleGroup1.setObjects(*((_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_c)))
if mibBuilder.loadTexts:hpicfHAMgmtModuleGroup1.setStatus(_B)
hpicfHAConfigGroup1=ObjectGroup((1,3,6,1,4,1,11,2,14,11,1,11,3,2,6))
hpicfHAConfigGroup1.setObjects(*((_A,_G),(_A,_H),(_A,_d)))
if mibBuilder.loadTexts:hpicfHAConfigGroup1.setStatus(_B)
hpicfHACompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,1,11,3,1,1))
hpicfHACompliance.setObjects(*((_A,_e),(_A,_M)))
if mibBuilder.loadTexts:hpicfHACompliance.setStatus(_E)
hpicfHACompliance1=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,1,11,3,1,2))
hpicfHACompliance1.setObjects(*((_A,_N),(_A,_f)))
if mibBuilder.loadTexts:hpicfHACompliance1.setStatus(_E)
hpicfHACompliance2=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,1,11,3,1,3))
hpicfHACompliance2.setObjects(*((_A,_N),(_A,_g)))
if mibBuilder.loadTexts:hpicfHACompliance2.setStatus(_B)
hpicfHACompliance3=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,1,11,3,1,4))
hpicfHACompliance3.setObjects(*((_A,_h),(_A,_M)))
if mibBuilder.loadTexts:hpicfHACompliance3.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'hpicfHighAvailability':hpicfHighAvailability,'hpicfHAConfigObjects':hpicfHAConfigObjects,_G:hpicfHARedundancyManagementModuleMode,_H:hpicfHAContinuousFwdingTime,_d:hpicfHAPreferredActiveManagement,'hpicfHAStatusObjects':hpicfHAStatusObjects,_V:hpicfHAMgmtRedundancyFailureReason,_W:hpicfHAMgmtFailovers,_X:hpicfHALastFailoverTime,'hpicfHAFailOverLogTable':hpicfHAFailOverLogTable,'hpicfHAFailOverLogEntry':hpicfHAFailOverLogEntry,_S:hpicfHAFailOverIndex,_Y:hpicfHAFailOverMgmtModule,_Z:hpicfHAFailOverState,_a:hpicfHAFailOverTime,_b:hpicfHAFailOverReason,'hpicfHAMgmtModuleTable':hpicfHAMgmtModuleTable,'hpicfHAMgmtModuleEntry':hpicfHAMgmtModuleEntry,_I:hpicfHAMgmtModuleState,_J:hpicfHAMgmtModuleCardUpSince,_K:hpicfHAMgmtModuleStateSince,_L:hpicfHAMgmtModuleRedundancyState,_c:hpicfHAMgmtModuleBackUpState,'hpicfHAConformance':hpicfHAConformance,'hpicfHACompliances':hpicfHACompliances,'hpicfHACompliance':hpicfHACompliance,'hpicfHACompliance1':hpicfHACompliance1,'hpicfHACompliance2':hpicfHACompliance2,'hpicfHACompliance3':hpicfHACompliance3,'hpicfHAGroups':hpicfHAGroups,_e:hpicfHAConfigGroup,_M:hpicfHAStatusGroup,_N:hpicfHAFailOverGroup,_f:hpicfHAMgmtModuleGroup,_g:hpicfHAMgmtModuleGroup1,_h:hpicfHAConfigGroup1})