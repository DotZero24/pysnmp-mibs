_AZ='infnAuditEventNotification'
_AY='infnSecurityEventNotification'
_AX='infnAdminEventNotification'
_AW='infnTcaNotification'
_AV='infnAlarmNotification'
_AU='tcaCategory'
_AT='alarmCategory'
_AS='saNonServiceAffecting'
_AR='saServiceAffecting'
_AQ='saUnknown'
_AP='softwareProcessing'
_AO='equipment'
_AN='environmental'
_AM='qualityOfService'
_AL='communication'
_AK='psNotReported'
_AJ='psCleared'
_AI='psWarning'
_AH='psCritical'
_AG='psIndeterminate'
_AF='infnSecurityMessage'
_AE='infnSecurityEventTime'
_AD='infnSecurityHostInfo'
_AC='infnSecuritySourceOid'
_AB='infnSecurityObjectAid'
_AA='infnSecurityObjectType'
_A9='infnSecurityNodeName'
_A8='infnSecurityNodeId'
_A7='infnAuditParamsList'
_A6='infnAuditOperationStatus'
_A5='infnAuditOperationName'
_A4='infnAuditTime'
_A3='infnAuditHostInfo'
_A2='infnAuditUserId'
_A1='infnAuditSourceOid'
_A0='infnAuditObjectAid'
_z='infnAuditObjectType'
_y='infnAuditNodeName'
_x='infnAuditNodeId'
_w='infnAdminCause'
_v='infnAdminEventTime'
_u='infnAdminSourceOid'
_t='infnAdminObjectAid'
_s='infnAdminObjectType'
_r='infnAdminNodeName'
_q='infnAdminNodeId'
_p='tcaAdditionalText'
_o='tcaProbableCauseDescription'
_n='tcaTimePeriod'
_m='tcaThresholdValue'
_l='tcaMonitoredValue'
_k='tcaDirection'
_j='tcaLocation'
_i='tcaOccurrenceTime'
_h='tcaServiceAffecting'
_g='tcaSeverity'
_f='tcaProbableCause'
_e='tcaSourceOid'
_d='tcaObjectAid'
_c='tcaObjectType'
_b='tcaNodeName'
_a='tcaNodeId'
_Z='alarmCorrelationId'
_Y='alarmAdditionalText'
_X='alarmProbableCauseDescription'
_W='alarmDirection'
_V='alarmLocation'
_U='alarmOccurrenceTime'
_T='alarmServiceAffecting'
_S='alarmSeverity'
_R='alarmProbableCause'
_Q='alarmSourceOid'
_P='alarmObjectAid'
_O='alarmObjectType'
_N='alarmNodeName'
_M='alarmNodeId'
_L='infnSecurityNotificationId'
_K='infnAuditNotificationId'
_J='infnAdminNotificationId'
_I='tcaNotificationId'
_H='notApplicable'
_G='alarmNotificationId'
_F='accessible-for-notify'
_E='DisplayString'
_D='Integer32'
_C='read-only'
_B='current'
_A='INFINERA-NOTIFICATION-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
common,=mibBuilder.importSymbols('INFINERA-REG-MIB','common')
InfnManagedObjectType,=mibBuilder.importSymbols('INFINERA-TC-MIB','InfnManagedObjectType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','TextualConvention')
infnNotifications=ModuleIdentity((1,3,6,1,4,1,21296,2,2,1,2))
_InfnNotificationConformance_ObjectIdentity=ObjectIdentity
infnNotificationConformance=_InfnNotificationConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,1,2,16))
_InfnNotificationObjectGroups_ObjectIdentity=ObjectIdentity
infnNotificationObjectGroups=_InfnNotificationObjectGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,1,2,16,1))
_InfnNotificationNotifGroups_ObjectIdentity=ObjectIdentity
infnNotificationNotifGroups=_InfnNotificationNotifGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,1,2,16,2))
_InfnAlarmTable_Object=MibTable
infnAlarmTable=_InfnAlarmTable_Object((1,3,6,1,4,1,21296,2,2,1,3))
if mibBuilder.loadTexts:infnAlarmTable.setStatus(_B)
_InfnAlarmEntry_Object=MibTableRow
infnAlarmEntry=_InfnAlarmEntry_Object((1,3,6,1,4,1,21296,2,2,1,3,1))
infnAlarmEntry.setIndexNames((0,_A,_G))
if mibBuilder.loadTexts:infnAlarmEntry.setStatus(_B)
class _AlarmNotificationId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AlarmNotificationId_Type.__name__=_D
_AlarmNotificationId_Object=MibTableColumn
alarmNotificationId=_AlarmNotificationId_Object((1,3,6,1,4,1,21296,2,2,1,3,1,1),_AlarmNotificationId_Type())
alarmNotificationId.setMaxAccess(_F)
if mibBuilder.loadTexts:alarmNotificationId.setStatus(_B)
class _AlarmNodeId_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_AlarmNodeId_Type.__name__=_E
_AlarmNodeId_Object=MibTableColumn
alarmNodeId=_AlarmNodeId_Object((1,3,6,1,4,1,21296,2,2,1,3,1,2),_AlarmNodeId_Type())
alarmNodeId.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmNodeId.setStatus(_B)
class _AlarmNodeName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_AlarmNodeName_Type.__name__=_E
_AlarmNodeName_Object=MibTableColumn
alarmNodeName=_AlarmNodeName_Object((1,3,6,1,4,1,21296,2,2,1,3,1,3),_AlarmNodeName_Type())
alarmNodeName.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmNodeName.setStatus(_B)
_AlarmObjectType_Type=InfnManagedObjectType
_AlarmObjectType_Object=MibTableColumn
alarmObjectType=_AlarmObjectType_Object((1,3,6,1,4,1,21296,2,2,1,3,1,4),_AlarmObjectType_Type())
alarmObjectType.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmObjectType.setStatus(_B)
_AlarmObjectAid_Type=DisplayString
_AlarmObjectAid_Object=MibTableColumn
alarmObjectAid=_AlarmObjectAid_Object((1,3,6,1,4,1,21296,2,2,1,3,1,5),_AlarmObjectAid_Type())
alarmObjectAid.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmObjectAid.setStatus(_B)
_AlarmSourceOid_Type=ObjectIdentifier
_AlarmSourceOid_Object=MibTableColumn
alarmSourceOid=_AlarmSourceOid_Object((1,3,6,1,4,1,21296,2,2,1,3,1,6),_AlarmSourceOid_Type())
alarmSourceOid.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmSourceOid.setStatus(_B)
class _AlarmProbableCause_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,164,165,166,200,201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226,227,228,229,230,231,232,233,234,235,236,237,238,239,240,241,242,243,244,245,246,247,248,249,250,251,300,301,303,304,305,306,307,308,309,310,311,312,313,314,315,316,317,318,319,320,321,322,323,324,325,326,327,328,329,330,331,332,333,334,340,341,342,343,500,501,502,503,504,505,506,507,508,509,510,511,512,513,514,515,516,517,518,519,532,533,535,536,537,538,539,540,541,542,543,544,545,546,547,548,549,550,551,552,554,556,557,558,559,560,561,562,563,564,565,566,567,568,569,570,571,572,573,574,575,576,577,578,579,580,581,582,583,584,585,586,587,588,589,590,591,592,593,595,596,597,598,599,600,601,602,603,604,605,606,700,701,702,703,704,705,706,707,708,709,710,711,712,713,714,715)));namedValues=NamedValues(*(('adminLock',1),('adminMaint',2),('adsrup',3),('adTimeout',4),('ais-dtp',5),('ais-l',6),('ais-ms',7),('alsDisabled',8),('ambientTempOorh',9),('aupfail',10),('auxEnetLoLinkCtrlA',11),('auxEnetLoLinkCtrlB',12),('bdi',13),('bdi-dtp',14),('backupMemoryLow',15),('backupMemoryVeryLow',16),('branMsmt',17),('breakerOpen48v',18),('ctrlCommFailA',19),('ctrlCommFailB',20),('dbMsmt',21),('dbRestoreFail',22),('dbRestoreFailReboot',23),('dcnEnetLoLinkCtrlA',24),('dcnEnetLoLinkCtrlB',25),('deEncapAis-l',26),('deEncapAis-ms',27),('deEncapLof',28),('deEncapLos',29),('deEncapLossOfSync',30),('eqpPer1',31),('eqpPer2',32),('eqpPer3',33),('eqptPartFail',34),('eqptProtFailSlot3',35),('eqptProtFailSlot4',36),('eqptProtFailSlot5',37),('eqptProtFailSlot6',38),('eqptCpReset',39),('eqptCpUr',40),('eqptDegrade',41),('eqptFail',42),('eqptMsmt',43),('excessiveChannels',44),('gmplsConfigMismatch',45),('gmplsNbrDown',46),('impropRmvl',47),('initFail',48),('insufficientGain',49),('interOamMisConn',50),('lineTestSigGen',51),('lineTestSigOos',52),('loa',53),('loc',54),('lockOutOfPr',55),('lockOutOfWk',56),('lof',57),('los',58),('lossOfSync',59),('lpbkFacility',60),('lpbkTerm',61),('misConn',62),('misConfigIpAddr',63),('nbrsOscIpAddrConflict',64),('nct1EnetLolinkCtrlA',65),('nct1EnetLolinkCtrlB',66),('nct2EnetLolinkCtrlA',67),('nct2EnetLolinkCtrlB',68),('ntpServerLoss',69),('nwDuplicateMeName',70),('nwDuplicateNbr',71),('nwDuplicateRouterId',72),('olOorh',73),('olos',74),('oprOorh',75),('oprOorl',76),('optOorh',77),('optOorl',78),('oscCommFailA',79),('oscCommFailB',80),('oscIpAddrDuplicate',81),('gccIpAddrSubnetMsmt',82),('peerCtrlCommFail',83),('plm',84),('postFecBerSf',85),('prbsGen',86),('prbsOos',87),('preFecBerSd',88),('pwrAdjustIncomplete',89),('power48vFail',90),('pwrLoopDisabled',91),('rfi-l',92),('rfi-ms',93),('spanLossOorh',94),('spanLossOorl',95),('sncFail',96),('sncSetupFail',97),('swInstallFail',98),('swUpgradeFail',99),('swUpgradeFailBootup',100),('tempOorDeviceShutdown',101),('tempOorh',102),('tempOorhRxPicShutdown',103),('tempOorhTxPicShutdown',104),('tempOorl',105),('tim-dtp',106),('tim-dts',107),('tim-s',108),('tribPrbsGen',109),('tribPrbsOos',110),('tribTestSigGen',111),('tribTestSigOos',112),('txfrPriFail',113),('txfrPriFailSna',114),('txfrsFail',115),('unknownFw',116),('powerDrawExceeded',117),('connectivityFail',118),('gccGmplsCfgMsmt',119),('gccGmplsNbrDown',120),('gccIPaddrDuplicate',121),('nbrsGccIPaddrInConflict',122),('ocgMismatch',123),('powerControl',124),('greTunnelAddressMismatch',125),('noManagementRedundancy',126),('lolm',127),('deEncapLolm',128),('oloorh',129),('ochMismatch',130),('switchBackToWrk',131),('manualSwitchBackToWrk',132),('wtrStart',133),('spectrumNotAttained',134),('incompatibleDse',135),('tempOorhDevAutoShutdown',136),('rmtChnlMismatch',137),('equipmentInit',138),('adminXfrReqDrop',139),('adminDBCurrupt',140),('adminRestoreFailed',141),('txfr-sec-fail',142),('optTooLow',143),('equipmentUnsupported',144),('ccmLoc',145),('ccmUnexpLevel',146),('ccmMisMerge',147),('ccmUnexpMep',148),('ccmUnexpPeriod',149),('ccmUnexpPrio',150),('ccmRemMacErr',151),('ethRdi',152),('ethAis',153),('vsiFail',154),('vsiPartialFail',155),('vsiMacLimit',156),('macFlap',157),('acMacLimit',158),('cacFail',159),('cacUnavail',160),('freqProvPending',161),('vsiMacLimDnlDnf',162),('intra-sch-carrier-ripple-high',164),('tx-tim',165),('rx-tim',166),('airCompressorFailure',200),('airConditioningFailure',201),('airDryerFailure',202),('batteryDischarging',203),('batteryFailure',204),('coolingFanFailure',205),('centralPowerFailureMajor',206),('centralPowerFailureMinor',207),('engineFailure',208),('engineOperating',209),('explosiveGas',210),('fireDetectorFailure',211),('fire',212),('flood',213),('fuseFailure',214),('generatorFailure',215),('highAirFlow',216),('highHumidity',217),('highTemperature',218),('highWater',219),('intrusion',220),('lowBatteryVoltage',221),('lowFuel',222),('lowHumidity',223),('lowCablePressure',224),('lowTemperature',225),('lowWater',226),('misc',227),('openDoor',228),('pumpFailure',229),('commercialPowerFailure',230),('power-xFailure',231),('rectifierFailure',232),('rectifierHighVoltage',233),('rectifierLowVoltage',234),('smoke',235),('toxicGas',236),('ventilationSystemFailure',237),('linePrbsGen',238),('ais',239),('deg',240),('linePrbsOos',241),('lck',242),('oci',243),('oldRevCtrlr',244),('protUnitAct',245),('misConfig',246),('lsActive',247),('deEncapAis-p',248),('rstPathAct',249),('ltc',250),('automaticGainCtrlNotFunctioning',251),('slOorh',300),('slOorl',301),('gainOorh',303),('gainOorl',304),('insufficientChanPower',305),('uSupportedTom',306),('ncLolink',307),('chassisMisconn',308),('dcnLolink',309),('loLink',310),('none',311),('unknownEqpt',312),('outputPwrFailure',313),('inputPwrFailure',314),('dropBandOptLow',315),('timOtu',316),('dropBandOprOorLow',317),('dropBandOprOorHigh',318),('dropBandOptOorLow',319),('dropBandOptOorHigh',320),('dropBandOLOS',321),('bandOptTooLow',322),('bandOptOorLow',323),('bandOptOorHigh',324),('bandOprOorLow',325),('bandOprOorHigh',326),('insufficientAttenuation',327),('oprOorHighOscDisabled',328),('switchToPr',329),('manualSwitchToPr',330),('adaptCommitPending',331),('txFail',332),('ntpAuthFail',333),('lowCh',334),('rf',340),('lf',341),('deEncapLf',342),('deEncapRf',343),('eqptProtFailSlot1',500),('eqptProtFailSlot2',501),('eqptProtFailSlot7',502),('eqptProtFailSlot8',503),('eqptProtFailSlot9',504),('eqptProtFailSlot10',505),('powerProtectionFail',506),('lossOfFrameDelineation',507),('upiMismatch',508),('exiMismatch',509),('clientSignalFail',510),('tsmUnavailable',511),('noTsmRedundancy',512),('switchFabricFailure',513),('switchProtUnavailable',514),('timingSourceMismatch',515),('muxStructureIdMismatch',516),('powerVoltageOver',517),('powerVoltageUnder',518),('oscMisConnection',519),('remmodMismatch',532),('rx-EDFA-SPLIM',533),('lockedSyncSourceActive',535),('rxOPRTooLow',536),('commFailLink',537),('deEncapLoa',538),('configMismatch',539),('lossOfFrameLossOfMultiFrame',540),('lockedSwitchModuleActive',541),('operatingModeMismatch',542),('powerCtrlInitiated',543),('lossOfMultiFrame',544),('degradedConfig',545),('licAssignmentMsmt',546),('licInsufficiency',547),('licModFmtMsmt',548),('licNwAuditMsMt',549),('shelfDbCorrupt',550),('tx-lossOfMultiFrame',551),('lossOfFrameLogicalLane',552),('lossOfLaneAllignment',554),('igccFail',556),('encmodeChangePending',557),('remPortFecMsmt',558),('aisOdu-ipath',559),('bdiOdu-ipath',560),('remPortEncModeMsmt',561),('pmdOorHigh',562),('flashFail',563),('preFecQSigDegrade',564),('flashRedundancyNotAvailable',565),('schMisConn',566),('opt-too-low',567),('forwarddefectindicationoverhead',568),('forwarddefectindicationpayload',569),('migrationfailed',570),('backwardDefectIndicationS',571),('openconnectionIndication',572),('remSchParamMsmt',573),('schNumMismatch',574),('payloadMissingIndication',575),('backwardDefectIndicationPayloadO',576),('muxOprOorl',577),('txPayloadMisMatchODUk',578),('lossOfOpuMultiFrameIdentifier',579),('serviceStateOOSAU',580),('odukPELatencyFacilityOorh',581),('odukPELatencyFacilityOorl',582),('odukPELatencyTerminalOorh',583),('odukPELatencyTerminalOorl',584),('odukPSLatencyFacilityOorh',585),('odukPSLatencyFacilityOorl',586),('odukPSLatencyTerminalOorh',587),('odukPSLatencyTerminalOorl',588),('insufficientTrgtOutPwr',589),('backwardDefectIndication',590),('backwardDefectIndicationPayload',591),('mainPowerFailure',592),('pemTypMismatch',593),('gccOspfNbrDown',595),('gccIpSubnetMismatch',596),('gccIpConflict',597),('gccOspfConfigMismatch',598),('greAddressMismatch',599),('rem-sch-parameters-msmt',600),('opr-too-high',601),('opr-too-low',602),('opr-oorl',603),('opr-oorh',604),('opt-oorl',605),('opt-oorh',606),('ocgTTIMsmt',700),('ocgReachThWarn',701),('ocgReachThExceed',702),('tx-olos',703),('pemGLUnavailable',704),('registrationRequired',705),('registrationExpired',706),('registrationRequiredMJ',707),('ttiMismatchXtSCH',708),('ethCsf',709),('linkDown',710),('maint-req',711),('gccFail',712),('rxBDI',713),('sbsOff',714),('idlerSeparationOor',715)))
_AlarmProbableCause_Type.__name__=_D
_AlarmProbableCause_Object=MibTableColumn
alarmProbableCause=_AlarmProbableCause_Object((1,3,6,1,4,1,21296,2,2,1,3,1,7),_AlarmProbableCause_Type())
alarmProbableCause.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmProbableCause.setStatus(_B)
class _AlarmSeverity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_AG,1),(_AH,2),('psMajor',3),('psMinor',4),(_AI,5),(_AJ,6),(_AK,7)))
_AlarmSeverity_Type.__name__=_D
_AlarmSeverity_Object=MibTableColumn
alarmSeverity=_AlarmSeverity_Object((1,3,6,1,4,1,21296,2,2,1,3,1,8),_AlarmSeverity_Type())
alarmSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmSeverity.setStatus(_B)
class _AlarmCategory_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('unknown',1),(_AL,2),(_AM,3),(_AN,4),(_AO,5),(_AP,6),('facility',7),('software',8)))
_AlarmCategory_Type.__name__=_D
_AlarmCategory_Object=MibTableColumn
alarmCategory=_AlarmCategory_Object((1,3,6,1,4,1,21296,2,2,1,3,1,9),_AlarmCategory_Type())
alarmCategory.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmCategory.setStatus(_B)
class _AlarmServiceAffecting_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_AQ,1),(_AR,2),(_AS,3)))
_AlarmServiceAffecting_Type.__name__=_D
_AlarmServiceAffecting_Object=MibTableColumn
alarmServiceAffecting=_AlarmServiceAffecting_Object((1,3,6,1,4,1,21296,2,2,1,3,1,10),_AlarmServiceAffecting_Type())
alarmServiceAffecting.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmServiceAffecting.setStatus(_B)
_AlarmOccurrenceTime_Type=DisplayString
_AlarmOccurrenceTime_Object=MibTableColumn
alarmOccurrenceTime=_AlarmOccurrenceTime_Object((1,3,6,1,4,1,21296,2,2,1,3,1,11),_AlarmOccurrenceTime_Type())
alarmOccurrenceTime.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmOccurrenceTime.setStatus(_B)
class _AlarmLocation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('nearEnd',1),('farEnd',2),(_H,3)))
_AlarmLocation_Type.__name__=_D
_AlarmLocation_Object=MibTableColumn
alarmLocation=_AlarmLocation_Object((1,3,6,1,4,1,21296,2,2,1,3,1,12),_AlarmLocation_Type())
alarmLocation.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmLocation.setStatus(_B)
class _AlarmDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('receive',1),('transmit',2),(_H,3)))
_AlarmDirection_Type.__name__=_D
_AlarmDirection_Object=MibTableColumn
alarmDirection=_AlarmDirection_Object((1,3,6,1,4,1,21296,2,2,1,3,1,13),_AlarmDirection_Type())
alarmDirection.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmDirection.setStatus(_B)
class _AlarmProbableCauseDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_AlarmProbableCauseDescription_Type.__name__=_E
_AlarmProbableCauseDescription_Object=MibTableColumn
alarmProbableCauseDescription=_AlarmProbableCauseDescription_Object((1,3,6,1,4,1,21296,2,2,1,3,1,14),_AlarmProbableCauseDescription_Type())
alarmProbableCauseDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmProbableCauseDescription.setStatus(_B)
_AlarmAdditionalText_Type=DisplayString
_AlarmAdditionalText_Object=MibTableColumn
alarmAdditionalText=_AlarmAdditionalText_Object((1,3,6,1,4,1,21296,2,2,1,3,1,15),_AlarmAdditionalText_Type())
alarmAdditionalText.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmAdditionalText.setStatus(_B)
class _AlarmCorrelationId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AlarmCorrelationId_Type.__name__=_D
_AlarmCorrelationId_Object=MibTableColumn
alarmCorrelationId=_AlarmCorrelationId_Object((1,3,6,1,4,1,21296,2,2,1,3,1,16),_AlarmCorrelationId_Type())
alarmCorrelationId.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmCorrelationId.setStatus(_B)
_InfnTcaTable_Object=MibTable
infnTcaTable=_InfnTcaTable_Object((1,3,6,1,4,1,21296,2,2,1,4))
if mibBuilder.loadTexts:infnTcaTable.setStatus(_B)
_InfnTcaEntry_Object=MibTableRow
infnTcaEntry=_InfnTcaEntry_Object((1,3,6,1,4,1,21296,2,2,1,4,1))
infnTcaEntry.setIndexNames((0,_A,_I))
if mibBuilder.loadTexts:infnTcaEntry.setStatus(_B)
class _TcaNotificationId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_TcaNotificationId_Type.__name__=_D
_TcaNotificationId_Object=MibTableColumn
tcaNotificationId=_TcaNotificationId_Object((1,3,6,1,4,1,21296,2,2,1,4,1,1),_TcaNotificationId_Type())
tcaNotificationId.setMaxAccess(_F)
if mibBuilder.loadTexts:tcaNotificationId.setStatus(_B)
class _TcaNodeId_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_TcaNodeId_Type.__name__=_E
_TcaNodeId_Object=MibTableColumn
tcaNodeId=_TcaNodeId_Object((1,3,6,1,4,1,21296,2,2,1,4,1,2),_TcaNodeId_Type())
tcaNodeId.setMaxAccess(_C)
if mibBuilder.loadTexts:tcaNodeId.setStatus(_B)
class _TcaNodeName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_TcaNodeName_Type.__name__=_E
_TcaNodeName_Object=MibTableColumn
tcaNodeName=_TcaNodeName_Object((1,3,6,1,4,1,21296,2,2,1,4,1,3),_TcaNodeName_Type())
tcaNodeName.setMaxAccess(_C)
if mibBuilder.loadTexts:tcaNodeName.setStatus(_B)
_TcaObjectType_Type=InfnManagedObjectType
_TcaObjectType_Object=MibTableColumn
tcaObjectType=_TcaObjectType_Object((1,3,6,1,4,1,21296,2,2,1,4,1,4),_TcaObjectType_Type())
tcaObjectType.setMaxAccess(_C)
if mibBuilder.loadTexts:tcaObjectType.setStatus(_B)
_TcaObjectAid_Type=DisplayString
_TcaObjectAid_Object=MibTableColumn
tcaObjectAid=_TcaObjectAid_Object((1,3,6,1,4,1,21296,2,2,1,4,1,5),_TcaObjectAid_Type())
tcaObjectAid.setMaxAccess(_C)
if mibBuilder.loadTexts:tcaObjectAid.setStatus(_B)
_TcaSourceOid_Type=ObjectIdentifier
_TcaSourceOid_Object=MibTableColumn
tcaSourceOid=_TcaSourceOid_Object((1,3,6,1,4,1,21296,2,2,1,4,1,6),_TcaSourceOid_Type())
tcaSourceOid.setMaxAccess(_C)
if mibBuilder.loadTexts:tcaSourceOid.setStatus(_B)
class _TcaProbableCause_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51)));namedValues=NamedValues(*(('cvs',1),('sess',2),('sefss',3),('ess',4),('uass',5),('cvp',6),('sesp',7),('sefsp',8),('esp',9),('uasp',10),('be-rs',11),('es-rs',12),('ses-rs',13),('ofs-rs',14),('loss-rs',15),('icg-pcs',16),('es-pcs',17),('ses-pcs',18),('sess-pcs',19),('jabberSeconds',20),('ses-mac',21),('errorOctets',22),('jabbers',23),('fragments',24),('crcAlignErrors',25),('underSized',26),('overSized',27),('pkts64',28),('pkts65to127',29),('pkts128to255',30),('pkts256to511',31),('pkts512to1023',32),('pkts1024to1518',33),('pkts1519tojumbo',34),('packets',35),('octets',36),('broadcastPkts',37),('multicastPkts',38),('inPauseFrames',39),('outPauseFrames',40),('pkts1024to1522',41),('pkts1523tojumbo',42),('invalidCrcs',43),('frames',44),('erroredFrames',45),('erroredOctets',46),('erroredBlocks',47),('defectSeconds',48),('beiCount',49),('erroredBlocksFarEnd',50),('defectSecondsFarEnd',51)))
_TcaProbableCause_Type.__name__=_D
_TcaProbableCause_Object=MibTableColumn
tcaProbableCause=_TcaProbableCause_Object((1,3,6,1,4,1,21296,2,2,1,4,1,7),_TcaProbableCause_Type())
tcaProbableCause.setMaxAccess(_C)
if mibBuilder.loadTexts:tcaProbableCause.setStatus(_B)
class _TcaSeverity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_AG,1),(_AH,2),('psMajor',3),('psMinor',4),(_AI,5),(_AJ,6),('psEvent',7),(_AK,8)))
_TcaSeverity_Type.__name__=_D
_TcaSeverity_Object=MibTableColumn
tcaSeverity=_TcaSeverity_Object((1,3,6,1,4,1,21296,2,2,1,4,1,8),_TcaSeverity_Type())
tcaSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:tcaSeverity.setStatus(_B)
class _TcaCategory_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('unknown',1),(_AL,2),(_AM,3),(_AN,4),(_AO,5),(_AP,6),('facility',7),('software',8)))
_TcaCategory_Type.__name__=_D
_TcaCategory_Object=MibTableColumn
tcaCategory=_TcaCategory_Object((1,3,6,1,4,1,21296,2,2,1,4,1,9),_TcaCategory_Type())
tcaCategory.setMaxAccess(_C)
if mibBuilder.loadTexts:tcaCategory.setStatus(_B)
class _TcaServiceAffecting_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_AQ,1),(_AR,2),(_AS,3)))
_TcaServiceAffecting_Type.__name__=_D
_TcaServiceAffecting_Object=MibTableColumn
tcaServiceAffecting=_TcaServiceAffecting_Object((1,3,6,1,4,1,21296,2,2,1,4,1,10),_TcaServiceAffecting_Type())
tcaServiceAffecting.setMaxAccess(_C)
if mibBuilder.loadTexts:tcaServiceAffecting.setStatus(_B)
_TcaOccurrenceTime_Type=DisplayString
_TcaOccurrenceTime_Object=MibTableColumn
tcaOccurrenceTime=_TcaOccurrenceTime_Object((1,3,6,1,4,1,21296,2,2,1,4,1,11),_TcaOccurrenceTime_Type())
tcaOccurrenceTime.setMaxAccess(_C)
if mibBuilder.loadTexts:tcaOccurrenceTime.setStatus(_B)
class _TcaLocation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('nearEnd',1),('farEnd',2),(_H,3)))
_TcaLocation_Type.__name__=_D
_TcaLocation_Object=MibTableColumn
tcaLocation=_TcaLocation_Object((1,3,6,1,4,1,21296,2,2,1,4,1,12),_TcaLocation_Type())
tcaLocation.setMaxAccess(_C)
if mibBuilder.loadTexts:tcaLocation.setStatus(_B)
class _TcaDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('receive',1),('transmit',2),(_H,3)))
_TcaDirection_Type.__name__=_D
_TcaDirection_Object=MibTableColumn
tcaDirection=_TcaDirection_Object((1,3,6,1,4,1,21296,2,2,1,4,1,13),_TcaDirection_Type())
tcaDirection.setMaxAccess(_C)
if mibBuilder.loadTexts:tcaDirection.setStatus(_B)
class _TcaMonitoredValue_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_TcaMonitoredValue_Type.__name__=_E
_TcaMonitoredValue_Object=MibTableColumn
tcaMonitoredValue=_TcaMonitoredValue_Object((1,3,6,1,4,1,21296,2,2,1,4,1,14),_TcaMonitoredValue_Type())
tcaMonitoredValue.setMaxAccess(_C)
if mibBuilder.loadTexts:tcaMonitoredValue.setStatus(_B)
class _TcaThresholdValue_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_TcaThresholdValue_Type.__name__=_E
_TcaThresholdValue_Object=MibTableColumn
tcaThresholdValue=_TcaThresholdValue_Object((1,3,6,1,4,1,21296,2,2,1,4,1,15),_TcaThresholdValue_Type())
tcaThresholdValue.setMaxAccess(_C)
if mibBuilder.loadTexts:tcaThresholdValue.setStatus(_B)
class _TcaTimePeriod_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_TcaTimePeriod_Type.__name__=_E
_TcaTimePeriod_Object=MibTableColumn
tcaTimePeriod=_TcaTimePeriod_Object((1,3,6,1,4,1,21296,2,2,1,4,1,16),_TcaTimePeriod_Type())
tcaTimePeriod.setMaxAccess(_C)
if mibBuilder.loadTexts:tcaTimePeriod.setStatus(_B)
class _TcaProbableCauseDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_TcaProbableCauseDescription_Type.__name__=_E
_TcaProbableCauseDescription_Object=MibTableColumn
tcaProbableCauseDescription=_TcaProbableCauseDescription_Object((1,3,6,1,4,1,21296,2,2,1,4,1,17),_TcaProbableCauseDescription_Type())
tcaProbableCauseDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:tcaProbableCauseDescription.setStatus(_B)
_TcaAdditionalText_Type=DisplayString
_TcaAdditionalText_Object=MibTableColumn
tcaAdditionalText=_TcaAdditionalText_Object((1,3,6,1,4,1,21296,2,2,1,4,1,18),_TcaAdditionalText_Type())
tcaAdditionalText.setMaxAccess(_C)
if mibBuilder.loadTexts:tcaAdditionalText.setStatus(_B)
_InfnAdminEventTable_Object=MibTable
infnAdminEventTable=_InfnAdminEventTable_Object((1,3,6,1,4,1,21296,2,2,1,5))
if mibBuilder.loadTexts:infnAdminEventTable.setStatus(_B)
_InfnAdminEventEntry_Object=MibTableRow
infnAdminEventEntry=_InfnAdminEventEntry_Object((1,3,6,1,4,1,21296,2,2,1,5,1))
infnAdminEventEntry.setIndexNames((0,_A,_J))
if mibBuilder.loadTexts:infnAdminEventEntry.setStatus(_B)
_InfnAdminNotificationId_Type=Integer32
_InfnAdminNotificationId_Object=MibTableColumn
infnAdminNotificationId=_InfnAdminNotificationId_Object((1,3,6,1,4,1,21296,2,2,1,5,1,1),_InfnAdminNotificationId_Type())
infnAdminNotificationId.setMaxAccess(_F)
if mibBuilder.loadTexts:infnAdminNotificationId.setStatus(_B)
_InfnAdminNodeId_Type=DisplayString
_InfnAdminNodeId_Object=MibTableColumn
infnAdminNodeId=_InfnAdminNodeId_Object((1,3,6,1,4,1,21296,2,2,1,5,1,2),_InfnAdminNodeId_Type())
infnAdminNodeId.setMaxAccess(_C)
if mibBuilder.loadTexts:infnAdminNodeId.setStatus(_B)
_InfnAdminNodeName_Type=DisplayString
_InfnAdminNodeName_Object=MibTableColumn
infnAdminNodeName=_InfnAdminNodeName_Object((1,3,6,1,4,1,21296,2,2,1,5,1,3),_InfnAdminNodeName_Type())
infnAdminNodeName.setMaxAccess(_C)
if mibBuilder.loadTexts:infnAdminNodeName.setStatus(_B)
_InfnAdminObjectType_Type=InfnManagedObjectType
_InfnAdminObjectType_Object=MibTableColumn
infnAdminObjectType=_InfnAdminObjectType_Object((1,3,6,1,4,1,21296,2,2,1,5,1,4),_InfnAdminObjectType_Type())
infnAdminObjectType.setMaxAccess(_C)
if mibBuilder.loadTexts:infnAdminObjectType.setStatus(_B)
_InfnAdminObjectAid_Type=DisplayString
_InfnAdminObjectAid_Object=MibTableColumn
infnAdminObjectAid=_InfnAdminObjectAid_Object((1,3,6,1,4,1,21296,2,2,1,5,1,5),_InfnAdminObjectAid_Type())
infnAdminObjectAid.setMaxAccess(_C)
if mibBuilder.loadTexts:infnAdminObjectAid.setStatus(_B)
_InfnAdminSourceOid_Type=ObjectIdentifier
_InfnAdminSourceOid_Object=MibTableColumn
infnAdminSourceOid=_InfnAdminSourceOid_Object((1,3,6,1,4,1,21296,2,2,1,5,1,6),_InfnAdminSourceOid_Type())
infnAdminSourceOid.setMaxAccess(_C)
if mibBuilder.loadTexts:infnAdminSourceOid.setStatus(_B)
_InfnAdminEventTime_Type=DisplayString
_InfnAdminEventTime_Object=MibTableColumn
infnAdminEventTime=_InfnAdminEventTime_Object((1,3,6,1,4,1,21296,2,2,1,5,1,7),_InfnAdminEventTime_Type())
infnAdminEventTime.setMaxAccess(_C)
if mibBuilder.loadTexts:infnAdminEventTime.setStatus(_B)
_InfnAdminCause_Type=DisplayString
_InfnAdminCause_Object=MibTableColumn
infnAdminCause=_InfnAdminCause_Object((1,3,6,1,4,1,21296,2,2,1,5,1,8),_InfnAdminCause_Type())
infnAdminCause.setMaxAccess(_C)
if mibBuilder.loadTexts:infnAdminCause.setStatus(_B)
_InfnAuditEventTable_Object=MibTable
infnAuditEventTable=_InfnAuditEventTable_Object((1,3,6,1,4,1,21296,2,2,1,6))
if mibBuilder.loadTexts:infnAuditEventTable.setStatus(_B)
_InfnAuditEventEntry_Object=MibTableRow
infnAuditEventEntry=_InfnAuditEventEntry_Object((1,3,6,1,4,1,21296,2,2,1,6,1))
infnAuditEventEntry.setIndexNames((0,_A,_K))
if mibBuilder.loadTexts:infnAuditEventEntry.setStatus(_B)
_InfnAuditNotificationId_Type=Integer32
_InfnAuditNotificationId_Object=MibTableColumn
infnAuditNotificationId=_InfnAuditNotificationId_Object((1,3,6,1,4,1,21296,2,2,1,6,1,1),_InfnAuditNotificationId_Type())
infnAuditNotificationId.setMaxAccess(_F)
if mibBuilder.loadTexts:infnAuditNotificationId.setStatus(_B)
_InfnAuditNodeId_Type=DisplayString
_InfnAuditNodeId_Object=MibTableColumn
infnAuditNodeId=_InfnAuditNodeId_Object((1,3,6,1,4,1,21296,2,2,1,6,1,2),_InfnAuditNodeId_Type())
infnAuditNodeId.setMaxAccess(_C)
if mibBuilder.loadTexts:infnAuditNodeId.setStatus(_B)
_InfnAuditNodeName_Type=DisplayString
_InfnAuditNodeName_Object=MibTableColumn
infnAuditNodeName=_InfnAuditNodeName_Object((1,3,6,1,4,1,21296,2,2,1,6,1,3),_InfnAuditNodeName_Type())
infnAuditNodeName.setMaxAccess(_C)
if mibBuilder.loadTexts:infnAuditNodeName.setStatus(_B)
_InfnAuditObjectType_Type=InfnManagedObjectType
_InfnAuditObjectType_Object=MibTableColumn
infnAuditObjectType=_InfnAuditObjectType_Object((1,3,6,1,4,1,21296,2,2,1,6,1,4),_InfnAuditObjectType_Type())
infnAuditObjectType.setMaxAccess(_C)
if mibBuilder.loadTexts:infnAuditObjectType.setStatus(_B)
_InfnAuditObjectAid_Type=DisplayString
_InfnAuditObjectAid_Object=MibTableColumn
infnAuditObjectAid=_InfnAuditObjectAid_Object((1,3,6,1,4,1,21296,2,2,1,6,1,5),_InfnAuditObjectAid_Type())
infnAuditObjectAid.setMaxAccess(_C)
if mibBuilder.loadTexts:infnAuditObjectAid.setStatus(_B)
_InfnAuditSourceOid_Type=ObjectIdentifier
_InfnAuditSourceOid_Object=MibTableColumn
infnAuditSourceOid=_InfnAuditSourceOid_Object((1,3,6,1,4,1,21296,2,2,1,6,1,6),_InfnAuditSourceOid_Type())
infnAuditSourceOid.setMaxAccess(_C)
if mibBuilder.loadTexts:infnAuditSourceOid.setStatus(_B)
_InfnAuditUserId_Type=DisplayString
_InfnAuditUserId_Object=MibTableColumn
infnAuditUserId=_InfnAuditUserId_Object((1,3,6,1,4,1,21296,2,2,1,6,1,7),_InfnAuditUserId_Type())
infnAuditUserId.setMaxAccess(_C)
if mibBuilder.loadTexts:infnAuditUserId.setStatus(_B)
_InfnAuditHostInfo_Type=DisplayString
_InfnAuditHostInfo_Object=MibTableColumn
infnAuditHostInfo=_InfnAuditHostInfo_Object((1,3,6,1,4,1,21296,2,2,1,6,1,8),_InfnAuditHostInfo_Type())
infnAuditHostInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:infnAuditHostInfo.setStatus(_B)
_InfnAuditTime_Type=DisplayString
_InfnAuditTime_Object=MibTableColumn
infnAuditTime=_InfnAuditTime_Object((1,3,6,1,4,1,21296,2,2,1,6,1,9),_InfnAuditTime_Type())
infnAuditTime.setMaxAccess(_C)
if mibBuilder.loadTexts:infnAuditTime.setStatus(_B)
_InfnAuditOperationName_Type=DisplayString
_InfnAuditOperationName_Object=MibTableColumn
infnAuditOperationName=_InfnAuditOperationName_Object((1,3,6,1,4,1,21296,2,2,1,6,1,10),_InfnAuditOperationName_Type())
infnAuditOperationName.setMaxAccess(_C)
if mibBuilder.loadTexts:infnAuditOperationName.setStatus(_B)
_InfnAuditOperationStatus_Type=DisplayString
_InfnAuditOperationStatus_Object=MibTableColumn
infnAuditOperationStatus=_InfnAuditOperationStatus_Object((1,3,6,1,4,1,21296,2,2,1,6,1,11),_InfnAuditOperationStatus_Type())
infnAuditOperationStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:infnAuditOperationStatus.setStatus(_B)
_InfnAuditParamsList_Type=DisplayString
_InfnAuditParamsList_Object=MibTableColumn
infnAuditParamsList=_InfnAuditParamsList_Object((1,3,6,1,4,1,21296,2,2,1,6,1,12),_InfnAuditParamsList_Type())
infnAuditParamsList.setMaxAccess(_C)
if mibBuilder.loadTexts:infnAuditParamsList.setStatus(_B)
_InfnSecurityEventTable_Object=MibTable
infnSecurityEventTable=_InfnSecurityEventTable_Object((1,3,6,1,4,1,21296,2,2,1,7))
if mibBuilder.loadTexts:infnSecurityEventTable.setStatus(_B)
_InfnSecurityEventEntry_Object=MibTableRow
infnSecurityEventEntry=_InfnSecurityEventEntry_Object((1,3,6,1,4,1,21296,2,2,1,7,1))
infnSecurityEventEntry.setIndexNames((0,_A,_L))
if mibBuilder.loadTexts:infnSecurityEventEntry.setStatus(_B)
_InfnSecurityNotificationId_Type=Integer32
_InfnSecurityNotificationId_Object=MibTableColumn
infnSecurityNotificationId=_InfnSecurityNotificationId_Object((1,3,6,1,4,1,21296,2,2,1,7,1,1),_InfnSecurityNotificationId_Type())
infnSecurityNotificationId.setMaxAccess(_F)
if mibBuilder.loadTexts:infnSecurityNotificationId.setStatus(_B)
_InfnSecurityNodeId_Type=DisplayString
_InfnSecurityNodeId_Object=MibTableColumn
infnSecurityNodeId=_InfnSecurityNodeId_Object((1,3,6,1,4,1,21296,2,2,1,7,1,2),_InfnSecurityNodeId_Type())
infnSecurityNodeId.setMaxAccess(_C)
if mibBuilder.loadTexts:infnSecurityNodeId.setStatus(_B)
_InfnSecurityNodeName_Type=DisplayString
_InfnSecurityNodeName_Object=MibTableColumn
infnSecurityNodeName=_InfnSecurityNodeName_Object((1,3,6,1,4,1,21296,2,2,1,7,1,3),_InfnSecurityNodeName_Type())
infnSecurityNodeName.setMaxAccess(_C)
if mibBuilder.loadTexts:infnSecurityNodeName.setStatus(_B)
_InfnSecurityObjectType_Type=InfnManagedObjectType
_InfnSecurityObjectType_Object=MibTableColumn
infnSecurityObjectType=_InfnSecurityObjectType_Object((1,3,6,1,4,1,21296,2,2,1,7,1,4),_InfnSecurityObjectType_Type())
infnSecurityObjectType.setMaxAccess(_C)
if mibBuilder.loadTexts:infnSecurityObjectType.setStatus(_B)
_InfnSecurityObjectAid_Type=DisplayString
_InfnSecurityObjectAid_Object=MibTableColumn
infnSecurityObjectAid=_InfnSecurityObjectAid_Object((1,3,6,1,4,1,21296,2,2,1,7,1,5),_InfnSecurityObjectAid_Type())
infnSecurityObjectAid.setMaxAccess(_C)
if mibBuilder.loadTexts:infnSecurityObjectAid.setStatus(_B)
_InfnSecuritySourceOid_Type=ObjectIdentifier
_InfnSecuritySourceOid_Object=MibTableColumn
infnSecuritySourceOid=_InfnSecuritySourceOid_Object((1,3,6,1,4,1,21296,2,2,1,7,1,6),_InfnSecuritySourceOid_Type())
infnSecuritySourceOid.setMaxAccess(_C)
if mibBuilder.loadTexts:infnSecuritySourceOid.setStatus(_B)
_InfnSecurityHostInfo_Type=DisplayString
_InfnSecurityHostInfo_Object=MibTableColumn
infnSecurityHostInfo=_InfnSecurityHostInfo_Object((1,3,6,1,4,1,21296,2,2,1,7,1,7),_InfnSecurityHostInfo_Type())
infnSecurityHostInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:infnSecurityHostInfo.setStatus(_B)
_InfnSecurityEventTime_Type=DisplayString
_InfnSecurityEventTime_Object=MibTableColumn
infnSecurityEventTime=_InfnSecurityEventTime_Object((1,3,6,1,4,1,21296,2,2,1,7,1,8),_InfnSecurityEventTime_Type())
infnSecurityEventTime.setMaxAccess(_C)
if mibBuilder.loadTexts:infnSecurityEventTime.setStatus(_B)
_InfnSecurityMessage_Type=DisplayString
_InfnSecurityMessage_Object=MibTableColumn
infnSecurityMessage=_InfnSecurityMessage_Object((1,3,6,1,4,1,21296,2,2,1,7,1,9),_InfnSecurityMessage_Type())
infnSecurityMessage.setMaxAccess(_C)
if mibBuilder.loadTexts:infnSecurityMessage.setStatus(_B)
infnAlarmGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,1,2,16,1,1))
infnAlarmGroup.setObjects(*((_A,_G),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z)))
if mibBuilder.loadTexts:infnAlarmGroup.setStatus(_B)
infnTcaGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,1,2,16,1,2))
infnTcaGroup.setObjects(*((_A,_I),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p)))
if mibBuilder.loadTexts:infnTcaGroup.setStatus(_B)
infnAdminEventGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,1,2,16,1,3))
infnAdminEventGroup.setObjects(*((_A,_J),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w)))
if mibBuilder.loadTexts:infnAdminEventGroup.setStatus(_B)
infnAuditEventGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,1,2,16,1,4))
infnAuditEventGroup.setObjects(*((_A,_K),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_A6),(_A,_A7)))
if mibBuilder.loadTexts:infnAuditEventGroup.setStatus(_B)
infnSecurityEventGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,1,2,16,1,5))
infnSecurityEventGroup.setObjects(*((_A,_L),(_A,_A8),(_A,_A9),(_A,_AA),(_A,_AB),(_A,_AC),(_A,_AD),(_A,_AE),(_A,_AF)))
if mibBuilder.loadTexts:infnSecurityEventGroup.setStatus(_B)
infnAlarmNotification=NotificationType((1,3,6,1,4,1,21296,2,2,1,2,1))
infnAlarmNotification.setObjects(*((_A,_G),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_AT),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z)))
if mibBuilder.loadTexts:infnAlarmNotification.setStatus(_B)
infnTcaNotification=NotificationType((1,3,6,1,4,1,21296,2,2,1,2,2))
infnTcaNotification.setObjects(*((_A,_I),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_AU),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p)))
if mibBuilder.loadTexts:infnTcaNotification.setStatus(_B)
infnAdminEventNotification=NotificationType((1,3,6,1,4,1,21296,2,2,1,2,3))
infnAdminEventNotification.setObjects(*((_A,_J),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w)))
if mibBuilder.loadTexts:infnAdminEventNotification.setStatus(_B)
infnAuditEventNotification=NotificationType((1,3,6,1,4,1,21296,2,2,1,2,4))
infnAuditEventNotification.setObjects(*((_A,_K),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_A6),(_A,_A7)))
if mibBuilder.loadTexts:infnAuditEventNotification.setStatus(_B)
infnSecurityEventNotification=NotificationType((1,3,6,1,4,1,21296,2,2,1,2,5))
infnSecurityEventNotification.setObjects(*((_A,_L),(_A,_A8),(_A,_A9),(_A,_AA),(_A,_AB),(_A,_AC),(_A,_AD),(_A,_AE),(_A,_AF)))
if mibBuilder.loadTexts:infnSecurityEventNotification.setStatus(_B)
infnNotificationGroup=NotificationGroup((1,3,6,1,4,1,21296,2,2,1,2,16,2,1))
infnNotificationGroup.setObjects(*((_A,_AV),(_A,_AW),(_A,_AX),(_A,_AY),(_A,_AZ)))
if mibBuilder.loadTexts:infnNotificationGroup.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'infnNotifications':infnNotifications,_AV:infnAlarmNotification,_AW:infnTcaNotification,_AX:infnAdminEventNotification,_AZ:infnAuditEventNotification,_AY:infnSecurityEventNotification,'infnNotificationConformance':infnNotificationConformance,'infnNotificationObjectGroups':infnNotificationObjectGroups,'infnAlarmGroup':infnAlarmGroup,'infnTcaGroup':infnTcaGroup,'infnAdminEventGroup':infnAdminEventGroup,'infnAuditEventGroup':infnAuditEventGroup,'infnSecurityEventGroup':infnSecurityEventGroup,'infnNotificationNotifGroups':infnNotificationNotifGroups,'infnNotificationGroup':infnNotificationGroup,'infnAlarmTable':infnAlarmTable,'infnAlarmEntry':infnAlarmEntry,_G:alarmNotificationId,_M:alarmNodeId,_N:alarmNodeName,_O:alarmObjectType,_P:alarmObjectAid,_Q:alarmSourceOid,_R:alarmProbableCause,_S:alarmSeverity,_AT:alarmCategory,_T:alarmServiceAffecting,_U:alarmOccurrenceTime,_V:alarmLocation,_W:alarmDirection,_X:alarmProbableCauseDescription,_Y:alarmAdditionalText,_Z:alarmCorrelationId,'infnTcaTable':infnTcaTable,'infnTcaEntry':infnTcaEntry,_I:tcaNotificationId,_a:tcaNodeId,_b:tcaNodeName,_c:tcaObjectType,_d:tcaObjectAid,_e:tcaSourceOid,_f:tcaProbableCause,_g:tcaSeverity,_AU:tcaCategory,_h:tcaServiceAffecting,_i:tcaOccurrenceTime,_j:tcaLocation,_k:tcaDirection,_l:tcaMonitoredValue,_m:tcaThresholdValue,_n:tcaTimePeriod,_o:tcaProbableCauseDescription,_p:tcaAdditionalText,'infnAdminEventTable':infnAdminEventTable,'infnAdminEventEntry':infnAdminEventEntry,_J:infnAdminNotificationId,_q:infnAdminNodeId,_r:infnAdminNodeName,_s:infnAdminObjectType,_t:infnAdminObjectAid,_u:infnAdminSourceOid,_v:infnAdminEventTime,_w:infnAdminCause,'infnAuditEventTable':infnAuditEventTable,'infnAuditEventEntry':infnAuditEventEntry,_K:infnAuditNotificationId,_x:infnAuditNodeId,_y:infnAuditNodeName,_z:infnAuditObjectType,_A0:infnAuditObjectAid,_A1:infnAuditSourceOid,_A2:infnAuditUserId,_A3:infnAuditHostInfo,_A4:infnAuditTime,_A5:infnAuditOperationName,_A6:infnAuditOperationStatus,_A7:infnAuditParamsList,'infnSecurityEventTable':infnSecurityEventTable,'infnSecurityEventEntry':infnSecurityEventEntry,_L:infnSecurityNotificationId,_A8:infnSecurityNodeId,_A9:infnSecurityNodeName,_AA:infnSecurityObjectType,_AB:infnSecurityObjectAid,_AC:infnSecuritySourceOid,_AD:infnSecurityHostInfo,_AE:infnSecurityEventTime,_AF:infnSecurityMessage})