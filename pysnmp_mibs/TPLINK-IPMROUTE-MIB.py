_J='tpIpMRouteStarGGroup'
_I='pimSparseMode'
_H='pimDenseMode'
_G='tpIpMRouteSGSource'
_F='tpIpMRouteSGGroup'
_E='TPLINK-IPMROUTE-MIB'
_D='OctetString'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
tplinkMgmt,=mibBuilder.importSymbols('TPLINK-MIB','tplinkMgmt')
tplinkIpMrouteMIB=ModuleIdentity((1,3,6,1,4,1,11863,6,78))
if mibBuilder.loadTexts:tplinkIpMrouteMIB.setRevisions(('2012-12-13 09:30',))
_TplinkIpMrouteMIBObjects_ObjectIdentity=ObjectIdentity
tplinkIpMrouteMIBObjects=_TplinkIpMrouteMIBObjects_ObjectIdentity((1,3,6,1,4,1,11863,6,78,1))
_TpIpMRoute_ObjectIdentity=ObjectIdentity
tpIpMRoute=_TpIpMRoute_ObjectIdentity((1,3,6,1,4,1,11863,6,78,1,1))
class _TpIpMRouteEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_TpIpMRouteEnable_Type.__name__=_C
_TpIpMRouteEnable_Object=MibScalar
tpIpMRouteEnable=_TpIpMRouteEnable_Object((1,3,6,1,4,1,11863,6,78,1,1,1),_TpIpMRouteEnable_Type())
tpIpMRouteEnable.setMaxAccess('read-write')
if mibBuilder.loadTexts:tpIpMRouteEnable.setStatus(_A)
_TpIpMRouteSGTable_Object=MibTable
tpIpMRouteSGTable=_TpIpMRouteSGTable_Object((1,3,6,1,4,1,11863,6,78,1,1,2))
if mibBuilder.loadTexts:tpIpMRouteSGTable.setStatus(_A)
_TpIpMRouteSGEntry_Object=MibTableRow
tpIpMRouteSGEntry=_TpIpMRouteSGEntry_Object((1,3,6,1,4,1,11863,6,78,1,1,2,1))
tpIpMRouteSGEntry.setIndexNames((0,_E,_F),(0,_E,_G))
if mibBuilder.loadTexts:tpIpMRouteSGEntry.setStatus(_A)
_TpIpMRouteSGGroup_Type=IpAddress
_TpIpMRouteSGGroup_Object=MibTableColumn
tpIpMRouteSGGroup=_TpIpMRouteSGGroup_Object((1,3,6,1,4,1,11863,6,78,1,1,2,1,1),_TpIpMRouteSGGroup_Type())
tpIpMRouteSGGroup.setMaxAccess(_B)
if mibBuilder.loadTexts:tpIpMRouteSGGroup.setStatus(_A)
_TpIpMRouteSGSource_Type=IpAddress
_TpIpMRouteSGSource_Object=MibTableColumn
tpIpMRouteSGSource=_TpIpMRouteSGSource_Object((1,3,6,1,4,1,11863,6,78,1,1,2,1,2),_TpIpMRouteSGSource_Type())
tpIpMRouteSGSource.setMaxAccess(_B)
if mibBuilder.loadTexts:tpIpMRouteSGSource.setStatus(_A)
class _TpIpMRouteSGIncomingInterface_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_TpIpMRouteSGIncomingInterface_Type.__name__=_D
_TpIpMRouteSGIncomingInterface_Object=MibTableColumn
tpIpMRouteSGIncomingInterface=_TpIpMRouteSGIncomingInterface_Object((1,3,6,1,4,1,11863,6,78,1,1,2,1,3),_TpIpMRouteSGIncomingInterface_Type())
tpIpMRouteSGIncomingInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:tpIpMRouteSGIncomingInterface.setStatus(_A)
class _TpIpMRouteSGOutgoingInterface_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_TpIpMRouteSGOutgoingInterface_Type.__name__=_D
_TpIpMRouteSGOutgoingInterface_Object=MibTableColumn
tpIpMRouteSGOutgoingInterface=_TpIpMRouteSGOutgoingInterface_Object((1,3,6,1,4,1,11863,6,78,1,1,2,1,4),_TpIpMRouteSGOutgoingInterface_Type())
tpIpMRouteSGOutgoingInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:tpIpMRouteSGOutgoingInterface.setStatus(_A)
_TpIpMRouteSGRpfNeighbor_Type=IpAddress
_TpIpMRouteSGRpfNeighbor_Object=MibTableColumn
tpIpMRouteSGRpfNeighbor=_TpIpMRouteSGRpfNeighbor_Object((1,3,6,1,4,1,11863,6,78,1,1,2,1,5),_TpIpMRouteSGRpfNeighbor_Type())
tpIpMRouteSGRpfNeighbor.setMaxAccess(_B)
if mibBuilder.loadTexts:tpIpMRouteSGRpfNeighbor.setStatus(_A)
_TpIpMRouteSGUpTime_Type=TimeTicks
_TpIpMRouteSGUpTime_Object=MibTableColumn
tpIpMRouteSGUpTime=_TpIpMRouteSGUpTime_Object((1,3,6,1,4,1,11863,6,78,1,1,2,1,6),_TpIpMRouteSGUpTime_Type())
tpIpMRouteSGUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:tpIpMRouteSGUpTime.setStatus(_A)
_TpIpMRouteSGExpiryTime_Type=TimeTicks
_TpIpMRouteSGExpiryTime_Object=MibTableColumn
tpIpMRouteSGExpiryTime=_TpIpMRouteSGExpiryTime_Object((1,3,6,1,4,1,11863,6,78,1,1,2,1,7),_TpIpMRouteSGExpiryTime_Type())
tpIpMRouteSGExpiryTime.setMaxAccess(_B)
if mibBuilder.loadTexts:tpIpMRouteSGExpiryTime.setStatus(_A)
class _TpIpMRouteSGProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_TpIpMRouteSGProtocol_Type.__name__=_C
_TpIpMRouteSGProtocol_Object=MibTableColumn
tpIpMRouteSGProtocol=_TpIpMRouteSGProtocol_Object((1,3,6,1,4,1,11863,6,78,1,1,2,1,8),_TpIpMRouteSGProtocol_Type())
tpIpMRouteSGProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:tpIpMRouteSGProtocol.setStatus(_A)
class _TpIpMRouteSGFlags_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('spt',1),('rpt',2)))
_TpIpMRouteSGFlags_Type.__name__=_C
_TpIpMRouteSGFlags_Object=MibTableColumn
tpIpMRouteSGFlags=_TpIpMRouteSGFlags_Object((1,3,6,1,4,1,11863,6,78,1,1,2,1,9),_TpIpMRouteSGFlags_Type())
tpIpMRouteSGFlags.setMaxAccess(_B)
if mibBuilder.loadTexts:tpIpMRouteSGFlags.setStatus(_A)
_TpIpMRouteStarGTable_Object=MibTable
tpIpMRouteStarGTable=_TpIpMRouteStarGTable_Object((1,3,6,1,4,1,11863,6,78,1,1,3))
if mibBuilder.loadTexts:tpIpMRouteStarGTable.setStatus(_A)
_TpIpMRouteStarGEntry_Object=MibTableRow
tpIpMRouteStarGEntry=_TpIpMRouteStarGEntry_Object((1,3,6,1,4,1,11863,6,78,1,1,3,1))
tpIpMRouteStarGEntry.setIndexNames((0,_E,_J))
if mibBuilder.loadTexts:tpIpMRouteStarGEntry.setStatus(_A)
_TpIpMRouteStarGGroup_Type=IpAddress
_TpIpMRouteStarGGroup_Object=MibTableColumn
tpIpMRouteStarGGroup=_TpIpMRouteStarGGroup_Object((1,3,6,1,4,1,11863,6,78,1,1,3,1,1),_TpIpMRouteStarGGroup_Type())
tpIpMRouteStarGGroup.setMaxAccess(_B)
if mibBuilder.loadTexts:tpIpMRouteStarGGroup.setStatus(_A)
_TpIpMRouteStarGSource_Type=IpAddress
_TpIpMRouteStarGSource_Object=MibTableColumn
tpIpMRouteStarGSource=_TpIpMRouteStarGSource_Object((1,3,6,1,4,1,11863,6,78,1,1,3,1,2),_TpIpMRouteStarGSource_Type())
tpIpMRouteStarGSource.setMaxAccess(_B)
if mibBuilder.loadTexts:tpIpMRouteStarGSource.setStatus(_A)
class _TpIpMRouteStarGIncomingInterface_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_TpIpMRouteStarGIncomingInterface_Type.__name__=_D
_TpIpMRouteStarGIncomingInterface_Object=MibTableColumn
tpIpMRouteStarGIncomingInterface=_TpIpMRouteStarGIncomingInterface_Object((1,3,6,1,4,1,11863,6,78,1,1,3,1,3),_TpIpMRouteStarGIncomingInterface_Type())
tpIpMRouteStarGIncomingInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:tpIpMRouteStarGIncomingInterface.setStatus(_A)
class _TpIpMRouteStarGOutgoingInterface_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_TpIpMRouteStarGOutgoingInterface_Type.__name__=_D
_TpIpMRouteStarGOutgoingInterface_Object=MibTableColumn
tpIpMRouteStarGOutgoingInterface=_TpIpMRouteStarGOutgoingInterface_Object((1,3,6,1,4,1,11863,6,78,1,1,3,1,4),_TpIpMRouteStarGOutgoingInterface_Type())
tpIpMRouteStarGOutgoingInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:tpIpMRouteStarGOutgoingInterface.setStatus(_A)
_TpIpMRouteStarGRpfNeighbor_Type=IpAddress
_TpIpMRouteStarGRpfNeighbor_Object=MibTableColumn
tpIpMRouteStarGRpfNeighbor=_TpIpMRouteStarGRpfNeighbor_Object((1,3,6,1,4,1,11863,6,78,1,1,3,1,5),_TpIpMRouteStarGRpfNeighbor_Type())
tpIpMRouteStarGRpfNeighbor.setMaxAccess(_B)
if mibBuilder.loadTexts:tpIpMRouteStarGRpfNeighbor.setStatus(_A)
_TpIpMRouteStarGUpTime_Type=TimeTicks
_TpIpMRouteStarGUpTime_Object=MibTableColumn
tpIpMRouteStarGUpTime=_TpIpMRouteStarGUpTime_Object((1,3,6,1,4,1,11863,6,78,1,1,3,1,6),_TpIpMRouteStarGUpTime_Type())
tpIpMRouteStarGUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:tpIpMRouteStarGUpTime.setStatus(_A)
_TpIpMRouteStarGExpiryTime_Type=TimeTicks
_TpIpMRouteStarGExpiryTime_Object=MibTableColumn
tpIpMRouteStarGExpiryTime=_TpIpMRouteStarGExpiryTime_Object((1,3,6,1,4,1,11863,6,78,1,1,3,1,7),_TpIpMRouteStarGExpiryTime_Type())
tpIpMRouteStarGExpiryTime.setMaxAccess(_B)
if mibBuilder.loadTexts:tpIpMRouteStarGExpiryTime.setStatus(_A)
class _TpIpMRouteStarGProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_TpIpMRouteStarGProtocol_Type.__name__=_C
_TpIpMRouteStarGProtocol_Object=MibTableColumn
tpIpMRouteStarGProtocol=_TpIpMRouteStarGProtocol_Object((1,3,6,1,4,1,11863,6,78,1,1,3,1,8),_TpIpMRouteStarGProtocol_Type())
tpIpMRouteStarGProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:tpIpMRouteStarGProtocol.setStatus(_A)
class _TpIpMRouteStarGFlags_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('spt',1),('rpt',2)))
_TpIpMRouteStarGFlags_Type.__name__=_C
_TpIpMRouteStarGFlags_Object=MibTableColumn
tpIpMRouteStarGFlags=_TpIpMRouteStarGFlags_Object((1,3,6,1,4,1,11863,6,78,1,1,3,1,9),_TpIpMRouteStarGFlags_Type())
tpIpMRouteStarGFlags.setMaxAccess(_B)
if mibBuilder.loadTexts:tpIpMRouteStarGFlags.setStatus(_A)
_TplinkIpMrouteNotifications_ObjectIdentity=ObjectIdentity
tplinkIpMrouteNotifications=_TplinkIpMrouteNotifications_ObjectIdentity((1,3,6,1,4,1,11863,6,78,2))
mibBuilder.exportSymbols(_E,**{'tplinkIpMrouteMIB':tplinkIpMrouteMIB,'tplinkIpMrouteMIBObjects':tplinkIpMrouteMIBObjects,'tpIpMRoute':tpIpMRoute,'tpIpMRouteEnable':tpIpMRouteEnable,'tpIpMRouteSGTable':tpIpMRouteSGTable,'tpIpMRouteSGEntry':tpIpMRouteSGEntry,_F:tpIpMRouteSGGroup,_G:tpIpMRouteSGSource,'tpIpMRouteSGIncomingInterface':tpIpMRouteSGIncomingInterface,'tpIpMRouteSGOutgoingInterface':tpIpMRouteSGOutgoingInterface,'tpIpMRouteSGRpfNeighbor':tpIpMRouteSGRpfNeighbor,'tpIpMRouteSGUpTime':tpIpMRouteSGUpTime,'tpIpMRouteSGExpiryTime':tpIpMRouteSGExpiryTime,'tpIpMRouteSGProtocol':tpIpMRouteSGProtocol,'tpIpMRouteSGFlags':tpIpMRouteSGFlags,'tpIpMRouteStarGTable':tpIpMRouteStarGTable,'tpIpMRouteStarGEntry':tpIpMRouteStarGEntry,_J:tpIpMRouteStarGGroup,'tpIpMRouteStarGSource':tpIpMRouteStarGSource,'tpIpMRouteStarGIncomingInterface':tpIpMRouteStarGIncomingInterface,'tpIpMRouteStarGOutgoingInterface':tpIpMRouteStarGOutgoingInterface,'tpIpMRouteStarGRpfNeighbor':tpIpMRouteStarGRpfNeighbor,'tpIpMRouteStarGUpTime':tpIpMRouteStarGUpTime,'tpIpMRouteStarGExpiryTime':tpIpMRouteStarGExpiryTime,'tpIpMRouteStarGProtocol':tpIpMRouteStarGProtocol,'tpIpMRouteStarGFlags':tpIpMRouteStarGFlags,'tplinkIpMrouteNotifications':tplinkIpMrouteNotifications})