_R='cadOverloadGroup'
_Q='cadMemoryGroup'
_P='cadProcessGroup'
_O='cadOvCardId'
_N='cadMeCardId'
_M='cadCpuCardId'
_L='Integer32'
_K='cardNumber'
_J='cadProcessOverloadStatus'
_I='not-accessible'
_H='trapSeverity'
_G='trapCounter'
_F='nanoseconds'
_E='OverloadStatus'
_D='CADANT-CMTS-EQUIPMENT-MIB'
_C='CADANT-CMTS-PROCESS-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cardNumber,trapCounter,trapSeverity=mibBuilder.importSymbols(_D,_K,_G,_H)
cadSystem,=mibBuilder.importSymbols('CADANT-PRODUCTS-MIB','cadSystem')
CardId,OverloadStatus=mibBuilder.importSymbols('CADANT-TC','CardId',_E)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_L,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeInterval,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TimeInterval','TruthValue')
cadProcessMib=ModuleIdentity((1,3,6,1,4,1,4998,1,1,5,3))
if mibBuilder.loadTexts:cadProcessMib.setRevisions(('2013-07-02 00:00','2011-05-22 00:00','2010-12-20 00:00','2005-10-20 00:00','2003-03-29 00:00','2003-03-20 00:00','2002-04-23 00:00'))
_CadProcessTraps_ObjectIdentity=ObjectIdentity
cadProcessTraps=_CadProcessTraps_ObjectIdentity((1,3,6,1,4,1,4998,1,1,5,3,0))
_CadProcessGroup_ObjectIdentity=ObjectIdentity
cadProcessGroup=_CadProcessGroup_ObjectIdentity((1,3,6,1,4,1,4998,1,1,5,3,1))
_CadCpu_Object=MibTable
cadCpu=_CadCpu_Object((1,3,6,1,4,1,4998,1,1,5,3,1,1))
if mibBuilder.loadTexts:cadCpu.setStatus(_A)
_CadCpuEntry_Object=MibTableRow
cadCpuEntry=_CadCpuEntry_Object((1,3,6,1,4,1,4998,1,1,5,3,1,1,1))
cadCpuEntry.setIndexNames((0,_C,_M))
if mibBuilder.loadTexts:cadCpuEntry.setStatus(_A)
_CadCpuCardId_Type=CardId
_CadCpuCardId_Object=MibTableColumn
cadCpuCardId=_CadCpuCardId_Object((1,3,6,1,4,1,4998,1,1,5,3,1,1,1,1),_CadCpuCardId_Type())
cadCpuCardId.setMaxAccess(_I)
if mibBuilder.loadTexts:cadCpuCardId.setStatus(_A)
_CadCpuRecentTime_Type=Counter64
_CadCpuRecentTime_Object=MibTableColumn
cadCpuRecentTime=_CadCpuRecentTime_Object((1,3,6,1,4,1,4998,1,1,5,3,1,1,1,2),_CadCpuRecentTime_Type())
cadCpuRecentTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cadCpuRecentTime.setStatus(_A)
if mibBuilder.loadTexts:cadCpuRecentTime.setUnits(_F)
_CadCpuTotalTime_Type=Counter64
_CadCpuTotalTime_Object=MibTableColumn
cadCpuTotalTime=_CadCpuTotalTime_Object((1,3,6,1,4,1,4998,1,1,5,3,1,1,1,3),_CadCpuTotalTime_Type())
cadCpuTotalTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cadCpuTotalTime.setStatus(_A)
if mibBuilder.loadTexts:cadCpuTotalTime.setUnits(_F)
_CadIdleCpuRecentTime_Type=Counter64
_CadIdleCpuRecentTime_Object=MibTableColumn
cadIdleCpuRecentTime=_CadIdleCpuRecentTime_Object((1,3,6,1,4,1,4998,1,1,5,3,1,1,1,4),_CadIdleCpuRecentTime_Type())
cadIdleCpuRecentTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cadIdleCpuRecentTime.setStatus(_A)
if mibBuilder.loadTexts:cadIdleCpuRecentTime.setUnits(_F)
_CadIdleCpuTotalTime_Type=Counter64
_CadIdleCpuTotalTime_Object=MibTableColumn
cadIdleCpuTotalTime=_CadIdleCpuTotalTime_Object((1,3,6,1,4,1,4998,1,1,5,3,1,1,1,5),_CadIdleCpuTotalTime_Type())
cadIdleCpuTotalTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cadIdleCpuTotalTime.setStatus(_A)
if mibBuilder.loadTexts:cadIdleCpuTotalTime.setUnits(_F)
_CadSwitchRecentCount_Type=Counter64
_CadSwitchRecentCount_Object=MibTableColumn
cadSwitchRecentCount=_CadSwitchRecentCount_Object((1,3,6,1,4,1,4998,1,1,5,3,1,1,1,6),_CadSwitchRecentCount_Type())
cadSwitchRecentCount.setMaxAccess(_B)
if mibBuilder.loadTexts:cadSwitchRecentCount.setStatus(_A)
_CadSwitchTotalCount_Type=Counter64
_CadSwitchTotalCount_Object=MibTableColumn
cadSwitchTotalCount=_CadSwitchTotalCount_Object((1,3,6,1,4,1,4998,1,1,5,3,1,1,1,7),_CadSwitchTotalCount_Type())
cadSwitchTotalCount.setMaxAccess(_B)
if mibBuilder.loadTexts:cadSwitchTotalCount.setStatus(_A)
class _CadIdleCpuRecentPercent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CadIdleCpuRecentPercent_Type.__name__=_L
_CadIdleCpuRecentPercent_Object=MibTableColumn
cadIdleCpuRecentPercent=_CadIdleCpuRecentPercent_Object((1,3,6,1,4,1,4998,1,1,5,3,1,1,1,8),_CadIdleCpuRecentPercent_Type())
cadIdleCpuRecentPercent.setMaxAccess(_B)
if mibBuilder.loadTexts:cadIdleCpuRecentPercent.setStatus(_A)
if mibBuilder.loadTexts:cadIdleCpuRecentPercent.setUnits('percent')
_CadMemoryGroup_ObjectIdentity=ObjectIdentity
cadMemoryGroup=_CadMemoryGroup_ObjectIdentity((1,3,6,1,4,1,4998,1,1,5,3,2))
_CadMemory_Object=MibTable
cadMemory=_CadMemory_Object((1,3,6,1,4,1,4998,1,1,5,3,2,1))
if mibBuilder.loadTexts:cadMemory.setStatus(_A)
_CadMemoryEntry_Object=MibTableRow
cadMemoryEntry=_CadMemoryEntry_Object((1,3,6,1,4,1,4998,1,1,5,3,2,1,1))
cadMemoryEntry.setIndexNames((0,_C,_N))
if mibBuilder.loadTexts:cadMemoryEntry.setStatus(_A)
_CadMeCardId_Type=CardId
_CadMeCardId_Object=MibTableColumn
cadMeCardId=_CadMeCardId_Object((1,3,6,1,4,1,4998,1,1,5,3,2,1,1,1),_CadMeCardId_Type())
cadMeCardId.setMaxAccess(_I)
if mibBuilder.loadTexts:cadMeCardId.setStatus(_A)
_CadMeHeapSize_Type=Unsigned32
_CadMeHeapSize_Object=MibTableColumn
cadMeHeapSize=_CadMeHeapSize_Object((1,3,6,1,4,1,4998,1,1,5,3,2,1,1,2),_CadMeHeapSize_Type())
cadMeHeapSize.setMaxAccess(_B)
if mibBuilder.loadTexts:cadMeHeapSize.setStatus(_A)
if mibBuilder.loadTexts:cadMeHeapSize.setUnits('bytes')
_CadMeHeapRemaining_Type=Unsigned32
_CadMeHeapRemaining_Object=MibTableColumn
cadMeHeapRemaining=_CadMeHeapRemaining_Object((1,3,6,1,4,1,4998,1,1,5,3,2,1,1,3),_CadMeHeapRemaining_Type())
cadMeHeapRemaining.setMaxAccess(_B)
if mibBuilder.loadTexts:cadMeHeapRemaining.setStatus(_A)
if mibBuilder.loadTexts:cadMeHeapRemaining.setUnits('bytes')
_CadOverloadGroup_ObjectIdentity=ObjectIdentity
cadOverloadGroup=_CadOverloadGroup_ObjectIdentity((1,3,6,1,4,1,4998,1,1,5,3,3))
_CadOverload_Object=MibTable
cadOverload=_CadOverload_Object((1,3,6,1,4,1,4998,1,1,5,3,3,1))
if mibBuilder.loadTexts:cadOverload.setStatus(_A)
_CadOverloadEntry_Object=MibTableRow
cadOverloadEntry=_CadOverloadEntry_Object((1,3,6,1,4,1,4998,1,1,5,3,3,1,1))
cadOverloadEntry.setIndexNames((0,_C,_O))
if mibBuilder.loadTexts:cadOverloadEntry.setStatus(_A)
_CadOvCardId_Type=CardId
_CadOvCardId_Object=MibTableColumn
cadOvCardId=_CadOvCardId_Object((1,3,6,1,4,1,4998,1,1,5,3,3,1,1,1),_CadOvCardId_Type())
cadOvCardId.setMaxAccess(_I)
if mibBuilder.loadTexts:cadOvCardId.setStatus(_A)
class _CadOvCpuStatus_Type(OverloadStatus):defaultValue=1
_CadOvCpuStatus_Type.__name__=_E
_CadOvCpuStatus_Object=MibTableColumn
cadOvCpuStatus=_CadOvCpuStatus_Object((1,3,6,1,4,1,4998,1,1,5,3,3,1,1,2),_CadOvCpuStatus_Type())
cadOvCpuStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cadOvCpuStatus.setStatus(_A)
class _CadOvMemStatus_Type(OverloadStatus):defaultValue=1
_CadOvMemStatus_Type.__name__=_E
_CadOvMemStatus_Object=MibTableColumn
cadOvMemStatus=_CadOvMemStatus_Object((1,3,6,1,4,1,4998,1,1,5,3,3,1,1,3),_CadOvMemStatus_Type())
cadOvMemStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cadOvMemStatus.setStatus('deprecated')
class _CadOvSysCpuStatus_Type(OverloadStatus):defaultValue=1
_CadOvSysCpuStatus_Type.__name__=_E
_CadOvSysCpuStatus_Object=MibScalar
cadOvSysCpuStatus=_CadOvSysCpuStatus_Object((1,3,6,1,4,1,4998,1,1,5,3,3,2),_CadOvSysCpuStatus_Type())
cadOvSysCpuStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cadOvSysCpuStatus.setStatus(_A)
class _CadOvSysMemStatus_Type(OverloadStatus):defaultValue=1
_CadOvSysMemStatus_Type.__name__=_E
_CadOvSysMemStatus_Object=MibScalar
cadOvSysMemStatus=_CadOvSysMemStatus_Object((1,3,6,1,4,1,4998,1,1,5,3,3,3),_CadOvSysMemStatus_Type())
cadOvSysMemStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cadOvSysMemStatus.setStatus(_A)
_CadProcessTrapInfo_ObjectIdentity=ObjectIdentity
cadProcessTrapInfo=_CadProcessTrapInfo_ObjectIdentity((1,3,6,1,4,1,4998,1,1,5,3,4))
class _CadProcessOverloadStatus_Type(OverloadStatus):defaultValue=1
_CadProcessOverloadStatus_Type.__name__=_E
_CadProcessOverloadStatus_Object=MibScalar
cadProcessOverloadStatus=_CadProcessOverloadStatus_Object((1,3,6,1,4,1,4998,1,1,5,3,4,1),_CadProcessOverloadStatus_Type())
cadProcessOverloadStatus.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:cadProcessOverloadStatus.setStatus(_A)
_CadProcessMibConformance_ObjectIdentity=ObjectIdentity
cadProcessMibConformance=_CadProcessMibConformance_ObjectIdentity((1,3,6,1,4,1,4998,1,1,5,3,5))
_CadProcessCompliances_ObjectIdentity=ObjectIdentity
cadProcessCompliances=_CadProcessCompliances_ObjectIdentity((1,3,6,1,4,1,4998,1,1,5,3,5,1))
_CadProcessGroups_ObjectIdentity=ObjectIdentity
cadProcessGroups=_CadProcessGroups_ObjectIdentity((1,3,6,1,4,1,4998,1,1,5,3,5,2))
cardOverloadNotification=NotificationType((1,3,6,1,4,1,4998,1,1,5,3,0,1))
cardOverloadNotification.setObjects(*((_D,_G),(_D,_H),(_D,_K),(_C,_J)))
if mibBuilder.loadTexts:cardOverloadNotification.setStatus(_A)
sysOverloadNotification=NotificationType((1,3,6,1,4,1,4998,1,1,5,3,0,2))
sysOverloadNotification.setObjects(*((_D,_G),(_D,_H),(_C,_J)))
if mibBuilder.loadTexts:sysOverloadNotification.setStatus(_A)
cadProcessCompliance=ModuleCompliance((1,3,6,1,4,1,4998,1,1,5,3,5,1,1))
cadProcessCompliance.setObjects(*((_C,_P),(_C,_Q),(_C,_R)))
if mibBuilder.loadTexts:cadProcessCompliance.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'cadProcessMib':cadProcessMib,'cadProcessTraps':cadProcessTraps,'cardOverloadNotification':cardOverloadNotification,'sysOverloadNotification':sysOverloadNotification,_P:cadProcessGroup,'cadCpu':cadCpu,'cadCpuEntry':cadCpuEntry,_M:cadCpuCardId,'cadCpuRecentTime':cadCpuRecentTime,'cadCpuTotalTime':cadCpuTotalTime,'cadIdleCpuRecentTime':cadIdleCpuRecentTime,'cadIdleCpuTotalTime':cadIdleCpuTotalTime,'cadSwitchRecentCount':cadSwitchRecentCount,'cadSwitchTotalCount':cadSwitchTotalCount,'cadIdleCpuRecentPercent':cadIdleCpuRecentPercent,_Q:cadMemoryGroup,'cadMemory':cadMemory,'cadMemoryEntry':cadMemoryEntry,_N:cadMeCardId,'cadMeHeapSize':cadMeHeapSize,'cadMeHeapRemaining':cadMeHeapRemaining,_R:cadOverloadGroup,'cadOverload':cadOverload,'cadOverloadEntry':cadOverloadEntry,_O:cadOvCardId,'cadOvCpuStatus':cadOvCpuStatus,'cadOvMemStatus':cadOvMemStatus,'cadOvSysCpuStatus':cadOvSysCpuStatus,'cadOvSysMemStatus':cadOvSysMemStatus,'cadProcessTrapInfo':cadProcessTrapInfo,_J:cadProcessOverloadStatus,'cadProcessMibConformance':cadProcessMibConformance,'cadProcessCompliances':cadProcessCompliances,'cadProcessCompliance':cadProcessCompliance,'cadProcessGroups':cadProcessGroups})