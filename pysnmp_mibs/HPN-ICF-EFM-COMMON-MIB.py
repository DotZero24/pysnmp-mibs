_Ab='hpnicfDot3OamNotificationGroup'
_Aa='hpnicfDot3OamEventLogGroup'
_AZ='hpnicfDot3OamErrFrameSecsSummaryEventGroup'
_AY='hpnicfDot3OamErrFrameEventGroup'
_AX='hpnicfDot3OamErrFramePeriodEventGroup'
_AW='hpnicfDot3OamErrSymbolPeriodEventGroup'
_AV='hpnicfDot3OamLoopbackGroup'
_AU='hpnicfDot3OamStatsBaseGroup'
_AT='hpnicfDot3OamPeerGroup'
_AS='hpnicfDot3OamControlGroup'
_AR='hpnicfDot3OamNonThresholdEvent'
_AQ='hpnicfDot3OamThresholdEvent'
_AP='hpnicfDot3OamErrFrameSecsEvNotifEnable'
_AO='hpnicfDot3OamErrFrameSecsSummaryThreshold'
_AN='hpnicfDot3OamErrFrameSecsSummaryWindow'
_AM='hpnicfDot3OamErrFrameEvNotifEnable'
_AL='hpnicfDot3OamErrFrameThreshold'
_AK='hpnicfDot3OamErrFrameWindow'
_AJ='hpnicfDot3OamErrFramePeriodEvNotifEnable'
_AI='hpnicfDot3OamErrFramePeriodThreshold'
_AH='hpnicfDot3OamErrFramePeriodWindow'
_AG='hpnicfDot3OamErrSymPeriodEvNotifEnable'
_AF='hpnicfDot3OamErrSymPeriodThresholdLo'
_AE='hpnicfDot3OamErrSymPeriodThresholdHi'
_AD='hpnicfDot3OamErrSymPeriodWindowLo'
_AC='hpnicfDot3OamErrSymPeriodWindowHi'
_AB='hpnicfDot3OamLoopbackIgnoreRx'
_AA='hpnicfDot3OamLoopbackStatus'
_A9='hpnicfDot3OamLoopbackCommand'
_A8='hpnicfDot3OamFramesLostDueToOam'
_A7='hpnicfDot3OamUnsupportedCodesRx'
_A6='hpnicfDot3OamUnsupportedCodesTx'
_A5='hpnicfDot3OamOrgSpecificRx'
_A4='hpnicfDot3OamOrgSpecificTx'
_A3='hpnicfDot3OamVariableResponseRx'
_A2='hpnicfDot3OamVariableResponseTx'
_A1='hpnicfDot3OamVariableRequestRx'
_A0='hpnicfDot3OamVariableRequestTx'
_z='hpnicfDot3OamLoopbackControlRx'
_y='hpnicfDot3OamLoopbackControlTx'
_x='hpnicfDot3OamDuplicateEventNotificationRx'
_w='hpnicfDot3OamDuplicateEventNotificationTx'
_v='hpnicfDot3OamUniqueEventNotificationRx'
_u='hpnicfDot3OamUniqueEventNotificationTx'
_t='hpnicfDot3OamInformationRx'
_s='hpnicfDot3OamInformationTx'
_r='hpnicfDot3OamPeerConfigRevision'
_q='hpnicfDot3OamPeerMaxOamPduSize'
_p='hpnicfDot3OamPeerFunctionsSupported'
_o='hpnicfDot3OamPeerMode'
_n='hpnicfDot3OamPeerVendorInfo'
_m='hpnicfDot3OamPeerVendorOui'
_l='hpnicfDot3OamPeerMacAddress'
_k='hpnicfDot3OamPeerStatus'
_j='hpnicfDot3OamFunctionsSupported'
_i='hpnicfDot3OamConfigRevision'
_h='hpnicfDot3OamMaxOamPduSize'
_g='hpnicfDot3OamMode'
_f='hpnicfDot3OamOperStatus'
_e='hpnicfDot3OamAdminState'
_d='hpnicfDot3OamEventLogIndex'
_c='noLoopback'
_b='unknown'
_a='variableSupport'
_Z='eventSupport'
_Y='loopbackSupport'
_X='unidirectionalSupport'
_W='passive'
_V='hpnicfDot3OamEventLogRunningTotal'
_U='hpnicfDot3OamEventLogValue'
_T='hpnicfDot3OamEventLogThresholdLo'
_S='hpnicfDot3OamEventLogThresholdHi'
_R='hpnicfDot3OamEventLogWindowLo'
_Q='hpnicfDot3OamEventLogWindowHi'
_P='active'
_O='Bits'
_N='hpnicfDot3OamEventLogEventTotal'
_M='hpnicfDot3OamEventLogLocation'
_L='hpnicfDot3OamEventLogType'
_K='hpnicfDot3OamEventLogOui'
_J='hpnicfDot3OamEventLogTimestamp'
_I='enabled'
_H='disabled'
_G='ifIndex'
_F='IF-MIB'
_E='read-write'
_D='Integer32'
_C='read-only'
_B='current'
_A='HPN-ICF-EFM-COMMON-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
CounterBasedGauge64,=mibBuilder.importSymbols('HCNUM-TC','CounterBasedGauge64')
hpnicfEpon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfEpon')
ifIndex,=mibBuilder.importSymbols(_F,_G)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI',_O,'Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','mib-2')
DateAndTime,DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','TextualConvention')
hpnicfEfmOamMIB=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,42,3))
if mibBuilder.loadTexts:hpnicfEfmOamMIB.setRevisions(('2004-10-24 00:00',))
class Dot3Oui(TextualConvention,OctetString):status=_B;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,3));fixedLength=3
_HpnicfDot3OamMIB_ObjectIdentity=ObjectIdentity
hpnicfDot3OamMIB=_HpnicfDot3OamMIB_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,42,3,1))
_HpnicfDot3OamTable_Object=MibTable
hpnicfDot3OamTable=_HpnicfDot3OamTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,3,1,1))
if mibBuilder.loadTexts:hpnicfDot3OamTable.setStatus(_B)
_HpnicfDot3OamEntry_Object=MibTableRow
hpnicfDot3OamEntry=_HpnicfDot3OamEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,3,1,1,1))
hpnicfDot3OamEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:hpnicfDot3OamEntry.setStatus(_B)
class _HpnicfDot3OamAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_HpnicfDot3OamAdminState_Type.__name__=_D
_HpnicfDot3OamAdminState_Object=MibTableColumn
hpnicfDot3OamAdminState=_HpnicfDot3OamAdminState_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,3,1,1,1,1),_HpnicfDot3OamAdminState_Type())
hpnicfDot3OamAdminState.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfDot3OamAdminState.setStatus(_B)
class _HpnicfDot3OamOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_H,1),('linkfault',2),('passiveWait',3),('activeSendLocal',4),('sendLocalAndRemote',5),('sendLocalAndRemoteOk',6),('oamPeeringLocallyRejected',7),('oamPeeringRemotelyRejected',8),('operational',9)))
_HpnicfDot3OamOperStatus_Type.__name__=_D
_HpnicfDot3OamOperStatus_Object=MibTableColumn
hpnicfDot3OamOperStatus=_HpnicfDot3OamOperStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,3,1,1,1,2),_HpnicfDot3OamOperStatus_Type())
hpnicfDot3OamOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot3OamOperStatus.setStatus(_B)
class _HpnicfDot3OamMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_W,2)))
_HpnicfDot3OamMode_Type.__name__=_D
_HpnicfDot3OamMode_Object=MibTableColumn
hpnicfDot3OamMode=_HpnicfDot3OamMode_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,3,1,1,1,3),_HpnicfDot3OamMode_Type())
hpnicfDot3OamMode.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfDot3OamMode.setStatus(_B)
class _HpnicfDot3OamMaxOamPduSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(64,1522))
_HpnicfDot3OamMaxOamPduSize_Type.__name__=_D
_HpnicfDot3OamMaxOamPduSize_Object=MibTableColumn
hpnicfDot3OamMaxOamPduSize=_HpnicfDot3OamMaxOamPduSize_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,3,1,1,1,4),_HpnicfDot3OamMaxOamPduSize_Type())
hpnicfDot3OamMaxOamPduSize.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot3OamMaxOamPduSize.setStatus(_B)
_HpnicfDot3OamConfigRevision_Type=Unsigned32
_HpnicfDot3OamConfigRevision_Object=MibTableColumn
hpnicfDot3OamConfigRevision=_HpnicfDot3OamConfigRevision_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,3,1,1,1,5),_HpnicfDot3OamConfigRevision_Type())
hpnicfDot3OamConfigRevision.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot3OamConfigRevision.setStatus(_B)
class _HpnicfDot3OamFunctionsSupported_Type(Bits):namedValues=NamedValues(*((_X,0),(_Y,1),(_Z,2),(_a,3)))
_HpnicfDot3OamFunctionsSupported_Type.__name__=_O
_HpnicfDot3OamFunctionsSupported_Object=MibTableColumn
hpnicfDot3OamFunctionsSupported=_HpnicfDot3OamFunctionsSupported_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,3,1,1,1,6),_HpnicfDot3OamFunctionsSupported_Type())
hpnicfDot3OamFunctionsSupported.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot3OamFunctionsSupported.setStatus(_B)
_HpnicfDot3OamPeerTable_Object=MibTable
hpnicfDot3OamPeerTable=_HpnicfDot3OamPeerTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,3,1,2))
if mibBuilder.loadTexts:hpnicfDot3OamPeerTable.setStatus(_B)
_HpnicfDot3OamPeerEntry_Object=MibTableRow
hpnicfDot3OamPeerEntry=_HpnicfDot3OamPeerEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,3,1,2,1))
hpnicfDot3OamPeerEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:hpnicfDot3OamPeerEntry.setStatus(_B)
class _HpnicfDot3OamPeerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),('inactive',2)))
_HpnicfDot3OamPeerStatus_Type.__name__=_D
_HpnicfDot3OamPeerStatus_Object=MibTableColumn
hpnicfDot3OamPeerStatus=_HpnicfDot3OamPeerStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,3,1,2,1,1),_HpnicfDot3OamPeerStatus_Type())
hpnicfDot3OamPeerStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot3OamPeerStatus.setStatus(_B)
_HpnicfDot3OamPeerMacAddress_Type=MacAddress
_HpnicfDot3OamPeerMacAddress_Object=MibTableColumn
hpnicfDot3OamPeerMacAddress=_HpnicfDot3OamPeerMacAddress_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,3,1,2,1,2),_HpnicfDot3OamPeerMacAddress_Type())
hpnicfDot3OamPeerMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot3OamPeerMacAddress.setStatus(_B)
_HpnicfDot3OamPeerVendorOui_Type=Dot3Oui
_HpnicfDot3OamPeerVendorOui_Object=MibTableColumn
hpnicfDot3OamPeerVendorOui=_HpnicfDot3OamPeerVendorOui_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,3,1,2,1,3),_HpnicfDot3OamPeerVendorOui_Type())
hpnicfDot3OamPeerVendorOui.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot3OamPeerVendorOui.setStatus(_B)
_HpnicfDot3OamPeerVendorInfo_Type=Unsigned32
_HpnicfDot3OamPeerVendorInfo_Object=MibTableColumn
hpnicfDot3OamPeerVendorInfo=_HpnicfDot3OamPeerVendorInfo_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,3,1,2,1,4),_HpnicfDot3OamPeerVendorInfo_Type())
hpnicfDot3OamPeerVendorInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot3OamPeerVendorInfo.setStatus(_B)
class _HpnicfDot3OamPeerMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_P,1),(_W,2),(_b,3)))
_HpnicfDot3OamPeerMode_Type.__name__=_D
_HpnicfDot3OamPeerMode_Object=MibTableColumn
hpnicfDot3OamPeerMode=_HpnicfDot3OamPeerMode_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,3,1,2,1,5),_HpnicfDot3OamPeerMode_Type())
hpnicfDot3OamPeerMode.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot3OamPeerMode.setStatus(_B)
class _HpnicfDot3OamPeerMaxOamPduSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(64,1522))
_HpnicfDot3OamPeerMaxOamPduSize_Type.__name__=_D
_HpnicfDot3OamPeerMaxOamPduSize_Object=MibTableColumn
hpnicfDot3OamPeerMaxOamPduSize=_HpnicfDot3OamPeerMaxOamPduSize_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,3,1,2,1,6),_HpnicfDot3OamPeerMaxOamPduSize_Type())
hpnicfDot3OamPeerMaxOamPduSize.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot3OamPeerMaxOamPduSize.setStatus(_B)
_HpnicfDot3OamPeerConfigRevision_Type=Unsigned32
_HpnicfDot3OamPeerConfigRevision_Object=MibTableColumn
hpnicfDot3OamPeerConfigRevision=_HpnicfDot3OamPeerConfigRevision_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,3,1,2,1,7),_HpnicfDot3OamPeerConfigRevision_Type())
hpnicfDot3OamPeerConfigRevision.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot3OamPeerConfigRevision.setStatus(_B)
class _HpnicfDot3OamPeerFunctionsSupported_Type(Bits):namedValues=NamedValues(*((_X,0),(_Y,1),(_Z,2),(_a,3)))
_HpnicfDot3OamPeerFunctionsSupported_Type.__name__=_O
_HpnicfDot3OamPeerFunctionsSupported_Object=MibTableColumn
hpnicfDot3OamPeerFunctionsSupported=_HpnicfDot3OamPeerFunctionsSupported_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,3,1,2,1,8),_HpnicfDot3OamPeerFunctionsSupported_Type())
hpnicfDot3OamPeerFunctionsSupported.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot3OamPeerFunctionsSupported.setStatus(_B)
_HpnicfDot3OamLoopbackTable_Object=MibTable
hpnicfDot3OamLoopbackTable=_HpnicfDot3OamLoopbackTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,3,1,3))
if mibBuilder.loadTexts:hpnicfDot3OamLoopbackTable.setStatus(_B)
_HpnicfDot3OamLoopbackEntry_Object=MibTableRow
hpnicfDot3OamLoopbackEntry=_HpnicfDot3OamLoopbackEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,3,1,3,1))
hpnicfDot3OamLoopbackEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:hpnicfDot3OamLoopbackEntry.setStatus(_B)
class _HpnicfDot3OamLoopbackCommand_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_c,1),('startRemoteLoopback',2),('stopRemoteLoopback',3)))
_HpnicfDot3OamLoopbackCommand_Type.__name__=_D
_HpnicfDot3OamLoopbackCommand_Object=MibTableColumn
hpnicfDot3OamLoopbackCommand=_HpnicfDot3OamLoopbackCommand_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,3,1,3,1,1),_HpnicfDot3OamLoopbackCommand_Type())
hpnicfDot3OamLoopbackCommand.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfDot3OamLoopbackCommand.setStatus(_B)
class _HpnicfDot3OamLoopbackStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_c,1),('initiatingLoopback',2),('remoteLoopback',3),('terminatingLoopback',4),('localLoopback',5),(_b,6)))
_HpnicfDot3OamLoopbackStatus_Type.__name__=_D
_HpnicfDot3OamLoopbackStatus_Object=MibTableColumn
hpnicfDot3OamLoopbackStatus=_HpnicfDot3OamLoopbackStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,3,1,3,1,2),_HpnicfDot3OamLoopbackStatus_Type())
hpnicfDot3OamLoopbackStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot3OamLoopbackStatus.setStatus(_B)
class _HpnicfDot3OamLoopbackIgnoreRx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ignore',1),('process',2)))
_HpnicfDot3OamLoopbackIgnoreRx_Type.__name__=_D
_HpnicfDot3OamLoopbackIgnoreRx_Object=MibTableColumn
hpnicfDot3OamLoopbackIgnoreRx=_HpnicfDot3OamLoopbackIgnoreRx_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,3,1,3,1,3),_HpnicfDot3OamLoopbackIgnoreRx_Type())
hpnicfDot3OamLoopbackIgnoreRx.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfDot3OamLoopbackIgnoreRx.setStatus(_B)
_HpnicfDot3OamStatsTable_Object=MibTable
hpnicfDot3OamStatsTable=_HpnicfDot3OamStatsTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,3,1,4))
if mibBuilder.loadTexts:hpnicfDot3OamStatsTable.setStatus(_B)
_HpnicfDot3OamStatsEntry_Object=MibTableRow
hpnicfDot3OamStatsEntry=_HpnicfDot3OamStatsEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,3,1,4,1))
hpnicfDot3OamStatsEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:hpnicfDot3OamStatsEntry.setStatus(_B)
_HpnicfDot3OamInformationTx_Type=Counter32
_HpnicfDot3OamInformationTx_Object=MibTableColumn
hpnicfDot3OamInformationTx=_HpnicfDot3OamInformationTx_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,3,1,4,1,1),_HpnicfDot3OamInformationTx_Type())
hpnicfDot3OamInformationTx.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot3OamInformationTx.setStatus(_B)
_HpnicfDot3OamInformationRx_Type=Counter32
_HpnicfDot3OamInformationRx_Object=MibTableColumn
hpnicfDot3OamInformationRx=_HpnicfDot3OamInformationRx_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,3,1,4,1,2),_HpnicfDot3OamInformationRx_Type())
hpnicfDot3OamInformationRx.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot3OamInformationRx.setStatus(_B)
_HpnicfDot3OamUniqueEventNotificationTx_Type=Counter32
_HpnicfDot3OamUniqueEventNotificationTx_Object=MibTableColumn
hpnicfDot3OamUniqueEventNotificationTx=_HpnicfDot3OamUniqueEventNotificationTx_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,3,1,4,1,3),_HpnicfDot3OamUniqueEventNotificationTx_Type())
hpnicfDot3OamUniqueEventNotificationTx.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot3OamUniqueEventNotificationTx.setStatus(_B)
_HpnicfDot3OamUniqueEventNotificationRx_Type=Counter32
_HpnicfDot3OamUniqueEventNotificationRx_Object=MibTableColumn
hpnicfDot3OamUniqueEventNotificationRx=_HpnicfDot3OamUniqueEventNotificationRx_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,3,1,4,1,4),_HpnicfDot3OamUniqueEventNotificationRx_Type())
hpnicfDot3OamUniqueEventNotificationRx.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot3OamUniqueEventNotificationRx.setStatus(_B)
_HpnicfDot3OamDuplicateEventNotificationTx_Type=Counter32
_HpnicfDot3OamDuplicateEventNotificationTx_Object=MibTableColumn
hpnicfDot3OamDuplicateEventNotificationTx=_HpnicfDot3OamDuplicateEventNotificationTx_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,3,1,4,1,5),_HpnicfDot3OamDuplicateEventNotificationTx_Type())
hpnicfDot3OamDuplicateEventNotificationTx.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot3OamDuplicateEventNotificationTx.setStatus(_B)
_HpnicfDot3OamDuplicateEventNotificationRx_Type=Counter32
_HpnicfDot3OamDuplicateEventNotificationRx_Object=MibTableColumn
hpnicfDot3OamDuplicateEventNotificationRx=_HpnicfDot3OamDuplicateEventNotificationRx_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,3,1,4,1,6),_HpnicfDot3OamDuplicateEventNotificationRx_Type())
hpnicfDot3OamDuplicateEventNotificationRx.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot3OamDuplicateEventNotificationRx.setStatus(_B)
_HpnicfDot3OamLoopbackControlTx_Type=Counter32
_HpnicfDot3OamLoopbackControlTx_Object=MibTableColumn
hpnicfDot3OamLoopbackControlTx=_HpnicfDot3OamLoopbackControlTx_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,3,1,4,1,7),_HpnicfDot3OamLoopbackControlTx_Type())
hpnicfDot3OamLoopbackControlTx.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot3OamLoopbackControlTx.setStatus(_B)
_HpnicfDot3OamLoopbackControlRx_Type=Counter32
_HpnicfDot3OamLoopbackControlRx_Object=MibTableColumn
hpnicfDot3OamLoopbackControlRx=_HpnicfDot3OamLoopbackControlRx_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,3,1,4,1,8),_HpnicfDot3OamLoopbackControlRx_Type())
hpnicfDot3OamLoopbackControlRx.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot3OamLoopbackControlRx.setStatus(_B)
_HpnicfDot3OamVariableRequestTx_Type=Counter32
_HpnicfDot3OamVariableRequestTx_Object=MibTableColumn
hpnicfDot3OamVariableRequestTx=_HpnicfDot3OamVariableRequestTx_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,3,1,4,1,9),_HpnicfDot3OamVariableRequestTx_Type())
hpnicfDot3OamVariableRequestTx.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot3OamVariableRequestTx.setStatus(_B)
_HpnicfDot3OamVariableRequestRx_Type=Counter32
_HpnicfDot3OamVariableRequestRx_Object=MibTableColumn
hpnicfDot3OamVariableRequestRx=_HpnicfDot3OamVariableRequestRx_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,3,1,4,1,10),_HpnicfDot3OamVariableRequestRx_Type())
hpnicfDot3OamVariableRequestRx.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot3OamVariableRequestRx.setStatus(_B)
_HpnicfDot3OamVariableResponseTx_Type=Counter32
_HpnicfDot3OamVariableResponseTx_Object=MibTableColumn
hpnicfDot3OamVariableResponseTx=_HpnicfDot3OamVariableResponseTx_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,3,1,4,1,11),_HpnicfDot3OamVariableResponseTx_Type())
hpnicfDot3OamVariableResponseTx.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot3OamVariableResponseTx.setStatus(_B)
_HpnicfDot3OamVariableResponseRx_Type=Counter32
_HpnicfDot3OamVariableResponseRx_Object=MibTableColumn
hpnicfDot3OamVariableResponseRx=_HpnicfDot3OamVariableResponseRx_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,3,1,4,1,12),_HpnicfDot3OamVariableResponseRx_Type())
hpnicfDot3OamVariableResponseRx.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot3OamVariableResponseRx.setStatus(_B)
_HpnicfDot3OamOrgSpecificTx_Type=Counter32
_HpnicfDot3OamOrgSpecificTx_Object=MibTableColumn
hpnicfDot3OamOrgSpecificTx=_HpnicfDot3OamOrgSpecificTx_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,3,1,4,1,13),_HpnicfDot3OamOrgSpecificTx_Type())
hpnicfDot3OamOrgSpecificTx.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot3OamOrgSpecificTx.setStatus(_B)
_HpnicfDot3OamOrgSpecificRx_Type=Counter32
_HpnicfDot3OamOrgSpecificRx_Object=MibTableColumn
hpnicfDot3OamOrgSpecificRx=_HpnicfDot3OamOrgSpecificRx_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,3,1,4,1,14),_HpnicfDot3OamOrgSpecificRx_Type())
hpnicfDot3OamOrgSpecificRx.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot3OamOrgSpecificRx.setStatus(_B)
_HpnicfDot3OamUnsupportedCodesTx_Type=Counter32
_HpnicfDot3OamUnsupportedCodesTx_Object=MibTableColumn
hpnicfDot3OamUnsupportedCodesTx=_HpnicfDot3OamUnsupportedCodesTx_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,3,1,4,1,15),_HpnicfDot3OamUnsupportedCodesTx_Type())
hpnicfDot3OamUnsupportedCodesTx.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot3OamUnsupportedCodesTx.setStatus(_B)
_HpnicfDot3OamUnsupportedCodesRx_Type=Counter32
_HpnicfDot3OamUnsupportedCodesRx_Object=MibTableColumn
hpnicfDot3OamUnsupportedCodesRx=_HpnicfDot3OamUnsupportedCodesRx_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,3,1,4,1,16),_HpnicfDot3OamUnsupportedCodesRx_Type())
hpnicfDot3OamUnsupportedCodesRx.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot3OamUnsupportedCodesRx.setStatus(_B)
_HpnicfDot3OamFramesLostDueToOam_Type=Counter32
_HpnicfDot3OamFramesLostDueToOam_Object=MibTableColumn
hpnicfDot3OamFramesLostDueToOam=_HpnicfDot3OamFramesLostDueToOam_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,3,1,4,1,17),_HpnicfDot3OamFramesLostDueToOam_Type())
hpnicfDot3OamFramesLostDueToOam.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot3OamFramesLostDueToOam.setStatus(_B)
_HpnicfDot3OamEventConfigTable_Object=MibTable
hpnicfDot3OamEventConfigTable=_HpnicfDot3OamEventConfigTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,3,1,5))
if mibBuilder.loadTexts:hpnicfDot3OamEventConfigTable.setStatus(_B)
_HpnicfDot3OamEventConfigEntry_Object=MibTableRow
hpnicfDot3OamEventConfigEntry=_HpnicfDot3OamEventConfigEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,3,1,5,1))
hpnicfDot3OamEventConfigEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:hpnicfDot3OamEventConfigEntry.setStatus(_B)
_HpnicfDot3OamErrSymPeriodWindowHi_Type=Unsigned32
_HpnicfDot3OamErrSymPeriodWindowHi_Object=MibTableColumn
hpnicfDot3OamErrSymPeriodWindowHi=_HpnicfDot3OamErrSymPeriodWindowHi_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,3,1,5,1,1),_HpnicfDot3OamErrSymPeriodWindowHi_Type())
hpnicfDot3OamErrSymPeriodWindowHi.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfDot3OamErrSymPeriodWindowHi.setStatus(_B)
_HpnicfDot3OamErrSymPeriodWindowLo_Type=Unsigned32
_HpnicfDot3OamErrSymPeriodWindowLo_Object=MibTableColumn
hpnicfDot3OamErrSymPeriodWindowLo=_HpnicfDot3OamErrSymPeriodWindowLo_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,3,1,5,1,2),_HpnicfDot3OamErrSymPeriodWindowLo_Type())
hpnicfDot3OamErrSymPeriodWindowLo.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfDot3OamErrSymPeriodWindowLo.setStatus(_B)
_HpnicfDot3OamErrSymPeriodThresholdHi_Type=Unsigned32
_HpnicfDot3OamErrSymPeriodThresholdHi_Object=MibTableColumn
hpnicfDot3OamErrSymPeriodThresholdHi=_HpnicfDot3OamErrSymPeriodThresholdHi_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,3,1,5,1,3),_HpnicfDot3OamErrSymPeriodThresholdHi_Type())
hpnicfDot3OamErrSymPeriodThresholdHi.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfDot3OamErrSymPeriodThresholdHi.setStatus(_B)
_HpnicfDot3OamErrSymPeriodThresholdLo_Type=Unsigned32
_HpnicfDot3OamErrSymPeriodThresholdLo_Object=MibTableColumn
hpnicfDot3OamErrSymPeriodThresholdLo=_HpnicfDot3OamErrSymPeriodThresholdLo_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,3,1,5,1,4),_HpnicfDot3OamErrSymPeriodThresholdLo_Type())
hpnicfDot3OamErrSymPeriodThresholdLo.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfDot3OamErrSymPeriodThresholdLo.setStatus(_B)
class _HpnicfDot3OamErrSymPeriodEvNotifEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_H,2)))
_HpnicfDot3OamErrSymPeriodEvNotifEnable_Type.__name__=_D
_HpnicfDot3OamErrSymPeriodEvNotifEnable_Object=MibTableColumn
hpnicfDot3OamErrSymPeriodEvNotifEnable=_HpnicfDot3OamErrSymPeriodEvNotifEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,3,1,5,1,5),_HpnicfDot3OamErrSymPeriodEvNotifEnable_Type())
hpnicfDot3OamErrSymPeriodEvNotifEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfDot3OamErrSymPeriodEvNotifEnable.setStatus(_B)
_HpnicfDot3OamErrFramePeriodWindow_Type=Unsigned32
_HpnicfDot3OamErrFramePeriodWindow_Object=MibTableColumn
hpnicfDot3OamErrFramePeriodWindow=_HpnicfDot3OamErrFramePeriodWindow_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,3,1,5,1,6),_HpnicfDot3OamErrFramePeriodWindow_Type())
hpnicfDot3OamErrFramePeriodWindow.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfDot3OamErrFramePeriodWindow.setStatus(_B)
_HpnicfDot3OamErrFramePeriodThreshold_Type=Unsigned32
_HpnicfDot3OamErrFramePeriodThreshold_Object=MibTableColumn
hpnicfDot3OamErrFramePeriodThreshold=_HpnicfDot3OamErrFramePeriodThreshold_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,3,1,5,1,7),_HpnicfDot3OamErrFramePeriodThreshold_Type())
hpnicfDot3OamErrFramePeriodThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfDot3OamErrFramePeriodThreshold.setStatus(_B)
class _HpnicfDot3OamErrFramePeriodEvNotifEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_H,2)))
_HpnicfDot3OamErrFramePeriodEvNotifEnable_Type.__name__=_D
_HpnicfDot3OamErrFramePeriodEvNotifEnable_Object=MibTableColumn
hpnicfDot3OamErrFramePeriodEvNotifEnable=_HpnicfDot3OamErrFramePeriodEvNotifEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,3,1,5,1,8),_HpnicfDot3OamErrFramePeriodEvNotifEnable_Type())
hpnicfDot3OamErrFramePeriodEvNotifEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfDot3OamErrFramePeriodEvNotifEnable.setStatus(_B)
_HpnicfDot3OamErrFrameWindow_Type=Unsigned32
_HpnicfDot3OamErrFrameWindow_Object=MibTableColumn
hpnicfDot3OamErrFrameWindow=_HpnicfDot3OamErrFrameWindow_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,3,1,5,1,9),_HpnicfDot3OamErrFrameWindow_Type())
hpnicfDot3OamErrFrameWindow.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfDot3OamErrFrameWindow.setStatus(_B)
_HpnicfDot3OamErrFrameThreshold_Type=Unsigned32
_HpnicfDot3OamErrFrameThreshold_Object=MibTableColumn
hpnicfDot3OamErrFrameThreshold=_HpnicfDot3OamErrFrameThreshold_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,3,1,5,1,10),_HpnicfDot3OamErrFrameThreshold_Type())
hpnicfDot3OamErrFrameThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfDot3OamErrFrameThreshold.setStatus(_B)
class _HpnicfDot3OamErrFrameEvNotifEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_H,2)))
_HpnicfDot3OamErrFrameEvNotifEnable_Type.__name__=_D
_HpnicfDot3OamErrFrameEvNotifEnable_Object=MibTableColumn
hpnicfDot3OamErrFrameEvNotifEnable=_HpnicfDot3OamErrFrameEvNotifEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,3,1,5,1,11),_HpnicfDot3OamErrFrameEvNotifEnable_Type())
hpnicfDot3OamErrFrameEvNotifEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfDot3OamErrFrameEvNotifEnable.setStatus(_B)
class _HpnicfDot3OamErrFrameSecsSummaryWindow_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,9000))
_HpnicfDot3OamErrFrameSecsSummaryWindow_Type.__name__=_D
_HpnicfDot3OamErrFrameSecsSummaryWindow_Object=MibTableColumn
hpnicfDot3OamErrFrameSecsSummaryWindow=_HpnicfDot3OamErrFrameSecsSummaryWindow_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,3,1,5,1,12),_HpnicfDot3OamErrFrameSecsSummaryWindow_Type())
hpnicfDot3OamErrFrameSecsSummaryWindow.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfDot3OamErrFrameSecsSummaryWindow.setStatus(_B)
class _HpnicfDot3OamErrFrameSecsSummaryThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,900))
_HpnicfDot3OamErrFrameSecsSummaryThreshold_Type.__name__=_D
_HpnicfDot3OamErrFrameSecsSummaryThreshold_Object=MibTableColumn
hpnicfDot3OamErrFrameSecsSummaryThreshold=_HpnicfDot3OamErrFrameSecsSummaryThreshold_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,3,1,5,1,13),_HpnicfDot3OamErrFrameSecsSummaryThreshold_Type())
hpnicfDot3OamErrFrameSecsSummaryThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfDot3OamErrFrameSecsSummaryThreshold.setStatus(_B)
class _HpnicfDot3OamErrFrameSecsEvNotifEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_H,2)))
_HpnicfDot3OamErrFrameSecsEvNotifEnable_Type.__name__=_D
_HpnicfDot3OamErrFrameSecsEvNotifEnable_Object=MibTableColumn
hpnicfDot3OamErrFrameSecsEvNotifEnable=_HpnicfDot3OamErrFrameSecsEvNotifEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,3,1,5,1,14),_HpnicfDot3OamErrFrameSecsEvNotifEnable_Type())
hpnicfDot3OamErrFrameSecsEvNotifEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfDot3OamErrFrameSecsEvNotifEnable.setStatus(_B)
_HpnicfDot3OamEventLogTable_Object=MibTable
hpnicfDot3OamEventLogTable=_HpnicfDot3OamEventLogTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,3,1,6))
if mibBuilder.loadTexts:hpnicfDot3OamEventLogTable.setStatus(_B)
_HpnicfDot3OamEventLogEntry_Object=MibTableRow
hpnicfDot3OamEventLogEntry=_HpnicfDot3OamEventLogEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,3,1,6,1))
hpnicfDot3OamEventLogEntry.setIndexNames((0,_F,_G),(0,_A,_d))
if mibBuilder.loadTexts:hpnicfDot3OamEventLogEntry.setStatus(_B)
_HpnicfDot3OamEventLogIndex_Type=Unsigned32
_HpnicfDot3OamEventLogIndex_Object=MibTableColumn
hpnicfDot3OamEventLogIndex=_HpnicfDot3OamEventLogIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,3,1,6,1,1),_HpnicfDot3OamEventLogIndex_Type())
hpnicfDot3OamEventLogIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:hpnicfDot3OamEventLogIndex.setStatus(_B)
_HpnicfDot3OamEventLogTimestamp_Type=DateAndTime
_HpnicfDot3OamEventLogTimestamp_Object=MibTableColumn
hpnicfDot3OamEventLogTimestamp=_HpnicfDot3OamEventLogTimestamp_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,3,1,6,1,2),_HpnicfDot3OamEventLogTimestamp_Type())
hpnicfDot3OamEventLogTimestamp.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot3OamEventLogTimestamp.setStatus(_B)
_HpnicfDot3OamEventLogOui_Type=Dot3Oui
_HpnicfDot3OamEventLogOui_Object=MibTableColumn
hpnicfDot3OamEventLogOui=_HpnicfDot3OamEventLogOui_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,3,1,6,1,3),_HpnicfDot3OamEventLogOui_Type())
hpnicfDot3OamEventLogOui.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot3OamEventLogOui.setStatus(_B)
_HpnicfDot3OamEventLogType_Type=Unsigned32
_HpnicfDot3OamEventLogType_Object=MibTableColumn
hpnicfDot3OamEventLogType=_HpnicfDot3OamEventLogType_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,3,1,6,1,4),_HpnicfDot3OamEventLogType_Type())
hpnicfDot3OamEventLogType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot3OamEventLogType.setStatus(_B)
class _HpnicfDot3OamEventLogLocation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('local',1),('remote',2)))
_HpnicfDot3OamEventLogLocation_Type.__name__=_D
_HpnicfDot3OamEventLogLocation_Object=MibTableColumn
hpnicfDot3OamEventLogLocation=_HpnicfDot3OamEventLogLocation_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,3,1,6,1,5),_HpnicfDot3OamEventLogLocation_Type())
hpnicfDot3OamEventLogLocation.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot3OamEventLogLocation.setStatus(_B)
_HpnicfDot3OamEventLogWindowHi_Type=Unsigned32
_HpnicfDot3OamEventLogWindowHi_Object=MibTableColumn
hpnicfDot3OamEventLogWindowHi=_HpnicfDot3OamEventLogWindowHi_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,3,1,6,1,6),_HpnicfDot3OamEventLogWindowHi_Type())
hpnicfDot3OamEventLogWindowHi.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot3OamEventLogWindowHi.setStatus(_B)
_HpnicfDot3OamEventLogWindowLo_Type=Unsigned32
_HpnicfDot3OamEventLogWindowLo_Object=MibTableColumn
hpnicfDot3OamEventLogWindowLo=_HpnicfDot3OamEventLogWindowLo_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,3,1,6,1,7),_HpnicfDot3OamEventLogWindowLo_Type())
hpnicfDot3OamEventLogWindowLo.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot3OamEventLogWindowLo.setStatus(_B)
_HpnicfDot3OamEventLogThresholdHi_Type=Unsigned32
_HpnicfDot3OamEventLogThresholdHi_Object=MibTableColumn
hpnicfDot3OamEventLogThresholdHi=_HpnicfDot3OamEventLogThresholdHi_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,3,1,6,1,8),_HpnicfDot3OamEventLogThresholdHi_Type())
hpnicfDot3OamEventLogThresholdHi.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot3OamEventLogThresholdHi.setStatus(_B)
_HpnicfDot3OamEventLogThresholdLo_Type=Unsigned32
_HpnicfDot3OamEventLogThresholdLo_Object=MibTableColumn
hpnicfDot3OamEventLogThresholdLo=_HpnicfDot3OamEventLogThresholdLo_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,3,1,6,1,9),_HpnicfDot3OamEventLogThresholdLo_Type())
hpnicfDot3OamEventLogThresholdLo.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot3OamEventLogThresholdLo.setStatus(_B)
_HpnicfDot3OamEventLogValue_Type=CounterBasedGauge64
_HpnicfDot3OamEventLogValue_Object=MibTableColumn
hpnicfDot3OamEventLogValue=_HpnicfDot3OamEventLogValue_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,3,1,6,1,10),_HpnicfDot3OamEventLogValue_Type())
hpnicfDot3OamEventLogValue.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot3OamEventLogValue.setStatus(_B)
_HpnicfDot3OamEventLogRunningTotal_Type=CounterBasedGauge64
_HpnicfDot3OamEventLogRunningTotal_Object=MibTableColumn
hpnicfDot3OamEventLogRunningTotal=_HpnicfDot3OamEventLogRunningTotal_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,3,1,6,1,11),_HpnicfDot3OamEventLogRunningTotal_Type())
hpnicfDot3OamEventLogRunningTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot3OamEventLogRunningTotal.setStatus(_B)
_HpnicfDot3OamEventLogEventTotal_Type=Unsigned32
_HpnicfDot3OamEventLogEventTotal_Object=MibTableColumn
hpnicfDot3OamEventLogEventTotal=_HpnicfDot3OamEventLogEventTotal_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,3,1,6,1,12),_HpnicfDot3OamEventLogEventTotal_Type())
hpnicfDot3OamEventLogEventTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot3OamEventLogEventTotal.setStatus(_B)
_HpnicfDot3OamTraps_ObjectIdentity=ObjectIdentity
hpnicfDot3OamTraps=_HpnicfDot3OamTraps_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,42,3,1,7))
_HpnicfDot3OamTrapsPrefix_ObjectIdentity=ObjectIdentity
hpnicfDot3OamTrapsPrefix=_HpnicfDot3OamTrapsPrefix_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,42,3,1,7,0))
_HpnicfDot3OamConformance_ObjectIdentity=ObjectIdentity
hpnicfDot3OamConformance=_HpnicfDot3OamConformance_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,42,3,2))
_HpnicfDot3OamGroups_ObjectIdentity=ObjectIdentity
hpnicfDot3OamGroups=_HpnicfDot3OamGroups_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,42,3,2,1))
_HpnicfDot3OamCompliances_ObjectIdentity=ObjectIdentity
hpnicfDot3OamCompliances=_HpnicfDot3OamCompliances_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,42,3,2,2))
hpnicfDot3OamControlGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,15,2,42,3,2,1,1))
hpnicfDot3OamControlGroup.setObjects(*((_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j)))
if mibBuilder.loadTexts:hpnicfDot3OamControlGroup.setStatus(_B)
hpnicfDot3OamPeerGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,15,2,42,3,2,1,2))
hpnicfDot3OamPeerGroup.setObjects(*((_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r)))
if mibBuilder.loadTexts:hpnicfDot3OamPeerGroup.setStatus(_B)
hpnicfDot3OamStatsBaseGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,15,2,42,3,2,1,3))
hpnicfDot3OamStatsBaseGroup.setObjects(*((_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_A8)))
if mibBuilder.loadTexts:hpnicfDot3OamStatsBaseGroup.setStatus(_B)
hpnicfDot3OamLoopbackGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,15,2,42,3,2,1,4))
hpnicfDot3OamLoopbackGroup.setObjects(*((_A,_A9),(_A,_AA),(_A,_AB)))
if mibBuilder.loadTexts:hpnicfDot3OamLoopbackGroup.setStatus(_B)
hpnicfDot3OamErrSymbolPeriodEventGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,15,2,42,3,2,1,5))
hpnicfDot3OamErrSymbolPeriodEventGroup.setObjects(*((_A,_AC),(_A,_AD),(_A,_AE),(_A,_AF),(_A,_AG)))
if mibBuilder.loadTexts:hpnicfDot3OamErrSymbolPeriodEventGroup.setStatus(_B)
hpnicfDot3OamErrFramePeriodEventGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,15,2,42,3,2,1,6))
hpnicfDot3OamErrFramePeriodEventGroup.setObjects(*((_A,_AH),(_A,_AI),(_A,_AJ)))
if mibBuilder.loadTexts:hpnicfDot3OamErrFramePeriodEventGroup.setStatus(_B)
hpnicfDot3OamErrFrameEventGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,15,2,42,3,2,1,7))
hpnicfDot3OamErrFrameEventGroup.setObjects(*((_A,_AK),(_A,_AL),(_A,_AM)))
if mibBuilder.loadTexts:hpnicfDot3OamErrFrameEventGroup.setStatus(_B)
hpnicfDot3OamErrFrameSecsSummaryEventGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,15,2,42,3,2,1,8))
hpnicfDot3OamErrFrameSecsSummaryEventGroup.setObjects(*((_A,_AN),(_A,_AO),(_A,_AP)))
if mibBuilder.loadTexts:hpnicfDot3OamErrFrameSecsSummaryEventGroup.setStatus(_B)
hpnicfDot3OamEventLogGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,15,2,42,3,2,1,9))
hpnicfDot3OamEventLogGroup.setObjects(*((_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_N)))
if mibBuilder.loadTexts:hpnicfDot3OamEventLogGroup.setStatus(_B)
hpnicfDot3OamThresholdEvent=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,42,3,1,7,0,1))
hpnicfDot3OamThresholdEvent.setObjects(*((_F,_G),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_N)))
if mibBuilder.loadTexts:hpnicfDot3OamThresholdEvent.setStatus(_B)
hpnicfDot3OamNonThresholdEvent=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,42,3,1,7,0,2))
hpnicfDot3OamNonThresholdEvent.setObjects(*((_F,_G),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:hpnicfDot3OamNonThresholdEvent.setStatus(_B)
hpnicfDot3OamNotificationGroup=NotificationGroup((1,3,6,1,4,1,11,2,14,11,15,2,42,3,2,1,10))
hpnicfDot3OamNotificationGroup.setObjects(*((_A,_AQ),(_A,_AR)))
if mibBuilder.loadTexts:hpnicfDot3OamNotificationGroup.setStatus(_B)
hpnicfDot3OamCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,15,2,42,3,2,2,1))
hpnicfDot3OamCompliance.setObjects(*((_A,_AS),(_A,_AT),(_A,_AU),(_A,_AV),(_A,_AW),(_A,_AX),(_A,_AY),(_A,_AZ),(_A,_Aa),(_A,_Ab)))
if mibBuilder.loadTexts:hpnicfDot3OamCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'Dot3Oui':Dot3Oui,'hpnicfEfmOamMIB':hpnicfEfmOamMIB,'hpnicfDot3OamMIB':hpnicfDot3OamMIB,'hpnicfDot3OamTable':hpnicfDot3OamTable,'hpnicfDot3OamEntry':hpnicfDot3OamEntry,_e:hpnicfDot3OamAdminState,_f:hpnicfDot3OamOperStatus,_g:hpnicfDot3OamMode,_h:hpnicfDot3OamMaxOamPduSize,_i:hpnicfDot3OamConfigRevision,_j:hpnicfDot3OamFunctionsSupported,'hpnicfDot3OamPeerTable':hpnicfDot3OamPeerTable,'hpnicfDot3OamPeerEntry':hpnicfDot3OamPeerEntry,_k:hpnicfDot3OamPeerStatus,_l:hpnicfDot3OamPeerMacAddress,_m:hpnicfDot3OamPeerVendorOui,_n:hpnicfDot3OamPeerVendorInfo,_o:hpnicfDot3OamPeerMode,_q:hpnicfDot3OamPeerMaxOamPduSize,_r:hpnicfDot3OamPeerConfigRevision,_p:hpnicfDot3OamPeerFunctionsSupported,'hpnicfDot3OamLoopbackTable':hpnicfDot3OamLoopbackTable,'hpnicfDot3OamLoopbackEntry':hpnicfDot3OamLoopbackEntry,_A9:hpnicfDot3OamLoopbackCommand,_AA:hpnicfDot3OamLoopbackStatus,_AB:hpnicfDot3OamLoopbackIgnoreRx,'hpnicfDot3OamStatsTable':hpnicfDot3OamStatsTable,'hpnicfDot3OamStatsEntry':hpnicfDot3OamStatsEntry,_s:hpnicfDot3OamInformationTx,_t:hpnicfDot3OamInformationRx,_u:hpnicfDot3OamUniqueEventNotificationTx,_v:hpnicfDot3OamUniqueEventNotificationRx,_w:hpnicfDot3OamDuplicateEventNotificationTx,_x:hpnicfDot3OamDuplicateEventNotificationRx,_y:hpnicfDot3OamLoopbackControlTx,_z:hpnicfDot3OamLoopbackControlRx,_A0:hpnicfDot3OamVariableRequestTx,_A1:hpnicfDot3OamVariableRequestRx,_A2:hpnicfDot3OamVariableResponseTx,_A3:hpnicfDot3OamVariableResponseRx,_A4:hpnicfDot3OamOrgSpecificTx,_A5:hpnicfDot3OamOrgSpecificRx,_A6:hpnicfDot3OamUnsupportedCodesTx,_A7:hpnicfDot3OamUnsupportedCodesRx,_A8:hpnicfDot3OamFramesLostDueToOam,'hpnicfDot3OamEventConfigTable':hpnicfDot3OamEventConfigTable,'hpnicfDot3OamEventConfigEntry':hpnicfDot3OamEventConfigEntry,_AC:hpnicfDot3OamErrSymPeriodWindowHi,_AD:hpnicfDot3OamErrSymPeriodWindowLo,_AE:hpnicfDot3OamErrSymPeriodThresholdHi,_AF:hpnicfDot3OamErrSymPeriodThresholdLo,_AG:hpnicfDot3OamErrSymPeriodEvNotifEnable,_AH:hpnicfDot3OamErrFramePeriodWindow,_AI:hpnicfDot3OamErrFramePeriodThreshold,_AJ:hpnicfDot3OamErrFramePeriodEvNotifEnable,_AK:hpnicfDot3OamErrFrameWindow,_AL:hpnicfDot3OamErrFrameThreshold,_AM:hpnicfDot3OamErrFrameEvNotifEnable,_AN:hpnicfDot3OamErrFrameSecsSummaryWindow,_AO:hpnicfDot3OamErrFrameSecsSummaryThreshold,_AP:hpnicfDot3OamErrFrameSecsEvNotifEnable,'hpnicfDot3OamEventLogTable':hpnicfDot3OamEventLogTable,'hpnicfDot3OamEventLogEntry':hpnicfDot3OamEventLogEntry,_d:hpnicfDot3OamEventLogIndex,_J:hpnicfDot3OamEventLogTimestamp,_K:hpnicfDot3OamEventLogOui,_L:hpnicfDot3OamEventLogType,_M:hpnicfDot3OamEventLogLocation,_Q:hpnicfDot3OamEventLogWindowHi,_R:hpnicfDot3OamEventLogWindowLo,_S:hpnicfDot3OamEventLogThresholdHi,_T:hpnicfDot3OamEventLogThresholdLo,_U:hpnicfDot3OamEventLogValue,_V:hpnicfDot3OamEventLogRunningTotal,_N:hpnicfDot3OamEventLogEventTotal,'hpnicfDot3OamTraps':hpnicfDot3OamTraps,'hpnicfDot3OamTrapsPrefix':hpnicfDot3OamTrapsPrefix,_AQ:hpnicfDot3OamThresholdEvent,_AR:hpnicfDot3OamNonThresholdEvent,'hpnicfDot3OamConformance':hpnicfDot3OamConformance,'hpnicfDot3OamGroups':hpnicfDot3OamGroups,_AS:hpnicfDot3OamControlGroup,_AT:hpnicfDot3OamPeerGroup,_AU:hpnicfDot3OamStatsBaseGroup,_AV:hpnicfDot3OamLoopbackGroup,_AW:hpnicfDot3OamErrSymbolPeriodEventGroup,_AX:hpnicfDot3OamErrFramePeriodEventGroup,_AY:hpnicfDot3OamErrFrameEventGroup,_AZ:hpnicfDot3OamErrFrameSecsSummaryEventGroup,_Aa:hpnicfDot3OamEventLogGroup,_Ab:hpnicfDot3OamNotificationGroup,'hpnicfDot3OamCompliances':hpnicfDot3OamCompliances,'hpnicfDot3OamCompliance':hpnicfDot3OamCompliance})