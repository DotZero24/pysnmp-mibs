_B4='zxAnDsx1CurrWorkingDsx1'
_B3='zxAnDsx1StandbyDsx1LinkNo'
_B2='zxAnDsx1StandbyDsx1Slot'
_B1='zxAnDsx1StandbyDsx1Shelf'
_B0='zxAnDsx1StandbyDsx1Rack'
_A_='zxAnDsx1MasterDsx1LinkNo'
_Az='zxAnDsx1MasterDsx1Slot'
_Ay='zxAnDsx1MasterDsx1Shelf'
_Ax='zxAnDsx1MasterDsx1Rack'
_Aw='zxAnDsx1ProtectionGroupName'
_Av='msagTrapIpAddress'
_Au='msagTrapParaLinkId'
_At='zxAnTrapInfoType'
_As='msagTrapErrcode'
_Ar='zxAnVoipCallerTestLogicalId'
_Aq='zxAnVoipCallerTestCircuitType'
_Ap='zxAnVoipCallerTestOnu'
_Ao='zxAnVoipCallerTestPort'
_An='zxAnVoipCallerTestSlot'
_Am='zxAnVoipCallerTestShelf'
_Al='zxAnVoipCallerTestRack'
_Ak='wrongDigit'
_Aj='noBidirectionVoice'
_Ai='noDownstreamVoice'
_Ah='noUpstreamVoice'
_Ag='connected'
_Af='servicePort'
_Ae='gemportOrLlid'
_Ad='bridgePort'
_Ac='physicalPort'
_Ab='zxAnVoipCalleeTestLogicalId'
_Aa='zxAnVoipCalleeTestCircuitType'
_AZ='zxAnVoipCalleeTestOnu'
_AY='zxAnVoipCalleeTestPort'
_AX='zxAnVoipCalleeTestSlot'
_AW='zxAnVoipCalleeTestShelf'
_AV='zxAnVoipCalleeTestRack'
_AU='a200rtpparparid'
_AT='a200IpsTermIDSeqNo'
_AS='a200slcTermIDBeginIndex'
_AR='a200slcTermIDslotno'
_AQ='a200slcTermIDshelfno'
_AP='a200slcTermIDrackno'
_AO='zxAnHwTimeSlotUsageShelf'
_AN='zxAnHwTimeSlotUsageRack'
_AM='zxAnDsx1ProtectionGroupId'
_AL='zxAnSelfswitchTktFtpServerId'
_AK='calloptIndex'
_AJ='a200CtlPortCtlId'
_AI='a200VoipRouteDestIp'
_AH='a200VoipRouteType'
_AG='a200VoipRouteMgId'
_AF='a200DigitMapDas'
_AE='a200MiscIndex'
_AD='a200QovsId'
_AC='a200mednatSubCard'
_AB='a200mednatIpsSlot'
_AA='a200mednatIpsShelf'
_A9='a200mednatIpsRack'
_A8='typeDisable'
_A7='typeEnable'
_A6='a200MgcTypeId'
_A5='a200mgcmgcid'
_A4='OctetString'
_A3='zxAnHwTimeSlotUsage'
_A2='zxAnHwTimeSlotUsageThreshold'
_A1='msagQosAlarmDetail'
_A0='msagQosAlarmType'
_z='msagTrapPort'
_y='msagTrapCurState'
_x='msagTrapCurEvent'
_w='msagTrapDLProType'
_v='msagTrapV5InterId'
_u='msagTrapReasionValue'
_t='msagTrapPcmNo'
_s='msagTrapUnitNo'
_r='zxAnIpsUsage'
_q='a200ipsThreshold'
_p='zxAnIpsResourceAlarmReason'
_o='zxAnNarrowbandResActType'
_n='zxAnNarrowbandResCfgType'
_m='failed'
_l='success'
_k='inProgress'
_j='notStarted'
_i='busyTone'
_h='allwaysLimit'
_g='percent'
_f='zxAnTrapSunit'
_e='zxAnTrapUnit'
_d='notLimit'
_c='notsend'
_b='send'
_a='notalways'
_Z='alwayssend'
_Y='msagTrapMgcNo'
_X='msagTrapLinkState'
_W='report'
_V='notReport'
_U='Unsigned32'
_T='typeMinDelay'
_S='typeMaxThruput'
_R='typeMaxSecurity'
_Q='typeMinFee'
_P='typeCommon'
_O='msagTrapReason'
_N='enable'
_M='disable'
_L='DisplayString'
_K='zxAnTrapSlot'
_J='zxAnTrapShelf'
_I='zxAnTrapRack'
_H='zxAnTrapPort'
_G='not-accessible'
_F='read-only'
_E='read-write'
_D='read-create'
_C='ZTE-AN-VOIP-BASE-MIB'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_A4,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_U,'enterprises','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_L,'MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
zxAnVoipBaseMib=ModuleIdentity((1,3,6,1,4,1,3902,1015,5200))
class A200ShelfTypes(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,8,9,10,11,12,13,14,15)));namedValues=NamedValues(*(('dBCONBSTBASE',1),('dBCONBSTBASE1',2),('dBCONBSTSLC',3),('dBCONBSTSLC1',4),('dBCONBSTMSAGEX',5),('dBCONBSTMSAGCTL',6),('dBONU100',8),('dBOUT50C',9),('dBOUT50D',10),('dBMBSLCTL',11),('dBMBSLEX',12),('dBTPUEX',13),('dBPPEX',14),('dBDOUBLEPPEX',15)))
class A200BoardTypes(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('dBCONWBTASCL',1),('dBCONWBTAMTT',2),('dBCONWBTMFP',3),('dBCONWBTAPR',4),('dBCONWBTAMSNIC',5),('dBCONWBTASP',6),('dBCONWBTASPI',7),('dBCONWBTAPOW',8),('dBCONWBTAPOWP',9),('dBCONWBTAFAN',10)))
_Zte_ObjectIdentity=ObjectIdentity
zte=_Zte_ObjectIdentity((1,3,6,1,4,1,3902))
_Msag_ObjectIdentity=ObjectIdentity
msag=_Msag_ObjectIdentity((1,3,6,1,4,1,3902,1015))
_MsagmajorVersion_ObjectIdentity=ObjectIdentity
msagmajorVersion=_MsagmajorVersion_ObjectIdentity((1,3,6,1,4,1,3902,1015,5200,3))
_MsagGlobalConfig_ObjectIdentity=ObjectIdentity
msagGlobalConfig=_MsagGlobalConfig_ObjectIdentity((1,3,6,1,4,1,3902,1015,5200,3,1))
_A200MgCfgTable_Object=MibTable
a200MgCfgTable=_A200MgCfgTable_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1))
if mibBuilder.loadTexts:a200MgCfgTable.setStatus(_A)
_A200MgCfgEntry_Object=MibTableRow
a200MgCfgEntry=_A200MgCfgEntry_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1,1))
a200MgCfgEntry.setIndexNames((0,_C,'a200mgid'))
if mibBuilder.loadTexts:a200MgCfgEntry.setStatus(_A)
_A200mgid_Type=Integer32
_A200mgid_Object=MibTableColumn
a200mgid=_A200mgid_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1,1,1),_A200mgid_Type())
a200mgid.setMaxAccess(_G)
if mibBuilder.loadTexts:a200mgid.setStatus(_A)
_A200protype_Type=Integer32
_A200protype_Object=MibTableColumn
a200protype=_A200protype_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1,1,2),_A200protype_Type())
a200protype.setMaxAccess(_D)
if mibBuilder.loadTexts:a200protype.setStatus(_A)
_A200version_Type=Integer32
_A200version_Object=MibTableColumn
a200version=_A200version_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1,1,3),_A200version_Type())
a200version.setMaxAccess(_D)
if mibBuilder.loadTexts:a200version.setStatus(_A)
_A200encodetp_Type=Integer32
_A200encodetp_Object=MibTableColumn
a200encodetp=_A200encodetp_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1,1,4),_A200encodetp_Type())
a200encodetp.setMaxAccess(_D)
if mibBuilder.loadTexts:a200encodetp.setStatus(_A)
_A200mgport_Type=Integer32
_A200mgport_Object=MibTableColumn
a200mgport=_A200mgport_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1,1,5),_A200mgport_Type())
a200mgport.setMaxAccess(_D)
if mibBuilder.loadTexts:a200mgport.setStatus(_A)
_A200translay_Type=Integer32
_A200translay_Object=MibTableColumn
a200translay=_A200translay_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1,1,6),_A200translay_Type())
a200translay.setMaxAccess(_D)
if mibBuilder.loadTexts:a200translay.setStatus(_A)
_A200transpro_Type=Integer32
_A200transpro_Object=MibTableColumn
a200transpro=_A200transpro_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1,1,7),_A200transpro_Type())
a200transpro.setMaxAccess(_D)
if mibBuilder.loadTexts:a200transpro.setStatus(_A)
class _A200mgDomainName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_A200mgDomainName_Type.__name__=_L
_A200mgDomainName_Object=MibTableColumn
a200mgDomainName=_A200mgDomainName_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1,1,8),_A200mgDomainName_Type())
a200mgDomainName.setMaxAccess(_D)
if mibBuilder.loadTexts:a200mgDomainName.setStatus(_A)
class _A200mgInfo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,4,128)));namedValues=NamedValues(*(('useIp',0),('useDomain',1),('ipsIdle',4),('englishTone',128)))
_A200mgInfo_Type.__name__=_B
_A200mgInfo_Object=MibTableColumn
a200mgInfo=_A200mgInfo_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1,1,9),_A200mgInfo_Type())
a200mgInfo.setMaxAccess(_D)
if mibBuilder.loadTexts:a200mgInfo.setStatus(_A)
class _A200mgcid1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_A200mgcid1_Type.__name__=_B
_A200mgcid1_Object=MibTableColumn
a200mgcid1=_A200mgcid1_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1,1,10),_A200mgcid1_Type())
a200mgcid1.setMaxAccess(_D)
if mibBuilder.loadTexts:a200mgcid1.setStatus(_A)
class _A200mgcid2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_A200mgcid2_Type.__name__=_B
_A200mgcid2_Object=MibTableColumn
a200mgcid2=_A200mgcid2_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1,1,11),_A200mgcid2_Type())
a200mgcid2.setMaxAccess(_D)
if mibBuilder.loadTexts:a200mgcid2.setStatus(_A)
class _A200mgcid3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_A200mgcid3_Type.__name__=_B
_A200mgcid3_Object=MibTableColumn
a200mgcid3=_A200mgcid3_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1,1,12),_A200mgcid3_Type())
a200mgcid3.setMaxAccess(_D)
if mibBuilder.loadTexts:a200mgcid3.setStatus(_A)
class _A200mgcid4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_A200mgcid4_Type.__name__=_B
_A200mgcid4_Object=MibTableColumn
a200mgcid4=_A200mgcid4_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1,1,13),_A200mgcid4_Type())
a200mgcid4.setMaxAccess(_D)
if mibBuilder.loadTexts:a200mgcid4.setStatus(_A)
class _A200selfexchange_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_M,0),(_N,1)))
_A200selfexchange_Type.__name__=_B
_A200selfexchange_Object=MibTableColumn
a200selfexchange=_A200selfexchange_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1,1,14),_A200selfexchange_Type())
a200selfexchange.setMaxAccess(_D)
if mibBuilder.loadTexts:a200selfexchange.setStatus(_A)
class _A200protectcall_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_M,0),(_N,1)))
_A200protectcall_Type.__name__=_B
_A200protectcall_Object=MibTableColumn
a200protectcall=_A200protectcall_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1,1,15),_A200protectcall_Type())
a200protectcall.setMaxAccess(_D)
if mibBuilder.loadTexts:a200protectcall.setStatus(_A)
class _A200disasterprot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('disble',0),(_N,1)))
_A200disasterprot_Type.__name__=_B
_A200disasterprot_Object=MibTableColumn
a200disasterprot=_A200disasterprot_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1,1,16),_A200disasterprot_Type())
a200disasterprot.setMaxAccess(_D)
if mibBuilder.loadTexts:a200disasterprot.setStatus(_A)
_A200mgRowStatus_Type=RowStatus
_A200mgRowStatus_Object=MibTableColumn
a200mgRowStatus=_A200mgRowStatus_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1,1,17),_A200mgRowStatus_Type())
a200mgRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:a200mgRowStatus.setStatus(_A)
_A200tractnum_Type=Integer32
_A200tractnum_Object=MibTableColumn
a200tractnum=_A200tractnum_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1,1,18),_A200tractnum_Type())
a200tractnum.setMaxAccess(_D)
if mibBuilder.loadTexts:a200tractnum.setStatus(_A)
_A200sdpcho_Type=Integer32
_A200sdpcho_Object=MibTableColumn
a200sdpcho=_A200sdpcho_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1,1,19),_A200sdpcho_Type())
a200sdpcho.setMaxAccess(_D)
if mibBuilder.loadTexts:a200sdpcho.setStatus(_A)
_A200retrannum_Type=Integer32
_A200retrannum_Object=MibTableColumn
a200retrannum=_A200retrannum_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1,1,20),_A200retrannum_Type())
a200retrannum.setMaxAccess(_D)
if mibBuilder.loadTexts:a200retrannum.setStatus(_A)
_A200resdelay_Type=Integer32
_A200resdelay_Object=MibTableColumn
a200resdelay=_A200resdelay_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1,1,21),_A200resdelay_Type())
a200resdelay.setMaxAccess(_D)
if mibBuilder.loadTexts:a200resdelay.setStatus(_A)
_A200retranmin_Type=Integer32
_A200retranmin_Object=MibTableColumn
a200retranmin=_A200retranmin_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1,1,22),_A200retranmin_Type())
a200retranmin.setMaxAccess(_D)
if mibBuilder.loadTexts:a200retranmin.setStatus(_A)
_A200lkpttime_Type=Integer32
_A200lkpttime_Object=MibTableColumn
a200lkpttime=_A200lkpttime_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1,1,23),_A200lkpttime_Type())
a200lkpttime.setMaxAccess(_D)
if mibBuilder.loadTexts:a200lkpttime.setStatus(_A)
_A200pendtime_Type=Integer32
_A200pendtime_Object=MibTableColumn
a200pendtime=_A200pendtime_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1,1,24),_A200pendtime_Type())
a200pendtime.setMaxAccess(_D)
if mibBuilder.loadTexts:a200pendtime.setStatus(_A)
_A200pendcount_Type=Integer32
_A200pendcount_Object=MibTableColumn
a200pendcount=_A200pendcount_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1,1,25),_A200pendcount_Type())
a200pendcount.setMaxAccess(_D)
if mibBuilder.loadTexts:a200pendcount.setStatus(_A)
_A200kprestime_Type=Integer32
_A200kprestime_Object=MibTableColumn
a200kprestime=_A200kprestime_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1,1,26),_A200kprestime_Type())
a200kprestime.setMaxAccess(_D)
if mibBuilder.loadTexts:a200kprestime.setStatus(_A)
_A200tranidmax_Type=Unsigned32
_A200tranidmax_Object=MibTableColumn
a200tranidmax=_A200tranidmax_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1,1,27),_A200tranidmax_Type())
a200tranidmax.setMaxAccess(_D)
if mibBuilder.loadTexts:a200tranidmax.setStatus(_A)
_A200tranidmin_Type=Unsigned32
_A200tranidmin_Object=MibTableColumn
a200tranidmin=_A200tranidmin_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1,1,28),_A200tranidmin_Type())
a200tranidmin.setMaxAccess(_D)
if mibBuilder.loadTexts:a200tranidmin.setStatus(_A)
class _A200rtpFaxPri1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('faxVBD',1),('faxT38',2)))
_A200rtpFaxPri1_Type.__name__=_B
_A200rtpFaxPri1_Object=MibTableColumn
a200rtpFaxPri1=_A200rtpFaxPri1_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1,1,29),_A200rtpFaxPri1_Type())
a200rtpFaxPri1.setMaxAccess(_D)
if mibBuilder.loadTexts:a200rtpFaxPri1.setStatus(_A)
class _A200rtpFaxPri2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('faxVBD',1),('faxT38',2)))
_A200rtpFaxPri2_Type.__name__=_B
_A200rtpFaxPri2_Object=MibTableColumn
a200rtpFaxPri2=_A200rtpFaxPri2_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1,1,30),_A200rtpFaxPri2_Type())
a200rtpFaxPri2.setMaxAccess(_D)
if mibBuilder.loadTexts:a200rtpFaxPri2.setStatus(_A)
class _A200subsuspendrtp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('sub',1),('notsub',2)))
_A200subsuspendrtp_Type.__name__=_B
_A200subsuspendrtp_Object=MibTableColumn
a200subsuspendrtp=_A200subsuspendrtp_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1,1,31),_A200subsuspendrtp_Type())
a200subsuspendrtp.setMaxAccess(_D)
if mibBuilder.loadTexts:a200subsuspendrtp.setStatus(_A)
class _A200hotlinewithspace_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('withoutSpace',0),('withSpace',1),('withT',2)))
_A200hotlinewithspace_Type.__name__=_B
_A200hotlinewithspace_Object=MibTableColumn
a200hotlinewithspace=_A200hotlinewithspace_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1,1,32),_A200hotlinewithspace_Type())
a200hotlinewithspace.setMaxAccess(_D)
if mibBuilder.loadTexts:a200hotlinewithspace.setStatus(_A)
class _A200rtp2833Type_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('type2833Redun',1),('typeRTP',2),('type2833NoRedun',3)))
_A200rtp2833Type_Type.__name__=_B
_A200rtp2833Type_Object=MibTableColumn
a200rtp2833Type=_A200rtp2833Type_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1,1,33),_A200rtp2833Type_Type())
a200rtp2833Type.setMaxAccess(_D)
if mibBuilder.loadTexts:a200rtp2833Type.setStatus(_A)
class _A200ipsThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_A200ipsThreshold_Type.__name__=_B
_A200ipsThreshold_Object=MibTableColumn
a200ipsThreshold=_A200ipsThreshold_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1,1,34),_A200ipsThreshold_Type())
a200ipsThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:a200ipsThreshold.setStatus(_A)
class _A200congesttime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,20))
_A200congesttime_Type.__name__=_B
_A200congesttime_Object=MibTableColumn
a200congesttime=_A200congesttime_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1,1,35),_A200congesttime_Type())
a200congesttime.setMaxAccess(_D)
if mibBuilder.loadTexts:a200congesttime.setStatus(_A)
class _A200congesttone_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(0));namedValues=NamedValues(('congtone',0))
_A200congesttone_Type.__name__=_B
_A200congesttone_Object=MibTableColumn
a200congesttone=_A200congesttone_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1,1,36),_A200congesttone_Type())
a200congesttone.setMaxAccess(_D)
if mibBuilder.loadTexts:a200congesttone.setStatus(_A)
_A200callmatchtype_Type=Integer32
_A200callmatchtype_Object=MibTableColumn
a200callmatchtype=_A200callmatchtype_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1,1,37),_A200callmatchtype_Type())
a200callmatchtype.setMaxAccess(_D)
if mibBuilder.loadTexts:a200callmatchtype.setStatus(_A)
_A200currentmgcid_Type=Integer32
_A200currentmgcid_Object=MibTableColumn
a200currentmgcid=_A200currentmgcid_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1,1,38),_A200currentmgcid_Type())
a200currentmgcid.setMaxAccess(_D)
if mibBuilder.loadTexts:a200currentmgcid.setStatus(_A)
class _A200mgSigTos_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,4,8)));namedValues=NamedValues(*((_P,0),(_Q,1),(_R,2),(_S,4),(_T,8)))
_A200mgSigTos_Type.__name__=_B
_A200mgSigTos_Object=MibTableColumn
a200mgSigTos=_A200mgSigTos_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1,1,39),_A200mgSigTos_Type())
a200mgSigTos.setMaxAccess(_D)
if mibBuilder.loadTexts:a200mgSigTos.setStatus(_A)
class _A200mgPSTNMediaVoiceTos_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,4,8)));namedValues=NamedValues(*((_P,0),(_Q,1),(_R,2),(_S,4),(_T,8)))
_A200mgPSTNMediaVoiceTos_Type.__name__=_B
_A200mgPSTNMediaVoiceTos_Object=MibTableColumn
a200mgPSTNMediaVoiceTos=_A200mgPSTNMediaVoiceTos_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1,1,40),_A200mgPSTNMediaVoiceTos_Type())
a200mgPSTNMediaVoiceTos.setMaxAccess(_D)
if mibBuilder.loadTexts:a200mgPSTNMediaVoiceTos.setStatus(_A)
class _A200mgPSTNMediaFaxTos_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,4,8)));namedValues=NamedValues(*((_P,0),(_Q,1),(_R,2),(_S,4),(_T,8)))
_A200mgPSTNMediaFaxTos_Type.__name__=_B
_A200mgPSTNMediaFaxTos_Object=MibTableColumn
a200mgPSTNMediaFaxTos=_A200mgPSTNMediaFaxTos_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1,1,41),_A200mgPSTNMediaFaxTos_Type())
a200mgPSTNMediaFaxTos.setMaxAccess(_D)
if mibBuilder.loadTexts:a200mgPSTNMediaFaxTos.setStatus(_A)
class _A200mgPSTNMediaModemTos_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,4,8)));namedValues=NamedValues(*((_P,0),(_Q,1),(_R,2),(_S,4),(_T,8)))
_A200mgPSTNMediaModemTos_Type.__name__=_B
_A200mgPSTNMediaModemTos_Object=MibTableColumn
a200mgPSTNMediaModemTos=_A200mgPSTNMediaModemTos_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1,1,42),_A200mgPSTNMediaModemTos_Type())
a200mgPSTNMediaModemTos.setMaxAccess(_D)
if mibBuilder.loadTexts:a200mgPSTNMediaModemTos.setStatus(_A)
class _A200mgPSTNMediaDataTos_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,4,8)));namedValues=NamedValues(*((_P,0),(_Q,1),(_R,2),(_S,4),(_T,8)))
_A200mgPSTNMediaDataTos_Type.__name__=_B
_A200mgPSTNMediaDataTos_Object=MibTableColumn
a200mgPSTNMediaDataTos=_A200mgPSTNMediaDataTos_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1,1,43),_A200mgPSTNMediaDataTos_Type())
a200mgPSTNMediaDataTos.setMaxAccess(_D)
if mibBuilder.loadTexts:a200mgPSTNMediaDataTos.setStatus(_A)
class _A200mgISDNMediaVoiceTos_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,4,8)));namedValues=NamedValues(*((_P,0),(_Q,1),(_R,2),(_S,4),(_T,8)))
_A200mgISDNMediaVoiceTos_Type.__name__=_B
_A200mgISDNMediaVoiceTos_Object=MibTableColumn
a200mgISDNMediaVoiceTos=_A200mgISDNMediaVoiceTos_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1,1,44),_A200mgISDNMediaVoiceTos_Type())
a200mgISDNMediaVoiceTos.setMaxAccess(_D)
if mibBuilder.loadTexts:a200mgISDNMediaVoiceTos.setStatus(_A)
class _A200mgISDNMediaFaxTos_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,4,8)));namedValues=NamedValues(*((_P,0),(_Q,1),(_R,2),(_S,4),(_T,8)))
_A200mgISDNMediaFaxTos_Type.__name__=_B
_A200mgISDNMediaFaxTos_Object=MibTableColumn
a200mgISDNMediaFaxTos=_A200mgISDNMediaFaxTos_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1,1,45),_A200mgISDNMediaFaxTos_Type())
a200mgISDNMediaFaxTos.setMaxAccess(_D)
if mibBuilder.loadTexts:a200mgISDNMediaFaxTos.setStatus(_A)
class _A200mgISDNMediaModemTos_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,4,8)));namedValues=NamedValues(*((_P,0),(_Q,1),(_R,2),(_S,4),(_T,8)))
_A200mgISDNMediaModemTos_Type.__name__=_B
_A200mgISDNMediaModemTos_Object=MibTableColumn
a200mgISDNMediaModemTos=_A200mgISDNMediaModemTos_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1,1,46),_A200mgISDNMediaModemTos_Type())
a200mgISDNMediaModemTos.setMaxAccess(_D)
if mibBuilder.loadTexts:a200mgISDNMediaModemTos.setStatus(_A)
class _A200mgISDNMediaDataTos_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,4,8)));namedValues=NamedValues(*((_P,0),(_Q,1),(_R,2),(_S,4),(_T,8)))
_A200mgISDNMediaDataTos_Type.__name__=_B
_A200mgISDNMediaDataTos_Object=MibTableColumn
a200mgISDNMediaDataTos=_A200mgISDNMediaDataTos_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1,1,47),_A200mgISDNMediaDataTos_Type())
a200mgISDNMediaDataTos.setMaxAccess(_D)
if mibBuilder.loadTexts:a200mgISDNMediaDataTos.setStatus(_A)
class _A200ringprofile_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_A200ringprofile_Type.__name__=_B
_A200ringprofile_Object=MibTableColumn
a200ringprofile=_A200ringprofile_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1,1,48),_A200ringprofile_Type())
a200ringprofile.setMaxAccess(_D)
if mibBuilder.loadTexts:a200ringprofile.setStatus(_A)
class _A200toneprofile_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_A200toneprofile_Type.__name__=_B
_A200toneprofile_Object=MibTableColumn
a200toneprofile=_A200toneprofile_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1,1,49),_A200toneprofile_Type())
a200toneprofile.setMaxAccess(_D)
if mibBuilder.loadTexts:a200toneprofile.setStatus(_A)
class _A200flashprofile_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_A200flashprofile_Type.__name__=_B
_A200flashprofile_Object=MibTableColumn
a200flashprofile=_A200flashprofile_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1,1,50),_A200flashprofile_Type())
a200flashprofile.setMaxAccess(_D)
if mibBuilder.loadTexts:a200flashprofile.setStatus(_A)
class _A200chg16kcwidth_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_A200chg16kcwidth_Type.__name__=_U
_A200chg16kcwidth_Object=MibTableColumn
a200chg16kcwidth=_A200chg16kcwidth_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1,1,51),_A200chg16kcwidth_Type())
a200chg16kcwidth.setMaxAccess(_D)
if mibBuilder.loadTexts:a200chg16kcwidth.setStatus(_A)
class _A200chg16kcinterval_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_A200chg16kcinterval_Type.__name__=_U
_A200chg16kcinterval_Object=MibTableColumn
a200chg16kcinterval=_A200chg16kcinterval_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1,1,52),_A200chg16kcinterval_Type())
a200chg16kcinterval.setMaxAccess(_D)
if mibBuilder.loadTexts:a200chg16kcinterval.setStatus(_A)
class _A200charge16kcvol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_A200charge16kcvol_Type.__name__=_B
_A200charge16kcvol_Object=MibTableColumn
a200charge16kcvol=_A200charge16kcvol_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1,1,53),_A200charge16kcvol_Type())
a200charge16kcvol.setMaxAccess(_D)
if mibBuilder.loadTexts:a200charge16kcvol.setStatus(_A)
class _A200kcflag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('power16KC',0),('power12KC',1),('nopower16KC',2),('nopower12KC',3)))
_A200kcflag_Type.__name__=_B
_A200kcflag_Object=MibTableColumn
a200kcflag=_A200kcflag_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1,1,54),_A200kcflag_Type())
a200kcflag.setMaxAccess(_D)
if mibBuilder.loadTexts:a200kcflag.setStatus(_A)
class _A200ExternalSelfswitchEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_M,2)))
_A200ExternalSelfswitchEnable_Type.__name__=_B
_A200ExternalSelfswitchEnable_Object=MibTableColumn
a200ExternalSelfswitchEnable=_A200ExternalSelfswitchEnable_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1,1,55),_A200ExternalSelfswitchEnable_Type())
a200ExternalSelfswitchEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:a200ExternalSelfswitchEnable.setStatus(_A)
class _ZxAnIpsUsage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_ZxAnIpsUsage_Type.__name__=_B
_ZxAnIpsUsage_Object=MibTableColumn
zxAnIpsUsage=_ZxAnIpsUsage_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1,1,56),_ZxAnIpsUsage_Type())
zxAnIpsUsage.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnIpsUsage.setStatus(_A)
if mibBuilder.loadTexts:zxAnIpsUsage.setUnits(_g)
class _A200MgCallEscapeMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('pri',2),('fxo',3)))
_A200MgCallEscapeMode_Type.__name__=_B
_A200MgCallEscapeMode_Object=MibTableColumn
a200MgCallEscapeMode=_A200MgCallEscapeMode_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1,1,57),_A200MgCallEscapeMode_Type())
a200MgCallEscapeMode.setMaxAccess(_D)
if mibBuilder.loadTexts:a200MgCallEscapeMode.setStatus(_A)
_A200mgccfgTable_Object=MibTable
a200mgccfgTable=_A200mgccfgTable_Object((1,3,6,1,4,1,3902,1015,5200,3,1,2))
if mibBuilder.loadTexts:a200mgccfgTable.setStatus(_A)
_A200mgccfgEntry_Object=MibTableRow
a200mgccfgEntry=_A200mgccfgEntry_Object((1,3,6,1,4,1,3902,1015,5200,3,1,2,1))
a200mgccfgEntry.setIndexNames((0,_C,_A5))
if mibBuilder.loadTexts:a200mgccfgEntry.setStatus(_A)
_A200mgcmgcid_Type=Integer32
_A200mgcmgcid_Object=MibTableColumn
a200mgcmgcid=_A200mgcmgcid_Object((1,3,6,1,4,1,3902,1015,5200,3,1,2,1,1),_A200mgcmgcid_Type())
a200mgcmgcid.setMaxAccess(_G)
if mibBuilder.loadTexts:a200mgcmgcid.setStatus(_A)
class _A200mgctypeid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_A200mgctypeid_Type.__name__=_B
_A200mgctypeid_Object=MibTableColumn
a200mgctypeid=_A200mgctypeid_Object((1,3,6,1,4,1,3902,1015,5200,3,1,2,1,2),_A200mgctypeid_Type())
a200mgctypeid.setMaxAccess(_D)
if mibBuilder.loadTexts:a200mgctypeid.setStatus(_A)
_A200mgcip_Type=IpAddress
_A200mgcip_Object=MibTableColumn
a200mgcip=_A200mgcip_Object((1,3,6,1,4,1,3902,1015,5200,3,1,2,1,3),_A200mgcip_Type())
a200mgcip.setMaxAccess(_D)
if mibBuilder.loadTexts:a200mgcip.setStatus(_A)
_A200mgcport_Type=Integer32
_A200mgcport_Object=MibTableColumn
a200mgcport=_A200mgcport_Object((1,3,6,1,4,1,3902,1015,5200,3,1,2,1,4),_A200mgcport_Type())
a200mgcport.setMaxAccess(_D)
if mibBuilder.loadTexts:a200mgcport.setStatus(_A)
class _A200mgcdomain_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_A200mgcdomain_Type.__name__=_L
_A200mgcdomain_Object=MibTableColumn
a200mgcdomain=_A200mgcdomain_Object((1,3,6,1,4,1,3902,1015,5200,3,1,2,1,5),_A200mgcdomain_Type())
a200mgcdomain.setMaxAccess(_D)
if mibBuilder.loadTexts:a200mgcdomain.setStatus(_A)
class _A200mgcinfo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_A200mgcinfo_Type.__name__=_B
_A200mgcinfo_Object=MibTableColumn
a200mgcinfo=_A200mgcinfo_Object((1,3,6,1,4,1,3902,1015,5200,3,1,2,1,6),_A200mgcinfo_Type())
a200mgcinfo.setMaxAccess(_D)
if mibBuilder.loadTexts:a200mgcinfo.setStatus(_A)
class _A200mgcMD5Info_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_A200mgcMD5Info_Type.__name__=_B
_A200mgcMD5Info_Object=MibTableColumn
a200mgcMD5Info=_A200mgcMD5Info_Object((1,3,6,1,4,1,3902,1015,5200,3,1,2,1,7),_A200mgcMD5Info_Type())
a200mgcMD5Info.setMaxAccess(_D)
if mibBuilder.loadTexts:a200mgcMD5Info.setStatus(_A)
_A200mgcRowStatus_Type=RowStatus
_A200mgcRowStatus_Object=MibTableColumn
a200mgcRowStatus=_A200mgcRowStatus_Object((1,3,6,1,4,1,3902,1015,5200,3,1,2,1,8),_A200mgcRowStatus_Type())
a200mgcRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:a200mgcRowStatus.setStatus(_A)
_A200MgcTypeTable_Object=MibTable
a200MgcTypeTable=_A200MgcTypeTable_Object((1,3,6,1,4,1,3902,1015,5200,3,1,3))
if mibBuilder.loadTexts:a200MgcTypeTable.setStatus(_A)
_A200MgcTypeEntry_Object=MibTableRow
a200MgcTypeEntry=_A200MgcTypeEntry_Object((1,3,6,1,4,1,3902,1015,5200,3,1,3,1))
a200MgcTypeEntry.setIndexNames((0,_C,_A6))
if mibBuilder.loadTexts:a200MgcTypeEntry.setStatus(_A)
class _A200MgcTypeId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_A200MgcTypeId_Type.__name__=_B
_A200MgcTypeId_Object=MibTableColumn
a200MgcTypeId=_A200MgcTypeId_Object((1,3,6,1,4,1,3902,1015,5200,3,1,3,1,1),_A200MgcTypeId_Type())
a200MgcTypeId.setMaxAccess(_G)
if mibBuilder.loadTexts:a200MgcTypeId.setStatus(_A)
class _A200MgcTypeDesc_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,17))
_A200MgcTypeDesc_Type.__name__=_L
_A200MgcTypeDesc_Object=MibTableColumn
a200MgcTypeDesc=_A200MgcTypeDesc_Object((1,3,6,1,4,1,3902,1015,5200,3,1,3,1,2),_A200MgcTypeDesc_Type())
a200MgcTypeDesc.setMaxAccess(_D)
if mibBuilder.loadTexts:a200MgcTypeDesc.setStatus(_A)
class _A200MgcTypeMaxTransPkg_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_A200MgcTypeMaxTransPkg_Type.__name__=_B
_A200MgcTypeMaxTransPkg_Object=MibTableColumn
a200MgcTypeMaxTransPkg=_A200MgcTypeMaxTransPkg_Object((1,3,6,1,4,1,3902,1015,5200,3,1,3,1,3),_A200MgcTypeMaxTransPkg_Type())
a200MgcTypeMaxTransPkg.setMaxAccess(_D)
if mibBuilder.loadTexts:a200MgcTypeMaxTransPkg.setStatus(_A)
class _A200MgcTypeReasonQuote_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_A7,1),(_A8,2)))
_A200MgcTypeReasonQuote_Type.__name__=_B
_A200MgcTypeReasonQuote_Object=MibTableColumn
a200MgcTypeReasonQuote=_A200MgcTypeReasonQuote_Object((1,3,6,1,4,1,3902,1015,5200,3,1,3,1,4),_A200MgcTypeReasonQuote_Type())
a200MgcTypeReasonQuote.setMaxAccess(_D)
if mibBuilder.loadTexts:a200MgcTypeReasonQuote.setStatus(_A)
class _A200MgcTypeQueryStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_A8,0),(_A7,1)))
_A200MgcTypeQueryStatus_Type.__name__=_B
_A200MgcTypeQueryStatus_Object=MibTableColumn
a200MgcTypeQueryStatus=_A200MgcTypeQueryStatus_Object((1,3,6,1,4,1,3902,1015,5200,3,1,3,1,5),_A200MgcTypeQueryStatus_Type())
a200MgcTypeQueryStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:a200MgcTypeQueryStatus.setStatus(_A)
class _A200MgcTypeHeartBeat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_A200MgcTypeHeartBeat_Type.__name__=_B
_A200MgcTypeHeartBeat_Object=MibTableColumn
a200MgcTypeHeartBeat=_A200MgcTypeHeartBeat_Object((1,3,6,1,4,1,3902,1015,5200,3,1,3,1,6),_A200MgcTypeHeartBeat_Type())
a200MgcTypeHeartBeat.setMaxAccess(_D)
if mibBuilder.loadTexts:a200MgcTypeHeartBeat.setStatus(_A)
class _A200MgcTypeDmLong_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,50))
_A200MgcTypeDmLong_Type.__name__=_B
_A200MgcTypeDmLong_Object=MibTableColumn
a200MgcTypeDmLong=_A200MgcTypeDmLong_Object((1,3,6,1,4,1,3902,1015,5200,3,1,3,1,7),_A200MgcTypeDmLong_Type())
a200MgcTypeDmLong.setMaxAccess(_D)
if mibBuilder.loadTexts:a200MgcTypeDmLong.setStatus(_A)
class _A200MgcTypeDmShort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,50))
_A200MgcTypeDmShort_Type.__name__=_B
_A200MgcTypeDmShort_Object=MibTableColumn
a200MgcTypeDmShort=_A200MgcTypeDmShort_Object((1,3,6,1,4,1,3902,1015,5200,3,1,3,1,8),_A200MgcTypeDmShort_Type())
a200MgcTypeDmShort.setMaxAccess(_D)
if mibBuilder.loadTexts:a200MgcTypeDmShort.setStatus(_A)
class _A200MgcTypeDmStart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,50))
_A200MgcTypeDmStart_Type.__name__=_B
_A200MgcTypeDmStart_Object=MibTableColumn
a200MgcTypeDmStart=_A200MgcTypeDmStart_Object((1,3,6,1,4,1,3902,1015,5200,3,1,3,1,9),_A200MgcTypeDmStart_Type())
a200MgcTypeDmStart.setMaxAccess(_D)
if mibBuilder.loadTexts:a200MgcTypeDmStart.setStatus(_A)
class _A200MgcTypeWithTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('include',1),('notinclude',2)))
_A200MgcTypeWithTime_Type.__name__=_B
_A200MgcTypeWithTime_Object=MibTableColumn
a200MgcTypeWithTime=_A200MgcTypeWithTime_Object((1,3,6,1,4,1,3902,1015,5200,3,1,3,1,10),_A200MgcTypeWithTime_Type())
a200MgcTypeWithTime.setMaxAccess(_D)
if mibBuilder.loadTexts:a200MgcTypeWithTime.setStatus(_A)
class _A200MgcTypeWithDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_A200MgcTypeWithDelay_Type.__name__=_B
_A200MgcTypeWithDelay_Object=MibTableColumn
a200MgcTypeWithDelay=_A200MgcTypeWithDelay_Object((1,3,6,1,4,1,3902,1015,5200,3,1,3,1,11),_A200MgcTypeWithDelay_Type())
a200MgcTypeWithDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:a200MgcTypeWithDelay.setStatus(_A)
class _A200MgcTypeProfileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_A200MgcTypeProfileName_Type.__name__=_L
_A200MgcTypeProfileName_Object=MibTableColumn
a200MgcTypeProfileName=_A200MgcTypeProfileName_Object((1,3,6,1,4,1,3902,1015,5200,3,1,3,1,12),_A200MgcTypeProfileName_Type())
a200MgcTypeProfileName.setMaxAccess(_D)
if mibBuilder.loadTexts:a200MgcTypeProfileName.setStatus(_A)
class _A200MgcTypeUserOut_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(900,915))
_A200MgcTypeUserOut_Type.__name__=_B
_A200MgcTypeUserOut_Object=MibTableColumn
a200MgcTypeUserOut=_A200MgcTypeUserOut_Object((1,3,6,1,4,1,3902,1015,5200,3,1,3,1,13),_A200MgcTypeUserOut_Type())
a200MgcTypeUserOut.setMaxAccess(_D)
if mibBuilder.loadTexts:a200MgcTypeUserOut.setStatus(_A)
class _A200MgcTypeAgOut_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(900,915))
_A200MgcTypeAgOut_Type.__name__=_B
_A200MgcTypeAgOut_Object=MibTableColumn
a200MgcTypeAgOut=_A200MgcTypeAgOut_Object((1,3,6,1,4,1,3902,1015,5200,3,1,3,1,14),_A200MgcTypeAgOut_Type())
a200MgcTypeAgOut.setMaxAccess(_D)
if mibBuilder.loadTexts:a200MgcTypeAgOut.setStatus(_A)
_A200MgcTypeHeartId_Type=Unsigned32
_A200MgcTypeHeartId_Object=MibTableColumn
a200MgcTypeHeartId=_A200MgcTypeHeartId_Object((1,3,6,1,4,1,3902,1015,5200,3,1,3,1,15),_A200MgcTypeHeartId_Type())
a200MgcTypeHeartId.setMaxAccess(_D)
if mibBuilder.loadTexts:a200MgcTypeHeartId.setStatus(_A)
class _A200MgcTypeAgRegOldMT_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_A200MgcTypeAgRegOldMT_Type.__name__=_B
_A200MgcTypeAgRegOldMT_Object=MibTableColumn
a200MgcTypeAgRegOldMT=_A200MgcTypeAgRegOldMT_Object((1,3,6,1,4,1,3902,1015,5200,3,1,3,1,16),_A200MgcTypeAgRegOldMT_Type())
a200MgcTypeAgRegOldMT.setMaxAccess(_D)
if mibBuilder.loadTexts:a200MgcTypeAgRegOldMT.setStatus(_A)
class _A200MgcTypeCanclerror_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_A200MgcTypeCanclerror_Type.__name__=_B
_A200MgcTypeCanclerror_Object=MibTableColumn
a200MgcTypeCanclerror=_A200MgcTypeCanclerror_Object((1,3,6,1,4,1,3902,1015,5200,3,1,3,1,17),_A200MgcTypeCanclerror_Type())
a200MgcTypeCanclerror.setMaxAccess(_D)
if mibBuilder.loadTexts:a200MgcTypeCanclerror.setStatus(_A)
_A200MgcTypeRowStatus_Type=RowStatus
_A200MgcTypeRowStatus_Object=MibTableColumn
a200MgcTypeRowStatus=_A200MgcTypeRowStatus_Object((1,3,6,1,4,1,3902,1015,5200,3,1,3,1,18),_A200MgcTypeRowStatus_Type())
a200MgcTypeRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:a200MgcTypeRowStatus.setStatus(_A)
_A200MedNatTable_Object=MibTable
a200MedNatTable=_A200MedNatTable_Object((1,3,6,1,4,1,3902,1015,5200,3,1,4))
if mibBuilder.loadTexts:a200MedNatTable.setStatus(_A)
_A200MedNatEntry_Object=MibTableRow
a200MedNatEntry=_A200MedNatEntry_Object((1,3,6,1,4,1,3902,1015,5200,3,1,4,1))
a200MedNatEntry.setIndexNames((0,_C,_A9),(0,_C,_AA),(0,_C,_AB),(0,_C,_AC))
if mibBuilder.loadTexts:a200MedNatEntry.setStatus(_A)
_A200mednatIpsRack_Type=Integer32
_A200mednatIpsRack_Object=MibTableColumn
a200mednatIpsRack=_A200mednatIpsRack_Object((1,3,6,1,4,1,3902,1015,5200,3,1,4,1,1),_A200mednatIpsRack_Type())
a200mednatIpsRack.setMaxAccess(_G)
if mibBuilder.loadTexts:a200mednatIpsRack.setStatus(_A)
_A200mednatIpsShelf_Type=Integer32
_A200mednatIpsShelf_Object=MibTableColumn
a200mednatIpsShelf=_A200mednatIpsShelf_Object((1,3,6,1,4,1,3902,1015,5200,3,1,4,1,2),_A200mednatIpsShelf_Type())
a200mednatIpsShelf.setMaxAccess(_G)
if mibBuilder.loadTexts:a200mednatIpsShelf.setStatus(_A)
_A200mednatIpsSlot_Type=Integer32
_A200mednatIpsSlot_Object=MibTableColumn
a200mednatIpsSlot=_A200mednatIpsSlot_Object((1,3,6,1,4,1,3902,1015,5200,3,1,4,1,3),_A200mednatIpsSlot_Type())
a200mednatIpsSlot.setMaxAccess(_G)
if mibBuilder.loadTexts:a200mednatIpsSlot.setStatus(_A)
_A200mednatSubCard_Type=Integer32
_A200mednatSubCard_Object=MibTableColumn
a200mednatSubCard=_A200mednatSubCard_Object((1,3,6,1,4,1,3902,1015,5200,3,1,4,1,4),_A200mednatSubCard_Type())
a200mednatSubCard.setMaxAccess(_G)
if mibBuilder.loadTexts:a200mednatSubCard.setStatus(_A)
_A200mednatNicRack_Type=Integer32
_A200mednatNicRack_Object=MibTableColumn
a200mednatNicRack=_A200mednatNicRack_Object((1,3,6,1,4,1,3902,1015,5200,3,1,4,1,5),_A200mednatNicRack_Type())
a200mednatNicRack.setMaxAccess(_D)
if mibBuilder.loadTexts:a200mednatNicRack.setStatus(_A)
_A200mednatNicShelf_Type=Integer32
_A200mednatNicShelf_Object=MibTableColumn
a200mednatNicShelf=_A200mednatNicShelf_Object((1,3,6,1,4,1,3902,1015,5200,3,1,4,1,6),_A200mednatNicShelf_Type())
a200mednatNicShelf.setMaxAccess(_D)
if mibBuilder.loadTexts:a200mednatNicShelf.setStatus(_A)
_A200mednatNicSlot_Type=Integer32
_A200mednatNicSlot_Object=MibTableColumn
a200mednatNicSlot=_A200mednatNicSlot_Object((1,3,6,1,4,1,3902,1015,5200,3,1,4,1,7),_A200mednatNicSlot_Type())
a200mednatNicSlot.setMaxAccess(_D)
if mibBuilder.loadTexts:a200mednatNicSlot.setStatus(_A)
_A200mednatInPhyPort_Type=Integer32
_A200mednatInPhyPort_Object=MibTableColumn
a200mednatInPhyPort=_A200mednatInPhyPort_Object((1,3,6,1,4,1,3902,1015,5200,3,1,4,1,8),_A200mednatInPhyPort_Type())
a200mednatInPhyPort.setMaxAccess(_D)
if mibBuilder.loadTexts:a200mednatInPhyPort.setStatus(_A)
_A200mednatExPhyPort_Type=Integer32
_A200mednatExPhyPort_Object=MibTableColumn
a200mednatExPhyPort=_A200mednatExPhyPort_Object((1,3,6,1,4,1,3902,1015,5200,3,1,4,1,9),_A200mednatExPhyPort_Type())
a200mednatExPhyPort.setMaxAccess(_D)
if mibBuilder.loadTexts:a200mednatExPhyPort.setStatus(_A)
_A200mednatExIp_Type=IpAddress
_A200mednatExIp_Object=MibTableColumn
a200mednatExIp=_A200mednatExIp_Object((1,3,6,1,4,1,3902,1015,5200,3,1,4,1,10),_A200mednatExIp_Type())
a200mednatExIp.setMaxAccess(_D)
if mibBuilder.loadTexts:a200mednatExIp.setStatus(_A)
_A200mednatUdpPort_Type=Integer32
_A200mednatUdpPort_Object=MibTableColumn
a200mednatUdpPort=_A200mednatUdpPort_Object((1,3,6,1,4,1,3902,1015,5200,3,1,4,1,11),_A200mednatUdpPort_Type())
a200mednatUdpPort.setMaxAccess(_D)
if mibBuilder.loadTexts:a200mednatUdpPort.setStatus(_A)
_A200mednatRowStatus_Type=RowStatus
_A200mednatRowStatus_Object=MibTableColumn
a200mednatRowStatus=_A200mednatRowStatus_Object((1,3,6,1,4,1,3902,1015,5200,3,1,4,1,12),_A200mednatRowStatus_Type())
a200mednatRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:a200mednatRowStatus.setStatus(_A)
_A200natCtrlId_Type=Integer32
_A200natCtrlId_Object=MibTableColumn
a200natCtrlId=_A200natCtrlId_Object((1,3,6,1,4,1,3902,1015,5200,3,1,4,1,13),_A200natCtrlId_Type())
a200natCtrlId.setMaxAccess(_F)
if mibBuilder.loadTexts:a200natCtrlId.setStatus(_A)
_A200QovsTable_Object=MibTable
a200QovsTable=_A200QovsTable_Object((1,3,6,1,4,1,3902,1015,5200,3,1,5))
if mibBuilder.loadTexts:a200QovsTable.setStatus(_A)
_A200QovsEntry_Object=MibTableRow
a200QovsEntry=_A200QovsEntry_Object((1,3,6,1,4,1,3902,1015,5200,3,1,5,1))
a200QovsEntry.setIndexNames((0,_C,_AD))
if mibBuilder.loadTexts:a200QovsEntry.setStatus(_A)
class _A200QovsId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_A200QovsId_Type.__name__=_B
_A200QovsId_Object=MibTableColumn
a200QovsId=_A200QovsId_Object((1,3,6,1,4,1,3902,1015,5200,3,1,5,1,1),_A200QovsId_Type())
a200QovsId.setMaxAccess(_G)
if mibBuilder.loadTexts:a200QovsId.setStatus(_A)
class _A200QovsLoss_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_A200QovsLoss_Type.__name__=_B
_A200QovsLoss_Object=MibTableColumn
a200QovsLoss=_A200QovsLoss_Object((1,3,6,1,4,1,3902,1015,5200,3,1,5,1,2),_A200QovsLoss_Type())
a200QovsLoss.setMaxAccess(_D)
if mibBuilder.loadTexts:a200QovsLoss.setStatus(_A)
class _A200QovsDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_A200QovsDelay_Type.__name__=_B
_A200QovsDelay_Object=MibTableColumn
a200QovsDelay=_A200QovsDelay_Object((1,3,6,1,4,1,3902,1015,5200,3,1,5,1,3),_A200QovsDelay_Type())
a200QovsDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:a200QovsDelay.setStatus(_A)
class _A200QovsJitter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_A200QovsJitter_Type.__name__=_B
_A200QovsJitter_Object=MibTableColumn
a200QovsJitter=_A200QovsJitter_Object((1,3,6,1,4,1,3902,1015,5200,3,1,5,1,4),_A200QovsJitter_Type())
a200QovsJitter.setMaxAccess(_D)
if mibBuilder.loadTexts:a200QovsJitter.setStatus(_A)
_A200QovsRowStatus_Type=RowStatus
_A200QovsRowStatus_Object=MibTableColumn
a200QovsRowStatus=_A200QovsRowStatus_Object((1,3,6,1,4,1,3902,1015,5200,3,1,5,1,5),_A200QovsRowStatus_Type())
a200QovsRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:a200QovsRowStatus.setStatus(_A)
_A200MiscTable_Object=MibTable
a200MiscTable=_A200MiscTable_Object((1,3,6,1,4,1,3902,1015,5200,3,1,7))
if mibBuilder.loadTexts:a200MiscTable.setStatus(_A)
_A200MiscEntry_Object=MibTableRow
a200MiscEntry=_A200MiscEntry_Object((1,3,6,1,4,1,3902,1015,5200,3,1,7,1))
a200MiscEntry.setIndexNames((0,_C,_AE))
if mibBuilder.loadTexts:a200MiscEntry.setStatus(_A)
class _A200MiscIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_A200MiscIndex_Type.__name__=_B
_A200MiscIndex_Object=MibTableColumn
a200MiscIndex=_A200MiscIndex_Object((1,3,6,1,4,1,3902,1015,5200,3,1,7,1,1),_A200MiscIndex_Type())
a200MiscIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:a200MiscIndex.setStatus(_A)
class _A200MiscFlashDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,50))
_A200MiscFlashDelay_Type.__name__=_B
_A200MiscFlashDelay_Object=MibTableColumn
a200MiscFlashDelay=_A200MiscFlashDelay_Object((1,3,6,1,4,1,3902,1015,5200,3,1,7,1,2),_A200MiscFlashDelay_Type())
a200MiscFlashDelay.setMaxAccess(_E)
if mibBuilder.loadTexts:a200MiscFlashDelay.setStatus(_A)
class _A200MiscCalledPartyReanwer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,600))
_A200MiscCalledPartyReanwer_Type.__name__=_B
_A200MiscCalledPartyReanwer_Object=MibTableColumn
a200MiscCalledPartyReanwer=_A200MiscCalledPartyReanwer_Object((1,3,6,1,4,1,3902,1015,5200,3,1,7,1,3),_A200MiscCalledPartyReanwer_Type())
a200MiscCalledPartyReanwer.setMaxAccess(_E)
if mibBuilder.loadTexts:a200MiscCalledPartyReanwer.setStatus(_A)
class _A200MiscH248BusyStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,1000))
_A200MiscH248BusyStatus_Type.__name__=_B
_A200MiscH248BusyStatus_Object=MibTableColumn
a200MiscH248BusyStatus=_A200MiscH248BusyStatus_Object((1,3,6,1,4,1,3902,1015,5200,3,1,7,1,4),_A200MiscH248BusyStatus_Type())
a200MiscH248BusyStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:a200MiscH248BusyStatus.setStatus(_A)
class _A200MiscHowlTone_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,1000))
_A200MiscHowlTone_Type.__name__=_B
_A200MiscHowlTone_Object=MibTableColumn
a200MiscHowlTone=_A200MiscHowlTone_Object((1,3,6,1,4,1,3902,1015,5200,3,1,7,1,5),_A200MiscHowlTone_Type())
a200MiscHowlTone.setMaxAccess(_E)
if mibBuilder.loadTexts:a200MiscHowlTone.setStatus(_A)
class _A200MiscH248Short_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,50))
_A200MiscH248Short_Type.__name__=_B
_A200MiscH248Short_Object=MibTableColumn
a200MiscH248Short=_A200MiscH248Short_Object((1,3,6,1,4,1,3902,1015,5200,3,1,7,1,6),_A200MiscH248Short_Type())
a200MiscH248Short.setMaxAccess(_E)
if mibBuilder.loadTexts:a200MiscH248Short.setStatus(_A)
class _A200MiscH248Long_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,100))
_A200MiscH248Long_Type.__name__=_B
_A200MiscH248Long_Object=MibTableColumn
a200MiscH248Long=_A200MiscH248Long_Object((1,3,6,1,4,1,3902,1015,5200,3,1,7,1,7),_A200MiscH248Long_Type())
a200MiscH248Long.setMaxAccess(_E)
if mibBuilder.loadTexts:a200MiscH248Long.setStatus(_A)
class _A200MiscRTPtimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,50))
_A200MiscRTPtimer_Type.__name__=_B
_A200MiscRTPtimer_Object=MibTableColumn
a200MiscRTPtimer=_A200MiscRTPtimer_Object((1,3,6,1,4,1,3902,1015,5200,3,1,7,1,8),_A200MiscRTPtimer_Type())
a200MiscRTPtimer.setMaxAccess(_E)
if mibBuilder.loadTexts:a200MiscRTPtimer.setStatus(_A)
class _A200MiscH248RingPattern_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ms',1),('tenms',2),('hundredms',3)))
_A200MiscH248RingPattern_Type.__name__=_B
_A200MiscH248RingPattern_Object=MibTableColumn
a200MiscH248RingPattern=_A200MiscH248RingPattern_Object((1,3,6,1,4,1,3902,1015,5200,3,1,7,1,9),_A200MiscH248RingPattern_Type())
a200MiscH248RingPattern.setMaxAccess(_E)
if mibBuilder.loadTexts:a200MiscH248RingPattern.setStatus(_A)
class _A200MiscCallAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,500))
_A200MiscCallAlarm_Type.__name__=_B
_A200MiscCallAlarm_Object=MibTableColumn
a200MiscCallAlarm=_A200MiscCallAlarm_Object((1,3,6,1,4,1,3902,1015,5200,3,1,7,1,10),_A200MiscCallAlarm_Type())
a200MiscCallAlarm.setMaxAccess(_E)
if mibBuilder.loadTexts:a200MiscCallAlarm.setStatus(_A)
class _A200MiscInterCallAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,300))
_A200MiscInterCallAlarm_Type.__name__=_B
_A200MiscInterCallAlarm_Object=MibTableColumn
a200MiscInterCallAlarm=_A200MiscInterCallAlarm_Object((1,3,6,1,4,1,3902,1015,5200,3,1,7,1,11),_A200MiscInterCallAlarm_Type())
a200MiscInterCallAlarm.setMaxAccess(_E)
if mibBuilder.loadTexts:a200MiscInterCallAlarm.setStatus(_A)
class _A200MiscFreshTnet_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,600))
_A200MiscFreshTnet_Type.__name__=_B
_A200MiscFreshTnet_Object=MibTableColumn
a200MiscFreshTnet=_A200MiscFreshTnet_Object((1,3,6,1,4,1,3902,1015,5200,3,1,7,1,12),_A200MiscFreshTnet_Type())
a200MiscFreshTnet.setMaxAccess(_E)
if mibBuilder.loadTexts:a200MiscFreshTnet.setStatus(_A)
class _A200MiscCheckContext_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_M,0),(_N,1)))
_A200MiscCheckContext_Type.__name__=_B
_A200MiscCheckContext_Object=MibTableColumn
a200MiscCheckContext=_A200MiscCheckContext_Object((1,3,6,1,4,1,3902,1015,5200,3,1,7,1,13),_A200MiscCheckContext_Type())
a200MiscCheckContext.setMaxAccess(_E)
if mibBuilder.loadTexts:a200MiscCheckContext.setStatus(_A)
class _A200MiscUpPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('withTimeStamp',0),('noTimeStamp',1)))
_A200MiscUpPort_Type.__name__=_B
_A200MiscUpPort_Object=MibTableColumn
a200MiscUpPort=_A200MiscUpPort_Object((1,3,6,1,4,1,3902,1015,5200,3,1,7,1,14),_A200MiscUpPort_Type())
a200MiscUpPort.setMaxAccess(_E)
if mibBuilder.loadTexts:a200MiscUpPort.setStatus(_A)
class _A200MiscResReportPeriod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_A200MiscResReportPeriod_Type.__name__=_B
_A200MiscResReportPeriod_Object=MibTableColumn
a200MiscResReportPeriod=_A200MiscResReportPeriod_Object((1,3,6,1,4,1,3902,1015,5200,3,1,7,1,15),_A200MiscResReportPeriod_Type())
a200MiscResReportPeriod.setMaxAccess(_E)
if mibBuilder.loadTexts:a200MiscResReportPeriod.setStatus(_A)
class _A200MiscAgMustDetOvrLd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_M,0),(_N,1)))
_A200MiscAgMustDetOvrLd_Type.__name__=_B
_A200MiscAgMustDetOvrLd_Object=MibTableColumn
a200MiscAgMustDetOvrLd=_A200MiscAgMustDetOvrLd_Object((1,3,6,1,4,1,3902,1015,5200,3,1,7,1,16),_A200MiscAgMustDetOvrLd_Type())
a200MiscAgMustDetOvrLd.setMaxAccess(_E)
if mibBuilder.loadTexts:a200MiscAgMustDetOvrLd.setStatus(_A)
class _A200MiscErrReplyInformSSEn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_M,0),(_N,1)))
_A200MiscErrReplyInformSSEn_Type.__name__=_B
_A200MiscErrReplyInformSSEn_Object=MibTableColumn
a200MiscErrReplyInformSSEn=_A200MiscErrReplyInformSSEn_Object((1,3,6,1,4,1,3902,1015,5200,3,1,7,1,17),_A200MiscErrReplyInformSSEn_Type())
a200MiscErrReplyInformSSEn.setMaxAccess(_E)
if mibBuilder.loadTexts:a200MiscErrReplyInformSSEn.setStatus(_A)
class _A200MiscCookieEchoFormat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('formZTE',0),('formStandard',1)))
_A200MiscCookieEchoFormat_Type.__name__=_B
_A200MiscCookieEchoFormat_Object=MibTableColumn
a200MiscCookieEchoFormat=_A200MiscCookieEchoFormat_Object((1,3,6,1,4,1,3902,1015,5200,3,1,7,1,18),_A200MiscCookieEchoFormat_Type())
a200MiscCookieEchoFormat.setMaxAccess(_E)
if mibBuilder.loadTexts:a200MiscCookieEchoFormat.setStatus(_A)
class _A200MiscCheckSumFormat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('formADLER32',0),('formCRC32',1)))
_A200MiscCheckSumFormat_Type.__name__=_B
_A200MiscCheckSumFormat_Object=MibTableColumn
a200MiscCheckSumFormat=_A200MiscCheckSumFormat_Object((1,3,6,1,4,1,3902,1015,5200,3,1,7,1,19),_A200MiscCheckSumFormat_Type())
a200MiscCheckSumFormat.setMaxAccess(_E)
if mibBuilder.loadTexts:a200MiscCheckSumFormat.setStatus(_A)
class _A200MiscIuaIsdnHwFormat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('formDisable',0),('formEnable',1)))
_A200MiscIuaIsdnHwFormat_Type.__name__=_B
_A200MiscIuaIsdnHwFormat_Object=MibTableColumn
a200MiscIuaIsdnHwFormat=_A200MiscIuaIsdnHwFormat_Object((1,3,6,1,4,1,3902,1015,5200,3,1,7,1,20),_A200MiscIuaIsdnHwFormat_Type())
a200MiscIuaIsdnHwFormat.setMaxAccess(_E)
if mibBuilder.loadTexts:a200MiscIuaIsdnHwFormat.setStatus(_A)
_A200DigitMapTable_Object=MibTable
a200DigitMapTable=_A200DigitMapTable_Object((1,3,6,1,4,1,3902,1015,5200,3,1,8))
if mibBuilder.loadTexts:a200DigitMapTable.setStatus(_A)
_A200DigitMapEntry_Object=MibTableRow
a200DigitMapEntry=_A200DigitMapEntry_Object((1,3,6,1,4,1,3902,1015,5200,3,1,8,1))
a200DigitMapEntry.setIndexNames((0,_C,_AF))
if mibBuilder.loadTexts:a200DigitMapEntry.setStatus(_A)
class _A200DigitMapDas_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_A200DigitMapDas_Type.__name__=_B
_A200DigitMapDas_Object=MibTableColumn
a200DigitMapDas=_A200DigitMapDas_Object((1,3,6,1,4,1,3902,1015,5200,3,1,8,1,1),_A200DigitMapDas_Type())
a200DigitMapDas.setMaxAccess(_G)
if mibBuilder.loadTexts:a200DigitMapDas.setStatus(_A)
class _A200DigitMapMgid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_A200DigitMapMgid_Type.__name__=_B
_A200DigitMapMgid_Object=MibTableColumn
a200DigitMapMgid=_A200DigitMapMgid_Object((1,3,6,1,4,1,3902,1015,5200,3,1,8,1,2),_A200DigitMapMgid_Type())
a200DigitMapMgid.setMaxAccess(_D)
if mibBuilder.loadTexts:a200DigitMapMgid.setStatus(_A)
class _A200DigitMapSrvType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('h248',0),('selfchange',1),('sip',2),('urgencymap',3),('callEscape',4)))
_A200DigitMapSrvType_Type.__name__=_B
_A200DigitMapSrvType_Object=MibTableColumn
a200DigitMapSrvType=_A200DigitMapSrvType_Object((1,3,6,1,4,1,3902,1015,5200,3,1,8,1,3),_A200DigitMapSrvType_Type())
a200DigitMapSrvType.setMaxAccess(_D)
if mibBuilder.loadTexts:a200DigitMapSrvType.setStatus(_A)
class _A200DigitMapDgtName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,20))
_A200DigitMapDgtName_Type.__name__=_L
_A200DigitMapDgtName_Object=MibTableColumn
a200DigitMapDgtName=_A200DigitMapDgtName_Object((1,3,6,1,4,1,3902,1015,5200,3,1,8,1,4),_A200DigitMapDgtName_Type())
a200DigitMapDgtName.setMaxAccess(_D)
if mibBuilder.loadTexts:a200DigitMapDgtName.setStatus(_A)
class _A200DigitMapDgtMap_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,250))
_A200DigitMapDgtMap_Type.__name__=_L
_A200DigitMapDgtMap_Object=MibTableColumn
a200DigitMapDgtMap=_A200DigitMapDgtMap_Object((1,3,6,1,4,1,3902,1015,5200,3,1,8,1,5),_A200DigitMapDgtMap_Type())
a200DigitMapDgtMap.setMaxAccess(_D)
if mibBuilder.loadTexts:a200DigitMapDgtMap.setStatus(_A)
_A200DigitMapRowStatus_Type=RowStatus
_A200DigitMapRowStatus_Object=MibTableColumn
a200DigitMapRowStatus=_A200DigitMapRowStatus_Object((1,3,6,1,4,1,3902,1015,5200,3,1,8,1,6),_A200DigitMapRowStatus_Type())
a200DigitMapRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:a200DigitMapRowStatus.setStatus(_A)
_A200VoipRouteTable_Object=MibTable
a200VoipRouteTable=_A200VoipRouteTable_Object((1,3,6,1,4,1,3902,1015,5200,3,1,10))
if mibBuilder.loadTexts:a200VoipRouteTable.setStatus(_A)
_A200VoipRouteEntry_Object=MibTableRow
a200VoipRouteEntry=_A200VoipRouteEntry_Object((1,3,6,1,4,1,3902,1015,5200,3,1,10,1))
a200VoipRouteEntry.setIndexNames((0,_C,_AG),(0,_C,_AH),(0,_C,_AI))
if mibBuilder.loadTexts:a200VoipRouteEntry.setStatus(_A)
class _A200VoipRouteMgId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_A200VoipRouteMgId_Type.__name__=_B
_A200VoipRouteMgId_Object=MibTableColumn
a200VoipRouteMgId=_A200VoipRouteMgId_Object((1,3,6,1,4,1,3902,1015,5200,3,1,10,1,1),_A200VoipRouteMgId_Type())
a200VoipRouteMgId.setMaxAccess(_G)
if mibBuilder.loadTexts:a200VoipRouteMgId.setStatus(_A)
class _A200VoipRouteType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('media',1),('ctrl',2)))
_A200VoipRouteType_Type.__name__=_B
_A200VoipRouteType_Object=MibTableColumn
a200VoipRouteType=_A200VoipRouteType_Object((1,3,6,1,4,1,3902,1015,5200,3,1,10,1,2),_A200VoipRouteType_Type())
a200VoipRouteType.setMaxAccess(_G)
if mibBuilder.loadTexts:a200VoipRouteType.setStatus(_A)
_A200VoipRouteDestIp_Type=IpAddress
_A200VoipRouteDestIp_Object=MibTableColumn
a200VoipRouteDestIp=_A200VoipRouteDestIp_Object((1,3,6,1,4,1,3902,1015,5200,3,1,10,1,3),_A200VoipRouteDestIp_Type())
a200VoipRouteDestIp.setMaxAccess(_G)
if mibBuilder.loadTexts:a200VoipRouteDestIp.setStatus(_A)
_A200VoipRouteDestMask_Type=IpAddress
_A200VoipRouteDestMask_Object=MibTableColumn
a200VoipRouteDestMask=_A200VoipRouteDestMask_Object((1,3,6,1,4,1,3902,1015,5200,3,1,10,1,4),_A200VoipRouteDestMask_Type())
a200VoipRouteDestMask.setMaxAccess(_D)
if mibBuilder.loadTexts:a200VoipRouteDestMask.setStatus(_A)
_A200VoipRouteNexthop_Type=IpAddress
_A200VoipRouteNexthop_Object=MibTableColumn
a200VoipRouteNexthop=_A200VoipRouteNexthop_Object((1,3,6,1,4,1,3902,1015,5200,3,1,10,1,5),_A200VoipRouteNexthop_Type())
a200VoipRouteNexthop.setMaxAccess(_D)
if mibBuilder.loadTexts:a200VoipRouteNexthop.setStatus(_A)
_A200VoipRouteNexthopMac_Type=MacAddress
_A200VoipRouteNexthopMac_Object=MibTableColumn
a200VoipRouteNexthopMac=_A200VoipRouteNexthopMac_Object((1,3,6,1,4,1,3902,1015,5200,3,1,10,1,6),_A200VoipRouteNexthopMac_Type())
a200VoipRouteNexthopMac.setMaxAccess(_D)
if mibBuilder.loadTexts:a200VoipRouteNexthopMac.setStatus(_A)
class _A200VoipRouteArpTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,720))
_A200VoipRouteArpTime_Type.__name__=_B
_A200VoipRouteArpTime_Object=MibTableColumn
a200VoipRouteArpTime=_A200VoipRouteArpTime_Object((1,3,6,1,4,1,3902,1015,5200,3,1,10,1,7),_A200VoipRouteArpTime_Type())
a200VoipRouteArpTime.setMaxAccess(_D)
if mibBuilder.loadTexts:a200VoipRouteArpTime.setStatus(_A)
_A200VoipRouteRowStatus_Type=RowStatus
_A200VoipRouteRowStatus_Object=MibTableColumn
a200VoipRouteRowStatus=_A200VoipRouteRowStatus_Object((1,3,6,1,4,1,3902,1015,5200,3,1,10,1,20),_A200VoipRouteRowStatus_Type())
a200VoipRouteRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:a200VoipRouteRowStatus.setStatus(_A)
_A200CtlPortTable_Object=MibTable
a200CtlPortTable=_A200CtlPortTable_Object((1,3,6,1,4,1,3902,1015,5200,3,1,11))
if mibBuilder.loadTexts:a200CtlPortTable.setStatus(_A)
_A200CtlPortEntry_Object=MibTableRow
a200CtlPortEntry=_A200CtlPortEntry_Object((1,3,6,1,4,1,3902,1015,5200,3,1,11,1))
a200CtlPortEntry.setIndexNames((0,_C,_AJ))
if mibBuilder.loadTexts:a200CtlPortEntry.setStatus(_A)
class _A200CtlPortCtlId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,40))
_A200CtlPortCtlId_Type.__name__=_B
_A200CtlPortCtlId_Object=MibTableColumn
a200CtlPortCtlId=_A200CtlPortCtlId_Object((1,3,6,1,4,1,3902,1015,5200,3,1,11,1,1),_A200CtlPortCtlId_Type())
a200CtlPortCtlId.setMaxAccess(_G)
if mibBuilder.loadTexts:a200CtlPortCtlId.setStatus(_A)
class _A200CtlPortInfo_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('udp',0),('tcp',1)))
_A200CtlPortInfo_Type.__name__=_B
_A200CtlPortInfo_Object=MibTableColumn
a200CtlPortInfo=_A200CtlPortInfo_Object((1,3,6,1,4,1,3902,1015,5200,3,1,11,1,2),_A200CtlPortInfo_Type())
a200CtlPortInfo.setMaxAccess(_D)
if mibBuilder.loadTexts:a200CtlPortInfo.setStatus(_A)
class _A200CtlPortUdpPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_A200CtlPortUdpPort_Type.__name__=_B
_A200CtlPortUdpPort_Object=MibTableColumn
a200CtlPortUdpPort=_A200CtlPortUdpPort_Object((1,3,6,1,4,1,3902,1015,5200,3,1,11,1,3),_A200CtlPortUdpPort_Type())
a200CtlPortUdpPort.setMaxAccess(_D)
if mibBuilder.loadTexts:a200CtlPortUdpPort.setStatus(_A)
_A200CtlPortRowStatus_Type=RowStatus
_A200CtlPortRowStatus_Object=MibTableColumn
a200CtlPortRowStatus=_A200CtlPortRowStatus_Object((1,3,6,1,4,1,3902,1015,5200,3,1,11,1,4),_A200CtlPortRowStatus_Type())
a200CtlPortRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:a200CtlPortRowStatus.setStatus(_A)
_CallOptimizeTable_Object=MibTable
callOptimizeTable=_CallOptimizeTable_Object((1,3,6,1,4,1,3902,1015,5200,3,1,13))
if mibBuilder.loadTexts:callOptimizeTable.setStatus(_A)
_CallOptimizeEntry_Object=MibTableRow
callOptimizeEntry=_CallOptimizeEntry_Object((1,3,6,1,4,1,3902,1015,5200,3,1,13,1))
callOptimizeEntry.setIndexNames((0,_C,_AK))
if mibBuilder.loadTexts:callOptimizeEntry.setStatus(_A)
class _CalloptIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_CalloptIndex_Type.__name__=_B
_CalloptIndex_Object=MibTableColumn
calloptIndex=_CalloptIndex_Object((1,3,6,1,4,1,3902,1015,5200,3,1,13,1,1),_CalloptIndex_Type())
calloptIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:calloptIndex.setStatus(_A)
class _CalloptOpenMsgAck_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_b,1),(_c,2)))
_CalloptOpenMsgAck_Type.__name__=_B
_CalloptOpenMsgAck_Object=MibTableColumn
calloptOpenMsgAck=_CalloptOpenMsgAck_Object((1,3,6,1,4,1,3902,1015,5200,3,1,13,1,2),_CalloptOpenMsgAck_Type())
calloptOpenMsgAck.setMaxAccess(_E)
if mibBuilder.loadTexts:calloptOpenMsgAck.setStatus(_A)
class _CalloptPlayToneAck_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_b,1),(_c,2)))
_CalloptPlayToneAck_Type.__name__=_B
_CalloptPlayToneAck_Object=MibTableColumn
calloptPlayToneAck=_CalloptPlayToneAck_Object((1,3,6,1,4,1,3902,1015,5200,3,1,13,1,3),_CalloptPlayToneAck_Type())
calloptPlayToneAck.setMaxAccess(_E)
if mibBuilder.loadTexts:calloptPlayToneAck.setStatus(_A)
class _CalloptSubPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('higher',1),('nothigher',2)))
_CalloptSubPriority_Type.__name__=_B
_CalloptSubPriority_Object=MibTableColumn
calloptSubPriority=_CalloptSubPriority_Object((1,3,6,1,4,1,3902,1015,5200,3,1,13,1,4),_CalloptSubPriority_Type())
calloptSubPriority.setMaxAccess(_E)
if mibBuilder.loadTexts:calloptSubPriority.setStatus(_A)
class _CalloptNumMax_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_CalloptNumMax_Type.__name__=_B
_CalloptNumMax_Object=MibTableColumn
calloptNumMax=_CalloptNumMax_Object((1,3,6,1,4,1,3902,1015,5200,3,1,13,1,5),_CalloptNumMax_Type())
calloptNumMax.setMaxAccess(_E)
if mibBuilder.loadTexts:calloptNumMax.setStatus(_A)
class _CalloptH248MsgAck_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_b,1),(_c,2)))
_CalloptH248MsgAck_Type.__name__=_B
_CalloptH248MsgAck_Object=MibTableColumn
calloptH248MsgAck=_CalloptH248MsgAck_Object((1,3,6,1,4,1,3902,1015,5200,3,1,13,1,6),_CalloptH248MsgAck_Type())
calloptH248MsgAck.setMaxAccess(_E)
if mibBuilder.loadTexts:calloptH248MsgAck.setStatus(_A)
class _CalloptH248MsgPn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_b,1),(_c,2)))
_CalloptH248MsgPn_Type.__name__=_B
_CalloptH248MsgPn_Object=MibTableColumn
calloptH248MsgPn=_CalloptH248MsgPn_Object((1,3,6,1,4,1,3902,1015,5200,3,1,13,1,7),_CalloptH248MsgPn_Type())
calloptH248MsgPn.setMaxAccess(_E)
if mibBuilder.loadTexts:calloptH248MsgPn.setStatus(_A)
class _CalloptH248Statistic_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_b,1),(_c,2)))
_CalloptH248Statistic_Type.__name__=_B
_CalloptH248Statistic_Object=MibTableColumn
calloptH248Statistic=_CalloptH248Statistic_Object((1,3,6,1,4,1,3902,1015,5200,3,1,13,1,8),_CalloptH248Statistic_Type())
calloptH248Statistic.setMaxAccess(_E)
if mibBuilder.loadTexts:calloptH248Statistic.setStatus(_A)
class _CalloptH248HookOffEvent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Z,1),(_a,2)))
_CalloptH248HookOffEvent_Type.__name__=_B
_CalloptH248HookOffEvent_Object=MibTableColumn
calloptH248HookOffEvent=_CalloptH248HookOffEvent_Object((1,3,6,1,4,1,3902,1015,5200,3,1,13,1,9),_CalloptH248HookOffEvent_Type())
calloptH248HookOffEvent.setMaxAccess(_E)
if mibBuilder.loadTexts:calloptH248HookOffEvent.setStatus(_A)
class _CalloptH248HookOnEvent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Z,1),(_a,2)))
_CalloptH248HookOnEvent_Type.__name__=_B
_CalloptH248HookOnEvent_Object=MibTableColumn
calloptH248HookOnEvent=_CalloptH248HookOnEvent_Object((1,3,6,1,4,1,3902,1015,5200,3,1,13,1,10),_CalloptH248HookOnEvent_Type())
calloptH248HookOnEvent.setMaxAccess(_E)
if mibBuilder.loadTexts:calloptH248HookOnEvent.setStatus(_A)
class _CalloptServiceAbnormal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Z,1),(_a,2)))
_CalloptServiceAbnormal_Type.__name__=_B
_CalloptServiceAbnormal_Object=MibTableColumn
calloptServiceAbnormal=_CalloptServiceAbnormal_Object((1,3,6,1,4,1,3902,1015,5200,3,1,13,1,11),_CalloptServiceAbnormal_Type())
calloptServiceAbnormal.setMaxAccess(_E)
if mibBuilder.loadTexts:calloptServiceAbnormal.setStatus(_A)
class _CalloptMgProtocolErr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Z,1),(_a,2)))
_CalloptMgProtocolErr_Type.__name__=_B
_CalloptMgProtocolErr_Object=MibTableColumn
calloptMgProtocolErr=_CalloptMgProtocolErr_Object((1,3,6,1,4,1,3902,1015,5200,3,1,13,1,12),_CalloptMgProtocolErr_Type())
calloptMgProtocolErr.setMaxAccess(_E)
if mibBuilder.loadTexts:calloptMgProtocolErr.setStatus(_A)
class _CalloptMgcProtocolErr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Z,1),(_a,2)))
_CalloptMgcProtocolErr_Type.__name__=_B
_CalloptMgcProtocolErr_Object=MibTableColumn
calloptMgcProtocolErr=_CalloptMgcProtocolErr_Object((1,3,6,1,4,1,3902,1015,5200,3,1,13,1,13),_CalloptMgcProtocolErr_Type())
calloptMgcProtocolErr.setMaxAccess(_E)
if mibBuilder.loadTexts:calloptMgcProtocolErr.setStatus(_A)
class _CalloptMgInsideErr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Z,1),(_a,2)))
_CalloptMgInsideErr_Type.__name__=_B
_CalloptMgInsideErr_Object=MibTableColumn
calloptMgInsideErr=_CalloptMgInsideErr_Object((1,3,6,1,4,1,3902,1015,5200,3,1,13,1,14),_CalloptMgInsideErr_Type())
calloptMgInsideErr.setMaxAccess(_E)
if mibBuilder.loadTexts:calloptMgInsideErr.setStatus(_A)
class _CalloptHookOffLimiteCycle_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,600))
_CalloptHookOffLimiteCycle_Type.__name__=_B
_CalloptHookOffLimiteCycle_Object=MibTableColumn
calloptHookOffLimiteCycle=_CalloptHookOffLimiteCycle_Object((1,3,6,1,4,1,3902,1015,5200,3,1,13,1,15),_CalloptHookOffLimiteCycle_Type())
calloptHookOffLimiteCycle.setMaxAccess(_E)
if mibBuilder.loadTexts:calloptHookOffLimiteCycle.setStatus(_A)
class _CalloptHookOffLimiteBlock_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(15,600))
_CalloptHookOffLimiteBlock_Type.__name__=_B
_CalloptHookOffLimiteBlock_Object=MibTableColumn
calloptHookOffLimiteBlock=_CalloptHookOffLimiteBlock_Object((1,3,6,1,4,1,3902,1015,5200,3,1,13,1,16),_CalloptHookOffLimiteBlock_Type())
calloptHookOffLimiteBlock.setMaxAccess(_E)
if mibBuilder.loadTexts:calloptHookOffLimiteBlock.setStatus(_A)
class _CalloptHookOffLimiteUnblock_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(12,600))
_CalloptHookOffLimiteUnblock_Type.__name__=_B
_CalloptHookOffLimiteUnblock_Object=MibTableColumn
calloptHookOffLimiteUnblock=_CalloptHookOffLimiteUnblock_Object((1,3,6,1,4,1,3902,1015,5200,3,1,13,1,17),_CalloptHookOffLimiteUnblock_Type())
calloptHookOffLimiteUnblock.setMaxAccess(_E)
if mibBuilder.loadTexts:calloptHookOffLimiteUnblock.setStatus(_A)
class _CalloptMgcCallWaitTone_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('breakdown',1),('notbreakdown',2)))
_CalloptMgcCallWaitTone_Type.__name__=_B
_CalloptMgcCallWaitTone_Object=MibTableColumn
calloptMgcCallWaitTone=_CalloptMgcCallWaitTone_Object((1,3,6,1,4,1,3902,1015,5200,3,1,13,1,18),_CalloptMgcCallWaitTone_Type())
calloptMgcCallWaitTone.setMaxAccess(_E)
if mibBuilder.loadTexts:calloptMgcCallWaitTone.setStatus(_A)
class _CalloptToneArea_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22)));namedValues=NamedValues(*(('mainland',1),('hongkong',2),('singapore',3),('russia',4),('chile',5),('dominican',6),('argentina',7),('croatia',8),('turkey',9),('singapore2',10),('malaysia',11),('belgium',12),('india',13),('taiwan',14),('srilanka',15),('austria',16),('greece',17),('nepal',18),('colombia',19),('peru',20),('morocco',21),('hungary',22)))
_CalloptToneArea_Type.__name__=_B
_CalloptToneArea_Object=MibTableColumn
calloptToneArea=_CalloptToneArea_Object((1,3,6,1,4,1,3902,1015,5200,3,1,13,1,19),_CalloptToneArea_Type())
calloptToneArea.setMaxAccess(_E)
if mibBuilder.loadTexts:calloptToneArea.setStatus(_A)
class _CalloptH248LinkBreakTone_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_i,1),('informationTone',2)))
_CalloptH248LinkBreakTone_Type.__name__=_B
_CalloptH248LinkBreakTone_Object=MibTableColumn
calloptH248LinkBreakTone=_CalloptH248LinkBreakTone_Object((1,3,6,1,4,1,3902,1015,5200,3,1,13,1,20),_CalloptH248LinkBreakTone_Type())
calloptH248LinkBreakTone.setMaxAccess(_E)
if mibBuilder.loadTexts:calloptH248LinkBreakTone.setStatus(_A)
class _MsagLoadDefaultRingProfile_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_MsagLoadDefaultRingProfile_Type.__name__=_B
_MsagLoadDefaultRingProfile_Object=MibScalar
msagLoadDefaultRingProfile=_MsagLoadDefaultRingProfile_Object((1,3,6,1,4,1,3902,1015,5200,3,1,14),_MsagLoadDefaultRingProfile_Type())
msagLoadDefaultRingProfile.setMaxAccess(_E)
if mibBuilder.loadTexts:msagLoadDefaultRingProfile.setStatus(_A)
_ZxAnVoipInterfaceTable_Object=MibTable
zxAnVoipInterfaceTable=_ZxAnVoipInterfaceTable_Object((1,3,6,1,4,1,3902,1015,5200,3,1,15))
if mibBuilder.loadTexts:zxAnVoipInterfaceTable.setStatus(_A)
_ZxAnVoipInterfaceEntry_Object=MibTableRow
zxAnVoipInterfaceEntry=_ZxAnVoipInterfaceEntry_Object((1,3,6,1,4,1,3902,1015,5200,3,1,15,1))
zxAnVoipInterfaceEntry.setIndexNames((0,_C,'zxAnMgId'))
if mibBuilder.loadTexts:zxAnVoipInterfaceEntry.setStatus(_A)
class _ZxAnMgId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_ZxAnMgId_Type.__name__=_B
_ZxAnMgId_Object=MibTableColumn
zxAnMgId=_ZxAnMgId_Object((1,3,6,1,4,1,3902,1015,5200,3,1,15,1,1),_ZxAnMgId_Type())
zxAnMgId.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnMgId.setStatus(_A)
_ZxAnVoipCtrlIpAddr_Type=IpAddress
_ZxAnVoipCtrlIpAddr_Object=MibTableColumn
zxAnVoipCtrlIpAddr=_ZxAnVoipCtrlIpAddr_Object((1,3,6,1,4,1,3902,1015,5200,3,1,15,1,2),_ZxAnVoipCtrlIpAddr_Type())
zxAnVoipCtrlIpAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnVoipCtrlIpAddr.setStatus(_A)
_ZxAnVoipCtrlIpMask_Type=IpAddress
_ZxAnVoipCtrlIpMask_Object=MibTableColumn
zxAnVoipCtrlIpMask=_ZxAnVoipCtrlIpMask_Object((1,3,6,1,4,1,3902,1015,5200,3,1,15,1,3),_ZxAnVoipCtrlIpMask_Type())
zxAnVoipCtrlIpMask.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnVoipCtrlIpMask.setStatus(_A)
_ZxAnVoipMediaIpaddr_Type=IpAddress
_ZxAnVoipMediaIpaddr_Object=MibTableColumn
zxAnVoipMediaIpaddr=_ZxAnVoipMediaIpaddr_Object((1,3,6,1,4,1,3902,1015,5200,3,1,15,1,4),_ZxAnVoipMediaIpaddr_Type())
zxAnVoipMediaIpaddr.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnVoipMediaIpaddr.setStatus(_A)
_ZxAnVoipMediaIpMask_Type=IpAddress
_ZxAnVoipMediaIpMask_Object=MibTableColumn
zxAnVoipMediaIpMask=_ZxAnVoipMediaIpMask_Object((1,3,6,1,4,1,3902,1015,5200,3,1,15,1,5),_ZxAnVoipMediaIpMask_Type())
zxAnVoipMediaIpMask.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnVoipMediaIpMask.setStatus(_A)
_ZxAnVoipInterfaceRowStatus_Type=RowStatus
_ZxAnVoipInterfaceRowStatus_Object=MibTableColumn
zxAnVoipInterfaceRowStatus=_ZxAnVoipInterfaceRowStatus_Object((1,3,6,1,4,1,3902,1015,5200,3,1,15,1,20),_ZxAnVoipInterfaceRowStatus_Type())
zxAnVoipInterfaceRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnVoipInterfaceRowStatus.setStatus(_A)
_ZxAnVoipBaseGlobalObjects_ObjectIdentity=ObjectIdentity
zxAnVoipBaseGlobalObjects=_ZxAnVoipBaseGlobalObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,5200,3,1,17))
class _ZxAnVoipBaseCapabilities_Type(Bits):namedValues=NamedValues(*(('externalSelfswitch',0),('slcFeedCurrent',1),('slcHighImpedance',2),('callerTestMode',3),('callEscapeMode',4)))
_ZxAnVoipBaseCapabilities_Type.__name__='Bits'
_ZxAnVoipBaseCapabilities_Object=MibScalar
zxAnVoipBaseCapabilities=_ZxAnVoipBaseCapabilities_Object((1,3,6,1,4,1,3902,1015,5200,3,1,17,1),_ZxAnVoipBaseCapabilities_Type())
zxAnVoipBaseCapabilities.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnVoipBaseCapabilities.setStatus(_A)
_ZxAnSelfswitchTktObjects_ObjectIdentity=ObjectIdentity
zxAnSelfswitchTktObjects=_ZxAnSelfswitchTktObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,5200,3,1,17,2))
class _ZxAnSelfswitchTktEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_M,2)))
_ZxAnSelfswitchTktEnable_Type.__name__=_B
_ZxAnSelfswitchTktEnable_Object=MibScalar
zxAnSelfswitchTktEnable=_ZxAnSelfswitchTktEnable_Object((1,3,6,1,4,1,3902,1015,5200,3,1,17,2,1),_ZxAnSelfswitchTktEnable_Type())
zxAnSelfswitchTktEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnSelfswitchTktEnable.setStatus(_A)
class _ZxAnSelfswitchTktUploadInterval_Type(Integer32):defaultValue=1440;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,44640))
_ZxAnSelfswitchTktUploadInterval_Type.__name__=_B
_ZxAnSelfswitchTktUploadInterval_Object=MibScalar
zxAnSelfswitchTktUploadInterval=_ZxAnSelfswitchTktUploadInterval_Object((1,3,6,1,4,1,3902,1015,5200,3,1,17,2,2),_ZxAnSelfswitchTktUploadInterval_Type())
zxAnSelfswitchTktUploadInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnSelfswitchTktUploadInterval.setStatus(_A)
if mibBuilder.loadTexts:zxAnSelfswitchTktUploadInterval.setUnits('minute')
class _ZxAnSelfswitchTktSizeThreshold_Type(Integer32):defaultValue=80;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_ZxAnSelfswitchTktSizeThreshold_Type.__name__=_B
_ZxAnSelfswitchTktSizeThreshold_Object=MibScalar
zxAnSelfswitchTktSizeThreshold=_ZxAnSelfswitchTktSizeThreshold_Object((1,3,6,1,4,1,3902,1015,5200,3,1,17,2,3),_ZxAnSelfswitchTktSizeThreshold_Type())
zxAnSelfswitchTktSizeThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnSelfswitchTktSizeThreshold.setStatus(_A)
if mibBuilder.loadTexts:zxAnSelfswitchTktSizeThreshold.setUnits(_g)
_ZxAnSelfswitchTelLoadObjects_ObjectIdentity=ObjectIdentity
zxAnSelfswitchTelLoadObjects=_ZxAnSelfswitchTelLoadObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,5200,3,1,17,3))
class _ZxAnSelfswitchTelLoadFileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ZxAnSelfswitchTelLoadFileName_Type.__name__=_L
_ZxAnSelfswitchTelLoadFileName_Object=MibScalar
zxAnSelfswitchTelLoadFileName=_ZxAnSelfswitchTelLoadFileName_Object((1,3,6,1,4,1,3902,1015,5200,3,1,17,3,1),_ZxAnSelfswitchTelLoadFileName_Type())
zxAnSelfswitchTelLoadFileName.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnSelfswitchTelLoadFileName.setStatus(_A)
class _ZxAnSelfswitchTelLoadStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_j,1),(_k,2),(_l,3),(_m,4)))
_ZxAnSelfswitchTelLoadStatus_Type.__name__=_B
_ZxAnSelfswitchTelLoadStatus_Object=MibScalar
zxAnSelfswitchTelLoadStatus=_ZxAnSelfswitchTelLoadStatus_Object((1,3,6,1,4,1,3902,1015,5200,3,1,17,3,2),_ZxAnSelfswitchTelLoadStatus_Type())
zxAnSelfswitchTelLoadStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnSelfswitchTelLoadStatus.setStatus(_A)
class _ZxAnSelfswitchTelLoadFailReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,255)));namedValues=NamedValues(*(('noError',1),('badFile',2),('noTelOfSelfNe',3),('otherErrors',255)))
_ZxAnSelfswitchTelLoadFailReason_Type.__name__=_B
_ZxAnSelfswitchTelLoadFailReason_Object=MibScalar
zxAnSelfswitchTelLoadFailReason=_ZxAnSelfswitchTelLoadFailReason_Object((1,3,6,1,4,1,3902,1015,5200,3,1,17,3,3),_ZxAnSelfswitchTelLoadFailReason_Type())
zxAnSelfswitchTelLoadFailReason.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnSelfswitchTelLoadFailReason.setStatus(_A)
class _ZxAnVoicePortLockoutTrapEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_ZxAnVoicePortLockoutTrapEnable_Type.__name__=_B
_ZxAnVoicePortLockoutTrapEnable_Object=MibScalar
zxAnVoicePortLockoutTrapEnable=_ZxAnVoicePortLockoutTrapEnable_Object((1,3,6,1,4,1,3902,1015,5200,3,1,17,4),_ZxAnVoicePortLockoutTrapEnable_Type())
zxAnVoicePortLockoutTrapEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnVoicePortLockoutTrapEnable.setStatus(_A)
_ZxAnSelfswitchTktFtpTable_Object=MibTable
zxAnSelfswitchTktFtpTable=_ZxAnSelfswitchTktFtpTable_Object((1,3,6,1,4,1,3902,1015,5200,3,1,18))
if mibBuilder.loadTexts:zxAnSelfswitchTktFtpTable.setStatus(_A)
_ZxAnSelfswitchTktFtpEntry_Object=MibTableRow
zxAnSelfswitchTktFtpEntry=_ZxAnSelfswitchTktFtpEntry_Object((1,3,6,1,4,1,3902,1015,5200,3,1,18,1))
zxAnSelfswitchTktFtpEntry.setIndexNames((0,_C,_AL))
if mibBuilder.loadTexts:zxAnSelfswitchTktFtpEntry.setStatus(_A)
class _ZxAnSelfswitchTktFtpServerId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_ZxAnSelfswitchTktFtpServerId_Type.__name__=_B
_ZxAnSelfswitchTktFtpServerId_Object=MibTableColumn
zxAnSelfswitchTktFtpServerId=_ZxAnSelfswitchTktFtpServerId_Object((1,3,6,1,4,1,3902,1015,5200,3,1,18,1,1),_ZxAnSelfswitchTktFtpServerId_Type())
zxAnSelfswitchTktFtpServerId.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnSelfswitchTktFtpServerId.setStatus(_A)
_ZxAnSelfswitchTktFtpServerIpType_Type=InetAddressType
_ZxAnSelfswitchTktFtpServerIpType_Object=MibTableColumn
zxAnSelfswitchTktFtpServerIpType=_ZxAnSelfswitchTktFtpServerIpType_Object((1,3,6,1,4,1,3902,1015,5200,3,1,18,1,2),_ZxAnSelfswitchTktFtpServerIpType_Type())
zxAnSelfswitchTktFtpServerIpType.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnSelfswitchTktFtpServerIpType.setStatus(_A)
_ZxAnSelfswitchTktFtpServerIp_Type=InetAddress
_ZxAnSelfswitchTktFtpServerIp_Object=MibTableColumn
zxAnSelfswitchTktFtpServerIp=_ZxAnSelfswitchTktFtpServerIp_Object((1,3,6,1,4,1,3902,1015,5200,3,1,18,1,3),_ZxAnSelfswitchTktFtpServerIp_Type())
zxAnSelfswitchTktFtpServerIp.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnSelfswitchTktFtpServerIp.setStatus(_A)
class _ZxAnSelfswitchTktFtpUserName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ZxAnSelfswitchTktFtpUserName_Type.__name__=_L
_ZxAnSelfswitchTktFtpUserName_Object=MibTableColumn
zxAnSelfswitchTktFtpUserName=_ZxAnSelfswitchTktFtpUserName_Object((1,3,6,1,4,1,3902,1015,5200,3,1,18,1,4),_ZxAnSelfswitchTktFtpUserName_Type())
zxAnSelfswitchTktFtpUserName.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnSelfswitchTktFtpUserName.setStatus(_A)
class _ZxAnSelfswitchTktFtpUserPwd_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ZxAnSelfswitchTktFtpUserPwd_Type.__name__=_L
_ZxAnSelfswitchTktFtpUserPwd_Object=MibTableColumn
zxAnSelfswitchTktFtpUserPwd=_ZxAnSelfswitchTktFtpUserPwd_Object((1,3,6,1,4,1,3902,1015,5200,3,1,18,1,5),_ZxAnSelfswitchTktFtpUserPwd_Type())
zxAnSelfswitchTktFtpUserPwd.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnSelfswitchTktFtpUserPwd.setStatus(_A)
class _ZxAnSelfswitchTktFtpServerPath_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_ZxAnSelfswitchTktFtpServerPath_Type.__name__=_L
_ZxAnSelfswitchTktFtpServerPath_Object=MibTableColumn
zxAnSelfswitchTktFtpServerPath=_ZxAnSelfswitchTktFtpServerPath_Object((1,3,6,1,4,1,3902,1015,5200,3,1,18,1,6),_ZxAnSelfswitchTktFtpServerPath_Type())
zxAnSelfswitchTktFtpServerPath.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnSelfswitchTktFtpServerPath.setStatus(_A)
_ZxAnSelfswitchTktFtpRowStatus_Type=RowStatus
_ZxAnSelfswitchTktFtpRowStatus_Object=MibTableColumn
zxAnSelfswitchTktFtpRowStatus=_ZxAnSelfswitchTktFtpRowStatus_Object((1,3,6,1,4,1,3902,1015,5200,3,1,18,1,20),_ZxAnSelfswitchTktFtpRowStatus_Type())
zxAnSelfswitchTktFtpRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnSelfswitchTktFtpRowStatus.setStatus(_A)
_ZxAnDsx1ProtectionGroupTable_Object=MibTable
zxAnDsx1ProtectionGroupTable=_ZxAnDsx1ProtectionGroupTable_Object((1,3,6,1,4,1,3902,1015,5200,3,1,19))
if mibBuilder.loadTexts:zxAnDsx1ProtectionGroupTable.setStatus(_A)
_ZxAnDsx1ProtectionGroupEntry_Object=MibTableRow
zxAnDsx1ProtectionGroupEntry=_ZxAnDsx1ProtectionGroupEntry_Object((1,3,6,1,4,1,3902,1015,5200,3,1,19,1))
zxAnDsx1ProtectionGroupEntry.setIndexNames((0,_C,_AM))
if mibBuilder.loadTexts:zxAnDsx1ProtectionGroupEntry.setStatus(_A)
class _ZxAnDsx1ProtectionGroupId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,48))
_ZxAnDsx1ProtectionGroupId_Type.__name__=_B
_ZxAnDsx1ProtectionGroupId_Object=MibTableColumn
zxAnDsx1ProtectionGroupId=_ZxAnDsx1ProtectionGroupId_Object((1,3,6,1,4,1,3902,1015,5200,3,1,19,1,1),_ZxAnDsx1ProtectionGroupId_Type())
zxAnDsx1ProtectionGroupId.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnDsx1ProtectionGroupId.setStatus(_A)
class _ZxAnDsx1ProtectionGroupName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ZxAnDsx1ProtectionGroupName_Type.__name__=_L
_ZxAnDsx1ProtectionGroupName_Object=MibTableColumn
zxAnDsx1ProtectionGroupName=_ZxAnDsx1ProtectionGroupName_Object((1,3,6,1,4,1,3902,1015,5200,3,1,19,1,2),_ZxAnDsx1ProtectionGroupName_Type())
zxAnDsx1ProtectionGroupName.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnDsx1ProtectionGroupName.setStatus(_A)
_ZxAnDsx1MasterDsx1Rack_Type=Integer32
_ZxAnDsx1MasterDsx1Rack_Object=MibTableColumn
zxAnDsx1MasterDsx1Rack=_ZxAnDsx1MasterDsx1Rack_Object((1,3,6,1,4,1,3902,1015,5200,3,1,19,1,3),_ZxAnDsx1MasterDsx1Rack_Type())
zxAnDsx1MasterDsx1Rack.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnDsx1MasterDsx1Rack.setStatus(_A)
_ZxAnDsx1MasterDsx1Shelf_Type=Integer32
_ZxAnDsx1MasterDsx1Shelf_Object=MibTableColumn
zxAnDsx1MasterDsx1Shelf=_ZxAnDsx1MasterDsx1Shelf_Object((1,3,6,1,4,1,3902,1015,5200,3,1,19,1,4),_ZxAnDsx1MasterDsx1Shelf_Type())
zxAnDsx1MasterDsx1Shelf.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnDsx1MasterDsx1Shelf.setStatus(_A)
_ZxAnDsx1MasterDsx1Slot_Type=Integer32
_ZxAnDsx1MasterDsx1Slot_Object=MibTableColumn
zxAnDsx1MasterDsx1Slot=_ZxAnDsx1MasterDsx1Slot_Object((1,3,6,1,4,1,3902,1015,5200,3,1,19,1,5),_ZxAnDsx1MasterDsx1Slot_Type())
zxAnDsx1MasterDsx1Slot.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnDsx1MasterDsx1Slot.setStatus(_A)
_ZxAnDsx1MasterDsx1LinkNo_Type=Integer32
_ZxAnDsx1MasterDsx1LinkNo_Object=MibTableColumn
zxAnDsx1MasterDsx1LinkNo=_ZxAnDsx1MasterDsx1LinkNo_Object((1,3,6,1,4,1,3902,1015,5200,3,1,19,1,6),_ZxAnDsx1MasterDsx1LinkNo_Type())
zxAnDsx1MasterDsx1LinkNo.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnDsx1MasterDsx1LinkNo.setStatus(_A)
_ZxAnDsx1StandbyDsx1Rack_Type=Integer32
_ZxAnDsx1StandbyDsx1Rack_Object=MibTableColumn
zxAnDsx1StandbyDsx1Rack=_ZxAnDsx1StandbyDsx1Rack_Object((1,3,6,1,4,1,3902,1015,5200,3,1,19,1,7),_ZxAnDsx1StandbyDsx1Rack_Type())
zxAnDsx1StandbyDsx1Rack.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnDsx1StandbyDsx1Rack.setStatus(_A)
_ZxAnDsx1StandbyDsx1Shelf_Type=Integer32
_ZxAnDsx1StandbyDsx1Shelf_Object=MibTableColumn
zxAnDsx1StandbyDsx1Shelf=_ZxAnDsx1StandbyDsx1Shelf_Object((1,3,6,1,4,1,3902,1015,5200,3,1,19,1,8),_ZxAnDsx1StandbyDsx1Shelf_Type())
zxAnDsx1StandbyDsx1Shelf.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnDsx1StandbyDsx1Shelf.setStatus(_A)
_ZxAnDsx1StandbyDsx1Slot_Type=Integer32
_ZxAnDsx1StandbyDsx1Slot_Object=MibTableColumn
zxAnDsx1StandbyDsx1Slot=_ZxAnDsx1StandbyDsx1Slot_Object((1,3,6,1,4,1,3902,1015,5200,3,1,19,1,9),_ZxAnDsx1StandbyDsx1Slot_Type())
zxAnDsx1StandbyDsx1Slot.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnDsx1StandbyDsx1Slot.setStatus(_A)
_ZxAnDsx1StandbyDsx1LinkNo_Type=Integer32
_ZxAnDsx1StandbyDsx1LinkNo_Object=MibTableColumn
zxAnDsx1StandbyDsx1LinkNo=_ZxAnDsx1StandbyDsx1LinkNo_Object((1,3,6,1,4,1,3902,1015,5200,3,1,19,1,10),_ZxAnDsx1StandbyDsx1LinkNo_Type())
zxAnDsx1StandbyDsx1LinkNo.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnDsx1StandbyDsx1LinkNo.setStatus(_A)
class _ZxAnDsx1CurrWorkingDsx1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('master',2),('standby',3)))
_ZxAnDsx1CurrWorkingDsx1_Type.__name__=_B
_ZxAnDsx1CurrWorkingDsx1_Object=MibTableColumn
zxAnDsx1CurrWorkingDsx1=_ZxAnDsx1CurrWorkingDsx1_Object((1,3,6,1,4,1,3902,1015,5200,3,1,19,1,11),_ZxAnDsx1CurrWorkingDsx1_Type())
zxAnDsx1CurrWorkingDsx1.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnDsx1CurrWorkingDsx1.setStatus(_A)
_ZxAnDsx1ProtectionGroupRowStatus_Type=RowStatus
_ZxAnDsx1ProtectionGroupRowStatus_Object=MibTableColumn
zxAnDsx1ProtectionGroupRowStatus=_ZxAnDsx1ProtectionGroupRowStatus_Object((1,3,6,1,4,1,3902,1015,5200,3,1,19,1,20),_ZxAnDsx1ProtectionGroupRowStatus_Type())
zxAnDsx1ProtectionGroupRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnDsx1ProtectionGroupRowStatus.setStatus(_A)
_ZxAnHwTimeSlotUsageObjects_ObjectIdentity=ObjectIdentity
zxAnHwTimeSlotUsageObjects=_ZxAnHwTimeSlotUsageObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,5200,3,1,20))
_ZxAnHwTimeSlotUsageGlobalObjects_ObjectIdentity=ObjectIdentity
zxAnHwTimeSlotUsageGlobalObjects=_ZxAnHwTimeSlotUsageGlobalObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,5200,3,1,20,1))
class _ZxAnHwTimeSlotUsageThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_ZxAnHwTimeSlotUsageThreshold_Type.__name__=_B
_ZxAnHwTimeSlotUsageThreshold_Object=MibScalar
zxAnHwTimeSlotUsageThreshold=_ZxAnHwTimeSlotUsageThreshold_Object((1,3,6,1,4,1,3902,1015,5200,3,1,20,1,1),_ZxAnHwTimeSlotUsageThreshold_Type())
zxAnHwTimeSlotUsageThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnHwTimeSlotUsageThreshold.setStatus(_A)
if mibBuilder.loadTexts:zxAnHwTimeSlotUsageThreshold.setUnits(_g)
_ZxAnHwTimeSlotUsageTable_Object=MibTable
zxAnHwTimeSlotUsageTable=_ZxAnHwTimeSlotUsageTable_Object((1,3,6,1,4,1,3902,1015,5200,3,1,20,2))
if mibBuilder.loadTexts:zxAnHwTimeSlotUsageTable.setStatus(_A)
_ZxAnHwTimeSlotUsageEntry_Object=MibTableRow
zxAnHwTimeSlotUsageEntry=_ZxAnHwTimeSlotUsageEntry_Object((1,3,6,1,4,1,3902,1015,5200,3,1,20,2,1))
zxAnHwTimeSlotUsageEntry.setIndexNames((0,_C,_AN),(0,_C,_AO))
if mibBuilder.loadTexts:zxAnHwTimeSlotUsageEntry.setStatus(_A)
_ZxAnHwTimeSlotUsageRack_Type=Integer32
_ZxAnHwTimeSlotUsageRack_Object=MibTableColumn
zxAnHwTimeSlotUsageRack=_ZxAnHwTimeSlotUsageRack_Object((1,3,6,1,4,1,3902,1015,5200,3,1,20,2,1,1),_ZxAnHwTimeSlotUsageRack_Type())
zxAnHwTimeSlotUsageRack.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnHwTimeSlotUsageRack.setStatus(_A)
_ZxAnHwTimeSlotUsageShelf_Type=Integer32
_ZxAnHwTimeSlotUsageShelf_Object=MibTableColumn
zxAnHwTimeSlotUsageShelf=_ZxAnHwTimeSlotUsageShelf_Object((1,3,6,1,4,1,3902,1015,5200,3,1,20,2,1,2),_ZxAnHwTimeSlotUsageShelf_Type())
zxAnHwTimeSlotUsageShelf.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnHwTimeSlotUsageShelf.setStatus(_A)
class _ZxAnHwTimeSlotUsage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_ZxAnHwTimeSlotUsage_Type.__name__=_B
_ZxAnHwTimeSlotUsage_Object=MibTableColumn
zxAnHwTimeSlotUsage=_ZxAnHwTimeSlotUsage_Object((1,3,6,1,4,1,3902,1015,5200,3,1,20,2,1,3),_ZxAnHwTimeSlotUsage_Type())
zxAnHwTimeSlotUsage.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnHwTimeSlotUsage.setStatus(_A)
if mibBuilder.loadTexts:zxAnHwTimeSlotUsage.setUnits(_g)
_MsagResource_ObjectIdentity=ObjectIdentity
msagResource=_MsagResource_ObjectIdentity((1,3,6,1,4,1,3902,1015,5200,3,3))
_A200SlcTermIDTable_Object=MibTable
a200SlcTermIDTable=_A200SlcTermIDTable_Object((1,3,6,1,4,1,3902,1015,5200,3,3,6))
if mibBuilder.loadTexts:a200SlcTermIDTable.setStatus(_A)
_A200SlcTermIDEntry_Object=MibTableRow
a200SlcTermIDEntry=_A200SlcTermIDEntry_Object((1,3,6,1,4,1,3902,1015,5200,3,3,6,1))
a200SlcTermIDEntry.setIndexNames((0,_C,_AP),(0,_C,_AQ),(0,_C,_AR),(0,_C,_AS))
if mibBuilder.loadTexts:a200SlcTermIDEntry.setStatus(_A)
_A200slcTermIDrackno_Type=Integer32
_A200slcTermIDrackno_Object=MibTableColumn
a200slcTermIDrackno=_A200slcTermIDrackno_Object((1,3,6,1,4,1,3902,1015,5200,3,3,6,1,1),_A200slcTermIDrackno_Type())
a200slcTermIDrackno.setMaxAccess(_G)
if mibBuilder.loadTexts:a200slcTermIDrackno.setStatus(_A)
_A200slcTermIDshelfno_Type=Integer32
_A200slcTermIDshelfno_Object=MibTableColumn
a200slcTermIDshelfno=_A200slcTermIDshelfno_Object((1,3,6,1,4,1,3902,1015,5200,3,3,6,1,2),_A200slcTermIDshelfno_Type())
a200slcTermIDshelfno.setMaxAccess(_G)
if mibBuilder.loadTexts:a200slcTermIDshelfno.setStatus(_A)
_A200slcTermIDslotno_Type=Integer32
_A200slcTermIDslotno_Object=MibTableColumn
a200slcTermIDslotno=_A200slcTermIDslotno_Object((1,3,6,1,4,1,3902,1015,5200,3,3,6,1,3),_A200slcTermIDslotno_Type())
a200slcTermIDslotno.setMaxAccess(_G)
if mibBuilder.loadTexts:a200slcTermIDslotno.setStatus(_A)
class _A200slcTermIDBeginIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
_A200slcTermIDBeginIndex_Type.__name__=_B
_A200slcTermIDBeginIndex_Object=MibTableColumn
a200slcTermIDBeginIndex=_A200slcTermIDBeginIndex_Object((1,3,6,1,4,1,3902,1015,5200,3,3,6,1,4),_A200slcTermIDBeginIndex_Type())
a200slcTermIDBeginIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:a200slcTermIDBeginIndex.setStatus(_A)
class _A200slcTermIDOperSum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,192))
_A200slcTermIDOperSum_Type.__name__=_B
_A200slcTermIDOperSum_Object=MibTableColumn
a200slcTermIDOperSum=_A200slcTermIDOperSum_Object((1,3,6,1,4,1,3902,1015,5200,3,3,6,1,5),_A200slcTermIDOperSum_Type())
a200slcTermIDOperSum.setMaxAccess(_D)
if mibBuilder.loadTexts:a200slcTermIDOperSum.setStatus(_A)
class _A200slcTermIDTMID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_A200slcTermIDTMID_Type.__name__=_A4
_A200slcTermIDTMID_Object=MibTableColumn
a200slcTermIDTMID=_A200slcTermIDTMID_Object((1,3,6,1,4,1,3902,1015,5200,3,3,6,1,6),_A200slcTermIDTMID_Type())
a200slcTermIDTMID.setMaxAccess(_D)
if mibBuilder.loadTexts:a200slcTermIDTMID.setStatus(_A)
class _A200slcTermIDType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('type1',1),('type2',2),('type3',3)))
_A200slcTermIDType_Type.__name__=_B
_A200slcTermIDType_Object=MibTableColumn
a200slcTermIDType=_A200slcTermIDType_Object((1,3,6,1,4,1,3902,1015,5200,3,3,6,1,7),_A200slcTermIDType_Type())
a200slcTermIDType.setMaxAccess(_D)
if mibBuilder.loadTexts:a200slcTermIDType.setStatus(_A)
_A200slcTermIDBeginNo_Type=Integer32
_A200slcTermIDBeginNo_Object=MibTableColumn
a200slcTermIDBeginNo=_A200slcTermIDBeginNo_Object((1,3,6,1,4,1,3902,1015,5200,3,3,6,1,8),_A200slcTermIDBeginNo_Type())
a200slcTermIDBeginNo.setMaxAccess(_D)
if mibBuilder.loadTexts:a200slcTermIDBeginNo.setStatus(_A)
class _A200slcTermIDDigitLen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,64))
_A200slcTermIDDigitLen_Type.__name__=_B
_A200slcTermIDDigitLen_Object=MibTableColumn
a200slcTermIDDigitLen=_A200slcTermIDDigitLen_Object((1,3,6,1,4,1,3902,1015,5200,3,3,6,1,9),_A200slcTermIDDigitLen_Type())
a200slcTermIDDigitLen.setMaxAccess(_D)
if mibBuilder.loadTexts:a200slcTermIDDigitLen.setStatus(_A)
class _A200slcTermIDMgId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_A200slcTermIDMgId_Type.__name__=_B
_A200slcTermIDMgId_Object=MibTableColumn
a200slcTermIDMgId=_A200slcTermIDMgId_Object((1,3,6,1,4,1,3902,1015,5200,3,3,6,1,11),_A200slcTermIDMgId_Type())
a200slcTermIDMgId.setMaxAccess(_D)
if mibBuilder.loadTexts:a200slcTermIDMgId.setStatus(_A)
class _A200slcTerminationID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,64))
_A200slcTerminationID_Type.__name__=_B
_A200slcTerminationID_Object=MibTableColumn
a200slcTerminationID=_A200slcTerminationID_Object((1,3,6,1,4,1,3902,1015,5200,3,3,6,1,12),_A200slcTerminationID_Type())
a200slcTerminationID.setMaxAccess(_F)
if mibBuilder.loadTexts:a200slcTerminationID.setStatus(_A)
_A200slcTermIDRowStatus_Type=RowStatus
_A200slcTermIDRowStatus_Object=MibTableColumn
a200slcTermIDRowStatus=_A200slcTermIDRowStatus_Object((1,3,6,1,4,1,3902,1015,5200,3,3,6,1,13),_A200slcTermIDRowStatus_Type())
a200slcTermIDRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:a200slcTermIDRowStatus.setStatus(_A)
_A200IpsTermIDTable_Object=MibTable
a200IpsTermIDTable=_A200IpsTermIDTable_Object((1,3,6,1,4,1,3902,1015,5200,3,3,7))
if mibBuilder.loadTexts:a200IpsTermIDTable.setStatus(_A)
_A200IpsTermIDEntry_Object=MibTableRow
a200IpsTermIDEntry=_A200IpsTermIDEntry_Object((1,3,6,1,4,1,3902,1015,5200,3,3,7,1))
a200IpsTermIDEntry.setIndexNames((0,_C,_AT))
if mibBuilder.loadTexts:a200IpsTermIDEntry.setStatus(_A)
_A200IpsTermIDSeqNo_Type=Integer32
_A200IpsTermIDSeqNo_Object=MibTableColumn
a200IpsTermIDSeqNo=_A200IpsTermIDSeqNo_Object((1,3,6,1,4,1,3902,1015,5200,3,3,7,1,1),_A200IpsTermIDSeqNo_Type())
a200IpsTermIDSeqNo.setMaxAccess(_G)
if mibBuilder.loadTexts:a200IpsTermIDSeqNo.setStatus(_A)
class _A200IpsTermIDDeltag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_A200IpsTermIDDeltag_Type.__name__=_B
_A200IpsTermIDDeltag_Object=MibTableColumn
a200IpsTermIDDeltag=_A200IpsTermIDDeltag_Object((1,3,6,1,4,1,3902,1015,5200,3,3,7,1,2),_A200IpsTermIDDeltag_Type())
a200IpsTermIDDeltag.setMaxAccess(_D)
if mibBuilder.loadTexts:a200IpsTermIDDeltag.setStatus(_A)
class _A200IpsTermIDBeginSeqNo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,720))
_A200IpsTermIDBeginSeqNo_Type.__name__=_B
_A200IpsTermIDBeginSeqNo_Object=MibTableColumn
a200IpsTermIDBeginSeqNo=_A200IpsTermIDBeginSeqNo_Object((1,3,6,1,4,1,3902,1015,5200,3,3,7,1,3),_A200IpsTermIDBeginSeqNo_Type())
a200IpsTermIDBeginSeqNo.setMaxAccess(_D)
if mibBuilder.loadTexts:a200IpsTermIDBeginSeqNo.setStatus(_A)
class _A200IpsTermIDOperNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,720))
_A200IpsTermIDOperNum_Type.__name__=_B
_A200IpsTermIDOperNum_Object=MibTableColumn
a200IpsTermIDOperNum=_A200IpsTermIDOperNum_Object((1,3,6,1,4,1,3902,1015,5200,3,3,7,1,4),_A200IpsTermIDOperNum_Type())
a200IpsTermIDOperNum.setMaxAccess(_D)
if mibBuilder.loadTexts:a200IpsTermIDOperNum.setStatus(_A)
class _A200IpsTermIDTMIDFix_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_A200IpsTermIDTMIDFix_Type.__name__=_L
_A200IpsTermIDTMIDFix_Object=MibTableColumn
a200IpsTermIDTMIDFix=_A200IpsTermIDTMIDFix_Object((1,3,6,1,4,1,3902,1015,5200,3,3,7,1,5),_A200IpsTermIDTMIDFix_Type())
a200IpsTermIDTMIDFix.setMaxAccess(_D)
if mibBuilder.loadTexts:a200IpsTermIDTMIDFix.setStatus(_A)
class _A200IpsTermIDType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*(('type2',2),('type3',3)))
_A200IpsTermIDType_Type.__name__=_B
_A200IpsTermIDType_Object=MibTableColumn
a200IpsTermIDType=_A200IpsTermIDType_Object((1,3,6,1,4,1,3902,1015,5200,3,3,7,1,6),_A200IpsTermIDType_Type())
a200IpsTermIDType.setMaxAccess(_D)
if mibBuilder.loadTexts:a200IpsTermIDType.setStatus(_A)
class _A200IpsTermIDDigitLen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,64))
_A200IpsTermIDDigitLen_Type.__name__=_B
_A200IpsTermIDDigitLen_Object=MibTableColumn
a200IpsTermIDDigitLen=_A200IpsTermIDDigitLen_Object((1,3,6,1,4,1,3902,1015,5200,3,3,7,1,7),_A200IpsTermIDDigitLen_Type())
a200IpsTermIDDigitLen.setMaxAccess(_D)
if mibBuilder.loadTexts:a200IpsTermIDDigitLen.setStatus(_A)
_A200IpsTermIDBeginNo_Type=Integer32
_A200IpsTermIDBeginNo_Object=MibTableColumn
a200IpsTermIDBeginNo=_A200IpsTermIDBeginNo_Object((1,3,6,1,4,1,3902,1015,5200,3,3,7,1,8),_A200IpsTermIDBeginNo_Type())
a200IpsTermIDBeginNo.setMaxAccess(_D)
if mibBuilder.loadTexts:a200IpsTermIDBeginNo.setStatus(_A)
class _A200IpsTermIDMgId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_A200IpsTermIDMgId_Type.__name__=_B
_A200IpsTermIDMgId_Object=MibTableColumn
a200IpsTermIDMgId=_A200IpsTermIDMgId_Object((1,3,6,1,4,1,3902,1015,5200,3,3,7,1,9),_A200IpsTermIDMgId_Type())
a200IpsTermIDMgId.setMaxAccess(_D)
if mibBuilder.loadTexts:a200IpsTermIDMgId.setStatus(_A)
class _A200IpsTerminationID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_A200IpsTerminationID_Type.__name__=_L
_A200IpsTerminationID_Object=MibTableColumn
a200IpsTerminationID=_A200IpsTerminationID_Object((1,3,6,1,4,1,3902,1015,5200,3,3,7,1,10),_A200IpsTerminationID_Type())
a200IpsTerminationID.setMaxAccess(_F)
if mibBuilder.loadTexts:a200IpsTerminationID.setStatus(_A)
_A200IpsTermIDRowStatus_Type=RowStatus
_A200IpsTermIDRowStatus_Object=MibTableColumn
a200IpsTermIDRowStatus=_A200IpsTermIDRowStatus_Object((1,3,6,1,4,1,3902,1015,5200,3,3,7,1,11),_A200IpsTermIDRowStatus_Type())
a200IpsTermIDRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:a200IpsTermIDRowStatus.setStatus(_A)
_A200RtpParTable_Object=MibTable
a200RtpParTable=_A200RtpParTable_Object((1,3,6,1,4,1,3902,1015,5200,3,3,8))
if mibBuilder.loadTexts:a200RtpParTable.setStatus(_A)
_A200RtpParEntry_Object=MibTableRow
a200RtpParEntry=_A200RtpParEntry_Object((1,3,6,1,4,1,3902,1015,5200,3,3,8,1))
a200RtpParEntry.setIndexNames((0,_C,_AU))
if mibBuilder.loadTexts:a200RtpParEntry.setStatus(_A)
class _A200rtpparparid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,254))
_A200rtpparparid_Type.__name__=_B
_A200rtpparparid_Object=MibTableColumn
a200rtpparparid=_A200rtpparparid_Object((1,3,6,1,4,1,3902,1015,5200,3,3,8,1,1),_A200rtpparparid_Type())
a200rtpparparid.setMaxAccess(_G)
if mibBuilder.loadTexts:a200rtpparparid.setStatus(_A)
class _A200rtpparvadval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_M,0),('defaultscheme',1),('pt13scheme',2),('nosilence',3)))
_A200rtpparvadval_Type.__name__=_B
_A200rtpparvadval_Object=MibTableColumn
a200rtpparvadval=_A200rtpparvadval_Object((1,3,6,1,4,1,3902,1015,5200,3,3,8,1,2),_A200rtpparvadval_Type())
a200rtpparvadval.setMaxAccess(_E)
if mibBuilder.loadTexts:a200rtpparvadval.setStatus(_A)
class _A200rtppardtmfrlmod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,4,6)));namedValues=NamedValues(*(('notRelay',0),('voiceCoding',1),('redRfc2833',2),('aal2Ietf',4),('nredRfc2833',6)))
_A200rtppardtmfrlmod_Type.__name__=_B
_A200rtppardtmfrlmod_Object=MibTableColumn
a200rtppardtmfrlmod=_A200rtppardtmfrlmod_Object((1,3,6,1,4,1,3902,1015,5200,3,3,8,1,3),_A200rtppardtmfrlmod_Type())
a200rtppardtmfrlmod.setMaxAccess(_E)
if mibBuilder.loadTexts:a200rtppardtmfrlmod.setStatus(_A)
class _A200rtpparpcmlaw_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('aLaw',0),('uLaw',1)))
_A200rtpparpcmlaw_Type.__name__=_B
_A200rtpparpcmlaw_Object=MibTableColumn
a200rtpparpcmlaw=_A200rtpparpcmlaw_Object((1,3,6,1,4,1,3902,1015,5200,3,3,8,1,4),_A200rtpparpcmlaw_Type())
a200rtpparpcmlaw.setMaxAccess(_E)
if mibBuilder.loadTexts:a200rtpparpcmlaw.setStatus(_A)
class _A200rtpparsiltopcm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('comfortNoise',0),('silence',1)))
_A200rtpparsiltopcm_Type.__name__=_B
_A200rtpparsiltopcm_Object=MibTableColumn
a200rtpparsiltopcm=_A200rtpparsiltopcm_Object((1,3,6,1,4,1,3902,1015,5200,3,3,8,1,5),_A200rtpparsiltopcm_Type())
a200rtpparsiltopcm.setMaxAccess(_E)
if mibBuilder.loadTexts:a200rtpparsiltopcm.setStatus(_A)
class _A200rtppardcfilter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_N,0),(_M,1)))
_A200rtppardcfilter_Type.__name__=_B
_A200rtppardcfilter_Object=MibTableColumn
a200rtppardcfilter=_A200rtppardcfilter_Object((1,3,6,1,4,1,3902,1015,5200,3,3,8,1,6),_A200rtppardcfilter_Type())
a200rtppardcfilter.setMaxAccess(_E)
if mibBuilder.loadTexts:a200rtppardcfilter.setStatus(_A)
class _A200rtpparpcmtopkggain_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,200))
_A200rtpparpcmtopkggain_Type.__name__=_B
_A200rtpparpcmtopkggain_Object=MibTableColumn
a200rtpparpcmtopkggain=_A200rtpparpcmtopkggain_Object((1,3,6,1,4,1,3902,1015,5200,3,3,8,1,7),_A200rtpparpcmtopkggain_Type())
a200rtpparpcmtopkggain.setMaxAccess(_E)
if mibBuilder.loadTexts:a200rtpparpcmtopkggain.setStatus(_A)
class _A200rtpparpkgtopcmgain_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,200))
_A200rtpparpkgtopcmgain_Type.__name__=_B
_A200rtpparpkgtopcmgain_Object=MibTableColumn
a200rtpparpkgtopcmgain=_A200rtpparpkgtopcmgain_Object((1,3,6,1,4,1,3902,1015,5200,3,3,8,1,8),_A200rtpparpkgtopcmgain_Type())
a200rtpparpkgtopcmgain.setMaxAccess(_E)
if mibBuilder.loadTexts:a200rtpparpkgtopcmgain.setStatus(_A)
class _A200rtpparconceal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('notReplace',0),('whiteLine',1),('lastLine',2)))
_A200rtpparconceal_Type.__name__=_B
_A200rtpparconceal_Object=MibTableColumn
a200rtpparconceal=_A200rtpparconceal_Object((1,3,6,1,4,1,3902,1015,5200,3,3,8,1,9),_A200rtpparconceal_Type())
a200rtpparconceal.setMaxAccess(_E)
if mibBuilder.loadTexts:a200rtpparconceal.setStatus(_A)
class _A200rtpparecmdisabl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_N,0),(_M,1)))
_A200rtpparecmdisabl_Type.__name__=_B
_A200rtpparecmdisabl_Object=MibTableColumn
a200rtpparecmdisabl=_A200rtpparecmdisabl_Object((1,3,6,1,4,1,3902,1015,5200,3,3,8,1,10),_A200rtpparecmdisabl_Type())
a200rtpparecmdisabl.setMaxAccess(_E)
if mibBuilder.loadTexts:a200rtpparecmdisabl.setStatus(_A)
class _A200rtpparspeedlim_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*(('noLimit',0),('is2400bps',1),('is4800bps',2),('is7200bps',3),('is9600bps',4),('is12000bps',5),('is14400bps',6)))
_A200rtpparspeedlim_Type.__name__=_B
_A200rtpparspeedlim_Object=MibTableColumn
a200rtpparspeedlim=_A200rtpparspeedlim_Object((1,3,6,1,4,1,3902,1015,5200,3,3,8,1,11),_A200rtpparspeedlim_Type())
a200rtpparspeedlim.setMaxAccess(_E)
if mibBuilder.loadTexts:a200rtpparspeedlim.setStatus(_A)
class _A200rtpparerrrecov_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('redundancy',0),('fec',1)))
_A200rtpparerrrecov_Type.__name__=_B
_A200rtpparerrrecov_Object=MibTableColumn
a200rtpparerrrecov=_A200rtpparerrrecov_Object((1,3,6,1,4,1,3902,1015,5200,3,3,8,1,12),_A200rtpparerrrecov_Type())
a200rtpparerrrecov.setMaxAccess(_E)
if mibBuilder.loadTexts:a200rtpparerrrecov.setStatus(_A)
class _A200rtppartcfproc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('procedure2',0),('procedure1',1)))
_A200rtppartcfproc_Type.__name__=_B
_A200rtppartcfproc_Object=MibTableColumn
a200rtppartcfproc=_A200rtppartcfproc_Object((1,3,6,1,4,1,3902,1015,5200,3,3,8,1,13),_A200rtppartcfproc_Type())
a200rtppartcfproc.setMaxAccess(_E)
if mibBuilder.loadTexts:a200rtppartcfproc.setStatus(_A)
class _A200rtppart38enable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,10,11)));namedValues=NamedValues(*(('t30',0),('t38',1),('rtp',2),('halfControl',10),('fullControl',11)))
_A200rtppart38enable_Type.__name__=_B
_A200rtppart38enable_Object=MibTableColumn
a200rtppart38enable=_A200rtppart38enable_Object((1,3,6,1,4,1,3902,1015,5200,3,3,8,1,14),_A200rtppart38enable_Type())
a200rtppart38enable.setMaxAccess(_E)
if mibBuilder.loadTexts:a200rtppart38enable.setStatus(_A)
class _A200rtppardtmfduplex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_A200rtppardtmfduplex_Type.__name__=_B
_A200rtppardtmfduplex_Object=MibTableColumn
a200rtppardtmfduplex=_A200rtppardtmfduplex_Object((1,3,6,1,4,1,3902,1015,5200,3,3,8,1,15),_A200rtppardtmfduplex_Type())
a200rtppardtmfduplex.setMaxAccess(_E)
if mibBuilder.loadTexts:a200rtppardtmfduplex.setStatus(_A)
class _A200rtpparNumBeforeOff_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_A200rtpparNumBeforeOff_Type.__name__=_B
_A200rtpparNumBeforeOff_Object=MibTableColumn
a200rtpparNumBeforeOff=_A200rtpparNumBeforeOff_Object((1,3,6,1,4,1,3902,1015,5200,3,3,8,1,16),_A200rtpparNumBeforeOff_Type())
a200rtpparNumBeforeOff.setMaxAccess(_E)
if mibBuilder.loadTexts:a200rtpparNumBeforeOff.setStatus(_A)
class _A200rtpparIgnoreA_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_A200rtpparIgnoreA_Type.__name__=_B
_A200rtpparIgnoreA_Object=MibTableColumn
a200rtpparIgnoreA=_A200rtpparIgnoreA_Object((1,3,6,1,4,1,3902,1015,5200,3,3,8,1,17),_A200rtpparIgnoreA_Type())
a200rtpparIgnoreA.setMaxAccess(_E)
if mibBuilder.loadTexts:a200rtpparIgnoreA.setStatus(_A)
class _A200rtpparToneDuplex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_A200rtpparToneDuplex_Type.__name__=_B
_A200rtpparToneDuplex_Object=MibTableColumn
a200rtpparToneDuplex=_A200rtpparToneDuplex_Object((1,3,6,1,4,1,3902,1015,5200,3,3,8,1,18),_A200rtpparToneDuplex_Type())
a200rtpparToneDuplex.setMaxAccess(_E)
if mibBuilder.loadTexts:a200rtpparToneDuplex.setStatus(_A)
class _A200rtppardecodadapt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_A200rtppardecodadapt_Type.__name__=_B
_A200rtppardecodadapt_Object=MibTableColumn
a200rtppardecodadapt=_A200rtppardecodadapt_Object((1,3,6,1,4,1,3902,1015,5200,3,3,8,1,19),_A200rtppardecodadapt_Type())
a200rtppardecodadapt.setMaxAccess(_E)
if mibBuilder.loadTexts:a200rtppardecodadapt.setStatus(_A)
class _A200rtpparg723rate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('lowRate',0),('highRate',1)))
_A200rtpparg723rate_Type.__name__=_B
_A200rtpparg723rate_Object=MibTableColumn
a200rtpparg723rate=_A200rtpparg723rate_Object((1,3,6,1,4,1,3902,1015,5200,3,3,8,1,20),_A200rtpparg723rate_Type())
a200rtpparg723rate.setMaxAccess(_E)
if mibBuilder.loadTexts:a200rtpparg723rate.setStatus(_A)
class _A200rtpparpckgendis_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_N,0),(_M,1)))
_A200rtpparpckgendis_Type.__name__=_B
_A200rtpparpckgendis_Object=MibTableColumn
a200rtpparpckgendis=_A200rtpparpckgendis_Object((1,3,6,1,4,1,3902,1015,5200,3,3,8,1,21),_A200rtpparpckgendis_Type())
a200rtpparpckgendis.setMaxAccess(_E)
if mibBuilder.loadTexts:a200rtpparpckgendis.setStatus(_A)
class _A200rtppardtmfpyld_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_A200rtppardtmfpyld_Type.__name__=_B
_A200rtppardtmfpyld_Object=MibTableColumn
a200rtppardtmfpyld=_A200rtppardtmfpyld_Object((1,3,6,1,4,1,3902,1015,5200,3,3,8,1,22),_A200rtppardtmfpyld_Type())
a200rtppardtmfpyld.setMaxAccess(_E)
if mibBuilder.loadTexts:a200rtppardtmfpyld.setStatus(_A)
class _A200rtppardtmfredpyld_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_A200rtppardtmfredpyld_Type.__name__=_B
_A200rtppardtmfredpyld_Object=MibTableColumn
a200rtppardtmfredpyld=_A200rtppardtmfredpyld_Object((1,3,6,1,4,1,3902,1015,5200,3,3,8,1,23),_A200rtppardtmfredpyld_Type())
a200rtppardtmfredpyld.setMaxAccess(_E)
if mibBuilder.loadTexts:a200rtppardtmfredpyld.setStatus(_A)
class _A200rtpparfaxdatared_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,200))
_A200rtpparfaxdatared_Type.__name__=_B
_A200rtpparfaxdatared_Object=MibTableColumn
a200rtpparfaxdatared=_A200rtpparfaxdatared_Object((1,3,6,1,4,1,3902,1015,5200,3,3,8,1,24),_A200rtpparfaxdatared_Type())
a200rtpparfaxdatared.setMaxAccess(_E)
if mibBuilder.loadTexts:a200rtpparfaxdatared.setStatus(_A)
class _A200rtppart30msgred_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_A200rtppart30msgred_Type.__name__=_B
_A200rtppart30msgred_Object=MibTableColumn
a200rtppart30msgred=_A200rtppart30msgred_Object((1,3,6,1,4,1,3902,1015,5200,3,3,8,1,25),_A200rtppart30msgred_Type())
a200rtppart30msgred.setMaxAccess(_E)
if mibBuilder.loadTexts:a200rtppart30msgred.setStatus(_A)
class _A200rtpparmasecenal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_M,0),(_N,1)))
_A200rtpparmasecenal_Type.__name__=_B
_A200rtpparmasecenal_Object=MibTableColumn
a200rtpparmasecenal=_A200rtpparmasecenal_Object((1,3,6,1,4,1,3902,1015,5200,3,3,8,1,26),_A200rtpparmasecenal_Type())
a200rtpparmasecenal.setMaxAccess(_E)
if mibBuilder.loadTexts:a200rtpparmasecenal.setStatus(_A)
class _A200rtpparhdwecdis_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_N,0),(_M,1)))
_A200rtpparhdwecdis_Type.__name__=_B
_A200rtpparhdwecdis_Object=MibTableColumn
a200rtpparhdwecdis=_A200rtpparhdwecdis_Object((1,3,6,1,4,1,3902,1015,5200,3,3,8,1,27),_A200rtpparhdwecdis_Type())
a200rtpparhdwecdis.setMaxAccess(_E)
if mibBuilder.loadTexts:a200rtpparhdwecdis.setStatus(_A)
class _A200rtpparhecfrz_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('allowUpdate',0),('disableUpdate',1)))
_A200rtpparhecfrz_Type.__name__=_B
_A200rtpparhecfrz_Object=MibTableColumn
a200rtpparhecfrz=_A200rtpparhecfrz_Object((1,3,6,1,4,1,3902,1015,5200,3,3,8,1,28),_A200rtpparhecfrz_Type())
a200rtpparhecfrz.setMaxAccess(_E)
if mibBuilder.loadTexts:a200rtpparhecfrz.setStatus(_A)
class _A200rtpparectxf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('nonLinear',0),('fixedGain',1)))
_A200rtpparectxf_Type.__name__=_B
_A200rtpparectxf_Object=MibTableColumn
a200rtpparectxf=_A200rtpparectxf_Object((1,3,6,1,4,1,3902,1015,5200,3,3,8,1,29),_A200rtpparectxf_Type())
a200rtpparectxf.setMaxAccess(_E)
if mibBuilder.loadTexts:a200rtpparectxf.setStatus(_A)
class _A200rtpparectxm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('normal',0),('mute',1)))
_A200rtpparectxm_Type.__name__=_B
_A200rtpparectxm_Object=MibTableColumn
a200rtpparectxm=_A200rtpparectxm_Object((1,3,6,1,4,1,3902,1015,5200,3,3,8,1,30),_A200rtpparectxm_Type())
a200rtpparectxm.setMaxAccess(_E)
if mibBuilder.loadTexts:a200rtpparectxm.setStatus(_A)
class _A200rtpparecrxm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('normal',0),('mute',1)))
_A200rtpparecrxm_Type.__name__=_B
_A200rtpparecrxm_Object=MibTableColumn
a200rtpparecrxm=_A200rtpparecrxm_Object((1,3,6,1,4,1,3902,1015,5200,3,3,8,1,31),_A200rtpparecrxm_Type())
a200rtpparecrxm.setMaxAccess(_E)
if mibBuilder.loadTexts:a200rtpparecrxm.setStatus(_A)
class _A200rtpparheclen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_A200rtpparheclen_Type.__name__=_B
_A200rtpparheclen_Object=MibTableColumn
a200rtpparheclen=_A200rtpparheclen_Object((1,3,6,1,4,1,3902,1015,5200,3,3,8,1,32),_A200rtpparheclen_Type())
a200rtpparheclen.setMaxAccess(_E)
if mibBuilder.loadTexts:a200rtpparheclen.setStatus(_A)
class _A200rtpparlpwmin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_A200rtpparlpwmin_Type.__name__=_B
_A200rtpparlpwmin_Object=MibTableColumn
a200rtpparlpwmin=_A200rtpparlpwmin_Object((1,3,6,1,4,1,3902,1015,5200,3,3,8,1,33),_A200rtpparlpwmin_Type())
a200rtpparlpwmin.setMaxAccess(_E)
if mibBuilder.loadTexts:a200rtpparlpwmin.setStatus(_A)
class _A200rtpparlpwmax_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_A200rtpparlpwmax_Type.__name__=_B
_A200rtpparlpwmax_Object=MibTableColumn
a200rtpparlpwmax=_A200rtpparlpwmax_Object((1,3,6,1,4,1,3902,1015,5200,3,3,8,1,34),_A200rtpparlpwmax_Type())
a200rtpparlpwmax.setMaxAccess(_E)
if mibBuilder.loadTexts:a200rtpparlpwmax.setStatus(_A)
class _A200rtpparlpwinit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_A200rtpparlpwinit_Type.__name__=_B
_A200rtpparlpwinit_Object=MibTableColumn
a200rtpparlpwinit=_A200rtpparlpwinit_Object((1,3,6,1,4,1,3902,1015,5200,3,3,8,1,35),_A200rtpparlpwinit_Type())
a200rtpparlpwinit.setMaxAccess(_E)
if mibBuilder.loadTexts:a200rtpparlpwinit.setStatus(_A)
class _A200rtpparlpr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_A200rtpparlpr_Type.__name__=_B
_A200rtpparlpr_Object=MibTableColumn
a200rtpparlpr=_A200rtpparlpr_Object((1,3,6,1,4,1,3902,1015,5200,3,3,8,1,36),_A200rtpparlpr_Type())
a200rtpparlpr.setMaxAccess(_E)
if mibBuilder.loadTexts:a200rtpparlpr.setStatus(_A)
class _A200rtpparfsklevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(62,382))
_A200rtpparfsklevel_Type.__name__=_B
_A200rtpparfsklevel_Object=MibTableColumn
a200rtpparfsklevel=_A200rtpparfsklevel_Object((1,3,6,1,4,1,3902,1015,5200,3,3,8,1,37),_A200rtpparfsklevel_Type())
a200rtpparfsklevel.setMaxAccess(_E)
if mibBuilder.loadTexts:a200rtpparfsklevel.setStatus(_A)
class _A200rtpparg711redund_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('noRedundancy',0),('is1Package',1),('is2Package',2),('is3Package',3)))
_A200rtpparg711redund_Type.__name__=_B
_A200rtpparg711redund_Object=MibTableColumn
a200rtpparg711redund=_A200rtpparg711redund_Object((1,3,6,1,4,1,3902,1015,5200,3,3,8,1,38),_A200rtpparg711redund_Type())
a200rtpparg711redund.setMaxAccess(_E)
if mibBuilder.loadTexts:a200rtpparg711redund.setStatus(_A)
class _A200rtpparmodemmode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,2,3,4,5,6,11)));namedValues=NamedValues(*(('modemDelay5s',0),('transparent',2),('modemImmediate',3),('faxImmediate',4),('cidImmediate',5),('ipModem',6),('fullCtrl',11)))
_A200rtpparmodemmode_Type.__name__=_B
_A200rtpparmodemmode_Object=MibTableColumn
a200rtpparmodemmode=_A200rtpparmodemmode_Object((1,3,6,1,4,1,3902,1015,5200,3,3,8,1,39),_A200rtpparmodemmode_Type())
a200rtpparmodemmode.setMaxAccess(_E)
if mibBuilder.loadTexts:a200rtpparmodemmode.setStatus(_A)
class _A200rtpparap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_A200rtpparap_Type.__name__=_B
_A200rtpparap_Object=MibTableColumn
a200rtpparap=_A200rtpparap_Object((1,3,6,1,4,1,3902,1015,5200,3,3,8,1,40),_A200rtpparap_Type())
a200rtpparap.setMaxAccess(_E)
if mibBuilder.loadTexts:a200rtpparap.setStatus(_A)
class _A200rtppardeletmode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_A200rtppardeletmode_Type.__name__=_B
_A200rtppardeletmode_Object=MibTableColumn
a200rtppardeletmode=_A200rtppardeletmode_Object((1,3,6,1,4,1,3902,1015,5200,3,3,8,1,41),_A200rtppardeletmode_Type())
a200rtppardeletmode.setMaxAccess(_E)
if mibBuilder.loadTexts:a200rtppardeletmode.setStatus(_A)
class _A200rtpparnortptime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_A200rtpparnortptime_Type.__name__=_B
_A200rtpparnortptime_Object=MibTableColumn
a200rtpparnortptime=_A200rtpparnortptime_Object((1,3,6,1,4,1,3902,1015,5200,3,3,8,1,42),_A200rtpparnortptime_Type())
a200rtpparnortptime.setMaxAccess(_E)
if mibBuilder.loadTexts:a200rtpparnortptime.setStatus(_A)
class _A200rtpparfaxswtime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_A200rtpparfaxswtime_Type.__name__=_B
_A200rtpparfaxswtime_Object=MibTableColumn
a200rtpparfaxswtime=_A200rtpparfaxswtime_Object((1,3,6,1,4,1,3902,1015,5200,3,3,8,1,43),_A200rtpparfaxswtime_Type())
a200rtpparfaxswtime.setMaxAccess(_E)
if mibBuilder.loadTexts:a200rtpparfaxswtime.setStatus(_A)
class _A200rtppardtmfcidelec_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,630))
_A200rtppardtmfcidelec_Type.__name__=_B
_A200rtppardtmfcidelec_Object=MibTableColumn
a200rtppardtmfcidelec=_A200rtppardtmfcidelec_Object((1,3,6,1,4,1,3902,1015,5200,3,3,8,1,44),_A200rtppardtmfcidelec_Type())
a200rtppardtmfcidelec.setMaxAccess(_E)
if mibBuilder.loadTexts:a200rtppardtmfcidelec.setStatus(_A)
_MsagCallCtrl_ObjectIdentity=ObjectIdentity
msagCallCtrl=_MsagCallCtrl_ObjectIdentity((1,3,6,1,4,1,3902,1015,5200,3,6))
_UpPortTable_Object=MibTable
upPortTable=_UpPortTable_Object((1,3,6,1,4,1,3902,1015,5200,3,6,1))
if mibBuilder.loadTexts:upPortTable.setStatus(_A)
_UpPortEntry_Object=MibTableRow
upPortEntry=_UpPortEntry_Object((1,3,6,1,4,1,3902,1015,5200,3,6,1,1))
upPortEntry.setIndexNames((0,_C,'upportid'))
if mibBuilder.loadTexts:upPortEntry.setStatus(_A)
class _Upportid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_Upportid_Type.__name__=_B
_Upportid_Object=MibTableColumn
upportid=_Upportid_Object((1,3,6,1,4,1,3902,1015,5200,3,6,1,1,1),_Upportid_Type())
upportid.setMaxAccess(_G)
if mibBuilder.loadTexts:upportid.setStatus(_A)
class _Upportrack_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_Upportrack_Type.__name__=_B
_Upportrack_Object=MibTableColumn
upportrack=_Upportrack_Object((1,3,6,1,4,1,3902,1015,5200,3,6,1,1,2),_Upportrack_Type())
upportrack.setMaxAccess(_D)
if mibBuilder.loadTexts:upportrack.setStatus(_A)
class _Upportshelf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_Upportshelf_Type.__name__=_B
_Upportshelf_Object=MibTableColumn
upportshelf=_Upportshelf_Object((1,3,6,1,4,1,3902,1015,5200,3,6,1,1,3),_Upportshelf_Type())
upportshelf.setMaxAccess(_D)
if mibBuilder.loadTexts:upportshelf.setStatus(_A)
class _Upportslot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,23))
_Upportslot_Type.__name__=_B
_Upportslot_Object=MibTableColumn
upportslot=_Upportslot_Object((1,3,6,1,4,1,3902,1015,5200,3,6,1,1,29),_Upportslot_Type())
upportslot.setMaxAccess(_D)
if mibBuilder.loadTexts:upportslot.setStatus(_A)
class _Upportport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_Upportport_Type.__name__=_B
_Upportport_Object=MibTableColumn
upportport=_Upportport_Object((1,3,6,1,4,1,3902,1015,5200,3,6,1,1,31),_Upportport_Type())
upportport.setMaxAccess(_D)
if mibBuilder.loadTexts:upportport.setStatus(_A)
class _Upportsendrateth_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,104857600))
_Upportsendrateth_Type.__name__=_U
_Upportsendrateth_Object=MibTableColumn
upportsendrateth=_Upportsendrateth_Object((1,3,6,1,4,1,3902,1015,5200,3,6,1,1,33),_Upportsendrateth_Type())
upportsendrateth.setMaxAccess(_D)
if mibBuilder.loadTexts:upportsendrateth.setStatus(_A)
class _Upportreceiverateth_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,104857600))
_Upportreceiverateth_Type.__name__=_U
_Upportreceiverateth_Object=MibTableColumn
upportreceiverateth=_Upportreceiverateth_Object((1,3,6,1,4,1,3902,1015,5200,3,6,1,1,35),_Upportreceiverateth_Type())
upportreceiverateth.setMaxAccess(_D)
if mibBuilder.loadTexts:upportreceiverateth.setStatus(_A)
_UpportRowStatus_Type=RowStatus
_UpportRowStatus_Object=MibTableColumn
upportRowStatus=_UpportRowStatus_Object((1,3,6,1,4,1,3902,1015,5200,3,6,1,1,37),_UpportRowStatus_Type())
upportRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:upportRowStatus.setStatus(_A)
_ToneTable_Object=MibTable
toneTable=_ToneTable_Object((1,3,6,1,4,1,3902,1015,5200,3,6,2))
if mibBuilder.loadTexts:toneTable.setStatus(_A)
_ToneEntry_Object=MibTableRow
toneEntry=_ToneEntry_Object((1,3,6,1,4,1,3902,1015,5200,3,6,2,1))
toneEntry.setIndexNames((0,_C,'tonemgid'))
if mibBuilder.loadTexts:toneEntry.setStatus(_A)
class _Tonemgid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_Tonemgid_Type.__name__=_B
_Tonemgid_Object=MibTableColumn
tonemgid=_Tonemgid_Object((1,3,6,1,4,1,3902,1015,5200,3,6,2,1,1),_Tonemgid_Type())
tonemgid.setMaxAccess(_G)
if mibBuilder.loadTexts:tonemgid.setStatus(_A)
class _Tonefaxcngtone_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_V,0),(_W,1)))
_Tonefaxcngtone_Type.__name__=_B
_Tonefaxcngtone_Object=MibTableColumn
tonefaxcngtone=_Tonefaxcngtone_Object((1,3,6,1,4,1,3902,1015,5200,3,6,2,1,2),_Tonefaxcngtone_Type())
tonefaxcngtone.setMaxAccess(_E)
if mibBuilder.loadTexts:tonefaxcngtone.setStatus(_A)
class _Tonev21flagstone_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_V,0),(_W,1)))
_Tonev21flagstone_Type.__name__=_B
_Tonev21flagstone_Object=MibTableColumn
tonev21flagstone=_Tonev21flagstone_Object((1,3,6,1,4,1,3902,1015,5200,3,6,2,1,3),_Tonev21flagstone_Type())
tonev21flagstone.setMaxAccess(_E)
if mibBuilder.loadTexts:tonev21flagstone.setStatus(_A)
class _Tonet38faxend_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_V,0),(_W,1)))
_Tonet38faxend_Type.__name__=_B
_Tonet38faxend_Object=MibTableColumn
tonet38faxend=_Tonet38faxend_Object((1,3,6,1,4,1,3902,1015,5200,3,6,2,1,4),_Tonet38faxend_Type())
tonet38faxend.setMaxAccess(_E)
if mibBuilder.loadTexts:tonet38faxend.setStatus(_A)
class _Toneansamwitone_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_V,0),(_W,1)))
_Toneansamwitone_Type.__name__=_B
_Toneansamwitone_Object=MibTableColumn
toneansamwitone=_Toneansamwitone_Object((1,3,6,1,4,1,3902,1015,5200,3,6,2,1,5),_Toneansamwitone_Type())
toneansamwitone.setMaxAccess(_E)
if mibBuilder.loadTexts:toneansamwitone.setStatus(_A)
class _Toneansamwotone_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_V,0),(_W,1)))
_Toneansamwotone_Type.__name__=_B
_Toneansamwotone_Object=MibTableColumn
toneansamwotone=_Toneansamwotone_Object((1,3,6,1,4,1,3902,1015,5200,3,6,2,1,6),_Toneansamwotone_Type())
toneansamwotone.setMaxAccess(_E)
if mibBuilder.loadTexts:toneansamwotone.setStatus(_A)
class _Toneanswitone_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_V,0),(_W,1)))
_Toneanswitone_Type.__name__=_B
_Toneanswitone_Object=MibTableColumn
toneanswitone=_Toneanswitone_Object((1,3,6,1,4,1,3902,1015,5200,3,6,2,1,7),_Toneanswitone_Type())
toneanswitone.setMaxAccess(_E)
if mibBuilder.loadTexts:toneanswitone.setStatus(_A)
class _Toneanswotone_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_V,0),(_W,1)))
_Toneanswotone_Type.__name__=_B
_Toneanswotone_Object=MibTableColumn
toneanswotone=_Toneanswotone_Object((1,3,6,1,4,1,3902,1015,5200,3,6,2,1,8),_Toneanswotone_Type())
toneanswotone.setMaxAccess(_E)
if mibBuilder.loadTexts:toneanswotone.setStatus(_A)
class _Tonefixtonechip_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('dsp',1),('ips',2)))
_Tonefixtonechip_Type.__name__=_B
_Tonefixtonechip_Object=MibScalar
tonefixtonechip=_Tonefixtonechip_Object((1,3,6,1,4,1,3902,1015,5200,3,6,3),_Tonefixtonechip_Type())
tonefixtonechip.setMaxAccess(_E)
if mibBuilder.loadTexts:tonefixtonechip.setStatus(_A)
_MsagH248Perform_ObjectIdentity=ObjectIdentity
msagH248Perform=_MsagH248Perform_ObjectIdentity((1,3,6,1,4,1,3902,1015,5200,3,6,6))
_MsagH248PSRecMsg_Type=Integer32
_MsagH248PSRecMsg_Object=MibScalar
msagH248PSRecMsg=_MsagH248PSRecMsg_Object((1,3,6,1,4,1,3902,1015,5200,3,6,6,1),_MsagH248PSRecMsg_Type())
msagH248PSRecMsg.setMaxAccess(_F)
if mibBuilder.loadTexts:msagH248PSRecMsg.setStatus(_A)
_MsagH248PSSendMsg_Type=Integer32
_MsagH248PSSendMsg_Object=MibScalar
msagH248PSSendMsg=_MsagH248PSSendMsg_Object((1,3,6,1,4,1,3902,1015,5200,3,6,6,2),_MsagH248PSSendMsg_Type())
msagH248PSSendMsg.setMaxAccess(_F)
if mibBuilder.loadTexts:msagH248PSSendMsg.setStatus(_A)
_MsagH248PSRecMsgByte_Type=Integer32
_MsagH248PSRecMsgByte_Object=MibScalar
msagH248PSRecMsgByte=_MsagH248PSRecMsgByte_Object((1,3,6,1,4,1,3902,1015,5200,3,6,6,3),_MsagH248PSRecMsgByte_Type())
msagH248PSRecMsgByte.setMaxAccess(_F)
if mibBuilder.loadTexts:msagH248PSRecMsgByte.setStatus(_A)
_MsagH248PSSendMsgByte_Type=Integer32
_MsagH248PSSendMsgByte_Object=MibScalar
msagH248PSSendMsgByte=_MsagH248PSSendMsgByte_Object((1,3,6,1,4,1,3902,1015,5200,3,6,6,4),_MsagH248PSSendMsgByte_Type())
msagH248PSSendMsgByte.setMaxAccess(_F)
if mibBuilder.loadTexts:msagH248PSSendMsgByte.setStatus(_A)
_MsagH248PSProtocolError_Type=Integer32
_MsagH248PSProtocolError_Object=MibScalar
msagH248PSProtocolError=_MsagH248PSProtocolError_Object((1,3,6,1,4,1,3902,1015,5200,3,6,6,5),_MsagH248PSProtocolError_Type())
msagH248PSProtocolError.setMaxAccess(_F)
if mibBuilder.loadTexts:msagH248PSProtocolError.setStatus(_A)
_MsagH248PSTimerOut_Type=Integer32
_MsagH248PSTimerOut_Object=MibScalar
msagH248PSTimerOut=_MsagH248PSTimerOut_Object((1,3,6,1,4,1,3902,1015,5200,3,6,6,6),_MsagH248PSTimerOut_Type())
msagH248PSTimerOut.setMaxAccess(_F)
if mibBuilder.loadTexts:msagH248PSTimerOut.setStatus(_A)
_MsagH248PSDisconnect_Type=Integer32
_MsagH248PSDisconnect_Object=MibScalar
msagH248PSDisconnect=_MsagH248PSDisconnect_Object((1,3,6,1,4,1,3902,1015,5200,3,6,6,7),_MsagH248PSDisconnect_Type())
msagH248PSDisconnect.setMaxAccess(_F)
if mibBuilder.loadTexts:msagH248PSDisconnect.setStatus(_A)
_MsagH248PSMGCChange_Type=Integer32
_MsagH248PSMGCChange_Object=MibScalar
msagH248PSMGCChange=_MsagH248PSMGCChange_Object((1,3,6,1,4,1,3902,1015,5200,3,6,6,8),_MsagH248PSMGCChange_Type())
msagH248PSMGCChange.setMaxAccess(_F)
if mibBuilder.loadTexts:msagH248PSMGCChange.setStatus(_A)
_MsagH248PSTransmitError_Type=Integer32
_MsagH248PSTransmitError_Object=MibScalar
msagH248PSTransmitError=_MsagH248PSTransmitError_Object((1,3,6,1,4,1,3902,1015,5200,3,6,6,9),_MsagH248PSTransmitError_Type())
msagH248PSTransmitError.setMaxAccess(_F)
if mibBuilder.loadTexts:msagH248PSTransmitError.setStatus(_A)
class _Calllimitipsthruput_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_Calllimitipsthruput_Type.__name__=_U
_Calllimitipsthruput_Object=MibScalar
calllimitipsthruput=_Calllimitipsthruput_Object((1,3,6,1,4,1,3902,1015,5200,3,6,19),_Calllimitipsthruput_Type())
calllimitipsthruput.setMaxAccess(_E)
if mibBuilder.loadTexts:calllimitipsthruput.setStatus(_A)
class _Calllimitnicthruput_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_Calllimitnicthruput_Type.__name__=_U
_Calllimitnicthruput_Object=MibScalar
calllimitnicthruput=_Calllimitnicthruput_Object((1,3,6,1,4,1,3902,1015,5200,3,6,20),_Calllimitnicthruput_Type())
calllimitnicthruput.setMaxAccess(_E)
if mibBuilder.loadTexts:calllimitnicthruput.setStatus(_A)
class _Calllimitcalllimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('limitByMg',1),('limitByMgc',2),(_d,3)))
_Calllimitcalllimit_Type.__name__=_B
_Calllimitcalllimit_Object=MibScalar
calllimitcalllimit=_Calllimitcalllimit_Object((1,3,6,1,4,1,3902,1015,5200,3,6,21),_Calllimitcalllimit_Type())
calllimitcalllimit.setMaxAccess(_E)
if mibBuilder.loadTexts:calllimitcalllimit.setStatus(_A)
class _Calllimitcpubusylimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_h,1),(_d,2)))
_Calllimitcpubusylimit_Type.__name__=_B
_Calllimitcpubusylimit_Object=MibScalar
calllimitcpubusylimit=_Calllimitcpubusylimit_Object((1,3,6,1,4,1,3902,1015,5200,3,6,22),_Calllimitcpubusylimit_Type())
calllimitcpubusylimit.setMaxAccess(_E)
if mibBuilder.loadTexts:calllimitcpubusylimit.setStatus(_A)
class _Calllimitupportlimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_h,1),(_d,2)))
_Calllimitupportlimit_Type.__name__=_B
_Calllimitupportlimit_Object=MibScalar
calllimitupportlimit=_Calllimitupportlimit_Object((1,3,6,1,4,1,3902,1015,5200,3,6,23),_Calllimitupportlimit_Type())
calllimitupportlimit.setMaxAccess(_E)
if mibBuilder.loadTexts:calllimitupportlimit.setStatus(_A)
class _Calllimitipslimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_h,1),(_d,2)))
_Calllimitipslimit_Type.__name__=_B
_Calllimitipslimit_Object=MibScalar
calllimitipslimit=_Calllimitipslimit_Object((1,3,6,1,4,1,3902,1015,5200,3,6,24),_Calllimitipslimit_Type())
calllimitipslimit.setMaxAccess(_E)
if mibBuilder.loadTexts:calllimitipslimit.setStatus(_A)
class _Calllimitniclimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_h,1),(_d,2)))
_Calllimitniclimit_Type.__name__=_B
_Calllimitniclimit_Object=MibScalar
calllimitniclimit=_Calllimitniclimit_Object((1,3,6,1,4,1,3902,1015,5200,3,6,25),_Calllimitniclimit_Type())
calllimitniclimit.setMaxAccess(_E)
if mibBuilder.loadTexts:calllimitniclimit.setStatus(_A)
_MsagTrap_ObjectIdentity=ObjectIdentity
msagTrap=_MsagTrap_ObjectIdentity((1,3,6,1,4,1,3902,1015,5200,3,10))
_MsagTrapId_ObjectIdentity=ObjectIdentity
msagTrapId=_MsagTrapId_ObjectIdentity((1,3,6,1,4,1,3902,1015,5200,3,10,1))
_MsagTrapObjectMib_ObjectIdentity=ObjectIdentity
msagTrapObjectMib=_MsagTrapObjectMib_ObjectIdentity((1,3,6,1,4,1,3902,1015,5200,3,10,2))
class _ZxAnNarrowbandResCfgType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('dtmf',1),('tone',2),('ipsMprb',3),('conference',4),('ipsSixty',5),('msdti',6),('odtT1',7),('notSourceType',8)))
_ZxAnNarrowbandResCfgType_Type.__name__=_B
_ZxAnNarrowbandResCfgType_Object=MibScalar
zxAnNarrowbandResCfgType=_ZxAnNarrowbandResCfgType_Object((1,3,6,1,4,1,3902,1015,5200,3,10,2,1),_ZxAnNarrowbandResCfgType_Type())
zxAnNarrowbandResCfgType.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnNarrowbandResCfgType.setStatus(_A)
class _ZxAnNarrowbandResActType_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_ZxAnNarrowbandResActType_Type.__name__=_L
_ZxAnNarrowbandResActType_Object=MibScalar
zxAnNarrowbandResActType=_ZxAnNarrowbandResActType_Object((1,3,6,1,4,1,3902,1015,5200,3,10,2,2),_ZxAnNarrowbandResActType_Type())
zxAnNarrowbandResActType.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnNarrowbandResActType.setStatus(_A)
_ZxAnIpsResourceAlarmReason_Type=Integer32
_ZxAnIpsResourceAlarmReason_Object=MibScalar
zxAnIpsResourceAlarmReason=_ZxAnIpsResourceAlarmReason_Object((1,3,6,1,4,1,3902,1015,5200,3,10,2,3),_ZxAnIpsResourceAlarmReason_Type())
zxAnIpsResourceAlarmReason.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnIpsResourceAlarmReason.setStatus(_A)
_ZxAnTrapRack_Type=Integer32
_ZxAnTrapRack_Object=MibScalar
zxAnTrapRack=_ZxAnTrapRack_Object((1,3,6,1,4,1,3902,1015,5200,3,10,2,4),_ZxAnTrapRack_Type())
zxAnTrapRack.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnTrapRack.setStatus(_A)
_ZxAnTrapShelf_Type=Integer32
_ZxAnTrapShelf_Object=MibScalar
zxAnTrapShelf=_ZxAnTrapShelf_Object((1,3,6,1,4,1,3902,1015,5200,3,10,2,5),_ZxAnTrapShelf_Type())
zxAnTrapShelf.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnTrapShelf.setStatus(_A)
_ZxAnTrapSlot_Type=Integer32
_ZxAnTrapSlot_Object=MibScalar
zxAnTrapSlot=_ZxAnTrapSlot_Object((1,3,6,1,4,1,3902,1015,5200,3,10,2,6),_ZxAnTrapSlot_Type())
zxAnTrapSlot.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnTrapSlot.setStatus(_A)
_ZxAnTrapUnit_Type=Integer32
_ZxAnTrapUnit_Object=MibScalar
zxAnTrapUnit=_ZxAnTrapUnit_Object((1,3,6,1,4,1,3902,1015,5200,3,10,2,7),_ZxAnTrapUnit_Type())
zxAnTrapUnit.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnTrapUnit.setStatus(_A)
_ZxAnTrapSunit_Type=Integer32
_ZxAnTrapSunit_Object=MibScalar
zxAnTrapSunit=_ZxAnTrapSunit_Object((1,3,6,1,4,1,3902,1015,5200,3,10,2,8),_ZxAnTrapSunit_Type())
zxAnTrapSunit.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnTrapSunit.setStatus(_A)
_ZxAnTrapPort_Type=Integer32
_ZxAnTrapPort_Object=MibScalar
zxAnTrapPort=_ZxAnTrapPort_Object((1,3,6,1,4,1,3902,1015,5200,3,10,2,9),_ZxAnTrapPort_Type())
zxAnTrapPort.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnTrapPort.setStatus(_A)
_MsagTrapReason_Type=Integer32
_MsagTrapReason_Object=MibScalar
msagTrapReason=_MsagTrapReason_Object((1,3,6,1,4,1,3902,1015,5200,3,10,2,10),_MsagTrapReason_Type())
msagTrapReason.setMaxAccess(_F)
if mibBuilder.loadTexts:msagTrapReason.setStatus(_A)
_MsagTrapLinkState_Type=Integer32
_MsagTrapLinkState_Object=MibScalar
msagTrapLinkState=_MsagTrapLinkState_Object((1,3,6,1,4,1,3902,1015,5200,3,10,2,11),_MsagTrapLinkState_Type())
msagTrapLinkState.setMaxAccess(_F)
if mibBuilder.loadTexts:msagTrapLinkState.setStatus(_A)
_MsagTrapMgcNo_Type=Integer32
_MsagTrapMgcNo_Object=MibScalar
msagTrapMgcNo=_MsagTrapMgcNo_Object((1,3,6,1,4,1,3902,1015,5200,3,10,2,12),_MsagTrapMgcNo_Type())
msagTrapMgcNo.setMaxAccess(_F)
if mibBuilder.loadTexts:msagTrapMgcNo.setStatus(_A)
_MsagTrapSLN_Type=Integer32
_MsagTrapSLN_Object=MibScalar
msagTrapSLN=_MsagTrapSLN_Object((1,3,6,1,4,1,3902,1015,5200,3,10,2,13),_MsagTrapSLN_Type())
msagTrapSLN.setMaxAccess(_F)
if mibBuilder.loadTexts:msagTrapSLN.setStatus(_A)
_MsagTrapFlag_Type=Integer32
_MsagTrapFlag_Object=MibScalar
msagTrapFlag=_MsagTrapFlag_Object((1,3,6,1,4,1,3902,1015,5200,3,10,2,14),_MsagTrapFlag_Type())
msagTrapFlag.setMaxAccess(_F)
if mibBuilder.loadTexts:msagTrapFlag.setStatus(_A)
_MsagTrapErrcode_Type=Integer32
_MsagTrapErrcode_Object=MibScalar
msagTrapErrcode=_MsagTrapErrcode_Object((1,3,6,1,4,1,3902,1015,5200,3,10,2,15),_MsagTrapErrcode_Type())
msagTrapErrcode.setMaxAccess(_F)
if mibBuilder.loadTexts:msagTrapErrcode.setStatus(_A)
_MsagTrapIpAddress_Type=Integer32
_MsagTrapIpAddress_Object=MibScalar
msagTrapIpAddress=_MsagTrapIpAddress_Object((1,3,6,1,4,1,3902,1015,5200,3,10,2,16),_MsagTrapIpAddress_Type())
msagTrapIpAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:msagTrapIpAddress.setStatus(_A)
_MsagTrapBETime_Type=Integer32
_MsagTrapBETime_Object=MibScalar
msagTrapBETime=_MsagTrapBETime_Object((1,3,6,1,4,1,3902,1015,5200,3,10,2,17),_MsagTrapBETime_Type())
msagTrapBETime.setMaxAccess(_F)
if mibBuilder.loadTexts:msagTrapBETime.setStatus(_A)
class _ZxAnTrapInfoType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('ei2',1),('ei3',2),('lsl',3),('rsy',4),('fj',5)))
_ZxAnTrapInfoType_Type.__name__=_B
_ZxAnTrapInfoType_Object=MibScalar
zxAnTrapInfoType=_ZxAnTrapInfoType_Object((1,3,6,1,4,1,3902,1015,5200,3,10,2,18),_ZxAnTrapInfoType_Type())
zxAnTrapInfoType.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnTrapInfoType.setStatus(_A)
_MsagTrapUnitNo_Type=Integer32
_MsagTrapUnitNo_Object=MibScalar
msagTrapUnitNo=_MsagTrapUnitNo_Object((1,3,6,1,4,1,3902,1015,5200,3,10,2,19),_MsagTrapUnitNo_Type())
msagTrapUnitNo.setMaxAccess(_F)
if mibBuilder.loadTexts:msagTrapUnitNo.setStatus(_A)
_MsagTrapPcmNo_Type=Integer32
_MsagTrapPcmNo_Object=MibScalar
msagTrapPcmNo=_MsagTrapPcmNo_Object((1,3,6,1,4,1,3902,1015,5200,3,10,2,20),_MsagTrapPcmNo_Type())
msagTrapPcmNo.setMaxAccess(_F)
if mibBuilder.loadTexts:msagTrapPcmNo.setStatus(_A)
_MsagTrapReasionValue_Type=Integer32
_MsagTrapReasionValue_Object=MibScalar
msagTrapReasionValue=_MsagTrapReasionValue_Object((1,3,6,1,4,1,3902,1015,5200,3,10,2,21),_MsagTrapReasionValue_Type())
msagTrapReasionValue.setMaxAccess(_F)
if mibBuilder.loadTexts:msagTrapReasionValue.setStatus(_A)
_MsagTrapRack_Type=Integer32
_MsagTrapRack_Object=MibScalar
msagTrapRack=_MsagTrapRack_Object((1,3,6,1,4,1,3902,1015,5200,3,10,2,22),_MsagTrapRack_Type())
msagTrapRack.setMaxAccess(_F)
if mibBuilder.loadTexts:msagTrapRack.setStatus(_A)
_MsagTrapShelf_Type=Integer32
_MsagTrapShelf_Object=MibScalar
msagTrapShelf=_MsagTrapShelf_Object((1,3,6,1,4,1,3902,1015,5200,3,10,2,23),_MsagTrapShelf_Type())
msagTrapShelf.setMaxAccess(_F)
if mibBuilder.loadTexts:msagTrapShelf.setStatus(_A)
_MsagTrapSlot_Type=Integer32
_MsagTrapSlot_Object=MibScalar
msagTrapSlot=_MsagTrapSlot_Object((1,3,6,1,4,1,3902,1015,5200,3,10,2,24),_MsagTrapSlot_Type())
msagTrapSlot.setMaxAccess(_F)
if mibBuilder.loadTexts:msagTrapSlot.setStatus(_A)
_MsagTrapV5InterId_Type=Integer32
_MsagTrapV5InterId_Object=MibScalar
msagTrapV5InterId=_MsagTrapV5InterId_Object((1,3,6,1,4,1,3902,1015,5200,3,10,2,25),_MsagTrapV5InterId_Type())
msagTrapV5InterId.setMaxAccess(_F)
if mibBuilder.loadTexts:msagTrapV5InterId.setStatus(_A)
_MsagTrapDLProType_Type=Integer32
_MsagTrapDLProType_Object=MibScalar
msagTrapDLProType=_MsagTrapDLProType_Object((1,3,6,1,4,1,3902,1015,5200,3,10,2,26),_MsagTrapDLProType_Type())
msagTrapDLProType.setMaxAccess(_F)
if mibBuilder.loadTexts:msagTrapDLProType.setStatus(_A)
_MsagTrapCurEvent_Type=Integer32
_MsagTrapCurEvent_Object=MibScalar
msagTrapCurEvent=_MsagTrapCurEvent_Object((1,3,6,1,4,1,3902,1015,5200,3,10,2,27),_MsagTrapCurEvent_Type())
msagTrapCurEvent.setMaxAccess(_F)
if mibBuilder.loadTexts:msagTrapCurEvent.setStatus(_A)
_MsagTrapCurState_Type=Integer32
_MsagTrapCurState_Object=MibScalar
msagTrapCurState=_MsagTrapCurState_Object((1,3,6,1,4,1,3902,1015,5200,3,10,2,28),_MsagTrapCurState_Type())
msagTrapCurState.setMaxAccess(_F)
if mibBuilder.loadTexts:msagTrapCurState.setStatus(_A)
_MsagTrapParaLinkId_Type=Integer32
_MsagTrapParaLinkId_Object=MibScalar
msagTrapParaLinkId=_MsagTrapParaLinkId_Object((1,3,6,1,4,1,3902,1015,5200,3,10,2,29),_MsagTrapParaLinkId_Type())
msagTrapParaLinkId.setMaxAccess(_F)
if mibBuilder.loadTexts:msagTrapParaLinkId.setStatus(_A)
_MsagQosAlarmType_Type=Integer32
_MsagQosAlarmType_Object=MibScalar
msagQosAlarmType=_MsagQosAlarmType_Object((1,3,6,1,4,1,3902,1015,5200,3,10,2,30),_MsagQosAlarmType_Type())
msagQosAlarmType.setMaxAccess(_F)
if mibBuilder.loadTexts:msagQosAlarmType.setStatus(_A)
_MsagQosAlarmDetail_Type=Integer32
_MsagQosAlarmDetail_Object=MibScalar
msagQosAlarmDetail=_MsagQosAlarmDetail_Object((1,3,6,1,4,1,3902,1015,5200,3,10,2,31),_MsagQosAlarmDetail_Type())
msagQosAlarmDetail.setMaxAccess(_F)
if mibBuilder.loadTexts:msagQosAlarmDetail.setStatus(_A)
_MsagTrapPort_Type=Integer32
_MsagTrapPort_Object=MibScalar
msagTrapPort=_MsagTrapPort_Object((1,3,6,1,4,1,3902,1015,5200,3,10,2,32),_MsagTrapPort_Type())
msagTrapPort.setMaxAccess(_F)
if mibBuilder.loadTexts:msagTrapPort.setStatus(_A)
_ZxAnVoipCallTest_ObjectIdentity=ObjectIdentity
zxAnVoipCallTest=_ZxAnVoipCallTest_ObjectIdentity((1,3,6,1,4,1,3902,1015,5200,3,12))
_ZxAnVoipCalleeTestTable_Object=MibTable
zxAnVoipCalleeTestTable=_ZxAnVoipCalleeTestTable_Object((1,3,6,1,4,1,3902,1015,5200,3,12,1))
if mibBuilder.loadTexts:zxAnVoipCalleeTestTable.setStatus(_A)
_ZxAnVoipCalleeTestEntry_Object=MibTableRow
zxAnVoipCalleeTestEntry=_ZxAnVoipCalleeTestEntry_Object((1,3,6,1,4,1,3902,1015,5200,3,12,1,1))
zxAnVoipCalleeTestEntry.setIndexNames((0,_C,_AV),(0,_C,_AW),(0,_C,_AX),(0,_C,_AY),(0,_C,_AZ),(0,_C,_Aa),(0,_C,_Ab))
if mibBuilder.loadTexts:zxAnVoipCalleeTestEntry.setStatus(_A)
_ZxAnVoipCalleeTestRack_Type=Integer32
_ZxAnVoipCalleeTestRack_Object=MibTableColumn
zxAnVoipCalleeTestRack=_ZxAnVoipCalleeTestRack_Object((1,3,6,1,4,1,3902,1015,5200,3,12,1,1,1),_ZxAnVoipCalleeTestRack_Type())
zxAnVoipCalleeTestRack.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnVoipCalleeTestRack.setStatus(_A)
_ZxAnVoipCalleeTestShelf_Type=Integer32
_ZxAnVoipCalleeTestShelf_Object=MibTableColumn
zxAnVoipCalleeTestShelf=_ZxAnVoipCalleeTestShelf_Object((1,3,6,1,4,1,3902,1015,5200,3,12,1,1,2),_ZxAnVoipCalleeTestShelf_Type())
zxAnVoipCalleeTestShelf.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnVoipCalleeTestShelf.setStatus(_A)
_ZxAnVoipCalleeTestSlot_Type=Integer32
_ZxAnVoipCalleeTestSlot_Object=MibTableColumn
zxAnVoipCalleeTestSlot=_ZxAnVoipCalleeTestSlot_Object((1,3,6,1,4,1,3902,1015,5200,3,12,1,1,3),_ZxAnVoipCalleeTestSlot_Type())
zxAnVoipCalleeTestSlot.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnVoipCalleeTestSlot.setStatus(_A)
_ZxAnVoipCalleeTestPort_Type=Integer32
_ZxAnVoipCalleeTestPort_Object=MibTableColumn
zxAnVoipCalleeTestPort=_ZxAnVoipCalleeTestPort_Object((1,3,6,1,4,1,3902,1015,5200,3,12,1,1,4),_ZxAnVoipCalleeTestPort_Type())
zxAnVoipCalleeTestPort.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnVoipCalleeTestPort.setStatus(_A)
_ZxAnVoipCalleeTestOnu_Type=Integer32
_ZxAnVoipCalleeTestOnu_Object=MibTableColumn
zxAnVoipCalleeTestOnu=_ZxAnVoipCalleeTestOnu_Object((1,3,6,1,4,1,3902,1015,5200,3,12,1,1,5),_ZxAnVoipCalleeTestOnu_Type())
zxAnVoipCalleeTestOnu.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnVoipCalleeTestOnu.setStatus(_A)
class _ZxAnVoipCalleeTestCircuitType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,11)));namedValues=NamedValues(*((_Ac,1),(_Ad,2),('onu',3),(_Ae,4),('onuUni',5),(_Af,11)))
_ZxAnVoipCalleeTestCircuitType_Type.__name__=_B
_ZxAnVoipCalleeTestCircuitType_Object=MibTableColumn
zxAnVoipCalleeTestCircuitType=_ZxAnVoipCalleeTestCircuitType_Object((1,3,6,1,4,1,3902,1015,5200,3,12,1,1,6),_ZxAnVoipCalleeTestCircuitType_Type())
zxAnVoipCalleeTestCircuitType.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnVoipCalleeTestCircuitType.setStatus(_A)
_ZxAnVoipCalleeTestLogicalId_Type=ObjectIdentifier
_ZxAnVoipCalleeTestLogicalId_Object=MibTableColumn
zxAnVoipCalleeTestLogicalId=_ZxAnVoipCalleeTestLogicalId_Object((1,3,6,1,4,1,3902,1015,5200,3,12,1,1,7),_ZxAnVoipCalleeTestLogicalId_Type())
zxAnVoipCalleeTestLogicalId.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnVoipCalleeTestLogicalId.setStatus(_A)
class _ZxAnVoipCalleeTestAction_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('start',1),('stop',2)))
_ZxAnVoipCalleeTestAction_Type.__name__=_B
_ZxAnVoipCalleeTestAction_Object=MibTableColumn
zxAnVoipCalleeTestAction=_ZxAnVoipCalleeTestAction_Object((1,3,6,1,4,1,3902,1015,5200,3,12,1,1,8),_ZxAnVoipCalleeTestAction_Type())
zxAnVoipCalleeTestAction.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnVoipCalleeTestAction.setStatus(_A)
class _ZxAnVoipCalleeTestTimeout_Type(Integer32):defaultValue=90;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,300))
_ZxAnVoipCalleeTestTimeout_Type.__name__=_B
_ZxAnVoipCalleeTestTimeout_Object=MibTableColumn
zxAnVoipCalleeTestTimeout=_ZxAnVoipCalleeTestTimeout_Object((1,3,6,1,4,1,3902,1015,5200,3,12,1,1,9),_ZxAnVoipCalleeTestTimeout_Type())
zxAnVoipCalleeTestTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnVoipCalleeTestTimeout.setStatus(_A)
if mibBuilder.loadTexts:zxAnVoipCalleeTestTimeout.setUnits('seconds')
class _ZxAnVoipCalleeTestStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_j,1),(_k,2),(_l,3),(_m,4)))
_ZxAnVoipCalleeTestStatus_Type.__name__=_B
_ZxAnVoipCalleeTestStatus_Object=MibTableColumn
zxAnVoipCalleeTestStatus=_ZxAnVoipCalleeTestStatus_Object((1,3,6,1,4,1,3902,1015,5200,3,12,1,1,10),_ZxAnVoipCalleeTestStatus_Type())
zxAnVoipCalleeTestStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnVoipCalleeTestStatus.setStatus(_A)
class _ZxAnVoipCalleeTestPortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('idle',1),('ringing',2),('offHook',3),(_Ag,4),(_i,5),('onHook',6),('testEnd',7)))
_ZxAnVoipCalleeTestPortStatus_Type.__name__=_B
_ZxAnVoipCalleeTestPortStatus_Object=MibTableColumn
zxAnVoipCalleeTestPortStatus=_ZxAnVoipCalleeTestPortStatus_Object((1,3,6,1,4,1,3902,1015,5200,3,12,1,1,11),_ZxAnVoipCalleeTestPortStatus_Type())
zxAnVoipCalleeTestPortStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnVoipCalleeTestPortStatus.setStatus(_A)
class _ZxAnVoipCalleeTestFailReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('other',1),('noRing',2),(_Ah,3),(_Ai,4),(_Aj,5),('ringReleasedEarly',6),('noDigit',7),(_Ak,8)))
_ZxAnVoipCalleeTestFailReason_Type.__name__=_B
_ZxAnVoipCalleeTestFailReason_Object=MibTableColumn
zxAnVoipCalleeTestFailReason=_ZxAnVoipCalleeTestFailReason_Object((1,3,6,1,4,1,3902,1015,5200,3,12,1,1,12),_ZxAnVoipCalleeTestFailReason_Type())
zxAnVoipCalleeTestFailReason.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnVoipCalleeTestFailReason.setStatus(_A)
class _ZxAnVoipCalleeTestFailDetail_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_ZxAnVoipCalleeTestFailDetail_Type.__name__=_L
_ZxAnVoipCalleeTestFailDetail_Object=MibTableColumn
zxAnVoipCalleeTestFailDetail=_ZxAnVoipCalleeTestFailDetail_Object((1,3,6,1,4,1,3902,1015,5200,3,12,1,1,13),_ZxAnVoipCalleeTestFailDetail_Type())
zxAnVoipCalleeTestFailDetail.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnVoipCalleeTestFailDetail.setStatus(_A)
_ZxAnVoipCalleeTestRowStatus_Type=RowStatus
_ZxAnVoipCalleeTestRowStatus_Object=MibTableColumn
zxAnVoipCalleeTestRowStatus=_ZxAnVoipCalleeTestRowStatus_Object((1,3,6,1,4,1,3902,1015,5200,3,12,1,1,50),_ZxAnVoipCalleeTestRowStatus_Type())
zxAnVoipCalleeTestRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnVoipCalleeTestRowStatus.setStatus(_A)
_ZxAnVoipCallerTestTable_Object=MibTable
zxAnVoipCallerTestTable=_ZxAnVoipCallerTestTable_Object((1,3,6,1,4,1,3902,1015,5200,3,12,2))
if mibBuilder.loadTexts:zxAnVoipCallerTestTable.setStatus(_A)
_ZxAnVoipCallerTestEntry_Object=MibTableRow
zxAnVoipCallerTestEntry=_ZxAnVoipCallerTestEntry_Object((1,3,6,1,4,1,3902,1015,5200,3,12,2,1))
zxAnVoipCallerTestEntry.setIndexNames((0,_C,_Al),(0,_C,_Am),(0,_C,_An),(0,_C,_Ao),(0,_C,_Ap),(0,_C,_Aq),(0,_C,_Ar))
if mibBuilder.loadTexts:zxAnVoipCallerTestEntry.setStatus(_A)
_ZxAnVoipCallerTestRack_Type=Integer32
_ZxAnVoipCallerTestRack_Object=MibTableColumn
zxAnVoipCallerTestRack=_ZxAnVoipCallerTestRack_Object((1,3,6,1,4,1,3902,1015,5200,3,12,2,1,1),_ZxAnVoipCallerTestRack_Type())
zxAnVoipCallerTestRack.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnVoipCallerTestRack.setStatus(_A)
_ZxAnVoipCallerTestShelf_Type=Integer32
_ZxAnVoipCallerTestShelf_Object=MibTableColumn
zxAnVoipCallerTestShelf=_ZxAnVoipCallerTestShelf_Object((1,3,6,1,4,1,3902,1015,5200,3,12,2,1,2),_ZxAnVoipCallerTestShelf_Type())
zxAnVoipCallerTestShelf.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnVoipCallerTestShelf.setStatus(_A)
_ZxAnVoipCallerTestSlot_Type=Integer32
_ZxAnVoipCallerTestSlot_Object=MibTableColumn
zxAnVoipCallerTestSlot=_ZxAnVoipCallerTestSlot_Object((1,3,6,1,4,1,3902,1015,5200,3,12,2,1,3),_ZxAnVoipCallerTestSlot_Type())
zxAnVoipCallerTestSlot.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnVoipCallerTestSlot.setStatus(_A)
_ZxAnVoipCallerTestPort_Type=Integer32
_ZxAnVoipCallerTestPort_Object=MibTableColumn
zxAnVoipCallerTestPort=_ZxAnVoipCallerTestPort_Object((1,3,6,1,4,1,3902,1015,5200,3,12,2,1,4),_ZxAnVoipCallerTestPort_Type())
zxAnVoipCallerTestPort.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnVoipCallerTestPort.setStatus(_A)
_ZxAnVoipCallerTestOnu_Type=Integer32
_ZxAnVoipCallerTestOnu_Object=MibTableColumn
zxAnVoipCallerTestOnu=_ZxAnVoipCallerTestOnu_Object((1,3,6,1,4,1,3902,1015,5200,3,12,2,1,5),_ZxAnVoipCallerTestOnu_Type())
zxAnVoipCallerTestOnu.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnVoipCallerTestOnu.setStatus(_A)
class _ZxAnVoipCallerTestCircuitType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,11)));namedValues=NamedValues(*((_Ac,1),(_Ad,2),('onu',3),(_Ae,4),('onuUni',5),(_Af,11)))
_ZxAnVoipCallerTestCircuitType_Type.__name__=_B
_ZxAnVoipCallerTestCircuitType_Object=MibTableColumn
zxAnVoipCallerTestCircuitType=_ZxAnVoipCallerTestCircuitType_Object((1,3,6,1,4,1,3902,1015,5200,3,12,2,1,6),_ZxAnVoipCallerTestCircuitType_Type())
zxAnVoipCallerTestCircuitType.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnVoipCallerTestCircuitType.setStatus(_A)
_ZxAnVoipCallerTestLogicalId_Type=ObjectIdentifier
_ZxAnVoipCallerTestLogicalId_Object=MibTableColumn
zxAnVoipCallerTestLogicalId=_ZxAnVoipCallerTestLogicalId_Object((1,3,6,1,4,1,3902,1015,5200,3,12,2,1,7),_ZxAnVoipCallerTestLogicalId_Type())
zxAnVoipCallerTestLogicalId.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnVoipCallerTestLogicalId.setStatus(_A)
class _ZxAnVoipCallerTestAction_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('start',1),('stop',2)))
_ZxAnVoipCallerTestAction_Type.__name__=_B
_ZxAnVoipCallerTestAction_Object=MibTableColumn
zxAnVoipCallerTestAction=_ZxAnVoipCallerTestAction_Object((1,3,6,1,4,1,3902,1015,5200,3,12,2,1,8),_ZxAnVoipCallerTestAction_Type())
zxAnVoipCallerTestAction.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnVoipCallerTestAction.setStatus(_A)
class _ZxAnVoipCallerTestTimeout_Type(Integer32):defaultValue=90;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,300))
_ZxAnVoipCallerTestTimeout_Type.__name__=_B
_ZxAnVoipCallerTestTimeout_Object=MibTableColumn
zxAnVoipCallerTestTimeout=_ZxAnVoipCallerTestTimeout_Object((1,3,6,1,4,1,3902,1015,5200,3,12,2,1,9),_ZxAnVoipCallerTestTimeout_Type())
zxAnVoipCallerTestTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnVoipCallerTestTimeout.setStatus(_A)
if mibBuilder.loadTexts:zxAnVoipCallerTestTimeout.setUnits('seconds')
class _ZxAnVoipCallerTestDialedNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_ZxAnVoipCallerTestDialedNumber_Type.__name__=_L
_ZxAnVoipCallerTestDialedNumber_Object=MibTableColumn
zxAnVoipCallerTestDialedNumber=_ZxAnVoipCallerTestDialedNumber_Object((1,3,6,1,4,1,3902,1015,5200,3,12,2,1,10),_ZxAnVoipCallerTestDialedNumber_Type())
zxAnVoipCallerTestDialedNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnVoipCallerTestDialedNumber.setStatus(_A)
class _ZxAnVoipCallerTestStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_j,1),(_k,2),(_l,3),(_m,4),('notForced',5)))
_ZxAnVoipCallerTestStatus_Type.__name__=_B
_ZxAnVoipCallerTestStatus_Object=MibTableColumn
zxAnVoipCallerTestStatus=_ZxAnVoipCallerTestStatus_Object((1,3,6,1,4,1,3902,1015,5200,3,12,2,1,11),_ZxAnVoipCallerTestStatus_Type())
zxAnVoipCallerTestStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnVoipCallerTestStatus.setStatus(_A)
class _ZxAnVoipCallerTestPortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('idle',1),('offHook',2),('dialTone',3),('receiveNumber',4),('receiveEnd',5),('ringBackTone',6),(_Ag,7),(_i,8),('onHook',9),('testEnd',10)))
_ZxAnVoipCallerTestPortStatus_Type.__name__=_B
_ZxAnVoipCallerTestPortStatus_Object=MibTableColumn
zxAnVoipCallerTestPortStatus=_ZxAnVoipCallerTestPortStatus_Object((1,3,6,1,4,1,3902,1015,5200,3,12,2,1,12),_ZxAnVoipCallerTestPortStatus_Type())
zxAnVoipCallerTestPortStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnVoipCallerTestPortStatus.setStatus(_A)
class _ZxAnVoipCallerTestFailReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('other',1),('noDialTone',2),('noRingBack',3),('noAnswer',4),(_Ah,5),(_Ai,6),(_Aj,7),('sipTestFailed',8),('noDigit',9),(_Ak,10)))
_ZxAnVoipCallerTestFailReason_Type.__name__=_B
_ZxAnVoipCallerTestFailReason_Object=MibTableColumn
zxAnVoipCallerTestFailReason=_ZxAnVoipCallerTestFailReason_Object((1,3,6,1,4,1,3902,1015,5200,3,12,2,1,13),_ZxAnVoipCallerTestFailReason_Type())
zxAnVoipCallerTestFailReason.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnVoipCallerTestFailReason.setStatus(_A)
class _ZxAnVoipCallerTestFailDetail_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_ZxAnVoipCallerTestFailDetail_Type.__name__=_L
_ZxAnVoipCallerTestFailDetail_Object=MibTableColumn
zxAnVoipCallerTestFailDetail=_ZxAnVoipCallerTestFailDetail_Object((1,3,6,1,4,1,3902,1015,5200,3,12,2,1,14),_ZxAnVoipCallerTestFailDetail_Type())
zxAnVoipCallerTestFailDetail.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnVoipCallerTestFailDetail.setStatus(_A)
class _ZxAnVoipCallerTestSipFailReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*(('inviteOkButNoBearerData',1),('callTimeoutNo200Ok',2),('noResponseToInvite',3),('errorCodeAndReasonPhrase',4),('callCancelledByServer',5),('callCancelledByOnt',6),('lineNotConfigured',7),('lineNotInValidState',8),('lineNotRegistered',9),('notchFiltersRequired',10),('dialToneTestFailure',11)))
_ZxAnVoipCallerTestSipFailReason_Type.__name__=_B
_ZxAnVoipCallerTestSipFailReason_Object=MibTableColumn
zxAnVoipCallerTestSipFailReason=_ZxAnVoipCallerTestSipFailReason_Object((1,3,6,1,4,1,3902,1015,5200,3,12,2,1,15),_ZxAnVoipCallerTestSipFailReason_Type())
zxAnVoipCallerTestSipFailReason.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnVoipCallerTestSipFailReason.setStatus(_A)
class _ZxAnVoipCallerTestSipErrorCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13)));namedValues=NamedValues(*(('unauthorized',1),('forbidden',2),('notFound',3),('proxyAuthenticationRequired',4),('requestTimeout',5),('temporarilyUnavailable',6),('addressIncomplete',7),('busyHere',8),('requestTerminated',9),('notAcceptableHere',10),('serverInternalError',11),('serviceUnavailable',12),('serverTimeout',13)))
_ZxAnVoipCallerTestSipErrorCode_Type.__name__=_B
_ZxAnVoipCallerTestSipErrorCode_Object=MibTableColumn
zxAnVoipCallerTestSipErrorCode=_ZxAnVoipCallerTestSipErrorCode_Object((1,3,6,1,4,1,3902,1015,5200,3,12,2,1,16),_ZxAnVoipCallerTestSipErrorCode_Type())
zxAnVoipCallerTestSipErrorCode.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnVoipCallerTestSipErrorCode.setStatus(_A)
class _ZxAnVoipCallerTestSipDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ZxAnVoipCallerTestSipDelay_Type.__name__=_B
_ZxAnVoipCallerTestSipDelay_Object=MibTableColumn
zxAnVoipCallerTestSipDelay=_ZxAnVoipCallerTestSipDelay_Object((1,3,6,1,4,1,3902,1015,5200,3,12,2,1,17),_ZxAnVoipCallerTestSipDelay_Type())
zxAnVoipCallerTestSipDelay.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnVoipCallerTestSipDelay.setStatus(_A)
if mibBuilder.loadTexts:zxAnVoipCallerTestSipDelay.setUnits('0.1second')
class _ZxAnVoipCallerTestMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('interactive',1),('nonInteractive',2)))
_ZxAnVoipCallerTestMode_Type.__name__=_B
_ZxAnVoipCallerTestMode_Object=MibTableColumn
zxAnVoipCallerTestMode=_ZxAnVoipCallerTestMode_Object((1,3,6,1,4,1,3902,1015,5200,3,12,2,1,18),_ZxAnVoipCallerTestMode_Type())
zxAnVoipCallerTestMode.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnVoipCallerTestMode.setStatus(_A)
_ZxAnVoipCallerTestRowStatus_Type=RowStatus
_ZxAnVoipCallerTestRowStatus_Object=MibTableColumn
zxAnVoipCallerTestRowStatus=_ZxAnVoipCallerTestRowStatus_Object((1,3,6,1,4,1,3902,1015,5200,3,12,2,1,50),_ZxAnVoipCallerTestRowStatus_Type())
zxAnVoipCallerTestRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnVoipCallerTestRowStatus.setStatus(_A)
zxAnNarrowbandResAvailable=NotificationType((1,3,6,1,4,1,3902,1015,5200,3,10,1,1))
zxAnNarrowbandResAvailable.setObjects(*((_C,_n),(_C,_o)))
if mibBuilder.loadTexts:zxAnNarrowbandResAvailable.setStatus(_A)
zxAnNarrowbandResUnavailable=NotificationType((1,3,6,1,4,1,3902,1015,5200,3,10,1,2))
zxAnNarrowbandResUnavailable.setObjects(*((_C,_n),(_C,_o)))
if mibBuilder.loadTexts:zxAnNarrowbandResUnavailable.setStatus(_A)
zxAnIpsResource=NotificationType((1,3,6,1,4,1,3902,1015,5200,3,10,1,3))
zxAnIpsResource.setObjects(*((_C,_p),(_C,_q),(_C,_r)))
if mibBuilder.loadTexts:zxAnIpsResource.setStatus(_A)
zxAnIpsResourceRestore=NotificationType((1,3,6,1,4,1,3902,1015,5200,3,10,1,4))
zxAnIpsResourceRestore.setObjects(*((_C,_p),(_C,_q),(_C,_r)))
if mibBuilder.loadTexts:zxAnIpsResourceRestore.setStatus(_A)
zxAnIpsChannelFault=NotificationType((1,3,6,1,4,1,3902,1015,5200,3,10,1,5))
zxAnIpsChannelFault.setObjects(*((_C,_e),(_C,_f),(_C,_H)))
if mibBuilder.loadTexts:zxAnIpsChannelFault.setStatus(_A)
zxAnIpsChannelFaultRestore=NotificationType((1,3,6,1,4,1,3902,1015,5200,3,10,1,6))
zxAnIpsChannelFaultRestore.setObjects(*((_C,_e),(_C,_f),(_C,_H)))
if mibBuilder.loadTexts:zxAnIpsChannelFaultRestore.setStatus(_A)
zxMsagH248Link=NotificationType((1,3,6,1,4,1,3902,1015,5200,3,10,1,7))
zxMsagH248Link.setObjects(*((_C,_O),(_C,_X),(_C,_Y)))
if mibBuilder.loadTexts:zxMsagH248Link.setStatus(_A)
zxMsagH248LinkRestore=NotificationType((1,3,6,1,4,1,3902,1015,5200,3,10,1,8))
zxMsagH248LinkRestore.setObjects(*((_C,_O),(_C,_X),(_C,_Y)))
if mibBuilder.loadTexts:zxMsagH248LinkRestore.setStatus(_A)
zxMsagH248ErrorCode=NotificationType((1,3,6,1,4,1,3902,1015,5200,3,10,1,9))
zxMsagH248ErrorCode.setObjects(*((_C,_As),(_C,_I),(_C,_J),(_C,_K),(_C,_H)))
if mibBuilder.loadTexts:zxMsagH248ErrorCode.setStatus(_A)
zxAnDlccNT1Los=NotificationType((1,3,6,1,4,1,3902,1015,5200,3,10,1,10))
zxAnDlccNT1Los.setObjects(*((_C,_I),(_C,_J),(_C,_K),(_C,_H),(_C,_At)))
if mibBuilder.loadTexts:zxAnDlccNT1Los.setStatus(_A)
zxMsagMgcpLink=NotificationType((1,3,6,1,4,1,3902,1015,5200,3,10,1,11))
zxMsagMgcpLink.setObjects(*((_C,_O),(_C,_X),(_C,_Y)))
if mibBuilder.loadTexts:zxMsagMgcpLink.setStatus(_A)
zxMsagMgcpLinkRestore=NotificationType((1,3,6,1,4,1,3902,1015,5200,3,10,1,12))
zxMsagMgcpLinkRestore.setObjects(*((_C,_O),(_C,_X),(_C,_Y)))
if mibBuilder.loadTexts:zxMsagMgcpLinkRestore.setStatus(_A)
zxMsagMgcpAbnormal=NotificationType((1,3,6,1,4,1,3902,1015,5200,3,10,1,13))
zxMsagMgcpAbnormal.setObjects(*((_C,_O),(_C,_X),(_C,_Y)))
if mibBuilder.loadTexts:zxMsagMgcpAbnormal.setStatus(_A)
zxMsagMgcpAbnormalRestore=NotificationType((1,3,6,1,4,1,3902,1015,5200,3,10,1,14))
zxMsagMgcpAbnormalRestore.setObjects(*((_C,_O),(_C,_X),(_C,_Y)))
if mibBuilder.loadTexts:zxMsagMgcpAbnormalRestore.setStatus(_A)
zxMsagV5Pcm=NotificationType((1,3,6,1,4,1,3902,1015,5200,3,10,1,15))
zxMsagV5Pcm.setObjects(*((_C,_s),(_C,_t),(_C,_u)))
if mibBuilder.loadTexts:zxMsagV5Pcm.setStatus(_A)
zxMsagV5PcmRestore=NotificationType((1,3,6,1,4,1,3902,1015,5200,3,10,1,16))
zxMsagV5PcmRestore.setObjects(*((_C,_s),(_C,_t),(_C,_u)))
if mibBuilder.loadTexts:zxMsagV5PcmRestore.setStatus(_A)
zxMsagV5Proto=NotificationType((1,3,6,1,4,1,3902,1015,5200,3,10,1,17))
zxMsagV5Proto.setObjects(*((_C,_v),(_C,_w),(_C,_x),(_C,_y)))
if mibBuilder.loadTexts:zxMsagV5Proto.setStatus(_A)
zxMsagV5ProtoRestore=NotificationType((1,3,6,1,4,1,3902,1015,5200,3,10,1,18))
zxMsagV5ProtoRestore.setObjects(*((_C,_v),(_C,_w),(_C,_x),(_C,_y)))
if mibBuilder.loadTexts:zxMsagV5ProtoRestore.setStatus(_A)
zxMsagISDNSctpInform=NotificationType((1,3,6,1,4,1,3902,1015,5200,3,10,1,19))
zxMsagISDNSctpInform.setObjects(*((_C,_O),(_C,_Au),(_C,_Av)))
if mibBuilder.loadTexts:zxMsagISDNSctpInform.setStatus(_A)
zxMsagISDNSctpAlarm=NotificationType((1,3,6,1,4,1,3902,1015,5200,3,10,1,20))
zxMsagISDNSctpAlarm.setObjects((_C,_O))
if mibBuilder.loadTexts:zxMsagISDNSctpAlarm.setStatus(_A)
zxMsagIUAInform=NotificationType((1,3,6,1,4,1,3902,1015,5200,3,10,1,21))
zxMsagIUAInform.setObjects((_C,_O))
if mibBuilder.loadTexts:zxMsagIUAInform.setStatus(_A)
zxMsagIUAAlarm=NotificationType((1,3,6,1,4,1,3902,1015,5200,3,10,1,22))
zxMsagIUAAlarm.setObjects((_C,_O))
if mibBuilder.loadTexts:zxMsagIUAAlarm.setStatus(_A)
zxMsagIUAAlarmRestore=NotificationType((1,3,6,1,4,1,3902,1015,5200,3,10,1,23))
zxMsagIUAAlarmRestore.setObjects((_C,_O))
if mibBuilder.loadTexts:zxMsagIUAAlarmRestore.setStatus(_A)
zxMsagCallAllocMemoryErrorAlarm=NotificationType((1,3,6,1,4,1,3902,1015,5200,3,10,1,24))
zxMsagCallAllocMemoryErrorAlarm.setObjects((_C,_O))
if mibBuilder.loadTexts:zxMsagCallAllocMemoryErrorAlarm.setStatus(_A)
zxMsagQosPoorAlarm=NotificationType((1,3,6,1,4,1,3902,1015,5200,3,10,1,25))
zxMsagQosPoorAlarm.setObjects(*((_C,_e),(_C,_f),(_C,_z),(_C,_A0),(_C,_A1),(_C,_I),(_C,_J),(_C,_K),(_C,_H)))
if mibBuilder.loadTexts:zxMsagQosPoorAlarm.setStatus(_A)
zxMsagQosPoorRestore=NotificationType((1,3,6,1,4,1,3902,1015,5200,3,10,1,26))
zxMsagQosPoorRestore.setObjects(*((_C,_e),(_C,_f),(_C,_z),(_C,_A0),(_C,_A1),(_C,_I),(_C,_J),(_C,_K),(_C,_H)))
if mibBuilder.loadTexts:zxMsagQosPoorRestore.setStatus(_A)
zxAnSlcFreqOffOnHookAlarm=NotificationType((1,3,6,1,4,1,3902,1015,5200,3,10,1,100))
zxAnSlcFreqOffOnHookAlarm.setObjects(*((_C,_I),(_C,_J),(_C,_K),(_C,_H)))
if mibBuilder.loadTexts:zxAnSlcFreqOffOnHookAlarm.setStatus(_A)
zxAnSlcFreqOffOnHookAlarmRestore=NotificationType((1,3,6,1,4,1,3902,1015,5200,3,10,1,101))
zxAnSlcFreqOffOnHookAlarmRestore.setObjects(*((_C,_I),(_C,_J),(_C,_K),(_C,_H)))
if mibBuilder.loadTexts:zxAnSlcFreqOffOnHookAlarmRestore.setStatus(_A)
zxAnSlcGroundedAlarm=NotificationType((1,3,6,1,4,1,3902,1015,5200,3,10,1,102))
zxAnSlcGroundedAlarm.setObjects(*((_C,_I),(_C,_J),(_C,_K),(_C,_H)))
if mibBuilder.loadTexts:zxAnSlcGroundedAlarm.setStatus(_A)
zxAnSlcGroundedRestore=NotificationType((1,3,6,1,4,1,3902,1015,5200,3,10,1,103))
zxAnSlcGroundedRestore.setObjects(*((_C,_I),(_C,_J),(_C,_K),(_C,_H)))
if mibBuilder.loadTexts:zxAnSlcGroundedRestore.setStatus(_A)
zxAnSlcContactedWithPower=NotificationType((1,3,6,1,4,1,3902,1015,5200,3,10,1,104))
zxAnSlcContactedWithPower.setObjects(*((_C,_I),(_C,_J),(_C,_K),(_C,_H)))
if mibBuilder.loadTexts:zxAnSlcContactedWithPower.setStatus(_A)
zxAnDsx1ProtectionGroupSwapped=NotificationType((1,3,6,1,4,1,3902,1015,5200,3,10,1,105))
zxAnDsx1ProtectionGroupSwapped.setObjects(*((_C,_Aw),(_C,_Ax),(_C,_Ay),(_C,_Az),(_C,_A_),(_C,_B0),(_C,_B1),(_C,_B2),(_C,_B3),(_C,_B4)))
if mibBuilder.loadTexts:zxAnDsx1ProtectionGroupSwapped.setStatus(_A)
zxAnIsdnUInterfaceLinkDown=NotificationType((1,3,6,1,4,1,3902,1015,5200,3,10,1,106))
zxAnIsdnUInterfaceLinkDown.setObjects(*((_C,_I),(_C,_J),(_C,_K),(_C,_H)))
if mibBuilder.loadTexts:zxAnIsdnUInterfaceLinkDown.setStatus(_A)
zxAnIsdnUInterfaceLinkUp=NotificationType((1,3,6,1,4,1,3902,1015,5200,3,10,1,107))
zxAnIsdnUInterfaceLinkUp.setObjects(*((_C,_I),(_C,_J),(_C,_K),(_C,_H)))
if mibBuilder.loadTexts:zxAnIsdnUInterfaceLinkUp.setStatus(_A)
zxAnSlcContactedWithPowerClr=NotificationType((1,3,6,1,4,1,3902,1015,5200,3,10,1,108))
zxAnSlcContactedWithPowerClr.setObjects(*((_C,_I),(_C,_J),(_C,_K),(_C,_H)))
if mibBuilder.loadTexts:zxAnSlcContactedWithPowerClr.setStatus(_A)
zxAnHwTsUsageAboveThresholdAlm=NotificationType((1,3,6,1,4,1,3902,1015,5200,3,10,1,109))
zxAnHwTsUsageAboveThresholdAlm.setObjects(*((_C,_A2),(_C,_A3)))
if mibBuilder.loadTexts:zxAnHwTsUsageAboveThresholdAlm.setStatus(_A)
zxAnHwTsUsageAboveThresholdClr=NotificationType((1,3,6,1,4,1,3902,1015,5200,3,10,1,110))
zxAnHwTsUsageAboveThresholdClr.setObjects(*((_C,_A2),(_C,_A3)))
if mibBuilder.loadTexts:zxAnHwTsUsageAboveThresholdClr.setStatus(_A)
zxAnVoicePortLockoutAlm=NotificationType((1,3,6,1,4,1,3902,1015,5200,3,10,1,111))
zxAnVoicePortLockoutAlm.setObjects(*((_C,_I),(_C,_J),(_C,_K),(_C,_H)))
if mibBuilder.loadTexts:zxAnVoicePortLockoutAlm.setStatus(_A)
zxAnVoicePortLockoutClr=NotificationType((1,3,6,1,4,1,3902,1015,5200,3,10,1,112))
zxAnVoicePortLockoutClr.setObjects(*((_C,_I),(_C,_J),(_C,_K),(_C,_H)))
if mibBuilder.loadTexts:zxAnVoicePortLockoutClr.setStatus(_A)
zxAnDdiSubscriberLineBrokenAlm=NotificationType((1,3,6,1,4,1,3902,1015,5200,3,10,1,113))
zxAnDdiSubscriberLineBrokenAlm.setObjects(*((_C,_I),(_C,_J),(_C,_K),(_C,_H)))
if mibBuilder.loadTexts:zxAnDdiSubscriberLineBrokenAlm.setStatus(_A)
zxAnDdiSubscriberLineBrokenClr=NotificationType((1,3,6,1,4,1,3902,1015,5200,3,10,1,114))
zxAnDdiSubscriberLineBrokenClr.setObjects(*((_C,_I),(_C,_J),(_C,_K),(_C,_H)))
if mibBuilder.loadTexts:zxAnDdiSubscriberLineBrokenClr.setStatus(_A)
zxAnVoicePortHighAcVoltageAlm=NotificationType((1,3,6,1,4,1,3902,1015,5200,3,10,1,115))
zxAnVoicePortHighAcVoltageAlm.setObjects(*((_C,_I),(_C,_J),(_C,_K),(_C,_H)))
if mibBuilder.loadTexts:zxAnVoicePortHighAcVoltageAlm.setStatus(_A)
zxAnVoicePortHighAcVoltageClr=NotificationType((1,3,6,1,4,1,3902,1015,5200,3,10,1,116))
zxAnVoicePortHighAcVoltageClr.setObjects(*((_C,_I),(_C,_J),(_C,_K),(_C,_H)))
if mibBuilder.loadTexts:zxAnVoicePortHighAcVoltageClr.setStatus(_A)
zxAnVoicePortHighDcVoltageAlm=NotificationType((1,3,6,1,4,1,3902,1015,5200,3,10,1,117))
zxAnVoicePortHighDcVoltageAlm.setObjects(*((_C,_I),(_C,_J),(_C,_K),(_C,_H)))
if mibBuilder.loadTexts:zxAnVoicePortHighDcVoltageAlm.setStatus(_A)
zxAnVoicePortHighDcVoltageClr=NotificationType((1,3,6,1,4,1,3902,1015,5200,3,10,1,118))
zxAnVoicePortHighDcVoltageClr.setObjects(*((_C,_I),(_C,_J),(_C,_K),(_C,_H)))
if mibBuilder.loadTexts:zxAnVoicePortHighDcVoltageClr.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'A200ShelfTypes':A200ShelfTypes,'A200BoardTypes':A200BoardTypes,'zte':zte,'msag':msag,'zxAnVoipBaseMib':zxAnVoipBaseMib,'msagmajorVersion':msagmajorVersion,'msagGlobalConfig':msagGlobalConfig,'a200MgCfgTable':a200MgCfgTable,'a200MgCfgEntry':a200MgCfgEntry,'a200mgid':a200mgid,'a200protype':a200protype,'a200version':a200version,'a200encodetp':a200encodetp,'a200mgport':a200mgport,'a200translay':a200translay,'a200transpro':a200transpro,'a200mgDomainName':a200mgDomainName,'a200mgInfo':a200mgInfo,'a200mgcid1':a200mgcid1,'a200mgcid2':a200mgcid2,'a200mgcid3':a200mgcid3,'a200mgcid4':a200mgcid4,'a200selfexchange':a200selfexchange,'a200protectcall':a200protectcall,'a200disasterprot':a200disasterprot,'a200mgRowStatus':a200mgRowStatus,'a200tractnum':a200tractnum,'a200sdpcho':a200sdpcho,'a200retrannum':a200retrannum,'a200resdelay':a200resdelay,'a200retranmin':a200retranmin,'a200lkpttime':a200lkpttime,'a200pendtime':a200pendtime,'a200pendcount':a200pendcount,'a200kprestime':a200kprestime,'a200tranidmax':a200tranidmax,'a200tranidmin':a200tranidmin,'a200rtpFaxPri1':a200rtpFaxPri1,'a200rtpFaxPri2':a200rtpFaxPri2,'a200subsuspendrtp':a200subsuspendrtp,'a200hotlinewithspace':a200hotlinewithspace,'a200rtp2833Type':a200rtp2833Type,_q:a200ipsThreshold,'a200congesttime':a200congesttime,'a200congesttone':a200congesttone,'a200callmatchtype':a200callmatchtype,'a200currentmgcid':a200currentmgcid,'a200mgSigTos':a200mgSigTos,'a200mgPSTNMediaVoiceTos':a200mgPSTNMediaVoiceTos,'a200mgPSTNMediaFaxTos':a200mgPSTNMediaFaxTos,'a200mgPSTNMediaModemTos':a200mgPSTNMediaModemTos,'a200mgPSTNMediaDataTos':a200mgPSTNMediaDataTos,'a200mgISDNMediaVoiceTos':a200mgISDNMediaVoiceTos,'a200mgISDNMediaFaxTos':a200mgISDNMediaFaxTos,'a200mgISDNMediaModemTos':a200mgISDNMediaModemTos,'a200mgISDNMediaDataTos':a200mgISDNMediaDataTos,'a200ringprofile':a200ringprofile,'a200toneprofile':a200toneprofile,'a200flashprofile':a200flashprofile,'a200chg16kcwidth':a200chg16kcwidth,'a200chg16kcinterval':a200chg16kcinterval,'a200charge16kcvol':a200charge16kcvol,'a200kcflag':a200kcflag,'a200ExternalSelfswitchEnable':a200ExternalSelfswitchEnable,_r:zxAnIpsUsage,'a200MgCallEscapeMode':a200MgCallEscapeMode,'a200mgccfgTable':a200mgccfgTable,'a200mgccfgEntry':a200mgccfgEntry,_A5:a200mgcmgcid,'a200mgctypeid':a200mgctypeid,'a200mgcip':a200mgcip,'a200mgcport':a200mgcport,'a200mgcdomain':a200mgcdomain,'a200mgcinfo':a200mgcinfo,'a200mgcMD5Info':a200mgcMD5Info,'a200mgcRowStatus':a200mgcRowStatus,'a200MgcTypeTable':a200MgcTypeTable,'a200MgcTypeEntry':a200MgcTypeEntry,_A6:a200MgcTypeId,'a200MgcTypeDesc':a200MgcTypeDesc,'a200MgcTypeMaxTransPkg':a200MgcTypeMaxTransPkg,'a200MgcTypeReasonQuote':a200MgcTypeReasonQuote,'a200MgcTypeQueryStatus':a200MgcTypeQueryStatus,'a200MgcTypeHeartBeat':a200MgcTypeHeartBeat,'a200MgcTypeDmLong':a200MgcTypeDmLong,'a200MgcTypeDmShort':a200MgcTypeDmShort,'a200MgcTypeDmStart':a200MgcTypeDmStart,'a200MgcTypeWithTime':a200MgcTypeWithTime,'a200MgcTypeWithDelay':a200MgcTypeWithDelay,'a200MgcTypeProfileName':a200MgcTypeProfileName,'a200MgcTypeUserOut':a200MgcTypeUserOut,'a200MgcTypeAgOut':a200MgcTypeAgOut,'a200MgcTypeHeartId':a200MgcTypeHeartId,'a200MgcTypeAgRegOldMT':a200MgcTypeAgRegOldMT,'a200MgcTypeCanclerror':a200MgcTypeCanclerror,'a200MgcTypeRowStatus':a200MgcTypeRowStatus,'a200MedNatTable':a200MedNatTable,'a200MedNatEntry':a200MedNatEntry,_A9:a200mednatIpsRack,_AA:a200mednatIpsShelf,_AB:a200mednatIpsSlot,_AC:a200mednatSubCard,'a200mednatNicRack':a200mednatNicRack,'a200mednatNicShelf':a200mednatNicShelf,'a200mednatNicSlot':a200mednatNicSlot,'a200mednatInPhyPort':a200mednatInPhyPort,'a200mednatExPhyPort':a200mednatExPhyPort,'a200mednatExIp':a200mednatExIp,'a200mednatUdpPort':a200mednatUdpPort,'a200mednatRowStatus':a200mednatRowStatus,'a200natCtrlId':a200natCtrlId,'a200QovsTable':a200QovsTable,'a200QovsEntry':a200QovsEntry,_AD:a200QovsId,'a200QovsLoss':a200QovsLoss,'a200QovsDelay':a200QovsDelay,'a200QovsJitter':a200QovsJitter,'a200QovsRowStatus':a200QovsRowStatus,'a200MiscTable':a200MiscTable,'a200MiscEntry':a200MiscEntry,_AE:a200MiscIndex,'a200MiscFlashDelay':a200MiscFlashDelay,'a200MiscCalledPartyReanwer':a200MiscCalledPartyReanwer,'a200MiscH248BusyStatus':a200MiscH248BusyStatus,'a200MiscHowlTone':a200MiscHowlTone,'a200MiscH248Short':a200MiscH248Short,'a200MiscH248Long':a200MiscH248Long,'a200MiscRTPtimer':a200MiscRTPtimer,'a200MiscH248RingPattern':a200MiscH248RingPattern,'a200MiscCallAlarm':a200MiscCallAlarm,'a200MiscInterCallAlarm':a200MiscInterCallAlarm,'a200MiscFreshTnet':a200MiscFreshTnet,'a200MiscCheckContext':a200MiscCheckContext,'a200MiscUpPort':a200MiscUpPort,'a200MiscResReportPeriod':a200MiscResReportPeriod,'a200MiscAgMustDetOvrLd':a200MiscAgMustDetOvrLd,'a200MiscErrReplyInformSSEn':a200MiscErrReplyInformSSEn,'a200MiscCookieEchoFormat':a200MiscCookieEchoFormat,'a200MiscCheckSumFormat':a200MiscCheckSumFormat,'a200MiscIuaIsdnHwFormat':a200MiscIuaIsdnHwFormat,'a200DigitMapTable':a200DigitMapTable,'a200DigitMapEntry':a200DigitMapEntry,_AF:a200DigitMapDas,'a200DigitMapMgid':a200DigitMapMgid,'a200DigitMapSrvType':a200DigitMapSrvType,'a200DigitMapDgtName':a200DigitMapDgtName,'a200DigitMapDgtMap':a200DigitMapDgtMap,'a200DigitMapRowStatus':a200DigitMapRowStatus,'a200VoipRouteTable':a200VoipRouteTable,'a200VoipRouteEntry':a200VoipRouteEntry,_AG:a200VoipRouteMgId,_AH:a200VoipRouteType,_AI:a200VoipRouteDestIp,'a200VoipRouteDestMask':a200VoipRouteDestMask,'a200VoipRouteNexthop':a200VoipRouteNexthop,'a200VoipRouteNexthopMac':a200VoipRouteNexthopMac,'a200VoipRouteArpTime':a200VoipRouteArpTime,'a200VoipRouteRowStatus':a200VoipRouteRowStatus,'a200CtlPortTable':a200CtlPortTable,'a200CtlPortEntry':a200CtlPortEntry,_AJ:a200CtlPortCtlId,'a200CtlPortInfo':a200CtlPortInfo,'a200CtlPortUdpPort':a200CtlPortUdpPort,'a200CtlPortRowStatus':a200CtlPortRowStatus,'callOptimizeTable':callOptimizeTable,'callOptimizeEntry':callOptimizeEntry,_AK:calloptIndex,'calloptOpenMsgAck':calloptOpenMsgAck,'calloptPlayToneAck':calloptPlayToneAck,'calloptSubPriority':calloptSubPriority,'calloptNumMax':calloptNumMax,'calloptH248MsgAck':calloptH248MsgAck,'calloptH248MsgPn':calloptH248MsgPn,'calloptH248Statistic':calloptH248Statistic,'calloptH248HookOffEvent':calloptH248HookOffEvent,'calloptH248HookOnEvent':calloptH248HookOnEvent,'calloptServiceAbnormal':calloptServiceAbnormal,'calloptMgProtocolErr':calloptMgProtocolErr,'calloptMgcProtocolErr':calloptMgcProtocolErr,'calloptMgInsideErr':calloptMgInsideErr,'calloptHookOffLimiteCycle':calloptHookOffLimiteCycle,'calloptHookOffLimiteBlock':calloptHookOffLimiteBlock,'calloptHookOffLimiteUnblock':calloptHookOffLimiteUnblock,'calloptMgcCallWaitTone':calloptMgcCallWaitTone,'calloptToneArea':calloptToneArea,'calloptH248LinkBreakTone':calloptH248LinkBreakTone,'msagLoadDefaultRingProfile':msagLoadDefaultRingProfile,'zxAnVoipInterfaceTable':zxAnVoipInterfaceTable,'zxAnVoipInterfaceEntry':zxAnVoipInterfaceEntry,'zxAnMgId':zxAnMgId,'zxAnVoipCtrlIpAddr':zxAnVoipCtrlIpAddr,'zxAnVoipCtrlIpMask':zxAnVoipCtrlIpMask,'zxAnVoipMediaIpaddr':zxAnVoipMediaIpaddr,'zxAnVoipMediaIpMask':zxAnVoipMediaIpMask,'zxAnVoipInterfaceRowStatus':zxAnVoipInterfaceRowStatus,'zxAnVoipBaseGlobalObjects':zxAnVoipBaseGlobalObjects,'zxAnVoipBaseCapabilities':zxAnVoipBaseCapabilities,'zxAnSelfswitchTktObjects':zxAnSelfswitchTktObjects,'zxAnSelfswitchTktEnable':zxAnSelfswitchTktEnable,'zxAnSelfswitchTktUploadInterval':zxAnSelfswitchTktUploadInterval,'zxAnSelfswitchTktSizeThreshold':zxAnSelfswitchTktSizeThreshold,'zxAnSelfswitchTelLoadObjects':zxAnSelfswitchTelLoadObjects,'zxAnSelfswitchTelLoadFileName':zxAnSelfswitchTelLoadFileName,'zxAnSelfswitchTelLoadStatus':zxAnSelfswitchTelLoadStatus,'zxAnSelfswitchTelLoadFailReason':zxAnSelfswitchTelLoadFailReason,'zxAnVoicePortLockoutTrapEnable':zxAnVoicePortLockoutTrapEnable,'zxAnSelfswitchTktFtpTable':zxAnSelfswitchTktFtpTable,'zxAnSelfswitchTktFtpEntry':zxAnSelfswitchTktFtpEntry,_AL:zxAnSelfswitchTktFtpServerId,'zxAnSelfswitchTktFtpServerIpType':zxAnSelfswitchTktFtpServerIpType,'zxAnSelfswitchTktFtpServerIp':zxAnSelfswitchTktFtpServerIp,'zxAnSelfswitchTktFtpUserName':zxAnSelfswitchTktFtpUserName,'zxAnSelfswitchTktFtpUserPwd':zxAnSelfswitchTktFtpUserPwd,'zxAnSelfswitchTktFtpServerPath':zxAnSelfswitchTktFtpServerPath,'zxAnSelfswitchTktFtpRowStatus':zxAnSelfswitchTktFtpRowStatus,'zxAnDsx1ProtectionGroupTable':zxAnDsx1ProtectionGroupTable,'zxAnDsx1ProtectionGroupEntry':zxAnDsx1ProtectionGroupEntry,_AM:zxAnDsx1ProtectionGroupId,_Aw:zxAnDsx1ProtectionGroupName,_Ax:zxAnDsx1MasterDsx1Rack,_Ay:zxAnDsx1MasterDsx1Shelf,_Az:zxAnDsx1MasterDsx1Slot,_A_:zxAnDsx1MasterDsx1LinkNo,_B0:zxAnDsx1StandbyDsx1Rack,_B1:zxAnDsx1StandbyDsx1Shelf,_B2:zxAnDsx1StandbyDsx1Slot,_B3:zxAnDsx1StandbyDsx1LinkNo,_B4:zxAnDsx1CurrWorkingDsx1,'zxAnDsx1ProtectionGroupRowStatus':zxAnDsx1ProtectionGroupRowStatus,'zxAnHwTimeSlotUsageObjects':zxAnHwTimeSlotUsageObjects,'zxAnHwTimeSlotUsageGlobalObjects':zxAnHwTimeSlotUsageGlobalObjects,_A2:zxAnHwTimeSlotUsageThreshold,'zxAnHwTimeSlotUsageTable':zxAnHwTimeSlotUsageTable,'zxAnHwTimeSlotUsageEntry':zxAnHwTimeSlotUsageEntry,_AN:zxAnHwTimeSlotUsageRack,_AO:zxAnHwTimeSlotUsageShelf,_A3:zxAnHwTimeSlotUsage,'msagResource':msagResource,'a200SlcTermIDTable':a200SlcTermIDTable,'a200SlcTermIDEntry':a200SlcTermIDEntry,_AP:a200slcTermIDrackno,_AQ:a200slcTermIDshelfno,_AR:a200slcTermIDslotno,_AS:a200slcTermIDBeginIndex,'a200slcTermIDOperSum':a200slcTermIDOperSum,'a200slcTermIDTMID':a200slcTermIDTMID,'a200slcTermIDType':a200slcTermIDType,'a200slcTermIDBeginNo':a200slcTermIDBeginNo,'a200slcTermIDDigitLen':a200slcTermIDDigitLen,'a200slcTermIDMgId':a200slcTermIDMgId,'a200slcTerminationID':a200slcTerminationID,'a200slcTermIDRowStatus':a200slcTermIDRowStatus,'a200IpsTermIDTable':a200IpsTermIDTable,'a200IpsTermIDEntry':a200IpsTermIDEntry,_AT:a200IpsTermIDSeqNo,'a200IpsTermIDDeltag':a200IpsTermIDDeltag,'a200IpsTermIDBeginSeqNo':a200IpsTermIDBeginSeqNo,'a200IpsTermIDOperNum':a200IpsTermIDOperNum,'a200IpsTermIDTMIDFix':a200IpsTermIDTMIDFix,'a200IpsTermIDType':a200IpsTermIDType,'a200IpsTermIDDigitLen':a200IpsTermIDDigitLen,'a200IpsTermIDBeginNo':a200IpsTermIDBeginNo,'a200IpsTermIDMgId':a200IpsTermIDMgId,'a200IpsTerminationID':a200IpsTerminationID,'a200IpsTermIDRowStatus':a200IpsTermIDRowStatus,'a200RtpParTable':a200RtpParTable,'a200RtpParEntry':a200RtpParEntry,_AU:a200rtpparparid,'a200rtpparvadval':a200rtpparvadval,'a200rtppardtmfrlmod':a200rtppardtmfrlmod,'a200rtpparpcmlaw':a200rtpparpcmlaw,'a200rtpparsiltopcm':a200rtpparsiltopcm,'a200rtppardcfilter':a200rtppardcfilter,'a200rtpparpcmtopkggain':a200rtpparpcmtopkggain,'a200rtpparpkgtopcmgain':a200rtpparpkgtopcmgain,'a200rtpparconceal':a200rtpparconceal,'a200rtpparecmdisabl':a200rtpparecmdisabl,'a200rtpparspeedlim':a200rtpparspeedlim,'a200rtpparerrrecov':a200rtpparerrrecov,'a200rtppartcfproc':a200rtppartcfproc,'a200rtppart38enable':a200rtppart38enable,'a200rtppardtmfduplex':a200rtppardtmfduplex,'a200rtpparNumBeforeOff':a200rtpparNumBeforeOff,'a200rtpparIgnoreA':a200rtpparIgnoreA,'a200rtpparToneDuplex':a200rtpparToneDuplex,'a200rtppardecodadapt':a200rtppardecodadapt,'a200rtpparg723rate':a200rtpparg723rate,'a200rtpparpckgendis':a200rtpparpckgendis,'a200rtppardtmfpyld':a200rtppardtmfpyld,'a200rtppardtmfredpyld':a200rtppardtmfredpyld,'a200rtpparfaxdatared':a200rtpparfaxdatared,'a200rtppart30msgred':a200rtppart30msgred,'a200rtpparmasecenal':a200rtpparmasecenal,'a200rtpparhdwecdis':a200rtpparhdwecdis,'a200rtpparhecfrz':a200rtpparhecfrz,'a200rtpparectxf':a200rtpparectxf,'a200rtpparectxm':a200rtpparectxm,'a200rtpparecrxm':a200rtpparecrxm,'a200rtpparheclen':a200rtpparheclen,'a200rtpparlpwmin':a200rtpparlpwmin,'a200rtpparlpwmax':a200rtpparlpwmax,'a200rtpparlpwinit':a200rtpparlpwinit,'a200rtpparlpr':a200rtpparlpr,'a200rtpparfsklevel':a200rtpparfsklevel,'a200rtpparg711redund':a200rtpparg711redund,'a200rtpparmodemmode':a200rtpparmodemmode,'a200rtpparap':a200rtpparap,'a200rtppardeletmode':a200rtppardeletmode,'a200rtpparnortptime':a200rtpparnortptime,'a200rtpparfaxswtime':a200rtpparfaxswtime,'a200rtppardtmfcidelec':a200rtppardtmfcidelec,'msagCallCtrl':msagCallCtrl,'upPortTable':upPortTable,'upPortEntry':upPortEntry,'upportid':upportid,'upportrack':upportrack,'upportshelf':upportshelf,'upportslot':upportslot,'upportport':upportport,'upportsendrateth':upportsendrateth,'upportreceiverateth':upportreceiverateth,'upportRowStatus':upportRowStatus,'toneTable':toneTable,'toneEntry':toneEntry,'tonemgid':tonemgid,'tonefaxcngtone':tonefaxcngtone,'tonev21flagstone':tonev21flagstone,'tonet38faxend':tonet38faxend,'toneansamwitone':toneansamwitone,'toneansamwotone':toneansamwotone,'toneanswitone':toneanswitone,'toneanswotone':toneanswotone,'tonefixtonechip':tonefixtonechip,'msagH248Perform':msagH248Perform,'msagH248PSRecMsg':msagH248PSRecMsg,'msagH248PSSendMsg':msagH248PSSendMsg,'msagH248PSRecMsgByte':msagH248PSRecMsgByte,'msagH248PSSendMsgByte':msagH248PSSendMsgByte,'msagH248PSProtocolError':msagH248PSProtocolError,'msagH248PSTimerOut':msagH248PSTimerOut,'msagH248PSDisconnect':msagH248PSDisconnect,'msagH248PSMGCChange':msagH248PSMGCChange,'msagH248PSTransmitError':msagH248PSTransmitError,'calllimitipsthruput':calllimitipsthruput,'calllimitnicthruput':calllimitnicthruput,'calllimitcalllimit':calllimitcalllimit,'calllimitcpubusylimit':calllimitcpubusylimit,'calllimitupportlimit':calllimitupportlimit,'calllimitipslimit':calllimitipslimit,'calllimitniclimit':calllimitniclimit,'msagTrap':msagTrap,'msagTrapId':msagTrapId,'zxAnNarrowbandResAvailable':zxAnNarrowbandResAvailable,'zxAnNarrowbandResUnavailable':zxAnNarrowbandResUnavailable,'zxAnIpsResource':zxAnIpsResource,'zxAnIpsResourceRestore':zxAnIpsResourceRestore,'zxAnIpsChannelFault':zxAnIpsChannelFault,'zxAnIpsChannelFaultRestore':zxAnIpsChannelFaultRestore,'zxMsagH248Link':zxMsagH248Link,'zxMsagH248LinkRestore':zxMsagH248LinkRestore,'zxMsagH248ErrorCode':zxMsagH248ErrorCode,'zxAnDlccNT1Los':zxAnDlccNT1Los,'zxMsagMgcpLink':zxMsagMgcpLink,'zxMsagMgcpLinkRestore':zxMsagMgcpLinkRestore,'zxMsagMgcpAbnormal':zxMsagMgcpAbnormal,'zxMsagMgcpAbnormalRestore':zxMsagMgcpAbnormalRestore,'zxMsagV5Pcm':zxMsagV5Pcm,'zxMsagV5PcmRestore':zxMsagV5PcmRestore,'zxMsagV5Proto':zxMsagV5Proto,'zxMsagV5ProtoRestore':zxMsagV5ProtoRestore,'zxMsagISDNSctpInform':zxMsagISDNSctpInform,'zxMsagISDNSctpAlarm':zxMsagISDNSctpAlarm,'zxMsagIUAInform':zxMsagIUAInform,'zxMsagIUAAlarm':zxMsagIUAAlarm,'zxMsagIUAAlarmRestore':zxMsagIUAAlarmRestore,'zxMsagCallAllocMemoryErrorAlarm':zxMsagCallAllocMemoryErrorAlarm,'zxMsagQosPoorAlarm':zxMsagQosPoorAlarm,'zxMsagQosPoorRestore':zxMsagQosPoorRestore,'zxAnSlcFreqOffOnHookAlarm':zxAnSlcFreqOffOnHookAlarm,'zxAnSlcFreqOffOnHookAlarmRestore':zxAnSlcFreqOffOnHookAlarmRestore,'zxAnSlcGroundedAlarm':zxAnSlcGroundedAlarm,'zxAnSlcGroundedRestore':zxAnSlcGroundedRestore,'zxAnSlcContactedWithPower':zxAnSlcContactedWithPower,'zxAnDsx1ProtectionGroupSwapped':zxAnDsx1ProtectionGroupSwapped,'zxAnIsdnUInterfaceLinkDown':zxAnIsdnUInterfaceLinkDown,'zxAnIsdnUInterfaceLinkUp':zxAnIsdnUInterfaceLinkUp,'zxAnSlcContactedWithPowerClr':zxAnSlcContactedWithPowerClr,'zxAnHwTsUsageAboveThresholdAlm':zxAnHwTsUsageAboveThresholdAlm,'zxAnHwTsUsageAboveThresholdClr':zxAnHwTsUsageAboveThresholdClr,'zxAnVoicePortLockoutAlm':zxAnVoicePortLockoutAlm,'zxAnVoicePortLockoutClr':zxAnVoicePortLockoutClr,'zxAnDdiSubscriberLineBrokenAlm':zxAnDdiSubscriberLineBrokenAlm,'zxAnDdiSubscriberLineBrokenClr':zxAnDdiSubscriberLineBrokenClr,'zxAnVoicePortHighAcVoltageAlm':zxAnVoicePortHighAcVoltageAlm,'zxAnVoicePortHighAcVoltageClr':zxAnVoicePortHighAcVoltageClr,'zxAnVoicePortHighDcVoltageAlm':zxAnVoicePortHighDcVoltageAlm,'zxAnVoicePortHighDcVoltageClr':zxAnVoicePortHighDcVoltageClr,'msagTrapObjectMib':msagTrapObjectMib,_n:zxAnNarrowbandResCfgType,_o:zxAnNarrowbandResActType,_p:zxAnIpsResourceAlarmReason,_I:zxAnTrapRack,_J:zxAnTrapShelf,_K:zxAnTrapSlot,_e:zxAnTrapUnit,_f:zxAnTrapSunit,_H:zxAnTrapPort,_O:msagTrapReason,_X:msagTrapLinkState,_Y:msagTrapMgcNo,'msagTrapSLN':msagTrapSLN,'msagTrapFlag':msagTrapFlag,_As:msagTrapErrcode,_Av:msagTrapIpAddress,'msagTrapBETime':msagTrapBETime,_At:zxAnTrapInfoType,_s:msagTrapUnitNo,_t:msagTrapPcmNo,_u:msagTrapReasionValue,'msagTrapRack':msagTrapRack,'msagTrapShelf':msagTrapShelf,'msagTrapSlot':msagTrapSlot,_v:msagTrapV5InterId,_w:msagTrapDLProType,_x:msagTrapCurEvent,_y:msagTrapCurState,_Au:msagTrapParaLinkId,_A0:msagQosAlarmType,_A1:msagQosAlarmDetail,_z:msagTrapPort,'zxAnVoipCallTest':zxAnVoipCallTest,'zxAnVoipCalleeTestTable':zxAnVoipCalleeTestTable,'zxAnVoipCalleeTestEntry':zxAnVoipCalleeTestEntry,_AV:zxAnVoipCalleeTestRack,_AW:zxAnVoipCalleeTestShelf,_AX:zxAnVoipCalleeTestSlot,_AY:zxAnVoipCalleeTestPort,_AZ:zxAnVoipCalleeTestOnu,_Aa:zxAnVoipCalleeTestCircuitType,_Ab:zxAnVoipCalleeTestLogicalId,'zxAnVoipCalleeTestAction':zxAnVoipCalleeTestAction,'zxAnVoipCalleeTestTimeout':zxAnVoipCalleeTestTimeout,'zxAnVoipCalleeTestStatus':zxAnVoipCalleeTestStatus,'zxAnVoipCalleeTestPortStatus':zxAnVoipCalleeTestPortStatus,'zxAnVoipCalleeTestFailReason':zxAnVoipCalleeTestFailReason,'zxAnVoipCalleeTestFailDetail':zxAnVoipCalleeTestFailDetail,'zxAnVoipCalleeTestRowStatus':zxAnVoipCalleeTestRowStatus,'zxAnVoipCallerTestTable':zxAnVoipCallerTestTable,'zxAnVoipCallerTestEntry':zxAnVoipCallerTestEntry,_Al:zxAnVoipCallerTestRack,_Am:zxAnVoipCallerTestShelf,_An:zxAnVoipCallerTestSlot,_Ao:zxAnVoipCallerTestPort,_Ap:zxAnVoipCallerTestOnu,_Aq:zxAnVoipCallerTestCircuitType,_Ar:zxAnVoipCallerTestLogicalId,'zxAnVoipCallerTestAction':zxAnVoipCallerTestAction,'zxAnVoipCallerTestTimeout':zxAnVoipCallerTestTimeout,'zxAnVoipCallerTestDialedNumber':zxAnVoipCallerTestDialedNumber,'zxAnVoipCallerTestStatus':zxAnVoipCallerTestStatus,'zxAnVoipCallerTestPortStatus':zxAnVoipCallerTestPortStatus,'zxAnVoipCallerTestFailReason':zxAnVoipCallerTestFailReason,'zxAnVoipCallerTestFailDetail':zxAnVoipCallerTestFailDetail,'zxAnVoipCallerTestSipFailReason':zxAnVoipCallerTestSipFailReason,'zxAnVoipCallerTestSipErrorCode':zxAnVoipCallerTestSipErrorCode,'zxAnVoipCallerTestSipDelay':zxAnVoipCallerTestSipDelay,'zxAnVoipCallerTestMode':zxAnVoipCallerTestMode,'zxAnVoipCallerTestRowStatus':zxAnVoipCallerTestRowStatus})