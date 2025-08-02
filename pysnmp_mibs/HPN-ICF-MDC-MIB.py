_Q='hpnicfMDCAllocateGroupIndex'
_P='not-accessible'
_O='hpnicfMDCDISKResourceInstance'
_N='HpnicfMdcActionValue'
_M='read-create'
_L='hpnicfMDCName'
_K='DisplayString'
_J='percent'
_I='entPhysicalIndex'
_H='ENTITY-MIB'
_G='KB'
_F='read-write'
_E='hpnicfMDCIndex'
_D='Integer32'
_C='HPN-ICF-MDC-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
entPhysicalIndex,=mibBuilder.importSymbols(_H,_I)
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_K,'PhysAddress','RowStatus','TextualConvention','TruthValue')
hpnicfMDC=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,136))
if mibBuilder.loadTexts:hpnicfMDC.setRevisions(('2013-03-05 14:48',))
class HpnicfMdcActionValue(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('start',1),('stop',2)))
class HpnicfMdcRunStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('inactive',1),('starting',2),('active',3),('stopping',4),('updating',5)))
_HpnicfMDCScalarObjects_ObjectIdentity=ObjectIdentity
hpnicfMDCScalarObjects=_HpnicfMDCScalarObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,136,1))
_HpnicfMDCMaxMDCNum_Type=Integer32
_HpnicfMDCMaxMDCNum_Object=MibScalar
hpnicfMDCMaxMDCNum=_HpnicfMDCMaxMDCNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,136,1,1),_HpnicfMDCMaxMDCNum_Type())
hpnicfMDCMaxMDCNum.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfMDCMaxMDCNum.setStatus(_A)
_HpnicfMDCCurrentMDCNum_Type=Integer32
_HpnicfMDCCurrentMDCNum_Object=MibScalar
hpnicfMDCCurrentMDCNum=_HpnicfMDCCurrentMDCNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,136,1,2),_HpnicfMDCCurrentMDCNum_Type())
hpnicfMDCCurrentMDCNum.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfMDCCurrentMDCNum.setStatus(_A)
_HpnicfMDCTables_ObjectIdentity=ObjectIdentity
hpnicfMDCTables=_HpnicfMDCTables_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,136,2))
_HpnicfMDCControl_ObjectIdentity=ObjectIdentity
hpnicfMDCControl=_HpnicfMDCControl_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,136,2,1))
_HpnicfMDCControlTable_Object=MibTable
hpnicfMDCControlTable=_HpnicfMDCControlTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,136,2,1,1))
if mibBuilder.loadTexts:hpnicfMDCControlTable.setStatus(_A)
_HpnicfMDCControlEntry_Object=MibTableRow
hpnicfMDCControlEntry=_HpnicfMDCControlEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,136,2,1,1,1))
hpnicfMDCControlEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:hpnicfMDCControlEntry.setStatus(_A)
class _HpnicfMDCIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HpnicfMDCIndex_Type.__name__=_D
_HpnicfMDCIndex_Object=MibTableColumn
hpnicfMDCIndex=_HpnicfMDCIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,136,2,1,1,1,1),_HpnicfMDCIndex_Type())
hpnicfMDCIndex.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:hpnicfMDCIndex.setStatus(_A)
class _HpnicfMDCName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,15))
_HpnicfMDCName_Type.__name__=_K
_HpnicfMDCName_Object=MibTableColumn
hpnicfMDCName=_HpnicfMDCName_Object((1,3,6,1,4,1,11,2,14,11,15,2,136,2,1,1,1,2),_HpnicfMDCName_Type())
hpnicfMDCName.setMaxAccess(_M)
if mibBuilder.loadTexts:hpnicfMDCName.setStatus(_A)
class _HpnicfMDCAction_Type(HpnicfMdcActionValue):defaultValue=2
_HpnicfMDCAction_Type.__name__=_N
_HpnicfMDCAction_Object=MibTableColumn
hpnicfMDCAction=_HpnicfMDCAction_Object((1,3,6,1,4,1,11,2,14,11,15,2,136,2,1,1,1,3),_HpnicfMDCAction_Type())
hpnicfMDCAction.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfMDCAction.setStatus(_A)
_HpnicfMDCStatus_Type=HpnicfMdcRunStatus
_HpnicfMDCStatus_Object=MibTableColumn
hpnicfMDCStatus=_HpnicfMDCStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,136,2,1,1,1,4),_HpnicfMDCStatus_Type())
hpnicfMDCStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfMDCStatus.setStatus(_A)
_HpnicfMDCRowStatus_Type=RowStatus
_HpnicfMDCRowStatus_Object=MibTableColumn
hpnicfMDCRowStatus=_HpnicfMDCRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,136,2,1,1,1,5),_HpnicfMDCRowStatus_Type())
hpnicfMDCRowStatus.setMaxAccess(_M)
if mibBuilder.loadTexts:hpnicfMDCRowStatus.setStatus(_A)
_HpnicfMDCResource_ObjectIdentity=ObjectIdentity
hpnicfMDCResource=_HpnicfMDCResource_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,136,2,2))
_HpnicfMDCDISKResourceTable_Object=MibTable
hpnicfMDCDISKResourceTable=_HpnicfMDCDISKResourceTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,136,2,2,1))
if mibBuilder.loadTexts:hpnicfMDCDISKResourceTable.setStatus(_A)
_HpnicfMDCDISKResourceEntry_Object=MibTableRow
hpnicfMDCDISKResourceEntry=_HpnicfMDCDISKResourceEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,136,2,2,1,1))
hpnicfMDCDISKResourceEntry.setIndexNames((0,_H,_I),(0,_C,_E),(0,_C,_O))
if mibBuilder.loadTexts:hpnicfMDCDISKResourceEntry.setStatus(_A)
class _HpnicfMDCDISKResourceInstance_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HpnicfMDCDISKResourceInstance_Type.__name__=_D
_HpnicfMDCDISKResourceInstance_Object=MibTableColumn
hpnicfMDCDISKResourceInstance=_HpnicfMDCDISKResourceInstance_Object((1,3,6,1,4,1,11,2,14,11,15,2,136,2,2,1,1,1),_HpnicfMDCDISKResourceInstance_Type())
hpnicfMDCDISKResourceInstance.setMaxAccess(_P)
if mibBuilder.loadTexts:hpnicfMDCDISKResourceInstance.setStatus(_A)
class _HpnicfMDCDISKResourceInstanceName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_HpnicfMDCDISKResourceInstanceName_Type.__name__=_K
_HpnicfMDCDISKResourceInstanceName_Object=MibTableColumn
hpnicfMDCDISKResourceInstanceName=_HpnicfMDCDISKResourceInstanceName_Object((1,3,6,1,4,1,11,2,14,11,15,2,136,2,2,1,1,2),_HpnicfMDCDISKResourceInstanceName_Type())
hpnicfMDCDISKResourceInstanceName.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfMDCDISKResourceInstanceName.setStatus(_A)
class _HpnicfMDCDISKResourceMinLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HpnicfMDCDISKResourceMinLimit_Type.__name__=_D
_HpnicfMDCDISKResourceMinLimit_Object=MibTableColumn
hpnicfMDCDISKResourceMinLimit=_HpnicfMDCDISKResourceMinLimit_Object((1,3,6,1,4,1,11,2,14,11,15,2,136,2,2,1,1,3),_HpnicfMDCDISKResourceMinLimit_Type())
hpnicfMDCDISKResourceMinLimit.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfMDCDISKResourceMinLimit.setStatus(_A)
if mibBuilder.loadTexts:hpnicfMDCDISKResourceMinLimit.setUnits(_J)
class _HpnicfMDCDISKResourceMaxLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_HpnicfMDCDISKResourceMaxLimit_Type.__name__=_D
_HpnicfMDCDISKResourceMaxLimit_Object=MibTableColumn
hpnicfMDCDISKResourceMaxLimit=_HpnicfMDCDISKResourceMaxLimit_Object((1,3,6,1,4,1,11,2,14,11,15,2,136,2,2,1,1,4),_HpnicfMDCDISKResourceMaxLimit_Type())
hpnicfMDCDISKResourceMaxLimit.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfMDCDISKResourceMaxLimit.setStatus(_A)
if mibBuilder.loadTexts:hpnicfMDCDISKResourceMaxLimit.setUnits(_J)
_HpnicfMDCDISKResourceReserve_Type=Unsigned32
_HpnicfMDCDISKResourceReserve_Object=MibTableColumn
hpnicfMDCDISKResourceReserve=_HpnicfMDCDISKResourceReserve_Object((1,3,6,1,4,1,11,2,14,11,15,2,136,2,2,1,1,5),_HpnicfMDCDISKResourceReserve_Type())
hpnicfMDCDISKResourceReserve.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfMDCDISKResourceReserve.setStatus(_A)
if mibBuilder.loadTexts:hpnicfMDCDISKResourceReserve.setUnits(_G)
_HpnicfMDCDISKResourceQuota_Type=Unsigned32
_HpnicfMDCDISKResourceQuota_Object=MibTableColumn
hpnicfMDCDISKResourceQuota=_HpnicfMDCDISKResourceQuota_Object((1,3,6,1,4,1,11,2,14,11,15,2,136,2,2,1,1,6),_HpnicfMDCDISKResourceQuota_Type())
hpnicfMDCDISKResourceQuota.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfMDCDISKResourceQuota.setStatus(_A)
if mibBuilder.loadTexts:hpnicfMDCDISKResourceQuota.setUnits(_G)
_HpnicfMDCDISKResourceUsage_Type=Unsigned32
_HpnicfMDCDISKResourceUsage_Object=MibTableColumn
hpnicfMDCDISKResourceUsage=_HpnicfMDCDISKResourceUsage_Object((1,3,6,1,4,1,11,2,14,11,15,2,136,2,2,1,1,7),_HpnicfMDCDISKResourceUsage_Type())
hpnicfMDCDISKResourceUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfMDCDISKResourceUsage.setStatus(_A)
if mibBuilder.loadTexts:hpnicfMDCDISKResourceUsage.setUnits(_G)
_HpnicfMDCDISKResourceAvailable_Type=Unsigned32
_HpnicfMDCDISKResourceAvailable_Object=MibTableColumn
hpnicfMDCDISKResourceAvailable=_HpnicfMDCDISKResourceAvailable_Object((1,3,6,1,4,1,11,2,14,11,15,2,136,2,2,1,1,8),_HpnicfMDCDISKResourceAvailable_Type())
hpnicfMDCDISKResourceAvailable.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfMDCDISKResourceAvailable.setStatus(_A)
if mibBuilder.loadTexts:hpnicfMDCDISKResourceAvailable.setUnits(_G)
_HpnicfMDCMemoryResourceTable_Object=MibTable
hpnicfMDCMemoryResourceTable=_HpnicfMDCMemoryResourceTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,136,2,2,2))
if mibBuilder.loadTexts:hpnicfMDCMemoryResourceTable.setStatus(_A)
_HpnicfMDCMemoryResourceEntry_Object=MibTableRow
hpnicfMDCMemoryResourceEntry=_HpnicfMDCMemoryResourceEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,136,2,2,2,1))
hpnicfMDCMemoryResourceEntry.setIndexNames((0,_H,_I),(0,_C,_E))
if mibBuilder.loadTexts:hpnicfMDCMemoryResourceEntry.setStatus(_A)
class _HpnicfMDCMemoryResourceMinLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HpnicfMDCMemoryResourceMinLimit_Type.__name__=_D
_HpnicfMDCMemoryResourceMinLimit_Object=MibTableColumn
hpnicfMDCMemoryResourceMinLimit=_HpnicfMDCMemoryResourceMinLimit_Object((1,3,6,1,4,1,11,2,14,11,15,2,136,2,2,2,1,1),_HpnicfMDCMemoryResourceMinLimit_Type())
hpnicfMDCMemoryResourceMinLimit.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfMDCMemoryResourceMinLimit.setStatus(_A)
if mibBuilder.loadTexts:hpnicfMDCMemoryResourceMinLimit.setUnits(_J)
class _HpnicfMDCMemoryResourceMaxLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_HpnicfMDCMemoryResourceMaxLimit_Type.__name__=_D
_HpnicfMDCMemoryResourceMaxLimit_Object=MibTableColumn
hpnicfMDCMemoryResourceMaxLimit=_HpnicfMDCMemoryResourceMaxLimit_Object((1,3,6,1,4,1,11,2,14,11,15,2,136,2,2,2,1,2),_HpnicfMDCMemoryResourceMaxLimit_Type())
hpnicfMDCMemoryResourceMaxLimit.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfMDCMemoryResourceMaxLimit.setStatus(_A)
if mibBuilder.loadTexts:hpnicfMDCMemoryResourceMaxLimit.setUnits(_J)
_HpnicfMDCMemoryResourceReserve_Type=Unsigned32
_HpnicfMDCMemoryResourceReserve_Object=MibTableColumn
hpnicfMDCMemoryResourceReserve=_HpnicfMDCMemoryResourceReserve_Object((1,3,6,1,4,1,11,2,14,11,15,2,136,2,2,2,1,3),_HpnicfMDCMemoryResourceReserve_Type())
hpnicfMDCMemoryResourceReserve.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfMDCMemoryResourceReserve.setStatus(_A)
if mibBuilder.loadTexts:hpnicfMDCMemoryResourceReserve.setUnits(_G)
_HpnicfMDCMemoryResourceQuota_Type=Unsigned32
_HpnicfMDCMemoryResourceQuota_Object=MibTableColumn
hpnicfMDCMemoryResourceQuota=_HpnicfMDCMemoryResourceQuota_Object((1,3,6,1,4,1,11,2,14,11,15,2,136,2,2,2,1,4),_HpnicfMDCMemoryResourceQuota_Type())
hpnicfMDCMemoryResourceQuota.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfMDCMemoryResourceQuota.setStatus(_A)
if mibBuilder.loadTexts:hpnicfMDCMemoryResourceQuota.setUnits(_G)
_HpnicfMDCMemoryResourceUsage_Type=Unsigned32
_HpnicfMDCMemoryResourceUsage_Object=MibTableColumn
hpnicfMDCMemoryResourceUsage=_HpnicfMDCMemoryResourceUsage_Object((1,3,6,1,4,1,11,2,14,11,15,2,136,2,2,2,1,5),_HpnicfMDCMemoryResourceUsage_Type())
hpnicfMDCMemoryResourceUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfMDCMemoryResourceUsage.setStatus(_A)
if mibBuilder.loadTexts:hpnicfMDCMemoryResourceUsage.setUnits(_G)
_HpnicfMDCMemoryResourceAvailable_Type=Unsigned32
_HpnicfMDCMemoryResourceAvailable_Object=MibTableColumn
hpnicfMDCMemoryResourceAvailable=_HpnicfMDCMemoryResourceAvailable_Object((1,3,6,1,4,1,11,2,14,11,15,2,136,2,2,2,1,6),_HpnicfMDCMemoryResourceAvailable_Type())
hpnicfMDCMemoryResourceAvailable.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfMDCMemoryResourceAvailable.setStatus(_A)
if mibBuilder.loadTexts:hpnicfMDCMemoryResourceAvailable.setUnits(_G)
_HpnicfMDCCPUResourceTable_Object=MibTable
hpnicfMDCCPUResourceTable=_HpnicfMDCCPUResourceTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,136,2,2,3))
if mibBuilder.loadTexts:hpnicfMDCCPUResourceTable.setStatus(_A)
_HpnicfMDCCPUResourceEntry_Object=MibTableRow
hpnicfMDCCPUResourceEntry=_HpnicfMDCCPUResourceEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,136,2,2,3,1))
hpnicfMDCCPUResourceEntry.setIndexNames((0,_H,_I),(0,_C,_E))
if mibBuilder.loadTexts:hpnicfMDCCPUResourceEntry.setStatus(_A)
class _HpnicfMDCCPUResourceLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_HpnicfMDCCPUResourceLimit_Type.__name__=_D
_HpnicfMDCCPUResourceLimit_Object=MibTableColumn
hpnicfMDCCPUResourceLimit=_HpnicfMDCCPUResourceLimit_Object((1,3,6,1,4,1,11,2,14,11,15,2,136,2,2,3,1,1),_HpnicfMDCCPUResourceLimit_Type())
hpnicfMDCCPUResourceLimit.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfMDCCPUResourceLimit.setStatus(_A)
if mibBuilder.loadTexts:hpnicfMDCCPUResourceLimit.setUnits('weight')
class _HpnicfMDCCPUResourceUsage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HpnicfMDCCPUResourceUsage_Type.__name__=_D
_HpnicfMDCCPUResourceUsage_Object=MibTableColumn
hpnicfMDCCPUResourceUsage=_HpnicfMDCCPUResourceUsage_Object((1,3,6,1,4,1,11,2,14,11,15,2,136,2,2,3,1,2),_HpnicfMDCCPUResourceUsage_Type())
hpnicfMDCCPUResourceUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfMDCCPUResourceUsage.setStatus(_A)
if mibBuilder.loadTexts:hpnicfMDCCPUResourceUsage.setUnits(_J)
_HpnicfMDCLocation_ObjectIdentity=ObjectIdentity
hpnicfMDCLocation=_HpnicfMDCLocation_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,136,2,3))
_HpnicfMDCLocationTable_Object=MibTable
hpnicfMDCLocationTable=_HpnicfMDCLocationTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,136,2,3,1))
if mibBuilder.loadTexts:hpnicfMDCLocationTable.setStatus(_A)
_HpnicfMDCLocationEntry_Object=MibTableRow
hpnicfMDCLocationEntry=_HpnicfMDCLocationEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,136,2,3,1,1))
hpnicfMDCLocationEntry.setIndexNames((0,_H,_I),(0,_C,_E))
if mibBuilder.loadTexts:hpnicfMDCLocationEntry.setStatus(_A)
_HpnicfMDCLocationStatus_Type=TruthValue
_HpnicfMDCLocationStatus_Object=MibTableColumn
hpnicfMDCLocationStatus=_HpnicfMDCLocationStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,136,2,3,1,1,1),_HpnicfMDCLocationStatus_Type())
hpnicfMDCLocationStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfMDCLocationStatus.setStatus(_A)
_HpnicfMDCAllocate_ObjectIdentity=ObjectIdentity
hpnicfMDCAllocate=_HpnicfMDCAllocate_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,136,2,4))
_HpnicfMDCGroupIfTable_Object=MibTable
hpnicfMDCGroupIfTable=_HpnicfMDCGroupIfTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,136,2,4,1))
if mibBuilder.loadTexts:hpnicfMDCGroupIfTable.setStatus(_A)
_HpnicfMDCGroupIfEntry_Object=MibTableRow
hpnicfMDCGroupIfEntry=_HpnicfMDCGroupIfEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,136,2,4,1,1))
hpnicfMDCGroupIfEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:hpnicfMDCGroupIfEntry.setStatus(_A)
_HpnicfMDCGroupIdentity_Type=Integer32
_HpnicfMDCGroupIdentity_Object=MibTableColumn
hpnicfMDCGroupIdentity=_HpnicfMDCGroupIdentity_Object((1,3,6,1,4,1,11,2,14,11,15,2,136,2,4,1,1,2),_HpnicfMDCGroupIdentity_Type())
hpnicfMDCGroupIdentity.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfMDCGroupIdentity.setStatus(_A)
_HpnicfMDCAllocateTable_Object=MibTable
hpnicfMDCAllocateTable=_HpnicfMDCAllocateTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,136,2,4,2))
if mibBuilder.loadTexts:hpnicfMDCAllocateTable.setStatus(_A)
_HpnicfMDCAllocateEntry_Object=MibTableRow
hpnicfMDCAllocateEntry=_HpnicfMDCAllocateEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,136,2,4,2,1))
hpnicfMDCAllocateEntry.setIndexNames((0,_C,_Q))
if mibBuilder.loadTexts:hpnicfMDCAllocateEntry.setStatus(_A)
class _HpnicfMDCAllocateGroupIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HpnicfMDCAllocateGroupIndex_Type.__name__=_D
_HpnicfMDCAllocateGroupIndex_Object=MibTableColumn
hpnicfMDCAllocateGroupIndex=_HpnicfMDCAllocateGroupIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,136,2,4,2,1,1),_HpnicfMDCAllocateGroupIndex_Type())
hpnicfMDCAllocateGroupIndex.setMaxAccess(_P)
if mibBuilder.loadTexts:hpnicfMDCAllocateGroupIndex.setStatus(_A)
class _HpnicfMDCAllocateGroupDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_HpnicfMDCAllocateGroupDescription_Type.__name__=_K
_HpnicfMDCAllocateGroupDescription_Object=MibTableColumn
hpnicfMDCAllocateGroupDescription=_HpnicfMDCAllocateGroupDescription_Object((1,3,6,1,4,1,11,2,14,11,15,2,136,2,4,2,1,2),_HpnicfMDCAllocateGroupDescription_Type())
hpnicfMDCAllocateGroupDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfMDCAllocateGroupDescription.setStatus(_A)
class _HpnicfMDCAllocateMDCId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HpnicfMDCAllocateMDCId_Type.__name__=_D
_HpnicfMDCAllocateMDCId_Object=MibTableColumn
hpnicfMDCAllocateMDCId=_HpnicfMDCAllocateMDCId_Object((1,3,6,1,4,1,11,2,14,11,15,2,136,2,4,2,1,3),_HpnicfMDCAllocateMDCId_Type())
hpnicfMDCAllocateMDCId.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfMDCAllocateMDCId.setStatus(_A)
_HpnicfMDCNotification_ObjectIdentity=ObjectIdentity
hpnicfMDCNotification=_HpnicfMDCNotification_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,136,3))
_HpnicfMDCNotificationObjects_ObjectIdentity=ObjectIdentity
hpnicfMDCNotificationObjects=_HpnicfMDCNotificationObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,136,3,0))
hpnicfMDCStateChangeToActive=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,136,3,0,1))
hpnicfMDCStateChangeToActive.setObjects(*((_C,_E),(_C,_L)))
if mibBuilder.loadTexts:hpnicfMDCStateChangeToActive.setStatus(_A)
hpnicfMDCStateChangeToInactive=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,136,3,0,2))
hpnicfMDCStateChangeToInactive.setObjects(*((_C,_E),(_C,_L)))
if mibBuilder.loadTexts:hpnicfMDCStateChangeToInactive.setStatus(_A)
mibBuilder.exportSymbols(_C,**{_N:HpnicfMdcActionValue,'HpnicfMdcRunStatus':HpnicfMdcRunStatus,'hpnicfMDC':hpnicfMDC,'hpnicfMDCScalarObjects':hpnicfMDCScalarObjects,'hpnicfMDCMaxMDCNum':hpnicfMDCMaxMDCNum,'hpnicfMDCCurrentMDCNum':hpnicfMDCCurrentMDCNum,'hpnicfMDCTables':hpnicfMDCTables,'hpnicfMDCControl':hpnicfMDCControl,'hpnicfMDCControlTable':hpnicfMDCControlTable,'hpnicfMDCControlEntry':hpnicfMDCControlEntry,_E:hpnicfMDCIndex,_L:hpnicfMDCName,'hpnicfMDCAction':hpnicfMDCAction,'hpnicfMDCStatus':hpnicfMDCStatus,'hpnicfMDCRowStatus':hpnicfMDCRowStatus,'hpnicfMDCResource':hpnicfMDCResource,'hpnicfMDCDISKResourceTable':hpnicfMDCDISKResourceTable,'hpnicfMDCDISKResourceEntry':hpnicfMDCDISKResourceEntry,_O:hpnicfMDCDISKResourceInstance,'hpnicfMDCDISKResourceInstanceName':hpnicfMDCDISKResourceInstanceName,'hpnicfMDCDISKResourceMinLimit':hpnicfMDCDISKResourceMinLimit,'hpnicfMDCDISKResourceMaxLimit':hpnicfMDCDISKResourceMaxLimit,'hpnicfMDCDISKResourceReserve':hpnicfMDCDISKResourceReserve,'hpnicfMDCDISKResourceQuota':hpnicfMDCDISKResourceQuota,'hpnicfMDCDISKResourceUsage':hpnicfMDCDISKResourceUsage,'hpnicfMDCDISKResourceAvailable':hpnicfMDCDISKResourceAvailable,'hpnicfMDCMemoryResourceTable':hpnicfMDCMemoryResourceTable,'hpnicfMDCMemoryResourceEntry':hpnicfMDCMemoryResourceEntry,'hpnicfMDCMemoryResourceMinLimit':hpnicfMDCMemoryResourceMinLimit,'hpnicfMDCMemoryResourceMaxLimit':hpnicfMDCMemoryResourceMaxLimit,'hpnicfMDCMemoryResourceReserve':hpnicfMDCMemoryResourceReserve,'hpnicfMDCMemoryResourceQuota':hpnicfMDCMemoryResourceQuota,'hpnicfMDCMemoryResourceUsage':hpnicfMDCMemoryResourceUsage,'hpnicfMDCMemoryResourceAvailable':hpnicfMDCMemoryResourceAvailable,'hpnicfMDCCPUResourceTable':hpnicfMDCCPUResourceTable,'hpnicfMDCCPUResourceEntry':hpnicfMDCCPUResourceEntry,'hpnicfMDCCPUResourceLimit':hpnicfMDCCPUResourceLimit,'hpnicfMDCCPUResourceUsage':hpnicfMDCCPUResourceUsage,'hpnicfMDCLocation':hpnicfMDCLocation,'hpnicfMDCLocationTable':hpnicfMDCLocationTable,'hpnicfMDCLocationEntry':hpnicfMDCLocationEntry,'hpnicfMDCLocationStatus':hpnicfMDCLocationStatus,'hpnicfMDCAllocate':hpnicfMDCAllocate,'hpnicfMDCGroupIfTable':hpnicfMDCGroupIfTable,'hpnicfMDCGroupIfEntry':hpnicfMDCGroupIfEntry,'hpnicfMDCGroupIdentity':hpnicfMDCGroupIdentity,'hpnicfMDCAllocateTable':hpnicfMDCAllocateTable,'hpnicfMDCAllocateEntry':hpnicfMDCAllocateEntry,_Q:hpnicfMDCAllocateGroupIndex,'hpnicfMDCAllocateGroupDescription':hpnicfMDCAllocateGroupDescription,'hpnicfMDCAllocateMDCId':hpnicfMDCAllocateMDCId,'hpnicfMDCNotification':hpnicfMDCNotification,'hpnicfMDCNotificationObjects':hpnicfMDCNotificationObjects,'hpnicfMDCStateChangeToActive':hpnicfMDCStateChangeToActive,'hpnicfMDCStateChangeToInactive':hpnicfMDCStateChangeToInactive})