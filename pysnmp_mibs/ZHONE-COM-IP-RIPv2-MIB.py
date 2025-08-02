_N='zhRip2PeerAddress'
_M='zhRip2IfConfAddress'
_L='zhRip2IfStatAddress'
_K='enabled'
_J='disabled'
_I='Unsigned32'
_H='not-accessible'
_G='ZHONE-COM-IP-RIPv2-MIB'
_F='rdIndex'
_E='ZHONE-COM-IP-RD-MIB'
_D='read-only'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_I,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
rdIndex,=mibBuilder.importSymbols(_E,_F)
zhoneIp,zhoneModules=mibBuilder.importSymbols('Zhone','zhoneIp','zhoneModules')
comIpRip2=ModuleIdentity((1,3,6,1,4,1,5504,6,52))
if mibBuilder.loadTexts:comIpRip2.setRevisions(('2001-09-12 13:18','2000-10-12 17:08','2000-10-02 08:05','2000-09-12 10:20'))
class RipAuthKey(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_Rip2_ObjectIdentity=ObjectIdentity
rip2=_Rip2_ObjectIdentity((1,3,6,1,4,1,5504,4,1,2))
if mibBuilder.loadTexts:rip2.setStatus(_A)
_ZhRip2GlobalTable_Object=MibTable
zhRip2GlobalTable=_ZhRip2GlobalTable_Object((1,3,6,1,4,1,5504,4,1,2,1))
if mibBuilder.loadTexts:zhRip2GlobalTable.setStatus(_A)
_ZhRip2GlobalEntry_Object=MibTableRow
zhRip2GlobalEntry=_ZhRip2GlobalEntry_Object((1,3,6,1,4,1,5504,4,1,2,1,1))
zhRip2GlobalEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:zhRip2GlobalEntry.setStatus(_A)
_ZhRip2GlobalRouteChanges_Type=Counter32
_ZhRip2GlobalRouteChanges_Object=MibTableColumn
zhRip2GlobalRouteChanges=_ZhRip2GlobalRouteChanges_Object((1,3,6,1,4,1,5504,4,1,2,1,1,1),_ZhRip2GlobalRouteChanges_Type())
zhRip2GlobalRouteChanges.setMaxAccess(_D)
if mibBuilder.loadTexts:zhRip2GlobalRouteChanges.setStatus(_A)
_ZhRip2GlobalQueries_Type=Counter32
_ZhRip2GlobalQueries_Object=MibTableColumn
zhRip2GlobalQueries=_ZhRip2GlobalQueries_Object((1,3,6,1,4,1,5504,4,1,2,1,1,2),_ZhRip2GlobalQueries_Type())
zhRip2GlobalQueries.setMaxAccess(_D)
if mibBuilder.loadTexts:zhRip2GlobalQueries.setStatus(_A)
class _ZhRip2GlobalAdminState_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_ZhRip2GlobalAdminState_Type.__name__=_C
_ZhRip2GlobalAdminState_Object=MibTableColumn
zhRip2GlobalAdminState=_ZhRip2GlobalAdminState_Object((1,3,6,1,4,1,5504,4,1,2,1,1,3),_ZhRip2GlobalAdminState_Type())
zhRip2GlobalAdminState.setMaxAccess(_B)
if mibBuilder.loadTexts:zhRip2GlobalAdminState.setStatus(_A)
class _ZhRip2GlobalUpdateTime_Type(Unsigned32):defaultValue=30
_ZhRip2GlobalUpdateTime_Type.__name__=_I
_ZhRip2GlobalUpdateTime_Object=MibTableColumn
zhRip2GlobalUpdateTime=_ZhRip2GlobalUpdateTime_Object((1,3,6,1,4,1,5504,4,1,2,1,1,4),_ZhRip2GlobalUpdateTime_Type())
zhRip2GlobalUpdateTime.setMaxAccess(_B)
if mibBuilder.loadTexts:zhRip2GlobalUpdateTime.setStatus(_A)
_ZhRip2IfStatTable_Object=MibTable
zhRip2IfStatTable=_ZhRip2IfStatTable_Object((1,3,6,1,4,1,5504,4,1,2,2))
if mibBuilder.loadTexts:zhRip2IfStatTable.setStatus(_A)
_ZhRip2IfStatEntry_Object=MibTableRow
zhRip2IfStatEntry=_ZhRip2IfStatEntry_Object((1,3,6,1,4,1,5504,4,1,2,2,1))
zhRip2IfStatEntry.setIndexNames((0,_E,_F),(0,_G,_L))
if mibBuilder.loadTexts:zhRip2IfStatEntry.setStatus(_A)
_ZhRip2IfStatAddress_Type=IpAddress
_ZhRip2IfStatAddress_Object=MibTableColumn
zhRip2IfStatAddress=_ZhRip2IfStatAddress_Object((1,3,6,1,4,1,5504,4,1,2,2,1,1),_ZhRip2IfStatAddress_Type())
zhRip2IfStatAddress.setMaxAccess(_H)
if mibBuilder.loadTexts:zhRip2IfStatAddress.setStatus(_A)
_ZhRip2IfStatRcvBadPackets_Type=Counter32
_ZhRip2IfStatRcvBadPackets_Object=MibTableColumn
zhRip2IfStatRcvBadPackets=_ZhRip2IfStatRcvBadPackets_Object((1,3,6,1,4,1,5504,4,1,2,2,1,2),_ZhRip2IfStatRcvBadPackets_Type())
zhRip2IfStatRcvBadPackets.setMaxAccess(_D)
if mibBuilder.loadTexts:zhRip2IfStatRcvBadPackets.setStatus(_A)
_ZhRip2IfStatRcvBadRoutes_Type=Counter32
_ZhRip2IfStatRcvBadRoutes_Object=MibTableColumn
zhRip2IfStatRcvBadRoutes=_ZhRip2IfStatRcvBadRoutes_Object((1,3,6,1,4,1,5504,4,1,2,2,1,3),_ZhRip2IfStatRcvBadRoutes_Type())
zhRip2IfStatRcvBadRoutes.setMaxAccess(_D)
if mibBuilder.loadTexts:zhRip2IfStatRcvBadRoutes.setStatus(_A)
_ZhRip2IfStatSentUpdates_Type=Counter32
_ZhRip2IfStatSentUpdates_Object=MibTableColumn
zhRip2IfStatSentUpdates=_ZhRip2IfStatSentUpdates_Object((1,3,6,1,4,1,5504,4,1,2,2,1,4),_ZhRip2IfStatSentUpdates_Type())
zhRip2IfStatSentUpdates.setMaxAccess(_D)
if mibBuilder.loadTexts:zhRip2IfStatSentUpdates.setStatus(_A)
_ZhRip2IfConfTable_Object=MibTable
zhRip2IfConfTable=_ZhRip2IfConfTable_Object((1,3,6,1,4,1,5504,4,1,2,3))
if mibBuilder.loadTexts:zhRip2IfConfTable.setStatus(_A)
_ZhRip2IfConfEntry_Object=MibTableRow
zhRip2IfConfEntry=_ZhRip2IfConfEntry_Object((1,3,6,1,4,1,5504,4,1,2,3,1))
zhRip2IfConfEntry.setIndexNames((0,_E,_F),(0,_G,_M))
if mibBuilder.loadTexts:zhRip2IfConfEntry.setStatus(_A)
_ZhRip2IfConfAddress_Type=IpAddress
_ZhRip2IfConfAddress_Object=MibTableColumn
zhRip2IfConfAddress=_ZhRip2IfConfAddress_Object((1,3,6,1,4,1,5504,4,1,2,3,1,1),_ZhRip2IfConfAddress_Type())
zhRip2IfConfAddress.setMaxAccess(_H)
if mibBuilder.loadTexts:zhRip2IfConfAddress.setStatus(_A)
class _ZhRip2IfConfAuthType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('noAuthentication',1),('simplePassword',2),('md5',3)))
_ZhRip2IfConfAuthType_Type.__name__=_C
_ZhRip2IfConfAuthType_Object=MibTableColumn
zhRip2IfConfAuthType=_ZhRip2IfConfAuthType_Object((1,3,6,1,4,1,5504,4,1,2,3,1,2),_ZhRip2IfConfAuthType_Type())
zhRip2IfConfAuthType.setMaxAccess(_B)
if mibBuilder.loadTexts:zhRip2IfConfAuthType.setStatus(_A)
_ZhRip2IfConfAuthKey_Type=RipAuthKey
_ZhRip2IfConfAuthKey_Object=MibTableColumn
zhRip2IfConfAuthKey=_ZhRip2IfConfAuthKey_Object((1,3,6,1,4,1,5504,4,1,2,3,1,3),_ZhRip2IfConfAuthKey_Type())
zhRip2IfConfAuthKey.setMaxAccess(_B)
if mibBuilder.loadTexts:zhRip2IfConfAuthKey.setStatus(_A)
class _ZhRip2IfConfSend_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('doNotSend',1),('ripVersion1',2),('rip1Compatible',3),('ripVersion2',4),('ripV1Demand',5),('ripV2Demand',6)))
_ZhRip2IfConfSend_Type.__name__=_C
_ZhRip2IfConfSend_Object=MibTableColumn
zhRip2IfConfSend=_ZhRip2IfConfSend_Object((1,3,6,1,4,1,5504,4,1,2,3,1,4),_ZhRip2IfConfSend_Type())
zhRip2IfConfSend.setMaxAccess(_B)
if mibBuilder.loadTexts:zhRip2IfConfSend.setStatus(_A)
class _ZhRip2IfConfReceive_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('rip1',1),('rip2',2),('rip1OrRip2',3),('doNotReceive',4)))
_ZhRip2IfConfReceive_Type.__name__=_C
_ZhRip2IfConfReceive_Object=MibTableColumn
zhRip2IfConfReceive=_ZhRip2IfConfReceive_Object((1,3,6,1,4,1,5504,4,1,2,3,1,5),_ZhRip2IfConfReceive_Type())
zhRip2IfConfReceive.setMaxAccess(_B)
if mibBuilder.loadTexts:zhRip2IfConfReceive.setStatus(_A)
class _ZhRip2IfConfDefaultMetric_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_ZhRip2IfConfDefaultMetric_Type.__name__=_C
_ZhRip2IfConfDefaultMetric_Object=MibTableColumn
zhRip2IfConfDefaultMetric=_ZhRip2IfConfDefaultMetric_Object((1,3,6,1,4,1,5504,4,1,2,3,1,6),_ZhRip2IfConfDefaultMetric_Type())
zhRip2IfConfDefaultMetric.setMaxAccess(_B)
if mibBuilder.loadTexts:zhRip2IfConfDefaultMetric.setStatus(_A)
_ZhRip2IfConfSrcAddress_Type=IpAddress
_ZhRip2IfConfSrcAddress_Object=MibTableColumn
zhRip2IfConfSrcAddress=_ZhRip2IfConfSrcAddress_Object((1,3,6,1,4,1,5504,4,1,2,3,1,7),_ZhRip2IfConfSrcAddress_Type())
zhRip2IfConfSrcAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:zhRip2IfConfSrcAddress.setStatus(_A)
class _ZhRip2IfConfStaticRouteAdvertisement_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('none',1),('low',2),('high',3),('both',4)))
_ZhRip2IfConfStaticRouteAdvertisement_Type.__name__=_C
_ZhRip2IfConfStaticRouteAdvertisement_Object=MibTableColumn
zhRip2IfConfStaticRouteAdvertisement=_ZhRip2IfConfStaticRouteAdvertisement_Object((1,3,6,1,4,1,5504,4,1,2,3,1,8),_ZhRip2IfConfStaticRouteAdvertisement_Type())
zhRip2IfConfStaticRouteAdvertisement.setMaxAccess(_B)
if mibBuilder.loadTexts:zhRip2IfConfStaticRouteAdvertisement.setStatus(_A)
class _ZhRip2IfConfPoison_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_ZhRip2IfConfPoison_Type.__name__=_C
_ZhRip2IfConfPoison_Object=MibTableColumn
zhRip2IfConfPoison=_ZhRip2IfConfPoison_Object((1,3,6,1,4,1,5504,4,1,2,3,1,9),_ZhRip2IfConfPoison_Type())
zhRip2IfConfPoison.setMaxAccess(_B)
if mibBuilder.loadTexts:zhRip2IfConfPoison.setStatus(_A)
_ZhRip2PeerTable_Object=MibTable
zhRip2PeerTable=_ZhRip2PeerTable_Object((1,3,6,1,4,1,5504,4,1,2,4))
if mibBuilder.loadTexts:zhRip2PeerTable.setStatus(_A)
_ZhRip2PeerEntry_Object=MibTableRow
zhRip2PeerEntry=_ZhRip2PeerEntry_Object((1,3,6,1,4,1,5504,4,1,2,4,1))
zhRip2PeerEntry.setIndexNames((0,_E,_F),(0,_G,_N))
if mibBuilder.loadTexts:zhRip2PeerEntry.setStatus(_A)
_ZhRip2PeerAddress_Type=IpAddress
_ZhRip2PeerAddress_Object=MibTableColumn
zhRip2PeerAddress=_ZhRip2PeerAddress_Object((1,3,6,1,4,1,5504,4,1,2,4,1,1),_ZhRip2PeerAddress_Type())
zhRip2PeerAddress.setMaxAccess(_H)
if mibBuilder.loadTexts:zhRip2PeerAddress.setStatus(_A)
_ZhRip2PeerLastUpdate_Type=TimeTicks
_ZhRip2PeerLastUpdate_Object=MibTableColumn
zhRip2PeerLastUpdate=_ZhRip2PeerLastUpdate_Object((1,3,6,1,4,1,5504,4,1,2,4,1,2),_ZhRip2PeerLastUpdate_Type())
zhRip2PeerLastUpdate.setMaxAccess(_D)
if mibBuilder.loadTexts:zhRip2PeerLastUpdate.setStatus(_A)
class _ZhRip2PeerVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_ZhRip2PeerVersion_Type.__name__=_C
_ZhRip2PeerVersion_Object=MibTableColumn
zhRip2PeerVersion=_ZhRip2PeerVersion_Object((1,3,6,1,4,1,5504,4,1,2,4,1,3),_ZhRip2PeerVersion_Type())
zhRip2PeerVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:zhRip2PeerVersion.setStatus(_A)
_ZhRip2PeerRcvBadPackets_Type=Counter32
_ZhRip2PeerRcvBadPackets_Object=MibTableColumn
zhRip2PeerRcvBadPackets=_ZhRip2PeerRcvBadPackets_Object((1,3,6,1,4,1,5504,4,1,2,4,1,4),_ZhRip2PeerRcvBadPackets_Type())
zhRip2PeerRcvBadPackets.setMaxAccess(_D)
if mibBuilder.loadTexts:zhRip2PeerRcvBadPackets.setStatus(_A)
_ZhRip2PeerRcvBadRoutes_Type=Counter32
_ZhRip2PeerRcvBadRoutes_Object=MibTableColumn
zhRip2PeerRcvBadRoutes=_ZhRip2PeerRcvBadRoutes_Object((1,3,6,1,4,1,5504,4,1,2,4,1,5),_ZhRip2PeerRcvBadRoutes_Type())
zhRip2PeerRcvBadRoutes.setMaxAccess(_D)
if mibBuilder.loadTexts:zhRip2PeerRcvBadRoutes.setStatus(_A)
mibBuilder.exportSymbols(_G,**{'RipAuthKey':RipAuthKey,'rip2':rip2,'zhRip2GlobalTable':zhRip2GlobalTable,'zhRip2GlobalEntry':zhRip2GlobalEntry,'zhRip2GlobalRouteChanges':zhRip2GlobalRouteChanges,'zhRip2GlobalQueries':zhRip2GlobalQueries,'zhRip2GlobalAdminState':zhRip2GlobalAdminState,'zhRip2GlobalUpdateTime':zhRip2GlobalUpdateTime,'zhRip2IfStatTable':zhRip2IfStatTable,'zhRip2IfStatEntry':zhRip2IfStatEntry,_L:zhRip2IfStatAddress,'zhRip2IfStatRcvBadPackets':zhRip2IfStatRcvBadPackets,'zhRip2IfStatRcvBadRoutes':zhRip2IfStatRcvBadRoutes,'zhRip2IfStatSentUpdates':zhRip2IfStatSentUpdates,'zhRip2IfConfTable':zhRip2IfConfTable,'zhRip2IfConfEntry':zhRip2IfConfEntry,_M:zhRip2IfConfAddress,'zhRip2IfConfAuthType':zhRip2IfConfAuthType,'zhRip2IfConfAuthKey':zhRip2IfConfAuthKey,'zhRip2IfConfSend':zhRip2IfConfSend,'zhRip2IfConfReceive':zhRip2IfConfReceive,'zhRip2IfConfDefaultMetric':zhRip2IfConfDefaultMetric,'zhRip2IfConfSrcAddress':zhRip2IfConfSrcAddress,'zhRip2IfConfStaticRouteAdvertisement':zhRip2IfConfStaticRouteAdvertisement,'zhRip2IfConfPoison':zhRip2IfConfPoison,'zhRip2PeerTable':zhRip2PeerTable,'zhRip2PeerEntry':zhRip2PeerEntry,_N:zhRip2PeerAddress,'zhRip2PeerLastUpdate':zhRip2PeerLastUpdate,'zhRip2PeerVersion':zhRip2PeerVersion,'zhRip2PeerRcvBadPackets':zhRip2PeerRcvBadPackets,'zhRip2PeerRcvBadRoutes':zhRip2PeerRcvBadRoutes,'comIpRip2':comIpRip2})