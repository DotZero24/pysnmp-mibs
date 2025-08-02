_W='altigaStatsLBSSFGroup'
_V='alLBSSFPeerJoinTime'
_U='alLBSSFPeerActiveSessions'
_T='alLBSSFPeerPriority'
_S='alLBSSFPeerLoad'
_R='alLBSSFPeerDeviceType'
_Q='alLBSSFPeerRole'
_P='alLBSSFPeerFaultZone'
_O='alLBSSFPeerActive'
_N='alLBSSFPeerMappedPubIpAddress'
_M='alLBSSFPeerPubIpAddress'
_L='alLBSSFPeerRowStatus'
_K='alLBSSFLoad'
_J='alLBSSFNumberOfPeers'
_I='alLBSSFActive'
_H='alLBSSFDeviceType'
_G='alLBSSFRole'
_F='alLBSSFPeerPrivIpAddress'
_E='Integer32'
_D='Gauge32'
_C='read-only'
_B='ALTIGA-LBSSF-STATS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
alLBSSFMibModule,=mibBuilder.importSymbols('ALTIGA-GLOBAL-REG','alLBSSFMibModule')
alLBSSFGroup,alStatsLBSSF=mibBuilder.importSymbols('ALTIGA-MIB','alLBSSFGroup','alStatsLBSSF')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64',_D,_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
altigaLBSSFStatsMibModule=ModuleIdentity((1,3,6,1,4,1,3076,1,1,41,2))
if mibBuilder.loadTexts:altigaLBSSFStatsMibModule.setRevisions(('2002-09-05 13:00','2002-07-10 00:00'))
class DeviceType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3,4,5,6,7,8)));namedValues=NamedValues(*(('unknown',1),('vpn3005',3),('vpn3015',4),('vpn3030',5),('vpn3060',6),('vpn3080',7),('vpn3002',8)))
class DeviceRole(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('virtualMaster',1),('slave',2)))
_AltigaLBSSFStatsMibConformance_ObjectIdentity=ObjectIdentity
altigaLBSSFStatsMibConformance=_AltigaLBSSFStatsMibConformance_ObjectIdentity((1,3,6,1,4,1,3076,1,1,41,2,1))
_AltigaLBSSFStatsMibCompliances_ObjectIdentity=ObjectIdentity
altigaLBSSFStatsMibCompliances=_AltigaLBSSFStatsMibCompliances_ObjectIdentity((1,3,6,1,4,1,3076,1,1,41,2,1,1))
_AlStatsLBSSFGlobal_ObjectIdentity=ObjectIdentity
alStatsLBSSFGlobal=_AlStatsLBSSFGlobal_ObjectIdentity((1,3,6,1,4,1,3076,2,1,2,36,1))
_AlLBSSFRole_Type=DeviceRole
_AlLBSSFRole_Object=MibScalar
alLBSSFRole=_AlLBSSFRole_Object((1,3,6,1,4,1,3076,2,1,2,36,1,1),_AlLBSSFRole_Type())
alLBSSFRole.setMaxAccess(_C)
if mibBuilder.loadTexts:alLBSSFRole.setStatus(_A)
_AlLBSSFDeviceType_Type=DeviceType
_AlLBSSFDeviceType_Object=MibScalar
alLBSSFDeviceType=_AlLBSSFDeviceType_Object((1,3,6,1,4,1,3076,2,1,2,36,1,2),_AlLBSSFDeviceType_Type())
alLBSSFDeviceType.setMaxAccess(_C)
if mibBuilder.loadTexts:alLBSSFDeviceType.setStatus(_A)
_AlLBSSFActive_Type=TruthValue
_AlLBSSFActive_Object=MibScalar
alLBSSFActive=_AlLBSSFActive_Object((1,3,6,1,4,1,3076,2,1,2,36,1,3),_AlLBSSFActive_Type())
alLBSSFActive.setMaxAccess(_C)
if mibBuilder.loadTexts:alLBSSFActive.setStatus(_A)
class _AlLBSSFNumberOfPeers_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,25))
_AlLBSSFNumberOfPeers_Type.__name__=_D
_AlLBSSFNumberOfPeers_Object=MibScalar
alLBSSFNumberOfPeers=_AlLBSSFNumberOfPeers_Object((1,3,6,1,4,1,3076,2,1,2,36,1,4),_AlLBSSFNumberOfPeers_Type())
alLBSSFNumberOfPeers.setMaxAccess(_C)
if mibBuilder.loadTexts:alLBSSFNumberOfPeers.setStatus(_A)
class _AlLBSSFLoad_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_AlLBSSFLoad_Type.__name__=_D
_AlLBSSFLoad_Object=MibScalar
alLBSSFLoad=_AlLBSSFLoad_Object((1,3,6,1,4,1,3076,2,1,2,36,1,5),_AlLBSSFLoad_Type())
alLBSSFLoad.setMaxAccess(_C)
if mibBuilder.loadTexts:alLBSSFLoad.setStatus(_A)
_AlLBSSFPeerTable_Object=MibTable
alLBSSFPeerTable=_AlLBSSFPeerTable_Object((1,3,6,1,4,1,3076,2,1,2,36,2))
if mibBuilder.loadTexts:alLBSSFPeerTable.setStatus(_A)
_AlLBSSFPeerEntry_Object=MibTableRow
alLBSSFPeerEntry=_AlLBSSFPeerEntry_Object((1,3,6,1,4,1,3076,2,1,2,36,2,1))
alLBSSFPeerEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:alLBSSFPeerEntry.setStatus(_A)
_AlLBSSFPeerRowStatus_Type=RowStatus
_AlLBSSFPeerRowStatus_Object=MibTableColumn
alLBSSFPeerRowStatus=_AlLBSSFPeerRowStatus_Object((1,3,6,1,4,1,3076,2,1,2,36,2,1,1),_AlLBSSFPeerRowStatus_Type())
alLBSSFPeerRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:alLBSSFPeerRowStatus.setStatus(_A)
_AlLBSSFPeerPrivIpAddress_Type=IpAddress
_AlLBSSFPeerPrivIpAddress_Object=MibTableColumn
alLBSSFPeerPrivIpAddress=_AlLBSSFPeerPrivIpAddress_Object((1,3,6,1,4,1,3076,2,1,2,36,2,1,2),_AlLBSSFPeerPrivIpAddress_Type())
alLBSSFPeerPrivIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:alLBSSFPeerPrivIpAddress.setStatus(_A)
_AlLBSSFPeerPubIpAddress_Type=IpAddress
_AlLBSSFPeerPubIpAddress_Object=MibTableColumn
alLBSSFPeerPubIpAddress=_AlLBSSFPeerPubIpAddress_Object((1,3,6,1,4,1,3076,2,1,2,36,2,1,3),_AlLBSSFPeerPubIpAddress_Type())
alLBSSFPeerPubIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:alLBSSFPeerPubIpAddress.setStatus(_A)
_AlLBSSFPeerMappedPubIpAddress_Type=IpAddress
_AlLBSSFPeerMappedPubIpAddress_Object=MibTableColumn
alLBSSFPeerMappedPubIpAddress=_AlLBSSFPeerMappedPubIpAddress_Object((1,3,6,1,4,1,3076,2,1,2,36,2,1,4),_AlLBSSFPeerMappedPubIpAddress_Type())
alLBSSFPeerMappedPubIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:alLBSSFPeerMappedPubIpAddress.setStatus(_A)
_AlLBSSFPeerActive_Type=TruthValue
_AlLBSSFPeerActive_Object=MibTableColumn
alLBSSFPeerActive=_AlLBSSFPeerActive_Object((1,3,6,1,4,1,3076,2,1,2,36,2,1,5),_AlLBSSFPeerActive_Type())
alLBSSFPeerActive.setMaxAccess(_C)
if mibBuilder.loadTexts:alLBSSFPeerActive.setStatus(_A)
class _AlLBSSFPeerFaultZone_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,25))
_AlLBSSFPeerFaultZone_Type.__name__=_E
_AlLBSSFPeerFaultZone_Object=MibTableColumn
alLBSSFPeerFaultZone=_AlLBSSFPeerFaultZone_Object((1,3,6,1,4,1,3076,2,1,2,36,2,1,6),_AlLBSSFPeerFaultZone_Type())
alLBSSFPeerFaultZone.setMaxAccess(_C)
if mibBuilder.loadTexts:alLBSSFPeerFaultZone.setStatus(_A)
_AlLBSSFPeerRole_Type=DeviceRole
_AlLBSSFPeerRole_Object=MibTableColumn
alLBSSFPeerRole=_AlLBSSFPeerRole_Object((1,3,6,1,4,1,3076,2,1,2,36,2,1,7),_AlLBSSFPeerRole_Type())
alLBSSFPeerRole.setMaxAccess(_C)
if mibBuilder.loadTexts:alLBSSFPeerRole.setStatus(_A)
_AlLBSSFPeerDeviceType_Type=DeviceType
_AlLBSSFPeerDeviceType_Object=MibTableColumn
alLBSSFPeerDeviceType=_AlLBSSFPeerDeviceType_Object((1,3,6,1,4,1,3076,2,1,2,36,2,1,8),_AlLBSSFPeerDeviceType_Type())
alLBSSFPeerDeviceType.setMaxAccess(_C)
if mibBuilder.loadTexts:alLBSSFPeerDeviceType.setStatus(_A)
class _AlLBSSFPeerLoad_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_AlLBSSFPeerLoad_Type.__name__=_D
_AlLBSSFPeerLoad_Object=MibTableColumn
alLBSSFPeerLoad=_AlLBSSFPeerLoad_Object((1,3,6,1,4,1,3076,2,1,2,36,2,1,9),_AlLBSSFPeerLoad_Type())
alLBSSFPeerLoad.setMaxAccess(_C)
if mibBuilder.loadTexts:alLBSSFPeerLoad.setStatus(_A)
class _AlLBSSFPeerPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_AlLBSSFPeerPriority_Type.__name__=_E
_AlLBSSFPeerPriority_Object=MibTableColumn
alLBSSFPeerPriority=_AlLBSSFPeerPriority_Object((1,3,6,1,4,1,3076,2,1,2,36,2,1,10),_AlLBSSFPeerPriority_Type())
alLBSSFPeerPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:alLBSSFPeerPriority.setStatus(_A)
class _AlLBSSFPeerActiveSessions_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100000))
_AlLBSSFPeerActiveSessions_Type.__name__=_D
_AlLBSSFPeerActiveSessions_Object=MibTableColumn
alLBSSFPeerActiveSessions=_AlLBSSFPeerActiveSessions_Object((1,3,6,1,4,1,3076,2,1,2,36,2,1,11),_AlLBSSFPeerActiveSessions_Type())
alLBSSFPeerActiveSessions.setMaxAccess(_C)
if mibBuilder.loadTexts:alLBSSFPeerActiveSessions.setStatus(_A)
_AlLBSSFPeerJoinTime_Type=TimeTicks
_AlLBSSFPeerJoinTime_Object=MibTableColumn
alLBSSFPeerJoinTime=_AlLBSSFPeerJoinTime_Object((1,3,6,1,4,1,3076,2,1,2,36,2,1,12),_AlLBSSFPeerJoinTime_Type())
alLBSSFPeerJoinTime.setMaxAccess(_C)
if mibBuilder.loadTexts:alLBSSFPeerJoinTime.setStatus(_A)
altigaStatsLBSSFGroup=ObjectGroup((1,3,6,1,4,1,3076,2,1,1,1,36,3))
altigaStatsLBSSFGroup.setObjects(*((_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_F),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V)))
if mibBuilder.loadTexts:altigaStatsLBSSFGroup.setStatus(_A)
altigaLBSSFStatsMibCompliance=ModuleCompliance((1,3,6,1,4,1,3076,1,1,41,2,1,1,1))
altigaLBSSFStatsMibCompliance.setObjects((_B,_W))
if mibBuilder.loadTexts:altigaLBSSFStatsMibCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'DeviceType':DeviceType,'DeviceRole':DeviceRole,'altigaLBSSFStatsMibModule':altigaLBSSFStatsMibModule,'altigaLBSSFStatsMibConformance':altigaLBSSFStatsMibConformance,'altigaLBSSFStatsMibCompliances':altigaLBSSFStatsMibCompliances,'altigaLBSSFStatsMibCompliance':altigaLBSSFStatsMibCompliance,_W:altigaStatsLBSSFGroup,'alStatsLBSSFGlobal':alStatsLBSSFGlobal,_G:alLBSSFRole,_H:alLBSSFDeviceType,_I:alLBSSFActive,_J:alLBSSFNumberOfPeers,_K:alLBSSFLoad,'alLBSSFPeerTable':alLBSSFPeerTable,'alLBSSFPeerEntry':alLBSSFPeerEntry,_L:alLBSSFPeerRowStatus,_F:alLBSSFPeerPrivIpAddress,_M:alLBSSFPeerPubIpAddress,_N:alLBSSFPeerMappedPubIpAddress,_O:alLBSSFPeerActive,_P:alLBSSFPeerFaultZone,_Q:alLBSSFPeerRole,_R:alLBSSFPeerDeviceType,_S:alLBSSFPeerLoad,_T:alLBSSFPeerPriority,_U:alLBSSFPeerActiveSessions,_V:alLBSSFPeerJoinTime})