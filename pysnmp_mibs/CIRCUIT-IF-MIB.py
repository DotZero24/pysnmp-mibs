_T='ciStatsGroup'
_S='ciIfMapGroup'
_R='ciCircuitGroup'
_Q='ciIfNumActive'
_P='ciIfLastChange'
_O='ciIfMapFlow'
_N='ciIfMapObject'
_M='ciCircuitStorageType'
_L='ciCircuitCreateTime'
_K='ciCircuitIfIndex'
_J='ciCircuitStatus'
_I='read-create'
_H='not-accessible'
_G='ciCircuitFlow'
_F='ciCircuitObject'
_E='ifIndex'
_D='IF-MIB'
_C='read-only'
_B='CIRCUIT-IF-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,ifIndex=mibBuilder.importSymbols(_D,'InterfaceIndex',_E)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','mib-2')
DisplayString,PhysAddress,RowPointer,RowStatus,StorageType,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowPointer','RowStatus','StorageType','TextualConvention','TimeStamp')
circuitIfMIB=ModuleIdentity((1,3,6,1,2,1,94))
if mibBuilder.loadTexts:circuitIfMIB.setRevisions(('2002-01-03 00:00',))
class CiFlowDirection(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('transmit',1),('receive',2),('both',3)))
_CiObjects_ObjectIdentity=ObjectIdentity
ciObjects=_CiObjects_ObjectIdentity((1,3,6,1,2,1,94,1))
_CiCircuitTable_Object=MibTable
ciCircuitTable=_CiCircuitTable_Object((1,3,6,1,2,1,94,1,1))
if mibBuilder.loadTexts:ciCircuitTable.setStatus(_A)
_CiCircuitEntry_Object=MibTableRow
ciCircuitEntry=_CiCircuitEntry_Object((1,3,6,1,2,1,94,1,1,1))
ciCircuitEntry.setIndexNames((0,_B,_F),(0,_B,_G))
if mibBuilder.loadTexts:ciCircuitEntry.setStatus(_A)
_CiCircuitObject_Type=RowPointer
_CiCircuitObject_Object=MibTableColumn
ciCircuitObject=_CiCircuitObject_Object((1,3,6,1,2,1,94,1,1,1,1),_CiCircuitObject_Type())
ciCircuitObject.setMaxAccess(_H)
if mibBuilder.loadTexts:ciCircuitObject.setStatus(_A)
_CiCircuitFlow_Type=CiFlowDirection
_CiCircuitFlow_Object=MibTableColumn
ciCircuitFlow=_CiCircuitFlow_Object((1,3,6,1,2,1,94,1,1,1,2),_CiCircuitFlow_Type())
ciCircuitFlow.setMaxAccess(_H)
if mibBuilder.loadTexts:ciCircuitFlow.setStatus(_A)
_CiCircuitStatus_Type=RowStatus
_CiCircuitStatus_Object=MibTableColumn
ciCircuitStatus=_CiCircuitStatus_Object((1,3,6,1,2,1,94,1,1,1,3),_CiCircuitStatus_Type())
ciCircuitStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:ciCircuitStatus.setStatus(_A)
_CiCircuitIfIndex_Type=InterfaceIndex
_CiCircuitIfIndex_Object=MibTableColumn
ciCircuitIfIndex=_CiCircuitIfIndex_Object((1,3,6,1,2,1,94,1,1,1,4),_CiCircuitIfIndex_Type())
ciCircuitIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ciCircuitIfIndex.setStatus(_A)
_CiCircuitCreateTime_Type=TimeStamp
_CiCircuitCreateTime_Object=MibTableColumn
ciCircuitCreateTime=_CiCircuitCreateTime_Object((1,3,6,1,2,1,94,1,1,1,5),_CiCircuitCreateTime_Type())
ciCircuitCreateTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ciCircuitCreateTime.setStatus(_A)
_CiCircuitStorageType_Type=StorageType
_CiCircuitStorageType_Object=MibTableColumn
ciCircuitStorageType=_CiCircuitStorageType_Object((1,3,6,1,2,1,94,1,1,1,6),_CiCircuitStorageType_Type())
ciCircuitStorageType.setMaxAccess(_I)
if mibBuilder.loadTexts:ciCircuitStorageType.setStatus(_A)
_CiIfMapTable_Object=MibTable
ciIfMapTable=_CiIfMapTable_Object((1,3,6,1,2,1,94,1,2))
if mibBuilder.loadTexts:ciIfMapTable.setStatus(_A)
_CiIfMapEntry_Object=MibTableRow
ciIfMapEntry=_CiIfMapEntry_Object((1,3,6,1,2,1,94,1,2,1))
ciIfMapEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:ciIfMapEntry.setStatus(_A)
_CiIfMapObject_Type=RowPointer
_CiIfMapObject_Object=MibTableColumn
ciIfMapObject=_CiIfMapObject_Object((1,3,6,1,2,1,94,1,2,1,1),_CiIfMapObject_Type())
ciIfMapObject.setMaxAccess(_C)
if mibBuilder.loadTexts:ciIfMapObject.setStatus(_A)
_CiIfMapFlow_Type=CiFlowDirection
_CiIfMapFlow_Object=MibTableColumn
ciIfMapFlow=_CiIfMapFlow_Object((1,3,6,1,2,1,94,1,2,1,2),_CiIfMapFlow_Type())
ciIfMapFlow.setMaxAccess(_C)
if mibBuilder.loadTexts:ciIfMapFlow.setStatus(_A)
_CiIfLastChange_Type=TimeStamp
_CiIfLastChange_Object=MibScalar
ciIfLastChange=_CiIfLastChange_Object((1,3,6,1,2,1,94,1,3),_CiIfLastChange_Type())
ciIfLastChange.setMaxAccess(_C)
if mibBuilder.loadTexts:ciIfLastChange.setStatus(_A)
_CiIfNumActive_Type=Gauge32
_CiIfNumActive_Object=MibScalar
ciIfNumActive=_CiIfNumActive_Object((1,3,6,1,2,1,94,1,4),_CiIfNumActive_Type())
ciIfNumActive.setMaxAccess(_C)
if mibBuilder.loadTexts:ciIfNumActive.setStatus(_A)
_CiCapabilities_ObjectIdentity=ObjectIdentity
ciCapabilities=_CiCapabilities_ObjectIdentity((1,3,6,1,2,1,94,2))
_CiConformance_ObjectIdentity=ObjectIdentity
ciConformance=_CiConformance_ObjectIdentity((1,3,6,1,2,1,94,3))
_CiMIBGroups_ObjectIdentity=ObjectIdentity
ciMIBGroups=_CiMIBGroups_ObjectIdentity((1,3,6,1,2,1,94,3,1))
_CiMIBCompliances_ObjectIdentity=ObjectIdentity
ciMIBCompliances=_CiMIBCompliances_ObjectIdentity((1,3,6,1,2,1,94,3,2))
ciCircuitGroup=ObjectGroup((1,3,6,1,2,1,94,3,1,1))
ciCircuitGroup.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M)))
if mibBuilder.loadTexts:ciCircuitGroup.setStatus(_A)
ciIfMapGroup=ObjectGroup((1,3,6,1,2,1,94,3,1,2))
ciIfMapGroup.setObjects(*((_B,_N),(_B,_O)))
if mibBuilder.loadTexts:ciIfMapGroup.setStatus(_A)
ciStatsGroup=ObjectGroup((1,3,6,1,2,1,94,3,1,3))
ciStatsGroup.setObjects(*((_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:ciStatsGroup.setStatus(_A)
ciCompliance=ModuleCompliance((1,3,6,1,2,1,94,3,2,1))
ciCompliance.setObjects(*((_B,_R),(_B,_S),(_B,_T)))
if mibBuilder.loadTexts:ciCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'CiFlowDirection':CiFlowDirection,'circuitIfMIB':circuitIfMIB,'ciObjects':ciObjects,'ciCircuitTable':ciCircuitTable,'ciCircuitEntry':ciCircuitEntry,_F:ciCircuitObject,_G:ciCircuitFlow,_J:ciCircuitStatus,_K:ciCircuitIfIndex,_L:ciCircuitCreateTime,_M:ciCircuitStorageType,'ciIfMapTable':ciIfMapTable,'ciIfMapEntry':ciIfMapEntry,_N:ciIfMapObject,_O:ciIfMapFlow,_P:ciIfLastChange,_Q:ciIfNumActive,'ciCapabilities':ciCapabilities,'ciConformance':ciConformance,'ciMIBGroups':ciMIBGroups,_R:ciCircuitGroup,_S:ciIfMapGroup,_T:ciStatsGroup,'ciMIBCompliances':ciMIBCompliances,'ciCompliance':ciCompliance})