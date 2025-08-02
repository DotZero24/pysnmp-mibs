_AB='ciscoDot11HtPhyEnhPowerLevelsGroup'
_AA='ciscoDot11HtPhyTxBfGroup'
_A9='ciscoDot11HtPhyMcsGroup'
_A8='ciscoDot11HtPhyConfigGroup'
_A7='ciscoDot11HtPhyAntennaGroup'
_A6='cD11HtPhyEnhPowerLevel40MHz'
_A5='cD11HtPhyEnhPowerLevel20MHz'
_A4='cD11HtPhyNumberCompSteerMatrixSupportAntenna'
_A3='cD11HtPhyNumberUncompSteerMatrixSupportAntenna'
_A2='cD11HtPhyNumberBeamFormingCSISupportAntenna'
_A1='cD11HtPhyExplCompSteerMatrixFdbkImplemented'
_A0='cD11HtPhyExplUncompSteerMatrixFdbkImplemented'
_z='cD11HtPhyExplBFCSIFdbkImplemented'
_y='cD11HtPhyExplUncompSteerMatrixImplemented'
_x='cD11HtPhyExplCSITxBFImplemented'
_w='cD11HtPhyCalibrationImplemented'
_v='cD11HtPhyImplicitTxBFImplemented'
_u='cD11HtPhyTxZLFImplemented'
_t='cD11HtPhyRxZLFImplemented'
_s='cD11HtPhyTxStaggerSoundImplemented'
_r='cD11HtPhyRxStaggerSoundImplemented'
_q='cD11HtPhySupportedMCSRxValue'
_p='cD11HtPhySupportedMCSTxValue'
_o='cD11HtPhyBeamFormingEnabled'
_n='cD11HtPhyBeamFormingImplemented'
_m='cD11HtPhyRxSTBCEnabled'
_l='cD11HtPhyRxSTBCImplemented'
_k='cD11HtPhyTxSTBCEnabled'
_j='cD11HtPhyTxSTBCImplemented'
_i='cD11HtPhyAdvancedCodingEnabled'
_h='cD11HtPhyAdvancedCodingImplemented'
_g='cD11HtPhyShortGIInFortyEnabled'
_f='cD11HtPhyShortGIInFortyImplemented'
_e='cD11HtPhyShortGIInTwentyEnabled'
_d='cD11HtPhyShortGIInTwentyImplemented'
_c='cD11HtPhyGreenFieldEnabled'
_b='cD11HtPhyGreenFieldImplemented'
_a='cD11HtPhyNumberOfSpatialStreamsEnabled'
_Z='cD11HtPhyNumberOfSpatialStreamsImplemented'
_Y='cD11HtPhyExtChannelCCAImplemented'
_X='cD11HtPhyCurrentExtensionChannel'
_W='cD11HtPhyCurrentControlChannel'
_V='cD11HtPhyFortyMHzOperationEnabled'
_U='cD11HtPhyFortyMHzOperationImplemented'
_T='cD11HtPhyOperBand'
_S='cD11HtPhyOperModeFrequency'
_R='cD11HtPhyOperatingMode'
_Q='cD11HtPhyXmitSoundPPDUImplemented'
_P='cD11HtPhyRcvAntennaSelImplemented'
_O='cD11HtPhyXmitIndCompFdbkASImplemented'
_N='cD11HtPhyExplCSIFdbkASImplemented'
_M='cD11HtPhyXmitIndFdbkASImplemented'
_L='cD11HtPhyXmitExpCSIFdbkASImplemented'
_K='cD11HtPhyAntennaSelectionImplemented'
_J='Unsigned32'
_I='OctetString'
_H='ifIndex'
_G='IF-MIB'
_F='read-write'
_E='Integer32'
_D='TruthValue'
_C='read-only'
_B='CISCO-DOT11-HT-PHY-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_I,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ifIndex,=mibBuilder.importSymbols(_G,_H)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_J,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_D)
ciscoDot11HtPhyMIB=ModuleIdentity((1,3,6,1,4,1,9,9,607))
if mibBuilder.loadTexts:ciscoDot11HtPhyMIB.setRevisions(('2006-12-11 00:00',))
class CD11HtPhyBeamformFeedback(TextualConvention,Bits):status=_A;namedValues=NamedValues(*(('unsolicited',0),('immediate',1),('aggregated',2)))
_CiscoDot11HtPhyMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoDot11HtPhyMIBNotifs=_CiscoDot11HtPhyMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,607,0))
_CiscoDot11HtPhyMIBObjects_ObjectIdentity=ObjectIdentity
ciscoDot11HtPhyMIBObjects=_CiscoDot11HtPhyMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,607,1))
_CD11HtPhy_ObjectIdentity=ObjectIdentity
cD11HtPhy=_CD11HtPhy_ObjectIdentity((1,3,6,1,4,1,9,9,607,1,1))
_CD11HtPhyAntennaTable_Object=MibTable
cD11HtPhyAntennaTable=_CD11HtPhyAntennaTable_Object((1,3,6,1,4,1,9,9,607,1,1,1))
if mibBuilder.loadTexts:cD11HtPhyAntennaTable.setStatus(_A)
_CD11HtPhyAntennaEntry_Object=MibTableRow
cD11HtPhyAntennaEntry=_CD11HtPhyAntennaEntry_Object((1,3,6,1,4,1,9,9,607,1,1,1,1))
cD11HtPhyAntennaEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:cD11HtPhyAntennaEntry.setStatus(_A)
class _CD11HtPhyAntennaSelectionImplemented_Type(TruthValue):defaultValue=2
_CD11HtPhyAntennaSelectionImplemented_Type.__name__=_D
_CD11HtPhyAntennaSelectionImplemented_Object=MibTableColumn
cD11HtPhyAntennaSelectionImplemented=_CD11HtPhyAntennaSelectionImplemented_Object((1,3,6,1,4,1,9,9,607,1,1,1,1,1),_CD11HtPhyAntennaSelectionImplemented_Type())
cD11HtPhyAntennaSelectionImplemented.setMaxAccess(_C)
if mibBuilder.loadTexts:cD11HtPhyAntennaSelectionImplemented.setStatus(_A)
class _CD11HtPhyXmitExpCSIFdbkASImplemented_Type(TruthValue):defaultValue=2
_CD11HtPhyXmitExpCSIFdbkASImplemented_Type.__name__=_D
_CD11HtPhyXmitExpCSIFdbkASImplemented_Object=MibTableColumn
cD11HtPhyXmitExpCSIFdbkASImplemented=_CD11HtPhyXmitExpCSIFdbkASImplemented_Object((1,3,6,1,4,1,9,9,607,1,1,1,1,5),_CD11HtPhyXmitExpCSIFdbkASImplemented_Type())
cD11HtPhyXmitExpCSIFdbkASImplemented.setMaxAccess(_C)
if mibBuilder.loadTexts:cD11HtPhyXmitExpCSIFdbkASImplemented.setStatus(_A)
class _CD11HtPhyXmitIndFdbkASImplemented_Type(TruthValue):defaultValue=2
_CD11HtPhyXmitIndFdbkASImplemented_Type.__name__=_D
_CD11HtPhyXmitIndFdbkASImplemented_Object=MibTableColumn
cD11HtPhyXmitIndFdbkASImplemented=_CD11HtPhyXmitIndFdbkASImplemented_Object((1,3,6,1,4,1,9,9,607,1,1,1,1,6),_CD11HtPhyXmitIndFdbkASImplemented_Type())
cD11HtPhyXmitIndFdbkASImplemented.setMaxAccess(_C)
if mibBuilder.loadTexts:cD11HtPhyXmitIndFdbkASImplemented.setStatus(_A)
class _CD11HtPhyExplCSIFdbkASImplemented_Type(TruthValue):defaultValue=2
_CD11HtPhyExplCSIFdbkASImplemented_Type.__name__=_D
_CD11HtPhyExplCSIFdbkASImplemented_Object=MibTableColumn
cD11HtPhyExplCSIFdbkASImplemented=_CD11HtPhyExplCSIFdbkASImplemented_Object((1,3,6,1,4,1,9,9,607,1,1,1,1,7),_CD11HtPhyExplCSIFdbkASImplemented_Type())
cD11HtPhyExplCSIFdbkASImplemented.setMaxAccess(_C)
if mibBuilder.loadTexts:cD11HtPhyExplCSIFdbkASImplemented.setStatus(_A)
class _CD11HtPhyXmitIndCompFdbkASImplemented_Type(TruthValue):defaultValue=2
_CD11HtPhyXmitIndCompFdbkASImplemented_Type.__name__=_D
_CD11HtPhyXmitIndCompFdbkASImplemented_Object=MibTableColumn
cD11HtPhyXmitIndCompFdbkASImplemented=_CD11HtPhyXmitIndCompFdbkASImplemented_Object((1,3,6,1,4,1,9,9,607,1,1,1,1,8),_CD11HtPhyXmitIndCompFdbkASImplemented_Type())
cD11HtPhyXmitIndCompFdbkASImplemented.setMaxAccess(_C)
if mibBuilder.loadTexts:cD11HtPhyXmitIndCompFdbkASImplemented.setStatus(_A)
class _CD11HtPhyRcvAntennaSelImplemented_Type(TruthValue):defaultValue=2
_CD11HtPhyRcvAntennaSelImplemented_Type.__name__=_D
_CD11HtPhyRcvAntennaSelImplemented_Object=MibTableColumn
cD11HtPhyRcvAntennaSelImplemented=_CD11HtPhyRcvAntennaSelImplemented_Object((1,3,6,1,4,1,9,9,607,1,1,1,1,9),_CD11HtPhyRcvAntennaSelImplemented_Type())
cD11HtPhyRcvAntennaSelImplemented.setMaxAccess(_C)
if mibBuilder.loadTexts:cD11HtPhyRcvAntennaSelImplemented.setStatus(_A)
class _CD11HtPhyXmitSoundPPDUImplemented_Type(TruthValue):defaultValue=2
_CD11HtPhyXmitSoundPPDUImplemented_Type.__name__=_D
_CD11HtPhyXmitSoundPPDUImplemented_Object=MibTableColumn
cD11HtPhyXmitSoundPPDUImplemented=_CD11HtPhyXmitSoundPPDUImplemented_Object((1,3,6,1,4,1,9,9,607,1,1,1,1,10),_CD11HtPhyXmitSoundPPDUImplemented_Type())
cD11HtPhyXmitSoundPPDUImplemented.setMaxAccess(_C)
if mibBuilder.loadTexts:cD11HtPhyXmitSoundPPDUImplemented.setStatus(_A)
_CD11HtPhyTable_Object=MibTable
cD11HtPhyTable=_CD11HtPhyTable_Object((1,3,6,1,4,1,9,9,607,1,1,2))
if mibBuilder.loadTexts:cD11HtPhyTable.setStatus(_A)
_CD11HtPhyEntry_Object=MibTableRow
cD11HtPhyEntry=_CD11HtPhyEntry_Object((1,3,6,1,4,1,9,9,607,1,1,2,1))
cD11HtPhyEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:cD11HtPhyEntry.setStatus(_A)
class _CD11HtPhyOperatingMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('legacy',1),('mixed',2),('greenField',3)))
_CD11HtPhyOperatingMode_Type.__name__=_E
_CD11HtPhyOperatingMode_Object=MibTableColumn
cD11HtPhyOperatingMode=_CD11HtPhyOperatingMode_Object((1,3,6,1,4,1,9,9,607,1,1,2,1,1),_CD11HtPhyOperatingMode_Type())
cD11HtPhyOperatingMode.setMaxAccess(_C)
if mibBuilder.loadTexts:cD11HtPhyOperatingMode.setStatus(_A)
class _CD11HtPhyOperModeFrequency_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('legacyMode',1),('htMode',2),('dupLegacyMode',3),('fortyMHzUpperMode',4),('fortyMHzLowerMode',5)))
_CD11HtPhyOperModeFrequency_Type.__name__=_E
_CD11HtPhyOperModeFrequency_Object=MibTableColumn
cD11HtPhyOperModeFrequency=_CD11HtPhyOperModeFrequency_Object((1,3,6,1,4,1,9,9,607,1,1,2,1,2),_CD11HtPhyOperModeFrequency_Type())
cD11HtPhyOperModeFrequency.setMaxAccess(_C)
if mibBuilder.loadTexts:cD11HtPhyOperModeFrequency.setStatus(_A)
class _CD11HtPhyOperBand_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('band24GHz',1),('band5GHz',2)))
_CD11HtPhyOperBand_Type.__name__=_E
_CD11HtPhyOperBand_Object=MibTableColumn
cD11HtPhyOperBand=_CD11HtPhyOperBand_Object((1,3,6,1,4,1,9,9,607,1,1,2,1,3),_CD11HtPhyOperBand_Type())
cD11HtPhyOperBand.setMaxAccess(_C)
if mibBuilder.loadTexts:cD11HtPhyOperBand.setStatus(_A)
class _CD11HtPhyFortyMHzOperationImplemented_Type(TruthValue):defaultValue=2
_CD11HtPhyFortyMHzOperationImplemented_Type.__name__=_D
_CD11HtPhyFortyMHzOperationImplemented_Object=MibTableColumn
cD11HtPhyFortyMHzOperationImplemented=_CD11HtPhyFortyMHzOperationImplemented_Object((1,3,6,1,4,1,9,9,607,1,1,2,1,4),_CD11HtPhyFortyMHzOperationImplemented_Type())
cD11HtPhyFortyMHzOperationImplemented.setMaxAccess(_C)
if mibBuilder.loadTexts:cD11HtPhyFortyMHzOperationImplemented.setStatus(_A)
class _CD11HtPhyFortyMHzOperationEnabled_Type(TruthValue):defaultValue=2
_CD11HtPhyFortyMHzOperationEnabled_Type.__name__=_D
_CD11HtPhyFortyMHzOperationEnabled_Object=MibTableColumn
cD11HtPhyFortyMHzOperationEnabled=_CD11HtPhyFortyMHzOperationEnabled_Object((1,3,6,1,4,1,9,9,607,1,1,2,1,5),_CD11HtPhyFortyMHzOperationEnabled_Type())
cD11HtPhyFortyMHzOperationEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:cD11HtPhyFortyMHzOperationEnabled.setStatus(_A)
_CD11HtPhyCurrentControlChannel_Type=Unsigned32
_CD11HtPhyCurrentControlChannel_Object=MibTableColumn
cD11HtPhyCurrentControlChannel=_CD11HtPhyCurrentControlChannel_Object((1,3,6,1,4,1,9,9,607,1,1,2,1,6),_CD11HtPhyCurrentControlChannel_Type())
cD11HtPhyCurrentControlChannel.setMaxAccess(_C)
if mibBuilder.loadTexts:cD11HtPhyCurrentControlChannel.setStatus(_A)
class _CD11HtPhyCurrentExtensionChannel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('noExtension',1),('extensionAbove',2),('extensionBelow',3)))
_CD11HtPhyCurrentExtensionChannel_Type.__name__=_E
_CD11HtPhyCurrentExtensionChannel_Object=MibTableColumn
cD11HtPhyCurrentExtensionChannel=_CD11HtPhyCurrentExtensionChannel_Object((1,3,6,1,4,1,9,9,607,1,1,2,1,7),_CD11HtPhyCurrentExtensionChannel_Type())
cD11HtPhyCurrentExtensionChannel.setMaxAccess(_F)
if mibBuilder.loadTexts:cD11HtPhyCurrentExtensionChannel.setStatus(_A)
class _CD11HtPhyExtChannelCCAImplemented_Type(TruthValue):defaultValue=2
_CD11HtPhyExtChannelCCAImplemented_Type.__name__=_D
_CD11HtPhyExtChannelCCAImplemented_Object=MibTableColumn
cD11HtPhyExtChannelCCAImplemented=_CD11HtPhyExtChannelCCAImplemented_Object((1,3,6,1,4,1,9,9,607,1,1,2,1,8),_CD11HtPhyExtChannelCCAImplemented_Type())
cD11HtPhyExtChannelCCAImplemented.setMaxAccess(_C)
if mibBuilder.loadTexts:cD11HtPhyExtChannelCCAImplemented.setStatus(_A)
class _CD11HtPhyNumberOfSpatialStreamsImplemented_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_CD11HtPhyNumberOfSpatialStreamsImplemented_Type.__name__=_E
_CD11HtPhyNumberOfSpatialStreamsImplemented_Object=MibTableColumn
cD11HtPhyNumberOfSpatialStreamsImplemented=_CD11HtPhyNumberOfSpatialStreamsImplemented_Object((1,3,6,1,4,1,9,9,607,1,1,2,1,9),_CD11HtPhyNumberOfSpatialStreamsImplemented_Type())
cD11HtPhyNumberOfSpatialStreamsImplemented.setMaxAccess(_C)
if mibBuilder.loadTexts:cD11HtPhyNumberOfSpatialStreamsImplemented.setStatus(_A)
class _CD11HtPhyNumberOfSpatialStreamsEnabled_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_CD11HtPhyNumberOfSpatialStreamsEnabled_Type.__name__=_E
_CD11HtPhyNumberOfSpatialStreamsEnabled_Object=MibTableColumn
cD11HtPhyNumberOfSpatialStreamsEnabled=_CD11HtPhyNumberOfSpatialStreamsEnabled_Object((1,3,6,1,4,1,9,9,607,1,1,2,1,10),_CD11HtPhyNumberOfSpatialStreamsEnabled_Type())
cD11HtPhyNumberOfSpatialStreamsEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:cD11HtPhyNumberOfSpatialStreamsEnabled.setStatus(_A)
class _CD11HtPhyGreenFieldImplemented_Type(TruthValue):defaultValue=2
_CD11HtPhyGreenFieldImplemented_Type.__name__=_D
_CD11HtPhyGreenFieldImplemented_Object=MibTableColumn
cD11HtPhyGreenFieldImplemented=_CD11HtPhyGreenFieldImplemented_Object((1,3,6,1,4,1,9,9,607,1,1,2,1,11),_CD11HtPhyGreenFieldImplemented_Type())
cD11HtPhyGreenFieldImplemented.setMaxAccess(_C)
if mibBuilder.loadTexts:cD11HtPhyGreenFieldImplemented.setStatus(_A)
class _CD11HtPhyGreenFieldEnabled_Type(TruthValue):defaultValue=2
_CD11HtPhyGreenFieldEnabled_Type.__name__=_D
_CD11HtPhyGreenFieldEnabled_Object=MibTableColumn
cD11HtPhyGreenFieldEnabled=_CD11HtPhyGreenFieldEnabled_Object((1,3,6,1,4,1,9,9,607,1,1,2,1,12),_CD11HtPhyGreenFieldEnabled_Type())
cD11HtPhyGreenFieldEnabled.setMaxAccess(_F)
if mibBuilder.loadTexts:cD11HtPhyGreenFieldEnabled.setStatus(_A)
class _CD11HtPhyShortGIInTwentyImplemented_Type(TruthValue):defaultValue=2
_CD11HtPhyShortGIInTwentyImplemented_Type.__name__=_D
_CD11HtPhyShortGIInTwentyImplemented_Object=MibTableColumn
cD11HtPhyShortGIInTwentyImplemented=_CD11HtPhyShortGIInTwentyImplemented_Object((1,3,6,1,4,1,9,9,607,1,1,2,1,13),_CD11HtPhyShortGIInTwentyImplemented_Type())
cD11HtPhyShortGIInTwentyImplemented.setMaxAccess(_C)
if mibBuilder.loadTexts:cD11HtPhyShortGIInTwentyImplemented.setStatus(_A)
class _CD11HtPhyShortGIInTwentyEnabled_Type(TruthValue):defaultValue=2
_CD11HtPhyShortGIInTwentyEnabled_Type.__name__=_D
_CD11HtPhyShortGIInTwentyEnabled_Object=MibTableColumn
cD11HtPhyShortGIInTwentyEnabled=_CD11HtPhyShortGIInTwentyEnabled_Object((1,3,6,1,4,1,9,9,607,1,1,2,1,14),_CD11HtPhyShortGIInTwentyEnabled_Type())
cD11HtPhyShortGIInTwentyEnabled.setMaxAccess(_F)
if mibBuilder.loadTexts:cD11HtPhyShortGIInTwentyEnabled.setStatus(_A)
class _CD11HtPhyShortGIInFortyImplemented_Type(TruthValue):defaultValue=2
_CD11HtPhyShortGIInFortyImplemented_Type.__name__=_D
_CD11HtPhyShortGIInFortyImplemented_Object=MibTableColumn
cD11HtPhyShortGIInFortyImplemented=_CD11HtPhyShortGIInFortyImplemented_Object((1,3,6,1,4,1,9,9,607,1,1,2,1,15),_CD11HtPhyShortGIInFortyImplemented_Type())
cD11HtPhyShortGIInFortyImplemented.setMaxAccess(_C)
if mibBuilder.loadTexts:cD11HtPhyShortGIInFortyImplemented.setStatus(_A)
class _CD11HtPhyShortGIInFortyEnabled_Type(TruthValue):defaultValue=2
_CD11HtPhyShortGIInFortyEnabled_Type.__name__=_D
_CD11HtPhyShortGIInFortyEnabled_Object=MibTableColumn
cD11HtPhyShortGIInFortyEnabled=_CD11HtPhyShortGIInFortyEnabled_Object((1,3,6,1,4,1,9,9,607,1,1,2,1,16),_CD11HtPhyShortGIInFortyEnabled_Type())
cD11HtPhyShortGIInFortyEnabled.setMaxAccess(_F)
if mibBuilder.loadTexts:cD11HtPhyShortGIInFortyEnabled.setStatus(_A)
class _CD11HtPhyAdvancedCodingImplemented_Type(TruthValue):defaultValue=2
_CD11HtPhyAdvancedCodingImplemented_Type.__name__=_D
_CD11HtPhyAdvancedCodingImplemented_Object=MibTableColumn
cD11HtPhyAdvancedCodingImplemented=_CD11HtPhyAdvancedCodingImplemented_Object((1,3,6,1,4,1,9,9,607,1,1,2,1,17),_CD11HtPhyAdvancedCodingImplemented_Type())
cD11HtPhyAdvancedCodingImplemented.setMaxAccess(_C)
if mibBuilder.loadTexts:cD11HtPhyAdvancedCodingImplemented.setStatus(_A)
class _CD11HtPhyAdvancedCodingEnabled_Type(TruthValue):defaultValue=2
_CD11HtPhyAdvancedCodingEnabled_Type.__name__=_D
_CD11HtPhyAdvancedCodingEnabled_Object=MibTableColumn
cD11HtPhyAdvancedCodingEnabled=_CD11HtPhyAdvancedCodingEnabled_Object((1,3,6,1,4,1,9,9,607,1,1,2,1,18),_CD11HtPhyAdvancedCodingEnabled_Type())
cD11HtPhyAdvancedCodingEnabled.setMaxAccess(_F)
if mibBuilder.loadTexts:cD11HtPhyAdvancedCodingEnabled.setStatus(_A)
class _CD11HtPhyTxSTBCImplemented_Type(TruthValue):defaultValue=2
_CD11HtPhyTxSTBCImplemented_Type.__name__=_D
_CD11HtPhyTxSTBCImplemented_Object=MibTableColumn
cD11HtPhyTxSTBCImplemented=_CD11HtPhyTxSTBCImplemented_Object((1,3,6,1,4,1,9,9,607,1,1,2,1,19),_CD11HtPhyTxSTBCImplemented_Type())
cD11HtPhyTxSTBCImplemented.setMaxAccess(_C)
if mibBuilder.loadTexts:cD11HtPhyTxSTBCImplemented.setStatus(_A)
class _CD11HtPhyTxSTBCEnabled_Type(TruthValue):defaultValue=2
_CD11HtPhyTxSTBCEnabled_Type.__name__=_D
_CD11HtPhyTxSTBCEnabled_Object=MibTableColumn
cD11HtPhyTxSTBCEnabled=_CD11HtPhyTxSTBCEnabled_Object((1,3,6,1,4,1,9,9,607,1,1,2,1,20),_CD11HtPhyTxSTBCEnabled_Type())
cD11HtPhyTxSTBCEnabled.setMaxAccess(_F)
if mibBuilder.loadTexts:cD11HtPhyTxSTBCEnabled.setStatus(_A)
class _CD11HtPhyRxSTBCImplemented_Type(TruthValue):defaultValue=2
_CD11HtPhyRxSTBCImplemented_Type.__name__=_D
_CD11HtPhyRxSTBCImplemented_Object=MibTableColumn
cD11HtPhyRxSTBCImplemented=_CD11HtPhyRxSTBCImplemented_Object((1,3,6,1,4,1,9,9,607,1,1,2,1,21),_CD11HtPhyRxSTBCImplemented_Type())
cD11HtPhyRxSTBCImplemented.setMaxAccess(_C)
if mibBuilder.loadTexts:cD11HtPhyRxSTBCImplemented.setStatus(_A)
class _CD11HtPhyRxSTBCEnabled_Type(TruthValue):defaultValue=2
_CD11HtPhyRxSTBCEnabled_Type.__name__=_D
_CD11HtPhyRxSTBCEnabled_Object=MibTableColumn
cD11HtPhyRxSTBCEnabled=_CD11HtPhyRxSTBCEnabled_Object((1,3,6,1,4,1,9,9,607,1,1,2,1,22),_CD11HtPhyRxSTBCEnabled_Type())
cD11HtPhyRxSTBCEnabled.setMaxAccess(_F)
if mibBuilder.loadTexts:cD11HtPhyRxSTBCEnabled.setStatus(_A)
class _CD11HtPhyBeamFormingImplemented_Type(TruthValue):defaultValue=2
_CD11HtPhyBeamFormingImplemented_Type.__name__=_D
_CD11HtPhyBeamFormingImplemented_Object=MibTableColumn
cD11HtPhyBeamFormingImplemented=_CD11HtPhyBeamFormingImplemented_Object((1,3,6,1,4,1,9,9,607,1,1,2,1,23),_CD11HtPhyBeamFormingImplemented_Type())
cD11HtPhyBeamFormingImplemented.setMaxAccess(_C)
if mibBuilder.loadTexts:cD11HtPhyBeamFormingImplemented.setStatus(_A)
class _CD11HtPhyBeamFormingEnabled_Type(TruthValue):defaultValue=2
_CD11HtPhyBeamFormingEnabled_Type.__name__=_D
_CD11HtPhyBeamFormingEnabled_Object=MibTableColumn
cD11HtPhyBeamFormingEnabled=_CD11HtPhyBeamFormingEnabled_Object((1,3,6,1,4,1,9,9,607,1,1,2,1,24),_CD11HtPhyBeamFormingEnabled_Type())
cD11HtPhyBeamFormingEnabled.setMaxAccess(_F)
if mibBuilder.loadTexts:cD11HtPhyBeamFormingEnabled.setStatus(_A)
_CD11HtPhySupportedMCSTable_Object=MibTable
cD11HtPhySupportedMCSTable=_CD11HtPhySupportedMCSTable_Object((1,3,6,1,4,1,9,9,607,1,1,3))
if mibBuilder.loadTexts:cD11HtPhySupportedMCSTable.setStatus(_A)
_CD11HtPhySupportedMCSEntry_Object=MibTableRow
cD11HtPhySupportedMCSEntry=_CD11HtPhySupportedMCSEntry_Object((1,3,6,1,4,1,9,9,607,1,1,3,1))
cD11HtPhySupportedMCSEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:cD11HtPhySupportedMCSEntry.setStatus(_A)
class _CD11HtPhySupportedMCSTxValue_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,127))
_CD11HtPhySupportedMCSTxValue_Type.__name__=_I
_CD11HtPhySupportedMCSTxValue_Object=MibTableColumn
cD11HtPhySupportedMCSTxValue=_CD11HtPhySupportedMCSTxValue_Object((1,3,6,1,4,1,9,9,607,1,1,3,1,1),_CD11HtPhySupportedMCSTxValue_Type())
cD11HtPhySupportedMCSTxValue.setMaxAccess(_C)
if mibBuilder.loadTexts:cD11HtPhySupportedMCSTxValue.setStatus(_A)
class _CD11HtPhySupportedMCSRxValue_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,127))
_CD11HtPhySupportedMCSRxValue_Type.__name__=_I
_CD11HtPhySupportedMCSRxValue_Object=MibTableColumn
cD11HtPhySupportedMCSRxValue=_CD11HtPhySupportedMCSRxValue_Object((1,3,6,1,4,1,9,9,607,1,1,3,1,2),_CD11HtPhySupportedMCSRxValue_Type())
cD11HtPhySupportedMCSRxValue.setMaxAccess(_C)
if mibBuilder.loadTexts:cD11HtPhySupportedMCSRxValue.setStatus(_A)
_CD11HtPhyTxBFConfigTable_Object=MibTable
cD11HtPhyTxBFConfigTable=_CD11HtPhyTxBFConfigTable_Object((1,3,6,1,4,1,9,9,607,1,1,4))
if mibBuilder.loadTexts:cD11HtPhyTxBFConfigTable.setStatus(_A)
_CD11HtPhyTxBFConfigEntry_Object=MibTableRow
cD11HtPhyTxBFConfigEntry=_CD11HtPhyTxBFConfigEntry_Object((1,3,6,1,4,1,9,9,607,1,1,4,1))
cD11HtPhyTxBFConfigEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:cD11HtPhyTxBFConfigEntry.setStatus(_A)
class _CD11HtPhyRxStaggerSoundImplemented_Type(TruthValue):defaultValue=2
_CD11HtPhyRxStaggerSoundImplemented_Type.__name__=_D
_CD11HtPhyRxStaggerSoundImplemented_Object=MibTableColumn
cD11HtPhyRxStaggerSoundImplemented=_CD11HtPhyRxStaggerSoundImplemented_Object((1,3,6,1,4,1,9,9,607,1,1,4,1,1),_CD11HtPhyRxStaggerSoundImplemented_Type())
cD11HtPhyRxStaggerSoundImplemented.setMaxAccess(_C)
if mibBuilder.loadTexts:cD11HtPhyRxStaggerSoundImplemented.setStatus(_A)
class _CD11HtPhyTxStaggerSoundImplemented_Type(TruthValue):defaultValue=2
_CD11HtPhyTxStaggerSoundImplemented_Type.__name__=_D
_CD11HtPhyTxStaggerSoundImplemented_Object=MibTableColumn
cD11HtPhyTxStaggerSoundImplemented=_CD11HtPhyTxStaggerSoundImplemented_Object((1,3,6,1,4,1,9,9,607,1,1,4,1,2),_CD11HtPhyTxStaggerSoundImplemented_Type())
cD11HtPhyTxStaggerSoundImplemented.setMaxAccess(_C)
if mibBuilder.loadTexts:cD11HtPhyTxStaggerSoundImplemented.setStatus(_A)
class _CD11HtPhyRxZLFImplemented_Type(TruthValue):defaultValue=2
_CD11HtPhyRxZLFImplemented_Type.__name__=_D
_CD11HtPhyRxZLFImplemented_Object=MibTableColumn
cD11HtPhyRxZLFImplemented=_CD11HtPhyRxZLFImplemented_Object((1,3,6,1,4,1,9,9,607,1,1,4,1,3),_CD11HtPhyRxZLFImplemented_Type())
cD11HtPhyRxZLFImplemented.setMaxAccess(_C)
if mibBuilder.loadTexts:cD11HtPhyRxZLFImplemented.setStatus(_A)
class _CD11HtPhyTxZLFImplemented_Type(TruthValue):defaultValue=2
_CD11HtPhyTxZLFImplemented_Type.__name__=_D
_CD11HtPhyTxZLFImplemented_Object=MibTableColumn
cD11HtPhyTxZLFImplemented=_CD11HtPhyTxZLFImplemented_Object((1,3,6,1,4,1,9,9,607,1,1,4,1,4),_CD11HtPhyTxZLFImplemented_Type())
cD11HtPhyTxZLFImplemented.setMaxAccess(_C)
if mibBuilder.loadTexts:cD11HtPhyTxZLFImplemented.setStatus(_A)
class _CD11HtPhyImplicitTxBFImplemented_Type(TruthValue):defaultValue=2
_CD11HtPhyImplicitTxBFImplemented_Type.__name__=_D
_CD11HtPhyImplicitTxBFImplemented_Object=MibTableColumn
cD11HtPhyImplicitTxBFImplemented=_CD11HtPhyImplicitTxBFImplemented_Object((1,3,6,1,4,1,9,9,607,1,1,4,1,5),_CD11HtPhyImplicitTxBFImplemented_Type())
cD11HtPhyImplicitTxBFImplemented.setMaxAccess(_C)
if mibBuilder.loadTexts:cD11HtPhyImplicitTxBFImplemented.setStatus(_A)
class _CD11HtPhyCalibrationImplemented_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('inCapable',1),('unableToInitiate',2),('ableToInitiate',3),('fullyCapable',4)))
_CD11HtPhyCalibrationImplemented_Type.__name__=_E
_CD11HtPhyCalibrationImplemented_Object=MibTableColumn
cD11HtPhyCalibrationImplemented=_CD11HtPhyCalibrationImplemented_Object((1,3,6,1,4,1,9,9,607,1,1,4,1,6),_CD11HtPhyCalibrationImplemented_Type())
cD11HtPhyCalibrationImplemented.setMaxAccess(_C)
if mibBuilder.loadTexts:cD11HtPhyCalibrationImplemented.setStatus(_A)
class _CD11HtPhyExplCSITxBFImplemented_Type(TruthValue):defaultValue=2
_CD11HtPhyExplCSITxBFImplemented_Type.__name__=_D
_CD11HtPhyExplCSITxBFImplemented_Object=MibTableColumn
cD11HtPhyExplCSITxBFImplemented=_CD11HtPhyExplCSITxBFImplemented_Object((1,3,6,1,4,1,9,9,607,1,1,4,1,7),_CD11HtPhyExplCSITxBFImplemented_Type())
cD11HtPhyExplCSITxBFImplemented.setMaxAccess(_C)
if mibBuilder.loadTexts:cD11HtPhyExplCSITxBFImplemented.setStatus(_A)
class _CD11HtPhyExplUncompSteerMatrixImplemented_Type(TruthValue):defaultValue=2
_CD11HtPhyExplUncompSteerMatrixImplemented_Type.__name__=_D
_CD11HtPhyExplUncompSteerMatrixImplemented_Object=MibTableColumn
cD11HtPhyExplUncompSteerMatrixImplemented=_CD11HtPhyExplUncompSteerMatrixImplemented_Object((1,3,6,1,4,1,9,9,607,1,1,4,1,8),_CD11HtPhyExplUncompSteerMatrixImplemented_Type())
cD11HtPhyExplUncompSteerMatrixImplemented.setMaxAccess(_C)
if mibBuilder.loadTexts:cD11HtPhyExplUncompSteerMatrixImplemented.setStatus(_A)
_CD11HtPhyExplBFCSIFdbkImplemented_Type=CD11HtPhyBeamformFeedback
_CD11HtPhyExplBFCSIFdbkImplemented_Object=MibTableColumn
cD11HtPhyExplBFCSIFdbkImplemented=_CD11HtPhyExplBFCSIFdbkImplemented_Object((1,3,6,1,4,1,9,9,607,1,1,4,1,9),_CD11HtPhyExplBFCSIFdbkImplemented_Type())
cD11HtPhyExplBFCSIFdbkImplemented.setMaxAccess(_C)
if mibBuilder.loadTexts:cD11HtPhyExplBFCSIFdbkImplemented.setStatus(_A)
_CD11HtPhyExplUncompSteerMatrixFdbkImplemented_Type=CD11HtPhyBeamformFeedback
_CD11HtPhyExplUncompSteerMatrixFdbkImplemented_Object=MibTableColumn
cD11HtPhyExplUncompSteerMatrixFdbkImplemented=_CD11HtPhyExplUncompSteerMatrixFdbkImplemented_Object((1,3,6,1,4,1,9,9,607,1,1,4,1,10),_CD11HtPhyExplUncompSteerMatrixFdbkImplemented_Type())
cD11HtPhyExplUncompSteerMatrixFdbkImplemented.setMaxAccess(_C)
if mibBuilder.loadTexts:cD11HtPhyExplUncompSteerMatrixFdbkImplemented.setStatus(_A)
_CD11HtPhyExplCompSteerMatrixFdbkImplemented_Type=CD11HtPhyBeamformFeedback
_CD11HtPhyExplCompSteerMatrixFdbkImplemented_Object=MibTableColumn
cD11HtPhyExplCompSteerMatrixFdbkImplemented=_CD11HtPhyExplCompSteerMatrixFdbkImplemented_Object((1,3,6,1,4,1,9,9,607,1,1,4,1,11),_CD11HtPhyExplCompSteerMatrixFdbkImplemented_Type())
cD11HtPhyExplCompSteerMatrixFdbkImplemented.setMaxAccess(_C)
if mibBuilder.loadTexts:cD11HtPhyExplCompSteerMatrixFdbkImplemented.setStatus(_A)
class _CD11HtPhyNumberBeamFormingCSISupportAntenna_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_CD11HtPhyNumberBeamFormingCSISupportAntenna_Type.__name__=_E
_CD11HtPhyNumberBeamFormingCSISupportAntenna_Object=MibTableColumn
cD11HtPhyNumberBeamFormingCSISupportAntenna=_CD11HtPhyNumberBeamFormingCSISupportAntenna_Object((1,3,6,1,4,1,9,9,607,1,1,4,1,12),_CD11HtPhyNumberBeamFormingCSISupportAntenna_Type())
cD11HtPhyNumberBeamFormingCSISupportAntenna.setMaxAccess(_C)
if mibBuilder.loadTexts:cD11HtPhyNumberBeamFormingCSISupportAntenna.setStatus(_A)
class _CD11HtPhyNumberUncompSteerMatrixSupportAntenna_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_CD11HtPhyNumberUncompSteerMatrixSupportAntenna_Type.__name__=_E
_CD11HtPhyNumberUncompSteerMatrixSupportAntenna_Object=MibTableColumn
cD11HtPhyNumberUncompSteerMatrixSupportAntenna=_CD11HtPhyNumberUncompSteerMatrixSupportAntenna_Object((1,3,6,1,4,1,9,9,607,1,1,4,1,13),_CD11HtPhyNumberUncompSteerMatrixSupportAntenna_Type())
cD11HtPhyNumberUncompSteerMatrixSupportAntenna.setMaxAccess(_C)
if mibBuilder.loadTexts:cD11HtPhyNumberUncompSteerMatrixSupportAntenna.setStatus(_A)
class _CD11HtPhyNumberCompSteerMatrixSupportAntenna_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_CD11HtPhyNumberCompSteerMatrixSupportAntenna_Type.__name__=_E
_CD11HtPhyNumberCompSteerMatrixSupportAntenna_Object=MibTableColumn
cD11HtPhyNumberCompSteerMatrixSupportAntenna=_CD11HtPhyNumberCompSteerMatrixSupportAntenna_Object((1,3,6,1,4,1,9,9,607,1,1,4,1,14),_CD11HtPhyNumberCompSteerMatrixSupportAntenna_Type())
cD11HtPhyNumberCompSteerMatrixSupportAntenna.setMaxAccess(_C)
if mibBuilder.loadTexts:cD11HtPhyNumberCompSteerMatrixSupportAntenna.setStatus(_A)
_CD11HtPhyEnhPowerTable_Object=MibTable
cD11HtPhyEnhPowerTable=_CD11HtPhyEnhPowerTable_Object((1,3,6,1,4,1,9,9,607,1,1,5))
if mibBuilder.loadTexts:cD11HtPhyEnhPowerTable.setStatus(_A)
_CD11HtPhyEnhPowerEntry_Object=MibTableRow
cD11HtPhyEnhPowerEntry=_CD11HtPhyEnhPowerEntry_Object((1,3,6,1,4,1,9,9,607,1,1,5,1))
cD11HtPhyEnhPowerEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:cD11HtPhyEnhPowerEntry.setStatus(_A)
class _CD11HtPhyEnhPowerLevel20MHz_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_CD11HtPhyEnhPowerLevel20MHz_Type.__name__=_J
_CD11HtPhyEnhPowerLevel20MHz_Object=MibTableColumn
cD11HtPhyEnhPowerLevel20MHz=_CD11HtPhyEnhPowerLevel20MHz_Object((1,3,6,1,4,1,9,9,607,1,1,5,1,1),_CD11HtPhyEnhPowerLevel20MHz_Type())
cD11HtPhyEnhPowerLevel20MHz.setMaxAccess(_C)
if mibBuilder.loadTexts:cD11HtPhyEnhPowerLevel20MHz.setStatus(_A)
class _CD11HtPhyEnhPowerLevel40MHz_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_CD11HtPhyEnhPowerLevel40MHz_Type.__name__=_J
_CD11HtPhyEnhPowerLevel40MHz_Object=MibTableColumn
cD11HtPhyEnhPowerLevel40MHz=_CD11HtPhyEnhPowerLevel40MHz_Object((1,3,6,1,4,1,9,9,607,1,1,5,1,2),_CD11HtPhyEnhPowerLevel40MHz_Type())
cD11HtPhyEnhPowerLevel40MHz.setMaxAccess(_C)
if mibBuilder.loadTexts:cD11HtPhyEnhPowerLevel40MHz.setStatus(_A)
_CiscoDot11HtPhyMIBConform_ObjectIdentity=ObjectIdentity
ciscoDot11HtPhyMIBConform=_CiscoDot11HtPhyMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,607,2))
_CiscoDot11HtPhyMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoDot11HtPhyMIBCompliances=_CiscoDot11HtPhyMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,607,2,1))
_CiscoDot11HtPhyMIBGroups_ObjectIdentity=ObjectIdentity
ciscoDot11HtPhyMIBGroups=_CiscoDot11HtPhyMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,607,2,2))
ciscoDot11HtPhyAntennaGroup=ObjectGroup((1,3,6,1,4,1,9,9,607,2,2,1))
ciscoDot11HtPhyAntennaGroup.setObjects(*((_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:ciscoDot11HtPhyAntennaGroup.setStatus(_A)
ciscoDot11HtPhyConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,607,2,2,2))
ciscoDot11HtPhyConfigGroup.setObjects(*((_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o)))
if mibBuilder.loadTexts:ciscoDot11HtPhyConfigGroup.setStatus(_A)
ciscoDot11HtPhyMcsGroup=ObjectGroup((1,3,6,1,4,1,9,9,607,2,2,3))
ciscoDot11HtPhyMcsGroup.setObjects(*((_B,_p),(_B,_q)))
if mibBuilder.loadTexts:ciscoDot11HtPhyMcsGroup.setStatus(_A)
ciscoDot11HtPhyTxBfGroup=ObjectGroup((1,3,6,1,4,1,9,9,607,2,2,4))
ciscoDot11HtPhyTxBfGroup.setObjects(*((_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4)))
if mibBuilder.loadTexts:ciscoDot11HtPhyTxBfGroup.setStatus(_A)
ciscoDot11HtPhyEnhPowerLevelsGroup=ObjectGroup((1,3,6,1,4,1,9,9,607,2,2,5))
ciscoDot11HtPhyEnhPowerLevelsGroup.setObjects(*((_B,_A5),(_B,_A6)))
if mibBuilder.loadTexts:ciscoDot11HtPhyEnhPowerLevelsGroup.setStatus(_A)
ciscoDot11HtMacCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,607,2,1,1))
ciscoDot11HtMacCompliance.setObjects(*((_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB)))
if mibBuilder.loadTexts:ciscoDot11HtMacCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'CD11HtPhyBeamformFeedback':CD11HtPhyBeamformFeedback,'ciscoDot11HtPhyMIB':ciscoDot11HtPhyMIB,'ciscoDot11HtPhyMIBNotifs':ciscoDot11HtPhyMIBNotifs,'ciscoDot11HtPhyMIBObjects':ciscoDot11HtPhyMIBObjects,'cD11HtPhy':cD11HtPhy,'cD11HtPhyAntennaTable':cD11HtPhyAntennaTable,'cD11HtPhyAntennaEntry':cD11HtPhyAntennaEntry,_K:cD11HtPhyAntennaSelectionImplemented,_L:cD11HtPhyXmitExpCSIFdbkASImplemented,_M:cD11HtPhyXmitIndFdbkASImplemented,_N:cD11HtPhyExplCSIFdbkASImplemented,_O:cD11HtPhyXmitIndCompFdbkASImplemented,_P:cD11HtPhyRcvAntennaSelImplemented,_Q:cD11HtPhyXmitSoundPPDUImplemented,'cD11HtPhyTable':cD11HtPhyTable,'cD11HtPhyEntry':cD11HtPhyEntry,_R:cD11HtPhyOperatingMode,_S:cD11HtPhyOperModeFrequency,_T:cD11HtPhyOperBand,_U:cD11HtPhyFortyMHzOperationImplemented,_V:cD11HtPhyFortyMHzOperationEnabled,_W:cD11HtPhyCurrentControlChannel,_X:cD11HtPhyCurrentExtensionChannel,_Y:cD11HtPhyExtChannelCCAImplemented,_Z:cD11HtPhyNumberOfSpatialStreamsImplemented,_a:cD11HtPhyNumberOfSpatialStreamsEnabled,_b:cD11HtPhyGreenFieldImplemented,_c:cD11HtPhyGreenFieldEnabled,_d:cD11HtPhyShortGIInTwentyImplemented,_e:cD11HtPhyShortGIInTwentyEnabled,_f:cD11HtPhyShortGIInFortyImplemented,_g:cD11HtPhyShortGIInFortyEnabled,_h:cD11HtPhyAdvancedCodingImplemented,_i:cD11HtPhyAdvancedCodingEnabled,_j:cD11HtPhyTxSTBCImplemented,_k:cD11HtPhyTxSTBCEnabled,_l:cD11HtPhyRxSTBCImplemented,_m:cD11HtPhyRxSTBCEnabled,_n:cD11HtPhyBeamFormingImplemented,_o:cD11HtPhyBeamFormingEnabled,'cD11HtPhySupportedMCSTable':cD11HtPhySupportedMCSTable,'cD11HtPhySupportedMCSEntry':cD11HtPhySupportedMCSEntry,_p:cD11HtPhySupportedMCSTxValue,_q:cD11HtPhySupportedMCSRxValue,'cD11HtPhyTxBFConfigTable':cD11HtPhyTxBFConfigTable,'cD11HtPhyTxBFConfigEntry':cD11HtPhyTxBFConfigEntry,_r:cD11HtPhyRxStaggerSoundImplemented,_s:cD11HtPhyTxStaggerSoundImplemented,_t:cD11HtPhyRxZLFImplemented,_u:cD11HtPhyTxZLFImplemented,_v:cD11HtPhyImplicitTxBFImplemented,_w:cD11HtPhyCalibrationImplemented,_x:cD11HtPhyExplCSITxBFImplemented,_y:cD11HtPhyExplUncompSteerMatrixImplemented,_z:cD11HtPhyExplBFCSIFdbkImplemented,_A0:cD11HtPhyExplUncompSteerMatrixFdbkImplemented,_A1:cD11HtPhyExplCompSteerMatrixFdbkImplemented,_A2:cD11HtPhyNumberBeamFormingCSISupportAntenna,_A3:cD11HtPhyNumberUncompSteerMatrixSupportAntenna,_A4:cD11HtPhyNumberCompSteerMatrixSupportAntenna,'cD11HtPhyEnhPowerTable':cD11HtPhyEnhPowerTable,'cD11HtPhyEnhPowerEntry':cD11HtPhyEnhPowerEntry,_A5:cD11HtPhyEnhPowerLevel20MHz,_A6:cD11HtPhyEnhPowerLevel40MHz,'ciscoDot11HtPhyMIBConform':ciscoDot11HtPhyMIBConform,'ciscoDot11HtPhyMIBCompliances':ciscoDot11HtPhyMIBCompliances,'ciscoDot11HtMacCompliance':ciscoDot11HtMacCompliance,'ciscoDot11HtPhyMIBGroups':ciscoDot11HtPhyMIBGroups,_A7:ciscoDot11HtPhyAntennaGroup,_A8:ciscoDot11HtPhyConfigGroup,_A9:ciscoDot11HtPhyMcsGroup,_AA:ciscoDot11HtPhyTxBfGroup,_AB:ciscoDot11HtPhyEnhPowerLevelsGroup})