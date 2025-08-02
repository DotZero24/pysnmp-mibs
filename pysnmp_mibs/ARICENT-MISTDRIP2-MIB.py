_O='fsMIStdRip2GlobalEntry'
_N='fsMIStdRip2PeerDomain'
_M='fsMIStdRip2PeerAddress'
_L='RouteTag'
_K='fsMIStdRip2IfConfAddress'
_J='fsMIStdRip2IfStatAddress'
_I='OctetString'
_H='not-accessible'
_G='fsMIRipContextId'
_F='ARICENT-MIRIP2-MIB'
_E='ARICENT-MISTDRIP2-MIB'
_D='Integer32'
_C='read-create'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_I,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsMIRip2GlobalEntry,fsMIRipContextId=mibBuilder.importSymbols(_F,'fsMIRip2GlobalEntry',_G)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
fsMIStdRip=ModuleIdentity((1,3,6,1,4,1,2076,152))
if mibBuilder.loadTexts:fsMIStdRip.setRevisions(('2012-09-05 00:00',))
class RouteTag(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_FsMIStdRip2Globals_ObjectIdentity=ObjectIdentity
fsMIStdRip2Globals=_FsMIStdRip2Globals_ObjectIdentity((1,3,6,1,4,1,2076,152,1))
_FsMIStdRip2GlobalTable_Object=MibTable
fsMIStdRip2GlobalTable=_FsMIStdRip2GlobalTable_Object((1,3,6,1,4,1,2076,152,1,1))
if mibBuilder.loadTexts:fsMIStdRip2GlobalTable.setStatus(_A)
_FsMIStdRip2GlobalEntry_Object=MibTableRow
fsMIStdRip2GlobalEntry=_FsMIStdRip2GlobalEntry_Object((1,3,6,1,4,1,2076,152,1,1,1))
if mibBuilder.loadTexts:fsMIStdRip2GlobalEntry.setStatus(_A)
_FsMIStdRip2GlobalRouteChanges_Type=Counter32
_FsMIStdRip2GlobalRouteChanges_Object=MibTableColumn
fsMIStdRip2GlobalRouteChanges=_FsMIStdRip2GlobalRouteChanges_Object((1,3,6,1,4,1,2076,152,1,1,1,1),_FsMIStdRip2GlobalRouteChanges_Type())
fsMIStdRip2GlobalRouteChanges.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdRip2GlobalRouteChanges.setStatus(_A)
_FsMIStdRip2GlobalQueries_Type=Counter32
_FsMIStdRip2GlobalQueries_Object=MibTableColumn
fsMIStdRip2GlobalQueries=_FsMIStdRip2GlobalQueries_Object((1,3,6,1,4,1,2076,152,1,1,1,2),_FsMIStdRip2GlobalQueries_Type())
fsMIStdRip2GlobalQueries.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdRip2GlobalQueries.setStatus(_A)
_FsMIStdRip2IfStatTable_Object=MibTable
fsMIStdRip2IfStatTable=_FsMIStdRip2IfStatTable_Object((1,3,6,1,4,1,2076,152,2))
if mibBuilder.loadTexts:fsMIStdRip2IfStatTable.setStatus(_A)
_FsMIStdRip2IfStatEntry_Object=MibTableRow
fsMIStdRip2IfStatEntry=_FsMIStdRip2IfStatEntry_Object((1,3,6,1,4,1,2076,152,2,1))
fsMIStdRip2IfStatEntry.setIndexNames((0,_F,_G),(0,_E,_J))
if mibBuilder.loadTexts:fsMIStdRip2IfStatEntry.setStatus(_A)
_FsMIStdRip2IfStatAddress_Type=IpAddress
_FsMIStdRip2IfStatAddress_Object=MibTableColumn
fsMIStdRip2IfStatAddress=_FsMIStdRip2IfStatAddress_Object((1,3,6,1,4,1,2076,152,2,1,1),_FsMIStdRip2IfStatAddress_Type())
fsMIStdRip2IfStatAddress.setMaxAccess(_H)
if mibBuilder.loadTexts:fsMIStdRip2IfStatAddress.setStatus(_A)
_FsMIStdRip2IfStatRcvBadPackets_Type=Counter32
_FsMIStdRip2IfStatRcvBadPackets_Object=MibTableColumn
fsMIStdRip2IfStatRcvBadPackets=_FsMIStdRip2IfStatRcvBadPackets_Object((1,3,6,1,4,1,2076,152,2,1,2),_FsMIStdRip2IfStatRcvBadPackets_Type())
fsMIStdRip2IfStatRcvBadPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdRip2IfStatRcvBadPackets.setStatus(_A)
_FsMIStdRip2IfStatRcvBadRoutes_Type=Counter32
_FsMIStdRip2IfStatRcvBadRoutes_Object=MibTableColumn
fsMIStdRip2IfStatRcvBadRoutes=_FsMIStdRip2IfStatRcvBadRoutes_Object((1,3,6,1,4,1,2076,152,2,1,3),_FsMIStdRip2IfStatRcvBadRoutes_Type())
fsMIStdRip2IfStatRcvBadRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdRip2IfStatRcvBadRoutes.setStatus(_A)
_FsMIStdRip2IfStatSentUpdates_Type=Counter32
_FsMIStdRip2IfStatSentUpdates_Object=MibTableColumn
fsMIStdRip2IfStatSentUpdates=_FsMIStdRip2IfStatSentUpdates_Object((1,3,6,1,4,1,2076,152,2,1,4),_FsMIStdRip2IfStatSentUpdates_Type())
fsMIStdRip2IfStatSentUpdates.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdRip2IfStatSentUpdates.setStatus(_A)
_FsMIStdRip2IfStatStatus_Type=RowStatus
_FsMIStdRip2IfStatStatus_Object=MibTableColumn
fsMIStdRip2IfStatStatus=_FsMIStdRip2IfStatStatus_Object((1,3,6,1,4,1,2076,152,2,1,5),_FsMIStdRip2IfStatStatus_Type())
fsMIStdRip2IfStatStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIStdRip2IfStatStatus.setStatus(_A)
_FsMIStdRip2IfStatPeriodicUpdates_Type=Counter32
_FsMIStdRip2IfStatPeriodicUpdates_Object=MibTableColumn
fsMIStdRip2IfStatPeriodicUpdates=_FsMIStdRip2IfStatPeriodicUpdates_Object((1,3,6,1,4,1,2076,152,2,1,6),_FsMIStdRip2IfStatPeriodicUpdates_Type())
fsMIStdRip2IfStatPeriodicUpdates.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdRip2IfStatPeriodicUpdates.setStatus(_A)
_FsMIStdRip2IfStatRcvBadAuthPackets_Type=Counter32
_FsMIStdRip2IfStatRcvBadAuthPackets_Object=MibTableColumn
fsMIStdRip2IfStatRcvBadAuthPackets=_FsMIStdRip2IfStatRcvBadAuthPackets_Object((1,3,6,1,4,1,2076,152,2,1,7),_FsMIStdRip2IfStatRcvBadAuthPackets_Type())
fsMIStdRip2IfStatRcvBadAuthPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdRip2IfStatRcvBadAuthPackets.setStatus(_A)
_FsMIStdRip2IfConfTable_Object=MibTable
fsMIStdRip2IfConfTable=_FsMIStdRip2IfConfTable_Object((1,3,6,1,4,1,2076,152,3))
if mibBuilder.loadTexts:fsMIStdRip2IfConfTable.setStatus(_A)
_FsMIStdRip2IfConfEntry_Object=MibTableRow
fsMIStdRip2IfConfEntry=_FsMIStdRip2IfConfEntry_Object((1,3,6,1,4,1,2076,152,3,1))
fsMIStdRip2IfConfEntry.setIndexNames((0,_F,_G),(0,_E,_K))
if mibBuilder.loadTexts:fsMIStdRip2IfConfEntry.setStatus(_A)
_FsMIStdRip2IfConfAddress_Type=IpAddress
_FsMIStdRip2IfConfAddress_Object=MibTableColumn
fsMIStdRip2IfConfAddress=_FsMIStdRip2IfConfAddress_Object((1,3,6,1,4,1,2076,152,3,1,1),_FsMIStdRip2IfConfAddress_Type())
fsMIStdRip2IfConfAddress.setMaxAccess(_H)
if mibBuilder.loadTexts:fsMIStdRip2IfConfAddress.setStatus(_A)
class _FsMIStdRip2IfConfDomain_Type(RouteTag):defaultHexValue='0000'
_FsMIStdRip2IfConfDomain_Type.__name__=_L
_FsMIStdRip2IfConfDomain_Object=MibTableColumn
fsMIStdRip2IfConfDomain=_FsMIStdRip2IfConfDomain_Object((1,3,6,1,4,1,2076,152,3,1,2),_FsMIStdRip2IfConfDomain_Type())
fsMIStdRip2IfConfDomain.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIStdRip2IfConfDomain.setStatus('obsolete')
class _FsMIStdRip2IfConfAuthType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('noAuthentication',1),('simplePassword',2),('md5',3),('sha1',4),('sha256',5),('sha384',6),('sha512',7)))
_FsMIStdRip2IfConfAuthType_Type.__name__=_D
_FsMIStdRip2IfConfAuthType_Object=MibTableColumn
fsMIStdRip2IfConfAuthType=_FsMIStdRip2IfConfAuthType_Object((1,3,6,1,4,1,2076,152,3,1,3),_FsMIStdRip2IfConfAuthType_Type())
fsMIStdRip2IfConfAuthType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIStdRip2IfConfAuthType.setStatus(_A)
class _FsMIStdRip2IfConfAuthKey_Type(OctetString):defaultHexValue='';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_FsMIStdRip2IfConfAuthKey_Type.__name__=_I
_FsMIStdRip2IfConfAuthKey_Object=MibTableColumn
fsMIStdRip2IfConfAuthKey=_FsMIStdRip2IfConfAuthKey_Object((1,3,6,1,4,1,2076,152,3,1,4),_FsMIStdRip2IfConfAuthKey_Type())
fsMIStdRip2IfConfAuthKey.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIStdRip2IfConfAuthKey.setStatus(_A)
class _FsMIStdRip2IfConfSend_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('doNotSend',1),('ripVersion1',2),('rip1Compatible',3),('ripVersion2',4),('ripV1Demand',5),('ripV2Demand',6)))
_FsMIStdRip2IfConfSend_Type.__name__=_D
_FsMIStdRip2IfConfSend_Object=MibTableColumn
fsMIStdRip2IfConfSend=_FsMIStdRip2IfConfSend_Object((1,3,6,1,4,1,2076,152,3,1,5),_FsMIStdRip2IfConfSend_Type())
fsMIStdRip2IfConfSend.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIStdRip2IfConfSend.setStatus(_A)
class _FsMIStdRip2IfConfReceive_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('rip1',1),('rip2',2),('rip1OrRip2',3),('doNotRecieve',4)))
_FsMIStdRip2IfConfReceive_Type.__name__=_D
_FsMIStdRip2IfConfReceive_Object=MibTableColumn
fsMIStdRip2IfConfReceive=_FsMIStdRip2IfConfReceive_Object((1,3,6,1,4,1,2076,152,3,1,6),_FsMIStdRip2IfConfReceive_Type())
fsMIStdRip2IfConfReceive.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIStdRip2IfConfReceive.setStatus(_A)
class _FsMIStdRip2IfConfDefaultMetric_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_FsMIStdRip2IfConfDefaultMetric_Type.__name__=_D
_FsMIStdRip2IfConfDefaultMetric_Object=MibTableColumn
fsMIStdRip2IfConfDefaultMetric=_FsMIStdRip2IfConfDefaultMetric_Object((1,3,6,1,4,1,2076,152,3,1,7),_FsMIStdRip2IfConfDefaultMetric_Type())
fsMIStdRip2IfConfDefaultMetric.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIStdRip2IfConfDefaultMetric.setStatus(_A)
_FsMIStdRip2IfConfStatus_Type=RowStatus
_FsMIStdRip2IfConfStatus_Object=MibTableColumn
fsMIStdRip2IfConfStatus=_FsMIStdRip2IfConfStatus_Object((1,3,6,1,4,1,2076,152,3,1,8),_FsMIStdRip2IfConfStatus_Type())
fsMIStdRip2IfConfStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIStdRip2IfConfStatus.setStatus(_A)
_FsMIStdRip2IfConfSrcAddress_Type=IpAddress
_FsMIStdRip2IfConfSrcAddress_Object=MibTableColumn
fsMIStdRip2IfConfSrcAddress=_FsMIStdRip2IfConfSrcAddress_Object((1,3,6,1,4,1,2076,152,3,1,9),_FsMIStdRip2IfConfSrcAddress_Type())
fsMIStdRip2IfConfSrcAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIStdRip2IfConfSrcAddress.setStatus(_A)
_FsMIStdRip2PeerTable_Object=MibTable
fsMIStdRip2PeerTable=_FsMIStdRip2PeerTable_Object((1,3,6,1,4,1,2076,152,4))
if mibBuilder.loadTexts:fsMIStdRip2PeerTable.setStatus(_A)
_FsMIStdRip2PeerEntry_Object=MibTableRow
fsMIStdRip2PeerEntry=_FsMIStdRip2PeerEntry_Object((1,3,6,1,4,1,2076,152,4,1))
fsMIStdRip2PeerEntry.setIndexNames((0,_F,_G),(0,_E,_M),(0,_E,_N))
if mibBuilder.loadTexts:fsMIStdRip2PeerEntry.setStatus(_A)
_FsMIStdRip2PeerAddress_Type=IpAddress
_FsMIStdRip2PeerAddress_Object=MibTableColumn
fsMIStdRip2PeerAddress=_FsMIStdRip2PeerAddress_Object((1,3,6,1,4,1,2076,152,4,1,1),_FsMIStdRip2PeerAddress_Type())
fsMIStdRip2PeerAddress.setMaxAccess(_H)
if mibBuilder.loadTexts:fsMIStdRip2PeerAddress.setStatus(_A)
_FsMIStdRip2PeerDomain_Type=RouteTag
_FsMIStdRip2PeerDomain_Object=MibTableColumn
fsMIStdRip2PeerDomain=_FsMIStdRip2PeerDomain_Object((1,3,6,1,4,1,2076,152,4,1,2),_FsMIStdRip2PeerDomain_Type())
fsMIStdRip2PeerDomain.setMaxAccess(_H)
if mibBuilder.loadTexts:fsMIStdRip2PeerDomain.setStatus(_A)
_FsMIStdRip2PeerLastUpdate_Type=TimeTicks
_FsMIStdRip2PeerLastUpdate_Object=MibTableColumn
fsMIStdRip2PeerLastUpdate=_FsMIStdRip2PeerLastUpdate_Object((1,3,6,1,4,1,2076,152,4,1,3),_FsMIStdRip2PeerLastUpdate_Type())
fsMIStdRip2PeerLastUpdate.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdRip2PeerLastUpdate.setStatus(_A)
class _FsMIStdRip2PeerVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FsMIStdRip2PeerVersion_Type.__name__=_D
_FsMIStdRip2PeerVersion_Object=MibTableColumn
fsMIStdRip2PeerVersion=_FsMIStdRip2PeerVersion_Object((1,3,6,1,4,1,2076,152,4,1,4),_FsMIStdRip2PeerVersion_Type())
fsMIStdRip2PeerVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdRip2PeerVersion.setStatus(_A)
_FsMIStdRip2PeerRcvBadPackets_Type=Counter32
_FsMIStdRip2PeerRcvBadPackets_Object=MibTableColumn
fsMIStdRip2PeerRcvBadPackets=_FsMIStdRip2PeerRcvBadPackets_Object((1,3,6,1,4,1,2076,152,4,1,5),_FsMIStdRip2PeerRcvBadPackets_Type())
fsMIStdRip2PeerRcvBadPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdRip2PeerRcvBadPackets.setStatus(_A)
_FsMIStdRip2PeerRcvBadRoutes_Type=Counter32
_FsMIStdRip2PeerRcvBadRoutes_Object=MibTableColumn
fsMIStdRip2PeerRcvBadRoutes=_FsMIStdRip2PeerRcvBadRoutes_Object((1,3,6,1,4,1,2076,152,4,1,6),_FsMIStdRip2PeerRcvBadRoutes_Type())
fsMIStdRip2PeerRcvBadRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdRip2PeerRcvBadRoutes.setStatus(_A)
class _FsMIStdRip2PeerInUseKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FsMIStdRip2PeerInUseKey_Type.__name__=_D
_FsMIStdRip2PeerInUseKey_Object=MibTableColumn
fsMIStdRip2PeerInUseKey=_FsMIStdRip2PeerInUseKey_Object((1,3,6,1,4,1,2076,152,4,1,7),_FsMIStdRip2PeerInUseKey_Type())
fsMIStdRip2PeerInUseKey.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIStdRip2PeerInUseKey.setStatus(_A)
fsMIRip2GlobalEntry.registerAugmentions((_E,_O))
fsMIStdRip2GlobalEntry.setIndexNames(*fsMIRip2GlobalEntry.getIndexNames())
mibBuilder.exportSymbols(_E,**{_L:RouteTag,'fsMIStdRip':fsMIStdRip,'fsMIStdRip2Globals':fsMIStdRip2Globals,'fsMIStdRip2GlobalTable':fsMIStdRip2GlobalTable,_O:fsMIStdRip2GlobalEntry,'fsMIStdRip2GlobalRouteChanges':fsMIStdRip2GlobalRouteChanges,'fsMIStdRip2GlobalQueries':fsMIStdRip2GlobalQueries,'fsMIStdRip2IfStatTable':fsMIStdRip2IfStatTable,'fsMIStdRip2IfStatEntry':fsMIStdRip2IfStatEntry,_J:fsMIStdRip2IfStatAddress,'fsMIStdRip2IfStatRcvBadPackets':fsMIStdRip2IfStatRcvBadPackets,'fsMIStdRip2IfStatRcvBadRoutes':fsMIStdRip2IfStatRcvBadRoutes,'fsMIStdRip2IfStatSentUpdates':fsMIStdRip2IfStatSentUpdates,'fsMIStdRip2IfStatStatus':fsMIStdRip2IfStatStatus,'fsMIStdRip2IfStatPeriodicUpdates':fsMIStdRip2IfStatPeriodicUpdates,'fsMIStdRip2IfStatRcvBadAuthPackets':fsMIStdRip2IfStatRcvBadAuthPackets,'fsMIStdRip2IfConfTable':fsMIStdRip2IfConfTable,'fsMIStdRip2IfConfEntry':fsMIStdRip2IfConfEntry,_K:fsMIStdRip2IfConfAddress,'fsMIStdRip2IfConfDomain':fsMIStdRip2IfConfDomain,'fsMIStdRip2IfConfAuthType':fsMIStdRip2IfConfAuthType,'fsMIStdRip2IfConfAuthKey':fsMIStdRip2IfConfAuthKey,'fsMIStdRip2IfConfSend':fsMIStdRip2IfConfSend,'fsMIStdRip2IfConfReceive':fsMIStdRip2IfConfReceive,'fsMIStdRip2IfConfDefaultMetric':fsMIStdRip2IfConfDefaultMetric,'fsMIStdRip2IfConfStatus':fsMIStdRip2IfConfStatus,'fsMIStdRip2IfConfSrcAddress':fsMIStdRip2IfConfSrcAddress,'fsMIStdRip2PeerTable':fsMIStdRip2PeerTable,'fsMIStdRip2PeerEntry':fsMIStdRip2PeerEntry,_M:fsMIStdRip2PeerAddress,_N:fsMIStdRip2PeerDomain,'fsMIStdRip2PeerLastUpdate':fsMIStdRip2PeerLastUpdate,'fsMIStdRip2PeerVersion':fsMIStdRip2PeerVersion,'fsMIStdRip2PeerRcvBadPackets':fsMIStdRip2PeerRcvBadPackets,'fsMIStdRip2PeerRcvBadRoutes':fsMIStdRip2PeerRcvBadRoutes,'fsMIStdRip2PeerInUseKey':fsMIStdRip2PeerInUseKey})