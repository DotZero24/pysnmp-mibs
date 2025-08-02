_e='alvarionUserSessionStMIBGroup'
_d='alvarionUserSessionInfoMIBGroup'
_c='coUserSessPacketsReceived'
_b='coUserSessPacketsSent'
_a='coUserSessBytesReceived'
_Z='coUserSessBytesSent'
_Y='coUserSessRADIUSServerIpAddress'
_X='coUserSessRADIUSServerProfileName'
_W='coUserSessCallingStationID'
_V='coUserSessCalledStationID'
_U='coUserSessAuthType'
_T='coUserSessPHYType'
_S='coUserSessVLAN'
_R='coUserSessSSID'
_Q='coUserSessVSCName'
_P='coUserSessMAPGroupName'
_O='coUserSessIdleTime'
_N='coUserSessSessionDuration'
_M='coUserSessClientIpAddress'
_L='coUserSessUserName'
_K='coUserSessNonACUserCount'
_J='coUserSessACUserCount'
_I='coUserSessNonACUserMaxCount'
_H='coUserSessACUserMaxCount'
_G='seconds'
_F='coUserSessIndex'
_E='Integer32'
_D='OctetString'
_C='read-only'
_B='ALVARION-USER-SESSION-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
alvarionMgmtV2,=mibBuilder.importSymbols('ALVARION-SMI','alvarionMgmtV2')
AlvarionSSIDOrNone,=mibBuilder.importSymbols('ALVARION-TC','AlvarionSSIDOrNone')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
alvarionUserSessionMIB=ModuleIdentity((1,3,6,1,4,1,12394,1,10,5,36))
_AlvarionUserSessionMIBObjects_ObjectIdentity=ObjectIdentity
alvarionUserSessionMIBObjects=_AlvarionUserSessionMIBObjects_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,36,1))
_CoUserSessionInfoGroup_ObjectIdentity=ObjectIdentity
coUserSessionInfoGroup=_CoUserSessionInfoGroup_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,36,1,1))
_CoUserSessACUserMaxCount_Type=Unsigned32
_CoUserSessACUserMaxCount_Object=MibScalar
coUserSessACUserMaxCount=_CoUserSessACUserMaxCount_Object((1,3,6,1,4,1,12394,1,10,5,36,1,1,1),_CoUserSessACUserMaxCount_Type())
coUserSessACUserMaxCount.setMaxAccess(_C)
if mibBuilder.loadTexts:coUserSessACUserMaxCount.setStatus(_A)
_CoUserSessNonACUserMaxCount_Type=Unsigned32
_CoUserSessNonACUserMaxCount_Object=MibScalar
coUserSessNonACUserMaxCount=_CoUserSessNonACUserMaxCount_Object((1,3,6,1,4,1,12394,1,10,5,36,1,1,2),_CoUserSessNonACUserMaxCount_Type())
coUserSessNonACUserMaxCount.setMaxAccess(_C)
if mibBuilder.loadTexts:coUserSessNonACUserMaxCount.setStatus(_A)
_CoUserSessACUserCount_Type=Gauge32
_CoUserSessACUserCount_Object=MibScalar
coUserSessACUserCount=_CoUserSessACUserCount_Object((1,3,6,1,4,1,12394,1,10,5,36,1,1,3),_CoUserSessACUserCount_Type())
coUserSessACUserCount.setMaxAccess(_C)
if mibBuilder.loadTexts:coUserSessACUserCount.setStatus(_A)
_CoUserSessNonACUserCount_Type=Gauge32
_CoUserSessNonACUserCount_Object=MibScalar
coUserSessNonACUserCount=_CoUserSessNonACUserCount_Object((1,3,6,1,4,1,12394,1,10,5,36,1,1,4),_CoUserSessNonACUserCount_Type())
coUserSessNonACUserCount.setMaxAccess(_C)
if mibBuilder.loadTexts:coUserSessNonACUserCount.setStatus(_A)
_CoUserSessionStGroup_ObjectIdentity=ObjectIdentity
coUserSessionStGroup=_CoUserSessionStGroup_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,36,1,2))
_CoUserSessionTable_Object=MibTable
coUserSessionTable=_CoUserSessionTable_Object((1,3,6,1,4,1,12394,1,10,5,36,1,2,1))
if mibBuilder.loadTexts:coUserSessionTable.setStatus(_A)
_CoUserSessionEntry_Object=MibTableRow
coUserSessionEntry=_CoUserSessionEntry_Object((1,3,6,1,4,1,12394,1,10,5,36,1,2,1,1))
coUserSessionEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:coUserSessionEntry.setStatus(_A)
class _CoUserSessIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CoUserSessIndex_Type.__name__=_E
_CoUserSessIndex_Object=MibTableColumn
coUserSessIndex=_CoUserSessIndex_Object((1,3,6,1,4,1,12394,1,10,5,36,1,2,1,1,1),_CoUserSessIndex_Type())
coUserSessIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:coUserSessIndex.setStatus(_A)
class _CoUserSessUserName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,252))
_CoUserSessUserName_Type.__name__=_D
_CoUserSessUserName_Object=MibTableColumn
coUserSessUserName=_CoUserSessUserName_Object((1,3,6,1,4,1,12394,1,10,5,36,1,2,1,1,2),_CoUserSessUserName_Type())
coUserSessUserName.setMaxAccess(_C)
if mibBuilder.loadTexts:coUserSessUserName.setStatus(_A)
_CoUserSessClientIpAddress_Type=IpAddress
_CoUserSessClientIpAddress_Object=MibTableColumn
coUserSessClientIpAddress=_CoUserSessClientIpAddress_Object((1,3,6,1,4,1,12394,1,10,5,36,1,2,1,1,3),_CoUserSessClientIpAddress_Type())
coUserSessClientIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:coUserSessClientIpAddress.setStatus(_A)
_CoUserSessSessionDuration_Type=Counter32
_CoUserSessSessionDuration_Object=MibTableColumn
coUserSessSessionDuration=_CoUserSessSessionDuration_Object((1,3,6,1,4,1,12394,1,10,5,36,1,2,1,1,4),_CoUserSessSessionDuration_Type())
coUserSessSessionDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:coUserSessSessionDuration.setStatus(_A)
if mibBuilder.loadTexts:coUserSessSessionDuration.setUnits(_G)
_CoUserSessIdleTime_Type=Counter32
_CoUserSessIdleTime_Object=MibTableColumn
coUserSessIdleTime=_CoUserSessIdleTime_Object((1,3,6,1,4,1,12394,1,10,5,36,1,2,1,1,5),_CoUserSessIdleTime_Type())
coUserSessIdleTime.setMaxAccess(_C)
if mibBuilder.loadTexts:coUserSessIdleTime.setStatus(_A)
if mibBuilder.loadTexts:coUserSessIdleTime.setUnits(_G)
class _CoUserSessMAPGroupName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_CoUserSessMAPGroupName_Type.__name__=_D
_CoUserSessMAPGroupName_Object=MibTableColumn
coUserSessMAPGroupName=_CoUserSessMAPGroupName_Object((1,3,6,1,4,1,12394,1,10,5,36,1,2,1,1,6),_CoUserSessMAPGroupName_Type())
coUserSessMAPGroupName.setMaxAccess(_C)
if mibBuilder.loadTexts:coUserSessMAPGroupName.setStatus(_A)
class _CoUserSessVSCName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CoUserSessVSCName_Type.__name__=_D
_CoUserSessVSCName_Object=MibTableColumn
coUserSessVSCName=_CoUserSessVSCName_Object((1,3,6,1,4,1,12394,1,10,5,36,1,2,1,1,7),_CoUserSessVSCName_Type())
coUserSessVSCName.setMaxAccess(_C)
if mibBuilder.loadTexts:coUserSessVSCName.setStatus(_A)
_CoUserSessSSID_Type=AlvarionSSIDOrNone
_CoUserSessSSID_Object=MibTableColumn
coUserSessSSID=_CoUserSessSSID_Object((1,3,6,1,4,1,12394,1,10,5,36,1,2,1,1,8),_CoUserSessSSID_Type())
coUserSessSSID.setMaxAccess(_C)
if mibBuilder.loadTexts:coUserSessSSID.setStatus(_A)
class _CoUserSessVLAN_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_CoUserSessVLAN_Type.__name__=_E
_CoUserSessVLAN_Object=MibTableColumn
coUserSessVLAN=_CoUserSessVLAN_Object((1,3,6,1,4,1,12394,1,10,5,36,1,2,1,1,9),_CoUserSessVLAN_Type())
coUserSessVLAN.setMaxAccess(_C)
if mibBuilder.loadTexts:coUserSessVLAN.setStatus(_A)
class _CoUserSessPHYType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('unknown',0),('ieee802dot11a',1),('ieee802dot11b',2),('ieee802dot11g',3)))
_CoUserSessPHYType_Type.__name__=_E
_CoUserSessPHYType_Object=MibTableColumn
coUserSessPHYType=_CoUserSessPHYType_Object((1,3,6,1,4,1,12394,1,10,5,36,1,2,1,1,10),_CoUserSessPHYType_Type())
coUserSessPHYType.setMaxAccess(_C)
if mibBuilder.loadTexts:coUserSessPHYType.setStatus(_A)
class _CoUserSessAuthType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ac',1),('nonAc',2)))
_CoUserSessAuthType_Type.__name__=_E
_CoUserSessAuthType_Object=MibTableColumn
coUserSessAuthType=_CoUserSessAuthType_Object((1,3,6,1,4,1,12394,1,10,5,36,1,2,1,1,11),_CoUserSessAuthType_Type())
coUserSessAuthType.setMaxAccess(_C)
if mibBuilder.loadTexts:coUserSessAuthType.setStatus(_A)
class _CoUserSessCalledStationID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,252))
_CoUserSessCalledStationID_Type.__name__=_D
_CoUserSessCalledStationID_Object=MibTableColumn
coUserSessCalledStationID=_CoUserSessCalledStationID_Object((1,3,6,1,4,1,12394,1,10,5,36,1,2,1,1,12),_CoUserSessCalledStationID_Type())
coUserSessCalledStationID.setMaxAccess(_C)
if mibBuilder.loadTexts:coUserSessCalledStationID.setStatus(_A)
class _CoUserSessCallingStationID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,252))
_CoUserSessCallingStationID_Type.__name__=_D
_CoUserSessCallingStationID_Object=MibTableColumn
coUserSessCallingStationID=_CoUserSessCallingStationID_Object((1,3,6,1,4,1,12394,1,10,5,36,1,2,1,1,13),_CoUserSessCallingStationID_Type())
coUserSessCallingStationID.setMaxAccess(_C)
if mibBuilder.loadTexts:coUserSessCallingStationID.setStatus(_A)
class _CoUserSessRADIUSServerProfileName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_CoUserSessRADIUSServerProfileName_Type.__name__=_D
_CoUserSessRADIUSServerProfileName_Object=MibTableColumn
coUserSessRADIUSServerProfileName=_CoUserSessRADIUSServerProfileName_Object((1,3,6,1,4,1,12394,1,10,5,36,1,2,1,1,14),_CoUserSessRADIUSServerProfileName_Type())
coUserSessRADIUSServerProfileName.setMaxAccess(_C)
if mibBuilder.loadTexts:coUserSessRADIUSServerProfileName.setStatus(_A)
_CoUserSessRADIUSServerIpAddress_Type=IpAddress
_CoUserSessRADIUSServerIpAddress_Object=MibTableColumn
coUserSessRADIUSServerIpAddress=_CoUserSessRADIUSServerIpAddress_Object((1,3,6,1,4,1,12394,1,10,5,36,1,2,1,1,15),_CoUserSessRADIUSServerIpAddress_Type())
coUserSessRADIUSServerIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:coUserSessRADIUSServerIpAddress.setStatus(_A)
_CoUserSessBytesSent_Type=Counter64
_CoUserSessBytesSent_Object=MibTableColumn
coUserSessBytesSent=_CoUserSessBytesSent_Object((1,3,6,1,4,1,12394,1,10,5,36,1,2,1,1,16),_CoUserSessBytesSent_Type())
coUserSessBytesSent.setMaxAccess(_C)
if mibBuilder.loadTexts:coUserSessBytesSent.setStatus(_A)
_CoUserSessBytesReceived_Type=Counter64
_CoUserSessBytesReceived_Object=MibTableColumn
coUserSessBytesReceived=_CoUserSessBytesReceived_Object((1,3,6,1,4,1,12394,1,10,5,36,1,2,1,1,17),_CoUserSessBytesReceived_Type())
coUserSessBytesReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:coUserSessBytesReceived.setStatus(_A)
_CoUserSessPacketsSent_Type=Counter32
_CoUserSessPacketsSent_Object=MibTableColumn
coUserSessPacketsSent=_CoUserSessPacketsSent_Object((1,3,6,1,4,1,12394,1,10,5,36,1,2,1,1,18),_CoUserSessPacketsSent_Type())
coUserSessPacketsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:coUserSessPacketsSent.setStatus(_A)
_CoUserSessPacketsReceived_Type=Counter32
_CoUserSessPacketsReceived_Object=MibTableColumn
coUserSessPacketsReceived=_CoUserSessPacketsReceived_Object((1,3,6,1,4,1,12394,1,10,5,36,1,2,1,1,19),_CoUserSessPacketsReceived_Type())
coUserSessPacketsReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:coUserSessPacketsReceived.setStatus(_A)
_UserSessionMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
userSessionMIBNotificationPrefix=_UserSessionMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,36,2))
_UserSessionMIBNotifications_ObjectIdentity=ObjectIdentity
userSessionMIBNotifications=_UserSessionMIBNotifications_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,36,2,0))
_AlvarionUserSessionMIBConformance_ObjectIdentity=ObjectIdentity
alvarionUserSessionMIBConformance=_AlvarionUserSessionMIBConformance_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,36,3))
_AlvarionUserSessionMIBCompliances_ObjectIdentity=ObjectIdentity
alvarionUserSessionMIBCompliances=_AlvarionUserSessionMIBCompliances_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,36,3,1))
_AlvarionUserSessionMIBGroups_ObjectIdentity=ObjectIdentity
alvarionUserSessionMIBGroups=_AlvarionUserSessionMIBGroups_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,36,3,2))
alvarionUserSessionInfoMIBGroup=ObjectGroup((1,3,6,1,4,1,12394,1,10,5,36,3,2,1))
alvarionUserSessionInfoMIBGroup.setObjects(*((_B,_H),(_B,_I),(_B,_J),(_B,_K)))
if mibBuilder.loadTexts:alvarionUserSessionInfoMIBGroup.setStatus(_A)
alvarionUserSessionStMIBGroup=ObjectGroup((1,3,6,1,4,1,12394,1,10,5,36,3,2,2))
alvarionUserSessionStMIBGroup.setObjects(*((_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c)))
if mibBuilder.loadTexts:alvarionUserSessionStMIBGroup.setStatus(_A)
alvarionUserSessionMIBCompliance=ModuleCompliance((1,3,6,1,4,1,12394,1,10,5,36,3,1,1))
alvarionUserSessionMIBCompliance.setObjects(*((_B,_d),(_B,_e)))
if mibBuilder.loadTexts:alvarionUserSessionMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'alvarionUserSessionMIB':alvarionUserSessionMIB,'alvarionUserSessionMIBObjects':alvarionUserSessionMIBObjects,'coUserSessionInfoGroup':coUserSessionInfoGroup,_H:coUserSessACUserMaxCount,_I:coUserSessNonACUserMaxCount,_J:coUserSessACUserCount,_K:coUserSessNonACUserCount,'coUserSessionStGroup':coUserSessionStGroup,'coUserSessionTable':coUserSessionTable,'coUserSessionEntry':coUserSessionEntry,_F:coUserSessIndex,_L:coUserSessUserName,_M:coUserSessClientIpAddress,_N:coUserSessSessionDuration,_O:coUserSessIdleTime,_P:coUserSessMAPGroupName,_Q:coUserSessVSCName,_R:coUserSessSSID,_S:coUserSessVLAN,_T:coUserSessPHYType,_U:coUserSessAuthType,_V:coUserSessCalledStationID,_W:coUserSessCallingStationID,_X:coUserSessRADIUSServerProfileName,_Y:coUserSessRADIUSServerIpAddress,_Z:coUserSessBytesSent,_a:coUserSessBytesReceived,_b:coUserSessPacketsSent,_c:coUserSessPacketsReceived,'userSessionMIBNotificationPrefix':userSessionMIBNotificationPrefix,'userSessionMIBNotifications':userSessionMIBNotifications,'alvarionUserSessionMIBConformance':alvarionUserSessionMIBConformance,'alvarionUserSessionMIBCompliances':alvarionUserSessionMIBCompliances,'alvarionUserSessionMIBCompliance':alvarionUserSessionMIBCompliance,'alvarionUserSessionMIBGroups':alvarionUserSessionMIBGroups,_d:alvarionUserSessionInfoMIBGroup,_e:alvarionUserSessionStMIBGroup})