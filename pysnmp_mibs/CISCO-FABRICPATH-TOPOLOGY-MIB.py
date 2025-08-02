_j='cfptTopologyTreeGroup'
_i='cfptTopologyIfVlanGroup'
_h='cfptTopologyIfGroup'
_g='cfptTopologyGroup'
_f='cfptTopologyTreeType'
_e='cfptTopologyTreeState'
_d='cfptTopologyTreeFtag'
_c='cfptTopologyIfActiveVlansSecond2K'
_b='cfptTopologyIfActiveVlansFirst2K'
_a='cfptTopologyIfVlansSecond2K'
_Z='cfptTopologyIfVlansFirst2K'
_Y='cfptTopologyIfRowStatus'
_X='cfptTopologyIfStorageType'
_W='cfptTopologyIfState'
_V='cfptTopologyRowStatus'
_U='cfptTopologyStorageType'
_T='cfptTopologyActiveVlansSecond2K'
_S='cfptTopologyActiveVlansFirst2K'
_R='cfptTopologyVlansSecond2K'
_Q='cfptTopologyVlansFirst2K'
_P='cfptTopologyStateChangeReason'
_O='cfptTopologyState'
_N='cfptTopologyDescr'
_M='cfptTopologyTreeId'
_L='cfptTopologyIfTopoIndex'
_K='not-accessible'
_J='cfptTopologyIndex'
_I='StorageType'
_H='ifIndex'
_G='IF-MIB'
_F='other'
_E='Integer32'
_D='read-create'
_C='read-only'
_B='CISCO-FABRICPATH-TOPOLOGY-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
Cisco2KVlanList,=mibBuilder.importSymbols('CISCO-TC','Cisco2KVlanList')
ifIndex,=mibBuilder.importSymbols(_G,_H)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus',_I,'TextualConvention')
ciscoFabricPathTopologyMIB=ModuleIdentity((1,3,6,1,4,1,9,9,801))
if mibBuilder.loadTexts:ciscoFabricPathTopologyMIB.setRevisions(('2013-03-11 00:00',))
_CiscoFabricPathTopologyMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoFabricPathTopologyMIBNotifs=_CiscoFabricPathTopologyMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,801,0))
_CiscoFabricPathTopologyMIBObjects_ObjectIdentity=ObjectIdentity
ciscoFabricPathTopologyMIBObjects=_CiscoFabricPathTopologyMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,801,1))
_CfptTopologyTable_Object=MibTable
cfptTopologyTable=_CfptTopologyTable_Object((1,3,6,1,4,1,9,9,801,1,1))
if mibBuilder.loadTexts:cfptTopologyTable.setStatus(_A)
_CfptTopologyEntry_Object=MibTableRow
cfptTopologyEntry=_CfptTopologyEntry_Object((1,3,6,1,4,1,9,9,801,1,1,1))
cfptTopologyEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:cfptTopologyEntry.setStatus(_A)
_CfptTopologyIndex_Type=Unsigned32
_CfptTopologyIndex_Object=MibTableColumn
cfptTopologyIndex=_CfptTopologyIndex_Object((1,3,6,1,4,1,9,9,801,1,1,1,1),_CfptTopologyIndex_Type())
cfptTopologyIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:cfptTopologyIndex.setStatus(_A)
_CfptTopologyDescr_Type=SnmpAdminString
_CfptTopologyDescr_Object=MibTableColumn
cfptTopologyDescr=_CfptTopologyDescr_Object((1,3,6,1,4,1,9,9,801,1,1,1,2),_CfptTopologyDescr_Type())
cfptTopologyDescr.setMaxAccess(_D)
if mibBuilder.loadTexts:cfptTopologyDescr.setStatus(_A)
class _CfptTopologyState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),('up',2),('down',3)))
_CfptTopologyState_Type.__name__=_E
_CfptTopologyState_Object=MibTableColumn
cfptTopologyState=_CfptTopologyState_Object((1,3,6,1,4,1,9,9,801,1,1,1,3),_CfptTopologyState_Type())
cfptTopologyState.setMaxAccess(_C)
if mibBuilder.loadTexts:cfptTopologyState.setStatus(_A)
_CfptTopologyStateChangeReason_Type=SnmpAdminString
_CfptTopologyStateChangeReason_Object=MibTableColumn
cfptTopologyStateChangeReason=_CfptTopologyStateChangeReason_Object((1,3,6,1,4,1,9,9,801,1,1,1,4),_CfptTopologyStateChangeReason_Type())
cfptTopologyStateChangeReason.setMaxAccess(_C)
if mibBuilder.loadTexts:cfptTopologyStateChangeReason.setStatus(_A)
_CfptTopologyVlansFirst2K_Type=Cisco2KVlanList
_CfptTopologyVlansFirst2K_Object=MibTableColumn
cfptTopologyVlansFirst2K=_CfptTopologyVlansFirst2K_Object((1,3,6,1,4,1,9,9,801,1,1,1,5),_CfptTopologyVlansFirst2K_Type())
cfptTopologyVlansFirst2K.setMaxAccess(_D)
if mibBuilder.loadTexts:cfptTopologyVlansFirst2K.setStatus(_A)
_CfptTopologyVlansSecond2K_Type=Cisco2KVlanList
_CfptTopologyVlansSecond2K_Object=MibTableColumn
cfptTopologyVlansSecond2K=_CfptTopologyVlansSecond2K_Object((1,3,6,1,4,1,9,9,801,1,1,1,6),_CfptTopologyVlansSecond2K_Type())
cfptTopologyVlansSecond2K.setMaxAccess(_D)
if mibBuilder.loadTexts:cfptTopologyVlansSecond2K.setStatus(_A)
_CfptTopologyActiveVlansFirst2K_Type=Cisco2KVlanList
_CfptTopologyActiveVlansFirst2K_Object=MibTableColumn
cfptTopologyActiveVlansFirst2K=_CfptTopologyActiveVlansFirst2K_Object((1,3,6,1,4,1,9,9,801,1,1,1,7),_CfptTopologyActiveVlansFirst2K_Type())
cfptTopologyActiveVlansFirst2K.setMaxAccess(_C)
if mibBuilder.loadTexts:cfptTopologyActiveVlansFirst2K.setStatus(_A)
_CfptTopologyActiveVlansSecond2K_Type=Cisco2KVlanList
_CfptTopologyActiveVlansSecond2K_Object=MibTableColumn
cfptTopologyActiveVlansSecond2K=_CfptTopologyActiveVlansSecond2K_Object((1,3,6,1,4,1,9,9,801,1,1,1,8),_CfptTopologyActiveVlansSecond2K_Type())
cfptTopologyActiveVlansSecond2K.setMaxAccess(_C)
if mibBuilder.loadTexts:cfptTopologyActiveVlansSecond2K.setStatus(_A)
class _CfptTopologyStorageType_Type(StorageType):defaultValue=2
_CfptTopologyStorageType_Type.__name__=_I
_CfptTopologyStorageType_Object=MibTableColumn
cfptTopologyStorageType=_CfptTopologyStorageType_Object((1,3,6,1,4,1,9,9,801,1,1,1,9),_CfptTopologyStorageType_Type())
cfptTopologyStorageType.setMaxAccess(_D)
if mibBuilder.loadTexts:cfptTopologyStorageType.setStatus(_A)
_CfptTopologyRowStatus_Type=RowStatus
_CfptTopologyRowStatus_Object=MibTableColumn
cfptTopologyRowStatus=_CfptTopologyRowStatus_Object((1,3,6,1,4,1,9,9,801,1,1,1,10),_CfptTopologyRowStatus_Type())
cfptTopologyRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:cfptTopologyRowStatus.setStatus(_A)
_CfptTopologyIfTable_Object=MibTable
cfptTopologyIfTable=_CfptTopologyIfTable_Object((1,3,6,1,4,1,9,9,801,1,2))
if mibBuilder.loadTexts:cfptTopologyIfTable.setStatus(_A)
_CfptTopologyIfEntry_Object=MibTableRow
cfptTopologyIfEntry=_CfptTopologyIfEntry_Object((1,3,6,1,4,1,9,9,801,1,2,1))
cfptTopologyIfEntry.setIndexNames((0,_B,_L),(0,_G,_H))
if mibBuilder.loadTexts:cfptTopologyIfEntry.setStatus(_A)
_CfptTopologyIfTopoIndex_Type=Unsigned32
_CfptTopologyIfTopoIndex_Object=MibTableColumn
cfptTopologyIfTopoIndex=_CfptTopologyIfTopoIndex_Object((1,3,6,1,4,1,9,9,801,1,2,1,1),_CfptTopologyIfTopoIndex_Type())
cfptTopologyIfTopoIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:cfptTopologyIfTopoIndex.setStatus(_A)
class _CfptTopologyIfState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),('up',2),('down',3)))
_CfptTopologyIfState_Type.__name__=_E
_CfptTopologyIfState_Object=MibTableColumn
cfptTopologyIfState=_CfptTopologyIfState_Object((1,3,6,1,4,1,9,9,801,1,2,1,2),_CfptTopologyIfState_Type())
cfptTopologyIfState.setMaxAccess(_C)
if mibBuilder.loadTexts:cfptTopologyIfState.setStatus(_A)
class _CfptTopologyIfStorageType_Type(StorageType):defaultValue=2
_CfptTopologyIfStorageType_Type.__name__=_I
_CfptTopologyIfStorageType_Object=MibTableColumn
cfptTopologyIfStorageType=_CfptTopologyIfStorageType_Object((1,3,6,1,4,1,9,9,801,1,2,1,3),_CfptTopologyIfStorageType_Type())
cfptTopologyIfStorageType.setMaxAccess(_D)
if mibBuilder.loadTexts:cfptTopologyIfStorageType.setStatus(_A)
_CfptTopologyIfRowStatus_Type=RowStatus
_CfptTopologyIfRowStatus_Object=MibTableColumn
cfptTopologyIfRowStatus=_CfptTopologyIfRowStatus_Object((1,3,6,1,4,1,9,9,801,1,2,1,4),_CfptTopologyIfRowStatus_Type())
cfptTopologyIfRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:cfptTopologyIfRowStatus.setStatus(_A)
_CfptTopologyIfVlanTable_Object=MibTable
cfptTopologyIfVlanTable=_CfptTopologyIfVlanTable_Object((1,3,6,1,4,1,9,9,801,1,3))
if mibBuilder.loadTexts:cfptTopologyIfVlanTable.setStatus(_A)
_CfptTopologyIfVlanEntry_Object=MibTableRow
cfptTopologyIfVlanEntry=_CfptTopologyIfVlanEntry_Object((1,3,6,1,4,1,9,9,801,1,3,1))
cfptTopologyIfVlanEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:cfptTopologyIfVlanEntry.setStatus(_A)
_CfptTopologyIfVlansFirst2K_Type=Cisco2KVlanList
_CfptTopologyIfVlansFirst2K_Object=MibTableColumn
cfptTopologyIfVlansFirst2K=_CfptTopologyIfVlansFirst2K_Object((1,3,6,1,4,1,9,9,801,1,3,1,1),_CfptTopologyIfVlansFirst2K_Type())
cfptTopologyIfVlansFirst2K.setMaxAccess(_C)
if mibBuilder.loadTexts:cfptTopologyIfVlansFirst2K.setStatus(_A)
_CfptTopologyIfVlansSecond2K_Type=Cisco2KVlanList
_CfptTopologyIfVlansSecond2K_Object=MibTableColumn
cfptTopologyIfVlansSecond2K=_CfptTopologyIfVlansSecond2K_Object((1,3,6,1,4,1,9,9,801,1,3,1,2),_CfptTopologyIfVlansSecond2K_Type())
cfptTopologyIfVlansSecond2K.setMaxAccess(_C)
if mibBuilder.loadTexts:cfptTopologyIfVlansSecond2K.setStatus(_A)
_CfptTopologyIfActiveVlansFirst2K_Type=Cisco2KVlanList
_CfptTopologyIfActiveVlansFirst2K_Object=MibTableColumn
cfptTopologyIfActiveVlansFirst2K=_CfptTopologyIfActiveVlansFirst2K_Object((1,3,6,1,4,1,9,9,801,1,3,1,3),_CfptTopologyIfActiveVlansFirst2K_Type())
cfptTopologyIfActiveVlansFirst2K.setMaxAccess(_C)
if mibBuilder.loadTexts:cfptTopologyIfActiveVlansFirst2K.setStatus(_A)
_CfptTopologyIfActiveVlansSecond2K_Type=Cisco2KVlanList
_CfptTopologyIfActiveVlansSecond2K_Object=MibTableColumn
cfptTopologyIfActiveVlansSecond2K=_CfptTopologyIfActiveVlansSecond2K_Object((1,3,6,1,4,1,9,9,801,1,3,1,4),_CfptTopologyIfActiveVlansSecond2K_Type())
cfptTopologyIfActiveVlansSecond2K.setMaxAccess(_C)
if mibBuilder.loadTexts:cfptTopologyIfActiveVlansSecond2K.setStatus(_A)
_CfptTopologyTreeTable_Object=MibTable
cfptTopologyTreeTable=_CfptTopologyTreeTable_Object((1,3,6,1,4,1,9,9,801,1,4))
if mibBuilder.loadTexts:cfptTopologyTreeTable.setStatus(_A)
_CfptTopologyTreeEntry_Object=MibTableRow
cfptTopologyTreeEntry=_CfptTopologyTreeEntry_Object((1,3,6,1,4,1,9,9,801,1,4,1))
cfptTopologyTreeEntry.setIndexNames((0,_B,_J),(0,_B,_M))
if mibBuilder.loadTexts:cfptTopologyTreeEntry.setStatus(_A)
_CfptTopologyTreeId_Type=Unsigned32
_CfptTopologyTreeId_Object=MibTableColumn
cfptTopologyTreeId=_CfptTopologyTreeId_Object((1,3,6,1,4,1,9,9,801,1,4,1,1),_CfptTopologyTreeId_Type())
cfptTopologyTreeId.setMaxAccess(_K)
if mibBuilder.loadTexts:cfptTopologyTreeId.setStatus(_A)
_CfptTopologyTreeFtag_Type=Unsigned32
_CfptTopologyTreeFtag_Object=MibTableColumn
cfptTopologyTreeFtag=_CfptTopologyTreeFtag_Object((1,3,6,1,4,1,9,9,801,1,4,1,2),_CfptTopologyTreeFtag_Type())
cfptTopologyTreeFtag.setMaxAccess(_C)
if mibBuilder.loadTexts:cfptTopologyTreeFtag.setStatus(_A)
class _CfptTopologyTreeState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),('active',2),('inactive',3)))
_CfptTopologyTreeState_Type.__name__=_E
_CfptTopologyTreeState_Object=MibTableColumn
cfptTopologyTreeState=_CfptTopologyTreeState_Object((1,3,6,1,4,1,9,9,801,1,4,1,3),_CfptTopologyTreeState_Type())
cfptTopologyTreeState.setMaxAccess(_C)
if mibBuilder.loadTexts:cfptTopologyTreeState.setStatus(_A)
class _CfptTopologyTreeType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),('mixed',2),('multicast',3)))
_CfptTopologyTreeType_Type.__name__=_E
_CfptTopologyTreeType_Object=MibTableColumn
cfptTopologyTreeType=_CfptTopologyTreeType_Object((1,3,6,1,4,1,9,9,801,1,4,1,4),_CfptTopologyTreeType_Type())
cfptTopologyTreeType.setMaxAccess(_C)
if mibBuilder.loadTexts:cfptTopologyTreeType.setStatus(_A)
_CiscoFabricPathTopologyMIBConformance_ObjectIdentity=ObjectIdentity
ciscoFabricPathTopologyMIBConformance=_CiscoFabricPathTopologyMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,801,2))
_CfptFabricPathTopologyMIBCompliances_ObjectIdentity=ObjectIdentity
cfptFabricPathTopologyMIBCompliances=_CfptFabricPathTopologyMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,801,2,1))
_CfptFabricPathTopologyMIBGroups_ObjectIdentity=ObjectIdentity
cfptFabricPathTopologyMIBGroups=_CfptFabricPathTopologyMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,801,2,2))
cfptTopologyGroup=ObjectGroup((1,3,6,1,4,1,9,9,801,2,2,1))
cfptTopologyGroup.setObjects(*((_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V)))
if mibBuilder.loadTexts:cfptTopologyGroup.setStatus(_A)
cfptTopologyIfGroup=ObjectGroup((1,3,6,1,4,1,9,9,801,2,2,2))
cfptTopologyIfGroup.setObjects(*((_B,_W),(_B,_X),(_B,_Y)))
if mibBuilder.loadTexts:cfptTopologyIfGroup.setStatus(_A)
cfptTopologyIfVlanGroup=ObjectGroup((1,3,6,1,4,1,9,9,801,2,2,3))
cfptTopologyIfVlanGroup.setObjects(*((_B,_Z),(_B,_a),(_B,_b),(_B,_c)))
if mibBuilder.loadTexts:cfptTopologyIfVlanGroup.setStatus(_A)
cfptTopologyTreeGroup=ObjectGroup((1,3,6,1,4,1,9,9,801,2,2,4))
cfptTopologyTreeGroup.setObjects(*((_B,_d),(_B,_e),(_B,_f)))
if mibBuilder.loadTexts:cfptTopologyTreeGroup.setStatus(_A)
cfptFabricPathTopologyMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,801,2,1,1))
cfptFabricPathTopologyMIBCompliance.setObjects(*((_B,_g),(_B,_h),(_B,_i),(_B,_j)))
if mibBuilder.loadTexts:cfptFabricPathTopologyMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoFabricPathTopologyMIB':ciscoFabricPathTopologyMIB,'ciscoFabricPathTopologyMIBNotifs':ciscoFabricPathTopologyMIBNotifs,'ciscoFabricPathTopologyMIBObjects':ciscoFabricPathTopologyMIBObjects,'cfptTopologyTable':cfptTopologyTable,'cfptTopologyEntry':cfptTopologyEntry,_J:cfptTopologyIndex,_N:cfptTopologyDescr,_O:cfptTopologyState,_P:cfptTopologyStateChangeReason,_Q:cfptTopologyVlansFirst2K,_R:cfptTopologyVlansSecond2K,_S:cfptTopologyActiveVlansFirst2K,_T:cfptTopologyActiveVlansSecond2K,_U:cfptTopologyStorageType,_V:cfptTopologyRowStatus,'cfptTopologyIfTable':cfptTopologyIfTable,'cfptTopologyIfEntry':cfptTopologyIfEntry,_L:cfptTopologyIfTopoIndex,_W:cfptTopologyIfState,_X:cfptTopologyIfStorageType,_Y:cfptTopologyIfRowStatus,'cfptTopologyIfVlanTable':cfptTopologyIfVlanTable,'cfptTopologyIfVlanEntry':cfptTopologyIfVlanEntry,_Z:cfptTopologyIfVlansFirst2K,_a:cfptTopologyIfVlansSecond2K,_b:cfptTopologyIfActiveVlansFirst2K,_c:cfptTopologyIfActiveVlansSecond2K,'cfptTopologyTreeTable':cfptTopologyTreeTable,'cfptTopologyTreeEntry':cfptTopologyTreeEntry,_M:cfptTopologyTreeId,_d:cfptTopologyTreeFtag,_e:cfptTopologyTreeState,_f:cfptTopologyTreeType,'ciscoFabricPathTopologyMIBConformance':ciscoFabricPathTopologyMIBConformance,'cfptFabricPathTopologyMIBCompliances':cfptFabricPathTopologyMIBCompliances,'cfptFabricPathTopologyMIBCompliance':cfptFabricPathTopologyMIBCompliance,'cfptFabricPathTopologyMIBGroups':cfptFabricPathTopologyMIBGroups,_g:cfptTopologyGroup,_h:cfptTopologyIfGroup,_i:cfptTopologyIfVlanGroup,_j:cfptTopologyTreeGroup})