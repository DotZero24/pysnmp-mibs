_G='read-write'
_F='zyStaticRouteGateway'
_E='zyStaticRouteSubnetMask'
_D='zyStaticRouteIpAddress'
_C='not-accessible'
_B='ZYXEL-STATIC-ROUTE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
esMgmt,=mibBuilder.importSymbols('ZYXEL-ES-SMI','esMgmt')
zyxelStaticRoute=ModuleIdentity((1,3,6,1,4,1,890,1,15,3,77))
_ZyxelStaticRouteSetup_ObjectIdentity=ObjectIdentity
zyxelStaticRouteSetup=_ZyxelStaticRouteSetup_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,77,1))
_ZyStaticRouteMaxNumberOfRoutes_Type=Integer32
_ZyStaticRouteMaxNumberOfRoutes_Object=MibScalar
zyStaticRouteMaxNumberOfRoutes=_ZyStaticRouteMaxNumberOfRoutes_Object((1,3,6,1,4,1,890,1,15,3,77,1,1),_ZyStaticRouteMaxNumberOfRoutes_Type())
zyStaticRouteMaxNumberOfRoutes.setMaxAccess('read-only')
if mibBuilder.loadTexts:zyStaticRouteMaxNumberOfRoutes.setStatus(_A)
_ZyxelStaticRouteTable_Object=MibTable
zyxelStaticRouteTable=_ZyxelStaticRouteTable_Object((1,3,6,1,4,1,890,1,15,3,77,1,2))
if mibBuilder.loadTexts:zyxelStaticRouteTable.setStatus(_A)
_ZyxelStaticRouteEntry_Object=MibTableRow
zyxelStaticRouteEntry=_ZyxelStaticRouteEntry_Object((1,3,6,1,4,1,890,1,15,3,77,1,2,1))
zyxelStaticRouteEntry.setIndexNames((0,_B,_D),(0,_B,_E),(0,_B,_F))
if mibBuilder.loadTexts:zyxelStaticRouteEntry.setStatus(_A)
_ZyStaticRouteName_Type=DisplayString
_ZyStaticRouteName_Object=MibTableColumn
zyStaticRouteName=_ZyStaticRouteName_Object((1,3,6,1,4,1,890,1,15,3,77,1,2,1,1),_ZyStaticRouteName_Type())
zyStaticRouteName.setMaxAccess(_G)
if mibBuilder.loadTexts:zyStaticRouteName.setStatus(_A)
_ZyStaticRouteIpAddress_Type=IpAddress
_ZyStaticRouteIpAddress_Object=MibTableColumn
zyStaticRouteIpAddress=_ZyStaticRouteIpAddress_Object((1,3,6,1,4,1,890,1,15,3,77,1,2,1,2),_ZyStaticRouteIpAddress_Type())
zyStaticRouteIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:zyStaticRouteIpAddress.setStatus(_A)
_ZyStaticRouteSubnetMask_Type=IpAddress
_ZyStaticRouteSubnetMask_Object=MibTableColumn
zyStaticRouteSubnetMask=_ZyStaticRouteSubnetMask_Object((1,3,6,1,4,1,890,1,15,3,77,1,2,1,3),_ZyStaticRouteSubnetMask_Type())
zyStaticRouteSubnetMask.setMaxAccess(_C)
if mibBuilder.loadTexts:zyStaticRouteSubnetMask.setStatus(_A)
_ZyStaticRouteGateway_Type=IpAddress
_ZyStaticRouteGateway_Object=MibTableColumn
zyStaticRouteGateway=_ZyStaticRouteGateway_Object((1,3,6,1,4,1,890,1,15,3,77,1,2,1,4),_ZyStaticRouteGateway_Type())
zyStaticRouteGateway.setMaxAccess(_C)
if mibBuilder.loadTexts:zyStaticRouteGateway.setStatus(_A)
_ZyStaticRouteMetric_Type=Integer32
_ZyStaticRouteMetric_Object=MibTableColumn
zyStaticRouteMetric=_ZyStaticRouteMetric_Object((1,3,6,1,4,1,890,1,15,3,77,1,2,1,5),_ZyStaticRouteMetric_Type())
zyStaticRouteMetric.setMaxAccess(_G)
if mibBuilder.loadTexts:zyStaticRouteMetric.setStatus(_A)
_ZyStaticRouteRowStatus_Type=RowStatus
_ZyStaticRouteRowStatus_Object=MibTableColumn
zyStaticRouteRowStatus=_ZyStaticRouteRowStatus_Object((1,3,6,1,4,1,890,1,15,3,77,1,2,1,6),_ZyStaticRouteRowStatus_Type())
zyStaticRouteRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:zyStaticRouteRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'zyxelStaticRoute':zyxelStaticRoute,'zyxelStaticRouteSetup':zyxelStaticRouteSetup,'zyStaticRouteMaxNumberOfRoutes':zyStaticRouteMaxNumberOfRoutes,'zyxelStaticRouteTable':zyxelStaticRouteTable,'zyxelStaticRouteEntry':zyxelStaticRouteEntry,'zyStaticRouteName':zyStaticRouteName,_D:zyStaticRouteIpAddress,_E:zyStaticRouteSubnetMask,_F:zyStaticRouteGateway,'zyStaticRouteMetric':zyStaticRouteMetric,'zyStaticRouteRowStatus':zyStaticRouteRowStatus})