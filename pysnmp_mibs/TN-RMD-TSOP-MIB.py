_K='tnRmdIfIndex'
_J='TN-RMD-IF-MIB'
_I='tnRmdTsopIwfChannelNumber'
_H='TN-RMD-TSOP-MIB'
_G='tnSysSwitchId'
_F='TROPIC-SYSTEM-MIB'
_E='tnRmdSystemId'
_D='TN-RMD-SYSTEM-MIB'
_C='read-only'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention','TruthValue')
tnRmdIfIndex,=mibBuilder.importSymbols(_J,_K)
tnRmdSystemId,=mibBuilder.importSymbols(_D,_E)
TnRmdUserLabel,=mibBuilder.importSymbols('TN-RMD-TC-MIB','TnRmdUserLabel')
tnRmdMIBModules,tnRmdObjs=mibBuilder.importSymbols('TROPIC-GLOBAL-REG','tnRmdMIBModules','tnRmdObjs')
tnSysSwitchId,=mibBuilder.importSymbols(_F,_G)
tnRmdTsopMibModule=ModuleIdentity((1,3,6,1,4,1,7483,5,1,4,6))
if mibBuilder.loadTexts:tnRmdTsopMibModule.setRevisions(('2018-02-23 12:00','2016-11-16 00:00','2013-11-16 00:00','2013-08-01 00:00'))
class TnRmdIwfChannelNumber(TextualConvention,Unsigned32):status=_A
class TnRmdIwfTimingMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,255)));namedValues=NamedValues(*(('iwfReTiming',1),('iwfLoopTiming',2),('iwfDifferentialTiming',3),('iwfTimingNotApplicable',255)))
class TnRmdRtpClockSource(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('rtpClockEthernet',1),('rtpClockTdm',2)))
class TnRmdRtpFrequency(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('rtpFreq19MHz',1),('rtpFreq25MHz',2)))
class TnRmdTdmLoopbackType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('transparantLoop',1),('nonTransparantLoop',2)))
class TnRmdTsopJbObservationPeriod(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,254,255)));namedValues=NamedValues(*(('period1min',1),('period2min',2),('period5min',3),('period10min',4),('periodNotAvailable',254),('periodNotApplicable',255)))
_TnRmdTsopObjects_ObjectIdentity=ObjectIdentity
tnRmdTsopObjects=_TnRmdTsopObjects_ObjectIdentity((1,3,6,1,4,1,7483,6,4,1,6))
_TnRmdTsopAttributeTotal_Type=Integer32
_TnRmdTsopAttributeTotal_Object=MibScalar
tnRmdTsopAttributeTotal=_TnRmdTsopAttributeTotal_Object((1,3,6,1,4,1,7483,6,4,1,6,1),_TnRmdTsopAttributeTotal_Type())
tnRmdTsopAttributeTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:tnRmdTsopAttributeTotal.setStatus(_A)
_TnRmdTsopSystemTable_Object=MibTable
tnRmdTsopSystemTable=_TnRmdTsopSystemTable_Object((1,3,6,1,4,1,7483,6,4,1,6,2))
if mibBuilder.loadTexts:tnRmdTsopSystemTable.setStatus(_A)
_TnRmdTsopSystemEntry_Object=MibTableRow
tnRmdTsopSystemEntry=_TnRmdTsopSystemEntry_Object((1,3,6,1,4,1,7483,6,4,1,6,2,1))
tnRmdTsopSystemEntry.setIndexNames((0,_F,_G),(0,_D,_E))
if mibBuilder.loadTexts:tnRmdTsopSystemEntry.setStatus(_A)
_TnRmdTsopSystemMaxNrChannels_Type=Unsigned32
_TnRmdTsopSystemMaxNrChannels_Object=MibTableColumn
tnRmdTsopSystemMaxNrChannels=_TnRmdTsopSystemMaxNrChannels_Object((1,3,6,1,4,1,7483,6,4,1,6,2,1,1),_TnRmdTsopSystemMaxNrChannels_Type())
tnRmdTsopSystemMaxNrChannels.setMaxAccess(_C)
if mibBuilder.loadTexts:tnRmdTsopSystemMaxNrChannels.setStatus(_A)
_TnRmdTsopSystemMaxJbSize_Type=Unsigned32
_TnRmdTsopSystemMaxJbSize_Object=MibTableColumn
tnRmdTsopSystemMaxJbSize=_TnRmdTsopSystemMaxJbSize_Object((1,3,6,1,4,1,7483,6,4,1,6,2,1,2),_TnRmdTsopSystemMaxJbSize_Type())
tnRmdTsopSystemMaxJbSize.setMaxAccess(_C)
if mibBuilder.loadTexts:tnRmdTsopSystemMaxJbSize.setStatus(_A)
_TnRmdTsopIwfTable_Object=MibTable
tnRmdTsopIwfTable=_TnRmdTsopIwfTable_Object((1,3,6,1,4,1,7483,6,4,1,6,3))
if mibBuilder.loadTexts:tnRmdTsopIwfTable.setStatus(_A)
_TnRmdTsopIwfEntry_Object=MibTableRow
tnRmdTsopIwfEntry=_TnRmdTsopIwfEntry_Object((1,3,6,1,4,1,7483,6,4,1,6,3,1))
tnRmdTsopIwfEntry.setIndexNames((0,_F,_G),(0,_D,_E),(0,_H,_I))
if mibBuilder.loadTexts:tnRmdTsopIwfEntry.setStatus(_A)
_TnRmdTsopIwfChannelNumber_Type=TnRmdIwfChannelNumber
_TnRmdTsopIwfChannelNumber_Object=MibTableColumn
tnRmdTsopIwfChannelNumber=_TnRmdTsopIwfChannelNumber_Object((1,3,6,1,4,1,7483,6,4,1,6,3,1,1),_TnRmdTsopIwfChannelNumber_Type())
tnRmdTsopIwfChannelNumber.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:tnRmdTsopIwfChannelNumber.setStatus(_A)
_TnRmdTsopIwfUserLabel_Type=TnRmdUserLabel
_TnRmdTsopIwfUserLabel_Object=MibTableColumn
tnRmdTsopIwfUserLabel=_TnRmdTsopIwfUserLabel_Object((1,3,6,1,4,1,7483,6,4,1,6,3,1,2),_TnRmdTsopIwfUserLabel_Type())
tnRmdTsopIwfUserLabel.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdTsopIwfUserLabel.setStatus(_A)
_TnRmdTsopIwfEncapTable_Object=MibTable
tnRmdTsopIwfEncapTable=_TnRmdTsopIwfEncapTable_Object((1,3,6,1,4,1,7483,6,4,1,6,4))
if mibBuilder.loadTexts:tnRmdTsopIwfEncapTable.setStatus(_A)
_TnRmdTsopIwfEncapEntry_Object=MibTableRow
tnRmdTsopIwfEncapEntry=_TnRmdTsopIwfEncapEntry_Object((1,3,6,1,4,1,7483,6,4,1,6,4,1))
tnRmdTsopIwfEncapEntry.setIndexNames((0,_F,_G),(0,_D,_E),(0,_H,_I))
if mibBuilder.loadTexts:tnRmdTsopIwfEncapEntry.setStatus(_A)
_TnRmdTsopIwfEncapOutput_Type=TruthValue
_TnRmdTsopIwfEncapOutput_Object=MibTableColumn
tnRmdTsopIwfEncapOutput=_TnRmdTsopIwfEncapOutput_Object((1,3,6,1,4,1,7483,6,4,1,6,4,1,1),_TnRmdTsopIwfEncapOutput_Type())
tnRmdTsopIwfEncapOutput.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdTsopIwfEncapOutput.setStatus(_A)
_TnRmdTsopIwfEncapGAisActive_Type=TruthValue
_TnRmdTsopIwfEncapGAisActive_Object=MibTableColumn
tnRmdTsopIwfEncapGAisActive=_TnRmdTsopIwfEncapGAisActive_Object((1,3,6,1,4,1,7483,6,4,1,6,4,1,2),_TnRmdTsopIwfEncapGAisActive_Type())
tnRmdTsopIwfEncapGAisActive.setMaxAccess(_C)
if mibBuilder.loadTexts:tnRmdTsopIwfEncapGAisActive.setStatus(_A)
_TnRmdTsopIwfEncapGAisIncludeLos_Type=TruthValue
_TnRmdTsopIwfEncapGAisIncludeLos_Object=MibTableColumn
tnRmdTsopIwfEncapGAisIncludeLos=_TnRmdTsopIwfEncapGAisIncludeLos_Object((1,3,6,1,4,1,7483,6,4,1,6,4,1,3),_TnRmdTsopIwfEncapGAisIncludeLos_Type())
tnRmdTsopIwfEncapGAisIncludeLos.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdTsopIwfEncapGAisIncludeLos.setStatus(_A)
_TnRmdTsopIwfEncapGAisIncludeLof_Type=TruthValue
_TnRmdTsopIwfEncapGAisIncludeLof_Object=MibTableColumn
tnRmdTsopIwfEncapGAisIncludeLof=_TnRmdTsopIwfEncapGAisIncludeLof_Object((1,3,6,1,4,1,7483,6,4,1,6,4,1,4),_TnRmdTsopIwfEncapGAisIncludeLof_Type())
tnRmdTsopIwfEncapGAisIncludeLof.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdTsopIwfEncapGAisIncludeLof.setStatus(_A)
_TnRmdTsopIwfEncapEcid_Type=Unsigned32
_TnRmdTsopIwfEncapEcid_Object=MibTableColumn
tnRmdTsopIwfEncapEcid=_TnRmdTsopIwfEncapEcid_Object((1,3,6,1,4,1,7483,6,4,1,6,4,1,5),_TnRmdTsopIwfEncapEcid_Type())
tnRmdTsopIwfEncapEcid.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdTsopIwfEncapEcid.setStatus(_A)
_TnRmdTsopIwfEncapInsertRtpHeader_Type=TruthValue
_TnRmdTsopIwfEncapInsertRtpHeader_Object=MibTableColumn
tnRmdTsopIwfEncapInsertRtpHeader=_TnRmdTsopIwfEncapInsertRtpHeader_Object((1,3,6,1,4,1,7483,6,4,1,6,4,1,6),_TnRmdTsopIwfEncapInsertRtpHeader_Type())
tnRmdTsopIwfEncapInsertRtpHeader.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdTsopIwfEncapInsertRtpHeader.setStatus(_A)
_TnRmdTsopIwfEncapRtpClockSource_Type=TnRmdRtpClockSource
_TnRmdTsopIwfEncapRtpClockSource_Object=MibTableColumn
tnRmdTsopIwfEncapRtpClockSource=_TnRmdTsopIwfEncapRtpClockSource_Object((1,3,6,1,4,1,7483,6,4,1,6,4,1,7),_TnRmdTsopIwfEncapRtpClockSource_Type())
tnRmdTsopIwfEncapRtpClockSource.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdTsopIwfEncapRtpClockSource.setStatus(_A)
_TnRmdTsopIwfEncapRtpFrequency_Type=TnRmdRtpFrequency
_TnRmdTsopIwfEncapRtpFrequency_Object=MibTableColumn
tnRmdTsopIwfEncapRtpFrequency=_TnRmdTsopIwfEncapRtpFrequency_Object((1,3,6,1,4,1,7483,6,4,1,6,4,1,8),_TnRmdTsopIwfEncapRtpFrequency_Type())
tnRmdTsopIwfEncapRtpFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdTsopIwfEncapRtpFrequency.setStatus(_A)
_TnRmdTsopIwfEncapRtpPayloadType_Type=Unsigned32
_TnRmdTsopIwfEncapRtpPayloadType_Object=MibTableColumn
tnRmdTsopIwfEncapRtpPayloadType=_TnRmdTsopIwfEncapRtpPayloadType_Object((1,3,6,1,4,1,7483,6,4,1,6,4,1,9),_TnRmdTsopIwfEncapRtpPayloadType_Type())
tnRmdTsopIwfEncapRtpPayloadType.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdTsopIwfEncapRtpPayloadType.setStatus(_A)
_TnRmdTsopIwfEncapRtpSsrc_Type=Unsigned32
_TnRmdTsopIwfEncapRtpSsrc_Object=MibTableColumn
tnRmdTsopIwfEncapRtpSsrc=_TnRmdTsopIwfEncapRtpSsrc_Object((1,3,6,1,4,1,7483,6,4,1,6,4,1,10),_TnRmdTsopIwfEncapRtpSsrc_Type())
tnRmdTsopIwfEncapRtpSsrc.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdTsopIwfEncapRtpSsrc.setStatus(_A)
_TnRmdTsopIwfDecapTable_Object=MibTable
tnRmdTsopIwfDecapTable=_TnRmdTsopIwfDecapTable_Object((1,3,6,1,4,1,7483,6,4,1,6,5))
if mibBuilder.loadTexts:tnRmdTsopIwfDecapTable.setStatus(_A)
_TnRmdTsopIwfDecapEntry_Object=MibTableRow
tnRmdTsopIwfDecapEntry=_TnRmdTsopIwfDecapEntry_Object((1,3,6,1,4,1,7483,6,4,1,6,5,1))
tnRmdTsopIwfDecapEntry.setIndexNames((0,_F,_G),(0,_D,_E),(0,_H,_I))
if mibBuilder.loadTexts:tnRmdTsopIwfDecapEntry.setStatus(_A)
_TnRmdTsopIwfDecapExpectedEcid_Type=Unsigned32
_TnRmdTsopIwfDecapExpectedEcid_Object=MibTableColumn
tnRmdTsopIwfDecapExpectedEcid=_TnRmdTsopIwfDecapExpectedEcid_Object((1,3,6,1,4,1,7483,6,4,1,6,5,1,1),_TnRmdTsopIwfDecapExpectedEcid_Type())
tnRmdTsopIwfDecapExpectedEcid.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdTsopIwfDecapExpectedEcid.setStatus(_A)
_TnRmdTsopIwfDecapUnknownEcid_Type=Unsigned32
_TnRmdTsopIwfDecapUnknownEcid_Object=MibTableColumn
tnRmdTsopIwfDecapUnknownEcid=_TnRmdTsopIwfDecapUnknownEcid_Object((1,3,6,1,4,1,7483,6,4,1,6,5,1,2),_TnRmdTsopIwfDecapUnknownEcid_Type())
tnRmdTsopIwfDecapUnknownEcid.setMaxAccess(_C)
if mibBuilder.loadTexts:tnRmdTsopIwfDecapUnknownEcid.setStatus(_A)
_TnRmdTsopIwfDecapTimingMode_Type=TnRmdIwfTimingMode
_TnRmdTsopIwfDecapTimingMode_Object=MibTableColumn
tnRmdTsopIwfDecapTimingMode=_TnRmdTsopIwfDecapTimingMode_Object((1,3,6,1,4,1,7483,6,4,1,6,5,1,3),_TnRmdTsopIwfDecapTimingMode_Type())
tnRmdTsopIwfDecapTimingMode.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdTsopIwfDecapTimingMode.setStatus(_A)
_TnRmdTsopIwfDecapRaiseThreshold_Type=Unsigned32
_TnRmdTsopIwfDecapRaiseThreshold_Object=MibTableColumn
tnRmdTsopIwfDecapRaiseThreshold=_TnRmdTsopIwfDecapRaiseThreshold_Object((1,3,6,1,4,1,7483,6,4,1,6,5,1,4),_TnRmdTsopIwfDecapRaiseThreshold_Type())
tnRmdTsopIwfDecapRaiseThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdTsopIwfDecapRaiseThreshold.setStatus(_A)
_TnRmdTsopIwfDecapClearThreshold_Type=Unsigned32
_TnRmdTsopIwfDecapClearThreshold_Object=MibTableColumn
tnRmdTsopIwfDecapClearThreshold=_TnRmdTsopIwfDecapClearThreshold_Object((1,3,6,1,4,1,7483,6,4,1,6,5,1,5),_TnRmdTsopIwfDecapClearThreshold_Type())
tnRmdTsopIwfDecapClearThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdTsopIwfDecapClearThreshold.setStatus(_A)
_TnRmdTsopIwfDecapGAisActive_Type=TruthValue
_TnRmdTsopIwfDecapGAisActive_Object=MibTableColumn
tnRmdTsopIwfDecapGAisActive=_TnRmdTsopIwfDecapGAisActive_Object((1,3,6,1,4,1,7483,6,4,1,6,5,1,6),_TnRmdTsopIwfDecapGAisActive_Type())
tnRmdTsopIwfDecapGAisActive.setMaxAccess(_C)
if mibBuilder.loadTexts:tnRmdTsopIwfDecapGAisActive.setStatus(_A)
_TnRmdTsopIwfDecapGAis_Type=TruthValue
_TnRmdTsopIwfDecapGAis_Object=MibTableColumn
tnRmdTsopIwfDecapGAis=_TnRmdTsopIwfDecapGAis_Object((1,3,6,1,4,1,7483,6,4,1,6,5,1,7),_TnRmdTsopIwfDecapGAis_Type())
tnRmdTsopIwfDecapGAis.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdTsopIwfDecapGAis.setStatus(_A)
_TnRmdTsopIwfDecapForceGAis_Type=TruthValue
_TnRmdTsopIwfDecapForceGAis_Object=MibTableColumn
tnRmdTsopIwfDecapForceGAis=_TnRmdTsopIwfDecapForceGAis_Object((1,3,6,1,4,1,7483,6,4,1,6,5,1,8),_TnRmdTsopIwfDecapForceGAis_Type())
tnRmdTsopIwfDecapForceGAis.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdTsopIwfDecapForceGAis.setStatus(_A)
_TnRmdTsopIwfDecapGAisIncludeInvalidLmBits_Type=TruthValue
_TnRmdTsopIwfDecapGAisIncludeInvalidLmBits_Object=MibTableColumn
tnRmdTsopIwfDecapGAisIncludeInvalidLmBits=_TnRmdTsopIwfDecapGAisIncludeInvalidLmBits_Object((1,3,6,1,4,1,7483,6,4,1,6,5,1,9),_TnRmdTsopIwfDecapGAisIncludeInvalidLmBits_Type())
tnRmdTsopIwfDecapGAisIncludeInvalidLmBits.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdTsopIwfDecapGAisIncludeInvalidLmBits.setStatus(_A)
_TnRmdTsopIwfDecapExpectRtpHeader_Type=TruthValue
_TnRmdTsopIwfDecapExpectRtpHeader_Object=MibTableColumn
tnRmdTsopIwfDecapExpectRtpHeader=_TnRmdTsopIwfDecapExpectRtpHeader_Object((1,3,6,1,4,1,7483,6,4,1,6,5,1,10),_TnRmdTsopIwfDecapExpectRtpHeader_Type())
tnRmdTsopIwfDecapExpectRtpHeader.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdTsopIwfDecapExpectRtpHeader.setStatus(_A)
_TnRmdTsopIwfDecapRtpClockSource_Type=TnRmdRtpClockSource
_TnRmdTsopIwfDecapRtpClockSource_Object=MibTableColumn
tnRmdTsopIwfDecapRtpClockSource=_TnRmdTsopIwfDecapRtpClockSource_Object((1,3,6,1,4,1,7483,6,4,1,6,5,1,11),_TnRmdTsopIwfDecapRtpClockSource_Type())
tnRmdTsopIwfDecapRtpClockSource.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdTsopIwfDecapRtpClockSource.setStatus(_A)
_TnRmdTsopIwfDecapRtpFrequency_Type=TnRmdRtpFrequency
_TnRmdTsopIwfDecapRtpFrequency_Object=MibTableColumn
tnRmdTsopIwfDecapRtpFrequency=_TnRmdTsopIwfDecapRtpFrequency_Object((1,3,6,1,4,1,7483,6,4,1,6,5,1,12),_TnRmdTsopIwfDecapRtpFrequency_Type())
tnRmdTsopIwfDecapRtpFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdTsopIwfDecapRtpFrequency.setStatus(_A)
_TnRmdTsopIwfDecapRtpExpectedPayloadType_Type=Unsigned32
_TnRmdTsopIwfDecapRtpExpectedPayloadType_Object=MibTableColumn
tnRmdTsopIwfDecapRtpExpectedPayloadType=_TnRmdTsopIwfDecapRtpExpectedPayloadType_Object((1,3,6,1,4,1,7483,6,4,1,6,5,1,13),_TnRmdTsopIwfDecapRtpExpectedPayloadType_Type())
tnRmdTsopIwfDecapRtpExpectedPayloadType.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdTsopIwfDecapRtpExpectedPayloadType.setStatus(_A)
_TnRmdTsopIwfDecapRtpPayloadTypeMismatchDetection_Type=TruthValue
_TnRmdTsopIwfDecapRtpPayloadTypeMismatchDetection_Object=MibTableColumn
tnRmdTsopIwfDecapRtpPayloadTypeMismatchDetection=_TnRmdTsopIwfDecapRtpPayloadTypeMismatchDetection_Object((1,3,6,1,4,1,7483,6,4,1,6,5,1,14),_TnRmdTsopIwfDecapRtpPayloadTypeMismatchDetection_Type())
tnRmdTsopIwfDecapRtpPayloadTypeMismatchDetection.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdTsopIwfDecapRtpPayloadTypeMismatchDetection.setStatus(_A)
_TnRmdTsopIwfDecapRtpExpectedSsrc_Type=Unsigned32
_TnRmdTsopIwfDecapRtpExpectedSsrc_Object=MibTableColumn
tnRmdTsopIwfDecapRtpExpectedSsrc=_TnRmdTsopIwfDecapRtpExpectedSsrc_Object((1,3,6,1,4,1,7483,6,4,1,6,5,1,15),_TnRmdTsopIwfDecapRtpExpectedSsrc_Type())
tnRmdTsopIwfDecapRtpExpectedSsrc.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdTsopIwfDecapRtpExpectedSsrc.setStatus(_A)
_TnRmdTsopIwfDecapGAisIncludeStray_Type=TruthValue
_TnRmdTsopIwfDecapGAisIncludeStray_Object=MibTableColumn
tnRmdTsopIwfDecapGAisIncludeStray=_TnRmdTsopIwfDecapGAisIncludeStray_Object((1,3,6,1,4,1,7483,6,4,1,6,5,1,16),_TnRmdTsopIwfDecapGAisIncludeStray_Type())
tnRmdTsopIwfDecapGAisIncludeStray.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdTsopIwfDecapGAisIncludeStray.setStatus(_A)
_TnRmdTsopIwfDecapGAisIncludeMalformed_Type=TruthValue
_TnRmdTsopIwfDecapGAisIncludeMalformed_Object=MibTableColumn
tnRmdTsopIwfDecapGAisIncludeMalformed=_TnRmdTsopIwfDecapGAisIncludeMalformed_Object((1,3,6,1,4,1,7483,6,4,1,6,5,1,17),_TnRmdTsopIwfDecapGAisIncludeMalformed_Type())
tnRmdTsopIwfDecapGAisIncludeMalformed.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdTsopIwfDecapGAisIncludeMalformed.setStatus(_A)
_TnRmdTsopIwfJbTable_Object=MibTable
tnRmdTsopIwfJbTable=_TnRmdTsopIwfJbTable_Object((1,3,6,1,4,1,7483,6,4,1,6,6))
if mibBuilder.loadTexts:tnRmdTsopIwfJbTable.setStatus(_A)
_TnRmdTsopIwfJbEntry_Object=MibTableRow
tnRmdTsopIwfJbEntry=_TnRmdTsopIwfJbEntry_Object((1,3,6,1,4,1,7483,6,4,1,6,6,1))
tnRmdTsopIwfJbEntry.setIndexNames((0,_F,_G),(0,_D,_E),(0,_H,_I))
if mibBuilder.loadTexts:tnRmdTsopIwfJbEntry.setStatus(_A)
_TnRmdTsopIwfJbMaxSize_Type=Unsigned32
_TnRmdTsopIwfJbMaxSize_Object=MibTableColumn
tnRmdTsopIwfJbMaxSize=_TnRmdTsopIwfJbMaxSize_Object((1,3,6,1,4,1,7483,6,4,1,6,6,1,1),_TnRmdTsopIwfJbMaxSize_Type())
tnRmdTsopIwfJbMaxSize.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdTsopIwfJbMaxSize.setStatus(_A)
_TnRmdTsopIwfJbMinimumFillLevel_Type=Unsigned32
_TnRmdTsopIwfJbMinimumFillLevel_Object=MibTableColumn
tnRmdTsopIwfJbMinimumFillLevel=_TnRmdTsopIwfJbMinimumFillLevel_Object((1,3,6,1,4,1,7483,6,4,1,6,6,1,2),_TnRmdTsopIwfJbMinimumFillLevel_Type())
tnRmdTsopIwfJbMinimumFillLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:tnRmdTsopIwfJbMinimumFillLevel.setStatus(_A)
_TnRmdTsopIwfJbMaximumFillLevel_Type=Unsigned32
_TnRmdTsopIwfJbMaximumFillLevel_Object=MibTableColumn
tnRmdTsopIwfJbMaximumFillLevel=_TnRmdTsopIwfJbMaximumFillLevel_Object((1,3,6,1,4,1,7483,6,4,1,6,6,1,3),_TnRmdTsopIwfJbMaximumFillLevel_Type())
tnRmdTsopIwfJbMaximumFillLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:tnRmdTsopIwfJbMaximumFillLevel.setStatus(_A)
_TnRmdTsopIwfJbRecenterPosition_Type=Unsigned32
_TnRmdTsopIwfJbRecenterPosition_Object=MibTableColumn
tnRmdTsopIwfJbRecenterPosition=_TnRmdTsopIwfJbRecenterPosition_Object((1,3,6,1,4,1,7483,6,4,1,6,6,1,4),_TnRmdTsopIwfJbRecenterPosition_Type())
tnRmdTsopIwfJbRecenterPosition.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdTsopIwfJbRecenterPosition.setStatus(_A)
_TnRmdTsopIwfJbFillLevelReset_Type=TruthValue
_TnRmdTsopIwfJbFillLevelReset_Object=MibTableColumn
tnRmdTsopIwfJbFillLevelReset=_TnRmdTsopIwfJbFillLevelReset_Object((1,3,6,1,4,1,7483,6,4,1,6,6,1,5),_TnRmdTsopIwfJbFillLevelReset_Type())
tnRmdTsopIwfJbFillLevelReset.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdTsopIwfJbFillLevelReset.setStatus(_A)
_TnRmdTsopIwfJbShiftPosition_Type=Unsigned32
_TnRmdTsopIwfJbShiftPosition_Object=MibTableColumn
tnRmdTsopIwfJbShiftPosition=_TnRmdTsopIwfJbShiftPosition_Object((1,3,6,1,4,1,7483,6,4,1,6,6,1,6),_TnRmdTsopIwfJbShiftPosition_Type())
tnRmdTsopIwfJbShiftPosition.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdTsopIwfJbShiftPosition.setStatus(_A)
_TnRmdTsopIwfJbRecenter_Type=TruthValue
_TnRmdTsopIwfJbRecenter_Object=MibTableColumn
tnRmdTsopIwfJbRecenter=_TnRmdTsopIwfJbRecenter_Object((1,3,6,1,4,1,7483,6,4,1,6,6,1,7),_TnRmdTsopIwfJbRecenter_Type())
tnRmdTsopIwfJbRecenter.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdTsopIwfJbRecenter.setStatus(_A)
_TnRmdTsopIwfJbLowThreshold_Type=Unsigned32
_TnRmdTsopIwfJbLowThreshold_Object=MibTableColumn
tnRmdTsopIwfJbLowThreshold=_TnRmdTsopIwfJbLowThreshold_Object((1,3,6,1,4,1,7483,6,4,1,6,6,1,8),_TnRmdTsopIwfJbLowThreshold_Type())
tnRmdTsopIwfJbLowThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdTsopIwfJbLowThreshold.setStatus(_A)
_TnRmdTsopIwfJbHighThreshold_Type=Unsigned32
_TnRmdTsopIwfJbHighThreshold_Object=MibTableColumn
tnRmdTsopIwfJbHighThreshold=_TnRmdTsopIwfJbHighThreshold_Object((1,3,6,1,4,1,7483,6,4,1,6,6,1,9),_TnRmdTsopIwfJbHighThreshold_Type())
tnRmdTsopIwfJbHighThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdTsopIwfJbHighThreshold.setStatus(_A)
_TnRmdTsopIwfJbRecenterThreshold_Type=Unsigned32
_TnRmdTsopIwfJbRecenterThreshold_Object=MibTableColumn
tnRmdTsopIwfJbRecenterThreshold=_TnRmdTsopIwfJbRecenterThreshold_Object((1,3,6,1,4,1,7483,6,4,1,6,6,1,10),_TnRmdTsopIwfJbRecenterThreshold_Type())
tnRmdTsopIwfJbRecenterThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdTsopIwfJbRecenterThreshold.setStatus(_A)
_TnRmdTsopIwfJbRecenterIncrement_Type=Unsigned32
_TnRmdTsopIwfJbRecenterIncrement_Object=MibTableColumn
tnRmdTsopIwfJbRecenterIncrement=_TnRmdTsopIwfJbRecenterIncrement_Object((1,3,6,1,4,1,7483,6,4,1,6,6,1,11),_TnRmdTsopIwfJbRecenterIncrement_Type())
tnRmdTsopIwfJbRecenterIncrement.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdTsopIwfJbRecenterIncrement.setStatus(_A)
_TnRmdTsopJbBasicApplMonitorTable_Object=MibTable
tnRmdTsopJbBasicApplMonitorTable=_TnRmdTsopJbBasicApplMonitorTable_Object((1,3,6,1,4,1,7483,6,4,1,6,7))
if mibBuilder.loadTexts:tnRmdTsopJbBasicApplMonitorTable.setStatus(_A)
_TnRmdTsopJbBasicApplMonitorEntry_Object=MibTableRow
tnRmdTsopJbBasicApplMonitorEntry=_TnRmdTsopJbBasicApplMonitorEntry_Object((1,3,6,1,4,1,7483,6,4,1,6,7,1))
tnRmdTsopJbBasicApplMonitorEntry.setIndexNames((0,_F,_G),(0,_D,_E),(0,_H,_I))
if mibBuilder.loadTexts:tnRmdTsopJbBasicApplMonitorEntry.setStatus(_A)
_TnRmdTsopJbBasicApplMonitorState_Type=TruthValue
_TnRmdTsopJbBasicApplMonitorState_Object=MibTableColumn
tnRmdTsopJbBasicApplMonitorState=_TnRmdTsopJbBasicApplMonitorState_Object((1,3,6,1,4,1,7483,6,4,1,6,7,1,1),_TnRmdTsopJbBasicApplMonitorState_Type())
tnRmdTsopJbBasicApplMonitorState.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdTsopJbBasicApplMonitorState.setStatus(_A)
_TnRmdTsopJbBasicApplMonitorReportFillLevels_Type=TruthValue
_TnRmdTsopJbBasicApplMonitorReportFillLevels_Object=MibTableColumn
tnRmdTsopJbBasicApplMonitorReportFillLevels=_TnRmdTsopJbBasicApplMonitorReportFillLevels_Object((1,3,6,1,4,1,7483,6,4,1,6,7,1,2),_TnRmdTsopJbBasicApplMonitorReportFillLevels_Type())
tnRmdTsopJbBasicApplMonitorReportFillLevels.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdTsopJbBasicApplMonitorReportFillLevels.setStatus(_A)
_TnRmdTsopJbBasicApplMonitorZeroObservationPeriod_Type=TnRmdTsopJbObservationPeriod
_TnRmdTsopJbBasicApplMonitorZeroObservationPeriod_Object=MibTableColumn
tnRmdTsopJbBasicApplMonitorZeroObservationPeriod=_TnRmdTsopJbBasicApplMonitorZeroObservationPeriod_Object((1,3,6,1,4,1,7483,6,4,1,6,7,1,3),_TnRmdTsopJbBasicApplMonitorZeroObservationPeriod_Type())
tnRmdTsopJbBasicApplMonitorZeroObservationPeriod.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdTsopJbBasicApplMonitorZeroObservationPeriod.setStatus(_A)
_TnRmdTsopJbBasicApplIntegrationTable_Object=MibTable
tnRmdTsopJbBasicApplIntegrationTable=_TnRmdTsopJbBasicApplIntegrationTable_Object((1,3,6,1,4,1,7483,6,4,1,6,8))
if mibBuilder.loadTexts:tnRmdTsopJbBasicApplIntegrationTable.setStatus(_A)
_TnRmdTsopJbBasicApplIntegrationEntry_Object=MibTableRow
tnRmdTsopJbBasicApplIntegrationEntry=_TnRmdTsopJbBasicApplIntegrationEntry_Object((1,3,6,1,4,1,7483,6,4,1,6,8,1))
tnRmdTsopJbBasicApplIntegrationEntry.setIndexNames((0,_F,_G),(0,_D,_E),(0,_H,_I))
if mibBuilder.loadTexts:tnRmdTsopJbBasicApplIntegrationEntry.setStatus(_A)
_TnRmdTsopJbBasicApplIntegrationState_Type=TruthValue
_TnRmdTsopJbBasicApplIntegrationState_Object=MibTableColumn
tnRmdTsopJbBasicApplIntegrationState=_TnRmdTsopJbBasicApplIntegrationState_Object((1,3,6,1,4,1,7483,6,4,1,6,8,1,1),_TnRmdTsopJbBasicApplIntegrationState_Type())
tnRmdTsopJbBasicApplIntegrationState.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdTsopJbBasicApplIntegrationState.setStatus(_A)
_TnRmdTsopJbBasicApplIntegrationObservationStages_Type=Unsigned32
_TnRmdTsopJbBasicApplIntegrationObservationStages_Object=MibTableColumn
tnRmdTsopJbBasicApplIntegrationObservationStages=_TnRmdTsopJbBasicApplIntegrationObservationStages_Object((1,3,6,1,4,1,7483,6,4,1,6,8,1,2),_TnRmdTsopJbBasicApplIntegrationObservationStages_Type())
tnRmdTsopJbBasicApplIntegrationObservationStages.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdTsopJbBasicApplIntegrationObservationStages.setStatus(_A)
_TnRmdTsopJbBasicApplIntegrationMaxObservationPeriod_Type=Unsigned32
_TnRmdTsopJbBasicApplIntegrationMaxObservationPeriod_Object=MibTableColumn
tnRmdTsopJbBasicApplIntegrationMaxObservationPeriod=_TnRmdTsopJbBasicApplIntegrationMaxObservationPeriod_Object((1,3,6,1,4,1,7483,6,4,1,6,8,1,3),_TnRmdTsopJbBasicApplIntegrationMaxObservationPeriod_Type())
tnRmdTsopJbBasicApplIntegrationMaxObservationPeriod.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdTsopJbBasicApplIntegrationMaxObservationPeriod.setStatus(_A)
_TnRmdTsopJbBasicApplIntegrationZeroLowThreshold_Type=Unsigned32
_TnRmdTsopJbBasicApplIntegrationZeroLowThreshold_Object=MibTableColumn
tnRmdTsopJbBasicApplIntegrationZeroLowThreshold=_TnRmdTsopJbBasicApplIntegrationZeroLowThreshold_Object((1,3,6,1,4,1,7483,6,4,1,6,8,1,4),_TnRmdTsopJbBasicApplIntegrationZeroLowThreshold_Type())
tnRmdTsopJbBasicApplIntegrationZeroLowThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdTsopJbBasicApplIntegrationZeroLowThreshold.setStatus(_A)
_TnRmdTsopJbBasicApplIntegrationZeroHighThreshold_Type=Unsigned32
_TnRmdTsopJbBasicApplIntegrationZeroHighThreshold_Object=MibTableColumn
tnRmdTsopJbBasicApplIntegrationZeroHighThreshold=_TnRmdTsopJbBasicApplIntegrationZeroHighThreshold_Object((1,3,6,1,4,1,7483,6,4,1,6,8,1,5),_TnRmdTsopJbBasicApplIntegrationZeroHighThreshold_Type())
tnRmdTsopJbBasicApplIntegrationZeroHighThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdTsopJbBasicApplIntegrationZeroHighThreshold.setStatus(_A)
_TnRmdTsopJbBasicApplIntegrationMaxLowThreshold_Type=Unsigned32
_TnRmdTsopJbBasicApplIntegrationMaxLowThreshold_Object=MibTableColumn
tnRmdTsopJbBasicApplIntegrationMaxLowThreshold=_TnRmdTsopJbBasicApplIntegrationMaxLowThreshold_Object((1,3,6,1,4,1,7483,6,4,1,6,8,1,6),_TnRmdTsopJbBasicApplIntegrationMaxLowThreshold_Type())
tnRmdTsopJbBasicApplIntegrationMaxLowThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdTsopJbBasicApplIntegrationMaxLowThreshold.setStatus(_A)
_TnRmdTsopJbBasicApplIntegrationMaxHighThreshold_Type=Unsigned32
_TnRmdTsopJbBasicApplIntegrationMaxHighThreshold_Object=MibTableColumn
tnRmdTsopJbBasicApplIntegrationMaxHighThreshold=_TnRmdTsopJbBasicApplIntegrationMaxHighThreshold_Object((1,3,6,1,4,1,7483,6,4,1,6,8,1,7),_TnRmdTsopJbBasicApplIntegrationMaxHighThreshold_Type())
tnRmdTsopJbBasicApplIntegrationMaxHighThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdTsopJbBasicApplIntegrationMaxHighThreshold.setStatus(_A)
_TnRmdTsopJbBasicApplManagementTable_Object=MibTable
tnRmdTsopJbBasicApplManagementTable=_TnRmdTsopJbBasicApplManagementTable_Object((1,3,6,1,4,1,7483,6,4,1,6,9))
if mibBuilder.loadTexts:tnRmdTsopJbBasicApplManagementTable.setStatus(_A)
_TnRmdTsopJbBasicApplManagementEntry_Object=MibTableRow
tnRmdTsopJbBasicApplManagementEntry=_TnRmdTsopJbBasicApplManagementEntry_Object((1,3,6,1,4,1,7483,6,4,1,6,9,1))
tnRmdTsopJbBasicApplManagementEntry.setIndexNames((0,_F,_G),(0,_D,_E),(0,_H,_I))
if mibBuilder.loadTexts:tnRmdTsopJbBasicApplManagementEntry.setStatus(_A)
_TnRmdTsopJbBasicApplManagementState_Type=TruthValue
_TnRmdTsopJbBasicApplManagementState_Object=MibTableColumn
tnRmdTsopJbBasicApplManagementState=_TnRmdTsopJbBasicApplManagementState_Object((1,3,6,1,4,1,7483,6,4,1,6,9,1,1),_TnRmdTsopJbBasicApplManagementState_Type())
tnRmdTsopJbBasicApplManagementState.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdTsopJbBasicApplManagementState.setStatus(_A)
_TnRmdTsopJbBasicApplManagementShiftAllowed_Type=TruthValue
_TnRmdTsopJbBasicApplManagementShiftAllowed_Object=MibTableColumn
tnRmdTsopJbBasicApplManagementShiftAllowed=_TnRmdTsopJbBasicApplManagementShiftAllowed_Object((1,3,6,1,4,1,7483,6,4,1,6,9,1,2),_TnRmdTsopJbBasicApplManagementShiftAllowed_Type())
tnRmdTsopJbBasicApplManagementShiftAllowed.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdTsopJbBasicApplManagementShiftAllowed.setStatus(_A)
_TnRmdTsopPsnTable_Object=MibTable
tnRmdTsopPsnTable=_TnRmdTsopPsnTable_Object((1,3,6,1,4,1,7483,6,4,1,6,10))
if mibBuilder.loadTexts:tnRmdTsopPsnTable.setStatus(_A)
_TnRmdTsopPsnEntry_Object=MibTableRow
tnRmdTsopPsnEntry=_TnRmdTsopPsnEntry_Object((1,3,6,1,4,1,7483,6,4,1,6,10,1))
tnRmdTsopPsnEntry.setIndexNames((0,_F,_G),(0,_D,_E),(0,_H,_I))
if mibBuilder.loadTexts:tnRmdTsopPsnEntry.setStatus(_A)
_TnRmdTsopPsnTxDestMac_Type=MacAddress
_TnRmdTsopPsnTxDestMac_Object=MibTableColumn
tnRmdTsopPsnTxDestMac=_TnRmdTsopPsnTxDestMac_Object((1,3,6,1,4,1,7483,6,4,1,6,10,1,1),_TnRmdTsopPsnTxDestMac_Type())
tnRmdTsopPsnTxDestMac.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdTsopPsnTxDestMac.setStatus(_A)
_TnRmdTsopEthIfTable_Object=MibTable
tnRmdTsopEthIfTable=_TnRmdTsopEthIfTable_Object((1,3,6,1,4,1,7483,6,4,1,6,11))
if mibBuilder.loadTexts:tnRmdTsopEthIfTable.setStatus(_A)
_TnRmdTsopEthIfEntry_Object=MibTableRow
tnRmdTsopEthIfEntry=_TnRmdTsopEthIfEntry_Object((1,3,6,1,4,1,7483,6,4,1,6,11,1))
tnRmdTsopEthIfEntry.setIndexNames((0,_F,_G),(0,_D,_E),(0,_J,_K))
if mibBuilder.loadTexts:tnRmdTsopEthIfEntry.setStatus(_A)
_TnRmdTsopEthIfSystemPsnRxDestMacCheck_Type=TruthValue
_TnRmdTsopEthIfSystemPsnRxDestMacCheck_Object=MibTableColumn
tnRmdTsopEthIfSystemPsnRxDestMacCheck=_TnRmdTsopEthIfSystemPsnRxDestMacCheck_Object((1,3,6,1,4,1,7483,6,4,1,6,11,1,1),_TnRmdTsopEthIfSystemPsnRxDestMacCheck_Type())
tnRmdTsopEthIfSystemPsnRxDestMacCheck.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdTsopEthIfSystemPsnRxDestMacCheck.setStatus(_A)
_TnRmdTsopIwfCountersTable_Object=MibTable
tnRmdTsopIwfCountersTable=_TnRmdTsopIwfCountersTable_Object((1,3,6,1,4,1,7483,6,4,1,6,12))
if mibBuilder.loadTexts:tnRmdTsopIwfCountersTable.setStatus(_A)
_TnRmdTsopIwfCountersEntry_Object=MibTableRow
tnRmdTsopIwfCountersEntry=_TnRmdTsopIwfCountersEntry_Object((1,3,6,1,4,1,7483,6,4,1,6,12,1))
tnRmdTsopIwfCountersEntry.setIndexNames((0,_F,_G),(0,_D,_E),(0,_H,_I))
if mibBuilder.loadTexts:tnRmdTsopIwfCountersEntry.setStatus(_A)
_TnRmdTsopIwfCountersRxPackets_Type=Counter64
_TnRmdTsopIwfCountersRxPackets_Object=MibTableColumn
tnRmdTsopIwfCountersRxPackets=_TnRmdTsopIwfCountersRxPackets_Object((1,3,6,1,4,1,7483,6,4,1,6,12,1,1),_TnRmdTsopIwfCountersRxPackets_Type())
tnRmdTsopIwfCountersRxPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:tnRmdTsopIwfCountersRxPackets.setStatus(_A)
_TnRmdTsopIwfCountersTxPackets_Type=Counter64
_TnRmdTsopIwfCountersTxPackets_Object=MibTableColumn
tnRmdTsopIwfCountersTxPackets=_TnRmdTsopIwfCountersTxPackets_Object((1,3,6,1,4,1,7483,6,4,1,6,12,1,2),_TnRmdTsopIwfCountersTxPackets_Type())
tnRmdTsopIwfCountersTxPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:tnRmdTsopIwfCountersTxPackets.setStatus(_A)
_TnRmdTsopIwfCountersMalformedPackets_Type=Counter64
_TnRmdTsopIwfCountersMalformedPackets_Object=MibTableColumn
tnRmdTsopIwfCountersMalformedPackets=_TnRmdTsopIwfCountersMalformedPackets_Object((1,3,6,1,4,1,7483,6,4,1,6,12,1,3),_TnRmdTsopIwfCountersMalformedPackets_Type())
tnRmdTsopIwfCountersMalformedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:tnRmdTsopIwfCountersMalformedPackets.setStatus(_A)
_TnRmdTsopIwfCountersReorderedPackets_Type=Counter64
_TnRmdTsopIwfCountersReorderedPackets_Object=MibTableColumn
tnRmdTsopIwfCountersReorderedPackets=_TnRmdTsopIwfCountersReorderedPackets_Object((1,3,6,1,4,1,7483,6,4,1,6,12,1,4),_TnRmdTsopIwfCountersReorderedPackets_Type())
tnRmdTsopIwfCountersReorderedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:tnRmdTsopIwfCountersReorderedPackets.setStatus(_A)
_TnRmdTsopIwfCountersMisorderedDroppedPackets_Type=Counter64
_TnRmdTsopIwfCountersMisorderedDroppedPackets_Object=MibTableColumn
tnRmdTsopIwfCountersMisorderedDroppedPackets=_TnRmdTsopIwfCountersMisorderedDroppedPackets_Object((1,3,6,1,4,1,7483,6,4,1,6,12,1,5),_TnRmdTsopIwfCountersMisorderedDroppedPackets_Type())
tnRmdTsopIwfCountersMisorderedDroppedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:tnRmdTsopIwfCountersMisorderedDroppedPackets.setStatus(_A)
_TnRmdTsopIwfCountersMissingPackets_Type=Counter64
_TnRmdTsopIwfCountersMissingPackets_Object=MibTableColumn
tnRmdTsopIwfCountersMissingPackets=_TnRmdTsopIwfCountersMissingPackets_Object((1,3,6,1,4,1,7483,6,4,1,6,12,1,6),_TnRmdTsopIwfCountersMissingPackets_Type())
tnRmdTsopIwfCountersMissingPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:tnRmdTsopIwfCountersMissingPackets.setStatus(_A)
_TnRmdTsopIwfCountersPlayedOutPackets_Type=Counter64
_TnRmdTsopIwfCountersPlayedOutPackets_Object=MibTableColumn
tnRmdTsopIwfCountersPlayedOutPackets=_TnRmdTsopIwfCountersPlayedOutPackets_Object((1,3,6,1,4,1,7483,6,4,1,6,12,1,7),_TnRmdTsopIwfCountersPlayedOutPackets_Type())
tnRmdTsopIwfCountersPlayedOutPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:tnRmdTsopIwfCountersPlayedOutPackets.setStatus(_A)
_TnRmdTsopIwfCountersJbOverrun_Type=Counter64
_TnRmdTsopIwfCountersJbOverrun_Object=MibTableColumn
tnRmdTsopIwfCountersJbOverrun=_TnRmdTsopIwfCountersJbOverrun_Object((1,3,6,1,4,1,7483,6,4,1,6,12,1,8),_TnRmdTsopIwfCountersJbOverrun_Type())
tnRmdTsopIwfCountersJbOverrun.setMaxAccess(_C)
if mibBuilder.loadTexts:tnRmdTsopIwfCountersJbOverrun.setStatus(_A)
_TnRmdTsopIwfCountersJbUnderrun_Type=Counter64
_TnRmdTsopIwfCountersJbUnderrun_Object=MibTableColumn
tnRmdTsopIwfCountersJbUnderrun=_TnRmdTsopIwfCountersJbUnderrun_Object((1,3,6,1,4,1,7483,6,4,1,6,12,1,9),_TnRmdTsopIwfCountersJbUnderrun_Type())
tnRmdTsopIwfCountersJbUnderrun.setMaxAccess(_C)
if mibBuilder.loadTexts:tnRmdTsopIwfCountersJbUnderrun.setStatus(_A)
_TnRmdTsopIwfCountersReset_Type=TruthValue
_TnRmdTsopIwfCountersReset_Object=MibTableColumn
tnRmdTsopIwfCountersReset=_TnRmdTsopIwfCountersReset_Object((1,3,6,1,4,1,7483,6,4,1,6,12,1,10),_TnRmdTsopIwfCountersReset_Type())
tnRmdTsopIwfCountersReset.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdTsopIwfCountersReset.setStatus(_A)
_TnRmdTsopTdmLoopbackTable_Object=MibTable
tnRmdTsopTdmLoopbackTable=_TnRmdTsopTdmLoopbackTable_Object((1,3,6,1,4,1,7483,6,4,1,6,13))
if mibBuilder.loadTexts:tnRmdTsopTdmLoopbackTable.setStatus(_A)
_TnRmdTsopTdmLoopbackEntry_Object=MibTableRow
tnRmdTsopTdmLoopbackEntry=_TnRmdTsopTdmLoopbackEntry_Object((1,3,6,1,4,1,7483,6,4,1,6,13,1))
tnRmdTsopTdmLoopbackEntry.setIndexNames((0,_F,_G),(0,_D,_E),(0,_J,_K))
if mibBuilder.loadTexts:tnRmdTsopTdmLoopbackEntry.setStatus(_A)
_TnRmdTsopTdmLoopbackInLoopEnabled_Type=TruthValue
_TnRmdTsopTdmLoopbackInLoopEnabled_Object=MibTableColumn
tnRmdTsopTdmLoopbackInLoopEnabled=_TnRmdTsopTdmLoopbackInLoopEnabled_Object((1,3,6,1,4,1,7483,6,4,1,6,13,1,1),_TnRmdTsopTdmLoopbackInLoopEnabled_Type())
tnRmdTsopTdmLoopbackInLoopEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdTsopTdmLoopbackInLoopEnabled.setStatus(_A)
_TnRmdTsopTdmLoopbackInLoopType_Type=TnRmdTdmLoopbackType
_TnRmdTsopTdmLoopbackInLoopType_Object=MibTableColumn
tnRmdTsopTdmLoopbackInLoopType=_TnRmdTsopTdmLoopbackInLoopType_Object((1,3,6,1,4,1,7483,6,4,1,6,13,1,2),_TnRmdTsopTdmLoopbackInLoopType_Type())
tnRmdTsopTdmLoopbackInLoopType.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdTsopTdmLoopbackInLoopType.setStatus(_A)
_TnRmdTsopTdmLoopbackOutLoopEnabled_Type=TruthValue
_TnRmdTsopTdmLoopbackOutLoopEnabled_Object=MibTableColumn
tnRmdTsopTdmLoopbackOutLoopEnabled=_TnRmdTsopTdmLoopbackOutLoopEnabled_Object((1,3,6,1,4,1,7483,6,4,1,6,13,1,3),_TnRmdTsopTdmLoopbackOutLoopEnabled_Type())
tnRmdTsopTdmLoopbackOutLoopEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdTsopTdmLoopbackOutLoopEnabled.setStatus(_A)
_TnRmdTsopTdmLoopbackOutLoopType_Type=TnRmdTdmLoopbackType
_TnRmdTsopTdmLoopbackOutLoopType_Object=MibTableColumn
tnRmdTsopTdmLoopbackOutLoopType=_TnRmdTsopTdmLoopbackOutLoopType_Object((1,3,6,1,4,1,7483,6,4,1,6,13,1,4),_TnRmdTsopTdmLoopbackOutLoopType_Type())
tnRmdTsopTdmLoopbackOutLoopType.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdTsopTdmLoopbackOutLoopType.setStatus(_A)
mibBuilder.exportSymbols(_H,**{'TnRmdIwfChannelNumber':TnRmdIwfChannelNumber,'TnRmdIwfTimingMode':TnRmdIwfTimingMode,'TnRmdRtpClockSource':TnRmdRtpClockSource,'TnRmdRtpFrequency':TnRmdRtpFrequency,'TnRmdTdmLoopbackType':TnRmdTdmLoopbackType,'TnRmdTsopJbObservationPeriod':TnRmdTsopJbObservationPeriod,'tnRmdTsopMibModule':tnRmdTsopMibModule,'tnRmdTsopObjects':tnRmdTsopObjects,'tnRmdTsopAttributeTotal':tnRmdTsopAttributeTotal,'tnRmdTsopSystemTable':tnRmdTsopSystemTable,'tnRmdTsopSystemEntry':tnRmdTsopSystemEntry,'tnRmdTsopSystemMaxNrChannels':tnRmdTsopSystemMaxNrChannels,'tnRmdTsopSystemMaxJbSize':tnRmdTsopSystemMaxJbSize,'tnRmdTsopIwfTable':tnRmdTsopIwfTable,'tnRmdTsopIwfEntry':tnRmdTsopIwfEntry,_I:tnRmdTsopIwfChannelNumber,'tnRmdTsopIwfUserLabel':tnRmdTsopIwfUserLabel,'tnRmdTsopIwfEncapTable':tnRmdTsopIwfEncapTable,'tnRmdTsopIwfEncapEntry':tnRmdTsopIwfEncapEntry,'tnRmdTsopIwfEncapOutput':tnRmdTsopIwfEncapOutput,'tnRmdTsopIwfEncapGAisActive':tnRmdTsopIwfEncapGAisActive,'tnRmdTsopIwfEncapGAisIncludeLos':tnRmdTsopIwfEncapGAisIncludeLos,'tnRmdTsopIwfEncapGAisIncludeLof':tnRmdTsopIwfEncapGAisIncludeLof,'tnRmdTsopIwfEncapEcid':tnRmdTsopIwfEncapEcid,'tnRmdTsopIwfEncapInsertRtpHeader':tnRmdTsopIwfEncapInsertRtpHeader,'tnRmdTsopIwfEncapRtpClockSource':tnRmdTsopIwfEncapRtpClockSource,'tnRmdTsopIwfEncapRtpFrequency':tnRmdTsopIwfEncapRtpFrequency,'tnRmdTsopIwfEncapRtpPayloadType':tnRmdTsopIwfEncapRtpPayloadType,'tnRmdTsopIwfEncapRtpSsrc':tnRmdTsopIwfEncapRtpSsrc,'tnRmdTsopIwfDecapTable':tnRmdTsopIwfDecapTable,'tnRmdTsopIwfDecapEntry':tnRmdTsopIwfDecapEntry,'tnRmdTsopIwfDecapExpectedEcid':tnRmdTsopIwfDecapExpectedEcid,'tnRmdTsopIwfDecapUnknownEcid':tnRmdTsopIwfDecapUnknownEcid,'tnRmdTsopIwfDecapTimingMode':tnRmdTsopIwfDecapTimingMode,'tnRmdTsopIwfDecapRaiseThreshold':tnRmdTsopIwfDecapRaiseThreshold,'tnRmdTsopIwfDecapClearThreshold':tnRmdTsopIwfDecapClearThreshold,'tnRmdTsopIwfDecapGAisActive':tnRmdTsopIwfDecapGAisActive,'tnRmdTsopIwfDecapGAis':tnRmdTsopIwfDecapGAis,'tnRmdTsopIwfDecapForceGAis':tnRmdTsopIwfDecapForceGAis,'tnRmdTsopIwfDecapGAisIncludeInvalidLmBits':tnRmdTsopIwfDecapGAisIncludeInvalidLmBits,'tnRmdTsopIwfDecapExpectRtpHeader':tnRmdTsopIwfDecapExpectRtpHeader,'tnRmdTsopIwfDecapRtpClockSource':tnRmdTsopIwfDecapRtpClockSource,'tnRmdTsopIwfDecapRtpFrequency':tnRmdTsopIwfDecapRtpFrequency,'tnRmdTsopIwfDecapRtpExpectedPayloadType':tnRmdTsopIwfDecapRtpExpectedPayloadType,'tnRmdTsopIwfDecapRtpPayloadTypeMismatchDetection':tnRmdTsopIwfDecapRtpPayloadTypeMismatchDetection,'tnRmdTsopIwfDecapRtpExpectedSsrc':tnRmdTsopIwfDecapRtpExpectedSsrc,'tnRmdTsopIwfDecapGAisIncludeStray':tnRmdTsopIwfDecapGAisIncludeStray,'tnRmdTsopIwfDecapGAisIncludeMalformed':tnRmdTsopIwfDecapGAisIncludeMalformed,'tnRmdTsopIwfJbTable':tnRmdTsopIwfJbTable,'tnRmdTsopIwfJbEntry':tnRmdTsopIwfJbEntry,'tnRmdTsopIwfJbMaxSize':tnRmdTsopIwfJbMaxSize,'tnRmdTsopIwfJbMinimumFillLevel':tnRmdTsopIwfJbMinimumFillLevel,'tnRmdTsopIwfJbMaximumFillLevel':tnRmdTsopIwfJbMaximumFillLevel,'tnRmdTsopIwfJbRecenterPosition':tnRmdTsopIwfJbRecenterPosition,'tnRmdTsopIwfJbFillLevelReset':tnRmdTsopIwfJbFillLevelReset,'tnRmdTsopIwfJbShiftPosition':tnRmdTsopIwfJbShiftPosition,'tnRmdTsopIwfJbRecenter':tnRmdTsopIwfJbRecenter,'tnRmdTsopIwfJbLowThreshold':tnRmdTsopIwfJbLowThreshold,'tnRmdTsopIwfJbHighThreshold':tnRmdTsopIwfJbHighThreshold,'tnRmdTsopIwfJbRecenterThreshold':tnRmdTsopIwfJbRecenterThreshold,'tnRmdTsopIwfJbRecenterIncrement':tnRmdTsopIwfJbRecenterIncrement,'tnRmdTsopJbBasicApplMonitorTable':tnRmdTsopJbBasicApplMonitorTable,'tnRmdTsopJbBasicApplMonitorEntry':tnRmdTsopJbBasicApplMonitorEntry,'tnRmdTsopJbBasicApplMonitorState':tnRmdTsopJbBasicApplMonitorState,'tnRmdTsopJbBasicApplMonitorReportFillLevels':tnRmdTsopJbBasicApplMonitorReportFillLevels,'tnRmdTsopJbBasicApplMonitorZeroObservationPeriod':tnRmdTsopJbBasicApplMonitorZeroObservationPeriod,'tnRmdTsopJbBasicApplIntegrationTable':tnRmdTsopJbBasicApplIntegrationTable,'tnRmdTsopJbBasicApplIntegrationEntry':tnRmdTsopJbBasicApplIntegrationEntry,'tnRmdTsopJbBasicApplIntegrationState':tnRmdTsopJbBasicApplIntegrationState,'tnRmdTsopJbBasicApplIntegrationObservationStages':tnRmdTsopJbBasicApplIntegrationObservationStages,'tnRmdTsopJbBasicApplIntegrationMaxObservationPeriod':tnRmdTsopJbBasicApplIntegrationMaxObservationPeriod,'tnRmdTsopJbBasicApplIntegrationZeroLowThreshold':tnRmdTsopJbBasicApplIntegrationZeroLowThreshold,'tnRmdTsopJbBasicApplIntegrationZeroHighThreshold':tnRmdTsopJbBasicApplIntegrationZeroHighThreshold,'tnRmdTsopJbBasicApplIntegrationMaxLowThreshold':tnRmdTsopJbBasicApplIntegrationMaxLowThreshold,'tnRmdTsopJbBasicApplIntegrationMaxHighThreshold':tnRmdTsopJbBasicApplIntegrationMaxHighThreshold,'tnRmdTsopJbBasicApplManagementTable':tnRmdTsopJbBasicApplManagementTable,'tnRmdTsopJbBasicApplManagementEntry':tnRmdTsopJbBasicApplManagementEntry,'tnRmdTsopJbBasicApplManagementState':tnRmdTsopJbBasicApplManagementState,'tnRmdTsopJbBasicApplManagementShiftAllowed':tnRmdTsopJbBasicApplManagementShiftAllowed,'tnRmdTsopPsnTable':tnRmdTsopPsnTable,'tnRmdTsopPsnEntry':tnRmdTsopPsnEntry,'tnRmdTsopPsnTxDestMac':tnRmdTsopPsnTxDestMac,'tnRmdTsopEthIfTable':tnRmdTsopEthIfTable,'tnRmdTsopEthIfEntry':tnRmdTsopEthIfEntry,'tnRmdTsopEthIfSystemPsnRxDestMacCheck':tnRmdTsopEthIfSystemPsnRxDestMacCheck,'tnRmdTsopIwfCountersTable':tnRmdTsopIwfCountersTable,'tnRmdTsopIwfCountersEntry':tnRmdTsopIwfCountersEntry,'tnRmdTsopIwfCountersRxPackets':tnRmdTsopIwfCountersRxPackets,'tnRmdTsopIwfCountersTxPackets':tnRmdTsopIwfCountersTxPackets,'tnRmdTsopIwfCountersMalformedPackets':tnRmdTsopIwfCountersMalformedPackets,'tnRmdTsopIwfCountersReorderedPackets':tnRmdTsopIwfCountersReorderedPackets,'tnRmdTsopIwfCountersMisorderedDroppedPackets':tnRmdTsopIwfCountersMisorderedDroppedPackets,'tnRmdTsopIwfCountersMissingPackets':tnRmdTsopIwfCountersMissingPackets,'tnRmdTsopIwfCountersPlayedOutPackets':tnRmdTsopIwfCountersPlayedOutPackets,'tnRmdTsopIwfCountersJbOverrun':tnRmdTsopIwfCountersJbOverrun,'tnRmdTsopIwfCountersJbUnderrun':tnRmdTsopIwfCountersJbUnderrun,'tnRmdTsopIwfCountersReset':tnRmdTsopIwfCountersReset,'tnRmdTsopTdmLoopbackTable':tnRmdTsopTdmLoopbackTable,'tnRmdTsopTdmLoopbackEntry':tnRmdTsopTdmLoopbackEntry,'tnRmdTsopTdmLoopbackInLoopEnabled':tnRmdTsopTdmLoopbackInLoopEnabled,'tnRmdTsopTdmLoopbackInLoopType':tnRmdTsopTdmLoopbackInLoopType,'tnRmdTsopTdmLoopbackOutLoopEnabled':tnRmdTsopTdmLoopbackOutLoopEnabled,'tnRmdTsopTdmLoopbackOutLoopType':tnRmdTsopTdmLoopbackOutLoopType})