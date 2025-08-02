_q='hpnicfDot11UserName'
_p='hpnicfDot11StaDisconnectReason'
_o='hpnicfDot11StationACIPv6Add'
_n='hpnicfDot11StationACIPAddress'
_m='hpnicfDot11StationRoamingTime'
_l='hpnicfDot11StationSessionStartTime'
_k='hpnicfDot11StationAssocFailCause'
_j='hpnicfDot11StationAuthMode'
_i='hpnicfDot11StationAuthorFailCause'
_h='hpnicfDot11StationAKMMode'
_g='hpnicfDot11StationAuthenMode'
_f='hpnicfDot11StationRfPingIndex'
_e='wlanex'
_d='sharedkey'
_c='opensystem'
_b='byte/s'
_a='powersave'
_Z='active'
_Y='not-accessible'
_X='HpnicfDot11SSIDEncryptModeType'
_W='hpnicfDot11StationSessionDuration'
_V='hpnicfDot11StationTrapAPMacAddress'
_U='hpnicfDot11StationFailCauseDesc'
_T='hpnicfDot11StationTrapBSSID'
_S='none'
_R='second'
_Q='OctetString'
_P='bytes'
_O='hpnicfDot11StationAPName'
_N='hpnicfDot11StationVlanId'
_M='hpnicfDot11StationBSSID'
_L='hpnicfDot11StationUserName'
_K='Mbps'
_J='hpnicfDot11StationMAC'
_I='hpnicfDot11StationSSIDName'
_H='hpnicfDot11CurrRadioID'
_G='hpnicfDot11CurrAPID'
_F='hpnicfDot11StationTrapStaMAC'
_E='Integer32'
_D='accessible-for-notify'
_C='read-only'
_B='HPN-ICF-DOT11-STATION-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_Q,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
HpnicfDot11AKMType,HpnicfDot11AssocFailType,HpnicfDot11AuthenType,HpnicfDot11AuthorFailType,HpnicfDot11ChannelScopeType,HpnicfDot11CipherType,HpnicfDot11ObjectIDType,HpnicfDot11RadioScopeType,HpnicfDot11RadioType,HpnicfDot11RadioType2,HpnicfDot11SSIDEncryptModeType,HpnicfDot11SSIDStringType,HpnicfDot11SecIEStatusType,hpnicfDot11=mibBuilder.importSymbols('HPN-ICF-DOT11-REF-MIB','HpnicfDot11AKMType','HpnicfDot11AssocFailType','HpnicfDot11AuthenType','HpnicfDot11AuthorFailType','HpnicfDot11ChannelScopeType','HpnicfDot11CipherType','HpnicfDot11ObjectIDType','HpnicfDot11RadioScopeType','HpnicfDot11RadioType','HpnicfDot11RadioType2',_X,'HpnicfDot11SSIDStringType','HpnicfDot11SecIEStatusType','hpnicfDot11')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','TextualConvention','TruthValue')
hpnicfDot11STATION=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,75,3))
if mibBuilder.loadTexts:hpnicfDot11STATION.setRevisions(('2010-09-02 18:00','2010-02-23 18:00','2009-12-01 18:00','2009-08-07 18:00','2009-07-29 18:00','2009-05-07 20:00','2008-11-07 17:30','2008-02-25 18:00','2007-12-21 18:00','2007-06-21 20:00','2007-04-27 20:00','2006-05-10 16:00'))
_HpnicfDot11StationMtGroup_ObjectIdentity=ObjectIdentity
hpnicfDot11StationMtGroup=_HpnicfDot11StationMtGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,75,3,1))
_HpnicfDot11StationAssociateTable_Object=MibTable
hpnicfDot11StationAssociateTable=_HpnicfDot11StationAssociateTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,3,1,1))
if mibBuilder.loadTexts:hpnicfDot11StationAssociateTable.setStatus(_A)
_HpnicfDot11StationAssociateEntry_Object=MibTableRow
hpnicfDot11StationAssociateEntry=_HpnicfDot11StationAssociateEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,3,1,1,1))
hpnicfDot11StationAssociateEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:hpnicfDot11StationAssociateEntry.setStatus(_A)
_HpnicfDot11StationMAC_Type=MacAddress
_HpnicfDot11StationMAC_Object=MibTableColumn
hpnicfDot11StationMAC=_HpnicfDot11StationMAC_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,3,1,1,1,1),_HpnicfDot11StationMAC_Type())
hpnicfDot11StationMAC.setMaxAccess(_Y)
if mibBuilder.loadTexts:hpnicfDot11StationMAC.setStatus(_A)
_HpnicfDot11StationIPAddress_Type=IpAddress
_HpnicfDot11StationIPAddress_Object=MibTableColumn
hpnicfDot11StationIPAddress=_HpnicfDot11StationIPAddress_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,3,1,1,1,2),_HpnicfDot11StationIPAddress_Type())
hpnicfDot11StationIPAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11StationIPAddress.setStatus(_A)
_HpnicfDot11StationUserName_Type=OctetString
_HpnicfDot11StationUserName_Object=MibTableColumn
hpnicfDot11StationUserName=_HpnicfDot11StationUserName_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,3,1,1,1,3),_HpnicfDot11StationUserName_Type())
hpnicfDot11StationUserName.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11StationUserName.setStatus(_A)
_HpnicfDot11StationTxRateSet_Type=OctetString
_HpnicfDot11StationTxRateSet_Object=MibTableColumn
hpnicfDot11StationTxRateSet=_HpnicfDot11StationTxRateSet_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,3,1,1,1,4),_HpnicfDot11StationTxRateSet_Type())
hpnicfDot11StationTxRateSet.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11StationTxRateSet.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11StationTxRateSet.setUnits(_K)
_HpnicfDot11StationUpTime_Type=Unsigned32
_HpnicfDot11StationUpTime_Object=MibTableColumn
hpnicfDot11StationUpTime=_HpnicfDot11StationUpTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,3,1,1,1,5),_HpnicfDot11StationUpTime_Type())
hpnicfDot11StationUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11StationUpTime.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11StationUpTime.setUnits(_R)
_HpnicfDot11StationSignalStrength_Type=Integer32
_HpnicfDot11StationSignalStrength_Object=MibTableColumn
hpnicfDot11StationSignalStrength=_HpnicfDot11StationSignalStrength_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,3,1,1,1,6),_HpnicfDot11StationSignalStrength_Type())
hpnicfDot11StationSignalStrength.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11StationSignalStrength.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11StationSignalStrength.setUnits('dBm')
_HpnicfDot11StationRSSI_Type=Integer32
_HpnicfDot11StationRSSI_Object=MibTableColumn
hpnicfDot11StationRSSI=_HpnicfDot11StationRSSI_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,3,1,1,1,7),_HpnicfDot11StationRSSI_Type())
hpnicfDot11StationRSSI.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11StationRSSI.setStatus(_A)
_HpnicfDot11StationChannel_Type=HpnicfDot11ChannelScopeType
_HpnicfDot11StationChannel_Object=MibTableColumn
hpnicfDot11StationChannel=_HpnicfDot11StationChannel_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,3,1,1,1,8),_HpnicfDot11StationChannel_Type())
hpnicfDot11StationChannel.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11StationChannel.setStatus(_A)
class _HpnicfDot11StationPowerSaveMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Z,1),(_a,2)))
_HpnicfDot11StationPowerSaveMode_Type.__name__=_E
_HpnicfDot11StationPowerSaveMode_Object=MibTableColumn
hpnicfDot11StationPowerSaveMode=_HpnicfDot11StationPowerSaveMode_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,3,1,1,1,9),_HpnicfDot11StationPowerSaveMode_Type())
hpnicfDot11StationPowerSaveMode.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11StationPowerSaveMode.setStatus(_A)
_HpnicfDot11StationAid_Type=Integer32
_HpnicfDot11StationAid_Object=MibTableColumn
hpnicfDot11StationAid=_HpnicfDot11StationAid_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,3,1,1,1,10),_HpnicfDot11StationAid_Type())
hpnicfDot11StationAid.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11StationAid.setStatus(_A)
_HpnicfDot11StationVlanId_Type=Integer32
_HpnicfDot11StationVlanId_Object=MibTableColumn
hpnicfDot11StationVlanId=_HpnicfDot11StationVlanId_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,3,1,1,1,11),_HpnicfDot11StationVlanId_Type())
hpnicfDot11StationVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11StationVlanId.setStatus(_A)
_HpnicfDot11StationSSIDName_Type=HpnicfDot11SSIDStringType
_HpnicfDot11StationSSIDName_Object=MibTableColumn
hpnicfDot11StationSSIDName=_HpnicfDot11StationSSIDName_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,3,1,1,1,12),_HpnicfDot11StationSSIDName_Type())
hpnicfDot11StationSSIDName.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11StationSSIDName.setStatus(_A)
_HpnicfDot11StationAuthenMode_Type=HpnicfDot11AuthenType
_HpnicfDot11StationAuthenMode_Object=MibTableColumn
hpnicfDot11StationAuthenMode=_HpnicfDot11StationAuthenMode_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,3,1,1,1,13),_HpnicfDot11StationAuthenMode_Type())
hpnicfDot11StationAuthenMode.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11StationAuthenMode.setStatus(_A)
_HpnicfDot11StationAKMMode_Type=HpnicfDot11AKMType
_HpnicfDot11StationAKMMode_Object=MibTableColumn
hpnicfDot11StationAKMMode=_HpnicfDot11StationAKMMode_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,3,1,1,1,14),_HpnicfDot11StationAKMMode_Type())
hpnicfDot11StationAKMMode.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11StationAKMMode.setStatus(_A)
_HpnicfDot11StationSecurityCiphers_Type=HpnicfDot11CipherType
_HpnicfDot11StationSecurityCiphers_Object=MibTableColumn
hpnicfDot11StationSecurityCiphers=_HpnicfDot11StationSecurityCiphers_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,3,1,1,1,15),_HpnicfDot11StationSecurityCiphers_Type())
hpnicfDot11StationSecurityCiphers.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11StationSecurityCiphers.setStatus(_A)
class _HpnicfDot11StationSSIDEncryptMode_Type(HpnicfDot11SSIDEncryptModeType):defaultValue=2
_HpnicfDot11StationSSIDEncryptMode_Type.__name__=_X
_HpnicfDot11StationSSIDEncryptMode_Object=MibTableColumn
hpnicfDot11StationSSIDEncryptMode=_HpnicfDot11StationSSIDEncryptMode_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,3,1,1,1,16),_HpnicfDot11StationSSIDEncryptMode_Type())
hpnicfDot11StationSSIDEncryptMode.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11StationSSIDEncryptMode.setStatus(_A)
_HpnicfDot11StationRxSNR_Type=Integer32
_HpnicfDot11StationRxSNR_Object=MibTableColumn
hpnicfDot11StationRxSNR=_HpnicfDot11StationRxSNR_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,3,1,1,1,17),_HpnicfDot11StationRxSNR_Type())
hpnicfDot11StationRxSNR.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11StationRxSNR.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11StationRxSNR.setUnits('One Percent')
_HpnicfDot11StationTxRate_Type=Integer32
_HpnicfDot11StationTxRate_Object=MibTableColumn
hpnicfDot11StationTxRate=_HpnicfDot11StationTxRate_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,3,1,1,1,18),_HpnicfDot11StationTxRate_Type())
hpnicfDot11StationTxRate.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11StationTxRate.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11StationTxRate.setUnits(_K)
_HpnicfDot11StationRxRate_Type=Integer32
_HpnicfDot11StationRxRate_Object=MibTableColumn
hpnicfDot11StationRxRate=_HpnicfDot11StationRxRate_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,3,1,1,1,19),_HpnicfDot11StationRxRate_Type())
hpnicfDot11StationRxRate.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11StationRxRate.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11StationRxRate.setUnits(_K)
class _HpnicfDot11StationVendorName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_HpnicfDot11StationVendorName_Type.__name__=_Q
_HpnicfDot11StationVendorName_Object=MibTableColumn
hpnicfDot11StationVendorName=_HpnicfDot11StationVendorName_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,3,1,1,1,20),_HpnicfDot11StationVendorName_Type())
hpnicfDot11StationVendorName.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11StationVendorName.setStatus(_A)
_HpnicfDot11StationRadioMode_Type=HpnicfDot11RadioType
_HpnicfDot11StationRadioMode_Object=MibTableColumn
hpnicfDot11StationRadioMode=_HpnicfDot11StationRadioMode_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,3,1,1,1,21),_HpnicfDot11StationRadioMode_Type())
hpnicfDot11StationRadioMode.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11StationRadioMode.setStatus(_A)
_HpnicfDot11StationRxNoise_Type=Integer32
_HpnicfDot11StationRxNoise_Object=MibTableColumn
hpnicfDot11StationRxNoise=_HpnicfDot11StationRxNoise_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,3,1,1,1,22),_HpnicfDot11StationRxNoise_Type())
hpnicfDot11StationRxNoise.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11StationRxNoise.setStatus(_A)
_HpnicfDot11StationMACAddress_Type=MacAddress
_HpnicfDot11StationMACAddress_Object=MibTableColumn
hpnicfDot11StationMACAddress=_HpnicfDot11StationMACAddress_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,3,1,1,1,23),_HpnicfDot11StationMACAddress_Type())
hpnicfDot11StationMACAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11StationMACAddress.setStatus(_A)
_HpnicfDot11StationTxSpeed_Type=Integer32
_HpnicfDot11StationTxSpeed_Object=MibTableColumn
hpnicfDot11StationTxSpeed=_HpnicfDot11StationTxSpeed_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,3,1,1,1,24),_HpnicfDot11StationTxSpeed_Type())
hpnicfDot11StationTxSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11StationTxSpeed.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11StationTxSpeed.setUnits(_b)
_HpnicfDot11StationRxSpeed_Type=Integer32
_HpnicfDot11StationRxSpeed_Object=MibTableColumn
hpnicfDot11StationRxSpeed=_HpnicfDot11StationRxSpeed_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,3,1,1,1,25),_HpnicfDot11StationRxSpeed_Type())
hpnicfDot11StationRxSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11StationRxSpeed.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11StationRxSpeed.setUnits(_b)
class _HpnicfDot11StationWmmMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('wmm',1),('nonwmm',2)))
_HpnicfDot11StationWmmMode_Type.__name__=_E
_HpnicfDot11StationWmmMode_Object=MibTableColumn
hpnicfDot11StationWmmMode=_HpnicfDot11StationWmmMode_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,3,1,1,1,26),_HpnicfDot11StationWmmMode_Type())
hpnicfDot11StationWmmMode.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11StationWmmMode.setStatus(_A)
_HpnicfDot11StationSecIEStatus_Type=HpnicfDot11SecIEStatusType
_HpnicfDot11StationSecIEStatus_Object=MibTableColumn
hpnicfDot11StationSecIEStatus=_HpnicfDot11StationSecIEStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,3,1,1,1,27),_HpnicfDot11StationSecIEStatus_Type())
hpnicfDot11StationSecIEStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11StationSecIEStatus.setStatus(_A)
_HpnicfDot11StationUpTimeTicks_Type=TimeTicks
_HpnicfDot11StationUpTimeTicks_Object=MibTableColumn
hpnicfDot11StationUpTimeTicks=_HpnicfDot11StationUpTimeTicks_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,3,1,1,1,28),_HpnicfDot11StationUpTimeTicks_Type())
hpnicfDot11StationUpTimeTicks.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11StationUpTimeTicks.setStatus(_A)
_HpnicfDot11StationRadioMode2_Type=HpnicfDot11RadioType2
_HpnicfDot11StationRadioMode2_Object=MibTableColumn
hpnicfDot11StationRadioMode2=_HpnicfDot11StationRadioMode2_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,3,1,1,1,29),_HpnicfDot11StationRadioMode2_Type())
hpnicfDot11StationRadioMode2.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11StationRadioMode2.setStatus(_A)
_HpnicfDot11StationAssTime_Type=DateAndTime
_HpnicfDot11StationAssTime_Object=MibTableColumn
hpnicfDot11StationAssTime=_HpnicfDot11StationAssTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,3,1,1,1,30),_HpnicfDot11StationAssTime_Type())
hpnicfDot11StationAssTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11StationAssTime.setStatus(_A)
class _HpnicfDot11StationUserAuthType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('portalAuth',1),('authFree',2),('associateAuth',3),('macAuth',4)))
_HpnicfDot11StationUserAuthType_Type.__name__=_E
_HpnicfDot11StationUserAuthType_Object=MibTableColumn
hpnicfDot11StationUserAuthType=_HpnicfDot11StationUserAuthType_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,3,1,1,1,31),_HpnicfDot11StationUserAuthType_Type())
hpnicfDot11StationUserAuthType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11StationUserAuthType.setStatus(_A)
_HpnicfDot11StationRfPingTest_Type=TruthValue
_HpnicfDot11StationRfPingTest_Object=MibTableColumn
hpnicfDot11StationRfPingTest=_HpnicfDot11StationRfPingTest_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,3,1,1,1,32),_HpnicfDot11StationRfPingTest_Type())
hpnicfDot11StationRfPingTest.setMaxAccess('read-write')
if mibBuilder.loadTexts:hpnicfDot11StationRfPingTest.setStatus(_A)
_HpnicfDot11StationMaxRate_Type=Integer32
_HpnicfDot11StationMaxRate_Object=MibTableColumn
hpnicfDot11StationMaxRate=_HpnicfDot11StationMaxRate_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,3,1,1,1,33),_HpnicfDot11StationMaxRate_Type())
hpnicfDot11StationMaxRate.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11StationMaxRate.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11StationMaxRate.setUnits(_K)
class _HpnicfDot11StationPowerSaveModeCM_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_Z,0),(_a,1)))
_HpnicfDot11StationPowerSaveModeCM_Type.__name__=_E
_HpnicfDot11StationPowerSaveModeCM_Object=MibTableColumn
hpnicfDot11StationPowerSaveModeCM=_HpnicfDot11StationPowerSaveModeCM_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,3,1,1,1,34),_HpnicfDot11StationPowerSaveModeCM_Type())
hpnicfDot11StationPowerSaveModeCM.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11StationPowerSaveModeCM.setStatus(_A)
class _HpnicfDot11StationAuthenModeCM_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_c,0),(_d,1)))
_HpnicfDot11StationAuthenModeCM_Type.__name__=_E
_HpnicfDot11StationAuthenModeCM_Object=MibTableColumn
hpnicfDot11StationAuthenModeCM=_HpnicfDot11StationAuthenModeCM_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,3,1,1,1,35),_HpnicfDot11StationAuthenModeCM_Type())
hpnicfDot11StationAuthenModeCM.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11StationAuthenModeCM.setStatus(_A)
class _HpnicfDot11StationAKMModeCM_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_S,0),('psk',1),('radius',2),(_e,3)))
_HpnicfDot11StationAKMModeCM_Type.__name__=_E
_HpnicfDot11StationAKMModeCM_Object=MibTableColumn
hpnicfDot11StationAKMModeCM=_HpnicfDot11StationAKMModeCM_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,3,1,1,1,36),_HpnicfDot11StationAKMModeCM_Type())
hpnicfDot11StationAKMModeCM.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11StationAKMModeCM.setStatus(_A)
class _HpnicfDot11StationSecurityCiphersCM_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_S,0),('wep40',1),('wep104',2),('tkip',3),('aesccmp',4),('wpisms4',5)))
_HpnicfDot11StationSecurityCiphersCM_Type.__name__=_E
_HpnicfDot11StationSecurityCiphersCM_Object=MibTableColumn
hpnicfDot11StationSecurityCiphersCM=_HpnicfDot11StationSecurityCiphersCM_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,3,1,1,1,37),_HpnicfDot11StationSecurityCiphersCM_Type())
hpnicfDot11StationSecurityCiphersCM.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11StationSecurityCiphersCM.setStatus(_A)
class _HpnicfDot11StationSecIEStatusCM_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_S,0),('wpa',1),('wpa2',2),(_e,3)))
_HpnicfDot11StationSecIEStatusCM_Type.__name__=_E
_HpnicfDot11StationSecIEStatusCM_Object=MibTableColumn
hpnicfDot11StationSecIEStatusCM=_HpnicfDot11StationSecIEStatusCM_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,3,1,1,1,38),_HpnicfDot11StationSecIEStatusCM_Type())
hpnicfDot11StationSecIEStatusCM.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11StationSecIEStatusCM.setStatus(_A)
_HpnicfDot11StationAPRelationTable_Object=MibTable
hpnicfDot11StationAPRelationTable=_HpnicfDot11StationAPRelationTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,3,1,2))
if mibBuilder.loadTexts:hpnicfDot11StationAPRelationTable.setStatus(_A)
_HpnicfDot11StationAPRelationEntry_Object=MibTableRow
hpnicfDot11StationAPRelationEntry=_HpnicfDot11StationAPRelationEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,3,1,2,1))
hpnicfDot11StationAPRelationEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:hpnicfDot11StationAPRelationEntry.setStatus(_A)
_HpnicfDot11CurrAPID_Type=HpnicfDot11ObjectIDType
_HpnicfDot11CurrAPID_Object=MibTableColumn
hpnicfDot11CurrAPID=_HpnicfDot11CurrAPID_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,3,1,2,1,1),_HpnicfDot11CurrAPID_Type())
hpnicfDot11CurrAPID.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11CurrAPID.setStatus(_A)
_HpnicfDot11CurrRadioID_Type=HpnicfDot11RadioScopeType
_HpnicfDot11CurrRadioID_Object=MibTableColumn
hpnicfDot11CurrRadioID=_HpnicfDot11CurrRadioID_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,3,1,2,1,2),_HpnicfDot11CurrRadioID_Type())
hpnicfDot11CurrRadioID.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11CurrRadioID.setStatus(_A)
_HpnicfDot11CurrWlanID_Type=Integer32
_HpnicfDot11CurrWlanID_Object=MibTableColumn
hpnicfDot11CurrWlanID=_HpnicfDot11CurrWlanID_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,3,1,2,1,3),_HpnicfDot11CurrWlanID_Type())
hpnicfDot11CurrWlanID.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11CurrWlanID.setStatus(_A)
_HpnicfDot11CurrAntennaID_Type=Integer32
_HpnicfDot11CurrAntennaID_Object=MibTableColumn
hpnicfDot11CurrAntennaID=_HpnicfDot11CurrAntennaID_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,3,1,2,1,4),_HpnicfDot11CurrAntennaID_Type())
hpnicfDot11CurrAntennaID.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11CurrAntennaID.setStatus(_A)
_HpnicfDot11StationStatisTable_Object=MibTable
hpnicfDot11StationStatisTable=_HpnicfDot11StationStatisTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,3,1,3))
if mibBuilder.loadTexts:hpnicfDot11StationStatisTable.setStatus(_A)
_HpnicfDot11StationStatisEntry_Object=MibTableRow
hpnicfDot11StationStatisEntry=_HpnicfDot11StationStatisEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,3,1,3,1))
hpnicfDot11StationStatisEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:hpnicfDot11StationStatisEntry.setStatus(_A)
_HpnicfDot11StationRxFrameCnt_Type=Counter32
_HpnicfDot11StationRxFrameCnt_Object=MibTableColumn
hpnicfDot11StationRxFrameCnt=_HpnicfDot11StationRxFrameCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,3,1,3,1,1),_HpnicfDot11StationRxFrameCnt_Type())
hpnicfDot11StationRxFrameCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11StationRxFrameCnt.setStatus(_A)
_HpnicfDot11StationTxFrameCnt_Type=Counter32
_HpnicfDot11StationTxFrameCnt_Object=MibTableColumn
hpnicfDot11StationTxFrameCnt=_HpnicfDot11StationTxFrameCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,3,1,3,1,2),_HpnicfDot11StationTxFrameCnt_Type())
hpnicfDot11StationTxFrameCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11StationTxFrameCnt.setStatus(_A)
_HpnicfDot11StationDropFrameCnt_Type=Counter32
_HpnicfDot11StationDropFrameCnt_Object=MibTableColumn
hpnicfDot11StationDropFrameCnt=_HpnicfDot11StationDropFrameCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,3,1,3,1,3),_HpnicfDot11StationDropFrameCnt_Type())
hpnicfDot11StationDropFrameCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11StationDropFrameCnt.setStatus(_A)
_HpnicfDot11StationRxFrameBytes_Type=Counter64
_HpnicfDot11StationRxFrameBytes_Object=MibTableColumn
hpnicfDot11StationRxFrameBytes=_HpnicfDot11StationRxFrameBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,3,1,3,1,4),_HpnicfDot11StationRxFrameBytes_Type())
hpnicfDot11StationRxFrameBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11StationRxFrameBytes.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11StationRxFrameBytes.setUnits(_P)
_HpnicfDot11StationTxFrameBytes_Type=Counter64
_HpnicfDot11StationTxFrameBytes_Object=MibTableColumn
hpnicfDot11StationTxFrameBytes=_HpnicfDot11StationTxFrameBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,3,1,3,1,5),_HpnicfDot11StationTxFrameBytes_Type())
hpnicfDot11StationTxFrameBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11StationTxFrameBytes.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11StationTxFrameBytes.setUnits(_P)
_HpnicfDot11StationDropFrameBytes_Type=Counter64
_HpnicfDot11StationDropFrameBytes_Object=MibTableColumn
hpnicfDot11StationDropFrameBytes=_HpnicfDot11StationDropFrameBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,3,1,3,1,6),_HpnicfDot11StationDropFrameBytes_Type())
hpnicfDot11StationDropFrameBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11StationDropFrameBytes.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11StationDropFrameBytes.setUnits(_P)
_HpnicfDot11StationRxRetryPkts_Type=Counter32
_HpnicfDot11StationRxRetryPkts_Object=MibTableColumn
hpnicfDot11StationRxRetryPkts=_HpnicfDot11StationRxRetryPkts_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,3,1,3,1,7),_HpnicfDot11StationRxRetryPkts_Type())
hpnicfDot11StationRxRetryPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11StationRxRetryPkts.setStatus(_A)
_HpnicfDot11StationTxRetryPkts_Type=Counter32
_HpnicfDot11StationTxRetryPkts_Object=MibTableColumn
hpnicfDot11StationTxRetryPkts=_HpnicfDot11StationTxRetryPkts_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,3,1,3,1,8),_HpnicfDot11StationTxRetryPkts_Type())
hpnicfDot11StationTxRetryPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11StationTxRetryPkts.setStatus(_A)
_HpnicfDot11StationRxRetryBytes_Type=Counter64
_HpnicfDot11StationRxRetryBytes_Object=MibTableColumn
hpnicfDot11StationRxRetryBytes=_HpnicfDot11StationRxRetryBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,3,1,3,1,9),_HpnicfDot11StationRxRetryBytes_Type())
hpnicfDot11StationRxRetryBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11StationRxRetryBytes.setStatus(_A)
_HpnicfDot11StationTxRetryBytes_Type=Counter64
_HpnicfDot11StationTxRetryBytes_Object=MibTableColumn
hpnicfDot11StationTxRetryBytes=_HpnicfDot11StationTxRetryBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,3,1,3,1,10),_HpnicfDot11StationTxRetryBytes_Type())
hpnicfDot11StationTxRetryBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11StationTxRetryBytes.setStatus(_A)
_HpnicfDot11StationThroughput_Type=Counter64
_HpnicfDot11StationThroughput_Object=MibTableColumn
hpnicfDot11StationThroughput=_HpnicfDot11StationThroughput_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,3,1,3,1,11),_HpnicfDot11StationThroughput_Type())
hpnicfDot11StationThroughput.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11StationThroughput.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11StationThroughput.setUnits(_P)
_HpnicfDot11StationSuccessTxCnt_Type=Counter32
_HpnicfDot11StationSuccessTxCnt_Object=MibTableColumn
hpnicfDot11StationSuccessTxCnt=_HpnicfDot11StationSuccessTxCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,3,1,3,1,12),_HpnicfDot11StationSuccessTxCnt_Type())
hpnicfDot11StationSuccessTxCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11StationSuccessTxCnt.setStatus(_A)
_HpnicfDot11StationSuccessTxDataCnt_Type=Counter32
_HpnicfDot11StationSuccessTxDataCnt_Object=MibTableColumn
hpnicfDot11StationSuccessTxDataCnt=_HpnicfDot11StationSuccessTxDataCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,3,1,3,1,13),_HpnicfDot11StationSuccessTxDataCnt_Type())
hpnicfDot11StationSuccessTxDataCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11StationSuccessTxDataCnt.setStatus(_A)
_HpnicfDot11StationRxDataFrameCnt_Type=Counter32
_HpnicfDot11StationRxDataFrameCnt_Object=MibTableColumn
hpnicfDot11StationRxDataFrameCnt=_HpnicfDot11StationRxDataFrameCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,3,1,3,1,14),_HpnicfDot11StationRxDataFrameCnt_Type())
hpnicfDot11StationRxDataFrameCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11StationRxDataFrameCnt.setStatus(_A)
_HpnicfDot11StationTxDataFrameCnt_Type=Counter32
_HpnicfDot11StationTxDataFrameCnt_Object=MibTableColumn
hpnicfDot11StationTxDataFrameCnt=_HpnicfDot11StationTxDataFrameCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,3,1,3,1,15),_HpnicfDot11StationTxDataFrameCnt_Type())
hpnicfDot11StationTxDataFrameCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11StationTxDataFrameCnt.setStatus(_A)
_HpnicfDot11StationRxDataFrameBytes_Type=Counter64
_HpnicfDot11StationRxDataFrameBytes_Object=MibTableColumn
hpnicfDot11StationRxDataFrameBytes=_HpnicfDot11StationRxDataFrameBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,3,1,3,1,16),_HpnicfDot11StationRxDataFrameBytes_Type())
hpnicfDot11StationRxDataFrameBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11StationRxDataFrameBytes.setStatus(_A)
_HpnicfDot11StationTxDataFrameBytes_Type=Counter64
_HpnicfDot11StationTxDataFrameBytes_Object=MibTableColumn
hpnicfDot11StationTxDataFrameBytes=_HpnicfDot11StationTxDataFrameBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,3,1,3,1,17),_HpnicfDot11StationTxDataFrameBytes_Type())
hpnicfDot11StationTxDataFrameBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11StationTxDataFrameBytes.setStatus(_A)
_HpnicfDot11StationRxFragCnt_Type=Counter32
_HpnicfDot11StationRxFragCnt_Object=MibTableColumn
hpnicfDot11StationRxFragCnt=_HpnicfDot11StationRxFragCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,3,1,3,1,18),_HpnicfDot11StationRxFragCnt_Type())
hpnicfDot11StationRxFragCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11StationRxFragCnt.setStatus(_A)
_HpnicfDot11StaRxErrDataFrameCnt_Type=Counter64
_HpnicfDot11StaRxErrDataFrameCnt_Object=MibTableColumn
hpnicfDot11StaRxErrDataFrameCnt=_HpnicfDot11StaRxErrDataFrameCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,3,1,3,1,19),_HpnicfDot11StaRxErrDataFrameCnt_Type())
hpnicfDot11StaRxErrDataFrameCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11StaRxErrDataFrameCnt.setStatus(_A)
_HpnicfDot11StaTxRetryDataFrameCnt_Type=Counter64
_HpnicfDot11StaTxRetryDataFrameCnt_Object=MibTableColumn
hpnicfDot11StaTxRetryDataFrameCnt=_HpnicfDot11StaTxRetryDataFrameCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,3,1,3,1,20),_HpnicfDot11StaTxRetryDataFrameCnt_Type())
hpnicfDot11StaTxRetryDataFrameCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11StaTxRetryDataFrameCnt.setStatus(_A)
_HpnicfDot11StaTxDataRatePkts_Type=OctetString
_HpnicfDot11StaTxDataRatePkts_Object=MibTableColumn
hpnicfDot11StaTxDataRatePkts=_HpnicfDot11StaTxDataRatePkts_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,3,1,3,1,21),_HpnicfDot11StaTxDataRatePkts_Type())
hpnicfDot11StaTxDataRatePkts.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11StaTxDataRatePkts.setStatus(_A)
_HpnicfDot11StaRxDataRatePkts_Type=OctetString
_HpnicfDot11StaRxDataRatePkts_Object=MibTableColumn
hpnicfDot11StaRxDataRatePkts=_HpnicfDot11StaRxDataRatePkts_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,3,1,3,1,22),_HpnicfDot11StaRxDataRatePkts_Type())
hpnicfDot11StaRxDataRatePkts.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11StaRxDataRatePkts.setStatus(_A)
_HpnicfDot11StaTxSignalStrengthPkts_Type=OctetString
_HpnicfDot11StaTxSignalStrengthPkts_Object=MibTableColumn
hpnicfDot11StaTxSignalStrengthPkts=_HpnicfDot11StaTxSignalStrengthPkts_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,3,1,3,1,23),_HpnicfDot11StaTxSignalStrengthPkts_Type())
hpnicfDot11StaTxSignalStrengthPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11StaTxSignalStrengthPkts.setStatus(_A)
_HpnicfDot11StaInternetRxFrameBytes_Type=Counter64
_HpnicfDot11StaInternetRxFrameBytes_Object=MibTableColumn
hpnicfDot11StaInternetRxFrameBytes=_HpnicfDot11StaInternetRxFrameBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,3,1,3,1,24),_HpnicfDot11StaInternetRxFrameBytes_Type())
hpnicfDot11StaInternetRxFrameBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11StaInternetRxFrameBytes.setStatus(_A)
_HpnicfDot11StaInternetTxFrameBytes_Type=Counter64
_HpnicfDot11StaInternetTxFrameBytes_Object=MibTableColumn
hpnicfDot11StaInternetTxFrameBytes=_HpnicfDot11StaInternetTxFrameBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,3,1,3,1,25),_HpnicfDot11StaInternetTxFrameBytes_Type())
hpnicfDot11StaInternetTxFrameBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11StaInternetTxFrameBytes.setStatus(_A)
_HpnicfDot11StaLocalRxFrameBytes_Type=Counter64
_HpnicfDot11StaLocalRxFrameBytes_Object=MibTableColumn
hpnicfDot11StaLocalRxFrameBytes=_HpnicfDot11StaLocalRxFrameBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,3,1,3,1,26),_HpnicfDot11StaLocalRxFrameBytes_Type())
hpnicfDot11StaLocalRxFrameBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11StaLocalRxFrameBytes.setStatus(_A)
_HpnicfDot11StaLocalTxFrameBytes_Type=Counter64
_HpnicfDot11StaLocalTxFrameBytes_Object=MibTableColumn
hpnicfDot11StaLocalTxFrameBytes=_HpnicfDot11StaLocalTxFrameBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,3,1,3,1,27),_HpnicfDot11StaLocalTxFrameBytes_Type())
hpnicfDot11StaLocalTxFrameBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11StaLocalTxFrameBytes.setStatus(_A)
_HpnicfDot11StationRfPingTable_Object=MibTable
hpnicfDot11StationRfPingTable=_HpnicfDot11StationRfPingTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,3,1,4))
if mibBuilder.loadTexts:hpnicfDot11StationRfPingTable.setStatus(_A)
_HpnicfDot11StationRfPingEntry_Object=MibTableRow
hpnicfDot11StationRfPingEntry=_HpnicfDot11StationRfPingEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,3,1,4,1))
hpnicfDot11StationRfPingEntry.setIndexNames((0,_B,_J),(0,_B,_f))
if mibBuilder.loadTexts:hpnicfDot11StationRfPingEntry.setStatus(_A)
class _HpnicfDot11StationRfPingIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,214783647))
_HpnicfDot11StationRfPingIndex_Type.__name__=_E
_HpnicfDot11StationRfPingIndex_Object=MibTableColumn
hpnicfDot11StationRfPingIndex=_HpnicfDot11StationRfPingIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,3,1,4,1,1),_HpnicfDot11StationRfPingIndex_Type())
hpnicfDot11StationRfPingIndex.setMaxAccess(_Y)
if mibBuilder.loadTexts:hpnicfDot11StationRfPingIndex.setStatus(_A)
_HpnicfDot11StationRfPingRate_Type=OctetString
_HpnicfDot11StationRfPingRate_Object=MibTableColumn
hpnicfDot11StationRfPingRate=_HpnicfDot11StationRfPingRate_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,3,1,4,1,2),_HpnicfDot11StationRfPingRate_Type())
hpnicfDot11StationRfPingRate.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11StationRfPingRate.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11StationRfPingRate.setUnits(_K)
_HpnicfDot11StationRfPingTxCnt_Type=Integer32
_HpnicfDot11StationRfPingTxCnt_Object=MibTableColumn
hpnicfDot11StationRfPingTxCnt=_HpnicfDot11StationRfPingTxCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,3,1,4,1,3),_HpnicfDot11StationRfPingTxCnt_Type())
hpnicfDot11StationRfPingTxCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11StationRfPingTxCnt.setStatus(_A)
_HpnicfDot11StationRfPingRxCnt_Type=Integer32
_HpnicfDot11StationRfPingRxCnt_Object=MibTableColumn
hpnicfDot11StationRfPingRxCnt=_HpnicfDot11StationRfPingRxCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,3,1,4,1,4),_HpnicfDot11StationRfPingRxCnt_Type())
hpnicfDot11StationRfPingRxCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11StationRfPingRxCnt.setStatus(_A)
_HpnicfDot11StationRfPingRssi_Type=Integer32
_HpnicfDot11StationRfPingRssi_Object=MibTableColumn
hpnicfDot11StationRfPingRssi=_HpnicfDot11StationRfPingRssi_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,3,1,4,1,5),_HpnicfDot11StationRfPingRssi_Type())
hpnicfDot11StationRfPingRssi.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11StationRfPingRssi.setStatus(_A)
_HpnicfDot11StationRfPingRetries_Type=Integer32
_HpnicfDot11StationRfPingRetries_Object=MibTableColumn
hpnicfDot11StationRfPingRetries=_HpnicfDot11StationRfPingRetries_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,3,1,4,1,6),_HpnicfDot11StationRfPingRetries_Type())
hpnicfDot11StationRfPingRetries.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11StationRfPingRetries.setStatus(_A)
_HpnicfDot11StationRfPingRtt_Type=Integer32
_HpnicfDot11StationRfPingRtt_Object=MibTableColumn
hpnicfDot11StationRfPingRtt=_HpnicfDot11StationRfPingRtt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,3,1,4,1,7),_HpnicfDot11StationRfPingRtt_Type())
hpnicfDot11StationRfPingRtt.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11StationRfPingRtt.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11StationRfPingRtt.setUnits('ms')
_HpnicfDot11StationNotifyGroup_ObjectIdentity=ObjectIdentity
hpnicfDot11StationNotifyGroup=_HpnicfDot11StationNotifyGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,75,3,2))
_HpnicfDot11StationTraps_ObjectIdentity=ObjectIdentity
hpnicfDot11StationTraps=_HpnicfDot11StationTraps_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,75,3,2,0))
_HpnicfDot11StationTrapVarObjects_ObjectIdentity=ObjectIdentity
hpnicfDot11StationTrapVarObjects=_HpnicfDot11StationTrapVarObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,75,3,2,1))
_HpnicfDot11StationTrapBSSID_Type=MacAddress
_HpnicfDot11StationTrapBSSID_Object=MibScalar
hpnicfDot11StationTrapBSSID=_HpnicfDot11StationTrapBSSID_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,3,2,1,1),_HpnicfDot11StationTrapBSSID_Type())
hpnicfDot11StationTrapBSSID.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfDot11StationTrapBSSID.setStatus(_A)
_HpnicfDot11StationTrapStaMAC_Type=MacAddress
_HpnicfDot11StationTrapStaMAC_Object=MibScalar
hpnicfDot11StationTrapStaMAC=_HpnicfDot11StationTrapStaMAC_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,3,2,1,2),_HpnicfDot11StationTrapStaMAC_Type())
hpnicfDot11StationTrapStaMAC.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfDot11StationTrapStaMAC.setStatus(_A)
_HpnicfDot11StationSessionStartTime_Type=DateAndTime
_HpnicfDot11StationSessionStartTime_Object=MibScalar
hpnicfDot11StationSessionStartTime=_HpnicfDot11StationSessionStartTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,3,2,1,3),_HpnicfDot11StationSessionStartTime_Type())
hpnicfDot11StationSessionStartTime.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfDot11StationSessionStartTime.setStatus(_A)
_HpnicfDot11StationAssocFailCause_Type=HpnicfDot11AssocFailType
_HpnicfDot11StationAssocFailCause_Object=MibScalar
hpnicfDot11StationAssocFailCause=_HpnicfDot11StationAssocFailCause_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,3,2,1,4),_HpnicfDot11StationAssocFailCause_Type())
hpnicfDot11StationAssocFailCause.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfDot11StationAssocFailCause.setStatus(_A)
_HpnicfDot11StationAuthorFailCause_Type=HpnicfDot11AuthorFailType
_HpnicfDot11StationAuthorFailCause_Object=MibScalar
hpnicfDot11StationAuthorFailCause=_HpnicfDot11StationAuthorFailCause_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,3,2,1,5),_HpnicfDot11StationAuthorFailCause_Type())
hpnicfDot11StationAuthorFailCause.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfDot11StationAuthorFailCause.setStatus(_A)
class _HpnicfDot11StationFailCauseDesc_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnicfDot11StationFailCauseDesc_Type.__name__=_Q
_HpnicfDot11StationFailCauseDesc_Object=MibScalar
hpnicfDot11StationFailCauseDesc=_HpnicfDot11StationFailCauseDesc_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,3,2,1,6),_HpnicfDot11StationFailCauseDesc_Type())
hpnicfDot11StationFailCauseDesc.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfDot11StationFailCauseDesc.setStatus(_A)
_HpnicfDot11StationSessionDuration_Type=Unsigned32
_HpnicfDot11StationSessionDuration_Object=MibScalar
hpnicfDot11StationSessionDuration=_HpnicfDot11StationSessionDuration_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,3,2,1,7),_HpnicfDot11StationSessionDuration_Type())
hpnicfDot11StationSessionDuration.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfDot11StationSessionDuration.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11StationSessionDuration.setUnits(_R)
_HpnicfDot11StationRoamingTime_Type=Unsigned32
_HpnicfDot11StationRoamingTime_Object=MibScalar
hpnicfDot11StationRoamingTime=_HpnicfDot11StationRoamingTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,3,2,1,8),_HpnicfDot11StationRoamingTime_Type())
hpnicfDot11StationRoamingTime.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfDot11StationRoamingTime.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11StationRoamingTime.setUnits(_R)
_HpnicfDot11StationACIPAddress_Type=IpAddress
_HpnicfDot11StationACIPAddress_Object=MibScalar
hpnicfDot11StationACIPAddress=_HpnicfDot11StationACIPAddress_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,3,2,1,9),_HpnicfDot11StationACIPAddress_Type())
hpnicfDot11StationACIPAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfDot11StationACIPAddress.setStatus(_A)
_HpnicfDot11StationAPName_Type=OctetString
_HpnicfDot11StationAPName_Object=MibScalar
hpnicfDot11StationAPName=_HpnicfDot11StationAPName_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,3,2,1,10),_HpnicfDot11StationAPName_Type())
hpnicfDot11StationAPName.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfDot11StationAPName.setStatus(_A)
_HpnicfDot11StationBSSID_Type=MacAddress
_HpnicfDot11StationBSSID_Object=MibScalar
hpnicfDot11StationBSSID=_HpnicfDot11StationBSSID_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,3,2,1,11),_HpnicfDot11StationBSSID_Type())
hpnicfDot11StationBSSID.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfDot11StationBSSID.setStatus(_A)
_HpnicfDot11StaDisconnectReason_Type=OctetString
_HpnicfDot11StaDisconnectReason_Object=MibScalar
hpnicfDot11StaDisconnectReason=_HpnicfDot11StaDisconnectReason_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,3,2,1,12),_HpnicfDot11StaDisconnectReason_Type())
hpnicfDot11StaDisconnectReason.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfDot11StaDisconnectReason.setStatus(_A)
class _HpnicfDot11StationAuthMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_c,1),(_d,2)))
_HpnicfDot11StationAuthMode_Type.__name__=_E
_HpnicfDot11StationAuthMode_Object=MibScalar
hpnicfDot11StationAuthMode=_HpnicfDot11StationAuthMode_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,3,2,1,13),_HpnicfDot11StationAuthMode_Type())
hpnicfDot11StationAuthMode.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfDot11StationAuthMode.setStatus(_A)
_HpnicfDot11StationACIPv6Add_Type=OctetString
_HpnicfDot11StationACIPv6Add_Object=MibScalar
hpnicfDot11StationACIPv6Add=_HpnicfDot11StationACIPv6Add_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,3,2,1,14),_HpnicfDot11StationACIPv6Add_Type())
hpnicfDot11StationACIPv6Add.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfDot11StationACIPv6Add.setStatus(_A)
_HpnicfDot11UserName_Type=OctetString
_HpnicfDot11UserName_Object=MibScalar
hpnicfDot11UserName=_HpnicfDot11UserName_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,3,2,1,15),_HpnicfDot11UserName_Type())
hpnicfDot11UserName.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfDot11UserName.setStatus(_A)
_HpnicfDot11StationTrapAPMacAddress_Type=MacAddress
_HpnicfDot11StationTrapAPMacAddress_Object=MibScalar
hpnicfDot11StationTrapAPMacAddress=_HpnicfDot11StationTrapAPMacAddress_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,3,2,1,16),_HpnicfDot11StationTrapAPMacAddress_Type())
hpnicfDot11StationTrapAPMacAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfDot11StationTrapAPMacAddress.setStatus(_A)
hpnicfDot11StationMICErrorTrap=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,75,3,2,0,1))
hpnicfDot11StationMICErrorTrap.setObjects(*((_B,_G),(_B,_H),(_B,_T),(_B,_I),(_B,_F)))
if mibBuilder.loadTexts:hpnicfDot11StationMICErrorTrap.setStatus(_A)
hpnicfDot11StationAuthenErrorTrap=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,75,3,2,0,2))
hpnicfDot11StationAuthenErrorTrap.setObjects(*((_B,_G),(_B,_H),(_B,_T),(_B,_I),(_B,_F),(_B,_g),(_B,_h)))
if mibBuilder.loadTexts:hpnicfDot11StationAuthenErrorTrap.setStatus(_A)
hpnicfDot11StationAuthorFailTrap=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,75,3,2,0,3))
hpnicfDot11StationAuthorFailTrap.setObjects(*((_B,_L),(_B,_F),(_B,_H),(_B,_I),(_B,_i),(_B,_U),(_B,_G),(_B,_M),(_B,_j),(_B,_V)))
if mibBuilder.loadTexts:hpnicfDot11StationAuthorFailTrap.setStatus(_A)
hpnicfDot11StationAssocFailTrap=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,75,3,2,0,4))
hpnicfDot11StationAssocFailTrap.setObjects(*((_B,_F),(_B,_H),(_B,_I),(_B,_k),(_B,_U),(_B,_G),(_B,_V)))
if mibBuilder.loadTexts:hpnicfDot11StationAssocFailTrap.setStatus(_A)
hpnicfDot11StationDeAssocTrap=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,75,3,2,0,5))
hpnicfDot11StationDeAssocTrap.setObjects(*((_B,_L),(_B,_F),(_B,_N),(_B,_H),(_B,_I),(_B,_W),(_B,_G),(_B,_O),(_B,_M)))
if mibBuilder.loadTexts:hpnicfDot11StationDeAssocTrap.setStatus(_A)
hpnicfDot11StationAuthorSuccTrap=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,75,3,2,0,6))
hpnicfDot11StationAuthorSuccTrap.setObjects(*((_B,_L),(_B,_F),(_B,_N),(_B,_l),(_B,_H),(_B,_I),(_B,_G),(_B,_O),(_B,_M)))
if mibBuilder.loadTexts:hpnicfDot11StationAuthorSuccTrap.setStatus(_A)
hpnicfDot11StationRoamingTrap=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,75,3,2,0,7))
hpnicfDot11StationRoamingTrap.setObjects(*((_B,_G),(_B,_L),(_B,_F),(_B,_N),(_B,_m),(_B,_H),(_B,_I),(_B,_n),(_B,_o)))
if mibBuilder.loadTexts:hpnicfDot11StationRoamingTrap.setStatus(_A)
hpnicfDot11StationDisconnectTrap=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,75,3,2,0,8))
hpnicfDot11StationDisconnectTrap.setObjects(*((_B,_O),(_B,_M),(_B,_I),(_B,_W),(_B,_N),(_B,_G),(_B,_H),(_B,_p),(_B,_F)))
if mibBuilder.loadTexts:hpnicfDot11StationDisconnectTrap.setStatus(_A)
hpnicfDot11UserDisconnectTrap=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,75,3,2,0,9))
hpnicfDot11UserDisconnectTrap.setObjects(*((_B,_O),(_B,_F),(_B,_q)))
if mibBuilder.loadTexts:hpnicfDot11UserDisconnectTrap.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'hpnicfDot11STATION':hpnicfDot11STATION,'hpnicfDot11StationMtGroup':hpnicfDot11StationMtGroup,'hpnicfDot11StationAssociateTable':hpnicfDot11StationAssociateTable,'hpnicfDot11StationAssociateEntry':hpnicfDot11StationAssociateEntry,_J:hpnicfDot11StationMAC,'hpnicfDot11StationIPAddress':hpnicfDot11StationIPAddress,_L:hpnicfDot11StationUserName,'hpnicfDot11StationTxRateSet':hpnicfDot11StationTxRateSet,'hpnicfDot11StationUpTime':hpnicfDot11StationUpTime,'hpnicfDot11StationSignalStrength':hpnicfDot11StationSignalStrength,'hpnicfDot11StationRSSI':hpnicfDot11StationRSSI,'hpnicfDot11StationChannel':hpnicfDot11StationChannel,'hpnicfDot11StationPowerSaveMode':hpnicfDot11StationPowerSaveMode,'hpnicfDot11StationAid':hpnicfDot11StationAid,_N:hpnicfDot11StationVlanId,_I:hpnicfDot11StationSSIDName,_g:hpnicfDot11StationAuthenMode,_h:hpnicfDot11StationAKMMode,'hpnicfDot11StationSecurityCiphers':hpnicfDot11StationSecurityCiphers,'hpnicfDot11StationSSIDEncryptMode':hpnicfDot11StationSSIDEncryptMode,'hpnicfDot11StationRxSNR':hpnicfDot11StationRxSNR,'hpnicfDot11StationTxRate':hpnicfDot11StationTxRate,'hpnicfDot11StationRxRate':hpnicfDot11StationRxRate,'hpnicfDot11StationVendorName':hpnicfDot11StationVendorName,'hpnicfDot11StationRadioMode':hpnicfDot11StationRadioMode,'hpnicfDot11StationRxNoise':hpnicfDot11StationRxNoise,'hpnicfDot11StationMACAddress':hpnicfDot11StationMACAddress,'hpnicfDot11StationTxSpeed':hpnicfDot11StationTxSpeed,'hpnicfDot11StationRxSpeed':hpnicfDot11StationRxSpeed,'hpnicfDot11StationWmmMode':hpnicfDot11StationWmmMode,'hpnicfDot11StationSecIEStatus':hpnicfDot11StationSecIEStatus,'hpnicfDot11StationUpTimeTicks':hpnicfDot11StationUpTimeTicks,'hpnicfDot11StationRadioMode2':hpnicfDot11StationRadioMode2,'hpnicfDot11StationAssTime':hpnicfDot11StationAssTime,'hpnicfDot11StationUserAuthType':hpnicfDot11StationUserAuthType,'hpnicfDot11StationRfPingTest':hpnicfDot11StationRfPingTest,'hpnicfDot11StationMaxRate':hpnicfDot11StationMaxRate,'hpnicfDot11StationPowerSaveModeCM':hpnicfDot11StationPowerSaveModeCM,'hpnicfDot11StationAuthenModeCM':hpnicfDot11StationAuthenModeCM,'hpnicfDot11StationAKMModeCM':hpnicfDot11StationAKMModeCM,'hpnicfDot11StationSecurityCiphersCM':hpnicfDot11StationSecurityCiphersCM,'hpnicfDot11StationSecIEStatusCM':hpnicfDot11StationSecIEStatusCM,'hpnicfDot11StationAPRelationTable':hpnicfDot11StationAPRelationTable,'hpnicfDot11StationAPRelationEntry':hpnicfDot11StationAPRelationEntry,_G:hpnicfDot11CurrAPID,_H:hpnicfDot11CurrRadioID,'hpnicfDot11CurrWlanID':hpnicfDot11CurrWlanID,'hpnicfDot11CurrAntennaID':hpnicfDot11CurrAntennaID,'hpnicfDot11StationStatisTable':hpnicfDot11StationStatisTable,'hpnicfDot11StationStatisEntry':hpnicfDot11StationStatisEntry,'hpnicfDot11StationRxFrameCnt':hpnicfDot11StationRxFrameCnt,'hpnicfDot11StationTxFrameCnt':hpnicfDot11StationTxFrameCnt,'hpnicfDot11StationDropFrameCnt':hpnicfDot11StationDropFrameCnt,'hpnicfDot11StationRxFrameBytes':hpnicfDot11StationRxFrameBytes,'hpnicfDot11StationTxFrameBytes':hpnicfDot11StationTxFrameBytes,'hpnicfDot11StationDropFrameBytes':hpnicfDot11StationDropFrameBytes,'hpnicfDot11StationRxRetryPkts':hpnicfDot11StationRxRetryPkts,'hpnicfDot11StationTxRetryPkts':hpnicfDot11StationTxRetryPkts,'hpnicfDot11StationRxRetryBytes':hpnicfDot11StationRxRetryBytes,'hpnicfDot11StationTxRetryBytes':hpnicfDot11StationTxRetryBytes,'hpnicfDot11StationThroughput':hpnicfDot11StationThroughput,'hpnicfDot11StationSuccessTxCnt':hpnicfDot11StationSuccessTxCnt,'hpnicfDot11StationSuccessTxDataCnt':hpnicfDot11StationSuccessTxDataCnt,'hpnicfDot11StationRxDataFrameCnt':hpnicfDot11StationRxDataFrameCnt,'hpnicfDot11StationTxDataFrameCnt':hpnicfDot11StationTxDataFrameCnt,'hpnicfDot11StationRxDataFrameBytes':hpnicfDot11StationRxDataFrameBytes,'hpnicfDot11StationTxDataFrameBytes':hpnicfDot11StationTxDataFrameBytes,'hpnicfDot11StationRxFragCnt':hpnicfDot11StationRxFragCnt,'hpnicfDot11StaRxErrDataFrameCnt':hpnicfDot11StaRxErrDataFrameCnt,'hpnicfDot11StaTxRetryDataFrameCnt':hpnicfDot11StaTxRetryDataFrameCnt,'hpnicfDot11StaTxDataRatePkts':hpnicfDot11StaTxDataRatePkts,'hpnicfDot11StaRxDataRatePkts':hpnicfDot11StaRxDataRatePkts,'hpnicfDot11StaTxSignalStrengthPkts':hpnicfDot11StaTxSignalStrengthPkts,'hpnicfDot11StaInternetRxFrameBytes':hpnicfDot11StaInternetRxFrameBytes,'hpnicfDot11StaInternetTxFrameBytes':hpnicfDot11StaInternetTxFrameBytes,'hpnicfDot11StaLocalRxFrameBytes':hpnicfDot11StaLocalRxFrameBytes,'hpnicfDot11StaLocalTxFrameBytes':hpnicfDot11StaLocalTxFrameBytes,'hpnicfDot11StationRfPingTable':hpnicfDot11StationRfPingTable,'hpnicfDot11StationRfPingEntry':hpnicfDot11StationRfPingEntry,_f:hpnicfDot11StationRfPingIndex,'hpnicfDot11StationRfPingRate':hpnicfDot11StationRfPingRate,'hpnicfDot11StationRfPingTxCnt':hpnicfDot11StationRfPingTxCnt,'hpnicfDot11StationRfPingRxCnt':hpnicfDot11StationRfPingRxCnt,'hpnicfDot11StationRfPingRssi':hpnicfDot11StationRfPingRssi,'hpnicfDot11StationRfPingRetries':hpnicfDot11StationRfPingRetries,'hpnicfDot11StationRfPingRtt':hpnicfDot11StationRfPingRtt,'hpnicfDot11StationNotifyGroup':hpnicfDot11StationNotifyGroup,'hpnicfDot11StationTraps':hpnicfDot11StationTraps,'hpnicfDot11StationMICErrorTrap':hpnicfDot11StationMICErrorTrap,'hpnicfDot11StationAuthenErrorTrap':hpnicfDot11StationAuthenErrorTrap,'hpnicfDot11StationAuthorFailTrap':hpnicfDot11StationAuthorFailTrap,'hpnicfDot11StationAssocFailTrap':hpnicfDot11StationAssocFailTrap,'hpnicfDot11StationDeAssocTrap':hpnicfDot11StationDeAssocTrap,'hpnicfDot11StationAuthorSuccTrap':hpnicfDot11StationAuthorSuccTrap,'hpnicfDot11StationRoamingTrap':hpnicfDot11StationRoamingTrap,'hpnicfDot11StationDisconnectTrap':hpnicfDot11StationDisconnectTrap,'hpnicfDot11UserDisconnectTrap':hpnicfDot11UserDisconnectTrap,'hpnicfDot11StationTrapVarObjects':hpnicfDot11StationTrapVarObjects,_T:hpnicfDot11StationTrapBSSID,_F:hpnicfDot11StationTrapStaMAC,_l:hpnicfDot11StationSessionStartTime,_k:hpnicfDot11StationAssocFailCause,_i:hpnicfDot11StationAuthorFailCause,_U:hpnicfDot11StationFailCauseDesc,_W:hpnicfDot11StationSessionDuration,_m:hpnicfDot11StationRoamingTime,_n:hpnicfDot11StationACIPAddress,_O:hpnicfDot11StationAPName,_M:hpnicfDot11StationBSSID,_p:hpnicfDot11StaDisconnectReason,_j:hpnicfDot11StationAuthMode,_o:hpnicfDot11StationACIPv6Add,_q:hpnicfDot11UserName,_V:hpnicfDot11StationTrapAPMacAddress})