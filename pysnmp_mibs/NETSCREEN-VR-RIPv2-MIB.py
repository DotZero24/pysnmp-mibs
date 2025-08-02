_O='nsVrRip2PeerDomain'
_N='nsVrRip2PeerAddress'
_M='nsVrRip2PeerVRID'
_L='RouteTag'
_K='nsVrRip2IfConfAddress'
_J='nsVrRip2IfConfVRID'
_I='nsVrRip2IfStatAddress'
_H='nsVrRip2IfStatVRID'
_G='nsVrRip2GlobalVRID'
_F='OctetString'
_E='read-create'
_D='NETSCREEN-VR-RIPv2-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
netscreenVR,=mibBuilder.importSymbols('NETSCREEN-SMI','netscreenVR')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
nsVrRip2=ModuleIdentity((1,3,6,1,4,1,3224,18,7))
class RouteTag(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_NsVrRip2GlobalsTable_Object=MibTable
nsVrRip2GlobalsTable=_NsVrRip2GlobalsTable_Object((1,3,6,1,4,1,3224,18,7,1))
if mibBuilder.loadTexts:nsVrRip2GlobalsTable.setStatus(_A)
_NsVrRip2GlobalsEntry_Object=MibTableRow
nsVrRip2GlobalsEntry=_NsVrRip2GlobalsEntry_Object((1,3,6,1,4,1,3224,18,7,1,1))
nsVrRip2GlobalsEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:nsVrRip2GlobalsEntry.setStatus(_A)
_NsVrRip2GlobalRouteChanges_Type=Counter32
_NsVrRip2GlobalRouteChanges_Object=MibTableColumn
nsVrRip2GlobalRouteChanges=_NsVrRip2GlobalRouteChanges_Object((1,3,6,1,4,1,3224,18,7,1,1,1),_NsVrRip2GlobalRouteChanges_Type())
nsVrRip2GlobalRouteChanges.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrRip2GlobalRouteChanges.setStatus(_A)
_NsVrRip2GlobalQueries_Type=Counter32
_NsVrRip2GlobalQueries_Object=MibTableColumn
nsVrRip2GlobalQueries=_NsVrRip2GlobalQueries_Object((1,3,6,1,4,1,3224,18,7,1,1,2),_NsVrRip2GlobalQueries_Type())
nsVrRip2GlobalQueries.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrRip2GlobalQueries.setStatus(_A)
class _NsVrRip2GlobalVRID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_NsVrRip2GlobalVRID_Type.__name__=_C
_NsVrRip2GlobalVRID_Object=MibTableColumn
nsVrRip2GlobalVRID=_NsVrRip2GlobalVRID_Object((1,3,6,1,4,1,3224,18,7,1,1,3),_NsVrRip2GlobalVRID_Type())
nsVrRip2GlobalVRID.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrRip2GlobalVRID.setStatus(_A)
_NsVrRip2IfStatTable_Object=MibTable
nsVrRip2IfStatTable=_NsVrRip2IfStatTable_Object((1,3,6,1,4,1,3224,18,7,2))
if mibBuilder.loadTexts:nsVrRip2IfStatTable.setStatus(_A)
_NsVrRip2IfStatEntry_Object=MibTableRow
nsVrRip2IfStatEntry=_NsVrRip2IfStatEntry_Object((1,3,6,1,4,1,3224,18,7,2,1))
nsVrRip2IfStatEntry.setIndexNames((0,_D,_H),(0,_D,_I))
if mibBuilder.loadTexts:nsVrRip2IfStatEntry.setStatus(_A)
_NsVrRip2IfStatAddress_Type=IpAddress
_NsVrRip2IfStatAddress_Object=MibTableColumn
nsVrRip2IfStatAddress=_NsVrRip2IfStatAddress_Object((1,3,6,1,4,1,3224,18,7,2,1,1),_NsVrRip2IfStatAddress_Type())
nsVrRip2IfStatAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrRip2IfStatAddress.setStatus(_A)
_NsVrRip2IfStatRcvBadPackets_Type=Counter32
_NsVrRip2IfStatRcvBadPackets_Object=MibTableColumn
nsVrRip2IfStatRcvBadPackets=_NsVrRip2IfStatRcvBadPackets_Object((1,3,6,1,4,1,3224,18,7,2,1,2),_NsVrRip2IfStatRcvBadPackets_Type())
nsVrRip2IfStatRcvBadPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrRip2IfStatRcvBadPackets.setStatus(_A)
_NsVrRip2IfStatRcvBadRoutes_Type=Counter32
_NsVrRip2IfStatRcvBadRoutes_Object=MibTableColumn
nsVrRip2IfStatRcvBadRoutes=_NsVrRip2IfStatRcvBadRoutes_Object((1,3,6,1,4,1,3224,18,7,2,1,3),_NsVrRip2IfStatRcvBadRoutes_Type())
nsVrRip2IfStatRcvBadRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrRip2IfStatRcvBadRoutes.setStatus(_A)
_NsVrRip2IfStatSentUpdates_Type=Counter32
_NsVrRip2IfStatSentUpdates_Object=MibTableColumn
nsVrRip2IfStatSentUpdates=_NsVrRip2IfStatSentUpdates_Object((1,3,6,1,4,1,3224,18,7,2,1,4),_NsVrRip2IfStatSentUpdates_Type())
nsVrRip2IfStatSentUpdates.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrRip2IfStatSentUpdates.setStatus(_A)
_NsVrRip2IfStatStatus_Type=RowStatus
_NsVrRip2IfStatStatus_Object=MibTableColumn
nsVrRip2IfStatStatus=_NsVrRip2IfStatStatus_Object((1,3,6,1,4,1,3224,18,7,2,1,5),_NsVrRip2IfStatStatus_Type())
nsVrRip2IfStatStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:nsVrRip2IfStatStatus.setStatus(_A)
class _NsVrRip2IfStatVRID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_NsVrRip2IfStatVRID_Type.__name__=_C
_NsVrRip2IfStatVRID_Object=MibTableColumn
nsVrRip2IfStatVRID=_NsVrRip2IfStatVRID_Object((1,3,6,1,4,1,3224,18,7,2,1,6),_NsVrRip2IfStatVRID_Type())
nsVrRip2IfStatVRID.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrRip2IfStatVRID.setStatus(_A)
_NsVrRip2IfConfTable_Object=MibTable
nsVrRip2IfConfTable=_NsVrRip2IfConfTable_Object((1,3,6,1,4,1,3224,18,7,3))
if mibBuilder.loadTexts:nsVrRip2IfConfTable.setStatus(_A)
_NsVrRip2IfConfEntry_Object=MibTableRow
nsVrRip2IfConfEntry=_NsVrRip2IfConfEntry_Object((1,3,6,1,4,1,3224,18,7,3,1))
nsVrRip2IfConfEntry.setIndexNames((0,_D,_J),(0,_D,_K))
if mibBuilder.loadTexts:nsVrRip2IfConfEntry.setStatus(_A)
_NsVrRip2IfConfAddress_Type=IpAddress
_NsVrRip2IfConfAddress_Object=MibTableColumn
nsVrRip2IfConfAddress=_NsVrRip2IfConfAddress_Object((1,3,6,1,4,1,3224,18,7,3,1,1),_NsVrRip2IfConfAddress_Type())
nsVrRip2IfConfAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrRip2IfConfAddress.setStatus(_A)
class _NsVrRip2IfConfDomain_Type(RouteTag):defaultHexValue='0000'
_NsVrRip2IfConfDomain_Type.__name__=_L
_NsVrRip2IfConfDomain_Object=MibTableColumn
nsVrRip2IfConfDomain=_NsVrRip2IfConfDomain_Object((1,3,6,1,4,1,3224,18,7,3,1,2),_NsVrRip2IfConfDomain_Type())
nsVrRip2IfConfDomain.setMaxAccess(_E)
if mibBuilder.loadTexts:nsVrRip2IfConfDomain.setStatus('obsolete')
class _NsVrRip2IfConfAuthType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('noAuthentication',1),('simplePassword',2),('md5',3)))
_NsVrRip2IfConfAuthType_Type.__name__=_C
_NsVrRip2IfConfAuthType_Object=MibTableColumn
nsVrRip2IfConfAuthType=_NsVrRip2IfConfAuthType_Object((1,3,6,1,4,1,3224,18,7,3,1,3),_NsVrRip2IfConfAuthType_Type())
nsVrRip2IfConfAuthType.setMaxAccess(_E)
if mibBuilder.loadTexts:nsVrRip2IfConfAuthType.setStatus(_A)
class _NsVrRip2IfConfAuthKey_Type(OctetString):defaultHexValue='';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_NsVrRip2IfConfAuthKey_Type.__name__=_F
_NsVrRip2IfConfAuthKey_Object=MibTableColumn
nsVrRip2IfConfAuthKey=_NsVrRip2IfConfAuthKey_Object((1,3,6,1,4,1,3224,18,7,3,1,4),_NsVrRip2IfConfAuthKey_Type())
nsVrRip2IfConfAuthKey.setMaxAccess(_E)
if mibBuilder.loadTexts:nsVrRip2IfConfAuthKey.setStatus(_A)
class _NsVrRip2IfConfSend_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('doNotSend',1),('ripVersion1',2),('rip1Compatible',3),('ripVersion2',4),('ripV1Demand',5),('ripV2Demand',6)))
_NsVrRip2IfConfSend_Type.__name__=_C
_NsVrRip2IfConfSend_Object=MibTableColumn
nsVrRip2IfConfSend=_NsVrRip2IfConfSend_Object((1,3,6,1,4,1,3224,18,7,3,1,5),_NsVrRip2IfConfSend_Type())
nsVrRip2IfConfSend.setMaxAccess(_E)
if mibBuilder.loadTexts:nsVrRip2IfConfSend.setStatus(_A)
class _NsVrRip2IfConfReceive_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('rip1',1),('rip2',2),('rip1OrRip2',3),('doNotRecieve',4)))
_NsVrRip2IfConfReceive_Type.__name__=_C
_NsVrRip2IfConfReceive_Object=MibTableColumn
nsVrRip2IfConfReceive=_NsVrRip2IfConfReceive_Object((1,3,6,1,4,1,3224,18,7,3,1,6),_NsVrRip2IfConfReceive_Type())
nsVrRip2IfConfReceive.setMaxAccess(_E)
if mibBuilder.loadTexts:nsVrRip2IfConfReceive.setStatus(_A)
class _NsVrRip2IfConfDefaultMetric_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_NsVrRip2IfConfDefaultMetric_Type.__name__=_C
_NsVrRip2IfConfDefaultMetric_Object=MibTableColumn
nsVrRip2IfConfDefaultMetric=_NsVrRip2IfConfDefaultMetric_Object((1,3,6,1,4,1,3224,18,7,3,1,7),_NsVrRip2IfConfDefaultMetric_Type())
nsVrRip2IfConfDefaultMetric.setMaxAccess(_E)
if mibBuilder.loadTexts:nsVrRip2IfConfDefaultMetric.setStatus(_A)
_NsVrRip2IfConfStatus_Type=RowStatus
_NsVrRip2IfConfStatus_Object=MibTableColumn
nsVrRip2IfConfStatus=_NsVrRip2IfConfStatus_Object((1,3,6,1,4,1,3224,18,7,3,1,8),_NsVrRip2IfConfStatus_Type())
nsVrRip2IfConfStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:nsVrRip2IfConfStatus.setStatus(_A)
_NsVrRip2IfConfSrcAddress_Type=IpAddress
_NsVrRip2IfConfSrcAddress_Object=MibTableColumn
nsVrRip2IfConfSrcAddress=_NsVrRip2IfConfSrcAddress_Object((1,3,6,1,4,1,3224,18,7,3,1,9),_NsVrRip2IfConfSrcAddress_Type())
nsVrRip2IfConfSrcAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:nsVrRip2IfConfSrcAddress.setStatus(_A)
class _NsVrRip2IfConfVRID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_NsVrRip2IfConfVRID_Type.__name__=_C
_NsVrRip2IfConfVRID_Object=MibTableColumn
nsVrRip2IfConfVRID=_NsVrRip2IfConfVRID_Object((1,3,6,1,4,1,3224,18,7,3,1,10),_NsVrRip2IfConfVRID_Type())
nsVrRip2IfConfVRID.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrRip2IfConfVRID.setStatus(_A)
_NsVrRip2PeerTable_Object=MibTable
nsVrRip2PeerTable=_NsVrRip2PeerTable_Object((1,3,6,1,4,1,3224,18,7,4))
if mibBuilder.loadTexts:nsVrRip2PeerTable.setStatus(_A)
_NsVrRip2PeerEntry_Object=MibTableRow
nsVrRip2PeerEntry=_NsVrRip2PeerEntry_Object((1,3,6,1,4,1,3224,18,7,4,1))
nsVrRip2PeerEntry.setIndexNames((0,_D,_M),(0,_D,_N),(0,_D,_O))
if mibBuilder.loadTexts:nsVrRip2PeerEntry.setStatus(_A)
_NsVrRip2PeerAddress_Type=IpAddress
_NsVrRip2PeerAddress_Object=MibTableColumn
nsVrRip2PeerAddress=_NsVrRip2PeerAddress_Object((1,3,6,1,4,1,3224,18,7,4,1,1),_NsVrRip2PeerAddress_Type())
nsVrRip2PeerAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrRip2PeerAddress.setStatus(_A)
_NsVrRip2PeerDomain_Type=RouteTag
_NsVrRip2PeerDomain_Object=MibTableColumn
nsVrRip2PeerDomain=_NsVrRip2PeerDomain_Object((1,3,6,1,4,1,3224,18,7,4,1,2),_NsVrRip2PeerDomain_Type())
nsVrRip2PeerDomain.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrRip2PeerDomain.setStatus(_A)
_NsVrRip2PeerLastUpdate_Type=TimeTicks
_NsVrRip2PeerLastUpdate_Object=MibTableColumn
nsVrRip2PeerLastUpdate=_NsVrRip2PeerLastUpdate_Object((1,3,6,1,4,1,3224,18,7,4,1,3),_NsVrRip2PeerLastUpdate_Type())
nsVrRip2PeerLastUpdate.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrRip2PeerLastUpdate.setStatus(_A)
class _NsVrRip2PeerVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_NsVrRip2PeerVersion_Type.__name__=_C
_NsVrRip2PeerVersion_Object=MibTableColumn
nsVrRip2PeerVersion=_NsVrRip2PeerVersion_Object((1,3,6,1,4,1,3224,18,7,4,1,4),_NsVrRip2PeerVersion_Type())
nsVrRip2PeerVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrRip2PeerVersion.setStatus(_A)
_NsVrRip2PeerRcvBadPackets_Type=Counter32
_NsVrRip2PeerRcvBadPackets_Object=MibTableColumn
nsVrRip2PeerRcvBadPackets=_NsVrRip2PeerRcvBadPackets_Object((1,3,6,1,4,1,3224,18,7,4,1,5),_NsVrRip2PeerRcvBadPackets_Type())
nsVrRip2PeerRcvBadPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrRip2PeerRcvBadPackets.setStatus(_A)
_NsVrRip2PeerRcvBadRoutes_Type=Counter32
_NsVrRip2PeerRcvBadRoutes_Object=MibTableColumn
nsVrRip2PeerRcvBadRoutes=_NsVrRip2PeerRcvBadRoutes_Object((1,3,6,1,4,1,3224,18,7,4,1,6),_NsVrRip2PeerRcvBadRoutes_Type())
nsVrRip2PeerRcvBadRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrRip2PeerRcvBadRoutes.setStatus(_A)
class _NsVrRip2PeerVRID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_NsVrRip2PeerVRID_Type.__name__=_C
_NsVrRip2PeerVRID_Object=MibTableColumn
nsVrRip2PeerVRID=_NsVrRip2PeerVRID_Object((1,3,6,1,4,1,3224,18,7,4,1,7),_NsVrRip2PeerVRID_Type())
nsVrRip2PeerVRID.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrRip2PeerVRID.setStatus(_A)
mibBuilder.exportSymbols(_D,**{_L:RouteTag,'nsVrRip2':nsVrRip2,'nsVrRip2GlobalsTable':nsVrRip2GlobalsTable,'nsVrRip2GlobalsEntry':nsVrRip2GlobalsEntry,'nsVrRip2GlobalRouteChanges':nsVrRip2GlobalRouteChanges,'nsVrRip2GlobalQueries':nsVrRip2GlobalQueries,_G:nsVrRip2GlobalVRID,'nsVrRip2IfStatTable':nsVrRip2IfStatTable,'nsVrRip2IfStatEntry':nsVrRip2IfStatEntry,_I:nsVrRip2IfStatAddress,'nsVrRip2IfStatRcvBadPackets':nsVrRip2IfStatRcvBadPackets,'nsVrRip2IfStatRcvBadRoutes':nsVrRip2IfStatRcvBadRoutes,'nsVrRip2IfStatSentUpdates':nsVrRip2IfStatSentUpdates,'nsVrRip2IfStatStatus':nsVrRip2IfStatStatus,_H:nsVrRip2IfStatVRID,'nsVrRip2IfConfTable':nsVrRip2IfConfTable,'nsVrRip2IfConfEntry':nsVrRip2IfConfEntry,_K:nsVrRip2IfConfAddress,'nsVrRip2IfConfDomain':nsVrRip2IfConfDomain,'nsVrRip2IfConfAuthType':nsVrRip2IfConfAuthType,'nsVrRip2IfConfAuthKey':nsVrRip2IfConfAuthKey,'nsVrRip2IfConfSend':nsVrRip2IfConfSend,'nsVrRip2IfConfReceive':nsVrRip2IfConfReceive,'nsVrRip2IfConfDefaultMetric':nsVrRip2IfConfDefaultMetric,'nsVrRip2IfConfStatus':nsVrRip2IfConfStatus,'nsVrRip2IfConfSrcAddress':nsVrRip2IfConfSrcAddress,_J:nsVrRip2IfConfVRID,'nsVrRip2PeerTable':nsVrRip2PeerTable,'nsVrRip2PeerEntry':nsVrRip2PeerEntry,_N:nsVrRip2PeerAddress,_O:nsVrRip2PeerDomain,'nsVrRip2PeerLastUpdate':nsVrRip2PeerLastUpdate,'nsVrRip2PeerVersion':nsVrRip2PeerVersion,'nsVrRip2PeerRcvBadPackets':nsVrRip2PeerRcvBadPackets,'nsVrRip2PeerRcvBadRoutes':nsVrRip2PeerRcvBadRoutes,_M:nsVrRip2PeerVRID})