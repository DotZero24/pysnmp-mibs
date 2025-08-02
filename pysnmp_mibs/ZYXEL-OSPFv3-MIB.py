_E='zyOspfv3RedistributeRouteProtocol'
_D='ZYXEL-OSPFv3-MIB'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB','EnabledStatus')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
esMgmt,=mibBuilder.importSymbols('ZYXEL-ES-SMI','esMgmt')
zyxelOspfv3=ModuleIdentity((1,3,6,1,4,1,890,1,15,3,117))
_ZyxelOspfv3Setup_ObjectIdentity=ObjectIdentity
zyxelOspfv3Setup=_ZyxelOspfv3Setup_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,117,1))
_ZyxelOspfv3RedistributeRouteTable_Object=MibTable
zyxelOspfv3RedistributeRouteTable=_ZyxelOspfv3RedistributeRouteTable_Object((1,3,6,1,4,1,890,1,15,3,117,1,1))
if mibBuilder.loadTexts:zyxelOspfv3RedistributeRouteTable.setStatus(_A)
_ZyxelOspfv3RedistributeRouteEntry_Object=MibTableRow
zyxelOspfv3RedistributeRouteEntry=_ZyxelOspfv3RedistributeRouteEntry_Object((1,3,6,1,4,1,890,1,15,3,117,1,1,1))
zyxelOspfv3RedistributeRouteEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:zyxelOspfv3RedistributeRouteEntry.setStatus(_A)
class _ZyOspfv3RedistributeRouteProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ripng',1),('static',2)))
_ZyOspfv3RedistributeRouteProtocol_Type.__name__=_C
_ZyOspfv3RedistributeRouteProtocol_Object=MibTableColumn
zyOspfv3RedistributeRouteProtocol=_ZyOspfv3RedistributeRouteProtocol_Object((1,3,6,1,4,1,890,1,15,3,117,1,1,1,1),_ZyOspfv3RedistributeRouteProtocol_Type())
zyOspfv3RedistributeRouteProtocol.setMaxAccess('read-only')
if mibBuilder.loadTexts:zyOspfv3RedistributeRouteProtocol.setStatus(_A)
_ZyOspfv3RedistributeRouteState_Type=EnabledStatus
_ZyOspfv3RedistributeRouteState_Object=MibTableColumn
zyOspfv3RedistributeRouteState=_ZyOspfv3RedistributeRouteState_Object((1,3,6,1,4,1,890,1,15,3,117,1,1,1,2),_ZyOspfv3RedistributeRouteState_Type())
zyOspfv3RedistributeRouteState.setMaxAccess(_B)
if mibBuilder.loadTexts:zyOspfv3RedistributeRouteState.setStatus(_A)
_ZyOspfv3RedistributeRouteType_Type=Integer32
_ZyOspfv3RedistributeRouteType_Object=MibTableColumn
zyOspfv3RedistributeRouteType=_ZyOspfv3RedistributeRouteType_Object((1,3,6,1,4,1,890,1,15,3,117,1,1,1,3),_ZyOspfv3RedistributeRouteType_Type())
zyOspfv3RedistributeRouteType.setMaxAccess(_B)
if mibBuilder.loadTexts:zyOspfv3RedistributeRouteType.setStatus(_A)
_ZyOspfv3RedistributeRouteMetric_Type=Integer32
_ZyOspfv3RedistributeRouteMetric_Object=MibTableColumn
zyOspfv3RedistributeRouteMetric=_ZyOspfv3RedistributeRouteMetric_Object((1,3,6,1,4,1,890,1,15,3,117,1,1,1,4),_ZyOspfv3RedistributeRouteMetric_Type())
zyOspfv3RedistributeRouteMetric.setMaxAccess(_B)
if mibBuilder.loadTexts:zyOspfv3RedistributeRouteMetric.setStatus(_A)
_ZyxelOspfv3GeneralGroup_ObjectIdentity=ObjectIdentity
zyxelOspfv3GeneralGroup=_ZyxelOspfv3GeneralGroup_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,117,1,2))
_ZyOspfv3Distance_Type=Integer32
_ZyOspfv3Distance_Object=MibScalar
zyOspfv3Distance=_ZyOspfv3Distance_Object((1,3,6,1,4,1,890,1,15,3,117,1,2,1),_ZyOspfv3Distance_Type())
zyOspfv3Distance.setMaxAccess(_B)
if mibBuilder.loadTexts:zyOspfv3Distance.setStatus(_A)
_ZyxelOspfv3Notifications_ObjectIdentity=ObjectIdentity
zyxelOspfv3Notifications=_ZyxelOspfv3Notifications_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,117,4))
zyOspfv3ExceedMaxDynamicRoutePath=NotificationType((1,3,6,1,4,1,890,1,15,3,117,4,1))
if mibBuilder.loadTexts:zyOspfv3ExceedMaxDynamicRoutePath.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'zyxelOspfv3':zyxelOspfv3,'zyxelOspfv3Setup':zyxelOspfv3Setup,'zyxelOspfv3RedistributeRouteTable':zyxelOspfv3RedistributeRouteTable,'zyxelOspfv3RedistributeRouteEntry':zyxelOspfv3RedistributeRouteEntry,_E:zyOspfv3RedistributeRouteProtocol,'zyOspfv3RedistributeRouteState':zyOspfv3RedistributeRouteState,'zyOspfv3RedistributeRouteType':zyOspfv3RedistributeRouteType,'zyOspfv3RedistributeRouteMetric':zyOspfv3RedistributeRouteMetric,'zyxelOspfv3GeneralGroup':zyxelOspfv3GeneralGroup,'zyOspfv3Distance':zyOspfv3Distance,'zyxelOspfv3Notifications':zyxelOspfv3Notifications,'zyOspfv3ExceedMaxDynamicRoutePath':zyOspfv3ExceedMaxDynamicRoutePath})