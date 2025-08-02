_Y='EqlVlanIdentifier'
_X='6400000000000000'
_W='TimeInterval'
_V='Integer32'
_U='EqlDcbxAppProtocol'
_T='EqlDcbxSupportedCapacity'
_S='off'
_R='ifIndex'
_Q='IF-MIB'
_P='eqlMemberIndex'
_O='EQLMEMBER-MIB'
_N='eqlGroupId'
_M='EQLGROUP-MIB'
_L='Mbit/s'
_K='EqlIEEE8021PriorityValue'
_J='EqlIEEEDraftSubtypeValue'
_I='OctetString'
_H='Unsigned32'
_G='deprecated'
_F='EqlDcbxTransmissionSelectionAlgorithm'
_E='EqlDcbxTrafficClassGroupValue'
_D='TruthValue'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_I,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
eqlGroupId,=mibBuilder.importSymbols(_M,_N)
eqlMemberIndex,=mibBuilder.importSymbols(_O,_P)
equalLogic,=mibBuilder.importSymbols('EQUALLOGIC-SMI','equalLogic')
ifIndex,=mibBuilder.importSymbols(_Q,_R)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_V,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_H,'enterprises','iso')
DisplayString,PhysAddress,TextualConvention,TimeInterval,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_W,_D)
eqlDcbMib=ModuleIdentity((1,3,6,1,4,1,12740,19))
if mibBuilder.loadTexts:eqlDcbMib.setRevisions(('2011-01-27 00:00',))
class EqlDcbxTrafficClassGroupValue(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
class EqlDcbxAppSelector(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('asEthertype',0),('asTCPPortNumber',1),('asUDPPortNumber',2),('asTCPUDPPortNumber',3),('asNotTCPUDPPortNumber',4)))
class EqlDcbxAppProtocol(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
class EqlDcbxSupportedCapacity(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8))
class EqlVlanIdentifier(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,4094),ValueRangeConstraint(4095,4095))
class EqlIEEE8021PriorityValue(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
class EqlIEEEDraftSubtypeValue(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
class EqlDcbxState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_S,0),('on',1),('disabled',2)))
class EqlDcbxVlanState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_S,0),('static',1),('dynamic',2)))
class EqlDcbxTransmissionSelectionAlgorithm(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,255)));namedValues=NamedValues(*(('tsaStrictPriority',0),('tsaCreditBasedShaper',1),('tsaEnhancedTransmission',2),('tsaVendorSpecific',255)))
class EqlDcbxMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_S,0),('dcbx101Baseline',1),('dcbxIeeeStandard',2)))
_EqlDcbMIBObjects_ObjectIdentity=ObjectIdentity
eqlDcbMIBObjects=_EqlDcbMIBObjects_ObjectIdentity((1,3,6,1,4,1,12740,19,1))
_EqlDcbStaticIfTable_Object=MibTable
eqlDcbStaticIfTable=_EqlDcbStaticIfTable_Object((1,3,6,1,4,1,12740,19,1,1))
if mibBuilder.loadTexts:eqlDcbStaticIfTable.setStatus(_A)
_EqlDcbStaticIfEntry_Object=MibTableRow
eqlDcbStaticIfEntry=_EqlDcbStaticIfEntry_Object((1,3,6,1,4,1,12740,19,1,1,1))
eqlDcbStaticIfEntry.setIndexNames((0,_M,_N),(0,_O,_P),(0,_Q,_R))
if mibBuilder.loadTexts:eqlDcbStaticIfEntry.setStatus(_A)
_EqlDcbxConfigTCSupportedTxEnable_Type=TruthValue
_EqlDcbxConfigTCSupportedTxEnable_Object=MibTableColumn
eqlDcbxConfigTCSupportedTxEnable=_EqlDcbxConfigTCSupportedTxEnable_Object((1,3,6,1,4,1,12740,19,1,1,1,1),_EqlDcbxConfigTCSupportedTxEnable_Type())
eqlDcbxConfigTCSupportedTxEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:eqlDcbxConfigTCSupportedTxEnable.setStatus(_G)
class _EqlDcbxConfigETSConfigurationTxEnable_Type(TruthValue):defaultValue=1
_EqlDcbxConfigETSConfigurationTxEnable_Type.__name__=_D
_EqlDcbxConfigETSConfigurationTxEnable_Object=MibTableColumn
eqlDcbxConfigETSConfigurationTxEnable=_EqlDcbxConfigETSConfigurationTxEnable_Object((1,3,6,1,4,1,12740,19,1,1,1,2),_EqlDcbxConfigETSConfigurationTxEnable_Type())
eqlDcbxConfigETSConfigurationTxEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:eqlDcbxConfigETSConfigurationTxEnable.setStatus(_A)
class _EqlDcbxConfigETSRecommendationTxEnable_Type(TruthValue):defaultValue=2
_EqlDcbxConfigETSRecommendationTxEnable_Type.__name__=_D
_EqlDcbxConfigETSRecommendationTxEnable_Object=MibTableColumn
eqlDcbxConfigETSRecommendationTxEnable=_EqlDcbxConfigETSRecommendationTxEnable_Object((1,3,6,1,4,1,12740,19,1,1,1,3),_EqlDcbxConfigETSRecommendationTxEnable_Type())
eqlDcbxConfigETSRecommendationTxEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:eqlDcbxConfigETSRecommendationTxEnable.setStatus(_A)
class _EqlDcbxConfigPFCTxEnable_Type(TruthValue):defaultValue=1
_EqlDcbxConfigPFCTxEnable_Type.__name__=_D
_EqlDcbxConfigPFCTxEnable_Object=MibTableColumn
eqlDcbxConfigPFCTxEnable=_EqlDcbxConfigPFCTxEnable_Object((1,3,6,1,4,1,12740,19,1,1,1,4),_EqlDcbxConfigPFCTxEnable_Type())
eqlDcbxConfigPFCTxEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:eqlDcbxConfigPFCTxEnable.setStatus(_A)
class _EqlDcbxConfigAppPriorityTxEnable_Type(TruthValue):defaultValue=1
_EqlDcbxConfigAppPriorityTxEnable_Type.__name__=_D
_EqlDcbxConfigAppPriorityTxEnable_Object=MibTableColumn
eqlDcbxConfigAppPriorityTxEnable=_EqlDcbxConfigAppPriorityTxEnable_Object((1,3,6,1,4,1,12740,19,1,1,1,5),_EqlDcbxConfigAppPriorityTxEnable_Type())
eqlDcbxConfigAppPriorityTxEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:eqlDcbxConfigAppPriorityTxEnable.setStatus(_A)
class _EqlDcbxConfigQcnTxEnable_Type(TruthValue):defaultValue=2
_EqlDcbxConfigQcnTxEnable_Type.__name__=_D
_EqlDcbxConfigQcnTxEnable_Object=MibTableColumn
eqlDcbxConfigQcnTxEnable=_EqlDcbxConfigQcnTxEnable_Object((1,3,6,1,4,1,12740,19,1,1,1,6),_EqlDcbxConfigQcnTxEnable_Type())
eqlDcbxConfigQcnTxEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:eqlDcbxConfigQcnTxEnable.setStatus(_A)
_EqlDcbxAdminTCSupported_Type=EqlDcbxSupportedCapacity
_EqlDcbxAdminTCSupported_Object=MibTableColumn
eqlDcbxAdminTCSupported=_EqlDcbxAdminTCSupported_Object((1,3,6,1,4,1,12740,19,1,1,1,7),_EqlDcbxAdminTCSupported_Type())
eqlDcbxAdminTCSupported.setMaxAccess(_C)
if mibBuilder.loadTexts:eqlDcbxAdminTCSupported.setStatus(_G)
class _EqlDcbxAdminETSConMaxTCG_Type(EqlDcbxSupportedCapacity):defaultValue=0
_EqlDcbxAdminETSConMaxTCG_Type.__name__=_T
_EqlDcbxAdminETSConMaxTCG_Object=MibTableColumn
eqlDcbxAdminETSConMaxTCG=_EqlDcbxAdminETSConMaxTCG_Object((1,3,6,1,4,1,12740,19,1,1,1,8),_EqlDcbxAdminETSConMaxTCG_Type())
eqlDcbxAdminETSConMaxTCG.setMaxAccess(_C)
if mibBuilder.loadTexts:eqlDcbxAdminETSConMaxTCG.setStatus(_A)
class _EqlDcbxAdminETSConWilling_Type(TruthValue):defaultValue=1
_EqlDcbxAdminETSConWilling_Type.__name__=_D
_EqlDcbxAdminETSConWilling_Object=MibTableColumn
eqlDcbxAdminETSConWilling=_EqlDcbxAdminETSConWilling_Object((1,3,6,1,4,1,12740,19,1,1,1,9),_EqlDcbxAdminETSConWilling_Type())
eqlDcbxAdminETSConWilling.setMaxAccess(_C)
if mibBuilder.loadTexts:eqlDcbxAdminETSConWilling.setStatus(_A)
class _EqlDcbxAdminETSConTrafficClassGroupBandwidthTable_Type(OctetString):defaultHexValue=_X;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_EqlDcbxAdminETSConTrafficClassGroupBandwidthTable_Type.__name__=_I
_EqlDcbxAdminETSConTrafficClassGroupBandwidthTable_Object=MibTableColumn
eqlDcbxAdminETSConTrafficClassGroupBandwidthTable=_EqlDcbxAdminETSConTrafficClassGroupBandwidthTable_Object((1,3,6,1,4,1,12740,19,1,1,1,10),_EqlDcbxAdminETSConTrafficClassGroupBandwidthTable_Type())
eqlDcbxAdminETSConTrafficClassGroupBandwidthTable.setMaxAccess(_C)
if mibBuilder.loadTexts:eqlDcbxAdminETSConTrafficClassGroupBandwidthTable.setStatus(_A)
class _EqlDcbxAdminETSRecoTrafficClassGroupBandwidthTable_Type(OctetString):defaultHexValue=_X;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_EqlDcbxAdminETSRecoTrafficClassGroupBandwidthTable_Type.__name__=_I
_EqlDcbxAdminETSRecoTrafficClassGroupBandwidthTable_Object=MibTableColumn
eqlDcbxAdminETSRecoTrafficClassGroupBandwidthTable=_EqlDcbxAdminETSRecoTrafficClassGroupBandwidthTable_Object((1,3,6,1,4,1,12740,19,1,1,1,11),_EqlDcbxAdminETSRecoTrafficClassGroupBandwidthTable_Type())
eqlDcbxAdminETSRecoTrafficClassGroupBandwidthTable.setMaxAccess(_C)
if mibBuilder.loadTexts:eqlDcbxAdminETSRecoTrafficClassGroupBandwidthTable.setStatus(_A)
class _EqlDcbxAdminPFCWilling_Type(TruthValue):defaultValue=1
_EqlDcbxAdminPFCWilling_Type.__name__=_D
_EqlDcbxAdminPFCWilling_Object=MibTableColumn
eqlDcbxAdminPFCWilling=_EqlDcbxAdminPFCWilling_Object((1,3,6,1,4,1,12740,19,1,1,1,12),_EqlDcbxAdminPFCWilling_Type())
eqlDcbxAdminPFCWilling.setMaxAccess(_C)
if mibBuilder.loadTexts:eqlDcbxAdminPFCWilling.setStatus(_A)
class _EqlDcbxAdminPFCMBC_Type(TruthValue):defaultValue=2
_EqlDcbxAdminPFCMBC_Type.__name__=_D
_EqlDcbxAdminPFCMBC_Object=MibTableColumn
eqlDcbxAdminPFCMBC=_EqlDcbxAdminPFCMBC_Object((1,3,6,1,4,1,12740,19,1,1,1,13),_EqlDcbxAdminPFCMBC_Type())
eqlDcbxAdminPFCMBC.setMaxAccess(_C)
if mibBuilder.loadTexts:eqlDcbxAdminPFCMBC.setStatus(_A)
class _EqlDcbxAdminPFCCap_Type(EqlDcbxSupportedCapacity):defaultValue=8
_EqlDcbxAdminPFCCap_Type.__name__=_T
_EqlDcbxAdminPFCCap_Object=MibTableColumn
eqlDcbxAdminPFCCap=_EqlDcbxAdminPFCCap_Object((1,3,6,1,4,1,12740,19,1,1,1,14),_EqlDcbxAdminPFCCap_Type())
eqlDcbxAdminPFCCap.setMaxAccess(_C)
if mibBuilder.loadTexts:eqlDcbxAdminPFCCap.setStatus(_A)
class _EqlDcbxAdminAppPriorityWilling_Type(TruthValue):defaultValue=1
_EqlDcbxAdminAppPriorityWilling_Type.__name__=_D
_EqlDcbxAdminAppPriorityWilling_Object=MibTableColumn
eqlDcbxAdminAppPriorityWilling=_EqlDcbxAdminAppPriorityWilling_Object((1,3,6,1,4,1,12740,19,1,1,1,15),_EqlDcbxAdminAppPriorityWilling_Type())
eqlDcbxAdminAppPriorityWilling.setMaxAccess(_C)
if mibBuilder.loadTexts:eqlDcbxAdminAppPriorityWilling.setStatus(_A)
class _EqlDcbxConfigAutoDetectVLANEnable_Type(TruthValue):defaultValue=2
_EqlDcbxConfigAutoDetectVLANEnable_Type.__name__=_D
_EqlDcbxConfigAutoDetectVLANEnable_Object=MibTableColumn
eqlDcbxConfigAutoDetectVLANEnable=_EqlDcbxConfigAutoDetectVLANEnable_Object((1,3,6,1,4,1,12740,19,1,1,1,16),_EqlDcbxConfigAutoDetectVLANEnable_Type())
eqlDcbxConfigAutoDetectVLANEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:eqlDcbxConfigAutoDetectVLANEnable.setStatus(_A)
class _EqlDcbxConfigVLANId_Type(EqlVlanIdentifier):defaultValue=4095
_EqlDcbxConfigVLANId_Type.__name__=_Y
_EqlDcbxConfigVLANId_Object=MibTableColumn
eqlDcbxConfigVLANId=_EqlDcbxConfigVLANId_Object((1,3,6,1,4,1,12740,19,1,1,1,17),_EqlDcbxConfigVLANId_Type())
eqlDcbxConfigVLANId.setMaxAccess(_C)
if mibBuilder.loadTexts:eqlDcbxConfigVLANId.setStatus(_A)
class _EqlDcbxAdminETSConTrafficClassGroupPri0_Type(EqlDcbxTrafficClassGroupValue):defaultValue=0
_EqlDcbxAdminETSConTrafficClassGroupPri0_Type.__name__=_E
_EqlDcbxAdminETSConTrafficClassGroupPri0_Object=MibTableColumn
eqlDcbxAdminETSConTrafficClassGroupPri0=_EqlDcbxAdminETSConTrafficClassGroupPri0_Object((1,3,6,1,4,1,12740,19,1,1,1,18),_EqlDcbxAdminETSConTrafficClassGroupPri0_Type())
eqlDcbxAdminETSConTrafficClassGroupPri0.setMaxAccess(_C)
if mibBuilder.loadTexts:eqlDcbxAdminETSConTrafficClassGroupPri0.setStatus(_A)
class _EqlDcbxAdminETSConTrafficClassGroupPri1_Type(EqlDcbxTrafficClassGroupValue):defaultValue=0
_EqlDcbxAdminETSConTrafficClassGroupPri1_Type.__name__=_E
_EqlDcbxAdminETSConTrafficClassGroupPri1_Object=MibTableColumn
eqlDcbxAdminETSConTrafficClassGroupPri1=_EqlDcbxAdminETSConTrafficClassGroupPri1_Object((1,3,6,1,4,1,12740,19,1,1,1,19),_EqlDcbxAdminETSConTrafficClassGroupPri1_Type())
eqlDcbxAdminETSConTrafficClassGroupPri1.setMaxAccess(_C)
if mibBuilder.loadTexts:eqlDcbxAdminETSConTrafficClassGroupPri1.setStatus(_A)
class _EqlDcbxAdminETSConTrafficClassGroupPri2_Type(EqlDcbxTrafficClassGroupValue):defaultValue=0
_EqlDcbxAdminETSConTrafficClassGroupPri2_Type.__name__=_E
_EqlDcbxAdminETSConTrafficClassGroupPri2_Object=MibTableColumn
eqlDcbxAdminETSConTrafficClassGroupPri2=_EqlDcbxAdminETSConTrafficClassGroupPri2_Object((1,3,6,1,4,1,12740,19,1,1,1,20),_EqlDcbxAdminETSConTrafficClassGroupPri2_Type())
eqlDcbxAdminETSConTrafficClassGroupPri2.setMaxAccess(_C)
if mibBuilder.loadTexts:eqlDcbxAdminETSConTrafficClassGroupPri2.setStatus(_A)
class _EqlDcbxAdminETSConTrafficClassGroupPri3_Type(EqlDcbxTrafficClassGroupValue):defaultValue=0
_EqlDcbxAdminETSConTrafficClassGroupPri3_Type.__name__=_E
_EqlDcbxAdminETSConTrafficClassGroupPri3_Object=MibTableColumn
eqlDcbxAdminETSConTrafficClassGroupPri3=_EqlDcbxAdminETSConTrafficClassGroupPri3_Object((1,3,6,1,4,1,12740,19,1,1,1,21),_EqlDcbxAdminETSConTrafficClassGroupPri3_Type())
eqlDcbxAdminETSConTrafficClassGroupPri3.setMaxAccess(_C)
if mibBuilder.loadTexts:eqlDcbxAdminETSConTrafficClassGroupPri3.setStatus(_A)
class _EqlDcbxAdminETSConTrafficClassGroupPri4_Type(EqlDcbxTrafficClassGroupValue):defaultValue=0
_EqlDcbxAdminETSConTrafficClassGroupPri4_Type.__name__=_E
_EqlDcbxAdminETSConTrafficClassGroupPri4_Object=MibTableColumn
eqlDcbxAdminETSConTrafficClassGroupPri4=_EqlDcbxAdminETSConTrafficClassGroupPri4_Object((1,3,6,1,4,1,12740,19,1,1,1,22),_EqlDcbxAdminETSConTrafficClassGroupPri4_Type())
eqlDcbxAdminETSConTrafficClassGroupPri4.setMaxAccess(_C)
if mibBuilder.loadTexts:eqlDcbxAdminETSConTrafficClassGroupPri4.setStatus(_A)
class _EqlDcbxAdminETSConTrafficClassGroupPri5_Type(EqlDcbxTrafficClassGroupValue):defaultValue=0
_EqlDcbxAdminETSConTrafficClassGroupPri5_Type.__name__=_E
_EqlDcbxAdminETSConTrafficClassGroupPri5_Object=MibTableColumn
eqlDcbxAdminETSConTrafficClassGroupPri5=_EqlDcbxAdminETSConTrafficClassGroupPri5_Object((1,3,6,1,4,1,12740,19,1,1,1,23),_EqlDcbxAdminETSConTrafficClassGroupPri5_Type())
eqlDcbxAdminETSConTrafficClassGroupPri5.setMaxAccess(_C)
if mibBuilder.loadTexts:eqlDcbxAdminETSConTrafficClassGroupPri5.setStatus(_A)
class _EqlDcbxAdminETSConTrafficClassGroupPri6_Type(EqlDcbxTrafficClassGroupValue):defaultValue=0
_EqlDcbxAdminETSConTrafficClassGroupPri6_Type.__name__=_E
_EqlDcbxAdminETSConTrafficClassGroupPri6_Object=MibTableColumn
eqlDcbxAdminETSConTrafficClassGroupPri6=_EqlDcbxAdminETSConTrafficClassGroupPri6_Object((1,3,6,1,4,1,12740,19,1,1,1,24),_EqlDcbxAdminETSConTrafficClassGroupPri6_Type())
eqlDcbxAdminETSConTrafficClassGroupPri6.setMaxAccess(_C)
if mibBuilder.loadTexts:eqlDcbxAdminETSConTrafficClassGroupPri6.setStatus(_A)
class _EqlDcbxAdminETSConTrafficClassGroupPri7_Type(EqlDcbxTrafficClassGroupValue):defaultValue=0
_EqlDcbxAdminETSConTrafficClassGroupPri7_Type.__name__=_E
_EqlDcbxAdminETSConTrafficClassGroupPri7_Object=MibTableColumn
eqlDcbxAdminETSConTrafficClassGroupPri7=_EqlDcbxAdminETSConTrafficClassGroupPri7_Object((1,3,6,1,4,1,12740,19,1,1,1,25),_EqlDcbxAdminETSConTrafficClassGroupPri7_Type())
eqlDcbxAdminETSConTrafficClassGroupPri7.setMaxAccess(_C)
if mibBuilder.loadTexts:eqlDcbxAdminETSConTrafficClassGroupPri7.setStatus(_A)
class _EqlDcbxAdminPFCEnableEnabledPri0_Type(TruthValue):defaultValue=2
_EqlDcbxAdminPFCEnableEnabledPri0_Type.__name__=_D
_EqlDcbxAdminPFCEnableEnabledPri0_Object=MibTableColumn
eqlDcbxAdminPFCEnableEnabledPri0=_EqlDcbxAdminPFCEnableEnabledPri0_Object((1,3,6,1,4,1,12740,19,1,1,1,26),_EqlDcbxAdminPFCEnableEnabledPri0_Type())
eqlDcbxAdminPFCEnableEnabledPri0.setMaxAccess(_C)
if mibBuilder.loadTexts:eqlDcbxAdminPFCEnableEnabledPri0.setStatus(_A)
class _EqlDcbxAdminPFCEnableEnabledPri1_Type(TruthValue):defaultValue=2
_EqlDcbxAdminPFCEnableEnabledPri1_Type.__name__=_D
_EqlDcbxAdminPFCEnableEnabledPri1_Object=MibTableColumn
eqlDcbxAdminPFCEnableEnabledPri1=_EqlDcbxAdminPFCEnableEnabledPri1_Object((1,3,6,1,4,1,12740,19,1,1,1,27),_EqlDcbxAdminPFCEnableEnabledPri1_Type())
eqlDcbxAdminPFCEnableEnabledPri1.setMaxAccess(_C)
if mibBuilder.loadTexts:eqlDcbxAdminPFCEnableEnabledPri1.setStatus(_A)
class _EqlDcbxAdminPFCEnableEnabledPri2_Type(TruthValue):defaultValue=2
_EqlDcbxAdminPFCEnableEnabledPri2_Type.__name__=_D
_EqlDcbxAdminPFCEnableEnabledPri2_Object=MibTableColumn
eqlDcbxAdminPFCEnableEnabledPri2=_EqlDcbxAdminPFCEnableEnabledPri2_Object((1,3,6,1,4,1,12740,19,1,1,1,28),_EqlDcbxAdminPFCEnableEnabledPri2_Type())
eqlDcbxAdminPFCEnableEnabledPri2.setMaxAccess(_C)
if mibBuilder.loadTexts:eqlDcbxAdminPFCEnableEnabledPri2.setStatus(_A)
class _EqlDcbxAdminPFCEnableEnabledPri3_Type(TruthValue):defaultValue=1
_EqlDcbxAdminPFCEnableEnabledPri3_Type.__name__=_D
_EqlDcbxAdminPFCEnableEnabledPri3_Object=MibTableColumn
eqlDcbxAdminPFCEnableEnabledPri3=_EqlDcbxAdminPFCEnableEnabledPri3_Object((1,3,6,1,4,1,12740,19,1,1,1,29),_EqlDcbxAdminPFCEnableEnabledPri3_Type())
eqlDcbxAdminPFCEnableEnabledPri3.setMaxAccess(_C)
if mibBuilder.loadTexts:eqlDcbxAdminPFCEnableEnabledPri3.setStatus(_A)
class _EqlDcbxAdminPFCEnableEnabledPri4_Type(TruthValue):defaultValue=1
_EqlDcbxAdminPFCEnableEnabledPri4_Type.__name__=_D
_EqlDcbxAdminPFCEnableEnabledPri4_Object=MibTableColumn
eqlDcbxAdminPFCEnableEnabledPri4=_EqlDcbxAdminPFCEnableEnabledPri4_Object((1,3,6,1,4,1,12740,19,1,1,1,30),_EqlDcbxAdminPFCEnableEnabledPri4_Type())
eqlDcbxAdminPFCEnableEnabledPri4.setMaxAccess(_C)
if mibBuilder.loadTexts:eqlDcbxAdminPFCEnableEnabledPri4.setStatus(_A)
class _EqlDcbxAdminPFCEnableEnabledPri5_Type(TruthValue):defaultValue=2
_EqlDcbxAdminPFCEnableEnabledPri5_Type.__name__=_D
_EqlDcbxAdminPFCEnableEnabledPri5_Object=MibTableColumn
eqlDcbxAdminPFCEnableEnabledPri5=_EqlDcbxAdminPFCEnableEnabledPri5_Object((1,3,6,1,4,1,12740,19,1,1,1,31),_EqlDcbxAdminPFCEnableEnabledPri5_Type())
eqlDcbxAdminPFCEnableEnabledPri5.setMaxAccess(_C)
if mibBuilder.loadTexts:eqlDcbxAdminPFCEnableEnabledPri5.setStatus(_A)
class _EqlDcbxAdminPFCEnableEnabledPri6_Type(TruthValue):defaultValue=2
_EqlDcbxAdminPFCEnableEnabledPri6_Type.__name__=_D
_EqlDcbxAdminPFCEnableEnabledPri6_Object=MibTableColumn
eqlDcbxAdminPFCEnableEnabledPri6=_EqlDcbxAdminPFCEnableEnabledPri6_Object((1,3,6,1,4,1,12740,19,1,1,1,32),_EqlDcbxAdminPFCEnableEnabledPri6_Type())
eqlDcbxAdminPFCEnableEnabledPri6.setMaxAccess(_C)
if mibBuilder.loadTexts:eqlDcbxAdminPFCEnableEnabledPri6.setStatus(_A)
class _EqlDcbxAdminPFCEnableEnabledPri7_Type(TruthValue):defaultValue=2
_EqlDcbxAdminPFCEnableEnabledPri7_Type.__name__=_D
_EqlDcbxAdminPFCEnableEnabledPri7_Object=MibTableColumn
eqlDcbxAdminPFCEnableEnabledPri7=_EqlDcbxAdminPFCEnableEnabledPri7_Object((1,3,6,1,4,1,12740,19,1,1,1,33),_EqlDcbxAdminPFCEnableEnabledPri7_Type())
eqlDcbxAdminPFCEnableEnabledPri7.setMaxAccess(_C)
if mibBuilder.loadTexts:eqlDcbxAdminPFCEnableEnabledPri7.setStatus(_A)
class _EqlDcbxAdminAppPriorityiSCSITxEnable_Type(TruthValue):defaultValue=1
_EqlDcbxAdminAppPriorityiSCSITxEnable_Type.__name__=_D
_EqlDcbxAdminAppPriorityiSCSITxEnable_Object=MibTableColumn
eqlDcbxAdminAppPriorityiSCSITxEnable=_EqlDcbxAdminAppPriorityiSCSITxEnable_Object((1,3,6,1,4,1,12740,19,1,1,1,34),_EqlDcbxAdminAppPriorityiSCSITxEnable_Type())
eqlDcbxAdminAppPriorityiSCSITxEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:eqlDcbxAdminAppPriorityiSCSITxEnable.setStatus(_A)
class _EqlDcbxAdminAppPriorityiSCSIProtocol_Type(EqlDcbxAppProtocol):defaultValue=3260
_EqlDcbxAdminAppPriorityiSCSIProtocol_Type.__name__=_U
_EqlDcbxAdminAppPriorityiSCSIProtocol_Object=MibTableColumn
eqlDcbxAdminAppPriorityiSCSIProtocol=_EqlDcbxAdminAppPriorityiSCSIProtocol_Object((1,3,6,1,4,1,12740,19,1,1,1,35),_EqlDcbxAdminAppPriorityiSCSIProtocol_Type())
eqlDcbxAdminAppPriorityiSCSIProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:eqlDcbxAdminAppPriorityiSCSIProtocol.setStatus(_A)
class _EqlDcbxAdminAppPriorityiSCSIPriority_Type(EqlIEEE8021PriorityValue):defaultValue=4
_EqlDcbxAdminAppPriorityiSCSIPriority_Type.__name__=_K
_EqlDcbxAdminAppPriorityiSCSIPriority_Object=MibTableColumn
eqlDcbxAdminAppPriorityiSCSIPriority=_EqlDcbxAdminAppPriorityiSCSIPriority_Object((1,3,6,1,4,1,12740,19,1,1,1,36),_EqlDcbxAdminAppPriorityiSCSIPriority_Type())
eqlDcbxAdminAppPriorityiSCSIPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:eqlDcbxAdminAppPriorityiSCSIPriority.setStatus(_A)
class _EqlDcbxAdminAppPriorityFCoETxEnable_Type(TruthValue):defaultValue=1
_EqlDcbxAdminAppPriorityFCoETxEnable_Type.__name__=_D
_EqlDcbxAdminAppPriorityFCoETxEnable_Object=MibTableColumn
eqlDcbxAdminAppPriorityFCoETxEnable=_EqlDcbxAdminAppPriorityFCoETxEnable_Object((1,3,6,1,4,1,12740,19,1,1,1,37),_EqlDcbxAdminAppPriorityFCoETxEnable_Type())
eqlDcbxAdminAppPriorityFCoETxEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:eqlDcbxAdminAppPriorityFCoETxEnable.setStatus(_A)
class _EqlDcbxAdminAppPriorityFCoEProtocol_Type(EqlDcbxAppProtocol):defaultValue=35078
_EqlDcbxAdminAppPriorityFCoEProtocol_Type.__name__=_U
_EqlDcbxAdminAppPriorityFCoEProtocol_Object=MibTableColumn
eqlDcbxAdminAppPriorityFCoEProtocol=_EqlDcbxAdminAppPriorityFCoEProtocol_Object((1,3,6,1,4,1,12740,19,1,1,1,38),_EqlDcbxAdminAppPriorityFCoEProtocol_Type())
eqlDcbxAdminAppPriorityFCoEProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:eqlDcbxAdminAppPriorityFCoEProtocol.setStatus(_A)
class _EqlDcbxAdminAppPriorityFCoEPriority_Type(EqlIEEE8021PriorityValue):defaultValue=3
_EqlDcbxAdminAppPriorityFCoEPriority_Type.__name__=_K
_EqlDcbxAdminAppPriorityFCoEPriority_Object=MibTableColumn
eqlDcbxAdminAppPriorityFCoEPriority=_EqlDcbxAdminAppPriorityFCoEPriority_Object((1,3,6,1,4,1,12740,19,1,1,1,39),_EqlDcbxAdminAppPriorityFCoEPriority_Type())
eqlDcbxAdminAppPriorityFCoEPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:eqlDcbxAdminAppPriorityFCoEPriority.setStatus(_A)
class _EqlDcbxConfigDCBEnable_Type(TruthValue):defaultValue=1
_EqlDcbxConfigDCBEnable_Type.__name__=_D
_EqlDcbxConfigDCBEnable_Object=MibTableColumn
eqlDcbxConfigDCBEnable=_EqlDcbxConfigDCBEnable_Object((1,3,6,1,4,1,12740,19,1,1,1,40),_EqlDcbxConfigDCBEnable_Type())
eqlDcbxConfigDCBEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:eqlDcbxConfigDCBEnable.setStatus(_A)
class _EqlDcbxConfigDCBX101Enable_Type(TruthValue):defaultValue=1
_EqlDcbxConfigDCBX101Enable_Type.__name__=_D
_EqlDcbxConfigDCBX101Enable_Object=MibTableColumn
eqlDcbxConfigDCBX101Enable=_EqlDcbxConfigDCBX101Enable_Object((1,3,6,1,4,1,12740,19,1,1,1,41),_EqlDcbxConfigDCBX101Enable_Type())
eqlDcbxConfigDCBX101Enable.setMaxAccess(_C)
if mibBuilder.loadTexts:eqlDcbxConfigDCBX101Enable.setStatus(_A)
class _EqlDcbxConfigDCBXIEEEDraftEnable_Type(TruthValue):defaultValue=1
_EqlDcbxConfigDCBXIEEEDraftEnable_Type.__name__=_D
_EqlDcbxConfigDCBXIEEEDraftEnable_Object=MibTableColumn
eqlDcbxConfigDCBXIEEEDraftEnable=_EqlDcbxConfigDCBXIEEEDraftEnable_Object((1,3,6,1,4,1,12740,19,1,1,1,42),_EqlDcbxConfigDCBXIEEEDraftEnable_Type())
eqlDcbxConfigDCBXIEEEDraftEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:eqlDcbxConfigDCBXIEEEDraftEnable.setStatus(_A)
class _EqlDcbxConfigQcnSubtype_Type(EqlIEEEDraftSubtypeValue):defaultValue=8
_EqlDcbxConfigQcnSubtype_Type.__name__=_J
_EqlDcbxConfigQcnSubtype_Object=MibTableColumn
eqlDcbxConfigQcnSubtype=_EqlDcbxConfigQcnSubtype_Object((1,3,6,1,4,1,12740,19,1,1,1,43),_EqlDcbxConfigQcnSubtype_Type())
eqlDcbxConfigQcnSubtype.setMaxAccess(_C)
if mibBuilder.loadTexts:eqlDcbxConfigQcnSubtype.setStatus(_G)
class _EqlDcbxConfigETSConSubtype_Type(EqlIEEEDraftSubtypeValue):defaultValue=9
_EqlDcbxConfigETSConSubtype_Type.__name__=_J
_EqlDcbxConfigETSConSubtype_Object=MibTableColumn
eqlDcbxConfigETSConSubtype=_EqlDcbxConfigETSConSubtype_Object((1,3,6,1,4,1,12740,19,1,1,1,44),_EqlDcbxConfigETSConSubtype_Type())
eqlDcbxConfigETSConSubtype.setMaxAccess(_C)
if mibBuilder.loadTexts:eqlDcbxConfigETSConSubtype.setStatus(_G)
class _EqlDcbxConfigETSRecoSubtype_Type(EqlIEEEDraftSubtypeValue):defaultValue=10
_EqlDcbxConfigETSRecoSubtype_Type.__name__=_J
_EqlDcbxConfigETSRecoSubtype_Object=MibTableColumn
eqlDcbxConfigETSRecoSubtype=_EqlDcbxConfigETSRecoSubtype_Object((1,3,6,1,4,1,12740,19,1,1,1,45),_EqlDcbxConfigETSRecoSubtype_Type())
eqlDcbxConfigETSRecoSubtype.setMaxAccess(_C)
if mibBuilder.loadTexts:eqlDcbxConfigETSRecoSubtype.setStatus(_G)
class _EqlDcbxConfigPFCSubtype_Type(EqlIEEEDraftSubtypeValue):defaultValue=11
_EqlDcbxConfigPFCSubtype_Type.__name__=_J
_EqlDcbxConfigPFCSubtype_Object=MibTableColumn
eqlDcbxConfigPFCSubtype=_EqlDcbxConfigPFCSubtype_Object((1,3,6,1,4,1,12740,19,1,1,1,46),_EqlDcbxConfigPFCSubtype_Type())
eqlDcbxConfigPFCSubtype.setMaxAccess(_C)
if mibBuilder.loadTexts:eqlDcbxConfigPFCSubtype.setStatus(_G)
class _EqlDcbxConfigAppPrioritySubtype_Type(EqlIEEEDraftSubtypeValue):defaultValue=12
_EqlDcbxConfigAppPrioritySubtype_Type.__name__=_J
_EqlDcbxConfigAppPrioritySubtype_Object=MibTableColumn
eqlDcbxConfigAppPrioritySubtype=_EqlDcbxConfigAppPrioritySubtype_Object((1,3,6,1,4,1,12740,19,1,1,1,47),_EqlDcbxConfigAppPrioritySubtype_Type())
eqlDcbxConfigAppPrioritySubtype.setMaxAccess(_C)
if mibBuilder.loadTexts:eqlDcbxConfigAppPrioritySubtype.setStatus(_G)
_EqlDcbxConfigTCSupportedSubtype_Type=EqlIEEEDraftSubtypeValue
_EqlDcbxConfigTCSupportedSubtype_Object=MibTableColumn
eqlDcbxConfigTCSupportedSubtype=_EqlDcbxConfigTCSupportedSubtype_Object((1,3,6,1,4,1,12740,19,1,1,1,48),_EqlDcbxConfigTCSupportedSubtype_Type())
eqlDcbxConfigTCSupportedSubtype.setMaxAccess(_C)
if mibBuilder.loadTexts:eqlDcbxConfigTCSupportedSubtype.setStatus(_G)
class _EqlDcbxAdminETSRecoTrafficClassGroupPri0_Type(EqlDcbxTrafficClassGroupValue):defaultValue=0
_EqlDcbxAdminETSRecoTrafficClassGroupPri0_Type.__name__=_E
_EqlDcbxAdminETSRecoTrafficClassGroupPri0_Object=MibTableColumn
eqlDcbxAdminETSRecoTrafficClassGroupPri0=_EqlDcbxAdminETSRecoTrafficClassGroupPri0_Object((1,3,6,1,4,1,12740,19,1,1,1,49),_EqlDcbxAdminETSRecoTrafficClassGroupPri0_Type())
eqlDcbxAdminETSRecoTrafficClassGroupPri0.setMaxAccess(_C)
if mibBuilder.loadTexts:eqlDcbxAdminETSRecoTrafficClassGroupPri0.setStatus(_A)
class _EqlDcbxAdminETSRecoTrafficClassGroupPri1_Type(EqlDcbxTrafficClassGroupValue):defaultValue=0
_EqlDcbxAdminETSRecoTrafficClassGroupPri1_Type.__name__=_E
_EqlDcbxAdminETSRecoTrafficClassGroupPri1_Object=MibTableColumn
eqlDcbxAdminETSRecoTrafficClassGroupPri1=_EqlDcbxAdminETSRecoTrafficClassGroupPri1_Object((1,3,6,1,4,1,12740,19,1,1,1,50),_EqlDcbxAdminETSRecoTrafficClassGroupPri1_Type())
eqlDcbxAdminETSRecoTrafficClassGroupPri1.setMaxAccess(_C)
if mibBuilder.loadTexts:eqlDcbxAdminETSRecoTrafficClassGroupPri1.setStatus(_A)
class _EqlDcbxAdminETSRecoTrafficClassGroupPri2_Type(EqlDcbxTrafficClassGroupValue):defaultValue=0
_EqlDcbxAdminETSRecoTrafficClassGroupPri2_Type.__name__=_E
_EqlDcbxAdminETSRecoTrafficClassGroupPri2_Object=MibTableColumn
eqlDcbxAdminETSRecoTrafficClassGroupPri2=_EqlDcbxAdminETSRecoTrafficClassGroupPri2_Object((1,3,6,1,4,1,12740,19,1,1,1,51),_EqlDcbxAdminETSRecoTrafficClassGroupPri2_Type())
eqlDcbxAdminETSRecoTrafficClassGroupPri2.setMaxAccess(_C)
if mibBuilder.loadTexts:eqlDcbxAdminETSRecoTrafficClassGroupPri2.setStatus(_A)
class _EqlDcbxAdminETSRecoTrafficClassGroupPri3_Type(EqlDcbxTrafficClassGroupValue):defaultValue=0
_EqlDcbxAdminETSRecoTrafficClassGroupPri3_Type.__name__=_E
_EqlDcbxAdminETSRecoTrafficClassGroupPri3_Object=MibTableColumn
eqlDcbxAdminETSRecoTrafficClassGroupPri3=_EqlDcbxAdminETSRecoTrafficClassGroupPri3_Object((1,3,6,1,4,1,12740,19,1,1,1,52),_EqlDcbxAdminETSRecoTrafficClassGroupPri3_Type())
eqlDcbxAdminETSRecoTrafficClassGroupPri3.setMaxAccess(_C)
if mibBuilder.loadTexts:eqlDcbxAdminETSRecoTrafficClassGroupPri3.setStatus(_A)
class _EqlDcbxAdminETSRecoTrafficClassGroupPri4_Type(EqlDcbxTrafficClassGroupValue):defaultValue=0
_EqlDcbxAdminETSRecoTrafficClassGroupPri4_Type.__name__=_E
_EqlDcbxAdminETSRecoTrafficClassGroupPri4_Object=MibTableColumn
eqlDcbxAdminETSRecoTrafficClassGroupPri4=_EqlDcbxAdminETSRecoTrafficClassGroupPri4_Object((1,3,6,1,4,1,12740,19,1,1,1,53),_EqlDcbxAdminETSRecoTrafficClassGroupPri4_Type())
eqlDcbxAdminETSRecoTrafficClassGroupPri4.setMaxAccess(_C)
if mibBuilder.loadTexts:eqlDcbxAdminETSRecoTrafficClassGroupPri4.setStatus(_A)
class _EqlDcbxAdminETSRecoTrafficClassGroupPri5_Type(EqlDcbxTrafficClassGroupValue):defaultValue=0
_EqlDcbxAdminETSRecoTrafficClassGroupPri5_Type.__name__=_E
_EqlDcbxAdminETSRecoTrafficClassGroupPri5_Object=MibTableColumn
eqlDcbxAdminETSRecoTrafficClassGroupPri5=_EqlDcbxAdminETSRecoTrafficClassGroupPri5_Object((1,3,6,1,4,1,12740,19,1,1,1,54),_EqlDcbxAdminETSRecoTrafficClassGroupPri5_Type())
eqlDcbxAdminETSRecoTrafficClassGroupPri5.setMaxAccess(_C)
if mibBuilder.loadTexts:eqlDcbxAdminETSRecoTrafficClassGroupPri5.setStatus(_A)
class _EqlDcbxAdminETSRecoTrafficClassGroupPri6_Type(EqlDcbxTrafficClassGroupValue):defaultValue=0
_EqlDcbxAdminETSRecoTrafficClassGroupPri6_Type.__name__=_E
_EqlDcbxAdminETSRecoTrafficClassGroupPri6_Object=MibTableColumn
eqlDcbxAdminETSRecoTrafficClassGroupPri6=_EqlDcbxAdminETSRecoTrafficClassGroupPri6_Object((1,3,6,1,4,1,12740,19,1,1,1,55),_EqlDcbxAdminETSRecoTrafficClassGroupPri6_Type())
eqlDcbxAdminETSRecoTrafficClassGroupPri6.setMaxAccess(_C)
if mibBuilder.loadTexts:eqlDcbxAdminETSRecoTrafficClassGroupPri6.setStatus(_A)
class _EqlDcbxAdminETSRecoTrafficClassGroupPri7_Type(EqlDcbxTrafficClassGroupValue):defaultValue=0
_EqlDcbxAdminETSRecoTrafficClassGroupPri7_Type.__name__=_E
_EqlDcbxAdminETSRecoTrafficClassGroupPri7_Object=MibTableColumn
eqlDcbxAdminETSRecoTrafficClassGroupPri7=_EqlDcbxAdminETSRecoTrafficClassGroupPri7_Object((1,3,6,1,4,1,12740,19,1,1,1,56),_EqlDcbxAdminETSRecoTrafficClassGroupPri7_Type())
eqlDcbxAdminETSRecoTrafficClassGroupPri7.setMaxAccess(_C)
if mibBuilder.loadTexts:eqlDcbxAdminETSRecoTrafficClassGroupPri7.setStatus(_A)
class _EqlDcbCnGlobalMasterEnable_Type(TruthValue):defaultValue=2
_EqlDcbCnGlobalMasterEnable_Type.__name__=_D
_EqlDcbCnGlobalMasterEnable_Object=MibTableColumn
eqlDcbCnGlobalMasterEnable=_EqlDcbCnGlobalMasterEnable_Object((1,3,6,1,4,1,12740,19,1,1,1,57),_EqlDcbCnGlobalMasterEnable_Type())
eqlDcbCnGlobalMasterEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:eqlDcbCnGlobalMasterEnable.setStatus(_A)
class _EqlDcbCnRpPortPriMaxRps_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_EqlDcbCnRpPortPriMaxRps_Type.__name__=_H
_EqlDcbCnRpPortPriMaxRps_Object=MibTableColumn
eqlDcbCnRpPortPriMaxRps=_EqlDcbCnRpPortPriMaxRps_Object((1,3,6,1,4,1,12740,19,1,1,1,58),_EqlDcbCnRpPortPriMaxRps_Type())
eqlDcbCnRpPortPriMaxRps.setMaxAccess(_C)
if mibBuilder.loadTexts:eqlDcbCnRpPortPriMaxRps.setStatus(_A)
class _EqlDcbCnRpgEnablePri0_Type(TruthValue):defaultValue=2
_EqlDcbCnRpgEnablePri0_Type.__name__=_D
_EqlDcbCnRpgEnablePri0_Object=MibTableColumn
eqlDcbCnRpgEnablePri0=_EqlDcbCnRpgEnablePri0_Object((1,3,6,1,4,1,12740,19,1,1,1,59),_EqlDcbCnRpgEnablePri0_Type())
eqlDcbCnRpgEnablePri0.setMaxAccess(_C)
if mibBuilder.loadTexts:eqlDcbCnRpgEnablePri0.setStatus(_A)
class _EqlDcbCnRpgEnablePri1_Type(TruthValue):defaultValue=2
_EqlDcbCnRpgEnablePri1_Type.__name__=_D
_EqlDcbCnRpgEnablePri1_Object=MibTableColumn
eqlDcbCnRpgEnablePri1=_EqlDcbCnRpgEnablePri1_Object((1,3,6,1,4,1,12740,19,1,1,1,60),_EqlDcbCnRpgEnablePri1_Type())
eqlDcbCnRpgEnablePri1.setMaxAccess(_C)
if mibBuilder.loadTexts:eqlDcbCnRpgEnablePri1.setStatus(_A)
class _EqlDcbCnRpgEnablePri2_Type(TruthValue):defaultValue=2
_EqlDcbCnRpgEnablePri2_Type.__name__=_D
_EqlDcbCnRpgEnablePri2_Object=MibTableColumn
eqlDcbCnRpgEnablePri2=_EqlDcbCnRpgEnablePri2_Object((1,3,6,1,4,1,12740,19,1,1,1,61),_EqlDcbCnRpgEnablePri2_Type())
eqlDcbCnRpgEnablePri2.setMaxAccess(_C)
if mibBuilder.loadTexts:eqlDcbCnRpgEnablePri2.setStatus(_A)
class _EqlDcbCnRpgEnablePri3_Type(TruthValue):defaultValue=2
_EqlDcbCnRpgEnablePri3_Type.__name__=_D
_EqlDcbCnRpgEnablePri3_Object=MibTableColumn
eqlDcbCnRpgEnablePri3=_EqlDcbCnRpgEnablePri3_Object((1,3,6,1,4,1,12740,19,1,1,1,62),_EqlDcbCnRpgEnablePri3_Type())
eqlDcbCnRpgEnablePri3.setMaxAccess(_C)
if mibBuilder.loadTexts:eqlDcbCnRpgEnablePri3.setStatus(_A)
class _EqlDcbCnRpgEnablePri4_Type(TruthValue):defaultValue=2
_EqlDcbCnRpgEnablePri4_Type.__name__=_D
_EqlDcbCnRpgEnablePri4_Object=MibTableColumn
eqlDcbCnRpgEnablePri4=_EqlDcbCnRpgEnablePri4_Object((1,3,6,1,4,1,12740,19,1,1,1,63),_EqlDcbCnRpgEnablePri4_Type())
eqlDcbCnRpgEnablePri4.setMaxAccess(_C)
if mibBuilder.loadTexts:eqlDcbCnRpgEnablePri4.setStatus(_A)
class _EqlDcbCnRpgEnablePri5_Type(TruthValue):defaultValue=2
_EqlDcbCnRpgEnablePri5_Type.__name__=_D
_EqlDcbCnRpgEnablePri5_Object=MibTableColumn
eqlDcbCnRpgEnablePri5=_EqlDcbCnRpgEnablePri5_Object((1,3,6,1,4,1,12740,19,1,1,1,64),_EqlDcbCnRpgEnablePri5_Type())
eqlDcbCnRpgEnablePri5.setMaxAccess(_C)
if mibBuilder.loadTexts:eqlDcbCnRpgEnablePri5.setStatus(_A)
class _EqlDcbCnRpgEnablePri6_Type(TruthValue):defaultValue=2
_EqlDcbCnRpgEnablePri6_Type.__name__=_D
_EqlDcbCnRpgEnablePri6_Object=MibTableColumn
eqlDcbCnRpgEnablePri6=_EqlDcbCnRpgEnablePri6_Object((1,3,6,1,4,1,12740,19,1,1,1,65),_EqlDcbCnRpgEnablePri6_Type())
eqlDcbCnRpgEnablePri6.setMaxAccess(_C)
if mibBuilder.loadTexts:eqlDcbCnRpgEnablePri6.setStatus(_A)
class _EqlDcbCnRpgEnablePri7_Type(TruthValue):defaultValue=2
_EqlDcbCnRpgEnablePri7_Type.__name__=_D
_EqlDcbCnRpgEnablePri7_Object=MibTableColumn
eqlDcbCnRpgEnablePri7=_EqlDcbCnRpgEnablePri7_Object((1,3,6,1,4,1,12740,19,1,1,1,66),_EqlDcbCnRpgEnablePri7_Type())
eqlDcbCnRpgEnablePri7.setMaxAccess(_C)
if mibBuilder.loadTexts:eqlDcbCnRpgEnablePri7.setStatus(_A)
class _EqlDcbCnRpgTimeReset_Type(TimeInterval):defaultValue=15
_EqlDcbCnRpgTimeReset_Type.__name__=_W
_EqlDcbCnRpgTimeReset_Object=MibTableColumn
eqlDcbCnRpgTimeReset=_EqlDcbCnRpgTimeReset_Object((1,3,6,1,4,1,12740,19,1,1,1,67),_EqlDcbCnRpgTimeReset_Type())
eqlDcbCnRpgTimeReset.setMaxAccess(_C)
if mibBuilder.loadTexts:eqlDcbCnRpgTimeReset.setStatus(_A)
if mibBuilder.loadTexts:eqlDcbCnRpgTimeReset.setUnits('milliseconds')
class _EqlDcbCnRpgByteReset_Type(Unsigned32):defaultValue=150000
_EqlDcbCnRpgByteReset_Type.__name__=_H
_EqlDcbCnRpgByteReset_Object=MibTableColumn
eqlDcbCnRpgByteReset=_EqlDcbCnRpgByteReset_Object((1,3,6,1,4,1,12740,19,1,1,1,68),_EqlDcbCnRpgByteReset_Type())
eqlDcbCnRpgByteReset.setMaxAccess(_C)
if mibBuilder.loadTexts:eqlDcbCnRpgByteReset.setStatus(_A)
if mibBuilder.loadTexts:eqlDcbCnRpgByteReset.setUnits('octets')
class _EqlDcbCnRpgThreshold_Type(Unsigned32):defaultValue=5
_EqlDcbCnRpgThreshold_Type.__name__=_H
_EqlDcbCnRpgThreshold_Object=MibTableColumn
eqlDcbCnRpgThreshold=_EqlDcbCnRpgThreshold_Object((1,3,6,1,4,1,12740,19,1,1,1,69),_EqlDcbCnRpgThreshold_Type())
eqlDcbCnRpgThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:eqlDcbCnRpgThreshold.setStatus(_A)
class _EqlDcbCnRpgMaxRate_Type(Unsigned32):defaultValue=10000
_EqlDcbCnRpgMaxRate_Type.__name__=_H
_EqlDcbCnRpgMaxRate_Object=MibTableColumn
eqlDcbCnRpgMaxRate=_EqlDcbCnRpgMaxRate_Object((1,3,6,1,4,1,12740,19,1,1,1,70),_EqlDcbCnRpgMaxRate_Type())
eqlDcbCnRpgMaxRate.setMaxAccess(_C)
if mibBuilder.loadTexts:eqlDcbCnRpgMaxRate.setStatus(_A)
if mibBuilder.loadTexts:eqlDcbCnRpgMaxRate.setUnits(_L)
class _EqlDcbCnRpgAiRate_Type(Unsigned32):defaultValue=5
_EqlDcbCnRpgAiRate_Type.__name__=_H
_EqlDcbCnRpgAiRate_Object=MibTableColumn
eqlDcbCnRpgAiRate=_EqlDcbCnRpgAiRate_Object((1,3,6,1,4,1,12740,19,1,1,1,71),_EqlDcbCnRpgAiRate_Type())
eqlDcbCnRpgAiRate.setMaxAccess(_C)
if mibBuilder.loadTexts:eqlDcbCnRpgAiRate.setStatus(_A)
if mibBuilder.loadTexts:eqlDcbCnRpgAiRate.setUnits(_L)
class _EqlDcbCnRpgHaiRate_Type(Unsigned32):defaultValue=50
_EqlDcbCnRpgHaiRate_Type.__name__=_H
_EqlDcbCnRpgHaiRate_Object=MibTableColumn
eqlDcbCnRpgHaiRate=_EqlDcbCnRpgHaiRate_Object((1,3,6,1,4,1,12740,19,1,1,1,72),_EqlDcbCnRpgHaiRate_Type())
eqlDcbCnRpgHaiRate.setMaxAccess(_C)
if mibBuilder.loadTexts:eqlDcbCnRpgHaiRate.setStatus(_A)
if mibBuilder.loadTexts:eqlDcbCnRpgHaiRate.setUnits(_L)
class _EqlDcbCnRpgGd_Type(Integer32):defaultValue=7
_EqlDcbCnRpgGd_Type.__name__=_V
_EqlDcbCnRpgGd_Object=MibTableColumn
eqlDcbCnRpgGd=_EqlDcbCnRpgGd_Object((1,3,6,1,4,1,12740,19,1,1,1,73),_EqlDcbCnRpgGd_Type())
eqlDcbCnRpgGd.setMaxAccess(_C)
if mibBuilder.loadTexts:eqlDcbCnRpgGd.setStatus(_A)
class _EqlDcbCnRpgMinDecFac_Type(Unsigned32):defaultValue=50;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_EqlDcbCnRpgMinDecFac_Type.__name__=_H
_EqlDcbCnRpgMinDecFac_Object=MibTableColumn
eqlDcbCnRpgMinDecFac=_EqlDcbCnRpgMinDecFac_Object((1,3,6,1,4,1,12740,19,1,1,1,74),_EqlDcbCnRpgMinDecFac_Type())
eqlDcbCnRpgMinDecFac.setMaxAccess(_C)
if mibBuilder.loadTexts:eqlDcbCnRpgMinDecFac.setStatus(_A)
if mibBuilder.loadTexts:eqlDcbCnRpgMinDecFac.setUnits('percent')
class _EqlDcbCnRpgMinRate_Type(Unsigned32):defaultValue=5
_EqlDcbCnRpgMinRate_Type.__name__=_H
_EqlDcbCnRpgMinRate_Object=MibTableColumn
eqlDcbCnRpgMinRate=_EqlDcbCnRpgMinRate_Object((1,3,6,1,4,1,12740,19,1,1,1,75),_EqlDcbCnRpgMinRate_Type())
eqlDcbCnRpgMinRate.setMaxAccess(_C)
if mibBuilder.loadTexts:eqlDcbCnRpgMinRate.setStatus(_A)
if mibBuilder.loadTexts:eqlDcbCnRpgMinRate.setUnits(_L)
class _EqlDcbDefaultiSCSIPriority_Type(EqlIEEE8021PriorityValue):defaultValue=0
_EqlDcbDefaultiSCSIPriority_Type.__name__=_K
_EqlDcbDefaultiSCSIPriority_Object=MibTableColumn
eqlDcbDefaultiSCSIPriority=_EqlDcbDefaultiSCSIPriority_Object((1,3,6,1,4,1,12740,19,1,1,1,76),_EqlDcbDefaultiSCSIPriority_Type())
eqlDcbDefaultiSCSIPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:eqlDcbDefaultiSCSIPriority.setStatus(_A)
class _EqlDcbDefaultFCoEPriority_Type(EqlIEEE8021PriorityValue):defaultValue=0
_EqlDcbDefaultFCoEPriority_Type.__name__=_K
_EqlDcbDefaultFCoEPriority_Object=MibTableColumn
eqlDcbDefaultFCoEPriority=_EqlDcbDefaultFCoEPriority_Object((1,3,6,1,4,1,12740,19,1,1,1,77),_EqlDcbDefaultFCoEPriority_Type())
eqlDcbDefaultFCoEPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:eqlDcbDefaultFCoEPriority.setStatus(_A)
class _EqlDcbxAdminETSConTsaTc0_Type(EqlDcbxTransmissionSelectionAlgorithm):defaultValue=255
_EqlDcbxAdminETSConTsaTc0_Type.__name__=_F
_EqlDcbxAdminETSConTsaTc0_Object=MibTableColumn
eqlDcbxAdminETSConTsaTc0=_EqlDcbxAdminETSConTsaTc0_Object((1,3,6,1,4,1,12740,19,1,1,1,78),_EqlDcbxAdminETSConTsaTc0_Type())
eqlDcbxAdminETSConTsaTc0.setMaxAccess(_C)
if mibBuilder.loadTexts:eqlDcbxAdminETSConTsaTc0.setStatus(_A)
class _EqlDcbxAdminETSConTsaTc1_Type(EqlDcbxTransmissionSelectionAlgorithm):defaultValue=255
_EqlDcbxAdminETSConTsaTc1_Type.__name__=_F
_EqlDcbxAdminETSConTsaTc1_Object=MibTableColumn
eqlDcbxAdminETSConTsaTc1=_EqlDcbxAdminETSConTsaTc1_Object((1,3,6,1,4,1,12740,19,1,1,1,79),_EqlDcbxAdminETSConTsaTc1_Type())
eqlDcbxAdminETSConTsaTc1.setMaxAccess(_C)
if mibBuilder.loadTexts:eqlDcbxAdminETSConTsaTc1.setStatus(_A)
class _EqlDcbxAdminETSConTsaTc2_Type(EqlDcbxTransmissionSelectionAlgorithm):defaultValue=255
_EqlDcbxAdminETSConTsaTc2_Type.__name__=_F
_EqlDcbxAdminETSConTsaTc2_Object=MibTableColumn
eqlDcbxAdminETSConTsaTc2=_EqlDcbxAdminETSConTsaTc2_Object((1,3,6,1,4,1,12740,19,1,1,1,80),_EqlDcbxAdminETSConTsaTc2_Type())
eqlDcbxAdminETSConTsaTc2.setMaxAccess(_C)
if mibBuilder.loadTexts:eqlDcbxAdminETSConTsaTc2.setStatus(_A)
class _EqlDcbxAdminETSConTsaTc3_Type(EqlDcbxTransmissionSelectionAlgorithm):defaultValue=255
_EqlDcbxAdminETSConTsaTc3_Type.__name__=_F
_EqlDcbxAdminETSConTsaTc3_Object=MibTableColumn
eqlDcbxAdminETSConTsaTc3=_EqlDcbxAdminETSConTsaTc3_Object((1,3,6,1,4,1,12740,19,1,1,1,81),_EqlDcbxAdminETSConTsaTc3_Type())
eqlDcbxAdminETSConTsaTc3.setMaxAccess(_C)
if mibBuilder.loadTexts:eqlDcbxAdminETSConTsaTc3.setStatus(_A)
class _EqlDcbxAdminETSConTsaTc4_Type(EqlDcbxTransmissionSelectionAlgorithm):defaultValue=255
_EqlDcbxAdminETSConTsaTc4_Type.__name__=_F
_EqlDcbxAdminETSConTsaTc4_Object=MibTableColumn
eqlDcbxAdminETSConTsaTc4=_EqlDcbxAdminETSConTsaTc4_Object((1,3,6,1,4,1,12740,19,1,1,1,82),_EqlDcbxAdminETSConTsaTc4_Type())
eqlDcbxAdminETSConTsaTc4.setMaxAccess(_C)
if mibBuilder.loadTexts:eqlDcbxAdminETSConTsaTc4.setStatus(_A)
class _EqlDcbxAdminETSConTsaTc5_Type(EqlDcbxTransmissionSelectionAlgorithm):defaultValue=255
_EqlDcbxAdminETSConTsaTc5_Type.__name__=_F
_EqlDcbxAdminETSConTsaTc5_Object=MibTableColumn
eqlDcbxAdminETSConTsaTc5=_EqlDcbxAdminETSConTsaTc5_Object((1,3,6,1,4,1,12740,19,1,1,1,83),_EqlDcbxAdminETSConTsaTc5_Type())
eqlDcbxAdminETSConTsaTc5.setMaxAccess(_C)
if mibBuilder.loadTexts:eqlDcbxAdminETSConTsaTc5.setStatus(_A)
class _EqlDcbxAdminETSConTsaTc6_Type(EqlDcbxTransmissionSelectionAlgorithm):defaultValue=255
_EqlDcbxAdminETSConTsaTc6_Type.__name__=_F
_EqlDcbxAdminETSConTsaTc6_Object=MibTableColumn
eqlDcbxAdminETSConTsaTc6=_EqlDcbxAdminETSConTsaTc6_Object((1,3,6,1,4,1,12740,19,1,1,1,84),_EqlDcbxAdminETSConTsaTc6_Type())
eqlDcbxAdminETSConTsaTc6.setMaxAccess(_C)
if mibBuilder.loadTexts:eqlDcbxAdminETSConTsaTc6.setStatus(_A)
class _EqlDcbxAdminETSConTsaTc7_Type(EqlDcbxTransmissionSelectionAlgorithm):defaultValue=255
_EqlDcbxAdminETSConTsaTc7_Type.__name__=_F
_EqlDcbxAdminETSConTsaTc7_Object=MibTableColumn
eqlDcbxAdminETSConTsaTc7=_EqlDcbxAdminETSConTsaTc7_Object((1,3,6,1,4,1,12740,19,1,1,1,85),_EqlDcbxAdminETSConTsaTc7_Type())
eqlDcbxAdminETSConTsaTc7.setMaxAccess(_C)
if mibBuilder.loadTexts:eqlDcbxAdminETSConTsaTc7.setStatus(_A)
class _EqlDcbxAdminETSRecoTsaTc0_Type(EqlDcbxTransmissionSelectionAlgorithm):defaultValue=255
_EqlDcbxAdminETSRecoTsaTc0_Type.__name__=_F
_EqlDcbxAdminETSRecoTsaTc0_Object=MibTableColumn
eqlDcbxAdminETSRecoTsaTc0=_EqlDcbxAdminETSRecoTsaTc0_Object((1,3,6,1,4,1,12740,19,1,1,1,86),_EqlDcbxAdminETSRecoTsaTc0_Type())
eqlDcbxAdminETSRecoTsaTc0.setMaxAccess(_C)
if mibBuilder.loadTexts:eqlDcbxAdminETSRecoTsaTc0.setStatus(_A)
class _EqlDcbxAdminETSRecoTsaTc1_Type(EqlDcbxTransmissionSelectionAlgorithm):defaultValue=255
_EqlDcbxAdminETSRecoTsaTc1_Type.__name__=_F
_EqlDcbxAdminETSRecoTsaTc1_Object=MibTableColumn
eqlDcbxAdminETSRecoTsaTc1=_EqlDcbxAdminETSRecoTsaTc1_Object((1,3,6,1,4,1,12740,19,1,1,1,87),_EqlDcbxAdminETSRecoTsaTc1_Type())
eqlDcbxAdminETSRecoTsaTc1.setMaxAccess(_C)
if mibBuilder.loadTexts:eqlDcbxAdminETSRecoTsaTc1.setStatus(_A)
class _EqlDcbxAdminETSRecoTsaTc2_Type(EqlDcbxTransmissionSelectionAlgorithm):defaultValue=255
_EqlDcbxAdminETSRecoTsaTc2_Type.__name__=_F
_EqlDcbxAdminETSRecoTsaTc2_Object=MibTableColumn
eqlDcbxAdminETSRecoTsaTc2=_EqlDcbxAdminETSRecoTsaTc2_Object((1,3,6,1,4,1,12740,19,1,1,1,88),_EqlDcbxAdminETSRecoTsaTc2_Type())
eqlDcbxAdminETSRecoTsaTc2.setMaxAccess(_C)
if mibBuilder.loadTexts:eqlDcbxAdminETSRecoTsaTc2.setStatus(_A)
class _EqlDcbxAdminETSRecoTsaTc3_Type(EqlDcbxTransmissionSelectionAlgorithm):defaultValue=255
_EqlDcbxAdminETSRecoTsaTc3_Type.__name__=_F
_EqlDcbxAdminETSRecoTsaTc3_Object=MibTableColumn
eqlDcbxAdminETSRecoTsaTc3=_EqlDcbxAdminETSRecoTsaTc3_Object((1,3,6,1,4,1,12740,19,1,1,1,89),_EqlDcbxAdminETSRecoTsaTc3_Type())
eqlDcbxAdminETSRecoTsaTc3.setMaxAccess(_C)
if mibBuilder.loadTexts:eqlDcbxAdminETSRecoTsaTc3.setStatus(_A)
class _EqlDcbxAdminETSRecoTsaTc4_Type(EqlDcbxTransmissionSelectionAlgorithm):defaultValue=255
_EqlDcbxAdminETSRecoTsaTc4_Type.__name__=_F
_EqlDcbxAdminETSRecoTsaTc4_Object=MibTableColumn
eqlDcbxAdminETSRecoTsaTc4=_EqlDcbxAdminETSRecoTsaTc4_Object((1,3,6,1,4,1,12740,19,1,1,1,90),_EqlDcbxAdminETSRecoTsaTc4_Type())
eqlDcbxAdminETSRecoTsaTc4.setMaxAccess(_C)
if mibBuilder.loadTexts:eqlDcbxAdminETSRecoTsaTc4.setStatus(_A)
class _EqlDcbxAdminETSRecoTsaTc5_Type(EqlDcbxTransmissionSelectionAlgorithm):defaultValue=255
_EqlDcbxAdminETSRecoTsaTc5_Type.__name__=_F
_EqlDcbxAdminETSRecoTsaTc5_Object=MibTableColumn
eqlDcbxAdminETSRecoTsaTc5=_EqlDcbxAdminETSRecoTsaTc5_Object((1,3,6,1,4,1,12740,19,1,1,1,91),_EqlDcbxAdminETSRecoTsaTc5_Type())
eqlDcbxAdminETSRecoTsaTc5.setMaxAccess(_C)
if mibBuilder.loadTexts:eqlDcbxAdminETSRecoTsaTc5.setStatus(_A)
class _EqlDcbxAdminETSRecoTsaTc6_Type(EqlDcbxTransmissionSelectionAlgorithm):defaultValue=255
_EqlDcbxAdminETSRecoTsaTc6_Type.__name__=_F
_EqlDcbxAdminETSRecoTsaTc6_Object=MibTableColumn
eqlDcbxAdminETSRecoTsaTc6=_EqlDcbxAdminETSRecoTsaTc6_Object((1,3,6,1,4,1,12740,19,1,1,1,92),_EqlDcbxAdminETSRecoTsaTc6_Type())
eqlDcbxAdminETSRecoTsaTc6.setMaxAccess(_C)
if mibBuilder.loadTexts:eqlDcbxAdminETSRecoTsaTc6.setStatus(_A)
class _EqlDcbxAdminETSRecoTsaTc7_Type(EqlDcbxTransmissionSelectionAlgorithm):defaultValue=255
_EqlDcbxAdminETSRecoTsaTc7_Type.__name__=_F
_EqlDcbxAdminETSRecoTsaTc7_Object=MibTableColumn
eqlDcbxAdminETSRecoTsaTc7=_EqlDcbxAdminETSRecoTsaTc7_Object((1,3,6,1,4,1,12740,19,1,1,1,93),_EqlDcbxAdminETSRecoTsaTc7_Type())
eqlDcbxAdminETSRecoTsaTc7.setMaxAccess(_C)
if mibBuilder.loadTexts:eqlDcbxAdminETSRecoTsaTc7.setStatus(_A)
_EqlDcbDynamicIfTable_Object=MibTable
eqlDcbDynamicIfTable=_EqlDcbDynamicIfTable_Object((1,3,6,1,4,1,12740,19,1,2))
if mibBuilder.loadTexts:eqlDcbDynamicIfTable.setStatus(_A)
_EqlDcbDynamicIfEntry_Object=MibTableRow
eqlDcbDynamicIfEntry=_EqlDcbDynamicIfEntry_Object((1,3,6,1,4,1,12740,19,1,2,1))
eqlDcbDynamicIfEntry.setIndexNames((0,_M,_N),(0,_O,_P),(0,_Q,_R))
if mibBuilder.loadTexts:eqlDcbDynamicIfEntry.setStatus(_A)
_EqlDcbPfcRequestsSent_Type=Counter32
_EqlDcbPfcRequestsSent_Object=MibTableColumn
eqlDcbPfcRequestsSent=_EqlDcbPfcRequestsSent_Object((1,3,6,1,4,1,12740,19,1,2,1,1),_EqlDcbPfcRequestsSent_Type())
eqlDcbPfcRequestsSent.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbPfcRequestsSent.setStatus(_A)
_EqlDcbPfcIndicationsReceived_Type=Counter32
_EqlDcbPfcIndicationsReceived_Object=MibTableColumn
eqlDcbPfcIndicationsReceived=_EqlDcbPfcIndicationsReceived_Object((1,3,6,1,4,1,12740,19,1,2,1,2),_EqlDcbPfcIndicationsReceived_Type())
eqlDcbPfcIndicationsReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbPfcIndicationsReceived.setStatus(_A)
_EqlDcbxLocTCSupported_Type=EqlDcbxSupportedCapacity
_EqlDcbxLocTCSupported_Object=MibTableColumn
eqlDcbxLocTCSupported=_EqlDcbxLocTCSupported_Object((1,3,6,1,4,1,12740,19,1,2,1,3),_EqlDcbxLocTCSupported_Type())
eqlDcbxLocTCSupported.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbxLocTCSupported.setStatus(_G)
_EqlDcbxLocETSConMaxTCG_Type=EqlDcbxSupportedCapacity
_EqlDcbxLocETSConMaxTCG_Object=MibTableColumn
eqlDcbxLocETSConMaxTCG=_EqlDcbxLocETSConMaxTCG_Object((1,3,6,1,4,1,12740,19,1,2,1,4),_EqlDcbxLocETSConMaxTCG_Type())
eqlDcbxLocETSConMaxTCG.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbxLocETSConMaxTCG.setStatus(_A)
_EqlDcbxLocETSConWilling_Type=TruthValue
_EqlDcbxLocETSConWilling_Object=MibTableColumn
eqlDcbxLocETSConWilling=_EqlDcbxLocETSConWilling_Object((1,3,6,1,4,1,12740,19,1,2,1,5),_EqlDcbxLocETSConWilling_Type())
eqlDcbxLocETSConWilling.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbxLocETSConWilling.setStatus(_A)
class _EqlDcbxLocETSConTrafficClassGroupBandwidthTable_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_EqlDcbxLocETSConTrafficClassGroupBandwidthTable_Type.__name__=_I
_EqlDcbxLocETSConTrafficClassGroupBandwidthTable_Object=MibTableColumn
eqlDcbxLocETSConTrafficClassGroupBandwidthTable=_EqlDcbxLocETSConTrafficClassGroupBandwidthTable_Object((1,3,6,1,4,1,12740,19,1,2,1,6),_EqlDcbxLocETSConTrafficClassGroupBandwidthTable_Type())
eqlDcbxLocETSConTrafficClassGroupBandwidthTable.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbxLocETSConTrafficClassGroupBandwidthTable.setStatus(_A)
class _EqlDcbxLocETSRecoTrafficClassGroupBandwidthTable_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_EqlDcbxLocETSRecoTrafficClassGroupBandwidthTable_Type.__name__=_I
_EqlDcbxLocETSRecoTrafficClassGroupBandwidthTable_Object=MibTableColumn
eqlDcbxLocETSRecoTrafficClassGroupBandwidthTable=_EqlDcbxLocETSRecoTrafficClassGroupBandwidthTable_Object((1,3,6,1,4,1,12740,19,1,2,1,7),_EqlDcbxLocETSRecoTrafficClassGroupBandwidthTable_Type())
eqlDcbxLocETSRecoTrafficClassGroupBandwidthTable.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbxLocETSRecoTrafficClassGroupBandwidthTable.setStatus(_A)
_EqlDcbxLocPFCWilling_Type=TruthValue
_EqlDcbxLocPFCWilling_Object=MibTableColumn
eqlDcbxLocPFCWilling=_EqlDcbxLocPFCWilling_Object((1,3,6,1,4,1,12740,19,1,2,1,8),_EqlDcbxLocPFCWilling_Type())
eqlDcbxLocPFCWilling.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbxLocPFCWilling.setStatus(_A)
_EqlDcbxLocPFCMBC_Type=TruthValue
_EqlDcbxLocPFCMBC_Object=MibTableColumn
eqlDcbxLocPFCMBC=_EqlDcbxLocPFCMBC_Object((1,3,6,1,4,1,12740,19,1,2,1,9),_EqlDcbxLocPFCMBC_Type())
eqlDcbxLocPFCMBC.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbxLocPFCMBC.setStatus(_A)
_EqlDcbxLocPFCCap_Type=EqlDcbxSupportedCapacity
_EqlDcbxLocPFCCap_Object=MibTableColumn
eqlDcbxLocPFCCap=_EqlDcbxLocPFCCap_Object((1,3,6,1,4,1,12740,19,1,2,1,10),_EqlDcbxLocPFCCap_Type())
eqlDcbxLocPFCCap.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbxLocPFCCap.setStatus(_A)
_EqlDcbxLocAppPriorityWilling_Type=TruthValue
_EqlDcbxLocAppPriorityWilling_Object=MibTableColumn
eqlDcbxLocAppPriorityWilling=_EqlDcbxLocAppPriorityWilling_Object((1,3,6,1,4,1,12740,19,1,2,1,11),_EqlDcbxLocAppPriorityWilling_Type())
eqlDcbxLocAppPriorityWilling.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbxLocAppPriorityWilling.setStatus(_A)
_EqlDcbxRemTCSupported_Type=EqlDcbxSupportedCapacity
_EqlDcbxRemTCSupported_Object=MibTableColumn
eqlDcbxRemTCSupported=_EqlDcbxRemTCSupported_Object((1,3,6,1,4,1,12740,19,1,2,1,12),_EqlDcbxRemTCSupported_Type())
eqlDcbxRemTCSupported.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbxRemTCSupported.setStatus(_G)
_EqlDcbxRemETSConMaxTCG_Type=EqlDcbxSupportedCapacity
_EqlDcbxRemETSConMaxTCG_Object=MibTableColumn
eqlDcbxRemETSConMaxTCG=_EqlDcbxRemETSConMaxTCG_Object((1,3,6,1,4,1,12740,19,1,2,1,13),_EqlDcbxRemETSConMaxTCG_Type())
eqlDcbxRemETSConMaxTCG.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbxRemETSConMaxTCG.setStatus(_A)
_EqlDcbxRemETSConWilling_Type=TruthValue
_EqlDcbxRemETSConWilling_Object=MibTableColumn
eqlDcbxRemETSConWilling=_EqlDcbxRemETSConWilling_Object((1,3,6,1,4,1,12740,19,1,2,1,14),_EqlDcbxRemETSConWilling_Type())
eqlDcbxRemETSConWilling.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbxRemETSConWilling.setStatus(_A)
class _EqlDcbxRemETSConTrafficClassGroupBandwidthTable_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_EqlDcbxRemETSConTrafficClassGroupBandwidthTable_Type.__name__=_I
_EqlDcbxRemETSConTrafficClassGroupBandwidthTable_Object=MibTableColumn
eqlDcbxRemETSConTrafficClassGroupBandwidthTable=_EqlDcbxRemETSConTrafficClassGroupBandwidthTable_Object((1,3,6,1,4,1,12740,19,1,2,1,15),_EqlDcbxRemETSConTrafficClassGroupBandwidthTable_Type())
eqlDcbxRemETSConTrafficClassGroupBandwidthTable.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbxRemETSConTrafficClassGroupBandwidthTable.setStatus(_A)
class _EqlDcbxRemETSRecoTrafficClassGroupBandwidthTable_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_EqlDcbxRemETSRecoTrafficClassGroupBandwidthTable_Type.__name__=_I
_EqlDcbxRemETSRecoTrafficClassGroupBandwidthTable_Object=MibTableColumn
eqlDcbxRemETSRecoTrafficClassGroupBandwidthTable=_EqlDcbxRemETSRecoTrafficClassGroupBandwidthTable_Object((1,3,6,1,4,1,12740,19,1,2,1,16),_EqlDcbxRemETSRecoTrafficClassGroupBandwidthTable_Type())
eqlDcbxRemETSRecoTrafficClassGroupBandwidthTable.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbxRemETSRecoTrafficClassGroupBandwidthTable.setStatus(_A)
_EqlDcbxRemPFCWilling_Type=TruthValue
_EqlDcbxRemPFCWilling_Object=MibTableColumn
eqlDcbxRemPFCWilling=_EqlDcbxRemPFCWilling_Object((1,3,6,1,4,1,12740,19,1,2,1,17),_EqlDcbxRemPFCWilling_Type())
eqlDcbxRemPFCWilling.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbxRemPFCWilling.setStatus(_A)
_EqlDcbxRemPFCMBC_Type=TruthValue
_EqlDcbxRemPFCMBC_Object=MibTableColumn
eqlDcbxRemPFCMBC=_EqlDcbxRemPFCMBC_Object((1,3,6,1,4,1,12740,19,1,2,1,18),_EqlDcbxRemPFCMBC_Type())
eqlDcbxRemPFCMBC.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbxRemPFCMBC.setStatus(_A)
_EqlDcbxRemPFCCap_Type=EqlDcbxSupportedCapacity
_EqlDcbxRemPFCCap_Object=MibTableColumn
eqlDcbxRemPFCCap=_EqlDcbxRemPFCCap_Object((1,3,6,1,4,1,12740,19,1,2,1,19),_EqlDcbxRemPFCCap_Type())
eqlDcbxRemPFCCap.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbxRemPFCCap.setStatus(_A)
_EqlDcbxRemAppPriorityWilling_Type=TruthValue
_EqlDcbxRemAppPriorityWilling_Object=MibTableColumn
eqlDcbxRemAppPriorityWilling=_EqlDcbxRemAppPriorityWilling_Object((1,3,6,1,4,1,12740,19,1,2,1,20),_EqlDcbxRemAppPriorityWilling_Type())
eqlDcbxRemAppPriorityWilling.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbxRemAppPriorityWilling.setStatus(_A)
_EqlDcbxLocETSConTrafficClassGroupPri0_Type=EqlDcbxTrafficClassGroupValue
_EqlDcbxLocETSConTrafficClassGroupPri0_Object=MibTableColumn
eqlDcbxLocETSConTrafficClassGroupPri0=_EqlDcbxLocETSConTrafficClassGroupPri0_Object((1,3,6,1,4,1,12740,19,1,2,1,21),_EqlDcbxLocETSConTrafficClassGroupPri0_Type())
eqlDcbxLocETSConTrafficClassGroupPri0.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbxLocETSConTrafficClassGroupPri0.setStatus(_A)
_EqlDcbxLocETSConTrafficClassGroupPri1_Type=EqlDcbxTrafficClassGroupValue
_EqlDcbxLocETSConTrafficClassGroupPri1_Object=MibTableColumn
eqlDcbxLocETSConTrafficClassGroupPri1=_EqlDcbxLocETSConTrafficClassGroupPri1_Object((1,3,6,1,4,1,12740,19,1,2,1,22),_EqlDcbxLocETSConTrafficClassGroupPri1_Type())
eqlDcbxLocETSConTrafficClassGroupPri1.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbxLocETSConTrafficClassGroupPri1.setStatus(_A)
_EqlDcbxLocETSConTrafficClassGroupPri2_Type=EqlDcbxTrafficClassGroupValue
_EqlDcbxLocETSConTrafficClassGroupPri2_Object=MibTableColumn
eqlDcbxLocETSConTrafficClassGroupPri2=_EqlDcbxLocETSConTrafficClassGroupPri2_Object((1,3,6,1,4,1,12740,19,1,2,1,23),_EqlDcbxLocETSConTrafficClassGroupPri2_Type())
eqlDcbxLocETSConTrafficClassGroupPri2.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbxLocETSConTrafficClassGroupPri2.setStatus(_A)
_EqlDcbxLocETSConTrafficClassGroupPri3_Type=EqlDcbxTrafficClassGroupValue
_EqlDcbxLocETSConTrafficClassGroupPri3_Object=MibTableColumn
eqlDcbxLocETSConTrafficClassGroupPri3=_EqlDcbxLocETSConTrafficClassGroupPri3_Object((1,3,6,1,4,1,12740,19,1,2,1,24),_EqlDcbxLocETSConTrafficClassGroupPri3_Type())
eqlDcbxLocETSConTrafficClassGroupPri3.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbxLocETSConTrafficClassGroupPri3.setStatus(_A)
_EqlDcbxLocETSConTrafficClassGroupPri4_Type=EqlDcbxTrafficClassGroupValue
_EqlDcbxLocETSConTrafficClassGroupPri4_Object=MibTableColumn
eqlDcbxLocETSConTrafficClassGroupPri4=_EqlDcbxLocETSConTrafficClassGroupPri4_Object((1,3,6,1,4,1,12740,19,1,2,1,25),_EqlDcbxLocETSConTrafficClassGroupPri4_Type())
eqlDcbxLocETSConTrafficClassGroupPri4.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbxLocETSConTrafficClassGroupPri4.setStatus(_A)
_EqlDcbxLocETSConTrafficClassGroupPri5_Type=EqlDcbxTrafficClassGroupValue
_EqlDcbxLocETSConTrafficClassGroupPri5_Object=MibTableColumn
eqlDcbxLocETSConTrafficClassGroupPri5=_EqlDcbxLocETSConTrafficClassGroupPri5_Object((1,3,6,1,4,1,12740,19,1,2,1,26),_EqlDcbxLocETSConTrafficClassGroupPri5_Type())
eqlDcbxLocETSConTrafficClassGroupPri5.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbxLocETSConTrafficClassGroupPri5.setStatus(_A)
_EqlDcbxLocETSConTrafficClassGroupPri6_Type=EqlDcbxTrafficClassGroupValue
_EqlDcbxLocETSConTrafficClassGroupPri6_Object=MibTableColumn
eqlDcbxLocETSConTrafficClassGroupPri6=_EqlDcbxLocETSConTrafficClassGroupPri6_Object((1,3,6,1,4,1,12740,19,1,2,1,27),_EqlDcbxLocETSConTrafficClassGroupPri6_Type())
eqlDcbxLocETSConTrafficClassGroupPri6.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbxLocETSConTrafficClassGroupPri6.setStatus(_A)
_EqlDcbxLocETSConTrafficClassGroupPri7_Type=EqlDcbxTrafficClassGroupValue
_EqlDcbxLocETSConTrafficClassGroupPri7_Object=MibTableColumn
eqlDcbxLocETSConTrafficClassGroupPri7=_EqlDcbxLocETSConTrafficClassGroupPri7_Object((1,3,6,1,4,1,12740,19,1,2,1,28),_EqlDcbxLocETSConTrafficClassGroupPri7_Type())
eqlDcbxLocETSConTrafficClassGroupPri7.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbxLocETSConTrafficClassGroupPri7.setStatus(_A)
_EqlDcbxLocPFCEnableEnabledPri0_Type=TruthValue
_EqlDcbxLocPFCEnableEnabledPri0_Object=MibTableColumn
eqlDcbxLocPFCEnableEnabledPri0=_EqlDcbxLocPFCEnableEnabledPri0_Object((1,3,6,1,4,1,12740,19,1,2,1,29),_EqlDcbxLocPFCEnableEnabledPri0_Type())
eqlDcbxLocPFCEnableEnabledPri0.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbxLocPFCEnableEnabledPri0.setStatus(_A)
_EqlDcbxLocPFCEnableEnabledPri1_Type=TruthValue
_EqlDcbxLocPFCEnableEnabledPri1_Object=MibTableColumn
eqlDcbxLocPFCEnableEnabledPri1=_EqlDcbxLocPFCEnableEnabledPri1_Object((1,3,6,1,4,1,12740,19,1,2,1,30),_EqlDcbxLocPFCEnableEnabledPri1_Type())
eqlDcbxLocPFCEnableEnabledPri1.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbxLocPFCEnableEnabledPri1.setStatus(_A)
_EqlDcbxLocPFCEnableEnabledPri2_Type=TruthValue
_EqlDcbxLocPFCEnableEnabledPri2_Object=MibTableColumn
eqlDcbxLocPFCEnableEnabledPri2=_EqlDcbxLocPFCEnableEnabledPri2_Object((1,3,6,1,4,1,12740,19,1,2,1,31),_EqlDcbxLocPFCEnableEnabledPri2_Type())
eqlDcbxLocPFCEnableEnabledPri2.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbxLocPFCEnableEnabledPri2.setStatus(_A)
_EqlDcbxLocPFCEnableEnabledPri3_Type=TruthValue
_EqlDcbxLocPFCEnableEnabledPri3_Object=MibTableColumn
eqlDcbxLocPFCEnableEnabledPri3=_EqlDcbxLocPFCEnableEnabledPri3_Object((1,3,6,1,4,1,12740,19,1,2,1,32),_EqlDcbxLocPFCEnableEnabledPri3_Type())
eqlDcbxLocPFCEnableEnabledPri3.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbxLocPFCEnableEnabledPri3.setStatus(_A)
_EqlDcbxLocPFCEnableEnabledPri4_Type=TruthValue
_EqlDcbxLocPFCEnableEnabledPri4_Object=MibTableColumn
eqlDcbxLocPFCEnableEnabledPri4=_EqlDcbxLocPFCEnableEnabledPri4_Object((1,3,6,1,4,1,12740,19,1,2,1,33),_EqlDcbxLocPFCEnableEnabledPri4_Type())
eqlDcbxLocPFCEnableEnabledPri4.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbxLocPFCEnableEnabledPri4.setStatus(_A)
_EqlDcbxLocPFCEnableEnabledPri5_Type=TruthValue
_EqlDcbxLocPFCEnableEnabledPri5_Object=MibTableColumn
eqlDcbxLocPFCEnableEnabledPri5=_EqlDcbxLocPFCEnableEnabledPri5_Object((1,3,6,1,4,1,12740,19,1,2,1,34),_EqlDcbxLocPFCEnableEnabledPri5_Type())
eqlDcbxLocPFCEnableEnabledPri5.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbxLocPFCEnableEnabledPri5.setStatus(_A)
_EqlDcbxLocPFCEnableEnabledPri6_Type=TruthValue
_EqlDcbxLocPFCEnableEnabledPri6_Object=MibTableColumn
eqlDcbxLocPFCEnableEnabledPri6=_EqlDcbxLocPFCEnableEnabledPri6_Object((1,3,6,1,4,1,12740,19,1,2,1,35),_EqlDcbxLocPFCEnableEnabledPri6_Type())
eqlDcbxLocPFCEnableEnabledPri6.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbxLocPFCEnableEnabledPri6.setStatus(_A)
_EqlDcbxLocPFCEnableEnabledPri7_Type=TruthValue
_EqlDcbxLocPFCEnableEnabledPri7_Object=MibTableColumn
eqlDcbxLocPFCEnableEnabledPri7=_EqlDcbxLocPFCEnableEnabledPri7_Object((1,3,6,1,4,1,12740,19,1,2,1,36),_EqlDcbxLocPFCEnableEnabledPri7_Type())
eqlDcbxLocPFCEnableEnabledPri7.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbxLocPFCEnableEnabledPri7.setStatus(_A)
_EqlDcbxLocVLANId_Type=EqlVlanIdentifier
_EqlDcbxLocVLANId_Object=MibTableColumn
eqlDcbxLocVLANId=_EqlDcbxLocVLANId_Object((1,3,6,1,4,1,12740,19,1,2,1,37),_EqlDcbxLocVLANId_Type())
eqlDcbxLocVLANId.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbxLocVLANId.setStatus(_A)
_EqlDcbxLocVLANState_Type=EqlDcbxVlanState
_EqlDcbxLocVLANState_Object=MibTableColumn
eqlDcbxLocVLANState=_EqlDcbxLocVLANState_Object((1,3,6,1,4,1,12740,19,1,2,1,38),_EqlDcbxLocVLANState_Type())
eqlDcbxLocVLANState.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbxLocVLANState.setStatus(_A)
_EqlDcbxLocDCBState_Type=EqlDcbxState
_EqlDcbxLocDCBState_Object=MibTableColumn
eqlDcbxLocDCBState=_EqlDcbxLocDCBState_Object((1,3,6,1,4,1,12740,19,1,2,1,39),_EqlDcbxLocDCBState_Type())
eqlDcbxLocDCBState.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbxLocDCBState.setStatus(_A)
_EqlDcbxLocPFCState_Type=EqlDcbxState
_EqlDcbxLocPFCState_Object=MibTableColumn
eqlDcbxLocPFCState=_EqlDcbxLocPFCState_Object((1,3,6,1,4,1,12740,19,1,2,1,40),_EqlDcbxLocPFCState_Type())
eqlDcbxLocPFCState.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbxLocPFCState.setStatus(_A)
_EqlDcbxLocETSState_Type=EqlDcbxState
_EqlDcbxLocETSState_Object=MibTableColumn
eqlDcbxLocETSState=_EqlDcbxLocETSState_Object((1,3,6,1,4,1,12740,19,1,2,1,41),_EqlDcbxLocETSState_Type())
eqlDcbxLocETSState.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbxLocETSState.setStatus(_A)
_EqlDcbxLocQCNState_Type=EqlDcbxState
_EqlDcbxLocQCNState_Object=MibTableColumn
eqlDcbxLocQCNState=_EqlDcbxLocQCNState_Object((1,3,6,1,4,1,12740,19,1,2,1,42),_EqlDcbxLocQCNState_Type())
eqlDcbxLocQCNState.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbxLocQCNState.setStatus(_A)
_EqlDcbxLociSCSIPriority_Type=EqlIEEE8021PriorityValue
_EqlDcbxLociSCSIPriority_Object=MibTableColumn
eqlDcbxLociSCSIPriority=_EqlDcbxLociSCSIPriority_Object((1,3,6,1,4,1,12740,19,1,2,1,43),_EqlDcbxLociSCSIPriority_Type())
eqlDcbxLociSCSIPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbxLociSCSIPriority.setStatus(_A)
_EqlDcbxLocFCoEPriority_Type=EqlIEEE8021PriorityValue
_EqlDcbxLocFCoEPriority_Object=MibTableColumn
eqlDcbxLocFCoEPriority=_EqlDcbxLocFCoEPriority_Object((1,3,6,1,4,1,12740,19,1,2,1,44),_EqlDcbxLocFCoEPriority_Type())
eqlDcbxLocFCoEPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbxLocFCoEPriority.setStatus(_A)
_EqlDcbxLocBytesRxPri0_Type=Counter64
_EqlDcbxLocBytesRxPri0_Object=MibTableColumn
eqlDcbxLocBytesRxPri0=_EqlDcbxLocBytesRxPri0_Object((1,3,6,1,4,1,12740,19,1,2,1,45),_EqlDcbxLocBytesRxPri0_Type())
eqlDcbxLocBytesRxPri0.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbxLocBytesRxPri0.setStatus(_A)
_EqlDcbxLocBytesRxPri1_Type=Counter64
_EqlDcbxLocBytesRxPri1_Object=MibTableColumn
eqlDcbxLocBytesRxPri1=_EqlDcbxLocBytesRxPri1_Object((1,3,6,1,4,1,12740,19,1,2,1,46),_EqlDcbxLocBytesRxPri1_Type())
eqlDcbxLocBytesRxPri1.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbxLocBytesRxPri1.setStatus(_A)
_EqlDcbxLocBytesRxPri2_Type=Counter64
_EqlDcbxLocBytesRxPri2_Object=MibTableColumn
eqlDcbxLocBytesRxPri2=_EqlDcbxLocBytesRxPri2_Object((1,3,6,1,4,1,12740,19,1,2,1,47),_EqlDcbxLocBytesRxPri2_Type())
eqlDcbxLocBytesRxPri2.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbxLocBytesRxPri2.setStatus(_A)
_EqlDcbxLocBytesRxPri3_Type=Counter64
_EqlDcbxLocBytesRxPri3_Object=MibTableColumn
eqlDcbxLocBytesRxPri3=_EqlDcbxLocBytesRxPri3_Object((1,3,6,1,4,1,12740,19,1,2,1,48),_EqlDcbxLocBytesRxPri3_Type())
eqlDcbxLocBytesRxPri3.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbxLocBytesRxPri3.setStatus(_A)
_EqlDcbxLocBytesRxPri4_Type=Counter64
_EqlDcbxLocBytesRxPri4_Object=MibTableColumn
eqlDcbxLocBytesRxPri4=_EqlDcbxLocBytesRxPri4_Object((1,3,6,1,4,1,12740,19,1,2,1,49),_EqlDcbxLocBytesRxPri4_Type())
eqlDcbxLocBytesRxPri4.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbxLocBytesRxPri4.setStatus(_A)
_EqlDcbxLocBytesRxPri5_Type=Counter64
_EqlDcbxLocBytesRxPri5_Object=MibTableColumn
eqlDcbxLocBytesRxPri5=_EqlDcbxLocBytesRxPri5_Object((1,3,6,1,4,1,12740,19,1,2,1,50),_EqlDcbxLocBytesRxPri5_Type())
eqlDcbxLocBytesRxPri5.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbxLocBytesRxPri5.setStatus(_A)
_EqlDcbxLocBytesRxPri6_Type=Counter64
_EqlDcbxLocBytesRxPri6_Object=MibTableColumn
eqlDcbxLocBytesRxPri6=_EqlDcbxLocBytesRxPri6_Object((1,3,6,1,4,1,12740,19,1,2,1,51),_EqlDcbxLocBytesRxPri6_Type())
eqlDcbxLocBytesRxPri6.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbxLocBytesRxPri6.setStatus(_A)
_EqlDcbxLocBytesRxPri7_Type=Counter64
_EqlDcbxLocBytesRxPri7_Object=MibTableColumn
eqlDcbxLocBytesRxPri7=_EqlDcbxLocBytesRxPri7_Object((1,3,6,1,4,1,12740,19,1,2,1,52),_EqlDcbxLocBytesRxPri7_Type())
eqlDcbxLocBytesRxPri7.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbxLocBytesRxPri7.setStatus(_A)
_EqlDcbxLocBytesTxPri0_Type=Counter64
_EqlDcbxLocBytesTxPri0_Object=MibTableColumn
eqlDcbxLocBytesTxPri0=_EqlDcbxLocBytesTxPri0_Object((1,3,6,1,4,1,12740,19,1,2,1,53),_EqlDcbxLocBytesTxPri0_Type())
eqlDcbxLocBytesTxPri0.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbxLocBytesTxPri0.setStatus(_A)
_EqlDcbxLocBytesTxPri1_Type=Counter64
_EqlDcbxLocBytesTxPri1_Object=MibTableColumn
eqlDcbxLocBytesTxPri1=_EqlDcbxLocBytesTxPri1_Object((1,3,6,1,4,1,12740,19,1,2,1,54),_EqlDcbxLocBytesTxPri1_Type())
eqlDcbxLocBytesTxPri1.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbxLocBytesTxPri1.setStatus(_A)
_EqlDcbxLocBytesTxPri2_Type=Counter64
_EqlDcbxLocBytesTxPri2_Object=MibTableColumn
eqlDcbxLocBytesTxPri2=_EqlDcbxLocBytesTxPri2_Object((1,3,6,1,4,1,12740,19,1,2,1,55),_EqlDcbxLocBytesTxPri2_Type())
eqlDcbxLocBytesTxPri2.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbxLocBytesTxPri2.setStatus(_A)
_EqlDcbxLocBytesTxPri3_Type=Counter64
_EqlDcbxLocBytesTxPri3_Object=MibTableColumn
eqlDcbxLocBytesTxPri3=_EqlDcbxLocBytesTxPri3_Object((1,3,6,1,4,1,12740,19,1,2,1,56),_EqlDcbxLocBytesTxPri3_Type())
eqlDcbxLocBytesTxPri3.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbxLocBytesTxPri3.setStatus(_A)
_EqlDcbxLocBytesTxPri4_Type=Counter64
_EqlDcbxLocBytesTxPri4_Object=MibTableColumn
eqlDcbxLocBytesTxPri4=_EqlDcbxLocBytesTxPri4_Object((1,3,6,1,4,1,12740,19,1,2,1,57),_EqlDcbxLocBytesTxPri4_Type())
eqlDcbxLocBytesTxPri4.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbxLocBytesTxPri4.setStatus(_A)
_EqlDcbxLocBytesTxPri5_Type=Counter64
_EqlDcbxLocBytesTxPri5_Object=MibTableColumn
eqlDcbxLocBytesTxPri5=_EqlDcbxLocBytesTxPri5_Object((1,3,6,1,4,1,12740,19,1,2,1,58),_EqlDcbxLocBytesTxPri5_Type())
eqlDcbxLocBytesTxPri5.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbxLocBytesTxPri5.setStatus(_A)
_EqlDcbxLocBytesTxPri6_Type=Counter64
_EqlDcbxLocBytesTxPri6_Object=MibTableColumn
eqlDcbxLocBytesTxPri6=_EqlDcbxLocBytesTxPri6_Object((1,3,6,1,4,1,12740,19,1,2,1,59),_EqlDcbxLocBytesTxPri6_Type())
eqlDcbxLocBytesTxPri6.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbxLocBytesTxPri6.setStatus(_A)
_EqlDcbxLocBytesTxPri7_Type=Counter64
_EqlDcbxLocBytesTxPri7_Object=MibTableColumn
eqlDcbxLocBytesTxPri7=_EqlDcbxLocBytesTxPri7_Object((1,3,6,1,4,1,12740,19,1,2,1,60),_EqlDcbxLocBytesTxPri7_Type())
eqlDcbxLocBytesTxPri7.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbxLocBytesTxPri7.setStatus(_A)
_EqlDcbCnRpPortPriCreatedRpsPri0_Type=Counter64
_EqlDcbCnRpPortPriCreatedRpsPri0_Object=MibTableColumn
eqlDcbCnRpPortPriCreatedRpsPri0=_EqlDcbCnRpPortPriCreatedRpsPri0_Object((1,3,6,1,4,1,12740,19,1,2,1,61),_EqlDcbCnRpPortPriCreatedRpsPri0_Type())
eqlDcbCnRpPortPriCreatedRpsPri0.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbCnRpPortPriCreatedRpsPri0.setStatus(_A)
_EqlDcbCnRpPortPriCreatedRpsPri1_Type=Counter64
_EqlDcbCnRpPortPriCreatedRpsPri1_Object=MibTableColumn
eqlDcbCnRpPortPriCreatedRpsPri1=_EqlDcbCnRpPortPriCreatedRpsPri1_Object((1,3,6,1,4,1,12740,19,1,2,1,62),_EqlDcbCnRpPortPriCreatedRpsPri1_Type())
eqlDcbCnRpPortPriCreatedRpsPri1.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbCnRpPortPriCreatedRpsPri1.setStatus(_A)
_EqlDcbCnRpPortPriCreatedRpsPri2_Type=Counter64
_EqlDcbCnRpPortPriCreatedRpsPri2_Object=MibTableColumn
eqlDcbCnRpPortPriCreatedRpsPri2=_EqlDcbCnRpPortPriCreatedRpsPri2_Object((1,3,6,1,4,1,12740,19,1,2,1,63),_EqlDcbCnRpPortPriCreatedRpsPri2_Type())
eqlDcbCnRpPortPriCreatedRpsPri2.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbCnRpPortPriCreatedRpsPri2.setStatus(_A)
_EqlDcbCnRpPortPriCreatedRpsPri3_Type=Counter64
_EqlDcbCnRpPortPriCreatedRpsPri3_Object=MibTableColumn
eqlDcbCnRpPortPriCreatedRpsPri3=_EqlDcbCnRpPortPriCreatedRpsPri3_Object((1,3,6,1,4,1,12740,19,1,2,1,64),_EqlDcbCnRpPortPriCreatedRpsPri3_Type())
eqlDcbCnRpPortPriCreatedRpsPri3.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbCnRpPortPriCreatedRpsPri3.setStatus(_A)
_EqlDcbCnRpPortPriCreatedRpsPri4_Type=Counter64
_EqlDcbCnRpPortPriCreatedRpsPri4_Object=MibTableColumn
eqlDcbCnRpPortPriCreatedRpsPri4=_EqlDcbCnRpPortPriCreatedRpsPri4_Object((1,3,6,1,4,1,12740,19,1,2,1,65),_EqlDcbCnRpPortPriCreatedRpsPri4_Type())
eqlDcbCnRpPortPriCreatedRpsPri4.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbCnRpPortPriCreatedRpsPri4.setStatus(_A)
_EqlDcbCnRpPortPriCreatedRpsPri5_Type=Counter64
_EqlDcbCnRpPortPriCreatedRpsPri5_Object=MibTableColumn
eqlDcbCnRpPortPriCreatedRpsPri5=_EqlDcbCnRpPortPriCreatedRpsPri5_Object((1,3,6,1,4,1,12740,19,1,2,1,66),_EqlDcbCnRpPortPriCreatedRpsPri5_Type())
eqlDcbCnRpPortPriCreatedRpsPri5.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbCnRpPortPriCreatedRpsPri5.setStatus(_A)
_EqlDcbCnRpPortPriCreatedRpsPri6_Type=Counter64
_EqlDcbCnRpPortPriCreatedRpsPri6_Object=MibTableColumn
eqlDcbCnRpPortPriCreatedRpsPri6=_EqlDcbCnRpPortPriCreatedRpsPri6_Object((1,3,6,1,4,1,12740,19,1,2,1,67),_EqlDcbCnRpPortPriCreatedRpsPri6_Type())
eqlDcbCnRpPortPriCreatedRpsPri6.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbCnRpPortPriCreatedRpsPri6.setStatus(_A)
_EqlDcbCnRpPortPriCreatedRpsPri7_Type=Counter64
_EqlDcbCnRpPortPriCreatedRpsPri7_Object=MibTableColumn
eqlDcbCnRpPortPriCreatedRpsPri7=_EqlDcbCnRpPortPriCreatedRpsPri7_Object((1,3,6,1,4,1,12740,19,1,2,1,68),_EqlDcbCnRpPortPriCreatedRpsPri7_Type())
eqlDcbCnRpPortPriCreatedRpsPri7.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbCnRpPortPriCreatedRpsPri7.setStatus(_A)
_EqlDcbCnRpPortPriCentisecondsPri0_Type=Counter64
_EqlDcbCnRpPortPriCentisecondsPri0_Object=MibTableColumn
eqlDcbCnRpPortPriCentisecondsPri0=_EqlDcbCnRpPortPriCentisecondsPri0_Object((1,3,6,1,4,1,12740,19,1,2,1,69),_EqlDcbCnRpPortPriCentisecondsPri0_Type())
eqlDcbCnRpPortPriCentisecondsPri0.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbCnRpPortPriCentisecondsPri0.setStatus(_A)
_EqlDcbCnRpPortPriCentisecondsPri1_Type=Counter64
_EqlDcbCnRpPortPriCentisecondsPri1_Object=MibTableColumn
eqlDcbCnRpPortPriCentisecondsPri1=_EqlDcbCnRpPortPriCentisecondsPri1_Object((1,3,6,1,4,1,12740,19,1,2,1,70),_EqlDcbCnRpPortPriCentisecondsPri1_Type())
eqlDcbCnRpPortPriCentisecondsPri1.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbCnRpPortPriCentisecondsPri1.setStatus(_A)
_EqlDcbCnRpPortPriCentisecondsPri2_Type=Counter64
_EqlDcbCnRpPortPriCentisecondsPri2_Object=MibTableColumn
eqlDcbCnRpPortPriCentisecondsPri2=_EqlDcbCnRpPortPriCentisecondsPri2_Object((1,3,6,1,4,1,12740,19,1,2,1,71),_EqlDcbCnRpPortPriCentisecondsPri2_Type())
eqlDcbCnRpPortPriCentisecondsPri2.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbCnRpPortPriCentisecondsPri2.setStatus(_A)
_EqlDcbCnRpPortPriCentisecondsPri3_Type=Counter64
_EqlDcbCnRpPortPriCentisecondsPri3_Object=MibTableColumn
eqlDcbCnRpPortPriCentisecondsPri3=_EqlDcbCnRpPortPriCentisecondsPri3_Object((1,3,6,1,4,1,12740,19,1,2,1,72),_EqlDcbCnRpPortPriCentisecondsPri3_Type())
eqlDcbCnRpPortPriCentisecondsPri3.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbCnRpPortPriCentisecondsPri3.setStatus(_A)
_EqlDcbCnRpPortPriCentisecondsPri4_Type=Counter64
_EqlDcbCnRpPortPriCentisecondsPri4_Object=MibTableColumn
eqlDcbCnRpPortPriCentisecondsPri4=_EqlDcbCnRpPortPriCentisecondsPri4_Object((1,3,6,1,4,1,12740,19,1,2,1,73),_EqlDcbCnRpPortPriCentisecondsPri4_Type())
eqlDcbCnRpPortPriCentisecondsPri4.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbCnRpPortPriCentisecondsPri4.setStatus(_A)
_EqlDcbCnRpPortPriCentisecondsPri5_Type=Counter64
_EqlDcbCnRpPortPriCentisecondsPri5_Object=MibTableColumn
eqlDcbCnRpPortPriCentisecondsPri5=_EqlDcbCnRpPortPriCentisecondsPri5_Object((1,3,6,1,4,1,12740,19,1,2,1,74),_EqlDcbCnRpPortPriCentisecondsPri5_Type())
eqlDcbCnRpPortPriCentisecondsPri5.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbCnRpPortPriCentisecondsPri5.setStatus(_A)
_EqlDcbCnRpPortPriCentisecondsPri6_Type=Counter64
_EqlDcbCnRpPortPriCentisecondsPri6_Object=MibTableColumn
eqlDcbCnRpPortPriCentisecondsPri6=_EqlDcbCnRpPortPriCentisecondsPri6_Object((1,3,6,1,4,1,12740,19,1,2,1,75),_EqlDcbCnRpPortPriCentisecondsPri6_Type())
eqlDcbCnRpPortPriCentisecondsPri6.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbCnRpPortPriCentisecondsPri6.setStatus(_A)
_EqlDcbCnRpPortPriCentisecondsPri7_Type=Counter64
_EqlDcbCnRpPortPriCentisecondsPri7_Object=MibTableColumn
eqlDcbCnRpPortPriCentisecondsPri7=_EqlDcbCnRpPortPriCentisecondsPri7_Object((1,3,6,1,4,1,12740,19,1,2,1,76),_EqlDcbCnRpPortPriCentisecondsPri7_Type())
eqlDcbCnRpPortPriCentisecondsPri7.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbCnRpPortPriCentisecondsPri7.setStatus(_A)
_EqlDcbxLocPfcPausePri0_Type=Counter64
_EqlDcbxLocPfcPausePri0_Object=MibTableColumn
eqlDcbxLocPfcPausePri0=_EqlDcbxLocPfcPausePri0_Object((1,3,6,1,4,1,12740,19,1,2,1,77),_EqlDcbxLocPfcPausePri0_Type())
eqlDcbxLocPfcPausePri0.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbxLocPfcPausePri0.setStatus(_A)
_EqlDcbxLocPfcPausePri1_Type=Counter64
_EqlDcbxLocPfcPausePri1_Object=MibTableColumn
eqlDcbxLocPfcPausePri1=_EqlDcbxLocPfcPausePri1_Object((1,3,6,1,4,1,12740,19,1,2,1,78),_EqlDcbxLocPfcPausePri1_Type())
eqlDcbxLocPfcPausePri1.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbxLocPfcPausePri1.setStatus(_A)
_EqlDcbxLocPfcPausePri2_Type=Counter64
_EqlDcbxLocPfcPausePri2_Object=MibTableColumn
eqlDcbxLocPfcPausePri2=_EqlDcbxLocPfcPausePri2_Object((1,3,6,1,4,1,12740,19,1,2,1,79),_EqlDcbxLocPfcPausePri2_Type())
eqlDcbxLocPfcPausePri2.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbxLocPfcPausePri2.setStatus(_A)
_EqlDcbxLocPfcPausePri3_Type=Counter64
_EqlDcbxLocPfcPausePri3_Object=MibTableColumn
eqlDcbxLocPfcPausePri3=_EqlDcbxLocPfcPausePri3_Object((1,3,6,1,4,1,12740,19,1,2,1,80),_EqlDcbxLocPfcPausePri3_Type())
eqlDcbxLocPfcPausePri3.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbxLocPfcPausePri3.setStatus(_A)
_EqlDcbxLocPfcPausePri4_Type=Counter64
_EqlDcbxLocPfcPausePri4_Object=MibTableColumn
eqlDcbxLocPfcPausePri4=_EqlDcbxLocPfcPausePri4_Object((1,3,6,1,4,1,12740,19,1,2,1,81),_EqlDcbxLocPfcPausePri4_Type())
eqlDcbxLocPfcPausePri4.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbxLocPfcPausePri4.setStatus(_A)
_EqlDcbxLocPfcPausePri5_Type=Counter64
_EqlDcbxLocPfcPausePri5_Object=MibTableColumn
eqlDcbxLocPfcPausePri5=_EqlDcbxLocPfcPausePri5_Object((1,3,6,1,4,1,12740,19,1,2,1,82),_EqlDcbxLocPfcPausePri5_Type())
eqlDcbxLocPfcPausePri5.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbxLocPfcPausePri5.setStatus(_A)
_EqlDcbxLocPfcPausePri6_Type=Counter64
_EqlDcbxLocPfcPausePri6_Object=MibTableColumn
eqlDcbxLocPfcPausePri6=_EqlDcbxLocPfcPausePri6_Object((1,3,6,1,4,1,12740,19,1,2,1,83),_EqlDcbxLocPfcPausePri6_Type())
eqlDcbxLocPfcPausePri6.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbxLocPfcPausePri6.setStatus(_A)
_EqlDcbxLocPfcPausePri7_Type=Counter64
_EqlDcbxLocPfcPausePri7_Object=MibTableColumn
eqlDcbxLocPfcPausePri7=_EqlDcbxLocPfcPausePri7_Object((1,3,6,1,4,1,12740,19,1,2,1,84),_EqlDcbxLocPfcPausePri7_Type())
eqlDcbxLocPfcPausePri7.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbxLocPfcPausePri7.setStatus(_A)
_EqlDcbxLocPfcUnpausePri0_Type=Counter64
_EqlDcbxLocPfcUnpausePri0_Object=MibTableColumn
eqlDcbxLocPfcUnpausePri0=_EqlDcbxLocPfcUnpausePri0_Object((1,3,6,1,4,1,12740,19,1,2,1,85),_EqlDcbxLocPfcUnpausePri0_Type())
eqlDcbxLocPfcUnpausePri0.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbxLocPfcUnpausePri0.setStatus(_A)
_EqlDcbxLocPfcUnpausePri1_Type=Counter64
_EqlDcbxLocPfcUnpausePri1_Object=MibTableColumn
eqlDcbxLocPfcUnpausePri1=_EqlDcbxLocPfcUnpausePri1_Object((1,3,6,1,4,1,12740,19,1,2,1,86),_EqlDcbxLocPfcUnpausePri1_Type())
eqlDcbxLocPfcUnpausePri1.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbxLocPfcUnpausePri1.setStatus(_A)
_EqlDcbxLocPfcUnpausePri2_Type=Counter64
_EqlDcbxLocPfcUnpausePri2_Object=MibTableColumn
eqlDcbxLocPfcUnpausePri2=_EqlDcbxLocPfcUnpausePri2_Object((1,3,6,1,4,1,12740,19,1,2,1,87),_EqlDcbxLocPfcUnpausePri2_Type())
eqlDcbxLocPfcUnpausePri2.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbxLocPfcUnpausePri2.setStatus(_A)
_EqlDcbxLocPfcUnpausePri3_Type=Counter64
_EqlDcbxLocPfcUnpausePri3_Object=MibTableColumn
eqlDcbxLocPfcUnpausePri3=_EqlDcbxLocPfcUnpausePri3_Object((1,3,6,1,4,1,12740,19,1,2,1,88),_EqlDcbxLocPfcUnpausePri3_Type())
eqlDcbxLocPfcUnpausePri3.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbxLocPfcUnpausePri3.setStatus(_A)
_EqlDcbxLocPfcUnpausePri4_Type=Counter64
_EqlDcbxLocPfcUnpausePri4_Object=MibTableColumn
eqlDcbxLocPfcUnpausePri4=_EqlDcbxLocPfcUnpausePri4_Object((1,3,6,1,4,1,12740,19,1,2,1,89),_EqlDcbxLocPfcUnpausePri4_Type())
eqlDcbxLocPfcUnpausePri4.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbxLocPfcUnpausePri4.setStatus(_A)
_EqlDcbxLocPfcUnpausePri5_Type=Counter64
_EqlDcbxLocPfcUnpausePri5_Object=MibTableColumn
eqlDcbxLocPfcUnpausePri5=_EqlDcbxLocPfcUnpausePri5_Object((1,3,6,1,4,1,12740,19,1,2,1,90),_EqlDcbxLocPfcUnpausePri5_Type())
eqlDcbxLocPfcUnpausePri5.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbxLocPfcUnpausePri5.setStatus(_A)
_EqlDcbxLocPfcUnpausePri6_Type=Counter64
_EqlDcbxLocPfcUnpausePri6_Object=MibTableColumn
eqlDcbxLocPfcUnpausePri6=_EqlDcbxLocPfcUnpausePri6_Object((1,3,6,1,4,1,12740,19,1,2,1,91),_EqlDcbxLocPfcUnpausePri6_Type())
eqlDcbxLocPfcUnpausePri6.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbxLocPfcUnpausePri6.setStatus(_A)
_EqlDcbxLocPfcUnpausePri7_Type=Counter64
_EqlDcbxLocPfcUnpausePri7_Object=MibTableColumn
eqlDcbxLocPfcUnpausePri7=_EqlDcbxLocPfcUnpausePri7_Object((1,3,6,1,4,1,12740,19,1,2,1,92),_EqlDcbxLocPfcUnpausePri7_Type())
eqlDcbxLocPfcUnpausePri7.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbxLocPfcUnpausePri7.setStatus(_A)
_EqlDcbxLocETSConTsaTc0_Type=EqlDcbxTransmissionSelectionAlgorithm
_EqlDcbxLocETSConTsaTc0_Object=MibTableColumn
eqlDcbxLocETSConTsaTc0=_EqlDcbxLocETSConTsaTc0_Object((1,3,6,1,4,1,12740,19,1,2,1,93),_EqlDcbxLocETSConTsaTc0_Type())
eqlDcbxLocETSConTsaTc0.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbxLocETSConTsaTc0.setStatus(_A)
_EqlDcbxLocETSConTsaTc1_Type=EqlDcbxTransmissionSelectionAlgorithm
_EqlDcbxLocETSConTsaTc1_Object=MibTableColumn
eqlDcbxLocETSConTsaTc1=_EqlDcbxLocETSConTsaTc1_Object((1,3,6,1,4,1,12740,19,1,2,1,94),_EqlDcbxLocETSConTsaTc1_Type())
eqlDcbxLocETSConTsaTc1.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbxLocETSConTsaTc1.setStatus(_A)
_EqlDcbxLocETSConTsaTc2_Type=EqlDcbxTransmissionSelectionAlgorithm
_EqlDcbxLocETSConTsaTc2_Object=MibTableColumn
eqlDcbxLocETSConTsaTc2=_EqlDcbxLocETSConTsaTc2_Object((1,3,6,1,4,1,12740,19,1,2,1,95),_EqlDcbxLocETSConTsaTc2_Type())
eqlDcbxLocETSConTsaTc2.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbxLocETSConTsaTc2.setStatus(_A)
_EqlDcbxLocETSConTsaTc3_Type=EqlDcbxTransmissionSelectionAlgorithm
_EqlDcbxLocETSConTsaTc3_Object=MibTableColumn
eqlDcbxLocETSConTsaTc3=_EqlDcbxLocETSConTsaTc3_Object((1,3,6,1,4,1,12740,19,1,2,1,96),_EqlDcbxLocETSConTsaTc3_Type())
eqlDcbxLocETSConTsaTc3.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbxLocETSConTsaTc3.setStatus(_A)
_EqlDcbxLocETSConTsaTc4_Type=EqlDcbxTransmissionSelectionAlgorithm
_EqlDcbxLocETSConTsaTc4_Object=MibTableColumn
eqlDcbxLocETSConTsaTc4=_EqlDcbxLocETSConTsaTc4_Object((1,3,6,1,4,1,12740,19,1,2,1,97),_EqlDcbxLocETSConTsaTc4_Type())
eqlDcbxLocETSConTsaTc4.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbxLocETSConTsaTc4.setStatus(_A)
_EqlDcbxLocETSConTsaTc5_Type=EqlDcbxTransmissionSelectionAlgorithm
_EqlDcbxLocETSConTsaTc5_Object=MibTableColumn
eqlDcbxLocETSConTsaTc5=_EqlDcbxLocETSConTsaTc5_Object((1,3,6,1,4,1,12740,19,1,2,1,98),_EqlDcbxLocETSConTsaTc5_Type())
eqlDcbxLocETSConTsaTc5.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbxLocETSConTsaTc5.setStatus(_A)
_EqlDcbxLocETSConTsaTc6_Type=EqlDcbxTransmissionSelectionAlgorithm
_EqlDcbxLocETSConTsaTc6_Object=MibTableColumn
eqlDcbxLocETSConTsaTc6=_EqlDcbxLocETSConTsaTc6_Object((1,3,6,1,4,1,12740,19,1,2,1,99),_EqlDcbxLocETSConTsaTc6_Type())
eqlDcbxLocETSConTsaTc6.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbxLocETSConTsaTc6.setStatus(_A)
_EqlDcbxLocETSConTsaTc7_Type=EqlDcbxTransmissionSelectionAlgorithm
_EqlDcbxLocETSConTsaTc7_Object=MibTableColumn
eqlDcbxLocETSConTsaTc7=_EqlDcbxLocETSConTsaTc7_Object((1,3,6,1,4,1,12740,19,1,2,1,100),_EqlDcbxLocETSConTsaTc7_Type())
eqlDcbxLocETSConTsaTc7.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbxLocETSConTsaTc7.setStatus(_A)
_EqlDcbxLocETSRecoTsaTc0_Type=EqlDcbxTransmissionSelectionAlgorithm
_EqlDcbxLocETSRecoTsaTc0_Object=MibTableColumn
eqlDcbxLocETSRecoTsaTc0=_EqlDcbxLocETSRecoTsaTc0_Object((1,3,6,1,4,1,12740,19,1,2,1,101),_EqlDcbxLocETSRecoTsaTc0_Type())
eqlDcbxLocETSRecoTsaTc0.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbxLocETSRecoTsaTc0.setStatus(_A)
_EqlDcbxLocETSRecoTsaTc1_Type=EqlDcbxTransmissionSelectionAlgorithm
_EqlDcbxLocETSRecoTsaTc1_Object=MibTableColumn
eqlDcbxLocETSRecoTsaTc1=_EqlDcbxLocETSRecoTsaTc1_Object((1,3,6,1,4,1,12740,19,1,2,1,102),_EqlDcbxLocETSRecoTsaTc1_Type())
eqlDcbxLocETSRecoTsaTc1.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbxLocETSRecoTsaTc1.setStatus(_A)
_EqlDcbxLocETSRecoTsaTc2_Type=EqlDcbxTransmissionSelectionAlgorithm
_EqlDcbxLocETSRecoTsaTc2_Object=MibTableColumn
eqlDcbxLocETSRecoTsaTc2=_EqlDcbxLocETSRecoTsaTc2_Object((1,3,6,1,4,1,12740,19,1,2,1,103),_EqlDcbxLocETSRecoTsaTc2_Type())
eqlDcbxLocETSRecoTsaTc2.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbxLocETSRecoTsaTc2.setStatus(_A)
_EqlDcbxLocETSRecoTsaTc3_Type=EqlDcbxTransmissionSelectionAlgorithm
_EqlDcbxLocETSRecoTsaTc3_Object=MibTableColumn
eqlDcbxLocETSRecoTsaTc3=_EqlDcbxLocETSRecoTsaTc3_Object((1,3,6,1,4,1,12740,19,1,2,1,104),_EqlDcbxLocETSRecoTsaTc3_Type())
eqlDcbxLocETSRecoTsaTc3.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbxLocETSRecoTsaTc3.setStatus(_A)
_EqlDcbxLocETSRecoTsaTc4_Type=EqlDcbxTransmissionSelectionAlgorithm
_EqlDcbxLocETSRecoTsaTc4_Object=MibTableColumn
eqlDcbxLocETSRecoTsaTc4=_EqlDcbxLocETSRecoTsaTc4_Object((1,3,6,1,4,1,12740,19,1,2,1,105),_EqlDcbxLocETSRecoTsaTc4_Type())
eqlDcbxLocETSRecoTsaTc4.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbxLocETSRecoTsaTc4.setStatus(_A)
_EqlDcbxLocETSRecoTsaTc5_Type=EqlDcbxTransmissionSelectionAlgorithm
_EqlDcbxLocETSRecoTsaTc5_Object=MibTableColumn
eqlDcbxLocETSRecoTsaTc5=_EqlDcbxLocETSRecoTsaTc5_Object((1,3,6,1,4,1,12740,19,1,2,1,106),_EqlDcbxLocETSRecoTsaTc5_Type())
eqlDcbxLocETSRecoTsaTc5.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbxLocETSRecoTsaTc5.setStatus(_A)
_EqlDcbxLocETSRecoTsaTc6_Type=EqlDcbxTransmissionSelectionAlgorithm
_EqlDcbxLocETSRecoTsaTc6_Object=MibTableColumn
eqlDcbxLocETSRecoTsaTc6=_EqlDcbxLocETSRecoTsaTc6_Object((1,3,6,1,4,1,12740,19,1,2,1,107),_EqlDcbxLocETSRecoTsaTc6_Type())
eqlDcbxLocETSRecoTsaTc6.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbxLocETSRecoTsaTc6.setStatus(_A)
_EqlDcbxLocETSRecoTsaTc7_Type=EqlDcbxTransmissionSelectionAlgorithm
_EqlDcbxLocETSRecoTsaTc7_Object=MibTableColumn
eqlDcbxLocETSRecoTsaTc7=_EqlDcbxLocETSRecoTsaTc7_Object((1,3,6,1,4,1,12740,19,1,2,1,108),_EqlDcbxLocETSRecoTsaTc7_Type())
eqlDcbxLocETSRecoTsaTc7.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbxLocETSRecoTsaTc7.setStatus(_A)
_EqlDcbxRemETSConTsaTc0_Type=EqlDcbxTransmissionSelectionAlgorithm
_EqlDcbxRemETSConTsaTc0_Object=MibTableColumn
eqlDcbxRemETSConTsaTc0=_EqlDcbxRemETSConTsaTc0_Object((1,3,6,1,4,1,12740,19,1,2,1,109),_EqlDcbxRemETSConTsaTc0_Type())
eqlDcbxRemETSConTsaTc0.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbxRemETSConTsaTc0.setStatus(_A)
_EqlDcbxRemETSConTsaTc1_Type=EqlDcbxTransmissionSelectionAlgorithm
_EqlDcbxRemETSConTsaTc1_Object=MibTableColumn
eqlDcbxRemETSConTsaTc1=_EqlDcbxRemETSConTsaTc1_Object((1,3,6,1,4,1,12740,19,1,2,1,110),_EqlDcbxRemETSConTsaTc1_Type())
eqlDcbxRemETSConTsaTc1.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbxRemETSConTsaTc1.setStatus(_A)
_EqlDcbxRemETSConTsaTc2_Type=EqlDcbxTransmissionSelectionAlgorithm
_EqlDcbxRemETSConTsaTc2_Object=MibTableColumn
eqlDcbxRemETSConTsaTc2=_EqlDcbxRemETSConTsaTc2_Object((1,3,6,1,4,1,12740,19,1,2,1,111),_EqlDcbxRemETSConTsaTc2_Type())
eqlDcbxRemETSConTsaTc2.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbxRemETSConTsaTc2.setStatus(_A)
_EqlDcbxRemETSConTsaTc3_Type=EqlDcbxTransmissionSelectionAlgorithm
_EqlDcbxRemETSConTsaTc3_Object=MibTableColumn
eqlDcbxRemETSConTsaTc3=_EqlDcbxRemETSConTsaTc3_Object((1,3,6,1,4,1,12740,19,1,2,1,112),_EqlDcbxRemETSConTsaTc3_Type())
eqlDcbxRemETSConTsaTc3.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbxRemETSConTsaTc3.setStatus(_A)
_EqlDcbxRemETSConTsaTc4_Type=EqlDcbxTransmissionSelectionAlgorithm
_EqlDcbxRemETSConTsaTc4_Object=MibTableColumn
eqlDcbxRemETSConTsaTc4=_EqlDcbxRemETSConTsaTc4_Object((1,3,6,1,4,1,12740,19,1,2,1,113),_EqlDcbxRemETSConTsaTc4_Type())
eqlDcbxRemETSConTsaTc4.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbxRemETSConTsaTc4.setStatus(_A)
_EqlDcbxRemETSConTsaTc5_Type=EqlDcbxTransmissionSelectionAlgorithm
_EqlDcbxRemETSConTsaTc5_Object=MibTableColumn
eqlDcbxRemETSConTsaTc5=_EqlDcbxRemETSConTsaTc5_Object((1,3,6,1,4,1,12740,19,1,2,1,114),_EqlDcbxRemETSConTsaTc5_Type())
eqlDcbxRemETSConTsaTc5.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbxRemETSConTsaTc5.setStatus(_A)
_EqlDcbxRemETSConTsaTc6_Type=EqlDcbxTransmissionSelectionAlgorithm
_EqlDcbxRemETSConTsaTc6_Object=MibTableColumn
eqlDcbxRemETSConTsaTc6=_EqlDcbxRemETSConTsaTc6_Object((1,3,6,1,4,1,12740,19,1,2,1,115),_EqlDcbxRemETSConTsaTc6_Type())
eqlDcbxRemETSConTsaTc6.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbxRemETSConTsaTc6.setStatus(_A)
_EqlDcbxRemETSConTsaTc7_Type=EqlDcbxTransmissionSelectionAlgorithm
_EqlDcbxRemETSConTsaTc7_Object=MibTableColumn
eqlDcbxRemETSConTsaTc7=_EqlDcbxRemETSConTsaTc7_Object((1,3,6,1,4,1,12740,19,1,2,1,116),_EqlDcbxRemETSConTsaTc7_Type())
eqlDcbxRemETSConTsaTc7.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbxRemETSConTsaTc7.setStatus(_A)
_EqlDcbxRemETSRecoTsaTc0_Type=EqlDcbxTransmissionSelectionAlgorithm
_EqlDcbxRemETSRecoTsaTc0_Object=MibTableColumn
eqlDcbxRemETSRecoTsaTc0=_EqlDcbxRemETSRecoTsaTc0_Object((1,3,6,1,4,1,12740,19,1,2,1,117),_EqlDcbxRemETSRecoTsaTc0_Type())
eqlDcbxRemETSRecoTsaTc0.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbxRemETSRecoTsaTc0.setStatus(_A)
_EqlDcbxRemETSRecoTsaTc1_Type=EqlDcbxTransmissionSelectionAlgorithm
_EqlDcbxRemETSRecoTsaTc1_Object=MibTableColumn
eqlDcbxRemETSRecoTsaTc1=_EqlDcbxRemETSRecoTsaTc1_Object((1,3,6,1,4,1,12740,19,1,2,1,118),_EqlDcbxRemETSRecoTsaTc1_Type())
eqlDcbxRemETSRecoTsaTc1.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbxRemETSRecoTsaTc1.setStatus(_A)
_EqlDcbxRemETSRecoTsaTc2_Type=EqlDcbxTransmissionSelectionAlgorithm
_EqlDcbxRemETSRecoTsaTc2_Object=MibTableColumn
eqlDcbxRemETSRecoTsaTc2=_EqlDcbxRemETSRecoTsaTc2_Object((1,3,6,1,4,1,12740,19,1,2,1,119),_EqlDcbxRemETSRecoTsaTc2_Type())
eqlDcbxRemETSRecoTsaTc2.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbxRemETSRecoTsaTc2.setStatus(_A)
_EqlDcbxRemETSRecoTsaTc3_Type=EqlDcbxTransmissionSelectionAlgorithm
_EqlDcbxRemETSRecoTsaTc3_Object=MibTableColumn
eqlDcbxRemETSRecoTsaTc3=_EqlDcbxRemETSRecoTsaTc3_Object((1,3,6,1,4,1,12740,19,1,2,1,120),_EqlDcbxRemETSRecoTsaTc3_Type())
eqlDcbxRemETSRecoTsaTc3.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbxRemETSRecoTsaTc3.setStatus(_A)
_EqlDcbxRemETSRecoTsaTc4_Type=EqlDcbxTransmissionSelectionAlgorithm
_EqlDcbxRemETSRecoTsaTc4_Object=MibTableColumn
eqlDcbxRemETSRecoTsaTc4=_EqlDcbxRemETSRecoTsaTc4_Object((1,3,6,1,4,1,12740,19,1,2,1,121),_EqlDcbxRemETSRecoTsaTc4_Type())
eqlDcbxRemETSRecoTsaTc4.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbxRemETSRecoTsaTc4.setStatus(_A)
_EqlDcbxRemETSRecoTsaTc5_Type=EqlDcbxTransmissionSelectionAlgorithm
_EqlDcbxRemETSRecoTsaTc5_Object=MibTableColumn
eqlDcbxRemETSRecoTsaTc5=_EqlDcbxRemETSRecoTsaTc5_Object((1,3,6,1,4,1,12740,19,1,2,1,122),_EqlDcbxRemETSRecoTsaTc5_Type())
eqlDcbxRemETSRecoTsaTc5.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbxRemETSRecoTsaTc5.setStatus(_A)
_EqlDcbxRemETSRecoTsaTc6_Type=EqlDcbxTransmissionSelectionAlgorithm
_EqlDcbxRemETSRecoTsaTc6_Object=MibTableColumn
eqlDcbxRemETSRecoTsaTc6=_EqlDcbxRemETSRecoTsaTc6_Object((1,3,6,1,4,1,12740,19,1,2,1,123),_EqlDcbxRemETSRecoTsaTc6_Type())
eqlDcbxRemETSRecoTsaTc6.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbxRemETSRecoTsaTc6.setStatus(_A)
_EqlDcbxRemETSRecoTsaTc7_Type=EqlDcbxTransmissionSelectionAlgorithm
_EqlDcbxRemETSRecoTsaTc7_Object=MibTableColumn
eqlDcbxRemETSRecoTsaTc7=_EqlDcbxRemETSRecoTsaTc7_Object((1,3,6,1,4,1,12740,19,1,2,1,124),_EqlDcbxRemETSRecoTsaTc7_Type())
eqlDcbxRemETSRecoTsaTc7.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbxRemETSRecoTsaTc7.setStatus(_A)
_EqlDcbxLocDCBMode_Type=EqlDcbxMode
_EqlDcbxLocDCBMode_Object=MibTableColumn
eqlDcbxLocDCBMode=_EqlDcbxLocDCBMode_Object((1,3,6,1,4,1,12740,19,1,2,1,125),_EqlDcbxLocDCBMode_Type())
eqlDcbxLocDCBMode.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDcbxLocDCBMode.setStatus(_A)
mibBuilder.exportSymbols('EQL-DCB-MIB',**{_E:EqlDcbxTrafficClassGroupValue,'EqlDcbxAppSelector':EqlDcbxAppSelector,_U:EqlDcbxAppProtocol,_T:EqlDcbxSupportedCapacity,_Y:EqlVlanIdentifier,_K:EqlIEEE8021PriorityValue,_J:EqlIEEEDraftSubtypeValue,'EqlDcbxState':EqlDcbxState,'EqlDcbxVlanState':EqlDcbxVlanState,_F:EqlDcbxTransmissionSelectionAlgorithm,'EqlDcbxMode':EqlDcbxMode,'eqlDcbMib':eqlDcbMib,'eqlDcbMIBObjects':eqlDcbMIBObjects,'eqlDcbStaticIfTable':eqlDcbStaticIfTable,'eqlDcbStaticIfEntry':eqlDcbStaticIfEntry,'eqlDcbxConfigTCSupportedTxEnable':eqlDcbxConfigTCSupportedTxEnable,'eqlDcbxConfigETSConfigurationTxEnable':eqlDcbxConfigETSConfigurationTxEnable,'eqlDcbxConfigETSRecommendationTxEnable':eqlDcbxConfigETSRecommendationTxEnable,'eqlDcbxConfigPFCTxEnable':eqlDcbxConfigPFCTxEnable,'eqlDcbxConfigAppPriorityTxEnable':eqlDcbxConfigAppPriorityTxEnable,'eqlDcbxConfigQcnTxEnable':eqlDcbxConfigQcnTxEnable,'eqlDcbxAdminTCSupported':eqlDcbxAdminTCSupported,'eqlDcbxAdminETSConMaxTCG':eqlDcbxAdminETSConMaxTCG,'eqlDcbxAdminETSConWilling':eqlDcbxAdminETSConWilling,'eqlDcbxAdminETSConTrafficClassGroupBandwidthTable':eqlDcbxAdminETSConTrafficClassGroupBandwidthTable,'eqlDcbxAdminETSRecoTrafficClassGroupBandwidthTable':eqlDcbxAdminETSRecoTrafficClassGroupBandwidthTable,'eqlDcbxAdminPFCWilling':eqlDcbxAdminPFCWilling,'eqlDcbxAdminPFCMBC':eqlDcbxAdminPFCMBC,'eqlDcbxAdminPFCCap':eqlDcbxAdminPFCCap,'eqlDcbxAdminAppPriorityWilling':eqlDcbxAdminAppPriorityWilling,'eqlDcbxConfigAutoDetectVLANEnable':eqlDcbxConfigAutoDetectVLANEnable,'eqlDcbxConfigVLANId':eqlDcbxConfigVLANId,'eqlDcbxAdminETSConTrafficClassGroupPri0':eqlDcbxAdminETSConTrafficClassGroupPri0,'eqlDcbxAdminETSConTrafficClassGroupPri1':eqlDcbxAdminETSConTrafficClassGroupPri1,'eqlDcbxAdminETSConTrafficClassGroupPri2':eqlDcbxAdminETSConTrafficClassGroupPri2,'eqlDcbxAdminETSConTrafficClassGroupPri3':eqlDcbxAdminETSConTrafficClassGroupPri3,'eqlDcbxAdminETSConTrafficClassGroupPri4':eqlDcbxAdminETSConTrafficClassGroupPri4,'eqlDcbxAdminETSConTrafficClassGroupPri5':eqlDcbxAdminETSConTrafficClassGroupPri5,'eqlDcbxAdminETSConTrafficClassGroupPri6':eqlDcbxAdminETSConTrafficClassGroupPri6,'eqlDcbxAdminETSConTrafficClassGroupPri7':eqlDcbxAdminETSConTrafficClassGroupPri7,'eqlDcbxAdminPFCEnableEnabledPri0':eqlDcbxAdminPFCEnableEnabledPri0,'eqlDcbxAdminPFCEnableEnabledPri1':eqlDcbxAdminPFCEnableEnabledPri1,'eqlDcbxAdminPFCEnableEnabledPri2':eqlDcbxAdminPFCEnableEnabledPri2,'eqlDcbxAdminPFCEnableEnabledPri3':eqlDcbxAdminPFCEnableEnabledPri3,'eqlDcbxAdminPFCEnableEnabledPri4':eqlDcbxAdminPFCEnableEnabledPri4,'eqlDcbxAdminPFCEnableEnabledPri5':eqlDcbxAdminPFCEnableEnabledPri5,'eqlDcbxAdminPFCEnableEnabledPri6':eqlDcbxAdminPFCEnableEnabledPri6,'eqlDcbxAdminPFCEnableEnabledPri7':eqlDcbxAdminPFCEnableEnabledPri7,'eqlDcbxAdminAppPriorityiSCSITxEnable':eqlDcbxAdminAppPriorityiSCSITxEnable,'eqlDcbxAdminAppPriorityiSCSIProtocol':eqlDcbxAdminAppPriorityiSCSIProtocol,'eqlDcbxAdminAppPriorityiSCSIPriority':eqlDcbxAdminAppPriorityiSCSIPriority,'eqlDcbxAdminAppPriorityFCoETxEnable':eqlDcbxAdminAppPriorityFCoETxEnable,'eqlDcbxAdminAppPriorityFCoEProtocol':eqlDcbxAdminAppPriorityFCoEProtocol,'eqlDcbxAdminAppPriorityFCoEPriority':eqlDcbxAdminAppPriorityFCoEPriority,'eqlDcbxConfigDCBEnable':eqlDcbxConfigDCBEnable,'eqlDcbxConfigDCBX101Enable':eqlDcbxConfigDCBX101Enable,'eqlDcbxConfigDCBXIEEEDraftEnable':eqlDcbxConfigDCBXIEEEDraftEnable,'eqlDcbxConfigQcnSubtype':eqlDcbxConfigQcnSubtype,'eqlDcbxConfigETSConSubtype':eqlDcbxConfigETSConSubtype,'eqlDcbxConfigETSRecoSubtype':eqlDcbxConfigETSRecoSubtype,'eqlDcbxConfigPFCSubtype':eqlDcbxConfigPFCSubtype,'eqlDcbxConfigAppPrioritySubtype':eqlDcbxConfigAppPrioritySubtype,'eqlDcbxConfigTCSupportedSubtype':eqlDcbxConfigTCSupportedSubtype,'eqlDcbxAdminETSRecoTrafficClassGroupPri0':eqlDcbxAdminETSRecoTrafficClassGroupPri0,'eqlDcbxAdminETSRecoTrafficClassGroupPri1':eqlDcbxAdminETSRecoTrafficClassGroupPri1,'eqlDcbxAdminETSRecoTrafficClassGroupPri2':eqlDcbxAdminETSRecoTrafficClassGroupPri2,'eqlDcbxAdminETSRecoTrafficClassGroupPri3':eqlDcbxAdminETSRecoTrafficClassGroupPri3,'eqlDcbxAdminETSRecoTrafficClassGroupPri4':eqlDcbxAdminETSRecoTrafficClassGroupPri4,'eqlDcbxAdminETSRecoTrafficClassGroupPri5':eqlDcbxAdminETSRecoTrafficClassGroupPri5,'eqlDcbxAdminETSRecoTrafficClassGroupPri6':eqlDcbxAdminETSRecoTrafficClassGroupPri6,'eqlDcbxAdminETSRecoTrafficClassGroupPri7':eqlDcbxAdminETSRecoTrafficClassGroupPri7,'eqlDcbCnGlobalMasterEnable':eqlDcbCnGlobalMasterEnable,'eqlDcbCnRpPortPriMaxRps':eqlDcbCnRpPortPriMaxRps,'eqlDcbCnRpgEnablePri0':eqlDcbCnRpgEnablePri0,'eqlDcbCnRpgEnablePri1':eqlDcbCnRpgEnablePri1,'eqlDcbCnRpgEnablePri2':eqlDcbCnRpgEnablePri2,'eqlDcbCnRpgEnablePri3':eqlDcbCnRpgEnablePri3,'eqlDcbCnRpgEnablePri4':eqlDcbCnRpgEnablePri4,'eqlDcbCnRpgEnablePri5':eqlDcbCnRpgEnablePri5,'eqlDcbCnRpgEnablePri6':eqlDcbCnRpgEnablePri6,'eqlDcbCnRpgEnablePri7':eqlDcbCnRpgEnablePri7,'eqlDcbCnRpgTimeReset':eqlDcbCnRpgTimeReset,'eqlDcbCnRpgByteReset':eqlDcbCnRpgByteReset,'eqlDcbCnRpgThreshold':eqlDcbCnRpgThreshold,'eqlDcbCnRpgMaxRate':eqlDcbCnRpgMaxRate,'eqlDcbCnRpgAiRate':eqlDcbCnRpgAiRate,'eqlDcbCnRpgHaiRate':eqlDcbCnRpgHaiRate,'eqlDcbCnRpgGd':eqlDcbCnRpgGd,'eqlDcbCnRpgMinDecFac':eqlDcbCnRpgMinDecFac,'eqlDcbCnRpgMinRate':eqlDcbCnRpgMinRate,'eqlDcbDefaultiSCSIPriority':eqlDcbDefaultiSCSIPriority,'eqlDcbDefaultFCoEPriority':eqlDcbDefaultFCoEPriority,'eqlDcbxAdminETSConTsaTc0':eqlDcbxAdminETSConTsaTc0,'eqlDcbxAdminETSConTsaTc1':eqlDcbxAdminETSConTsaTc1,'eqlDcbxAdminETSConTsaTc2':eqlDcbxAdminETSConTsaTc2,'eqlDcbxAdminETSConTsaTc3':eqlDcbxAdminETSConTsaTc3,'eqlDcbxAdminETSConTsaTc4':eqlDcbxAdminETSConTsaTc4,'eqlDcbxAdminETSConTsaTc5':eqlDcbxAdminETSConTsaTc5,'eqlDcbxAdminETSConTsaTc6':eqlDcbxAdminETSConTsaTc6,'eqlDcbxAdminETSConTsaTc7':eqlDcbxAdminETSConTsaTc7,'eqlDcbxAdminETSRecoTsaTc0':eqlDcbxAdminETSRecoTsaTc0,'eqlDcbxAdminETSRecoTsaTc1':eqlDcbxAdminETSRecoTsaTc1,'eqlDcbxAdminETSRecoTsaTc2':eqlDcbxAdminETSRecoTsaTc2,'eqlDcbxAdminETSRecoTsaTc3':eqlDcbxAdminETSRecoTsaTc3,'eqlDcbxAdminETSRecoTsaTc4':eqlDcbxAdminETSRecoTsaTc4,'eqlDcbxAdminETSRecoTsaTc5':eqlDcbxAdminETSRecoTsaTc5,'eqlDcbxAdminETSRecoTsaTc6':eqlDcbxAdminETSRecoTsaTc6,'eqlDcbxAdminETSRecoTsaTc7':eqlDcbxAdminETSRecoTsaTc7,'eqlDcbDynamicIfTable':eqlDcbDynamicIfTable,'eqlDcbDynamicIfEntry':eqlDcbDynamicIfEntry,'eqlDcbPfcRequestsSent':eqlDcbPfcRequestsSent,'eqlDcbPfcIndicationsReceived':eqlDcbPfcIndicationsReceived,'eqlDcbxLocTCSupported':eqlDcbxLocTCSupported,'eqlDcbxLocETSConMaxTCG':eqlDcbxLocETSConMaxTCG,'eqlDcbxLocETSConWilling':eqlDcbxLocETSConWilling,'eqlDcbxLocETSConTrafficClassGroupBandwidthTable':eqlDcbxLocETSConTrafficClassGroupBandwidthTable,'eqlDcbxLocETSRecoTrafficClassGroupBandwidthTable':eqlDcbxLocETSRecoTrafficClassGroupBandwidthTable,'eqlDcbxLocPFCWilling':eqlDcbxLocPFCWilling,'eqlDcbxLocPFCMBC':eqlDcbxLocPFCMBC,'eqlDcbxLocPFCCap':eqlDcbxLocPFCCap,'eqlDcbxLocAppPriorityWilling':eqlDcbxLocAppPriorityWilling,'eqlDcbxRemTCSupported':eqlDcbxRemTCSupported,'eqlDcbxRemETSConMaxTCG':eqlDcbxRemETSConMaxTCG,'eqlDcbxRemETSConWilling':eqlDcbxRemETSConWilling,'eqlDcbxRemETSConTrafficClassGroupBandwidthTable':eqlDcbxRemETSConTrafficClassGroupBandwidthTable,'eqlDcbxRemETSRecoTrafficClassGroupBandwidthTable':eqlDcbxRemETSRecoTrafficClassGroupBandwidthTable,'eqlDcbxRemPFCWilling':eqlDcbxRemPFCWilling,'eqlDcbxRemPFCMBC':eqlDcbxRemPFCMBC,'eqlDcbxRemPFCCap':eqlDcbxRemPFCCap,'eqlDcbxRemAppPriorityWilling':eqlDcbxRemAppPriorityWilling,'eqlDcbxLocETSConTrafficClassGroupPri0':eqlDcbxLocETSConTrafficClassGroupPri0,'eqlDcbxLocETSConTrafficClassGroupPri1':eqlDcbxLocETSConTrafficClassGroupPri1,'eqlDcbxLocETSConTrafficClassGroupPri2':eqlDcbxLocETSConTrafficClassGroupPri2,'eqlDcbxLocETSConTrafficClassGroupPri3':eqlDcbxLocETSConTrafficClassGroupPri3,'eqlDcbxLocETSConTrafficClassGroupPri4':eqlDcbxLocETSConTrafficClassGroupPri4,'eqlDcbxLocETSConTrafficClassGroupPri5':eqlDcbxLocETSConTrafficClassGroupPri5,'eqlDcbxLocETSConTrafficClassGroupPri6':eqlDcbxLocETSConTrafficClassGroupPri6,'eqlDcbxLocETSConTrafficClassGroupPri7':eqlDcbxLocETSConTrafficClassGroupPri7,'eqlDcbxLocPFCEnableEnabledPri0':eqlDcbxLocPFCEnableEnabledPri0,'eqlDcbxLocPFCEnableEnabledPri1':eqlDcbxLocPFCEnableEnabledPri1,'eqlDcbxLocPFCEnableEnabledPri2':eqlDcbxLocPFCEnableEnabledPri2,'eqlDcbxLocPFCEnableEnabledPri3':eqlDcbxLocPFCEnableEnabledPri3,'eqlDcbxLocPFCEnableEnabledPri4':eqlDcbxLocPFCEnableEnabledPri4,'eqlDcbxLocPFCEnableEnabledPri5':eqlDcbxLocPFCEnableEnabledPri5,'eqlDcbxLocPFCEnableEnabledPri6':eqlDcbxLocPFCEnableEnabledPri6,'eqlDcbxLocPFCEnableEnabledPri7':eqlDcbxLocPFCEnableEnabledPri7,'eqlDcbxLocVLANId':eqlDcbxLocVLANId,'eqlDcbxLocVLANState':eqlDcbxLocVLANState,'eqlDcbxLocDCBState':eqlDcbxLocDCBState,'eqlDcbxLocPFCState':eqlDcbxLocPFCState,'eqlDcbxLocETSState':eqlDcbxLocETSState,'eqlDcbxLocQCNState':eqlDcbxLocQCNState,'eqlDcbxLociSCSIPriority':eqlDcbxLociSCSIPriority,'eqlDcbxLocFCoEPriority':eqlDcbxLocFCoEPriority,'eqlDcbxLocBytesRxPri0':eqlDcbxLocBytesRxPri0,'eqlDcbxLocBytesRxPri1':eqlDcbxLocBytesRxPri1,'eqlDcbxLocBytesRxPri2':eqlDcbxLocBytesRxPri2,'eqlDcbxLocBytesRxPri3':eqlDcbxLocBytesRxPri3,'eqlDcbxLocBytesRxPri4':eqlDcbxLocBytesRxPri4,'eqlDcbxLocBytesRxPri5':eqlDcbxLocBytesRxPri5,'eqlDcbxLocBytesRxPri6':eqlDcbxLocBytesRxPri6,'eqlDcbxLocBytesRxPri7':eqlDcbxLocBytesRxPri7,'eqlDcbxLocBytesTxPri0':eqlDcbxLocBytesTxPri0,'eqlDcbxLocBytesTxPri1':eqlDcbxLocBytesTxPri1,'eqlDcbxLocBytesTxPri2':eqlDcbxLocBytesTxPri2,'eqlDcbxLocBytesTxPri3':eqlDcbxLocBytesTxPri3,'eqlDcbxLocBytesTxPri4':eqlDcbxLocBytesTxPri4,'eqlDcbxLocBytesTxPri5':eqlDcbxLocBytesTxPri5,'eqlDcbxLocBytesTxPri6':eqlDcbxLocBytesTxPri6,'eqlDcbxLocBytesTxPri7':eqlDcbxLocBytesTxPri7,'eqlDcbCnRpPortPriCreatedRpsPri0':eqlDcbCnRpPortPriCreatedRpsPri0,'eqlDcbCnRpPortPriCreatedRpsPri1':eqlDcbCnRpPortPriCreatedRpsPri1,'eqlDcbCnRpPortPriCreatedRpsPri2':eqlDcbCnRpPortPriCreatedRpsPri2,'eqlDcbCnRpPortPriCreatedRpsPri3':eqlDcbCnRpPortPriCreatedRpsPri3,'eqlDcbCnRpPortPriCreatedRpsPri4':eqlDcbCnRpPortPriCreatedRpsPri4,'eqlDcbCnRpPortPriCreatedRpsPri5':eqlDcbCnRpPortPriCreatedRpsPri5,'eqlDcbCnRpPortPriCreatedRpsPri6':eqlDcbCnRpPortPriCreatedRpsPri6,'eqlDcbCnRpPortPriCreatedRpsPri7':eqlDcbCnRpPortPriCreatedRpsPri7,'eqlDcbCnRpPortPriCentisecondsPri0':eqlDcbCnRpPortPriCentisecondsPri0,'eqlDcbCnRpPortPriCentisecondsPri1':eqlDcbCnRpPortPriCentisecondsPri1,'eqlDcbCnRpPortPriCentisecondsPri2':eqlDcbCnRpPortPriCentisecondsPri2,'eqlDcbCnRpPortPriCentisecondsPri3':eqlDcbCnRpPortPriCentisecondsPri3,'eqlDcbCnRpPortPriCentisecondsPri4':eqlDcbCnRpPortPriCentisecondsPri4,'eqlDcbCnRpPortPriCentisecondsPri5':eqlDcbCnRpPortPriCentisecondsPri5,'eqlDcbCnRpPortPriCentisecondsPri6':eqlDcbCnRpPortPriCentisecondsPri6,'eqlDcbCnRpPortPriCentisecondsPri7':eqlDcbCnRpPortPriCentisecondsPri7,'eqlDcbxLocPfcPausePri0':eqlDcbxLocPfcPausePri0,'eqlDcbxLocPfcPausePri1':eqlDcbxLocPfcPausePri1,'eqlDcbxLocPfcPausePri2':eqlDcbxLocPfcPausePri2,'eqlDcbxLocPfcPausePri3':eqlDcbxLocPfcPausePri3,'eqlDcbxLocPfcPausePri4':eqlDcbxLocPfcPausePri4,'eqlDcbxLocPfcPausePri5':eqlDcbxLocPfcPausePri5,'eqlDcbxLocPfcPausePri6':eqlDcbxLocPfcPausePri6,'eqlDcbxLocPfcPausePri7':eqlDcbxLocPfcPausePri7,'eqlDcbxLocPfcUnpausePri0':eqlDcbxLocPfcUnpausePri0,'eqlDcbxLocPfcUnpausePri1':eqlDcbxLocPfcUnpausePri1,'eqlDcbxLocPfcUnpausePri2':eqlDcbxLocPfcUnpausePri2,'eqlDcbxLocPfcUnpausePri3':eqlDcbxLocPfcUnpausePri3,'eqlDcbxLocPfcUnpausePri4':eqlDcbxLocPfcUnpausePri4,'eqlDcbxLocPfcUnpausePri5':eqlDcbxLocPfcUnpausePri5,'eqlDcbxLocPfcUnpausePri6':eqlDcbxLocPfcUnpausePri6,'eqlDcbxLocPfcUnpausePri7':eqlDcbxLocPfcUnpausePri7,'eqlDcbxLocETSConTsaTc0':eqlDcbxLocETSConTsaTc0,'eqlDcbxLocETSConTsaTc1':eqlDcbxLocETSConTsaTc1,'eqlDcbxLocETSConTsaTc2':eqlDcbxLocETSConTsaTc2,'eqlDcbxLocETSConTsaTc3':eqlDcbxLocETSConTsaTc3,'eqlDcbxLocETSConTsaTc4':eqlDcbxLocETSConTsaTc4,'eqlDcbxLocETSConTsaTc5':eqlDcbxLocETSConTsaTc5,'eqlDcbxLocETSConTsaTc6':eqlDcbxLocETSConTsaTc6,'eqlDcbxLocETSConTsaTc7':eqlDcbxLocETSConTsaTc7,'eqlDcbxLocETSRecoTsaTc0':eqlDcbxLocETSRecoTsaTc0,'eqlDcbxLocETSRecoTsaTc1':eqlDcbxLocETSRecoTsaTc1,'eqlDcbxLocETSRecoTsaTc2':eqlDcbxLocETSRecoTsaTc2,'eqlDcbxLocETSRecoTsaTc3':eqlDcbxLocETSRecoTsaTc3,'eqlDcbxLocETSRecoTsaTc4':eqlDcbxLocETSRecoTsaTc4,'eqlDcbxLocETSRecoTsaTc5':eqlDcbxLocETSRecoTsaTc5,'eqlDcbxLocETSRecoTsaTc6':eqlDcbxLocETSRecoTsaTc6,'eqlDcbxLocETSRecoTsaTc7':eqlDcbxLocETSRecoTsaTc7,'eqlDcbxRemETSConTsaTc0':eqlDcbxRemETSConTsaTc0,'eqlDcbxRemETSConTsaTc1':eqlDcbxRemETSConTsaTc1,'eqlDcbxRemETSConTsaTc2':eqlDcbxRemETSConTsaTc2,'eqlDcbxRemETSConTsaTc3':eqlDcbxRemETSConTsaTc3,'eqlDcbxRemETSConTsaTc4':eqlDcbxRemETSConTsaTc4,'eqlDcbxRemETSConTsaTc5':eqlDcbxRemETSConTsaTc5,'eqlDcbxRemETSConTsaTc6':eqlDcbxRemETSConTsaTc6,'eqlDcbxRemETSConTsaTc7':eqlDcbxRemETSConTsaTc7,'eqlDcbxRemETSRecoTsaTc0':eqlDcbxRemETSRecoTsaTc0,'eqlDcbxRemETSRecoTsaTc1':eqlDcbxRemETSRecoTsaTc1,'eqlDcbxRemETSRecoTsaTc2':eqlDcbxRemETSRecoTsaTc2,'eqlDcbxRemETSRecoTsaTc3':eqlDcbxRemETSRecoTsaTc3,'eqlDcbxRemETSRecoTsaTc4':eqlDcbxRemETSRecoTsaTc4,'eqlDcbxRemETSRecoTsaTc5':eqlDcbxRemETSRecoTsaTc5,'eqlDcbxRemETSRecoTsaTc6':eqlDcbxRemETSRecoTsaTc6,'eqlDcbxRemETSRecoTsaTc7':eqlDcbxRemETSRecoTsaTc7,'eqlDcbxLocDCBMode':eqlDcbxLocDCBMode})