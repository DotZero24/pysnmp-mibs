_j='uxEthernetPortCurrentIndex'
_i='uxEthernetPortInterval'
_h='uxEthernetPortIntervalIndex'
_g='uxSIPRegistrationsIntervalNumber'
_f='uxSIPRegistrationsIntervalIndex'
_e='uxSIPRegistrationsCurrentIndex'
_d='uxLicenseIntervalNumber'
_c='uxCallRtTotalEntryIndex'
_b='uxCallRtTotalTablesIndex'
_a='uxCallRtIntervalNumber'
_Z='uxCallRtIntervalEntryIndex'
_Y='uxCallRtIntervalTablesIndex'
_X='uxCallRtCurrentEntryIndex'
_W='uxCallRtCurrentTablesIndex'
_V='uxSGIntervalNumber'
_U='uxSGIntervalIndex'
_T='uxSGCurrentIndex'
_S='uxChChannelNumber'
_R='uxChPortNumber'
_Q='uxChSlotNumber'
_P='uxChShelfNumber'
_O='uxSipServerIndex'
_N='uxSGIndex'
_M='uxSGEntryIndex'
_L='uxCallRtIndex'
_K='uxCallRtTablesIndex'
_J='uxCallRtTablesTableIndex'
_I='uxPTIndex'
_H='DisplayString'
_G='enabled'
_F='disabled'
_E='not-accessible'
_D='UX-CALL-STATS-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
PerfCurrentCount,PerfIntervalCount,PerfTotalCount=mibBuilder.importSymbols('PerfHist-TC-MIB','PerfCurrentCount','PerfIntervalCount','PerfTotalCount')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_H,'PhysAddress','TextualConvention')
ux=ModuleIdentity((1,3,6,1,4,1,177,15))
if mibBuilder.loadTexts:ux.setRevisions(('2009-11-04 17:05',))
_Net_ObjectIdentity=ObjectIdentity
net=_Net_ObjectIdentity((1,3,6,1,4,1,177))
_UxObjects_ObjectIdentity=ObjectIdentity
uxObjects=_UxObjects_ObjectIdentity((1,3,6,1,4,1,177,15,1))
_IpSystem_ObjectIdentity=ObjectIdentity
ipSystem=_IpSystem_ObjectIdentity((1,3,6,1,4,1,177,15,1,4))
_SysVersion_Type=DisplayString
_SysVersion_Object=MibScalar
sysVersion=_SysVersion_Object((1,3,6,1,4,1,177,15,1,4,1),_SysVersion_Type())
sysVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:sysVersion.setStatus(_A)
_SysBuildNumber_Type=DisplayString
_SysBuildNumber_Object=MibScalar
sysBuildNumber=_SysBuildNumber_Object((1,3,6,1,4,1,177,15,1,4,2),_SysBuildNumber_Type())
sysBuildNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:sysBuildNumber.setStatus(_A)
_IpTelephony_ObjectIdentity=ObjectIdentity
ipTelephony=_IpTelephony_ObjectIdentity((1,3,6,1,4,1,177,15,1,5))
_CallStatistics_ObjectIdentity=ObjectIdentity
callStatistics=_CallStatistics_ObjectIdentity((1,3,6,1,4,1,177,15,1,5,1))
_UxPortTable_Object=MibTable
uxPortTable=_UxPortTable_Object((1,3,6,1,4,1,177,15,1,5,1,2))
if mibBuilder.loadTexts:uxPortTable.setStatus(_A)
_UxPortEntry_Object=MibTableRow
uxPortEntry=_UxPortEntry_Object((1,3,6,1,4,1,177,15,1,5,1,2,1))
uxPortEntry.setIndexNames((0,_D,_I))
if mibBuilder.loadTexts:uxPortEntry.setStatus(_A)
_UxPTIndex_Type=Unsigned32
_UxPTIndex_Object=MibTableColumn
uxPTIndex=_UxPTIndex_Object((1,3,6,1,4,1,177,15,1,5,1,2,1,1),_UxPTIndex_Type())
uxPTIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:uxPTIndex.setStatus(_A)
_UxPTShelf_Type=Unsigned32
_UxPTShelf_Object=MibTableColumn
uxPTShelf=_UxPTShelf_Object((1,3,6,1,4,1,177,15,1,5,1,2,1,2),_UxPTShelf_Type())
uxPTShelf.setMaxAccess(_B)
if mibBuilder.loadTexts:uxPTShelf.setStatus(_A)
_UxPTSlot_Type=Unsigned32
_UxPTSlot_Object=MibTableColumn
uxPTSlot=_UxPTSlot_Object((1,3,6,1,4,1,177,15,1,5,1,2,1,3),_UxPTSlot_Type())
uxPTSlot.setMaxAccess(_B)
if mibBuilder.loadTexts:uxPTSlot.setStatus(_A)
_UxPTPort_Type=Unsigned32
_UxPTPort_Object=MibTableColumn
uxPTPort=_UxPTPort_Object((1,3,6,1,4,1,177,15,1,5,1,2,1,4),_UxPTPort_Type())
uxPTPort.setMaxAccess(_B)
if mibBuilder.loadTexts:uxPTPort.setStatus(_A)
_UxPTCurrentCalls_Type=Gauge32
_UxPTCurrentCalls_Object=MibTableColumn
uxPTCurrentCalls=_UxPTCurrentCalls_Object((1,3,6,1,4,1,177,15,1,5,1,2,1,5),_UxPTCurrentCalls_Type())
uxPTCurrentCalls.setMaxAccess(_B)
if mibBuilder.loadTexts:uxPTCurrentCalls.setStatus(_A)
_UxPTTotalCalls_Type=Counter32
_UxPTTotalCalls_Object=MibTableColumn
uxPTTotalCalls=_UxPTTotalCalls_Object((1,3,6,1,4,1,177,15,1,5,1,2,1,6),_UxPTTotalCalls_Type())
uxPTTotalCalls.setMaxAccess(_B)
if mibBuilder.loadTexts:uxPTTotalCalls.setStatus(_A)
_UxPTConnectedCalls_Type=Counter32
_UxPTConnectedCalls_Object=MibTableColumn
uxPTConnectedCalls=_UxPTConnectedCalls_Object((1,3,6,1,4,1,177,15,1,5,1,2,1,7),_UxPTConnectedCalls_Type())
uxPTConnectedCalls.setMaxAccess(_B)
if mibBuilder.loadTexts:uxPTConnectedCalls.setStatus(_A)
_UxPTRefusedCalls_Type=Counter32
_UxPTRefusedCalls_Object=MibTableColumn
uxPTRefusedCalls=_UxPTRefusedCalls_Object((1,3,6,1,4,1,177,15,1,5,1,2,1,8),_UxPTRefusedCalls_Type())
uxPTRefusedCalls.setMaxAccess(_B)
if mibBuilder.loadTexts:uxPTRefusedCalls.setStatus(_A)
_UxPTErroredCalls_Type=Counter32
_UxPTErroredCalls_Object=MibTableColumn
uxPTErroredCalls=_UxPTErroredCalls_Object((1,3,6,1,4,1,177,15,1,5,1,2,1,9),_UxPTErroredCalls_Type())
uxPTErroredCalls.setMaxAccess(_B)
if mibBuilder.loadTexts:uxPTErroredCalls.setStatus(_A)
_UxPTEgressCallAttempts_Type=Counter32
_UxPTEgressCallAttempts_Object=MibTableColumn
uxPTEgressCallAttempts=_UxPTEgressCallAttempts_Object((1,3,6,1,4,1,177,15,1,5,1,2,1,10),_UxPTEgressCallAttempts_Type())
uxPTEgressCallAttempts.setMaxAccess(_B)
if mibBuilder.loadTexts:uxPTEgressCallAttempts.setStatus(_A)
_UxPTEgressCallsAccepted_Type=Counter32
_UxPTEgressCallsAccepted_Object=MibTableColumn
uxPTEgressCallsAccepted=_UxPTEgressCallsAccepted_Object((1,3,6,1,4,1,177,15,1,5,1,2,1,11),_UxPTEgressCallsAccepted_Type())
uxPTEgressCallsAccepted.setMaxAccess(_B)
if mibBuilder.loadTexts:uxPTEgressCallsAccepted.setStatus(_A)
_UxPTEgressCallsCompleted_Type=Counter32
_UxPTEgressCallsCompleted_Object=MibTableColumn
uxPTEgressCallsCompleted=_UxPTEgressCallsCompleted_Object((1,3,6,1,4,1,177,15,1,5,1,2,1,12),_UxPTEgressCallsCompleted_Type())
uxPTEgressCallsCompleted.setMaxAccess(_B)
if mibBuilder.loadTexts:uxPTEgressCallsCompleted.setStatus(_A)
_UxPTEgressCallsRejected_Type=Counter32
_UxPTEgressCallsRejected_Object=MibTableColumn
uxPTEgressCallsRejected=_UxPTEgressCallsRejected_Object((1,3,6,1,4,1,177,15,1,5,1,2,1,13),_UxPTEgressCallsRejected_Type())
uxPTEgressCallsRejected.setMaxAccess(_B)
if mibBuilder.loadTexts:uxPTEgressCallsRejected.setStatus(_A)
_UxPTIngressCallAttempts_Type=Counter32
_UxPTIngressCallAttempts_Object=MibTableColumn
uxPTIngressCallAttempts=_UxPTIngressCallAttempts_Object((1,3,6,1,4,1,177,15,1,5,1,2,1,14),_UxPTIngressCallAttempts_Type())
uxPTIngressCallAttempts.setMaxAccess(_B)
if mibBuilder.loadTexts:uxPTIngressCallAttempts.setStatus(_A)
_UxPTIngressCallsAccepted_Type=Counter32
_UxPTIngressCallsAccepted_Object=MibTableColumn
uxPTIngressCallsAccepted=_UxPTIngressCallsAccepted_Object((1,3,6,1,4,1,177,15,1,5,1,2,1,15),_UxPTIngressCallsAccepted_Type())
uxPTIngressCallsAccepted.setMaxAccess(_B)
if mibBuilder.loadTexts:uxPTIngressCallsAccepted.setStatus(_A)
_UxPTIngressCallsCompleted_Type=Counter32
_UxPTIngressCallsCompleted_Object=MibTableColumn
uxPTIngressCallsCompleted=_UxPTIngressCallsCompleted_Object((1,3,6,1,4,1,177,15,1,5,1,2,1,16),_UxPTIngressCallsCompleted_Type())
uxPTIngressCallsCompleted.setMaxAccess(_B)
if mibBuilder.loadTexts:uxPTIngressCallsCompleted.setStatus(_A)
_UxPTIngressCallsRejected_Type=Counter32
_UxPTIngressCallsRejected_Object=MibTableColumn
uxPTIngressCallsRejected=_UxPTIngressCallsRejected_Object((1,3,6,1,4,1,177,15,1,5,1,2,1,17),_UxPTIngressCallsRejected_Type())
uxPTIngressCallsRejected.setMaxAccess(_B)
if mibBuilder.loadTexts:uxPTIngressCallsRejected.setStatus(_A)
_UxPTBlockedCalls_Type=Counter32
_UxPTBlockedCalls_Object=MibTableColumn
uxPTBlockedCalls=_UxPTBlockedCalls_Object((1,3,6,1,4,1,177,15,1,5,1,2,1,18),_UxPTBlockedCalls_Type())
uxPTBlockedCalls.setMaxAccess(_B)
if mibBuilder.loadTexts:uxPTBlockedCalls.setStatus(_A)
_UxPTEgressBlockedCalls_Type=Counter32
_UxPTEgressBlockedCalls_Object=MibTableColumn
uxPTEgressBlockedCalls=_UxPTEgressBlockedCalls_Object((1,3,6,1,4,1,177,15,1,5,1,2,1,19),_UxPTEgressBlockedCalls_Type())
uxPTEgressBlockedCalls.setMaxAccess(_B)
if mibBuilder.loadTexts:uxPTEgressBlockedCalls.setStatus(_A)
_UxPTIngressBlockedCalls_Type=Counter32
_UxPTIngressBlockedCalls_Object=MibTableColumn
uxPTIngressBlockedCalls=_UxPTIngressBlockedCalls_Object((1,3,6,1,4,1,177,15,1,5,1,2,1,20),_UxPTIngressBlockedCalls_Type())
uxPTIngressBlockedCalls.setMaxAccess(_B)
if mibBuilder.loadTexts:uxPTIngressBlockedCalls.setStatus(_A)
_UxPTEgressCurrentCalls_Type=Counter32
_UxPTEgressCurrentCalls_Object=MibTableColumn
uxPTEgressCurrentCalls=_UxPTEgressCurrentCalls_Object((1,3,6,1,4,1,177,15,1,5,1,2,1,21),_UxPTEgressCurrentCalls_Type())
uxPTEgressCurrentCalls.setMaxAccess(_B)
if mibBuilder.loadTexts:uxPTEgressCurrentCalls.setStatus(_A)
_UxPTIngressCurrentCalls_Type=Counter32
_UxPTIngressCurrentCalls_Object=MibTableColumn
uxPTIngressCurrentCalls=_UxPTIngressCurrentCalls_Object((1,3,6,1,4,1,177,15,1,5,1,2,1,22),_UxPTIngressCurrentCalls_Type())
uxPTIngressCurrentCalls.setMaxAccess(_B)
if mibBuilder.loadTexts:uxPTIngressCurrentCalls.setStatus(_A)
_UxPTBHCARate_Type=Counter32
_UxPTBHCARate_Object=MibTableColumn
uxPTBHCARate=_UxPTBHCARate_Object((1,3,6,1,4,1,177,15,1,5,1,2,1,23),_UxPTBHCARate_Type())
uxPTBHCARate.setMaxAccess(_B)
if mibBuilder.loadTexts:uxPTBHCARate.setStatus(_A)
_UxPTBHCCRate_Type=Counter32
_UxPTBHCCRate_Object=MibTableColumn
uxPTBHCCRate=_UxPTBHCCRate_Object((1,3,6,1,4,1,177,15,1,5,1,2,1,24),_UxPTBHCCRate_Type())
uxPTBHCCRate.setMaxAccess(_B)
if mibBuilder.loadTexts:uxPTBHCCRate.setStatus(_A)
_UxCallRtTablesTable_Object=MibTable
uxCallRtTablesTable=_UxCallRtTablesTable_Object((1,3,6,1,4,1,177,15,1,5,2))
if mibBuilder.loadTexts:uxCallRtTablesTable.setStatus(_A)
_UxCallRtTablesEntry_Object=MibTableRow
uxCallRtTablesEntry=_UxCallRtTablesEntry_Object((1,3,6,1,4,1,177,15,1,5,2,1))
uxCallRtTablesEntry.setIndexNames((0,_D,_J))
if mibBuilder.loadTexts:uxCallRtTablesEntry.setStatus(_A)
class _UxCallRtTablesTableIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_UxCallRtTablesTableIndex_Type.__name__=_C
_UxCallRtTablesTableIndex_Object=MibTableColumn
uxCallRtTablesTableIndex=_UxCallRtTablesTableIndex_Object((1,3,6,1,4,1,177,15,1,5,2,1,1),_UxCallRtTablesTableIndex_Type())
uxCallRtTablesTableIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:uxCallRtTablesTableIndex.setStatus(_A)
_UxDesc_Type=DisplayString
_UxDesc_Object=MibTableColumn
uxDesc=_UxDesc_Object((1,3,6,1,4,1,177,15,1,5,2,1,2),_UxDesc_Type())
uxDesc.setMaxAccess(_B)
if mibBuilder.loadTexts:uxDesc.setStatus(_A)
class _UxCallRtSequence_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30000))
_UxCallRtSequence_Type.__name__=_H
_UxCallRtSequence_Object=MibTableColumn
uxCallRtSequence=_UxCallRtSequence_Object((1,3,6,1,4,1,177,15,1,5,2,1,3),_UxCallRtSequence_Type())
uxCallRtSequence.setMaxAccess(_B)
if mibBuilder.loadTexts:uxCallRtSequence.setStatus(_A)
_UxCallRtTable_Object=MibTable
uxCallRtTable=_UxCallRtTable_Object((1,3,6,1,4,1,177,15,1,5,3))
if mibBuilder.loadTexts:uxCallRtTable.setStatus(_A)
_UxCallRtEntry_Object=MibTableRow
uxCallRtEntry=_UxCallRtEntry_Object((1,3,6,1,4,1,177,15,1,5,3,1))
uxCallRtEntry.setIndexNames((0,_D,_K),(0,_D,_L))
if mibBuilder.loadTexts:uxCallRtEntry.setStatus(_A)
class _UxCallRtTablesIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_UxCallRtTablesIndex_Type.__name__=_C
_UxCallRtTablesIndex_Object=MibTableColumn
uxCallRtTablesIndex=_UxCallRtTablesIndex_Object((1,3,6,1,4,1,177,15,1,5,3,1,1),_UxCallRtTablesIndex_Type())
uxCallRtTablesIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:uxCallRtTablesIndex.setStatus(_A)
class _UxCallRtIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_UxCallRtIndex_Type.__name__=_C
_UxCallRtIndex_Object=MibTableColumn
uxCallRtIndex=_UxCallRtIndex_Object((1,3,6,1,4,1,177,15,1,5,3,1,2),_UxCallRtIndex_Type())
uxCallRtIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:uxCallRtIndex.setStatus(_A)
_UxDescription_Type=DisplayString
_UxDescription_Object=MibTableColumn
uxDescription=_UxDescription_Object((1,3,6,1,4,1,177,15,1,5,3,1,3),_UxDescription_Type())
uxDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:uxDescription.setStatus(_A)
class _UxAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_UxAdminState_Type.__name__=_C
_UxAdminState_Object=MibTableColumn
uxAdminState=_UxAdminState_Object((1,3,6,1,4,1,177,15,1,5,3,1,4),_UxAdminState_Type())
uxAdminState.setMaxAccess(_B)
if mibBuilder.loadTexts:uxAdminState.setStatus(_A)
_UxRoutePriority_Type=Integer32
_UxRoutePriority_Object=MibTableColumn
uxRoutePriority=_UxRoutePriority_Object((1,3,6,1,4,1,177,15,1,5,3,1,5),_UxRoutePriority_Type())
uxRoutePriority.setMaxAccess(_B)
if mibBuilder.loadTexts:uxRoutePriority.setStatus(_A)
_UxSignalingGroupList_Type=DisplayString
_UxSignalingGroupList_Object=MibTableColumn
uxSignalingGroupList=_UxSignalingGroupList_Object((1,3,6,1,4,1,177,15,1,5,3,1,6),_UxSignalingGroupList_Type())
uxSignalingGroupList.setMaxAccess(_B)
if mibBuilder.loadTexts:uxSignalingGroupList.setStatus(_A)
_UxQualityMetricCalls_Type=Integer32
_UxQualityMetricCalls_Object=MibTableColumn
uxQualityMetricCalls=_UxQualityMetricCalls_Object((1,3,6,1,4,1,177,15,1,5,3,1,7),_UxQualityMetricCalls_Type())
uxQualityMetricCalls.setMaxAccess(_B)
if mibBuilder.loadTexts:uxQualityMetricCalls.setStatus(_A)
_UxQualityMetricTime_Type=Integer32
_UxQualityMetricTime_Object=MibTableColumn
uxQualityMetricTime=_UxQualityMetricTime_Object((1,3,6,1,4,1,177,15,1,5,3,1,8),_UxQualityMetricTime_Type())
uxQualityMetricTime.setMaxAccess(_B)
if mibBuilder.loadTexts:uxQualityMetricTime.setStatus(_A)
_UxQualityMinASRThreshold_Type=Integer32
_UxQualityMinASRThreshold_Object=MibTableColumn
uxQualityMinASRThreshold=_UxQualityMinASRThreshold_Object((1,3,6,1,4,1,177,15,1,5,3,1,9),_UxQualityMinASRThreshold_Type())
uxQualityMinASRThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:uxQualityMinASRThreshold.setStatus(_A)
_UxQualityMaxRoundTripDelayThreshold_Type=Integer32
_UxQualityMaxRoundTripDelayThreshold_Object=MibTableColumn
uxQualityMaxRoundTripDelayThreshold=_UxQualityMaxRoundTripDelayThreshold_Object((1,3,6,1,4,1,177,15,1,5,3,1,10),_UxQualityMaxRoundTripDelayThreshold_Type())
uxQualityMaxRoundTripDelayThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:uxQualityMaxRoundTripDelayThreshold.setStatus(_A)
_UxQualityMaxJitterThreshold_Type=Integer32
_UxQualityMaxJitterThreshold_Object=MibTableColumn
uxQualityMaxJitterThreshold=_UxQualityMaxJitterThreshold_Object((1,3,6,1,4,1,177,15,1,5,3,1,11),_UxQualityMaxJitterThreshold_Type())
uxQualityMaxJitterThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:uxQualityMaxJitterThreshold.setStatus(_A)
_UxQualityMinMOSThreshold_Type=Integer32
_UxQualityMinMOSThreshold_Object=MibTableColumn
uxQualityMinMOSThreshold=_UxQualityMinMOSThreshold_Object((1,3,6,1,4,1,177,15,1,5,3,1,12),_UxQualityMinMOSThreshold_Type())
uxQualityMinMOSThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:uxQualityMinMOSThreshold.setStatus(_A)
_UxSGTable_Object=MibTable
uxSGTable=_UxSGTable_Object((1,3,6,1,4,1,177,15,1,5,4))
if mibBuilder.loadTexts:uxSGTable.setStatus(_A)
_UxSGEntry_Object=MibTableRow
uxSGEntry=_UxSGEntry_Object((1,3,6,1,4,1,177,15,1,5,4,1))
uxSGEntry.setIndexNames((0,_D,_M))
if mibBuilder.loadTexts:uxSGEntry.setStatus(_A)
class _UxSGEntryIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_UxSGEntryIndex_Type.__name__=_C
_UxSGEntryIndex_Object=MibTableColumn
uxSGEntryIndex=_UxSGEntryIndex_Object((1,3,6,1,4,1,177,15,1,5,4,1,1),_UxSGEntryIndex_Type())
uxSGEntryIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:uxSGEntryIndex.setStatus(_A)
_UxSGDescription_Type=DisplayString
_UxSGDescription_Object=MibTableColumn
uxSGDescription=_UxSGDescription_Object((1,3,6,1,4,1,177,15,1,5,4,1,2),_UxSGDescription_Type())
uxSGDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:uxSGDescription.setStatus(_A)
class _UxSGType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('sip',1),('isdn',2),('cas',3)))
_UxSGType_Type.__name__=_C
_UxSGType_Object=MibTableColumn
uxSGType=_UxSGType_Object((1,3,6,1,4,1,177,15,1,5,4,1,3),_UxSGType_Type())
uxSGType.setMaxAccess(_B)
if mibBuilder.loadTexts:uxSGType.setStatus(_A)
class _UxSGAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_F,0),(_G,1),('drain',2)))
_UxSGAdminState_Type.__name__=_C
_UxSGAdminState_Object=MibTableColumn
uxSGAdminState=_UxSGAdminState_Object((1,3,6,1,4,1,177,15,1,5,4,1,4),_UxSGAdminState_Type())
uxSGAdminState.setMaxAccess(_B)
if mibBuilder.loadTexts:uxSGAdminState.setStatus(_A)
class _UxSGServiceState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_UxSGServiceState_Type.__name__=_C
_UxSGServiceState_Object=MibTableColumn
uxSGServiceState=_UxSGServiceState_Object((1,3,6,1,4,1,177,15,1,5,4,1,5),_UxSGServiceState_Type())
uxSGServiceState.setMaxAccess(_B)
if mibBuilder.loadTexts:uxSGServiceState.setStatus(_A)
_UxSipServerTable_Object=MibTable
uxSipServerTable=_UxSipServerTable_Object((1,3,6,1,4,1,177,15,1,5,5))
if mibBuilder.loadTexts:uxSipServerTable.setStatus(_A)
_UxSipServerEntry_Object=MibTableRow
uxSipServerEntry=_UxSipServerEntry_Object((1,3,6,1,4,1,177,15,1,5,5,1))
uxSipServerEntry.setIndexNames((0,_D,_N),(0,_D,_O))
if mibBuilder.loadTexts:uxSipServerEntry.setStatus(_A)
class _UxSGIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_UxSGIndex_Type.__name__=_C
_UxSGIndex_Object=MibTableColumn
uxSGIndex=_UxSGIndex_Object((1,3,6,1,4,1,177,15,1,5,5,1,1),_UxSGIndex_Type())
uxSGIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:uxSGIndex.setStatus(_A)
class _UxSipServerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_UxSipServerIndex_Type.__name__=_C
_UxSipServerIndex_Object=MibTableColumn
uxSipServerIndex=_UxSipServerIndex_Object((1,3,6,1,4,1,177,15,1,5,5,1,2),_UxSipServerIndex_Type())
uxSipServerIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:uxSipServerIndex.setStatus(_A)
_UxSipSvrPriority_Type=Integer32
_UxSipSvrPriority_Object=MibTableColumn
uxSipSvrPriority=_UxSipSvrPriority_Object((1,3,6,1,4,1,177,15,1,5,5,1,3),_UxSipSvrPriority_Type())
uxSipSvrPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:uxSipSvrPriority.setStatus(_A)
_UxSipSvrHost_Type=DisplayString
_UxSipSvrHost_Object=MibTableColumn
uxSipSvrHost=_UxSipSvrHost_Object((1,3,6,1,4,1,177,15,1,5,5,1,4),_UxSipSvrHost_Type())
uxSipSvrHost.setMaxAccess(_B)
if mibBuilder.loadTexts:uxSipSvrHost.setStatus(_A)
_UxSipSvrPort_Type=Integer32
_UxSipSvrPort_Object=MibTableColumn
uxSipSvrPort=_UxSipSvrPort_Object((1,3,6,1,4,1,177,15,1,5,5,1,5),_UxSipSvrPort_Type())
uxSipSvrPort.setMaxAccess(_B)
if mibBuilder.loadTexts:uxSipSvrPort.setStatus(_A)
class _UxSipSvrTransProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4)));namedValues=NamedValues(*(('udp',1),('tcp',2),('tls',4)))
_UxSipSvrTransProtocol_Type.__name__=_C
_UxSipSvrTransProtocol_Object=MibTableColumn
uxSipSvrTransProtocol=_UxSipSvrTransProtocol_Object((1,3,6,1,4,1,177,15,1,5,5,1,6),_UxSipSvrTransProtocol_Type())
uxSipSvrTransProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:uxSipSvrTransProtocol.setStatus(_A)
_UxChannelStatusTable_Object=MibTable
uxChannelStatusTable=_UxChannelStatusTable_Object((1,3,6,1,4,1,177,15,1,5,6))
if mibBuilder.loadTexts:uxChannelStatusTable.setStatus(_A)
_UxChannelStatusEntry_Object=MibTableRow
uxChannelStatusEntry=_UxChannelStatusEntry_Object((1,3,6,1,4,1,177,15,1,5,6,1))
uxChannelStatusEntry.setIndexNames((0,_D,_P),(0,_D,_Q),(0,_D,_R),(0,_D,_S))
if mibBuilder.loadTexts:uxChannelStatusEntry.setStatus(_A)
_UxChShelfNumber_Type=Unsigned32
_UxChShelfNumber_Object=MibTableColumn
uxChShelfNumber=_UxChShelfNumber_Object((1,3,6,1,4,1,177,15,1,5,6,1,1),_UxChShelfNumber_Type())
uxChShelfNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:uxChShelfNumber.setStatus(_A)
_UxChSlotNumber_Type=Unsigned32
_UxChSlotNumber_Object=MibTableColumn
uxChSlotNumber=_UxChSlotNumber_Object((1,3,6,1,4,1,177,15,1,5,6,1,2),_UxChSlotNumber_Type())
uxChSlotNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:uxChSlotNumber.setStatus(_A)
_UxChPortNumber_Type=Unsigned32
_UxChPortNumber_Object=MibTableColumn
uxChPortNumber=_UxChPortNumber_Object((1,3,6,1,4,1,177,15,1,5,6,1,3),_UxChPortNumber_Type())
uxChPortNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:uxChPortNumber.setStatus(_A)
_UxChChannelNumber_Type=Unsigned32
_UxChChannelNumber_Object=MibTableColumn
uxChChannelNumber=_UxChChannelNumber_Object((1,3,6,1,4,1,177,15,1,5,6,1,4),_UxChChannelNumber_Type())
uxChChannelNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:uxChChannelNumber.setStatus(_A)
class _UxChAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('down',0),('up',1)))
_UxChAdminState_Type.__name__=_C
_UxChAdminState_Object=MibTableColumn
uxChAdminState=_UxChAdminState_Object((1,3,6,1,4,1,177,15,1,5,6,1,5),_UxChAdminState_Type())
uxChAdminState.setMaxAccess(_B)
if mibBuilder.loadTexts:uxChAdminState.setStatus(_A)
class _UxChOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)));namedValues=NamedValues(*(('outOfService',0),('idle',1),('pending',2),('waitingForRoute',3),('actionList',4),('waitingForDigits',5),('remoteSetUp',6),('peerSetUp',7),('alerting',8),('inBandInfo',9),('connected',10),('toneGeneration',11),('releasing',12),('aborting',13),('resetting',14),('up',15),('down',16)))
_UxChOperState_Type.__name__=_C
_UxChOperState_Object=MibTableColumn
uxChOperState=_UxChOperState_Object((1,3,6,1,4,1,177,15,1,5,6,1,6),_UxChOperState_Type())
uxChOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:uxChOperState.setStatus(_A)
_UxChInUseSeconds_Type=Counter32
_UxChInUseSeconds_Object=MibTableColumn
uxChInUseSeconds=_UxChInUseSeconds_Object((1,3,6,1,4,1,177,15,1,5,6,1,7),_UxChInUseSeconds_Type())
uxChInUseSeconds.setMaxAccess(_B)
if mibBuilder.loadTexts:uxChInUseSeconds.setStatus(_A)
_UxSGStatsCurrentTable_Object=MibTable
uxSGStatsCurrentTable=_UxSGStatsCurrentTable_Object((1,3,6,1,4,1,177,15,1,5,7))
if mibBuilder.loadTexts:uxSGStatsCurrentTable.setStatus(_A)
_UxSGStatsCurrentEntry_Object=MibTableRow
uxSGStatsCurrentEntry=_UxSGStatsCurrentEntry_Object((1,3,6,1,4,1,177,15,1,5,7,1))
uxSGStatsCurrentEntry.setIndexNames((0,_D,_T))
if mibBuilder.loadTexts:uxSGStatsCurrentEntry.setStatus(_A)
class _UxSGCurrentIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_UxSGCurrentIndex_Type.__name__=_C
_UxSGCurrentIndex_Object=MibTableColumn
uxSGCurrentIndex=_UxSGCurrentIndex_Object((1,3,6,1,4,1,177,15,1,5,7,1,1),_UxSGCurrentIndex_Type())
uxSGCurrentIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:uxSGCurrentIndex.setStatus(_A)
_UxSGCurrentPeakChannelUsage_Type=PerfCurrentCount
_UxSGCurrentPeakChannelUsage_Object=MibTableColumn
uxSGCurrentPeakChannelUsage=_UxSGCurrentPeakChannelUsage_Object((1,3,6,1,4,1,177,15,1,5,7,1,2),_UxSGCurrentPeakChannelUsage_Type())
uxSGCurrentPeakChannelUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:uxSGCurrentPeakChannelUsage.setStatus(_A)
_UxSGCurrentCompletedCalls_Type=PerfCurrentCount
_UxSGCurrentCompletedCalls_Object=MibTableColumn
uxSGCurrentCompletedCalls=_UxSGCurrentCompletedCalls_Object((1,3,6,1,4,1,177,15,1,5,7,1,3),_UxSGCurrentCompletedCalls_Type())
uxSGCurrentCompletedCalls.setMaxAccess(_B)
if mibBuilder.loadTexts:uxSGCurrentCompletedCalls.setStatus(_A)
_UxSGCurrentIncompleteCalls_Type=PerfCurrentCount
_UxSGCurrentIncompleteCalls_Object=MibTableColumn
uxSGCurrentIncompleteCalls=_UxSGCurrentIncompleteCalls_Object((1,3,6,1,4,1,177,15,1,5,7,1,4),_UxSGCurrentIncompleteCalls_Type())
uxSGCurrentIncompleteCalls.setMaxAccess(_B)
if mibBuilder.loadTexts:uxSGCurrentIncompleteCalls.setStatus(_A)
_UxSGStatsIntervalTable_Object=MibTable
uxSGStatsIntervalTable=_UxSGStatsIntervalTable_Object((1,3,6,1,4,1,177,15,1,5,8))
if mibBuilder.loadTexts:uxSGStatsIntervalTable.setStatus(_A)
_UxSGStatsIntervalEntry_Object=MibTableRow
uxSGStatsIntervalEntry=_UxSGStatsIntervalEntry_Object((1,3,6,1,4,1,177,15,1,5,8,1))
uxSGStatsIntervalEntry.setIndexNames((0,_D,_U),(0,_D,_V))
if mibBuilder.loadTexts:uxSGStatsIntervalEntry.setStatus(_A)
class _UxSGIntervalIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_UxSGIntervalIndex_Type.__name__=_C
_UxSGIntervalIndex_Object=MibTableColumn
uxSGIntervalIndex=_UxSGIntervalIndex_Object((1,3,6,1,4,1,177,15,1,5,8,1,1),_UxSGIntervalIndex_Type())
uxSGIntervalIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:uxSGIntervalIndex.setStatus(_A)
class _UxSGIntervalNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,24))
_UxSGIntervalNumber_Type.__name__=_C
_UxSGIntervalNumber_Object=MibTableColumn
uxSGIntervalNumber=_UxSGIntervalNumber_Object((1,3,6,1,4,1,177,15,1,5,8,1,2),_UxSGIntervalNumber_Type())
uxSGIntervalNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:uxSGIntervalNumber.setStatus(_A)
_UxSGIntervalPeakChannelUsage_Type=PerfIntervalCount
_UxSGIntervalPeakChannelUsage_Object=MibTableColumn
uxSGIntervalPeakChannelUsage=_UxSGIntervalPeakChannelUsage_Object((1,3,6,1,4,1,177,15,1,5,8,1,3),_UxSGIntervalPeakChannelUsage_Type())
uxSGIntervalPeakChannelUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:uxSGIntervalPeakChannelUsage.setStatus(_A)
_UxSGIntervalCompletedCalls_Type=PerfIntervalCount
_UxSGIntervalCompletedCalls_Object=MibTableColumn
uxSGIntervalCompletedCalls=_UxSGIntervalCompletedCalls_Object((1,3,6,1,4,1,177,15,1,5,8,1,4),_UxSGIntervalCompletedCalls_Type())
uxSGIntervalCompletedCalls.setMaxAccess(_B)
if mibBuilder.loadTexts:uxSGIntervalCompletedCalls.setStatus(_A)
_UxSGIntervalIncompleteCalls_Type=PerfIntervalCount
_UxSGIntervalIncompleteCalls_Object=MibTableColumn
uxSGIntervalIncompleteCalls=_UxSGIntervalIncompleteCalls_Object((1,3,6,1,4,1,177,15,1,5,8,1,5),_UxSGIntervalIncompleteCalls_Type())
uxSGIntervalIncompleteCalls.setMaxAccess(_B)
if mibBuilder.loadTexts:uxSGIntervalIncompleteCalls.setStatus(_A)
_UxCallRtStatsCurrentTable_Object=MibTable
uxCallRtStatsCurrentTable=_UxCallRtStatsCurrentTable_Object((1,3,6,1,4,1,177,15,1,5,10))
if mibBuilder.loadTexts:uxCallRtStatsCurrentTable.setStatus(_A)
_UxCallRtStatsCurrentEntry_Object=MibTableRow
uxCallRtStatsCurrentEntry=_UxCallRtStatsCurrentEntry_Object((1,3,6,1,4,1,177,15,1,5,10,1))
uxCallRtStatsCurrentEntry.setIndexNames((0,_D,_W),(0,_D,_X))
if mibBuilder.loadTexts:uxCallRtStatsCurrentEntry.setStatus(_A)
class _UxCallRtCurrentTablesIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_UxCallRtCurrentTablesIndex_Type.__name__=_C
_UxCallRtCurrentTablesIndex_Object=MibTableColumn
uxCallRtCurrentTablesIndex=_UxCallRtCurrentTablesIndex_Object((1,3,6,1,4,1,177,15,1,5,10,1,1),_UxCallRtCurrentTablesIndex_Type())
uxCallRtCurrentTablesIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:uxCallRtCurrentTablesIndex.setStatus(_A)
class _UxCallRtCurrentEntryIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_UxCallRtCurrentEntryIndex_Type.__name__=_C
_UxCallRtCurrentEntryIndex_Object=MibTableColumn
uxCallRtCurrentEntryIndex=_UxCallRtCurrentEntryIndex_Object((1,3,6,1,4,1,177,15,1,5,10,1,2),_UxCallRtCurrentEntryIndex_Type())
uxCallRtCurrentEntryIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:uxCallRtCurrentEntryIndex.setStatus(_A)
_UxCallRtCurrentRuleUsage_Type=PerfCurrentCount
_UxCallRtCurrentRuleUsage_Object=MibTableColumn
uxCallRtCurrentRuleUsage=_UxCallRtCurrentRuleUsage_Object((1,3,6,1,4,1,177,15,1,5,10,1,3),_UxCallRtCurrentRuleUsage_Type())
uxCallRtCurrentRuleUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:uxCallRtCurrentRuleUsage.setStatus(_A)
_UxCallRtStatsIntervalTable_Object=MibTable
uxCallRtStatsIntervalTable=_UxCallRtStatsIntervalTable_Object((1,3,6,1,4,1,177,15,1,5,11))
if mibBuilder.loadTexts:uxCallRtStatsIntervalTable.setStatus(_A)
_UxCallRtStatsIntervalEntry_Object=MibTableRow
uxCallRtStatsIntervalEntry=_UxCallRtStatsIntervalEntry_Object((1,3,6,1,4,1,177,15,1,5,11,1))
uxCallRtStatsIntervalEntry.setIndexNames((0,_D,_Y),(0,_D,_Z),(0,_D,_a))
if mibBuilder.loadTexts:uxCallRtStatsIntervalEntry.setStatus(_A)
class _UxCallRtIntervalTablesIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_UxCallRtIntervalTablesIndex_Type.__name__=_C
_UxCallRtIntervalTablesIndex_Object=MibTableColumn
uxCallRtIntervalTablesIndex=_UxCallRtIntervalTablesIndex_Object((1,3,6,1,4,1,177,15,1,5,11,1,1),_UxCallRtIntervalTablesIndex_Type())
uxCallRtIntervalTablesIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:uxCallRtIntervalTablesIndex.setStatus(_A)
class _UxCallRtIntervalEntryIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_UxCallRtIntervalEntryIndex_Type.__name__=_C
_UxCallRtIntervalEntryIndex_Object=MibTableColumn
uxCallRtIntervalEntryIndex=_UxCallRtIntervalEntryIndex_Object((1,3,6,1,4,1,177,15,1,5,11,1,2),_UxCallRtIntervalEntryIndex_Type())
uxCallRtIntervalEntryIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:uxCallRtIntervalEntryIndex.setStatus(_A)
class _UxCallRtIntervalNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,24))
_UxCallRtIntervalNumber_Type.__name__=_C
_UxCallRtIntervalNumber_Object=MibTableColumn
uxCallRtIntervalNumber=_UxCallRtIntervalNumber_Object((1,3,6,1,4,1,177,15,1,5,11,1,3),_UxCallRtIntervalNumber_Type())
uxCallRtIntervalNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:uxCallRtIntervalNumber.setStatus(_A)
_UxCallRtIntervalRuleUsage_Type=PerfIntervalCount
_UxCallRtIntervalRuleUsage_Object=MibTableColumn
uxCallRtIntervalRuleUsage=_UxCallRtIntervalRuleUsage_Object((1,3,6,1,4,1,177,15,1,5,11,1,4),_UxCallRtIntervalRuleUsage_Type())
uxCallRtIntervalRuleUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:uxCallRtIntervalRuleUsage.setStatus(_A)
_UxCallRtStatsTotalTable_Object=MibTable
uxCallRtStatsTotalTable=_UxCallRtStatsTotalTable_Object((1,3,6,1,4,1,177,15,1,5,12))
if mibBuilder.loadTexts:uxCallRtStatsTotalTable.setStatus(_A)
_UxCallRtStatsTotalEntry_Object=MibTableRow
uxCallRtStatsTotalEntry=_UxCallRtStatsTotalEntry_Object((1,3,6,1,4,1,177,15,1,5,12,1))
uxCallRtStatsTotalEntry.setIndexNames((0,_D,_b),(0,_D,_c))
if mibBuilder.loadTexts:uxCallRtStatsTotalEntry.setStatus(_A)
class _UxCallRtTotalTablesIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_UxCallRtTotalTablesIndex_Type.__name__=_C
_UxCallRtTotalTablesIndex_Object=MibTableColumn
uxCallRtTotalTablesIndex=_UxCallRtTotalTablesIndex_Object((1,3,6,1,4,1,177,15,1,5,12,1,1),_UxCallRtTotalTablesIndex_Type())
uxCallRtTotalTablesIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:uxCallRtTotalTablesIndex.setStatus(_A)
class _UxCallRtTotalEntryIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_UxCallRtTotalEntryIndex_Type.__name__=_C
_UxCallRtTotalEntryIndex_Object=MibTableColumn
uxCallRtTotalEntryIndex=_UxCallRtTotalEntryIndex_Object((1,3,6,1,4,1,177,15,1,5,12,1,2),_UxCallRtTotalEntryIndex_Type())
uxCallRtTotalEntryIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:uxCallRtTotalEntryIndex.setStatus(_A)
_UxCallRtTotalRuleUsage_Type=PerfTotalCount
_UxCallRtTotalRuleUsage_Object=MibTableColumn
uxCallRtTotalRuleUsage=_UxCallRtTotalRuleUsage_Object((1,3,6,1,4,1,177,15,1,5,12,1,3),_UxCallRtTotalRuleUsage_Type())
uxCallRtTotalRuleUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:uxCallRtTotalRuleUsage.setStatus(_A)
_UxLicenseStatsIntervalTable_Object=MibTable
uxLicenseStatsIntervalTable=_UxLicenseStatsIntervalTable_Object((1,3,6,1,4,1,177,15,1,5,13))
if mibBuilder.loadTexts:uxLicenseStatsIntervalTable.setStatus(_A)
_UxLicenseStatsIntervalEntry_Object=MibTableRow
uxLicenseStatsIntervalEntry=_UxLicenseStatsIntervalEntry_Object((1,3,6,1,4,1,177,15,1,5,13,1))
uxLicenseStatsIntervalEntry.setIndexNames((0,_D,_d))
if mibBuilder.loadTexts:uxLicenseStatsIntervalEntry.setStatus(_A)
class _UxLicenseIntervalNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,24))
_UxLicenseIntervalNumber_Type.__name__=_C
_UxLicenseIntervalNumber_Object=MibTableColumn
uxLicenseIntervalNumber=_UxLicenseIntervalNumber_Object((1,3,6,1,4,1,177,15,1,5,13,1,1),_UxLicenseIntervalNumber_Type())
uxLicenseIntervalNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:uxLicenseIntervalNumber.setStatus(_A)
_UxLicenseIntervalPeakSIPCall_Type=PerfTotalCount
_UxLicenseIntervalPeakSIPCall_Object=MibTableColumn
uxLicenseIntervalPeakSIPCall=_UxLicenseIntervalPeakSIPCall_Object((1,3,6,1,4,1,177,15,1,5,13,1,2),_UxLicenseIntervalPeakSIPCall_Type())
uxLicenseIntervalPeakSIPCall.setMaxAccess(_B)
if mibBuilder.loadTexts:uxLicenseIntervalPeakSIPCall.setStatus(_A)
_UxLicenseIntervalPeakSIPRegistration_Type=PerfTotalCount
_UxLicenseIntervalPeakSIPRegistration_Object=MibTableColumn
uxLicenseIntervalPeakSIPRegistration=_UxLicenseIntervalPeakSIPRegistration_Object((1,3,6,1,4,1,177,15,1,5,13,1,3),_UxLicenseIntervalPeakSIPRegistration_Type())
uxLicenseIntervalPeakSIPRegistration.setMaxAccess(_B)
if mibBuilder.loadTexts:uxLicenseIntervalPeakSIPRegistration.setStatus(_A)
_UxLicenseIntervalPeakTDMChannel_Type=PerfTotalCount
_UxLicenseIntervalPeakTDMChannel_Object=MibTableColumn
uxLicenseIntervalPeakTDMChannel=_UxLicenseIntervalPeakTDMChannel_Object((1,3,6,1,4,1,177,15,1,5,13,1,4),_UxLicenseIntervalPeakTDMChannel_Type())
uxLicenseIntervalPeakTDMChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:uxLicenseIntervalPeakTDMChannel.setStatus('deprecated')
_UxLicenseIntervalPeakDSP_Type=PerfTotalCount
_UxLicenseIntervalPeakDSP_Object=MibTableColumn
uxLicenseIntervalPeakDSP=_UxLicenseIntervalPeakDSP_Object((1,3,6,1,4,1,177,15,1,5,13,1,5),_UxLicenseIntervalPeakDSP_Type())
uxLicenseIntervalPeakDSP.setMaxAccess(_B)
if mibBuilder.loadTexts:uxLicenseIntervalPeakDSP.setStatus(_A)
_UxSIPRegistrationsStatsCurrentTable_Object=MibTable
uxSIPRegistrationsStatsCurrentTable=_UxSIPRegistrationsStatsCurrentTable_Object((1,3,6,1,4,1,177,15,1,5,15))
if mibBuilder.loadTexts:uxSIPRegistrationsStatsCurrentTable.setStatus(_A)
_UxSIPRegistrationsStatsCurrentEntry_Object=MibTableRow
uxSIPRegistrationsStatsCurrentEntry=_UxSIPRegistrationsStatsCurrentEntry_Object((1,3,6,1,4,1,177,15,1,5,15,1))
uxSIPRegistrationsStatsCurrentEntry.setIndexNames((0,_D,_e))
if mibBuilder.loadTexts:uxSIPRegistrationsStatsCurrentEntry.setStatus(_A)
class _UxSIPRegistrationsCurrentIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_UxSIPRegistrationsCurrentIndex_Type.__name__=_C
_UxSIPRegistrationsCurrentIndex_Object=MibTableColumn
uxSIPRegistrationsCurrentIndex=_UxSIPRegistrationsCurrentIndex_Object((1,3,6,1,4,1,177,15,1,5,15,1,1),_UxSIPRegistrationsCurrentIndex_Type())
uxSIPRegistrationsCurrentIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:uxSIPRegistrationsCurrentIndex.setStatus(_A)
_UxSIPRegistrationsCurrentPeakUsers_Type=PerfCurrentCount
_UxSIPRegistrationsCurrentPeakUsers_Object=MibTableColumn
uxSIPRegistrationsCurrentPeakUsers=_UxSIPRegistrationsCurrentPeakUsers_Object((1,3,6,1,4,1,177,15,1,5,15,1,2),_UxSIPRegistrationsCurrentPeakUsers_Type())
uxSIPRegistrationsCurrentPeakUsers.setMaxAccess(_B)
if mibBuilder.loadTexts:uxSIPRegistrationsCurrentPeakUsers.setStatus(_A)
_UxSIPRegistrationsStatsIntervalTable_Object=MibTable
uxSIPRegistrationsStatsIntervalTable=_UxSIPRegistrationsStatsIntervalTable_Object((1,3,6,1,4,1,177,15,1,5,16))
if mibBuilder.loadTexts:uxSIPRegistrationsStatsIntervalTable.setStatus(_A)
_UxSIPRegistrationsStatsIntervalEntry_Object=MibTableRow
uxSIPRegistrationsStatsIntervalEntry=_UxSIPRegistrationsStatsIntervalEntry_Object((1,3,6,1,4,1,177,15,1,5,16,1))
uxSIPRegistrationsStatsIntervalEntry.setIndexNames((0,_D,_f),(0,_D,_g))
if mibBuilder.loadTexts:uxSIPRegistrationsStatsIntervalEntry.setStatus(_A)
class _UxSIPRegistrationsIntervalIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_UxSIPRegistrationsIntervalIndex_Type.__name__=_C
_UxSIPRegistrationsIntervalIndex_Object=MibTableColumn
uxSIPRegistrationsIntervalIndex=_UxSIPRegistrationsIntervalIndex_Object((1,3,6,1,4,1,177,15,1,5,16,1,1),_UxSIPRegistrationsIntervalIndex_Type())
uxSIPRegistrationsIntervalIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:uxSIPRegistrationsIntervalIndex.setStatus(_A)
class _UxSIPRegistrationsIntervalNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,24))
_UxSIPRegistrationsIntervalNumber_Type.__name__=_C
_UxSIPRegistrationsIntervalNumber_Object=MibTableColumn
uxSIPRegistrationsIntervalNumber=_UxSIPRegistrationsIntervalNumber_Object((1,3,6,1,4,1,177,15,1,5,16,1,2),_UxSIPRegistrationsIntervalNumber_Type())
uxSIPRegistrationsIntervalNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:uxSIPRegistrationsIntervalNumber.setStatus(_A)
_UxSIPRegistrationsIntervalPeakUsers_Type=PerfIntervalCount
_UxSIPRegistrationsIntervalPeakUsers_Object=MibTableColumn
uxSIPRegistrationsIntervalPeakUsers=_UxSIPRegistrationsIntervalPeakUsers_Object((1,3,6,1,4,1,177,15,1,5,16,1,3),_UxSIPRegistrationsIntervalPeakUsers_Type())
uxSIPRegistrationsIntervalPeakUsers.setMaxAccess(_B)
if mibBuilder.loadTexts:uxSIPRegistrationsIntervalPeakUsers.setStatus(_A)
_UxEthernetPortStatsIntervalTable_Object=MibTable
uxEthernetPortStatsIntervalTable=_UxEthernetPortStatsIntervalTable_Object((1,3,6,1,4,1,177,15,1,5,17))
if mibBuilder.loadTexts:uxEthernetPortStatsIntervalTable.setStatus(_A)
_UxEthernetPortStatsIntervalEntry_Object=MibTableRow
uxEthernetPortStatsIntervalEntry=_UxEthernetPortStatsIntervalEntry_Object((1,3,6,1,4,1,177,15,1,5,17,1))
uxEthernetPortStatsIntervalEntry.setIndexNames((0,_D,_h),(0,_D,_i))
if mibBuilder.loadTexts:uxEthernetPortStatsIntervalEntry.setStatus(_A)
class _UxEthernetPortIntervalIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_UxEthernetPortIntervalIndex_Type.__name__=_C
_UxEthernetPortIntervalIndex_Object=MibTableColumn
uxEthernetPortIntervalIndex=_UxEthernetPortIntervalIndex_Object((1,3,6,1,4,1,177,15,1,5,17,1,1),_UxEthernetPortIntervalIndex_Type())
uxEthernetPortIntervalIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:uxEthernetPortIntervalIndex.setStatus(_A)
class _UxEthernetPortInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,24))
_UxEthernetPortInterval_Type.__name__=_C
_UxEthernetPortInterval_Object=MibTableColumn
uxEthernetPortInterval=_UxEthernetPortInterval_Object((1,3,6,1,4,1,177,15,1,5,17,1,2),_UxEthernetPortInterval_Type())
uxEthernetPortInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:uxEthernetPortInterval.setStatus(_A)
_UxIntervalifInUcastPkts_Type=PerfIntervalCount
_UxIntervalifInUcastPkts_Object=MibTableColumn
uxIntervalifInUcastPkts=_UxIntervalifInUcastPkts_Object((1,3,6,1,4,1,177,15,1,5,17,1,3),_UxIntervalifInUcastPkts_Type())
uxIntervalifInUcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:uxIntervalifInUcastPkts.setStatus(_A)
_UxIntervalifInBroadcastPkts_Type=PerfIntervalCount
_UxIntervalifInBroadcastPkts_Object=MibTableColumn
uxIntervalifInBroadcastPkts=_UxIntervalifInBroadcastPkts_Object((1,3,6,1,4,1,177,15,1,5,17,1,4),_UxIntervalifInBroadcastPkts_Type())
uxIntervalifInBroadcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:uxIntervalifInBroadcastPkts.setStatus(_A)
_UxIntervalifInMulticastPkts_Type=PerfIntervalCount
_UxIntervalifInMulticastPkts_Object=MibTableColumn
uxIntervalifInMulticastPkts=_UxIntervalifInMulticastPkts_Object((1,3,6,1,4,1,177,15,1,5,17,1,5),_UxIntervalifInMulticastPkts_Type())
uxIntervalifInMulticastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:uxIntervalifInMulticastPkts.setStatus(_A)
_UxIntervalifInOctets_Type=PerfIntervalCount
_UxIntervalifInOctets_Object=MibTableColumn
uxIntervalifInOctets=_UxIntervalifInOctets_Object((1,3,6,1,4,1,177,15,1,5,17,1,6),_UxIntervalifInOctets_Type())
uxIntervalifInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:uxIntervalifInOctets.setStatus(_A)
_UxIntervalifInErrors_Type=PerfIntervalCount
_UxIntervalifInErrors_Object=MibTableColumn
uxIntervalifInErrors=_UxIntervalifInErrors_Object((1,3,6,1,4,1,177,15,1,5,17,1,7),_UxIntervalifInErrors_Type())
uxIntervalifInErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:uxIntervalifInErrors.setStatus(_A)
_UxIntervalifInDiscards_Type=PerfIntervalCount
_UxIntervalifInDiscards_Object=MibTableColumn
uxIntervalifInDiscards=_UxIntervalifInDiscards_Object((1,3,6,1,4,1,177,15,1,5,17,1,8),_UxIntervalifInDiscards_Type())
uxIntervalifInDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:uxIntervalifInDiscards.setStatus(_A)
_UxIntervalifInUnknwnProto_Type=PerfIntervalCount
_UxIntervalifInUnknwnProto_Object=MibTableColumn
uxIntervalifInUnknwnProto=_UxIntervalifInUnknwnProto_Object((1,3,6,1,4,1,177,15,1,5,17,1,9),_UxIntervalifInUnknwnProto_Type())
uxIntervalifInUnknwnProto.setMaxAccess(_B)
if mibBuilder.loadTexts:uxIntervalifInUnknwnProto.setStatus(_A)
_UxIntervalifInUndersizedPkts_Type=PerfIntervalCount
_UxIntervalifInUndersizedPkts_Object=MibTableColumn
uxIntervalifInUndersizedPkts=_UxIntervalifInUndersizedPkts_Object((1,3,6,1,4,1,177,15,1,5,17,1,10),_UxIntervalifInUndersizedPkts_Type())
uxIntervalifInUndersizedPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:uxIntervalifInUndersizedPkts.setStatus(_A)
_UxIntervalifInOverSizedPkts_Type=PerfIntervalCount
_UxIntervalifInOverSizedPkts_Object=MibTableColumn
uxIntervalifInOverSizedPkts=_UxIntervalifInOverSizedPkts_Object((1,3,6,1,4,1,177,15,1,5,17,1,11),_UxIntervalifInOverSizedPkts_Type())
uxIntervalifInOverSizedPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:uxIntervalifInOverSizedPkts.setStatus(_A)
_UxIntervalifInFCSErrors_Type=PerfIntervalCount
_UxIntervalifInFCSErrors_Object=MibTableColumn
uxIntervalifInFCSErrors=_UxIntervalifInFCSErrors_Object((1,3,6,1,4,1,177,15,1,5,17,1,12),_UxIntervalifInFCSErrors_Type())
uxIntervalifInFCSErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:uxIntervalifInFCSErrors.setStatus(_A)
_UxIntervalifInAlignErrors_Type=PerfIntervalCount
_UxIntervalifInAlignErrors_Object=MibTableColumn
uxIntervalifInAlignErrors=_UxIntervalifInAlignErrors_Object((1,3,6,1,4,1,177,15,1,5,17,1,13),_UxIntervalifInAlignErrors_Type())
uxIntervalifInAlignErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:uxIntervalifInAlignErrors.setStatus(_A)
_UxIntervalifInFragmentedPkts_Type=PerfIntervalCount
_UxIntervalifInFragmentedPkts_Object=MibTableColumn
uxIntervalifInFragmentedPkts=_UxIntervalifInFragmentedPkts_Object((1,3,6,1,4,1,177,15,1,5,17,1,14),_UxIntervalifInFragmentedPkts_Type())
uxIntervalifInFragmentedPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:uxIntervalifInFragmentedPkts.setStatus(_A)
_UxIntervalifOutUcastPkts_Type=PerfIntervalCount
_UxIntervalifOutUcastPkts_Object=MibTableColumn
uxIntervalifOutUcastPkts=_UxIntervalifOutUcastPkts_Object((1,3,6,1,4,1,177,15,1,5,17,1,15),_UxIntervalifOutUcastPkts_Type())
uxIntervalifOutUcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:uxIntervalifOutUcastPkts.setStatus(_A)
_UxIntervalifOutOctets_Type=PerfIntervalCount
_UxIntervalifOutOctets_Object=MibTableColumn
uxIntervalifOutOctets=_UxIntervalifOutOctets_Object((1,3,6,1,4,1,177,15,1,5,17,1,16),_UxIntervalifOutOctets_Type())
uxIntervalifOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:uxIntervalifOutOctets.setStatus(_A)
_UxIntervalifOutBroadcastPkts_Type=PerfIntervalCount
_UxIntervalifOutBroadcastPkts_Object=MibTableColumn
uxIntervalifOutBroadcastPkts=_UxIntervalifOutBroadcastPkts_Object((1,3,6,1,4,1,177,15,1,5,17,1,17),_UxIntervalifOutBroadcastPkts_Type())
uxIntervalifOutBroadcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:uxIntervalifOutBroadcastPkts.setStatus(_A)
_UxIntervalifOutMulticastPkts_Type=PerfIntervalCount
_UxIntervalifOutMulticastPkts_Object=MibTableColumn
uxIntervalifOutMulticastPkts=_UxIntervalifOutMulticastPkts_Object((1,3,6,1,4,1,177,15,1,5,17,1,18),_UxIntervalifOutMulticastPkts_Type())
uxIntervalifOutMulticastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:uxIntervalifOutMulticastPkts.setStatus(_A)
_UxIntervalifOutErrors_Type=PerfIntervalCount
_UxIntervalifOutErrors_Object=MibTableColumn
uxIntervalifOutErrors=_UxIntervalifOutErrors_Object((1,3,6,1,4,1,177,15,1,5,17,1,19),_UxIntervalifOutErrors_Type())
uxIntervalifOutErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:uxIntervalifOutErrors.setStatus(_A)
_UxIntervalifOutDiscards_Type=PerfIntervalCount
_UxIntervalifOutDiscards_Object=MibTableColumn
uxIntervalifOutDiscards=_UxIntervalifOutDiscards_Object((1,3,6,1,4,1,177,15,1,5,17,1,20),_UxIntervalifOutDiscards_Type())
uxIntervalifOutDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:uxIntervalifOutDiscards.setStatus(_A)
_UxIntervalifOutLateCollissions_Type=PerfIntervalCount
_UxIntervalifOutLateCollissions_Object=MibTableColumn
uxIntervalifOutLateCollissions=_UxIntervalifOutLateCollissions_Object((1,3,6,1,4,1,177,15,1,5,17,1,21),_UxIntervalifOutLateCollissions_Type())
uxIntervalifOutLateCollissions.setMaxAccess(_B)
if mibBuilder.loadTexts:uxIntervalifOutLateCollissions.setStatus(_A)
_UxIntervalifOutDeferredTransmissions_Type=PerfIntervalCount
_UxIntervalifOutDeferredTransmissions_Object=MibTableColumn
uxIntervalifOutDeferredTransmissions=_UxIntervalifOutDeferredTransmissions_Object((1,3,6,1,4,1,177,15,1,5,17,1,22),_UxIntervalifOutDeferredTransmissions_Type())
uxIntervalifOutDeferredTransmissions.setMaxAccess(_B)
if mibBuilder.loadTexts:uxIntervalifOutDeferredTransmissions.setStatus(_A)
_UxEthernetPortStatsCurrentTable_Object=MibTable
uxEthernetPortStatsCurrentTable=_UxEthernetPortStatsCurrentTable_Object((1,3,6,1,4,1,177,15,1,5,18))
if mibBuilder.loadTexts:uxEthernetPortStatsCurrentTable.setStatus(_A)
_UxEthernetPortStatsCurrentEntry_Object=MibTableRow
uxEthernetPortStatsCurrentEntry=_UxEthernetPortStatsCurrentEntry_Object((1,3,6,1,4,1,177,15,1,5,18,1))
uxEthernetPortStatsCurrentEntry.setIndexNames((0,_D,_j))
if mibBuilder.loadTexts:uxEthernetPortStatsCurrentEntry.setStatus(_A)
class _UxEthernetPortCurrentIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_UxEthernetPortCurrentIndex_Type.__name__=_C
_UxEthernetPortCurrentIndex_Object=MibTableColumn
uxEthernetPortCurrentIndex=_UxEthernetPortCurrentIndex_Object((1,3,6,1,4,1,177,15,1,5,18,1,1),_UxEthernetPortCurrentIndex_Type())
uxEthernetPortCurrentIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:uxEthernetPortCurrentIndex.setStatus(_A)
_UxCurrentifInUcastPkts_Type=PerfCurrentCount
_UxCurrentifInUcastPkts_Object=MibTableColumn
uxCurrentifInUcastPkts=_UxCurrentifInUcastPkts_Object((1,3,6,1,4,1,177,15,1,5,18,1,2),_UxCurrentifInUcastPkts_Type())
uxCurrentifInUcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:uxCurrentifInUcastPkts.setStatus(_A)
_UxCurrentifInBroadcastPkts_Type=PerfCurrentCount
_UxCurrentifInBroadcastPkts_Object=MibTableColumn
uxCurrentifInBroadcastPkts=_UxCurrentifInBroadcastPkts_Object((1,3,6,1,4,1,177,15,1,5,18,1,3),_UxCurrentifInBroadcastPkts_Type())
uxCurrentifInBroadcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:uxCurrentifInBroadcastPkts.setStatus(_A)
_UxCurrentifInMulticastPkts_Type=PerfCurrentCount
_UxCurrentifInMulticastPkts_Object=MibTableColumn
uxCurrentifInMulticastPkts=_UxCurrentifInMulticastPkts_Object((1,3,6,1,4,1,177,15,1,5,18,1,4),_UxCurrentifInMulticastPkts_Type())
uxCurrentifInMulticastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:uxCurrentifInMulticastPkts.setStatus(_A)
_UxCurrentifInOctets_Type=PerfCurrentCount
_UxCurrentifInOctets_Object=MibTableColumn
uxCurrentifInOctets=_UxCurrentifInOctets_Object((1,3,6,1,4,1,177,15,1,5,18,1,5),_UxCurrentifInOctets_Type())
uxCurrentifInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:uxCurrentifInOctets.setStatus(_A)
_UxCurrentifInErrors_Type=PerfCurrentCount
_UxCurrentifInErrors_Object=MibTableColumn
uxCurrentifInErrors=_UxCurrentifInErrors_Object((1,3,6,1,4,1,177,15,1,5,18,1,6),_UxCurrentifInErrors_Type())
uxCurrentifInErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:uxCurrentifInErrors.setStatus(_A)
_UxCurrentifInDiscards_Type=PerfCurrentCount
_UxCurrentifInDiscards_Object=MibTableColumn
uxCurrentifInDiscards=_UxCurrentifInDiscards_Object((1,3,6,1,4,1,177,15,1,5,18,1,7),_UxCurrentifInDiscards_Type())
uxCurrentifInDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:uxCurrentifInDiscards.setStatus(_A)
_UxCurrentifInUnknwnProto_Type=PerfCurrentCount
_UxCurrentifInUnknwnProto_Object=MibTableColumn
uxCurrentifInUnknwnProto=_UxCurrentifInUnknwnProto_Object((1,3,6,1,4,1,177,15,1,5,18,1,8),_UxCurrentifInUnknwnProto_Type())
uxCurrentifInUnknwnProto.setMaxAccess(_B)
if mibBuilder.loadTexts:uxCurrentifInUnknwnProto.setStatus(_A)
_UxCurrentifInUndersizedPkts_Type=PerfCurrentCount
_UxCurrentifInUndersizedPkts_Object=MibTableColumn
uxCurrentifInUndersizedPkts=_UxCurrentifInUndersizedPkts_Object((1,3,6,1,4,1,177,15,1,5,18,1,9),_UxCurrentifInUndersizedPkts_Type())
uxCurrentifInUndersizedPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:uxCurrentifInUndersizedPkts.setStatus(_A)
_UxCurrentifInOverSizedPkts_Type=PerfCurrentCount
_UxCurrentifInOverSizedPkts_Object=MibTableColumn
uxCurrentifInOverSizedPkts=_UxCurrentifInOverSizedPkts_Object((1,3,6,1,4,1,177,15,1,5,18,1,10),_UxCurrentifInOverSizedPkts_Type())
uxCurrentifInOverSizedPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:uxCurrentifInOverSizedPkts.setStatus(_A)
_UxCurrentifInFCSErrors_Type=PerfCurrentCount
_UxCurrentifInFCSErrors_Object=MibTableColumn
uxCurrentifInFCSErrors=_UxCurrentifInFCSErrors_Object((1,3,6,1,4,1,177,15,1,5,18,1,11),_UxCurrentifInFCSErrors_Type())
uxCurrentifInFCSErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:uxCurrentifInFCSErrors.setStatus(_A)
_UxCurrentifInAlignErrors_Type=PerfCurrentCount
_UxCurrentifInAlignErrors_Object=MibTableColumn
uxCurrentifInAlignErrors=_UxCurrentifInAlignErrors_Object((1,3,6,1,4,1,177,15,1,5,18,1,12),_UxCurrentifInAlignErrors_Type())
uxCurrentifInAlignErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:uxCurrentifInAlignErrors.setStatus(_A)
_UxCurrentifInFragmentedPkts_Type=PerfCurrentCount
_UxCurrentifInFragmentedPkts_Object=MibTableColumn
uxCurrentifInFragmentedPkts=_UxCurrentifInFragmentedPkts_Object((1,3,6,1,4,1,177,15,1,5,18,1,13),_UxCurrentifInFragmentedPkts_Type())
uxCurrentifInFragmentedPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:uxCurrentifInFragmentedPkts.setStatus(_A)
_UxCurrentifOutUcastPkts_Type=PerfCurrentCount
_UxCurrentifOutUcastPkts_Object=MibTableColumn
uxCurrentifOutUcastPkts=_UxCurrentifOutUcastPkts_Object((1,3,6,1,4,1,177,15,1,5,18,1,14),_UxCurrentifOutUcastPkts_Type())
uxCurrentifOutUcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:uxCurrentifOutUcastPkts.setStatus(_A)
_UxCurrentifOutOctets_Type=PerfCurrentCount
_UxCurrentifOutOctets_Object=MibTableColumn
uxCurrentifOutOctets=_UxCurrentifOutOctets_Object((1,3,6,1,4,1,177,15,1,5,18,1,15),_UxCurrentifOutOctets_Type())
uxCurrentifOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:uxCurrentifOutOctets.setStatus(_A)
_UxCurrentifOutBroadcastPkts_Type=PerfCurrentCount
_UxCurrentifOutBroadcastPkts_Object=MibTableColumn
uxCurrentifOutBroadcastPkts=_UxCurrentifOutBroadcastPkts_Object((1,3,6,1,4,1,177,15,1,5,18,1,16),_UxCurrentifOutBroadcastPkts_Type())
uxCurrentifOutBroadcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:uxCurrentifOutBroadcastPkts.setStatus(_A)
_UxCurrentifOutMulticastPkts_Type=PerfCurrentCount
_UxCurrentifOutMulticastPkts_Object=MibTableColumn
uxCurrentifOutMulticastPkts=_UxCurrentifOutMulticastPkts_Object((1,3,6,1,4,1,177,15,1,5,18,1,17),_UxCurrentifOutMulticastPkts_Type())
uxCurrentifOutMulticastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:uxCurrentifOutMulticastPkts.setStatus(_A)
_UxCurrentifOutErrors_Type=PerfCurrentCount
_UxCurrentifOutErrors_Object=MibTableColumn
uxCurrentifOutErrors=_UxCurrentifOutErrors_Object((1,3,6,1,4,1,177,15,1,5,18,1,18),_UxCurrentifOutErrors_Type())
uxCurrentifOutErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:uxCurrentifOutErrors.setStatus(_A)
_UxCurrentifOutDiscards_Type=PerfCurrentCount
_UxCurrentifOutDiscards_Object=MibTableColumn
uxCurrentifOutDiscards=_UxCurrentifOutDiscards_Object((1,3,6,1,4,1,177,15,1,5,18,1,19),_UxCurrentifOutDiscards_Type())
uxCurrentifOutDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:uxCurrentifOutDiscards.setStatus(_A)
_UxCurrentifOutLateCollissions_Type=PerfCurrentCount
_UxCurrentifOutLateCollissions_Object=MibTableColumn
uxCurrentifOutLateCollissions=_UxCurrentifOutLateCollissions_Object((1,3,6,1,4,1,177,15,1,5,18,1,20),_UxCurrentifOutLateCollissions_Type())
uxCurrentifOutLateCollissions.setMaxAccess(_B)
if mibBuilder.loadTexts:uxCurrentifOutLateCollissions.setStatus(_A)
_UxCurrentifOutDeferredTransmissions_Type=PerfCurrentCount
_UxCurrentifOutDeferredTransmissions_Object=MibTableColumn
uxCurrentifOutDeferredTransmissions=_UxCurrentifOutDeferredTransmissions_Object((1,3,6,1,4,1,177,15,1,5,18,1,21),_UxCurrentifOutDeferredTransmissions_Type())
uxCurrentifOutDeferredTransmissions.setMaxAccess(_B)
if mibBuilder.loadTexts:uxCurrentifOutDeferredTransmissions.setStatus(_A)
_UxGlobalCallCounters_ObjectIdentity=ObjectIdentity
uxGlobalCallCounters=_UxGlobalCallCounters_ObjectIdentity((1,3,6,1,4,1,177,15,1,5,19))
_UxNumCallAttempts_Type=Integer32
_UxNumCallAttempts_Object=MibScalar
uxNumCallAttempts=_UxNumCallAttempts_Object((1,3,6,1,4,1,177,15,1,5,19,1),_UxNumCallAttempts_Type())
uxNumCallAttempts.setMaxAccess(_B)
if mibBuilder.loadTexts:uxNumCallAttempts.setStatus(_A)
_UxNumCallSucceeded_Type=Integer32
_UxNumCallSucceeded_Object=MibScalar
uxNumCallSucceeded=_UxNumCallSucceeded_Object((1,3,6,1,4,1,177,15,1,5,19,2),_UxNumCallSucceeded_Type())
uxNumCallSucceeded.setMaxAccess(_B)
if mibBuilder.loadTexts:uxNumCallSucceeded.setStatus(_A)
_UxNumCallFailed_Type=Integer32
_UxNumCallFailed_Object=MibScalar
uxNumCallFailed=_UxNumCallFailed_Object((1,3,6,1,4,1,177,15,1,5,19,3),_UxNumCallFailed_Type())
uxNumCallFailed.setMaxAccess(_B)
if mibBuilder.loadTexts:uxNumCallFailed.setStatus(_A)
_UxNumCallCurrentlyUp_Type=Integer32
_UxNumCallCurrentlyUp_Object=MibScalar
uxNumCallCurrentlyUp=_UxNumCallCurrentlyUp_Object((1,3,6,1,4,1,177,15,1,5,19,4),_UxNumCallCurrentlyUp_Type())
uxNumCallCurrentlyUp.setMaxAccess(_B)
if mibBuilder.loadTexts:uxNumCallCurrentlyUp.setStatus(_A)
_UxNumCallCurrentlyTransient_Type=Integer32
_UxNumCallCurrentlyTransient_Object=MibScalar
uxNumCallCurrentlyTransient=_UxNumCallCurrentlyTransient_Object((1,3,6,1,4,1,177,15,1,5,19,5),_UxNumCallCurrentlyTransient_Type())
uxNumCallCurrentlyTransient.setMaxAccess(_B)
if mibBuilder.loadTexts:uxNumCallCurrentlyTransient.setStatus(_A)
_UxNumInternalGlares_Type=Integer32
_UxNumInternalGlares_Object=MibScalar
uxNumInternalGlares=_UxNumInternalGlares_Object((1,3,6,1,4,1,177,15,1,5,19,6),_UxNumInternalGlares_Type())
uxNumInternalGlares.setMaxAccess(_B)
if mibBuilder.loadTexts:uxNumInternalGlares.setStatus(_A)
_UxNumExternalGlares_Type=Integer32
_UxNumExternalGlares_Object=MibScalar
uxNumExternalGlares=_UxNumExternalGlares_Object((1,3,6,1,4,1,177,15,1,5,19,7),_UxNumExternalGlares_Type())
uxNumExternalGlares.setMaxAccess(_B)
if mibBuilder.loadTexts:uxNumExternalGlares.setStatus(_A)
_UxNumCallAbandonedNoTrunk_Type=Integer32
_UxNumCallAbandonedNoTrunk_Object=MibScalar
uxNumCallAbandonedNoTrunk=_UxNumCallAbandonedNoTrunk_Object((1,3,6,1,4,1,177,15,1,5,19,8),_UxNumCallAbandonedNoTrunk_Type())
uxNumCallAbandonedNoTrunk.setMaxAccess(_B)
if mibBuilder.loadTexts:uxNumCallAbandonedNoTrunk.setStatus(_A)
_UxNumCallUnAnswered_Type=Integer32
_UxNumCallUnAnswered_Object=MibScalar
uxNumCallUnAnswered=_UxNumCallUnAnswered_Object((1,3,6,1,4,1,177,15,1,5,19,9),_UxNumCallUnAnswered_Type())
uxNumCallUnAnswered.setMaxAccess(_B)
if mibBuilder.loadTexts:uxNumCallUnAnswered.setStatus(_A)
_UxTraps_ObjectIdentity=ObjectIdentity
uxTraps=_UxTraps_ObjectIdentity((1,3,6,1,4,1,177,15,2))
mibBuilder.exportSymbols(_D,**{'net':net,'ux':ux,'uxObjects':uxObjects,'ipSystem':ipSystem,'sysVersion':sysVersion,'sysBuildNumber':sysBuildNumber,'ipTelephony':ipTelephony,'callStatistics':callStatistics,'uxPortTable':uxPortTable,'uxPortEntry':uxPortEntry,_I:uxPTIndex,'uxPTShelf':uxPTShelf,'uxPTSlot':uxPTSlot,'uxPTPort':uxPTPort,'uxPTCurrentCalls':uxPTCurrentCalls,'uxPTTotalCalls':uxPTTotalCalls,'uxPTConnectedCalls':uxPTConnectedCalls,'uxPTRefusedCalls':uxPTRefusedCalls,'uxPTErroredCalls':uxPTErroredCalls,'uxPTEgressCallAttempts':uxPTEgressCallAttempts,'uxPTEgressCallsAccepted':uxPTEgressCallsAccepted,'uxPTEgressCallsCompleted':uxPTEgressCallsCompleted,'uxPTEgressCallsRejected':uxPTEgressCallsRejected,'uxPTIngressCallAttempts':uxPTIngressCallAttempts,'uxPTIngressCallsAccepted':uxPTIngressCallsAccepted,'uxPTIngressCallsCompleted':uxPTIngressCallsCompleted,'uxPTIngressCallsRejected':uxPTIngressCallsRejected,'uxPTBlockedCalls':uxPTBlockedCalls,'uxPTEgressBlockedCalls':uxPTEgressBlockedCalls,'uxPTIngressBlockedCalls':uxPTIngressBlockedCalls,'uxPTEgressCurrentCalls':uxPTEgressCurrentCalls,'uxPTIngressCurrentCalls':uxPTIngressCurrentCalls,'uxPTBHCARate':uxPTBHCARate,'uxPTBHCCRate':uxPTBHCCRate,'uxCallRtTablesTable':uxCallRtTablesTable,'uxCallRtTablesEntry':uxCallRtTablesEntry,_J:uxCallRtTablesTableIndex,'uxDesc':uxDesc,'uxCallRtSequence':uxCallRtSequence,'uxCallRtTable':uxCallRtTable,'uxCallRtEntry':uxCallRtEntry,_K:uxCallRtTablesIndex,_L:uxCallRtIndex,'uxDescription':uxDescription,'uxAdminState':uxAdminState,'uxRoutePriority':uxRoutePriority,'uxSignalingGroupList':uxSignalingGroupList,'uxQualityMetricCalls':uxQualityMetricCalls,'uxQualityMetricTime':uxQualityMetricTime,'uxQualityMinASRThreshold':uxQualityMinASRThreshold,'uxQualityMaxRoundTripDelayThreshold':uxQualityMaxRoundTripDelayThreshold,'uxQualityMaxJitterThreshold':uxQualityMaxJitterThreshold,'uxQualityMinMOSThreshold':uxQualityMinMOSThreshold,'uxSGTable':uxSGTable,'uxSGEntry':uxSGEntry,_M:uxSGEntryIndex,'uxSGDescription':uxSGDescription,'uxSGType':uxSGType,'uxSGAdminState':uxSGAdminState,'uxSGServiceState':uxSGServiceState,'uxSipServerTable':uxSipServerTable,'uxSipServerEntry':uxSipServerEntry,_N:uxSGIndex,_O:uxSipServerIndex,'uxSipSvrPriority':uxSipSvrPriority,'uxSipSvrHost':uxSipSvrHost,'uxSipSvrPort':uxSipSvrPort,'uxSipSvrTransProtocol':uxSipSvrTransProtocol,'uxChannelStatusTable':uxChannelStatusTable,'uxChannelStatusEntry':uxChannelStatusEntry,_P:uxChShelfNumber,_Q:uxChSlotNumber,_R:uxChPortNumber,_S:uxChChannelNumber,'uxChAdminState':uxChAdminState,'uxChOperState':uxChOperState,'uxChInUseSeconds':uxChInUseSeconds,'uxSGStatsCurrentTable':uxSGStatsCurrentTable,'uxSGStatsCurrentEntry':uxSGStatsCurrentEntry,_T:uxSGCurrentIndex,'uxSGCurrentPeakChannelUsage':uxSGCurrentPeakChannelUsage,'uxSGCurrentCompletedCalls':uxSGCurrentCompletedCalls,'uxSGCurrentIncompleteCalls':uxSGCurrentIncompleteCalls,'uxSGStatsIntervalTable':uxSGStatsIntervalTable,'uxSGStatsIntervalEntry':uxSGStatsIntervalEntry,_U:uxSGIntervalIndex,_V:uxSGIntervalNumber,'uxSGIntervalPeakChannelUsage':uxSGIntervalPeakChannelUsage,'uxSGIntervalCompletedCalls':uxSGIntervalCompletedCalls,'uxSGIntervalIncompleteCalls':uxSGIntervalIncompleteCalls,'uxCallRtStatsCurrentTable':uxCallRtStatsCurrentTable,'uxCallRtStatsCurrentEntry':uxCallRtStatsCurrentEntry,_W:uxCallRtCurrentTablesIndex,_X:uxCallRtCurrentEntryIndex,'uxCallRtCurrentRuleUsage':uxCallRtCurrentRuleUsage,'uxCallRtStatsIntervalTable':uxCallRtStatsIntervalTable,'uxCallRtStatsIntervalEntry':uxCallRtStatsIntervalEntry,_Y:uxCallRtIntervalTablesIndex,_Z:uxCallRtIntervalEntryIndex,_a:uxCallRtIntervalNumber,'uxCallRtIntervalRuleUsage':uxCallRtIntervalRuleUsage,'uxCallRtStatsTotalTable':uxCallRtStatsTotalTable,'uxCallRtStatsTotalEntry':uxCallRtStatsTotalEntry,_b:uxCallRtTotalTablesIndex,_c:uxCallRtTotalEntryIndex,'uxCallRtTotalRuleUsage':uxCallRtTotalRuleUsage,'uxLicenseStatsIntervalTable':uxLicenseStatsIntervalTable,'uxLicenseStatsIntervalEntry':uxLicenseStatsIntervalEntry,_d:uxLicenseIntervalNumber,'uxLicenseIntervalPeakSIPCall':uxLicenseIntervalPeakSIPCall,'uxLicenseIntervalPeakSIPRegistration':uxLicenseIntervalPeakSIPRegistration,'uxLicenseIntervalPeakTDMChannel':uxLicenseIntervalPeakTDMChannel,'uxLicenseIntervalPeakDSP':uxLicenseIntervalPeakDSP,'uxSIPRegistrationsStatsCurrentTable':uxSIPRegistrationsStatsCurrentTable,'uxSIPRegistrationsStatsCurrentEntry':uxSIPRegistrationsStatsCurrentEntry,_e:uxSIPRegistrationsCurrentIndex,'uxSIPRegistrationsCurrentPeakUsers':uxSIPRegistrationsCurrentPeakUsers,'uxSIPRegistrationsStatsIntervalTable':uxSIPRegistrationsStatsIntervalTable,'uxSIPRegistrationsStatsIntervalEntry':uxSIPRegistrationsStatsIntervalEntry,_f:uxSIPRegistrationsIntervalIndex,_g:uxSIPRegistrationsIntervalNumber,'uxSIPRegistrationsIntervalPeakUsers':uxSIPRegistrationsIntervalPeakUsers,'uxEthernetPortStatsIntervalTable':uxEthernetPortStatsIntervalTable,'uxEthernetPortStatsIntervalEntry':uxEthernetPortStatsIntervalEntry,_h:uxEthernetPortIntervalIndex,_i:uxEthernetPortInterval,'uxIntervalifInUcastPkts':uxIntervalifInUcastPkts,'uxIntervalifInBroadcastPkts':uxIntervalifInBroadcastPkts,'uxIntervalifInMulticastPkts':uxIntervalifInMulticastPkts,'uxIntervalifInOctets':uxIntervalifInOctets,'uxIntervalifInErrors':uxIntervalifInErrors,'uxIntervalifInDiscards':uxIntervalifInDiscards,'uxIntervalifInUnknwnProto':uxIntervalifInUnknwnProto,'uxIntervalifInUndersizedPkts':uxIntervalifInUndersizedPkts,'uxIntervalifInOverSizedPkts':uxIntervalifInOverSizedPkts,'uxIntervalifInFCSErrors':uxIntervalifInFCSErrors,'uxIntervalifInAlignErrors':uxIntervalifInAlignErrors,'uxIntervalifInFragmentedPkts':uxIntervalifInFragmentedPkts,'uxIntervalifOutUcastPkts':uxIntervalifOutUcastPkts,'uxIntervalifOutOctets':uxIntervalifOutOctets,'uxIntervalifOutBroadcastPkts':uxIntervalifOutBroadcastPkts,'uxIntervalifOutMulticastPkts':uxIntervalifOutMulticastPkts,'uxIntervalifOutErrors':uxIntervalifOutErrors,'uxIntervalifOutDiscards':uxIntervalifOutDiscards,'uxIntervalifOutLateCollissions':uxIntervalifOutLateCollissions,'uxIntervalifOutDeferredTransmissions':uxIntervalifOutDeferredTransmissions,'uxEthernetPortStatsCurrentTable':uxEthernetPortStatsCurrentTable,'uxEthernetPortStatsCurrentEntry':uxEthernetPortStatsCurrentEntry,_j:uxEthernetPortCurrentIndex,'uxCurrentifInUcastPkts':uxCurrentifInUcastPkts,'uxCurrentifInBroadcastPkts':uxCurrentifInBroadcastPkts,'uxCurrentifInMulticastPkts':uxCurrentifInMulticastPkts,'uxCurrentifInOctets':uxCurrentifInOctets,'uxCurrentifInErrors':uxCurrentifInErrors,'uxCurrentifInDiscards':uxCurrentifInDiscards,'uxCurrentifInUnknwnProto':uxCurrentifInUnknwnProto,'uxCurrentifInUndersizedPkts':uxCurrentifInUndersizedPkts,'uxCurrentifInOverSizedPkts':uxCurrentifInOverSizedPkts,'uxCurrentifInFCSErrors':uxCurrentifInFCSErrors,'uxCurrentifInAlignErrors':uxCurrentifInAlignErrors,'uxCurrentifInFragmentedPkts':uxCurrentifInFragmentedPkts,'uxCurrentifOutUcastPkts':uxCurrentifOutUcastPkts,'uxCurrentifOutOctets':uxCurrentifOutOctets,'uxCurrentifOutBroadcastPkts':uxCurrentifOutBroadcastPkts,'uxCurrentifOutMulticastPkts':uxCurrentifOutMulticastPkts,'uxCurrentifOutErrors':uxCurrentifOutErrors,'uxCurrentifOutDiscards':uxCurrentifOutDiscards,'uxCurrentifOutLateCollissions':uxCurrentifOutLateCollissions,'uxCurrentifOutDeferredTransmissions':uxCurrentifOutDeferredTransmissions,'uxGlobalCallCounters':uxGlobalCallCounters,'uxNumCallAttempts':uxNumCallAttempts,'uxNumCallSucceeded':uxNumCallSucceeded,'uxNumCallFailed':uxNumCallFailed,'uxNumCallCurrentlyUp':uxNumCallCurrentlyUp,'uxNumCallCurrentlyTransient':uxNumCallCurrentlyTransient,'uxNumInternalGlares':uxNumInternalGlares,'uxNumExternalGlares':uxNumExternalGlares,'uxNumCallAbandonedNoTrunk':uxNumCallAbandonedNoTrunk,'uxNumCallUnAnswered':uxNumCallUnAnswered,'uxTraps':uxTraps})