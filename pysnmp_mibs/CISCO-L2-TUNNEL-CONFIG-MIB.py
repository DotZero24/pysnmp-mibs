_v='cltcTunnelSysDropNotifGroup'
_u='cltcTunnelSysDropGroup'
_t='cltcTunnelSysDropNotifEnableGroup'
_s='cltcTunnelTotalDropGroup'
_r='cltcTunnelSysDropThresholdExceeded'
_q='cltcTunnelShutdownThresholdExceeded'
_p='cltcTunnelDropThresholdExceeded'
_o='cltcTunnelSysDropNotifEnable'
_n='cltcTunnelTotalDropStats'
_m='cltcNotificationEnable'
_l='cltcTunnelDropStats'
_k='cltcDot1qAllTaggedIfEnabled'
_j='cltcDot1qAllTaggedEnabled'
_i='cltcTunnelDeEncapStats'
_h='cltcTunnelEncapStats'
_g='cltcTunnelCos'
_f='cltcTunneledProtocolType'
_e='cltcDot1qTunnelMode'
_d='encapsulated PDUs'
_c='not-accessible'
_b='cltcTunnelThresholdProtocolIndex'
_a='cltcTunnelThresholdNotifsGroup'
_Z='cltcNotifsEnableGroup'
_Y='cltcTunnelSysDropThreshold'
_X='cltcTunnelShutdownThreshold'
_W='cltcTunnelDropThreshold'
_V='cltcTunneledProtocolIndex'
_U='lldp'
_T='eoam'
_S='stp'
_R='vtp'
_Q='cdp'
_P='PDUs/sec'
_O='Unsigned32'
_N='cltcTunnelDropStatisticsGroup'
_M='deprecated'
_L='read-only'
_K='Integer32'
_J='cltcDot1qAllTaggedGroup'
_I='cltcTunnelStatisticsGroup'
_H='cltcTunnelThresholdGroup'
_G='cltcTunneledProtocolGroup'
_F='cltcDot1qTunnelGroup'
_E='ifIndex'
_D='IF-MIB'
_C='read-write'
_B='current'
_A='CISCO-L2-TUNNEL-CONFIG-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
QosLayer2Cos,=mibBuilder.importSymbols('CISCO-QOS-PIB-MIB','QosLayer2Cos')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ifIndex,=mibBuilder.importSymbols(_D,_E)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_K,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_O,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
ciscoL2TunnelConfigMIB=ModuleIdentity((1,3,6,1,4,1,9,9,246))
if mibBuilder.loadTexts:ciscoL2TunnelConfigMIB.setRevisions(('2007-02-15 00:00','2006-07-25 00:00','2005-06-27 00:00','2004-06-09 00:00','2003-09-03 00:00','2002-05-31 10:00','2002-02-14 00:00'))
_CltcMIBObjects_ObjectIdentity=ObjectIdentity
cltcMIBObjects=_CltcMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,246,1))
_CltcGlobal_ObjectIdentity=ObjectIdentity
cltcGlobal=_CltcGlobal_ObjectIdentity((1,3,6,1,4,1,9,9,246,1,1))
_CltcTunnelCos_Type=QosLayer2Cos
_CltcTunnelCos_Object=MibScalar
cltcTunnelCos=_CltcTunnelCos_Object((1,3,6,1,4,1,9,9,246,1,1,1),_CltcTunnelCos_Type())
cltcTunnelCos.setMaxAccess(_C)
if mibBuilder.loadTexts:cltcTunnelCos.setStatus(_B)
_CltcNotificationEnable_Type=TruthValue
_CltcNotificationEnable_Object=MibScalar
cltcNotificationEnable=_CltcNotificationEnable_Object((1,3,6,1,4,1,9,9,246,1,1,2),_CltcNotificationEnable_Type())
cltcNotificationEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:cltcNotificationEnable.setStatus(_B)
_CltcTunnelSysDropThreshold_Type=Unsigned32
_CltcTunnelSysDropThreshold_Object=MibScalar
cltcTunnelSysDropThreshold=_CltcTunnelSysDropThreshold_Object((1,3,6,1,4,1,9,9,246,1,1,3),_CltcTunnelSysDropThreshold_Type())
cltcTunnelSysDropThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:cltcTunnelSysDropThreshold.setStatus(_B)
if mibBuilder.loadTexts:cltcTunnelSysDropThreshold.setUnits(_P)
_CltcTunnelSysDropNotifEnable_Type=TruthValue
_CltcTunnelSysDropNotifEnable_Object=MibScalar
cltcTunnelSysDropNotifEnable=_CltcTunnelSysDropNotifEnable_Object((1,3,6,1,4,1,9,9,246,1,1,4),_CltcTunnelSysDropNotifEnable_Type())
cltcTunnelSysDropNotifEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:cltcTunnelSysDropNotifEnable.setStatus(_B)
_CltcDot1qTunnel_ObjectIdentity=ObjectIdentity
cltcDot1qTunnel=_CltcDot1qTunnel_ObjectIdentity((1,3,6,1,4,1,9,9,246,1,2))
_CltcDot1qTunnelTable_Object=MibTable
cltcDot1qTunnelTable=_CltcDot1qTunnelTable_Object((1,3,6,1,4,1,9,9,246,1,2,1))
if mibBuilder.loadTexts:cltcDot1qTunnelTable.setStatus(_B)
_CltcDot1qTunnelEntry_Object=MibTableRow
cltcDot1qTunnelEntry=_CltcDot1qTunnelEntry_Object((1,3,6,1,4,1,9,9,246,1,2,1,1))
cltcDot1qTunnelEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:cltcDot1qTunnelEntry.setStatus(_B)
class _CltcDot1qTunnelMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_CltcDot1qTunnelMode_Type.__name__=_K
_CltcDot1qTunnelMode_Object=MibTableColumn
cltcDot1qTunnelMode=_CltcDot1qTunnelMode_Object((1,3,6,1,4,1,9,9,246,1,2,1,1,1),_CltcDot1qTunnelMode_Type())
cltcDot1qTunnelMode.setMaxAccess(_C)
if mibBuilder.loadTexts:cltcDot1qTunnelMode.setStatus(_B)
_CltcTunneledProtocol_ObjectIdentity=ObjectIdentity
cltcTunneledProtocol=_CltcTunneledProtocol_ObjectIdentity((1,3,6,1,4,1,9,9,246,1,3))
_CltcTunneledProtocolTable_Object=MibTable
cltcTunneledProtocolTable=_CltcTunneledProtocolTable_Object((1,3,6,1,4,1,9,9,246,1,3,1))
if mibBuilder.loadTexts:cltcTunneledProtocolTable.setStatus(_B)
_CltcTunneledProtocolEntry_Object=MibTableRow
cltcTunneledProtocolEntry=_CltcTunneledProtocolEntry_Object((1,3,6,1,4,1,9,9,246,1,3,1,1))
cltcTunneledProtocolEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:cltcTunneledProtocolEntry.setStatus(_B)
class _CltcTunneledProtocolType_Type(Bits):namedValues=NamedValues(*((_Q,0),(_R,1),(_S,2),(_T,3),(_U,4)))
_CltcTunneledProtocolType_Type.__name__='Bits'
_CltcTunneledProtocolType_Object=MibTableColumn
cltcTunneledProtocolType=_CltcTunneledProtocolType_Object((1,3,6,1,4,1,9,9,246,1,3,1,1,1),_CltcTunneledProtocolType_Type())
cltcTunneledProtocolType.setMaxAccess(_C)
if mibBuilder.loadTexts:cltcTunneledProtocolType.setStatus(_B)
_CltcTunnelThreshold_ObjectIdentity=ObjectIdentity
cltcTunnelThreshold=_CltcTunnelThreshold_ObjectIdentity((1,3,6,1,4,1,9,9,246,1,4))
_CltcTunnelThresholdTable_Object=MibTable
cltcTunnelThresholdTable=_CltcTunnelThresholdTable_Object((1,3,6,1,4,1,9,9,246,1,4,1))
if mibBuilder.loadTexts:cltcTunnelThresholdTable.setStatus(_B)
_CltcTunnelThresholdEntry_Object=MibTableRow
cltcTunnelThresholdEntry=_CltcTunnelThresholdEntry_Object((1,3,6,1,4,1,9,9,246,1,4,1,1))
cltcTunnelThresholdEntry.setIndexNames((0,_D,_E),(0,_A,_b))
if mibBuilder.loadTexts:cltcTunnelThresholdEntry.setStatus(_B)
class _CltcTunnelThresholdProtocolIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('all',1),(_Q,2),(_R,3),(_S,4),(_T,5),(_U,6)))
_CltcTunnelThresholdProtocolIndex_Type.__name__=_K
_CltcTunnelThresholdProtocolIndex_Object=MibTableColumn
cltcTunnelThresholdProtocolIndex=_CltcTunnelThresholdProtocolIndex_Object((1,3,6,1,4,1,9,9,246,1,4,1,1,1),_CltcTunnelThresholdProtocolIndex_Type())
cltcTunnelThresholdProtocolIndex.setMaxAccess(_c)
if mibBuilder.loadTexts:cltcTunnelThresholdProtocolIndex.setStatus(_B)
class _CltcTunnelDropThreshold_Type(Unsigned32):defaultValue=0
_CltcTunnelDropThreshold_Type.__name__=_O
_CltcTunnelDropThreshold_Object=MibTableColumn
cltcTunnelDropThreshold=_CltcTunnelDropThreshold_Object((1,3,6,1,4,1,9,9,246,1,4,1,1,2),_CltcTunnelDropThreshold_Type())
cltcTunnelDropThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:cltcTunnelDropThreshold.setStatus(_B)
if mibBuilder.loadTexts:cltcTunnelDropThreshold.setUnits(_P)
class _CltcTunnelShutdownThreshold_Type(Unsigned32):defaultValue=0
_CltcTunnelShutdownThreshold_Type.__name__=_O
_CltcTunnelShutdownThreshold_Object=MibTableColumn
cltcTunnelShutdownThreshold=_CltcTunnelShutdownThreshold_Object((1,3,6,1,4,1,9,9,246,1,4,1,1,3),_CltcTunnelShutdownThreshold_Type())
cltcTunnelShutdownThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:cltcTunnelShutdownThreshold.setStatus(_B)
if mibBuilder.loadTexts:cltcTunnelShutdownThreshold.setUnits(_P)
_CltcTunnelStatistics_ObjectIdentity=ObjectIdentity
cltcTunnelStatistics=_CltcTunnelStatistics_ObjectIdentity((1,3,6,1,4,1,9,9,246,1,5))
_CltcTunnelStatisticsTable_Object=MibTable
cltcTunnelStatisticsTable=_CltcTunnelStatisticsTable_Object((1,3,6,1,4,1,9,9,246,1,5,1))
if mibBuilder.loadTexts:cltcTunnelStatisticsTable.setStatus(_B)
_CltcTunnelStatisticsEntry_Object=MibTableRow
cltcTunnelStatisticsEntry=_CltcTunnelStatisticsEntry_Object((1,3,6,1,4,1,9,9,246,1,5,1,1))
cltcTunnelStatisticsEntry.setIndexNames((0,_D,_E),(0,_A,_V))
if mibBuilder.loadTexts:cltcTunnelStatisticsEntry.setStatus(_B)
class _CltcTunneledProtocolIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4,5,6)));namedValues=NamedValues(*((_Q,2),(_R,3),(_S,4),(_T,5),(_U,6)))
_CltcTunneledProtocolIndex_Type.__name__=_K
_CltcTunneledProtocolIndex_Object=MibTableColumn
cltcTunneledProtocolIndex=_CltcTunneledProtocolIndex_Object((1,3,6,1,4,1,9,9,246,1,5,1,1,1),_CltcTunneledProtocolIndex_Type())
cltcTunneledProtocolIndex.setMaxAccess(_c)
if mibBuilder.loadTexts:cltcTunneledProtocolIndex.setStatus(_B)
_CltcTunnelEncapStats_Type=Counter32
_CltcTunnelEncapStats_Object=MibTableColumn
cltcTunnelEncapStats=_CltcTunnelEncapStats_Object((1,3,6,1,4,1,9,9,246,1,5,1,1,2),_CltcTunnelEncapStats_Type())
cltcTunnelEncapStats.setMaxAccess(_L)
if mibBuilder.loadTexts:cltcTunnelEncapStats.setStatus(_B)
if mibBuilder.loadTexts:cltcTunnelEncapStats.setUnits(_d)
_CltcTunnelDeEncapStats_Type=Counter32
_CltcTunnelDeEncapStats_Object=MibTableColumn
cltcTunnelDeEncapStats=_CltcTunnelDeEncapStats_Object((1,3,6,1,4,1,9,9,246,1,5,1,1,3),_CltcTunnelDeEncapStats_Type())
cltcTunnelDeEncapStats.setMaxAccess(_L)
if mibBuilder.loadTexts:cltcTunnelDeEncapStats.setStatus(_B)
if mibBuilder.loadTexts:cltcTunnelDeEncapStats.setUnits('de-encapsulated PDUs')
_CltcTunnelDropStats_Type=Counter32
_CltcTunnelDropStats_Object=MibTableColumn
cltcTunnelDropStats=_CltcTunnelDropStats_Object((1,3,6,1,4,1,9,9,246,1,5,1,1,4),_CltcTunnelDropStats_Type())
cltcTunnelDropStats.setMaxAccess(_L)
if mibBuilder.loadTexts:cltcTunnelDropStats.setStatus(_B)
if mibBuilder.loadTexts:cltcTunnelDropStats.setUnits('PDUs')
_CltcTunnelDropStatTable_Object=MibTable
cltcTunnelDropStatTable=_CltcTunnelDropStatTable_Object((1,3,6,1,4,1,9,9,246,1,5,2))
if mibBuilder.loadTexts:cltcTunnelDropStatTable.setStatus(_B)
_CltcTunnelDropStatEntry_Object=MibTableRow
cltcTunnelDropStatEntry=_CltcTunnelDropStatEntry_Object((1,3,6,1,4,1,9,9,246,1,5,2,1))
cltcTunnelDropStatEntry.setIndexNames((0,_A,_V))
if mibBuilder.loadTexts:cltcTunnelDropStatEntry.setStatus(_B)
_CltcTunnelTotalDropStats_Type=Counter32
_CltcTunnelTotalDropStats_Object=MibTableColumn
cltcTunnelTotalDropStats=_CltcTunnelTotalDropStats_Object((1,3,6,1,4,1,9,9,246,1,5,2,1,1),_CltcTunnelTotalDropStats_Type())
cltcTunnelTotalDropStats.setMaxAccess(_L)
if mibBuilder.loadTexts:cltcTunnelTotalDropStats.setStatus(_B)
if mibBuilder.loadTexts:cltcTunnelTotalDropStats.setUnits(_d)
_CltcDot1qAllTagged_ObjectIdentity=ObjectIdentity
cltcDot1qAllTagged=_CltcDot1qAllTagged_ObjectIdentity((1,3,6,1,4,1,9,9,246,1,6))
_CltcDot1qAllTaggedEnabled_Type=TruthValue
_CltcDot1qAllTaggedEnabled_Object=MibScalar
cltcDot1qAllTaggedEnabled=_CltcDot1qAllTaggedEnabled_Object((1,3,6,1,4,1,9,9,246,1,6,1),_CltcDot1qAllTaggedEnabled_Type())
cltcDot1qAllTaggedEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:cltcDot1qAllTaggedEnabled.setStatus(_B)
_CltcDot1qAllTaggedIfTable_Object=MibTable
cltcDot1qAllTaggedIfTable=_CltcDot1qAllTaggedIfTable_Object((1,3,6,1,4,1,9,9,246,1,6,2))
if mibBuilder.loadTexts:cltcDot1qAllTaggedIfTable.setStatus(_B)
_CltcDot1qAllTaggedIfEntry_Object=MibTableRow
cltcDot1qAllTaggedIfEntry=_CltcDot1qAllTaggedIfEntry_Object((1,3,6,1,4,1,9,9,246,1,6,2,1))
cltcDot1qAllTaggedIfEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:cltcDot1qAllTaggedIfEntry.setStatus(_B)
_CltcDot1qAllTaggedIfEnabled_Type=TruthValue
_CltcDot1qAllTaggedIfEnabled_Object=MibTableColumn
cltcDot1qAllTaggedIfEnabled=_CltcDot1qAllTaggedIfEnabled_Object((1,3,6,1,4,1,9,9,246,1,6,2,1,1),_CltcDot1qAllTaggedIfEnabled_Type())
cltcDot1qAllTaggedIfEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:cltcDot1qAllTaggedIfEnabled.setStatus(_B)
_CltcMIBNotifications_ObjectIdentity=ObjectIdentity
cltcMIBNotifications=_CltcMIBNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,246,2))
_CltcMIBNotificationsPrefix_ObjectIdentity=ObjectIdentity
cltcMIBNotificationsPrefix=_CltcMIBNotificationsPrefix_ObjectIdentity((1,3,6,1,4,1,9,9,246,2,0))
_CltcMIBConformance_ObjectIdentity=ObjectIdentity
cltcMIBConformance=_CltcMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,246,3))
_CltcMIBCompliances_ObjectIdentity=ObjectIdentity
cltcMIBCompliances=_CltcMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,246,3,1))
_CltcMIBGroups_ObjectIdentity=ObjectIdentity
cltcMIBGroups=_CltcMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,246,3,2))
cltcDot1qTunnelGroup=ObjectGroup((1,3,6,1,4,1,9,9,246,3,2,1))
cltcDot1qTunnelGroup.setObjects((_A,_e))
if mibBuilder.loadTexts:cltcDot1qTunnelGroup.setStatus(_B)
cltcTunneledProtocolGroup=ObjectGroup((1,3,6,1,4,1,9,9,246,3,2,2))
cltcTunneledProtocolGroup.setObjects(*((_A,_f),(_A,_g)))
if mibBuilder.loadTexts:cltcTunneledProtocolGroup.setStatus(_B)
cltcTunnelThresholdGroup=ObjectGroup((1,3,6,1,4,1,9,9,246,3,2,3))
cltcTunnelThresholdGroup.setObjects(*((_A,_W),(_A,_X)))
if mibBuilder.loadTexts:cltcTunnelThresholdGroup.setStatus(_B)
cltcTunnelStatisticsGroup=ObjectGroup((1,3,6,1,4,1,9,9,246,3,2,4))
cltcTunnelStatisticsGroup.setObjects(*((_A,_h),(_A,_i)))
if mibBuilder.loadTexts:cltcTunnelStatisticsGroup.setStatus(_B)
cltcDot1qAllTaggedGroup=ObjectGroup((1,3,6,1,4,1,9,9,246,3,2,5))
cltcDot1qAllTaggedGroup.setObjects(*((_A,_j),(_A,_k)))
if mibBuilder.loadTexts:cltcDot1qAllTaggedGroup.setStatus(_B)
cltcTunnelDropStatisticsGroup=ObjectGroup((1,3,6,1,4,1,9,9,246,3,2,6))
cltcTunnelDropStatisticsGroup.setObjects((_A,_l))
if mibBuilder.loadTexts:cltcTunnelDropStatisticsGroup.setStatus(_B)
cltcNotifsEnableGroup=ObjectGroup((1,3,6,1,4,1,9,9,246,3,2,7))
cltcNotifsEnableGroup.setObjects((_A,_m))
if mibBuilder.loadTexts:cltcNotifsEnableGroup.setStatus(_B)
cltcTunnelTotalDropGroup=ObjectGroup((1,3,6,1,4,1,9,9,246,3,2,9))
cltcTunnelTotalDropGroup.setObjects((_A,_n))
if mibBuilder.loadTexts:cltcTunnelTotalDropGroup.setStatus(_B)
cltcTunnelSysDropNotifEnableGroup=ObjectGroup((1,3,6,1,4,1,9,9,246,3,2,10))
cltcTunnelSysDropNotifEnableGroup.setObjects((_A,_o))
if mibBuilder.loadTexts:cltcTunnelSysDropNotifEnableGroup.setStatus(_B)
cltcTunnelSysDropGroup=ObjectGroup((1,3,6,1,4,1,9,9,246,3,2,11))
cltcTunnelSysDropGroup.setObjects((_A,_Y))
if mibBuilder.loadTexts:cltcTunnelSysDropGroup.setStatus(_B)
cltcTunnelDropThresholdExceeded=NotificationType((1,3,6,1,4,1,9,9,246,2,0,1))
cltcTunnelDropThresholdExceeded.setObjects((_A,_W))
if mibBuilder.loadTexts:cltcTunnelDropThresholdExceeded.setStatus(_B)
cltcTunnelShutdownThresholdExceeded=NotificationType((1,3,6,1,4,1,9,9,246,2,0,2))
cltcTunnelShutdownThresholdExceeded.setObjects((_A,_X))
if mibBuilder.loadTexts:cltcTunnelShutdownThresholdExceeded.setStatus(_B)
cltcTunnelSysDropThresholdExceeded=NotificationType((1,3,6,1,4,1,9,9,246,2,0,3))
cltcTunnelSysDropThresholdExceeded.setObjects((_A,_Y))
if mibBuilder.loadTexts:cltcTunnelSysDropThresholdExceeded.setStatus(_B)
cltcTunnelThresholdNotifsGroup=NotificationGroup((1,3,6,1,4,1,9,9,246,3,2,8))
cltcTunnelThresholdNotifsGroup.setObjects(*((_A,_p),(_A,_q)))
if mibBuilder.loadTexts:cltcTunnelThresholdNotifsGroup.setStatus(_B)
cltcTunnelSysDropNotifGroup=NotificationGroup((1,3,6,1,4,1,9,9,246,3,2,12))
cltcTunnelSysDropNotifGroup.setObjects((_A,_r))
if mibBuilder.loadTexts:cltcTunnelSysDropNotifGroup.setStatus(_B)
cltcMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,246,3,1,1))
cltcMIBCompliance.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I)))
if mibBuilder.loadTexts:cltcMIBCompliance.setStatus(_M)
cltcMIBCompliance2=ModuleCompliance((1,3,6,1,4,1,9,9,246,3,1,2))
cltcMIBCompliance2.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:cltcMIBCompliance2.setStatus(_M)
cltcMIBCompliance3=ModuleCompliance((1,3,6,1,4,1,9,9,246,3,1,3))
cltcMIBCompliance3.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_N)))
if mibBuilder.loadTexts:cltcMIBCompliance3.setStatus(_M)
cltcMIBCompliance4=ModuleCompliance((1,3,6,1,4,1,9,9,246,3,1,4))
cltcMIBCompliance4.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_N),(_A,_Z),(_A,_a)))
if mibBuilder.loadTexts:cltcMIBCompliance4.setStatus(_M)
cltcMIBCompliance5=ModuleCompliance((1,3,6,1,4,1,9,9,246,3,1,5))
cltcMIBCompliance5.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_N),(_A,_s),(_A,_Z),(_A,_a),(_A,_t),(_A,_u),(_A,_v)))
if mibBuilder.loadTexts:cltcMIBCompliance5.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ciscoL2TunnelConfigMIB':ciscoL2TunnelConfigMIB,'cltcMIBObjects':cltcMIBObjects,'cltcGlobal':cltcGlobal,_g:cltcTunnelCos,_m:cltcNotificationEnable,_Y:cltcTunnelSysDropThreshold,_o:cltcTunnelSysDropNotifEnable,'cltcDot1qTunnel':cltcDot1qTunnel,'cltcDot1qTunnelTable':cltcDot1qTunnelTable,'cltcDot1qTunnelEntry':cltcDot1qTunnelEntry,_e:cltcDot1qTunnelMode,'cltcTunneledProtocol':cltcTunneledProtocol,'cltcTunneledProtocolTable':cltcTunneledProtocolTable,'cltcTunneledProtocolEntry':cltcTunneledProtocolEntry,_f:cltcTunneledProtocolType,'cltcTunnelThreshold':cltcTunnelThreshold,'cltcTunnelThresholdTable':cltcTunnelThresholdTable,'cltcTunnelThresholdEntry':cltcTunnelThresholdEntry,_b:cltcTunnelThresholdProtocolIndex,_W:cltcTunnelDropThreshold,_X:cltcTunnelShutdownThreshold,'cltcTunnelStatistics':cltcTunnelStatistics,'cltcTunnelStatisticsTable':cltcTunnelStatisticsTable,'cltcTunnelStatisticsEntry':cltcTunnelStatisticsEntry,_V:cltcTunneledProtocolIndex,_h:cltcTunnelEncapStats,_i:cltcTunnelDeEncapStats,_l:cltcTunnelDropStats,'cltcTunnelDropStatTable':cltcTunnelDropStatTable,'cltcTunnelDropStatEntry':cltcTunnelDropStatEntry,_n:cltcTunnelTotalDropStats,'cltcDot1qAllTagged':cltcDot1qAllTagged,_j:cltcDot1qAllTaggedEnabled,'cltcDot1qAllTaggedIfTable':cltcDot1qAllTaggedIfTable,'cltcDot1qAllTaggedIfEntry':cltcDot1qAllTaggedIfEntry,_k:cltcDot1qAllTaggedIfEnabled,'cltcMIBNotifications':cltcMIBNotifications,'cltcMIBNotificationsPrefix':cltcMIBNotificationsPrefix,_p:cltcTunnelDropThresholdExceeded,_q:cltcTunnelShutdownThresholdExceeded,_r:cltcTunnelSysDropThresholdExceeded,'cltcMIBConformance':cltcMIBConformance,'cltcMIBCompliances':cltcMIBCompliances,'cltcMIBCompliance':cltcMIBCompliance,'cltcMIBCompliance2':cltcMIBCompliance2,'cltcMIBCompliance3':cltcMIBCompliance3,'cltcMIBCompliance4':cltcMIBCompliance4,'cltcMIBCompliance5':cltcMIBCompliance5,'cltcMIBGroups':cltcMIBGroups,_F:cltcDot1qTunnelGroup,_G:cltcTunneledProtocolGroup,_H:cltcTunnelThresholdGroup,_I:cltcTunnelStatisticsGroup,_J:cltcDot1qAllTaggedGroup,_N:cltcTunnelDropStatisticsGroup,_Z:cltcNotifsEnableGroup,_a:cltcTunnelThresholdNotifsGroup,_s:cltcTunnelTotalDropGroup,_t:cltcTunnelSysDropNotifEnableGroup,_u:cltcTunnelSysDropGroup,_v:cltcTunnelSysDropNotifGroup})