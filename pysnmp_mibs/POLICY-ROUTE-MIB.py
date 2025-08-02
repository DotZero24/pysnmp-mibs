_E='swPolicyRouteName'
_D='POLICY-ROUTE-MIB'
_C='DisplayString'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dlink_common_mgmt,=mibBuilder.importSymbols('DLINK-ID-REC-MIB','dlink-common-mgmt')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_C,'MacAddress','PhysAddress','RowStatus','TextualConvention')
swPolicyRouteMIB=ModuleIdentity((1,3,6,1,4,1,171,12,32))
_SwPolicyRouteCtrl_ObjectIdentity=ObjectIdentity
swPolicyRouteCtrl=_SwPolicyRouteCtrl_ObjectIdentity((1,3,6,1,4,1,171,12,32,1))
_SwPolicyRouteInfo_ObjectIdentity=ObjectIdentity
swPolicyRouteInfo=_SwPolicyRouteInfo_ObjectIdentity((1,3,6,1,4,1,171,12,32,2))
_SwPolicyRouteMgmt_ObjectIdentity=ObjectIdentity
swPolicyRouteMgmt=_SwPolicyRouteMgmt_ObjectIdentity((1,3,6,1,4,1,171,12,32,3))
_SwPolicyRouteTable_Object=MibTable
swPolicyRouteTable=_SwPolicyRouteTable_Object((1,3,6,1,4,1,171,12,32,3,1))
if mibBuilder.loadTexts:swPolicyRouteTable.setStatus(_A)
_SwPolicyRouteEntry_Object=MibTableRow
swPolicyRouteEntry=_SwPolicyRouteEntry_Object((1,3,6,1,4,1,171,12,32,3,1,1))
swPolicyRouteEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:swPolicyRouteEntry.setStatus(_A)
class _SwPolicyRouteName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_SwPolicyRouteName_Type.__name__=_C
_SwPolicyRouteName_Object=MibTableColumn
swPolicyRouteName=_SwPolicyRouteName_Object((1,3,6,1,4,1,171,12,32,3,1,1,1),_SwPolicyRouteName_Type())
swPolicyRouteName.setMaxAccess('read-only')
if mibBuilder.loadTexts:swPolicyRouteName.setStatus(_A)
_SwPolicyRouteProfileId_Type=Integer32
_SwPolicyRouteProfileId_Object=MibTableColumn
swPolicyRouteProfileId=_SwPolicyRouteProfileId_Object((1,3,6,1,4,1,171,12,32,3,1,1,2),_SwPolicyRouteProfileId_Type())
swPolicyRouteProfileId.setMaxAccess(_B)
if mibBuilder.loadTexts:swPolicyRouteProfileId.setStatus(_A)
_SwPolicyRouteAccessId_Type=Integer32
_SwPolicyRouteAccessId_Object=MibTableColumn
swPolicyRouteAccessId=_SwPolicyRouteAccessId_Object((1,3,6,1,4,1,171,12,32,3,1,1,3),_SwPolicyRouteAccessId_Type())
swPolicyRouteAccessId.setMaxAccess(_B)
if mibBuilder.loadTexts:swPolicyRouteAccessId.setStatus(_A)
_SwPolicyRouteNextHop_Type=IpAddress
_SwPolicyRouteNextHop_Object=MibTableColumn
swPolicyRouteNextHop=_SwPolicyRouteNextHop_Object((1,3,6,1,4,1,171,12,32,3,1,1,4),_SwPolicyRouteNextHop_Type())
swPolicyRouteNextHop.setMaxAccess(_B)
if mibBuilder.loadTexts:swPolicyRouteNextHop.setStatus(_A)
_SwPolicyRouteRowStatus_Type=RowStatus
_SwPolicyRouteRowStatus_Object=MibTableColumn
swPolicyRouteRowStatus=_SwPolicyRouteRowStatus_Object((1,3,6,1,4,1,171,12,32,3,1,1,5),_SwPolicyRouteRowStatus_Type())
swPolicyRouteRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:swPolicyRouteRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'swPolicyRouteMIB':swPolicyRouteMIB,'swPolicyRouteCtrl':swPolicyRouteCtrl,'swPolicyRouteInfo':swPolicyRouteInfo,'swPolicyRouteMgmt':swPolicyRouteMgmt,'swPolicyRouteTable':swPolicyRouteTable,'swPolicyRouteEntry':swPolicyRouteEntry,_E:swPolicyRouteName,'swPolicyRouteProfileId':swPolicyRouteProfileId,'swPolicyRouteAccessId':swPolicyRouteAccessId,'swPolicyRouteNextHop':swPolicyRouteNextHop,'swPolicyRouteRowStatus':swPolicyRouteRowStatus})