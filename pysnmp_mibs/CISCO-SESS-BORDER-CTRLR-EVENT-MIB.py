_BI='csbNotifEnabledGroupSup1'
_BH='csbNotificationGroupSup1'
_BG='csbQOSAlertGroup'
_BF='csbNotifEnabledGroup'
_BE='csbSLAGroup'
_BD='csbNotificationGroup'
_BC='csbQOSUnansweredCallRatioEvent'
_BB='csbQOSMoscqeClearEvent'
_BA='csbQOSMoscqeEvent'
_B9='csbQOSRemoteJitterClearEvent'
_B8='csbQOSRemoteJitterEvent'
_B7='csbQOSLocalJitterClearEvent'
_B6='csbQOSLocalJitterEvent'
_B5='csbQOSRoundTripDelayClearEvent'
_B4='csbQOSRoundTripDelayEvent'
_B3='csbQOSPercentPktDropClearEvent'
_B2='csbQOSPercentPktDropEvent'
_B1='csbQOSPercentPktLostClearEvent'
_B0='csbQOSPercentPktLostEvent'
_A_='csbQOSUnansweredCallRatioClearEvent'
_Az='csbSLAViolationRev1'
_Ay='csbSLAViolation'
_Ax='csbQOSAlertMoscqeNotifEnabled'
_Aw='csbQOSAlertPercentPktLostNotifEnabled'
_Av='csbQOSAlertRemoteJitterNotifEnabled'
_Au='csbQOSAlertLocalJitterNotifEnabled'
_At='csbQOSAlertRoundTripDelayNotifEnabled'
_As='csbQOSAlertPercentPktDropNotifEnabled'
_Ar='csbQOSAlertUnansweredCallRatioNotifEnabled'
_Aq='csbSLAViolationNotifEnabledRev1'
_Ap='csbSLAViolationNotifEnabled'
_Ao='authentication'
_An='accounting'
_Am='SnmpAdminString'
_Al='InetPortNumber'
_Ak='csbNotifEnabledGroupRev1'
_Aj='csbSLAGroupRev1'
_Ai='csbNotificationGroupRev1'
_Ah='csbH248ControllerStatus'
_Ag='csbDiameterConnectionStatus'
_Af='csbRadiusConnectionStatus'
_Ae='csbSystemCongestionAlarmEvent'
_Ad='csbServiceStateEvent'
_Ac='csbAdjacencyStatus'
_Ab='csbDynamicBlackListEvent'
_Aa='csbSourceAlertEvent'
_AZ='csbSLACurrentUsageRev1'
_AY='csbSLAPolicyLimitRev1'
_AX='csbH248ControllerStatusNotifEnabled'
_AW='csbDiameterConnectionStatusNotifEnabled'
_AV='csbRadiusConnectionStatusNotifEnabled'
_AU='csbCongestionAlarmNotifEnabled'
_AT='csbServiceStateNotifEnabled'
_AS='csbAdjacencyStatusNotifEnabled'
_AR='csbBlackListNotifEnabled'
_AQ='csbSourceAlertNotifEnabled'
_AP='csbH248ControllerPort'
_AO='csbH248ControllerAddress'
_AN='csb248ControllerAddressType'
_AM='csbH248ControllerState'
_AL='csbDiameterServerName'
_AK='csbDiameterGroupName'
_AJ='csbDiameterType'
_AI='csbDiameterConnectionState'
_AH='csbRadiusServerPriority'
_AG='csbRadiusServerAddress'
_AF='csbRadiusServerAddressType'
_AE='csbRadiusServerName'
_AD='csbRadiusType'
_AC='csbRadiusConnectionState'
_AB='csbSLACurrentUsage'
_AA='csbSLAPolicyLimit'
_A9='csbCongestionAlarmType'
_A8='csbCongestionAlarmState'
_A7='csbSBCServiceState'
_A6='csbSBCServiceSlot'
_A5='csbAdjacencyState'
_A4='csbAdjacencyAccountName'
_A3='csbAdjacencyType'
_A2='csbDynamicBlackListSrcBlocked'
_A1='csbDynamicBlackListPortNumber'
_A0='csbDynamicBlackListTransportType'
_z='csbDynamicBlackListAddress'
_y='csbDynamicBlackListAddressType'
_x='csbDynamicBlackListVpnId'
_w='csbDynamicBlackListSubFamily'
_v='csbSrcAlertLocalAddressType'
_u='csbSrcAlertVpnId'
_t='csbSrcAlertRemotePort'
_s='csbSrcAlertRemoteAddress'
_r='csbSrcAlertRemoteAddressType'
_q='csbSrcAlertLocalPort'
_p='csbSrcAlertLocalAddress'
_o='csbSrcAlertFlowPairId'
_n='csbSrcAlertGateId'
_m='csbSrcAlertVdbeId'
_l='csbCongestionGroup'
_k='csbH248StatusGroup'
_j='csbDiameterConnectionGroup'
_i='csbRadiusConnectionGroup'
_h='csbSBCServiceGroup'
_g='csbAdjacencyGroup'
_f='csbNotificationManadatoryParams'
_e='csbDynamicBlackListGroup'
_d='csbSourceAlertGroup'
_c='occurrences'
_b='OctetString'
_a='csbSLAPolicyRestriction'
_Z='csbSLAViolationEvent'
_Y='csbSLAPolicyScope'
_X='csbSLAPolicyAccountName'
_W='InetAddress'
_V='csbQOSAlertCurrentLevel'
_U='deprecated'
_T='Integer32'
_S='csbQOSAlertSummaryPeriod'
_R='csbQOSAlertType'
_Q='csbQOSMajorAlertCount'
_P='csbQOSCriticalAlertCount'
_O='csbQOSMinorAlertCount'
_N='csbQOSNormalAlertCount'
_M='csbQOSAlertPreviousLevel'
_L='csbQOSAlertCurrentValue'
_K='csbAdjacencyName'
_J='read-write'
_I='csbAlarmDescription'
_H='csbSBCServiceName'
_G='csbAlarmTime'
_F='csbAlarmID'
_E='csbAlarmSeverity'
_D='csbAlarmSubsystem'
_C='accessible-for-notify'
_B='current'
_A='CISCO-SESS-BORDER-CTRLR-EVENT-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_b,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
CiscoSbcPeriodicStatsInterval,=mibBuilder.importSymbols('CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB','CiscoSbcPeriodicStatsInterval')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CiscoAlarmSeverity,=mibBuilder.importSymbols('CISCO-TC','CiscoAlarmSeverity')
InetAddress,InetAddressType,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB',_W,'InetAddressType',_Al)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_Am)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_T,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
ciscoSessBorderCtrlrEventMIB=ModuleIdentity((1,3,6,1,4,1,9,9,658))
if mibBuilder.loadTexts:ciscoSessBorderCtrlrEventMIB.setRevisions(('2010-12-06 00:00','2008-08-27 00:00','2008-05-29 00:00'))
class CsbQOSAlertScopeType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('global',1),('adjacency',2)))
class CsbDynamicBlackListedSrcSubFamily(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('blackVPN',1),('blackAddress',2),('blackPort',3)))
class CsbDynamicBlackListedTransPortType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('udp',2),('tcp',3)))
_CiscoSessBorderCtrlrMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoSessBorderCtrlrMIBNotifs=_CiscoSessBorderCtrlrMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,658,0))
_CiscoSessBorderCtrlrMIBObjects_ObjectIdentity=ObjectIdentity
ciscoSessBorderCtrlrMIBObjects=_CiscoSessBorderCtrlrMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,658,1))
class _CsbAlarmSubsystem_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('signaling',1),('media',2),('cac',3)))
_CsbAlarmSubsystem_Type.__name__=_T
_CsbAlarmSubsystem_Object=MibScalar
csbAlarmSubsystem=_CsbAlarmSubsystem_Object((1,3,6,1,4,1,9,9,658,1,1),_CsbAlarmSubsystem_Type())
csbAlarmSubsystem.setMaxAccess(_C)
if mibBuilder.loadTexts:csbAlarmSubsystem.setStatus(_B)
_CsbAlarmSeverity_Type=CiscoAlarmSeverity
_CsbAlarmSeverity_Object=MibScalar
csbAlarmSeverity=_CsbAlarmSeverity_Object((1,3,6,1,4,1,9,9,658,1,2),_CsbAlarmSeverity_Type())
csbAlarmSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:csbAlarmSeverity.setStatus(_B)
class _CsbAlarmID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CsbAlarmID_Type.__name__=_T
_CsbAlarmID_Object=MibScalar
csbAlarmID=_CsbAlarmID_Object((1,3,6,1,4,1,9,9,658,1,3),_CsbAlarmID_Type())
csbAlarmID.setMaxAccess(_C)
if mibBuilder.loadTexts:csbAlarmID.setStatus(_B)
class _CsbAlarmTime_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_CsbAlarmTime_Type.__name__=_b
_CsbAlarmTime_Object=MibScalar
csbAlarmTime=_CsbAlarmTime_Object((1,3,6,1,4,1,9,9,658,1,4),_CsbAlarmTime_Type())
csbAlarmTime.setMaxAccess(_C)
if mibBuilder.loadTexts:csbAlarmTime.setStatus(_B)
_CsbSBCServiceName_Type=SnmpAdminString
_CsbSBCServiceName_Object=MibScalar
csbSBCServiceName=_CsbSBCServiceName_Object((1,3,6,1,4,1,9,9,658,1,5),_CsbSBCServiceName_Type())
csbSBCServiceName.setMaxAccess(_C)
if mibBuilder.loadTexts:csbSBCServiceName.setStatus(_B)
_CsbAlarmDescription_Type=OctetString
_CsbAlarmDescription_Object=MibScalar
csbAlarmDescription=_CsbAlarmDescription_Object((1,3,6,1,4,1,9,9,658,1,6),_CsbAlarmDescription_Type())
csbAlarmDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:csbAlarmDescription.setStatus(_B)
class _CsbSrcAlertVdbeId_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_CsbSrcAlertVdbeId_Type.__name__=_Am
_CsbSrcAlertVdbeId_Object=MibScalar
csbSrcAlertVdbeId=_CsbSrcAlertVdbeId_Object((1,3,6,1,4,1,9,9,658,1,7),_CsbSrcAlertVdbeId_Type())
csbSrcAlertVdbeId.setMaxAccess(_C)
if mibBuilder.loadTexts:csbSrcAlertVdbeId.setStatus(_B)
_CsbSrcAlertGateId_Type=Unsigned32
_CsbSrcAlertGateId_Object=MibScalar
csbSrcAlertGateId=_CsbSrcAlertGateId_Object((1,3,6,1,4,1,9,9,658,1,8),_CsbSrcAlertGateId_Type())
csbSrcAlertGateId.setMaxAccess(_C)
if mibBuilder.loadTexts:csbSrcAlertGateId.setStatus(_B)
_CsbSrcAlertFlowPairId_Type=Unsigned32
_CsbSrcAlertFlowPairId_Object=MibScalar
csbSrcAlertFlowPairId=_CsbSrcAlertFlowPairId_Object((1,3,6,1,4,1,9,9,658,1,9),_CsbSrcAlertFlowPairId_Type())
csbSrcAlertFlowPairId.setMaxAccess(_C)
if mibBuilder.loadTexts:csbSrcAlertFlowPairId.setStatus(_B)
_CsbSrcAlertLocalAddressType_Type=InetAddressType
_CsbSrcAlertLocalAddressType_Object=MibScalar
csbSrcAlertLocalAddressType=_CsbSrcAlertLocalAddressType_Object((1,3,6,1,4,1,9,9,658,1,10),_CsbSrcAlertLocalAddressType_Type())
csbSrcAlertLocalAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:csbSrcAlertLocalAddressType.setStatus(_B)
class _CsbSrcAlertLocalAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_CsbSrcAlertLocalAddress_Type.__name__=_W
_CsbSrcAlertLocalAddress_Object=MibScalar
csbSrcAlertLocalAddress=_CsbSrcAlertLocalAddress_Object((1,3,6,1,4,1,9,9,658,1,11),_CsbSrcAlertLocalAddress_Type())
csbSrcAlertLocalAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:csbSrcAlertLocalAddress.setStatus(_B)
_CsbSrcAlertLocalPort_Type=InetPortNumber
_CsbSrcAlertLocalPort_Object=MibScalar
csbSrcAlertLocalPort=_CsbSrcAlertLocalPort_Object((1,3,6,1,4,1,9,9,658,1,12),_CsbSrcAlertLocalPort_Type())
csbSrcAlertLocalPort.setMaxAccess(_C)
if mibBuilder.loadTexts:csbSrcAlertLocalPort.setStatus(_B)
_CsbSrcAlertRemoteAddressType_Type=InetAddressType
_CsbSrcAlertRemoteAddressType_Object=MibScalar
csbSrcAlertRemoteAddressType=_CsbSrcAlertRemoteAddressType_Object((1,3,6,1,4,1,9,9,658,1,13),_CsbSrcAlertRemoteAddressType_Type())
csbSrcAlertRemoteAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:csbSrcAlertRemoteAddressType.setStatus(_B)
class _CsbSrcAlertRemoteAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_CsbSrcAlertRemoteAddress_Type.__name__=_W
_CsbSrcAlertRemoteAddress_Object=MibScalar
csbSrcAlertRemoteAddress=_CsbSrcAlertRemoteAddress_Object((1,3,6,1,4,1,9,9,658,1,14),_CsbSrcAlertRemoteAddress_Type())
csbSrcAlertRemoteAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:csbSrcAlertRemoteAddress.setStatus(_B)
class _CsbSrcAlertRemotePort_Type(InetPortNumber):subtypeSpec=InetPortNumber.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CsbSrcAlertRemotePort_Type.__name__=_Al
_CsbSrcAlertRemotePort_Object=MibScalar
csbSrcAlertRemotePort=_CsbSrcAlertRemotePort_Object((1,3,6,1,4,1,9,9,658,1,15),_CsbSrcAlertRemotePort_Type())
csbSrcAlertRemotePort.setMaxAccess(_C)
if mibBuilder.loadTexts:csbSrcAlertRemotePort.setStatus(_B)
class _CsbSrcAlertVpnId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CsbSrcAlertVpnId_Type.__name__=_b
_CsbSrcAlertVpnId_Object=MibScalar
csbSrcAlertVpnId=_CsbSrcAlertVpnId_Object((1,3,6,1,4,1,9,9,658,1,16),_CsbSrcAlertVpnId_Type())
csbSrcAlertVpnId.setMaxAccess(_C)
if mibBuilder.loadTexts:csbSrcAlertVpnId.setStatus(_B)
_CsbDynamicBlackListSubFamily_Type=CsbDynamicBlackListedSrcSubFamily
_CsbDynamicBlackListSubFamily_Object=MibScalar
csbDynamicBlackListSubFamily=_CsbDynamicBlackListSubFamily_Object((1,3,6,1,4,1,9,9,658,1,17),_CsbDynamicBlackListSubFamily_Type())
csbDynamicBlackListSubFamily.setMaxAccess(_C)
if mibBuilder.loadTexts:csbDynamicBlackListSubFamily.setStatus(_B)
class _CsbDynamicBlackListVpnId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CsbDynamicBlackListVpnId_Type.__name__=_b
_CsbDynamicBlackListVpnId_Object=MibScalar
csbDynamicBlackListVpnId=_CsbDynamicBlackListVpnId_Object((1,3,6,1,4,1,9,9,658,1,18),_CsbDynamicBlackListVpnId_Type())
csbDynamicBlackListVpnId.setMaxAccess(_C)
if mibBuilder.loadTexts:csbDynamicBlackListVpnId.setStatus(_B)
_CsbDynamicBlackListAddressType_Type=InetAddressType
_CsbDynamicBlackListAddressType_Object=MibScalar
csbDynamicBlackListAddressType=_CsbDynamicBlackListAddressType_Object((1,3,6,1,4,1,9,9,658,1,19),_CsbDynamicBlackListAddressType_Type())
csbDynamicBlackListAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:csbDynamicBlackListAddressType.setStatus(_B)
_CsbDynamicBlackListAddress_Type=InetAddress
_CsbDynamicBlackListAddress_Object=MibScalar
csbDynamicBlackListAddress=_CsbDynamicBlackListAddress_Object((1,3,6,1,4,1,9,9,658,1,20),_CsbDynamicBlackListAddress_Type())
csbDynamicBlackListAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:csbDynamicBlackListAddress.setStatus(_B)
_CsbDynamicBlackListTransportType_Type=CsbDynamicBlackListedTransPortType
_CsbDynamicBlackListTransportType_Object=MibScalar
csbDynamicBlackListTransportType=_CsbDynamicBlackListTransportType_Object((1,3,6,1,4,1,9,9,658,1,21),_CsbDynamicBlackListTransportType_Type())
csbDynamicBlackListTransportType.setMaxAccess(_C)
if mibBuilder.loadTexts:csbDynamicBlackListTransportType.setStatus(_B)
_CsbDynamicBlackListPortNumber_Type=InetPortNumber
_CsbDynamicBlackListPortNumber_Object=MibScalar
csbDynamicBlackListPortNumber=_CsbDynamicBlackListPortNumber_Object((1,3,6,1,4,1,9,9,658,1,22),_CsbDynamicBlackListPortNumber_Type())
csbDynamicBlackListPortNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:csbDynamicBlackListPortNumber.setStatus(_B)
_CsbDynamicBlackListSrcBlocked_Type=TruthValue
_CsbDynamicBlackListSrcBlocked_Object=MibScalar
csbDynamicBlackListSrcBlocked=_CsbDynamicBlackListSrcBlocked_Object((1,3,6,1,4,1,9,9,658,1,23),_CsbDynamicBlackListSrcBlocked_Type())
csbDynamicBlackListSrcBlocked.setMaxAccess(_C)
if mibBuilder.loadTexts:csbDynamicBlackListSrcBlocked.setStatus(_B)
class _CsbAdjacencyType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('sip',1),('h323',2)))
_CsbAdjacencyType_Type.__name__=_T
_CsbAdjacencyType_Object=MibScalar
csbAdjacencyType=_CsbAdjacencyType_Object((1,3,6,1,4,1,9,9,658,1,24),_CsbAdjacencyType_Type())
csbAdjacencyType.setMaxAccess(_C)
if mibBuilder.loadTexts:csbAdjacencyType.setStatus(_B)
class _CsbAdjacencyState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('attached',1),('detached',2)))
_CsbAdjacencyState_Type.__name__=_T
_CsbAdjacencyState_Object=MibScalar
csbAdjacencyState=_CsbAdjacencyState_Object((1,3,6,1,4,1,9,9,658,1,25),_CsbAdjacencyState_Type())
csbAdjacencyState.setMaxAccess(_C)
if mibBuilder.loadTexts:csbAdjacencyState.setStatus(_B)
_CsbAdjacencyName_Type=SnmpAdminString
_CsbAdjacencyName_Object=MibScalar
csbAdjacencyName=_CsbAdjacencyName_Object((1,3,6,1,4,1,9,9,658,1,26),_CsbAdjacencyName_Type())
csbAdjacencyName.setMaxAccess(_C)
if mibBuilder.loadTexts:csbAdjacencyName.setStatus(_B)
_CsbAdjacencyAccountName_Type=SnmpAdminString
_CsbAdjacencyAccountName_Object=MibScalar
csbAdjacencyAccountName=_CsbAdjacencyAccountName_Object((1,3,6,1,4,1,9,9,658,1,27),_CsbAdjacencyAccountName_Type())
csbAdjacencyAccountName.setMaxAccess(_C)
if mibBuilder.loadTexts:csbAdjacencyAccountName.setStatus(_B)
class _CsbSBCServiceState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('active',1),('standby',2),('offline',3)))
_CsbSBCServiceState_Type.__name__=_T
_CsbSBCServiceState_Object=MibScalar
csbSBCServiceState=_CsbSBCServiceState_Object((1,3,6,1,4,1,9,9,658,1,28),_CsbSBCServiceState_Type())
csbSBCServiceState.setMaxAccess(_C)
if mibBuilder.loadTexts:csbSBCServiceState.setStatus(_B)
_CsbSBCServiceSlot_Type=Integer32
_CsbSBCServiceSlot_Object=MibScalar
csbSBCServiceSlot=_CsbSBCServiceSlot_Object((1,3,6,1,4,1,9,9,658,1,29),_CsbSBCServiceSlot_Type())
csbSBCServiceSlot.setMaxAccess(_C)
if mibBuilder.loadTexts:csbSBCServiceSlot.setStatus(_B)
class _CsbCongestionAlarmType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('unknown',1),('cpu',2),('memory',3)))
_CsbCongestionAlarmType_Type.__name__=_T
_CsbCongestionAlarmType_Object=MibScalar
csbCongestionAlarmType=_CsbCongestionAlarmType_Object((1,3,6,1,4,1,9,9,658,1,30),_CsbCongestionAlarmType_Type())
csbCongestionAlarmType.setMaxAccess(_C)
if mibBuilder.loadTexts:csbCongestionAlarmType.setStatus(_B)
class _CsbCongestionAlarmState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('raised',1),('cleared',2)))
_CsbCongestionAlarmState_Type.__name__=_T
_CsbCongestionAlarmState_Object=MibScalar
csbCongestionAlarmState=_CsbCongestionAlarmState_Object((1,3,6,1,4,1,9,9,658,1,31),_CsbCongestionAlarmState_Type())
csbCongestionAlarmState.setMaxAccess(_C)
if mibBuilder.loadTexts:csbCongestionAlarmState.setStatus(_B)
_CsbSLAPolicyAccountName_Type=SnmpAdminString
_CsbSLAPolicyAccountName_Object=MibScalar
csbSLAPolicyAccountName=_CsbSLAPolicyAccountName_Object((1,3,6,1,4,1,9,9,658,1,32),_CsbSLAPolicyAccountName_Type())
csbSLAPolicyAccountName.setMaxAccess(_C)
if mibBuilder.loadTexts:csbSLAPolicyAccountName.setStatus(_B)
_CsbSLAPolicyScope_Type=SnmpAdminString
_CsbSLAPolicyScope_Object=MibScalar
csbSLAPolicyScope=_CsbSLAPolicyScope_Object((1,3,6,1,4,1,9,9,658,1,33),_CsbSLAPolicyScope_Type())
csbSLAPolicyScope.setMaxAccess(_C)
if mibBuilder.loadTexts:csbSLAPolicyScope.setStatus(_B)
_CsbSLAPolicyLimit_Type=Integer32
_CsbSLAPolicyLimit_Object=MibScalar
csbSLAPolicyLimit=_CsbSLAPolicyLimit_Object((1,3,6,1,4,1,9,9,658,1,34),_CsbSLAPolicyLimit_Type())
csbSLAPolicyLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:csbSLAPolicyLimit.setStatus(_U)
_CsbSLAViolationEvent_Type=SnmpAdminString
_CsbSLAViolationEvent_Object=MibScalar
csbSLAViolationEvent=_CsbSLAViolationEvent_Object((1,3,6,1,4,1,9,9,658,1,35),_CsbSLAViolationEvent_Type())
csbSLAViolationEvent.setMaxAccess(_C)
if mibBuilder.loadTexts:csbSLAViolationEvent.setStatus(_B)
_CsbSLAPolicyRestriction_Type=SnmpAdminString
_CsbSLAPolicyRestriction_Object=MibScalar
csbSLAPolicyRestriction=_CsbSLAPolicyRestriction_Object((1,3,6,1,4,1,9,9,658,1,36),_CsbSLAPolicyRestriction_Type())
csbSLAPolicyRestriction.setMaxAccess(_C)
if mibBuilder.loadTexts:csbSLAPolicyRestriction.setStatus(_B)
_CsbSLACurrentUsage_Type=Integer32
_CsbSLACurrentUsage_Object=MibScalar
csbSLACurrentUsage=_CsbSLACurrentUsage_Object((1,3,6,1,4,1,9,9,658,1,37),_CsbSLACurrentUsage_Type())
csbSLACurrentUsage.setMaxAccess(_C)
if mibBuilder.loadTexts:csbSLACurrentUsage.setStatus(_U)
class _CsbRadiusConnectionState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_CsbRadiusConnectionState_Type.__name__=_T
_CsbRadiusConnectionState_Object=MibScalar
csbRadiusConnectionState=_CsbRadiusConnectionState_Object((1,3,6,1,4,1,9,9,658,1,38),_CsbRadiusConnectionState_Type())
csbRadiusConnectionState.setMaxAccess(_C)
if mibBuilder.loadTexts:csbRadiusConnectionState.setStatus(_B)
class _CsbRadiusType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_An,1),(_Ao,2)))
_CsbRadiusType_Type.__name__=_T
_CsbRadiusType_Object=MibScalar
csbRadiusType=_CsbRadiusType_Object((1,3,6,1,4,1,9,9,658,1,39),_CsbRadiusType_Type())
csbRadiusType.setMaxAccess(_C)
if mibBuilder.loadTexts:csbRadiusType.setStatus(_B)
_CsbRadiusServerName_Type=SnmpAdminString
_CsbRadiusServerName_Object=MibScalar
csbRadiusServerName=_CsbRadiusServerName_Object((1,3,6,1,4,1,9,9,658,1,40),_CsbRadiusServerName_Type())
csbRadiusServerName.setMaxAccess(_C)
if mibBuilder.loadTexts:csbRadiusServerName.setStatus(_B)
_CsbRadiusServerAddressType_Type=InetAddressType
_CsbRadiusServerAddressType_Object=MibScalar
csbRadiusServerAddressType=_CsbRadiusServerAddressType_Object((1,3,6,1,4,1,9,9,658,1,41),_CsbRadiusServerAddressType_Type())
csbRadiusServerAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:csbRadiusServerAddressType.setStatus(_B)
class _CsbRadiusServerAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_CsbRadiusServerAddress_Type.__name__=_W
_CsbRadiusServerAddress_Object=MibScalar
csbRadiusServerAddress=_CsbRadiusServerAddress_Object((1,3,6,1,4,1,9,9,658,1,42),_CsbRadiusServerAddress_Type())
csbRadiusServerAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:csbRadiusServerAddress.setStatus(_B)
_CsbRadiusServerPriority_Type=Integer32
_CsbRadiusServerPriority_Object=MibScalar
csbRadiusServerPriority=_CsbRadiusServerPriority_Object((1,3,6,1,4,1,9,9,658,1,43),_CsbRadiusServerPriority_Type())
csbRadiusServerPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:csbRadiusServerPriority.setStatus(_B)
class _CsbDiameterConnectionState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_CsbDiameterConnectionState_Type.__name__=_T
_CsbDiameterConnectionState_Object=MibScalar
csbDiameterConnectionState=_CsbDiameterConnectionState_Object((1,3,6,1,4,1,9,9,658,1,44),_CsbDiameterConnectionState_Type())
csbDiameterConnectionState.setMaxAccess(_C)
if mibBuilder.loadTexts:csbDiameterConnectionState.setStatus(_B)
class _CsbDiameterType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_An,1),(_Ao,2)))
_CsbDiameterType_Type.__name__=_T
_CsbDiameterType_Object=MibScalar
csbDiameterType=_CsbDiameterType_Object((1,3,6,1,4,1,9,9,658,1,45),_CsbDiameterType_Type())
csbDiameterType.setMaxAccess(_C)
if mibBuilder.loadTexts:csbDiameterType.setStatus(_B)
_CsbDiameterGroupName_Type=SnmpAdminString
_CsbDiameterGroupName_Object=MibScalar
csbDiameterGroupName=_CsbDiameterGroupName_Object((1,3,6,1,4,1,9,9,658,1,46),_CsbDiameterGroupName_Type())
csbDiameterGroupName.setMaxAccess(_C)
if mibBuilder.loadTexts:csbDiameterGroupName.setStatus(_B)
_CsbDiameterServerName_Type=SnmpAdminString
_CsbDiameterServerName_Object=MibScalar
csbDiameterServerName=_CsbDiameterServerName_Object((1,3,6,1,4,1,9,9,658,1,47),_CsbDiameterServerName_Type())
csbDiameterServerName.setMaxAccess(_C)
if mibBuilder.loadTexts:csbDiameterServerName.setStatus(_B)
class _CsbH248ControllerState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('attached',1),('detached',2)))
_CsbH248ControllerState_Type.__name__=_T
_CsbH248ControllerState_Object=MibScalar
csbH248ControllerState=_CsbH248ControllerState_Object((1,3,6,1,4,1,9,9,658,1,48),_CsbH248ControllerState_Type())
csbH248ControllerState.setMaxAccess(_C)
if mibBuilder.loadTexts:csbH248ControllerState.setStatus(_B)
_Csb248ControllerAddressType_Type=InetAddressType
_Csb248ControllerAddressType_Object=MibScalar
csb248ControllerAddressType=_Csb248ControllerAddressType_Object((1,3,6,1,4,1,9,9,658,1,49),_Csb248ControllerAddressType_Type())
csb248ControllerAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:csb248ControllerAddressType.setStatus(_B)
class _CsbH248ControllerAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_CsbH248ControllerAddress_Type.__name__=_W
_CsbH248ControllerAddress_Object=MibScalar
csbH248ControllerAddress=_CsbH248ControllerAddress_Object((1,3,6,1,4,1,9,9,658,1,50),_CsbH248ControllerAddress_Type())
csbH248ControllerAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:csbH248ControllerAddress.setStatus(_B)
_CsbH248ControllerPort_Type=InetPortNumber
_CsbH248ControllerPort_Object=MibScalar
csbH248ControllerPort=_CsbH248ControllerPort_Object((1,3,6,1,4,1,9,9,658,1,51),_CsbH248ControllerPort_Type())
csbH248ControllerPort.setMaxAccess(_C)
if mibBuilder.loadTexts:csbH248ControllerPort.setStatus(_B)
_CsbSourceAlertNotifEnabled_Type=TruthValue
_CsbSourceAlertNotifEnabled_Object=MibScalar
csbSourceAlertNotifEnabled=_CsbSourceAlertNotifEnabled_Object((1,3,6,1,4,1,9,9,658,1,52),_CsbSourceAlertNotifEnabled_Type())
csbSourceAlertNotifEnabled.setMaxAccess(_J)
if mibBuilder.loadTexts:csbSourceAlertNotifEnabled.setStatus(_B)
_CsbBlackListNotifEnabled_Type=TruthValue
_CsbBlackListNotifEnabled_Object=MibScalar
csbBlackListNotifEnabled=_CsbBlackListNotifEnabled_Object((1,3,6,1,4,1,9,9,658,1,53),_CsbBlackListNotifEnabled_Type())
csbBlackListNotifEnabled.setMaxAccess(_J)
if mibBuilder.loadTexts:csbBlackListNotifEnabled.setStatus(_B)
_CsbAdjacencyStatusNotifEnabled_Type=TruthValue
_CsbAdjacencyStatusNotifEnabled_Object=MibScalar
csbAdjacencyStatusNotifEnabled=_CsbAdjacencyStatusNotifEnabled_Object((1,3,6,1,4,1,9,9,658,1,54),_CsbAdjacencyStatusNotifEnabled_Type())
csbAdjacencyStatusNotifEnabled.setMaxAccess(_J)
if mibBuilder.loadTexts:csbAdjacencyStatusNotifEnabled.setStatus(_B)
_CsbServiceStateNotifEnabled_Type=TruthValue
_CsbServiceStateNotifEnabled_Object=MibScalar
csbServiceStateNotifEnabled=_CsbServiceStateNotifEnabled_Object((1,3,6,1,4,1,9,9,658,1,55),_CsbServiceStateNotifEnabled_Type())
csbServiceStateNotifEnabled.setMaxAccess(_J)
if mibBuilder.loadTexts:csbServiceStateNotifEnabled.setStatus(_B)
_CsbCongestionAlarmNotifEnabled_Type=TruthValue
_CsbCongestionAlarmNotifEnabled_Object=MibScalar
csbCongestionAlarmNotifEnabled=_CsbCongestionAlarmNotifEnabled_Object((1,3,6,1,4,1,9,9,658,1,56),_CsbCongestionAlarmNotifEnabled_Type())
csbCongestionAlarmNotifEnabled.setMaxAccess(_J)
if mibBuilder.loadTexts:csbCongestionAlarmNotifEnabled.setStatus(_B)
_CsbSLAViolationNotifEnabled_Type=TruthValue
_CsbSLAViolationNotifEnabled_Object=MibScalar
csbSLAViolationNotifEnabled=_CsbSLAViolationNotifEnabled_Object((1,3,6,1,4,1,9,9,658,1,57),_CsbSLAViolationNotifEnabled_Type())
csbSLAViolationNotifEnabled.setMaxAccess(_J)
if mibBuilder.loadTexts:csbSLAViolationNotifEnabled.setStatus(_U)
_CsbRadiusConnectionStatusNotifEnabled_Type=TruthValue
_CsbRadiusConnectionStatusNotifEnabled_Object=MibScalar
csbRadiusConnectionStatusNotifEnabled=_CsbRadiusConnectionStatusNotifEnabled_Object((1,3,6,1,4,1,9,9,658,1,58),_CsbRadiusConnectionStatusNotifEnabled_Type())
csbRadiusConnectionStatusNotifEnabled.setMaxAccess(_J)
if mibBuilder.loadTexts:csbRadiusConnectionStatusNotifEnabled.setStatus(_B)
_CsbDiameterConnectionStatusNotifEnabled_Type=TruthValue
_CsbDiameterConnectionStatusNotifEnabled_Object=MibScalar
csbDiameterConnectionStatusNotifEnabled=_CsbDiameterConnectionStatusNotifEnabled_Object((1,3,6,1,4,1,9,9,658,1,59),_CsbDiameterConnectionStatusNotifEnabled_Type())
csbDiameterConnectionStatusNotifEnabled.setMaxAccess(_J)
if mibBuilder.loadTexts:csbDiameterConnectionStatusNotifEnabled.setStatus(_B)
_CsbH248ControllerStatusNotifEnabled_Type=TruthValue
_CsbH248ControllerStatusNotifEnabled_Object=MibScalar
csbH248ControllerStatusNotifEnabled=_CsbH248ControllerStatusNotifEnabled_Object((1,3,6,1,4,1,9,9,658,1,60),_CsbH248ControllerStatusNotifEnabled_Type())
csbH248ControllerStatusNotifEnabled.setMaxAccess(_J)
if mibBuilder.loadTexts:csbH248ControllerStatusNotifEnabled.setStatus(_B)
_CsbSLAPolicyLimitRev1_Type=Counter64
_CsbSLAPolicyLimitRev1_Object=MibScalar
csbSLAPolicyLimitRev1=_CsbSLAPolicyLimitRev1_Object((1,3,6,1,4,1,9,9,658,1,61),_CsbSLAPolicyLimitRev1_Type())
csbSLAPolicyLimitRev1.setMaxAccess(_C)
if mibBuilder.loadTexts:csbSLAPolicyLimitRev1.setStatus(_B)
_CsbSLACurrentUsageRev1_Type=Counter64
_CsbSLACurrentUsageRev1_Object=MibScalar
csbSLACurrentUsageRev1=_CsbSLACurrentUsageRev1_Object((1,3,6,1,4,1,9,9,658,1,62),_CsbSLACurrentUsageRev1_Type())
csbSLACurrentUsageRev1.setMaxAccess(_C)
if mibBuilder.loadTexts:csbSLACurrentUsageRev1.setStatus(_B)
_CsbSLAViolationNotifEnabledRev1_Type=TruthValue
_CsbSLAViolationNotifEnabledRev1_Object=MibScalar
csbSLAViolationNotifEnabledRev1=_CsbSLAViolationNotifEnabledRev1_Object((1,3,6,1,4,1,9,9,658,1,63),_CsbSLAViolationNotifEnabledRev1_Type())
csbSLAViolationNotifEnabledRev1.setMaxAccess(_J)
if mibBuilder.loadTexts:csbSLAViolationNotifEnabledRev1.setStatus(_B)
_CsbQOSAlertCurrentValue_Type=Unsigned32
_CsbQOSAlertCurrentValue_Object=MibScalar
csbQOSAlertCurrentValue=_CsbQOSAlertCurrentValue_Object((1,3,6,1,4,1,9,9,658,1,64),_CsbQOSAlertCurrentValue_Type())
csbQOSAlertCurrentValue.setMaxAccess(_C)
if mibBuilder.loadTexts:csbQOSAlertCurrentValue.setStatus(_B)
_CsbQOSAlertCurrentLevel_Type=CiscoAlarmSeverity
_CsbQOSAlertCurrentLevel_Object=MibScalar
csbQOSAlertCurrentLevel=_CsbQOSAlertCurrentLevel_Object((1,3,6,1,4,1,9,9,658,1,65),_CsbQOSAlertCurrentLevel_Type())
csbQOSAlertCurrentLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:csbQOSAlertCurrentLevel.setStatus(_B)
_CsbQOSAlertPreviousLevel_Type=CiscoAlarmSeverity
_CsbQOSAlertPreviousLevel_Object=MibScalar
csbQOSAlertPreviousLevel=_CsbQOSAlertPreviousLevel_Object((1,3,6,1,4,1,9,9,658,1,66),_CsbQOSAlertPreviousLevel_Type())
csbQOSAlertPreviousLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:csbQOSAlertPreviousLevel.setStatus(_B)
_CsbQOSNormalAlertCount_Type=Counter32
_CsbQOSNormalAlertCount_Object=MibScalar
csbQOSNormalAlertCount=_CsbQOSNormalAlertCount_Object((1,3,6,1,4,1,9,9,658,1,67),_CsbQOSNormalAlertCount_Type())
csbQOSNormalAlertCount.setMaxAccess(_C)
if mibBuilder.loadTexts:csbQOSNormalAlertCount.setStatus(_B)
if mibBuilder.loadTexts:csbQOSNormalAlertCount.setUnits(_c)
_CsbQOSMinorAlertCount_Type=Counter32
_CsbQOSMinorAlertCount_Object=MibScalar
csbQOSMinorAlertCount=_CsbQOSMinorAlertCount_Object((1,3,6,1,4,1,9,9,658,1,68),_CsbQOSMinorAlertCount_Type())
csbQOSMinorAlertCount.setMaxAccess(_C)
if mibBuilder.loadTexts:csbQOSMinorAlertCount.setStatus(_B)
if mibBuilder.loadTexts:csbQOSMinorAlertCount.setUnits(_c)
_CsbQOSCriticalAlertCount_Type=Counter32
_CsbQOSCriticalAlertCount_Object=MibScalar
csbQOSCriticalAlertCount=_CsbQOSCriticalAlertCount_Object((1,3,6,1,4,1,9,9,658,1,69),_CsbQOSCriticalAlertCount_Type())
csbQOSCriticalAlertCount.setMaxAccess(_C)
if mibBuilder.loadTexts:csbQOSCriticalAlertCount.setStatus(_B)
if mibBuilder.loadTexts:csbQOSCriticalAlertCount.setUnits(_c)
_CsbQOSMajorAlertCount_Type=Counter32
_CsbQOSMajorAlertCount_Object=MibScalar
csbQOSMajorAlertCount=_CsbQOSMajorAlertCount_Object((1,3,6,1,4,1,9,9,658,1,70),_CsbQOSMajorAlertCount_Type())
csbQOSMajorAlertCount.setMaxAccess(_C)
if mibBuilder.loadTexts:csbQOSMajorAlertCount.setStatus(_B)
if mibBuilder.loadTexts:csbQOSMajorAlertCount.setUnits(_c)
_CsbQOSAlertType_Type=CsbQOSAlertScopeType
_CsbQOSAlertType_Object=MibScalar
csbQOSAlertType=_CsbQOSAlertType_Object((1,3,6,1,4,1,9,9,658,1,71),_CsbQOSAlertType_Type())
csbQOSAlertType.setMaxAccess(_C)
if mibBuilder.loadTexts:csbQOSAlertType.setStatus(_B)
_CsbQOSAlertSummaryPeriod_Type=CiscoSbcPeriodicStatsInterval
_CsbQOSAlertSummaryPeriod_Object=MibScalar
csbQOSAlertSummaryPeriod=_CsbQOSAlertSummaryPeriod_Object((1,3,6,1,4,1,9,9,658,1,72),_CsbQOSAlertSummaryPeriod_Type())
csbQOSAlertSummaryPeriod.setMaxAccess(_C)
if mibBuilder.loadTexts:csbQOSAlertSummaryPeriod.setStatus(_B)
_CsbQOSAlertUnansweredCallRatioNotifEnabled_Type=TruthValue
_CsbQOSAlertUnansweredCallRatioNotifEnabled_Object=MibScalar
csbQOSAlertUnansweredCallRatioNotifEnabled=_CsbQOSAlertUnansweredCallRatioNotifEnabled_Object((1,3,6,1,4,1,9,9,658,1,73),_CsbQOSAlertUnansweredCallRatioNotifEnabled_Type())
csbQOSAlertUnansweredCallRatioNotifEnabled.setMaxAccess(_J)
if mibBuilder.loadTexts:csbQOSAlertUnansweredCallRatioNotifEnabled.setStatus(_B)
_CsbQOSAlertPercentPktDropNotifEnabled_Type=TruthValue
_CsbQOSAlertPercentPktDropNotifEnabled_Object=MibScalar
csbQOSAlertPercentPktDropNotifEnabled=_CsbQOSAlertPercentPktDropNotifEnabled_Object((1,3,6,1,4,1,9,9,658,1,74),_CsbQOSAlertPercentPktDropNotifEnabled_Type())
csbQOSAlertPercentPktDropNotifEnabled.setMaxAccess(_J)
if mibBuilder.loadTexts:csbQOSAlertPercentPktDropNotifEnabled.setStatus(_B)
_CsbQOSAlertRoundTripDelayNotifEnabled_Type=TruthValue
_CsbQOSAlertRoundTripDelayNotifEnabled_Object=MibScalar
csbQOSAlertRoundTripDelayNotifEnabled=_CsbQOSAlertRoundTripDelayNotifEnabled_Object((1,3,6,1,4,1,9,9,658,1,75),_CsbQOSAlertRoundTripDelayNotifEnabled_Type())
csbQOSAlertRoundTripDelayNotifEnabled.setMaxAccess(_J)
if mibBuilder.loadTexts:csbQOSAlertRoundTripDelayNotifEnabled.setStatus(_B)
_CsbQOSAlertMoscqeNotifEnabled_Type=TruthValue
_CsbQOSAlertMoscqeNotifEnabled_Object=MibScalar
csbQOSAlertMoscqeNotifEnabled=_CsbQOSAlertMoscqeNotifEnabled_Object((1,3,6,1,4,1,9,9,658,1,76),_CsbQOSAlertMoscqeNotifEnabled_Type())
csbQOSAlertMoscqeNotifEnabled.setMaxAccess(_J)
if mibBuilder.loadTexts:csbQOSAlertMoscqeNotifEnabled.setStatus(_B)
_CsbQOSAlertLocalJitterNotifEnabled_Type=TruthValue
_CsbQOSAlertLocalJitterNotifEnabled_Object=MibScalar
csbQOSAlertLocalJitterNotifEnabled=_CsbQOSAlertLocalJitterNotifEnabled_Object((1,3,6,1,4,1,9,9,658,1,77),_CsbQOSAlertLocalJitterNotifEnabled_Type())
csbQOSAlertLocalJitterNotifEnabled.setMaxAccess(_J)
if mibBuilder.loadTexts:csbQOSAlertLocalJitterNotifEnabled.setStatus(_B)
_CsbQOSAlertRemoteJitterNotifEnabled_Type=TruthValue
_CsbQOSAlertRemoteJitterNotifEnabled_Object=MibScalar
csbQOSAlertRemoteJitterNotifEnabled=_CsbQOSAlertRemoteJitterNotifEnabled_Object((1,3,6,1,4,1,9,9,658,1,78),_CsbQOSAlertRemoteJitterNotifEnabled_Type())
csbQOSAlertRemoteJitterNotifEnabled.setMaxAccess(_J)
if mibBuilder.loadTexts:csbQOSAlertRemoteJitterNotifEnabled.setStatus(_B)
_CsbQOSAlertPercentPktLostNotifEnabled_Type=TruthValue
_CsbQOSAlertPercentPktLostNotifEnabled_Object=MibScalar
csbQOSAlertPercentPktLostNotifEnabled=_CsbQOSAlertPercentPktLostNotifEnabled_Object((1,3,6,1,4,1,9,9,658,1,79),_CsbQOSAlertPercentPktLostNotifEnabled_Type())
csbQOSAlertPercentPktLostNotifEnabled.setMaxAccess(_J)
if mibBuilder.loadTexts:csbQOSAlertPercentPktLostNotifEnabled.setStatus(_B)
_CiscoSessBorderCtrlrMIBConform_ObjectIdentity=ObjectIdentity
ciscoSessBorderCtrlrMIBConform=_CiscoSessBorderCtrlrMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,658,2))
_CiscoSessBorderCtrlrMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoSessBorderCtrlrMIBCompliances=_CiscoSessBorderCtrlrMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,658,2,1))
_CiscoSessBorderCtrlrMIBGroups_ObjectIdentity=ObjectIdentity
ciscoSessBorderCtrlrMIBGroups=_CiscoSessBorderCtrlrMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,658,2,2))
csbNotificationManadatoryParams=ObjectGroup((1,3,6,1,4,1,9,9,658,2,2,2))
csbNotificationManadatoryParams.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I)))
if mibBuilder.loadTexts:csbNotificationManadatoryParams.setStatus(_B)
csbSourceAlertGroup=ObjectGroup((1,3,6,1,4,1,9,9,658,2,2,3))
csbSourceAlertGroup.setObjects(*((_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v)))
if mibBuilder.loadTexts:csbSourceAlertGroup.setStatus(_B)
csbDynamicBlackListGroup=ObjectGroup((1,3,6,1,4,1,9,9,658,2,2,4))
csbDynamicBlackListGroup.setObjects(*((_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2)))
if mibBuilder.loadTexts:csbDynamicBlackListGroup.setStatus(_B)
csbAdjacencyGroup=ObjectGroup((1,3,6,1,4,1,9,9,658,2,2,5))
csbAdjacencyGroup.setObjects(*((_A,_A3),(_A,_K),(_A,_A4),(_A,_A5)))
if mibBuilder.loadTexts:csbAdjacencyGroup.setStatus(_B)
csbSBCServiceGroup=ObjectGroup((1,3,6,1,4,1,9,9,658,2,2,6))
csbSBCServiceGroup.setObjects(*((_A,_A6),(_A,_A7)))
if mibBuilder.loadTexts:csbSBCServiceGroup.setStatus(_B)
csbCongestionGroup=ObjectGroup((1,3,6,1,4,1,9,9,658,2,2,7))
csbCongestionGroup.setObjects(*((_A,_A8),(_A,_A9)))
if mibBuilder.loadTexts:csbCongestionGroup.setStatus(_B)
csbSLAGroup=ObjectGroup((1,3,6,1,4,1,9,9,658,2,2,8))
csbSLAGroup.setObjects(*((_A,_X),(_A,_Y),(_A,_AA),(_A,_AB),(_A,_Z),(_A,_a)))
if mibBuilder.loadTexts:csbSLAGroup.setStatus(_U)
csbRadiusConnectionGroup=ObjectGroup((1,3,6,1,4,1,9,9,658,2,2,9))
csbRadiusConnectionGroup.setObjects(*((_A,_AC),(_A,_AD),(_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH)))
if mibBuilder.loadTexts:csbRadiusConnectionGroup.setStatus(_B)
csbDiameterConnectionGroup=ObjectGroup((1,3,6,1,4,1,9,9,658,2,2,10))
csbDiameterConnectionGroup.setObjects(*((_A,_AI),(_A,_AJ),(_A,_AK),(_A,_AL)))
if mibBuilder.loadTexts:csbDiameterConnectionGroup.setStatus(_B)
csbH248StatusGroup=ObjectGroup((1,3,6,1,4,1,9,9,658,2,2,11))
csbH248StatusGroup.setObjects(*((_A,_AM),(_A,_AN),(_A,_AO),(_A,_AP)))
if mibBuilder.loadTexts:csbH248StatusGroup.setStatus(_B)
csbNotifEnabledGroup=ObjectGroup((1,3,6,1,4,1,9,9,658,2,2,12))
csbNotifEnabledGroup.setObjects(*((_A,_AQ),(_A,_AR),(_A,_AS),(_A,_AT),(_A,_AU),(_A,_Ap),(_A,_AV),(_A,_AW),(_A,_AX)))
if mibBuilder.loadTexts:csbNotifEnabledGroup.setStatus(_U)
csbSLAGroupRev1=ObjectGroup((1,3,6,1,4,1,9,9,658,2,2,14))
csbSLAGroupRev1.setObjects(*((_A,_X),(_A,_Y),(_A,_AY),(_A,_AZ),(_A,_Z),(_A,_a)))
if mibBuilder.loadTexts:csbSLAGroupRev1.setStatus(_B)
csbNotifEnabledGroupRev1=ObjectGroup((1,3,6,1,4,1,9,9,658,2,2,15))
csbNotifEnabledGroupRev1.setObjects(*((_A,_AQ),(_A,_AR),(_A,_AS),(_A,_AT),(_A,_AU),(_A,_Aq),(_A,_AV),(_A,_AW),(_A,_AX)))
if mibBuilder.loadTexts:csbNotifEnabledGroupRev1.setStatus(_B)
csbQOSAlertGroup=ObjectGroup((1,3,6,1,4,1,9,9,658,2,2,16))
csbQOSAlertGroup.setObjects(*((_A,_L),(_A,_V),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S)))
if mibBuilder.loadTexts:csbQOSAlertGroup.setStatus(_B)
csbNotifEnabledGroupSup1=ObjectGroup((1,3,6,1,4,1,9,9,658,2,2,18))
csbNotifEnabledGroupSup1.setObjects(*((_A,_Ar),(_A,_As),(_A,_At),(_A,_Au),(_A,_Av),(_A,_Aw),(_A,_Ax)))
if mibBuilder.loadTexts:csbNotifEnabledGroupSup1.setStatus(_B)
csbSourceAlertEvent=NotificationType((1,3,6,1,4,1,9,9,658,0,1))
csbSourceAlertEvent.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_m),(_A,_n),(_A,_o),(_A,_v),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_I)))
if mibBuilder.loadTexts:csbSourceAlertEvent.setStatus(_B)
csbDynamicBlackListEvent=NotificationType((1,3,6,1,4,1,9,9,658,0,2))
csbDynamicBlackListEvent.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_I)))
if mibBuilder.loadTexts:csbDynamicBlackListEvent.setStatus(_B)
csbAdjacencyStatus=NotificationType((1,3,6,1,4,1,9,9,658,0,3))
csbAdjacencyStatus.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_A5),(_A,_A3),(_A,_K),(_A,_A4),(_A,_I)))
if mibBuilder.loadTexts:csbAdjacencyStatus.setStatus(_B)
csbServiceStateEvent=NotificationType((1,3,6,1,4,1,9,9,658,0,4))
csbServiceStateEvent.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_A7),(_A,_A6),(_A,_I)))
if mibBuilder.loadTexts:csbServiceStateEvent.setStatus(_B)
csbSystemCongestionAlarmEvent=NotificationType((1,3,6,1,4,1,9,9,658,0,5))
csbSystemCongestionAlarmEvent.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_A9),(_A,_A8),(_A,_I)))
if mibBuilder.loadTexts:csbSystemCongestionAlarmEvent.setStatus(_B)
csbSLAViolation=NotificationType((1,3,6,1,4,1,9,9,658,0,6))
csbSLAViolation.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_X),(_A,_Y),(_A,_AA),(_A,_AB),(_A,_Z),(_A,_a),(_A,_I)))
if mibBuilder.loadTexts:csbSLAViolation.setStatus(_U)
csbRadiusConnectionStatus=NotificationType((1,3,6,1,4,1,9,9,658,0,7))
csbRadiusConnectionStatus.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_AC),(_A,_AD),(_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_I)))
if mibBuilder.loadTexts:csbRadiusConnectionStatus.setStatus(_B)
csbDiameterConnectionStatus=NotificationType((1,3,6,1,4,1,9,9,658,0,8))
csbDiameterConnectionStatus.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_AI),(_A,_AJ),(_A,_AK),(_A,_AL),(_A,_I)))
if mibBuilder.loadTexts:csbDiameterConnectionStatus.setStatus(_B)
csbH248ControllerStatus=NotificationType((1,3,6,1,4,1,9,9,658,0,9))
csbH248ControllerStatus.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_AM),(_A,_AN),(_A,_AO),(_A,_AP),(_A,_I)))
if mibBuilder.loadTexts:csbH248ControllerStatus.setStatus(_B)
csbSLAViolationRev1=NotificationType((1,3,6,1,4,1,9,9,658,0,10))
csbSLAViolationRev1.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_X),(_A,_Y),(_A,_AY),(_A,_AZ),(_A,_Z),(_A,_a),(_A,_I)))
if mibBuilder.loadTexts:csbSLAViolationRev1.setStatus(_B)
csbQOSUnansweredCallRatioEvent=NotificationType((1,3,6,1,4,1,9,9,658,0,11))
csbQOSUnansweredCallRatioEvent.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_R),(_A,_K),(_A,_S),(_A,_L),(_A,_V),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_I),(_A,_Q)))
if mibBuilder.loadTexts:csbQOSUnansweredCallRatioEvent.setStatus(_B)
csbQOSUnansweredCallRatioClearEvent=NotificationType((1,3,6,1,4,1,9,9,658,0,12))
csbQOSUnansweredCallRatioClearEvent.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_R),(_A,_K),(_A,_S),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_I),(_A,_Q)))
if mibBuilder.loadTexts:csbQOSUnansweredCallRatioClearEvent.setStatus(_B)
csbQOSPercentPktLostEvent=NotificationType((1,3,6,1,4,1,9,9,658,0,13))
csbQOSPercentPktLostEvent.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_R),(_A,_K),(_A,_S),(_A,_L),(_A,_V),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_I),(_A,_Q)))
if mibBuilder.loadTexts:csbQOSPercentPktLostEvent.setStatus(_B)
csbQOSPercentPktLostClearEvent=NotificationType((1,3,6,1,4,1,9,9,658,0,14))
csbQOSPercentPktLostClearEvent.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_R),(_A,_K),(_A,_S),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_I),(_A,_Q)))
if mibBuilder.loadTexts:csbQOSPercentPktLostClearEvent.setStatus(_B)
csbQOSPercentPktDropEvent=NotificationType((1,3,6,1,4,1,9,9,658,0,15))
csbQOSPercentPktDropEvent.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_R),(_A,_K),(_A,_S),(_A,_L),(_A,_V),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_I),(_A,_Q)))
if mibBuilder.loadTexts:csbQOSPercentPktDropEvent.setStatus(_B)
csbQOSPercentPktDropClearEvent=NotificationType((1,3,6,1,4,1,9,9,658,0,16))
csbQOSPercentPktDropClearEvent.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_R),(_A,_K),(_A,_S),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_I),(_A,_Q)))
if mibBuilder.loadTexts:csbQOSPercentPktDropClearEvent.setStatus(_B)
csbQOSRoundTripDelayEvent=NotificationType((1,3,6,1,4,1,9,9,658,0,17))
csbQOSRoundTripDelayEvent.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_R),(_A,_K),(_A,_S),(_A,_L),(_A,_V),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_I),(_A,_Q)))
if mibBuilder.loadTexts:csbQOSRoundTripDelayEvent.setStatus(_B)
csbQOSRoundTripDelayClearEvent=NotificationType((1,3,6,1,4,1,9,9,658,0,18))
csbQOSRoundTripDelayClearEvent.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_R),(_A,_K),(_A,_S),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_I),(_A,_Q)))
if mibBuilder.loadTexts:csbQOSRoundTripDelayClearEvent.setStatus(_B)
csbQOSLocalJitterEvent=NotificationType((1,3,6,1,4,1,9,9,658,0,19))
csbQOSLocalJitterEvent.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_R),(_A,_K),(_A,_S),(_A,_L),(_A,_V),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_I),(_A,_Q)))
if mibBuilder.loadTexts:csbQOSLocalJitterEvent.setStatus(_B)
csbQOSLocalJitterClearEvent=NotificationType((1,3,6,1,4,1,9,9,658,0,20))
csbQOSLocalJitterClearEvent.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_R),(_A,_K),(_A,_S),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_I),(_A,_Q)))
if mibBuilder.loadTexts:csbQOSLocalJitterClearEvent.setStatus(_B)
csbQOSRemoteJitterEvent=NotificationType((1,3,6,1,4,1,9,9,658,0,21))
csbQOSRemoteJitterEvent.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_R),(_A,_K),(_A,_S),(_A,_L),(_A,_V),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_I),(_A,_Q)))
if mibBuilder.loadTexts:csbQOSRemoteJitterEvent.setStatus(_B)
csbQOSRemoteJitterClearEvent=NotificationType((1,3,6,1,4,1,9,9,658,0,22))
csbQOSRemoteJitterClearEvent.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_R),(_A,_K),(_A,_S),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_I),(_A,_Q)))
if mibBuilder.loadTexts:csbQOSRemoteJitterClearEvent.setStatus(_B)
csbQOSMoscqeEvent=NotificationType((1,3,6,1,4,1,9,9,658,0,23))
csbQOSMoscqeEvent.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_R),(_A,_K),(_A,_S),(_A,_L),(_A,_V),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_I),(_A,_Q)))
if mibBuilder.loadTexts:csbQOSMoscqeEvent.setStatus(_B)
csbQOSMoscqeClearEvent=NotificationType((1,3,6,1,4,1,9,9,658,0,24))
csbQOSMoscqeClearEvent.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_R),(_A,_K),(_A,_S),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_I),(_A,_Q)))
if mibBuilder.loadTexts:csbQOSMoscqeClearEvent.setStatus(_B)
csbNotificationGroup=NotificationGroup((1,3,6,1,4,1,9,9,658,2,2,1))
csbNotificationGroup.setObjects(*((_A,_Aa),(_A,_Ab),(_A,_Ac),(_A,_Ad),(_A,_Ae),(_A,_Ay),(_A,_Af),(_A,_Ag),(_A,_Ah)))
if mibBuilder.loadTexts:csbNotificationGroup.setStatus(_U)
csbNotificationGroupRev1=NotificationGroup((1,3,6,1,4,1,9,9,658,2,2,13))
csbNotificationGroupRev1.setObjects(*((_A,_Aa),(_A,_Ab),(_A,_Ac),(_A,_Ad),(_A,_Ae),(_A,_Az),(_A,_Af),(_A,_Ag),(_A,_Ah)))
if mibBuilder.loadTexts:csbNotificationGroupRev1.setStatus(_B)
csbNotificationGroupSup1=NotificationGroup((1,3,6,1,4,1,9,9,658,2,2,17))
csbNotificationGroupSup1.setObjects(*((_A,_A_),(_A,_B0),(_A,_B1),(_A,_B2),(_A,_B3),(_A,_B4),(_A,_B5),(_A,_B6),(_A,_B7),(_A,_B8),(_A,_B9),(_A,_BA),(_A,_BB),(_A,_BC)))
if mibBuilder.loadTexts:csbNotificationGroupSup1.setStatus(_B)
csbCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,658,2,1,1))
csbCompliance.setObjects(*((_A,_d),(_A,_e),(_A,_BD),(_A,_f),(_A,_g),(_A,_h),(_A,_BE),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_BF)))
if mibBuilder.loadTexts:csbCompliance.setStatus(_U)
csbComplianceRev1=ModuleCompliance((1,3,6,1,4,1,9,9,658,2,1,2))
csbComplianceRev1.setObjects(*((_A,_d),(_A,_e),(_A,_Ai),(_A,_f),(_A,_g),(_A,_h),(_A,_Aj),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_Ak)))
if mibBuilder.loadTexts:csbComplianceRev1.setStatus(_U)
csbComplianceRev2=ModuleCompliance((1,3,6,1,4,1,9,9,658,2,1,3))
csbComplianceRev2.setObjects(*((_A,_d),(_A,_e),(_A,_Ai),(_A,_f),(_A,_g),(_A,_h),(_A,_Aj),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_Ak),(_A,_BG),(_A,_BH),(_A,_BI)))
if mibBuilder.loadTexts:csbComplianceRev2.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'CsbQOSAlertScopeType':CsbQOSAlertScopeType,'CsbDynamicBlackListedSrcSubFamily':CsbDynamicBlackListedSrcSubFamily,'CsbDynamicBlackListedTransPortType':CsbDynamicBlackListedTransPortType,'ciscoSessBorderCtrlrEventMIB':ciscoSessBorderCtrlrEventMIB,'ciscoSessBorderCtrlrMIBNotifs':ciscoSessBorderCtrlrMIBNotifs,_Aa:csbSourceAlertEvent,_Ab:csbDynamicBlackListEvent,_Ac:csbAdjacencyStatus,_Ad:csbServiceStateEvent,_Ae:csbSystemCongestionAlarmEvent,_Ay:csbSLAViolation,_Af:csbRadiusConnectionStatus,_Ag:csbDiameterConnectionStatus,_Ah:csbH248ControllerStatus,_Az:csbSLAViolationRev1,_BC:csbQOSUnansweredCallRatioEvent,_A_:csbQOSUnansweredCallRatioClearEvent,_B0:csbQOSPercentPktLostEvent,_B1:csbQOSPercentPktLostClearEvent,_B2:csbQOSPercentPktDropEvent,_B3:csbQOSPercentPktDropClearEvent,_B4:csbQOSRoundTripDelayEvent,_B5:csbQOSRoundTripDelayClearEvent,_B6:csbQOSLocalJitterEvent,_B7:csbQOSLocalJitterClearEvent,_B8:csbQOSRemoteJitterEvent,_B9:csbQOSRemoteJitterClearEvent,_BA:csbQOSMoscqeEvent,_BB:csbQOSMoscqeClearEvent,'ciscoSessBorderCtrlrMIBObjects':ciscoSessBorderCtrlrMIBObjects,_D:csbAlarmSubsystem,_E:csbAlarmSeverity,_F:csbAlarmID,_G:csbAlarmTime,_H:csbSBCServiceName,_I:csbAlarmDescription,_m:csbSrcAlertVdbeId,_n:csbSrcAlertGateId,_o:csbSrcAlertFlowPairId,_v:csbSrcAlertLocalAddressType,_p:csbSrcAlertLocalAddress,_q:csbSrcAlertLocalPort,_r:csbSrcAlertRemoteAddressType,_s:csbSrcAlertRemoteAddress,_t:csbSrcAlertRemotePort,_u:csbSrcAlertVpnId,_w:csbDynamicBlackListSubFamily,_x:csbDynamicBlackListVpnId,_y:csbDynamicBlackListAddressType,_z:csbDynamicBlackListAddress,_A0:csbDynamicBlackListTransportType,_A1:csbDynamicBlackListPortNumber,_A2:csbDynamicBlackListSrcBlocked,_A3:csbAdjacencyType,_A5:csbAdjacencyState,_K:csbAdjacencyName,_A4:csbAdjacencyAccountName,_A7:csbSBCServiceState,_A6:csbSBCServiceSlot,_A9:csbCongestionAlarmType,_A8:csbCongestionAlarmState,_X:csbSLAPolicyAccountName,_Y:csbSLAPolicyScope,_AA:csbSLAPolicyLimit,_Z:csbSLAViolationEvent,_a:csbSLAPolicyRestriction,_AB:csbSLACurrentUsage,_AC:csbRadiusConnectionState,_AD:csbRadiusType,_AE:csbRadiusServerName,_AF:csbRadiusServerAddressType,_AG:csbRadiusServerAddress,_AH:csbRadiusServerPriority,_AI:csbDiameterConnectionState,_AJ:csbDiameterType,_AK:csbDiameterGroupName,_AL:csbDiameterServerName,_AM:csbH248ControllerState,_AN:csb248ControllerAddressType,_AO:csbH248ControllerAddress,_AP:csbH248ControllerPort,_AQ:csbSourceAlertNotifEnabled,_AR:csbBlackListNotifEnabled,_AS:csbAdjacencyStatusNotifEnabled,_AT:csbServiceStateNotifEnabled,_AU:csbCongestionAlarmNotifEnabled,_Ap:csbSLAViolationNotifEnabled,_AV:csbRadiusConnectionStatusNotifEnabled,_AW:csbDiameterConnectionStatusNotifEnabled,_AX:csbH248ControllerStatusNotifEnabled,_AY:csbSLAPolicyLimitRev1,_AZ:csbSLACurrentUsageRev1,_Aq:csbSLAViolationNotifEnabledRev1,_L:csbQOSAlertCurrentValue,_V:csbQOSAlertCurrentLevel,_M:csbQOSAlertPreviousLevel,_N:csbQOSNormalAlertCount,_O:csbQOSMinorAlertCount,_P:csbQOSCriticalAlertCount,_Q:csbQOSMajorAlertCount,_R:csbQOSAlertType,_S:csbQOSAlertSummaryPeriod,_Ar:csbQOSAlertUnansweredCallRatioNotifEnabled,_As:csbQOSAlertPercentPktDropNotifEnabled,_At:csbQOSAlertRoundTripDelayNotifEnabled,_Ax:csbQOSAlertMoscqeNotifEnabled,_Au:csbQOSAlertLocalJitterNotifEnabled,_Av:csbQOSAlertRemoteJitterNotifEnabled,_Aw:csbQOSAlertPercentPktLostNotifEnabled,'ciscoSessBorderCtrlrMIBConform':ciscoSessBorderCtrlrMIBConform,'ciscoSessBorderCtrlrMIBCompliances':ciscoSessBorderCtrlrMIBCompliances,'csbCompliance':csbCompliance,'csbComplianceRev1':csbComplianceRev1,'csbComplianceRev2':csbComplianceRev2,'ciscoSessBorderCtrlrMIBGroups':ciscoSessBorderCtrlrMIBGroups,_BD:csbNotificationGroup,_f:csbNotificationManadatoryParams,_d:csbSourceAlertGroup,_e:csbDynamicBlackListGroup,_g:csbAdjacencyGroup,_h:csbSBCServiceGroup,_l:csbCongestionGroup,_BE:csbSLAGroup,_i:csbRadiusConnectionGroup,_j:csbDiameterConnectionGroup,_k:csbH248StatusGroup,_BF:csbNotifEnabledGroup,_Ai:csbNotificationGroupRev1,_Aj:csbSLAGroupRev1,_Ak:csbNotifEnabledGroupRev1,_BG:csbQOSAlertGroup,_BH:csbNotificationGroupSup1,_BI:csbNotifEnabledGroupSup1})