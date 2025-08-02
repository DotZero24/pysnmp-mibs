_Ak='mauIfGrpPerPCSLaneStats'
_Aj='mauIfGrpTimeSync'
_Ai='mauIfGrpEEE'
_Ah='mauIfGrpSNR'
_Ag='mauIfGrpFEC'
_Af='ifMauNotifications'
_Ae='mauIfGrpAutoNeg1000Mbps'
_Ad='mauIfGrpAutoNeg2'
_Ac='mauIfGrpJack'
_Ab='mauIfGrpHCStats'
_Aa='mauIfGrpHighCapacity'
_AZ='mauIfGrpBasic'
_AY='rpMauNotifications'
_AX='mauRpGrpJack'
_AW='mauRpGrp100Mbs'
_AV='mauRpGrpBasic'
_AU='ifMauJabberTrap'
_AT='rpMauJabberTrap'
_AS='ifMauPCStoPHYLaneMapping'
_AR='ifMauBIPErrorCount'
_AQ='ifMauPPLFECUncorrectableBlocks'
_AP='ifMauPPLFECCorrectedBlocks'
_AO='ifMauTimeSyncDelayRXmin'
_AN='ifMauTimeSyncDelayRXmax'
_AM='ifMauTimeSyncDelayTXmin'
_AL='ifMauTimeSyncDelayTXmax'
_AK='ifMauTimeSyncCapabilityRX'
_AJ='ifMauTimeSyncCapabilityTX'
_AI='ifMauEEELPFastRetrainCount'
_AH='ifMauEEELDFastRetrainCount'
_AG='ifMauEEESupportList'
_AF='ifMauSNROpMarginChnlD'
_AE='ifMauSNROpMarginChnlC'
_AD='ifMauSNROpMarginChnlB'
_AC='ifMauSNROpMarginChnlA'
_AB='ifMauFECUnCorrectableBlocks'
_AA='ifMauFECCorrectedBlocks'
_A9='ifMauFECMode'
_A8='ifMauFECAbility'
_A7='ifMauPCSCodingViolations'
_A6='ifMauHCFalseCarriers'
_A5='ifMauAutoNegRemoteFaultReceived'
_A4='ifMauAutoNegRemoteFaultAdvertised'
_A3='ifMauAutoNegRestart'
_A2='ifMauAutoNegCapReceivedBits'
_A1='ifMauAutoNegCapAdvertisedBits'
_A0='ifMauAutoNegCapabilityBits'
_z='ifMauAutoNegConfig'
_y='ifMauAutoNegRemoteSignaling'
_x='ifMauAutoNegAdminStatus'
_w='ifMauAutoNegSupported'
_v='ifMauDefaultType'
_u='ifMauTypeListBits'
_t='ifMauFalseCarriers'
_s='ifJackType'
_r='dot3Placeholder'
_q='ifMauJabberingStateEnters'
_p='ifMauMediaAvailableStateExits'
_o='ifMauMediaAvailable'
_n='ifMauStatus'
_m='ifMauType'
_l='rpJackType'
_k='rpMauFalseCarriers'
_j='rpMauJabberingStateEnters'
_i='rpMauMediaAvailableStateExits'
_h='rpMauMediaAvailable'
_g='rpMauStatus'
_f='rpMauType'
_e='autoNegError'
_d='linkFailure'
_c='offline'
_b='noError'
_a='ifPCSLaneIndex'
_Z='ifJackIndex'
_Y='deprecated'
_X='enabled'
_W='rpJackIndex'
_V='jabbering'
_U='noJabber'
_T='shutdown'
_S='standby'
_R='operational'
_Q='Unsigned32'
_P='ifMauJabberState'
_O='rpMauJabberState'
_N='disabled'
_M='rpMauIndex'
_L='rpMauPortIndex'
_K='rpMauGroupIndex'
_J='ifMauIndex'
_I='ifMauIfIndex'
_H='other'
_G='unknown'
_F='read-write'
_E='not-accessible'
_D='Integer32'
_C='read-only'
_B='IEEE8023-MAU-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
IANAifJackType,IANAifMauAutoNegCapBits,IANAifMauMediaAvailable,IANAifMauTypeListBits=mibBuilder.importSymbols('IANA-MAU-MIB','IANAifJackType','IANAifMauAutoNegCapBits','IANAifMauMediaAvailable','IANAifMauTypeListBits')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,org=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_Q,'iso','org')
AutonomousType,DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','AutonomousType','DisplayString','PhysAddress','TextualConvention','TruthValue')
ieee8023mauMIB=ModuleIdentity((1,3,111,2,802,3,1,13))
if mibBuilder.loadTexts:ieee8023mauMIB.setRevisions(('2013-04-11 00:00','2011-02-02 00:00'))
_Ieee8023snmpDot3MauMgt_ObjectIdentity=ObjectIdentity
ieee8023snmpDot3MauMgt=_Ieee8023snmpDot3MauMgt_ObjectIdentity((1,3,111,2,802,3,1,13,1))
_SnmpDot3MauTraps_ObjectIdentity=ObjectIdentity
snmpDot3MauTraps=_SnmpDot3MauTraps_ObjectIdentity((1,3,111,2,802,3,1,13,1,0))
_Dot3RpMauBasicGroup_ObjectIdentity=ObjectIdentity
dot3RpMauBasicGroup=_Dot3RpMauBasicGroup_ObjectIdentity((1,3,111,2,802,3,1,13,1,1))
_RpMauTable_Object=MibTable
rpMauTable=_RpMauTable_Object((1,3,111,2,802,3,1,13,1,1,1))
if mibBuilder.loadTexts:rpMauTable.setStatus(_A)
_RpMauEntry_Object=MibTableRow
rpMauEntry=_RpMauEntry_Object((1,3,111,2,802,3,1,13,1,1,1,1))
rpMauEntry.setIndexNames((0,_B,_K),(0,_B,_L),(0,_B,_M))
if mibBuilder.loadTexts:rpMauEntry.setStatus(_A)
class _RpMauGroupIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_RpMauGroupIndex_Type.__name__=_D
_RpMauGroupIndex_Object=MibTableColumn
rpMauGroupIndex=_RpMauGroupIndex_Object((1,3,111,2,802,3,1,13,1,1,1,1,1),_RpMauGroupIndex_Type())
rpMauGroupIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:rpMauGroupIndex.setStatus(_A)
class _RpMauPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_RpMauPortIndex_Type.__name__=_D
_RpMauPortIndex_Object=MibTableColumn
rpMauPortIndex=_RpMauPortIndex_Object((1,3,111,2,802,3,1,13,1,1,1,1,2),_RpMauPortIndex_Type())
rpMauPortIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:rpMauPortIndex.setStatus(_A)
class _RpMauIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_RpMauIndex_Type.__name__=_D
_RpMauIndex_Object=MibTableColumn
rpMauIndex=_RpMauIndex_Object((1,3,111,2,802,3,1,13,1,1,1,1,3),_RpMauIndex_Type())
rpMauIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:rpMauIndex.setStatus(_A)
_RpMauType_Type=AutonomousType
_RpMauType_Object=MibTableColumn
rpMauType=_RpMauType_Object((1,3,111,2,802,3,1,13,1,1,1,1,4),_RpMauType_Type())
rpMauType.setMaxAccess(_C)
if mibBuilder.loadTexts:rpMauType.setStatus(_A)
class _RpMauStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_H,1),(_G,2),(_R,3),(_S,4),(_T,5),('reset',6)))
_RpMauStatus_Type.__name__=_D
_RpMauStatus_Object=MibTableColumn
rpMauStatus=_RpMauStatus_Object((1,3,111,2,802,3,1,13,1,1,1,1,5),_RpMauStatus_Type())
rpMauStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:rpMauStatus.setStatus(_A)
_RpMauMediaAvailable_Type=IANAifMauMediaAvailable
_RpMauMediaAvailable_Object=MibTableColumn
rpMauMediaAvailable=_RpMauMediaAvailable_Object((1,3,111,2,802,3,1,13,1,1,1,1,6),_RpMauMediaAvailable_Type())
rpMauMediaAvailable.setMaxAccess(_C)
if mibBuilder.loadTexts:rpMauMediaAvailable.setStatus(_A)
_RpMauMediaAvailableStateExits_Type=Counter32
_RpMauMediaAvailableStateExits_Object=MibTableColumn
rpMauMediaAvailableStateExits=_RpMauMediaAvailableStateExits_Object((1,3,111,2,802,3,1,13,1,1,1,1,7),_RpMauMediaAvailableStateExits_Type())
rpMauMediaAvailableStateExits.setMaxAccess(_C)
if mibBuilder.loadTexts:rpMauMediaAvailableStateExits.setStatus(_A)
class _RpMauJabberState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_H,1),(_G,2),(_U,3),(_V,4)))
_RpMauJabberState_Type.__name__=_D
_RpMauJabberState_Object=MibTableColumn
rpMauJabberState=_RpMauJabberState_Object((1,3,111,2,802,3,1,13,1,1,1,1,8),_RpMauJabberState_Type())
rpMauJabberState.setMaxAccess(_C)
if mibBuilder.loadTexts:rpMauJabberState.setStatus(_A)
_RpMauJabberingStateEnters_Type=Counter32
_RpMauJabberingStateEnters_Object=MibTableColumn
rpMauJabberingStateEnters=_RpMauJabberingStateEnters_Object((1,3,111,2,802,3,1,13,1,1,1,1,9),_RpMauJabberingStateEnters_Type())
rpMauJabberingStateEnters.setMaxAccess(_C)
if mibBuilder.loadTexts:rpMauJabberingStateEnters.setStatus(_A)
_RpMauFalseCarriers_Type=Counter32
_RpMauFalseCarriers_Object=MibTableColumn
rpMauFalseCarriers=_RpMauFalseCarriers_Object((1,3,111,2,802,3,1,13,1,1,1,1,10),_RpMauFalseCarriers_Type())
rpMauFalseCarriers.setMaxAccess(_C)
if mibBuilder.loadTexts:rpMauFalseCarriers.setStatus(_A)
_RpJackTable_Object=MibTable
rpJackTable=_RpJackTable_Object((1,3,111,2,802,3,1,13,1,1,2))
if mibBuilder.loadTexts:rpJackTable.setStatus(_A)
_RpJackEntry_Object=MibTableRow
rpJackEntry=_RpJackEntry_Object((1,3,111,2,802,3,1,13,1,1,2,1))
rpJackEntry.setIndexNames((0,_B,_K),(0,_B,_L),(0,_B,_M),(0,_B,_W))
if mibBuilder.loadTexts:rpJackEntry.setStatus(_A)
class _RpJackIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_RpJackIndex_Type.__name__=_D
_RpJackIndex_Object=MibTableColumn
rpJackIndex=_RpJackIndex_Object((1,3,111,2,802,3,1,13,1,1,2,1,1),_RpJackIndex_Type())
rpJackIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:rpJackIndex.setStatus(_A)
_RpJackType_Type=IANAifJackType
_RpJackType_Object=MibTableColumn
rpJackType=_RpJackType_Object((1,3,111,2,802,3,1,13,1,1,2,1,2),_RpJackType_Type())
rpJackType.setMaxAccess(_C)
if mibBuilder.loadTexts:rpJackType.setStatus(_A)
_Dot3IfMauBasicGroup_ObjectIdentity=ObjectIdentity
dot3IfMauBasicGroup=_Dot3IfMauBasicGroup_ObjectIdentity((1,3,111,2,802,3,1,13,1,2))
_IfMauTable_Object=MibTable
ifMauTable=_IfMauTable_Object((1,3,111,2,802,3,1,13,1,2,1))
if mibBuilder.loadTexts:ifMauTable.setStatus(_A)
_IfMauEntry_Object=MibTableRow
ifMauEntry=_IfMauEntry_Object((1,3,111,2,802,3,1,13,1,2,1,1))
ifMauEntry.setIndexNames((0,_B,_I),(0,_B,_J))
if mibBuilder.loadTexts:ifMauEntry.setStatus(_A)
_IfMauIfIndex_Type=InterfaceIndex
_IfMauIfIndex_Object=MibTableColumn
ifMauIfIndex=_IfMauIfIndex_Object((1,3,111,2,802,3,1,13,1,2,1,1,1),_IfMauIfIndex_Type())
ifMauIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:ifMauIfIndex.setStatus(_A)
class _IfMauIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_IfMauIndex_Type.__name__=_D
_IfMauIndex_Object=MibTableColumn
ifMauIndex=_IfMauIndex_Object((1,3,111,2,802,3,1,13,1,2,1,1,2),_IfMauIndex_Type())
ifMauIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:ifMauIndex.setStatus(_A)
_IfMauType_Type=AutonomousType
_IfMauType_Object=MibTableColumn
ifMauType=_IfMauType_Object((1,3,111,2,802,3,1,13,1,2,1,1,3),_IfMauType_Type())
ifMauType.setMaxAccess(_C)
if mibBuilder.loadTexts:ifMauType.setStatus(_A)
class _IfMauStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_H,1),(_G,2),(_R,3),(_S,4),(_T,5),('reset',6)))
_IfMauStatus_Type.__name__=_D
_IfMauStatus_Object=MibTableColumn
ifMauStatus=_IfMauStatus_Object((1,3,111,2,802,3,1,13,1,2,1,1,4),_IfMauStatus_Type())
ifMauStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:ifMauStatus.setStatus(_A)
_IfMauMediaAvailable_Type=IANAifMauMediaAvailable
_IfMauMediaAvailable_Object=MibTableColumn
ifMauMediaAvailable=_IfMauMediaAvailable_Object((1,3,111,2,802,3,1,13,1,2,1,1,5),_IfMauMediaAvailable_Type())
ifMauMediaAvailable.setMaxAccess(_C)
if mibBuilder.loadTexts:ifMauMediaAvailable.setStatus(_A)
_IfMauMediaAvailableStateExits_Type=Counter32
_IfMauMediaAvailableStateExits_Object=MibTableColumn
ifMauMediaAvailableStateExits=_IfMauMediaAvailableStateExits_Object((1,3,111,2,802,3,1,13,1,2,1,1,6),_IfMauMediaAvailableStateExits_Type())
ifMauMediaAvailableStateExits.setMaxAccess(_C)
if mibBuilder.loadTexts:ifMauMediaAvailableStateExits.setStatus(_A)
class _IfMauJabberState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_H,1),(_G,2),(_U,3),(_V,4)))
_IfMauJabberState_Type.__name__=_D
_IfMauJabberState_Object=MibTableColumn
ifMauJabberState=_IfMauJabberState_Object((1,3,111,2,802,3,1,13,1,2,1,1,7),_IfMauJabberState_Type())
ifMauJabberState.setMaxAccess(_C)
if mibBuilder.loadTexts:ifMauJabberState.setStatus(_A)
_IfMauJabberingStateEnters_Type=Counter32
_IfMauJabberingStateEnters_Object=MibTableColumn
ifMauJabberingStateEnters=_IfMauJabberingStateEnters_Object((1,3,111,2,802,3,1,13,1,2,1,1,8),_IfMauJabberingStateEnters_Type())
ifMauJabberingStateEnters.setMaxAccess(_C)
if mibBuilder.loadTexts:ifMauJabberingStateEnters.setStatus(_A)
_IfMauFalseCarriers_Type=Counter32
_IfMauFalseCarriers_Object=MibTableColumn
ifMauFalseCarriers=_IfMauFalseCarriers_Object((1,3,111,2,802,3,1,13,1,2,1,1,9),_IfMauFalseCarriers_Type())
ifMauFalseCarriers.setMaxAccess(_C)
if mibBuilder.loadTexts:ifMauFalseCarriers.setStatus(_A)
_IfMauDefaultType_Type=AutonomousType
_IfMauDefaultType_Object=MibTableColumn
ifMauDefaultType=_IfMauDefaultType_Object((1,3,111,2,802,3,1,13,1,2,1,1,10),_IfMauDefaultType_Type())
ifMauDefaultType.setMaxAccess(_F)
if mibBuilder.loadTexts:ifMauDefaultType.setStatus(_A)
_IfMauAutoNegSupported_Type=TruthValue
_IfMauAutoNegSupported_Object=MibTableColumn
ifMauAutoNegSupported=_IfMauAutoNegSupported_Object((1,3,111,2,802,3,1,13,1,2,1,1,11),_IfMauAutoNegSupported_Type())
ifMauAutoNegSupported.setMaxAccess(_C)
if mibBuilder.loadTexts:ifMauAutoNegSupported.setStatus(_A)
_IfMauTypeListBits_Type=IANAifMauTypeListBits
_IfMauTypeListBits_Object=MibTableColumn
ifMauTypeListBits=_IfMauTypeListBits_Object((1,3,111,2,802,3,1,13,1,2,1,1,12),_IfMauTypeListBits_Type())
ifMauTypeListBits.setMaxAccess(_C)
if mibBuilder.loadTexts:ifMauTypeListBits.setStatus(_A)
_IfMauHCFalseCarriers_Type=Counter64
_IfMauHCFalseCarriers_Object=MibTableColumn
ifMauHCFalseCarriers=_IfMauHCFalseCarriers_Object((1,3,111,2,802,3,1,13,1,2,1,1,13),_IfMauHCFalseCarriers_Type())
ifMauHCFalseCarriers.setMaxAccess(_C)
if mibBuilder.loadTexts:ifMauHCFalseCarriers.setStatus(_A)
_IfMauPCSCodingViolations_Type=Counter64
_IfMauPCSCodingViolations_Object=MibTableColumn
ifMauPCSCodingViolations=_IfMauPCSCodingViolations_Object((1,3,111,2,802,3,1,13,1,2,1,1,14),_IfMauPCSCodingViolations_Type())
ifMauPCSCodingViolations.setMaxAccess(_C)
if mibBuilder.loadTexts:ifMauPCSCodingViolations.setStatus(_A)
class _IfMauFECAbility_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),('supported',2),('notsupported',3)))
_IfMauFECAbility_Type.__name__=_D
_IfMauFECAbility_Object=MibTableColumn
ifMauFECAbility=_IfMauFECAbility_Object((1,3,111,2,802,3,1,13,1,2,1,1,15),_IfMauFECAbility_Type())
ifMauFECAbility.setMaxAccess(_C)
if mibBuilder.loadTexts:ifMauFECAbility.setStatus(_A)
class _IfMauFECMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_N,2),(_X,3)))
_IfMauFECMode_Type.__name__=_D
_IfMauFECMode_Object=MibTableColumn
ifMauFECMode=_IfMauFECMode_Object((1,3,111,2,802,3,1,13,1,2,1,1,16),_IfMauFECMode_Type())
ifMauFECMode.setMaxAccess(_F)
if mibBuilder.loadTexts:ifMauFECMode.setStatus(_A)
_IfMauFECCorrectedBlocks_Type=Counter64
_IfMauFECCorrectedBlocks_Object=MibTableColumn
ifMauFECCorrectedBlocks=_IfMauFECCorrectedBlocks_Object((1,3,111,2,802,3,1,13,1,2,1,1,17),_IfMauFECCorrectedBlocks_Type())
ifMauFECCorrectedBlocks.setMaxAccess(_C)
if mibBuilder.loadTexts:ifMauFECCorrectedBlocks.setStatus(_Y)
_IfMauFECUnCorrectableBlocks_Type=Counter64
_IfMauFECUnCorrectableBlocks_Object=MibTableColumn
ifMauFECUnCorrectableBlocks=_IfMauFECUnCorrectableBlocks_Object((1,3,111,2,802,3,1,13,1,2,1,1,18),_IfMauFECUnCorrectableBlocks_Type())
ifMauFECUnCorrectableBlocks.setMaxAccess(_C)
if mibBuilder.loadTexts:ifMauFECUnCorrectableBlocks.setStatus(_Y)
class _IfMauSNROpMarginChnlA_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-127,127))
_IfMauSNROpMarginChnlA_Type.__name__=_D
_IfMauSNROpMarginChnlA_Object=MibTableColumn
ifMauSNROpMarginChnlA=_IfMauSNROpMarginChnlA_Object((1,3,111,2,802,3,1,13,1,2,1,1,19),_IfMauSNROpMarginChnlA_Type())
ifMauSNROpMarginChnlA.setMaxAccess(_C)
if mibBuilder.loadTexts:ifMauSNROpMarginChnlA.setStatus(_A)
class _IfMauSNROpMarginChnlB_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-127,127))
_IfMauSNROpMarginChnlB_Type.__name__=_D
_IfMauSNROpMarginChnlB_Object=MibTableColumn
ifMauSNROpMarginChnlB=_IfMauSNROpMarginChnlB_Object((1,3,111,2,802,3,1,13,1,2,1,1,20),_IfMauSNROpMarginChnlB_Type())
ifMauSNROpMarginChnlB.setMaxAccess(_C)
if mibBuilder.loadTexts:ifMauSNROpMarginChnlB.setStatus(_A)
class _IfMauSNROpMarginChnlC_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-127,127))
_IfMauSNROpMarginChnlC_Type.__name__=_D
_IfMauSNROpMarginChnlC_Object=MibTableColumn
ifMauSNROpMarginChnlC=_IfMauSNROpMarginChnlC_Object((1,3,111,2,802,3,1,13,1,2,1,1,21),_IfMauSNROpMarginChnlC_Type())
ifMauSNROpMarginChnlC.setMaxAccess(_C)
if mibBuilder.loadTexts:ifMauSNROpMarginChnlC.setStatus(_A)
class _IfMauSNROpMarginChnlD_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-127,127))
_IfMauSNROpMarginChnlD_Type.__name__=_D
_IfMauSNROpMarginChnlD_Object=MibTableColumn
ifMauSNROpMarginChnlD=_IfMauSNROpMarginChnlD_Object((1,3,111,2,802,3,1,13,1,2,1,1,22),_IfMauSNROpMarginChnlD_Type())
ifMauSNROpMarginChnlD.setMaxAccess(_C)
if mibBuilder.loadTexts:ifMauSNROpMarginChnlD.setStatus(_A)
_IfMauEEESupportList_Type=IANAifMauTypeListBits
_IfMauEEESupportList_Object=MibTableColumn
ifMauEEESupportList=_IfMauEEESupportList_Object((1,3,111,2,802,3,1,13,1,2,1,1,23),_IfMauEEESupportList_Type())
ifMauEEESupportList.setMaxAccess(_C)
if mibBuilder.loadTexts:ifMauEEESupportList.setStatus(_A)
_IfMauEEELDFastRetrainCount_Type=Counter32
_IfMauEEELDFastRetrainCount_Object=MibTableColumn
ifMauEEELDFastRetrainCount=_IfMauEEELDFastRetrainCount_Object((1,3,111,2,802,3,1,13,1,2,1,1,24),_IfMauEEELDFastRetrainCount_Type())
ifMauEEELDFastRetrainCount.setMaxAccess(_C)
if mibBuilder.loadTexts:ifMauEEELDFastRetrainCount.setStatus(_A)
_IfMauEEELPFastRetrainCount_Type=Counter32
_IfMauEEELPFastRetrainCount_Object=MibTableColumn
ifMauEEELPFastRetrainCount=_IfMauEEELPFastRetrainCount_Object((1,3,111,2,802,3,1,13,1,2,1,1,25),_IfMauEEELPFastRetrainCount_Type())
ifMauEEELPFastRetrainCount.setMaxAccess(_C)
if mibBuilder.loadTexts:ifMauEEELPFastRetrainCount.setStatus(_A)
_IfMauTimeSyncCapabilityTX_Type=TruthValue
_IfMauTimeSyncCapabilityTX_Object=MibTableColumn
ifMauTimeSyncCapabilityTX=_IfMauTimeSyncCapabilityTX_Object((1,3,111,2,802,3,1,13,1,2,1,1,26),_IfMauTimeSyncCapabilityTX_Type())
ifMauTimeSyncCapabilityTX.setMaxAccess(_C)
if mibBuilder.loadTexts:ifMauTimeSyncCapabilityTX.setStatus(_A)
_IfMauTimeSyncCapabilityRX_Type=TruthValue
_IfMauTimeSyncCapabilityRX_Object=MibTableColumn
ifMauTimeSyncCapabilityRX=_IfMauTimeSyncCapabilityRX_Object((1,3,111,2,802,3,1,13,1,2,1,1,27),_IfMauTimeSyncCapabilityRX_Type())
ifMauTimeSyncCapabilityRX.setMaxAccess(_C)
if mibBuilder.loadTexts:ifMauTimeSyncCapabilityRX.setStatus(_A)
_IfMauTimeSyncDelayTXmax_Type=Integer32
_IfMauTimeSyncDelayTXmax_Object=MibTableColumn
ifMauTimeSyncDelayTXmax=_IfMauTimeSyncDelayTXmax_Object((1,3,111,2,802,3,1,13,1,2,1,1,28),_IfMauTimeSyncDelayTXmax_Type())
ifMauTimeSyncDelayTXmax.setMaxAccess(_C)
if mibBuilder.loadTexts:ifMauTimeSyncDelayTXmax.setStatus(_A)
_IfMauTimeSyncDelayTXmin_Type=Integer32
_IfMauTimeSyncDelayTXmin_Object=MibTableColumn
ifMauTimeSyncDelayTXmin=_IfMauTimeSyncDelayTXmin_Object((1,3,111,2,802,3,1,13,1,2,1,1,29),_IfMauTimeSyncDelayTXmin_Type())
ifMauTimeSyncDelayTXmin.setMaxAccess(_C)
if mibBuilder.loadTexts:ifMauTimeSyncDelayTXmin.setStatus(_A)
_IfMauTimeSyncDelayRXmax_Type=Integer32
_IfMauTimeSyncDelayRXmax_Object=MibTableColumn
ifMauTimeSyncDelayRXmax=_IfMauTimeSyncDelayRXmax_Object((1,3,111,2,802,3,1,13,1,2,1,1,30),_IfMauTimeSyncDelayRXmax_Type())
ifMauTimeSyncDelayRXmax.setMaxAccess(_C)
if mibBuilder.loadTexts:ifMauTimeSyncDelayRXmax.setStatus(_A)
_IfMauTimeSyncDelayRXmin_Type=Integer32
_IfMauTimeSyncDelayRXmin_Object=MibTableColumn
ifMauTimeSyncDelayRXmin=_IfMauTimeSyncDelayRXmin_Object((1,3,111,2,802,3,1,13,1,2,1,1,31),_IfMauTimeSyncDelayRXmin_Type())
ifMauTimeSyncDelayRXmin.setMaxAccess(_C)
if mibBuilder.loadTexts:ifMauTimeSyncDelayRXmin.setStatus(_A)
_IfJackTable_Object=MibTable
ifJackTable=_IfJackTable_Object((1,3,111,2,802,3,1,13,1,2,2))
if mibBuilder.loadTexts:ifJackTable.setStatus(_A)
_IfJackEntry_Object=MibTableRow
ifJackEntry=_IfJackEntry_Object((1,3,111,2,802,3,1,13,1,2,2,1))
ifJackEntry.setIndexNames((0,_B,_I),(0,_B,_J),(0,_B,_Z))
if mibBuilder.loadTexts:ifJackEntry.setStatus(_A)
class _IfJackIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_IfJackIndex_Type.__name__=_D
_IfJackIndex_Object=MibTableColumn
ifJackIndex=_IfJackIndex_Object((1,3,111,2,802,3,1,13,1,2,2,1,1),_IfJackIndex_Type())
ifJackIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:ifJackIndex.setStatus(_A)
_IfJackType_Type=IANAifJackType
_IfJackType_Object=MibTableColumn
ifJackType=_IfJackType_Object((1,3,111,2,802,3,1,13,1,2,2,1,2),_IfJackType_Type())
ifJackType.setMaxAccess(_C)
if mibBuilder.loadTexts:ifJackType.setStatus(_A)
_IfMauPerPCSLaneStatsTable_Object=MibTable
ifMauPerPCSLaneStatsTable=_IfMauPerPCSLaneStatsTable_Object((1,3,111,2,802,3,1,13,1,2,3))
if mibBuilder.loadTexts:ifMauPerPCSLaneStatsTable.setStatus(_A)
_IfMauPerPCSLaneStatsEntry_Object=MibTableRow
ifMauPerPCSLaneStatsEntry=_IfMauPerPCSLaneStatsEntry_Object((1,3,111,2,802,3,1,13,1,2,3,1))
ifMauPerPCSLaneStatsEntry.setIndexNames((0,_B,_I),(0,_B,_J),(0,_B,_a))
if mibBuilder.loadTexts:ifMauPerPCSLaneStatsEntry.setStatus(_A)
class _IfPCSLaneIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_IfPCSLaneIndex_Type.__name__=_Q
_IfPCSLaneIndex_Object=MibTableColumn
ifPCSLaneIndex=_IfPCSLaneIndex_Object((1,3,111,2,802,3,1,13,1,2,3,1,1),_IfPCSLaneIndex_Type())
ifPCSLaneIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:ifPCSLaneIndex.setStatus(_A)
_IfMauPPLFECCorrectedBlocks_Type=Counter64
_IfMauPPLFECCorrectedBlocks_Object=MibTableColumn
ifMauPPLFECCorrectedBlocks=_IfMauPPLFECCorrectedBlocks_Object((1,3,111,2,802,3,1,13,1,2,3,1,2),_IfMauPPLFECCorrectedBlocks_Type())
ifMauPPLFECCorrectedBlocks.setMaxAccess(_C)
if mibBuilder.loadTexts:ifMauPPLFECCorrectedBlocks.setStatus(_A)
_IfMauPPLFECUncorrectableBlocks_Type=Counter64
_IfMauPPLFECUncorrectableBlocks_Object=MibTableColumn
ifMauPPLFECUncorrectableBlocks=_IfMauPPLFECUncorrectableBlocks_Object((1,3,111,2,802,3,1,13,1,2,3,1,3),_IfMauPPLFECUncorrectableBlocks_Type())
ifMauPPLFECUncorrectableBlocks.setMaxAccess(_C)
if mibBuilder.loadTexts:ifMauPPLFECUncorrectableBlocks.setStatus(_A)
_IfMauBIPErrorCount_Type=Counter32
_IfMauBIPErrorCount_Object=MibTableColumn
ifMauBIPErrorCount=_IfMauBIPErrorCount_Object((1,3,111,2,802,3,1,13,1,2,3,1,4),_IfMauBIPErrorCount_Type())
ifMauBIPErrorCount.setMaxAccess(_C)
if mibBuilder.loadTexts:ifMauBIPErrorCount.setStatus(_A)
_IfMauPCStoPHYLaneMapping_Type=Unsigned32
_IfMauPCStoPHYLaneMapping_Object=MibTableColumn
ifMauPCStoPHYLaneMapping=_IfMauPCStoPHYLaneMapping_Object((1,3,111,2,802,3,1,13,1,2,3,1,5),_IfMauPCStoPHYLaneMapping_Type())
ifMauPCStoPHYLaneMapping.setMaxAccess(_C)
if mibBuilder.loadTexts:ifMauPCStoPHYLaneMapping.setStatus(_A)
_Dot3PlaceholderGroup_ObjectIdentity=ObjectIdentity
dot3PlaceholderGroup=_Dot3PlaceholderGroup_ObjectIdentity((1,3,111,2,802,3,1,13,1,3))
class _Dot3Placeholder_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('placeholder',1))
_Dot3Placeholder_Type.__name__=_D
_Dot3Placeholder_Object=MibScalar
dot3Placeholder=_Dot3Placeholder_Object((1,3,111,2,802,3,1,13,1,3,1),_Dot3Placeholder_Type())
dot3Placeholder.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3Placeholder.setStatus(_A)
_Dot3IfMauAutoNegGroup_ObjectIdentity=ObjectIdentity
dot3IfMauAutoNegGroup=_Dot3IfMauAutoNegGroup_ObjectIdentity((1,3,111,2,802,3,1,13,1,5))
_IfMauAutoNegTable_Object=MibTable
ifMauAutoNegTable=_IfMauAutoNegTable_Object((1,3,111,2,802,3,1,13,1,5,1))
if mibBuilder.loadTexts:ifMauAutoNegTable.setStatus(_A)
_IfMauAutoNegEntry_Object=MibTableRow
ifMauAutoNegEntry=_IfMauAutoNegEntry_Object((1,3,111,2,802,3,1,13,1,5,1,1))
ifMauAutoNegEntry.setIndexNames((0,_B,_I),(0,_B,_J))
if mibBuilder.loadTexts:ifMauAutoNegEntry.setStatus(_A)
class _IfMauAutoNegAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_X,1),(_N,2)))
_IfMauAutoNegAdminStatus_Type.__name__=_D
_IfMauAutoNegAdminStatus_Object=MibTableColumn
ifMauAutoNegAdminStatus=_IfMauAutoNegAdminStatus_Object((1,3,111,2,802,3,1,13,1,5,1,1,1),_IfMauAutoNegAdminStatus_Type())
ifMauAutoNegAdminStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:ifMauAutoNegAdminStatus.setStatus(_A)
class _IfMauAutoNegRemoteSignaling_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('detected',1),('notdetected',2)))
_IfMauAutoNegRemoteSignaling_Type.__name__=_D
_IfMauAutoNegRemoteSignaling_Object=MibTableColumn
ifMauAutoNegRemoteSignaling=_IfMauAutoNegRemoteSignaling_Object((1,3,111,2,802,3,1,13,1,5,1,1,2),_IfMauAutoNegRemoteSignaling_Type())
ifMauAutoNegRemoteSignaling.setMaxAccess(_C)
if mibBuilder.loadTexts:ifMauAutoNegRemoteSignaling.setStatus(_A)
class _IfMauAutoNegConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_H,1),('configuring',2),('complete',3),(_N,4),('parallelDetectFail',5)))
_IfMauAutoNegConfig_Type.__name__=_D
_IfMauAutoNegConfig_Object=MibTableColumn
ifMauAutoNegConfig=_IfMauAutoNegConfig_Object((1,3,111,2,802,3,1,13,1,5,1,1,4),_IfMauAutoNegConfig_Type())
ifMauAutoNegConfig.setMaxAccess(_C)
if mibBuilder.loadTexts:ifMauAutoNegConfig.setStatus(_A)
class _IfMauAutoNegRestart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('restart',1),('norestart',2)))
_IfMauAutoNegRestart_Type.__name__=_D
_IfMauAutoNegRestart_Object=MibTableColumn
ifMauAutoNegRestart=_IfMauAutoNegRestart_Object((1,3,111,2,802,3,1,13,1,5,1,1,5),_IfMauAutoNegRestart_Type())
ifMauAutoNegRestart.setMaxAccess(_F)
if mibBuilder.loadTexts:ifMauAutoNegRestart.setStatus(_A)
_IfMauAutoNegCapabilityBits_Type=IANAifMauAutoNegCapBits
_IfMauAutoNegCapabilityBits_Object=MibTableColumn
ifMauAutoNegCapabilityBits=_IfMauAutoNegCapabilityBits_Object((1,3,111,2,802,3,1,13,1,5,1,1,6),_IfMauAutoNegCapabilityBits_Type())
ifMauAutoNegCapabilityBits.setMaxAccess(_C)
if mibBuilder.loadTexts:ifMauAutoNegCapabilityBits.setStatus(_A)
_IfMauAutoNegCapAdvertisedBits_Type=IANAifMauAutoNegCapBits
_IfMauAutoNegCapAdvertisedBits_Object=MibTableColumn
ifMauAutoNegCapAdvertisedBits=_IfMauAutoNegCapAdvertisedBits_Object((1,3,111,2,802,3,1,13,1,5,1,1,7),_IfMauAutoNegCapAdvertisedBits_Type())
ifMauAutoNegCapAdvertisedBits.setMaxAccess(_F)
if mibBuilder.loadTexts:ifMauAutoNegCapAdvertisedBits.setStatus(_A)
_IfMauAutoNegCapReceivedBits_Type=IANAifMauAutoNegCapBits
_IfMauAutoNegCapReceivedBits_Object=MibTableColumn
ifMauAutoNegCapReceivedBits=_IfMauAutoNegCapReceivedBits_Object((1,3,111,2,802,3,1,13,1,5,1,1,8),_IfMauAutoNegCapReceivedBits_Type())
ifMauAutoNegCapReceivedBits.setMaxAccess(_C)
if mibBuilder.loadTexts:ifMauAutoNegCapReceivedBits.setStatus(_A)
class _IfMauAutoNegRemoteFaultAdvertised_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_b,1),(_c,2),(_d,3),(_e,4)))
_IfMauAutoNegRemoteFaultAdvertised_Type.__name__=_D
_IfMauAutoNegRemoteFaultAdvertised_Object=MibTableColumn
ifMauAutoNegRemoteFaultAdvertised=_IfMauAutoNegRemoteFaultAdvertised_Object((1,3,111,2,802,3,1,13,1,5,1,1,9),_IfMauAutoNegRemoteFaultAdvertised_Type())
ifMauAutoNegRemoteFaultAdvertised.setMaxAccess(_F)
if mibBuilder.loadTexts:ifMauAutoNegRemoteFaultAdvertised.setStatus(_A)
class _IfMauAutoNegRemoteFaultReceived_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_b,1),(_c,2),(_d,3),(_e,4)))
_IfMauAutoNegRemoteFaultReceived_Type.__name__=_D
_IfMauAutoNegRemoteFaultReceived_Object=MibTableColumn
ifMauAutoNegRemoteFaultReceived=_IfMauAutoNegRemoteFaultReceived_Object((1,3,111,2,802,3,1,13,1,5,1,1,10),_IfMauAutoNegRemoteFaultReceived_Type())
ifMauAutoNegRemoteFaultReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:ifMauAutoNegRemoteFaultReceived.setStatus(_A)
_MauModConf_ObjectIdentity=ObjectIdentity
mauModConf=_MauModConf_ObjectIdentity((1,3,111,2,802,3,1,13,2))
_MauModCompls_ObjectIdentity=ObjectIdentity
mauModCompls=_MauModCompls_ObjectIdentity((1,3,111,2,802,3,1,13,2,1))
_MauModObjGrps_ObjectIdentity=ObjectIdentity
mauModObjGrps=_MauModObjGrps_ObjectIdentity((1,3,111,2,802,3,1,13,2,2))
_MauModNotGrps_ObjectIdentity=ObjectIdentity
mauModNotGrps=_MauModNotGrps_ObjectIdentity((1,3,111,2,802,3,1,13,2,3))
mauRpGrpBasic=ObjectGroup((1,3,111,2,802,3,1,13,2,2,1))
mauRpGrpBasic.setObjects(*((_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_O),(_B,_j)))
if mibBuilder.loadTexts:mauRpGrpBasic.setStatus(_A)
mauRpGrp100Mbs=ObjectGroup((1,3,111,2,802,3,1,13,2,2,2))
mauRpGrp100Mbs.setObjects((_B,_k))
if mibBuilder.loadTexts:mauRpGrp100Mbs.setStatus(_A)
mauRpGrpJack=ObjectGroup((1,3,111,2,802,3,1,13,2,2,3))
mauRpGrpJack.setObjects((_B,_l))
if mibBuilder.loadTexts:mauRpGrpJack.setStatus(_A)
mauIfGrpBasic=ObjectGroup((1,3,111,2,802,3,1,13,2,2,4))
mauIfGrpBasic.setObjects(*((_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_P),(_B,_q),(_B,_r)))
if mibBuilder.loadTexts:mauIfGrpBasic.setStatus(_A)
mauIfGrpJack=ObjectGroup((1,3,111,2,802,3,1,13,2,2,5))
mauIfGrpJack.setObjects((_B,_s))
if mibBuilder.loadTexts:mauIfGrpJack.setStatus(_A)
mauIfGrpHighCapacity=ObjectGroup((1,3,111,2,802,3,1,13,2,2,6))
mauIfGrpHighCapacity.setObjects(*((_B,_t),(_B,_u),(_B,_v),(_B,_w)))
if mibBuilder.loadTexts:mauIfGrpHighCapacity.setStatus(_A)
mauIfGrpAutoNeg2=ObjectGroup((1,3,111,2,802,3,1,13,2,2,7))
mauIfGrpAutoNeg2.setObjects(*((_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3)))
if mibBuilder.loadTexts:mauIfGrpAutoNeg2.setStatus(_A)
mauIfGrpAutoNeg1000Mbps=ObjectGroup((1,3,111,2,802,3,1,13,2,2,8))
mauIfGrpAutoNeg1000Mbps.setObjects(*((_B,_A4),(_B,_A5)))
if mibBuilder.loadTexts:mauIfGrpAutoNeg1000Mbps.setStatus(_A)
mauIfGrpHCStats=ObjectGroup((1,3,111,2,802,3,1,13,2,2,9))
mauIfGrpHCStats.setObjects(*((_B,_A6),(_B,_A7)))
if mibBuilder.loadTexts:mauIfGrpHCStats.setStatus(_A)
mauIfGrpFEC=ObjectGroup((1,3,111,2,802,3,1,13,2,2,10))
mauIfGrpFEC.setObjects(*((_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB)))
if mibBuilder.loadTexts:mauIfGrpFEC.setStatus(_A)
mauIfGrpSNR=ObjectGroup((1,3,111,2,802,3,1,13,2,2,11))
mauIfGrpSNR.setObjects(*((_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF)))
if mibBuilder.loadTexts:mauIfGrpSNR.setStatus(_A)
mauIfGrpEEE=ObjectGroup((1,3,111,2,802,3,1,13,2,2,12))
mauIfGrpEEE.setObjects(*((_B,_AG),(_B,_AH),(_B,_AI)))
if mibBuilder.loadTexts:mauIfGrpEEE.setStatus(_A)
mauIfGrpTimeSync=ObjectGroup((1,3,111,2,802,3,1,13,2,2,13))
mauIfGrpTimeSync.setObjects(*((_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO)))
if mibBuilder.loadTexts:mauIfGrpTimeSync.setStatus(_A)
mauIfGrpPerPCSLaneStats=ObjectGroup((1,3,111,2,802,3,1,13,2,2,14))
mauIfGrpPerPCSLaneStats.setObjects(*((_B,_AP),(_B,_AQ),(_B,_AR),(_B,_AS)))
if mibBuilder.loadTexts:mauIfGrpPerPCSLaneStats.setStatus(_A)
rpMauJabberTrap=NotificationType((1,3,111,2,802,3,1,13,1,0,1))
rpMauJabberTrap.setObjects((_B,_O))
if mibBuilder.loadTexts:rpMauJabberTrap.setStatus(_A)
ifMauJabberTrap=NotificationType((1,3,111,2,802,3,1,13,1,0,2))
ifMauJabberTrap.setObjects((_B,_P))
if mibBuilder.loadTexts:ifMauJabberTrap.setStatus(_A)
rpMauNotifications=NotificationGroup((1,3,111,2,802,3,1,13,2,3,1))
rpMauNotifications.setObjects((_B,_AT))
if mibBuilder.loadTexts:rpMauNotifications.setStatus(_A)
ifMauNotifications=NotificationGroup((1,3,111,2,802,3,1,13,2,3,2))
ifMauNotifications.setObjects((_B,_AU))
if mibBuilder.loadTexts:ifMauNotifications.setStatus(_A)
mauModRpCompl2=ModuleCompliance((1,3,111,2,802,3,1,13,2,1,1))
mauModRpCompl2.setObjects(*((_B,_AV),(_B,_AW),(_B,_AX),(_B,_AY)))
if mibBuilder.loadTexts:mauModRpCompl2.setStatus(_A)
mauModIfCompl3=ModuleCompliance((1,3,111,2,802,3,1,13,2,1,2))
mauModIfCompl3.setObjects(*((_B,_AZ),(_B,_Aa),(_B,_Ab),(_B,_Ac),(_B,_Ad),(_B,_Ae),(_B,_Af),(_B,_Ag),(_B,_Ah),(_B,_Ai),(_B,_Aj),(_B,_Ak)))
if mibBuilder.loadTexts:mauModIfCompl3.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ieee8023mauMIB':ieee8023mauMIB,'ieee8023snmpDot3MauMgt':ieee8023snmpDot3MauMgt,'snmpDot3MauTraps':snmpDot3MauTraps,_AT:rpMauJabberTrap,_AU:ifMauJabberTrap,'dot3RpMauBasicGroup':dot3RpMauBasicGroup,'rpMauTable':rpMauTable,'rpMauEntry':rpMauEntry,_K:rpMauGroupIndex,_L:rpMauPortIndex,_M:rpMauIndex,_f:rpMauType,_g:rpMauStatus,_h:rpMauMediaAvailable,_i:rpMauMediaAvailableStateExits,_O:rpMauJabberState,_j:rpMauJabberingStateEnters,_k:rpMauFalseCarriers,'rpJackTable':rpJackTable,'rpJackEntry':rpJackEntry,_W:rpJackIndex,_l:rpJackType,'dot3IfMauBasicGroup':dot3IfMauBasicGroup,'ifMauTable':ifMauTable,'ifMauEntry':ifMauEntry,_I:ifMauIfIndex,_J:ifMauIndex,_m:ifMauType,_n:ifMauStatus,_o:ifMauMediaAvailable,_p:ifMauMediaAvailableStateExits,_P:ifMauJabberState,_q:ifMauJabberingStateEnters,_t:ifMauFalseCarriers,_v:ifMauDefaultType,_w:ifMauAutoNegSupported,_u:ifMauTypeListBits,_A6:ifMauHCFalseCarriers,_A7:ifMauPCSCodingViolations,_A8:ifMauFECAbility,_A9:ifMauFECMode,_AA:ifMauFECCorrectedBlocks,_AB:ifMauFECUnCorrectableBlocks,_AC:ifMauSNROpMarginChnlA,_AD:ifMauSNROpMarginChnlB,_AE:ifMauSNROpMarginChnlC,_AF:ifMauSNROpMarginChnlD,_AG:ifMauEEESupportList,_AH:ifMauEEELDFastRetrainCount,_AI:ifMauEEELPFastRetrainCount,_AJ:ifMauTimeSyncCapabilityTX,_AK:ifMauTimeSyncCapabilityRX,_AL:ifMauTimeSyncDelayTXmax,_AM:ifMauTimeSyncDelayTXmin,_AN:ifMauTimeSyncDelayRXmax,_AO:ifMauTimeSyncDelayRXmin,'ifJackTable':ifJackTable,'ifJackEntry':ifJackEntry,_Z:ifJackIndex,_s:ifJackType,'ifMauPerPCSLaneStatsTable':ifMauPerPCSLaneStatsTable,'ifMauPerPCSLaneStatsEntry':ifMauPerPCSLaneStatsEntry,_a:ifPCSLaneIndex,_AP:ifMauPPLFECCorrectedBlocks,_AQ:ifMauPPLFECUncorrectableBlocks,_AR:ifMauBIPErrorCount,_AS:ifMauPCStoPHYLaneMapping,'dot3PlaceholderGroup':dot3PlaceholderGroup,_r:dot3Placeholder,'dot3IfMauAutoNegGroup':dot3IfMauAutoNegGroup,'ifMauAutoNegTable':ifMauAutoNegTable,'ifMauAutoNegEntry':ifMauAutoNegEntry,_x:ifMauAutoNegAdminStatus,_y:ifMauAutoNegRemoteSignaling,_z:ifMauAutoNegConfig,_A3:ifMauAutoNegRestart,_A0:ifMauAutoNegCapabilityBits,_A1:ifMauAutoNegCapAdvertisedBits,_A2:ifMauAutoNegCapReceivedBits,_A4:ifMauAutoNegRemoteFaultAdvertised,_A5:ifMauAutoNegRemoteFaultReceived,'mauModConf':mauModConf,'mauModCompls':mauModCompls,'mauModRpCompl2':mauModRpCompl2,'mauModIfCompl3':mauModIfCompl3,'mauModObjGrps':mauModObjGrps,_AV:mauRpGrpBasic,_AW:mauRpGrp100Mbs,_AX:mauRpGrpJack,_AZ:mauIfGrpBasic,_Ac:mauIfGrpJack,_Aa:mauIfGrpHighCapacity,_Ad:mauIfGrpAutoNeg2,_Ae:mauIfGrpAutoNeg1000Mbps,_Ab:mauIfGrpHCStats,_Ag:mauIfGrpFEC,_Ah:mauIfGrpSNR,_Ai:mauIfGrpEEE,_Aj:mauIfGrpTimeSync,_Ak:mauIfGrpPerPCSLaneStats,'mauModNotGrps':mauModNotGrps,_AY:rpMauNotifications,_Af:ifMauNotifications})