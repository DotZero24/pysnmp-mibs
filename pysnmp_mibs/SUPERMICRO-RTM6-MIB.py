_N='fsRrd6RoutingProtoId'
_M='netmgmt'
_L='fsRrd6ControlNetMaskLen'
_K='fsRrd6ControlDestIpAddress'
_J='Unsigned32'
_I='OctetString'
_H='not-accessible'
_G='disable'
_F='enable'
_E='SUPERMICRO-RTM6-MIB'
_D='read-only'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_I,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_J,'enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
futurertm6=ModuleIdentity((1,3,6,1,4,1,10876,101,1,92))
if mibBuilder.loadTexts:futurertm6.setRevisions(('2012-09-05 00:00',))
_Fsrrd6Scalar_ObjectIdentity=ObjectIdentity
fsrrd6Scalar=_Fsrrd6Scalar_ObjectIdentity((1,3,6,1,4,1,10876,101,1,92,1))
_FsRrd6RouterId_Type=IpAddress
_FsRrd6RouterId_Object=MibScalar
fsRrd6RouterId=_FsRrd6RouterId_Object((1,3,6,1,4,1,10876,101,1,92,1,1),_FsRrd6RouterId_Type())
fsRrd6RouterId.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRrd6RouterId.setStatus(_A)
class _FsRrd6FilterByOspfTag_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_FsRrd6FilterByOspfTag_Type.__name__=_C
_FsRrd6FilterByOspfTag_Object=MibScalar
fsRrd6FilterByOspfTag=_FsRrd6FilterByOspfTag_Object((1,3,6,1,4,1,10876,101,1,92,1,2),_FsRrd6FilterByOspfTag_Type())
fsRrd6FilterByOspfTag.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRrd6FilterByOspfTag.setStatus(_A)
_FsRrd6FilterOspfTag_Type=Integer32
_FsRrd6FilterOspfTag_Object=MibScalar
fsRrd6FilterOspfTag=_FsRrd6FilterOspfTag_Object((1,3,6,1,4,1,10876,101,1,92,1,3),_FsRrd6FilterOspfTag_Type())
fsRrd6FilterOspfTag.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRrd6FilterOspfTag.setStatus(_A)
class _FsRrd6FilterOspfTagMask_Type(Integer32):defaultValue=-1
_FsRrd6FilterOspfTagMask_Type.__name__=_C
_FsRrd6FilterOspfTagMask_Object=MibScalar
fsRrd6FilterOspfTagMask=_FsRrd6FilterOspfTagMask_Object((1,3,6,1,4,1,10876,101,1,92,1,4),_FsRrd6FilterOspfTagMask_Type())
fsRrd6FilterOspfTagMask.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRrd6FilterOspfTagMask.setStatus(_A)
class _FsRrd6RouterASNumber_Type(Integer32):defaultValue=0
_FsRrd6RouterASNumber_Type.__name__=_C
_FsRrd6RouterASNumber_Object=MibScalar
fsRrd6RouterASNumber=_FsRrd6RouterASNumber_Object((1,3,6,1,4,1,10876,101,1,92,1,5),_FsRrd6RouterASNumber_Type())
fsRrd6RouterASNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRrd6RouterASNumber.setStatus(_A)
class _FsRrd6AdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_FsRrd6AdminStatus_Type.__name__=_C
_FsRrd6AdminStatus_Object=MibScalar
fsRrd6AdminStatus=_FsRrd6AdminStatus_Object((1,3,6,1,4,1,10876,101,1,92,1,6),_FsRrd6AdminStatus_Type())
fsRrd6AdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRrd6AdminStatus.setStatus(_A)
_FsRrd6Trace_Type=Unsigned32
_FsRrd6Trace_Object=MibScalar
fsRrd6Trace=_FsRrd6Trace_Object((1,3,6,1,4,1,10876,101,1,92,1,7),_FsRrd6Trace_Type())
fsRrd6Trace.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRrd6Trace.setStatus(_A)
class _FsRrd6ThrotLimit_Type(Unsigned32):defaultValue=1000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_FsRrd6ThrotLimit_Type.__name__=_J
_FsRrd6ThrotLimit_Object=MibScalar
fsRrd6ThrotLimit=_FsRrd6ThrotLimit_Object((1,3,6,1,4,1,10876,101,1,92,1,8),_FsRrd6ThrotLimit_Type())
fsRrd6ThrotLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRrd6ThrotLimit.setStatus(_A)
_FsRrd6ControlTable_Object=MibTable
fsRrd6ControlTable=_FsRrd6ControlTable_Object((1,3,6,1,4,1,10876,101,1,92,2))
if mibBuilder.loadTexts:fsRrd6ControlTable.setStatus(_A)
_FsRrd6ControlEntry_Object=MibTableRow
fsRrd6ControlEntry=_FsRrd6ControlEntry_Object((1,3,6,1,4,1,10876,101,1,92,2,1))
fsRrd6ControlEntry.setIndexNames((0,_E,_K),(0,_E,_L))
if mibBuilder.loadTexts:fsRrd6ControlEntry.setStatus(_A)
class _FsRrd6ControlDestIpAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_FsRrd6ControlDestIpAddress_Type.__name__=_I
_FsRrd6ControlDestIpAddress_Object=MibTableColumn
fsRrd6ControlDestIpAddress=_FsRrd6ControlDestIpAddress_Object((1,3,6,1,4,1,10876,101,1,92,2,1,1),_FsRrd6ControlDestIpAddress_Type())
fsRrd6ControlDestIpAddress.setMaxAccess(_H)
if mibBuilder.loadTexts:fsRrd6ControlDestIpAddress.setStatus(_A)
class _FsRrd6ControlNetMaskLen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_FsRrd6ControlNetMaskLen_Type.__name__=_C
_FsRrd6ControlNetMaskLen_Object=MibTableColumn
fsRrd6ControlNetMaskLen=_FsRrd6ControlNetMaskLen_Object((1,3,6,1,4,1,10876,101,1,92,2,1,2),_FsRrd6ControlNetMaskLen_Type())
fsRrd6ControlNetMaskLen.setMaxAccess(_H)
if mibBuilder.loadTexts:fsRrd6ControlNetMaskLen.setStatus(_A)
class _FsRrd6ControlSourceProto_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('all',0),('other',1),('local',2),(_M,3),('ndisc',4),('rip',5),('ospf',6),('bgp',7),('idrp',8),('igrp',9)))
_FsRrd6ControlSourceProto_Type.__name__=_C
_FsRrd6ControlSourceProto_Object=MibTableColumn
fsRrd6ControlSourceProto=_FsRrd6ControlSourceProto_Object((1,3,6,1,4,1,10876,101,1,92,2,1,3),_FsRrd6ControlSourceProto_Type())
fsRrd6ControlSourceProto.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRrd6ControlSourceProto.setStatus(_A)
class _FsRrd6ControlDestProto_Type(Integer32):defaultValue=0
_FsRrd6ControlDestProto_Type.__name__=_C
_FsRrd6ControlDestProto_Object=MibTableColumn
fsRrd6ControlDestProto=_FsRrd6ControlDestProto_Object((1,3,6,1,4,1,10876,101,1,92,2,1,4),_FsRrd6ControlDestProto_Type())
fsRrd6ControlDestProto.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRrd6ControlDestProto.setStatus(_A)
class _FsRrd6ControlRouteExportFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('permit',1),('deny',2)))
_FsRrd6ControlRouteExportFlag_Type.__name__=_C
_FsRrd6ControlRouteExportFlag_Object=MibTableColumn
fsRrd6ControlRouteExportFlag=_FsRrd6ControlRouteExportFlag_Object((1,3,6,1,4,1,10876,101,1,92,2,1,5),_FsRrd6ControlRouteExportFlag_Type())
fsRrd6ControlRouteExportFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRrd6ControlRouteExportFlag.setStatus(_A)
_FsRrd6ControlRowStatus_Type=RowStatus
_FsRrd6ControlRowStatus_Object=MibTableColumn
fsRrd6ControlRowStatus=_FsRrd6ControlRowStatus_Object((1,3,6,1,4,1,10876,101,1,92,2,1,6),_FsRrd6ControlRowStatus_Type())
fsRrd6ControlRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRrd6ControlRowStatus.setStatus(_A)
_FsRrd6RoutingProtoTable_Object=MibTable
fsRrd6RoutingProtoTable=_FsRrd6RoutingProtoTable_Object((1,3,6,1,4,1,10876,101,1,92,3))
if mibBuilder.loadTexts:fsRrd6RoutingProtoTable.setStatus(_A)
_FsRrd6RoutingProtoEntry_Object=MibTableRow
fsRrd6RoutingProtoEntry=_FsRrd6RoutingProtoEntry_Object((1,3,6,1,4,1,10876,101,1,92,3,1))
fsRrd6RoutingProtoEntry.setIndexNames((0,_E,_N))
if mibBuilder.loadTexts:fsRrd6RoutingProtoEntry.setStatus(_A)
class _FsRrd6RoutingProtoId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('other',1),('local',2),(_M,3),('ndisc',4),('rip',5),('ospf',6),('bgp',7),('idrp',8),('igrp',9)))
_FsRrd6RoutingProtoId_Type.__name__=_C
_FsRrd6RoutingProtoId_Object=MibTableColumn
fsRrd6RoutingProtoId=_FsRrd6RoutingProtoId_Object((1,3,6,1,4,1,10876,101,1,92,3,1,1),_FsRrd6RoutingProtoId_Type())
fsRrd6RoutingProtoId.setMaxAccess(_H)
if mibBuilder.loadTexts:fsRrd6RoutingProtoId.setStatus(_A)
_FsRrd6RoutingRegnId_Type=Integer32
_FsRrd6RoutingRegnId_Object=MibTableColumn
fsRrd6RoutingRegnId=_FsRrd6RoutingRegnId_Object((1,3,6,1,4,1,10876,101,1,92,3,1,2),_FsRrd6RoutingRegnId_Type())
fsRrd6RoutingRegnId.setMaxAccess(_D)
if mibBuilder.loadTexts:fsRrd6RoutingRegnId.setStatus(_A)
_FsRrd6RoutingProtoTaskIdent_Type=OctetString
_FsRrd6RoutingProtoTaskIdent_Object=MibTableColumn
fsRrd6RoutingProtoTaskIdent=_FsRrd6RoutingProtoTaskIdent_Object((1,3,6,1,4,1,10876,101,1,92,3,1,3),_FsRrd6RoutingProtoTaskIdent_Type())
fsRrd6RoutingProtoTaskIdent.setMaxAccess(_D)
if mibBuilder.loadTexts:fsRrd6RoutingProtoTaskIdent.setStatus(_A)
_FsRrd6RoutingProtoQueueIdent_Type=OctetString
_FsRrd6RoutingProtoQueueIdent_Object=MibTableColumn
fsRrd6RoutingProtoQueueIdent=_FsRrd6RoutingProtoQueueIdent_Object((1,3,6,1,4,1,10876,101,1,92,3,1,4),_FsRrd6RoutingProtoQueueIdent_Type())
fsRrd6RoutingProtoQueueIdent.setMaxAccess(_D)
if mibBuilder.loadTexts:fsRrd6RoutingProtoQueueIdent.setStatus(_A)
class _FsRrd6AllowOspfAreaRoutes_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_FsRrd6AllowOspfAreaRoutes_Type.__name__=_C
_FsRrd6AllowOspfAreaRoutes_Object=MibTableColumn
fsRrd6AllowOspfAreaRoutes=_FsRrd6AllowOspfAreaRoutes_Object((1,3,6,1,4,1,10876,101,1,92,3,1,5),_FsRrd6AllowOspfAreaRoutes_Type())
fsRrd6AllowOspfAreaRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRrd6AllowOspfAreaRoutes.setStatus(_A)
class _FsRrd6AllowOspfExtRoutes_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_FsRrd6AllowOspfExtRoutes_Type.__name__=_C
_FsRrd6AllowOspfExtRoutes_Object=MibTableColumn
fsRrd6AllowOspfExtRoutes=_FsRrd6AllowOspfExtRoutes_Object((1,3,6,1,4,1,10876,101,1,92,3,1,6),_FsRrd6AllowOspfExtRoutes_Type())
fsRrd6AllowOspfExtRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRrd6AllowOspfExtRoutes.setStatus(_A)
_FsRtm6RedTest_ObjectIdentity=ObjectIdentity
fsRtm6RedTest=_FsRtm6RedTest_ObjectIdentity((1,3,6,1,4,1,10876,101,1,92,4))
_FsRtm6RedEntryTime_Type=Integer32
_FsRtm6RedEntryTime_Object=MibScalar
fsRtm6RedEntryTime=_FsRtm6RedEntryTime_Object((1,3,6,1,4,1,10876,101,1,92,4,1),_FsRtm6RedEntryTime_Type())
fsRtm6RedEntryTime.setMaxAccess(_D)
if mibBuilder.loadTexts:fsRtm6RedEntryTime.setStatus(_A)
_FsRtm6RedExitTime_Type=Integer32
_FsRtm6RedExitTime_Object=MibScalar
fsRtm6RedExitTime=_FsRtm6RedExitTime_Object((1,3,6,1,4,1,10876,101,1,92,4,2),_FsRtm6RedExitTime_Type())
fsRtm6RedExitTime.setMaxAccess(_D)
if mibBuilder.loadTexts:fsRtm6RedExitTime.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'futurertm6':futurertm6,'fsrrd6Scalar':fsrrd6Scalar,'fsRrd6RouterId':fsRrd6RouterId,'fsRrd6FilterByOspfTag':fsRrd6FilterByOspfTag,'fsRrd6FilterOspfTag':fsRrd6FilterOspfTag,'fsRrd6FilterOspfTagMask':fsRrd6FilterOspfTagMask,'fsRrd6RouterASNumber':fsRrd6RouterASNumber,'fsRrd6AdminStatus':fsRrd6AdminStatus,'fsRrd6Trace':fsRrd6Trace,'fsRrd6ThrotLimit':fsRrd6ThrotLimit,'fsRrd6ControlTable':fsRrd6ControlTable,'fsRrd6ControlEntry':fsRrd6ControlEntry,_K:fsRrd6ControlDestIpAddress,_L:fsRrd6ControlNetMaskLen,'fsRrd6ControlSourceProto':fsRrd6ControlSourceProto,'fsRrd6ControlDestProto':fsRrd6ControlDestProto,'fsRrd6ControlRouteExportFlag':fsRrd6ControlRouteExportFlag,'fsRrd6ControlRowStatus':fsRrd6ControlRowStatus,'fsRrd6RoutingProtoTable':fsRrd6RoutingProtoTable,'fsRrd6RoutingProtoEntry':fsRrd6RoutingProtoEntry,_N:fsRrd6RoutingProtoId,'fsRrd6RoutingRegnId':fsRrd6RoutingRegnId,'fsRrd6RoutingProtoTaskIdent':fsRrd6RoutingProtoTaskIdent,'fsRrd6RoutingProtoQueueIdent':fsRrd6RoutingProtoQueueIdent,'fsRrd6AllowOspfAreaRoutes':fsRrd6AllowOspfAreaRoutes,'fsRrd6AllowOspfExtRoutes':fsRrd6AllowOspfExtRoutes,'fsRtm6RedTest':fsRtm6RedTest,'fsRtm6RedEntryTime':fsRtm6RedEntryTime,'fsRtm6RedExitTime':fsRtm6RedExitTime})