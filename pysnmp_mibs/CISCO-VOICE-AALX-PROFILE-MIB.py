_AV='cvapCodecConfigGroupRev1'
_AU='cvapCodecConfigGroup'
_AT='cvapCodecConfigNewJtrNomDelay'
_AS='cvapSvcResyncExpiries'
_AR='cvapSvcRestartExpiries'
_AQ='cvapSvcConnAckExpiries'
_AP='cvapSvcConnExpiries'
_AO='cvapSvcReleasExpiries'
_AN='cvapSvcCallProcExpiries'
_AM='cvapSvcRxBulkResyncs'
_AL='cvapSvcTxBulkResyncs'
_AK='cvapSvcRxResyncEndAcks'
_AJ='cvapSvcRxResyncEnds'
_AI='cvapSvcTxResyncEndAcks'
_AH='cvapSvcTxResyncEnds'
_AG='cvapSvcRxResyncStrtAcks'
_AF='cvapSvcRxResyncStrts'
_AE='cvapSvcTxResyncStrtAcks'
_AD='cvapSvcTxResyncStrts'
_AC='cvapSvcRxRestartAcks'
_AB='cvapSvcRxRestarts'
_AA='cvapSvcTxRestartAcks'
_A9='cvapSvcTxRestarts'
_A8='cvapSvcRxReleaseCompls'
_A7='cvapSvcRxReleases'
_A6='cvapSvcTxReleaseCompls'
_A5='cvapSvcTxReleases'
_A4='cvapSvcRxConnAcks'
_A3='cvapSvcRxConns'
_A2='cvapSvcTxConnAcks'
_A1='cvapSvcTxConns'
_A0='cvapSvcRxCallProcs'
_z='cvapSvcTxCallProcs'
_y='cvapSvcRxSetups'
_x='cvapSvcTxSetups'
_w='cvapSvcMultiCIDGlareThreshold'
_v='cvapSvcMultiCIDTerminatDelTimer'
_u='cvapSvcMultiCIDOriginatDelTimer'
_t='cvapSvcMultiCIDCACPCR'
_s='cvapSvcMultiCIDCACSCR'
_r='cvapSvcMultiCIDFillTimer'
_q='cvapSvcMultiCIDPerSvc'
_p='cvapSvcDelNotifGuardTimer'
_o='cvapSvcH248SelectorByteValue'
_n='cvapSvcMgcpSelectorByteValue'
_m='cvapSvcPartialFillSupported'
_l='cvapSvcAggLinkState'
_k='cvapSvcAggTrafficClipping'
_j='cvapSvcAal2CidNumber'
_i='cvapSvcTrfScalingFactor'
_h='cvapSvcAtmQosClr'
_g='cvapSvcAtmQosCtd'
_f='cvapSvcAtmQosCellDelay'
_e='cvapCodecConfigJitterNomDelay'
_d='cvapCodecConfigVbdPacketPeriod'
_c='Cells per Second'
_b='cvapCodecConfigType'
_a='cvapCodecConfigAdaptType'
_Z='cvapCodecNegotiationAdaptType'
_Y='CCallControlJitterDelayMode'
_X='cvapSvcStatsGroup'
_W='cvapSvcConfigGroup'
_V='cvapCodecConfigPayloadType'
_U='cvapCodecConfigDtmfRelay'
_T='cvapCodecConfigJitterMinDelay'
_S='cvapCodecConfigJitterMaxDelay'
_R='cvapCodecConfigJitterDelayMode'
_Q='cvapCodecConfigVoicePacketPeriod'
_P='cvapCodecConfigPreference'
_O='cvapCodecNegotiationOption'
_N='seconds'
_M='not-accessible'
_L='TruthValue'
_K='deprecated'
_J='microseconds'
_I='milliseconds'
_H='cmgwIndex'
_G='CISCO-MEDIA-GATEWAY-MIB'
_F='Unsigned32'
_E='Integer32'
_D='read-write'
_C='read-only'
_B='current'
_A='CISCO-VOICE-AALX-PROFILE-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
CCallControlJitterDelayMode,cmgwIndex=mibBuilder.importSymbols(_G,_Y,_H)
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CvcSpeechCoderRate,=mibBuilder.importSymbols('CISCO-VOICE-COMMON-DIAL-CONTROL-MIB','CvcSpeechCoderRate')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_L)
ciscoVoiceAalxProfileMIB=ModuleIdentity((1,3,6,1,4,1,9,9,323))
if mibBuilder.loadTexts:ciscoVoiceAalxProfileMIB.setRevisions(('2005-04-21 00:00','2004-10-15 00:00','2003-07-18 00:00'))
class CiscoAal2ProfileType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('itu',1),('custom',2)))
class CiscoAal2ProfileNumber(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,7,8,12,100,101,110,200,210)));namedValues=NamedValues(*(('profileITU1',1),('profileITU2',2),('profileITU3',3),('profileITU7',7),('profileITU8',8),('profileITU12',12),('profileCustom100',100),('profileCustom101',101),('profileCustom110',110),('profileCustom200',200),('profileCustom210',210)))
class CiscoCodecPacketPeriod(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)));namedValues=NamedValues(*(('pktPeriod5000us',1),('pktPeriod5500us',2),('pktPeriod5785us',3),('pktPeriod10000us',4),('pktPeriod15000us',5),('pktPeriod20000us',6),('pktPeriod25000us',7),('pktPeriod30000us',8),('pktPeriod35000us',9),('pktPeriod40000us',10),('pktPeriod45000us',11),('pktPeriod50000us',12),('pktPeriod55000us',13),('pktPeriod60000us',14),('pktPeriod65000us',15),('pktPeriod70000us',16),('pktPeriod75000us',17),('pktPeriod80000us',18),('pktPeriod85000us',19),('pktPeriod90000us',20)))
_CiscoVoiceAalxProfileMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoVoiceAalxProfileMIBNotifs=_CiscoVoiceAalxProfileMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,323,0))
_CiscoVoiceAalxProfileMIBObjects_ObjectIdentity=ObjectIdentity
ciscoVoiceAalxProfileMIBObjects=_CiscoVoiceAalxProfileMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,323,1))
_CvapCodecConfig_ObjectIdentity=ObjectIdentity
cvapCodecConfig=_CvapCodecConfig_ObjectIdentity((1,3,6,1,4,1,9,9,323,1,1))
_CvapCodecTable_Object=MibTable
cvapCodecTable=_CvapCodecTable_Object((1,3,6,1,4,1,9,9,323,1,1,1))
if mibBuilder.loadTexts:cvapCodecTable.setStatus(_B)
_CvapCodecEntry_Object=MibTableRow
cvapCodecEntry=_CvapCodecEntry_Object((1,3,6,1,4,1,9,9,323,1,1,1,1))
cvapCodecEntry.setIndexNames((0,_G,_H),(0,_A,_Z))
if mibBuilder.loadTexts:cvapCodecEntry.setStatus(_B)
class _CvapCodecNegotiationAdaptType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('aal5',1),('aal1',2)))
_CvapCodecNegotiationAdaptType_Type.__name__=_E
_CvapCodecNegotiationAdaptType_Object=MibTableColumn
cvapCodecNegotiationAdaptType=_CvapCodecNegotiationAdaptType_Object((1,3,6,1,4,1,9,9,323,1,1,1,1,1),_CvapCodecNegotiationAdaptType_Type())
cvapCodecNegotiationAdaptType.setMaxAccess(_M)
if mibBuilder.loadTexts:cvapCodecNegotiationAdaptType.setStatus(_B)
class _CvapCodecNegotiationOption_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('lcoRcdLcl',1),('lcoLclRcd',2),('rcdLcoLcl',3),('rcdLclLco',4),('lclLcoRcd',5),('lclRcdLco',6)))
_CvapCodecNegotiationOption_Type.__name__=_E
_CvapCodecNegotiationOption_Object=MibTableColumn
cvapCodecNegotiationOption=_CvapCodecNegotiationOption_Object((1,3,6,1,4,1,9,9,323,1,1,1,1,2),_CvapCodecNegotiationOption_Type())
cvapCodecNegotiationOption.setMaxAccess(_D)
if mibBuilder.loadTexts:cvapCodecNegotiationOption.setStatus(_B)
_CvapCodecConfigTable_Object=MibTable
cvapCodecConfigTable=_CvapCodecConfigTable_Object((1,3,6,1,4,1,9,9,323,1,1,2))
if mibBuilder.loadTexts:cvapCodecConfigTable.setStatus(_B)
_CvapCodecConfigEntry_Object=MibTableRow
cvapCodecConfigEntry=_CvapCodecConfigEntry_Object((1,3,6,1,4,1,9,9,323,1,1,2,1))
cvapCodecConfigEntry.setIndexNames((0,_G,_H),(0,_A,_a),(0,_A,_b))
if mibBuilder.loadTexts:cvapCodecConfigEntry.setStatus(_B)
class _CvapCodecConfigAdaptType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('other',1),('aal5',2),('aal1',3),('aal2',4)))
_CvapCodecConfigAdaptType_Type.__name__=_E
_CvapCodecConfigAdaptType_Object=MibTableColumn
cvapCodecConfigAdaptType=_CvapCodecConfigAdaptType_Object((1,3,6,1,4,1,9,9,323,1,1,2,1,1),_CvapCodecConfigAdaptType_Type())
cvapCodecConfigAdaptType.setMaxAccess(_M)
if mibBuilder.loadTexts:cvapCodecConfigAdaptType.setStatus(_B)
_CvapCodecConfigType_Type=CvcSpeechCoderRate
_CvapCodecConfigType_Object=MibTableColumn
cvapCodecConfigType=_CvapCodecConfigType_Object((1,3,6,1,4,1,9,9,323,1,1,2,1,2),_CvapCodecConfigType_Type())
cvapCodecConfigType.setMaxAccess(_M)
if mibBuilder.loadTexts:cvapCodecConfigType.setStatus(_B)
class _CvapCodecConfigPreference_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CvapCodecConfigPreference_Type.__name__=_F
_CvapCodecConfigPreference_Object=MibTableColumn
cvapCodecConfigPreference=_CvapCodecConfigPreference_Object((1,3,6,1,4,1,9,9,323,1,1,2,1,3),_CvapCodecConfigPreference_Type())
cvapCodecConfigPreference.setMaxAccess(_D)
if mibBuilder.loadTexts:cvapCodecConfigPreference.setStatus(_B)
_CvapCodecConfigVoicePacketPeriod_Type=CiscoCodecPacketPeriod
_CvapCodecConfigVoicePacketPeriod_Object=MibTableColumn
cvapCodecConfigVoicePacketPeriod=_CvapCodecConfigVoicePacketPeriod_Object((1,3,6,1,4,1,9,9,323,1,1,2,1,4),_CvapCodecConfigVoicePacketPeriod_Type())
cvapCodecConfigVoicePacketPeriod.setMaxAccess(_D)
if mibBuilder.loadTexts:cvapCodecConfigVoicePacketPeriod.setStatus(_B)
if mibBuilder.loadTexts:cvapCodecConfigVoicePacketPeriod.setUnits(_J)
_CvapCodecConfigVbdPacketPeriod_Type=CiscoCodecPacketPeriod
_CvapCodecConfigVbdPacketPeriod_Object=MibTableColumn
cvapCodecConfigVbdPacketPeriod=_CvapCodecConfigVbdPacketPeriod_Object((1,3,6,1,4,1,9,9,323,1,1,2,1,5),_CvapCodecConfigVbdPacketPeriod_Type())
cvapCodecConfigVbdPacketPeriod.setMaxAccess(_D)
if mibBuilder.loadTexts:cvapCodecConfigVbdPacketPeriod.setStatus(_K)
if mibBuilder.loadTexts:cvapCodecConfigVbdPacketPeriod.setUnits(_J)
class _CvapCodecConfigJitterDelayMode_Type(CCallControlJitterDelayMode):defaultValue=1
_CvapCodecConfigJitterDelayMode_Type.__name__=_Y
_CvapCodecConfigJitterDelayMode_Object=MibTableColumn
cvapCodecConfigJitterDelayMode=_CvapCodecConfigJitterDelayMode_Object((1,3,6,1,4,1,9,9,323,1,1,2,1,6),_CvapCodecConfigJitterDelayMode_Type())
cvapCodecConfigJitterDelayMode.setMaxAccess(_D)
if mibBuilder.loadTexts:cvapCodecConfigJitterDelayMode.setStatus(_B)
class _CvapCodecConfigJitterMaxDelay_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(20,500))
_CvapCodecConfigJitterMaxDelay_Type.__name__=_F
_CvapCodecConfigJitterMaxDelay_Object=MibTableColumn
cvapCodecConfigJitterMaxDelay=_CvapCodecConfigJitterMaxDelay_Object((1,3,6,1,4,1,9,9,323,1,1,2,1,7),_CvapCodecConfigJitterMaxDelay_Type())
cvapCodecConfigJitterMaxDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:cvapCodecConfigJitterMaxDelay.setStatus(_B)
if mibBuilder.loadTexts:cvapCodecConfigJitterMaxDelay.setUnits(_I)
class _CvapCodecConfigJitterNomDelay_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,500))
_CvapCodecConfigJitterNomDelay_Type.__name__=_F
_CvapCodecConfigJitterNomDelay_Object=MibTableColumn
cvapCodecConfigJitterNomDelay=_CvapCodecConfigJitterNomDelay_Object((1,3,6,1,4,1,9,9,323,1,1,2,1,8),_CvapCodecConfigJitterNomDelay_Type())
cvapCodecConfigJitterNomDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:cvapCodecConfigJitterNomDelay.setStatus(_K)
if mibBuilder.loadTexts:cvapCodecConfigJitterNomDelay.setUnits(_I)
class _CvapCodecConfigJitterMinDelay_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,500))
_CvapCodecConfigJitterMinDelay_Type.__name__=_F
_CvapCodecConfigJitterMinDelay_Object=MibTableColumn
cvapCodecConfigJitterMinDelay=_CvapCodecConfigJitterMinDelay_Object((1,3,6,1,4,1,9,9,323,1,1,2,1,9),_CvapCodecConfigJitterMinDelay_Type())
cvapCodecConfigJitterMinDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:cvapCodecConfigJitterMinDelay.setStatus(_B)
if mibBuilder.loadTexts:cvapCodecConfigJitterMinDelay.setUnits(_I)
_CvapCodecConfigDtmfRelay_Type=TruthValue
_CvapCodecConfigDtmfRelay_Object=MibTableColumn
cvapCodecConfigDtmfRelay=_CvapCodecConfigDtmfRelay_Object((1,3,6,1,4,1,9,9,323,1,1,2,1,10),_CvapCodecConfigDtmfRelay_Type())
cvapCodecConfigDtmfRelay.setMaxAccess(_D)
if mibBuilder.loadTexts:cvapCodecConfigDtmfRelay.setStatus(_B)
class _CvapCodecConfigPayloadType_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_CvapCodecConfigPayloadType_Type.__name__=_F
_CvapCodecConfigPayloadType_Object=MibTableColumn
cvapCodecConfigPayloadType=_CvapCodecConfigPayloadType_Object((1,3,6,1,4,1,9,9,323,1,1,2,1,11),_CvapCodecConfigPayloadType_Type())
cvapCodecConfigPayloadType.setMaxAccess(_D)
if mibBuilder.loadTexts:cvapCodecConfigPayloadType.setStatus(_B)
class _CvapCodecConfigNewJtrNomDelay_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,500))
_CvapCodecConfigNewJtrNomDelay_Type.__name__=_F
_CvapCodecConfigNewJtrNomDelay_Object=MibTableColumn
cvapCodecConfigNewJtrNomDelay=_CvapCodecConfigNewJtrNomDelay_Object((1,3,6,1,4,1,9,9,323,1,1,2,1,12),_CvapCodecConfigNewJtrNomDelay_Type())
cvapCodecConfigNewJtrNomDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:cvapCodecConfigNewJtrNomDelay.setStatus(_B)
if mibBuilder.loadTexts:cvapCodecConfigNewJtrNomDelay.setUnits(_I)
_CvapAal2Config_ObjectIdentity=ObjectIdentity
cvapAal2Config=_CvapAal2Config_ObjectIdentity((1,3,6,1,4,1,9,9,323,1,2))
_CvapSvcConfig_ObjectIdentity=ObjectIdentity
cvapSvcConfig=_CvapSvcConfig_ObjectIdentity((1,3,6,1,4,1,9,9,323,1,3))
_CvapSvcConfigTable_Object=MibTable
cvapSvcConfigTable=_CvapSvcConfigTable_Object((1,3,6,1,4,1,9,9,323,1,3,1))
if mibBuilder.loadTexts:cvapSvcConfigTable.setStatus(_B)
_CvapSvcConfigEntry_Object=MibTableRow
cvapSvcConfigEntry=_CvapSvcConfigEntry_Object((1,3,6,1,4,1,9,9,323,1,3,1,1))
cvapSvcConfigEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:cvapSvcConfigEntry.setStatus(_B)
class _CvapSvcAtmQosCellDelay_Type(Integer32):defaultValue=20000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(500,20000))
_CvapSvcAtmQosCellDelay_Type.__name__=_E
_CvapSvcAtmQosCellDelay_Object=MibTableColumn
cvapSvcAtmQosCellDelay=_CvapSvcAtmQosCellDelay_Object((1,3,6,1,4,1,9,9,323,1,3,1,1,1),_CvapSvcAtmQosCellDelay_Type())
cvapSvcAtmQosCellDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:cvapSvcAtmQosCellDelay.setStatus(_B)
if mibBuilder.loadTexts:cvapSvcAtmQosCellDelay.setUnits(_J)
class _CvapSvcAtmQosCtd_Type(Integer32):defaultValue=150000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(20000,150000))
_CvapSvcAtmQosCtd_Type.__name__=_E
_CvapSvcAtmQosCtd_Object=MibTableColumn
cvapSvcAtmQosCtd=_CvapSvcAtmQosCtd_Object((1,3,6,1,4,1,9,9,323,1,3,1,1,2),_CvapSvcAtmQosCtd_Type())
cvapSvcAtmQosCtd.setMaxAccess(_D)
if mibBuilder.loadTexts:cvapSvcAtmQosCtd.setStatus(_B)
if mibBuilder.loadTexts:cvapSvcAtmQosCtd.setUnits(_J)
class _CvapSvcAtmQosClr_Type(Integer32):defaultValue=8;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,8))
_CvapSvcAtmQosClr_Type.__name__=_E
_CvapSvcAtmQosClr_Object=MibTableColumn
cvapSvcAtmQosClr=_CvapSvcAtmQosClr_Object((1,3,6,1,4,1,9,9,323,1,3,1,1,3),_CvapSvcAtmQosClr_Type())
cvapSvcAtmQosClr.setMaxAccess(_D)
if mibBuilder.loadTexts:cvapSvcAtmQosClr.setStatus(_B)
class _CvapSvcTrfScalingFactor_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(50,200))
_CvapSvcTrfScalingFactor_Type.__name__=_E
_CvapSvcTrfScalingFactor_Object=MibTableColumn
cvapSvcTrfScalingFactor=_CvapSvcTrfScalingFactor_Object((1,3,6,1,4,1,9,9,323,1,3,1,1,4),_CvapSvcTrfScalingFactor_Type())
cvapSvcTrfScalingFactor.setMaxAccess(_D)
if mibBuilder.loadTexts:cvapSvcTrfScalingFactor.setStatus(_B)
class _CvapSvcAal2CidNumber_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(8,255))
_CvapSvcAal2CidNumber_Type.__name__=_E
_CvapSvcAal2CidNumber_Object=MibTableColumn
cvapSvcAal2CidNumber=_CvapSvcAal2CidNumber_Object((1,3,6,1,4,1,9,9,323,1,3,1,1,5),_CvapSvcAal2CidNumber_Type())
cvapSvcAal2CidNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:cvapSvcAal2CidNumber.setStatus(_B)
class _CvapSvcAggTrafficClipping_Type(TruthValue):defaultValue=1
_CvapSvcAggTrafficClipping_Type.__name__=_L
_CvapSvcAggTrafficClipping_Object=MibTableColumn
cvapSvcAggTrafficClipping=_CvapSvcAggTrafficClipping_Object((1,3,6,1,4,1,9,9,323,1,3,1,1,6),_CvapSvcAggTrafficClipping_Type())
cvapSvcAggTrafficClipping.setMaxAccess(_D)
if mibBuilder.loadTexts:cvapSvcAggTrafficClipping.setStatus(_B)
class _CvapSvcAggLinkState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_CvapSvcAggLinkState_Type.__name__=_E
_CvapSvcAggLinkState_Object=MibTableColumn
cvapSvcAggLinkState=_CvapSvcAggLinkState_Object((1,3,6,1,4,1,9,9,323,1,3,1,1,7),_CvapSvcAggLinkState_Type())
cvapSvcAggLinkState.setMaxAccess(_C)
if mibBuilder.loadTexts:cvapSvcAggLinkState.setStatus(_B)
class _CvapSvcPartialFillSupported_Type(Integer32):defaultValue=47;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,48))
_CvapSvcPartialFillSupported_Type.__name__=_E
_CvapSvcPartialFillSupported_Object=MibTableColumn
cvapSvcPartialFillSupported=_CvapSvcPartialFillSupported_Object((1,3,6,1,4,1,9,9,323,1,3,1,1,8),_CvapSvcPartialFillSupported_Type())
cvapSvcPartialFillSupported.setMaxAccess(_D)
if mibBuilder.loadTexts:cvapSvcPartialFillSupported.setStatus(_B)
class _CvapSvcMgcpSelectorByteValue_Type(Integer32):defaultValue=21;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_CvapSvcMgcpSelectorByteValue_Type.__name__=_E
_CvapSvcMgcpSelectorByteValue_Object=MibTableColumn
cvapSvcMgcpSelectorByteValue=_CvapSvcMgcpSelectorByteValue_Object((1,3,6,1,4,1,9,9,323,1,3,1,1,9),_CvapSvcMgcpSelectorByteValue_Type())
cvapSvcMgcpSelectorByteValue.setMaxAccess(_D)
if mibBuilder.loadTexts:cvapSvcMgcpSelectorByteValue.setStatus(_B)
class _CvapSvcH248SelectorByteValue_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_CvapSvcH248SelectorByteValue_Type.__name__=_E
_CvapSvcH248SelectorByteValue_Object=MibTableColumn
cvapSvcH248SelectorByteValue=_CvapSvcH248SelectorByteValue_Object((1,3,6,1,4,1,9,9,323,1,3,1,1,10),_CvapSvcH248SelectorByteValue_Type())
cvapSvcH248SelectorByteValue.setMaxAccess(_D)
if mibBuilder.loadTexts:cvapSvcH248SelectorByteValue.setStatus(_B)
class _CvapSvcDelNotifGuardTimer_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,120))
_CvapSvcDelNotifGuardTimer_Type.__name__=_E
_CvapSvcDelNotifGuardTimer_Object=MibTableColumn
cvapSvcDelNotifGuardTimer=_CvapSvcDelNotifGuardTimer_Object((1,3,6,1,4,1,9,9,323,1,3,1,1,11),_CvapSvcDelNotifGuardTimer_Type())
cvapSvcDelNotifGuardTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:cvapSvcDelNotifGuardTimer.setStatus(_B)
if mibBuilder.loadTexts:cvapSvcDelNotifGuardTimer.setUnits(_N)
class _CvapSvcMultiCIDPerSvc_Type(TruthValue):defaultValue=2
_CvapSvcMultiCIDPerSvc_Type.__name__=_L
_CvapSvcMultiCIDPerSvc_Object=MibTableColumn
cvapSvcMultiCIDPerSvc=_CvapSvcMultiCIDPerSvc_Object((1,3,6,1,4,1,9,9,323,1,3,1,1,12),_CvapSvcMultiCIDPerSvc_Type())
cvapSvcMultiCIDPerSvc.setMaxAccess(_D)
if mibBuilder.loadTexts:cvapSvcMultiCIDPerSvc.setStatus(_B)
class _CvapSvcMultiCIDFillTimer_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CvapSvcMultiCIDFillTimer_Type.__name__=_F
_CvapSvcMultiCIDFillTimer_Object=MibTableColumn
cvapSvcMultiCIDFillTimer=_CvapSvcMultiCIDFillTimer_Object((1,3,6,1,4,1,9,9,323,1,3,1,1,13),_CvapSvcMultiCIDFillTimer_Type())
cvapSvcMultiCIDFillTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:cvapSvcMultiCIDFillTimer.setStatus(_B)
if mibBuilder.loadTexts:cvapSvcMultiCIDFillTimer.setUnits(_I)
class _CvapSvcMultiCIDCACSCR_Type(Unsigned32):defaultValue=450;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(20,60000))
_CvapSvcMultiCIDCACSCR_Type.__name__=_F
_CvapSvcMultiCIDCACSCR_Object=MibTableColumn
cvapSvcMultiCIDCACSCR=_CvapSvcMultiCIDCACSCR_Object((1,3,6,1,4,1,9,9,323,1,3,1,1,14),_CvapSvcMultiCIDCACSCR_Type())
cvapSvcMultiCIDCACSCR.setMaxAccess(_D)
if mibBuilder.loadTexts:cvapSvcMultiCIDCACSCR.setStatus(_B)
if mibBuilder.loadTexts:cvapSvcMultiCIDCACSCR.setUnits(_c)
class _CvapSvcMultiCIDCACPCR_Type(Unsigned32):defaultValue=875;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(20,60000))
_CvapSvcMultiCIDCACPCR_Type.__name__=_F
_CvapSvcMultiCIDCACPCR_Object=MibTableColumn
cvapSvcMultiCIDCACPCR=_CvapSvcMultiCIDCACPCR_Object((1,3,6,1,4,1,9,9,323,1,3,1,1,15),_CvapSvcMultiCIDCACPCR_Type())
cvapSvcMultiCIDCACPCR.setMaxAccess(_D)
if mibBuilder.loadTexts:cvapSvcMultiCIDCACPCR.setStatus(_B)
if mibBuilder.loadTexts:cvapSvcMultiCIDCACPCR.setUnits(_c)
class _CvapSvcMultiCIDOriginatDelTimer_Type(Unsigned32):defaultValue=15;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1200))
_CvapSvcMultiCIDOriginatDelTimer_Type.__name__=_F
_CvapSvcMultiCIDOriginatDelTimer_Object=MibTableColumn
cvapSvcMultiCIDOriginatDelTimer=_CvapSvcMultiCIDOriginatDelTimer_Object((1,3,6,1,4,1,9,9,323,1,3,1,1,16),_CvapSvcMultiCIDOriginatDelTimer_Type())
cvapSvcMultiCIDOriginatDelTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:cvapSvcMultiCIDOriginatDelTimer.setStatus(_B)
if mibBuilder.loadTexts:cvapSvcMultiCIDOriginatDelTimer.setUnits(_N)
class _CvapSvcMultiCIDTerminatDelTimer_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1195))
_CvapSvcMultiCIDTerminatDelTimer_Type.__name__=_F
_CvapSvcMultiCIDTerminatDelTimer_Object=MibTableColumn
cvapSvcMultiCIDTerminatDelTimer=_CvapSvcMultiCIDTerminatDelTimer_Object((1,3,6,1,4,1,9,9,323,1,3,1,1,17),_CvapSvcMultiCIDTerminatDelTimer_Type())
cvapSvcMultiCIDTerminatDelTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:cvapSvcMultiCIDTerminatDelTimer.setStatus(_B)
if mibBuilder.loadTexts:cvapSvcMultiCIDTerminatDelTimer.setUnits(_N)
class _CvapSvcMultiCIDGlareThreshold_Type(Unsigned32):defaultValue=243;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,248))
_CvapSvcMultiCIDGlareThreshold_Type.__name__=_F
_CvapSvcMultiCIDGlareThreshold_Object=MibTableColumn
cvapSvcMultiCIDGlareThreshold=_CvapSvcMultiCIDGlareThreshold_Object((1,3,6,1,4,1,9,9,323,1,3,1,1,18),_CvapSvcMultiCIDGlareThreshold_Type())
cvapSvcMultiCIDGlareThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:cvapSvcMultiCIDGlareThreshold.setStatus(_B)
if mibBuilder.loadTexts:cvapSvcMultiCIDGlareThreshold.setUnits('number of CIDs')
_CvapSvcStats_ObjectIdentity=ObjectIdentity
cvapSvcStats=_CvapSvcStats_ObjectIdentity((1,3,6,1,4,1,9,9,323,1,4))
_CvapSvcStatsTable_Object=MibTable
cvapSvcStatsTable=_CvapSvcStatsTable_Object((1,3,6,1,4,1,9,9,323,1,4,1))
if mibBuilder.loadTexts:cvapSvcStatsTable.setStatus(_B)
_CvapSvcStatsEntry_Object=MibTableRow
cvapSvcStatsEntry=_CvapSvcStatsEntry_Object((1,3,6,1,4,1,9,9,323,1,4,1,1))
cvapSvcStatsEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:cvapSvcStatsEntry.setStatus(_B)
_CvapSvcTxSetups_Type=Counter32
_CvapSvcTxSetups_Object=MibTableColumn
cvapSvcTxSetups=_CvapSvcTxSetups_Object((1,3,6,1,4,1,9,9,323,1,4,1,1,1),_CvapSvcTxSetups_Type())
cvapSvcTxSetups.setMaxAccess(_C)
if mibBuilder.loadTexts:cvapSvcTxSetups.setStatus(_B)
_CvapSvcRxSetups_Type=Counter32
_CvapSvcRxSetups_Object=MibTableColumn
cvapSvcRxSetups=_CvapSvcRxSetups_Object((1,3,6,1,4,1,9,9,323,1,4,1,1,2),_CvapSvcRxSetups_Type())
cvapSvcRxSetups.setMaxAccess(_C)
if mibBuilder.loadTexts:cvapSvcRxSetups.setStatus(_B)
_CvapSvcTxCallProcs_Type=Counter32
_CvapSvcTxCallProcs_Object=MibTableColumn
cvapSvcTxCallProcs=_CvapSvcTxCallProcs_Object((1,3,6,1,4,1,9,9,323,1,4,1,1,3),_CvapSvcTxCallProcs_Type())
cvapSvcTxCallProcs.setMaxAccess(_C)
if mibBuilder.loadTexts:cvapSvcTxCallProcs.setStatus(_B)
_CvapSvcRxCallProcs_Type=Counter32
_CvapSvcRxCallProcs_Object=MibTableColumn
cvapSvcRxCallProcs=_CvapSvcRxCallProcs_Object((1,3,6,1,4,1,9,9,323,1,4,1,1,4),_CvapSvcRxCallProcs_Type())
cvapSvcRxCallProcs.setMaxAccess(_C)
if mibBuilder.loadTexts:cvapSvcRxCallProcs.setStatus(_B)
_CvapSvcTxConns_Type=Counter32
_CvapSvcTxConns_Object=MibTableColumn
cvapSvcTxConns=_CvapSvcTxConns_Object((1,3,6,1,4,1,9,9,323,1,4,1,1,5),_CvapSvcTxConns_Type())
cvapSvcTxConns.setMaxAccess(_C)
if mibBuilder.loadTexts:cvapSvcTxConns.setStatus(_B)
_CvapSvcTxConnAcks_Type=Counter32
_CvapSvcTxConnAcks_Object=MibTableColumn
cvapSvcTxConnAcks=_CvapSvcTxConnAcks_Object((1,3,6,1,4,1,9,9,323,1,4,1,1,6),_CvapSvcTxConnAcks_Type())
cvapSvcTxConnAcks.setMaxAccess(_C)
if mibBuilder.loadTexts:cvapSvcTxConnAcks.setStatus(_B)
_CvapSvcRxConns_Type=Counter32
_CvapSvcRxConns_Object=MibTableColumn
cvapSvcRxConns=_CvapSvcRxConns_Object((1,3,6,1,4,1,9,9,323,1,4,1,1,7),_CvapSvcRxConns_Type())
cvapSvcRxConns.setMaxAccess(_C)
if mibBuilder.loadTexts:cvapSvcRxConns.setStatus(_B)
_CvapSvcRxConnAcks_Type=Counter32
_CvapSvcRxConnAcks_Object=MibTableColumn
cvapSvcRxConnAcks=_CvapSvcRxConnAcks_Object((1,3,6,1,4,1,9,9,323,1,4,1,1,8),_CvapSvcRxConnAcks_Type())
cvapSvcRxConnAcks.setMaxAccess(_C)
if mibBuilder.loadTexts:cvapSvcRxConnAcks.setStatus(_B)
_CvapSvcTxReleases_Type=Counter32
_CvapSvcTxReleases_Object=MibTableColumn
cvapSvcTxReleases=_CvapSvcTxReleases_Object((1,3,6,1,4,1,9,9,323,1,4,1,1,9),_CvapSvcTxReleases_Type())
cvapSvcTxReleases.setMaxAccess(_C)
if mibBuilder.loadTexts:cvapSvcTxReleases.setStatus(_B)
_CvapSvcTxReleaseCompls_Type=Counter32
_CvapSvcTxReleaseCompls_Object=MibTableColumn
cvapSvcTxReleaseCompls=_CvapSvcTxReleaseCompls_Object((1,3,6,1,4,1,9,9,323,1,4,1,1,10),_CvapSvcTxReleaseCompls_Type())
cvapSvcTxReleaseCompls.setMaxAccess(_C)
if mibBuilder.loadTexts:cvapSvcTxReleaseCompls.setStatus(_B)
_CvapSvcRxReleases_Type=Counter32
_CvapSvcRxReleases_Object=MibTableColumn
cvapSvcRxReleases=_CvapSvcRxReleases_Object((1,3,6,1,4,1,9,9,323,1,4,1,1,11),_CvapSvcRxReleases_Type())
cvapSvcRxReleases.setMaxAccess(_C)
if mibBuilder.loadTexts:cvapSvcRxReleases.setStatus(_B)
_CvapSvcRxReleaseCompls_Type=Counter32
_CvapSvcRxReleaseCompls_Object=MibTableColumn
cvapSvcRxReleaseCompls=_CvapSvcRxReleaseCompls_Object((1,3,6,1,4,1,9,9,323,1,4,1,1,12),_CvapSvcRxReleaseCompls_Type())
cvapSvcRxReleaseCompls.setMaxAccess(_C)
if mibBuilder.loadTexts:cvapSvcRxReleaseCompls.setStatus(_B)
_CvapSvcTxRestarts_Type=Counter32
_CvapSvcTxRestarts_Object=MibTableColumn
cvapSvcTxRestarts=_CvapSvcTxRestarts_Object((1,3,6,1,4,1,9,9,323,1,4,1,1,13),_CvapSvcTxRestarts_Type())
cvapSvcTxRestarts.setMaxAccess(_C)
if mibBuilder.loadTexts:cvapSvcTxRestarts.setStatus(_B)
_CvapSvcTxRestartAcks_Type=Counter32
_CvapSvcTxRestartAcks_Object=MibTableColumn
cvapSvcTxRestartAcks=_CvapSvcTxRestartAcks_Object((1,3,6,1,4,1,9,9,323,1,4,1,1,14),_CvapSvcTxRestartAcks_Type())
cvapSvcTxRestartAcks.setMaxAccess(_C)
if mibBuilder.loadTexts:cvapSvcTxRestartAcks.setStatus(_B)
_CvapSvcRxRestarts_Type=Counter32
_CvapSvcRxRestarts_Object=MibTableColumn
cvapSvcRxRestarts=_CvapSvcRxRestarts_Object((1,3,6,1,4,1,9,9,323,1,4,1,1,15),_CvapSvcRxRestarts_Type())
cvapSvcRxRestarts.setMaxAccess(_C)
if mibBuilder.loadTexts:cvapSvcRxRestarts.setStatus(_B)
_CvapSvcRxRestartAcks_Type=Counter32
_CvapSvcRxRestartAcks_Object=MibTableColumn
cvapSvcRxRestartAcks=_CvapSvcRxRestartAcks_Object((1,3,6,1,4,1,9,9,323,1,4,1,1,16),_CvapSvcRxRestartAcks_Type())
cvapSvcRxRestartAcks.setMaxAccess(_C)
if mibBuilder.loadTexts:cvapSvcRxRestartAcks.setStatus(_B)
_CvapSvcTxResyncStrts_Type=Counter32
_CvapSvcTxResyncStrts_Object=MibTableColumn
cvapSvcTxResyncStrts=_CvapSvcTxResyncStrts_Object((1,3,6,1,4,1,9,9,323,1,4,1,1,17),_CvapSvcTxResyncStrts_Type())
cvapSvcTxResyncStrts.setMaxAccess(_C)
if mibBuilder.loadTexts:cvapSvcTxResyncStrts.setStatus(_B)
_CvapSvcTxResyncStrtAcks_Type=Counter32
_CvapSvcTxResyncStrtAcks_Object=MibTableColumn
cvapSvcTxResyncStrtAcks=_CvapSvcTxResyncStrtAcks_Object((1,3,6,1,4,1,9,9,323,1,4,1,1,18),_CvapSvcTxResyncStrtAcks_Type())
cvapSvcTxResyncStrtAcks.setMaxAccess(_C)
if mibBuilder.loadTexts:cvapSvcTxResyncStrtAcks.setStatus(_B)
_CvapSvcRxResyncStrts_Type=Counter32
_CvapSvcRxResyncStrts_Object=MibTableColumn
cvapSvcRxResyncStrts=_CvapSvcRxResyncStrts_Object((1,3,6,1,4,1,9,9,323,1,4,1,1,19),_CvapSvcRxResyncStrts_Type())
cvapSvcRxResyncStrts.setMaxAccess(_C)
if mibBuilder.loadTexts:cvapSvcRxResyncStrts.setStatus(_B)
_CvapSvcRxResyncStrtAcks_Type=Counter32
_CvapSvcRxResyncStrtAcks_Object=MibTableColumn
cvapSvcRxResyncStrtAcks=_CvapSvcRxResyncStrtAcks_Object((1,3,6,1,4,1,9,9,323,1,4,1,1,20),_CvapSvcRxResyncStrtAcks_Type())
cvapSvcRxResyncStrtAcks.setMaxAccess(_C)
if mibBuilder.loadTexts:cvapSvcRxResyncStrtAcks.setStatus(_B)
_CvapSvcTxResyncEnds_Type=Counter32
_CvapSvcTxResyncEnds_Object=MibTableColumn
cvapSvcTxResyncEnds=_CvapSvcTxResyncEnds_Object((1,3,6,1,4,1,9,9,323,1,4,1,1,21),_CvapSvcTxResyncEnds_Type())
cvapSvcTxResyncEnds.setMaxAccess(_C)
if mibBuilder.loadTexts:cvapSvcTxResyncEnds.setStatus(_B)
_CvapSvcTxResyncEndAcks_Type=Counter32
_CvapSvcTxResyncEndAcks_Object=MibTableColumn
cvapSvcTxResyncEndAcks=_CvapSvcTxResyncEndAcks_Object((1,3,6,1,4,1,9,9,323,1,4,1,1,22),_CvapSvcTxResyncEndAcks_Type())
cvapSvcTxResyncEndAcks.setMaxAccess(_C)
if mibBuilder.loadTexts:cvapSvcTxResyncEndAcks.setStatus(_B)
_CvapSvcRxResyncEnds_Type=Counter32
_CvapSvcRxResyncEnds_Object=MibTableColumn
cvapSvcRxResyncEnds=_CvapSvcRxResyncEnds_Object((1,3,6,1,4,1,9,9,323,1,4,1,1,23),_CvapSvcRxResyncEnds_Type())
cvapSvcRxResyncEnds.setMaxAccess(_C)
if mibBuilder.loadTexts:cvapSvcRxResyncEnds.setStatus(_B)
_CvapSvcRxResyncEndAcks_Type=Counter32
_CvapSvcRxResyncEndAcks_Object=MibTableColumn
cvapSvcRxResyncEndAcks=_CvapSvcRxResyncEndAcks_Object((1,3,6,1,4,1,9,9,323,1,4,1,1,24),_CvapSvcRxResyncEndAcks_Type())
cvapSvcRxResyncEndAcks.setMaxAccess(_C)
if mibBuilder.loadTexts:cvapSvcRxResyncEndAcks.setStatus(_B)
_CvapSvcTxBulkResyncs_Type=Counter32
_CvapSvcTxBulkResyncs_Object=MibTableColumn
cvapSvcTxBulkResyncs=_CvapSvcTxBulkResyncs_Object((1,3,6,1,4,1,9,9,323,1,4,1,1,25),_CvapSvcTxBulkResyncs_Type())
cvapSvcTxBulkResyncs.setMaxAccess(_C)
if mibBuilder.loadTexts:cvapSvcTxBulkResyncs.setStatus(_B)
_CvapSvcRxBulkResyncs_Type=Counter32
_CvapSvcRxBulkResyncs_Object=MibTableColumn
cvapSvcRxBulkResyncs=_CvapSvcRxBulkResyncs_Object((1,3,6,1,4,1,9,9,323,1,4,1,1,26),_CvapSvcRxBulkResyncs_Type())
cvapSvcRxBulkResyncs.setMaxAccess(_C)
if mibBuilder.loadTexts:cvapSvcRxBulkResyncs.setStatus(_B)
_CvapSvcCallProcExpiries_Type=Counter32
_CvapSvcCallProcExpiries_Object=MibTableColumn
cvapSvcCallProcExpiries=_CvapSvcCallProcExpiries_Object((1,3,6,1,4,1,9,9,323,1,4,1,1,27),_CvapSvcCallProcExpiries_Type())
cvapSvcCallProcExpiries.setMaxAccess(_C)
if mibBuilder.loadTexts:cvapSvcCallProcExpiries.setStatus(_B)
_CvapSvcReleasExpiries_Type=Counter32
_CvapSvcReleasExpiries_Object=MibTableColumn
cvapSvcReleasExpiries=_CvapSvcReleasExpiries_Object((1,3,6,1,4,1,9,9,323,1,4,1,1,28),_CvapSvcReleasExpiries_Type())
cvapSvcReleasExpiries.setMaxAccess(_C)
if mibBuilder.loadTexts:cvapSvcReleasExpiries.setStatus(_B)
_CvapSvcConnExpiries_Type=Counter32
_CvapSvcConnExpiries_Object=MibTableColumn
cvapSvcConnExpiries=_CvapSvcConnExpiries_Object((1,3,6,1,4,1,9,9,323,1,4,1,1,29),_CvapSvcConnExpiries_Type())
cvapSvcConnExpiries.setMaxAccess(_C)
if mibBuilder.loadTexts:cvapSvcConnExpiries.setStatus(_B)
_CvapSvcConnAckExpiries_Type=Counter32
_CvapSvcConnAckExpiries_Object=MibTableColumn
cvapSvcConnAckExpiries=_CvapSvcConnAckExpiries_Object((1,3,6,1,4,1,9,9,323,1,4,1,1,30),_CvapSvcConnAckExpiries_Type())
cvapSvcConnAckExpiries.setMaxAccess(_C)
if mibBuilder.loadTexts:cvapSvcConnAckExpiries.setStatus(_B)
_CvapSvcRestartExpiries_Type=Counter32
_CvapSvcRestartExpiries_Object=MibTableColumn
cvapSvcRestartExpiries=_CvapSvcRestartExpiries_Object((1,3,6,1,4,1,9,9,323,1,4,1,1,31),_CvapSvcRestartExpiries_Type())
cvapSvcRestartExpiries.setMaxAccess(_C)
if mibBuilder.loadTexts:cvapSvcRestartExpiries.setStatus(_B)
_CvapSvcResyncExpiries_Type=Counter32
_CvapSvcResyncExpiries_Object=MibTableColumn
cvapSvcResyncExpiries=_CvapSvcResyncExpiries_Object((1,3,6,1,4,1,9,9,323,1,4,1,1,32),_CvapSvcResyncExpiries_Type())
cvapSvcResyncExpiries.setMaxAccess(_C)
if mibBuilder.loadTexts:cvapSvcResyncExpiries.setStatus(_B)
_CvaProfileMIBConformance_ObjectIdentity=ObjectIdentity
cvaProfileMIBConformance=_CvaProfileMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,323,2))
_CvaProfileMIBCompliances_ObjectIdentity=ObjectIdentity
cvaProfileMIBCompliances=_CvaProfileMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,323,2,1))
_CvaProfileMIBGroups_ObjectIdentity=ObjectIdentity
cvaProfileMIBGroups=_CvaProfileMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,323,2,2))
cvapCodecConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,323,2,2,1))
cvapCodecConfigGroup.setObjects(*((_A,_O),(_A,_P),(_A,_Q),(_A,_d),(_A,_R),(_A,_S),(_A,_e),(_A,_T),(_A,_U),(_A,_V)))
if mibBuilder.loadTexts:cvapCodecConfigGroup.setStatus(_K)
cvapSvcConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,323,2,2,2))
cvapSvcConfigGroup.setObjects(*((_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w)))
if mibBuilder.loadTexts:cvapSvcConfigGroup.setStatus(_B)
cvapSvcStatsGroup=ObjectGroup((1,3,6,1,4,1,9,9,323,2,2,3))
cvapSvcStatsGroup.setObjects(*((_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA),(_A,_AB),(_A,_AC),(_A,_AD),(_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ),(_A,_AK),(_A,_AL),(_A,_AM),(_A,_AN),(_A,_AO),(_A,_AP),(_A,_AQ),(_A,_AR),(_A,_AS)))
if mibBuilder.loadTexts:cvapSvcStatsGroup.setStatus(_B)
cvapCodecConfigGroupRev1=ObjectGroup((1,3,6,1,4,1,9,9,323,2,2,4))
cvapCodecConfigGroupRev1.setObjects(*((_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_AT)))
if mibBuilder.loadTexts:cvapCodecConfigGroupRev1.setStatus(_B)
cvaProfileMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,323,2,1,1))
cvaProfileMIBCompliance.setObjects(*((_A,_AU),(_A,_W),(_A,_X)))
if mibBuilder.loadTexts:cvaProfileMIBCompliance.setStatus(_K)
cvaProfileMIBComplianceRev1=ModuleCompliance((1,3,6,1,4,1,9,9,323,2,1,2))
cvaProfileMIBComplianceRev1.setObjects(*((_A,_AV),(_A,_W),(_A,_X)))
if mibBuilder.loadTexts:cvaProfileMIBComplianceRev1.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'CiscoAal2ProfileType':CiscoAal2ProfileType,'CiscoAal2ProfileNumber':CiscoAal2ProfileNumber,'CiscoCodecPacketPeriod':CiscoCodecPacketPeriod,'ciscoVoiceAalxProfileMIB':ciscoVoiceAalxProfileMIB,'ciscoVoiceAalxProfileMIBNotifs':ciscoVoiceAalxProfileMIBNotifs,'ciscoVoiceAalxProfileMIBObjects':ciscoVoiceAalxProfileMIBObjects,'cvapCodecConfig':cvapCodecConfig,'cvapCodecTable':cvapCodecTable,'cvapCodecEntry':cvapCodecEntry,_Z:cvapCodecNegotiationAdaptType,_O:cvapCodecNegotiationOption,'cvapCodecConfigTable':cvapCodecConfigTable,'cvapCodecConfigEntry':cvapCodecConfigEntry,_a:cvapCodecConfigAdaptType,_b:cvapCodecConfigType,_P:cvapCodecConfigPreference,_Q:cvapCodecConfigVoicePacketPeriod,_d:cvapCodecConfigVbdPacketPeriod,_R:cvapCodecConfigJitterDelayMode,_S:cvapCodecConfigJitterMaxDelay,_e:cvapCodecConfigJitterNomDelay,_T:cvapCodecConfigJitterMinDelay,_U:cvapCodecConfigDtmfRelay,_V:cvapCodecConfigPayloadType,_AT:cvapCodecConfigNewJtrNomDelay,'cvapAal2Config':cvapAal2Config,'cvapSvcConfig':cvapSvcConfig,'cvapSvcConfigTable':cvapSvcConfigTable,'cvapSvcConfigEntry':cvapSvcConfigEntry,_f:cvapSvcAtmQosCellDelay,_g:cvapSvcAtmQosCtd,_h:cvapSvcAtmQosClr,_i:cvapSvcTrfScalingFactor,_j:cvapSvcAal2CidNumber,_k:cvapSvcAggTrafficClipping,_l:cvapSvcAggLinkState,_m:cvapSvcPartialFillSupported,_n:cvapSvcMgcpSelectorByteValue,_o:cvapSvcH248SelectorByteValue,_p:cvapSvcDelNotifGuardTimer,_q:cvapSvcMultiCIDPerSvc,_r:cvapSvcMultiCIDFillTimer,_s:cvapSvcMultiCIDCACSCR,_t:cvapSvcMultiCIDCACPCR,_u:cvapSvcMultiCIDOriginatDelTimer,_v:cvapSvcMultiCIDTerminatDelTimer,_w:cvapSvcMultiCIDGlareThreshold,'cvapSvcStats':cvapSvcStats,'cvapSvcStatsTable':cvapSvcStatsTable,'cvapSvcStatsEntry':cvapSvcStatsEntry,_x:cvapSvcTxSetups,_y:cvapSvcRxSetups,_z:cvapSvcTxCallProcs,_A0:cvapSvcRxCallProcs,_A1:cvapSvcTxConns,_A2:cvapSvcTxConnAcks,_A3:cvapSvcRxConns,_A4:cvapSvcRxConnAcks,_A5:cvapSvcTxReleases,_A6:cvapSvcTxReleaseCompls,_A7:cvapSvcRxReleases,_A8:cvapSvcRxReleaseCompls,_A9:cvapSvcTxRestarts,_AA:cvapSvcTxRestartAcks,_AB:cvapSvcRxRestarts,_AC:cvapSvcRxRestartAcks,_AD:cvapSvcTxResyncStrts,_AE:cvapSvcTxResyncStrtAcks,_AF:cvapSvcRxResyncStrts,_AG:cvapSvcRxResyncStrtAcks,_AH:cvapSvcTxResyncEnds,_AI:cvapSvcTxResyncEndAcks,_AJ:cvapSvcRxResyncEnds,_AK:cvapSvcRxResyncEndAcks,_AL:cvapSvcTxBulkResyncs,_AM:cvapSvcRxBulkResyncs,_AN:cvapSvcCallProcExpiries,_AO:cvapSvcReleasExpiries,_AP:cvapSvcConnExpiries,_AQ:cvapSvcConnAckExpiries,_AR:cvapSvcRestartExpiries,_AS:cvapSvcResyncExpiries,'cvaProfileMIBConformance':cvaProfileMIBConformance,'cvaProfileMIBCompliances':cvaProfileMIBCompliances,'cvaProfileMIBCompliance':cvaProfileMIBCompliance,'cvaProfileMIBComplianceRev1':cvaProfileMIBComplianceRev1,'cvaProfileMIBGroups':cvaProfileMIBGroups,_AU:cvapCodecConfigGroup,_W:cvapSvcConfigGroup,_X:cvapSvcStatsGroup,_AV:cvapCodecConfigGroupRev1})