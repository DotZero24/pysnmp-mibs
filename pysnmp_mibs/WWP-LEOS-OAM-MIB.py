_i='wwpLeosOamEventLogLocation'
_h='wwpLeosOamEventLogType'
_g='wwpLeosOamEventLogIndex'
_f='tenths of a second'
_e='wwpLeosOamEventPort'
_d='wwpLeosOamStatsPort'
_c='noLoopback'
_b='wwpLeosOamLoopbackPort'
_a='unknown'
_Z='wwpLeosOamLocalPort'
_Y='variableSupport'
_X='eventSupport'
_W='loopbackSupport'
_V='unidirectionalSupport'
_U='passive'
_T='wwpLeosOamPeerMacAddress'
_S='wwpLeosOamPeerStatus'
_R='wwpLeosOamOperStatus'
_Q='wwpLeosOamEventLogPort'
_P='active'
_O='wwpLeosEtherPortOperStatus'
_N='wwpLeosEtherPortDesc'
_M='Bits'
_L='wwpLeosOamPort'
_K='OctetString'
_J='WWP-LEOS-PORT-MIB'
_I='Unsigned32'
_H='enabled'
_G='disabled'
_F='WWP-LEOS-OAM-MIB'
_E='frames'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_K,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_M,'Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_I,'iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeStamp','TruthValue')
wwpLeosEtherPortDesc,wwpLeosEtherPortOperStatus=mibBuilder.importSymbols(_J,_N,_O)
wwpModulesLeos,=mibBuilder.importSymbols('WWP-SMI','wwpModulesLeos')
wwpLeosOamMibModule=ModuleIdentity((1,3,6,1,4,1,6141,2,60,400))
if mibBuilder.loadTexts:wwpLeosOamMibModule.setRevisions(('2008-01-03 00:00',))
_WwpLeosOamMIB_ObjectIdentity=ObjectIdentity
wwpLeosOamMIB=_WwpLeosOamMIB_ObjectIdentity((1,3,6,1,4,1,6141,2,60,400,1))
_WwpLeosOamConf_ObjectIdentity=ObjectIdentity
wwpLeosOamConf=_WwpLeosOamConf_ObjectIdentity((1,3,6,1,4,1,6141,2,60,400,1,1))
_WwpLeosOamGroups_ObjectIdentity=ObjectIdentity
wwpLeosOamGroups=_WwpLeosOamGroups_ObjectIdentity((1,3,6,1,4,1,6141,2,60,400,1,1,1))
_WwpLeosOamCompls_ObjectIdentity=ObjectIdentity
wwpLeosOamCompls=_WwpLeosOamCompls_ObjectIdentity((1,3,6,1,4,1,6141,2,60,400,1,1,2))
_WwpLeosOamObjs_ObjectIdentity=ObjectIdentity
wwpLeosOamObjs=_WwpLeosOamObjs_ObjectIdentity((1,3,6,1,4,1,6141,2,60,400,1,2))
_WwpLeosOamTable_Object=MibTable
wwpLeosOamTable=_WwpLeosOamTable_Object((1,3,6,1,4,1,6141,2,60,400,1,2,1))
if mibBuilder.loadTexts:wwpLeosOamTable.setStatus(_A)
_WwpLeosOamEntry_Object=MibTableRow
wwpLeosOamEntry=_WwpLeosOamEntry_Object((1,3,6,1,4,1,6141,2,60,400,1,2,1,1))
wwpLeosOamEntry.setIndexNames((0,_F,_L))
if mibBuilder.loadTexts:wwpLeosOamEntry.setStatus(_A)
class _WwpLeosOamAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_WwpLeosOamAdminState_Type.__name__=_C
_WwpLeosOamAdminState_Object=MibTableColumn
wwpLeosOamAdminState=_WwpLeosOamAdminState_Object((1,3,6,1,4,1,6141,2,60,400,1,2,1,1,1),_WwpLeosOamAdminState_Type())
wwpLeosOamAdminState.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosOamAdminState.setStatus(_A)
class _WwpLeosOamOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_G,1),('linkfault',2),('passiveWait',3),('activeSendLocal',4),('sendLocalAndRemote',5),('sendLocalAndRemoteOk',6),('oamPeeringLocallyRejected',7),('oamPeeringRemotelyRejected',8),('operational',9)))
_WwpLeosOamOperStatus_Type.__name__=_C
_WwpLeosOamOperStatus_Object=MibTableColumn
wwpLeosOamOperStatus=_WwpLeosOamOperStatus_Object((1,3,6,1,4,1,6141,2,60,400,1,2,1,1,2),_WwpLeosOamOperStatus_Type())
wwpLeosOamOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosOamOperStatus.setStatus(_A)
class _WwpLeosOamMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_U,2)))
_WwpLeosOamMode_Type.__name__=_C
_WwpLeosOamMode_Object=MibTableColumn
wwpLeosOamMode=_WwpLeosOamMode_Object((1,3,6,1,4,1,6141,2,60,400,1,2,1,1,3),_WwpLeosOamMode_Type())
wwpLeosOamMode.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosOamMode.setStatus(_A)
_WwpLeosMaxOamPduSize_Type=Integer32
_WwpLeosMaxOamPduSize_Object=MibTableColumn
wwpLeosMaxOamPduSize=_WwpLeosMaxOamPduSize_Object((1,3,6,1,4,1,6141,2,60,400,1,2,1,1,4),_WwpLeosMaxOamPduSize_Type())
wwpLeosMaxOamPduSize.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosMaxOamPduSize.setStatus(_A)
if mibBuilder.loadTexts:wwpLeosMaxOamPduSize.setUnits('bytes')
_WwpLeosOamConfigRevision_Type=Unsigned32
_WwpLeosOamConfigRevision_Object=MibTableColumn
wwpLeosOamConfigRevision=_WwpLeosOamConfigRevision_Object((1,3,6,1,4,1,6141,2,60,400,1,2,1,1,5),_WwpLeosOamConfigRevision_Type())
wwpLeosOamConfigRevision.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosOamConfigRevision.setStatus(_A)
class _WwpLeosOamFunctionsSupported_Type(Bits):namedValues=NamedValues(*((_V,0),(_W,1),(_X,2),(_Y,3)))
_WwpLeosOamFunctionsSupported_Type.__name__=_M
_WwpLeosOamFunctionsSupported_Object=MibTableColumn
wwpLeosOamFunctionsSupported=_WwpLeosOamFunctionsSupported_Object((1,3,6,1,4,1,6141,2,60,400,1,2,1,1,6),_WwpLeosOamFunctionsSupported_Type())
wwpLeosOamFunctionsSupported.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosOamFunctionsSupported.setStatus(_A)
class _WwpLeosOamPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_WwpLeosOamPort_Type.__name__=_C
_WwpLeosOamPort_Object=MibTableColumn
wwpLeosOamPort=_WwpLeosOamPort_Object((1,3,6,1,4,1,6141,2,60,400,1,2,1,1,7),_WwpLeosOamPort_Type())
wwpLeosOamPort.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosOamPort.setStatus(_A)
class _WwpLeosOamPduTimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,1000))
_WwpLeosOamPduTimer_Type.__name__=_C
_WwpLeosOamPduTimer_Object=MibTableColumn
wwpLeosOamPduTimer=_WwpLeosOamPduTimer_Object((1,3,6,1,4,1,6141,2,60,400,1,2,1,1,8),_WwpLeosOamPduTimer_Type())
wwpLeosOamPduTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosOamPduTimer.setStatus(_A)
class _WwpLeosOamLinkLostTimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(500,5000))
_WwpLeosOamLinkLostTimer_Type.__name__=_C
_WwpLeosOamLinkLostTimer_Object=MibTableColumn
wwpLeosOamLinkLostTimer=_WwpLeosOamLinkLostTimer_Object((1,3,6,1,4,1,6141,2,60,400,1,2,1,1,9),_WwpLeosOamLinkLostTimer_Type())
wwpLeosOamLinkLostTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosOamLinkLostTimer.setStatus(_A)
class _WwpLeosOamPeerStatusNotifyState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),('off',2)))
_WwpLeosOamPeerStatusNotifyState_Type.__name__=_C
_WwpLeosOamPeerStatusNotifyState_Object=MibTableColumn
wwpLeosOamPeerStatusNotifyState=_WwpLeosOamPeerStatusNotifyState_Object((1,3,6,1,4,1,6141,2,60,400,1,2,1,1,10),_WwpLeosOamPeerStatusNotifyState_Type())
wwpLeosOamPeerStatusNotifyState.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosOamPeerStatusNotifyState.setStatus(_A)
_WwpLeosOamPeerTable_Object=MibTable
wwpLeosOamPeerTable=_WwpLeosOamPeerTable_Object((1,3,6,1,4,1,6141,2,60,400,1,2,2))
if mibBuilder.loadTexts:wwpLeosOamPeerTable.setStatus(_A)
_WwpLeosOamPeerEntry_Object=MibTableRow
wwpLeosOamPeerEntry=_WwpLeosOamPeerEntry_Object((1,3,6,1,4,1,6141,2,60,400,1,2,2,1))
wwpLeosOamPeerEntry.setIndexNames((0,_F,_Z))
if mibBuilder.loadTexts:wwpLeosOamPeerEntry.setStatus(_A)
class _WwpLeosOamPeerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),('inactive',2)))
_WwpLeosOamPeerStatus_Type.__name__=_C
_WwpLeosOamPeerStatus_Object=MibTableColumn
wwpLeosOamPeerStatus=_WwpLeosOamPeerStatus_Object((1,3,6,1,4,1,6141,2,60,400,1,2,2,1,1),_WwpLeosOamPeerStatus_Type())
wwpLeosOamPeerStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosOamPeerStatus.setStatus(_A)
class _WwpLeosOamPeerMacAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_WwpLeosOamPeerMacAddress_Type.__name__=_K
_WwpLeosOamPeerMacAddress_Object=MibTableColumn
wwpLeosOamPeerMacAddress=_WwpLeosOamPeerMacAddress_Object((1,3,6,1,4,1,6141,2,60,400,1,2,2,1,2),_WwpLeosOamPeerMacAddress_Type())
wwpLeosOamPeerMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosOamPeerMacAddress.setStatus(_A)
class _WwpLeosOamPeerVendorOui_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,3));fixedLength=3
_WwpLeosOamPeerVendorOui_Type.__name__=_K
_WwpLeosOamPeerVendorOui_Object=MibTableColumn
wwpLeosOamPeerVendorOui=_WwpLeosOamPeerVendorOui_Object((1,3,6,1,4,1,6141,2,60,400,1,2,2,1,3),_WwpLeosOamPeerVendorOui_Type())
wwpLeosOamPeerVendorOui.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosOamPeerVendorOui.setStatus(_A)
_WwpLeosOamPeerVendorInfo_Type=Unsigned32
_WwpLeosOamPeerVendorInfo_Object=MibTableColumn
wwpLeosOamPeerVendorInfo=_WwpLeosOamPeerVendorInfo_Object((1,3,6,1,4,1,6141,2,60,400,1,2,2,1,4),_WwpLeosOamPeerVendorInfo_Type())
wwpLeosOamPeerVendorInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosOamPeerVendorInfo.setStatus(_A)
class _WwpLeosOamPeerMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_P,1),(_U,2),(_a,3)))
_WwpLeosOamPeerMode_Type.__name__=_C
_WwpLeosOamPeerMode_Object=MibTableColumn
wwpLeosOamPeerMode=_WwpLeosOamPeerMode_Object((1,3,6,1,4,1,6141,2,60,400,1,2,2,1,5),_WwpLeosOamPeerMode_Type())
wwpLeosOamPeerMode.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosOamPeerMode.setStatus(_A)
_WwpLeosOamPeerMaxOamPduSize_Type=Integer32
_WwpLeosOamPeerMaxOamPduSize_Object=MibTableColumn
wwpLeosOamPeerMaxOamPduSize=_WwpLeosOamPeerMaxOamPduSize_Object((1,3,6,1,4,1,6141,2,60,400,1,2,2,1,6),_WwpLeosOamPeerMaxOamPduSize_Type())
wwpLeosOamPeerMaxOamPduSize.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosOamPeerMaxOamPduSize.setStatus(_A)
if mibBuilder.loadTexts:wwpLeosOamPeerMaxOamPduSize.setUnits('bytes')
_WwpLeosOamPeerConfigRevision_Type=Unsigned32
_WwpLeosOamPeerConfigRevision_Object=MibTableColumn
wwpLeosOamPeerConfigRevision=_WwpLeosOamPeerConfigRevision_Object((1,3,6,1,4,1,6141,2,60,400,1,2,2,1,7),_WwpLeosOamPeerConfigRevision_Type())
wwpLeosOamPeerConfigRevision.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosOamPeerConfigRevision.setStatus(_A)
class _WwpLeosOamPeerFunctionsSupported_Type(Bits):namedValues=NamedValues(*((_V,0),(_W,1),(_X,2),(_Y,3)))
_WwpLeosOamPeerFunctionsSupported_Type.__name__=_M
_WwpLeosOamPeerFunctionsSupported_Object=MibTableColumn
wwpLeosOamPeerFunctionsSupported=_WwpLeosOamPeerFunctionsSupported_Object((1,3,6,1,4,1,6141,2,60,400,1,2,2,1,8),_WwpLeosOamPeerFunctionsSupported_Type())
wwpLeosOamPeerFunctionsSupported.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosOamPeerFunctionsSupported.setStatus(_A)
class _WwpLeosOamLocalPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_WwpLeosOamLocalPort_Type.__name__=_C
_WwpLeosOamLocalPort_Object=MibTableColumn
wwpLeosOamLocalPort=_WwpLeosOamLocalPort_Object((1,3,6,1,4,1,6141,2,60,400,1,2,2,1,9),_WwpLeosOamLocalPort_Type())
wwpLeosOamLocalPort.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosOamLocalPort.setStatus(_A)
_WwpLeosOamLoopbackTable_Object=MibTable
wwpLeosOamLoopbackTable=_WwpLeosOamLoopbackTable_Object((1,3,6,1,4,1,6141,2,60,400,1,2,3))
if mibBuilder.loadTexts:wwpLeosOamLoopbackTable.setStatus(_A)
_WwpLeosOamLoopbackEntry_Object=MibTableRow
wwpLeosOamLoopbackEntry=_WwpLeosOamLoopbackEntry_Object((1,3,6,1,4,1,6141,2,60,400,1,2,3,1))
wwpLeosOamLoopbackEntry.setIndexNames((0,_F,_b))
if mibBuilder.loadTexts:wwpLeosOamLoopbackEntry.setStatus(_A)
class _WwpLeosOamLoopbackCommand_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_c,1),('startRemoteLoopback',2),('stopRemoteLoopback',3)))
_WwpLeosOamLoopbackCommand_Type.__name__=_C
_WwpLeosOamLoopbackCommand_Object=MibTableColumn
wwpLeosOamLoopbackCommand=_WwpLeosOamLoopbackCommand_Object((1,3,6,1,4,1,6141,2,60,400,1,2,3,1,1),_WwpLeosOamLoopbackCommand_Type())
wwpLeosOamLoopbackCommand.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosOamLoopbackCommand.setStatus(_A)
class _WwpLeosOamLoopbackStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_c,1),('initiatingLoopback',2),('remoteLoopback',3),('terminatingLoopback',4),('localLoopback',5),(_a,6)))
_WwpLeosOamLoopbackStatus_Type.__name__=_C
_WwpLeosOamLoopbackStatus_Object=MibTableColumn
wwpLeosOamLoopbackStatus=_WwpLeosOamLoopbackStatus_Object((1,3,6,1,4,1,6141,2,60,400,1,2,3,1,2),_WwpLeosOamLoopbackStatus_Type())
wwpLeosOamLoopbackStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosOamLoopbackStatus.setStatus(_A)
class _WwpLeosOamLoopbackIgnoreRx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ignore',1),('process',2)))
_WwpLeosOamLoopbackIgnoreRx_Type.__name__=_C
_WwpLeosOamLoopbackIgnoreRx_Object=MibTableColumn
wwpLeosOamLoopbackIgnoreRx=_WwpLeosOamLoopbackIgnoreRx_Object((1,3,6,1,4,1,6141,2,60,400,1,2,3,1,3),_WwpLeosOamLoopbackIgnoreRx_Type())
wwpLeosOamLoopbackIgnoreRx.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosOamLoopbackIgnoreRx.setStatus(_A)
class _WwpLeosOamLoopbackPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_WwpLeosOamLoopbackPort_Type.__name__=_C
_WwpLeosOamLoopbackPort_Object=MibTableColumn
wwpLeosOamLoopbackPort=_WwpLeosOamLoopbackPort_Object((1,3,6,1,4,1,6141,2,60,400,1,2,3,1,4),_WwpLeosOamLoopbackPort_Type())
wwpLeosOamLoopbackPort.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosOamLoopbackPort.setStatus(_A)
_WwpLeosOamStatsTable_Object=MibTable
wwpLeosOamStatsTable=_WwpLeosOamStatsTable_Object((1,3,6,1,4,1,6141,2,60,400,1,2,4))
if mibBuilder.loadTexts:wwpLeosOamStatsTable.setStatus(_A)
_WwpLeosOamStatsEntry_Object=MibTableRow
wwpLeosOamStatsEntry=_WwpLeosOamStatsEntry_Object((1,3,6,1,4,1,6141,2,60,400,1,2,4,1))
wwpLeosOamStatsEntry.setIndexNames((0,_F,_d))
if mibBuilder.loadTexts:wwpLeosOamStatsEntry.setStatus(_A)
_WwpLeosOamInformationTx_Type=Counter32
_WwpLeosOamInformationTx_Object=MibTableColumn
wwpLeosOamInformationTx=_WwpLeosOamInformationTx_Object((1,3,6,1,4,1,6141,2,60,400,1,2,4,1,1),_WwpLeosOamInformationTx_Type())
wwpLeosOamInformationTx.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosOamInformationTx.setStatus(_A)
if mibBuilder.loadTexts:wwpLeosOamInformationTx.setUnits(_E)
_WwpLeosOamInformationRx_Type=Counter32
_WwpLeosOamInformationRx_Object=MibTableColumn
wwpLeosOamInformationRx=_WwpLeosOamInformationRx_Object((1,3,6,1,4,1,6141,2,60,400,1,2,4,1,2),_WwpLeosOamInformationRx_Type())
wwpLeosOamInformationRx.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosOamInformationRx.setStatus(_A)
if mibBuilder.loadTexts:wwpLeosOamInformationRx.setUnits(_E)
_WwpLeosOamUniqueEventNotificationTx_Type=Counter32
_WwpLeosOamUniqueEventNotificationTx_Object=MibTableColumn
wwpLeosOamUniqueEventNotificationTx=_WwpLeosOamUniqueEventNotificationTx_Object((1,3,6,1,4,1,6141,2,60,400,1,2,4,1,3),_WwpLeosOamUniqueEventNotificationTx_Type())
wwpLeosOamUniqueEventNotificationTx.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosOamUniqueEventNotificationTx.setStatus(_A)
if mibBuilder.loadTexts:wwpLeosOamUniqueEventNotificationTx.setUnits(_E)
_WwpLeosOamUniqueEventNotificationRx_Type=Counter32
_WwpLeosOamUniqueEventNotificationRx_Object=MibTableColumn
wwpLeosOamUniqueEventNotificationRx=_WwpLeosOamUniqueEventNotificationRx_Object((1,3,6,1,4,1,6141,2,60,400,1,2,4,1,4),_WwpLeosOamUniqueEventNotificationRx_Type())
wwpLeosOamUniqueEventNotificationRx.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosOamUniqueEventNotificationRx.setStatus(_A)
if mibBuilder.loadTexts:wwpLeosOamUniqueEventNotificationRx.setUnits(_E)
_WwpLeosOamLoopbackControlTx_Type=Counter32
_WwpLeosOamLoopbackControlTx_Object=MibTableColumn
wwpLeosOamLoopbackControlTx=_WwpLeosOamLoopbackControlTx_Object((1,3,6,1,4,1,6141,2,60,400,1,2,4,1,5),_WwpLeosOamLoopbackControlTx_Type())
wwpLeosOamLoopbackControlTx.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosOamLoopbackControlTx.setStatus(_A)
if mibBuilder.loadTexts:wwpLeosOamLoopbackControlTx.setUnits(_E)
_WwpLeosOamLoopbackControlRx_Type=Counter32
_WwpLeosOamLoopbackControlRx_Object=MibTableColumn
wwpLeosOamLoopbackControlRx=_WwpLeosOamLoopbackControlRx_Object((1,3,6,1,4,1,6141,2,60,400,1,2,4,1,6),_WwpLeosOamLoopbackControlRx_Type())
wwpLeosOamLoopbackControlRx.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosOamLoopbackControlRx.setStatus(_A)
if mibBuilder.loadTexts:wwpLeosOamLoopbackControlRx.setUnits(_E)
_WwpLeosOamVariableRequestTx_Type=Counter32
_WwpLeosOamVariableRequestTx_Object=MibTableColumn
wwpLeosOamVariableRequestTx=_WwpLeosOamVariableRequestTx_Object((1,3,6,1,4,1,6141,2,60,400,1,2,4,1,7),_WwpLeosOamVariableRequestTx_Type())
wwpLeosOamVariableRequestTx.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosOamVariableRequestTx.setStatus(_A)
if mibBuilder.loadTexts:wwpLeosOamVariableRequestTx.setUnits(_E)
_WwpLeosOamVariableRequestRx_Type=Counter32
_WwpLeosOamVariableRequestRx_Object=MibTableColumn
wwpLeosOamVariableRequestRx=_WwpLeosOamVariableRequestRx_Object((1,3,6,1,4,1,6141,2,60,400,1,2,4,1,8),_WwpLeosOamVariableRequestRx_Type())
wwpLeosOamVariableRequestRx.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosOamVariableRequestRx.setStatus(_A)
if mibBuilder.loadTexts:wwpLeosOamVariableRequestRx.setUnits(_E)
_WwpLeosOamVariableResponseTx_Type=Counter32
_WwpLeosOamVariableResponseTx_Object=MibTableColumn
wwpLeosOamVariableResponseTx=_WwpLeosOamVariableResponseTx_Object((1,3,6,1,4,1,6141,2,60,400,1,2,4,1,9),_WwpLeosOamVariableResponseTx_Type())
wwpLeosOamVariableResponseTx.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosOamVariableResponseTx.setStatus(_A)
if mibBuilder.loadTexts:wwpLeosOamVariableResponseTx.setUnits(_E)
_WwpLeosOamVariableResponseRx_Type=Counter32
_WwpLeosOamVariableResponseRx_Object=MibTableColumn
wwpLeosOamVariableResponseRx=_WwpLeosOamVariableResponseRx_Object((1,3,6,1,4,1,6141,2,60,400,1,2,4,1,10),_WwpLeosOamVariableResponseRx_Type())
wwpLeosOamVariableResponseRx.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosOamVariableResponseRx.setStatus(_A)
if mibBuilder.loadTexts:wwpLeosOamVariableResponseRx.setUnits(_E)
_WwpLeosOamOrgSpecificTx_Type=Counter32
_WwpLeosOamOrgSpecificTx_Object=MibTableColumn
wwpLeosOamOrgSpecificTx=_WwpLeosOamOrgSpecificTx_Object((1,3,6,1,4,1,6141,2,60,400,1,2,4,1,11),_WwpLeosOamOrgSpecificTx_Type())
wwpLeosOamOrgSpecificTx.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosOamOrgSpecificTx.setStatus(_A)
if mibBuilder.loadTexts:wwpLeosOamOrgSpecificTx.setUnits(_E)
_WwpLeosOamOrgSpecificRx_Type=Counter32
_WwpLeosOamOrgSpecificRx_Object=MibTableColumn
wwpLeosOamOrgSpecificRx=_WwpLeosOamOrgSpecificRx_Object((1,3,6,1,4,1,6141,2,60,400,1,2,4,1,12),_WwpLeosOamOrgSpecificRx_Type())
wwpLeosOamOrgSpecificRx.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosOamOrgSpecificRx.setStatus(_A)
if mibBuilder.loadTexts:wwpLeosOamOrgSpecificRx.setUnits(_E)
_WwpLeosOamUnsupportedCodesTx_Type=Counter32
_WwpLeosOamUnsupportedCodesTx_Object=MibTableColumn
wwpLeosOamUnsupportedCodesTx=_WwpLeosOamUnsupportedCodesTx_Object((1,3,6,1,4,1,6141,2,60,400,1,2,4,1,13),_WwpLeosOamUnsupportedCodesTx_Type())
wwpLeosOamUnsupportedCodesTx.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosOamUnsupportedCodesTx.setStatus(_A)
if mibBuilder.loadTexts:wwpLeosOamUnsupportedCodesTx.setUnits(_E)
_WwpLeosOamUnsupportedCodesRx_Type=Counter32
_WwpLeosOamUnsupportedCodesRx_Object=MibTableColumn
wwpLeosOamUnsupportedCodesRx=_WwpLeosOamUnsupportedCodesRx_Object((1,3,6,1,4,1,6141,2,60,400,1,2,4,1,14),_WwpLeosOamUnsupportedCodesRx_Type())
wwpLeosOamUnsupportedCodesRx.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosOamUnsupportedCodesRx.setStatus(_A)
if mibBuilder.loadTexts:wwpLeosOamUnsupportedCodesRx.setUnits(_E)
_WwpLeosOamframesLostDueToOam_Type=Counter32
_WwpLeosOamframesLostDueToOam_Object=MibTableColumn
wwpLeosOamframesLostDueToOam=_WwpLeosOamframesLostDueToOam_Object((1,3,6,1,4,1,6141,2,60,400,1,2,4,1,15),_WwpLeosOamframesLostDueToOam_Type())
wwpLeosOamframesLostDueToOam.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosOamframesLostDueToOam.setStatus(_A)
if mibBuilder.loadTexts:wwpLeosOamframesLostDueToOam.setUnits(_E)
class _WwpLeosOamStatsPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_WwpLeosOamStatsPort_Type.__name__=_C
_WwpLeosOamStatsPort_Object=MibTableColumn
wwpLeosOamStatsPort=_WwpLeosOamStatsPort_Object((1,3,6,1,4,1,6141,2,60,400,1,2,4,1,16),_WwpLeosOamStatsPort_Type())
wwpLeosOamStatsPort.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosOamStatsPort.setStatus(_A)
_WwpLeosOamDuplicateEventNotificationTx_Type=Counter32
_WwpLeosOamDuplicateEventNotificationTx_Object=MibTableColumn
wwpLeosOamDuplicateEventNotificationTx=_WwpLeosOamDuplicateEventNotificationTx_Object((1,3,6,1,4,1,6141,2,60,400,1,2,4,1,17),_WwpLeosOamDuplicateEventNotificationTx_Type())
wwpLeosOamDuplicateEventNotificationTx.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosOamDuplicateEventNotificationTx.setStatus(_A)
if mibBuilder.loadTexts:wwpLeosOamDuplicateEventNotificationTx.setUnits(_E)
_WwpLeosOamDuplicateEventNotificationRx_Type=Counter32
_WwpLeosOamDuplicateEventNotificationRx_Object=MibTableColumn
wwpLeosOamDuplicateEventNotificationRx=_WwpLeosOamDuplicateEventNotificationRx_Object((1,3,6,1,4,1,6141,2,60,400,1,2,4,1,18),_WwpLeosOamDuplicateEventNotificationRx_Type())
wwpLeosOamDuplicateEventNotificationRx.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosOamDuplicateEventNotificationRx.setStatus(_A)
if mibBuilder.loadTexts:wwpLeosOamDuplicateEventNotificationRx.setUnits(_E)
class _WwpLeosOamSystemEnableDisable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_WwpLeosOamSystemEnableDisable_Type.__name__=_C
_WwpLeosOamSystemEnableDisable_Object=MibScalar
wwpLeosOamSystemEnableDisable=_WwpLeosOamSystemEnableDisable_Object((1,3,6,1,4,1,6141,2,60,400,1,2,5),_WwpLeosOamSystemEnableDisable_Type())
wwpLeosOamSystemEnableDisable.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosOamSystemEnableDisable.setStatus(_A)
_WwpLeosOamEventConfigTable_Object=MibTable
wwpLeosOamEventConfigTable=_WwpLeosOamEventConfigTable_Object((1,3,6,1,4,1,6141,2,60,400,1,2,6))
if mibBuilder.loadTexts:wwpLeosOamEventConfigTable.setStatus(_A)
_WwpLeosOamEventConfigEntry_Object=MibTableRow
wwpLeosOamEventConfigEntry=_WwpLeosOamEventConfigEntry_Object((1,3,6,1,4,1,6141,2,60,400,1,2,6,1))
wwpLeosOamEventConfigEntry.setIndexNames((0,_F,_e))
if mibBuilder.loadTexts:wwpLeosOamEventConfigEntry.setStatus(_A)
class _WwpLeosOamEventPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_WwpLeosOamEventPort_Type.__name__=_C
_WwpLeosOamEventPort_Object=MibTableColumn
wwpLeosOamEventPort=_WwpLeosOamEventPort_Object((1,3,6,1,4,1,6141,2,60,400,1,2,6,1,1),_WwpLeosOamEventPort_Type())
wwpLeosOamEventPort.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosOamEventPort.setStatus(_A)
class _WwpLeosOamErrFramePeriodWindow_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(14880,8928000))
_WwpLeosOamErrFramePeriodWindow_Type.__name__=_I
_WwpLeosOamErrFramePeriodWindow_Object=MibTableColumn
wwpLeosOamErrFramePeriodWindow=_WwpLeosOamErrFramePeriodWindow_Object((1,3,6,1,4,1,6141,2,60,400,1,2,6,1,2),_WwpLeosOamErrFramePeriodWindow_Type())
wwpLeosOamErrFramePeriodWindow.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosOamErrFramePeriodWindow.setStatus(_A)
if mibBuilder.loadTexts:wwpLeosOamErrFramePeriodWindow.setUnits(_E)
class _WwpLeosOamErrFramePeriodThreshold_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967293))
_WwpLeosOamErrFramePeriodThreshold_Type.__name__=_I
_WwpLeosOamErrFramePeriodThreshold_Object=MibTableColumn
wwpLeosOamErrFramePeriodThreshold=_WwpLeosOamErrFramePeriodThreshold_Object((1,3,6,1,4,1,6141,2,60,400,1,2,6,1,3),_WwpLeosOamErrFramePeriodThreshold_Type())
wwpLeosOamErrFramePeriodThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosOamErrFramePeriodThreshold.setStatus(_A)
if mibBuilder.loadTexts:wwpLeosOamErrFramePeriodThreshold.setUnits(_E)
class _WwpLeosOamErrFramePeriodEvNotifEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_WwpLeosOamErrFramePeriodEvNotifEnable_Type.__name__=_C
_WwpLeosOamErrFramePeriodEvNotifEnable_Object=MibTableColumn
wwpLeosOamErrFramePeriodEvNotifEnable=_WwpLeosOamErrFramePeriodEvNotifEnable_Object((1,3,6,1,4,1,6141,2,60,400,1,2,6,1,4),_WwpLeosOamErrFramePeriodEvNotifEnable_Type())
wwpLeosOamErrFramePeriodEvNotifEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosOamErrFramePeriodEvNotifEnable.setStatus(_A)
class _WwpLeosOamErrFrameWindow_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,600))
_WwpLeosOamErrFrameWindow_Type.__name__=_I
_WwpLeosOamErrFrameWindow_Object=MibTableColumn
wwpLeosOamErrFrameWindow=_WwpLeosOamErrFrameWindow_Object((1,3,6,1,4,1,6141,2,60,400,1,2,6,1,5),_WwpLeosOamErrFrameWindow_Type())
wwpLeosOamErrFrameWindow.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosOamErrFrameWindow.setStatus(_A)
if mibBuilder.loadTexts:wwpLeosOamErrFrameWindow.setUnits(_f)
class _WwpLeosOamErrFrameThreshold_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967293))
_WwpLeosOamErrFrameThreshold_Type.__name__=_I
_WwpLeosOamErrFrameThreshold_Object=MibTableColumn
wwpLeosOamErrFrameThreshold=_WwpLeosOamErrFrameThreshold_Object((1,3,6,1,4,1,6141,2,60,400,1,2,6,1,6),_WwpLeosOamErrFrameThreshold_Type())
wwpLeosOamErrFrameThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosOamErrFrameThreshold.setStatus(_A)
if mibBuilder.loadTexts:wwpLeosOamErrFrameThreshold.setUnits(_E)
class _WwpLeosOamErrFrameEvNotifEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_WwpLeosOamErrFrameEvNotifEnable_Type.__name__=_C
_WwpLeosOamErrFrameEvNotifEnable_Object=MibTableColumn
wwpLeosOamErrFrameEvNotifEnable=_WwpLeosOamErrFrameEvNotifEnable_Object((1,3,6,1,4,1,6141,2,60,400,1,2,6,1,7),_WwpLeosOamErrFrameEvNotifEnable_Type())
wwpLeosOamErrFrameEvNotifEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosOamErrFrameEvNotifEnable.setStatus(_A)
class _WwpLeosOamErrFrameSecsSummaryWindow_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,9000))
_WwpLeosOamErrFrameSecsSummaryWindow_Type.__name__=_C
_WwpLeosOamErrFrameSecsSummaryWindow_Object=MibTableColumn
wwpLeosOamErrFrameSecsSummaryWindow=_WwpLeosOamErrFrameSecsSummaryWindow_Object((1,3,6,1,4,1,6141,2,60,400,1,2,6,1,8),_WwpLeosOamErrFrameSecsSummaryWindow_Type())
wwpLeosOamErrFrameSecsSummaryWindow.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosOamErrFrameSecsSummaryWindow.setStatus(_A)
if mibBuilder.loadTexts:wwpLeosOamErrFrameSecsSummaryWindow.setUnits(_f)
class _WwpLeosOamErrFrameSecsSummaryThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WwpLeosOamErrFrameSecsSummaryThreshold_Type.__name__=_C
_WwpLeosOamErrFrameSecsSummaryThreshold_Object=MibTableColumn
wwpLeosOamErrFrameSecsSummaryThreshold=_WwpLeosOamErrFrameSecsSummaryThreshold_Object((1,3,6,1,4,1,6141,2,60,400,1,2,6,1,9),_WwpLeosOamErrFrameSecsSummaryThreshold_Type())
wwpLeosOamErrFrameSecsSummaryThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosOamErrFrameSecsSummaryThreshold.setStatus(_A)
if mibBuilder.loadTexts:wwpLeosOamErrFrameSecsSummaryThreshold.setUnits('errored frame seconds')
class _WwpLeosOamErrFrameSecsEvNotifEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_WwpLeosOamErrFrameSecsEvNotifEnable_Type.__name__=_C
_WwpLeosOamErrFrameSecsEvNotifEnable_Object=MibTableColumn
wwpLeosOamErrFrameSecsEvNotifEnable=_WwpLeosOamErrFrameSecsEvNotifEnable_Object((1,3,6,1,4,1,6141,2,60,400,1,2,6,1,10),_WwpLeosOamErrFrameSecsEvNotifEnable_Type())
wwpLeosOamErrFrameSecsEvNotifEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosOamErrFrameSecsEvNotifEnable.setStatus(_A)
class _WwpLeosOamDyingGaspEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_WwpLeosOamDyingGaspEnable_Type.__name__=_C
_WwpLeosOamDyingGaspEnable_Object=MibTableColumn
wwpLeosOamDyingGaspEnable=_WwpLeosOamDyingGaspEnable_Object((1,3,6,1,4,1,6141,2,60,400,1,2,6,1,11),_WwpLeosOamDyingGaspEnable_Type())
wwpLeosOamDyingGaspEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosOamDyingGaspEnable.setStatus(_A)
class _WwpLeosOamCriticalEventEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_WwpLeosOamCriticalEventEnable_Type.__name__=_C
_WwpLeosOamCriticalEventEnable_Object=MibTableColumn
wwpLeosOamCriticalEventEnable=_WwpLeosOamCriticalEventEnable_Object((1,3,6,1,4,1,6141,2,60,400,1,2,6,1,12),_WwpLeosOamCriticalEventEnable_Type())
wwpLeosOamCriticalEventEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosOamCriticalEventEnable.setStatus(_A)
_WwpLeosOamEventLogTable_Object=MibTable
wwpLeosOamEventLogTable=_WwpLeosOamEventLogTable_Object((1,3,6,1,4,1,6141,2,60,400,1,2,7))
if mibBuilder.loadTexts:wwpLeosOamEventLogTable.setStatus(_A)
_WwpLeosOamEventLogEntry_Object=MibTableRow
wwpLeosOamEventLogEntry=_WwpLeosOamEventLogEntry_Object((1,3,6,1,4,1,6141,2,60,400,1,2,7,1))
wwpLeosOamEventLogEntry.setIndexNames((0,_F,_Q),(0,_F,_g))
if mibBuilder.loadTexts:wwpLeosOamEventLogEntry.setStatus(_A)
class _WwpLeosOamEventLogPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_WwpLeosOamEventLogPort_Type.__name__=_C
_WwpLeosOamEventLogPort_Object=MibTableColumn
wwpLeosOamEventLogPort=_WwpLeosOamEventLogPort_Object((1,3,6,1,4,1,6141,2,60,400,1,2,7,1,1),_WwpLeosOamEventLogPort_Type())
wwpLeosOamEventLogPort.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosOamEventLogPort.setStatus(_A)
_WwpLeosOamEventLogIndex_Type=Unsigned32
_WwpLeosOamEventLogIndex_Object=MibTableColumn
wwpLeosOamEventLogIndex=_WwpLeosOamEventLogIndex_Object((1,3,6,1,4,1,6141,2,60,400,1,2,7,1,2),_WwpLeosOamEventLogIndex_Type())
wwpLeosOamEventLogIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosOamEventLogIndex.setStatus(_A)
_WwpLeosOamEventLogTimestamp_Type=TimeStamp
_WwpLeosOamEventLogTimestamp_Object=MibTableColumn
wwpLeosOamEventLogTimestamp=_WwpLeosOamEventLogTimestamp_Object((1,3,6,1,4,1,6141,2,60,400,1,2,7,1,3),_WwpLeosOamEventLogTimestamp_Type())
wwpLeosOamEventLogTimestamp.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosOamEventLogTimestamp.setStatus(_A)
class _WwpLeosOamEventLogOui_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,3));fixedLength=3
_WwpLeosOamEventLogOui_Type.__name__=_K
_WwpLeosOamEventLogOui_Object=MibTableColumn
wwpLeosOamEventLogOui=_WwpLeosOamEventLogOui_Object((1,3,6,1,4,1,6141,2,60,400,1,2,7,1,4),_WwpLeosOamEventLogOui_Type())
wwpLeosOamEventLogOui.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosOamEventLogOui.setStatus(_A)
_WwpLeosOamEventLogType_Type=Unsigned32
_WwpLeosOamEventLogType_Object=MibTableColumn
wwpLeosOamEventLogType=_WwpLeosOamEventLogType_Object((1,3,6,1,4,1,6141,2,60,400,1,2,7,1,5),_WwpLeosOamEventLogType_Type())
wwpLeosOamEventLogType.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosOamEventLogType.setStatus(_A)
class _WwpLeosOamEventLogLocation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('local',1),('remote',2)))
_WwpLeosOamEventLogLocation_Type.__name__=_C
_WwpLeosOamEventLogLocation_Object=MibTableColumn
wwpLeosOamEventLogLocation=_WwpLeosOamEventLogLocation_Object((1,3,6,1,4,1,6141,2,60,400,1,2,7,1,6),_WwpLeosOamEventLogLocation_Type())
wwpLeosOamEventLogLocation.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosOamEventLogLocation.setStatus(_A)
_WwpLeosOamEventLogWindowHi_Type=Unsigned32
_WwpLeosOamEventLogWindowHi_Object=MibTableColumn
wwpLeosOamEventLogWindowHi=_WwpLeosOamEventLogWindowHi_Object((1,3,6,1,4,1,6141,2,60,400,1,2,7,1,7),_WwpLeosOamEventLogWindowHi_Type())
wwpLeosOamEventLogWindowHi.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosOamEventLogWindowHi.setStatus(_A)
_WwpLeosOamEventLogWindowLo_Type=Unsigned32
_WwpLeosOamEventLogWindowLo_Object=MibTableColumn
wwpLeosOamEventLogWindowLo=_WwpLeosOamEventLogWindowLo_Object((1,3,6,1,4,1,6141,2,60,400,1,2,7,1,8),_WwpLeosOamEventLogWindowLo_Type())
wwpLeosOamEventLogWindowLo.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosOamEventLogWindowLo.setStatus(_A)
_WwpLeosOamEventLogThresholdHi_Type=Unsigned32
_WwpLeosOamEventLogThresholdHi_Object=MibTableColumn
wwpLeosOamEventLogThresholdHi=_WwpLeosOamEventLogThresholdHi_Object((1,3,6,1,4,1,6141,2,60,400,1,2,7,1,9),_WwpLeosOamEventLogThresholdHi_Type())
wwpLeosOamEventLogThresholdHi.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosOamEventLogThresholdHi.setStatus(_A)
_WwpLeosOamEventLogThresholdLo_Type=Unsigned32
_WwpLeosOamEventLogThresholdLo_Object=MibTableColumn
wwpLeosOamEventLogThresholdLo=_WwpLeosOamEventLogThresholdLo_Object((1,3,6,1,4,1,6141,2,60,400,1,2,7,1,10),_WwpLeosOamEventLogThresholdLo_Type())
wwpLeosOamEventLogThresholdLo.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosOamEventLogThresholdLo.setStatus(_A)
_WwpLeosOamEventLogValue_Type=Counter64
_WwpLeosOamEventLogValue_Object=MibTableColumn
wwpLeosOamEventLogValue=_WwpLeosOamEventLogValue_Object((1,3,6,1,4,1,6141,2,60,400,1,2,7,1,11),_WwpLeosOamEventLogValue_Type())
wwpLeosOamEventLogValue.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosOamEventLogValue.setStatus(_A)
_WwpLeosOamEventLogRunningTotal_Type=Counter64
_WwpLeosOamEventLogRunningTotal_Object=MibTableColumn
wwpLeosOamEventLogRunningTotal=_WwpLeosOamEventLogRunningTotal_Object((1,3,6,1,4,1,6141,2,60,400,1,2,7,1,12),_WwpLeosOamEventLogRunningTotal_Type())
wwpLeosOamEventLogRunningTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosOamEventLogRunningTotal.setStatus(_A)
_WwpLeosOamEventLogEventTotal_Type=Unsigned32
_WwpLeosOamEventLogEventTotal_Object=MibTableColumn
wwpLeosOamEventLogEventTotal=_WwpLeosOamEventLogEventTotal_Object((1,3,6,1,4,1,6141,2,60,400,1,2,7,1,13),_WwpLeosOamEventLogEventTotal_Type())
wwpLeosOamEventLogEventTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosOamEventLogEventTotal.setStatus(_A)
_WwpLeosOamGlobal_ObjectIdentity=ObjectIdentity
wwpLeosOamGlobal=_WwpLeosOamGlobal_ObjectIdentity((1,3,6,1,4,1,6141,2,60,400,1,2,8))
_WwpLeosOamStatsClear_Type=TruthValue
_WwpLeosOamStatsClear_Object=MibScalar
wwpLeosOamStatsClear=_WwpLeosOamStatsClear_Object((1,3,6,1,4,1,6141,2,60,400,1,2,8,1),_WwpLeosOamStatsClear_Type())
wwpLeosOamStatsClear.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosOamStatsClear.setStatus(_A)
_WwpLeosOamNotifMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
wwpLeosOamNotifMIBNotificationPrefix=_WwpLeosOamNotifMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,6141,2,60,400,1,3))
_WwpLeosOamNotifMIBNotification_ObjectIdentity=ObjectIdentity
wwpLeosOamNotifMIBNotification=_WwpLeosOamNotifMIBNotification_ObjectIdentity((1,3,6,1,4,1,6141,2,60,400,1,3,0))
wwpLeosOamLinkEventTrap=NotificationType((1,3,6,1,4,1,6141,2,60,400,1,3,0,1))
wwpLeosOamLinkEventTrap.setObjects(*((_F,_Q),(_F,_h),(_F,_i)))
if mibBuilder.loadTexts:wwpLeosOamLinkEventTrap.setStatus(_A)
wwpLeosOamLinkLostTimerActiveTrap=NotificationType((1,3,6,1,4,1,6141,2,60,400,1,3,0,2))
wwpLeosOamLinkLostTimerActiveTrap.setObjects(*((_F,_L),(_J,_N),(_J,_O),(_F,_R),(_F,_S),(_F,_T)))
if mibBuilder.loadTexts:wwpLeosOamLinkLostTimerActiveTrap.setStatus(_A)
wwpLeosOamLinkLostTimerExpiredTrap=NotificationType((1,3,6,1,4,1,6141,2,60,400,1,3,0,3))
wwpLeosOamLinkLostTimerExpiredTrap.setObjects(*((_F,_L),(_J,_N),(_J,_O),(_F,_R),(_F,_S),(_F,_T)))
if mibBuilder.loadTexts:wwpLeosOamLinkLostTimerExpiredTrap.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'wwpLeosOamMibModule':wwpLeosOamMibModule,'wwpLeosOamMIB':wwpLeosOamMIB,'wwpLeosOamConf':wwpLeosOamConf,'wwpLeosOamGroups':wwpLeosOamGroups,'wwpLeosOamCompls':wwpLeosOamCompls,'wwpLeosOamObjs':wwpLeosOamObjs,'wwpLeosOamTable':wwpLeosOamTable,'wwpLeosOamEntry':wwpLeosOamEntry,'wwpLeosOamAdminState':wwpLeosOamAdminState,_R:wwpLeosOamOperStatus,'wwpLeosOamMode':wwpLeosOamMode,'wwpLeosMaxOamPduSize':wwpLeosMaxOamPduSize,'wwpLeosOamConfigRevision':wwpLeosOamConfigRevision,'wwpLeosOamFunctionsSupported':wwpLeosOamFunctionsSupported,_L:wwpLeosOamPort,'wwpLeosOamPduTimer':wwpLeosOamPduTimer,'wwpLeosOamLinkLostTimer':wwpLeosOamLinkLostTimer,'wwpLeosOamPeerStatusNotifyState':wwpLeosOamPeerStatusNotifyState,'wwpLeosOamPeerTable':wwpLeosOamPeerTable,'wwpLeosOamPeerEntry':wwpLeosOamPeerEntry,_S:wwpLeosOamPeerStatus,_T:wwpLeosOamPeerMacAddress,'wwpLeosOamPeerVendorOui':wwpLeosOamPeerVendorOui,'wwpLeosOamPeerVendorInfo':wwpLeosOamPeerVendorInfo,'wwpLeosOamPeerMode':wwpLeosOamPeerMode,'wwpLeosOamPeerMaxOamPduSize':wwpLeosOamPeerMaxOamPduSize,'wwpLeosOamPeerConfigRevision':wwpLeosOamPeerConfigRevision,'wwpLeosOamPeerFunctionsSupported':wwpLeosOamPeerFunctionsSupported,_Z:wwpLeosOamLocalPort,'wwpLeosOamLoopbackTable':wwpLeosOamLoopbackTable,'wwpLeosOamLoopbackEntry':wwpLeosOamLoopbackEntry,'wwpLeosOamLoopbackCommand':wwpLeosOamLoopbackCommand,'wwpLeosOamLoopbackStatus':wwpLeosOamLoopbackStatus,'wwpLeosOamLoopbackIgnoreRx':wwpLeosOamLoopbackIgnoreRx,_b:wwpLeosOamLoopbackPort,'wwpLeosOamStatsTable':wwpLeosOamStatsTable,'wwpLeosOamStatsEntry':wwpLeosOamStatsEntry,'wwpLeosOamInformationTx':wwpLeosOamInformationTx,'wwpLeosOamInformationRx':wwpLeosOamInformationRx,'wwpLeosOamUniqueEventNotificationTx':wwpLeosOamUniqueEventNotificationTx,'wwpLeosOamUniqueEventNotificationRx':wwpLeosOamUniqueEventNotificationRx,'wwpLeosOamLoopbackControlTx':wwpLeosOamLoopbackControlTx,'wwpLeosOamLoopbackControlRx':wwpLeosOamLoopbackControlRx,'wwpLeosOamVariableRequestTx':wwpLeosOamVariableRequestTx,'wwpLeosOamVariableRequestRx':wwpLeosOamVariableRequestRx,'wwpLeosOamVariableResponseTx':wwpLeosOamVariableResponseTx,'wwpLeosOamVariableResponseRx':wwpLeosOamVariableResponseRx,'wwpLeosOamOrgSpecificTx':wwpLeosOamOrgSpecificTx,'wwpLeosOamOrgSpecificRx':wwpLeosOamOrgSpecificRx,'wwpLeosOamUnsupportedCodesTx':wwpLeosOamUnsupportedCodesTx,'wwpLeosOamUnsupportedCodesRx':wwpLeosOamUnsupportedCodesRx,'wwpLeosOamframesLostDueToOam':wwpLeosOamframesLostDueToOam,_d:wwpLeosOamStatsPort,'wwpLeosOamDuplicateEventNotificationTx':wwpLeosOamDuplicateEventNotificationTx,'wwpLeosOamDuplicateEventNotificationRx':wwpLeosOamDuplicateEventNotificationRx,'wwpLeosOamSystemEnableDisable':wwpLeosOamSystemEnableDisable,'wwpLeosOamEventConfigTable':wwpLeosOamEventConfigTable,'wwpLeosOamEventConfigEntry':wwpLeosOamEventConfigEntry,_e:wwpLeosOamEventPort,'wwpLeosOamErrFramePeriodWindow':wwpLeosOamErrFramePeriodWindow,'wwpLeosOamErrFramePeriodThreshold':wwpLeosOamErrFramePeriodThreshold,'wwpLeosOamErrFramePeriodEvNotifEnable':wwpLeosOamErrFramePeriodEvNotifEnable,'wwpLeosOamErrFrameWindow':wwpLeosOamErrFrameWindow,'wwpLeosOamErrFrameThreshold':wwpLeosOamErrFrameThreshold,'wwpLeosOamErrFrameEvNotifEnable':wwpLeosOamErrFrameEvNotifEnable,'wwpLeosOamErrFrameSecsSummaryWindow':wwpLeosOamErrFrameSecsSummaryWindow,'wwpLeosOamErrFrameSecsSummaryThreshold':wwpLeosOamErrFrameSecsSummaryThreshold,'wwpLeosOamErrFrameSecsEvNotifEnable':wwpLeosOamErrFrameSecsEvNotifEnable,'wwpLeosOamDyingGaspEnable':wwpLeosOamDyingGaspEnable,'wwpLeosOamCriticalEventEnable':wwpLeosOamCriticalEventEnable,'wwpLeosOamEventLogTable':wwpLeosOamEventLogTable,'wwpLeosOamEventLogEntry':wwpLeosOamEventLogEntry,_Q:wwpLeosOamEventLogPort,_g:wwpLeosOamEventLogIndex,'wwpLeosOamEventLogTimestamp':wwpLeosOamEventLogTimestamp,'wwpLeosOamEventLogOui':wwpLeosOamEventLogOui,_h:wwpLeosOamEventLogType,_i:wwpLeosOamEventLogLocation,'wwpLeosOamEventLogWindowHi':wwpLeosOamEventLogWindowHi,'wwpLeosOamEventLogWindowLo':wwpLeosOamEventLogWindowLo,'wwpLeosOamEventLogThresholdHi':wwpLeosOamEventLogThresholdHi,'wwpLeosOamEventLogThresholdLo':wwpLeosOamEventLogThresholdLo,'wwpLeosOamEventLogValue':wwpLeosOamEventLogValue,'wwpLeosOamEventLogRunningTotal':wwpLeosOamEventLogRunningTotal,'wwpLeosOamEventLogEventTotal':wwpLeosOamEventLogEventTotal,'wwpLeosOamGlobal':wwpLeosOamGlobal,'wwpLeosOamStatsClear':wwpLeosOamStatsClear,'wwpLeosOamNotifMIBNotificationPrefix':wwpLeosOamNotifMIBNotificationPrefix,'wwpLeosOamNotifMIBNotification':wwpLeosOamNotifMIBNotification,'wwpLeosOamLinkEventTrap':wwpLeosOamLinkEventTrap,'wwpLeosOamLinkLostTimerActiveTrap':wwpLeosOamLinkLostTimerActiveTrap,'wwpLeosOamLinkLostTimerExpiredTrap':wwpLeosOamLinkLostTimerExpiredTrap})