_A2='cgxWanObjectGroup'
_A1='cgxWanNotificationGroup'
_A0='cgxVpnObjectGroup'
_z='cgxVpnNotificationGroup'
_y='cgxSiteObjectGroup'
_x='cgxRoutingObjectGroup'
_w='cgxRoutingNotificationGroup'
_v='cgxProcessObjectGroup'
_u='cgxProcessNotificationGroup'
_t='cgxElementObjectGroup'
_s='cgxProcessStopClear'
_r='cgxProcessStop'
_q='cgxPrivateWanUp'
_p='cgxPrivateWanDown'
_o='cgxPublicWanUp'
_n='cgxPublicWanDown'
_m='cgxPrivateWanUncreachableClear'
_l='cgxPrivateWanUncreachable'
_k='cgxPrivateWanDegradedClear'
_j='cgxPrivateWanDegraded'
_i='cgxRoutePeerUp'
_h='cgxRoutePeerDown'
_g='cgxVpnPeerUnreachableClear'
_f='cgxVpnPeerUnreachable'
_e='cgxVpnLinkUp'
_d='cgxVpnLinkDown'
_c='cgxVpnBfdUp'
_b='cgxVpnBfdDown'
_a='cgxProcessId'
_Z='cgxWanNetworkPrefix'
_Y='cgxRoutePeerName'
_X='cgxProcessName'
_W='cgxRoutePeerType'
_V='cgxRoutePeerIp'
_U='cgxRoutePeerId'
_T='cgxWanNetworkRemoteType'
_S='cgxWanNetworkRemoteName'
_R='cgxWanNetworkRemoteId'
_Q='cgxElementRemoteName'
_P='cgxElementRemoteId'
_O='cgxSiteRemoteName'
_N='cgxSiteRemoteId'
_M='cgxVpnLinkId'
_L='cgxWanNetworkType'
_K='cgxWanNetworkName'
_J='cgxWanNetworkId'
_I='cgxSiteWanInterfaceName'
_H='cgxSiteWanInterfaceId'
_G='cgxElementName'
_F='cgxElementId'
_E='cgxSiteName'
_D='cgxSiteId'
_C='accessible-for-notify'
_B='current'
_A='CGX-EVENTS-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cgxMgmt,=mibBuilder.importSymbols('CLOUDGENIX-SMI','cgxMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
cgxEventsMIB=ModuleIdentity((1,3,6,1,4,1,50114,10,1))
if mibBuilder.loadTexts:cgxEventsMIB.setRevisions(('2017-06-19 18:00',))
_CgxEventsNotifications_ObjectIdentity=ObjectIdentity
cgxEventsNotifications=_CgxEventsNotifications_ObjectIdentity((1,3,6,1,4,1,50114,10,1,0))
_CgxEventsObjects_ObjectIdentity=ObjectIdentity
cgxEventsObjects=_CgxEventsObjects_ObjectIdentity((1,3,6,1,4,1,50114,10,1,1))
_CgxEventsObjectStats_ObjectIdentity=ObjectIdentity
cgxEventsObjectStats=_CgxEventsObjectStats_ObjectIdentity((1,3,6,1,4,1,50114,10,1,1,1))
_CgxVpnObjects_ObjectIdentity=ObjectIdentity
cgxVpnObjects=_CgxVpnObjects_ObjectIdentity((1,3,6,1,4,1,50114,10,1,1,2))
_CgxVpnLinkId_Type=DisplayString
_CgxVpnLinkId_Object=MibScalar
cgxVpnLinkId=_CgxVpnLinkId_Object((1,3,6,1,4,1,50114,10,1,1,2,1),_CgxVpnLinkId_Type())
cgxVpnLinkId.setMaxAccess(_C)
if mibBuilder.loadTexts:cgxVpnLinkId.setStatus(_B)
_CgxRoutingObjects_ObjectIdentity=ObjectIdentity
cgxRoutingObjects=_CgxRoutingObjects_ObjectIdentity((1,3,6,1,4,1,50114,10,1,1,3))
_CgxRoutePeerId_Type=DisplayString
_CgxRoutePeerId_Object=MibScalar
cgxRoutePeerId=_CgxRoutePeerId_Object((1,3,6,1,4,1,50114,10,1,1,3,1),_CgxRoutePeerId_Type())
cgxRoutePeerId.setMaxAccess(_C)
if mibBuilder.loadTexts:cgxRoutePeerId.setStatus(_B)
_CgxRoutePeerName_Type=DisplayString
_CgxRoutePeerName_Object=MibScalar
cgxRoutePeerName=_CgxRoutePeerName_Object((1,3,6,1,4,1,50114,10,1,1,3,2),_CgxRoutePeerName_Type())
cgxRoutePeerName.setMaxAccess(_C)
if mibBuilder.loadTexts:cgxRoutePeerName.setStatus(_B)
_CgxRoutePeerIp_Type=IpAddress
_CgxRoutePeerIp_Object=MibScalar
cgxRoutePeerIp=_CgxRoutePeerIp_Object((1,3,6,1,4,1,50114,10,1,1,3,3),_CgxRoutePeerIp_Type())
cgxRoutePeerIp.setMaxAccess(_C)
if mibBuilder.loadTexts:cgxRoutePeerIp.setStatus(_B)
_CgxRoutePeerType_Type=DisplayString
_CgxRoutePeerType_Object=MibScalar
cgxRoutePeerType=_CgxRoutePeerType_Object((1,3,6,1,4,1,50114,10,1,1,3,4),_CgxRoutePeerType_Type())
cgxRoutePeerType.setMaxAccess(_C)
if mibBuilder.loadTexts:cgxRoutePeerType.setStatus(_B)
_CgxSiteObjects_ObjectIdentity=ObjectIdentity
cgxSiteObjects=_CgxSiteObjects_ObjectIdentity((1,3,6,1,4,1,50114,10,1,1,4))
_CgxSiteId_Type=DisplayString
_CgxSiteId_Object=MibScalar
cgxSiteId=_CgxSiteId_Object((1,3,6,1,4,1,50114,10,1,1,4,1),_CgxSiteId_Type())
cgxSiteId.setMaxAccess(_C)
if mibBuilder.loadTexts:cgxSiteId.setStatus(_B)
_CgxSiteName_Type=DisplayString
_CgxSiteName_Object=MibScalar
cgxSiteName=_CgxSiteName_Object((1,3,6,1,4,1,50114,10,1,1,4,2),_CgxSiteName_Type())
cgxSiteName.setMaxAccess(_C)
if mibBuilder.loadTexts:cgxSiteName.setStatus(_B)
_CgxSiteRemoteId_Type=DisplayString
_CgxSiteRemoteId_Object=MibScalar
cgxSiteRemoteId=_CgxSiteRemoteId_Object((1,3,6,1,4,1,50114,10,1,1,4,3),_CgxSiteRemoteId_Type())
cgxSiteRemoteId.setMaxAccess(_C)
if mibBuilder.loadTexts:cgxSiteRemoteId.setStatus(_B)
_CgxSiteRemoteName_Type=DisplayString
_CgxSiteRemoteName_Object=MibScalar
cgxSiteRemoteName=_CgxSiteRemoteName_Object((1,3,6,1,4,1,50114,10,1,1,4,4),_CgxSiteRemoteName_Type())
cgxSiteRemoteName.setMaxAccess(_C)
if mibBuilder.loadTexts:cgxSiteRemoteName.setStatus(_B)
_CgxSiteWanInterfaceId_Type=DisplayString
_CgxSiteWanInterfaceId_Object=MibScalar
cgxSiteWanInterfaceId=_CgxSiteWanInterfaceId_Object((1,3,6,1,4,1,50114,10,1,1,4,5),_CgxSiteWanInterfaceId_Type())
cgxSiteWanInterfaceId.setMaxAccess(_C)
if mibBuilder.loadTexts:cgxSiteWanInterfaceId.setStatus(_B)
_CgxSiteWanInterfaceName_Type=DisplayString
_CgxSiteWanInterfaceName_Object=MibScalar
cgxSiteWanInterfaceName=_CgxSiteWanInterfaceName_Object((1,3,6,1,4,1,50114,10,1,1,4,6),_CgxSiteWanInterfaceName_Type())
cgxSiteWanInterfaceName.setMaxAccess(_C)
if mibBuilder.loadTexts:cgxSiteWanInterfaceName.setStatus(_B)
_CgxElementObjects_ObjectIdentity=ObjectIdentity
cgxElementObjects=_CgxElementObjects_ObjectIdentity((1,3,6,1,4,1,50114,10,1,1,5))
_CgxElementId_Type=DisplayString
_CgxElementId_Object=MibScalar
cgxElementId=_CgxElementId_Object((1,3,6,1,4,1,50114,10,1,1,5,1),_CgxElementId_Type())
cgxElementId.setMaxAccess(_C)
if mibBuilder.loadTexts:cgxElementId.setStatus(_B)
_CgxElementName_Type=DisplayString
_CgxElementName_Object=MibScalar
cgxElementName=_CgxElementName_Object((1,3,6,1,4,1,50114,10,1,1,5,2),_CgxElementName_Type())
cgxElementName.setMaxAccess(_C)
if mibBuilder.loadTexts:cgxElementName.setStatus(_B)
_CgxElementRemoteId_Type=DisplayString
_CgxElementRemoteId_Object=MibScalar
cgxElementRemoteId=_CgxElementRemoteId_Object((1,3,6,1,4,1,50114,10,1,1,5,3),_CgxElementRemoteId_Type())
cgxElementRemoteId.setMaxAccess(_C)
if mibBuilder.loadTexts:cgxElementRemoteId.setStatus(_B)
_CgxElementRemoteName_Type=DisplayString
_CgxElementRemoteName_Object=MibScalar
cgxElementRemoteName=_CgxElementRemoteName_Object((1,3,6,1,4,1,50114,10,1,1,5,4),_CgxElementRemoteName_Type())
cgxElementRemoteName.setMaxAccess(_C)
if mibBuilder.loadTexts:cgxElementRemoteName.setStatus(_B)
_CgxWanObjects_ObjectIdentity=ObjectIdentity
cgxWanObjects=_CgxWanObjects_ObjectIdentity((1,3,6,1,4,1,50114,10,1,1,6))
_CgxWanNetworkId_Type=DisplayString
_CgxWanNetworkId_Object=MibScalar
cgxWanNetworkId=_CgxWanNetworkId_Object((1,3,6,1,4,1,50114,10,1,1,6,1),_CgxWanNetworkId_Type())
cgxWanNetworkId.setMaxAccess(_C)
if mibBuilder.loadTexts:cgxWanNetworkId.setStatus(_B)
_CgxWanNetworkName_Type=DisplayString
_CgxWanNetworkName_Object=MibScalar
cgxWanNetworkName=_CgxWanNetworkName_Object((1,3,6,1,4,1,50114,10,1,1,6,2),_CgxWanNetworkName_Type())
cgxWanNetworkName.setMaxAccess(_C)
if mibBuilder.loadTexts:cgxWanNetworkName.setStatus(_B)
_CgxWanNetworkType_Type=DisplayString
_CgxWanNetworkType_Object=MibScalar
cgxWanNetworkType=_CgxWanNetworkType_Object((1,3,6,1,4,1,50114,10,1,1,6,3),_CgxWanNetworkType_Type())
cgxWanNetworkType.setMaxAccess(_C)
if mibBuilder.loadTexts:cgxWanNetworkType.setStatus(_B)
_CgxWanNetworkRemoteId_Type=DisplayString
_CgxWanNetworkRemoteId_Object=MibScalar
cgxWanNetworkRemoteId=_CgxWanNetworkRemoteId_Object((1,3,6,1,4,1,50114,10,1,1,6,4),_CgxWanNetworkRemoteId_Type())
cgxWanNetworkRemoteId.setMaxAccess(_C)
if mibBuilder.loadTexts:cgxWanNetworkRemoteId.setStatus(_B)
_CgxWanNetworkRemoteName_Type=DisplayString
_CgxWanNetworkRemoteName_Object=MibScalar
cgxWanNetworkRemoteName=_CgxWanNetworkRemoteName_Object((1,3,6,1,4,1,50114,10,1,1,6,5),_CgxWanNetworkRemoteName_Type())
cgxWanNetworkRemoteName.setMaxAccess(_C)
if mibBuilder.loadTexts:cgxWanNetworkRemoteName.setStatus(_B)
_CgxWanNetworkRemoteType_Type=DisplayString
_CgxWanNetworkRemoteType_Object=MibScalar
cgxWanNetworkRemoteType=_CgxWanNetworkRemoteType_Object((1,3,6,1,4,1,50114,10,1,1,6,6),_CgxWanNetworkRemoteType_Type())
cgxWanNetworkRemoteType.setMaxAccess(_C)
if mibBuilder.loadTexts:cgxWanNetworkRemoteType.setStatus(_B)
_CgxWanNetworkPrefix_Type=DisplayString
_CgxWanNetworkPrefix_Object=MibScalar
cgxWanNetworkPrefix=_CgxWanNetworkPrefix_Object((1,3,6,1,4,1,50114,10,1,1,6,7),_CgxWanNetworkPrefix_Type())
cgxWanNetworkPrefix.setMaxAccess(_C)
if mibBuilder.loadTexts:cgxWanNetworkPrefix.setStatus(_B)
_CgxProcessObjects_ObjectIdentity=ObjectIdentity
cgxProcessObjects=_CgxProcessObjects_ObjectIdentity((1,3,6,1,4,1,50114,10,1,1,7))
_CgxProcessId_Type=DisplayString
_CgxProcessId_Object=MibScalar
cgxProcessId=_CgxProcessId_Object((1,3,6,1,4,1,50114,10,1,1,7,1),_CgxProcessId_Type())
cgxProcessId.setMaxAccess(_C)
if mibBuilder.loadTexts:cgxProcessId.setStatus(_B)
_CgxProcessName_Type=DisplayString
_CgxProcessName_Object=MibScalar
cgxProcessName=_CgxProcessName_Object((1,3,6,1,4,1,50114,10,1,1,7,2),_CgxProcessName_Type())
cgxProcessName.setMaxAccess(_C)
if mibBuilder.loadTexts:cgxProcessName.setStatus(_B)
_CgxEventsConformance_ObjectIdentity=ObjectIdentity
cgxEventsConformance=_CgxEventsConformance_ObjectIdentity((1,3,6,1,4,1,50114,10,1,2))
_CgxEventsCompliances_ObjectIdentity=ObjectIdentity
cgxEventsCompliances=_CgxEventsCompliances_ObjectIdentity((1,3,6,1,4,1,50114,10,1,2,1))
_CgxEventsGroups_ObjectIdentity=ObjectIdentity
cgxEventsGroups=_CgxEventsGroups_ObjectIdentity((1,3,6,1,4,1,50114,10,1,2,2))
cgxVpnObjectGroup=ObjectGroup((1,3,6,1,4,1,50114,10,1,2,2,2))
cgxVpnObjectGroup.setObjects((_A,_M))
if mibBuilder.loadTexts:cgxVpnObjectGroup.setStatus(_B)
cgxRoutingObjectGroup=ObjectGroup((1,3,6,1,4,1,50114,10,1,2,2,3))
cgxRoutingObjectGroup.setObjects(*((_A,_U),(_A,_V),(_A,_Y),(_A,_W)))
if mibBuilder.loadTexts:cgxRoutingObjectGroup.setStatus(_B)
cgxSiteObjectGroup=ObjectGroup((1,3,6,1,4,1,50114,10,1,2,2,4))
cgxSiteObjectGroup.setObjects(*((_A,_D),(_A,_E),(_A,_N),(_A,_O),(_A,_H),(_A,_I)))
if mibBuilder.loadTexts:cgxSiteObjectGroup.setStatus(_B)
cgxElementObjectGroup=ObjectGroup((1,3,6,1,4,1,50114,10,1,2,2,5))
cgxElementObjectGroup.setObjects(*((_A,_F),(_A,_G),(_A,_P),(_A,_Q)))
if mibBuilder.loadTexts:cgxElementObjectGroup.setStatus(_B)
cgxWanObjectGroup=ObjectGroup((1,3,6,1,4,1,50114,10,1,2,2,6))
cgxWanObjectGroup.setObjects(*((_A,_J),(_A,_K),(_A,_L),(_A,_R),(_A,_S),(_A,_T),(_A,_Z)))
if mibBuilder.loadTexts:cgxWanObjectGroup.setStatus(_B)
cgxProcessObjectGroup=ObjectGroup((1,3,6,1,4,1,50114,10,1,2,2,7))
cgxProcessObjectGroup.setObjects(*((_A,_a),(_A,_X)))
if mibBuilder.loadTexts:cgxProcessObjectGroup.setStatus(_B)
cgxVpnLinkUp=NotificationType((1,3,6,1,4,1,50114,10,1,0,1))
cgxVpnLinkUp.setObjects(*((_A,_F),(_A,_G),(_A,_P),(_A,_Q),(_A,_D),(_A,_E),(_A,_N),(_A,_O),(_A,_H),(_A,_I),(_A,_M),(_A,_J),(_A,_K),(_A,_L),(_A,_R),(_A,_S),(_A,_T)))
if mibBuilder.loadTexts:cgxVpnLinkUp.setStatus(_B)
cgxVpnLinkDown=NotificationType((1,3,6,1,4,1,50114,10,1,0,2))
cgxVpnLinkDown.setObjects(*((_A,_F),(_A,_G),(_A,_P),(_A,_Q),(_A,_D),(_A,_E),(_A,_N),(_A,_O),(_A,_H),(_A,_I),(_A,_M),(_A,_J),(_A,_K),(_A,_L),(_A,_R),(_A,_S),(_A,_T)))
if mibBuilder.loadTexts:cgxVpnLinkDown.setStatus(_B)
cgxVpnPeerUnreachableClear=NotificationType((1,3,6,1,4,1,50114,10,1,0,3))
cgxVpnPeerUnreachableClear.setObjects(*((_A,_F),(_A,_G),(_A,_P),(_A,_Q),(_A,_D),(_A,_E),(_A,_N),(_A,_O),(_A,_H),(_A,_I),(_A,_M),(_A,_J),(_A,_K),(_A,_L),(_A,_R),(_A,_S),(_A,_T)))
if mibBuilder.loadTexts:cgxVpnPeerUnreachableClear.setStatus(_B)
cgxVpnPeerUnreachable=NotificationType((1,3,6,1,4,1,50114,10,1,0,4))
cgxVpnPeerUnreachable.setObjects(*((_A,_F),(_A,_G),(_A,_P),(_A,_Q),(_A,_D),(_A,_E),(_A,_N),(_A,_O),(_A,_H),(_A,_I),(_A,_M),(_A,_J),(_A,_K),(_A,_L),(_A,_R),(_A,_S),(_A,_T)))
if mibBuilder.loadTexts:cgxVpnPeerUnreachable.setStatus(_B)
cgxVpnBfdUp=NotificationType((1,3,6,1,4,1,50114,10,1,0,5))
cgxVpnBfdUp.setObjects(*((_A,_F),(_A,_G),(_A,_P),(_A,_Q),(_A,_D),(_A,_E),(_A,_N),(_A,_O),(_A,_H),(_A,_I),(_A,_M),(_A,_J),(_A,_K),(_A,_L),(_A,_R),(_A,_S),(_A,_T)))
if mibBuilder.loadTexts:cgxVpnBfdUp.setStatus(_B)
cgxVpnBfdDown=NotificationType((1,3,6,1,4,1,50114,10,1,0,6))
cgxVpnBfdDown.setObjects(*((_A,_F),(_A,_G),(_A,_P),(_A,_Q),(_A,_D),(_A,_E),(_A,_N),(_A,_O),(_A,_H),(_A,_I),(_A,_M),(_A,_J),(_A,_K),(_A,_L),(_A,_R),(_A,_S),(_A,_T)))
if mibBuilder.loadTexts:cgxVpnBfdDown.setStatus(_B)
cgxRoutePeerUp=NotificationType((1,3,6,1,4,1,50114,10,1,0,101))
cgxRoutePeerUp.setObjects(*((_A,_F),(_A,_G),(_A,_D),(_A,_E),(_A,_U),(_A,_V),(_A,_W)))
if mibBuilder.loadTexts:cgxRoutePeerUp.setStatus(_B)
cgxRoutePeerDown=NotificationType((1,3,6,1,4,1,50114,10,1,0,102))
cgxRoutePeerDown.setObjects(*((_A,_F),(_A,_G),(_A,_D),(_A,_E),(_A,_U),(_A,_V),(_A,_W)))
if mibBuilder.loadTexts:cgxRoutePeerDown.setStatus(_B)
cgxPrivateWanUncreachableClear=NotificationType((1,3,6,1,4,1,50114,10,1,0,201))
cgxPrivateWanUncreachableClear.setObjects(*((_A,_F),(_A,_G),(_A,_D),(_A,_E),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L)))
if mibBuilder.loadTexts:cgxPrivateWanUncreachableClear.setStatus(_B)
cgxPrivateWanUncreachable=NotificationType((1,3,6,1,4,1,50114,10,1,0,202))
cgxPrivateWanUncreachable.setObjects(*((_A,_F),(_A,_G),(_A,_D),(_A,_E),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L)))
if mibBuilder.loadTexts:cgxPrivateWanUncreachable.setStatus(_B)
cgxPrivateWanDegradedClear=NotificationType((1,3,6,1,4,1,50114,10,1,0,203))
cgxPrivateWanDegradedClear.setObjects(*((_A,_F),(_A,_G),(_A,_D),(_A,_E),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L)))
if mibBuilder.loadTexts:cgxPrivateWanDegradedClear.setStatus(_B)
cgxPrivateWanDegraded=NotificationType((1,3,6,1,4,1,50114,10,1,0,204))
cgxPrivateWanDegraded.setObjects(*((_A,_F),(_A,_G),(_A,_D),(_A,_E),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L)))
if mibBuilder.loadTexts:cgxPrivateWanDegraded.setStatus(_B)
cgxPublicWanUp=NotificationType((1,3,6,1,4,1,50114,10,1,0,205))
cgxPublicWanUp.setObjects(*((_A,_F),(_A,_G),(_A,_D),(_A,_E),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L)))
if mibBuilder.loadTexts:cgxPublicWanUp.setStatus(_B)
cgxPublicWanDown=NotificationType((1,3,6,1,4,1,50114,10,1,0,206))
cgxPublicWanDown.setObjects(*((_A,_F),(_A,_G),(_A,_D),(_A,_E),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L)))
if mibBuilder.loadTexts:cgxPublicWanDown.setStatus(_B)
cgxPrivateWanUp=NotificationType((1,3,6,1,4,1,50114,10,1,0,207))
cgxPrivateWanUp.setObjects(*((_A,_F),(_A,_G),(_A,_D),(_A,_E),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L)))
if mibBuilder.loadTexts:cgxPrivateWanUp.setStatus(_B)
cgxPrivateWanDown=NotificationType((1,3,6,1,4,1,50114,10,1,0,208))
cgxPrivateWanDown.setObjects(*((_A,_F),(_A,_G),(_A,_D),(_A,_E),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L)))
if mibBuilder.loadTexts:cgxPrivateWanDown.setStatus(_B)
cgxProcessStopClear=NotificationType((1,3,6,1,4,1,50114,10,1,0,301))
cgxProcessStopClear.setObjects(*((_A,_F),(_A,_G),(_A,_D),(_A,_E),(_A,_X)))
if mibBuilder.loadTexts:cgxProcessStopClear.setStatus(_B)
cgxProcessStop=NotificationType((1,3,6,1,4,1,50114,10,1,0,302))
cgxProcessStop.setObjects(*((_A,_F),(_A,_G),(_A,_D),(_A,_E),(_A,_X)))
if mibBuilder.loadTexts:cgxProcessStop.setStatus(_B)
cgxVpnNotificationGroup=NotificationGroup((1,3,6,1,4,1,50114,10,1,2,2,102))
cgxVpnNotificationGroup.setObjects(*((_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g)))
if mibBuilder.loadTexts:cgxVpnNotificationGroup.setStatus(_B)
cgxRoutingNotificationGroup=NotificationGroup((1,3,6,1,4,1,50114,10,1,2,2,103))
cgxRoutingNotificationGroup.setObjects(*((_A,_h),(_A,_i)))
if mibBuilder.loadTexts:cgxRoutingNotificationGroup.setStatus(_B)
cgxWanNotificationGroup=NotificationGroup((1,3,6,1,4,1,50114,10,1,2,2,104))
cgxWanNotificationGroup.setObjects(*((_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q)))
if mibBuilder.loadTexts:cgxWanNotificationGroup.setStatus(_B)
cgxProcessNotificationGroup=NotificationGroup((1,3,6,1,4,1,50114,10,1,2,2,105))
cgxProcessNotificationGroup.setObjects(*((_A,_r),(_A,_s)))
if mibBuilder.loadTexts:cgxProcessNotificationGroup.setStatus(_B)
cgxEventsMIBCompliance=ModuleCompliance((1,3,6,1,4,1,50114,10,1,2,1,1))
cgxEventsMIBCompliance.setObjects(*((_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2)))
if mibBuilder.loadTexts:cgxEventsMIBCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'cgxEventsMIB':cgxEventsMIB,'cgxEventsNotifications':cgxEventsNotifications,_e:cgxVpnLinkUp,_d:cgxVpnLinkDown,_g:cgxVpnPeerUnreachableClear,_f:cgxVpnPeerUnreachable,_c:cgxVpnBfdUp,_b:cgxVpnBfdDown,_i:cgxRoutePeerUp,_h:cgxRoutePeerDown,_m:cgxPrivateWanUncreachableClear,_l:cgxPrivateWanUncreachable,_k:cgxPrivateWanDegradedClear,_j:cgxPrivateWanDegraded,_o:cgxPublicWanUp,_n:cgxPublicWanDown,_q:cgxPrivateWanUp,_p:cgxPrivateWanDown,_s:cgxProcessStopClear,_r:cgxProcessStop,'cgxEventsObjects':cgxEventsObjects,'cgxEventsObjectStats':cgxEventsObjectStats,'cgxVpnObjects':cgxVpnObjects,_M:cgxVpnLinkId,'cgxRoutingObjects':cgxRoutingObjects,_U:cgxRoutePeerId,_Y:cgxRoutePeerName,_V:cgxRoutePeerIp,_W:cgxRoutePeerType,'cgxSiteObjects':cgxSiteObjects,_D:cgxSiteId,_E:cgxSiteName,_N:cgxSiteRemoteId,_O:cgxSiteRemoteName,_H:cgxSiteWanInterfaceId,_I:cgxSiteWanInterfaceName,'cgxElementObjects':cgxElementObjects,_F:cgxElementId,_G:cgxElementName,_P:cgxElementRemoteId,_Q:cgxElementRemoteName,'cgxWanObjects':cgxWanObjects,_J:cgxWanNetworkId,_K:cgxWanNetworkName,_L:cgxWanNetworkType,_R:cgxWanNetworkRemoteId,_S:cgxWanNetworkRemoteName,_T:cgxWanNetworkRemoteType,_Z:cgxWanNetworkPrefix,'cgxProcessObjects':cgxProcessObjects,_a:cgxProcessId,_X:cgxProcessName,'cgxEventsConformance':cgxEventsConformance,'cgxEventsCompliances':cgxEventsCompliances,'cgxEventsMIBCompliance':cgxEventsMIBCompliance,'cgxEventsGroups':cgxEventsGroups,_A0:cgxVpnObjectGroup,_x:cgxRoutingObjectGroup,_y:cgxSiteObjectGroup,_t:cgxElementObjectGroup,_A2:cgxWanObjectGroup,_v:cgxProcessObjectGroup,_z:cgxVpnNotificationGroup,_w:cgxRoutingNotificationGroup,_A1:cgxWanNotificationGroup,_u:cgxProcessNotificationGroup})