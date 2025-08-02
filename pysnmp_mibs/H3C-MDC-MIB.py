_Q='h3cMDCAllocateGroupIndex'
_P='not-accessible'
_O='h3cMDCDISKResourceInstance'
_N='H3cMdcActionValue'
_M='read-create'
_L='h3cMDCName'
_K='DisplayString'
_J='percent'
_I='entPhysicalIndex'
_H='ENTITY-MIB'
_G='KB'
_F='read-write'
_E='h3cMDCIndex'
_D='Integer32'
_C='H3C-MDC-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
entPhysicalIndex,=mibBuilder.importSymbols(_H,_I)
h3cCommon,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','h3cCommon')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_K,'PhysAddress','RowStatus','TextualConvention','TruthValue')
h3cMDC=ModuleIdentity((1,3,6,1,4,1,2011,10,2,136))
if mibBuilder.loadTexts:h3cMDC.setRevisions(('2013-03-05 14:48',))
class H3cMdcActionValue(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('start',1),('stop',2)))
class H3cMdcRunStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('inactive',1),('starting',2),('active',3),('stopping',4),('updating',5)))
_H3cMDCScalarObjects_ObjectIdentity=ObjectIdentity
h3cMDCScalarObjects=_H3cMDCScalarObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,136,1))
_H3cMDCMaxMDCNum_Type=Integer32
_H3cMDCMaxMDCNum_Object=MibScalar
h3cMDCMaxMDCNum=_H3cMDCMaxMDCNum_Object((1,3,6,1,4,1,2011,10,2,136,1,1),_H3cMDCMaxMDCNum_Type())
h3cMDCMaxMDCNum.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cMDCMaxMDCNum.setStatus(_A)
_H3cMDCCurrentMDCNum_Type=Integer32
_H3cMDCCurrentMDCNum_Object=MibScalar
h3cMDCCurrentMDCNum=_H3cMDCCurrentMDCNum_Object((1,3,6,1,4,1,2011,10,2,136,1,2),_H3cMDCCurrentMDCNum_Type())
h3cMDCCurrentMDCNum.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cMDCCurrentMDCNum.setStatus(_A)
_H3cMDCTables_ObjectIdentity=ObjectIdentity
h3cMDCTables=_H3cMDCTables_ObjectIdentity((1,3,6,1,4,1,2011,10,2,136,2))
_H3cMDCControl_ObjectIdentity=ObjectIdentity
h3cMDCControl=_H3cMDCControl_ObjectIdentity((1,3,6,1,4,1,2011,10,2,136,2,1))
_H3cMDCControlTable_Object=MibTable
h3cMDCControlTable=_H3cMDCControlTable_Object((1,3,6,1,4,1,2011,10,2,136,2,1,1))
if mibBuilder.loadTexts:h3cMDCControlTable.setStatus(_A)
_H3cMDCControlEntry_Object=MibTableRow
h3cMDCControlEntry=_H3cMDCControlEntry_Object((1,3,6,1,4,1,2011,10,2,136,2,1,1,1))
h3cMDCControlEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:h3cMDCControlEntry.setStatus(_A)
class _H3cMDCIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_H3cMDCIndex_Type.__name__=_D
_H3cMDCIndex_Object=MibTableColumn
h3cMDCIndex=_H3cMDCIndex_Object((1,3,6,1,4,1,2011,10,2,136,2,1,1,1,1),_H3cMDCIndex_Type())
h3cMDCIndex.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:h3cMDCIndex.setStatus(_A)
class _H3cMDCName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,15))
_H3cMDCName_Type.__name__=_K
_H3cMDCName_Object=MibTableColumn
h3cMDCName=_H3cMDCName_Object((1,3,6,1,4,1,2011,10,2,136,2,1,1,1,2),_H3cMDCName_Type())
h3cMDCName.setMaxAccess(_M)
if mibBuilder.loadTexts:h3cMDCName.setStatus(_A)
class _H3cMDCAction_Type(H3cMdcActionValue):defaultValue=2
_H3cMDCAction_Type.__name__=_N
_H3cMDCAction_Object=MibTableColumn
h3cMDCAction=_H3cMDCAction_Object((1,3,6,1,4,1,2011,10,2,136,2,1,1,1,3),_H3cMDCAction_Type())
h3cMDCAction.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cMDCAction.setStatus(_A)
_H3cMDCStatus_Type=H3cMdcRunStatus
_H3cMDCStatus_Object=MibTableColumn
h3cMDCStatus=_H3cMDCStatus_Object((1,3,6,1,4,1,2011,10,2,136,2,1,1,1,4),_H3cMDCStatus_Type())
h3cMDCStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cMDCStatus.setStatus(_A)
_H3cMDCRowStatus_Type=RowStatus
_H3cMDCRowStatus_Object=MibTableColumn
h3cMDCRowStatus=_H3cMDCRowStatus_Object((1,3,6,1,4,1,2011,10,2,136,2,1,1,1,5),_H3cMDCRowStatus_Type())
h3cMDCRowStatus.setMaxAccess(_M)
if mibBuilder.loadTexts:h3cMDCRowStatus.setStatus(_A)
_H3cMDCResource_ObjectIdentity=ObjectIdentity
h3cMDCResource=_H3cMDCResource_ObjectIdentity((1,3,6,1,4,1,2011,10,2,136,2,2))
_H3cMDCDISKResourceTable_Object=MibTable
h3cMDCDISKResourceTable=_H3cMDCDISKResourceTable_Object((1,3,6,1,4,1,2011,10,2,136,2,2,1))
if mibBuilder.loadTexts:h3cMDCDISKResourceTable.setStatus(_A)
_H3cMDCDISKResourceEntry_Object=MibTableRow
h3cMDCDISKResourceEntry=_H3cMDCDISKResourceEntry_Object((1,3,6,1,4,1,2011,10,2,136,2,2,1,1))
h3cMDCDISKResourceEntry.setIndexNames((0,_H,_I),(0,_C,_E),(0,_C,_O))
if mibBuilder.loadTexts:h3cMDCDISKResourceEntry.setStatus(_A)
class _H3cMDCDISKResourceInstance_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_H3cMDCDISKResourceInstance_Type.__name__=_D
_H3cMDCDISKResourceInstance_Object=MibTableColumn
h3cMDCDISKResourceInstance=_H3cMDCDISKResourceInstance_Object((1,3,6,1,4,1,2011,10,2,136,2,2,1,1,1),_H3cMDCDISKResourceInstance_Type())
h3cMDCDISKResourceInstance.setMaxAccess(_P)
if mibBuilder.loadTexts:h3cMDCDISKResourceInstance.setStatus(_A)
class _H3cMDCDISKResourceInstanceName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_H3cMDCDISKResourceInstanceName_Type.__name__=_K
_H3cMDCDISKResourceInstanceName_Object=MibTableColumn
h3cMDCDISKResourceInstanceName=_H3cMDCDISKResourceInstanceName_Object((1,3,6,1,4,1,2011,10,2,136,2,2,1,1,2),_H3cMDCDISKResourceInstanceName_Type())
h3cMDCDISKResourceInstanceName.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cMDCDISKResourceInstanceName.setStatus(_A)
class _H3cMDCDISKResourceMinLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_H3cMDCDISKResourceMinLimit_Type.__name__=_D
_H3cMDCDISKResourceMinLimit_Object=MibTableColumn
h3cMDCDISKResourceMinLimit=_H3cMDCDISKResourceMinLimit_Object((1,3,6,1,4,1,2011,10,2,136,2,2,1,1,3),_H3cMDCDISKResourceMinLimit_Type())
h3cMDCDISKResourceMinLimit.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cMDCDISKResourceMinLimit.setStatus(_A)
if mibBuilder.loadTexts:h3cMDCDISKResourceMinLimit.setUnits(_J)
class _H3cMDCDISKResourceMaxLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_H3cMDCDISKResourceMaxLimit_Type.__name__=_D
_H3cMDCDISKResourceMaxLimit_Object=MibTableColumn
h3cMDCDISKResourceMaxLimit=_H3cMDCDISKResourceMaxLimit_Object((1,3,6,1,4,1,2011,10,2,136,2,2,1,1,4),_H3cMDCDISKResourceMaxLimit_Type())
h3cMDCDISKResourceMaxLimit.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cMDCDISKResourceMaxLimit.setStatus(_A)
if mibBuilder.loadTexts:h3cMDCDISKResourceMaxLimit.setUnits(_J)
_H3cMDCDISKResourceReserve_Type=Unsigned32
_H3cMDCDISKResourceReserve_Object=MibTableColumn
h3cMDCDISKResourceReserve=_H3cMDCDISKResourceReserve_Object((1,3,6,1,4,1,2011,10,2,136,2,2,1,1,5),_H3cMDCDISKResourceReserve_Type())
h3cMDCDISKResourceReserve.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cMDCDISKResourceReserve.setStatus(_A)
if mibBuilder.loadTexts:h3cMDCDISKResourceReserve.setUnits(_G)
_H3cMDCDISKResourceQuota_Type=Unsigned32
_H3cMDCDISKResourceQuota_Object=MibTableColumn
h3cMDCDISKResourceQuota=_H3cMDCDISKResourceQuota_Object((1,3,6,1,4,1,2011,10,2,136,2,2,1,1,6),_H3cMDCDISKResourceQuota_Type())
h3cMDCDISKResourceQuota.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cMDCDISKResourceQuota.setStatus(_A)
if mibBuilder.loadTexts:h3cMDCDISKResourceQuota.setUnits(_G)
_H3cMDCDISKResourceUsage_Type=Unsigned32
_H3cMDCDISKResourceUsage_Object=MibTableColumn
h3cMDCDISKResourceUsage=_H3cMDCDISKResourceUsage_Object((1,3,6,1,4,1,2011,10,2,136,2,2,1,1,7),_H3cMDCDISKResourceUsage_Type())
h3cMDCDISKResourceUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cMDCDISKResourceUsage.setStatus(_A)
if mibBuilder.loadTexts:h3cMDCDISKResourceUsage.setUnits(_G)
_H3cMDCDISKResourceAvailable_Type=Unsigned32
_H3cMDCDISKResourceAvailable_Object=MibTableColumn
h3cMDCDISKResourceAvailable=_H3cMDCDISKResourceAvailable_Object((1,3,6,1,4,1,2011,10,2,136,2,2,1,1,8),_H3cMDCDISKResourceAvailable_Type())
h3cMDCDISKResourceAvailable.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cMDCDISKResourceAvailable.setStatus(_A)
if mibBuilder.loadTexts:h3cMDCDISKResourceAvailable.setUnits(_G)
_H3cMDCMemoryResourceTable_Object=MibTable
h3cMDCMemoryResourceTable=_H3cMDCMemoryResourceTable_Object((1,3,6,1,4,1,2011,10,2,136,2,2,2))
if mibBuilder.loadTexts:h3cMDCMemoryResourceTable.setStatus(_A)
_H3cMDCMemoryResourceEntry_Object=MibTableRow
h3cMDCMemoryResourceEntry=_H3cMDCMemoryResourceEntry_Object((1,3,6,1,4,1,2011,10,2,136,2,2,2,1))
h3cMDCMemoryResourceEntry.setIndexNames((0,_H,_I),(0,_C,_E))
if mibBuilder.loadTexts:h3cMDCMemoryResourceEntry.setStatus(_A)
class _H3cMDCMemoryResourceMinLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_H3cMDCMemoryResourceMinLimit_Type.__name__=_D
_H3cMDCMemoryResourceMinLimit_Object=MibTableColumn
h3cMDCMemoryResourceMinLimit=_H3cMDCMemoryResourceMinLimit_Object((1,3,6,1,4,1,2011,10,2,136,2,2,2,1,1),_H3cMDCMemoryResourceMinLimit_Type())
h3cMDCMemoryResourceMinLimit.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cMDCMemoryResourceMinLimit.setStatus(_A)
if mibBuilder.loadTexts:h3cMDCMemoryResourceMinLimit.setUnits(_J)
class _H3cMDCMemoryResourceMaxLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_H3cMDCMemoryResourceMaxLimit_Type.__name__=_D
_H3cMDCMemoryResourceMaxLimit_Object=MibTableColumn
h3cMDCMemoryResourceMaxLimit=_H3cMDCMemoryResourceMaxLimit_Object((1,3,6,1,4,1,2011,10,2,136,2,2,2,1,2),_H3cMDCMemoryResourceMaxLimit_Type())
h3cMDCMemoryResourceMaxLimit.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cMDCMemoryResourceMaxLimit.setStatus(_A)
if mibBuilder.loadTexts:h3cMDCMemoryResourceMaxLimit.setUnits(_J)
_H3cMDCMemoryResourceReserve_Type=Unsigned32
_H3cMDCMemoryResourceReserve_Object=MibTableColumn
h3cMDCMemoryResourceReserve=_H3cMDCMemoryResourceReserve_Object((1,3,6,1,4,1,2011,10,2,136,2,2,2,1,3),_H3cMDCMemoryResourceReserve_Type())
h3cMDCMemoryResourceReserve.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cMDCMemoryResourceReserve.setStatus(_A)
if mibBuilder.loadTexts:h3cMDCMemoryResourceReserve.setUnits(_G)
_H3cMDCMemoryResourceQuota_Type=Unsigned32
_H3cMDCMemoryResourceQuota_Object=MibTableColumn
h3cMDCMemoryResourceQuota=_H3cMDCMemoryResourceQuota_Object((1,3,6,1,4,1,2011,10,2,136,2,2,2,1,4),_H3cMDCMemoryResourceQuota_Type())
h3cMDCMemoryResourceQuota.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cMDCMemoryResourceQuota.setStatus(_A)
if mibBuilder.loadTexts:h3cMDCMemoryResourceQuota.setUnits(_G)
_H3cMDCMemoryResourceUsage_Type=Unsigned32
_H3cMDCMemoryResourceUsage_Object=MibTableColumn
h3cMDCMemoryResourceUsage=_H3cMDCMemoryResourceUsage_Object((1,3,6,1,4,1,2011,10,2,136,2,2,2,1,5),_H3cMDCMemoryResourceUsage_Type())
h3cMDCMemoryResourceUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cMDCMemoryResourceUsage.setStatus(_A)
if mibBuilder.loadTexts:h3cMDCMemoryResourceUsage.setUnits(_G)
_H3cMDCMemoryResourceAvailable_Type=Unsigned32
_H3cMDCMemoryResourceAvailable_Object=MibTableColumn
h3cMDCMemoryResourceAvailable=_H3cMDCMemoryResourceAvailable_Object((1,3,6,1,4,1,2011,10,2,136,2,2,2,1,6),_H3cMDCMemoryResourceAvailable_Type())
h3cMDCMemoryResourceAvailable.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cMDCMemoryResourceAvailable.setStatus(_A)
if mibBuilder.loadTexts:h3cMDCMemoryResourceAvailable.setUnits(_G)
_H3cMDCCPUResourceTable_Object=MibTable
h3cMDCCPUResourceTable=_H3cMDCCPUResourceTable_Object((1,3,6,1,4,1,2011,10,2,136,2,2,3))
if mibBuilder.loadTexts:h3cMDCCPUResourceTable.setStatus(_A)
_H3cMDCCPUResourceEntry_Object=MibTableRow
h3cMDCCPUResourceEntry=_H3cMDCCPUResourceEntry_Object((1,3,6,1,4,1,2011,10,2,136,2,2,3,1))
h3cMDCCPUResourceEntry.setIndexNames((0,_H,_I),(0,_C,_E))
if mibBuilder.loadTexts:h3cMDCCPUResourceEntry.setStatus(_A)
class _H3cMDCCPUResourceLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_H3cMDCCPUResourceLimit_Type.__name__=_D
_H3cMDCCPUResourceLimit_Object=MibTableColumn
h3cMDCCPUResourceLimit=_H3cMDCCPUResourceLimit_Object((1,3,6,1,4,1,2011,10,2,136,2,2,3,1,1),_H3cMDCCPUResourceLimit_Type())
h3cMDCCPUResourceLimit.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cMDCCPUResourceLimit.setStatus(_A)
if mibBuilder.loadTexts:h3cMDCCPUResourceLimit.setUnits('weight')
class _H3cMDCCPUResourceUsage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_H3cMDCCPUResourceUsage_Type.__name__=_D
_H3cMDCCPUResourceUsage_Object=MibTableColumn
h3cMDCCPUResourceUsage=_H3cMDCCPUResourceUsage_Object((1,3,6,1,4,1,2011,10,2,136,2,2,3,1,2),_H3cMDCCPUResourceUsage_Type())
h3cMDCCPUResourceUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cMDCCPUResourceUsage.setStatus(_A)
if mibBuilder.loadTexts:h3cMDCCPUResourceUsage.setUnits(_J)
_H3cMDCLocation_ObjectIdentity=ObjectIdentity
h3cMDCLocation=_H3cMDCLocation_ObjectIdentity((1,3,6,1,4,1,2011,10,2,136,2,3))
_H3cMDCLocationTable_Object=MibTable
h3cMDCLocationTable=_H3cMDCLocationTable_Object((1,3,6,1,4,1,2011,10,2,136,2,3,1))
if mibBuilder.loadTexts:h3cMDCLocationTable.setStatus(_A)
_H3cMDCLocationEntry_Object=MibTableRow
h3cMDCLocationEntry=_H3cMDCLocationEntry_Object((1,3,6,1,4,1,2011,10,2,136,2,3,1,1))
h3cMDCLocationEntry.setIndexNames((0,_H,_I),(0,_C,_E))
if mibBuilder.loadTexts:h3cMDCLocationEntry.setStatus(_A)
_H3cMDCLocationStatus_Type=TruthValue
_H3cMDCLocationStatus_Object=MibTableColumn
h3cMDCLocationStatus=_H3cMDCLocationStatus_Object((1,3,6,1,4,1,2011,10,2,136,2,3,1,1,1),_H3cMDCLocationStatus_Type())
h3cMDCLocationStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cMDCLocationStatus.setStatus(_A)
_H3cMDCAllocate_ObjectIdentity=ObjectIdentity
h3cMDCAllocate=_H3cMDCAllocate_ObjectIdentity((1,3,6,1,4,1,2011,10,2,136,2,4))
_H3cMDCGroupIfTable_Object=MibTable
h3cMDCGroupIfTable=_H3cMDCGroupIfTable_Object((1,3,6,1,4,1,2011,10,2,136,2,4,1))
if mibBuilder.loadTexts:h3cMDCGroupIfTable.setStatus(_A)
_H3cMDCGroupIfEntry_Object=MibTableRow
h3cMDCGroupIfEntry=_H3cMDCGroupIfEntry_Object((1,3,6,1,4,1,2011,10,2,136,2,4,1,1))
h3cMDCGroupIfEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:h3cMDCGroupIfEntry.setStatus(_A)
_H3cMDCGroupIdentity_Type=Integer32
_H3cMDCGroupIdentity_Object=MibTableColumn
h3cMDCGroupIdentity=_H3cMDCGroupIdentity_Object((1,3,6,1,4,1,2011,10,2,136,2,4,1,1,2),_H3cMDCGroupIdentity_Type())
h3cMDCGroupIdentity.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cMDCGroupIdentity.setStatus(_A)
_H3cMDCAllocateTable_Object=MibTable
h3cMDCAllocateTable=_H3cMDCAllocateTable_Object((1,3,6,1,4,1,2011,10,2,136,2,4,2))
if mibBuilder.loadTexts:h3cMDCAllocateTable.setStatus(_A)
_H3cMDCAllocateEntry_Object=MibTableRow
h3cMDCAllocateEntry=_H3cMDCAllocateEntry_Object((1,3,6,1,4,1,2011,10,2,136,2,4,2,1))
h3cMDCAllocateEntry.setIndexNames((0,_C,_Q))
if mibBuilder.loadTexts:h3cMDCAllocateEntry.setStatus(_A)
class _H3cMDCAllocateGroupIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_H3cMDCAllocateGroupIndex_Type.__name__=_D
_H3cMDCAllocateGroupIndex_Object=MibTableColumn
h3cMDCAllocateGroupIndex=_H3cMDCAllocateGroupIndex_Object((1,3,6,1,4,1,2011,10,2,136,2,4,2,1,1),_H3cMDCAllocateGroupIndex_Type())
h3cMDCAllocateGroupIndex.setMaxAccess(_P)
if mibBuilder.loadTexts:h3cMDCAllocateGroupIndex.setStatus(_A)
class _H3cMDCAllocateGroupDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_H3cMDCAllocateGroupDescription_Type.__name__=_K
_H3cMDCAllocateGroupDescription_Object=MibTableColumn
h3cMDCAllocateGroupDescription=_H3cMDCAllocateGroupDescription_Object((1,3,6,1,4,1,2011,10,2,136,2,4,2,1,2),_H3cMDCAllocateGroupDescription_Type())
h3cMDCAllocateGroupDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cMDCAllocateGroupDescription.setStatus(_A)
class _H3cMDCAllocateMDCId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_H3cMDCAllocateMDCId_Type.__name__=_D
_H3cMDCAllocateMDCId_Object=MibTableColumn
h3cMDCAllocateMDCId=_H3cMDCAllocateMDCId_Object((1,3,6,1,4,1,2011,10,2,136,2,4,2,1,3),_H3cMDCAllocateMDCId_Type())
h3cMDCAllocateMDCId.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cMDCAllocateMDCId.setStatus(_A)
_H3cMDCNotification_ObjectIdentity=ObjectIdentity
h3cMDCNotification=_H3cMDCNotification_ObjectIdentity((1,3,6,1,4,1,2011,10,2,136,3))
_H3cMDCNotificationObjects_ObjectIdentity=ObjectIdentity
h3cMDCNotificationObjects=_H3cMDCNotificationObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,136,3,0))
h3cMDCStateChangeToActive=NotificationType((1,3,6,1,4,1,2011,10,2,136,3,0,1))
h3cMDCStateChangeToActive.setObjects(*((_C,_E),(_C,_L)))
if mibBuilder.loadTexts:h3cMDCStateChangeToActive.setStatus(_A)
h3cMDCStateChangeToInactive=NotificationType((1,3,6,1,4,1,2011,10,2,136,3,0,2))
h3cMDCStateChangeToInactive.setObjects(*((_C,_E),(_C,_L)))
if mibBuilder.loadTexts:h3cMDCStateChangeToInactive.setStatus(_A)
mibBuilder.exportSymbols(_C,**{_N:H3cMdcActionValue,'H3cMdcRunStatus':H3cMdcRunStatus,'h3cMDC':h3cMDC,'h3cMDCScalarObjects':h3cMDCScalarObjects,'h3cMDCMaxMDCNum':h3cMDCMaxMDCNum,'h3cMDCCurrentMDCNum':h3cMDCCurrentMDCNum,'h3cMDCTables':h3cMDCTables,'h3cMDCControl':h3cMDCControl,'h3cMDCControlTable':h3cMDCControlTable,'h3cMDCControlEntry':h3cMDCControlEntry,_E:h3cMDCIndex,_L:h3cMDCName,'h3cMDCAction':h3cMDCAction,'h3cMDCStatus':h3cMDCStatus,'h3cMDCRowStatus':h3cMDCRowStatus,'h3cMDCResource':h3cMDCResource,'h3cMDCDISKResourceTable':h3cMDCDISKResourceTable,'h3cMDCDISKResourceEntry':h3cMDCDISKResourceEntry,_O:h3cMDCDISKResourceInstance,'h3cMDCDISKResourceInstanceName':h3cMDCDISKResourceInstanceName,'h3cMDCDISKResourceMinLimit':h3cMDCDISKResourceMinLimit,'h3cMDCDISKResourceMaxLimit':h3cMDCDISKResourceMaxLimit,'h3cMDCDISKResourceReserve':h3cMDCDISKResourceReserve,'h3cMDCDISKResourceQuota':h3cMDCDISKResourceQuota,'h3cMDCDISKResourceUsage':h3cMDCDISKResourceUsage,'h3cMDCDISKResourceAvailable':h3cMDCDISKResourceAvailable,'h3cMDCMemoryResourceTable':h3cMDCMemoryResourceTable,'h3cMDCMemoryResourceEntry':h3cMDCMemoryResourceEntry,'h3cMDCMemoryResourceMinLimit':h3cMDCMemoryResourceMinLimit,'h3cMDCMemoryResourceMaxLimit':h3cMDCMemoryResourceMaxLimit,'h3cMDCMemoryResourceReserve':h3cMDCMemoryResourceReserve,'h3cMDCMemoryResourceQuota':h3cMDCMemoryResourceQuota,'h3cMDCMemoryResourceUsage':h3cMDCMemoryResourceUsage,'h3cMDCMemoryResourceAvailable':h3cMDCMemoryResourceAvailable,'h3cMDCCPUResourceTable':h3cMDCCPUResourceTable,'h3cMDCCPUResourceEntry':h3cMDCCPUResourceEntry,'h3cMDCCPUResourceLimit':h3cMDCCPUResourceLimit,'h3cMDCCPUResourceUsage':h3cMDCCPUResourceUsage,'h3cMDCLocation':h3cMDCLocation,'h3cMDCLocationTable':h3cMDCLocationTable,'h3cMDCLocationEntry':h3cMDCLocationEntry,'h3cMDCLocationStatus':h3cMDCLocationStatus,'h3cMDCAllocate':h3cMDCAllocate,'h3cMDCGroupIfTable':h3cMDCGroupIfTable,'h3cMDCGroupIfEntry':h3cMDCGroupIfEntry,'h3cMDCGroupIdentity':h3cMDCGroupIdentity,'h3cMDCAllocateTable':h3cMDCAllocateTable,'h3cMDCAllocateEntry':h3cMDCAllocateEntry,_Q:h3cMDCAllocateGroupIndex,'h3cMDCAllocateGroupDescription':h3cMDCAllocateGroupDescription,'h3cMDCAllocateMDCId':h3cMDCAllocateMDCId,'h3cMDCNotification':h3cMDCNotification,'h3cMDCNotificationObjects':h3cMDCNotificationObjects,'h3cMDCStateChangeToActive':h3cMDCStateChangeToActive,'h3cMDCStateChangeToInactive':h3cMDCStateChangeToInactive})