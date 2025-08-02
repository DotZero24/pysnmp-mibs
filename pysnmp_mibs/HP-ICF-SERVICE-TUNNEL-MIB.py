_r='hpicfServiceTunnelGroup1'
_q='hpicfServiceScalarsGroup1'
_p='hpicfServiceTunnelNotificationGroup'
_o='hpicfServiceTunnelStatsGroup'
_n='hpicfServiceTunnelGroup'
_m='hpicfServiceScalarsStatsGroup'
_l='hpicfServiceScalarsGroup'
_k='hpicfServiceTunnelIfDown'
_j='hpicfServiceTunnelIfUp'
_i='hpicfServiceTunnelInterfaceTruncate'
_h='hpicfTotalIPv4TapServiceTunnels'
_g='hpicfMaxIPv4TapServiceTunnels'
_f='hpicfTotalIPv4InterceptServiceTunnels'
_e='hpicfMaxInterceptServiceTunnels'
_d='hpicfServiceTunnelStatsClear'
_c='hpicfServiceTunnelLastHeartbeatPacketTimestamp'
_b='hpicfServiceTunnelStatsTxHeartbeat'
_a='hpicfServiceTunnelStatsRxHeartbeat'
_Z='hpicfServiceTunnelStatsTxPackets'
_Y='hpicfServiceTunnelStatsRxPackets'
_X='hpicfServiceTunnelStatsScalarClear'
_W='hpicfServiceTunnelStatsUnknownSrcMac'
_V='hpicfServiceTunnelStatsTxMTUViolationDrop'
_U='hpicfServiceTunnelStatsRxFragmentDrops'
_T='hpicfServiceTunnelStatsRxInvalidKey'
_S='hpicfServiceTunnelStatsIfEntry'
_R='hpicfServiceTunnelIfEntry'
_Q='hpicfServiceTunnelEntry'
_P='read-write'
_O='hpicfServiceTunnelInterfaceStatus'
_N='hpicfServiceTunnelIfMTU'
_M='hpicfServiceTunnelName'
_L='hpicfServiceTunnelType'
_K='hpicfTotalIPv4ServiceTunnels'
_J='hpicfMaxIPv4ServiceTunnels'
_I='ifIndex'
_H='ifAlias'
_G='hpicfServiceTunnelInterfaceDownReason'
_F='read-create'
_E='Integer32'
_D='IF-MIB'
_C='read-only'
_B='current'
_A='HP-ICF-SERVICE-TUNNEL-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpSwitch,=mibBuilder.importSymbols('HP-ICF-OID','hpSwitch')
ifAlias,ifIndex=mibBuilder.importSymbols(_D,_H,_I)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
tunnelIfEntry,tunnelInetConfigEntry=mibBuilder.importSymbols('TUNNEL-MIB','tunnelIfEntry','tunnelInetConfigEntry')
hpicfServiceTunnel=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,5,1,100))
if mibBuilder.loadTexts:hpicfServiceTunnel.setRevisions(('2014-06-17 00:00','2013-06-13 00:00'))
_HpicfServiceTunnelNotifications_ObjectIdentity=ObjectIdentity
hpicfServiceTunnelNotifications=_HpicfServiceTunnelNotifications_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,100,0))
_HpicfServiceTunnelConfigurationObjects_ObjectIdentity=ObjectIdentity
hpicfServiceTunnelConfigurationObjects=_HpicfServiceTunnelConfigurationObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,100,1))
_HpicfServiceTunnelScalars_ObjectIdentity=ObjectIdentity
hpicfServiceTunnelScalars=_HpicfServiceTunnelScalars_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,100,1,1))
_HpicfMaxIPv4ServiceTunnels_Type=Unsigned32
_HpicfMaxIPv4ServiceTunnels_Object=MibScalar
hpicfMaxIPv4ServiceTunnels=_HpicfMaxIPv4ServiceTunnels_Object((1,3,6,1,4,1,11,2,14,11,5,1,100,1,1,1),_HpicfMaxIPv4ServiceTunnels_Type())
hpicfMaxIPv4ServiceTunnels.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfMaxIPv4ServiceTunnels.setStatus(_B)
_HpicfTotalIPv4ServiceTunnels_Type=Unsigned32
_HpicfTotalIPv4ServiceTunnels_Object=MibScalar
hpicfTotalIPv4ServiceTunnels=_HpicfTotalIPv4ServiceTunnels_Object((1,3,6,1,4,1,11,2,14,11,5,1,100,1,1,2),_HpicfTotalIPv4ServiceTunnels_Type())
hpicfTotalIPv4ServiceTunnels.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfTotalIPv4ServiceTunnels.setStatus(_B)
_HpicfMaxInterceptServiceTunnels_Type=Unsigned32
_HpicfMaxInterceptServiceTunnels_Object=MibScalar
hpicfMaxInterceptServiceTunnels=_HpicfMaxInterceptServiceTunnels_Object((1,3,6,1,4,1,11,2,14,11,5,1,100,1,1,3),_HpicfMaxInterceptServiceTunnels_Type())
hpicfMaxInterceptServiceTunnels.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfMaxInterceptServiceTunnels.setStatus(_B)
_HpicfTotalIPv4InterceptServiceTunnels_Type=Unsigned32
_HpicfTotalIPv4InterceptServiceTunnels_Object=MibScalar
hpicfTotalIPv4InterceptServiceTunnels=_HpicfTotalIPv4InterceptServiceTunnels_Object((1,3,6,1,4,1,11,2,14,11,5,1,100,1,1,4),_HpicfTotalIPv4InterceptServiceTunnels_Type())
hpicfTotalIPv4InterceptServiceTunnels.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfTotalIPv4InterceptServiceTunnels.setStatus(_B)
_HpicfMaxIPv4TapServiceTunnels_Type=Unsigned32
_HpicfMaxIPv4TapServiceTunnels_Object=MibScalar
hpicfMaxIPv4TapServiceTunnels=_HpicfMaxIPv4TapServiceTunnels_Object((1,3,6,1,4,1,11,2,14,11,5,1,100,1,1,5),_HpicfMaxIPv4TapServiceTunnels_Type())
hpicfMaxIPv4TapServiceTunnels.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfMaxIPv4TapServiceTunnels.setStatus(_B)
_HpicfTotalIPv4TapServiceTunnels_Type=Unsigned32
_HpicfTotalIPv4TapServiceTunnels_Object=MibScalar
hpicfTotalIPv4TapServiceTunnels=_HpicfTotalIPv4TapServiceTunnels_Object((1,3,6,1,4,1,11,2,14,11,5,1,100,1,1,6),_HpicfTotalIPv4TapServiceTunnels_Type())
hpicfTotalIPv4TapServiceTunnels.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfTotalIPv4TapServiceTunnels.setStatus(_B)
_HpicfServiceTunnelTable_Object=MibTable
hpicfServiceTunnelTable=_HpicfServiceTunnelTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,100,1,2))
if mibBuilder.loadTexts:hpicfServiceTunnelTable.setStatus(_B)
_HpicfServiceTunnelEntry_Object=MibTableRow
hpicfServiceTunnelEntry=_HpicfServiceTunnelEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,100,1,2,1))
if mibBuilder.loadTexts:hpicfServiceTunnelEntry.setStatus(_B)
class _HpicfServiceTunnelType_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('none',0),('intercept',1),('tap',2)))
_HpicfServiceTunnelType_Type.__name__=_E
_HpicfServiceTunnelType_Object=MibTableColumn
hpicfServiceTunnelType=_HpicfServiceTunnelType_Object((1,3,6,1,4,1,11,2,14,11,5,1,100,1,2,1,1),_HpicfServiceTunnelType_Type())
hpicfServiceTunnelType.setMaxAccess(_F)
if mibBuilder.loadTexts:hpicfServiceTunnelType.setStatus(_B)
_HpicfServiceTunnelName_Type=SnmpAdminString
_HpicfServiceTunnelName_Object=MibTableColumn
hpicfServiceTunnelName=_HpicfServiceTunnelName_Object((1,3,6,1,4,1,11,2,14,11,5,1,100,1,2,1,2),_HpicfServiceTunnelName_Type())
hpicfServiceTunnelName.setMaxAccess(_F)
if mibBuilder.loadTexts:hpicfServiceTunnelName.setStatus(_B)
_HpicfServiceTunnelIfTable_Object=MibTable
hpicfServiceTunnelIfTable=_HpicfServiceTunnelIfTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,100,1,3))
if mibBuilder.loadTexts:hpicfServiceTunnelIfTable.setStatus(_B)
_HpicfServiceTunnelIfEntry_Object=MibTableRow
hpicfServiceTunnelIfEntry=_HpicfServiceTunnelIfEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,100,1,3,1))
if mibBuilder.loadTexts:hpicfServiceTunnelIfEntry.setStatus(_B)
_HpicfServiceTunnelIfMTU_Type=Unsigned32
_HpicfServiceTunnelIfMTU_Object=MibTableColumn
hpicfServiceTunnelIfMTU=_HpicfServiceTunnelIfMTU_Object((1,3,6,1,4,1,11,2,14,11,5,1,100,1,3,1,1),_HpicfServiceTunnelIfMTU_Type())
hpicfServiceTunnelIfMTU.setMaxAccess(_F)
if mibBuilder.loadTexts:hpicfServiceTunnelIfMTU.setStatus(_B)
class _HpicfServiceTunnelInterfaceStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_HpicfServiceTunnelInterfaceStatus_Type.__name__=_E
_HpicfServiceTunnelInterfaceStatus_Object=MibTableColumn
hpicfServiceTunnelInterfaceStatus=_HpicfServiceTunnelInterfaceStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,100,1,3,1,2),_HpicfServiceTunnelInterfaceStatus_Type())
hpicfServiceTunnelInterfaceStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfServiceTunnelInterfaceStatus.setStatus(_B)
class _HpicfServiceTunnelInterfaceDownReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('notApplicable',0),('resourceUnavailable',1),('noRouteToDestination',2),('ifAdminDown',3)))
_HpicfServiceTunnelInterfaceDownReason_Type.__name__=_E
_HpicfServiceTunnelInterfaceDownReason_Object=MibTableColumn
hpicfServiceTunnelInterfaceDownReason=_HpicfServiceTunnelInterfaceDownReason_Object((1,3,6,1,4,1,11,2,14,11,5,1,100,1,3,1,3),_HpicfServiceTunnelInterfaceDownReason_Type())
hpicfServiceTunnelInterfaceDownReason.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfServiceTunnelInterfaceDownReason.setStatus(_B)
class _HpicfServiceTunnelInterfaceTruncate_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_HpicfServiceTunnelInterfaceTruncate_Type.__name__=_E
_HpicfServiceTunnelInterfaceTruncate_Object=MibTableColumn
hpicfServiceTunnelInterfaceTruncate=_HpicfServiceTunnelInterfaceTruncate_Object((1,3,6,1,4,1,11,2,14,11,5,1,100,1,3,1,4),_HpicfServiceTunnelInterfaceTruncate_Type())
hpicfServiceTunnelInterfaceTruncate.setMaxAccess(_P)
if mibBuilder.loadTexts:hpicfServiceTunnelInterfaceTruncate.setStatus(_B)
_HpicfServiceTunnelStatisticsObjects_ObjectIdentity=ObjectIdentity
hpicfServiceTunnelStatisticsObjects=_HpicfServiceTunnelStatisticsObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,100,2))
_HpicfServiceTunnelScalarStats_ObjectIdentity=ObjectIdentity
hpicfServiceTunnelScalarStats=_HpicfServiceTunnelScalarStats_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,100,2,1))
_HpicfServiceTunnelStatsRxInvalidKey_Type=Counter64
_HpicfServiceTunnelStatsRxInvalidKey_Object=MibScalar
hpicfServiceTunnelStatsRxInvalidKey=_HpicfServiceTunnelStatsRxInvalidKey_Object((1,3,6,1,4,1,11,2,14,11,5,1,100,2,1,1),_HpicfServiceTunnelStatsRxInvalidKey_Type())
hpicfServiceTunnelStatsRxInvalidKey.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfServiceTunnelStatsRxInvalidKey.setStatus(_B)
_HpicfServiceTunnelStatsRxFragmentDrops_Type=Counter64
_HpicfServiceTunnelStatsRxFragmentDrops_Object=MibScalar
hpicfServiceTunnelStatsRxFragmentDrops=_HpicfServiceTunnelStatsRxFragmentDrops_Object((1,3,6,1,4,1,11,2,14,11,5,1,100,2,1,2),_HpicfServiceTunnelStatsRxFragmentDrops_Type())
hpicfServiceTunnelStatsRxFragmentDrops.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfServiceTunnelStatsRxFragmentDrops.setStatus(_B)
_HpicfServiceTunnelStatsTxMTUViolationDrop_Type=Counter64
_HpicfServiceTunnelStatsTxMTUViolationDrop_Object=MibScalar
hpicfServiceTunnelStatsTxMTUViolationDrop=_HpicfServiceTunnelStatsTxMTUViolationDrop_Object((1,3,6,1,4,1,11,2,14,11,5,1,100,2,1,3),_HpicfServiceTunnelStatsTxMTUViolationDrop_Type())
hpicfServiceTunnelStatsTxMTUViolationDrop.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfServiceTunnelStatsTxMTUViolationDrop.setStatus(_B)
_HpicfServiceTunnelStatsUnknownSrcMac_Type=Counter64
_HpicfServiceTunnelStatsUnknownSrcMac_Object=MibScalar
hpicfServiceTunnelStatsUnknownSrcMac=_HpicfServiceTunnelStatsUnknownSrcMac_Object((1,3,6,1,4,1,11,2,14,11,5,1,100,2,1,4),_HpicfServiceTunnelStatsUnknownSrcMac_Type())
hpicfServiceTunnelStatsUnknownSrcMac.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfServiceTunnelStatsUnknownSrcMac.setStatus(_B)
_HpicfServiceTunnelStatsScalarClear_Type=TruthValue
_HpicfServiceTunnelStatsScalarClear_Object=MibScalar
hpicfServiceTunnelStatsScalarClear=_HpicfServiceTunnelStatsScalarClear_Object((1,3,6,1,4,1,11,2,14,11,5,1,100,2,1,5),_HpicfServiceTunnelStatsScalarClear_Type())
hpicfServiceTunnelStatsScalarClear.setMaxAccess(_P)
if mibBuilder.loadTexts:hpicfServiceTunnelStatsScalarClear.setStatus(_B)
_HpicfServiceTunnelStatsIfTable_Object=MibTable
hpicfServiceTunnelStatsIfTable=_HpicfServiceTunnelStatsIfTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,100,2,2))
if mibBuilder.loadTexts:hpicfServiceTunnelStatsIfTable.setStatus(_B)
_HpicfServiceTunnelStatsIfEntry_Object=MibTableRow
hpicfServiceTunnelStatsIfEntry=_HpicfServiceTunnelStatsIfEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,100,2,2,1))
if mibBuilder.loadTexts:hpicfServiceTunnelStatsIfEntry.setStatus(_B)
_HpicfServiceTunnelStatsRxPackets_Type=Counter64
_HpicfServiceTunnelStatsRxPackets_Object=MibTableColumn
hpicfServiceTunnelStatsRxPackets=_HpicfServiceTunnelStatsRxPackets_Object((1,3,6,1,4,1,11,2,14,11,5,1,100,2,2,1,1),_HpicfServiceTunnelStatsRxPackets_Type())
hpicfServiceTunnelStatsRxPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfServiceTunnelStatsRxPackets.setStatus(_B)
_HpicfServiceTunnelStatsTxPackets_Type=Counter64
_HpicfServiceTunnelStatsTxPackets_Object=MibTableColumn
hpicfServiceTunnelStatsTxPackets=_HpicfServiceTunnelStatsTxPackets_Object((1,3,6,1,4,1,11,2,14,11,5,1,100,2,2,1,2),_HpicfServiceTunnelStatsTxPackets_Type())
hpicfServiceTunnelStatsTxPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfServiceTunnelStatsTxPackets.setStatus(_B)
_HpicfServiceTunnelStatsRxHeartbeat_Type=Counter64
_HpicfServiceTunnelStatsRxHeartbeat_Object=MibTableColumn
hpicfServiceTunnelStatsRxHeartbeat=_HpicfServiceTunnelStatsRxHeartbeat_Object((1,3,6,1,4,1,11,2,14,11,5,1,100,2,2,1,3),_HpicfServiceTunnelStatsRxHeartbeat_Type())
hpicfServiceTunnelStatsRxHeartbeat.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfServiceTunnelStatsRxHeartbeat.setStatus(_B)
_HpicfServiceTunnelStatsTxHeartbeat_Type=Counter64
_HpicfServiceTunnelStatsTxHeartbeat_Object=MibTableColumn
hpicfServiceTunnelStatsTxHeartbeat=_HpicfServiceTunnelStatsTxHeartbeat_Object((1,3,6,1,4,1,11,2,14,11,5,1,100,2,2,1,4),_HpicfServiceTunnelStatsTxHeartbeat_Type())
hpicfServiceTunnelStatsTxHeartbeat.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfServiceTunnelStatsTxHeartbeat.setStatus(_B)
_HpicfServiceTunnelLastHeartbeatPacketTimestamp_Type=TimeTicks
_HpicfServiceTunnelLastHeartbeatPacketTimestamp_Object=MibTableColumn
hpicfServiceTunnelLastHeartbeatPacketTimestamp=_HpicfServiceTunnelLastHeartbeatPacketTimestamp_Object((1,3,6,1,4,1,11,2,14,11,5,1,100,2,2,1,5),_HpicfServiceTunnelLastHeartbeatPacketTimestamp_Type())
hpicfServiceTunnelLastHeartbeatPacketTimestamp.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfServiceTunnelLastHeartbeatPacketTimestamp.setStatus(_B)
_HpicfServiceTunnelStatsClear_Type=TruthValue
_HpicfServiceTunnelStatsClear_Object=MibTableColumn
hpicfServiceTunnelStatsClear=_HpicfServiceTunnelStatsClear_Object((1,3,6,1,4,1,11,2,14,11,5,1,100,2,2,1,6),_HpicfServiceTunnelStatsClear_Type())
hpicfServiceTunnelStatsClear.setMaxAccess(_F)
if mibBuilder.loadTexts:hpicfServiceTunnelStatsClear.setStatus(_B)
_HpicfServiceTunnelConformance_ObjectIdentity=ObjectIdentity
hpicfServiceTunnelConformance=_HpicfServiceTunnelConformance_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,100,3))
_HpicfServiceTunnelCompliances_ObjectIdentity=ObjectIdentity
hpicfServiceTunnelCompliances=_HpicfServiceTunnelCompliances_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,100,3,1))
_HpicfServiceTunnelGroups_ObjectIdentity=ObjectIdentity
hpicfServiceTunnelGroups=_HpicfServiceTunnelGroups_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,100,3,2))
tunnelInetConfigEntry.registerAugmentions((_A,_Q))
hpicfServiceTunnelEntry.setIndexNames(*tunnelInetConfigEntry.getIndexNames())
tunnelIfEntry.registerAugmentions((_A,_R))
hpicfServiceTunnelIfEntry.setIndexNames(*tunnelIfEntry.getIndexNames())
tunnelIfEntry.registerAugmentions((_A,_S))
hpicfServiceTunnelStatsIfEntry.setIndexNames(*tunnelIfEntry.getIndexNames())
hpicfServiceScalarsGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,100,3,2,1))
hpicfServiceScalarsGroup.setObjects(*((_A,_J),(_A,_K)))
if mibBuilder.loadTexts:hpicfServiceScalarsGroup.setStatus(_B)
hpicfServiceScalarsStatsGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,100,3,2,2))
hpicfServiceScalarsStatsGroup.setObjects(*((_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X)))
if mibBuilder.loadTexts:hpicfServiceScalarsStatsGroup.setStatus(_B)
hpicfServiceTunnelGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,100,3,2,3))
hpicfServiceTunnelGroup.setObjects(*((_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_G)))
if mibBuilder.loadTexts:hpicfServiceTunnelGroup.setStatus(_B)
hpicfServiceTunnelStatsGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,100,3,2,4))
hpicfServiceTunnelStatsGroup.setObjects(*((_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d)))
if mibBuilder.loadTexts:hpicfServiceTunnelStatsGroup.setStatus(_B)
hpicfServiceScalarsGroup1=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,100,3,2,6))
hpicfServiceScalarsGroup1.setObjects(*((_A,_J),(_A,_K),(_A,_e),(_A,_f),(_A,_g),(_A,_h)))
if mibBuilder.loadTexts:hpicfServiceScalarsGroup1.setStatus(_B)
hpicfServiceTunnelGroup1=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,100,3,2,7))
hpicfServiceTunnelGroup1.setObjects(*((_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_G),(_A,_i)))
if mibBuilder.loadTexts:hpicfServiceTunnelGroup1.setStatus(_B)
hpicfServiceTunnelIfUp=NotificationType((1,3,6,1,4,1,11,2,14,11,5,1,100,0,1))
hpicfServiceTunnelIfUp.setObjects(*((_D,_I),(_D,_H)))
if mibBuilder.loadTexts:hpicfServiceTunnelIfUp.setStatus(_B)
hpicfServiceTunnelIfDown=NotificationType((1,3,6,1,4,1,11,2,14,11,5,1,100,0,2))
hpicfServiceTunnelIfDown.setObjects(*((_D,_I),(_D,_H),(_A,_G)))
if mibBuilder.loadTexts:hpicfServiceTunnelIfDown.setStatus(_B)
hpicfServiceTunnelNotificationGroup=NotificationGroup((1,3,6,1,4,1,11,2,14,11,5,1,100,3,2,5))
hpicfServiceTunnelNotificationGroup.setObjects(*((_A,_j),(_A,_k)))
if mibBuilder.loadTexts:hpicfServiceTunnelNotificationGroup.setStatus(_B)
hpicfServiceTunnelCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,100,3,1,1))
hpicfServiceTunnelCompliance.setObjects(*((_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r)))
if mibBuilder.loadTexts:hpicfServiceTunnelCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'hpicfServiceTunnel':hpicfServiceTunnel,'hpicfServiceTunnelNotifications':hpicfServiceTunnelNotifications,_j:hpicfServiceTunnelIfUp,_k:hpicfServiceTunnelIfDown,'hpicfServiceTunnelConfigurationObjects':hpicfServiceTunnelConfigurationObjects,'hpicfServiceTunnelScalars':hpicfServiceTunnelScalars,_J:hpicfMaxIPv4ServiceTunnels,_K:hpicfTotalIPv4ServiceTunnels,_e:hpicfMaxInterceptServiceTunnels,_f:hpicfTotalIPv4InterceptServiceTunnels,_g:hpicfMaxIPv4TapServiceTunnels,_h:hpicfTotalIPv4TapServiceTunnels,'hpicfServiceTunnelTable':hpicfServiceTunnelTable,_Q:hpicfServiceTunnelEntry,_L:hpicfServiceTunnelType,_M:hpicfServiceTunnelName,'hpicfServiceTunnelIfTable':hpicfServiceTunnelIfTable,_R:hpicfServiceTunnelIfEntry,_N:hpicfServiceTunnelIfMTU,_O:hpicfServiceTunnelInterfaceStatus,_G:hpicfServiceTunnelInterfaceDownReason,_i:hpicfServiceTunnelInterfaceTruncate,'hpicfServiceTunnelStatisticsObjects':hpicfServiceTunnelStatisticsObjects,'hpicfServiceTunnelScalarStats':hpicfServiceTunnelScalarStats,_T:hpicfServiceTunnelStatsRxInvalidKey,_U:hpicfServiceTunnelStatsRxFragmentDrops,_V:hpicfServiceTunnelStatsTxMTUViolationDrop,_W:hpicfServiceTunnelStatsUnknownSrcMac,_X:hpicfServiceTunnelStatsScalarClear,'hpicfServiceTunnelStatsIfTable':hpicfServiceTunnelStatsIfTable,_S:hpicfServiceTunnelStatsIfEntry,_Y:hpicfServiceTunnelStatsRxPackets,_Z:hpicfServiceTunnelStatsTxPackets,_a:hpicfServiceTunnelStatsRxHeartbeat,_b:hpicfServiceTunnelStatsTxHeartbeat,_c:hpicfServiceTunnelLastHeartbeatPacketTimestamp,_d:hpicfServiceTunnelStatsClear,'hpicfServiceTunnelConformance':hpicfServiceTunnelConformance,'hpicfServiceTunnelCompliances':hpicfServiceTunnelCompliances,'hpicfServiceTunnelCompliance':hpicfServiceTunnelCompliance,'hpicfServiceTunnelGroups':hpicfServiceTunnelGroups,_l:hpicfServiceScalarsGroup,_m:hpicfServiceScalarsStatsGroup,_n:hpicfServiceTunnelGroup,_o:hpicfServiceTunnelStatsGroup,_p:hpicfServiceTunnelNotificationGroup,_q:hpicfServiceScalarsGroup1,_r:hpicfServiceTunnelGroup1})