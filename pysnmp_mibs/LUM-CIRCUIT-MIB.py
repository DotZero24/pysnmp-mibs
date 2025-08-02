_g='fdfrStatusGroupV5'
_f='fdfrStatusGroupV4'
_e='fdfrStatusGroupV3'
_d='fdfrStatusGroupV2'
_c='fdfrStatusGroup'
_b='fdfrStatusUnknown'
_a='circuitStatusIncomplete'
_Z='circuitStatusDown'
_Y='circuitStatusDegraded'
_X='circuitStatusOperStatus'
_W='circuitStatusAdminStatus'
_V='circuitStatusDescription'
_U='circuitStatusName'
_T='circuitGeneralStatusTableSize'
_S='circuitGeneralStateLastChangeTime'
_R='circuitGeneralConfigLastChangeTime'
_Q='undefined'
_P='fdfrStatusMplsTunnelProtectionDegraded'
_O='fdfrStatusMplsTunnelProtectionFailed'
_N='circuitStatusIndex'
_M='Unsigned32'
_L='Integer32'
_K='fdfrStatusDegraded'
_J='fdfrStatusUnexpectedMfdfrType'
_I='circuitStatusGroup'
_H='circuitGeneralGroup'
_G='fdfrStatusIncomplete'
_F='fdfrStatusDown'
_E='fdfrStatusIndex'
_D='deprecated'
_C='read-only'
_B='current'
_A='LUM-CIRCUIT-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
lumCircuitMIB,lumModules=mibBuilder.importSymbols('LUM-REG','lumCircuitMIB','lumModules')
FaultStatus,MgmtNameString=mibBuilder.importSymbols('LUM-TC','FaultStatus','MgmtNameString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_L,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_M,'iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention')
lumCircuitMIBModule=ModuleIdentity((1,3,6,1,4,1,8708,1,1,30))
if mibBuilder.loadTexts:lumCircuitMIBModule.setRevisions(('2017-06-15 00:00','2011-03-24 00:00'))
_LumCircuitConfs_ObjectIdentity=ObjectIdentity
lumCircuitConfs=_LumCircuitConfs_ObjectIdentity((1,3,6,1,4,1,8708,2,30,1))
_LumCircuitGroups_ObjectIdentity=ObjectIdentity
lumCircuitGroups=_LumCircuitGroups_ObjectIdentity((1,3,6,1,4,1,8708,2,30,1,1))
_LumCircuitCompl_ObjectIdentity=ObjectIdentity
lumCircuitCompl=_LumCircuitCompl_ObjectIdentity((1,3,6,1,4,1,8708,2,30,1,2))
_LumCircuitMIBObjects_ObjectIdentity=ObjectIdentity
lumCircuitMIBObjects=_LumCircuitMIBObjects_ObjectIdentity((1,3,6,1,4,1,8708,2,30,2))
_CircuitGeneral_ObjectIdentity=ObjectIdentity
circuitGeneral=_CircuitGeneral_ObjectIdentity((1,3,6,1,4,1,8708,2,30,2,1))
_CircuitGeneralConfigLastChangeTime_Type=DateAndTime
_CircuitGeneralConfigLastChangeTime_Object=MibScalar
circuitGeneralConfigLastChangeTime=_CircuitGeneralConfigLastChangeTime_Object((1,3,6,1,4,1,8708,2,30,2,1,1),_CircuitGeneralConfigLastChangeTime_Type())
circuitGeneralConfigLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:circuitGeneralConfigLastChangeTime.setStatus(_B)
_CircuitGeneralStateLastChangeTime_Type=DateAndTime
_CircuitGeneralStateLastChangeTime_Object=MibScalar
circuitGeneralStateLastChangeTime=_CircuitGeneralStateLastChangeTime_Object((1,3,6,1,4,1,8708,2,30,2,1,2),_CircuitGeneralStateLastChangeTime_Type())
circuitGeneralStateLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:circuitGeneralStateLastChangeTime.setStatus(_B)
_CircuitGeneralStatusTableSize_Type=Unsigned32
_CircuitGeneralStatusTableSize_Object=MibScalar
circuitGeneralStatusTableSize=_CircuitGeneralStatusTableSize_Object((1,3,6,1,4,1,8708,2,30,2,1,3),_CircuitGeneralStatusTableSize_Type())
circuitGeneralStatusTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:circuitGeneralStatusTableSize.setStatus(_B)
_CircuitStatusList_ObjectIdentity=ObjectIdentity
circuitStatusList=_CircuitStatusList_ObjectIdentity((1,3,6,1,4,1,8708,2,30,2,2))
_CircuitStatusTable_Object=MibTable
circuitStatusTable=_CircuitStatusTable_Object((1,3,6,1,4,1,8708,2,30,2,2,1))
if mibBuilder.loadTexts:circuitStatusTable.setStatus(_B)
_CircuitStatusEntry_Object=MibTableRow
circuitStatusEntry=_CircuitStatusEntry_Object((1,3,6,1,4,1,8708,2,30,2,2,1,1))
circuitStatusEntry.setIndexNames((0,_A,_N))
if mibBuilder.loadTexts:circuitStatusEntry.setStatus(_B)
class _CircuitStatusIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CircuitStatusIndex_Type.__name__=_M
_CircuitStatusIndex_Object=MibTableColumn
circuitStatusIndex=_CircuitStatusIndex_Object((1,3,6,1,4,1,8708,2,30,2,2,1,1,1),_CircuitStatusIndex_Type())
circuitStatusIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:circuitStatusIndex.setStatus(_B)
_CircuitStatusName_Type=MgmtNameString
_CircuitStatusName_Object=MibTableColumn
circuitStatusName=_CircuitStatusName_Object((1,3,6,1,4,1,8708,2,30,2,2,1,1,2),_CircuitStatusName_Type())
circuitStatusName.setMaxAccess(_C)
if mibBuilder.loadTexts:circuitStatusName.setStatus(_B)
_CircuitStatusDescription_Type=DisplayString
_CircuitStatusDescription_Object=MibTableColumn
circuitStatusDescription=_CircuitStatusDescription_Object((1,3,6,1,4,1,8708,2,30,2,2,1,1,3),_CircuitStatusDescription_Type())
circuitStatusDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:circuitStatusDescription.setStatus(_B)
class _CircuitStatusAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_Q,0),('inService',1),('maintenance',2),('notUsed',3)))
_CircuitStatusAdminStatus_Type.__name__=_L
_CircuitStatusAdminStatus_Object=MibTableColumn
circuitStatusAdminStatus=_CircuitStatusAdminStatus_Object((1,3,6,1,4,1,8708,2,30,2,2,1,1,4),_CircuitStatusAdminStatus_Type())
circuitStatusAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:circuitStatusAdminStatus.setStatus(_B)
class _CircuitStatusOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_Q,0),('incomplete',1),('down',2),('degraded',3),('up',4)))
_CircuitStatusOperStatus_Type.__name__=_L
_CircuitStatusOperStatus_Object=MibTableColumn
circuitStatusOperStatus=_CircuitStatusOperStatus_Object((1,3,6,1,4,1,8708,2,30,2,2,1,1,5),_CircuitStatusOperStatus_Type())
circuitStatusOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:circuitStatusOperStatus.setStatus(_B)
_CircuitStatusIncomplete_Type=FaultStatus
_CircuitStatusIncomplete_Object=MibTableColumn
circuitStatusIncomplete=_CircuitStatusIncomplete_Object((1,3,6,1,4,1,8708,2,30,2,2,1,1,6),_CircuitStatusIncomplete_Type())
circuitStatusIncomplete.setMaxAccess(_C)
if mibBuilder.loadTexts:circuitStatusIncomplete.setStatus(_B)
_CircuitStatusDegraded_Type=FaultStatus
_CircuitStatusDegraded_Object=MibTableColumn
circuitStatusDegraded=_CircuitStatusDegraded_Object((1,3,6,1,4,1,8708,2,30,2,2,1,1,7),_CircuitStatusDegraded_Type())
circuitStatusDegraded.setMaxAccess(_C)
if mibBuilder.loadTexts:circuitStatusDegraded.setStatus(_B)
_CircuitStatusDown_Type=FaultStatus
_CircuitStatusDown_Object=MibTableColumn
circuitStatusDown=_CircuitStatusDown_Object((1,3,6,1,4,1,8708,2,30,2,2,1,1,8),_CircuitStatusDown_Type())
circuitStatusDown.setMaxAccess(_C)
if mibBuilder.loadTexts:circuitStatusDown.setStatus(_B)
_L2CircuitStatusList_ObjectIdentity=ObjectIdentity
l2CircuitStatusList=_L2CircuitStatusList_ObjectIdentity((1,3,6,1,4,1,8708,2,30,2,3))
_FdfrStatusTable_Object=MibTable
fdfrStatusTable=_FdfrStatusTable_Object((1,3,6,1,4,1,8708,2,30,2,3,1))
if mibBuilder.loadTexts:fdfrStatusTable.setStatus(_B)
_FdfrStatusEntry_Object=MibTableRow
fdfrStatusEntry=_FdfrStatusEntry_Object((1,3,6,1,4,1,8708,2,30,2,3,1,1))
fdfrStatusEntry.setIndexNames((0,_A,_E))
if mibBuilder.loadTexts:fdfrStatusEntry.setStatus(_B)
class _FdfrStatusIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_FdfrStatusIndex_Type.__name__=_M
_FdfrStatusIndex_Object=MibTableColumn
fdfrStatusIndex=_FdfrStatusIndex_Object((1,3,6,1,4,1,8708,2,30,2,3,1,1,1),_FdfrStatusIndex_Type())
fdfrStatusIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fdfrStatusIndex.setStatus(_B)
_FdfrStatusDown_Type=FaultStatus
_FdfrStatusDown_Object=MibTableColumn
fdfrStatusDown=_FdfrStatusDown_Object((1,3,6,1,4,1,8708,2,30,2,3,1,1,2),_FdfrStatusDown_Type())
fdfrStatusDown.setMaxAccess(_C)
if mibBuilder.loadTexts:fdfrStatusDown.setStatus(_B)
_FdfrStatusIncomplete_Type=FaultStatus
_FdfrStatusIncomplete_Object=MibTableColumn
fdfrStatusIncomplete=_FdfrStatusIncomplete_Object((1,3,6,1,4,1,8708,2,30,2,3,1,1,3),_FdfrStatusIncomplete_Type())
fdfrStatusIncomplete.setMaxAccess(_C)
if mibBuilder.loadTexts:fdfrStatusIncomplete.setStatus(_B)
_FdfrStatusUnexpectedMfdfrType_Type=FaultStatus
_FdfrStatusUnexpectedMfdfrType_Object=MibTableColumn
fdfrStatusUnexpectedMfdfrType=_FdfrStatusUnexpectedMfdfrType_Object((1,3,6,1,4,1,8708,2,30,2,3,1,1,4),_FdfrStatusUnexpectedMfdfrType_Type())
fdfrStatusUnexpectedMfdfrType.setMaxAccess(_C)
if mibBuilder.loadTexts:fdfrStatusUnexpectedMfdfrType.setStatus(_B)
_FdfrStatusDegraded_Type=FaultStatus
_FdfrStatusDegraded_Object=MibTableColumn
fdfrStatusDegraded=_FdfrStatusDegraded_Object((1,3,6,1,4,1,8708,2,30,2,3,1,1,5),_FdfrStatusDegraded_Type())
fdfrStatusDegraded.setMaxAccess(_C)
if mibBuilder.loadTexts:fdfrStatusDegraded.setStatus(_B)
_FdfrStatusMplsTunnelProtectionFailed_Type=FaultStatus
_FdfrStatusMplsTunnelProtectionFailed_Object=MibTableColumn
fdfrStatusMplsTunnelProtectionFailed=_FdfrStatusMplsTunnelProtectionFailed_Object((1,3,6,1,4,1,8708,2,30,2,3,1,1,6),_FdfrStatusMplsTunnelProtectionFailed_Type())
fdfrStatusMplsTunnelProtectionFailed.setMaxAccess(_C)
if mibBuilder.loadTexts:fdfrStatusMplsTunnelProtectionFailed.setStatus(_B)
_FdfrStatusMplsTunnelProtectionDegraded_Type=FaultStatus
_FdfrStatusMplsTunnelProtectionDegraded_Object=MibTableColumn
fdfrStatusMplsTunnelProtectionDegraded=_FdfrStatusMplsTunnelProtectionDegraded_Object((1,3,6,1,4,1,8708,2,30,2,3,1,1,7),_FdfrStatusMplsTunnelProtectionDegraded_Type())
fdfrStatusMplsTunnelProtectionDegraded.setMaxAccess(_C)
if mibBuilder.loadTexts:fdfrStatusMplsTunnelProtectionDegraded.setStatus(_B)
_FdfrStatusUnknown_Type=FaultStatus
_FdfrStatusUnknown_Object=MibTableColumn
fdfrStatusUnknown=_FdfrStatusUnknown_Object((1,3,6,1,4,1,8708,2,30,2,3,1,1,8),_FdfrStatusUnknown_Type())
fdfrStatusUnknown.setMaxAccess(_C)
if mibBuilder.loadTexts:fdfrStatusUnknown.setStatus(_B)
circuitGeneralGroup=ObjectGroup((1,3,6,1,4,1,8708,2,30,1,1,1))
circuitGeneralGroup.setObjects(*((_A,_R),(_A,_S),(_A,_T)))
if mibBuilder.loadTexts:circuitGeneralGroup.setStatus(_B)
circuitStatusGroup=ObjectGroup((1,3,6,1,4,1,8708,2,30,1,1,2))
circuitStatusGroup.setObjects(*((_A,_N),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a)))
if mibBuilder.loadTexts:circuitStatusGroup.setStatus(_B)
fdfrStatusGroup=ObjectGroup((1,3,6,1,4,1,8708,2,30,1,1,3))
fdfrStatusGroup.setObjects(*((_A,_E),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:fdfrStatusGroup.setStatus(_D)
fdfrStatusGroupV2=ObjectGroup((1,3,6,1,4,1,8708,2,30,1,1,4))
fdfrStatusGroupV2.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_J)))
if mibBuilder.loadTexts:fdfrStatusGroupV2.setStatus(_D)
fdfrStatusGroupV3=ObjectGroup((1,3,6,1,4,1,8708,2,30,1,1,5))
fdfrStatusGroupV3.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:fdfrStatusGroupV3.setStatus(_D)
fdfrStatusGroupV4=ObjectGroup((1,3,6,1,4,1,8708,2,30,1,1,6))
fdfrStatusGroupV4.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_J),(_A,_K),(_A,_O),(_A,_P)))
if mibBuilder.loadTexts:fdfrStatusGroupV4.setStatus(_D)
fdfrStatusGroupV5=ObjectGroup((1,3,6,1,4,1,8708,2,30,1,1,7))
fdfrStatusGroupV5.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_J),(_A,_K),(_A,_O),(_A,_P),(_A,_b)))
if mibBuilder.loadTexts:fdfrStatusGroupV5.setStatus(_B)
lumCircuitBasicComplV1=ModuleCompliance((1,3,6,1,4,1,8708,2,30,1,2,1))
lumCircuitBasicComplV1.setObjects(*((_A,_H),(_A,_I),(_A,_c)))
if mibBuilder.loadTexts:lumCircuitBasicComplV1.setStatus(_D)
lumCircuitBasicComplV2=ModuleCompliance((1,3,6,1,4,1,8708,2,30,1,2,2))
lumCircuitBasicComplV2.setObjects(*((_A,_H),(_A,_I),(_A,_d)))
if mibBuilder.loadTexts:lumCircuitBasicComplV2.setStatus(_D)
lumCircuitBasicComplV3=ModuleCompliance((1,3,6,1,4,1,8708,2,30,1,2,3))
lumCircuitBasicComplV3.setObjects(*((_A,_H),(_A,_I),(_A,_e)))
if mibBuilder.loadTexts:lumCircuitBasicComplV3.setStatus(_D)
lumCircuitBasicComplV4=ModuleCompliance((1,3,6,1,4,1,8708,2,30,1,2,4))
lumCircuitBasicComplV4.setObjects(*((_A,_H),(_A,_I),(_A,_f)))
if mibBuilder.loadTexts:lumCircuitBasicComplV4.setStatus(_D)
lumCircuitBasicComplV5=ModuleCompliance((1,3,6,1,4,1,8708,2,30,1,2,5))
lumCircuitBasicComplV5.setObjects(*((_A,_H),(_A,_I),(_A,_g)))
if mibBuilder.loadTexts:lumCircuitBasicComplV5.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'lumCircuitMIBModule':lumCircuitMIBModule,'lumCircuitConfs':lumCircuitConfs,'lumCircuitGroups':lumCircuitGroups,_H:circuitGeneralGroup,_I:circuitStatusGroup,_c:fdfrStatusGroup,_d:fdfrStatusGroupV2,_e:fdfrStatusGroupV3,_f:fdfrStatusGroupV4,_g:fdfrStatusGroupV5,'lumCircuitCompl':lumCircuitCompl,'lumCircuitBasicComplV1':lumCircuitBasicComplV1,'lumCircuitBasicComplV2':lumCircuitBasicComplV2,'lumCircuitBasicComplV3':lumCircuitBasicComplV3,'lumCircuitBasicComplV4':lumCircuitBasicComplV4,'lumCircuitBasicComplV5':lumCircuitBasicComplV5,'lumCircuitMIBObjects':lumCircuitMIBObjects,'circuitGeneral':circuitGeneral,_R:circuitGeneralConfigLastChangeTime,_S:circuitGeneralStateLastChangeTime,_T:circuitGeneralStatusTableSize,'circuitStatusList':circuitStatusList,'circuitStatusTable':circuitStatusTable,'circuitStatusEntry':circuitStatusEntry,_N:circuitStatusIndex,_U:circuitStatusName,_V:circuitStatusDescription,_W:circuitStatusAdminStatus,_X:circuitStatusOperStatus,_a:circuitStatusIncomplete,_Y:circuitStatusDegraded,_Z:circuitStatusDown,'l2CircuitStatusList':l2CircuitStatusList,'fdfrStatusTable':fdfrStatusTable,'fdfrStatusEntry':fdfrStatusEntry,_E:fdfrStatusIndex,_F:fdfrStatusDown,_G:fdfrStatusIncomplete,_J:fdfrStatusUnexpectedMfdfrType,_K:fdfrStatusDegraded,_O:fdfrStatusMplsTunnelProtectionFailed,_P:fdfrStatusMplsTunnelProtectionDegraded,_b:fdfrStatusUnknown})