_O='InterfaceIndex'
_N='futOspfExtRouteTOS'
_M='futOspfExtRouteMask'
_L='futOspfExtRouteDest'
_K='futOspfBRRouteDestType'
_J='futOspfBRRouteIpNextHop'
_I='futOspfBRRouteIpTos'
_H='futOspfBRRouteIpAddrMask'
_G='futOspfBRRouteIpAddr'
_F='read-only'
_E='Integer32'
_D='read-create'
_C='not-accessible'
_B='SUPERMICRO-OSPF-TEST-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
futOspfTestGroup=ModuleIdentity((1,3,6,1,4,1,10876,101,1,10,100))
if mibBuilder.loadTexts:futOspfTestGroup.setRevisions(('2012-09-05 00:00',))
class BigMetric(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16777215))
class InterfaceIndex(TextualConvention,Integer32):status=_A;displayHint='d'
class TOSType(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,30))
_FutOspfBRRouteTable_Object=MibTable
futOspfBRRouteTable=_FutOspfBRRouteTable_Object((1,3,6,1,4,1,10876,101,1,10,100,1))
if mibBuilder.loadTexts:futOspfBRRouteTable.setStatus(_A)
_FutOspfBRRouteEntry_Object=MibTableRow
futOspfBRRouteEntry=_FutOspfBRRouteEntry_Object((1,3,6,1,4,1,10876,101,1,10,100,1,1))
futOspfBRRouteEntry.setIndexNames((0,_B,_G),(0,_B,_H),(0,_B,_I),(0,_B,_J),(0,_B,_K))
if mibBuilder.loadTexts:futOspfBRRouteEntry.setStatus(_A)
_FutOspfBRRouteIpAddr_Type=IpAddress
_FutOspfBRRouteIpAddr_Object=MibTableColumn
futOspfBRRouteIpAddr=_FutOspfBRRouteIpAddr_Object((1,3,6,1,4,1,10876,101,1,10,100,1,1,1),_FutOspfBRRouteIpAddr_Type())
futOspfBRRouteIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:futOspfBRRouteIpAddr.setStatus(_A)
_FutOspfBRRouteIpAddrMask_Type=IpAddress
_FutOspfBRRouteIpAddrMask_Object=MibTableColumn
futOspfBRRouteIpAddrMask=_FutOspfBRRouteIpAddrMask_Object((1,3,6,1,4,1,10876,101,1,10,100,1,1,2),_FutOspfBRRouteIpAddrMask_Type())
futOspfBRRouteIpAddrMask.setMaxAccess(_C)
if mibBuilder.loadTexts:futOspfBRRouteIpAddrMask.setStatus(_A)
_FutOspfBRRouteIpTos_Type=Unsigned32
_FutOspfBRRouteIpTos_Object=MibTableColumn
futOspfBRRouteIpTos=_FutOspfBRRouteIpTos_Object((1,3,6,1,4,1,10876,101,1,10,100,1,1,3),_FutOspfBRRouteIpTos_Type())
futOspfBRRouteIpTos.setMaxAccess(_C)
if mibBuilder.loadTexts:futOspfBRRouteIpTos.setStatus(_A)
_FutOspfBRRouteIpNextHop_Type=IpAddress
_FutOspfBRRouteIpNextHop_Object=MibTableColumn
futOspfBRRouteIpNextHop=_FutOspfBRRouteIpNextHop_Object((1,3,6,1,4,1,10876,101,1,10,100,1,1,4),_FutOspfBRRouteIpNextHop_Type())
futOspfBRRouteIpNextHop.setMaxAccess(_C)
if mibBuilder.loadTexts:futOspfBRRouteIpNextHop.setStatus(_A)
class _FutOspfBRRouteDestType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*(('areaBorder',2),('asBoundary',3)))
_FutOspfBRRouteDestType_Type.__name__=_E
_FutOspfBRRouteDestType_Object=MibTableColumn
futOspfBRRouteDestType=_FutOspfBRRouteDestType_Object((1,3,6,1,4,1,10876,101,1,10,100,1,1,5),_FutOspfBRRouteDestType_Type())
futOspfBRRouteDestType.setMaxAccess(_C)
if mibBuilder.loadTexts:futOspfBRRouteDestType.setStatus(_A)
class _FutOspfBRRouteType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('intraArea',1),('interArea',2)))
_FutOspfBRRouteType_Type.__name__=_E
_FutOspfBRRouteType_Object=MibTableColumn
futOspfBRRouteType=_FutOspfBRRouteType_Object((1,3,6,1,4,1,10876,101,1,10,100,1,1,6),_FutOspfBRRouteType_Type())
futOspfBRRouteType.setMaxAccess(_F)
if mibBuilder.loadTexts:futOspfBRRouteType.setStatus(_A)
_FutOspfBRRouteAreaId_Type=IpAddress
_FutOspfBRRouteAreaId_Object=MibTableColumn
futOspfBRRouteAreaId=_FutOspfBRRouteAreaId_Object((1,3,6,1,4,1,10876,101,1,10,100,1,1,7),_FutOspfBRRouteAreaId_Type())
futOspfBRRouteAreaId.setMaxAccess(_F)
if mibBuilder.loadTexts:futOspfBRRouteAreaId.setStatus(_A)
_FutOspfBRRouteCost_Type=BigMetric
_FutOspfBRRouteCost_Object=MibTableColumn
futOspfBRRouteCost=_FutOspfBRRouteCost_Object((1,3,6,1,4,1,10876,101,1,10,100,1,1,8),_FutOspfBRRouteCost_Type())
futOspfBRRouteCost.setMaxAccess(_F)
if mibBuilder.loadTexts:futOspfBRRouteCost.setStatus(_A)
_FutOspfBRRouteInterfaceIndex_Type=InterfaceIndex
_FutOspfBRRouteInterfaceIndex_Object=MibTableColumn
futOspfBRRouteInterfaceIndex=_FutOspfBRRouteInterfaceIndex_Object((1,3,6,1,4,1,10876,101,1,10,100,1,1,9),_FutOspfBRRouteInterfaceIndex_Type())
futOspfBRRouteInterfaceIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:futOspfBRRouteInterfaceIndex.setStatus(_A)
_FutOspfExtRouteTable_Object=MibTable
futOspfExtRouteTable=_FutOspfExtRouteTable_Object((1,3,6,1,4,1,10876,101,1,10,100,2))
if mibBuilder.loadTexts:futOspfExtRouteTable.setStatus(_A)
_FutOspfExtRouteEntry_Object=MibTableRow
futOspfExtRouteEntry=_FutOspfExtRouteEntry_Object((1,3,6,1,4,1,10876,101,1,10,100,2,1))
futOspfExtRouteEntry.setIndexNames((0,_B,_L),(0,_B,_M),(0,_B,_N))
if mibBuilder.loadTexts:futOspfExtRouteEntry.setStatus(_A)
_FutOspfExtRouteDest_Type=IpAddress
_FutOspfExtRouteDest_Object=MibTableColumn
futOspfExtRouteDest=_FutOspfExtRouteDest_Object((1,3,6,1,4,1,10876,101,1,10,100,2,1,1),_FutOspfExtRouteDest_Type())
futOspfExtRouteDest.setMaxAccess(_C)
if mibBuilder.loadTexts:futOspfExtRouteDest.setStatus(_A)
_FutOspfExtRouteMask_Type=IpAddress
_FutOspfExtRouteMask_Object=MibTableColumn
futOspfExtRouteMask=_FutOspfExtRouteMask_Object((1,3,6,1,4,1,10876,101,1,10,100,2,1,2),_FutOspfExtRouteMask_Type())
futOspfExtRouteMask.setMaxAccess(_C)
if mibBuilder.loadTexts:futOspfExtRouteMask.setStatus(_A)
_FutOspfExtRouteTOS_Type=TOSType
_FutOspfExtRouteTOS_Object=MibTableColumn
futOspfExtRouteTOS=_FutOspfExtRouteTOS_Object((1,3,6,1,4,1,10876,101,1,10,100,2,1,3),_FutOspfExtRouteTOS_Type())
futOspfExtRouteTOS.setMaxAccess(_C)
if mibBuilder.loadTexts:futOspfExtRouteTOS.setStatus(_A)
_FutOspfExtRouteMetric_Type=BigMetric
_FutOspfExtRouteMetric_Object=MibTableColumn
futOspfExtRouteMetric=_FutOspfExtRouteMetric_Object((1,3,6,1,4,1,10876,101,1,10,100,2,1,4),_FutOspfExtRouteMetric_Type())
futOspfExtRouteMetric.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfExtRouteMetric.setStatus(_A)
class _FutOspfExtRouteMetricType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('asexttype1',1),('asexttype2',2)))
_FutOspfExtRouteMetricType_Type.__name__=_E
_FutOspfExtRouteMetricType_Object=MibTableColumn
futOspfExtRouteMetricType=_FutOspfExtRouteMetricType_Object((1,3,6,1,4,1,10876,101,1,10,100,2,1,5),_FutOspfExtRouteMetricType_Type())
futOspfExtRouteMetricType.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfExtRouteMetricType.setStatus(_A)
class _FutOspfExtRouteTag_Type(Integer32):defaultValue=0
_FutOspfExtRouteTag_Type.__name__=_E
_FutOspfExtRouteTag_Object=MibTableColumn
futOspfExtRouteTag=_FutOspfExtRouteTag_Object((1,3,6,1,4,1,10876,101,1,10,100,2,1,6),_FutOspfExtRouteTag_Type())
futOspfExtRouteTag.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfExtRouteTag.setStatus(_A)
_FutOspfExtRouteFwdAdr_Type=IpAddress
_FutOspfExtRouteFwdAdr_Object=MibTableColumn
futOspfExtRouteFwdAdr=_FutOspfExtRouteFwdAdr_Object((1,3,6,1,4,1,10876,101,1,10,100,2,1,7),_FutOspfExtRouteFwdAdr_Type())
futOspfExtRouteFwdAdr.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfExtRouteFwdAdr.setStatus(_A)
class _FutOspfExtRouteIfIndex_Type(InterfaceIndex):defaultValue=0;subtypeSpec=InterfaceIndex.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FutOspfExtRouteIfIndex_Type.__name__=_O
_FutOspfExtRouteIfIndex_Object=MibTableColumn
futOspfExtRouteIfIndex=_FutOspfExtRouteIfIndex_Object((1,3,6,1,4,1,10876,101,1,10,100,2,1,8),_FutOspfExtRouteIfIndex_Type())
futOspfExtRouteIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfExtRouteIfIndex.setStatus(_A)
_FutOspfExtRouteNextHop_Type=IpAddress
_FutOspfExtRouteNextHop_Object=MibTableColumn
futOspfExtRouteNextHop=_FutOspfExtRouteNextHop_Object((1,3,6,1,4,1,10876,101,1,10,100,2,1,9),_FutOspfExtRouteNextHop_Type())
futOspfExtRouteNextHop.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfExtRouteNextHop.setStatus(_A)
_FutOspfExtRouteStatus_Type=RowStatus
_FutOspfExtRouteStatus_Object=MibTableColumn
futOspfExtRouteStatus=_FutOspfExtRouteStatus_Object((1,3,6,1,4,1,10876,101,1,10,100,2,1,10),_FutOspfExtRouteStatus_Type())
futOspfExtRouteStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:futOspfExtRouteStatus.setStatus(_A)
_FutOspfGrTestGroup_ObjectIdentity=ObjectIdentity
futOspfGrTestGroup=_FutOspfGrTestGroup_ObjectIdentity((1,3,6,1,4,1,10876,101,1,10,100,100))
class _FutOspfGrShutdown_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('none',1),('unplanned',2)))
_FutOspfGrShutdown_Type.__name__=_E
_FutOspfGrShutdown_Object=MibScalar
futOspfGrShutdown=_FutOspfGrShutdown_Object((1,3,6,1,4,1,10876,101,1,10,100,100,1),_FutOspfGrShutdown_Type())
futOspfGrShutdown.setMaxAccess('read-write')
if mibBuilder.loadTexts:futOspfGrShutdown.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'BigMetric':BigMetric,_O:InterfaceIndex,'TOSType':TOSType,'futOspfTestGroup':futOspfTestGroup,'futOspfBRRouteTable':futOspfBRRouteTable,'futOspfBRRouteEntry':futOspfBRRouteEntry,_G:futOspfBRRouteIpAddr,_H:futOspfBRRouteIpAddrMask,_I:futOspfBRRouteIpTos,_J:futOspfBRRouteIpNextHop,_K:futOspfBRRouteDestType,'futOspfBRRouteType':futOspfBRRouteType,'futOspfBRRouteAreaId':futOspfBRRouteAreaId,'futOspfBRRouteCost':futOspfBRRouteCost,'futOspfBRRouteInterfaceIndex':futOspfBRRouteInterfaceIndex,'futOspfExtRouteTable':futOspfExtRouteTable,'futOspfExtRouteEntry':futOspfExtRouteEntry,_L:futOspfExtRouteDest,_M:futOspfExtRouteMask,_N:futOspfExtRouteTOS,'futOspfExtRouteMetric':futOspfExtRouteMetric,'futOspfExtRouteMetricType':futOspfExtRouteMetricType,'futOspfExtRouteTag':futOspfExtRouteTag,'futOspfExtRouteFwdAdr':futOspfExtRouteFwdAdr,'futOspfExtRouteIfIndex':futOspfExtRouteIfIndex,'futOspfExtRouteNextHop':futOspfExtRouteNextHop,'futOspfExtRouteStatus':futOspfExtRouteStatus,'futOspfGrTestGroup':futOspfGrTestGroup,'futOspfGrShutdown':futOspfGrShutdown})