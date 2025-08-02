_Aq='oaLdCardEntityOptDwdmRx'
_Ap='oaLdCardEntityOptAccRx'
_Ao='oaLdCardPortsLink'
_An='oaLdRedOptSecondaryRx'
_Am='oaLdRedOptPrimaryRx'
_Al='oaLdCardOptDwdmRx'
_Ak='oaLdCardOptAccRx'
_Aj='oaLdDcmCardPortsPortNumber'
_Ai='oaLdDcmCardPortsSlotNumber'
_Ah='oaLdPeaksMonitorPeakNumber'
_Ag='oaLdPeaksMonitorPortNumber'
_Af='oaLdPeaksMonitorSlotNumber'
_Ae='oaLdMeasurmentPointsPortNumber'
_Ad='oaLdMeasurmentPointsSlotNumber'
_Ac='oaLdPortsCrossConnectPortNumber'
_Ab='oaLdPortsCrossConnectSlotNumber'
_Aa='oaLdRoadmPortThresholdIndex'
_AZ='oaLdRoadmPortThresholdPortIndex'
_AY='oaLdRoadmPortThresholdSlotIndex'
_AX='oaLdRoadmPortPortNumber'
_AW='oaLdRoadmPortSlotNumber'
_AV='hysteresisFailHigh'
_AU='hysteresisFailLow'
_AT='hysteresisDegradeHigh'
_AS='hysteresisDegradeLow'
_AR='degradeHigh'
_AQ='degradeLow'
_AP='oaLdRoadmThresholdIndex'
_AO='oaLdRoadmThresholdSlotNumber'
_AN='oaLdRoadmChannelPortNumber'
_AM='oaLdRoadmChannelLambdaChannel'
_AL='oaLdRoadmChannelSlotNumber'
_AK='oaLdRoadmMonitorSlotNumber'
_AJ='operating'
_AI='oaLdRoadmSlotNumber'
_AH='oaLdOcmCardPortsPortNumber'
_AG='oaLdOcmCardPortsSlotNumber'
_AF='oaLdOAmplifierPumpNumber'
_AE='oaLdCardChChannelId'
_AD='oaLdCardChGroupId'
_AC='oaLdCardChSlotId'
_AB='oaLdAdcCardPortsPortNumber'
_AA='oaLdAdcCardPortsSlotNumber'
_A9='oaLdAdcCardSlotNumber'
_A8='supported'
_A7='automatic'
_A6='inProgress'
_A5='redundant'
_A4='oaLdDevCPUIndex'
_A3='notActive'
_A2='hd1001sdi'
_A1='fiberChannel8giga'
_A0='fiberChannel4250'
_z='eth10giga'
_y='fiberChannel531'
_x='fiberChannel256'
_w='bypass'
_v='fiberChannel2125'
_u='fiberChannel1062'
_t='NotificationType'
_s='oaLdCardEntityClockSource'
_r='oaLdOAmplifierCardSlotNumber'
_q='drop'
_p='add'
_o='primary'
_n='secondary'
_m='localLoopback'
_l='remoteLoopback'
_k='loopback'
_j='active'
_i='oaLdCardPortsLoopBack'
_h='oaLdCardEntityLoopBack'
_g='oaLdCardLoopBack'
_f='done'
_e='percent'
_d='ps/nm'
_c='manual'
_b='high'
_a='ok'
_Z='fail'
_Y='oaLdDevFANIndex'
_X='OctetString'
_W='none'
_V='oaLdDevPSIndex'
_U='oaLdRedOptSlotNumber'
_T='notSupported'
_S='normal'
_R='oaLdCardEntityEntityIndex'
_Q='oaLdCardEntityCardIndex'
_P='oaLdCardPortsPortNumber'
_O='oaLdCardIndex'
_N='enable'
_M='off'
_L='on'
_K='disable'
_J='DisplayString'
_I='oaDevTrapsPortsIfAlias'
_H='OA-TRAP-MESSAGES-MIB'
_G='oaLdCardPortsSlotNumber'
_F='read-write'
_E='other'
_D='Integer32'
_C='OADWDM-MIB'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_X,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
oaDevTrapsPortsIfAlias,=mibBuilder.importSymbols(_H,_I)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier',_t,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_t,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_J,'PhysAddress','TextualConvention')
class LambdaCh(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108)));namedValues=NamedValues(*((_E,1),('ch21',2),('ch23',3),('ch25',4),('ch27',5),('ch29',6),('ch31',7),('ch33',8),('ch35',9),('ch37',10),('ch39',11),('ch41',12),('ch43',13),('ch45',14),('ch47',15),('ch49',16),('ch51',17),('ch53',18),('ch55',19),('ch57',20),('ch59',21),('wl1470',31),('wl1490',32),('wl1510',33),('wl1530',34),('wl1550',35),('wl1570',36),('wl1590',37),('wl1610',38),('wl1310',39),('wl1310sm',40),('wl1330',41),('wl1350',42),('wl1370',43),('wl1390',44),('wl1410',45),('wl1430',46),('wl1450',47),('ch20',48),('ch22',49),('ch24',50),('ch26',51),('ch28',52),('ch30',53),('ch32',54),('ch34',55),('ch36',56),('ch38',57),('ch40',58),('ch42',59),('ch44',60),('ch46',61),('ch48',62),('ch50',63),('ch52',64),('ch54',65),('ch56',66),('ch58',67),('ch60',68),('ch205',69),('ch225',70),('ch245',71),('ch265',72),('ch285',73),('ch305',74),('ch325',75),('ch345',76),('ch365',77),('ch385',78),('ch405',79),('ch425',80),('ch445',81),('ch465',82),('ch485',83),('ch505',84),('ch525',85),('ch545',86),('ch565',87),('ch585',88),('ch215',89),('ch235',90),('ch255',91),('ch275',92),('ch295',93),('ch315',94),('ch335',95),('ch355',96),('ch375',97),('ch395',98),('ch415',99),('ch435',100),('ch455',101),('ch475',102),('ch495',103),('ch515',104),('ch535',105),('ch555',106),('ch575',107),('ch595',108)))
class RateSelect(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53)));namedValues=NamedValues(*((_E,1),('oc3',2),('oc12',3),('oc48',4),('giga',5),(_u,6),(_v,7),('fastEthernet',8),('escon',9),('stm1',10),('stm4',11),('stm16',12),(_w,13),('e3',14),('e32',15),('ds3',16),('oc1',17),('ds3c',18),('fddi',19),('e4',20),('dtv',21),(_x,22),('ds4',23),('cmi',24),('hdtv',25),('hdtv2',26),('dtv2',27),(_y,28),('ds5',29),('oc24',30),('ds5x',31),('hdtv3',32),(_z,33),('oc192',34),(_A0,35),('stm64',36),('otu2',37),('sonetSdh10giga',38),('fiberChannel10giga',39),(_A1,40),('tdm10giga',41),('smpte292',42),('eth10M',43),('otu1',44),('sdi143',45),('sdi270',46),('sdi360',47),('sdi540',48),('hdsdi',49),('sdi3g',50),(_A2,51),('otu4',52),('eth100g',53)))
class RateMode(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51)));namedValues=NamedValues(*((_E,1),('oc3',2),('oc3c',3),('oc12au3',4),('oc12c',5),('oc12au4',6),(_u,7),(_v,8),('oc48',9),('oc48c',10),(_z,11),('oc192',12),('stm64',13),('stm16',14),('fiberChannel10519',15),('eth10gigaWan',16),('eth10gigaDi',17),('eth100M',18),('eth1giga',19),(_A0,20),('otu0',21),('otu1',22),('otu2',23),('sdi143',24),('sdi270',25),('sdi360',26),('hdsdi',27),('sdi3g',28),('otu3',29),('oc768',30),('stm256',31),('eth40giga',32),(_A2,33),('sdi177',34),('sdi540',35),('dvbasi',36),('smpte292',37),('eth10M',38),('escon',39),(_x,40),(_y,41),(_w,42),('gm2-eth',43),('gm2-fc',44),('e3',45),('cpri614',46),('cpri1228',47),('cpri2457',48),('cpri3072',49),('cpri4915',50),(_A1,51)))
_Oaccess_ObjectIdentity=ObjectIdentity
oaccess=_Oaccess_ObjectIdentity((1,3,6,1,4,1,6926))
_OaManagement_ObjectIdentity=ObjectIdentity
oaManagement=_OaManagement_ObjectIdentity((1,3,6,1,4,1,6926,1))
_OaLambdaDriver_ObjectIdentity=ObjectIdentity
oaLambdaDriver=_OaLambdaDriver_ObjectIdentity((1,3,6,1,4,1,6926,1,41))
_OaLdDevIdentify_ObjectIdentity=ObjectIdentity
oaLdDevIdentify=_OaLdDevIdentify_ObjectIdentity((1,3,6,1,4,1,6926,1,41,1))
_OaLdNSlots_Type=Integer32
_OaLdNSlots_Object=MibScalar
oaLdNSlots=_OaLdNSlots_Object((1,3,6,1,4,1,6926,1,41,1,1),_OaLdNSlots_Type())
oaLdNSlots.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdNSlots.setStatus(_A)
_OaLdCardHardVers_Type=Integer32
_OaLdCardHardVers_Object=MibScalar
oaLdCardHardVers=_OaLdCardHardVers_Object((1,3,6,1,4,1,6926,1,41,1,2),_OaLdCardHardVers_Type())
oaLdCardHardVers.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdCardHardVers.setStatus(_A)
_OaLdSoftVers_Type=Integer32
_OaLdSoftVers_Object=MibScalar
oaLdSoftVers=_OaLdSoftVers_Object((1,3,6,1,4,1,6926,1,41,1,3),_OaLdSoftVers_Type())
oaLdSoftVers.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdSoftVers.setStatus(_A)
_OaLdCreatinDate_Type=DisplayString
_OaLdCreatinDate_Object=MibScalar
oaLdCreatinDate=_OaLdCreatinDate_Object((1,3,6,1,4,1,6926,1,41,1,4),_OaLdCreatinDate_Type())
oaLdCreatinDate.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdCreatinDate.setStatus(_A)
class _OaLdDeviceType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14)));namedValues=NamedValues(*((_E,1),('ld800',2),('ld1600',3),('ld400',4),('ld800P',5),('ld1600L',6),('ld400L',7),('ld400P',8),('ld1600P',9),('ld200',10),('ld200L',11),('ld400i',12),('ld100G',13),('ld400iL',14)))
_OaLdDeviceType_Type.__name__=_D
_OaLdDeviceType_Object=MibScalar
oaLdDeviceType=_OaLdDeviceType_Object((1,3,6,1,4,1,6926,1,41,1,5),_OaLdDeviceType_Type())
oaLdDeviceType.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdDeviceType.setStatus(_A)
_OaLdCardFpgaVers_Type=Integer32
_OaLdCardFpgaVers_Object=MibScalar
oaLdCardFpgaVers=_OaLdCardFpgaVers_Object((1,3,6,1,4,1,6926,1,41,1,6),_OaLdCardFpgaVers_Type())
oaLdCardFpgaVers.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdCardFpgaVers.setStatus(_A)
_OaLdCardBackplaneVers_Type=Integer32
_OaLdCardBackplaneVers_Object=MibScalar
oaLdCardBackplaneVers=_OaLdCardBackplaneVers_Object((1,3,6,1,4,1,6926,1,41,1,7),_OaLdCardBackplaneVers_Type())
oaLdCardBackplaneVers.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdCardBackplaneVers.setStatus(_A)
_OaLdTrapsVer_Type=Integer32
_OaLdTrapsVer_Object=MibScalar
oaLdTrapsVer=_OaLdTrapsVer_Object((1,3,6,1,4,1,6926,1,41,1,8),_OaLdTrapsVer_Type())
oaLdTrapsVer.setMaxAccess(_F)
if mibBuilder.loadTexts:oaLdTrapsVer.setStatus(_A)
class _OaLdCpuCardSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(10,10));fixedLength=10
_OaLdCpuCardSerialNumber_Type.__name__=_J
_OaLdCpuCardSerialNumber_Object=MibScalar
oaLdCpuCardSerialNumber=_OaLdCpuCardSerialNumber_Object((1,3,6,1,4,1,6926,1,41,1,9),_OaLdCpuCardSerialNumber_Type())
oaLdCpuCardSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdCpuCardSerialNumber.setStatus(_A)
_OaLdDevGenConfig_ObjectIdentity=ObjectIdentity
oaLdDevGenConfig=_OaLdDevGenConfig_ObjectIdentity((1,3,6,1,4,1,6926,1,41,1,10))
_OaLdDevPS_ObjectIdentity=ObjectIdentity
oaLdDevPS=_OaLdDevPS_ObjectIdentity((1,3,6,1,4,1,6926,1,41,1,10,1))
_OaLdDevPSNumber_Type=Integer32
_OaLdDevPSNumber_Object=MibScalar
oaLdDevPSNumber=_OaLdDevPSNumber_Object((1,3,6,1,4,1,6926,1,41,1,10,1,1),_OaLdDevPSNumber_Type())
oaLdDevPSNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdDevPSNumber.setStatus(_A)
_OaLdDevPSTable_Object=MibTable
oaLdDevPSTable=_OaLdDevPSTable_Object((1,3,6,1,4,1,6926,1,41,1,10,1,2))
if mibBuilder.loadTexts:oaLdDevPSTable.setStatus(_A)
_OaLdDevPSEntry_Object=MibTableRow
oaLdDevPSEntry=_OaLdDevPSEntry_Object((1,3,6,1,4,1,6926,1,41,1,10,1,2,1))
oaLdDevPSEntry.setIndexNames((0,_C,_V))
if mibBuilder.loadTexts:oaLdDevPSEntry.setStatus(_A)
_OaLdDevPSIndex_Type=Integer32
_OaLdDevPSIndex_Object=MibTableColumn
oaLdDevPSIndex=_OaLdDevPSIndex_Object((1,3,6,1,4,1,6926,1,41,1,10,1,2,1,1),_OaLdDevPSIndex_Type())
oaLdDevPSIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdDevPSIndex.setStatus(_A)
class _OaLdDevPSOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_W,1),(_j,2),(_A3,3)))
_OaLdDevPSOperStatus_Type.__name__=_D
_OaLdDevPSOperStatus_Object=MibTableColumn
oaLdDevPSOperStatus=_OaLdDevPSOperStatus_Object((1,3,6,1,4,1,6926,1,41,1,10,1,2,1,5),_OaLdDevPSOperStatus_Type())
oaLdDevPSOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdDevPSOperStatus.setStatus(_A)
class _OaLdDevPSPartNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_OaLdDevPSPartNumber_Type.__name__=_J
_OaLdDevPSPartNumber_Object=MibTableColumn
oaLdDevPSPartNumber=_OaLdDevPSPartNumber_Object((1,3,6,1,4,1,6926,1,41,1,10,1,2,1,6),_OaLdDevPSPartNumber_Type())
oaLdDevPSPartNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdDevPSPartNumber.setStatus(_A)
class _OaLdDevPSSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(10,10));fixedLength=10
_OaLdDevPSSerialNumber_Type.__name__=_J
_OaLdDevPSSerialNumber_Object=MibTableColumn
oaLdDevPSSerialNumber=_OaLdDevPSSerialNumber_Object((1,3,6,1,4,1,6926,1,41,1,10,1,2,1,7),_OaLdDevPSSerialNumber_Type())
oaLdDevPSSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdDevPSSerialNumber.setStatus(_A)
_OaLdDevPSHwRev_Type=Integer32
_OaLdDevPSHwRev_Object=MibTableColumn
oaLdDevPSHwRev=_OaLdDevPSHwRev_Object((1,3,6,1,4,1,6926,1,41,1,10,1,2,1,8),_OaLdDevPSHwRev_Type())
oaLdDevPSHwRev.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdDevPSHwRev.setStatus(_A)
_OaLdDevFAN_ObjectIdentity=ObjectIdentity
oaLdDevFAN=_OaLdDevFAN_ObjectIdentity((1,3,6,1,4,1,6926,1,41,1,10,3))
_OaLdDevFANsNumber_Type=Integer32
_OaLdDevFANsNumber_Object=MibScalar
oaLdDevFANsNumber=_OaLdDevFANsNumber_Object((1,3,6,1,4,1,6926,1,41,1,10,3,1),_OaLdDevFANsNumber_Type())
oaLdDevFANsNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdDevFANsNumber.setStatus(_A)
_OaLdDevFANTable_Object=MibTable
oaLdDevFANTable=_OaLdDevFANTable_Object((1,3,6,1,4,1,6926,1,41,1,10,3,2))
if mibBuilder.loadTexts:oaLdDevFANTable.setStatus(_A)
_OaLdDevFANEntry_Object=MibTableRow
oaLdDevFANEntry=_OaLdDevFANEntry_Object((1,3,6,1,4,1,6926,1,41,1,10,3,2,1))
oaLdDevFANEntry.setIndexNames((0,_C,_Y))
if mibBuilder.loadTexts:oaLdDevFANEntry.setStatus(_A)
_OaLdDevFANIndex_Type=Integer32
_OaLdDevFANIndex_Object=MibTableColumn
oaLdDevFANIndex=_OaLdDevFANIndex_Object((1,3,6,1,4,1,6926,1,41,1,10,3,2,1,1),_OaLdDevFANIndex_Type())
oaLdDevFANIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdDevFANIndex.setStatus(_A)
class _OaLdDevFANOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_W,1),(_j,2),(_A3,3),(_Z,4)))
_OaLdDevFANOperStatus_Type.__name__=_D
_OaLdDevFANOperStatus_Object=MibTableColumn
oaLdDevFANOperStatus=_OaLdDevFANOperStatus_Object((1,3,6,1,4,1,6926,1,41,1,10,3,2,1,5),_OaLdDevFANOperStatus_Type())
oaLdDevFANOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdDevFANOperStatus.setStatus(_A)
_OaLdDevCPU_ObjectIdentity=ObjectIdentity
oaLdDevCPU=_OaLdDevCPU_ObjectIdentity((1,3,6,1,4,1,6926,1,41,1,10,4))
_OaLdDevCPUNumber_Type=Integer32
_OaLdDevCPUNumber_Object=MibScalar
oaLdDevCPUNumber=_OaLdDevCPUNumber_Object((1,3,6,1,4,1,6926,1,41,1,10,4,1),_OaLdDevCPUNumber_Type())
oaLdDevCPUNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdDevCPUNumber.setStatus(_A)
_OaLdDevCPUTable_Object=MibTable
oaLdDevCPUTable=_OaLdDevCPUTable_Object((1,3,6,1,4,1,6926,1,41,1,10,4,10))
if mibBuilder.loadTexts:oaLdDevCPUTable.setStatus(_A)
_OaLdDevCPUEntry_Object=MibTableRow
oaLdDevCPUEntry=_OaLdDevCPUEntry_Object((1,3,6,1,4,1,6926,1,41,1,10,4,10,1))
oaLdDevCPUEntry.setIndexNames((0,_C,_A4))
if mibBuilder.loadTexts:oaLdDevCPUEntry.setStatus(_A)
_OaLdDevCPUIndex_Type=Integer32
_OaLdDevCPUIndex_Object=MibTableColumn
oaLdDevCPUIndex=_OaLdDevCPUIndex_Object((1,3,6,1,4,1,6926,1,41,1,10,4,10,1,1),_OaLdDevCPUIndex_Type())
oaLdDevCPUIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdDevCPUIndex.setStatus(_A)
class _OaLdDevCPUOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_j,2),('standby',3),('reset',4)))
_OaLdDevCPUOperStatus_Type.__name__=_D
_OaLdDevCPUOperStatus_Object=MibTableColumn
oaLdDevCPUOperStatus=_OaLdDevCPUOperStatus_Object((1,3,6,1,4,1,6926,1,41,1,10,4,10,1,2),_OaLdDevCPUOperStatus_Type())
oaLdDevCPUOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdDevCPUOperStatus.setStatus(_A)
class _OaLdDevCPUType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),('mgtd',2),('mgtp',3),('mngt',4)))
_OaLdDevCPUType_Type.__name__=_D
_OaLdDevCPUType_Object=MibTableColumn
oaLdDevCPUType=_OaLdDevCPUType_Object((1,3,6,1,4,1,6926,1,41,1,10,4,10,1,3),_OaLdDevCPUType_Type())
oaLdDevCPUType.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdDevCPUType.setStatus(_A)
_OaLdDevCPUHardVers_Type=Integer32
_OaLdDevCPUHardVers_Object=MibTableColumn
oaLdDevCPUHardVers=_OaLdDevCPUHardVers_Object((1,3,6,1,4,1,6926,1,41,1,10,4,10,1,4),_OaLdDevCPUHardVers_Type())
oaLdDevCPUHardVers.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdDevCPUHardVers.setStatus(_A)
_OaLdDevCPUFpgaVers_Type=Integer32
_OaLdDevCPUFpgaVers_Object=MibTableColumn
oaLdDevCPUFpgaVers=_OaLdDevCPUFpgaVers_Object((1,3,6,1,4,1,6926,1,41,1,10,4,10,1,5),_OaLdDevCPUFpgaVers_Type())
oaLdDevCPUFpgaVers.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdDevCPUFpgaVers.setStatus(_A)
class _OaLdDevCPUSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(10,10));fixedLength=10
_OaLdDevCPUSerialNumber_Type.__name__=_J
_OaLdDevCPUSerialNumber_Object=MibTableColumn
oaLdDevCPUSerialNumber=_OaLdDevCPUSerialNumber_Object((1,3,6,1,4,1,6926,1,41,1,10,4,10,1,6),_OaLdDevCPUSerialNumber_Type())
oaLdDevCPUSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdDevCPUSerialNumber.setStatus(_A)
_OaLdDevCPUBuildTime_Type=DisplayString
_OaLdDevCPUBuildTime_Object=MibTableColumn
oaLdDevCPUBuildTime=_OaLdDevCPUBuildTime_Object((1,3,6,1,4,1,6926,1,41,1,10,4,10,1,7),_OaLdDevCPUBuildTime_Type())
oaLdDevCPUBuildTime.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdDevCPUBuildTime.setStatus(_A)
_OaLdDevCPUSoftVers_Type=DisplayString
_OaLdDevCPUSoftVers_Object=MibTableColumn
oaLdDevCPUSoftVers=_OaLdDevCPUSoftVers_Object((1,3,6,1,4,1,6926,1,41,1,10,4,10,1,8),_OaLdDevCPUSoftVers_Type())
oaLdDevCPUSoftVers.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdDevCPUSoftVers.setStatus(_A)
_OaLdDevCPUBoardID_Type=Integer32
_OaLdDevCPUBoardID_Object=MibTableColumn
oaLdDevCPUBoardID=_OaLdDevCPUBoardID_Object((1,3,6,1,4,1,6926,1,41,1,10,4,10,1,9),_OaLdDevCPUBoardID_Type())
oaLdDevCPUBoardID.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdDevCPUBoardID.setStatus(_A)
_OaLdDevCPUBoardHardVers_Type=Integer32
_OaLdDevCPUBoardHardVers_Object=MibTableColumn
oaLdDevCPUBoardHardVers=_OaLdDevCPUBoardHardVers_Object((1,3,6,1,4,1,6926,1,41,1,10,4,10,1,10),_OaLdDevCPUBoardHardVers_Type())
oaLdDevCPUBoardHardVers.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdDevCPUBoardHardVers.setStatus(_A)
_OaLdDevRedundantCPU_ObjectIdentity=ObjectIdentity
oaLdDevRedundantCPU=_OaLdDevRedundantCPU_ObjectIdentity((1,3,6,1,4,1,6926,1,41,1,10,5))
class _OaLdDevRedundantFeature_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_N,2),(_K,3)))
_OaLdDevRedundantFeature_Type.__name__=_D
_OaLdDevRedundantFeature_Object=MibScalar
oaLdDevRedundantFeature=_OaLdDevRedundantFeature_Object((1,3,6,1,4,1,6926,1,41,1,10,5,1),_OaLdDevRedundantFeature_Type())
oaLdDevRedundantFeature.setMaxAccess(_F)
if mibBuilder.loadTexts:oaLdDevRedundantFeature.setStatus(_A)
class _OaLdDevRedundantMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_N,2),(_K,3)))
_OaLdDevRedundantMode_Type.__name__=_D
_OaLdDevRedundantMode_Object=MibScalar
oaLdDevRedundantMode=_OaLdDevRedundantMode_Object((1,3,6,1,4,1,6926,1,41,1,10,5,2),_OaLdDevRedundantMode_Type())
oaLdDevRedundantMode.setMaxAccess(_F)
if mibBuilder.loadTexts:oaLdDevRedundantMode.setStatus(_A)
class _OaLdDevRedundantCommand_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),('forceSwitchOver',2),('forceSync',3)))
_OaLdDevRedundantCommand_Type.__name__=_D
_OaLdDevRedundantCommand_Object=MibScalar
oaLdDevRedundantCommand=_OaLdDevRedundantCommand_Object((1,3,6,1,4,1,6926,1,41,1,10,5,3),_OaLdDevRedundantCommand_Type())
oaLdDevRedundantCommand.setMaxAccess(_F)
if mibBuilder.loadTexts:oaLdDevRedundantCommand.setStatus(_A)
class _OaLdDevRedundantPeerAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),('recover',2),('reboot',3),('shutdown',4)))
_OaLdDevRedundantPeerAdminStatus_Type.__name__=_D
_OaLdDevRedundantPeerAdminStatus_Object=MibScalar
oaLdDevRedundantPeerAdminStatus=_OaLdDevRedundantPeerAdminStatus_Object((1,3,6,1,4,1,6926,1,41,1,10,5,4),_OaLdDevRedundantPeerAdminStatus_Type())
oaLdDevRedundantPeerAdminStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:oaLdDevRedundantPeerAdminStatus.setStatus(_A)
_OaLdDevGenIdentify_ObjectIdentity=ObjectIdentity
oaLdDevGenIdentify=_OaLdDevGenIdentify_ObjectIdentity((1,3,6,1,4,1,6926,1,41,1,11))
class _OaLdCardBackplaneSN_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(10,10));fixedLength=10
_OaLdCardBackplaneSN_Type.__name__=_J
_OaLdCardBackplaneSN_Object=MibScalar
oaLdCardBackplaneSN=_OaLdCardBackplaneSN_Object((1,3,6,1,4,1,6926,1,41,1,11,1),_OaLdCardBackplaneSN_Type())
oaLdCardBackplaneSN.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdCardBackplaneSN.setStatus(_A)
_OaLdSoftVersString_Type=DisplayString
_OaLdSoftVersString_Object=MibScalar
oaLdSoftVersString=_OaLdSoftVersString_Object((1,3,6,1,4,1,6926,1,41,1,11,2),_OaLdSoftVersString_Type())
oaLdSoftVersString.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdSoftVersString.setStatus(_A)
class _OaLdCardBackplanePN_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_OaLdCardBackplanePN_Type.__name__=_J
_OaLdCardBackplanePN_Object=MibScalar
oaLdCardBackplanePN=_OaLdCardBackplanePN_Object((1,3,6,1,4,1,6926,1,41,1,11,3),_OaLdCardBackplanePN_Type())
oaLdCardBackplanePN.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdCardBackplanePN.setStatus(_A)
class _OaLdCardIftableExtMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_N,2),(_K,3)))
_OaLdCardIftableExtMode_Type.__name__=_D
_OaLdCardIftableExtMode_Object=MibScalar
oaLdCardIftableExtMode=_OaLdCardIftableExtMode_Object((1,3,6,1,4,1,6926,1,41,1,11,4),_OaLdCardIftableExtMode_Type())
oaLdCardIftableExtMode.setMaxAccess(_F)
if mibBuilder.loadTexts:oaLdCardIftableExtMode.setStatus(_A)
_OaLdSlotsStatTable_ObjectIdentity=ObjectIdentity
oaLdSlotsStatTable=_OaLdSlotsStatTable_ObjectIdentity((1,3,6,1,4,1,6926,1,41,3))
_OaLdCardsStatTable_Object=MibTable
oaLdCardsStatTable=_OaLdCardsStatTable_Object((1,3,6,1,4,1,6926,1,41,3,1))
if mibBuilder.loadTexts:oaLdCardsStatTable.setStatus(_A)
_OaLdCardsStatEntry_Object=MibTableRow
oaLdCardsStatEntry=_OaLdCardsStatEntry_Object((1,3,6,1,4,1,6926,1,41,3,1,1))
oaLdCardsStatEntry.setIndexNames((0,_C,_O))
if mibBuilder.loadTexts:oaLdCardsStatEntry.setStatus(_A)
_OaLdCardIndex_Type=Integer32
_OaLdCardIndex_Object=MibTableColumn
oaLdCardIndex=_OaLdCardIndex_Object((1,3,6,1,4,1,6926,1,41,3,1,1,1),_OaLdCardIndex_Type())
oaLdCardIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdCardIndex.setStatus(_A)
class _OaLdCardType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180)));namedValues=NamedValues(*((_E,1),('empty',2),('em2009dm',3),('em2009dh',4),('dw16mux',5),('dw16dmux',6),('cw8mux',7),('cw8dmux',8),('ld1600red',9),('ld1600mgt',10),('em2009cm',11),('em2009ch',12),('ld800red',13),('ld800mgt',14),('dw8mux',15),('dw8dmux',16),('em2009em',17),('oadm1',18),('oadm2',19),('oadm3',20),('oadm4',21),('em2009oe2',22),('em800srv',23),('em1600srv',24),('tmsfpc',25),('tmsfpd',26),('adc800',27),('adcd800',28),('w8MuxDmux',29),('w16MuxDmux',30),('ld800redN',31),('ld1600redN',32),('adc1600',33),('adcd1600',34),('em2009gm2',35),('em800oa',36),('em1600oa',37),('tm2sfp',38),('em2009fm2',39),('em2009e8gm',40),('em2009t8gm',41),('tme8gm',42),('tmt8gm',43),('tmgm2',44),('tmfm2',45),('tmdxfp',46),('em2009e3gm',47),('em2009dsgm',48),('tme3gm',49),('tmdsgm',50),('em800rbbs4',51),('em800mgtd',52),('em800dcm',53),('em800dcmd',54),('em1600dcm',55),('em1600dcmd',56),('em800dsrv',57),('em800mp2',58),('em800roa',59),('em2009ftxm4',60),('em2009ftxm8',61),('em2009fxm4',62),('em2009fxm8',63),('tmftxm4',64),('tmftxm8',65),('tmfxm4',66),('tmfxm8',67),('em800oaid',68),('oadmxx',69),('em2009ocm4',70),('em2009ocm8',71),('tmocm4',72),('tmocm8',73),('em2009ftlm4',74),('em2009ftlm8',75),('em8MuxDmux',76),('em16MuxDmux',77),('em1600mgtd',78),('tmdxfpMsa',79),('tmdxfpMsaTunable',80),('em2009fetxm4',81),('em2009fetxm8',82),('tmfetxm4',83),('tmfetxm8',84),('em2009em4',85),('tmd4gsfp',86),('tm2d4gsfp',87),('em1600Roadm',88),('tmgm8d',89),('tmgm8cd',90),('tmgm8dTunable',91),('tmgm8cdTunable',92),('em1600Raman',93),('bsxx',94),('em1600dsrv',95),('em16004cc10g',96),('em16008cc10g',97),('em800rbbs2',98),('em1600rbbs2',99),('b4oadmxx',100),('em1600oab22p',101),('em1600oab22pm',102),('em800oab22p',103),('em800oab22pm',104),('tm1600dxfpfx',105),('tm1600dxfpfxt',106),('tm1600ocm48d',107),('tm1600ocm48dt',108),('tmfcm8d',109),('tmfcm8dt',110),('tmfc2m4d',111),('tmfc2m4dt',112),('em16Mux40',113),('em16Dmux40',114),('em1600rbbs4',115),('tm1600dxfpcx',116),('tm1600dxfpcxt',117),('em2009a4',118),('em1600oai21p',119),('em1600oai21pm',120),('em800oai21p',121),('em800oai21pm',122),('em2009eam2',123),('tm2sfppxfp',124),('em1600roadmw9',125),('tm2xfp',126),('opn1600c82',127),('add800',128),('addd800',129),('add1600',130),('addd1600',131),('em1600oaid',132),('em800oaDual',133),('em1600oaDual',134),('opn800s82',135),('opn1600s82',136),('tmgm8xfp',137),('tm2sfppxfpfc8',138),('tm2xfpf',139),('em1600mp2xx',140),('tm2xfpe',141),('em20094rs530',142),('em800dcmt',143),('em800dcmdt',144),('em1600dcmt',145),('em1600dcmdt',146),('tmdxfpfxt',147),('tmdxfpfxtDual',148),('em2009Voa4',149),('em2009Voa8',150),('tmgm8dft',151),('tmfc1m8xfp',152),('tmfc2m4xfp',153),('tmocm48xfp',154),('tmgm8df',155),('em20098xfp',156),('em20098xfp2',157),('tm8a',158),('em800ocm',159),('tm2sfpenge',160),('tm40gt',161),('em100mngp',162),('em160016axfp2',163),('tm2sfpengel2',164),('tm2sfpxc',165),('tm10gm4t',166),('em1600wss2q',167),('em1600wss4d',168),('em800mngt',169),('em16Mux80',170),('em16Dmux80',171),('em16Mux40h',172),('em16Dmux40h',173),('em800tdcm',174),('em1600Raman12',175),('tm2xsfpfm',176),('em800mp2e2',177),('em800cin502',178),('tm6cfpf',179),('em1600mngt',180)))
_OaLdCardType_Type.__name__=_D
_OaLdCardType_Object=MibTableColumn
oaLdCardType=_OaLdCardType_Object((1,3,6,1,4,1,6926,1,41,3,1,1,2),_OaLdCardType_Type())
oaLdCardType.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdCardType.setStatus(_A)
class _OaLdCardRev_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_E,1),('rev1',2),('rev2',3),('rev3',4),('rev4',5),('rev5',6),('rev6',7),('rev7',8)))
_OaLdCardRev_Type.__name__=_D
_OaLdCardRev_Object=MibTableColumn
oaLdCardRev=_OaLdCardRev_Object((1,3,6,1,4,1,6926,1,41,3,1,1,3),_OaLdCardRev_Type())
oaLdCardRev.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdCardRev.setStatus(_A)
_OaLdCardLambdaCh_Type=LambdaCh
_OaLdCardLambdaCh_Object=MibTableColumn
oaLdCardLambdaCh=_OaLdCardLambdaCh_Object((1,3,6,1,4,1,6926,1,41,3,1,1,4),_OaLdCardLambdaCh_Type())
oaLdCardLambdaCh.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdCardLambdaCh.setStatus(_A)
class _OaLdCardOptAccRx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_L,2),(_M,3)))
_OaLdCardOptAccRx_Type.__name__=_D
_OaLdCardOptAccRx_Object=MibTableColumn
oaLdCardOptAccRx=_OaLdCardOptAccRx_Object((1,3,6,1,4,1,6926,1,41,3,1,1,5),_OaLdCardOptAccRx_Type())
oaLdCardOptAccRx.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdCardOptAccRx.setStatus(_A)
class _OaLdCardOptDwdmRx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_L,2),(_M,3)))
_OaLdCardOptDwdmRx_Type.__name__=_D
_OaLdCardOptDwdmRx_Object=MibTableColumn
oaLdCardOptDwdmRx=_OaLdCardOptDwdmRx_Object((1,3,6,1,4,1,6926,1,41,3,1,1,6),_OaLdCardOptDwdmRx_Type())
oaLdCardOptDwdmRx.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdCardOptDwdmRx.setStatus(_A)
class _OaLdCardDwdmLaserTx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_a,2),(_Z,3)))
_OaLdCardDwdmLaserTx_Type.__name__=_D
_OaLdCardDwdmLaserTx_Object=MibTableColumn
oaLdCardDwdmLaserTx=_OaLdCardDwdmLaserTx_Object((1,3,6,1,4,1,6926,1,41,3,1,1,7),_OaLdCardDwdmLaserTx_Type())
oaLdCardDwdmLaserTx.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdCardDwdmLaserTx.setStatus(_A)
class _OaLdCardLaserTemp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_S,2),(_b,3)))
_OaLdCardLaserTemp_Type.__name__=_D
_OaLdCardLaserTemp_Object=MibTableColumn
oaLdCardLaserTemp=_OaLdCardLaserTemp_Object((1,3,6,1,4,1,6926,1,41,3,1,1,8),_OaLdCardLaserTemp_Type())
oaLdCardLaserTemp.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdCardLaserTemp.setStatus(_A)
class _OaLdCardAmbientTemp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_S,2),(_b,3)))
_OaLdCardAmbientTemp_Type.__name__=_D
_OaLdCardAmbientTemp_Object=MibTableColumn
oaLdCardAmbientTemp=_OaLdCardAmbientTemp_Object((1,3,6,1,4,1,6926,1,41,3,1,1,9),_OaLdCardAmbientTemp_Type())
oaLdCardAmbientTemp.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdCardAmbientTemp.setStatus(_A)
_OaLdCardRateSelect_Type=RateSelect
_OaLdCardRateSelect_Object=MibTableColumn
oaLdCardRateSelect=_OaLdCardRateSelect_Object((1,3,6,1,4,1,6926,1,41,3,1,1,10),_OaLdCardRateSelect_Type())
oaLdCardRateSelect.setMaxAccess(_F)
if mibBuilder.loadTexts:oaLdCardRateSelect.setStatus(_A)
class _OaLdCardRateMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),('auto',2),(_c,3)))
_OaLdCardRateMode_Type.__name__=_D
_OaLdCardRateMode_Object=MibTableColumn
oaLdCardRateMode=_OaLdCardRateMode_Object((1,3,6,1,4,1,6926,1,41,3,1,1,11),_OaLdCardRateMode_Type())
oaLdCardRateMode.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdCardRateMode.setStatus(_A)
class _OaLdCardLaserMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_N,2),(_K,3)))
_OaLdCardLaserMode_Type.__name__=_D
_OaLdCardLaserMode_Object=MibTableColumn
oaLdCardLaserMode=_OaLdCardLaserMode_Object((1,3,6,1,4,1,6926,1,41,3,1,1,12),_OaLdCardLaserMode_Type())
oaLdCardLaserMode.setMaxAccess(_F)
if mibBuilder.loadTexts:oaLdCardLaserMode.setStatus(_A)
_OaLdCardWdmRxPm_Type=Integer32
_OaLdCardWdmRxPm_Object=MibTableColumn
oaLdCardWdmRxPm=_OaLdCardWdmRxPm_Object((1,3,6,1,4,1,6926,1,41,3,1,1,15),_OaLdCardWdmRxPm_Type())
oaLdCardWdmRxPm.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdCardWdmRxPm.setStatus(_A)
_OaLdCardWdmTxPm_Type=Integer32
_OaLdCardWdmTxPm_Object=MibTableColumn
oaLdCardWdmTxPm=_OaLdCardWdmTxPm_Object((1,3,6,1,4,1,6926,1,41,3,1,1,16),_OaLdCardWdmTxPm_Type())
oaLdCardWdmTxPm.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdCardWdmTxPm.setStatus(_A)
class _OaLdCardLoopBack_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_E,1),(_S,2),(_k,3),(_l,4),(_m,5)))
_OaLdCardLoopBack_Type.__name__=_D
_OaLdCardLoopBack_Object=MibTableColumn
oaLdCardLoopBack=_OaLdCardLoopBack_Object((1,3,6,1,4,1,6926,1,41,3,1,1,17),_OaLdCardLoopBack_Type())
oaLdCardLoopBack.setMaxAccess(_F)
if mibBuilder.loadTexts:oaLdCardLoopBack.setStatus(_A)
class _OaLdCardRedundantState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_S,2),(_A5,3)))
_OaLdCardRedundantState_Type.__name__=_D
_OaLdCardRedundantState_Object=MibTableColumn
oaLdCardRedundantState=_OaLdCardRedundantState_Object((1,3,6,1,4,1,6926,1,41,3,1,1,18),_OaLdCardRedundantState_Type())
oaLdCardRedundantState.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdCardRedundantState.setStatus(_A)
class _OaLdCardPrimaryState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_n,2),(_o,3)))
_OaLdCardPrimaryState_Type.__name__=_D
_OaLdCardPrimaryState_Object=MibTableColumn
oaLdCardPrimaryState=_OaLdCardPrimaryState_Object((1,3,6,1,4,1,6926,1,41,3,1,1,19),_OaLdCardPrimaryState_Type())
oaLdCardPrimaryState.setMaxAccess(_F)
if mibBuilder.loadTexts:oaLdCardPrimaryState.setStatus(_A)
_OaLdCardFPGARev_Type=Integer32
_OaLdCardFPGARev_Object=MibTableColumn
oaLdCardFPGARev=_OaLdCardFPGARev_Object((1,3,6,1,4,1,6926,1,41,3,1,1,20),_OaLdCardFPGARev_Type())
oaLdCardFPGARev.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdCardFPGARev.setStatus(_A)
class _OaLdCardPartNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_OaLdCardPartNumber_Type.__name__=_J
_OaLdCardPartNumber_Object=MibTableColumn
oaLdCardPartNumber=_OaLdCardPartNumber_Object((1,3,6,1,4,1,6926,1,41,3,1,1,21),_OaLdCardPartNumber_Type())
oaLdCardPartNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdCardPartNumber.setStatus(_A)
class _OaLdCardSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(10,10));fixedLength=10
_OaLdCardSerialNumber_Type.__name__=_J
_OaLdCardSerialNumber_Object=MibTableColumn
oaLdCardSerialNumber=_OaLdCardSerialNumber_Object((1,3,6,1,4,1,6926,1,41,3,1,1,22),_OaLdCardSerialNumber_Type())
oaLdCardSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdCardSerialNumber.setStatus(_A)
_OaLdCardHwRev_Type=Integer32
_OaLdCardHwRev_Object=MibTableColumn
oaLdCardHwRev=_OaLdCardHwRev_Object((1,3,6,1,4,1,6926,1,41,3,1,1,23),_OaLdCardHwRev_Type())
oaLdCardHwRev.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdCardHwRev.setStatus(_A)
class _OaLdCardOptAccTx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_L,2),(_M,3)))
_OaLdCardOptAccTx_Type.__name__=_D
_OaLdCardOptAccTx_Object=MibTableColumn
oaLdCardOptAccTx=_OaLdCardOptAccTx_Object((1,3,6,1,4,1,6926,1,41,3,1,1,24),_OaLdCardOptAccTx_Type())
oaLdCardOptAccTx.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdCardOptAccTx.setStatus(_A)
class _OaLdCardOptDwdmTx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_L,2),(_M,3)))
_OaLdCardOptDwdmTx_Type.__name__=_D
_OaLdCardOptDwdmTx_Object=MibTableColumn
oaLdCardOptDwdmTx=_OaLdCardOptDwdmTx_Object((1,3,6,1,4,1,6926,1,41,3,1,1,25),_OaLdCardOptDwdmTx_Type())
oaLdCardOptDwdmTx.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdCardOptDwdmTx.setStatus(_A)
_OaLdCardTemp_Type=Integer32
_OaLdCardTemp_Object=MibTableColumn
oaLdCardTemp=_OaLdCardTemp_Object((1,3,6,1,4,1,6926,1,41,3,1,1,26),_OaLdCardTemp_Type())
oaLdCardTemp.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdCardTemp.setStatus(_A)
class _OaLdCardSubType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),('regular',2),('enchanced',3)))
_OaLdCardSubType_Type.__name__=_D
_OaLdCardSubType_Object=MibTableColumn
oaLdCardSubType=_OaLdCardSubType_Object((1,3,6,1,4,1,6926,1,41,3,1,1,27),_OaLdCardSubType_Type())
oaLdCardSubType.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdCardSubType.setStatus(_A)
_OaLdSlotEntitysStat_ObjectIdentity=ObjectIdentity
oaLdSlotEntitysStat=_OaLdSlotEntitysStat_ObjectIdentity((1,3,6,1,4,1,6926,1,41,4))
_OaLdCardEntityStatTable_Object=MibTable
oaLdCardEntityStatTable=_OaLdCardEntityStatTable_Object((1,3,6,1,4,1,6926,1,41,4,1))
if mibBuilder.loadTexts:oaLdCardEntityStatTable.setStatus(_A)
_OaLdCardEntityStatEntry_Object=MibTableRow
oaLdCardEntityStatEntry=_OaLdCardEntityStatEntry_Object((1,3,6,1,4,1,6926,1,41,4,1,1))
oaLdCardEntityStatEntry.setIndexNames((0,_C,_Q),(0,_C,_R))
if mibBuilder.loadTexts:oaLdCardEntityStatEntry.setStatus(_A)
_OaLdCardEntityCardIndex_Type=Integer32
_OaLdCardEntityCardIndex_Object=MibTableColumn
oaLdCardEntityCardIndex=_OaLdCardEntityCardIndex_Object((1,3,6,1,4,1,6926,1,41,4,1,1,1),_OaLdCardEntityCardIndex_Type())
oaLdCardEntityCardIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdCardEntityCardIndex.setStatus(_A)
_OaLdCardEntityEntityIndex_Type=Integer32
_OaLdCardEntityEntityIndex_Object=MibTableColumn
oaLdCardEntityEntityIndex=_OaLdCardEntityEntityIndex_Object((1,3,6,1,4,1,6926,1,41,4,1,1,2),_OaLdCardEntityEntityIndex_Type())
oaLdCardEntityEntityIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdCardEntityEntityIndex.setStatus(_A)
_OaLdCardEntityWaveLength_Type=Integer32
_OaLdCardEntityWaveLength_Object=MibTableColumn
oaLdCardEntityWaveLength=_OaLdCardEntityWaveLength_Object((1,3,6,1,4,1,6926,1,41,4,1,1,5),_OaLdCardEntityWaveLength_Type())
oaLdCardEntityWaveLength.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdCardEntityWaveLength.setStatus(_A)
class _OaLdCardEntityOptAccRx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_L,2),(_M,3)))
_OaLdCardEntityOptAccRx_Type.__name__=_D
_OaLdCardEntityOptAccRx_Object=MibTableColumn
oaLdCardEntityOptAccRx=_OaLdCardEntityOptAccRx_Object((1,3,6,1,4,1,6926,1,41,4,1,1,6),_OaLdCardEntityOptAccRx_Type())
oaLdCardEntityOptAccRx.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdCardEntityOptAccRx.setStatus(_A)
class _OaLdCardEntityOptDwdmRx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_L,2),(_M,3)))
_OaLdCardEntityOptDwdmRx_Type.__name__=_D
_OaLdCardEntityOptDwdmRx_Object=MibTableColumn
oaLdCardEntityOptDwdmRx=_OaLdCardEntityOptDwdmRx_Object((1,3,6,1,4,1,6926,1,41,4,1,1,7),_OaLdCardEntityOptDwdmRx_Type())
oaLdCardEntityOptDwdmRx.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdCardEntityOptDwdmRx.setStatus(_A)
class _OaLdCardEntityDwdmLaserTx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_a,2),(_Z,3)))
_OaLdCardEntityDwdmLaserTx_Type.__name__=_D
_OaLdCardEntityDwdmLaserTx_Object=MibTableColumn
oaLdCardEntityDwdmLaserTx=_OaLdCardEntityDwdmLaserTx_Object((1,3,6,1,4,1,6926,1,41,4,1,1,8),_OaLdCardEntityDwdmLaserTx_Type())
oaLdCardEntityDwdmLaserTx.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdCardEntityDwdmLaserTx.setStatus(_A)
class _OaLdCardEntityLaserTemp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_S,2),(_b,3)))
_OaLdCardEntityLaserTemp_Type.__name__=_D
_OaLdCardEntityLaserTemp_Object=MibTableColumn
oaLdCardEntityLaserTemp=_OaLdCardEntityLaserTemp_Object((1,3,6,1,4,1,6926,1,41,4,1,1,9),_OaLdCardEntityLaserTemp_Type())
oaLdCardEntityLaserTemp.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdCardEntityLaserTemp.setStatus(_A)
class _OaLdCardEntityAmbientTemp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_S,2),(_b,3)))
_OaLdCardEntityAmbientTemp_Type.__name__=_D
_OaLdCardEntityAmbientTemp_Object=MibTableColumn
oaLdCardEntityAmbientTemp=_OaLdCardEntityAmbientTemp_Object((1,3,6,1,4,1,6926,1,41,4,1,1,10),_OaLdCardEntityAmbientTemp_Type())
oaLdCardEntityAmbientTemp.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdCardEntityAmbientTemp.setStatus(_A)
_OaLdCardEntityRateSelect_Type=RateSelect
_OaLdCardEntityRateSelect_Object=MibTableColumn
oaLdCardEntityRateSelect=_OaLdCardEntityRateSelect_Object((1,3,6,1,4,1,6926,1,41,4,1,1,11),_OaLdCardEntityRateSelect_Type())
oaLdCardEntityRateSelect.setMaxAccess(_F)
if mibBuilder.loadTexts:oaLdCardEntityRateSelect.setStatus(_A)
class _OaLdCardEntityRateMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),('auto',2),(_c,3)))
_OaLdCardEntityRateMode_Type.__name__=_D
_OaLdCardEntityRateMode_Object=MibTableColumn
oaLdCardEntityRateMode=_OaLdCardEntityRateMode_Object((1,3,6,1,4,1,6926,1,41,4,1,1,12),_OaLdCardEntityRateMode_Type())
oaLdCardEntityRateMode.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdCardEntityRateMode.setStatus(_A)
class _OaLdCardEntityLaserMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_N,2),(_K,3)))
_OaLdCardEntityLaserMode_Type.__name__=_D
_OaLdCardEntityLaserMode_Object=MibTableColumn
oaLdCardEntityLaserMode=_OaLdCardEntityLaserMode_Object((1,3,6,1,4,1,6926,1,41,4,1,1,13),_OaLdCardEntityLaserMode_Type())
oaLdCardEntityLaserMode.setMaxAccess(_F)
if mibBuilder.loadTexts:oaLdCardEntityLaserMode.setStatus(_A)
_OaLdCardEntityWdmRxPm_Type=Integer32
_OaLdCardEntityWdmRxPm_Object=MibTableColumn
oaLdCardEntityWdmRxPm=_OaLdCardEntityWdmRxPm_Object((1,3,6,1,4,1,6926,1,41,4,1,1,16),_OaLdCardEntityWdmRxPm_Type())
oaLdCardEntityWdmRxPm.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdCardEntityWdmRxPm.setStatus(_A)
_OaLdCardEntityWdmTxPm_Type=Integer32
_OaLdCardEntityWdmTxPm_Object=MibTableColumn
oaLdCardEntityWdmTxPm=_OaLdCardEntityWdmTxPm_Object((1,3,6,1,4,1,6926,1,41,4,1,1,17),_OaLdCardEntityWdmTxPm_Type())
oaLdCardEntityWdmTxPm.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdCardEntityWdmTxPm.setStatus(_A)
class _OaLdCardEntityLoopBack_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_E,1),(_S,2),(_k,3),(_l,4),(_m,5)))
_OaLdCardEntityLoopBack_Type.__name__=_D
_OaLdCardEntityLoopBack_Object=MibTableColumn
oaLdCardEntityLoopBack=_OaLdCardEntityLoopBack_Object((1,3,6,1,4,1,6926,1,41,4,1,1,18),_OaLdCardEntityLoopBack_Type())
oaLdCardEntityLoopBack.setMaxAccess(_F)
if mibBuilder.loadTexts:oaLdCardEntityLoopBack.setStatus(_A)
class _OaLdCardEntityRedundantState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_S,2),(_A5,3)))
_OaLdCardEntityRedundantState_Type.__name__=_D
_OaLdCardEntityRedundantState_Object=MibTableColumn
oaLdCardEntityRedundantState=_OaLdCardEntityRedundantState_Object((1,3,6,1,4,1,6926,1,41,4,1,1,19),_OaLdCardEntityRedundantState_Type())
oaLdCardEntityRedundantState.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdCardEntityRedundantState.setStatus(_A)
class _OaLdCardEntityPrimaryState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_n,2),(_o,3)))
_OaLdCardEntityPrimaryState_Type.__name__=_D
_OaLdCardEntityPrimaryState_Object=MibTableColumn
oaLdCardEntityPrimaryState=_OaLdCardEntityPrimaryState_Object((1,3,6,1,4,1,6926,1,41,4,1,1,20),_OaLdCardEntityPrimaryState_Type())
oaLdCardEntityPrimaryState.setMaxAccess(_F)
if mibBuilder.loadTexts:oaLdCardEntityPrimaryState.setStatus(_A)
class _OaLdCardEntityClockSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_E,1),('p1',2),('p2',3),('p3',4),('p4',5),('p5',6),('p6',7),('p7',8),('p8',9),('p9',10)))
_OaLdCardEntityClockSource_Type.__name__=_D
_OaLdCardEntityClockSource_Object=MibTableColumn
oaLdCardEntityClockSource=_OaLdCardEntityClockSource_Object((1,3,6,1,4,1,6926,1,41,4,1,1,21),_OaLdCardEntityClockSource_Type())
oaLdCardEntityClockSource.setMaxAccess(_F)
if mibBuilder.loadTexts:oaLdCardEntityClockSource.setStatus(_A)
class _OaLdCardEntityTransparency_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),('transparent',2),('noTransparent',3)))
_OaLdCardEntityTransparency_Type.__name__=_D
_OaLdCardEntityTransparency_Object=MibTableColumn
oaLdCardEntityTransparency=_OaLdCardEntityTransparency_Object((1,3,6,1,4,1,6926,1,41,4,1,1,22),_OaLdCardEntityTransparency_Type())
oaLdCardEntityTransparency.setMaxAccess(_F)
if mibBuilder.loadTexts:oaLdCardEntityTransparency.setStatus(_A)
class _OaLdCardEntityStandard_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),('sonet',2),('sdh',3)))
_OaLdCardEntityStandard_Type.__name__=_D
_OaLdCardEntityStandard_Object=MibTableColumn
oaLdCardEntityStandard=_OaLdCardEntityStandard_Object((1,3,6,1,4,1,6926,1,41,4,1,1,23),_OaLdCardEntityStandard_Type())
oaLdCardEntityStandard.setMaxAccess(_F)
if mibBuilder.loadTexts:oaLdCardEntityStandard.setStatus(_A)
class _OaLdCardEntityAccessLinState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_N,2),(_K,3)))
_OaLdCardEntityAccessLinState_Type.__name__=_D
_OaLdCardEntityAccessLinState_Object=MibTableColumn
oaLdCardEntityAccessLinState=_OaLdCardEntityAccessLinState_Object((1,3,6,1,4,1,6926,1,41,4,1,1,24),_OaLdCardEntityAccessLinState_Type())
oaLdCardEntityAccessLinState.setMaxAccess(_F)
if mibBuilder.loadTexts:oaLdCardEntityAccessLinState.setStatus(_A)
class _OaLdCardEntityLineCoding_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),('b8zs',2),('ami',3)))
_OaLdCardEntityLineCoding_Type.__name__=_D
_OaLdCardEntityLineCoding_Object=MibTableColumn
oaLdCardEntityLineCoding=_OaLdCardEntityLineCoding_Object((1,3,6,1,4,1,6926,1,41,4,1,1,25),_OaLdCardEntityLineCoding_Type())
oaLdCardEntityLineCoding.setMaxAccess(_F)
if mibBuilder.loadTexts:oaLdCardEntityLineCoding.setStatus(_A)
class _OaLdCardEntityUartBaudRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_E,1),('baud1200',2),('baud2400',3),('baud4800',4),('baud9600',5),('baud19200',6),('baud38400',7),('baud57600',8),('baud115200',9)))
_OaLdCardEntityUartBaudRate_Type.__name__=_D
_OaLdCardEntityUartBaudRate_Object=MibTableColumn
oaLdCardEntityUartBaudRate=_OaLdCardEntityUartBaudRate_Object((1,3,6,1,4,1,6926,1,41,4,1,1,26),_OaLdCardEntityUartBaudRate_Type())
oaLdCardEntityUartBaudRate.setMaxAccess(_F)
if mibBuilder.loadTexts:oaLdCardEntityUartBaudRate.setStatus(_A)
class _OaLdCardEntityUartParity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),('even',2),('odd',3),('noParity',4)))
_OaLdCardEntityUartParity_Type.__name__=_D
_OaLdCardEntityUartParity_Object=MibTableColumn
oaLdCardEntityUartParity=_OaLdCardEntityUartParity_Object((1,3,6,1,4,1,6926,1,41,4,1,1,27),_OaLdCardEntityUartParity_Type())
oaLdCardEntityUartParity.setMaxAccess(_F)
if mibBuilder.loadTexts:oaLdCardEntityUartParity.setStatus(_A)
class _OaLdCardEntityUartStopBit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),('stopBit1',2),('stopBit15',3)))
_OaLdCardEntityUartStopBit_Type.__name__=_D
_OaLdCardEntityUartStopBit_Object=MibTableColumn
oaLdCardEntityUartStopBit=_OaLdCardEntityUartStopBit_Object((1,3,6,1,4,1,6926,1,41,4,1,1,28),_OaLdCardEntityUartStopBit_Type())
oaLdCardEntityUartStopBit.setMaxAccess(_F)
if mibBuilder.loadTexts:oaLdCardEntityUartStopBit.setStatus(_A)
class _OaLdCardEntityPmMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_N,2),(_K,3)))
_OaLdCardEntityPmMode_Type.__name__=_D
_OaLdCardEntityPmMode_Object=MibTableColumn
oaLdCardEntityPmMode=_OaLdCardEntityPmMode_Object((1,3,6,1,4,1,6926,1,41,4,1,1,29),_OaLdCardEntityPmMode_Type())
oaLdCardEntityPmMode.setMaxAccess(_F)
if mibBuilder.loadTexts:oaLdCardEntityPmMode.setStatus(_A)
class _OaLdCardEntityWdmFecMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_E,1),('g709',2),('eFec',3),('byPass',4),('uFec',5)))
_OaLdCardEntityWdmFecMode_Type.__name__=_D
_OaLdCardEntityWdmFecMode_Object=MibTableColumn
oaLdCardEntityWdmFecMode=_OaLdCardEntityWdmFecMode_Object((1,3,6,1,4,1,6926,1,41,4,1,1,30),_OaLdCardEntityWdmFecMode_Type())
oaLdCardEntityWdmFecMode.setMaxAccess(_F)
if mibBuilder.loadTexts:oaLdCardEntityWdmFecMode.setStatus(_A)
_OaLdCardEntityMinDispDist_Type=Integer32
_OaLdCardEntityMinDispDist_Object=MibTableColumn
oaLdCardEntityMinDispDist=_OaLdCardEntityMinDispDist_Object((1,3,6,1,4,1,6926,1,41,4,1,1,31),_OaLdCardEntityMinDispDist_Type())
oaLdCardEntityMinDispDist.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdCardEntityMinDispDist.setStatus(_A)
if mibBuilder.loadTexts:oaLdCardEntityMinDispDist.setUnits(_d)
_OaLdCardEntityMaxDispDist_Type=Integer32
_OaLdCardEntityMaxDispDist_Object=MibTableColumn
oaLdCardEntityMaxDispDist=_OaLdCardEntityMaxDispDist_Object((1,3,6,1,4,1,6926,1,41,4,1,1,32),_OaLdCardEntityMaxDispDist_Type())
oaLdCardEntityMaxDispDist.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdCardEntityMaxDispDist.setStatus(_A)
if mibBuilder.loadTexts:oaLdCardEntityMaxDispDist.setUnits(_d)
_OaLdCardEntityDispDist_Type=Integer32
_OaLdCardEntityDispDist_Object=MibTableColumn
oaLdCardEntityDispDist=_OaLdCardEntityDispDist_Object((1,3,6,1,4,1,6926,1,41,4,1,1,33),_OaLdCardEntityDispDist_Type())
oaLdCardEntityDispDist.setMaxAccess(_F)
if mibBuilder.loadTexts:oaLdCardEntityDispDist.setStatus(_A)
if mibBuilder.loadTexts:oaLdCardEntityDispDist.setUnits(_d)
class _OaLdCardEntityCCMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_E,1),('dual1234',2),('dual1324',3),('dual1423',4),('protectRxMon',5),('protectTxMon',6),('multicast2',7),('multicast3',8),('multicast4',9),(_k,10)))
_OaLdCardEntityCCMode_Type.__name__=_D
_OaLdCardEntityCCMode_Object=MibTableColumn
oaLdCardEntityCCMode=_OaLdCardEntityCCMode_Object((1,3,6,1,4,1,6926,1,41,4,1,1,34),_OaLdCardEntityCCMode_Type())
oaLdCardEntityCCMode.setMaxAccess(_F)
if mibBuilder.loadTexts:oaLdCardEntityCCMode.setStatus(_A)
class _OaLdCardEntityOptAccTx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_L,2),(_M,3)))
_OaLdCardEntityOptAccTx_Type.__name__=_D
_OaLdCardEntityOptAccTx_Object=MibTableColumn
oaLdCardEntityOptAccTx=_OaLdCardEntityOptAccTx_Object((1,3,6,1,4,1,6926,1,41,4,1,1,35),_OaLdCardEntityOptAccTx_Type())
oaLdCardEntityOptAccTx.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdCardEntityOptAccTx.setStatus(_A)
class _OaLdCardEntityOptDwdmTx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_L,2),(_M,3)))
_OaLdCardEntityOptDwdmTx_Type.__name__=_D
_OaLdCardEntityOptDwdmTx_Object=MibTableColumn
oaLdCardEntityOptDwdmTx=_OaLdCardEntityOptDwdmTx_Object((1,3,6,1,4,1,6926,1,41,4,1,1,36),_OaLdCardEntityOptDwdmTx_Type())
oaLdCardEntityOptDwdmTx.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdCardEntityOptDwdmTx.setStatus(_A)
class _OaLdCardEntityEMCfgType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_E,1),('typeI',2),('typeII',3),('typeIII',4),('typeIV',5),('typeV',6)))
_OaLdCardEntityEMCfgType_Type.__name__=_D
_OaLdCardEntityEMCfgType_Object=MibTableColumn
oaLdCardEntityEMCfgType=_OaLdCardEntityEMCfgType_Object((1,3,6,1,4,1,6926,1,41,4,1,1,37),_OaLdCardEntityEMCfgType_Type())
oaLdCardEntityEMCfgType.setMaxAccess(_F)
if mibBuilder.loadTexts:oaLdCardEntityEMCfgType.setStatus(_A)
class _OaLdCardEntityEMCfgSide_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),('trunkCircuitSide',2),('signalingUnitSide',3)))
_OaLdCardEntityEMCfgSide_Type.__name__=_D
_OaLdCardEntityEMCfgSide_Object=MibTableColumn
oaLdCardEntityEMCfgSide=_OaLdCardEntityEMCfgSide_Object((1,3,6,1,4,1,6926,1,41,4,1,1,38),_OaLdCardEntityEMCfgSide_Type())
oaLdCardEntityEMCfgSide.setMaxAccess(_F)
if mibBuilder.loadTexts:oaLdCardEntityEMCfgSide.setStatus(_A)
class _OaLdCardEntityPreemptionMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),('port2',2),('port3',3),('noPreemption',4)))
_OaLdCardEntityPreemptionMode_Type.__name__=_D
_OaLdCardEntityPreemptionMode_Object=MibTableColumn
oaLdCardEntityPreemptionMode=_OaLdCardEntityPreemptionMode_Object((1,3,6,1,4,1,6926,1,41,4,1,1,39),_OaLdCardEntityPreemptionMode_Type())
oaLdCardEntityPreemptionMode.setMaxAccess(_F)
if mibBuilder.loadTexts:oaLdCardEntityPreemptionMode.setStatus(_A)
class _OaLdCardEntityActivePort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),('port2',2),('port3',3),('noActive',4)))
_OaLdCardEntityActivePort_Type.__name__=_D
_OaLdCardEntityActivePort_Object=MibTableColumn
oaLdCardEntityActivePort=_OaLdCardEntityActivePort_Object((1,3,6,1,4,1,6926,1,41,4,1,1,40),_OaLdCardEntityActivePort_Type())
oaLdCardEntityActivePort.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdCardEntityActivePort.setStatus(_A)
class _OaLdCardEntityOperationMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_E,1),(_S,2),('yCableRedundant',3),('repeater',4),('repeaterWan',5),('dualTransponder',6),('broadcastUni',7),('crossTransponder',8),('mux2WDM1Access',9)))
_OaLdCardEntityOperationMode_Type.__name__=_D
_OaLdCardEntityOperationMode_Object=MibTableColumn
oaLdCardEntityOperationMode=_OaLdCardEntityOperationMode_Object((1,3,6,1,4,1,6926,1,41,4,1,1,41),_OaLdCardEntityOperationMode_Type())
oaLdCardEntityOperationMode.setMaxAccess(_F)
if mibBuilder.loadTexts:oaLdCardEntityOperationMode.setStatus(_A)
class _OaLdCardEntityRedundantType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_E,1),(_S,2),('dualSlotRedundancy',3),('singleSlotRedundancy',4),('singleSlotOneAccessRedundancy',5)))
_OaLdCardEntityRedundantType_Type.__name__=_D
_OaLdCardEntityRedundantType_Object=MibTableColumn
oaLdCardEntityRedundantType=_OaLdCardEntityRedundantType_Object((1,3,6,1,4,1,6926,1,41,4,1,1,42),_OaLdCardEntityRedundantType_Type())
oaLdCardEntityRedundantType.setMaxAccess(_F)
if mibBuilder.loadTexts:oaLdCardEntityRedundantType.setStatus(_A)
class _OaLdCardEntityOtu2MappingMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_W,1),('basicMode',2),('extendedMode1',3),('extendedMode2',4)))
_OaLdCardEntityOtu2MappingMode_Type.__name__=_D
_OaLdCardEntityOtu2MappingMode_Object=MibTableColumn
oaLdCardEntityOtu2MappingMode=_OaLdCardEntityOtu2MappingMode_Object((1,3,6,1,4,1,6926,1,41,4,1,1,43),_OaLdCardEntityOtu2MappingMode_Type())
oaLdCardEntityOtu2MappingMode.setMaxAccess(_F)
if mibBuilder.loadTexts:oaLdCardEntityOtu2MappingMode.setStatus(_A)
class _OaLdCardEntityTopologyMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_W,1),('pointToPoint',2),('linearADM',3),('ringUniDirection',4),('ringBiDirection',5)))
_OaLdCardEntityTopologyMode_Type.__name__=_D
_OaLdCardEntityTopologyMode_Object=MibTableColumn
oaLdCardEntityTopologyMode=_OaLdCardEntityTopologyMode_Object((1,3,6,1,4,1,6926,1,41,4,1,1,44),_OaLdCardEntityTopologyMode_Type())
oaLdCardEntityTopologyMode.setMaxAccess(_F)
if mibBuilder.loadTexts:oaLdCardEntityTopologyMode.setStatus(_A)
_OaLdCardEntityDispDistAdmin_Type=Integer32
_OaLdCardEntityDispDistAdmin_Object=MibTableColumn
oaLdCardEntityDispDistAdmin=_OaLdCardEntityDispDistAdmin_Object((1,3,6,1,4,1,6926,1,41,4,1,1,45),_OaLdCardEntityDispDistAdmin_Type())
oaLdCardEntityDispDistAdmin.setMaxAccess(_F)
if mibBuilder.loadTexts:oaLdCardEntityDispDistAdmin.setStatus(_A)
if mibBuilder.loadTexts:oaLdCardEntityDispDistAdmin.setUnits(_d)
_OaLdCardEntityChannelOffset_Type=Integer32
_OaLdCardEntityChannelOffset_Object=MibTableColumn
oaLdCardEntityChannelOffset=_OaLdCardEntityChannelOffset_Object((1,3,6,1,4,1,6926,1,41,4,1,1,46),_OaLdCardEntityChannelOffset_Type())
oaLdCardEntityChannelOffset.setMaxAccess(_F)
if mibBuilder.loadTexts:oaLdCardEntityChannelOffset.setStatus(_A)
if mibBuilder.loadTexts:oaLdCardEntityChannelOffset.setUnits('GHz')
class _OaLdCardEntityTimingMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_W,1),('phaseMode',2),('fifoMode',3)))
_OaLdCardEntityTimingMode_Type.__name__=_D
_OaLdCardEntityTimingMode_Object=MibTableColumn
oaLdCardEntityTimingMode=_OaLdCardEntityTimingMode_Object((1,3,6,1,4,1,6926,1,41,4,1,1,47),_OaLdCardEntityTimingMode_Type())
oaLdCardEntityTimingMode.setMaxAccess(_F)
if mibBuilder.loadTexts:oaLdCardEntityTimingMode.setStatus(_A)
class _OaLdCardEntityTdcmTuningStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_A6,2),(_a,3)))
_OaLdCardEntityTdcmTuningStatus_Type.__name__=_D
_OaLdCardEntityTdcmTuningStatus_Object=MibTableColumn
oaLdCardEntityTdcmTuningStatus=_OaLdCardEntityTdcmTuningStatus_Object((1,3,6,1,4,1,6926,1,41,4,1,1,48),_OaLdCardEntityTdcmTuningStatus_Type())
oaLdCardEntityTdcmTuningStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdCardEntityTdcmTuningStatus.setStatus(_A)
_OaLdCardEntityRedModeActivePort_Type=Integer32
_OaLdCardEntityRedModeActivePort_Object=MibTableColumn
oaLdCardEntityRedModeActivePort=_OaLdCardEntityRedModeActivePort_Object((1,3,6,1,4,1,6926,1,41,4,1,1,49),_OaLdCardEntityRedModeActivePort_Type())
oaLdCardEntityRedModeActivePort.setMaxAccess(_F)
if mibBuilder.loadTexts:oaLdCardEntityRedModeActivePort.setStatus(_A)
class _OaLdCardEntityAutoShutdownMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_N,2),(_K,3)))
_OaLdCardEntityAutoShutdownMode_Type.__name__=_D
_OaLdCardEntityAutoShutdownMode_Object=MibTableColumn
oaLdCardEntityAutoShutdownMode=_OaLdCardEntityAutoShutdownMode_Object((1,3,6,1,4,1,6926,1,41,4,1,1,50),_OaLdCardEntityAutoShutdownMode_Type())
oaLdCardEntityAutoShutdownMode.setMaxAccess(_F)
if mibBuilder.loadTexts:oaLdCardEntityAutoShutdownMode.setStatus(_A)
_OaLdRedundantOptic_ObjectIdentity=ObjectIdentity
oaLdRedundantOptic=_OaLdRedundantOptic_ObjectIdentity((1,3,6,1,4,1,6926,1,41,6))
_OaLdRedundantOpticTable_Object=MibTable
oaLdRedundantOpticTable=_OaLdRedundantOpticTable_Object((1,3,6,1,4,1,6926,1,41,6,1))
if mibBuilder.loadTexts:oaLdRedundantOpticTable.setStatus(_A)
_OaLdRedundantOpticEntry_Object=MibTableRow
oaLdRedundantOpticEntry=_OaLdRedundantOpticEntry_Object((1,3,6,1,4,1,6926,1,41,6,1,1))
oaLdRedundantOpticEntry.setIndexNames((0,_C,_U))
if mibBuilder.loadTexts:oaLdRedundantOpticEntry.setStatus(_A)
_OaLdRedOptSlotNumber_Type=Integer32
_OaLdRedOptSlotNumber_Object=MibTableColumn
oaLdRedOptSlotNumber=_OaLdRedOptSlotNumber_Object((1,3,6,1,4,1,6926,1,41,6,1,1,1),_OaLdRedOptSlotNumber_Type())
oaLdRedOptSlotNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdRedOptSlotNumber.setStatus(_A)
class _OaLdRedOptSwitchPosition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_o,2),(_n,3)))
_OaLdRedOptSwitchPosition_Type.__name__=_D
_OaLdRedOptSwitchPosition_Object=MibTableColumn
oaLdRedOptSwitchPosition=_OaLdRedOptSwitchPosition_Object((1,3,6,1,4,1,6926,1,41,6,1,1,2),_OaLdRedOptSwitchPosition_Type())
oaLdRedOptSwitchPosition.setMaxAccess(_F)
if mibBuilder.loadTexts:oaLdRedOptSwitchPosition.setStatus(_A)
class _OaLdRedOptLastCommand_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_A7,2),(_c,3)))
_OaLdRedOptLastCommand_Type.__name__=_D
_OaLdRedOptLastCommand_Object=MibTableColumn
oaLdRedOptLastCommand=_OaLdRedOptLastCommand_Object((1,3,6,1,4,1,6926,1,41,6,1,1,3),_OaLdRedOptLastCommand_Type())
oaLdRedOptLastCommand.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdRedOptLastCommand.setStatus(_A)
class _OaLdRedOptPrimaryRx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_L,2),(_M,3)))
_OaLdRedOptPrimaryRx_Type.__name__=_D
_OaLdRedOptPrimaryRx_Object=MibTableColumn
oaLdRedOptPrimaryRx=_OaLdRedOptPrimaryRx_Object((1,3,6,1,4,1,6926,1,41,6,1,1,4),_OaLdRedOptPrimaryRx_Type())
oaLdRedOptPrimaryRx.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdRedOptPrimaryRx.setStatus(_A)
class _OaLdRedOptSecondaryRx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_L,2),(_M,3)))
_OaLdRedOptSecondaryRx_Type.__name__=_D
_OaLdRedOptSecondaryRx_Object=MibTableColumn
oaLdRedOptSecondaryRx=_OaLdRedOptSecondaryRx_Object((1,3,6,1,4,1,6926,1,41,6,1,1,5),_OaLdRedOptSecondaryRx_Type())
oaLdRedOptSecondaryRx.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdRedOptSecondaryRx.setStatus(_A)
_OaLdCardPortsStat_ObjectIdentity=ObjectIdentity
oaLdCardPortsStat=_OaLdCardPortsStat_ObjectIdentity((1,3,6,1,4,1,6926,1,41,8))
_OaLdCardPortsStatTable_Object=MibTable
oaLdCardPortsStatTable=_OaLdCardPortsStatTable_Object((1,3,6,1,4,1,6926,1,41,8,1))
if mibBuilder.loadTexts:oaLdCardPortsStatTable.setStatus(_A)
_OaLdCardPortsStatEntry_Object=MibTableRow
oaLdCardPortsStatEntry=_OaLdCardPortsStatEntry_Object((1,3,6,1,4,1,6926,1,41,8,1,1))
oaLdCardPortsStatEntry.setIndexNames((0,_C,_G),(0,_C,_P))
if mibBuilder.loadTexts:oaLdCardPortsStatEntry.setStatus(_A)
_OaLdCardPortsSlotNumber_Type=Integer32
_OaLdCardPortsSlotNumber_Object=MibTableColumn
oaLdCardPortsSlotNumber=_OaLdCardPortsSlotNumber_Object((1,3,6,1,4,1,6926,1,41,8,1,1,1),_OaLdCardPortsSlotNumber_Type())
oaLdCardPortsSlotNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdCardPortsSlotNumber.setStatus(_A)
_OaLdCardPortsPortNumber_Type=Integer32
_OaLdCardPortsPortNumber_Object=MibTableColumn
oaLdCardPortsPortNumber=_OaLdCardPortsPortNumber_Object((1,3,6,1,4,1,6926,1,41,8,1,1,2),_OaLdCardPortsPortNumber_Type())
oaLdCardPortsPortNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdCardPortsPortNumber.setStatus(_A)
class _OaLdCardPortsLink_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_L,2),(_M,3)))
_OaLdCardPortsLink_Type.__name__=_D
_OaLdCardPortsLink_Object=MibTableColumn
oaLdCardPortsLink=_OaLdCardPortsLink_Object((1,3,6,1,4,1,6926,1,41,8,1,1,3),_OaLdCardPortsLink_Type())
oaLdCardPortsLink.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdCardPortsLink.setStatus(_A)
class _OaLdCardPortsActivity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_L,2),(_M,3)))
_OaLdCardPortsActivity_Type.__name__=_D
_OaLdCardPortsActivity_Object=MibTableColumn
oaLdCardPortsActivity=_OaLdCardPortsActivity_Object((1,3,6,1,4,1,6926,1,41,8,1,1,4),_OaLdCardPortsActivity_Type())
oaLdCardPortsActivity.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdCardPortsActivity.setStatus(_A)
_OaLdCardPortsWaveLength_Type=Integer32
_OaLdCardPortsWaveLength_Object=MibTableColumn
oaLdCardPortsWaveLength=_OaLdCardPortsWaveLength_Object((1,3,6,1,4,1,6926,1,41,8,1,1,6),_OaLdCardPortsWaveLength_Type())
oaLdCardPortsWaveLength.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdCardPortsWaveLength.setStatus(_A)
class _OaLdCardPortsLoopBack_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_E,1),(_S,2),(_l,3),(_m,4),('lineLoopbackEnable',5),('diagnosticLoopbackEnable',6)))
_OaLdCardPortsLoopBack_Type.__name__=_D
_OaLdCardPortsLoopBack_Object=MibTableColumn
oaLdCardPortsLoopBack=_OaLdCardPortsLoopBack_Object((1,3,6,1,4,1,6926,1,41,8,1,1,8),_OaLdCardPortsLoopBack_Type())
oaLdCardPortsLoopBack.setMaxAccess(_F)
if mibBuilder.loadTexts:oaLdCardPortsLoopBack.setStatus(_A)
class _OaLdCardPortsCounters_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_T,1),(_A8,2),('clearCounters',3),('extendedCounters',4)))
_OaLdCardPortsCounters_Type.__name__=_D
_OaLdCardPortsCounters_Object=MibTableColumn
oaLdCardPortsCounters=_OaLdCardPortsCounters_Object((1,3,6,1,4,1,6926,1,41,8,1,1,12),_OaLdCardPortsCounters_Type())
oaLdCardPortsCounters.setMaxAccess(_F)
if mibBuilder.loadTexts:oaLdCardPortsCounters.setStatus(_A)
_OaLdCardPortsCounter1Low_Type=Counter32
_OaLdCardPortsCounter1Low_Object=MibTableColumn
oaLdCardPortsCounter1Low=_OaLdCardPortsCounter1Low_Object((1,3,6,1,4,1,6926,1,41,8,1,1,14),_OaLdCardPortsCounter1Low_Type())
oaLdCardPortsCounter1Low.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdCardPortsCounter1Low.setStatus(_A)
_OaLdCardPortsCounter1High_Type=Counter32
_OaLdCardPortsCounter1High_Object=MibTableColumn
oaLdCardPortsCounter1High=_OaLdCardPortsCounter1High_Object((1,3,6,1,4,1,6926,1,41,8,1,1,15),_OaLdCardPortsCounter1High_Type())
oaLdCardPortsCounter1High.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdCardPortsCounter1High.setStatus(_A)
_OaLdCardPortsCounter2Low_Type=Counter32
_OaLdCardPortsCounter2Low_Object=MibTableColumn
oaLdCardPortsCounter2Low=_OaLdCardPortsCounter2Low_Object((1,3,6,1,4,1,6926,1,41,8,1,1,17),_OaLdCardPortsCounter2Low_Type())
oaLdCardPortsCounter2Low.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdCardPortsCounter2Low.setStatus(_A)
_OaLdCardPortsCounter2High_Type=Counter32
_OaLdCardPortsCounter2High_Object=MibTableColumn
oaLdCardPortsCounter2High=_OaLdCardPortsCounter2High_Object((1,3,6,1,4,1,6926,1,41,8,1,1,18),_OaLdCardPortsCounter2High_Type())
oaLdCardPortsCounter2High.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdCardPortsCounter2High.setStatus(_A)
class _OaLdCardPortsConnectorType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_E,1),('static',2),('gbic',3),('sfp',4),('xfp',5),('xfpe',6),('cfp',7)))
_OaLdCardPortsConnectorType_Type.__name__=_D
_OaLdCardPortsConnectorType_Object=MibTableColumn
oaLdCardPortsConnectorType=_OaLdCardPortsConnectorType_Object((1,3,6,1,4,1,6926,1,41,8,1,1,20),_OaLdCardPortsConnectorType_Type())
oaLdCardPortsConnectorType.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdCardPortsConnectorType.setStatus(_A)
class _OaLdCardPortsConnectorSubType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*((_E,1),('rj45',2),('sc',3),('lc',4),('mtrj',5),('vf',6),('mu',7),('miniCoax',8),('mdiCx',9),('bnc',10),('mpo',11)))
_OaLdCardPortsConnectorSubType_Type.__name__=_D
_OaLdCardPortsConnectorSubType_Object=MibTableColumn
oaLdCardPortsConnectorSubType=_OaLdCardPortsConnectorSubType_Object((1,3,6,1,4,1,6926,1,41,8,1,1,21),_OaLdCardPortsConnectorSubType_Type())
oaLdCardPortsConnectorSubType.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdCardPortsConnectorSubType.setStatus(_A)
_OaLdCardPortsRate_Type=RateMode
_OaLdCardPortsRate_Object=MibTableColumn
oaLdCardPortsRate=_OaLdCardPortsRate_Object((1,3,6,1,4,1,6926,1,41,8,1,1,22),_OaLdCardPortsRate_Type())
oaLdCardPortsRate.setMaxAccess(_F)
if mibBuilder.loadTexts:oaLdCardPortsRate.setStatus(_A)
class _OaLdCardPortsLineLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_E,1),('from0to133',2),('from133to266',3),('from266to399',4),('from399to533',5),('from533to655',6)))
_OaLdCardPortsLineLength_Type.__name__=_D
_OaLdCardPortsLineLength_Object=MibTableColumn
oaLdCardPortsLineLength=_OaLdCardPortsLineLength_Object((1,3,6,1,4,1,6926,1,41,8,1,1,23),_OaLdCardPortsLineLength_Type())
oaLdCardPortsLineLength.setMaxAccess(_F)
if mibBuilder.loadTexts:oaLdCardPortsLineLength.setStatus(_A)
class _OaLdCardPortsAccessLinState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_N,2),(_K,3)))
_OaLdCardPortsAccessLinState_Type.__name__=_D
_OaLdCardPortsAccessLinState_Object=MibTableColumn
oaLdCardPortsAccessLinState=_OaLdCardPortsAccessLinState_Object((1,3,6,1,4,1,6926,1,41,8,1,1,24),_OaLdCardPortsAccessLinState_Type())
oaLdCardPortsAccessLinState.setMaxAccess(_F)
if mibBuilder.loadTexts:oaLdCardPortsAccessLinState.setStatus(_A)
class _OaLdCardPortsFlowControlMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_N,2),(_K,3)))
_OaLdCardPortsFlowControlMode_Type.__name__=_D
_OaLdCardPortsFlowControlMode_Object=MibTableColumn
oaLdCardPortsFlowControlMode=_OaLdCardPortsFlowControlMode_Object((1,3,6,1,4,1,6926,1,41,8,1,1,25),_OaLdCardPortsFlowControlMode_Type())
oaLdCardPortsFlowControlMode.setMaxAccess(_F)
if mibBuilder.loadTexts:oaLdCardPortsFlowControlMode.setStatus(_A)
class _OaLdCardPortsDryContactStat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),('open',2),('close',3)))
_OaLdCardPortsDryContactStat_Type.__name__=_D
_OaLdCardPortsDryContactStat_Object=MibTableColumn
oaLdCardPortsDryContactStat=_OaLdCardPortsDryContactStat_Object((1,3,6,1,4,1,6926,1,41,8,1,1,26),_OaLdCardPortsDryContactStat_Type())
oaLdCardPortsDryContactStat.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdCardPortsDryContactStat.setStatus(_A)
class _OaLdCardPortsPowerTuning_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-10,10))
_OaLdCardPortsPowerTuning_Type.__name__=_D
_OaLdCardPortsPowerTuning_Object=MibTableColumn
oaLdCardPortsPowerTuning=_OaLdCardPortsPowerTuning_Object((1,3,6,1,4,1,6926,1,41,8,1,1,27),_OaLdCardPortsPowerTuning_Type())
oaLdCardPortsPowerTuning.setMaxAccess(_F)
if mibBuilder.loadTexts:oaLdCardPortsPowerTuning.setStatus(_A)
class _OaLdCardPortsMediaType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),('copper',2),('fiber',3)))
_OaLdCardPortsMediaType_Type.__name__=_D
_OaLdCardPortsMediaType_Object=MibTableColumn
oaLdCardPortsMediaType=_OaLdCardPortsMediaType_Object((1,3,6,1,4,1,6926,1,41,8,1,1,28),_OaLdCardPortsMediaType_Type())
oaLdCardPortsMediaType.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdCardPortsMediaType.setStatus(_A)
class _OaLdCardPortsEMCfgOperation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),('twoWires',2),('fourWires',3)))
_OaLdCardPortsEMCfgOperation_Type.__name__=_D
_OaLdCardPortsEMCfgOperation_Object=MibTableColumn
oaLdCardPortsEMCfgOperation=_OaLdCardPortsEMCfgOperation_Object((1,3,6,1,4,1,6926,1,41,8,1,1,29),_OaLdCardPortsEMCfgOperation_Type())
oaLdCardPortsEMCfgOperation.setMaxAccess(_F)
if mibBuilder.loadTexts:oaLdCardPortsEMCfgOperation.setStatus(_A)
class _OaLdCardPortsEyemaxState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_E,1),(_K,2),(_N,3),('scanning',4),('tracking',5),('calibrating',6),('stopTracking',7)))
_OaLdCardPortsEyemaxState_Type.__name__=_D
_OaLdCardPortsEyemaxState_Object=MibTableColumn
oaLdCardPortsEyemaxState=_OaLdCardPortsEyemaxState_Object((1,3,6,1,4,1,6926,1,41,8,1,1,30),_OaLdCardPortsEyemaxState_Type())
oaLdCardPortsEyemaxState.setMaxAccess(_F)
if mibBuilder.loadTexts:oaLdCardPortsEyemaxState.setStatus(_A)
class _OaLdCardPortsEyemaxOperFactor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_OaLdCardPortsEyemaxOperFactor_Type.__name__=_D
_OaLdCardPortsEyemaxOperFactor_Object=MibTableColumn
oaLdCardPortsEyemaxOperFactor=_OaLdCardPortsEyemaxOperFactor_Object((1,3,6,1,4,1,6926,1,41,8,1,1,31),_OaLdCardPortsEyemaxOperFactor_Type())
oaLdCardPortsEyemaxOperFactor.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdCardPortsEyemaxOperFactor.setStatus(_A)
if mibBuilder.loadTexts:oaLdCardPortsEyemaxOperFactor.setUnits(_e)
class _OaLdCardPortsEyemaxAdminFactor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_OaLdCardPortsEyemaxAdminFactor_Type.__name__=_D
_OaLdCardPortsEyemaxAdminFactor_Object=MibTableColumn
oaLdCardPortsEyemaxAdminFactor=_OaLdCardPortsEyemaxAdminFactor_Object((1,3,6,1,4,1,6926,1,41,8,1,1,32),_OaLdCardPortsEyemaxAdminFactor_Type())
oaLdCardPortsEyemaxAdminFactor.setMaxAccess(_F)
if mibBuilder.loadTexts:oaLdCardPortsEyemaxAdminFactor.setStatus(_A)
if mibBuilder.loadTexts:oaLdCardPortsEyemaxAdminFactor.setUnits(_e)
class _OaLdCardPortsFefMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_N,2),(_K,3)))
_OaLdCardPortsFefMode_Type.__name__=_D
_OaLdCardPortsFefMode_Object=MibTableColumn
oaLdCardPortsFefMode=_OaLdCardPortsFefMode_Object((1,3,6,1,4,1,6926,1,41,8,1,1,33),_OaLdCardPortsFefMode_Type())
oaLdCardPortsFefMode.setMaxAccess(_F)
if mibBuilder.loadTexts:oaLdCardPortsFefMode.setStatus(_A)
class _OaLdCardPortsOdu1Index_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4))
_OaLdCardPortsOdu1Index_Type.__name__=_D
_OaLdCardPortsOdu1Index_Object=MibTableColumn
oaLdCardPortsOdu1Index=_OaLdCardPortsOdu1Index_Object((1,3,6,1,4,1,6926,1,41,8,1,1,34),_OaLdCardPortsOdu1Index_Type())
oaLdCardPortsOdu1Index.setMaxAccess(_F)
if mibBuilder.loadTexts:oaLdCardPortsOdu1Index.setStatus(_A)
class _OaLdCardPortsOdu1TsIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_OaLdCardPortsOdu1TsIndex_Type.__name__=_D
_OaLdCardPortsOdu1TsIndex_Object=MibTableColumn
oaLdCardPortsOdu1TsIndex=_OaLdCardPortsOdu1TsIndex_Object((1,3,6,1,4,1,6926,1,41,8,1,1,35),_OaLdCardPortsOdu1TsIndex_Type())
oaLdCardPortsOdu1TsIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:oaLdCardPortsOdu1TsIndex.setStatus(_A)
class _OaLdCardPortsPmMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_N,2),(_K,3)))
_OaLdCardPortsPmMode_Type.__name__=_D
_OaLdCardPortsPmMode_Object=MibTableColumn
oaLdCardPortsPmMode=_OaLdCardPortsPmMode_Object((1,3,6,1,4,1,6926,1,41,8,1,1,36),_OaLdCardPortsPmMode_Type())
oaLdCardPortsPmMode.setMaxAccess(_F)
if mibBuilder.loadTexts:oaLdCardPortsPmMode.setStatus(_A)
class _OaLdCardPortsFecMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_E,1),('g709',2),('eFec',3),('byPass',4),('g9751i4',5),('g9751i7',6),('hFec-7',7),('zeroFec',8)))
_OaLdCardPortsFecMode_Type.__name__=_D
_OaLdCardPortsFecMode_Object=MibTableColumn
oaLdCardPortsFecMode=_OaLdCardPortsFecMode_Object((1,3,6,1,4,1,6926,1,41,8,1,1,37),_OaLdCardPortsFecMode_Type())
oaLdCardPortsFecMode.setMaxAccess(_F)
if mibBuilder.loadTexts:oaLdCardPortsFecMode.setStatus(_A)
class _OaLdCardPortsLock_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),('locked',2),('notlocked',3)))
_OaLdCardPortsLock_Type.__name__=_D
_OaLdCardPortsLock_Object=MibTableColumn
oaLdCardPortsLock=_OaLdCardPortsLock_Object((1,3,6,1,4,1,6926,1,41,8,1,1,38),_OaLdCardPortsLock_Type())
oaLdCardPortsLock.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdCardPortsLock.setStatus(_A)
class _OaLdCardPortsLaserMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_N,2),(_K,3)))
_OaLdCardPortsLaserMode_Type.__name__=_D
_OaLdCardPortsLaserMode_Object=MibTableColumn
oaLdCardPortsLaserMode=_OaLdCardPortsLaserMode_Object((1,3,6,1,4,1,6926,1,41,8,1,1,39),_OaLdCardPortsLaserMode_Type())
oaLdCardPortsLaserMode.setMaxAccess(_F)
if mibBuilder.loadTexts:oaLdCardPortsLaserMode.setStatus(_A)
_OaLdCardPortsOdu1TsSize_Type=Integer32
_OaLdCardPortsOdu1TsSize_Object=MibTableColumn
oaLdCardPortsOdu1TsSize=_OaLdCardPortsOdu1TsSize_Object((1,3,6,1,4,1,6926,1,41,8,1,1,40),_OaLdCardPortsOdu1TsSize_Type())
oaLdCardPortsOdu1TsSize.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdCardPortsOdu1TsSize.setStatus(_A)
class _OaLdCardPortsSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),('autoNegotiation',2),('force',3)))
_OaLdCardPortsSpeed_Type.__name__=_D
_OaLdCardPortsSpeed_Object=MibTableColumn
oaLdCardPortsSpeed=_OaLdCardPortsSpeed_Object((1,3,6,1,4,1,6926,1,41,8,1,1,41),_OaLdCardPortsSpeed_Type())
oaLdCardPortsSpeed.setMaxAccess(_F)
if mibBuilder.loadTexts:oaLdCardPortsSpeed.setStatus(_A)
_OaLdCardPortsPriorityClockSource_Type=Integer32
_OaLdCardPortsPriorityClockSource_Object=MibTableColumn
oaLdCardPortsPriorityClockSource=_OaLdCardPortsPriorityClockSource_Object((1,3,6,1,4,1,6926,1,41,8,1,1,42),_OaLdCardPortsPriorityClockSource_Type())
oaLdCardPortsPriorityClockSource.setMaxAccess(_F)
if mibBuilder.loadTexts:oaLdCardPortsPriorityClockSource.setStatus(_A)
class _OaLdCardPortsActionMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_W,1),(_p,2),(_q,3),('addAndDrop',4)))
_OaLdCardPortsActionMode_Type.__name__=_D
_OaLdCardPortsActionMode_Object=MibTableColumn
oaLdCardPortsActionMode=_OaLdCardPortsActionMode_Object((1,3,6,1,4,1,6926,1,41,8,1,1,43),_OaLdCardPortsActionMode_Type())
oaLdCardPortsActionMode.setMaxAccess(_F)
if mibBuilder.loadTexts:oaLdCardPortsActionMode.setStatus(_A)
_OaLdCardPortsOutputPortId_Type=Integer32
_OaLdCardPortsOutputPortId_Object=MibTableColumn
oaLdCardPortsOutputPortId=_OaLdCardPortsOutputPortId_Object((1,3,6,1,4,1,6926,1,41,8,1,1,44),_OaLdCardPortsOutputPortId_Type())
oaLdCardPortsOutputPortId.setMaxAccess(_F)
if mibBuilder.loadTexts:oaLdCardPortsOutputPortId.setStatus(_A)
_OaLdCardPortsGroupId_Type=Integer32
_OaLdCardPortsGroupId_Object=MibTableColumn
oaLdCardPortsGroupId=_OaLdCardPortsGroupId_Object((1,3,6,1,4,1,6926,1,41,8,1,1,45),_OaLdCardPortsGroupId_Type())
oaLdCardPortsGroupId.setMaxAccess(_F)
if mibBuilder.loadTexts:oaLdCardPortsGroupId.setStatus(_A)
_OaLdCardPortsChannelId_Type=Integer32
_OaLdCardPortsChannelId_Object=MibTableColumn
oaLdCardPortsChannelId=_OaLdCardPortsChannelId_Object((1,3,6,1,4,1,6926,1,41,8,1,1,46),_OaLdCardPortsChannelId_Type())
oaLdCardPortsChannelId.setMaxAccess(_F)
if mibBuilder.loadTexts:oaLdCardPortsChannelId.setStatus(_A)
class _OaLdCardPortsAutoShutdownMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_N,2),(_K,3)))
_OaLdCardPortsAutoShutdownMode_Type.__name__=_D
_OaLdCardPortsAutoShutdownMode_Object=MibTableColumn
oaLdCardPortsAutoShutdownMode=_OaLdCardPortsAutoShutdownMode_Object((1,3,6,1,4,1,6926,1,41,8,1,1,47),_OaLdCardPortsAutoShutdownMode_Type())
oaLdCardPortsAutoShutdownMode.setMaxAccess(_F)
if mibBuilder.loadTexts:oaLdCardPortsAutoShutdownMode.setStatus(_A)
_OaLdCardPortsEymxScnAmpFctr_Type=Integer32
_OaLdCardPortsEymxScnAmpFctr_Object=MibTableColumn
oaLdCardPortsEymxScnAmpFctr=_OaLdCardPortsEymxScnAmpFctr_Object((1,3,6,1,4,1,6926,1,41,8,1,1,48),_OaLdCardPortsEymxScnAmpFctr_Type())
oaLdCardPortsEymxScnAmpFctr.setMaxAccess(_F)
if mibBuilder.loadTexts:oaLdCardPortsEymxScnAmpFctr.setStatus(_A)
_OaLdCardPortsEymxScnAmpFctrMin_Type=Integer32
_OaLdCardPortsEymxScnAmpFctrMin_Object=MibTableColumn
oaLdCardPortsEymxScnAmpFctrMin=_OaLdCardPortsEymxScnAmpFctrMin_Object((1,3,6,1,4,1,6926,1,41,8,1,1,49),_OaLdCardPortsEymxScnAmpFctrMin_Type())
oaLdCardPortsEymxScnAmpFctrMin.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdCardPortsEymxScnAmpFctrMin.setStatus(_A)
_OaLdCardPortsEymxScnAmpFctrMax_Type=Integer32
_OaLdCardPortsEymxScnAmpFctrMax_Object=MibTableColumn
oaLdCardPortsEymxScnAmpFctrMax=_OaLdCardPortsEymxScnAmpFctrMax_Object((1,3,6,1,4,1,6926,1,41,8,1,1,50),_OaLdCardPortsEymxScnAmpFctrMax_Type())
oaLdCardPortsEymxScnAmpFctrMax.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdCardPortsEymxScnAmpFctrMax.setStatus(_A)
_OaLdCardPortsEymxScnDspComps_Type=Integer32
_OaLdCardPortsEymxScnDspComps_Object=MibTableColumn
oaLdCardPortsEymxScnDspComps=_OaLdCardPortsEymxScnDspComps_Object((1,3,6,1,4,1,6926,1,41,8,1,1,51),_OaLdCardPortsEymxScnDspComps_Type())
oaLdCardPortsEymxScnDspComps.setMaxAccess(_F)
if mibBuilder.loadTexts:oaLdCardPortsEymxScnDspComps.setStatus(_A)
class _OaLdCardPortsEymxScnTreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_OaLdCardPortsEymxScnTreshold_Type.__name__=_D
_OaLdCardPortsEymxScnTreshold_Object=MibTableColumn
oaLdCardPortsEymxScnTreshold=_OaLdCardPortsEymxScnTreshold_Object((1,3,6,1,4,1,6926,1,41,8,1,1,52),_OaLdCardPortsEymxScnTreshold_Type())
oaLdCardPortsEymxScnTreshold.setMaxAccess(_F)
if mibBuilder.loadTexts:oaLdCardPortsEymxScnTreshold.setStatus(_A)
if mibBuilder.loadTexts:oaLdCardPortsEymxScnTreshold.setUnits(_e)
class _OaLdCardPortsEymxScnOperComplt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_OaLdCardPortsEymxScnOperComplt_Type.__name__=_D
_OaLdCardPortsEymxScnOperComplt_Object=MibTableColumn
oaLdCardPortsEymxScnOperComplt=_OaLdCardPortsEymxScnOperComplt_Object((1,3,6,1,4,1,6926,1,41,8,1,1,53),_OaLdCardPortsEymxScnOperComplt_Type())
oaLdCardPortsEymxScnOperComplt.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdCardPortsEymxScnOperComplt.setStatus(_A)
if mibBuilder.loadTexts:oaLdCardPortsEymxScnOperComplt.setUnits(_e)
_OaLdCardPortsEymxScnResult_Type=DisplayString
_OaLdCardPortsEymxScnResult_Object=MibTableColumn
oaLdCardPortsEymxScnResult=_OaLdCardPortsEymxScnResult_Object((1,3,6,1,4,1,6926,1,41,8,1,1,54),_OaLdCardPortsEymxScnResult_Type())
oaLdCardPortsEymxScnResult.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdCardPortsEymxScnResult.setStatus(_A)
_OaLdAdcCardInfo_ObjectIdentity=ObjectIdentity
oaLdAdcCardInfo=_OaLdAdcCardInfo_ObjectIdentity((1,3,6,1,4,1,6926,1,41,9))
_OaLdAdcCardInfoTable_Object=MibTable
oaLdAdcCardInfoTable=_OaLdAdcCardInfoTable_Object((1,3,6,1,4,1,6926,1,41,9,2))
if mibBuilder.loadTexts:oaLdAdcCardInfoTable.setStatus(_A)
_OaLdAdcCardInfoEntry_Object=MibTableRow
oaLdAdcCardInfoEntry=_OaLdAdcCardInfoEntry_Object((1,3,6,1,4,1,6926,1,41,9,2,1))
oaLdAdcCardInfoEntry.setIndexNames((0,_C,_A9))
if mibBuilder.loadTexts:oaLdAdcCardInfoEntry.setStatus(_A)
_OaLdAdcCardSlotNumber_Type=Integer32
_OaLdAdcCardSlotNumber_Object=MibTableColumn
oaLdAdcCardSlotNumber=_OaLdAdcCardSlotNumber_Object((1,3,6,1,4,1,6926,1,41,9,2,1,1),_OaLdAdcCardSlotNumber_Type())
oaLdAdcCardSlotNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdAdcCardSlotNumber.setStatus(_A)
_OaLdAdcCardNumberOfPorts_Type=Integer32
_OaLdAdcCardNumberOfPorts_Object=MibTableColumn
oaLdAdcCardNumberOfPorts=_OaLdAdcCardNumberOfPorts_Object((1,3,6,1,4,1,6926,1,41,9,2,1,2),_OaLdAdcCardNumberOfPorts_Type())
oaLdAdcCardNumberOfPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdAdcCardNumberOfPorts.setStatus(_A)
class _OaLdAdcCardWdmWaveLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),('cwdm',2),('dwdm',3)))
_OaLdAdcCardWdmWaveLength_Type.__name__=_D
_OaLdAdcCardWdmWaveLength_Object=MibTableColumn
oaLdAdcCardWdmWaveLength=_OaLdAdcCardWdmWaveLength_Object((1,3,6,1,4,1,6926,1,41,9,2,1,3),_OaLdAdcCardWdmWaveLength_Type())
oaLdAdcCardWdmWaveLength.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdAdcCardWdmWaveLength.setStatus(_A)
class _OaLdAdcCardCardType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_E,1),('adc',2),('adcd',3),('mux',4),('dmux',5),('muxDmux',6)))
_OaLdAdcCardCardType_Type.__name__=_D
_OaLdAdcCardCardType_Object=MibTableColumn
oaLdAdcCardCardType=_OaLdAdcCardCardType_Object((1,3,6,1,4,1,6926,1,41,9,2,1,4),_OaLdAdcCardCardType_Type())
oaLdAdcCardCardType.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdAdcCardCardType.setStatus(_A)
class _OaLdAdcCardSpacing_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),('g50',2),('g100',3),('g200',4)))
_OaLdAdcCardSpacing_Type.__name__=_D
_OaLdAdcCardSpacing_Object=MibTableColumn
oaLdAdcCardSpacing=_OaLdAdcCardSpacing_Object((1,3,6,1,4,1,6926,1,41,9,2,1,5),_OaLdAdcCardSpacing_Type())
oaLdAdcCardSpacing.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdAdcCardSpacing.setStatus(_A)
class _OaLdAdcCardSubBand_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),('red',2),('blue',3),('redAndBlue',4)))
_OaLdAdcCardSubBand_Type.__name__=_D
_OaLdAdcCardSubBand_Object=MibTableColumn
oaLdAdcCardSubBand=_OaLdAdcCardSubBand_Object((1,3,6,1,4,1,6926,1,41,9,2,1,6),_OaLdAdcCardSubBand_Type())
oaLdAdcCardSubBand.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdAdcCardSubBand.setStatus(_A)
_OaLdAdcCardChannelsPerPort_Type=Integer32
_OaLdAdcCardChannelsPerPort_Object=MibTableColumn
oaLdAdcCardChannelsPerPort=_OaLdAdcCardChannelsPerPort_Object((1,3,6,1,4,1,6926,1,41,9,2,1,7),_OaLdAdcCardChannelsPerPort_Type())
oaLdAdcCardChannelsPerPort.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdAdcCardChannelsPerPort.setStatus(_A)
_OaLdAdcCardPortsInfoTable_Object=MibTable
oaLdAdcCardPortsInfoTable=_OaLdAdcCardPortsInfoTable_Object((1,3,6,1,4,1,6926,1,41,9,4))
if mibBuilder.loadTexts:oaLdAdcCardPortsInfoTable.setStatus(_A)
_OaLdAdcCardPortsInfoEntry_Object=MibTableRow
oaLdAdcCardPortsInfoEntry=_OaLdAdcCardPortsInfoEntry_Object((1,3,6,1,4,1,6926,1,41,9,4,1))
oaLdAdcCardPortsInfoEntry.setIndexNames((0,_C,_AA),(0,_C,_AB))
if mibBuilder.loadTexts:oaLdAdcCardPortsInfoEntry.setStatus(_A)
_OaLdAdcCardPortsSlotNumber_Type=Integer32
_OaLdAdcCardPortsSlotNumber_Object=MibTableColumn
oaLdAdcCardPortsSlotNumber=_OaLdAdcCardPortsSlotNumber_Object((1,3,6,1,4,1,6926,1,41,9,4,1,1),_OaLdAdcCardPortsSlotNumber_Type())
oaLdAdcCardPortsSlotNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdAdcCardPortsSlotNumber.setStatus(_A)
_OaLdAdcCardPortsPortNumber_Type=Integer32
_OaLdAdcCardPortsPortNumber_Object=MibTableColumn
oaLdAdcCardPortsPortNumber=_OaLdAdcCardPortsPortNumber_Object((1,3,6,1,4,1,6926,1,41,9,4,1,2),_OaLdAdcCardPortsPortNumber_Type())
oaLdAdcCardPortsPortNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdAdcCardPortsPortNumber.setStatus(_A)
_OaLdAdcCardPortsLambdaCh_Type=LambdaCh
_OaLdAdcCardPortsLambdaCh_Object=MibTableColumn
oaLdAdcCardPortsLambdaCh=_OaLdAdcCardPortsLambdaCh_Object((1,3,6,1,4,1,6926,1,41,9,4,1,3),_OaLdAdcCardPortsLambdaCh_Type())
oaLdAdcCardPortsLambdaCh.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdAdcCardPortsLambdaCh.setStatus(_A)
_OaLdCardChannelInfo_ObjectIdentity=ObjectIdentity
oaLdCardChannelInfo=_OaLdCardChannelInfo_ObjectIdentity((1,3,6,1,4,1,6926,1,41,11))
_OaLdCardChannelCfgTable_Object=MibTable
oaLdCardChannelCfgTable=_OaLdCardChannelCfgTable_Object((1,3,6,1,4,1,6926,1,41,11,2))
if mibBuilder.loadTexts:oaLdCardChannelCfgTable.setStatus(_A)
_OaLdCardChannelCfgEntry_Object=MibTableRow
oaLdCardChannelCfgEntry=_OaLdCardChannelCfgEntry_Object((1,3,6,1,4,1,6926,1,41,11,2,1))
oaLdCardChannelCfgEntry.setIndexNames((0,_C,_AC),(0,_C,_AD),(0,_C,_AE))
if mibBuilder.loadTexts:oaLdCardChannelCfgEntry.setStatus(_A)
_OaLdCardChSlotId_Type=Integer32
_OaLdCardChSlotId_Object=MibTableColumn
oaLdCardChSlotId=_OaLdCardChSlotId_Object((1,3,6,1,4,1,6926,1,41,11,2,1,1),_OaLdCardChSlotId_Type())
oaLdCardChSlotId.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdCardChSlotId.setStatus(_A)
_OaLdCardChGroupId_Type=Integer32
_OaLdCardChGroupId_Object=MibTableColumn
oaLdCardChGroupId=_OaLdCardChGroupId_Object((1,3,6,1,4,1,6926,1,41,11,2,1,2),_OaLdCardChGroupId_Type())
oaLdCardChGroupId.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdCardChGroupId.setStatus(_A)
class _OaLdCardChChannelId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_OaLdCardChChannelId_Type.__name__=_D
_OaLdCardChChannelId_Object=MibTableColumn
oaLdCardChChannelId=_OaLdCardChChannelId_Object((1,3,6,1,4,1,6926,1,41,11,2,1,3),_OaLdCardChChannelId_Type())
oaLdCardChChannelId.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdCardChChannelId.setStatus(_A)
class _OaLdCardChOdu1Index_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4))
_OaLdCardChOdu1Index_Type.__name__=_D
_OaLdCardChOdu1Index_Object=MibTableColumn
oaLdCardChOdu1Index=_OaLdCardChOdu1Index_Object((1,3,6,1,4,1,6926,1,41,11,2,1,4),_OaLdCardChOdu1Index_Type())
oaLdCardChOdu1Index.setMaxAccess(_F)
if mibBuilder.loadTexts:oaLdCardChOdu1Index.setStatus(_A)
class _OaLdCardChOdu1TsIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_OaLdCardChOdu1TsIndex_Type.__name__=_D
_OaLdCardChOdu1TsIndex_Object=MibTableColumn
oaLdCardChOdu1TsIndex=_OaLdCardChOdu1TsIndex_Object((1,3,6,1,4,1,6926,1,41,11,2,1,5),_OaLdCardChOdu1TsIndex_Type())
oaLdCardChOdu1TsIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:oaLdCardChOdu1TsIndex.setStatus(_A)
_OaLdCardChOdu1TsSize_Type=Integer32
_OaLdCardChOdu1TsSize_Object=MibTableColumn
oaLdCardChOdu1TsSize=_OaLdCardChOdu1TsSize_Object((1,3,6,1,4,1,6926,1,41,11,2,1,6),_OaLdCardChOdu1TsSize_Type())
oaLdCardChOdu1TsSize.setMaxAccess(_F)
if mibBuilder.loadTexts:oaLdCardChOdu1TsSize.setStatus(_A)
_OaLdCardChRate_Type=RateMode
_OaLdCardChRate_Object=MibTableColumn
oaLdCardChRate=_OaLdCardChRate_Object((1,3,6,1,4,1,6926,1,41,11,2,1,7),_OaLdCardChRate_Type())
oaLdCardChRate.setMaxAccess(_F)
if mibBuilder.loadTexts:oaLdCardChRate.setStatus(_A)
_OaLdOAmplifierInfo_ObjectIdentity=ObjectIdentity
oaLdOAmplifierInfo=_OaLdOAmplifierInfo_ObjectIdentity((1,3,6,1,4,1,6926,1,41,12))
_OaLdOAmplifierCardInfoTable_Object=MibTable
oaLdOAmplifierCardInfoTable=_OaLdOAmplifierCardInfoTable_Object((1,3,6,1,4,1,6926,1,41,12,2))
if mibBuilder.loadTexts:oaLdOAmplifierCardInfoTable.setStatus(_A)
_OaLdOAmplifierCardInfoEntry_Object=MibTableRow
oaLdOAmplifierCardInfoEntry=_OaLdOAmplifierCardInfoEntry_Object((1,3,6,1,4,1,6926,1,41,12,2,1))
oaLdOAmplifierCardInfoEntry.setIndexNames((0,_C,_r))
if mibBuilder.loadTexts:oaLdOAmplifierCardInfoEntry.setStatus(_A)
_OaLdOAmplifierCardSlotNumber_Type=Integer32
_OaLdOAmplifierCardSlotNumber_Object=MibTableColumn
oaLdOAmplifierCardSlotNumber=_OaLdOAmplifierCardSlotNumber_Object((1,3,6,1,4,1,6926,1,41,12,2,1,1),_OaLdOAmplifierCardSlotNumber_Type())
oaLdOAmplifierCardSlotNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdOAmplifierCardSlotNumber.setStatus(_A)
class _OaLdOAmplifierCardConfiguration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),('singlePump',2),('dualPump',3),('quadroPump',4)))
_OaLdOAmplifierCardConfiguration_Type.__name__=_D
_OaLdOAmplifierCardConfiguration_Object=MibTableColumn
oaLdOAmplifierCardConfiguration=_OaLdOAmplifierCardConfiguration_Object((1,3,6,1,4,1,6926,1,41,12,2,1,2),_OaLdOAmplifierCardConfiguration_Type())
oaLdOAmplifierCardConfiguration.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdOAmplifierCardConfiguration.setStatus(_A)
class _OaLdOAmplifierCardModuleType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_E,1),('amplet',2),('bosterAmplifier',3),('lineAmplifier',4),('preAmplifier',5),('vgoaRamanAmplifier',6),('cBandRamanAmplifier',7)))
_OaLdOAmplifierCardModuleType_Type.__name__=_D
_OaLdOAmplifierCardModuleType_Object=MibTableColumn
oaLdOAmplifierCardModuleType=_OaLdOAmplifierCardModuleType_Object((1,3,6,1,4,1,6926,1,41,12,2,1,3),_OaLdOAmplifierCardModuleType_Type())
oaLdOAmplifierCardModuleType.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdOAmplifierCardModuleType.setStatus(_A)
class _OaLdOAmplifierCardHardwareVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_OaLdOAmplifierCardHardwareVersion_Type.__name__=_J
_OaLdOAmplifierCardHardwareVersion_Object=MibTableColumn
oaLdOAmplifierCardHardwareVersion=_OaLdOAmplifierCardHardwareVersion_Object((1,3,6,1,4,1,6926,1,41,12,2,1,4),_OaLdOAmplifierCardHardwareVersion_Type())
oaLdOAmplifierCardHardwareVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdOAmplifierCardHardwareVersion.setStatus(_A)
class _OaLdOAmplifierCardSoftwareVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_OaLdOAmplifierCardSoftwareVersion_Type.__name__=_J
_OaLdOAmplifierCardSoftwareVersion_Object=MibTableColumn
oaLdOAmplifierCardSoftwareVersion=_OaLdOAmplifierCardSoftwareVersion_Object((1,3,6,1,4,1,6926,1,41,12,2,1,5),_OaLdOAmplifierCardSoftwareVersion_Type())
oaLdOAmplifierCardSoftwareVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdOAmplifierCardSoftwareVersion.setStatus(_A)
class _OaLdOAmplifierCardSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_OaLdOAmplifierCardSerialNumber_Type.__name__=_J
_OaLdOAmplifierCardSerialNumber_Object=MibTableColumn
oaLdOAmplifierCardSerialNumber=_OaLdOAmplifierCardSerialNumber_Object((1,3,6,1,4,1,6926,1,41,12,2,1,6),_OaLdOAmplifierCardSerialNumber_Type())
oaLdOAmplifierCardSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdOAmplifierCardSerialNumber.setStatus(_A)
_OaLdOAmplifierCardTemperature_Type=Integer32
_OaLdOAmplifierCardTemperature_Object=MibTableColumn
oaLdOAmplifierCardTemperature=_OaLdOAmplifierCardTemperature_Object((1,3,6,1,4,1,6926,1,41,12,2,1,7),_OaLdOAmplifierCardTemperature_Type())
oaLdOAmplifierCardTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdOAmplifierCardTemperature.setStatus(_A)
_OaLdOAmplifierCardPSVoltage_Type=Integer32
_OaLdOAmplifierCardPSVoltage_Object=MibTableColumn
oaLdOAmplifierCardPSVoltage=_OaLdOAmplifierCardPSVoltage_Object((1,3,6,1,4,1,6926,1,41,12,2,1,8),_OaLdOAmplifierCardPSVoltage_Type())
oaLdOAmplifierCardPSVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdOAmplifierCardPSVoltage.setStatus(_A)
_OaLdOAmplifierCardPump1Current_Type=Integer32
_OaLdOAmplifierCardPump1Current_Object=MibTableColumn
oaLdOAmplifierCardPump1Current=_OaLdOAmplifierCardPump1Current_Object((1,3,6,1,4,1,6926,1,41,12,2,1,9),_OaLdOAmplifierCardPump1Current_Type())
oaLdOAmplifierCardPump1Current.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdOAmplifierCardPump1Current.setStatus(_A)
_OaLdOAmplifierCardPump1MaxCurrent_Type=Integer32
_OaLdOAmplifierCardPump1MaxCurrent_Object=MibTableColumn
oaLdOAmplifierCardPump1MaxCurrent=_OaLdOAmplifierCardPump1MaxCurrent_Object((1,3,6,1,4,1,6926,1,41,12,2,1,10),_OaLdOAmplifierCardPump1MaxCurrent_Type())
oaLdOAmplifierCardPump1MaxCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdOAmplifierCardPump1MaxCurrent.setStatus(_A)
_OaLdOAmplifierCardPump2Current_Type=Integer32
_OaLdOAmplifierCardPump2Current_Object=MibTableColumn
oaLdOAmplifierCardPump2Current=_OaLdOAmplifierCardPump2Current_Object((1,3,6,1,4,1,6926,1,41,12,2,1,11),_OaLdOAmplifierCardPump2Current_Type())
oaLdOAmplifierCardPump2Current.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdOAmplifierCardPump2Current.setStatus(_A)
_OaLdOAmplifierCardPump2MaxCurrent_Type=Integer32
_OaLdOAmplifierCardPump2MaxCurrent_Object=MibTableColumn
oaLdOAmplifierCardPump2MaxCurrent=_OaLdOAmplifierCardPump2MaxCurrent_Object((1,3,6,1,4,1,6926,1,41,12,2,1,12),_OaLdOAmplifierCardPump2MaxCurrent_Type())
oaLdOAmplifierCardPump2MaxCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdOAmplifierCardPump2MaxCurrent.setStatus(_A)
_OaLdOAmplifierCardInputPower_Type=Integer32
_OaLdOAmplifierCardInputPower_Object=MibTableColumn
oaLdOAmplifierCardInputPower=_OaLdOAmplifierCardInputPower_Object((1,3,6,1,4,1,6926,1,41,12,2,1,13),_OaLdOAmplifierCardInputPower_Type())
oaLdOAmplifierCardInputPower.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdOAmplifierCardInputPower.setStatus(_A)
_OaLdOAmplifierCardOutputPower_Type=Integer32
_OaLdOAmplifierCardOutputPower_Object=MibTableColumn
oaLdOAmplifierCardOutputPower=_OaLdOAmplifierCardOutputPower_Object((1,3,6,1,4,1,6926,1,41,12,2,1,14),_OaLdOAmplifierCardOutputPower_Type())
oaLdOAmplifierCardOutputPower.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdOAmplifierCardOutputPower.setStatus(_A)
_OaLdOAmplifierCardModuleGain_Type=Integer32
_OaLdOAmplifierCardModuleGain_Object=MibTableColumn
oaLdOAmplifierCardModuleGain=_OaLdOAmplifierCardModuleGain_Object((1,3,6,1,4,1,6926,1,41,12,2,1,15),_OaLdOAmplifierCardModuleGain_Type())
oaLdOAmplifierCardModuleGain.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdOAmplifierCardModuleGain.setStatus(_A)
_OaLdOAmplifierCardPump1Power_Type=Integer32
_OaLdOAmplifierCardPump1Power_Object=MibTableColumn
oaLdOAmplifierCardPump1Power=_OaLdOAmplifierCardPump1Power_Object((1,3,6,1,4,1,6926,1,41,12,2,1,16),_OaLdOAmplifierCardPump1Power_Type())
oaLdOAmplifierCardPump1Power.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdOAmplifierCardPump1Power.setStatus(_A)
_OaLdOAmplifierCardPump2Power_Type=Integer32
_OaLdOAmplifierCardPump2Power_Object=MibTableColumn
oaLdOAmplifierCardPump2Power=_OaLdOAmplifierCardPump2Power_Object((1,3,6,1,4,1,6926,1,41,12,2,1,17),_OaLdOAmplifierCardPump2Power_Type())
oaLdOAmplifierCardPump2Power.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdOAmplifierCardPump2Power.setStatus(_A)
_OaLdOAmplifierCardMaximumPower_Type=Integer32
_OaLdOAmplifierCardMaximumPower_Object=MibTableColumn
oaLdOAmplifierCardMaximumPower=_OaLdOAmplifierCardMaximumPower_Object((1,3,6,1,4,1,6926,1,41,12,2,1,18),_OaLdOAmplifierCardMaximumPower_Type())
oaLdOAmplifierCardMaximumPower.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdOAmplifierCardMaximumPower.setStatus(_A)
_OaLdOAmplifierCardRatedGain_Type=Integer32
_OaLdOAmplifierCardRatedGain_Object=MibTableColumn
oaLdOAmplifierCardRatedGain=_OaLdOAmplifierCardRatedGain_Object((1,3,6,1,4,1,6926,1,41,12,2,1,19),_OaLdOAmplifierCardRatedGain_Type())
oaLdOAmplifierCardRatedGain.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdOAmplifierCardRatedGain.setStatus(_A)
class _OaLdOAmplifierCardAlarmStatus_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_OaLdOAmplifierCardAlarmStatus_Type.__name__=_X
_OaLdOAmplifierCardAlarmStatus_Object=MibTableColumn
oaLdOAmplifierCardAlarmStatus=_OaLdOAmplifierCardAlarmStatus_Object((1,3,6,1,4,1,6926,1,41,12,2,1,20),_OaLdOAmplifierCardAlarmStatus_Type())
oaLdOAmplifierCardAlarmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdOAmplifierCardAlarmStatus.setStatus(_A)
class _OaLdOAmplifierCardAttributes_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_OaLdOAmplifierCardAttributes_Type.__name__=_X
_OaLdOAmplifierCardAttributes_Object=MibTableColumn
oaLdOAmplifierCardAttributes=_OaLdOAmplifierCardAttributes_Object((1,3,6,1,4,1,6926,1,41,12,2,1,25),_OaLdOAmplifierCardAttributes_Type())
oaLdOAmplifierCardAttributes.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdOAmplifierCardAttributes.setStatus(_A)
class _OaLdOAmplifierCardOperationMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_E,1),('constantCurrent',2),('constantPumpPower',3),('constantOutputPower',4),('constantGain',5)))
_OaLdOAmplifierCardOperationMode_Type.__name__=_D
_OaLdOAmplifierCardOperationMode_Object=MibTableColumn
oaLdOAmplifierCardOperationMode=_OaLdOAmplifierCardOperationMode_Object((1,3,6,1,4,1,6926,1,41,12,2,1,30),_OaLdOAmplifierCardOperationMode_Type())
oaLdOAmplifierCardOperationMode.setMaxAccess(_F)
if mibBuilder.loadTexts:oaLdOAmplifierCardOperationMode.setStatus(_A)
class _OaLdOAmplifierCardRunMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),('start',2),('shutdownPower',3),('eyeSafe',4)))
_OaLdOAmplifierCardRunMode_Type.__name__=_D
_OaLdOAmplifierCardRunMode_Object=MibTableColumn
oaLdOAmplifierCardRunMode=_OaLdOAmplifierCardRunMode_Object((1,3,6,1,4,1,6926,1,41,12,2,1,31),_OaLdOAmplifierCardRunMode_Type())
oaLdOAmplifierCardRunMode.setMaxAccess(_F)
if mibBuilder.loadTexts:oaLdOAmplifierCardRunMode.setStatus(_A)
class _OaLdOAmplifierCardAutoShutdownState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_N,2),(_K,3)))
_OaLdOAmplifierCardAutoShutdownState_Type.__name__=_D
_OaLdOAmplifierCardAutoShutdownState_Object=MibTableColumn
oaLdOAmplifierCardAutoShutdownState=_OaLdOAmplifierCardAutoShutdownState_Object((1,3,6,1,4,1,6926,1,41,12,2,1,32),_OaLdOAmplifierCardAutoShutdownState_Type())
oaLdOAmplifierCardAutoShutdownState.setMaxAccess(_F)
if mibBuilder.loadTexts:oaLdOAmplifierCardAutoShutdownState.setStatus(_A)
_OaLdOAmplifierCardInputThreshold_Type=Integer32
_OaLdOAmplifierCardInputThreshold_Object=MibTableColumn
oaLdOAmplifierCardInputThreshold=_OaLdOAmplifierCardInputThreshold_Object((1,3,6,1,4,1,6926,1,41,12,2,1,33),_OaLdOAmplifierCardInputThreshold_Type())
oaLdOAmplifierCardInputThreshold.setMaxAccess(_F)
if mibBuilder.loadTexts:oaLdOAmplifierCardInputThreshold.setStatus(_A)
_OaLdOAmplifierCardOutputThreshold_Type=Integer32
_OaLdOAmplifierCardOutputThreshold_Object=MibTableColumn
oaLdOAmplifierCardOutputThreshold=_OaLdOAmplifierCardOutputThreshold_Object((1,3,6,1,4,1,6926,1,41,12,2,1,34),_OaLdOAmplifierCardOutputThreshold_Type())
oaLdOAmplifierCardOutputThreshold.setMaxAccess(_F)
if mibBuilder.loadTexts:oaLdOAmplifierCardOutputThreshold.setStatus(_A)
_OaLdOAmplifierCardShutdownThreshold_Type=Integer32
_OaLdOAmplifierCardShutdownThreshold_Object=MibTableColumn
oaLdOAmplifierCardShutdownThreshold=_OaLdOAmplifierCardShutdownThreshold_Object((1,3,6,1,4,1,6926,1,41,12,2,1,35),_OaLdOAmplifierCardShutdownThreshold_Type())
oaLdOAmplifierCardShutdownThreshold.setMaxAccess(_F)
if mibBuilder.loadTexts:oaLdOAmplifierCardShutdownThreshold.setStatus(_A)
_OaLdOAmplifierCardLowTempThreshold_Type=Integer32
_OaLdOAmplifierCardLowTempThreshold_Object=MibTableColumn
oaLdOAmplifierCardLowTempThreshold=_OaLdOAmplifierCardLowTempThreshold_Object((1,3,6,1,4,1,6926,1,41,12,2,1,36),_OaLdOAmplifierCardLowTempThreshold_Type())
oaLdOAmplifierCardLowTempThreshold.setMaxAccess(_F)
if mibBuilder.loadTexts:oaLdOAmplifierCardLowTempThreshold.setStatus(_A)
_OaLdOAmplifierCardHighTempThreshold_Type=Integer32
_OaLdOAmplifierCardHighTempThreshold_Object=MibTableColumn
oaLdOAmplifierCardHighTempThreshold=_OaLdOAmplifierCardHighTempThreshold_Object((1,3,6,1,4,1,6926,1,41,12,2,1,37),_OaLdOAmplifierCardHighTempThreshold_Type())
oaLdOAmplifierCardHighTempThreshold.setMaxAccess(_F)
if mibBuilder.loadTexts:oaLdOAmplifierCardHighTempThreshold.setStatus(_A)
_OaLdOAmplifierCardPump1CurrentSet_Type=Integer32
_OaLdOAmplifierCardPump1CurrentSet_Object=MibTableColumn
oaLdOAmplifierCardPump1CurrentSet=_OaLdOAmplifierCardPump1CurrentSet_Object((1,3,6,1,4,1,6926,1,41,12,2,1,38),_OaLdOAmplifierCardPump1CurrentSet_Type())
oaLdOAmplifierCardPump1CurrentSet.setMaxAccess(_F)
if mibBuilder.loadTexts:oaLdOAmplifierCardPump1CurrentSet.setStatus(_A)
_OaLdOAmplifierCardPump2CurrentSet_Type=Integer32
_OaLdOAmplifierCardPump2CurrentSet_Object=MibTableColumn
oaLdOAmplifierCardPump2CurrentSet=_OaLdOAmplifierCardPump2CurrentSet_Object((1,3,6,1,4,1,6926,1,41,12,2,1,39),_OaLdOAmplifierCardPump2CurrentSet_Type())
oaLdOAmplifierCardPump2CurrentSet.setMaxAccess(_F)
if mibBuilder.loadTexts:oaLdOAmplifierCardPump2CurrentSet.setStatus(_A)
_OaLdOAmplifierCardOutputPowerSet_Type=Integer32
_OaLdOAmplifierCardOutputPowerSet_Object=MibTableColumn
oaLdOAmplifierCardOutputPowerSet=_OaLdOAmplifierCardOutputPowerSet_Object((1,3,6,1,4,1,6926,1,41,12,2,1,40),_OaLdOAmplifierCardOutputPowerSet_Type())
oaLdOAmplifierCardOutputPowerSet.setMaxAccess(_F)
if mibBuilder.loadTexts:oaLdOAmplifierCardOutputPowerSet.setStatus(_A)
_OaLdOAmplifierCardGainSet_Type=Integer32
_OaLdOAmplifierCardGainSet_Object=MibTableColumn
oaLdOAmplifierCardGainSet=_OaLdOAmplifierCardGainSet_Object((1,3,6,1,4,1,6926,1,41,12,2,1,41),_OaLdOAmplifierCardGainSet_Type())
oaLdOAmplifierCardGainSet.setMaxAccess(_F)
if mibBuilder.loadTexts:oaLdOAmplifierCardGainSet.setStatus(_A)
_OaLdOAmplifierCardPumpOutputPower_Type=Integer32
_OaLdOAmplifierCardPumpOutputPower_Object=MibTableColumn
oaLdOAmplifierCardPumpOutputPower=_OaLdOAmplifierCardPumpOutputPower_Object((1,3,6,1,4,1,6926,1,41,12,2,1,42),_OaLdOAmplifierCardPumpOutputPower_Type())
oaLdOAmplifierCardPumpOutputPower.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdOAmplifierCardPumpOutputPower.setStatus(_A)
_OaLdOAmplifierCardReflectedPower_Type=Integer32
_OaLdOAmplifierCardReflectedPower_Object=MibTableColumn
oaLdOAmplifierCardReflectedPower=_OaLdOAmplifierCardReflectedPower_Object((1,3,6,1,4,1,6926,1,41,12,2,1,43),_OaLdOAmplifierCardReflectedPower_Type())
oaLdOAmplifierCardReflectedPower.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdOAmplifierCardReflectedPower.setStatus(_A)
_OaLdOAmplifierCardBackReflRatio_Type=Integer32
_OaLdOAmplifierCardBackReflRatio_Object=MibTableColumn
oaLdOAmplifierCardBackReflRatio=_OaLdOAmplifierCardBackReflRatio_Object((1,3,6,1,4,1,6926,1,41,12,2,1,44),_OaLdOAmplifierCardBackReflRatio_Type())
oaLdOAmplifierCardBackReflRatio.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdOAmplifierCardBackReflRatio.setStatus(_A)
_OaLdOAmplifierCardBackReflThresh_Type=Integer32
_OaLdOAmplifierCardBackReflThresh_Object=MibTableColumn
oaLdOAmplifierCardBackReflThresh=_OaLdOAmplifierCardBackReflThresh_Object((1,3,6,1,4,1,6926,1,41,12,2,1,45),_OaLdOAmplifierCardBackReflThresh_Type())
oaLdOAmplifierCardBackReflThresh.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdOAmplifierCardBackReflThresh.setStatus(_A)
class _OaLdOAmplifierCardAutoPowerReduction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_N,2),(_K,3)))
_OaLdOAmplifierCardAutoPowerReduction_Type.__name__=_D
_OaLdOAmplifierCardAutoPowerReduction_Object=MibTableColumn
oaLdOAmplifierCardAutoPowerReduction=_OaLdOAmplifierCardAutoPowerReduction_Object((1,3,6,1,4,1,6926,1,41,12,2,1,46),_OaLdOAmplifierCardAutoPowerReduction_Type())
oaLdOAmplifierCardAutoPowerReduction.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdOAmplifierCardAutoPowerReduction.setStatus(_A)
_OaLdOAmplifierCardOutputPumpPowerThresh_Type=Integer32
_OaLdOAmplifierCardOutputPumpPowerThresh_Object=MibTableColumn
oaLdOAmplifierCardOutputPumpPowerThresh=_OaLdOAmplifierCardOutputPumpPowerThresh_Object((1,3,6,1,4,1,6926,1,41,12,2,1,47),_OaLdOAmplifierCardOutputPumpPowerThresh_Type())
oaLdOAmplifierCardOutputPumpPowerThresh.setMaxAccess(_F)
if mibBuilder.loadTexts:oaLdOAmplifierCardOutputPumpPowerThresh.setStatus(_A)
_OaLdOAmplifierCardCalibrationFactor_Type=Integer32
_OaLdOAmplifierCardCalibrationFactor_Object=MibTableColumn
oaLdOAmplifierCardCalibrationFactor=_OaLdOAmplifierCardCalibrationFactor_Object((1,3,6,1,4,1,6926,1,41,12,2,1,48),_OaLdOAmplifierCardCalibrationFactor_Type())
oaLdOAmplifierCardCalibrationFactor.setMaxAccess(_F)
if mibBuilder.loadTexts:oaLdOAmplifierCardCalibrationFactor.setStatus(_A)
class _OaLdOAmplifierCardTempAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_N,2),(_K,3)))
_OaLdOAmplifierCardTempAlarm_Type.__name__=_D
_OaLdOAmplifierCardTempAlarm_Object=MibTableColumn
oaLdOAmplifierCardTempAlarm=_OaLdOAmplifierCardTempAlarm_Object((1,3,6,1,4,1,6926,1,41,12,2,1,49),_OaLdOAmplifierCardTempAlarm_Type())
oaLdOAmplifierCardTempAlarm.setMaxAccess(_F)
if mibBuilder.loadTexts:oaLdOAmplifierCardTempAlarm.setStatus(_A)
_OaLdOAmplifierCardPump1Ratio_Type=Integer32
_OaLdOAmplifierCardPump1Ratio_Object=MibTableColumn
oaLdOAmplifierCardPump1Ratio=_OaLdOAmplifierCardPump1Ratio_Object((1,3,6,1,4,1,6926,1,41,12,2,1,50),_OaLdOAmplifierCardPump1Ratio_Type())
oaLdOAmplifierCardPump1Ratio.setMaxAccess(_F)
if mibBuilder.loadTexts:oaLdOAmplifierCardPump1Ratio.setStatus(_A)
_OaLdOAmplifierPumpInfoTable_Object=MibTable
oaLdOAmplifierPumpInfoTable=_OaLdOAmplifierPumpInfoTable_Object((1,3,6,1,4,1,6926,1,41,12,3))
if mibBuilder.loadTexts:oaLdOAmplifierPumpInfoTable.setStatus(_A)
_OaLdOAmplifierPumpInfoEntry_Object=MibTableRow
oaLdOAmplifierPumpInfoEntry=_OaLdOAmplifierPumpInfoEntry_Object((1,3,6,1,4,1,6926,1,41,12,3,1))
oaLdOAmplifierPumpInfoEntry.setIndexNames((0,_C,_r),(0,_C,_AF))
if mibBuilder.loadTexts:oaLdOAmplifierPumpInfoEntry.setStatus(_A)
_OaLdOAmplifierPumpNumber_Type=Integer32
_OaLdOAmplifierPumpNumber_Object=MibTableColumn
oaLdOAmplifierPumpNumber=_OaLdOAmplifierPumpNumber_Object((1,3,6,1,4,1,6926,1,41,12,3,1,2),_OaLdOAmplifierPumpNumber_Type())
oaLdOAmplifierPumpNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdOAmplifierPumpNumber.setStatus(_A)
_OaLdOAmplifierPumpCurrent_Type=Integer32
_OaLdOAmplifierPumpCurrent_Object=MibTableColumn
oaLdOAmplifierPumpCurrent=_OaLdOAmplifierPumpCurrent_Object((1,3,6,1,4,1,6926,1,41,12,3,1,3),_OaLdOAmplifierPumpCurrent_Type())
oaLdOAmplifierPumpCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdOAmplifierPumpCurrent.setStatus(_A)
_OaLdOAmplifierPumpPower_Type=Integer32
_OaLdOAmplifierPumpPower_Object=MibTableColumn
oaLdOAmplifierPumpPower=_OaLdOAmplifierPumpPower_Object((1,3,6,1,4,1,6926,1,41,12,3,1,4),_OaLdOAmplifierPumpPower_Type())
oaLdOAmplifierPumpPower.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdOAmplifierPumpPower.setStatus(_A)
_OaLdOAmplifierPumpLaserTemp_Type=Integer32
_OaLdOAmplifierPumpLaserTemp_Object=MibTableColumn
oaLdOAmplifierPumpLaserTemp=_OaLdOAmplifierPumpLaserTemp_Object((1,3,6,1,4,1,6926,1,41,12,3,1,5),_OaLdOAmplifierPumpLaserTemp_Type())
oaLdOAmplifierPumpLaserTemp.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdOAmplifierPumpLaserTemp.setStatus(_A)
_OaLdOAmplifierCompInterfaceCount_Type=Integer32
_OaLdOAmplifierCompInterfaceCount_Object=MibScalar
oaLdOAmplifierCompInterfaceCount=_OaLdOAmplifierCompInterfaceCount_Object((1,3,6,1,4,1,6926,1,41,12,10),_OaLdOAmplifierCompInterfaceCount_Type())
oaLdOAmplifierCompInterfaceCount.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdOAmplifierCompInterfaceCount.setStatus(_A)
_OaLdOcmCardInfo_ObjectIdentity=ObjectIdentity
oaLdOcmCardInfo=_OaLdOcmCardInfo_ObjectIdentity((1,3,6,1,4,1,6926,1,41,13))
_OaLdOcmCardPortsInfoTable_Object=MibTable
oaLdOcmCardPortsInfoTable=_OaLdOcmCardPortsInfoTable_Object((1,3,6,1,4,1,6926,1,41,13,2))
if mibBuilder.loadTexts:oaLdOcmCardPortsInfoTable.setStatus(_A)
_OaLdOcmCardPortsInfoEntry_Object=MibTableRow
oaLdOcmCardPortsInfoEntry=_OaLdOcmCardPortsInfoEntry_Object((1,3,6,1,4,1,6926,1,41,13,2,1))
oaLdOcmCardPortsInfoEntry.setIndexNames((0,_C,_AG),(0,_C,_AH))
if mibBuilder.loadTexts:oaLdOcmCardPortsInfoEntry.setStatus(_A)
_OaLdOcmCardPortsSlotNumber_Type=Integer32
_OaLdOcmCardPortsSlotNumber_Object=MibTableColumn
oaLdOcmCardPortsSlotNumber=_OaLdOcmCardPortsSlotNumber_Object((1,3,6,1,4,1,6926,1,41,13,2,1,1),_OaLdOcmCardPortsSlotNumber_Type())
oaLdOcmCardPortsSlotNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdOcmCardPortsSlotNumber.setStatus(_A)
_OaLdOcmCardPortsPortNumber_Type=Integer32
_OaLdOcmCardPortsPortNumber_Object=MibTableColumn
oaLdOcmCardPortsPortNumber=_OaLdOcmCardPortsPortNumber_Object((1,3,6,1,4,1,6926,1,41,13,2,1,2),_OaLdOcmCardPortsPortNumber_Type())
oaLdOcmCardPortsPortNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdOcmCardPortsPortNumber.setStatus(_A)
class _OaLdOcmCardPortsSectionLof_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_T,2),(_L,3),(_M,4)))
_OaLdOcmCardPortsSectionLof_Type.__name__=_D
_OaLdOcmCardPortsSectionLof_Object=MibTableColumn
oaLdOcmCardPortsSectionLof=_OaLdOcmCardPortsSectionLof_Object((1,3,6,1,4,1,6926,1,41,13,2,1,3),_OaLdOcmCardPortsSectionLof_Type())
oaLdOcmCardPortsSectionLof.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdOcmCardPortsSectionLof.setStatus(_A)
class _OaLdOcmCardPortsSectionLos_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_T,2),(_L,3),(_M,4)))
_OaLdOcmCardPortsSectionLos_Type.__name__=_D
_OaLdOcmCardPortsSectionLos_Object=MibTableColumn
oaLdOcmCardPortsSectionLos=_OaLdOcmCardPortsSectionLos_Object((1,3,6,1,4,1,6926,1,41,13,2,1,4),_OaLdOcmCardPortsSectionLos_Type())
oaLdOcmCardPortsSectionLos.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdOcmCardPortsSectionLos.setStatus(_A)
class _OaLdOcmCardPortsSectionLoc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_T,2),(_L,3),(_M,4)))
_OaLdOcmCardPortsSectionLoc_Type.__name__=_D
_OaLdOcmCardPortsSectionLoc_Object=MibTableColumn
oaLdOcmCardPortsSectionLoc=_OaLdOcmCardPortsSectionLoc_Object((1,3,6,1,4,1,6926,1,41,13,2,1,5),_OaLdOcmCardPortsSectionLoc_Type())
oaLdOcmCardPortsSectionLoc.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdOcmCardPortsSectionLoc.setStatus(_A)
_OaLdOcmCardPortsSectionB1_Type=Counter32
_OaLdOcmCardPortsSectionB1_Object=MibTableColumn
oaLdOcmCardPortsSectionB1=_OaLdOcmCardPortsSectionB1_Object((1,3,6,1,4,1,6926,1,41,13,2,1,6),_OaLdOcmCardPortsSectionB1_Type())
oaLdOcmCardPortsSectionB1.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdOcmCardPortsSectionB1.setStatus(_A)
class _OaLdOcmCardPortsLineAis_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_T,2),(_L,3),(_M,4)))
_OaLdOcmCardPortsLineAis_Type.__name__=_D
_OaLdOcmCardPortsLineAis_Object=MibTableColumn
oaLdOcmCardPortsLineAis=_OaLdOcmCardPortsLineAis_Object((1,3,6,1,4,1,6926,1,41,13,2,1,7),_OaLdOcmCardPortsLineAis_Type())
oaLdOcmCardPortsLineAis.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdOcmCardPortsLineAis.setStatus(_A)
class _OaLdOcmCardPortsLineRdi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_T,2),(_L,3),(_M,4)))
_OaLdOcmCardPortsLineRdi_Type.__name__=_D
_OaLdOcmCardPortsLineRdi_Object=MibTableColumn
oaLdOcmCardPortsLineRdi=_OaLdOcmCardPortsLineRdi_Object((1,3,6,1,4,1,6926,1,41,13,2,1,8),_OaLdOcmCardPortsLineRdi_Type())
oaLdOcmCardPortsLineRdi.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdOcmCardPortsLineRdi.setStatus(_A)
_OaLdOcmCardPortsLineB2_Type=Counter32
_OaLdOcmCardPortsLineB2_Object=MibTableColumn
oaLdOcmCardPortsLineB2=_OaLdOcmCardPortsLineB2_Object((1,3,6,1,4,1,6926,1,41,13,2,1,9),_OaLdOcmCardPortsLineB2_Type())
oaLdOcmCardPortsLineB2.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdOcmCardPortsLineB2.setStatus(_A)
_OaLdOcmCardPortsLineFebe_Type=Counter32
_OaLdOcmCardPortsLineFebe_Object=MibTableColumn
oaLdOcmCardPortsLineFebe=_OaLdOcmCardPortsLineFebe_Object((1,3,6,1,4,1,6926,1,41,13,2,1,10),_OaLdOcmCardPortsLineFebe_Type())
oaLdOcmCardPortsLineFebe.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdOcmCardPortsLineFebe.setStatus(_A)
class _OaLdOcmCardPortsPathAis_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_T,2),(_L,3),(_M,4)))
_OaLdOcmCardPortsPathAis_Type.__name__=_D
_OaLdOcmCardPortsPathAis_Object=MibTableColumn
oaLdOcmCardPortsPathAis=_OaLdOcmCardPortsPathAis_Object((1,3,6,1,4,1,6926,1,41,13,2,1,11),_OaLdOcmCardPortsPathAis_Type())
oaLdOcmCardPortsPathAis.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdOcmCardPortsPathAis.setStatus(_A)
class _OaLdOcmCardPortsPathLop_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_T,2),(_L,3),(_M,4)))
_OaLdOcmCardPortsPathLop_Type.__name__=_D
_OaLdOcmCardPortsPathLop_Object=MibTableColumn
oaLdOcmCardPortsPathLop=_OaLdOcmCardPortsPathLop_Object((1,3,6,1,4,1,6926,1,41,13,2,1,12),_OaLdOcmCardPortsPathLop_Type())
oaLdOcmCardPortsPathLop.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdOcmCardPortsPathLop.setStatus(_A)
_OaLdOcmCardPortsPathB3_Type=Counter32
_OaLdOcmCardPortsPathB3_Object=MibTableColumn
oaLdOcmCardPortsPathB3=_OaLdOcmCardPortsPathB3_Object((1,3,6,1,4,1,6926,1,41,13,2,1,13),_OaLdOcmCardPortsPathB3_Type())
oaLdOcmCardPortsPathB3.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdOcmCardPortsPathB3.setStatus(_A)
_OaLdOcmCardPortsPathPse_Type=Counter32
_OaLdOcmCardPortsPathPse_Object=MibTableColumn
oaLdOcmCardPortsPathPse=_OaLdOcmCardPortsPathPse_Object((1,3,6,1,4,1,6926,1,41,13,2,1,14),_OaLdOcmCardPortsPathPse_Type())
oaLdOcmCardPortsPathPse.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdOcmCardPortsPathPse.setStatus(_A)
_OaLdOcmCardPortsPathNse_Type=Counter32
_OaLdOcmCardPortsPathNse_Object=MibTableColumn
oaLdOcmCardPortsPathNse=_OaLdOcmCardPortsPathNse_Object((1,3,6,1,4,1,6926,1,41,13,2,1,15),_OaLdOcmCardPortsPathNse_Type())
oaLdOcmCardPortsPathNse.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdOcmCardPortsPathNse.setStatus(_A)
_OaLdRoadmInfo_ObjectIdentity=ObjectIdentity
oaLdRoadmInfo=_OaLdRoadmInfo_ObjectIdentity((1,3,6,1,4,1,6926,1,41,15))
_OaLdRoadmInfoTable_Object=MibTable
oaLdRoadmInfoTable=_OaLdRoadmInfoTable_Object((1,3,6,1,4,1,6926,1,41,15,2))
if mibBuilder.loadTexts:oaLdRoadmInfoTable.setStatus(_A)
_OaLdRoadmInfoEntry_Object=MibTableRow
oaLdRoadmInfoEntry=_OaLdRoadmInfoEntry_Object((1,3,6,1,4,1,6926,1,41,15,2,1))
oaLdRoadmInfoEntry.setIndexNames((0,_C,_AI))
if mibBuilder.loadTexts:oaLdRoadmInfoEntry.setStatus(_A)
_OaLdRoadmSlotNumber_Type=Integer32
_OaLdRoadmSlotNumber_Object=MibTableColumn
oaLdRoadmSlotNumber=_OaLdRoadmSlotNumber_Object((1,3,6,1,4,1,6926,1,41,15,2,1,1),_OaLdRoadmSlotNumber_Type())
oaLdRoadmSlotNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdRoadmSlotNumber.setStatus(_A)
_OaLdRoadmType_Type=Integer32
_OaLdRoadmType_Object=MibTableColumn
oaLdRoadmType=_OaLdRoadmType_Object((1,3,6,1,4,1,6926,1,41,15,2,1,2),_OaLdRoadmType_Type())
oaLdRoadmType.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdRoadmType.setStatus(_A)
class _OaLdRoadmDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_OaLdRoadmDescription_Type.__name__=_J
_OaLdRoadmDescription_Object=MibTableColumn
oaLdRoadmDescription=_OaLdRoadmDescription_Object((1,3,6,1,4,1,6926,1,41,15,2,1,3),_OaLdRoadmDescription_Type())
oaLdRoadmDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdRoadmDescription.setStatus(_A)
class _OaLdRoadmSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_OaLdRoadmSerialNumber_Type.__name__=_J
_OaLdRoadmSerialNumber_Object=MibTableColumn
oaLdRoadmSerialNumber=_OaLdRoadmSerialNumber_Object((1,3,6,1,4,1,6926,1,41,15,2,1,4),_OaLdRoadmSerialNumber_Type())
oaLdRoadmSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdRoadmSerialNumber.setStatus(_A)
class _OaLdRoadmBoardVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_OaLdRoadmBoardVersion_Type.__name__=_J
_OaLdRoadmBoardVersion_Object=MibTableColumn
oaLdRoadmBoardVersion=_OaLdRoadmBoardVersion_Object((1,3,6,1,4,1,6926,1,41,15,2,1,5),_OaLdRoadmBoardVersion_Type())
oaLdRoadmBoardVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdRoadmBoardVersion.setStatus(_A)
class _OaLdRoadmFpgaVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_OaLdRoadmFpgaVersion_Type.__name__=_J
_OaLdRoadmFpgaVersion_Object=MibTableColumn
oaLdRoadmFpgaVersion=_OaLdRoadmFpgaVersion_Object((1,3,6,1,4,1,6926,1,41,15,2,1,6),_OaLdRoadmFpgaVersion_Type())
oaLdRoadmFpgaVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdRoadmFpgaVersion.setStatus(_A)
class _OaLdRoadmBootVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_OaLdRoadmBootVersion_Type.__name__=_J
_OaLdRoadmBootVersion_Object=MibTableColumn
oaLdRoadmBootVersion=_OaLdRoadmBootVersion_Object((1,3,6,1,4,1,6926,1,41,15,2,1,7),_OaLdRoadmBootVersion_Type())
oaLdRoadmBootVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdRoadmBootVersion.setStatus(_A)
class _OaLdRoadmMcVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_OaLdRoadmMcVersion_Type.__name__=_J
_OaLdRoadmMcVersion_Object=MibTableColumn
oaLdRoadmMcVersion=_OaLdRoadmMcVersion_Object((1,3,6,1,4,1,6926,1,41,15,2,1,8),_OaLdRoadmMcVersion_Type())
oaLdRoadmMcVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdRoadmMcVersion.setStatus(_A)
class _OaLdRoadmDate_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_OaLdRoadmDate_Type.__name__=_J
_OaLdRoadmDate_Object=MibTableColumn
oaLdRoadmDate=_OaLdRoadmDate_Object((1,3,6,1,4,1,6926,1,41,15,2,1,9),_OaLdRoadmDate_Type())
oaLdRoadmDate.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdRoadmDate.setStatus(_A)
class _OaLdRoadmStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),('initInProgress',2),(_AJ,3)))
_OaLdRoadmStatus_Type.__name__=_D
_OaLdRoadmStatus_Object=MibTableColumn
oaLdRoadmStatus=_OaLdRoadmStatus_Object((1,3,6,1,4,1,6926,1,41,15,2,1,15),_OaLdRoadmStatus_Type())
oaLdRoadmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdRoadmStatus.setStatus(_A)
class _OaLdRoadmComOutPortAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_S,2),(_K,3)))
_OaLdRoadmComOutPortAdminStatus_Type.__name__=_D
_OaLdRoadmComOutPortAdminStatus_Object=MibTableColumn
oaLdRoadmComOutPortAdminStatus=_OaLdRoadmComOutPortAdminStatus_Object((1,3,6,1,4,1,6926,1,41,15,2,1,16),_OaLdRoadmComOutPortAdminStatus_Type())
oaLdRoadmComOutPortAdminStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:oaLdRoadmComOutPortAdminStatus.setStatus(_A)
class _OaLdRoadmFail_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_a,2),(_Z,3)))
_OaLdRoadmFail_Type.__name__=_D
_OaLdRoadmFail_Object=MibTableColumn
oaLdRoadmFail=_OaLdRoadmFail_Object((1,3,6,1,4,1,6926,1,41,15,2,1,17),_OaLdRoadmFail_Type())
oaLdRoadmFail.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdRoadmFail.setStatus(_A)
_OaLdRoadmTemperature_Type=Integer32
_OaLdRoadmTemperature_Object=MibTableColumn
oaLdRoadmTemperature=_OaLdRoadmTemperature_Object((1,3,6,1,4,1,6926,1,41,15,2,1,18),_OaLdRoadmTemperature_Type())
oaLdRoadmTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdRoadmTemperature.setStatus(_A)
class _OaLdRoadmHeaterMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_AJ,2),(_K,3)))
_OaLdRoadmHeaterMode_Type.__name__=_D
_OaLdRoadmHeaterMode_Object=MibTableColumn
oaLdRoadmHeaterMode=_OaLdRoadmHeaterMode_Object((1,3,6,1,4,1,6926,1,41,15,2,1,19),_OaLdRoadmHeaterMode_Type())
oaLdRoadmHeaterMode.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdRoadmHeaterMode.setStatus(_A)
_OaLdRoadmHeaterTemperature_Type=Integer32
_OaLdRoadmHeaterTemperature_Object=MibTableColumn
oaLdRoadmHeaterTemperature=_OaLdRoadmHeaterTemperature_Object((1,3,6,1,4,1,6926,1,41,15,2,1,20),_OaLdRoadmHeaterTemperature_Type())
oaLdRoadmHeaterTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdRoadmHeaterTemperature.setStatus(_A)
class _OaLdRoadmSpacing_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),('s100',2),('s50',3)))
_OaLdRoadmSpacing_Type.__name__=_D
_OaLdRoadmSpacing_Object=MibTableColumn
oaLdRoadmSpacing=_OaLdRoadmSpacing_Object((1,3,6,1,4,1,6926,1,41,15,2,1,21),_OaLdRoadmSpacing_Type())
oaLdRoadmSpacing.setMaxAccess(_F)
if mibBuilder.loadTexts:oaLdRoadmSpacing.setStatus(_A)
_OaLdRoadmNumberOfChPorts_Type=Integer32
_OaLdRoadmNumberOfChPorts_Object=MibTableColumn
oaLdRoadmNumberOfChPorts=_OaLdRoadmNumberOfChPorts_Object((1,3,6,1,4,1,6926,1,41,15,2,1,22),_OaLdRoadmNumberOfChPorts_Type())
oaLdRoadmNumberOfChPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdRoadmNumberOfChPorts.setStatus(_A)
class _OaLdRoadmPowerEqualization_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_f,1),('equalization',2)))
_OaLdRoadmPowerEqualization_Type.__name__=_D
_OaLdRoadmPowerEqualization_Object=MibTableColumn
oaLdRoadmPowerEqualization=_OaLdRoadmPowerEqualization_Object((1,3,6,1,4,1,6926,1,41,15,2,1,23),_OaLdRoadmPowerEqualization_Type())
oaLdRoadmPowerEqualization.setMaxAccess(_F)
if mibBuilder.loadTexts:oaLdRoadmPowerEqualization.setStatus(_A)
_OaLdRoadmZone2Temperature_Type=Integer32
_OaLdRoadmZone2Temperature_Object=MibTableColumn
oaLdRoadmZone2Temperature=_OaLdRoadmZone2Temperature_Object((1,3,6,1,4,1,6926,1,41,15,2,1,24),_OaLdRoadmZone2Temperature_Type())
oaLdRoadmZone2Temperature.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdRoadmZone2Temperature.setStatus(_A)
_OaLdRoadmZone3Temperature_Type=Integer32
_OaLdRoadmZone3Temperature_Object=MibTableColumn
oaLdRoadmZone3Temperature=_OaLdRoadmZone3Temperature_Object((1,3,6,1,4,1,6926,1,41,15,2,1,25),_OaLdRoadmZone3Temperature_Type())
oaLdRoadmZone3Temperature.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdRoadmZone3Temperature.setStatus(_A)
_OaLdRoadmNumberOfChannels_Type=Integer32
_OaLdRoadmNumberOfChannels_Object=MibTableColumn
oaLdRoadmNumberOfChannels=_OaLdRoadmNumberOfChannels_Object((1,3,6,1,4,1,6926,1,41,15,2,1,26),_OaLdRoadmNumberOfChannels_Type())
oaLdRoadmNumberOfChannels.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdRoadmNumberOfChannels.setStatus(_A)
class _OaLdRoadmReconfigureSwitch_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_f,2),('reconfigure',3)))
_OaLdRoadmReconfigureSwitch_Type.__name__=_D
_OaLdRoadmReconfigureSwitch_Object=MibTableColumn
oaLdRoadmReconfigureSwitch=_OaLdRoadmReconfigureSwitch_Object((1,3,6,1,4,1,6926,1,41,15,2,1,27),_OaLdRoadmReconfigureSwitch_Type())
oaLdRoadmReconfigureSwitch.setMaxAccess(_F)
if mibBuilder.loadTexts:oaLdRoadmReconfigureSwitch.setStatus(_A)
_OaLdRoadmFirstChannel_Type=Integer32
_OaLdRoadmFirstChannel_Object=MibTableColumn
oaLdRoadmFirstChannel=_OaLdRoadmFirstChannel_Object((1,3,6,1,4,1,6926,1,41,15,2,1,28),_OaLdRoadmFirstChannel_Type())
oaLdRoadmFirstChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdRoadmFirstChannel.setStatus(_A)
_OaLdRoadmLastChannel_Type=Integer32
_OaLdRoadmLastChannel_Object=MibTableColumn
oaLdRoadmLastChannel=_OaLdRoadmLastChannel_Object((1,3,6,1,4,1,6926,1,41,15,2,1,29),_OaLdRoadmLastChannel_Type())
oaLdRoadmLastChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdRoadmLastChannel.setStatus(_A)
class _OaLdRoadmDefaultConfiguration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_f,2),('restoreDefault',3)))
_OaLdRoadmDefaultConfiguration_Type.__name__=_D
_OaLdRoadmDefaultConfiguration_Object=MibTableColumn
oaLdRoadmDefaultConfiguration=_OaLdRoadmDefaultConfiguration_Object((1,3,6,1,4,1,6926,1,41,15,2,1,30),_OaLdRoadmDefaultConfiguration_Type())
oaLdRoadmDefaultConfiguration.setMaxAccess(_F)
if mibBuilder.loadTexts:oaLdRoadmDefaultConfiguration.setStatus(_A)
class _OaLdRoadmPowerBalancingMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_c,2),(_A7,3)))
_OaLdRoadmPowerBalancingMode_Type.__name__=_D
_OaLdRoadmPowerBalancingMode_Object=MibTableColumn
oaLdRoadmPowerBalancingMode=_OaLdRoadmPowerBalancingMode_Object((1,3,6,1,4,1,6926,1,41,15,2,1,31),_OaLdRoadmPowerBalancingMode_Type())
oaLdRoadmPowerBalancingMode.setMaxAccess(_F)
if mibBuilder.loadTexts:oaLdRoadmPowerBalancingMode.setStatus(_A)
_OaLdRoadmMonitorTable_Object=MibTable
oaLdRoadmMonitorTable=_OaLdRoadmMonitorTable_Object((1,3,6,1,4,1,6926,1,41,15,3))
if mibBuilder.loadTexts:oaLdRoadmMonitorTable.setStatus(_A)
_OaLdRoadmMonitorEntry_Object=MibTableRow
oaLdRoadmMonitorEntry=_OaLdRoadmMonitorEntry_Object((1,3,6,1,4,1,6926,1,41,15,3,1))
oaLdRoadmMonitorEntry.setIndexNames((0,_C,_AK))
if mibBuilder.loadTexts:oaLdRoadmMonitorEntry.setStatus(_A)
_OaLdRoadmMonitorSlotNumber_Type=Integer32
_OaLdRoadmMonitorSlotNumber_Object=MibTableColumn
oaLdRoadmMonitorSlotNumber=_OaLdRoadmMonitorSlotNumber_Object((1,3,6,1,4,1,6926,1,41,15,3,1,1),_OaLdRoadmMonitorSlotNumber_Type())
oaLdRoadmMonitorSlotNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdRoadmMonitorSlotNumber.setStatus(_A)
_OaLdRoadmMonitorComInputPower_Type=Integer32
_OaLdRoadmMonitorComInputPower_Object=MibTableColumn
oaLdRoadmMonitorComInputPower=_OaLdRoadmMonitorComInputPower_Object((1,3,6,1,4,1,6926,1,41,15,3,1,2),_OaLdRoadmMonitorComInputPower_Type())
oaLdRoadmMonitorComInputPower.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdRoadmMonitorComInputPower.setStatus(_A)
_OaLdRoadmMonitorComOutputPower_Type=Integer32
_OaLdRoadmMonitorComOutputPower_Object=MibTableColumn
oaLdRoadmMonitorComOutputPower=_OaLdRoadmMonitorComOutputPower_Object((1,3,6,1,4,1,6926,1,41,15,3,1,3),_OaLdRoadmMonitorComOutputPower_Type())
oaLdRoadmMonitorComOutputPower.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdRoadmMonitorComOutputPower.setStatus(_A)
_OaLdRoadmMonitorExpInputPower_Type=Integer32
_OaLdRoadmMonitorExpInputPower_Object=MibTableColumn
oaLdRoadmMonitorExpInputPower=_OaLdRoadmMonitorExpInputPower_Object((1,3,6,1,4,1,6926,1,41,15,3,1,4),_OaLdRoadmMonitorExpInputPower_Type())
oaLdRoadmMonitorExpInputPower.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdRoadmMonitorExpInputPower.setStatus(_A)
_OaLdRoadmMonitorExpOutputPower_Type=Integer32
_OaLdRoadmMonitorExpOutputPower_Object=MibTableColumn
oaLdRoadmMonitorExpOutputPower=_OaLdRoadmMonitorExpOutputPower_Object((1,3,6,1,4,1,6926,1,41,15,3,1,5),_OaLdRoadmMonitorExpOutputPower_Type())
oaLdRoadmMonitorExpOutputPower.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdRoadmMonitorExpOutputPower.setStatus(_A)
_OaLdRoadmMonitorDropOutputPower_Type=Integer32
_OaLdRoadmMonitorDropOutputPower_Object=MibTableColumn
oaLdRoadmMonitorDropOutputPower=_OaLdRoadmMonitorDropOutputPower_Object((1,3,6,1,4,1,6926,1,41,15,3,1,6),_OaLdRoadmMonitorDropOutputPower_Type())
oaLdRoadmMonitorDropOutputPower.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdRoadmMonitorDropOutputPower.setStatus(_A)
_OaLdRoadmChannelTable_Object=MibTable
oaLdRoadmChannelTable=_OaLdRoadmChannelTable_Object((1,3,6,1,4,1,6926,1,41,15,4))
if mibBuilder.loadTexts:oaLdRoadmChannelTable.setStatus(_A)
_OaLdRoadmChannelEntry_Object=MibTableRow
oaLdRoadmChannelEntry=_OaLdRoadmChannelEntry_Object((1,3,6,1,4,1,6926,1,41,15,4,1))
oaLdRoadmChannelEntry.setIndexNames((0,_C,_AL),(0,_C,_AM),(0,_C,_AN))
if mibBuilder.loadTexts:oaLdRoadmChannelEntry.setStatus(_A)
_OaLdRoadmChannelSlotNumber_Type=Integer32
_OaLdRoadmChannelSlotNumber_Object=MibTableColumn
oaLdRoadmChannelSlotNumber=_OaLdRoadmChannelSlotNumber_Object((1,3,6,1,4,1,6926,1,41,15,4,1,1),_OaLdRoadmChannelSlotNumber_Type())
oaLdRoadmChannelSlotNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdRoadmChannelSlotNumber.setStatus(_A)
_OaLdRoadmChannelLambdaChannel_Type=Integer32
_OaLdRoadmChannelLambdaChannel_Object=MibTableColumn
oaLdRoadmChannelLambdaChannel=_OaLdRoadmChannelLambdaChannel_Object((1,3,6,1,4,1,6926,1,41,15,4,1,2),_OaLdRoadmChannelLambdaChannel_Type())
oaLdRoadmChannelLambdaChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdRoadmChannelLambdaChannel.setStatus(_A)
_OaLdRoadmChannelPortNumber_Type=Integer32
_OaLdRoadmChannelPortNumber_Object=MibTableColumn
oaLdRoadmChannelPortNumber=_OaLdRoadmChannelPortNumber_Object((1,3,6,1,4,1,6926,1,41,15,4,1,3),_OaLdRoadmChannelPortNumber_Type())
oaLdRoadmChannelPortNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdRoadmChannelPortNumber.setStatus(_A)
_OaLdRoadmChannelWavelength_Type=Integer32
_OaLdRoadmChannelWavelength_Object=MibTableColumn
oaLdRoadmChannelWavelength=_OaLdRoadmChannelWavelength_Object((1,3,6,1,4,1,6926,1,41,15,4,1,4),_OaLdRoadmChannelWavelength_Type())
oaLdRoadmChannelWavelength.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdRoadmChannelWavelength.setStatus(_A)
_OaLdRoadmChannelDropPortNumber_Type=Integer32
_OaLdRoadmChannelDropPortNumber_Object=MibTableColumn
oaLdRoadmChannelDropPortNumber=_OaLdRoadmChannelDropPortNumber_Object((1,3,6,1,4,1,6926,1,41,15,4,1,5),_OaLdRoadmChannelDropPortNumber_Type())
oaLdRoadmChannelDropPortNumber.setMaxAccess(_F)
if mibBuilder.loadTexts:oaLdRoadmChannelDropPortNumber.setStatus(_A)
_OaLdRoadmChannelDropAttenuation_Type=Integer32
_OaLdRoadmChannelDropAttenuation_Object=MibTableColumn
oaLdRoadmChannelDropAttenuation=_OaLdRoadmChannelDropAttenuation_Object((1,3,6,1,4,1,6926,1,41,15,4,1,6),_OaLdRoadmChannelDropAttenuation_Type())
oaLdRoadmChannelDropAttenuation.setMaxAccess(_F)
if mibBuilder.loadTexts:oaLdRoadmChannelDropAttenuation.setStatus(_A)
class _OaLdRoadmChannelConfigStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),('virtual',2),('saved',3)))
_OaLdRoadmChannelConfigStatus_Type.__name__=_D
_OaLdRoadmChannelConfigStatus_Object=MibTableColumn
oaLdRoadmChannelConfigStatus=_OaLdRoadmChannelConfigStatus_Object((1,3,6,1,4,1,6926,1,41,15,4,1,7),_OaLdRoadmChannelConfigStatus_Type())
oaLdRoadmChannelConfigStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdRoadmChannelConfigStatus.setStatus(_A)
_OaLdRoadmChannelPower1_Type=Integer32
_OaLdRoadmChannelPower1_Object=MibTableColumn
oaLdRoadmChannelPower1=_OaLdRoadmChannelPower1_Object((1,3,6,1,4,1,6926,1,41,15,4,1,8),_OaLdRoadmChannelPower1_Type())
oaLdRoadmChannelPower1.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdRoadmChannelPower1.setStatus(_A)
_OaLdRoadmChannelPower2_Type=Integer32
_OaLdRoadmChannelPower2_Object=MibTableColumn
oaLdRoadmChannelPower2=_OaLdRoadmChannelPower2_Object((1,3,6,1,4,1,6926,1,41,15,4,1,9),_OaLdRoadmChannelPower2_Type())
oaLdRoadmChannelPower2.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdRoadmChannelPower2.setStatus(_A)
_OaLdRoadmChannelDropPeakFrequency_Type=Integer32
_OaLdRoadmChannelDropPeakFrequency_Object=MibTableColumn
oaLdRoadmChannelDropPeakFrequency=_OaLdRoadmChannelDropPeakFrequency_Object((1,3,6,1,4,1,6926,1,41,15,4,1,10),_OaLdRoadmChannelDropPeakFrequency_Type())
oaLdRoadmChannelDropPeakFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdRoadmChannelDropPeakFrequency.setStatus(_A)
_OaLdRoadmChannelAddPeakFrequency_Type=Integer32
_OaLdRoadmChannelAddPeakFrequency_Object=MibTableColumn
oaLdRoadmChannelAddPeakFrequency=_OaLdRoadmChannelAddPeakFrequency_Object((1,3,6,1,4,1,6926,1,41,15,4,1,11),_OaLdRoadmChannelAddPeakFrequency_Type())
oaLdRoadmChannelAddPeakFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdRoadmChannelAddPeakFrequency.setStatus(_A)
_OaLdRoadmChannelAddAttenuation_Type=Integer32
_OaLdRoadmChannelAddAttenuation_Object=MibTableColumn
oaLdRoadmChannelAddAttenuation=_OaLdRoadmChannelAddAttenuation_Object((1,3,6,1,4,1,6926,1,41,15,4,1,12),_OaLdRoadmChannelAddAttenuation_Type())
oaLdRoadmChannelAddAttenuation.setMaxAccess(_F)
if mibBuilder.loadTexts:oaLdRoadmChannelAddAttenuation.setStatus(_A)
_OaLdRoadmChannelGridFrequency_Type=Integer32
_OaLdRoadmChannelGridFrequency_Object=MibTableColumn
oaLdRoadmChannelGridFrequency=_OaLdRoadmChannelGridFrequency_Object((1,3,6,1,4,1,6926,1,41,15,4,1,13),_OaLdRoadmChannelGridFrequency_Type())
oaLdRoadmChannelGridFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdRoadmChannelGridFrequency.setStatus(_A)
class _OaLdRoadmChannelSpacing_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),('s100',2),('s50',3)))
_OaLdRoadmChannelSpacing_Type.__name__=_D
_OaLdRoadmChannelSpacing_Object=MibTableColumn
oaLdRoadmChannelSpacing=_OaLdRoadmChannelSpacing_Object((1,3,6,1,4,1,6926,1,41,15,4,1,14),_OaLdRoadmChannelSpacing_Type())
oaLdRoadmChannelSpacing.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdRoadmChannelSpacing.setStatus(_A)
_OaLdRoadmThresholdTable_Object=MibTable
oaLdRoadmThresholdTable=_OaLdRoadmThresholdTable_Object((1,3,6,1,4,1,6926,1,41,15,5))
if mibBuilder.loadTexts:oaLdRoadmThresholdTable.setStatus(_A)
_OaLdRoadmThresholdEntry_Object=MibTableRow
oaLdRoadmThresholdEntry=_OaLdRoadmThresholdEntry_Object((1,3,6,1,4,1,6926,1,41,15,5,1))
oaLdRoadmThresholdEntry.setIndexNames((0,_C,_AO),(0,_C,_AP))
if mibBuilder.loadTexts:oaLdRoadmThresholdEntry.setStatus(_A)
_OaLdRoadmThresholdSlotNumber_Type=Integer32
_OaLdRoadmThresholdSlotNumber_Object=MibTableColumn
oaLdRoadmThresholdSlotNumber=_OaLdRoadmThresholdSlotNumber_Object((1,3,6,1,4,1,6926,1,41,15,5,1,1),_OaLdRoadmThresholdSlotNumber_Type())
oaLdRoadmThresholdSlotNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdRoadmThresholdSlotNumber.setStatus(_A)
class _OaLdRoadmThresholdIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_AQ,1),(_AR,2),('failLow',3),('failHigh',4),(_AS,5),(_AT,6),(_AU,7),(_AV,8),('tRaise',9),('tFall',10)))
_OaLdRoadmThresholdIndex_Type.__name__=_D
_OaLdRoadmThresholdIndex_Object=MibTableColumn
oaLdRoadmThresholdIndex=_OaLdRoadmThresholdIndex_Object((1,3,6,1,4,1,6926,1,41,15,5,1,2),_OaLdRoadmThresholdIndex_Type())
oaLdRoadmThresholdIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdRoadmThresholdIndex.setStatus(_A)
_OaLdRoadmThresholdAwgTemp_Type=Integer32
_OaLdRoadmThresholdAwgTemp_Object=MibTableColumn
oaLdRoadmThresholdAwgTemp=_OaLdRoadmThresholdAwgTemp_Object((1,3,6,1,4,1,6926,1,41,15,5,1,3),_OaLdRoadmThresholdAwgTemp_Type())
oaLdRoadmThresholdAwgTemp.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdRoadmThresholdAwgTemp.setStatus(_A)
_OaLdRoadmThresholdTemp_Type=Integer32
_OaLdRoadmThresholdTemp_Object=MibTableColumn
oaLdRoadmThresholdTemp=_OaLdRoadmThresholdTemp_Object((1,3,6,1,4,1,6926,1,41,15,5,1,4),_OaLdRoadmThresholdTemp_Type())
oaLdRoadmThresholdTemp.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdRoadmThresholdTemp.setStatus(_A)
_OaLdRoadmThresholdComInputPwr_Type=Integer32
_OaLdRoadmThresholdComInputPwr_Object=MibTableColumn
oaLdRoadmThresholdComInputPwr=_OaLdRoadmThresholdComInputPwr_Object((1,3,6,1,4,1,6926,1,41,15,5,1,5),_OaLdRoadmThresholdComInputPwr_Type())
oaLdRoadmThresholdComInputPwr.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdRoadmThresholdComInputPwr.setStatus(_A)
_OaLdRoadmThresholdComOutputPwr_Type=Integer32
_OaLdRoadmThresholdComOutputPwr_Object=MibTableColumn
oaLdRoadmThresholdComOutputPwr=_OaLdRoadmThresholdComOutputPwr_Object((1,3,6,1,4,1,6926,1,41,15,5,1,6),_OaLdRoadmThresholdComOutputPwr_Type())
oaLdRoadmThresholdComOutputPwr.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdRoadmThresholdComOutputPwr.setStatus(_A)
_OaLdRoadmThresholdExpInputPwr_Type=Integer32
_OaLdRoadmThresholdExpInputPwr_Object=MibTableColumn
oaLdRoadmThresholdExpInputPwr=_OaLdRoadmThresholdExpInputPwr_Object((1,3,6,1,4,1,6926,1,41,15,5,1,7),_OaLdRoadmThresholdExpInputPwr_Type())
oaLdRoadmThresholdExpInputPwr.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdRoadmThresholdExpInputPwr.setStatus(_A)
_OaLdRoadmThresholdExpOutputPwr_Type=Integer32
_OaLdRoadmThresholdExpOutputPwr_Object=MibTableColumn
oaLdRoadmThresholdExpOutputPwr=_OaLdRoadmThresholdExpOutputPwr_Object((1,3,6,1,4,1,6926,1,41,15,5,1,8),_OaLdRoadmThresholdExpOutputPwr_Type())
oaLdRoadmThresholdExpOutputPwr.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdRoadmThresholdExpOutputPwr.setStatus(_A)
_OaLdRoadmThresholdDropOutputPwr_Type=Integer32
_OaLdRoadmThresholdDropOutputPwr_Object=MibTableColumn
oaLdRoadmThresholdDropOutputPwr=_OaLdRoadmThresholdDropOutputPwr_Object((1,3,6,1,4,1,6926,1,41,15,5,1,9),_OaLdRoadmThresholdDropOutputPwr_Type())
oaLdRoadmThresholdDropOutputPwr.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdRoadmThresholdDropOutputPwr.setStatus(_A)
_OaLdRoadmPortInfoTable_Object=MibTable
oaLdRoadmPortInfoTable=_OaLdRoadmPortInfoTable_Object((1,3,6,1,4,1,6926,1,41,15,6))
if mibBuilder.loadTexts:oaLdRoadmPortInfoTable.setStatus(_A)
_OaLdRoadmPortInfoEntry_Object=MibTableRow
oaLdRoadmPortInfoEntry=_OaLdRoadmPortInfoEntry_Object((1,3,6,1,4,1,6926,1,41,15,6,1))
oaLdRoadmPortInfoEntry.setIndexNames((0,_C,_AW),(0,_C,_AX))
if mibBuilder.loadTexts:oaLdRoadmPortInfoEntry.setStatus(_A)
_OaLdRoadmPortSlotNumber_Type=Integer32
_OaLdRoadmPortSlotNumber_Object=MibTableColumn
oaLdRoadmPortSlotNumber=_OaLdRoadmPortSlotNumber_Object((1,3,6,1,4,1,6926,1,41,15,6,1,1),_OaLdRoadmPortSlotNumber_Type())
oaLdRoadmPortSlotNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdRoadmPortSlotNumber.setStatus(_A)
_OaLdRoadmPortPortNumber_Type=Integer32
_OaLdRoadmPortPortNumber_Object=MibTableColumn
oaLdRoadmPortPortNumber=_OaLdRoadmPortPortNumber_Object((1,3,6,1,4,1,6926,1,41,15,6,1,2),_OaLdRoadmPortPortNumber_Type())
oaLdRoadmPortPortNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdRoadmPortPortNumber.setStatus(_A)
class _OaLdRoadmPortAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_E,1),(_p,2),('pass',3),('dark',4),(_q,5)))
_OaLdRoadmPortAdminState_Type.__name__=_D
_OaLdRoadmPortAdminState_Object=MibTableColumn
oaLdRoadmPortAdminState=_OaLdRoadmPortAdminState_Object((1,3,6,1,4,1,6926,1,41,15,6,1,3),_OaLdRoadmPortAdminState_Type())
oaLdRoadmPortAdminState.setMaxAccess(_F)
if mibBuilder.loadTexts:oaLdRoadmPortAdminState.setStatus(_A)
class _OaLdRoadmPortServiceState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_E,1),(_p,2),('pass',3),('dark',4),(_q,5)))
_OaLdRoadmPortServiceState_Type.__name__=_D
_OaLdRoadmPortServiceState_Object=MibTableColumn
oaLdRoadmPortServiceState=_OaLdRoadmPortServiceState_Object((1,3,6,1,4,1,6926,1,41,15,6,1,4),_OaLdRoadmPortServiceState_Type())
oaLdRoadmPortServiceState.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdRoadmPortServiceState.setStatus(_A)
_OaLdRoadmPortPower_Type=Integer32
_OaLdRoadmPortPower_Object=MibTableColumn
oaLdRoadmPortPower=_OaLdRoadmPortPower_Object((1,3,6,1,4,1,6926,1,41,15,6,1,5),_OaLdRoadmPortPower_Type())
oaLdRoadmPortPower.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdRoadmPortPower.setStatus(_A)
_OaLdRoadmPortVoaAttenuationAdd_Type=Integer32
_OaLdRoadmPortVoaAttenuationAdd_Object=MibTableColumn
oaLdRoadmPortVoaAttenuationAdd=_OaLdRoadmPortVoaAttenuationAdd_Object((1,3,6,1,4,1,6926,1,41,15,6,1,7),_OaLdRoadmPortVoaAttenuationAdd_Type())
oaLdRoadmPortVoaAttenuationAdd.setMaxAccess(_F)
if mibBuilder.loadTexts:oaLdRoadmPortVoaAttenuationAdd.setStatus(_A)
_OaLdRoadmPortVoaAttenuationPass_Type=Integer32
_OaLdRoadmPortVoaAttenuationPass_Object=MibTableColumn
oaLdRoadmPortVoaAttenuationPass=_OaLdRoadmPortVoaAttenuationPass_Object((1,3,6,1,4,1,6926,1,41,15,6,1,8),_OaLdRoadmPortVoaAttenuationPass_Type())
oaLdRoadmPortVoaAttenuationPass.setMaxAccess(_F)
if mibBuilder.loadTexts:oaLdRoadmPortVoaAttenuationPass.setStatus(_A)
_OaLdRoadmPortVoaAttenuationDrop_Type=Integer32
_OaLdRoadmPortVoaAttenuationDrop_Object=MibTableColumn
oaLdRoadmPortVoaAttenuationDrop=_OaLdRoadmPortVoaAttenuationDrop_Object((1,3,6,1,4,1,6926,1,41,15,6,1,9),_OaLdRoadmPortVoaAttenuationDrop_Type())
oaLdRoadmPortVoaAttenuationDrop.setMaxAccess(_F)
if mibBuilder.loadTexts:oaLdRoadmPortVoaAttenuationDrop.setStatus(_A)
_OaLdRoadmPortChannelWavelength_Type=Integer32
_OaLdRoadmPortChannelWavelength_Object=MibTableColumn
oaLdRoadmPortChannelWavelength=_OaLdRoadmPortChannelWavelength_Object((1,3,6,1,4,1,6926,1,41,15,6,1,10),_OaLdRoadmPortChannelWavelength_Type())
oaLdRoadmPortChannelWavelength.setMaxAccess(_F)
if mibBuilder.loadTexts:oaLdRoadmPortChannelWavelength.setStatus(_A)
_OaLdRoadmPortLambdaChannel_Type=Integer32
_OaLdRoadmPortLambdaChannel_Object=MibTableColumn
oaLdRoadmPortLambdaChannel=_OaLdRoadmPortLambdaChannel_Object((1,3,6,1,4,1,6926,1,41,15,6,1,11),_OaLdRoadmPortLambdaChannel_Type())
oaLdRoadmPortLambdaChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdRoadmPortLambdaChannel.setStatus(_A)
_OaLdRoadmPortVoaMinAttenuation_Type=Integer32
_OaLdRoadmPortVoaMinAttenuation_Object=MibTableColumn
oaLdRoadmPortVoaMinAttenuation=_OaLdRoadmPortVoaMinAttenuation_Object((1,3,6,1,4,1,6926,1,41,15,6,1,12),_OaLdRoadmPortVoaMinAttenuation_Type())
oaLdRoadmPortVoaMinAttenuation.setMaxAccess(_F)
if mibBuilder.loadTexts:oaLdRoadmPortVoaMinAttenuation.setStatus(_A)
_OaLdRoadmPortVoaMaxAttenuation_Type=Integer32
_OaLdRoadmPortVoaMaxAttenuation_Object=MibTableColumn
oaLdRoadmPortVoaMaxAttenuation=_OaLdRoadmPortVoaMaxAttenuation_Object((1,3,6,1,4,1,6926,1,41,15,6,1,13),_OaLdRoadmPortVoaMaxAttenuation_Type())
oaLdRoadmPortVoaMaxAttenuation.setMaxAccess(_F)
if mibBuilder.loadTexts:oaLdRoadmPortVoaMaxAttenuation.setStatus(_A)
class _OaLdRoadmPortName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(18,18));fixedLength=18
_OaLdRoadmPortName_Type.__name__=_J
_OaLdRoadmPortName_Object=MibTableColumn
oaLdRoadmPortName=_OaLdRoadmPortName_Object((1,3,6,1,4,1,6926,1,41,15,6,1,14),_OaLdRoadmPortName_Type())
oaLdRoadmPortName.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdRoadmPortName.setStatus(_A)
class _OaLdRoadmPortPowerSupported_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_A8,1),(_T,2)))
_OaLdRoadmPortPowerSupported_Type.__name__=_D
_OaLdRoadmPortPowerSupported_Object=MibTableColumn
oaLdRoadmPortPowerSupported=_OaLdRoadmPortPowerSupported_Object((1,3,6,1,4,1,6926,1,41,15,6,1,15),_OaLdRoadmPortPowerSupported_Type())
oaLdRoadmPortPowerSupported.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdRoadmPortPowerSupported.setStatus(_A)
_OaLdRoadmPortTotalPower_Type=Integer32
_OaLdRoadmPortTotalPower_Object=MibTableColumn
oaLdRoadmPortTotalPower=_OaLdRoadmPortTotalPower_Object((1,3,6,1,4,1,6926,1,41,15,6,1,16),_OaLdRoadmPortTotalPower_Type())
oaLdRoadmPortTotalPower.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdRoadmPortTotalPower.setStatus(_A)
class _OaLdRoadmPortChanList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(96,96));fixedLength=96
_OaLdRoadmPortChanList_Type.__name__=_X
_OaLdRoadmPortChanList_Object=MibTableColumn
oaLdRoadmPortChanList=_OaLdRoadmPortChanList_Object((1,3,6,1,4,1,6926,1,41,15,6,1,17),_OaLdRoadmPortChanList_Type())
oaLdRoadmPortChanList.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdRoadmPortChanList.setStatus(_A)
class _OaLdRoadmPortChanSrcPortList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(96,96));fixedLength=96
_OaLdRoadmPortChanSrcPortList_Type.__name__=_X
_OaLdRoadmPortChanSrcPortList_Object=MibTableColumn
oaLdRoadmPortChanSrcPortList=_OaLdRoadmPortChanSrcPortList_Object((1,3,6,1,4,1,6926,1,41,15,6,1,18),_OaLdRoadmPortChanSrcPortList_Type())
oaLdRoadmPortChanSrcPortList.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdRoadmPortChanSrcPortList.setStatus(_A)
class _OaLdRoadmPortBalancingAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),('balancing',2),('negate',3)))
_OaLdRoadmPortBalancingAdminStatus_Type.__name__=_D
_OaLdRoadmPortBalancingAdminStatus_Object=MibTableColumn
oaLdRoadmPortBalancingAdminStatus=_OaLdRoadmPortBalancingAdminStatus_Object((1,3,6,1,4,1,6926,1,41,15,6,1,19),_OaLdRoadmPortBalancingAdminStatus_Type())
oaLdRoadmPortBalancingAdminStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:oaLdRoadmPortBalancingAdminStatus.setStatus(_A)
class _OaLdRoadmPortBalancingOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_A6,2),(_f,3),('failed',4)))
_OaLdRoadmPortBalancingOperStatus_Type.__name__=_D
_OaLdRoadmPortBalancingOperStatus_Object=MibTableColumn
oaLdRoadmPortBalancingOperStatus=_OaLdRoadmPortBalancingOperStatus_Object((1,3,6,1,4,1,6926,1,41,15,6,1,20),_OaLdRoadmPortBalancingOperStatus_Type())
oaLdRoadmPortBalancingOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdRoadmPortBalancingOperStatus.setStatus(_A)
_OaLdRoadmPortBalancingPower_Type=Integer32
_OaLdRoadmPortBalancingPower_Object=MibTableColumn
oaLdRoadmPortBalancingPower=_OaLdRoadmPortBalancingPower_Object((1,3,6,1,4,1,6926,1,41,15,6,1,21),_OaLdRoadmPortBalancingPower_Type())
oaLdRoadmPortBalancingPower.setMaxAccess(_F)
if mibBuilder.loadTexts:oaLdRoadmPortBalancingPower.setStatus(_A)
_OaLdRoadmPortBalancingMaxChnlsNum_Type=Integer32
_OaLdRoadmPortBalancingMaxChnlsNum_Object=MibTableColumn
oaLdRoadmPortBalancingMaxChnlsNum=_OaLdRoadmPortBalancingMaxChnlsNum_Object((1,3,6,1,4,1,6926,1,41,15,6,1,22),_OaLdRoadmPortBalancingMaxChnlsNum_Type())
oaLdRoadmPortBalancingMaxChnlsNum.setMaxAccess(_F)
if mibBuilder.loadTexts:oaLdRoadmPortBalancingMaxChnlsNum.setStatus(_A)
_OaLdRoadmPortBalancingPowerPerChnl_Type=Integer32
_OaLdRoadmPortBalancingPowerPerChnl_Object=MibTableColumn
oaLdRoadmPortBalancingPowerPerChnl=_OaLdRoadmPortBalancingPowerPerChnl_Object((1,3,6,1,4,1,6926,1,41,15,6,1,23),_OaLdRoadmPortBalancingPowerPerChnl_Type())
oaLdRoadmPortBalancingPowerPerChnl.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdRoadmPortBalancingPowerPerChnl.setStatus(_A)
_OaLdRoadmPortThresholdTable_Object=MibTable
oaLdRoadmPortThresholdTable=_OaLdRoadmPortThresholdTable_Object((1,3,6,1,4,1,6926,1,41,15,7))
if mibBuilder.loadTexts:oaLdRoadmPortThresholdTable.setStatus(_A)
_OaLdRoadmPortThresholdEntry_Object=MibTableRow
oaLdRoadmPortThresholdEntry=_OaLdRoadmPortThresholdEntry_Object((1,3,6,1,4,1,6926,1,41,15,7,1))
oaLdRoadmPortThresholdEntry.setIndexNames((0,_C,_AY),(0,_C,_AZ),(0,_C,_Aa))
if mibBuilder.loadTexts:oaLdRoadmPortThresholdEntry.setStatus(_A)
_OaLdRoadmPortThresholdSlotIndex_Type=Integer32
_OaLdRoadmPortThresholdSlotIndex_Object=MibTableColumn
oaLdRoadmPortThresholdSlotIndex=_OaLdRoadmPortThresholdSlotIndex_Object((1,3,6,1,4,1,6926,1,41,15,7,1,1),_OaLdRoadmPortThresholdSlotIndex_Type())
oaLdRoadmPortThresholdSlotIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdRoadmPortThresholdSlotIndex.setStatus(_A)
_OaLdRoadmPortThresholdPortIndex_Type=Integer32
_OaLdRoadmPortThresholdPortIndex_Object=MibTableColumn
oaLdRoadmPortThresholdPortIndex=_OaLdRoadmPortThresholdPortIndex_Object((1,3,6,1,4,1,6926,1,41,15,7,1,2),_OaLdRoadmPortThresholdPortIndex_Type())
oaLdRoadmPortThresholdPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdRoadmPortThresholdPortIndex.setStatus(_A)
class _OaLdRoadmPortThresholdIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_AQ,1),(_AR,2),('failLow',3),('failHigh',4),(_AS,5),(_AT,6),(_AU,7),(_AV,8),('tRaise',9),('tFall',10)))
_OaLdRoadmPortThresholdIndex_Type.__name__=_D
_OaLdRoadmPortThresholdIndex_Object=MibTableColumn
oaLdRoadmPortThresholdIndex=_OaLdRoadmPortThresholdIndex_Object((1,3,6,1,4,1,6926,1,41,15,7,1,3),_OaLdRoadmPortThresholdIndex_Type())
oaLdRoadmPortThresholdIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdRoadmPortThresholdIndex.setStatus(_A)
_OaLdRoadmPortThresholdPwr_Type=Integer32
_OaLdRoadmPortThresholdPwr_Object=MibTableColumn
oaLdRoadmPortThresholdPwr=_OaLdRoadmPortThresholdPwr_Object((1,3,6,1,4,1,6926,1,41,15,7,1,4),_OaLdRoadmPortThresholdPwr_Type())
oaLdRoadmPortThresholdPwr.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdRoadmPortThresholdPwr.setStatus(_A)
_OaLdPortsCrossConnect_ObjectIdentity=ObjectIdentity
oaLdPortsCrossConnect=_OaLdPortsCrossConnect_ObjectIdentity((1,3,6,1,4,1,6926,1,41,16))
_OaLdPortsCrossConnectTable_Object=MibTable
oaLdPortsCrossConnectTable=_OaLdPortsCrossConnectTable_Object((1,3,6,1,4,1,6926,1,41,16,1))
if mibBuilder.loadTexts:oaLdPortsCrossConnectTable.setStatus(_A)
_OaLdPortsCrossConnectEntry_Object=MibTableRow
oaLdPortsCrossConnectEntry=_OaLdPortsCrossConnectEntry_Object((1,3,6,1,4,1,6926,1,41,16,1,1))
oaLdPortsCrossConnectEntry.setIndexNames((0,_C,_Ab),(0,_C,_Ac))
if mibBuilder.loadTexts:oaLdPortsCrossConnectEntry.setStatus(_A)
_OaLdPortsCrossConnectSlotNumber_Type=Integer32
_OaLdPortsCrossConnectSlotNumber_Object=MibTableColumn
oaLdPortsCrossConnectSlotNumber=_OaLdPortsCrossConnectSlotNumber_Object((1,3,6,1,4,1,6926,1,41,16,1,1,1),_OaLdPortsCrossConnectSlotNumber_Type())
oaLdPortsCrossConnectSlotNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdPortsCrossConnectSlotNumber.setStatus(_A)
_OaLdPortsCrossConnectPortNumber_Type=Integer32
_OaLdPortsCrossConnectPortNumber_Object=MibTableColumn
oaLdPortsCrossConnectPortNumber=_OaLdPortsCrossConnectPortNumber_Object((1,3,6,1,4,1,6926,1,41,16,1,1,2),_OaLdPortsCrossConnectPortNumber_Type())
oaLdPortsCrossConnectPortNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdPortsCrossConnectPortNumber.setStatus(_A)
_OaLdPortsCrossConnectNumber_Type=Integer32
_OaLdPortsCrossConnectNumber_Object=MibTableColumn
oaLdPortsCrossConnectNumber=_OaLdPortsCrossConnectNumber_Object((1,3,6,1,4,1,6926,1,41,16,1,1,3),_OaLdPortsCrossConnectNumber_Type())
oaLdPortsCrossConnectNumber.setMaxAccess(_F)
if mibBuilder.loadTexts:oaLdPortsCrossConnectNumber.setStatus(_A)
class _OaLdPortsCrossConnectAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),('connect',2),('disconnect',3)))
_OaLdPortsCrossConnectAction_Type.__name__=_D
_OaLdPortsCrossConnectAction_Object=MibTableColumn
oaLdPortsCrossConnectAction=_OaLdPortsCrossConnectAction_Object((1,3,6,1,4,1,6926,1,41,16,1,1,4),_OaLdPortsCrossConnectAction_Type())
oaLdPortsCrossConnectAction.setMaxAccess(_F)
if mibBuilder.loadTexts:oaLdPortsCrossConnectAction.setStatus(_A)
_OaLdOpticalMonitor_ObjectIdentity=ObjectIdentity
oaLdOpticalMonitor=_OaLdOpticalMonitor_ObjectIdentity((1,3,6,1,4,1,6926,1,41,17))
_OaLdMeasurmentPointsTable_Object=MibTable
oaLdMeasurmentPointsTable=_OaLdMeasurmentPointsTable_Object((1,3,6,1,4,1,6926,1,41,17,1))
if mibBuilder.loadTexts:oaLdMeasurmentPointsTable.setStatus(_A)
_OaLdMeasurmentPointsEntry_Object=MibTableRow
oaLdMeasurmentPointsEntry=_OaLdMeasurmentPointsEntry_Object((1,3,6,1,4,1,6926,1,41,17,1,1))
oaLdMeasurmentPointsEntry.setIndexNames((0,_C,_Ad),(0,_C,_Ae))
if mibBuilder.loadTexts:oaLdMeasurmentPointsEntry.setStatus(_A)
_OaLdMeasurmentPointsSlotNumber_Type=Integer32
_OaLdMeasurmentPointsSlotNumber_Object=MibTableColumn
oaLdMeasurmentPointsSlotNumber=_OaLdMeasurmentPointsSlotNumber_Object((1,3,6,1,4,1,6926,1,41,17,1,1,1),_OaLdMeasurmentPointsSlotNumber_Type())
oaLdMeasurmentPointsSlotNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdMeasurmentPointsSlotNumber.setStatus(_A)
_OaLdMeasurmentPointsPortNumber_Type=Integer32
_OaLdMeasurmentPointsPortNumber_Object=MibTableColumn
oaLdMeasurmentPointsPortNumber=_OaLdMeasurmentPointsPortNumber_Object((1,3,6,1,4,1,6926,1,41,17,1,1,2),_OaLdMeasurmentPointsPortNumber_Type())
oaLdMeasurmentPointsPortNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdMeasurmentPointsPortNumber.setStatus(_A)
_OaLdPeaksNumber_Type=Integer32
_OaLdPeaksNumber_Object=MibTableColumn
oaLdPeaksNumber=_OaLdPeaksNumber_Object((1,3,6,1,4,1,6926,1,41,17,1,1,3),_OaLdPeaksNumber_Type())
oaLdPeaksNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdPeaksNumber.setStatus(_A)
_OaLdTotalBandPower_Type=Integer32
_OaLdTotalBandPower_Object=MibTableColumn
oaLdTotalBandPower=_OaLdTotalBandPower_Object((1,3,6,1,4,1,6926,1,41,17,1,1,4),_OaLdTotalBandPower_Type())
oaLdTotalBandPower.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdTotalBandPower.setStatus(_A)
_OaLdPeaksMonitorTable_Object=MibTable
oaLdPeaksMonitorTable=_OaLdPeaksMonitorTable_Object((1,3,6,1,4,1,6926,1,41,17,2))
if mibBuilder.loadTexts:oaLdPeaksMonitorTable.setStatus(_A)
_OaLdPeaksMonitorEntry_Object=MibTableRow
oaLdPeaksMonitorEntry=_OaLdPeaksMonitorEntry_Object((1,3,6,1,4,1,6926,1,41,17,2,1))
oaLdPeaksMonitorEntry.setIndexNames((0,_C,_Af),(0,_C,_Ag),(0,_C,_Ah))
if mibBuilder.loadTexts:oaLdPeaksMonitorEntry.setStatus(_A)
_OaLdPeaksMonitorSlotNumber_Type=Integer32
_OaLdPeaksMonitorSlotNumber_Object=MibTableColumn
oaLdPeaksMonitorSlotNumber=_OaLdPeaksMonitorSlotNumber_Object((1,3,6,1,4,1,6926,1,41,17,2,1,1),_OaLdPeaksMonitorSlotNumber_Type())
oaLdPeaksMonitorSlotNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdPeaksMonitorSlotNumber.setStatus(_A)
_OaLdPeaksMonitorPortNumber_Type=Integer32
_OaLdPeaksMonitorPortNumber_Object=MibTableColumn
oaLdPeaksMonitorPortNumber=_OaLdPeaksMonitorPortNumber_Object((1,3,6,1,4,1,6926,1,41,17,2,1,2),_OaLdPeaksMonitorPortNumber_Type())
oaLdPeaksMonitorPortNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdPeaksMonitorPortNumber.setStatus(_A)
_OaLdPeaksMonitorPeakNumber_Type=Integer32
_OaLdPeaksMonitorPeakNumber_Object=MibTableColumn
oaLdPeaksMonitorPeakNumber=_OaLdPeaksMonitorPeakNumber_Object((1,3,6,1,4,1,6926,1,41,17,2,1,3),_OaLdPeaksMonitorPeakNumber_Type())
oaLdPeaksMonitorPeakNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdPeaksMonitorPeakNumber.setStatus(_A)
_OaLdPeaksMonitorPeakFreq_Type=Integer32
_OaLdPeaksMonitorPeakFreq_Object=MibTableColumn
oaLdPeaksMonitorPeakFreq=_OaLdPeaksMonitorPeakFreq_Object((1,3,6,1,4,1,6926,1,41,17,2,1,4),_OaLdPeaksMonitorPeakFreq_Type())
oaLdPeaksMonitorPeakFreq.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdPeaksMonitorPeakFreq.setStatus(_A)
_OaLdPeaksMonitorPeakWavelength_Type=Integer32
_OaLdPeaksMonitorPeakWavelength_Object=MibTableColumn
oaLdPeaksMonitorPeakWavelength=_OaLdPeaksMonitorPeakWavelength_Object((1,3,6,1,4,1,6926,1,41,17,2,1,5),_OaLdPeaksMonitorPeakWavelength_Type())
oaLdPeaksMonitorPeakWavelength.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdPeaksMonitorPeakWavelength.setStatus(_A)
_OaLdPeaksMonitorPeakPower_Type=Integer32
_OaLdPeaksMonitorPeakPower_Object=MibTableColumn
oaLdPeaksMonitorPeakPower=_OaLdPeaksMonitorPeakPower_Object((1,3,6,1,4,1,6926,1,41,17,2,1,6),_OaLdPeaksMonitorPeakPower_Type())
oaLdPeaksMonitorPeakPower.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdPeaksMonitorPeakPower.setStatus(_A)
_OaLdPeaksMonitorTotalPower_Type=Integer32
_OaLdPeaksMonitorTotalPower_Object=MibTableColumn
oaLdPeaksMonitorTotalPower=_OaLdPeaksMonitorTotalPower_Object((1,3,6,1,4,1,6926,1,41,17,2,1,7),_OaLdPeaksMonitorTotalPower_Type())
oaLdPeaksMonitorTotalPower.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdPeaksMonitorTotalPower.setStatus(_A)
_OaLdPeaksMonitorOsnr_Type=Integer32
_OaLdPeaksMonitorOsnr_Object=MibTableColumn
oaLdPeaksMonitorOsnr=_OaLdPeaksMonitorOsnr_Object((1,3,6,1,4,1,6926,1,41,17,2,1,8),_OaLdPeaksMonitorOsnr_Type())
oaLdPeaksMonitorOsnr.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdPeaksMonitorOsnr.setStatus(_A)
_OaLdPeaksMonitorLeftValleyFreq_Type=Integer32
_OaLdPeaksMonitorLeftValleyFreq_Object=MibTableColumn
oaLdPeaksMonitorLeftValleyFreq=_OaLdPeaksMonitorLeftValleyFreq_Object((1,3,6,1,4,1,6926,1,41,17,2,1,9),_OaLdPeaksMonitorLeftValleyFreq_Type())
oaLdPeaksMonitorLeftValleyFreq.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdPeaksMonitorLeftValleyFreq.setStatus(_A)
_OaLdPeaksMonitorLeftValleyPower_Type=Integer32
_OaLdPeaksMonitorLeftValleyPower_Object=MibTableColumn
oaLdPeaksMonitorLeftValleyPower=_OaLdPeaksMonitorLeftValleyPower_Object((1,3,6,1,4,1,6926,1,41,17,2,1,10),_OaLdPeaksMonitorLeftValleyPower_Type())
oaLdPeaksMonitorLeftValleyPower.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdPeaksMonitorLeftValleyPower.setStatus(_A)
_OaLdPeaksMonitorRightValleyFreq_Type=Integer32
_OaLdPeaksMonitorRightValleyFreq_Object=MibTableColumn
oaLdPeaksMonitorRightValleyFreq=_OaLdPeaksMonitorRightValleyFreq_Object((1,3,6,1,4,1,6926,1,41,17,2,1,11),_OaLdPeaksMonitorRightValleyFreq_Type())
oaLdPeaksMonitorRightValleyFreq.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdPeaksMonitorRightValleyFreq.setStatus(_A)
_OaLdPeaksMonitorRightValleyPower_Type=Integer32
_OaLdPeaksMonitorRightValleyPower_Object=MibTableColumn
oaLdPeaksMonitorRightValleyPower=_OaLdPeaksMonitorRightValleyPower_Object((1,3,6,1,4,1,6926,1,41,17,2,1,12),_OaLdPeaksMonitorRightValleyPower_Type())
oaLdPeaksMonitorRightValleyPower.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdPeaksMonitorRightValleyPower.setStatus(_A)
_OaLdDcmCardAttributes_ObjectIdentity=ObjectIdentity
oaLdDcmCardAttributes=_OaLdDcmCardAttributes_ObjectIdentity((1,3,6,1,4,1,6926,1,41,18))
_OaLdDcmCardPortsTable_Object=MibTable
oaLdDcmCardPortsTable=_OaLdDcmCardPortsTable_Object((1,3,6,1,4,1,6926,1,41,18,1))
if mibBuilder.loadTexts:oaLdDcmCardPortsTable.setStatus(_A)
_OaLdDcmCardPortsEntry_Object=MibTableRow
oaLdDcmCardPortsEntry=_OaLdDcmCardPortsEntry_Object((1,3,6,1,4,1,6926,1,41,18,1,1))
oaLdDcmCardPortsEntry.setIndexNames((0,_C,_Ai),(0,_C,_Aj))
if mibBuilder.loadTexts:oaLdDcmCardPortsEntry.setStatus(_A)
_OaLdDcmCardPortsSlotNumber_Type=Integer32
_OaLdDcmCardPortsSlotNumber_Object=MibTableColumn
oaLdDcmCardPortsSlotNumber=_OaLdDcmCardPortsSlotNumber_Object((1,3,6,1,4,1,6926,1,41,18,1,1,1),_OaLdDcmCardPortsSlotNumber_Type())
oaLdDcmCardPortsSlotNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdDcmCardPortsSlotNumber.setStatus(_A)
_OaLdDcmCardPortsPortNumber_Type=Integer32
_OaLdDcmCardPortsPortNumber_Object=MibTableColumn
oaLdDcmCardPortsPortNumber=_OaLdDcmCardPortsPortNumber_Object((1,3,6,1,4,1,6926,1,41,18,1,1,2),_OaLdDcmCardPortsPortNumber_Type())
oaLdDcmCardPortsPortNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdDcmCardPortsPortNumber.setStatus(_A)
_OaLdDcmCardPortsDistance_Type=Integer32
_OaLdDcmCardPortsDistance_Object=MibTableColumn
oaLdDcmCardPortsDistance=_OaLdDcmCardPortsDistance_Object((1,3,6,1,4,1,6926,1,41,18,1,1,3),_OaLdDcmCardPortsDistance_Type())
oaLdDcmCardPortsDistance.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdDcmCardPortsDistance.setStatus(_A)
_OaLdDcmCardPortsSpacing_Type=Integer32
_OaLdDcmCardPortsSpacing_Object=MibTableColumn
oaLdDcmCardPortsSpacing=_OaLdDcmCardPortsSpacing_Object((1,3,6,1,4,1,6926,1,41,18,1,1,4),_OaLdDcmCardPortsSpacing_Type())
oaLdDcmCardPortsSpacing.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdDcmCardPortsSpacing.setStatus(_A)
_OaLdDcmCardPortsRate_Type=Integer32
_OaLdDcmCardPortsRate_Object=MibTableColumn
oaLdDcmCardPortsRate=_OaLdDcmCardPortsRate_Object((1,3,6,1,4,1,6926,1,41,18,1,1,5),_OaLdDcmCardPortsRate_Type())
oaLdDcmCardPortsRate.setMaxAccess(_B)
if mibBuilder.loadTexts:oaLdDcmCardPortsRate.setStatus(_A)
powerSupplyUpLD=NotificationType((1,3,6,1,4,1,6926,1,41,0,2))
powerSupplyUpLD.setObjects((_C,_V))
if mibBuilder.loadTexts:powerSupplyUpLD.setStatus('')
powerSupplyDownLD=NotificationType((1,3,6,1,4,1,6926,1,41,0,3))
powerSupplyDownLD.setObjects((_C,_V))
if mibBuilder.loadTexts:powerSupplyDownLD.setStatus('')
powerSupplyInLD=NotificationType((1,3,6,1,4,1,6926,1,41,0,4))
powerSupplyInLD.setObjects((_C,_V))
if mibBuilder.loadTexts:powerSupplyInLD.setStatus('')
powerSupplyOutLD=NotificationType((1,3,6,1,4,1,6926,1,41,0,5))
powerSupplyOutLD.setObjects((_C,_V))
if mibBuilder.loadTexts:powerSupplyOutLD.setStatus('')
fanUp=NotificationType((1,3,6,1,4,1,6926,1,41,0,10))
fanUp.setObjects((_C,_Y))
if mibBuilder.loadTexts:fanUp.setStatus('')
fanDown=NotificationType((1,3,6,1,4,1,6926,1,41,0,11))
fanDown.setObjects((_C,_Y))
if mibBuilder.loadTexts:fanDown.setStatus('')
switchPrimary=NotificationType((1,3,6,1,4,1,6926,1,41,0,12))
if mibBuilder.loadTexts:switchPrimary.setStatus('')
switchSecondary=NotificationType((1,3,6,1,4,1,6926,1,41,0,13))
if mibBuilder.loadTexts:switchSecondary.setStatus('')
configChangeIn=NotificationType((1,3,6,1,4,1,6926,1,41,0,14))
configChangeIn.setObjects((_C,_O))
if mibBuilder.loadTexts:configChangeIn.setStatus('')
transponderAccessRx=NotificationType((1,3,6,1,4,1,6926,1,41,0,15))
transponderAccessRx.setObjects(*((_C,_O),(_C,_Ak)))
if mibBuilder.loadTexts:transponderAccessRx.setStatus('')
transponderWdmRx=NotificationType((1,3,6,1,4,1,6926,1,41,0,17))
transponderWdmRx.setObjects(*((_C,_O),(_C,_Al)))
if mibBuilder.loadTexts:transponderWdmRx.setStatus('')
configChangeOut=NotificationType((1,3,6,1,4,1,6926,1,41,0,19))
configChangeOut.setObjects((_C,_O))
if mibBuilder.loadTexts:configChangeOut.setStatus('')
transponderCardLoopBack=NotificationType((1,3,6,1,4,1,6926,1,41,0,20))
transponderCardLoopBack.setObjects(*((_C,_O),(_C,_g)))
if mibBuilder.loadTexts:transponderCardLoopBack.setStatus('')
redundantCardPrimaryRx=NotificationType((1,3,6,1,4,1,6926,1,41,0,21))
redundantCardPrimaryRx.setObjects(*((_C,_U),(_C,_Am)))
if mibBuilder.loadTexts:redundantCardPrimaryRx.setStatus('')
redundantCardSecondaryRx=NotificationType((1,3,6,1,4,1,6926,1,41,0,22))
redundantCardSecondaryRx.setObjects(*((_C,_U),(_C,_An)))
if mibBuilder.loadTexts:redundantCardSecondaryRx.setStatus('')
cardPortsLink=NotificationType((1,3,6,1,4,1,6926,1,41,0,23))
cardPortsLink.setObjects(*((_C,_G),(_C,_P),(_C,_Ao)))
if mibBuilder.loadTexts:cardPortsLink.setStatus('')
transponderEntityAccessRx=NotificationType((1,3,6,1,4,1,6926,1,41,0,25))
transponderEntityAccessRx.setObjects(*((_C,_Q),(_C,_R),(_C,_Ap)))
if mibBuilder.loadTexts:transponderEntityAccessRx.setStatus('')
transponderEntityWdmRx=NotificationType((1,3,6,1,4,1,6926,1,41,0,27))
transponderEntityWdmRx.setObjects(*((_C,_Q),(_C,_R),(_C,_Aq)))
if mibBuilder.loadTexts:transponderEntityWdmRx.setStatus('')
transponderEntityLoopBack=NotificationType((1,3,6,1,4,1,6926,1,41,0,28))
transponderEntityLoopBack.setObjects(*((_C,_Q),(_C,_R),(_C,_h)))
if mibBuilder.loadTexts:transponderEntityLoopBack.setStatus('')
transponderCardPortsLoopBack=NotificationType((1,3,6,1,4,1,6926,1,41,0,29))
transponderCardPortsLoopBack.setObjects(*((_C,_G),(_C,_P),(_C,_i)))
if mibBuilder.loadTexts:transponderCardPortsLoopBack.setStatus('')
transponderAccessRxOn=NotificationType((1,3,6,1,4,1,6926,1,41,0,30))
transponderAccessRxOn.setObjects(*((_C,_O),(_H,_I)))
if mibBuilder.loadTexts:transponderAccessRxOn.setStatus('')
transponderAccessRxOff=NotificationType((1,3,6,1,4,1,6926,1,41,0,31))
transponderAccessRxOff.setObjects(*((_C,_O),(_H,_I)))
if mibBuilder.loadTexts:transponderAccessRxOff.setStatus('')
transponderWdmRxOn=NotificationType((1,3,6,1,4,1,6926,1,41,0,32))
transponderWdmRxOn.setObjects(*((_C,_O),(_H,_I)))
if mibBuilder.loadTexts:transponderWdmRxOn.setStatus('')
transponderWdmRxOff=NotificationType((1,3,6,1,4,1,6926,1,41,0,33))
transponderWdmRxOff.setObjects(*((_C,_O),(_H,_I)))
if mibBuilder.loadTexts:transponderWdmRxOff.setStatus('')
transponderCardLoopBackLoop=NotificationType((1,3,6,1,4,1,6926,1,41,0,34))
transponderCardLoopBackLoop.setObjects(*((_C,_O),(_C,_g),(_H,_I)))
if mibBuilder.loadTexts:transponderCardLoopBackLoop.setStatus('')
transponderCardLoopBackNormal=NotificationType((1,3,6,1,4,1,6926,1,41,0,35))
transponderCardLoopBackNormal.setObjects(*((_C,_O),(_C,_g),(_H,_I)))
if mibBuilder.loadTexts:transponderCardLoopBackNormal.setStatus('')
cardPortsLinkOn=NotificationType((1,3,6,1,4,1,6926,1,41,0,36))
cardPortsLinkOn.setObjects(*((_C,_G),(_C,_P),(_H,_I)))
if mibBuilder.loadTexts:cardPortsLinkOn.setStatus('')
cardPortsLinkOff=NotificationType((1,3,6,1,4,1,6926,1,41,0,37))
cardPortsLinkOff.setObjects(*((_C,_G),(_C,_P),(_H,_I)))
if mibBuilder.loadTexts:cardPortsLinkOff.setStatus('')
transponderEntityAccessRxOn=NotificationType((1,3,6,1,4,1,6926,1,41,0,38))
transponderEntityAccessRxOn.setObjects(*((_C,_Q),(_C,_R),(_H,_I)))
if mibBuilder.loadTexts:transponderEntityAccessRxOn.setStatus('')
transponderEntityAccessRxOff=NotificationType((1,3,6,1,4,1,6926,1,41,0,39))
transponderEntityAccessRxOff.setObjects(*((_C,_Q),(_C,_R),(_H,_I)))
if mibBuilder.loadTexts:transponderEntityAccessRxOff.setStatus('')
transponderEntityWdmRxOn=NotificationType((1,3,6,1,4,1,6926,1,41,0,40))
transponderEntityWdmRxOn.setObjects(*((_C,_Q),(_C,_R),(_H,_I)))
if mibBuilder.loadTexts:transponderEntityWdmRxOn.setStatus('')
transponderEntityWdmRxOff=NotificationType((1,3,6,1,4,1,6926,1,41,0,41))
transponderEntityWdmRxOff.setObjects(*((_C,_Q),(_C,_R),(_H,_I)))
if mibBuilder.loadTexts:transponderEntityWdmRxOff.setStatus('')
transponderEntityLoopBackLoop=NotificationType((1,3,6,1,4,1,6926,1,41,0,42))
transponderEntityLoopBackLoop.setObjects(*((_C,_Q),(_C,_R),(_C,_h),(_H,_I)))
if mibBuilder.loadTexts:transponderEntityLoopBackLoop.setStatus('')
transponderEntityLoopBackNormal=NotificationType((1,3,6,1,4,1,6926,1,41,0,43))
transponderEntityLoopBackNormal.setObjects(*((_C,_Q),(_C,_R),(_C,_h),(_H,_I)))
if mibBuilder.loadTexts:transponderEntityLoopBackNormal.setStatus('')
transponderCardPortsLoopBackLoop=NotificationType((1,3,6,1,4,1,6926,1,41,0,44))
transponderCardPortsLoopBackLoop.setObjects(*((_C,_G),(_C,_P),(_C,_i),(_H,_I)))
if mibBuilder.loadTexts:transponderCardPortsLoopBackLoop.setStatus('')
transponderCardPortsLoopBackNormal=NotificationType((1,3,6,1,4,1,6926,1,41,0,45))
transponderCardPortsLoopBackNormal.setObjects(*((_C,_G),(_C,_P),(_C,_i),(_H,_I)))
if mibBuilder.loadTexts:transponderCardPortsLoopBackNormal.setStatus('')
redCardPositionPrimary=NotificationType((1,3,6,1,4,1,6926,1,41,0,46))
redCardPositionPrimary.setObjects((_C,_O))
if mibBuilder.loadTexts:redCardPositionPrimary.setStatus('')
redCardPositionSecondary=NotificationType((1,3,6,1,4,1,6926,1,41,0,47))
redCardPositionSecondary.setObjects((_C,_O))
if mibBuilder.loadTexts:redCardPositionSecondary.setStatus('')
oaLdCardTemperatureNormal=NotificationType((1,3,6,1,4,1,6926,1,41,0,48))
oaLdCardTemperatureNormal.setObjects((_C,_G))
if mibBuilder.loadTexts:oaLdCardTemperatureNormal.setStatus('')
oaLdCardTemperatureHigh=NotificationType((1,3,6,1,4,1,6926,1,41,0,49))
oaLdCardTemperatureHigh.setObjects((_C,_G))
if mibBuilder.loadTexts:oaLdCardTemperatureHigh.setStatus('')
oaLdOAmplifierInputAlarmOn=NotificationType((1,3,6,1,4,1,6926,1,41,0,50))
oaLdOAmplifierInputAlarmOn.setObjects((_C,_G))
if mibBuilder.loadTexts:oaLdOAmplifierInputAlarmOn.setStatus('')
oaLdOAmplifierInputAlarmOff=NotificationType((1,3,6,1,4,1,6926,1,41,0,51))
oaLdOAmplifierInputAlarmOff.setObjects((_C,_G))
if mibBuilder.loadTexts:oaLdOAmplifierInputAlarmOff.setStatus('')
oaLdOAmplifierOutputAlarmOn=NotificationType((1,3,6,1,4,1,6926,1,41,0,52))
oaLdOAmplifierOutputAlarmOn.setObjects((_C,_G))
if mibBuilder.loadTexts:oaLdOAmplifierOutputAlarmOn.setStatus('')
oaLdOAmplifierOutputAlarmOff=NotificationType((1,3,6,1,4,1,6926,1,41,0,53))
oaLdOAmplifierOutputAlarmOff.setObjects((_C,_G))
if mibBuilder.loadTexts:oaLdOAmplifierOutputAlarmOff.setStatus('')
oaLdOAmplifierModuleTempAlarmOn=NotificationType((1,3,6,1,4,1,6926,1,41,0,54))
oaLdOAmplifierModuleTempAlarmOn.setObjects((_C,_G))
if mibBuilder.loadTexts:oaLdOAmplifierModuleTempAlarmOn.setStatus('')
oaLdOAmplifierModuleTempAlarmOff=NotificationType((1,3,6,1,4,1,6926,1,41,0,55))
oaLdOAmplifierModuleTempAlarmOff.setObjects((_C,_G))
if mibBuilder.loadTexts:oaLdOAmplifierModuleTempAlarmOff.setStatus('')
oaLdOAmplifierInput2AlarmOn=NotificationType((1,3,6,1,4,1,6926,1,41,0,56))
oaLdOAmplifierInput2AlarmOn.setObjects((_C,_G))
if mibBuilder.loadTexts:oaLdOAmplifierInput2AlarmOn.setStatus('')
oaLdOAmplifierInput2AlarmOff=NotificationType((1,3,6,1,4,1,6926,1,41,0,57))
oaLdOAmplifierInput2AlarmOff.setObjects((_C,_G))
if mibBuilder.loadTexts:oaLdOAmplifierInput2AlarmOff.setStatus('')
oaLdOAmplifierPSAlarmOn=NotificationType((1,3,6,1,4,1,6926,1,41,0,58))
oaLdOAmplifierPSAlarmOn.setObjects((_C,_G))
if mibBuilder.loadTexts:oaLdOAmplifierPSAlarmOn.setStatus('')
oaLdOAmplifierPSAlarmOff=NotificationType((1,3,6,1,4,1,6926,1,41,0,59))
oaLdOAmplifierPSAlarmOff.setObjects((_C,_G))
if mibBuilder.loadTexts:oaLdOAmplifierPSAlarmOff.setStatus('')
oaLdOAmplifierAutoShutdownAlarmOn=NotificationType((1,3,6,1,4,1,6926,1,41,0,60))
oaLdOAmplifierAutoShutdownAlarmOn.setObjects((_C,_G))
if mibBuilder.loadTexts:oaLdOAmplifierAutoShutdownAlarmOn.setStatus('')
oaLdOAmplifierAutoShutdownAlarmOff=NotificationType((1,3,6,1,4,1,6926,1,41,0,61))
oaLdOAmplifierAutoShutdownAlarmOff.setObjects((_C,_G))
if mibBuilder.loadTexts:oaLdOAmplifierAutoShutdownAlarmOff.setStatus('')
oaLdOAmplifierPumpTempAlarmOn=NotificationType((1,3,6,1,4,1,6926,1,41,0,62))
oaLdOAmplifierPumpTempAlarmOn.setObjects((_C,_G))
if mibBuilder.loadTexts:oaLdOAmplifierPumpTempAlarmOn.setStatus('')
oaLdOAmplifierPumpTempAlarmOff=NotificationType((1,3,6,1,4,1,6926,1,41,0,63))
oaLdOAmplifierPumpTempAlarmOff.setObjects((_C,_G))
if mibBuilder.loadTexts:oaLdOAmplifierPumpTempAlarmOff.setStatus('')
oaLdOAmplifierPumpDriveCurrentAlarmOn=NotificationType((1,3,6,1,4,1,6926,1,41,0,64))
oaLdOAmplifierPumpDriveCurrentAlarmOn.setObjects((_C,_G))
if mibBuilder.loadTexts:oaLdOAmplifierPumpDriveCurrentAlarmOn.setStatus('')
oaLdOAmplifierPumpDriveCurrentAlarmOff=NotificationType((1,3,6,1,4,1,6926,1,41,0,65))
oaLdOAmplifierPumpDriveCurrentAlarmOff.setObjects((_C,_G))
if mibBuilder.loadTexts:oaLdOAmplifierPumpDriveCurrentAlarmOff.setStatus('')
oaLdRamanAmplifierReflectedAlarmOn=NotificationType((1,3,6,1,4,1,6926,1,41,0,66))
oaLdRamanAmplifierReflectedAlarmOn.setObjects((_C,_G))
if mibBuilder.loadTexts:oaLdRamanAmplifierReflectedAlarmOn.setStatus('')
oaLdRamanAmplifierReflectedAlarmOff=NotificationType((1,3,6,1,4,1,6926,1,41,0,67))
oaLdRamanAmplifierReflectedAlarmOff.setObjects((_C,_G))
if mibBuilder.loadTexts:oaLdRamanAmplifierReflectedAlarmOff.setStatus('')
oaLdDevCPUForceSwitchoverCommandInvoked=NotificationType((1,3,6,1,4,1,6926,1,41,0,94))
if mibBuilder.loadTexts:oaLdDevCPUForceSwitchoverCommandInvoked.setStatus('')
oaLdFiberPrbsTestError=NotificationType((1,3,6,1,4,1,6926,1,41,0,95))
oaLdFiberPrbsTestError.setObjects((_C,_O))
if mibBuilder.loadTexts:oaLdFiberPrbsTestError.setStatus('')
oaLdEMPortDryContactClosed=NotificationType((1,3,6,1,4,1,6926,1,41,0,96))
oaLdEMPortDryContactClosed.setObjects(*((_C,_G),(_C,_P),(_H,_I)))
if mibBuilder.loadTexts:oaLdEMPortDryContactClosed.setStatus('')
oaLdEMPortDryContactOpened=NotificationType((1,3,6,1,4,1,6926,1,41,0,97))
oaLdEMPortDryContactOpened.setObjects(*((_C,_G),(_C,_P),(_H,_I)))
if mibBuilder.loadTexts:oaLdEMPortDryContactOpened.setStatus('')
oaLdCardRestarted=NotificationType((1,3,6,1,4,1,6926,1,41,0,163))
oaLdCardRestarted.setObjects((_C,_G))
if mibBuilder.loadTexts:oaLdCardRestarted.setStatus('')
redundantCardPrimaryRxOn=NotificationType((1,3,6,1,4,1,6926,1,41,0,164))
redundantCardPrimaryRxOn.setObjects((_C,_U))
if mibBuilder.loadTexts:redundantCardPrimaryRxOn.setStatus('')
redundantCardPrimaryRxOff=NotificationType((1,3,6,1,4,1,6926,1,41,0,165))
redundantCardPrimaryRxOff.setObjects((_C,_U))
if mibBuilder.loadTexts:redundantCardPrimaryRxOff.setStatus('')
redundantCardSecondaryRxOn=NotificationType((1,3,6,1,4,1,6926,1,41,0,166))
redundantCardSecondaryRxOn.setObjects((_C,_U))
if mibBuilder.loadTexts:redundantCardSecondaryRxOn.setStatus('')
redundantCardSecondaryRxOff=NotificationType((1,3,6,1,4,1,6926,1,41,0,167))
redundantCardSecondaryRxOff.setObjects((_C,_U))
if mibBuilder.loadTexts:redundantCardSecondaryRxOff.setStatus('')
cardPortsPrimaryClockSource=NotificationType((1,3,6,1,4,1,6926,1,41,0,168))
cardPortsPrimaryClockSource.setObjects(*((_C,_Q),(_C,_R),(_C,_s),(_H,_I)))
if mibBuilder.loadTexts:cardPortsPrimaryClockSource.setStatus('')
cardPortsNonPrimaryClockSource=NotificationType((1,3,6,1,4,1,6926,1,41,0,169))
cardPortsNonPrimaryClockSource.setObjects(*((_C,_Q),(_C,_R),(_C,_s),(_H,_I)))
if mibBuilder.loadTexts:cardPortsNonPrimaryClockSource.setStatus('')
eyemaxScanningStart=NotificationType((1,3,6,1,4,1,6926,1,41,0,170))
eyemaxScanningStart.setObjects(*((_C,_G),(_C,_P),(_H,_I)))
if mibBuilder.loadTexts:eyemaxScanningStart.setStatus('')
eyemaxScanningCompleted=NotificationType((1,3,6,1,4,1,6926,1,41,0,171))
eyemaxScanningCompleted.setObjects(*((_C,_G),(_C,_P),(_H,_I)))
if mibBuilder.loadTexts:eyemaxScanningCompleted.setStatus('')
powerBalancingDone=NotificationType((1,3,6,1,4,1,6926,1,41,0,172))
powerBalancingDone.setObjects(*((_C,_G),(_C,_P),(_H,_I)))
if mibBuilder.loadTexts:powerBalancingDone.setStatus('')
powerBalancingNegate=NotificationType((1,3,6,1,4,1,6926,1,41,0,173))
powerBalancingNegate.setObjects(*((_C,_G),(_C,_P),(_H,_I)))
if mibBuilder.loadTexts:powerBalancingNegate.setStatus('')
rebootIsRequestedByUser=NotificationType((1,3,6,1,4,1,6926,1,41,0,174))
if mibBuilder.loadTexts:rebootIsRequestedByUser.setStatus('')
mibBuilder.exportSymbols(_C,**{'LambdaCh':LambdaCh,'RateSelect':RateSelect,'RateMode':RateMode,'oaccess':oaccess,'oaManagement':oaManagement,'oaLambdaDriver':oaLambdaDriver,'powerSupplyUpLD':powerSupplyUpLD,'powerSupplyDownLD':powerSupplyDownLD,'powerSupplyInLD':powerSupplyInLD,'powerSupplyOutLD':powerSupplyOutLD,'fanUp':fanUp,'fanDown':fanDown,'switchPrimary':switchPrimary,'switchSecondary':switchSecondary,'configChangeIn':configChangeIn,'transponderAccessRx':transponderAccessRx,'transponderWdmRx':transponderWdmRx,'configChangeOut':configChangeOut,'transponderCardLoopBack':transponderCardLoopBack,'redundantCardPrimaryRx':redundantCardPrimaryRx,'redundantCardSecondaryRx':redundantCardSecondaryRx,'cardPortsLink':cardPortsLink,'transponderEntityAccessRx':transponderEntityAccessRx,'transponderEntityWdmRx':transponderEntityWdmRx,'transponderEntityLoopBack':transponderEntityLoopBack,'transponderCardPortsLoopBack':transponderCardPortsLoopBack,'transponderAccessRxOn':transponderAccessRxOn,'transponderAccessRxOff':transponderAccessRxOff,'transponderWdmRxOn':transponderWdmRxOn,'transponderWdmRxOff':transponderWdmRxOff,'transponderCardLoopBackLoop':transponderCardLoopBackLoop,'transponderCardLoopBackNormal':transponderCardLoopBackNormal,'cardPortsLinkOn':cardPortsLinkOn,'cardPortsLinkOff':cardPortsLinkOff,'transponderEntityAccessRxOn':transponderEntityAccessRxOn,'transponderEntityAccessRxOff':transponderEntityAccessRxOff,'transponderEntityWdmRxOn':transponderEntityWdmRxOn,'transponderEntityWdmRxOff':transponderEntityWdmRxOff,'transponderEntityLoopBackLoop':transponderEntityLoopBackLoop,'transponderEntityLoopBackNormal':transponderEntityLoopBackNormal,'transponderCardPortsLoopBackLoop':transponderCardPortsLoopBackLoop,'transponderCardPortsLoopBackNormal':transponderCardPortsLoopBackNormal,'redCardPositionPrimary':redCardPositionPrimary,'redCardPositionSecondary':redCardPositionSecondary,'oaLdCardTemperatureNormal':oaLdCardTemperatureNormal,'oaLdCardTemperatureHigh':oaLdCardTemperatureHigh,'oaLdOAmplifierInputAlarmOn':oaLdOAmplifierInputAlarmOn,'oaLdOAmplifierInputAlarmOff':oaLdOAmplifierInputAlarmOff,'oaLdOAmplifierOutputAlarmOn':oaLdOAmplifierOutputAlarmOn,'oaLdOAmplifierOutputAlarmOff':oaLdOAmplifierOutputAlarmOff,'oaLdOAmplifierModuleTempAlarmOn':oaLdOAmplifierModuleTempAlarmOn,'oaLdOAmplifierModuleTempAlarmOff':oaLdOAmplifierModuleTempAlarmOff,'oaLdOAmplifierInput2AlarmOn':oaLdOAmplifierInput2AlarmOn,'oaLdOAmplifierInput2AlarmOff':oaLdOAmplifierInput2AlarmOff,'oaLdOAmplifierPSAlarmOn':oaLdOAmplifierPSAlarmOn,'oaLdOAmplifierPSAlarmOff':oaLdOAmplifierPSAlarmOff,'oaLdOAmplifierAutoShutdownAlarmOn':oaLdOAmplifierAutoShutdownAlarmOn,'oaLdOAmplifierAutoShutdownAlarmOff':oaLdOAmplifierAutoShutdownAlarmOff,'oaLdOAmplifierPumpTempAlarmOn':oaLdOAmplifierPumpTempAlarmOn,'oaLdOAmplifierPumpTempAlarmOff':oaLdOAmplifierPumpTempAlarmOff,'oaLdOAmplifierPumpDriveCurrentAlarmOn':oaLdOAmplifierPumpDriveCurrentAlarmOn,'oaLdOAmplifierPumpDriveCurrentAlarmOff':oaLdOAmplifierPumpDriveCurrentAlarmOff,'oaLdRamanAmplifierReflectedAlarmOn':oaLdRamanAmplifierReflectedAlarmOn,'oaLdRamanAmplifierReflectedAlarmOff':oaLdRamanAmplifierReflectedAlarmOff,'oaLdDevCPUForceSwitchoverCommandInvoked':oaLdDevCPUForceSwitchoverCommandInvoked,'oaLdFiberPrbsTestError':oaLdFiberPrbsTestError,'oaLdEMPortDryContactClosed':oaLdEMPortDryContactClosed,'oaLdEMPortDryContactOpened':oaLdEMPortDryContactOpened,'oaLdCardRestarted':oaLdCardRestarted,'redundantCardPrimaryRxOn':redundantCardPrimaryRxOn,'redundantCardPrimaryRxOff':redundantCardPrimaryRxOff,'redundantCardSecondaryRxOn':redundantCardSecondaryRxOn,'redundantCardSecondaryRxOff':redundantCardSecondaryRxOff,'cardPortsPrimaryClockSource':cardPortsPrimaryClockSource,'cardPortsNonPrimaryClockSource':cardPortsNonPrimaryClockSource,'eyemaxScanningStart':eyemaxScanningStart,'eyemaxScanningCompleted':eyemaxScanningCompleted,'powerBalancingDone':powerBalancingDone,'powerBalancingNegate':powerBalancingNegate,'rebootIsRequestedByUser':rebootIsRequestedByUser,'oaLdDevIdentify':oaLdDevIdentify,'oaLdNSlots':oaLdNSlots,'oaLdCardHardVers':oaLdCardHardVers,'oaLdSoftVers':oaLdSoftVers,'oaLdCreatinDate':oaLdCreatinDate,'oaLdDeviceType':oaLdDeviceType,'oaLdCardFpgaVers':oaLdCardFpgaVers,'oaLdCardBackplaneVers':oaLdCardBackplaneVers,'oaLdTrapsVer':oaLdTrapsVer,'oaLdCpuCardSerialNumber':oaLdCpuCardSerialNumber,'oaLdDevGenConfig':oaLdDevGenConfig,'oaLdDevPS':oaLdDevPS,'oaLdDevPSNumber':oaLdDevPSNumber,'oaLdDevPSTable':oaLdDevPSTable,'oaLdDevPSEntry':oaLdDevPSEntry,_V:oaLdDevPSIndex,'oaLdDevPSOperStatus':oaLdDevPSOperStatus,'oaLdDevPSPartNumber':oaLdDevPSPartNumber,'oaLdDevPSSerialNumber':oaLdDevPSSerialNumber,'oaLdDevPSHwRev':oaLdDevPSHwRev,'oaLdDevFAN':oaLdDevFAN,'oaLdDevFANsNumber':oaLdDevFANsNumber,'oaLdDevFANTable':oaLdDevFANTable,'oaLdDevFANEntry':oaLdDevFANEntry,_Y:oaLdDevFANIndex,'oaLdDevFANOperStatus':oaLdDevFANOperStatus,'oaLdDevCPU':oaLdDevCPU,'oaLdDevCPUNumber':oaLdDevCPUNumber,'oaLdDevCPUTable':oaLdDevCPUTable,'oaLdDevCPUEntry':oaLdDevCPUEntry,_A4:oaLdDevCPUIndex,'oaLdDevCPUOperStatus':oaLdDevCPUOperStatus,'oaLdDevCPUType':oaLdDevCPUType,'oaLdDevCPUHardVers':oaLdDevCPUHardVers,'oaLdDevCPUFpgaVers':oaLdDevCPUFpgaVers,'oaLdDevCPUSerialNumber':oaLdDevCPUSerialNumber,'oaLdDevCPUBuildTime':oaLdDevCPUBuildTime,'oaLdDevCPUSoftVers':oaLdDevCPUSoftVers,'oaLdDevCPUBoardID':oaLdDevCPUBoardID,'oaLdDevCPUBoardHardVers':oaLdDevCPUBoardHardVers,'oaLdDevRedundantCPU':oaLdDevRedundantCPU,'oaLdDevRedundantFeature':oaLdDevRedundantFeature,'oaLdDevRedundantMode':oaLdDevRedundantMode,'oaLdDevRedundantCommand':oaLdDevRedundantCommand,'oaLdDevRedundantPeerAdminStatus':oaLdDevRedundantPeerAdminStatus,'oaLdDevGenIdentify':oaLdDevGenIdentify,'oaLdCardBackplaneSN':oaLdCardBackplaneSN,'oaLdSoftVersString':oaLdSoftVersString,'oaLdCardBackplanePN':oaLdCardBackplanePN,'oaLdCardIftableExtMode':oaLdCardIftableExtMode,'oaLdSlotsStatTable':oaLdSlotsStatTable,'oaLdCardsStatTable':oaLdCardsStatTable,'oaLdCardsStatEntry':oaLdCardsStatEntry,_O:oaLdCardIndex,'oaLdCardType':oaLdCardType,'oaLdCardRev':oaLdCardRev,'oaLdCardLambdaCh':oaLdCardLambdaCh,_Ak:oaLdCardOptAccRx,_Al:oaLdCardOptDwdmRx,'oaLdCardDwdmLaserTx':oaLdCardDwdmLaserTx,'oaLdCardLaserTemp':oaLdCardLaserTemp,'oaLdCardAmbientTemp':oaLdCardAmbientTemp,'oaLdCardRateSelect':oaLdCardRateSelect,'oaLdCardRateMode':oaLdCardRateMode,'oaLdCardLaserMode':oaLdCardLaserMode,'oaLdCardWdmRxPm':oaLdCardWdmRxPm,'oaLdCardWdmTxPm':oaLdCardWdmTxPm,_g:oaLdCardLoopBack,'oaLdCardRedundantState':oaLdCardRedundantState,'oaLdCardPrimaryState':oaLdCardPrimaryState,'oaLdCardFPGARev':oaLdCardFPGARev,'oaLdCardPartNumber':oaLdCardPartNumber,'oaLdCardSerialNumber':oaLdCardSerialNumber,'oaLdCardHwRev':oaLdCardHwRev,'oaLdCardOptAccTx':oaLdCardOptAccTx,'oaLdCardOptDwdmTx':oaLdCardOptDwdmTx,'oaLdCardTemp':oaLdCardTemp,'oaLdCardSubType':oaLdCardSubType,'oaLdSlotEntitysStat':oaLdSlotEntitysStat,'oaLdCardEntityStatTable':oaLdCardEntityStatTable,'oaLdCardEntityStatEntry':oaLdCardEntityStatEntry,_Q:oaLdCardEntityCardIndex,_R:oaLdCardEntityEntityIndex,'oaLdCardEntityWaveLength':oaLdCardEntityWaveLength,_Ap:oaLdCardEntityOptAccRx,_Aq:oaLdCardEntityOptDwdmRx,'oaLdCardEntityDwdmLaserTx':oaLdCardEntityDwdmLaserTx,'oaLdCardEntityLaserTemp':oaLdCardEntityLaserTemp,'oaLdCardEntityAmbientTemp':oaLdCardEntityAmbientTemp,'oaLdCardEntityRateSelect':oaLdCardEntityRateSelect,'oaLdCardEntityRateMode':oaLdCardEntityRateMode,'oaLdCardEntityLaserMode':oaLdCardEntityLaserMode,'oaLdCardEntityWdmRxPm':oaLdCardEntityWdmRxPm,'oaLdCardEntityWdmTxPm':oaLdCardEntityWdmTxPm,_h:oaLdCardEntityLoopBack,'oaLdCardEntityRedundantState':oaLdCardEntityRedundantState,'oaLdCardEntityPrimaryState':oaLdCardEntityPrimaryState,_s:oaLdCardEntityClockSource,'oaLdCardEntityTransparency':oaLdCardEntityTransparency,'oaLdCardEntityStandard':oaLdCardEntityStandard,'oaLdCardEntityAccessLinState':oaLdCardEntityAccessLinState,'oaLdCardEntityLineCoding':oaLdCardEntityLineCoding,'oaLdCardEntityUartBaudRate':oaLdCardEntityUartBaudRate,'oaLdCardEntityUartParity':oaLdCardEntityUartParity,'oaLdCardEntityUartStopBit':oaLdCardEntityUartStopBit,'oaLdCardEntityPmMode':oaLdCardEntityPmMode,'oaLdCardEntityWdmFecMode':oaLdCardEntityWdmFecMode,'oaLdCardEntityMinDispDist':oaLdCardEntityMinDispDist,'oaLdCardEntityMaxDispDist':oaLdCardEntityMaxDispDist,'oaLdCardEntityDispDist':oaLdCardEntityDispDist,'oaLdCardEntityCCMode':oaLdCardEntityCCMode,'oaLdCardEntityOptAccTx':oaLdCardEntityOptAccTx,'oaLdCardEntityOptDwdmTx':oaLdCardEntityOptDwdmTx,'oaLdCardEntityEMCfgType':oaLdCardEntityEMCfgType,'oaLdCardEntityEMCfgSide':oaLdCardEntityEMCfgSide,'oaLdCardEntityPreemptionMode':oaLdCardEntityPreemptionMode,'oaLdCardEntityActivePort':oaLdCardEntityActivePort,'oaLdCardEntityOperationMode':oaLdCardEntityOperationMode,'oaLdCardEntityRedundantType':oaLdCardEntityRedundantType,'oaLdCardEntityOtu2MappingMode':oaLdCardEntityOtu2MappingMode,'oaLdCardEntityTopologyMode':oaLdCardEntityTopologyMode,'oaLdCardEntityDispDistAdmin':oaLdCardEntityDispDistAdmin,'oaLdCardEntityChannelOffset':oaLdCardEntityChannelOffset,'oaLdCardEntityTimingMode':oaLdCardEntityTimingMode,'oaLdCardEntityTdcmTuningStatus':oaLdCardEntityTdcmTuningStatus,'oaLdCardEntityRedModeActivePort':oaLdCardEntityRedModeActivePort,'oaLdCardEntityAutoShutdownMode':oaLdCardEntityAutoShutdownMode,'oaLdRedundantOptic':oaLdRedundantOptic,'oaLdRedundantOpticTable':oaLdRedundantOpticTable,'oaLdRedundantOpticEntry':oaLdRedundantOpticEntry,_U:oaLdRedOptSlotNumber,'oaLdRedOptSwitchPosition':oaLdRedOptSwitchPosition,'oaLdRedOptLastCommand':oaLdRedOptLastCommand,_Am:oaLdRedOptPrimaryRx,_An:oaLdRedOptSecondaryRx,'oaLdCardPortsStat':oaLdCardPortsStat,'oaLdCardPortsStatTable':oaLdCardPortsStatTable,'oaLdCardPortsStatEntry':oaLdCardPortsStatEntry,_G:oaLdCardPortsSlotNumber,_P:oaLdCardPortsPortNumber,_Ao:oaLdCardPortsLink,'oaLdCardPortsActivity':oaLdCardPortsActivity,'oaLdCardPortsWaveLength':oaLdCardPortsWaveLength,_i:oaLdCardPortsLoopBack,'oaLdCardPortsCounters':oaLdCardPortsCounters,'oaLdCardPortsCounter1Low':oaLdCardPortsCounter1Low,'oaLdCardPortsCounter1High':oaLdCardPortsCounter1High,'oaLdCardPortsCounter2Low':oaLdCardPortsCounter2Low,'oaLdCardPortsCounter2High':oaLdCardPortsCounter2High,'oaLdCardPortsConnectorType':oaLdCardPortsConnectorType,'oaLdCardPortsConnectorSubType':oaLdCardPortsConnectorSubType,'oaLdCardPortsRate':oaLdCardPortsRate,'oaLdCardPortsLineLength':oaLdCardPortsLineLength,'oaLdCardPortsAccessLinState':oaLdCardPortsAccessLinState,'oaLdCardPortsFlowControlMode':oaLdCardPortsFlowControlMode,'oaLdCardPortsDryContactStat':oaLdCardPortsDryContactStat,'oaLdCardPortsPowerTuning':oaLdCardPortsPowerTuning,'oaLdCardPortsMediaType':oaLdCardPortsMediaType,'oaLdCardPortsEMCfgOperation':oaLdCardPortsEMCfgOperation,'oaLdCardPortsEyemaxState':oaLdCardPortsEyemaxState,'oaLdCardPortsEyemaxOperFactor':oaLdCardPortsEyemaxOperFactor,'oaLdCardPortsEyemaxAdminFactor':oaLdCardPortsEyemaxAdminFactor,'oaLdCardPortsFefMode':oaLdCardPortsFefMode,'oaLdCardPortsOdu1Index':oaLdCardPortsOdu1Index,'oaLdCardPortsOdu1TsIndex':oaLdCardPortsOdu1TsIndex,'oaLdCardPortsPmMode':oaLdCardPortsPmMode,'oaLdCardPortsFecMode':oaLdCardPortsFecMode,'oaLdCardPortsLock':oaLdCardPortsLock,'oaLdCardPortsLaserMode':oaLdCardPortsLaserMode,'oaLdCardPortsOdu1TsSize':oaLdCardPortsOdu1TsSize,'oaLdCardPortsSpeed':oaLdCardPortsSpeed,'oaLdCardPortsPriorityClockSource':oaLdCardPortsPriorityClockSource,'oaLdCardPortsActionMode':oaLdCardPortsActionMode,'oaLdCardPortsOutputPortId':oaLdCardPortsOutputPortId,'oaLdCardPortsGroupId':oaLdCardPortsGroupId,'oaLdCardPortsChannelId':oaLdCardPortsChannelId,'oaLdCardPortsAutoShutdownMode':oaLdCardPortsAutoShutdownMode,'oaLdCardPortsEymxScnAmpFctr':oaLdCardPortsEymxScnAmpFctr,'oaLdCardPortsEymxScnAmpFctrMin':oaLdCardPortsEymxScnAmpFctrMin,'oaLdCardPortsEymxScnAmpFctrMax':oaLdCardPortsEymxScnAmpFctrMax,'oaLdCardPortsEymxScnDspComps':oaLdCardPortsEymxScnDspComps,'oaLdCardPortsEymxScnTreshold':oaLdCardPortsEymxScnTreshold,'oaLdCardPortsEymxScnOperComplt':oaLdCardPortsEymxScnOperComplt,'oaLdCardPortsEymxScnResult':oaLdCardPortsEymxScnResult,'oaLdAdcCardInfo':oaLdAdcCardInfo,'oaLdAdcCardInfoTable':oaLdAdcCardInfoTable,'oaLdAdcCardInfoEntry':oaLdAdcCardInfoEntry,_A9:oaLdAdcCardSlotNumber,'oaLdAdcCardNumberOfPorts':oaLdAdcCardNumberOfPorts,'oaLdAdcCardWdmWaveLength':oaLdAdcCardWdmWaveLength,'oaLdAdcCardCardType':oaLdAdcCardCardType,'oaLdAdcCardSpacing':oaLdAdcCardSpacing,'oaLdAdcCardSubBand':oaLdAdcCardSubBand,'oaLdAdcCardChannelsPerPort':oaLdAdcCardChannelsPerPort,'oaLdAdcCardPortsInfoTable':oaLdAdcCardPortsInfoTable,'oaLdAdcCardPortsInfoEntry':oaLdAdcCardPortsInfoEntry,_AA:oaLdAdcCardPortsSlotNumber,_AB:oaLdAdcCardPortsPortNumber,'oaLdAdcCardPortsLambdaCh':oaLdAdcCardPortsLambdaCh,'oaLdCardChannelInfo':oaLdCardChannelInfo,'oaLdCardChannelCfgTable':oaLdCardChannelCfgTable,'oaLdCardChannelCfgEntry':oaLdCardChannelCfgEntry,_AC:oaLdCardChSlotId,_AD:oaLdCardChGroupId,_AE:oaLdCardChChannelId,'oaLdCardChOdu1Index':oaLdCardChOdu1Index,'oaLdCardChOdu1TsIndex':oaLdCardChOdu1TsIndex,'oaLdCardChOdu1TsSize':oaLdCardChOdu1TsSize,'oaLdCardChRate':oaLdCardChRate,'oaLdOAmplifierInfo':oaLdOAmplifierInfo,'oaLdOAmplifierCardInfoTable':oaLdOAmplifierCardInfoTable,'oaLdOAmplifierCardInfoEntry':oaLdOAmplifierCardInfoEntry,_r:oaLdOAmplifierCardSlotNumber,'oaLdOAmplifierCardConfiguration':oaLdOAmplifierCardConfiguration,'oaLdOAmplifierCardModuleType':oaLdOAmplifierCardModuleType,'oaLdOAmplifierCardHardwareVersion':oaLdOAmplifierCardHardwareVersion,'oaLdOAmplifierCardSoftwareVersion':oaLdOAmplifierCardSoftwareVersion,'oaLdOAmplifierCardSerialNumber':oaLdOAmplifierCardSerialNumber,'oaLdOAmplifierCardTemperature':oaLdOAmplifierCardTemperature,'oaLdOAmplifierCardPSVoltage':oaLdOAmplifierCardPSVoltage,'oaLdOAmplifierCardPump1Current':oaLdOAmplifierCardPump1Current,'oaLdOAmplifierCardPump1MaxCurrent':oaLdOAmplifierCardPump1MaxCurrent,'oaLdOAmplifierCardPump2Current':oaLdOAmplifierCardPump2Current,'oaLdOAmplifierCardPump2MaxCurrent':oaLdOAmplifierCardPump2MaxCurrent,'oaLdOAmplifierCardInputPower':oaLdOAmplifierCardInputPower,'oaLdOAmplifierCardOutputPower':oaLdOAmplifierCardOutputPower,'oaLdOAmplifierCardModuleGain':oaLdOAmplifierCardModuleGain,'oaLdOAmplifierCardPump1Power':oaLdOAmplifierCardPump1Power,'oaLdOAmplifierCardPump2Power':oaLdOAmplifierCardPump2Power,'oaLdOAmplifierCardMaximumPower':oaLdOAmplifierCardMaximumPower,'oaLdOAmplifierCardRatedGain':oaLdOAmplifierCardRatedGain,'oaLdOAmplifierCardAlarmStatus':oaLdOAmplifierCardAlarmStatus,'oaLdOAmplifierCardAttributes':oaLdOAmplifierCardAttributes,'oaLdOAmplifierCardOperationMode':oaLdOAmplifierCardOperationMode,'oaLdOAmplifierCardRunMode':oaLdOAmplifierCardRunMode,'oaLdOAmplifierCardAutoShutdownState':oaLdOAmplifierCardAutoShutdownState,'oaLdOAmplifierCardInputThreshold':oaLdOAmplifierCardInputThreshold,'oaLdOAmplifierCardOutputThreshold':oaLdOAmplifierCardOutputThreshold,'oaLdOAmplifierCardShutdownThreshold':oaLdOAmplifierCardShutdownThreshold,'oaLdOAmplifierCardLowTempThreshold':oaLdOAmplifierCardLowTempThreshold,'oaLdOAmplifierCardHighTempThreshold':oaLdOAmplifierCardHighTempThreshold,'oaLdOAmplifierCardPump1CurrentSet':oaLdOAmplifierCardPump1CurrentSet,'oaLdOAmplifierCardPump2CurrentSet':oaLdOAmplifierCardPump2CurrentSet,'oaLdOAmplifierCardOutputPowerSet':oaLdOAmplifierCardOutputPowerSet,'oaLdOAmplifierCardGainSet':oaLdOAmplifierCardGainSet,'oaLdOAmplifierCardPumpOutputPower':oaLdOAmplifierCardPumpOutputPower,'oaLdOAmplifierCardReflectedPower':oaLdOAmplifierCardReflectedPower,'oaLdOAmplifierCardBackReflRatio':oaLdOAmplifierCardBackReflRatio,'oaLdOAmplifierCardBackReflThresh':oaLdOAmplifierCardBackReflThresh,'oaLdOAmplifierCardAutoPowerReduction':oaLdOAmplifierCardAutoPowerReduction,'oaLdOAmplifierCardOutputPumpPowerThresh':oaLdOAmplifierCardOutputPumpPowerThresh,'oaLdOAmplifierCardCalibrationFactor':oaLdOAmplifierCardCalibrationFactor,'oaLdOAmplifierCardTempAlarm':oaLdOAmplifierCardTempAlarm,'oaLdOAmplifierCardPump1Ratio':oaLdOAmplifierCardPump1Ratio,'oaLdOAmplifierPumpInfoTable':oaLdOAmplifierPumpInfoTable,'oaLdOAmplifierPumpInfoEntry':oaLdOAmplifierPumpInfoEntry,_AF:oaLdOAmplifierPumpNumber,'oaLdOAmplifierPumpCurrent':oaLdOAmplifierPumpCurrent,'oaLdOAmplifierPumpPower':oaLdOAmplifierPumpPower,'oaLdOAmplifierPumpLaserTemp':oaLdOAmplifierPumpLaserTemp,'oaLdOAmplifierCompInterfaceCount':oaLdOAmplifierCompInterfaceCount,'oaLdOcmCardInfo':oaLdOcmCardInfo,'oaLdOcmCardPortsInfoTable':oaLdOcmCardPortsInfoTable,'oaLdOcmCardPortsInfoEntry':oaLdOcmCardPortsInfoEntry,_AG:oaLdOcmCardPortsSlotNumber,_AH:oaLdOcmCardPortsPortNumber,'oaLdOcmCardPortsSectionLof':oaLdOcmCardPortsSectionLof,'oaLdOcmCardPortsSectionLos':oaLdOcmCardPortsSectionLos,'oaLdOcmCardPortsSectionLoc':oaLdOcmCardPortsSectionLoc,'oaLdOcmCardPortsSectionB1':oaLdOcmCardPortsSectionB1,'oaLdOcmCardPortsLineAis':oaLdOcmCardPortsLineAis,'oaLdOcmCardPortsLineRdi':oaLdOcmCardPortsLineRdi,'oaLdOcmCardPortsLineB2':oaLdOcmCardPortsLineB2,'oaLdOcmCardPortsLineFebe':oaLdOcmCardPortsLineFebe,'oaLdOcmCardPortsPathAis':oaLdOcmCardPortsPathAis,'oaLdOcmCardPortsPathLop':oaLdOcmCardPortsPathLop,'oaLdOcmCardPortsPathB3':oaLdOcmCardPortsPathB3,'oaLdOcmCardPortsPathPse':oaLdOcmCardPortsPathPse,'oaLdOcmCardPortsPathNse':oaLdOcmCardPortsPathNse,'oaLdRoadmInfo':oaLdRoadmInfo,'oaLdRoadmInfoTable':oaLdRoadmInfoTable,'oaLdRoadmInfoEntry':oaLdRoadmInfoEntry,_AI:oaLdRoadmSlotNumber,'oaLdRoadmType':oaLdRoadmType,'oaLdRoadmDescription':oaLdRoadmDescription,'oaLdRoadmSerialNumber':oaLdRoadmSerialNumber,'oaLdRoadmBoardVersion':oaLdRoadmBoardVersion,'oaLdRoadmFpgaVersion':oaLdRoadmFpgaVersion,'oaLdRoadmBootVersion':oaLdRoadmBootVersion,'oaLdRoadmMcVersion':oaLdRoadmMcVersion,'oaLdRoadmDate':oaLdRoadmDate,'oaLdRoadmStatus':oaLdRoadmStatus,'oaLdRoadmComOutPortAdminStatus':oaLdRoadmComOutPortAdminStatus,'oaLdRoadmFail':oaLdRoadmFail,'oaLdRoadmTemperature':oaLdRoadmTemperature,'oaLdRoadmHeaterMode':oaLdRoadmHeaterMode,'oaLdRoadmHeaterTemperature':oaLdRoadmHeaterTemperature,'oaLdRoadmSpacing':oaLdRoadmSpacing,'oaLdRoadmNumberOfChPorts':oaLdRoadmNumberOfChPorts,'oaLdRoadmPowerEqualization':oaLdRoadmPowerEqualization,'oaLdRoadmZone2Temperature':oaLdRoadmZone2Temperature,'oaLdRoadmZone3Temperature':oaLdRoadmZone3Temperature,'oaLdRoadmNumberOfChannels':oaLdRoadmNumberOfChannels,'oaLdRoadmReconfigureSwitch':oaLdRoadmReconfigureSwitch,'oaLdRoadmFirstChannel':oaLdRoadmFirstChannel,'oaLdRoadmLastChannel':oaLdRoadmLastChannel,'oaLdRoadmDefaultConfiguration':oaLdRoadmDefaultConfiguration,'oaLdRoadmPowerBalancingMode':oaLdRoadmPowerBalancingMode,'oaLdRoadmMonitorTable':oaLdRoadmMonitorTable,'oaLdRoadmMonitorEntry':oaLdRoadmMonitorEntry,_AK:oaLdRoadmMonitorSlotNumber,'oaLdRoadmMonitorComInputPower':oaLdRoadmMonitorComInputPower,'oaLdRoadmMonitorComOutputPower':oaLdRoadmMonitorComOutputPower,'oaLdRoadmMonitorExpInputPower':oaLdRoadmMonitorExpInputPower,'oaLdRoadmMonitorExpOutputPower':oaLdRoadmMonitorExpOutputPower,'oaLdRoadmMonitorDropOutputPower':oaLdRoadmMonitorDropOutputPower,'oaLdRoadmChannelTable':oaLdRoadmChannelTable,'oaLdRoadmChannelEntry':oaLdRoadmChannelEntry,_AL:oaLdRoadmChannelSlotNumber,_AM:oaLdRoadmChannelLambdaChannel,_AN:oaLdRoadmChannelPortNumber,'oaLdRoadmChannelWavelength':oaLdRoadmChannelWavelength,'oaLdRoadmChannelDropPortNumber':oaLdRoadmChannelDropPortNumber,'oaLdRoadmChannelDropAttenuation':oaLdRoadmChannelDropAttenuation,'oaLdRoadmChannelConfigStatus':oaLdRoadmChannelConfigStatus,'oaLdRoadmChannelPower1':oaLdRoadmChannelPower1,'oaLdRoadmChannelPower2':oaLdRoadmChannelPower2,'oaLdRoadmChannelDropPeakFrequency':oaLdRoadmChannelDropPeakFrequency,'oaLdRoadmChannelAddPeakFrequency':oaLdRoadmChannelAddPeakFrequency,'oaLdRoadmChannelAddAttenuation':oaLdRoadmChannelAddAttenuation,'oaLdRoadmChannelGridFrequency':oaLdRoadmChannelGridFrequency,'oaLdRoadmChannelSpacing':oaLdRoadmChannelSpacing,'oaLdRoadmThresholdTable':oaLdRoadmThresholdTable,'oaLdRoadmThresholdEntry':oaLdRoadmThresholdEntry,_AO:oaLdRoadmThresholdSlotNumber,_AP:oaLdRoadmThresholdIndex,'oaLdRoadmThresholdAwgTemp':oaLdRoadmThresholdAwgTemp,'oaLdRoadmThresholdTemp':oaLdRoadmThresholdTemp,'oaLdRoadmThresholdComInputPwr':oaLdRoadmThresholdComInputPwr,'oaLdRoadmThresholdComOutputPwr':oaLdRoadmThresholdComOutputPwr,'oaLdRoadmThresholdExpInputPwr':oaLdRoadmThresholdExpInputPwr,'oaLdRoadmThresholdExpOutputPwr':oaLdRoadmThresholdExpOutputPwr,'oaLdRoadmThresholdDropOutputPwr':oaLdRoadmThresholdDropOutputPwr,'oaLdRoadmPortInfoTable':oaLdRoadmPortInfoTable,'oaLdRoadmPortInfoEntry':oaLdRoadmPortInfoEntry,_AW:oaLdRoadmPortSlotNumber,_AX:oaLdRoadmPortPortNumber,'oaLdRoadmPortAdminState':oaLdRoadmPortAdminState,'oaLdRoadmPortServiceState':oaLdRoadmPortServiceState,'oaLdRoadmPortPower':oaLdRoadmPortPower,'oaLdRoadmPortVoaAttenuationAdd':oaLdRoadmPortVoaAttenuationAdd,'oaLdRoadmPortVoaAttenuationPass':oaLdRoadmPortVoaAttenuationPass,'oaLdRoadmPortVoaAttenuationDrop':oaLdRoadmPortVoaAttenuationDrop,'oaLdRoadmPortChannelWavelength':oaLdRoadmPortChannelWavelength,'oaLdRoadmPortLambdaChannel':oaLdRoadmPortLambdaChannel,'oaLdRoadmPortVoaMinAttenuation':oaLdRoadmPortVoaMinAttenuation,'oaLdRoadmPortVoaMaxAttenuation':oaLdRoadmPortVoaMaxAttenuation,'oaLdRoadmPortName':oaLdRoadmPortName,'oaLdRoadmPortPowerSupported':oaLdRoadmPortPowerSupported,'oaLdRoadmPortTotalPower':oaLdRoadmPortTotalPower,'oaLdRoadmPortChanList':oaLdRoadmPortChanList,'oaLdRoadmPortChanSrcPortList':oaLdRoadmPortChanSrcPortList,'oaLdRoadmPortBalancingAdminStatus':oaLdRoadmPortBalancingAdminStatus,'oaLdRoadmPortBalancingOperStatus':oaLdRoadmPortBalancingOperStatus,'oaLdRoadmPortBalancingPower':oaLdRoadmPortBalancingPower,'oaLdRoadmPortBalancingMaxChnlsNum':oaLdRoadmPortBalancingMaxChnlsNum,'oaLdRoadmPortBalancingPowerPerChnl':oaLdRoadmPortBalancingPowerPerChnl,'oaLdRoadmPortThresholdTable':oaLdRoadmPortThresholdTable,'oaLdRoadmPortThresholdEntry':oaLdRoadmPortThresholdEntry,_AY:oaLdRoadmPortThresholdSlotIndex,_AZ:oaLdRoadmPortThresholdPortIndex,_Aa:oaLdRoadmPortThresholdIndex,'oaLdRoadmPortThresholdPwr':oaLdRoadmPortThresholdPwr,'oaLdPortsCrossConnect':oaLdPortsCrossConnect,'oaLdPortsCrossConnectTable':oaLdPortsCrossConnectTable,'oaLdPortsCrossConnectEntry':oaLdPortsCrossConnectEntry,_Ab:oaLdPortsCrossConnectSlotNumber,_Ac:oaLdPortsCrossConnectPortNumber,'oaLdPortsCrossConnectNumber':oaLdPortsCrossConnectNumber,'oaLdPortsCrossConnectAction':oaLdPortsCrossConnectAction,'oaLdOpticalMonitor':oaLdOpticalMonitor,'oaLdMeasurmentPointsTable':oaLdMeasurmentPointsTable,'oaLdMeasurmentPointsEntry':oaLdMeasurmentPointsEntry,_Ad:oaLdMeasurmentPointsSlotNumber,_Ae:oaLdMeasurmentPointsPortNumber,'oaLdPeaksNumber':oaLdPeaksNumber,'oaLdTotalBandPower':oaLdTotalBandPower,'oaLdPeaksMonitorTable':oaLdPeaksMonitorTable,'oaLdPeaksMonitorEntry':oaLdPeaksMonitorEntry,_Af:oaLdPeaksMonitorSlotNumber,_Ag:oaLdPeaksMonitorPortNumber,_Ah:oaLdPeaksMonitorPeakNumber,'oaLdPeaksMonitorPeakFreq':oaLdPeaksMonitorPeakFreq,'oaLdPeaksMonitorPeakWavelength':oaLdPeaksMonitorPeakWavelength,'oaLdPeaksMonitorPeakPower':oaLdPeaksMonitorPeakPower,'oaLdPeaksMonitorTotalPower':oaLdPeaksMonitorTotalPower,'oaLdPeaksMonitorOsnr':oaLdPeaksMonitorOsnr,'oaLdPeaksMonitorLeftValleyFreq':oaLdPeaksMonitorLeftValleyFreq,'oaLdPeaksMonitorLeftValleyPower':oaLdPeaksMonitorLeftValleyPower,'oaLdPeaksMonitorRightValleyFreq':oaLdPeaksMonitorRightValleyFreq,'oaLdPeaksMonitorRightValleyPower':oaLdPeaksMonitorRightValleyPower,'oaLdDcmCardAttributes':oaLdDcmCardAttributes,'oaLdDcmCardPortsTable':oaLdDcmCardPortsTable,'oaLdDcmCardPortsEntry':oaLdDcmCardPortsEntry,_Ai:oaLdDcmCardPortsSlotNumber,_Aj:oaLdDcmCardPortsPortNumber,'oaLdDcmCardPortsDistance':oaLdDcmCardPortsDistance,'oaLdDcmCardPortsSpacing':oaLdDcmCardPortsSpacing,'oaLdDcmCardPortsRate':oaLdDcmCardPortsRate})