_W='notConnected'
_V='undefined'
_U='mrpStatusIndex'
_T='couplingStatusIndex'
_S='statisticsIndex'
_R='statusIndex'
_Q='mrpConfigIndex'
_P='configIndex'
_O='forwarding'
_N='blocking'
_M='unused'
_L='manager'
_K='client'
_J='enabled'
_I='not-accessible'
_H='disabled'
_G='G6-RING-MIB'
_F='true'
_E='false'
_D='read-write'
_C='read-only'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
g6,=mibBuilder.importSymbols('MICROSENS-G6-MIB','g6')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
protocol=ModuleIdentity((1,3,6,1,4,1,3181,10,6,2))
if mibBuilder.loadTexts:protocol.setRevisions(('2018-02-12 16:19',))
_Ring_ObjectIdentity=ObjectIdentity
ring=_Ring_ObjectIdentity((1,3,6,1,4,1,3181,10,6,2,45))
_ConfigTable_Object=MibTable
configTable=_ConfigTable_Object((1,3,6,1,4,1,3181,10,6,2,45,1))
if mibBuilder.loadTexts:configTable.setStatus(_A)
_ConfigEntry_Object=MibTableRow
configEntry=_ConfigEntry_Object((1,3,6,1,4,1,3181,10,6,2,45,1,1))
configEntry.setIndexNames((0,_G,_P))
if mibBuilder.loadTexts:configEntry.setStatus(_A)
class _ConfigIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_ConfigIndex_Type.__name__=_B
_ConfigIndex_Object=MibTableColumn
configIndex=_ConfigIndex_Object((1,3,6,1,4,1,3181,10,6,2,45,1,1,1),_ConfigIndex_Type())
configIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:configIndex.setStatus(_A)
_ConfigName_Type=DisplayString
_ConfigName_Object=MibTableColumn
configName=_ConfigName_Object((1,3,6,1,4,1,3181,10,6,2,45,1,1,2),_ConfigName_Type())
configName.setMaxAccess(_D)
if mibBuilder.loadTexts:configName.setStatus(_A)
class _ConfigEnableRing_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_J,1)))
_ConfigEnableRing_Type.__name__=_B
_ConfigEnableRing_Object=MibTableColumn
configEnableRing=_ConfigEnableRing_Object((1,3,6,1,4,1,3181,10,6,2,45,1,1,3),_ConfigEnableRing_Type())
configEnableRing.setMaxAccess(_D)
if mibBuilder.loadTexts:configEnableRing.setStatus(_A)
class _ConfigRingMaster_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_J,1)))
_ConfigRingMaster_Type.__name__=_B
_ConfigRingMaster_Object=MibTableColumn
configRingMaster=_ConfigRingMaster_Object((1,3,6,1,4,1,3181,10,6,2,45,1,1,4),_ConfigRingMaster_Type())
configRingMaster.setMaxAccess(_D)
if mibBuilder.loadTexts:configRingMaster.setStatus(_A)
class _ConfigNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_ConfigNumber_Type.__name__=_B
_ConfigNumber_Object=MibTableColumn
configNumber=_ConfigNumber_Object((1,3,6,1,4,1,3181,10,6,2,45,1,1,5),_ConfigNumber_Type())
configNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:configNumber.setStatus(_A)
class _ConfigPortA_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ConfigPortA_Type.__name__=_B
_ConfigPortA_Object=MibTableColumn
configPortA=_ConfigPortA_Object((1,3,6,1,4,1,3181,10,6,2,45,1,1,6),_ConfigPortA_Type())
configPortA.setMaxAccess(_D)
if mibBuilder.loadTexts:configPortA.setStatus(_A)
class _ConfigPortB_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ConfigPortB_Type.__name__=_B
_ConfigPortB_Object=MibTableColumn
configPortB=_ConfigPortB_Object((1,3,6,1,4,1,3181,10,6,2,45,1,1,7),_ConfigPortB_Type())
configPortB.setMaxAccess(_D)
if mibBuilder.loadTexts:configPortB.setStatus(_A)
_MrpConfigTable_Object=MibTable
mrpConfigTable=_MrpConfigTable_Object((1,3,6,1,4,1,3181,10,6,2,45,2))
if mibBuilder.loadTexts:mrpConfigTable.setStatus(_A)
_MrpConfigEntry_Object=MibTableRow
mrpConfigEntry=_MrpConfigEntry_Object((1,3,6,1,4,1,3181,10,6,2,45,2,1))
mrpConfigEntry.setIndexNames((0,_G,_Q))
if mibBuilder.loadTexts:mrpConfigEntry.setStatus(_A)
class _MrpConfigIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0))
_MrpConfigIndex_Type.__name__=_B
_MrpConfigIndex_Object=MibTableColumn
mrpConfigIndex=_MrpConfigIndex_Object((1,3,6,1,4,1,3181,10,6,2,45,2,1,1),_MrpConfigIndex_Type())
mrpConfigIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:mrpConfigIndex.setStatus(_A)
class _MrpConfigEnableMrp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_J,1)))
_MrpConfigEnableMrp_Type.__name__=_B
_MrpConfigEnableMrp_Object=MibTableColumn
mrpConfigEnableMrp=_MrpConfigEnableMrp_Object((1,3,6,1,4,1,3181,10,6,2,45,2,1,2),_MrpConfigEnableMrp_Type())
mrpConfigEnableMrp.setMaxAccess(_D)
if mibBuilder.loadTexts:mrpConfigEnableMrp.setStatus(_A)
_MrpConfigDomainName_Type=DisplayString
_MrpConfigDomainName_Object=MibTableColumn
mrpConfigDomainName=_MrpConfigDomainName_Object((1,3,6,1,4,1,3181,10,6,2,45,2,1,3),_MrpConfigDomainName_Type())
mrpConfigDomainName.setMaxAccess(_D)
if mibBuilder.loadTexts:mrpConfigDomainName.setStatus(_A)
class _MrpConfigExpectedRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_MrpConfigExpectedRole_Type.__name__=_B
_MrpConfigExpectedRole_Object=MibTableColumn
mrpConfigExpectedRole=_MrpConfigExpectedRole_Object((1,3,6,1,4,1,3181,10,6,2,45,2,1,4),_MrpConfigExpectedRole_Type())
mrpConfigExpectedRole.setMaxAccess(_D)
if mibBuilder.loadTexts:mrpConfigExpectedRole.setStatus(_A)
class _MrpConfigReactOnLinkChange_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_J,1)))
_MrpConfigReactOnLinkChange_Type.__name__=_B
_MrpConfigReactOnLinkChange_Object=MibTableColumn
mrpConfigReactOnLinkChange=_MrpConfigReactOnLinkChange_Object((1,3,6,1,4,1,3181,10,6,2,45,2,1,5),_MrpConfigReactOnLinkChange_Type())
mrpConfigReactOnLinkChange.setMaxAccess(_D)
if mibBuilder.loadTexts:mrpConfigReactOnLinkChange.setStatus(_A)
class _MrpConfigRecoveryTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('recoveryTime500Ms',0),('recoveryTime200Ms',1)))
_MrpConfigRecoveryTime_Type.__name__=_B
_MrpConfigRecoveryTime_Object=MibTableColumn
mrpConfigRecoveryTime=_MrpConfigRecoveryTime_Object((1,3,6,1,4,1,3181,10,6,2,45,2,1,6),_MrpConfigRecoveryTime_Type())
mrpConfigRecoveryTime.setMaxAccess(_D)
if mibBuilder.loadTexts:mrpConfigRecoveryTime.setStatus(_A)
class _MrpConfigPort1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MrpConfigPort1_Type.__name__=_B
_MrpConfigPort1_Object=MibTableColumn
mrpConfigPort1=_MrpConfigPort1_Object((1,3,6,1,4,1,3181,10,6,2,45,2,1,7),_MrpConfigPort1_Type())
mrpConfigPort1.setMaxAccess(_D)
if mibBuilder.loadTexts:mrpConfigPort1.setStatus(_A)
class _MrpConfigPort2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MrpConfigPort2_Type.__name__=_B
_MrpConfigPort2_Object=MibTableColumn
mrpConfigPort2=_MrpConfigPort2_Object((1,3,6,1,4,1,3181,10,6,2,45,2,1,8),_MrpConfigPort2_Type())
mrpConfigPort2.setMaxAccess(_D)
if mibBuilder.loadTexts:mrpConfigPort2.setStatus(_A)
class _MrpConfigVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MrpConfigVlanId_Type.__name__=_B
_MrpConfigVlanId_Object=MibTableColumn
mrpConfigVlanId=_MrpConfigVlanId_Object((1,3,6,1,4,1,3181,10,6,2,45,2,1,9),_MrpConfigVlanId_Type())
mrpConfigVlanId.setMaxAccess(_D)
if mibBuilder.loadTexts:mrpConfigVlanId.setStatus(_A)
_MrpConfigResetRoundTripDelays_Type=DisplayString
_MrpConfigResetRoundTripDelays_Object=MibTableColumn
mrpConfigResetRoundTripDelays=_MrpConfigResetRoundTripDelays_Object((1,3,6,1,4,1,3181,10,6,2,45,2,1,10),_MrpConfigResetRoundTripDelays_Type())
mrpConfigResetRoundTripDelays.setMaxAccess(_D)
if mibBuilder.loadTexts:mrpConfigResetRoundTripDelays.setStatus(_A)
_MrpConfigResetStatistics_Type=DisplayString
_MrpConfigResetStatistics_Object=MibTableColumn
mrpConfigResetStatistics=_MrpConfigResetStatistics_Object((1,3,6,1,4,1,3181,10,6,2,45,2,1,11),_MrpConfigResetStatistics_Type())
mrpConfigResetStatistics.setMaxAccess(_D)
if mibBuilder.loadTexts:mrpConfigResetStatistics.setStatus(_A)
_StatusTable_Object=MibTable
statusTable=_StatusTable_Object((1,3,6,1,4,1,3181,10,6,2,45,100))
if mibBuilder.loadTexts:statusTable.setStatus(_A)
_StatusEntry_Object=MibTableRow
statusEntry=_StatusEntry_Object((1,3,6,1,4,1,3181,10,6,2,45,100,1))
statusEntry.setIndexNames((0,_G,_R))
if mibBuilder.loadTexts:statusEntry.setStatus(_A)
class _StatusIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_StatusIndex_Type.__name__=_B
_StatusIndex_Object=MibTableColumn
statusIndex=_StatusIndex_Object((1,3,6,1,4,1,3181,10,6,2,45,100,1,1),_StatusIndex_Type())
statusIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:statusIndex.setStatus(_A)
class _StatusState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_M,0),('normal',1),('backup',2),('error',3),('misconfigured',4)))
_StatusState_Type.__name__=_B
_StatusState_Object=MibTableColumn
statusState=_StatusState_Object((1,3,6,1,4,1,3181,10,6,2,45,100,1,2),_StatusState_Type())
statusState.setMaxAccess(_C)
if mibBuilder.loadTexts:statusState.setStatus(_A)
_StatusLastStateChange_Type=DisplayString
_StatusLastStateChange_Object=MibTableColumn
statusLastStateChange=_StatusLastStateChange_Object((1,3,6,1,4,1,3181,10,6,2,45,100,1,3),_StatusLastStateChange_Type())
statusLastStateChange.setMaxAccess(_C)
if mibBuilder.loadTexts:statusLastStateChange.setStatus(_A)
class _StatusRingInterrupt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_StatusRingInterrupt_Type.__name__=_B
_StatusRingInterrupt_Object=MibTableColumn
statusRingInterrupt=_StatusRingInterrupt_Object((1,3,6,1,4,1,3181,10,6,2,45,100,1,4),_StatusRingInterrupt_Type())
statusRingInterrupt.setMaxAccess(_C)
if mibBuilder.loadTexts:statusRingInterrupt.setStatus(_A)
class _StatusGlobalRingAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_StatusGlobalRingAlarm_Type.__name__=_B
_StatusGlobalRingAlarm_Object=MibTableColumn
statusGlobalRingAlarm=_StatusGlobalRingAlarm_Object((1,3,6,1,4,1,3181,10,6,2,45,100,1,5),_StatusGlobalRingAlarm_Type())
statusGlobalRingAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:statusGlobalRingAlarm.setStatus(_A)
class _StatusErrorDetected_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_StatusErrorDetected_Type.__name__=_B
_StatusErrorDetected_Object=MibTableColumn
statusErrorDetected=_StatusErrorDetected_Object((1,3,6,1,4,1,3181,10,6,2,45,100,1,6),_StatusErrorDetected_Type())
statusErrorDetected.setMaxAccess(_C)
if mibBuilder.loadTexts:statusErrorDetected.setStatus(_A)
class _StatusRingPortAInterrupted_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_StatusRingPortAInterrupted_Type.__name__=_B
_StatusRingPortAInterrupted_Object=MibTableColumn
statusRingPortAInterrupted=_StatusRingPortAInterrupted_Object((1,3,6,1,4,1,3181,10,6,2,45,100,1,7),_StatusRingPortAInterrupted_Type())
statusRingPortAInterrupted.setMaxAccess(_C)
if mibBuilder.loadTexts:statusRingPortAInterrupted.setStatus(_A)
class _StatusRingPortBInterrupted_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_StatusRingPortBInterrupted_Type.__name__=_B
_StatusRingPortBInterrupted_Object=MibTableColumn
statusRingPortBInterrupted=_StatusRingPortBInterrupted_Object((1,3,6,1,4,1,3181,10,6,2,45,100,1,8),_StatusRingPortBInterrupted_Type())
statusRingPortBInterrupted.setMaxAccess(_C)
if mibBuilder.loadTexts:statusRingPortBInterrupted.setStatus(_A)
_StatisticsTable_Object=MibTable
statisticsTable=_StatisticsTable_Object((1,3,6,1,4,1,3181,10,6,2,45,101))
if mibBuilder.loadTexts:statisticsTable.setStatus(_A)
_StatisticsEntry_Object=MibTableRow
statisticsEntry=_StatisticsEntry_Object((1,3,6,1,4,1,3181,10,6,2,45,101,1))
statisticsEntry.setIndexNames((0,_G,_S))
if mibBuilder.loadTexts:statisticsEntry.setStatus(_A)
class _StatisticsIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_StatisticsIndex_Type.__name__=_B
_StatisticsIndex_Object=MibTableColumn
statisticsIndex=_StatisticsIndex_Object((1,3,6,1,4,1,3181,10,6,2,45,101,1,1),_StatisticsIndex_Type())
statisticsIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:statisticsIndex.setStatus(_A)
_StatisticsNumberOfBackups_Type=Unsigned32
_StatisticsNumberOfBackups_Object=MibTableColumn
statisticsNumberOfBackups=_StatisticsNumberOfBackups_Object((1,3,6,1,4,1,3181,10,6,2,45,101,1,2),_StatisticsNumberOfBackups_Type())
statisticsNumberOfBackups.setMaxAccess(_C)
if mibBuilder.loadTexts:statisticsNumberOfBackups.setStatus(_A)
_StatisticsCurrentBackupDuration_Type=Counter32
_StatisticsCurrentBackupDuration_Object=MibTableColumn
statisticsCurrentBackupDuration=_StatisticsCurrentBackupDuration_Object((1,3,6,1,4,1,3181,10,6,2,45,101,1,3),_StatisticsCurrentBackupDuration_Type())
statisticsCurrentBackupDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:statisticsCurrentBackupDuration.setStatus(_A)
_StatisticsLastBackupDuration_Type=Counter32
_StatisticsLastBackupDuration_Object=MibTableColumn
statisticsLastBackupDuration=_StatisticsLastBackupDuration_Object((1,3,6,1,4,1,3181,10,6,2,45,101,1,4),_StatisticsLastBackupDuration_Type())
statisticsLastBackupDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:statisticsLastBackupDuration.setStatus(_A)
_StatisticsTotalBackupDuration_Type=Counter32
_StatisticsTotalBackupDuration_Object=MibTableColumn
statisticsTotalBackupDuration=_StatisticsTotalBackupDuration_Object((1,3,6,1,4,1,3181,10,6,2,45,101,1,5),_StatisticsTotalBackupDuration_Type())
statisticsTotalBackupDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:statisticsTotalBackupDuration.setStatus(_A)
_CouplingStatusTable_Object=MibTable
couplingStatusTable=_CouplingStatusTable_Object((1,3,6,1,4,1,3181,10,6,2,45,102))
if mibBuilder.loadTexts:couplingStatusTable.setStatus(_A)
_CouplingStatusEntry_Object=MibTableRow
couplingStatusEntry=_CouplingStatusEntry_Object((1,3,6,1,4,1,3181,10,6,2,45,102,1))
couplingStatusEntry.setIndexNames((0,_G,_T))
if mibBuilder.loadTexts:couplingStatusEntry.setStatus(_A)
class _CouplingStatusIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0))
_CouplingStatusIndex_Type.__name__=_B
_CouplingStatusIndex_Object=MibTableColumn
couplingStatusIndex=_CouplingStatusIndex_Object((1,3,6,1,4,1,3181,10,6,2,45,102,1,1),_CouplingStatusIndex_Type())
couplingStatusIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:couplingStatusIndex.setStatus(_A)
class _CouplingStatusControllerState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_H,0),(_N,1),('link',2),(_O,3),('standby',4)))
_CouplingStatusControllerState_Type.__name__=_B
_CouplingStatusControllerState_Object=MibTableColumn
couplingStatusControllerState=_CouplingStatusControllerState_Object((1,3,6,1,4,1,3181,10,6,2,45,102,1,2),_CouplingStatusControllerState_Type())
couplingStatusControllerState.setMaxAccess(_C)
if mibBuilder.loadTexts:couplingStatusControllerState.setStatus(_A)
class _CouplingStatusCportLink_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_CouplingStatusCportLink_Type.__name__=_B
_CouplingStatusCportLink_Object=MibTableColumn
couplingStatusCportLink=_CouplingStatusCportLink_Object((1,3,6,1,4,1,3181,10,6,2,45,102,1,3),_CouplingStatusCportLink_Type())
couplingStatusCportLink.setMaxAccess(_C)
if mibBuilder.loadTexts:couplingStatusCportLink.setStatus(_A)
class _CouplingStatusCportForward_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_CouplingStatusCportForward_Type.__name__=_B
_CouplingStatusCportForward_Object=MibTableColumn
couplingStatusCportForward=_CouplingStatusCportForward_Object((1,3,6,1,4,1,3181,10,6,2,45,102,1,4),_CouplingStatusCportForward_Type())
couplingStatusCportForward.setMaxAccess(_C)
if mibBuilder.loadTexts:couplingStatusCportForward.setStatus(_A)
class _CouplingStatusCportTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_CouplingStatusCportTimeout_Type.__name__=_B
_CouplingStatusCportTimeout_Object=MibTableColumn
couplingStatusCportTimeout=_CouplingStatusCportTimeout_Object((1,3,6,1,4,1,3181,10,6,2,45,102,1,5),_CouplingStatusCportTimeout_Type())
couplingStatusCportTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:couplingStatusCportTimeout.setStatus(_A)
class _CouplingStatusConnectionValid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_CouplingStatusConnectionValid_Type.__name__=_B
_CouplingStatusConnectionValid_Object=MibTableColumn
couplingStatusConnectionValid=_CouplingStatusConnectionValid_Object((1,3,6,1,4,1,3181,10,6,2,45,102,1,6),_CouplingStatusConnectionValid_Type())
couplingStatusConnectionValid.setMaxAccess(_C)
if mibBuilder.loadTexts:couplingStatusConnectionValid.setStatus(_A)
class _CouplingStatusValidPartnerIp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_CouplingStatusValidPartnerIp_Type.__name__=_B
_CouplingStatusValidPartnerIp_Object=MibTableColumn
couplingStatusValidPartnerIp=_CouplingStatusValidPartnerIp_Object((1,3,6,1,4,1,3181,10,6,2,45,102,1,7),_CouplingStatusValidPartnerIp_Type())
couplingStatusValidPartnerIp.setMaxAccess(_C)
if mibBuilder.loadTexts:couplingStatusValidPartnerIp.setStatus(_A)
class _CouplingStatusValidPartnerId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_CouplingStatusValidPartnerId_Type.__name__=_B
_CouplingStatusValidPartnerId_Object=MibTableColumn
couplingStatusValidPartnerId=_CouplingStatusValidPartnerId_Object((1,3,6,1,4,1,3181,10,6,2,45,102,1,8),_CouplingStatusValidPartnerId_Type())
couplingStatusValidPartnerId.setMaxAccess(_C)
if mibBuilder.loadTexts:couplingStatusValidPartnerId.setStatus(_A)
_MrpStatusTable_Object=MibTable
mrpStatusTable=_MrpStatusTable_Object((1,3,6,1,4,1,3181,10,6,2,45,103))
if mibBuilder.loadTexts:mrpStatusTable.setStatus(_A)
_MrpStatusEntry_Object=MibTableRow
mrpStatusEntry=_MrpStatusEntry_Object((1,3,6,1,4,1,3181,10,6,2,45,103,1))
mrpStatusEntry.setIndexNames((0,_G,_U))
if mibBuilder.loadTexts:mrpStatusEntry.setStatus(_A)
class _MrpStatusIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0))
_MrpStatusIndex_Type.__name__=_B
_MrpStatusIndex_Object=MibTableColumn
mrpStatusIndex=_MrpStatusIndex_Object((1,3,6,1,4,1,3181,10,6,2,45,103,1,1),_MrpStatusIndex_Type())
mrpStatusIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:mrpStatusIndex.setStatus(_A)
class _MrpStatusAdminRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_V,0),(_K,1),(_L,2)))
_MrpStatusAdminRole_Type.__name__=_B
_MrpStatusAdminRole_Object=MibTableColumn
mrpStatusAdminRole=_MrpStatusAdminRole_Object((1,3,6,1,4,1,3181,10,6,2,45,103,1,2),_MrpStatusAdminRole_Type())
mrpStatusAdminRole.setMaxAccess(_C)
if mibBuilder.loadTexts:mrpStatusAdminRole.setStatus(_A)
class _MrpStatusOperationalRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_V,0),(_K,1),(_L,2)))
_MrpStatusOperationalRole_Type.__name__=_B
_MrpStatusOperationalRole_Object=MibTableColumn
mrpStatusOperationalRole=_MrpStatusOperationalRole_Object((1,3,6,1,4,1,3181,10,6,2,45,103,1,3),_MrpStatusOperationalRole_Type())
mrpStatusOperationalRole.setMaxAccess(_C)
if mibBuilder.loadTexts:mrpStatusOperationalRole.setStatus(_A)
class _MrpStatusPortAState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,3,4)));namedValues=NamedValues(*((_M,0),(_N,1),(_O,3),(_W,4)))
_MrpStatusPortAState_Type.__name__=_B
_MrpStatusPortAState_Object=MibTableColumn
mrpStatusPortAState=_MrpStatusPortAState_Object((1,3,6,1,4,1,3181,10,6,2,45,103,1,4),_MrpStatusPortAState_Type())
mrpStatusPortAState.setMaxAccess(_C)
if mibBuilder.loadTexts:mrpStatusPortAState.setStatus(_A)
class _MrpStatusPortBState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,3,4)));namedValues=NamedValues(*((_M,0),(_N,1),(_O,3),(_W,4)))
_MrpStatusPortBState_Type.__name__=_B
_MrpStatusPortBState_Object=MibTableColumn
mrpStatusPortBState=_MrpStatusPortBState_Object((1,3,6,1,4,1,3181,10,6,2,45,103,1,5),_MrpStatusPortBState_Type())
mrpStatusPortBState.setMaxAccess(_C)
if mibBuilder.loadTexts:mrpStatusPortBState.setStatus(_A)
_MrpStatusDomainId_Type=DisplayString
_MrpStatusDomainId_Object=MibTableColumn
mrpStatusDomainId=_MrpStatusDomainId_Object((1,3,6,1,4,1,3181,10,6,2,45,103,1,6),_MrpStatusDomainId_Type())
mrpStatusDomainId.setMaxAccess(_C)
if mibBuilder.loadTexts:mrpStatusDomainId.setStatus(_A)
class _MrpStatusDomainState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_H,0),('ok',1),('ringOpen',2)))
_MrpStatusDomainState_Type.__name__=_B
_MrpStatusDomainState_Object=MibTableColumn
mrpStatusDomainState=_MrpStatusDomainState_Object((1,3,6,1,4,1,3181,10,6,2,45,103,1,7),_MrpStatusDomainState_Type())
mrpStatusDomainState.setMaxAccess(_C)
if mibBuilder.loadTexts:mrpStatusDomainState.setStatus(_A)
class _MrpStatusDomainError_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*((_H,0),('noError',1),('invalidVlan',2),('invalid',3),('multiMgr',4),('singleSide',5),('linkError',6)))
_MrpStatusDomainError_Type.__name__=_B
_MrpStatusDomainError_Object=MibTableColumn
mrpStatusDomainError=_MrpStatusDomainError_Object((1,3,6,1,4,1,3181,10,6,2,45,103,1,8),_MrpStatusDomainError_Type())
mrpStatusDomainError.setMaxAccess(_C)
if mibBuilder.loadTexts:mrpStatusDomainError.setStatus(_A)
class _MrpStatusDomainBlocked_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_MrpStatusDomainBlocked_Type.__name__=_B
_MrpStatusDomainBlocked_Object=MibTableColumn
mrpStatusDomainBlocked=_MrpStatusDomainBlocked_Object((1,3,6,1,4,1,3181,10,6,2,45,103,1,9),_MrpStatusDomainBlocked_Type())
mrpStatusDomainBlocked.setMaxAccess(_C)
if mibBuilder.loadTexts:mrpStatusDomainBlocked.setStatus(_A)
_MrpStatusManagerPriority_Type=Unsigned32
_MrpStatusManagerPriority_Object=MibTableColumn
mrpStatusManagerPriority=_MrpStatusManagerPriority_Object((1,3,6,1,4,1,3181,10,6,2,45,103,1,10),_MrpStatusManagerPriority_Type())
mrpStatusManagerPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:mrpStatusManagerPriority.setStatus(_A)
_MrpStatusRingOpenCount_Type=Unsigned32
_MrpStatusRingOpenCount_Object=MibTableColumn
mrpStatusRingOpenCount=_MrpStatusRingOpenCount_Object((1,3,6,1,4,1,3181,10,6,2,45,103,1,11),_MrpStatusRingOpenCount_Type())
mrpStatusRingOpenCount.setMaxAccess(_C)
if mibBuilder.loadTexts:mrpStatusRingOpenCount.setStatus(_A)
_MrpStatusLastRingOpenTimeStamp_Type=Counter32
_MrpStatusLastRingOpenTimeStamp_Object=MibTableColumn
mrpStatusLastRingOpenTimeStamp=_MrpStatusLastRingOpenTimeStamp_Object((1,3,6,1,4,1,3181,10,6,2,45,103,1,12),_MrpStatusLastRingOpenTimeStamp_Type())
mrpStatusLastRingOpenTimeStamp.setMaxAccess(_C)
if mibBuilder.loadTexts:mrpStatusLastRingOpenTimeStamp.setStatus(_A)
_MrpStatusMaxRoundTripDelay_Type=Unsigned32
_MrpStatusMaxRoundTripDelay_Object=MibTableColumn
mrpStatusMaxRoundTripDelay=_MrpStatusMaxRoundTripDelay_Object((1,3,6,1,4,1,3181,10,6,2,45,103,1,13),_MrpStatusMaxRoundTripDelay_Type())
mrpStatusMaxRoundTripDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:mrpStatusMaxRoundTripDelay.setStatus(_A)
_MrpStatusMinRoundTripDelay_Type=Unsigned32
_MrpStatusMinRoundTripDelay_Object=MibTableColumn
mrpStatusMinRoundTripDelay=_MrpStatusMinRoundTripDelay_Object((1,3,6,1,4,1,3181,10,6,2,45,103,1,14),_MrpStatusMinRoundTripDelay_Type())
mrpStatusMinRoundTripDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:mrpStatusMinRoundTripDelay.setStatus(_A)
mibBuilder.exportSymbols(_G,**{'protocol':protocol,'ring':ring,'configTable':configTable,'configEntry':configEntry,_P:configIndex,'configName':configName,'configEnableRing':configEnableRing,'configRingMaster':configRingMaster,'configNumber':configNumber,'configPortA':configPortA,'configPortB':configPortB,'mrpConfigTable':mrpConfigTable,'mrpConfigEntry':mrpConfigEntry,_Q:mrpConfigIndex,'mrpConfigEnableMrp':mrpConfigEnableMrp,'mrpConfigDomainName':mrpConfigDomainName,'mrpConfigExpectedRole':mrpConfigExpectedRole,'mrpConfigReactOnLinkChange':mrpConfigReactOnLinkChange,'mrpConfigRecoveryTime':mrpConfigRecoveryTime,'mrpConfigPort1':mrpConfigPort1,'mrpConfigPort2':mrpConfigPort2,'mrpConfigVlanId':mrpConfigVlanId,'mrpConfigResetRoundTripDelays':mrpConfigResetRoundTripDelays,'mrpConfigResetStatistics':mrpConfigResetStatistics,'statusTable':statusTable,'statusEntry':statusEntry,_R:statusIndex,'statusState':statusState,'statusLastStateChange':statusLastStateChange,'statusRingInterrupt':statusRingInterrupt,'statusGlobalRingAlarm':statusGlobalRingAlarm,'statusErrorDetected':statusErrorDetected,'statusRingPortAInterrupted':statusRingPortAInterrupted,'statusRingPortBInterrupted':statusRingPortBInterrupted,'statisticsTable':statisticsTable,'statisticsEntry':statisticsEntry,_S:statisticsIndex,'statisticsNumberOfBackups':statisticsNumberOfBackups,'statisticsCurrentBackupDuration':statisticsCurrentBackupDuration,'statisticsLastBackupDuration':statisticsLastBackupDuration,'statisticsTotalBackupDuration':statisticsTotalBackupDuration,'couplingStatusTable':couplingStatusTable,'couplingStatusEntry':couplingStatusEntry,_T:couplingStatusIndex,'couplingStatusControllerState':couplingStatusControllerState,'couplingStatusCportLink':couplingStatusCportLink,'couplingStatusCportForward':couplingStatusCportForward,'couplingStatusCportTimeout':couplingStatusCportTimeout,'couplingStatusConnectionValid':couplingStatusConnectionValid,'couplingStatusValidPartnerIp':couplingStatusValidPartnerIp,'couplingStatusValidPartnerId':couplingStatusValidPartnerId,'mrpStatusTable':mrpStatusTable,'mrpStatusEntry':mrpStatusEntry,_U:mrpStatusIndex,'mrpStatusAdminRole':mrpStatusAdminRole,'mrpStatusOperationalRole':mrpStatusOperationalRole,'mrpStatusPortAState':mrpStatusPortAState,'mrpStatusPortBState':mrpStatusPortBState,'mrpStatusDomainId':mrpStatusDomainId,'mrpStatusDomainState':mrpStatusDomainState,'mrpStatusDomainError':mrpStatusDomainError,'mrpStatusDomainBlocked':mrpStatusDomainBlocked,'mrpStatusManagerPriority':mrpStatusManagerPriority,'mrpStatusRingOpenCount':mrpStatusRingOpenCount,'mrpStatusLastRingOpenTimeStamp':mrpStatusLastRingOpenTimeStamp,'mrpStatusMaxRoundTripDelay':mrpStatusMaxRoundTripDelay,'mrpStatusMinRoundTripDelay':mrpStatusMinRoundTripDelay})