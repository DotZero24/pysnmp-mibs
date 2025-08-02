_Ag='cdot3OamNotificationGroup'
_Af='cdot3OamEventLogGroup'
_Ae='cdot3OamFlagEventGroup'
_Ad='cdot3OamErrFrameSecsSummaryEventGroup'
_Ac='cdot3OamErrFrameEventGroup'
_Ab='cdot3OamErrFramePeriodEventGroup'
_Aa='cdot3OamErrSymbolPeriodEventGroup'
_AZ='cdot3OamLoopbackGroup'
_AY='cdot3OamStatsBaseGroup'
_AX='cdot3OamPeerGroup'
_AW='cdot3OamControlGroup'
_AV='cdot3OamNonThresholdEvent'
_AU='cdot3OamThresholdEvent'
_AT='cdot3OamCriticalEventEnable'
_AS='cdot3OamDyingGaspEnable'
_AR='cdot3OamErrFrameSecsEvNotifEnable'
_AQ='cdot3OamErrFrameSecsSummaryThreshold'
_AP='cdot3OamErrFrameSecsSummaryWindow'
_AO='cdot3OamErrFrameEvNotifEnable'
_AN='cdot3OamErrFrameThreshold'
_AM='cdot3OamErrFrameWindow'
_AL='cdot3OamErrFramePeriodEvNotifEnable'
_AK='cdot3OamErrFramePeriodThreshold'
_AJ='cdot3OamErrFramePeriodWindow'
_AI='cdot3OamErrSymPeriodEvNotifEnable'
_AH='cdot3OamErrSymPeriodThresholdLo'
_AG='cdot3OamErrSymPeriodThresholdHi'
_AF='cdot3OamErrSymPeriodWindowLo'
_AE='cdot3OamErrSymPeriodWindowHi'
_AD='cdot3OamLoopbackIgnoreRx'
_AC='cdot3OamLoopbackStatus'
_AB='cdot3OamFramesLostDueToOam'
_AA='cdot3OamUnsupportedCodesRx'
_A9='cdot3OamUnsupportedCodesTx'
_A8='cdot3OamOrgSpecificRx'
_A7='cdot3OamOrgSpecificTx'
_A6='cdot3OamVariableResponseRx'
_A5='cdot3OamVariableResponseTx'
_A4='cdot3OamVariableRequestRx'
_A3='cdot3OamVariableRequestTx'
_A2='cdot3OamLoopbackControlRx'
_A1='cdot3OamLoopbackControlTx'
_A0='cdot3OamDuplicateEventNotificationRx'
_z='cdot3OamDuplicateEventNotificationTx'
_y='cdot3OamUniqueEventNotificationRx'
_x='cdot3OamUniqueEventNotificationTx'
_w='cdot3OamInformationRx'
_v='cdot3OamInformationTx'
_u='cdot3OamPeerConfigRevision'
_t='cdot3OamPeerMaxOamPduSize'
_s='cdot3OamPeerFunctionsSupported'
_r='cdot3OamPeerMode'
_q='cdot3OamPeerVendorInfo'
_p='cdot3OamPeerVendorOui'
_o='cdot3OamPeerMacAddress'
_n='cdot3OamFunctionsSupported'
_m='cdot3OamConfigRevision'
_l='cdot3OamMaxOamPduSize'
_k='cdot3OamMode'
_j='cdot3OamOperStatus'
_i='cdot3OamAdminState'
_h='cdot3OamEventLogIndex'
_g='tenths of a second'
_f='symbols'
_e='2^32 symbols'
_d='unknown'
_c='variableSupport'
_b='eventSupport'
_a='loopbackSupport'
_Z='unidirectionalSupport'
_Y='octets'
_X='passive'
_W='active'
_V='disabled'
_U='cdot3OamEventLogRunningTotal'
_T='cdot3OamEventLogValue'
_S='cdot3OamEventLogThresholdLo'
_R='cdot3OamEventLogThresholdHi'
_Q='cdot3OamEventLogWindowLo'
_P='cdot3OamEventLogWindowHi'
_O='Bits'
_N='cdot3OamEventLogEventTotal'
_M='cdot3OamEventLogLocation'
_L='cdot3OamEventLogType'
_K='cdot3OamEventLogOui'
_J='cdot3OamEventLogTimestamp'
_I='Unsigned32'
_H='ifIndex'
_G='IF-MIB'
_F='Integer32'
_E='frames'
_D='read-write'
_C='read-only'
_B='current'
_A='CISCO-DOT3-OAM-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoExperiment,=mibBuilder.importSymbols('CISCO-SMI','ciscoExperiment')
CounterBasedGauge64,=mibBuilder.importSymbols('HCNUM-TC','CounterBasedGauge64')
ifIndex,=mibBuilder.importSymbols(_G,_H)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_O,'Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_I,'iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention','TimeStamp','TruthValue')
cdot3OamMIB=ModuleIdentity((1,3,6,1,4,1,9,10,136))
if mibBuilder.loadTexts:cdot3OamMIB.setRevisions(('2006-05-31 00:00',))
class Cdot3Oui(TextualConvention,OctetString):status=_B;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,3));fixedLength=3
_Cdot3OamNotifications_ObjectIdentity=ObjectIdentity
cdot3OamNotifications=_Cdot3OamNotifications_ObjectIdentity((1,3,6,1,4,1,9,10,136,0))
_Cdot3OamObjects_ObjectIdentity=ObjectIdentity
cdot3OamObjects=_Cdot3OamObjects_ObjectIdentity((1,3,6,1,4,1,9,10,136,1))
_Cdot3OamTable_Object=MibTable
cdot3OamTable=_Cdot3OamTable_Object((1,3,6,1,4,1,9,10,136,1,1))
if mibBuilder.loadTexts:cdot3OamTable.setStatus(_B)
_Cdot3OamEntry_Object=MibTableRow
cdot3OamEntry=_Cdot3OamEntry_Object((1,3,6,1,4,1,9,10,136,1,1,1))
cdot3OamEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:cdot3OamEntry.setStatus(_B)
class _Cdot3OamAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_V,1),('enabled',2)))
_Cdot3OamAdminState_Type.__name__=_F
_Cdot3OamAdminState_Object=MibTableColumn
cdot3OamAdminState=_Cdot3OamAdminState_Object((1,3,6,1,4,1,9,10,136,1,1,1,1),_Cdot3OamAdminState_Type())
cdot3OamAdminState.setMaxAccess(_D)
if mibBuilder.loadTexts:cdot3OamAdminState.setStatus(_B)
class _Cdot3OamOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_V,1),('linkFault',2),('passiveWait',3),('activeSendLocal',4),('sendLocalAndRemote',5),('sendLocalAndRemoteOk',6),('oamPeeringLocallyRejected',7),('oamPeeringRemotelyRejected',8),('operational',9),('nonOperHalfDuplex',10)))
_Cdot3OamOperStatus_Type.__name__=_F
_Cdot3OamOperStatus_Object=MibTableColumn
cdot3OamOperStatus=_Cdot3OamOperStatus_Object((1,3,6,1,4,1,9,10,136,1,1,1,2),_Cdot3OamOperStatus_Type())
cdot3OamOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cdot3OamOperStatus.setStatus(_B)
class _Cdot3OamMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_W,1),(_X,2)))
_Cdot3OamMode_Type.__name__=_F
_Cdot3OamMode_Object=MibTableColumn
cdot3OamMode=_Cdot3OamMode_Object((1,3,6,1,4,1,9,10,136,1,1,1,3),_Cdot3OamMode_Type())
cdot3OamMode.setMaxAccess(_D)
if mibBuilder.loadTexts:cdot3OamMode.setStatus(_B)
class _Cdot3OamMaxOamPduSize_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(64,1518))
_Cdot3OamMaxOamPduSize_Type.__name__=_I
_Cdot3OamMaxOamPduSize_Object=MibTableColumn
cdot3OamMaxOamPduSize=_Cdot3OamMaxOamPduSize_Object((1,3,6,1,4,1,9,10,136,1,1,1,4),_Cdot3OamMaxOamPduSize_Type())
cdot3OamMaxOamPduSize.setMaxAccess(_C)
if mibBuilder.loadTexts:cdot3OamMaxOamPduSize.setStatus(_B)
if mibBuilder.loadTexts:cdot3OamMaxOamPduSize.setUnits(_Y)
class _Cdot3OamConfigRevision_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Cdot3OamConfigRevision_Type.__name__=_I
_Cdot3OamConfigRevision_Object=MibTableColumn
cdot3OamConfigRevision=_Cdot3OamConfigRevision_Object((1,3,6,1,4,1,9,10,136,1,1,1,5),_Cdot3OamConfigRevision_Type())
cdot3OamConfigRevision.setMaxAccess(_C)
if mibBuilder.loadTexts:cdot3OamConfigRevision.setStatus(_B)
class _Cdot3OamFunctionsSupported_Type(Bits):namedValues=NamedValues(*((_Z,0),(_a,1),(_b,2),(_c,3)))
_Cdot3OamFunctionsSupported_Type.__name__=_O
_Cdot3OamFunctionsSupported_Object=MibTableColumn
cdot3OamFunctionsSupported=_Cdot3OamFunctionsSupported_Object((1,3,6,1,4,1,9,10,136,1,1,1,6),_Cdot3OamFunctionsSupported_Type())
cdot3OamFunctionsSupported.setMaxAccess(_C)
if mibBuilder.loadTexts:cdot3OamFunctionsSupported.setStatus(_B)
_Cdot3OamPeerTable_Object=MibTable
cdot3OamPeerTable=_Cdot3OamPeerTable_Object((1,3,6,1,4,1,9,10,136,1,2))
if mibBuilder.loadTexts:cdot3OamPeerTable.setStatus(_B)
_Cdot3OamPeerEntry_Object=MibTableRow
cdot3OamPeerEntry=_Cdot3OamPeerEntry_Object((1,3,6,1,4,1,9,10,136,1,2,1))
cdot3OamPeerEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:cdot3OamPeerEntry.setStatus(_B)
_Cdot3OamPeerMacAddress_Type=MacAddress
_Cdot3OamPeerMacAddress_Object=MibTableColumn
cdot3OamPeerMacAddress=_Cdot3OamPeerMacAddress_Object((1,3,6,1,4,1,9,10,136,1,2,1,1),_Cdot3OamPeerMacAddress_Type())
cdot3OamPeerMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cdot3OamPeerMacAddress.setStatus(_B)
_Cdot3OamPeerVendorOui_Type=Cdot3Oui
_Cdot3OamPeerVendorOui_Object=MibTableColumn
cdot3OamPeerVendorOui=_Cdot3OamPeerVendorOui_Object((1,3,6,1,4,1,9,10,136,1,2,1,2),_Cdot3OamPeerVendorOui_Type())
cdot3OamPeerVendorOui.setMaxAccess(_C)
if mibBuilder.loadTexts:cdot3OamPeerVendorOui.setStatus(_B)
_Cdot3OamPeerVendorInfo_Type=Unsigned32
_Cdot3OamPeerVendorInfo_Object=MibTableColumn
cdot3OamPeerVendorInfo=_Cdot3OamPeerVendorInfo_Object((1,3,6,1,4,1,9,10,136,1,2,1,3),_Cdot3OamPeerVendorInfo_Type())
cdot3OamPeerVendorInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:cdot3OamPeerVendorInfo.setStatus(_B)
class _Cdot3OamPeerMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_W,1),(_X,2),(_d,3)))
_Cdot3OamPeerMode_Type.__name__=_F
_Cdot3OamPeerMode_Object=MibTableColumn
cdot3OamPeerMode=_Cdot3OamPeerMode_Object((1,3,6,1,4,1,9,10,136,1,2,1,4),_Cdot3OamPeerMode_Type())
cdot3OamPeerMode.setMaxAccess(_C)
if mibBuilder.loadTexts:cdot3OamPeerMode.setStatus(_B)
class _Cdot3OamPeerMaxOamPduSize_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1518))
_Cdot3OamPeerMaxOamPduSize_Type.__name__=_I
_Cdot3OamPeerMaxOamPduSize_Object=MibTableColumn
cdot3OamPeerMaxOamPduSize=_Cdot3OamPeerMaxOamPduSize_Object((1,3,6,1,4,1,9,10,136,1,2,1,5),_Cdot3OamPeerMaxOamPduSize_Type())
cdot3OamPeerMaxOamPduSize.setMaxAccess(_C)
if mibBuilder.loadTexts:cdot3OamPeerMaxOamPduSize.setStatus(_B)
if mibBuilder.loadTexts:cdot3OamPeerMaxOamPduSize.setUnits(_Y)
class _Cdot3OamPeerConfigRevision_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Cdot3OamPeerConfigRevision_Type.__name__=_I
_Cdot3OamPeerConfigRevision_Object=MibTableColumn
cdot3OamPeerConfigRevision=_Cdot3OamPeerConfigRevision_Object((1,3,6,1,4,1,9,10,136,1,2,1,6),_Cdot3OamPeerConfigRevision_Type())
cdot3OamPeerConfigRevision.setMaxAccess(_C)
if mibBuilder.loadTexts:cdot3OamPeerConfigRevision.setStatus(_B)
class _Cdot3OamPeerFunctionsSupported_Type(Bits):namedValues=NamedValues(*((_Z,0),(_a,1),(_b,2),(_c,3)))
_Cdot3OamPeerFunctionsSupported_Type.__name__=_O
_Cdot3OamPeerFunctionsSupported_Object=MibTableColumn
cdot3OamPeerFunctionsSupported=_Cdot3OamPeerFunctionsSupported_Object((1,3,6,1,4,1,9,10,136,1,2,1,7),_Cdot3OamPeerFunctionsSupported_Type())
cdot3OamPeerFunctionsSupported.setMaxAccess(_C)
if mibBuilder.loadTexts:cdot3OamPeerFunctionsSupported.setStatus(_B)
_Cdot3OamLoopbackTable_Object=MibTable
cdot3OamLoopbackTable=_Cdot3OamLoopbackTable_Object((1,3,6,1,4,1,9,10,136,1,3))
if mibBuilder.loadTexts:cdot3OamLoopbackTable.setStatus(_B)
_Cdot3OamLoopbackEntry_Object=MibTableRow
cdot3OamLoopbackEntry=_Cdot3OamLoopbackEntry_Object((1,3,6,1,4,1,9,10,136,1,3,1))
cdot3OamLoopbackEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:cdot3OamLoopbackEntry.setStatus(_B)
class _Cdot3OamLoopbackStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('noLoopback',1),('initiatingLoopback',2),('remoteLoopback',3),('terminatingLoopback',4),('localLoopback',5),(_d,6)))
_Cdot3OamLoopbackStatus_Type.__name__=_F
_Cdot3OamLoopbackStatus_Object=MibTableColumn
cdot3OamLoopbackStatus=_Cdot3OamLoopbackStatus_Object((1,3,6,1,4,1,9,10,136,1,3,1,1),_Cdot3OamLoopbackStatus_Type())
cdot3OamLoopbackStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:cdot3OamLoopbackStatus.setStatus(_B)
class _Cdot3OamLoopbackIgnoreRx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ignore',1),('process',2)))
_Cdot3OamLoopbackIgnoreRx_Type.__name__=_F
_Cdot3OamLoopbackIgnoreRx_Object=MibTableColumn
cdot3OamLoopbackIgnoreRx=_Cdot3OamLoopbackIgnoreRx_Object((1,3,6,1,4,1,9,10,136,1,3,1,2),_Cdot3OamLoopbackIgnoreRx_Type())
cdot3OamLoopbackIgnoreRx.setMaxAccess(_D)
if mibBuilder.loadTexts:cdot3OamLoopbackIgnoreRx.setStatus(_B)
_Cdot3OamStatsTable_Object=MibTable
cdot3OamStatsTable=_Cdot3OamStatsTable_Object((1,3,6,1,4,1,9,10,136,1,4))
if mibBuilder.loadTexts:cdot3OamStatsTable.setStatus(_B)
_Cdot3OamStatsEntry_Object=MibTableRow
cdot3OamStatsEntry=_Cdot3OamStatsEntry_Object((1,3,6,1,4,1,9,10,136,1,4,1))
cdot3OamStatsEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:cdot3OamStatsEntry.setStatus(_B)
_Cdot3OamInformationTx_Type=Counter32
_Cdot3OamInformationTx_Object=MibTableColumn
cdot3OamInformationTx=_Cdot3OamInformationTx_Object((1,3,6,1,4,1,9,10,136,1,4,1,1),_Cdot3OamInformationTx_Type())
cdot3OamInformationTx.setMaxAccess(_C)
if mibBuilder.loadTexts:cdot3OamInformationTx.setStatus(_B)
if mibBuilder.loadTexts:cdot3OamInformationTx.setUnits(_E)
_Cdot3OamInformationRx_Type=Counter32
_Cdot3OamInformationRx_Object=MibTableColumn
cdot3OamInformationRx=_Cdot3OamInformationRx_Object((1,3,6,1,4,1,9,10,136,1,4,1,2),_Cdot3OamInformationRx_Type())
cdot3OamInformationRx.setMaxAccess(_C)
if mibBuilder.loadTexts:cdot3OamInformationRx.setStatus(_B)
if mibBuilder.loadTexts:cdot3OamInformationRx.setUnits(_E)
_Cdot3OamUniqueEventNotificationTx_Type=Counter32
_Cdot3OamUniqueEventNotificationTx_Object=MibTableColumn
cdot3OamUniqueEventNotificationTx=_Cdot3OamUniqueEventNotificationTx_Object((1,3,6,1,4,1,9,10,136,1,4,1,3),_Cdot3OamUniqueEventNotificationTx_Type())
cdot3OamUniqueEventNotificationTx.setMaxAccess(_C)
if mibBuilder.loadTexts:cdot3OamUniqueEventNotificationTx.setStatus(_B)
if mibBuilder.loadTexts:cdot3OamUniqueEventNotificationTx.setUnits(_E)
_Cdot3OamUniqueEventNotificationRx_Type=Counter32
_Cdot3OamUniqueEventNotificationRx_Object=MibTableColumn
cdot3OamUniqueEventNotificationRx=_Cdot3OamUniqueEventNotificationRx_Object((1,3,6,1,4,1,9,10,136,1,4,1,4),_Cdot3OamUniqueEventNotificationRx_Type())
cdot3OamUniqueEventNotificationRx.setMaxAccess(_C)
if mibBuilder.loadTexts:cdot3OamUniqueEventNotificationRx.setStatus(_B)
if mibBuilder.loadTexts:cdot3OamUniqueEventNotificationRx.setUnits(_E)
_Cdot3OamDuplicateEventNotificationTx_Type=Counter32
_Cdot3OamDuplicateEventNotificationTx_Object=MibTableColumn
cdot3OamDuplicateEventNotificationTx=_Cdot3OamDuplicateEventNotificationTx_Object((1,3,6,1,4,1,9,10,136,1,4,1,5),_Cdot3OamDuplicateEventNotificationTx_Type())
cdot3OamDuplicateEventNotificationTx.setMaxAccess(_C)
if mibBuilder.loadTexts:cdot3OamDuplicateEventNotificationTx.setStatus(_B)
if mibBuilder.loadTexts:cdot3OamDuplicateEventNotificationTx.setUnits(_E)
_Cdot3OamDuplicateEventNotificationRx_Type=Counter32
_Cdot3OamDuplicateEventNotificationRx_Object=MibTableColumn
cdot3OamDuplicateEventNotificationRx=_Cdot3OamDuplicateEventNotificationRx_Object((1,3,6,1,4,1,9,10,136,1,4,1,6),_Cdot3OamDuplicateEventNotificationRx_Type())
cdot3OamDuplicateEventNotificationRx.setMaxAccess(_C)
if mibBuilder.loadTexts:cdot3OamDuplicateEventNotificationRx.setStatus(_B)
if mibBuilder.loadTexts:cdot3OamDuplicateEventNotificationRx.setUnits(_E)
_Cdot3OamLoopbackControlTx_Type=Counter32
_Cdot3OamLoopbackControlTx_Object=MibTableColumn
cdot3OamLoopbackControlTx=_Cdot3OamLoopbackControlTx_Object((1,3,6,1,4,1,9,10,136,1,4,1,7),_Cdot3OamLoopbackControlTx_Type())
cdot3OamLoopbackControlTx.setMaxAccess(_C)
if mibBuilder.loadTexts:cdot3OamLoopbackControlTx.setStatus(_B)
if mibBuilder.loadTexts:cdot3OamLoopbackControlTx.setUnits(_E)
_Cdot3OamLoopbackControlRx_Type=Counter32
_Cdot3OamLoopbackControlRx_Object=MibTableColumn
cdot3OamLoopbackControlRx=_Cdot3OamLoopbackControlRx_Object((1,3,6,1,4,1,9,10,136,1,4,1,8),_Cdot3OamLoopbackControlRx_Type())
cdot3OamLoopbackControlRx.setMaxAccess(_C)
if mibBuilder.loadTexts:cdot3OamLoopbackControlRx.setStatus(_B)
if mibBuilder.loadTexts:cdot3OamLoopbackControlRx.setUnits(_E)
_Cdot3OamVariableRequestTx_Type=Counter32
_Cdot3OamVariableRequestTx_Object=MibTableColumn
cdot3OamVariableRequestTx=_Cdot3OamVariableRequestTx_Object((1,3,6,1,4,1,9,10,136,1,4,1,9),_Cdot3OamVariableRequestTx_Type())
cdot3OamVariableRequestTx.setMaxAccess(_C)
if mibBuilder.loadTexts:cdot3OamVariableRequestTx.setStatus(_B)
if mibBuilder.loadTexts:cdot3OamVariableRequestTx.setUnits(_E)
_Cdot3OamVariableRequestRx_Type=Counter32
_Cdot3OamVariableRequestRx_Object=MibTableColumn
cdot3OamVariableRequestRx=_Cdot3OamVariableRequestRx_Object((1,3,6,1,4,1,9,10,136,1,4,1,10),_Cdot3OamVariableRequestRx_Type())
cdot3OamVariableRequestRx.setMaxAccess(_C)
if mibBuilder.loadTexts:cdot3OamVariableRequestRx.setStatus(_B)
if mibBuilder.loadTexts:cdot3OamVariableRequestRx.setUnits(_E)
_Cdot3OamVariableResponseTx_Type=Counter32
_Cdot3OamVariableResponseTx_Object=MibTableColumn
cdot3OamVariableResponseTx=_Cdot3OamVariableResponseTx_Object((1,3,6,1,4,1,9,10,136,1,4,1,11),_Cdot3OamVariableResponseTx_Type())
cdot3OamVariableResponseTx.setMaxAccess(_C)
if mibBuilder.loadTexts:cdot3OamVariableResponseTx.setStatus(_B)
if mibBuilder.loadTexts:cdot3OamVariableResponseTx.setUnits(_E)
_Cdot3OamVariableResponseRx_Type=Counter32
_Cdot3OamVariableResponseRx_Object=MibTableColumn
cdot3OamVariableResponseRx=_Cdot3OamVariableResponseRx_Object((1,3,6,1,4,1,9,10,136,1,4,1,12),_Cdot3OamVariableResponseRx_Type())
cdot3OamVariableResponseRx.setMaxAccess(_C)
if mibBuilder.loadTexts:cdot3OamVariableResponseRx.setStatus(_B)
if mibBuilder.loadTexts:cdot3OamVariableResponseRx.setUnits(_E)
_Cdot3OamOrgSpecificTx_Type=Counter32
_Cdot3OamOrgSpecificTx_Object=MibTableColumn
cdot3OamOrgSpecificTx=_Cdot3OamOrgSpecificTx_Object((1,3,6,1,4,1,9,10,136,1,4,1,13),_Cdot3OamOrgSpecificTx_Type())
cdot3OamOrgSpecificTx.setMaxAccess(_C)
if mibBuilder.loadTexts:cdot3OamOrgSpecificTx.setStatus(_B)
if mibBuilder.loadTexts:cdot3OamOrgSpecificTx.setUnits(_E)
_Cdot3OamOrgSpecificRx_Type=Counter32
_Cdot3OamOrgSpecificRx_Object=MibTableColumn
cdot3OamOrgSpecificRx=_Cdot3OamOrgSpecificRx_Object((1,3,6,1,4,1,9,10,136,1,4,1,14),_Cdot3OamOrgSpecificRx_Type())
cdot3OamOrgSpecificRx.setMaxAccess(_C)
if mibBuilder.loadTexts:cdot3OamOrgSpecificRx.setStatus(_B)
if mibBuilder.loadTexts:cdot3OamOrgSpecificRx.setUnits(_E)
_Cdot3OamUnsupportedCodesTx_Type=Counter32
_Cdot3OamUnsupportedCodesTx_Object=MibTableColumn
cdot3OamUnsupportedCodesTx=_Cdot3OamUnsupportedCodesTx_Object((1,3,6,1,4,1,9,10,136,1,4,1,15),_Cdot3OamUnsupportedCodesTx_Type())
cdot3OamUnsupportedCodesTx.setMaxAccess(_C)
if mibBuilder.loadTexts:cdot3OamUnsupportedCodesTx.setStatus(_B)
if mibBuilder.loadTexts:cdot3OamUnsupportedCodesTx.setUnits(_E)
_Cdot3OamUnsupportedCodesRx_Type=Counter32
_Cdot3OamUnsupportedCodesRx_Object=MibTableColumn
cdot3OamUnsupportedCodesRx=_Cdot3OamUnsupportedCodesRx_Object((1,3,6,1,4,1,9,10,136,1,4,1,16),_Cdot3OamUnsupportedCodesRx_Type())
cdot3OamUnsupportedCodesRx.setMaxAccess(_C)
if mibBuilder.loadTexts:cdot3OamUnsupportedCodesRx.setStatus(_B)
if mibBuilder.loadTexts:cdot3OamUnsupportedCodesRx.setUnits(_E)
_Cdot3OamFramesLostDueToOam_Type=Counter32
_Cdot3OamFramesLostDueToOam_Object=MibTableColumn
cdot3OamFramesLostDueToOam=_Cdot3OamFramesLostDueToOam_Object((1,3,6,1,4,1,9,10,136,1,4,1,17),_Cdot3OamFramesLostDueToOam_Type())
cdot3OamFramesLostDueToOam.setMaxAccess(_C)
if mibBuilder.loadTexts:cdot3OamFramesLostDueToOam.setStatus(_B)
if mibBuilder.loadTexts:cdot3OamFramesLostDueToOam.setUnits(_E)
_Cdot3OamEventConfigTable_Object=MibTable
cdot3OamEventConfigTable=_Cdot3OamEventConfigTable_Object((1,3,6,1,4,1,9,10,136,1,5))
if mibBuilder.loadTexts:cdot3OamEventConfigTable.setStatus(_B)
_Cdot3OamEventConfigEntry_Object=MibTableRow
cdot3OamEventConfigEntry=_Cdot3OamEventConfigEntry_Object((1,3,6,1,4,1,9,10,136,1,5,1))
cdot3OamEventConfigEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:cdot3OamEventConfigEntry.setStatus(_B)
_Cdot3OamErrSymPeriodWindowHi_Type=Unsigned32
_Cdot3OamErrSymPeriodWindowHi_Object=MibTableColumn
cdot3OamErrSymPeriodWindowHi=_Cdot3OamErrSymPeriodWindowHi_Object((1,3,6,1,4,1,9,10,136,1,5,1,1),_Cdot3OamErrSymPeriodWindowHi_Type())
cdot3OamErrSymPeriodWindowHi.setMaxAccess(_D)
if mibBuilder.loadTexts:cdot3OamErrSymPeriodWindowHi.setStatus(_B)
if mibBuilder.loadTexts:cdot3OamErrSymPeriodWindowHi.setUnits(_e)
_Cdot3OamErrSymPeriodWindowLo_Type=Unsigned32
_Cdot3OamErrSymPeriodWindowLo_Object=MibTableColumn
cdot3OamErrSymPeriodWindowLo=_Cdot3OamErrSymPeriodWindowLo_Object((1,3,6,1,4,1,9,10,136,1,5,1,2),_Cdot3OamErrSymPeriodWindowLo_Type())
cdot3OamErrSymPeriodWindowLo.setMaxAccess(_D)
if mibBuilder.loadTexts:cdot3OamErrSymPeriodWindowLo.setStatus(_B)
if mibBuilder.loadTexts:cdot3OamErrSymPeriodWindowLo.setUnits(_f)
_Cdot3OamErrSymPeriodThresholdHi_Type=Unsigned32
_Cdot3OamErrSymPeriodThresholdHi_Object=MibTableColumn
cdot3OamErrSymPeriodThresholdHi=_Cdot3OamErrSymPeriodThresholdHi_Object((1,3,6,1,4,1,9,10,136,1,5,1,3),_Cdot3OamErrSymPeriodThresholdHi_Type())
cdot3OamErrSymPeriodThresholdHi.setMaxAccess(_D)
if mibBuilder.loadTexts:cdot3OamErrSymPeriodThresholdHi.setStatus(_B)
if mibBuilder.loadTexts:cdot3OamErrSymPeriodThresholdHi.setUnits(_e)
_Cdot3OamErrSymPeriodThresholdLo_Type=Unsigned32
_Cdot3OamErrSymPeriodThresholdLo_Object=MibTableColumn
cdot3OamErrSymPeriodThresholdLo=_Cdot3OamErrSymPeriodThresholdLo_Object((1,3,6,1,4,1,9,10,136,1,5,1,4),_Cdot3OamErrSymPeriodThresholdLo_Type())
cdot3OamErrSymPeriodThresholdLo.setMaxAccess(_D)
if mibBuilder.loadTexts:cdot3OamErrSymPeriodThresholdLo.setStatus(_B)
if mibBuilder.loadTexts:cdot3OamErrSymPeriodThresholdLo.setUnits(_f)
_Cdot3OamErrSymPeriodEvNotifEnable_Type=TruthValue
_Cdot3OamErrSymPeriodEvNotifEnable_Object=MibTableColumn
cdot3OamErrSymPeriodEvNotifEnable=_Cdot3OamErrSymPeriodEvNotifEnable_Object((1,3,6,1,4,1,9,10,136,1,5,1,5),_Cdot3OamErrSymPeriodEvNotifEnable_Type())
cdot3OamErrSymPeriodEvNotifEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:cdot3OamErrSymPeriodEvNotifEnable.setStatus(_B)
_Cdot3OamErrFramePeriodWindow_Type=Unsigned32
_Cdot3OamErrFramePeriodWindow_Object=MibTableColumn
cdot3OamErrFramePeriodWindow=_Cdot3OamErrFramePeriodWindow_Object((1,3,6,1,4,1,9,10,136,1,5,1,6),_Cdot3OamErrFramePeriodWindow_Type())
cdot3OamErrFramePeriodWindow.setMaxAccess(_D)
if mibBuilder.loadTexts:cdot3OamErrFramePeriodWindow.setStatus(_B)
if mibBuilder.loadTexts:cdot3OamErrFramePeriodWindow.setUnits(_E)
_Cdot3OamErrFramePeriodThreshold_Type=Unsigned32
_Cdot3OamErrFramePeriodThreshold_Object=MibTableColumn
cdot3OamErrFramePeriodThreshold=_Cdot3OamErrFramePeriodThreshold_Object((1,3,6,1,4,1,9,10,136,1,5,1,7),_Cdot3OamErrFramePeriodThreshold_Type())
cdot3OamErrFramePeriodThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:cdot3OamErrFramePeriodThreshold.setStatus(_B)
if mibBuilder.loadTexts:cdot3OamErrFramePeriodThreshold.setUnits(_E)
_Cdot3OamErrFramePeriodEvNotifEnable_Type=TruthValue
_Cdot3OamErrFramePeriodEvNotifEnable_Object=MibTableColumn
cdot3OamErrFramePeriodEvNotifEnable=_Cdot3OamErrFramePeriodEvNotifEnable_Object((1,3,6,1,4,1,9,10,136,1,5,1,8),_Cdot3OamErrFramePeriodEvNotifEnable_Type())
cdot3OamErrFramePeriodEvNotifEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:cdot3OamErrFramePeriodEvNotifEnable.setStatus(_B)
_Cdot3OamErrFrameWindow_Type=Unsigned32
_Cdot3OamErrFrameWindow_Object=MibTableColumn
cdot3OamErrFrameWindow=_Cdot3OamErrFrameWindow_Object((1,3,6,1,4,1,9,10,136,1,5,1,9),_Cdot3OamErrFrameWindow_Type())
cdot3OamErrFrameWindow.setMaxAccess(_D)
if mibBuilder.loadTexts:cdot3OamErrFrameWindow.setStatus(_B)
if mibBuilder.loadTexts:cdot3OamErrFrameWindow.setUnits(_g)
_Cdot3OamErrFrameThreshold_Type=Unsigned32
_Cdot3OamErrFrameThreshold_Object=MibTableColumn
cdot3OamErrFrameThreshold=_Cdot3OamErrFrameThreshold_Object((1,3,6,1,4,1,9,10,136,1,5,1,10),_Cdot3OamErrFrameThreshold_Type())
cdot3OamErrFrameThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:cdot3OamErrFrameThreshold.setStatus(_B)
if mibBuilder.loadTexts:cdot3OamErrFrameThreshold.setUnits(_E)
_Cdot3OamErrFrameEvNotifEnable_Type=TruthValue
_Cdot3OamErrFrameEvNotifEnable_Object=MibTableColumn
cdot3OamErrFrameEvNotifEnable=_Cdot3OamErrFrameEvNotifEnable_Object((1,3,6,1,4,1,9,10,136,1,5,1,11),_Cdot3OamErrFrameEvNotifEnable_Type())
cdot3OamErrFrameEvNotifEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:cdot3OamErrFrameEvNotifEnable.setStatus(_B)
class _Cdot3OamErrFrameSecsSummaryWindow_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,9000))
_Cdot3OamErrFrameSecsSummaryWindow_Type.__name__=_F
_Cdot3OamErrFrameSecsSummaryWindow_Object=MibTableColumn
cdot3OamErrFrameSecsSummaryWindow=_Cdot3OamErrFrameSecsSummaryWindow_Object((1,3,6,1,4,1,9,10,136,1,5,1,12),_Cdot3OamErrFrameSecsSummaryWindow_Type())
cdot3OamErrFrameSecsSummaryWindow.setMaxAccess(_D)
if mibBuilder.loadTexts:cdot3OamErrFrameSecsSummaryWindow.setStatus(_B)
if mibBuilder.loadTexts:cdot3OamErrFrameSecsSummaryWindow.setUnits(_g)
class _Cdot3OamErrFrameSecsSummaryThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,900))
_Cdot3OamErrFrameSecsSummaryThreshold_Type.__name__=_F
_Cdot3OamErrFrameSecsSummaryThreshold_Object=MibTableColumn
cdot3OamErrFrameSecsSummaryThreshold=_Cdot3OamErrFrameSecsSummaryThreshold_Object((1,3,6,1,4,1,9,10,136,1,5,1,13),_Cdot3OamErrFrameSecsSummaryThreshold_Type())
cdot3OamErrFrameSecsSummaryThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:cdot3OamErrFrameSecsSummaryThreshold.setStatus(_B)
if mibBuilder.loadTexts:cdot3OamErrFrameSecsSummaryThreshold.setUnits('errored frame seconds')
_Cdot3OamErrFrameSecsEvNotifEnable_Type=TruthValue
_Cdot3OamErrFrameSecsEvNotifEnable_Object=MibTableColumn
cdot3OamErrFrameSecsEvNotifEnable=_Cdot3OamErrFrameSecsEvNotifEnable_Object((1,3,6,1,4,1,9,10,136,1,5,1,14),_Cdot3OamErrFrameSecsEvNotifEnable_Type())
cdot3OamErrFrameSecsEvNotifEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:cdot3OamErrFrameSecsEvNotifEnable.setStatus(_B)
_Cdot3OamDyingGaspEnable_Type=TruthValue
_Cdot3OamDyingGaspEnable_Object=MibTableColumn
cdot3OamDyingGaspEnable=_Cdot3OamDyingGaspEnable_Object((1,3,6,1,4,1,9,10,136,1,5,1,15),_Cdot3OamDyingGaspEnable_Type())
cdot3OamDyingGaspEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:cdot3OamDyingGaspEnable.setStatus(_B)
_Cdot3OamCriticalEventEnable_Type=TruthValue
_Cdot3OamCriticalEventEnable_Object=MibTableColumn
cdot3OamCriticalEventEnable=_Cdot3OamCriticalEventEnable_Object((1,3,6,1,4,1,9,10,136,1,5,1,16),_Cdot3OamCriticalEventEnable_Type())
cdot3OamCriticalEventEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:cdot3OamCriticalEventEnable.setStatus(_B)
_Cdot3OamEventLogTable_Object=MibTable
cdot3OamEventLogTable=_Cdot3OamEventLogTable_Object((1,3,6,1,4,1,9,10,136,1,6))
if mibBuilder.loadTexts:cdot3OamEventLogTable.setStatus(_B)
_Cdot3OamEventLogEntry_Object=MibTableRow
cdot3OamEventLogEntry=_Cdot3OamEventLogEntry_Object((1,3,6,1,4,1,9,10,136,1,6,1))
cdot3OamEventLogEntry.setIndexNames((0,_G,_H),(0,_A,_h))
if mibBuilder.loadTexts:cdot3OamEventLogEntry.setStatus(_B)
_Cdot3OamEventLogIndex_Type=Unsigned32
_Cdot3OamEventLogIndex_Object=MibTableColumn
cdot3OamEventLogIndex=_Cdot3OamEventLogIndex_Object((1,3,6,1,4,1,9,10,136,1,6,1,1),_Cdot3OamEventLogIndex_Type())
cdot3OamEventLogIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:cdot3OamEventLogIndex.setStatus(_B)
_Cdot3OamEventLogTimestamp_Type=TimeStamp
_Cdot3OamEventLogTimestamp_Object=MibTableColumn
cdot3OamEventLogTimestamp=_Cdot3OamEventLogTimestamp_Object((1,3,6,1,4,1,9,10,136,1,6,1,2),_Cdot3OamEventLogTimestamp_Type())
cdot3OamEventLogTimestamp.setMaxAccess(_C)
if mibBuilder.loadTexts:cdot3OamEventLogTimestamp.setStatus(_B)
_Cdot3OamEventLogOui_Type=Cdot3Oui
_Cdot3OamEventLogOui_Object=MibTableColumn
cdot3OamEventLogOui=_Cdot3OamEventLogOui_Object((1,3,6,1,4,1,9,10,136,1,6,1,3),_Cdot3OamEventLogOui_Type())
cdot3OamEventLogOui.setMaxAccess(_C)
if mibBuilder.loadTexts:cdot3OamEventLogOui.setStatus(_B)
_Cdot3OamEventLogType_Type=Unsigned32
_Cdot3OamEventLogType_Object=MibTableColumn
cdot3OamEventLogType=_Cdot3OamEventLogType_Object((1,3,6,1,4,1,9,10,136,1,6,1,4),_Cdot3OamEventLogType_Type())
cdot3OamEventLogType.setMaxAccess(_C)
if mibBuilder.loadTexts:cdot3OamEventLogType.setStatus(_B)
class _Cdot3OamEventLogLocation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('local',1),('remote',2)))
_Cdot3OamEventLogLocation_Type.__name__=_F
_Cdot3OamEventLogLocation_Object=MibTableColumn
cdot3OamEventLogLocation=_Cdot3OamEventLogLocation_Object((1,3,6,1,4,1,9,10,136,1,6,1,5),_Cdot3OamEventLogLocation_Type())
cdot3OamEventLogLocation.setMaxAccess(_C)
if mibBuilder.loadTexts:cdot3OamEventLogLocation.setStatus(_B)
_Cdot3OamEventLogWindowHi_Type=Unsigned32
_Cdot3OamEventLogWindowHi_Object=MibTableColumn
cdot3OamEventLogWindowHi=_Cdot3OamEventLogWindowHi_Object((1,3,6,1,4,1,9,10,136,1,6,1,6),_Cdot3OamEventLogWindowHi_Type())
cdot3OamEventLogWindowHi.setMaxAccess(_C)
if mibBuilder.loadTexts:cdot3OamEventLogWindowHi.setStatus(_B)
_Cdot3OamEventLogWindowLo_Type=Unsigned32
_Cdot3OamEventLogWindowLo_Object=MibTableColumn
cdot3OamEventLogWindowLo=_Cdot3OamEventLogWindowLo_Object((1,3,6,1,4,1,9,10,136,1,6,1,7),_Cdot3OamEventLogWindowLo_Type())
cdot3OamEventLogWindowLo.setMaxAccess(_C)
if mibBuilder.loadTexts:cdot3OamEventLogWindowLo.setStatus(_B)
_Cdot3OamEventLogThresholdHi_Type=Unsigned32
_Cdot3OamEventLogThresholdHi_Object=MibTableColumn
cdot3OamEventLogThresholdHi=_Cdot3OamEventLogThresholdHi_Object((1,3,6,1,4,1,9,10,136,1,6,1,8),_Cdot3OamEventLogThresholdHi_Type())
cdot3OamEventLogThresholdHi.setMaxAccess(_C)
if mibBuilder.loadTexts:cdot3OamEventLogThresholdHi.setStatus(_B)
_Cdot3OamEventLogThresholdLo_Type=Unsigned32
_Cdot3OamEventLogThresholdLo_Object=MibTableColumn
cdot3OamEventLogThresholdLo=_Cdot3OamEventLogThresholdLo_Object((1,3,6,1,4,1,9,10,136,1,6,1,9),_Cdot3OamEventLogThresholdLo_Type())
cdot3OamEventLogThresholdLo.setMaxAccess(_C)
if mibBuilder.loadTexts:cdot3OamEventLogThresholdLo.setStatus(_B)
_Cdot3OamEventLogValue_Type=CounterBasedGauge64
_Cdot3OamEventLogValue_Object=MibTableColumn
cdot3OamEventLogValue=_Cdot3OamEventLogValue_Object((1,3,6,1,4,1,9,10,136,1,6,1,10),_Cdot3OamEventLogValue_Type())
cdot3OamEventLogValue.setMaxAccess(_C)
if mibBuilder.loadTexts:cdot3OamEventLogValue.setStatus(_B)
_Cdot3OamEventLogRunningTotal_Type=CounterBasedGauge64
_Cdot3OamEventLogRunningTotal_Object=MibTableColumn
cdot3OamEventLogRunningTotal=_Cdot3OamEventLogRunningTotal_Object((1,3,6,1,4,1,9,10,136,1,6,1,11),_Cdot3OamEventLogRunningTotal_Type())
cdot3OamEventLogRunningTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:cdot3OamEventLogRunningTotal.setStatus(_B)
_Cdot3OamEventLogEventTotal_Type=Unsigned32
_Cdot3OamEventLogEventTotal_Object=MibTableColumn
cdot3OamEventLogEventTotal=_Cdot3OamEventLogEventTotal_Object((1,3,6,1,4,1,9,10,136,1,6,1,12),_Cdot3OamEventLogEventTotal_Type())
cdot3OamEventLogEventTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:cdot3OamEventLogEventTotal.setStatus(_B)
_Cdot3OamConformance_ObjectIdentity=ObjectIdentity
cdot3OamConformance=_Cdot3OamConformance_ObjectIdentity((1,3,6,1,4,1,9,10,136,2))
_Cdot3OamGroups_ObjectIdentity=ObjectIdentity
cdot3OamGroups=_Cdot3OamGroups_ObjectIdentity((1,3,6,1,4,1,9,10,136,2,1))
_Cdot3OamCompliances_ObjectIdentity=ObjectIdentity
cdot3OamCompliances=_Cdot3OamCompliances_ObjectIdentity((1,3,6,1,4,1,9,10,136,2,2))
cdot3OamControlGroup=ObjectGroup((1,3,6,1,4,1,9,10,136,2,1,1))
cdot3OamControlGroup.setObjects(*((_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n)))
if mibBuilder.loadTexts:cdot3OamControlGroup.setStatus(_B)
cdot3OamPeerGroup=ObjectGroup((1,3,6,1,4,1,9,10,136,2,1,2))
cdot3OamPeerGroup.setObjects(*((_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u)))
if mibBuilder.loadTexts:cdot3OamPeerGroup.setStatus(_B)
cdot3OamStatsBaseGroup=ObjectGroup((1,3,6,1,4,1,9,10,136,2,1,3))
cdot3OamStatsBaseGroup.setObjects(*((_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA),(_A,_AB)))
if mibBuilder.loadTexts:cdot3OamStatsBaseGroup.setStatus(_B)
cdot3OamLoopbackGroup=ObjectGroup((1,3,6,1,4,1,9,10,136,2,1,4))
cdot3OamLoopbackGroup.setObjects(*((_A,_AC),(_A,_AD)))
if mibBuilder.loadTexts:cdot3OamLoopbackGroup.setStatus(_B)
cdot3OamErrSymbolPeriodEventGroup=ObjectGroup((1,3,6,1,4,1,9,10,136,2,1,5))
cdot3OamErrSymbolPeriodEventGroup.setObjects(*((_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI)))
if mibBuilder.loadTexts:cdot3OamErrSymbolPeriodEventGroup.setStatus(_B)
cdot3OamErrFramePeriodEventGroup=ObjectGroup((1,3,6,1,4,1,9,10,136,2,1,6))
cdot3OamErrFramePeriodEventGroup.setObjects(*((_A,_AJ),(_A,_AK),(_A,_AL)))
if mibBuilder.loadTexts:cdot3OamErrFramePeriodEventGroup.setStatus(_B)
cdot3OamErrFrameEventGroup=ObjectGroup((1,3,6,1,4,1,9,10,136,2,1,7))
cdot3OamErrFrameEventGroup.setObjects(*((_A,_AM),(_A,_AN),(_A,_AO)))
if mibBuilder.loadTexts:cdot3OamErrFrameEventGroup.setStatus(_B)
cdot3OamErrFrameSecsSummaryEventGroup=ObjectGroup((1,3,6,1,4,1,9,10,136,2,1,8))
cdot3OamErrFrameSecsSummaryEventGroup.setObjects(*((_A,_AP),(_A,_AQ),(_A,_AR)))
if mibBuilder.loadTexts:cdot3OamErrFrameSecsSummaryEventGroup.setStatus(_B)
cdot3OamFlagEventGroup=ObjectGroup((1,3,6,1,4,1,9,10,136,2,1,9))
cdot3OamFlagEventGroup.setObjects(*((_A,_AS),(_A,_AT)))
if mibBuilder.loadTexts:cdot3OamFlagEventGroup.setStatus(_B)
cdot3OamEventLogGroup=ObjectGroup((1,3,6,1,4,1,9,10,136,2,1,10))
cdot3OamEventLogGroup.setObjects(*((_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_N)))
if mibBuilder.loadTexts:cdot3OamEventLogGroup.setStatus(_B)
cdot3OamThresholdEvent=NotificationType((1,3,6,1,4,1,9,10,136,0,1))
cdot3OamThresholdEvent.setObjects(*((_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_N)))
if mibBuilder.loadTexts:cdot3OamThresholdEvent.setStatus(_B)
cdot3OamNonThresholdEvent=NotificationType((1,3,6,1,4,1,9,10,136,0,2))
cdot3OamNonThresholdEvent.setObjects(*((_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:cdot3OamNonThresholdEvent.setStatus(_B)
cdot3OamNotificationGroup=NotificationGroup((1,3,6,1,4,1,9,10,136,2,1,11))
cdot3OamNotificationGroup.setObjects(*((_A,_AU),(_A,_AV)))
if mibBuilder.loadTexts:cdot3OamNotificationGroup.setStatus(_B)
cdot3OamCompliance=ModuleCompliance((1,3,6,1,4,1,9,10,136,2,2,1))
cdot3OamCompliance.setObjects(*((_A,_AW),(_A,_AX),(_A,_AY),(_A,_AZ),(_A,_Aa),(_A,_Ab),(_A,_Ac),(_A,_Ad),(_A,_Ae),(_A,_Af),(_A,_Ag)))
if mibBuilder.loadTexts:cdot3OamCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'Cdot3Oui':Cdot3Oui,'cdot3OamMIB':cdot3OamMIB,'cdot3OamNotifications':cdot3OamNotifications,_AU:cdot3OamThresholdEvent,_AV:cdot3OamNonThresholdEvent,'cdot3OamObjects':cdot3OamObjects,'cdot3OamTable':cdot3OamTable,'cdot3OamEntry':cdot3OamEntry,_i:cdot3OamAdminState,_j:cdot3OamOperStatus,_k:cdot3OamMode,_l:cdot3OamMaxOamPduSize,_m:cdot3OamConfigRevision,_n:cdot3OamFunctionsSupported,'cdot3OamPeerTable':cdot3OamPeerTable,'cdot3OamPeerEntry':cdot3OamPeerEntry,_o:cdot3OamPeerMacAddress,_p:cdot3OamPeerVendorOui,_q:cdot3OamPeerVendorInfo,_r:cdot3OamPeerMode,_t:cdot3OamPeerMaxOamPduSize,_u:cdot3OamPeerConfigRevision,_s:cdot3OamPeerFunctionsSupported,'cdot3OamLoopbackTable':cdot3OamLoopbackTable,'cdot3OamLoopbackEntry':cdot3OamLoopbackEntry,_AC:cdot3OamLoopbackStatus,_AD:cdot3OamLoopbackIgnoreRx,'cdot3OamStatsTable':cdot3OamStatsTable,'cdot3OamStatsEntry':cdot3OamStatsEntry,_v:cdot3OamInformationTx,_w:cdot3OamInformationRx,_x:cdot3OamUniqueEventNotificationTx,_y:cdot3OamUniqueEventNotificationRx,_z:cdot3OamDuplicateEventNotificationTx,_A0:cdot3OamDuplicateEventNotificationRx,_A1:cdot3OamLoopbackControlTx,_A2:cdot3OamLoopbackControlRx,_A3:cdot3OamVariableRequestTx,_A4:cdot3OamVariableRequestRx,_A5:cdot3OamVariableResponseTx,_A6:cdot3OamVariableResponseRx,_A7:cdot3OamOrgSpecificTx,_A8:cdot3OamOrgSpecificRx,_A9:cdot3OamUnsupportedCodesTx,_AA:cdot3OamUnsupportedCodesRx,_AB:cdot3OamFramesLostDueToOam,'cdot3OamEventConfigTable':cdot3OamEventConfigTable,'cdot3OamEventConfigEntry':cdot3OamEventConfigEntry,_AE:cdot3OamErrSymPeriodWindowHi,_AF:cdot3OamErrSymPeriodWindowLo,_AG:cdot3OamErrSymPeriodThresholdHi,_AH:cdot3OamErrSymPeriodThresholdLo,_AI:cdot3OamErrSymPeriodEvNotifEnable,_AJ:cdot3OamErrFramePeriodWindow,_AK:cdot3OamErrFramePeriodThreshold,_AL:cdot3OamErrFramePeriodEvNotifEnable,_AM:cdot3OamErrFrameWindow,_AN:cdot3OamErrFrameThreshold,_AO:cdot3OamErrFrameEvNotifEnable,_AP:cdot3OamErrFrameSecsSummaryWindow,_AQ:cdot3OamErrFrameSecsSummaryThreshold,_AR:cdot3OamErrFrameSecsEvNotifEnable,_AS:cdot3OamDyingGaspEnable,_AT:cdot3OamCriticalEventEnable,'cdot3OamEventLogTable':cdot3OamEventLogTable,'cdot3OamEventLogEntry':cdot3OamEventLogEntry,_h:cdot3OamEventLogIndex,_J:cdot3OamEventLogTimestamp,_K:cdot3OamEventLogOui,_L:cdot3OamEventLogType,_M:cdot3OamEventLogLocation,_P:cdot3OamEventLogWindowHi,_Q:cdot3OamEventLogWindowLo,_R:cdot3OamEventLogThresholdHi,_S:cdot3OamEventLogThresholdLo,_T:cdot3OamEventLogValue,_U:cdot3OamEventLogRunningTotal,_N:cdot3OamEventLogEventTotal,'cdot3OamConformance':cdot3OamConformance,'cdot3OamGroups':cdot3OamGroups,_AW:cdot3OamControlGroup,_AX:cdot3OamPeerGroup,_AY:cdot3OamStatsBaseGroup,_AZ:cdot3OamLoopbackGroup,_Aa:cdot3OamErrSymbolPeriodEventGroup,_Ab:cdot3OamErrFramePeriodEventGroup,_Ac:cdot3OamErrFrameEventGroup,_Ad:cdot3OamErrFrameSecsSummaryEventGroup,_Ae:cdot3OamFlagEventGroup,_Af:cdot3OamEventLogGroup,_Ag:cdot3OamNotificationGroup,'cdot3OamCompliances':cdot3OamCompliances,'cdot3OamCompliance':cdot3OamCompliance})