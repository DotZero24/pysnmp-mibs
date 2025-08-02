_A3='radioGroup'
_A2='radioBandChanged'
_A1='radioFreqChanged'
_A0='rmSelectChannel'
_z='rmBandsBand'
_y='rmChainMode'
_x='rmNoiseFloor'
_w='rmDistanceAuto'
_v='radioStatRecvBytes'
_u='radioStatRecvPackets'
_t='radioStatErrors'
_s='radioStatRepeatBytes'
_r='radioStatBytes'
_q='radioStatRepeatPackets'
_p='radioStatRepeats'
_o='radioStatPackets'
_n='rmBitratesBitrate'
_m='rmFrequenciesFreq'
_l='rmPowerLevelsPower'
_k='rmBCsid'
_j='rmWOCD'
_i='rmTXVRT'
_h='rmTXRT'
_g='rmPowerCtl'
_f='rmLongRange'
_e='rmBurst'
_d='rmDistance'
_c='rmAntenna'
_b='rmModulation'
_a='rmCurPowerLevel'
_Z='rmBitRate'
_Y='rmType'
_X='tenth dBm.'
_W='OctetString'
_V='rmBandwidth'
_U='rmFrequency'
_T='rmBandsValIndex'
_S='rmBandsIfIndex'
_R='radioStatMacAddress'
_Q='rmBitratesValIndex'
_P='rmBitratesIfIndex'
_O='rmFrequenciesValIndex'
_N='rmFrequenciesIfIndex'
_M='rmPowerLevelsValIndex'
_L='rmPowerLevelsIfIndex'
_K='sysTrapSequence'
_J='sysSerialNumber'
_I='rmPropertiesIfIndex'
_H='AQUASYSTEM-MIB'
_G='off'
_F='on'
_E='read-write'
_D='Integer32'
_C='read-only'
_B='AQUARADIO-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_W,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
sysSerialNumber,sysTrapSequence=mibBuilder.importSymbols(_H,_J,_K)
ifIndex,=mibBuilder.importSymbols('IF-MIB','ifIndex')
wanflex,=mibBuilder.importSymbols('INFINET-MIB','wanflex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
aquaradioMIB=ModuleIdentity((1,3,6,1,4,1,3942,1,1,2))
if mibBuilder.loadTexts:aquaradioMIB.setRevisions(('2014-09-22 05:56','2013-07-26 04:27','2013-04-08 11:40','2013-04-08 10:59','2009-11-10 11:56','2009-10-30 08:38','2009-05-12 11:22','2007-11-08 13:09','2004-10-11 16:28'))
class RadioSID(TextualConvention,Integer32):status=_A;displayHint='x'
_RmPropertiesTable_Object=MibTable
rmPropertiesTable=_RmPropertiesTable_Object((1,3,6,1,4,1,3942,1,1,2,1))
if mibBuilder.loadTexts:rmPropertiesTable.setStatus(_A)
_RmPropertiesEntry_Object=MibTableRow
rmPropertiesEntry=_RmPropertiesEntry_Object((1,3,6,1,4,1,3942,1,1,2,1,1))
rmPropertiesEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:rmPropertiesEntry.setStatus(_A)
class _RmPropertiesIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_RmPropertiesIfIndex_Type.__name__=_D
_RmPropertiesIfIndex_Object=MibTableColumn
rmPropertiesIfIndex=_RmPropertiesIfIndex_Object((1,3,6,1,4,1,3942,1,1,2,1,1,1),_RmPropertiesIfIndex_Type())
rmPropertiesIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:rmPropertiesIfIndex.setStatus(_A)
_RmType_Type=OctetString
_RmType_Object=MibTableColumn
rmType=_RmType_Object((1,3,6,1,4,1,3942,1,1,2,1,1,2),_RmType_Type())
rmType.setMaxAccess(_C)
if mibBuilder.loadTexts:rmType.setStatus(_A)
_RmFrequency_Type=Integer32
_RmFrequency_Object=MibTableColumn
rmFrequency=_RmFrequency_Object((1,3,6,1,4,1,3942,1,1,2,1,1,3),_RmFrequency_Type())
rmFrequency.setMaxAccess(_E)
if mibBuilder.loadTexts:rmFrequency.setStatus(_A)
if mibBuilder.loadTexts:rmFrequency.setUnits('KHz')
_RmBitRate_Type=Integer32
_RmBitRate_Object=MibTableColumn
rmBitRate=_RmBitRate_Object((1,3,6,1,4,1,3942,1,1,2,1,1,4),_RmBitRate_Type())
rmBitRate.setMaxAccess(_E)
if mibBuilder.loadTexts:rmBitRate.setStatus(_A)
_RmSid_Type=RadioSID
_RmSid_Object=MibTableColumn
rmSid=_RmSid_Object((1,3,6,1,4,1,3942,1,1,2,1,1,5),_RmSid_Type())
rmSid.setMaxAccess(_E)
if mibBuilder.loadTexts:rmSid.setStatus(_A)
_RmCurPowerLevel_Type=Integer32
_RmCurPowerLevel_Object=MibTableColumn
rmCurPowerLevel=_RmCurPowerLevel_Object((1,3,6,1,4,1,3942,1,1,2,1,1,6),_RmCurPowerLevel_Type())
rmCurPowerLevel.setMaxAccess(_E)
if mibBuilder.loadTexts:rmCurPowerLevel.setStatus(_A)
if mibBuilder.loadTexts:rmCurPowerLevel.setUnits(_X)
class _RmModulation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('irrelevant',0),('cck',1),('mok',2)))
_RmModulation_Type.__name__=_D
_RmModulation_Object=MibTableColumn
rmModulation=_RmModulation_Object((1,3,6,1,4,1,3942,1,1,2,1,1,7),_RmModulation_Type())
rmModulation.setMaxAccess(_E)
if mibBuilder.loadTexts:rmModulation.setStatus(_A)
class _RmAntenna_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('right',1),('left',2),('div',3),('both',4),('txr',5),('txl',6)))
_RmAntenna_Type.__name__=_D
_RmAntenna_Object=MibTableColumn
rmAntenna=_RmAntenna_Object((1,3,6,1,4,1,3942,1,1,2,1,1,8),_RmAntenna_Type())
rmAntenna.setMaxAccess(_E)
if mibBuilder.loadTexts:rmAntenna.setStatus(_A)
_RmDistance_Type=Integer32
_RmDistance_Object=MibTableColumn
rmDistance=_RmDistance_Object((1,3,6,1,4,1,3942,1,1,2,1,1,9),_RmDistance_Type())
rmDistance.setMaxAccess(_E)
if mibBuilder.loadTexts:rmDistance.setStatus(_A)
if mibBuilder.loadTexts:rmDistance.setUnits('kilometers')
class _RmBurst_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_RmBurst_Type.__name__=_D
_RmBurst_Object=MibTableColumn
rmBurst=_RmBurst_Object((1,3,6,1,4,1,3942,1,1,2,1,1,10),_RmBurst_Type())
rmBurst.setMaxAccess(_E)
if mibBuilder.loadTexts:rmBurst.setStatus(_A)
class _RmLongRange_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_RmLongRange_Type.__name__=_D
_RmLongRange_Object=MibTableColumn
rmLongRange=_RmLongRange_Object((1,3,6,1,4,1,3942,1,1,2,1,1,11),_RmLongRange_Type())
rmLongRange.setMaxAccess(_E)
if mibBuilder.loadTexts:rmLongRange.setStatus(_A)
class _RmPowerCtl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_RmPowerCtl_Type.__name__=_D
_RmPowerCtl_Object=MibTableColumn
rmPowerCtl=_RmPowerCtl_Object((1,3,6,1,4,1,3942,1,1,2,1,1,12),_RmPowerCtl_Type())
rmPowerCtl.setMaxAccess(_E)
if mibBuilder.loadTexts:rmPowerCtl.setStatus(_A)
_RmTXRT_Type=Integer32
_RmTXRT_Object=MibTableColumn
rmTXRT=_RmTXRT_Object((1,3,6,1,4,1,3942,1,1,2,1,1,13),_RmTXRT_Type())
rmTXRT.setMaxAccess(_E)
if mibBuilder.loadTexts:rmTXRT.setStatus(_A)
_RmTXVRT_Type=Integer32
_RmTXVRT_Object=MibTableColumn
rmTXVRT=_RmTXVRT_Object((1,3,6,1,4,1,3942,1,1,2,1,1,14),_RmTXVRT_Type())
rmTXVRT.setMaxAccess(_E)
if mibBuilder.loadTexts:rmTXVRT.setStatus(_A)
class _RmPTP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_RmPTP_Type.__name__=_D
_RmPTP_Object=MibTableColumn
rmPTP=_RmPTP_Object((1,3,6,1,4,1,3942,1,1,2,1,1,15),_RmPTP_Type())
rmPTP.setMaxAccess(_E)
if mibBuilder.loadTexts:rmPTP.setStatus(_A)
class _RmWOCD_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_RmWOCD_Type.__name__=_D
_RmWOCD_Object=MibTableColumn
rmWOCD=_RmWOCD_Object((1,3,6,1,4,1,3942,1,1,2,1,1,16),_RmWOCD_Type())
rmWOCD.setMaxAccess(_E)
if mibBuilder.loadTexts:rmWOCD.setStatus(_A)
class _RmBCsid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_RmBCsid_Type.__name__=_D
_RmBCsid_Object=MibTableColumn
rmBCsid=_RmBCsid_Object((1,3,6,1,4,1,3942,1,1,2,1,1,17),_RmBCsid_Type())
rmBCsid.setMaxAccess(_E)
if mibBuilder.loadTexts:rmBCsid.setStatus(_A)
class _RmDistanceAuto_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_RmDistanceAuto_Type.__name__=_D
_RmDistanceAuto_Object=MibTableColumn
rmDistanceAuto=_RmDistanceAuto_Object((1,3,6,1,4,1,3942,1,1,2,1,1,18),_RmDistanceAuto_Type())
rmDistanceAuto.setMaxAccess(_E)
if mibBuilder.loadTexts:rmDistanceAuto.setStatus(_A)
_RmNoiseFloor_Type=Integer32
_RmNoiseFloor_Object=MibTableColumn
rmNoiseFloor=_RmNoiseFloor_Object((1,3,6,1,4,1,3942,1,1,2,1,1,19),_RmNoiseFloor_Type())
rmNoiseFloor.setMaxAccess(_C)
if mibBuilder.loadTexts:rmNoiseFloor.setStatus(_A)
_RmBandwidth_Type=Unsigned32
_RmBandwidth_Object=MibTableColumn
rmBandwidth=_RmBandwidth_Object((1,3,6,1,4,1,3942,1,1,2,1,1,20),_RmBandwidth_Type())
rmBandwidth.setMaxAccess(_E)
if mibBuilder.loadTexts:rmBandwidth.setStatus(_A)
if mibBuilder.loadTexts:rmBandwidth.setUnits('KHz')
class _RmChainMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('miso',1),('mimo',2)))
_RmChainMode_Type.__name__=_D
_RmChainMode_Object=MibTableColumn
rmChainMode=_RmChainMode_Object((1,3,6,1,4,1,3942,1,1,2,1,1,21),_RmChainMode_Type())
rmChainMode.setMaxAccess(_C)
if mibBuilder.loadTexts:rmChainMode.setStatus(_A)
class _RmSelectChannel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('reading-stub',0),('new',1),('renew',2)))
_RmSelectChannel_Type.__name__=_D
_RmSelectChannel_Object=MibTableColumn
rmSelectChannel=_RmSelectChannel_Object((1,3,6,1,4,1,3942,1,1,2,1,1,22),_RmSelectChannel_Type())
rmSelectChannel.setMaxAccess(_E)
if mibBuilder.loadTexts:rmSelectChannel.setStatus(_A)
_RmPowerLevelsTable_Object=MibTable
rmPowerLevelsTable=_RmPowerLevelsTable_Object((1,3,6,1,4,1,3942,1,1,2,4))
if mibBuilder.loadTexts:rmPowerLevelsTable.setStatus(_A)
_RmPowerLevelsEntry_Object=MibTableRow
rmPowerLevelsEntry=_RmPowerLevelsEntry_Object((1,3,6,1,4,1,3942,1,1,2,4,1))
rmPowerLevelsEntry.setIndexNames((0,_B,_L),(0,_B,_M))
if mibBuilder.loadTexts:rmPowerLevelsEntry.setStatus(_A)
class _RmPowerLevelsIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_RmPowerLevelsIfIndex_Type.__name__=_D
_RmPowerLevelsIfIndex_Object=MibTableColumn
rmPowerLevelsIfIndex=_RmPowerLevelsIfIndex_Object((1,3,6,1,4,1,3942,1,1,2,4,1,1),_RmPowerLevelsIfIndex_Type())
rmPowerLevelsIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:rmPowerLevelsIfIndex.setStatus(_A)
class _RmPowerLevelsValIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_RmPowerLevelsValIndex_Type.__name__=_D
_RmPowerLevelsValIndex_Object=MibTableColumn
rmPowerLevelsValIndex=_RmPowerLevelsValIndex_Object((1,3,6,1,4,1,3942,1,1,2,4,1,2),_RmPowerLevelsValIndex_Type())
rmPowerLevelsValIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:rmPowerLevelsValIndex.setStatus(_A)
_RmPowerLevelsPower_Type=Integer32
_RmPowerLevelsPower_Object=MibTableColumn
rmPowerLevelsPower=_RmPowerLevelsPower_Object((1,3,6,1,4,1,3942,1,1,2,4,1,3),_RmPowerLevelsPower_Type())
rmPowerLevelsPower.setMaxAccess(_C)
if mibBuilder.loadTexts:rmPowerLevelsPower.setStatus(_A)
if mibBuilder.loadTexts:rmPowerLevelsPower.setUnits(_X)
_RmFrequenciesTable_Object=MibTable
rmFrequenciesTable=_RmFrequenciesTable_Object((1,3,6,1,4,1,3942,1,1,2,5))
if mibBuilder.loadTexts:rmFrequenciesTable.setStatus(_A)
_RmFrequenciesEntry_Object=MibTableRow
rmFrequenciesEntry=_RmFrequenciesEntry_Object((1,3,6,1,4,1,3942,1,1,2,5,1))
rmFrequenciesEntry.setIndexNames((0,_B,_N),(0,_B,_O))
if mibBuilder.loadTexts:rmFrequenciesEntry.setStatus(_A)
class _RmFrequenciesIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_RmFrequenciesIfIndex_Type.__name__=_D
_RmFrequenciesIfIndex_Object=MibTableColumn
rmFrequenciesIfIndex=_RmFrequenciesIfIndex_Object((1,3,6,1,4,1,3942,1,1,2,5,1,1),_RmFrequenciesIfIndex_Type())
rmFrequenciesIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:rmFrequenciesIfIndex.setStatus(_A)
class _RmFrequenciesValIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_RmFrequenciesValIndex_Type.__name__=_D
_RmFrequenciesValIndex_Object=MibTableColumn
rmFrequenciesValIndex=_RmFrequenciesValIndex_Object((1,3,6,1,4,1,3942,1,1,2,5,1,2),_RmFrequenciesValIndex_Type())
rmFrequenciesValIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:rmFrequenciesValIndex.setStatus(_A)
_RmFrequenciesFreq_Type=Integer32
_RmFrequenciesFreq_Object=MibTableColumn
rmFrequenciesFreq=_RmFrequenciesFreq_Object((1,3,6,1,4,1,3942,1,1,2,5,1,3),_RmFrequenciesFreq_Type())
rmFrequenciesFreq.setMaxAccess(_C)
if mibBuilder.loadTexts:rmFrequenciesFreq.setStatus(_A)
_RmBitratesTable_Object=MibTable
rmBitratesTable=_RmBitratesTable_Object((1,3,6,1,4,1,3942,1,1,2,6))
if mibBuilder.loadTexts:rmBitratesTable.setStatus(_A)
_RmBitratesEntry_Object=MibTableRow
rmBitratesEntry=_RmBitratesEntry_Object((1,3,6,1,4,1,3942,1,1,2,6,1))
rmBitratesEntry.setIndexNames((0,_B,_P),(0,_B,_Q))
if mibBuilder.loadTexts:rmBitratesEntry.setStatus(_A)
class _RmBitratesIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_RmBitratesIfIndex_Type.__name__=_D
_RmBitratesIfIndex_Object=MibTableColumn
rmBitratesIfIndex=_RmBitratesIfIndex_Object((1,3,6,1,4,1,3942,1,1,2,6,1,1),_RmBitratesIfIndex_Type())
rmBitratesIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:rmBitratesIfIndex.setStatus(_A)
class _RmBitratesValIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_RmBitratesValIndex_Type.__name__=_D
_RmBitratesValIndex_Object=MibTableColumn
rmBitratesValIndex=_RmBitratesValIndex_Object((1,3,6,1,4,1,3942,1,1,2,6,1,2),_RmBitratesValIndex_Type())
rmBitratesValIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:rmBitratesValIndex.setStatus(_A)
_RmBitratesBitrate_Type=Integer32
_RmBitratesBitrate_Object=MibTableColumn
rmBitratesBitrate=_RmBitratesBitrate_Object((1,3,6,1,4,1,3942,1,1,2,6,1,3),_RmBitratesBitrate_Type())
rmBitratesBitrate.setMaxAccess(_C)
if mibBuilder.loadTexts:rmBitratesBitrate.setStatus(_A)
_RadioStatTable_Object=MibTable
radioStatTable=_RadioStatTable_Object((1,3,6,1,4,1,3942,1,1,2,7))
if mibBuilder.loadTexts:radioStatTable.setStatus(_A)
_RadioStatEntry_Object=MibTableRow
radioStatEntry=_RadioStatEntry_Object((1,3,6,1,4,1,3942,1,1,2,7,1))
radioStatEntry.setIndexNames((0,_B,_R))
if mibBuilder.loadTexts:radioStatEntry.setStatus(_A)
class _RadioStatMacAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_RadioStatMacAddress_Type.__name__=_W
_RadioStatMacAddress_Object=MibTableColumn
radioStatMacAddress=_RadioStatMacAddress_Object((1,3,6,1,4,1,3942,1,1,2,7,1,1),_RadioStatMacAddress_Type())
radioStatMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:radioStatMacAddress.setStatus(_A)
_RadioStatPackets_Type=Counter32
_RadioStatPackets_Object=MibTableColumn
radioStatPackets=_RadioStatPackets_Object((1,3,6,1,4,1,3942,1,1,2,7,1,2),_RadioStatPackets_Type())
radioStatPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:radioStatPackets.setStatus(_A)
_RadioStatRepeats_Type=Counter32
_RadioStatRepeats_Object=MibTableColumn
radioStatRepeats=_RadioStatRepeats_Object((1,3,6,1,4,1,3942,1,1,2,7,1,3),_RadioStatRepeats_Type())
radioStatRepeats.setMaxAccess(_C)
if mibBuilder.loadTexts:radioStatRepeats.setStatus(_A)
_RadioStatRepeatPackets_Type=Counter32
_RadioStatRepeatPackets_Object=MibTableColumn
radioStatRepeatPackets=_RadioStatRepeatPackets_Object((1,3,6,1,4,1,3942,1,1,2,7,1,4),_RadioStatRepeatPackets_Type())
radioStatRepeatPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:radioStatRepeatPackets.setStatus(_A)
_RadioStatBytes_Type=Counter32
_RadioStatBytes_Object=MibTableColumn
radioStatBytes=_RadioStatBytes_Object((1,3,6,1,4,1,3942,1,1,2,7,1,5),_RadioStatBytes_Type())
radioStatBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:radioStatBytes.setStatus(_A)
_RadioStatRepeatBytes_Type=Counter32
_RadioStatRepeatBytes_Object=MibTableColumn
radioStatRepeatBytes=_RadioStatRepeatBytes_Object((1,3,6,1,4,1,3942,1,1,2,7,1,6),_RadioStatRepeatBytes_Type())
radioStatRepeatBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:radioStatRepeatBytes.setStatus(_A)
_RadioStatErrors_Type=Counter32
_RadioStatErrors_Object=MibTableColumn
radioStatErrors=_RadioStatErrors_Object((1,3,6,1,4,1,3942,1,1,2,7,1,7),_RadioStatErrors_Type())
radioStatErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:radioStatErrors.setStatus(_A)
_RadioStatRecvPackets_Type=Counter32
_RadioStatRecvPackets_Object=MibTableColumn
radioStatRecvPackets=_RadioStatRecvPackets_Object((1,3,6,1,4,1,3942,1,1,2,7,1,8),_RadioStatRecvPackets_Type())
radioStatRecvPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:radioStatRecvPackets.setStatus(_A)
_RadioStatRecvBytes_Type=Counter32
_RadioStatRecvBytes_Object=MibTableColumn
radioStatRecvBytes=_RadioStatRecvBytes_Object((1,3,6,1,4,1,3942,1,1,2,7,1,9),_RadioStatRecvBytes_Type())
radioStatRecvBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:radioStatRecvBytes.setStatus(_A)
_RmBandsTable_Object=MibTable
rmBandsTable=_RmBandsTable_Object((1,3,6,1,4,1,3942,1,1,2,8))
if mibBuilder.loadTexts:rmBandsTable.setStatus(_A)
_RmBandsEntry_Object=MibTableRow
rmBandsEntry=_RmBandsEntry_Object((1,3,6,1,4,1,3942,1,1,2,8,1))
rmBandsEntry.setIndexNames((0,_B,_S),(0,_B,_T))
if mibBuilder.loadTexts:rmBandsEntry.setStatus(_A)
class _RmBandsIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_RmBandsIfIndex_Type.__name__=_D
_RmBandsIfIndex_Object=MibTableColumn
rmBandsIfIndex=_RmBandsIfIndex_Object((1,3,6,1,4,1,3942,1,1,2,8,1,1),_RmBandsIfIndex_Type())
rmBandsIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:rmBandsIfIndex.setStatus(_A)
class _RmBandsValIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_RmBandsValIndex_Type.__name__=_D
_RmBandsValIndex_Object=MibTableColumn
rmBandsValIndex=_RmBandsValIndex_Object((1,3,6,1,4,1,3942,1,1,2,8,1,2),_RmBandsValIndex_Type())
rmBandsValIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:rmBandsValIndex.setStatus(_A)
_RmBandsBand_Type=Integer32
_RmBandsBand_Object=MibTableColumn
rmBandsBand=_RmBandsBand_Object((1,3,6,1,4,1,3942,1,1,2,8,1,3),_RmBandsBand_Type())
rmBandsBand.setMaxAccess(_C)
if mibBuilder.loadTexts:rmBandsBand.setStatus(_A)
if mibBuilder.loadTexts:rmBandsBand.setUnits('Hz')
_AquaradioMIBNotificationsPrefix_ObjectIdentity=ObjectIdentity
aquaradioMIBNotificationsPrefix=_AquaradioMIBNotificationsPrefix_ObjectIdentity((1,3,6,1,4,1,3942,1,1,2,17))
_AquaradioMIBnotifications_ObjectIdentity=ObjectIdentity
aquaradioMIBnotifications=_AquaradioMIBnotifications_ObjectIdentity((1,3,6,1,4,1,3942,1,1,2,17,0))
_AquaradioMIBConformance_ObjectIdentity=ObjectIdentity
aquaradioMIBConformance=_AquaradioMIBConformance_ObjectIdentity((1,3,6,1,4,1,3942,1,1,2,18))
_AquaradioMIBCompliances_ObjectIdentity=ObjectIdentity
aquaradioMIBCompliances=_AquaradioMIBCompliances_ObjectIdentity((1,3,6,1,4,1,3942,1,1,2,18,1))
_AquaradioMIBGroups_ObjectIdentity=ObjectIdentity
aquaradioMIBGroups=_AquaradioMIBGroups_ObjectIdentity((1,3,6,1,4,1,3942,1,1,2,18,2))
radioGroup=ObjectGroup((1,3,6,1,4,1,3942,1,1,2,18,2,1))
radioGroup.setObjects(*((_B,_I),(_B,_Y),(_B,_U),(_B,_Z),(_B,'rmSid'),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,'rmPTP'),(_B,_j),(_B,_k),(_B,_L),(_B,_M),(_B,_l),(_B,_N),(_B,_O),(_B,_m),(_B,_P),(_B,_Q),(_B,_n),(_B,_R),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_V),(_B,_y),(_B,_S),(_B,_T),(_B,_z),(_B,_A0)))
if mibBuilder.loadTexts:radioGroup.setStatus(_A)
radioFreqChanged=NotificationType((1,3,6,1,4,1,3942,1,1,2,17,0,1))
radioFreqChanged.setObjects(*((_H,_J),(_H,_K),(_B,_U),(_B,_I)))
if mibBuilder.loadTexts:radioFreqChanged.setStatus(_A)
radioBandChanged=NotificationType((1,3,6,1,4,1,3942,1,1,2,17,0,2))
radioBandChanged.setObjects(*((_H,_J),(_H,_K),(_B,_V),(_B,_I)))
if mibBuilder.loadTexts:radioBandChanged.setStatus(_A)
aquaradioNotifications=NotificationGroup((1,3,6,1,4,1,3942,1,1,2,18,3))
aquaradioNotifications.setObjects(*((_B,_A1),(_B,_A2)))
if mibBuilder.loadTexts:aquaradioNotifications.setStatus(_A)
aquaradioMIBCompliance=ModuleCompliance((1,3,6,1,4,1,3942,1,1,2,18,1,1))
aquaradioMIBCompliance.setObjects((_B,_A3))
if mibBuilder.loadTexts:aquaradioMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'RadioSID':RadioSID,'aquaradioMIB':aquaradioMIB,'rmPropertiesTable':rmPropertiesTable,'rmPropertiesEntry':rmPropertiesEntry,_I:rmPropertiesIfIndex,_Y:rmType,_U:rmFrequency,_Z:rmBitRate,'rmSid':rmSid,_a:rmCurPowerLevel,_b:rmModulation,_c:rmAntenna,_d:rmDistance,_e:rmBurst,_f:rmLongRange,_g:rmPowerCtl,_h:rmTXRT,_i:rmTXVRT,'rmPTP':rmPTP,_j:rmWOCD,_k:rmBCsid,_w:rmDistanceAuto,_x:rmNoiseFloor,_V:rmBandwidth,_y:rmChainMode,_A0:rmSelectChannel,'rmPowerLevelsTable':rmPowerLevelsTable,'rmPowerLevelsEntry':rmPowerLevelsEntry,_L:rmPowerLevelsIfIndex,_M:rmPowerLevelsValIndex,_l:rmPowerLevelsPower,'rmFrequenciesTable':rmFrequenciesTable,'rmFrequenciesEntry':rmFrequenciesEntry,_N:rmFrequenciesIfIndex,_O:rmFrequenciesValIndex,_m:rmFrequenciesFreq,'rmBitratesTable':rmBitratesTable,'rmBitratesEntry':rmBitratesEntry,_P:rmBitratesIfIndex,_Q:rmBitratesValIndex,_n:rmBitratesBitrate,'radioStatTable':radioStatTable,'radioStatEntry':radioStatEntry,_R:radioStatMacAddress,_o:radioStatPackets,_p:radioStatRepeats,_q:radioStatRepeatPackets,_r:radioStatBytes,_s:radioStatRepeatBytes,_t:radioStatErrors,_u:radioStatRecvPackets,_v:radioStatRecvBytes,'rmBandsTable':rmBandsTable,'rmBandsEntry':rmBandsEntry,_S:rmBandsIfIndex,_T:rmBandsValIndex,_z:rmBandsBand,'aquaradioMIBNotificationsPrefix':aquaradioMIBNotificationsPrefix,'aquaradioMIBnotifications':aquaradioMIBnotifications,_A1:radioFreqChanged,_A2:radioBandChanged,'aquaradioMIBConformance':aquaradioMIBConformance,'aquaradioMIBCompliances':aquaradioMIBCompliances,'aquaradioMIBCompliance':aquaradioMIBCompliance,'aquaradioMIBGroups':aquaradioMIBGroups,_A3:radioGroup,'aquaradioNotifications':aquaradioNotifications})