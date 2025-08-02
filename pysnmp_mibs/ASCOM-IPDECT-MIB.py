_BH='ipDectActiveAlarmsIndex'
_BG='indeterminate'
_BF='configPutFailed'
_BE='bmcGetFailed'
_BD='configGetFailed'
_BC='firmwareGetFailed'
_BB='bootGetFailed'
_BA='updateScriptGetFailed'
_B9='icpConnectionDown'
_B8='cuniteCommunicationFailure'
_B7='uniteCommunicationFailure'
_B6='provisioningDataCommunicationsPutError'
_B5='provisioningDataCommunicationsError'
_B4='sysBusyForSpeech'
_B3='dectMasterConnectionTimeout'
_B2='dectCipherTimeout'
_B1='dectDefEncKeyTimeout'
_B0='rfpBusyForSpeech'
_A_='boxMemoryLow'
_Az='ipNoRouteToDestinationLoop'
_Ay='ipNoRouteToDestinationNoGateway'
_Ax='ipNoRouteToDestinationIfNotConfigured'
_Aw='ipNoRouteToDestinationIfUnknown'
_Av='ipNoRouteToDestinationIfDown'
_Au='ipNoRouteToDestination'
_At='ipUdpBindError'
_As='ipOutOfUdpPorts'
_Ar='ipOutOfUdpRtpPorts'
_Aq='ipTcpBindError'
_Ap='ipOutOfTcpPorts'
_Ao='ipOutOfTcpNatPorts'
_An='ipArpPoisoningDetected'
_Am='ipInvalidNatPortRange'
_Al='ipInvalidUdpNatPortRange'
_Ak='ipInvalidUdpRtpPortRange'
_Aj='ipDhcpServerNotResponding'
_Ai='ipInterfaceNotConfigured'
_Ah='ipInterfaceDown'
_Ag='syncUnsynchronizedToReference'
_Af='syncRefSignalLost'
_Ae='syncRingBroken'
_Ad='envFanFailure'
_Ac='envSupplyVoltageHigh'
_Ab='envSupplyVoltageLow'
_Aa='envHighPowerConsumption'
_AZ='envHighTemperature'
_AY='rfpRestarted'
_AX='rfpSyncMasterFailedToResynchronizeToReference'
_AW='rfpDetectedSysidCollision'
_AV='rfpAlienSyncLost'
_AU='rfpUnsynchronized'
_AT='rfpSwDlFailed'
_AS='rfpDisabled'
_AR='rfpMalfunctioning'
_AQ='rfpDisconnected'
_AP='x509CertificateNearExpiration'
_AO='x509SystemTimeNotSet'
_AN='kerberosCrossRealmFailure'
_AM='kerberosServerUnreachable'
_AL='kerberosServiceNotFound'
_AK='tlsNoRenegotiation'
_AJ='tlsUserCancelled'
_AI='tlsInternalError'
_AH='tlsInsufficientSecurity'
_AG='tlsProtocolVersion'
_AF='tlsExportRestriction'
_AE='tlsDecryptionError'
_AD='tlsDecodeError'
_AC='tlsAccessDenied'
_AB='tlsUnknownCA'
_AA='tlsIllegalParameter'
_A9='tlsUnknownCertificate'
_A8='tlsExpiredCertificate'
_A7='tlsRevocedCertificate'
_A6='tlsUnsupportedCertificate'
_A5='tlsBadCertificate'
_A4='tlsNoCertificate'
_A3='tlsHandshakeFailure'
_A2='tlsDecompressionFailure'
_A1='tlsRecordOverflow'
_A0='tlsDecryptionFailed'
_z='tlsBadMac'
_y='tlsUnexpectedMessage'
_x='cmdRestart'
_w='webmCoderMissingInUrl'
_v='webmInvalidUrl'
_u='sipDnsFailed'
_t='sipIntMediaNegotiationFailed'
_s='sipMediaConfigFailure'
_r='sipCoderSelectionFailure'
_q='sipOverloadDetected'
_p='sipNatDiscoverFailure'
_o='h323MediaIncompatible'
_n='h323SrtpKeyMismatch'
_m='h323SignalingTimeout'
_l='h323SignalingTCPFailed'
_k='h323StatusEnquiry'
_j='h323UnexpectedMessageReceived'
_i='rtpSrtpAuthFailure'
_h='rtpIceFailure'
_g='rtpSrtcpAuthFailure'
_f='rtpStunFailure'
_e='rtpWrongPayloadTypeReceived'
_d='rtpExcessiveLossOfData'
_c='rtpNoMediaDataReceived'
_b='cmInboundMobmRegDown'
_a='mobmStandbyActive'
_Z='mobmMasterRegDown'
_Y='mobmOutboundMobmRegDown'
_X='mobmInboundMobmRegDown'
_W='masterAbnormalCallRelease'
_V='masterLimitStaticRadiosReached'
_U='masterInactive'
_T='masterActive'
_S='masterPrimaryOrRedundantTrunkIsDown'
_R='masterRadioRegDown'
_Q='masterEmergencyRegDown'
_P='masterUserRegDown'
_O='masterStandbyActive'
_N='radioCpuResourcesAreNotAvailable'
_M='usersTheLdapReplicatorIsNotConnected'
_L='gwProtocolError'
_K='gwRegDown'
_J='gwInterfaceDown'
_I='ipDectFaultIndex'
_H='1907-12-01 00:00'
_G='ifIndex'
_F='IF-MIB'
_E='Integer32'
_D='ipDectLastErrorCode'
_C='ASCOM-IPDECT-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_F,_G)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ascomIpdectMIB=ModuleIdentity((1,3,6,1,4,1,27614,1,1,1))
if mibBuilder.loadTexts:ascomIpdectMIB.setRevisions(('1917-06-27 00:00','1917-02-15 00:00','1914-01-17 00:00','1913-10-07 00:00','1913-10-04 00:00','1913-05-14 00:00','1913-05-07 00:00','1913-04-22 00:00','1912-09-11 00:00','1912-08-31 00:00','1910-11-23 00:00','1910-06-17 00:00','1908-09-25 00:00',_H,_H))
_Ascom_ObjectIdentity=ObjectIdentity
ascom=_Ascom_ObjectIdentity((1,3,6,1,4,1,27614))
_AscomTraps_ObjectIdentity=ObjectIdentity
ascomTraps=_AscomTraps_ObjectIdentity((1,3,6,1,4,1,27614,0))
_AscomMibs_ObjectIdentity=ObjectIdentity
ascomMibs=_AscomMibs_ObjectIdentity((1,3,6,1,4,1,27614,1))
_AscomIpdect_ObjectIdentity=ObjectIdentity
ascomIpdect=_AscomIpdect_ObjectIdentity((1,3,6,1,4,1,27614,1,1))
_IpDectAttr_ObjectIdentity=ObjectIdentity
ipDectAttr=_IpDectAttr_ObjectIdentity((1,3,6,1,4,1,27614,1,1,1,1))
_IpDectFaultLogEntries_Type=Integer32
_IpDectFaultLogEntries_Object=MibScalar
ipDectFaultLogEntries=_IpDectFaultLogEntries_Object((1,3,6,1,4,1,27614,1,1,1,1,1),_IpDectFaultLogEntries_Type())
ipDectFaultLogEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:ipDectFaultLogEntries.setStatus(_A)
_IpDectAlarmLogEntries_Type=Integer32
_IpDectAlarmLogEntries_Object=MibScalar
ipDectAlarmLogEntries=_IpDectAlarmLogEntries_Object((1,3,6,1,4,1,27614,1,1,1,1,2),_IpDectAlarmLogEntries_Type())
ipDectAlarmLogEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:ipDectAlarmLogEntries.setStatus(_A)
_IpDectLastErrorCode_Type=Integer32
_IpDectLastErrorCode_Object=MibScalar
ipDectLastErrorCode=_IpDectLastErrorCode_Object((1,3,6,1,4,1,27614,1,1,1,1,3),_IpDectLastErrorCode_Type())
ipDectLastErrorCode.setMaxAccess(_B)
if mibBuilder.loadTexts:ipDectLastErrorCode.setStatus(_A)
_IpDectFaults_ObjectIdentity=ObjectIdentity
ipDectFaults=_IpDectFaults_ObjectIdentity((1,3,6,1,4,1,27614,1,1,1,2))
_IpDectFaultLogTable_Object=MibTable
ipDectFaultLogTable=_IpDectFaultLogTable_Object((1,3,6,1,4,1,27614,1,1,1,2,1))
if mibBuilder.loadTexts:ipDectFaultLogTable.setStatus(_A)
_IpDectFaultLogEntry_Object=MibTableRow
ipDectFaultLogEntry=_IpDectFaultLogEntry_Object((1,3,6,1,4,1,27614,1,1,1,2,1,1))
ipDectFaultLogEntry.setIndexNames((0,_C,_I))
if mibBuilder.loadTexts:ipDectFaultLogEntry.setStatus(_A)
class _IpDectFaultIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_IpDectFaultIndex_Type.__name__=_E
_IpDectFaultIndex_Object=MibTableColumn
ipDectFaultIndex=_IpDectFaultIndex_Object((1,3,6,1,4,1,27614,1,1,1,2,1,1,1),_IpDectFaultIndex_Type())
ipDectFaultIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ipDectFaultIndex.setStatus(_A)
_IpDectFaultDate_Type=OctetString
_IpDectFaultDate_Object=MibTableColumn
ipDectFaultDate=_IpDectFaultDate_Object((1,3,6,1,4,1,27614,1,1,1,2,1,1,2),_IpDectFaultDate_Type())
ipDectFaultDate.setMaxAccess(_B)
if mibBuilder.loadTexts:ipDectFaultDate.setStatus(_A)
_IpDectFaultTime_Type=OctetString
_IpDectFaultTime_Object=MibTableColumn
ipDectFaultTime=_IpDectFaultTime_Object((1,3,6,1,4,1,27614,1,1,1,2,1,1,3),_IpDectFaultTime_Type())
ipDectFaultTime.setMaxAccess(_B)
if mibBuilder.loadTexts:ipDectFaultTime.setStatus(_A)
class _IpDectFaultActivity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('alarm',0),('alarmCleared',1),('alarmTimeout',2),('error',3)))
_IpDectFaultActivity_Type.__name__=_E
_IpDectFaultActivity_Object=MibTableColumn
ipDectFaultActivity=_IpDectFaultActivity_Object((1,3,6,1,4,1,27614,1,1,1,2,1,1,4),_IpDectFaultActivity_Type())
ipDectFaultActivity.setMaxAccess(_B)
if mibBuilder.loadTexts:ipDectFaultActivity.setStatus(_A)
class _IpDectFaultCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(65537,65538,65539,196609,196865,197121,197122,197123,197124,197125,197126,197127,197128,197136,197377,197378,197379,197380,197633,327681,327682,327683,327684,327686,327688,327689,393217,393218,393219,393220,393221,393222,458753,458755,458756,458757,458759,458763,524289,524290,720897,786954,786964,786965,786966,786974,786984,786985,786986,786987,786988,786989,786990,786991,786992,786993,786994,786995,787004,787014,787015,787024,787034,787044,787459,787462,787463,790528,790529,917505,917506,917507,917508,917509,917510,917512,917513,917514,983041,983042,983044,983048,983056,1048577,1048578,1048580,1048584,1114112,1114113,1114114,1114137,1114138,1114139,1114177,1114182,1114183,1114185,1114192,1114193,1114195,1114202,1114203,1114204,1114205,1114206,1114207,1179649,1310721,1310821,1310822,1310823,1376257,1638401,1638402,1703937,1704192,2097152,2162689,2162690,2162691,2162692,2162693,2162694)));namedValues=NamedValues(*((_J,65537),(_K,65538),(_L,65539),(_M,196609),(_N,196865),(_O,197121),(_P,197122),(_Q,197123),(_R,197124),(_S,197125),(_T,197126),(_U,197127),(_V,197128),(_W,197136),(_X,197377),(_Y,197378),(_Z,197379),(_a,197380),(_b,197633),(_c,327681),(_d,327682),(_e,327683),(_f,327684),(_g,327686),(_h,327688),(_i,327689),(_j,393217),(_k,393218),(_l,393219),(_m,393220),(_n,393221),(_o,393222),(_p,458753),(_q,458755),(_r,458756),(_s,458757),(_t,458759),(_u,458763),(_v,524289),(_w,524290),(_x,720897),(_y,786954),(_z,786964),(_A0,786965),(_A1,786966),(_A2,786974),(_A3,786984),(_A4,786985),(_A5,786986),(_A6,786987),(_A7,786988),(_A8,786989),(_A9,786990),(_AA,786991),(_AB,786992),(_AC,786993),(_AD,786994),(_AE,786995),(_AF,787004),(_AG,787014),(_AH,787015),(_AI,787024),(_AJ,787034),(_AK,787044),(_AL,787459),(_AM,787462),(_AN,787463),(_AO,790528),(_AP,790529),(_AQ,917505),(_AR,917506),(_AS,917507),(_AT,917508),(_AU,917509),(_AV,917510),(_AW,917512),(_AX,917513),(_AY,917514),(_AZ,983041),(_Aa,983042),(_Ab,983044),(_Ac,983048),(_Ad,983056),(_Ae,1048577),(_Af,1048578),('syncLost',1048580),(_Ag,1048584),(_Ah,1114112),(_Ai,1114113),(_Aj,1114114),(_Ak,1114137),(_Al,1114138),(_Am,1114139),(_An,1114177),(_Ao,1114182),(_Ap,1114183),(_Aq,1114185),(_Ar,1114192),(_As,1114193),(_At,1114195),(_Au,1114202),(_Av,1114203),(_Aw,1114204),(_Ax,1114205),(_Ay,1114206),(_Az,1114207),(_A_,1179649),(_B0,1310721),(_B1,1310821),(_B2,1310822),(_B3,1310823),(_B4,1376257),(_B5,1638401),(_B6,1638402),(_B7,1703937),(_B8,1704192),(_B9,2097152),(_BA,2162689),(_BB,2162690),(_BC,2162691),(_BD,2162692),(_BE,2162693),(_BF,2162694)))
_IpDectFaultCode_Type.__name__=_E
_IpDectFaultCode_Object=MibTableColumn
ipDectFaultCode=_IpDectFaultCode_Object((1,3,6,1,4,1,27614,1,1,1,2,1,1,5),_IpDectFaultCode_Type())
ipDectFaultCode.setMaxAccess(_B)
if mibBuilder.loadTexts:ipDectFaultCode.setStatus(_A)
class _IpDectFaultSeverity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,99)));namedValues=NamedValues(*((_BG,0),('major',1),('critical',2),('none',99)))
_IpDectFaultSeverity_Type.__name__=_E
_IpDectFaultSeverity_Object=MibTableColumn
ipDectFaultSeverity=_IpDectFaultSeverity_Object((1,3,6,1,4,1,27614,1,1,1,2,1,1,6),_IpDectFaultSeverity_Type())
ipDectFaultSeverity.setMaxAccess(_B)
if mibBuilder.loadTexts:ipDectFaultSeverity.setStatus(_A)
_IpDectFaultSource_Type=OctetString
_IpDectFaultSource_Object=MibTableColumn
ipDectFaultSource=_IpDectFaultSource_Object((1,3,6,1,4,1,27614,1,1,1,2,1,1,7),_IpDectFaultSource_Type())
ipDectFaultSource.setMaxAccess(_B)
if mibBuilder.loadTexts:ipDectFaultSource.setStatus(_A)
_IpDectFaultIp_Type=IpAddress
_IpDectFaultIp_Object=MibTableColumn
ipDectFaultIp=_IpDectFaultIp_Object((1,3,6,1,4,1,27614,1,1,1,2,1,1,8),_IpDectFaultIp_Type())
ipDectFaultIp.setMaxAccess(_B)
if mibBuilder.loadTexts:ipDectFaultIp.setStatus(_A)
_IpDectFaultDescription_Type=OctetString
_IpDectFaultDescription_Object=MibTableColumn
ipDectFaultDescription=_IpDectFaultDescription_Object((1,3,6,1,4,1,27614,1,1,1,2,1,1,9),_IpDectFaultDescription_Type())
ipDectFaultDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:ipDectFaultDescription.setStatus(_A)
_IpDectActiveAlarmsTable_Object=MibTable
ipDectActiveAlarmsTable=_IpDectActiveAlarmsTable_Object((1,3,6,1,4,1,27614,1,1,1,2,2))
if mibBuilder.loadTexts:ipDectActiveAlarmsTable.setStatus(_A)
_IpDectActiveAlarmsEntry_Object=MibTableRow
ipDectActiveAlarmsEntry=_IpDectActiveAlarmsEntry_Object((1,3,6,1,4,1,27614,1,1,1,2,2,1))
ipDectActiveAlarmsEntry.setIndexNames((0,_C,_BH))
if mibBuilder.loadTexts:ipDectActiveAlarmsEntry.setStatus(_A)
class _IpDectActiveAlarmsIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_IpDectActiveAlarmsIndex_Type.__name__=_E
_IpDectActiveAlarmsIndex_Object=MibTableColumn
ipDectActiveAlarmsIndex=_IpDectActiveAlarmsIndex_Object((1,3,6,1,4,1,27614,1,1,1,2,2,1,1),_IpDectActiveAlarmsIndex_Type())
ipDectActiveAlarmsIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ipDectActiveAlarmsIndex.setStatus(_A)
_IpDectAlarmDate_Type=OctetString
_IpDectAlarmDate_Object=MibTableColumn
ipDectAlarmDate=_IpDectAlarmDate_Object((1,3,6,1,4,1,27614,1,1,1,2,2,1,2),_IpDectAlarmDate_Type())
ipDectAlarmDate.setMaxAccess(_B)
if mibBuilder.loadTexts:ipDectAlarmDate.setStatus(_A)
_IpDectAlarmTime_Type=OctetString
_IpDectAlarmTime_Object=MibTableColumn
ipDectAlarmTime=_IpDectAlarmTime_Object((1,3,6,1,4,1,27614,1,1,1,2,2,1,3),_IpDectAlarmTime_Type())
ipDectAlarmTime.setMaxAccess(_B)
if mibBuilder.loadTexts:ipDectAlarmTime.setStatus(_A)
class _IpDectAlarmCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(65537,65538,65539,196609,196865,197121,197122,197123,197124,197125,197126,197127,197128,197136,197377,197378,197379,197380,197633,327681,327682,327683,327684,327686,327688,327689,393217,393218,393219,393220,393221,393222,458753,458755,458756,458757,458759,458763,524289,524290,720897,786954,786964,786965,786966,786974,786984,786985,786986,786987,786988,786989,786990,786991,786992,786993,786994,786995,787004,787014,787015,787024,787034,787044,787459,787462,787463,790528,790529,917505,917506,917507,917508,917509,917510,917512,917513,917514,983041,983042,983044,983048,983056,1048577,1048578,1048580,1048584,1114112,1114113,1114114,1114137,1114138,1114139,1114177,1114182,1114183,1114185,1114192,1114193,1114195,1114202,1114203,1114204,1114205,1114206,1114207,1179649,1310721,1310821,1310822,1310823,1376257,1638401,1638402,1703937,1704192,2097152,2162689,2162690,2162691,2162692,2162693,2162694)));namedValues=NamedValues(*((_J,65537),(_K,65538),(_L,65539),(_M,196609),(_N,196865),(_O,197121),(_P,197122),(_Q,197123),(_R,197124),(_S,197125),(_T,197126),(_U,197127),(_V,197128),(_W,197136),(_X,197377),(_Y,197378),(_Z,197379),(_a,197380),(_b,197633),(_c,327681),(_d,327682),(_e,327683),(_f,327684),(_g,327686),(_h,327688),(_i,327689),(_j,393217),(_k,393218),(_l,393219),(_m,393220),(_n,393221),(_o,393222),(_p,458753),(_q,458755),(_r,458756),(_s,458757),(_t,458759),(_u,458763),(_v,524289),(_w,524290),(_x,720897),(_y,786954),(_z,786964),(_A0,786965),(_A1,786966),(_A2,786974),(_A3,786984),(_A4,786985),(_A5,786986),(_A6,786987),(_A7,786988),(_A8,786989),(_A9,786990),(_AA,786991),(_AB,786992),(_AC,786993),(_AD,786994),(_AE,786995),(_AF,787004),(_AG,787014),(_AH,787015),(_AI,787024),(_AJ,787034),(_AK,787044),(_AL,787459),(_AM,787462),(_AN,787463),(_AO,790528),(_AP,790529),(_AQ,917505),(_AR,917506),(_AS,917507),(_AT,917508),(_AU,917509),(_AV,917510),(_AW,917512),(_AX,917513),(_AY,917514),(_AZ,983041),(_Aa,983042),(_Ab,983044),(_Ac,983048),(_Ad,983056),(_Ae,1048577),(_Af,1048578),('syncLost',1048580),(_Ag,1048584),(_Ah,1114112),(_Ai,1114113),(_Aj,1114114),(_Ak,1114137),(_Al,1114138),(_Am,1114139),(_An,1114177),(_Ao,1114182),(_Ap,1114183),(_Aq,1114185),(_Ar,1114192),(_As,1114193),(_At,1114195),(_Au,1114202),(_Av,1114203),(_Aw,1114204),(_Ax,1114205),(_Ay,1114206),(_Az,1114207),(_A_,1179649),(_B0,1310721),(_B1,1310821),(_B2,1310822),(_B3,1310823),(_B4,1376257),(_B5,1638401),(_B6,1638402),(_B7,1703937),(_B8,1704192),(_B9,2097152),(_BA,2162689),(_BB,2162690),(_BC,2162691),(_BD,2162692),(_BE,2162693),(_BF,2162694)))
_IpDectAlarmCode_Type.__name__=_E
_IpDectAlarmCode_Object=MibTableColumn
ipDectAlarmCode=_IpDectAlarmCode_Object((1,3,6,1,4,1,27614,1,1,1,2,2,1,4),_IpDectAlarmCode_Type())
ipDectAlarmCode.setMaxAccess(_B)
if mibBuilder.loadTexts:ipDectAlarmCode.setStatus(_A)
class _IpDectAlarmSeverity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_BG,0),('major',1),('critical',2)))
_IpDectAlarmSeverity_Type.__name__=_E
_IpDectAlarmSeverity_Object=MibTableColumn
ipDectAlarmSeverity=_IpDectAlarmSeverity_Object((1,3,6,1,4,1,27614,1,1,1,2,2,1,5),_IpDectAlarmSeverity_Type())
ipDectAlarmSeverity.setMaxAccess(_B)
if mibBuilder.loadTexts:ipDectAlarmSeverity.setStatus(_A)
_IpDectAlarmSource_Type=OctetString
_IpDectAlarmSource_Object=MibTableColumn
ipDectAlarmSource=_IpDectAlarmSource_Object((1,3,6,1,4,1,27614,1,1,1,2,2,1,6),_IpDectAlarmSource_Type())
ipDectAlarmSource.setMaxAccess(_B)
if mibBuilder.loadTexts:ipDectAlarmSource.setStatus(_A)
_IpDectAlarmIp_Type=IpAddress
_IpDectAlarmIp_Object=MibTableColumn
ipDectAlarmIp=_IpDectAlarmIp_Object((1,3,6,1,4,1,27614,1,1,1,2,2,1,7),_IpDectAlarmIp_Type())
ipDectAlarmIp.setMaxAccess(_B)
if mibBuilder.loadTexts:ipDectAlarmIp.setStatus(_A)
_IpDectAlarmDescription_Type=OctetString
_IpDectAlarmDescription_Object=MibTableColumn
ipDectAlarmDescription=_IpDectAlarmDescription_Object((1,3,6,1,4,1,27614,1,1,1,2,2,1,8),_IpDectAlarmDescription_Type())
ipDectAlarmDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:ipDectAlarmDescription.setStatus(_A)
ascomColdStart=NotificationType((1,3,6,1,4,1,27614,0,0))
if mibBuilder.loadTexts:ascomColdStart.setStatus(_A)
ascomWarmStart=NotificationType((1,3,6,1,4,1,27614,0,1))
if mibBuilder.loadTexts:ascomWarmStart.setStatus(_A)
ascomLinkDown=NotificationType((1,3,6,1,4,1,27614,0,2))
ascomLinkDown.setObjects((_F,_G))
if mibBuilder.loadTexts:ascomLinkDown.setStatus(_A)
ascomLinkUp=NotificationType((1,3,6,1,4,1,27614,0,3))
ascomLinkUp.setObjects((_F,_G))
if mibBuilder.loadTexts:ascomLinkUp.setStatus(_A)
ascomAuthenticationFailure=NotificationType((1,3,6,1,4,1,27614,0,4))
if mibBuilder.loadTexts:ascomAuthenticationFailure.setStatus(_A)
ipDectSetCriticalAlarmTrap=NotificationType((1,3,6,1,4,1,27614,0,11))
ipDectSetCriticalAlarmTrap.setObjects((_C,_D))
if mibBuilder.loadTexts:ipDectSetCriticalAlarmTrap.setStatus(_A)
ipDectSetMajorAlarmTrap=NotificationType((1,3,6,1,4,1,27614,0,12))
ipDectSetMajorAlarmTrap.setObjects((_C,_D))
if mibBuilder.loadTexts:ipDectSetMajorAlarmTrap.setStatus(_A)
ipDectSetMinorAlarmTrap=NotificationType((1,3,6,1,4,1,27614,0,13))
ipDectSetMinorAlarmTrap.setObjects((_C,_D))
if mibBuilder.loadTexts:ipDectSetMinorAlarmTrap.setStatus(_A)
ipDectSetIndeterminateAlarmTrap=NotificationType((1,3,6,1,4,1,27614,0,14))
ipDectSetIndeterminateAlarmTrap.setObjects((_C,_D))
if mibBuilder.loadTexts:ipDectSetIndeterminateAlarmTrap.setStatus(_A)
ipDectClearAlarmTrap=NotificationType((1,3,6,1,4,1,27614,0,15))
ipDectClearAlarmTrap.setObjects((_C,_D))
if mibBuilder.loadTexts:ipDectClearAlarmTrap.setStatus(_A)
ipDectCriticalFaultTrap=NotificationType((1,3,6,1,4,1,27614,0,16))
ipDectCriticalFaultTrap.setObjects((_C,_D))
if mibBuilder.loadTexts:ipDectCriticalFaultTrap.setStatus(_A)
ipDectMajorFaultTrap=NotificationType((1,3,6,1,4,1,27614,0,17))
ipDectMajorFaultTrap.setObjects((_C,_D))
if mibBuilder.loadTexts:ipDectMajorFaultTrap.setStatus(_A)
ipDectMinorFaultTrap=NotificationType((1,3,6,1,4,1,27614,0,18))
ipDectMinorFaultTrap.setObjects((_C,_D))
if mibBuilder.loadTexts:ipDectMinorFaultTrap.setStatus(_A)
ipDectIndeterminateFaultTrap=NotificationType((1,3,6,1,4,1,27614,0,19))
ipDectIndeterminateFaultTrap.setObjects((_C,_D))
if mibBuilder.loadTexts:ipDectIndeterminateFaultTrap.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'ascom':ascom,'ascomTraps':ascomTraps,'ascomColdStart':ascomColdStart,'ascomWarmStart':ascomWarmStart,'ascomLinkDown':ascomLinkDown,'ascomLinkUp':ascomLinkUp,'ascomAuthenticationFailure':ascomAuthenticationFailure,'ipDectSetCriticalAlarmTrap':ipDectSetCriticalAlarmTrap,'ipDectSetMajorAlarmTrap':ipDectSetMajorAlarmTrap,'ipDectSetMinorAlarmTrap':ipDectSetMinorAlarmTrap,'ipDectSetIndeterminateAlarmTrap':ipDectSetIndeterminateAlarmTrap,'ipDectClearAlarmTrap':ipDectClearAlarmTrap,'ipDectCriticalFaultTrap':ipDectCriticalFaultTrap,'ipDectMajorFaultTrap':ipDectMajorFaultTrap,'ipDectMinorFaultTrap':ipDectMinorFaultTrap,'ipDectIndeterminateFaultTrap':ipDectIndeterminateFaultTrap,'ascomMibs':ascomMibs,'ascomIpdect':ascomIpdect,'ascomIpdectMIB':ascomIpdectMIB,'ipDectAttr':ipDectAttr,'ipDectFaultLogEntries':ipDectFaultLogEntries,'ipDectAlarmLogEntries':ipDectAlarmLogEntries,_D:ipDectLastErrorCode,'ipDectFaults':ipDectFaults,'ipDectFaultLogTable':ipDectFaultLogTable,'ipDectFaultLogEntry':ipDectFaultLogEntry,_I:ipDectFaultIndex,'ipDectFaultDate':ipDectFaultDate,'ipDectFaultTime':ipDectFaultTime,'ipDectFaultActivity':ipDectFaultActivity,'ipDectFaultCode':ipDectFaultCode,'ipDectFaultSeverity':ipDectFaultSeverity,'ipDectFaultSource':ipDectFaultSource,'ipDectFaultIp':ipDectFaultIp,'ipDectFaultDescription':ipDectFaultDescription,'ipDectActiveAlarmsTable':ipDectActiveAlarmsTable,'ipDectActiveAlarmsEntry':ipDectActiveAlarmsEntry,_BH:ipDectActiveAlarmsIndex,'ipDectAlarmDate':ipDectAlarmDate,'ipDectAlarmTime':ipDectAlarmTime,'ipDectAlarmCode':ipDectAlarmCode,'ipDectAlarmSeverity':ipDectAlarmSeverity,'ipDectAlarmSource':ipDectAlarmSource,'ipDectAlarmIp':ipDectAlarmIp,'ipDectAlarmDescription':ipDectAlarmDescription})