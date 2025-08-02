_d='colubrisDeviceIfFdbMIBGroup'
_c='colubrisDeviceIfStatsMIBGroup'
_b='colubrisDeviceIfStatusMIBGroup'
_a='coDevIfFdbAgeing'
_Z='coDevIfFdbAuthorized'
_Y='coDevIfFdbMACAddress'
_X='coDevIfStsTxErrors'
_W='coDevIfStsTxPackets'
_V='coDevIfStsTxBytes'
_U='coDevIfStsRxErrors'
_T='coDevIfStsRxPackets'
_S='coDevIfStsRxBytes'
_R='coDevIfStaPowerForwardingStatus'
_Q='coDevIfStaState'
_P='coDevIfStaMACAddress'
_O='coDevIfStaNetworkMask'
_N='coDevIfStaIpAddress'
_M='coDevIfStaVLAN'
_L='coDevIfStaType'
_K='coDevIfStaFriendlyInterfaceName'
_J='coDeviceIfStatsEntry'
_I='coDevIfFdbMacIndex'
_H='not-accessible'
_G='coDevIfStaIfIndex'
_F='coDevDisIndex'
_E='COLUBRIS-DEVICE-MIB'
_D='Integer32'
_C='read-only'
_B='COLUBRIS-DEVICE-IF-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
coDevDisIndex,=mibBuilder.importSymbols(_E,_F)
colubrisMgmtV2,=mibBuilder.importSymbols('COLUBRIS-SMI','colubrisMgmtV2')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention','TruthValue')
colubrisDeviceIfMIB=ModuleIdentity((1,3,6,1,4,1,8744,5,24))
_ColubrisDeviceIfMIBObjects_ObjectIdentity=ObjectIdentity
colubrisDeviceIfMIBObjects=_ColubrisDeviceIfMIBObjects_ObjectIdentity((1,3,6,1,4,1,8744,5,24,1))
_CoDeviceIfStatusGroup_ObjectIdentity=ObjectIdentity
coDeviceIfStatusGroup=_CoDeviceIfStatusGroup_ObjectIdentity((1,3,6,1,4,1,8744,5,24,1,1))
_CoDeviceIfStatusTable_Object=MibTable
coDeviceIfStatusTable=_CoDeviceIfStatusTable_Object((1,3,6,1,4,1,8744,5,24,1,1,1))
if mibBuilder.loadTexts:coDeviceIfStatusTable.setStatus(_A)
_CoDeviceIfStatusEntry_Object=MibTableRow
coDeviceIfStatusEntry=_CoDeviceIfStatusEntry_Object((1,3,6,1,4,1,8744,5,24,1,1,1,1))
coDeviceIfStatusEntry.setIndexNames((0,_E,_F),(0,_B,_G))
if mibBuilder.loadTexts:coDeviceIfStatusEntry.setStatus(_A)
class _CoDevIfStaIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CoDevIfStaIfIndex_Type.__name__=_D
_CoDevIfStaIfIndex_Object=MibTableColumn
coDevIfStaIfIndex=_CoDevIfStaIfIndex_Object((1,3,6,1,4,1,8744,5,24,1,1,1,1,1),_CoDevIfStaIfIndex_Type())
coDevIfStaIfIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:coDevIfStaIfIndex.setStatus(_A)
_CoDevIfStaFriendlyInterfaceName_Type=DisplayString
_CoDevIfStaFriendlyInterfaceName_Object=MibTableColumn
coDevIfStaFriendlyInterfaceName=_CoDevIfStaFriendlyInterfaceName_Object((1,3,6,1,4,1,8744,5,24,1,1,1,1,2),_CoDevIfStaFriendlyInterfaceName_Type())
coDevIfStaFriendlyInterfaceName.setMaxAccess(_C)
if mibBuilder.loadTexts:coDevIfStaFriendlyInterfaceName.setStatus(_A)
class _CoDevIfStaType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('other',1),('ethernet',2),('l2vlan',3),('bridge',4),('ieee80211',5),('ieee80211Wds',6)))
_CoDevIfStaType_Type.__name__=_D
_CoDevIfStaType_Object=MibTableColumn
coDevIfStaType=_CoDevIfStaType_Object((1,3,6,1,4,1,8744,5,24,1,1,1,1,3),_CoDevIfStaType_Type())
coDevIfStaType.setMaxAccess(_C)
if mibBuilder.loadTexts:coDevIfStaType.setStatus(_A)
class _CoDevIfStaVLAN_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_CoDevIfStaVLAN_Type.__name__=_D
_CoDevIfStaVLAN_Object=MibTableColumn
coDevIfStaVLAN=_CoDevIfStaVLAN_Object((1,3,6,1,4,1,8744,5,24,1,1,1,1,4),_CoDevIfStaVLAN_Type())
coDevIfStaVLAN.setMaxAccess(_C)
if mibBuilder.loadTexts:coDevIfStaVLAN.setStatus(_A)
_CoDevIfStaIpAddress_Type=IpAddress
_CoDevIfStaIpAddress_Object=MibTableColumn
coDevIfStaIpAddress=_CoDevIfStaIpAddress_Object((1,3,6,1,4,1,8744,5,24,1,1,1,1,5),_CoDevIfStaIpAddress_Type())
coDevIfStaIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:coDevIfStaIpAddress.setStatus(_A)
_CoDevIfStaNetworkMask_Type=IpAddress
_CoDevIfStaNetworkMask_Object=MibTableColumn
coDevIfStaNetworkMask=_CoDevIfStaNetworkMask_Object((1,3,6,1,4,1,8744,5,24,1,1,1,1,6),_CoDevIfStaNetworkMask_Type())
coDevIfStaNetworkMask.setMaxAccess(_C)
if mibBuilder.loadTexts:coDevIfStaNetworkMask.setStatus(_A)
_CoDevIfStaMACAddress_Type=MacAddress
_CoDevIfStaMACAddress_Object=MibTableColumn
coDevIfStaMACAddress=_CoDevIfStaMACAddress_Object((1,3,6,1,4,1,8744,5,24,1,1,1,1,7),_CoDevIfStaMACAddress_Type())
coDevIfStaMACAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:coDevIfStaMACAddress.setStatus(_A)
class _CoDevIfStaState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_CoDevIfStaState_Type.__name__=_D
_CoDevIfStaState_Object=MibTableColumn
coDevIfStaState=_CoDevIfStaState_Object((1,3,6,1,4,1,8744,5,24,1,1,1,1,8),_CoDevIfStaState_Type())
coDevIfStaState.setMaxAccess(_C)
if mibBuilder.loadTexts:coDevIfStaState.setStatus(_A)
_CoDevIfStaPowerForwardingStatus_Type=TruthValue
_CoDevIfStaPowerForwardingStatus_Object=MibTableColumn
coDevIfStaPowerForwardingStatus=_CoDevIfStaPowerForwardingStatus_Object((1,3,6,1,4,1,8744,5,24,1,1,1,1,9),_CoDevIfStaPowerForwardingStatus_Type())
coDevIfStaPowerForwardingStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:coDevIfStaPowerForwardingStatus.setStatus(_A)
_CoDeviceIfStatsGroup_ObjectIdentity=ObjectIdentity
coDeviceIfStatsGroup=_CoDeviceIfStatsGroup_ObjectIdentity((1,3,6,1,4,1,8744,5,24,1,2))
_CoDeviceIfStatsTable_Object=MibTable
coDeviceIfStatsTable=_CoDeviceIfStatsTable_Object((1,3,6,1,4,1,8744,5,24,1,2,1))
if mibBuilder.loadTexts:coDeviceIfStatsTable.setStatus(_A)
_CoDeviceIfStatsEntry_Object=MibTableRow
coDeviceIfStatsEntry=_CoDeviceIfStatsEntry_Object((1,3,6,1,4,1,8744,5,24,1,2,1,1))
if mibBuilder.loadTexts:coDeviceIfStatsEntry.setStatus(_A)
_CoDevIfStsRxBytes_Type=Counter64
_CoDevIfStsRxBytes_Object=MibTableColumn
coDevIfStsRxBytes=_CoDevIfStsRxBytes_Object((1,3,6,1,4,1,8744,5,24,1,2,1,1,1),_CoDevIfStsRxBytes_Type())
coDevIfStsRxBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:coDevIfStsRxBytes.setStatus(_A)
_CoDevIfStsRxPackets_Type=Counter32
_CoDevIfStsRxPackets_Object=MibTableColumn
coDevIfStsRxPackets=_CoDevIfStsRxPackets_Object((1,3,6,1,4,1,8744,5,24,1,2,1,1,2),_CoDevIfStsRxPackets_Type())
coDevIfStsRxPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:coDevIfStsRxPackets.setStatus(_A)
_CoDevIfStsRxErrors_Type=Counter32
_CoDevIfStsRxErrors_Object=MibTableColumn
coDevIfStsRxErrors=_CoDevIfStsRxErrors_Object((1,3,6,1,4,1,8744,5,24,1,2,1,1,3),_CoDevIfStsRxErrors_Type())
coDevIfStsRxErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:coDevIfStsRxErrors.setStatus(_A)
_CoDevIfStsTxBytes_Type=Counter64
_CoDevIfStsTxBytes_Object=MibTableColumn
coDevIfStsTxBytes=_CoDevIfStsTxBytes_Object((1,3,6,1,4,1,8744,5,24,1,2,1,1,4),_CoDevIfStsTxBytes_Type())
coDevIfStsTxBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:coDevIfStsTxBytes.setStatus(_A)
_CoDevIfStsTxPackets_Type=Counter32
_CoDevIfStsTxPackets_Object=MibTableColumn
coDevIfStsTxPackets=_CoDevIfStsTxPackets_Object((1,3,6,1,4,1,8744,5,24,1,2,1,1,5),_CoDevIfStsTxPackets_Type())
coDevIfStsTxPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:coDevIfStsTxPackets.setStatus(_A)
_CoDevIfStsTxErrors_Type=Counter32
_CoDevIfStsTxErrors_Object=MibTableColumn
coDevIfStsTxErrors=_CoDevIfStsTxErrors_Object((1,3,6,1,4,1,8744,5,24,1,2,1,1,6),_CoDevIfStsTxErrors_Type())
coDevIfStsTxErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:coDevIfStsTxErrors.setStatus(_A)
_CoDeviceIfFdbGroup_ObjectIdentity=ObjectIdentity
coDeviceIfFdbGroup=_CoDeviceIfFdbGroup_ObjectIdentity((1,3,6,1,4,1,8744,5,24,1,3))
_CoDeviceIfFdbTable_Object=MibTable
coDeviceIfFdbTable=_CoDeviceIfFdbTable_Object((1,3,6,1,4,1,8744,5,24,1,3,1))
if mibBuilder.loadTexts:coDeviceIfFdbTable.setStatus(_A)
_CoDeviceIfFdbEntry_Object=MibTableRow
coDeviceIfFdbEntry=_CoDeviceIfFdbEntry_Object((1,3,6,1,4,1,8744,5,24,1,3,1,1))
coDeviceIfFdbEntry.setIndexNames((0,_E,_F),(0,_B,_G),(0,_B,_I))
if mibBuilder.loadTexts:coDeviceIfFdbEntry.setStatus(_A)
class _CoDevIfFdbMacIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CoDevIfFdbMacIndex_Type.__name__=_D
_CoDevIfFdbMacIndex_Object=MibTableColumn
coDevIfFdbMacIndex=_CoDevIfFdbMacIndex_Object((1,3,6,1,4,1,8744,5,24,1,3,1,1,1),_CoDevIfFdbMacIndex_Type())
coDevIfFdbMacIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:coDevIfFdbMacIndex.setStatus(_A)
_CoDevIfFdbMACAddress_Type=MacAddress
_CoDevIfFdbMACAddress_Object=MibTableColumn
coDevIfFdbMACAddress=_CoDevIfFdbMACAddress_Object((1,3,6,1,4,1,8744,5,24,1,3,1,1,2),_CoDevIfFdbMACAddress_Type())
coDevIfFdbMACAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:coDevIfFdbMACAddress.setStatus(_A)
_CoDevIfFdbAuthorized_Type=TruthValue
_CoDevIfFdbAuthorized_Object=MibTableColumn
coDevIfFdbAuthorized=_CoDevIfFdbAuthorized_Object((1,3,6,1,4,1,8744,5,24,1,3,1,1,3),_CoDevIfFdbAuthorized_Type())
coDevIfFdbAuthorized.setMaxAccess(_C)
if mibBuilder.loadTexts:coDevIfFdbAuthorized.setStatus(_A)
_CoDevIfFdbAgeing_Type=Integer32
_CoDevIfFdbAgeing_Object=MibTableColumn
coDevIfFdbAgeing=_CoDevIfFdbAgeing_Object((1,3,6,1,4,1,8744,5,24,1,3,1,1,4),_CoDevIfFdbAgeing_Type())
coDevIfFdbAgeing.setMaxAccess(_C)
if mibBuilder.loadTexts:coDevIfFdbAgeing.setStatus(_A)
if mibBuilder.loadTexts:coDevIfFdbAgeing.setUnits('msec')
_ColubrisDeviceIfMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
colubrisDeviceIfMIBNotificationPrefix=_ColubrisDeviceIfMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,8744,5,24,2))
_ColubrisDeviceIfMIBNotifications_ObjectIdentity=ObjectIdentity
colubrisDeviceIfMIBNotifications=_ColubrisDeviceIfMIBNotifications_ObjectIdentity((1,3,6,1,4,1,8744,5,24,2,0))
_ColubrisDeviceIfMIBConformance_ObjectIdentity=ObjectIdentity
colubrisDeviceIfMIBConformance=_ColubrisDeviceIfMIBConformance_ObjectIdentity((1,3,6,1,4,1,8744,5,24,3))
_ColubrisDeviceIfMIBCompliances_ObjectIdentity=ObjectIdentity
colubrisDeviceIfMIBCompliances=_ColubrisDeviceIfMIBCompliances_ObjectIdentity((1,3,6,1,4,1,8744,5,24,3,1))
_ColubrisDeviceIfMIBGroups_ObjectIdentity=ObjectIdentity
colubrisDeviceIfMIBGroups=_ColubrisDeviceIfMIBGroups_ObjectIdentity((1,3,6,1,4,1,8744,5,24,3,2))
coDeviceIfStatusEntry.registerAugmentions((_B,_J))
coDeviceIfStatsEntry.setIndexNames(*coDeviceIfStatusEntry.getIndexNames())
colubrisDeviceIfStatusMIBGroup=ObjectGroup((1,3,6,1,4,1,8744,5,24,3,2,1))
colubrisDeviceIfStatusMIBGroup.setObjects(*((_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:colubrisDeviceIfStatusMIBGroup.setStatus(_A)
colubrisDeviceIfStatsMIBGroup=ObjectGroup((1,3,6,1,4,1,8744,5,24,3,2,2))
colubrisDeviceIfStatsMIBGroup.setObjects(*((_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X)))
if mibBuilder.loadTexts:colubrisDeviceIfStatsMIBGroup.setStatus(_A)
colubrisDeviceIfFdbMIBGroup=ObjectGroup((1,3,6,1,4,1,8744,5,24,3,2,3))
colubrisDeviceIfFdbMIBGroup.setObjects(*((_B,_Y),(_B,_Z),(_B,_a)))
if mibBuilder.loadTexts:colubrisDeviceIfFdbMIBGroup.setStatus(_A)
colubrisDeviceIfMIBCompliance=ModuleCompliance((1,3,6,1,4,1,8744,5,24,3,1,1))
colubrisDeviceIfMIBCompliance.setObjects(*((_B,_b),(_B,_c),(_B,_d)))
if mibBuilder.loadTexts:colubrisDeviceIfMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'colubrisDeviceIfMIB':colubrisDeviceIfMIB,'colubrisDeviceIfMIBObjects':colubrisDeviceIfMIBObjects,'coDeviceIfStatusGroup':coDeviceIfStatusGroup,'coDeviceIfStatusTable':coDeviceIfStatusTable,'coDeviceIfStatusEntry':coDeviceIfStatusEntry,_G:coDevIfStaIfIndex,_K:coDevIfStaFriendlyInterfaceName,_L:coDevIfStaType,_M:coDevIfStaVLAN,_N:coDevIfStaIpAddress,_O:coDevIfStaNetworkMask,_P:coDevIfStaMACAddress,_Q:coDevIfStaState,_R:coDevIfStaPowerForwardingStatus,'coDeviceIfStatsGroup':coDeviceIfStatsGroup,'coDeviceIfStatsTable':coDeviceIfStatsTable,_J:coDeviceIfStatsEntry,_S:coDevIfStsRxBytes,_T:coDevIfStsRxPackets,_U:coDevIfStsRxErrors,_V:coDevIfStsTxBytes,_W:coDevIfStsTxPackets,_X:coDevIfStsTxErrors,'coDeviceIfFdbGroup':coDeviceIfFdbGroup,'coDeviceIfFdbTable':coDeviceIfFdbTable,'coDeviceIfFdbEntry':coDeviceIfFdbEntry,_I:coDevIfFdbMacIndex,_Y:coDevIfFdbMACAddress,_Z:coDevIfFdbAuthorized,_a:coDevIfFdbAgeing,'colubrisDeviceIfMIBNotificationPrefix':colubrisDeviceIfMIBNotificationPrefix,'colubrisDeviceIfMIBNotifications':colubrisDeviceIfMIBNotifications,'colubrisDeviceIfMIBConformance':colubrisDeviceIfMIBConformance,'colubrisDeviceIfMIBCompliances':colubrisDeviceIfMIBCompliances,'colubrisDeviceIfMIBCompliance':colubrisDeviceIfMIBCompliance,'colubrisDeviceIfMIBGroups':colubrisDeviceIfMIBGroups,_b:colubrisDeviceIfStatusMIBGroup,_c:colubrisDeviceIfStatsMIBGroup,_d:colubrisDeviceIfFdbMIBGroup})