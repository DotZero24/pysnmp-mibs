_AY='lldpXdot1dcbxApplicationPriorityGroup'
_AX='lldpXdot1dcbxPFCGroup'
_AW='lldpXdot1dcbxETSGroup'
_AV='lldpXdot1dcbxAdminApplicationPriorityAEPriority'
_AU='lldpXdot1dcbxRemApplicationPriorityAEPriority'
_AT='lldpXdot1dcbxLocApplicationPriorityAEPriority'
_AS='lldpXdot1dcbxConfigApplicationPriorityTxEnable'
_AR='lldpXdot1dcbxAdminPFCEnableEnabled'
_AQ='lldpXdot1dcbxAdminPFCCap'
_AP='lldpXdot1dcbxAdminPFCMBC'
_AO='lldpXdot1dcbxAdminPFCWilling'
_AN='lldpXdot1dcbxRemPFCEnableEnabled'
_AM='lldpXdot1dcbxRemPFCCap'
_AL='lldpXdot1dcbxRemPFCMBC'
_AK='lldpXdot1dcbxRemPFCWilling'
_AJ='lldpXdot1dcbxLocPFCEnableEnabled'
_AI='lldpXdot1dcbxLocPFCCap'
_AH='lldpXdot1dcbxLocPFCMBC'
_AG='lldpXdot1dcbxLocPFCWilling'
_AF='lldpXdot1dcbxConfigPFCTxEnable'
_AE='lldpXdot1dcbxAdminETSRecoTrafficSelectionAlgorithm'
_AD='lldpXdot1dcbxAdminETSRecoTrafficClassBandwidth'
_AC='lldpXdot1dcbxAdminETSConTrafficSelectionAlgorithm'
_AB='lldpXdot1dcbxAdminETSConTrafficClassBandwidth'
_AA='lldpXdot1dcbxAdminETSConPriTrafficClass'
_A9='lldpXdot1dcbxAdminETSConWilling'
_A8='lldpXdot1dcbxAdminETSConTrafficClassesSupported'
_A7='lldpXdot1dcbxAdminETSConCreditBasedShaperSupport'
_A6='lldpXdot1dcbxRemETSRecoTrafficSelectionAlgorithm'
_A5='lldpXdot1dcbxRemETSRecoTrafficClassBandwidth'
_A4='lldpXdot1dcbxRemETSConTrafficSelectionAlgorithm'
_A3='lldpXdot1dcbxRemETSConTrafficClassBandwidth'
_A2='lldpXdot1dcbxRemETSConPriTrafficClass'
_A1='lldpXdot1dcbxRemETSConWilling'
_A0='lldpXdot1dcbxRemETSConTrafficClassesSupported'
_z='lldpXdot1dcbxRemETSConCreditBasedShaperSupport'
_y='lldpXdot1dcbxLocETSRecoTrafficSelectionAlgorithm'
_x='lldpXdot1dcbxLocETSRecoTrafficClassBandwidth'
_w='lldpXdot1dcbxLocETSConTrafficSelectionAlgorithm'
_v='lldpXdot1dcbxLocETSConTrafficClassBandwidth'
_u='lldpXdot1dcbxLocETSConPriTrafficClass'
_t='lldpXdot1dcbxLocETSConWilling'
_s='lldpXdot1dcbxLocETSConTrafficClassesSupported'
_r='lldpXdot1dcbxLocETSConCreditBasedShaperSupport'
_q='lldpXdot1dcbxConfigETSRecommendationTxEnable'
_p='lldpXdot1dcbxConfigETSConfigurationTxEnable'
_o='lldpXdot1dcbxConfigApplicationPriorityEntry'
_n='lldpXdot1dcbxConfigPFCEntry'
_m='lldpXdot1dcbxConfigETSRecommendationEntry'
_l='lldpXdot1dcbxConfigETSConfigurationEntry'
_k='lldpXdot1dcbxAdminApplicationPriorityAEProtocol'
_j='lldpXdot1dcbxAdminApplicationPriorityAESelector'
_i='lldpXdot1dcbxAdminPFCEnablePriority'
_h='lldpXdot1dcbxAdminETSRecoTSATrafficClass'
_g='lldpXdot1dcbxAdminETSRecoTrafficClass'
_f='lldpXdot1dcbxAdminETSConTSATrafficClass'
_e='lldpXdot1dcbxAdminETSConTrafficClass'
_d='LldpXdot1dcbxTrafficClassValue'
_c='lldpXdot1dcbxAdminETSConPriority'
_b='lldpXdot1dcbxRemApplicationPriorityAEProtocol'
_a='lldpXdot1dcbxRemApplicationPriorityAESelector'
_Z='lldpXdot1dcbxRemPFCEnablePriority'
_Y='lldpXdot1dcbxRemETSRecoTSATrafficClass'
_X='lldpXdot1dcbxRemETSRecoTrafficClass'
_W='lldpXdot1dcbxRemETSConTSATrafficClass'
_V='lldpXdot1dcbxRemETSConTrafficClass'
_U='lldpXdot1dcbxRemETSConPriority'
_T='lldpXdot1dcbxLocApplicationPriorityAEProtocol'
_S='lldpXdot1dcbxLocApplicationPriorityAESelector'
_R='lldpXdot1dcbxLocPFCEnablePriority'
_Q='lldpXdot1dcbxLocETSRecoTSATrafficClass'
_P='lldpXdot1dcbxLocETSRecoTrafficClass'
_O='lldpXdot1dcbxLocETSConTSATrafficClass'
_N='lldpXdot1dcbxLocETSConTrafficClass'
_M='lldpXdot1dcbxLocETSConPriority'
_L='TruthValue'
_K='lldpV2RemTimeMark'
_J='lldpV2RemLocalIfIndex'
_I='lldpV2RemLocalDestMACAddress'
_H='lldpV2RemIndex'
_G='read-write'
_F='lldpV2LocPortIfIndex'
_E='not-accessible'
_D='read-only'
_C='LLDP-V2-MIB'
_B='LLDP-EXT-DOT1-DCBX-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
IEEE8021PriorityValue,=mibBuilder.importSymbols('IEEE8021-TC-MIB','IEEE8021PriorityValue')
lldpV2Xdot1MIB,=mibBuilder.importSymbols('LLDP-EXT-DOT1-V2-MIB','lldpV2Xdot1MIB')
lldpV2LocPortIfIndex,lldpV2PortConfigEntry,lldpV2RemIndex,lldpV2RemLocalDestMACAddress,lldpV2RemLocalIfIndex,lldpV2RemTimeMark=mibBuilder.importSymbols(_C,_F,'lldpV2PortConfigEntry',_H,_I,_J,_K)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_L)
lldpXdot1dcbxMIB=ModuleIdentity((1,3,111,2,802,1,1,13,1,5,32962,5))
if mibBuilder.loadTexts:lldpXdot1dcbxMIB.setRevisions(('2009-11-25 18:00',))
class LldpXdot1dcbxTrafficClassValue(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
class LldpXdot1dcbxTrafficClassBandwidthValue(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
class LldpXdot1dcbxAppSelector(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('asEthertype',1),('asTCPPortNumber',2),('asUDPPortNumber',3),('asTCPUDPPortNumber',4)))
class LldpXdot1dcbxAppProtocol(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
class LldpXdot1dcbxSupportedCapacity(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
class LldpXdot1dcbxTrafficSelectionAlgorithm(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,255)));namedValues=NamedValues(*(('tsaStrictPriority',0),('tsaCreditBasedShaper',1),('tsaEnhancedTransmission',2),('tsaVendorSpecific',255)))
_LldpXdot1dcbxObjects_ObjectIdentity=ObjectIdentity
lldpXdot1dcbxObjects=_LldpXdot1dcbxObjects_ObjectIdentity((1,3,111,2,802,1,1,13,1,5,32962,5,1))
_LldpXdot1dcbxConfig_ObjectIdentity=ObjectIdentity
lldpXdot1dcbxConfig=_LldpXdot1dcbxConfig_ObjectIdentity((1,3,111,2,802,1,1,13,1,5,32962,5,1,1))
_LldpXdot1dcbxConfigETSConfigurationTable_Object=MibTable
lldpXdot1dcbxConfigETSConfigurationTable=_LldpXdot1dcbxConfigETSConfigurationTable_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,1,1))
if mibBuilder.loadTexts:lldpXdot1dcbxConfigETSConfigurationTable.setStatus(_A)
_LldpXdot1dcbxConfigETSConfigurationEntry_Object=MibTableRow
lldpXdot1dcbxConfigETSConfigurationEntry=_LldpXdot1dcbxConfigETSConfigurationEntry_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,1,1,1))
if mibBuilder.loadTexts:lldpXdot1dcbxConfigETSConfigurationEntry.setStatus(_A)
class _LldpXdot1dcbxConfigETSConfigurationTxEnable_Type(TruthValue):defaultValue=2
_LldpXdot1dcbxConfigETSConfigurationTxEnable_Type.__name__=_L
_LldpXdot1dcbxConfigETSConfigurationTxEnable_Object=MibTableColumn
lldpXdot1dcbxConfigETSConfigurationTxEnable=_LldpXdot1dcbxConfigETSConfigurationTxEnable_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,1,1,1,1),_LldpXdot1dcbxConfigETSConfigurationTxEnable_Type())
lldpXdot1dcbxConfigETSConfigurationTxEnable.setMaxAccess(_G)
if mibBuilder.loadTexts:lldpXdot1dcbxConfigETSConfigurationTxEnable.setStatus(_A)
_LldpXdot1dcbxConfigETSRecommendationTable_Object=MibTable
lldpXdot1dcbxConfigETSRecommendationTable=_LldpXdot1dcbxConfigETSRecommendationTable_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,1,2))
if mibBuilder.loadTexts:lldpXdot1dcbxConfigETSRecommendationTable.setStatus(_A)
_LldpXdot1dcbxConfigETSRecommendationEntry_Object=MibTableRow
lldpXdot1dcbxConfigETSRecommendationEntry=_LldpXdot1dcbxConfigETSRecommendationEntry_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,1,2,1))
if mibBuilder.loadTexts:lldpXdot1dcbxConfigETSRecommendationEntry.setStatus(_A)
class _LldpXdot1dcbxConfigETSRecommendationTxEnable_Type(TruthValue):defaultValue=2
_LldpXdot1dcbxConfigETSRecommendationTxEnable_Type.__name__=_L
_LldpXdot1dcbxConfigETSRecommendationTxEnable_Object=MibTableColumn
lldpXdot1dcbxConfigETSRecommendationTxEnable=_LldpXdot1dcbxConfigETSRecommendationTxEnable_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,1,2,1,1),_LldpXdot1dcbxConfigETSRecommendationTxEnable_Type())
lldpXdot1dcbxConfigETSRecommendationTxEnable.setMaxAccess(_G)
if mibBuilder.loadTexts:lldpXdot1dcbxConfigETSRecommendationTxEnable.setStatus(_A)
_LldpXdot1dcbxConfigPFCTable_Object=MibTable
lldpXdot1dcbxConfigPFCTable=_LldpXdot1dcbxConfigPFCTable_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,1,3))
if mibBuilder.loadTexts:lldpXdot1dcbxConfigPFCTable.setStatus(_A)
_LldpXdot1dcbxConfigPFCEntry_Object=MibTableRow
lldpXdot1dcbxConfigPFCEntry=_LldpXdot1dcbxConfigPFCEntry_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,1,3,1))
if mibBuilder.loadTexts:lldpXdot1dcbxConfigPFCEntry.setStatus(_A)
class _LldpXdot1dcbxConfigPFCTxEnable_Type(TruthValue):defaultValue=2
_LldpXdot1dcbxConfigPFCTxEnable_Type.__name__=_L
_LldpXdot1dcbxConfigPFCTxEnable_Object=MibTableColumn
lldpXdot1dcbxConfigPFCTxEnable=_LldpXdot1dcbxConfigPFCTxEnable_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,1,3,1,1),_LldpXdot1dcbxConfigPFCTxEnable_Type())
lldpXdot1dcbxConfigPFCTxEnable.setMaxAccess(_G)
if mibBuilder.loadTexts:lldpXdot1dcbxConfigPFCTxEnable.setStatus(_A)
_LldpXdot1dcbxConfigApplicationPriorityTable_Object=MibTable
lldpXdot1dcbxConfigApplicationPriorityTable=_LldpXdot1dcbxConfigApplicationPriorityTable_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,1,4))
if mibBuilder.loadTexts:lldpXdot1dcbxConfigApplicationPriorityTable.setStatus(_A)
_LldpXdot1dcbxConfigApplicationPriorityEntry_Object=MibTableRow
lldpXdot1dcbxConfigApplicationPriorityEntry=_LldpXdot1dcbxConfigApplicationPriorityEntry_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,1,4,1))
if mibBuilder.loadTexts:lldpXdot1dcbxConfigApplicationPriorityEntry.setStatus(_A)
class _LldpXdot1dcbxConfigApplicationPriorityTxEnable_Type(TruthValue):defaultValue=2
_LldpXdot1dcbxConfigApplicationPriorityTxEnable_Type.__name__=_L
_LldpXdot1dcbxConfigApplicationPriorityTxEnable_Object=MibTableColumn
lldpXdot1dcbxConfigApplicationPriorityTxEnable=_LldpXdot1dcbxConfigApplicationPriorityTxEnable_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,1,4,1,1),_LldpXdot1dcbxConfigApplicationPriorityTxEnable_Type())
lldpXdot1dcbxConfigApplicationPriorityTxEnable.setMaxAccess(_G)
if mibBuilder.loadTexts:lldpXdot1dcbxConfigApplicationPriorityTxEnable.setStatus(_A)
_LldpXdot1dcbxLocalData_ObjectIdentity=ObjectIdentity
lldpXdot1dcbxLocalData=_LldpXdot1dcbxLocalData_ObjectIdentity((1,3,111,2,802,1,1,13,1,5,32962,5,1,2))
_LldpXdot1dcbxLocETSConfiguration_ObjectIdentity=ObjectIdentity
lldpXdot1dcbxLocETSConfiguration=_LldpXdot1dcbxLocETSConfiguration_ObjectIdentity((1,3,111,2,802,1,1,13,1,5,32962,5,1,2,1))
_LldpXdot1dcbxLocETSBasicConfigurationTable_Object=MibTable
lldpXdot1dcbxLocETSBasicConfigurationTable=_LldpXdot1dcbxLocETSBasicConfigurationTable_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,2,1,1))
if mibBuilder.loadTexts:lldpXdot1dcbxLocETSBasicConfigurationTable.setStatus(_A)
_LldpXdot1dcbxLocETSBasicConfigurationEntry_Object=MibTableRow
lldpXdot1dcbxLocETSBasicConfigurationEntry=_LldpXdot1dcbxLocETSBasicConfigurationEntry_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,2,1,1,1))
lldpXdot1dcbxLocETSBasicConfigurationEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:lldpXdot1dcbxLocETSBasicConfigurationEntry.setStatus(_A)
_LldpXdot1dcbxLocETSConCreditBasedShaperSupport_Type=TruthValue
_LldpXdot1dcbxLocETSConCreditBasedShaperSupport_Object=MibTableColumn
lldpXdot1dcbxLocETSConCreditBasedShaperSupport=_LldpXdot1dcbxLocETSConCreditBasedShaperSupport_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,2,1,1,1,1),_LldpXdot1dcbxLocETSConCreditBasedShaperSupport_Type())
lldpXdot1dcbxLocETSConCreditBasedShaperSupport.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpXdot1dcbxLocETSConCreditBasedShaperSupport.setStatus(_A)
_LldpXdot1dcbxLocETSConTrafficClassesSupported_Type=LldpXdot1dcbxSupportedCapacity
_LldpXdot1dcbxLocETSConTrafficClassesSupported_Object=MibTableColumn
lldpXdot1dcbxLocETSConTrafficClassesSupported=_LldpXdot1dcbxLocETSConTrafficClassesSupported_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,2,1,1,1,2),_LldpXdot1dcbxLocETSConTrafficClassesSupported_Type())
lldpXdot1dcbxLocETSConTrafficClassesSupported.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpXdot1dcbxLocETSConTrafficClassesSupported.setStatus(_A)
_LldpXdot1dcbxLocETSConWilling_Type=TruthValue
_LldpXdot1dcbxLocETSConWilling_Object=MibTableColumn
lldpXdot1dcbxLocETSConWilling=_LldpXdot1dcbxLocETSConWilling_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,2,1,1,1,3),_LldpXdot1dcbxLocETSConWilling_Type())
lldpXdot1dcbxLocETSConWilling.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpXdot1dcbxLocETSConWilling.setStatus(_A)
_LldpXdot1dcbxLocETSConPriorityAssignmentTable_Object=MibTable
lldpXdot1dcbxLocETSConPriorityAssignmentTable=_LldpXdot1dcbxLocETSConPriorityAssignmentTable_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,2,1,2))
if mibBuilder.loadTexts:lldpXdot1dcbxLocETSConPriorityAssignmentTable.setStatus(_A)
_LldpXdot1dcbxLocETSConPriorityAssignmentEntry_Object=MibTableRow
lldpXdot1dcbxLocETSConPriorityAssignmentEntry=_LldpXdot1dcbxLocETSConPriorityAssignmentEntry_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,2,1,2,1))
lldpXdot1dcbxLocETSConPriorityAssignmentEntry.setIndexNames((0,_C,_F),(0,_B,_M))
if mibBuilder.loadTexts:lldpXdot1dcbxLocETSConPriorityAssignmentEntry.setStatus(_A)
_LldpXdot1dcbxLocETSConPriority_Type=IEEE8021PriorityValue
_LldpXdot1dcbxLocETSConPriority_Object=MibTableColumn
lldpXdot1dcbxLocETSConPriority=_LldpXdot1dcbxLocETSConPriority_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,2,1,2,1,1),_LldpXdot1dcbxLocETSConPriority_Type())
lldpXdot1dcbxLocETSConPriority.setMaxAccess(_E)
if mibBuilder.loadTexts:lldpXdot1dcbxLocETSConPriority.setStatus(_A)
_LldpXdot1dcbxLocETSConPriTrafficClass_Type=LldpXdot1dcbxTrafficClassValue
_LldpXdot1dcbxLocETSConPriTrafficClass_Object=MibTableColumn
lldpXdot1dcbxLocETSConPriTrafficClass=_LldpXdot1dcbxLocETSConPriTrafficClass_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,2,1,2,1,2),_LldpXdot1dcbxLocETSConPriTrafficClass_Type())
lldpXdot1dcbxLocETSConPriTrafficClass.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpXdot1dcbxLocETSConPriTrafficClass.setStatus(_A)
_LldpXdot1dcbxLocETSConTrafficClassBandwidthTable_Object=MibTable
lldpXdot1dcbxLocETSConTrafficClassBandwidthTable=_LldpXdot1dcbxLocETSConTrafficClassBandwidthTable_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,2,1,3))
if mibBuilder.loadTexts:lldpXdot1dcbxLocETSConTrafficClassBandwidthTable.setStatus(_A)
_LldpXdot1dcbxLocETSConTrafficClassBandwidthEntry_Object=MibTableRow
lldpXdot1dcbxLocETSConTrafficClassBandwidthEntry=_LldpXdot1dcbxLocETSConTrafficClassBandwidthEntry_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,2,1,3,1))
lldpXdot1dcbxLocETSConTrafficClassBandwidthEntry.setIndexNames((0,_C,_F),(0,_B,_N))
if mibBuilder.loadTexts:lldpXdot1dcbxLocETSConTrafficClassBandwidthEntry.setStatus(_A)
_LldpXdot1dcbxLocETSConTrafficClass_Type=LldpXdot1dcbxTrafficClassValue
_LldpXdot1dcbxLocETSConTrafficClass_Object=MibTableColumn
lldpXdot1dcbxLocETSConTrafficClass=_LldpXdot1dcbxLocETSConTrafficClass_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,2,1,3,1,1),_LldpXdot1dcbxLocETSConTrafficClass_Type())
lldpXdot1dcbxLocETSConTrafficClass.setMaxAccess(_E)
if mibBuilder.loadTexts:lldpXdot1dcbxLocETSConTrafficClass.setStatus(_A)
_LldpXdot1dcbxLocETSConTrafficClassBandwidth_Type=LldpXdot1dcbxTrafficClassBandwidthValue
_LldpXdot1dcbxLocETSConTrafficClassBandwidth_Object=MibTableColumn
lldpXdot1dcbxLocETSConTrafficClassBandwidth=_LldpXdot1dcbxLocETSConTrafficClassBandwidth_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,2,1,3,1,2),_LldpXdot1dcbxLocETSConTrafficClassBandwidth_Type())
lldpXdot1dcbxLocETSConTrafficClassBandwidth.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpXdot1dcbxLocETSConTrafficClassBandwidth.setStatus(_A)
_LldpXdot1dcbxLocETSConTrafficSelectionAlgorithmTable_Object=MibTable
lldpXdot1dcbxLocETSConTrafficSelectionAlgorithmTable=_LldpXdot1dcbxLocETSConTrafficSelectionAlgorithmTable_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,2,1,4))
if mibBuilder.loadTexts:lldpXdot1dcbxLocETSConTrafficSelectionAlgorithmTable.setStatus(_A)
_LldpXdot1dcbxLocETSConTrafficSelectionAlgorithmEntry_Object=MibTableRow
lldpXdot1dcbxLocETSConTrafficSelectionAlgorithmEntry=_LldpXdot1dcbxLocETSConTrafficSelectionAlgorithmEntry_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,2,1,4,1))
lldpXdot1dcbxLocETSConTrafficSelectionAlgorithmEntry.setIndexNames((0,_C,_F),(0,_B,_O))
if mibBuilder.loadTexts:lldpXdot1dcbxLocETSConTrafficSelectionAlgorithmEntry.setStatus(_A)
_LldpXdot1dcbxLocETSConTSATrafficClass_Type=LldpXdot1dcbxTrafficClassValue
_LldpXdot1dcbxLocETSConTSATrafficClass_Object=MibTableColumn
lldpXdot1dcbxLocETSConTSATrafficClass=_LldpXdot1dcbxLocETSConTSATrafficClass_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,2,1,4,1,1),_LldpXdot1dcbxLocETSConTSATrafficClass_Type())
lldpXdot1dcbxLocETSConTSATrafficClass.setMaxAccess(_E)
if mibBuilder.loadTexts:lldpXdot1dcbxLocETSConTSATrafficClass.setStatus(_A)
_LldpXdot1dcbxLocETSConTrafficSelectionAlgorithm_Type=LldpXdot1dcbxTrafficSelectionAlgorithm
_LldpXdot1dcbxLocETSConTrafficSelectionAlgorithm_Object=MibTableColumn
lldpXdot1dcbxLocETSConTrafficSelectionAlgorithm=_LldpXdot1dcbxLocETSConTrafficSelectionAlgorithm_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,2,1,4,1,2),_LldpXdot1dcbxLocETSConTrafficSelectionAlgorithm_Type())
lldpXdot1dcbxLocETSConTrafficSelectionAlgorithm.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpXdot1dcbxLocETSConTrafficSelectionAlgorithm.setStatus(_A)
_LldpXdot1dcbxLocETSReco_ObjectIdentity=ObjectIdentity
lldpXdot1dcbxLocETSReco=_LldpXdot1dcbxLocETSReco_ObjectIdentity((1,3,111,2,802,1,1,13,1,5,32962,5,1,2,2))
_LldpXdot1dcbxLocETSRecoTrafficClassBandwidthTable_Object=MibTable
lldpXdot1dcbxLocETSRecoTrafficClassBandwidthTable=_LldpXdot1dcbxLocETSRecoTrafficClassBandwidthTable_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,2,2,1))
if mibBuilder.loadTexts:lldpXdot1dcbxLocETSRecoTrafficClassBandwidthTable.setStatus(_A)
_LldpXdot1dcbxLocETSRecoTrafficClassBandwidthEntry_Object=MibTableRow
lldpXdot1dcbxLocETSRecoTrafficClassBandwidthEntry=_LldpXdot1dcbxLocETSRecoTrafficClassBandwidthEntry_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,2,2,1,1))
lldpXdot1dcbxLocETSRecoTrafficClassBandwidthEntry.setIndexNames((0,_C,_F),(0,_B,_P))
if mibBuilder.loadTexts:lldpXdot1dcbxLocETSRecoTrafficClassBandwidthEntry.setStatus(_A)
_LldpXdot1dcbxLocETSRecoTrafficClass_Type=LldpXdot1dcbxTrafficClassValue
_LldpXdot1dcbxLocETSRecoTrafficClass_Object=MibTableColumn
lldpXdot1dcbxLocETSRecoTrafficClass=_LldpXdot1dcbxLocETSRecoTrafficClass_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,2,2,1,1,1),_LldpXdot1dcbxLocETSRecoTrafficClass_Type())
lldpXdot1dcbxLocETSRecoTrafficClass.setMaxAccess(_E)
if mibBuilder.loadTexts:lldpXdot1dcbxLocETSRecoTrafficClass.setStatus(_A)
_LldpXdot1dcbxLocETSRecoTrafficClassBandwidth_Type=LldpXdot1dcbxTrafficClassBandwidthValue
_LldpXdot1dcbxLocETSRecoTrafficClassBandwidth_Object=MibTableColumn
lldpXdot1dcbxLocETSRecoTrafficClassBandwidth=_LldpXdot1dcbxLocETSRecoTrafficClassBandwidth_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,2,2,1,1,2),_LldpXdot1dcbxLocETSRecoTrafficClassBandwidth_Type())
lldpXdot1dcbxLocETSRecoTrafficClassBandwidth.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpXdot1dcbxLocETSRecoTrafficClassBandwidth.setStatus(_A)
_LldpXdot1dcbxLocETSRecoTrafficSelectionAlgorithmTable_Object=MibTable
lldpXdot1dcbxLocETSRecoTrafficSelectionAlgorithmTable=_LldpXdot1dcbxLocETSRecoTrafficSelectionAlgorithmTable_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,2,2,2))
if mibBuilder.loadTexts:lldpXdot1dcbxLocETSRecoTrafficSelectionAlgorithmTable.setStatus(_A)
_LldpXdot1dcbxLocETSRecoTrafficSelectionAlgorithmEntry_Object=MibTableRow
lldpXdot1dcbxLocETSRecoTrafficSelectionAlgorithmEntry=_LldpXdot1dcbxLocETSRecoTrafficSelectionAlgorithmEntry_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,2,2,2,1))
lldpXdot1dcbxLocETSRecoTrafficSelectionAlgorithmEntry.setIndexNames((0,_C,_F),(0,_B,_Q))
if mibBuilder.loadTexts:lldpXdot1dcbxLocETSRecoTrafficSelectionAlgorithmEntry.setStatus(_A)
_LldpXdot1dcbxLocETSRecoTSATrafficClass_Type=LldpXdot1dcbxTrafficClassValue
_LldpXdot1dcbxLocETSRecoTSATrafficClass_Object=MibTableColumn
lldpXdot1dcbxLocETSRecoTSATrafficClass=_LldpXdot1dcbxLocETSRecoTSATrafficClass_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,2,2,2,1,1),_LldpXdot1dcbxLocETSRecoTSATrafficClass_Type())
lldpXdot1dcbxLocETSRecoTSATrafficClass.setMaxAccess(_E)
if mibBuilder.loadTexts:lldpXdot1dcbxLocETSRecoTSATrafficClass.setStatus(_A)
_LldpXdot1dcbxLocETSRecoTrafficSelectionAlgorithm_Type=LldpXdot1dcbxTrafficSelectionAlgorithm
_LldpXdot1dcbxLocETSRecoTrafficSelectionAlgorithm_Object=MibTableColumn
lldpXdot1dcbxLocETSRecoTrafficSelectionAlgorithm=_LldpXdot1dcbxLocETSRecoTrafficSelectionAlgorithm_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,2,2,2,1,2),_LldpXdot1dcbxLocETSRecoTrafficSelectionAlgorithm_Type())
lldpXdot1dcbxLocETSRecoTrafficSelectionAlgorithm.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpXdot1dcbxLocETSRecoTrafficSelectionAlgorithm.setStatus(_A)
_LldpXdot1dcbxLocPFC_ObjectIdentity=ObjectIdentity
lldpXdot1dcbxLocPFC=_LldpXdot1dcbxLocPFC_ObjectIdentity((1,3,111,2,802,1,1,13,1,5,32962,5,1,2,3))
_LldpXdot1dcbxLocPFCBasicTable_Object=MibTable
lldpXdot1dcbxLocPFCBasicTable=_LldpXdot1dcbxLocPFCBasicTable_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,2,3,1))
if mibBuilder.loadTexts:lldpXdot1dcbxLocPFCBasicTable.setStatus(_A)
_LldpXdot1dcbxLocPFCBasicEntry_Object=MibTableRow
lldpXdot1dcbxLocPFCBasicEntry=_LldpXdot1dcbxLocPFCBasicEntry_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,2,3,1,1))
lldpXdot1dcbxLocPFCBasicEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:lldpXdot1dcbxLocPFCBasicEntry.setStatus(_A)
_LldpXdot1dcbxLocPFCWilling_Type=TruthValue
_LldpXdot1dcbxLocPFCWilling_Object=MibTableColumn
lldpXdot1dcbxLocPFCWilling=_LldpXdot1dcbxLocPFCWilling_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,2,3,1,1,1),_LldpXdot1dcbxLocPFCWilling_Type())
lldpXdot1dcbxLocPFCWilling.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpXdot1dcbxLocPFCWilling.setStatus(_A)
_LldpXdot1dcbxLocPFCMBC_Type=TruthValue
_LldpXdot1dcbxLocPFCMBC_Object=MibTableColumn
lldpXdot1dcbxLocPFCMBC=_LldpXdot1dcbxLocPFCMBC_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,2,3,1,1,2),_LldpXdot1dcbxLocPFCMBC_Type())
lldpXdot1dcbxLocPFCMBC.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpXdot1dcbxLocPFCMBC.setStatus(_A)
_LldpXdot1dcbxLocPFCCap_Type=LldpXdot1dcbxSupportedCapacity
_LldpXdot1dcbxLocPFCCap_Object=MibTableColumn
lldpXdot1dcbxLocPFCCap=_LldpXdot1dcbxLocPFCCap_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,2,3,1,1,3),_LldpXdot1dcbxLocPFCCap_Type())
lldpXdot1dcbxLocPFCCap.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpXdot1dcbxLocPFCCap.setStatus(_A)
_LldpXdot1dcbxLocPFCEnableTable_Object=MibTable
lldpXdot1dcbxLocPFCEnableTable=_LldpXdot1dcbxLocPFCEnableTable_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,2,3,2))
if mibBuilder.loadTexts:lldpXdot1dcbxLocPFCEnableTable.setStatus(_A)
_LldpXdot1dcbxLocPFCEnableEntry_Object=MibTableRow
lldpXdot1dcbxLocPFCEnableEntry=_LldpXdot1dcbxLocPFCEnableEntry_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,2,3,2,1))
lldpXdot1dcbxLocPFCEnableEntry.setIndexNames((0,_C,_F),(0,_B,_R))
if mibBuilder.loadTexts:lldpXdot1dcbxLocPFCEnableEntry.setStatus(_A)
_LldpXdot1dcbxLocPFCEnablePriority_Type=IEEE8021PriorityValue
_LldpXdot1dcbxLocPFCEnablePriority_Object=MibTableColumn
lldpXdot1dcbxLocPFCEnablePriority=_LldpXdot1dcbxLocPFCEnablePriority_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,2,3,2,1,1),_LldpXdot1dcbxLocPFCEnablePriority_Type())
lldpXdot1dcbxLocPFCEnablePriority.setMaxAccess(_E)
if mibBuilder.loadTexts:lldpXdot1dcbxLocPFCEnablePriority.setStatus(_A)
_LldpXdot1dcbxLocPFCEnableEnabled_Type=TruthValue
_LldpXdot1dcbxLocPFCEnableEnabled_Object=MibTableColumn
lldpXdot1dcbxLocPFCEnableEnabled=_LldpXdot1dcbxLocPFCEnableEnabled_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,2,3,2,1,2),_LldpXdot1dcbxLocPFCEnableEnabled_Type())
lldpXdot1dcbxLocPFCEnableEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpXdot1dcbxLocPFCEnableEnabled.setStatus(_A)
_LldpXdot1dcbxLocApplicationPriorityAppTable_Object=MibTable
lldpXdot1dcbxLocApplicationPriorityAppTable=_LldpXdot1dcbxLocApplicationPriorityAppTable_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,2,4))
if mibBuilder.loadTexts:lldpXdot1dcbxLocApplicationPriorityAppTable.setStatus(_A)
_LldpXdot1dcbxLocApplicationPriorityAppEntry_Object=MibTableRow
lldpXdot1dcbxLocApplicationPriorityAppEntry=_LldpXdot1dcbxLocApplicationPriorityAppEntry_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,2,4,1))
lldpXdot1dcbxLocApplicationPriorityAppEntry.setIndexNames((0,_C,_F),(0,_B,_S),(0,_B,_T))
if mibBuilder.loadTexts:lldpXdot1dcbxLocApplicationPriorityAppEntry.setStatus(_A)
_LldpXdot1dcbxLocApplicationPriorityAESelector_Type=LldpXdot1dcbxAppSelector
_LldpXdot1dcbxLocApplicationPriorityAESelector_Object=MibTableColumn
lldpXdot1dcbxLocApplicationPriorityAESelector=_LldpXdot1dcbxLocApplicationPriorityAESelector_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,2,4,1,1),_LldpXdot1dcbxLocApplicationPriorityAESelector_Type())
lldpXdot1dcbxLocApplicationPriorityAESelector.setMaxAccess(_E)
if mibBuilder.loadTexts:lldpXdot1dcbxLocApplicationPriorityAESelector.setStatus(_A)
_LldpXdot1dcbxLocApplicationPriorityAEProtocol_Type=LldpXdot1dcbxAppProtocol
_LldpXdot1dcbxLocApplicationPriorityAEProtocol_Object=MibTableColumn
lldpXdot1dcbxLocApplicationPriorityAEProtocol=_LldpXdot1dcbxLocApplicationPriorityAEProtocol_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,2,4,1,2),_LldpXdot1dcbxLocApplicationPriorityAEProtocol_Type())
lldpXdot1dcbxLocApplicationPriorityAEProtocol.setMaxAccess(_E)
if mibBuilder.loadTexts:lldpXdot1dcbxLocApplicationPriorityAEProtocol.setStatus(_A)
_LldpXdot1dcbxLocApplicationPriorityAEPriority_Type=IEEE8021PriorityValue
_LldpXdot1dcbxLocApplicationPriorityAEPriority_Object=MibTableColumn
lldpXdot1dcbxLocApplicationPriorityAEPriority=_LldpXdot1dcbxLocApplicationPriorityAEPriority_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,2,4,1,3),_LldpXdot1dcbxLocApplicationPriorityAEPriority_Type())
lldpXdot1dcbxLocApplicationPriorityAEPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpXdot1dcbxLocApplicationPriorityAEPriority.setStatus(_A)
_LldpXdot1dcbxRemoteData_ObjectIdentity=ObjectIdentity
lldpXdot1dcbxRemoteData=_LldpXdot1dcbxRemoteData_ObjectIdentity((1,3,111,2,802,1,1,13,1,5,32962,5,1,3))
_LldpXdot1dcbxRemETSConfiguration_ObjectIdentity=ObjectIdentity
lldpXdot1dcbxRemETSConfiguration=_LldpXdot1dcbxRemETSConfiguration_ObjectIdentity((1,3,111,2,802,1,1,13,1,5,32962,5,1,3,1))
_LldpXdot1dcbxRemETSBasicConfigurationTable_Object=MibTable
lldpXdot1dcbxRemETSBasicConfigurationTable=_LldpXdot1dcbxRemETSBasicConfigurationTable_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,3,1,1))
if mibBuilder.loadTexts:lldpXdot1dcbxRemETSBasicConfigurationTable.setStatus(_A)
_LldpXdot1dcbxRemETSBasicConfigurationEntry_Object=MibTableRow
lldpXdot1dcbxRemETSBasicConfigurationEntry=_LldpXdot1dcbxRemETSBasicConfigurationEntry_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,3,1,1,1))
lldpXdot1dcbxRemETSBasicConfigurationEntry.setIndexNames((0,_C,_K),(0,_C,_J),(0,_C,_I),(0,_C,_H))
if mibBuilder.loadTexts:lldpXdot1dcbxRemETSBasicConfigurationEntry.setStatus(_A)
_LldpXdot1dcbxRemETSConCreditBasedShaperSupport_Type=TruthValue
_LldpXdot1dcbxRemETSConCreditBasedShaperSupport_Object=MibTableColumn
lldpXdot1dcbxRemETSConCreditBasedShaperSupport=_LldpXdot1dcbxRemETSConCreditBasedShaperSupport_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,3,1,1,1,1),_LldpXdot1dcbxRemETSConCreditBasedShaperSupport_Type())
lldpXdot1dcbxRemETSConCreditBasedShaperSupport.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpXdot1dcbxRemETSConCreditBasedShaperSupport.setStatus(_A)
_LldpXdot1dcbxRemETSConTrafficClassesSupported_Type=LldpXdot1dcbxSupportedCapacity
_LldpXdot1dcbxRemETSConTrafficClassesSupported_Object=MibTableColumn
lldpXdot1dcbxRemETSConTrafficClassesSupported=_LldpXdot1dcbxRemETSConTrafficClassesSupported_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,3,1,1,1,2),_LldpXdot1dcbxRemETSConTrafficClassesSupported_Type())
lldpXdot1dcbxRemETSConTrafficClassesSupported.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpXdot1dcbxRemETSConTrafficClassesSupported.setStatus(_A)
_LldpXdot1dcbxRemETSConWilling_Type=TruthValue
_LldpXdot1dcbxRemETSConWilling_Object=MibTableColumn
lldpXdot1dcbxRemETSConWilling=_LldpXdot1dcbxRemETSConWilling_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,3,1,1,1,3),_LldpXdot1dcbxRemETSConWilling_Type())
lldpXdot1dcbxRemETSConWilling.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpXdot1dcbxRemETSConWilling.setStatus(_A)
_LldpXdot1dcbxRemETSConPriorityAssignmentTable_Object=MibTable
lldpXdot1dcbxRemETSConPriorityAssignmentTable=_LldpXdot1dcbxRemETSConPriorityAssignmentTable_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,3,1,2))
if mibBuilder.loadTexts:lldpXdot1dcbxRemETSConPriorityAssignmentTable.setStatus(_A)
_LldpXdot1dcbxRemETSConPriorityAssignmentEntry_Object=MibTableRow
lldpXdot1dcbxRemETSConPriorityAssignmentEntry=_LldpXdot1dcbxRemETSConPriorityAssignmentEntry_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,3,1,2,1))
lldpXdot1dcbxRemETSConPriorityAssignmentEntry.setIndexNames((0,_C,_K),(0,_C,_J),(0,_C,_I),(0,_C,_H),(0,_B,_U))
if mibBuilder.loadTexts:lldpXdot1dcbxRemETSConPriorityAssignmentEntry.setStatus(_A)
_LldpXdot1dcbxRemETSConPriority_Type=IEEE8021PriorityValue
_LldpXdot1dcbxRemETSConPriority_Object=MibTableColumn
lldpXdot1dcbxRemETSConPriority=_LldpXdot1dcbxRemETSConPriority_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,3,1,2,1,1),_LldpXdot1dcbxRemETSConPriority_Type())
lldpXdot1dcbxRemETSConPriority.setMaxAccess(_E)
if mibBuilder.loadTexts:lldpXdot1dcbxRemETSConPriority.setStatus(_A)
_LldpXdot1dcbxRemETSConPriTrafficClass_Type=LldpXdot1dcbxTrafficClassValue
_LldpXdot1dcbxRemETSConPriTrafficClass_Object=MibTableColumn
lldpXdot1dcbxRemETSConPriTrafficClass=_LldpXdot1dcbxRemETSConPriTrafficClass_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,3,1,2,1,2),_LldpXdot1dcbxRemETSConPriTrafficClass_Type())
lldpXdot1dcbxRemETSConPriTrafficClass.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpXdot1dcbxRemETSConPriTrafficClass.setStatus(_A)
_LldpXdot1dcbxRemETSConTrafficClassBandwidthTable_Object=MibTable
lldpXdot1dcbxRemETSConTrafficClassBandwidthTable=_LldpXdot1dcbxRemETSConTrafficClassBandwidthTable_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,3,1,3))
if mibBuilder.loadTexts:lldpXdot1dcbxRemETSConTrafficClassBandwidthTable.setStatus(_A)
_LldpXdot1dcbxRemETSConTrafficClassBandwidthEntry_Object=MibTableRow
lldpXdot1dcbxRemETSConTrafficClassBandwidthEntry=_LldpXdot1dcbxRemETSConTrafficClassBandwidthEntry_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,3,1,3,1))
lldpXdot1dcbxRemETSConTrafficClassBandwidthEntry.setIndexNames((0,_C,_K),(0,_C,_J),(0,_C,_I),(0,_C,_H),(0,_B,_V))
if mibBuilder.loadTexts:lldpXdot1dcbxRemETSConTrafficClassBandwidthEntry.setStatus(_A)
_LldpXdot1dcbxRemETSConTrafficClass_Type=LldpXdot1dcbxTrafficClassValue
_LldpXdot1dcbxRemETSConTrafficClass_Object=MibTableColumn
lldpXdot1dcbxRemETSConTrafficClass=_LldpXdot1dcbxRemETSConTrafficClass_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,3,1,3,1,1),_LldpXdot1dcbxRemETSConTrafficClass_Type())
lldpXdot1dcbxRemETSConTrafficClass.setMaxAccess(_E)
if mibBuilder.loadTexts:lldpXdot1dcbxRemETSConTrafficClass.setStatus(_A)
_LldpXdot1dcbxRemETSConTrafficClassBandwidth_Type=LldpXdot1dcbxTrafficClassBandwidthValue
_LldpXdot1dcbxRemETSConTrafficClassBandwidth_Object=MibTableColumn
lldpXdot1dcbxRemETSConTrafficClassBandwidth=_LldpXdot1dcbxRemETSConTrafficClassBandwidth_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,3,1,3,1,2),_LldpXdot1dcbxRemETSConTrafficClassBandwidth_Type())
lldpXdot1dcbxRemETSConTrafficClassBandwidth.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpXdot1dcbxRemETSConTrafficClassBandwidth.setStatus(_A)
_LldpXdot1dcbxRemETSConTrafficSelectionAlgorithmTable_Object=MibTable
lldpXdot1dcbxRemETSConTrafficSelectionAlgorithmTable=_LldpXdot1dcbxRemETSConTrafficSelectionAlgorithmTable_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,3,1,4))
if mibBuilder.loadTexts:lldpXdot1dcbxRemETSConTrafficSelectionAlgorithmTable.setStatus(_A)
_LldpXdot1dcbxRemETSConTrafficSelectionAlgorithmEntry_Object=MibTableRow
lldpXdot1dcbxRemETSConTrafficSelectionAlgorithmEntry=_LldpXdot1dcbxRemETSConTrafficSelectionAlgorithmEntry_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,3,1,4,1))
lldpXdot1dcbxRemETSConTrafficSelectionAlgorithmEntry.setIndexNames((0,_C,_K),(0,_C,_J),(0,_C,_I),(0,_C,_H),(0,_B,_W))
if mibBuilder.loadTexts:lldpXdot1dcbxRemETSConTrafficSelectionAlgorithmEntry.setStatus(_A)
_LldpXdot1dcbxRemETSConTSATrafficClass_Type=LldpXdot1dcbxTrafficClassValue
_LldpXdot1dcbxRemETSConTSATrafficClass_Object=MibTableColumn
lldpXdot1dcbxRemETSConTSATrafficClass=_LldpXdot1dcbxRemETSConTSATrafficClass_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,3,1,4,1,1),_LldpXdot1dcbxRemETSConTSATrafficClass_Type())
lldpXdot1dcbxRemETSConTSATrafficClass.setMaxAccess(_E)
if mibBuilder.loadTexts:lldpXdot1dcbxRemETSConTSATrafficClass.setStatus(_A)
_LldpXdot1dcbxRemETSConTrafficSelectionAlgorithm_Type=LldpXdot1dcbxTrafficSelectionAlgorithm
_LldpXdot1dcbxRemETSConTrafficSelectionAlgorithm_Object=MibTableColumn
lldpXdot1dcbxRemETSConTrafficSelectionAlgorithm=_LldpXdot1dcbxRemETSConTrafficSelectionAlgorithm_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,3,1,4,1,2),_LldpXdot1dcbxRemETSConTrafficSelectionAlgorithm_Type())
lldpXdot1dcbxRemETSConTrafficSelectionAlgorithm.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpXdot1dcbxRemETSConTrafficSelectionAlgorithm.setStatus(_A)
_LldpXdot1dcbxRemETSReco_ObjectIdentity=ObjectIdentity
lldpXdot1dcbxRemETSReco=_LldpXdot1dcbxRemETSReco_ObjectIdentity((1,3,111,2,802,1,1,13,1,5,32962,5,1,3,2))
_LldpXdot1dcbxRemETSRecoTrafficClassBandwidthTable_Object=MibTable
lldpXdot1dcbxRemETSRecoTrafficClassBandwidthTable=_LldpXdot1dcbxRemETSRecoTrafficClassBandwidthTable_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,3,2,1))
if mibBuilder.loadTexts:lldpXdot1dcbxRemETSRecoTrafficClassBandwidthTable.setStatus(_A)
_LldpXdot1dcbxRemETSRecoTrafficClassBandwidthEntry_Object=MibTableRow
lldpXdot1dcbxRemETSRecoTrafficClassBandwidthEntry=_LldpXdot1dcbxRemETSRecoTrafficClassBandwidthEntry_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,3,2,1,1))
lldpXdot1dcbxRemETSRecoTrafficClassBandwidthEntry.setIndexNames((0,_C,_K),(0,_C,_J),(0,_C,_I),(0,_C,_H),(0,_B,_X))
if mibBuilder.loadTexts:lldpXdot1dcbxRemETSRecoTrafficClassBandwidthEntry.setStatus(_A)
_LldpXdot1dcbxRemETSRecoTrafficClass_Type=LldpXdot1dcbxTrafficClassValue
_LldpXdot1dcbxRemETSRecoTrafficClass_Object=MibTableColumn
lldpXdot1dcbxRemETSRecoTrafficClass=_LldpXdot1dcbxRemETSRecoTrafficClass_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,3,2,1,1,1),_LldpXdot1dcbxRemETSRecoTrafficClass_Type())
lldpXdot1dcbxRemETSRecoTrafficClass.setMaxAccess(_E)
if mibBuilder.loadTexts:lldpXdot1dcbxRemETSRecoTrafficClass.setStatus(_A)
_LldpXdot1dcbxRemETSRecoTrafficClassBandwidth_Type=LldpXdot1dcbxTrafficClassBandwidthValue
_LldpXdot1dcbxRemETSRecoTrafficClassBandwidth_Object=MibTableColumn
lldpXdot1dcbxRemETSRecoTrafficClassBandwidth=_LldpXdot1dcbxRemETSRecoTrafficClassBandwidth_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,3,2,1,1,2),_LldpXdot1dcbxRemETSRecoTrafficClassBandwidth_Type())
lldpXdot1dcbxRemETSRecoTrafficClassBandwidth.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpXdot1dcbxRemETSRecoTrafficClassBandwidth.setStatus(_A)
_LldpXdot1dcbxRemETSRecoTrafficSelectionAlgorithmTable_Object=MibTable
lldpXdot1dcbxRemETSRecoTrafficSelectionAlgorithmTable=_LldpXdot1dcbxRemETSRecoTrafficSelectionAlgorithmTable_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,3,2,2))
if mibBuilder.loadTexts:lldpXdot1dcbxRemETSRecoTrafficSelectionAlgorithmTable.setStatus(_A)
_LldpXdot1dcbxRemETSRecoTrafficSelectionAlgorithmEntry_Object=MibTableRow
lldpXdot1dcbxRemETSRecoTrafficSelectionAlgorithmEntry=_LldpXdot1dcbxRemETSRecoTrafficSelectionAlgorithmEntry_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,3,2,2,1))
lldpXdot1dcbxRemETSRecoTrafficSelectionAlgorithmEntry.setIndexNames((0,_C,_K),(0,_C,_J),(0,_C,_I),(0,_C,_H),(0,_B,_Y))
if mibBuilder.loadTexts:lldpXdot1dcbxRemETSRecoTrafficSelectionAlgorithmEntry.setStatus(_A)
_LldpXdot1dcbxRemETSRecoTSATrafficClass_Type=LldpXdot1dcbxTrafficClassValue
_LldpXdot1dcbxRemETSRecoTSATrafficClass_Object=MibTableColumn
lldpXdot1dcbxRemETSRecoTSATrafficClass=_LldpXdot1dcbxRemETSRecoTSATrafficClass_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,3,2,2,1,1),_LldpXdot1dcbxRemETSRecoTSATrafficClass_Type())
lldpXdot1dcbxRemETSRecoTSATrafficClass.setMaxAccess(_E)
if mibBuilder.loadTexts:lldpXdot1dcbxRemETSRecoTSATrafficClass.setStatus(_A)
_LldpXdot1dcbxRemETSRecoTrafficSelectionAlgorithm_Type=LldpXdot1dcbxTrafficSelectionAlgorithm
_LldpXdot1dcbxRemETSRecoTrafficSelectionAlgorithm_Object=MibTableColumn
lldpXdot1dcbxRemETSRecoTrafficSelectionAlgorithm=_LldpXdot1dcbxRemETSRecoTrafficSelectionAlgorithm_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,3,2,2,1,2),_LldpXdot1dcbxRemETSRecoTrafficSelectionAlgorithm_Type())
lldpXdot1dcbxRemETSRecoTrafficSelectionAlgorithm.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpXdot1dcbxRemETSRecoTrafficSelectionAlgorithm.setStatus(_A)
_LldpXdot1dcbxRemPFC_ObjectIdentity=ObjectIdentity
lldpXdot1dcbxRemPFC=_LldpXdot1dcbxRemPFC_ObjectIdentity((1,3,111,2,802,1,1,13,1,5,32962,5,1,3,3))
_LldpXdot1dcbxRemPFCBasicTable_Object=MibTable
lldpXdot1dcbxRemPFCBasicTable=_LldpXdot1dcbxRemPFCBasicTable_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,3,3,1))
if mibBuilder.loadTexts:lldpXdot1dcbxRemPFCBasicTable.setStatus(_A)
_LldpXdot1dcbxRemPFCBasicEntry_Object=MibTableRow
lldpXdot1dcbxRemPFCBasicEntry=_LldpXdot1dcbxRemPFCBasicEntry_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,3,3,1,1))
lldpXdot1dcbxRemPFCBasicEntry.setIndexNames((0,_C,_K),(0,_C,_J),(0,_C,_I),(0,_C,_H))
if mibBuilder.loadTexts:lldpXdot1dcbxRemPFCBasicEntry.setStatus(_A)
_LldpXdot1dcbxRemPFCWilling_Type=TruthValue
_LldpXdot1dcbxRemPFCWilling_Object=MibTableColumn
lldpXdot1dcbxRemPFCWilling=_LldpXdot1dcbxRemPFCWilling_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,3,3,1,1,1),_LldpXdot1dcbxRemPFCWilling_Type())
lldpXdot1dcbxRemPFCWilling.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpXdot1dcbxRemPFCWilling.setStatus(_A)
_LldpXdot1dcbxRemPFCMBC_Type=TruthValue
_LldpXdot1dcbxRemPFCMBC_Object=MibTableColumn
lldpXdot1dcbxRemPFCMBC=_LldpXdot1dcbxRemPFCMBC_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,3,3,1,1,2),_LldpXdot1dcbxRemPFCMBC_Type())
lldpXdot1dcbxRemPFCMBC.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpXdot1dcbxRemPFCMBC.setStatus(_A)
_LldpXdot1dcbxRemPFCCap_Type=LldpXdot1dcbxSupportedCapacity
_LldpXdot1dcbxRemPFCCap_Object=MibTableColumn
lldpXdot1dcbxRemPFCCap=_LldpXdot1dcbxRemPFCCap_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,3,3,1,1,3),_LldpXdot1dcbxRemPFCCap_Type())
lldpXdot1dcbxRemPFCCap.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpXdot1dcbxRemPFCCap.setStatus(_A)
_LldpXdot1dcbxRemPFCEnableTable_Object=MibTable
lldpXdot1dcbxRemPFCEnableTable=_LldpXdot1dcbxRemPFCEnableTable_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,3,3,2))
if mibBuilder.loadTexts:lldpXdot1dcbxRemPFCEnableTable.setStatus(_A)
_LldpXdot1dcbxRemPFCEnableEntry_Object=MibTableRow
lldpXdot1dcbxRemPFCEnableEntry=_LldpXdot1dcbxRemPFCEnableEntry_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,3,3,2,1))
lldpXdot1dcbxRemPFCEnableEntry.setIndexNames((0,_C,_K),(0,_C,_J),(0,_C,_I),(0,_C,_H),(0,_B,_Z))
if mibBuilder.loadTexts:lldpXdot1dcbxRemPFCEnableEntry.setStatus(_A)
_LldpXdot1dcbxRemPFCEnablePriority_Type=IEEE8021PriorityValue
_LldpXdot1dcbxRemPFCEnablePriority_Object=MibTableColumn
lldpXdot1dcbxRemPFCEnablePriority=_LldpXdot1dcbxRemPFCEnablePriority_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,3,3,2,1,1),_LldpXdot1dcbxRemPFCEnablePriority_Type())
lldpXdot1dcbxRemPFCEnablePriority.setMaxAccess(_E)
if mibBuilder.loadTexts:lldpXdot1dcbxRemPFCEnablePriority.setStatus(_A)
_LldpXdot1dcbxRemPFCEnableEnabled_Type=TruthValue
_LldpXdot1dcbxRemPFCEnableEnabled_Object=MibTableColumn
lldpXdot1dcbxRemPFCEnableEnabled=_LldpXdot1dcbxRemPFCEnableEnabled_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,3,3,2,1,2),_LldpXdot1dcbxRemPFCEnableEnabled_Type())
lldpXdot1dcbxRemPFCEnableEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpXdot1dcbxRemPFCEnableEnabled.setStatus(_A)
_LldpXdot1dcbxRemApplicationPriorityAppTable_Object=MibTable
lldpXdot1dcbxRemApplicationPriorityAppTable=_LldpXdot1dcbxRemApplicationPriorityAppTable_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,3,4))
if mibBuilder.loadTexts:lldpXdot1dcbxRemApplicationPriorityAppTable.setStatus(_A)
_LldpXdot1dcbxRemApplicationPriorityAppEntry_Object=MibTableRow
lldpXdot1dcbxRemApplicationPriorityAppEntry=_LldpXdot1dcbxRemApplicationPriorityAppEntry_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,3,4,1))
lldpXdot1dcbxRemApplicationPriorityAppEntry.setIndexNames((0,_C,_K),(0,_C,_J),(0,_C,_I),(0,_C,_H),(0,_B,_a),(0,_B,_b))
if mibBuilder.loadTexts:lldpXdot1dcbxRemApplicationPriorityAppEntry.setStatus(_A)
_LldpXdot1dcbxRemApplicationPriorityAESelector_Type=LldpXdot1dcbxAppSelector
_LldpXdot1dcbxRemApplicationPriorityAESelector_Object=MibTableColumn
lldpXdot1dcbxRemApplicationPriorityAESelector=_LldpXdot1dcbxRemApplicationPriorityAESelector_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,3,4,1,1),_LldpXdot1dcbxRemApplicationPriorityAESelector_Type())
lldpXdot1dcbxRemApplicationPriorityAESelector.setMaxAccess(_E)
if mibBuilder.loadTexts:lldpXdot1dcbxRemApplicationPriorityAESelector.setStatus(_A)
_LldpXdot1dcbxRemApplicationPriorityAEProtocol_Type=LldpXdot1dcbxAppProtocol
_LldpXdot1dcbxRemApplicationPriorityAEProtocol_Object=MibTableColumn
lldpXdot1dcbxRemApplicationPriorityAEProtocol=_LldpXdot1dcbxRemApplicationPriorityAEProtocol_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,3,4,1,2),_LldpXdot1dcbxRemApplicationPriorityAEProtocol_Type())
lldpXdot1dcbxRemApplicationPriorityAEProtocol.setMaxAccess(_E)
if mibBuilder.loadTexts:lldpXdot1dcbxRemApplicationPriorityAEProtocol.setStatus(_A)
_LldpXdot1dcbxRemApplicationPriorityAEPriority_Type=IEEE8021PriorityValue
_LldpXdot1dcbxRemApplicationPriorityAEPriority_Object=MibTableColumn
lldpXdot1dcbxRemApplicationPriorityAEPriority=_LldpXdot1dcbxRemApplicationPriorityAEPriority_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,3,4,1,3),_LldpXdot1dcbxRemApplicationPriorityAEPriority_Type())
lldpXdot1dcbxRemApplicationPriorityAEPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpXdot1dcbxRemApplicationPriorityAEPriority.setStatus(_A)
_LldpXdot1dcbxAdminData_ObjectIdentity=ObjectIdentity
lldpXdot1dcbxAdminData=_LldpXdot1dcbxAdminData_ObjectIdentity((1,3,111,2,802,1,1,13,1,5,32962,5,1,4))
_LldpXdot1dcbxAdminETSConfiguration_ObjectIdentity=ObjectIdentity
lldpXdot1dcbxAdminETSConfiguration=_LldpXdot1dcbxAdminETSConfiguration_ObjectIdentity((1,3,111,2,802,1,1,13,1,5,32962,5,1,4,1))
_LldpXdot1dcbxAdminETSBasicConfigurationTable_Object=MibTable
lldpXdot1dcbxAdminETSBasicConfigurationTable=_LldpXdot1dcbxAdminETSBasicConfigurationTable_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,4,1,1))
if mibBuilder.loadTexts:lldpXdot1dcbxAdminETSBasicConfigurationTable.setStatus(_A)
_LldpXdot1dcbxAdminETSBasicConfigurationEntry_Object=MibTableRow
lldpXdot1dcbxAdminETSBasicConfigurationEntry=_LldpXdot1dcbxAdminETSBasicConfigurationEntry_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,4,1,1,1))
lldpXdot1dcbxAdminETSBasicConfigurationEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:lldpXdot1dcbxAdminETSBasicConfigurationEntry.setStatus(_A)
_LldpXdot1dcbxAdminETSConCreditBasedShaperSupport_Type=TruthValue
_LldpXdot1dcbxAdminETSConCreditBasedShaperSupport_Object=MibTableColumn
lldpXdot1dcbxAdminETSConCreditBasedShaperSupport=_LldpXdot1dcbxAdminETSConCreditBasedShaperSupport_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,4,1,1,1,1),_LldpXdot1dcbxAdminETSConCreditBasedShaperSupport_Type())
lldpXdot1dcbxAdminETSConCreditBasedShaperSupport.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpXdot1dcbxAdminETSConCreditBasedShaperSupport.setStatus(_A)
_LldpXdot1dcbxAdminETSConTrafficClassesSupported_Type=LldpXdot1dcbxSupportedCapacity
_LldpXdot1dcbxAdminETSConTrafficClassesSupported_Object=MibTableColumn
lldpXdot1dcbxAdminETSConTrafficClassesSupported=_LldpXdot1dcbxAdminETSConTrafficClassesSupported_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,4,1,1,1,2),_LldpXdot1dcbxAdminETSConTrafficClassesSupported_Type())
lldpXdot1dcbxAdminETSConTrafficClassesSupported.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpXdot1dcbxAdminETSConTrafficClassesSupported.setStatus(_A)
class _LldpXdot1dcbxAdminETSConWilling_Type(TruthValue):defaultValue=2
_LldpXdot1dcbxAdminETSConWilling_Type.__name__=_L
_LldpXdot1dcbxAdminETSConWilling_Object=MibTableColumn
lldpXdot1dcbxAdminETSConWilling=_LldpXdot1dcbxAdminETSConWilling_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,4,1,1,1,3),_LldpXdot1dcbxAdminETSConWilling_Type())
lldpXdot1dcbxAdminETSConWilling.setMaxAccess(_G)
if mibBuilder.loadTexts:lldpXdot1dcbxAdminETSConWilling.setStatus(_A)
_LldpXdot1dcbxAdminETSConPriorityAssignmentTable_Object=MibTable
lldpXdot1dcbxAdminETSConPriorityAssignmentTable=_LldpXdot1dcbxAdminETSConPriorityAssignmentTable_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,4,1,2))
if mibBuilder.loadTexts:lldpXdot1dcbxAdminETSConPriorityAssignmentTable.setStatus(_A)
_LldpXdot1dcbxAdminETSConPriorityAssignmentEntry_Object=MibTableRow
lldpXdot1dcbxAdminETSConPriorityAssignmentEntry=_LldpXdot1dcbxAdminETSConPriorityAssignmentEntry_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,4,1,2,1))
lldpXdot1dcbxAdminETSConPriorityAssignmentEntry.setIndexNames((0,_C,_F),(0,_B,_c))
if mibBuilder.loadTexts:lldpXdot1dcbxAdminETSConPriorityAssignmentEntry.setStatus(_A)
_LldpXdot1dcbxAdminETSConPriority_Type=IEEE8021PriorityValue
_LldpXdot1dcbxAdminETSConPriority_Object=MibTableColumn
lldpXdot1dcbxAdminETSConPriority=_LldpXdot1dcbxAdminETSConPriority_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,4,1,2,1,1),_LldpXdot1dcbxAdminETSConPriority_Type())
lldpXdot1dcbxAdminETSConPriority.setMaxAccess(_E)
if mibBuilder.loadTexts:lldpXdot1dcbxAdminETSConPriority.setStatus(_A)
class _LldpXdot1dcbxAdminETSConPriTrafficClass_Type(LldpXdot1dcbxTrafficClassValue):defaultValue=0
_LldpXdot1dcbxAdminETSConPriTrafficClass_Type.__name__=_d
_LldpXdot1dcbxAdminETSConPriTrafficClass_Object=MibTableColumn
lldpXdot1dcbxAdminETSConPriTrafficClass=_LldpXdot1dcbxAdminETSConPriTrafficClass_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,4,1,2,1,2),_LldpXdot1dcbxAdminETSConPriTrafficClass_Type())
lldpXdot1dcbxAdminETSConPriTrafficClass.setMaxAccess(_G)
if mibBuilder.loadTexts:lldpXdot1dcbxAdminETSConPriTrafficClass.setStatus(_A)
_LldpXdot1dcbxAdminETSConTrafficClassBandwidthTable_Object=MibTable
lldpXdot1dcbxAdminETSConTrafficClassBandwidthTable=_LldpXdot1dcbxAdminETSConTrafficClassBandwidthTable_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,4,1,3))
if mibBuilder.loadTexts:lldpXdot1dcbxAdminETSConTrafficClassBandwidthTable.setStatus(_A)
_LldpXdot1dcbxAdminETSConTrafficClassBandwidthEntry_Object=MibTableRow
lldpXdot1dcbxAdminETSConTrafficClassBandwidthEntry=_LldpXdot1dcbxAdminETSConTrafficClassBandwidthEntry_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,4,1,3,1))
lldpXdot1dcbxAdminETSConTrafficClassBandwidthEntry.setIndexNames((0,_C,_F),(0,_B,_e))
if mibBuilder.loadTexts:lldpXdot1dcbxAdminETSConTrafficClassBandwidthEntry.setStatus(_A)
_LldpXdot1dcbxAdminETSConTrafficClass_Type=LldpXdot1dcbxTrafficClassValue
_LldpXdot1dcbxAdminETSConTrafficClass_Object=MibTableColumn
lldpXdot1dcbxAdminETSConTrafficClass=_LldpXdot1dcbxAdminETSConTrafficClass_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,4,1,3,1,1),_LldpXdot1dcbxAdminETSConTrafficClass_Type())
lldpXdot1dcbxAdminETSConTrafficClass.setMaxAccess(_E)
if mibBuilder.loadTexts:lldpXdot1dcbxAdminETSConTrafficClass.setStatus(_A)
_LldpXdot1dcbxAdminETSConTrafficClassBandwidth_Type=LldpXdot1dcbxTrafficClassBandwidthValue
_LldpXdot1dcbxAdminETSConTrafficClassBandwidth_Object=MibTableColumn
lldpXdot1dcbxAdminETSConTrafficClassBandwidth=_LldpXdot1dcbxAdminETSConTrafficClassBandwidth_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,4,1,3,1,2),_LldpXdot1dcbxAdminETSConTrafficClassBandwidth_Type())
lldpXdot1dcbxAdminETSConTrafficClassBandwidth.setMaxAccess(_G)
if mibBuilder.loadTexts:lldpXdot1dcbxAdminETSConTrafficClassBandwidth.setStatus(_A)
_LldpXdot1dcbxAdminETSConTrafficSelectionAlgorithmTable_Object=MibTable
lldpXdot1dcbxAdminETSConTrafficSelectionAlgorithmTable=_LldpXdot1dcbxAdminETSConTrafficSelectionAlgorithmTable_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,4,1,4))
if mibBuilder.loadTexts:lldpXdot1dcbxAdminETSConTrafficSelectionAlgorithmTable.setStatus(_A)
_LldpXdot1dcbxAdminETSConTrafficSelectionAlgorithmEntry_Object=MibTableRow
lldpXdot1dcbxAdminETSConTrafficSelectionAlgorithmEntry=_LldpXdot1dcbxAdminETSConTrafficSelectionAlgorithmEntry_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,4,1,4,1))
lldpXdot1dcbxAdminETSConTrafficSelectionAlgorithmEntry.setIndexNames((0,_C,_F),(0,_B,_f))
if mibBuilder.loadTexts:lldpXdot1dcbxAdminETSConTrafficSelectionAlgorithmEntry.setStatus(_A)
_LldpXdot1dcbxAdminETSConTSATrafficClass_Type=LldpXdot1dcbxTrafficClassValue
_LldpXdot1dcbxAdminETSConTSATrafficClass_Object=MibTableColumn
lldpXdot1dcbxAdminETSConTSATrafficClass=_LldpXdot1dcbxAdminETSConTSATrafficClass_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,4,1,4,1,1),_LldpXdot1dcbxAdminETSConTSATrafficClass_Type())
lldpXdot1dcbxAdminETSConTSATrafficClass.setMaxAccess(_E)
if mibBuilder.loadTexts:lldpXdot1dcbxAdminETSConTSATrafficClass.setStatus(_A)
_LldpXdot1dcbxAdminETSConTrafficSelectionAlgorithm_Type=LldpXdot1dcbxTrafficSelectionAlgorithm
_LldpXdot1dcbxAdminETSConTrafficSelectionAlgorithm_Object=MibTableColumn
lldpXdot1dcbxAdminETSConTrafficSelectionAlgorithm=_LldpXdot1dcbxAdminETSConTrafficSelectionAlgorithm_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,4,1,4,1,2),_LldpXdot1dcbxAdminETSConTrafficSelectionAlgorithm_Type())
lldpXdot1dcbxAdminETSConTrafficSelectionAlgorithm.setMaxAccess(_G)
if mibBuilder.loadTexts:lldpXdot1dcbxAdminETSConTrafficSelectionAlgorithm.setStatus(_A)
_LldpXdot1dcbxAdminETSReco_ObjectIdentity=ObjectIdentity
lldpXdot1dcbxAdminETSReco=_LldpXdot1dcbxAdminETSReco_ObjectIdentity((1,3,111,2,802,1,1,13,1,5,32962,5,1,4,2))
_LldpXdot1dcbxAdminETSRecoTrafficClassBandwidthTable_Object=MibTable
lldpXdot1dcbxAdminETSRecoTrafficClassBandwidthTable=_LldpXdot1dcbxAdminETSRecoTrafficClassBandwidthTable_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,4,2,1))
if mibBuilder.loadTexts:lldpXdot1dcbxAdminETSRecoTrafficClassBandwidthTable.setStatus(_A)
_LldpXdot1dcbxAdminETSRecoTrafficClassBandwidthEntry_Object=MibTableRow
lldpXdot1dcbxAdminETSRecoTrafficClassBandwidthEntry=_LldpXdot1dcbxAdminETSRecoTrafficClassBandwidthEntry_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,4,2,1,1))
lldpXdot1dcbxAdminETSRecoTrafficClassBandwidthEntry.setIndexNames((0,_C,_F),(0,_B,_g))
if mibBuilder.loadTexts:lldpXdot1dcbxAdminETSRecoTrafficClassBandwidthEntry.setStatus(_A)
_LldpXdot1dcbxAdminETSRecoTrafficClass_Type=LldpXdot1dcbxTrafficClassValue
_LldpXdot1dcbxAdminETSRecoTrafficClass_Object=MibTableColumn
lldpXdot1dcbxAdminETSRecoTrafficClass=_LldpXdot1dcbxAdminETSRecoTrafficClass_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,4,2,1,1,1),_LldpXdot1dcbxAdminETSRecoTrafficClass_Type())
lldpXdot1dcbxAdminETSRecoTrafficClass.setMaxAccess(_E)
if mibBuilder.loadTexts:lldpXdot1dcbxAdminETSRecoTrafficClass.setStatus(_A)
_LldpXdot1dcbxAdminETSRecoTrafficClassBandwidth_Type=LldpXdot1dcbxTrafficClassBandwidthValue
_LldpXdot1dcbxAdminETSRecoTrafficClassBandwidth_Object=MibTableColumn
lldpXdot1dcbxAdminETSRecoTrafficClassBandwidth=_LldpXdot1dcbxAdminETSRecoTrafficClassBandwidth_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,4,2,1,1,2),_LldpXdot1dcbxAdminETSRecoTrafficClassBandwidth_Type())
lldpXdot1dcbxAdminETSRecoTrafficClassBandwidth.setMaxAccess(_G)
if mibBuilder.loadTexts:lldpXdot1dcbxAdminETSRecoTrafficClassBandwidth.setStatus(_A)
_LldpXdot1dcbxAdminETSRecoTrafficSelectionAlgorithmTable_Object=MibTable
lldpXdot1dcbxAdminETSRecoTrafficSelectionAlgorithmTable=_LldpXdot1dcbxAdminETSRecoTrafficSelectionAlgorithmTable_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,4,2,2))
if mibBuilder.loadTexts:lldpXdot1dcbxAdminETSRecoTrafficSelectionAlgorithmTable.setStatus(_A)
_LldpXdot1dcbxAdminETSRecoTrafficSelectionAlgorithmEntry_Object=MibTableRow
lldpXdot1dcbxAdminETSRecoTrafficSelectionAlgorithmEntry=_LldpXdot1dcbxAdminETSRecoTrafficSelectionAlgorithmEntry_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,4,2,2,1))
lldpXdot1dcbxAdminETSRecoTrafficSelectionAlgorithmEntry.setIndexNames((0,_C,_F),(0,_B,_h))
if mibBuilder.loadTexts:lldpXdot1dcbxAdminETSRecoTrafficSelectionAlgorithmEntry.setStatus(_A)
_LldpXdot1dcbxAdminETSRecoTSATrafficClass_Type=LldpXdot1dcbxTrafficClassValue
_LldpXdot1dcbxAdminETSRecoTSATrafficClass_Object=MibTableColumn
lldpXdot1dcbxAdminETSRecoTSATrafficClass=_LldpXdot1dcbxAdminETSRecoTSATrafficClass_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,4,2,2,1,1),_LldpXdot1dcbxAdminETSRecoTSATrafficClass_Type())
lldpXdot1dcbxAdminETSRecoTSATrafficClass.setMaxAccess(_E)
if mibBuilder.loadTexts:lldpXdot1dcbxAdminETSRecoTSATrafficClass.setStatus(_A)
_LldpXdot1dcbxAdminETSRecoTrafficSelectionAlgorithm_Type=LldpXdot1dcbxTrafficSelectionAlgorithm
_LldpXdot1dcbxAdminETSRecoTrafficSelectionAlgorithm_Object=MibTableColumn
lldpXdot1dcbxAdminETSRecoTrafficSelectionAlgorithm=_LldpXdot1dcbxAdminETSRecoTrafficSelectionAlgorithm_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,4,2,2,1,2),_LldpXdot1dcbxAdminETSRecoTrafficSelectionAlgorithm_Type())
lldpXdot1dcbxAdminETSRecoTrafficSelectionAlgorithm.setMaxAccess(_G)
if mibBuilder.loadTexts:lldpXdot1dcbxAdminETSRecoTrafficSelectionAlgorithm.setStatus(_A)
_LldpXdot1dcbxAdminPFC_ObjectIdentity=ObjectIdentity
lldpXdot1dcbxAdminPFC=_LldpXdot1dcbxAdminPFC_ObjectIdentity((1,3,111,2,802,1,1,13,1,5,32962,5,1,4,3))
_LldpXdot1dcbxAdminPFCBasicTable_Object=MibTable
lldpXdot1dcbxAdminPFCBasicTable=_LldpXdot1dcbxAdminPFCBasicTable_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,4,3,1))
if mibBuilder.loadTexts:lldpXdot1dcbxAdminPFCBasicTable.setStatus(_A)
_LldpXdot1dcbxAdminPFCBasicEntry_Object=MibTableRow
lldpXdot1dcbxAdminPFCBasicEntry=_LldpXdot1dcbxAdminPFCBasicEntry_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,4,3,1,1))
lldpXdot1dcbxAdminPFCBasicEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:lldpXdot1dcbxAdminPFCBasicEntry.setStatus(_A)
class _LldpXdot1dcbxAdminPFCWilling_Type(TruthValue):defaultValue=2
_LldpXdot1dcbxAdminPFCWilling_Type.__name__=_L
_LldpXdot1dcbxAdminPFCWilling_Object=MibTableColumn
lldpXdot1dcbxAdminPFCWilling=_LldpXdot1dcbxAdminPFCWilling_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,4,3,1,1,1),_LldpXdot1dcbxAdminPFCWilling_Type())
lldpXdot1dcbxAdminPFCWilling.setMaxAccess(_G)
if mibBuilder.loadTexts:lldpXdot1dcbxAdminPFCWilling.setStatus(_A)
_LldpXdot1dcbxAdminPFCMBC_Type=TruthValue
_LldpXdot1dcbxAdminPFCMBC_Object=MibTableColumn
lldpXdot1dcbxAdminPFCMBC=_LldpXdot1dcbxAdminPFCMBC_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,4,3,1,1,2),_LldpXdot1dcbxAdminPFCMBC_Type())
lldpXdot1dcbxAdminPFCMBC.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpXdot1dcbxAdminPFCMBC.setStatus(_A)
_LldpXdot1dcbxAdminPFCCap_Type=LldpXdot1dcbxSupportedCapacity
_LldpXdot1dcbxAdminPFCCap_Object=MibTableColumn
lldpXdot1dcbxAdminPFCCap=_LldpXdot1dcbxAdminPFCCap_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,4,3,1,1,3),_LldpXdot1dcbxAdminPFCCap_Type())
lldpXdot1dcbxAdminPFCCap.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpXdot1dcbxAdminPFCCap.setStatus(_A)
_LldpXdot1dcbxAdminPFCEnableTable_Object=MibTable
lldpXdot1dcbxAdminPFCEnableTable=_LldpXdot1dcbxAdminPFCEnableTable_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,4,3,2))
if mibBuilder.loadTexts:lldpXdot1dcbxAdminPFCEnableTable.setStatus(_A)
_LldpXdot1dcbxAdminPFCEnableEntry_Object=MibTableRow
lldpXdot1dcbxAdminPFCEnableEntry=_LldpXdot1dcbxAdminPFCEnableEntry_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,4,3,2,1))
lldpXdot1dcbxAdminPFCEnableEntry.setIndexNames((0,_C,_F),(0,_B,_i))
if mibBuilder.loadTexts:lldpXdot1dcbxAdminPFCEnableEntry.setStatus(_A)
_LldpXdot1dcbxAdminPFCEnablePriority_Type=IEEE8021PriorityValue
_LldpXdot1dcbxAdminPFCEnablePriority_Object=MibTableColumn
lldpXdot1dcbxAdminPFCEnablePriority=_LldpXdot1dcbxAdminPFCEnablePriority_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,4,3,2,1,1),_LldpXdot1dcbxAdminPFCEnablePriority_Type())
lldpXdot1dcbxAdminPFCEnablePriority.setMaxAccess(_E)
if mibBuilder.loadTexts:lldpXdot1dcbxAdminPFCEnablePriority.setStatus(_A)
class _LldpXdot1dcbxAdminPFCEnableEnabled_Type(TruthValue):defaultValue=2
_LldpXdot1dcbxAdminPFCEnableEnabled_Type.__name__=_L
_LldpXdot1dcbxAdminPFCEnableEnabled_Object=MibTableColumn
lldpXdot1dcbxAdminPFCEnableEnabled=_LldpXdot1dcbxAdminPFCEnableEnabled_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,4,3,2,1,2),_LldpXdot1dcbxAdminPFCEnableEnabled_Type())
lldpXdot1dcbxAdminPFCEnableEnabled.setMaxAccess(_G)
if mibBuilder.loadTexts:lldpXdot1dcbxAdminPFCEnableEnabled.setStatus(_A)
_LldpXdot1dcbxAdminApplicationPriorityAppTable_Object=MibTable
lldpXdot1dcbxAdminApplicationPriorityAppTable=_LldpXdot1dcbxAdminApplicationPriorityAppTable_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,4,4))
if mibBuilder.loadTexts:lldpXdot1dcbxAdminApplicationPriorityAppTable.setStatus(_A)
_LldpXdot1dcbxAdminApplicationPriorityAppEntry_Object=MibTableRow
lldpXdot1dcbxAdminApplicationPriorityAppEntry=_LldpXdot1dcbxAdminApplicationPriorityAppEntry_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,4,4,1))
lldpXdot1dcbxAdminApplicationPriorityAppEntry.setIndexNames((0,_C,_F),(0,_B,_j),(0,_B,_k))
if mibBuilder.loadTexts:lldpXdot1dcbxAdminApplicationPriorityAppEntry.setStatus(_A)
_LldpXdot1dcbxAdminApplicationPriorityAESelector_Type=LldpXdot1dcbxAppSelector
_LldpXdot1dcbxAdminApplicationPriorityAESelector_Object=MibTableColumn
lldpXdot1dcbxAdminApplicationPriorityAESelector=_LldpXdot1dcbxAdminApplicationPriorityAESelector_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,4,4,1,1),_LldpXdot1dcbxAdminApplicationPriorityAESelector_Type())
lldpXdot1dcbxAdminApplicationPriorityAESelector.setMaxAccess(_E)
if mibBuilder.loadTexts:lldpXdot1dcbxAdminApplicationPriorityAESelector.setStatus(_A)
_LldpXdot1dcbxAdminApplicationPriorityAEProtocol_Type=LldpXdot1dcbxAppProtocol
_LldpXdot1dcbxAdminApplicationPriorityAEProtocol_Object=MibTableColumn
lldpXdot1dcbxAdminApplicationPriorityAEProtocol=_LldpXdot1dcbxAdminApplicationPriorityAEProtocol_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,4,4,1,2),_LldpXdot1dcbxAdminApplicationPriorityAEProtocol_Type())
lldpXdot1dcbxAdminApplicationPriorityAEProtocol.setMaxAccess(_E)
if mibBuilder.loadTexts:lldpXdot1dcbxAdminApplicationPriorityAEProtocol.setStatus(_A)
_LldpXdot1dcbxAdminApplicationPriorityAEPriority_Type=IEEE8021PriorityValue
_LldpXdot1dcbxAdminApplicationPriorityAEPriority_Object=MibTableColumn
lldpXdot1dcbxAdminApplicationPriorityAEPriority=_LldpXdot1dcbxAdminApplicationPriorityAEPriority_Object((1,3,111,2,802,1,1,13,1,5,32962,5,1,4,4,1,3),_LldpXdot1dcbxAdminApplicationPriorityAEPriority_Type())
lldpXdot1dcbxAdminApplicationPriorityAEPriority.setMaxAccess('read-create')
if mibBuilder.loadTexts:lldpXdot1dcbxAdminApplicationPriorityAEPriority.setStatus(_A)
_LldpXdot1dcbxConformance_ObjectIdentity=ObjectIdentity
lldpXdot1dcbxConformance=_LldpXdot1dcbxConformance_ObjectIdentity((1,3,111,2,802,1,1,13,1,5,32962,6))
_LldpXdot1dcbxCompliances_ObjectIdentity=ObjectIdentity
lldpXdot1dcbxCompliances=_LldpXdot1dcbxCompliances_ObjectIdentity((1,3,111,2,802,1,1,13,1,5,32962,6,1))
_LldpXdot1dcbxGroups_ObjectIdentity=ObjectIdentity
lldpXdot1dcbxGroups=_LldpXdot1dcbxGroups_ObjectIdentity((1,3,111,2,802,1,1,13,1,5,32962,6,2))
lldpV2PortConfigEntry.registerAugmentions((_B,_l))
lldpXdot1dcbxConfigETSConfigurationEntry.setIndexNames(*lldpV2PortConfigEntry.getIndexNames())
lldpV2PortConfigEntry.registerAugmentions((_B,_m))
lldpXdot1dcbxConfigETSRecommendationEntry.setIndexNames(*lldpV2PortConfigEntry.getIndexNames())
lldpV2PortConfigEntry.registerAugmentions((_B,_n))
lldpXdot1dcbxConfigPFCEntry.setIndexNames(*lldpV2PortConfigEntry.getIndexNames())
lldpV2PortConfigEntry.registerAugmentions((_B,_o))
lldpXdot1dcbxConfigApplicationPriorityEntry.setIndexNames(*lldpV2PortConfigEntry.getIndexNames())
lldpXdot1dcbxETSGroup=ObjectGroup((1,3,111,2,802,1,1,13,1,5,32962,6,2,1))
lldpXdot1dcbxETSGroup.setObjects(*((_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE)))
if mibBuilder.loadTexts:lldpXdot1dcbxETSGroup.setStatus(_A)
lldpXdot1dcbxPFCGroup=ObjectGroup((1,3,111,2,802,1,1,13,1,5,32962,6,2,2))
lldpXdot1dcbxPFCGroup.setObjects(*((_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR)))
if mibBuilder.loadTexts:lldpXdot1dcbxPFCGroup.setStatus(_A)
lldpXdot1dcbxApplicationPriorityGroup=ObjectGroup((1,3,111,2,802,1,1,13,1,5,32962,6,2,3))
lldpXdot1dcbxApplicationPriorityGroup.setObjects(*((_B,_AS),(_B,_AT),(_B,_AU),(_B,_AV)))
if mibBuilder.loadTexts:lldpXdot1dcbxApplicationPriorityGroup.setStatus(_A)
lldpXdot1dcbxCompliance=ModuleCompliance((1,3,111,2,802,1,1,13,1,5,32962,6,1,1))
lldpXdot1dcbxCompliance.setObjects(*((_B,_AW),(_B,_AX),(_B,_AY),(_B,'ifGeneralInformationGroup')))
if mibBuilder.loadTexts:lldpXdot1dcbxCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_d:LldpXdot1dcbxTrafficClassValue,'LldpXdot1dcbxTrafficClassBandwidthValue':LldpXdot1dcbxTrafficClassBandwidthValue,'LldpXdot1dcbxAppSelector':LldpXdot1dcbxAppSelector,'LldpXdot1dcbxAppProtocol':LldpXdot1dcbxAppProtocol,'LldpXdot1dcbxSupportedCapacity':LldpXdot1dcbxSupportedCapacity,'LldpXdot1dcbxTrafficSelectionAlgorithm':LldpXdot1dcbxTrafficSelectionAlgorithm,'lldpXdot1dcbxMIB':lldpXdot1dcbxMIB,'lldpXdot1dcbxObjects':lldpXdot1dcbxObjects,'lldpXdot1dcbxConfig':lldpXdot1dcbxConfig,'lldpXdot1dcbxConfigETSConfigurationTable':lldpXdot1dcbxConfigETSConfigurationTable,_l:lldpXdot1dcbxConfigETSConfigurationEntry,_p:lldpXdot1dcbxConfigETSConfigurationTxEnable,'lldpXdot1dcbxConfigETSRecommendationTable':lldpXdot1dcbxConfigETSRecommendationTable,_m:lldpXdot1dcbxConfigETSRecommendationEntry,_q:lldpXdot1dcbxConfigETSRecommendationTxEnable,'lldpXdot1dcbxConfigPFCTable':lldpXdot1dcbxConfigPFCTable,_n:lldpXdot1dcbxConfigPFCEntry,_AF:lldpXdot1dcbxConfigPFCTxEnable,'lldpXdot1dcbxConfigApplicationPriorityTable':lldpXdot1dcbxConfigApplicationPriorityTable,_o:lldpXdot1dcbxConfigApplicationPriorityEntry,_AS:lldpXdot1dcbxConfigApplicationPriorityTxEnable,'lldpXdot1dcbxLocalData':lldpXdot1dcbxLocalData,'lldpXdot1dcbxLocETSConfiguration':lldpXdot1dcbxLocETSConfiguration,'lldpXdot1dcbxLocETSBasicConfigurationTable':lldpXdot1dcbxLocETSBasicConfigurationTable,'lldpXdot1dcbxLocETSBasicConfigurationEntry':lldpXdot1dcbxLocETSBasicConfigurationEntry,_r:lldpXdot1dcbxLocETSConCreditBasedShaperSupport,_s:lldpXdot1dcbxLocETSConTrafficClassesSupported,_t:lldpXdot1dcbxLocETSConWilling,'lldpXdot1dcbxLocETSConPriorityAssignmentTable':lldpXdot1dcbxLocETSConPriorityAssignmentTable,'lldpXdot1dcbxLocETSConPriorityAssignmentEntry':lldpXdot1dcbxLocETSConPriorityAssignmentEntry,_M:lldpXdot1dcbxLocETSConPriority,_u:lldpXdot1dcbxLocETSConPriTrafficClass,'lldpXdot1dcbxLocETSConTrafficClassBandwidthTable':lldpXdot1dcbxLocETSConTrafficClassBandwidthTable,'lldpXdot1dcbxLocETSConTrafficClassBandwidthEntry':lldpXdot1dcbxLocETSConTrafficClassBandwidthEntry,_N:lldpXdot1dcbxLocETSConTrafficClass,_v:lldpXdot1dcbxLocETSConTrafficClassBandwidth,'lldpXdot1dcbxLocETSConTrafficSelectionAlgorithmTable':lldpXdot1dcbxLocETSConTrafficSelectionAlgorithmTable,'lldpXdot1dcbxLocETSConTrafficSelectionAlgorithmEntry':lldpXdot1dcbxLocETSConTrafficSelectionAlgorithmEntry,_O:lldpXdot1dcbxLocETSConTSATrafficClass,_w:lldpXdot1dcbxLocETSConTrafficSelectionAlgorithm,'lldpXdot1dcbxLocETSReco':lldpXdot1dcbxLocETSReco,'lldpXdot1dcbxLocETSRecoTrafficClassBandwidthTable':lldpXdot1dcbxLocETSRecoTrafficClassBandwidthTable,'lldpXdot1dcbxLocETSRecoTrafficClassBandwidthEntry':lldpXdot1dcbxLocETSRecoTrafficClassBandwidthEntry,_P:lldpXdot1dcbxLocETSRecoTrafficClass,_x:lldpXdot1dcbxLocETSRecoTrafficClassBandwidth,'lldpXdot1dcbxLocETSRecoTrafficSelectionAlgorithmTable':lldpXdot1dcbxLocETSRecoTrafficSelectionAlgorithmTable,'lldpXdot1dcbxLocETSRecoTrafficSelectionAlgorithmEntry':lldpXdot1dcbxLocETSRecoTrafficSelectionAlgorithmEntry,_Q:lldpXdot1dcbxLocETSRecoTSATrafficClass,_y:lldpXdot1dcbxLocETSRecoTrafficSelectionAlgorithm,'lldpXdot1dcbxLocPFC':lldpXdot1dcbxLocPFC,'lldpXdot1dcbxLocPFCBasicTable':lldpXdot1dcbxLocPFCBasicTable,'lldpXdot1dcbxLocPFCBasicEntry':lldpXdot1dcbxLocPFCBasicEntry,_AG:lldpXdot1dcbxLocPFCWilling,_AH:lldpXdot1dcbxLocPFCMBC,_AI:lldpXdot1dcbxLocPFCCap,'lldpXdot1dcbxLocPFCEnableTable':lldpXdot1dcbxLocPFCEnableTable,'lldpXdot1dcbxLocPFCEnableEntry':lldpXdot1dcbxLocPFCEnableEntry,_R:lldpXdot1dcbxLocPFCEnablePriority,_AJ:lldpXdot1dcbxLocPFCEnableEnabled,'lldpXdot1dcbxLocApplicationPriorityAppTable':lldpXdot1dcbxLocApplicationPriorityAppTable,'lldpXdot1dcbxLocApplicationPriorityAppEntry':lldpXdot1dcbxLocApplicationPriorityAppEntry,_S:lldpXdot1dcbxLocApplicationPriorityAESelector,_T:lldpXdot1dcbxLocApplicationPriorityAEProtocol,_AT:lldpXdot1dcbxLocApplicationPriorityAEPriority,'lldpXdot1dcbxRemoteData':lldpXdot1dcbxRemoteData,'lldpXdot1dcbxRemETSConfiguration':lldpXdot1dcbxRemETSConfiguration,'lldpXdot1dcbxRemETSBasicConfigurationTable':lldpXdot1dcbxRemETSBasicConfigurationTable,'lldpXdot1dcbxRemETSBasicConfigurationEntry':lldpXdot1dcbxRemETSBasicConfigurationEntry,_z:lldpXdot1dcbxRemETSConCreditBasedShaperSupport,_A0:lldpXdot1dcbxRemETSConTrafficClassesSupported,_A1:lldpXdot1dcbxRemETSConWilling,'lldpXdot1dcbxRemETSConPriorityAssignmentTable':lldpXdot1dcbxRemETSConPriorityAssignmentTable,'lldpXdot1dcbxRemETSConPriorityAssignmentEntry':lldpXdot1dcbxRemETSConPriorityAssignmentEntry,_U:lldpXdot1dcbxRemETSConPriority,_A2:lldpXdot1dcbxRemETSConPriTrafficClass,'lldpXdot1dcbxRemETSConTrafficClassBandwidthTable':lldpXdot1dcbxRemETSConTrafficClassBandwidthTable,'lldpXdot1dcbxRemETSConTrafficClassBandwidthEntry':lldpXdot1dcbxRemETSConTrafficClassBandwidthEntry,_V:lldpXdot1dcbxRemETSConTrafficClass,_A3:lldpXdot1dcbxRemETSConTrafficClassBandwidth,'lldpXdot1dcbxRemETSConTrafficSelectionAlgorithmTable':lldpXdot1dcbxRemETSConTrafficSelectionAlgorithmTable,'lldpXdot1dcbxRemETSConTrafficSelectionAlgorithmEntry':lldpXdot1dcbxRemETSConTrafficSelectionAlgorithmEntry,_W:lldpXdot1dcbxRemETSConTSATrafficClass,_A4:lldpXdot1dcbxRemETSConTrafficSelectionAlgorithm,'lldpXdot1dcbxRemETSReco':lldpXdot1dcbxRemETSReco,'lldpXdot1dcbxRemETSRecoTrafficClassBandwidthTable':lldpXdot1dcbxRemETSRecoTrafficClassBandwidthTable,'lldpXdot1dcbxRemETSRecoTrafficClassBandwidthEntry':lldpXdot1dcbxRemETSRecoTrafficClassBandwidthEntry,_X:lldpXdot1dcbxRemETSRecoTrafficClass,_A5:lldpXdot1dcbxRemETSRecoTrafficClassBandwidth,'lldpXdot1dcbxRemETSRecoTrafficSelectionAlgorithmTable':lldpXdot1dcbxRemETSRecoTrafficSelectionAlgorithmTable,'lldpXdot1dcbxRemETSRecoTrafficSelectionAlgorithmEntry':lldpXdot1dcbxRemETSRecoTrafficSelectionAlgorithmEntry,_Y:lldpXdot1dcbxRemETSRecoTSATrafficClass,_A6:lldpXdot1dcbxRemETSRecoTrafficSelectionAlgorithm,'lldpXdot1dcbxRemPFC':lldpXdot1dcbxRemPFC,'lldpXdot1dcbxRemPFCBasicTable':lldpXdot1dcbxRemPFCBasicTable,'lldpXdot1dcbxRemPFCBasicEntry':lldpXdot1dcbxRemPFCBasicEntry,_AK:lldpXdot1dcbxRemPFCWilling,_AL:lldpXdot1dcbxRemPFCMBC,_AM:lldpXdot1dcbxRemPFCCap,'lldpXdot1dcbxRemPFCEnableTable':lldpXdot1dcbxRemPFCEnableTable,'lldpXdot1dcbxRemPFCEnableEntry':lldpXdot1dcbxRemPFCEnableEntry,_Z:lldpXdot1dcbxRemPFCEnablePriority,_AN:lldpXdot1dcbxRemPFCEnableEnabled,'lldpXdot1dcbxRemApplicationPriorityAppTable':lldpXdot1dcbxRemApplicationPriorityAppTable,'lldpXdot1dcbxRemApplicationPriorityAppEntry':lldpXdot1dcbxRemApplicationPriorityAppEntry,_a:lldpXdot1dcbxRemApplicationPriorityAESelector,_b:lldpXdot1dcbxRemApplicationPriorityAEProtocol,_AU:lldpXdot1dcbxRemApplicationPriorityAEPriority,'lldpXdot1dcbxAdminData':lldpXdot1dcbxAdminData,'lldpXdot1dcbxAdminETSConfiguration':lldpXdot1dcbxAdminETSConfiguration,'lldpXdot1dcbxAdminETSBasicConfigurationTable':lldpXdot1dcbxAdminETSBasicConfigurationTable,'lldpXdot1dcbxAdminETSBasicConfigurationEntry':lldpXdot1dcbxAdminETSBasicConfigurationEntry,_A7:lldpXdot1dcbxAdminETSConCreditBasedShaperSupport,_A8:lldpXdot1dcbxAdminETSConTrafficClassesSupported,_A9:lldpXdot1dcbxAdminETSConWilling,'lldpXdot1dcbxAdminETSConPriorityAssignmentTable':lldpXdot1dcbxAdminETSConPriorityAssignmentTable,'lldpXdot1dcbxAdminETSConPriorityAssignmentEntry':lldpXdot1dcbxAdminETSConPriorityAssignmentEntry,_c:lldpXdot1dcbxAdminETSConPriority,_AA:lldpXdot1dcbxAdminETSConPriTrafficClass,'lldpXdot1dcbxAdminETSConTrafficClassBandwidthTable':lldpXdot1dcbxAdminETSConTrafficClassBandwidthTable,'lldpXdot1dcbxAdminETSConTrafficClassBandwidthEntry':lldpXdot1dcbxAdminETSConTrafficClassBandwidthEntry,_e:lldpXdot1dcbxAdminETSConTrafficClass,_AB:lldpXdot1dcbxAdminETSConTrafficClassBandwidth,'lldpXdot1dcbxAdminETSConTrafficSelectionAlgorithmTable':lldpXdot1dcbxAdminETSConTrafficSelectionAlgorithmTable,'lldpXdot1dcbxAdminETSConTrafficSelectionAlgorithmEntry':lldpXdot1dcbxAdminETSConTrafficSelectionAlgorithmEntry,_f:lldpXdot1dcbxAdminETSConTSATrafficClass,_AC:lldpXdot1dcbxAdminETSConTrafficSelectionAlgorithm,'lldpXdot1dcbxAdminETSReco':lldpXdot1dcbxAdminETSReco,'lldpXdot1dcbxAdminETSRecoTrafficClassBandwidthTable':lldpXdot1dcbxAdminETSRecoTrafficClassBandwidthTable,'lldpXdot1dcbxAdminETSRecoTrafficClassBandwidthEntry':lldpXdot1dcbxAdminETSRecoTrafficClassBandwidthEntry,_g:lldpXdot1dcbxAdminETSRecoTrafficClass,_AD:lldpXdot1dcbxAdminETSRecoTrafficClassBandwidth,'lldpXdot1dcbxAdminETSRecoTrafficSelectionAlgorithmTable':lldpXdot1dcbxAdminETSRecoTrafficSelectionAlgorithmTable,'lldpXdot1dcbxAdminETSRecoTrafficSelectionAlgorithmEntry':lldpXdot1dcbxAdminETSRecoTrafficSelectionAlgorithmEntry,_h:lldpXdot1dcbxAdminETSRecoTSATrafficClass,_AE:lldpXdot1dcbxAdminETSRecoTrafficSelectionAlgorithm,'lldpXdot1dcbxAdminPFC':lldpXdot1dcbxAdminPFC,'lldpXdot1dcbxAdminPFCBasicTable':lldpXdot1dcbxAdminPFCBasicTable,'lldpXdot1dcbxAdminPFCBasicEntry':lldpXdot1dcbxAdminPFCBasicEntry,_AO:lldpXdot1dcbxAdminPFCWilling,_AP:lldpXdot1dcbxAdminPFCMBC,_AQ:lldpXdot1dcbxAdminPFCCap,'lldpXdot1dcbxAdminPFCEnableTable':lldpXdot1dcbxAdminPFCEnableTable,'lldpXdot1dcbxAdminPFCEnableEntry':lldpXdot1dcbxAdminPFCEnableEntry,_i:lldpXdot1dcbxAdminPFCEnablePriority,_AR:lldpXdot1dcbxAdminPFCEnableEnabled,'lldpXdot1dcbxAdminApplicationPriorityAppTable':lldpXdot1dcbxAdminApplicationPriorityAppTable,'lldpXdot1dcbxAdminApplicationPriorityAppEntry':lldpXdot1dcbxAdminApplicationPriorityAppEntry,_j:lldpXdot1dcbxAdminApplicationPriorityAESelector,_k:lldpXdot1dcbxAdminApplicationPriorityAEProtocol,_AV:lldpXdot1dcbxAdminApplicationPriorityAEPriority,'lldpXdot1dcbxConformance':lldpXdot1dcbxConformance,'lldpXdot1dcbxCompliances':lldpXdot1dcbxCompliances,'lldpXdot1dcbxCompliance':lldpXdot1dcbxCompliance,'lldpXdot1dcbxGroups':lldpXdot1dcbxGroups,_AW:lldpXdot1dcbxETSGroup,_AX:lldpXdot1dcbxPFCGroup,_AY:lldpXdot1dcbxApplicationPriorityGroup})