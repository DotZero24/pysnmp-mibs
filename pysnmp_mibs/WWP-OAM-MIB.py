_Z='wwpOamEventLogIndex'
_Y='wwpOamEventLogPort'
_X='tenths of a second'
_W='wwpOamEventPort'
_V='wwpOamStatsPort'
_U='noLoopback'
_T='wwpOamLoopbackPort'
_S='unknown'
_R='wwpOamLocalPort'
_Q='variableSupport'
_P='eventSupport'
_O='loopbackSupport'
_N='unidirectionalSupport'
_M='passive'
_L='wwpOamPort'
_K='active'
_J='Bits'
_I='OctetString'
_H='enabled'
_G='disabled'
_F='WWP-OAM-MIB'
_E='read-write'
_D='frames'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_I,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_J,'Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeStamp')
wwpModules,=mibBuilder.importSymbols('WWP-SMI','wwpModules')
wwpOamMibModule=ModuleIdentity((1,3,6,1,4,1,6141,2,400))
_WwpOamMIB_ObjectIdentity=ObjectIdentity
wwpOamMIB=_WwpOamMIB_ObjectIdentity((1,3,6,1,4,1,6141,2,400,1))
_WwpOamConf_ObjectIdentity=ObjectIdentity
wwpOamConf=_WwpOamConf_ObjectIdentity((1,3,6,1,4,1,6141,2,400,1,1))
_WwpOamGroups_ObjectIdentity=ObjectIdentity
wwpOamGroups=_WwpOamGroups_ObjectIdentity((1,3,6,1,4,1,6141,2,400,1,1,1))
_WwpOamCompls_ObjectIdentity=ObjectIdentity
wwpOamCompls=_WwpOamCompls_ObjectIdentity((1,3,6,1,4,1,6141,2,400,1,1,2))
_WwpOamObjs_ObjectIdentity=ObjectIdentity
wwpOamObjs=_WwpOamObjs_ObjectIdentity((1,3,6,1,4,1,6141,2,400,1,2))
_WwpOamTable_Object=MibTable
wwpOamTable=_WwpOamTable_Object((1,3,6,1,4,1,6141,2,400,1,2,1))
if mibBuilder.loadTexts:wwpOamTable.setStatus(_A)
_WwpOamEntry_Object=MibTableRow
wwpOamEntry=_WwpOamEntry_Object((1,3,6,1,4,1,6141,2,400,1,2,1,1))
wwpOamEntry.setIndexNames((0,_F,_L))
if mibBuilder.loadTexts:wwpOamEntry.setStatus(_A)
class _WwpOamAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_WwpOamAdminState_Type.__name__=_C
_WwpOamAdminState_Object=MibTableColumn
wwpOamAdminState=_WwpOamAdminState_Object((1,3,6,1,4,1,6141,2,400,1,2,1,1,1),_WwpOamAdminState_Type())
wwpOamAdminState.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpOamAdminState.setStatus(_A)
class _WwpOamOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_G,1),('linkfault',2),('passiveWait',3),('activeSendLocal',4),('sendLocalAndRemote',5),('sendLocalAndRemoteOk',6),('oamPeeringLocallyRejected',7),('oamPeeringRemotelyRejected',8),('operational',9)))
_WwpOamOperStatus_Type.__name__=_C
_WwpOamOperStatus_Object=MibTableColumn
wwpOamOperStatus=_WwpOamOperStatus_Object((1,3,6,1,4,1,6141,2,400,1,2,1,1,2),_WwpOamOperStatus_Type())
wwpOamOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpOamOperStatus.setStatus(_A)
class _WwpOamMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_M,2)))
_WwpOamMode_Type.__name__=_C
_WwpOamMode_Object=MibTableColumn
wwpOamMode=_WwpOamMode_Object((1,3,6,1,4,1,6141,2,400,1,2,1,1,3),_WwpOamMode_Type())
wwpOamMode.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpOamMode.setStatus(_A)
_WwpMaxOamPduSize_Type=Integer32
_WwpMaxOamPduSize_Object=MibTableColumn
wwpMaxOamPduSize=_WwpMaxOamPduSize_Object((1,3,6,1,4,1,6141,2,400,1,2,1,1,4),_WwpMaxOamPduSize_Type())
wwpMaxOamPduSize.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpMaxOamPduSize.setStatus(_A)
if mibBuilder.loadTexts:wwpMaxOamPduSize.setUnits('bytes')
_WwpOamConfigRevision_Type=Unsigned32
_WwpOamConfigRevision_Object=MibTableColumn
wwpOamConfigRevision=_WwpOamConfigRevision_Object((1,3,6,1,4,1,6141,2,400,1,2,1,1,5),_WwpOamConfigRevision_Type())
wwpOamConfigRevision.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpOamConfigRevision.setStatus(_A)
class _WwpOamFunctionsSupported_Type(Bits):namedValues=NamedValues(*((_N,0),(_O,1),(_P,2),(_Q,3)))
_WwpOamFunctionsSupported_Type.__name__=_J
_WwpOamFunctionsSupported_Object=MibTableColumn
wwpOamFunctionsSupported=_WwpOamFunctionsSupported_Object((1,3,6,1,4,1,6141,2,400,1,2,1,1,6),_WwpOamFunctionsSupported_Type())
wwpOamFunctionsSupported.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpOamFunctionsSupported.setStatus(_A)
class _WwpOamPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_WwpOamPort_Type.__name__=_C
_WwpOamPort_Object=MibTableColumn
wwpOamPort=_WwpOamPort_Object((1,3,6,1,4,1,6141,2,400,1,2,1,1,7),_WwpOamPort_Type())
wwpOamPort.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpOamPort.setStatus(_A)
_WwpOamPeerTable_Object=MibTable
wwpOamPeerTable=_WwpOamPeerTable_Object((1,3,6,1,4,1,6141,2,400,1,2,2))
if mibBuilder.loadTexts:wwpOamPeerTable.setStatus(_A)
_WwpOamPeerEntry_Object=MibTableRow
wwpOamPeerEntry=_WwpOamPeerEntry_Object((1,3,6,1,4,1,6141,2,400,1,2,2,1))
wwpOamPeerEntry.setIndexNames((0,_F,_R))
if mibBuilder.loadTexts:wwpOamPeerEntry.setStatus(_A)
class _WwpOamPeerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),('inactive',2)))
_WwpOamPeerStatus_Type.__name__=_C
_WwpOamPeerStatus_Object=MibTableColumn
wwpOamPeerStatus=_WwpOamPeerStatus_Object((1,3,6,1,4,1,6141,2,400,1,2,2,1,1),_WwpOamPeerStatus_Type())
wwpOamPeerStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpOamPeerStatus.setStatus(_A)
class _WwpOamPeerMacAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_WwpOamPeerMacAddress_Type.__name__=_I
_WwpOamPeerMacAddress_Object=MibTableColumn
wwpOamPeerMacAddress=_WwpOamPeerMacAddress_Object((1,3,6,1,4,1,6141,2,400,1,2,2,1,2),_WwpOamPeerMacAddress_Type())
wwpOamPeerMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpOamPeerMacAddress.setStatus(_A)
class _WwpOamPeerVendorOui_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,3));fixedLength=3
_WwpOamPeerVendorOui_Type.__name__=_I
_WwpOamPeerVendorOui_Object=MibTableColumn
wwpOamPeerVendorOui=_WwpOamPeerVendorOui_Object((1,3,6,1,4,1,6141,2,400,1,2,2,1,3),_WwpOamPeerVendorOui_Type())
wwpOamPeerVendorOui.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpOamPeerVendorOui.setStatus(_A)
_WwpOamPeerVendorInfo_Type=Unsigned32
_WwpOamPeerVendorInfo_Object=MibTableColumn
wwpOamPeerVendorInfo=_WwpOamPeerVendorInfo_Object((1,3,6,1,4,1,6141,2,400,1,2,2,1,4),_WwpOamPeerVendorInfo_Type())
wwpOamPeerVendorInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpOamPeerVendorInfo.setStatus(_A)
class _WwpOamPeerMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_K,1),(_M,2),(_S,3)))
_WwpOamPeerMode_Type.__name__=_C
_WwpOamPeerMode_Object=MibTableColumn
wwpOamPeerMode=_WwpOamPeerMode_Object((1,3,6,1,4,1,6141,2,400,1,2,2,1,5),_WwpOamPeerMode_Type())
wwpOamPeerMode.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpOamPeerMode.setStatus(_A)
_WwpOamPeerMaxOamPduSize_Type=Integer32
_WwpOamPeerMaxOamPduSize_Object=MibTableColumn
wwpOamPeerMaxOamPduSize=_WwpOamPeerMaxOamPduSize_Object((1,3,6,1,4,1,6141,2,400,1,2,2,1,6),_WwpOamPeerMaxOamPduSize_Type())
wwpOamPeerMaxOamPduSize.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpOamPeerMaxOamPduSize.setStatus(_A)
if mibBuilder.loadTexts:wwpOamPeerMaxOamPduSize.setUnits('bytes')
_WwpOamPeerConfigRevision_Type=Unsigned32
_WwpOamPeerConfigRevision_Object=MibTableColumn
wwpOamPeerConfigRevision=_WwpOamPeerConfigRevision_Object((1,3,6,1,4,1,6141,2,400,1,2,2,1,7),_WwpOamPeerConfigRevision_Type())
wwpOamPeerConfigRevision.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpOamPeerConfigRevision.setStatus(_A)
class _WwpOamPeerFunctionsSupported_Type(Bits):namedValues=NamedValues(*((_N,0),(_O,1),(_P,2),(_Q,3)))
_WwpOamPeerFunctionsSupported_Type.__name__=_J
_WwpOamPeerFunctionsSupported_Object=MibTableColumn
wwpOamPeerFunctionsSupported=_WwpOamPeerFunctionsSupported_Object((1,3,6,1,4,1,6141,2,400,1,2,2,1,8),_WwpOamPeerFunctionsSupported_Type())
wwpOamPeerFunctionsSupported.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpOamPeerFunctionsSupported.setStatus(_A)
class _WwpOamLocalPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_WwpOamLocalPort_Type.__name__=_C
_WwpOamLocalPort_Object=MibTableColumn
wwpOamLocalPort=_WwpOamLocalPort_Object((1,3,6,1,4,1,6141,2,400,1,2,2,1,9),_WwpOamLocalPort_Type())
wwpOamLocalPort.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpOamLocalPort.setStatus(_A)
_WwpOamLoopbackTable_Object=MibTable
wwpOamLoopbackTable=_WwpOamLoopbackTable_Object((1,3,6,1,4,1,6141,2,400,1,2,3))
if mibBuilder.loadTexts:wwpOamLoopbackTable.setStatus(_A)
_WwpOamLoopbackEntry_Object=MibTableRow
wwpOamLoopbackEntry=_WwpOamLoopbackEntry_Object((1,3,6,1,4,1,6141,2,400,1,2,3,1))
wwpOamLoopbackEntry.setIndexNames((0,_F,_T))
if mibBuilder.loadTexts:wwpOamLoopbackEntry.setStatus(_A)
class _WwpOamLoopbackCommand_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_U,1),('startRemoteLoopback',2),('stopRemoteLoopback',3)))
_WwpOamLoopbackCommand_Type.__name__=_C
_WwpOamLoopbackCommand_Object=MibTableColumn
wwpOamLoopbackCommand=_WwpOamLoopbackCommand_Object((1,3,6,1,4,1,6141,2,400,1,2,3,1,1),_WwpOamLoopbackCommand_Type())
wwpOamLoopbackCommand.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpOamLoopbackCommand.setStatus(_A)
class _WwpOamLoopbackStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_U,1),('initiatingLoopback',2),('remoteLoopback',3),('terminatingLoopback',4),('localLoopback',5),(_S,6)))
_WwpOamLoopbackStatus_Type.__name__=_C
_WwpOamLoopbackStatus_Object=MibTableColumn
wwpOamLoopbackStatus=_WwpOamLoopbackStatus_Object((1,3,6,1,4,1,6141,2,400,1,2,3,1,2),_WwpOamLoopbackStatus_Type())
wwpOamLoopbackStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpOamLoopbackStatus.setStatus(_A)
class _WwpOamLoopbackIgnoreRx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ignore',1),('process',2)))
_WwpOamLoopbackIgnoreRx_Type.__name__=_C
_WwpOamLoopbackIgnoreRx_Object=MibTableColumn
wwpOamLoopbackIgnoreRx=_WwpOamLoopbackIgnoreRx_Object((1,3,6,1,4,1,6141,2,400,1,2,3,1,3),_WwpOamLoopbackIgnoreRx_Type())
wwpOamLoopbackIgnoreRx.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpOamLoopbackIgnoreRx.setStatus(_A)
class _WwpOamLoopbackPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_WwpOamLoopbackPort_Type.__name__=_C
_WwpOamLoopbackPort_Object=MibTableColumn
wwpOamLoopbackPort=_WwpOamLoopbackPort_Object((1,3,6,1,4,1,6141,2,400,1,2,3,1,4),_WwpOamLoopbackPort_Type())
wwpOamLoopbackPort.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpOamLoopbackPort.setStatus(_A)
_WwpOamStatsTable_Object=MibTable
wwpOamStatsTable=_WwpOamStatsTable_Object((1,3,6,1,4,1,6141,2,400,1,2,4))
if mibBuilder.loadTexts:wwpOamStatsTable.setStatus(_A)
_WwpOamStatsEntry_Object=MibTableRow
wwpOamStatsEntry=_WwpOamStatsEntry_Object((1,3,6,1,4,1,6141,2,400,1,2,4,1))
wwpOamStatsEntry.setIndexNames((0,_F,_V))
if mibBuilder.loadTexts:wwpOamStatsEntry.setStatus(_A)
_WwpOamInformationTx_Type=Counter32
_WwpOamInformationTx_Object=MibTableColumn
wwpOamInformationTx=_WwpOamInformationTx_Object((1,3,6,1,4,1,6141,2,400,1,2,4,1,1),_WwpOamInformationTx_Type())
wwpOamInformationTx.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpOamInformationTx.setStatus(_A)
if mibBuilder.loadTexts:wwpOamInformationTx.setUnits(_D)
_WwpOamInformationRx_Type=Counter32
_WwpOamInformationRx_Object=MibTableColumn
wwpOamInformationRx=_WwpOamInformationRx_Object((1,3,6,1,4,1,6141,2,400,1,2,4,1,2),_WwpOamInformationRx_Type())
wwpOamInformationRx.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpOamInformationRx.setStatus(_A)
if mibBuilder.loadTexts:wwpOamInformationRx.setUnits(_D)
_WwpOamUniqueEventNotificationTx_Type=Counter32
_WwpOamUniqueEventNotificationTx_Object=MibTableColumn
wwpOamUniqueEventNotificationTx=_WwpOamUniqueEventNotificationTx_Object((1,3,6,1,4,1,6141,2,400,1,2,4,1,3),_WwpOamUniqueEventNotificationTx_Type())
wwpOamUniqueEventNotificationTx.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpOamUniqueEventNotificationTx.setStatus(_A)
if mibBuilder.loadTexts:wwpOamUniqueEventNotificationTx.setUnits(_D)
_WwpOamUniqueEventNotificationRx_Type=Counter32
_WwpOamUniqueEventNotificationRx_Object=MibTableColumn
wwpOamUniqueEventNotificationRx=_WwpOamUniqueEventNotificationRx_Object((1,3,6,1,4,1,6141,2,400,1,2,4,1,4),_WwpOamUniqueEventNotificationRx_Type())
wwpOamUniqueEventNotificationRx.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpOamUniqueEventNotificationRx.setStatus(_A)
if mibBuilder.loadTexts:wwpOamUniqueEventNotificationRx.setUnits(_D)
_WwpOamLoopbackControlTx_Type=Counter32
_WwpOamLoopbackControlTx_Object=MibTableColumn
wwpOamLoopbackControlTx=_WwpOamLoopbackControlTx_Object((1,3,6,1,4,1,6141,2,400,1,2,4,1,5),_WwpOamLoopbackControlTx_Type())
wwpOamLoopbackControlTx.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpOamLoopbackControlTx.setStatus(_A)
if mibBuilder.loadTexts:wwpOamLoopbackControlTx.setUnits(_D)
_WwpOamLoopbackControlRx_Type=Counter32
_WwpOamLoopbackControlRx_Object=MibTableColumn
wwpOamLoopbackControlRx=_WwpOamLoopbackControlRx_Object((1,3,6,1,4,1,6141,2,400,1,2,4,1,6),_WwpOamLoopbackControlRx_Type())
wwpOamLoopbackControlRx.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpOamLoopbackControlRx.setStatus(_A)
if mibBuilder.loadTexts:wwpOamLoopbackControlRx.setUnits(_D)
_WwpOamVariableRequestTx_Type=Counter32
_WwpOamVariableRequestTx_Object=MibTableColumn
wwpOamVariableRequestTx=_WwpOamVariableRequestTx_Object((1,3,6,1,4,1,6141,2,400,1,2,4,1,7),_WwpOamVariableRequestTx_Type())
wwpOamVariableRequestTx.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpOamVariableRequestTx.setStatus(_A)
if mibBuilder.loadTexts:wwpOamVariableRequestTx.setUnits(_D)
_WwpOamVariableRequestRx_Type=Counter32
_WwpOamVariableRequestRx_Object=MibTableColumn
wwpOamVariableRequestRx=_WwpOamVariableRequestRx_Object((1,3,6,1,4,1,6141,2,400,1,2,4,1,8),_WwpOamVariableRequestRx_Type())
wwpOamVariableRequestRx.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpOamVariableRequestRx.setStatus(_A)
if mibBuilder.loadTexts:wwpOamVariableRequestRx.setUnits(_D)
_WwpOamVariableResponseTx_Type=Counter32
_WwpOamVariableResponseTx_Object=MibTableColumn
wwpOamVariableResponseTx=_WwpOamVariableResponseTx_Object((1,3,6,1,4,1,6141,2,400,1,2,4,1,9),_WwpOamVariableResponseTx_Type())
wwpOamVariableResponseTx.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpOamVariableResponseTx.setStatus(_A)
if mibBuilder.loadTexts:wwpOamVariableResponseTx.setUnits(_D)
_WwpOamVariableResponseRx_Type=Counter32
_WwpOamVariableResponseRx_Object=MibTableColumn
wwpOamVariableResponseRx=_WwpOamVariableResponseRx_Object((1,3,6,1,4,1,6141,2,400,1,2,4,1,10),_WwpOamVariableResponseRx_Type())
wwpOamVariableResponseRx.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpOamVariableResponseRx.setStatus(_A)
if mibBuilder.loadTexts:wwpOamVariableResponseRx.setUnits(_D)
_WwpOamOrgSpecificTx_Type=Counter32
_WwpOamOrgSpecificTx_Object=MibTableColumn
wwpOamOrgSpecificTx=_WwpOamOrgSpecificTx_Object((1,3,6,1,4,1,6141,2,400,1,2,4,1,11),_WwpOamOrgSpecificTx_Type())
wwpOamOrgSpecificTx.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpOamOrgSpecificTx.setStatus(_A)
if mibBuilder.loadTexts:wwpOamOrgSpecificTx.setUnits(_D)
_WwpOamOrgSpecificRx_Type=Counter32
_WwpOamOrgSpecificRx_Object=MibTableColumn
wwpOamOrgSpecificRx=_WwpOamOrgSpecificRx_Object((1,3,6,1,4,1,6141,2,400,1,2,4,1,12),_WwpOamOrgSpecificRx_Type())
wwpOamOrgSpecificRx.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpOamOrgSpecificRx.setStatus(_A)
if mibBuilder.loadTexts:wwpOamOrgSpecificRx.setUnits(_D)
_WwpOamUnsupportedCodesTx_Type=Counter32
_WwpOamUnsupportedCodesTx_Object=MibTableColumn
wwpOamUnsupportedCodesTx=_WwpOamUnsupportedCodesTx_Object((1,3,6,1,4,1,6141,2,400,1,2,4,1,13),_WwpOamUnsupportedCodesTx_Type())
wwpOamUnsupportedCodesTx.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpOamUnsupportedCodesTx.setStatus(_A)
if mibBuilder.loadTexts:wwpOamUnsupportedCodesTx.setUnits(_D)
_WwpOamUnsupportedCodesRx_Type=Counter32
_WwpOamUnsupportedCodesRx_Object=MibTableColumn
wwpOamUnsupportedCodesRx=_WwpOamUnsupportedCodesRx_Object((1,3,6,1,4,1,6141,2,400,1,2,4,1,14),_WwpOamUnsupportedCodesRx_Type())
wwpOamUnsupportedCodesRx.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpOamUnsupportedCodesRx.setStatus(_A)
if mibBuilder.loadTexts:wwpOamUnsupportedCodesRx.setUnits(_D)
_WwpOamframesLostDueToOam_Type=Counter32
_WwpOamframesLostDueToOam_Object=MibTableColumn
wwpOamframesLostDueToOam=_WwpOamframesLostDueToOam_Object((1,3,6,1,4,1,6141,2,400,1,2,4,1,15),_WwpOamframesLostDueToOam_Type())
wwpOamframesLostDueToOam.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpOamframesLostDueToOam.setStatus(_A)
if mibBuilder.loadTexts:wwpOamframesLostDueToOam.setUnits(_D)
class _WwpOamStatsPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_WwpOamStatsPort_Type.__name__=_C
_WwpOamStatsPort_Object=MibTableColumn
wwpOamStatsPort=_WwpOamStatsPort_Object((1,3,6,1,4,1,6141,2,400,1,2,4,1,16),_WwpOamStatsPort_Type())
wwpOamStatsPort.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpOamStatsPort.setStatus(_A)
_WwpOamDuplicateEventNotificationTx_Type=Counter32
_WwpOamDuplicateEventNotificationTx_Object=MibTableColumn
wwpOamDuplicateEventNotificationTx=_WwpOamDuplicateEventNotificationTx_Object((1,3,6,1,4,1,6141,2,400,1,2,4,1,17),_WwpOamDuplicateEventNotificationTx_Type())
wwpOamDuplicateEventNotificationTx.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpOamDuplicateEventNotificationTx.setStatus(_A)
if mibBuilder.loadTexts:wwpOamDuplicateEventNotificationTx.setUnits(_D)
_WwpOamDuplicateEventNotificationRx_Type=Counter32
_WwpOamDuplicateEventNotificationRx_Object=MibTableColumn
wwpOamDuplicateEventNotificationRx=_WwpOamDuplicateEventNotificationRx_Object((1,3,6,1,4,1,6141,2,400,1,2,4,1,18),_WwpOamDuplicateEventNotificationRx_Type())
wwpOamDuplicateEventNotificationRx.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpOamDuplicateEventNotificationRx.setStatus(_A)
if mibBuilder.loadTexts:wwpOamDuplicateEventNotificationRx.setUnits(_D)
class _WwpOamSystemEnableDisable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_WwpOamSystemEnableDisable_Type.__name__=_C
_WwpOamSystemEnableDisable_Object=MibScalar
wwpOamSystemEnableDisable=_WwpOamSystemEnableDisable_Object((1,3,6,1,4,1,6141,2,400,1,2,5),_WwpOamSystemEnableDisable_Type())
wwpOamSystemEnableDisable.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpOamSystemEnableDisable.setStatus(_A)
_WwpOamEventConfigTable_Object=MibTable
wwpOamEventConfigTable=_WwpOamEventConfigTable_Object((1,3,6,1,4,1,6141,2,400,1,2,6))
if mibBuilder.loadTexts:wwpOamEventConfigTable.setStatus(_A)
_WwpOamEventConfigEntry_Object=MibTableRow
wwpOamEventConfigEntry=_WwpOamEventConfigEntry_Object((1,3,6,1,4,1,6141,2,400,1,2,6,1))
wwpOamEventConfigEntry.setIndexNames((0,_F,_W))
if mibBuilder.loadTexts:wwpOamEventConfigEntry.setStatus(_A)
class _WwpOamEventPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_WwpOamEventPort_Type.__name__=_C
_WwpOamEventPort_Object=MibTableColumn
wwpOamEventPort=_WwpOamEventPort_Object((1,3,6,1,4,1,6141,2,400,1,2,6,1,1),_WwpOamEventPort_Type())
wwpOamEventPort.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpOamEventPort.setStatus(_A)
_WwpOamErrFramePeriodWindow_Type=Unsigned32
_WwpOamErrFramePeriodWindow_Object=MibTableColumn
wwpOamErrFramePeriodWindow=_WwpOamErrFramePeriodWindow_Object((1,3,6,1,4,1,6141,2,400,1,2,6,1,2),_WwpOamErrFramePeriodWindow_Type())
wwpOamErrFramePeriodWindow.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpOamErrFramePeriodWindow.setStatus(_A)
if mibBuilder.loadTexts:wwpOamErrFramePeriodWindow.setUnits(_D)
_WwpOamErrFramePeriodThreshold_Type=Unsigned32
_WwpOamErrFramePeriodThreshold_Object=MibTableColumn
wwpOamErrFramePeriodThreshold=_WwpOamErrFramePeriodThreshold_Object((1,3,6,1,4,1,6141,2,400,1,2,6,1,3),_WwpOamErrFramePeriodThreshold_Type())
wwpOamErrFramePeriodThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpOamErrFramePeriodThreshold.setStatus(_A)
if mibBuilder.loadTexts:wwpOamErrFramePeriodThreshold.setUnits(_D)
class _WwpOamErrFramePeriodEvNotifEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_WwpOamErrFramePeriodEvNotifEnable_Type.__name__=_C
_WwpOamErrFramePeriodEvNotifEnable_Object=MibTableColumn
wwpOamErrFramePeriodEvNotifEnable=_WwpOamErrFramePeriodEvNotifEnable_Object((1,3,6,1,4,1,6141,2,400,1,2,6,1,4),_WwpOamErrFramePeriodEvNotifEnable_Type())
wwpOamErrFramePeriodEvNotifEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpOamErrFramePeriodEvNotifEnable.setStatus(_A)
_WwpOamErrFrameWindow_Type=Unsigned32
_WwpOamErrFrameWindow_Object=MibTableColumn
wwpOamErrFrameWindow=_WwpOamErrFrameWindow_Object((1,3,6,1,4,1,6141,2,400,1,2,6,1,5),_WwpOamErrFrameWindow_Type())
wwpOamErrFrameWindow.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpOamErrFrameWindow.setStatus(_A)
if mibBuilder.loadTexts:wwpOamErrFrameWindow.setUnits(_X)
_WwpOamErrFrameThreshold_Type=Unsigned32
_WwpOamErrFrameThreshold_Object=MibTableColumn
wwpOamErrFrameThreshold=_WwpOamErrFrameThreshold_Object((1,3,6,1,4,1,6141,2,400,1,2,6,1,6),_WwpOamErrFrameThreshold_Type())
wwpOamErrFrameThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpOamErrFrameThreshold.setStatus(_A)
if mibBuilder.loadTexts:wwpOamErrFrameThreshold.setUnits(_D)
class _WwpOamErrFrameEvNotifEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_WwpOamErrFrameEvNotifEnable_Type.__name__=_C
_WwpOamErrFrameEvNotifEnable_Object=MibTableColumn
wwpOamErrFrameEvNotifEnable=_WwpOamErrFrameEvNotifEnable_Object((1,3,6,1,4,1,6141,2,400,1,2,6,1,7),_WwpOamErrFrameEvNotifEnable_Type())
wwpOamErrFrameEvNotifEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpOamErrFrameEvNotifEnable.setStatus(_A)
class _WwpOamErrFrameSecsSummaryWindow_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,9000))
_WwpOamErrFrameSecsSummaryWindow_Type.__name__=_C
_WwpOamErrFrameSecsSummaryWindow_Object=MibTableColumn
wwpOamErrFrameSecsSummaryWindow=_WwpOamErrFrameSecsSummaryWindow_Object((1,3,6,1,4,1,6141,2,400,1,2,6,1,8),_WwpOamErrFrameSecsSummaryWindow_Type())
wwpOamErrFrameSecsSummaryWindow.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpOamErrFrameSecsSummaryWindow.setStatus(_A)
if mibBuilder.loadTexts:wwpOamErrFrameSecsSummaryWindow.setUnits(_X)
_WwpOamErrFrameSecsSummaryThreshold_Type=Integer32
_WwpOamErrFrameSecsSummaryThreshold_Object=MibTableColumn
wwpOamErrFrameSecsSummaryThreshold=_WwpOamErrFrameSecsSummaryThreshold_Object((1,3,6,1,4,1,6141,2,400,1,2,6,1,9),_WwpOamErrFrameSecsSummaryThreshold_Type())
wwpOamErrFrameSecsSummaryThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpOamErrFrameSecsSummaryThreshold.setStatus(_A)
if mibBuilder.loadTexts:wwpOamErrFrameSecsSummaryThreshold.setUnits('errored frame seconds')
class _WwpOamErrFrameSecsEvNotifEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_WwpOamErrFrameSecsEvNotifEnable_Type.__name__=_C
_WwpOamErrFrameSecsEvNotifEnable_Object=MibTableColumn
wwpOamErrFrameSecsEvNotifEnable=_WwpOamErrFrameSecsEvNotifEnable_Object((1,3,6,1,4,1,6141,2,400,1,2,6,1,10),_WwpOamErrFrameSecsEvNotifEnable_Type())
wwpOamErrFrameSecsEvNotifEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpOamErrFrameSecsEvNotifEnable.setStatus(_A)
class _WwpOamDyingGaspEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_WwpOamDyingGaspEnable_Type.__name__=_C
_WwpOamDyingGaspEnable_Object=MibTableColumn
wwpOamDyingGaspEnable=_WwpOamDyingGaspEnable_Object((1,3,6,1,4,1,6141,2,400,1,2,6,1,11),_WwpOamDyingGaspEnable_Type())
wwpOamDyingGaspEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpOamDyingGaspEnable.setStatus(_A)
class _WwpOamCriticalEventEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_WwpOamCriticalEventEnable_Type.__name__=_C
_WwpOamCriticalEventEnable_Object=MibTableColumn
wwpOamCriticalEventEnable=_WwpOamCriticalEventEnable_Object((1,3,6,1,4,1,6141,2,400,1,2,6,1,12),_WwpOamCriticalEventEnable_Type())
wwpOamCriticalEventEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpOamCriticalEventEnable.setStatus(_A)
_WwpOamEventLogTable_Object=MibTable
wwpOamEventLogTable=_WwpOamEventLogTable_Object((1,3,6,1,4,1,6141,2,400,1,2,7))
if mibBuilder.loadTexts:wwpOamEventLogTable.setStatus(_A)
_WwpOamEventLogEntry_Object=MibTableRow
wwpOamEventLogEntry=_WwpOamEventLogEntry_Object((1,3,6,1,4,1,6141,2,400,1,2,7,1))
wwpOamEventLogEntry.setIndexNames((0,_F,_Y),(0,_F,_Z))
if mibBuilder.loadTexts:wwpOamEventLogEntry.setStatus(_A)
class _WwpOamEventLogPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_WwpOamEventLogPort_Type.__name__=_C
_WwpOamEventLogPort_Object=MibTableColumn
wwpOamEventLogPort=_WwpOamEventLogPort_Object((1,3,6,1,4,1,6141,2,400,1,2,7,1,1),_WwpOamEventLogPort_Type())
wwpOamEventLogPort.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpOamEventLogPort.setStatus(_A)
_WwpOamEventLogIndex_Type=Unsigned32
_WwpOamEventLogIndex_Object=MibTableColumn
wwpOamEventLogIndex=_WwpOamEventLogIndex_Object((1,3,6,1,4,1,6141,2,400,1,2,7,1,2),_WwpOamEventLogIndex_Type())
wwpOamEventLogIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpOamEventLogIndex.setStatus(_A)
_WwpOamEventLogTimestamp_Type=TimeStamp
_WwpOamEventLogTimestamp_Object=MibTableColumn
wwpOamEventLogTimestamp=_WwpOamEventLogTimestamp_Object((1,3,6,1,4,1,6141,2,400,1,2,7,1,3),_WwpOamEventLogTimestamp_Type())
wwpOamEventLogTimestamp.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpOamEventLogTimestamp.setStatus(_A)
class _WwpOamEventLogOui_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,3));fixedLength=3
_WwpOamEventLogOui_Type.__name__=_I
_WwpOamEventLogOui_Object=MibTableColumn
wwpOamEventLogOui=_WwpOamEventLogOui_Object((1,3,6,1,4,1,6141,2,400,1,2,7,1,4),_WwpOamEventLogOui_Type())
wwpOamEventLogOui.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpOamEventLogOui.setStatus(_A)
_WwpOamEventLogType_Type=Unsigned32
_WwpOamEventLogType_Object=MibTableColumn
wwpOamEventLogType=_WwpOamEventLogType_Object((1,3,6,1,4,1,6141,2,400,1,2,7,1,5),_WwpOamEventLogType_Type())
wwpOamEventLogType.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpOamEventLogType.setStatus(_A)
class _WwpOamEventLogLocation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('local',1),('remote',2)))
_WwpOamEventLogLocation_Type.__name__=_C
_WwpOamEventLogLocation_Object=MibTableColumn
wwpOamEventLogLocation=_WwpOamEventLogLocation_Object((1,3,6,1,4,1,6141,2,400,1,2,7,1,6),_WwpOamEventLogLocation_Type())
wwpOamEventLogLocation.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpOamEventLogLocation.setStatus(_A)
_WwpOamEventLogWindowHi_Type=Unsigned32
_WwpOamEventLogWindowHi_Object=MibTableColumn
wwpOamEventLogWindowHi=_WwpOamEventLogWindowHi_Object((1,3,6,1,4,1,6141,2,400,1,2,7,1,7),_WwpOamEventLogWindowHi_Type())
wwpOamEventLogWindowHi.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpOamEventLogWindowHi.setStatus(_A)
_WwpOamEventLogWindowLo_Type=Unsigned32
_WwpOamEventLogWindowLo_Object=MibTableColumn
wwpOamEventLogWindowLo=_WwpOamEventLogWindowLo_Object((1,3,6,1,4,1,6141,2,400,1,2,7,1,8),_WwpOamEventLogWindowLo_Type())
wwpOamEventLogWindowLo.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpOamEventLogWindowLo.setStatus(_A)
_WwpOamEventLogThresholdHi_Type=Unsigned32
_WwpOamEventLogThresholdHi_Object=MibTableColumn
wwpOamEventLogThresholdHi=_WwpOamEventLogThresholdHi_Object((1,3,6,1,4,1,6141,2,400,1,2,7,1,9),_WwpOamEventLogThresholdHi_Type())
wwpOamEventLogThresholdHi.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpOamEventLogThresholdHi.setStatus(_A)
_WwpOamEventLogThresholdLo_Type=Unsigned32
_WwpOamEventLogThresholdLo_Object=MibTableColumn
wwpOamEventLogThresholdLo=_WwpOamEventLogThresholdLo_Object((1,3,6,1,4,1,6141,2,400,1,2,7,1,10),_WwpOamEventLogThresholdLo_Type())
wwpOamEventLogThresholdLo.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpOamEventLogThresholdLo.setStatus(_A)
_WwpOamEventLogValue_Type=Counter64
_WwpOamEventLogValue_Object=MibTableColumn
wwpOamEventLogValue=_WwpOamEventLogValue_Object((1,3,6,1,4,1,6141,2,400,1,2,7,1,11),_WwpOamEventLogValue_Type())
wwpOamEventLogValue.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpOamEventLogValue.setStatus(_A)
_WwpOamEventLogRunningTotal_Type=Counter64
_WwpOamEventLogRunningTotal_Object=MibTableColumn
wwpOamEventLogRunningTotal=_WwpOamEventLogRunningTotal_Object((1,3,6,1,4,1,6141,2,400,1,2,7,1,12),_WwpOamEventLogRunningTotal_Type())
wwpOamEventLogRunningTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpOamEventLogRunningTotal.setStatus(_A)
_WwpOamEventLogEventTotal_Type=Unsigned32
_WwpOamEventLogEventTotal_Object=MibTableColumn
wwpOamEventLogEventTotal=_WwpOamEventLogEventTotal_Object((1,3,6,1,4,1,6141,2,400,1,2,7,1,13),_WwpOamEventLogEventTotal_Type())
wwpOamEventLogEventTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpOamEventLogEventTotal.setStatus(_A)
_WwpOamEvents_ObjectIdentity=ObjectIdentity
wwpOamEvents=_WwpOamEvents_ObjectIdentity((1,3,6,1,4,1,6141,2,400,1,3))
_WwpOamEventsV2_ObjectIdentity=ObjectIdentity
wwpOamEventsV2=_WwpOamEventsV2_ObjectIdentity((1,3,6,1,4,1,6141,2,400,1,3,0))
mibBuilder.exportSymbols(_F,**{'wwpOamMibModule':wwpOamMibModule,'wwpOamMIB':wwpOamMIB,'wwpOamConf':wwpOamConf,'wwpOamGroups':wwpOamGroups,'wwpOamCompls':wwpOamCompls,'wwpOamObjs':wwpOamObjs,'wwpOamTable':wwpOamTable,'wwpOamEntry':wwpOamEntry,'wwpOamAdminState':wwpOamAdminState,'wwpOamOperStatus':wwpOamOperStatus,'wwpOamMode':wwpOamMode,'wwpMaxOamPduSize':wwpMaxOamPduSize,'wwpOamConfigRevision':wwpOamConfigRevision,'wwpOamFunctionsSupported':wwpOamFunctionsSupported,_L:wwpOamPort,'wwpOamPeerTable':wwpOamPeerTable,'wwpOamPeerEntry':wwpOamPeerEntry,'wwpOamPeerStatus':wwpOamPeerStatus,'wwpOamPeerMacAddress':wwpOamPeerMacAddress,'wwpOamPeerVendorOui':wwpOamPeerVendorOui,'wwpOamPeerVendorInfo':wwpOamPeerVendorInfo,'wwpOamPeerMode':wwpOamPeerMode,'wwpOamPeerMaxOamPduSize':wwpOamPeerMaxOamPduSize,'wwpOamPeerConfigRevision':wwpOamPeerConfigRevision,'wwpOamPeerFunctionsSupported':wwpOamPeerFunctionsSupported,_R:wwpOamLocalPort,'wwpOamLoopbackTable':wwpOamLoopbackTable,'wwpOamLoopbackEntry':wwpOamLoopbackEntry,'wwpOamLoopbackCommand':wwpOamLoopbackCommand,'wwpOamLoopbackStatus':wwpOamLoopbackStatus,'wwpOamLoopbackIgnoreRx':wwpOamLoopbackIgnoreRx,_T:wwpOamLoopbackPort,'wwpOamStatsTable':wwpOamStatsTable,'wwpOamStatsEntry':wwpOamStatsEntry,'wwpOamInformationTx':wwpOamInformationTx,'wwpOamInformationRx':wwpOamInformationRx,'wwpOamUniqueEventNotificationTx':wwpOamUniqueEventNotificationTx,'wwpOamUniqueEventNotificationRx':wwpOamUniqueEventNotificationRx,'wwpOamLoopbackControlTx':wwpOamLoopbackControlTx,'wwpOamLoopbackControlRx':wwpOamLoopbackControlRx,'wwpOamVariableRequestTx':wwpOamVariableRequestTx,'wwpOamVariableRequestRx':wwpOamVariableRequestRx,'wwpOamVariableResponseTx':wwpOamVariableResponseTx,'wwpOamVariableResponseRx':wwpOamVariableResponseRx,'wwpOamOrgSpecificTx':wwpOamOrgSpecificTx,'wwpOamOrgSpecificRx':wwpOamOrgSpecificRx,'wwpOamUnsupportedCodesTx':wwpOamUnsupportedCodesTx,'wwpOamUnsupportedCodesRx':wwpOamUnsupportedCodesRx,'wwpOamframesLostDueToOam':wwpOamframesLostDueToOam,_V:wwpOamStatsPort,'wwpOamDuplicateEventNotificationTx':wwpOamDuplicateEventNotificationTx,'wwpOamDuplicateEventNotificationRx':wwpOamDuplicateEventNotificationRx,'wwpOamSystemEnableDisable':wwpOamSystemEnableDisable,'wwpOamEventConfigTable':wwpOamEventConfigTable,'wwpOamEventConfigEntry':wwpOamEventConfigEntry,_W:wwpOamEventPort,'wwpOamErrFramePeriodWindow':wwpOamErrFramePeriodWindow,'wwpOamErrFramePeriodThreshold':wwpOamErrFramePeriodThreshold,'wwpOamErrFramePeriodEvNotifEnable':wwpOamErrFramePeriodEvNotifEnable,'wwpOamErrFrameWindow':wwpOamErrFrameWindow,'wwpOamErrFrameThreshold':wwpOamErrFrameThreshold,'wwpOamErrFrameEvNotifEnable':wwpOamErrFrameEvNotifEnable,'wwpOamErrFrameSecsSummaryWindow':wwpOamErrFrameSecsSummaryWindow,'wwpOamErrFrameSecsSummaryThreshold':wwpOamErrFrameSecsSummaryThreshold,'wwpOamErrFrameSecsEvNotifEnable':wwpOamErrFrameSecsEvNotifEnable,'wwpOamDyingGaspEnable':wwpOamDyingGaspEnable,'wwpOamCriticalEventEnable':wwpOamCriticalEventEnable,'wwpOamEventLogTable':wwpOamEventLogTable,'wwpOamEventLogEntry':wwpOamEventLogEntry,_Y:wwpOamEventLogPort,_Z:wwpOamEventLogIndex,'wwpOamEventLogTimestamp':wwpOamEventLogTimestamp,'wwpOamEventLogOui':wwpOamEventLogOui,'wwpOamEventLogType':wwpOamEventLogType,'wwpOamEventLogLocation':wwpOamEventLogLocation,'wwpOamEventLogWindowHi':wwpOamEventLogWindowHi,'wwpOamEventLogWindowLo':wwpOamEventLogWindowLo,'wwpOamEventLogThresholdHi':wwpOamEventLogThresholdHi,'wwpOamEventLogThresholdLo':wwpOamEventLogThresholdLo,'wwpOamEventLogValue':wwpOamEventLogValue,'wwpOamEventLogRunningTotal':wwpOamEventLogRunningTotal,'wwpOamEventLogEventTotal':wwpOamEventLogEventTotal,'wwpOamEvents':wwpOamEvents,'wwpOamEventsV2':wwpOamEventsV2})