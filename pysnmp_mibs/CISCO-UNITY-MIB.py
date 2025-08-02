_AA='ciscoUnityPortInfoGroup3'
_A9='ciscoUnityPortInfoGroup2'
_A8='ciscoUnityLicInfoGroup'
_A7='ciscoUnityMonitoredEvent'
_A6='ciscoUnityPortObjectId'
_A5='ciscoUnityPortActivity'
_A4='ciscoUnityLicUtilVMISubs'
_A3='ciscoUnityLicUtilSubs'
_A2='ciscoUnityLicUtilSecondServer'
_A1='ciscoUnityLicSecondServerIsLic'
_A0='ciscoUnityLicPrimaryServerIsLic'
_z='ciscoUnityLicVPIMIsLicensed'
_y='ciscoUnityLicPoolingIsEnabled'
_x='ciscoUnityLicMaxMsgRecLenIsLic'
_w='ciscoUnityLicAMISIsLicensed'
_v='ciscoUnityLicBridgeSessionsMax'
_u='ciscoUnityLicVoicePortsMax'
_t='ciscoUnityLicVMISubscribersMax'
_s='ciscoUnityLicUMSubscribersMax'
_r='ciscoUnityLicSubscribersMax'
_q='ciscoUnityLicTTSSessionsMax'
_p='ciscoUnityLicLanguagesMax'
_o='ciscoUnityPortTRAPConnection'
_n='ciscoUnityPortAMISDelivery'
_m='ciscoUnityPortDialoutMWI'
_l='ciscoUnityPortMessageNotif'
_k='ciscoUnityPortAnswerCalls'
_j='ciscoUnityPortEnabled'
_i='ciscoUnityPortExtension'
_h='ciscoUnityPortIntegration'
_g='ciscoUnityPortNumber'
_f='ciscoUnityPortsOutboundActive'
_e='ciscoUnityPortsOutbound'
_d='ciscoUnityPortsInboundActive'
_c='ciscoUnityPortsInbound'
_b='ciscoUnityPortsActive'
_a='ciscoUnityPorts'
_Z='ciscoUnityServerState'
_Y='ciscoUnityVersion'
_X='ciscoUnityName'
_W='ciscoUnityPortIndex'
_V='not-accessible'
_U='ciscoUnityIndex'
_T='Integer32'
_S='ciscoUnityPortInfoGroup'
_R='ciscoUnityNotificationsGroup'
_Q='ciscoUnityNotificationsInfoGroup'
_P='ciscoUnityInfoGroup'
_O='ciscoUnityEventEMSNotes'
_N='ciscoUnityEventDescription'
_M='ciscoUnityEventComputer'
_L='ciscoUnityEventUser'
_K='ciscoUnityEventDate'
_J='ciscoUnityEventId'
_I='ciscoUnityEventCategory'
_H='ciscoUnityEventSource'
_G='ciscoUnityEventType'
_F='SnmpAdminString'
_E='accessible-for-notify'
_D='Unsigned32'
_C='read-only'
_B='current'
_A='CISCO-UNITY-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_F)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_T,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention','TruthValue')
ciscoUnityMIB=ModuleIdentity((1,3,6,1,4,1,9,9,385))
if mibBuilder.loadTexts:ciscoUnityMIB.setRevisions(('2005-12-12 00:00','2004-01-06 00:00'))
class CiscoUnityIndex(TextualConvention,Unsigned32):status=_B;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
class CiscoUnityServerStatus(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('stopped',1),('starting',2),('running',3),('stopping',4)))
_CiscoUnityMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoUnityMIBNotifs=_CiscoUnityMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,385,0))
_CiscoUnityMIBObjects_ObjectIdentity=ObjectIdentity
ciscoUnityMIBObjects=_CiscoUnityMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,385,1))
_CiscoUnityGeneralInfo_ObjectIdentity=ObjectIdentity
ciscoUnityGeneralInfo=_CiscoUnityGeneralInfo_ObjectIdentity((1,3,6,1,4,1,9,9,385,1,1))
_CiscoUnityTable_Object=MibTable
ciscoUnityTable=_CiscoUnityTable_Object((1,3,6,1,4,1,9,9,385,1,1,1))
if mibBuilder.loadTexts:ciscoUnityTable.setStatus(_B)
_CiscoUnityEntry_Object=MibTableRow
ciscoUnityEntry=_CiscoUnityEntry_Object((1,3,6,1,4,1,9,9,385,1,1,1,1))
ciscoUnityEntry.setIndexNames((0,_A,_U))
if mibBuilder.loadTexts:ciscoUnityEntry.setStatus(_B)
_CiscoUnityIndex_Type=CiscoUnityIndex
_CiscoUnityIndex_Object=MibTableColumn
ciscoUnityIndex=_CiscoUnityIndex_Object((1,3,6,1,4,1,9,9,385,1,1,1,1,1),_CiscoUnityIndex_Type())
ciscoUnityIndex.setMaxAccess(_V)
if mibBuilder.loadTexts:ciscoUnityIndex.setStatus(_B)
_CiscoUnityName_Type=SnmpAdminString
_CiscoUnityName_Object=MibTableColumn
ciscoUnityName=_CiscoUnityName_Object((1,3,6,1,4,1,9,9,385,1,1,1,1,2),_CiscoUnityName_Type())
ciscoUnityName.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoUnityName.setStatus(_B)
class _CiscoUnityVersion_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_CiscoUnityVersion_Type.__name__=_F
_CiscoUnityVersion_Object=MibTableColumn
ciscoUnityVersion=_CiscoUnityVersion_Object((1,3,6,1,4,1,9,9,385,1,1,1,1,3),_CiscoUnityVersion_Type())
ciscoUnityVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoUnityVersion.setStatus(_B)
_CiscoUnityPortTable_Object=MibTable
ciscoUnityPortTable=_CiscoUnityPortTable_Object((1,3,6,1,4,1,9,9,385,1,1,2))
if mibBuilder.loadTexts:ciscoUnityPortTable.setStatus(_B)
_CiscoUnityPortEntry_Object=MibTableRow
ciscoUnityPortEntry=_CiscoUnityPortEntry_Object((1,3,6,1,4,1,9,9,385,1,1,2,1))
ciscoUnityPortEntry.setIndexNames((0,_A,_W))
if mibBuilder.loadTexts:ciscoUnityPortEntry.setStatus(_B)
_CiscoUnityPortIndex_Type=CiscoUnityIndex
_CiscoUnityPortIndex_Object=MibTableColumn
ciscoUnityPortIndex=_CiscoUnityPortIndex_Object((1,3,6,1,4,1,9,9,385,1,1,2,1,1),_CiscoUnityPortIndex_Type())
ciscoUnityPortIndex.setMaxAccess(_V)
if mibBuilder.loadTexts:ciscoUnityPortIndex.setStatus(_B)
class _CiscoUnityPortNumber_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CiscoUnityPortNumber_Type.__name__=_D
_CiscoUnityPortNumber_Object=MibTableColumn
ciscoUnityPortNumber=_CiscoUnityPortNumber_Object((1,3,6,1,4,1,9,9,385,1,1,2,1,2),_CiscoUnityPortNumber_Type())
ciscoUnityPortNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoUnityPortNumber.setStatus(_B)
class _CiscoUnityPortIntegration_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_CiscoUnityPortIntegration_Type.__name__=_F
_CiscoUnityPortIntegration_Object=MibTableColumn
ciscoUnityPortIntegration=_CiscoUnityPortIntegration_Object((1,3,6,1,4,1,9,9,385,1,1,2,1,3),_CiscoUnityPortIntegration_Type())
ciscoUnityPortIntegration.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoUnityPortIntegration.setStatus(_B)
class _CiscoUnityPortExtension_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_CiscoUnityPortExtension_Type.__name__=_F
_CiscoUnityPortExtension_Object=MibTableColumn
ciscoUnityPortExtension=_CiscoUnityPortExtension_Object((1,3,6,1,4,1,9,9,385,1,1,2,1,4),_CiscoUnityPortExtension_Type())
ciscoUnityPortExtension.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoUnityPortExtension.setStatus(_B)
_CiscoUnityPortEnabled_Type=TruthValue
_CiscoUnityPortEnabled_Object=MibTableColumn
ciscoUnityPortEnabled=_CiscoUnityPortEnabled_Object((1,3,6,1,4,1,9,9,385,1,1,2,1,5),_CiscoUnityPortEnabled_Type())
ciscoUnityPortEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoUnityPortEnabled.setStatus(_B)
_CiscoUnityPortAnswerCalls_Type=TruthValue
_CiscoUnityPortAnswerCalls_Object=MibTableColumn
ciscoUnityPortAnswerCalls=_CiscoUnityPortAnswerCalls_Object((1,3,6,1,4,1,9,9,385,1,1,2,1,6),_CiscoUnityPortAnswerCalls_Type())
ciscoUnityPortAnswerCalls.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoUnityPortAnswerCalls.setStatus(_B)
_CiscoUnityPortMessageNotif_Type=TruthValue
_CiscoUnityPortMessageNotif_Object=MibTableColumn
ciscoUnityPortMessageNotif=_CiscoUnityPortMessageNotif_Object((1,3,6,1,4,1,9,9,385,1,1,2,1,7),_CiscoUnityPortMessageNotif_Type())
ciscoUnityPortMessageNotif.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoUnityPortMessageNotif.setStatus(_B)
_CiscoUnityPortDialoutMWI_Type=TruthValue
_CiscoUnityPortDialoutMWI_Object=MibTableColumn
ciscoUnityPortDialoutMWI=_CiscoUnityPortDialoutMWI_Object((1,3,6,1,4,1,9,9,385,1,1,2,1,8),_CiscoUnityPortDialoutMWI_Type())
ciscoUnityPortDialoutMWI.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoUnityPortDialoutMWI.setStatus(_B)
_CiscoUnityPortAMISDelivery_Type=TruthValue
_CiscoUnityPortAMISDelivery_Object=MibTableColumn
ciscoUnityPortAMISDelivery=_CiscoUnityPortAMISDelivery_Object((1,3,6,1,4,1,9,9,385,1,1,2,1,9),_CiscoUnityPortAMISDelivery_Type())
ciscoUnityPortAMISDelivery.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoUnityPortAMISDelivery.setStatus(_B)
_CiscoUnityPortTRAPConnection_Type=TruthValue
_CiscoUnityPortTRAPConnection_Object=MibTableColumn
ciscoUnityPortTRAPConnection=_CiscoUnityPortTRAPConnection_Object((1,3,6,1,4,1,9,9,385,1,1,2,1,10),_CiscoUnityPortTRAPConnection_Type())
ciscoUnityPortTRAPConnection.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoUnityPortTRAPConnection.setStatus(_B)
_CiscoUnityPortActivity_Type=SnmpAdminString
_CiscoUnityPortActivity_Object=MibTableColumn
ciscoUnityPortActivity=_CiscoUnityPortActivity_Object((1,3,6,1,4,1,9,9,385,1,1,2,1,11),_CiscoUnityPortActivity_Type())
ciscoUnityPortActivity.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoUnityPortActivity.setStatus(_B)
class _CiscoUnityPortObjectId_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,38))
_CiscoUnityPortObjectId_Type.__name__=_F
_CiscoUnityPortObjectId_Object=MibTableColumn
ciscoUnityPortObjectId=_CiscoUnityPortObjectId_Object((1,3,6,1,4,1,9,9,385,1,1,2,1,12),_CiscoUnityPortObjectId_Type())
ciscoUnityPortObjectId.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoUnityPortObjectId.setStatus(_B)
_CiscoUnityGlobalInfo_ObjectIdentity=ObjectIdentity
ciscoUnityGlobalInfo=_CiscoUnityGlobalInfo_ObjectIdentity((1,3,6,1,4,1,9,9,385,1,2))
_CiscoUnityServerState_Type=CiscoUnityServerStatus
_CiscoUnityServerState_Object=MibScalar
ciscoUnityServerState=_CiscoUnityServerState_Object((1,3,6,1,4,1,9,9,385,1,2,1),_CiscoUnityServerState_Type())
ciscoUnityServerState.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoUnityServerState.setStatus(_B)
class _CiscoUnityPorts_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CiscoUnityPorts_Type.__name__=_D
_CiscoUnityPorts_Object=MibScalar
ciscoUnityPorts=_CiscoUnityPorts_Object((1,3,6,1,4,1,9,9,385,1,2,2),_CiscoUnityPorts_Type())
ciscoUnityPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoUnityPorts.setStatus(_B)
class _CiscoUnityPortsActive_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CiscoUnityPortsActive_Type.__name__=_D
_CiscoUnityPortsActive_Object=MibScalar
ciscoUnityPortsActive=_CiscoUnityPortsActive_Object((1,3,6,1,4,1,9,9,385,1,2,3),_CiscoUnityPortsActive_Type())
ciscoUnityPortsActive.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoUnityPortsActive.setStatus(_B)
class _CiscoUnityPortsInbound_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CiscoUnityPortsInbound_Type.__name__=_D
_CiscoUnityPortsInbound_Object=MibScalar
ciscoUnityPortsInbound=_CiscoUnityPortsInbound_Object((1,3,6,1,4,1,9,9,385,1,2,4),_CiscoUnityPortsInbound_Type())
ciscoUnityPortsInbound.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoUnityPortsInbound.setStatus(_B)
class _CiscoUnityPortsInboundActive_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CiscoUnityPortsInboundActive_Type.__name__=_D
_CiscoUnityPortsInboundActive_Object=MibScalar
ciscoUnityPortsInboundActive=_CiscoUnityPortsInboundActive_Object((1,3,6,1,4,1,9,9,385,1,2,5),_CiscoUnityPortsInboundActive_Type())
ciscoUnityPortsInboundActive.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoUnityPortsInboundActive.setStatus(_B)
class _CiscoUnityPortsOutbound_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CiscoUnityPortsOutbound_Type.__name__=_D
_CiscoUnityPortsOutbound_Object=MibScalar
ciscoUnityPortsOutbound=_CiscoUnityPortsOutbound_Object((1,3,6,1,4,1,9,9,385,1,2,6),_CiscoUnityPortsOutbound_Type())
ciscoUnityPortsOutbound.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoUnityPortsOutbound.setStatus(_B)
class _CiscoUnityPortsOutboundActive_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CiscoUnityPortsOutboundActive_Type.__name__=_D
_CiscoUnityPortsOutboundActive_Object=MibScalar
ciscoUnityPortsOutboundActive=_CiscoUnityPortsOutboundActive_Object((1,3,6,1,4,1,9,9,385,1,2,7),_CiscoUnityPortsOutboundActive_Type())
ciscoUnityPortsOutboundActive.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoUnityPortsOutboundActive.setStatus(_B)
class _CiscoUnityLicLanguagesMax_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CiscoUnityLicLanguagesMax_Type.__name__=_D
_CiscoUnityLicLanguagesMax_Object=MibScalar
ciscoUnityLicLanguagesMax=_CiscoUnityLicLanguagesMax_Object((1,3,6,1,4,1,9,9,385,1,2,8),_CiscoUnityLicLanguagesMax_Type())
ciscoUnityLicLanguagesMax.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoUnityLicLanguagesMax.setStatus(_B)
class _CiscoUnityLicTTSSessionsMax_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CiscoUnityLicTTSSessionsMax_Type.__name__=_D
_CiscoUnityLicTTSSessionsMax_Object=MibScalar
ciscoUnityLicTTSSessionsMax=_CiscoUnityLicTTSSessionsMax_Object((1,3,6,1,4,1,9,9,385,1,2,9),_CiscoUnityLicTTSSessionsMax_Type())
ciscoUnityLicTTSSessionsMax.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoUnityLicTTSSessionsMax.setStatus(_B)
class _CiscoUnityLicSubscribersMax_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CiscoUnityLicSubscribersMax_Type.__name__=_D
_CiscoUnityLicSubscribersMax_Object=MibScalar
ciscoUnityLicSubscribersMax=_CiscoUnityLicSubscribersMax_Object((1,3,6,1,4,1,9,9,385,1,2,10),_CiscoUnityLicSubscribersMax_Type())
ciscoUnityLicSubscribersMax.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoUnityLicSubscribersMax.setStatus(_B)
class _CiscoUnityLicUMSubscribersMax_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CiscoUnityLicUMSubscribersMax_Type.__name__=_D
_CiscoUnityLicUMSubscribersMax_Object=MibScalar
ciscoUnityLicUMSubscribersMax=_CiscoUnityLicUMSubscribersMax_Object((1,3,6,1,4,1,9,9,385,1,2,11),_CiscoUnityLicUMSubscribersMax_Type())
ciscoUnityLicUMSubscribersMax.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoUnityLicUMSubscribersMax.setStatus(_B)
class _CiscoUnityLicVMISubscribersMax_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CiscoUnityLicVMISubscribersMax_Type.__name__=_D
_CiscoUnityLicVMISubscribersMax_Object=MibScalar
ciscoUnityLicVMISubscribersMax=_CiscoUnityLicVMISubscribersMax_Object((1,3,6,1,4,1,9,9,385,1,2,12),_CiscoUnityLicVMISubscribersMax_Type())
ciscoUnityLicVMISubscribersMax.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoUnityLicVMISubscribersMax.setStatus(_B)
class _CiscoUnityLicVoicePortsMax_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CiscoUnityLicVoicePortsMax_Type.__name__=_D
_CiscoUnityLicVoicePortsMax_Object=MibScalar
ciscoUnityLicVoicePortsMax=_CiscoUnityLicVoicePortsMax_Object((1,3,6,1,4,1,9,9,385,1,2,13),_CiscoUnityLicVoicePortsMax_Type())
ciscoUnityLicVoicePortsMax.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoUnityLicVoicePortsMax.setStatus(_B)
class _CiscoUnityLicBridgeSessionsMax_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CiscoUnityLicBridgeSessionsMax_Type.__name__=_D
_CiscoUnityLicBridgeSessionsMax_Object=MibScalar
ciscoUnityLicBridgeSessionsMax=_CiscoUnityLicBridgeSessionsMax_Object((1,3,6,1,4,1,9,9,385,1,2,14),_CiscoUnityLicBridgeSessionsMax_Type())
ciscoUnityLicBridgeSessionsMax.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoUnityLicBridgeSessionsMax.setStatus(_B)
_CiscoUnityLicAMISIsLicensed_Type=TruthValue
_CiscoUnityLicAMISIsLicensed_Object=MibScalar
ciscoUnityLicAMISIsLicensed=_CiscoUnityLicAMISIsLicensed_Object((1,3,6,1,4,1,9,9,385,1,2,15),_CiscoUnityLicAMISIsLicensed_Type())
ciscoUnityLicAMISIsLicensed.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoUnityLicAMISIsLicensed.setStatus(_B)
_CiscoUnityLicMaxMsgRecLenIsLic_Type=TruthValue
_CiscoUnityLicMaxMsgRecLenIsLic_Object=MibScalar
ciscoUnityLicMaxMsgRecLenIsLic=_CiscoUnityLicMaxMsgRecLenIsLic_Object((1,3,6,1,4,1,9,9,385,1,2,16),_CiscoUnityLicMaxMsgRecLenIsLic_Type())
ciscoUnityLicMaxMsgRecLenIsLic.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoUnityLicMaxMsgRecLenIsLic.setStatus(_B)
_CiscoUnityLicPoolingIsEnabled_Type=TruthValue
_CiscoUnityLicPoolingIsEnabled_Object=MibScalar
ciscoUnityLicPoolingIsEnabled=_CiscoUnityLicPoolingIsEnabled_Object((1,3,6,1,4,1,9,9,385,1,2,17),_CiscoUnityLicPoolingIsEnabled_Type())
ciscoUnityLicPoolingIsEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoUnityLicPoolingIsEnabled.setStatus(_B)
_CiscoUnityLicVPIMIsLicensed_Type=TruthValue
_CiscoUnityLicVPIMIsLicensed_Object=MibScalar
ciscoUnityLicVPIMIsLicensed=_CiscoUnityLicVPIMIsLicensed_Object((1,3,6,1,4,1,9,9,385,1,2,18),_CiscoUnityLicVPIMIsLicensed_Type())
ciscoUnityLicVPIMIsLicensed.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoUnityLicVPIMIsLicensed.setStatus(_B)
_CiscoUnityLicPrimaryServerIsLic_Type=TruthValue
_CiscoUnityLicPrimaryServerIsLic_Object=MibScalar
ciscoUnityLicPrimaryServerIsLic=_CiscoUnityLicPrimaryServerIsLic_Object((1,3,6,1,4,1,9,9,385,1,2,19),_CiscoUnityLicPrimaryServerIsLic_Type())
ciscoUnityLicPrimaryServerIsLic.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoUnityLicPrimaryServerIsLic.setStatus(_B)
_CiscoUnityLicSecondServerIsLic_Type=TruthValue
_CiscoUnityLicSecondServerIsLic_Object=MibScalar
ciscoUnityLicSecondServerIsLic=_CiscoUnityLicSecondServerIsLic_Object((1,3,6,1,4,1,9,9,385,1,2,20),_CiscoUnityLicSecondServerIsLic_Type())
ciscoUnityLicSecondServerIsLic.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoUnityLicSecondServerIsLic.setStatus(_B)
class _CiscoUnityLicUtilSecondServer_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_CiscoUnityLicUtilSecondServer_Type.__name__=_D
_CiscoUnityLicUtilSecondServer_Object=MibScalar
ciscoUnityLicUtilSecondServer=_CiscoUnityLicUtilSecondServer_Object((1,3,6,1,4,1,9,9,385,1,2,21),_CiscoUnityLicUtilSecondServer_Type())
ciscoUnityLicUtilSecondServer.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoUnityLicUtilSecondServer.setStatus(_B)
class _CiscoUnityLicUtilSubs_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CiscoUnityLicUtilSubs_Type.__name__=_D
_CiscoUnityLicUtilSubs_Object=MibScalar
ciscoUnityLicUtilSubs=_CiscoUnityLicUtilSubs_Object((1,3,6,1,4,1,9,9,385,1,2,22),_CiscoUnityLicUtilSubs_Type())
ciscoUnityLicUtilSubs.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoUnityLicUtilSubs.setStatus(_B)
class _CiscoUnityLicUtilVMISubs_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CiscoUnityLicUtilVMISubs_Type.__name__=_D
_CiscoUnityLicUtilVMISubs_Object=MibScalar
ciscoUnityLicUtilVMISubs=_CiscoUnityLicUtilVMISubs_Object((1,3,6,1,4,1,9,9,385,1,2,23),_CiscoUnityLicUtilVMISubs_Type())
ciscoUnityLicUtilVMISubs.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoUnityLicUtilVMISubs.setStatus(_B)
_CiscoUnityNotificationsInfo_ObjectIdentity=ObjectIdentity
ciscoUnityNotificationsInfo=_CiscoUnityNotificationsInfo_ObjectIdentity((1,3,6,1,4,1,9,9,385,1,3))
class _CiscoUnityEventType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('error',1),('warning',2),('informational',3)))
_CiscoUnityEventType_Type.__name__=_T
_CiscoUnityEventType_Object=MibScalar
ciscoUnityEventType=_CiscoUnityEventType_Object((1,3,6,1,4,1,9,9,385,1,3,1),_CiscoUnityEventType_Type())
ciscoUnityEventType.setMaxAccess(_E)
if mibBuilder.loadTexts:ciscoUnityEventType.setStatus(_B)
_CiscoUnityEventSource_Type=SnmpAdminString
_CiscoUnityEventSource_Object=MibScalar
ciscoUnityEventSource=_CiscoUnityEventSource_Object((1,3,6,1,4,1,9,9,385,1,3,2),_CiscoUnityEventSource_Type())
ciscoUnityEventSource.setMaxAccess(_E)
if mibBuilder.loadTexts:ciscoUnityEventSource.setStatus(_B)
_CiscoUnityEventCategory_Type=SnmpAdminString
_CiscoUnityEventCategory_Object=MibScalar
ciscoUnityEventCategory=_CiscoUnityEventCategory_Object((1,3,6,1,4,1,9,9,385,1,3,3),_CiscoUnityEventCategory_Type())
ciscoUnityEventCategory.setMaxAccess(_E)
if mibBuilder.loadTexts:ciscoUnityEventCategory.setStatus(_B)
class _CiscoUnityEventId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CiscoUnityEventId_Type.__name__=_D
_CiscoUnityEventId_Object=MibScalar
ciscoUnityEventId=_CiscoUnityEventId_Object((1,3,6,1,4,1,9,9,385,1,3,4),_CiscoUnityEventId_Type())
ciscoUnityEventId.setMaxAccess(_E)
if mibBuilder.loadTexts:ciscoUnityEventId.setStatus(_B)
_CiscoUnityEventDate_Type=DateAndTime
_CiscoUnityEventDate_Object=MibScalar
ciscoUnityEventDate=_CiscoUnityEventDate_Object((1,3,6,1,4,1,9,9,385,1,3,5),_CiscoUnityEventDate_Type())
ciscoUnityEventDate.setMaxAccess(_E)
if mibBuilder.loadTexts:ciscoUnityEventDate.setStatus(_B)
_CiscoUnityEventUser_Type=SnmpAdminString
_CiscoUnityEventUser_Object=MibScalar
ciscoUnityEventUser=_CiscoUnityEventUser_Object((1,3,6,1,4,1,9,9,385,1,3,6),_CiscoUnityEventUser_Type())
ciscoUnityEventUser.setMaxAccess(_E)
if mibBuilder.loadTexts:ciscoUnityEventUser.setStatus(_B)
_CiscoUnityEventComputer_Type=SnmpAdminString
_CiscoUnityEventComputer_Object=MibScalar
ciscoUnityEventComputer=_CiscoUnityEventComputer_Object((1,3,6,1,4,1,9,9,385,1,3,7),_CiscoUnityEventComputer_Type())
ciscoUnityEventComputer.setMaxAccess(_E)
if mibBuilder.loadTexts:ciscoUnityEventComputer.setStatus(_B)
_CiscoUnityEventDescription_Type=SnmpAdminString
_CiscoUnityEventDescription_Object=MibScalar
ciscoUnityEventDescription=_CiscoUnityEventDescription_Object((1,3,6,1,4,1,9,9,385,1,3,8),_CiscoUnityEventDescription_Type())
ciscoUnityEventDescription.setMaxAccess(_E)
if mibBuilder.loadTexts:ciscoUnityEventDescription.setStatus(_B)
_CiscoUnityEventEMSNotes_Type=SnmpAdminString
_CiscoUnityEventEMSNotes_Object=MibScalar
ciscoUnityEventEMSNotes=_CiscoUnityEventEMSNotes_Object((1,3,6,1,4,1,9,9,385,1,3,9),_CiscoUnityEventEMSNotes_Type())
ciscoUnityEventEMSNotes.setMaxAccess(_E)
if mibBuilder.loadTexts:ciscoUnityEventEMSNotes.setStatus(_B)
_CiscoUnityMIBConform_ObjectIdentity=ObjectIdentity
ciscoUnityMIBConform=_CiscoUnityMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,385,2))
_CiscoUnityMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoUnityMIBCompliances=_CiscoUnityMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,385,2,1))
_CiscoUnityMIBGroups_ObjectIdentity=ObjectIdentity
ciscoUnityMIBGroups=_CiscoUnityMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,385,2,2))
ciscoUnityInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,385,2,2,1))
ciscoUnityInfoGroup.setObjects(*((_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f)))
if mibBuilder.loadTexts:ciscoUnityInfoGroup.setStatus(_B)
ciscoUnityPortInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,385,2,2,2))
ciscoUnityPortInfoGroup.setObjects(*((_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o)))
if mibBuilder.loadTexts:ciscoUnityPortInfoGroup.setStatus(_B)
ciscoUnityNotificationsInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,385,2,2,3))
ciscoUnityNotificationsInfoGroup.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:ciscoUnityNotificationsInfoGroup.setStatus(_B)
ciscoUnityLicInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,385,2,2,5))
ciscoUnityLicInfoGroup.setObjects(*((_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4)))
if mibBuilder.loadTexts:ciscoUnityLicInfoGroup.setStatus(_B)
ciscoUnityPortInfoGroup2=ObjectGroup((1,3,6,1,4,1,9,9,385,2,2,6))
ciscoUnityPortInfoGroup2.setObjects((_A,_A5))
if mibBuilder.loadTexts:ciscoUnityPortInfoGroup2.setStatus(_B)
ciscoUnityPortInfoGroup3=ObjectGroup((1,3,6,1,4,1,9,9,385,2,2,7))
ciscoUnityPortInfoGroup3.setObjects((_A,_A6))
if mibBuilder.loadTexts:ciscoUnityPortInfoGroup3.setStatus(_B)
ciscoUnityMonitoredEvent=NotificationType((1,3,6,1,4,1,9,9,385,0,1))
ciscoUnityMonitoredEvent.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:ciscoUnityMonitoredEvent.setStatus(_B)
ciscoUnityNotificationsGroup=NotificationGroup((1,3,6,1,4,1,9,9,385,2,2,4))
ciscoUnityNotificationsGroup.setObjects((_A,_A7))
if mibBuilder.loadTexts:ciscoUnityNotificationsGroup.setStatus(_B)
ciscoUnityMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,385,2,1,1))
ciscoUnityMIBCompliance.setObjects(*((_A,_P),(_A,_Q),(_A,_R),(_A,_S)))
if mibBuilder.loadTexts:ciscoUnityMIBCompliance.setStatus('deprecated')
ciscoUnityMIBComplianceRev1=ModuleCompliance((1,3,6,1,4,1,9,9,385,2,1,2))
ciscoUnityMIBComplianceRev1.setObjects(*((_A,_P),(_A,_Q),(_A,_R),(_A,_A8),(_A,_S),(_A,_A9),(_A,_AA)))
if mibBuilder.loadTexts:ciscoUnityMIBComplianceRev1.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'CiscoUnityIndex':CiscoUnityIndex,'CiscoUnityServerStatus':CiscoUnityServerStatus,'ciscoUnityMIB':ciscoUnityMIB,'ciscoUnityMIBNotifs':ciscoUnityMIBNotifs,_A7:ciscoUnityMonitoredEvent,'ciscoUnityMIBObjects':ciscoUnityMIBObjects,'ciscoUnityGeneralInfo':ciscoUnityGeneralInfo,'ciscoUnityTable':ciscoUnityTable,'ciscoUnityEntry':ciscoUnityEntry,_U:ciscoUnityIndex,_X:ciscoUnityName,_Y:ciscoUnityVersion,'ciscoUnityPortTable':ciscoUnityPortTable,'ciscoUnityPortEntry':ciscoUnityPortEntry,_W:ciscoUnityPortIndex,_g:ciscoUnityPortNumber,_h:ciscoUnityPortIntegration,_i:ciscoUnityPortExtension,_j:ciscoUnityPortEnabled,_k:ciscoUnityPortAnswerCalls,_l:ciscoUnityPortMessageNotif,_m:ciscoUnityPortDialoutMWI,_n:ciscoUnityPortAMISDelivery,_o:ciscoUnityPortTRAPConnection,_A5:ciscoUnityPortActivity,_A6:ciscoUnityPortObjectId,'ciscoUnityGlobalInfo':ciscoUnityGlobalInfo,_Z:ciscoUnityServerState,_a:ciscoUnityPorts,_b:ciscoUnityPortsActive,_c:ciscoUnityPortsInbound,_d:ciscoUnityPortsInboundActive,_e:ciscoUnityPortsOutbound,_f:ciscoUnityPortsOutboundActive,_p:ciscoUnityLicLanguagesMax,_q:ciscoUnityLicTTSSessionsMax,_r:ciscoUnityLicSubscribersMax,_s:ciscoUnityLicUMSubscribersMax,_t:ciscoUnityLicVMISubscribersMax,_u:ciscoUnityLicVoicePortsMax,_v:ciscoUnityLicBridgeSessionsMax,_w:ciscoUnityLicAMISIsLicensed,_x:ciscoUnityLicMaxMsgRecLenIsLic,_y:ciscoUnityLicPoolingIsEnabled,_z:ciscoUnityLicVPIMIsLicensed,_A0:ciscoUnityLicPrimaryServerIsLic,_A1:ciscoUnityLicSecondServerIsLic,_A2:ciscoUnityLicUtilSecondServer,_A3:ciscoUnityLicUtilSubs,_A4:ciscoUnityLicUtilVMISubs,'ciscoUnityNotificationsInfo':ciscoUnityNotificationsInfo,_G:ciscoUnityEventType,_H:ciscoUnityEventSource,_I:ciscoUnityEventCategory,_J:ciscoUnityEventId,_K:ciscoUnityEventDate,_L:ciscoUnityEventUser,_M:ciscoUnityEventComputer,_N:ciscoUnityEventDescription,_O:ciscoUnityEventEMSNotes,'ciscoUnityMIBConform':ciscoUnityMIBConform,'ciscoUnityMIBCompliances':ciscoUnityMIBCompliances,'ciscoUnityMIBCompliance':ciscoUnityMIBCompliance,'ciscoUnityMIBComplianceRev1':ciscoUnityMIBComplianceRev1,'ciscoUnityMIBGroups':ciscoUnityMIBGroups,_P:ciscoUnityInfoGroup,_S:ciscoUnityPortInfoGroup,_Q:ciscoUnityNotificationsInfoGroup,_R:ciscoUnityNotificationsGroup,_A8:ciscoUnityLicInfoGroup,_A9:ciscoUnityPortInfoGroup2,_AA:ciscoUnityPortInfoGroup3})