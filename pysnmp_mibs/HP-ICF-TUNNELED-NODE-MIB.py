_l='hpicfTunneledNodeGroup4'
_k='hpicfTunneledNodeGroup3'
_j='hpicfTunneledNodeGroup2'
_i='hpicfTunneledNodeGroup1'
_h='hpicfTunneledNodeGroup'
_g='hpicfTunneledNodeWolVIDList'
_f='hpicfTunneledNodePapiRowStatus'
_e='hpicfTunneledNodePapiKeyEncr'
_d='hpicfTunneledNodePapiKeyValue'
_c='hpicfTunneledNodeFallbackLclSw'
_b='hpicfTunneledNodePortRowStatus'
_a='hpicfTunneledNodePapiAuthMode'
_Z='not-accessible'
_Y='hpicfTunneledNodeIndex'
_X='TruthValue'
_W='Unsigned32'
_V='ifIndex'
_U='IF-MIB'
_T='hpicfTunneledNodeMPeriod'
_S='OctetString'
_R='hpicfTunneledNodeReservedVlanId'
_Q='hpicfTunneledNodeVlanMode'
_P='hpicfTunneledNodeMode'
_O='Integer32'
_N='hpicfTunneledNodePapiGroup'
_M='hpicfTunneledNodePortGroup'
_L='hpicfTunneledNodeClearStats'
_K='hpicfTunneledNodeRowStatus'
_J='hpicfTunneledNodeTimeout'
_I='hpicfTunneledNodeBackupAddr'
_H='hpicfTunneledNodeBackupAddrType'
_G='hpicfTunneledNodePrimaryAddr'
_F='hpicfTunneledNodePrimaryAddrType'
_E='hpicfTunneledNodeEnable'
_D='deprecated'
_C='read-create'
_B='current'
_A='HP-ICF-TUNNELED-NODE-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_S,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpSwitch,=mibBuilder.importSymbols('HP-ICF-OID','hpSwitch')
VidList,=mibBuilder.importSymbols('HP-ICF-TC','VidList')
ifIndex,=mibBuilder.importSymbols(_U,_V)
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
VlanIndex,=mibBuilder.importSymbols('Q-BRIDGE-MIB','VlanIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_O,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_W,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_X)
hpicfTunneledNode=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,5,1,128))
if mibBuilder.loadTexts:hpicfTunneledNode.setRevisions(('2021-06-12 00:00','2018-05-23 00:00','2018-05-22 00:00','2016-12-06 00:00','2016-08-05 00:00','2016-02-11 00:00'))
_HpicfTunneledNodeObjects_ObjectIdentity=ObjectIdentity
hpicfTunneledNodeObjects=_HpicfTunneledNodeObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,128,1))
_HpicfTunneledNodeConfig_ObjectIdentity=ObjectIdentity
hpicfTunneledNodeConfig=_HpicfTunneledNodeConfig_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,128,1,1))
_HpicfTunneledNodeTable_Object=MibTable
hpicfTunneledNodeTable=_HpicfTunneledNodeTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,128,1,1,1))
if mibBuilder.loadTexts:hpicfTunneledNodeTable.setStatus(_B)
_HpicfTunneledNodeEntry_Object=MibTableRow
hpicfTunneledNodeEntry=_HpicfTunneledNodeEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,128,1,1,1,1))
hpicfTunneledNodeEntry.setIndexNames((0,_A,_Y))
if mibBuilder.loadTexts:hpicfTunneledNodeEntry.setStatus(_B)
_HpicfTunneledNodeIndex_Type=Unsigned32
_HpicfTunneledNodeIndex_Object=MibTableColumn
hpicfTunneledNodeIndex=_HpicfTunneledNodeIndex_Object((1,3,6,1,4,1,11,2,14,11,5,1,128,1,1,1,1,1),_HpicfTunneledNodeIndex_Type())
hpicfTunneledNodeIndex.setMaxAccess(_Z)
if mibBuilder.loadTexts:hpicfTunneledNodeIndex.setStatus(_B)
_HpicfTunneledNodeEnable_Type=TruthValue
_HpicfTunneledNodeEnable_Object=MibTableColumn
hpicfTunneledNodeEnable=_HpicfTunneledNodeEnable_Object((1,3,6,1,4,1,11,2,14,11,5,1,128,1,1,1,1,2),_HpicfTunneledNodeEnable_Type())
hpicfTunneledNodeEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfTunneledNodeEnable.setStatus(_B)
_HpicfTunneledNodePrimaryAddrType_Type=InetAddressType
_HpicfTunneledNodePrimaryAddrType_Object=MibTableColumn
hpicfTunneledNodePrimaryAddrType=_HpicfTunneledNodePrimaryAddrType_Object((1,3,6,1,4,1,11,2,14,11,5,1,128,1,1,1,1,3),_HpicfTunneledNodePrimaryAddrType_Type())
hpicfTunneledNodePrimaryAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfTunneledNodePrimaryAddrType.setStatus(_B)
_HpicfTunneledNodePrimaryAddr_Type=InetAddress
_HpicfTunneledNodePrimaryAddr_Object=MibTableColumn
hpicfTunneledNodePrimaryAddr=_HpicfTunneledNodePrimaryAddr_Object((1,3,6,1,4,1,11,2,14,11,5,1,128,1,1,1,1,4),_HpicfTunneledNodePrimaryAddr_Type())
hpicfTunneledNodePrimaryAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfTunneledNodePrimaryAddr.setStatus(_B)
_HpicfTunneledNodeBackupAddrType_Type=InetAddressType
_HpicfTunneledNodeBackupAddrType_Object=MibTableColumn
hpicfTunneledNodeBackupAddrType=_HpicfTunneledNodeBackupAddrType_Object((1,3,6,1,4,1,11,2,14,11,5,1,128,1,1,1,1,5),_HpicfTunneledNodeBackupAddrType_Type())
hpicfTunneledNodeBackupAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfTunneledNodeBackupAddrType.setStatus(_B)
_HpicfTunneledNodeBackupAddr_Type=InetAddress
_HpicfTunneledNodeBackupAddr_Object=MibTableColumn
hpicfTunneledNodeBackupAddr=_HpicfTunneledNodeBackupAddr_Object((1,3,6,1,4,1,11,2,14,11,5,1,128,1,1,1,1,6),_HpicfTunneledNodeBackupAddr_Type())
hpicfTunneledNodeBackupAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfTunneledNodeBackupAddr.setStatus(_B)
class _HpicfTunneledNodeTimeout_Type(Unsigned32):defaultValue=8
_HpicfTunneledNodeTimeout_Type.__name__=_W
_HpicfTunneledNodeTimeout_Object=MibTableColumn
hpicfTunneledNodeTimeout=_HpicfTunneledNodeTimeout_Object((1,3,6,1,4,1,11,2,14,11,5,1,128,1,1,1,1,7),_HpicfTunneledNodeTimeout_Type())
hpicfTunneledNodeTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfTunneledNodeTimeout.setStatus(_B)
_HpicfTunneledNodeRowStatus_Type=RowStatus
_HpicfTunneledNodeRowStatus_Object=MibTableColumn
hpicfTunneledNodeRowStatus=_HpicfTunneledNodeRowStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,128,1,1,1,1,8),_HpicfTunneledNodeRowStatus_Type())
hpicfTunneledNodeRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfTunneledNodeRowStatus.setStatus(_B)
class _HpicfTunneledNodeMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('portbased',1),('rolebased',2)))
_HpicfTunneledNodeMode_Type.__name__=_O
_HpicfTunneledNodeMode_Object=MibTableColumn
hpicfTunneledNodeMode=_HpicfTunneledNodeMode_Object((1,3,6,1,4,1,11,2,14,11,5,1,128,1,1,1,1,9),_HpicfTunneledNodeMode_Type())
hpicfTunneledNodeMode.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfTunneledNodeMode.setStatus(_B)
class _HpicfTunneledNodeVlanMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('vlanextend',1),('novlan',2)))
_HpicfTunneledNodeVlanMode_Type.__name__=_O
_HpicfTunneledNodeVlanMode_Object=MibTableColumn
hpicfTunneledNodeVlanMode=_HpicfTunneledNodeVlanMode_Object((1,3,6,1,4,1,11,2,14,11,5,1,128,1,1,1,1,10),_HpicfTunneledNodeVlanMode_Type())
hpicfTunneledNodeVlanMode.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfTunneledNodeVlanMode.setStatus(_B)
_HpicfTunneledNodeReservedVlanId_Type=VlanIndex
_HpicfTunneledNodeReservedVlanId_Object=MibTableColumn
hpicfTunneledNodeReservedVlanId=_HpicfTunneledNodeReservedVlanId_Object((1,3,6,1,4,1,11,2,14,11,5,1,128,1,1,1,1,11),_HpicfTunneledNodeReservedVlanId_Type())
hpicfTunneledNodeReservedVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfTunneledNodeReservedVlanId.setStatus(_B)
class _HpicfTunneledNodeMPeriod_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,720))
_HpicfTunneledNodeMPeriod_Type.__name__=_O
_HpicfTunneledNodeMPeriod_Object=MibTableColumn
hpicfTunneledNodeMPeriod=_HpicfTunneledNodeMPeriod_Object((1,3,6,1,4,1,11,2,14,11,5,1,128,1,1,1,1,12),_HpicfTunneledNodeMPeriod_Type())
hpicfTunneledNodeMPeriod.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfTunneledNodeMPeriod.setStatus(_B)
if mibBuilder.loadTexts:hpicfTunneledNodeMPeriod.setUnits('hour')
_HpicfTunneledNodeWolVIDList_Type=VidList
_HpicfTunneledNodeWolVIDList_Object=MibTableColumn
hpicfTunneledNodeWolVIDList=_HpicfTunneledNodeWolVIDList_Object((1,3,6,1,4,1,11,2,14,11,5,1,128,1,1,1,1,13),_HpicfTunneledNodeWolVIDList_Type())
hpicfTunneledNodeWolVIDList.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfTunneledNodeWolVIDList.setStatus(_B)
_HpicfTunneledNodePortConfigTable_Object=MibTable
hpicfTunneledNodePortConfigTable=_HpicfTunneledNodePortConfigTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,128,1,1,2))
if mibBuilder.loadTexts:hpicfTunneledNodePortConfigTable.setStatus(_B)
_HpicfTunneledNodePortConfigEntry_Object=MibTableRow
hpicfTunneledNodePortConfigEntry=_HpicfTunneledNodePortConfigEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,128,1,1,2,1))
hpicfTunneledNodePortConfigEntry.setIndexNames((0,_U,_V))
if mibBuilder.loadTexts:hpicfTunneledNodePortConfigEntry.setStatus(_B)
_HpicfTunneledNodePortRowStatus_Type=RowStatus
_HpicfTunneledNodePortRowStatus_Object=MibTableColumn
hpicfTunneledNodePortRowStatus=_HpicfTunneledNodePortRowStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,128,1,1,2,1,1),_HpicfTunneledNodePortRowStatus_Type())
hpicfTunneledNodePortRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfTunneledNodePortRowStatus.setStatus(_B)
_HpicfTunneledNodeFallbackLclSw_Type=TruthValue
_HpicfTunneledNodeFallbackLclSw_Object=MibTableColumn
hpicfTunneledNodeFallbackLclSw=_HpicfTunneledNodeFallbackLclSw_Object((1,3,6,1,4,1,11,2,14,11,5,1,128,1,1,2,1,2),_HpicfTunneledNodeFallbackLclSw_Type())
hpicfTunneledNodeFallbackLclSw.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfTunneledNodeFallbackLclSw.setStatus(_B)
class _HpicfTunneledNodeClearStats_Type(TruthValue):defaultValue=2
_HpicfTunneledNodeClearStats_Type.__name__=_X
_HpicfTunneledNodeClearStats_Object=MibScalar
hpicfTunneledNodeClearStats=_HpicfTunneledNodeClearStats_Object((1,3,6,1,4,1,11,2,14,11,5,1,128,1,1,3),_HpicfTunneledNodeClearStats_Type())
hpicfTunneledNodeClearStats.setMaxAccess('read-write')
if mibBuilder.loadTexts:hpicfTunneledNodeClearStats.setStatus(_B)
_HpicfTunneledNodePapiTable_Object=MibTable
hpicfTunneledNodePapiTable=_HpicfTunneledNodePapiTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,128,1,1,4))
if mibBuilder.loadTexts:hpicfTunneledNodePapiTable.setStatus(_B)
_HpicfTunneledNodePapiEntry_Object=MibTableRow
hpicfTunneledNodePapiEntry=_HpicfTunneledNodePapiEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,128,1,1,4,1))
hpicfTunneledNodePapiEntry.setIndexNames((0,_A,_a))
if mibBuilder.loadTexts:hpicfTunneledNodePapiEntry.setStatus(_B)
class _HpicfTunneledNodePapiAuthMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('none',1),('md5',2)))
_HpicfTunneledNodePapiAuthMode_Type.__name__=_O
_HpicfTunneledNodePapiAuthMode_Object=MibTableColumn
hpicfTunneledNodePapiAuthMode=_HpicfTunneledNodePapiAuthMode_Object((1,3,6,1,4,1,11,2,14,11,5,1,128,1,1,4,1,1),_HpicfTunneledNodePapiAuthMode_Type())
hpicfTunneledNodePapiAuthMode.setMaxAccess(_Z)
if mibBuilder.loadTexts:hpicfTunneledNodePapiAuthMode.setStatus(_B)
class _HpicfTunneledNodePapiKeyValue_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_HpicfTunneledNodePapiKeyValue_Type.__name__=_S
_HpicfTunneledNodePapiKeyValue_Object=MibTableColumn
hpicfTunneledNodePapiKeyValue=_HpicfTunneledNodePapiKeyValue_Object((1,3,6,1,4,1,11,2,14,11,5,1,128,1,1,4,1,2),_HpicfTunneledNodePapiKeyValue_Type())
hpicfTunneledNodePapiKeyValue.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfTunneledNodePapiKeyValue.setStatus(_B)
class _HpicfTunneledNodePapiKeyEncr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_HpicfTunneledNodePapiKeyEncr_Type.__name__=_S
_HpicfTunneledNodePapiKeyEncr_Object=MibTableColumn
hpicfTunneledNodePapiKeyEncr=_HpicfTunneledNodePapiKeyEncr_Object((1,3,6,1,4,1,11,2,14,11,5,1,128,1,1,4,1,3),_HpicfTunneledNodePapiKeyEncr_Type())
hpicfTunneledNodePapiKeyEncr.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfTunneledNodePapiKeyEncr.setStatus(_B)
_HpicfTunneledNodePapiRowStatus_Type=RowStatus
_HpicfTunneledNodePapiRowStatus_Object=MibTableColumn
hpicfTunneledNodePapiRowStatus=_HpicfTunneledNodePapiRowStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,128,1,1,4,1,4),_HpicfTunneledNodePapiRowStatus_Type())
hpicfTunneledNodePapiRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfTunneledNodePapiRowStatus.setStatus(_B)
_HpicfTunneledNodeConformance_ObjectIdentity=ObjectIdentity
hpicfTunneledNodeConformance=_HpicfTunneledNodeConformance_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,128,2))
_HpicfTunneledNodeCompliances_ObjectIdentity=ObjectIdentity
hpicfTunneledNodeCompliances=_HpicfTunneledNodeCompliances_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,128,2,1))
_HpicfTunneledNodeGroups_ObjectIdentity=ObjectIdentity
hpicfTunneledNodeGroups=_HpicfTunneledNodeGroups_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,128,2,2))
hpicfTunneledNodeGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,128,2,2,1))
hpicfTunneledNodeGroup.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L)))
if mibBuilder.loadTexts:hpicfTunneledNodeGroup.setStatus(_D)
hpicfTunneledNodePortGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,128,2,2,2))
hpicfTunneledNodePortGroup.setObjects(*((_A,_b),(_A,_c)))
if mibBuilder.loadTexts:hpicfTunneledNodePortGroup.setStatus(_B)
hpicfTunneledNodePapiGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,128,2,2,3))
hpicfTunneledNodePapiGroup.setObjects(*((_A,_d),(_A,_e),(_A,_f)))
if mibBuilder.loadTexts:hpicfTunneledNodePapiGroup.setStatus(_B)
hpicfTunneledNodeGroup1=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,128,2,2,4))
hpicfTunneledNodeGroup1.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_P),(_A,_Q),(_A,_R)))
if mibBuilder.loadTexts:hpicfTunneledNodeGroup1.setStatus(_D)
hpicfTunneledNodeGroup2=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,128,2,2,5))
hpicfTunneledNodeGroup2.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_P),(_A,_Q),(_A,_R)))
if mibBuilder.loadTexts:hpicfTunneledNodeGroup2.setStatus(_D)
hpicfTunneledNodeGroup3=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,128,2,2,6))
hpicfTunneledNodeGroup3.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_P),(_A,_Q),(_A,_R),(_A,_T)))
if mibBuilder.loadTexts:hpicfTunneledNodeGroup3.setStatus(_D)
hpicfTunneledNodeGroup4=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,128,2,2,7))
hpicfTunneledNodeGroup4.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_P),(_A,_Q),(_A,_R),(_A,_T),(_A,_g)))
if mibBuilder.loadTexts:hpicfTunneledNodeGroup4.setStatus(_B)
hpicfTunneledNodeCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,128,2,1,1))
hpicfTunneledNodeCompliance.setObjects(*((_A,_h),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:hpicfTunneledNodeCompliance.setStatus(_D)
hpicfTunneledNodeCompliance1=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,128,2,1,2))
hpicfTunneledNodeCompliance1.setObjects(*((_A,_i),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:hpicfTunneledNodeCompliance1.setStatus(_D)
hpicfTunneledNodeCompliance2=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,128,2,1,3))
hpicfTunneledNodeCompliance2.setObjects(*((_A,_j),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:hpicfTunneledNodeCompliance2.setStatus(_D)
hpicfTunneledNodeCompliance3=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,128,2,1,4))
hpicfTunneledNodeCompliance3.setObjects(*((_A,_k),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:hpicfTunneledNodeCompliance3.setStatus(_D)
hpicfTunneledNodeCompliance4=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,128,2,1,5))
hpicfTunneledNodeCompliance4.setObjects(*((_A,_l),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:hpicfTunneledNodeCompliance4.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'hpicfTunneledNode':hpicfTunneledNode,'hpicfTunneledNodeObjects':hpicfTunneledNodeObjects,'hpicfTunneledNodeConfig':hpicfTunneledNodeConfig,'hpicfTunneledNodeTable':hpicfTunneledNodeTable,'hpicfTunneledNodeEntry':hpicfTunneledNodeEntry,_Y:hpicfTunneledNodeIndex,_E:hpicfTunneledNodeEnable,_F:hpicfTunneledNodePrimaryAddrType,_G:hpicfTunneledNodePrimaryAddr,_H:hpicfTunneledNodeBackupAddrType,_I:hpicfTunneledNodeBackupAddr,_J:hpicfTunneledNodeTimeout,_K:hpicfTunneledNodeRowStatus,_P:hpicfTunneledNodeMode,_Q:hpicfTunneledNodeVlanMode,_R:hpicfTunneledNodeReservedVlanId,_T:hpicfTunneledNodeMPeriod,_g:hpicfTunneledNodeWolVIDList,'hpicfTunneledNodePortConfigTable':hpicfTunneledNodePortConfigTable,'hpicfTunneledNodePortConfigEntry':hpicfTunneledNodePortConfigEntry,_b:hpicfTunneledNodePortRowStatus,_c:hpicfTunneledNodeFallbackLclSw,_L:hpicfTunneledNodeClearStats,'hpicfTunneledNodePapiTable':hpicfTunneledNodePapiTable,'hpicfTunneledNodePapiEntry':hpicfTunneledNodePapiEntry,_a:hpicfTunneledNodePapiAuthMode,_d:hpicfTunneledNodePapiKeyValue,_e:hpicfTunneledNodePapiKeyEncr,_f:hpicfTunneledNodePapiRowStatus,'hpicfTunneledNodeConformance':hpicfTunneledNodeConformance,'hpicfTunneledNodeCompliances':hpicfTunneledNodeCompliances,'hpicfTunneledNodeCompliance':hpicfTunneledNodeCompliance,'hpicfTunneledNodeCompliance1':hpicfTunneledNodeCompliance1,'hpicfTunneledNodeCompliance2':hpicfTunneledNodeCompliance2,'hpicfTunneledNodeCompliance3':hpicfTunneledNodeCompliance3,'hpicfTunneledNodeCompliance4':hpicfTunneledNodeCompliance4,'hpicfTunneledNodeGroups':hpicfTunneledNodeGroups,_h:hpicfTunneledNodeGroup,_M:hpicfTunneledNodePortGroup,_N:hpicfTunneledNodePapiGroup,_i:hpicfTunneledNodeGroup1,_j:hpicfTunneledNodeGroup2,_k:hpicfTunneledNodeGroup3,_l:hpicfTunneledNodeGroup4})