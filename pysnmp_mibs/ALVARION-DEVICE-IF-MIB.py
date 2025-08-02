_W='alvarionDeviceIfStatsMIBGroup'
_V='alvarionDeviceIfStatusMIBGroup'
_U='coDevIfStsTxErrors'
_T='coDevIfStsTxPackets'
_S='coDevIfStsTxBytes'
_R='coDevIfStsRxErrors'
_Q='coDevIfStsRxPackets'
_P='coDevIfStsRxBytes'
_O='coDevIfStaState'
_N='coDevIfStaMACAddress'
_M='coDevIfStaNetworkMask'
_L='coDevIfStaIpAddress'
_K='coDevIfStaVLAN'
_J='coDevIfStaType'
_I='coDevIfStaFriendlyInterfaceName'
_H='coDeviceIfStatsEntry'
_G='coDevIfStaIfIndex'
_F='coDevDisIndex'
_E='ALVARION-DEVICE-MIB'
_D='Integer32'
_C='read-only'
_B='ALVARION-DEVICE-IF-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
coDevDisIndex,=mibBuilder.importSymbols(_E,_F)
alvarionMgmtV2,=mibBuilder.importSymbols('ALVARION-SMI','alvarionMgmtV2')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
alvarionDeviceIfMIB=ModuleIdentity((1,3,6,1,4,1,12394,1,10,5,24))
_AlvarionDeviceIfMIBObjects_ObjectIdentity=ObjectIdentity
alvarionDeviceIfMIBObjects=_AlvarionDeviceIfMIBObjects_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,24,1))
_CoDeviceIfStatusGroup_ObjectIdentity=ObjectIdentity
coDeviceIfStatusGroup=_CoDeviceIfStatusGroup_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,24,1,1))
_CoDeviceIfStatusTable_Object=MibTable
coDeviceIfStatusTable=_CoDeviceIfStatusTable_Object((1,3,6,1,4,1,12394,1,10,5,24,1,1,1))
if mibBuilder.loadTexts:coDeviceIfStatusTable.setStatus(_A)
_CoDeviceIfStatusEntry_Object=MibTableRow
coDeviceIfStatusEntry=_CoDeviceIfStatusEntry_Object((1,3,6,1,4,1,12394,1,10,5,24,1,1,1,1))
coDeviceIfStatusEntry.setIndexNames((0,_E,_F),(0,_B,_G))
if mibBuilder.loadTexts:coDeviceIfStatusEntry.setStatus(_A)
class _CoDevIfStaIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CoDevIfStaIfIndex_Type.__name__=_D
_CoDevIfStaIfIndex_Object=MibTableColumn
coDevIfStaIfIndex=_CoDevIfStaIfIndex_Object((1,3,6,1,4,1,12394,1,10,5,24,1,1,1,1,1),_CoDevIfStaIfIndex_Type())
coDevIfStaIfIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:coDevIfStaIfIndex.setStatus(_A)
_CoDevIfStaFriendlyInterfaceName_Type=DisplayString
_CoDevIfStaFriendlyInterfaceName_Object=MibTableColumn
coDevIfStaFriendlyInterfaceName=_CoDevIfStaFriendlyInterfaceName_Object((1,3,6,1,4,1,12394,1,10,5,24,1,1,1,1,2),_CoDevIfStaFriendlyInterfaceName_Type())
coDevIfStaFriendlyInterfaceName.setMaxAccess(_C)
if mibBuilder.loadTexts:coDevIfStaFriendlyInterfaceName.setStatus(_A)
class _CoDevIfStaType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('other',1),('ethernet',2),('l2vlan',3),('bridge',4),('ieee80211',5),('ieee80211Wds',6)))
_CoDevIfStaType_Type.__name__=_D
_CoDevIfStaType_Object=MibTableColumn
coDevIfStaType=_CoDevIfStaType_Object((1,3,6,1,4,1,12394,1,10,5,24,1,1,1,1,3),_CoDevIfStaType_Type())
coDevIfStaType.setMaxAccess(_C)
if mibBuilder.loadTexts:coDevIfStaType.setStatus(_A)
class _CoDevIfStaVLAN_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_CoDevIfStaVLAN_Type.__name__=_D
_CoDevIfStaVLAN_Object=MibTableColumn
coDevIfStaVLAN=_CoDevIfStaVLAN_Object((1,3,6,1,4,1,12394,1,10,5,24,1,1,1,1,4),_CoDevIfStaVLAN_Type())
coDevIfStaVLAN.setMaxAccess(_C)
if mibBuilder.loadTexts:coDevIfStaVLAN.setStatus(_A)
_CoDevIfStaIpAddress_Type=IpAddress
_CoDevIfStaIpAddress_Object=MibTableColumn
coDevIfStaIpAddress=_CoDevIfStaIpAddress_Object((1,3,6,1,4,1,12394,1,10,5,24,1,1,1,1,5),_CoDevIfStaIpAddress_Type())
coDevIfStaIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:coDevIfStaIpAddress.setStatus(_A)
_CoDevIfStaNetworkMask_Type=IpAddress
_CoDevIfStaNetworkMask_Object=MibTableColumn
coDevIfStaNetworkMask=_CoDevIfStaNetworkMask_Object((1,3,6,1,4,1,12394,1,10,5,24,1,1,1,1,6),_CoDevIfStaNetworkMask_Type())
coDevIfStaNetworkMask.setMaxAccess(_C)
if mibBuilder.loadTexts:coDevIfStaNetworkMask.setStatus(_A)
_CoDevIfStaMACAddress_Type=MacAddress
_CoDevIfStaMACAddress_Object=MibTableColumn
coDevIfStaMACAddress=_CoDevIfStaMACAddress_Object((1,3,6,1,4,1,12394,1,10,5,24,1,1,1,1,7),_CoDevIfStaMACAddress_Type())
coDevIfStaMACAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:coDevIfStaMACAddress.setStatus(_A)
class _CoDevIfStaState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_CoDevIfStaState_Type.__name__=_D
_CoDevIfStaState_Object=MibTableColumn
coDevIfStaState=_CoDevIfStaState_Object((1,3,6,1,4,1,12394,1,10,5,24,1,1,1,1,8),_CoDevIfStaState_Type())
coDevIfStaState.setMaxAccess(_C)
if mibBuilder.loadTexts:coDevIfStaState.setStatus(_A)
_CoDeviceIfStatsGroup_ObjectIdentity=ObjectIdentity
coDeviceIfStatsGroup=_CoDeviceIfStatsGroup_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,24,1,2))
_CoDeviceIfStatsTable_Object=MibTable
coDeviceIfStatsTable=_CoDeviceIfStatsTable_Object((1,3,6,1,4,1,12394,1,10,5,24,1,2,1))
if mibBuilder.loadTexts:coDeviceIfStatsTable.setStatus(_A)
_CoDeviceIfStatsEntry_Object=MibTableRow
coDeviceIfStatsEntry=_CoDeviceIfStatsEntry_Object((1,3,6,1,4,1,12394,1,10,5,24,1,2,1,1))
if mibBuilder.loadTexts:coDeviceIfStatsEntry.setStatus(_A)
_CoDevIfStsRxBytes_Type=Counter64
_CoDevIfStsRxBytes_Object=MibTableColumn
coDevIfStsRxBytes=_CoDevIfStsRxBytes_Object((1,3,6,1,4,1,12394,1,10,5,24,1,2,1,1,1),_CoDevIfStsRxBytes_Type())
coDevIfStsRxBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:coDevIfStsRxBytes.setStatus(_A)
_CoDevIfStsRxPackets_Type=Counter32
_CoDevIfStsRxPackets_Object=MibTableColumn
coDevIfStsRxPackets=_CoDevIfStsRxPackets_Object((1,3,6,1,4,1,12394,1,10,5,24,1,2,1,1,2),_CoDevIfStsRxPackets_Type())
coDevIfStsRxPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:coDevIfStsRxPackets.setStatus(_A)
_CoDevIfStsRxErrors_Type=Counter32
_CoDevIfStsRxErrors_Object=MibTableColumn
coDevIfStsRxErrors=_CoDevIfStsRxErrors_Object((1,3,6,1,4,1,12394,1,10,5,24,1,2,1,1,3),_CoDevIfStsRxErrors_Type())
coDevIfStsRxErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:coDevIfStsRxErrors.setStatus(_A)
_CoDevIfStsTxBytes_Type=Counter64
_CoDevIfStsTxBytes_Object=MibTableColumn
coDevIfStsTxBytes=_CoDevIfStsTxBytes_Object((1,3,6,1,4,1,12394,1,10,5,24,1,2,1,1,4),_CoDevIfStsTxBytes_Type())
coDevIfStsTxBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:coDevIfStsTxBytes.setStatus(_A)
_CoDevIfStsTxPackets_Type=Counter32
_CoDevIfStsTxPackets_Object=MibTableColumn
coDevIfStsTxPackets=_CoDevIfStsTxPackets_Object((1,3,6,1,4,1,12394,1,10,5,24,1,2,1,1,5),_CoDevIfStsTxPackets_Type())
coDevIfStsTxPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:coDevIfStsTxPackets.setStatus(_A)
_CoDevIfStsTxErrors_Type=Counter32
_CoDevIfStsTxErrors_Object=MibTableColumn
coDevIfStsTxErrors=_CoDevIfStsTxErrors_Object((1,3,6,1,4,1,12394,1,10,5,24,1,2,1,1,6),_CoDevIfStsTxErrors_Type())
coDevIfStsTxErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:coDevIfStsTxErrors.setStatus(_A)
_AlvarionDeviceIfMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
alvarionDeviceIfMIBNotificationPrefix=_AlvarionDeviceIfMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,24,2))
_AlvarionDeviceIfMIBNotifications_ObjectIdentity=ObjectIdentity
alvarionDeviceIfMIBNotifications=_AlvarionDeviceIfMIBNotifications_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,24,2,0))
_AlvarionDeviceIfMIBConformance_ObjectIdentity=ObjectIdentity
alvarionDeviceIfMIBConformance=_AlvarionDeviceIfMIBConformance_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,24,3))
_AlvarionDeviceIfMIBCompliances_ObjectIdentity=ObjectIdentity
alvarionDeviceIfMIBCompliances=_AlvarionDeviceIfMIBCompliances_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,24,3,1))
_AlvarionDeviceIfMIBGroups_ObjectIdentity=ObjectIdentity
alvarionDeviceIfMIBGroups=_AlvarionDeviceIfMIBGroups_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,24,3,2))
coDeviceIfStatusEntry.registerAugmentions((_B,_H))
coDeviceIfStatsEntry.setIndexNames(*coDeviceIfStatusEntry.getIndexNames())
alvarionDeviceIfStatusMIBGroup=ObjectGroup((1,3,6,1,4,1,12394,1,10,5,24,3,2,1))
alvarionDeviceIfStatusMIBGroup.setObjects(*((_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O)))
if mibBuilder.loadTexts:alvarionDeviceIfStatusMIBGroup.setStatus(_A)
alvarionDeviceIfStatsMIBGroup=ObjectGroup((1,3,6,1,4,1,12394,1,10,5,24,3,2,2))
alvarionDeviceIfStatsMIBGroup.setObjects(*((_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U)))
if mibBuilder.loadTexts:alvarionDeviceIfStatsMIBGroup.setStatus(_A)
alvarionDeviceIfMIBCompliance=ModuleCompliance((1,3,6,1,4,1,12394,1,10,5,24,3,1,1))
alvarionDeviceIfMIBCompliance.setObjects(*((_B,_V),(_B,_W)))
if mibBuilder.loadTexts:alvarionDeviceIfMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'alvarionDeviceIfMIB':alvarionDeviceIfMIB,'alvarionDeviceIfMIBObjects':alvarionDeviceIfMIBObjects,'coDeviceIfStatusGroup':coDeviceIfStatusGroup,'coDeviceIfStatusTable':coDeviceIfStatusTable,'coDeviceIfStatusEntry':coDeviceIfStatusEntry,_G:coDevIfStaIfIndex,_I:coDevIfStaFriendlyInterfaceName,_J:coDevIfStaType,_K:coDevIfStaVLAN,_L:coDevIfStaIpAddress,_M:coDevIfStaNetworkMask,_N:coDevIfStaMACAddress,_O:coDevIfStaState,'coDeviceIfStatsGroup':coDeviceIfStatsGroup,'coDeviceIfStatsTable':coDeviceIfStatsTable,_H:coDeviceIfStatsEntry,_P:coDevIfStsRxBytes,_Q:coDevIfStsRxPackets,_R:coDevIfStsRxErrors,_S:coDevIfStsTxBytes,_T:coDevIfStsTxPackets,_U:coDevIfStsTxErrors,'alvarionDeviceIfMIBNotificationPrefix':alvarionDeviceIfMIBNotificationPrefix,'alvarionDeviceIfMIBNotifications':alvarionDeviceIfMIBNotifications,'alvarionDeviceIfMIBConformance':alvarionDeviceIfMIBConformance,'alvarionDeviceIfMIBCompliances':alvarionDeviceIfMIBCompliances,'alvarionDeviceIfMIBCompliance':alvarionDeviceIfMIBCompliance,'alvarionDeviceIfMIBGroups':alvarionDeviceIfMIBGroups,_V:alvarionDeviceIfStatusMIBGroup,_W:alvarionDeviceIfStatsMIBGroup})