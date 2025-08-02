_Q='colubrisControllerNotificationGroup'
_P='colubrisControllerMIBGroup'
_O='coControllerStateNotification'
_N='coControllerNbDisController'
_M='coControllerTeamName'
_L='coControllerTeamIpAddress'
_K='coControllerStateNotificationEnabled'
_J='coControllerDisIndex'
_I='ColubrisNotificationEnable'
_H='coControllerDisState'
_G='coControllerDisIpAddress'
_F='coControllerDisMacAddress'
_E='coControllerDisSerialNumber'
_D='Integer32'
_C='read-only'
_B='current'
_A='COLUBRIS-CONTROLLER-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
colubrisMgmtV2,=mibBuilder.importSymbols('COLUBRIS-SMI','colubrisMgmtV2')
ColubrisNotificationEnable,=mibBuilder.importSymbols('COLUBRIS-TC',_I)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
colubrisControllerMIB=ModuleIdentity((1,3,6,1,4,1,8744,5,27))
_ColubrisControllerMIBObjects_ObjectIdentity=ObjectIdentity
colubrisControllerMIBObjects=_ColubrisControllerMIBObjects_ObjectIdentity((1,3,6,1,4,1,8744,5,27,1))
_CoControllerConfigGroup_ObjectIdentity=ObjectIdentity
coControllerConfigGroup=_CoControllerConfigGroup_ObjectIdentity((1,3,6,1,4,1,8744,5,27,1,1))
class _CoControllerStateNotificationEnabled_Type(ColubrisNotificationEnable):defaultValue=2
_CoControllerStateNotificationEnabled_Type.__name__=_I
_CoControllerStateNotificationEnabled_Object=MibScalar
coControllerStateNotificationEnabled=_CoControllerStateNotificationEnabled_Object((1,3,6,1,4,1,8744,5,27,1,1,1),_CoControllerStateNotificationEnabled_Type())
coControllerStateNotificationEnabled.setMaxAccess('read-write')
if mibBuilder.loadTexts:coControllerStateNotificationEnabled.setStatus(_B)
_CoControllerTeamIpAddress_Type=IpAddress
_CoControllerTeamIpAddress_Object=MibScalar
coControllerTeamIpAddress=_CoControllerTeamIpAddress_Object((1,3,6,1,4,1,8744,5,27,1,1,2),_CoControllerTeamIpAddress_Type())
coControllerTeamIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:coControllerTeamIpAddress.setStatus(_B)
_CoControllerTeamName_Type=DisplayString
_CoControllerTeamName_Object=MibScalar
coControllerTeamName=_CoControllerTeamName_Object((1,3,6,1,4,1,8744,5,27,1,1,3),_CoControllerTeamName_Type())
coControllerTeamName.setMaxAccess(_C)
if mibBuilder.loadTexts:coControllerTeamName.setStatus(_B)
_CoControllerDiscoveryGroup_ObjectIdentity=ObjectIdentity
coControllerDiscoveryGroup=_CoControllerDiscoveryGroup_ObjectIdentity((1,3,6,1,4,1,8744,5,27,1,2))
_CoControllerNbDisController_Type=Unsigned32
_CoControllerNbDisController_Object=MibScalar
coControllerNbDisController=_CoControllerNbDisController_Object((1,3,6,1,4,1,8744,5,27,1,2,1),_CoControllerNbDisController_Type())
coControllerNbDisController.setMaxAccess(_C)
if mibBuilder.loadTexts:coControllerNbDisController.setStatus(_B)
_CoControllerDiscoveryTable_Object=MibTable
coControllerDiscoveryTable=_CoControllerDiscoveryTable_Object((1,3,6,1,4,1,8744,5,27,1,2,2))
if mibBuilder.loadTexts:coControllerDiscoveryTable.setStatus(_B)
_CoControllerDiscoveryEntry_Object=MibTableRow
coControllerDiscoveryEntry=_CoControllerDiscoveryEntry_Object((1,3,6,1,4,1,8744,5,27,1,2,2,1))
coControllerDiscoveryEntry.setIndexNames((0,_A,_J))
if mibBuilder.loadTexts:coControllerDiscoveryEntry.setStatus(_B)
class _CoControllerDisIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CoControllerDisIndex_Type.__name__=_D
_CoControllerDisIndex_Object=MibTableColumn
coControllerDisIndex=_CoControllerDisIndex_Object((1,3,6,1,4,1,8744,5,27,1,2,2,1,1),_CoControllerDisIndex_Type())
coControllerDisIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:coControllerDisIndex.setStatus(_B)
_CoControllerDisSerialNumber_Type=DisplayString
_CoControllerDisSerialNumber_Object=MibTableColumn
coControllerDisSerialNumber=_CoControllerDisSerialNumber_Object((1,3,6,1,4,1,8744,5,27,1,2,2,1,2),_CoControllerDisSerialNumber_Type())
coControllerDisSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:coControllerDisSerialNumber.setStatus(_B)
_CoControllerDisMacAddress_Type=MacAddress
_CoControllerDisMacAddress_Object=MibTableColumn
coControllerDisMacAddress=_CoControllerDisMacAddress_Object((1,3,6,1,4,1,8744,5,27,1,2,2,1,3),_CoControllerDisMacAddress_Type())
coControllerDisMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:coControllerDisMacAddress.setStatus(_B)
_CoControllerDisIpAddress_Type=IpAddress
_CoControllerDisIpAddress_Object=MibTableColumn
coControllerDisIpAddress=_CoControllerDisIpAddress_Object((1,3,6,1,4,1,8744,5,27,1,2,2,1,4),_CoControllerDisIpAddress_Type())
coControllerDisIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:coControllerDisIpAddress.setStatus(_B)
class _CoControllerDisState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('disconnected',1),('authorized',2),('join',3),('firmware',4),('security',5),('configuration',6),('running',7)))
_CoControllerDisState_Type.__name__=_D
_CoControllerDisState_Object=MibTableColumn
coControllerDisState=_CoControllerDisState_Object((1,3,6,1,4,1,8744,5,27,1,2,2,1,5),_CoControllerDisState_Type())
coControllerDisState.setMaxAccess(_C)
if mibBuilder.loadTexts:coControllerDisState.setStatus(_B)
_ColubrisControllerMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
colubrisControllerMIBNotificationPrefix=_ColubrisControllerMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,8744,5,27,2))
_ColubrisControllerMIBNotifications_ObjectIdentity=ObjectIdentity
colubrisControllerMIBNotifications=_ColubrisControllerMIBNotifications_ObjectIdentity((1,3,6,1,4,1,8744,5,27,2,0))
_ColubrisControllerMIBConformance_ObjectIdentity=ObjectIdentity
colubrisControllerMIBConformance=_ColubrisControllerMIBConformance_ObjectIdentity((1,3,6,1,4,1,8744,5,27,3))
_ColubrisControllerMIBCompliances_ObjectIdentity=ObjectIdentity
colubrisControllerMIBCompliances=_ColubrisControllerMIBCompliances_ObjectIdentity((1,3,6,1,4,1,8744,5,27,3,1))
_ColubrisControllerMIBGroups_ObjectIdentity=ObjectIdentity
colubrisControllerMIBGroups=_ColubrisControllerMIBGroups_ObjectIdentity((1,3,6,1,4,1,8744,5,27,3,2))
colubrisControllerMIBGroup=ObjectGroup((1,3,6,1,4,1,8744,5,27,3,2,1))
colubrisControllerMIBGroup.setObjects(*((_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_E),(_A,_F),(_A,_G),(_A,_H)))
if mibBuilder.loadTexts:colubrisControllerMIBGroup.setStatus(_B)
coControllerStateNotification=NotificationType((1,3,6,1,4,1,8744,5,27,2,0,1))
coControllerStateNotification.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H)))
if mibBuilder.loadTexts:coControllerStateNotification.setStatus(_B)
colubrisControllerNotificationGroup=NotificationGroup((1,3,6,1,4,1,8744,5,27,3,2,2))
colubrisControllerNotificationGroup.setObjects((_A,_O))
if mibBuilder.loadTexts:colubrisControllerNotificationGroup.setStatus(_B)
colubrisControllerMIBCompliance=ModuleCompliance((1,3,6,1,4,1,8744,5,27,3,1,1))
colubrisControllerMIBCompliance.setObjects(*((_A,_P),(_A,_Q)))
if mibBuilder.loadTexts:colubrisControllerMIBCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'colubrisControllerMIB':colubrisControllerMIB,'colubrisControllerMIBObjects':colubrisControllerMIBObjects,'coControllerConfigGroup':coControllerConfigGroup,_K:coControllerStateNotificationEnabled,_L:coControllerTeamIpAddress,_M:coControllerTeamName,'coControllerDiscoveryGroup':coControllerDiscoveryGroup,_N:coControllerNbDisController,'coControllerDiscoveryTable':coControllerDiscoveryTable,'coControllerDiscoveryEntry':coControllerDiscoveryEntry,_J:coControllerDisIndex,_E:coControllerDisSerialNumber,_F:coControllerDisMacAddress,_G:coControllerDisIpAddress,_H:coControllerDisState,'colubrisControllerMIBNotificationPrefix':colubrisControllerMIBNotificationPrefix,'colubrisControllerMIBNotifications':colubrisControllerMIBNotifications,_O:coControllerStateNotification,'colubrisControllerMIBConformance':colubrisControllerMIBConformance,'colubrisControllerMIBCompliances':colubrisControllerMIBCompliances,'colubrisControllerMIBCompliance':colubrisControllerMIBCompliance,'colubrisControllerMIBGroups':colubrisControllerMIBGroups,_P:colubrisControllerMIBGroup,_Q:colubrisControllerNotificationGroup})