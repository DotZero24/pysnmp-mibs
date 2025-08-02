_O='fsMIRrd6RoutingProtoId'
_N='netmgmt'
_M='fsMIRrd6ControlNetMaskLen'
_L='fsMIRrd6ControlDestIpAddress'
_K='Unsigned32'
_J='OctetString'
_I='disable'
_H='enable'
_G='not-accessible'
_F='fsMIRtm6ContextId'
_E='read-only'
_D='SUPERMICRO-RTM6MI-MIB'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_J,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_K,'enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
fsMIRtm6=ModuleIdentity((1,3,6,1,4,1,10876,101,2,32))
if mibBuilder.loadTexts:fsMIRtm6.setRevisions(('2012-09-05 00:00',))
_FsMIRtm6Scalar_ObjectIdentity=ObjectIdentity
fsMIRtm6Scalar=_FsMIRtm6Scalar_ObjectIdentity((1,3,6,1,4,1,10876,101,2,32,1))
_FsMIRtm6GlobalTrace_Type=Unsigned32
_FsMIRtm6GlobalTrace_Object=MibScalar
fsMIRtm6GlobalTrace=_FsMIRtm6GlobalTrace_Object((1,3,6,1,4,1,10876,101,2,32,1,1),_FsMIRtm6GlobalTrace_Type())
fsMIRtm6GlobalTrace.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIRtm6GlobalTrace.setStatus(_A)
class _FsMIRtm6ThrotLimit_Type(Unsigned32):defaultValue=1000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_FsMIRtm6ThrotLimit_Type.__name__=_K
_FsMIRtm6ThrotLimit_Object=MibScalar
fsMIRtm6ThrotLimit=_FsMIRtm6ThrotLimit_Object((1,3,6,1,4,1,10876,101,2,32,1,2),_FsMIRtm6ThrotLimit_Type())
fsMIRtm6ThrotLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIRtm6ThrotLimit.setStatus(_A)
_FsMIRtm6Table_Object=MibTable
fsMIRtm6Table=_FsMIRtm6Table_Object((1,3,6,1,4,1,10876,101,2,32,2))
if mibBuilder.loadTexts:fsMIRtm6Table.setStatus(_A)
_FsMIRtm6Entry_Object=MibTableRow
fsMIRtm6Entry=_FsMIRtm6Entry_Object((1,3,6,1,4,1,10876,101,2,32,2,1))
fsMIRtm6Entry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:fsMIRtm6Entry.setStatus(_A)
class _FsMIRtm6ContextId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_FsMIRtm6ContextId_Type.__name__=_C
_FsMIRtm6ContextId_Object=MibTableColumn
fsMIRtm6ContextId=_FsMIRtm6ContextId_Object((1,3,6,1,4,1,10876,101,2,32,2,1,1),_FsMIRtm6ContextId_Type())
fsMIRtm6ContextId.setMaxAccess(_G)
if mibBuilder.loadTexts:fsMIRtm6ContextId.setStatus(_A)
_FsMIRrd6RouterId_Type=IpAddress
_FsMIRrd6RouterId_Object=MibTableColumn
fsMIRrd6RouterId=_FsMIRrd6RouterId_Object((1,3,6,1,4,1,10876,101,2,32,2,1,2),_FsMIRrd6RouterId_Type())
fsMIRrd6RouterId.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIRrd6RouterId.setStatus(_A)
class _FsMIRrd6FilterByOspfTag_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_FsMIRrd6FilterByOspfTag_Type.__name__=_C
_FsMIRrd6FilterByOspfTag_Object=MibTableColumn
fsMIRrd6FilterByOspfTag=_FsMIRrd6FilterByOspfTag_Object((1,3,6,1,4,1,10876,101,2,32,2,1,3),_FsMIRrd6FilterByOspfTag_Type())
fsMIRrd6FilterByOspfTag.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIRrd6FilterByOspfTag.setStatus(_A)
_FsMIRrd6FilterOspfTag_Type=Integer32
_FsMIRrd6FilterOspfTag_Object=MibTableColumn
fsMIRrd6FilterOspfTag=_FsMIRrd6FilterOspfTag_Object((1,3,6,1,4,1,10876,101,2,32,2,1,4),_FsMIRrd6FilterOspfTag_Type())
fsMIRrd6FilterOspfTag.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIRrd6FilterOspfTag.setStatus(_A)
class _FsMIRrd6FilterOspfTagMask_Type(Integer32):defaultValue=-1
_FsMIRrd6FilterOspfTagMask_Type.__name__=_C
_FsMIRrd6FilterOspfTagMask_Object=MibTableColumn
fsMIRrd6FilterOspfTagMask=_FsMIRrd6FilterOspfTagMask_Object((1,3,6,1,4,1,10876,101,2,32,2,1,5),_FsMIRrd6FilterOspfTagMask_Type())
fsMIRrd6FilterOspfTagMask.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIRrd6FilterOspfTagMask.setStatus(_A)
class _FsMIRrd6RouterASNumber_Type(Integer32):defaultValue=0
_FsMIRrd6RouterASNumber_Type.__name__=_C
_FsMIRrd6RouterASNumber_Object=MibTableColumn
fsMIRrd6RouterASNumber=_FsMIRrd6RouterASNumber_Object((1,3,6,1,4,1,10876,101,2,32,2,1,6),_FsMIRrd6RouterASNumber_Type())
fsMIRrd6RouterASNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIRrd6RouterASNumber.setStatus(_A)
class _FsMIRrd6AdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_FsMIRrd6AdminStatus_Type.__name__=_C
_FsMIRrd6AdminStatus_Object=MibTableColumn
fsMIRrd6AdminStatus=_FsMIRrd6AdminStatus_Object((1,3,6,1,4,1,10876,101,2,32,2,1,7),_FsMIRrd6AdminStatus_Type())
fsMIRrd6AdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIRrd6AdminStatus.setStatus(_A)
_FsMIRrd6Trace_Type=Unsigned32
_FsMIRrd6Trace_Object=MibTableColumn
fsMIRrd6Trace=_FsMIRrd6Trace_Object((1,3,6,1,4,1,10876,101,2,32,2,1,8),_FsMIRrd6Trace_Type())
fsMIRrd6Trace.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIRrd6Trace.setStatus(_A)
_FsMIRrd6ControlTable_Object=MibTable
fsMIRrd6ControlTable=_FsMIRrd6ControlTable_Object((1,3,6,1,4,1,10876,101,2,32,3))
if mibBuilder.loadTexts:fsMIRrd6ControlTable.setStatus(_A)
_FsMIRrd6ControlEntry_Object=MibTableRow
fsMIRrd6ControlEntry=_FsMIRrd6ControlEntry_Object((1,3,6,1,4,1,10876,101,2,32,3,1))
fsMIRrd6ControlEntry.setIndexNames((0,_D,_F),(0,_D,_L),(0,_D,_M))
if mibBuilder.loadTexts:fsMIRrd6ControlEntry.setStatus(_A)
class _FsMIRrd6ControlDestIpAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_FsMIRrd6ControlDestIpAddress_Type.__name__=_J
_FsMIRrd6ControlDestIpAddress_Object=MibTableColumn
fsMIRrd6ControlDestIpAddress=_FsMIRrd6ControlDestIpAddress_Object((1,3,6,1,4,1,10876,101,2,32,3,1,1),_FsMIRrd6ControlDestIpAddress_Type())
fsMIRrd6ControlDestIpAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:fsMIRrd6ControlDestIpAddress.setStatus(_A)
class _FsMIRrd6ControlNetMaskLen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_FsMIRrd6ControlNetMaskLen_Type.__name__=_C
_FsMIRrd6ControlNetMaskLen_Object=MibTableColumn
fsMIRrd6ControlNetMaskLen=_FsMIRrd6ControlNetMaskLen_Object((1,3,6,1,4,1,10876,101,2,32,3,1,2),_FsMIRrd6ControlNetMaskLen_Type())
fsMIRrd6ControlNetMaskLen.setMaxAccess(_G)
if mibBuilder.loadTexts:fsMIRrd6ControlNetMaskLen.setStatus(_A)
class _FsMIRrd6ControlSourceProto_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('all',0),('other',1),('local',2),(_N,3),('ndisc',4),('rip',5),('ospf',6),('bgp',7),('idrp',8),('igrp',9)))
_FsMIRrd6ControlSourceProto_Type.__name__=_C
_FsMIRrd6ControlSourceProto_Object=MibTableColumn
fsMIRrd6ControlSourceProto=_FsMIRrd6ControlSourceProto_Object((1,3,6,1,4,1,10876,101,2,32,3,1,3),_FsMIRrd6ControlSourceProto_Type())
fsMIRrd6ControlSourceProto.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIRrd6ControlSourceProto.setStatus(_A)
class _FsMIRrd6ControlDestProto_Type(Integer32):defaultValue=0
_FsMIRrd6ControlDestProto_Type.__name__=_C
_FsMIRrd6ControlDestProto_Object=MibTableColumn
fsMIRrd6ControlDestProto=_FsMIRrd6ControlDestProto_Object((1,3,6,1,4,1,10876,101,2,32,3,1,4),_FsMIRrd6ControlDestProto_Type())
fsMIRrd6ControlDestProto.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIRrd6ControlDestProto.setStatus(_A)
class _FsMIRrd6ControlRouteExportFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('permit',1),('deny',2)))
_FsMIRrd6ControlRouteExportFlag_Type.__name__=_C
_FsMIRrd6ControlRouteExportFlag_Object=MibTableColumn
fsMIRrd6ControlRouteExportFlag=_FsMIRrd6ControlRouteExportFlag_Object((1,3,6,1,4,1,10876,101,2,32,3,1,5),_FsMIRrd6ControlRouteExportFlag_Type())
fsMIRrd6ControlRouteExportFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIRrd6ControlRouteExportFlag.setStatus(_A)
_FsMIRrd6ControlRowStatus_Type=RowStatus
_FsMIRrd6ControlRowStatus_Object=MibTableColumn
fsMIRrd6ControlRowStatus=_FsMIRrd6ControlRowStatus_Object((1,3,6,1,4,1,10876,101,2,32,3,1,6),_FsMIRrd6ControlRowStatus_Type())
fsMIRrd6ControlRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIRrd6ControlRowStatus.setStatus(_A)
_FsMIRrd6RoutingProtoTable_Object=MibTable
fsMIRrd6RoutingProtoTable=_FsMIRrd6RoutingProtoTable_Object((1,3,6,1,4,1,10876,101,2,32,4))
if mibBuilder.loadTexts:fsMIRrd6RoutingProtoTable.setStatus(_A)
_FsMIRrd6RoutingProtoEntry_Object=MibTableRow
fsMIRrd6RoutingProtoEntry=_FsMIRrd6RoutingProtoEntry_Object((1,3,6,1,4,1,10876,101,2,32,4,1))
fsMIRrd6RoutingProtoEntry.setIndexNames((0,_D,_F),(0,_D,_O))
if mibBuilder.loadTexts:fsMIRrd6RoutingProtoEntry.setStatus(_A)
class _FsMIRrd6RoutingProtoId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('other',1),('local',2),(_N,3),('ndisc',4),('rip',5),('ospf',6),('bgp',7),('idrp',8),('igrp',9)))
_FsMIRrd6RoutingProtoId_Type.__name__=_C
_FsMIRrd6RoutingProtoId_Object=MibTableColumn
fsMIRrd6RoutingProtoId=_FsMIRrd6RoutingProtoId_Object((1,3,6,1,4,1,10876,101,2,32,4,1,1),_FsMIRrd6RoutingProtoId_Type())
fsMIRrd6RoutingProtoId.setMaxAccess(_G)
if mibBuilder.loadTexts:fsMIRrd6RoutingProtoId.setStatus(_A)
_FsMIRrd6RoutingRegnId_Type=Integer32
_FsMIRrd6RoutingRegnId_Object=MibTableColumn
fsMIRrd6RoutingRegnId=_FsMIRrd6RoutingRegnId_Object((1,3,6,1,4,1,10876,101,2,32,4,1,2),_FsMIRrd6RoutingRegnId_Type())
fsMIRrd6RoutingRegnId.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIRrd6RoutingRegnId.setStatus(_A)
_FsMIRrd6RoutingProtoTaskIdent_Type=OctetString
_FsMIRrd6RoutingProtoTaskIdent_Object=MibTableColumn
fsMIRrd6RoutingProtoTaskIdent=_FsMIRrd6RoutingProtoTaskIdent_Object((1,3,6,1,4,1,10876,101,2,32,4,1,3),_FsMIRrd6RoutingProtoTaskIdent_Type())
fsMIRrd6RoutingProtoTaskIdent.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIRrd6RoutingProtoTaskIdent.setStatus(_A)
_FsMIRrd6RoutingProtoQueueIdent_Type=OctetString
_FsMIRrd6RoutingProtoQueueIdent_Object=MibTableColumn
fsMIRrd6RoutingProtoQueueIdent=_FsMIRrd6RoutingProtoQueueIdent_Object((1,3,6,1,4,1,10876,101,2,32,4,1,4),_FsMIRrd6RoutingProtoQueueIdent_Type())
fsMIRrd6RoutingProtoQueueIdent.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIRrd6RoutingProtoQueueIdent.setStatus(_A)
class _FsMIRrd6AllowOspfAreaRoutes_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_FsMIRrd6AllowOspfAreaRoutes_Type.__name__=_C
_FsMIRrd6AllowOspfAreaRoutes_Object=MibTableColumn
fsMIRrd6AllowOspfAreaRoutes=_FsMIRrd6AllowOspfAreaRoutes_Object((1,3,6,1,4,1,10876,101,2,32,4,1,5),_FsMIRrd6AllowOspfAreaRoutes_Type())
fsMIRrd6AllowOspfAreaRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIRrd6AllowOspfAreaRoutes.setStatus(_A)
class _FsMIRrd6AllowOspfExtRoutes_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_FsMIRrd6AllowOspfExtRoutes_Type.__name__=_C
_FsMIRrd6AllowOspfExtRoutes_Object=MibTableColumn
fsMIRrd6AllowOspfExtRoutes=_FsMIRrd6AllowOspfExtRoutes_Object((1,3,6,1,4,1,10876,101,2,32,4,1,6),_FsMIRrd6AllowOspfExtRoutes_Type())
fsMIRrd6AllowOspfExtRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIRrd6AllowOspfExtRoutes.setStatus(_A)
_FsMIRtm6RedTest_ObjectIdentity=ObjectIdentity
fsMIRtm6RedTest=_FsMIRtm6RedTest_ObjectIdentity((1,3,6,1,4,1,10876,101,2,32,5))
_FsMIRtm6RedEntryTime_Type=Integer32
_FsMIRtm6RedEntryTime_Object=MibScalar
fsMIRtm6RedEntryTime=_FsMIRtm6RedEntryTime_Object((1,3,6,1,4,1,10876,101,2,32,5,1),_FsMIRtm6RedEntryTime_Type())
fsMIRtm6RedEntryTime.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIRtm6RedEntryTime.setStatus(_A)
_FsMIRtm6RedExitTime_Type=Integer32
_FsMIRtm6RedExitTime_Object=MibScalar
fsMIRtm6RedExitTime=_FsMIRtm6RedExitTime_Object((1,3,6,1,4,1,10876,101,2,32,5,2),_FsMIRtm6RedExitTime_Type())
fsMIRtm6RedExitTime.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIRtm6RedExitTime.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'fsMIRtm6':fsMIRtm6,'fsMIRtm6Scalar':fsMIRtm6Scalar,'fsMIRtm6GlobalTrace':fsMIRtm6GlobalTrace,'fsMIRtm6ThrotLimit':fsMIRtm6ThrotLimit,'fsMIRtm6Table':fsMIRtm6Table,'fsMIRtm6Entry':fsMIRtm6Entry,_F:fsMIRtm6ContextId,'fsMIRrd6RouterId':fsMIRrd6RouterId,'fsMIRrd6FilterByOspfTag':fsMIRrd6FilterByOspfTag,'fsMIRrd6FilterOspfTag':fsMIRrd6FilterOspfTag,'fsMIRrd6FilterOspfTagMask':fsMIRrd6FilterOspfTagMask,'fsMIRrd6RouterASNumber':fsMIRrd6RouterASNumber,'fsMIRrd6AdminStatus':fsMIRrd6AdminStatus,'fsMIRrd6Trace':fsMIRrd6Trace,'fsMIRrd6ControlTable':fsMIRrd6ControlTable,'fsMIRrd6ControlEntry':fsMIRrd6ControlEntry,_L:fsMIRrd6ControlDestIpAddress,_M:fsMIRrd6ControlNetMaskLen,'fsMIRrd6ControlSourceProto':fsMIRrd6ControlSourceProto,'fsMIRrd6ControlDestProto':fsMIRrd6ControlDestProto,'fsMIRrd6ControlRouteExportFlag':fsMIRrd6ControlRouteExportFlag,'fsMIRrd6ControlRowStatus':fsMIRrd6ControlRowStatus,'fsMIRrd6RoutingProtoTable':fsMIRrd6RoutingProtoTable,'fsMIRrd6RoutingProtoEntry':fsMIRrd6RoutingProtoEntry,_O:fsMIRrd6RoutingProtoId,'fsMIRrd6RoutingRegnId':fsMIRrd6RoutingRegnId,'fsMIRrd6RoutingProtoTaskIdent':fsMIRrd6RoutingProtoTaskIdent,'fsMIRrd6RoutingProtoQueueIdent':fsMIRrd6RoutingProtoQueueIdent,'fsMIRrd6AllowOspfAreaRoutes':fsMIRrd6AllowOspfAreaRoutes,'fsMIRrd6AllowOspfExtRoutes':fsMIRrd6AllowOspfExtRoutes,'fsMIRtm6RedTest':fsMIRtm6RedTest,'fsMIRtm6RedEntryTime':fsMIRtm6RedEntryTime,'fsMIRtm6RedExitTime':fsMIRtm6RedExitTime})