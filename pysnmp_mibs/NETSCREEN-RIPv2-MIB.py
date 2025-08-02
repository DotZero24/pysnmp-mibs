_O='nsRip2PeerVRID'
_N='nsRip2PeerDomain'
_M='nsRip2PeerAddress'
_L='RouteTag'
_K='nsRip2IfConfVRID'
_J='nsRip2IfConfAddress'
_I='nsRip2IfStatVRID'
_H='nsRip2IfStatAddress'
_G='nsRip2GlobalVRID'
_F='OctetString'
_E='read-create'
_D='NETSCREEN-RIPv2-MIB'
_C='Integer32'
_B='read-only'
_A='deprecated'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
netscreenVR,=mibBuilder.importSymbols('NETSCREEN-SMI','netscreenVR')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
nsRip2=ModuleIdentity((1,3,6,1,4,1,3224,18,4))
class RouteTag(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_NsRip2GlobalsTable_Object=MibTable
nsRip2GlobalsTable=_NsRip2GlobalsTable_Object((1,3,6,1,4,1,3224,18,4,1))
if mibBuilder.loadTexts:nsRip2GlobalsTable.setStatus(_A)
_NsRip2GlobalsEntry_Object=MibTableRow
nsRip2GlobalsEntry=_NsRip2GlobalsEntry_Object((1,3,6,1,4,1,3224,18,4,1,1))
nsRip2GlobalsEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:nsRip2GlobalsEntry.setStatus(_A)
_NsRip2GlobalRouteChanges_Type=Counter32
_NsRip2GlobalRouteChanges_Object=MibTableColumn
nsRip2GlobalRouteChanges=_NsRip2GlobalRouteChanges_Object((1,3,6,1,4,1,3224,18,4,1,1,1),_NsRip2GlobalRouteChanges_Type())
nsRip2GlobalRouteChanges.setMaxAccess(_B)
if mibBuilder.loadTexts:nsRip2GlobalRouteChanges.setStatus(_A)
_NsRip2GlobalQueries_Type=Counter32
_NsRip2GlobalQueries_Object=MibTableColumn
nsRip2GlobalQueries=_NsRip2GlobalQueries_Object((1,3,6,1,4,1,3224,18,4,1,1,2),_NsRip2GlobalQueries_Type())
nsRip2GlobalQueries.setMaxAccess(_B)
if mibBuilder.loadTexts:nsRip2GlobalQueries.setStatus(_A)
class _NsRip2GlobalVRID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_NsRip2GlobalVRID_Type.__name__=_C
_NsRip2GlobalVRID_Object=MibTableColumn
nsRip2GlobalVRID=_NsRip2GlobalVRID_Object((1,3,6,1,4,1,3224,18,4,1,1,3),_NsRip2GlobalVRID_Type())
nsRip2GlobalVRID.setMaxAccess(_B)
if mibBuilder.loadTexts:nsRip2GlobalVRID.setStatus(_A)
_NsRip2IfStatTable_Object=MibTable
nsRip2IfStatTable=_NsRip2IfStatTable_Object((1,3,6,1,4,1,3224,18,4,2))
if mibBuilder.loadTexts:nsRip2IfStatTable.setStatus(_A)
_NsRip2IfStatEntry_Object=MibTableRow
nsRip2IfStatEntry=_NsRip2IfStatEntry_Object((1,3,6,1,4,1,3224,18,4,2,1))
nsRip2IfStatEntry.setIndexNames((0,_D,_H),(0,_D,_I))
if mibBuilder.loadTexts:nsRip2IfStatEntry.setStatus(_A)
_NsRip2IfStatAddress_Type=IpAddress
_NsRip2IfStatAddress_Object=MibTableColumn
nsRip2IfStatAddress=_NsRip2IfStatAddress_Object((1,3,6,1,4,1,3224,18,4,2,1,1),_NsRip2IfStatAddress_Type())
nsRip2IfStatAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:nsRip2IfStatAddress.setStatus(_A)
_NsRip2IfStatRcvBadPackets_Type=Counter32
_NsRip2IfStatRcvBadPackets_Object=MibTableColumn
nsRip2IfStatRcvBadPackets=_NsRip2IfStatRcvBadPackets_Object((1,3,6,1,4,1,3224,18,4,2,1,2),_NsRip2IfStatRcvBadPackets_Type())
nsRip2IfStatRcvBadPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:nsRip2IfStatRcvBadPackets.setStatus(_A)
_NsRip2IfStatRcvBadRoutes_Type=Counter32
_NsRip2IfStatRcvBadRoutes_Object=MibTableColumn
nsRip2IfStatRcvBadRoutes=_NsRip2IfStatRcvBadRoutes_Object((1,3,6,1,4,1,3224,18,4,2,1,3),_NsRip2IfStatRcvBadRoutes_Type())
nsRip2IfStatRcvBadRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:nsRip2IfStatRcvBadRoutes.setStatus(_A)
_NsRip2IfStatSentUpdates_Type=Counter32
_NsRip2IfStatSentUpdates_Object=MibTableColumn
nsRip2IfStatSentUpdates=_NsRip2IfStatSentUpdates_Object((1,3,6,1,4,1,3224,18,4,2,1,4),_NsRip2IfStatSentUpdates_Type())
nsRip2IfStatSentUpdates.setMaxAccess(_B)
if mibBuilder.loadTexts:nsRip2IfStatSentUpdates.setStatus(_A)
_NsRip2IfStatStatus_Type=RowStatus
_NsRip2IfStatStatus_Object=MibTableColumn
nsRip2IfStatStatus=_NsRip2IfStatStatus_Object((1,3,6,1,4,1,3224,18,4,2,1,5),_NsRip2IfStatStatus_Type())
nsRip2IfStatStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:nsRip2IfStatStatus.setStatus(_A)
class _NsRip2IfStatVRID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_NsRip2IfStatVRID_Type.__name__=_C
_NsRip2IfStatVRID_Object=MibTableColumn
nsRip2IfStatVRID=_NsRip2IfStatVRID_Object((1,3,6,1,4,1,3224,18,4,2,1,6),_NsRip2IfStatVRID_Type())
nsRip2IfStatVRID.setMaxAccess(_B)
if mibBuilder.loadTexts:nsRip2IfStatVRID.setStatus(_A)
_NsRip2IfConfTable_Object=MibTable
nsRip2IfConfTable=_NsRip2IfConfTable_Object((1,3,6,1,4,1,3224,18,4,3))
if mibBuilder.loadTexts:nsRip2IfConfTable.setStatus(_A)
_NsRip2IfConfEntry_Object=MibTableRow
nsRip2IfConfEntry=_NsRip2IfConfEntry_Object((1,3,6,1,4,1,3224,18,4,3,1))
nsRip2IfConfEntry.setIndexNames((0,_D,_J),(0,_D,_K))
if mibBuilder.loadTexts:nsRip2IfConfEntry.setStatus(_A)
_NsRip2IfConfAddress_Type=IpAddress
_NsRip2IfConfAddress_Object=MibTableColumn
nsRip2IfConfAddress=_NsRip2IfConfAddress_Object((1,3,6,1,4,1,3224,18,4,3,1,1),_NsRip2IfConfAddress_Type())
nsRip2IfConfAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:nsRip2IfConfAddress.setStatus(_A)
class _NsRip2IfConfDomain_Type(RouteTag):defaultHexValue='0000'
_NsRip2IfConfDomain_Type.__name__=_L
_NsRip2IfConfDomain_Object=MibTableColumn
nsRip2IfConfDomain=_NsRip2IfConfDomain_Object((1,3,6,1,4,1,3224,18,4,3,1,2),_NsRip2IfConfDomain_Type())
nsRip2IfConfDomain.setMaxAccess(_E)
if mibBuilder.loadTexts:nsRip2IfConfDomain.setStatus('obsolete')
class _NsRip2IfConfAuthType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('noAuthentication',1),('simplePassword',2),('md5',3)))
_NsRip2IfConfAuthType_Type.__name__=_C
_NsRip2IfConfAuthType_Object=MibTableColumn
nsRip2IfConfAuthType=_NsRip2IfConfAuthType_Object((1,3,6,1,4,1,3224,18,4,3,1,3),_NsRip2IfConfAuthType_Type())
nsRip2IfConfAuthType.setMaxAccess(_E)
if mibBuilder.loadTexts:nsRip2IfConfAuthType.setStatus(_A)
class _NsRip2IfConfAuthKey_Type(OctetString):defaultHexValue='';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_NsRip2IfConfAuthKey_Type.__name__=_F
_NsRip2IfConfAuthKey_Object=MibTableColumn
nsRip2IfConfAuthKey=_NsRip2IfConfAuthKey_Object((1,3,6,1,4,1,3224,18,4,3,1,4),_NsRip2IfConfAuthKey_Type())
nsRip2IfConfAuthKey.setMaxAccess(_E)
if mibBuilder.loadTexts:nsRip2IfConfAuthKey.setStatus(_A)
class _NsRip2IfConfSend_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('doNotSend',1),('ripVersion1',2),('rip1Compatible',3),('ripVersion2',4),('ripV1Demand',5),('ripV2Demand',6)))
_NsRip2IfConfSend_Type.__name__=_C
_NsRip2IfConfSend_Object=MibTableColumn
nsRip2IfConfSend=_NsRip2IfConfSend_Object((1,3,6,1,4,1,3224,18,4,3,1,5),_NsRip2IfConfSend_Type())
nsRip2IfConfSend.setMaxAccess(_E)
if mibBuilder.loadTexts:nsRip2IfConfSend.setStatus(_A)
class _NsRip2IfConfReceive_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('rip1',1),('rip2',2),('rip1OrRip2',3),('doNotRecieve',4)))
_NsRip2IfConfReceive_Type.__name__=_C
_NsRip2IfConfReceive_Object=MibTableColumn
nsRip2IfConfReceive=_NsRip2IfConfReceive_Object((1,3,6,1,4,1,3224,18,4,3,1,6),_NsRip2IfConfReceive_Type())
nsRip2IfConfReceive.setMaxAccess(_E)
if mibBuilder.loadTexts:nsRip2IfConfReceive.setStatus(_A)
class _NsRip2IfConfDefaultMetric_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_NsRip2IfConfDefaultMetric_Type.__name__=_C
_NsRip2IfConfDefaultMetric_Object=MibTableColumn
nsRip2IfConfDefaultMetric=_NsRip2IfConfDefaultMetric_Object((1,3,6,1,4,1,3224,18,4,3,1,7),_NsRip2IfConfDefaultMetric_Type())
nsRip2IfConfDefaultMetric.setMaxAccess(_E)
if mibBuilder.loadTexts:nsRip2IfConfDefaultMetric.setStatus(_A)
_NsRip2IfConfStatus_Type=RowStatus
_NsRip2IfConfStatus_Object=MibTableColumn
nsRip2IfConfStatus=_NsRip2IfConfStatus_Object((1,3,6,1,4,1,3224,18,4,3,1,8),_NsRip2IfConfStatus_Type())
nsRip2IfConfStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:nsRip2IfConfStatus.setStatus(_A)
_NsRip2IfConfSrcAddress_Type=IpAddress
_NsRip2IfConfSrcAddress_Object=MibTableColumn
nsRip2IfConfSrcAddress=_NsRip2IfConfSrcAddress_Object((1,3,6,1,4,1,3224,18,4,3,1,9),_NsRip2IfConfSrcAddress_Type())
nsRip2IfConfSrcAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:nsRip2IfConfSrcAddress.setStatus(_A)
class _NsRip2IfConfVRID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_NsRip2IfConfVRID_Type.__name__=_C
_NsRip2IfConfVRID_Object=MibTableColumn
nsRip2IfConfVRID=_NsRip2IfConfVRID_Object((1,3,6,1,4,1,3224,18,4,3,1,10),_NsRip2IfConfVRID_Type())
nsRip2IfConfVRID.setMaxAccess(_B)
if mibBuilder.loadTexts:nsRip2IfConfVRID.setStatus(_A)
_NsRip2PeerTable_Object=MibTable
nsRip2PeerTable=_NsRip2PeerTable_Object((1,3,6,1,4,1,3224,18,4,4))
if mibBuilder.loadTexts:nsRip2PeerTable.setStatus(_A)
_NsRip2PeerEntry_Object=MibTableRow
nsRip2PeerEntry=_NsRip2PeerEntry_Object((1,3,6,1,4,1,3224,18,4,4,1))
nsRip2PeerEntry.setIndexNames((0,_D,_M),(0,_D,_N),(0,_D,_O))
if mibBuilder.loadTexts:nsRip2PeerEntry.setStatus(_A)
_NsRip2PeerAddress_Type=IpAddress
_NsRip2PeerAddress_Object=MibTableColumn
nsRip2PeerAddress=_NsRip2PeerAddress_Object((1,3,6,1,4,1,3224,18,4,4,1,1),_NsRip2PeerAddress_Type())
nsRip2PeerAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:nsRip2PeerAddress.setStatus(_A)
_NsRip2PeerDomain_Type=RouteTag
_NsRip2PeerDomain_Object=MibTableColumn
nsRip2PeerDomain=_NsRip2PeerDomain_Object((1,3,6,1,4,1,3224,18,4,4,1,2),_NsRip2PeerDomain_Type())
nsRip2PeerDomain.setMaxAccess(_B)
if mibBuilder.loadTexts:nsRip2PeerDomain.setStatus(_A)
_NsRip2PeerLastUpdate_Type=TimeTicks
_NsRip2PeerLastUpdate_Object=MibTableColumn
nsRip2PeerLastUpdate=_NsRip2PeerLastUpdate_Object((1,3,6,1,4,1,3224,18,4,4,1,3),_NsRip2PeerLastUpdate_Type())
nsRip2PeerLastUpdate.setMaxAccess(_B)
if mibBuilder.loadTexts:nsRip2PeerLastUpdate.setStatus(_A)
class _NsRip2PeerVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_NsRip2PeerVersion_Type.__name__=_C
_NsRip2PeerVersion_Object=MibTableColumn
nsRip2PeerVersion=_NsRip2PeerVersion_Object((1,3,6,1,4,1,3224,18,4,4,1,4),_NsRip2PeerVersion_Type())
nsRip2PeerVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:nsRip2PeerVersion.setStatus(_A)
_NsRip2PeerRcvBadPackets_Type=Counter32
_NsRip2PeerRcvBadPackets_Object=MibTableColumn
nsRip2PeerRcvBadPackets=_NsRip2PeerRcvBadPackets_Object((1,3,6,1,4,1,3224,18,4,4,1,5),_NsRip2PeerRcvBadPackets_Type())
nsRip2PeerRcvBadPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:nsRip2PeerRcvBadPackets.setStatus(_A)
_NsRip2PeerRcvBadRoutes_Type=Counter32
_NsRip2PeerRcvBadRoutes_Object=MibTableColumn
nsRip2PeerRcvBadRoutes=_NsRip2PeerRcvBadRoutes_Object((1,3,6,1,4,1,3224,18,4,4,1,6),_NsRip2PeerRcvBadRoutes_Type())
nsRip2PeerRcvBadRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:nsRip2PeerRcvBadRoutes.setStatus(_A)
class _NsRip2PeerVRID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_NsRip2PeerVRID_Type.__name__=_C
_NsRip2PeerVRID_Object=MibTableColumn
nsRip2PeerVRID=_NsRip2PeerVRID_Object((1,3,6,1,4,1,3224,18,4,4,1,7),_NsRip2PeerVRID_Type())
nsRip2PeerVRID.setMaxAccess(_B)
if mibBuilder.loadTexts:nsRip2PeerVRID.setStatus(_A)
mibBuilder.exportSymbols(_D,**{_L:RouteTag,'nsRip2':nsRip2,'nsRip2GlobalsTable':nsRip2GlobalsTable,'nsRip2GlobalsEntry':nsRip2GlobalsEntry,'nsRip2GlobalRouteChanges':nsRip2GlobalRouteChanges,'nsRip2GlobalQueries':nsRip2GlobalQueries,_G:nsRip2GlobalVRID,'nsRip2IfStatTable':nsRip2IfStatTable,'nsRip2IfStatEntry':nsRip2IfStatEntry,_H:nsRip2IfStatAddress,'nsRip2IfStatRcvBadPackets':nsRip2IfStatRcvBadPackets,'nsRip2IfStatRcvBadRoutes':nsRip2IfStatRcvBadRoutes,'nsRip2IfStatSentUpdates':nsRip2IfStatSentUpdates,'nsRip2IfStatStatus':nsRip2IfStatStatus,_I:nsRip2IfStatVRID,'nsRip2IfConfTable':nsRip2IfConfTable,'nsRip2IfConfEntry':nsRip2IfConfEntry,_J:nsRip2IfConfAddress,'nsRip2IfConfDomain':nsRip2IfConfDomain,'nsRip2IfConfAuthType':nsRip2IfConfAuthType,'nsRip2IfConfAuthKey':nsRip2IfConfAuthKey,'nsRip2IfConfSend':nsRip2IfConfSend,'nsRip2IfConfReceive':nsRip2IfConfReceive,'nsRip2IfConfDefaultMetric':nsRip2IfConfDefaultMetric,'nsRip2IfConfStatus':nsRip2IfConfStatus,'nsRip2IfConfSrcAddress':nsRip2IfConfSrcAddress,_K:nsRip2IfConfVRID,'nsRip2PeerTable':nsRip2PeerTable,'nsRip2PeerEntry':nsRip2PeerEntry,_M:nsRip2PeerAddress,_N:nsRip2PeerDomain,'nsRip2PeerLastUpdate':nsRip2PeerLastUpdate,'nsRip2PeerVersion':nsRip2PeerVersion,'nsRip2PeerRcvBadPackets':nsRip2PeerRcvBadPackets,'nsRip2PeerRcvBadRoutes':nsRip2PeerRcvBadRoutes,_O:nsRip2PeerVRID})