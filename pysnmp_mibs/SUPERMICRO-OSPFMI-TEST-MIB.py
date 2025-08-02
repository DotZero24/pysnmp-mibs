_P='fsMIOspfExtRouteTOS'
_O='fsMIOspfExtRouteMask'
_N='fsMIOspfExtRouteDest'
_M='fsMIOspfBRRouteDestType'
_L='fsMIOspfBRRouteIpNextHop'
_K='fsMIOspfBRRouteIpTos'
_J='fsMIOspfBRRouteIpAddrMask'
_I='fsMIOspfBRRouteIpAddr'
_H='read-only'
_G='fsMIStdOspfContextId'
_F='SUPERMICRO-MISTDOSPF-MIB'
_E='read-create'
_D='not-accessible'
_C='Integer32'
_B='SUPERMICRO-OSPFMI-TEST-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
BigMetric,TOSType,fsMIStdOspfContextId=mibBuilder.importSymbols(_F,'BigMetric','TOSType',_G)
fsMIOspfTestGroup=ModuleIdentity((1,3,6,1,4,1,10876,101,1,147))
if mibBuilder.loadTexts:fsMIOspfTestGroup.setRevisions(('2012-09-05 00:00',))
_FsMIOspfBRRouteTable_Object=MibTable
fsMIOspfBRRouteTable=_FsMIOspfBRRouteTable_Object((1,3,6,1,4,1,10876,101,1,147,1))
if mibBuilder.loadTexts:fsMIOspfBRRouteTable.setStatus(_A)
_FsMIOspfBRRouteEntry_Object=MibTableRow
fsMIOspfBRRouteEntry=_FsMIOspfBRRouteEntry_Object((1,3,6,1,4,1,10876,101,1,147,1,1))
fsMIOspfBRRouteEntry.setIndexNames((0,_F,_G),(0,_B,_I),(0,_B,_J),(0,_B,_K),(0,_B,_L),(0,_B,_M))
if mibBuilder.loadTexts:fsMIOspfBRRouteEntry.setStatus(_A)
_FsMIOspfBRRouteIpAddr_Type=IpAddress
_FsMIOspfBRRouteIpAddr_Object=MibTableColumn
fsMIOspfBRRouteIpAddr=_FsMIOspfBRRouteIpAddr_Object((1,3,6,1,4,1,10876,101,1,147,1,1,1),_FsMIOspfBRRouteIpAddr_Type())
fsMIOspfBRRouteIpAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfBRRouteIpAddr.setStatus(_A)
_FsMIOspfBRRouteIpAddrMask_Type=IpAddress
_FsMIOspfBRRouteIpAddrMask_Object=MibTableColumn
fsMIOspfBRRouteIpAddrMask=_FsMIOspfBRRouteIpAddrMask_Object((1,3,6,1,4,1,10876,101,1,147,1,1,2),_FsMIOspfBRRouteIpAddrMask_Type())
fsMIOspfBRRouteIpAddrMask.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfBRRouteIpAddrMask.setStatus(_A)
_FsMIOspfBRRouteIpTos_Type=Unsigned32
_FsMIOspfBRRouteIpTos_Object=MibTableColumn
fsMIOspfBRRouteIpTos=_FsMIOspfBRRouteIpTos_Object((1,3,6,1,4,1,10876,101,1,147,1,1,3),_FsMIOspfBRRouteIpTos_Type())
fsMIOspfBRRouteIpTos.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfBRRouteIpTos.setStatus(_A)
_FsMIOspfBRRouteIpNextHop_Type=IpAddress
_FsMIOspfBRRouteIpNextHop_Object=MibTableColumn
fsMIOspfBRRouteIpNextHop=_FsMIOspfBRRouteIpNextHop_Object((1,3,6,1,4,1,10876,101,1,147,1,1,4),_FsMIOspfBRRouteIpNextHop_Type())
fsMIOspfBRRouteIpNextHop.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfBRRouteIpNextHop.setStatus(_A)
class _FsMIOspfBRRouteDestType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*(('areaBorder',2),('asBoundary',3)))
_FsMIOspfBRRouteDestType_Type.__name__=_C
_FsMIOspfBRRouteDestType_Object=MibTableColumn
fsMIOspfBRRouteDestType=_FsMIOspfBRRouteDestType_Object((1,3,6,1,4,1,10876,101,1,147,1,1,5),_FsMIOspfBRRouteDestType_Type())
fsMIOspfBRRouteDestType.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfBRRouteDestType.setStatus(_A)
class _FsMIOspfBRRouteType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('intraArea',1),('interArea',2)))
_FsMIOspfBRRouteType_Type.__name__=_C
_FsMIOspfBRRouteType_Object=MibTableColumn
fsMIOspfBRRouteType=_FsMIOspfBRRouteType_Object((1,3,6,1,4,1,10876,101,1,147,1,1,6),_FsMIOspfBRRouteType_Type())
fsMIOspfBRRouteType.setMaxAccess(_H)
if mibBuilder.loadTexts:fsMIOspfBRRouteType.setStatus(_A)
_FsMIOspfBRRouteAreaId_Type=IpAddress
_FsMIOspfBRRouteAreaId_Object=MibTableColumn
fsMIOspfBRRouteAreaId=_FsMIOspfBRRouteAreaId_Object((1,3,6,1,4,1,10876,101,1,147,1,1,7),_FsMIOspfBRRouteAreaId_Type())
fsMIOspfBRRouteAreaId.setMaxAccess(_H)
if mibBuilder.loadTexts:fsMIOspfBRRouteAreaId.setStatus(_A)
_FsMIOspfBRRouteCost_Type=BigMetric
_FsMIOspfBRRouteCost_Object=MibTableColumn
fsMIOspfBRRouteCost=_FsMIOspfBRRouteCost_Object((1,3,6,1,4,1,10876,101,1,147,1,1,8),_FsMIOspfBRRouteCost_Type())
fsMIOspfBRRouteCost.setMaxAccess(_H)
if mibBuilder.loadTexts:fsMIOspfBRRouteCost.setStatus(_A)
class _FsMIOspfBRRouteInterfaceIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsMIOspfBRRouteInterfaceIndex_Type.__name__=_C
_FsMIOspfBRRouteInterfaceIndex_Object=MibTableColumn
fsMIOspfBRRouteInterfaceIndex=_FsMIOspfBRRouteInterfaceIndex_Object((1,3,6,1,4,1,10876,101,1,147,1,1,9),_FsMIOspfBRRouteInterfaceIndex_Type())
fsMIOspfBRRouteInterfaceIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:fsMIOspfBRRouteInterfaceIndex.setStatus(_A)
_FsMIOspfExtRouteTable_Object=MibTable
fsMIOspfExtRouteTable=_FsMIOspfExtRouteTable_Object((1,3,6,1,4,1,10876,101,1,147,2))
if mibBuilder.loadTexts:fsMIOspfExtRouteTable.setStatus(_A)
_FsMIOspfExtRouteEntry_Object=MibTableRow
fsMIOspfExtRouteEntry=_FsMIOspfExtRouteEntry_Object((1,3,6,1,4,1,10876,101,1,147,2,1))
fsMIOspfExtRouteEntry.setIndexNames((0,_F,_G),(0,_B,_N),(0,_B,_O),(0,_B,_P))
if mibBuilder.loadTexts:fsMIOspfExtRouteEntry.setStatus(_A)
_FsMIOspfExtRouteDest_Type=IpAddress
_FsMIOspfExtRouteDest_Object=MibTableColumn
fsMIOspfExtRouteDest=_FsMIOspfExtRouteDest_Object((1,3,6,1,4,1,10876,101,1,147,2,1,1),_FsMIOspfExtRouteDest_Type())
fsMIOspfExtRouteDest.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfExtRouteDest.setStatus(_A)
_FsMIOspfExtRouteMask_Type=IpAddress
_FsMIOspfExtRouteMask_Object=MibTableColumn
fsMIOspfExtRouteMask=_FsMIOspfExtRouteMask_Object((1,3,6,1,4,1,10876,101,1,147,2,1,2),_FsMIOspfExtRouteMask_Type())
fsMIOspfExtRouteMask.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfExtRouteMask.setStatus(_A)
_FsMIOspfExtRouteTOS_Type=TOSType
_FsMIOspfExtRouteTOS_Object=MibTableColumn
fsMIOspfExtRouteTOS=_FsMIOspfExtRouteTOS_Object((1,3,6,1,4,1,10876,101,1,147,2,1,3),_FsMIOspfExtRouteTOS_Type())
fsMIOspfExtRouteTOS.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIOspfExtRouteTOS.setStatus(_A)
_FsMIOspfExtRouteMetric_Type=BigMetric
_FsMIOspfExtRouteMetric_Object=MibTableColumn
fsMIOspfExtRouteMetric=_FsMIOspfExtRouteMetric_Object((1,3,6,1,4,1,10876,101,1,147,2,1,4),_FsMIOspfExtRouteMetric_Type())
fsMIOspfExtRouteMetric.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIOspfExtRouteMetric.setStatus(_A)
class _FsMIOspfExtRouteMetricType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('asexttype1',1),('asexttype2',2)))
_FsMIOspfExtRouteMetricType_Type.__name__=_C
_FsMIOspfExtRouteMetricType_Object=MibTableColumn
fsMIOspfExtRouteMetricType=_FsMIOspfExtRouteMetricType_Object((1,3,6,1,4,1,10876,101,1,147,2,1,5),_FsMIOspfExtRouteMetricType_Type())
fsMIOspfExtRouteMetricType.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIOspfExtRouteMetricType.setStatus(_A)
class _FsMIOspfExtRouteTag_Type(Integer32):defaultValue=0
_FsMIOspfExtRouteTag_Type.__name__=_C
_FsMIOspfExtRouteTag_Object=MibTableColumn
fsMIOspfExtRouteTag=_FsMIOspfExtRouteTag_Object((1,3,6,1,4,1,10876,101,1,147,2,1,6),_FsMIOspfExtRouteTag_Type())
fsMIOspfExtRouteTag.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIOspfExtRouteTag.setStatus(_A)
_FsMIOspfExtRouteFwdAdr_Type=IpAddress
_FsMIOspfExtRouteFwdAdr_Object=MibTableColumn
fsMIOspfExtRouteFwdAdr=_FsMIOspfExtRouteFwdAdr_Object((1,3,6,1,4,1,10876,101,1,147,2,1,7),_FsMIOspfExtRouteFwdAdr_Type())
fsMIOspfExtRouteFwdAdr.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIOspfExtRouteFwdAdr.setStatus(_A)
class _FsMIOspfExtRouteIfIndex_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsMIOspfExtRouteIfIndex_Type.__name__=_C
_FsMIOspfExtRouteIfIndex_Object=MibTableColumn
fsMIOspfExtRouteIfIndex=_FsMIOspfExtRouteIfIndex_Object((1,3,6,1,4,1,10876,101,1,147,2,1,8),_FsMIOspfExtRouteIfIndex_Type())
fsMIOspfExtRouteIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIOspfExtRouteIfIndex.setStatus(_A)
_FsMIOspfExtRouteNextHop_Type=IpAddress
_FsMIOspfExtRouteNextHop_Object=MibTableColumn
fsMIOspfExtRouteNextHop=_FsMIOspfExtRouteNextHop_Object((1,3,6,1,4,1,10876,101,1,147,2,1,9),_FsMIOspfExtRouteNextHop_Type())
fsMIOspfExtRouteNextHop.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIOspfExtRouteNextHop.setStatus(_A)
_FsMIOspfExtRouteStatus_Type=RowStatus
_FsMIOspfExtRouteStatus_Object=MibTableColumn
fsMIOspfExtRouteStatus=_FsMIOspfExtRouteStatus_Object((1,3,6,1,4,1,10876,101,1,147,2,1,10),_FsMIOspfExtRouteStatus_Type())
fsMIOspfExtRouteStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIOspfExtRouteStatus.setStatus(_A)
_FsMIOspfGrTestGroup_ObjectIdentity=ObjectIdentity
fsMIOspfGrTestGroup=_FsMIOspfGrTestGroup_ObjectIdentity((1,3,6,1,4,1,10876,101,1,147,100))
_FsMIOspfGrTable_Object=MibTable
fsMIOspfGrTable=_FsMIOspfGrTable_Object((1,3,6,1,4,1,10876,101,1,147,100,2))
if mibBuilder.loadTexts:fsMIOspfGrTable.setStatus(_A)
_FsMIOspfGrEntry_Object=MibTableRow
fsMIOspfGrEntry=_FsMIOspfGrEntry_Object((1,3,6,1,4,1,10876,101,1,147,100,2,1))
fsMIOspfGrEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:fsMIOspfGrEntry.setStatus(_A)
class _FsMIOspfGrShutdown_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('none',1),('unplanned',2)))
_FsMIOspfGrShutdown_Type.__name__=_C
_FsMIOspfGrShutdown_Object=MibTableColumn
fsMIOspfGrShutdown=_FsMIOspfGrShutdown_Object((1,3,6,1,4,1,10876,101,1,147,100,2,1,1),_FsMIOspfGrShutdown_Type())
fsMIOspfGrShutdown.setMaxAccess('read-write')
if mibBuilder.loadTexts:fsMIOspfGrShutdown.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'fsMIOspfTestGroup':fsMIOspfTestGroup,'fsMIOspfBRRouteTable':fsMIOspfBRRouteTable,'fsMIOspfBRRouteEntry':fsMIOspfBRRouteEntry,_I:fsMIOspfBRRouteIpAddr,_J:fsMIOspfBRRouteIpAddrMask,_K:fsMIOspfBRRouteIpTos,_L:fsMIOspfBRRouteIpNextHop,_M:fsMIOspfBRRouteDestType,'fsMIOspfBRRouteType':fsMIOspfBRRouteType,'fsMIOspfBRRouteAreaId':fsMIOspfBRRouteAreaId,'fsMIOspfBRRouteCost':fsMIOspfBRRouteCost,'fsMIOspfBRRouteInterfaceIndex':fsMIOspfBRRouteInterfaceIndex,'fsMIOspfExtRouteTable':fsMIOspfExtRouteTable,'fsMIOspfExtRouteEntry':fsMIOspfExtRouteEntry,_N:fsMIOspfExtRouteDest,_O:fsMIOspfExtRouteMask,_P:fsMIOspfExtRouteTOS,'fsMIOspfExtRouteMetric':fsMIOspfExtRouteMetric,'fsMIOspfExtRouteMetricType':fsMIOspfExtRouteMetricType,'fsMIOspfExtRouteTag':fsMIOspfExtRouteTag,'fsMIOspfExtRouteFwdAdr':fsMIOspfExtRouteFwdAdr,'fsMIOspfExtRouteIfIndex':fsMIOspfExtRouteIfIndex,'fsMIOspfExtRouteNextHop':fsMIOspfExtRouteNextHop,'fsMIOspfExtRouteStatus':fsMIOspfExtRouteStatus,'fsMIOspfGrTestGroup':fsMIOspfGrTestGroup,'fsMIOspfGrTable':fsMIOspfGrTable,'fsMIOspfGrEntry':fsMIOspfGrEntry,'fsMIOspfGrShutdown':fsMIOspfGrShutdown})