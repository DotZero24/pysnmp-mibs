_r='cvMIBVnetNotifGroup'
_q='cvMIBVnetGroup'
_p='cvMIBVrfNotifGroup'
_o='cvMIBVrfGroup'
_n='cvVnetTrunkDown'
_m='cvVnetTrunkUp'
_l='cvVrfIfDown'
_k='cvVrfIfUp'
_j='cvVnetTrunkNotifEnable'
_i='cvInterfaceVnetVrfList'
_h='cvInterfaceVnetTrunkEnabled'
_g='cvVrfInterfaceVnetTagOverride'
_f='cvVrfListRowStatus'
_e='cvVrfListStorageType'
_d='cvVrfListVrfIndex'
_c='cvVrfVnetTag'
_b='cvVrfIfNotifEnable'
_a='cvVrfInterfaceRowStatus'
_Z='cvVrfInterfaceStorageType'
_Y='cvVrfInterfaceType'
_X='cvVrfRouteDistProt'
_W='cvVrfRowStatus'
_V='cvVrfStorageType'
_U='cvVrfInterfaceIndex'
_T='cvVrfListVindex'
_S='cvVrfListName'
_R='Integer32'
_Q='ifIndex'
_P='InterfaceIndex'
_O='CvVnetTagOrZero'
_N='cvVrfIndex'
_M='cvVrfName'
_L='cvVrfOperStatus'
_K='read-write'
_J='not-accessible'
_I='TruthValue'
_H='Unsigned32'
_G='SnmpAdminString'
_F='ifName'
_E='read-only'
_D='IF-MIB'
_C='read-create'
_B='CISCO-VRF-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
InterfaceIndex,ifIndex,ifName=mibBuilder.importSymbols(_D,_P,_Q,_F)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_G)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_R,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_H,'iso')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','StorageType','TextualConvention',_I)
ciscoVrfMIB=ModuleIdentity((1,3,6,1,4,1,9,9,711))
if mibBuilder.loadTexts:ciscoVrfMIB.setRevisions(('2009-12-10 00:00',))
class CvVrfIfType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('vNETTrunkSI',1),('vNETEdge',2),('vrfEdge',3)))
class CvVnetTagOrZero(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(2,4094))
_CiscoVrfMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoVrfMIBNotifs=_CiscoVrfMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,711,0))
_CiscoVrfMIBObjects_ObjectIdentity=ObjectIdentity
ciscoVrfMIBObjects=_CiscoVrfMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,711,1))
_CvVrf_ObjectIdentity=ObjectIdentity
cvVrf=_CvVrf_ObjectIdentity((1,3,6,1,4,1,9,9,711,1,1))
_CvVrfTable_Object=MibTable
cvVrfTable=_CvVrfTable_Object((1,3,6,1,4,1,9,9,711,1,1,1))
if mibBuilder.loadTexts:cvVrfTable.setStatus(_A)
_CvVrfEntry_Object=MibTableRow
cvVrfEntry=_CvVrfEntry_Object((1,3,6,1,4,1,9,9,711,1,1,1,1))
cvVrfEntry.setIndexNames((0,_B,_N))
if mibBuilder.loadTexts:cvVrfEntry.setStatus(_A)
class _CvVrfIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CvVrfIndex_Type.__name__=_H
_CvVrfIndex_Object=MibTableColumn
cvVrfIndex=_CvVrfIndex_Object((1,3,6,1,4,1,9,9,711,1,1,1,1,1),_CvVrfIndex_Type())
cvVrfIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:cvVrfIndex.setStatus(_A)
class _CvVrfName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_CvVrfName_Type.__name__=_G
_CvVrfName_Object=MibTableColumn
cvVrfName=_CvVrfName_Object((1,3,6,1,4,1,9,9,711,1,1,1,1,2),_CvVrfName_Type())
cvVrfName.setMaxAccess(_C)
if mibBuilder.loadTexts:cvVrfName.setStatus(_A)
class _CvVrfVnetTag_Type(CvVnetTagOrZero):defaultValue=0;subtypeSpec=CvVnetTagOrZero.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(2,4094))
_CvVrfVnetTag_Type.__name__=_O
_CvVrfVnetTag_Object=MibTableColumn
cvVrfVnetTag=_CvVrfVnetTag_Object((1,3,6,1,4,1,9,9,711,1,1,1,1,3),_CvVrfVnetTag_Type())
cvVrfVnetTag.setMaxAccess(_C)
if mibBuilder.loadTexts:cvVrfVnetTag.setStatus(_A)
class _CvVrfOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_CvVrfOperStatus_Type.__name__=_R
_CvVrfOperStatus_Object=MibTableColumn
cvVrfOperStatus=_CvVrfOperStatus_Object((1,3,6,1,4,1,9,9,711,1,1,1,1,4),_CvVrfOperStatus_Type())
cvVrfOperStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:cvVrfOperStatus.setStatus(_A)
class _CvVrfRouteDistProt_Type(Bits):namedValues=NamedValues(*(('none',0),('other',1),('ospf',2),('rip',3),('isis',4),('eigrp',5),('bgp',6)))
_CvVrfRouteDistProt_Type.__name__='Bits'
_CvVrfRouteDistProt_Object=MibTableColumn
cvVrfRouteDistProt=_CvVrfRouteDistProt_Object((1,3,6,1,4,1,9,9,711,1,1,1,1,5),_CvVrfRouteDistProt_Type())
cvVrfRouteDistProt.setMaxAccess(_E)
if mibBuilder.loadTexts:cvVrfRouteDistProt.setStatus(_A)
_CvVrfStorageType_Type=StorageType
_CvVrfStorageType_Object=MibTableColumn
cvVrfStorageType=_CvVrfStorageType_Object((1,3,6,1,4,1,9,9,711,1,1,1,1,6),_CvVrfStorageType_Type())
cvVrfStorageType.setMaxAccess(_E)
if mibBuilder.loadTexts:cvVrfStorageType.setStatus(_A)
_CvVrfRowStatus_Type=RowStatus
_CvVrfRowStatus_Object=MibTableColumn
cvVrfRowStatus=_CvVrfRowStatus_Object((1,3,6,1,4,1,9,9,711,1,1,1,1,7),_CvVrfRowStatus_Type())
cvVrfRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cvVrfRowStatus.setStatus(_A)
_CvVrfListTable_Object=MibTable
cvVrfListTable=_CvVrfListTable_Object((1,3,6,1,4,1,9,9,711,1,1,2))
if mibBuilder.loadTexts:cvVrfListTable.setStatus(_A)
_CvVrfListEntry_Object=MibTableRow
cvVrfListEntry=_CvVrfListEntry_Object((1,3,6,1,4,1,9,9,711,1,1,2,1))
cvVrfListEntry.setIndexNames((0,_B,_S),(0,_B,_T))
if mibBuilder.loadTexts:cvVrfListEntry.setStatus(_A)
class _CvVrfListName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_CvVrfListName_Type.__name__=_G
_CvVrfListName_Object=MibTableColumn
cvVrfListName=_CvVrfListName_Object((1,3,6,1,4,1,9,9,711,1,1,2,1,1),_CvVrfListName_Type())
cvVrfListName.setMaxAccess(_J)
if mibBuilder.loadTexts:cvVrfListName.setStatus(_A)
class _CvVrfListVindex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_CvVrfListVindex_Type.__name__=_H
_CvVrfListVindex_Object=MibTableColumn
cvVrfListVindex=_CvVrfListVindex_Object((1,3,6,1,4,1,9,9,711,1,1,2,1,2),_CvVrfListVindex_Type())
cvVrfListVindex.setMaxAccess(_J)
if mibBuilder.loadTexts:cvVrfListVindex.setStatus(_A)
class _CvVrfListVrfIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CvVrfListVrfIndex_Type.__name__=_H
_CvVrfListVrfIndex_Object=MibTableColumn
cvVrfListVrfIndex=_CvVrfListVrfIndex_Object((1,3,6,1,4,1,9,9,711,1,1,2,1,3),_CvVrfListVrfIndex_Type())
cvVrfListVrfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cvVrfListVrfIndex.setStatus(_A)
_CvVrfListStorageType_Type=StorageType
_CvVrfListStorageType_Object=MibTableColumn
cvVrfListStorageType=_CvVrfListStorageType_Object((1,3,6,1,4,1,9,9,711,1,1,2,1,4),_CvVrfListStorageType_Type())
cvVrfListStorageType.setMaxAccess(_E)
if mibBuilder.loadTexts:cvVrfListStorageType.setStatus(_A)
_CvVrfListRowStatus_Type=RowStatus
_CvVrfListRowStatus_Object=MibTableColumn
cvVrfListRowStatus=_CvVrfListRowStatus_Object((1,3,6,1,4,1,9,9,711,1,1,2,1,5),_CvVrfListRowStatus_Type())
cvVrfListRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cvVrfListRowStatus.setStatus(_A)
_CvInterface_ObjectIdentity=ObjectIdentity
cvInterface=_CvInterface_ObjectIdentity((1,3,6,1,4,1,9,9,711,1,2))
_CvVrfInterfaceTable_Object=MibTable
cvVrfInterfaceTable=_CvVrfInterfaceTable_Object((1,3,6,1,4,1,9,9,711,1,2,1))
if mibBuilder.loadTexts:cvVrfInterfaceTable.setStatus(_A)
_CvVrfInterfaceEntry_Object=MibTableRow
cvVrfInterfaceEntry=_CvVrfInterfaceEntry_Object((1,3,6,1,4,1,9,9,711,1,2,1,1))
cvVrfInterfaceEntry.setIndexNames((0,_B,_N),(0,_B,_U))
if mibBuilder.loadTexts:cvVrfInterfaceEntry.setStatus(_A)
class _CvVrfInterfaceIndex_Type(InterfaceIndex):subtypeSpec=InterfaceIndex.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CvVrfInterfaceIndex_Type.__name__=_P
_CvVrfInterfaceIndex_Object=MibTableColumn
cvVrfInterfaceIndex=_CvVrfInterfaceIndex_Object((1,3,6,1,4,1,9,9,711,1,2,1,1,1),_CvVrfInterfaceIndex_Type())
cvVrfInterfaceIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:cvVrfInterfaceIndex.setStatus(_A)
_CvVrfInterfaceType_Type=CvVrfIfType
_CvVrfInterfaceType_Object=MibTableColumn
cvVrfInterfaceType=_CvVrfInterfaceType_Object((1,3,6,1,4,1,9,9,711,1,2,1,1,2),_CvVrfInterfaceType_Type())
cvVrfInterfaceType.setMaxAccess(_E)
if mibBuilder.loadTexts:cvVrfInterfaceType.setStatus(_A)
class _CvVrfInterfaceVnetTagOverride_Type(CvVnetTagOrZero):defaultValue=0;subtypeSpec=CvVnetTagOrZero.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(2,4094))
_CvVrfInterfaceVnetTagOverride_Type.__name__=_O
_CvVrfInterfaceVnetTagOverride_Object=MibTableColumn
cvVrfInterfaceVnetTagOverride=_CvVrfInterfaceVnetTagOverride_Object((1,3,6,1,4,1,9,9,711,1,2,1,1,3),_CvVrfInterfaceVnetTagOverride_Type())
cvVrfInterfaceVnetTagOverride.setMaxAccess(_C)
if mibBuilder.loadTexts:cvVrfInterfaceVnetTagOverride.setStatus(_A)
_CvVrfInterfaceStorageType_Type=StorageType
_CvVrfInterfaceStorageType_Object=MibTableColumn
cvVrfInterfaceStorageType=_CvVrfInterfaceStorageType_Object((1,3,6,1,4,1,9,9,711,1,2,1,1,4),_CvVrfInterfaceStorageType_Type())
cvVrfInterfaceStorageType.setMaxAccess(_E)
if mibBuilder.loadTexts:cvVrfInterfaceStorageType.setStatus(_A)
_CvVrfInterfaceRowStatus_Type=RowStatus
_CvVrfInterfaceRowStatus_Object=MibTableColumn
cvVrfInterfaceRowStatus=_CvVrfInterfaceRowStatus_Object((1,3,6,1,4,1,9,9,711,1,2,1,1,5),_CvVrfInterfaceRowStatus_Type())
cvVrfInterfaceRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cvVrfInterfaceRowStatus.setStatus(_A)
_CvInterfaceTable_Object=MibTable
cvInterfaceTable=_CvInterfaceTable_Object((1,3,6,1,4,1,9,9,711,1,2,2))
if mibBuilder.loadTexts:cvInterfaceTable.setStatus(_A)
_CvInterfaceEntry_Object=MibTableRow
cvInterfaceEntry=_CvInterfaceEntry_Object((1,3,6,1,4,1,9,9,711,1,2,2,1))
cvInterfaceEntry.setIndexNames((0,_D,_Q))
if mibBuilder.loadTexts:cvInterfaceEntry.setStatus(_A)
class _CvInterfaceVnetTrunkEnabled_Type(TruthValue):defaultValue=2
_CvInterfaceVnetTrunkEnabled_Type.__name__=_I
_CvInterfaceVnetTrunkEnabled_Object=MibTableColumn
cvInterfaceVnetTrunkEnabled=_CvInterfaceVnetTrunkEnabled_Object((1,3,6,1,4,1,9,9,711,1,2,2,1,1),_CvInterfaceVnetTrunkEnabled_Type())
cvInterfaceVnetTrunkEnabled.setMaxAccess(_K)
if mibBuilder.loadTexts:cvInterfaceVnetTrunkEnabled.setStatus(_A)
class _CvInterfaceVnetVrfList_Type(SnmpAdminString):defaultValue=OctetString('');subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(1,32))
_CvInterfaceVnetVrfList_Type.__name__=_G
_CvInterfaceVnetVrfList_Object=MibTableColumn
cvInterfaceVnetVrfList=_CvInterfaceVnetVrfList_Object((1,3,6,1,4,1,9,9,711,1,2,2,1,2),_CvInterfaceVnetVrfList_Type())
cvInterfaceVnetVrfList.setMaxAccess(_K)
if mibBuilder.loadTexts:cvInterfaceVnetVrfList.setStatus(_A)
_CvNotifCntl_ObjectIdentity=ObjectIdentity
cvNotifCntl=_CvNotifCntl_ObjectIdentity((1,3,6,1,4,1,9,9,711,1,3))
class _CvVrfIfNotifEnable_Type(TruthValue):defaultValue=2
_CvVrfIfNotifEnable_Type.__name__=_I
_CvVrfIfNotifEnable_Object=MibScalar
cvVrfIfNotifEnable=_CvVrfIfNotifEnable_Object((1,3,6,1,4,1,9,9,711,1,3,1),_CvVrfIfNotifEnable_Type())
cvVrfIfNotifEnable.setMaxAccess(_K)
if mibBuilder.loadTexts:cvVrfIfNotifEnable.setStatus(_A)
class _CvVnetTrunkNotifEnable_Type(TruthValue):defaultValue=2
_CvVnetTrunkNotifEnable_Type.__name__=_I
_CvVnetTrunkNotifEnable_Object=MibScalar
cvVnetTrunkNotifEnable=_CvVnetTrunkNotifEnable_Object((1,3,6,1,4,1,9,9,711,1,3,2),_CvVnetTrunkNotifEnable_Type())
cvVnetTrunkNotifEnable.setMaxAccess(_K)
if mibBuilder.loadTexts:cvVnetTrunkNotifEnable.setStatus(_A)
_CiscoVrfMIBConform_ObjectIdentity=ObjectIdentity
ciscoVrfMIBConform=_CiscoVrfMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,711,2))
_CvMIBGroups_ObjectIdentity=ObjectIdentity
cvMIBGroups=_CvMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,711,2,1))
_CvMIBCompliances_ObjectIdentity=ObjectIdentity
cvMIBCompliances=_CvMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,711,2,2))
cvMIBVrfGroup=ObjectGroup((1,3,6,1,4,1,9,9,711,2,1,1))
cvMIBVrfGroup.setObjects(*((_B,_L),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_M)))
if mibBuilder.loadTexts:cvMIBVrfGroup.setStatus(_A)
cvMIBVnetGroup=ObjectGroup((1,3,6,1,4,1,9,9,711,2,1,3))
cvMIBVnetGroup.setObjects(*((_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j)))
if mibBuilder.loadTexts:cvMIBVnetGroup.setStatus(_A)
cvVrfIfUp=NotificationType((1,3,6,1,4,1,9,9,711,0,1))
cvVrfIfUp.setObjects(*((_D,_F),(_B,_M),(_B,_L)))
if mibBuilder.loadTexts:cvVrfIfUp.setStatus(_A)
cvVrfIfDown=NotificationType((1,3,6,1,4,1,9,9,711,0,2))
cvVrfIfDown.setObjects(*((_D,_F),(_B,_M),(_B,_L)))
if mibBuilder.loadTexts:cvVrfIfDown.setStatus(_A)
cvVnetTrunkUp=NotificationType((1,3,6,1,4,1,9,9,711,0,3))
cvVnetTrunkUp.setObjects((_D,_F))
if mibBuilder.loadTexts:cvVnetTrunkUp.setStatus(_A)
cvVnetTrunkDown=NotificationType((1,3,6,1,4,1,9,9,711,0,4))
cvVnetTrunkDown.setObjects((_D,_F))
if mibBuilder.loadTexts:cvVnetTrunkDown.setStatus(_A)
cvMIBVrfNotifGroup=NotificationGroup((1,3,6,1,4,1,9,9,711,2,1,2))
cvMIBVrfNotifGroup.setObjects(*((_B,_k),(_B,_l)))
if mibBuilder.loadTexts:cvMIBVrfNotifGroup.setStatus(_A)
cvMIBVnetNotifGroup=NotificationGroup((1,3,6,1,4,1,9,9,711,2,1,4))
cvMIBVnetNotifGroup.setObjects(*((_B,_m),(_B,_n)))
if mibBuilder.loadTexts:cvMIBVnetNotifGroup.setStatus(_A)
cvMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,711,2,2,1))
cvMIBCompliance.setObjects(*((_B,_o),(_B,_p),(_B,_q),(_B,_r)))
if mibBuilder.loadTexts:cvMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'CvVrfIfType':CvVrfIfType,_O:CvVnetTagOrZero,'ciscoVrfMIB':ciscoVrfMIB,'ciscoVrfMIBNotifs':ciscoVrfMIBNotifs,_k:cvVrfIfUp,_l:cvVrfIfDown,_m:cvVnetTrunkUp,_n:cvVnetTrunkDown,'ciscoVrfMIBObjects':ciscoVrfMIBObjects,'cvVrf':cvVrf,'cvVrfTable':cvVrfTable,'cvVrfEntry':cvVrfEntry,_N:cvVrfIndex,_M:cvVrfName,_c:cvVrfVnetTag,_L:cvVrfOperStatus,_X:cvVrfRouteDistProt,_V:cvVrfStorageType,_W:cvVrfRowStatus,'cvVrfListTable':cvVrfListTable,'cvVrfListEntry':cvVrfListEntry,_S:cvVrfListName,_T:cvVrfListVindex,_d:cvVrfListVrfIndex,_e:cvVrfListStorageType,_f:cvVrfListRowStatus,'cvInterface':cvInterface,'cvVrfInterfaceTable':cvVrfInterfaceTable,'cvVrfInterfaceEntry':cvVrfInterfaceEntry,_U:cvVrfInterfaceIndex,_Y:cvVrfInterfaceType,_g:cvVrfInterfaceVnetTagOverride,_Z:cvVrfInterfaceStorageType,_a:cvVrfInterfaceRowStatus,'cvInterfaceTable':cvInterfaceTable,'cvInterfaceEntry':cvInterfaceEntry,_h:cvInterfaceVnetTrunkEnabled,_i:cvInterfaceVnetVrfList,'cvNotifCntl':cvNotifCntl,_b:cvVrfIfNotifEnable,_j:cvVnetTrunkNotifEnable,'ciscoVrfMIBConform':ciscoVrfMIBConform,'cvMIBGroups':cvMIBGroups,_o:cvMIBVrfGroup,_p:cvMIBVrfNotifGroup,_q:cvMIBVnetGroup,_r:cvMIBVnetNotifGroup,'cvMIBCompliances':cvMIBCompliances,'cvMIBCompliance':cvMIBCompliance})