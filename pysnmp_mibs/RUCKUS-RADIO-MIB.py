_H='ruckusRadioStatsIndex'
_G='ruckusRadioIndex'
_F='OctetString'
_E='RUCKUS-RADIO-MIB'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,ifIndex=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','ifIndex')
ruckusCommonRadioModule,=mibBuilder.importSymbols('RUCKUS-ROOT-MIB','ruckusCommonRadioModule')
RuckusCountryCode,RuckusRadioMode,RuckusRate=mibBuilder.importSymbols('RUCKUS-TC-MIB','RuckusCountryCode','RuckusRadioMode','RuckusRate')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ruckusRadioMIB=ModuleIdentity((1,3,6,1,4,1,25053,1,1,12,1))
_RuckusRadioObjects_ObjectIdentity=ObjectIdentity
ruckusRadioObjects=_RuckusRadioObjects_ObjectIdentity((1,3,6,1,4,1,25053,1,1,12,1,1))
_RuckusRadioInfo_ObjectIdentity=ObjectIdentity
ruckusRadioInfo=_RuckusRadioInfo_ObjectIdentity((1,3,6,1,4,1,25053,1,1,12,1,1,1))
_RuckusRadioNumber_Type=Integer32
_RuckusRadioNumber_Object=MibScalar
ruckusRadioNumber=_RuckusRadioNumber_Object((1,3,6,1,4,1,25053,1,1,12,1,1,1,1),_RuckusRadioNumber_Type())
ruckusRadioNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusRadioNumber.setStatus(_A)
_RuckusRadioTable_Object=MibTable
ruckusRadioTable=_RuckusRadioTable_Object((1,3,6,1,4,1,25053,1,1,12,1,1,1,2))
if mibBuilder.loadTexts:ruckusRadioTable.setStatus(_A)
_RuckusRadioEntry_Object=MibTableRow
ruckusRadioEntry=_RuckusRadioEntry_Object((1,3,6,1,4,1,25053,1,1,12,1,1,1,2,1))
ruckusRadioEntry.setIndexNames((0,_E,_G))
if mibBuilder.loadTexts:ruckusRadioEntry.setStatus(_A)
class _RuckusRadioMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,8)));namedValues=NamedValues(*(('auto',0),('ieee802dot11g-only',1),('ieee802dot11b-only',2),('ieee802dot11ng',3),('ieee802dot11na',4),('ieee802dot11a-only',5),('ieee802dot11ac',6),('ieee802dot11ax',8)))
_RuckusRadioMode_Type.__name__=_C
_RuckusRadioMode_Object=MibTableColumn
ruckusRadioMode=_RuckusRadioMode_Object((1,3,6,1,4,1,25053,1,1,12,1,1,1,2,1,1),_RuckusRadioMode_Type())
ruckusRadioMode.setMaxAccess(_D)
if mibBuilder.loadTexts:ruckusRadioMode.setStatus(_A)
_RuckusRadioCountry_Type=RuckusCountryCode
_RuckusRadioCountry_Object=MibTableColumn
ruckusRadioCountry=_RuckusRadioCountry_Object((1,3,6,1,4,1,25053,1,1,12,1,1,1,2,1,2),_RuckusRadioCountry_Type())
ruckusRadioCountry.setMaxAccess(_D)
if mibBuilder.loadTexts:ruckusRadioCountry.setStatus(_A)
class _RuckusRadioBSSType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('station',1),('master',2),('independent',3)))
_RuckusRadioBSSType_Type.__name__=_C
_RuckusRadioBSSType_Object=MibTableColumn
ruckusRadioBSSType=_RuckusRadioBSSType_Object((1,3,6,1,4,1,25053,1,1,12,1,1,1,2,1,3),_RuckusRadioBSSType_Type())
ruckusRadioBSSType.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusRadioBSSType.setStatus(_A)
class _RuckusRadioChannel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,14))
_RuckusRadioChannel_Type.__name__=_C
_RuckusRadioChannel_Object=MibTableColumn
ruckusRadioChannel=_RuckusRadioChannel_Object((1,3,6,1,4,1,25053,1,1,12,1,1,1,2,1,4),_RuckusRadioChannel_Type())
ruckusRadioChannel.setMaxAccess(_D)
if mibBuilder.loadTexts:ruckusRadioChannel.setStatus(_A)
class _RuckusRadioDataRate_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_RuckusRadioDataRate_Type.__name__=_F
_RuckusRadioDataRate_Object=MibTableColumn
ruckusRadioDataRate=_RuckusRadioDataRate_Object((1,3,6,1,4,1,25053,1,1,12,1,1,1,2,1,5),_RuckusRadioDataRate_Type())
ruckusRadioDataRate.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusRadioDataRate.setStatus(_A)
class _RuckusRadioTxPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,24)));namedValues=NamedValues(*(('full',0),('minus1',1),('minus2',2),('half',3),('minus4',4),('minus5',5),('quarter',6),('minus7',7),('minus8',8),('eighth',9),('minus10',10),('minus24',24)))
_RuckusRadioTxPower_Type.__name__=_C
_RuckusRadioTxPower_Object=MibTableColumn
ruckusRadioTxPower=_RuckusRadioTxPower_Object((1,3,6,1,4,1,25053,1,1,12,1,1,1,2,1,6),_RuckusRadioTxPower_Type())
ruckusRadioTxPower.setMaxAccess(_D)
if mibBuilder.loadTexts:ruckusRadioTxPower.setStatus(_A)
class _RuckusRadioProtectionMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('none',0),('ctsOnly',1),('ctsRts',2)))
_RuckusRadioProtectionMode_Type.__name__=_C
_RuckusRadioProtectionMode_Object=MibTableColumn
ruckusRadioProtectionMode=_RuckusRadioProtectionMode_Object((1,3,6,1,4,1,25053,1,1,12,1,1,1,2,1,7),_RuckusRadioProtectionMode_Type())
ruckusRadioProtectionMode.setMaxAccess(_D)
if mibBuilder.loadTexts:ruckusRadioProtectionMode.setStatus(_A)
_RuckusRadioNoiseFloor_Type=Integer32
_RuckusRadioNoiseFloor_Object=MibTableColumn
ruckusRadioNoiseFloor=_RuckusRadioNoiseFloor_Object((1,3,6,1,4,1,25053,1,1,12,1,1,1,2,1,8),_RuckusRadioNoiseFloor_Type())
ruckusRadioNoiseFloor.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusRadioNoiseFloor.setStatus(_A)
_RuckusRadioIndex_Type=InterfaceIndex
_RuckusRadioIndex_Object=MibTableColumn
ruckusRadioIndex=_RuckusRadioIndex_Object((1,3,6,1,4,1,25053,1,1,12,1,1,1,2,1,200),_RuckusRadioIndex_Type())
ruckusRadioIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusRadioIndex.setStatus(_A)
_RuckusRadioStatsTable_Object=MibTable
ruckusRadioStatsTable=_RuckusRadioStatsTable_Object((1,3,6,1,4,1,25053,1,1,12,1,1,1,3))
if mibBuilder.loadTexts:ruckusRadioStatsTable.setStatus(_A)
_RuckusRadioStatsEntry_Object=MibTableRow
ruckusRadioStatsEntry=_RuckusRadioStatsEntry_Object((1,3,6,1,4,1,25053,1,1,12,1,1,1,3,1))
ruckusRadioStatsEntry.setIndexNames((0,_E,_H))
if mibBuilder.loadTexts:ruckusRadioStatsEntry.setStatus(_A)
_RuckusRadioStatsMaxSta_Type=Counter32
_RuckusRadioStatsMaxSta_Object=MibTableColumn
ruckusRadioStatsMaxSta=_RuckusRadioStatsMaxSta_Object((1,3,6,1,4,1,25053,1,1,12,1,1,1,3,1,1),_RuckusRadioStatsMaxSta_Type())
ruckusRadioStatsMaxSta.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusRadioStatsMaxSta.setStatus(_A)
_RuckusRadioStatsNumSta_Type=Counter32
_RuckusRadioStatsNumSta_Object=MibTableColumn
ruckusRadioStatsNumSta=_RuckusRadioStatsNumSta_Object((1,3,6,1,4,1,25053,1,1,12,1,1,1,3,1,2),_RuckusRadioStatsNumSta_Type())
ruckusRadioStatsNumSta.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusRadioStatsNumSta.setStatus(_A)
_RuckusRadioStatsNumAuthSta_Type=Counter32
_RuckusRadioStatsNumAuthSta_Object=MibTableColumn
ruckusRadioStatsNumAuthSta=_RuckusRadioStatsNumAuthSta_Object((1,3,6,1,4,1,25053,1,1,12,1,1,1,3,1,3),_RuckusRadioStatsNumAuthSta_Type())
ruckusRadioStatsNumAuthSta.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusRadioStatsNumAuthSta.setStatus(_A)
_RuckusRadioStatsNumAuthReq_Type=Counter32
_RuckusRadioStatsNumAuthReq_Object=MibTableColumn
ruckusRadioStatsNumAuthReq=_RuckusRadioStatsNumAuthReq_Object((1,3,6,1,4,1,25053,1,1,12,1,1,1,3,1,4),_RuckusRadioStatsNumAuthReq_Type())
ruckusRadioStatsNumAuthReq.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusRadioStatsNumAuthReq.setStatus(_A)
_RuckusRadioStatsNumAuthResp_Type=Counter32
_RuckusRadioStatsNumAuthResp_Object=MibTableColumn
ruckusRadioStatsNumAuthResp=_RuckusRadioStatsNumAuthResp_Object((1,3,6,1,4,1,25053,1,1,12,1,1,1,3,1,5),_RuckusRadioStatsNumAuthResp_Type())
ruckusRadioStatsNumAuthResp.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusRadioStatsNumAuthResp.setStatus(_A)
_RuckusRadioStatsNumAuthSuccess_Type=Counter32
_RuckusRadioStatsNumAuthSuccess_Object=MibTableColumn
ruckusRadioStatsNumAuthSuccess=_RuckusRadioStatsNumAuthSuccess_Object((1,3,6,1,4,1,25053,1,1,12,1,1,1,3,1,6),_RuckusRadioStatsNumAuthSuccess_Type())
ruckusRadioStatsNumAuthSuccess.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusRadioStatsNumAuthSuccess.setStatus(_A)
_RuckusRadioStatsNumAuthFail_Type=Counter32
_RuckusRadioStatsNumAuthFail_Object=MibTableColumn
ruckusRadioStatsNumAuthFail=_RuckusRadioStatsNumAuthFail_Object((1,3,6,1,4,1,25053,1,1,12,1,1,1,3,1,7),_RuckusRadioStatsNumAuthFail_Type())
ruckusRadioStatsNumAuthFail.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusRadioStatsNumAuthFail.setStatus(_A)
_RuckusRadioStatsNumAssocReq_Type=Counter32
_RuckusRadioStatsNumAssocReq_Object=MibTableColumn
ruckusRadioStatsNumAssocReq=_RuckusRadioStatsNumAssocReq_Object((1,3,6,1,4,1,25053,1,1,12,1,1,1,3,1,8),_RuckusRadioStatsNumAssocReq_Type())
ruckusRadioStatsNumAssocReq.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusRadioStatsNumAssocReq.setStatus(_A)
_RuckusRadioStatsNumAssocResp_Type=Counter32
_RuckusRadioStatsNumAssocResp_Object=MibTableColumn
ruckusRadioStatsNumAssocResp=_RuckusRadioStatsNumAssocResp_Object((1,3,6,1,4,1,25053,1,1,12,1,1,1,3,1,9),_RuckusRadioStatsNumAssocResp_Type())
ruckusRadioStatsNumAssocResp.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusRadioStatsNumAssocResp.setStatus(_A)
_RuckusRadioStatsNumAssocSuccess_Type=Counter32
_RuckusRadioStatsNumAssocSuccess_Object=MibTableColumn
ruckusRadioStatsNumAssocSuccess=_RuckusRadioStatsNumAssocSuccess_Object((1,3,6,1,4,1,25053,1,1,12,1,1,1,3,1,10),_RuckusRadioStatsNumAssocSuccess_Type())
ruckusRadioStatsNumAssocSuccess.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusRadioStatsNumAssocSuccess.setStatus(_A)
_RuckusRadioStatsNumAssocFail_Type=Counter32
_RuckusRadioStatsNumAssocFail_Object=MibTableColumn
ruckusRadioStatsNumAssocFail=_RuckusRadioStatsNumAssocFail_Object((1,3,6,1,4,1,25053,1,1,12,1,1,1,3,1,11),_RuckusRadioStatsNumAssocFail_Type())
ruckusRadioStatsNumAssocFail.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusRadioStatsNumAssocFail.setStatus(_A)
_RuckusRadioStatsAssocFailRate_Type=Unsigned32
_RuckusRadioStatsAssocFailRate_Object=MibTableColumn
ruckusRadioStatsAssocFailRate=_RuckusRadioStatsAssocFailRate_Object((1,3,6,1,4,1,25053,1,1,12,1,1,1,3,1,12),_RuckusRadioStatsAssocFailRate_Type())
ruckusRadioStatsAssocFailRate.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusRadioStatsAssocFailRate.setStatus(_A)
_RuckusRadioStatsAuthFailRate_Type=Unsigned32
_RuckusRadioStatsAuthFailRate_Object=MibTableColumn
ruckusRadioStatsAuthFailRate=_RuckusRadioStatsAuthFailRate_Object((1,3,6,1,4,1,25053,1,1,12,1,1,1,3,1,13),_RuckusRadioStatsAuthFailRate_Type())
ruckusRadioStatsAuthFailRate.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusRadioStatsAuthFailRate.setStatus(_A)
_RuckusRadioStatsAssocSuccessRate_Type=Unsigned32
_RuckusRadioStatsAssocSuccessRate_Object=MibTableColumn
ruckusRadioStatsAssocSuccessRate=_RuckusRadioStatsAssocSuccessRate_Object((1,3,6,1,4,1,25053,1,1,12,1,1,1,3,1,14),_RuckusRadioStatsAssocSuccessRate_Type())
ruckusRadioStatsAssocSuccessRate.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusRadioStatsAssocSuccessRate.setStatus(_A)
_RuckusRadioStatsResourceUtil_Type=Unsigned32
_RuckusRadioStatsResourceUtil_Object=MibTableColumn
ruckusRadioStatsResourceUtil=_RuckusRadioStatsResourceUtil_Object((1,3,6,1,4,1,25053,1,1,12,1,1,1,3,1,15),_RuckusRadioStatsResourceUtil_Type())
ruckusRadioStatsResourceUtil.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusRadioStatsResourceUtil.setStatus(_A)
_RuckusRadioStatsRxBytes_Type=Counter32
_RuckusRadioStatsRxBytes_Object=MibTableColumn
ruckusRadioStatsRxBytes=_RuckusRadioStatsRxBytes_Object((1,3,6,1,4,1,25053,1,1,12,1,1,1,3,1,16),_RuckusRadioStatsRxBytes_Type())
ruckusRadioStatsRxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusRadioStatsRxBytes.setStatus(_A)
_RuckusRadioStatsRxFrames_Type=Counter32
_RuckusRadioStatsRxFrames_Object=MibTableColumn
ruckusRadioStatsRxFrames=_RuckusRadioStatsRxFrames_Object((1,3,6,1,4,1,25053,1,1,12,1,1,1,3,1,17),_RuckusRadioStatsRxFrames_Type())
ruckusRadioStatsRxFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusRadioStatsRxFrames.setStatus(_A)
_RuckusRadioStatsRxWEPFail_Type=Counter32
_RuckusRadioStatsRxWEPFail_Object=MibTableColumn
ruckusRadioStatsRxWEPFail=_RuckusRadioStatsRxWEPFail_Object((1,3,6,1,4,1,25053,1,1,12,1,1,1,3,1,18),_RuckusRadioStatsRxWEPFail_Type())
ruckusRadioStatsRxWEPFail.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusRadioStatsRxWEPFail.setStatus(_A)
_RuckusRadioStatsRxDecryptCRCError_Type=Counter32
_RuckusRadioStatsRxDecryptCRCError_Object=MibTableColumn
ruckusRadioStatsRxDecryptCRCError=_RuckusRadioStatsRxDecryptCRCError_Object((1,3,6,1,4,1,25053,1,1,12,1,1,1,3,1,19),_RuckusRadioStatsRxDecryptCRCError_Type())
ruckusRadioStatsRxDecryptCRCError.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusRadioStatsRxDecryptCRCError.setStatus(_A)
_RuckusRadioStatsRxMICError_Type=Counter32
_RuckusRadioStatsRxMICError_Object=MibTableColumn
ruckusRadioStatsRxMICError=_RuckusRadioStatsRxMICError_Object((1,3,6,1,4,1,25053,1,1,12,1,1,1,3,1,20),_RuckusRadioStatsRxMICError_Type())
ruckusRadioStatsRxMICError.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusRadioStatsRxMICError.setStatus(_A)
_RuckusRadioStatsRxErrors_Type=Counter32
_RuckusRadioStatsRxErrors_Object=MibTableColumn
ruckusRadioStatsRxErrors=_RuckusRadioStatsRxErrors_Object((1,3,6,1,4,1,25053,1,1,12,1,1,1,3,1,21),_RuckusRadioStatsRxErrors_Type())
ruckusRadioStatsRxErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusRadioStatsRxErrors.setStatus(_A)
_RuckusRadioStatsTxBytes_Type=Counter32
_RuckusRadioStatsTxBytes_Object=MibTableColumn
ruckusRadioStatsTxBytes=_RuckusRadioStatsTxBytes_Object((1,3,6,1,4,1,25053,1,1,12,1,1,1,3,1,22),_RuckusRadioStatsTxBytes_Type())
ruckusRadioStatsTxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusRadioStatsTxBytes.setStatus(_A)
_RuckusRadioStatsTxFrames_Type=Counter32
_RuckusRadioStatsTxFrames_Object=MibTableColumn
ruckusRadioStatsTxFrames=_RuckusRadioStatsTxFrames_Object((1,3,6,1,4,1,25053,1,1,12,1,1,1,3,1,23),_RuckusRadioStatsTxFrames_Type())
ruckusRadioStatsTxFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusRadioStatsTxFrames.setStatus(_A)
_RuckusRadioStatsTotalAssocTime_Type=TimeTicks
_RuckusRadioStatsTotalAssocTime_Object=MibTableColumn
ruckusRadioStatsTotalAssocTime=_RuckusRadioStatsTotalAssocTime_Object((1,3,6,1,4,1,25053,1,1,12,1,1,1,3,1,42),_RuckusRadioStatsTotalAssocTime_Type())
ruckusRadioStatsTotalAssocTime.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusRadioStatsTotalAssocTime.setStatus(_A)
_RuckusRadioStatsTotalAirtime_Type=Counter32
_RuckusRadioStatsTotalAirtime_Object=MibTableColumn
ruckusRadioStatsTotalAirtime=_RuckusRadioStatsTotalAirtime_Object((1,3,6,1,4,1,25053,1,1,12,1,1,1,3,1,50),_RuckusRadioStatsTotalAirtime_Type())
ruckusRadioStatsTotalAirtime.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusRadioStatsTotalAirtime.setStatus(_A)
_RuckusRadioStatsBusyAirtime_Type=Counter32
_RuckusRadioStatsBusyAirtime_Object=MibTableColumn
ruckusRadioStatsBusyAirtime=_RuckusRadioStatsBusyAirtime_Object((1,3,6,1,4,1,25053,1,1,12,1,1,1,3,1,51),_RuckusRadioStatsBusyAirtime_Type())
ruckusRadioStatsBusyAirtime.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusRadioStatsBusyAirtime.setStatus(_A)
_RuckusRadioStatsTxAirtime_Type=Counter32
_RuckusRadioStatsTxAirtime_Object=MibTableColumn
ruckusRadioStatsTxAirtime=_RuckusRadioStatsTxAirtime_Object((1,3,6,1,4,1,25053,1,1,12,1,1,1,3,1,52),_RuckusRadioStatsTxAirtime_Type())
ruckusRadioStatsTxAirtime.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusRadioStatsTxAirtime.setStatus(_A)
_RuckusRadioStatsRxAirtime_Type=Counter32
_RuckusRadioStatsRxAirtime_Object=MibTableColumn
ruckusRadioStatsRxAirtime=_RuckusRadioStatsRxAirtime_Object((1,3,6,1,4,1,25053,1,1,12,1,1,1,3,1,53),_RuckusRadioStatsRxAirtime_Type())
ruckusRadioStatsRxAirtime.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusRadioStatsRxAirtime.setStatus(_A)
_RuckusRadioStatsIndex_Type=InterfaceIndex
_RuckusRadioStatsIndex_Object=MibTableColumn
ruckusRadioStatsIndex=_RuckusRadioStatsIndex_Object((1,3,6,1,4,1,25053,1,1,12,1,1,1,3,1,200),_RuckusRadioStatsIndex_Type())
ruckusRadioStatsIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusRadioStatsIndex.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'ruckusRadioMIB':ruckusRadioMIB,'ruckusRadioObjects':ruckusRadioObjects,'ruckusRadioInfo':ruckusRadioInfo,'ruckusRadioNumber':ruckusRadioNumber,'ruckusRadioTable':ruckusRadioTable,'ruckusRadioEntry':ruckusRadioEntry,'ruckusRadioMode':ruckusRadioMode,'ruckusRadioCountry':ruckusRadioCountry,'ruckusRadioBSSType':ruckusRadioBSSType,'ruckusRadioChannel':ruckusRadioChannel,'ruckusRadioDataRate':ruckusRadioDataRate,'ruckusRadioTxPower':ruckusRadioTxPower,'ruckusRadioProtectionMode':ruckusRadioProtectionMode,'ruckusRadioNoiseFloor':ruckusRadioNoiseFloor,_G:ruckusRadioIndex,'ruckusRadioStatsTable':ruckusRadioStatsTable,'ruckusRadioStatsEntry':ruckusRadioStatsEntry,'ruckusRadioStatsMaxSta':ruckusRadioStatsMaxSta,'ruckusRadioStatsNumSta':ruckusRadioStatsNumSta,'ruckusRadioStatsNumAuthSta':ruckusRadioStatsNumAuthSta,'ruckusRadioStatsNumAuthReq':ruckusRadioStatsNumAuthReq,'ruckusRadioStatsNumAuthResp':ruckusRadioStatsNumAuthResp,'ruckusRadioStatsNumAuthSuccess':ruckusRadioStatsNumAuthSuccess,'ruckusRadioStatsNumAuthFail':ruckusRadioStatsNumAuthFail,'ruckusRadioStatsNumAssocReq':ruckusRadioStatsNumAssocReq,'ruckusRadioStatsNumAssocResp':ruckusRadioStatsNumAssocResp,'ruckusRadioStatsNumAssocSuccess':ruckusRadioStatsNumAssocSuccess,'ruckusRadioStatsNumAssocFail':ruckusRadioStatsNumAssocFail,'ruckusRadioStatsAssocFailRate':ruckusRadioStatsAssocFailRate,'ruckusRadioStatsAuthFailRate':ruckusRadioStatsAuthFailRate,'ruckusRadioStatsAssocSuccessRate':ruckusRadioStatsAssocSuccessRate,'ruckusRadioStatsResourceUtil':ruckusRadioStatsResourceUtil,'ruckusRadioStatsRxBytes':ruckusRadioStatsRxBytes,'ruckusRadioStatsRxFrames':ruckusRadioStatsRxFrames,'ruckusRadioStatsRxWEPFail':ruckusRadioStatsRxWEPFail,'ruckusRadioStatsRxDecryptCRCError':ruckusRadioStatsRxDecryptCRCError,'ruckusRadioStatsRxMICError':ruckusRadioStatsRxMICError,'ruckusRadioStatsRxErrors':ruckusRadioStatsRxErrors,'ruckusRadioStatsTxBytes':ruckusRadioStatsTxBytes,'ruckusRadioStatsTxFrames':ruckusRadioStatsTxFrames,'ruckusRadioStatsTotalAssocTime':ruckusRadioStatsTotalAssocTime,'ruckusRadioStatsTotalAirtime':ruckusRadioStatsTotalAirtime,'ruckusRadioStatsBusyAirtime':ruckusRadioStatsBusyAirtime,'ruckusRadioStatsTxAirtime':ruckusRadioStatsTxAirtime,'ruckusRadioStatsRxAirtime':ruckusRadioStatsRxAirtime,_H:ruckusRadioStatsIndex})