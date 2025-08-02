_Y='oammMjJoinStatus'
_X='oammMjOperStatus'
_W='oammMjAdminStatus'
_V='oammMjRowStatus'
_U='oammEntRescheduleLimit'
_T='oammEntFriBufferPoolSize'
_S='oammEntEnableTrapSupport'
_R='oammEntOperStatus'
_Q='oammEntAdminStatus'
_P='oammEntRowStatus'
_O='oammMjSubIndex'
_N='oammMjPartnerIndex'
_M='oammMjPartnerType'
_L='oammMjInterfaceId'
_K='oammMjApplIndex'
_J='oammEntApplIndex'
_I='TruthValue'
_H='oammGeneralGroup'
_G='read-only'
_F='Integer32'
_E='AdminStatus'
_D='not-accessible'
_C='read-create'
_B='DC-OAMM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
AdminStatus,BaseOperStatus,MjStatus,OperStatus=mibBuilder.importSymbols('DC-MASTER-TC',_E,'BaseOperStatus','MjStatus','OperStatus')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_I)
oammMib=ModuleIdentity((1,3,6,1,4,1,629,10,14))
if mibBuilder.loadTexts:oammMib.setRevisions(('2014-12-21 00:00',))
class OammMjIfId(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(696844288,697761792,1518338048,1904214016,1988100096)));namedValues=NamedValues(*(('ifAtgI3',696844288),('ifAtgFri',697761792),('ifAtgBfdi',1518338048),('ifAtgLpi',1904214016),('ifAtgPmi',1988100096)))
_Nbase_ObjectIdentity=ObjectIdentity
nbase=_Nbase_ObjectIdentity((1,3,6,1,4,1,629))
_Opx_ObjectIdentity=ObjectIdentity
opx=_Opx_ObjectIdentity((1,3,6,1,4,1,629,10))
_OammObjects_ObjectIdentity=ObjectIdentity
oammObjects=_OammObjects_ObjectIdentity((1,3,6,1,4,1,629,10,14,1))
_OammEntTable_Object=MibTable
oammEntTable=_OammEntTable_Object((1,3,6,1,4,1,629,10,14,1,1))
if mibBuilder.loadTexts:oammEntTable.setStatus(_A)
_OammEntEntry_Object=MibTableRow
oammEntEntry=_OammEntEntry_Object((1,3,6,1,4,1,629,10,14,1,1,1))
oammEntEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:oammEntEntry.setStatus(_A)
_OammEntApplIndex_Type=Unsigned32
_OammEntApplIndex_Object=MibTableColumn
oammEntApplIndex=_OammEntApplIndex_Object((1,3,6,1,4,1,629,10,14,1,1,1,1),_OammEntApplIndex_Type())
oammEntApplIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:oammEntApplIndex.setStatus(_A)
_OammEntRowStatus_Type=RowStatus
_OammEntRowStatus_Object=MibTableColumn
oammEntRowStatus=_OammEntRowStatus_Object((1,3,6,1,4,1,629,10,14,1,1,1,2),_OammEntRowStatus_Type())
oammEntRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:oammEntRowStatus.setStatus(_A)
class _OammEntAdminStatus_Type(AdminStatus):defaultValue=1
_OammEntAdminStatus_Type.__name__=_E
_OammEntAdminStatus_Object=MibTableColumn
oammEntAdminStatus=_OammEntAdminStatus_Object((1,3,6,1,4,1,629,10,14,1,1,1,3),_OammEntAdminStatus_Type())
oammEntAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:oammEntAdminStatus.setStatus(_A)
_OammEntOperStatus_Type=BaseOperStatus
_OammEntOperStatus_Object=MibTableColumn
oammEntOperStatus=_OammEntOperStatus_Object((1,3,6,1,4,1,629,10,14,1,1,1,4),_OammEntOperStatus_Type())
oammEntOperStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:oammEntOperStatus.setStatus(_A)
class _OammEntEnableTrapSupport_Type(TruthValue):defaultValue=2
_OammEntEnableTrapSupport_Type.__name__=_I
_OammEntEnableTrapSupport_Object=MibTableColumn
oammEntEnableTrapSupport=_OammEntEnableTrapSupport_Object((1,3,6,1,4,1,629,10,14,1,1,1,5),_OammEntEnableTrapSupport_Type())
oammEntEnableTrapSupport.setMaxAccess(_C)
if mibBuilder.loadTexts:oammEntEnableTrapSupport.setStatus(_A)
class _OammEntFriBufferPoolSize_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,200))
_OammEntFriBufferPoolSize_Type.__name__=_F
_OammEntFriBufferPoolSize_Object=MibTableColumn
oammEntFriBufferPoolSize=_OammEntFriBufferPoolSize_Object((1,3,6,1,4,1,629,10,14,1,1,1,6),_OammEntFriBufferPoolSize_Type())
oammEntFriBufferPoolSize.setMaxAccess(_C)
if mibBuilder.loadTexts:oammEntFriBufferPoolSize.setStatus(_A)
class _OammEntRescheduleLimit_Type(Integer32):defaultValue=1000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_OammEntRescheduleLimit_Type.__name__=_F
_OammEntRescheduleLimit_Object=MibTableColumn
oammEntRescheduleLimit=_OammEntRescheduleLimit_Object((1,3,6,1,4,1,629,10,14,1,1,1,7),_OammEntRescheduleLimit_Type())
oammEntRescheduleLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:oammEntRescheduleLimit.setStatus(_A)
_OammMjTable_Object=MibTable
oammMjTable=_OammMjTable_Object((1,3,6,1,4,1,629,10,14,1,2))
if mibBuilder.loadTexts:oammMjTable.setStatus(_A)
_OammMjEntry_Object=MibTableRow
oammMjEntry=_OammMjEntry_Object((1,3,6,1,4,1,629,10,14,1,2,1))
oammMjEntry.setIndexNames((0,_B,_K),(0,_B,_L),(0,_B,_M),(0,_B,_N),(0,_B,_O))
if mibBuilder.loadTexts:oammMjEntry.setStatus(_A)
_OammMjApplIndex_Type=Unsigned32
_OammMjApplIndex_Object=MibTableColumn
oammMjApplIndex=_OammMjApplIndex_Object((1,3,6,1,4,1,629,10,14,1,2,1,1),_OammMjApplIndex_Type())
oammMjApplIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:oammMjApplIndex.setStatus(_A)
_OammMjInterfaceId_Type=OammMjIfId
_OammMjInterfaceId_Object=MibTableColumn
oammMjInterfaceId=_OammMjInterfaceId_Object((1,3,6,1,4,1,629,10,14,1,2,1,2),_OammMjInterfaceId_Type())
oammMjInterfaceId.setMaxAccess(_D)
if mibBuilder.loadTexts:oammMjInterfaceId.setStatus(_A)
_OammMjPartnerType_Type=Unsigned32
_OammMjPartnerType_Object=MibTableColumn
oammMjPartnerType=_OammMjPartnerType_Object((1,3,6,1,4,1,629,10,14,1,2,1,3),_OammMjPartnerType_Type())
oammMjPartnerType.setMaxAccess(_D)
if mibBuilder.loadTexts:oammMjPartnerType.setStatus(_A)
_OammMjPartnerIndex_Type=Unsigned32
_OammMjPartnerIndex_Object=MibTableColumn
oammMjPartnerIndex=_OammMjPartnerIndex_Object((1,3,6,1,4,1,629,10,14,1,2,1,4),_OammMjPartnerIndex_Type())
oammMjPartnerIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:oammMjPartnerIndex.setStatus(_A)
_OammMjSubIndex_Type=Unsigned32
_OammMjSubIndex_Object=MibTableColumn
oammMjSubIndex=_OammMjSubIndex_Object((1,3,6,1,4,1,629,10,14,1,2,1,5),_OammMjSubIndex_Type())
oammMjSubIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:oammMjSubIndex.setStatus(_A)
_OammMjRowStatus_Type=RowStatus
_OammMjRowStatus_Object=MibTableColumn
oammMjRowStatus=_OammMjRowStatus_Object((1,3,6,1,4,1,629,10,14,1,2,1,6),_OammMjRowStatus_Type())
oammMjRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:oammMjRowStatus.setStatus(_A)
class _OammMjAdminStatus_Type(AdminStatus):defaultValue=1
_OammMjAdminStatus_Type.__name__=_E
_OammMjAdminStatus_Object=MibTableColumn
oammMjAdminStatus=_OammMjAdminStatus_Object((1,3,6,1,4,1,629,10,14,1,2,1,7),_OammMjAdminStatus_Type())
oammMjAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:oammMjAdminStatus.setStatus(_A)
_OammMjOperStatus_Type=OperStatus
_OammMjOperStatus_Object=MibTableColumn
oammMjOperStatus=_OammMjOperStatus_Object((1,3,6,1,4,1,629,10,14,1,2,1,8),_OammMjOperStatus_Type())
oammMjOperStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:oammMjOperStatus.setStatus(_A)
_OammMjJoinStatus_Type=MjStatus
_OammMjJoinStatus_Object=MibTableColumn
oammMjJoinStatus=_OammMjJoinStatus_Object((1,3,6,1,4,1,629,10,14,1,2,1,9),_OammMjJoinStatus_Type())
oammMjJoinStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:oammMjJoinStatus.setStatus(_A)
_OammConformance_ObjectIdentity=ObjectIdentity
oammConformance=_OammConformance_ObjectIdentity((1,3,6,1,4,1,629,10,14,2))
_OammGroups_ObjectIdentity=ObjectIdentity
oammGroups=_OammGroups_ObjectIdentity((1,3,6,1,4,1,629,10,14,2,1))
_OammCompliances_ObjectIdentity=ObjectIdentity
oammCompliances=_OammCompliances_ObjectIdentity((1,3,6,1,4,1,629,10,14,2,2))
oammGeneralGroup=ObjectGroup((1,3,6,1,4,1,629,10,14,2,1,1))
oammGeneralGroup.setObjects(*((_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y)))
if mibBuilder.loadTexts:oammGeneralGroup.setStatus(_A)
oammModuleFullCompliance=ModuleCompliance((1,3,6,1,4,1,629,10,14,2,2,1))
oammModuleFullCompliance.setObjects((_B,_H))
if mibBuilder.loadTexts:oammModuleFullCompliance.setStatus(_A)
oammModuleReadOnlyCompliance=ModuleCompliance((1,3,6,1,4,1,629,10,14,2,2,2))
oammModuleReadOnlyCompliance.setObjects((_B,_H))
if mibBuilder.loadTexts:oammModuleReadOnlyCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'OammMjIfId':OammMjIfId,'nbase':nbase,'opx':opx,'oammMib':oammMib,'oammObjects':oammObjects,'oammEntTable':oammEntTable,'oammEntEntry':oammEntEntry,_J:oammEntApplIndex,_P:oammEntRowStatus,_Q:oammEntAdminStatus,_R:oammEntOperStatus,_S:oammEntEnableTrapSupport,_T:oammEntFriBufferPoolSize,_U:oammEntRescheduleLimit,'oammMjTable':oammMjTable,'oammMjEntry':oammMjEntry,_K:oammMjApplIndex,_L:oammMjInterfaceId,_M:oammMjPartnerType,_N:oammMjPartnerIndex,_O:oammMjSubIndex,_V:oammMjRowStatus,_W:oammMjAdminStatus,_X:oammMjOperStatus,_Y:oammMjJoinStatus,'oammConformance':oammConformance,'oammGroups':oammGroups,_H:oammGeneralGroup,'oammCompliances':oammCompliances,'oammModuleFullCompliance':oammModuleFullCompliance,'oammModuleReadOnlyCompliance':oammModuleReadOnlyCompliance})