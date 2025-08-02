_V='ipiMIBVrfNotifGroup'
_U='ipiMIBVrfGroup'
_T='ipiVrfIfDown'
_S='ipiVrfIfUp'
_R='ipiVrfInterfaceRowStatus'
_Q='ipiVrfInterfaceStorageType'
_P='ipiVrfInterfaceName'
_O='ipiVrfRouteDistProt'
_N='ipiVrfRowStatus'
_M='ipiVrfStorageType'
_L='ipiVrfIndex'
_K='Unsigned32'
_J='Integer32'
_I='InterfaceIndex'
_H='SnmpAdminString'
_G='ipiVrfName'
_F='ipiVrfOperStatus'
_E='read-create'
_D='ipiVrfInterfaceIndex'
_C='read-only'
_B='current'
_A='IPI-VRF-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB',_I)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_H)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_J,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_K,'enterprises','iso')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','StorageType','TextualConvention')
ipiVrfMIB=ModuleIdentity((1,3,6,1,4,1,6926,2,35))
if mibBuilder.loadTexts:ipiVrfMIB.setRevisions(('2014-05-16 12:25',))
_Oaccess_ObjectIdentity=ObjectIdentity
oaccess=_Oaccess_ObjectIdentity((1,3,6,1,4,1,6926))
_OaOptiSwitch_ObjectIdentity=ObjectIdentity
oaOptiSwitch=_OaOptiSwitch_ObjectIdentity((1,3,6,1,4,1,6926,2))
_IpiVrfMIBNotifs_ObjectIdentity=ObjectIdentity
ipiVrfMIBNotifs=_IpiVrfMIBNotifs_ObjectIdentity((1,3,6,1,4,1,6926,2,35,0))
_IpiVrfMIBObjects_ObjectIdentity=ObjectIdentity
ipiVrfMIBObjects=_IpiVrfMIBObjects_ObjectIdentity((1,3,6,1,4,1,6926,2,35,1))
_IpiVrf_ObjectIdentity=ObjectIdentity
ipiVrf=_IpiVrf_ObjectIdentity((1,3,6,1,4,1,6926,2,35,1,1))
_IpiVrfTable_Object=MibTable
ipiVrfTable=_IpiVrfTable_Object((1,3,6,1,4,1,6926,2,35,1,1,1))
if mibBuilder.loadTexts:ipiVrfTable.setStatus(_B)
_IpiVrfEntry_Object=MibTableRow
ipiVrfEntry=_IpiVrfEntry_Object((1,3,6,1,4,1,6926,2,35,1,1,1,1))
ipiVrfEntry.setIndexNames((0,_A,_L))
if mibBuilder.loadTexts:ipiVrfEntry.setStatus(_B)
class _IpiVrfIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_IpiVrfIndex_Type.__name__=_K
_IpiVrfIndex_Object=MibTableColumn
ipiVrfIndex=_IpiVrfIndex_Object((1,3,6,1,4,1,6926,2,35,1,1,1,1,1),_IpiVrfIndex_Type())
ipiVrfIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:ipiVrfIndex.setStatus(_B)
class _IpiVrfName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_IpiVrfName_Type.__name__=_H
_IpiVrfName_Object=MibTableColumn
ipiVrfName=_IpiVrfName_Object((1,3,6,1,4,1,6926,2,35,1,1,1,1,2),_IpiVrfName_Type())
ipiVrfName.setMaxAccess(_E)
if mibBuilder.loadTexts:ipiVrfName.setStatus(_B)
class _IpiVrfOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_IpiVrfOperStatus_Type.__name__=_J
_IpiVrfOperStatus_Object=MibTableColumn
ipiVrfOperStatus=_IpiVrfOperStatus_Object((1,3,6,1,4,1,6926,2,35,1,1,1,1,3),_IpiVrfOperStatus_Type())
ipiVrfOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ipiVrfOperStatus.setStatus(_B)
class _IpiVrfRouteDistProt_Type(Bits):namedValues=NamedValues(*(('none',0),('other',1),('static',2),('ospf',3),('bgp',4),('pim',5),('igmp',6)))
_IpiVrfRouteDistProt_Type.__name__='Bits'
_IpiVrfRouteDistProt_Object=MibTableColumn
ipiVrfRouteDistProt=_IpiVrfRouteDistProt_Object((1,3,6,1,4,1,6926,2,35,1,1,1,1,4),_IpiVrfRouteDistProt_Type())
ipiVrfRouteDistProt.setMaxAccess(_C)
if mibBuilder.loadTexts:ipiVrfRouteDistProt.setStatus(_B)
_IpiVrfStorageType_Type=StorageType
_IpiVrfStorageType_Object=MibTableColumn
ipiVrfStorageType=_IpiVrfStorageType_Object((1,3,6,1,4,1,6926,2,35,1,1,1,1,5),_IpiVrfStorageType_Type())
ipiVrfStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:ipiVrfStorageType.setStatus(_B)
_IpiVrfRowStatus_Type=RowStatus
_IpiVrfRowStatus_Object=MibTableColumn
ipiVrfRowStatus=_IpiVrfRowStatus_Object((1,3,6,1,4,1,6926,2,35,1,1,1,1,6),_IpiVrfRowStatus_Type())
ipiVrfRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:ipiVrfRowStatus.setStatus(_B)
_IpiInterface_ObjectIdentity=ObjectIdentity
ipiInterface=_IpiInterface_ObjectIdentity((1,3,6,1,4,1,6926,2,35,1,2))
_IpiVrfInterfaceTable_Object=MibTable
ipiVrfInterfaceTable=_IpiVrfInterfaceTable_Object((1,3,6,1,4,1,6926,2,35,1,2,1))
if mibBuilder.loadTexts:ipiVrfInterfaceTable.setStatus(_B)
_IpiVrfInterfaceEntry_Object=MibTableRow
ipiVrfInterfaceEntry=_IpiVrfInterfaceEntry_Object((1,3,6,1,4,1,6926,2,35,1,2,1,1))
ipiVrfInterfaceEntry.setIndexNames((0,_A,_D))
if mibBuilder.loadTexts:ipiVrfInterfaceEntry.setStatus(_B)
class _IpiVrfInterfaceIndex_Type(InterfaceIndex):subtypeSpec=InterfaceIndex.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_IpiVrfInterfaceIndex_Type.__name__=_I
_IpiVrfInterfaceIndex_Object=MibTableColumn
ipiVrfInterfaceIndex=_IpiVrfInterfaceIndex_Object((1,3,6,1,4,1,6926,2,35,1,2,1,1,1),_IpiVrfInterfaceIndex_Type())
ipiVrfInterfaceIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ipiVrfInterfaceIndex.setStatus(_B)
class _IpiVrfInterfaceName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_IpiVrfInterfaceName_Type.__name__=_H
_IpiVrfInterfaceName_Object=MibTableColumn
ipiVrfInterfaceName=_IpiVrfInterfaceName_Object((1,3,6,1,4,1,6926,2,35,1,2,1,1,2),_IpiVrfInterfaceName_Type())
ipiVrfInterfaceName.setMaxAccess(_E)
if mibBuilder.loadTexts:ipiVrfInterfaceName.setStatus(_B)
_IpiVrfInterfaceStorageType_Type=StorageType
_IpiVrfInterfaceStorageType_Object=MibTableColumn
ipiVrfInterfaceStorageType=_IpiVrfInterfaceStorageType_Object((1,3,6,1,4,1,6926,2,35,1,2,1,1,3),_IpiVrfInterfaceStorageType_Type())
ipiVrfInterfaceStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:ipiVrfInterfaceStorageType.setStatus(_B)
_IpiVrfInterfaceRowStatus_Type=RowStatus
_IpiVrfInterfaceRowStatus_Object=MibTableColumn
ipiVrfInterfaceRowStatus=_IpiVrfInterfaceRowStatus_Object((1,3,6,1,4,1,6926,2,35,1,2,1,1,4),_IpiVrfInterfaceRowStatus_Type())
ipiVrfInterfaceRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:ipiVrfInterfaceRowStatus.setStatus(_B)
_IpiVrfMIBConform_ObjectIdentity=ObjectIdentity
ipiVrfMIBConform=_IpiVrfMIBConform_ObjectIdentity((1,3,6,1,4,1,6926,2,35,2))
_IpiMIBGroups_ObjectIdentity=ObjectIdentity
ipiMIBGroups=_IpiMIBGroups_ObjectIdentity((1,3,6,1,4,1,6926,2,35,2,1))
_IpiMIBCompliances_ObjectIdentity=ObjectIdentity
ipiMIBCompliances=_IpiMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6926,2,35,2,2))
ipiMIBVrfGroup=ObjectGroup((1,3,6,1,4,1,6926,2,35,2,1,1))
ipiMIBVrfGroup.setObjects(*((_A,_F),(_A,_M),(_A,_N),(_A,_O),(_A,_D),(_A,_P),(_A,_Q),(_A,_R),(_A,_G)))
if mibBuilder.loadTexts:ipiMIBVrfGroup.setStatus(_B)
ipiVrfIfUp=NotificationType((1,3,6,1,4,1,6926,2,35,0,1))
ipiVrfIfUp.setObjects(*((_A,_D),(_A,_G),(_A,_F)))
if mibBuilder.loadTexts:ipiVrfIfUp.setStatus(_B)
ipiVrfIfDown=NotificationType((1,3,6,1,4,1,6926,2,35,0,2))
ipiVrfIfDown.setObjects(*((_A,_D),(_A,_G),(_A,_F)))
if mibBuilder.loadTexts:ipiVrfIfDown.setStatus(_B)
ipiMIBVrfNotifGroup=NotificationGroup((1,3,6,1,4,1,6926,2,35,2,1,2))
ipiMIBVrfNotifGroup.setObjects(*((_A,_S),(_A,_T)))
if mibBuilder.loadTexts:ipiMIBVrfNotifGroup.setStatus(_B)
ipiMIBCompliance=ModuleCompliance((1,3,6,1,4,1,6926,2,35,2,2,1))
ipiMIBCompliance.setObjects(*((_A,_U),(_A,_V)))
if mibBuilder.loadTexts:ipiMIBCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'oaccess':oaccess,'oaOptiSwitch':oaOptiSwitch,'ipiVrfMIB':ipiVrfMIB,'ipiVrfMIBNotifs':ipiVrfMIBNotifs,_S:ipiVrfIfUp,_T:ipiVrfIfDown,'ipiVrfMIBObjects':ipiVrfMIBObjects,'ipiVrf':ipiVrf,'ipiVrfTable':ipiVrfTable,'ipiVrfEntry':ipiVrfEntry,_L:ipiVrfIndex,_G:ipiVrfName,_F:ipiVrfOperStatus,_O:ipiVrfRouteDistProt,_M:ipiVrfStorageType,_N:ipiVrfRowStatus,'ipiInterface':ipiInterface,'ipiVrfInterfaceTable':ipiVrfInterfaceTable,'ipiVrfInterfaceEntry':ipiVrfInterfaceEntry,_D:ipiVrfInterfaceIndex,_P:ipiVrfInterfaceName,_Q:ipiVrfInterfaceStorageType,_R:ipiVrfInterfaceRowStatus,'ipiVrfMIBConform':ipiVrfMIBConform,'ipiMIBGroups':ipiMIBGroups,_U:ipiMIBVrfGroup,_V:ipiMIBVrfNotifGroup,'ipiMIBCompliances':ipiMIBCompliances,'ipiMIBCompliance':ipiMIBCompliance})