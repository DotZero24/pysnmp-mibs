_AL='alaDcbxPfcUsageNewGroup'
_AK='alaDcbxPfcUsageGroup'
_AJ='alaDcbxPortInstancePriorityGroup'
_AI='alaDcbxPortInstanceGroup'
_AH='alaDcbxDCPTrafficClassGroup'
_AG='alaDcbxDCProfileGroup'
_AF='alaXdot1dcbxAdminApplicationPriorityAppRowStatus'
_AE='alaXdot1dcbxAdminApplicationPriorityAEPriority'
_AD='alaDcbxPfcUsagePrioritiesAvailable'
_AC='alaDcbxPfcUsagePrioritiesReserved'
_AB='alaDcbxPfcUsagePrioritiesUsed'
_AA='alaDcbxPfcLLPrioritiesAvailable'
_A9='alaDcbxPfcLLPrioritiesReserved'
_A8='alaDcbxPfcLLPrioritiesUsed'
_A7='alaDcbxPIPrioPFCPacketsTransmitted'
_A6='alaDcbxPIPrioPFCPacketsReceived'
_A5='alaDcbxPIPrioTC'
_A4='alaDcbxPIDCBXRemoteOperVersion'
_A3='alaDcbxPIDCBXOperVersion'
_A2='alaDcbxPIDCBXVersion'
_A1='alaDcbxPIRowStatus'
_A0='alaDcbxPIActionTaken'
_z='alaDcbxPIStatus'
_y='alaDcbxPIPFCStatsClear'
_x='alaDcbxPIPFCDefense'
_w='alaDcbxPILocalModified'
_v='alaDcbxPIAdminDCPName'
_u='alaDcbxPIAdminDCPId'
_t='alaDcbxPIDCBXOper'
_s='alaDcbxPIDCBXAdmin'
_r='alaDcbxDCPTCRecommendedTrafficScheduler'
_q='alaDcbxDCPTCRecommendedBandwidth'
_p='alaDcbxDCPTCTrafficScheduler'
_o='alaDcbxDCPTCPriorityMap'
_n='alaDcbxDCPTCPFCTrafficFlow'
_m='alaDcbxDCPTCPFCLinkDelayUserModified'
_l='alaDcbxDCPTCPFCLinkDelay'
_k='alaDcbxDCPTCMinimumBandwidth'
_j='alaDcbxDCPTCMaximumBandwidth'
_i='alaDcbxDCPTCDCPName'
_h='alaDcbxDCPRowStatus'
_g='alaDcbxDCP8023xPauseReady'
_f='alaDcbxDCPTCsPresent'
_e='alaDcbxDCPTemplateDCPName'
_d='alaDcbxDCPTemplateDCPId'
_c='alaDcbxDCPPriorityTCMap'
_b='alaDcbxDCPPFCCap'
_a='alaDcbxDCPETSTrafficClassesSupported'
_Z='alaDcbxDCPName'
_Y='alaDcbxPfcUsageChassisId'
_X='alaDcbxPIPrioPriority'
_W='alaDcbxPIPrioIfIndex'
_V='DcbxActionTaken'
_U='DcbxStatus'
_T='alaDcbxPIIfIndex'
_S='alaDcbxDCPTCTrafficClass'
_R='alaDcbxDCPTCDCPId'
_Q='alaDcbxDCPId'
_P='lldpV2LocPortIfIndex'
_O='LLDP-V2-MIB'
_N='lldpXdot1dcbxAdminApplicationPriorityAESelector'
_M='lldpXdot1dcbxAdminApplicationPriorityAEProtocol'
_L='deprecated'
_K='TruthValue'
_J='LLDP-EXT-DOT1-V2-MIB'
_I='SnmpAdminString'
_H='read-write'
_G='Unsigned32'
_F='VfcEnableState'
_E='not-accessible'
_D='read-create'
_C='read-only'
_B='ALCATEL-ENT1-DCBX-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
softentIND1Dcbx,=mibBuilder.importSymbols('ALCATEL-ENT1-BASE','softentIND1Dcbx')
VfcEnableState,=mibBuilder.importSymbols('ALCATEL-ENT1-VIRTUAL-FLOW-CONTROL-MIB',_F)
IEEE8021PriorityValue,=mibBuilder.importSymbols('IEEE8021-TC-MIB','IEEE8021PriorityValue')
LldpXdot1dcbxAppProtocol,LldpXdot1dcbxAppSelector,LldpXdot1dcbxSupportedCapacity,LldpXdot1dcbxTrafficClassBandwidthValue,LldpXdot1dcbxTrafficClassValue,LldpXdot1dcbxTrafficSelectionAlgorithm,lldpXdot1dcbxAdminApplicationPriorityAEProtocol,lldpXdot1dcbxAdminApplicationPriorityAESelector=mibBuilder.importSymbols(_J,'LldpXdot1dcbxAppProtocol','LldpXdot1dcbxAppSelector','LldpXdot1dcbxSupportedCapacity','LldpXdot1dcbxTrafficClassBandwidthValue','LldpXdot1dcbxTrafficClassValue','LldpXdot1dcbxTrafficSelectionAlgorithm',_M,_N)
lldpV2LocPortIfIndex,=mibBuilder.importSymbols(_O,_P)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_I)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_K)
alcatelIND1DcbxMIB=ModuleIdentity((1,3,6,1,4,1,6486,801,1,2,1,72,1))
if mibBuilder.loadTexts:alcatelIND1DcbxMIB.setRevisions(('2011-06-28 00:00',))
class DcbxTrafficFlow(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('tfLossy',0),('tfLossless',1)))
class DcbxPriorityTCMap(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(32,32));fixedLength=32
class DcbxStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('ok',0),('pfcResourcesExhausted',1),('pfcTlvMismatch',2),('etsTlvMismatch',3),('etsPfcTlvMismatch',4)))
class DcbxActionTaken(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('na',0),('restEtsAdminCfg',1),('restPfcAdminCfg',2),('disabledPfc',3),('restEtsPfcAdminCfg',4),('cfgLocalAdmin',5),('cfgLocalRecom',6),('cfgRemoteAdmin',7),('cfgRemoteRecom',8)))
class DcbxTCsPresent(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1));fixedLength=1
class DcbxVersion(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('ieee',0),('cee',1),('auto',2)))
class RemoteDcbxVersion(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('ieee',0),('cee',1),('auto',2),('unknown',3)))
_AlcatelIND1DcbxMIBObjects_ObjectIdentity=ObjectIdentity
alcatelIND1DcbxMIBObjects=_AlcatelIND1DcbxMIBObjects_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,72,1,1))
if mibBuilder.loadTexts:alcatelIND1DcbxMIBObjects.setStatus(_A)
_AlaDcbxConfig_ObjectIdentity=ObjectIdentity
alaDcbxConfig=_AlaDcbxConfig_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,72,1,1,1))
_AlaDcbxDCProfileTable_Object=MibTable
alaDcbxDCProfileTable=_AlaDcbxDCProfileTable_Object((1,3,6,1,4,1,6486,801,1,2,1,72,1,1,1,1))
if mibBuilder.loadTexts:alaDcbxDCProfileTable.setStatus(_A)
_AlaDcbxDCProfileEntry_Object=MibTableRow
alaDcbxDCProfileEntry=_AlaDcbxDCProfileEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,72,1,1,1,1,1))
alaDcbxDCProfileEntry.setIndexNames((0,_B,_Q))
if mibBuilder.loadTexts:alaDcbxDCProfileEntry.setStatus(_A)
class _AlaDcbxDCPId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_AlaDcbxDCPId_Type.__name__=_G
_AlaDcbxDCPId_Object=MibTableColumn
alaDcbxDCPId=_AlaDcbxDCPId_Object((1,3,6,1,4,1,6486,801,1,2,1,72,1,1,1,1,1,1),_AlaDcbxDCPId_Type())
alaDcbxDCPId.setMaxAccess(_E)
if mibBuilder.loadTexts:alaDcbxDCPId.setStatus(_A)
class _AlaDcbxDCPName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_AlaDcbxDCPName_Type.__name__=_I
_AlaDcbxDCPName_Object=MibTableColumn
alaDcbxDCPName=_AlaDcbxDCPName_Object((1,3,6,1,4,1,6486,801,1,2,1,72,1,1,1,1,1,2),_AlaDcbxDCPName_Type())
alaDcbxDCPName.setMaxAccess(_D)
if mibBuilder.loadTexts:alaDcbxDCPName.setStatus(_A)
_AlaDcbxDCPETSTrafficClassesSupported_Type=LldpXdot1dcbxSupportedCapacity
_AlaDcbxDCPETSTrafficClassesSupported_Object=MibTableColumn
alaDcbxDCPETSTrafficClassesSupported=_AlaDcbxDCPETSTrafficClassesSupported_Object((1,3,6,1,4,1,6486,801,1,2,1,72,1,1,1,1,1,3),_AlaDcbxDCPETSTrafficClassesSupported_Type())
alaDcbxDCPETSTrafficClassesSupported.setMaxAccess(_C)
if mibBuilder.loadTexts:alaDcbxDCPETSTrafficClassesSupported.setStatus(_A)
_AlaDcbxDCPPFCCap_Type=LldpXdot1dcbxSupportedCapacity
_AlaDcbxDCPPFCCap_Object=MibTableColumn
alaDcbxDCPPFCCap=_AlaDcbxDCPPFCCap_Object((1,3,6,1,4,1,6486,801,1,2,1,72,1,1,1,1,1,4),_AlaDcbxDCPPFCCap_Type())
alaDcbxDCPPFCCap.setMaxAccess(_C)
if mibBuilder.loadTexts:alaDcbxDCPPFCCap.setStatus(_A)
_AlaDcbxDCPPriorityTCMap_Type=DcbxPriorityTCMap
_AlaDcbxDCPPriorityTCMap_Object=MibTableColumn
alaDcbxDCPPriorityTCMap=_AlaDcbxDCPPriorityTCMap_Object((1,3,6,1,4,1,6486,801,1,2,1,72,1,1,1,1,1,5),_AlaDcbxDCPPriorityTCMap_Type())
alaDcbxDCPPriorityTCMap.setMaxAccess(_C)
if mibBuilder.loadTexts:alaDcbxDCPPriorityTCMap.setStatus(_A)
class _AlaDcbxDCPTemplateDCPId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_AlaDcbxDCPTemplateDCPId_Type.__name__=_G
_AlaDcbxDCPTemplateDCPId_Object=MibTableColumn
alaDcbxDCPTemplateDCPId=_AlaDcbxDCPTemplateDCPId_Object((1,3,6,1,4,1,6486,801,1,2,1,72,1,1,1,1,1,6),_AlaDcbxDCPTemplateDCPId_Type())
alaDcbxDCPTemplateDCPId.setMaxAccess(_D)
if mibBuilder.loadTexts:alaDcbxDCPTemplateDCPId.setStatus(_A)
class _AlaDcbxDCPTemplateDCPName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_AlaDcbxDCPTemplateDCPName_Type.__name__=_I
_AlaDcbxDCPTemplateDCPName_Object=MibTableColumn
alaDcbxDCPTemplateDCPName=_AlaDcbxDCPTemplateDCPName_Object((1,3,6,1,4,1,6486,801,1,2,1,72,1,1,1,1,1,7),_AlaDcbxDCPTemplateDCPName_Type())
alaDcbxDCPTemplateDCPName.setMaxAccess(_D)
if mibBuilder.loadTexts:alaDcbxDCPTemplateDCPName.setStatus(_A)
_AlaDcbxDCPTCsPresent_Type=DcbxTCsPresent
_AlaDcbxDCPTCsPresent_Object=MibTableColumn
alaDcbxDCPTCsPresent=_AlaDcbxDCPTCsPresent_Object((1,3,6,1,4,1,6486,801,1,2,1,72,1,1,1,1,1,8),_AlaDcbxDCPTCsPresent_Type())
alaDcbxDCPTCsPresent.setMaxAccess(_D)
if mibBuilder.loadTexts:alaDcbxDCPTCsPresent.setStatus(_A)
class _AlaDcbxDCP8023xPauseReady_Type(VfcEnableState):defaultValue=0
_AlaDcbxDCP8023xPauseReady_Type.__name__=_F
_AlaDcbxDCP8023xPauseReady_Object=MibTableColumn
alaDcbxDCP8023xPauseReady=_AlaDcbxDCP8023xPauseReady_Object((1,3,6,1,4,1,6486,801,1,2,1,72,1,1,1,1,1,9),_AlaDcbxDCP8023xPauseReady_Type())
alaDcbxDCP8023xPauseReady.setMaxAccess(_D)
if mibBuilder.loadTexts:alaDcbxDCP8023xPauseReady.setStatus(_A)
_AlaDcbxDCPRowStatus_Type=RowStatus
_AlaDcbxDCPRowStatus_Object=MibTableColumn
alaDcbxDCPRowStatus=_AlaDcbxDCPRowStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,72,1,1,1,1,1,10),_AlaDcbxDCPRowStatus_Type())
alaDcbxDCPRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:alaDcbxDCPRowStatus.setStatus(_A)
_AlaDcbxDCPTrafficClassTable_Object=MibTable
alaDcbxDCPTrafficClassTable=_AlaDcbxDCPTrafficClassTable_Object((1,3,6,1,4,1,6486,801,1,2,1,72,1,1,1,2))
if mibBuilder.loadTexts:alaDcbxDCPTrafficClassTable.setStatus(_A)
_AlaDcbxDCPTCEntry_Object=MibTableRow
alaDcbxDCPTCEntry=_AlaDcbxDCPTCEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,72,1,1,1,2,1))
alaDcbxDCPTCEntry.setIndexNames((0,_B,_R),(0,_B,_S))
if mibBuilder.loadTexts:alaDcbxDCPTCEntry.setStatus(_A)
class _AlaDcbxDCPTCDCPId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_AlaDcbxDCPTCDCPId_Type.__name__=_G
_AlaDcbxDCPTCDCPId_Object=MibTableColumn
alaDcbxDCPTCDCPId=_AlaDcbxDCPTCDCPId_Object((1,3,6,1,4,1,6486,801,1,2,1,72,1,1,1,2,1,1),_AlaDcbxDCPTCDCPId_Type())
alaDcbxDCPTCDCPId.setMaxAccess(_E)
if mibBuilder.loadTexts:alaDcbxDCPTCDCPId.setStatus(_A)
_AlaDcbxDCPTCTrafficClass_Type=LldpXdot1dcbxTrafficClassValue
_AlaDcbxDCPTCTrafficClass_Object=MibTableColumn
alaDcbxDCPTCTrafficClass=_AlaDcbxDCPTCTrafficClass_Object((1,3,6,1,4,1,6486,801,1,2,1,72,1,1,1,2,1,2),_AlaDcbxDCPTCTrafficClass_Type())
alaDcbxDCPTCTrafficClass.setMaxAccess(_E)
if mibBuilder.loadTexts:alaDcbxDCPTCTrafficClass.setStatus(_A)
class _AlaDcbxDCPTCDCPName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_AlaDcbxDCPTCDCPName_Type.__name__=_I
_AlaDcbxDCPTCDCPName_Object=MibTableColumn
alaDcbxDCPTCDCPName=_AlaDcbxDCPTCDCPName_Object((1,3,6,1,4,1,6486,801,1,2,1,72,1,1,1,2,1,3),_AlaDcbxDCPTCDCPName_Type())
alaDcbxDCPTCDCPName.setMaxAccess(_H)
if mibBuilder.loadTexts:alaDcbxDCPTCDCPName.setStatus(_A)
_AlaDcbxDCPTCMaximumBandwidth_Type=LldpXdot1dcbxTrafficClassBandwidthValue
_AlaDcbxDCPTCMaximumBandwidth_Object=MibTableColumn
alaDcbxDCPTCMaximumBandwidth=_AlaDcbxDCPTCMaximumBandwidth_Object((1,3,6,1,4,1,6486,801,1,2,1,72,1,1,1,2,1,4),_AlaDcbxDCPTCMaximumBandwidth_Type())
alaDcbxDCPTCMaximumBandwidth.setMaxAccess(_H)
if mibBuilder.loadTexts:alaDcbxDCPTCMaximumBandwidth.setStatus(_A)
_AlaDcbxDCPTCMinimumBandwidth_Type=LldpXdot1dcbxTrafficClassBandwidthValue
_AlaDcbxDCPTCMinimumBandwidth_Object=MibTableColumn
alaDcbxDCPTCMinimumBandwidth=_AlaDcbxDCPTCMinimumBandwidth_Object((1,3,6,1,4,1,6486,801,1,2,1,72,1,1,1,2,1,5),_AlaDcbxDCPTCMinimumBandwidth_Type())
alaDcbxDCPTCMinimumBandwidth.setMaxAccess(_H)
if mibBuilder.loadTexts:alaDcbxDCPTCMinimumBandwidth.setStatus(_A)
class _AlaDcbxDCPTCPFCLinkDelay_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(10,100))
_AlaDcbxDCPTCPFCLinkDelay_Type.__name__=_G
_AlaDcbxDCPTCPFCLinkDelay_Object=MibTableColumn
alaDcbxDCPTCPFCLinkDelay=_AlaDcbxDCPTCPFCLinkDelay_Object((1,3,6,1,4,1,6486,801,1,2,1,72,1,1,1,2,1,6),_AlaDcbxDCPTCPFCLinkDelay_Type())
alaDcbxDCPTCPFCLinkDelay.setMaxAccess(_H)
if mibBuilder.loadTexts:alaDcbxDCPTCPFCLinkDelay.setStatus(_A)
class _AlaDcbxDCPTCPFCLinkDelayUserModified_Type(TruthValue):defaultValue=2
_AlaDcbxDCPTCPFCLinkDelayUserModified_Type.__name__=_K
_AlaDcbxDCPTCPFCLinkDelayUserModified_Object=MibTableColumn
alaDcbxDCPTCPFCLinkDelayUserModified=_AlaDcbxDCPTCPFCLinkDelayUserModified_Object((1,3,6,1,4,1,6486,801,1,2,1,72,1,1,1,2,1,7),_AlaDcbxDCPTCPFCLinkDelayUserModified_Type())
alaDcbxDCPTCPFCLinkDelayUserModified.setMaxAccess(_C)
if mibBuilder.loadTexts:alaDcbxDCPTCPFCLinkDelayUserModified.setStatus(_A)
_AlaDcbxDCPTCPFCTrafficFlow_Type=DcbxTrafficFlow
_AlaDcbxDCPTCPFCTrafficFlow_Object=MibTableColumn
alaDcbxDCPTCPFCTrafficFlow=_AlaDcbxDCPTCPFCTrafficFlow_Object((1,3,6,1,4,1,6486,801,1,2,1,72,1,1,1,2,1,8),_AlaDcbxDCPTCPFCTrafficFlow_Type())
alaDcbxDCPTCPFCTrafficFlow.setMaxAccess(_H)
if mibBuilder.loadTexts:alaDcbxDCPTCPFCTrafficFlow.setStatus(_A)
_AlaDcbxDCPTCPriorityMap_Type=Unsigned32
_AlaDcbxDCPTCPriorityMap_Object=MibTableColumn
alaDcbxDCPTCPriorityMap=_AlaDcbxDCPTCPriorityMap_Object((1,3,6,1,4,1,6486,801,1,2,1,72,1,1,1,2,1,9),_AlaDcbxDCPTCPriorityMap_Type())
alaDcbxDCPTCPriorityMap.setMaxAccess(_C)
if mibBuilder.loadTexts:alaDcbxDCPTCPriorityMap.setStatus(_A)
_AlaDcbxDCPTCTrafficScheduler_Type=LldpXdot1dcbxTrafficSelectionAlgorithm
_AlaDcbxDCPTCTrafficScheduler_Object=MibTableColumn
alaDcbxDCPTCTrafficScheduler=_AlaDcbxDCPTCTrafficScheduler_Object((1,3,6,1,4,1,6486,801,1,2,1,72,1,1,1,2,1,10),_AlaDcbxDCPTCTrafficScheduler_Type())
alaDcbxDCPTCTrafficScheduler.setMaxAccess(_C)
if mibBuilder.loadTexts:alaDcbxDCPTCTrafficScheduler.setStatus(_A)
_AlaDcbxDCPTCRecommendedBandwidth_Type=LldpXdot1dcbxTrafficClassBandwidthValue
_AlaDcbxDCPTCRecommendedBandwidth_Object=MibTableColumn
alaDcbxDCPTCRecommendedBandwidth=_AlaDcbxDCPTCRecommendedBandwidth_Object((1,3,6,1,4,1,6486,801,1,2,1,72,1,1,1,2,1,11),_AlaDcbxDCPTCRecommendedBandwidth_Type())
alaDcbxDCPTCRecommendedBandwidth.setMaxAccess(_H)
if mibBuilder.loadTexts:alaDcbxDCPTCRecommendedBandwidth.setStatus(_A)
_AlaDcbxDCPTCRecommendedTrafficScheduler_Type=LldpXdot1dcbxTrafficSelectionAlgorithm
_AlaDcbxDCPTCRecommendedTrafficScheduler_Object=MibTableColumn
alaDcbxDCPTCRecommendedTrafficScheduler=_AlaDcbxDCPTCRecommendedTrafficScheduler_Object((1,3,6,1,4,1,6486,801,1,2,1,72,1,1,1,2,1,12),_AlaDcbxDCPTCRecommendedTrafficScheduler_Type())
alaDcbxDCPTCRecommendedTrafficScheduler.setMaxAccess(_C)
if mibBuilder.loadTexts:alaDcbxDCPTCRecommendedTrafficScheduler.setStatus(_A)
_AlaDcbxPortInstanceTable_Object=MibTable
alaDcbxPortInstanceTable=_AlaDcbxPortInstanceTable_Object((1,3,6,1,4,1,6486,801,1,2,1,72,1,1,1,3))
if mibBuilder.loadTexts:alaDcbxPortInstanceTable.setStatus(_A)
_AlaDcbxPortInstanceEntry_Object=MibTableRow
alaDcbxPortInstanceEntry=_AlaDcbxPortInstanceEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,72,1,1,1,3,1))
alaDcbxPortInstanceEntry.setIndexNames((0,_B,_T))
if mibBuilder.loadTexts:alaDcbxPortInstanceEntry.setStatus(_A)
_AlaDcbxPIIfIndex_Type=Unsigned32
_AlaDcbxPIIfIndex_Object=MibTableColumn
alaDcbxPIIfIndex=_AlaDcbxPIIfIndex_Object((1,3,6,1,4,1,6486,801,1,2,1,72,1,1,1,3,1,1),_AlaDcbxPIIfIndex_Type())
alaDcbxPIIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:alaDcbxPIIfIndex.setStatus(_A)
class _AlaDcbxPIDCBXAdmin_Type(VfcEnableState):defaultValue=1
_AlaDcbxPIDCBXAdmin_Type.__name__=_F
_AlaDcbxPIDCBXAdmin_Object=MibTableColumn
alaDcbxPIDCBXAdmin=_AlaDcbxPIDCBXAdmin_Object((1,3,6,1,4,1,6486,801,1,2,1,72,1,1,1,3,1,2),_AlaDcbxPIDCBXAdmin_Type())
alaDcbxPIDCBXAdmin.setMaxAccess(_D)
if mibBuilder.loadTexts:alaDcbxPIDCBXAdmin.setStatus(_A)
class _AlaDcbxPIDCBXOper_Type(VfcEnableState):defaultValue=0
_AlaDcbxPIDCBXOper_Type.__name__=_F
_AlaDcbxPIDCBXOper_Object=MibTableColumn
alaDcbxPIDCBXOper=_AlaDcbxPIDCBXOper_Object((1,3,6,1,4,1,6486,801,1,2,1,72,1,1,1,3,1,3),_AlaDcbxPIDCBXOper_Type())
alaDcbxPIDCBXOper.setMaxAccess(_C)
if mibBuilder.loadTexts:alaDcbxPIDCBXOper.setStatus(_A)
class _AlaDcbxPIAdminDCPId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_AlaDcbxPIAdminDCPId_Type.__name__=_G
_AlaDcbxPIAdminDCPId_Object=MibTableColumn
alaDcbxPIAdminDCPId=_AlaDcbxPIAdminDCPId_Object((1,3,6,1,4,1,6486,801,1,2,1,72,1,1,1,3,1,4),_AlaDcbxPIAdminDCPId_Type())
alaDcbxPIAdminDCPId.setMaxAccess(_D)
if mibBuilder.loadTexts:alaDcbxPIAdminDCPId.setStatus(_A)
class _AlaDcbxPIAdminDCPName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_AlaDcbxPIAdminDCPName_Type.__name__=_I
_AlaDcbxPIAdminDCPName_Object=MibTableColumn
alaDcbxPIAdminDCPName=_AlaDcbxPIAdminDCPName_Object((1,3,6,1,4,1,6486,801,1,2,1,72,1,1,1,3,1,5),_AlaDcbxPIAdminDCPName_Type())
alaDcbxPIAdminDCPName.setMaxAccess(_D)
if mibBuilder.loadTexts:alaDcbxPIAdminDCPName.setStatus(_A)
class _AlaDcbxPILocalModified_Type(TruthValue):defaultValue=2
_AlaDcbxPILocalModified_Type.__name__=_K
_AlaDcbxPILocalModified_Object=MibTableColumn
alaDcbxPILocalModified=_AlaDcbxPILocalModified_Object((1,3,6,1,4,1,6486,801,1,2,1,72,1,1,1,3,1,6),_AlaDcbxPILocalModified_Type())
alaDcbxPILocalModified.setMaxAccess(_C)
if mibBuilder.loadTexts:alaDcbxPILocalModified.setStatus(_A)
class _AlaDcbxPIPFCDefense_Type(VfcEnableState):defaultValue=1
_AlaDcbxPIPFCDefense_Type.__name__=_F
_AlaDcbxPIPFCDefense_Object=MibTableColumn
alaDcbxPIPFCDefense=_AlaDcbxPIPFCDefense_Object((1,3,6,1,4,1,6486,801,1,2,1,72,1,1,1,3,1,7),_AlaDcbxPIPFCDefense_Type())
alaDcbxPIPFCDefense.setMaxAccess(_D)
if mibBuilder.loadTexts:alaDcbxPIPFCDefense.setStatus(_A)
class _AlaDcbxPIPFCStatsClear_Type(VfcEnableState):defaultValue=0
_AlaDcbxPIPFCStatsClear_Type.__name__=_F
_AlaDcbxPIPFCStatsClear_Object=MibTableColumn
alaDcbxPIPFCStatsClear=_AlaDcbxPIPFCStatsClear_Object((1,3,6,1,4,1,6486,801,1,2,1,72,1,1,1,3,1,8),_AlaDcbxPIPFCStatsClear_Type())
alaDcbxPIPFCStatsClear.setMaxAccess(_D)
if mibBuilder.loadTexts:alaDcbxPIPFCStatsClear.setStatus(_A)
class _AlaDcbxPIStatus_Type(DcbxStatus):defaultValue=0
_AlaDcbxPIStatus_Type.__name__=_U
_AlaDcbxPIStatus_Object=MibTableColumn
alaDcbxPIStatus=_AlaDcbxPIStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,72,1,1,1,3,1,9),_AlaDcbxPIStatus_Type())
alaDcbxPIStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:alaDcbxPIStatus.setStatus(_A)
class _AlaDcbxPIActionTaken_Type(DcbxActionTaken):defaultValue=0
_AlaDcbxPIActionTaken_Type.__name__=_V
_AlaDcbxPIActionTaken_Object=MibTableColumn
alaDcbxPIActionTaken=_AlaDcbxPIActionTaken_Object((1,3,6,1,4,1,6486,801,1,2,1,72,1,1,1,3,1,10),_AlaDcbxPIActionTaken_Type())
alaDcbxPIActionTaken.setMaxAccess(_C)
if mibBuilder.loadTexts:alaDcbxPIActionTaken.setStatus(_A)
_AlaDcbxPIRowStatus_Type=RowStatus
_AlaDcbxPIRowStatus_Object=MibTableColumn
alaDcbxPIRowStatus=_AlaDcbxPIRowStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,72,1,1,1,3,1,11),_AlaDcbxPIRowStatus_Type())
alaDcbxPIRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:alaDcbxPIRowStatus.setStatus(_A)
_AlaDcbxPIDCBXVersion_Type=DcbxVersion
_AlaDcbxPIDCBXVersion_Object=MibTableColumn
alaDcbxPIDCBXVersion=_AlaDcbxPIDCBXVersion_Object((1,3,6,1,4,1,6486,801,1,2,1,72,1,1,1,3,1,12),_AlaDcbxPIDCBXVersion_Type())
alaDcbxPIDCBXVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:alaDcbxPIDCBXVersion.setStatus(_A)
_AlaDcbxPIDCBXOperVersion_Type=DcbxVersion
_AlaDcbxPIDCBXOperVersion_Object=MibTableColumn
alaDcbxPIDCBXOperVersion=_AlaDcbxPIDCBXOperVersion_Object((1,3,6,1,4,1,6486,801,1,2,1,72,1,1,1,3,1,13),_AlaDcbxPIDCBXOperVersion_Type())
alaDcbxPIDCBXOperVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:alaDcbxPIDCBXOperVersion.setStatus(_A)
_AlaDcbxPIDCBXRemoteOperVersion_Type=RemoteDcbxVersion
_AlaDcbxPIDCBXRemoteOperVersion_Object=MibTableColumn
alaDcbxPIDCBXRemoteOperVersion=_AlaDcbxPIDCBXRemoteOperVersion_Object((1,3,6,1,4,1,6486,801,1,2,1,72,1,1,1,3,1,14),_AlaDcbxPIDCBXRemoteOperVersion_Type())
alaDcbxPIDCBXRemoteOperVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:alaDcbxPIDCBXRemoteOperVersion.setStatus(_A)
_AlaDcbxPIPriorityTable_Object=MibTable
alaDcbxPIPriorityTable=_AlaDcbxPIPriorityTable_Object((1,3,6,1,4,1,6486,801,1,2,1,72,1,1,1,4))
if mibBuilder.loadTexts:alaDcbxPIPriorityTable.setStatus(_A)
_AlaDcbxPIPrioEntry_Object=MibTableRow
alaDcbxPIPrioEntry=_AlaDcbxPIPrioEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,72,1,1,1,4,1))
alaDcbxPIPrioEntry.setIndexNames((0,_B,_W),(0,_B,_X))
if mibBuilder.loadTexts:alaDcbxPIPrioEntry.setStatus(_A)
_AlaDcbxPIPrioIfIndex_Type=Unsigned32
_AlaDcbxPIPrioIfIndex_Object=MibTableColumn
alaDcbxPIPrioIfIndex=_AlaDcbxPIPrioIfIndex_Object((1,3,6,1,4,1,6486,801,1,2,1,72,1,1,1,4,1,1),_AlaDcbxPIPrioIfIndex_Type())
alaDcbxPIPrioIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:alaDcbxPIPrioIfIndex.setStatus(_A)
_AlaDcbxPIPrioPriority_Type=IEEE8021PriorityValue
_AlaDcbxPIPrioPriority_Object=MibTableColumn
alaDcbxPIPrioPriority=_AlaDcbxPIPrioPriority_Object((1,3,6,1,4,1,6486,801,1,2,1,72,1,1,1,4,1,2),_AlaDcbxPIPrioPriority_Type())
alaDcbxPIPrioPriority.setMaxAccess(_E)
if mibBuilder.loadTexts:alaDcbxPIPrioPriority.setStatus(_A)
_AlaDcbxPIPrioTC_Type=LldpXdot1dcbxTrafficClassValue
_AlaDcbxPIPrioTC_Object=MibTableColumn
alaDcbxPIPrioTC=_AlaDcbxPIPrioTC_Object((1,3,6,1,4,1,6486,801,1,2,1,72,1,1,1,4,1,3),_AlaDcbxPIPrioTC_Type())
alaDcbxPIPrioTC.setMaxAccess(_C)
if mibBuilder.loadTexts:alaDcbxPIPrioTC.setStatus(_A)
_AlaDcbxPIPrioPFCPacketsReceived_Type=Counter64
_AlaDcbxPIPrioPFCPacketsReceived_Object=MibTableColumn
alaDcbxPIPrioPFCPacketsReceived=_AlaDcbxPIPrioPFCPacketsReceived_Object((1,3,6,1,4,1,6486,801,1,2,1,72,1,1,1,4,1,4),_AlaDcbxPIPrioPFCPacketsReceived_Type())
alaDcbxPIPrioPFCPacketsReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:alaDcbxPIPrioPFCPacketsReceived.setStatus(_A)
_AlaDcbxPIPrioPFCPacketsTransmitted_Type=Counter64
_AlaDcbxPIPrioPFCPacketsTransmitted_Object=MibTableColumn
alaDcbxPIPrioPFCPacketsTransmitted=_AlaDcbxPIPrioPFCPacketsTransmitted_Object((1,3,6,1,4,1,6486,801,1,2,1,72,1,1,1,4,1,5),_AlaDcbxPIPrioPFCPacketsTransmitted_Type())
alaDcbxPIPrioPFCPacketsTransmitted.setMaxAccess(_C)
if mibBuilder.loadTexts:alaDcbxPIPrioPFCPacketsTransmitted.setStatus(_A)
_AlaDcbxPfcLLPrioritiesUsed_Type=Unsigned32
_AlaDcbxPfcLLPrioritiesUsed_Object=MibScalar
alaDcbxPfcLLPrioritiesUsed=_AlaDcbxPfcLLPrioritiesUsed_Object((1,3,6,1,4,1,6486,801,1,2,1,72,1,1,1,5),_AlaDcbxPfcLLPrioritiesUsed_Type())
alaDcbxPfcLLPrioritiesUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:alaDcbxPfcLLPrioritiesUsed.setStatus(_L)
_AlaDcbxPfcLLPrioritiesReserved_Type=Unsigned32
_AlaDcbxPfcLLPrioritiesReserved_Object=MibScalar
alaDcbxPfcLLPrioritiesReserved=_AlaDcbxPfcLLPrioritiesReserved_Object((1,3,6,1,4,1,6486,801,1,2,1,72,1,1,1,6),_AlaDcbxPfcLLPrioritiesReserved_Type())
alaDcbxPfcLLPrioritiesReserved.setMaxAccess(_C)
if mibBuilder.loadTexts:alaDcbxPfcLLPrioritiesReserved.setStatus(_L)
_AlaDcbxPfcLLPrioritiesAvailable_Type=Unsigned32
_AlaDcbxPfcLLPrioritiesAvailable_Object=MibScalar
alaDcbxPfcLLPrioritiesAvailable=_AlaDcbxPfcLLPrioritiesAvailable_Object((1,3,6,1,4,1,6486,801,1,2,1,72,1,1,1,7),_AlaDcbxPfcLLPrioritiesAvailable_Type())
alaDcbxPfcLLPrioritiesAvailable.setMaxAccess(_C)
if mibBuilder.loadTexts:alaDcbxPfcLLPrioritiesAvailable.setStatus(_L)
_AlaDcbxPfcUsageTable_Object=MibTable
alaDcbxPfcUsageTable=_AlaDcbxPfcUsageTable_Object((1,3,6,1,4,1,6486,801,1,2,1,72,1,1,1,8))
if mibBuilder.loadTexts:alaDcbxPfcUsageTable.setStatus(_A)
_AlaDcbxPfcUsageEntry_Object=MibTableRow
alaDcbxPfcUsageEntry=_AlaDcbxPfcUsageEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,72,1,1,1,8,1))
alaDcbxPfcUsageEntry.setIndexNames((0,_B,_Y))
if mibBuilder.loadTexts:alaDcbxPfcUsageEntry.setStatus(_A)
_AlaDcbxPfcUsageChassisId_Type=Unsigned32
_AlaDcbxPfcUsageChassisId_Object=MibTableColumn
alaDcbxPfcUsageChassisId=_AlaDcbxPfcUsageChassisId_Object((1,3,6,1,4,1,6486,801,1,2,1,72,1,1,1,8,1,1),_AlaDcbxPfcUsageChassisId_Type())
alaDcbxPfcUsageChassisId.setMaxAccess(_E)
if mibBuilder.loadTexts:alaDcbxPfcUsageChassisId.setStatus(_A)
_AlaDcbxPfcUsagePrioritiesUsed_Type=Unsigned32
_AlaDcbxPfcUsagePrioritiesUsed_Object=MibTableColumn
alaDcbxPfcUsagePrioritiesUsed=_AlaDcbxPfcUsagePrioritiesUsed_Object((1,3,6,1,4,1,6486,801,1,2,1,72,1,1,1,8,1,2),_AlaDcbxPfcUsagePrioritiesUsed_Type())
alaDcbxPfcUsagePrioritiesUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:alaDcbxPfcUsagePrioritiesUsed.setStatus(_A)
_AlaDcbxPfcUsagePrioritiesReserved_Type=Unsigned32
_AlaDcbxPfcUsagePrioritiesReserved_Object=MibTableColumn
alaDcbxPfcUsagePrioritiesReserved=_AlaDcbxPfcUsagePrioritiesReserved_Object((1,3,6,1,4,1,6486,801,1,2,1,72,1,1,1,8,1,3),_AlaDcbxPfcUsagePrioritiesReserved_Type())
alaDcbxPfcUsagePrioritiesReserved.setMaxAccess(_C)
if mibBuilder.loadTexts:alaDcbxPfcUsagePrioritiesReserved.setStatus(_A)
_AlaDcbxPfcUsagePrioritiesAvailable_Type=Unsigned32
_AlaDcbxPfcUsagePrioritiesAvailable_Object=MibTableColumn
alaDcbxPfcUsagePrioritiesAvailable=_AlaDcbxPfcUsagePrioritiesAvailable_Object((1,3,6,1,4,1,6486,801,1,2,1,72,1,1,1,8,1,4),_AlaDcbxPfcUsagePrioritiesAvailable_Type())
alaDcbxPfcUsagePrioritiesAvailable.setMaxAccess(_C)
if mibBuilder.loadTexts:alaDcbxPfcUsagePrioritiesAvailable.setStatus(_A)
_AlaXdot1dcbxAdminApplicationPriorityAppTable_Object=MibTable
alaXdot1dcbxAdminApplicationPriorityAppTable=_AlaXdot1dcbxAdminApplicationPriorityAppTable_Object((1,3,6,1,4,1,6486,801,1,2,1,72,1,1,1,9))
if mibBuilder.loadTexts:alaXdot1dcbxAdminApplicationPriorityAppTable.setStatus(_A)
_AlaXdot1dcbxAdminApplicationPriorityAppEntry_Object=MibTableRow
alaXdot1dcbxAdminApplicationPriorityAppEntry=_AlaXdot1dcbxAdminApplicationPriorityAppEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,72,1,1,1,9,1))
alaXdot1dcbxAdminApplicationPriorityAppEntry.setIndexNames((0,_O,_P),(0,_J,_N),(0,_J,_M))
if mibBuilder.loadTexts:alaXdot1dcbxAdminApplicationPriorityAppEntry.setStatus(_A)
_AlaXdot1dcbxAdminApplicationPriorityAEPriority_Type=IEEE8021PriorityValue
_AlaXdot1dcbxAdminApplicationPriorityAEPriority_Object=MibTableColumn
alaXdot1dcbxAdminApplicationPriorityAEPriority=_AlaXdot1dcbxAdminApplicationPriorityAEPriority_Object((1,3,6,1,4,1,6486,801,1,2,1,72,1,1,1,9,1,1),_AlaXdot1dcbxAdminApplicationPriorityAEPriority_Type())
alaXdot1dcbxAdminApplicationPriorityAEPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:alaXdot1dcbxAdminApplicationPriorityAEPriority.setStatus(_A)
_AlaXdot1dcbxAdminApplicationPriorityAppRowStatus_Type=RowStatus
_AlaXdot1dcbxAdminApplicationPriorityAppRowStatus_Object=MibTableColumn
alaXdot1dcbxAdminApplicationPriorityAppRowStatus=_AlaXdot1dcbxAdminApplicationPriorityAppRowStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,72,1,1,1,9,1,2),_AlaXdot1dcbxAdminApplicationPriorityAppRowStatus_Type())
alaXdot1dcbxAdminApplicationPriorityAppRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:alaXdot1dcbxAdminApplicationPriorityAppRowStatus.setStatus(_A)
_AlaDcbxConformance_ObjectIdentity=ObjectIdentity
alaDcbxConformance=_AlaDcbxConformance_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,72,1,1,2))
_AlcatelIND1DcbxMIBConformance_ObjectIdentity=ObjectIdentity
alcatelIND1DcbxMIBConformance=_AlcatelIND1DcbxMIBConformance_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,72,1,2))
if mibBuilder.loadTexts:alcatelIND1DcbxMIBConformance.setStatus(_A)
_AlcatelIND1DcbxMIBGroups_ObjectIdentity=ObjectIdentity
alcatelIND1DcbxMIBGroups=_AlcatelIND1DcbxMIBGroups_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,72,1,2,1))
if mibBuilder.loadTexts:alcatelIND1DcbxMIBGroups.setStatus(_A)
_AlcatelIND1DcbxMIBCompliances_ObjectIdentity=ObjectIdentity
alcatelIND1DcbxMIBCompliances=_AlcatelIND1DcbxMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,72,1,2,2))
if mibBuilder.loadTexts:alcatelIND1DcbxMIBCompliances.setStatus(_A)
alaDcbxDCProfileGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,72,1,2,1,1))
alaDcbxDCProfileGroup.setObjects(*((_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h)))
if mibBuilder.loadTexts:alaDcbxDCProfileGroup.setStatus(_A)
alaDcbxDCPTrafficClassGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,72,1,2,1,2))
alaDcbxDCPTrafficClassGroup.setObjects(*((_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r)))
if mibBuilder.loadTexts:alaDcbxDCPTrafficClassGroup.setStatus(_A)
alaDcbxPortInstanceGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,72,1,2,1,3))
alaDcbxPortInstanceGroup.setObjects(*((_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4)))
if mibBuilder.loadTexts:alaDcbxPortInstanceGroup.setStatus(_A)
alaDcbxPortInstancePriorityGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,72,1,2,1,4))
alaDcbxPortInstancePriorityGroup.setObjects(*((_B,_A5),(_B,_A6),(_B,_A7)))
if mibBuilder.loadTexts:alaDcbxPortInstancePriorityGroup.setStatus(_A)
alaDcbxPfcUsageGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,72,1,2,1,5))
alaDcbxPfcUsageGroup.setObjects(*((_B,_A8),(_B,_A9),(_B,_AA)))
if mibBuilder.loadTexts:alaDcbxPfcUsageGroup.setStatus(_A)
alaDcbxPfcUsageNewGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,72,1,2,1,6))
alaDcbxPfcUsageNewGroup.setObjects(*((_B,_AB),(_B,_AC),(_B,_AD)))
if mibBuilder.loadTexts:alaDcbxPfcUsageNewGroup.setStatus(_A)
alaXdot1dcbxAdminApplicationPriorityGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,72,1,2,1,7))
alaXdot1dcbxAdminApplicationPriorityGroup.setObjects(*((_B,_AE),(_B,_AF)))
if mibBuilder.loadTexts:alaXdot1dcbxAdminApplicationPriorityGroup.setStatus(_A)
alcatelIND1DcbxMIBCompliance=ModuleCompliance((1,3,6,1,4,1,6486,801,1,2,1,72,1,2,2,1))
alcatelIND1DcbxMIBCompliance.setObjects(*((_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL)))
if mibBuilder.loadTexts:alcatelIND1DcbxMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'DcbxTrafficFlow':DcbxTrafficFlow,'DcbxPriorityTCMap':DcbxPriorityTCMap,_U:DcbxStatus,_V:DcbxActionTaken,'DcbxTCsPresent':DcbxTCsPresent,'DcbxVersion':DcbxVersion,'RemoteDcbxVersion':RemoteDcbxVersion,'alcatelIND1DcbxMIB':alcatelIND1DcbxMIB,'alcatelIND1DcbxMIBObjects':alcatelIND1DcbxMIBObjects,'alaDcbxConfig':alaDcbxConfig,'alaDcbxDCProfileTable':alaDcbxDCProfileTable,'alaDcbxDCProfileEntry':alaDcbxDCProfileEntry,_Q:alaDcbxDCPId,_Z:alaDcbxDCPName,_a:alaDcbxDCPETSTrafficClassesSupported,_b:alaDcbxDCPPFCCap,_c:alaDcbxDCPPriorityTCMap,_d:alaDcbxDCPTemplateDCPId,_e:alaDcbxDCPTemplateDCPName,_f:alaDcbxDCPTCsPresent,_g:alaDcbxDCP8023xPauseReady,_h:alaDcbxDCPRowStatus,'alaDcbxDCPTrafficClassTable':alaDcbxDCPTrafficClassTable,'alaDcbxDCPTCEntry':alaDcbxDCPTCEntry,_R:alaDcbxDCPTCDCPId,_S:alaDcbxDCPTCTrafficClass,_i:alaDcbxDCPTCDCPName,_j:alaDcbxDCPTCMaximumBandwidth,_k:alaDcbxDCPTCMinimumBandwidth,_l:alaDcbxDCPTCPFCLinkDelay,_m:alaDcbxDCPTCPFCLinkDelayUserModified,_n:alaDcbxDCPTCPFCTrafficFlow,_o:alaDcbxDCPTCPriorityMap,_p:alaDcbxDCPTCTrafficScheduler,_q:alaDcbxDCPTCRecommendedBandwidth,_r:alaDcbxDCPTCRecommendedTrafficScheduler,'alaDcbxPortInstanceTable':alaDcbxPortInstanceTable,'alaDcbxPortInstanceEntry':alaDcbxPortInstanceEntry,_T:alaDcbxPIIfIndex,_s:alaDcbxPIDCBXAdmin,_t:alaDcbxPIDCBXOper,_u:alaDcbxPIAdminDCPId,_v:alaDcbxPIAdminDCPName,_w:alaDcbxPILocalModified,_x:alaDcbxPIPFCDefense,_y:alaDcbxPIPFCStatsClear,_z:alaDcbxPIStatus,_A0:alaDcbxPIActionTaken,_A1:alaDcbxPIRowStatus,_A2:alaDcbxPIDCBXVersion,_A3:alaDcbxPIDCBXOperVersion,_A4:alaDcbxPIDCBXRemoteOperVersion,'alaDcbxPIPriorityTable':alaDcbxPIPriorityTable,'alaDcbxPIPrioEntry':alaDcbxPIPrioEntry,_W:alaDcbxPIPrioIfIndex,_X:alaDcbxPIPrioPriority,_A5:alaDcbxPIPrioTC,_A6:alaDcbxPIPrioPFCPacketsReceived,_A7:alaDcbxPIPrioPFCPacketsTransmitted,_A8:alaDcbxPfcLLPrioritiesUsed,_A9:alaDcbxPfcLLPrioritiesReserved,_AA:alaDcbxPfcLLPrioritiesAvailable,'alaDcbxPfcUsageTable':alaDcbxPfcUsageTable,'alaDcbxPfcUsageEntry':alaDcbxPfcUsageEntry,_Y:alaDcbxPfcUsageChassisId,_AB:alaDcbxPfcUsagePrioritiesUsed,_AC:alaDcbxPfcUsagePrioritiesReserved,_AD:alaDcbxPfcUsagePrioritiesAvailable,'alaXdot1dcbxAdminApplicationPriorityAppTable':alaXdot1dcbxAdminApplicationPriorityAppTable,'alaXdot1dcbxAdminApplicationPriorityAppEntry':alaXdot1dcbxAdminApplicationPriorityAppEntry,_AE:alaXdot1dcbxAdminApplicationPriorityAEPriority,_AF:alaXdot1dcbxAdminApplicationPriorityAppRowStatus,'alaDcbxConformance':alaDcbxConformance,'alcatelIND1DcbxMIBConformance':alcatelIND1DcbxMIBConformance,'alcatelIND1DcbxMIBGroups':alcatelIND1DcbxMIBGroups,_AG:alaDcbxDCProfileGroup,_AH:alaDcbxDCPTrafficClassGroup,_AI:alaDcbxPortInstanceGroup,_AJ:alaDcbxPortInstancePriorityGroup,_AK:alaDcbxPfcUsageGroup,_AL:alaDcbxPfcUsageNewGroup,'alaXdot1dcbxAdminApplicationPriorityGroup':alaXdot1dcbxAdminApplicationPriorityGroup,'alcatelIND1DcbxMIBCompliances':alcatelIND1DcbxMIBCompliances,'alcatelIND1DcbxMIBCompliance':alcatelIND1DcbxMIBCompliance})