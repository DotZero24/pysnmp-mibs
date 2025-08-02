_A3='sfpEventGroup'
_A2='sfpInformationGroup'
_A1='sfpMIBObjectsGroup'
_A0='sfpNotificationsGroup'
_z='sfpCommandGroup'
_y='sfpEventRemoved'
_x='sfpEventInserted'
_w='sfpEventOperational'
_v='sfpEventFaulty'
_u='sfpNotificationEnable'
_t='sfpCommand'
_s='sfpVendorSpecificData'
_r='sfpVendorSpecificLotCode'
_q='sfpVendorDate'
_p='sfpBRMax'
_o='sfpBRMin'
_n='sfpOptions'
_m='sfpLaserWavelength'
_l='sfpVendorRev'
_k='sfpVendorSN'
_j='sfpVendorPN'
_i='sfpVendorOUI'
_h='sfpVendorName'
_g='sfpLengthCopperM'
_f='sfpLength62Pt5Mi10M'
_e='sfpLength50Mi10M'
_d='sfpLength9Mi100M'
_c='sfpLength9MiKm'
_b='sfpBRNominal100Mbps'
_a='sfpEncoding'
_Z='sfpFibreChannelTransmissionSpeed'
_Y='sfpFibreChannelTransmissionMedia'
_X='sfpFibreChannelTransmitterTechnology'
_W='sfpFibreChannelLinkLength'
_V='sfpTransceiverComplianceCodes'
_U='sfpVendorSpecificConnector'
_T='sfpConnector'
_S='sfpExtIdentifier'
_R='sfpVendorSpecificIdentifier'
_Q='sfpIdentifier'
_P='sfpCompatibleInterfaceCount'
_O='read-write'
_N='operational'
_M='faulty'
_L='10 Meters(M)'
_K='ifIndex'
_J='IF-MIB'
_I='DisplayString'
_H='sfpStatusCurrent'
_G='Integer32'
_F='OctetString'
_E='Bits'
_D='unknown'
_C='read-only'
_B='PDN-SFP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_J,_K)
pdn_ietf_drafts,=mibBuilder.importSymbols('PDN-HEADER-MIB','pdn-ietf-drafts')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_E,'Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_I,'PhysAddress','TextualConvention')
pdnSfp=ModuleIdentity((1,3,6,1,4,1,1795,2,24,14,3))
if mibBuilder.loadTexts:pdnSfp.setRevisions(('2003-04-23 00:00','2003-02-01 00:00'))
_SfpMIBObjects_ObjectIdentity=ObjectIdentity
sfpMIBObjects=_SfpMIBObjects_ObjectIdentity((1,3,6,1,4,1,1795,2,24,14,3,1))
_SfpCompatibleInterfaceCount_Type=Integer32
_SfpCompatibleInterfaceCount_Object=MibScalar
sfpCompatibleInterfaceCount=_SfpCompatibleInterfaceCount_Object((1,3,6,1,4,1,1795,2,24,14,3,1,1),_SfpCompatibleInterfaceCount_Type())
sfpCompatibleInterfaceCount.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpCompatibleInterfaceCount.setStatus(_A)
_SfpInfoTable_Object=MibTable
sfpInfoTable=_SfpInfoTable_Object((1,3,6,1,4,1,1795,2,24,14,3,1,2))
if mibBuilder.loadTexts:sfpInfoTable.setStatus(_A)
_SfpInfoEntry_Object=MibTableRow
sfpInfoEntry=_SfpInfoEntry_Object((1,3,6,1,4,1,1795,2,24,14,3,1,2,1))
sfpInfoEntry.setIndexNames((0,_J,_K))
if mibBuilder.loadTexts:sfpInfoEntry.setStatus(_A)
class _SfpIdentifier_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_D,1),('gbic',2),('fixed',3),('sfp',4),('other',5)))
_SfpIdentifier_Type.__name__=_G
_SfpIdentifier_Object=MibTableColumn
sfpIdentifier=_SfpIdentifier_Object((1,3,6,1,4,1,1795,2,24,14,3,1,2,1,1),_SfpIdentifier_Type())
sfpIdentifier.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpIdentifier.setStatus(_A)
class _SfpVendorSpecificIdentifier_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1));fixedLength=1
_SfpVendorSpecificIdentifier_Type.__name__=_F
_SfpVendorSpecificIdentifier_Object=MibTableColumn
sfpVendorSpecificIdentifier=_SfpVendorSpecificIdentifier_Object((1,3,6,1,4,1,1795,2,24,14,3,1,2,1,2),_SfpVendorSpecificIdentifier_Type())
sfpVendorSpecificIdentifier.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpVendorSpecificIdentifier.setStatus(_A)
class _SfpExtIdentifier_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),('simd',2)))
_SfpExtIdentifier_Type.__name__=_G
_SfpExtIdentifier_Object=MibTableColumn
sfpExtIdentifier=_SfpExtIdentifier_Object((1,3,6,1,4,1,1795,2,24,14,3,1,2,1,3),_SfpExtIdentifier_Type())
sfpExtIdentifier.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpExtIdentifier.setStatus(_A)
class _SfpConnector_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)));namedValues=NamedValues(*((_D,1),('sc',2),('fcscc1',3),('fcscc2',4),('bnctnc',5),('fcch',6),('fiberJack',7),('lc',8),('mtrj',9),('mu',10),('sg',11),('opticalPigtail',12),('hssdcii',13),('copperPigtail',14),('other',15)))
_SfpConnector_Type.__name__=_G
_SfpConnector_Object=MibTableColumn
sfpConnector=_SfpConnector_Object((1,3,6,1,4,1,1795,2,24,14,3,1,2,1,4),_SfpConnector_Type())
sfpConnector.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpConnector.setStatus(_A)
class _SfpVendorSpecificConnector_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1));fixedLength=1
_SfpVendorSpecificConnector_Type.__name__=_F
_SfpVendorSpecificConnector_Object=MibTableColumn
sfpVendorSpecificConnector=_SfpVendorSpecificConnector_Object((1,3,6,1,4,1,1795,2,24,14,3,1,2,1,5),_SfpVendorSpecificConnector_Type())
sfpVendorSpecificConnector.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpVendorSpecificConnector.setStatus(_A)
class _SfpTransceiverComplianceCodes_Type(Bits):namedValues=NamedValues(*((_D,0),('oc48LongReach1',1),('oc48LongReach2',2),('oc48LongReach3',3),('oc48IntermediateReach1',4),('oc48IntermediateReach2',5),('oc48ShortReach',6),('oc12SMLongReach1',7),('oc12SMLongReach2',8),('oc12SMLongReach3',9),('oc12SMIntermediateReach1',10),('oc12SMIntermediateReach2',11),('oc12MMShortReach',12),('oc3SMLongReach1',13),('oc3SMLongReach2',14),('oc3SMLongReach3',15),('oc3SMIntermediateReach1',16),('oc3SMIntermediateReach2',17),('oc3MMShortReach',18),('base1000T',19),('base1000CX',20),('base1000LX',21),('base1000SX',22),('sx1x',23),('lx1x',24),('copperActive1x',25),('copperPassive1x',26)))
_SfpTransceiverComplianceCodes_Type.__name__=_E
_SfpTransceiverComplianceCodes_Object=MibTableColumn
sfpTransceiverComplianceCodes=_SfpTransceiverComplianceCodes_Object((1,3,6,1,4,1,1795,2,24,14,3,1,2,1,6),_SfpTransceiverComplianceCodes_Type())
sfpTransceiverComplianceCodes.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpTransceiverComplianceCodes.setStatus(_A)
class _SfpFibreChannelLinkLength_Type(Bits):namedValues=NamedValues(*((_D,0),('veryLong',1),('short',2),('intermediate',3),('long',4)))
_SfpFibreChannelLinkLength_Type.__name__=_E
_SfpFibreChannelLinkLength_Object=MibTableColumn
sfpFibreChannelLinkLength=_SfpFibreChannelLinkLength_Object((1,3,6,1,4,1,1795,2,24,14,3,1,2,1,7),_SfpFibreChannelLinkLength_Type())
sfpFibreChannelLinkLength.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpFibreChannelLinkLength.setStatus(_A)
class _SfpFibreChannelTransmitterTechnology_Type(Bits):namedValues=NamedValues(*((_D,0),('lc',1),('el1',2),('el2',3),('sn',4),('sl',5),('ll',6)))
_SfpFibreChannelTransmitterTechnology_Type.__name__=_E
_SfpFibreChannelTransmitterTechnology_Object=MibTableColumn
sfpFibreChannelTransmitterTechnology=_SfpFibreChannelTransmitterTechnology_Object((1,3,6,1,4,1,1795,2,24,14,3,1,2,1,8),_SfpFibreChannelTransmitterTechnology_Type())
sfpFibreChannelTransmitterTechnology.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpFibreChannelTransmitterTechnology.setStatus(_A)
class _SfpFibreChannelTransmissionMedia_Type(Bits):namedValues=NamedValues(*((_D,0),('tw',1),('tp',2),('mi',3),('tv',4),('m6',5),('m5',6),('sm',7)))
_SfpFibreChannelTransmissionMedia_Type.__name__=_E
_SfpFibreChannelTransmissionMedia_Object=MibTableColumn
sfpFibreChannelTransmissionMedia=_SfpFibreChannelTransmissionMedia_Object((1,3,6,1,4,1,1795,2,24,14,3,1,2,1,9),_SfpFibreChannelTransmissionMedia_Type())
sfpFibreChannelTransmissionMedia.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpFibreChannelTransmissionMedia.setStatus(_A)
class _SfpFibreChannelTransmissionSpeed_Type(Bits):namedValues=NamedValues(*((_D,0),('mbps400',1),('mbps200',2),('mbps100',3)))
_SfpFibreChannelTransmissionSpeed_Type.__name__=_E
_SfpFibreChannelTransmissionSpeed_Object=MibTableColumn
sfpFibreChannelTransmissionSpeed=_SfpFibreChannelTransmissionSpeed_Object((1,3,6,1,4,1,1795,2,24,14,3,1,2,1,10),_SfpFibreChannelTransmissionSpeed_Type())
sfpFibreChannelTransmissionSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpFibreChannelTransmissionSpeed.setStatus(_A)
class _SfpEncoding_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_D,1),('b8b10',2),('b4b5',3),('nrz',4),('manchester',5),('sonetScrambled',6)))
_SfpEncoding_Type.__name__=_G
_SfpEncoding_Object=MibTableColumn
sfpEncoding=_SfpEncoding_Object((1,3,6,1,4,1,1795,2,24,14,3,1,2,1,11),_SfpEncoding_Type())
sfpEncoding.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpEncoding.setStatus(_A)
_SfpBRNominal100Mbps_Type=Integer32
_SfpBRNominal100Mbps_Object=MibTableColumn
sfpBRNominal100Mbps=_SfpBRNominal100Mbps_Object((1,3,6,1,4,1,1795,2,24,14,3,1,2,1,12),_SfpBRNominal100Mbps_Type())
sfpBRNominal100Mbps.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpBRNominal100Mbps.setStatus(_A)
if mibBuilder.loadTexts:sfpBRNominal100Mbps.setUnits('100 Megabits per second (Mbps)')
_SfpLength9MiKm_Type=Integer32
_SfpLength9MiKm_Object=MibTableColumn
sfpLength9MiKm=_SfpLength9MiKm_Object((1,3,6,1,4,1,1795,2,24,14,3,1,2,1,13),_SfpLength9MiKm_Type())
sfpLength9MiKm.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpLength9MiKm.setStatus(_A)
if mibBuilder.loadTexts:sfpLength9MiKm.setUnits('Kilometer(Km)')
_SfpLength9Mi100M_Type=Integer32
_SfpLength9Mi100M_Object=MibTableColumn
sfpLength9Mi100M=_SfpLength9Mi100M_Object((1,3,6,1,4,1,1795,2,24,14,3,1,2,1,14),_SfpLength9Mi100M_Type())
sfpLength9Mi100M.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpLength9Mi100M.setStatus(_A)
if mibBuilder.loadTexts:sfpLength9Mi100M.setUnits('100 Meters(M)')
_SfpLength50Mi10M_Type=Integer32
_SfpLength50Mi10M_Object=MibTableColumn
sfpLength50Mi10M=_SfpLength50Mi10M_Object((1,3,6,1,4,1,1795,2,24,14,3,1,2,1,15),_SfpLength50Mi10M_Type())
sfpLength50Mi10M.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpLength50Mi10M.setStatus(_A)
if mibBuilder.loadTexts:sfpLength50Mi10M.setUnits(_L)
_SfpLength62Pt5Mi10M_Type=Integer32
_SfpLength62Pt5Mi10M_Object=MibTableColumn
sfpLength62Pt5Mi10M=_SfpLength62Pt5Mi10M_Object((1,3,6,1,4,1,1795,2,24,14,3,1,2,1,16),_SfpLength62Pt5Mi10M_Type())
sfpLength62Pt5Mi10M.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpLength62Pt5Mi10M.setStatus(_A)
if mibBuilder.loadTexts:sfpLength62Pt5Mi10M.setUnits(_L)
_SfpLengthCopperM_Type=Integer32
_SfpLengthCopperM_Object=MibTableColumn
sfpLengthCopperM=_SfpLengthCopperM_Object((1,3,6,1,4,1,1795,2,24,14,3,1,2,1,17),_SfpLengthCopperM_Type())
sfpLengthCopperM.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpLengthCopperM.setStatus(_A)
if mibBuilder.loadTexts:sfpLengthCopperM.setUnits('1 Meter(M)')
class _SfpVendorName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_SfpVendorName_Type.__name__=_I
_SfpVendorName_Object=MibTableColumn
sfpVendorName=_SfpVendorName_Object((1,3,6,1,4,1,1795,2,24,14,3,1,2,1,18),_SfpVendorName_Type())
sfpVendorName.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpVendorName.setStatus(_A)
class _SfpVendorOUI_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,3));fixedLength=3
_SfpVendorOUI_Type.__name__=_F
_SfpVendorOUI_Object=MibTableColumn
sfpVendorOUI=_SfpVendorOUI_Object((1,3,6,1,4,1,1795,2,24,14,3,1,2,1,19),_SfpVendorOUI_Type())
sfpVendorOUI.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpVendorOUI.setStatus(_A)
class _SfpVendorPN_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_SfpVendorPN_Type.__name__=_I
_SfpVendorPN_Object=MibTableColumn
sfpVendorPN=_SfpVendorPN_Object((1,3,6,1,4,1,1795,2,24,14,3,1,2,1,20),_SfpVendorPN_Type())
sfpVendorPN.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpVendorPN.setStatus(_A)
class _SfpVendorSN_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_SfpVendorSN_Type.__name__=_I
_SfpVendorSN_Object=MibTableColumn
sfpVendorSN=_SfpVendorSN_Object((1,3,6,1,4,1,1795,2,24,14,3,1,2,1,21),_SfpVendorSN_Type())
sfpVendorSN.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpVendorSN.setStatus(_A)
class _SfpVendorRev_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,4))
_SfpVendorRev_Type.__name__=_I
_SfpVendorRev_Object=MibTableColumn
sfpVendorRev=_SfpVendorRev_Object((1,3,6,1,4,1,1795,2,24,14,3,1,2,1,22),_SfpVendorRev_Type())
sfpVendorRev.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpVendorRev.setStatus(_A)
_SfpLaserWavelength_Type=Integer32
_SfpLaserWavelength_Object=MibTableColumn
sfpLaserWavelength=_SfpLaserWavelength_Object((1,3,6,1,4,1,1795,2,24,14,3,1,2,1,23),_SfpLaserWavelength_Type())
sfpLaserWavelength.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpLaserWavelength.setStatus(_A)
if mibBuilder.loadTexts:sfpLaserWavelength.setUnits('Nano Meter(NM)')
class _SfpOptions_Type(Bits):namedValues=NamedValues(*((_D,0),('rateSelect',1),('txDisable',2),('txFault',3),('losInverted',4),('losNormal',5)))
_SfpOptions_Type.__name__=_E
_SfpOptions_Object=MibTableColumn
sfpOptions=_SfpOptions_Object((1,3,6,1,4,1,1795,2,24,14,3,1,2,1,24),_SfpOptions_Type())
sfpOptions.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpOptions.setStatus(_A)
_SfpBRMin_Type=Integer32
_SfpBRMin_Object=MibTableColumn
sfpBRMin=_SfpBRMin_Object((1,3,6,1,4,1,1795,2,24,14,3,1,2,1,25),_SfpBRMin_Type())
sfpBRMin.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpBRMin.setStatus(_A)
if mibBuilder.loadTexts:sfpBRMin.setUnits('percent below sfpBRNominal')
_SfpBRMax_Type=Integer32
_SfpBRMax_Object=MibTableColumn
sfpBRMax=_SfpBRMax_Object((1,3,6,1,4,1,1795,2,24,14,3,1,2,1,26),_SfpBRMax_Type())
sfpBRMax.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpBRMax.setStatus(_A)
if mibBuilder.loadTexts:sfpBRMax.setUnits('percent above sfpBRNominal')
_SfpVendorDate_Type=DateAndTime
_SfpVendorDate_Object=MibTableColumn
sfpVendorDate=_SfpVendorDate_Object((1,3,6,1,4,1,1795,2,24,14,3,1,2,1,27),_SfpVendorDate_Type())
sfpVendorDate.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpVendorDate.setStatus(_A)
class _SfpVendorSpecificLotCode_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_SfpVendorSpecificLotCode_Type.__name__=_F
_SfpVendorSpecificLotCode_Object=MibTableColumn
sfpVendorSpecificLotCode=_SfpVendorSpecificLotCode_Object((1,3,6,1,4,1,1795,2,24,14,3,1,2,1,28),_SfpVendorSpecificLotCode_Type())
sfpVendorSpecificLotCode.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpVendorSpecificLotCode.setStatus(_A)
class _SfpVendorSpecificData_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SfpVendorSpecificData_Type.__name__=_F
_SfpVendorSpecificData_Object=MibTableColumn
sfpVendorSpecificData=_SfpVendorSpecificData_Object((1,3,6,1,4,1,1795,2,24,14,3,1,2,1,29),_SfpVendorSpecificData_Type())
sfpVendorSpecificData.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpVendorSpecificData.setStatus(_A)
class _SfpStatusCurrent_Type(Bits):namedValues=NamedValues(*((_D,0),('notInstalled',1),('installed',2),(_M,3),(_N,4),('enabled',5),('disabled',6),('inValidCCBase',7),('inValidCCExt',8)))
_SfpStatusCurrent_Type.__name__=_E
_SfpStatusCurrent_Object=MibTableColumn
sfpStatusCurrent=_SfpStatusCurrent_Object((1,3,6,1,4,1,1795,2,24,14,3,1,2,1,30),_SfpStatusCurrent_Type())
sfpStatusCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpStatusCurrent.setStatus(_A)
_SfpCommandTable_Object=MibTable
sfpCommandTable=_SfpCommandTable_Object((1,3,6,1,4,1,1795,2,24,14,3,1,3))
if mibBuilder.loadTexts:sfpCommandTable.setStatus(_A)
_SfpCommandEntry_Object=MibTableRow
sfpCommandEntry=_SfpCommandEntry_Object((1,3,6,1,4,1,1795,2,24,14,3,1,3,1))
sfpCommandEntry.setIndexNames((0,_J,_K))
if mibBuilder.loadTexts:sfpCommandEntry.setStatus(_A)
class _SfpCommand_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('noCmd',1),('enable',2),('disable',3),('reset',4)))
_SfpCommand_Type.__name__=_G
_SfpCommand_Object=MibTableColumn
sfpCommand=_SfpCommand_Object((1,3,6,1,4,1,1795,2,24,14,3,1,3,1,1),_SfpCommand_Type())
sfpCommand.setMaxAccess(_O)
if mibBuilder.loadTexts:sfpCommand.setStatus(_A)
class _SfpNotificationEnable_Type(Bits):defaultBinValue='0';namedValues=NamedValues(*((_M,0),(_N,1),('inserted',2),('removed',3)))
_SfpNotificationEnable_Type.__name__=_E
_SfpNotificationEnable_Object=MibScalar
sfpNotificationEnable=_SfpNotificationEnable_Object((1,3,6,1,4,1,1795,2,24,14,3,1,4),_SfpNotificationEnable_Type())
sfpNotificationEnable.setMaxAccess(_O)
if mibBuilder.loadTexts:sfpNotificationEnable.setStatus(_A)
_SfpMIBNotifications_ObjectIdentity=ObjectIdentity
sfpMIBNotifications=_SfpMIBNotifications_ObjectIdentity((1,3,6,1,4,1,1795,2,24,14,3,2))
_SfpNotificationsPrefix_ObjectIdentity=ObjectIdentity
sfpNotificationsPrefix=_SfpNotificationsPrefix_ObjectIdentity((1,3,6,1,4,1,1795,2,24,14,3,2,0))
_SfpMIBConformance_ObjectIdentity=ObjectIdentity
sfpMIBConformance=_SfpMIBConformance_ObjectIdentity((1,3,6,1,4,1,1795,2,24,14,3,3))
_SfpGroups_ObjectIdentity=ObjectIdentity
sfpGroups=_SfpGroups_ObjectIdentity((1,3,6,1,4,1,1795,2,24,14,3,3,1))
_SfpCompliances_ObjectIdentity=ObjectIdentity
sfpCompliances=_SfpCompliances_ObjectIdentity((1,3,6,1,4,1,1795,2,24,14,3,3,2))
sfpMIBObjectsGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,14,3,3,1,1))
sfpMIBObjectsGroup.setObjects((_B,_P))
if mibBuilder.loadTexts:sfpMIBObjectsGroup.setStatus(_A)
sfpInformationGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,14,3,3,1,2))
sfpInformationGroup.setObjects(*((_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_H)))
if mibBuilder.loadTexts:sfpInformationGroup.setStatus(_A)
sfpCommandGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,14,3,3,1,3))
sfpCommandGroup.setObjects((_B,_t))
if mibBuilder.loadTexts:sfpCommandGroup.setStatus(_A)
sfpNotificationsGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,14,3,3,1,4))
sfpNotificationsGroup.setObjects((_B,_u))
if mibBuilder.loadTexts:sfpNotificationsGroup.setStatus(_A)
sfpEventFaulty=NotificationType((1,3,6,1,4,1,1795,2,24,14,3,2,0,1))
sfpEventFaulty.setObjects((_B,_H))
if mibBuilder.loadTexts:sfpEventFaulty.setStatus(_A)
sfpEventOperational=NotificationType((1,3,6,1,4,1,1795,2,24,14,3,2,0,2))
sfpEventOperational.setObjects((_B,_H))
if mibBuilder.loadTexts:sfpEventOperational.setStatus(_A)
sfpEventInserted=NotificationType((1,3,6,1,4,1,1795,2,24,14,3,2,0,3))
sfpEventInserted.setObjects((_B,_H))
if mibBuilder.loadTexts:sfpEventInserted.setStatus(_A)
sfpEventRemoved=NotificationType((1,3,6,1,4,1,1795,2,24,14,3,2,0,4))
sfpEventRemoved.setObjects((_B,_H))
if mibBuilder.loadTexts:sfpEventRemoved.setStatus(_A)
sfpEventGroup=NotificationGroup((1,3,6,1,4,1,1795,2,24,14,3,3,1,5))
sfpEventGroup.setObjects(*((_B,_v),(_B,_w),(_B,_x),(_B,_y)))
if mibBuilder.loadTexts:sfpEventGroup.setStatus(_A)
sfpReadWriteCompliance=ModuleCompliance((1,3,6,1,4,1,1795,2,24,14,3,3,2,1))
sfpReadWriteCompliance.setObjects(*((_B,_z),(_B,_A0)))
if mibBuilder.loadTexts:sfpReadWriteCompliance.setStatus(_A)
sfpReadOnlyCompliance=ModuleCompliance((1,3,6,1,4,1,1795,2,24,14,3,3,2,2))
sfpReadOnlyCompliance.setObjects(*((_B,_A1),(_B,_A2)))
if mibBuilder.loadTexts:sfpReadOnlyCompliance.setStatus(_A)
sfpNotificationCompliance=ModuleCompliance((1,3,6,1,4,1,1795,2,24,14,3,3,2,3))
sfpNotificationCompliance.setObjects((_B,_A3))
if mibBuilder.loadTexts:sfpNotificationCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'pdnSfp':pdnSfp,'sfpMIBObjects':sfpMIBObjects,_P:sfpCompatibleInterfaceCount,'sfpInfoTable':sfpInfoTable,'sfpInfoEntry':sfpInfoEntry,_Q:sfpIdentifier,_R:sfpVendorSpecificIdentifier,_S:sfpExtIdentifier,_T:sfpConnector,_U:sfpVendorSpecificConnector,_V:sfpTransceiverComplianceCodes,_W:sfpFibreChannelLinkLength,_X:sfpFibreChannelTransmitterTechnology,_Y:sfpFibreChannelTransmissionMedia,_Z:sfpFibreChannelTransmissionSpeed,_a:sfpEncoding,_b:sfpBRNominal100Mbps,_c:sfpLength9MiKm,_d:sfpLength9Mi100M,_e:sfpLength50Mi10M,_f:sfpLength62Pt5Mi10M,_g:sfpLengthCopperM,_h:sfpVendorName,_i:sfpVendorOUI,_j:sfpVendorPN,_k:sfpVendorSN,_l:sfpVendorRev,_m:sfpLaserWavelength,_n:sfpOptions,_o:sfpBRMin,_p:sfpBRMax,_q:sfpVendorDate,_r:sfpVendorSpecificLotCode,_s:sfpVendorSpecificData,_H:sfpStatusCurrent,'sfpCommandTable':sfpCommandTable,'sfpCommandEntry':sfpCommandEntry,_t:sfpCommand,_u:sfpNotificationEnable,'sfpMIBNotifications':sfpMIBNotifications,'sfpNotificationsPrefix':sfpNotificationsPrefix,_v:sfpEventFaulty,_w:sfpEventOperational,_x:sfpEventInserted,_y:sfpEventRemoved,'sfpMIBConformance':sfpMIBConformance,'sfpGroups':sfpGroups,_A1:sfpMIBObjectsGroup,_A2:sfpInformationGroup,_z:sfpCommandGroup,_A0:sfpNotificationsGroup,_A3:sfpEventGroup,'sfpCompliances':sfpCompliances,'sfpReadWriteCompliance':sfpReadWriteCompliance,'sfpReadOnlyCompliance':sfpReadOnlyCompliance,'sfpNotificationCompliance':sfpNotificationCompliance})