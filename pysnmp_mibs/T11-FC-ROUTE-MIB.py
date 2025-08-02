_a='t11FcRouteGroup'
_Z='t11FcRouteRowStatus'
_Y='t11FcRouteStorageType'
_X='t11FcRouteIfDown'
_W='t11FcRouteType'
_V='t11FcRouteMetric'
_U='t11FcRouteDomainId'
_T='t11FcRouteFabricLastChange'
_S='t11FcRouteOutInterface'
_R='t11FcRouteProto'
_Q='t11FcRouteInInterface'
_P='t11FcRouteSrcMask'
_O='t11FcRouteSrcAddrId'
_N='t11FcRouteDestMask'
_M='t11FcRouteDestAddrId'
_L='StorageType'
_K='Unsigned32'
_J='FcAddressIdOrZero'
_I='t11FcRouteFabricIndex'
_H='fcmSwitchIndex'
_G='fcmInstanceIndex'
_F='Integer32'
_E='FC-MGMT-MIB'
_D='read-create'
_C='not-accessible'
_B='T11-FC-ROUTE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
FcAddressIdOrZero,FcDomainIdOrZero,fcmInstanceIndex,fcmSwitchIndex=mibBuilder.importSymbols(_E,_J,'FcDomainIdOrZero',_G,_H)
InterfaceIndex,InterfaceIndexOrZero=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','InterfaceIndexOrZero')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_K,'iso','mib-2')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus',_L,'TextualConvention','TimeStamp')
T11FabricIndex,=mibBuilder.importSymbols('T11-TC-MIB','T11FabricIndex')
t11FcRouteMIB=ModuleIdentity((1,3,6,1,2,1,144))
if mibBuilder.loadTexts:t11FcRouteMIB.setRevisions(('2006-08-14 00:00',))
_T11FcRouteNotifications_ObjectIdentity=ObjectIdentity
t11FcRouteNotifications=_T11FcRouteNotifications_ObjectIdentity((1,3,6,1,2,1,144,0))
_T11FcRouteObjects_ObjectIdentity=ObjectIdentity
t11FcRouteObjects=_T11FcRouteObjects_ObjectIdentity((1,3,6,1,2,1,144,1))
_T11FcRouteFabricTable_Object=MibTable
t11FcRouteFabricTable=_T11FcRouteFabricTable_Object((1,3,6,1,2,1,144,1,1))
if mibBuilder.loadTexts:t11FcRouteFabricTable.setStatus(_A)
_T11FcRouteFabricEntry_Object=MibTableRow
t11FcRouteFabricEntry=_T11FcRouteFabricEntry_Object((1,3,6,1,2,1,144,1,1,1))
t11FcRouteFabricEntry.setIndexNames((0,_E,_G),(0,_E,_H),(0,_B,_I))
if mibBuilder.loadTexts:t11FcRouteFabricEntry.setStatus(_A)
_T11FcRouteFabricIndex_Type=T11FabricIndex
_T11FcRouteFabricIndex_Object=MibTableColumn
t11FcRouteFabricIndex=_T11FcRouteFabricIndex_Object((1,3,6,1,2,1,144,1,1,1,1),_T11FcRouteFabricIndex_Type())
t11FcRouteFabricIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:t11FcRouteFabricIndex.setStatus(_A)
_T11FcRouteFabricLastChange_Type=TimeStamp
_T11FcRouteFabricLastChange_Object=MibTableColumn
t11FcRouteFabricLastChange=_T11FcRouteFabricLastChange_Object((1,3,6,1,2,1,144,1,1,1,2),_T11FcRouteFabricLastChange_Type())
t11FcRouteFabricLastChange.setMaxAccess('read-only')
if mibBuilder.loadTexts:t11FcRouteFabricLastChange.setStatus(_A)
_T11FcRouteTable_Object=MibTable
t11FcRouteTable=_T11FcRouteTable_Object((1,3,6,1,2,1,144,1,2))
if mibBuilder.loadTexts:t11FcRouteTable.setStatus(_A)
_T11FcRouteEntry_Object=MibTableRow
t11FcRouteEntry=_T11FcRouteEntry_Object((1,3,6,1,2,1,144,1,2,1))
t11FcRouteEntry.setIndexNames((0,_E,_G),(0,_E,_H),(0,_B,_I),(0,_B,_M),(0,_B,_N),(0,_B,_O),(0,_B,_P),(0,_B,_Q),(0,_B,_R),(0,_B,_S))
if mibBuilder.loadTexts:t11FcRouteEntry.setStatus(_A)
class _T11FcRouteDestAddrId_Type(FcAddressIdOrZero):subtypeSpec=FcAddressIdOrZero.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,3));fixedLength=3
_T11FcRouteDestAddrId_Type.__name__=_J
_T11FcRouteDestAddrId_Object=MibTableColumn
t11FcRouteDestAddrId=_T11FcRouteDestAddrId_Object((1,3,6,1,2,1,144,1,2,1,1),_T11FcRouteDestAddrId_Type())
t11FcRouteDestAddrId.setMaxAccess(_C)
if mibBuilder.loadTexts:t11FcRouteDestAddrId.setStatus(_A)
_T11FcRouteDestMask_Type=FcAddressIdOrZero
_T11FcRouteDestMask_Object=MibTableColumn
t11FcRouteDestMask=_T11FcRouteDestMask_Object((1,3,6,1,2,1,144,1,2,1,2),_T11FcRouteDestMask_Type())
t11FcRouteDestMask.setMaxAccess(_C)
if mibBuilder.loadTexts:t11FcRouteDestMask.setStatus(_A)
_T11FcRouteSrcAddrId_Type=FcAddressIdOrZero
_T11FcRouteSrcAddrId_Object=MibTableColumn
t11FcRouteSrcAddrId=_T11FcRouteSrcAddrId_Object((1,3,6,1,2,1,144,1,2,1,3),_T11FcRouteSrcAddrId_Type())
t11FcRouteSrcAddrId.setMaxAccess(_C)
if mibBuilder.loadTexts:t11FcRouteSrcAddrId.setStatus(_A)
_T11FcRouteSrcMask_Type=FcAddressIdOrZero
_T11FcRouteSrcMask_Object=MibTableColumn
t11FcRouteSrcMask=_T11FcRouteSrcMask_Object((1,3,6,1,2,1,144,1,2,1,4),_T11FcRouteSrcMask_Type())
t11FcRouteSrcMask.setMaxAccess(_C)
if mibBuilder.loadTexts:t11FcRouteSrcMask.setStatus(_A)
_T11FcRouteInInterface_Type=InterfaceIndexOrZero
_T11FcRouteInInterface_Object=MibTableColumn
t11FcRouteInInterface=_T11FcRouteInInterface_Object((1,3,6,1,2,1,144,1,2,1,5),_T11FcRouteInInterface_Type())
t11FcRouteInInterface.setMaxAccess(_C)
if mibBuilder.loadTexts:t11FcRouteInInterface.setStatus(_A)
class _T11FcRouteProto_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('other',1),('local',2),('netmgmt',3),('fspf',4)))
_T11FcRouteProto_Type.__name__=_F
_T11FcRouteProto_Object=MibTableColumn
t11FcRouteProto=_T11FcRouteProto_Object((1,3,6,1,2,1,144,1,2,1,6),_T11FcRouteProto_Type())
t11FcRouteProto.setMaxAccess(_C)
if mibBuilder.loadTexts:t11FcRouteProto.setStatus(_A)
_T11FcRouteOutInterface_Type=InterfaceIndex
_T11FcRouteOutInterface_Object=MibTableColumn
t11FcRouteOutInterface=_T11FcRouteOutInterface_Object((1,3,6,1,2,1,144,1,2,1,7),_T11FcRouteOutInterface_Type())
t11FcRouteOutInterface.setMaxAccess(_C)
if mibBuilder.loadTexts:t11FcRouteOutInterface.setStatus(_A)
_T11FcRouteDomainId_Type=FcDomainIdOrZero
_T11FcRouteDomainId_Object=MibTableColumn
t11FcRouteDomainId=_T11FcRouteDomainId_Object((1,3,6,1,2,1,144,1,2,1,8),_T11FcRouteDomainId_Type())
t11FcRouteDomainId.setMaxAccess(_D)
if mibBuilder.loadTexts:t11FcRouteDomainId.setStatus(_A)
class _T11FcRouteMetric_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_T11FcRouteMetric_Type.__name__=_K
_T11FcRouteMetric_Object=MibTableColumn
t11FcRouteMetric=_T11FcRouteMetric_Object((1,3,6,1,2,1,144,1,2,1,9),_T11FcRouteMetric_Type())
t11FcRouteMetric.setMaxAccess(_D)
if mibBuilder.loadTexts:t11FcRouteMetric.setStatus(_A)
class _T11FcRouteType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('local',1),('remote',2)))
_T11FcRouteType_Type.__name__=_F
_T11FcRouteType_Object=MibTableColumn
t11FcRouteType=_T11FcRouteType_Object((1,3,6,1,2,1,144,1,2,1,10),_T11FcRouteType_Type())
t11FcRouteType.setMaxAccess(_D)
if mibBuilder.loadTexts:t11FcRouteType.setStatus(_A)
class _T11FcRouteIfDown_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('remove',1),('retain',2)))
_T11FcRouteIfDown_Type.__name__=_F
_T11FcRouteIfDown_Object=MibTableColumn
t11FcRouteIfDown=_T11FcRouteIfDown_Object((1,3,6,1,2,1,144,1,2,1,11),_T11FcRouteIfDown_Type())
t11FcRouteIfDown.setMaxAccess(_D)
if mibBuilder.loadTexts:t11FcRouteIfDown.setStatus(_A)
class _T11FcRouteStorageType_Type(StorageType):defaultValue=3
_T11FcRouteStorageType_Type.__name__=_L
_T11FcRouteStorageType_Object=MibTableColumn
t11FcRouteStorageType=_T11FcRouteStorageType_Object((1,3,6,1,2,1,144,1,2,1,12),_T11FcRouteStorageType_Type())
t11FcRouteStorageType.setMaxAccess(_D)
if mibBuilder.loadTexts:t11FcRouteStorageType.setStatus(_A)
_T11FcRouteRowStatus_Type=RowStatus
_T11FcRouteRowStatus_Object=MibTableColumn
t11FcRouteRowStatus=_T11FcRouteRowStatus_Object((1,3,6,1,2,1,144,1,2,1,13),_T11FcRouteRowStatus_Type())
t11FcRouteRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:t11FcRouteRowStatus.setStatus(_A)
_T11FcRouteConformance_ObjectIdentity=ObjectIdentity
t11FcRouteConformance=_T11FcRouteConformance_ObjectIdentity((1,3,6,1,2,1,144,2))
_T11FcRouteCompliances_ObjectIdentity=ObjectIdentity
t11FcRouteCompliances=_T11FcRouteCompliances_ObjectIdentity((1,3,6,1,2,1,144,2,1))
_T11FcRouteGroups_ObjectIdentity=ObjectIdentity
t11FcRouteGroups=_T11FcRouteGroups_ObjectIdentity((1,3,6,1,2,1,144,2,2))
t11FcRouteGroup=ObjectGroup((1,3,6,1,2,1,144,2,2,1))
t11FcRouteGroup.setObjects(*((_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z)))
if mibBuilder.loadTexts:t11FcRouteGroup.setStatus(_A)
t11FcRouteCompliance=ModuleCompliance((1,3,6,1,2,1,144,2,1,1))
t11FcRouteCompliance.setObjects((_B,_a))
if mibBuilder.loadTexts:t11FcRouteCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'t11FcRouteMIB':t11FcRouteMIB,'t11FcRouteNotifications':t11FcRouteNotifications,'t11FcRouteObjects':t11FcRouteObjects,'t11FcRouteFabricTable':t11FcRouteFabricTable,'t11FcRouteFabricEntry':t11FcRouteFabricEntry,_I:t11FcRouteFabricIndex,_T:t11FcRouteFabricLastChange,'t11FcRouteTable':t11FcRouteTable,'t11FcRouteEntry':t11FcRouteEntry,_M:t11FcRouteDestAddrId,_N:t11FcRouteDestMask,_O:t11FcRouteSrcAddrId,_P:t11FcRouteSrcMask,_Q:t11FcRouteInInterface,_R:t11FcRouteProto,_S:t11FcRouteOutInterface,_U:t11FcRouteDomainId,_V:t11FcRouteMetric,_W:t11FcRouteType,_X:t11FcRouteIfDown,_Y:t11FcRouteStorageType,_Z:t11FcRouteRowStatus,'t11FcRouteConformance':t11FcRouteConformance,'t11FcRouteCompliances':t11FcRouteCompliances,'t11FcRouteCompliance':t11FcRouteCompliance,'t11FcRouteGroups':t11FcRouteGroups,_a:t11FcRouteGroup})