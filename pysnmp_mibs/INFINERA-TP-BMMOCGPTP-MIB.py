_b='bmmOcgPtpGroup'
_a='bmmOcgPtpProvOpenWaveRemotePtp'
_Z='bmmOcgPtpShutterState'
_Y='bmmOcgPtpAutoDiscSoakTime'
_X='bmmOcgPtpDiscoveredRemoteTP'
_W='bmmOcgPtpOcgActiveChannelMap'
_V='bmmOcgPtpOcgSignalType'
_U='bmmOcgPtpOcgPortConfig'
_T='bmmOcgPtpPmHistStatsEnable'
_S='bmmOcgPtpDeMuxInsertionLoss'
_R='bmmOcgPtpMuxInsertionLoss'
_Q='bmmOcgPtpTargetRxOcgPower'
_P='bmmOcgPtpOcgPowerControlLoop'
_O='bmmOcgPtpOcgNumber'
_N='bmmOcgPtpProvisionedOcgTP'
_M='bmmOcgPtpDiscoveredOcgTP'
_L='Integer32'
_K='InfnSignalType'
_J='InfnPowerControlLoop'
_I='InfnPmHistStatsControl'
_H='InfnOcgPortConfig'
_G='ifIndex'
_F='IF-MIB'
_E='FloatTenths'
_D='read-only'
_C='read-write'
_B='INFINERA-TP-BMMOCGPTP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_F,_G)
terminationPoint,=mibBuilder.importSymbols('INFINERA-REG-MIB','terminationPoint')
FloatTenths,InfnOcgChannelMap,InfnOcgPortConfig,InfnPmHistStatsControl,InfnPowerControlLoop,InfnShutterState,InfnSignalType=mibBuilder.importSymbols('INFINERA-TC-MIB',_E,'InfnOcgChannelMap',_H,_I,_J,'InfnShutterState',_K)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_L,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
bmmOcgPtpMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,2,3))
if mibBuilder.loadTexts:bmmOcgPtpMIB.setRevisions(('2008-10-20 00:00',))
_BmmOcgPtpTable_Object=MibTable
bmmOcgPtpTable=_BmmOcgPtpTable_Object((1,3,6,1,4,1,21296,2,2,2,2,3,1))
if mibBuilder.loadTexts:bmmOcgPtpTable.setStatus(_A)
_BmmOcgPtpEntry_Object=MibTableRow
bmmOcgPtpEntry=_BmmOcgPtpEntry_Object((1,3,6,1,4,1,21296,2,2,2,2,3,1,1))
bmmOcgPtpEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:bmmOcgPtpEntry.setStatus(_A)
_BmmOcgPtpDiscoveredOcgTP_Type=DisplayString
_BmmOcgPtpDiscoveredOcgTP_Object=MibTableColumn
bmmOcgPtpDiscoveredOcgTP=_BmmOcgPtpDiscoveredOcgTP_Object((1,3,6,1,4,1,21296,2,2,2,2,3,1,1,1),_BmmOcgPtpDiscoveredOcgTP_Type())
bmmOcgPtpDiscoveredOcgTP.setMaxAccess(_D)
if mibBuilder.loadTexts:bmmOcgPtpDiscoveredOcgTP.setStatus(_A)
_BmmOcgPtpProvisionedOcgTP_Type=DisplayString
_BmmOcgPtpProvisionedOcgTP_Object=MibTableColumn
bmmOcgPtpProvisionedOcgTP=_BmmOcgPtpProvisionedOcgTP_Object((1,3,6,1,4,1,21296,2,2,2,2,3,1,1,2),_BmmOcgPtpProvisionedOcgTP_Type())
bmmOcgPtpProvisionedOcgTP.setMaxAccess(_C)
if mibBuilder.loadTexts:bmmOcgPtpProvisionedOcgTP.setStatus(_A)
class _BmmOcgPtpOcgNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_BmmOcgPtpOcgNumber_Type.__name__=_L
_BmmOcgPtpOcgNumber_Object=MibTableColumn
bmmOcgPtpOcgNumber=_BmmOcgPtpOcgNumber_Object((1,3,6,1,4,1,21296,2,2,2,2,3,1,1,3),_BmmOcgPtpOcgNumber_Type())
bmmOcgPtpOcgNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:bmmOcgPtpOcgNumber.setStatus(_A)
class _BmmOcgPtpOcgPowerControlLoop_Type(InfnPowerControlLoop):defaultValue=2
_BmmOcgPtpOcgPowerControlLoop_Type.__name__=_J
_BmmOcgPtpOcgPowerControlLoop_Object=MibTableColumn
bmmOcgPtpOcgPowerControlLoop=_BmmOcgPtpOcgPowerControlLoop_Object((1,3,6,1,4,1,21296,2,2,2,2,3,1,1,4),_BmmOcgPtpOcgPowerControlLoop_Type())
bmmOcgPtpOcgPowerControlLoop.setMaxAccess(_C)
if mibBuilder.loadTexts:bmmOcgPtpOcgPowerControlLoop.setStatus(_A)
class _BmmOcgPtpTargetRxOcgPower_Type(FloatTenths):defaultValue=0
_BmmOcgPtpTargetRxOcgPower_Type.__name__=_E
_BmmOcgPtpTargetRxOcgPower_Object=MibTableColumn
bmmOcgPtpTargetRxOcgPower=_BmmOcgPtpTargetRxOcgPower_Object((1,3,6,1,4,1,21296,2,2,2,2,3,1,1,5),_BmmOcgPtpTargetRxOcgPower_Type())
bmmOcgPtpTargetRxOcgPower.setMaxAccess(_D)
if mibBuilder.loadTexts:bmmOcgPtpTargetRxOcgPower.setStatus(_A)
class _BmmOcgPtpMuxInsertionLoss_Type(FloatTenths):defaultValue=0
_BmmOcgPtpMuxInsertionLoss_Type.__name__=_E
_BmmOcgPtpMuxInsertionLoss_Object=MibTableColumn
bmmOcgPtpMuxInsertionLoss=_BmmOcgPtpMuxInsertionLoss_Object((1,3,6,1,4,1,21296,2,2,2,2,3,1,1,6),_BmmOcgPtpMuxInsertionLoss_Type())
bmmOcgPtpMuxInsertionLoss.setMaxAccess(_D)
if mibBuilder.loadTexts:bmmOcgPtpMuxInsertionLoss.setStatus(_A)
class _BmmOcgPtpDeMuxInsertionLoss_Type(FloatTenths):defaultValue=0
_BmmOcgPtpDeMuxInsertionLoss_Type.__name__=_E
_BmmOcgPtpDeMuxInsertionLoss_Object=MibTableColumn
bmmOcgPtpDeMuxInsertionLoss=_BmmOcgPtpDeMuxInsertionLoss_Object((1,3,6,1,4,1,21296,2,2,2,2,3,1,1,7),_BmmOcgPtpDeMuxInsertionLoss_Type())
bmmOcgPtpDeMuxInsertionLoss.setMaxAccess(_D)
if mibBuilder.loadTexts:bmmOcgPtpDeMuxInsertionLoss.setStatus(_A)
class _BmmOcgPtpPmHistStatsEnable_Type(InfnPmHistStatsControl):defaultValue=1
_BmmOcgPtpPmHistStatsEnable_Type.__name__=_I
_BmmOcgPtpPmHistStatsEnable_Object=MibTableColumn
bmmOcgPtpPmHistStatsEnable=_BmmOcgPtpPmHistStatsEnable_Object((1,3,6,1,4,1,21296,2,2,2,2,3,1,1,8),_BmmOcgPtpPmHistStatsEnable_Type())
bmmOcgPtpPmHistStatsEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:bmmOcgPtpPmHistStatsEnable.setStatus(_A)
class _BmmOcgPtpOcgPortConfig_Type(InfnOcgPortConfig):defaultValue=2
_BmmOcgPtpOcgPortConfig_Type.__name__=_H
_BmmOcgPtpOcgPortConfig_Object=MibTableColumn
bmmOcgPtpOcgPortConfig=_BmmOcgPtpOcgPortConfig_Object((1,3,6,1,4,1,21296,2,2,2,2,3,1,1,9),_BmmOcgPtpOcgPortConfig_Type())
bmmOcgPtpOcgPortConfig.setMaxAccess(_D)
if mibBuilder.loadTexts:bmmOcgPtpOcgPortConfig.setStatus(_A)
class _BmmOcgPtpOcgSignalType_Type(InfnSignalType):defaultValue=1
_BmmOcgPtpOcgSignalType_Type.__name__=_K
_BmmOcgPtpOcgSignalType_Object=MibTableColumn
bmmOcgPtpOcgSignalType=_BmmOcgPtpOcgSignalType_Object((1,3,6,1,4,1,21296,2,2,2,2,3,1,1,10),_BmmOcgPtpOcgSignalType_Type())
bmmOcgPtpOcgSignalType.setMaxAccess(_C)
if mibBuilder.loadTexts:bmmOcgPtpOcgSignalType.setStatus(_A)
_BmmOcgPtpOcgActiveChannelMap_Type=InfnOcgChannelMap
_BmmOcgPtpOcgActiveChannelMap_Object=MibTableColumn
bmmOcgPtpOcgActiveChannelMap=_BmmOcgPtpOcgActiveChannelMap_Object((1,3,6,1,4,1,21296,2,2,2,2,3,1,1,11),_BmmOcgPtpOcgActiveChannelMap_Type())
bmmOcgPtpOcgActiveChannelMap.setMaxAccess(_C)
if mibBuilder.loadTexts:bmmOcgPtpOcgActiveChannelMap.setStatus(_A)
_BmmOcgPtpDiscoveredRemoteTP_Type=DisplayString
_BmmOcgPtpDiscoveredRemoteTP_Object=MibTableColumn
bmmOcgPtpDiscoveredRemoteTP=_BmmOcgPtpDiscoveredRemoteTP_Object((1,3,6,1,4,1,21296,2,2,2,2,3,1,1,12),_BmmOcgPtpDiscoveredRemoteTP_Type())
bmmOcgPtpDiscoveredRemoteTP.setMaxAccess(_D)
if mibBuilder.loadTexts:bmmOcgPtpDiscoveredRemoteTP.setStatus(_A)
_BmmOcgPtpAutoDiscSoakTime_Type=Unsigned32
_BmmOcgPtpAutoDiscSoakTime_Object=MibTableColumn
bmmOcgPtpAutoDiscSoakTime=_BmmOcgPtpAutoDiscSoakTime_Object((1,3,6,1,4,1,21296,2,2,2,2,3,1,1,13),_BmmOcgPtpAutoDiscSoakTime_Type())
bmmOcgPtpAutoDiscSoakTime.setMaxAccess(_C)
if mibBuilder.loadTexts:bmmOcgPtpAutoDiscSoakTime.setStatus(_A)
_BmmOcgPtpShutterState_Type=InfnShutterState
_BmmOcgPtpShutterState_Object=MibTableColumn
bmmOcgPtpShutterState=_BmmOcgPtpShutterState_Object((1,3,6,1,4,1,21296,2,2,2,2,3,1,1,14),_BmmOcgPtpShutterState_Type())
bmmOcgPtpShutterState.setMaxAccess(_C)
if mibBuilder.loadTexts:bmmOcgPtpShutterState.setStatus(_A)
_BmmOcgPtpProvOpenWaveRemotePtp_Type=DisplayString
_BmmOcgPtpProvOpenWaveRemotePtp_Object=MibTableColumn
bmmOcgPtpProvOpenWaveRemotePtp=_BmmOcgPtpProvOpenWaveRemotePtp_Object((1,3,6,1,4,1,21296,2,2,2,2,3,1,1,15),_BmmOcgPtpProvOpenWaveRemotePtp_Type())
bmmOcgPtpProvOpenWaveRemotePtp.setMaxAccess(_C)
if mibBuilder.loadTexts:bmmOcgPtpProvOpenWaveRemotePtp.setStatus(_A)
_BmmOcgPtpConformance_ObjectIdentity=ObjectIdentity
bmmOcgPtpConformance=_BmmOcgPtpConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,3,3))
_BmmOcgPtpCompliances_ObjectIdentity=ObjectIdentity
bmmOcgPtpCompliances=_BmmOcgPtpCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,3,3,1))
_BmmOcgPtpGroups_ObjectIdentity=ObjectIdentity
bmmOcgPtpGroups=_BmmOcgPtpGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,3,3,2))
bmmOcgPtpGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,2,3,3,2,1))
bmmOcgPtpGroup.setObjects(*((_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a)))
if mibBuilder.loadTexts:bmmOcgPtpGroup.setStatus(_A)
bmmOcgPtpCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,2,3,3,1,1))
bmmOcgPtpCompliance.setObjects((_B,_b))
if mibBuilder.loadTexts:bmmOcgPtpCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'bmmOcgPtpMIB':bmmOcgPtpMIB,'bmmOcgPtpTable':bmmOcgPtpTable,'bmmOcgPtpEntry':bmmOcgPtpEntry,_M:bmmOcgPtpDiscoveredOcgTP,_N:bmmOcgPtpProvisionedOcgTP,_O:bmmOcgPtpOcgNumber,_P:bmmOcgPtpOcgPowerControlLoop,_Q:bmmOcgPtpTargetRxOcgPower,_R:bmmOcgPtpMuxInsertionLoss,_S:bmmOcgPtpDeMuxInsertionLoss,_T:bmmOcgPtpPmHistStatsEnable,_U:bmmOcgPtpOcgPortConfig,_V:bmmOcgPtpOcgSignalType,_W:bmmOcgPtpOcgActiveChannelMap,_X:bmmOcgPtpDiscoveredRemoteTP,_Y:bmmOcgPtpAutoDiscSoakTime,_Z:bmmOcgPtpShutterState,_a:bmmOcgPtpProvOpenWaveRemotePtp,'bmmOcgPtpConformance':bmmOcgPtpConformance,'bmmOcgPtpCompliances':bmmOcgPtpCompliances,'bmmOcgPtpCompliance':bmmOcgPtpCompliance,'bmmOcgPtpGroups':bmmOcgPtpGroups,_b:bmmOcgPtpGroup})