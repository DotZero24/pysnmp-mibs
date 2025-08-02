_O='wwpL2CFTStatsProtocolNum'
_N='wwpL2CFTStatsVlanId'
_M='vlanbridge'
_L='stp-uplink-fast'
_K='marker-protocol'
_J='bridge-grp-addr'
_I='l28021x'
_H='wwpL2CFTProtocolNum'
_G='wwpL2CFTVlanId'
_F='wwpL2CFTunnelVlanId'
_E='read-write'
_D='WWP-L2-CF-TUNNEL-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
wwpModules,=mibBuilder.importSymbols('WWP-SMI','wwpModules')
wwpL2CFTunnelMIB=ModuleIdentity((1,3,6,1,4,1,6141,2,53))
if mibBuilder.loadTexts:wwpL2CFTunnelMIB.setRevisions(('2005-03-08 16:00',))
class VlanId(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_WwpL2CFTunnelMIBObjects_ObjectIdentity=ObjectIdentity
wwpL2CFTunnelMIBObjects=_WwpL2CFTunnelMIBObjects_ObjectIdentity((1,3,6,1,4,1,6141,2,53,1))
_WwpL2CFTunnel_ObjectIdentity=ObjectIdentity
wwpL2CFTunnel=_WwpL2CFTunnel_ObjectIdentity((1,3,6,1,4,1,6141,2,53,1,1))
_WwpL2CFTunnelTable_Object=MibTable
wwpL2CFTunnelTable=_WwpL2CFTunnelTable_Object((1,3,6,1,4,1,6141,2,53,1,1,1))
if mibBuilder.loadTexts:wwpL2CFTunnelTable.setStatus(_A)
_WwpL2CFTunnelEntry_Object=MibTableRow
wwpL2CFTunnelEntry=_WwpL2CFTunnelEntry_Object((1,3,6,1,4,1,6141,2,53,1,1,1,1))
wwpL2CFTunnelEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:wwpL2CFTunnelEntry.setStatus(_A)
_WwpL2CFTunnelVlanId_Type=VlanId
_WwpL2CFTunnelVlanId_Object=MibTableColumn
wwpL2CFTunnelVlanId=_WwpL2CFTunnelVlanId_Object((1,3,6,1,4,1,6141,2,53,1,1,1,1,1),_WwpL2CFTunnelVlanId_Type())
wwpL2CFTunnelVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpL2CFTunnelVlanId.setStatus(_A)
class _WwpL2CFTunnelOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('operActive',0),('operVlanNotExist',1),('operInvalidVlanPortTag',2),('operInvalidVlanNumPorts',3),('operInvalidCfg',4),('operDisabled',5)))
_WwpL2CFTunnelOperStatus_Type.__name__=_C
_WwpL2CFTunnelOperStatus_Object=MibTableColumn
wwpL2CFTunnelOperStatus=_WwpL2CFTunnelOperStatus_Object((1,3,6,1,4,1,6141,2,53,1,1,1,1,2),_WwpL2CFTunnelOperStatus_Type())
wwpL2CFTunnelOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpL2CFTunnelOperStatus.setStatus(_A)
class _WwpL2CFTunnelAdminStatus_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('disabled',0),('enabled',1)))
_WwpL2CFTunnelAdminStatus_Type.__name__=_C
_WwpL2CFTunnelAdminStatus_Object=MibTableColumn
wwpL2CFTunnelAdminStatus=_WwpL2CFTunnelAdminStatus_Object((1,3,6,1,4,1,6141,2,53,1,1,1,1,3),_WwpL2CFTunnelAdminStatus_Type())
wwpL2CFTunnelAdminStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpL2CFTunnelAdminStatus.setStatus(_A)
class _WwpL2CFTunnelPriority_Type(Integer32):defaultValue=6;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('p0',0),('p1',1),('p2',2),('p3',3),('p4',4),('p5',5),('p6',6),('p7',7)))
_WwpL2CFTunnelPriority_Type.__name__=_C
_WwpL2CFTunnelPriority_Object=MibTableColumn
wwpL2CFTunnelPriority=_WwpL2CFTunnelPriority_Object((1,3,6,1,4,1,6141,2,53,1,1,1,1,4),_WwpL2CFTunnelPriority_Type())
wwpL2CFTunnelPriority.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpL2CFTunnelPriority.setStatus(_A)
_WwpL2CFTunnelRowStatus_Type=RowStatus
_WwpL2CFTunnelRowStatus_Object=MibTableColumn
wwpL2CFTunnelRowStatus=_WwpL2CFTunnelRowStatus_Object((1,3,6,1,4,1,6141,2,53,1,1,1,1,5),_WwpL2CFTunnelRowStatus_Type())
wwpL2CFTunnelRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpL2CFTunnelRowStatus.setStatus(_A)
_WwpL2CFTProtocolTable_Object=MibTable
wwpL2CFTProtocolTable=_WwpL2CFTProtocolTable_Object((1,3,6,1,4,1,6141,2,53,1,1,2))
if mibBuilder.loadTexts:wwpL2CFTProtocolTable.setStatus(_A)
_WwpL2CFTProtocolEntry_Object=MibTableRow
wwpL2CFTProtocolEntry=_WwpL2CFTProtocolEntry_Object((1,3,6,1,4,1,6141,2,53,1,1,2,1))
wwpL2CFTProtocolEntry.setIndexNames((0,_D,_G),(0,_D,_H))
if mibBuilder.loadTexts:wwpL2CFTProtocolEntry.setStatus(_A)
_WwpL2CFTVlanId_Type=VlanId
_WwpL2CFTVlanId_Object=MibTableColumn
wwpL2CFTVlanId=_WwpL2CFTVlanId_Object((1,3,6,1,4,1,6141,2,53,1,1,2,1,1),_WwpL2CFTVlanId_Type())
wwpL2CFTVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpL2CFTVlanId.setStatus(_A)
class _WwpL2CFTProtocolNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)));namedValues=NamedValues(*((_I,1),(_J,2),('cdp',3),('dtp',4),('gvrp',5),('lacp',6),(_K,7),('oam',8),('pagp',9),('pvst',10),(_L,11),('udld',12),(_M,13),('vtp',14),('lldp',15)))
_WwpL2CFTProtocolNum_Type.__name__=_C
_WwpL2CFTProtocolNum_Object=MibTableColumn
wwpL2CFTProtocolNum=_WwpL2CFTProtocolNum_Object((1,3,6,1,4,1,6141,2,53,1,1,2,1,2),_WwpL2CFTProtocolNum_Type())
wwpL2CFTProtocolNum.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpL2CFTProtocolNum.setStatus(_A)
class _WwpL2CFTDispositionType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('discard',0),('peer',1),('tunnel',2)))
_WwpL2CFTDispositionType_Type.__name__=_C
_WwpL2CFTDispositionType_Object=MibTableColumn
wwpL2CFTDispositionType=_WwpL2CFTDispositionType_Object((1,3,6,1,4,1,6141,2,53,1,1,2,1,3),_WwpL2CFTDispositionType_Type())
wwpL2CFTDispositionType.setMaxAccess('read-create')
if mibBuilder.loadTexts:wwpL2CFTDispositionType.setStatus(_A)
_WwpL2CFTStatsTable_Object=MibTable
wwpL2CFTStatsTable=_WwpL2CFTStatsTable_Object((1,3,6,1,4,1,6141,2,53,1,1,3))
if mibBuilder.loadTexts:wwpL2CFTStatsTable.setStatus(_A)
_WwpL2CFTStatsEntry_Object=MibTableRow
wwpL2CFTStatsEntry=_WwpL2CFTStatsEntry_Object((1,3,6,1,4,1,6141,2,53,1,1,3,1))
wwpL2CFTStatsEntry.setIndexNames((0,_D,_N),(0,_D,_O))
if mibBuilder.loadTexts:wwpL2CFTStatsEntry.setStatus(_A)
_WwpL2CFTStatsVlanId_Type=VlanId
_WwpL2CFTStatsVlanId_Object=MibTableColumn
wwpL2CFTStatsVlanId=_WwpL2CFTStatsVlanId_Object((1,3,6,1,4,1,6141,2,53,1,1,3,1,1),_WwpL2CFTStatsVlanId_Type())
wwpL2CFTStatsVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpL2CFTStatsVlanId.setStatus(_A)
class _WwpL2CFTStatsProtocolNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14)));namedValues=NamedValues(*((_I,1),(_J,2),('cdp',3),('dtp',4),('gvrp',5),('lacp',6),(_K,7),('oam',8),('pagp',9),('pvst',10),(_L,11),('udld',12),(_M,13),('vtp',14)))
_WwpL2CFTStatsProtocolNum_Type.__name__=_C
_WwpL2CFTStatsProtocolNum_Object=MibTableColumn
wwpL2CFTStatsProtocolNum=_WwpL2CFTStatsProtocolNum_Object((1,3,6,1,4,1,6141,2,53,1,1,3,1,2),_WwpL2CFTStatsProtocolNum_Type())
wwpL2CFTStatsProtocolNum.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpL2CFTStatsProtocolNum.setStatus(_A)
_WwpL2CFTStatsPacketsRx_Type=Counter32
_WwpL2CFTStatsPacketsRx_Object=MibTableColumn
wwpL2CFTStatsPacketsRx=_WwpL2CFTStatsPacketsRx_Object((1,3,6,1,4,1,6141,2,53,1,1,3,1,3),_WwpL2CFTStatsPacketsRx_Type())
wwpL2CFTStatsPacketsRx.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpL2CFTStatsPacketsRx.setStatus(_A)
_WwpL2CFTStatsTunneledFrames_Type=Counter32
_WwpL2CFTStatsTunneledFrames_Object=MibTableColumn
wwpL2CFTStatsTunneledFrames=_WwpL2CFTStatsTunneledFrames_Object((1,3,6,1,4,1,6141,2,53,1,1,3,1,4),_WwpL2CFTStatsTunneledFrames_Type())
wwpL2CFTStatsTunneledFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpL2CFTStatsTunneledFrames.setStatus(_A)
_WwpL2CFTStatsDecodedFrames_Type=Counter32
_WwpL2CFTStatsDecodedFrames_Object=MibTableColumn
wwpL2CFTStatsDecodedFrames=_WwpL2CFTStatsDecodedFrames_Object((1,3,6,1,4,1,6141,2,53,1,1,3,1,5),_WwpL2CFTStatsDecodedFrames_Type())
wwpL2CFTStatsDecodedFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpL2CFTStatsDecodedFrames.setStatus(_A)
_WwpL2CFTStatsDecodedFailed_Type=Counter32
_WwpL2CFTStatsDecodedFailed_Object=MibTableColumn
wwpL2CFTStatsDecodedFailed=_WwpL2CFTStatsDecodedFailed_Object((1,3,6,1,4,1,6141,2,53,1,1,3,1,6),_WwpL2CFTStatsDecodedFailed_Type())
wwpL2CFTStatsDecodedFailed.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpL2CFTStatsDecodedFailed.setStatus(_A)
_WwpL2CFTStatsPeeredFrames_Type=Counter32
_WwpL2CFTStatsPeeredFrames_Object=MibTableColumn
wwpL2CFTStatsPeeredFrames=_WwpL2CFTStatsPeeredFrames_Object((1,3,6,1,4,1,6141,2,53,1,1,3,1,7),_WwpL2CFTStatsPeeredFrames_Type())
wwpL2CFTStatsPeeredFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpL2CFTStatsPeeredFrames.setStatus(_A)
_WwpL2CFTStatsDiscardFrames_Type=Counter32
_WwpL2CFTStatsDiscardFrames_Object=MibTableColumn
wwpL2CFTStatsDiscardFrames=_WwpL2CFTStatsDiscardFrames_Object((1,3,6,1,4,1,6141,2,53,1,1,3,1,8),_WwpL2CFTStatsDiscardFrames_Type())
wwpL2CFTStatsDiscardFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpL2CFTStatsDiscardFrames.setStatus(_A)
_WwpL2CFTStatsTunFrameSubPort_Type=Counter32
_WwpL2CFTStatsTunFrameSubPort_Object=MibTableColumn
wwpL2CFTStatsTunFrameSubPort=_WwpL2CFTStatsTunFrameSubPort_Object((1,3,6,1,4,1,6141,2,53,1,1,3,1,9),_WwpL2CFTStatsTunFrameSubPort_Type())
wwpL2CFTStatsTunFrameSubPort.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpL2CFTStatsTunFrameSubPort.setStatus(_A)
_WwpL2CFTGlobalStats_ObjectIdentity=ObjectIdentity
wwpL2CFTGlobalStats=_WwpL2CFTGlobalStats_ObjectIdentity((1,3,6,1,4,1,6141,2,53,1,1,4))
_WwpL2CFTGlobalStatsPacketsRx_Type=Counter32
_WwpL2CFTGlobalStatsPacketsRx_Object=MibScalar
wwpL2CFTGlobalStatsPacketsRx=_WwpL2CFTGlobalStatsPacketsRx_Object((1,3,6,1,4,1,6141,2,53,1,1,4,1),_WwpL2CFTGlobalStatsPacketsRx_Type())
wwpL2CFTGlobalStatsPacketsRx.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpL2CFTGlobalStatsPacketsRx.setStatus(_A)
_WwpL2CFTGlobalStatsTunneledFrames_Type=Counter32
_WwpL2CFTGlobalStatsTunneledFrames_Object=MibScalar
wwpL2CFTGlobalStatsTunneledFrames=_WwpL2CFTGlobalStatsTunneledFrames_Object((1,3,6,1,4,1,6141,2,53,1,1,4,2),_WwpL2CFTGlobalStatsTunneledFrames_Type())
wwpL2CFTGlobalStatsTunneledFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpL2CFTGlobalStatsTunneledFrames.setStatus(_A)
_WwpL2CFTGlobalStatsDecodedFrames_Type=Counter32
_WwpL2CFTGlobalStatsDecodedFrames_Object=MibScalar
wwpL2CFTGlobalStatsDecodedFrames=_WwpL2CFTGlobalStatsDecodedFrames_Object((1,3,6,1,4,1,6141,2,53,1,1,4,3),_WwpL2CFTGlobalStatsDecodedFrames_Type())
wwpL2CFTGlobalStatsDecodedFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpL2CFTGlobalStatsDecodedFrames.setStatus(_A)
_WwpL2CFTGlobalStatsDecodedFailed_Type=Counter32
_WwpL2CFTGlobalStatsDecodedFailed_Object=MibScalar
wwpL2CFTGlobalStatsDecodedFailed=_WwpL2CFTGlobalStatsDecodedFailed_Object((1,3,6,1,4,1,6141,2,53,1,1,4,4),_WwpL2CFTGlobalStatsDecodedFailed_Type())
wwpL2CFTGlobalStatsDecodedFailed.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpL2CFTGlobalStatsDecodedFailed.setStatus(_A)
_WwpL2CFTGlobalStatsPeeredFrames_Type=Counter32
_WwpL2CFTGlobalStatsPeeredFrames_Object=MibScalar
wwpL2CFTGlobalStatsPeeredFrames=_WwpL2CFTGlobalStatsPeeredFrames_Object((1,3,6,1,4,1,6141,2,53,1,1,4,5),_WwpL2CFTGlobalStatsPeeredFrames_Type())
wwpL2CFTGlobalStatsPeeredFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpL2CFTGlobalStatsPeeredFrames.setStatus(_A)
_WwpL2CFTGlobalStatsDiscardFrames_Type=Counter32
_WwpL2CFTGlobalStatsDiscardFrames_Object=MibScalar
wwpL2CFTGlobalStatsDiscardFrames=_WwpL2CFTGlobalStatsDiscardFrames_Object((1,3,6,1,4,1,6141,2,53,1,1,4,6),_WwpL2CFTGlobalStatsDiscardFrames_Type())
wwpL2CFTGlobalStatsDiscardFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpL2CFTGlobalStatsDiscardFrames.setStatus(_A)
_WwpL2CFTGlobalStatsTunFrameSubPort_Type=Counter32
_WwpL2CFTGlobalStatsTunFrameSubPort_Object=MibScalar
wwpL2CFTGlobalStatsTunFrameSubPort=_WwpL2CFTGlobalStatsTunFrameSubPort_Object((1,3,6,1,4,1,6141,2,53,1,1,4,7),_WwpL2CFTGlobalStatsTunFrameSubPort_Type())
wwpL2CFTGlobalStatsTunFrameSubPort.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpL2CFTGlobalStatsTunFrameSubPort.setStatus(_A)
class _WwpL2CFTResetStatCounters_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('none',0),('reset',1)))
_WwpL2CFTResetStatCounters_Type.__name__=_C
_WwpL2CFTResetStatCounters_Object=MibScalar
wwpL2CFTResetStatCounters=_WwpL2CFTResetStatCounters_Object((1,3,6,1,4,1,6141,2,53,1,1,5),_WwpL2CFTResetStatCounters_Type())
wwpL2CFTResetStatCounters.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpL2CFTResetStatCounters.setStatus(_A)
_WwpL2CFTunnelMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
wwpL2CFTunnelMIBNotificationPrefix=_WwpL2CFTunnelMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,6141,2,53,2))
_WwpL2CFTunnelMIBNotifications_ObjectIdentity=ObjectIdentity
wwpL2CFTunnelMIBNotifications=_WwpL2CFTunnelMIBNotifications_ObjectIdentity((1,3,6,1,4,1,6141,2,53,2,0))
_WwpL2CFTunnelMIBConformance_ObjectIdentity=ObjectIdentity
wwpL2CFTunnelMIBConformance=_WwpL2CFTunnelMIBConformance_ObjectIdentity((1,3,6,1,4,1,6141,2,53,3))
_WwpL2CFTunnelMIBCompliances_ObjectIdentity=ObjectIdentity
wwpL2CFTunnelMIBCompliances=_WwpL2CFTunnelMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6141,2,53,3,1))
_WwpL2CFTunnelMIBGroups_ObjectIdentity=ObjectIdentity
wwpL2CFTunnelMIBGroups=_WwpL2CFTunnelMIBGroups_ObjectIdentity((1,3,6,1,4,1,6141,2,53,3,2))
mibBuilder.exportSymbols(_D,**{'VlanId':VlanId,'wwpL2CFTunnelMIB':wwpL2CFTunnelMIB,'wwpL2CFTunnelMIBObjects':wwpL2CFTunnelMIBObjects,'wwpL2CFTunnel':wwpL2CFTunnel,'wwpL2CFTunnelTable':wwpL2CFTunnelTable,'wwpL2CFTunnelEntry':wwpL2CFTunnelEntry,_F:wwpL2CFTunnelVlanId,'wwpL2CFTunnelOperStatus':wwpL2CFTunnelOperStatus,'wwpL2CFTunnelAdminStatus':wwpL2CFTunnelAdminStatus,'wwpL2CFTunnelPriority':wwpL2CFTunnelPriority,'wwpL2CFTunnelRowStatus':wwpL2CFTunnelRowStatus,'wwpL2CFTProtocolTable':wwpL2CFTProtocolTable,'wwpL2CFTProtocolEntry':wwpL2CFTProtocolEntry,_G:wwpL2CFTVlanId,_H:wwpL2CFTProtocolNum,'wwpL2CFTDispositionType':wwpL2CFTDispositionType,'wwpL2CFTStatsTable':wwpL2CFTStatsTable,'wwpL2CFTStatsEntry':wwpL2CFTStatsEntry,_N:wwpL2CFTStatsVlanId,_O:wwpL2CFTStatsProtocolNum,'wwpL2CFTStatsPacketsRx':wwpL2CFTStatsPacketsRx,'wwpL2CFTStatsTunneledFrames':wwpL2CFTStatsTunneledFrames,'wwpL2CFTStatsDecodedFrames':wwpL2CFTStatsDecodedFrames,'wwpL2CFTStatsDecodedFailed':wwpL2CFTStatsDecodedFailed,'wwpL2CFTStatsPeeredFrames':wwpL2CFTStatsPeeredFrames,'wwpL2CFTStatsDiscardFrames':wwpL2CFTStatsDiscardFrames,'wwpL2CFTStatsTunFrameSubPort':wwpL2CFTStatsTunFrameSubPort,'wwpL2CFTGlobalStats':wwpL2CFTGlobalStats,'wwpL2CFTGlobalStatsPacketsRx':wwpL2CFTGlobalStatsPacketsRx,'wwpL2CFTGlobalStatsTunneledFrames':wwpL2CFTGlobalStatsTunneledFrames,'wwpL2CFTGlobalStatsDecodedFrames':wwpL2CFTGlobalStatsDecodedFrames,'wwpL2CFTGlobalStatsDecodedFailed':wwpL2CFTGlobalStatsDecodedFailed,'wwpL2CFTGlobalStatsPeeredFrames':wwpL2CFTGlobalStatsPeeredFrames,'wwpL2CFTGlobalStatsDiscardFrames':wwpL2CFTGlobalStatsDiscardFrames,'wwpL2CFTGlobalStatsTunFrameSubPort':wwpL2CFTGlobalStatsTunFrameSubPort,'wwpL2CFTResetStatCounters':wwpL2CFTResetStatCounters,'wwpL2CFTunnelMIBNotificationPrefix':wwpL2CFTunnelMIBNotificationPrefix,'wwpL2CFTunnelMIBNotifications':wwpL2CFTunnelMIBNotifications,'wwpL2CFTunnelMIBConformance':wwpL2CFTunnelMIBConformance,'wwpL2CFTunnelMIBCompliances':wwpL2CFTunnelMIBCompliances,'wwpL2CFTunnelMIBGroups':wwpL2CFTunnelMIBGroups})