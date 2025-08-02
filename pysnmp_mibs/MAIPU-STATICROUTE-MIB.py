_N='staticGwRouteGwVrfName'
_M='staticGwRouteGw'
_L='staticGwRouteMask'
_K='staticGwRouteDest'
_J='staticGwRouteVrfName'
_I='staticIfRouteIfName'
_H='staticIfRouteMask'
_G='staticIfRouteDest'
_F='staticIfRouteVrfName'
_E='Integer32'
_D='DisplayString'
_C='MAIPU-STATICROUTE-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mpMgmt,=mibBuilder.importSymbols('MAIPU-SMI','mpMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,ObjectName,ObjectSyntax,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','ObjectName','ObjectSyntax','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_D,'MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
_RouteMib_ObjectIdentity=ObjectIdentity
routeMib=_RouteMib_ObjectIdentity((1,3,6,1,4,1,5651,3,81))
_StaticRoute_ObjectIdentity=ObjectIdentity
staticRoute=_StaticRoute_ObjectIdentity((1,3,6,1,4,1,5651,3,81,7))
_StaticIfRouteTable_Object=MibTable
staticIfRouteTable=_StaticIfRouteTable_Object((1,3,6,1,4,1,5651,3,81,7,1))
if mibBuilder.loadTexts:staticIfRouteTable.setStatus(_A)
_StaticIfRouteEntry_Object=MibTableRow
staticIfRouteEntry=_StaticIfRouteEntry_Object((1,3,6,1,4,1,5651,3,81,7,1,1))
staticIfRouteEntry.setIndexNames((0,_C,_F),(0,_C,_G),(0,_C,_H),(0,_C,_I))
if mibBuilder.loadTexts:staticIfRouteEntry.setStatus(_A)
class _StaticIfRouteVrfName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_StaticIfRouteVrfName_Type.__name__=_D
_StaticIfRouteVrfName_Object=MibScalar
staticIfRouteVrfName=_StaticIfRouteVrfName_Object((1,3,6,1,4,1,5651,3,81,7,1,1,1),_StaticIfRouteVrfName_Type())
staticIfRouteVrfName.setMaxAccess(_B)
if mibBuilder.loadTexts:staticIfRouteVrfName.setStatus(_A)
_StaticIfRouteDest_Type=IpAddress
_StaticIfRouteDest_Object=MibScalar
staticIfRouteDest=_StaticIfRouteDest_Object((1,3,6,1,4,1,5651,3,81,7,1,1,2),_StaticIfRouteDest_Type())
staticIfRouteDest.setMaxAccess(_B)
if mibBuilder.loadTexts:staticIfRouteDest.setStatus(_A)
_StaticIfRouteMask_Type=IpAddress
_StaticIfRouteMask_Object=MibScalar
staticIfRouteMask=_StaticIfRouteMask_Object((1,3,6,1,4,1,5651,3,81,7,1,1,3),_StaticIfRouteMask_Type())
staticIfRouteMask.setMaxAccess(_B)
if mibBuilder.loadTexts:staticIfRouteMask.setStatus(_A)
class _StaticIfRouteIfName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_StaticIfRouteIfName_Type.__name__=_D
_StaticIfRouteIfName_Object=MibScalar
staticIfRouteIfName=_StaticIfRouteIfName_Object((1,3,6,1,4,1,5651,3,81,7,1,1,4),_StaticIfRouteIfName_Type())
staticIfRouteIfName.setMaxAccess(_B)
if mibBuilder.loadTexts:staticIfRouteIfName.setStatus(_A)
class _StaticIfRouteDistance_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_StaticIfRouteDistance_Type.__name__=_E
_StaticIfRouteDistance_Object=MibScalar
staticIfRouteDistance=_StaticIfRouteDistance_Object((1,3,6,1,4,1,5651,3,81,7,1,1,5),_StaticIfRouteDistance_Type())
staticIfRouteDistance.setMaxAccess(_B)
if mibBuilder.loadTexts:staticIfRouteDistance.setStatus(_A)
_StaticIfRouteRowStatus_Type=RowStatus
_StaticIfRouteRowStatus_Object=MibScalar
staticIfRouteRowStatus=_StaticIfRouteRowStatus_Object((1,3,6,1,4,1,5651,3,81,7,1,1,6),_StaticIfRouteRowStatus_Type())
staticIfRouteRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:staticIfRouteRowStatus.setStatus(_A)
_StaticGwRouteTable_Object=MibTable
staticGwRouteTable=_StaticGwRouteTable_Object((1,3,6,1,4,1,5651,3,81,7,2))
if mibBuilder.loadTexts:staticGwRouteTable.setStatus(_A)
_StaticGwRouteEntry_Object=MibTableRow
staticGwRouteEntry=_StaticGwRouteEntry_Object((1,3,6,1,4,1,5651,3,81,7,2,1))
staticGwRouteEntry.setIndexNames((0,_C,_J),(0,_C,_K),(0,_C,_L),(0,_C,_M),(0,_C,_N))
if mibBuilder.loadTexts:staticGwRouteEntry.setStatus(_A)
class _StaticGwRouteVrfName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_StaticGwRouteVrfName_Type.__name__=_D
_StaticGwRouteVrfName_Object=MibScalar
staticGwRouteVrfName=_StaticGwRouteVrfName_Object((1,3,6,1,4,1,5651,3,81,7,2,1,1),_StaticGwRouteVrfName_Type())
staticGwRouteVrfName.setMaxAccess(_B)
if mibBuilder.loadTexts:staticGwRouteVrfName.setStatus(_A)
_StaticGwRouteDest_Type=IpAddress
_StaticGwRouteDest_Object=MibScalar
staticGwRouteDest=_StaticGwRouteDest_Object((1,3,6,1,4,1,5651,3,81,7,2,1,2),_StaticGwRouteDest_Type())
staticGwRouteDest.setMaxAccess(_B)
if mibBuilder.loadTexts:staticGwRouteDest.setStatus(_A)
_StaticGwRouteMask_Type=IpAddress
_StaticGwRouteMask_Object=MibScalar
staticGwRouteMask=_StaticGwRouteMask_Object((1,3,6,1,4,1,5651,3,81,7,2,1,3),_StaticGwRouteMask_Type())
staticGwRouteMask.setMaxAccess(_B)
if mibBuilder.loadTexts:staticGwRouteMask.setStatus(_A)
_StaticGwRouteGw_Type=IpAddress
_StaticGwRouteGw_Object=MibScalar
staticGwRouteGw=_StaticGwRouteGw_Object((1,3,6,1,4,1,5651,3,81,7,2,1,4),_StaticGwRouteGw_Type())
staticGwRouteGw.setMaxAccess(_B)
if mibBuilder.loadTexts:staticGwRouteGw.setStatus(_A)
class _StaticGwRouteGwVrfName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_StaticGwRouteGwVrfName_Type.__name__=_D
_StaticGwRouteGwVrfName_Object=MibScalar
staticGwRouteGwVrfName=_StaticGwRouteGwVrfName_Object((1,3,6,1,4,1,5651,3,81,7,2,1,5),_StaticGwRouteGwVrfName_Type())
staticGwRouteGwVrfName.setMaxAccess(_B)
if mibBuilder.loadTexts:staticGwRouteGwVrfName.setStatus(_A)
class _StaticGwRouteDistance_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_StaticGwRouteDistance_Type.__name__=_E
_StaticGwRouteDistance_Object=MibScalar
staticGwRouteDistance=_StaticGwRouteDistance_Object((1,3,6,1,4,1,5651,3,81,7,2,1,6),_StaticGwRouteDistance_Type())
staticGwRouteDistance.setMaxAccess(_B)
if mibBuilder.loadTexts:staticGwRouteDistance.setStatus(_A)
_StaticGwRouteRowStatus_Type=RowStatus
_StaticGwRouteRowStatus_Object=MibScalar
staticGwRouteRowStatus=_StaticGwRouteRowStatus_Object((1,3,6,1,4,1,5651,3,81,7,2,1,7),_StaticGwRouteRowStatus_Type())
staticGwRouteRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:staticGwRouteRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'routeMib':routeMib,'staticRoute':staticRoute,'staticIfRouteTable':staticIfRouteTable,'staticIfRouteEntry':staticIfRouteEntry,_F:staticIfRouteVrfName,_G:staticIfRouteDest,_H:staticIfRouteMask,_I:staticIfRouteIfName,'staticIfRouteDistance':staticIfRouteDistance,'staticIfRouteRowStatus':staticIfRouteRowStatus,'staticGwRouteTable':staticGwRouteTable,'staticGwRouteEntry':staticGwRouteEntry,_J:staticGwRouteVrfName,_K:staticGwRouteDest,_L:staticGwRouteMask,_M:staticGwRouteGw,_N:staticGwRouteGwVrfName,'staticGwRouteDistance':staticGwRouteDistance,'staticGwRouteRowStatus':staticGwRouteRowStatus})