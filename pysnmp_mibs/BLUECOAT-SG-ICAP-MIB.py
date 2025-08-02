_U='bluecoatSgICAPMIBGroup'
_T='sgICAPTrap'
_S='icapServiceStatsSuccessfullReqs'
_R='icapServiceStatsFailedReqs'
_Q='icapServiceStatsSentBytes'
_P='icapServiceStatsRcvdBytes'
_O='icapServiceStatsSecureActvReqs'
_N='icapServiceStatsPlainActvReqs'
_M='icapServiceStatsSecuredConns'
_L='icapServiceStatsPlainConns'
_K='icapServiceStatsEntityType'
_J='icapServiceStatsIndex'
_I='Unsigned32'
_H='OctetString'
_G='sgICAPNotification'
_F='icapServiceStatsDeferredReqs'
_E='icapServiceStatsQueuedReqs'
_D='icapServiceStatsName'
_C='read-only'
_B='BLUECOAT-SG-ICAP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_H,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
blueCoatMgmt,=mibBuilder.importSymbols('BLUECOAT-MIB','blueCoatMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_I,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
bluecoatSGICAPMIB=ModuleIdentity((1,3,6,1,4,1,3417,2,14))
if mibBuilder.loadTexts:bluecoatSGICAPMIB.setRevisions(('2013-02-08 14:00',))
class ICAPServiceEntityType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('service',1),('servivceGroup',2)))
class ICAPServiceNotificationType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('queuedRequestsAboveThreshold',1),('queuedRequestsBelowThreshold',2),('deferredRequestsAboveThreshold',3),('deferredRequestsBelowThreshold',4)))
_BluecoatSgICAPMIBObjects_ObjectIdentity=ObjectIdentity
bluecoatSgICAPMIBObjects=_BluecoatSgICAPMIBObjects_ObjectIdentity((1,3,6,1,4,1,3417,2,14,1))
_BluecoatSgICAPValues_ObjectIdentity=ObjectIdentity
bluecoatSgICAPValues=_BluecoatSgICAPValues_ObjectIdentity((1,3,6,1,4,1,3417,2,14,1,1))
_IcapService_ObjectIdentity=ObjectIdentity
icapService=_IcapService_ObjectIdentity((1,3,6,1,4,1,3417,2,14,1,1,1))
_IcapServiceStatsTable_Object=MibTable
icapServiceStatsTable=_IcapServiceStatsTable_Object((1,3,6,1,4,1,3417,2,14,1,1,1,1))
if mibBuilder.loadTexts:icapServiceStatsTable.setStatus(_A)
_IcapServiceStatsTableEntry_Object=MibTableRow
icapServiceStatsTableEntry=_IcapServiceStatsTableEntry_Object((1,3,6,1,4,1,3417,2,14,1,1,1,1,1))
icapServiceStatsTableEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:icapServiceStatsTableEntry.setStatus(_A)
class _IcapServiceStatsIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_IcapServiceStatsIndex_Type.__name__=_I
_IcapServiceStatsIndex_Object=MibTableColumn
icapServiceStatsIndex=_IcapServiceStatsIndex_Object((1,3,6,1,4,1,3417,2,14,1,1,1,1,1,1),_IcapServiceStatsIndex_Type())
icapServiceStatsIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:icapServiceStatsIndex.setStatus(_A)
class _IcapServiceStatsName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_IcapServiceStatsName_Type.__name__=_H
_IcapServiceStatsName_Object=MibTableColumn
icapServiceStatsName=_IcapServiceStatsName_Object((1,3,6,1,4,1,3417,2,14,1,1,1,1,1,2),_IcapServiceStatsName_Type())
icapServiceStatsName.setMaxAccess(_C)
if mibBuilder.loadTexts:icapServiceStatsName.setStatus(_A)
_IcapServiceStatsEntityType_Type=ICAPServiceEntityType
_IcapServiceStatsEntityType_Object=MibTableColumn
icapServiceStatsEntityType=_IcapServiceStatsEntityType_Object((1,3,6,1,4,1,3417,2,14,1,1,1,1,1,3),_IcapServiceStatsEntityType_Type())
icapServiceStatsEntityType.setMaxAccess(_C)
if mibBuilder.loadTexts:icapServiceStatsEntityType.setStatus(_A)
_IcapServiceStatsPlainConns_Type=Gauge32
_IcapServiceStatsPlainConns_Object=MibTableColumn
icapServiceStatsPlainConns=_IcapServiceStatsPlainConns_Object((1,3,6,1,4,1,3417,2,14,1,1,1,1,1,4),_IcapServiceStatsPlainConns_Type())
icapServiceStatsPlainConns.setMaxAccess(_C)
if mibBuilder.loadTexts:icapServiceStatsPlainConns.setStatus(_A)
_IcapServiceStatsSecuredConns_Type=Gauge32
_IcapServiceStatsSecuredConns_Object=MibTableColumn
icapServiceStatsSecuredConns=_IcapServiceStatsSecuredConns_Object((1,3,6,1,4,1,3417,2,14,1,1,1,1,1,5),_IcapServiceStatsSecuredConns_Type())
icapServiceStatsSecuredConns.setMaxAccess(_C)
if mibBuilder.loadTexts:icapServiceStatsSecuredConns.setStatus(_A)
_IcapServiceStatsPlainActvReqs_Type=Gauge32
_IcapServiceStatsPlainActvReqs_Object=MibTableColumn
icapServiceStatsPlainActvReqs=_IcapServiceStatsPlainActvReqs_Object((1,3,6,1,4,1,3417,2,14,1,1,1,1,1,6),_IcapServiceStatsPlainActvReqs_Type())
icapServiceStatsPlainActvReqs.setMaxAccess(_C)
if mibBuilder.loadTexts:icapServiceStatsPlainActvReqs.setStatus(_A)
_IcapServiceStatsSecureActvReqs_Type=Gauge32
_IcapServiceStatsSecureActvReqs_Object=MibTableColumn
icapServiceStatsSecureActvReqs=_IcapServiceStatsSecureActvReqs_Object((1,3,6,1,4,1,3417,2,14,1,1,1,1,1,7),_IcapServiceStatsSecureActvReqs_Type())
icapServiceStatsSecureActvReqs.setMaxAccess(_C)
if mibBuilder.loadTexts:icapServiceStatsSecureActvReqs.setStatus(_A)
_IcapServiceStatsQueuedReqs_Type=Gauge32
_IcapServiceStatsQueuedReqs_Object=MibTableColumn
icapServiceStatsQueuedReqs=_IcapServiceStatsQueuedReqs_Object((1,3,6,1,4,1,3417,2,14,1,1,1,1,1,8),_IcapServiceStatsQueuedReqs_Type())
icapServiceStatsQueuedReqs.setMaxAccess(_C)
if mibBuilder.loadTexts:icapServiceStatsQueuedReqs.setStatus(_A)
_IcapServiceStatsDeferredReqs_Type=Gauge32
_IcapServiceStatsDeferredReqs_Object=MibTableColumn
icapServiceStatsDeferredReqs=_IcapServiceStatsDeferredReqs_Object((1,3,6,1,4,1,3417,2,14,1,1,1,1,1,9),_IcapServiceStatsDeferredReqs_Type())
icapServiceStatsDeferredReqs.setMaxAccess(_C)
if mibBuilder.loadTexts:icapServiceStatsDeferredReqs.setStatus(_A)
_IcapServiceStatsRcvdBytes_Type=Counter64
_IcapServiceStatsRcvdBytes_Object=MibTableColumn
icapServiceStatsRcvdBytes=_IcapServiceStatsRcvdBytes_Object((1,3,6,1,4,1,3417,2,14,1,1,1,1,1,10),_IcapServiceStatsRcvdBytes_Type())
icapServiceStatsRcvdBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:icapServiceStatsRcvdBytes.setStatus(_A)
_IcapServiceStatsSentBytes_Type=Counter64
_IcapServiceStatsSentBytes_Object=MibTableColumn
icapServiceStatsSentBytes=_IcapServiceStatsSentBytes_Object((1,3,6,1,4,1,3417,2,14,1,1,1,1,1,11),_IcapServiceStatsSentBytes_Type())
icapServiceStatsSentBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:icapServiceStatsSentBytes.setStatus(_A)
_IcapServiceStatsFailedReqs_Type=Counter64
_IcapServiceStatsFailedReqs_Object=MibTableColumn
icapServiceStatsFailedReqs=_IcapServiceStatsFailedReqs_Object((1,3,6,1,4,1,3417,2,14,1,1,1,1,1,12),_IcapServiceStatsFailedReqs_Type())
icapServiceStatsFailedReqs.setMaxAccess(_C)
if mibBuilder.loadTexts:icapServiceStatsFailedReqs.setStatus(_A)
_IcapServiceStatsSuccessfullReqs_Type=Counter64
_IcapServiceStatsSuccessfullReqs_Object=MibTableColumn
icapServiceStatsSuccessfullReqs=_IcapServiceStatsSuccessfullReqs_Object((1,3,6,1,4,1,3417,2,14,1,1,1,1,1,13),_IcapServiceStatsSuccessfullReqs_Type())
icapServiceStatsSuccessfullReqs.setMaxAccess(_C)
if mibBuilder.loadTexts:icapServiceStatsSuccessfullReqs.setStatus(_A)
_SgICAPNotification_Type=ICAPServiceNotificationType
_SgICAPNotification_Object=MibScalar
sgICAPNotification=_SgICAPNotification_Object((1,3,6,1,4,1,3417,2,14,1,1,2),_SgICAPNotification_Type())
sgICAPNotification.setMaxAccess(_C)
if mibBuilder.loadTexts:sgICAPNotification.setStatus(_A)
_BluecoatSgICAPMIBNotifications_ObjectIdentity=ObjectIdentity
bluecoatSgICAPMIBNotifications=_BluecoatSgICAPMIBNotifications_ObjectIdentity((1,3,6,1,4,1,3417,2,14,2))
_SgICAPMIBNotificationsPrefix_ObjectIdentity=ObjectIdentity
sgICAPMIBNotificationsPrefix=_SgICAPMIBNotificationsPrefix_ObjectIdentity((1,3,6,1,4,1,3417,2,14,2,0))
_BluecoatSgICAPMIBConformance_ObjectIdentity=ObjectIdentity
bluecoatSgICAPMIBConformance=_BluecoatSgICAPMIBConformance_ObjectIdentity((1,3,6,1,4,1,3417,2,14,3))
_BluecoatSgICAPMIBCompliances_ObjectIdentity=ObjectIdentity
bluecoatSgICAPMIBCompliances=_BluecoatSgICAPMIBCompliances_ObjectIdentity((1,3,6,1,4,1,3417,2,14,3,1))
_BluecoatSgICAPMIBGroups_ObjectIdentity=ObjectIdentity
bluecoatSgICAPMIBGroups=_BluecoatSgICAPMIBGroups_ObjectIdentity((1,3,6,1,4,1,3417,2,14,3,2))
_BluecoatSgICAPMIBNotifGroups_ObjectIdentity=ObjectIdentity
bluecoatSgICAPMIBNotifGroups=_BluecoatSgICAPMIBNotifGroups_ObjectIdentity((1,3,6,1,4,1,3417,2,14,3,3))
bluecoatSgICAPMIBGroup=ObjectGroup((1,3,6,1,4,1,3417,2,14,3,2,1))
bluecoatSgICAPMIBGroup.setObjects(*((_B,_D),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_E),(_B,_F),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_G)))
if mibBuilder.loadTexts:bluecoatSgICAPMIBGroup.setStatus(_A)
sgICAPTrap=NotificationType((1,3,6,1,4,1,3417,2,14,2,0,1))
sgICAPTrap.setObjects(*((_B,_G),(_B,_D),(_B,_F),(_B,_E)))
if mibBuilder.loadTexts:sgICAPTrap.setStatus(_A)
bluecoatSgICAPMIBNotifGroup=NotificationGroup((1,3,6,1,4,1,3417,2,14,3,3,1))
bluecoatSgICAPMIBNotifGroup.setObjects((_B,_T))
if mibBuilder.loadTexts:bluecoatSgICAPMIBNotifGroup.setStatus(_A)
bluecoatSgICAPMIBCompliance=ModuleCompliance((1,3,6,1,4,1,3417,2,14,3,1,1))
bluecoatSgICAPMIBCompliance.setObjects((_B,_U))
if mibBuilder.loadTexts:bluecoatSgICAPMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ICAPServiceEntityType':ICAPServiceEntityType,'ICAPServiceNotificationType':ICAPServiceNotificationType,'bluecoatSGICAPMIB':bluecoatSGICAPMIB,'bluecoatSgICAPMIBObjects':bluecoatSgICAPMIBObjects,'bluecoatSgICAPValues':bluecoatSgICAPValues,'icapService':icapService,'icapServiceStatsTable':icapServiceStatsTable,'icapServiceStatsTableEntry':icapServiceStatsTableEntry,_J:icapServiceStatsIndex,_D:icapServiceStatsName,_K:icapServiceStatsEntityType,_L:icapServiceStatsPlainConns,_M:icapServiceStatsSecuredConns,_N:icapServiceStatsPlainActvReqs,_O:icapServiceStatsSecureActvReqs,_E:icapServiceStatsQueuedReqs,_F:icapServiceStatsDeferredReqs,_P:icapServiceStatsRcvdBytes,_Q:icapServiceStatsSentBytes,_R:icapServiceStatsFailedReqs,_S:icapServiceStatsSuccessfullReqs,_G:sgICAPNotification,'bluecoatSgICAPMIBNotifications':bluecoatSgICAPMIBNotifications,'sgICAPMIBNotificationsPrefix':sgICAPMIBNotificationsPrefix,_T:sgICAPTrap,'bluecoatSgICAPMIBConformance':bluecoatSgICAPMIBConformance,'bluecoatSgICAPMIBCompliances':bluecoatSgICAPMIBCompliances,'bluecoatSgICAPMIBCompliance':bluecoatSgICAPMIBCompliance,'bluecoatSgICAPMIBGroups':bluecoatSgICAPMIBGroups,_U:bluecoatSgICAPMIBGroup,'bluecoatSgICAPMIBNotifGroups':bluecoatSgICAPMIBNotifGroups,'bluecoatSgICAPMIBNotifGroup':bluecoatSgICAPMIBNotifGroup})