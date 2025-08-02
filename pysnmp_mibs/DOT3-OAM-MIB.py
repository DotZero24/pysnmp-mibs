_Ah='dot3OamNotificationGroup'
_Ag='dot3OamEventLogGroup'
_Af='dot3OamFlagEventGroup'
_Ae='dot3OamErrFrameSecsSummaryEventGroup'
_Ad='dot3OamErrFrameEventGroup'
_Ac='dot3OamErrFramePeriodEventGroup'
_Ab='dot3OamErrSymbolPeriodEventGroup'
_Aa='dot3OamLoopbackGroup'
_AZ='dot3OamStatsBaseGroup'
_AY='dot3OamPeerGroup'
_AX='dot3OamControlGroup'
_AW='dot3OamNonThresholdEvent'
_AV='dot3OamThresholdEvent'
_AU='dot3OamCriticalEventEnable'
_AT='dot3OamDyingGaspEnable'
_AS='dot3OamErrFrameSecsEvNotifEnable'
_AR='dot3OamErrFrameSecsSummaryThreshold'
_AQ='dot3OamErrFrameSecsSummaryWindow'
_AP='dot3OamErrFrameEvNotifEnable'
_AO='dot3OamErrFrameThreshold'
_AN='dot3OamErrFrameWindow'
_AM='dot3OamErrFramePeriodEvNotifEnable'
_AL='dot3OamErrFramePeriodThreshold'
_AK='dot3OamErrFramePeriodWindow'
_AJ='dot3OamErrSymPeriodEvNotifEnable'
_AI='dot3OamErrSymPeriodThresholdLo'
_AH='dot3OamErrSymPeriodThresholdHi'
_AG='dot3OamErrSymPeriodWindowLo'
_AF='dot3OamErrSymPeriodWindowHi'
_AE='dot3OamLoopbackIgnoreRx'
_AD='dot3OamLoopbackStatus'
_AC='dot3OamFramesLostDueToOam'
_AB='dot3OamUnsupportedCodesRx'
_AA='dot3OamUnsupportedCodesTx'
_A9='dot3OamOrgSpecificRx'
_A8='dot3OamOrgSpecificTx'
_A7='dot3OamVariableResponseRx'
_A6='dot3OamVariableResponseTx'
_A5='dot3OamVariableRequestRx'
_A4='dot3OamVariableRequestTx'
_A3='dot3OamLoopbackControlRx'
_A2='dot3OamLoopbackControlTx'
_A1='dot3OamDuplicateEventNotificationRx'
_A0='dot3OamDuplicateEventNotificationTx'
_z='dot3OamUniqueEventNotificationRx'
_y='dot3OamUniqueEventNotificationTx'
_x='dot3OamInformationRx'
_w='dot3OamInformationTx'
_v='dot3OamPeerConfigRevision'
_u='dot3OamPeerMaxOamPduSize'
_t='dot3OamPeerFunctionsSupported'
_s='dot3OamPeerMode'
_r='dot3OamPeerVendorInfo'
_q='dot3OamPeerVendorOui'
_p='dot3OamPeerMacAddress'
_o='dot3OamFunctionsSupported'
_n='dot3OamConfigRevision'
_m='dot3OamMaxOamPduSize'
_l='dot3OamMode'
_k='dot3OamOperStatus'
_j='dot3OamAdminState'
_i='dot3OamEventLogIndex'
_h='tenths of a second'
_g='symbols'
_f='2^32 symbols'
_e='unknown'
_d='variableSupport'
_c='eventSupport'
_b='loopbackSupport'
_a='unidirectionalSupport'
_Z='octets'
_Y='active'
_X='passive'
_W='disabled'
_V='dot3OamEventLogRunningTotal'
_U='dot3OamEventLogValue'
_T='dot3OamEventLogThresholdLo'
_S='dot3OamEventLogThresholdHi'
_R='dot3OamEventLogWindowLo'
_Q='dot3OamEventLogWindowHi'
_P='Bits'
_O='dot3OamEventLogEventTotal'
_N='dot3OamEventLogLocation'
_M='dot3OamEventLogType'
_L='dot3OamEventLogOui'
_K='dot3OamEventLogTimestamp'
_J='TruthValue'
_I='ifIndex'
_H='IF-MIB'
_G='Unsigned32'
_F='Integer32'
_E='frames'
_D='read-write'
_C='read-only'
_B='current'
_A='DOT3-OAM-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
CounterBasedGauge64,=mibBuilder.importSymbols('HCNUM-TC','CounterBasedGauge64')
ifIndex,=mibBuilder.importSymbols(_H,_I)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI',_P,'Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso','mib-2')
DisplayString,MacAddress,PhysAddress,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention','TimeStamp',_J)
dot3OamMIB=ModuleIdentity((1,3,6,1,2,1,158))
if mibBuilder.loadTexts:dot3OamMIB.setRevisions(('2007-06-14 00:00',))
class EightOTwoOui(TextualConvention,OctetString):status=_B;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,3));fixedLength=3
_Dot3OamNotifications_ObjectIdentity=ObjectIdentity
dot3OamNotifications=_Dot3OamNotifications_ObjectIdentity((1,3,6,1,2,1,158,0))
_Dot3OamObjects_ObjectIdentity=ObjectIdentity
dot3OamObjects=_Dot3OamObjects_ObjectIdentity((1,3,6,1,2,1,158,1))
_Dot3OamTable_Object=MibTable
dot3OamTable=_Dot3OamTable_Object((1,3,6,1,2,1,158,1,1))
if mibBuilder.loadTexts:dot3OamTable.setStatus(_B)
_Dot3OamEntry_Object=MibTableRow
dot3OamEntry=_Dot3OamEntry_Object((1,3,6,1,2,1,158,1,1,1))
dot3OamEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:dot3OamEntry.setStatus(_B)
class _Dot3OamAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),(_W,2)))
_Dot3OamAdminState_Type.__name__=_F
_Dot3OamAdminState_Object=MibTableColumn
dot3OamAdminState=_Dot3OamAdminState_Object((1,3,6,1,2,1,158,1,1,1,1),_Dot3OamAdminState_Type())
dot3OamAdminState.setMaxAccess(_D)
if mibBuilder.loadTexts:dot3OamAdminState.setStatus(_B)
class _Dot3OamOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_W,1),('linkFault',2),('passiveWait',3),('activeSendLocal',4),('sendLocalAndRemote',5),('sendLocalAndRemoteOk',6),('oamPeeringLocallyRejected',7),('oamPeeringRemotelyRejected',8),('operational',9),('nonOperHalfDuplex',10)))
_Dot3OamOperStatus_Type.__name__=_F
_Dot3OamOperStatus_Object=MibTableColumn
dot3OamOperStatus=_Dot3OamOperStatus_Object((1,3,6,1,2,1,158,1,1,1,2),_Dot3OamOperStatus_Type())
dot3OamOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3OamOperStatus.setStatus(_B)
class _Dot3OamMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_X,1),(_Y,2)))
_Dot3OamMode_Type.__name__=_F
_Dot3OamMode_Object=MibTableColumn
dot3OamMode=_Dot3OamMode_Object((1,3,6,1,2,1,158,1,1,1,3),_Dot3OamMode_Type())
dot3OamMode.setMaxAccess(_D)
if mibBuilder.loadTexts:dot3OamMode.setStatus(_B)
class _Dot3OamMaxOamPduSize_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(64,1518))
_Dot3OamMaxOamPduSize_Type.__name__=_G
_Dot3OamMaxOamPduSize_Object=MibTableColumn
dot3OamMaxOamPduSize=_Dot3OamMaxOamPduSize_Object((1,3,6,1,2,1,158,1,1,1,4),_Dot3OamMaxOamPduSize_Type())
dot3OamMaxOamPduSize.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3OamMaxOamPduSize.setStatus(_B)
if mibBuilder.loadTexts:dot3OamMaxOamPduSize.setUnits(_Z)
class _Dot3OamConfigRevision_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Dot3OamConfigRevision_Type.__name__=_G
_Dot3OamConfigRevision_Object=MibTableColumn
dot3OamConfigRevision=_Dot3OamConfigRevision_Object((1,3,6,1,2,1,158,1,1,1,5),_Dot3OamConfigRevision_Type())
dot3OamConfigRevision.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3OamConfigRevision.setStatus(_B)
class _Dot3OamFunctionsSupported_Type(Bits):namedValues=NamedValues(*((_a,0),(_b,1),(_c,2),(_d,3)))
_Dot3OamFunctionsSupported_Type.__name__=_P
_Dot3OamFunctionsSupported_Object=MibTableColumn
dot3OamFunctionsSupported=_Dot3OamFunctionsSupported_Object((1,3,6,1,2,1,158,1,1,1,6),_Dot3OamFunctionsSupported_Type())
dot3OamFunctionsSupported.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3OamFunctionsSupported.setStatus(_B)
_Dot3OamPeerTable_Object=MibTable
dot3OamPeerTable=_Dot3OamPeerTable_Object((1,3,6,1,2,1,158,1,2))
if mibBuilder.loadTexts:dot3OamPeerTable.setStatus(_B)
_Dot3OamPeerEntry_Object=MibTableRow
dot3OamPeerEntry=_Dot3OamPeerEntry_Object((1,3,6,1,2,1,158,1,2,1))
dot3OamPeerEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:dot3OamPeerEntry.setStatus(_B)
_Dot3OamPeerMacAddress_Type=MacAddress
_Dot3OamPeerMacAddress_Object=MibTableColumn
dot3OamPeerMacAddress=_Dot3OamPeerMacAddress_Object((1,3,6,1,2,1,158,1,2,1,1),_Dot3OamPeerMacAddress_Type())
dot3OamPeerMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3OamPeerMacAddress.setStatus(_B)
_Dot3OamPeerVendorOui_Type=EightOTwoOui
_Dot3OamPeerVendorOui_Object=MibTableColumn
dot3OamPeerVendorOui=_Dot3OamPeerVendorOui_Object((1,3,6,1,2,1,158,1,2,1,2),_Dot3OamPeerVendorOui_Type())
dot3OamPeerVendorOui.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3OamPeerVendorOui.setStatus(_B)
_Dot3OamPeerVendorInfo_Type=Unsigned32
_Dot3OamPeerVendorInfo_Object=MibTableColumn
dot3OamPeerVendorInfo=_Dot3OamPeerVendorInfo_Object((1,3,6,1,2,1,158,1,2,1,3),_Dot3OamPeerVendorInfo_Type())
dot3OamPeerVendorInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3OamPeerVendorInfo.setStatus(_B)
class _Dot3OamPeerMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_X,1),(_Y,2),(_e,3)))
_Dot3OamPeerMode_Type.__name__=_F
_Dot3OamPeerMode_Object=MibTableColumn
dot3OamPeerMode=_Dot3OamPeerMode_Object((1,3,6,1,2,1,158,1,2,1,4),_Dot3OamPeerMode_Type())
dot3OamPeerMode.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3OamPeerMode.setStatus(_B)
class _Dot3OamPeerMaxOamPduSize_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(64,1518))
_Dot3OamPeerMaxOamPduSize_Type.__name__=_G
_Dot3OamPeerMaxOamPduSize_Object=MibTableColumn
dot3OamPeerMaxOamPduSize=_Dot3OamPeerMaxOamPduSize_Object((1,3,6,1,2,1,158,1,2,1,5),_Dot3OamPeerMaxOamPduSize_Type())
dot3OamPeerMaxOamPduSize.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3OamPeerMaxOamPduSize.setStatus(_B)
if mibBuilder.loadTexts:dot3OamPeerMaxOamPduSize.setUnits(_Z)
class _Dot3OamPeerConfigRevision_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Dot3OamPeerConfigRevision_Type.__name__=_G
_Dot3OamPeerConfigRevision_Object=MibTableColumn
dot3OamPeerConfigRevision=_Dot3OamPeerConfigRevision_Object((1,3,6,1,2,1,158,1,2,1,6),_Dot3OamPeerConfigRevision_Type())
dot3OamPeerConfigRevision.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3OamPeerConfigRevision.setStatus(_B)
class _Dot3OamPeerFunctionsSupported_Type(Bits):namedValues=NamedValues(*((_a,0),(_b,1),(_c,2),(_d,3)))
_Dot3OamPeerFunctionsSupported_Type.__name__=_P
_Dot3OamPeerFunctionsSupported_Object=MibTableColumn
dot3OamPeerFunctionsSupported=_Dot3OamPeerFunctionsSupported_Object((1,3,6,1,2,1,158,1,2,1,7),_Dot3OamPeerFunctionsSupported_Type())
dot3OamPeerFunctionsSupported.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3OamPeerFunctionsSupported.setStatus(_B)
_Dot3OamLoopbackTable_Object=MibTable
dot3OamLoopbackTable=_Dot3OamLoopbackTable_Object((1,3,6,1,2,1,158,1,3))
if mibBuilder.loadTexts:dot3OamLoopbackTable.setStatus(_B)
_Dot3OamLoopbackEntry_Object=MibTableRow
dot3OamLoopbackEntry=_Dot3OamLoopbackEntry_Object((1,3,6,1,2,1,158,1,3,1))
dot3OamLoopbackEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:dot3OamLoopbackEntry.setStatus(_B)
class _Dot3OamLoopbackStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('noLoopback',1),('initiatingLoopback',2),('remoteLoopback',3),('terminatingLoopback',4),('localLoopback',5),(_e,6)))
_Dot3OamLoopbackStatus_Type.__name__=_F
_Dot3OamLoopbackStatus_Object=MibTableColumn
dot3OamLoopbackStatus=_Dot3OamLoopbackStatus_Object((1,3,6,1,2,1,158,1,3,1,1),_Dot3OamLoopbackStatus_Type())
dot3OamLoopbackStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:dot3OamLoopbackStatus.setStatus(_B)
class _Dot3OamLoopbackIgnoreRx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ignore',1),('process',2)))
_Dot3OamLoopbackIgnoreRx_Type.__name__=_F
_Dot3OamLoopbackIgnoreRx_Object=MibTableColumn
dot3OamLoopbackIgnoreRx=_Dot3OamLoopbackIgnoreRx_Object((1,3,6,1,2,1,158,1,3,1,2),_Dot3OamLoopbackIgnoreRx_Type())
dot3OamLoopbackIgnoreRx.setMaxAccess(_D)
if mibBuilder.loadTexts:dot3OamLoopbackIgnoreRx.setStatus(_B)
_Dot3OamStatsTable_Object=MibTable
dot3OamStatsTable=_Dot3OamStatsTable_Object((1,3,6,1,2,1,158,1,4))
if mibBuilder.loadTexts:dot3OamStatsTable.setStatus(_B)
_Dot3OamStatsEntry_Object=MibTableRow
dot3OamStatsEntry=_Dot3OamStatsEntry_Object((1,3,6,1,2,1,158,1,4,1))
dot3OamStatsEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:dot3OamStatsEntry.setStatus(_B)
_Dot3OamInformationTx_Type=Counter32
_Dot3OamInformationTx_Object=MibTableColumn
dot3OamInformationTx=_Dot3OamInformationTx_Object((1,3,6,1,2,1,158,1,4,1,1),_Dot3OamInformationTx_Type())
dot3OamInformationTx.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3OamInformationTx.setStatus(_B)
if mibBuilder.loadTexts:dot3OamInformationTx.setUnits(_E)
_Dot3OamInformationRx_Type=Counter32
_Dot3OamInformationRx_Object=MibTableColumn
dot3OamInformationRx=_Dot3OamInformationRx_Object((1,3,6,1,2,1,158,1,4,1,2),_Dot3OamInformationRx_Type())
dot3OamInformationRx.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3OamInformationRx.setStatus(_B)
if mibBuilder.loadTexts:dot3OamInformationRx.setUnits(_E)
_Dot3OamUniqueEventNotificationTx_Type=Counter32
_Dot3OamUniqueEventNotificationTx_Object=MibTableColumn
dot3OamUniqueEventNotificationTx=_Dot3OamUniqueEventNotificationTx_Object((1,3,6,1,2,1,158,1,4,1,3),_Dot3OamUniqueEventNotificationTx_Type())
dot3OamUniqueEventNotificationTx.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3OamUniqueEventNotificationTx.setStatus(_B)
if mibBuilder.loadTexts:dot3OamUniqueEventNotificationTx.setUnits(_E)
_Dot3OamUniqueEventNotificationRx_Type=Counter32
_Dot3OamUniqueEventNotificationRx_Object=MibTableColumn
dot3OamUniqueEventNotificationRx=_Dot3OamUniqueEventNotificationRx_Object((1,3,6,1,2,1,158,1,4,1,4),_Dot3OamUniqueEventNotificationRx_Type())
dot3OamUniqueEventNotificationRx.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3OamUniqueEventNotificationRx.setStatus(_B)
if mibBuilder.loadTexts:dot3OamUniqueEventNotificationRx.setUnits(_E)
_Dot3OamDuplicateEventNotificationTx_Type=Counter32
_Dot3OamDuplicateEventNotificationTx_Object=MibTableColumn
dot3OamDuplicateEventNotificationTx=_Dot3OamDuplicateEventNotificationTx_Object((1,3,6,1,2,1,158,1,4,1,5),_Dot3OamDuplicateEventNotificationTx_Type())
dot3OamDuplicateEventNotificationTx.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3OamDuplicateEventNotificationTx.setStatus(_B)
if mibBuilder.loadTexts:dot3OamDuplicateEventNotificationTx.setUnits(_E)
_Dot3OamDuplicateEventNotificationRx_Type=Counter32
_Dot3OamDuplicateEventNotificationRx_Object=MibTableColumn
dot3OamDuplicateEventNotificationRx=_Dot3OamDuplicateEventNotificationRx_Object((1,3,6,1,2,1,158,1,4,1,6),_Dot3OamDuplicateEventNotificationRx_Type())
dot3OamDuplicateEventNotificationRx.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3OamDuplicateEventNotificationRx.setStatus(_B)
if mibBuilder.loadTexts:dot3OamDuplicateEventNotificationRx.setUnits(_E)
_Dot3OamLoopbackControlTx_Type=Counter32
_Dot3OamLoopbackControlTx_Object=MibTableColumn
dot3OamLoopbackControlTx=_Dot3OamLoopbackControlTx_Object((1,3,6,1,2,1,158,1,4,1,7),_Dot3OamLoopbackControlTx_Type())
dot3OamLoopbackControlTx.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3OamLoopbackControlTx.setStatus(_B)
if mibBuilder.loadTexts:dot3OamLoopbackControlTx.setUnits(_E)
_Dot3OamLoopbackControlRx_Type=Counter32
_Dot3OamLoopbackControlRx_Object=MibTableColumn
dot3OamLoopbackControlRx=_Dot3OamLoopbackControlRx_Object((1,3,6,1,2,1,158,1,4,1,8),_Dot3OamLoopbackControlRx_Type())
dot3OamLoopbackControlRx.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3OamLoopbackControlRx.setStatus(_B)
if mibBuilder.loadTexts:dot3OamLoopbackControlRx.setUnits(_E)
_Dot3OamVariableRequestTx_Type=Counter32
_Dot3OamVariableRequestTx_Object=MibTableColumn
dot3OamVariableRequestTx=_Dot3OamVariableRequestTx_Object((1,3,6,1,2,1,158,1,4,1,9),_Dot3OamVariableRequestTx_Type())
dot3OamVariableRequestTx.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3OamVariableRequestTx.setStatus(_B)
if mibBuilder.loadTexts:dot3OamVariableRequestTx.setUnits(_E)
_Dot3OamVariableRequestRx_Type=Counter32
_Dot3OamVariableRequestRx_Object=MibTableColumn
dot3OamVariableRequestRx=_Dot3OamVariableRequestRx_Object((1,3,6,1,2,1,158,1,4,1,10),_Dot3OamVariableRequestRx_Type())
dot3OamVariableRequestRx.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3OamVariableRequestRx.setStatus(_B)
if mibBuilder.loadTexts:dot3OamVariableRequestRx.setUnits(_E)
_Dot3OamVariableResponseTx_Type=Counter32
_Dot3OamVariableResponseTx_Object=MibTableColumn
dot3OamVariableResponseTx=_Dot3OamVariableResponseTx_Object((1,3,6,1,2,1,158,1,4,1,11),_Dot3OamVariableResponseTx_Type())
dot3OamVariableResponseTx.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3OamVariableResponseTx.setStatus(_B)
if mibBuilder.loadTexts:dot3OamVariableResponseTx.setUnits(_E)
_Dot3OamVariableResponseRx_Type=Counter32
_Dot3OamVariableResponseRx_Object=MibTableColumn
dot3OamVariableResponseRx=_Dot3OamVariableResponseRx_Object((1,3,6,1,2,1,158,1,4,1,12),_Dot3OamVariableResponseRx_Type())
dot3OamVariableResponseRx.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3OamVariableResponseRx.setStatus(_B)
if mibBuilder.loadTexts:dot3OamVariableResponseRx.setUnits(_E)
_Dot3OamOrgSpecificTx_Type=Counter32
_Dot3OamOrgSpecificTx_Object=MibTableColumn
dot3OamOrgSpecificTx=_Dot3OamOrgSpecificTx_Object((1,3,6,1,2,1,158,1,4,1,13),_Dot3OamOrgSpecificTx_Type())
dot3OamOrgSpecificTx.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3OamOrgSpecificTx.setStatus(_B)
if mibBuilder.loadTexts:dot3OamOrgSpecificTx.setUnits(_E)
_Dot3OamOrgSpecificRx_Type=Counter32
_Dot3OamOrgSpecificRx_Object=MibTableColumn
dot3OamOrgSpecificRx=_Dot3OamOrgSpecificRx_Object((1,3,6,1,2,1,158,1,4,1,14),_Dot3OamOrgSpecificRx_Type())
dot3OamOrgSpecificRx.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3OamOrgSpecificRx.setStatus(_B)
if mibBuilder.loadTexts:dot3OamOrgSpecificRx.setUnits(_E)
_Dot3OamUnsupportedCodesTx_Type=Counter32
_Dot3OamUnsupportedCodesTx_Object=MibTableColumn
dot3OamUnsupportedCodesTx=_Dot3OamUnsupportedCodesTx_Object((1,3,6,1,2,1,158,1,4,1,15),_Dot3OamUnsupportedCodesTx_Type())
dot3OamUnsupportedCodesTx.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3OamUnsupportedCodesTx.setStatus(_B)
if mibBuilder.loadTexts:dot3OamUnsupportedCodesTx.setUnits(_E)
_Dot3OamUnsupportedCodesRx_Type=Counter32
_Dot3OamUnsupportedCodesRx_Object=MibTableColumn
dot3OamUnsupportedCodesRx=_Dot3OamUnsupportedCodesRx_Object((1,3,6,1,2,1,158,1,4,1,16),_Dot3OamUnsupportedCodesRx_Type())
dot3OamUnsupportedCodesRx.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3OamUnsupportedCodesRx.setStatus(_B)
if mibBuilder.loadTexts:dot3OamUnsupportedCodesRx.setUnits(_E)
_Dot3OamFramesLostDueToOam_Type=Counter32
_Dot3OamFramesLostDueToOam_Object=MibTableColumn
dot3OamFramesLostDueToOam=_Dot3OamFramesLostDueToOam_Object((1,3,6,1,2,1,158,1,4,1,17),_Dot3OamFramesLostDueToOam_Type())
dot3OamFramesLostDueToOam.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3OamFramesLostDueToOam.setStatus(_B)
if mibBuilder.loadTexts:dot3OamFramesLostDueToOam.setUnits(_E)
_Dot3OamEventConfigTable_Object=MibTable
dot3OamEventConfigTable=_Dot3OamEventConfigTable_Object((1,3,6,1,2,1,158,1,5))
if mibBuilder.loadTexts:dot3OamEventConfigTable.setStatus(_B)
_Dot3OamEventConfigEntry_Object=MibTableRow
dot3OamEventConfigEntry=_Dot3OamEventConfigEntry_Object((1,3,6,1,2,1,158,1,5,1))
dot3OamEventConfigEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:dot3OamEventConfigEntry.setStatus(_B)
_Dot3OamErrSymPeriodWindowHi_Type=Unsigned32
_Dot3OamErrSymPeriodWindowHi_Object=MibTableColumn
dot3OamErrSymPeriodWindowHi=_Dot3OamErrSymPeriodWindowHi_Object((1,3,6,1,2,1,158,1,5,1,1),_Dot3OamErrSymPeriodWindowHi_Type())
dot3OamErrSymPeriodWindowHi.setMaxAccess(_D)
if mibBuilder.loadTexts:dot3OamErrSymPeriodWindowHi.setStatus(_B)
if mibBuilder.loadTexts:dot3OamErrSymPeriodWindowHi.setUnits(_f)
_Dot3OamErrSymPeriodWindowLo_Type=Unsigned32
_Dot3OamErrSymPeriodWindowLo_Object=MibTableColumn
dot3OamErrSymPeriodWindowLo=_Dot3OamErrSymPeriodWindowLo_Object((1,3,6,1,2,1,158,1,5,1,2),_Dot3OamErrSymPeriodWindowLo_Type())
dot3OamErrSymPeriodWindowLo.setMaxAccess(_D)
if mibBuilder.loadTexts:dot3OamErrSymPeriodWindowLo.setStatus(_B)
if mibBuilder.loadTexts:dot3OamErrSymPeriodWindowLo.setUnits(_g)
_Dot3OamErrSymPeriodThresholdHi_Type=Unsigned32
_Dot3OamErrSymPeriodThresholdHi_Object=MibTableColumn
dot3OamErrSymPeriodThresholdHi=_Dot3OamErrSymPeriodThresholdHi_Object((1,3,6,1,2,1,158,1,5,1,3),_Dot3OamErrSymPeriodThresholdHi_Type())
dot3OamErrSymPeriodThresholdHi.setMaxAccess(_D)
if mibBuilder.loadTexts:dot3OamErrSymPeriodThresholdHi.setStatus(_B)
if mibBuilder.loadTexts:dot3OamErrSymPeriodThresholdHi.setUnits(_f)
_Dot3OamErrSymPeriodThresholdLo_Type=Unsigned32
_Dot3OamErrSymPeriodThresholdLo_Object=MibTableColumn
dot3OamErrSymPeriodThresholdLo=_Dot3OamErrSymPeriodThresholdLo_Object((1,3,6,1,2,1,158,1,5,1,4),_Dot3OamErrSymPeriodThresholdLo_Type())
dot3OamErrSymPeriodThresholdLo.setMaxAccess(_D)
if mibBuilder.loadTexts:dot3OamErrSymPeriodThresholdLo.setStatus(_B)
if mibBuilder.loadTexts:dot3OamErrSymPeriodThresholdLo.setUnits(_g)
_Dot3OamErrSymPeriodEvNotifEnable_Type=TruthValue
_Dot3OamErrSymPeriodEvNotifEnable_Object=MibTableColumn
dot3OamErrSymPeriodEvNotifEnable=_Dot3OamErrSymPeriodEvNotifEnable_Object((1,3,6,1,2,1,158,1,5,1,5),_Dot3OamErrSymPeriodEvNotifEnable_Type())
dot3OamErrSymPeriodEvNotifEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:dot3OamErrSymPeriodEvNotifEnable.setStatus(_B)
_Dot3OamErrFramePeriodWindow_Type=Unsigned32
_Dot3OamErrFramePeriodWindow_Object=MibTableColumn
dot3OamErrFramePeriodWindow=_Dot3OamErrFramePeriodWindow_Object((1,3,6,1,2,1,158,1,5,1,6),_Dot3OamErrFramePeriodWindow_Type())
dot3OamErrFramePeriodWindow.setMaxAccess(_D)
if mibBuilder.loadTexts:dot3OamErrFramePeriodWindow.setStatus(_B)
if mibBuilder.loadTexts:dot3OamErrFramePeriodWindow.setUnits(_E)
_Dot3OamErrFramePeriodThreshold_Type=Unsigned32
_Dot3OamErrFramePeriodThreshold_Object=MibTableColumn
dot3OamErrFramePeriodThreshold=_Dot3OamErrFramePeriodThreshold_Object((1,3,6,1,2,1,158,1,5,1,7),_Dot3OamErrFramePeriodThreshold_Type())
dot3OamErrFramePeriodThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:dot3OamErrFramePeriodThreshold.setStatus(_B)
if mibBuilder.loadTexts:dot3OamErrFramePeriodThreshold.setUnits(_E)
_Dot3OamErrFramePeriodEvNotifEnable_Type=TruthValue
_Dot3OamErrFramePeriodEvNotifEnable_Object=MibTableColumn
dot3OamErrFramePeriodEvNotifEnable=_Dot3OamErrFramePeriodEvNotifEnable_Object((1,3,6,1,2,1,158,1,5,1,8),_Dot3OamErrFramePeriodEvNotifEnable_Type())
dot3OamErrFramePeriodEvNotifEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:dot3OamErrFramePeriodEvNotifEnable.setStatus(_B)
class _Dot3OamErrFrameWindow_Type(Unsigned32):defaultValue=10
_Dot3OamErrFrameWindow_Type.__name__=_G
_Dot3OamErrFrameWindow_Object=MibTableColumn
dot3OamErrFrameWindow=_Dot3OamErrFrameWindow_Object((1,3,6,1,2,1,158,1,5,1,9),_Dot3OamErrFrameWindow_Type())
dot3OamErrFrameWindow.setMaxAccess(_D)
if mibBuilder.loadTexts:dot3OamErrFrameWindow.setStatus(_B)
if mibBuilder.loadTexts:dot3OamErrFrameWindow.setUnits(_h)
class _Dot3OamErrFrameThreshold_Type(Unsigned32):defaultValue=1
_Dot3OamErrFrameThreshold_Type.__name__=_G
_Dot3OamErrFrameThreshold_Object=MibTableColumn
dot3OamErrFrameThreshold=_Dot3OamErrFrameThreshold_Object((1,3,6,1,2,1,158,1,5,1,10),_Dot3OamErrFrameThreshold_Type())
dot3OamErrFrameThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:dot3OamErrFrameThreshold.setStatus(_B)
if mibBuilder.loadTexts:dot3OamErrFrameThreshold.setUnits(_E)
class _Dot3OamErrFrameEvNotifEnable_Type(TruthValue):defaultValue=1
_Dot3OamErrFrameEvNotifEnable_Type.__name__=_J
_Dot3OamErrFrameEvNotifEnable_Object=MibTableColumn
dot3OamErrFrameEvNotifEnable=_Dot3OamErrFrameEvNotifEnable_Object((1,3,6,1,2,1,158,1,5,1,11),_Dot3OamErrFrameEvNotifEnable_Type())
dot3OamErrFrameEvNotifEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:dot3OamErrFrameEvNotifEnable.setStatus(_B)
class _Dot3OamErrFrameSecsSummaryWindow_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,9000))
_Dot3OamErrFrameSecsSummaryWindow_Type.__name__=_F
_Dot3OamErrFrameSecsSummaryWindow_Object=MibTableColumn
dot3OamErrFrameSecsSummaryWindow=_Dot3OamErrFrameSecsSummaryWindow_Object((1,3,6,1,2,1,158,1,5,1,12),_Dot3OamErrFrameSecsSummaryWindow_Type())
dot3OamErrFrameSecsSummaryWindow.setMaxAccess(_D)
if mibBuilder.loadTexts:dot3OamErrFrameSecsSummaryWindow.setStatus(_B)
if mibBuilder.loadTexts:dot3OamErrFrameSecsSummaryWindow.setUnits(_h)
class _Dot3OamErrFrameSecsSummaryThreshold_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,900))
_Dot3OamErrFrameSecsSummaryThreshold_Type.__name__=_F
_Dot3OamErrFrameSecsSummaryThreshold_Object=MibTableColumn
dot3OamErrFrameSecsSummaryThreshold=_Dot3OamErrFrameSecsSummaryThreshold_Object((1,3,6,1,2,1,158,1,5,1,13),_Dot3OamErrFrameSecsSummaryThreshold_Type())
dot3OamErrFrameSecsSummaryThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:dot3OamErrFrameSecsSummaryThreshold.setStatus(_B)
if mibBuilder.loadTexts:dot3OamErrFrameSecsSummaryThreshold.setUnits('errored frame seconds')
class _Dot3OamErrFrameSecsEvNotifEnable_Type(TruthValue):defaultValue=1
_Dot3OamErrFrameSecsEvNotifEnable_Type.__name__=_J
_Dot3OamErrFrameSecsEvNotifEnable_Object=MibTableColumn
dot3OamErrFrameSecsEvNotifEnable=_Dot3OamErrFrameSecsEvNotifEnable_Object((1,3,6,1,2,1,158,1,5,1,14),_Dot3OamErrFrameSecsEvNotifEnable_Type())
dot3OamErrFrameSecsEvNotifEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:dot3OamErrFrameSecsEvNotifEnable.setStatus(_B)
class _Dot3OamDyingGaspEnable_Type(TruthValue):defaultValue=1
_Dot3OamDyingGaspEnable_Type.__name__=_J
_Dot3OamDyingGaspEnable_Object=MibTableColumn
dot3OamDyingGaspEnable=_Dot3OamDyingGaspEnable_Object((1,3,6,1,2,1,158,1,5,1,15),_Dot3OamDyingGaspEnable_Type())
dot3OamDyingGaspEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:dot3OamDyingGaspEnable.setStatus(_B)
class _Dot3OamCriticalEventEnable_Type(TruthValue):defaultValue=1
_Dot3OamCriticalEventEnable_Type.__name__=_J
_Dot3OamCriticalEventEnable_Object=MibTableColumn
dot3OamCriticalEventEnable=_Dot3OamCriticalEventEnable_Object((1,3,6,1,2,1,158,1,5,1,16),_Dot3OamCriticalEventEnable_Type())
dot3OamCriticalEventEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:dot3OamCriticalEventEnable.setStatus(_B)
_Dot3OamEventLogTable_Object=MibTable
dot3OamEventLogTable=_Dot3OamEventLogTable_Object((1,3,6,1,2,1,158,1,6))
if mibBuilder.loadTexts:dot3OamEventLogTable.setStatus(_B)
_Dot3OamEventLogEntry_Object=MibTableRow
dot3OamEventLogEntry=_Dot3OamEventLogEntry_Object((1,3,6,1,2,1,158,1,6,1))
dot3OamEventLogEntry.setIndexNames((0,_H,_I),(0,_A,_i))
if mibBuilder.loadTexts:dot3OamEventLogEntry.setStatus(_B)
class _Dot3OamEventLogIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_Dot3OamEventLogIndex_Type.__name__=_G
_Dot3OamEventLogIndex_Object=MibTableColumn
dot3OamEventLogIndex=_Dot3OamEventLogIndex_Object((1,3,6,1,2,1,158,1,6,1,1),_Dot3OamEventLogIndex_Type())
dot3OamEventLogIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:dot3OamEventLogIndex.setStatus(_B)
_Dot3OamEventLogTimestamp_Type=TimeStamp
_Dot3OamEventLogTimestamp_Object=MibTableColumn
dot3OamEventLogTimestamp=_Dot3OamEventLogTimestamp_Object((1,3,6,1,2,1,158,1,6,1,2),_Dot3OamEventLogTimestamp_Type())
dot3OamEventLogTimestamp.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3OamEventLogTimestamp.setStatus(_B)
_Dot3OamEventLogOui_Type=EightOTwoOui
_Dot3OamEventLogOui_Object=MibTableColumn
dot3OamEventLogOui=_Dot3OamEventLogOui_Object((1,3,6,1,2,1,158,1,6,1,3),_Dot3OamEventLogOui_Type())
dot3OamEventLogOui.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3OamEventLogOui.setStatus(_B)
_Dot3OamEventLogType_Type=Unsigned32
_Dot3OamEventLogType_Object=MibTableColumn
dot3OamEventLogType=_Dot3OamEventLogType_Object((1,3,6,1,2,1,158,1,6,1,4),_Dot3OamEventLogType_Type())
dot3OamEventLogType.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3OamEventLogType.setStatus(_B)
class _Dot3OamEventLogLocation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('local',1),('remote',2)))
_Dot3OamEventLogLocation_Type.__name__=_F
_Dot3OamEventLogLocation_Object=MibTableColumn
dot3OamEventLogLocation=_Dot3OamEventLogLocation_Object((1,3,6,1,2,1,158,1,6,1,5),_Dot3OamEventLogLocation_Type())
dot3OamEventLogLocation.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3OamEventLogLocation.setStatus(_B)
_Dot3OamEventLogWindowHi_Type=Unsigned32
_Dot3OamEventLogWindowHi_Object=MibTableColumn
dot3OamEventLogWindowHi=_Dot3OamEventLogWindowHi_Object((1,3,6,1,2,1,158,1,6,1,6),_Dot3OamEventLogWindowHi_Type())
dot3OamEventLogWindowHi.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3OamEventLogWindowHi.setStatus(_B)
_Dot3OamEventLogWindowLo_Type=Unsigned32
_Dot3OamEventLogWindowLo_Object=MibTableColumn
dot3OamEventLogWindowLo=_Dot3OamEventLogWindowLo_Object((1,3,6,1,2,1,158,1,6,1,7),_Dot3OamEventLogWindowLo_Type())
dot3OamEventLogWindowLo.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3OamEventLogWindowLo.setStatus(_B)
_Dot3OamEventLogThresholdHi_Type=Unsigned32
_Dot3OamEventLogThresholdHi_Object=MibTableColumn
dot3OamEventLogThresholdHi=_Dot3OamEventLogThresholdHi_Object((1,3,6,1,2,1,158,1,6,1,8),_Dot3OamEventLogThresholdHi_Type())
dot3OamEventLogThresholdHi.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3OamEventLogThresholdHi.setStatus(_B)
_Dot3OamEventLogThresholdLo_Type=Unsigned32
_Dot3OamEventLogThresholdLo_Object=MibTableColumn
dot3OamEventLogThresholdLo=_Dot3OamEventLogThresholdLo_Object((1,3,6,1,2,1,158,1,6,1,9),_Dot3OamEventLogThresholdLo_Type())
dot3OamEventLogThresholdLo.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3OamEventLogThresholdLo.setStatus(_B)
_Dot3OamEventLogValue_Type=CounterBasedGauge64
_Dot3OamEventLogValue_Object=MibTableColumn
dot3OamEventLogValue=_Dot3OamEventLogValue_Object((1,3,6,1,2,1,158,1,6,1,10),_Dot3OamEventLogValue_Type())
dot3OamEventLogValue.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3OamEventLogValue.setStatus(_B)
_Dot3OamEventLogRunningTotal_Type=CounterBasedGauge64
_Dot3OamEventLogRunningTotal_Object=MibTableColumn
dot3OamEventLogRunningTotal=_Dot3OamEventLogRunningTotal_Object((1,3,6,1,2,1,158,1,6,1,11),_Dot3OamEventLogRunningTotal_Type())
dot3OamEventLogRunningTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3OamEventLogRunningTotal.setStatus(_B)
_Dot3OamEventLogEventTotal_Type=Unsigned32
_Dot3OamEventLogEventTotal_Object=MibTableColumn
dot3OamEventLogEventTotal=_Dot3OamEventLogEventTotal_Object((1,3,6,1,2,1,158,1,6,1,12),_Dot3OamEventLogEventTotal_Type())
dot3OamEventLogEventTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3OamEventLogEventTotal.setStatus(_B)
_Dot3OamConformance_ObjectIdentity=ObjectIdentity
dot3OamConformance=_Dot3OamConformance_ObjectIdentity((1,3,6,1,2,1,158,2))
_Dot3OamGroups_ObjectIdentity=ObjectIdentity
dot3OamGroups=_Dot3OamGroups_ObjectIdentity((1,3,6,1,2,1,158,2,1))
_Dot3OamCompliances_ObjectIdentity=ObjectIdentity
dot3OamCompliances=_Dot3OamCompliances_ObjectIdentity((1,3,6,1,2,1,158,2,2))
dot3OamControlGroup=ObjectGroup((1,3,6,1,2,1,158,2,1,1))
dot3OamControlGroup.setObjects(*((_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o)))
if mibBuilder.loadTexts:dot3OamControlGroup.setStatus(_B)
dot3OamPeerGroup=ObjectGroup((1,3,6,1,2,1,158,2,1,2))
dot3OamPeerGroup.setObjects(*((_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v)))
if mibBuilder.loadTexts:dot3OamPeerGroup.setStatus(_B)
dot3OamStatsBaseGroup=ObjectGroup((1,3,6,1,2,1,158,2,1,3))
dot3OamStatsBaseGroup.setObjects(*((_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA),(_A,_AB),(_A,_AC)))
if mibBuilder.loadTexts:dot3OamStatsBaseGroup.setStatus(_B)
dot3OamLoopbackGroup=ObjectGroup((1,3,6,1,2,1,158,2,1,4))
dot3OamLoopbackGroup.setObjects(*((_A,_AD),(_A,_AE)))
if mibBuilder.loadTexts:dot3OamLoopbackGroup.setStatus(_B)
dot3OamErrSymbolPeriodEventGroup=ObjectGroup((1,3,6,1,2,1,158,2,1,5))
dot3OamErrSymbolPeriodEventGroup.setObjects(*((_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ)))
if mibBuilder.loadTexts:dot3OamErrSymbolPeriodEventGroup.setStatus(_B)
dot3OamErrFramePeriodEventGroup=ObjectGroup((1,3,6,1,2,1,158,2,1,6))
dot3OamErrFramePeriodEventGroup.setObjects(*((_A,_AK),(_A,_AL),(_A,_AM)))
if mibBuilder.loadTexts:dot3OamErrFramePeriodEventGroup.setStatus(_B)
dot3OamErrFrameEventGroup=ObjectGroup((1,3,6,1,2,1,158,2,1,7))
dot3OamErrFrameEventGroup.setObjects(*((_A,_AN),(_A,_AO),(_A,_AP)))
if mibBuilder.loadTexts:dot3OamErrFrameEventGroup.setStatus(_B)
dot3OamErrFrameSecsSummaryEventGroup=ObjectGroup((1,3,6,1,2,1,158,2,1,8))
dot3OamErrFrameSecsSummaryEventGroup.setObjects(*((_A,_AQ),(_A,_AR),(_A,_AS)))
if mibBuilder.loadTexts:dot3OamErrFrameSecsSummaryEventGroup.setStatus(_B)
dot3OamFlagEventGroup=ObjectGroup((1,3,6,1,2,1,158,2,1,9))
dot3OamFlagEventGroup.setObjects(*((_A,_AT),(_A,_AU)))
if mibBuilder.loadTexts:dot3OamFlagEventGroup.setStatus(_B)
dot3OamEventLogGroup=ObjectGroup((1,3,6,1,2,1,158,2,1,10))
dot3OamEventLogGroup.setObjects(*((_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_O)))
if mibBuilder.loadTexts:dot3OamEventLogGroup.setStatus(_B)
dot3OamThresholdEvent=NotificationType((1,3,6,1,2,1,158,0,1))
dot3OamThresholdEvent.setObjects(*((_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_O)))
if mibBuilder.loadTexts:dot3OamThresholdEvent.setStatus(_B)
dot3OamNonThresholdEvent=NotificationType((1,3,6,1,2,1,158,0,2))
dot3OamNonThresholdEvent.setObjects(*((_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:dot3OamNonThresholdEvent.setStatus(_B)
dot3OamNotificationGroup=NotificationGroup((1,3,6,1,2,1,158,2,1,11))
dot3OamNotificationGroup.setObjects(*((_A,_AV),(_A,_AW)))
if mibBuilder.loadTexts:dot3OamNotificationGroup.setStatus(_B)
dot3OamCompliance=ModuleCompliance((1,3,6,1,2,1,158,2,2,1))
dot3OamCompliance.setObjects(*((_A,_AX),(_A,_AY),(_A,_AZ),(_A,_Aa),(_A,_Ab),(_A,_Ac),(_A,_Ad),(_A,_Ae),(_A,_Af),(_A,_Ag),(_A,_Ah)))
if mibBuilder.loadTexts:dot3OamCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'EightOTwoOui':EightOTwoOui,'dot3OamMIB':dot3OamMIB,'dot3OamNotifications':dot3OamNotifications,_AV:dot3OamThresholdEvent,_AW:dot3OamNonThresholdEvent,'dot3OamObjects':dot3OamObjects,'dot3OamTable':dot3OamTable,'dot3OamEntry':dot3OamEntry,_j:dot3OamAdminState,_k:dot3OamOperStatus,_l:dot3OamMode,_m:dot3OamMaxOamPduSize,_n:dot3OamConfigRevision,_o:dot3OamFunctionsSupported,'dot3OamPeerTable':dot3OamPeerTable,'dot3OamPeerEntry':dot3OamPeerEntry,_p:dot3OamPeerMacAddress,_q:dot3OamPeerVendorOui,_r:dot3OamPeerVendorInfo,_s:dot3OamPeerMode,_u:dot3OamPeerMaxOamPduSize,_v:dot3OamPeerConfigRevision,_t:dot3OamPeerFunctionsSupported,'dot3OamLoopbackTable':dot3OamLoopbackTable,'dot3OamLoopbackEntry':dot3OamLoopbackEntry,_AD:dot3OamLoopbackStatus,_AE:dot3OamLoopbackIgnoreRx,'dot3OamStatsTable':dot3OamStatsTable,'dot3OamStatsEntry':dot3OamStatsEntry,_w:dot3OamInformationTx,_x:dot3OamInformationRx,_y:dot3OamUniqueEventNotificationTx,_z:dot3OamUniqueEventNotificationRx,_A0:dot3OamDuplicateEventNotificationTx,_A1:dot3OamDuplicateEventNotificationRx,_A2:dot3OamLoopbackControlTx,_A3:dot3OamLoopbackControlRx,_A4:dot3OamVariableRequestTx,_A5:dot3OamVariableRequestRx,_A6:dot3OamVariableResponseTx,_A7:dot3OamVariableResponseRx,_A8:dot3OamOrgSpecificTx,_A9:dot3OamOrgSpecificRx,_AA:dot3OamUnsupportedCodesTx,_AB:dot3OamUnsupportedCodesRx,_AC:dot3OamFramesLostDueToOam,'dot3OamEventConfigTable':dot3OamEventConfigTable,'dot3OamEventConfigEntry':dot3OamEventConfigEntry,_AF:dot3OamErrSymPeriodWindowHi,_AG:dot3OamErrSymPeriodWindowLo,_AH:dot3OamErrSymPeriodThresholdHi,_AI:dot3OamErrSymPeriodThresholdLo,_AJ:dot3OamErrSymPeriodEvNotifEnable,_AK:dot3OamErrFramePeriodWindow,_AL:dot3OamErrFramePeriodThreshold,_AM:dot3OamErrFramePeriodEvNotifEnable,_AN:dot3OamErrFrameWindow,_AO:dot3OamErrFrameThreshold,_AP:dot3OamErrFrameEvNotifEnable,_AQ:dot3OamErrFrameSecsSummaryWindow,_AR:dot3OamErrFrameSecsSummaryThreshold,_AS:dot3OamErrFrameSecsEvNotifEnable,_AT:dot3OamDyingGaspEnable,_AU:dot3OamCriticalEventEnable,'dot3OamEventLogTable':dot3OamEventLogTable,'dot3OamEventLogEntry':dot3OamEventLogEntry,_i:dot3OamEventLogIndex,_K:dot3OamEventLogTimestamp,_L:dot3OamEventLogOui,_M:dot3OamEventLogType,_N:dot3OamEventLogLocation,_Q:dot3OamEventLogWindowHi,_R:dot3OamEventLogWindowLo,_S:dot3OamEventLogThresholdHi,_T:dot3OamEventLogThresholdLo,_U:dot3OamEventLogValue,_V:dot3OamEventLogRunningTotal,_O:dot3OamEventLogEventTotal,'dot3OamConformance':dot3OamConformance,'dot3OamGroups':dot3OamGroups,_AX:dot3OamControlGroup,_AY:dot3OamPeerGroup,_AZ:dot3OamStatsBaseGroup,_Aa:dot3OamLoopbackGroup,_Ab:dot3OamErrSymbolPeriodEventGroup,_Ac:dot3OamErrFramePeriodEventGroup,_Ad:dot3OamErrFrameEventGroup,_Ae:dot3OamErrFrameSecsSummaryEventGroup,_Af:dot3OamFlagEventGroup,_Ag:dot3OamEventLogGroup,_Ah:dot3OamNotificationGroup,'dot3OamCompliances':dot3OamCompliances,'dot3OamCompliance':dot3OamCompliance})