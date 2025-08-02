_O='agentNsfLastStartupReason'
_N='agentNsfUnitEntry'
_M='always'
_L='planned'
_K='unknown'
_J='agentInventoryUnitNumber'
_I='NETGEAR-INVENTORY-MIB'
_H='NETGEAR-NSF-MIB'
_G='none'
_F='disable'
_E='enable'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
agentInventoryUnitEntry,agentInventoryUnitNumber=mibBuilder.importSymbols(_I,'agentInventoryUnitEntry',_J)
ng7000managedswitch,=mibBuilder.importSymbols('NETGEAR-REF-MIB','ng7000managedswitch')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
fastPathNsf=ModuleIdentity((1,3,6,1,4,1,4526,10,46))
if mibBuilder.loadTexts:fastPathNsf.setRevisions(('2011-01-26 00:00','2009-04-23 00:00'))
_AgentNsfTraps_ObjectIdentity=ObjectIdentity
agentNsfTraps=_AgentNsfTraps_ObjectIdentity((1,3,6,1,4,1,4526,10,46,0))
_AgentNsfUnitTable_Object=MibTable
agentNsfUnitTable=_AgentNsfUnitTable_Object((1,3,6,1,4,1,4526,10,46,1))
if mibBuilder.loadTexts:agentNsfUnitTable.setStatus(_A)
_AgentNsfUnitEntry_Object=MibTableRow
agentNsfUnitEntry=_AgentNsfUnitEntry_Object((1,3,6,1,4,1,4526,10,46,1,1))
if mibBuilder.loadTexts:agentNsfUnitEntry.setStatus(_A)
_AgentNsfUnitSupport_Type=TruthValue
_AgentNsfUnitSupport_Object=MibTableColumn
agentNsfUnitSupport=_AgentNsfUnitSupport_Object((1,3,6,1,4,1,4526,10,46,1,1,1),_AgentNsfUnitSupport_Type())
agentNsfUnitSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:agentNsfUnitSupport.setStatus(_A)
_AgentNsfGroup_ObjectIdentity=ObjectIdentity
agentNsfGroup=_AgentNsfGroup_ObjectIdentity((1,3,6,1,4,1,4526,10,46,2))
class _AgentNsfAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AgentNsfAdminStatus_Type.__name__=_C
_AgentNsfAdminStatus_Object=MibScalar
agentNsfAdminStatus=_AgentNsfAdminStatus_Object((1,3,6,1,4,1,4526,10,46,2,1),_AgentNsfAdminStatus_Type())
agentNsfAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:agentNsfAdminStatus.setStatus(_A)
class _AgentNsfOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AgentNsfOperStatus_Type.__name__=_C
_AgentNsfOperStatus_Object=MibScalar
agentNsfOperStatus=_AgentNsfOperStatus_Object((1,3,6,1,4,1,4526,10,46,2,2),_AgentNsfOperStatus_Type())
agentNsfOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:agentNsfOperStatus.setStatus(_A)
class _AgentNsfLastStartupReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_K,1),('power-on',2),('warm-admin-move',3),('cold-admin-move',4),('warm-auto-restart',5),('cold-auto-restart',6)))
_AgentNsfLastStartupReason_Type.__name__=_C
_AgentNsfLastStartupReason_Object=MibScalar
agentNsfLastStartupReason=_AgentNsfLastStartupReason_Object((1,3,6,1,4,1,4526,10,46,2,3),_AgentNsfLastStartupReason_Type())
agentNsfLastStartupReason.setMaxAccess(_B)
if mibBuilder.loadTexts:agentNsfLastStartupReason.setStatus(_A)
_AgentNsfTimeSinceLastRestart_Type=TimeTicks
_AgentNsfTimeSinceLastRestart_Object=MibScalar
agentNsfTimeSinceLastRestart=_AgentNsfTimeSinceLastRestart_Object((1,3,6,1,4,1,4526,10,46,2,4),_AgentNsfTimeSinceLastRestart_Type())
agentNsfTimeSinceLastRestart.setMaxAccess(_B)
if mibBuilder.loadTexts:agentNsfTimeSinceLastRestart.setStatus(_A)
_AgentNsfRestartInProgress_Type=TruthValue
_AgentNsfRestartInProgress_Object=MibScalar
agentNsfRestartInProgress=_AgentNsfRestartInProgress_Object((1,3,6,1,4,1,4526,10,46,2,5),_AgentNsfRestartInProgress_Type())
agentNsfRestartInProgress.setMaxAccess(_B)
if mibBuilder.loadTexts:agentNsfRestartInProgress.setStatus(_A)
_AgentNsfWarmRestartReady_Type=TruthValue
_AgentNsfWarmRestartReady_Object=MibScalar
agentNsfWarmRestartReady=_AgentNsfWarmRestartReady_Object((1,3,6,1,4,1,4526,10,46,2,6),_AgentNsfWarmRestartReady_Type())
agentNsfWarmRestartReady.setMaxAccess(_B)
if mibBuilder.loadTexts:agentNsfWarmRestartReady.setStatus(_A)
_AgentNsfBackupConfigurationAge_Type=TimeTicks
_AgentNsfBackupConfigurationAge_Object=MibScalar
agentNsfBackupConfigurationAge=_AgentNsfBackupConfigurationAge_Object((1,3,6,1,4,1,4526,10,46,2,7),_AgentNsfBackupConfigurationAge_Type())
agentNsfBackupConfigurationAge.setMaxAccess(_B)
if mibBuilder.loadTexts:agentNsfBackupConfigurationAge.setStatus(_A)
class _AgentNsfInitiateFailover_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AgentNsfInitiateFailover_Type.__name__=_C
_AgentNsfInitiateFailover_Object=MibScalar
agentNsfInitiateFailover=_AgentNsfInitiateFailover_Object((1,3,6,1,4,1,4526,10,46,2,8),_AgentNsfInitiateFailover_Type())
agentNsfInitiateFailover.setMaxAccess(_D)
if mibBuilder.loadTexts:agentNsfInitiateFailover.setStatus(_A)
_AgentCheckpointStatsGroup_ObjectIdentity=ObjectIdentity
agentCheckpointStatsGroup=_AgentCheckpointStatsGroup_ObjectIdentity((1,3,6,1,4,1,4526,10,46,3))
class _AgentCheckpointClearStatistics_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AgentCheckpointClearStatistics_Type.__name__=_C
_AgentCheckpointClearStatistics_Object=MibScalar
agentCheckpointClearStatistics=_AgentCheckpointClearStatistics_Object((1,3,6,1,4,1,4526,10,46,3,1),_AgentCheckpointClearStatistics_Type())
agentCheckpointClearStatistics.setMaxAccess(_D)
if mibBuilder.loadTexts:agentCheckpointClearStatistics.setStatus(_A)
_AgentCheckpointMessages_Type=Counter32
_AgentCheckpointMessages_Object=MibScalar
agentCheckpointMessages=_AgentCheckpointMessages_Object((1,3,6,1,4,1,4526,10,46,3,2),_AgentCheckpointMessages_Type())
agentCheckpointMessages.setMaxAccess(_B)
if mibBuilder.loadTexts:agentCheckpointMessages.setStatus(_A)
_AgentCheckpointBytes_Type=Counter32
_AgentCheckpointBytes_Object=MibScalar
agentCheckpointBytes=_AgentCheckpointBytes_Object((1,3,6,1,4,1,4526,10,46,3,3),_AgentCheckpointBytes_Type())
agentCheckpointBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:agentCheckpointBytes.setStatus(_A)
_AgentCheckpointTimeSinceCountersCleared_Type=TimeTicks
_AgentCheckpointTimeSinceCountersCleared_Object=MibScalar
agentCheckpointTimeSinceCountersCleared=_AgentCheckpointTimeSinceCountersCleared_Object((1,3,6,1,4,1,4526,10,46,3,4),_AgentCheckpointTimeSinceCountersCleared_Type())
agentCheckpointTimeSinceCountersCleared.setMaxAccess(_B)
if mibBuilder.loadTexts:agentCheckpointTimeSinceCountersCleared.setStatus(_A)
_AgentCheckpointMessageRateInterval_Type=Unsigned32
_AgentCheckpointMessageRateInterval_Object=MibScalar
agentCheckpointMessageRateInterval=_AgentCheckpointMessageRateInterval_Object((1,3,6,1,4,1,4526,10,46,3,5),_AgentCheckpointMessageRateInterval_Type())
agentCheckpointMessageRateInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:agentCheckpointMessageRateInterval.setStatus(_A)
if mibBuilder.loadTexts:agentCheckpointMessageRateInterval.setUnits('seconds')
_AgentCheckpointMessageRate_Type=Gauge32
_AgentCheckpointMessageRate_Object=MibScalar
agentCheckpointMessageRate=_AgentCheckpointMessageRate_Object((1,3,6,1,4,1,4526,10,46,3,6),_AgentCheckpointMessageRate_Type())
agentCheckpointMessageRate.setMaxAccess(_B)
if mibBuilder.loadTexts:agentCheckpointMessageRate.setStatus(_A)
_AgentCheckpointHighestMessageRate_Type=Gauge32
_AgentCheckpointHighestMessageRate_Object=MibScalar
agentCheckpointHighestMessageRate=_AgentCheckpointHighestMessageRate_Object((1,3,6,1,4,1,4526,10,46,3,7),_AgentCheckpointHighestMessageRate_Type())
agentCheckpointHighestMessageRate.setMaxAccess(_B)
if mibBuilder.loadTexts:agentCheckpointHighestMessageRate.setStatus(_A)
_AgentNsfOspfGroup_ObjectIdentity=ObjectIdentity
agentNsfOspfGroup=_AgentNsfOspfGroup_ObjectIdentity((1,3,6,1,4,1,4526,10,46,4))
class _AgentNsfOspfSupportMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_L,2),(_M,3)))
_AgentNsfOspfSupportMode_Type.__name__=_C
_AgentNsfOspfSupportMode_Object=MibScalar
agentNsfOspfSupportMode=_AgentNsfOspfSupportMode_Object((1,3,6,1,4,1,4526,10,46,4,1),_AgentNsfOspfSupportMode_Type())
agentNsfOspfSupportMode.setMaxAccess(_D)
if mibBuilder.loadTexts:agentNsfOspfSupportMode.setStatus(_A)
_AgentNsfOspfRestartInterval_Type=Unsigned32
_AgentNsfOspfRestartInterval_Object=MibScalar
agentNsfOspfRestartInterval=_AgentNsfOspfRestartInterval_Object((1,3,6,1,4,1,4526,10,46,4,2),_AgentNsfOspfRestartInterval_Type())
agentNsfOspfRestartInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:agentNsfOspfRestartInterval.setStatus(_A)
class _AgentNsfOspfRestartStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_K,1),('not-restarting',2),('planned-restart',3),('unplanned-restart',4)))
_AgentNsfOspfRestartStatus_Type.__name__=_C
_AgentNsfOspfRestartStatus_Object=MibScalar
agentNsfOspfRestartStatus=_AgentNsfOspfRestartStatus_Object((1,3,6,1,4,1,4526,10,46,4,3),_AgentNsfOspfRestartStatus_Type())
agentNsfOspfRestartStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:agentNsfOspfRestartStatus.setStatus(_A)
_AgentNsfOspfRestartAge_Type=TimeTicks
_AgentNsfOspfRestartAge_Object=MibScalar
agentNsfOspfRestartAge=_AgentNsfOspfRestartAge_Object((1,3,6,1,4,1,4526,10,46,4,4),_AgentNsfOspfRestartAge_Type())
agentNsfOspfRestartAge.setMaxAccess(_B)
if mibBuilder.loadTexts:agentNsfOspfRestartAge.setStatus(_A)
class _AgentNsfOspfRestartExitReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_G,1),('in-progress',2),('completed',3),('timed-out',4),('topology-change',5),('manual-clear',6)))
_AgentNsfOspfRestartExitReason_Type.__name__=_C
_AgentNsfOspfRestartExitReason_Object=MibScalar
agentNsfOspfRestartExitReason=_AgentNsfOspfRestartExitReason_Object((1,3,6,1,4,1,4526,10,46,4,5),_AgentNsfOspfRestartExitReason_Type())
agentNsfOspfRestartExitReason.setMaxAccess(_B)
if mibBuilder.loadTexts:agentNsfOspfRestartExitReason.setStatus(_A)
class _AgentNsfOspfHelperSupportMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_L,2),(_M,3)))
_AgentNsfOspfHelperSupportMode_Type.__name__=_C
_AgentNsfOspfHelperSupportMode_Object=MibScalar
agentNsfOspfHelperSupportMode=_AgentNsfOspfHelperSupportMode_Object((1,3,6,1,4,1,4526,10,46,4,6),_AgentNsfOspfHelperSupportMode_Type())
agentNsfOspfHelperSupportMode.setMaxAccess(_D)
if mibBuilder.loadTexts:agentNsfOspfHelperSupportMode.setStatus(_A)
class _AgentNsfOspfHelperStrictLSAChecking_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AgentNsfOspfHelperStrictLSAChecking_Type.__name__=_C
_AgentNsfOspfHelperStrictLSAChecking_Object=MibScalar
agentNsfOspfHelperStrictLSAChecking=_AgentNsfOspfHelperStrictLSAChecking_Object((1,3,6,1,4,1,4526,10,46,4,7),_AgentNsfOspfHelperStrictLSAChecking_Type())
agentNsfOspfHelperStrictLSAChecking.setMaxAccess(_D)
if mibBuilder.loadTexts:agentNsfOspfHelperStrictLSAChecking.setStatus(_A)
agentInventoryUnitEntry.registerAugmentions((_H,_N))
agentNsfUnitEntry.setIndexNames(*agentInventoryUnitEntry.getIndexNames())
agentNsfStackRestartComplete=NotificationType((1,3,6,1,4,1,4526,10,46,0,1))
agentNsfStackRestartComplete.setObjects(*((_I,_J),(_H,_O)))
if mibBuilder.loadTexts:agentNsfStackRestartComplete.setStatus(_A)
mibBuilder.exportSymbols(_H,**{'fastPathNsf':fastPathNsf,'agentNsfTraps':agentNsfTraps,'agentNsfStackRestartComplete':agentNsfStackRestartComplete,'agentNsfUnitTable':agentNsfUnitTable,_N:agentNsfUnitEntry,'agentNsfUnitSupport':agentNsfUnitSupport,'agentNsfGroup':agentNsfGroup,'agentNsfAdminStatus':agentNsfAdminStatus,'agentNsfOperStatus':agentNsfOperStatus,_O:agentNsfLastStartupReason,'agentNsfTimeSinceLastRestart':agentNsfTimeSinceLastRestart,'agentNsfRestartInProgress':agentNsfRestartInProgress,'agentNsfWarmRestartReady':agentNsfWarmRestartReady,'agentNsfBackupConfigurationAge':agentNsfBackupConfigurationAge,'agentNsfInitiateFailover':agentNsfInitiateFailover,'agentCheckpointStatsGroup':agentCheckpointStatsGroup,'agentCheckpointClearStatistics':agentCheckpointClearStatistics,'agentCheckpointMessages':agentCheckpointMessages,'agentCheckpointBytes':agentCheckpointBytes,'agentCheckpointTimeSinceCountersCleared':agentCheckpointTimeSinceCountersCleared,'agentCheckpointMessageRateInterval':agentCheckpointMessageRateInterval,'agentCheckpointMessageRate':agentCheckpointMessageRate,'agentCheckpointHighestMessageRate':agentCheckpointHighestMessageRate,'agentNsfOspfGroup':agentNsfOspfGroup,'agentNsfOspfSupportMode':agentNsfOspfSupportMode,'agentNsfOspfRestartInterval':agentNsfOspfRestartInterval,'agentNsfOspfRestartStatus':agentNsfOspfRestartStatus,'agentNsfOspfRestartAge':agentNsfOspfRestartAge,'agentNsfOspfRestartExitReason':agentNsfOspfRestartExitReason,'agentNsfOspfHelperSupportMode':agentNsfOspfHelperSupportMode,'agentNsfOspfHelperStrictLSAChecking':agentNsfOspfHelperStrictLSAChecking})