_O='colubrisConnectionLimitingNotificationGroup'
_N='colubrisConnectionLimitingInfoMIBGroup'
_M='colubrisConnectionLimitingConfigMIBGroup'
_L='connectionLimitingMaximumUserConnectionsReached'
_K='connectionLimitingMaximumSystemConnections'
_J='connectionLimitingNotificationEnabled'
_I='accessible-for-notify'
_H='read-write'
_G='Integer32'
_F='ColubrisNotificationEnable'
_E='connectionLimitingUserIPAddress'
_D='connectionLimitingUserMACAddress'
_C='connectionLimitingMaximumUserConnections'
_B='current'
_A='COLUBRIS-CONNECTION-LIMITING-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
colubrisMgmtV2,=mibBuilder.importSymbols('COLUBRIS-SMI','colubrisMgmtV2')
ColubrisNotificationEnable,=mibBuilder.importSymbols('COLUBRIS-TC',_F)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
colubrisConnectionLimitingMIB=ModuleIdentity((1,3,6,1,4,1,8744,5,18))
_ColubrisConnectionLimitingMIBObjects_ObjectIdentity=ObjectIdentity
colubrisConnectionLimitingMIBObjects=_ColubrisConnectionLimitingMIBObjects_ObjectIdentity((1,3,6,1,4,1,8744,5,18,1))
_ConnectionLimitingConfig_ObjectIdentity=ObjectIdentity
connectionLimitingConfig=_ConnectionLimitingConfig_ObjectIdentity((1,3,6,1,4,1,8744,5,18,1,1))
class _ConnectionLimitingMaximumUserConnections_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(20,2000))
_ConnectionLimitingMaximumUserConnections_Type.__name__=_G
_ConnectionLimitingMaximumUserConnections_Object=MibScalar
connectionLimitingMaximumUserConnections=_ConnectionLimitingMaximumUserConnections_Object((1,3,6,1,4,1,8744,5,18,1,1,1),_ConnectionLimitingMaximumUserConnections_Type())
connectionLimitingMaximumUserConnections.setMaxAccess(_H)
if mibBuilder.loadTexts:connectionLimitingMaximumUserConnections.setStatus(_B)
class _ConnectionLimitingNotificationEnabled_Type(ColubrisNotificationEnable):defaultValue=1
_ConnectionLimitingNotificationEnabled_Type.__name__=_F
_ConnectionLimitingNotificationEnabled_Object=MibScalar
connectionLimitingNotificationEnabled=_ConnectionLimitingNotificationEnabled_Object((1,3,6,1,4,1,8744,5,18,1,1,2),_ConnectionLimitingNotificationEnabled_Type())
connectionLimitingNotificationEnabled.setMaxAccess(_H)
if mibBuilder.loadTexts:connectionLimitingNotificationEnabled.setStatus(_B)
_ConnectionLimitingInfo_ObjectIdentity=ObjectIdentity
connectionLimitingInfo=_ConnectionLimitingInfo_ObjectIdentity((1,3,6,1,4,1,8744,5,18,1,2))
_ConnectionLimitingMaximumSystemConnections_Type=Integer32
_ConnectionLimitingMaximumSystemConnections_Object=MibScalar
connectionLimitingMaximumSystemConnections=_ConnectionLimitingMaximumSystemConnections_Object((1,3,6,1,4,1,8744,5,18,1,2,1),_ConnectionLimitingMaximumSystemConnections_Type())
connectionLimitingMaximumSystemConnections.setMaxAccess('read-only')
if mibBuilder.loadTexts:connectionLimitingMaximumSystemConnections.setStatus(_B)
_ConnectionLimitingUserMACAddress_Type=MacAddress
_ConnectionLimitingUserMACAddress_Object=MibScalar
connectionLimitingUserMACAddress=_ConnectionLimitingUserMACAddress_Object((1,3,6,1,4,1,8744,5,18,1,2,2),_ConnectionLimitingUserMACAddress_Type())
connectionLimitingUserMACAddress.setMaxAccess(_I)
if mibBuilder.loadTexts:connectionLimitingUserMACAddress.setStatus(_B)
_ConnectionLimitingUserIPAddress_Type=IpAddress
_ConnectionLimitingUserIPAddress_Object=MibScalar
connectionLimitingUserIPAddress=_ConnectionLimitingUserIPAddress_Object((1,3,6,1,4,1,8744,5,18,1,2,3),_ConnectionLimitingUserIPAddress_Type())
connectionLimitingUserIPAddress.setMaxAccess(_I)
if mibBuilder.loadTexts:connectionLimitingUserIPAddress.setStatus(_B)
_ColubrisConnectionLimitingMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
colubrisConnectionLimitingMIBNotificationPrefix=_ColubrisConnectionLimitingMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,8744,5,18,2))
_ColubrisConnectionLimitingMIBNotifications_ObjectIdentity=ObjectIdentity
colubrisConnectionLimitingMIBNotifications=_ColubrisConnectionLimitingMIBNotifications_ObjectIdentity((1,3,6,1,4,1,8744,5,18,2,0))
_ColubrisConnectionLimitingMIBConformance_ObjectIdentity=ObjectIdentity
colubrisConnectionLimitingMIBConformance=_ColubrisConnectionLimitingMIBConformance_ObjectIdentity((1,3,6,1,4,1,8744,5,18,3))
_ColubrisConnectionLimitingMIBCompliances_ObjectIdentity=ObjectIdentity
colubrisConnectionLimitingMIBCompliances=_ColubrisConnectionLimitingMIBCompliances_ObjectIdentity((1,3,6,1,4,1,8744,5,18,3,1))
_ColubrisConnectionLimitingMIBGroups_ObjectIdentity=ObjectIdentity
colubrisConnectionLimitingMIBGroups=_ColubrisConnectionLimitingMIBGroups_ObjectIdentity((1,3,6,1,4,1,8744,5,18,3,2))
colubrisConnectionLimitingConfigMIBGroup=ObjectGroup((1,3,6,1,4,1,8744,5,18,3,2,1))
colubrisConnectionLimitingConfigMIBGroup.setObjects(*((_A,_C),(_A,_J)))
if mibBuilder.loadTexts:colubrisConnectionLimitingConfigMIBGroup.setStatus(_B)
colubrisConnectionLimitingInfoMIBGroup=ObjectGroup((1,3,6,1,4,1,8744,5,18,3,2,2))
colubrisConnectionLimitingInfoMIBGroup.setObjects(*((_A,_K),(_A,_D),(_A,_E)))
if mibBuilder.loadTexts:colubrisConnectionLimitingInfoMIBGroup.setStatus(_B)
connectionLimitingMaximumUserConnectionsReached=NotificationType((1,3,6,1,4,1,8744,5,18,2,0,1))
connectionLimitingMaximumUserConnectionsReached.setObjects(*((_A,_C),(_A,_D),(_A,_E)))
if mibBuilder.loadTexts:connectionLimitingMaximumUserConnectionsReached.setStatus(_B)
colubrisConnectionLimitingNotificationGroup=NotificationGroup((1,3,6,1,4,1,8744,5,18,3,2,3))
colubrisConnectionLimitingNotificationGroup.setObjects((_A,_L))
if mibBuilder.loadTexts:colubrisConnectionLimitingNotificationGroup.setStatus(_B)
colubrisConnectionLimitingMIBCompliance=ModuleCompliance((1,3,6,1,4,1,8744,5,18,3,1,1))
colubrisConnectionLimitingMIBCompliance.setObjects(*((_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:colubrisConnectionLimitingMIBCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'colubrisConnectionLimitingMIB':colubrisConnectionLimitingMIB,'colubrisConnectionLimitingMIBObjects':colubrisConnectionLimitingMIBObjects,'connectionLimitingConfig':connectionLimitingConfig,_C:connectionLimitingMaximumUserConnections,_J:connectionLimitingNotificationEnabled,'connectionLimitingInfo':connectionLimitingInfo,_K:connectionLimitingMaximumSystemConnections,_D:connectionLimitingUserMACAddress,_E:connectionLimitingUserIPAddress,'colubrisConnectionLimitingMIBNotificationPrefix':colubrisConnectionLimitingMIBNotificationPrefix,'colubrisConnectionLimitingMIBNotifications':colubrisConnectionLimitingMIBNotifications,_L:connectionLimitingMaximumUserConnectionsReached,'colubrisConnectionLimitingMIBConformance':colubrisConnectionLimitingMIBConformance,'colubrisConnectionLimitingMIBCompliances':colubrisConnectionLimitingMIBCompliances,'colubrisConnectionLimitingMIBCompliance':colubrisConnectionLimitingMIBCompliance,'colubrisConnectionLimitingMIBGroups':colubrisConnectionLimitingMIBGroups,_M:colubrisConnectionLimitingConfigMIBGroup,_N:colubrisConnectionLimitingInfoMIBGroup,_O:colubrisConnectionLimitingNotificationGroup})