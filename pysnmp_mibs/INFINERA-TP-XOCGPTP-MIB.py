_p='xOcgPtpGroup'
_o='xOcgPtpBwQlicensed'
_n='xOcgPtpBwQused'
_m='xOcgPtpBwQmax'
_l='xOcgPtpLoopback'
_k='xOcgPtpOcgReceivedTTI'
_j='xOcgPtpOcgExpectedTTI'
_i='xOcgPtpOcgTxTTI'
_h='xOcgPtpRxEdfaOutputPowerTarget'
_g='xOcgPtpMaxFruGain'
_f='xOcgPtpGain'
_e='xOcgPtpCurOcgNumber'
_d='xOcgPtpRemainingTunabilityOperatingHours'
_c='xOcgPtpTunableOcgNumber'
_b='xOcgPtpAvailableTunableOcgNumbers'
_a='xOcgPtpAutomaticTunable'
_Z='xOcgPtpInstalledEncodingMode'
_Y='xOcgPtpProvisionedEncodingMode'
_X='xOcgPtpOpenwaveTargetTxOcgPower'
_W='xOcgPtpAutoDiscoveryPeerLm'
_V='xOcgPtpDiscoveredPeerTp'
_U='xOcgPtpProvisionedPeerTp'
_T='xOcgPtpLineSystemMode'
_S='xOcgPtpChannelCount'
_R='xOcgPtpDlmEqptTyp'
_Q='xOcgPtpRxPicState'
_P='xOcgPtpTxPicState'
_O='xOcgPtpOcgPowerControlLoop'
_N='xOcgPtpPmHistStatsEnable'
_M='disabled'
_L='enabled'
_K='InfnOperationalState'
_J='InfnChassisType'
_I='InfnAutoTunable'
_H='ifIndex'
_G='IF-MIB'
_F='InfnEncoding'
_E='Integer32'
_D='read-write'
_C='read-only'
_B='INFINERA-TP-XOCGPTP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_G,_H)
terminationPoint,=mibBuilder.importSymbols('INFINERA-REG-MIB','terminationPoint')
FloatHundredths,FloatTenths,InfnAutoTunable,InfnChassisType,InfnEnableDisable,InfnEncoding,InfnModulation,InfnOperationalState,InfnPicStatus=mibBuilder.importSymbols('INFINERA-TC-MIB','FloatHundredths','FloatTenths',_I,_J,'InfnEnableDisable',_F,'InfnModulation',_K,'InfnPicStatus')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
xOcgPtpMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,2,51))
if mibBuilder.loadTexts:xOcgPtpMIB.setRevisions(('2008-10-20 00:00',))
_XOcgPtpTable_Object=MibTable
xOcgPtpTable=_XOcgPtpTable_Object((1,3,6,1,4,1,21296,2,2,2,2,51,1))
if mibBuilder.loadTexts:xOcgPtpTable.setStatus(_A)
_XOcgPtpEntry_Object=MibTableRow
xOcgPtpEntry=_XOcgPtpEntry_Object((1,3,6,1,4,1,21296,2,2,2,2,51,1,1))
xOcgPtpEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:xOcgPtpEntry.setStatus(_A)
class _XOcgPtpPmHistStatsEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_XOcgPtpPmHistStatsEnable_Type.__name__=_E
_XOcgPtpPmHistStatsEnable_Object=MibTableColumn
xOcgPtpPmHistStatsEnable=_XOcgPtpPmHistStatsEnable_Object((1,3,6,1,4,1,21296,2,2,2,2,51,1,1,1),_XOcgPtpPmHistStatsEnable_Type())
xOcgPtpPmHistStatsEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:xOcgPtpPmHistStatsEnable.setStatus(_A)
class _XOcgPtpOcgPowerControlLoop_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_M,1),(_L,2),('unknown',3)))
_XOcgPtpOcgPowerControlLoop_Type.__name__=_E
_XOcgPtpOcgPowerControlLoop_Object=MibTableColumn
xOcgPtpOcgPowerControlLoop=_XOcgPtpOcgPowerControlLoop_Object((1,3,6,1,4,1,21296,2,2,2,2,51,1,1,2),_XOcgPtpOcgPowerControlLoop_Type())
xOcgPtpOcgPowerControlLoop.setMaxAccess(_D)
if mibBuilder.loadTexts:xOcgPtpOcgPowerControlLoop.setStatus(_A)
_XOcgPtpTxPicState_Type=InfnPicStatus
_XOcgPtpTxPicState_Object=MibTableColumn
xOcgPtpTxPicState=_XOcgPtpTxPicState_Object((1,3,6,1,4,1,21296,2,2,2,2,51,1,1,3),_XOcgPtpTxPicState_Type())
xOcgPtpTxPicState.setMaxAccess(_C)
if mibBuilder.loadTexts:xOcgPtpTxPicState.setStatus(_A)
_XOcgPtpRxPicState_Type=InfnPicStatus
_XOcgPtpRxPicState_Object=MibTableColumn
xOcgPtpRxPicState=_XOcgPtpRxPicState_Object((1,3,6,1,4,1,21296,2,2,2,2,51,1,1,4),_XOcgPtpRxPicState_Type())
xOcgPtpRxPicState.setMaxAccess(_C)
if mibBuilder.loadTexts:xOcgPtpRxPicState.setStatus(_A)
class _XOcgPtpDlmEqptTyp_Type(InfnChassisType):defaultValue=6
_XOcgPtpDlmEqptTyp_Type.__name__=_J
_XOcgPtpDlmEqptTyp_Object=MibTableColumn
xOcgPtpDlmEqptTyp=_XOcgPtpDlmEqptTyp_Object((1,3,6,1,4,1,21296,2,2,2,2,51,1,1,5),_XOcgPtpDlmEqptTyp_Type())
xOcgPtpDlmEqptTyp.setMaxAccess(_C)
if mibBuilder.loadTexts:xOcgPtpDlmEqptTyp.setStatus(_A)
_XOcgPtpChannelCount_Type=FloatTenths
_XOcgPtpChannelCount_Object=MibTableColumn
xOcgPtpChannelCount=_XOcgPtpChannelCount_Object((1,3,6,1,4,1,21296,2,2,2,2,51,1,1,6),_XOcgPtpChannelCount_Type())
xOcgPtpChannelCount.setMaxAccess(_C)
if mibBuilder.loadTexts:xOcgPtpChannelCount.setStatus(_A)
class _XOcgPtpLineSystemMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('modeocg',1),('modeopenwave',2),('modescg',3),('modescgpassivemux-1',4)))
_XOcgPtpLineSystemMode_Type.__name__=_E
_XOcgPtpLineSystemMode_Object=MibTableColumn
xOcgPtpLineSystemMode=_XOcgPtpLineSystemMode_Object((1,3,6,1,4,1,21296,2,2,2,2,51,1,1,7),_XOcgPtpLineSystemMode_Type())
xOcgPtpLineSystemMode.setMaxAccess(_C)
if mibBuilder.loadTexts:xOcgPtpLineSystemMode.setStatus(_A)
_XOcgPtpProvisionedPeerTp_Type=DisplayString
_XOcgPtpProvisionedPeerTp_Object=MibTableColumn
xOcgPtpProvisionedPeerTp=_XOcgPtpProvisionedPeerTp_Object((1,3,6,1,4,1,21296,2,2,2,2,51,1,1,8),_XOcgPtpProvisionedPeerTp_Type())
xOcgPtpProvisionedPeerTp.setMaxAccess(_D)
if mibBuilder.loadTexts:xOcgPtpProvisionedPeerTp.setStatus(_A)
_XOcgPtpDiscoveredPeerTp_Type=DisplayString
_XOcgPtpDiscoveredPeerTp_Object=MibTableColumn
xOcgPtpDiscoveredPeerTp=_XOcgPtpDiscoveredPeerTp_Object((1,3,6,1,4,1,21296,2,2,2,2,51,1,1,9),_XOcgPtpDiscoveredPeerTp_Type())
xOcgPtpDiscoveredPeerTp.setMaxAccess(_C)
if mibBuilder.loadTexts:xOcgPtpDiscoveredPeerTp.setStatus(_A)
class _XOcgPtpAutoDiscoveryPeerLm_Type(InfnOperationalState):defaultValue=1
_XOcgPtpAutoDiscoveryPeerLm_Type.__name__=_K
_XOcgPtpAutoDiscoveryPeerLm_Object=MibTableColumn
xOcgPtpAutoDiscoveryPeerLm=_XOcgPtpAutoDiscoveryPeerLm_Object((1,3,6,1,4,1,21296,2,2,2,2,51,1,1,10),_XOcgPtpAutoDiscoveryPeerLm_Type())
xOcgPtpAutoDiscoveryPeerLm.setMaxAccess(_D)
if mibBuilder.loadTexts:xOcgPtpAutoDiscoveryPeerLm.setStatus(_A)
_XOcgPtpOpenwaveTargetTxOcgPower_Type=FloatTenths
_XOcgPtpOpenwaveTargetTxOcgPower_Object=MibTableColumn
xOcgPtpOpenwaveTargetTxOcgPower=_XOcgPtpOpenwaveTargetTxOcgPower_Object((1,3,6,1,4,1,21296,2,2,2,2,51,1,1,11),_XOcgPtpOpenwaveTargetTxOcgPower_Type())
xOcgPtpOpenwaveTargetTxOcgPower.setMaxAccess(_D)
if mibBuilder.loadTexts:xOcgPtpOpenwaveTargetTxOcgPower.setStatus(_A)
class _XOcgPtpProvisionedEncodingMode_Type(InfnEncoding):defaultValue=1
_XOcgPtpProvisionedEncodingMode_Type.__name__=_F
_XOcgPtpProvisionedEncodingMode_Object=MibTableColumn
xOcgPtpProvisionedEncodingMode=_XOcgPtpProvisionedEncodingMode_Object((1,3,6,1,4,1,21296,2,2,2,2,51,1,1,12),_XOcgPtpProvisionedEncodingMode_Type())
xOcgPtpProvisionedEncodingMode.setMaxAccess(_D)
if mibBuilder.loadTexts:xOcgPtpProvisionedEncodingMode.setStatus(_A)
class _XOcgPtpInstalledEncodingMode_Type(InfnEncoding):defaultValue=1
_XOcgPtpInstalledEncodingMode_Type.__name__=_F
_XOcgPtpInstalledEncodingMode_Object=MibTableColumn
xOcgPtpInstalledEncodingMode=_XOcgPtpInstalledEncodingMode_Object((1,3,6,1,4,1,21296,2,2,2,2,51,1,1,13),_XOcgPtpInstalledEncodingMode_Type())
xOcgPtpInstalledEncodingMode.setMaxAccess(_C)
if mibBuilder.loadTexts:xOcgPtpInstalledEncodingMode.setStatus(_A)
class _XOcgPtpAutomaticTunable_Type(InfnAutoTunable):defaultValue=2
_XOcgPtpAutomaticTunable_Type.__name__=_I
_XOcgPtpAutomaticTunable_Object=MibTableColumn
xOcgPtpAutomaticTunable=_XOcgPtpAutomaticTunable_Object((1,3,6,1,4,1,21296,2,2,2,2,51,1,1,14),_XOcgPtpAutomaticTunable_Type())
xOcgPtpAutomaticTunable.setMaxAccess(_D)
if mibBuilder.loadTexts:xOcgPtpAutomaticTunable.setStatus(_A)
_XOcgPtpAvailableTunableOcgNumbers_Type=Integer32
_XOcgPtpAvailableTunableOcgNumbers_Object=MibTableColumn
xOcgPtpAvailableTunableOcgNumbers=_XOcgPtpAvailableTunableOcgNumbers_Object((1,3,6,1,4,1,21296,2,2,2,2,51,1,1,15),_XOcgPtpAvailableTunableOcgNumbers_Type())
xOcgPtpAvailableTunableOcgNumbers.setMaxAccess(_C)
if mibBuilder.loadTexts:xOcgPtpAvailableTunableOcgNumbers.setStatus(_A)
_XOcgPtpTunableOcgNumber_Type=Integer32
_XOcgPtpTunableOcgNumber_Object=MibTableColumn
xOcgPtpTunableOcgNumber=_XOcgPtpTunableOcgNumber_Object((1,3,6,1,4,1,21296,2,2,2,2,51,1,1,16),_XOcgPtpTunableOcgNumber_Type())
xOcgPtpTunableOcgNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:xOcgPtpTunableOcgNumber.setStatus(_A)
_XOcgPtpRemainingTunabilityOperatingHours_Type=Integer32
_XOcgPtpRemainingTunabilityOperatingHours_Object=MibTableColumn
xOcgPtpRemainingTunabilityOperatingHours=_XOcgPtpRemainingTunabilityOperatingHours_Object((1,3,6,1,4,1,21296,2,2,2,2,51,1,1,17),_XOcgPtpRemainingTunabilityOperatingHours_Type())
xOcgPtpRemainingTunabilityOperatingHours.setMaxAccess(_C)
if mibBuilder.loadTexts:xOcgPtpRemainingTunabilityOperatingHours.setStatus(_A)
_XOcgPtpCurOcgNumber_Type=Integer32
_XOcgPtpCurOcgNumber_Object=MibTableColumn
xOcgPtpCurOcgNumber=_XOcgPtpCurOcgNumber_Object((1,3,6,1,4,1,21296,2,2,2,2,51,1,1,18),_XOcgPtpCurOcgNumber_Type())
xOcgPtpCurOcgNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:xOcgPtpCurOcgNumber.setStatus(_A)
_XOcgPtpGain_Type=FloatTenths
_XOcgPtpGain_Object=MibTableColumn
xOcgPtpGain=_XOcgPtpGain_Object((1,3,6,1,4,1,21296,2,2,2,2,51,1,1,19),_XOcgPtpGain_Type())
xOcgPtpGain.setMaxAccess(_D)
if mibBuilder.loadTexts:xOcgPtpGain.setStatus(_A)
_XOcgPtpMaxFruGain_Type=FloatHundredths
_XOcgPtpMaxFruGain_Object=MibTableColumn
xOcgPtpMaxFruGain=_XOcgPtpMaxFruGain_Object((1,3,6,1,4,1,21296,2,2,2,2,51,1,1,20),_XOcgPtpMaxFruGain_Type())
xOcgPtpMaxFruGain.setMaxAccess(_C)
if mibBuilder.loadTexts:xOcgPtpMaxFruGain.setStatus(_A)
_XOcgPtpRxEdfaOutputPowerTarget_Type=FloatTenths
_XOcgPtpRxEdfaOutputPowerTarget_Object=MibTableColumn
xOcgPtpRxEdfaOutputPowerTarget=_XOcgPtpRxEdfaOutputPowerTarget_Object((1,3,6,1,4,1,21296,2,2,2,2,51,1,1,21),_XOcgPtpRxEdfaOutputPowerTarget_Type())
xOcgPtpRxEdfaOutputPowerTarget.setMaxAccess(_C)
if mibBuilder.loadTexts:xOcgPtpRxEdfaOutputPowerTarget.setStatus(_A)
_XOcgPtpOcgTxTTI_Type=DisplayString
_XOcgPtpOcgTxTTI_Object=MibTableColumn
xOcgPtpOcgTxTTI=_XOcgPtpOcgTxTTI_Object((1,3,6,1,4,1,21296,2,2,2,2,51,1,1,22),_XOcgPtpOcgTxTTI_Type())
xOcgPtpOcgTxTTI.setMaxAccess(_D)
if mibBuilder.loadTexts:xOcgPtpOcgTxTTI.setStatus(_A)
_XOcgPtpOcgExpectedTTI_Type=DisplayString
_XOcgPtpOcgExpectedTTI_Object=MibTableColumn
xOcgPtpOcgExpectedTTI=_XOcgPtpOcgExpectedTTI_Object((1,3,6,1,4,1,21296,2,2,2,2,51,1,1,23),_XOcgPtpOcgExpectedTTI_Type())
xOcgPtpOcgExpectedTTI.setMaxAccess(_D)
if mibBuilder.loadTexts:xOcgPtpOcgExpectedTTI.setStatus(_A)
_XOcgPtpOcgReceivedTTI_Type=DisplayString
_XOcgPtpOcgReceivedTTI_Object=MibTableColumn
xOcgPtpOcgReceivedTTI=_XOcgPtpOcgReceivedTTI_Object((1,3,6,1,4,1,21296,2,2,2,2,51,1,1,24),_XOcgPtpOcgReceivedTTI_Type())
xOcgPtpOcgReceivedTTI.setMaxAccess(_C)
if mibBuilder.loadTexts:xOcgPtpOcgReceivedTTI.setStatus(_A)
_XOcgPtpLoopback_Type=TruthValue
_XOcgPtpLoopback_Object=MibTableColumn
xOcgPtpLoopback=_XOcgPtpLoopback_Object((1,3,6,1,4,1,21296,2,2,2,2,51,1,1,25),_XOcgPtpLoopback_Type())
xOcgPtpLoopback.setMaxAccess(_D)
if mibBuilder.loadTexts:xOcgPtpLoopback.setStatus(_A)
_XOcgPtpBwQmax_Type=FloatTenths
_XOcgPtpBwQmax_Object=MibTableColumn
xOcgPtpBwQmax=_XOcgPtpBwQmax_Object((1,3,6,1,4,1,21296,2,2,2,2,51,1,1,26),_XOcgPtpBwQmax_Type())
xOcgPtpBwQmax.setMaxAccess(_C)
if mibBuilder.loadTexts:xOcgPtpBwQmax.setStatus(_A)
_XOcgPtpBwQused_Type=FloatTenths
_XOcgPtpBwQused_Object=MibTableColumn
xOcgPtpBwQused=_XOcgPtpBwQused_Object((1,3,6,1,4,1,21296,2,2,2,2,51,1,1,27),_XOcgPtpBwQused_Type())
xOcgPtpBwQused.setMaxAccess(_C)
if mibBuilder.loadTexts:xOcgPtpBwQused.setStatus(_A)
_XOcgPtpBwQlicensed_Type=FloatTenths
_XOcgPtpBwQlicensed_Object=MibTableColumn
xOcgPtpBwQlicensed=_XOcgPtpBwQlicensed_Object((1,3,6,1,4,1,21296,2,2,2,2,51,1,1,28),_XOcgPtpBwQlicensed_Type())
xOcgPtpBwQlicensed.setMaxAccess(_C)
if mibBuilder.loadTexts:xOcgPtpBwQlicensed.setStatus(_A)
_XOcgPtpConformance_ObjectIdentity=ObjectIdentity
xOcgPtpConformance=_XOcgPtpConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,51,3))
_XOcgPtpCompliances_ObjectIdentity=ObjectIdentity
xOcgPtpCompliances=_XOcgPtpCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,51,3,1))
_XOcgPtpGroups_ObjectIdentity=ObjectIdentity
xOcgPtpGroups=_XOcgPtpGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,51,3,2))
xOcgPtpGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,2,51,3,2,1))
xOcgPtpGroup.setObjects(*((_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o)))
if mibBuilder.loadTexts:xOcgPtpGroup.setStatus(_A)
xOcgPtpCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,2,51,3,1,1))
xOcgPtpCompliance.setObjects((_B,_p))
if mibBuilder.loadTexts:xOcgPtpCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'xOcgPtpMIB':xOcgPtpMIB,'xOcgPtpTable':xOcgPtpTable,'xOcgPtpEntry':xOcgPtpEntry,_N:xOcgPtpPmHistStatsEnable,_O:xOcgPtpOcgPowerControlLoop,_P:xOcgPtpTxPicState,_Q:xOcgPtpRxPicState,_R:xOcgPtpDlmEqptTyp,_S:xOcgPtpChannelCount,_T:xOcgPtpLineSystemMode,_U:xOcgPtpProvisionedPeerTp,_V:xOcgPtpDiscoveredPeerTp,_W:xOcgPtpAutoDiscoveryPeerLm,_X:xOcgPtpOpenwaveTargetTxOcgPower,_Y:xOcgPtpProvisionedEncodingMode,_Z:xOcgPtpInstalledEncodingMode,_a:xOcgPtpAutomaticTunable,_b:xOcgPtpAvailableTunableOcgNumbers,_c:xOcgPtpTunableOcgNumber,_d:xOcgPtpRemainingTunabilityOperatingHours,_e:xOcgPtpCurOcgNumber,_f:xOcgPtpGain,_g:xOcgPtpMaxFruGain,_h:xOcgPtpRxEdfaOutputPowerTarget,_i:xOcgPtpOcgTxTTI,_j:xOcgPtpOcgExpectedTTI,_k:xOcgPtpOcgReceivedTTI,_l:xOcgPtpLoopback,_m:xOcgPtpBwQmax,_n:xOcgPtpBwQused,_o:xOcgPtpBwQlicensed,'xOcgPtpConformance':xOcgPtpConformance,'xOcgPtpCompliances':xOcgPtpCompliances,'xOcgPtpCompliance':xOcgPtpCompliance,'xOcgPtpGroups':xOcgPtpGroups,_p:xOcgPtpGroup})