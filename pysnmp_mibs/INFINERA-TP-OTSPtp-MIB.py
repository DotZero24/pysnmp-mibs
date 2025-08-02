_x='otsPTPGroup'
_w='otsPTPFiberLabelTx'
_v='otsPtpTimDetMode'
_u='otsPtpExpectedDAPI'
_t='otsPtpExpectedSAPI'
_s='otsptpAmpType'
_r='otsptpRecievedTTI'
_q='otsptpTransmitTTI'
_p='otsptpRemoteOAMStatus'
_o='otsptpOAMControl'
_n='otsPtpRxFiberTypeOverride'
_m='otsPTPAssociatedSltetp'
_l='otsPTPRxAssociatedOtsEqptType'
_k='otsPTPTxAssociatedOtsEqptType'
_j='otsPTPRxEqptList'
_i='otsPTPTxEqptList'
_h='otsPTPPostSpanPad'
_g='otsPTPPreSpanPad'
_f='otsPTPInlineDcmType'
_e='otsPTPSpanDistance'
_d='otsPTPTxAssociatedOtsptp'
_c='otsPTPRxAssociatedOtsptp'
_b='otsPTPPmHistStatsEnable'
_a='otsPTPRxFiberType'
_Z='otsPTPTxFiberType'
_Y='otsPtpTxAssociatedidlerPtp'
_X='otsPtpRxAssociatedidlerPtp'
_W='otsPtpLinkType'
_V='otsPtpAssociatedSltePtp'
_U='otsPtpRxAssociatedSltePtp'
_T='otsPtpAssociatedPeerTxFiberType'
_S='otsPtpProvRxFiberType'
_R='otsPtpAlsPilotSignalState'
_Q='otsPtpExpectedSpanLossRange'
_P='otsPtpOperationalOpticalSpectrum'
_O='otsPtpSupportedOpticalSpectrum'
_N='otsPTPProvisionedNeighborTP'
_M='otsPTPDiscoveredNeighborTP'
_L='extendedcband'
_K='InfnPmHistStatsControl'
_J='InfnDcmType'
_I='ifIndex'
_H='IF-MIB'
_G='InfnFiberType'
_F='FloatTenths'
_E='Integer32'
_D='read-only'
_C='read-write'
_B='INFINERA-TP-OTSPtp-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_H,_I)
terminationPoint,=mibBuilder.importSymbols('INFINERA-REG-MIB','terminationPoint')
FloatTenths,InfnDcmType,InfnEnableDisable,InfnEqptType,InfnFiberType,InfnPmHistStatsControl,InfnTimReptMode=mibBuilder.importSymbols('INFINERA-TC-MIB',_F,_J,'InfnEnableDisable','InfnEqptType',_G,_K,'InfnTimReptMode')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
otsPTPMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,2,14))
if mibBuilder.loadTexts:otsPTPMIB.setRevisions(('2008-10-20 00:00',))
_OtsPTPTable_Object=MibTable
otsPTPTable=_OtsPTPTable_Object((1,3,6,1,4,1,21296,2,2,2,2,14,1))
if mibBuilder.loadTexts:otsPTPTable.setStatus(_A)
_OtsPTPEntry_Object=MibTableRow
otsPTPEntry=_OtsPTPEntry_Object((1,3,6,1,4,1,21296,2,2,2,2,14,1,1))
otsPTPEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:otsPTPEntry.setStatus(_A)
_OtsPTPDiscoveredNeighborTP_Type=DisplayString
_OtsPTPDiscoveredNeighborTP_Object=MibTableColumn
otsPTPDiscoveredNeighborTP=_OtsPTPDiscoveredNeighborTP_Object((1,3,6,1,4,1,21296,2,2,2,2,14,1,1,1),_OtsPTPDiscoveredNeighborTP_Type())
otsPTPDiscoveredNeighborTP.setMaxAccess(_D)
if mibBuilder.loadTexts:otsPTPDiscoveredNeighborTP.setStatus(_A)
_OtsPTPProvisionedNeighborTP_Type=DisplayString
_OtsPTPProvisionedNeighborTP_Object=MibTableColumn
otsPTPProvisionedNeighborTP=_OtsPTPProvisionedNeighborTP_Object((1,3,6,1,4,1,21296,2,2,2,2,14,1,1,2),_OtsPTPProvisionedNeighborTP_Type())
otsPTPProvisionedNeighborTP.setMaxAccess(_C)
if mibBuilder.loadTexts:otsPTPProvisionedNeighborTP.setStatus(_A)
class _OtsPtpSupportedOpticalSpectrum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('cband',1),(_L,2)))
_OtsPtpSupportedOpticalSpectrum_Type.__name__=_E
_OtsPtpSupportedOpticalSpectrum_Object=MibTableColumn
otsPtpSupportedOpticalSpectrum=_OtsPtpSupportedOpticalSpectrum_Object((1,3,6,1,4,1,21296,2,2,2,2,14,1,1,3),_OtsPtpSupportedOpticalSpectrum_Type())
otsPtpSupportedOpticalSpectrum.setMaxAccess(_D)
if mibBuilder.loadTexts:otsPtpSupportedOpticalSpectrum.setStatus(_A)
class _OtsPtpOperationalOpticalSpectrum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('cband',1),(_L,2)))
_OtsPtpOperationalOpticalSpectrum_Type.__name__=_E
_OtsPtpOperationalOpticalSpectrum_Object=MibTableColumn
otsPtpOperationalOpticalSpectrum=_OtsPtpOperationalOpticalSpectrum_Object((1,3,6,1,4,1,21296,2,2,2,2,14,1,1,4),_OtsPtpOperationalOpticalSpectrum_Type())
otsPtpOperationalOpticalSpectrum.setMaxAccess(_D)
if mibBuilder.loadTexts:otsPtpOperationalOpticalSpectrum.setStatus(_A)
class _OtsPtpExpectedSpanLossRange_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('under25dB',1),('over25dB',2)))
_OtsPtpExpectedSpanLossRange_Type.__name__=_E
_OtsPtpExpectedSpanLossRange_Object=MibTableColumn
otsPtpExpectedSpanLossRange=_OtsPtpExpectedSpanLossRange_Object((1,3,6,1,4,1,21296,2,2,2,2,14,1,1,5),_OtsPtpExpectedSpanLossRange_Type())
otsPtpExpectedSpanLossRange.setMaxAccess(_C)
if mibBuilder.loadTexts:otsPtpExpectedSpanLossRange.setStatus(_A)
class _OtsPtpAlsPilotSignalState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('unknown',1),('normal',2),('nosignal',3),('remoteRxFault',4),('localRxFault',5)))
_OtsPtpAlsPilotSignalState_Type.__name__=_E
_OtsPtpAlsPilotSignalState_Object=MibTableColumn
otsPtpAlsPilotSignalState=_OtsPtpAlsPilotSignalState_Object((1,3,6,1,4,1,21296,2,2,2,2,14,1,1,6),_OtsPtpAlsPilotSignalState_Type())
otsPtpAlsPilotSignalState.setMaxAccess(_D)
if mibBuilder.loadTexts:otsPtpAlsPilotSignalState.setStatus(_A)
class _OtsPTPTxFiberType_Type(InfnFiberType):defaultValue=2
_OtsPTPTxFiberType_Type.__name__=_G
_OtsPTPTxFiberType_Object=MibTableColumn
otsPTPTxFiberType=_OtsPTPTxFiberType_Object((1,3,6,1,4,1,21296,2,2,2,2,14,1,1,7),_OtsPTPTxFiberType_Type())
otsPTPTxFiberType.setMaxAccess(_C)
if mibBuilder.loadTexts:otsPTPTxFiberType.setStatus(_A)
_OtsPtpProvRxFiberType_Type=InfnFiberType
_OtsPtpProvRxFiberType_Object=MibTableColumn
otsPtpProvRxFiberType=_OtsPtpProvRxFiberType_Object((1,3,6,1,4,1,21296,2,2,2,2,14,1,1,8),_OtsPtpProvRxFiberType_Type())
otsPtpProvRxFiberType.setMaxAccess(_D)
if mibBuilder.loadTexts:otsPtpProvRxFiberType.setStatus(_A)
class _OtsPTPRxFiberType_Type(InfnFiberType):defaultValue=1
_OtsPTPRxFiberType_Type.__name__=_G
_OtsPTPRxFiberType_Object=MibTableColumn
otsPTPRxFiberType=_OtsPTPRxFiberType_Object((1,3,6,1,4,1,21296,2,2,2,2,14,1,1,9),_OtsPTPRxFiberType_Type())
otsPTPRxFiberType.setMaxAccess(_D)
if mibBuilder.loadTexts:otsPTPRxFiberType.setStatus(_A)
_OtsPtpAssociatedPeerTxFiberType_Type=InfnFiberType
_OtsPtpAssociatedPeerTxFiberType_Object=MibTableColumn
otsPtpAssociatedPeerTxFiberType=_OtsPtpAssociatedPeerTxFiberType_Object((1,3,6,1,4,1,21296,2,2,2,2,14,1,1,10),_OtsPtpAssociatedPeerTxFiberType_Type())
otsPtpAssociatedPeerTxFiberType.setMaxAccess(_C)
if mibBuilder.loadTexts:otsPtpAssociatedPeerTxFiberType.setStatus(_A)
class _OtsPTPPmHistStatsEnable_Type(InfnPmHistStatsControl):defaultValue=1
_OtsPTPPmHistStatsEnable_Type.__name__=_K
_OtsPTPPmHistStatsEnable_Object=MibTableColumn
otsPTPPmHistStatsEnable=_OtsPTPPmHistStatsEnable_Object((1,3,6,1,4,1,21296,2,2,2,2,14,1,1,11),_OtsPTPPmHistStatsEnable_Type())
otsPTPPmHistStatsEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:otsPTPPmHistStatsEnable.setStatus(_A)
class _OtsPtpLinkType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('linktype1',1),('linktype2',2)))
_OtsPtpLinkType_Type.__name__=_E
_OtsPtpLinkType_Object=MibTableColumn
otsPtpLinkType=_OtsPtpLinkType_Object((1,3,6,1,4,1,21296,2,2,2,2,14,1,1,12),_OtsPtpLinkType_Type())
otsPtpLinkType.setMaxAccess(_C)
if mibBuilder.loadTexts:otsPtpLinkType.setStatus(_A)
_OtsPTPRxAssociatedOtsptp_Type=DisplayString
_OtsPTPRxAssociatedOtsptp_Object=MibTableColumn
otsPTPRxAssociatedOtsptp=_OtsPTPRxAssociatedOtsptp_Object((1,3,6,1,4,1,21296,2,2,2,2,14,1,1,13),_OtsPTPRxAssociatedOtsptp_Type())
otsPTPRxAssociatedOtsptp.setMaxAccess(_C)
if mibBuilder.loadTexts:otsPTPRxAssociatedOtsptp.setStatus(_A)
_OtsPTPTxAssociatedOtsptp_Type=DisplayString
_OtsPTPTxAssociatedOtsptp_Object=MibTableColumn
otsPTPTxAssociatedOtsptp=_OtsPTPTxAssociatedOtsptp_Object((1,3,6,1,4,1,21296,2,2,2,2,14,1,1,14),_OtsPTPTxAssociatedOtsptp_Type())
otsPTPTxAssociatedOtsptp.setMaxAccess(_C)
if mibBuilder.loadTexts:otsPTPTxAssociatedOtsptp.setStatus(_A)
_OtsPTPTxAssociatedOtsEqptType_Type=InfnEqptType
_OtsPTPTxAssociatedOtsEqptType_Object=MibTableColumn
otsPTPTxAssociatedOtsEqptType=_OtsPTPTxAssociatedOtsEqptType_Object((1,3,6,1,4,1,21296,2,2,2,2,14,1,1,15),_OtsPTPTxAssociatedOtsEqptType_Type())
otsPTPTxAssociatedOtsEqptType.setMaxAccess(_D)
if mibBuilder.loadTexts:otsPTPTxAssociatedOtsEqptType.setStatus(_A)
_OtsPTPRxAssociatedOtsEqptType_Type=InfnEqptType
_OtsPTPRxAssociatedOtsEqptType_Object=MibTableColumn
otsPTPRxAssociatedOtsEqptType=_OtsPTPRxAssociatedOtsEqptType_Object((1,3,6,1,4,1,21296,2,2,2,2,14,1,1,16),_OtsPTPRxAssociatedOtsEqptType_Type())
otsPTPRxAssociatedOtsEqptType.setMaxAccess(_D)
if mibBuilder.loadTexts:otsPTPRxAssociatedOtsEqptType.setStatus(_A)
class _OtsPTPSpanDistance_Type(FloatTenths):defaultValue=0
_OtsPTPSpanDistance_Type.__name__=_F
_OtsPTPSpanDistance_Object=MibTableColumn
otsPTPSpanDistance=_OtsPTPSpanDistance_Object((1,3,6,1,4,1,21296,2,2,2,2,14,1,1,17),_OtsPTPSpanDistance_Type())
otsPTPSpanDistance.setMaxAccess(_C)
if mibBuilder.loadTexts:otsPTPSpanDistance.setStatus(_A)
class _OtsPTPInlineDcmType_Type(InfnDcmType):defaultValue=25
_OtsPTPInlineDcmType_Type.__name__=_J
_OtsPTPInlineDcmType_Object=MibTableColumn
otsPTPInlineDcmType=_OtsPTPInlineDcmType_Object((1,3,6,1,4,1,21296,2,2,2,2,14,1,1,18),_OtsPTPInlineDcmType_Type())
otsPTPInlineDcmType.setMaxAccess(_C)
if mibBuilder.loadTexts:otsPTPInlineDcmType.setStatus(_A)
class _OtsPTPPreSpanPad_Type(FloatTenths):defaultValue=0
_OtsPTPPreSpanPad_Type.__name__=_F
_OtsPTPPreSpanPad_Object=MibTableColumn
otsPTPPreSpanPad=_OtsPTPPreSpanPad_Object((1,3,6,1,4,1,21296,2,2,2,2,14,1,1,19),_OtsPTPPreSpanPad_Type())
otsPTPPreSpanPad.setMaxAccess(_C)
if mibBuilder.loadTexts:otsPTPPreSpanPad.setStatus(_A)
class _OtsPTPPostSpanPad_Type(FloatTenths):defaultValue=0
_OtsPTPPostSpanPad_Type.__name__=_F
_OtsPTPPostSpanPad_Object=MibTableColumn
otsPTPPostSpanPad=_OtsPTPPostSpanPad_Object((1,3,6,1,4,1,21296,2,2,2,2,14,1,1,20),_OtsPTPPostSpanPad_Type())
otsPTPPostSpanPad.setMaxAccess(_C)
if mibBuilder.loadTexts:otsPTPPostSpanPad.setStatus(_A)
_OtsPTPAssociatedSltetp_Type=DisplayString
_OtsPTPAssociatedSltetp_Object=MibTableColumn
otsPTPAssociatedSltetp=_OtsPTPAssociatedSltetp_Object((1,3,6,1,4,1,21296,2,2,2,2,14,1,1,21),_OtsPTPAssociatedSltetp_Type())
otsPTPAssociatedSltetp.setMaxAccess(_C)
if mibBuilder.loadTexts:otsPTPAssociatedSltetp.setStatus(_A)
_OtsPtpRxAssociatedSltePtp_Type=DisplayString
_OtsPtpRxAssociatedSltePtp_Object=MibTableColumn
otsPtpRxAssociatedSltePtp=_OtsPtpRxAssociatedSltePtp_Object((1,3,6,1,4,1,21296,2,2,2,2,14,1,1,22),_OtsPtpRxAssociatedSltePtp_Type())
otsPtpRxAssociatedSltePtp.setMaxAccess(_C)
if mibBuilder.loadTexts:otsPtpRxAssociatedSltePtp.setStatus(_A)
_OtsPtpAssociatedSltePtp_Type=DisplayString
_OtsPtpAssociatedSltePtp_Object=MibTableColumn
otsPtpAssociatedSltePtp=_OtsPtpAssociatedSltePtp_Object((1,3,6,1,4,1,21296,2,2,2,2,14,1,1,23),_OtsPtpAssociatedSltePtp_Type())
otsPtpAssociatedSltePtp.setMaxAccess(_C)
if mibBuilder.loadTexts:otsPtpAssociatedSltePtp.setStatus(_A)
_OtsPtpTxAssociatedidlerPtp_Type=DisplayString
_OtsPtpTxAssociatedidlerPtp_Object=MibTableColumn
otsPtpTxAssociatedidlerPtp=_OtsPtpTxAssociatedidlerPtp_Object((1,3,6,1,4,1,21296,2,2,2,2,14,1,1,24),_OtsPtpTxAssociatedidlerPtp_Type())
otsPtpTxAssociatedidlerPtp.setMaxAccess(_D)
if mibBuilder.loadTexts:otsPtpTxAssociatedidlerPtp.setStatus(_A)
_OtsPtpRxAssociatedidlerPtp_Type=DisplayString
_OtsPtpRxAssociatedidlerPtp_Object=MibTableColumn
otsPtpRxAssociatedidlerPtp=_OtsPtpRxAssociatedidlerPtp_Object((1,3,6,1,4,1,21296,2,2,2,2,14,1,1,25),_OtsPtpRxAssociatedidlerPtp_Type())
otsPtpRxAssociatedidlerPtp.setMaxAccess(_D)
if mibBuilder.loadTexts:otsPtpRxAssociatedidlerPtp.setStatus(_A)
_OtsPTPTxEqptList_Type=DisplayString
_OtsPTPTxEqptList_Object=MibTableColumn
otsPTPTxEqptList=_OtsPTPTxEqptList_Object((1,3,6,1,4,1,21296,2,2,2,2,14,1,1,26),_OtsPTPTxEqptList_Type())
otsPTPTxEqptList.setMaxAccess(_C)
if mibBuilder.loadTexts:otsPTPTxEqptList.setStatus(_A)
_OtsPTPRxEqptList_Type=DisplayString
_OtsPTPRxEqptList_Object=MibTableColumn
otsPTPRxEqptList=_OtsPTPRxEqptList_Object((1,3,6,1,4,1,21296,2,2,2,2,14,1,1,27),_OtsPTPRxEqptList_Type())
otsPTPRxEqptList.setMaxAccess(_C)
if mibBuilder.loadTexts:otsPTPRxEqptList.setStatus(_A)
class _OtsPtpRxFiberTypeOverride_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_OtsPtpRxFiberTypeOverride_Type.__name__=_E
_OtsPtpRxFiberTypeOverride_Object=MibTableColumn
otsPtpRxFiberTypeOverride=_OtsPtpRxFiberTypeOverride_Object((1,3,6,1,4,1,21296,2,2,2,2,14,1,1,28),_OtsPtpRxFiberTypeOverride_Type())
otsPtpRxFiberTypeOverride.setMaxAccess(_C)
if mibBuilder.loadTexts:otsPtpRxFiberTypeOverride.setStatus(_A)
_OtsptpOAMControl_Type=InfnEnableDisable
_OtsptpOAMControl_Object=MibTableColumn
otsptpOAMControl=_OtsptpOAMControl_Object((1,3,6,1,4,1,21296,2,2,2,2,14,1,1,29),_OtsptpOAMControl_Type())
otsptpOAMControl.setMaxAccess(_C)
if mibBuilder.loadTexts:otsptpOAMControl.setStatus(_A)
_OtsptpRemoteOAMStatus_Type=InfnEnableDisable
_OtsptpRemoteOAMStatus_Object=MibTableColumn
otsptpRemoteOAMStatus=_OtsptpRemoteOAMStatus_Object((1,3,6,1,4,1,21296,2,2,2,2,14,1,1,30),_OtsptpRemoteOAMStatus_Type())
otsptpRemoteOAMStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:otsptpRemoteOAMStatus.setStatus(_A)
_OtsptpTransmitTTI_Type=DisplayString
_OtsptpTransmitTTI_Object=MibTableColumn
otsptpTransmitTTI=_OtsptpTransmitTTI_Object((1,3,6,1,4,1,21296,2,2,2,2,14,1,1,31),_OtsptpTransmitTTI_Type())
otsptpTransmitTTI.setMaxAccess(_D)
if mibBuilder.loadTexts:otsptpTransmitTTI.setStatus(_A)
_OtsptpRecievedTTI_Type=DisplayString
_OtsptpRecievedTTI_Object=MibTableColumn
otsptpRecievedTTI=_OtsptpRecievedTTI_Object((1,3,6,1,4,1,21296,2,2,2,2,14,1,1,32),_OtsptpRecievedTTI_Type())
otsptpRecievedTTI.setMaxAccess(_D)
if mibBuilder.loadTexts:otsptpRecievedTTI.setStatus(_A)
_OtsptpAmpType_Type=Integer32
_OtsptpAmpType_Object=MibTableColumn
otsptpAmpType=_OtsptpAmpType_Object((1,3,6,1,4,1,21296,2,2,2,2,14,1,1,33),_OtsptpAmpType_Type())
otsptpAmpType.setMaxAccess(_D)
if mibBuilder.loadTexts:otsptpAmpType.setStatus(_A)
_OtsPtpExpectedSAPI_Type=DisplayString
_OtsPtpExpectedSAPI_Object=MibTableColumn
otsPtpExpectedSAPI=_OtsPtpExpectedSAPI_Object((1,3,6,1,4,1,21296,2,2,2,2,14,1,1,34),_OtsPtpExpectedSAPI_Type())
otsPtpExpectedSAPI.setMaxAccess(_C)
if mibBuilder.loadTexts:otsPtpExpectedSAPI.setStatus(_A)
_OtsPtpExpectedDAPI_Type=DisplayString
_OtsPtpExpectedDAPI_Object=MibTableColumn
otsPtpExpectedDAPI=_OtsPtpExpectedDAPI_Object((1,3,6,1,4,1,21296,2,2,2,2,14,1,1,35),_OtsPtpExpectedDAPI_Type())
otsPtpExpectedDAPI.setMaxAccess(_C)
if mibBuilder.loadTexts:otsPtpExpectedDAPI.setStatus(_A)
_OtsPtpTimDetMode_Type=InfnTimReptMode
_OtsPtpTimDetMode_Object=MibTableColumn
otsPtpTimDetMode=_OtsPtpTimDetMode_Object((1,3,6,1,4,1,21296,2,2,2,2,14,1,1,36),_OtsPtpTimDetMode_Type())
otsPtpTimDetMode.setMaxAccess(_C)
if mibBuilder.loadTexts:otsPtpTimDetMode.setStatus(_A)
_OtsPTPFiberLabelTx_Type=DisplayString
_OtsPTPFiberLabelTx_Object=MibTableColumn
otsPTPFiberLabelTx=_OtsPTPFiberLabelTx_Object((1,3,6,1,4,1,21296,2,2,2,2,14,1,1,37),_OtsPTPFiberLabelTx_Type())
otsPTPFiberLabelTx.setMaxAccess(_C)
if mibBuilder.loadTexts:otsPTPFiberLabelTx.setStatus(_A)
_OtsPTPConformance_ObjectIdentity=ObjectIdentity
otsPTPConformance=_OtsPTPConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,14,3))
_OtsPTPCompliances_ObjectIdentity=ObjectIdentity
otsPTPCompliances=_OtsPTPCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,14,3,1))
_OtsPTPGroups_ObjectIdentity=ObjectIdentity
otsPTPGroups=_OtsPTPGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,14,3,2))
otsPTPGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,2,14,3,2,1))
otsPTPGroup.setObjects(*((_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w)))
if mibBuilder.loadTexts:otsPTPGroup.setStatus(_A)
otsPTPCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,2,14,3,1,1))
otsPTPCompliance.setObjects((_B,_x))
if mibBuilder.loadTexts:otsPTPCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'otsPTPMIB':otsPTPMIB,'otsPTPTable':otsPTPTable,'otsPTPEntry':otsPTPEntry,_M:otsPTPDiscoveredNeighborTP,_N:otsPTPProvisionedNeighborTP,_O:otsPtpSupportedOpticalSpectrum,_P:otsPtpOperationalOpticalSpectrum,_Q:otsPtpExpectedSpanLossRange,_R:otsPtpAlsPilotSignalState,_Z:otsPTPTxFiberType,_S:otsPtpProvRxFiberType,_a:otsPTPRxFiberType,_T:otsPtpAssociatedPeerTxFiberType,_b:otsPTPPmHistStatsEnable,_W:otsPtpLinkType,_c:otsPTPRxAssociatedOtsptp,_d:otsPTPTxAssociatedOtsptp,_k:otsPTPTxAssociatedOtsEqptType,_l:otsPTPRxAssociatedOtsEqptType,_e:otsPTPSpanDistance,_f:otsPTPInlineDcmType,_g:otsPTPPreSpanPad,_h:otsPTPPostSpanPad,_m:otsPTPAssociatedSltetp,_U:otsPtpRxAssociatedSltePtp,_V:otsPtpAssociatedSltePtp,_Y:otsPtpTxAssociatedidlerPtp,_X:otsPtpRxAssociatedidlerPtp,_i:otsPTPTxEqptList,_j:otsPTPRxEqptList,_n:otsPtpRxFiberTypeOverride,_o:otsptpOAMControl,_p:otsptpRemoteOAMStatus,_q:otsptpTransmitTTI,_r:otsptpRecievedTTI,_s:otsptpAmpType,_t:otsPtpExpectedSAPI,_u:otsPtpExpectedDAPI,_v:otsPtpTimDetMode,_w:otsPTPFiberLabelTx,'otsPTPConformance':otsPTPConformance,'otsPTPCompliances':otsPTPCompliances,'otsPTPCompliance':otsPTPCompliance,'otsPTPGroups':otsPTPGroups,_x:otsPTPGroup})