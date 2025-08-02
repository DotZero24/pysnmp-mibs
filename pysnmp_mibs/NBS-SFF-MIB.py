_Q='nbsSffMsxPhysicalIfIndex'
_P='supported'
_O='reserved'
_N='OctetString'
_M='on'
_L='off'
_K='nbsSffMsaPhysicalIfIndex'
_J='NBS-SFF-MIB'
_I='notSupported'
_H='implemented'
_G='notImplemented'
_F='yes'
_E='no'
_D='DisplayString'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_N,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
NbsCmmcChannelBand,=mibBuilder.importSymbols('NBS-CMMCENUM-MIB','NbsCmmcChannelBand')
NbsTcMHz,nbs=mibBuilder.importSymbols('NBS-MIB','NbsTcMHz','nbs')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention')
nbsSffMib=ModuleIdentity((1,3,6,1,4,1,629,204))
_NbsSffObjects_ObjectIdentity=ObjectIdentity
nbsSffObjects=_NbsSffObjects_ObjectIdentity((1,3,6,1,4,1,629,204,1))
if mibBuilder.loadTexts:nbsSffObjects.setStatus(_A)
_NbsSffMsaGrp_ObjectIdentity=ObjectIdentity
nbsSffMsaGrp=_NbsSffMsaGrp_ObjectIdentity((1,3,6,1,4,1,629,204,1,1))
if mibBuilder.loadTexts:nbsSffMsaGrp.setStatus(_A)
_NbsSffMsaTable_Object=MibTable
nbsSffMsaTable=_NbsSffMsaTable_Object((1,3,6,1,4,1,629,204,1,1,1))
if mibBuilder.loadTexts:nbsSffMsaTable.setStatus(_A)
_NbsSffMsaEntry_Object=MibTableRow
nbsSffMsaEntry=_NbsSffMsaEntry_Object((1,3,6,1,4,1,629,204,1,1,1,1))
nbsSffMsaEntry.setIndexNames((0,_J,_K))
if mibBuilder.loadTexts:nbsSffMsaEntry.setStatus(_A)
_NbsSffMsaPhysicalIfIndex_Type=InterfaceIndex
_NbsSffMsaPhysicalIfIndex_Object=MibTableColumn
nbsSffMsaPhysicalIfIndex=_NbsSffMsaPhysicalIfIndex_Object((1,3,6,1,4,1,629,204,1,1,1,1,1),_NbsSffMsaPhysicalIfIndex_Type())
nbsSffMsaPhysicalIfIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:nbsSffMsaPhysicalIfIndex.setStatus(_A)
class _NbsSffMsaIdentifier_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,130)));namedValues=NamedValues(*(('unknown',1),('gbic',2),('moduleSolderedToBoard',3),('sfpTransceiver',4),('threeHundredPinXBI',5),('xenpak',6),('xfp',7),('xff',8),('xfpe',9),('xpak',10),('x2',11),('dwdm',12),('qsfp',13),('qsfpPlus',14),('cfp',15),('cxp',16),('mrvCxp',130)))
_NbsSffMsaIdentifier_Type.__name__=_C
_NbsSffMsaIdentifier_Object=MibTableColumn
nbsSffMsaIdentifier=_NbsSffMsaIdentifier_Object((1,3,6,1,4,1,629,204,1,1,1,1,2),_NbsSffMsaIdentifier_Type())
nbsSffMsaIdentifier.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSffMsaIdentifier.setStatus(_A)
_NbsSffMsaExtIdentifier_Type=Integer32
_NbsSffMsaExtIdentifier_Object=MibTableColumn
nbsSffMsaExtIdentifier=_NbsSffMsaExtIdentifier_Object((1,3,6,1,4,1,629,204,1,1,1,1,3),_NbsSffMsaExtIdentifier_Type())
nbsSffMsaExtIdentifier.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSffMsaExtIdentifier.setStatus(_A)
_NbsSffMsaOpticalConnector_Type=Integer32
_NbsSffMsaOpticalConnector_Object=MibTableColumn
nbsSffMsaOpticalConnector=_NbsSffMsaOpticalConnector_Object((1,3,6,1,4,1,629,204,1,1,1,1,4),_NbsSffMsaOpticalConnector_Type())
nbsSffMsaOpticalConnector.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSffMsaOpticalConnector.setStatus(_A)
class _NbsSffMsaTransceiverCodes_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,11))
_NbsSffMsaTransceiverCodes_Type.__name__=_N
_NbsSffMsaTransceiverCodes_Object=MibTableColumn
nbsSffMsaTransceiverCodes=_NbsSffMsaTransceiverCodes_Object((1,3,6,1,4,1,629,204,1,1,1,1,5),_NbsSffMsaTransceiverCodes_Type())
nbsSffMsaTransceiverCodes.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSffMsaTransceiverCodes.setStatus(_A)
class _NbsSffMsaSerialEncoding_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_I,1),('lineCode8To10',2),('lineCode4To5',3),('nrz',4),('manchester',5),('sonetScrambled',6),('unspecified',7)))
_NbsSffMsaSerialEncoding_Type.__name__=_C
_NbsSffMsaSerialEncoding_Object=MibTableColumn
nbsSffMsaSerialEncoding=_NbsSffMsaSerialEncoding_Object((1,3,6,1,4,1,629,204,1,1,1,1,6),_NbsSffMsaSerialEncoding_Type())
nbsSffMsaSerialEncoding.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSffMsaSerialEncoding.setStatus(_A)
_NbsSffMsaNominalBitRate_Type=Integer32
_NbsSffMsaNominalBitRate_Object=MibTableColumn
nbsSffMsaNominalBitRate=_NbsSffMsaNominalBitRate_Object((1,3,6,1,4,1,629,204,1,1,1,1,7),_NbsSffMsaNominalBitRate_Type())
nbsSffMsaNominalBitRate.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSffMsaNominalBitRate.setStatus(_A)
_NbsSffMsaLinkLengthSmfKm_Type=Integer32
_NbsSffMsaLinkLengthSmfKm_Object=MibTableColumn
nbsSffMsaLinkLengthSmfKm=_NbsSffMsaLinkLengthSmfKm_Object((1,3,6,1,4,1,629,204,1,1,1,1,8),_NbsSffMsaLinkLengthSmfKm_Type())
nbsSffMsaLinkLengthSmfKm.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSffMsaLinkLengthSmfKm.setStatus(_A)
_NbsSffMsaLinkLengthSmf100m_Type=Integer32
_NbsSffMsaLinkLengthSmf100m_Object=MibTableColumn
nbsSffMsaLinkLengthSmf100m=_NbsSffMsaLinkLengthSmf100m_Object((1,3,6,1,4,1,629,204,1,1,1,1,9),_NbsSffMsaLinkLengthSmf100m_Type())
nbsSffMsaLinkLengthSmf100m.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSffMsaLinkLengthSmf100m.setStatus(_A)
_NbsSffMsaLinkLengthMmf10m_Type=Integer32
_NbsSffMsaLinkLengthMmf10m_Object=MibTableColumn
nbsSffMsaLinkLengthMmf10m=_NbsSffMsaLinkLengthMmf10m_Object((1,3,6,1,4,1,629,204,1,1,1,1,10),_NbsSffMsaLinkLengthMmf10m_Type())
nbsSffMsaLinkLengthMmf10m.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSffMsaLinkLengthMmf10m.setStatus(_A)
_NbsSffMsaLinkLength625Mmf10m_Type=Integer32
_NbsSffMsaLinkLength625Mmf10m_Object=MibTableColumn
nbsSffMsaLinkLength625Mmf10m=_NbsSffMsaLinkLength625Mmf10m_Object((1,3,6,1,4,1,629,204,1,1,1,1,11),_NbsSffMsaLinkLength625Mmf10m_Type())
nbsSffMsaLinkLength625Mmf10m.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSffMsaLinkLength625Mmf10m.setStatus(_A)
_NbsSffMsaCopperLinkLength_Type=Integer32
_NbsSffMsaCopperLinkLength_Object=MibTableColumn
nbsSffMsaCopperLinkLength=_NbsSffMsaCopperLinkLength_Object((1,3,6,1,4,1,629,204,1,1,1,1,12),_NbsSffMsaCopperLinkLength_Type())
nbsSffMsaCopperLinkLength.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSffMsaCopperLinkLength.setStatus(_A)
class _NbsSffMsaVendorName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_NbsSffMsaVendorName_Type.__name__=_D
_NbsSffMsaVendorName_Object=MibTableColumn
nbsSffMsaVendorName=_NbsSffMsaVendorName_Object((1,3,6,1,4,1,629,204,1,1,1,1,13),_NbsSffMsaVendorName_Type())
nbsSffMsaVendorName.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSffMsaVendorName.setStatus(_A)
class _NbsSffMsaVendorOUI_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,3));fixedLength=3
_NbsSffMsaVendorOUI_Type.__name__=_N
_NbsSffMsaVendorOUI_Object=MibTableColumn
nbsSffMsaVendorOUI=_NbsSffMsaVendorOUI_Object((1,3,6,1,4,1,629,204,1,1,1,1,14),_NbsSffMsaVendorOUI_Type())
nbsSffMsaVendorOUI.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSffMsaVendorOUI.setStatus(_A)
class _NbsSffMsaVendorPartNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_NbsSffMsaVendorPartNumber_Type.__name__=_D
_NbsSffMsaVendorPartNumber_Object=MibTableColumn
nbsSffMsaVendorPartNumber=_NbsSffMsaVendorPartNumber_Object((1,3,6,1,4,1,629,204,1,1,1,1,15),_NbsSffMsaVendorPartNumber_Type())
nbsSffMsaVendorPartNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSffMsaVendorPartNumber.setStatus(_A)
class _NbsSffMsaVendorRevision_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,4))
_NbsSffMsaVendorRevision_Type.__name__=_D
_NbsSffMsaVendorRevision_Object=MibTableColumn
nbsSffMsaVendorRevision=_NbsSffMsaVendorRevision_Object((1,3,6,1,4,1,629,204,1,1,1,1,16),_NbsSffMsaVendorRevision_Type())
nbsSffMsaVendorRevision.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSffMsaVendorRevision.setStatus(_A)
class _NbsSffMsaBaseChecksumMatch_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_NbsSffMsaBaseChecksumMatch_Type.__name__=_C
_NbsSffMsaBaseChecksumMatch_Object=MibTableColumn
nbsSffMsaBaseChecksumMatch=_NbsSffMsaBaseChecksumMatch_Object((1,3,6,1,4,1,629,204,1,1,1,1,17),_NbsSffMsaBaseChecksumMatch_Type())
nbsSffMsaBaseChecksumMatch.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSffMsaBaseChecksumMatch.setStatus(_A)
_NbsSffMsaLossOfSignalImplemented_Type=Integer32
_NbsSffMsaLossOfSignalImplemented_Object=MibTableColumn
nbsSffMsaLossOfSignalImplemented=_NbsSffMsaLossOfSignalImplemented_Object((1,3,6,1,4,1,629,204,1,1,1,1,18),_NbsSffMsaLossOfSignalImplemented_Type())
nbsSffMsaLossOfSignalImplemented.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSffMsaLossOfSignalImplemented.setStatus(_A)
_NbsSffMsaLossOfSignalInverted_Type=Integer32
_NbsSffMsaLossOfSignalInverted_Object=MibTableColumn
nbsSffMsaLossOfSignalInverted=_NbsSffMsaLossOfSignalInverted_Object((1,3,6,1,4,1,629,204,1,1,1,1,19),_NbsSffMsaLossOfSignalInverted_Type())
nbsSffMsaLossOfSignalInverted.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSffMsaLossOfSignalInverted.setStatus(_A)
class _NbsSffMsaTxFault_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_NbsSffMsaTxFault_Type.__name__=_C
_NbsSffMsaTxFault_Object=MibTableColumn
nbsSffMsaTxFault=_NbsSffMsaTxFault_Object((1,3,6,1,4,1,629,204,1,1,1,1,20),_NbsSffMsaTxFault_Type())
nbsSffMsaTxFault.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSffMsaTxFault.setStatus(_A)
_NbsSffMsaTxDisable_Type=Integer32
_NbsSffMsaTxDisable_Object=MibTableColumn
nbsSffMsaTxDisable=_NbsSffMsaTxDisable_Object((1,3,6,1,4,1,629,204,1,1,1,1,21),_NbsSffMsaTxDisable_Type())
nbsSffMsaTxDisable.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSffMsaTxDisable.setStatus(_A)
class _NbsSffMsaRateSelectImplemented_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_NbsSffMsaRateSelectImplemented_Type.__name__=_C
_NbsSffMsaRateSelectImplemented_Object=MibTableColumn
nbsSffMsaRateSelectImplemented=_NbsSffMsaRateSelectImplemented_Object((1,3,6,1,4,1,629,204,1,1,1,1,22),_NbsSffMsaRateSelectImplemented_Type())
nbsSffMsaRateSelectImplemented.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSffMsaRateSelectImplemented.setStatus(_A)
_NbsSffMsaMaxBitRate_Type=Integer32
_NbsSffMsaMaxBitRate_Object=MibTableColumn
nbsSffMsaMaxBitRate=_NbsSffMsaMaxBitRate_Object((1,3,6,1,4,1,629,204,1,1,1,1,23),_NbsSffMsaMaxBitRate_Type())
nbsSffMsaMaxBitRate.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSffMsaMaxBitRate.setStatus(_A)
_NbsSffMsaMinBitRate_Type=Integer32
_NbsSffMsaMinBitRate_Object=MibTableColumn
nbsSffMsaMinBitRate=_NbsSffMsaMinBitRate_Object((1,3,6,1,4,1,629,204,1,1,1,1,24),_NbsSffMsaMinBitRate_Type())
nbsSffMsaMinBitRate.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSffMsaMinBitRate.setStatus(_A)
class _NbsSffMsaVendorSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_NbsSffMsaVendorSerialNumber_Type.__name__=_D
_NbsSffMsaVendorSerialNumber_Object=MibTableColumn
nbsSffMsaVendorSerialNumber=_NbsSffMsaVendorSerialNumber_Object((1,3,6,1,4,1,629,204,1,1,1,1,25),_NbsSffMsaVendorSerialNumber_Type())
nbsSffMsaVendorSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSffMsaVendorSerialNumber.setStatus(_A)
class _NbsSffMsaVendorDateCode_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,8))
_NbsSffMsaVendorDateCode_Type.__name__=_D
_NbsSffMsaVendorDateCode_Object=MibTableColumn
nbsSffMsaVendorDateCode=_NbsSffMsaVendorDateCode_Object((1,3,6,1,4,1,629,204,1,1,1,1,26),_NbsSffMsaVendorDateCode_Type())
nbsSffMsaVendorDateCode.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSffMsaVendorDateCode.setStatus(_A)
class _NbsSffMsaExtChecksumMatch_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_NbsSffMsaExtChecksumMatch_Type.__name__=_C
_NbsSffMsaExtChecksumMatch_Object=MibTableColumn
nbsSffMsaExtChecksumMatch=_NbsSffMsaExtChecksumMatch_Object((1,3,6,1,4,1,629,204,1,1,1,1,27),_NbsSffMsaExtChecksumMatch_Type())
nbsSffMsaExtChecksumMatch.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSffMsaExtChecksumMatch.setStatus(_A)
_NbsSffWdmGrp_ObjectIdentity=ObjectIdentity
nbsSffWdmGrp=_NbsSffWdmGrp_ObjectIdentity((1,3,6,1,4,1,629,204,1,2))
if mibBuilder.loadTexts:nbsSffWdmGrp.setStatus(_A)
_NbsSffWdmTable_Object=MibTable
nbsSffWdmTable=_NbsSffWdmTable_Object((1,3,6,1,4,1,629,204,1,2,1))
if mibBuilder.loadTexts:nbsSffWdmTable.setStatus(_A)
_NbsSffWdmEntry_Object=MibTableRow
nbsSffWdmEntry=_NbsSffWdmEntry_Object((1,3,6,1,4,1,629,204,1,2,1,1))
nbsSffWdmEntry.setIndexNames((0,_J,_K))
if mibBuilder.loadTexts:nbsSffWdmEntry.setStatus(_A)
class _NbsSffWdmClassOfPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('under1W',1),('oneToOneAndHalfW',2),('overOneAndHalfW',3),(_O,4)))
_NbsSffWdmClassOfPower_Type.__name__=_C
_NbsSffWdmClassOfPower_Object=MibTableColumn
nbsSffWdmClassOfPower=_NbsSffWdmClassOfPower_Object((1,3,6,1,4,1,629,204,1,2,1,1,1),_NbsSffWdmClassOfPower_Type())
nbsSffWdmClassOfPower.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSffWdmClassOfPower.setStatus(_A)
class _NbsSffWdmClassOfTemperature_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('class0',1),('class1',2),('class2',3),('class3',4)))
_NbsSffWdmClassOfTemperature_Type.__name__=_C
_NbsSffWdmClassOfTemperature_Object=MibTableColumn
nbsSffWdmClassOfTemperature=_NbsSffWdmClassOfTemperature_Object((1,3,6,1,4,1,629,204,1,2,1,1,2),_NbsSffWdmClassOfTemperature_Type())
nbsSffWdmClassOfTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSffWdmClassOfTemperature.setStatus(_A)
class _NbsSffWdmClassOfWdm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('noWdm',1),('cwdm',2),('dwdm',3),(_O,4)))
_NbsSffWdmClassOfWdm_Type.__name__=_C
_NbsSffWdmClassOfWdm_Object=MibTableColumn
nbsSffWdmClassOfWdm=_NbsSffWdmClassOfWdm_Object((1,3,6,1,4,1,629,204,1,2,1,1,3),_NbsSffWdmClassOfWdm_Type())
nbsSffWdmClassOfWdm.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSffWdmClassOfWdm.setStatus(_A)
_NbsSffWdmOpticalReach_Type=Integer32
_NbsSffWdmOpticalReach_Object=MibTableColumn
nbsSffWdmOpticalReach=_NbsSffWdmOpticalReach_Object((1,3,6,1,4,1,629,204,1,2,1,1,4),_NbsSffWdmOpticalReach_Type())
nbsSffWdmOpticalReach.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSffWdmOpticalReach.setStatus(_A)
class _NbsSffWdmMaxCaseTemperature_Type(Integer32):defaultValue=70;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483647,2147483647))
_NbsSffWdmMaxCaseTemperature_Type.__name__=_C
_NbsSffWdmMaxCaseTemperature_Object=MibTableColumn
nbsSffWdmMaxCaseTemperature=_NbsSffWdmMaxCaseTemperature_Object((1,3,6,1,4,1,629,204,1,2,1,1,5),_NbsSffWdmMaxCaseTemperature_Type())
nbsSffWdmMaxCaseTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSffWdmMaxCaseTemperature.setStatus(_A)
class _NbsSffWdmMinCaseTemperature_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483647,2147483647))
_NbsSffWdmMinCaseTemperature_Type.__name__=_C
_NbsSffWdmMinCaseTemperature_Object=MibTableColumn
nbsSffWdmMinCaseTemperature=_NbsSffWdmMinCaseTemperature_Object((1,3,6,1,4,1,629,204,1,2,1,1,6),_NbsSffWdmMinCaseTemperature_Type())
nbsSffWdmMinCaseTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSffWdmMinCaseTemperature.setStatus(_A)
_NbsSffWdmMaxSupplyCurrent_Type=Integer32
_NbsSffWdmMaxSupplyCurrent_Object=MibTableColumn
nbsSffWdmMaxSupplyCurrent=_NbsSffWdmMaxSupplyCurrent_Object((1,3,6,1,4,1,629,204,1,2,1,1,7),_NbsSffWdmMaxSupplyCurrent_Type())
nbsSffWdmMaxSupplyCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSffWdmMaxSupplyCurrent.setStatus(_A)
_NbsSffWdmNumberOfChannels_Type=Integer32
_NbsSffWdmNumberOfChannels_Object=MibTableColumn
nbsSffWdmNumberOfChannels=_NbsSffWdmNumberOfChannels_Object((1,3,6,1,4,1,629,204,1,2,1,1,8),_NbsSffWdmNumberOfChannels_Type())
nbsSffWdmNumberOfChannels.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSffWdmNumberOfChannels.setStatus(_A)
class _NbsSffWdmChannelSpacing_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('notTunable',1),('ghz50',2),('ghz100',3),('ghz200',4)))
_NbsSffWdmChannelSpacing_Type.__name__=_C
_NbsSffWdmChannelSpacing_Object=MibTableColumn
nbsSffWdmChannelSpacing=_NbsSffWdmChannelSpacing_Object((1,3,6,1,4,1,629,204,1,2,1,1,9),_NbsSffWdmChannelSpacing_Type())
nbsSffWdmChannelSpacing.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSffWdmChannelSpacing.setStatus(_A)
class _NbsSffWdmVariableDecisionThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_P,2)))
_NbsSffWdmVariableDecisionThreshold_Type.__name__=_C
_NbsSffWdmVariableDecisionThreshold_Object=MibTableColumn
nbsSffWdmVariableDecisionThreshold=_NbsSffWdmVariableDecisionThreshold_Object((1,3,6,1,4,1,629,204,1,2,1,1,10),_NbsSffWdmVariableDecisionThreshold_Type())
nbsSffWdmVariableDecisionThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSffWdmVariableDecisionThreshold.setStatus(_A)
class _NbsSffWdmWavelengthMonitorType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('wavelength',1),('laserTemperature',2)))
_NbsSffWdmWavelengthMonitorType_Type.__name__=_C
_NbsSffWdmWavelengthMonitorType_Object=MibTableColumn
nbsSffWdmWavelengthMonitorType=_NbsSffWdmWavelengthMonitorType_Object((1,3,6,1,4,1,629,204,1,2,1,1,11),_NbsSffWdmWavelengthMonitorType_Type())
nbsSffWdmWavelengthMonitorType.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSffWdmWavelengthMonitorType.setStatus(_A)
class _NbsSffWdmExtTransmitPowerType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('pwrDefault',1),('pwrExtended',2)))
_NbsSffWdmExtTransmitPowerType_Type.__name__=_C
_NbsSffWdmExtTransmitPowerType_Object=MibTableColumn
nbsSffWdmExtTransmitPowerType=_NbsSffWdmExtTransmitPowerType_Object((1,3,6,1,4,1,629,204,1,2,1,1,12),_NbsSffWdmExtTransmitPowerType_Type())
nbsSffWdmExtTransmitPowerType.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSffWdmExtTransmitPowerType.setStatus(_A)
class _NbsSffWdmVariableOpticalAttenuator_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_NbsSffWdmVariableOpticalAttenuator_Type.__name__=_C
_NbsSffWdmVariableOpticalAttenuator_Object=MibTableColumn
nbsSffWdmVariableOpticalAttenuator=_NbsSffWdmVariableOpticalAttenuator_Object((1,3,6,1,4,1,629,204,1,2,1,1,13),_NbsSffWdmVariableOpticalAttenuator_Type())
nbsSffWdmVariableOpticalAttenuator.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSffWdmVariableOpticalAttenuator.setStatus(_A)
class _NbsSffWdmPilotToneFunctionality_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('pilotToneNone',1),('pilotToneDetection',2),('pilotToneInjection',3),('pilotToneInjectionDetection',4),('pilotToneEnhanced',5)))
_NbsSffWdmPilotToneFunctionality_Type.__name__=_C
_NbsSffWdmPilotToneFunctionality_Object=MibTableColumn
nbsSffWdmPilotToneFunctionality=_NbsSffWdmPilotToneFunctionality_Object((1,3,6,1,4,1,629,204,1,2,1,1,14),_NbsSffWdmPilotToneFunctionality_Type())
nbsSffWdmPilotToneFunctionality.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSffWdmPilotToneFunctionality.setStatus(_A)
class _NbsSffWdmOptionalInterruptPin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_P,2)))
_NbsSffWdmOptionalInterruptPin_Type.__name__=_C
_NbsSffWdmOptionalInterruptPin_Object=MibTableColumn
nbsSffWdmOptionalInterruptPin=_NbsSffWdmOptionalInterruptPin_Object((1,3,6,1,4,1,629,204,1,2,1,1,15),_NbsSffWdmOptionalInterruptPin_Type())
nbsSffWdmOptionalInterruptPin.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSffWdmOptionalInterruptPin.setStatus(_A)
class _NbsSffWdmLaserWavelength_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,150))
_NbsSffWdmLaserWavelength_Type.__name__=_D
_NbsSffWdmLaserWavelength_Object=MibTableColumn
nbsSffWdmLaserWavelength=_NbsSffWdmLaserWavelength_Object((1,3,6,1,4,1,629,204,1,2,1,1,16),_NbsSffWdmLaserWavelength_Type())
nbsSffWdmLaserWavelength.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSffWdmLaserWavelength.setStatus(_A)
_NbsSffWdmFrequency_Type=NbsTcMHz
_NbsSffWdmFrequency_Object=MibTableColumn
nbsSffWdmFrequency=_NbsSffWdmFrequency_Object((1,3,6,1,4,1,629,204,1,2,1,1,17),_NbsSffWdmFrequency_Type())
nbsSffWdmFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSffWdmFrequency.setStatus(_A)
_NbsSffWdmChannelBand_Type=NbsCmmcChannelBand
_NbsSffWdmChannelBand_Object=MibTableColumn
nbsSffWdmChannelBand=_NbsSffWdmChannelBand_Object((1,3,6,1,4,1,629,204,1,2,1,1,18),_NbsSffWdmChannelBand_Type())
nbsSffWdmChannelBand.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSffWdmChannelBand.setStatus(_A)
_NbsSffWdmChannelNumber_Type=Integer32
_NbsSffWdmChannelNumber_Object=MibTableColumn
nbsSffWdmChannelNumber=_NbsSffWdmChannelNumber_Object((1,3,6,1,4,1,629,204,1,2,1,1,19),_NbsSffWdmChannelNumber_Type())
nbsSffWdmChannelNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSffWdmChannelNumber.setStatus(_A)
_NbsSffDiagnosticsGrp_ObjectIdentity=ObjectIdentity
nbsSffDiagnosticsGrp=_NbsSffDiagnosticsGrp_ObjectIdentity((1,3,6,1,4,1,629,204,1,3))
if mibBuilder.loadTexts:nbsSffDiagnosticsGrp.setStatus(_A)
_NbsSffDiagsTable_Object=MibTable
nbsSffDiagsTable=_NbsSffDiagsTable_Object((1,3,6,1,4,1,629,204,1,3,1))
if mibBuilder.loadTexts:nbsSffDiagsTable.setStatus(_A)
_NbsSffDiagsEntry_Object=MibTableRow
nbsSffDiagsEntry=_NbsSffDiagsEntry_Object((1,3,6,1,4,1,629,204,1,3,1,1))
nbsSffDiagsEntry.setIndexNames((0,_J,_K))
if mibBuilder.loadTexts:nbsSffDiagsEntry.setStatus(_A)
class _NbsSffDiagsRateIdentifier_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_I,1),('rate421G',2),('rate842GRx',3),('rate842GRxTx',4),('rate842GTx',5)))
_NbsSffDiagsRateIdentifier_Type.__name__=_C
_NbsSffDiagsRateIdentifier_Object=MibTableColumn
nbsSffDiagsRateIdentifier=_NbsSffDiagsRateIdentifier_Object((1,3,6,1,4,1,629,204,1,3,1,1,1),_NbsSffDiagsRateIdentifier_Type())
nbsSffDiagsRateIdentifier.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSffDiagsRateIdentifier.setStatus(_A)
_NbsSffDiagsLinkLengthOm3_Type=Integer32
_NbsSffDiagsLinkLengthOm3_Object=MibTableColumn
nbsSffDiagsLinkLengthOm3=_NbsSffDiagsLinkLengthOm3_Object((1,3,6,1,4,1,629,204,1,3,1,1,2),_NbsSffDiagsLinkLengthOm3_Type())
nbsSffDiagsLinkLengthOm3.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSffDiagsLinkLengthOm3.setStatus(_A)
_NbsSffDiagsLaserWavelength_Type=Integer32
_NbsSffDiagsLaserWavelength_Object=MibTableColumn
nbsSffDiagsLaserWavelength=_NbsSffDiagsLaserWavelength_Object((1,3,6,1,4,1,629,204,1,3,1,1,3),_NbsSffDiagsLaserWavelength_Type())
nbsSffDiagsLaserWavelength.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSffDiagsLaserWavelength.setStatus(_A)
class _NbsSffDiagsLROutputImplemented_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_NbsSffDiagsLROutputImplemented_Type.__name__=_C
_NbsSffDiagsLROutputImplemented_Object=MibTableColumn
nbsSffDiagsLROutputImplemented=_NbsSffDiagsLROutputImplemented_Object((1,3,6,1,4,1,629,204,1,3,1,1,4),_NbsSffDiagsLROutputImplemented_Type())
nbsSffDiagsLROutputImplemented.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSffDiagsLROutputImplemented.setStatus(_A)
class _NbsSffDiagsPowerLevelDeclaration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('level1',1),('level2',2)))
_NbsSffDiagsPowerLevelDeclaration_Type.__name__=_C
_NbsSffDiagsPowerLevelDeclaration_Object=MibTableColumn
nbsSffDiagsPowerLevelDeclaration=_NbsSffDiagsPowerLevelDeclaration_Object((1,3,6,1,4,1,629,204,1,3,1,1,5),_NbsSffDiagsPowerLevelDeclaration_Type())
nbsSffDiagsPowerLevelDeclaration.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSffDiagsPowerLevelDeclaration.setStatus(_A)
class _NbsSffDiagsCooledTranDeclaration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('uncooled',1),('cooled',2)))
_NbsSffDiagsCooledTranDeclaration_Type.__name__=_C
_NbsSffDiagsCooledTranDeclaration_Object=MibTableColumn
nbsSffDiagsCooledTranDeclaration=_NbsSffDiagsCooledTranDeclaration_Object((1,3,6,1,4,1,629,204,1,3,1,1,6),_NbsSffDiagsCooledTranDeclaration_Type())
nbsSffDiagsCooledTranDeclaration.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSffDiagsCooledTranDeclaration.setStatus(_A)
class _NbsSffDiagsAddressChangeRequired_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_NbsSffDiagsAddressChangeRequired_Type.__name__=_C
_NbsSffDiagsAddressChangeRequired_Object=MibTableColumn
nbsSffDiagsAddressChangeRequired=_NbsSffDiagsAddressChangeRequired_Object((1,3,6,1,4,1,629,204,1,3,1,1,7),_NbsSffDiagsAddressChangeRequired_Type())
nbsSffDiagsAddressChangeRequired.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSffDiagsAddressChangeRequired.setStatus(_A)
class _NbsSffDiagsPowerMeasurementType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('oma',1),('averagePower',2)))
_NbsSffDiagsPowerMeasurementType_Type.__name__=_C
_NbsSffDiagsPowerMeasurementType_Object=MibTableColumn
nbsSffDiagsPowerMeasurementType=_NbsSffDiagsPowerMeasurementType_Object((1,3,6,1,4,1,629,204,1,3,1,1,8),_NbsSffDiagsPowerMeasurementType_Type())
nbsSffDiagsPowerMeasurementType.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSffDiagsPowerMeasurementType.setStatus(_A)
class _NbsSffDiagsExternallyCalibrated_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_NbsSffDiagsExternallyCalibrated_Type.__name__=_C
_NbsSffDiagsExternallyCalibrated_Object=MibTableColumn
nbsSffDiagsExternallyCalibrated=_NbsSffDiagsExternallyCalibrated_Object((1,3,6,1,4,1,629,204,1,3,1,1,9),_NbsSffDiagsExternallyCalibrated_Type())
nbsSffDiagsExternallyCalibrated.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSffDiagsExternallyCalibrated.setStatus(_A)
class _NbsSffDiagsInternallyCalibrated_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_NbsSffDiagsInternallyCalibrated_Type.__name__=_C
_NbsSffDiagsInternallyCalibrated_Object=MibTableColumn
nbsSffDiagsInternallyCalibrated=_NbsSffDiagsInternallyCalibrated_Object((1,3,6,1,4,1,629,204,1,3,1,1,10),_NbsSffDiagsInternallyCalibrated_Type())
nbsSffDiagsInternallyCalibrated.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSffDiagsInternallyCalibrated.setStatus(_A)
class _NbsSffDiagsDDMonitoringImplemented_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_NbsSffDiagsDDMonitoringImplemented_Type.__name__=_C
_NbsSffDiagsDDMonitoringImplemented_Object=MibTableColumn
nbsSffDiagsDDMonitoringImplemented=_NbsSffDiagsDDMonitoringImplemented_Object((1,3,6,1,4,1,629,204,1,3,1,1,11),_NbsSffDiagsDDMonitoringImplemented_Type())
nbsSffDiagsDDMonitoringImplemented.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSffDiagsDDMonitoringImplemented.setStatus(_A)
class _NbsSffDiagsOptRateSelectControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_NbsSffDiagsOptRateSelectControl_Type.__name__=_C
_NbsSffDiagsOptRateSelectControl_Object=MibTableColumn
nbsSffDiagsOptRateSelectControl=_NbsSffDiagsOptRateSelectControl_Object((1,3,6,1,4,1,629,204,1,3,1,1,12),_NbsSffDiagsOptRateSelectControl_Type())
nbsSffDiagsOptRateSelectControl.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSffDiagsOptRateSelectControl.setStatus(_A)
class _NbsSffDiagsOptAppSelectControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_NbsSffDiagsOptAppSelectControl_Type.__name__=_C
_NbsSffDiagsOptAppSelectControl_Object=MibTableColumn
nbsSffDiagsOptAppSelectControl=_NbsSffDiagsOptAppSelectControl_Object((1,3,6,1,4,1,629,204,1,3,1,1,13),_NbsSffDiagsOptAppSelectControl_Type())
nbsSffDiagsOptAppSelectControl.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSffDiagsOptAppSelectControl.setStatus(_A)
class _NbsSffDiagsOptSoftRSControlMon_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_NbsSffDiagsOptSoftRSControlMon_Type.__name__=_C
_NbsSffDiagsOptSoftRSControlMon_Object=MibTableColumn
nbsSffDiagsOptSoftRSControlMon=_NbsSffDiagsOptSoftRSControlMon_Object((1,3,6,1,4,1,629,204,1,3,1,1,14),_NbsSffDiagsOptSoftRSControlMon_Type())
nbsSffDiagsOptSoftRSControlMon.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSffDiagsOptSoftRSControlMon.setStatus(_A)
class _NbsSffDiagsOptSoftRxLoSMonitoring_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_NbsSffDiagsOptSoftRxLoSMonitoring_Type.__name__=_C
_NbsSffDiagsOptSoftRxLoSMonitoring_Object=MibTableColumn
nbsSffDiagsOptSoftRxLoSMonitoring=_NbsSffDiagsOptSoftRxLoSMonitoring_Object((1,3,6,1,4,1,629,204,1,3,1,1,15),_NbsSffDiagsOptSoftRxLoSMonitoring_Type())
nbsSffDiagsOptSoftRxLoSMonitoring.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSffDiagsOptSoftRxLoSMonitoring.setStatus(_A)
class _NbsSffDiagsOptSoftTxFaultMonitoring_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_NbsSffDiagsOptSoftTxFaultMonitoring_Type.__name__=_C
_NbsSffDiagsOptSoftTxFaultMonitoring_Object=MibTableColumn
nbsSffDiagsOptSoftTxFaultMonitoring=_NbsSffDiagsOptSoftTxFaultMonitoring_Object((1,3,6,1,4,1,629,204,1,3,1,1,16),_NbsSffDiagsOptSoftTxFaultMonitoring_Type())
nbsSffDiagsOptSoftTxFaultMonitoring.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSffDiagsOptSoftTxFaultMonitoring.setStatus(_A)
class _NbsSffDiagsOptSoftTxDisable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_NbsSffDiagsOptSoftTxDisable_Type.__name__=_C
_NbsSffDiagsOptSoftTxDisable_Object=MibTableColumn
nbsSffDiagsOptSoftTxDisable=_NbsSffDiagsOptSoftTxDisable_Object((1,3,6,1,4,1,629,204,1,3,1,1,17),_NbsSffDiagsOptSoftTxDisable_Type())
nbsSffDiagsOptSoftTxDisable.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSffDiagsOptSoftTxDisable.setStatus(_A)
class _NbsSffDiagsOptAlarmWarningFlags_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_NbsSffDiagsOptAlarmWarningFlags_Type.__name__=_C
_NbsSffDiagsOptAlarmWarningFlags_Object=MibTableColumn
nbsSffDiagsOptAlarmWarningFlags=_NbsSffDiagsOptAlarmWarningFlags_Object((1,3,6,1,4,1,629,204,1,3,1,1,18),_NbsSffDiagsOptAlarmWarningFlags_Type())
nbsSffDiagsOptAlarmWarningFlags.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSffDiagsOptAlarmWarningFlags.setStatus(_A)
class _NbsSffDiags8472Compliance_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,256)));namedValues=NamedValues(*((_I,1),('rev9dot3of8472',2),('rev9dot5of8472',3),('rev10dot2of8472',4),('rev10dot4of8472',5),('rev11dot0of8472',6),('rev11dot3of8472',7),('rev11dot4of8472',8),('rev12dot0of8472',9),('unallocated',256)))
_NbsSffDiags8472Compliance_Type.__name__=_C
_NbsSffDiags8472Compliance_Object=MibTableColumn
nbsSffDiags8472Compliance=_NbsSffDiags8472Compliance_Object((1,3,6,1,4,1,629,204,1,3,1,1,19),_NbsSffDiags8472Compliance_Type())
nbsSffDiags8472Compliance.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSffDiags8472Compliance.setStatus(_A)
class _NbsSffDiagsTemperature_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483647,2147483647))
_NbsSffDiagsTemperature_Type.__name__=_C
_NbsSffDiagsTemperature_Object=MibTableColumn
nbsSffDiagsTemperature=_NbsSffDiagsTemperature_Object((1,3,6,1,4,1,629,204,1,3,1,1,20),_NbsSffDiagsTemperature_Type())
nbsSffDiagsTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSffDiagsTemperature.setStatus(_A)
_NbsSffDiagsTempLowAlarm_Type=Integer32
_NbsSffDiagsTempLowAlarm_Object=MibTableColumn
nbsSffDiagsTempLowAlarm=_NbsSffDiagsTempLowAlarm_Object((1,3,6,1,4,1,629,204,1,3,1,1,21),_NbsSffDiagsTempLowAlarm_Type())
nbsSffDiagsTempLowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSffDiagsTempLowAlarm.setStatus(_A)
_NbsSffDiagsTempLowWarn_Type=Integer32
_NbsSffDiagsTempLowWarn_Object=MibTableColumn
nbsSffDiagsTempLowWarn=_NbsSffDiagsTempLowWarn_Object((1,3,6,1,4,1,629,204,1,3,1,1,22),_NbsSffDiagsTempLowWarn_Type())
nbsSffDiagsTempLowWarn.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSffDiagsTempLowWarn.setStatus(_A)
_NbsSffDiagsTempHighWarn_Type=Integer32
_NbsSffDiagsTempHighWarn_Object=MibTableColumn
nbsSffDiagsTempHighWarn=_NbsSffDiagsTempHighWarn_Object((1,3,6,1,4,1,629,204,1,3,1,1,23),_NbsSffDiagsTempHighWarn_Type())
nbsSffDiagsTempHighWarn.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSffDiagsTempHighWarn.setStatus(_A)
_NbsSffDiagsTempHighAlarm_Type=Integer32
_NbsSffDiagsTempHighAlarm_Object=MibTableColumn
nbsSffDiagsTempHighAlarm=_NbsSffDiagsTempHighAlarm_Object((1,3,6,1,4,1,629,204,1,3,1,1,24),_NbsSffDiagsTempHighAlarm_Type())
nbsSffDiagsTempHighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSffDiagsTempHighAlarm.setStatus(_A)
class _NbsSffDiagsVoltage_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_NbsSffDiagsVoltage_Type.__name__=_D
_NbsSffDiagsVoltage_Object=MibTableColumn
nbsSffDiagsVoltage=_NbsSffDiagsVoltage_Object((1,3,6,1,4,1,629,204,1,3,1,1,25),_NbsSffDiagsVoltage_Type())
nbsSffDiagsVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSffDiagsVoltage.setStatus(_A)
_NbsSffDiagsVoltLowAlarm_Type=Integer32
_NbsSffDiagsVoltLowAlarm_Object=MibTableColumn
nbsSffDiagsVoltLowAlarm=_NbsSffDiagsVoltLowAlarm_Object((1,3,6,1,4,1,629,204,1,3,1,1,26),_NbsSffDiagsVoltLowAlarm_Type())
nbsSffDiagsVoltLowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSffDiagsVoltLowAlarm.setStatus(_A)
_NbsSffDiagsVoltLowWarn_Type=Integer32
_NbsSffDiagsVoltLowWarn_Object=MibTableColumn
nbsSffDiagsVoltLowWarn=_NbsSffDiagsVoltLowWarn_Object((1,3,6,1,4,1,629,204,1,3,1,1,27),_NbsSffDiagsVoltLowWarn_Type())
nbsSffDiagsVoltLowWarn.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSffDiagsVoltLowWarn.setStatus(_A)
_NbsSffDiagsVoltHighWarn_Type=Integer32
_NbsSffDiagsVoltHighWarn_Object=MibTableColumn
nbsSffDiagsVoltHighWarn=_NbsSffDiagsVoltHighWarn_Object((1,3,6,1,4,1,629,204,1,3,1,1,28),_NbsSffDiagsVoltHighWarn_Type())
nbsSffDiagsVoltHighWarn.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSffDiagsVoltHighWarn.setStatus(_A)
_NbsSffDiagsVoltHighAlarm_Type=Integer32
_NbsSffDiagsVoltHighAlarm_Object=MibTableColumn
nbsSffDiagsVoltHighAlarm=_NbsSffDiagsVoltHighAlarm_Object((1,3,6,1,4,1,629,204,1,3,1,1,29),_NbsSffDiagsVoltHighAlarm_Type())
nbsSffDiagsVoltHighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSffDiagsVoltHighAlarm.setStatus(_A)
class _NbsSffDiagsBiasCurrent_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_NbsSffDiagsBiasCurrent_Type.__name__=_D
_NbsSffDiagsBiasCurrent_Object=MibTableColumn
nbsSffDiagsBiasCurrent=_NbsSffDiagsBiasCurrent_Object((1,3,6,1,4,1,629,204,1,3,1,1,30),_NbsSffDiagsBiasCurrent_Type())
nbsSffDiagsBiasCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSffDiagsBiasCurrent.setStatus(_A)
_NbsSffDiagsBiasLowAlarm_Type=Integer32
_NbsSffDiagsBiasLowAlarm_Object=MibTableColumn
nbsSffDiagsBiasLowAlarm=_NbsSffDiagsBiasLowAlarm_Object((1,3,6,1,4,1,629,204,1,3,1,1,31),_NbsSffDiagsBiasLowAlarm_Type())
nbsSffDiagsBiasLowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSffDiagsBiasLowAlarm.setStatus(_A)
_NbsSffDiagsBiasLowWarn_Type=Integer32
_NbsSffDiagsBiasLowWarn_Object=MibTableColumn
nbsSffDiagsBiasLowWarn=_NbsSffDiagsBiasLowWarn_Object((1,3,6,1,4,1,629,204,1,3,1,1,32),_NbsSffDiagsBiasLowWarn_Type())
nbsSffDiagsBiasLowWarn.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSffDiagsBiasLowWarn.setStatus(_A)
_NbsSffDiagsBiasHighWarn_Type=Integer32
_NbsSffDiagsBiasHighWarn_Object=MibTableColumn
nbsSffDiagsBiasHighWarn=_NbsSffDiagsBiasHighWarn_Object((1,3,6,1,4,1,629,204,1,3,1,1,33),_NbsSffDiagsBiasHighWarn_Type())
nbsSffDiagsBiasHighWarn.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSffDiagsBiasHighWarn.setStatus(_A)
_NbsSffDiagsBiasHighAlarm_Type=Integer32
_NbsSffDiagsBiasHighAlarm_Object=MibTableColumn
nbsSffDiagsBiasHighAlarm=_NbsSffDiagsBiasHighAlarm_Object((1,3,6,1,4,1,629,204,1,3,1,1,34),_NbsSffDiagsBiasHighAlarm_Type())
nbsSffDiagsBiasHighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSffDiagsBiasHighAlarm.setStatus(_A)
class _NbsSffDiagsTxPower_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_NbsSffDiagsTxPower_Type.__name__=_D
_NbsSffDiagsTxPower_Object=MibTableColumn
nbsSffDiagsTxPower=_NbsSffDiagsTxPower_Object((1,3,6,1,4,1,629,204,1,3,1,1,35),_NbsSffDiagsTxPower_Type())
nbsSffDiagsTxPower.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSffDiagsTxPower.setStatus(_A)
_NbsSffDiagsTxPowerLowAlarm_Type=Integer32
_NbsSffDiagsTxPowerLowAlarm_Object=MibTableColumn
nbsSffDiagsTxPowerLowAlarm=_NbsSffDiagsTxPowerLowAlarm_Object((1,3,6,1,4,1,629,204,1,3,1,1,36),_NbsSffDiagsTxPowerLowAlarm_Type())
nbsSffDiagsTxPowerLowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSffDiagsTxPowerLowAlarm.setStatus(_A)
_NbsSffDiagsTxPowerLowWarn_Type=Integer32
_NbsSffDiagsTxPowerLowWarn_Object=MibTableColumn
nbsSffDiagsTxPowerLowWarn=_NbsSffDiagsTxPowerLowWarn_Object((1,3,6,1,4,1,629,204,1,3,1,1,37),_NbsSffDiagsTxPowerLowWarn_Type())
nbsSffDiagsTxPowerLowWarn.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSffDiagsTxPowerLowWarn.setStatus(_A)
_NbsSffDiagsTxPowerHighWarn_Type=Integer32
_NbsSffDiagsTxPowerHighWarn_Object=MibTableColumn
nbsSffDiagsTxPowerHighWarn=_NbsSffDiagsTxPowerHighWarn_Object((1,3,6,1,4,1,629,204,1,3,1,1,38),_NbsSffDiagsTxPowerHighWarn_Type())
nbsSffDiagsTxPowerHighWarn.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSffDiagsTxPowerHighWarn.setStatus(_A)
_NbsSffDiagsTxPowerHighAlarm_Type=Integer32
_NbsSffDiagsTxPowerHighAlarm_Object=MibTableColumn
nbsSffDiagsTxPowerHighAlarm=_NbsSffDiagsTxPowerHighAlarm_Object((1,3,6,1,4,1,629,204,1,3,1,1,39),_NbsSffDiagsTxPowerHighAlarm_Type())
nbsSffDiagsTxPowerHighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSffDiagsTxPowerHighAlarm.setStatus(_A)
class _NbsSffDiagsRxPower_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_NbsSffDiagsRxPower_Type.__name__=_D
_NbsSffDiagsRxPower_Object=MibTableColumn
nbsSffDiagsRxPower=_NbsSffDiagsRxPower_Object((1,3,6,1,4,1,629,204,1,3,1,1,40),_NbsSffDiagsRxPower_Type())
nbsSffDiagsRxPower.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSffDiagsRxPower.setStatus(_A)
_NbsSffDiagsRxPowerLowAlarm_Type=Integer32
_NbsSffDiagsRxPowerLowAlarm_Object=MibTableColumn
nbsSffDiagsRxPowerLowAlarm=_NbsSffDiagsRxPowerLowAlarm_Object((1,3,6,1,4,1,629,204,1,3,1,1,41),_NbsSffDiagsRxPowerLowAlarm_Type())
nbsSffDiagsRxPowerLowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSffDiagsRxPowerLowAlarm.setStatus(_A)
_NbsSffDiagsRxPowerLowWarn_Type=Integer32
_NbsSffDiagsRxPowerLowWarn_Object=MibTableColumn
nbsSffDiagsRxPowerLowWarn=_NbsSffDiagsRxPowerLowWarn_Object((1,3,6,1,4,1,629,204,1,3,1,1,42),_NbsSffDiagsRxPowerLowWarn_Type())
nbsSffDiagsRxPowerLowWarn.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSffDiagsRxPowerLowWarn.setStatus(_A)
_NbsSffDiagsRxPowerHighWarn_Type=Integer32
_NbsSffDiagsRxPowerHighWarn_Object=MibTableColumn
nbsSffDiagsRxPowerHighWarn=_NbsSffDiagsRxPowerHighWarn_Object((1,3,6,1,4,1,629,204,1,3,1,1,43),_NbsSffDiagsRxPowerHighWarn_Type())
nbsSffDiagsRxPowerHighWarn.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSffDiagsRxPowerHighWarn.setStatus(_A)
_NbsSffDiagsRxPowerHighAlarm_Type=Integer32
_NbsSffDiagsRxPowerHighAlarm_Object=MibTableColumn
nbsSffDiagsRxPowerHighAlarm=_NbsSffDiagsRxPowerHighAlarm_Object((1,3,6,1,4,1,629,204,1,3,1,1,44),_NbsSffDiagsRxPowerHighAlarm_Type())
nbsSffDiagsRxPowerHighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSffDiagsRxPowerHighAlarm.setStatus(_A)
_NbsSffDiagsDataReadyBarState_Type=Integer32
_NbsSffDiagsDataReadyBarState_Object=MibTableColumn
nbsSffDiagsDataReadyBarState=_NbsSffDiagsDataReadyBarState_Object((1,3,6,1,4,1,629,204,1,3,1,1,45),_NbsSffDiagsDataReadyBarState_Type())
nbsSffDiagsDataReadyBarState.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSffDiagsDataReadyBarState.setStatus(_A)
_NbsSffDiagsRxLosState_Type=Integer32
_NbsSffDiagsRxLosState_Object=MibTableColumn
nbsSffDiagsRxLosState=_NbsSffDiagsRxLosState_Object((1,3,6,1,4,1,629,204,1,3,1,1,46),_NbsSffDiagsRxLosState_Type())
nbsSffDiagsRxLosState.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSffDiagsRxLosState.setStatus(_A)
_NbsSffDiagsTxFaultState_Type=Integer32
_NbsSffDiagsTxFaultState_Object=MibTableColumn
nbsSffDiagsTxFaultState=_NbsSffDiagsTxFaultState_Object((1,3,6,1,4,1,629,204,1,3,1,1,47),_NbsSffDiagsTxFaultState_Type())
nbsSffDiagsTxFaultState.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSffDiagsTxFaultState.setStatus(_A)
_NbsSffDiagsSoftRateSelect_Type=Integer32
_NbsSffDiagsSoftRateSelect_Object=MibTableColumn
nbsSffDiagsSoftRateSelect=_NbsSffDiagsSoftRateSelect_Object((1,3,6,1,4,1,629,204,1,3,1,1,48),_NbsSffDiagsSoftRateSelect_Type())
nbsSffDiagsSoftRateSelect.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSffDiagsSoftRateSelect.setStatus(_A)
_NbsSffDiagsRateSelectState0_Type=Integer32
_NbsSffDiagsRateSelectState0_Object=MibTableColumn
nbsSffDiagsRateSelectState0=_NbsSffDiagsRateSelectState0_Object((1,3,6,1,4,1,629,204,1,3,1,1,49),_NbsSffDiagsRateSelectState0_Type())
nbsSffDiagsRateSelectState0.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSffDiagsRateSelectState0.setStatus(_A)
_NbsSffDiagsRS1State_Type=Integer32
_NbsSffDiagsRS1State_Object=MibTableColumn
nbsSffDiagsRS1State=_NbsSffDiagsRS1State_Object((1,3,6,1,4,1,629,204,1,3,1,1,50),_NbsSffDiagsRS1State_Type())
nbsSffDiagsRS1State.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSffDiagsRS1State.setStatus(_A)
_NbsSffDiagsSoftTxDisableSelect_Type=Integer32
_NbsSffDiagsSoftTxDisableSelect_Object=MibTableColumn
nbsSffDiagsSoftTxDisableSelect=_NbsSffDiagsSoftTxDisableSelect_Object((1,3,6,1,4,1,629,204,1,3,1,1,51),_NbsSffDiagsSoftTxDisableSelect_Type())
nbsSffDiagsSoftTxDisableSelect.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSffDiagsSoftTxDisableSelect.setStatus(_A)
_NbsSffDiagsTxDisableState_Type=Integer32
_NbsSffDiagsTxDisableState_Object=MibTableColumn
nbsSffDiagsTxDisableState=_NbsSffDiagsTxDisableState_Object((1,3,6,1,4,1,629,204,1,3,1,1,52),_NbsSffDiagsTxDisableState_Type())
nbsSffDiagsTxDisableState.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSffDiagsTxDisableState.setStatus(_A)
class _NbsSffDiagsBiasCurrentSlope_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_NbsSffDiagsBiasCurrentSlope_Type.__name__=_D
_NbsSffDiagsBiasCurrentSlope_Object=MibTableColumn
nbsSffDiagsBiasCurrentSlope=_NbsSffDiagsBiasCurrentSlope_Object((1,3,6,1,4,1,629,204,1,3,1,1,53),_NbsSffDiagsBiasCurrentSlope_Type())
nbsSffDiagsBiasCurrentSlope.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSffDiagsBiasCurrentSlope.setStatus(_A)
_NbsSffDiagsBiasCurrentOffset_Type=Integer32
_NbsSffDiagsBiasCurrentOffset_Object=MibTableColumn
nbsSffDiagsBiasCurrentOffset=_NbsSffDiagsBiasCurrentOffset_Object((1,3,6,1,4,1,629,204,1,3,1,1,54),_NbsSffDiagsBiasCurrentOffset_Type())
nbsSffDiagsBiasCurrentOffset.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSffDiagsBiasCurrentOffset.setStatus(_A)
class _NbsSffDiagsTxPowerSlope_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_NbsSffDiagsTxPowerSlope_Type.__name__=_D
_NbsSffDiagsTxPowerSlope_Object=MibTableColumn
nbsSffDiagsTxPowerSlope=_NbsSffDiagsTxPowerSlope_Object((1,3,6,1,4,1,629,204,1,3,1,1,55),_NbsSffDiagsTxPowerSlope_Type())
nbsSffDiagsTxPowerSlope.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSffDiagsTxPowerSlope.setStatus(_A)
_NbsSffDiagsTxPowerOffset_Type=Integer32
_NbsSffDiagsTxPowerOffset_Object=MibTableColumn
nbsSffDiagsTxPowerOffset=_NbsSffDiagsTxPowerOffset_Object((1,3,6,1,4,1,629,204,1,3,1,1,56),_NbsSffDiagsTxPowerOffset_Type())
nbsSffDiagsTxPowerOffset.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSffDiagsTxPowerOffset.setStatus(_A)
class _NbsSffDiagsTemperatureSlope_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_NbsSffDiagsTemperatureSlope_Type.__name__=_D
_NbsSffDiagsTemperatureSlope_Object=MibTableColumn
nbsSffDiagsTemperatureSlope=_NbsSffDiagsTemperatureSlope_Object((1,3,6,1,4,1,629,204,1,3,1,1,57),_NbsSffDiagsTemperatureSlope_Type())
nbsSffDiagsTemperatureSlope.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSffDiagsTemperatureSlope.setStatus(_A)
_NbsSffDiagsTemperatureOffset_Type=Integer32
_NbsSffDiagsTemperatureOffset_Object=MibTableColumn
nbsSffDiagsTemperatureOffset=_NbsSffDiagsTemperatureOffset_Object((1,3,6,1,4,1,629,204,1,3,1,1,58),_NbsSffDiagsTemperatureOffset_Type())
nbsSffDiagsTemperatureOffset.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSffDiagsTemperatureOffset.setStatus(_A)
class _NbsSffDiagsVoltageSlope_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_NbsSffDiagsVoltageSlope_Type.__name__=_D
_NbsSffDiagsVoltageSlope_Object=MibTableColumn
nbsSffDiagsVoltageSlope=_NbsSffDiagsVoltageSlope_Object((1,3,6,1,4,1,629,204,1,3,1,1,59),_NbsSffDiagsVoltageSlope_Type())
nbsSffDiagsVoltageSlope.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSffDiagsVoltageSlope.setStatus(_A)
_NbsSffDiagsVoltageOffset_Type=Integer32
_NbsSffDiagsVoltageOffset_Object=MibTableColumn
nbsSffDiagsVoltageOffset=_NbsSffDiagsVoltageOffset_Object((1,3,6,1,4,1,629,204,1,3,1,1,60),_NbsSffDiagsVoltageOffset_Type())
nbsSffDiagsVoltageOffset.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSffDiagsVoltageOffset.setStatus(_A)
class _NbsSffDiagsPowerLevelSelect_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_NbsSffDiagsPowerLevelSelect_Type.__name__=_C
_NbsSffDiagsPowerLevelSelect_Object=MibTableColumn
nbsSffDiagsPowerLevelSelect=_NbsSffDiagsPowerLevelSelect_Object((1,3,6,1,4,1,629,204,1,3,1,1,61),_NbsSffDiagsPowerLevelSelect_Type())
nbsSffDiagsPowerLevelSelect.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSffDiagsPowerLevelSelect.setStatus(_A)
class _NbsSffDiagsPowerLevelOpState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_NbsSffDiagsPowerLevelOpState_Type.__name__=_C
_NbsSffDiagsPowerLevelOpState_Object=MibTableColumn
nbsSffDiagsPowerLevelOpState=_NbsSffDiagsPowerLevelOpState_Object((1,3,6,1,4,1,629,204,1,3,1,1,62),_NbsSffDiagsPowerLevelOpState_Type())
nbsSffDiagsPowerLevelOpState.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSffDiagsPowerLevelOpState.setStatus(_A)
class _NbsSffDiagsSoftRSSelect_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_NbsSffDiagsSoftRSSelect_Type.__name__=_C
_NbsSffDiagsSoftRSSelect_Object=MibTableColumn
nbsSffDiagsSoftRSSelect=_NbsSffDiagsSoftRSSelect_Object((1,3,6,1,4,1,629,204,1,3,1,1,63),_NbsSffDiagsSoftRSSelect_Type())
nbsSffDiagsSoftRSSelect.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSffDiagsSoftRSSelect.setStatus(_A)
_NbsSffMsxGrp_ObjectIdentity=ObjectIdentity
nbsSffMsxGrp=_NbsSffMsxGrp_ObjectIdentity((1,3,6,1,4,1,629,204,1,4))
if mibBuilder.loadTexts:nbsSffMsxGrp.setStatus(_A)
_NbsSffMsxTableSize_Type=Unsigned32
_NbsSffMsxTableSize_Object=MibScalar
nbsSffMsxTableSize=_NbsSffMsxTableSize_Object((1,3,6,1,4,1,629,204,1,4,1),_NbsSffMsxTableSize_Type())
nbsSffMsxTableSize.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSffMsxTableSize.setStatus(_A)
_NbsSffMsxTable_Object=MibTable
nbsSffMsxTable=_NbsSffMsxTable_Object((1,3,6,1,4,1,629,204,1,4,2))
if mibBuilder.loadTexts:nbsSffMsxTable.setStatus(_A)
_NbsSffMsxEntry_Object=MibTableRow
nbsSffMsxEntry=_NbsSffMsxEntry_Object((1,3,6,1,4,1,629,204,1,4,2,1))
nbsSffMsxEntry.setIndexNames((0,_J,_Q))
if mibBuilder.loadTexts:nbsSffMsxEntry.setStatus(_A)
_NbsSffMsxPhysicalIfIndex_Type=InterfaceIndex
_NbsSffMsxPhysicalIfIndex_Object=MibTableColumn
nbsSffMsxPhysicalIfIndex=_NbsSffMsxPhysicalIfIndex_Object((1,3,6,1,4,1,629,204,1,4,2,1,1),_NbsSffMsxPhysicalIfIndex_Type())
nbsSffMsxPhysicalIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSffMsxPhysicalIfIndex.setStatus(_A)
class _NbsSffMsxHasSgmiiPhy_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),(_E,2),(_F,3)))
_NbsSffMsxHasSgmiiPhy_Type.__name__=_C
_NbsSffMsxHasSgmiiPhy_Object=MibTableColumn
nbsSffMsxHasSgmiiPhy=_NbsSffMsxHasSgmiiPhy_Object((1,3,6,1,4,1,629,204,1,4,2,1,2),_NbsSffMsxHasSgmiiPhy_Type())
nbsSffMsxHasSgmiiPhy.setMaxAccess('read-write')
if mibBuilder.loadTexts:nbsSffMsxHasSgmiiPhy.setStatus(_A)
mibBuilder.exportSymbols(_J,**{'nbsSffMib':nbsSffMib,'nbsSffObjects':nbsSffObjects,'nbsSffMsaGrp':nbsSffMsaGrp,'nbsSffMsaTable':nbsSffMsaTable,'nbsSffMsaEntry':nbsSffMsaEntry,_K:nbsSffMsaPhysicalIfIndex,'nbsSffMsaIdentifier':nbsSffMsaIdentifier,'nbsSffMsaExtIdentifier':nbsSffMsaExtIdentifier,'nbsSffMsaOpticalConnector':nbsSffMsaOpticalConnector,'nbsSffMsaTransceiverCodes':nbsSffMsaTransceiverCodes,'nbsSffMsaSerialEncoding':nbsSffMsaSerialEncoding,'nbsSffMsaNominalBitRate':nbsSffMsaNominalBitRate,'nbsSffMsaLinkLengthSmfKm':nbsSffMsaLinkLengthSmfKm,'nbsSffMsaLinkLengthSmf100m':nbsSffMsaLinkLengthSmf100m,'nbsSffMsaLinkLengthMmf10m':nbsSffMsaLinkLengthMmf10m,'nbsSffMsaLinkLength625Mmf10m':nbsSffMsaLinkLength625Mmf10m,'nbsSffMsaCopperLinkLength':nbsSffMsaCopperLinkLength,'nbsSffMsaVendorName':nbsSffMsaVendorName,'nbsSffMsaVendorOUI':nbsSffMsaVendorOUI,'nbsSffMsaVendorPartNumber':nbsSffMsaVendorPartNumber,'nbsSffMsaVendorRevision':nbsSffMsaVendorRevision,'nbsSffMsaBaseChecksumMatch':nbsSffMsaBaseChecksumMatch,'nbsSffMsaLossOfSignalImplemented':nbsSffMsaLossOfSignalImplemented,'nbsSffMsaLossOfSignalInverted':nbsSffMsaLossOfSignalInverted,'nbsSffMsaTxFault':nbsSffMsaTxFault,'nbsSffMsaTxDisable':nbsSffMsaTxDisable,'nbsSffMsaRateSelectImplemented':nbsSffMsaRateSelectImplemented,'nbsSffMsaMaxBitRate':nbsSffMsaMaxBitRate,'nbsSffMsaMinBitRate':nbsSffMsaMinBitRate,'nbsSffMsaVendorSerialNumber':nbsSffMsaVendorSerialNumber,'nbsSffMsaVendorDateCode':nbsSffMsaVendorDateCode,'nbsSffMsaExtChecksumMatch':nbsSffMsaExtChecksumMatch,'nbsSffWdmGrp':nbsSffWdmGrp,'nbsSffWdmTable':nbsSffWdmTable,'nbsSffWdmEntry':nbsSffWdmEntry,'nbsSffWdmClassOfPower':nbsSffWdmClassOfPower,'nbsSffWdmClassOfTemperature':nbsSffWdmClassOfTemperature,'nbsSffWdmClassOfWdm':nbsSffWdmClassOfWdm,'nbsSffWdmOpticalReach':nbsSffWdmOpticalReach,'nbsSffWdmMaxCaseTemperature':nbsSffWdmMaxCaseTemperature,'nbsSffWdmMinCaseTemperature':nbsSffWdmMinCaseTemperature,'nbsSffWdmMaxSupplyCurrent':nbsSffWdmMaxSupplyCurrent,'nbsSffWdmNumberOfChannels':nbsSffWdmNumberOfChannels,'nbsSffWdmChannelSpacing':nbsSffWdmChannelSpacing,'nbsSffWdmVariableDecisionThreshold':nbsSffWdmVariableDecisionThreshold,'nbsSffWdmWavelengthMonitorType':nbsSffWdmWavelengthMonitorType,'nbsSffWdmExtTransmitPowerType':nbsSffWdmExtTransmitPowerType,'nbsSffWdmVariableOpticalAttenuator':nbsSffWdmVariableOpticalAttenuator,'nbsSffWdmPilotToneFunctionality':nbsSffWdmPilotToneFunctionality,'nbsSffWdmOptionalInterruptPin':nbsSffWdmOptionalInterruptPin,'nbsSffWdmLaserWavelength':nbsSffWdmLaserWavelength,'nbsSffWdmFrequency':nbsSffWdmFrequency,'nbsSffWdmChannelBand':nbsSffWdmChannelBand,'nbsSffWdmChannelNumber':nbsSffWdmChannelNumber,'nbsSffDiagnosticsGrp':nbsSffDiagnosticsGrp,'nbsSffDiagsTable':nbsSffDiagsTable,'nbsSffDiagsEntry':nbsSffDiagsEntry,'nbsSffDiagsRateIdentifier':nbsSffDiagsRateIdentifier,'nbsSffDiagsLinkLengthOm3':nbsSffDiagsLinkLengthOm3,'nbsSffDiagsLaserWavelength':nbsSffDiagsLaserWavelength,'nbsSffDiagsLROutputImplemented':nbsSffDiagsLROutputImplemented,'nbsSffDiagsPowerLevelDeclaration':nbsSffDiagsPowerLevelDeclaration,'nbsSffDiagsCooledTranDeclaration':nbsSffDiagsCooledTranDeclaration,'nbsSffDiagsAddressChangeRequired':nbsSffDiagsAddressChangeRequired,'nbsSffDiagsPowerMeasurementType':nbsSffDiagsPowerMeasurementType,'nbsSffDiagsExternallyCalibrated':nbsSffDiagsExternallyCalibrated,'nbsSffDiagsInternallyCalibrated':nbsSffDiagsInternallyCalibrated,'nbsSffDiagsDDMonitoringImplemented':nbsSffDiagsDDMonitoringImplemented,'nbsSffDiagsOptRateSelectControl':nbsSffDiagsOptRateSelectControl,'nbsSffDiagsOptAppSelectControl':nbsSffDiagsOptAppSelectControl,'nbsSffDiagsOptSoftRSControlMon':nbsSffDiagsOptSoftRSControlMon,'nbsSffDiagsOptSoftRxLoSMonitoring':nbsSffDiagsOptSoftRxLoSMonitoring,'nbsSffDiagsOptSoftTxFaultMonitoring':nbsSffDiagsOptSoftTxFaultMonitoring,'nbsSffDiagsOptSoftTxDisable':nbsSffDiagsOptSoftTxDisable,'nbsSffDiagsOptAlarmWarningFlags':nbsSffDiagsOptAlarmWarningFlags,'nbsSffDiags8472Compliance':nbsSffDiags8472Compliance,'nbsSffDiagsTemperature':nbsSffDiagsTemperature,'nbsSffDiagsTempLowAlarm':nbsSffDiagsTempLowAlarm,'nbsSffDiagsTempLowWarn':nbsSffDiagsTempLowWarn,'nbsSffDiagsTempHighWarn':nbsSffDiagsTempHighWarn,'nbsSffDiagsTempHighAlarm':nbsSffDiagsTempHighAlarm,'nbsSffDiagsVoltage':nbsSffDiagsVoltage,'nbsSffDiagsVoltLowAlarm':nbsSffDiagsVoltLowAlarm,'nbsSffDiagsVoltLowWarn':nbsSffDiagsVoltLowWarn,'nbsSffDiagsVoltHighWarn':nbsSffDiagsVoltHighWarn,'nbsSffDiagsVoltHighAlarm':nbsSffDiagsVoltHighAlarm,'nbsSffDiagsBiasCurrent':nbsSffDiagsBiasCurrent,'nbsSffDiagsBiasLowAlarm':nbsSffDiagsBiasLowAlarm,'nbsSffDiagsBiasLowWarn':nbsSffDiagsBiasLowWarn,'nbsSffDiagsBiasHighWarn':nbsSffDiagsBiasHighWarn,'nbsSffDiagsBiasHighAlarm':nbsSffDiagsBiasHighAlarm,'nbsSffDiagsTxPower':nbsSffDiagsTxPower,'nbsSffDiagsTxPowerLowAlarm':nbsSffDiagsTxPowerLowAlarm,'nbsSffDiagsTxPowerLowWarn':nbsSffDiagsTxPowerLowWarn,'nbsSffDiagsTxPowerHighWarn':nbsSffDiagsTxPowerHighWarn,'nbsSffDiagsTxPowerHighAlarm':nbsSffDiagsTxPowerHighAlarm,'nbsSffDiagsRxPower':nbsSffDiagsRxPower,'nbsSffDiagsRxPowerLowAlarm':nbsSffDiagsRxPowerLowAlarm,'nbsSffDiagsRxPowerLowWarn':nbsSffDiagsRxPowerLowWarn,'nbsSffDiagsRxPowerHighWarn':nbsSffDiagsRxPowerHighWarn,'nbsSffDiagsRxPowerHighAlarm':nbsSffDiagsRxPowerHighAlarm,'nbsSffDiagsDataReadyBarState':nbsSffDiagsDataReadyBarState,'nbsSffDiagsRxLosState':nbsSffDiagsRxLosState,'nbsSffDiagsTxFaultState':nbsSffDiagsTxFaultState,'nbsSffDiagsSoftRateSelect':nbsSffDiagsSoftRateSelect,'nbsSffDiagsRateSelectState0':nbsSffDiagsRateSelectState0,'nbsSffDiagsRS1State':nbsSffDiagsRS1State,'nbsSffDiagsSoftTxDisableSelect':nbsSffDiagsSoftTxDisableSelect,'nbsSffDiagsTxDisableState':nbsSffDiagsTxDisableState,'nbsSffDiagsBiasCurrentSlope':nbsSffDiagsBiasCurrentSlope,'nbsSffDiagsBiasCurrentOffset':nbsSffDiagsBiasCurrentOffset,'nbsSffDiagsTxPowerSlope':nbsSffDiagsTxPowerSlope,'nbsSffDiagsTxPowerOffset':nbsSffDiagsTxPowerOffset,'nbsSffDiagsTemperatureSlope':nbsSffDiagsTemperatureSlope,'nbsSffDiagsTemperatureOffset':nbsSffDiagsTemperatureOffset,'nbsSffDiagsVoltageSlope':nbsSffDiagsVoltageSlope,'nbsSffDiagsVoltageOffset':nbsSffDiagsVoltageOffset,'nbsSffDiagsPowerLevelSelect':nbsSffDiagsPowerLevelSelect,'nbsSffDiagsPowerLevelOpState':nbsSffDiagsPowerLevelOpState,'nbsSffDiagsSoftRSSelect':nbsSffDiagsSoftRSSelect,'nbsSffMsxGrp':nbsSffMsxGrp,'nbsSffMsxTableSize':nbsSffMsxTableSize,'nbsSffMsxTable':nbsSffMsxTable,'nbsSffMsxEntry':nbsSffMsxEntry,_Q:nbsSffMsxPhysicalIfIndex,'nbsSffMsxHasSgmiiPhy':nbsSffMsxHasSgmiiPhy})