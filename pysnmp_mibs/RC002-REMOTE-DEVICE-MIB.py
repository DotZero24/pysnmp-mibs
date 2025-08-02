_B4='rcftRemoteMoudleE1Status'
_B3='rcftRemoteMoudleEthFeStatus'
_B2='rcftRemoteMoudleExist'
_B1='rcftRemoteDS1PortFaultPassIndicator'
_B0='rcftRemoteSHDSLPortESThreshold'
_A_='rcftRemoteSHDSLPortLOLKThreshold'
_Az='rcftRemoteSHDSLPortLOSWThreshold'
_Ay='rcftRemoteSHDSLPortLOSThreshold'
_Ax='rcftRemoteSHDSLPortAttenuationThreshold'
_Aw='rcftRemoteSHDSLPortSNRThreshold'
_Av='rcftRemoteEthFxPortSFPInfo'
_Au='rcftRemoteEthFxPortExist'
_At='rcftRemoteEthFxPortLink'
_As='rcftRemoteEthFxPortSD'
_Ar='rcftRemoteEthFxPortLaserAbnormal'
_Aq='rcftRemoteEthFxPortRxSensitiveAbnormal'
_Ap='rcftRemoteEthFxPortTxPowerAbnormal'
_Ao='rcftRemoteEthFxPortTLK'
_An='rcftRemoteEthFxPortRLK'
_Am='rcftRemoteEthFeLinkStatus'
_Al='rcftRemoteDevicePowerDown'
_Ak='rcftRemoteSysTemperature'
_Aj='rcftRemoteDeviceExist'
_Ai='rcftRemoteVCGStatisticEntry'
_Ah='rcftRemoteMoudleE1StatisticEntry'
_Ag='rcftRemoteMoudleEthFeStatisticEntry'
_Af='rcftRemoteDS1StatisticEntry'
_Ae='rcftRemoteDS3E3StatisticEntry'
_Ad='rcftRemoteE1StatisticEntry'
_Ac='rcftRemoteEthFxStatisticEntry'
_Ab='rcftRemoteEthFeStatisticEntry'
_Aa='rcftRemoteVCGIndex'
_AZ='rcftRemotePortIndex'
_AY='rcftRemoteVLANIndex'
_AX='rcftRemoteSimpleModuleIndex'
_AW='rcftRemoteDataPortIndex'
_AV='rcftRemoteVideoPortIndex'
_AU='rcftRemoteAudioPortIndex'
_AT='rcftRemoteMoudleV35Index'
_AS='rcftRemoteMoudleE1Index'
_AR='rcftRemoteMoudlePdhIndex'
_AQ='rcftRemoteMoudleEthFeIndex'
_AP='rcftRemoteDS1PortIndex'
_AO='rcftRemotePdhPortIndex'
_AN='rcftRemoteDS3E3PortIndex'
_AM='rcftRemoteV35PortIndex'
_AL='rcftRemoteSHDSLPortIntervalDayNumber'
_AK='rcftRemoteSHDSLPortIntervalNumber'
_AJ='localOutSideLoopEnable'
_AI='localInSideLoopEnale'
_AH='transparent'
_AG='rcftRemoteE1Index'
_AF='rcftRemoteEthFxIntervalNumber'
_AE='unknown-type'
_AD='optical-SFP'
_AC='optical-S15'
_AB='optical-SS35'
_AA='optical-SS34'
_A9='optical-SS25'
_A8='optical-SS23'
_A7='optical-SS15'
_A6='optical-SS13'
_A5='optical-S3'
_A4='optical-S2'
_A3='optical-S1'
_A2='optical-M'
_A1='half-duplex'
_A0='full-duplex'
_z='rcft10Gbps'
_y='rcft1000Mbps'
_x='rcft100Mbps'
_w='rcft10Mbps'
_v='secondary'
_u='1909-05-26 00:00'
_t='rcftRemoteMoudlePdhAlarmStatus'
_s='rcftRemoteT1AlarmStatus'
_r='rcftRemoteE1TransErrorCode'
_q='rcftRemoteDeviceStatus'
_p='rcftRemoteSysVoltageStatus'
_o='remoteDoubleLoopDisable'
_n='remoteDoubleLoopEnable'
_m='localDoubleLoopDisable'
_l='localDoubleLoopEnable'
_k='abnormal'
_j='unlink'
_i='link'
_h='rcftRemoteEthFeIndex'
_g='exist'
_f='rcftRemoteVideoPortStatus'
_e='rcftRemoteToLVCGMemberAlarmStatus'
_d='rcftRemoteVCGMemberAlarmStatus'
_c='rcftRemoteToLocalE1AlarmStatus'
_b='rcftRemoteEthFxIndex'
_a='close'
_Z='open'
_Y='rcftRemoteMoudleE1AlarmStatus'
_X='rcftRemoteSHDSLPortAlarmStatus'
_W='rcftRemoteMoudleIndex'
_V='rcftRemoteSHDSLPortIndex'
_U='normal'
_T='rcftRemoteVCGAlarmStatus'
_S='rcftRemotePdhPortAlarmStatus'
_R='rcftRemoteEthFxSFPDiagnoWarningStatus'
_Q='rcftRemoteE1AlarmStatus'
_P='disable'
_O='enable'
_N='rcftRemoteDS1PortAlarmStatus'
_M='rcftRemoteEthFxSFPDiagnoAlarmStatus'
_L='rcftRemoteV35PortAlarmStatus'
_K='rcftRemoteDS3E3PortAlarmStatus'
_J='rcftRemoteDeviceIndex'
_I='rcftSlotIndex'
_H='rcftChassisIndex'
_G='OctetString'
_F='RAISECOM-RCFT-MIB'
_E='Integer32'
_D='read-write'
_C='RC002-REMOTE-DEVICE-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_G,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
rcftChassisIndex,rcftMibObjects,rcftSlotIndex=mibBuilder.importSymbols(_F,_H,'rcftMibObjects',_I)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeStamp')
rcftRemoteDeviceMib=ModuleIdentity((1,3,6,1,4,1,8886,2,1,6))
if mibBuilder.loadTexts:rcftRemoteDeviceMib.setRevisions(('1905-07-04 00:00','1909-01-09 00:00','1909-01-21 00:00','1909-02-09 00:00','1909-03-17 00:00','1909-03-24 00:00','1909-04-15 00:00','1909-05-14 00:00','1909-05-15 00:00','1909-05-19 00:00',_u,_u,'1909-05-27 16:00','1909-06-09 16:00','1909-07-02 16:00','1909-07-17 16:00','1909-08-19 00:00','1909-08-21 16:00','1909-09-02 10:00','1909-09-08 14:30','1909-09-09 11:30','1909-09-09 16:30','1909-09-18 00:00','1909-09-27 00:00','1909-10-30 10:06','1909-12-21 00:00','1910-03-03 00:00','1910-03-04 00:00','1910-03-10 00:00','1910-09-29 09:50','1910-10-22 16:57','1910-11-15 00:00','1911-12-19 17:25','1912-03-02 00:00'))
_RcftRemoteDeviceSystemMIB_ObjectIdentity=ObjectIdentity
rcftRemoteDeviceSystemMIB=_RcftRemoteDeviceSystemMIB_ObjectIdentity((1,3,6,1,4,1,8886,2,1,6,1))
_RcftRemoteDeviceSysObjects_ObjectIdentity=ObjectIdentity
rcftRemoteDeviceSysObjects=_RcftRemoteDeviceSysObjects_ObjectIdentity((1,3,6,1,4,1,8886,2,1,6,1,1))
_RcftRemoteDeviceSysTable_Object=MibTable
rcftRemoteDeviceSysTable=_RcftRemoteDeviceSysTable_Object((1,3,6,1,4,1,8886,2,1,6,1,1,1))
if mibBuilder.loadTexts:rcftRemoteDeviceSysTable.setStatus(_A)
_RcftRemoteDeviceSysEntry_Object=MibTableRow
rcftRemoteDeviceSysEntry=_RcftRemoteDeviceSysEntry_Object((1,3,6,1,4,1,8886,2,1,6,1,1,1,1))
rcftRemoteDeviceSysEntry.setIndexNames((0,_F,_H),(0,_F,_I),(0,_C,_J))
if mibBuilder.loadTexts:rcftRemoteDeviceSysEntry.setStatus(_A)
_RcftRemoteDeviceIndex_Type=Integer32
_RcftRemoteDeviceIndex_Object=MibTableColumn
rcftRemoteDeviceIndex=_RcftRemoteDeviceIndex_Object((1,3,6,1,4,1,8886,2,1,6,1,1,1,1,1),_RcftRemoteDeviceIndex_Type())
rcftRemoteDeviceIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteDeviceIndex.setStatus(_A)
class _RcftRemoteDeviceExist_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_g,1),('noexist',2)))
_RcftRemoteDeviceExist_Type.__name__=_E
_RcftRemoteDeviceExist_Object=MibTableColumn
rcftRemoteDeviceExist=_RcftRemoteDeviceExist_Object((1,3,6,1,4,1,8886,2,1,6,1,1,1,1,2),_RcftRemoteDeviceExist_Type())
rcftRemoteDeviceExist.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteDeviceExist.setStatus(_A)
class _RcftRemoteDeviceType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(5394,20001,20002,20003,20004,20005,20006,20007,20008,20009,20010,20011,20012,20013,20014,20015,20016,20017,20018,20019,20020,20021,20022,20023,20024,20025,20026,20027,20028,20029,20030,20031,20032,20033,20034,20035,20036,20037,20038,20039,20040,20041,20042,20043,20044,20045,20046,20047,20048,20049,20050,20051,20052,20053,20054,20055,20056,20057,20058,20059,20060,20061,20062,20063,20064,20065,20066,20067,20068,20069,20070,20073,20074,20075,20076,20077,20078,20079,21001,21002,21003,21004,21005,21006,21007,22050,22051,22052,22053,22054,22055,22056,22057,22058,22059,22060,22061,22062,22063,22064,22065,22066,22070,22071,22072,22073,22074,22075,22076,22077,22078,22079,22081,22082,22083,22084,25004,25005,25006,25007,26008,26011,26099,26100,45313,45314,45318,62128,62471,62514,62518,62521,62526,62529,62533,62536,62540,62543,62546,62550,62553,62557,62560,62563,62567,62571,62575,62578,62582,62589,62592,62595,62598,62603,62606,62607,62611,62615,62616,62618,64769,64770,64771,206915,206918,206919)));namedValues=NamedValues(*(('rcftTypeRCMS2802-240GE-REV-A-REMOTE',5394),('rcftTypeRC501-FE-REV-C',20001),('rcftTypeRC601-FE-REV-C',20002),('rcftTypeRC511-FE-REV-A',20003),('rcftTypeRC952-FEE1-REV-A',20004),('rcftTypeRC952-FXE1-REV-A',20005),('rcftTypeRC601-FE-REV-E',20006),('rcftTypeRC511-4FE-REV-A',20007),('rcftTypeRC511-FE-C-REV-A',20008),('rcftTypeRC951-FEE1-REV-A',20009),('rcftTypeRC513-FE-REV-A',20010),('rcftTypeRC513-FE-C-REV-A',20011),('rcftTypeRC954-FE4E1-REV-A',20012),('rcftTypeRC954-FX4E1-REV-A',20013),('rcftTypeRC953-FE4E1-REV-A',20014),('rcftTypeRC953-FX4E1-REV-A',20015),('rcftTypeRC953-FE8E1-REV-A',20016),('rcftTypeRC953-FX8E1-REV-A',20017),('rcftTypeRC953-FE8E1-BL-REV-A',20018),('rcftTypeRC953-FX8E1-BL-REV-A',20019),('rcftTypeRC532-FE-REV-A',20020),('rcftTypeRC531-FE-REV-A',20021),('rcftTypeRC532-2FE-REV-A',20022),('rcftTypeRC1102-E1-SLAVE-REV-B1',20023),('rcftTypeRC1102-E1-SLAVE-BL-REV-A1',20024),('rcftTypeRC954-2FE4E1-BL-REV-A',20025),('rcftTypeRC954-FE4E1-BL-REV-A',20026),('rcftTypeRC954-FX4E1-BL-REV-A',20027),('rcftTypeRC954-2FE8E1-BL-REV-A',20028),('rcftTypeRC1102-V35-REV-A1',20029),('rcftTypeRC1102-V35-REV-B',20030),('rcftTypeRC602-GEF-REV-B',20031),('rcftTypeRC802-DS3E3-REV-A',20032),('rcftTypeE-SUBM-FE4E1-A',20033),('rcftTypeRC954-FE8E1-REV-A',20034),('rcftTypeRC1102-E1-REV-B2',20035),('rcftTypeRC1102-E1-BL-REV-A2',20036),('rcftTypeRC952-FE-DS3E3-REV-A-SLAVE',20037),('rcftTypeRC802-DS1-REV-A-SLAVE',20038),('rcftTypeRC952-FE-DS1-REV-A-SLAVE',20039),('rcftTypeRC952-FE-DS3E3-F-REV-A-SLAVE',20040),('rcftTypeRC852-30-SLAVE-REV-B',20041),('rcftTypeRC951-4FEE1-REV-A',20042),('rcftTypeRC512-FE-REV-A-SLAVE-M',20043),('rcftTypeRC512-FE-REV-A-SLAVE-S1',20044),('rcftTypeRC512-FE-REV-A-SLAVE-S2',20045),('rcftTypeRC512-FE-REV-A-SLAVE-S3',20046),('rcftTypeRC512-FE-REV-A-SLAVE-noOptical',20047),('rcftTypeRC512-FE-REV-A-SLAVE-SS13',20048),('rcftTypeRC512-FE-REV-A-SLAVE-SS23',20049),('rcftTypeRC512-FE-REV-A-SLAVE-SS34',20050),('rcftTypeRC512-FE-REV-A-S-M',20051),('rcftTypeRC512-FE-REV-A-S-S1',20052),('rcftTypeRC512-FE-REV-A-S-S2',20053),('rcftTypeRC512-FE-REV-A-S-S3',20054),('rcftTypeRC512-FE-REV-A-S-noOptical',20055),('rcftTypeRC512-FE-REV-A-S-SS13',20056),('rcftTypeRC512-FE-REV-A-S-SS23',20057),('rcftTypeRC512-FE-REV-A-S-SS34',20058),('rcftTypeRC512-FE-REV-A-C-M',20059),('rcftTypeRC512-FE-REV-A-C-S1',20060),('rcftTypeRC512-FE-REV-A-C-S2',20061),('rcftTypeRC512-FE-REV-A-C-S3',20062),('rcftTypeRC512-FE-REV-A-C-noOptical',20063),('rcftTypeRC512-FE-REV-A-C-SS13',20064),('rcftTypeRC512-FE-REV-A-C-SS23',20065),('rcftTypeRC512-FE-REV-A-C-SS34',20066),('rcftTypeRC952-FXE1-REV-C-SLAVE',20067),('rcftTypeRC511-4FE-REV-B-SLAVE',20068),('rcftTypeRC952-FEE1-REV-B-REMOTE',20069),('rcftTypeRC906H-FEE1-REMOTE-PRIVATE',20070),('rcftTypeRC521H-FE-DoubleFiber-S',20073),('rcftTypeRC521H-FE-SingleFiber-S',20074),('rcftTypeRC521H-FE-S',20075),('rcftTypeRC522E-FE-REMOTE',20076),('rcftTypeRC521E-FE',20077),('rcftTypeRC512-FE',20078),('rcftTypeRC512-FE-SLAVE',20079),('rcftTypeRC551-FE-REV-A',21001),('rcftTypeRC551-GE-REV-A',21002),('rcftTypeRC551-4FE-REV-A',21003),('rcftTypeRC551-GE-REV-A1',21004),('rcftTypeRC552-GE-REV-C',21005),('rcftTypeRC954-FX8E1-REV-A',21006),('rcftTypeRC552-FE-REV-B',21007),('rcftTypeRC831-120-REV-A',22050),('rcftTypeRC831-240-REV-A',22051),('rcftTypeRC831-240E-REV-A',22052),('rcftTypeRC831-30-FV35-REV-A',22053),('rcftTypeRC831-60-FV35-REV-A',22054),('rcftTypeRC832-30-SLAVE-REV-A',22055),('rcftTypeRC832-30-FV35-SLAVE-REV-A',22056),('rcftTypeRC832-60-SLAVE-REV-A',22057),('rcftTypeRC832-120L-SLAVE-REV-A',22058),('rcftTypeRC832-240L-SLAVE-REV-A',22059),('rcftTypeRCMS2801-30FE-FV35-REV-A',22060),('rcftTypeRCMS2801-60FE-FV35-REV-A',22061),('rcftTypeRCMS2801-120FE-SLAVE-REV-A',22062),('rcftTypeRCMS2801-240FE-SLAVE-REV-A',22063),('rcftTypeRCMS2801-240EFE-SLAVE-REV-A',22064),('rcftTypeRCMS2802-30FE-SLAVE-REV-A',22065),('rcftTypeRCMS2802-60FE-SLAVE-REV-A',22066),('rcftTypeRCMS2802-120LFE-SLAVE-REV-A',22070),('rcftTypeRCMS2802-240LFE-SLAVE-REV-A',22071),('rcftTypeRC832-30-FV35-SLAVE-REVB',22072),('rcftTypeRC804-30B-S1-SLAVE-REV-A',22073),('rcftTypeRC806-30B-S1-SLAVE-REV-A',22074),('rcftTypeRC832-30-FV35-SLAVE-REVA1',22075),('rcftTypeRC831-30-FV35-SLAVE-REVA1',22076),('rcftTypeRC831-60-FV35-SLAVE-REVA1',22077),('rcftTypeRCMS2801-30FE-FV35-SLAVE-REVA1',22078),('rcftTypeRCMS2801-60FE-FV35-SLAVE-REVA1',22079),('rcftTypeRCMS2802-2T1-FE-SLAVE-REV-A',22081),('rcftTypeRCMS2802-4T1-FE-SLAVE-REV-A',22082),('rcftTypeRCMS2802-8T1-FE-SLAVE-REV-A',22083),('rcftTypeRCMS2802-60FX-SLAVE-REV-A',22084),('rcftTypeRC1101-FEV35E1-REV-A',25004),('rcftTypeRC1102-FE-REV-B-SLAVE',25005),('rcftTypeRC1102-FE-4W-REV-A-SLAVE',25006),('rcftTypeRC1101-FE-V35E1-REV-B',25007),('rcftTypeRCMS2802-120LGE-BL-A-SLAVE',26008),('rcftTypeRCMS2802-240LGE-BL-A-SLAVE',26011),('rcftTypeRCMS2802-60GE-BL-A-SLAVE',26099),('rcftTypeRCMS2802-30GE-BL-A-SLAVE',26100),('rcftTypeRC906H-FEE1-REV-A-REMOTE',45313),('rcftTypeRC906H-FXE1-REV-A-REMOTE',45314),('rcftTypeRC602-GEF-REV-C',45318),('rcftTypeTHIRD-PARTY-PRODUCT',62128),('rcftTypeRCMS2802-60GE-BL-REV-B-REMOTE',62471),('rcftTypeRC904-PE1-REMOTE',62514),('rcftTypeRCMS2802-120LGE-BL-REV-B-REMOTE',62518),('rcftTypeRCMS2802-240LGE-BL-REV-B-REMOTE',62521),('rcftTypeRC958-FE4E1-REV-A-REMOTE',62526),('rcftTypeRC958-FE8E1-REV-A-REMOTE',62529),('rcftTypeRC958-FX4E1-REV-A-REMOTE',62533),('rcftTypeRC958-FX8E1-REV-A-REMOTE',62536),('rcftTypeRC908-FEV35-REV-A-REMOTE',62540),('rcftTypeRC958-FEE1-REV-A-REMOTE',62543),('rcftTypeRC958-FXE1-REV-A-REMOTE',62546),('rcftTypeRC906G-FE4E1-REMOTE',62550),('rcftTypeRC906G-FX4E1-REMOTE',62553),('rcftTypeRC906G-FEE1-REMOTE',62557),('rcftTypeRC906G-FXE1-REMOTE',62560),('rcftTypeRC906G-FE8E1-REMOTE',62563),('rcftTypeRC906G-FX8E1-REMOTE',62567),('rcftTypeRCVS1000-901UL-REMOTE',62571),('rcftTypeRCMS2912-4E1T1GE-REV-A',62575),('rcftTypeRCMS2912-8E1T1GE-REV-A',62578),('rcftTypeRC952-SE1M-REMOTE',62582),('rcftTypeRCMS2902-120LFE-REMOTE',62589),('rcftTypeRCMS2902-240LFE-REMOTE',62592),('rcftTypeRCMS2902-60FE-REMOTE',62595),('rcftTypeRC862-60-REMOTE',62598),('rcftTypeRC862-30-REMOTE',62603),('rcftTypeRC952-CSE1M-REMOTE',62606),('rcftTypeRCMS2911-480FE',62607),('rcftTypeRCMS2912-480FE-REMOTE',62611),('rcftTypeRCMS2912-240FE-REMOTE',62615),('rcftTypeRCMS2901-480EFE',62616),('rcftTypeRC861-480E',62618),('rcftTypeTS1000-UNCONFIG-PRODUCT',64769),('rcftTypeRC521-FE-REV-C',64770),('rcftTypeRC521-FE-REV-D',64771),('rcftTypeRCVS1000-504A',206915),('rcftTypeRCVS1000-501B',206918),('rcftTypeRCVS1000-502B',206919)))
_RcftRemoteDeviceType_Type.__name__=_E
_RcftRemoteDeviceType_Object=MibTableColumn
rcftRemoteDeviceType=_RcftRemoteDeviceType_Object((1,3,6,1,4,1,8886,2,1,6,1,1,1,1,3),_RcftRemoteDeviceType_Type())
rcftRemoteDeviceType.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteDeviceType.setStatus(_A)
class _RcftRemoteDeviceLocalPortType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('ethport',1),('optical',2),('e1port',3),('ghdsl',4)))
_RcftRemoteDeviceLocalPortType_Type.__name__=_E
_RcftRemoteDeviceLocalPortType_Object=MibTableColumn
rcftRemoteDeviceLocalPortType=_RcftRemoteDeviceLocalPortType_Object((1,3,6,1,4,1,8886,2,1,6,1,1,1,1,4),_RcftRemoteDeviceLocalPortType_Type())
rcftRemoteDeviceLocalPortType.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteDeviceLocalPortType.setStatus(_A)
_RcftRemoteDeviceLocalPortIndex_Type=Integer32
_RcftRemoteDeviceLocalPortIndex_Object=MibTableColumn
rcftRemoteDeviceLocalPortIndex=_RcftRemoteDeviceLocalPortIndex_Object((1,3,6,1,4,1,8886,2,1,6,1,1,1,1,5),_RcftRemoteDeviceLocalPortIndex_Type())
rcftRemoteDeviceLocalPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteDeviceLocalPortIndex.setStatus(_A)
class _RcftRemoteDeviceVersionInfo_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,100))
_RcftRemoteDeviceVersionInfo_Type.__name__=_G
_RcftRemoteDeviceVersionInfo_Object=MibTableColumn
rcftRemoteDeviceVersionInfo=_RcftRemoteDeviceVersionInfo_Object((1,3,6,1,4,1,8886,2,1,6,1,1,1,1,6),_RcftRemoteDeviceVersionInfo_Type())
rcftRemoteDeviceVersionInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteDeviceVersionInfo.setStatus(_A)
_RcftRemoteSysTemperature_Type=Integer32
_RcftRemoteSysTemperature_Object=MibTableColumn
rcftRemoteSysTemperature=_RcftRemoteSysTemperature_Object((1,3,6,1,4,1,8886,2,1,6,1,1,1,1,7),_RcftRemoteSysTemperature_Type())
rcftRemoteSysTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteSysTemperature.setStatus(_A)
class _RcftRemoteSysVoltageStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_U,1),('toohigh',2),('toolow',3)))
_RcftRemoteSysVoltageStatus_Type.__name__=_E
_RcftRemoteSysVoltageStatus_Object=MibTableColumn
rcftRemoteSysVoltageStatus=_RcftRemoteSysVoltageStatus_Object((1,3,6,1,4,1,8886,2,1,6,1,1,1,1,8),_RcftRemoteSysVoltageStatus_Type())
rcftRemoteSysVoltageStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteSysVoltageStatus.setStatus(_A)
class _RcftRemoteDeviceWorkMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('masterCtrl',1),('slaveCtrl',2)))
_RcftRemoteDeviceWorkMode_Type.__name__=_E
_RcftRemoteDeviceWorkMode_Object=MibTableColumn
rcftRemoteDeviceWorkMode=_RcftRemoteDeviceWorkMode_Object((1,3,6,1,4,1,8886,2,1,6,1,1,1,1,9),_RcftRemoteDeviceWorkMode_Type())
rcftRemoteDeviceWorkMode.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteDeviceWorkMode.setStatus(_A)
class _RcftRemoteDeviceFrameLen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('framelen1916B',1),('framelen1536B',2),('framelen9728B',3),('framelen1518B',4),('framelen9kB',5),('framelen2048',6)))
_RcftRemoteDeviceFrameLen_Type.__name__=_E
_RcftRemoteDeviceFrameLen_Object=MibTableColumn
rcftRemoteDeviceFrameLen=_RcftRemoteDeviceFrameLen_Object((1,3,6,1,4,1,8886,2,1,6,1,1,1,1,10),_RcftRemoteDeviceFrameLen_Type())
rcftRemoteDeviceFrameLen.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteDeviceFrameLen.setStatus(_A)
class _RcftRemoteDeviceOrder_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,17,24,25)));namedValues=NamedValues(*(('reset',1),('reqInfoStart',2),('reqInfoStop',3),('shdslPortReset',4),('shdslPortInisdeLoopEnable',5),('shdslPortOutsideLoopEnable',6),('shdslPortInisdeLoopDisable',7),('shdslPortOutsideLoopDisable',8),('e1UnUsedAlarmMask',9),('e1UnUsedAlarmUnMask',10),('pdhPortOutsideLoopEnable',11),('ds3E3PortOutsideLoopEnable',12),('allLoopDisable',13),('errorCodeTestEnable',14),('errorCodeTestDisable',15),('portOutsideLoopEnable',17),('statisticInfoClear',24),('defaultConfigData',25)))
_RcftRemoteDeviceOrder_Type.__name__=_E
_RcftRemoteDeviceOrder_Object=MibTableColumn
rcftRemoteDeviceOrder=_RcftRemoteDeviceOrder_Object((1,3,6,1,4,1,8886,2,1,6,1,1,1,1,11),_RcftRemoteDeviceOrder_Type())
rcftRemoteDeviceOrder.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteDeviceOrder.setStatus(_A)
class _RcftRemoteDeviceConfigFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('set',1))
_RcftRemoteDeviceConfigFlag_Type.__name__=_E
_RcftRemoteDeviceConfigFlag_Object=MibTableColumn
rcftRemoteDeviceConfigFlag=_RcftRemoteDeviceConfigFlag_Object((1,3,6,1,4,1,8886,2,1,6,1,1,1,1,12),_RcftRemoteDeviceConfigFlag_Type())
rcftRemoteDeviceConfigFlag.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteDeviceConfigFlag.setStatus(_A)
class _RcftRemoteSlotAutoCutErrLineEn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_O,1),(_P,2)))
_RcftRemoteSlotAutoCutErrLineEn_Type.__name__=_E
_RcftRemoteSlotAutoCutErrLineEn_Object=MibTableColumn
rcftRemoteSlotAutoCutErrLineEn=_RcftRemoteSlotAutoCutErrLineEn_Object((1,3,6,1,4,1,8886,2,1,6,1,1,1,1,13),_RcftRemoteSlotAutoCutErrLineEn_Type())
rcftRemoteSlotAutoCutErrLineEn.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteSlotAutoCutErrLineEn.setStatus(_A)
class _RcftRemotePowerSupply_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ac220v',1),('dc-48v',2),('dc24v',3)))
_RcftRemotePowerSupply_Type.__name__=_E
_RcftRemotePowerSupply_Object=MibTableColumn
rcftRemotePowerSupply=_RcftRemotePowerSupply_Object((1,3,6,1,4,1,8886,2,1,6,1,1,1,1,14),_RcftRemotePowerSupply_Type())
rcftRemotePowerSupply.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemotePowerSupply.setStatus(_A)
class _RcftRemoteDevicePowerDown_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_U,1),('powerdown',2)))
_RcftRemoteDevicePowerDown_Type.__name__=_E
_RcftRemoteDevicePowerDown_Object=MibTableColumn
rcftRemoteDevicePowerDown=_RcftRemoteDevicePowerDown_Object((1,3,6,1,4,1,8886,2,1,6,1,1,1,1,15),_RcftRemoteDevicePowerDown_Type())
rcftRemoteDevicePowerDown.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteDevicePowerDown.setStatus(_A)
class _RcftRemoteDeviceClkMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,100)));namedValues=NamedValues(*(('masterClk',1),('e1PortClk',2),('gPortClk',3),(_v,4),('v35PortClk',5),('reserved',100)))
_RcftRemoteDeviceClkMode_Type.__name__=_E
_RcftRemoteDeviceClkMode_Object=MibTableColumn
rcftRemoteDeviceClkMode=_RcftRemoteDeviceClkMode_Object((1,3,6,1,4,1,8886,2,1,6,1,1,1,1,16),_RcftRemoteDeviceClkMode_Type())
rcftRemoteDeviceClkMode.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteDeviceClkMode.setStatus(_A)
_RcftRemoteDeviceE1SubCardType_Type=Integer32
_RcftRemoteDeviceE1SubCardType_Object=MibTableColumn
rcftRemoteDeviceE1SubCardType=_RcftRemoteDeviceE1SubCardType_Object((1,3,6,1,4,1,8886,2,1,6,1,1,1,1,17),_RcftRemoteDeviceE1SubCardType_Type())
rcftRemoteDeviceE1SubCardType.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteDeviceE1SubCardType.setStatus(_A)
class _RcftRemoteDeviceGateway_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_RcftRemoteDeviceGateway_Type.__name__=_G
_RcftRemoteDeviceGateway_Object=MibTableColumn
rcftRemoteDeviceGateway=_RcftRemoteDeviceGateway_Object((1,3,6,1,4,1,8886,2,1,6,1,1,1,1,18),_RcftRemoteDeviceGateway_Type())
rcftRemoteDeviceGateway.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteDeviceGateway.setStatus(_A)
class _RcftRemoteDeviceIP_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_RcftRemoteDeviceIP_Type.__name__=_G
_RcftRemoteDeviceIP_Object=MibTableColumn
rcftRemoteDeviceIP=_RcftRemoteDeviceIP_Object((1,3,6,1,4,1,8886,2,1,6,1,1,1,1,19),_RcftRemoteDeviceIP_Type())
rcftRemoteDeviceIP.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteDeviceIP.setStatus(_A)
class _RcftRemoteDeviceSubnetMask_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_RcftRemoteDeviceSubnetMask_Type.__name__=_G
_RcftRemoteDeviceSubnetMask_Object=MibTableColumn
rcftRemoteDeviceSubnetMask=_RcftRemoteDeviceSubnetMask_Object((1,3,6,1,4,1,8886,2,1,6,1,1,1,1,20),_RcftRemoteDeviceSubnetMask_Type())
rcftRemoteDeviceSubnetMask.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteDeviceSubnetMask.setStatus(_A)
_RcftRemoteDeviceVLANID_Type=Integer32
_RcftRemoteDeviceVLANID_Object=MibTableColumn
rcftRemoteDeviceVLANID=_RcftRemoteDeviceVLANID_Object((1,3,6,1,4,1,8886,2,1,6,1,1,1,1,21),_RcftRemoteDeviceVLANID_Type())
rcftRemoteDeviceVLANID.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteDeviceVLANID.setStatus(_A)
class _RcftRemoteDeviceCommunityRW_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('read',1),('readwrite',2),('clear',3)))
_RcftRemoteDeviceCommunityRW_Type.__name__=_E
_RcftRemoteDeviceCommunityRW_Object=MibTableColumn
rcftRemoteDeviceCommunityRW=_RcftRemoteDeviceCommunityRW_Object((1,3,6,1,4,1,8886,2,1,6,1,1,1,1,22),_RcftRemoteDeviceCommunityRW_Type())
rcftRemoteDeviceCommunityRW.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteDeviceCommunityRW.setStatus(_A)
_RcftRemoteDeviceCommunityLength_Type=Integer32
_RcftRemoteDeviceCommunityLength_Object=MibTableColumn
rcftRemoteDeviceCommunityLength=_RcftRemoteDeviceCommunityLength_Object((1,3,6,1,4,1,8886,2,1,6,1,1,1,1,23),_RcftRemoteDeviceCommunityLength_Type())
rcftRemoteDeviceCommunityLength.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteDeviceCommunityLength.setStatus(_A)
class _RcftRemoteDeviceCommunity_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_RcftRemoteDeviceCommunity_Type.__name__=_G
_RcftRemoteDeviceCommunity_Object=MibTableColumn
rcftRemoteDeviceCommunity=_RcftRemoteDeviceCommunity_Object((1,3,6,1,4,1,8886,2,1,6,1,1,1,1,24),_RcftRemoteDeviceCommunity_Type())
rcftRemoteDeviceCommunity.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteDeviceCommunity.setStatus(_A)
_RcftRemoteDeviceVoltageValue_Type=Unsigned32
_RcftRemoteDeviceVoltageValue_Object=MibTableColumn
rcftRemoteDeviceVoltageValue=_RcftRemoteDeviceVoltageValue_Object((1,3,6,1,4,1,8886,2,1,6,1,1,1,1,25),_RcftRemoteDeviceVoltageValue_Type())
rcftRemoteDeviceVoltageValue.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteDeviceVoltageValue.setStatus(_A)
_RcftRemoteDeviceStatus_Type=Integer32
_RcftRemoteDeviceStatus_Object=MibTableColumn
rcftRemoteDeviceStatus=_RcftRemoteDeviceStatus_Object((1,3,6,1,4,1,8886,2,1,6,1,1,1,1,26),_RcftRemoteDeviceStatus_Type())
rcftRemoteDeviceStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteDeviceStatus.setStatus(_A)
_RcftRemoteSubModuleExist_Type=Integer32
_RcftRemoteSubModuleExist_Object=MibTableColumn
rcftRemoteSubModuleExist=_RcftRemoteSubModuleExist_Object((1,3,6,1,4,1,8886,2,1,6,1,1,1,1,27),_RcftRemoteSubModuleExist_Type())
rcftRemoteSubModuleExist.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteSubModuleExist.setStatus(_A)
class _RcftRemoteMultiE1LoopOrder_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_RcftRemoteMultiE1LoopOrder_Type.__name__=_G
_RcftRemoteMultiE1LoopOrder_Object=MibTableColumn
rcftRemoteMultiE1LoopOrder=_RcftRemoteMultiE1LoopOrder_Object((1,3,6,1,4,1,8886,2,1,6,1,1,1,1,28),_RcftRemoteMultiE1LoopOrder_Type())
rcftRemoteMultiE1LoopOrder.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteMultiE1LoopOrder.setStatus(_A)
_RcftRemoteOrderTimeParameter_Type=Integer32
_RcftRemoteOrderTimeParameter_Object=MibTableColumn
rcftRemoteOrderTimeParameter=_RcftRemoteOrderTimeParameter_Object((1,3,6,1,4,1,8886,2,1,6,1,1,1,1,29),_RcftRemoteOrderTimeParameter_Type())
rcftRemoteOrderTimeParameter.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteOrderTimeParameter.setStatus(_A)
_RcftRemoteOrderModeParameter_Type=Integer32
_RcftRemoteOrderModeParameter_Object=MibTableColumn
rcftRemoteOrderModeParameter=_RcftRemoteOrderModeParameter_Object((1,3,6,1,4,1,8886,2,1,6,1,1,1,1,30),_RcftRemoteOrderModeParameter_Type())
rcftRemoteOrderModeParameter.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteOrderModeParameter.setStatus(_A)
_RcftRemoteSDRAMBuf_Type=Integer32
_RcftRemoteSDRAMBuf_Object=MibTableColumn
rcftRemoteSDRAMBuf=_RcftRemoteSDRAMBuf_Object((1,3,6,1,4,1,8886,2,1,6,1,1,1,1,31),_RcftRemoteSDRAMBuf_Type())
rcftRemoteSDRAMBuf.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteSDRAMBuf.setStatus(_A)
_RcftRemoteRLPStatus_Type=Integer32
_RcftRemoteRLPStatus_Object=MibTableColumn
rcftRemoteRLPStatus=_RcftRemoteRLPStatus_Object((1,3,6,1,4,1,8886,2,1,6,1,1,1,1,32),_RcftRemoteRLPStatus_Type())
rcftRemoteRLPStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteRLPStatus.setStatus(_A)
_RcftRemoteLALStatus_Type=Integer32
_RcftRemoteLALStatus_Object=MibTableColumn
rcftRemoteLALStatus=_RcftRemoteLALStatus_Object((1,3,6,1,4,1,8886,2,1,6,1,1,1,1,33),_RcftRemoteLALStatus_Type())
rcftRemoteLALStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteLALStatus.setStatus(_A)
_RcftRemoteRALStatus_Type=Integer32
_RcftRemoteRALStatus_Object=MibTableColumn
rcftRemoteRALStatus=_RcftRemoteRALStatus_Object((1,3,6,1,4,1,8886,2,1,6,1,1,1,1,34),_RcftRemoteRALStatus_Type())
rcftRemoteRALStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteRALStatus.setStatus(_A)
_RcftRemoteDeviceSwitchStatus_Type=Integer32
_RcftRemoteDeviceSwitchStatus_Object=MibTableColumn
rcftRemoteDeviceSwitchStatus=_RcftRemoteDeviceSwitchStatus_Object((1,3,6,1,4,1,8886,2,1,6,1,1,1,1,35),_RcftRemoteDeviceSwitchStatus_Type())
rcftRemoteDeviceSwitchStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteDeviceSwitchStatus.setStatus(_A)
_RcftRemoteDeviceMoudleExist_Type=Integer32
_RcftRemoteDeviceMoudleExist_Object=MibTableColumn
rcftRemoteDeviceMoudleExist=_RcftRemoteDeviceMoudleExist_Object((1,3,6,1,4,1,8886,2,1,6,1,1,1,1,36),_RcftRemoteDeviceMoudleExist_Type())
rcftRemoteDeviceMoudleExist.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteDeviceMoudleExist.setStatus(_A)
class _RcftRemoteCardInformation_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_RcftRemoteCardInformation_Type.__name__=_G
_RcftRemoteCardInformation_Object=MibTableColumn
rcftRemoteCardInformation=_RcftRemoteCardInformation_Object((1,3,6,1,4,1,8886,2,1,6,1,1,1,1,37),_RcftRemoteCardInformation_Type())
rcftRemoteCardInformation.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteCardInformation.setStatus(_A)
_RcftRemoteSwitchType_Type=Integer32
_RcftRemoteSwitchType_Object=MibTableColumn
rcftRemoteSwitchType=_RcftRemoteSwitchType_Object((1,3,6,1,4,1,8886,2,1,6,1,1,1,1,38),_RcftRemoteSwitchType_Type())
rcftRemoteSwitchType.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteSwitchType.setStatus(_A)
_RcftRemoteConnectMode_Type=Integer32
_RcftRemoteConnectMode_Object=MibTableColumn
rcftRemoteConnectMode=_RcftRemoteConnectMode_Object((1,3,6,1,4,1,8886,2,1,6,1,1,1,1,39),_RcftRemoteConnectMode_Type())
rcftRemoteConnectMode.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteConnectMode.setStatus(_A)
_RcftRemoteQosEnable_Type=Integer32
_RcftRemoteQosEnable_Object=MibTableColumn
rcftRemoteQosEnable=_RcftRemoteQosEnable_Object((1,3,6,1,4,1,8886,2,1,6,1,1,1,1,40),_RcftRemoteQosEnable_Type())
rcftRemoteQosEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteQosEnable.setStatus(_A)
_RcftRemoteBaseCOS_Type=Integer32
_RcftRemoteBaseCOS_Object=MibTableColumn
rcftRemoteBaseCOS=_RcftRemoteBaseCOS_Object((1,3,6,1,4,1,8886,2,1,6,1,1,1,1,41),_RcftRemoteBaseCOS_Type())
rcftRemoteBaseCOS.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteBaseCOS.setStatus(_A)
class _RcftRemoteDSCP_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,65))
_RcftRemoteDSCP_Type.__name__=_G
_RcftRemoteDSCP_Object=MibTableColumn
rcftRemoteDSCP=_RcftRemoteDSCP_Object((1,3,6,1,4,1,8886,2,1,6,1,1,1,1,42),_RcftRemoteDSCP_Type())
rcftRemoteDSCP.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteDSCP.setStatus(_A)
_RcftRemoteQueuesPolicy_Type=Integer32
_RcftRemoteQueuesPolicy_Object=MibTableColumn
rcftRemoteQueuesPolicy=_RcftRemoteQueuesPolicy_Object((1,3,6,1,4,1,8886,2,1,6,1,1,1,1,43),_RcftRemoteQueuesPolicy_Type())
rcftRemoteQueuesPolicy.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteQueuesPolicy.setStatus(_A)
class _RcftRemoteMultiE1AlarmRejectOrder_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_RcftRemoteMultiE1AlarmRejectOrder_Type.__name__=_G
_RcftRemoteMultiE1AlarmRejectOrder_Object=MibTableColumn
rcftRemoteMultiE1AlarmRejectOrder=_RcftRemoteMultiE1AlarmRejectOrder_Object((1,3,6,1,4,1,8886,2,1,6,1,1,1,1,44),_RcftRemoteMultiE1AlarmRejectOrder_Type())
rcftRemoteMultiE1AlarmRejectOrder.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteMultiE1AlarmRejectOrder.setStatus(_A)
_RcftRemoteT1PortPulseWaveForm_Type=Integer32
_RcftRemoteT1PortPulseWaveForm_Object=MibTableColumn
rcftRemoteT1PortPulseWaveForm=_RcftRemoteT1PortPulseWaveForm_Object((1,3,6,1,4,1,8886,2,1,6,1,1,1,1,45),_RcftRemoteT1PortPulseWaveForm_Type())
rcftRemoteT1PortPulseWaveForm.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteT1PortPulseWaveForm.setStatus(_A)
_RcftRemoteT1PortCodeType_Type=Integer32
_RcftRemoteT1PortCodeType_Object=MibTableColumn
rcftRemoteT1PortCodeType=_RcftRemoteT1PortCodeType_Object((1,3,6,1,4,1,8886,2,1,6,1,1,1,1,46),_RcftRemoteT1PortCodeType_Type())
rcftRemoteT1PortCodeType.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteT1PortCodeType.setStatus(_A)
_RcftRemoteDeviceSabitMode_Type=Integer32
_RcftRemoteDeviceSabitMode_Object=MibTableColumn
rcftRemoteDeviceSabitMode=_RcftRemoteDeviceSabitMode_Object((1,3,6,1,4,1,8886,2,1,6,1,1,1,1,47),_RcftRemoteDeviceSabitMode_Type())
rcftRemoteDeviceSabitMode.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteDeviceSabitMode.setStatus(_A)
class _RcftRemoteDeviceApsWaitToRestore_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_RcftRemoteDeviceApsWaitToRestore_Type.__name__=_E
_RcftRemoteDeviceApsWaitToRestore_Object=MibTableColumn
rcftRemoteDeviceApsWaitToRestore=_RcftRemoteDeviceApsWaitToRestore_Object((1,3,6,1,4,1,8886,2,1,6,1,1,1,1,48),_RcftRemoteDeviceApsWaitToRestore_Type())
rcftRemoteDeviceApsWaitToRestore.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteDeviceApsWaitToRestore.setStatus(_A)
_RcftRemoteDeviceCLKChannel_Type=Integer32
_RcftRemoteDeviceCLKChannel_Object=MibTableColumn
rcftRemoteDeviceCLKChannel=_RcftRemoteDeviceCLKChannel_Object((1,3,6,1,4,1,8886,2,1,6,1,1,1,1,49),_RcftRemoteDeviceCLKChannel_Type())
rcftRemoteDeviceCLKChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteDeviceCLKChannel.setStatus(_A)
_RcftRemoteDeviceRmcChannelType_Type=Integer32
_RcftRemoteDeviceRmcChannelType_Object=MibTableColumn
rcftRemoteDeviceRmcChannelType=_RcftRemoteDeviceRmcChannelType_Object((1,3,6,1,4,1,8886,2,1,6,1,1,1,1,50),_RcftRemoteDeviceRmcChannelType_Type())
rcftRemoteDeviceRmcChannelType.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteDeviceRmcChannelType.setStatus(_A)
class _RcftRemoteDeviceProductType_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_RcftRemoteDeviceProductType_Type.__name__=_G
_RcftRemoteDeviceProductType_Object=MibTableColumn
rcftRemoteDeviceProductType=_RcftRemoteDeviceProductType_Object((1,3,6,1,4,1,8886,2,1,6,1,1,1,1,51),_RcftRemoteDeviceProductType_Type())
rcftRemoteDeviceProductType.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteDeviceProductType.setStatus(_A)
_RcftRemoteDeviceProtocolVer_Type=Integer32
_RcftRemoteDeviceProtocolVer_Object=MibTableColumn
rcftRemoteDeviceProtocolVer=_RcftRemoteDeviceProtocolVer_Object((1,3,6,1,4,1,8886,2,1,6,1,1,1,1,52),_RcftRemoteDeviceProtocolVer_Type())
rcftRemoteDeviceProtocolVer.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteDeviceProtocolVer.setStatus(_A)
_RcftRemoteDeviceVenderCode_Type=Integer32
_RcftRemoteDeviceVenderCode_Object=MibTableColumn
rcftRemoteDeviceVenderCode=_RcftRemoteDeviceVenderCode_Object((1,3,6,1,4,1,8886,2,1,6,1,1,1,1,53),_RcftRemoteDeviceVenderCode_Type())
rcftRemoteDeviceVenderCode.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteDeviceVenderCode.setStatus(_A)
_RcftRemoteDeviceModelID_Type=Integer32
_RcftRemoteDeviceModelID_Object=MibTableColumn
rcftRemoteDeviceModelID=_RcftRemoteDeviceModelID_Object((1,3,6,1,4,1,8886,2,1,6,1,1,1,1,54),_RcftRemoteDeviceModelID_Type())
rcftRemoteDeviceModelID.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteDeviceModelID.setStatus(_A)
_RcftRemoteE1PortNumber_Type=Integer32
_RcftRemoteE1PortNumber_Object=MibTableColumn
rcftRemoteE1PortNumber=_RcftRemoteE1PortNumber_Object((1,3,6,1,4,1,8886,2,1,6,1,1,1,1,55),_RcftRemoteE1PortNumber_Type())
rcftRemoteE1PortNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteE1PortNumber.setStatus(_A)
_RcftRemoteDeviceVLANType_Type=Integer32
_RcftRemoteDeviceVLANType_Object=MibTableColumn
rcftRemoteDeviceVLANType=_RcftRemoteDeviceVLANType_Object((1,3,6,1,4,1,8886,2,1,6,1,1,1,1,56),_RcftRemoteDeviceVLANType_Type())
rcftRemoteDeviceVLANType.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteDeviceVLANType.setStatus(_A)
_RcftRemoteDeviceQoSPolicy_Type=Integer32
_RcftRemoteDeviceQoSPolicy_Object=MibTableColumn
rcftRemoteDeviceQoSPolicy=_RcftRemoteDeviceQoSPolicy_Object((1,3,6,1,4,1,8886,2,1,6,1,1,1,1,57),_RcftRemoteDeviceQoSPolicy_Type())
rcftRemoteDeviceQoSPolicy.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteDeviceQoSPolicy.setStatus(_A)
_RcftRemoteDeviceApsE3SwitchDelay_Type=Integer32
_RcftRemoteDeviceApsE3SwitchDelay_Object=MibTableColumn
rcftRemoteDeviceApsE3SwitchDelay=_RcftRemoteDeviceApsE3SwitchDelay_Object((1,3,6,1,4,1,8886,2,1,6,1,1,1,1,58),_RcftRemoteDeviceApsE3SwitchDelay_Type())
rcftRemoteDeviceApsE3SwitchDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteDeviceApsE3SwitchDelay.setStatus(_A)
_RcftRemoteDeviceApsE6SwitchDelay_Type=Integer32
_RcftRemoteDeviceApsE6SwitchDelay_Object=MibTableColumn
rcftRemoteDeviceApsE6SwitchDelay=_RcftRemoteDeviceApsE6SwitchDelay_Object((1,3,6,1,4,1,8886,2,1,6,1,1,1,1,59),_RcftRemoteDeviceApsE6SwitchDelay_Type())
rcftRemoteDeviceApsE6SwitchDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteDeviceApsE6SwitchDelay.setStatus(_A)
_RcftRemoteDeviceVLANTagDirection_Type=Integer32
_RcftRemoteDeviceVLANTagDirection_Object=MibTableColumn
rcftRemoteDeviceVLANTagDirection=_RcftRemoteDeviceVLANTagDirection_Object((1,3,6,1,4,1,8886,2,1,6,1,1,1,1,60),_RcftRemoteDeviceVLANTagDirection_Type())
rcftRemoteDeviceVLANTagDirection.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteDeviceVLANTagDirection.setStatus(_A)
_RcftRemoteDeviceVLANTagModule_Type=Integer32
_RcftRemoteDeviceVLANTagModule_Object=MibTableColumn
rcftRemoteDeviceVLANTagModule=_RcftRemoteDeviceVLANTagModule_Object((1,3,6,1,4,1,8886,2,1,6,1,1,1,1,61),_RcftRemoteDeviceVLANTagModule_Type())
rcftRemoteDeviceVLANTagModule.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteDeviceVLANTagModule.setStatus(_A)
_RcftRemoteDeviceISPTPID_Type=Integer32
_RcftRemoteDeviceISPTPID_Object=MibTableColumn
rcftRemoteDeviceISPTPID=_RcftRemoteDeviceISPTPID_Object((1,3,6,1,4,1,8886,2,1,6,1,1,1,1,62),_RcftRemoteDeviceISPTPID_Type())
rcftRemoteDeviceISPTPID.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteDeviceISPTPID.setStatus(_A)
_RcftRemoteE1DS1PortType_Type=Integer32
_RcftRemoteE1DS1PortType_Object=MibTableColumn
rcftRemoteE1DS1PortType=_RcftRemoteE1DS1PortType_Object((1,3,6,1,4,1,8886,2,1,6,1,1,1,1,63),_RcftRemoteE1DS1PortType_Type())
rcftRemoteE1DS1PortType.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteE1DS1PortType.setStatus(_A)
_RcftRemoteDeviceE1FrameChannel_Type=Integer32
_RcftRemoteDeviceE1FrameChannel_Object=MibTableColumn
rcftRemoteDeviceE1FrameChannel=_RcftRemoteDeviceE1FrameChannel_Object((1,3,6,1,4,1,8886,2,1,6,1,1,1,1,64),_RcftRemoteDeviceE1FrameChannel_Type())
rcftRemoteDeviceE1FrameChannel.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteDeviceE1FrameChannel.setStatus(_A)
_RcftRemoteDeviceManageID_Type=Integer32
_RcftRemoteDeviceManageID_Object=MibTableColumn
rcftRemoteDeviceManageID=_RcftRemoteDeviceManageID_Object((1,3,6,1,4,1,8886,2,1,6,1,1,1,1,65),_RcftRemoteDeviceManageID_Type())
rcftRemoteDeviceManageID.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteDeviceManageID.setStatus(_A)
class _RcftRemoteDeviceMibUse_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('mib002',1),('rccomlib',2)))
_RcftRemoteDeviceMibUse_Type.__name__=_E
_RcftRemoteDeviceMibUse_Object=MibTableColumn
rcftRemoteDeviceMibUse=_RcftRemoteDeviceMibUse_Object((1,3,6,1,4,1,8886,2,1,6,1,1,1,1,66),_RcftRemoteDeviceMibUse_Type())
rcftRemoteDeviceMibUse.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteDeviceMibUse.setStatus(_A)
_RcftRemoteDeviceConfigFlagTable_Object=MibTable
rcftRemoteDeviceConfigFlagTable=_RcftRemoteDeviceConfigFlagTable_Object((1,3,6,1,4,1,8886,2,1,6,1,1,2))
if mibBuilder.loadTexts:rcftRemoteDeviceConfigFlagTable.setStatus(_A)
_RcftRemoteDeviceConfigFlagEntry_Object=MibTableRow
rcftRemoteDeviceConfigFlagEntry=_RcftRemoteDeviceConfigFlagEntry_Object((1,3,6,1,4,1,8886,2,1,6,1,1,2,1))
rcftRemoteDeviceConfigFlagEntry.setIndexNames((0,_F,_H),(0,_F,_I),(0,_C,_J))
if mibBuilder.loadTexts:rcftRemoteDeviceConfigFlagEntry.setStatus(_A)
_RcftRemoteDeviceConfigFinishFlag_Type=Integer32
_RcftRemoteDeviceConfigFinishFlag_Object=MibTableColumn
rcftRemoteDeviceConfigFinishFlag=_RcftRemoteDeviceConfigFinishFlag_Object((1,3,6,1,4,1,8886,2,1,6,1,1,2,1,1),_RcftRemoteDeviceConfigFinishFlag_Type())
rcftRemoteDeviceConfigFinishFlag.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteDeviceConfigFinishFlag.setStatus(_A)
_RcftRemoteDeviceSysTraps_ObjectIdentity=ObjectIdentity
rcftRemoteDeviceSysTraps=_RcftRemoteDeviceSysTraps_ObjectIdentity((1,3,6,1,4,1,8886,2,1,6,1,2))
_RcftRemoteDeviceEthMIB_ObjectIdentity=ObjectIdentity
rcftRemoteDeviceEthMIB=_RcftRemoteDeviceEthMIB_ObjectIdentity((1,3,6,1,4,1,8886,2,1,6,2))
_RcftRemoteDeviceEthFeMIB_ObjectIdentity=ObjectIdentity
rcftRemoteDeviceEthFeMIB=_RcftRemoteDeviceEthFeMIB_ObjectIdentity((1,3,6,1,4,1,8886,2,1,6,2,1))
_RcftRemoteDeviceEthFeObjects_ObjectIdentity=ObjectIdentity
rcftRemoteDeviceEthFeObjects=_RcftRemoteDeviceEthFeObjects_ObjectIdentity((1,3,6,1,4,1,8886,2,1,6,2,1,1))
_RcftRemoteEthFePortTable_Object=MibTable
rcftRemoteEthFePortTable=_RcftRemoteEthFePortTable_Object((1,3,6,1,4,1,8886,2,1,6,2,1,1,1))
if mibBuilder.loadTexts:rcftRemoteEthFePortTable.setStatus(_A)
_RcftRemoteEthFePortEntry_Object=MibTableRow
rcftRemoteEthFePortEntry=_RcftRemoteEthFePortEntry_Object((1,3,6,1,4,1,8886,2,1,6,2,1,1,1,1))
rcftRemoteEthFePortEntry.setIndexNames((0,_F,_H),(0,_F,_I),(0,_C,_J),(0,_C,_h))
if mibBuilder.loadTexts:rcftRemoteEthFePortEntry.setStatus(_A)
_RcftRemoteEthFeIndex_Type=Integer32
_RcftRemoteEthFeIndex_Object=MibTableColumn
rcftRemoteEthFeIndex=_RcftRemoteEthFeIndex_Object((1,3,6,1,4,1,8886,2,1,6,2,1,1,1,1,1),_RcftRemoteEthFeIndex_Type())
rcftRemoteEthFeIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteEthFeIndex.setStatus(_A)
class _RcftRemoteEthFeLinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('linkup',1),('linkdown',2)))
_RcftRemoteEthFeLinkStatus_Type.__name__=_E
_RcftRemoteEthFeLinkStatus_Object=MibTableColumn
rcftRemoteEthFeLinkStatus=_RcftRemoteEthFeLinkStatus_Object((1,3,6,1,4,1,8886,2,1,6,2,1,1,1,1,2),_RcftRemoteEthFeLinkStatus_Type())
rcftRemoteEthFeLinkStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteEthFeLinkStatus.setStatus(_A)
class _RcftRemoteEthFeShutDown_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_Z,1),(_a,2),('closebyLocalOtherPortFault',3),('closebyOppositeFePortFault',4),('closebyLoopBack',5)))
_RcftRemoteEthFeShutDown_Type.__name__=_E
_RcftRemoteEthFeShutDown_Object=MibTableColumn
rcftRemoteEthFeShutDown=_RcftRemoteEthFeShutDown_Object((1,3,6,1,4,1,8886,2,1,6,2,1,1,1,1,3),_RcftRemoteEthFeShutDown_Type())
rcftRemoteEthFeShutDown.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteEthFeShutDown.setStatus(_A)
class _RcftRemoteEthFeAutoNegotiation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('auto',1),('manul',2)))
_RcftRemoteEthFeAutoNegotiation_Type.__name__=_E
_RcftRemoteEthFeAutoNegotiation_Object=MibTableColumn
rcftRemoteEthFeAutoNegotiation=_RcftRemoteEthFeAutoNegotiation_Object((1,3,6,1,4,1,8886,2,1,6,2,1,1,1,1,4),_RcftRemoteEthFeAutoNegotiation_Type())
rcftRemoteEthFeAutoNegotiation.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteEthFeAutoNegotiation.setStatus(_A)
class _RcftRemoteEthFeSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,16)));namedValues=NamedValues(*((_w,1),(_x,2),(_y,3),(_z,4),('other',16)))
_RcftRemoteEthFeSpeed_Type.__name__=_E
_RcftRemoteEthFeSpeed_Object=MibTableColumn
rcftRemoteEthFeSpeed=_RcftRemoteEthFeSpeed_Object((1,3,6,1,4,1,8886,2,1,6,2,1,1,1,1,5),_RcftRemoteEthFeSpeed_Type())
rcftRemoteEthFeSpeed.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteEthFeSpeed.setStatus(_A)
class _RcftRemoteEthFeDuplex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_A0,1),(_A1,2)))
_RcftRemoteEthFeDuplex_Type.__name__=_E
_RcftRemoteEthFeDuplex_Object=MibTableColumn
rcftRemoteEthFeDuplex=_RcftRemoteEthFeDuplex_Object((1,3,6,1,4,1,8886,2,1,6,2,1,1,1,1,6),_RcftRemoteEthFeDuplex_Type())
rcftRemoteEthFeDuplex.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteEthFeDuplex.setStatus(_A)
class _RcftRemoteEthFeFlowControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_O,1),(_P,2)))
_RcftRemoteEthFeFlowControl_Type.__name__=_E
_RcftRemoteEthFeFlowControl_Object=MibTableColumn
rcftRemoteEthFeFlowControl=_RcftRemoteEthFeFlowControl_Object((1,3,6,1,4,1,8886,2,1,6,2,1,1,1,1,7),_RcftRemoteEthFeFlowControl_Type())
rcftRemoteEthFeFlowControl.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteEthFeFlowControl.setStatus(_A)
_RcftRemoteEthFeRestrictSpeed_Type=Integer32
_RcftRemoteEthFeRestrictSpeed_Object=MibTableColumn
rcftRemoteEthFeRestrictSpeed=_RcftRemoteEthFeRestrictSpeed_Object((1,3,6,1,4,1,8886,2,1,6,2,1,1,1,1,8),_RcftRemoteEthFeRestrictSpeed_Type())
rcftRemoteEthFeRestrictSpeed.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteEthFeRestrictSpeed.setStatus(_A)
class _RcftRemoteEthFeFaultPass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_O,1),(_P,2)))
_RcftRemoteEthFeFaultPass_Type.__name__=_E
_RcftRemoteEthFeFaultPass_Object=MibTableColumn
rcftRemoteEthFeFaultPass=_RcftRemoteEthFeFaultPass_Object((1,3,6,1,4,1,8886,2,1,6,2,1,1,1,1,9),_RcftRemoteEthFeFaultPass_Type())
rcftRemoteEthFeFaultPass.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteEthFeFaultPass.setStatus(_A)
class _RcftRemoteEthFeDisabledByRemoteTP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Z,1),(_a,2)))
_RcftRemoteEthFeDisabledByRemoteTP_Type.__name__=_E
_RcftRemoteEthFeDisabledByRemoteTP_Object=MibTableColumn
rcftRemoteEthFeDisabledByRemoteTP=_RcftRemoteEthFeDisabledByRemoteTP_Object((1,3,6,1,4,1,8886,2,1,6,2,1,1,1,1,10),_RcftRemoteEthFeDisabledByRemoteTP_Type())
rcftRemoteEthFeDisabledByRemoteTP.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteEthFeDisabledByRemoteTP.setStatus(_A)
class _RcftRemoteEthFeDisabledByFxToFeFP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Z,1),(_a,2)))
_RcftRemoteEthFeDisabledByFxToFeFP_Type.__name__=_E
_RcftRemoteEthFeDisabledByFxToFeFP_Object=MibTableColumn
rcftRemoteEthFeDisabledByFxToFeFP=_RcftRemoteEthFeDisabledByFxToFeFP_Object((1,3,6,1,4,1,8886,2,1,6,2,1,1,1,1,11),_RcftRemoteEthFeDisabledByFxToFeFP_Type())
rcftRemoteEthFeDisabledByFxToFeFP.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteEthFeDisabledByFxToFeFP.setStatus(_A)
_RcftRemoteEthFeTxRestrictSpeed_Type=Integer32
_RcftRemoteEthFeTxRestrictSpeed_Object=MibTableColumn
rcftRemoteEthFeTxRestrictSpeed=_RcftRemoteEthFeTxRestrictSpeed_Object((1,3,6,1,4,1,8886,2,1,6,2,1,1,1,1,12),_RcftRemoteEthFeTxRestrictSpeed_Type())
rcftRemoteEthFeTxRestrictSpeed.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteEthFeTxRestrictSpeed.setStatus(_A)
class _RcftRemoteEthFeTag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('tag',1),('untag',2)))
_RcftRemoteEthFeTag_Type.__name__=_E
_RcftRemoteEthFeTag_Object=MibTableColumn
rcftRemoteEthFeTag=_RcftRemoteEthFeTag_Object((1,3,6,1,4,1,8886,2,1,6,2,1,1,1,1,13),_RcftRemoteEthFeTag_Type())
rcftRemoteEthFeTag.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteEthFeTag.setStatus(_A)
_RcftRemoteEthFePortStatus_Type=Integer32
_RcftRemoteEthFePortStatus_Object=MibTableColumn
rcftRemoteEthFePortStatus=_RcftRemoteEthFePortStatus_Object((1,3,6,1,4,1,8886,2,1,6,2,1,1,1,1,14),_RcftRemoteEthFePortStatus_Type())
rcftRemoteEthFePortStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteEthFePortStatus.setStatus(_A)
_RcftRemoteEthFeRestrictSpeedStep_Type=Integer32
_RcftRemoteEthFeRestrictSpeedStep_Object=MibTableColumn
rcftRemoteEthFeRestrictSpeedStep=_RcftRemoteEthFeRestrictSpeedStep_Object((1,3,6,1,4,1,8886,2,1,6,2,1,1,1,1,15),_RcftRemoteEthFeRestrictSpeedStep_Type())
rcftRemoteEthFeRestrictSpeedStep.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteEthFeRestrictSpeedStep.setStatus(_A)
_RcftRemoteEthFeOrderTimeParameter_Type=Integer32
_RcftRemoteEthFeOrderTimeParameter_Object=MibTableColumn
rcftRemoteEthFeOrderTimeParameter=_RcftRemoteEthFeOrderTimeParameter_Object((1,3,6,1,4,1,8886,2,1,6,2,1,1,1,1,16),_RcftRemoteEthFeOrderTimeParameter_Type())
rcftRemoteEthFeOrderTimeParameter.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteEthFeOrderTimeParameter.setStatus(_A)
_RcftRemoteEthFeOrderModeParameter_Type=Integer32
_RcftRemoteEthFeOrderModeParameter_Object=MibTableColumn
rcftRemoteEthFeOrderModeParameter=_RcftRemoteEthFeOrderModeParameter_Object((1,3,6,1,4,1,8886,2,1,6,2,1,1,1,1,17),_RcftRemoteEthFeOrderModeParameter_Type())
rcftRemoteEthFeOrderModeParameter.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteEthFeOrderModeParameter.setStatus(_A)
_RcftRemoteEthFeOrder_Type=Integer32
_RcftRemoteEthFeOrder_Object=MibTableColumn
rcftRemoteEthFeOrder=_RcftRemoteEthFeOrder_Object((1,3,6,1,4,1,8886,2,1,6,2,1,1,1,1,18),_RcftRemoteEthFeOrder_Type())
rcftRemoteEthFeOrder.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteEthFeOrder.setStatus(_A)
_RcftRemoteEthFePortStatusExtend_Type=Integer32
_RcftRemoteEthFePortStatusExtend_Object=MibTableColumn
rcftRemoteEthFePortStatusExtend=_RcftRemoteEthFePortStatusExtend_Object((1,3,6,1,4,1,8886,2,1,6,2,1,1,1,1,19),_RcftRemoteEthFePortStatusExtend_Type())
rcftRemoteEthFePortStatusExtend.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteEthFePortStatusExtend.setStatus(_A)
_RcftRemoteEthFeStormControl_Type=Integer32
_RcftRemoteEthFeStormControl_Object=MibTableColumn
rcftRemoteEthFeStormControl=_RcftRemoteEthFeStormControl_Object((1,3,6,1,4,1,8886,2,1,6,2,1,1,1,1,20),_RcftRemoteEthFeStormControl_Type())
rcftRemoteEthFeStormControl.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteEthFeStormControl.setStatus(_A)
_RcftRemoteEthFePVID_Type=Integer32
_RcftRemoteEthFePVID_Object=MibTableColumn
rcftRemoteEthFePVID=_RcftRemoteEthFePVID_Object((1,3,6,1,4,1,8886,2,1,6,2,1,1,1,1,21),_RcftRemoteEthFePVID_Type())
rcftRemoteEthFePVID.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteEthFePVID.setStatus(_A)
_RcftRemoteEthFeDefaultCOS_Type=Integer32
_RcftRemoteEthFeDefaultCOS_Object=MibTableColumn
rcftRemoteEthFeDefaultCOS=_RcftRemoteEthFeDefaultCOS_Object((1,3,6,1,4,1,8886,2,1,6,2,1,1,1,1,22),_RcftRemoteEthFeDefaultCOS_Type())
rcftRemoteEthFeDefaultCOS.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteEthFeDefaultCOS.setStatus(_A)
_RcftRemoteEthFeQoSPolicy_Type=Integer32
_RcftRemoteEthFeQoSPolicy_Object=MibTableColumn
rcftRemoteEthFeQoSPolicy=_RcftRemoteEthFeQoSPolicy_Object((1,3,6,1,4,1,8886,2,1,6,2,1,1,1,1,23),_RcftRemoteEthFeQoSPolicy_Type())
rcftRemoteEthFeQoSPolicy.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteEthFeQoSPolicy.setStatus(_A)
_RcftRemoteEthFeStatisticTable_Object=MibTable
rcftRemoteEthFeStatisticTable=_RcftRemoteEthFeStatisticTable_Object((1,3,6,1,4,1,8886,2,1,6,2,1,1,2))
if mibBuilder.loadTexts:rcftRemoteEthFeStatisticTable.setStatus(_A)
_RcftRemoteEthFeStatisticEntry_Object=MibTableRow
rcftRemoteEthFeStatisticEntry=_RcftRemoteEthFeStatisticEntry_Object((1,3,6,1,4,1,8886,2,1,6,2,1,1,2,1))
if mibBuilder.loadTexts:rcftRemoteEthFeStatisticEntry.setStatus(_A)
_RcftRemoteEthFeTxPackets_Type=Counter32
_RcftRemoteEthFeTxPackets_Object=MibTableColumn
rcftRemoteEthFeTxPackets=_RcftRemoteEthFeTxPackets_Object((1,3,6,1,4,1,8886,2,1,6,2,1,1,2,1,1),_RcftRemoteEthFeTxPackets_Type())
rcftRemoteEthFeTxPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteEthFeTxPackets.setStatus(_A)
_RcftRemoteEthFeTxBytes_Type=Counter32
_RcftRemoteEthFeTxBytes_Object=MibTableColumn
rcftRemoteEthFeTxBytes=_RcftRemoteEthFeTxBytes_Object((1,3,6,1,4,1,8886,2,1,6,2,1,1,2,1,2),_RcftRemoteEthFeTxBytes_Type())
rcftRemoteEthFeTxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteEthFeTxBytes.setStatus(_A)
_RcftRemoteEthFeRxPackets_Type=Counter32
_RcftRemoteEthFeRxPackets_Object=MibTableColumn
rcftRemoteEthFeRxPackets=_RcftRemoteEthFeRxPackets_Object((1,3,6,1,4,1,8886,2,1,6,2,1,1,2,1,3),_RcftRemoteEthFeRxPackets_Type())
rcftRemoteEthFeRxPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteEthFeRxPackets.setStatus(_A)
_RcftRemoteEthFeRxBytes_Type=Counter32
_RcftRemoteEthFeRxBytes_Object=MibTableColumn
rcftRemoteEthFeRxBytes=_RcftRemoteEthFeRxBytes_Object((1,3,6,1,4,1,8886,2,1,6,2,1,1,2,1,4),_RcftRemoteEthFeRxBytes_Type())
rcftRemoteEthFeRxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteEthFeRxBytes.setStatus(_A)
_RcftRemoteEthFeRxLostPackets_Type=Counter32
_RcftRemoteEthFeRxLostPackets_Object=MibTableColumn
rcftRemoteEthFeRxLostPackets=_RcftRemoteEthFeRxLostPackets_Object((1,3,6,1,4,1,8886,2,1,6,2,1,1,2,1,5),_RcftRemoteEthFeRxLostPackets_Type())
rcftRemoteEthFeRxLostPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteEthFeRxLostPackets.setStatus(_A)
_RcftRemoteEthFeFluxTimer_Type=Counter32
_RcftRemoteEthFeFluxTimer_Object=MibTableColumn
rcftRemoteEthFeFluxTimer=_RcftRemoteEthFeFluxTimer_Object((1,3,6,1,4,1,8886,2,1,6,2,1,1,2,1,6),_RcftRemoteEthFeFluxTimer_Type())
rcftRemoteEthFeFluxTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteEthFeFluxTimer.setStatus(_A)
_RcftRemoteEthFeTxLostPackets_Type=Counter32
_RcftRemoteEthFeTxLostPackets_Object=MibTableColumn
rcftRemoteEthFeTxLostPackets=_RcftRemoteEthFeTxLostPackets_Object((1,3,6,1,4,1,8886,2,1,6,2,1,1,2,1,7),_RcftRemoteEthFeTxLostPackets_Type())
rcftRemoteEthFeTxLostPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteEthFeTxLostPackets.setStatus(_A)
_RcftRemoteEthFePortConfTable_Object=MibTable
rcftRemoteEthFePortConfTable=_RcftRemoteEthFePortConfTable_Object((1,3,6,1,4,1,8886,2,1,6,2,1,1,3))
if mibBuilder.loadTexts:rcftRemoteEthFePortConfTable.setStatus(_A)
_RcftRemoteEthFePortConfEntry_Object=MibTableRow
rcftRemoteEthFePortConfEntry=_RcftRemoteEthFePortConfEntry_Object((1,3,6,1,4,1,8886,2,1,6,2,1,1,3,1))
rcftRemoteEthFePortConfEntry.setIndexNames((0,_F,_H),(0,_F,_I),(0,_C,_J),(0,_C,_h))
if mibBuilder.loadTexts:rcftRemoteEthFePortConfEntry.setStatus(_A)
class _RcftRemoteEthFeConfSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,16)));namedValues=NamedValues(*((_w,1),(_x,2),(_y,3),(_z,4),('other',16)))
_RcftRemoteEthFeConfSpeed_Type.__name__=_E
_RcftRemoteEthFeConfSpeed_Object=MibTableColumn
rcftRemoteEthFeConfSpeed=_RcftRemoteEthFeConfSpeed_Object((1,3,6,1,4,1,8886,2,1,6,2,1,1,3,1,1),_RcftRemoteEthFeConfSpeed_Type())
rcftRemoteEthFeConfSpeed.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteEthFeConfSpeed.setStatus(_A)
class _RcftRemoteEthFeConfDuplex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_A0,1),(_A1,2)))
_RcftRemoteEthFeConfDuplex_Type.__name__=_E
_RcftRemoteEthFeConfDuplex_Object=MibTableColumn
rcftRemoteEthFeConfDuplex=_RcftRemoteEthFeConfDuplex_Object((1,3,6,1,4,1,8886,2,1,6,2,1,1,3,1,2),_RcftRemoteEthFeConfDuplex_Type())
rcftRemoteEthFeConfDuplex.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteEthFeConfDuplex.setStatus(_A)
_RcftRemoteDeviceEthFeTraps_ObjectIdentity=ObjectIdentity
rcftRemoteDeviceEthFeTraps=_RcftRemoteDeviceEthFeTraps_ObjectIdentity((1,3,6,1,4,1,8886,2,1,6,2,1,2))
_RcftRemoteDeviceEthFxMIB_ObjectIdentity=ObjectIdentity
rcftRemoteDeviceEthFxMIB=_RcftRemoteDeviceEthFxMIB_ObjectIdentity((1,3,6,1,4,1,8886,2,1,6,2,2))
_RcftRemoteDeviceEthFxObjects_ObjectIdentity=ObjectIdentity
rcftRemoteDeviceEthFxObjects=_RcftRemoteDeviceEthFxObjects_ObjectIdentity((1,3,6,1,4,1,8886,2,1,6,2,2,1))
_RcftRemoteEthFxPortTable_Object=MibTable
rcftRemoteEthFxPortTable=_RcftRemoteEthFxPortTable_Object((1,3,6,1,4,1,8886,2,1,6,2,2,1,1))
if mibBuilder.loadTexts:rcftRemoteEthFxPortTable.setStatus(_A)
_RcftRemoteEthFxPortEntry_Object=MibTableRow
rcftRemoteEthFxPortEntry=_RcftRemoteEthFxPortEntry_Object((1,3,6,1,4,1,8886,2,1,6,2,2,1,1,1))
rcftRemoteEthFxPortEntry.setIndexNames((0,_F,_H),(0,_F,_I),(0,_C,_J),(0,_C,_b))
if mibBuilder.loadTexts:rcftRemoteEthFxPortEntry.setStatus(_A)
_RcftRemoteEthFxIndex_Type=Integer32
_RcftRemoteEthFxIndex_Object=MibTableColumn
rcftRemoteEthFxIndex=_RcftRemoteEthFxIndex_Object((1,3,6,1,4,1,8886,2,1,6,2,2,1,1,1,1),_RcftRemoteEthFxIndex_Type())
rcftRemoteEthFxIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteEthFxIndex.setStatus(_A)
class _RcftRemoteEthFxFlowControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_O,1),(_P,2)))
_RcftRemoteEthFxFlowControl_Type.__name__=_E
_RcftRemoteEthFxFlowControl_Object=MibTableColumn
rcftRemoteEthFxFlowControl=_RcftRemoteEthFxFlowControl_Object((1,3,6,1,4,1,8886,2,1,6,2,2,1,1,1,2),_RcftRemoteEthFxFlowControl_Type())
rcftRemoteEthFxFlowControl.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteEthFxFlowControl.setStatus(_A)
class _RcftRemoteEthFxPortRLK_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_i,1),(_j,2)))
_RcftRemoteEthFxPortRLK_Type.__name__=_E
_RcftRemoteEthFxPortRLK_Object=MibTableColumn
rcftRemoteEthFxPortRLK=_RcftRemoteEthFxPortRLK_Object((1,3,6,1,4,1,8886,2,1,6,2,2,1,1,1,3),_RcftRemoteEthFxPortRLK_Type())
rcftRemoteEthFxPortRLK.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteEthFxPortRLK.setStatus(_A)
class _RcftRemoteEthFxPortTLK_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_i,1),(_j,2)))
_RcftRemoteEthFxPortTLK_Type.__name__=_E
_RcftRemoteEthFxPortTLK_Object=MibTableColumn
rcftRemoteEthFxPortTLK=_RcftRemoteEthFxPortTLK_Object((1,3,6,1,4,1,8886,2,1,6,2,2,1,1,1,4),_RcftRemoteEthFxPortTLK_Type())
rcftRemoteEthFxPortTLK.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteEthFxPortTLK.setStatus(_A)
class _RcftRemoteEthFxPortSD_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_U,1),('sd',2)))
_RcftRemoteEthFxPortSD_Type.__name__=_E
_RcftRemoteEthFxPortSD_Object=MibTableColumn
rcftRemoteEthFxPortSD=_RcftRemoteEthFxPortSD_Object((1,3,6,1,4,1,8886,2,1,6,2,2,1,1,1,5),_RcftRemoteEthFxPortSD_Type())
rcftRemoteEthFxPortSD.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteEthFxPortSD.setStatus(_A)
class _RcftRemoteEthFxPortTxPowerAbnormal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_U,1),(_k,2)))
_RcftRemoteEthFxPortTxPowerAbnormal_Type.__name__=_E
_RcftRemoteEthFxPortTxPowerAbnormal_Object=MibTableColumn
rcftRemoteEthFxPortTxPowerAbnormal=_RcftRemoteEthFxPortTxPowerAbnormal_Object((1,3,6,1,4,1,8886,2,1,6,2,2,1,1,1,6),_RcftRemoteEthFxPortTxPowerAbnormal_Type())
rcftRemoteEthFxPortTxPowerAbnormal.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteEthFxPortTxPowerAbnormal.setStatus(_A)
class _RcftRemoteEthFxPortRxSensitiveAbnormal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_U,1),(_k,2)))
_RcftRemoteEthFxPortRxSensitiveAbnormal_Type.__name__=_E
_RcftRemoteEthFxPortRxSensitiveAbnormal_Object=MibTableColumn
rcftRemoteEthFxPortRxSensitiveAbnormal=_RcftRemoteEthFxPortRxSensitiveAbnormal_Object((1,3,6,1,4,1,8886,2,1,6,2,2,1,1,1,7),_RcftRemoteEthFxPortRxSensitiveAbnormal_Type())
rcftRemoteEthFxPortRxSensitiveAbnormal.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteEthFxPortRxSensitiveAbnormal.setStatus(_A)
class _RcftRemoteEthFxPortLaserAbnormal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_U,1),(_k,2)))
_RcftRemoteEthFxPortLaserAbnormal_Type.__name__=_E
_RcftRemoteEthFxPortLaserAbnormal_Object=MibTableColumn
rcftRemoteEthFxPortLaserAbnormal=_RcftRemoteEthFxPortLaserAbnormal_Object((1,3,6,1,4,1,8886,2,1,6,2,2,1,1,1,8),_RcftRemoteEthFxPortLaserAbnormal_Type())
rcftRemoteEthFxPortLaserAbnormal.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteEthFxPortLaserAbnormal.setStatus(_A)
class _RcftRemoteEthFxShutDown_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_Z,1),(_a,2),('closeByFP',3),('closeByALS',4),('closeByLP',5)))
_RcftRemoteEthFxShutDown_Type.__name__=_E
_RcftRemoteEthFxShutDown_Object=MibTableColumn
rcftRemoteEthFxShutDown=_RcftRemoteEthFxShutDown_Object((1,3,6,1,4,1,8886,2,1,6,2,2,1,1,1,9),_RcftRemoteEthFxShutDown_Type())
rcftRemoteEthFxShutDown.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteEthFxShutDown.setStatus(_A)
class _RcftRemoteEthFxModuleType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,12,15,100)));namedValues=NamedValues(*((_A2,1),(_A3,2),(_A4,3),(_A5,4),(_A6,5),(_A7,6),(_A8,7),(_A9,8),(_AA,9),(_AB,10),(_AC,12),(_AD,15),(_AE,100)))
_RcftRemoteEthFxModuleType_Type.__name__=_E
_RcftRemoteEthFxModuleType_Object=MibTableColumn
rcftRemoteEthFxModuleType=_RcftRemoteEthFxModuleType_Object((1,3,6,1,4,1,8886,2,1,6,2,2,1,1,1,10),_RcftRemoteEthFxModuleType_Type())
rcftRemoteEthFxModuleType.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteEthFxModuleType.setStatus(_A)
class _RcftRemoteEthFxFaultPass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_O,1),(_P,2)))
_RcftRemoteEthFxFaultPass_Type.__name__=_E
_RcftRemoteEthFxFaultPass_Object=MibTableColumn
rcftRemoteEthFxFaultPass=_RcftRemoteEthFxFaultPass_Object((1,3,6,1,4,1,8886,2,1,6,2,2,1,1,1,11),_RcftRemoteEthFxFaultPass_Type())
rcftRemoteEthFxFaultPass.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteEthFxFaultPass.setStatus(_A)
class _RcftRemoteEthFxPortLink_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_i,1),(_j,2)))
_RcftRemoteEthFxPortLink_Type.__name__=_E
_RcftRemoteEthFxPortLink_Object=MibTableColumn
rcftRemoteEthFxPortLink=_RcftRemoteEthFxPortLink_Object((1,3,6,1,4,1,8886,2,1,6,2,2,1,1,1,12),_RcftRemoteEthFxPortLink_Type())
rcftRemoteEthFxPortLink.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteEthFxPortLink.setStatus(_A)
class _RcftRemoteEthFxRxToTxFaultPass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_O,1),(_P,2)))
_RcftRemoteEthFxRxToTxFaultPass_Type.__name__=_E
_RcftRemoteEthFxRxToTxFaultPass_Object=MibTableColumn
rcftRemoteEthFxRxToTxFaultPass=_RcftRemoteEthFxRxToTxFaultPass_Object((1,3,6,1,4,1,8886,2,1,6,2,2,1,1,1,13),_RcftRemoteEthFxRxToTxFaultPass_Type())
rcftRemoteEthFxRxToTxFaultPass.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteEthFxRxToTxFaultPass.setStatus(_A)
class _RcftRemoteEthFxTxDisabledByFR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Z,1),(_a,2)))
_RcftRemoteEthFxTxDisabledByFR_Type.__name__=_E
_RcftRemoteEthFxTxDisabledByFR_Object=MibTableColumn
rcftRemoteEthFxTxDisabledByFR=_RcftRemoteEthFxTxDisabledByFR_Object((1,3,6,1,4,1,8886,2,1,6,2,2,1,1,1,14),_RcftRemoteEthFxTxDisabledByFR_Type())
rcftRemoteEthFxTxDisabledByFR.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteEthFxTxDisabledByFR.setStatus(_A)
_RcftRemoteEthFxOrderTimeParameter_Type=Integer32
_RcftRemoteEthFxOrderTimeParameter_Object=MibTableColumn
rcftRemoteEthFxOrderTimeParameter=_RcftRemoteEthFxOrderTimeParameter_Object((1,3,6,1,4,1,8886,2,1,6,2,2,1,1,1,15),_RcftRemoteEthFxOrderTimeParameter_Type())
rcftRemoteEthFxOrderTimeParameter.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteEthFxOrderTimeParameter.setStatus(_A)
_RcftRemoteEthFxOrderModeParameter_Type=Integer32
_RcftRemoteEthFxOrderModeParameter_Object=MibTableColumn
rcftRemoteEthFxOrderModeParameter=_RcftRemoteEthFxOrderModeParameter_Object((1,3,6,1,4,1,8886,2,1,6,2,2,1,1,1,16),_RcftRemoteEthFxOrderModeParameter_Type())
rcftRemoteEthFxOrderModeParameter.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteEthFxOrderModeParameter.setStatus(_A)
_RcftRemoteEthFxOrder_Type=Integer32
_RcftRemoteEthFxOrder_Object=MibTableColumn
rcftRemoteEthFxOrder=_RcftRemoteEthFxOrder_Object((1,3,6,1,4,1,8886,2,1,6,2,2,1,1,1,17),_RcftRemoteEthFxOrder_Type())
rcftRemoteEthFxOrder.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteEthFxOrder.setStatus(_A)
class _RcftRemoteEthFxPortExist_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_g,1),('no-exist',2)))
_RcftRemoteEthFxPortExist_Type.__name__=_E
_RcftRemoteEthFxPortExist_Object=MibTableColumn
rcftRemoteEthFxPortExist=_RcftRemoteEthFxPortExist_Object((1,3,6,1,4,1,8886,2,1,6,2,2,1,1,1,18),_RcftRemoteEthFxPortExist_Type())
rcftRemoteEthFxPortExist.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteEthFxPortExist.setStatus(_A)
class _RcftRemoteEthFxPortAuto_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_O,1),(_P,2)))
_RcftRemoteEthFxPortAuto_Type.__name__=_E
_RcftRemoteEthFxPortAuto_Object=MibTableColumn
rcftRemoteEthFxPortAuto=_RcftRemoteEthFxPortAuto_Object((1,3,6,1,4,1,8886,2,1,6,2,2,1,1,1,19),_RcftRemoteEthFxPortAuto_Type())
rcftRemoteEthFxPortAuto.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteEthFxPortAuto.setStatus(_A)
class _RcftRemoteEthFxModuleMaxSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('stm16',1),('stm8',2),('stm4',3),('stm1',4)))
_RcftRemoteEthFxModuleMaxSpeed_Type.__name__=_E
_RcftRemoteEthFxModuleMaxSpeed_Object=MibTableColumn
rcftRemoteEthFxModuleMaxSpeed=_RcftRemoteEthFxModuleMaxSpeed_Object((1,3,6,1,4,1,8886,2,1,6,2,2,1,1,1,20),_RcftRemoteEthFxModuleMaxSpeed_Type())
rcftRemoteEthFxModuleMaxSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteEthFxModuleMaxSpeed.setStatus(_A)
_RcftRemoteEthFxTranDistance_Type=Integer32
_RcftRemoteEthFxTranDistance_Object=MibTableColumn
rcftRemoteEthFxTranDistance=_RcftRemoteEthFxTranDistance_Object((1,3,6,1,4,1,8886,2,1,6,2,2,1,1,1,21),_RcftRemoteEthFxTranDistance_Type())
rcftRemoteEthFxTranDistance.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteEthFxTranDistance.setStatus(_A)
_RcftRemoteEthFxModuleWaveLen_Type=Integer32
_RcftRemoteEthFxModuleWaveLen_Object=MibTableColumn
rcftRemoteEthFxModuleWaveLen=_RcftRemoteEthFxModuleWaveLen_Object((1,3,6,1,4,1,8886,2,1,6,2,2,1,1,1,22),_RcftRemoteEthFxModuleWaveLen_Type())
rcftRemoteEthFxModuleWaveLen.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteEthFxModuleWaveLen.setStatus(_A)
class _RcftRemoteEthFxPortConnectorType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)));namedValues=NamedValues(*(('unkkown',1),('rj45',2),('sc',3),('style1',4),('style2',5),('bnctnc',6),('coaheader',7),('jack',8),('lc',9),('mtrj',10),('mu',11),('sg',12),('opticalpigtail',13),('hssdc2',14),('copperpigtail',15)))
_RcftRemoteEthFxPortConnectorType_Type.__name__=_E
_RcftRemoteEthFxPortConnectorType_Object=MibTableColumn
rcftRemoteEthFxPortConnectorType=_RcftRemoteEthFxPortConnectorType_Object((1,3,6,1,4,1,8886,2,1,6,2,2,1,1,1,23),_RcftRemoteEthFxPortConnectorType_Type())
rcftRemoteEthFxPortConnectorType.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteEthFxPortConnectorType.setStatus(_A)
class _RcftRemoteEthFxPortTransmitMedia_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,15)));namedValues=NamedValues(*(('unkkown',1),('singleMode9um',2),('multiMode50um',3),('multiMode62point5um',4),('copperline',15)))
_RcftRemoteEthFxPortTransmitMedia_Type.__name__=_E
_RcftRemoteEthFxPortTransmitMedia_Object=MibTableColumn
rcftRemoteEthFxPortTransmitMedia=_RcftRemoteEthFxPortTransmitMedia_Object((1,3,6,1,4,1,8886,2,1,6,2,2,1,1,1,24),_RcftRemoteEthFxPortTransmitMedia_Type())
rcftRemoteEthFxPortTransmitMedia.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteEthFxPortTransmitMedia.setStatus(_A)
class _RcftRemoteEthFxModuleManufacturer_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_RcftRemoteEthFxModuleManufacturer_Type.__name__=_G
_RcftRemoteEthFxModuleManufacturer_Object=MibTableColumn
rcftRemoteEthFxModuleManufacturer=_RcftRemoteEthFxModuleManufacturer_Object((1,3,6,1,4,1,8886,2,1,6,2,2,1,1,1,25),_RcftRemoteEthFxModuleManufacturer_Type())
rcftRemoteEthFxModuleManufacturer.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteEthFxModuleManufacturer.setStatus(_A)
class _RcftRemoteEthFxModuleDescr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_RcftRemoteEthFxModuleDescr_Type.__name__=_G
_RcftRemoteEthFxModuleDescr_Object=MibTableColumn
rcftRemoteEthFxModuleDescr=_RcftRemoteEthFxModuleDescr_Object((1,3,6,1,4,1,8886,2,1,6,2,2,1,1,1,26),_RcftRemoteEthFxModuleDescr_Type())
rcftRemoteEthFxModuleDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteEthFxModuleDescr.setStatus(_A)
class _RcftRemoteEthFxPortModuleVersion_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_RcftRemoteEthFxPortModuleVersion_Type.__name__=_G
_RcftRemoteEthFxPortModuleVersion_Object=MibTableColumn
rcftRemoteEthFxPortModuleVersion=_RcftRemoteEthFxPortModuleVersion_Object((1,3,6,1,4,1,8886,2,1,6,2,2,1,1,1,27),_RcftRemoteEthFxPortModuleVersion_Type())
rcftRemoteEthFxPortModuleVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteEthFxPortModuleVersion.setStatus(_A)
class _RcftRemoteEthFxModuleSerialNumber_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_RcftRemoteEthFxModuleSerialNumber_Type.__name__=_G
_RcftRemoteEthFxModuleSerialNumber_Object=MibTableColumn
rcftRemoteEthFxModuleSerialNumber=_RcftRemoteEthFxModuleSerialNumber_Object((1,3,6,1,4,1,8886,2,1,6,2,2,1,1,1,28),_RcftRemoteEthFxModuleSerialNumber_Type())
rcftRemoteEthFxModuleSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteEthFxModuleSerialNumber.setStatus(_A)
_RcftRemoteEthFxPortSFPDiagnoInfo_Type=Integer32
_RcftRemoteEthFxPortSFPDiagnoInfo_Object=MibTableColumn
rcftRemoteEthFxPortSFPDiagnoInfo=_RcftRemoteEthFxPortSFPDiagnoInfo_Object((1,3,6,1,4,1,8886,2,1,6,2,2,1,1,1,29),_RcftRemoteEthFxPortSFPDiagnoInfo_Type())
rcftRemoteEthFxPortSFPDiagnoInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteEthFxPortSFPDiagnoInfo.setStatus(_A)
_RcftRemoteEthFxSFPDiagnoAlarmStatus_Type=Integer32
_RcftRemoteEthFxSFPDiagnoAlarmStatus_Object=MibTableColumn
rcftRemoteEthFxSFPDiagnoAlarmStatus=_RcftRemoteEthFxSFPDiagnoAlarmStatus_Object((1,3,6,1,4,1,8886,2,1,6,2,2,1,1,1,30),_RcftRemoteEthFxSFPDiagnoAlarmStatus_Type())
rcftRemoteEthFxSFPDiagnoAlarmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteEthFxSFPDiagnoAlarmStatus.setStatus(_A)
_RcftRemoteEthFxPortStatus_Type=Integer32
_RcftRemoteEthFxPortStatus_Object=MibTableColumn
rcftRemoteEthFxPortStatus=_RcftRemoteEthFxPortStatus_Object((1,3,6,1,4,1,8886,2,1,6,2,2,1,1,1,31),_RcftRemoteEthFxPortStatus_Type())
rcftRemoteEthFxPortStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteEthFxPortStatus.setStatus(_A)
_RcftRemoteEthFxUntag_Type=Integer32
_RcftRemoteEthFxUntag_Object=MibTableColumn
rcftRemoteEthFxUntag=_RcftRemoteEthFxUntag_Object((1,3,6,1,4,1,8886,2,1,6,2,2,1,1,1,32),_RcftRemoteEthFxUntag_Type())
rcftRemoteEthFxUntag.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteEthFxUntag.setStatus(_A)
_RcftRemoteEthFxPVID_Type=Integer32
_RcftRemoteEthFxPVID_Object=MibTableColumn
rcftRemoteEthFxPVID=_RcftRemoteEthFxPVID_Object((1,3,6,1,4,1,8886,2,1,6,2,2,1,1,1,33),_RcftRemoteEthFxPVID_Type())
rcftRemoteEthFxPVID.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteEthFxPVID.setStatus(_A)
class _RcftRemoteEthFxPortSFPType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('utp',1),('fiber',2)))
_RcftRemoteEthFxPortSFPType_Type.__name__=_E
_RcftRemoteEthFxPortSFPType_Object=MibTableColumn
rcftRemoteEthFxPortSFPType=_RcftRemoteEthFxPortSFPType_Object((1,3,6,1,4,1,8886,2,1,6,2,2,1,1,1,34),_RcftRemoteEthFxPortSFPType_Type())
rcftRemoteEthFxPortSFPType.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteEthFxPortSFPType.setStatus(_A)
_RcftRemoteEthFxPortSFPInfo_Type=Integer32
_RcftRemoteEthFxPortSFPInfo_Object=MibTableColumn
rcftRemoteEthFxPortSFPInfo=_RcftRemoteEthFxPortSFPInfo_Object((1,3,6,1,4,1,8886,2,1,6,2,2,1,1,1,35),_RcftRemoteEthFxPortSFPInfo_Type())
rcftRemoteEthFxPortSFPInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteEthFxPortSFPInfo.setStatus(_A)
_RcftRemoteEthFxPortLoopStatus_Type=Integer32
_RcftRemoteEthFxPortLoopStatus_Object=MibTableColumn
rcftRemoteEthFxPortLoopStatus=_RcftRemoteEthFxPortLoopStatus_Object((1,3,6,1,4,1,8886,2,1,6,2,2,1,1,1,36),_RcftRemoteEthFxPortLoopStatus_Type())
rcftRemoteEthFxPortLoopStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteEthFxPortLoopStatus.setStatus(_A)
_RcftRemoteEthFxPortRxRestrictSpeed_Type=Integer32
_RcftRemoteEthFxPortRxRestrictSpeed_Object=MibTableColumn
rcftRemoteEthFxPortRxRestrictSpeed=_RcftRemoteEthFxPortRxRestrictSpeed_Object((1,3,6,1,4,1,8886,2,1,6,2,2,1,1,1,37),_RcftRemoteEthFxPortRxRestrictSpeed_Type())
rcftRemoteEthFxPortRxRestrictSpeed.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteEthFxPortRxRestrictSpeed.setStatus(_A)
_RcftRemoteEthFxPortTxRestrictSpeed_Type=Integer32
_RcftRemoteEthFxPortTxRestrictSpeed_Object=MibTableColumn
rcftRemoteEthFxPortTxRestrictSpeed=_RcftRemoteEthFxPortTxRestrictSpeed_Object((1,3,6,1,4,1,8886,2,1,6,2,2,1,1,1,38),_RcftRemoteEthFxPortTxRestrictSpeed_Type())
rcftRemoteEthFxPortTxRestrictSpeed.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteEthFxPortTxRestrictSpeed.setStatus(_A)
_RcftRemoteEthFxSFPDiagnoWarningStatus_Type=Integer32
_RcftRemoteEthFxSFPDiagnoWarningStatus_Object=MibTableColumn
rcftRemoteEthFxSFPDiagnoWarningStatus=_RcftRemoteEthFxSFPDiagnoWarningStatus_Object((1,3,6,1,4,1,8886,2,1,6,2,2,1,1,1,39),_RcftRemoteEthFxSFPDiagnoWarningStatus_Type())
rcftRemoteEthFxSFPDiagnoWarningStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteEthFxSFPDiagnoWarningStatus.setStatus(_A)
_RcftRemoteEthFxPortLineOrClient_Type=Integer32
_RcftRemoteEthFxPortLineOrClient_Object=MibTableColumn
rcftRemoteEthFxPortLineOrClient=_RcftRemoteEthFxPortLineOrClient_Object((1,3,6,1,4,1,8886,2,1,6,2,2,1,1,1,40),_RcftRemoteEthFxPortLineOrClient_Type())
rcftRemoteEthFxPortLineOrClient.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteEthFxPortLineOrClient.setStatus(_A)
_RcftRemoteEthFxCOS_Type=Integer32
_RcftRemoteEthFxCOS_Object=MibTableColumn
rcftRemoteEthFxCOS=_RcftRemoteEthFxCOS_Object((1,3,6,1,4,1,8886,2,1,6,2,2,1,1,1,41),_RcftRemoteEthFxCOS_Type())
rcftRemoteEthFxCOS.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteEthFxCOS.setStatus(_A)
_RcftRemoteEthFxStatisticTable_Object=MibTable
rcftRemoteEthFxStatisticTable=_RcftRemoteEthFxStatisticTable_Object((1,3,6,1,4,1,8886,2,1,6,2,2,1,2))
if mibBuilder.loadTexts:rcftRemoteEthFxStatisticTable.setStatus(_A)
_RcftRemoteEthFxStatisticEntry_Object=MibTableRow
rcftRemoteEthFxStatisticEntry=_RcftRemoteEthFxStatisticEntry_Object((1,3,6,1,4,1,8886,2,1,6,2,2,1,2,1))
if mibBuilder.loadTexts:rcftRemoteEthFxStatisticEntry.setStatus(_A)
_RcftRemoteEthFxTxPackets_Type=Counter32
_RcftRemoteEthFxTxPackets_Object=MibTableColumn
rcftRemoteEthFxTxPackets=_RcftRemoteEthFxTxPackets_Object((1,3,6,1,4,1,8886,2,1,6,2,2,1,2,1,1),_RcftRemoteEthFxTxPackets_Type())
rcftRemoteEthFxTxPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteEthFxTxPackets.setStatus(_A)
_RcftRemoteEthFxTxBytes_Type=Counter32
_RcftRemoteEthFxTxBytes_Object=MibTableColumn
rcftRemoteEthFxTxBytes=_RcftRemoteEthFxTxBytes_Object((1,3,6,1,4,1,8886,2,1,6,2,2,1,2,1,2),_RcftRemoteEthFxTxBytes_Type())
rcftRemoteEthFxTxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteEthFxTxBytes.setStatus(_A)
_RcftRemoteEthFxRxPackets_Type=Counter32
_RcftRemoteEthFxRxPackets_Object=MibTableColumn
rcftRemoteEthFxRxPackets=_RcftRemoteEthFxRxPackets_Object((1,3,6,1,4,1,8886,2,1,6,2,2,1,2,1,3),_RcftRemoteEthFxRxPackets_Type())
rcftRemoteEthFxRxPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteEthFxRxPackets.setStatus(_A)
_RcftRemoteEthFxRxBytes_Type=Counter32
_RcftRemoteEthFxRxBytes_Object=MibTableColumn
rcftRemoteEthFxRxBytes=_RcftRemoteEthFxRxBytes_Object((1,3,6,1,4,1,8886,2,1,6,2,2,1,2,1,4),_RcftRemoteEthFxRxBytes_Type())
rcftRemoteEthFxRxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteEthFxRxBytes.setStatus(_A)
_RcftRemoteEthFxRxLostPackets_Type=Counter32
_RcftRemoteEthFxRxLostPackets_Object=MibTableColumn
rcftRemoteEthFxRxLostPackets=_RcftRemoteEthFxRxLostPackets_Object((1,3,6,1,4,1,8886,2,1,6,2,2,1,2,1,5),_RcftRemoteEthFxRxLostPackets_Type())
rcftRemoteEthFxRxLostPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteEthFxRxLostPackets.setStatus(_A)
_RcftRemoteEthFxFluxTimer_Type=Counter32
_RcftRemoteEthFxFluxTimer_Object=MibTableColumn
rcftRemoteEthFxFluxTimer=_RcftRemoteEthFxFluxTimer_Object((1,3,6,1,4,1,8886,2,1,6,2,2,1,2,1,6),_RcftRemoteEthFxFluxTimer_Type())
rcftRemoteEthFxFluxTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteEthFxFluxTimer.setStatus(_A)
_RcftRemoteEthFxTxLostPackets_Type=Counter32
_RcftRemoteEthFxTxLostPackets_Object=MibTableColumn
rcftRemoteEthFxTxLostPackets=_RcftRemoteEthFxTxLostPackets_Object((1,3,6,1,4,1,8886,2,1,6,2,2,1,2,1,7),_RcftRemoteEthFxTxLostPackets_Type())
rcftRemoteEthFxTxLostPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteEthFxTxLostPackets.setStatus(_A)
_RcftRemoteEthFx64TxBytes_Type=Counter64
_RcftRemoteEthFx64TxBytes_Object=MibTableColumn
rcftRemoteEthFx64TxBytes=_RcftRemoteEthFx64TxBytes_Object((1,3,6,1,4,1,8886,2,1,6,2,2,1,2,1,8),_RcftRemoteEthFx64TxBytes_Type())
rcftRemoteEthFx64TxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteEthFx64TxBytes.setStatus(_A)
_RcftRemoteEthFx64RxBytes_Type=Counter64
_RcftRemoteEthFx64RxBytes_Object=MibTableColumn
rcftRemoteEthFx64RxBytes=_RcftRemoteEthFx64RxBytes_Object((1,3,6,1,4,1,8886,2,1,6,2,2,1,2,1,9),_RcftRemoteEthFx64RxBytes_Type())
rcftRemoteEthFx64RxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteEthFx64RxBytes.setStatus(_A)
_RcftRemoteDeviceEthFxTraps_ObjectIdentity=ObjectIdentity
rcftRemoteDeviceEthFxTraps=_RcftRemoteDeviceEthFxTraps_ObjectIdentity((1,3,6,1,4,1,8886,2,1,6,2,2,2))
_RcftRemoteDeviceEthFxPerformance_ObjectIdentity=ObjectIdentity
rcftRemoteDeviceEthFxPerformance=_RcftRemoteDeviceEthFxPerformance_ObjectIdentity((1,3,6,1,4,1,8886,2,1,6,2,2,3))
_RcftRemoteEthFxPortCurrentTable_Object=MibTable
rcftRemoteEthFxPortCurrentTable=_RcftRemoteEthFxPortCurrentTable_Object((1,3,6,1,4,1,8886,2,1,6,2,2,3,1))
if mibBuilder.loadTexts:rcftRemoteEthFxPortCurrentTable.setStatus(_A)
_RcftRemoteEthFxPortCurrentEntry_Object=MibTableRow
rcftRemoteEthFxPortCurrentEntry=_RcftRemoteEthFxPortCurrentEntry_Object((1,3,6,1,4,1,8886,2,1,6,2,2,3,1,1))
rcftRemoteEthFxPortCurrentEntry.setIndexNames((0,_F,_H),(0,_F,_I),(0,_C,_J),(0,_C,_b))
if mibBuilder.loadTexts:rcftRemoteEthFxPortCurrentEntry.setStatus(_A)
class _RcftRemoteEthFxCurrentTemperature_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_RcftRemoteEthFxCurrentTemperature_Type.__name__=_G
_RcftRemoteEthFxCurrentTemperature_Object=MibTableColumn
rcftRemoteEthFxCurrentTemperature=_RcftRemoteEthFxCurrentTemperature_Object((1,3,6,1,4,1,8886,2,1,6,2,2,3,1,1,1),_RcftRemoteEthFxCurrentTemperature_Type())
rcftRemoteEthFxCurrentTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteEthFxCurrentTemperature.setStatus(_A)
class _RcftRemoteEthFxCurrentVoltage_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_RcftRemoteEthFxCurrentVoltage_Type.__name__=_G
_RcftRemoteEthFxCurrentVoltage_Object=MibTableColumn
rcftRemoteEthFxCurrentVoltage=_RcftRemoteEthFxCurrentVoltage_Object((1,3,6,1,4,1,8886,2,1,6,2,2,3,1,1,2),_RcftRemoteEthFxCurrentVoltage_Type())
rcftRemoteEthFxCurrentVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteEthFxCurrentVoltage.setStatus(_A)
class _RcftRemoteEthFxCurrentOffsetCurr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_RcftRemoteEthFxCurrentOffsetCurr_Type.__name__=_G
_RcftRemoteEthFxCurrentOffsetCurr_Object=MibTableColumn
rcftRemoteEthFxCurrentOffsetCurr=_RcftRemoteEthFxCurrentOffsetCurr_Object((1,3,6,1,4,1,8886,2,1,6,2,2,3,1,1,3),_RcftRemoteEthFxCurrentOffsetCurr_Type())
rcftRemoteEthFxCurrentOffsetCurr.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteEthFxCurrentOffsetCurr.setStatus(_A)
class _RcftRemoteEthFxCurrentRecvPower_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_RcftRemoteEthFxCurrentRecvPower_Type.__name__=_G
_RcftRemoteEthFxCurrentRecvPower_Object=MibTableColumn
rcftRemoteEthFxCurrentRecvPower=_RcftRemoteEthFxCurrentRecvPower_Object((1,3,6,1,4,1,8886,2,1,6,2,2,3,1,1,4),_RcftRemoteEthFxCurrentRecvPower_Type())
rcftRemoteEthFxCurrentRecvPower.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteEthFxCurrentRecvPower.setStatus(_A)
class _RcftRemoteEthFxCurrentSendPower_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_RcftRemoteEthFxCurrentSendPower_Type.__name__=_G
_RcftRemoteEthFxCurrentSendPower_Object=MibTableColumn
rcftRemoteEthFxCurrentSendPower=_RcftRemoteEthFxCurrentSendPower_Object((1,3,6,1,4,1,8886,2,1,6,2,2,3,1,1,5),_RcftRemoteEthFxCurrentSendPower_Type())
rcftRemoteEthFxCurrentSendPower.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteEthFxCurrentSendPower.setStatus(_A)
_RcftRemoteEthFxPortIntervalTable_Object=MibTable
rcftRemoteEthFxPortIntervalTable=_RcftRemoteEthFxPortIntervalTable_Object((1,3,6,1,4,1,8886,2,1,6,2,2,3,2))
if mibBuilder.loadTexts:rcftRemoteEthFxPortIntervalTable.setStatus(_A)
_RcftRemoteEthFxPortIntervalEntry_Object=MibTableRow
rcftRemoteEthFxPortIntervalEntry=_RcftRemoteEthFxPortIntervalEntry_Object((1,3,6,1,4,1,8886,2,1,6,2,2,3,2,1))
rcftRemoteEthFxPortIntervalEntry.setIndexNames((0,_F,_H),(0,_F,_I),(0,_C,_J),(0,_C,_b),(0,_C,_AF))
if mibBuilder.loadTexts:rcftRemoteEthFxPortIntervalEntry.setStatus(_A)
_RcftRemoteEthFxIntervalNumber_Type=Integer32
_RcftRemoteEthFxIntervalNumber_Object=MibTableColumn
rcftRemoteEthFxIntervalNumber=_RcftRemoteEthFxIntervalNumber_Object((1,3,6,1,4,1,8886,2,1,6,2,2,3,2,1,1),_RcftRemoteEthFxIntervalNumber_Type())
rcftRemoteEthFxIntervalNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteEthFxIntervalNumber.setStatus(_A)
class _RcftRemoteEthFxIntervalTemperature_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_RcftRemoteEthFxIntervalTemperature_Type.__name__=_G
_RcftRemoteEthFxIntervalTemperature_Object=MibTableColumn
rcftRemoteEthFxIntervalTemperature=_RcftRemoteEthFxIntervalTemperature_Object((1,3,6,1,4,1,8886,2,1,6,2,2,3,2,1,2),_RcftRemoteEthFxIntervalTemperature_Type())
rcftRemoteEthFxIntervalTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteEthFxIntervalTemperature.setStatus(_A)
class _RcftRemoteEthFxIntervalVoltage_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_RcftRemoteEthFxIntervalVoltage_Type.__name__=_G
_RcftRemoteEthFxIntervalVoltage_Object=MibTableColumn
rcftRemoteEthFxIntervalVoltage=_RcftRemoteEthFxIntervalVoltage_Object((1,3,6,1,4,1,8886,2,1,6,2,2,3,2,1,3),_RcftRemoteEthFxIntervalVoltage_Type())
rcftRemoteEthFxIntervalVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteEthFxIntervalVoltage.setStatus(_A)
class _RcftRemoteEthFxIntervalOffsetCurr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_RcftRemoteEthFxIntervalOffsetCurr_Type.__name__=_G
_RcftRemoteEthFxIntervalOffsetCurr_Object=MibTableColumn
rcftRemoteEthFxIntervalOffsetCurr=_RcftRemoteEthFxIntervalOffsetCurr_Object((1,3,6,1,4,1,8886,2,1,6,2,2,3,2,1,4),_RcftRemoteEthFxIntervalOffsetCurr_Type())
rcftRemoteEthFxIntervalOffsetCurr.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteEthFxIntervalOffsetCurr.setStatus(_A)
class _RcftRemoteEthFxIntervalRecvPower_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_RcftRemoteEthFxIntervalRecvPower_Type.__name__=_G
_RcftRemoteEthFxIntervalRecvPower_Object=MibTableColumn
rcftRemoteEthFxIntervalRecvPower=_RcftRemoteEthFxIntervalRecvPower_Object((1,3,6,1,4,1,8886,2,1,6,2,2,3,2,1,5),_RcftRemoteEthFxIntervalRecvPower_Type())
rcftRemoteEthFxIntervalRecvPower.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteEthFxIntervalRecvPower.setStatus(_A)
class _RcftRemoteEthFxIntervalSendPower_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_RcftRemoteEthFxIntervalSendPower_Type.__name__=_G
_RcftRemoteEthFxIntervalSendPower_Object=MibTableColumn
rcftRemoteEthFxIntervalSendPower=_RcftRemoteEthFxIntervalSendPower_Object((1,3,6,1,4,1,8886,2,1,6,2,2,3,2,1,6),_RcftRemoteEthFxIntervalSendPower_Type())
rcftRemoteEthFxIntervalSendPower.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteEthFxIntervalSendPower.setStatus(_A)
_RcftRemoteEthFxPortPerTable_Object=MibTable
rcftRemoteEthFxPortPerTable=_RcftRemoteEthFxPortPerTable_Object((1,3,6,1,4,1,8886,2,1,6,2,2,3,3))
if mibBuilder.loadTexts:rcftRemoteEthFxPortPerTable.setStatus(_A)
_RcftRemoteEthFxPortPerEntry_Object=MibTableRow
rcftRemoteEthFxPortPerEntry=_RcftRemoteEthFxPortPerEntry_Object((1,3,6,1,4,1,8886,2,1,6,2,2,3,3,1))
rcftRemoteEthFxPortPerEntry.setIndexNames((0,_F,_H),(0,_F,_I),(0,_C,_J),(0,_C,_b))
if mibBuilder.loadTexts:rcftRemoteEthFxPortPerEntry.setStatus(_A)
class _RcftRemoteEthFxPortPerTemperature_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_RcftRemoteEthFxPortPerTemperature_Type.__name__=_G
_RcftRemoteEthFxPortPerTemperature_Object=MibTableColumn
rcftRemoteEthFxPortPerTemperature=_RcftRemoteEthFxPortPerTemperature_Object((1,3,6,1,4,1,8886,2,1,6,2,2,3,3,1,1),_RcftRemoteEthFxPortPerTemperature_Type())
rcftRemoteEthFxPortPerTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteEthFxPortPerTemperature.setStatus(_A)
class _RcftRemoteEthFxPortPerVoltage_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_RcftRemoteEthFxPortPerVoltage_Type.__name__=_G
_RcftRemoteEthFxPortPerVoltage_Object=MibTableColumn
rcftRemoteEthFxPortPerVoltage=_RcftRemoteEthFxPortPerVoltage_Object((1,3,6,1,4,1,8886,2,1,6,2,2,3,3,1,2),_RcftRemoteEthFxPortPerVoltage_Type())
rcftRemoteEthFxPortPerVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteEthFxPortPerVoltage.setStatus(_A)
class _RcftRemoteEthFxPortPerOffsetCurr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_RcftRemoteEthFxPortPerOffsetCurr_Type.__name__=_G
_RcftRemoteEthFxPortPerOffsetCurr_Object=MibTableColumn
rcftRemoteEthFxPortPerOffsetCurr=_RcftRemoteEthFxPortPerOffsetCurr_Object((1,3,6,1,4,1,8886,2,1,6,2,2,3,3,1,3),_RcftRemoteEthFxPortPerOffsetCurr_Type())
rcftRemoteEthFxPortPerOffsetCurr.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteEthFxPortPerOffsetCurr.setStatus(_A)
class _RcftRemoteEthFxPortPerRecvPower_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_RcftRemoteEthFxPortPerRecvPower_Type.__name__=_G
_RcftRemoteEthFxPortPerRecvPower_Object=MibTableColumn
rcftRemoteEthFxPortPerRecvPower=_RcftRemoteEthFxPortPerRecvPower_Object((1,3,6,1,4,1,8886,2,1,6,2,2,3,3,1,4),_RcftRemoteEthFxPortPerRecvPower_Type())
rcftRemoteEthFxPortPerRecvPower.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteEthFxPortPerRecvPower.setStatus(_A)
class _RcftRemoteEthFxPortPerSendPower_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_RcftRemoteEthFxPortPerSendPower_Type.__name__=_G
_RcftRemoteEthFxPortPerSendPower_Object=MibTableColumn
rcftRemoteEthFxPortPerSendPower=_RcftRemoteEthFxPortPerSendPower_Object((1,3,6,1,4,1,8886,2,1,6,2,2,3,3,1,5),_RcftRemoteEthFxPortPerSendPower_Type())
rcftRemoteEthFxPortPerSendPower.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteEthFxPortPerSendPower.setStatus(_A)
_RcftRemoteDeviceE1MIB_ObjectIdentity=ObjectIdentity
rcftRemoteDeviceE1MIB=_RcftRemoteDeviceE1MIB_ObjectIdentity((1,3,6,1,4,1,8886,2,1,6,3))
_RcftRemoteDeviceE1Objects_ObjectIdentity=ObjectIdentity
rcftRemoteDeviceE1Objects=_RcftRemoteDeviceE1Objects_ObjectIdentity((1,3,6,1,4,1,8886,2,1,6,3,1))
_RcftRemoteDeviceE1Table_Object=MibTable
rcftRemoteDeviceE1Table=_RcftRemoteDeviceE1Table_Object((1,3,6,1,4,1,8886,2,1,6,3,1,1))
if mibBuilder.loadTexts:rcftRemoteDeviceE1Table.setStatus(_A)
_RcftRemoteDeviceE1Entry_Object=MibTableRow
rcftRemoteDeviceE1Entry=_RcftRemoteDeviceE1Entry_Object((1,3,6,1,4,1,8886,2,1,6,3,1,1,1))
rcftRemoteDeviceE1Entry.setIndexNames((0,_F,_H),(0,_F,_I),(0,_C,_J),(0,_C,_AG))
if mibBuilder.loadTexts:rcftRemoteDeviceE1Entry.setStatus(_A)
_RcftRemoteE1Index_Type=Integer32
_RcftRemoteE1Index_Object=MibTableColumn
rcftRemoteE1Index=_RcftRemoteE1Index_Object((1,3,6,1,4,1,8886,2,1,6,3,1,1,1,1),_RcftRemoteE1Index_Type())
rcftRemoteE1Index.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteE1Index.setStatus(_A)
class _RcftRemoteE1BertEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_O,1),(_P,2)))
_RcftRemoteE1BertEnable_Type.__name__=_E
_RcftRemoteE1BertEnable_Object=MibTableColumn
rcftRemoteE1BertEnable=_RcftRemoteE1BertEnable_Object((1,3,6,1,4,1,8886,2,1,6,3,1,1,1,2),_RcftRemoteE1BertEnable_Type())
rcftRemoteE1BertEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteE1BertEnable.setStatus(_A)
class _RcftRemoteE1ClockMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('master',1),(_v,2),(_AH,3),('e1received',4)))
_RcftRemoteE1ClockMode_Type.__name__=_E
_RcftRemoteE1ClockMode_Object=MibTableColumn
rcftRemoteE1ClockMode=_RcftRemoteE1ClockMode_Object((1,3,6,1,4,1,8886,2,1,6,3,1,1,1,3),_RcftRemoteE1ClockMode_Type())
rcftRemoteE1ClockMode.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteE1ClockMode.setStatus(_A)
class _RcftRemoteE1FrameEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_AH,1),('pcm',2)))
_RcftRemoteE1FrameEnable_Type.__name__=_E
_RcftRemoteE1FrameEnable_Object=MibTableColumn
rcftRemoteE1FrameEnable=_RcftRemoteE1FrameEnable_Object((1,3,6,1,4,1,8886,2,1,6,3,1,1,1,4),_RcftRemoteE1FrameEnable_Type())
rcftRemoteE1FrameEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteE1FrameEnable.setStatus(_A)
_RcftRemoteE1AlarmStatus_Type=Integer32
_RcftRemoteE1AlarmStatus_Object=MibTableColumn
rcftRemoteE1AlarmStatus=_RcftRemoteE1AlarmStatus_Object((1,3,6,1,4,1,8886,2,1,6,3,1,1,1,5),_RcftRemoteE1AlarmStatus_Type())
rcftRemoteE1AlarmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteE1AlarmStatus.setStatus(_A)
_RcftRemoteE1SubSpeed_Type=Unsigned32
_RcftRemoteE1SubSpeed_Object=MibTableColumn
rcftRemoteE1SubSpeed=_RcftRemoteE1SubSpeed_Object((1,3,6,1,4,1,8886,2,1,6,3,1,1,1,6),_RcftRemoteE1SubSpeed_Type())
rcftRemoteE1SubSpeed.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteE1SubSpeed.setStatus(_A)
class _RcftRemoteE1CRCDetectEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_O,1),(_P,2)))
_RcftRemoteE1CRCDetectEnable_Type.__name__=_E
_RcftRemoteE1CRCDetectEnable_Object=MibTableColumn
rcftRemoteE1CRCDetectEnable=_RcftRemoteE1CRCDetectEnable_Object((1,3,6,1,4,1,8886,2,1,6,3,1,1,1,7),_RcftRemoteE1CRCDetectEnable_Type())
rcftRemoteE1CRCDetectEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteE1CRCDetectEnable.setStatus(_A)
_RcftRemoteE1ErrCodeSecCnt_Type=Counter32
_RcftRemoteE1ErrCodeSecCnt_Object=MibTableColumn
rcftRemoteE1ErrCodeSecCnt=_RcftRemoteE1ErrCodeSecCnt_Object((1,3,6,1,4,1,8886,2,1,6,3,1,1,1,8),_RcftRemoteE1ErrCodeSecCnt_Type())
rcftRemoteE1ErrCodeSecCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteE1ErrCodeSecCnt.setStatus(_A)
_RcftRemoteE1SErrCodeSecCnt_Type=Counter32
_RcftRemoteE1SErrCodeSecCnt_Object=MibTableColumn
rcftRemoteE1SErrCodeSecCnt=_RcftRemoteE1SErrCodeSecCnt_Object((1,3,6,1,4,1,8886,2,1,6,3,1,1,1,9),_RcftRemoteE1SErrCodeSecCnt_Type())
rcftRemoteE1SErrCodeSecCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteE1SErrCodeSecCnt.setStatus(_A)
class _RcftRemoteE1TransErrorCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('less10E-6',1),('more10E-6',2),('more10E-3',3)))
_RcftRemoteE1TransErrorCode_Type.__name__=_E
_RcftRemoteE1TransErrorCode_Object=MibTableColumn
rcftRemoteE1TransErrorCode=_RcftRemoteE1TransErrorCode_Object((1,3,6,1,4,1,8886,2,1,6,3,1,1,1,10),_RcftRemoteE1TransErrorCode_Type())
rcftRemoteE1TransErrorCode.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteE1TransErrorCode.setStatus(_A)
class _RcftRemoteE1CRCStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_O,1),(_P,2)))
_RcftRemoteE1CRCStatus_Type.__name__=_E
_RcftRemoteE1CRCStatus_Object=MibTableColumn
rcftRemoteE1CRCStatus=_RcftRemoteE1CRCStatus_Object((1,3,6,1,4,1,8886,2,1,6,3,1,1,1,11),_RcftRemoteE1CRCStatus_Type())
rcftRemoteE1CRCStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteE1CRCStatus.setStatus(_A)
class _RcftRemoteE1FaultPass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_O,1),(_P,2)))
_RcftRemoteE1FaultPass_Type.__name__=_E
_RcftRemoteE1FaultPass_Object=MibTableColumn
rcftRemoteE1FaultPass=_RcftRemoteE1FaultPass_Object((1,3,6,1,4,1,8886,2,1,6,3,1,1,1,12),_RcftRemoteE1FaultPass_Type())
rcftRemoteE1FaultPass.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteE1FaultPass.setStatus(_A)
class _RcftRemoteE1LocalLoopEn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_O,1),(_P,2)))
_RcftRemoteE1LocalLoopEn_Type.__name__=_E
_RcftRemoteE1LocalLoopEn_Object=MibTableColumn
rcftRemoteE1LocalLoopEn=_RcftRemoteE1LocalLoopEn_Object((1,3,6,1,4,1,8886,2,1,6,3,1,1,1,13),_RcftRemoteE1LocalLoopEn_Type())
rcftRemoteE1LocalLoopEn.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteE1LocalLoopEn.setStatus(_A)
class _RcftRemoteE1Location_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,100)));namedValues=NamedValues(*(('e1-1',1),('e1-2',2),('e1-3',3),('e1-4',4),('e1-5',5),('e1-6',6),('e1-7',7),('e1-8',8),('unknown',100)))
_RcftRemoteE1Location_Type.__name__=_E
_RcftRemoteE1Location_Object=MibTableColumn
rcftRemoteE1Location=_RcftRemoteE1Location_Object((1,3,6,1,4,1,8886,2,1,6,3,1,1,1,14),_RcftRemoteE1Location_Type())
rcftRemoteE1Location.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteE1Location.setStatus(_A)
class _RcftRemoteE1FoundLink_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,100)));namedValues=NamedValues(*(('success',1),('failForDelay',2),('failForOtherReason',100)))
_RcftRemoteE1FoundLink_Type.__name__=_E
_RcftRemoteE1FoundLink_Object=MibTableColumn
rcftRemoteE1FoundLink=_RcftRemoteE1FoundLink_Object((1,3,6,1,4,1,8886,2,1,6,3,1,1,1,15),_RcftRemoteE1FoundLink_Type())
rcftRemoteE1FoundLink.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteE1FoundLink.setStatus(_A)
class _RcftRemoteE1UnUsed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('unused',1),('used',2)))
_RcftRemoteE1UnUsed_Type.__name__=_E
_RcftRemoteE1UnUsed_Object=MibTableColumn
rcftRemoteE1UnUsed=_RcftRemoteE1UnUsed_Object((1,3,6,1,4,1,8886,2,1,6,3,1,1,1,16),_RcftRemoteE1UnUsed_Type())
rcftRemoteE1UnUsed.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteE1UnUsed.setStatus(_A)
_RcftRemoteToLocalE1AlarmStatus_Type=Integer32
_RcftRemoteToLocalE1AlarmStatus_Object=MibTableColumn
rcftRemoteToLocalE1AlarmStatus=_RcftRemoteToLocalE1AlarmStatus_Object((1,3,6,1,4,1,8886,2,1,6,3,1,1,1,17),_RcftRemoteToLocalE1AlarmStatus_Type())
rcftRemoteToLocalE1AlarmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteToLocalE1AlarmStatus.setStatus(_A)
class _RcftRemoteE1Balance_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('balance',1),('imbalance',2)))
_RcftRemoteE1Balance_Type.__name__=_E
_RcftRemoteE1Balance_Object=MibTableColumn
rcftRemoteE1Balance=_RcftRemoteE1Balance_Object((1,3,6,1,4,1,8886,2,1,6,3,1,1,1,18),_RcftRemoteE1Balance_Type())
rcftRemoteE1Balance.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteE1Balance.setStatus(_A)
_RcftRemoteE1PortStatus_Type=Integer32
_RcftRemoteE1PortStatus_Object=MibTableColumn
rcftRemoteE1PortStatus=_RcftRemoteE1PortStatus_Object((1,3,6,1,4,1,8886,2,1,6,3,1,1,1,19),_RcftRemoteE1PortStatus_Type())
rcftRemoteE1PortStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteE1PortStatus.setStatus(_A)
_RcftRemoteE1PortTS0Mode_Type=Integer32
_RcftRemoteE1PortTS0Mode_Object=MibTableColumn
rcftRemoteE1PortTS0Mode=_RcftRemoteE1PortTS0Mode_Object((1,3,6,1,4,1,8886,2,1,6,3,1,1,1,20),_RcftRemoteE1PortTS0Mode_Type())
rcftRemoteE1PortTS0Mode.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteE1PortTS0Mode.setStatus(_A)
_RcftRemoteE1PortIdleCode_Type=Integer32
_RcftRemoteE1PortIdleCode_Object=MibTableColumn
rcftRemoteE1PortIdleCode=_RcftRemoteE1PortIdleCode_Object((1,3,6,1,4,1,8886,2,1,6,3,1,1,1,21),_RcftRemoteE1PortIdleCode_Type())
rcftRemoteE1PortIdleCode.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteE1PortIdleCode.setStatus(_A)
class _RcftRemoteE1LoopStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_l,1),(_m,2),(_n,3),(_o,4)))
_RcftRemoteE1LoopStatus_Type.__name__=_E
_RcftRemoteE1LoopStatus_Object=MibTableColumn
rcftRemoteE1LoopStatus=_RcftRemoteE1LoopStatus_Object((1,3,6,1,4,1,8886,2,1,6,3,1,1,1,22),_RcftRemoteE1LoopStatus_Type())
rcftRemoteE1LoopStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteE1LoopStatus.setStatus(_A)
_RcftRemoteE1OrderTimeParameter_Type=Integer32
_RcftRemoteE1OrderTimeParameter_Object=MibTableColumn
rcftRemoteE1OrderTimeParameter=_RcftRemoteE1OrderTimeParameter_Object((1,3,6,1,4,1,8886,2,1,6,3,1,1,1,23),_RcftRemoteE1OrderTimeParameter_Type())
rcftRemoteE1OrderTimeParameter.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteE1OrderTimeParameter.setStatus(_A)
_RcftRemoteE1OrderModeParameter_Type=Integer32
_RcftRemoteE1OrderModeParameter_Object=MibTableColumn
rcftRemoteE1OrderModeParameter=_RcftRemoteE1OrderModeParameter_Object((1,3,6,1,4,1,8886,2,1,6,3,1,1,1,24),_RcftRemoteE1OrderModeParameter_Type())
rcftRemoteE1OrderModeParameter.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteE1OrderModeParameter.setStatus(_A)
_RcftRemoteE1Order_Type=Integer32
_RcftRemoteE1Order_Object=MibTableColumn
rcftRemoteE1Order=_RcftRemoteE1Order_Object((1,3,6,1,4,1,8886,2,1,6,3,1,1,1,25),_RcftRemoteE1Order_Type())
rcftRemoteE1Order.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteE1Order.setStatus(_A)
_RcftRemoteE1PortType_Type=Integer32
_RcftRemoteE1PortType_Object=MibTableColumn
rcftRemoteE1PortType=_RcftRemoteE1PortType_Object((1,3,6,1,4,1,8886,2,1,6,3,1,1,1,26),_RcftRemoteE1PortType_Type())
rcftRemoteE1PortType.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteE1PortType.setStatus(_A)
_RcftRemoteE1BertStatus_Type=Integer32
_RcftRemoteE1BertStatus_Object=MibTableColumn
rcftRemoteE1BertStatus=_RcftRemoteE1BertStatus_Object((1,3,6,1,4,1,8886,2,1,6,3,1,1,1,27),_RcftRemoteE1BertStatus_Type())
rcftRemoteE1BertStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteE1BertStatus.setStatus(_A)
_RcftRemoteE1BertTime_Type=Unsigned32
_RcftRemoteE1BertTime_Object=MibTableColumn
rcftRemoteE1BertTime=_RcftRemoteE1BertTime_Object((1,3,6,1,4,1,8886,2,1,6,3,1,1,1,28),_RcftRemoteE1BertTime_Type())
rcftRemoteE1BertTime.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteE1BertTime.setStatus(_A)
_RcftRemoteE1BertErrCode_Type=Unsigned32
_RcftRemoteE1BertErrCode_Object=MibTableColumn
rcftRemoteE1BertErrCode=_RcftRemoteE1BertErrCode_Object((1,3,6,1,4,1,8886,2,1,6,3,1,1,1,29),_RcftRemoteE1BertErrCode_Type())
rcftRemoteE1BertErrCode.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteE1BertErrCode.setStatus(_A)
_RcftRemoteE1BertUnusedTime_Type=Unsigned32
_RcftRemoteE1BertUnusedTime_Object=MibTableColumn
rcftRemoteE1BertUnusedTime=_RcftRemoteE1BertUnusedTime_Object((1,3,6,1,4,1,8886,2,1,6,3,1,1,1,30),_RcftRemoteE1BertUnusedTime_Type())
rcftRemoteE1BertUnusedTime.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteE1BertUnusedTime.setStatus(_A)
_RcftRemoteE1BertPortSpeed_Type=Unsigned32
_RcftRemoteE1BertPortSpeed_Object=MibTableColumn
rcftRemoteE1BertPortSpeed=_RcftRemoteE1BertPortSpeed_Object((1,3,6,1,4,1,8886,2,1,6,3,1,1,1,31),_RcftRemoteE1BertPortSpeed_Type())
rcftRemoteE1BertPortSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteE1BertPortSpeed.setStatus(_A)
_RcftRemoteE1BertCodeType_Type=Integer32
_RcftRemoteE1BertCodeType_Object=MibTableColumn
rcftRemoteE1BertCodeType=_RcftRemoteE1BertCodeType_Object((1,3,6,1,4,1,8886,2,1,6,3,1,1,1,32),_RcftRemoteE1BertCodeType_Type())
rcftRemoteE1BertCodeType.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteE1BertCodeType.setStatus(_A)
_RcftRemoteE1BertCodeNum_Type=Integer32
_RcftRemoteE1BertCodeNum_Object=MibTableColumn
rcftRemoteE1BertCodeNum=_RcftRemoteE1BertCodeNum_Object((1,3,6,1,4,1,8886,2,1,6,3,1,1,1,33),_RcftRemoteE1BertCodeNum_Type())
rcftRemoteE1BertCodeNum.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteE1BertCodeNum.setStatus(_A)
_RcftRemoteE1LoopSwitchStatus_Type=Integer32
_RcftRemoteE1LoopSwitchStatus_Object=MibTableColumn
rcftRemoteE1LoopSwitchStatus=_RcftRemoteE1LoopSwitchStatus_Object((1,3,6,1,4,1,8886,2,1,6,3,1,1,1,34),_RcftRemoteE1LoopSwitchStatus_Type())
rcftRemoteE1LoopSwitchStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteE1LoopSwitchStatus.setStatus(_A)
_RcftRemoteE1AlarmRejest_Type=Integer32
_RcftRemoteE1AlarmRejest_Object=MibTableColumn
rcftRemoteE1AlarmRejest=_RcftRemoteE1AlarmRejest_Object((1,3,6,1,4,1,8886,2,1,6,3,1,1,1,35),_RcftRemoteE1AlarmRejest_Type())
rcftRemoteE1AlarmRejest.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteE1AlarmRejest.setStatus(_A)
_RcftRemoteT1AlarmStatus_Type=Integer32
_RcftRemoteT1AlarmStatus_Object=MibTableColumn
rcftRemoteT1AlarmStatus=_RcftRemoteT1AlarmStatus_Object((1,3,6,1,4,1,8886,2,1,6,3,1,1,1,36),_RcftRemoteT1AlarmStatus_Type())
rcftRemoteT1AlarmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteT1AlarmStatus.setStatus(_A)
_RcftRemoteE1PortVCGNumber_Type=Integer32
_RcftRemoteE1PortVCGNumber_Object=MibTableColumn
rcftRemoteE1PortVCGNumber=_RcftRemoteE1PortVCGNumber_Object((1,3,6,1,4,1,8886,2,1,6,3,1,1,1,37),_RcftRemoteE1PortVCGNumber_Type())
rcftRemoteE1PortVCGNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteE1PortVCGNumber.setStatus(_A)
_RcftRemoteE1ToLNumber_Type=Integer32
_RcftRemoteE1ToLNumber_Object=MibTableColumn
rcftRemoteE1ToLNumber=_RcftRemoteE1ToLNumber_Object((1,3,6,1,4,1,8886,2,1,6,3,1,1,1,38),_RcftRemoteE1ToLNumber_Type())
rcftRemoteE1ToLNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteE1ToLNumber.setStatus(_A)
_RcftRemoteE1CVCnt_Type=Integer32
_RcftRemoteE1CVCnt_Object=MibTableColumn
rcftRemoteE1CVCnt=_RcftRemoteE1CVCnt_Object((1,3,6,1,4,1,8886,2,1,6,3,1,1,1,39),_RcftRemoteE1CVCnt_Type())
rcftRemoteE1CVCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteE1CVCnt.setStatus(_A)
_RcftRemoteE1StatisticTable_Object=MibTable
rcftRemoteE1StatisticTable=_RcftRemoteE1StatisticTable_Object((1,3,6,1,4,1,8886,2,1,6,3,1,2))
if mibBuilder.loadTexts:rcftRemoteE1StatisticTable.setStatus(_A)
_RcftRemoteE1StatisticEntry_Object=MibTableRow
rcftRemoteE1StatisticEntry=_RcftRemoteE1StatisticEntry_Object((1,3,6,1,4,1,8886,2,1,6,3,1,2,1))
if mibBuilder.loadTexts:rcftRemoteE1StatisticEntry.setStatus(_A)
_RcftRemoteE1TxPackets_Type=Counter32
_RcftRemoteE1TxPackets_Object=MibTableColumn
rcftRemoteE1TxPackets=_RcftRemoteE1TxPackets_Object((1,3,6,1,4,1,8886,2,1,6,3,1,2,1,1),_RcftRemoteE1TxPackets_Type())
rcftRemoteE1TxPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteE1TxPackets.setStatus(_A)
_RcftRemoteE1TxBytes_Type=Counter32
_RcftRemoteE1TxBytes_Object=MibTableColumn
rcftRemoteE1TxBytes=_RcftRemoteE1TxBytes_Object((1,3,6,1,4,1,8886,2,1,6,3,1,2,1,2),_RcftRemoteE1TxBytes_Type())
rcftRemoteE1TxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteE1TxBytes.setStatus(_A)
_RcftRemoteE1RxPackets_Type=Counter32
_RcftRemoteE1RxPackets_Object=MibTableColumn
rcftRemoteE1RxPackets=_RcftRemoteE1RxPackets_Object((1,3,6,1,4,1,8886,2,1,6,3,1,2,1,3),_RcftRemoteE1RxPackets_Type())
rcftRemoteE1RxPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteE1RxPackets.setStatus(_A)
_RcftRemoteE1RxBytes_Type=Counter32
_RcftRemoteE1RxBytes_Object=MibTableColumn
rcftRemoteE1RxBytes=_RcftRemoteE1RxBytes_Object((1,3,6,1,4,1,8886,2,1,6,3,1,2,1,4),_RcftRemoteE1RxBytes_Type())
rcftRemoteE1RxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteE1RxBytes.setStatus(_A)
_RcftRemoteE1RxERRPackets_Type=Counter32
_RcftRemoteE1RxERRPackets_Object=MibTableColumn
rcftRemoteE1RxERRPackets=_RcftRemoteE1RxERRPackets_Object((1,3,6,1,4,1,8886,2,1,6,3,1,2,1,5),_RcftRemoteE1RxERRPackets_Type())
rcftRemoteE1RxERRPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteE1RxERRPackets.setStatus(_A)
_RcftRemoteE1FluxTimer_Type=Counter32
_RcftRemoteE1FluxTimer_Object=MibTableColumn
rcftRemoteE1FluxTimer=_RcftRemoteE1FluxTimer_Object((1,3,6,1,4,1,8886,2,1,6,3,1,2,1,6),_RcftRemoteE1FluxTimer_Type())
rcftRemoteE1FluxTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteE1FluxTimer.setStatus(_A)
_RcftRemoteE1LANTxPackets_Type=Counter32
_RcftRemoteE1LANTxPackets_Object=MibTableColumn
rcftRemoteE1LANTxPackets=_RcftRemoteE1LANTxPackets_Object((1,3,6,1,4,1,8886,2,1,6,3,1,2,1,7),_RcftRemoteE1LANTxPackets_Type())
rcftRemoteE1LANTxPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteE1LANTxPackets.setStatus(_A)
_RcftRemoteE1LANRxPackets_Type=Counter32
_RcftRemoteE1LANRxPackets_Object=MibTableColumn
rcftRemoteE1LANRxPackets=_RcftRemoteE1LANRxPackets_Object((1,3,6,1,4,1,8886,2,1,6,3,1,2,1,8),_RcftRemoteE1LANRxPackets_Type())
rcftRemoteE1LANRxPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteE1LANRxPackets.setStatus(_A)
_RcftRemoteE1LANRxLosPackets_Type=Counter32
_RcftRemoteE1LANRxLosPackets_Object=MibTableColumn
rcftRemoteE1LANRxLosPackets=_RcftRemoteE1LANRxLosPackets_Object((1,3,6,1,4,1,8886,2,1,6,3,1,2,1,9),_RcftRemoteE1LANRxLosPackets_Type())
rcftRemoteE1LANRxLosPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteE1LANRxLosPackets.setStatus(_A)
_RcftRemoteDeviceE1Traps_ObjectIdentity=ObjectIdentity
rcftRemoteDeviceE1Traps=_RcftRemoteDeviceE1Traps_ObjectIdentity((1,3,6,1,4,1,8886,2,1,6,3,2))
_RcftRemoteDeviceSHDSLMIB_ObjectIdentity=ObjectIdentity
rcftRemoteDeviceSHDSLMIB=_RcftRemoteDeviceSHDSLMIB_ObjectIdentity((1,3,6,1,4,1,8886,2,1,6,4))
_RcftRemoteSHDSLPortObjects_ObjectIdentity=ObjectIdentity
rcftRemoteSHDSLPortObjects=_RcftRemoteSHDSLPortObjects_ObjectIdentity((1,3,6,1,4,1,8886,2,1,6,4,1))
_RcftRemoteSHDSLPortTable_Object=MibTable
rcftRemoteSHDSLPortTable=_RcftRemoteSHDSLPortTable_Object((1,3,6,1,4,1,8886,2,1,6,4,1,1))
if mibBuilder.loadTexts:rcftRemoteSHDSLPortTable.setStatus(_A)
_RcftRemoteSHDSLPortEntry_Object=MibTableRow
rcftRemoteSHDSLPortEntry=_RcftRemoteSHDSLPortEntry_Object((1,3,6,1,4,1,8886,2,1,6,4,1,1,1))
rcftRemoteSHDSLPortEntry.setIndexNames((0,_F,_H),(0,_F,_I),(0,_C,_J),(0,_C,_V))
if mibBuilder.loadTexts:rcftRemoteSHDSLPortEntry.setStatus(_A)
_RcftRemoteSHDSLPortIndex_Type=Integer32
_RcftRemoteSHDSLPortIndex_Object=MibTableColumn
rcftRemoteSHDSLPortIndex=_RcftRemoteSHDSLPortIndex_Object((1,3,6,1,4,1,8886,2,1,6,4,1,1,1,1),_RcftRemoteSHDSLPortIndex_Type())
rcftRemoteSHDSLPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteSHDSLPortIndex.setStatus(_A)
_RcftRemoteSHDSLPortAlarmStatus_Type=Integer32
_RcftRemoteSHDSLPortAlarmStatus_Object=MibTableColumn
rcftRemoteSHDSLPortAlarmStatus=_RcftRemoteSHDSLPortAlarmStatus_Object((1,3,6,1,4,1,8886,2,1,6,4,1,1,1,2),_RcftRemoteSHDSLPortAlarmStatus_Type())
rcftRemoteSHDSLPortAlarmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteSHDSLPortAlarmStatus.setStatus(_A)
_RcftRemoteSHDSLPortStatus_Type=Integer32
_RcftRemoteSHDSLPortStatus_Object=MibTableColumn
rcftRemoteSHDSLPortStatus=_RcftRemoteSHDSLPortStatus_Object((1,3,6,1,4,1,8886,2,1,6,4,1,1,1,3),_RcftRemoteSHDSLPortStatus_Type())
rcftRemoteSHDSLPortStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteSHDSLPortStatus.setStatus(_A)
_RcftRemoteSHDSLPortCapableSpeed_Type=Integer32
_RcftRemoteSHDSLPortCapableSpeed_Object=MibTableColumn
rcftRemoteSHDSLPortCapableSpeed=_RcftRemoteSHDSLPortCapableSpeed_Object((1,3,6,1,4,1,8886,2,1,6,4,1,1,1,4),_RcftRemoteSHDSLPortCapableSpeed_Type())
rcftRemoteSHDSLPortCapableSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteSHDSLPortCapableSpeed.setStatus(_A)
_RcftRemoteSHDSLPortWorkSpeed_Type=Integer32
_RcftRemoteSHDSLPortWorkSpeed_Object=MibTableColumn
rcftRemoteSHDSLPortWorkSpeed=_RcftRemoteSHDSLPortWorkSpeed_Object((1,3,6,1,4,1,8886,2,1,6,4,1,1,1,5),_RcftRemoteSHDSLPortWorkSpeed_Type())
rcftRemoteSHDSLPortWorkSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteSHDSLPortWorkSpeed.setStatus(_A)
_RcftRemoteSHDSLPortProbeMaxSpeed_Type=Integer32
_RcftRemoteSHDSLPortProbeMaxSpeed_Object=MibTableColumn
rcftRemoteSHDSLPortProbeMaxSpeed=_RcftRemoteSHDSLPortProbeMaxSpeed_Object((1,3,6,1,4,1,8886,2,1,6,4,1,1,1,6),_RcftRemoteSHDSLPortProbeMaxSpeed_Type())
rcftRemoteSHDSLPortProbeMaxSpeed.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteSHDSLPortProbeMaxSpeed.setStatus(_A)
_RcftRemoteSHDSLPortProbeMinSpeed_Type=Integer32
_RcftRemoteSHDSLPortProbeMinSpeed_Object=MibTableColumn
rcftRemoteSHDSLPortProbeMinSpeed=_RcftRemoteSHDSLPortProbeMinSpeed_Object((1,3,6,1,4,1,8886,2,1,6,4,1,1,1,7),_RcftRemoteSHDSLPortProbeMinSpeed_Type())
rcftRemoteSHDSLPortProbeMinSpeed.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteSHDSLPortProbeMinSpeed.setStatus(_A)
_RcftRemoteSDHSLPortSNR_Type=Integer32
_RcftRemoteSDHSLPortSNR_Object=MibTableColumn
rcftRemoteSDHSLPortSNR=_RcftRemoteSDHSLPortSNR_Object((1,3,6,1,4,1,8886,2,1,6,4,1,1,1,8),_RcftRemoteSDHSLPortSNR_Type())
rcftRemoteSDHSLPortSNR.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteSDHSLPortSNR.setStatus(_A)
_RcftRemoteSHDSLPortConfigSNR_Type=Integer32
_RcftRemoteSHDSLPortConfigSNR_Object=MibTableColumn
rcftRemoteSHDSLPortConfigSNR=_RcftRemoteSHDSLPortConfigSNR_Object((1,3,6,1,4,1,8886,2,1,6,4,1,1,1,9),_RcftRemoteSHDSLPortConfigSNR_Type())
rcftRemoteSHDSLPortConfigSNR.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteSHDSLPortConfigSNR.setStatus(_A)
_RcftRemoteSHDSLPortSNRThreshold_Type=Integer32
_RcftRemoteSHDSLPortSNRThreshold_Object=MibTableColumn
rcftRemoteSHDSLPortSNRThreshold=_RcftRemoteSHDSLPortSNRThreshold_Object((1,3,6,1,4,1,8886,2,1,6,4,1,1,1,10),_RcftRemoteSHDSLPortSNRThreshold_Type())
rcftRemoteSHDSLPortSNRThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteSHDSLPortSNRThreshold.setStatus(_A)
_RcftRemoteSHDSLPortAttenuation_Type=Integer32
_RcftRemoteSHDSLPortAttenuation_Object=MibTableColumn
rcftRemoteSHDSLPortAttenuation=_RcftRemoteSHDSLPortAttenuation_Object((1,3,6,1,4,1,8886,2,1,6,4,1,1,1,11),_RcftRemoteSHDSLPortAttenuation_Type())
rcftRemoteSHDSLPortAttenuation.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteSHDSLPortAttenuation.setStatus(_A)
_RcftRemoteSHDSLPortAttenuationThreshold_Type=Integer32
_RcftRemoteSHDSLPortAttenuationThreshold_Object=MibTableColumn
rcftRemoteSHDSLPortAttenuationThreshold=_RcftRemoteSHDSLPortAttenuationThreshold_Object((1,3,6,1,4,1,8886,2,1,6,4,1,1,1,12),_RcftRemoteSHDSLPortAttenuationThreshold_Type())
rcftRemoteSHDSLPortAttenuationThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteSHDSLPortAttenuationThreshold.setStatus(_A)
_RcftRemoteSHDSLPortPBO_Type=Integer32
_RcftRemoteSHDSLPortPBO_Object=MibTableColumn
rcftRemoteSHDSLPortPBO=_RcftRemoteSHDSLPortPBO_Object((1,3,6,1,4,1,8886,2,1,6,4,1,1,1,13),_RcftRemoteSHDSLPortPBO_Type())
rcftRemoteSHDSLPortPBO.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteSHDSLPortPBO.setStatus(_A)
_RcftRemoteSHDSLPortLOSThreshold_Type=Integer32
_RcftRemoteSHDSLPortLOSThreshold_Object=MibTableColumn
rcftRemoteSHDSLPortLOSThreshold=_RcftRemoteSHDSLPortLOSThreshold_Object((1,3,6,1,4,1,8886,2,1,6,4,1,1,1,14),_RcftRemoteSHDSLPortLOSThreshold_Type())
rcftRemoteSHDSLPortLOSThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteSHDSLPortLOSThreshold.setStatus(_A)
_RcftRemoteSHDSLPortLOSWThreshold_Type=Integer32
_RcftRemoteSHDSLPortLOSWThreshold_Object=MibTableColumn
rcftRemoteSHDSLPortLOSWThreshold=_RcftRemoteSHDSLPortLOSWThreshold_Object((1,3,6,1,4,1,8886,2,1,6,4,1,1,1,15),_RcftRemoteSHDSLPortLOSWThreshold_Type())
rcftRemoteSHDSLPortLOSWThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteSHDSLPortLOSWThreshold.setStatus(_A)
_RcftRemoteSHDSLPortLOLKThreshold_Type=Integer32
_RcftRemoteSHDSLPortLOLKThreshold_Object=MibTableColumn
rcftRemoteSHDSLPortLOLKThreshold=_RcftRemoteSHDSLPortLOLKThreshold_Object((1,3,6,1,4,1,8886,2,1,6,4,1,1,1,16),_RcftRemoteSHDSLPortLOLKThreshold_Type())
rcftRemoteSHDSLPortLOLKThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteSHDSLPortLOLKThreshold.setStatus(_A)
_RcftRemoteSHDSLPortESThreshold_Type=Integer32
_RcftRemoteSHDSLPortESThreshold_Object=MibTableColumn
rcftRemoteSHDSLPortESThreshold=_RcftRemoteSHDSLPortESThreshold_Object((1,3,6,1,4,1,8886,2,1,6,4,1,1,1,17),_RcftRemoteSHDSLPortESThreshold_Type())
rcftRemoteSHDSLPortESThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteSHDSLPortESThreshold.setStatus(_A)
class _RcftRemoteSHDSLPortLoopStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,100)));namedValues=NamedValues(*(('insideLoop',1),('outsideLoop',2),('doubleloop',3),(_U,100)))
_RcftRemoteSHDSLPortLoopStatus_Type.__name__=_E
_RcftRemoteSHDSLPortLoopStatus_Object=MibTableColumn
rcftRemoteSHDSLPortLoopStatus=_RcftRemoteSHDSLPortLoopStatus_Object((1,3,6,1,4,1,8886,2,1,6,4,1,1,1,18),_RcftRemoteSHDSLPortLoopStatus_Type())
rcftRemoteSHDSLPortLoopStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteSHDSLPortLoopStatus.setStatus(_A)
_RcftRemoteSHDSLPortAttenuationInitThreshhold_Type=Integer32
_RcftRemoteSHDSLPortAttenuationInitThreshhold_Object=MibTableColumn
rcftRemoteSHDSLPortAttenuationInitThreshhold=_RcftRemoteSHDSLPortAttenuationInitThreshhold_Object((1,3,6,1,4,1,8886,2,1,6,4,1,1,1,19),_RcftRemoteSHDSLPortAttenuationInitThreshhold_Type())
rcftRemoteSHDSLPortAttenuationInitThreshhold.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteSHDSLPortAttenuationInitThreshhold.setStatus(_A)
_RcftRemoteSHDSLPortOrderTimeParameter_Type=Integer32
_RcftRemoteSHDSLPortOrderTimeParameter_Object=MibTableColumn
rcftRemoteSHDSLPortOrderTimeParameter=_RcftRemoteSHDSLPortOrderTimeParameter_Object((1,3,6,1,4,1,8886,2,1,6,4,1,1,1,20),_RcftRemoteSHDSLPortOrderTimeParameter_Type())
rcftRemoteSHDSLPortOrderTimeParameter.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteSHDSLPortOrderTimeParameter.setStatus(_A)
_RcftRemoteSHDSLPortOrderModeParameter_Type=Integer32
_RcftRemoteSHDSLPortOrderModeParameter_Object=MibTableColumn
rcftRemoteSHDSLPortOrderModeParameter=_RcftRemoteSHDSLPortOrderModeParameter_Object((1,3,6,1,4,1,8886,2,1,6,4,1,1,1,21),_RcftRemoteSHDSLPortOrderModeParameter_Type())
rcftRemoteSHDSLPortOrderModeParameter.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteSHDSLPortOrderModeParameter.setStatus(_A)
_RcftRemoteSHDSLPortOrder_Type=Integer32
_RcftRemoteSHDSLPortOrder_Object=MibTableColumn
rcftRemoteSHDSLPortOrder=_RcftRemoteSHDSLPortOrder_Object((1,3,6,1,4,1,8886,2,1,6,4,1,1,1,22),_RcftRemoteSHDSLPortOrder_Type())
rcftRemoteSHDSLPortOrder.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteSHDSLPortOrder.setStatus(_A)
_RcftRemoteSHDSLPortPBOAmount_Type=Integer32
_RcftRemoteSHDSLPortPBOAmount_Object=MibTableColumn
rcftRemoteSHDSLPortPBOAmount=_RcftRemoteSHDSLPortPBOAmount_Object((1,3,6,1,4,1,8886,2,1,6,4,1,1,1,23),_RcftRemoteSHDSLPortPBOAmount_Type())
rcftRemoteSHDSLPortPBOAmount.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteSHDSLPortPBOAmount.setStatus(_A)
_RcftRemoteSHDSLBertStatus_Type=Integer32
_RcftRemoteSHDSLBertStatus_Object=MibTableColumn
rcftRemoteSHDSLBertStatus=_RcftRemoteSHDSLBertStatus_Object((1,3,6,1,4,1,8886,2,1,6,4,1,1,1,24),_RcftRemoteSHDSLBertStatus_Type())
rcftRemoteSHDSLBertStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteSHDSLBertStatus.setStatus(_A)
_RcftRemoteSHDSLBertTime_Type=Unsigned32
_RcftRemoteSHDSLBertTime_Object=MibTableColumn
rcftRemoteSHDSLBertTime=_RcftRemoteSHDSLBertTime_Object((1,3,6,1,4,1,8886,2,1,6,4,1,1,1,25),_RcftRemoteSHDSLBertTime_Type())
rcftRemoteSHDSLBertTime.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteSHDSLBertTime.setStatus(_A)
_RcftRemoteSHDSLBertErrCode_Type=Unsigned32
_RcftRemoteSHDSLBertErrCode_Object=MibTableColumn
rcftRemoteSHDSLBertErrCode=_RcftRemoteSHDSLBertErrCode_Object((1,3,6,1,4,1,8886,2,1,6,4,1,1,1,26),_RcftRemoteSHDSLBertErrCode_Type())
rcftRemoteSHDSLBertErrCode.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteSHDSLBertErrCode.setStatus(_A)
_RcftRemoteSHDSLBertUnusedTime_Type=Unsigned32
_RcftRemoteSHDSLBertUnusedTime_Object=MibTableColumn
rcftRemoteSHDSLBertUnusedTime=_RcftRemoteSHDSLBertUnusedTime_Object((1,3,6,1,4,1,8886,2,1,6,4,1,1,1,27),_RcftRemoteSHDSLBertUnusedTime_Type())
rcftRemoteSHDSLBertUnusedTime.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteSHDSLBertUnusedTime.setStatus(_A)
_RcftRemoteSHDSLBertPortSpeed_Type=Unsigned32
_RcftRemoteSHDSLBertPortSpeed_Object=MibTableColumn
rcftRemoteSHDSLBertPortSpeed=_RcftRemoteSHDSLBertPortSpeed_Object((1,3,6,1,4,1,8886,2,1,6,4,1,1,1,28),_RcftRemoteSHDSLBertPortSpeed_Type())
rcftRemoteSHDSLBertPortSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteSHDSLBertPortSpeed.setStatus(_A)
_RcftRemoteSHDSLBertCodeType_Type=Integer32
_RcftRemoteSHDSLBertCodeType_Object=MibTableColumn
rcftRemoteSHDSLBertCodeType=_RcftRemoteSHDSLBertCodeType_Object((1,3,6,1,4,1,8886,2,1,6,4,1,1,1,29),_RcftRemoteSHDSLBertCodeType_Type())
rcftRemoteSHDSLBertCodeType.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteSHDSLBertCodeType.setStatus(_A)
_RcftRemoteSHDSLBertCodeNum_Type=Integer32
_RcftRemoteSHDSLBertCodeNum_Object=MibTableColumn
rcftRemoteSHDSLBertCodeNum=_RcftRemoteSHDSLBertCodeNum_Object((1,3,6,1,4,1,8886,2,1,6,4,1,1,1,30),_RcftRemoteSHDSLBertCodeNum_Type())
rcftRemoteSHDSLBertCodeNum.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteSHDSLBertCodeNum.setStatus(_A)
class _RcftRemoteSHDSLLoopStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_l,1),(_m,2),(_n,3),(_o,4),(_U,5),(_AI,6),(_AJ,7)))
_RcftRemoteSHDSLLoopStatus_Type.__name__=_E
_RcftRemoteSHDSLLoopStatus_Object=MibTableColumn
rcftRemoteSHDSLLoopStatus=_RcftRemoteSHDSLLoopStatus_Object((1,3,6,1,4,1,8886,2,1,6,4,1,1,1,31),_RcftRemoteSHDSLLoopStatus_Type())
rcftRemoteSHDSLLoopStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteSHDSLLoopStatus.setStatus(_A)
_RcftRemoteSHDSLPortPerformance_ObjectIdentity=ObjectIdentity
rcftRemoteSHDSLPortPerformance=_RcftRemoteSHDSLPortPerformance_ObjectIdentity((1,3,6,1,4,1,8886,2,1,6,4,2))
_RcftRemoteSHDSLPortCurrentTable_Object=MibTable
rcftRemoteSHDSLPortCurrentTable=_RcftRemoteSHDSLPortCurrentTable_Object((1,3,6,1,4,1,8886,2,1,6,4,2,1))
if mibBuilder.loadTexts:rcftRemoteSHDSLPortCurrentTable.setStatus(_A)
_RcftRemoteSHDSLPortCurrentEntry_Object=MibTableRow
rcftRemoteSHDSLPortCurrentEntry=_RcftRemoteSHDSLPortCurrentEntry_Object((1,3,6,1,4,1,8886,2,1,6,4,2,1,1))
rcftRemoteSHDSLPortCurrentEntry.setIndexNames((0,_F,_H),(0,_F,_I),(0,_C,_J),(0,_C,_V))
if mibBuilder.loadTexts:rcftRemoteSHDSLPortCurrentEntry.setStatus(_A)
_RcftRemoteSHDSLPortCurrentLOSTimes_Type=Integer32
_RcftRemoteSHDSLPortCurrentLOSTimes_Object=MibTableColumn
rcftRemoteSHDSLPortCurrentLOSTimes=_RcftRemoteSHDSLPortCurrentLOSTimes_Object((1,3,6,1,4,1,8886,2,1,6,4,2,1,1,1),_RcftRemoteSHDSLPortCurrentLOSTimes_Type())
rcftRemoteSHDSLPortCurrentLOSTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteSHDSLPortCurrentLOSTimes.setStatus(_A)
_RcftRemoteSHDSLPortCurrentLOSWTimes_Type=Integer32
_RcftRemoteSHDSLPortCurrentLOSWTimes_Object=MibTableColumn
rcftRemoteSHDSLPortCurrentLOSWTimes=_RcftRemoteSHDSLPortCurrentLOSWTimes_Object((1,3,6,1,4,1,8886,2,1,6,4,2,1,1,2),_RcftRemoteSHDSLPortCurrentLOSWTimes_Type())
rcftRemoteSHDSLPortCurrentLOSWTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteSHDSLPortCurrentLOSWTimes.setStatus(_A)
_RcftRemoteSHDSLPortCurrentLOLKTimes_Type=Integer32
_RcftRemoteSHDSLPortCurrentLOLKTimes_Object=MibTableColumn
rcftRemoteSHDSLPortCurrentLOLKTimes=_RcftRemoteSHDSLPortCurrentLOLKTimes_Object((1,3,6,1,4,1,8886,2,1,6,4,2,1,1,3),_RcftRemoteSHDSLPortCurrentLOLKTimes_Type())
rcftRemoteSHDSLPortCurrentLOLKTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteSHDSLPortCurrentLOLKTimes.setStatus(_A)
_RcftRemoteSHDSLPortCurrentCVTimes_Type=Integer32
_RcftRemoteSHDSLPortCurrentCVTimes_Object=MibTableColumn
rcftRemoteSHDSLPortCurrentCVTimes=_RcftRemoteSHDSLPortCurrentCVTimes_Object((1,3,6,1,4,1,8886,2,1,6,4,2,1,1,4),_RcftRemoteSHDSLPortCurrentCVTimes_Type())
rcftRemoteSHDSLPortCurrentCVTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteSHDSLPortCurrentCVTimes.setStatus(_A)
_RcftRemoteSHDSLPortCurrentES_Type=Integer32
_RcftRemoteSHDSLPortCurrentES_Object=MibTableColumn
rcftRemoteSHDSLPortCurrentES=_RcftRemoteSHDSLPortCurrentES_Object((1,3,6,1,4,1,8886,2,1,6,4,2,1,1,5),_RcftRemoteSHDSLPortCurrentES_Type())
rcftRemoteSHDSLPortCurrentES.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteSHDSLPortCurrentES.setStatus(_A)
_RcftRemoteSHDSLPortCurrentSES_Type=Integer32
_RcftRemoteSHDSLPortCurrentSES_Object=MibTableColumn
rcftRemoteSHDSLPortCurrentSES=_RcftRemoteSHDSLPortCurrentSES_Object((1,3,6,1,4,1,8886,2,1,6,4,2,1,1,6),_RcftRemoteSHDSLPortCurrentSES_Type())
rcftRemoteSHDSLPortCurrentSES.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteSHDSLPortCurrentSES.setStatus(_A)
_RcftRemoteSHDSLPortCurrentUAS_Type=Integer32
_RcftRemoteSHDSLPortCurrentUAS_Object=MibTableColumn
rcftRemoteSHDSLPortCurrentUAS=_RcftRemoteSHDSLPortCurrentUAS_Object((1,3,6,1,4,1,8886,2,1,6,4,2,1,1,7),_RcftRemoteSHDSLPortCurrentUAS_Type())
rcftRemoteSHDSLPortCurrentUAS.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteSHDSLPortCurrentUAS.setStatus(_A)
_RcftRemoteSHDSLPortCurrentLOSWS_Type=Integer32
_RcftRemoteSHDSLPortCurrentLOSWS_Object=MibTableColumn
rcftRemoteSHDSLPortCurrentLOSWS=_RcftRemoteSHDSLPortCurrentLOSWS_Object((1,3,6,1,4,1,8886,2,1,6,4,2,1,1,8),_RcftRemoteSHDSLPortCurrentLOSWS_Type())
rcftRemoteSHDSLPortCurrentLOSWS.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteSHDSLPortCurrentLOSWS.setStatus(_A)
_RcftRemoteSHDSLPortCurrentCRCTimes_Type=Integer32
_RcftRemoteSHDSLPortCurrentCRCTimes_Object=MibTableColumn
rcftRemoteSHDSLPortCurrentCRCTimes=_RcftRemoteSHDSLPortCurrentCRCTimes_Object((1,3,6,1,4,1,8886,2,1,6,4,2,1,1,9),_RcftRemoteSHDSLPortCurrentCRCTimes_Type())
rcftRemoteSHDSLPortCurrentCRCTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteSHDSLPortCurrentCRCTimes.setStatus(_A)
_RcftRemoteSHDSLPortIntervalTable_Object=MibTable
rcftRemoteSHDSLPortIntervalTable=_RcftRemoteSHDSLPortIntervalTable_Object((1,3,6,1,4,1,8886,2,1,6,4,2,2))
if mibBuilder.loadTexts:rcftRemoteSHDSLPortIntervalTable.setStatus(_A)
_RcftRemoteSHDSLPortIntervalEntry_Object=MibTableRow
rcftRemoteSHDSLPortIntervalEntry=_RcftRemoteSHDSLPortIntervalEntry_Object((1,3,6,1,4,1,8886,2,1,6,4,2,2,1))
rcftRemoteSHDSLPortIntervalEntry.setIndexNames((0,_F,_H),(0,_F,_I),(0,_C,_J),(0,_C,_V),(0,_C,_AK))
if mibBuilder.loadTexts:rcftRemoteSHDSLPortIntervalEntry.setStatus(_A)
_RcftRemoteSHDSLPortIntervalNumber_Type=Integer32
_RcftRemoteSHDSLPortIntervalNumber_Object=MibTableColumn
rcftRemoteSHDSLPortIntervalNumber=_RcftRemoteSHDSLPortIntervalNumber_Object((1,3,6,1,4,1,8886,2,1,6,4,2,2,1,1),_RcftRemoteSHDSLPortIntervalNumber_Type())
rcftRemoteSHDSLPortIntervalNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteSHDSLPortIntervalNumber.setStatus(_A)
_RcftRemoteSHDSLPortIntervalLOSTimes_Type=Integer32
_RcftRemoteSHDSLPortIntervalLOSTimes_Object=MibTableColumn
rcftRemoteSHDSLPortIntervalLOSTimes=_RcftRemoteSHDSLPortIntervalLOSTimes_Object((1,3,6,1,4,1,8886,2,1,6,4,2,2,1,2),_RcftRemoteSHDSLPortIntervalLOSTimes_Type())
rcftRemoteSHDSLPortIntervalLOSTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteSHDSLPortIntervalLOSTimes.setStatus(_A)
_RcftRemoteSHDSLPortIntervalLOSWTimes_Type=Integer32
_RcftRemoteSHDSLPortIntervalLOSWTimes_Object=MibTableColumn
rcftRemoteSHDSLPortIntervalLOSWTimes=_RcftRemoteSHDSLPortIntervalLOSWTimes_Object((1,3,6,1,4,1,8886,2,1,6,4,2,2,1,3),_RcftRemoteSHDSLPortIntervalLOSWTimes_Type())
rcftRemoteSHDSLPortIntervalLOSWTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteSHDSLPortIntervalLOSWTimes.setStatus(_A)
_RcftRemoteSHDSLPortIntervalLOLKTimes_Type=Integer32
_RcftRemoteSHDSLPortIntervalLOLKTimes_Object=MibTableColumn
rcftRemoteSHDSLPortIntervalLOLKTimes=_RcftRemoteSHDSLPortIntervalLOLKTimes_Object((1,3,6,1,4,1,8886,2,1,6,4,2,2,1,4),_RcftRemoteSHDSLPortIntervalLOLKTimes_Type())
rcftRemoteSHDSLPortIntervalLOLKTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteSHDSLPortIntervalLOLKTimes.setStatus(_A)
_RcftRemoteSHDSLPortIntervalCVTimes_Type=Integer32
_RcftRemoteSHDSLPortIntervalCVTimes_Object=MibTableColumn
rcftRemoteSHDSLPortIntervalCVTimes=_RcftRemoteSHDSLPortIntervalCVTimes_Object((1,3,6,1,4,1,8886,2,1,6,4,2,2,1,5),_RcftRemoteSHDSLPortIntervalCVTimes_Type())
rcftRemoteSHDSLPortIntervalCVTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteSHDSLPortIntervalCVTimes.setStatus(_A)
_RcftRemoteSHDSLPortIntervalES_Type=Integer32
_RcftRemoteSHDSLPortIntervalES_Object=MibTableColumn
rcftRemoteSHDSLPortIntervalES=_RcftRemoteSHDSLPortIntervalES_Object((1,3,6,1,4,1,8886,2,1,6,4,2,2,1,6),_RcftRemoteSHDSLPortIntervalES_Type())
rcftRemoteSHDSLPortIntervalES.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteSHDSLPortIntervalES.setStatus(_A)
_RcftRemoteSHDSLPortIntervalSES_Type=Integer32
_RcftRemoteSHDSLPortIntervalSES_Object=MibTableColumn
rcftRemoteSHDSLPortIntervalSES=_RcftRemoteSHDSLPortIntervalSES_Object((1,3,6,1,4,1,8886,2,1,6,4,2,2,1,7),_RcftRemoteSHDSLPortIntervalSES_Type())
rcftRemoteSHDSLPortIntervalSES.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteSHDSLPortIntervalSES.setStatus(_A)
_RcftRemoteSHDSLPortIntervalUAS_Type=Integer32
_RcftRemoteSHDSLPortIntervalUAS_Object=MibTableColumn
rcftRemoteSHDSLPortIntervalUAS=_RcftRemoteSHDSLPortIntervalUAS_Object((1,3,6,1,4,1,8886,2,1,6,4,2,2,1,8),_RcftRemoteSHDSLPortIntervalUAS_Type())
rcftRemoteSHDSLPortIntervalUAS.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteSHDSLPortIntervalUAS.setStatus(_A)
_RcftRemoteSHDSLPortIntervalLOSWS_Type=Integer32
_RcftRemoteSHDSLPortIntervalLOSWS_Object=MibTableColumn
rcftRemoteSHDSLPortIntervalLOSWS=_RcftRemoteSHDSLPortIntervalLOSWS_Object((1,3,6,1,4,1,8886,2,1,6,4,2,2,1,9),_RcftRemoteSHDSLPortIntervalLOSWS_Type())
rcftRemoteSHDSLPortIntervalLOSWS.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteSHDSLPortIntervalLOSWS.setStatus(_A)
_RcftRemoteSHDSLPortIntervalCRCTimes_Type=Integer32
_RcftRemoteSHDSLPortIntervalCRCTimes_Object=MibTableColumn
rcftRemoteSHDSLPortIntervalCRCTimes=_RcftRemoteSHDSLPortIntervalCRCTimes_Object((1,3,6,1,4,1,8886,2,1,6,4,2,2,1,10),_RcftRemoteSHDSLPortIntervalCRCTimes_Type())
rcftRemoteSHDSLPortIntervalCRCTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteSHDSLPortIntervalCRCTimes.setStatus(_A)
_RcftRemoteSHDSLPortCurrentDayTable_Object=MibTable
rcftRemoteSHDSLPortCurrentDayTable=_RcftRemoteSHDSLPortCurrentDayTable_Object((1,3,6,1,4,1,8886,2,1,6,4,2,3))
if mibBuilder.loadTexts:rcftRemoteSHDSLPortCurrentDayTable.setStatus(_A)
_RcftRemoteSHDSLPortCurrentDayEntry_Object=MibTableRow
rcftRemoteSHDSLPortCurrentDayEntry=_RcftRemoteSHDSLPortCurrentDayEntry_Object((1,3,6,1,4,1,8886,2,1,6,4,2,3,1))
rcftRemoteSHDSLPortCurrentDayEntry.setIndexNames((0,_F,_H),(0,_F,_I),(0,_C,_J),(0,_C,_V))
if mibBuilder.loadTexts:rcftRemoteSHDSLPortCurrentDayEntry.setStatus(_A)
_RcftRemoteSHDSLPortCurrentDayLOSTimes_Type=Integer32
_RcftRemoteSHDSLPortCurrentDayLOSTimes_Object=MibTableColumn
rcftRemoteSHDSLPortCurrentDayLOSTimes=_RcftRemoteSHDSLPortCurrentDayLOSTimes_Object((1,3,6,1,4,1,8886,2,1,6,4,2,3,1,1),_RcftRemoteSHDSLPortCurrentDayLOSTimes_Type())
rcftRemoteSHDSLPortCurrentDayLOSTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteSHDSLPortCurrentDayLOSTimes.setStatus(_A)
_RcftRemoteSHDSLPortCurrentDayLOSWTimes_Type=Integer32
_RcftRemoteSHDSLPortCurrentDayLOSWTimes_Object=MibTableColumn
rcftRemoteSHDSLPortCurrentDayLOSWTimes=_RcftRemoteSHDSLPortCurrentDayLOSWTimes_Object((1,3,6,1,4,1,8886,2,1,6,4,2,3,1,2),_RcftRemoteSHDSLPortCurrentDayLOSWTimes_Type())
rcftRemoteSHDSLPortCurrentDayLOSWTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteSHDSLPortCurrentDayLOSWTimes.setStatus(_A)
_RcftRemoteSHDSLPortCurrentDayLOLKTimes_Type=Integer32
_RcftRemoteSHDSLPortCurrentDayLOLKTimes_Object=MibTableColumn
rcftRemoteSHDSLPortCurrentDayLOLKTimes=_RcftRemoteSHDSLPortCurrentDayLOLKTimes_Object((1,3,6,1,4,1,8886,2,1,6,4,2,3,1,3),_RcftRemoteSHDSLPortCurrentDayLOLKTimes_Type())
rcftRemoteSHDSLPortCurrentDayLOLKTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteSHDSLPortCurrentDayLOLKTimes.setStatus(_A)
_RcftRemoteSHDSLPortCurrentDayCVTimes_Type=Integer32
_RcftRemoteSHDSLPortCurrentDayCVTimes_Object=MibTableColumn
rcftRemoteSHDSLPortCurrentDayCVTimes=_RcftRemoteSHDSLPortCurrentDayCVTimes_Object((1,3,6,1,4,1,8886,2,1,6,4,2,3,1,4),_RcftRemoteSHDSLPortCurrentDayCVTimes_Type())
rcftRemoteSHDSLPortCurrentDayCVTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteSHDSLPortCurrentDayCVTimes.setStatus(_A)
_RcftRemoteSHDSLPortCurrentDayES_Type=Integer32
_RcftRemoteSHDSLPortCurrentDayES_Object=MibTableColumn
rcftRemoteSHDSLPortCurrentDayES=_RcftRemoteSHDSLPortCurrentDayES_Object((1,3,6,1,4,1,8886,2,1,6,4,2,3,1,5),_RcftRemoteSHDSLPortCurrentDayES_Type())
rcftRemoteSHDSLPortCurrentDayES.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteSHDSLPortCurrentDayES.setStatus(_A)
_RcftRemoteSHDSLPortCurrentDaySES_Type=Integer32
_RcftRemoteSHDSLPortCurrentDaySES_Object=MibTableColumn
rcftRemoteSHDSLPortCurrentDaySES=_RcftRemoteSHDSLPortCurrentDaySES_Object((1,3,6,1,4,1,8886,2,1,6,4,2,3,1,6),_RcftRemoteSHDSLPortCurrentDaySES_Type())
rcftRemoteSHDSLPortCurrentDaySES.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteSHDSLPortCurrentDaySES.setStatus(_A)
_RcftRemoteSHDSLPortCurrentDayUAS_Type=Integer32
_RcftRemoteSHDSLPortCurrentDayUAS_Object=MibTableColumn
rcftRemoteSHDSLPortCurrentDayUAS=_RcftRemoteSHDSLPortCurrentDayUAS_Object((1,3,6,1,4,1,8886,2,1,6,4,2,3,1,7),_RcftRemoteSHDSLPortCurrentDayUAS_Type())
rcftRemoteSHDSLPortCurrentDayUAS.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteSHDSLPortCurrentDayUAS.setStatus(_A)
_RcftRemoteSHDSLPortCurrentDayLOSWS_Type=Integer32
_RcftRemoteSHDSLPortCurrentDayLOSWS_Object=MibTableColumn
rcftRemoteSHDSLPortCurrentDayLOSWS=_RcftRemoteSHDSLPortCurrentDayLOSWS_Object((1,3,6,1,4,1,8886,2,1,6,4,2,3,1,8),_RcftRemoteSHDSLPortCurrentDayLOSWS_Type())
rcftRemoteSHDSLPortCurrentDayLOSWS.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteSHDSLPortCurrentDayLOSWS.setStatus(_A)
_RcftRemoteSHDSLPortCurrentDayCRCTimes_Type=Integer32
_RcftRemoteSHDSLPortCurrentDayCRCTimes_Object=MibTableColumn
rcftRemoteSHDSLPortCurrentDayCRCTimes=_RcftRemoteSHDSLPortCurrentDayCRCTimes_Object((1,3,6,1,4,1,8886,2,1,6,4,2,3,1,9),_RcftRemoteSHDSLPortCurrentDayCRCTimes_Type())
rcftRemoteSHDSLPortCurrentDayCRCTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteSHDSLPortCurrentDayCRCTimes.setStatus(_A)
_RcftRemoteSHDSLPortIntervalDayTable_Object=MibTable
rcftRemoteSHDSLPortIntervalDayTable=_RcftRemoteSHDSLPortIntervalDayTable_Object((1,3,6,1,4,1,8886,2,1,6,4,2,4))
if mibBuilder.loadTexts:rcftRemoteSHDSLPortIntervalDayTable.setStatus(_A)
_RcftRemoteSHDSLPortIntervalDayEntry_Object=MibTableRow
rcftRemoteSHDSLPortIntervalDayEntry=_RcftRemoteSHDSLPortIntervalDayEntry_Object((1,3,6,1,4,1,8886,2,1,6,4,2,4,1))
rcftRemoteSHDSLPortIntervalDayEntry.setIndexNames((0,_F,_H),(0,_F,_I),(0,_C,_J),(0,_C,_V),(0,_C,_AL))
if mibBuilder.loadTexts:rcftRemoteSHDSLPortIntervalDayEntry.setStatus(_A)
_RcftRemoteSHDSLPortIntervalDayNumber_Type=Integer32
_RcftRemoteSHDSLPortIntervalDayNumber_Object=MibTableColumn
rcftRemoteSHDSLPortIntervalDayNumber=_RcftRemoteSHDSLPortIntervalDayNumber_Object((1,3,6,1,4,1,8886,2,1,6,4,2,4,1,1),_RcftRemoteSHDSLPortIntervalDayNumber_Type())
rcftRemoteSHDSLPortIntervalDayNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteSHDSLPortIntervalDayNumber.setStatus(_A)
_RcftRemoteSHDSLPortIntervalDayLOSTimes_Type=Integer32
_RcftRemoteSHDSLPortIntervalDayLOSTimes_Object=MibTableColumn
rcftRemoteSHDSLPortIntervalDayLOSTimes=_RcftRemoteSHDSLPortIntervalDayLOSTimes_Object((1,3,6,1,4,1,8886,2,1,6,4,2,4,1,2),_RcftRemoteSHDSLPortIntervalDayLOSTimes_Type())
rcftRemoteSHDSLPortIntervalDayLOSTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteSHDSLPortIntervalDayLOSTimes.setStatus(_A)
_RcftRemoteSHDSLPortIntervalDayLOSWTimes_Type=Integer32
_RcftRemoteSHDSLPortIntervalDayLOSWTimes_Object=MibTableColumn
rcftRemoteSHDSLPortIntervalDayLOSWTimes=_RcftRemoteSHDSLPortIntervalDayLOSWTimes_Object((1,3,6,1,4,1,8886,2,1,6,4,2,4,1,3),_RcftRemoteSHDSLPortIntervalDayLOSWTimes_Type())
rcftRemoteSHDSLPortIntervalDayLOSWTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteSHDSLPortIntervalDayLOSWTimes.setStatus(_A)
_RcftRemoteSHDSLPortIntervalDayLOLKTimes_Type=Integer32
_RcftRemoteSHDSLPortIntervalDayLOLKTimes_Object=MibTableColumn
rcftRemoteSHDSLPortIntervalDayLOLKTimes=_RcftRemoteSHDSLPortIntervalDayLOLKTimes_Object((1,3,6,1,4,1,8886,2,1,6,4,2,4,1,4),_RcftRemoteSHDSLPortIntervalDayLOLKTimes_Type())
rcftRemoteSHDSLPortIntervalDayLOLKTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteSHDSLPortIntervalDayLOLKTimes.setStatus(_A)
_RcftRemoteSHDSLPortIntervalDayCVTimes_Type=Integer32
_RcftRemoteSHDSLPortIntervalDayCVTimes_Object=MibTableColumn
rcftRemoteSHDSLPortIntervalDayCVTimes=_RcftRemoteSHDSLPortIntervalDayCVTimes_Object((1,3,6,1,4,1,8886,2,1,6,4,2,4,1,5),_RcftRemoteSHDSLPortIntervalDayCVTimes_Type())
rcftRemoteSHDSLPortIntervalDayCVTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteSHDSLPortIntervalDayCVTimes.setStatus(_A)
_RcftRemoteSHDSLPortIntervalDayES_Type=Integer32
_RcftRemoteSHDSLPortIntervalDayES_Object=MibTableColumn
rcftRemoteSHDSLPortIntervalDayES=_RcftRemoteSHDSLPortIntervalDayES_Object((1,3,6,1,4,1,8886,2,1,6,4,2,4,1,6),_RcftRemoteSHDSLPortIntervalDayES_Type())
rcftRemoteSHDSLPortIntervalDayES.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteSHDSLPortIntervalDayES.setStatus(_A)
_RcftRemoteSHDSLPortIntervalDaySES_Type=Integer32
_RcftRemoteSHDSLPortIntervalDaySES_Object=MibTableColumn
rcftRemoteSHDSLPortIntervalDaySES=_RcftRemoteSHDSLPortIntervalDaySES_Object((1,3,6,1,4,1,8886,2,1,6,4,2,4,1,7),_RcftRemoteSHDSLPortIntervalDaySES_Type())
rcftRemoteSHDSLPortIntervalDaySES.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteSHDSLPortIntervalDaySES.setStatus(_A)
_RcftRemoteSHDSLPortIntervalDayUAS_Type=Integer32
_RcftRemoteSHDSLPortIntervalDayUAS_Object=MibTableColumn
rcftRemoteSHDSLPortIntervalDayUAS=_RcftRemoteSHDSLPortIntervalDayUAS_Object((1,3,6,1,4,1,8886,2,1,6,4,2,4,1,8),_RcftRemoteSHDSLPortIntervalDayUAS_Type())
rcftRemoteSHDSLPortIntervalDayUAS.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteSHDSLPortIntervalDayUAS.setStatus(_A)
_RcftRemoteSHDSLPortIntervalDayLOSWS_Type=Integer32
_RcftRemoteSHDSLPortIntervalDayLOSWS_Object=MibTableColumn
rcftRemoteSHDSLPortIntervalDayLOSWS=_RcftRemoteSHDSLPortIntervalDayLOSWS_Object((1,3,6,1,4,1,8886,2,1,6,4,2,4,1,9),_RcftRemoteSHDSLPortIntervalDayLOSWS_Type())
rcftRemoteSHDSLPortIntervalDayLOSWS.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteSHDSLPortIntervalDayLOSWS.setStatus(_A)
_RcftRemoteSHDSLPortIntervalDayCRCTimes_Type=Integer32
_RcftRemoteSHDSLPortIntervalDayCRCTimes_Object=MibTableColumn
rcftRemoteSHDSLPortIntervalDayCRCTimes=_RcftRemoteSHDSLPortIntervalDayCRCTimes_Object((1,3,6,1,4,1,8886,2,1,6,4,2,4,1,10),_RcftRemoteSHDSLPortIntervalDayCRCTimes_Type())
rcftRemoteSHDSLPortIntervalDayCRCTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteSHDSLPortIntervalDayCRCTimes.setStatus(_A)
_RcftRemoteSHDSLPortTraps_ObjectIdentity=ObjectIdentity
rcftRemoteSHDSLPortTraps=_RcftRemoteSHDSLPortTraps_ObjectIdentity((1,3,6,1,4,1,8886,2,1,6,4,10))
_RcftRemoteDeviceV35MIB_ObjectIdentity=ObjectIdentity
rcftRemoteDeviceV35MIB=_RcftRemoteDeviceV35MIB_ObjectIdentity((1,3,6,1,4,1,8886,2,1,6,5))
_RcftRemoteV35PortObjects_ObjectIdentity=ObjectIdentity
rcftRemoteV35PortObjects=_RcftRemoteV35PortObjects_ObjectIdentity((1,3,6,1,4,1,8886,2,1,6,5,1))
_RcftRemoteV35PortTable_Object=MibTable
rcftRemoteV35PortTable=_RcftRemoteV35PortTable_Object((1,3,6,1,4,1,8886,2,1,6,5,1,1))
if mibBuilder.loadTexts:rcftRemoteV35PortTable.setStatus(_A)
_RcftRemoteV35PortEntry_Object=MibTableRow
rcftRemoteV35PortEntry=_RcftRemoteV35PortEntry_Object((1,3,6,1,4,1,8886,2,1,6,5,1,1,1))
rcftRemoteV35PortEntry.setIndexNames((0,_F,_H),(0,_F,_I),(0,_C,_J),(0,_C,_AM))
if mibBuilder.loadTexts:rcftRemoteV35PortEntry.setStatus(_A)
_RcftRemoteV35PortIndex_Type=Integer32
_RcftRemoteV35PortIndex_Object=MibTableColumn
rcftRemoteV35PortIndex=_RcftRemoteV35PortIndex_Object((1,3,6,1,4,1,8886,2,1,6,5,1,1,1,1),_RcftRemoteV35PortIndex_Type())
rcftRemoteV35PortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteV35PortIndex.setStatus(_A)
_RcftRemoteV35PortAlarmStatus_Type=Integer32
_RcftRemoteV35PortAlarmStatus_Object=MibTableColumn
rcftRemoteV35PortAlarmStatus=_RcftRemoteV35PortAlarmStatus_Object((1,3,6,1,4,1,8886,2,1,6,5,1,1,1,2),_RcftRemoteV35PortAlarmStatus_Type())
rcftRemoteV35PortAlarmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteV35PortAlarmStatus.setStatus(_A)
_RcftRemoteV35PortStatus_Type=Integer32
_RcftRemoteV35PortStatus_Object=MibTableColumn
rcftRemoteV35PortStatus=_RcftRemoteV35PortStatus_Object((1,3,6,1,4,1,8886,2,1,6,5,1,1,1,3),_RcftRemoteV35PortStatus_Type())
rcftRemoteV35PortStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteV35PortStatus.setStatus(_A)
_RcftRemoteV35PortSpeed_Type=Integer32
_RcftRemoteV35PortSpeed_Object=MibTableColumn
rcftRemoteV35PortSpeed=_RcftRemoteV35PortSpeed_Object((1,3,6,1,4,1,8886,2,1,6,5,1,1,1,4),_RcftRemoteV35PortSpeed_Type())
rcftRemoteV35PortSpeed.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteV35PortSpeed.setStatus(_A)
_RcftRemoteV35PortOrderTimeParameter_Type=Integer32
_RcftRemoteV35PortOrderTimeParameter_Object=MibTableColumn
rcftRemoteV35PortOrderTimeParameter=_RcftRemoteV35PortOrderTimeParameter_Object((1,3,6,1,4,1,8886,2,1,6,5,1,1,1,5),_RcftRemoteV35PortOrderTimeParameter_Type())
rcftRemoteV35PortOrderTimeParameter.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteV35PortOrderTimeParameter.setStatus(_A)
_RcftRemoteV35PortOrderModeParameter_Type=Integer32
_RcftRemoteV35PortOrderModeParameter_Object=MibTableColumn
rcftRemoteV35PortOrderModeParameter=_RcftRemoteV35PortOrderModeParameter_Object((1,3,6,1,4,1,8886,2,1,6,5,1,1,1,6),_RcftRemoteV35PortOrderModeParameter_Type())
rcftRemoteV35PortOrderModeParameter.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteV35PortOrderModeParameter.setStatus(_A)
_RcftRemoteV35PortOrder_Type=Integer32
_RcftRemoteV35PortOrder_Object=MibTableColumn
rcftRemoteV35PortOrder=_RcftRemoteV35PortOrder_Object((1,3,6,1,4,1,8886,2,1,6,5,1,1,1,7),_RcftRemoteV35PortOrder_Type())
rcftRemoteV35PortOrder.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteV35PortOrder.setStatus(_A)
_RcftRemoteV35BertStatus_Type=Integer32
_RcftRemoteV35BertStatus_Object=MibTableColumn
rcftRemoteV35BertStatus=_RcftRemoteV35BertStatus_Object((1,3,6,1,4,1,8886,2,1,6,5,1,1,1,8),_RcftRemoteV35BertStatus_Type())
rcftRemoteV35BertStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteV35BertStatus.setStatus(_A)
_RcftRemoteV35BertTime_Type=Unsigned32
_RcftRemoteV35BertTime_Object=MibTableColumn
rcftRemoteV35BertTime=_RcftRemoteV35BertTime_Object((1,3,6,1,4,1,8886,2,1,6,5,1,1,1,9),_RcftRemoteV35BertTime_Type())
rcftRemoteV35BertTime.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteV35BertTime.setStatus(_A)
_RcftRemoteV35BertErrCode_Type=Unsigned32
_RcftRemoteV35BertErrCode_Object=MibTableColumn
rcftRemoteV35BertErrCode=_RcftRemoteV35BertErrCode_Object((1,3,6,1,4,1,8886,2,1,6,5,1,1,1,10),_RcftRemoteV35BertErrCode_Type())
rcftRemoteV35BertErrCode.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteV35BertErrCode.setStatus(_A)
_RcftRemoteV35BertUnusedTime_Type=Unsigned32
_RcftRemoteV35BertUnusedTime_Object=MibTableColumn
rcftRemoteV35BertUnusedTime=_RcftRemoteV35BertUnusedTime_Object((1,3,6,1,4,1,8886,2,1,6,5,1,1,1,11),_RcftRemoteV35BertUnusedTime_Type())
rcftRemoteV35BertUnusedTime.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteV35BertUnusedTime.setStatus(_A)
_RcftRemoteV35BertPortSpeed_Type=Unsigned32
_RcftRemoteV35BertPortSpeed_Object=MibTableColumn
rcftRemoteV35BertPortSpeed=_RcftRemoteV35BertPortSpeed_Object((1,3,6,1,4,1,8886,2,1,6,5,1,1,1,12),_RcftRemoteV35BertPortSpeed_Type())
rcftRemoteV35BertPortSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteV35BertPortSpeed.setStatus(_A)
_RcftRemoteV35BertCodeType_Type=Integer32
_RcftRemoteV35BertCodeType_Object=MibTableColumn
rcftRemoteV35BertCodeType=_RcftRemoteV35BertCodeType_Object((1,3,6,1,4,1,8886,2,1,6,5,1,1,1,13),_RcftRemoteV35BertCodeType_Type())
rcftRemoteV35BertCodeType.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteV35BertCodeType.setStatus(_A)
_RcftRemoteV35BertCodeNum_Type=Integer32
_RcftRemoteV35BertCodeNum_Object=MibTableColumn
rcftRemoteV35BertCodeNum=_RcftRemoteV35BertCodeNum_Object((1,3,6,1,4,1,8886,2,1,6,5,1,1,1,14),_RcftRemoteV35BertCodeNum_Type())
rcftRemoteV35BertCodeNum.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteV35BertCodeNum.setStatus(_A)
class _RcftRemoteV35LoopStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_l,1),(_m,2),(_n,3),(_o,4),(_U,5),(_AI,6),(_AJ,7)))
_RcftRemoteV35LoopStatus_Type.__name__=_E
_RcftRemoteV35LoopStatus_Object=MibTableColumn
rcftRemoteV35LoopStatus=_RcftRemoteV35LoopStatus_Object((1,3,6,1,4,1,8886,2,1,6,5,1,1,1,15),_RcftRemoteV35LoopStatus_Type())
rcftRemoteV35LoopStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteV35LoopStatus.setStatus(_A)
_RcftRemoteV35PortPerformance_ObjectIdentity=ObjectIdentity
rcftRemoteV35PortPerformance=_RcftRemoteV35PortPerformance_ObjectIdentity((1,3,6,1,4,1,8886,2,1,6,5,2))
_RcftRemoteV35PortTraps_ObjectIdentity=ObjectIdentity
rcftRemoteV35PortTraps=_RcftRemoteV35PortTraps_ObjectIdentity((1,3,6,1,4,1,8886,2,1,6,5,3))
_RcftRemoteDS3E3PortMIB_ObjectIdentity=ObjectIdentity
rcftRemoteDS3E3PortMIB=_RcftRemoteDS3E3PortMIB_ObjectIdentity((1,3,6,1,4,1,8886,2,1,6,6))
_RcftRemoteDS3E3PortObjects_ObjectIdentity=ObjectIdentity
rcftRemoteDS3E3PortObjects=_RcftRemoteDS3E3PortObjects_ObjectIdentity((1,3,6,1,4,1,8886,2,1,6,6,1))
_RcftRemoteDS3E3PortTable_Object=MibTable
rcftRemoteDS3E3PortTable=_RcftRemoteDS3E3PortTable_Object((1,3,6,1,4,1,8886,2,1,6,6,1,1))
if mibBuilder.loadTexts:rcftRemoteDS3E3PortTable.setStatus(_A)
_RcftRemoteDS3E3PortEntry_Object=MibTableRow
rcftRemoteDS3E3PortEntry=_RcftRemoteDS3E3PortEntry_Object((1,3,6,1,4,1,8886,2,1,6,6,1,1,1))
rcftRemoteDS3E3PortEntry.setIndexNames((0,_F,_H),(0,_F,_I),(0,_C,_J),(0,_C,_AN))
if mibBuilder.loadTexts:rcftRemoteDS3E3PortEntry.setStatus(_A)
_RcftRemoteDS3E3PortIndex_Type=Integer32
_RcftRemoteDS3E3PortIndex_Object=MibTableColumn
rcftRemoteDS3E3PortIndex=_RcftRemoteDS3E3PortIndex_Object((1,3,6,1,4,1,8886,2,1,6,6,1,1,1,1),_RcftRemoteDS3E3PortIndex_Type())
rcftRemoteDS3E3PortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteDS3E3PortIndex.setStatus(_A)
_RcftRemoteDS3E3PortAlarmStatus_Type=Integer32
_RcftRemoteDS3E3PortAlarmStatus_Object=MibTableColumn
rcftRemoteDS3E3PortAlarmStatus=_RcftRemoteDS3E3PortAlarmStatus_Object((1,3,6,1,4,1,8886,2,1,6,6,1,1,1,2),_RcftRemoteDS3E3PortAlarmStatus_Type())
rcftRemoteDS3E3PortAlarmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteDS3E3PortAlarmStatus.setStatus(_A)
_RcftRemoteDS3E3PortStatus_Type=Integer32
_RcftRemoteDS3E3PortStatus_Object=MibTableColumn
rcftRemoteDS3E3PortStatus=_RcftRemoteDS3E3PortStatus_Object((1,3,6,1,4,1,8886,2,1,6,6,1,1,1,3),_RcftRemoteDS3E3PortStatus_Type())
rcftRemoteDS3E3PortStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteDS3E3PortStatus.setStatus(_A)
_RcftRemoteDS3E3PortESCont_Type=Integer32
_RcftRemoteDS3E3PortESCont_Object=MibTableColumn
rcftRemoteDS3E3PortESCont=_RcftRemoteDS3E3PortESCont_Object((1,3,6,1,4,1,8886,2,1,6,6,1,1,1,4),_RcftRemoteDS3E3PortESCont_Type())
rcftRemoteDS3E3PortESCont.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteDS3E3PortESCont.setStatus(_A)
_RcftRemoteDS3E3PortBertStatus_Type=Integer32
_RcftRemoteDS3E3PortBertStatus_Object=MibTableColumn
rcftRemoteDS3E3PortBertStatus=_RcftRemoteDS3E3PortBertStatus_Object((1,3,6,1,4,1,8886,2,1,6,6,1,1,1,5),_RcftRemoteDS3E3PortBertStatus_Type())
rcftRemoteDS3E3PortBertStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteDS3E3PortBertStatus.setStatus(_A)
_RcftRemoteDS3E3PortFaultFass_Type=Integer32
_RcftRemoteDS3E3PortFaultFass_Object=MibTableColumn
rcftRemoteDS3E3PortFaultFass=_RcftRemoteDS3E3PortFaultFass_Object((1,3,6,1,4,1,8886,2,1,6,6,1,1,1,6),_RcftRemoteDS3E3PortFaultFass_Type())
rcftRemoteDS3E3PortFaultFass.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteDS3E3PortFaultFass.setStatus(_A)
_RcftRemoteDS3E3PortLoopStatus_Type=Integer32
_RcftRemoteDS3E3PortLoopStatus_Object=MibTableColumn
rcftRemoteDS3E3PortLoopStatus=_RcftRemoteDS3E3PortLoopStatus_Object((1,3,6,1,4,1,8886,2,1,6,6,1,1,1,7),_RcftRemoteDS3E3PortLoopStatus_Type())
rcftRemoteDS3E3PortLoopStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteDS3E3PortLoopStatus.setStatus(_A)
_RcftRemoteDS3E3PortOrder_Type=Integer32
_RcftRemoteDS3E3PortOrder_Object=MibTableColumn
rcftRemoteDS3E3PortOrder=_RcftRemoteDS3E3PortOrder_Object((1,3,6,1,4,1,8886,2,1,6,6,1,1,1,8),_RcftRemoteDS3E3PortOrder_Type())
rcftRemoteDS3E3PortOrder.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteDS3E3PortOrder.setStatus(_A)
_RcftRemoteDS3E3PortPerformance_ObjectIdentity=ObjectIdentity
rcftRemoteDS3E3PortPerformance=_RcftRemoteDS3E3PortPerformance_ObjectIdentity((1,3,6,1,4,1,8886,2,1,6,6,2))
_RcftRemoteDS3E3StatisticTable_Object=MibTable
rcftRemoteDS3E3StatisticTable=_RcftRemoteDS3E3StatisticTable_Object((1,3,6,1,4,1,8886,2,1,6,6,2,1))
if mibBuilder.loadTexts:rcftRemoteDS3E3StatisticTable.setStatus(_A)
_RcftRemoteDS3E3StatisticEntry_Object=MibTableRow
rcftRemoteDS3E3StatisticEntry=_RcftRemoteDS3E3StatisticEntry_Object((1,3,6,1,4,1,8886,2,1,6,6,2,1,1))
if mibBuilder.loadTexts:rcftRemoteDS3E3StatisticEntry.setStatus(_A)
_RcftRemoteDS3E3TxPackets_Type=Counter32
_RcftRemoteDS3E3TxPackets_Object=MibTableColumn
rcftRemoteDS3E3TxPackets=_RcftRemoteDS3E3TxPackets_Object((1,3,6,1,4,1,8886,2,1,6,6,2,1,1,1),_RcftRemoteDS3E3TxPackets_Type())
rcftRemoteDS3E3TxPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteDS3E3TxPackets.setStatus(_A)
_RcftRemoteDS3E3TxBytes_Type=Counter32
_RcftRemoteDS3E3TxBytes_Object=MibTableColumn
rcftRemoteDS3E3TxBytes=_RcftRemoteDS3E3TxBytes_Object((1,3,6,1,4,1,8886,2,1,6,6,2,1,1,2),_RcftRemoteDS3E3TxBytes_Type())
rcftRemoteDS3E3TxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteDS3E3TxBytes.setStatus(_A)
_RcftRemoteDS3E3TxFailurePackets_Type=Counter32
_RcftRemoteDS3E3TxFailurePackets_Object=MibTableColumn
rcftRemoteDS3E3TxFailurePackets=_RcftRemoteDS3E3TxFailurePackets_Object((1,3,6,1,4,1,8886,2,1,6,6,2,1,1,3),_RcftRemoteDS3E3TxFailurePackets_Type())
rcftRemoteDS3E3TxFailurePackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteDS3E3TxFailurePackets.setStatus(_A)
_RcftRemoteDS3E3RxPackets_Type=Counter32
_RcftRemoteDS3E3RxPackets_Object=MibTableColumn
rcftRemoteDS3E3RxPackets=_RcftRemoteDS3E3RxPackets_Object((1,3,6,1,4,1,8886,2,1,6,6,2,1,1,4),_RcftRemoteDS3E3RxPackets_Type())
rcftRemoteDS3E3RxPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteDS3E3RxPackets.setStatus(_A)
_RcftRemoteDS3E3RxBytes_Type=Counter32
_RcftRemoteDS3E3RxBytes_Object=MibTableColumn
rcftRemoteDS3E3RxBytes=_RcftRemoteDS3E3RxBytes_Object((1,3,6,1,4,1,8886,2,1,6,6,2,1,1,5),_RcftRemoteDS3E3RxBytes_Type())
rcftRemoteDS3E3RxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteDS3E3RxBytes.setStatus(_A)
_RcftRemoteDS3E3RxErrorPackets_Type=Counter32
_RcftRemoteDS3E3RxErrorPackets_Object=MibTableColumn
rcftRemoteDS3E3RxErrorPackets=_RcftRemoteDS3E3RxErrorPackets_Object((1,3,6,1,4,1,8886,2,1,6,6,2,1,1,6),_RcftRemoteDS3E3RxErrorPackets_Type())
rcftRemoteDS3E3RxErrorPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteDS3E3RxErrorPackets.setStatus(_A)
_RcftRemoteDS3E3FluxTimer_Type=Counter32
_RcftRemoteDS3E3FluxTimer_Object=MibTableColumn
rcftRemoteDS3E3FluxTimer=_RcftRemoteDS3E3FluxTimer_Object((1,3,6,1,4,1,8886,2,1,6,6,2,1,1,7),_RcftRemoteDS3E3FluxTimer_Type())
rcftRemoteDS3E3FluxTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteDS3E3FluxTimer.setStatus(_A)
_RcftRemoteDS3E3PortTraps_ObjectIdentity=ObjectIdentity
rcftRemoteDS3E3PortTraps=_RcftRemoteDS3E3PortTraps_ObjectIdentity((1,3,6,1,4,1,8886,2,1,6,6,10))
_RcftRemotePdhPortMIB_ObjectIdentity=ObjectIdentity
rcftRemotePdhPortMIB=_RcftRemotePdhPortMIB_ObjectIdentity((1,3,6,1,4,1,8886,2,1,6,7))
_RcftRemotePdhPortObjects_ObjectIdentity=ObjectIdentity
rcftRemotePdhPortObjects=_RcftRemotePdhPortObjects_ObjectIdentity((1,3,6,1,4,1,8886,2,1,6,7,1))
_RcftRemotePdhPortTable_Object=MibTable
rcftRemotePdhPortTable=_RcftRemotePdhPortTable_Object((1,3,6,1,4,1,8886,2,1,6,7,1,1))
if mibBuilder.loadTexts:rcftRemotePdhPortTable.setStatus(_A)
_RcftRemotePdhPortEntry_Object=MibTableRow
rcftRemotePdhPortEntry=_RcftRemotePdhPortEntry_Object((1,3,6,1,4,1,8886,2,1,6,7,1,1,1))
rcftRemotePdhPortEntry.setIndexNames((0,_F,_H),(0,_F,_I),(0,_C,_J),(0,_C,_AO))
if mibBuilder.loadTexts:rcftRemotePdhPortEntry.setStatus(_A)
_RcftRemotePdhPortIndex_Type=Integer32
_RcftRemotePdhPortIndex_Object=MibTableColumn
rcftRemotePdhPortIndex=_RcftRemotePdhPortIndex_Object((1,3,6,1,4,1,8886,2,1,6,7,1,1,1,1),_RcftRemotePdhPortIndex_Type())
rcftRemotePdhPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemotePdhPortIndex.setStatus(_A)
class _RcftRemotePdhPortModuleType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,12,15,23,50,51,52,53,100)));namedValues=NamedValues(*((_A2,1),(_A3,2),(_A4,3),(_A5,4),(_A6,5),(_A7,6),(_A8,7),(_A9,8),(_AA,9),(_AB,10),(_AC,12),(_AD,15),('optical-SS24',23),('optical-S1FC',50),('optical-S1A',51),('optical-S2A',52),('optical-S3A',53),(_AE,100)))
_RcftRemotePdhPortModuleType_Type.__name__=_E
_RcftRemotePdhPortModuleType_Object=MibTableColumn
rcftRemotePdhPortModuleType=_RcftRemotePdhPortModuleType_Object((1,3,6,1,4,1,8886,2,1,6,7,1,1,1,2),_RcftRemotePdhPortModuleType_Type())
rcftRemotePdhPortModuleType.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemotePdhPortModuleType.setStatus(_A)
_RcftRemotePdhPortAlarmStatus_Type=Integer32
_RcftRemotePdhPortAlarmStatus_Object=MibTableColumn
rcftRemotePdhPortAlarmStatus=_RcftRemotePdhPortAlarmStatus_Object((1,3,6,1,4,1,8886,2,1,6,7,1,1,1,3),_RcftRemotePdhPortAlarmStatus_Type())
rcftRemotePdhPortAlarmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemotePdhPortAlarmStatus.setStatus(_A)
_RcftRemotePdhPortStatus_Type=Integer32
_RcftRemotePdhPortStatus_Object=MibTableColumn
rcftRemotePdhPortStatus=_RcftRemotePdhPortStatus_Object((1,3,6,1,4,1,8886,2,1,6,7,1,1,1,4),_RcftRemotePdhPortStatus_Type())
rcftRemotePdhPortStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemotePdhPortStatus.setStatus(_A)
_RcftRemotePdhPortECSCnt_Type=Integer32
_RcftRemotePdhPortECSCnt_Object=MibTableColumn
rcftRemotePdhPortECSCnt=_RcftRemotePdhPortECSCnt_Object((1,3,6,1,4,1,8886,2,1,6,7,1,1,1,5),_RcftRemotePdhPortECSCnt_Type())
rcftRemotePdhPortECSCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemotePdhPortECSCnt.setStatus(_A)
_RcftRemotePdhPortSECSCnt_Type=Integer32
_RcftRemotePdhPortSECSCnt_Object=MibTableColumn
rcftRemotePdhPortSECSCnt=_RcftRemotePdhPortSECSCnt_Object((1,3,6,1,4,1,8886,2,1,6,7,1,1,1,6),_RcftRemotePdhPortSECSCnt_Type())
rcftRemotePdhPortSECSCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemotePdhPortSECSCnt.setStatus(_A)
_RcftRemotePdhPortLoopStatus_Type=Integer32
_RcftRemotePdhPortLoopStatus_Object=MibTableColumn
rcftRemotePdhPortLoopStatus=_RcftRemotePdhPortLoopStatus_Object((1,3,6,1,4,1,8886,2,1,6,7,1,1,1,7),_RcftRemotePdhPortLoopStatus_Type())
rcftRemotePdhPortLoopStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemotePdhPortLoopStatus.setStatus(_A)
_RcftRemotePdhPortOrder_Type=Integer32
_RcftRemotePdhPortOrder_Object=MibTableColumn
rcftRemotePdhPortOrder=_RcftRemotePdhPortOrder_Object((1,3,6,1,4,1,8886,2,1,6,7,1,1,1,8),_RcftRemotePdhPortOrder_Type())
rcftRemotePdhPortOrder.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemotePdhPortOrder.setStatus(_A)
_RcftRemotePdhPortBertStatus_Type=Integer32
_RcftRemotePdhPortBertStatus_Object=MibTableColumn
rcftRemotePdhPortBertStatus=_RcftRemotePdhPortBertStatus_Object((1,3,6,1,4,1,8886,2,1,6,7,1,1,1,9),_RcftRemotePdhPortBertStatus_Type())
rcftRemotePdhPortBertStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemotePdhPortBertStatus.setStatus(_A)
_RcftRemotePdhPortBertErrCode_Type=Unsigned32
_RcftRemotePdhPortBertErrCode_Object=MibTableColumn
rcftRemotePdhPortBertErrCode=_RcftRemotePdhPortBertErrCode_Object((1,3,6,1,4,1,8886,2,1,6,7,1,1,1,10),_RcftRemotePdhPortBertErrCode_Type())
rcftRemotePdhPortBertErrCode.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemotePdhPortBertErrCode.setStatus(_A)
_RcftRemotePdhPortPerformance_ObjectIdentity=ObjectIdentity
rcftRemotePdhPortPerformance=_RcftRemotePdhPortPerformance_ObjectIdentity((1,3,6,1,4,1,8886,2,1,6,7,2))
_RcftRemotePdhPortTraps_ObjectIdentity=ObjectIdentity
rcftRemotePdhPortTraps=_RcftRemotePdhPortTraps_ObjectIdentity((1,3,6,1,4,1,8886,2,1,6,7,10))
_RcftRemoteDS1PortMIB_ObjectIdentity=ObjectIdentity
rcftRemoteDS1PortMIB=_RcftRemoteDS1PortMIB_ObjectIdentity((1,3,6,1,4,1,8886,2,1,6,8))
_RcftRemoteDS1PortObjects_ObjectIdentity=ObjectIdentity
rcftRemoteDS1PortObjects=_RcftRemoteDS1PortObjects_ObjectIdentity((1,3,6,1,4,1,8886,2,1,6,8,1))
_RcftRemoteDS1PortTable_Object=MibTable
rcftRemoteDS1PortTable=_RcftRemoteDS1PortTable_Object((1,3,6,1,4,1,8886,2,1,6,8,1,1))
if mibBuilder.loadTexts:rcftRemoteDS1PortTable.setStatus(_A)
_RcftRemoteDS1PortEntry_Object=MibTableRow
rcftRemoteDS1PortEntry=_RcftRemoteDS1PortEntry_Object((1,3,6,1,4,1,8886,2,1,6,8,1,1,1))
rcftRemoteDS1PortEntry.setIndexNames((0,_F,_H),(0,_F,_I),(0,_C,_J),(0,_C,_AP))
if mibBuilder.loadTexts:rcftRemoteDS1PortEntry.setStatus(_A)
_RcftRemoteDS1PortIndex_Type=Integer32
_RcftRemoteDS1PortIndex_Object=MibTableColumn
rcftRemoteDS1PortIndex=_RcftRemoteDS1PortIndex_Object((1,3,6,1,4,1,8886,2,1,6,8,1,1,1,1),_RcftRemoteDS1PortIndex_Type())
rcftRemoteDS1PortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteDS1PortIndex.setStatus(_A)
_RcftRemoteDS1PortAlarmStatus_Type=Integer32
_RcftRemoteDS1PortAlarmStatus_Object=MibTableColumn
rcftRemoteDS1PortAlarmStatus=_RcftRemoteDS1PortAlarmStatus_Object((1,3,6,1,4,1,8886,2,1,6,8,1,1,1,2),_RcftRemoteDS1PortAlarmStatus_Type())
rcftRemoteDS1PortAlarmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteDS1PortAlarmStatus.setStatus(_A)
_RcftRemoteDS1PortStatus_Type=Integer32
_RcftRemoteDS1PortStatus_Object=MibTableColumn
rcftRemoteDS1PortStatus=_RcftRemoteDS1PortStatus_Object((1,3,6,1,4,1,8886,2,1,6,8,1,1,1,3),_RcftRemoteDS1PortStatus_Type())
rcftRemoteDS1PortStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteDS1PortStatus.setStatus(_A)
_RcftRemoteDS1PortESCont_Type=Integer32
_RcftRemoteDS1PortESCont_Object=MibTableColumn
rcftRemoteDS1PortESCont=_RcftRemoteDS1PortESCont_Object((1,3,6,1,4,1,8886,2,1,6,8,1,1,1,4),_RcftRemoteDS1PortESCont_Type())
rcftRemoteDS1PortESCont.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteDS1PortESCont.setStatus(_A)
_RcftRemoteDS1PortSESCont_Type=Integer32
_RcftRemoteDS1PortSESCont_Object=MibTableColumn
rcftRemoteDS1PortSESCont=_RcftRemoteDS1PortSESCont_Object((1,3,6,1,4,1,8886,2,1,6,8,1,1,1,5),_RcftRemoteDS1PortSESCont_Type())
rcftRemoteDS1PortSESCont.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteDS1PortSESCont.setStatus(_A)
_RcftRemoteDS1PortBertStatus_Type=Integer32
_RcftRemoteDS1PortBertStatus_Object=MibTableColumn
rcftRemoteDS1PortBertStatus=_RcftRemoteDS1PortBertStatus_Object((1,3,6,1,4,1,8886,2,1,6,8,1,1,1,6),_RcftRemoteDS1PortBertStatus_Type())
rcftRemoteDS1PortBertStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteDS1PortBertStatus.setStatus(_A)
_RcftRemoteDS1PortFaultPass_Type=Integer32
_RcftRemoteDS1PortFaultPass_Object=MibTableColumn
rcftRemoteDS1PortFaultPass=_RcftRemoteDS1PortFaultPass_Object((1,3,6,1,4,1,8886,2,1,6,8,1,1,1,7),_RcftRemoteDS1PortFaultPass_Type())
rcftRemoteDS1PortFaultPass.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteDS1PortFaultPass.setStatus(_A)
_RcftRemoteDS1PortLoopStatus_Type=Integer32
_RcftRemoteDS1PortLoopStatus_Object=MibTableColumn
rcftRemoteDS1PortLoopStatus=_RcftRemoteDS1PortLoopStatus_Object((1,3,6,1,4,1,8886,2,1,6,8,1,1,1,8),_RcftRemoteDS1PortLoopStatus_Type())
rcftRemoteDS1PortLoopStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteDS1PortLoopStatus.setStatus(_A)
_RcftRemoteDS1PortOrder_Type=Integer32
_RcftRemoteDS1PortOrder_Object=MibTableColumn
rcftRemoteDS1PortOrder=_RcftRemoteDS1PortOrder_Object((1,3,6,1,4,1,8886,2,1,6,8,1,1,1,9),_RcftRemoteDS1PortOrder_Type())
rcftRemoteDS1PortOrder.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteDS1PortOrder.setStatus(_A)
_RcftRemoteDS1PortTranLength_Type=Integer32
_RcftRemoteDS1PortTranLength_Object=MibTableColumn
rcftRemoteDS1PortTranLength=_RcftRemoteDS1PortTranLength_Object((1,3,6,1,4,1,8886,2,1,6,8,1,1,1,10),_RcftRemoteDS1PortTranLength_Type())
rcftRemoteDS1PortTranLength.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteDS1PortTranLength.setStatus(_A)
_RcftRemoteDS1PortFaultPassIndicator_Type=Integer32
_RcftRemoteDS1PortFaultPassIndicator_Object=MibTableColumn
rcftRemoteDS1PortFaultPassIndicator=_RcftRemoteDS1PortFaultPassIndicator_Object((1,3,6,1,4,1,8886,2,1,6,8,1,1,1,11),_RcftRemoteDS1PortFaultPassIndicator_Type())
rcftRemoteDS1PortFaultPassIndicator.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteDS1PortFaultPassIndicator.setStatus(_A)
_RcftRemoteDS1PortframeType_Type=Integer32
_RcftRemoteDS1PortframeType_Object=MibTableColumn
rcftRemoteDS1PortframeType=_RcftRemoteDS1PortframeType_Object((1,3,6,1,4,1,8886,2,1,6,8,1,1,1,12),_RcftRemoteDS1PortframeType_Type())
rcftRemoteDS1PortframeType.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteDS1PortframeType.setStatus(_A)
_RcftRemoteDS1PortChannel_Type=Integer32
_RcftRemoteDS1PortChannel_Object=MibTableColumn
rcftRemoteDS1PortChannel=_RcftRemoteDS1PortChannel_Object((1,3,6,1,4,1,8886,2,1,6,8,1,1,1,13),_RcftRemoteDS1PortChannel_Type())
rcftRemoteDS1PortChannel.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteDS1PortChannel.setStatus(_A)
_RcftRemoteDS1PortPerformance_ObjectIdentity=ObjectIdentity
rcftRemoteDS1PortPerformance=_RcftRemoteDS1PortPerformance_ObjectIdentity((1,3,6,1,4,1,8886,2,1,6,8,2))
_RcftRemoteDS1StatisticTable_Object=MibTable
rcftRemoteDS1StatisticTable=_RcftRemoteDS1StatisticTable_Object((1,3,6,1,4,1,8886,2,1,6,8,2,1))
if mibBuilder.loadTexts:rcftRemoteDS1StatisticTable.setStatus(_A)
_RcftRemoteDS1StatisticEntry_Object=MibTableRow
rcftRemoteDS1StatisticEntry=_RcftRemoteDS1StatisticEntry_Object((1,3,6,1,4,1,8886,2,1,6,8,2,1,1))
if mibBuilder.loadTexts:rcftRemoteDS1StatisticEntry.setStatus(_A)
_RcftRemoteDS1TxPackets_Type=Counter32
_RcftRemoteDS1TxPackets_Object=MibTableColumn
rcftRemoteDS1TxPackets=_RcftRemoteDS1TxPackets_Object((1,3,6,1,4,1,8886,2,1,6,8,2,1,1,1),_RcftRemoteDS1TxPackets_Type())
rcftRemoteDS1TxPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteDS1TxPackets.setStatus(_A)
_RcftRemoteDS1TxBytes_Type=Counter32
_RcftRemoteDS1TxBytes_Object=MibTableColumn
rcftRemoteDS1TxBytes=_RcftRemoteDS1TxBytes_Object((1,3,6,1,4,1,8886,2,1,6,8,2,1,1,2),_RcftRemoteDS1TxBytes_Type())
rcftRemoteDS1TxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteDS1TxBytes.setStatus(_A)
_RcftRemoteDS1TxFailurePackets_Type=Counter32
_RcftRemoteDS1TxFailurePackets_Object=MibTableColumn
rcftRemoteDS1TxFailurePackets=_RcftRemoteDS1TxFailurePackets_Object((1,3,6,1,4,1,8886,2,1,6,8,2,1,1,3),_RcftRemoteDS1TxFailurePackets_Type())
rcftRemoteDS1TxFailurePackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteDS1TxFailurePackets.setStatus(_A)
_RcftRemoteDS1RxPackets_Type=Counter32
_RcftRemoteDS1RxPackets_Object=MibTableColumn
rcftRemoteDS1RxPackets=_RcftRemoteDS1RxPackets_Object((1,3,6,1,4,1,8886,2,1,6,8,2,1,1,4),_RcftRemoteDS1RxPackets_Type())
rcftRemoteDS1RxPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteDS1RxPackets.setStatus(_A)
_RcftRemoteDS1RxBytes_Type=Counter32
_RcftRemoteDS1RxBytes_Object=MibTableColumn
rcftRemoteDS1RxBytes=_RcftRemoteDS1RxBytes_Object((1,3,6,1,4,1,8886,2,1,6,8,2,1,1,5),_RcftRemoteDS1RxBytes_Type())
rcftRemoteDS1RxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteDS1RxBytes.setStatus(_A)
_RcftRemoteDS1RxErrorPackets_Type=Counter32
_RcftRemoteDS1RxErrorPackets_Object=MibTableColumn
rcftRemoteDS1RxErrorPackets=_RcftRemoteDS1RxErrorPackets_Object((1,3,6,1,4,1,8886,2,1,6,8,2,1,1,6),_RcftRemoteDS1RxErrorPackets_Type())
rcftRemoteDS1RxErrorPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteDS1RxErrorPackets.setStatus(_A)
_RcftRemoteDS1FluxTimer_Type=Counter32
_RcftRemoteDS1FluxTimer_Object=MibTableColumn
rcftRemoteDS1FluxTimer=_RcftRemoteDS1FluxTimer_Object((1,3,6,1,4,1,8886,2,1,6,8,2,1,1,7),_RcftRemoteDS1FluxTimer_Type())
rcftRemoteDS1FluxTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteDS1FluxTimer.setStatus(_A)
_RcftRemoteDS1PortTraps_ObjectIdentity=ObjectIdentity
rcftRemoteDS1PortTraps=_RcftRemoteDS1PortTraps_ObjectIdentity((1,3,6,1,4,1,8886,2,1,6,8,10))
_RcftRemoteMoudleMIB_ObjectIdentity=ObjectIdentity
rcftRemoteMoudleMIB=_RcftRemoteMoudleMIB_ObjectIdentity((1,3,6,1,4,1,8886,2,1,6,9))
_RcftRemoteMoudle_ObjectIdentity=ObjectIdentity
rcftRemoteMoudle=_RcftRemoteMoudle_ObjectIdentity((1,3,6,1,4,1,8886,2,1,6,9,1))
_RcftRemoteMoudleObjects_ObjectIdentity=ObjectIdentity
rcftRemoteMoudleObjects=_RcftRemoteMoudleObjects_ObjectIdentity((1,3,6,1,4,1,8886,2,1,6,9,1,1))
_RcftRemoteMoudleTable_Object=MibTable
rcftRemoteMoudleTable=_RcftRemoteMoudleTable_Object((1,3,6,1,4,1,8886,2,1,6,9,1,1,1))
if mibBuilder.loadTexts:rcftRemoteMoudleTable.setStatus(_A)
_RcftRemoteMoudleEntry_Object=MibTableRow
rcftRemoteMoudleEntry=_RcftRemoteMoudleEntry_Object((1,3,6,1,4,1,8886,2,1,6,9,1,1,1,1))
rcftRemoteMoudleEntry.setIndexNames((0,_F,_H),(0,_F,_I),(0,_C,_J),(0,_C,_W))
if mibBuilder.loadTexts:rcftRemoteMoudleEntry.setStatus(_A)
_RcftRemoteMoudleIndex_Type=Integer32
_RcftRemoteMoudleIndex_Object=MibTableColumn
rcftRemoteMoudleIndex=_RcftRemoteMoudleIndex_Object((1,3,6,1,4,1,8886,2,1,6,9,1,1,1,1,1),_RcftRemoteMoudleIndex_Type())
rcftRemoteMoudleIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteMoudleIndex.setStatus(_A)
class _RcftRemoteMoudleExist_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_g,1),('notExist',2)))
_RcftRemoteMoudleExist_Type.__name__=_E
_RcftRemoteMoudleExist_Object=MibTableColumn
rcftRemoteMoudleExist=_RcftRemoteMoudleExist_Object((1,3,6,1,4,1,8886,2,1,6,9,1,1,1,1,2),_RcftRemoteMoudleExist_Type())
rcftRemoteMoudleExist.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteMoudleExist.setStatus(_A)
class _RcftRemoteMoudleType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(6402,6422,6423,6424,6425,6427,6428)));namedValues=NamedValues(*(('e-SUBM-2E1-A',6402),('e-SUBM-2FV35-A',6422),('e-SUBM-2FE-A',6423),('e-SUBM-FE4E1-A',6424),('e-SUBM-FV35-A',6425),('e-SUBM-FV35-B',6427),('e-SUBM-2FV35-B',6428)))
_RcftRemoteMoudleType_Type.__name__=_E
_RcftRemoteMoudleType_Object=MibTableColumn
rcftRemoteMoudleType=_RcftRemoteMoudleType_Object((1,3,6,1,4,1,8886,2,1,6,9,1,1,1,1,3),_RcftRemoteMoudleType_Type())
rcftRemoteMoudleType.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteMoudleType.setStatus(_A)
_RcftRemoteMoudleStatus_Type=Integer32
_RcftRemoteMoudleStatus_Object=MibTableColumn
rcftRemoteMoudleStatus=_RcftRemoteMoudleStatus_Object((1,3,6,1,4,1,8886,2,1,6,9,1,1,1,1,4),_RcftRemoteMoudleStatus_Type())
rcftRemoteMoudleStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteMoudleStatus.setStatus(_A)
class _RcftRemoteMoudleSigleChipDescr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_RcftRemoteMoudleSigleChipDescr_Type.__name__=_G
_RcftRemoteMoudleSigleChipDescr_Object=MibTableColumn
rcftRemoteMoudleSigleChipDescr=_RcftRemoteMoudleSigleChipDescr_Object((1,3,6,1,4,1,8886,2,1,6,9,1,1,1,1,5),_RcftRemoteMoudleSigleChipDescr_Type())
rcftRemoteMoudleSigleChipDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteMoudleSigleChipDescr.setStatus(_A)
class _RcftRemoteMoudleHardWareDescr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_RcftRemoteMoudleHardWareDescr_Type.__name__=_G
_RcftRemoteMoudleHardWareDescr_Object=MibTableColumn
rcftRemoteMoudleHardWareDescr=_RcftRemoteMoudleHardWareDescr_Object((1,3,6,1,4,1,8886,2,1,6,9,1,1,1,1,6),_RcftRemoteMoudleHardWareDescr_Type())
rcftRemoteMoudleHardWareDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteMoudleHardWareDescr.setStatus(_A)
class _RcftRemoteMoudleFPGADescr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_RcftRemoteMoudleFPGADescr_Type.__name__=_G
_RcftRemoteMoudleFPGADescr_Object=MibTableColumn
rcftRemoteMoudleFPGADescr=_RcftRemoteMoudleFPGADescr_Object((1,3,6,1,4,1,8886,2,1,6,9,1,1,1,1,7),_RcftRemoteMoudleFPGADescr_Type())
rcftRemoteMoudleFPGADescr.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteMoudleFPGADescr.setStatus(_A)
_RcftRemoteMoudleOrder_Type=Integer32
_RcftRemoteMoudleOrder_Object=MibTableColumn
rcftRemoteMoudleOrder=_RcftRemoteMoudleOrder_Object((1,3,6,1,4,1,8886,2,1,6,9,1,1,1,1,8),_RcftRemoteMoudleOrder_Type())
rcftRemoteMoudleOrder.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteMoudleOrder.setStatus(_A)
class _RcftRemoteMoudleIFOrder_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_RcftRemoteMoudleIFOrder_Type.__name__=_G
_RcftRemoteMoudleIFOrder_Object=MibTableColumn
rcftRemoteMoudleIFOrder=_RcftRemoteMoudleIFOrder_Object((1,3,6,1,4,1,8886,2,1,6,9,1,1,1,1,9),_RcftRemoteMoudleIFOrder_Type())
rcftRemoteMoudleIFOrder.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteMoudleIFOrder.setStatus(_A)
_RcftRemoteMoudleTraps_ObjectIdentity=ObjectIdentity
rcftRemoteMoudleTraps=_RcftRemoteMoudleTraps_ObjectIdentity((1,3,6,1,4,1,8886,2,1,6,9,1,10))
_RcftRemoteMoudleEthFe_ObjectIdentity=ObjectIdentity
rcftRemoteMoudleEthFe=_RcftRemoteMoudleEthFe_ObjectIdentity((1,3,6,1,4,1,8886,2,1,6,9,2))
_RcftRemoteMoudleEthFeObjects_ObjectIdentity=ObjectIdentity
rcftRemoteMoudleEthFeObjects=_RcftRemoteMoudleEthFeObjects_ObjectIdentity((1,3,6,1,4,1,8886,2,1,6,9,2,1))
_RcftRemoteMoudleEthFeTable_Object=MibTable
rcftRemoteMoudleEthFeTable=_RcftRemoteMoudleEthFeTable_Object((1,3,6,1,4,1,8886,2,1,6,9,2,1,1))
if mibBuilder.loadTexts:rcftRemoteMoudleEthFeTable.setStatus(_A)
_RcftRemoteMoudleEthFeEntry_Object=MibTableRow
rcftRemoteMoudleEthFeEntry=_RcftRemoteMoudleEthFeEntry_Object((1,3,6,1,4,1,8886,2,1,6,9,2,1,1,1))
rcftRemoteMoudleEthFeEntry.setIndexNames((0,_F,_H),(0,_F,_I),(0,_C,_J),(0,_C,_W),(0,_C,_AQ))
if mibBuilder.loadTexts:rcftRemoteMoudleEthFeEntry.setStatus(_A)
_RcftRemoteMoudleEthFeIndex_Type=Integer32
_RcftRemoteMoudleEthFeIndex_Object=MibTableColumn
rcftRemoteMoudleEthFeIndex=_RcftRemoteMoudleEthFeIndex_Object((1,3,6,1,4,1,8886,2,1,6,9,2,1,1,1,1),_RcftRemoteMoudleEthFeIndex_Type())
rcftRemoteMoudleEthFeIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteMoudleEthFeIndex.setStatus(_A)
_RcftRemoteMoudleEthFeStatus_Type=Integer32
_RcftRemoteMoudleEthFeStatus_Object=MibTableColumn
rcftRemoteMoudleEthFeStatus=_RcftRemoteMoudleEthFeStatus_Object((1,3,6,1,4,1,8886,2,1,6,9,2,1,1,1,2),_RcftRemoteMoudleEthFeStatus_Type())
rcftRemoteMoudleEthFeStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteMoudleEthFeStatus.setStatus(_A)
_RcftRemoteMoudleEthFeRxRestrictSpeed_Type=Integer32
_RcftRemoteMoudleEthFeRxRestrictSpeed_Object=MibTableColumn
rcftRemoteMoudleEthFeRxRestrictSpeed=_RcftRemoteMoudleEthFeRxRestrictSpeed_Object((1,3,6,1,4,1,8886,2,1,6,9,2,1,1,1,3),_RcftRemoteMoudleEthFeRxRestrictSpeed_Type())
rcftRemoteMoudleEthFeRxRestrictSpeed.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteMoudleEthFeRxRestrictSpeed.setStatus(_A)
_RcftRemoteMoudleEthFeTxRestrictSpeed_Type=Integer32
_RcftRemoteMoudleEthFeTxRestrictSpeed_Object=MibTableColumn
rcftRemoteMoudleEthFeTxRestrictSpeed=_RcftRemoteMoudleEthFeTxRestrictSpeed_Object((1,3,6,1,4,1,8886,2,1,6,9,2,1,1,1,4),_RcftRemoteMoudleEthFeTxRestrictSpeed_Type())
rcftRemoteMoudleEthFeTxRestrictSpeed.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteMoudleEthFeTxRestrictSpeed.setStatus(_A)
_RcftRemoteMoudleEthFeRestrictSpeedStep_Type=Integer32
_RcftRemoteMoudleEthFeRestrictSpeedStep_Object=MibTableColumn
rcftRemoteMoudleEthFeRestrictSpeedStep=_RcftRemoteMoudleEthFeRestrictSpeedStep_Object((1,3,6,1,4,1,8886,2,1,6,9,2,1,1,1,5),_RcftRemoteMoudleEthFeRestrictSpeedStep_Type())
rcftRemoteMoudleEthFeRestrictSpeedStep.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteMoudleEthFeRestrictSpeedStep.setStatus(_A)
_RcftRemoteMoudleEthFeAlarmStatus_Type=Integer32
_RcftRemoteMoudleEthFeAlarmStatus_Object=MibTableColumn
rcftRemoteMoudleEthFeAlarmStatus=_RcftRemoteMoudleEthFeAlarmStatus_Object((1,3,6,1,4,1,8886,2,1,6,9,2,1,1,1,6),_RcftRemoteMoudleEthFeAlarmStatus_Type())
rcftRemoteMoudleEthFeAlarmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteMoudleEthFeAlarmStatus.setStatus(_A)
_RcftRemoteMoudleEthFePerformance_ObjectIdentity=ObjectIdentity
rcftRemoteMoudleEthFePerformance=_RcftRemoteMoudleEthFePerformance_ObjectIdentity((1,3,6,1,4,1,8886,2,1,6,9,2,2))
_RcftRemoteMoudleEthFeStatisticTable_Object=MibTable
rcftRemoteMoudleEthFeStatisticTable=_RcftRemoteMoudleEthFeStatisticTable_Object((1,3,6,1,4,1,8886,2,1,6,9,2,2,1))
if mibBuilder.loadTexts:rcftRemoteMoudleEthFeStatisticTable.setStatus(_A)
_RcftRemoteMoudleEthFeStatisticEntry_Object=MibTableRow
rcftRemoteMoudleEthFeStatisticEntry=_RcftRemoteMoudleEthFeStatisticEntry_Object((1,3,6,1,4,1,8886,2,1,6,9,2,2,1,1))
if mibBuilder.loadTexts:rcftRemoteMoudleEthFeStatisticEntry.setStatus(_A)
_RcftRemoteMoudleEthFeTxPackets_Type=Counter32
_RcftRemoteMoudleEthFeTxPackets_Object=MibTableColumn
rcftRemoteMoudleEthFeTxPackets=_RcftRemoteMoudleEthFeTxPackets_Object((1,3,6,1,4,1,8886,2,1,6,9,2,2,1,1,1),_RcftRemoteMoudleEthFeTxPackets_Type())
rcftRemoteMoudleEthFeTxPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteMoudleEthFeTxPackets.setStatus(_A)
_RcftRemoteMoudleEthFeTxBytes_Type=Counter32
_RcftRemoteMoudleEthFeTxBytes_Object=MibTableColumn
rcftRemoteMoudleEthFeTxBytes=_RcftRemoteMoudleEthFeTxBytes_Object((1,3,6,1,4,1,8886,2,1,6,9,2,2,1,1,2),_RcftRemoteMoudleEthFeTxBytes_Type())
rcftRemoteMoudleEthFeTxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteMoudleEthFeTxBytes.setStatus(_A)
_RcftRemoteMoudleEthFeTxFailurePackets_Type=Counter32
_RcftRemoteMoudleEthFeTxFailurePackets_Object=MibTableColumn
rcftRemoteMoudleEthFeTxFailurePackets=_RcftRemoteMoudleEthFeTxFailurePackets_Object((1,3,6,1,4,1,8886,2,1,6,9,2,2,1,1,3),_RcftRemoteMoudleEthFeTxFailurePackets_Type())
rcftRemoteMoudleEthFeTxFailurePackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteMoudleEthFeTxFailurePackets.setStatus(_A)
_RcftRemoteMoudleEthFeRxPackets_Type=Counter32
_RcftRemoteMoudleEthFeRxPackets_Object=MibTableColumn
rcftRemoteMoudleEthFeRxPackets=_RcftRemoteMoudleEthFeRxPackets_Object((1,3,6,1,4,1,8886,2,1,6,9,2,2,1,1,4),_RcftRemoteMoudleEthFeRxPackets_Type())
rcftRemoteMoudleEthFeRxPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteMoudleEthFeRxPackets.setStatus(_A)
_RcftRemoteMoudleEthFeRxBytes_Type=Counter32
_RcftRemoteMoudleEthFeRxBytes_Object=MibTableColumn
rcftRemoteMoudleEthFeRxBytes=_RcftRemoteMoudleEthFeRxBytes_Object((1,3,6,1,4,1,8886,2,1,6,9,2,2,1,1,5),_RcftRemoteMoudleEthFeRxBytes_Type())
rcftRemoteMoudleEthFeRxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteMoudleEthFeRxBytes.setStatus(_A)
_RcftRemoteMoudleEthFeRxErrorPackets_Type=Counter32
_RcftRemoteMoudleEthFeRxErrorPackets_Object=MibTableColumn
rcftRemoteMoudleEthFeRxErrorPackets=_RcftRemoteMoudleEthFeRxErrorPackets_Object((1,3,6,1,4,1,8886,2,1,6,9,2,2,1,1,6),_RcftRemoteMoudleEthFeRxErrorPackets_Type())
rcftRemoteMoudleEthFeRxErrorPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteMoudleEthFeRxErrorPackets.setStatus(_A)
_RcftRemoteMoudleEthFeFluxTimer_Type=Counter32
_RcftRemoteMoudleEthFeFluxTimer_Object=MibTableColumn
rcftRemoteMoudleEthFeFluxTimer=_RcftRemoteMoudleEthFeFluxTimer_Object((1,3,6,1,4,1,8886,2,1,6,9,2,2,1,1,7),_RcftRemoteMoudleEthFeFluxTimer_Type())
rcftRemoteMoudleEthFeFluxTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteMoudleEthFeFluxTimer.setStatus(_A)
_RcftRemoteMoudleEthFeTraps_ObjectIdentity=ObjectIdentity
rcftRemoteMoudleEthFeTraps=_RcftRemoteMoudleEthFeTraps_ObjectIdentity((1,3,6,1,4,1,8886,2,1,6,9,2,10))
_RcftRemoteMoudlePdh_ObjectIdentity=ObjectIdentity
rcftRemoteMoudlePdh=_RcftRemoteMoudlePdh_ObjectIdentity((1,3,6,1,4,1,8886,2,1,6,9,3))
_RcftRemoteMoudlePdhObjects_ObjectIdentity=ObjectIdentity
rcftRemoteMoudlePdhObjects=_RcftRemoteMoudlePdhObjects_ObjectIdentity((1,3,6,1,4,1,8886,2,1,6,9,3,1))
_RcftRemoteMoudlePdhTable_Object=MibTable
rcftRemoteMoudlePdhTable=_RcftRemoteMoudlePdhTable_Object((1,3,6,1,4,1,8886,2,1,6,9,3,1,1))
if mibBuilder.loadTexts:rcftRemoteMoudlePdhTable.setStatus(_A)
_RcftRemoteMoudlePdhEntry_Object=MibTableRow
rcftRemoteMoudlePdhEntry=_RcftRemoteMoudlePdhEntry_Object((1,3,6,1,4,1,8886,2,1,6,9,3,1,1,1))
rcftRemoteMoudlePdhEntry.setIndexNames((0,_F,_H),(0,_F,_I),(0,_C,_J),(0,_C,_W),(0,_C,_AR))
if mibBuilder.loadTexts:rcftRemoteMoudlePdhEntry.setStatus(_A)
_RcftRemoteMoudlePdhIndex_Type=Integer32
_RcftRemoteMoudlePdhIndex_Object=MibTableColumn
rcftRemoteMoudlePdhIndex=_RcftRemoteMoudlePdhIndex_Object((1,3,6,1,4,1,8886,2,1,6,9,3,1,1,1,1),_RcftRemoteMoudlePdhIndex_Type())
rcftRemoteMoudlePdhIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteMoudlePdhIndex.setStatus(_A)
_RcftRemoteMoudlePdhAlarmStatus_Type=Integer32
_RcftRemoteMoudlePdhAlarmStatus_Object=MibTableColumn
rcftRemoteMoudlePdhAlarmStatus=_RcftRemoteMoudlePdhAlarmStatus_Object((1,3,6,1,4,1,8886,2,1,6,9,3,1,1,1,2),_RcftRemoteMoudlePdhAlarmStatus_Type())
rcftRemoteMoudlePdhAlarmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteMoudlePdhAlarmStatus.setStatus(_A)
_RcftRemoteMoudlePdhStatus_Type=Integer32
_RcftRemoteMoudlePdhStatus_Object=MibTableColumn
rcftRemoteMoudlePdhStatus=_RcftRemoteMoudlePdhStatus_Object((1,3,6,1,4,1,8886,2,1,6,9,3,1,1,1,3),_RcftRemoteMoudlePdhStatus_Type())
rcftRemoteMoudlePdhStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteMoudlePdhStatus.setStatus(_A)
_RcftRemoteMoudlePdhTraps_ObjectIdentity=ObjectIdentity
rcftRemoteMoudlePdhTraps=_RcftRemoteMoudlePdhTraps_ObjectIdentity((1,3,6,1,4,1,8886,2,1,6,9,3,10))
_RcftRemoteMoudleE1_ObjectIdentity=ObjectIdentity
rcftRemoteMoudleE1=_RcftRemoteMoudleE1_ObjectIdentity((1,3,6,1,4,1,8886,2,1,6,9,4))
_RcftRemoteMoudleE1Objects_ObjectIdentity=ObjectIdentity
rcftRemoteMoudleE1Objects=_RcftRemoteMoudleE1Objects_ObjectIdentity((1,3,6,1,4,1,8886,2,1,6,9,4,1))
_RcftRemoteMoudleE1Table_Object=MibTable
rcftRemoteMoudleE1Table=_RcftRemoteMoudleE1Table_Object((1,3,6,1,4,1,8886,2,1,6,9,4,1,1))
if mibBuilder.loadTexts:rcftRemoteMoudleE1Table.setStatus(_A)
_RcftRemoteMoudleE1Entry_Object=MibTableRow
rcftRemoteMoudleE1Entry=_RcftRemoteMoudleE1Entry_Object((1,3,6,1,4,1,8886,2,1,6,9,4,1,1,1))
rcftRemoteMoudleE1Entry.setIndexNames((0,_F,_H),(0,_F,_I),(0,_C,_J),(0,_C,_W),(0,_C,_AS))
if mibBuilder.loadTexts:rcftRemoteMoudleE1Entry.setStatus(_A)
_RcftRemoteMoudleE1Index_Type=Integer32
_RcftRemoteMoudleE1Index_Object=MibTableColumn
rcftRemoteMoudleE1Index=_RcftRemoteMoudleE1Index_Object((1,3,6,1,4,1,8886,2,1,6,9,4,1,1,1,1),_RcftRemoteMoudleE1Index_Type())
rcftRemoteMoudleE1Index.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteMoudleE1Index.setStatus(_A)
_RcftRemoteMoudleE1AlarmStatus_Type=Integer32
_RcftRemoteMoudleE1AlarmStatus_Object=MibTableColumn
rcftRemoteMoudleE1AlarmStatus=_RcftRemoteMoudleE1AlarmStatus_Object((1,3,6,1,4,1,8886,2,1,6,9,4,1,1,1,2),_RcftRemoteMoudleE1AlarmStatus_Type())
rcftRemoteMoudleE1AlarmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteMoudleE1AlarmStatus.setStatus(_A)
_RcftRemoteMoudleE1Status_Type=Integer32
_RcftRemoteMoudleE1Status_Object=MibTableColumn
rcftRemoteMoudleE1Status=_RcftRemoteMoudleE1Status_Object((1,3,6,1,4,1,8886,2,1,6,9,4,1,1,1,3),_RcftRemoteMoudleE1Status_Type())
rcftRemoteMoudleE1Status.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteMoudleE1Status.setStatus(_A)
_RcftRemoteMoudleE1TimeSlots_Type=Integer32
_RcftRemoteMoudleE1TimeSlots_Object=MibTableColumn
rcftRemoteMoudleE1TimeSlots=_RcftRemoteMoudleE1TimeSlots_Object((1,3,6,1,4,1,8886,2,1,6,9,4,1,1,1,4),_RcftRemoteMoudleE1TimeSlots_Type())
rcftRemoteMoudleE1TimeSlots.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteMoudleE1TimeSlots.setStatus(_A)
_RcftRemoteMoudleE1TS0Mode_Type=Integer32
_RcftRemoteMoudleE1TS0Mode_Object=MibTableColumn
rcftRemoteMoudleE1TS0Mode=_RcftRemoteMoudleE1TS0Mode_Object((1,3,6,1,4,1,8886,2,1,6,9,4,1,1,1,5),_RcftRemoteMoudleE1TS0Mode_Type())
rcftRemoteMoudleE1TS0Mode.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteMoudleE1TS0Mode.setStatus(_A)
_RcftRemoteMoudleE1LoopStatus_Type=Integer32
_RcftRemoteMoudleE1LoopStatus_Object=MibTableColumn
rcftRemoteMoudleE1LoopStatus=_RcftRemoteMoudleE1LoopStatus_Object((1,3,6,1,4,1,8886,2,1,6,9,4,1,1,1,6),_RcftRemoteMoudleE1LoopStatus_Type())
rcftRemoteMoudleE1LoopStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteMoudleE1LoopStatus.setStatus(_A)
_RcftRemoteMoudleE1ESCnt_Type=Integer32
_RcftRemoteMoudleE1ESCnt_Object=MibTableColumn
rcftRemoteMoudleE1ESCnt=_RcftRemoteMoudleE1ESCnt_Object((1,3,6,1,4,1,8886,2,1,6,9,4,1,1,1,7),_RcftRemoteMoudleE1ESCnt_Type())
rcftRemoteMoudleE1ESCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteMoudleE1ESCnt.setStatus(_A)
_RcftRemoteMoudleE1SESCnt_Type=Integer32
_RcftRemoteMoudleE1SESCnt_Object=MibTableColumn
rcftRemoteMoudleE1SESCnt=_RcftRemoteMoudleE1SESCnt_Object((1,3,6,1,4,1,8886,2,1,6,9,4,1,1,1,8),_RcftRemoteMoudleE1SESCnt_Type())
rcftRemoteMoudleE1SESCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteMoudleE1SESCnt.setStatus(_A)
_RcftRemoteMoudleE1Performance_ObjectIdentity=ObjectIdentity
rcftRemoteMoudleE1Performance=_RcftRemoteMoudleE1Performance_ObjectIdentity((1,3,6,1,4,1,8886,2,1,6,9,4,2))
_RcftRemoteMoudleE1StatisticTable_Object=MibTable
rcftRemoteMoudleE1StatisticTable=_RcftRemoteMoudleE1StatisticTable_Object((1,3,6,1,4,1,8886,2,1,6,9,4,2,1))
if mibBuilder.loadTexts:rcftRemoteMoudleE1StatisticTable.setStatus(_A)
_RcftRemoteMoudleE1StatisticEntry_Object=MibTableRow
rcftRemoteMoudleE1StatisticEntry=_RcftRemoteMoudleE1StatisticEntry_Object((1,3,6,1,4,1,8886,2,1,6,9,4,2,1,1))
if mibBuilder.loadTexts:rcftRemoteMoudleE1StatisticEntry.setStatus(_A)
_RcftRemoteMoudleE1TxPackets_Type=Counter32
_RcftRemoteMoudleE1TxPackets_Object=MibTableColumn
rcftRemoteMoudleE1TxPackets=_RcftRemoteMoudleE1TxPackets_Object((1,3,6,1,4,1,8886,2,1,6,9,4,2,1,1,1),_RcftRemoteMoudleE1TxPackets_Type())
rcftRemoteMoudleE1TxPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteMoudleE1TxPackets.setStatus(_A)
_RcftRemoteMoudleE1TxBytes_Type=Counter32
_RcftRemoteMoudleE1TxBytes_Object=MibTableColumn
rcftRemoteMoudleE1TxBytes=_RcftRemoteMoudleE1TxBytes_Object((1,3,6,1,4,1,8886,2,1,6,9,4,2,1,1,2),_RcftRemoteMoudleE1TxBytes_Type())
rcftRemoteMoudleE1TxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteMoudleE1TxBytes.setStatus(_A)
_RcftRemoteMoudleE1TxFailurePackets_Type=Counter32
_RcftRemoteMoudleE1TxFailurePackets_Object=MibTableColumn
rcftRemoteMoudleE1TxFailurePackets=_RcftRemoteMoudleE1TxFailurePackets_Object((1,3,6,1,4,1,8886,2,1,6,9,4,2,1,1,3),_RcftRemoteMoudleE1TxFailurePackets_Type())
rcftRemoteMoudleE1TxFailurePackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteMoudleE1TxFailurePackets.setStatus(_A)
_RcftRemoteMoudleE1RxPackets_Type=Counter32
_RcftRemoteMoudleE1RxPackets_Object=MibTableColumn
rcftRemoteMoudleE1RxPackets=_RcftRemoteMoudleE1RxPackets_Object((1,3,6,1,4,1,8886,2,1,6,9,4,2,1,1,4),_RcftRemoteMoudleE1RxPackets_Type())
rcftRemoteMoudleE1RxPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteMoudleE1RxPackets.setStatus(_A)
_RcftRemoteMoudleE1RxBytes_Type=Counter32
_RcftRemoteMoudleE1RxBytes_Object=MibTableColumn
rcftRemoteMoudleE1RxBytes=_RcftRemoteMoudleE1RxBytes_Object((1,3,6,1,4,1,8886,2,1,6,9,4,2,1,1,5),_RcftRemoteMoudleE1RxBytes_Type())
rcftRemoteMoudleE1RxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteMoudleE1RxBytes.setStatus(_A)
_RcftRemoteMoudleE1RxErrorPackets_Type=Counter32
_RcftRemoteMoudleE1RxErrorPackets_Object=MibTableColumn
rcftRemoteMoudleE1RxErrorPackets=_RcftRemoteMoudleE1RxErrorPackets_Object((1,3,6,1,4,1,8886,2,1,6,9,4,2,1,1,6),_RcftRemoteMoudleE1RxErrorPackets_Type())
rcftRemoteMoudleE1RxErrorPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteMoudleE1RxErrorPackets.setStatus(_A)
_RcftRemoteMoudleE1FluxTimer_Type=Counter32
_RcftRemoteMoudleE1FluxTimer_Object=MibTableColumn
rcftRemoteMoudleE1FluxTimer=_RcftRemoteMoudleE1FluxTimer_Object((1,3,6,1,4,1,8886,2,1,6,9,4,2,1,1,7),_RcftRemoteMoudleE1FluxTimer_Type())
rcftRemoteMoudleE1FluxTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteMoudleE1FluxTimer.setStatus(_A)
_RcftRemoteMoudleE1Traps_ObjectIdentity=ObjectIdentity
rcftRemoteMoudleE1Traps=_RcftRemoteMoudleE1Traps_ObjectIdentity((1,3,6,1,4,1,8886,2,1,6,9,4,10))
_RcftRemoteMoudleV35_ObjectIdentity=ObjectIdentity
rcftRemoteMoudleV35=_RcftRemoteMoudleV35_ObjectIdentity((1,3,6,1,4,1,8886,2,1,6,9,5))
_RcftRemoteMoudleV35Objects_ObjectIdentity=ObjectIdentity
rcftRemoteMoudleV35Objects=_RcftRemoteMoudleV35Objects_ObjectIdentity((1,3,6,1,4,1,8886,2,1,6,9,5,1))
_RcftRemoteMoudleV35Table_Object=MibTable
rcftRemoteMoudleV35Table=_RcftRemoteMoudleV35Table_Object((1,3,6,1,4,1,8886,2,1,6,9,5,1,1))
if mibBuilder.loadTexts:rcftRemoteMoudleV35Table.setStatus(_A)
_RcftRemoteMoudleV35Entry_Object=MibTableRow
rcftRemoteMoudleV35Entry=_RcftRemoteMoudleV35Entry_Object((1,3,6,1,4,1,8886,2,1,6,9,5,1,1,1))
rcftRemoteMoudleV35Entry.setIndexNames((0,_F,_H),(0,_F,_I),(0,_C,_J),(0,_C,_W),(0,_C,_AT))
if mibBuilder.loadTexts:rcftRemoteMoudleV35Entry.setStatus(_A)
_RcftRemoteMoudleV35Index_Type=Integer32
_RcftRemoteMoudleV35Index_Object=MibTableColumn
rcftRemoteMoudleV35Index=_RcftRemoteMoudleV35Index_Object((1,3,6,1,4,1,8886,2,1,6,9,5,1,1,1,1),_RcftRemoteMoudleV35Index_Type())
rcftRemoteMoudleV35Index.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteMoudleV35Index.setStatus(_A)
_RcftRemoteMoudleV35AlarmStatus_Type=Integer32
_RcftRemoteMoudleV35AlarmStatus_Object=MibTableColumn
rcftRemoteMoudleV35AlarmStatus=_RcftRemoteMoudleV35AlarmStatus_Object((1,3,6,1,4,1,8886,2,1,6,9,5,1,1,1,2),_RcftRemoteMoudleV35AlarmStatus_Type())
rcftRemoteMoudleV35AlarmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteMoudleV35AlarmStatus.setStatus(_A)
_RcftRemoteMoudleV35Status_Type=Integer32
_RcftRemoteMoudleV35Status_Object=MibTableColumn
rcftRemoteMoudleV35Status=_RcftRemoteMoudleV35Status_Object((1,3,6,1,4,1,8886,2,1,6,9,5,1,1,1,3),_RcftRemoteMoudleV35Status_Type())
rcftRemoteMoudleV35Status.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteMoudleV35Status.setStatus(_A)
_RcftRemoteMoudleV35Traps_ObjectIdentity=ObjectIdentity
rcftRemoteMoudleV35Traps=_RcftRemoteMoudleV35Traps_ObjectIdentity((1,3,6,1,4,1,8886,2,1,6,9,5,10))
_RcftRemoteAudioPortMIB_ObjectIdentity=ObjectIdentity
rcftRemoteAudioPortMIB=_RcftRemoteAudioPortMIB_ObjectIdentity((1,3,6,1,4,1,8886,2,1,6,10))
_RcftRemoteAudioPortObjects_ObjectIdentity=ObjectIdentity
rcftRemoteAudioPortObjects=_RcftRemoteAudioPortObjects_ObjectIdentity((1,3,6,1,4,1,8886,2,1,6,10,1))
_RcftRemoteAudioPortTable_Object=MibTable
rcftRemoteAudioPortTable=_RcftRemoteAudioPortTable_Object((1,3,6,1,4,1,8886,2,1,6,10,1,1))
if mibBuilder.loadTexts:rcftRemoteAudioPortTable.setStatus(_A)
_RcftRemoteAudioPortEntry_Object=MibTableRow
rcftRemoteAudioPortEntry=_RcftRemoteAudioPortEntry_Object((1,3,6,1,4,1,8886,2,1,6,10,1,1,1))
rcftRemoteAudioPortEntry.setIndexNames((0,_F,_H),(0,_F,_I),(0,_C,_J),(0,_C,_AU))
if mibBuilder.loadTexts:rcftRemoteAudioPortEntry.setStatus(_A)
_RcftRemoteAudioPortIndex_Type=Integer32
_RcftRemoteAudioPortIndex_Object=MibTableColumn
rcftRemoteAudioPortIndex=_RcftRemoteAudioPortIndex_Object((1,3,6,1,4,1,8886,2,1,6,10,1,1,1,1),_RcftRemoteAudioPortIndex_Type())
rcftRemoteAudioPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteAudioPortIndex.setStatus(_A)
_RcftRemoteAudioPortStatus_Type=Integer32
_RcftRemoteAudioPortStatus_Object=MibTableColumn
rcftRemoteAudioPortStatus=_RcftRemoteAudioPortStatus_Object((1,3,6,1,4,1,8886,2,1,6,10,1,1,1,2),_RcftRemoteAudioPortStatus_Type())
rcftRemoteAudioPortStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteAudioPortStatus.setStatus(_A)
_RcftRemoteAudioPortPosition_Type=Integer32
_RcftRemoteAudioPortPosition_Object=MibTableColumn
rcftRemoteAudioPortPosition=_RcftRemoteAudioPortPosition_Object((1,3,6,1,4,1,8886,2,1,6,10,1,1,1,3),_RcftRemoteAudioPortPosition_Type())
rcftRemoteAudioPortPosition.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteAudioPortPosition.setStatus(_A)
_RcftRemoteAudioPortType_Type=Integer32
_RcftRemoteAudioPortType_Object=MibTableColumn
rcftRemoteAudioPortType=_RcftRemoteAudioPortType_Object((1,3,6,1,4,1,8886,2,1,6,10,1,1,1,4),_RcftRemoteAudioPortType_Type())
rcftRemoteAudioPortType.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteAudioPortType.setStatus(_A)
_RcftRemoteAudioPortPerformance_ObjectIdentity=ObjectIdentity
rcftRemoteAudioPortPerformance=_RcftRemoteAudioPortPerformance_ObjectIdentity((1,3,6,1,4,1,8886,2,1,6,10,2))
_RcftRemoteAudioPortTraps_ObjectIdentity=ObjectIdentity
rcftRemoteAudioPortTraps=_RcftRemoteAudioPortTraps_ObjectIdentity((1,3,6,1,4,1,8886,2,1,6,10,10))
_RcftRemoteVideoPortMIB_ObjectIdentity=ObjectIdentity
rcftRemoteVideoPortMIB=_RcftRemoteVideoPortMIB_ObjectIdentity((1,3,6,1,4,1,8886,2,1,6,11))
_RcftRemoteVideoPortObjects_ObjectIdentity=ObjectIdentity
rcftRemoteVideoPortObjects=_RcftRemoteVideoPortObjects_ObjectIdentity((1,3,6,1,4,1,8886,2,1,6,11,1))
_RcftRemoteVideoPortTable_Object=MibTable
rcftRemoteVideoPortTable=_RcftRemoteVideoPortTable_Object((1,3,6,1,4,1,8886,2,1,6,11,1,1))
if mibBuilder.loadTexts:rcftRemoteVideoPortTable.setStatus(_A)
_RcftRemoteVideoPortEntry_Object=MibTableRow
rcftRemoteVideoPortEntry=_RcftRemoteVideoPortEntry_Object((1,3,6,1,4,1,8886,2,1,6,11,1,1,1))
rcftRemoteVideoPortEntry.setIndexNames((0,_F,_H),(0,_F,_I),(0,_C,_J),(0,_C,_AV))
if mibBuilder.loadTexts:rcftRemoteVideoPortEntry.setStatus(_A)
_RcftRemoteVideoPortIndex_Type=Integer32
_RcftRemoteVideoPortIndex_Object=MibTableColumn
rcftRemoteVideoPortIndex=_RcftRemoteVideoPortIndex_Object((1,3,6,1,4,1,8886,2,1,6,11,1,1,1,1),_RcftRemoteVideoPortIndex_Type())
rcftRemoteVideoPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteVideoPortIndex.setStatus(_A)
_RcftRemoteVideoPortStatus_Type=Integer32
_RcftRemoteVideoPortStatus_Object=MibTableColumn
rcftRemoteVideoPortStatus=_RcftRemoteVideoPortStatus_Object((1,3,6,1,4,1,8886,2,1,6,11,1,1,1,2),_RcftRemoteVideoPortStatus_Type())
rcftRemoteVideoPortStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteVideoPortStatus.setStatus(_A)
_RcftRemoteVideoPortPosition_Type=Integer32
_RcftRemoteVideoPortPosition_Object=MibTableColumn
rcftRemoteVideoPortPosition=_RcftRemoteVideoPortPosition_Object((1,3,6,1,4,1,8886,2,1,6,11,1,1,1,3),_RcftRemoteVideoPortPosition_Type())
rcftRemoteVideoPortPosition.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteVideoPortPosition.setStatus(_A)
_RcftRemoteVideoPortSourceID_Type=Integer32
_RcftRemoteVideoPortSourceID_Object=MibTableColumn
rcftRemoteVideoPortSourceID=_RcftRemoteVideoPortSourceID_Object((1,3,6,1,4,1,8886,2,1,6,11,1,1,1,4),_RcftRemoteVideoPortSourceID_Type())
rcftRemoteVideoPortSourceID.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteVideoPortSourceID.setStatus(_A)
_RcftRemoteVideoPortPerformance_ObjectIdentity=ObjectIdentity
rcftRemoteVideoPortPerformance=_RcftRemoteVideoPortPerformance_ObjectIdentity((1,3,6,1,4,1,8886,2,1,6,11,2))
_RcftRemoteVideoPortTraps_ObjectIdentity=ObjectIdentity
rcftRemoteVideoPortTraps=_RcftRemoteVideoPortTraps_ObjectIdentity((1,3,6,1,4,1,8886,2,1,6,11,10))
_RcftRemoteDataPortMIB_ObjectIdentity=ObjectIdentity
rcftRemoteDataPortMIB=_RcftRemoteDataPortMIB_ObjectIdentity((1,3,6,1,4,1,8886,2,1,6,12))
_RcftRemoteDataPortObjects_ObjectIdentity=ObjectIdentity
rcftRemoteDataPortObjects=_RcftRemoteDataPortObjects_ObjectIdentity((1,3,6,1,4,1,8886,2,1,6,12,1))
_RcftRemoteDataPortTable_Object=MibTable
rcftRemoteDataPortTable=_RcftRemoteDataPortTable_Object((1,3,6,1,4,1,8886,2,1,6,12,1,1))
if mibBuilder.loadTexts:rcftRemoteDataPortTable.setStatus(_A)
_RcftRemoteDataPortEntry_Object=MibTableRow
rcftRemoteDataPortEntry=_RcftRemoteDataPortEntry_Object((1,3,6,1,4,1,8886,2,1,6,12,1,1,1))
rcftRemoteDataPortEntry.setIndexNames((0,_F,_H),(0,_F,_I),(0,_C,_J),(0,_C,_AW))
if mibBuilder.loadTexts:rcftRemoteDataPortEntry.setStatus(_A)
_RcftRemoteDataPortIndex_Type=Integer32
_RcftRemoteDataPortIndex_Object=MibTableColumn
rcftRemoteDataPortIndex=_RcftRemoteDataPortIndex_Object((1,3,6,1,4,1,8886,2,1,6,12,1,1,1,1),_RcftRemoteDataPortIndex_Type())
rcftRemoteDataPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteDataPortIndex.setStatus(_A)
_RcftRemoteDataPortStatus_Type=Integer32
_RcftRemoteDataPortStatus_Object=MibTableColumn
rcftRemoteDataPortStatus=_RcftRemoteDataPortStatus_Object((1,3,6,1,4,1,8886,2,1,6,12,1,1,1,2),_RcftRemoteDataPortStatus_Type())
rcftRemoteDataPortStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteDataPortStatus.setStatus(_A)
_RcftRemoteDataPortPosition_Type=Integer32
_RcftRemoteDataPortPosition_Object=MibTableColumn
rcftRemoteDataPortPosition=_RcftRemoteDataPortPosition_Object((1,3,6,1,4,1,8886,2,1,6,12,1,1,1,3),_RcftRemoteDataPortPosition_Type())
rcftRemoteDataPortPosition.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteDataPortPosition.setStatus(_A)
_RcftRemoteDataPortType_Type=Integer32
_RcftRemoteDataPortType_Object=MibTableColumn
rcftRemoteDataPortType=_RcftRemoteDataPortType_Object((1,3,6,1,4,1,8886,2,1,6,12,1,1,1,4),_RcftRemoteDataPortType_Type())
rcftRemoteDataPortType.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteDataPortType.setStatus(_A)
_RcftRemoteDataPortPerformance_ObjectIdentity=ObjectIdentity
rcftRemoteDataPortPerformance=_RcftRemoteDataPortPerformance_ObjectIdentity((1,3,6,1,4,1,8886,2,1,6,12,2))
_RcftRemoteDataPortTraps_ObjectIdentity=ObjectIdentity
rcftRemoteDataPortTraps=_RcftRemoteDataPortTraps_ObjectIdentity((1,3,6,1,4,1,8886,2,1,6,12,10))
_RcftRemoteSimpleModuleMIB_ObjectIdentity=ObjectIdentity
rcftRemoteSimpleModuleMIB=_RcftRemoteSimpleModuleMIB_ObjectIdentity((1,3,6,1,4,1,8886,2,1,6,13))
_RcftRemoteSimpleModuleObjects_ObjectIdentity=ObjectIdentity
rcftRemoteSimpleModuleObjects=_RcftRemoteSimpleModuleObjects_ObjectIdentity((1,3,6,1,4,1,8886,2,1,6,13,1))
_RcftRemoteSimpleModuleTable_Object=MibTable
rcftRemoteSimpleModuleTable=_RcftRemoteSimpleModuleTable_Object((1,3,6,1,4,1,8886,2,1,6,13,1,1))
if mibBuilder.loadTexts:rcftRemoteSimpleModuleTable.setStatus(_A)
_RcftRemoteSimpleModuleEntry_Object=MibTableRow
rcftRemoteSimpleModuleEntry=_RcftRemoteSimpleModuleEntry_Object((1,3,6,1,4,1,8886,2,1,6,13,1,1,1))
rcftRemoteSimpleModuleEntry.setIndexNames((0,_F,_H),(0,_F,_I),(0,_C,_J),(0,_C,_AX))
if mibBuilder.loadTexts:rcftRemoteSimpleModuleEntry.setStatus(_A)
_RcftRemoteSimpleModuleIndex_Type=Integer32
_RcftRemoteSimpleModuleIndex_Object=MibTableColumn
rcftRemoteSimpleModuleIndex=_RcftRemoteSimpleModuleIndex_Object((1,3,6,1,4,1,8886,2,1,6,13,1,1,1,1),_RcftRemoteSimpleModuleIndex_Type())
rcftRemoteSimpleModuleIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteSimpleModuleIndex.setStatus(_A)
_RcftRemoteSimpleModuleExist_Type=Integer32
_RcftRemoteSimpleModuleExist_Object=MibTableColumn
rcftRemoteSimpleModuleExist=_RcftRemoteSimpleModuleExist_Object((1,3,6,1,4,1,8886,2,1,6,13,1,1,1,2),_RcftRemoteSimpleModuleExist_Type())
rcftRemoteSimpleModuleExist.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteSimpleModuleExist.setStatus(_A)
_RcftRemoteSimpleModulePosition_Type=Integer32
_RcftRemoteSimpleModulePosition_Object=MibTableColumn
rcftRemoteSimpleModulePosition=_RcftRemoteSimpleModulePosition_Object((1,3,6,1,4,1,8886,2,1,6,13,1,1,1,3),_RcftRemoteSimpleModulePosition_Type())
rcftRemoteSimpleModulePosition.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteSimpleModulePosition.setStatus(_A)
_RcftRemoteSimpleModuleStatus_Type=Integer32
_RcftRemoteSimpleModuleStatus_Object=MibTableColumn
rcftRemoteSimpleModuleStatus=_RcftRemoteSimpleModuleStatus_Object((1,3,6,1,4,1,8886,2,1,6,13,1,1,1,4),_RcftRemoteSimpleModuleStatus_Type())
rcftRemoteSimpleModuleStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteSimpleModuleStatus.setStatus(_A)
_RcftRemoteSimpleModuleType_Type=Integer32
_RcftRemoteSimpleModuleType_Object=MibTableColumn
rcftRemoteSimpleModuleType=_RcftRemoteSimpleModuleType_Object((1,3,6,1,4,1,8886,2,1,6,13,1,1,1,5),_RcftRemoteSimpleModuleType_Type())
rcftRemoteSimpleModuleType.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteSimpleModuleType.setStatus(_A)
_RcftRemoteSimpleModulePerformance_ObjectIdentity=ObjectIdentity
rcftRemoteSimpleModulePerformance=_RcftRemoteSimpleModulePerformance_ObjectIdentity((1,3,6,1,4,1,8886,2,1,6,13,2))
_RcftRemoteSimpleModuleTraps_ObjectIdentity=ObjectIdentity
rcftRemoteSimpleModuleTraps=_RcftRemoteSimpleModuleTraps_ObjectIdentity((1,3,6,1,4,1,8886,2,1,6,13,10))
_RcftRemoteVLANMIB_ObjectIdentity=ObjectIdentity
rcftRemoteVLANMIB=_RcftRemoteVLANMIB_ObjectIdentity((1,3,6,1,4,1,8886,2,1,6,14))
_RcftRemoteVLANObjects_ObjectIdentity=ObjectIdentity
rcftRemoteVLANObjects=_RcftRemoteVLANObjects_ObjectIdentity((1,3,6,1,4,1,8886,2,1,6,14,1))
_RcftRemoteVLANTable_Object=MibTable
rcftRemoteVLANTable=_RcftRemoteVLANTable_Object((1,3,6,1,4,1,8886,2,1,6,14,1,1))
if mibBuilder.loadTexts:rcftRemoteVLANTable.setStatus(_A)
_RcftRemoteVLANEntry_Object=MibTableRow
rcftRemoteVLANEntry=_RcftRemoteVLANEntry_Object((1,3,6,1,4,1,8886,2,1,6,14,1,1,1))
rcftRemoteVLANEntry.setIndexNames((0,_F,_H),(0,_F,_I),(0,_C,_J),(0,_C,_AY))
if mibBuilder.loadTexts:rcftRemoteVLANEntry.setStatus(_A)
_RcftRemoteVLANIndex_Type=Integer32
_RcftRemoteVLANIndex_Object=MibTableColumn
rcftRemoteVLANIndex=_RcftRemoteVLANIndex_Object((1,3,6,1,4,1,8886,2,1,6,14,1,1,1,1),_RcftRemoteVLANIndex_Type())
rcftRemoteVLANIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteVLANIndex.setStatus(_A)
_RcftRemoteVLANStatus_Type=Integer32
_RcftRemoteVLANStatus_Object=MibTableColumn
rcftRemoteVLANStatus=_RcftRemoteVLANStatus_Object((1,3,6,1,4,1,8886,2,1,6,14,1,1,1,2),_RcftRemoteVLANStatus_Type())
rcftRemoteVLANStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteVLANStatus.setStatus(_A)
_RcftRemoteVLANmember_Type=Integer32
_RcftRemoteVLANmember_Object=MibTableColumn
rcftRemoteVLANmember=_RcftRemoteVLANmember_Object((1,3,6,1,4,1,8886,2,1,6,14,1,1,1,3),_RcftRemoteVLANmember_Type())
rcftRemoteVLANmember.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteVLANmember.setStatus(_A)
_RcftRemoteVID_Type=Integer32
_RcftRemoteVID_Object=MibTableColumn
rcftRemoteVID=_RcftRemoteVID_Object((1,3,6,1,4,1,8886,2,1,6,14,1,1,1,4),_RcftRemoteVID_Type())
rcftRemoteVID.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteVID.setStatus(_A)
_RcftRemotePerformaceMib_ObjectIdentity=ObjectIdentity
rcftRemotePerformaceMib=_RcftRemotePerformaceMib_ObjectIdentity((1,3,6,1,4,1,8886,2,1,6,15))
_RcftRemoteStatisticPerformance_ObjectIdentity=ObjectIdentity
rcftRemoteStatisticPerformance=_RcftRemoteStatisticPerformance_ObjectIdentity((1,3,6,1,4,1,8886,2,1,6,15,1))
_RcftRemoteStatisticTable_Object=MibTable
rcftRemoteStatisticTable=_RcftRemoteStatisticTable_Object((1,3,6,1,4,1,8886,2,1,6,15,1,1))
if mibBuilder.loadTexts:rcftRemoteStatisticTable.setStatus(_A)
_RcftRemoteStatisticEntry_Object=MibTableRow
rcftRemoteStatisticEntry=_RcftRemoteStatisticEntry_Object((1,3,6,1,4,1,8886,2,1,6,15,1,1,1))
rcftRemoteStatisticEntry.setIndexNames((0,_F,_H),(0,_F,_I),(0,_C,_J),(0,_C,_AZ))
if mibBuilder.loadTexts:rcftRemoteStatisticEntry.setStatus(_A)
_RcftRemotePortIndex_Type=Integer32
_RcftRemotePortIndex_Object=MibTableColumn
rcftRemotePortIndex=_RcftRemotePortIndex_Object((1,3,6,1,4,1,8886,2,1,6,15,1,1,1,1),_RcftRemotePortIndex_Type())
rcftRemotePortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemotePortIndex.setStatus(_A)
_RcftRemotePortType_Type=Integer32
_RcftRemotePortType_Object=MibTableColumn
rcftRemotePortType=_RcftRemotePortType_Object((1,3,6,1,4,1,8886,2,1,6,15,1,1,1,2),_RcftRemotePortType_Type())
rcftRemotePortType.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemotePortType.setStatus(_A)
_RcftRemoteRxPackets_Type=Counter32
_RcftRemoteRxPackets_Object=MibTableColumn
rcftRemoteRxPackets=_RcftRemoteRxPackets_Object((1,3,6,1,4,1,8886,2,1,6,15,1,1,1,3),_RcftRemoteRxPackets_Type())
rcftRemoteRxPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteRxPackets.setStatus(_A)
_RcftRemoteRxLosPackets_Type=Counter32
_RcftRemoteRxLosPackets_Object=MibTableColumn
rcftRemoteRxLosPackets=_RcftRemoteRxLosPackets_Object((1,3,6,1,4,1,8886,2,1,6,15,1,1,1,4),_RcftRemoteRxLosPackets_Type())
rcftRemoteRxLosPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteRxLosPackets.setStatus(_A)
_RcftRemoteRxPreabErrPackets_Type=Counter32
_RcftRemoteRxPreabErrPackets_Object=MibTableColumn
rcftRemoteRxPreabErrPackets=_RcftRemoteRxPreabErrPackets_Object((1,3,6,1,4,1,8886,2,1,6,15,1,1,1,5),_RcftRemoteRxPreabErrPackets_Type())
rcftRemoteRxPreabErrPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteRxPreabErrPackets.setStatus(_A)
_RcftRemoteRxFCSErrPackets_Type=Counter32
_RcftRemoteRxFCSErrPackets_Object=MibTableColumn
rcftRemoteRxFCSErrPackets=_RcftRemoteRxFCSErrPackets_Object((1,3,6,1,4,1,8886,2,1,6,15,1,1,1,6),_RcftRemoteRxFCSErrPackets_Type())
rcftRemoteRxFCSErrPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteRxFCSErrPackets.setStatus(_A)
_RcftRemoteRxUnderSizePackets_Type=Counter32
_RcftRemoteRxUnderSizePackets_Object=MibTableColumn
rcftRemoteRxUnderSizePackets=_RcftRemoteRxUnderSizePackets_Object((1,3,6,1,4,1,8886,2,1,6,15,1,1,1,7),_RcftRemoteRxUnderSizePackets_Type())
rcftRemoteRxUnderSizePackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteRxUnderSizePackets.setStatus(_A)
_RcftRemoteRxOverSizePackets_Type=Counter32
_RcftRemoteRxOverSizePackets_Object=MibTableColumn
rcftRemoteRxOverSizePackets=_RcftRemoteRxOverSizePackets_Object((1,3,6,1,4,1,8886,2,1,6,15,1,1,1,8),_RcftRemoteRxOverSizePackets_Type())
rcftRemoteRxOverSizePackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteRxOverSizePackets.setStatus(_A)
_RcftRemoteRxPausePackets_Type=Counter32
_RcftRemoteRxPausePackets_Object=MibTableColumn
rcftRemoteRxPausePackets=_RcftRemoteRxPausePackets_Object((1,3,6,1,4,1,8886,2,1,6,15,1,1,1,9),_RcftRemoteRxPausePackets_Type())
rcftRemoteRxPausePackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteRxPausePackets.setStatus(_A)
_RcftRemoteRxOamPackets_Type=Counter32
_RcftRemoteRxOamPackets_Object=MibTableColumn
rcftRemoteRxOamPackets=_RcftRemoteRxOamPackets_Object((1,3,6,1,4,1,8886,2,1,6,15,1,1,1,10),_RcftRemoteRxOamPackets_Type())
rcftRemoteRxOamPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteRxOamPackets.setStatus(_A)
_RcftRemoteRxBytes_Type=Counter32
_RcftRemoteRxBytes_Object=MibTableColumn
rcftRemoteRxBytes=_RcftRemoteRxBytes_Object((1,3,6,1,4,1,8886,2,1,6,15,1,1,1,11),_RcftRemoteRxBytes_Type())
rcftRemoteRxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteRxBytes.setStatus(_A)
_RcftRemoteTxPackets_Type=Counter32
_RcftRemoteTxPackets_Object=MibTableColumn
rcftRemoteTxPackets=_RcftRemoteTxPackets_Object((1,3,6,1,4,1,8886,2,1,6,15,1,1,1,12),_RcftRemoteTxPackets_Type())
rcftRemoteTxPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteTxPackets.setStatus(_A)
_RcftRemoteTxFCSErrPackets_Type=Counter32
_RcftRemoteTxFCSErrPackets_Object=MibTableColumn
rcftRemoteTxFCSErrPackets=_RcftRemoteTxFCSErrPackets_Object((1,3,6,1,4,1,8886,2,1,6,15,1,1,1,13),_RcftRemoteTxFCSErrPackets_Type())
rcftRemoteTxFCSErrPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteTxFCSErrPackets.setStatus(_A)
_RcftRemoteTxPausePackets_Type=Counter32
_RcftRemoteTxPausePackets_Object=MibTableColumn
rcftRemoteTxPausePackets=_RcftRemoteTxPausePackets_Object((1,3,6,1,4,1,8886,2,1,6,15,1,1,1,14),_RcftRemoteTxPausePackets_Type())
rcftRemoteTxPausePackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteTxPausePackets.setStatus(_A)
_RcftRemoteTxOamPackets_Type=Counter32
_RcftRemoteTxOamPackets_Object=MibTableColumn
rcftRemoteTxOamPackets=_RcftRemoteTxOamPackets_Object((1,3,6,1,4,1,8886,2,1,6,15,1,1,1,15),_RcftRemoteTxOamPackets_Type())
rcftRemoteTxOamPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteTxOamPackets.setStatus(_A)
_RcftRemoteTxBytes_Type=Counter32
_RcftRemoteTxBytes_Object=MibTableColumn
rcftRemoteTxBytes=_RcftRemoteTxBytes_Object((1,3,6,1,4,1,8886,2,1,6,15,1,1,1,16),_RcftRemoteTxBytes_Type())
rcftRemoteTxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteTxBytes.setStatus(_A)
_RcftRemoteFluxTimer_Type=Counter32
_RcftRemoteFluxTimer_Object=MibTableColumn
rcftRemoteFluxTimer=_RcftRemoteFluxTimer_Object((1,3,6,1,4,1,8886,2,1,6,15,1,1,1,17),_RcftRemoteFluxTimer_Type())
rcftRemoteFluxTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteFluxTimer.setStatus(_A)
_RcftRemoteVCGMib_ObjectIdentity=ObjectIdentity
rcftRemoteVCGMib=_RcftRemoteVCGMib_ObjectIdentity((1,3,6,1,4,1,8886,2,1,6,16))
_RcftRemoteVCGObjects_ObjectIdentity=ObjectIdentity
rcftRemoteVCGObjects=_RcftRemoteVCGObjects_ObjectIdentity((1,3,6,1,4,1,8886,2,1,6,16,1))
_RcftRemoteVCGTable_Object=MibTable
rcftRemoteVCGTable=_RcftRemoteVCGTable_Object((1,3,6,1,4,1,8886,2,1,6,16,1,1))
if mibBuilder.loadTexts:rcftRemoteVCGTable.setStatus(_A)
_RcftRemoteVCGEntry_Object=MibTableRow
rcftRemoteVCGEntry=_RcftRemoteVCGEntry_Object((1,3,6,1,4,1,8886,2,1,6,16,1,1,1))
rcftRemoteVCGEntry.setIndexNames((0,_F,_H),(0,_F,_I),(0,_C,_J),(0,_C,_Aa))
if mibBuilder.loadTexts:rcftRemoteVCGEntry.setStatus(_A)
_RcftRemoteVCGIndex_Type=Integer32
_RcftRemoteVCGIndex_Object=MibTableColumn
rcftRemoteVCGIndex=_RcftRemoteVCGIndex_Object((1,3,6,1,4,1,8886,2,1,6,16,1,1,1,1),_RcftRemoteVCGIndex_Type())
rcftRemoteVCGIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteVCGIndex.setStatus(_A)
_RcftRemoteVCGStatus_Type=Integer32
_RcftRemoteVCGStatus_Object=MibTableColumn
rcftRemoteVCGStatus=_RcftRemoteVCGStatus_Object((1,3,6,1,4,1,8886,2,1,6,16,1,1,1,2),_RcftRemoteVCGStatus_Type())
rcftRemoteVCGStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteVCGStatus.setStatus(_A)
_RcftRemoteVCGLoopStatus_Type=Integer32
_RcftRemoteVCGLoopStatus_Object=MibTableColumn
rcftRemoteVCGLoopStatus=_RcftRemoteVCGLoopStatus_Object((1,3,6,1,4,1,8886,2,1,6,16,1,1,1,3),_RcftRemoteVCGLoopStatus_Type())
rcftRemoteVCGLoopStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteVCGLoopStatus.setStatus(_A)
_RcftRemoteVCGLcasXPR_Type=Integer32
_RcftRemoteVCGLcasXPR_Object=MibTableColumn
rcftRemoteVCGLcasXPR=_RcftRemoteVCGLcasXPR_Object((1,3,6,1,4,1,8886,2,1,6,16,1,1,1,4),_RcftRemoteVCGLcasXPR_Type())
rcftRemoteVCGLcasXPR.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteVCGLcasXPR.setStatus(_A)
_RcftRemoteVCGLcasXAR_Type=Integer32
_RcftRemoteVCGLcasXAR_Object=MibTableColumn
rcftRemoteVCGLcasXAR=_RcftRemoteVCGLcasXAR_Object((1,3,6,1,4,1,8886,2,1,6,16,1,1,1,5),_RcftRemoteVCGLcasXAR_Type())
rcftRemoteVCGLcasXAR.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteVCGLcasXAR.setStatus(_A)
_RcftRemoteVCGLcasXPT_Type=Integer32
_RcftRemoteVCGLcasXPT_Object=MibTableColumn
rcftRemoteVCGLcasXPT=_RcftRemoteVCGLcasXPT_Object((1,3,6,1,4,1,8886,2,1,6,16,1,1,1,6),_RcftRemoteVCGLcasXPT_Type())
rcftRemoteVCGLcasXPT.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteVCGLcasXPT.setStatus(_A)
_RcftRemoteVCGLcasXAT_Type=Integer32
_RcftRemoteVCGLcasXAT_Object=MibTableColumn
rcftRemoteVCGLcasXAT=_RcftRemoteVCGLcasXAT_Object((1,3,6,1,4,1,8886,2,1,6,16,1,1,1,7),_RcftRemoteVCGLcasXAT_Type())
rcftRemoteVCGLcasXAT.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteVCGLcasXAT.setStatus(_A)
_RcftRemoteVCGAlarmStatus_Type=Integer32
_RcftRemoteVCGAlarmStatus_Object=MibTableColumn
rcftRemoteVCGAlarmStatus=_RcftRemoteVCGAlarmStatus_Object((1,3,6,1,4,1,8886,2,1,6,16,1,1,1,8),_RcftRemoteVCGAlarmStatus_Type())
rcftRemoteVCGAlarmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteVCGAlarmStatus.setStatus(_A)
_RcftRemoteVCGRxISPTPID_Type=Integer32
_RcftRemoteVCGRxISPTPID_Object=MibTableColumn
rcftRemoteVCGRxISPTPID=_RcftRemoteVCGRxISPTPID_Object((1,3,6,1,4,1,8886,2,1,6,16,1,1,1,9),_RcftRemoteVCGRxISPTPID_Type())
rcftRemoteVCGRxISPTPID.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteVCGRxISPTPID.setStatus(_A)
_RcftRemoteVCGTxISPTPID_Type=Integer32
_RcftRemoteVCGTxISPTPID_Object=MibTableColumn
rcftRemoteVCGTxISPTPID=_RcftRemoteVCGTxISPTPID_Object((1,3,6,1,4,1,8886,2,1,6,16,1,1,1,10),_RcftRemoteVCGTxISPTPID_Type())
rcftRemoteVCGTxISPTPID.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteVCGTxISPTPID.setStatus(_A)
_RcftRemoteVCGBaseCoS_Type=Integer32
_RcftRemoteVCGBaseCoS_Object=MibTableColumn
rcftRemoteVCGBaseCoS=_RcftRemoteVCGBaseCoS_Object((1,3,6,1,4,1,8886,2,1,6,16,1,1,1,11),_RcftRemoteVCGBaseCoS_Type())
rcftRemoteVCGBaseCoS.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteVCGBaseCoS.setStatus(_A)
_RcftRemoteVCGVLANID_Type=Integer32
_RcftRemoteVCGVLANID_Object=MibTableColumn
rcftRemoteVCGVLANID=_RcftRemoteVCGVLANID_Object((1,3,6,1,4,1,8886,2,1,6,16,1,1,1,12),_RcftRemoteVCGVLANID_Type())
rcftRemoteVCGVLANID.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteVCGVLANID.setStatus(_A)
class _RcftRemoteVCGMemberList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_RcftRemoteVCGMemberList_Type.__name__=_G
_RcftRemoteVCGMemberList_Object=MibTableColumn
rcftRemoteVCGMemberList=_RcftRemoteVCGMemberList_Object((1,3,6,1,4,1,8886,2,1,6,16,1,1,1,13),_RcftRemoteVCGMemberList_Type())
rcftRemoteVCGMemberList.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteVCGMemberList.setStatus(_A)
class _RcftRemoteVCGMemberStatus_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_RcftRemoteVCGMemberStatus_Type.__name__=_G
_RcftRemoteVCGMemberStatus_Object=MibTableColumn
rcftRemoteVCGMemberStatus=_RcftRemoteVCGMemberStatus_Object((1,3,6,1,4,1,8886,2,1,6,16,1,1,1,14),_RcftRemoteVCGMemberStatus_Type())
rcftRemoteVCGMemberStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftRemoteVCGMemberStatus.setStatus(_A)
class _RcftRemoteVCGMemberRxCode_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_RcftRemoteVCGMemberRxCode_Type.__name__=_G
_RcftRemoteVCGMemberRxCode_Object=MibTableColumn
rcftRemoteVCGMemberRxCode=_RcftRemoteVCGMemberRxCode_Object((1,3,6,1,4,1,8886,2,1,6,16,1,1,1,15),_RcftRemoteVCGMemberRxCode_Type())
rcftRemoteVCGMemberRxCode.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteVCGMemberRxCode.setStatus(_A)
class _RcftRemoteVCGMemberTxCode_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_RcftRemoteVCGMemberTxCode_Type.__name__=_G
_RcftRemoteVCGMemberTxCode_Object=MibTableColumn
rcftRemoteVCGMemberTxCode=_RcftRemoteVCGMemberTxCode_Object((1,3,6,1,4,1,8886,2,1,6,16,1,1,1,16),_RcftRemoteVCGMemberTxCode_Type())
rcftRemoteVCGMemberTxCode.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteVCGMemberTxCode.setStatus(_A)
class _RcftRemoteVCGMemberAlarmStatus_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_RcftRemoteVCGMemberAlarmStatus_Type.__name__=_G
_RcftRemoteVCGMemberAlarmStatus_Object=MibTableColumn
rcftRemoteVCGMemberAlarmStatus=_RcftRemoteVCGMemberAlarmStatus_Object((1,3,6,1,4,1,8886,2,1,6,16,1,1,1,17),_RcftRemoteVCGMemberAlarmStatus_Type())
rcftRemoteVCGMemberAlarmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteVCGMemberAlarmStatus.setStatus(_A)
class _RcftRemoteToLVCGMemberAlarmStatus_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_RcftRemoteToLVCGMemberAlarmStatus_Type.__name__=_G
_RcftRemoteToLVCGMemberAlarmStatus_Object=MibTableColumn
rcftRemoteToLVCGMemberAlarmStatus=_RcftRemoteToLVCGMemberAlarmStatus_Object((1,3,6,1,4,1,8886,2,1,6,16,1,1,1,18),_RcftRemoteToLVCGMemberAlarmStatus_Type())
rcftRemoteToLVCGMemberAlarmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteToLVCGMemberAlarmStatus.setStatus(_A)
_RcftRemoteVCGPerformance_ObjectIdentity=ObjectIdentity
rcftRemoteVCGPerformance=_RcftRemoteVCGPerformance_ObjectIdentity((1,3,6,1,4,1,8886,2,1,6,16,2))
_RcftRemoteVCGStatisticTable_Object=MibTable
rcftRemoteVCGStatisticTable=_RcftRemoteVCGStatisticTable_Object((1,3,6,1,4,1,8886,2,1,6,16,2,1))
if mibBuilder.loadTexts:rcftRemoteVCGStatisticTable.setStatus(_A)
_RcftRemoteVCGStatisticEntry_Object=MibTableRow
rcftRemoteVCGStatisticEntry=_RcftRemoteVCGStatisticEntry_Object((1,3,6,1,4,1,8886,2,1,6,16,2,1,1))
if mibBuilder.loadTexts:rcftRemoteVCGStatisticEntry.setStatus(_A)
_RcftRemoteVCGRxClientPackets_Type=Counter32
_RcftRemoteVCGRxClientPackets_Object=MibTableColumn
rcftRemoteVCGRxClientPackets=_RcftRemoteVCGRxClientPackets_Object((1,3,6,1,4,1,8886,2,1,6,16,2,1,1,1),_RcftRemoteVCGRxClientPackets_Type())
rcftRemoteVCGRxClientPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteVCGRxClientPackets.setStatus(_A)
_RcftRemoteVCGRxIdlePackets_Type=Counter32
_RcftRemoteVCGRxIdlePackets_Object=MibTableColumn
rcftRemoteVCGRxIdlePackets=_RcftRemoteVCGRxIdlePackets_Object((1,3,6,1,4,1,8886,2,1,6,16,2,1,1,2),_RcftRemoteVCGRxIdlePackets_Type())
rcftRemoteVCGRxIdlePackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteVCGRxIdlePackets.setStatus(_A)
_RcftRemoteVCGRxMgmntPackets_Type=Counter32
_RcftRemoteVCGRxMgmntPackets_Object=MibTableColumn
rcftRemoteVCGRxMgmntPackets=_RcftRemoteVCGRxMgmntPackets_Object((1,3,6,1,4,1,8886,2,1,6,16,2,1,1,3),_RcftRemoteVCGRxMgmntPackets_Type())
rcftRemoteVCGRxMgmntPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteVCGRxMgmntPackets.setStatus(_A)
_RcftRemoteVCGRxFCSErrMgmntPackets_Type=Counter32
_RcftRemoteVCGRxFCSErrMgmntPackets_Object=MibTableColumn
rcftRemoteVCGRxFCSErrMgmntPackets=_RcftRemoteVCGRxFCSErrMgmntPackets_Object((1,3,6,1,4,1,8886,2,1,6,16,2,1,1,4),_RcftRemoteVCGRxFCSErrMgmntPackets_Type())
rcftRemoteVCGRxFCSErrMgmntPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteVCGRxFCSErrMgmntPackets.setStatus(_A)
_RcftRemoteVCGRxLenErrPackets_Type=Counter32
_RcftRemoteVCGRxLenErrPackets_Object=MibTableColumn
rcftRemoteVCGRxLenErrPackets=_RcftRemoteVCGRxLenErrPackets_Object((1,3,6,1,4,1,8886,2,1,6,16,2,1,1,5),_RcftRemoteVCGRxLenErrPackets_Type())
rcftRemoteVCGRxLenErrPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteVCGRxLenErrPackets.setStatus(_A)
_RcftRemoteVCGRxFCSErrClientPackets_Type=Counter32
_RcftRemoteVCGRxFCSErrClientPackets_Object=MibTableColumn
rcftRemoteVCGRxFCSErrClientPackets=_RcftRemoteVCGRxFCSErrClientPackets_Object((1,3,6,1,4,1,8886,2,1,6,16,2,1,1,6),_RcftRemoteVCGRxFCSErrClientPackets_Type())
rcftRemoteVCGRxFCSErrClientPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteVCGRxFCSErrClientPackets.setStatus(_A)
_RcftRemoteVCGRxThecErrPackets_Type=Counter32
_RcftRemoteVCGRxThecErrPackets_Object=MibTableColumn
rcftRemoteVCGRxThecErrPackets=_RcftRemoteVCGRxThecErrPackets_Object((1,3,6,1,4,1,8886,2,1,6,16,2,1,1,7),_RcftRemoteVCGRxThecErrPackets_Type())
rcftRemoteVCGRxThecErrPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteVCGRxThecErrPackets.setStatus(_A)
_RcftRemoteVCGRxEhecErrPackets_Type=Counter32
_RcftRemoteVCGRxEhecErrPackets_Object=MibTableColumn
rcftRemoteVCGRxEhecErrPackets=_RcftRemoteVCGRxEhecErrPackets_Object((1,3,6,1,4,1,8886,2,1,6,16,2,1,1,8),_RcftRemoteVCGRxEhecErrPackets_Type())
rcftRemoteVCGRxEhecErrPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteVCGRxEhecErrPackets.setStatus(_A)
_RcftRemoteVCGRxCIDErrPackets_Type=Counter32
_RcftRemoteVCGRxCIDErrPackets_Object=MibTableColumn
rcftRemoteVCGRxCIDErrPackets=_RcftRemoteVCGRxCIDErrPackets_Object((1,3,6,1,4,1,8886,2,1,6,16,2,1,1,9),_RcftRemoteVCGRxCIDErrPackets_Type())
rcftRemoteVCGRxCIDErrPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteVCGRxCIDErrPackets.setStatus(_A)
_RcftRemoteVCGRxSpareErrPackets_Type=Counter32
_RcftRemoteVCGRxSpareErrPackets_Object=MibTableColumn
rcftRemoteVCGRxSpareErrPackets=_RcftRemoteVCGRxSpareErrPackets_Object((1,3,6,1,4,1,8886,2,1,6,16,2,1,1,10),_RcftRemoteVCGRxSpareErrPackets_Type())
rcftRemoteVCGRxSpareErrPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteVCGRxSpareErrPackets.setStatus(_A)
_RcftRemoteVCGRxChecCorPackets_Type=Counter32
_RcftRemoteVCGRxChecCorPackets_Object=MibTableColumn
rcftRemoteVCGRxChecCorPackets=_RcftRemoteVCGRxChecCorPackets_Object((1,3,6,1,4,1,8886,2,1,6,16,2,1,1,11),_RcftRemoteVCGRxChecCorPackets_Type())
rcftRemoteVCGRxChecCorPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteVCGRxChecCorPackets.setStatus(_A)
_RcftRemoteVCGRxThecCorPackets_Type=Counter32
_RcftRemoteVCGRxThecCorPackets_Object=MibTableColumn
rcftRemoteVCGRxThecCorPackets=_RcftRemoteVCGRxThecCorPackets_Object((1,3,6,1,4,1,8886,2,1,6,16,2,1,1,12),_RcftRemoteVCGRxThecCorPackets_Type())
rcftRemoteVCGRxThecCorPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteVCGRxThecCorPackets.setStatus(_A)
_RcftRemoteVCGRxEhecCorPackets_Type=Counter32
_RcftRemoteVCGRxEhecCorPackets_Object=MibTableColumn
rcftRemoteVCGRxEhecCorPackets=_RcftRemoteVCGRxEhecCorPackets_Object((1,3,6,1,4,1,8886,2,1,6,16,2,1,1,13),_RcftRemoteVCGRxEhecCorPackets_Type())
rcftRemoteVCGRxEhecCorPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteVCGRxEhecCorPackets.setStatus(_A)
_RcftRemoteVCGRxBytes_Type=Counter32
_RcftRemoteVCGRxBytes_Object=MibTableColumn
rcftRemoteVCGRxBytes=_RcftRemoteVCGRxBytes_Object((1,3,6,1,4,1,8886,2,1,6,16,2,1,1,14),_RcftRemoteVCGRxBytes_Type())
rcftRemoteVCGRxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteVCGRxBytes.setStatus(_A)
_RcftRemoteVCGTxClientPackets_Type=Counter32
_RcftRemoteVCGTxClientPackets_Object=MibTableColumn
rcftRemoteVCGTxClientPackets=_RcftRemoteVCGTxClientPackets_Object((1,3,6,1,4,1,8886,2,1,6,16,2,1,1,15),_RcftRemoteVCGTxClientPackets_Type())
rcftRemoteVCGTxClientPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteVCGTxClientPackets.setStatus(_A)
_RcftRemoteVCGTxIdlePackets_Type=Counter32
_RcftRemoteVCGTxIdlePackets_Object=MibTableColumn
rcftRemoteVCGTxIdlePackets=_RcftRemoteVCGTxIdlePackets_Object((1,3,6,1,4,1,8886,2,1,6,16,2,1,1,16),_RcftRemoteVCGTxIdlePackets_Type())
rcftRemoteVCGTxIdlePackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteVCGTxIdlePackets.setStatus(_A)
_RcftRemoteVCGTxMgmntPackets_Type=Counter32
_RcftRemoteVCGTxMgmntPackets_Object=MibTableColumn
rcftRemoteVCGTxMgmntPackets=_RcftRemoteVCGTxMgmntPackets_Object((1,3,6,1,4,1,8886,2,1,6,16,2,1,1,17),_RcftRemoteVCGTxMgmntPackets_Type())
rcftRemoteVCGTxMgmntPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteVCGTxMgmntPackets.setStatus(_A)
_RcftRemoteVCGTxBytes_Type=Counter32
_RcftRemoteVCGTxBytes_Object=MibTableColumn
rcftRemoteVCGTxBytes=_RcftRemoteVCGTxBytes_Object((1,3,6,1,4,1,8886,2,1,6,16,2,1,1,18),_RcftRemoteVCGTxBytes_Type())
rcftRemoteVCGTxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteVCGTxBytes.setStatus(_A)
_RcftRemoteVCGFluxTimer_Type=Counter32
_RcftRemoteVCGFluxTimer_Object=MibTableColumn
rcftRemoteVCGFluxTimer=_RcftRemoteVCGFluxTimer_Object((1,3,6,1,4,1,8886,2,1,6,16,2,1,1,19),_RcftRemoteVCGFluxTimer_Type())
rcftRemoteVCGFluxTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRemoteVCGFluxTimer.setStatus(_A)
_RcftRemoteVCGTraps_ObjectIdentity=ObjectIdentity
rcftRemoteVCGTraps=_RcftRemoteVCGTraps_ObjectIdentity((1,3,6,1,4,1,8886,2,1,6,16,10))
rcftRemoteEthFePortEntry.registerAugmentions((_C,_Ab))
rcftRemoteEthFeStatisticEntry.setIndexNames(*rcftRemoteEthFePortEntry.getIndexNames())
rcftRemoteEthFxPortEntry.registerAugmentions((_C,_Ac))
rcftRemoteEthFxStatisticEntry.setIndexNames(*rcftRemoteEthFxPortEntry.getIndexNames())
rcftRemoteDeviceE1Entry.registerAugmentions((_C,_Ad))
rcftRemoteE1StatisticEntry.setIndexNames(*rcftRemoteDeviceE1Entry.getIndexNames())
rcftRemoteDS3E3PortEntry.registerAugmentions((_C,_Ae))
rcftRemoteDS3E3StatisticEntry.setIndexNames(*rcftRemoteDS3E3PortEntry.getIndexNames())
rcftRemoteDS1PortEntry.registerAugmentions((_C,_Af))
rcftRemoteDS1StatisticEntry.setIndexNames(*rcftRemoteDS1PortEntry.getIndexNames())
rcftRemoteMoudleEthFeEntry.registerAugmentions((_C,_Ag))
rcftRemoteMoudleEthFeStatisticEntry.setIndexNames(*rcftRemoteMoudleEthFeEntry.getIndexNames())
rcftRemoteMoudleE1Entry.registerAugmentions((_C,_Ah))
rcftRemoteMoudleE1StatisticEntry.setIndexNames(*rcftRemoteMoudleE1Entry.getIndexNames())
rcftRemoteVCGEntry.registerAugmentions((_C,_Ai))
rcftRemoteVCGStatisticEntry.setIndexNames(*rcftRemoteVCGEntry.getIndexNames())
rcftRemoteDevExistTrap=NotificationType((1,3,6,1,4,1,8886,2,1,6,1,2,1))
rcftRemoteDevExistTrap.setObjects((_C,_Aj))
if mibBuilder.loadTexts:rcftRemoteDevExistTrap.setStatus(_A)
rcftRemoteDevVoltTooHighTrap=NotificationType((1,3,6,1,4,1,8886,2,1,6,1,2,2))
rcftRemoteDevVoltTooHighTrap.setObjects((_C,_p))
if mibBuilder.loadTexts:rcftRemoteDevVoltTooHighTrap.setStatus(_A)
rcftRemoteDevVoltTooLowTrap=NotificationType((1,3,6,1,4,1,8886,2,1,6,1,2,3))
rcftRemoteDevVoltTooLowTrap.setObjects((_C,_p))
if mibBuilder.loadTexts:rcftRemoteDevVoltTooLowTrap.setStatus(_A)
rcftRemoteDevTmptTrap=NotificationType((1,3,6,1,4,1,8886,2,1,6,1,2,4))
rcftRemoteDevTmptTrap.setObjects((_C,_Ak))
if mibBuilder.loadTexts:rcftRemoteDevTmptTrap.setStatus(_A)
rcftRemoteDevPowerDownTrap=NotificationType((1,3,6,1,4,1,8886,2,1,6,1,2,5))
rcftRemoteDevPowerDownTrap.setObjects((_C,_Al))
if mibBuilder.loadTexts:rcftRemoteDevPowerDownTrap.setStatus(_A)
rcftRemoteDevPSChannelTrap=NotificationType((1,3,6,1,4,1,8886,2,1,6,1,2,6))
rcftRemoteDevPSChannelTrap.setObjects((_C,_q))
if mibBuilder.loadTexts:rcftRemoteDevPSChannelTrap.setStatus(_A)
rcftRemoteDevSPChannelTrap=NotificationType((1,3,6,1,4,1,8886,2,1,6,1,2,7))
rcftRemoteDevSPChannelTrap.setObjects((_C,_q))
if mibBuilder.loadTexts:rcftRemoteDevSPChannelTrap.setStatus(_A)
rcftRemoteEthFeLinkTrap=NotificationType((1,3,6,1,4,1,8886,2,1,6,2,1,2,1))
rcftRemoteEthFeLinkTrap.setObjects((_C,_Am))
if mibBuilder.loadTexts:rcftRemoteEthFeLinkTrap.setStatus(_A)
rcftRemoteEthFxPortRLKTrap=NotificationType((1,3,6,1,4,1,8886,2,1,6,2,2,2,1))
rcftRemoteEthFxPortRLKTrap.setObjects((_C,_An))
if mibBuilder.loadTexts:rcftRemoteEthFxPortRLKTrap.setStatus(_A)
rcftRemoteEthFxPortTLKTrap=NotificationType((1,3,6,1,4,1,8886,2,1,6,2,2,2,2))
rcftRemoteEthFxPortTLKTrap.setObjects((_C,_Ao))
if mibBuilder.loadTexts:rcftRemoteEthFxPortTLKTrap.setStatus(_A)
rcftRemoteEthFxPortTxPowerTrap=NotificationType((1,3,6,1,4,1,8886,2,1,6,2,2,2,3))
rcftRemoteEthFxPortTxPowerTrap.setObjects((_C,_Ap))
if mibBuilder.loadTexts:rcftRemoteEthFxPortTxPowerTrap.setStatus(_A)
rcftRemoteEthFxPortRxSensitiveTrap=NotificationType((1,3,6,1,4,1,8886,2,1,6,2,2,2,4))
rcftRemoteEthFxPortRxSensitiveTrap.setObjects((_C,_Aq))
if mibBuilder.loadTexts:rcftRemoteEthFxPortRxSensitiveTrap.setStatus(_A)
rcftRemoteEthFxPortLaserTrap=NotificationType((1,3,6,1,4,1,8886,2,1,6,2,2,2,5))
rcftRemoteEthFxPortLaserTrap.setObjects((_C,_Ar))
if mibBuilder.loadTexts:rcftRemoteEthFxPortLaserTrap.setStatus(_A)
rcftRemoteEthFxPortSDTrap=NotificationType((1,3,6,1,4,1,8886,2,1,6,2,2,2,6))
rcftRemoteEthFxPortSDTrap.setObjects((_C,_As))
if mibBuilder.loadTexts:rcftRemoteEthFxPortSDTrap.setStatus(_A)
rcftRemoteEthFxPortLinkTrap=NotificationType((1,3,6,1,4,1,8886,2,1,6,2,2,2,7))
rcftRemoteEthFxPortLinkTrap.setObjects((_C,_At))
if mibBuilder.loadTexts:rcftRemoteEthFxPortLinkTrap.setStatus(_A)
rcftRemoteEthFxPortExitTrap=NotificationType((1,3,6,1,4,1,8886,2,1,6,2,2,2,8))
rcftRemoteEthFxPortExitTrap.setObjects((_C,_Au))
if mibBuilder.loadTexts:rcftRemoteEthFxPortExitTrap.setStatus(_A)
rcftRemoteEthFxPortTempHighTrap=NotificationType((1,3,6,1,4,1,8886,2,1,6,2,2,2,9))
rcftRemoteEthFxPortTempHighTrap.setObjects((_C,_M))
if mibBuilder.loadTexts:rcftRemoteEthFxPortTempHighTrap.setStatus(_A)
rcftRemoteEthFxPortTempLowTrap=NotificationType((1,3,6,1,4,1,8886,2,1,6,2,2,2,10))
rcftRemoteEthFxPortTempLowTrap.setObjects((_C,_M))
if mibBuilder.loadTexts:rcftRemoteEthFxPortTempLowTrap.setStatus(_A)
rcftRemoteEthFxPortVoltageHighTrap=NotificationType((1,3,6,1,4,1,8886,2,1,6,2,2,2,11))
rcftRemoteEthFxPortVoltageHighTrap.setObjects((_C,_M))
if mibBuilder.loadTexts:rcftRemoteEthFxPortVoltageHighTrap.setStatus(_A)
rcftRemoteEthFxPortVoltageLowTrap=NotificationType((1,3,6,1,4,1,8886,2,1,6,2,2,2,12))
rcftRemoteEthFxPortVoltageLowTrap.setObjects((_C,_M))
if mibBuilder.loadTexts:rcftRemoteEthFxPortVoltageLowTrap.setStatus(_A)
rcftRemoteEthFxPortOffsetCurrHighTrap=NotificationType((1,3,6,1,4,1,8886,2,1,6,2,2,2,13))
rcftRemoteEthFxPortOffsetCurrHighTrap.setObjects((_C,_M))
if mibBuilder.loadTexts:rcftRemoteEthFxPortOffsetCurrHighTrap.setStatus(_A)
rcftRemoteEthFxPortOffsetCurrLowTrap=NotificationType((1,3,6,1,4,1,8886,2,1,6,2,2,2,14))
rcftRemoteEthFxPortOffsetCurrLowTrap.setObjects((_C,_M))
if mibBuilder.loadTexts:rcftRemoteEthFxPortOffsetCurrLowTrap.setStatus(_A)
rcftRemoteEthFxPortSendPowerHighTrap=NotificationType((1,3,6,1,4,1,8886,2,1,6,2,2,2,15))
rcftRemoteEthFxPortSendPowerHighTrap.setObjects((_C,_M))
if mibBuilder.loadTexts:rcftRemoteEthFxPortSendPowerHighTrap.setStatus(_A)
rcftRemoteEthFxPortSendPowerLowTrap=NotificationType((1,3,6,1,4,1,8886,2,1,6,2,2,2,16))
rcftRemoteEthFxPortSendPowerLowTrap.setObjects((_C,_M))
if mibBuilder.loadTexts:rcftRemoteEthFxPortSendPowerLowTrap.setStatus(_A)
rcftRemoteEthFxPortRecvPowerHighTrap=NotificationType((1,3,6,1,4,1,8886,2,1,6,2,2,2,17))
rcftRemoteEthFxPortRecvPowerHighTrap.setObjects((_C,_M))
if mibBuilder.loadTexts:rcftRemoteEthFxPortRecvPowerHighTrap.setStatus(_A)
rcftRemoteEthFxPortRecvPowerLowTrap=NotificationType((1,3,6,1,4,1,8886,2,1,6,2,2,2,18))
rcftRemoteEthFxPortRecvPowerLowTrap.setObjects((_C,_M))
if mibBuilder.loadTexts:rcftRemoteEthFxPortRecvPowerLowTrap.setStatus(_A)
rcftRemoteEthFxPortRemotePowerDownTrap=NotificationType((1,3,6,1,4,1,8886,2,1,6,2,2,2,19))
rcftRemoteEthFxPortRemotePowerDownTrap.setObjects((_C,_M))
if mibBuilder.loadTexts:rcftRemoteEthFxPortRemotePowerDownTrap.setStatus(_A)
rcftRemoteEthFxPortInputSignalLosTrap=NotificationType((1,3,6,1,4,1,8886,2,1,6,2,2,2,20))
rcftRemoteEthFxPortInputSignalLosTrap.setObjects((_C,_Av))
if mibBuilder.loadTexts:rcftRemoteEthFxPortInputSignalLosTrap.setStatus(_A)
rcftRemoteEthFxPortTempHighWarnning=NotificationType((1,3,6,1,4,1,8886,2,1,6,2,2,2,21))
rcftRemoteEthFxPortTempHighWarnning.setObjects((_C,_M))
if mibBuilder.loadTexts:rcftRemoteEthFxPortTempHighWarnning.setStatus(_A)
rcftRemoteEthFxPortTempLowWarning=NotificationType((1,3,6,1,4,1,8886,2,1,6,2,2,2,22))
rcftRemoteEthFxPortTempLowWarning.setObjects((_C,_R))
if mibBuilder.loadTexts:rcftRemoteEthFxPortTempLowWarning.setStatus(_A)
rcftRemoteEthFxPortVoltageHighWarning=NotificationType((1,3,6,1,4,1,8886,2,1,6,2,2,2,23))
rcftRemoteEthFxPortVoltageHighWarning.setObjects((_C,_R))
if mibBuilder.loadTexts:rcftRemoteEthFxPortVoltageHighWarning.setStatus(_A)
rcftRemoteEthFxPortVoltageLowWarning=NotificationType((1,3,6,1,4,1,8886,2,1,6,2,2,2,24))
rcftRemoteEthFxPortVoltageLowWarning.setObjects((_C,_R))
if mibBuilder.loadTexts:rcftRemoteEthFxPortVoltageLowWarning.setStatus(_A)
rcftRemoteEthFxPortOffsetCurrHighWarning=NotificationType((1,3,6,1,4,1,8886,2,1,6,2,2,2,25))
rcftRemoteEthFxPortOffsetCurrHighWarning.setObjects((_C,_R))
if mibBuilder.loadTexts:rcftRemoteEthFxPortOffsetCurrHighWarning.setStatus(_A)
rcftRemoteEthFxPortOffsetCurrLowWarning=NotificationType((1,3,6,1,4,1,8886,2,1,6,2,2,2,26))
rcftRemoteEthFxPortOffsetCurrLowWarning.setObjects((_C,_R))
if mibBuilder.loadTexts:rcftRemoteEthFxPortOffsetCurrLowWarning.setStatus(_A)
rcftRemoteEthFxPortSendPowerHighWarning=NotificationType((1,3,6,1,4,1,8886,2,1,6,2,2,2,27))
rcftRemoteEthFxPortSendPowerHighWarning.setObjects((_C,_R))
if mibBuilder.loadTexts:rcftRemoteEthFxPortSendPowerHighWarning.setStatus(_A)
rcftRemoteEthFxPortSendPowerLowWarning=NotificationType((1,3,6,1,4,1,8886,2,1,6,2,2,2,28))
rcftRemoteEthFxPortSendPowerLowWarning.setObjects((_C,_R))
if mibBuilder.loadTexts:rcftRemoteEthFxPortSendPowerLowWarning.setStatus(_A)
rcftRemoteEthFxPortRecvPowerHighWarning=NotificationType((1,3,6,1,4,1,8886,2,1,6,2,2,2,29))
rcftRemoteEthFxPortRecvPowerHighWarning.setObjects((_C,_R))
if mibBuilder.loadTexts:rcftRemoteEthFxPortRecvPowerHighWarning.setStatus(_A)
rcftRemoteEthFxPortRecvPowerLowWarning=NotificationType((1,3,6,1,4,1,8886,2,1,6,2,2,2,30))
rcftRemoteEthFxPortRecvPowerLowWarning.setObjects((_C,_R))
if mibBuilder.loadTexts:rcftRemoteEthFxPortRecvPowerLowWarning.setStatus(_A)
rcftRemoteDevE1LOSTRAP=NotificationType((1,3,6,1,4,1,8886,2,1,6,3,2,1))
rcftRemoteDevE1LOSTRAP.setObjects((_C,_Q))
if mibBuilder.loadTexts:rcftRemoteDevE1LOSTRAP.setStatus(_A)
rcftRemoteDevE1LOFTRAP=NotificationType((1,3,6,1,4,1,8886,2,1,6,3,2,2))
rcftRemoteDevE1LOFTRAP.setObjects((_C,_Q))
if mibBuilder.loadTexts:rcftRemoteDevE1LOFTRAP.setStatus(_A)
rcftRemoteDevE1CRCTRAP=NotificationType((1,3,6,1,4,1,8886,2,1,6,3,2,3))
rcftRemoteDevE1CRCTRAP.setObjects((_C,_Q))
if mibBuilder.loadTexts:rcftRemoteDevE1CRCTRAP.setStatus(_A)
rcftRemoteDevE1AISTrap=NotificationType((1,3,6,1,4,1,8886,2,1,6,3,2,4))
rcftRemoteDevE1AISTrap.setObjects((_C,_Q))
if mibBuilder.loadTexts:rcftRemoteDevE1AISTrap.setStatus(_A)
rcftRemoteDevE1TransErrorCodeMore10E_3=NotificationType((1,3,6,1,4,1,8886,2,1,6,3,2,5))
rcftRemoteDevE1TransErrorCodeMore10E_3.setObjects((_C,_r))
if mibBuilder.loadTexts:rcftRemoteDevE1TransErrorCodeMore10E_3.setStatus(_A)
rcftRemoteDevE1TransErrorCodeMore10E_6=NotificationType((1,3,6,1,4,1,8886,2,1,6,3,2,6))
rcftRemoteDevE1TransErrorCodeMore10E_6.setObjects((_C,_r))
if mibBuilder.loadTexts:rcftRemoteDevE1TransErrorCodeMore10E_6.setStatus(_A)
rcftRemoteDevToLocalDevE1LOSTRAP=NotificationType((1,3,6,1,4,1,8886,2,1,6,3,2,7))
rcftRemoteDevToLocalDevE1LOSTRAP.setObjects((_C,_c))
if mibBuilder.loadTexts:rcftRemoteDevToLocalDevE1LOSTRAP.setStatus(_A)
rcftRemoteDevToLocalDevE1LOFTRAP=NotificationType((1,3,6,1,4,1,8886,2,1,6,3,2,8))
rcftRemoteDevToLocalDevE1LOFTRAP.setObjects((_C,_c))
if mibBuilder.loadTexts:rcftRemoteDevToLocalDevE1LOFTRAP.setStatus(_A)
rcftRemoteDevToLocalDevE1CRCTRAP=NotificationType((1,3,6,1,4,1,8886,2,1,6,3,2,9))
rcftRemoteDevToLocalDevE1CRCTRAP.setObjects((_C,_c))
if mibBuilder.loadTexts:rcftRemoteDevToLocalDevE1CRCTRAP.setStatus(_A)
rcftRemoteDevToLocalDevE1AISTrap=NotificationType((1,3,6,1,4,1,8886,2,1,6,3,2,10))
rcftRemoteDevToLocalDevE1AISTrap.setObjects((_C,_c))
if mibBuilder.loadTexts:rcftRemoteDevToLocalDevE1AISTrap.setStatus(_A)
rcftRemoteDevE1CVTrap=NotificationType((1,3,6,1,4,1,8886,2,1,6,3,2,11))
rcftRemoteDevE1CVTrap.setObjects((_C,_Q))
if mibBuilder.loadTexts:rcftRemoteDevE1CVTrap.setStatus(_A)
rcftRemoteDevE1LOMFTrap=NotificationType((1,3,6,1,4,1,8886,2,1,6,3,2,12))
rcftRemoteDevE1LOMFTrap.setObjects((_C,_Q))
if mibBuilder.loadTexts:rcftRemoteDevE1LOMFTrap.setStatus(_A)
rcftRemoteDevT1LOSTrap=NotificationType((1,3,6,1,4,1,8886,2,1,6,3,2,13))
rcftRemoteDevT1LOSTrap.setObjects((_C,_s))
if mibBuilder.loadTexts:rcftRemoteDevT1LOSTrap.setStatus(_A)
rcftRemoteDevT1AISTrap=NotificationType((1,3,6,1,4,1,8886,2,1,6,3,2,14))
rcftRemoteDevT1AISTrap.setObjects((_C,_s))
if mibBuilder.loadTexts:rcftRemoteDevT1AISTrap.setStatus(_A)
rcftRemoteDevE1TSDTrap=NotificationType((1,3,6,1,4,1,8886,2,1,6,3,2,15))
rcftRemoteDevE1TSDTrap.setObjects((_C,_Q))
if mibBuilder.loadTexts:rcftRemoteDevE1TSDTrap.setStatus(_A)
rcftRemoteE1PortToLTSDTrap=NotificationType((1,3,6,1,4,1,8886,2,1,6,3,2,16))
rcftRemoteE1PortToLTSDTrap.setObjects((_C,_Q))
if mibBuilder.loadTexts:rcftRemoteE1PortToLTSDTrap.setStatus(_A)
rcftRemoteDevE1RDITrap=NotificationType((1,3,6,1,4,1,8886,2,1,6,3,2,17))
rcftRemoteDevE1RDITrap.setObjects((_C,_Q))
if mibBuilder.loadTexts:rcftRemoteDevE1RDITrap.setStatus(_A)
rcftRemoteE1PortToLLOMFTrap=NotificationType((1,3,6,1,4,1,8886,2,1,6,3,2,18))
rcftRemoteE1PortToLLOMFTrap.setObjects((_C,_Q))
if mibBuilder.loadTexts:rcftRemoteE1PortToLLOMFTrap.setStatus(_A)
rcftRemoteSHDSLPortLOSTrap=NotificationType((1,3,6,1,4,1,8886,2,1,6,4,10,1))
rcftRemoteSHDSLPortLOSTrap.setObjects((_C,_X))
if mibBuilder.loadTexts:rcftRemoteSHDSLPortLOSTrap.setStatus(_A)
rcftRemoteSHDSLPortLOSWTrap=NotificationType((1,3,6,1,4,1,8886,2,1,6,4,10,2))
rcftRemoteSHDSLPortLOSWTrap.setObjects((_C,_X))
if mibBuilder.loadTexts:rcftRemoteSHDSLPortLOSWTrap.setStatus(_A)
rcftRemoteSHDSLPortLINKTrap=NotificationType((1,3,6,1,4,1,8886,2,1,6,4,10,3))
rcftRemoteSHDSLPortLINKTrap.setObjects((_C,_X))
if mibBuilder.loadTexts:rcftRemoteSHDSLPortLINKTrap.setStatus(_A)
rcftRemoteSHDSLPortFECTrap=NotificationType((1,3,6,1,4,1,8886,2,1,6,4,10,4))
rcftRemoteSHDSLPortFECTrap.setObjects((_C,_X))
if mibBuilder.loadTexts:rcftRemoteSHDSLPortFECTrap.setStatus(_A)
rcftRemoteSHDSLPortCRCTrap=NotificationType((1,3,6,1,4,1,8886,2,1,6,4,10,5))
rcftRemoteSHDSLPortCRCTrap.setObjects((_C,_X))
if mibBuilder.loadTexts:rcftRemoteSHDSLPortCRCTrap.setStatus(_A)
rcftRemoteSHDSLPortSNRThresholdTrap=NotificationType((1,3,6,1,4,1,8886,2,1,6,4,10,6))
rcftRemoteSHDSLPortSNRThresholdTrap.setObjects((_C,_Aw))
if mibBuilder.loadTexts:rcftRemoteSHDSLPortSNRThresholdTrap.setStatus(_A)
rcftRemoteSHDSLPortAttenuationThresholdTrap=NotificationType((1,3,6,1,4,1,8886,2,1,6,4,10,7))
rcftRemoteSHDSLPortAttenuationThresholdTrap.setObjects((_C,_Ax))
if mibBuilder.loadTexts:rcftRemoteSHDSLPortAttenuationThresholdTrap.setStatus(_A)
rcftRemoteSHDSLPortLOSThresholdTrap=NotificationType((1,3,6,1,4,1,8886,2,1,6,4,10,8))
rcftRemoteSHDSLPortLOSThresholdTrap.setObjects((_C,_Ay))
if mibBuilder.loadTexts:rcftRemoteSHDSLPortLOSThresholdTrap.setStatus(_A)
rcftRemoteSHDSLPortLOSWThresholdTrap=NotificationType((1,3,6,1,4,1,8886,2,1,6,4,10,9))
rcftRemoteSHDSLPortLOSWThresholdTrap.setObjects((_C,_Az))
if mibBuilder.loadTexts:rcftRemoteSHDSLPortLOSWThresholdTrap.setStatus(_A)
rcftRemoteSHDSLPortLOLKThresholdTrap=NotificationType((1,3,6,1,4,1,8886,2,1,6,4,10,10))
rcftRemoteSHDSLPortLOLKThresholdTrap.setObjects((_C,_A_))
if mibBuilder.loadTexts:rcftRemoteSHDSLPortLOLKThresholdTrap.setStatus(_A)
rcftRemoteSHDSLPortESThresholdTrap=NotificationType((1,3,6,1,4,1,8886,2,1,6,4,10,11))
rcftRemoteSHDSLPortESThresholdTrap.setObjects((_C,_B0))
if mibBuilder.loadTexts:rcftRemoteSHDSLPortESThresholdTrap.setStatus(_A)
rcftRemoteV35PortDCDTrap=NotificationType((1,3,6,1,4,1,8886,2,1,6,5,3,1))
rcftRemoteV35PortDCDTrap.setObjects((_C,_L))
if mibBuilder.loadTexts:rcftRemoteV35PortDCDTrap.setStatus(_A)
rcftRemoteV35PortCTSTrap=NotificationType((1,3,6,1,4,1,8886,2,1,6,5,3,2))
rcftRemoteV35PortCTSTrap.setObjects((_C,_L))
if mibBuilder.loadTexts:rcftRemoteV35PortCTSTrap.setStatus(_A)
rcftRemoteV35PortDTRTrap=NotificationType((1,3,6,1,4,1,8886,2,1,6,5,3,3))
rcftRemoteV35PortDTRTrap.setObjects((_C,_L))
if mibBuilder.loadTexts:rcftRemoteV35PortDTRTrap.setStatus(_A)
rcftRemoteV35PortRTSTrap=NotificationType((1,3,6,1,4,1,8886,2,1,6,5,3,4))
rcftRemoteV35PortRTSTrap.setObjects((_C,_L))
if mibBuilder.loadTexts:rcftRemoteV35PortRTSTrap.setStatus(_A)
rcftRemoteV35PortCRCTrap=NotificationType((1,3,6,1,4,1,8886,2,1,6,5,3,5))
rcftRemoteV35PortCRCTrap.setObjects((_C,_L))
if mibBuilder.loadTexts:rcftRemoteV35PortCRCTrap.setStatus(_A)
rcftRemoteV35PortPATTTrap=NotificationType((1,3,6,1,4,1,8886,2,1,6,5,3,6))
rcftRemoteV35PortPATTTrap.setObjects((_C,_L))
if mibBuilder.loadTexts:rcftRemoteV35PortPATTTrap.setStatus(_A)
rcftRemoteV35PortLOFTrap=NotificationType((1,3,6,1,4,1,8886,2,1,6,5,3,7))
rcftRemoteV35PortLOFTrap.setObjects((_C,_L))
if mibBuilder.loadTexts:rcftRemoteV35PortLOFTrap.setStatus(_A)
rcftRemoteV35PortCVTrap=NotificationType((1,3,6,1,4,1,8886,2,1,6,5,3,8))
rcftRemoteV35PortCVTrap.setObjects((_C,_L))
if mibBuilder.loadTexts:rcftRemoteV35PortCVTrap.setStatus(_A)
rcftRemoteV35PortAISTrap=NotificationType((1,3,6,1,4,1,8886,2,1,6,5,3,9))
rcftRemoteV35PortAISTrap.setObjects((_C,_L))
if mibBuilder.loadTexts:rcftRemoteV35PortAISTrap.setStatus(_A)
rcftRemoteV35PortToLLOFTrap=NotificationType((1,3,6,1,4,1,8886,2,1,6,5,3,10))
rcftRemoteV35PortToLLOFTrap.setObjects((_C,_L))
if mibBuilder.loadTexts:rcftRemoteV35PortToLLOFTrap.setStatus(_A)
rcftRemoteV35PortToLCVTrap=NotificationType((1,3,6,1,4,1,8886,2,1,6,5,3,11))
rcftRemoteV35PortToLCVTrap.setObjects((_C,_L))
if mibBuilder.loadTexts:rcftRemoteV35PortToLCVTrap.setStatus(_A)
rcftRemoteV35PortToLAISTrap=NotificationType((1,3,6,1,4,1,8886,2,1,6,5,3,12))
rcftRemoteV35PortToLAISTrap.setObjects((_C,_L))
if mibBuilder.loadTexts:rcftRemoteV35PortToLAISTrap.setStatus(_A)
rcftRemoteV35PortDSRTrap=NotificationType((1,3,6,1,4,1,8886,2,1,6,5,3,13))
rcftRemoteV35PortDSRTrap.setObjects((_C,_L))
if mibBuilder.loadTexts:rcftRemoteV35PortDSRTrap.setStatus(_A)
rcftRemoteDS3E3PortAISTrap=NotificationType((1,3,6,1,4,1,8886,2,1,6,6,10,1))
rcftRemoteDS3E3PortAISTrap.setObjects((_C,_K))
if mibBuilder.loadTexts:rcftRemoteDS3E3PortAISTrap.setStatus(_A)
rcftRemoteDS3E3PortLOSTrap=NotificationType((1,3,6,1,4,1,8886,2,1,6,6,10,2))
rcftRemoteDS3E3PortLOSTrap.setObjects((_C,_K))
if mibBuilder.loadTexts:rcftRemoteDS3E3PortLOSTrap.setStatus(_A)
rcftRemoteDS3E3PortLOLTrap=NotificationType((1,3,6,1,4,1,8886,2,1,6,6,10,3))
rcftRemoteDS3E3PortLOLTrap.setObjects((_C,_K))
if mibBuilder.loadTexts:rcftRemoteDS3E3PortLOLTrap.setStatus(_A)
rcftRemoteDS3E3PortDMOTrap=NotificationType((1,3,6,1,4,1,8886,2,1,6,6,10,4))
rcftRemoteDS3E3PortDMOTrap.setObjects((_C,_K))
if mibBuilder.loadTexts:rcftRemoteDS3E3PortDMOTrap.setStatus(_A)
rcftRemoteDS3E3PortCVTrap=NotificationType((1,3,6,1,4,1,8886,2,1,6,6,10,5))
rcftRemoteDS3E3PortCVTrap.setObjects((_C,_K))
if mibBuilder.loadTexts:rcftRemoteDS3E3PortCVTrap.setStatus(_A)
rcftRemoteDS3E3PortCRCTrap=NotificationType((1,3,6,1,4,1,8886,2,1,6,6,10,6))
rcftRemoteDS3E3PortCRCTrap.setObjects((_C,_K))
if mibBuilder.loadTexts:rcftRemoteDS3E3PortCRCTrap.setStatus(_A)
rcftRemoteDS3E3PortToLAISTrap=NotificationType((1,3,6,1,4,1,8886,2,1,6,6,10,7))
rcftRemoteDS3E3PortToLAISTrap.setObjects((_C,_K))
if mibBuilder.loadTexts:rcftRemoteDS3E3PortToLAISTrap.setStatus(_A)
rcftRemoteDS3E3PortToLLOSTrap=NotificationType((1,3,6,1,4,1,8886,2,1,6,6,10,8))
rcftRemoteDS3E3PortToLLOSTrap.setObjects((_C,_K))
if mibBuilder.loadTexts:rcftRemoteDS3E3PortToLLOSTrap.setStatus(_A)
rcftRemoteDS3E3PortToLLOLTrap=NotificationType((1,3,6,1,4,1,8886,2,1,6,6,10,9))
rcftRemoteDS3E3PortToLLOLTrap.setObjects((_C,_K))
if mibBuilder.loadTexts:rcftRemoteDS3E3PortToLLOLTrap.setStatus(_A)
rcftRemoteDS3E3PortToLDMOTrap=NotificationType((1,3,6,1,4,1,8886,2,1,6,6,10,10))
rcftRemoteDS3E3PortToLDMOTrap.setObjects((_C,_K))
if mibBuilder.loadTexts:rcftRemoteDS3E3PortToLDMOTrap.setStatus(_A)
rcftRemoteDS3E3PortToLCVTrap=NotificationType((1,3,6,1,4,1,8886,2,1,6,6,10,11))
rcftRemoteDS3E3PortToLCVTrap.setObjects((_C,_K))
if mibBuilder.loadTexts:rcftRemoteDS3E3PortToLCVTrap.setStatus(_A)
rcftRemoteDS3E3PortToLCRCTrap=NotificationType((1,3,6,1,4,1,8886,2,1,6,6,10,12))
rcftRemoteDS3E3PortToLCRCTrap.setObjects((_C,_K))
if mibBuilder.loadTexts:rcftRemoteDS3E3PortToLCRCTrap.setStatus(_A)
rcftRemoteDS3E3PortLOFTrap=NotificationType((1,3,6,1,4,1,8886,2,1,6,6,10,13))
rcftRemoteDS3E3PortLOFTrap.setObjects((_C,_K))
if mibBuilder.loadTexts:rcftRemoteDS3E3PortLOFTrap.setStatus(_A)
rcftRemoteDS3E3PortToLLOFTrap=NotificationType((1,3,6,1,4,1,8886,2,1,6,6,10,14))
rcftRemoteDS3E3PortToLLOFTrap.setObjects((_C,_K))
if mibBuilder.loadTexts:rcftRemoteDS3E3PortToLLOFTrap.setStatus(_A)
rcftRemoteDS3E3PortRAITrap=NotificationType((1,3,6,1,4,1,8886,2,1,6,6,10,15))
rcftRemoteDS3E3PortRAITrap.setObjects((_C,_K))
if mibBuilder.loadTexts:rcftRemoteDS3E3PortRAITrap.setStatus(_A)
rcftRemoteDS3E3PortToLRAITrap=NotificationType((1,3,6,1,4,1,8886,2,1,6,6,10,16))
rcftRemoteDS3E3PortToLRAITrap.setObjects((_C,_K))
if mibBuilder.loadTexts:rcftRemoteDS3E3PortToLRAITrap.setStatus(_A)
rcftRemoteDS3E3PortOOFTrap=NotificationType((1,3,6,1,4,1,8886,2,1,6,6,10,17))
rcftRemoteDS3E3PortOOFTrap.setObjects((_C,_K))
if mibBuilder.loadTexts:rcftRemoteDS3E3PortOOFTrap.setStatus(_A)
rcftRemoteDS3E3PortToLOOFTrap=NotificationType((1,3,6,1,4,1,8886,2,1,6,6,10,18))
rcftRemoteDS3E3PortToLOOFTrap.setObjects((_C,_K))
if mibBuilder.loadTexts:rcftRemoteDS3E3PortToLOOFTrap.setStatus(_A)
rcftRemotePdhPortLOSTrap=NotificationType((1,3,6,1,4,1,8886,2,1,6,7,10,1))
rcftRemotePdhPortLOSTrap.setObjects((_C,_S))
if mibBuilder.loadTexts:rcftRemotePdhPortLOSTrap.setStatus(_A)
rcftRemotePdhPortLOFTrap=NotificationType((1,3,6,1,4,1,8886,2,1,6,7,10,2))
rcftRemotePdhPortLOFTrap.setObjects((_C,_S))
if mibBuilder.loadTexts:rcftRemotePdhPortLOFTrap.setStatus(_A)
rcftRemotePdhPortE3Trap=NotificationType((1,3,6,1,4,1,8886,2,1,6,7,10,3))
rcftRemotePdhPortE3Trap.setObjects((_C,_S))
if mibBuilder.loadTexts:rcftRemotePdhPortE3Trap.setStatus(_A)
rcftRemotePdhPortE6Trap=NotificationType((1,3,6,1,4,1,8886,2,1,6,7,10,4))
rcftRemotePdhPortE6Trap.setObjects((_C,_S))
if mibBuilder.loadTexts:rcftRemotePdhPortE6Trap.setStatus(_A)
rcftRemotePdhPortToLLOSTrap=NotificationType((1,3,6,1,4,1,8886,2,1,6,7,10,5))
rcftRemotePdhPortToLLOSTrap.setObjects((_C,_S))
if mibBuilder.loadTexts:rcftRemotePdhPortToLLOSTrap.setStatus(_A)
rcftRemotePdhPortToLLOFTrap=NotificationType((1,3,6,1,4,1,8886,2,1,6,7,10,6))
rcftRemotePdhPortToLLOFTrap.setObjects((_C,_S))
if mibBuilder.loadTexts:rcftRemotePdhPortToLLOFTrap.setStatus(_A)
rcftRemotePdhPortToLE3Trap=NotificationType((1,3,6,1,4,1,8886,2,1,6,7,10,7))
rcftRemotePdhPortToLE3Trap.setObjects((_C,_S))
if mibBuilder.loadTexts:rcftRemotePdhPortToLE3Trap.setStatus(_A)
rcftRemotePdhPortToLE6rap=NotificationType((1,3,6,1,4,1,8886,2,1,6,7,10,8))
rcftRemotePdhPortToLE6rap.setObjects((_C,_S))
if mibBuilder.loadTexts:rcftRemotePdhPortToLE6rap.setStatus(_A)
rcftRemotePdhPortToRPowerDown=NotificationType((1,3,6,1,4,1,8886,2,1,6,7,10,9))
rcftRemotePdhPortToRPowerDown.setObjects((_C,_S))
if mibBuilder.loadTexts:rcftRemotePdhPortToRPowerDown.setStatus(_A)
rcftRemoteDS1PortAISTrap=NotificationType((1,3,6,1,4,1,8886,2,1,6,8,10,1))
rcftRemoteDS1PortAISTrap.setObjects((_C,_N))
if mibBuilder.loadTexts:rcftRemoteDS1PortAISTrap.setStatus(_A)
rcftRemoteDS1PortLOSTrap=NotificationType((1,3,6,1,4,1,8886,2,1,6,8,10,2))
rcftRemoteDS1PortLOSTrap.setObjects((_C,_N))
if mibBuilder.loadTexts:rcftRemoteDS1PortLOSTrap.setStatus(_A)
rcftRemoteDS1PortToLAISTrap=NotificationType((1,3,6,1,4,1,8886,2,1,6,8,10,3))
rcftRemoteDS1PortToLAISTrap.setObjects((_C,_N))
if mibBuilder.loadTexts:rcftRemoteDS1PortToLAISTrap.setStatus(_A)
rcftRemoteDS1PortToLLOSTrap=NotificationType((1,3,6,1,4,1,8886,2,1,6,8,10,4))
rcftRemoteDS1PortToLLOSTrap.setObjects((_C,_N))
if mibBuilder.loadTexts:rcftRemoteDS1PortToLLOSTrap.setStatus(_A)
rcftRemoteDS1PortLOFTrap=NotificationType((1,3,6,1,4,1,8886,2,1,6,8,10,5))
rcftRemoteDS1PortLOFTrap.setObjects((_C,_N))
if mibBuilder.loadTexts:rcftRemoteDS1PortLOFTrap.setStatus(_A)
rcftRemoteDS1PortCRCTrap=NotificationType((1,3,6,1,4,1,8886,2,1,6,8,10,6))
rcftRemoteDS1PortCRCTrap.setObjects((_C,_N))
if mibBuilder.loadTexts:rcftRemoteDS1PortCRCTrap.setStatus(_A)
rcftRemoteDS1PortToLLOFTrap=NotificationType((1,3,6,1,4,1,8886,2,1,6,8,10,7))
rcftRemoteDS1PortToLLOFTrap.setObjects((_C,_N))
if mibBuilder.loadTexts:rcftRemoteDS1PortToLLOFTrap.setStatus(_A)
rcftRemoteDS1PortToLCRCTrap=NotificationType((1,3,6,1,4,1,8886,2,1,6,8,10,8))
rcftRemoteDS1PortToLCRCTrap.setObjects((_C,_N))
if mibBuilder.loadTexts:rcftRemoteDS1PortToLCRCTrap.setStatus(_A)
rcftRemoteDS1PortFaultPassIndicatorTrap=NotificationType((1,3,6,1,4,1,8886,2,1,6,8,10,9))
rcftRemoteDS1PortFaultPassIndicatorTrap.setObjects((_C,_B1))
if mibBuilder.loadTexts:rcftRemoteDS1PortFaultPassIndicatorTrap.setStatus(_A)
rcftRemoteDS1PortDMOTrap=NotificationType((1,3,6,1,4,1,8886,2,1,6,8,10,10))
rcftRemoteDS1PortDMOTrap.setObjects((_C,_N))
if mibBuilder.loadTexts:rcftRemoteDS1PortDMOTrap.setStatus(_A)
rcftRemoteDS1PortCVTrap=NotificationType((1,3,6,1,4,1,8886,2,1,6,8,10,11))
rcftRemoteDS1PortCVTrap.setObjects((_C,_N))
if mibBuilder.loadTexts:rcftRemoteDS1PortCVTrap.setStatus(_A)
rcftRemoteDS1PortYELTrap=NotificationType((1,3,6,1,4,1,8886,2,1,6,8,10,12))
rcftRemoteDS1PortYELTrap.setObjects((_C,_N))
if mibBuilder.loadTexts:rcftRemoteDS1PortYELTrap.setStatus(_A)
rcftRemoteDS1PortREDTrap=NotificationType((1,3,6,1,4,1,8886,2,1,6,8,10,13))
rcftRemoteDS1PortREDTrap.setObjects((_C,_N))
if mibBuilder.loadTexts:rcftRemoteDS1PortREDTrap.setStatus(_A)
rcftRemoteMoudleExistTrap=NotificationType((1,3,6,1,4,1,8886,2,1,6,9,1,10,1))
rcftRemoteMoudleExistTrap.setObjects((_C,_B2))
if mibBuilder.loadTexts:rcftRemoteMoudleExistTrap.setStatus(_A)
rcftRemoteMoudleEthFeLinkTrap=NotificationType((1,3,6,1,4,1,8886,2,1,6,9,2,10,1))
rcftRemoteMoudleEthFeLinkTrap.setObjects((_C,_B3))
if mibBuilder.loadTexts:rcftRemoteMoudleEthFeLinkTrap.setStatus(_A)
rcftRemoteMoudlePdhLOSTrap=NotificationType((1,3,6,1,4,1,8886,2,1,6,9,3,10,1))
rcftRemoteMoudlePdhLOSTrap.setObjects((_C,_t))
if mibBuilder.loadTexts:rcftRemoteMoudlePdhLOSTrap.setStatus(_A)
rcftRemoteMoudlePdhLOFTrap=NotificationType((1,3,6,1,4,1,8886,2,1,6,9,3,10,2))
rcftRemoteMoudlePdhLOFTrap.setObjects((_C,_t))
if mibBuilder.loadTexts:rcftRemoteMoudlePdhLOFTrap.setStatus(_A)
rcftRemoteMoudleE1LOSTrap=NotificationType((1,3,6,1,4,1,8886,2,1,6,9,4,10,1))
rcftRemoteMoudleE1LOSTrap.setObjects((_C,_Y))
if mibBuilder.loadTexts:rcftRemoteMoudleE1LOSTrap.setStatus(_A)
rcftRemoteMoudleE1AISTrap=NotificationType((1,3,6,1,4,1,8886,2,1,6,9,4,10,2))
rcftRemoteMoudleE1AISTrap.setObjects((_C,_Y))
if mibBuilder.loadTexts:rcftRemoteMoudleE1AISTrap.setStatus(_A)
rcftRemoteMoudleE1CRCTrap=NotificationType((1,3,6,1,4,1,8886,2,1,6,9,4,10,3))
rcftRemoteMoudleE1CRCTrap.setObjects((_C,_Y))
if mibBuilder.loadTexts:rcftRemoteMoudleE1CRCTrap.setStatus(_A)
rcftRemoteMoudleE1CVTrap=NotificationType((1,3,6,1,4,1,8886,2,1,6,9,4,10,4))
rcftRemoteMoudleE1CVTrap.setObjects((_C,_Y))
if mibBuilder.loadTexts:rcftRemoteMoudleE1CVTrap.setStatus(_A)
rcftRemoteMoudleE1LOFTrap=NotificationType((1,3,6,1,4,1,8886,2,1,6,9,4,10,5))
rcftRemoteMoudleE1LOFTrap.setObjects((_C,_Y))
if mibBuilder.loadTexts:rcftRemoteMoudleE1LOFTrap.setStatus(_A)
rcftRemoteMoudleE1ErrorCodeTrap=NotificationType((1,3,6,1,4,1,8886,2,1,6,9,4,10,6))
rcftRemoteMoudleE1ErrorCodeTrap.setObjects((_C,_B4))
if mibBuilder.loadTexts:rcftRemoteMoudleE1ErrorCodeTrap.setStatus(_A)
rcftRemoteVideoPortSignalLos=NotificationType((1,3,6,1,4,1,8886,2,1,6,11,10,1))
rcftRemoteVideoPortSignalLos.setObjects((_C,_f))
if mibBuilder.loadTexts:rcftRemoteVideoPortSignalLos.setStatus(_A)
rcftRemoteVideoPortSignalInLos=NotificationType((1,3,6,1,4,1,8886,2,1,6,11,10,2))
rcftRemoteVideoPortSignalInLos.setObjects((_C,_f))
if mibBuilder.loadTexts:rcftRemoteVideoPortSignalInLos.setStatus(_A)
rcftRemoteVideoPortSignalOutLos=NotificationType((1,3,6,1,4,1,8886,2,1,6,11,10,3))
rcftRemoteVideoPortSignalOutLos.setObjects((_C,_f))
if mibBuilder.loadTexts:rcftRemoteVideoPortSignalOutLos.setStatus(_A)
rcftRemoteVCGGIDTraps=NotificationType((1,3,6,1,4,1,8886,2,1,6,16,10,1))
rcftRemoteVCGGIDTraps.setObjects((_C,_T))
if mibBuilder.loadTexts:rcftRemoteVCGGIDTraps.setStatus(_A)
rcftRemoteVCGLOATraps=NotificationType((1,3,6,1,4,1,8886,2,1,6,16,10,2))
rcftRemoteVCGLOATraps.setObjects((_C,_T))
if mibBuilder.loadTexts:rcftRemoteVCGLOATraps.setStatus(_A)
rcftRemoteVCGLFDTraps=NotificationType((1,3,6,1,4,1,8886,2,1,6,16,10,3))
rcftRemoteVCGLFDTraps.setObjects((_C,_T))
if mibBuilder.loadTexts:rcftRemoteVCGLFDTraps.setStatus(_A)
rcftRemoteVCGCSFTraps=NotificationType((1,3,6,1,4,1,8886,2,1,6,16,10,4))
rcftRemoteVCGCSFTraps.setObjects((_C,_T))
if mibBuilder.loadTexts:rcftRemoteVCGCSFTraps.setStatus(_A)
rcftRemoteVCGTLCTTraps=NotificationType((1,3,6,1,4,1,8886,2,1,6,16,10,5))
rcftRemoteVCGTLCTTraps.setObjects((_C,_T))
if mibBuilder.loadTexts:rcftRemoteVCGTLCTTraps.setStatus(_A)
rcftRemoteVCGTLCRTraps=NotificationType((1,3,6,1,4,1,8886,2,1,6,16,10,6))
rcftRemoteVCGTLCRTraps.setObjects((_C,_T))
if mibBuilder.loadTexts:rcftRemoteVCGTLCRTraps.setStatus(_A)
rcftRemoteVCGToLGIDTraps=NotificationType((1,3,6,1,4,1,8886,2,1,6,16,10,7))
rcftRemoteVCGToLGIDTraps.setObjects((_C,_T))
if mibBuilder.loadTexts:rcftRemoteVCGToLGIDTraps.setStatus(_A)
rcftRemoteVCGToLLOATraps=NotificationType((1,3,6,1,4,1,8886,2,1,6,16,10,8))
rcftRemoteVCGToLLOATraps.setObjects((_C,_T))
if mibBuilder.loadTexts:rcftRemoteVCGToLLOATraps.setStatus(_A)
rcftRemoteVCGToLLFDTraps=NotificationType((1,3,6,1,4,1,8886,2,1,6,16,10,9))
rcftRemoteVCGToLLFDTraps.setObjects((_C,_T))
if mibBuilder.loadTexts:rcftRemoteVCGToLLFDTraps.setStatus(_A)
rcftRemoteVCGMemberLOMTraps=NotificationType((1,3,6,1,4,1,8886,2,1,6,16,10,10))
rcftRemoteVCGMemberLOMTraps.setObjects((_C,_d))
if mibBuilder.loadTexts:rcftRemoteVCGMemberLOMTraps.setStatus(_A)
rcftRemoteVCGMemberSQMTraps=NotificationType((1,3,6,1,4,1,8886,2,1,6,16,10,11))
rcftRemoteVCGMemberSQMTraps.setObjects((_C,_d))
if mibBuilder.loadTexts:rcftRemoteVCGMemberSQMTraps.setStatus(_A)
rcftRemoteVCGMemberCRCTraps=NotificationType((1,3,6,1,4,1,8886,2,1,6,16,10,12))
rcftRemoteVCGMemberCRCTraps.setObjects((_C,_d))
if mibBuilder.loadTexts:rcftRemoteVCGMemberCRCTraps.setStatus(_A)
rcftRemoteVCGMemberLOATraps=NotificationType((1,3,6,1,4,1,8886,2,1,6,16,10,13))
rcftRemoteVCGMemberLOATraps.setObjects((_C,_d))
if mibBuilder.loadTexts:rcftRemoteVCGMemberLOATraps.setStatus(_A)
rcftRemoteVCGToLMemberLOMTraps=NotificationType((1,3,6,1,4,1,8886,2,1,6,16,10,14))
rcftRemoteVCGToLMemberLOMTraps.setObjects((_C,_e))
if mibBuilder.loadTexts:rcftRemoteVCGToLMemberLOMTraps.setStatus(_A)
rcftRemoteVCGToLMemberSQMTraps=NotificationType((1,3,6,1,4,1,8886,2,1,6,16,10,15))
rcftRemoteVCGToLMemberSQMTraps.setObjects((_C,_e))
if mibBuilder.loadTexts:rcftRemoteVCGToLMemberSQMTraps.setStatus(_A)
rcftRemoteVCGToLMemberCRCTraps=NotificationType((1,3,6,1,4,1,8886,2,1,6,16,10,16))
rcftRemoteVCGToLMemberCRCTraps.setObjects((_C,_e))
if mibBuilder.loadTexts:rcftRemoteVCGToLMemberCRCTraps.setStatus(_A)
rcftRemoteVCGToLMemberLOATraps=NotificationType((1,3,6,1,4,1,8886,2,1,6,16,10,17))
rcftRemoteVCGToLMemberLOATraps.setObjects((_C,_e))
if mibBuilder.loadTexts:rcftRemoteVCGToLMemberLOATraps.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'rcftRemoteDeviceMib':rcftRemoteDeviceMib,'rcftRemoteDeviceSystemMIB':rcftRemoteDeviceSystemMIB,'rcftRemoteDeviceSysObjects':rcftRemoteDeviceSysObjects,'rcftRemoteDeviceSysTable':rcftRemoteDeviceSysTable,'rcftRemoteDeviceSysEntry':rcftRemoteDeviceSysEntry,_J:rcftRemoteDeviceIndex,_Aj:rcftRemoteDeviceExist,'rcftRemoteDeviceType':rcftRemoteDeviceType,'rcftRemoteDeviceLocalPortType':rcftRemoteDeviceLocalPortType,'rcftRemoteDeviceLocalPortIndex':rcftRemoteDeviceLocalPortIndex,'rcftRemoteDeviceVersionInfo':rcftRemoteDeviceVersionInfo,_Ak:rcftRemoteSysTemperature,_p:rcftRemoteSysVoltageStatus,'rcftRemoteDeviceWorkMode':rcftRemoteDeviceWorkMode,'rcftRemoteDeviceFrameLen':rcftRemoteDeviceFrameLen,'rcftRemoteDeviceOrder':rcftRemoteDeviceOrder,'rcftRemoteDeviceConfigFlag':rcftRemoteDeviceConfigFlag,'rcftRemoteSlotAutoCutErrLineEn':rcftRemoteSlotAutoCutErrLineEn,'rcftRemotePowerSupply':rcftRemotePowerSupply,_Al:rcftRemoteDevicePowerDown,'rcftRemoteDeviceClkMode':rcftRemoteDeviceClkMode,'rcftRemoteDeviceE1SubCardType':rcftRemoteDeviceE1SubCardType,'rcftRemoteDeviceGateway':rcftRemoteDeviceGateway,'rcftRemoteDeviceIP':rcftRemoteDeviceIP,'rcftRemoteDeviceSubnetMask':rcftRemoteDeviceSubnetMask,'rcftRemoteDeviceVLANID':rcftRemoteDeviceVLANID,'rcftRemoteDeviceCommunityRW':rcftRemoteDeviceCommunityRW,'rcftRemoteDeviceCommunityLength':rcftRemoteDeviceCommunityLength,'rcftRemoteDeviceCommunity':rcftRemoteDeviceCommunity,'rcftRemoteDeviceVoltageValue':rcftRemoteDeviceVoltageValue,_q:rcftRemoteDeviceStatus,'rcftRemoteSubModuleExist':rcftRemoteSubModuleExist,'rcftRemoteMultiE1LoopOrder':rcftRemoteMultiE1LoopOrder,'rcftRemoteOrderTimeParameter':rcftRemoteOrderTimeParameter,'rcftRemoteOrderModeParameter':rcftRemoteOrderModeParameter,'rcftRemoteSDRAMBuf':rcftRemoteSDRAMBuf,'rcftRemoteRLPStatus':rcftRemoteRLPStatus,'rcftRemoteLALStatus':rcftRemoteLALStatus,'rcftRemoteRALStatus':rcftRemoteRALStatus,'rcftRemoteDeviceSwitchStatus':rcftRemoteDeviceSwitchStatus,'rcftRemoteDeviceMoudleExist':rcftRemoteDeviceMoudleExist,'rcftRemoteCardInformation':rcftRemoteCardInformation,'rcftRemoteSwitchType':rcftRemoteSwitchType,'rcftRemoteConnectMode':rcftRemoteConnectMode,'rcftRemoteQosEnable':rcftRemoteQosEnable,'rcftRemoteBaseCOS':rcftRemoteBaseCOS,'rcftRemoteDSCP':rcftRemoteDSCP,'rcftRemoteQueuesPolicy':rcftRemoteQueuesPolicy,'rcftRemoteMultiE1AlarmRejectOrder':rcftRemoteMultiE1AlarmRejectOrder,'rcftRemoteT1PortPulseWaveForm':rcftRemoteT1PortPulseWaveForm,'rcftRemoteT1PortCodeType':rcftRemoteT1PortCodeType,'rcftRemoteDeviceSabitMode':rcftRemoteDeviceSabitMode,'rcftRemoteDeviceApsWaitToRestore':rcftRemoteDeviceApsWaitToRestore,'rcftRemoteDeviceCLKChannel':rcftRemoteDeviceCLKChannel,'rcftRemoteDeviceRmcChannelType':rcftRemoteDeviceRmcChannelType,'rcftRemoteDeviceProductType':rcftRemoteDeviceProductType,'rcftRemoteDeviceProtocolVer':rcftRemoteDeviceProtocolVer,'rcftRemoteDeviceVenderCode':rcftRemoteDeviceVenderCode,'rcftRemoteDeviceModelID':rcftRemoteDeviceModelID,'rcftRemoteE1PortNumber':rcftRemoteE1PortNumber,'rcftRemoteDeviceVLANType':rcftRemoteDeviceVLANType,'rcftRemoteDeviceQoSPolicy':rcftRemoteDeviceQoSPolicy,'rcftRemoteDeviceApsE3SwitchDelay':rcftRemoteDeviceApsE3SwitchDelay,'rcftRemoteDeviceApsE6SwitchDelay':rcftRemoteDeviceApsE6SwitchDelay,'rcftRemoteDeviceVLANTagDirection':rcftRemoteDeviceVLANTagDirection,'rcftRemoteDeviceVLANTagModule':rcftRemoteDeviceVLANTagModule,'rcftRemoteDeviceISPTPID':rcftRemoteDeviceISPTPID,'rcftRemoteE1DS1PortType':rcftRemoteE1DS1PortType,'rcftRemoteDeviceE1FrameChannel':rcftRemoteDeviceE1FrameChannel,'rcftRemoteDeviceManageID':rcftRemoteDeviceManageID,'rcftRemoteDeviceMibUse':rcftRemoteDeviceMibUse,'rcftRemoteDeviceConfigFlagTable':rcftRemoteDeviceConfigFlagTable,'rcftRemoteDeviceConfigFlagEntry':rcftRemoteDeviceConfigFlagEntry,'rcftRemoteDeviceConfigFinishFlag':rcftRemoteDeviceConfigFinishFlag,'rcftRemoteDeviceSysTraps':rcftRemoteDeviceSysTraps,'rcftRemoteDevExistTrap':rcftRemoteDevExistTrap,'rcftRemoteDevVoltTooHighTrap':rcftRemoteDevVoltTooHighTrap,'rcftRemoteDevVoltTooLowTrap':rcftRemoteDevVoltTooLowTrap,'rcftRemoteDevTmptTrap':rcftRemoteDevTmptTrap,'rcftRemoteDevPowerDownTrap':rcftRemoteDevPowerDownTrap,'rcftRemoteDevPSChannelTrap':rcftRemoteDevPSChannelTrap,'rcftRemoteDevSPChannelTrap':rcftRemoteDevSPChannelTrap,'rcftRemoteDeviceEthMIB':rcftRemoteDeviceEthMIB,'rcftRemoteDeviceEthFeMIB':rcftRemoteDeviceEthFeMIB,'rcftRemoteDeviceEthFeObjects':rcftRemoteDeviceEthFeObjects,'rcftRemoteEthFePortTable':rcftRemoteEthFePortTable,'rcftRemoteEthFePortEntry':rcftRemoteEthFePortEntry,_h:rcftRemoteEthFeIndex,_Am:rcftRemoteEthFeLinkStatus,'rcftRemoteEthFeShutDown':rcftRemoteEthFeShutDown,'rcftRemoteEthFeAutoNegotiation':rcftRemoteEthFeAutoNegotiation,'rcftRemoteEthFeSpeed':rcftRemoteEthFeSpeed,'rcftRemoteEthFeDuplex':rcftRemoteEthFeDuplex,'rcftRemoteEthFeFlowControl':rcftRemoteEthFeFlowControl,'rcftRemoteEthFeRestrictSpeed':rcftRemoteEthFeRestrictSpeed,'rcftRemoteEthFeFaultPass':rcftRemoteEthFeFaultPass,'rcftRemoteEthFeDisabledByRemoteTP':rcftRemoteEthFeDisabledByRemoteTP,'rcftRemoteEthFeDisabledByFxToFeFP':rcftRemoteEthFeDisabledByFxToFeFP,'rcftRemoteEthFeTxRestrictSpeed':rcftRemoteEthFeTxRestrictSpeed,'rcftRemoteEthFeTag':rcftRemoteEthFeTag,'rcftRemoteEthFePortStatus':rcftRemoteEthFePortStatus,'rcftRemoteEthFeRestrictSpeedStep':rcftRemoteEthFeRestrictSpeedStep,'rcftRemoteEthFeOrderTimeParameter':rcftRemoteEthFeOrderTimeParameter,'rcftRemoteEthFeOrderModeParameter':rcftRemoteEthFeOrderModeParameter,'rcftRemoteEthFeOrder':rcftRemoteEthFeOrder,'rcftRemoteEthFePortStatusExtend':rcftRemoteEthFePortStatusExtend,'rcftRemoteEthFeStormControl':rcftRemoteEthFeStormControl,'rcftRemoteEthFePVID':rcftRemoteEthFePVID,'rcftRemoteEthFeDefaultCOS':rcftRemoteEthFeDefaultCOS,'rcftRemoteEthFeQoSPolicy':rcftRemoteEthFeQoSPolicy,'rcftRemoteEthFeStatisticTable':rcftRemoteEthFeStatisticTable,_Ab:rcftRemoteEthFeStatisticEntry,'rcftRemoteEthFeTxPackets':rcftRemoteEthFeTxPackets,'rcftRemoteEthFeTxBytes':rcftRemoteEthFeTxBytes,'rcftRemoteEthFeRxPackets':rcftRemoteEthFeRxPackets,'rcftRemoteEthFeRxBytes':rcftRemoteEthFeRxBytes,'rcftRemoteEthFeRxLostPackets':rcftRemoteEthFeRxLostPackets,'rcftRemoteEthFeFluxTimer':rcftRemoteEthFeFluxTimer,'rcftRemoteEthFeTxLostPackets':rcftRemoteEthFeTxLostPackets,'rcftRemoteEthFePortConfTable':rcftRemoteEthFePortConfTable,'rcftRemoteEthFePortConfEntry':rcftRemoteEthFePortConfEntry,'rcftRemoteEthFeConfSpeed':rcftRemoteEthFeConfSpeed,'rcftRemoteEthFeConfDuplex':rcftRemoteEthFeConfDuplex,'rcftRemoteDeviceEthFeTraps':rcftRemoteDeviceEthFeTraps,'rcftRemoteEthFeLinkTrap':rcftRemoteEthFeLinkTrap,'rcftRemoteDeviceEthFxMIB':rcftRemoteDeviceEthFxMIB,'rcftRemoteDeviceEthFxObjects':rcftRemoteDeviceEthFxObjects,'rcftRemoteEthFxPortTable':rcftRemoteEthFxPortTable,'rcftRemoteEthFxPortEntry':rcftRemoteEthFxPortEntry,_b:rcftRemoteEthFxIndex,'rcftRemoteEthFxFlowControl':rcftRemoteEthFxFlowControl,_An:rcftRemoteEthFxPortRLK,_Ao:rcftRemoteEthFxPortTLK,_As:rcftRemoteEthFxPortSD,_Ap:rcftRemoteEthFxPortTxPowerAbnormal,_Aq:rcftRemoteEthFxPortRxSensitiveAbnormal,_Ar:rcftRemoteEthFxPortLaserAbnormal,'rcftRemoteEthFxShutDown':rcftRemoteEthFxShutDown,'rcftRemoteEthFxModuleType':rcftRemoteEthFxModuleType,'rcftRemoteEthFxFaultPass':rcftRemoteEthFxFaultPass,_At:rcftRemoteEthFxPortLink,'rcftRemoteEthFxRxToTxFaultPass':rcftRemoteEthFxRxToTxFaultPass,'rcftRemoteEthFxTxDisabledByFR':rcftRemoteEthFxTxDisabledByFR,'rcftRemoteEthFxOrderTimeParameter':rcftRemoteEthFxOrderTimeParameter,'rcftRemoteEthFxOrderModeParameter':rcftRemoteEthFxOrderModeParameter,'rcftRemoteEthFxOrder':rcftRemoteEthFxOrder,_Au:rcftRemoteEthFxPortExist,'rcftRemoteEthFxPortAuto':rcftRemoteEthFxPortAuto,'rcftRemoteEthFxModuleMaxSpeed':rcftRemoteEthFxModuleMaxSpeed,'rcftRemoteEthFxTranDistance':rcftRemoteEthFxTranDistance,'rcftRemoteEthFxModuleWaveLen':rcftRemoteEthFxModuleWaveLen,'rcftRemoteEthFxPortConnectorType':rcftRemoteEthFxPortConnectorType,'rcftRemoteEthFxPortTransmitMedia':rcftRemoteEthFxPortTransmitMedia,'rcftRemoteEthFxModuleManufacturer':rcftRemoteEthFxModuleManufacturer,'rcftRemoteEthFxModuleDescr':rcftRemoteEthFxModuleDescr,'rcftRemoteEthFxPortModuleVersion':rcftRemoteEthFxPortModuleVersion,'rcftRemoteEthFxModuleSerialNumber':rcftRemoteEthFxModuleSerialNumber,'rcftRemoteEthFxPortSFPDiagnoInfo':rcftRemoteEthFxPortSFPDiagnoInfo,_M:rcftRemoteEthFxSFPDiagnoAlarmStatus,'rcftRemoteEthFxPortStatus':rcftRemoteEthFxPortStatus,'rcftRemoteEthFxUntag':rcftRemoteEthFxUntag,'rcftRemoteEthFxPVID':rcftRemoteEthFxPVID,'rcftRemoteEthFxPortSFPType':rcftRemoteEthFxPortSFPType,_Av:rcftRemoteEthFxPortSFPInfo,'rcftRemoteEthFxPortLoopStatus':rcftRemoteEthFxPortLoopStatus,'rcftRemoteEthFxPortRxRestrictSpeed':rcftRemoteEthFxPortRxRestrictSpeed,'rcftRemoteEthFxPortTxRestrictSpeed':rcftRemoteEthFxPortTxRestrictSpeed,_R:rcftRemoteEthFxSFPDiagnoWarningStatus,'rcftRemoteEthFxPortLineOrClient':rcftRemoteEthFxPortLineOrClient,'rcftRemoteEthFxCOS':rcftRemoteEthFxCOS,'rcftRemoteEthFxStatisticTable':rcftRemoteEthFxStatisticTable,_Ac:rcftRemoteEthFxStatisticEntry,'rcftRemoteEthFxTxPackets':rcftRemoteEthFxTxPackets,'rcftRemoteEthFxTxBytes':rcftRemoteEthFxTxBytes,'rcftRemoteEthFxRxPackets':rcftRemoteEthFxRxPackets,'rcftRemoteEthFxRxBytes':rcftRemoteEthFxRxBytes,'rcftRemoteEthFxRxLostPackets':rcftRemoteEthFxRxLostPackets,'rcftRemoteEthFxFluxTimer':rcftRemoteEthFxFluxTimer,'rcftRemoteEthFxTxLostPackets':rcftRemoteEthFxTxLostPackets,'rcftRemoteEthFx64TxBytes':rcftRemoteEthFx64TxBytes,'rcftRemoteEthFx64RxBytes':rcftRemoteEthFx64RxBytes,'rcftRemoteDeviceEthFxTraps':rcftRemoteDeviceEthFxTraps,'rcftRemoteEthFxPortRLKTrap':rcftRemoteEthFxPortRLKTrap,'rcftRemoteEthFxPortTLKTrap':rcftRemoteEthFxPortTLKTrap,'rcftRemoteEthFxPortTxPowerTrap':rcftRemoteEthFxPortTxPowerTrap,'rcftRemoteEthFxPortRxSensitiveTrap':rcftRemoteEthFxPortRxSensitiveTrap,'rcftRemoteEthFxPortLaserTrap':rcftRemoteEthFxPortLaserTrap,'rcftRemoteEthFxPortSDTrap':rcftRemoteEthFxPortSDTrap,'rcftRemoteEthFxPortLinkTrap':rcftRemoteEthFxPortLinkTrap,'rcftRemoteEthFxPortExitTrap':rcftRemoteEthFxPortExitTrap,'rcftRemoteEthFxPortTempHighTrap':rcftRemoteEthFxPortTempHighTrap,'rcftRemoteEthFxPortTempLowTrap':rcftRemoteEthFxPortTempLowTrap,'rcftRemoteEthFxPortVoltageHighTrap':rcftRemoteEthFxPortVoltageHighTrap,'rcftRemoteEthFxPortVoltageLowTrap':rcftRemoteEthFxPortVoltageLowTrap,'rcftRemoteEthFxPortOffsetCurrHighTrap':rcftRemoteEthFxPortOffsetCurrHighTrap,'rcftRemoteEthFxPortOffsetCurrLowTrap':rcftRemoteEthFxPortOffsetCurrLowTrap,'rcftRemoteEthFxPortSendPowerHighTrap':rcftRemoteEthFxPortSendPowerHighTrap,'rcftRemoteEthFxPortSendPowerLowTrap':rcftRemoteEthFxPortSendPowerLowTrap,'rcftRemoteEthFxPortRecvPowerHighTrap':rcftRemoteEthFxPortRecvPowerHighTrap,'rcftRemoteEthFxPortRecvPowerLowTrap':rcftRemoteEthFxPortRecvPowerLowTrap,'rcftRemoteEthFxPortRemotePowerDownTrap':rcftRemoteEthFxPortRemotePowerDownTrap,'rcftRemoteEthFxPortInputSignalLosTrap':rcftRemoteEthFxPortInputSignalLosTrap,'rcftRemoteEthFxPortTempHighWarnning':rcftRemoteEthFxPortTempHighWarnning,'rcftRemoteEthFxPortTempLowWarning':rcftRemoteEthFxPortTempLowWarning,'rcftRemoteEthFxPortVoltageHighWarning':rcftRemoteEthFxPortVoltageHighWarning,'rcftRemoteEthFxPortVoltageLowWarning':rcftRemoteEthFxPortVoltageLowWarning,'rcftRemoteEthFxPortOffsetCurrHighWarning':rcftRemoteEthFxPortOffsetCurrHighWarning,'rcftRemoteEthFxPortOffsetCurrLowWarning':rcftRemoteEthFxPortOffsetCurrLowWarning,'rcftRemoteEthFxPortSendPowerHighWarning':rcftRemoteEthFxPortSendPowerHighWarning,'rcftRemoteEthFxPortSendPowerLowWarning':rcftRemoteEthFxPortSendPowerLowWarning,'rcftRemoteEthFxPortRecvPowerHighWarning':rcftRemoteEthFxPortRecvPowerHighWarning,'rcftRemoteEthFxPortRecvPowerLowWarning':rcftRemoteEthFxPortRecvPowerLowWarning,'rcftRemoteDeviceEthFxPerformance':rcftRemoteDeviceEthFxPerformance,'rcftRemoteEthFxPortCurrentTable':rcftRemoteEthFxPortCurrentTable,'rcftRemoteEthFxPortCurrentEntry':rcftRemoteEthFxPortCurrentEntry,'rcftRemoteEthFxCurrentTemperature':rcftRemoteEthFxCurrentTemperature,'rcftRemoteEthFxCurrentVoltage':rcftRemoteEthFxCurrentVoltage,'rcftRemoteEthFxCurrentOffsetCurr':rcftRemoteEthFxCurrentOffsetCurr,'rcftRemoteEthFxCurrentRecvPower':rcftRemoteEthFxCurrentRecvPower,'rcftRemoteEthFxCurrentSendPower':rcftRemoteEthFxCurrentSendPower,'rcftRemoteEthFxPortIntervalTable':rcftRemoteEthFxPortIntervalTable,'rcftRemoteEthFxPortIntervalEntry':rcftRemoteEthFxPortIntervalEntry,_AF:rcftRemoteEthFxIntervalNumber,'rcftRemoteEthFxIntervalTemperature':rcftRemoteEthFxIntervalTemperature,'rcftRemoteEthFxIntervalVoltage':rcftRemoteEthFxIntervalVoltage,'rcftRemoteEthFxIntervalOffsetCurr':rcftRemoteEthFxIntervalOffsetCurr,'rcftRemoteEthFxIntervalRecvPower':rcftRemoteEthFxIntervalRecvPower,'rcftRemoteEthFxIntervalSendPower':rcftRemoteEthFxIntervalSendPower,'rcftRemoteEthFxPortPerTable':rcftRemoteEthFxPortPerTable,'rcftRemoteEthFxPortPerEntry':rcftRemoteEthFxPortPerEntry,'rcftRemoteEthFxPortPerTemperature':rcftRemoteEthFxPortPerTemperature,'rcftRemoteEthFxPortPerVoltage':rcftRemoteEthFxPortPerVoltage,'rcftRemoteEthFxPortPerOffsetCurr':rcftRemoteEthFxPortPerOffsetCurr,'rcftRemoteEthFxPortPerRecvPower':rcftRemoteEthFxPortPerRecvPower,'rcftRemoteEthFxPortPerSendPower':rcftRemoteEthFxPortPerSendPower,'rcftRemoteDeviceE1MIB':rcftRemoteDeviceE1MIB,'rcftRemoteDeviceE1Objects':rcftRemoteDeviceE1Objects,'rcftRemoteDeviceE1Table':rcftRemoteDeviceE1Table,'rcftRemoteDeviceE1Entry':rcftRemoteDeviceE1Entry,_AG:rcftRemoteE1Index,'rcftRemoteE1BertEnable':rcftRemoteE1BertEnable,'rcftRemoteE1ClockMode':rcftRemoteE1ClockMode,'rcftRemoteE1FrameEnable':rcftRemoteE1FrameEnable,_Q:rcftRemoteE1AlarmStatus,'rcftRemoteE1SubSpeed':rcftRemoteE1SubSpeed,'rcftRemoteE1CRCDetectEnable':rcftRemoteE1CRCDetectEnable,'rcftRemoteE1ErrCodeSecCnt':rcftRemoteE1ErrCodeSecCnt,'rcftRemoteE1SErrCodeSecCnt':rcftRemoteE1SErrCodeSecCnt,_r:rcftRemoteE1TransErrorCode,'rcftRemoteE1CRCStatus':rcftRemoteE1CRCStatus,'rcftRemoteE1FaultPass':rcftRemoteE1FaultPass,'rcftRemoteE1LocalLoopEn':rcftRemoteE1LocalLoopEn,'rcftRemoteE1Location':rcftRemoteE1Location,'rcftRemoteE1FoundLink':rcftRemoteE1FoundLink,'rcftRemoteE1UnUsed':rcftRemoteE1UnUsed,_c:rcftRemoteToLocalE1AlarmStatus,'rcftRemoteE1Balance':rcftRemoteE1Balance,'rcftRemoteE1PortStatus':rcftRemoteE1PortStatus,'rcftRemoteE1PortTS0Mode':rcftRemoteE1PortTS0Mode,'rcftRemoteE1PortIdleCode':rcftRemoteE1PortIdleCode,'rcftRemoteE1LoopStatus':rcftRemoteE1LoopStatus,'rcftRemoteE1OrderTimeParameter':rcftRemoteE1OrderTimeParameter,'rcftRemoteE1OrderModeParameter':rcftRemoteE1OrderModeParameter,'rcftRemoteE1Order':rcftRemoteE1Order,'rcftRemoteE1PortType':rcftRemoteE1PortType,'rcftRemoteE1BertStatus':rcftRemoteE1BertStatus,'rcftRemoteE1BertTime':rcftRemoteE1BertTime,'rcftRemoteE1BertErrCode':rcftRemoteE1BertErrCode,'rcftRemoteE1BertUnusedTime':rcftRemoteE1BertUnusedTime,'rcftRemoteE1BertPortSpeed':rcftRemoteE1BertPortSpeed,'rcftRemoteE1BertCodeType':rcftRemoteE1BertCodeType,'rcftRemoteE1BertCodeNum':rcftRemoteE1BertCodeNum,'rcftRemoteE1LoopSwitchStatus':rcftRemoteE1LoopSwitchStatus,'rcftRemoteE1AlarmRejest':rcftRemoteE1AlarmRejest,_s:rcftRemoteT1AlarmStatus,'rcftRemoteE1PortVCGNumber':rcftRemoteE1PortVCGNumber,'rcftRemoteE1ToLNumber':rcftRemoteE1ToLNumber,'rcftRemoteE1CVCnt':rcftRemoteE1CVCnt,'rcftRemoteE1StatisticTable':rcftRemoteE1StatisticTable,_Ad:rcftRemoteE1StatisticEntry,'rcftRemoteE1TxPackets':rcftRemoteE1TxPackets,'rcftRemoteE1TxBytes':rcftRemoteE1TxBytes,'rcftRemoteE1RxPackets':rcftRemoteE1RxPackets,'rcftRemoteE1RxBytes':rcftRemoteE1RxBytes,'rcftRemoteE1RxERRPackets':rcftRemoteE1RxERRPackets,'rcftRemoteE1FluxTimer':rcftRemoteE1FluxTimer,'rcftRemoteE1LANTxPackets':rcftRemoteE1LANTxPackets,'rcftRemoteE1LANRxPackets':rcftRemoteE1LANRxPackets,'rcftRemoteE1LANRxLosPackets':rcftRemoteE1LANRxLosPackets,'rcftRemoteDeviceE1Traps':rcftRemoteDeviceE1Traps,'rcftRemoteDevE1LOSTRAP':rcftRemoteDevE1LOSTRAP,'rcftRemoteDevE1LOFTRAP':rcftRemoteDevE1LOFTRAP,'rcftRemoteDevE1CRCTRAP':rcftRemoteDevE1CRCTRAP,'rcftRemoteDevE1AISTrap':rcftRemoteDevE1AISTrap,'rcftRemoteDevE1TransErrorCodeMore10E-3':rcftRemoteDevE1TransErrorCodeMore10E_3,'rcftRemoteDevE1TransErrorCodeMore10E-6':rcftRemoteDevE1TransErrorCodeMore10E_6,'rcftRemoteDevToLocalDevE1LOSTRAP':rcftRemoteDevToLocalDevE1LOSTRAP,'rcftRemoteDevToLocalDevE1LOFTRAP':rcftRemoteDevToLocalDevE1LOFTRAP,'rcftRemoteDevToLocalDevE1CRCTRAP':rcftRemoteDevToLocalDevE1CRCTRAP,'rcftRemoteDevToLocalDevE1AISTrap':rcftRemoteDevToLocalDevE1AISTrap,'rcftRemoteDevE1CVTrap':rcftRemoteDevE1CVTrap,'rcftRemoteDevE1LOMFTrap':rcftRemoteDevE1LOMFTrap,'rcftRemoteDevT1LOSTrap':rcftRemoteDevT1LOSTrap,'rcftRemoteDevT1AISTrap':rcftRemoteDevT1AISTrap,'rcftRemoteDevE1TSDTrap':rcftRemoteDevE1TSDTrap,'rcftRemoteE1PortToLTSDTrap':rcftRemoteE1PortToLTSDTrap,'rcftRemoteDevE1RDITrap':rcftRemoteDevE1RDITrap,'rcftRemoteE1PortToLLOMFTrap':rcftRemoteE1PortToLLOMFTrap,'rcftRemoteDeviceSHDSLMIB':rcftRemoteDeviceSHDSLMIB,'rcftRemoteSHDSLPortObjects':rcftRemoteSHDSLPortObjects,'rcftRemoteSHDSLPortTable':rcftRemoteSHDSLPortTable,'rcftRemoteSHDSLPortEntry':rcftRemoteSHDSLPortEntry,_V:rcftRemoteSHDSLPortIndex,_X:rcftRemoteSHDSLPortAlarmStatus,'rcftRemoteSHDSLPortStatus':rcftRemoteSHDSLPortStatus,'rcftRemoteSHDSLPortCapableSpeed':rcftRemoteSHDSLPortCapableSpeed,'rcftRemoteSHDSLPortWorkSpeed':rcftRemoteSHDSLPortWorkSpeed,'rcftRemoteSHDSLPortProbeMaxSpeed':rcftRemoteSHDSLPortProbeMaxSpeed,'rcftRemoteSHDSLPortProbeMinSpeed':rcftRemoteSHDSLPortProbeMinSpeed,'rcftRemoteSDHSLPortSNR':rcftRemoteSDHSLPortSNR,'rcftRemoteSHDSLPortConfigSNR':rcftRemoteSHDSLPortConfigSNR,_Aw:rcftRemoteSHDSLPortSNRThreshold,'rcftRemoteSHDSLPortAttenuation':rcftRemoteSHDSLPortAttenuation,_Ax:rcftRemoteSHDSLPortAttenuationThreshold,'rcftRemoteSHDSLPortPBO':rcftRemoteSHDSLPortPBO,_Ay:rcftRemoteSHDSLPortLOSThreshold,_Az:rcftRemoteSHDSLPortLOSWThreshold,_A_:rcftRemoteSHDSLPortLOLKThreshold,_B0:rcftRemoteSHDSLPortESThreshold,'rcftRemoteSHDSLPortLoopStatus':rcftRemoteSHDSLPortLoopStatus,'rcftRemoteSHDSLPortAttenuationInitThreshhold':rcftRemoteSHDSLPortAttenuationInitThreshhold,'rcftRemoteSHDSLPortOrderTimeParameter':rcftRemoteSHDSLPortOrderTimeParameter,'rcftRemoteSHDSLPortOrderModeParameter':rcftRemoteSHDSLPortOrderModeParameter,'rcftRemoteSHDSLPortOrder':rcftRemoteSHDSLPortOrder,'rcftRemoteSHDSLPortPBOAmount':rcftRemoteSHDSLPortPBOAmount,'rcftRemoteSHDSLBertStatus':rcftRemoteSHDSLBertStatus,'rcftRemoteSHDSLBertTime':rcftRemoteSHDSLBertTime,'rcftRemoteSHDSLBertErrCode':rcftRemoteSHDSLBertErrCode,'rcftRemoteSHDSLBertUnusedTime':rcftRemoteSHDSLBertUnusedTime,'rcftRemoteSHDSLBertPortSpeed':rcftRemoteSHDSLBertPortSpeed,'rcftRemoteSHDSLBertCodeType':rcftRemoteSHDSLBertCodeType,'rcftRemoteSHDSLBertCodeNum':rcftRemoteSHDSLBertCodeNum,'rcftRemoteSHDSLLoopStatus':rcftRemoteSHDSLLoopStatus,'rcftRemoteSHDSLPortPerformance':rcftRemoteSHDSLPortPerformance,'rcftRemoteSHDSLPortCurrentTable':rcftRemoteSHDSLPortCurrentTable,'rcftRemoteSHDSLPortCurrentEntry':rcftRemoteSHDSLPortCurrentEntry,'rcftRemoteSHDSLPortCurrentLOSTimes':rcftRemoteSHDSLPortCurrentLOSTimes,'rcftRemoteSHDSLPortCurrentLOSWTimes':rcftRemoteSHDSLPortCurrentLOSWTimes,'rcftRemoteSHDSLPortCurrentLOLKTimes':rcftRemoteSHDSLPortCurrentLOLKTimes,'rcftRemoteSHDSLPortCurrentCVTimes':rcftRemoteSHDSLPortCurrentCVTimes,'rcftRemoteSHDSLPortCurrentES':rcftRemoteSHDSLPortCurrentES,'rcftRemoteSHDSLPortCurrentSES':rcftRemoteSHDSLPortCurrentSES,'rcftRemoteSHDSLPortCurrentUAS':rcftRemoteSHDSLPortCurrentUAS,'rcftRemoteSHDSLPortCurrentLOSWS':rcftRemoteSHDSLPortCurrentLOSWS,'rcftRemoteSHDSLPortCurrentCRCTimes':rcftRemoteSHDSLPortCurrentCRCTimes,'rcftRemoteSHDSLPortIntervalTable':rcftRemoteSHDSLPortIntervalTable,'rcftRemoteSHDSLPortIntervalEntry':rcftRemoteSHDSLPortIntervalEntry,_AK:rcftRemoteSHDSLPortIntervalNumber,'rcftRemoteSHDSLPortIntervalLOSTimes':rcftRemoteSHDSLPortIntervalLOSTimes,'rcftRemoteSHDSLPortIntervalLOSWTimes':rcftRemoteSHDSLPortIntervalLOSWTimes,'rcftRemoteSHDSLPortIntervalLOLKTimes':rcftRemoteSHDSLPortIntervalLOLKTimes,'rcftRemoteSHDSLPortIntervalCVTimes':rcftRemoteSHDSLPortIntervalCVTimes,'rcftRemoteSHDSLPortIntervalES':rcftRemoteSHDSLPortIntervalES,'rcftRemoteSHDSLPortIntervalSES':rcftRemoteSHDSLPortIntervalSES,'rcftRemoteSHDSLPortIntervalUAS':rcftRemoteSHDSLPortIntervalUAS,'rcftRemoteSHDSLPortIntervalLOSWS':rcftRemoteSHDSLPortIntervalLOSWS,'rcftRemoteSHDSLPortIntervalCRCTimes':rcftRemoteSHDSLPortIntervalCRCTimes,'rcftRemoteSHDSLPortCurrentDayTable':rcftRemoteSHDSLPortCurrentDayTable,'rcftRemoteSHDSLPortCurrentDayEntry':rcftRemoteSHDSLPortCurrentDayEntry,'rcftRemoteSHDSLPortCurrentDayLOSTimes':rcftRemoteSHDSLPortCurrentDayLOSTimes,'rcftRemoteSHDSLPortCurrentDayLOSWTimes':rcftRemoteSHDSLPortCurrentDayLOSWTimes,'rcftRemoteSHDSLPortCurrentDayLOLKTimes':rcftRemoteSHDSLPortCurrentDayLOLKTimes,'rcftRemoteSHDSLPortCurrentDayCVTimes':rcftRemoteSHDSLPortCurrentDayCVTimes,'rcftRemoteSHDSLPortCurrentDayES':rcftRemoteSHDSLPortCurrentDayES,'rcftRemoteSHDSLPortCurrentDaySES':rcftRemoteSHDSLPortCurrentDaySES,'rcftRemoteSHDSLPortCurrentDayUAS':rcftRemoteSHDSLPortCurrentDayUAS,'rcftRemoteSHDSLPortCurrentDayLOSWS':rcftRemoteSHDSLPortCurrentDayLOSWS,'rcftRemoteSHDSLPortCurrentDayCRCTimes':rcftRemoteSHDSLPortCurrentDayCRCTimes,'rcftRemoteSHDSLPortIntervalDayTable':rcftRemoteSHDSLPortIntervalDayTable,'rcftRemoteSHDSLPortIntervalDayEntry':rcftRemoteSHDSLPortIntervalDayEntry,_AL:rcftRemoteSHDSLPortIntervalDayNumber,'rcftRemoteSHDSLPortIntervalDayLOSTimes':rcftRemoteSHDSLPortIntervalDayLOSTimes,'rcftRemoteSHDSLPortIntervalDayLOSWTimes':rcftRemoteSHDSLPortIntervalDayLOSWTimes,'rcftRemoteSHDSLPortIntervalDayLOLKTimes':rcftRemoteSHDSLPortIntervalDayLOLKTimes,'rcftRemoteSHDSLPortIntervalDayCVTimes':rcftRemoteSHDSLPortIntervalDayCVTimes,'rcftRemoteSHDSLPortIntervalDayES':rcftRemoteSHDSLPortIntervalDayES,'rcftRemoteSHDSLPortIntervalDaySES':rcftRemoteSHDSLPortIntervalDaySES,'rcftRemoteSHDSLPortIntervalDayUAS':rcftRemoteSHDSLPortIntervalDayUAS,'rcftRemoteSHDSLPortIntervalDayLOSWS':rcftRemoteSHDSLPortIntervalDayLOSWS,'rcftRemoteSHDSLPortIntervalDayCRCTimes':rcftRemoteSHDSLPortIntervalDayCRCTimes,'rcftRemoteSHDSLPortTraps':rcftRemoteSHDSLPortTraps,'rcftRemoteSHDSLPortLOSTrap':rcftRemoteSHDSLPortLOSTrap,'rcftRemoteSHDSLPortLOSWTrap':rcftRemoteSHDSLPortLOSWTrap,'rcftRemoteSHDSLPortLINKTrap':rcftRemoteSHDSLPortLINKTrap,'rcftRemoteSHDSLPortFECTrap':rcftRemoteSHDSLPortFECTrap,'rcftRemoteSHDSLPortCRCTrap':rcftRemoteSHDSLPortCRCTrap,'rcftRemoteSHDSLPortSNRThresholdTrap':rcftRemoteSHDSLPortSNRThresholdTrap,'rcftRemoteSHDSLPortAttenuationThresholdTrap':rcftRemoteSHDSLPortAttenuationThresholdTrap,'rcftRemoteSHDSLPortLOSThresholdTrap':rcftRemoteSHDSLPortLOSThresholdTrap,'rcftRemoteSHDSLPortLOSWThresholdTrap':rcftRemoteSHDSLPortLOSWThresholdTrap,'rcftRemoteSHDSLPortLOLKThresholdTrap':rcftRemoteSHDSLPortLOLKThresholdTrap,'rcftRemoteSHDSLPortESThresholdTrap':rcftRemoteSHDSLPortESThresholdTrap,'rcftRemoteDeviceV35MIB':rcftRemoteDeviceV35MIB,'rcftRemoteV35PortObjects':rcftRemoteV35PortObjects,'rcftRemoteV35PortTable':rcftRemoteV35PortTable,'rcftRemoteV35PortEntry':rcftRemoteV35PortEntry,_AM:rcftRemoteV35PortIndex,_L:rcftRemoteV35PortAlarmStatus,'rcftRemoteV35PortStatus':rcftRemoteV35PortStatus,'rcftRemoteV35PortSpeed':rcftRemoteV35PortSpeed,'rcftRemoteV35PortOrderTimeParameter':rcftRemoteV35PortOrderTimeParameter,'rcftRemoteV35PortOrderModeParameter':rcftRemoteV35PortOrderModeParameter,'rcftRemoteV35PortOrder':rcftRemoteV35PortOrder,'rcftRemoteV35BertStatus':rcftRemoteV35BertStatus,'rcftRemoteV35BertTime':rcftRemoteV35BertTime,'rcftRemoteV35BertErrCode':rcftRemoteV35BertErrCode,'rcftRemoteV35BertUnusedTime':rcftRemoteV35BertUnusedTime,'rcftRemoteV35BertPortSpeed':rcftRemoteV35BertPortSpeed,'rcftRemoteV35BertCodeType':rcftRemoteV35BertCodeType,'rcftRemoteV35BertCodeNum':rcftRemoteV35BertCodeNum,'rcftRemoteV35LoopStatus':rcftRemoteV35LoopStatus,'rcftRemoteV35PortPerformance':rcftRemoteV35PortPerformance,'rcftRemoteV35PortTraps':rcftRemoteV35PortTraps,'rcftRemoteV35PortDCDTrap':rcftRemoteV35PortDCDTrap,'rcftRemoteV35PortCTSTrap':rcftRemoteV35PortCTSTrap,'rcftRemoteV35PortDTRTrap':rcftRemoteV35PortDTRTrap,'rcftRemoteV35PortRTSTrap':rcftRemoteV35PortRTSTrap,'rcftRemoteV35PortCRCTrap':rcftRemoteV35PortCRCTrap,'rcftRemoteV35PortPATTTrap':rcftRemoteV35PortPATTTrap,'rcftRemoteV35PortLOFTrap':rcftRemoteV35PortLOFTrap,'rcftRemoteV35PortCVTrap':rcftRemoteV35PortCVTrap,'rcftRemoteV35PortAISTrap':rcftRemoteV35PortAISTrap,'rcftRemoteV35PortToLLOFTrap':rcftRemoteV35PortToLLOFTrap,'rcftRemoteV35PortToLCVTrap':rcftRemoteV35PortToLCVTrap,'rcftRemoteV35PortToLAISTrap':rcftRemoteV35PortToLAISTrap,'rcftRemoteV35PortDSRTrap':rcftRemoteV35PortDSRTrap,'rcftRemoteDS3E3PortMIB':rcftRemoteDS3E3PortMIB,'rcftRemoteDS3E3PortObjects':rcftRemoteDS3E3PortObjects,'rcftRemoteDS3E3PortTable':rcftRemoteDS3E3PortTable,'rcftRemoteDS3E3PortEntry':rcftRemoteDS3E3PortEntry,_AN:rcftRemoteDS3E3PortIndex,_K:rcftRemoteDS3E3PortAlarmStatus,'rcftRemoteDS3E3PortStatus':rcftRemoteDS3E3PortStatus,'rcftRemoteDS3E3PortESCont':rcftRemoteDS3E3PortESCont,'rcftRemoteDS3E3PortBertStatus':rcftRemoteDS3E3PortBertStatus,'rcftRemoteDS3E3PortFaultFass':rcftRemoteDS3E3PortFaultFass,'rcftRemoteDS3E3PortLoopStatus':rcftRemoteDS3E3PortLoopStatus,'rcftRemoteDS3E3PortOrder':rcftRemoteDS3E3PortOrder,'rcftRemoteDS3E3PortPerformance':rcftRemoteDS3E3PortPerformance,'rcftRemoteDS3E3StatisticTable':rcftRemoteDS3E3StatisticTable,_Ae:rcftRemoteDS3E3StatisticEntry,'rcftRemoteDS3E3TxPackets':rcftRemoteDS3E3TxPackets,'rcftRemoteDS3E3TxBytes':rcftRemoteDS3E3TxBytes,'rcftRemoteDS3E3TxFailurePackets':rcftRemoteDS3E3TxFailurePackets,'rcftRemoteDS3E3RxPackets':rcftRemoteDS3E3RxPackets,'rcftRemoteDS3E3RxBytes':rcftRemoteDS3E3RxBytes,'rcftRemoteDS3E3RxErrorPackets':rcftRemoteDS3E3RxErrorPackets,'rcftRemoteDS3E3FluxTimer':rcftRemoteDS3E3FluxTimer,'rcftRemoteDS3E3PortTraps':rcftRemoteDS3E3PortTraps,'rcftRemoteDS3E3PortAISTrap':rcftRemoteDS3E3PortAISTrap,'rcftRemoteDS3E3PortLOSTrap':rcftRemoteDS3E3PortLOSTrap,'rcftRemoteDS3E3PortLOLTrap':rcftRemoteDS3E3PortLOLTrap,'rcftRemoteDS3E3PortDMOTrap':rcftRemoteDS3E3PortDMOTrap,'rcftRemoteDS3E3PortCVTrap':rcftRemoteDS3E3PortCVTrap,'rcftRemoteDS3E3PortCRCTrap':rcftRemoteDS3E3PortCRCTrap,'rcftRemoteDS3E3PortToLAISTrap':rcftRemoteDS3E3PortToLAISTrap,'rcftRemoteDS3E3PortToLLOSTrap':rcftRemoteDS3E3PortToLLOSTrap,'rcftRemoteDS3E3PortToLLOLTrap':rcftRemoteDS3E3PortToLLOLTrap,'rcftRemoteDS3E3PortToLDMOTrap':rcftRemoteDS3E3PortToLDMOTrap,'rcftRemoteDS3E3PortToLCVTrap':rcftRemoteDS3E3PortToLCVTrap,'rcftRemoteDS3E3PortToLCRCTrap':rcftRemoteDS3E3PortToLCRCTrap,'rcftRemoteDS3E3PortLOFTrap':rcftRemoteDS3E3PortLOFTrap,'rcftRemoteDS3E3PortToLLOFTrap':rcftRemoteDS3E3PortToLLOFTrap,'rcftRemoteDS3E3PortRAITrap':rcftRemoteDS3E3PortRAITrap,'rcftRemoteDS3E3PortToLRAITrap':rcftRemoteDS3E3PortToLRAITrap,'rcftRemoteDS3E3PortOOFTrap':rcftRemoteDS3E3PortOOFTrap,'rcftRemoteDS3E3PortToLOOFTrap':rcftRemoteDS3E3PortToLOOFTrap,'rcftRemotePdhPortMIB':rcftRemotePdhPortMIB,'rcftRemotePdhPortObjects':rcftRemotePdhPortObjects,'rcftRemotePdhPortTable':rcftRemotePdhPortTable,'rcftRemotePdhPortEntry':rcftRemotePdhPortEntry,_AO:rcftRemotePdhPortIndex,'rcftRemotePdhPortModuleType':rcftRemotePdhPortModuleType,_S:rcftRemotePdhPortAlarmStatus,'rcftRemotePdhPortStatus':rcftRemotePdhPortStatus,'rcftRemotePdhPortECSCnt':rcftRemotePdhPortECSCnt,'rcftRemotePdhPortSECSCnt':rcftRemotePdhPortSECSCnt,'rcftRemotePdhPortLoopStatus':rcftRemotePdhPortLoopStatus,'rcftRemotePdhPortOrder':rcftRemotePdhPortOrder,'rcftRemotePdhPortBertStatus':rcftRemotePdhPortBertStatus,'rcftRemotePdhPortBertErrCode':rcftRemotePdhPortBertErrCode,'rcftRemotePdhPortPerformance':rcftRemotePdhPortPerformance,'rcftRemotePdhPortTraps':rcftRemotePdhPortTraps,'rcftRemotePdhPortLOSTrap':rcftRemotePdhPortLOSTrap,'rcftRemotePdhPortLOFTrap':rcftRemotePdhPortLOFTrap,'rcftRemotePdhPortE3Trap':rcftRemotePdhPortE3Trap,'rcftRemotePdhPortE6Trap':rcftRemotePdhPortE6Trap,'rcftRemotePdhPortToLLOSTrap':rcftRemotePdhPortToLLOSTrap,'rcftRemotePdhPortToLLOFTrap':rcftRemotePdhPortToLLOFTrap,'rcftRemotePdhPortToLE3Trap':rcftRemotePdhPortToLE3Trap,'rcftRemotePdhPortToLE6rap':rcftRemotePdhPortToLE6rap,'rcftRemotePdhPortToRPowerDown':rcftRemotePdhPortToRPowerDown,'rcftRemoteDS1PortMIB':rcftRemoteDS1PortMIB,'rcftRemoteDS1PortObjects':rcftRemoteDS1PortObjects,'rcftRemoteDS1PortTable':rcftRemoteDS1PortTable,'rcftRemoteDS1PortEntry':rcftRemoteDS1PortEntry,_AP:rcftRemoteDS1PortIndex,_N:rcftRemoteDS1PortAlarmStatus,'rcftRemoteDS1PortStatus':rcftRemoteDS1PortStatus,'rcftRemoteDS1PortESCont':rcftRemoteDS1PortESCont,'rcftRemoteDS1PortSESCont':rcftRemoteDS1PortSESCont,'rcftRemoteDS1PortBertStatus':rcftRemoteDS1PortBertStatus,'rcftRemoteDS1PortFaultPass':rcftRemoteDS1PortFaultPass,'rcftRemoteDS1PortLoopStatus':rcftRemoteDS1PortLoopStatus,'rcftRemoteDS1PortOrder':rcftRemoteDS1PortOrder,'rcftRemoteDS1PortTranLength':rcftRemoteDS1PortTranLength,_B1:rcftRemoteDS1PortFaultPassIndicator,'rcftRemoteDS1PortframeType':rcftRemoteDS1PortframeType,'rcftRemoteDS1PortChannel':rcftRemoteDS1PortChannel,'rcftRemoteDS1PortPerformance':rcftRemoteDS1PortPerformance,'rcftRemoteDS1StatisticTable':rcftRemoteDS1StatisticTable,_Af:rcftRemoteDS1StatisticEntry,'rcftRemoteDS1TxPackets':rcftRemoteDS1TxPackets,'rcftRemoteDS1TxBytes':rcftRemoteDS1TxBytes,'rcftRemoteDS1TxFailurePackets':rcftRemoteDS1TxFailurePackets,'rcftRemoteDS1RxPackets':rcftRemoteDS1RxPackets,'rcftRemoteDS1RxBytes':rcftRemoteDS1RxBytes,'rcftRemoteDS1RxErrorPackets':rcftRemoteDS1RxErrorPackets,'rcftRemoteDS1FluxTimer':rcftRemoteDS1FluxTimer,'rcftRemoteDS1PortTraps':rcftRemoteDS1PortTraps,'rcftRemoteDS1PortAISTrap':rcftRemoteDS1PortAISTrap,'rcftRemoteDS1PortLOSTrap':rcftRemoteDS1PortLOSTrap,'rcftRemoteDS1PortToLAISTrap':rcftRemoteDS1PortToLAISTrap,'rcftRemoteDS1PortToLLOSTrap':rcftRemoteDS1PortToLLOSTrap,'rcftRemoteDS1PortLOFTrap':rcftRemoteDS1PortLOFTrap,'rcftRemoteDS1PortCRCTrap':rcftRemoteDS1PortCRCTrap,'rcftRemoteDS1PortToLLOFTrap':rcftRemoteDS1PortToLLOFTrap,'rcftRemoteDS1PortToLCRCTrap':rcftRemoteDS1PortToLCRCTrap,'rcftRemoteDS1PortFaultPassIndicatorTrap':rcftRemoteDS1PortFaultPassIndicatorTrap,'rcftRemoteDS1PortDMOTrap':rcftRemoteDS1PortDMOTrap,'rcftRemoteDS1PortCVTrap':rcftRemoteDS1PortCVTrap,'rcftRemoteDS1PortYELTrap':rcftRemoteDS1PortYELTrap,'rcftRemoteDS1PortREDTrap':rcftRemoteDS1PortREDTrap,'rcftRemoteMoudleMIB':rcftRemoteMoudleMIB,'rcftRemoteMoudle':rcftRemoteMoudle,'rcftRemoteMoudleObjects':rcftRemoteMoudleObjects,'rcftRemoteMoudleTable':rcftRemoteMoudleTable,'rcftRemoteMoudleEntry':rcftRemoteMoudleEntry,_W:rcftRemoteMoudleIndex,_B2:rcftRemoteMoudleExist,'rcftRemoteMoudleType':rcftRemoteMoudleType,'rcftRemoteMoudleStatus':rcftRemoteMoudleStatus,'rcftRemoteMoudleSigleChipDescr':rcftRemoteMoudleSigleChipDescr,'rcftRemoteMoudleHardWareDescr':rcftRemoteMoudleHardWareDescr,'rcftRemoteMoudleFPGADescr':rcftRemoteMoudleFPGADescr,'rcftRemoteMoudleOrder':rcftRemoteMoudleOrder,'rcftRemoteMoudleIFOrder':rcftRemoteMoudleIFOrder,'rcftRemoteMoudleTraps':rcftRemoteMoudleTraps,'rcftRemoteMoudleExistTrap':rcftRemoteMoudleExistTrap,'rcftRemoteMoudleEthFe':rcftRemoteMoudleEthFe,'rcftRemoteMoudleEthFeObjects':rcftRemoteMoudleEthFeObjects,'rcftRemoteMoudleEthFeTable':rcftRemoteMoudleEthFeTable,'rcftRemoteMoudleEthFeEntry':rcftRemoteMoudleEthFeEntry,_AQ:rcftRemoteMoudleEthFeIndex,_B3:rcftRemoteMoudleEthFeStatus,'rcftRemoteMoudleEthFeRxRestrictSpeed':rcftRemoteMoudleEthFeRxRestrictSpeed,'rcftRemoteMoudleEthFeTxRestrictSpeed':rcftRemoteMoudleEthFeTxRestrictSpeed,'rcftRemoteMoudleEthFeRestrictSpeedStep':rcftRemoteMoudleEthFeRestrictSpeedStep,'rcftRemoteMoudleEthFeAlarmStatus':rcftRemoteMoudleEthFeAlarmStatus,'rcftRemoteMoudleEthFePerformance':rcftRemoteMoudleEthFePerformance,'rcftRemoteMoudleEthFeStatisticTable':rcftRemoteMoudleEthFeStatisticTable,_Ag:rcftRemoteMoudleEthFeStatisticEntry,'rcftRemoteMoudleEthFeTxPackets':rcftRemoteMoudleEthFeTxPackets,'rcftRemoteMoudleEthFeTxBytes':rcftRemoteMoudleEthFeTxBytes,'rcftRemoteMoudleEthFeTxFailurePackets':rcftRemoteMoudleEthFeTxFailurePackets,'rcftRemoteMoudleEthFeRxPackets':rcftRemoteMoudleEthFeRxPackets,'rcftRemoteMoudleEthFeRxBytes':rcftRemoteMoudleEthFeRxBytes,'rcftRemoteMoudleEthFeRxErrorPackets':rcftRemoteMoudleEthFeRxErrorPackets,'rcftRemoteMoudleEthFeFluxTimer':rcftRemoteMoudleEthFeFluxTimer,'rcftRemoteMoudleEthFeTraps':rcftRemoteMoudleEthFeTraps,'rcftRemoteMoudleEthFeLinkTrap':rcftRemoteMoudleEthFeLinkTrap,'rcftRemoteMoudlePdh':rcftRemoteMoudlePdh,'rcftRemoteMoudlePdhObjects':rcftRemoteMoudlePdhObjects,'rcftRemoteMoudlePdhTable':rcftRemoteMoudlePdhTable,'rcftRemoteMoudlePdhEntry':rcftRemoteMoudlePdhEntry,_AR:rcftRemoteMoudlePdhIndex,_t:rcftRemoteMoudlePdhAlarmStatus,'rcftRemoteMoudlePdhStatus':rcftRemoteMoudlePdhStatus,'rcftRemoteMoudlePdhTraps':rcftRemoteMoudlePdhTraps,'rcftRemoteMoudlePdhLOSTrap':rcftRemoteMoudlePdhLOSTrap,'rcftRemoteMoudlePdhLOFTrap':rcftRemoteMoudlePdhLOFTrap,'rcftRemoteMoudleE1':rcftRemoteMoudleE1,'rcftRemoteMoudleE1Objects':rcftRemoteMoudleE1Objects,'rcftRemoteMoudleE1Table':rcftRemoteMoudleE1Table,'rcftRemoteMoudleE1Entry':rcftRemoteMoudleE1Entry,_AS:rcftRemoteMoudleE1Index,_Y:rcftRemoteMoudleE1AlarmStatus,_B4:rcftRemoteMoudleE1Status,'rcftRemoteMoudleE1TimeSlots':rcftRemoteMoudleE1TimeSlots,'rcftRemoteMoudleE1TS0Mode':rcftRemoteMoudleE1TS0Mode,'rcftRemoteMoudleE1LoopStatus':rcftRemoteMoudleE1LoopStatus,'rcftRemoteMoudleE1ESCnt':rcftRemoteMoudleE1ESCnt,'rcftRemoteMoudleE1SESCnt':rcftRemoteMoudleE1SESCnt,'rcftRemoteMoudleE1Performance':rcftRemoteMoudleE1Performance,'rcftRemoteMoudleE1StatisticTable':rcftRemoteMoudleE1StatisticTable,_Ah:rcftRemoteMoudleE1StatisticEntry,'rcftRemoteMoudleE1TxPackets':rcftRemoteMoudleE1TxPackets,'rcftRemoteMoudleE1TxBytes':rcftRemoteMoudleE1TxBytes,'rcftRemoteMoudleE1TxFailurePackets':rcftRemoteMoudleE1TxFailurePackets,'rcftRemoteMoudleE1RxPackets':rcftRemoteMoudleE1RxPackets,'rcftRemoteMoudleE1RxBytes':rcftRemoteMoudleE1RxBytes,'rcftRemoteMoudleE1RxErrorPackets':rcftRemoteMoudleE1RxErrorPackets,'rcftRemoteMoudleE1FluxTimer':rcftRemoteMoudleE1FluxTimer,'rcftRemoteMoudleE1Traps':rcftRemoteMoudleE1Traps,'rcftRemoteMoudleE1LOSTrap':rcftRemoteMoudleE1LOSTrap,'rcftRemoteMoudleE1AISTrap':rcftRemoteMoudleE1AISTrap,'rcftRemoteMoudleE1CRCTrap':rcftRemoteMoudleE1CRCTrap,'rcftRemoteMoudleE1CVTrap':rcftRemoteMoudleE1CVTrap,'rcftRemoteMoudleE1LOFTrap':rcftRemoteMoudleE1LOFTrap,'rcftRemoteMoudleE1ErrorCodeTrap':rcftRemoteMoudleE1ErrorCodeTrap,'rcftRemoteMoudleV35':rcftRemoteMoudleV35,'rcftRemoteMoudleV35Objects':rcftRemoteMoudleV35Objects,'rcftRemoteMoudleV35Table':rcftRemoteMoudleV35Table,'rcftRemoteMoudleV35Entry':rcftRemoteMoudleV35Entry,_AT:rcftRemoteMoudleV35Index,'rcftRemoteMoudleV35AlarmStatus':rcftRemoteMoudleV35AlarmStatus,'rcftRemoteMoudleV35Status':rcftRemoteMoudleV35Status,'rcftRemoteMoudleV35Traps':rcftRemoteMoudleV35Traps,'rcftRemoteAudioPortMIB':rcftRemoteAudioPortMIB,'rcftRemoteAudioPortObjects':rcftRemoteAudioPortObjects,'rcftRemoteAudioPortTable':rcftRemoteAudioPortTable,'rcftRemoteAudioPortEntry':rcftRemoteAudioPortEntry,_AU:rcftRemoteAudioPortIndex,'rcftRemoteAudioPortStatus':rcftRemoteAudioPortStatus,'rcftRemoteAudioPortPosition':rcftRemoteAudioPortPosition,'rcftRemoteAudioPortType':rcftRemoteAudioPortType,'rcftRemoteAudioPortPerformance':rcftRemoteAudioPortPerformance,'rcftRemoteAudioPortTraps':rcftRemoteAudioPortTraps,'rcftRemoteVideoPortMIB':rcftRemoteVideoPortMIB,'rcftRemoteVideoPortObjects':rcftRemoteVideoPortObjects,'rcftRemoteVideoPortTable':rcftRemoteVideoPortTable,'rcftRemoteVideoPortEntry':rcftRemoteVideoPortEntry,_AV:rcftRemoteVideoPortIndex,_f:rcftRemoteVideoPortStatus,'rcftRemoteVideoPortPosition':rcftRemoteVideoPortPosition,'rcftRemoteVideoPortSourceID':rcftRemoteVideoPortSourceID,'rcftRemoteVideoPortPerformance':rcftRemoteVideoPortPerformance,'rcftRemoteVideoPortTraps':rcftRemoteVideoPortTraps,'rcftRemoteVideoPortSignalLos':rcftRemoteVideoPortSignalLos,'rcftRemoteVideoPortSignalInLos':rcftRemoteVideoPortSignalInLos,'rcftRemoteVideoPortSignalOutLos':rcftRemoteVideoPortSignalOutLos,'rcftRemoteDataPortMIB':rcftRemoteDataPortMIB,'rcftRemoteDataPortObjects':rcftRemoteDataPortObjects,'rcftRemoteDataPortTable':rcftRemoteDataPortTable,'rcftRemoteDataPortEntry':rcftRemoteDataPortEntry,_AW:rcftRemoteDataPortIndex,'rcftRemoteDataPortStatus':rcftRemoteDataPortStatus,'rcftRemoteDataPortPosition':rcftRemoteDataPortPosition,'rcftRemoteDataPortType':rcftRemoteDataPortType,'rcftRemoteDataPortPerformance':rcftRemoteDataPortPerformance,'rcftRemoteDataPortTraps':rcftRemoteDataPortTraps,'rcftRemoteSimpleModuleMIB':rcftRemoteSimpleModuleMIB,'rcftRemoteSimpleModuleObjects':rcftRemoteSimpleModuleObjects,'rcftRemoteSimpleModuleTable':rcftRemoteSimpleModuleTable,'rcftRemoteSimpleModuleEntry':rcftRemoteSimpleModuleEntry,_AX:rcftRemoteSimpleModuleIndex,'rcftRemoteSimpleModuleExist':rcftRemoteSimpleModuleExist,'rcftRemoteSimpleModulePosition':rcftRemoteSimpleModulePosition,'rcftRemoteSimpleModuleStatus':rcftRemoteSimpleModuleStatus,'rcftRemoteSimpleModuleType':rcftRemoteSimpleModuleType,'rcftRemoteSimpleModulePerformance':rcftRemoteSimpleModulePerformance,'rcftRemoteSimpleModuleTraps':rcftRemoteSimpleModuleTraps,'rcftRemoteVLANMIB':rcftRemoteVLANMIB,'rcftRemoteVLANObjects':rcftRemoteVLANObjects,'rcftRemoteVLANTable':rcftRemoteVLANTable,'rcftRemoteVLANEntry':rcftRemoteVLANEntry,_AY:rcftRemoteVLANIndex,'rcftRemoteVLANStatus':rcftRemoteVLANStatus,'rcftRemoteVLANmember':rcftRemoteVLANmember,'rcftRemoteVID':rcftRemoteVID,'rcftRemotePerformaceMib':rcftRemotePerformaceMib,'rcftRemoteStatisticPerformance':rcftRemoteStatisticPerformance,'rcftRemoteStatisticTable':rcftRemoteStatisticTable,'rcftRemoteStatisticEntry':rcftRemoteStatisticEntry,_AZ:rcftRemotePortIndex,'rcftRemotePortType':rcftRemotePortType,'rcftRemoteRxPackets':rcftRemoteRxPackets,'rcftRemoteRxLosPackets':rcftRemoteRxLosPackets,'rcftRemoteRxPreabErrPackets':rcftRemoteRxPreabErrPackets,'rcftRemoteRxFCSErrPackets':rcftRemoteRxFCSErrPackets,'rcftRemoteRxUnderSizePackets':rcftRemoteRxUnderSizePackets,'rcftRemoteRxOverSizePackets':rcftRemoteRxOverSizePackets,'rcftRemoteRxPausePackets':rcftRemoteRxPausePackets,'rcftRemoteRxOamPackets':rcftRemoteRxOamPackets,'rcftRemoteRxBytes':rcftRemoteRxBytes,'rcftRemoteTxPackets':rcftRemoteTxPackets,'rcftRemoteTxFCSErrPackets':rcftRemoteTxFCSErrPackets,'rcftRemoteTxPausePackets':rcftRemoteTxPausePackets,'rcftRemoteTxOamPackets':rcftRemoteTxOamPackets,'rcftRemoteTxBytes':rcftRemoteTxBytes,'rcftRemoteFluxTimer':rcftRemoteFluxTimer,'rcftRemoteVCGMib':rcftRemoteVCGMib,'rcftRemoteVCGObjects':rcftRemoteVCGObjects,'rcftRemoteVCGTable':rcftRemoteVCGTable,'rcftRemoteVCGEntry':rcftRemoteVCGEntry,_Aa:rcftRemoteVCGIndex,'rcftRemoteVCGStatus':rcftRemoteVCGStatus,'rcftRemoteVCGLoopStatus':rcftRemoteVCGLoopStatus,'rcftRemoteVCGLcasXPR':rcftRemoteVCGLcasXPR,'rcftRemoteVCGLcasXAR':rcftRemoteVCGLcasXAR,'rcftRemoteVCGLcasXPT':rcftRemoteVCGLcasXPT,'rcftRemoteVCGLcasXAT':rcftRemoteVCGLcasXAT,_T:rcftRemoteVCGAlarmStatus,'rcftRemoteVCGRxISPTPID':rcftRemoteVCGRxISPTPID,'rcftRemoteVCGTxISPTPID':rcftRemoteVCGTxISPTPID,'rcftRemoteVCGBaseCoS':rcftRemoteVCGBaseCoS,'rcftRemoteVCGVLANID':rcftRemoteVCGVLANID,'rcftRemoteVCGMemberList':rcftRemoteVCGMemberList,'rcftRemoteVCGMemberStatus':rcftRemoteVCGMemberStatus,'rcftRemoteVCGMemberRxCode':rcftRemoteVCGMemberRxCode,'rcftRemoteVCGMemberTxCode':rcftRemoteVCGMemberTxCode,_d:rcftRemoteVCGMemberAlarmStatus,_e:rcftRemoteToLVCGMemberAlarmStatus,'rcftRemoteVCGPerformance':rcftRemoteVCGPerformance,'rcftRemoteVCGStatisticTable':rcftRemoteVCGStatisticTable,_Ai:rcftRemoteVCGStatisticEntry,'rcftRemoteVCGRxClientPackets':rcftRemoteVCGRxClientPackets,'rcftRemoteVCGRxIdlePackets':rcftRemoteVCGRxIdlePackets,'rcftRemoteVCGRxMgmntPackets':rcftRemoteVCGRxMgmntPackets,'rcftRemoteVCGRxFCSErrMgmntPackets':rcftRemoteVCGRxFCSErrMgmntPackets,'rcftRemoteVCGRxLenErrPackets':rcftRemoteVCGRxLenErrPackets,'rcftRemoteVCGRxFCSErrClientPackets':rcftRemoteVCGRxFCSErrClientPackets,'rcftRemoteVCGRxThecErrPackets':rcftRemoteVCGRxThecErrPackets,'rcftRemoteVCGRxEhecErrPackets':rcftRemoteVCGRxEhecErrPackets,'rcftRemoteVCGRxCIDErrPackets':rcftRemoteVCGRxCIDErrPackets,'rcftRemoteVCGRxSpareErrPackets':rcftRemoteVCGRxSpareErrPackets,'rcftRemoteVCGRxChecCorPackets':rcftRemoteVCGRxChecCorPackets,'rcftRemoteVCGRxThecCorPackets':rcftRemoteVCGRxThecCorPackets,'rcftRemoteVCGRxEhecCorPackets':rcftRemoteVCGRxEhecCorPackets,'rcftRemoteVCGRxBytes':rcftRemoteVCGRxBytes,'rcftRemoteVCGTxClientPackets':rcftRemoteVCGTxClientPackets,'rcftRemoteVCGTxIdlePackets':rcftRemoteVCGTxIdlePackets,'rcftRemoteVCGTxMgmntPackets':rcftRemoteVCGTxMgmntPackets,'rcftRemoteVCGTxBytes':rcftRemoteVCGTxBytes,'rcftRemoteVCGFluxTimer':rcftRemoteVCGFluxTimer,'rcftRemoteVCGTraps':rcftRemoteVCGTraps,'rcftRemoteVCGGIDTraps':rcftRemoteVCGGIDTraps,'rcftRemoteVCGLOATraps':rcftRemoteVCGLOATraps,'rcftRemoteVCGLFDTraps':rcftRemoteVCGLFDTraps,'rcftRemoteVCGCSFTraps':rcftRemoteVCGCSFTraps,'rcftRemoteVCGTLCTTraps':rcftRemoteVCGTLCTTraps,'rcftRemoteVCGTLCRTraps':rcftRemoteVCGTLCRTraps,'rcftRemoteVCGToLGIDTraps':rcftRemoteVCGToLGIDTraps,'rcftRemoteVCGToLLOATraps':rcftRemoteVCGToLLOATraps,'rcftRemoteVCGToLLFDTraps':rcftRemoteVCGToLLFDTraps,'rcftRemoteVCGMemberLOMTraps':rcftRemoteVCGMemberLOMTraps,'rcftRemoteVCGMemberSQMTraps':rcftRemoteVCGMemberSQMTraps,'rcftRemoteVCGMemberCRCTraps':rcftRemoteVCGMemberCRCTraps,'rcftRemoteVCGMemberLOATraps':rcftRemoteVCGMemberLOATraps,'rcftRemoteVCGToLMemberLOMTraps':rcftRemoteVCGToLMemberLOMTraps,'rcftRemoteVCGToLMemberSQMTraps':rcftRemoteVCGToLMemberSQMTraps,'rcftRemoteVCGToLMemberCRCTraps':rcftRemoteVCGToLMemberCRCTraps,'rcftRemoteVCGToLMemberLOATraps':rcftRemoteVCGToLMemberLOATraps})