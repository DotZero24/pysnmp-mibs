_K='rip2PeerDomain'
_J='rip2PeerAddress'
_I='rip2IfConfAddress'
_H='invalid'
_G='rip2IfStatAddress'
_F='OctetString'
_E='RFC1389-MIB'
_D='Integer32'
_C='read-write'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
class RouteTag(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_Mgmt_ObjectIdentity=ObjectIdentity
mgmt=_Mgmt_ObjectIdentity((1,3,6,1,2))
_Mib_2_ObjectIdentity=ObjectIdentity
mib_2=_Mib_2_ObjectIdentity((1,3,6,1,2,1))
_Rip2_ObjectIdentity=ObjectIdentity
rip2=_Rip2_ObjectIdentity((1,3,6,1,2,1,23))
_Rip2GlobalGroup_ObjectIdentity=ObjectIdentity
rip2GlobalGroup=_Rip2GlobalGroup_ObjectIdentity((1,3,6,1,2,1,23,1))
_Rip2GlobalRouteChanges_Type=Counter32
_Rip2GlobalRouteChanges_Object=MibScalar
rip2GlobalRouteChanges=_Rip2GlobalRouteChanges_Object((1,3,6,1,2,1,23,1,1),_Rip2GlobalRouteChanges_Type())
rip2GlobalRouteChanges.setMaxAccess(_B)
if mibBuilder.loadTexts:rip2GlobalRouteChanges.setStatus(_A)
_Rip2GlobalQueries_Type=Counter32
_Rip2GlobalQueries_Object=MibScalar
rip2GlobalQueries=_Rip2GlobalQueries_Object((1,3,6,1,2,1,23,1,2),_Rip2GlobalQueries_Type())
rip2GlobalQueries.setMaxAccess(_B)
if mibBuilder.loadTexts:rip2GlobalQueries.setStatus(_A)
_Rip2IfStatTable_Object=MibTable
rip2IfStatTable=_Rip2IfStatTable_Object((1,3,6,1,2,1,23,2))
if mibBuilder.loadTexts:rip2IfStatTable.setStatus(_A)
_Rip2IfStatEntry_Object=MibTableRow
rip2IfStatEntry=_Rip2IfStatEntry_Object((1,3,6,1,2,1,23,2,1))
rip2IfStatEntry.setIndexNames((0,_E,_G))
if mibBuilder.loadTexts:rip2IfStatEntry.setStatus(_A)
_Rip2IfStatAddress_Type=IpAddress
_Rip2IfStatAddress_Object=MibTableColumn
rip2IfStatAddress=_Rip2IfStatAddress_Object((1,3,6,1,2,1,23,2,1,1),_Rip2IfStatAddress_Type())
rip2IfStatAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:rip2IfStatAddress.setStatus(_A)
_Rip2IfStatRcvBadPackets_Type=Counter32
_Rip2IfStatRcvBadPackets_Object=MibTableColumn
rip2IfStatRcvBadPackets=_Rip2IfStatRcvBadPackets_Object((1,3,6,1,2,1,23,2,1,2),_Rip2IfStatRcvBadPackets_Type())
rip2IfStatRcvBadPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rip2IfStatRcvBadPackets.setStatus(_A)
_Rip2IfStatRcvBadRoutes_Type=Counter32
_Rip2IfStatRcvBadRoutes_Object=MibTableColumn
rip2IfStatRcvBadRoutes=_Rip2IfStatRcvBadRoutes_Object((1,3,6,1,2,1,23,2,1,3),_Rip2IfStatRcvBadRoutes_Type())
rip2IfStatRcvBadRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:rip2IfStatRcvBadRoutes.setStatus(_A)
_Rip2IfStatSentUpdates_Type=Counter32
_Rip2IfStatSentUpdates_Object=MibTableColumn
rip2IfStatSentUpdates=_Rip2IfStatSentUpdates_Object((1,3,6,1,2,1,23,2,1,4),_Rip2IfStatSentUpdates_Type())
rip2IfStatSentUpdates.setMaxAccess(_B)
if mibBuilder.loadTexts:rip2IfStatSentUpdates.setStatus(_A)
class _Rip2IfStatStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('valid',1),(_H,2)))
_Rip2IfStatStatus_Type.__name__=_D
_Rip2IfStatStatus_Object=MibTableColumn
rip2IfStatStatus=_Rip2IfStatStatus_Object((1,3,6,1,2,1,23,2,1,5),_Rip2IfStatStatus_Type())
rip2IfStatStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:rip2IfStatStatus.setStatus(_A)
_Rip2IfConfTable_Object=MibTable
rip2IfConfTable=_Rip2IfConfTable_Object((1,3,6,1,2,1,23,3))
if mibBuilder.loadTexts:rip2IfConfTable.setStatus(_A)
_Rip2IfConfEntry_Object=MibTableRow
rip2IfConfEntry=_Rip2IfConfEntry_Object((1,3,6,1,2,1,23,3,1))
rip2IfConfEntry.setIndexNames((0,_E,_I))
if mibBuilder.loadTexts:rip2IfConfEntry.setStatus(_A)
_Rip2IfConfAddress_Type=IpAddress
_Rip2IfConfAddress_Object=MibTableColumn
rip2IfConfAddress=_Rip2IfConfAddress_Object((1,3,6,1,2,1,23,3,1,1),_Rip2IfConfAddress_Type())
rip2IfConfAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:rip2IfConfAddress.setStatus(_A)
_Rip2IfConfDomain_Type=RouteTag
_Rip2IfConfDomain_Object=MibTableColumn
rip2IfConfDomain=_Rip2IfConfDomain_Object((1,3,6,1,2,1,23,3,1,2),_Rip2IfConfDomain_Type())
rip2IfConfDomain.setMaxAccess(_C)
if mibBuilder.loadTexts:rip2IfConfDomain.setStatus('deprecated')
class _Rip2IfConfAuthType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('noAuthentication',1),('simplePassword',2),('md5',3)))
_Rip2IfConfAuthType_Type.__name__=_D
_Rip2IfConfAuthType_Object=MibTableColumn
rip2IfConfAuthType=_Rip2IfConfAuthType_Object((1,3,6,1,2,1,23,3,1,3),_Rip2IfConfAuthType_Type())
rip2IfConfAuthType.setMaxAccess(_C)
if mibBuilder.loadTexts:rip2IfConfAuthType.setStatus(_A)
class _Rip2IfConfAuthKey_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_Rip2IfConfAuthKey_Type.__name__=_F
_Rip2IfConfAuthKey_Object=MibTableColumn
rip2IfConfAuthKey=_Rip2IfConfAuthKey_Object((1,3,6,1,2,1,23,3,1,4),_Rip2IfConfAuthKey_Type())
rip2IfConfAuthKey.setMaxAccess(_C)
if mibBuilder.loadTexts:rip2IfConfAuthKey.setStatus(_A)
class _Rip2IfConfSend_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('doNotSend',1),('ripVersion1',2),('rip1Compatible',3),('ripVersion2',4),('ripV1Demand',5),('ripV2Demand',6)))
_Rip2IfConfSend_Type.__name__=_D
_Rip2IfConfSend_Object=MibTableColumn
rip2IfConfSend=_Rip2IfConfSend_Object((1,3,6,1,2,1,23,3,1,5),_Rip2IfConfSend_Type())
rip2IfConfSend.setMaxAccess(_C)
if mibBuilder.loadTexts:rip2IfConfSend.setStatus(_A)
class _Rip2IfConfReceive_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('rip1',1),('rip2',2),('rip1OrRip2',3),('doNotRecieve',4)))
_Rip2IfConfReceive_Type.__name__=_D
_Rip2IfConfReceive_Object=MibTableColumn
rip2IfConfReceive=_Rip2IfConfReceive_Object((1,3,6,1,2,1,23,3,1,6),_Rip2IfConfReceive_Type())
rip2IfConfReceive.setMaxAccess(_C)
if mibBuilder.loadTexts:rip2IfConfReceive.setStatus(_A)
class _Rip2IfConfDefaultMetric_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_Rip2IfConfDefaultMetric_Type.__name__=_D
_Rip2IfConfDefaultMetric_Object=MibTableColumn
rip2IfConfDefaultMetric=_Rip2IfConfDefaultMetric_Object((1,3,6,1,2,1,23,3,1,7),_Rip2IfConfDefaultMetric_Type())
rip2IfConfDefaultMetric.setMaxAccess(_C)
if mibBuilder.loadTexts:rip2IfConfDefaultMetric.setStatus(_A)
class _Rip2IfConfStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('valid',1),(_H,2)))
_Rip2IfConfStatus_Type.__name__=_D
_Rip2IfConfStatus_Object=MibTableColumn
rip2IfConfStatus=_Rip2IfConfStatus_Object((1,3,6,1,2,1,23,3,1,8),_Rip2IfConfStatus_Type())
rip2IfConfStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:rip2IfConfStatus.setStatus(_A)
_Rip2IfConfSrcAddress_Type=IpAddress
_Rip2IfConfSrcAddress_Object=MibTableColumn
rip2IfConfSrcAddress=_Rip2IfConfSrcAddress_Object((1,3,6,1,2,1,23,3,1,9),_Rip2IfConfSrcAddress_Type())
rip2IfConfSrcAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:rip2IfConfSrcAddress.setStatus(_A)
_Rip2PeerTable_Object=MibTable
rip2PeerTable=_Rip2PeerTable_Object((1,3,6,1,2,1,23,4))
if mibBuilder.loadTexts:rip2PeerTable.setStatus(_A)
_Rip2PeerEntry_Object=MibTableRow
rip2PeerEntry=_Rip2PeerEntry_Object((1,3,6,1,2,1,23,4,1))
rip2PeerEntry.setIndexNames((0,_E,_J),(0,_E,_K))
if mibBuilder.loadTexts:rip2PeerEntry.setStatus(_A)
_Rip2PeerAddress_Type=IpAddress
_Rip2PeerAddress_Object=MibTableColumn
rip2PeerAddress=_Rip2PeerAddress_Object((1,3,6,1,2,1,23,4,1,1),_Rip2PeerAddress_Type())
rip2PeerAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:rip2PeerAddress.setStatus(_A)
_Rip2PeerDomain_Type=RouteTag
_Rip2PeerDomain_Object=MibTableColumn
rip2PeerDomain=_Rip2PeerDomain_Object((1,3,6,1,2,1,23,4,1,2),_Rip2PeerDomain_Type())
rip2PeerDomain.setMaxAccess(_B)
if mibBuilder.loadTexts:rip2PeerDomain.setStatus(_A)
_Rip2PeerLastUpdate_Type=TimeTicks
_Rip2PeerLastUpdate_Object=MibTableColumn
rip2PeerLastUpdate=_Rip2PeerLastUpdate_Object((1,3,6,1,2,1,23,4,1,3),_Rip2PeerLastUpdate_Type())
rip2PeerLastUpdate.setMaxAccess(_B)
if mibBuilder.loadTexts:rip2PeerLastUpdate.setStatus(_A)
class _Rip2PeerVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_Rip2PeerVersion_Type.__name__=_D
_Rip2PeerVersion_Object=MibTableColumn
rip2PeerVersion=_Rip2PeerVersion_Object((1,3,6,1,2,1,23,4,1,4),_Rip2PeerVersion_Type())
rip2PeerVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:rip2PeerVersion.setStatus(_A)
_Rip2PeerRcvBadPackets_Type=Counter32
_Rip2PeerRcvBadPackets_Object=MibTableColumn
rip2PeerRcvBadPackets=_Rip2PeerRcvBadPackets_Object((1,3,6,1,2,1,23,4,1,5),_Rip2PeerRcvBadPackets_Type())
rip2PeerRcvBadPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rip2PeerRcvBadPackets.setStatus(_A)
_Rip2PeerRcvBadRoutes_Type=Counter32
_Rip2PeerRcvBadRoutes_Object=MibTableColumn
rip2PeerRcvBadRoutes=_Rip2PeerRcvBadRoutes_Object((1,3,6,1,2,1,23,4,1,6),_Rip2PeerRcvBadRoutes_Type())
rip2PeerRcvBadRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:rip2PeerRcvBadRoutes.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'RouteTag':RouteTag,'mgmt':mgmt,'mib-2':mib_2,'rip2':rip2,'rip2GlobalGroup':rip2GlobalGroup,'rip2GlobalRouteChanges':rip2GlobalRouteChanges,'rip2GlobalQueries':rip2GlobalQueries,'rip2IfStatTable':rip2IfStatTable,'rip2IfStatEntry':rip2IfStatEntry,_G:rip2IfStatAddress,'rip2IfStatRcvBadPackets':rip2IfStatRcvBadPackets,'rip2IfStatRcvBadRoutes':rip2IfStatRcvBadRoutes,'rip2IfStatSentUpdates':rip2IfStatSentUpdates,'rip2IfStatStatus':rip2IfStatStatus,'rip2IfConfTable':rip2IfConfTable,'rip2IfConfEntry':rip2IfConfEntry,_I:rip2IfConfAddress,'rip2IfConfDomain':rip2IfConfDomain,'rip2IfConfAuthType':rip2IfConfAuthType,'rip2IfConfAuthKey':rip2IfConfAuthKey,'rip2IfConfSend':rip2IfConfSend,'rip2IfConfReceive':rip2IfConfReceive,'rip2IfConfDefaultMetric':rip2IfConfDefaultMetric,'rip2IfConfStatus':rip2IfConfStatus,'rip2IfConfSrcAddress':rip2IfConfSrcAddress,'rip2PeerTable':rip2PeerTable,'rip2PeerEntry':rip2PeerEntry,_J:rip2PeerAddress,_K:rip2PeerDomain,'rip2PeerLastUpdate':rip2PeerLastUpdate,'rip2PeerVersion':rip2PeerVersion,'rip2PeerRcvBadPackets':rip2PeerRcvBadPackets,'rip2PeerRcvBadRoutes':rip2PeerRcvBadRoutes})