_A0='ntcTsMuxConfGrpV1Standard'
_z='ntcInputSelectionEnable'
_y='ntcTsMuxNpRangeTimeWindow'
_x='ntcTsMuxNpRangeThrMaxRate'
_w='ntcTsMuxNpRangeThrMinRate'
_v='ntcTsMuxNpRangeThrEnable'
_u='ntcTsMuxNpRateOutRange'
_t='ntcTsMuxAlmBufferOverflow'
_s='ntcTsMuxAlmSignalOverflow'
_r='ntcTsMuxAlmSignalTableProcError'
_q='ntcTsMuxAlmLocalPidOnInput'
_p='ntcTsMuxSigPmtRepetitionRate'
_o='ntcTsMuxSigSdtRepetitionRate'
_n='ntcTsMuxSigPatRepetitionRate'
_m='ntcTsMuxSigTransportStreamId'
_l='ntcTsMuxSigNetworkId'
_k='ntcTsMuxCarIdLatitudeString'
_j='ntcTsMuxCarIdLongitudeString'
_i='ntcTsMuxCarIdUserInfo'
_h='ntcTsMuxCarIdLatitude'
_g='ntcTsMuxCarIdLongitude'
_f='ntcTsMuxCarIdTelephoneNr'
_e='ntcTsMuxCarIdCarrierIdentifier'
_d='ntcTsMuxCarIdModSerialNr'
_c='ntcTsMuxCarIdModMfg'
_b='ntcTsMuxCarIdDescriptorTag'
_a='ntcTsMuxCarIdEnable'
_Z='ntcTsMuxMonBWOccopation'
_Y='ntcTsMuxMonBitRatet'
_X='ntcTsMuxMonPacketRate'
_W='ntcTsMuxMonPacketCount'
_V='ntcTsMuxMonResetCounters'
_U='ntcTsMuxRaPcrRestamp'
_T='ntcTsMuxRaNullPktDrop'
_S='ntcTsMuxRaEnable'
_R='0.0000'
_Q='00000000'
_P='ntcTsMuxMonStatisticsType'
_O='not-accessible'
_N='protectedTsOverIp'
_M='tsOverIp'
_L='ntcInputSelectionInputType'
_K='bps'
_J='Float32TC'
_I='deprecated'
_H='Integer32'
_G='NtcEnable'
_F='DisplayString'
_E='Unsigned32'
_D='read-only'
_C='read-write'
_B='NEWTEC-TSMULTIPLEXING-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
Float32TC,=mibBuilder.importSymbols('FLOAT-TC-MIB',_J)
ntcFunction,=mibBuilder.importSymbols('NEWTEC-MAIN-MIB','ntcFunction')
NtcAlarmState,NtcEnable=mibBuilder.importSymbols('NEWTEC-TC-MIB','NtcAlarmState',_G)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','TextualConvention')
ntcTsMultiplexing=ModuleIdentity((1,3,6,1,4,1,5835,5,2,1600))
if mibBuilder.loadTexts:ntcTsMultiplexing.setRevisions(('2017-07-10 12:00','2016-02-02 07:00','2014-09-09 09:00','2013-09-20 10:00','2013-03-27 10:00','2012-06-28 12:00'))
_NtcTsMuxObjects_ObjectIdentity=ObjectIdentity
ntcTsMuxObjects=_NtcTsMuxObjects_ObjectIdentity((1,3,6,1,4,1,5835,5,2,1600,1))
if mibBuilder.loadTexts:ntcTsMuxObjects.setStatus(_A)
_NtcInputSelectionTable_Object=MibTable
ntcInputSelectionTable=_NtcInputSelectionTable_Object((1,3,6,1,4,1,5835,5,2,1600,1,1))
if mibBuilder.loadTexts:ntcInputSelectionTable.setStatus(_I)
_NtcInputSelectionEntry_Object=MibTableRow
ntcInputSelectionEntry=_NtcInputSelectionEntry_Object((1,3,6,1,4,1,5835,5,2,1600,1,1,1))
ntcInputSelectionEntry.setIndexNames((0,_B,_L))
if mibBuilder.loadTexts:ntcInputSelectionEntry.setStatus(_I)
class _NtcInputSelectionInputType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('asi',0),(_M,1),('mpe',2),('prbs',3),(_N,4)))
_NtcInputSelectionInputType_Type.__name__=_H
_NtcInputSelectionInputType_Object=MibTableColumn
ntcInputSelectionInputType=_NtcInputSelectionInputType_Object((1,3,6,1,4,1,5835,5,2,1600,1,1,1,1),_NtcInputSelectionInputType_Type())
ntcInputSelectionInputType.setMaxAccess(_O)
if mibBuilder.loadTexts:ntcInputSelectionInputType.setStatus(_I)
class _NtcInputSelectionEnable_Type(NtcEnable):defaultValue=0
_NtcInputSelectionEnable_Type.__name__=_G
_NtcInputSelectionEnable_Object=MibTableColumn
ntcInputSelectionEnable=_NtcInputSelectionEnable_Object((1,3,6,1,4,1,5835,5,2,1600,1,1,1,2),_NtcInputSelectionEnable_Type())
ntcInputSelectionEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcInputSelectionEnable.setStatus(_I)
_NtcTsMuxRateAdapter_ObjectIdentity=ObjectIdentity
ntcTsMuxRateAdapter=_NtcTsMuxRateAdapter_ObjectIdentity((1,3,6,1,4,1,5835,5,2,1600,1,2))
if mibBuilder.loadTexts:ntcTsMuxRateAdapter.setStatus(_A)
class _NtcTsMuxRaEnable_Type(NtcEnable):defaultValue=1
_NtcTsMuxRaEnable_Type.__name__=_G
_NtcTsMuxRaEnable_Object=MibScalar
ntcTsMuxRaEnable=_NtcTsMuxRaEnable_Object((1,3,6,1,4,1,5835,5,2,1600,1,2,1),_NtcTsMuxRaEnable_Type())
ntcTsMuxRaEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsMuxRaEnable.setStatus(_A)
class _NtcTsMuxRaNullPktDrop_Type(NtcEnable):defaultValue=1
_NtcTsMuxRaNullPktDrop_Type.__name__=_G
_NtcTsMuxRaNullPktDrop_Object=MibScalar
ntcTsMuxRaNullPktDrop=_NtcTsMuxRaNullPktDrop_Object((1,3,6,1,4,1,5835,5,2,1600,1,2,2),_NtcTsMuxRaNullPktDrop_Type())
ntcTsMuxRaNullPktDrop.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsMuxRaNullPktDrop.setStatus(_A)
class _NtcTsMuxRaPcrRestamp_Type(NtcEnable):defaultValue=1
_NtcTsMuxRaPcrRestamp_Type.__name__=_G
_NtcTsMuxRaPcrRestamp_Object=MibScalar
ntcTsMuxRaPcrRestamp=_NtcTsMuxRaPcrRestamp_Object((1,3,6,1,4,1,5835,5,2,1600,1,2,3),_NtcTsMuxRaPcrRestamp_Type())
ntcTsMuxRaPcrRestamp.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsMuxRaPcrRestamp.setStatus(_A)
_NtcTsMuxMonitor_ObjectIdentity=ObjectIdentity
ntcTsMuxMonitor=_NtcTsMuxMonitor_ObjectIdentity((1,3,6,1,4,1,5835,5,2,1600,1,3))
if mibBuilder.loadTexts:ntcTsMuxMonitor.setStatus(_A)
class _NtcTsMuxMonResetCounters_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('counting',0),('reset',1)))
_NtcTsMuxMonResetCounters_Type.__name__=_H
_NtcTsMuxMonResetCounters_Object=MibScalar
ntcTsMuxMonResetCounters=_NtcTsMuxMonResetCounters_Object((1,3,6,1,4,1,5835,5,2,1600,1,3,1),_NtcTsMuxMonResetCounters_Type())
ntcTsMuxMonResetCounters.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsMuxMonResetCounters.setStatus(_A)
_NtcTsMuxMonStatisticsTable_Object=MibTable
ntcTsMuxMonStatisticsTable=_NtcTsMuxMonStatisticsTable_Object((1,3,6,1,4,1,5835,5,2,1600,1,3,2))
if mibBuilder.loadTexts:ntcTsMuxMonStatisticsTable.setStatus(_A)
_NtcTsMuxMonStatisticsEntry_Object=MibTableRow
ntcTsMuxMonStatisticsEntry=_NtcTsMuxMonStatisticsEntry_Object((1,3,6,1,4,1,5835,5,2,1600,1,3,2,1))
ntcTsMuxMonStatisticsEntry.setIndexNames((0,_B,_P))
if mibBuilder.loadTexts:ntcTsMuxMonStatisticsEntry.setStatus(_A)
class _NtcTsMuxMonStatisticsType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('asi',0),(_M,1),('mpe',2),('inputNullPackets',3),('signalling',4),('outputNullPackets',5),('outputDataPackets',6),('outputTotalPackets',7),(_N,8)))
_NtcTsMuxMonStatisticsType_Type.__name__=_H
_NtcTsMuxMonStatisticsType_Object=MibTableColumn
ntcTsMuxMonStatisticsType=_NtcTsMuxMonStatisticsType_Object((1,3,6,1,4,1,5835,5,2,1600,1,3,2,1,1),_NtcTsMuxMonStatisticsType_Type())
ntcTsMuxMonStatisticsType.setMaxAccess(_O)
if mibBuilder.loadTexts:ntcTsMuxMonStatisticsType.setStatus(_A)
_NtcTsMuxMonPacketCount_Type=Counter32
_NtcTsMuxMonPacketCount_Object=MibTableColumn
ntcTsMuxMonPacketCount=_NtcTsMuxMonPacketCount_Object((1,3,6,1,4,1,5835,5,2,1600,1,3,2,1,2),_NtcTsMuxMonPacketCount_Type())
ntcTsMuxMonPacketCount.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcTsMuxMonPacketCount.setStatus(_A)
if mibBuilder.loadTexts:ntcTsMuxMonPacketCount.setUnits('packets')
_NtcTsMuxMonPacketRate_Type=Counter32
_NtcTsMuxMonPacketRate_Object=MibTableColumn
ntcTsMuxMonPacketRate=_NtcTsMuxMonPacketRate_Object((1,3,6,1,4,1,5835,5,2,1600,1,3,2,1,3),_NtcTsMuxMonPacketRate_Type())
ntcTsMuxMonPacketRate.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcTsMuxMonPacketRate.setStatus(_A)
if mibBuilder.loadTexts:ntcTsMuxMonPacketRate.setUnits('pps')
_NtcTsMuxMonBitRatet_Type=Counter32
_NtcTsMuxMonBitRatet_Object=MibTableColumn
ntcTsMuxMonBitRatet=_NtcTsMuxMonBitRatet_Object((1,3,6,1,4,1,5835,5,2,1600,1,3,2,1,4),_NtcTsMuxMonBitRatet_Type())
ntcTsMuxMonBitRatet.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcTsMuxMonBitRatet.setStatus(_A)
if mibBuilder.loadTexts:ntcTsMuxMonBitRatet.setUnits(_K)
class _NtcTsMuxMonBWOccopation_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_NtcTsMuxMonBWOccopation_Type.__name__=_E
_NtcTsMuxMonBWOccopation_Object=MibTableColumn
ntcTsMuxMonBWOccopation=_NtcTsMuxMonBWOccopation_Object((1,3,6,1,4,1,5835,5,2,1600,1,3,2,1,5),_NtcTsMuxMonBWOccopation_Type())
ntcTsMuxMonBWOccopation.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcTsMuxMonBWOccopation.setStatus(_A)
if mibBuilder.loadTexts:ntcTsMuxMonBWOccopation.setUnits('%')
_NtcTsMuxCarrierId_ObjectIdentity=ObjectIdentity
ntcTsMuxCarrierId=_NtcTsMuxCarrierId_ObjectIdentity((1,3,6,1,4,1,5835,5,2,1600,1,4))
if mibBuilder.loadTexts:ntcTsMuxCarrierId.setStatus(_A)
class _NtcTsMuxCarIdEnable_Type(NtcEnable):defaultValue=0
_NtcTsMuxCarIdEnable_Type.__name__=_G
_NtcTsMuxCarIdEnable_Object=MibScalar
ntcTsMuxCarIdEnable=_NtcTsMuxCarIdEnable_Object((1,3,6,1,4,1,5835,5,2,1600,1,4,1),_NtcTsMuxCarIdEnable_Type())
ntcTsMuxCarIdEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsMuxCarIdEnable.setStatus(_A)
class _NtcTsMuxCarIdDescriptorTag_Type(Unsigned32):defaultValue=196;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(192,254))
_NtcTsMuxCarIdDescriptorTag_Type.__name__=_E
_NtcTsMuxCarIdDescriptorTag_Object=MibScalar
ntcTsMuxCarIdDescriptorTag=_NtcTsMuxCarIdDescriptorTag_Object((1,3,6,1,4,1,5835,5,2,1600,1,4,2),_NtcTsMuxCarIdDescriptorTag_Type())
ntcTsMuxCarIdDescriptorTag.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsMuxCarIdDescriptorTag.setStatus(_A)
class _NtcTsMuxCarIdModMfg_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,5))
_NtcTsMuxCarIdModMfg_Type.__name__=_F
_NtcTsMuxCarIdModMfg_Object=MibScalar
ntcTsMuxCarIdModMfg=_NtcTsMuxCarIdModMfg_Object((1,3,6,1,4,1,5835,5,2,1600,1,4,3),_NtcTsMuxCarIdModMfg_Type())
ntcTsMuxCarIdModMfg.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcTsMuxCarIdModMfg.setStatus(_A)
class _NtcTsMuxCarIdModSerialNr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,12))
_NtcTsMuxCarIdModSerialNr_Type.__name__=_F
_NtcTsMuxCarIdModSerialNr_Object=MibScalar
ntcTsMuxCarIdModSerialNr=_NtcTsMuxCarIdModSerialNr_Object((1,3,6,1,4,1,5835,5,2,1600,1,4,4),_NtcTsMuxCarIdModSerialNr_Type())
ntcTsMuxCarIdModSerialNr.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcTsMuxCarIdModSerialNr.setStatus(_A)
class _NtcTsMuxCarIdCarrierIdentifier_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,5))
_NtcTsMuxCarIdCarrierIdentifier_Type.__name__=_F
_NtcTsMuxCarIdCarrierIdentifier_Object=MibScalar
ntcTsMuxCarIdCarrierIdentifier=_NtcTsMuxCarIdCarrierIdentifier_Object((1,3,6,1,4,1,5835,5,2,1600,1,4,5),_NtcTsMuxCarIdCarrierIdentifier_Type())
ntcTsMuxCarIdCarrierIdentifier.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsMuxCarIdCarrierIdentifier.setStatus(_A)
class _NtcTsMuxCarIdTelephoneNr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,17))
_NtcTsMuxCarIdTelephoneNr_Type.__name__=_F
_NtcTsMuxCarIdTelephoneNr_Object=MibScalar
ntcTsMuxCarIdTelephoneNr=_NtcTsMuxCarIdTelephoneNr_Object((1,3,6,1,4,1,5835,5,2,1600,1,4,6),_NtcTsMuxCarIdTelephoneNr_Type())
ntcTsMuxCarIdTelephoneNr.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsMuxCarIdTelephoneNr.setStatus(_A)
class _NtcTsMuxCarIdLongitude_Type(Float32TC):defaultHexValue=_Q
_NtcTsMuxCarIdLongitude_Type.__name__=_J
_NtcTsMuxCarIdLongitude_Object=MibScalar
ntcTsMuxCarIdLongitude=_NtcTsMuxCarIdLongitude_Object((1,3,6,1,4,1,5835,5,2,1600,1,4,7),_NtcTsMuxCarIdLongitude_Type())
ntcTsMuxCarIdLongitude.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsMuxCarIdLongitude.setStatus(_A)
class _NtcTsMuxCarIdLatitude_Type(Float32TC):defaultHexValue=_Q
_NtcTsMuxCarIdLatitude_Type.__name__=_J
_NtcTsMuxCarIdLatitude_Object=MibScalar
ntcTsMuxCarIdLatitude=_NtcTsMuxCarIdLatitude_Object((1,3,6,1,4,1,5835,5,2,1600,1,4,8),_NtcTsMuxCarIdLatitude_Type())
ntcTsMuxCarIdLatitude.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsMuxCarIdLatitude.setStatus(_A)
class _NtcTsMuxCarIdUserInfo_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_NtcTsMuxCarIdUserInfo_Type.__name__=_F
_NtcTsMuxCarIdUserInfo_Object=MibScalar
ntcTsMuxCarIdUserInfo=_NtcTsMuxCarIdUserInfo_Object((1,3,6,1,4,1,5835,5,2,1600,1,4,9),_NtcTsMuxCarIdUserInfo_Type())
ntcTsMuxCarIdUserInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsMuxCarIdUserInfo.setStatus(_A)
class _NtcTsMuxCarIdLongitudeString_Type(DisplayString):defaultValue=OctetString(_R);subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,9))
_NtcTsMuxCarIdLongitudeString_Type.__name__=_F
_NtcTsMuxCarIdLongitudeString_Object=MibScalar
ntcTsMuxCarIdLongitudeString=_NtcTsMuxCarIdLongitudeString_Object((1,3,6,1,4,1,5835,5,2,1600,1,4,10),_NtcTsMuxCarIdLongitudeString_Type())
ntcTsMuxCarIdLongitudeString.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsMuxCarIdLongitudeString.setStatus(_A)
class _NtcTsMuxCarIdLatitudeString_Type(DisplayString):defaultValue=OctetString(_R);subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,9))
_NtcTsMuxCarIdLatitudeString_Type.__name__=_F
_NtcTsMuxCarIdLatitudeString_Object=MibScalar
ntcTsMuxCarIdLatitudeString=_NtcTsMuxCarIdLatitudeString_Object((1,3,6,1,4,1,5835,5,2,1600,1,4,11),_NtcTsMuxCarIdLatitudeString_Type())
ntcTsMuxCarIdLatitudeString.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsMuxCarIdLatitudeString.setStatus(_A)
_NtcTsMuxSignalling_ObjectIdentity=ObjectIdentity
ntcTsMuxSignalling=_NtcTsMuxSignalling_ObjectIdentity((1,3,6,1,4,1,5835,5,2,1600,1,5))
if mibBuilder.loadTexts:ntcTsMuxSignalling.setStatus(_A)
class _NtcTsMuxSigNetworkId_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_NtcTsMuxSigNetworkId_Type.__name__=_E
_NtcTsMuxSigNetworkId_Object=MibScalar
ntcTsMuxSigNetworkId=_NtcTsMuxSigNetworkId_Object((1,3,6,1,4,1,5835,5,2,1600,1,5,1),_NtcTsMuxSigNetworkId_Type())
ntcTsMuxSigNetworkId.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsMuxSigNetworkId.setStatus(_A)
class _NtcTsMuxSigTransportStreamId_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_NtcTsMuxSigTransportStreamId_Type.__name__=_E
_NtcTsMuxSigTransportStreamId_Object=MibScalar
ntcTsMuxSigTransportStreamId=_NtcTsMuxSigTransportStreamId_Object((1,3,6,1,4,1,5835,5,2,1600,1,5,2),_NtcTsMuxSigTransportStreamId_Type())
ntcTsMuxSigTransportStreamId.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsMuxSigTransportStreamId.setStatus(_A)
class _NtcTsMuxSigPatRepetitionRate_Type(Unsigned32):defaultValue=400;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(25,500))
_NtcTsMuxSigPatRepetitionRate_Type.__name__=_E
_NtcTsMuxSigPatRepetitionRate_Object=MibScalar
ntcTsMuxSigPatRepetitionRate=_NtcTsMuxSigPatRepetitionRate_Object((1,3,6,1,4,1,5835,5,2,1600,1,5,3),_NtcTsMuxSigPatRepetitionRate_Type())
ntcTsMuxSigPatRepetitionRate.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsMuxSigPatRepetitionRate.setStatus(_A)
if mibBuilder.loadTexts:ntcTsMuxSigPatRepetitionRate.setUnits('ms')
class _NtcTsMuxSigSdtRepetitionRate_Type(Unsigned32):defaultValue=500;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(25,2000))
_NtcTsMuxSigSdtRepetitionRate_Type.__name__=_E
_NtcTsMuxSigSdtRepetitionRate_Object=MibScalar
ntcTsMuxSigSdtRepetitionRate=_NtcTsMuxSigSdtRepetitionRate_Object((1,3,6,1,4,1,5835,5,2,1600,1,5,4),_NtcTsMuxSigSdtRepetitionRate_Type())
ntcTsMuxSigSdtRepetitionRate.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsMuxSigSdtRepetitionRate.setStatus(_A)
if mibBuilder.loadTexts:ntcTsMuxSigSdtRepetitionRate.setUnits('ms')
class _NtcTsMuxSigPmtRepetitionRate_Type(Unsigned32):defaultValue=400;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(25,500))
_NtcTsMuxSigPmtRepetitionRate_Type.__name__=_E
_NtcTsMuxSigPmtRepetitionRate_Object=MibScalar
ntcTsMuxSigPmtRepetitionRate=_NtcTsMuxSigPmtRepetitionRate_Object((1,3,6,1,4,1,5835,5,2,1600,1,5,5),_NtcTsMuxSigPmtRepetitionRate_Type())
ntcTsMuxSigPmtRepetitionRate.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsMuxSigPmtRepetitionRate.setStatus(_A)
if mibBuilder.loadTexts:ntcTsMuxSigPmtRepetitionRate.setUnits('ms')
_NtcTsMuxAlarm_ObjectIdentity=ObjectIdentity
ntcTsMuxAlarm=_NtcTsMuxAlarm_ObjectIdentity((1,3,6,1,4,1,5835,5,2,1600,1,6))
if mibBuilder.loadTexts:ntcTsMuxAlarm.setStatus(_A)
_NtcTsMuxAlmLocalPidOnInput_Type=NtcAlarmState
_NtcTsMuxAlmLocalPidOnInput_Object=MibScalar
ntcTsMuxAlmLocalPidOnInput=_NtcTsMuxAlmLocalPidOnInput_Object((1,3,6,1,4,1,5835,5,2,1600,1,6,1),_NtcTsMuxAlmLocalPidOnInput_Type())
ntcTsMuxAlmLocalPidOnInput.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcTsMuxAlmLocalPidOnInput.setStatus(_A)
_NtcTsMuxAlmSignalTableProcError_Type=NtcAlarmState
_NtcTsMuxAlmSignalTableProcError_Object=MibScalar
ntcTsMuxAlmSignalTableProcError=_NtcTsMuxAlmSignalTableProcError_Object((1,3,6,1,4,1,5835,5,2,1600,1,6,2),_NtcTsMuxAlmSignalTableProcError_Type())
ntcTsMuxAlmSignalTableProcError.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcTsMuxAlmSignalTableProcError.setStatus(_A)
_NtcTsMuxAlmSignalOverflow_Type=NtcAlarmState
_NtcTsMuxAlmSignalOverflow_Object=MibScalar
ntcTsMuxAlmSignalOverflow=_NtcTsMuxAlmSignalOverflow_Object((1,3,6,1,4,1,5835,5,2,1600,1,6,3),_NtcTsMuxAlmSignalOverflow_Type())
ntcTsMuxAlmSignalOverflow.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcTsMuxAlmSignalOverflow.setStatus(_A)
_NtcTsMuxAlmBufferOverflow_Type=NtcAlarmState
_NtcTsMuxAlmBufferOverflow_Object=MibScalar
ntcTsMuxAlmBufferOverflow=_NtcTsMuxAlmBufferOverflow_Object((1,3,6,1,4,1,5835,5,2,1600,1,6,4),_NtcTsMuxAlmBufferOverflow_Type())
ntcTsMuxAlmBufferOverflow.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcTsMuxAlmBufferOverflow.setStatus(_A)
_NtcTsMuxNpRateOutRange_Type=NtcAlarmState
_NtcTsMuxNpRateOutRange_Object=MibScalar
ntcTsMuxNpRateOutRange=_NtcTsMuxNpRateOutRange_Object((1,3,6,1,4,1,5835,5,2,1600,1,6,5),_NtcTsMuxNpRateOutRange_Type())
ntcTsMuxNpRateOutRange.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcTsMuxNpRateOutRange.setStatus(_A)
_NtcTsMuxNpRangeThr_ObjectIdentity=ObjectIdentity
ntcTsMuxNpRangeThr=_NtcTsMuxNpRangeThr_ObjectIdentity((1,3,6,1,4,1,5835,5,2,1600,1,7))
if mibBuilder.loadTexts:ntcTsMuxNpRangeThr.setStatus(_A)
class _NtcTsMuxNpRangeThrEnable_Type(NtcEnable):defaultValue=0
_NtcTsMuxNpRangeThrEnable_Type.__name__=_G
_NtcTsMuxNpRangeThrEnable_Object=MibScalar
ntcTsMuxNpRangeThrEnable=_NtcTsMuxNpRangeThrEnable_Object((1,3,6,1,4,1,5835,5,2,1600,1,7,1),_NtcTsMuxNpRangeThrEnable_Type())
ntcTsMuxNpRangeThrEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsMuxNpRangeThrEnable.setStatus(_A)
class _NtcTsMuxNpRangeThrMinRate_Type(Unsigned32):defaultValue=0
_NtcTsMuxNpRangeThrMinRate_Type.__name__=_E
_NtcTsMuxNpRangeThrMinRate_Object=MibScalar
ntcTsMuxNpRangeThrMinRate=_NtcTsMuxNpRangeThrMinRate_Object((1,3,6,1,4,1,5835,5,2,1600,1,7,2),_NtcTsMuxNpRangeThrMinRate_Type())
ntcTsMuxNpRangeThrMinRate.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsMuxNpRangeThrMinRate.setStatus(_A)
if mibBuilder.loadTexts:ntcTsMuxNpRangeThrMinRate.setUnits(_K)
class _NtcTsMuxNpRangeThrMaxRate_Type(Unsigned32):defaultValue=0
_NtcTsMuxNpRangeThrMaxRate_Type.__name__=_E
_NtcTsMuxNpRangeThrMaxRate_Object=MibScalar
ntcTsMuxNpRangeThrMaxRate=_NtcTsMuxNpRangeThrMaxRate_Object((1,3,6,1,4,1,5835,5,2,1600,1,7,3),_NtcTsMuxNpRangeThrMaxRate_Type())
ntcTsMuxNpRangeThrMaxRate.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsMuxNpRangeThrMaxRate.setStatus(_A)
if mibBuilder.loadTexts:ntcTsMuxNpRangeThrMaxRate.setUnits(_K)
class _NtcTsMuxNpRangeTimeWindow_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,50))
_NtcTsMuxNpRangeTimeWindow_Type.__name__=_H
_NtcTsMuxNpRangeTimeWindow_Object=MibScalar
ntcTsMuxNpRangeTimeWindow=_NtcTsMuxNpRangeTimeWindow_Object((1,3,6,1,4,1,5835,5,2,1600,1,7,4),_NtcTsMuxNpRangeTimeWindow_Type())
ntcTsMuxNpRangeTimeWindow.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsMuxNpRangeTimeWindow.setStatus(_A)
if mibBuilder.loadTexts:ntcTsMuxNpRangeTimeWindow.setUnits('s')
_NtcTsMuxConformance_ObjectIdentity=ObjectIdentity
ntcTsMuxConformance=_NtcTsMuxConformance_ObjectIdentity((1,3,6,1,4,1,5835,5,2,1600,2))
if mibBuilder.loadTexts:ntcTsMuxConformance.setStatus(_A)
_NtcTsMuxConfCompliance_ObjectIdentity=ObjectIdentity
ntcTsMuxConfCompliance=_NtcTsMuxConfCompliance_ObjectIdentity((1,3,6,1,4,1,5835,5,2,1600,2,1))
if mibBuilder.loadTexts:ntcTsMuxConfCompliance.setStatus(_A)
_NtcTsMuxConfGroup_ObjectIdentity=ObjectIdentity
ntcTsMuxConfGroup=_NtcTsMuxConfGroup_ObjectIdentity((1,3,6,1,4,1,5835,5,2,1600,2,2))
if mibBuilder.loadTexts:ntcTsMuxConfGroup.setStatus(_A)
ntcTsMuxConfGrpV1Standard=ObjectGroup((1,3,6,1,4,1,5835,5,2,1600,2,2,1))
ntcTsMuxConfGrpV1Standard.setObjects(*((_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y)))
if mibBuilder.loadTexts:ntcTsMuxConfGrpV1Standard.setStatus(_A)
ntcTsMuxConfGrpObsolete=ObjectGroup((1,3,6,1,4,1,5835,5,2,1600,2,2,2))
ntcTsMuxConfGrpObsolete.setObjects((_B,_z))
if mibBuilder.loadTexts:ntcTsMuxConfGrpObsolete.setStatus('obsolete')
ntcTsMuxConfCompV1Standard=ModuleCompliance((1,3,6,1,4,1,5835,5,2,1600,2,1,1))
ntcTsMuxConfCompV1Standard.setObjects((_B,_A0))
if mibBuilder.loadTexts:ntcTsMuxConfCompV1Standard.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ntcTsMultiplexing':ntcTsMultiplexing,'ntcTsMuxObjects':ntcTsMuxObjects,'ntcInputSelectionTable':ntcInputSelectionTable,'ntcInputSelectionEntry':ntcInputSelectionEntry,_L:ntcInputSelectionInputType,_z:ntcInputSelectionEnable,'ntcTsMuxRateAdapter':ntcTsMuxRateAdapter,_S:ntcTsMuxRaEnable,_T:ntcTsMuxRaNullPktDrop,_U:ntcTsMuxRaPcrRestamp,'ntcTsMuxMonitor':ntcTsMuxMonitor,_V:ntcTsMuxMonResetCounters,'ntcTsMuxMonStatisticsTable':ntcTsMuxMonStatisticsTable,'ntcTsMuxMonStatisticsEntry':ntcTsMuxMonStatisticsEntry,_P:ntcTsMuxMonStatisticsType,_W:ntcTsMuxMonPacketCount,_X:ntcTsMuxMonPacketRate,_Y:ntcTsMuxMonBitRatet,_Z:ntcTsMuxMonBWOccopation,'ntcTsMuxCarrierId':ntcTsMuxCarrierId,_a:ntcTsMuxCarIdEnable,_b:ntcTsMuxCarIdDescriptorTag,_c:ntcTsMuxCarIdModMfg,_d:ntcTsMuxCarIdModSerialNr,_e:ntcTsMuxCarIdCarrierIdentifier,_f:ntcTsMuxCarIdTelephoneNr,_g:ntcTsMuxCarIdLongitude,_h:ntcTsMuxCarIdLatitude,_i:ntcTsMuxCarIdUserInfo,_j:ntcTsMuxCarIdLongitudeString,_k:ntcTsMuxCarIdLatitudeString,'ntcTsMuxSignalling':ntcTsMuxSignalling,_l:ntcTsMuxSigNetworkId,_m:ntcTsMuxSigTransportStreamId,_n:ntcTsMuxSigPatRepetitionRate,_o:ntcTsMuxSigSdtRepetitionRate,_p:ntcTsMuxSigPmtRepetitionRate,'ntcTsMuxAlarm':ntcTsMuxAlarm,_q:ntcTsMuxAlmLocalPidOnInput,_r:ntcTsMuxAlmSignalTableProcError,_s:ntcTsMuxAlmSignalOverflow,_t:ntcTsMuxAlmBufferOverflow,_u:ntcTsMuxNpRateOutRange,'ntcTsMuxNpRangeThr':ntcTsMuxNpRangeThr,_v:ntcTsMuxNpRangeThrEnable,_w:ntcTsMuxNpRangeThrMinRate,_x:ntcTsMuxNpRangeThrMaxRate,_y:ntcTsMuxNpRangeTimeWindow,'ntcTsMuxConformance':ntcTsMuxConformance,'ntcTsMuxConfCompliance':ntcTsMuxConfCompliance,'ntcTsMuxConfCompV1Standard':ntcTsMuxConfCompV1Standard,'ntcTsMuxConfGroup':ntcTsMuxConfGroup,_A0:ntcTsMuxConfGrpV1Standard,'ntcTsMuxConfGrpObsolete':ntcTsMuxConfGrpObsolete})