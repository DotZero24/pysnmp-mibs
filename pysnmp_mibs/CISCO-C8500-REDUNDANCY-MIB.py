_j='ccrNotificationsGroup'
_i='ccrCpuMibGroup1'
_h='ccrCpuMibGroup'
_g='ccrSwitchModeChange'
_f='ccrSwitchStatusChange'
_e='ccrCpuStatusChange'
_d='ccrSigCounterSyncEnable'
_c='ccrVcCounterSyncFreq'
_b='ccrIfCounterSyncFreq'
_a='ccrForceCounterSync'
_Z='ccrCpuSwitchoverTime'
_Y='ccrCpuStandbyEnableMode'
_X='ccrDesiredSwitchBw'
_W='ccrSwitchBw'
_V='ccrSwitchLastSwitchoverReason'
_U='ccrSwitchLastSwitchoverTime'
_T='obsolete'
_S='twentyGbps'
_R='tenGbps'
_Q='ccrSwitchSlotIndex'
_P='minutes'
_O='not-accessible'
_N='ccrCpuSlotIndex'
_M='notPresent'
_L='TruthValue'
_K='ccrSwitchMibGroup'
_J='ccrSwitchStatus'
_I='ccrSwitchMode'
_H='ccrSyncConfigOnSet'
_G='ccrCpuMode'
_F='ccrCpuStatus'
_E='read-only'
_D='Integer32'
_C='read-write'
_B='current'
_A='CISCO-C8500-REDUNDANCY-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeStamp',_L)
ciscoC8500RedundancyMIB=ModuleIdentity((1,3,6,1,4,1,9,9,105))
if mibBuilder.loadTexts:ciscoC8500RedundancyMIB.setRevisions(('2003-05-04 00:00','1998-06-22 00:00'))
class RedundancyStatus(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_M,1),('ok',2),('fault',3)))
class RedundancyMode(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('active',1),('standby',2),('unused',3),(_M,4)))
class RedundancySlotIndex(TextualConvention,Unsigned32):status=_B;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CiscoC8500RedundancyMIBObjects_ObjectIdentity=ObjectIdentity
ciscoC8500RedundancyMIBObjects=_CiscoC8500RedundancyMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,105,1))
_CcrCpu_ObjectIdentity=ObjectIdentity
ccrCpu=_CcrCpu_ObjectIdentity((1,3,6,1,4,1,9,9,105,1,1))
_CcrCpuTable_Object=MibTable
ccrCpuTable=_CcrCpuTable_Object((1,3,6,1,4,1,9,9,105,1,1,1))
if mibBuilder.loadTexts:ccrCpuTable.setStatus(_B)
_CcrCpuEntry_Object=MibTableRow
ccrCpuEntry=_CcrCpuEntry_Object((1,3,6,1,4,1,9,9,105,1,1,1,1))
ccrCpuEntry.setIndexNames((0,_A,_N))
if mibBuilder.loadTexts:ccrCpuEntry.setStatus(_B)
_CcrCpuSlotIndex_Type=RedundancySlotIndex
_CcrCpuSlotIndex_Object=MibTableColumn
ccrCpuSlotIndex=_CcrCpuSlotIndex_Object((1,3,6,1,4,1,9,9,105,1,1,1,1,1),_CcrCpuSlotIndex_Type())
ccrCpuSlotIndex.setMaxAccess(_O)
if mibBuilder.loadTexts:ccrCpuSlotIndex.setStatus(_B)
_CcrCpuMode_Type=RedundancyMode
_CcrCpuMode_Object=MibTableColumn
ccrCpuMode=_CcrCpuMode_Object((1,3,6,1,4,1,9,9,105,1,1,1,1,2),_CcrCpuMode_Type())
ccrCpuMode.setMaxAccess(_C)
if mibBuilder.loadTexts:ccrCpuMode.setStatus(_B)
_CcrCpuStatus_Type=RedundancyStatus
_CcrCpuStatus_Object=MibTableColumn
ccrCpuStatus=_CcrCpuStatus_Object((1,3,6,1,4,1,9,9,105,1,1,1,1,3),_CcrCpuStatus_Type())
ccrCpuStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:ccrCpuStatus.setStatus(_B)
class _CcrSyncConfigOnSet_Type(Bits):namedValues=NamedValues(*(('runningConfig',0),('startupConfig',1)))
_CcrSyncConfigOnSet_Type.__name__='Bits'
_CcrSyncConfigOnSet_Object=MibScalar
ccrSyncConfigOnSet=_CcrSyncConfigOnSet_Object((1,3,6,1,4,1,9,9,105,1,1,2),_CcrSyncConfigOnSet_Type())
ccrSyncConfigOnSet.setMaxAccess(_C)
if mibBuilder.loadTexts:ccrSyncConfigOnSet.setStatus(_B)
class _CcrCpuStandbyEnableMode_Type(TruthValue):defaultValue=2
_CcrCpuStandbyEnableMode_Type.__name__=_L
_CcrCpuStandbyEnableMode_Object=MibScalar
ccrCpuStandbyEnableMode=_CcrCpuStandbyEnableMode_Object((1,3,6,1,4,1,9,9,105,1,1,3),_CcrCpuStandbyEnableMode_Type())
ccrCpuStandbyEnableMode.setMaxAccess(_C)
if mibBuilder.loadTexts:ccrCpuStandbyEnableMode.setStatus(_B)
class _CcrCpuSwitchoverTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CcrCpuSwitchoverTime_Type.__name__=_D
_CcrCpuSwitchoverTime_Object=MibScalar
ccrCpuSwitchoverTime=_CcrCpuSwitchoverTime_Object((1,3,6,1,4,1,9,9,105,1,1,4),_CcrCpuSwitchoverTime_Type())
ccrCpuSwitchoverTime.setMaxAccess(_E)
if mibBuilder.loadTexts:ccrCpuSwitchoverTime.setStatus(_B)
if mibBuilder.loadTexts:ccrCpuSwitchoverTime.setUnits('seconds')
class _CcrForceCounterSync_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('forcesync',1),('noop',2)))
_CcrForceCounterSync_Type.__name__=_D
_CcrForceCounterSync_Object=MibScalar
ccrForceCounterSync=_CcrForceCounterSync_Object((1,3,6,1,4,1,9,9,105,1,1,5),_CcrForceCounterSync_Type())
ccrForceCounterSync.setMaxAccess(_C)
if mibBuilder.loadTexts:ccrForceCounterSync.setStatus(_B)
class _CcrIfCounterSyncFreq_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1440))
_CcrIfCounterSyncFreq_Type.__name__=_D
_CcrIfCounterSyncFreq_Object=MibScalar
ccrIfCounterSyncFreq=_CcrIfCounterSyncFreq_Object((1,3,6,1,4,1,9,9,105,1,1,6),_CcrIfCounterSyncFreq_Type())
ccrIfCounterSyncFreq.setMaxAccess(_C)
if mibBuilder.loadTexts:ccrIfCounterSyncFreq.setStatus(_B)
if mibBuilder.loadTexts:ccrIfCounterSyncFreq.setUnits(_P)
class _CcrVcCounterSyncFreq_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1440))
_CcrVcCounterSyncFreq_Type.__name__=_D
_CcrVcCounterSyncFreq_Object=MibScalar
ccrVcCounterSyncFreq=_CcrVcCounterSyncFreq_Object((1,3,6,1,4,1,9,9,105,1,1,7),_CcrVcCounterSyncFreq_Type())
ccrVcCounterSyncFreq.setMaxAccess(_C)
if mibBuilder.loadTexts:ccrVcCounterSyncFreq.setStatus(_B)
if mibBuilder.loadTexts:ccrVcCounterSyncFreq.setUnits(_P)
_CcrSigCounterSyncEnable_Type=TruthValue
_CcrSigCounterSyncEnable_Object=MibScalar
ccrSigCounterSyncEnable=_CcrSigCounterSyncEnable_Object((1,3,6,1,4,1,9,9,105,1,1,8),_CcrSigCounterSyncEnable_Type())
ccrSigCounterSyncEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:ccrSigCounterSyncEnable.setStatus(_B)
_CcrSwitch_ObjectIdentity=ObjectIdentity
ccrSwitch=_CcrSwitch_ObjectIdentity((1,3,6,1,4,1,9,9,105,1,2))
_CcrSwitchTable_Object=MibTable
ccrSwitchTable=_CcrSwitchTable_Object((1,3,6,1,4,1,9,9,105,1,2,1))
if mibBuilder.loadTexts:ccrSwitchTable.setStatus(_B)
_CcrSwitchEntry_Object=MibTableRow
ccrSwitchEntry=_CcrSwitchEntry_Object((1,3,6,1,4,1,9,9,105,1,2,1,1))
ccrSwitchEntry.setIndexNames((0,_A,_Q))
if mibBuilder.loadTexts:ccrSwitchEntry.setStatus(_B)
_CcrSwitchSlotIndex_Type=RedundancySlotIndex
_CcrSwitchSlotIndex_Object=MibTableColumn
ccrSwitchSlotIndex=_CcrSwitchSlotIndex_Object((1,3,6,1,4,1,9,9,105,1,2,1,1,1),_CcrSwitchSlotIndex_Type())
ccrSwitchSlotIndex.setMaxAccess(_O)
if mibBuilder.loadTexts:ccrSwitchSlotIndex.setStatus(_B)
_CcrSwitchMode_Type=RedundancyMode
_CcrSwitchMode_Object=MibTableColumn
ccrSwitchMode=_CcrSwitchMode_Object((1,3,6,1,4,1,9,9,105,1,2,1,1,2),_CcrSwitchMode_Type())
ccrSwitchMode.setMaxAccess(_C)
if mibBuilder.loadTexts:ccrSwitchMode.setStatus(_B)
_CcrSwitchStatus_Type=RedundancyStatus
_CcrSwitchStatus_Object=MibTableColumn
ccrSwitchStatus=_CcrSwitchStatus_Object((1,3,6,1,4,1,9,9,105,1,2,1,1,3),_CcrSwitchStatus_Type())
ccrSwitchStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:ccrSwitchStatus.setStatus(_B)
_CcrSwitchLastSwitchoverTime_Type=TimeStamp
_CcrSwitchLastSwitchoverTime_Object=MibScalar
ccrSwitchLastSwitchoverTime=_CcrSwitchLastSwitchoverTime_Object((1,3,6,1,4,1,9,9,105,1,2,2),_CcrSwitchLastSwitchoverTime_Type())
ccrSwitchLastSwitchoverTime.setMaxAccess(_E)
if mibBuilder.loadTexts:ccrSwitchLastSwitchoverTime.setStatus(_B)
class _CcrSwitchLastSwitchoverReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('none',1),('notKnown',2),('userInitiated',3),('cardFailed',4),('cardRecovered',5),('cardRemoved',6),('cardInserted',7)))
_CcrSwitchLastSwitchoverReason_Type.__name__=_D
_CcrSwitchLastSwitchoverReason_Object=MibScalar
ccrSwitchLastSwitchoverReason=_CcrSwitchLastSwitchoverReason_Object((1,3,6,1,4,1,9,9,105,1,2,3),_CcrSwitchLastSwitchoverReason_Type())
ccrSwitchLastSwitchoverReason.setMaxAccess(_E)
if mibBuilder.loadTexts:ccrSwitchLastSwitchoverReason.setStatus(_B)
class _CcrSwitchBw_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_R,1),(_S,2)))
_CcrSwitchBw_Type.__name__=_D
_CcrSwitchBw_Object=MibScalar
ccrSwitchBw=_CcrSwitchBw_Object((1,3,6,1,4,1,9,9,105,1,2,4),_CcrSwitchBw_Type())
ccrSwitchBw.setMaxAccess(_E)
if mibBuilder.loadTexts:ccrSwitchBw.setStatus(_B)
class _CcrDesiredSwitchBw_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_R,1),(_S,2)))
_CcrDesiredSwitchBw_Type.__name__=_D
_CcrDesiredSwitchBw_Object=MibScalar
ccrDesiredSwitchBw=_CcrDesiredSwitchBw_Object((1,3,6,1,4,1,9,9,105,1,2,5),_CcrDesiredSwitchBw_Type())
ccrDesiredSwitchBw.setMaxAccess(_C)
if mibBuilder.loadTexts:ccrDesiredSwitchBw.setStatus(_B)
_CiscoC8500RedundancyMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
ciscoC8500RedundancyMIBNotificationPrefix=_CiscoC8500RedundancyMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,9,9,105,2))
_CcrMIBNotifications_ObjectIdentity=ObjectIdentity
ccrMIBNotifications=_CcrMIBNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,105,2,0))
_CiscoC8500RedundancyMIBConformance_ObjectIdentity=ObjectIdentity
ciscoC8500RedundancyMIBConformance=_CiscoC8500RedundancyMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,105,3))
_CiscoC8500RedundancyMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoC8500RedundancyMIBCompliances=_CiscoC8500RedundancyMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,105,3,1))
_CiscoC8500RedundancyMIBGroups_ObjectIdentity=ObjectIdentity
ciscoC8500RedundancyMIBGroups=_CiscoC8500RedundancyMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,105,3,2))
ccrCpuMibGroup=ObjectGroup((1,3,6,1,4,1,9,9,105,3,2,1))
ccrCpuMibGroup.setObjects(*((_A,_G),(_A,_F),(_A,_H)))
if mibBuilder.loadTexts:ccrCpuMibGroup.setStatus(_T)
ccrSwitchMibGroup=ObjectGroup((1,3,6,1,4,1,9,9,105,3,2,2))
ccrSwitchMibGroup.setObjects(*((_A,_I),(_A,_J),(_A,_U),(_A,_V),(_A,_W),(_A,_X)))
if mibBuilder.loadTexts:ccrSwitchMibGroup.setStatus(_B)
ccrCpuMibGroup1=ObjectGroup((1,3,6,1,4,1,9,9,105,3,2,4))
ccrCpuMibGroup1.setObjects(*((_A,_G),(_A,_F),(_A,_H),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d)))
if mibBuilder.loadTexts:ccrCpuMibGroup1.setStatus(_B)
ccrCpuStatusChange=NotificationType((1,3,6,1,4,1,9,9,105,2,0,1))
ccrCpuStatusChange.setObjects((_A,_F))
if mibBuilder.loadTexts:ccrCpuStatusChange.setStatus(_B)
ccrSwitchStatusChange=NotificationType((1,3,6,1,4,1,9,9,105,2,0,2))
ccrSwitchStatusChange.setObjects((_A,_J))
if mibBuilder.loadTexts:ccrSwitchStatusChange.setStatus(_B)
ccrSwitchModeChange=NotificationType((1,3,6,1,4,1,9,9,105,2,0,3))
ccrSwitchModeChange.setObjects((_A,_I))
if mibBuilder.loadTexts:ccrSwitchModeChange.setStatus(_B)
ccrNotificationsGroup=NotificationGroup((1,3,6,1,4,1,9,9,105,3,2,3))
ccrNotificationsGroup.setObjects(*((_A,_e),(_A,_f),(_A,_g)))
if mibBuilder.loadTexts:ccrNotificationsGroup.setStatus(_B)
ciscoC8500RedundancyMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,105,3,1,1))
ciscoC8500RedundancyMIBCompliance.setObjects(*((_A,_h),(_A,_K)))
if mibBuilder.loadTexts:ciscoC8500RedundancyMIBCompliance.setStatus(_T)
ciscoC8500RedundancyMIBComplianceRev1=ModuleCompliance((1,3,6,1,4,1,9,9,105,3,1,2))
ciscoC8500RedundancyMIBComplianceRev1.setObjects(*((_A,_i),(_A,_K),(_A,_j)))
if mibBuilder.loadTexts:ciscoC8500RedundancyMIBComplianceRev1.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'RedundancyStatus':RedundancyStatus,'RedundancyMode':RedundancyMode,'RedundancySlotIndex':RedundancySlotIndex,'ciscoC8500RedundancyMIB':ciscoC8500RedundancyMIB,'ciscoC8500RedundancyMIBObjects':ciscoC8500RedundancyMIBObjects,'ccrCpu':ccrCpu,'ccrCpuTable':ccrCpuTable,'ccrCpuEntry':ccrCpuEntry,_N:ccrCpuSlotIndex,_G:ccrCpuMode,_F:ccrCpuStatus,_H:ccrSyncConfigOnSet,_Y:ccrCpuStandbyEnableMode,_Z:ccrCpuSwitchoverTime,_a:ccrForceCounterSync,_b:ccrIfCounterSyncFreq,_c:ccrVcCounterSyncFreq,_d:ccrSigCounterSyncEnable,'ccrSwitch':ccrSwitch,'ccrSwitchTable':ccrSwitchTable,'ccrSwitchEntry':ccrSwitchEntry,_Q:ccrSwitchSlotIndex,_I:ccrSwitchMode,_J:ccrSwitchStatus,_U:ccrSwitchLastSwitchoverTime,_V:ccrSwitchLastSwitchoverReason,_W:ccrSwitchBw,_X:ccrDesiredSwitchBw,'ciscoC8500RedundancyMIBNotificationPrefix':ciscoC8500RedundancyMIBNotificationPrefix,'ccrMIBNotifications':ccrMIBNotifications,_e:ccrCpuStatusChange,_f:ccrSwitchStatusChange,_g:ccrSwitchModeChange,'ciscoC8500RedundancyMIBConformance':ciscoC8500RedundancyMIBConformance,'ciscoC8500RedundancyMIBCompliances':ciscoC8500RedundancyMIBCompliances,'ciscoC8500RedundancyMIBCompliance':ciscoC8500RedundancyMIBCompliance,'ciscoC8500RedundancyMIBComplianceRev1':ciscoC8500RedundancyMIBComplianceRev1,'ciscoC8500RedundancyMIBGroups':ciscoC8500RedundancyMIBGroups,_h:ccrCpuMibGroup,_K:ccrSwitchMibGroup,_j:ccrNotificationsGroup,_i:ccrCpuMibGroup1})