_l='sysinfoBoardProcessGroup'
_k='sysinfoBoardMemoryGroup'
_j='sysinfoBoardLoadGroup'
_i='sysinfoBoardStartupGroup'
_h='sysinfoBoardProcessReferenceTime'
_g='sysinfoBoardProcessVmRSSDiff'
_f='sysinfoBoardProcessVmSizeDiff'
_e='sysinfoBoardProcessVmRSSReference'
_d='sysinfoBoardProcessVmSizeReference'
_c='sysinfoBoardProcessSetReference'
_b='sysinfoBoardProcessVmRSS'
_a='sysinfoBoardProcessVmSize'
_Z='sysinfoBoardProcessPid'
_Y='sysinfoBoardProcessProcessName'
_X='sysinfoBoardProcessName'
_W='sysinfoBoardMemoryUsageMemPercent'
_V='sysinfoBoardMemoryAvailableMem'
_U='sysinfoBoardMemoryFreeMem'
_T='sysinfoBoardMemoryTotalMem'
_S='sysinfoBoardMemoryName'
_R='sysinfoBoardLoadLoad15Min'
_Q='sysinfoBoardLoadLoad5Min'
_P='sysinfoBoardLoadLoad1Min'
_O='sysinfoBoardLoadName'
_N='sysinfoBoardStartupRebootReason'
_M='sysinfoBoardStartupUptimeSeconds'
_L='sysinfoBoardStartupUptime'
_K='sysinfoBoardStartupName'
_J='Integer32'
_I='sysinfoBoardProcessIndex'
_H='sysinfoBoardMemoryIndex'
_G='sysinfoBoardLoadIndex'
_F='sysinfoBoardStartupIndex'
_E='DisplayString'
_D='Unsigned32'
_C='read-only'
_B='LUM-SYSINFO-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
lumModules,lumSysinfoMIB=mibBuilder.importSymbols('LUM-REG','lumModules','lumSysinfoMIB')
Integer32WithNA,MgmtNameString,Unsigned32WithNA=mibBuilder.importSymbols('LUM-TC','Integer32WithNA','MgmtNameString','Unsigned32WithNA')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_J,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','TextualConvention')
lumSysinfoMIBModule=ModuleIdentity((1,3,6,1,4,1,8708,1,1,71))
if mibBuilder.loadTexts:lumSysinfoMIBModule.setRevisions(('2018-06-29 00:00',))
_LumSysinfoConfs_ObjectIdentity=ObjectIdentity
lumSysinfoConfs=_LumSysinfoConfs_ObjectIdentity((1,3,6,1,4,1,8708,2,71,1))
_LumSysinfoGroups_ObjectIdentity=ObjectIdentity
lumSysinfoGroups=_LumSysinfoGroups_ObjectIdentity((1,3,6,1,4,1,8708,2,71,1,1))
_LumSysinfoCompl_ObjectIdentity=ObjectIdentity
lumSysinfoCompl=_LumSysinfoCompl_ObjectIdentity((1,3,6,1,4,1,8708,2,71,1,2))
_LumSysinfoMIBObjects_ObjectIdentity=ObjectIdentity
lumSysinfoMIBObjects=_LumSysinfoMIBObjects_ObjectIdentity((1,3,6,1,4,1,8708,2,71,2))
_SysinfoBoardStartupList_ObjectIdentity=ObjectIdentity
sysinfoBoardStartupList=_SysinfoBoardStartupList_ObjectIdentity((1,3,6,1,4,1,8708,2,71,2,1))
_SysinfoBoardStartupTable_Object=MibTable
sysinfoBoardStartupTable=_SysinfoBoardStartupTable_Object((1,3,6,1,4,1,8708,2,71,2,1,1))
if mibBuilder.loadTexts:sysinfoBoardStartupTable.setStatus(_A)
_SysinfoBoardStartupEntry_Object=MibTableRow
sysinfoBoardStartupEntry=_SysinfoBoardStartupEntry_Object((1,3,6,1,4,1,8708,2,71,2,1,1,1))
sysinfoBoardStartupEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:sysinfoBoardStartupEntry.setStatus(_A)
class _SysinfoBoardStartupIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_SysinfoBoardStartupIndex_Type.__name__=_D
_SysinfoBoardStartupIndex_Object=MibTableColumn
sysinfoBoardStartupIndex=_SysinfoBoardStartupIndex_Object((1,3,6,1,4,1,8708,2,71,2,1,1,1,1),_SysinfoBoardStartupIndex_Type())
sysinfoBoardStartupIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:sysinfoBoardStartupIndex.setStatus(_A)
_SysinfoBoardStartupName_Type=MgmtNameString
_SysinfoBoardStartupName_Object=MibTableColumn
sysinfoBoardStartupName=_SysinfoBoardStartupName_Object((1,3,6,1,4,1,8708,2,71,2,1,1,1,2),_SysinfoBoardStartupName_Type())
sysinfoBoardStartupName.setMaxAccess(_C)
if mibBuilder.loadTexts:sysinfoBoardStartupName.setStatus(_A)
_SysinfoBoardStartupUptime_Type=DisplayString
_SysinfoBoardStartupUptime_Object=MibTableColumn
sysinfoBoardStartupUptime=_SysinfoBoardStartupUptime_Object((1,3,6,1,4,1,8708,2,71,2,1,1,1,3),_SysinfoBoardStartupUptime_Type())
sysinfoBoardStartupUptime.setMaxAccess(_C)
if mibBuilder.loadTexts:sysinfoBoardStartupUptime.setStatus(_A)
_SysinfoBoardStartupUptimeSeconds_Type=Unsigned32
_SysinfoBoardStartupUptimeSeconds_Object=MibTableColumn
sysinfoBoardStartupUptimeSeconds=_SysinfoBoardStartupUptimeSeconds_Object((1,3,6,1,4,1,8708,2,71,2,1,1,1,4),_SysinfoBoardStartupUptimeSeconds_Type())
sysinfoBoardStartupUptimeSeconds.setMaxAccess(_C)
if mibBuilder.loadTexts:sysinfoBoardStartupUptimeSeconds.setStatus(_A)
class _SysinfoBoardStartupRebootReason_Type(DisplayString):defaultValue=OctetString(' ')
_SysinfoBoardStartupRebootReason_Type.__name__=_E
_SysinfoBoardStartupRebootReason_Object=MibTableColumn
sysinfoBoardStartupRebootReason=_SysinfoBoardStartupRebootReason_Object((1,3,6,1,4,1,8708,2,71,2,1,1,1,5),_SysinfoBoardStartupRebootReason_Type())
sysinfoBoardStartupRebootReason.setMaxAccess(_C)
if mibBuilder.loadTexts:sysinfoBoardStartupRebootReason.setStatus(_A)
_SysinfoBoardLoadList_ObjectIdentity=ObjectIdentity
sysinfoBoardLoadList=_SysinfoBoardLoadList_ObjectIdentity((1,3,6,1,4,1,8708,2,71,2,2))
_SysinfoBoardLoadTable_Object=MibTable
sysinfoBoardLoadTable=_SysinfoBoardLoadTable_Object((1,3,6,1,4,1,8708,2,71,2,2,1))
if mibBuilder.loadTexts:sysinfoBoardLoadTable.setStatus(_A)
_SysinfoBoardLoadEntry_Object=MibTableRow
sysinfoBoardLoadEntry=_SysinfoBoardLoadEntry_Object((1,3,6,1,4,1,8708,2,71,2,2,1,1))
sysinfoBoardLoadEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:sysinfoBoardLoadEntry.setStatus(_A)
class _SysinfoBoardLoadIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_SysinfoBoardLoadIndex_Type.__name__=_D
_SysinfoBoardLoadIndex_Object=MibTableColumn
sysinfoBoardLoadIndex=_SysinfoBoardLoadIndex_Object((1,3,6,1,4,1,8708,2,71,2,2,1,1,1),_SysinfoBoardLoadIndex_Type())
sysinfoBoardLoadIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:sysinfoBoardLoadIndex.setStatus(_A)
_SysinfoBoardLoadName_Type=MgmtNameString
_SysinfoBoardLoadName_Object=MibTableColumn
sysinfoBoardLoadName=_SysinfoBoardLoadName_Object((1,3,6,1,4,1,8708,2,71,2,2,1,1,2),_SysinfoBoardLoadName_Type())
sysinfoBoardLoadName.setMaxAccess(_C)
if mibBuilder.loadTexts:sysinfoBoardLoadName.setStatus(_A)
_SysinfoBoardLoadLoad1Min_Type=Unsigned32
_SysinfoBoardLoadLoad1Min_Object=MibTableColumn
sysinfoBoardLoadLoad1Min=_SysinfoBoardLoadLoad1Min_Object((1,3,6,1,4,1,8708,2,71,2,2,1,1,3),_SysinfoBoardLoadLoad1Min_Type())
sysinfoBoardLoadLoad1Min.setMaxAccess(_C)
if mibBuilder.loadTexts:sysinfoBoardLoadLoad1Min.setStatus(_A)
_SysinfoBoardLoadLoad5Min_Type=Unsigned32
_SysinfoBoardLoadLoad5Min_Object=MibTableColumn
sysinfoBoardLoadLoad5Min=_SysinfoBoardLoadLoad5Min_Object((1,3,6,1,4,1,8708,2,71,2,2,1,1,4),_SysinfoBoardLoadLoad5Min_Type())
sysinfoBoardLoadLoad5Min.setMaxAccess(_C)
if mibBuilder.loadTexts:sysinfoBoardLoadLoad5Min.setStatus(_A)
_SysinfoBoardLoadLoad15Min_Type=Unsigned32
_SysinfoBoardLoadLoad15Min_Object=MibTableColumn
sysinfoBoardLoadLoad15Min=_SysinfoBoardLoadLoad15Min_Object((1,3,6,1,4,1,8708,2,71,2,2,1,1,5),_SysinfoBoardLoadLoad15Min_Type())
sysinfoBoardLoadLoad15Min.setMaxAccess(_C)
if mibBuilder.loadTexts:sysinfoBoardLoadLoad15Min.setStatus(_A)
_SysinfoBoardMemoryList_ObjectIdentity=ObjectIdentity
sysinfoBoardMemoryList=_SysinfoBoardMemoryList_ObjectIdentity((1,3,6,1,4,1,8708,2,71,2,3))
_SysinfoBoardMemoryTable_Object=MibTable
sysinfoBoardMemoryTable=_SysinfoBoardMemoryTable_Object((1,3,6,1,4,1,8708,2,71,2,3,1))
if mibBuilder.loadTexts:sysinfoBoardMemoryTable.setStatus(_A)
_SysinfoBoardMemoryEntry_Object=MibTableRow
sysinfoBoardMemoryEntry=_SysinfoBoardMemoryEntry_Object((1,3,6,1,4,1,8708,2,71,2,3,1,1))
sysinfoBoardMemoryEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:sysinfoBoardMemoryEntry.setStatus(_A)
class _SysinfoBoardMemoryIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_SysinfoBoardMemoryIndex_Type.__name__=_D
_SysinfoBoardMemoryIndex_Object=MibTableColumn
sysinfoBoardMemoryIndex=_SysinfoBoardMemoryIndex_Object((1,3,6,1,4,1,8708,2,71,2,3,1,1,1),_SysinfoBoardMemoryIndex_Type())
sysinfoBoardMemoryIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:sysinfoBoardMemoryIndex.setStatus(_A)
_SysinfoBoardMemoryName_Type=MgmtNameString
_SysinfoBoardMemoryName_Object=MibTableColumn
sysinfoBoardMemoryName=_SysinfoBoardMemoryName_Object((1,3,6,1,4,1,8708,2,71,2,3,1,1,2),_SysinfoBoardMemoryName_Type())
sysinfoBoardMemoryName.setMaxAccess(_C)
if mibBuilder.loadTexts:sysinfoBoardMemoryName.setStatus(_A)
_SysinfoBoardMemoryTotalMem_Type=Unsigned32
_SysinfoBoardMemoryTotalMem_Object=MibTableColumn
sysinfoBoardMemoryTotalMem=_SysinfoBoardMemoryTotalMem_Object((1,3,6,1,4,1,8708,2,71,2,3,1,1,3),_SysinfoBoardMemoryTotalMem_Type())
sysinfoBoardMemoryTotalMem.setMaxAccess(_C)
if mibBuilder.loadTexts:sysinfoBoardMemoryTotalMem.setStatus(_A)
_SysinfoBoardMemoryFreeMem_Type=Unsigned32
_SysinfoBoardMemoryFreeMem_Object=MibTableColumn
sysinfoBoardMemoryFreeMem=_SysinfoBoardMemoryFreeMem_Object((1,3,6,1,4,1,8708,2,71,2,3,1,1,4),_SysinfoBoardMemoryFreeMem_Type())
sysinfoBoardMemoryFreeMem.setMaxAccess(_C)
if mibBuilder.loadTexts:sysinfoBoardMemoryFreeMem.setStatus(_A)
_SysinfoBoardMemoryAvailableMem_Type=Unsigned32
_SysinfoBoardMemoryAvailableMem_Object=MibTableColumn
sysinfoBoardMemoryAvailableMem=_SysinfoBoardMemoryAvailableMem_Object((1,3,6,1,4,1,8708,2,71,2,3,1,1,5),_SysinfoBoardMemoryAvailableMem_Type())
sysinfoBoardMemoryAvailableMem.setMaxAccess(_C)
if mibBuilder.loadTexts:sysinfoBoardMemoryAvailableMem.setStatus(_A)
_SysinfoBoardMemoryUsageMemPercent_Type=Unsigned32
_SysinfoBoardMemoryUsageMemPercent_Object=MibTableColumn
sysinfoBoardMemoryUsageMemPercent=_SysinfoBoardMemoryUsageMemPercent_Object((1,3,6,1,4,1,8708,2,71,2,3,1,1,6),_SysinfoBoardMemoryUsageMemPercent_Type())
sysinfoBoardMemoryUsageMemPercent.setMaxAccess(_C)
if mibBuilder.loadTexts:sysinfoBoardMemoryUsageMemPercent.setStatus(_A)
_SysinfoBoardProcessList_ObjectIdentity=ObjectIdentity
sysinfoBoardProcessList=_SysinfoBoardProcessList_ObjectIdentity((1,3,6,1,4,1,8708,2,71,2,4))
_SysinfoBoardProcessTable_Object=MibTable
sysinfoBoardProcessTable=_SysinfoBoardProcessTable_Object((1,3,6,1,4,1,8708,2,71,2,4,1))
if mibBuilder.loadTexts:sysinfoBoardProcessTable.setStatus(_A)
_SysinfoBoardProcessEntry_Object=MibTableRow
sysinfoBoardProcessEntry=_SysinfoBoardProcessEntry_Object((1,3,6,1,4,1,8708,2,71,2,4,1,1))
sysinfoBoardProcessEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:sysinfoBoardProcessEntry.setStatus(_A)
class _SysinfoBoardProcessIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_SysinfoBoardProcessIndex_Type.__name__=_D
_SysinfoBoardProcessIndex_Object=MibTableColumn
sysinfoBoardProcessIndex=_SysinfoBoardProcessIndex_Object((1,3,6,1,4,1,8708,2,71,2,4,1,1,1),_SysinfoBoardProcessIndex_Type())
sysinfoBoardProcessIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:sysinfoBoardProcessIndex.setStatus(_A)
_SysinfoBoardProcessName_Type=MgmtNameString
_SysinfoBoardProcessName_Object=MibTableColumn
sysinfoBoardProcessName=_SysinfoBoardProcessName_Object((1,3,6,1,4,1,8708,2,71,2,4,1,1,2),_SysinfoBoardProcessName_Type())
sysinfoBoardProcessName.setMaxAccess(_C)
if mibBuilder.loadTexts:sysinfoBoardProcessName.setStatus(_A)
_SysinfoBoardProcessProcessName_Type=MgmtNameString
_SysinfoBoardProcessProcessName_Object=MibTableColumn
sysinfoBoardProcessProcessName=_SysinfoBoardProcessProcessName_Object((1,3,6,1,4,1,8708,2,71,2,4,1,1,3),_SysinfoBoardProcessProcessName_Type())
sysinfoBoardProcessProcessName.setMaxAccess(_C)
if mibBuilder.loadTexts:sysinfoBoardProcessProcessName.setStatus(_A)
_SysinfoBoardProcessPid_Type=Integer32
_SysinfoBoardProcessPid_Object=MibTableColumn
sysinfoBoardProcessPid=_SysinfoBoardProcessPid_Object((1,3,6,1,4,1,8708,2,71,2,4,1,1,4),_SysinfoBoardProcessPid_Type())
sysinfoBoardProcessPid.setMaxAccess(_C)
if mibBuilder.loadTexts:sysinfoBoardProcessPid.setStatus(_A)
_SysinfoBoardProcessVmSize_Type=Unsigned32
_SysinfoBoardProcessVmSize_Object=MibTableColumn
sysinfoBoardProcessVmSize=_SysinfoBoardProcessVmSize_Object((1,3,6,1,4,1,8708,2,71,2,4,1,1,5),_SysinfoBoardProcessVmSize_Type())
sysinfoBoardProcessVmSize.setMaxAccess(_C)
if mibBuilder.loadTexts:sysinfoBoardProcessVmSize.setStatus(_A)
_SysinfoBoardProcessVmRSS_Type=Unsigned32
_SysinfoBoardProcessVmRSS_Object=MibTableColumn
sysinfoBoardProcessVmRSS=_SysinfoBoardProcessVmRSS_Object((1,3,6,1,4,1,8708,2,71,2,4,1,1,6),_SysinfoBoardProcessVmRSS_Type())
sysinfoBoardProcessVmRSS.setMaxAccess(_C)
if mibBuilder.loadTexts:sysinfoBoardProcessVmRSS.setStatus(_A)
class _SysinfoBoardProcessSetReference_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noAction',1),('setReference',2)))
_SysinfoBoardProcessSetReference_Type.__name__=_J
_SysinfoBoardProcessSetReference_Object=MibTableColumn
sysinfoBoardProcessSetReference=_SysinfoBoardProcessSetReference_Object((1,3,6,1,4,1,8708,2,71,2,4,1,1,7),_SysinfoBoardProcessSetReference_Type())
sysinfoBoardProcessSetReference.setMaxAccess('read-write')
if mibBuilder.loadTexts:sysinfoBoardProcessSetReference.setStatus(_A)
_SysinfoBoardProcessVmSizeReference_Type=Unsigned32WithNA
_SysinfoBoardProcessVmSizeReference_Object=MibTableColumn
sysinfoBoardProcessVmSizeReference=_SysinfoBoardProcessVmSizeReference_Object((1,3,6,1,4,1,8708,2,71,2,4,1,1,8),_SysinfoBoardProcessVmSizeReference_Type())
sysinfoBoardProcessVmSizeReference.setMaxAccess(_C)
if mibBuilder.loadTexts:sysinfoBoardProcessVmSizeReference.setStatus(_A)
_SysinfoBoardProcessVmRSSReference_Type=Unsigned32WithNA
_SysinfoBoardProcessVmRSSReference_Object=MibTableColumn
sysinfoBoardProcessVmRSSReference=_SysinfoBoardProcessVmRSSReference_Object((1,3,6,1,4,1,8708,2,71,2,4,1,1,9),_SysinfoBoardProcessVmRSSReference_Type())
sysinfoBoardProcessVmRSSReference.setMaxAccess(_C)
if mibBuilder.loadTexts:sysinfoBoardProcessVmRSSReference.setStatus(_A)
_SysinfoBoardProcessVmSizeDiff_Type=Integer32WithNA
_SysinfoBoardProcessVmSizeDiff_Object=MibTableColumn
sysinfoBoardProcessVmSizeDiff=_SysinfoBoardProcessVmSizeDiff_Object((1,3,6,1,4,1,8708,2,71,2,4,1,1,10),_SysinfoBoardProcessVmSizeDiff_Type())
sysinfoBoardProcessVmSizeDiff.setMaxAccess(_C)
if mibBuilder.loadTexts:sysinfoBoardProcessVmSizeDiff.setStatus(_A)
_SysinfoBoardProcessVmRSSDiff_Type=Integer32WithNA
_SysinfoBoardProcessVmRSSDiff_Object=MibTableColumn
sysinfoBoardProcessVmRSSDiff=_SysinfoBoardProcessVmRSSDiff_Object((1,3,6,1,4,1,8708,2,71,2,4,1,1,11),_SysinfoBoardProcessVmRSSDiff_Type())
sysinfoBoardProcessVmRSSDiff.setMaxAccess(_C)
if mibBuilder.loadTexts:sysinfoBoardProcessVmRSSDiff.setStatus(_A)
class _SysinfoBoardProcessReferenceTime_Type(DisplayString):defaultValue=OctetString('Not set')
_SysinfoBoardProcessReferenceTime_Type.__name__=_E
_SysinfoBoardProcessReferenceTime_Object=MibTableColumn
sysinfoBoardProcessReferenceTime=_SysinfoBoardProcessReferenceTime_Object((1,3,6,1,4,1,8708,2,71,2,4,1,1,12),_SysinfoBoardProcessReferenceTime_Type())
sysinfoBoardProcessReferenceTime.setMaxAccess(_C)
if mibBuilder.loadTexts:sysinfoBoardProcessReferenceTime.setStatus(_A)
sysinfoBoardStartupGroup=ObjectGroup((1,3,6,1,4,1,8708,2,71,1,1,1))
sysinfoBoardStartupGroup.setObjects(*((_B,_F),(_B,_K),(_B,_L),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:sysinfoBoardStartupGroup.setStatus(_A)
sysinfoBoardLoadGroup=ObjectGroup((1,3,6,1,4,1,8708,2,71,1,1,2))
sysinfoBoardLoadGroup.setObjects(*((_B,_G),(_B,_O),(_B,_P),(_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:sysinfoBoardLoadGroup.setStatus(_A)
sysinfoBoardMemoryGroup=ObjectGroup((1,3,6,1,4,1,8708,2,71,1,1,3))
sysinfoBoardMemoryGroup.setObjects(*((_B,_H),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W)))
if mibBuilder.loadTexts:sysinfoBoardMemoryGroup.setStatus(_A)
sysinfoBoardProcessGroup=ObjectGroup((1,3,6,1,4,1,8708,2,71,1,1,4))
sysinfoBoardProcessGroup.setObjects(*((_B,_I),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h)))
if mibBuilder.loadTexts:sysinfoBoardProcessGroup.setStatus(_A)
lumSysinfoBasicComplV1=ModuleCompliance((1,3,6,1,4,1,8708,2,71,1,2,1))
lumSysinfoBasicComplV1.setObjects(*((_B,_i),(_B,_j),(_B,_k),(_B,_l)))
if mibBuilder.loadTexts:lumSysinfoBasicComplV1.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'lumSysinfoMIBModule':lumSysinfoMIBModule,'lumSysinfoConfs':lumSysinfoConfs,'lumSysinfoGroups':lumSysinfoGroups,_i:sysinfoBoardStartupGroup,_j:sysinfoBoardLoadGroup,_k:sysinfoBoardMemoryGroup,_l:sysinfoBoardProcessGroup,'lumSysinfoCompl':lumSysinfoCompl,'lumSysinfoBasicComplV1':lumSysinfoBasicComplV1,'lumSysinfoMIBObjects':lumSysinfoMIBObjects,'sysinfoBoardStartupList':sysinfoBoardStartupList,'sysinfoBoardStartupTable':sysinfoBoardStartupTable,'sysinfoBoardStartupEntry':sysinfoBoardStartupEntry,_F:sysinfoBoardStartupIndex,_K:sysinfoBoardStartupName,_L:sysinfoBoardStartupUptime,_M:sysinfoBoardStartupUptimeSeconds,_N:sysinfoBoardStartupRebootReason,'sysinfoBoardLoadList':sysinfoBoardLoadList,'sysinfoBoardLoadTable':sysinfoBoardLoadTable,'sysinfoBoardLoadEntry':sysinfoBoardLoadEntry,_G:sysinfoBoardLoadIndex,_O:sysinfoBoardLoadName,_P:sysinfoBoardLoadLoad1Min,_Q:sysinfoBoardLoadLoad5Min,_R:sysinfoBoardLoadLoad15Min,'sysinfoBoardMemoryList':sysinfoBoardMemoryList,'sysinfoBoardMemoryTable':sysinfoBoardMemoryTable,'sysinfoBoardMemoryEntry':sysinfoBoardMemoryEntry,_H:sysinfoBoardMemoryIndex,_S:sysinfoBoardMemoryName,_T:sysinfoBoardMemoryTotalMem,_U:sysinfoBoardMemoryFreeMem,_V:sysinfoBoardMemoryAvailableMem,_W:sysinfoBoardMemoryUsageMemPercent,'sysinfoBoardProcessList':sysinfoBoardProcessList,'sysinfoBoardProcessTable':sysinfoBoardProcessTable,'sysinfoBoardProcessEntry':sysinfoBoardProcessEntry,_I:sysinfoBoardProcessIndex,_X:sysinfoBoardProcessName,_Y:sysinfoBoardProcessProcessName,_Z:sysinfoBoardProcessPid,_a:sysinfoBoardProcessVmSize,_b:sysinfoBoardProcessVmRSS,_c:sysinfoBoardProcessSetReference,_d:sysinfoBoardProcessVmSizeReference,_e:sysinfoBoardProcessVmRSSReference,_f:sysinfoBoardProcessVmSizeDiff,_g:sysinfoBoardProcessVmRSSDiff,_h:sysinfoBoardProcessReferenceTime})