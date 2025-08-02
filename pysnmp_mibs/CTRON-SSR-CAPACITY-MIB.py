_o='capConfGroupV20'
_n='capConfGroupV10'
_m='capCPUMaxThreshold'
_l='capCPUMinThreshold'
_k='deprecated'
_j='capMemoryIndex'
_i='capMemoryType'
_h='capTaskIndex'
_g='capTaskModuleIndex'
_f='read-write'
_e='capCPUModuleIndex'
_d='capMemoryRemovable'
_c='capMemoryFailures'
_b='capMemoryBlockSize'
_a='capMemoryUsed'
_Z='capMemoryFree'
_Y='capMemorySize'
_X='capMemoryDescr'
_W='capTaskUsed'
_V='capTaskStatus'
_U='capTaskShed'
_T='capTaskName'
_S='capCPUNIATransmitted'
_R='capCPUNIAReceived'
_Q='capCPUL2Aged'
_P='capCPUL2Learned'
_O='capCPUL3Aged'
_N='capCPUL3Learned'
_M='capCPUCurrentUtilization'
_L='capChassisSFRedundancy'
_K='capChassisPSRedundancy'
_J='capChassisCPURedundancy'
_I='capChassisSlotsFree'
_H='capChassisSlotsUsed'
_G='capChassisSlotCount'
_F='OctetString'
_E='not-accessible'
_D='Integer32'
_C='read-only'
_B='current'
_A='CTRON-SSR-CAPACITY-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ssrMibs,=mibBuilder.importSymbols('CTRON-SSR-SMI-MIB','ssrMibs')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
capacityMIB=ModuleIdentity((1,3,6,1,4,1,52,2501,1,270))
if mibBuilder.loadTexts:capacityMIB.setRevisions(('2000-07-15 00:00','1998-11-05 00:00'))
class SSRMemoryType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('cpu',1),('intFlash',2),('pcmcia',3),('rmon',4),('l2Hardware',5),('l3Hardware',6)))
class SSRCapabilityType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('noSupport',1),('available',2),('enabled',3),('disabled',4)))
class SSRStatusType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*(('ready',0),('suspPure',1),('suspSleep',2),('suspMbox',3),('suspQue',4),('suspPipe',5),('suspSema4',6),('suspEvent',7),('suspPart',8),('suspMem',9),('suspDrvr',10),('finished',11),('terminated',12)))
_ChassisCap_ObjectIdentity=ObjectIdentity
chassisCap=_ChassisCap_ObjectIdentity((1,3,6,1,4,1,52,2501,1,270,1))
class _CapChassisSlotCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,32))
_CapChassisSlotCount_Type.__name__=_D
_CapChassisSlotCount_Object=MibScalar
capChassisSlotCount=_CapChassisSlotCount_Object((1,3,6,1,4,1,52,2501,1,270,1,1),_CapChassisSlotCount_Type())
capChassisSlotCount.setMaxAccess(_C)
if mibBuilder.loadTexts:capChassisSlotCount.setStatus(_B)
class _CapChassisSlotsUsed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32))
_CapChassisSlotsUsed_Type.__name__=_D
_CapChassisSlotsUsed_Object=MibScalar
capChassisSlotsUsed=_CapChassisSlotsUsed_Object((1,3,6,1,4,1,52,2501,1,270,1,2),_CapChassisSlotsUsed_Type())
capChassisSlotsUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:capChassisSlotsUsed.setStatus(_B)
class _CapChassisSlotsFree_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32))
_CapChassisSlotsFree_Type.__name__=_D
_CapChassisSlotsFree_Object=MibScalar
capChassisSlotsFree=_CapChassisSlotsFree_Object((1,3,6,1,4,1,52,2501,1,270,1,3),_CapChassisSlotsFree_Type())
capChassisSlotsFree.setMaxAccess(_C)
if mibBuilder.loadTexts:capChassisSlotsFree.setStatus(_B)
_CapChassisCPURedundancy_Type=SSRCapabilityType
_CapChassisCPURedundancy_Object=MibScalar
capChassisCPURedundancy=_CapChassisCPURedundancy_Object((1,3,6,1,4,1,52,2501,1,270,1,4),_CapChassisCPURedundancy_Type())
capChassisCPURedundancy.setMaxAccess(_C)
if mibBuilder.loadTexts:capChassisCPURedundancy.setStatus(_B)
_CapChassisPSRedundancy_Type=SSRCapabilityType
_CapChassisPSRedundancy_Object=MibScalar
capChassisPSRedundancy=_CapChassisPSRedundancy_Object((1,3,6,1,4,1,52,2501,1,270,1,5),_CapChassisPSRedundancy_Type())
capChassisPSRedundancy.setMaxAccess(_C)
if mibBuilder.loadTexts:capChassisPSRedundancy.setStatus(_B)
_CapChassisSFRedundancy_Type=SSRCapabilityType
_CapChassisSFRedundancy_Object=MibScalar
capChassisSFRedundancy=_CapChassisSFRedundancy_Object((1,3,6,1,4,1,52,2501,1,270,1,6),_CapChassisSFRedundancy_Type())
capChassisSFRedundancy.setMaxAccess(_C)
if mibBuilder.loadTexts:capChassisSFRedundancy.setStatus(_B)
_Cpu_ObjectIdentity=ObjectIdentity
cpu=_Cpu_ObjectIdentity((1,3,6,1,4,1,52,2501,1,270,2))
_CapCPUTable_Object=MibTable
capCPUTable=_CapCPUTable_Object((1,3,6,1,4,1,52,2501,1,270,2,1))
if mibBuilder.loadTexts:capCPUTable.setStatus(_B)
_CapCPUEntry_Object=MibTableRow
capCPUEntry=_CapCPUEntry_Object((1,3,6,1,4,1,52,2501,1,270,2,1,1))
capCPUEntry.setIndexNames((0,_A,_e))
if mibBuilder.loadTexts:capCPUEntry.setStatus(_B)
class _CapCPUModuleIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CapCPUModuleIndex_Type.__name__=_D
_CapCPUModuleIndex_Object=MibTableColumn
capCPUModuleIndex=_CapCPUModuleIndex_Object((1,3,6,1,4,1,52,2501,1,270,2,1,1,1),_CapCPUModuleIndex_Type())
capCPUModuleIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:capCPUModuleIndex.setStatus(_B)
class _CapCPUCurrentUtilization_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CapCPUCurrentUtilization_Type.__name__=_D
_CapCPUCurrentUtilization_Object=MibTableColumn
capCPUCurrentUtilization=_CapCPUCurrentUtilization_Object((1,3,6,1,4,1,52,2501,1,270,2,1,1,2),_CapCPUCurrentUtilization_Type())
capCPUCurrentUtilization.setMaxAccess(_C)
if mibBuilder.loadTexts:capCPUCurrentUtilization.setStatus(_B)
_CapCPUL3Learned_Type=Counter32
_CapCPUL3Learned_Object=MibTableColumn
capCPUL3Learned=_CapCPUL3Learned_Object((1,3,6,1,4,1,52,2501,1,270,2,1,1,3),_CapCPUL3Learned_Type())
capCPUL3Learned.setMaxAccess(_C)
if mibBuilder.loadTexts:capCPUL3Learned.setStatus(_B)
_CapCPUL3Aged_Type=Counter32
_CapCPUL3Aged_Object=MibTableColumn
capCPUL3Aged=_CapCPUL3Aged_Object((1,3,6,1,4,1,52,2501,1,270,2,1,1,4),_CapCPUL3Aged_Type())
capCPUL3Aged.setMaxAccess(_C)
if mibBuilder.loadTexts:capCPUL3Aged.setStatus(_B)
_CapCPUL2Learned_Type=Counter32
_CapCPUL2Learned_Object=MibTableColumn
capCPUL2Learned=_CapCPUL2Learned_Object((1,3,6,1,4,1,52,2501,1,270,2,1,1,5),_CapCPUL2Learned_Type())
capCPUL2Learned.setMaxAccess(_C)
if mibBuilder.loadTexts:capCPUL2Learned.setStatus(_B)
_CapCPUL2Aged_Type=Counter32
_CapCPUL2Aged_Object=MibTableColumn
capCPUL2Aged=_CapCPUL2Aged_Object((1,3,6,1,4,1,52,2501,1,270,2,1,1,6),_CapCPUL2Aged_Type())
capCPUL2Aged.setMaxAccess(_C)
if mibBuilder.loadTexts:capCPUL2Aged.setStatus(_B)
_CapCPUNIAReceived_Type=Counter32
_CapCPUNIAReceived_Object=MibTableColumn
capCPUNIAReceived=_CapCPUNIAReceived_Object((1,3,6,1,4,1,52,2501,1,270,2,1,1,7),_CapCPUNIAReceived_Type())
capCPUNIAReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:capCPUNIAReceived.setStatus(_B)
_CapCPUNIATransmitted_Type=Counter32
_CapCPUNIATransmitted_Object=MibTableColumn
capCPUNIATransmitted=_CapCPUNIATransmitted_Object((1,3,6,1,4,1,52,2501,1,270,2,1,1,8),_CapCPUNIATransmitted_Type())
capCPUNIATransmitted.setMaxAccess(_C)
if mibBuilder.loadTexts:capCPUNIATransmitted.setStatus(_B)
class _CapCPUMinThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,99))
_CapCPUMinThreshold_Type.__name__=_D
_CapCPUMinThreshold_Object=MibTableColumn
capCPUMinThreshold=_CapCPUMinThreshold_Object((1,3,6,1,4,1,52,2501,1,270,2,1,1,9),_CapCPUMinThreshold_Type())
capCPUMinThreshold.setMaxAccess(_f)
if mibBuilder.loadTexts:capCPUMinThreshold.setStatus(_B)
class _CapCPUMaxThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,99))
_CapCPUMaxThreshold_Type.__name__=_D
_CapCPUMaxThreshold_Object=MibTableColumn
capCPUMaxThreshold=_CapCPUMaxThreshold_Object((1,3,6,1,4,1,52,2501,1,270,2,1,1,10),_CapCPUMaxThreshold_Type())
capCPUMaxThreshold.setMaxAccess(_f)
if mibBuilder.loadTexts:capCPUMaxThreshold.setStatus(_B)
_Tasks_ObjectIdentity=ObjectIdentity
tasks=_Tasks_ObjectIdentity((1,3,6,1,4,1,52,2501,1,270,3))
_CapTaskTable_Object=MibTable
capTaskTable=_CapTaskTable_Object((1,3,6,1,4,1,52,2501,1,270,3,1))
if mibBuilder.loadTexts:capTaskTable.setStatus(_B)
_CapTaskEntry_Object=MibTableRow
capTaskEntry=_CapTaskEntry_Object((1,3,6,1,4,1,52,2501,1,270,3,1,1))
capTaskEntry.setIndexNames((0,_A,_g),(0,_A,_h))
if mibBuilder.loadTexts:capTaskEntry.setStatus(_B)
class _CapTaskModuleIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CapTaskModuleIndex_Type.__name__=_D
_CapTaskModuleIndex_Object=MibTableColumn
capTaskModuleIndex=_CapTaskModuleIndex_Object((1,3,6,1,4,1,52,2501,1,270,3,1,1,1),_CapTaskModuleIndex_Type())
capTaskModuleIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:capTaskModuleIndex.setStatus(_B)
class _CapTaskIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CapTaskIndex_Type.__name__=_D
_CapTaskIndex_Object=MibTableColumn
capTaskIndex=_CapTaskIndex_Object((1,3,6,1,4,1,52,2501,1,270,3,1,1,2),_CapTaskIndex_Type())
capTaskIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:capTaskIndex.setStatus(_B)
class _CapTaskName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_CapTaskName_Type.__name__=_F
_CapTaskName_Object=MibTableColumn
capTaskName=_CapTaskName_Object((1,3,6,1,4,1,52,2501,1,270,3,1,1,3),_CapTaskName_Type())
capTaskName.setMaxAccess(_C)
if mibBuilder.loadTexts:capTaskName.setStatus(_B)
_CapTaskShed_Type=Counter32
_CapTaskShed_Object=MibTableColumn
capTaskShed=_CapTaskShed_Object((1,3,6,1,4,1,52,2501,1,270,3,1,1,4),_CapTaskShed_Type())
capTaskShed.setMaxAccess(_C)
if mibBuilder.loadTexts:capTaskShed.setStatus(_B)
_CapTaskStatus_Type=SSRStatusType
_CapTaskStatus_Object=MibTableColumn
capTaskStatus=_CapTaskStatus_Object((1,3,6,1,4,1,52,2501,1,270,3,1,1,5),_CapTaskStatus_Type())
capTaskStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:capTaskStatus.setStatus(_B)
class _CapTaskUsed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CapTaskUsed_Type.__name__=_D
_CapTaskUsed_Object=MibTableColumn
capTaskUsed=_CapTaskUsed_Object((1,3,6,1,4,1,52,2501,1,270,3,1,1,6),_CapTaskUsed_Type())
capTaskUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:capTaskUsed.setStatus(_B)
_Memory_ObjectIdentity=ObjectIdentity
memory=_Memory_ObjectIdentity((1,3,6,1,4,1,52,2501,1,270,4))
_CapMemoryTable_Object=MibTable
capMemoryTable=_CapMemoryTable_Object((1,3,6,1,4,1,52,2501,1,270,4,1))
if mibBuilder.loadTexts:capMemoryTable.setStatus(_B)
_CapMemoryEntry_Object=MibTableRow
capMemoryEntry=_CapMemoryEntry_Object((1,3,6,1,4,1,52,2501,1,270,4,1,1))
capMemoryEntry.setIndexNames((0,_A,_i),(0,_A,_j))
if mibBuilder.loadTexts:capMemoryEntry.setStatus(_B)
_CapMemoryType_Type=SSRMemoryType
_CapMemoryType_Object=MibTableColumn
capMemoryType=_CapMemoryType_Object((1,3,6,1,4,1,52,2501,1,270,4,1,1,1),_CapMemoryType_Type())
capMemoryType.setMaxAccess(_E)
if mibBuilder.loadTexts:capMemoryType.setStatus(_B)
class _CapMemoryIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CapMemoryIndex_Type.__name__=_D
_CapMemoryIndex_Object=MibTableColumn
capMemoryIndex=_CapMemoryIndex_Object((1,3,6,1,4,1,52,2501,1,270,4,1,1,2),_CapMemoryIndex_Type())
capMemoryIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:capMemoryIndex.setStatus(_B)
class _CapMemoryDescr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_CapMemoryDescr_Type.__name__=_F
_CapMemoryDescr_Object=MibTableColumn
capMemoryDescr=_CapMemoryDescr_Object((1,3,6,1,4,1,52,2501,1,270,4,1,1,3),_CapMemoryDescr_Type())
capMemoryDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:capMemoryDescr.setStatus(_B)
class _CapMemorySize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CapMemorySize_Type.__name__=_D
_CapMemorySize_Object=MibTableColumn
capMemorySize=_CapMemorySize_Object((1,3,6,1,4,1,52,2501,1,270,4,1,1,4),_CapMemorySize_Type())
capMemorySize.setMaxAccess(_C)
if mibBuilder.loadTexts:capMemorySize.setStatus(_B)
class _CapMemoryFree_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CapMemoryFree_Type.__name__=_D
_CapMemoryFree_Object=MibTableColumn
capMemoryFree=_CapMemoryFree_Object((1,3,6,1,4,1,52,2501,1,270,4,1,1,5),_CapMemoryFree_Type())
capMemoryFree.setMaxAccess(_C)
if mibBuilder.loadTexts:capMemoryFree.setStatus(_B)
class _CapMemoryUsed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CapMemoryUsed_Type.__name__=_D
_CapMemoryUsed_Object=MibTableColumn
capMemoryUsed=_CapMemoryUsed_Object((1,3,6,1,4,1,52,2501,1,270,4,1,1,6),_CapMemoryUsed_Type())
capMemoryUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:capMemoryUsed.setStatus(_B)
class _CapMemoryBlockSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CapMemoryBlockSize_Type.__name__=_D
_CapMemoryBlockSize_Object=MibTableColumn
capMemoryBlockSize=_CapMemoryBlockSize_Object((1,3,6,1,4,1,52,2501,1,270,4,1,1,7),_CapMemoryBlockSize_Type())
capMemoryBlockSize.setMaxAccess(_C)
if mibBuilder.loadTexts:capMemoryBlockSize.setStatus(_B)
_CapMemoryFailures_Type=Counter32
_CapMemoryFailures_Object=MibTableColumn
capMemoryFailures=_CapMemoryFailures_Object((1,3,6,1,4,1,52,2501,1,270,4,1,1,8),_CapMemoryFailures_Type())
capMemoryFailures.setMaxAccess(_C)
if mibBuilder.loadTexts:capMemoryFailures.setStatus(_B)
_CapMemoryRemovable_Type=TruthValue
_CapMemoryRemovable_Object=MibTableColumn
capMemoryRemovable=_CapMemoryRemovable_Object((1,3,6,1,4,1,52,2501,1,270,4,1,1,9),_CapMemoryRemovable_Type())
capMemoryRemovable.setMaxAccess(_C)
if mibBuilder.loadTexts:capMemoryRemovable.setStatus(_B)
_CapConformance_ObjectIdentity=ObjectIdentity
capConformance=_CapConformance_ObjectIdentity((1,3,6,1,4,1,52,2501,1,270,6))
_CapCompliances_ObjectIdentity=ObjectIdentity
capCompliances=_CapCompliances_ObjectIdentity((1,3,6,1,4,1,52,2501,1,270,6,1))
_CapGroups_ObjectIdentity=ObjectIdentity
capGroups=_CapGroups_ObjectIdentity((1,3,6,1,4,1,52,2501,1,270,6,2))
capConfGroupV10=ObjectGroup((1,3,6,1,4,1,52,2501,1,270,6,2,1))
capConfGroupV10.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d)))
if mibBuilder.loadTexts:capConfGroupV10.setStatus(_k)
capConfGroupV20=ObjectGroup((1,3,6,1,4,1,52,2501,1,270,6,2,2))
capConfGroupV20.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_l),(_A,_m),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d)))
if mibBuilder.loadTexts:capConfGroupV20.setStatus(_B)
capComplianceV10=ModuleCompliance((1,3,6,1,4,1,52,2501,1,270,6,2,1,1))
capComplianceV10.setObjects((_A,_n))
if mibBuilder.loadTexts:capComplianceV10.setStatus(_k)
capComplianceV20=ModuleCompliance((1,3,6,1,4,1,52,2501,1,270,6,2,2,1))
capComplianceV20.setObjects((_A,_o))
if mibBuilder.loadTexts:capComplianceV20.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'SSRMemoryType':SSRMemoryType,'SSRCapabilityType':SSRCapabilityType,'SSRStatusType':SSRStatusType,'capacityMIB':capacityMIB,'chassisCap':chassisCap,_G:capChassisSlotCount,_H:capChassisSlotsUsed,_I:capChassisSlotsFree,_J:capChassisCPURedundancy,_K:capChassisPSRedundancy,_L:capChassisSFRedundancy,'cpu':cpu,'capCPUTable':capCPUTable,'capCPUEntry':capCPUEntry,_e:capCPUModuleIndex,_M:capCPUCurrentUtilization,_N:capCPUL3Learned,_O:capCPUL3Aged,_P:capCPUL2Learned,_Q:capCPUL2Aged,_R:capCPUNIAReceived,_S:capCPUNIATransmitted,_l:capCPUMinThreshold,_m:capCPUMaxThreshold,'tasks':tasks,'capTaskTable':capTaskTable,'capTaskEntry':capTaskEntry,_g:capTaskModuleIndex,_h:capTaskIndex,_T:capTaskName,_U:capTaskShed,_V:capTaskStatus,_W:capTaskUsed,'memory':memory,'capMemoryTable':capMemoryTable,'capMemoryEntry':capMemoryEntry,_i:capMemoryType,_j:capMemoryIndex,_X:capMemoryDescr,_Y:capMemorySize,_Z:capMemoryFree,_a:capMemoryUsed,_b:capMemoryBlockSize,_c:capMemoryFailures,_d:capMemoryRemovable,'capConformance':capConformance,'capCompliances':capCompliances,'capGroups':capGroups,_n:capConfGroupV10,'capComplianceV10':capComplianceV10,_o:capConfGroupV20,'capComplianceV20':capComplianceV20})