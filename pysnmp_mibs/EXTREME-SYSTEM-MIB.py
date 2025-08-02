_z='extremeSystemPowerUsageUnitMultiplier'
_y='extremeSystemPowerUsageValue'
_x='extremePowerSupplyStatus'
_w='message'
_v='eventName'
_u='severity'
_t='extremeSystemPowerState'
_s='extremeInstallImageStartTime'
_r='extremeInstallImagePartition'
_q='extremeInstallImageFilename'
_p='extremeInstallImageStatus'
_o='extremeDownloadImageStartTime'
_n='extremeDownloadImagePartition'
_m='extremeDownloadImageFilename'
_l='extremeDownloadImageStatus'
_k='extremeSlotNumber'
_j='extremeRebootSlotId'
_i='extremeSystemPowerMonitorIndex1'
_h='extremeSlotIndex'
_g='extremePowerSupplyOutputSensorIdx'
_f='extremePowerSupplyIndex'
_e='extremeImageFeatureNumber'
_d='extremeImageNumber'
_c='not-accessible'
_b='extremeCpuTask2Name'
_a='extremeCpuTask2CpuId'
_Z='noRPMInfo'
_Y='extremeFanNumber'
_X='factoryDefault'
_W='sysUpTime'
_V='extremeInstallImageSlotId'
_U='extremeDownloadImageSlotId'
_T='extremePowerSupplyNumber'
_S='presentNotOK'
_R='presentOK'
_Q='sysDescr'
_P='SNMPv2-MIB'
_O='notPresent'
_N='secondary'
_M='primary'
_L='enabled'
_K='disabled'
_J='unknown'
_I='accessible-for-notify'
_H='read-create'
_G='deprecated'
_F='DisplayString'
_E='EXTREME-SYSTEM-MIB'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
PortList,extremeAgent=mibBuilder.importSymbols('EXTREME-BASE-MIB','PortList','extremeAgent')
ifDescr,=mibBuilder.importSymbols('IF-MIB','ifDescr')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
sysDescr,sysUpTime=mibBuilder.importSymbols(_P,_Q,_W)
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_F,'MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
extremeSystem=ModuleIdentity((1,3,6,1,4,1,1916,1,1))
if mibBuilder.loadTexts:extremeSystem.setRevisions(('2020-02-12 17:39','2019-09-04 21:20','2018-09-26 23:02','2019-08-05 10:31','2018-09-14 15:31','2018-07-24 14:00','2018-07-02 10:10','2018-06-07 14:10','2018-03-01 16:31','2017-08-29 19:48','2017-06-28 03:38','2017-06-14 15:01','2017-06-01 16:30','2016-08-05 18:09','2016-07-25 08:10','2016-03-29 00:00','2015-03-06 19:55'))
class SlotType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,50,51,52,53,54,55,101,102,103,104,105,106,107,108,200,201,202,203,204,301,400,401,402,406,414,415,416,417,418,419,420,421,422,423,424,425,426,427,428,429,430,431,432,433,434,435,437,439,440,442,443,444,445,446,447,448,449,450,451,452,453,454,455,456,457,458,459,460,461,462,463,464,465,466,467,468,469,470,471,472,473,474,475,476,477,478,480,481,482,483,484,485,486,487,488,489,490,491,492,493,494,496,497,498,500,503,504,505,506,507,508,509,510,511,512,513,514,515,516,517,518,519,520,521,522,523,524,525,526,527,528,529,530,531,532,533,534,535,536,537,538,539,540,541,542,543,546,547,548,549,550,551,552,553,554,555,556,557,558,559,560,561,562,563,564,565,566,567,568,569,570,571,572,573,574,575,576,578,579,580,582,583,584,585,586,587,588,589,590,591,592,593,594,595,596,597,600,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633,634,635,636,637,638,639,640,641,642,643,644,645,646,647,648,650,651,652,653,656,660,661,662,663,664,665,666,667,670,671,672,673,674,675,676,677,678,679,680,681,682,683,684)));namedValues=NamedValues(*(('none',1),('fe32',2),('g4x',3),('g6x',4),('fe32fx',5),('msm',6),('f48ti',7),('g8xi',8),('g8ti',9),('g12sxi',10),('g12ti',11),('msm64i',18),('alpine3808',19),('alpine3804',20),('fm32t',21),('gm4x',22),('gm4sx',23),('gm4t',24),('wdm8',25),('fm24f',26),('fm24sf',27),('fm24te',28),('f96ti',29),('wdm4',30),('f32fi',31),('tenGig',32),('tenGigLR',33),('g16x3',34),('g24t3',35),('gm16x3',36),('gm16t3',37),('fm16t3',38),('fm32p',39),('fm8v',50),('wm4t1',51),('wm4t3',52),('wm1t3',53),('wm4e1',54),('alpine3802',55),('p3c',101),('p12c',102),('arm',103),('mpls',104),('sma',105),('p48c',106),('a3c',107),('a12c',108),('pxm',200),('s300fixed',201),('msm3',202),('msm1',203),('msm1xl',204),('s300expansion',301),('g60t',400),('g60x',401),('teng6x',402),('vm386EXOS',406),('msm-g8x',414),('g8x',415),('g48t',416),('g48p',417),('g24x',418),('teng4x',419),('teng2x',420),('g20x',421),('teng2h',422),('x450-24x',423),('x450-24t',424),('msm5',425),('msm5r',426),('gm20t',427),('gm20xt',428),('gm20xtr',429),('xm2x',430),('xm2xr',431),('msm6r',432),('g48te',433),('g48ta',434),('g48pe',435),('g48x',437),('x450a-24t',439),('x450e-24p',440),('x450a-48t',442),('x450e-48p',443),('x450a-24x',444),('x450a-24tdc',445),('x450a-24xdc',446),('msm-48',447),('teng4ca',448),('teng4xa',449),('g48tc',450),('g48te2',451),('g48xc',452),('g24xc',453),('tenG4xc',454),('tenG8xc',455),('msms48c',456),('g8xc',457),('tenG1xc',458),('g48tcPoE',459),('g48te2PoE',460),('x450a-48tdc',461),('x250e-24t',462),('x250e-24p',463),('x250e-48t',464),('x250e-48p',465),('x250e-24x',466),('x250e-24xtaa',467),('x250e-24tdc',468),('x250e-48tdc',469),('x250e-24xdc',470),('x150-24t',471),('x150-24tdc',472),('x150-24p',473),('x150-48t',474),('x150-48tdc',475),('x150-48p',476),('x150-24x',477),('x150-24xdc',478),('xm2hr',480),('x350-24t',481),('x350-48t',482),('x650-24t',483),('x650-24x',484),('x650-24tG4X',485),('x650-24xG4X',486),('x650-24tG4X10G2S',487),('x650-24xG4X10G2S',488),('x650-24t10G8X10G2S',489),('x650-24x10G8X10G2S',490),('x650-24t64G2S',491),('x650-24x64G2S',492),('x650-24t64G4S',493),('x650-24x64G4S',494),('mmbase',496),('mmadv',497),('gm40xb',498),('xm8xb',500),('x8900msm128',503),('x8900tenG24xc',504),('x8900tenG8xm',505),('x8900g48tm',506),('x8900g48xm',507),('x8900g96tc',508),('x8900g48tmPoE',509),('nwie450a',510),('x480-24x',511),('x480-48x',512),('x480-48t',513),('x480-24x10G2S',514),('x480-48x10G2S',515),('x480-48t10G2S',516),('x480-24x10G4X',517),('x480-48x10G4X',518),('x480-48t10G4X',519),('x480-24x32G2S',520),('x480-48x32G2S',521),('x480-48t32G2S',522),('x8500msm48',523),('x8500g24xa',524),('x8500g48te',525),('x8500g48tePoE',526),('x460-24t',527),('x460-24p',528),('x460-24x',529),('x460-48t',530),('x460-48p',531),('x460-48x',532),('x450e-24t',533),('x450e-48t',534),('hm-2x24ga',535),('xcm88s1',536),('xcm8848t',537),('xcm88p',538),('xcm8824f',539),('xcm8808x',540),('xcm888f',541),('x480-48x20G2S',542),('x480-48t20G2S',543),('x670-48x',546),('x670v-48x',547),('e4g-400',548),('bdx-mm1',549),('bdxa-10g48x',550),('bdxa-10g24x',551),('bdxa-40g24x',552),('bdxa-40g12x',553),('bdxa-fm20t',554),('bdxa-fm10t',555),('x480-24x20G2S',556),('x650-24x40G4X',557),('x650-24t40G4X',558),('x480-24x40G4X',559),('x480-48x40G4X',560),('x480-48t40G4X',561),('tenG2xc',562),('fortyG6xc',563),('e4g-200',564),('x440-8t',565),('x440-8p',566),('x440-24t',567),('x440-24p',568),('x440-48t',569),('x440-48p',570),('x440-24t-10G',571),('x440-24p-10G',572),('x440-48t-10G',573),('x440-48p-10G',574),('ags100-24t',575),('ags150-24p',576),('x670v-48t',578),('x440-L2-24t',579),('x440-L2-48t',580),('x440-24x',582),('x440-48x',583),('bdxa-10g48t',584),('x430-24t',585),('x430-48t',586),('x440-24tdc',587),('x440-48tdc',588),('x770-32q',589),('x670G2-48x-4q',590),('x670G2-72x',591),('x460G2-24t-10G4',592),('x460G2-24p-10G4',593),('x460G2-24x-10G4',594),('x460G2-48t-10G4',595),('x460G2-48p-10G4',596),('x460G2-48x-10G4',597),('bdxb-40g12x-xl',600),('bdxb-100g4x-xl',601),('x430-8p',602),('x430-24p',603),('bdxb-100g4x',604),('ctr-8440',605),('x450-G2-24t',606),('x450-G2-24p',607),('x450-G2-48t',608),('x450-G2-48p',609),('x450-G2-24t-GE4',610),('x450-G2-24p-GE4',611),('x450-G2-48t-GE4',612),('x450-G2-48p-GE4',613),('x460G2-24t-G4',614),('x460G2-24p-G4',615),('x460G2-48t-G4',616),('x460G2-48p-G4',617),('x440G2-48p-10G4',618),('x440G2-48t-10G4',619),('x440G2-48t-10G4-DC',620),('x440G2-24p-10G4',621),('x440G2-24t-10G4',622),('x440G2-24t-10G4-DC',623),('x440G2-24x-10G4',624),('x440G2-12p-10GE4',625),('x440G2-12t-10GE4',626),('x440G2-12t8fx-G4',627),('x440G2-24t-G4',628),('x440G2-24fx-G4',629),('bdxa-48t',630),('bdxa-48x',631),('bdxa-48x-0',632),('x620-16t',633),('x620-16p',634),('x620-16x',635),('x620-10x',636),('x620-8t-2x',637),('x8900msm96',638),('x870-32c',639),('x870-96x-8c',640),('x560-48mp-10GE4-100GE2',641),('x560-48mt-10GE4-100GE2',642),('x560-24mp-10GE4-100GE2',643),('x690-48t-4q-2c',644),('x690-48x-4q-2c',645),('x460-G2-16mp-32p-10GE4',646),('x460G2-24p-24hp',647),('x460G2-24t-24ht',648),('v400-24t-10GE2',650),('v400-24p-10GE2',651),('v400-48t-10GE4',652),('v400-48p-10GE4',653),('xtremeWhitebox',656),('x695-48y-8c',660),('x590-24t-1q-2c',661),('x590-24x-1q-2c',662),('x465-48t',663),('x465-48p',664),('x465-48w',665),('x465-24mu',666),('x465-24mu-24w',667),('x465-24w',670),('x725-48y',671),('v300-8p-2t-w',672),('v300-8p-2x',673),('v300-8t-2x',674),('v300ht-8p-2x',675),('v300ht-8t-2x',676),('x465-24xe',677),('x465-24s',678),('x435-24p-4s',679),('x435-24t-4s',680),('x435-8p-4s',681),('x435-8t-4s',682),('x435-8p-2t-w',683),('x465i-48w',684)))
class PowerValue(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('v110',1),('v220',2),('v48DC',3),(_J,4)))
class UnitMultiplier(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-24,-21,-18,-15,-12,-9,-6,-3,0,3,6,9,12,15,18,21,24)));namedValues=NamedValues(*(('yocto',-24),('zepto',-21),('atto',-18),('femto',-15),('pico',-12),('nano',-9),('micro',-6),('milli',-3),('units',0),('kilo',3),('mega',6),('giga',9),('tera',12),('peta',15),('exa',18),('zetta',21),('yotta',24)))
_ExtremeSystemCommon_ObjectIdentity=ObjectIdentity
extremeSystemCommon=_ExtremeSystemCommon_ObjectIdentity((1,3,6,1,4,1,1916,1,1,1))
class _ExtremeSaveConfiguration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('saveToPrimary',1),('saveToSecondary',2),('saveToCurrent',3),(_X,4),('saveToFile',5)))
_ExtremeSaveConfiguration_Type.__name__=_C
_ExtremeSaveConfiguration_Object=MibScalar
extremeSaveConfiguration=_ExtremeSaveConfiguration_Object((1,3,6,1,4,1,1916,1,1,1,3),_ExtremeSaveConfiguration_Type())
extremeSaveConfiguration.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeSaveConfiguration.setStatus(_A)
class _ExtremeSaveStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('saveInProgress',1),('saveNotInProgress',2),('saveNotReady',3)))
_ExtremeSaveStatus_Type.__name__=_C
_ExtremeSaveStatus_Object=MibScalar
extremeSaveStatus=_ExtremeSaveStatus_Object((1,3,6,1,4,1,1916,1,1,1,4),_ExtremeSaveStatus_Type())
extremeSaveStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeSaveStatus.setStatus(_A)
class _ExtremeCurrentConfigInUse_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_M,1),(_N,2),('other',3),(_X,4)))
_ExtremeCurrentConfigInUse_Type.__name__=_C
_ExtremeCurrentConfigInUse_Object=MibScalar
extremeCurrentConfigInUse=_ExtremeCurrentConfigInUse_Object((1,3,6,1,4,1,1916,1,1,1,5),_ExtremeCurrentConfigInUse_Type())
extremeCurrentConfigInUse.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeCurrentConfigInUse.setStatus(_A)
class _ExtremeConfigToUseOnReboot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_M,1),(_N,2),('other',3)))
_ExtremeConfigToUseOnReboot_Type.__name__=_C
_ExtremeConfigToUseOnReboot_Object=MibScalar
extremeConfigToUseOnReboot=_ExtremeConfigToUseOnReboot_Object((1,3,6,1,4,1,1916,1,1,1,6),_ExtremeConfigToUseOnReboot_Type())
extremeConfigToUseOnReboot.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeConfigToUseOnReboot.setStatus(_A)
_ExtremeOverTemperatureAlarm_Type=TruthValue
_ExtremeOverTemperatureAlarm_Object=MibScalar
extremeOverTemperatureAlarm=_ExtremeOverTemperatureAlarm_Object((1,3,6,1,4,1,1916,1,1,1,7),_ExtremeOverTemperatureAlarm_Type())
extremeOverTemperatureAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeOverTemperatureAlarm.setStatus(_A)
class _ExtremeCurrentTemperature_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_ExtremeCurrentTemperature_Type.__name__=_C
_ExtremeCurrentTemperature_Object=MibScalar
extremeCurrentTemperature=_ExtremeCurrentTemperature_Object((1,3,6,1,4,1,1916,1,1,1,8),_ExtremeCurrentTemperature_Type())
extremeCurrentTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeCurrentTemperature.setStatus(_A)
_ExtremeFanStatusTable_Object=MibTable
extremeFanStatusTable=_ExtremeFanStatusTable_Object((1,3,6,1,4,1,1916,1,1,1,9))
if mibBuilder.loadTexts:extremeFanStatusTable.setStatus(_A)
_ExtremeFanStatusEntry_Object=MibTableRow
extremeFanStatusEntry=_ExtremeFanStatusEntry_Object((1,3,6,1,4,1,1916,1,1,1,9,1))
extremeFanStatusEntry.setIndexNames((0,_E,_Y))
if mibBuilder.loadTexts:extremeFanStatusEntry.setStatus(_A)
_ExtremeFanNumber_Type=Integer32
_ExtremeFanNumber_Object=MibTableColumn
extremeFanNumber=_ExtremeFanNumber_Object((1,3,6,1,4,1,1916,1,1,1,9,1,1),_ExtremeFanNumber_Type())
extremeFanNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeFanNumber.setStatus(_A)
_ExtremeFanOperational_Type=TruthValue
_ExtremeFanOperational_Object=MibTableColumn
extremeFanOperational=_ExtremeFanOperational_Object((1,3,6,1,4,1,1916,1,1,1,9,1,2),_ExtremeFanOperational_Type())
extremeFanOperational.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeFanOperational.setStatus(_A)
_ExtremeFanEntPhysicalIndex_Type=Integer32
_ExtremeFanEntPhysicalIndex_Object=MibTableColumn
extremeFanEntPhysicalIndex=_ExtremeFanEntPhysicalIndex_Object((1,3,6,1,4,1,1916,1,1,1,9,1,3),_ExtremeFanEntPhysicalIndex_Type())
extremeFanEntPhysicalIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeFanEntPhysicalIndex.setStatus(_A)
_ExtremeFanSpeed_Type=Integer32
_ExtremeFanSpeed_Object=MibTableColumn
extremeFanSpeed=_ExtremeFanSpeed_Object((1,3,6,1,4,1,1916,1,1,1,9,1,4),_ExtremeFanSpeed_Type())
extremeFanSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeFanSpeed.setStatus(_A)
_ExtremePrimaryPowerOperational_Type=TruthValue
_ExtremePrimaryPowerOperational_Object=MibScalar
extremePrimaryPowerOperational=_ExtremePrimaryPowerOperational_Object((1,3,6,1,4,1,1916,1,1,1,10),_ExtremePrimaryPowerOperational_Type())
extremePrimaryPowerOperational.setMaxAccess(_B)
if mibBuilder.loadTexts:extremePrimaryPowerOperational.setStatus(_A)
class _ExtremeRedundantPowerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_O,1),(_R,2),(_S,3)))
_ExtremeRedundantPowerStatus_Type.__name__=_C
_ExtremeRedundantPowerStatus_Object=MibScalar
extremeRedundantPowerStatus=_ExtremeRedundantPowerStatus_Object((1,3,6,1,4,1,1916,1,1,1,11),_ExtremeRedundantPowerStatus_Type())
extremeRedundantPowerStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeRedundantPowerStatus.setStatus(_A)
_ExtremeRedundantPowerAlarm_Type=TruthValue
_ExtremeRedundantPowerAlarm_Object=MibScalar
extremeRedundantPowerAlarm=_ExtremeRedundantPowerAlarm_Object((1,3,6,1,4,1,1916,1,1,1,12),_ExtremeRedundantPowerAlarm_Type())
extremeRedundantPowerAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeRedundantPowerAlarm.setStatus(_A)
class _ExtremePrimarySoftwareRev_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_ExtremePrimarySoftwareRev_Type.__name__=_F
_ExtremePrimarySoftwareRev_Object=MibScalar
extremePrimarySoftwareRev=_ExtremePrimarySoftwareRev_Object((1,3,6,1,4,1,1916,1,1,1,13),_ExtremePrimarySoftwareRev_Type())
extremePrimarySoftwareRev.setMaxAccess(_B)
if mibBuilder.loadTexts:extremePrimarySoftwareRev.setStatus(_A)
class _ExtremeSecondarySoftwareRev_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_ExtremeSecondarySoftwareRev_Type.__name__=_F
_ExtremeSecondarySoftwareRev_Object=MibScalar
extremeSecondarySoftwareRev=_ExtremeSecondarySoftwareRev_Object((1,3,6,1,4,1,1916,1,1,1,14),_ExtremeSecondarySoftwareRev_Type())
extremeSecondarySoftwareRev.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeSecondarySoftwareRev.setStatus(_A)
class _ExtremeImageToUseOnReboot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_ExtremeImageToUseOnReboot_Type.__name__=_C
_ExtremeImageToUseOnReboot_Object=MibScalar
extremeImageToUseOnReboot=_ExtremeImageToUseOnReboot_Object((1,3,6,1,4,1,1916,1,1,1,15),_ExtremeImageToUseOnReboot_Type())
extremeImageToUseOnReboot.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeImageToUseOnReboot.setStatus(_A)
class _ExtremeSystemID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,126))
_ExtremeSystemID_Type.__name__=_F
_ExtremeSystemID_Object=MibScalar
extremeSystemID=_ExtremeSystemID_Object((1,3,6,1,4,1,1916,1,1,1,16),_ExtremeSystemID_Type())
extremeSystemID.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeSystemID.setStatus(_A)
class _ExtremeSystemBoardID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,126))
_ExtremeSystemBoardID_Type.__name__=_F
_ExtremeSystemBoardID_Object=MibScalar
extremeSystemBoardID=_ExtremeSystemBoardID_Object((1,3,6,1,4,1,1916,1,1,1,17),_ExtremeSystemBoardID_Type())
extremeSystemBoardID.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeSystemBoardID.setStatus(_A)
class _ExtremeSystemLeftBoardID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,126))
_ExtremeSystemLeftBoardID_Type.__name__=_F
_ExtremeSystemLeftBoardID_Object=MibScalar
extremeSystemLeftBoardID=_ExtremeSystemLeftBoardID_Object((1,3,6,1,4,1,1916,1,1,1,18),_ExtremeSystemLeftBoardID_Type())
extremeSystemLeftBoardID.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeSystemLeftBoardID.setStatus(_A)
class _ExtremeSystemRightBoardID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,126))
_ExtremeSystemRightBoardID_Type.__name__=_F
_ExtremeSystemRightBoardID_Object=MibScalar
extremeSystemRightBoardID=_ExtremeSystemRightBoardID_Object((1,3,6,1,4,1,1916,1,1,1,19),_ExtremeSystemRightBoardID_Type())
extremeSystemRightBoardID.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeSystemRightBoardID.setStatus(_A)
_ExtremeInputPowerVoltage_Type=PowerValue
_ExtremeInputPowerVoltage_Object=MibScalar
extremeInputPowerVoltage=_ExtremeInputPowerVoltage_Object((1,3,6,1,4,1,1916,1,1,1,20),_ExtremeInputPowerVoltage_Type())
extremeInputPowerVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeInputPowerVoltage.setStatus(_A)
class _ExtremePowerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_O,1),(_R,2),(_S,3)))
_ExtremePowerStatus_Type.__name__=_C
_ExtremePowerStatus_Object=MibScalar
extremePowerStatus=_ExtremePowerStatus_Object((1,3,6,1,4,1,1916,1,1,1,21),_ExtremePowerStatus_Type())
extremePowerStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:extremePowerStatus.setStatus(_A)
_ExtremePowerAlarm_Type=TruthValue
_ExtremePowerAlarm_Object=MibScalar
extremePowerAlarm=_ExtremePowerAlarm_Object((1,3,6,1,4,1,1916,1,1,1,22),_ExtremePowerAlarm_Type())
extremePowerAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:extremePowerAlarm.setStatus(_A)
_ExtremeRmonEnable_Type=TruthValue
_ExtremeRmonEnable_Object=MibScalar
extremeRmonEnable=_ExtremeRmonEnable_Object((1,3,6,1,4,1,1916,1,1,1,23),_ExtremeRmonEnable_Type())
extremeRmonEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeRmonEnable.setStatus(_A)
class _ExtremeBootROMVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_ExtremeBootROMVersion_Type.__name__=_F
_ExtremeBootROMVersion_Object=MibScalar
extremeBootROMVersion=_ExtremeBootROMVersion_Object((1,3,6,1,4,1,1916,1,1,1,25),_ExtremeBootROMVersion_Type())
extremeBootROMVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeBootROMVersion.setStatus(_A)
_ExtremeDot1dTpFdbTableEnable_Type=TruthValue
_ExtremeDot1dTpFdbTableEnable_Object=MibScalar
extremeDot1dTpFdbTableEnable=_ExtremeDot1dTpFdbTableEnable_Object((1,3,6,1,4,1,1916,1,1,1,26),_ExtremeDot1dTpFdbTableEnable_Type())
extremeDot1dTpFdbTableEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeDot1dTpFdbTableEnable.setStatus('obsolete')
_ExtremePowerSupplyTable_Object=MibTable
extremePowerSupplyTable=_ExtremePowerSupplyTable_Object((1,3,6,1,4,1,1916,1,1,1,27))
if mibBuilder.loadTexts:extremePowerSupplyTable.setStatus(_A)
_ExtremePowerSupplyEntry_Object=MibTableRow
extremePowerSupplyEntry=_ExtremePowerSupplyEntry_Object((1,3,6,1,4,1,1916,1,1,1,27,1))
extremePowerSupplyEntry.setIndexNames((0,_E,_T))
if mibBuilder.loadTexts:extremePowerSupplyEntry.setStatus(_A)
_ExtremePowerSupplyNumber_Type=Integer32
_ExtremePowerSupplyNumber_Object=MibTableColumn
extremePowerSupplyNumber=_ExtremePowerSupplyNumber_Object((1,3,6,1,4,1,1916,1,1,1,27,1,1),_ExtremePowerSupplyNumber_Type())
extremePowerSupplyNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:extremePowerSupplyNumber.setStatus(_A)
class _ExtremePowerSupplyStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_O,1),(_R,2),(_S,3),('presentPowerOff',4)))
_ExtremePowerSupplyStatus_Type.__name__=_C
_ExtremePowerSupplyStatus_Object=MibTableColumn
extremePowerSupplyStatus=_ExtremePowerSupplyStatus_Object((1,3,6,1,4,1,1916,1,1,1,27,1,2),_ExtremePowerSupplyStatus_Type())
extremePowerSupplyStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:extremePowerSupplyStatus.setStatus(_A)
_ExtremePowerSupplyInputVoltage_Type=PowerValue
_ExtremePowerSupplyInputVoltage_Object=MibTableColumn
extremePowerSupplyInputVoltage=_ExtremePowerSupplyInputVoltage_Object((1,3,6,1,4,1,1916,1,1,1,27,1,3),_ExtremePowerSupplyInputVoltage_Type())
extremePowerSupplyInputVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:extremePowerSupplyInputVoltage.setStatus(_A)
class _ExtremePowerSupplySerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,126))
_ExtremePowerSupplySerialNumber_Type.__name__=_F
_ExtremePowerSupplySerialNumber_Object=MibTableColumn
extremePowerSupplySerialNumber=_ExtremePowerSupplySerialNumber_Object((1,3,6,1,4,1,1916,1,1,1,27,1,4),_ExtremePowerSupplySerialNumber_Type())
extremePowerSupplySerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:extremePowerSupplySerialNumber.setStatus(_A)
_ExtremePowerSupplyEntPhysicalIndex_Type=Integer32
_ExtremePowerSupplyEntPhysicalIndex_Object=MibTableColumn
extremePowerSupplyEntPhysicalIndex=_ExtremePowerSupplyEntPhysicalIndex_Object((1,3,6,1,4,1,1916,1,1,1,27,1,5),_ExtremePowerSupplyEntPhysicalIndex_Type())
extremePowerSupplyEntPhysicalIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:extremePowerSupplyEntPhysicalIndex.setStatus(_A)
class _ExtremePowerSupplyFan1Speed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-2,-1)));namedValues=NamedValues(*((_Z,-2),(_O,-1)))
_ExtremePowerSupplyFan1Speed_Type.__name__=_C
_ExtremePowerSupplyFan1Speed_Object=MibTableColumn
extremePowerSupplyFan1Speed=_ExtremePowerSupplyFan1Speed_Object((1,3,6,1,4,1,1916,1,1,1,27,1,6),_ExtremePowerSupplyFan1Speed_Type())
extremePowerSupplyFan1Speed.setMaxAccess(_B)
if mibBuilder.loadTexts:extremePowerSupplyFan1Speed.setStatus(_A)
class _ExtremePowerSupplyFan2Speed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-2,-1)));namedValues=NamedValues(*((_Z,-2),(_O,-1)))
_ExtremePowerSupplyFan2Speed_Type.__name__=_C
_ExtremePowerSupplyFan2Speed_Object=MibTableColumn
extremePowerSupplyFan2Speed=_ExtremePowerSupplyFan2Speed_Object((1,3,6,1,4,1,1916,1,1,1,27,1,7),_ExtremePowerSupplyFan2Speed_Type())
extremePowerSupplyFan2Speed.setMaxAccess(_B)
if mibBuilder.loadTexts:extremePowerSupplyFan2Speed.setStatus(_A)
class _ExtremePowerSupplySource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_J,1),('ac',2),('dc',3),('externalPowerSupply',4),('internalRedundant',5)))
_ExtremePowerSupplySource_Type.__name__=_C
_ExtremePowerSupplySource_Object=MibTableColumn
extremePowerSupplySource=_ExtremePowerSupplySource_Object((1,3,6,1,4,1,1916,1,1,1,27,1,8),_ExtremePowerSupplySource_Type())
extremePowerSupplySource.setMaxAccess(_B)
if mibBuilder.loadTexts:extremePowerSupplySource.setStatus(_A)
_ExtremePowerSupplyInputPowerUsage_Type=Integer32
_ExtremePowerSupplyInputPowerUsage_Object=MibTableColumn
extremePowerSupplyInputPowerUsage=_ExtremePowerSupplyInputPowerUsage_Object((1,3,6,1,4,1,1916,1,1,1,27,1,9),_ExtremePowerSupplyInputPowerUsage_Type())
extremePowerSupplyInputPowerUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:extremePowerSupplyInputPowerUsage.setStatus(_A)
_ExtremePowerMonSupplyNumOutput_Type=Integer32
_ExtremePowerMonSupplyNumOutput_Object=MibTableColumn
extremePowerMonSupplyNumOutput=_ExtremePowerMonSupplyNumOutput_Object((1,3,6,1,4,1,1916,1,1,1,27,1,10),_ExtremePowerMonSupplyNumOutput_Type())
extremePowerMonSupplyNumOutput.setMaxAccess(_B)
if mibBuilder.loadTexts:extremePowerMonSupplyNumOutput.setStatus(_A)
_ExtremePowerSupplyInputPowerUsageUnitMultiplier_Type=UnitMultiplier
_ExtremePowerSupplyInputPowerUsageUnitMultiplier_Object=MibTableColumn
extremePowerSupplyInputPowerUsageUnitMultiplier=_ExtremePowerSupplyInputPowerUsageUnitMultiplier_Object((1,3,6,1,4,1,1916,1,1,1,27,1,11),_ExtremePowerSupplyInputPowerUsageUnitMultiplier_Type())
extremePowerSupplyInputPowerUsageUnitMultiplier.setMaxAccess(_B)
if mibBuilder.loadTexts:extremePowerSupplyInputPowerUsageUnitMultiplier.setStatus(_A)
_ExtremeCpuAggregateUtilization_Type=Integer32
_ExtremeCpuAggregateUtilization_Object=MibScalar
extremeCpuAggregateUtilization=_ExtremeCpuAggregateUtilization_Object((1,3,6,1,4,1,1916,1,1,1,28),_ExtremeCpuAggregateUtilization_Type())
extremeCpuAggregateUtilization.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeCpuAggregateUtilization.setStatus(_G)
_ExtremeCpuTask2Table_Object=MibTable
extremeCpuTask2Table=_ExtremeCpuTask2Table_Object((1,3,6,1,4,1,1916,1,1,1,29))
if mibBuilder.loadTexts:extremeCpuTask2Table.setStatus(_G)
_ExtremeCpuTask2Entry_Object=MibTableRow
extremeCpuTask2Entry=_ExtremeCpuTask2Entry_Object((1,3,6,1,4,1,1916,1,1,1,29,1))
extremeCpuTask2Entry.setIndexNames((0,_E,_a),(0,_E,_b))
if mibBuilder.loadTexts:extremeCpuTask2Entry.setStatus(_G)
_ExtremeCpuTask2CpuId_Type=Unsigned32
_ExtremeCpuTask2CpuId_Object=MibTableColumn
extremeCpuTask2CpuId=_ExtremeCpuTask2CpuId_Object((1,3,6,1,4,1,1916,1,1,1,29,1,1),_ExtremeCpuTask2CpuId_Type())
extremeCpuTask2CpuId.setMaxAccess(_c)
if mibBuilder.loadTexts:extremeCpuTask2CpuId.setStatus(_G)
class _ExtremeCpuTask2Name_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_ExtremeCpuTask2Name_Type.__name__=_F
_ExtremeCpuTask2Name_Object=MibTableColumn
extremeCpuTask2Name=_ExtremeCpuTask2Name_Object((1,3,6,1,4,1,1916,1,1,1,29,1,2),_ExtremeCpuTask2Name_Type())
extremeCpuTask2Name.setMaxAccess(_c)
if mibBuilder.loadTexts:extremeCpuTask2Name.setStatus(_G)
_ExtremeCpuTask2Id_Type=Unsigned32
_ExtremeCpuTask2Id_Object=MibTableColumn
extremeCpuTask2Id=_ExtremeCpuTask2Id_Object((1,3,6,1,4,1,1916,1,1,1,29,1,3),_ExtremeCpuTask2Id_Type())
extremeCpuTask2Id.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeCpuTask2Id.setStatus(_G)
_ExtremeCpuTask2Pc_Type=Unsigned32
_ExtremeCpuTask2Pc_Object=MibTableColumn
extremeCpuTask2Pc=_ExtremeCpuTask2Pc_Object((1,3,6,1,4,1,1916,1,1,1,29,1,4),_ExtremeCpuTask2Pc_Type())
extremeCpuTask2Pc.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeCpuTask2Pc.setStatus(_G)
_ExtremeCpuTask2Status_Type=DisplayString
_ExtremeCpuTask2Status_Object=MibTableColumn
extremeCpuTask2Status=_ExtremeCpuTask2Status_Object((1,3,6,1,4,1,1916,1,1,1,29,1,5),_ExtremeCpuTask2Status_Type())
extremeCpuTask2Status.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeCpuTask2Status.setStatus(_G)
_ExtremeCpuTask2Utilization_Type=Unsigned32
_ExtremeCpuTask2Utilization_Object=MibTableColumn
extremeCpuTask2Utilization=_ExtremeCpuTask2Utilization_Object((1,3,6,1,4,1,1916,1,1,1,29,1,6),_ExtremeCpuTask2Utilization_Type())
extremeCpuTask2Utilization.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeCpuTask2Utilization.setStatus(_G)
_ExtremeCpuTask2MaxUtilization_Type=Unsigned32
_ExtremeCpuTask2MaxUtilization_Object=MibTableColumn
extremeCpuTask2MaxUtilization=_ExtremeCpuTask2MaxUtilization_Object((1,3,6,1,4,1,1916,1,1,1,29,1,7),_ExtremeCpuTask2MaxUtilization_Type())
extremeCpuTask2MaxUtilization.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeCpuTask2MaxUtilization.setStatus(_G)
_ExtremeAuthFailSrcAddr_Type=IpAddress
_ExtremeAuthFailSrcAddr_Object=MibScalar
extremeAuthFailSrcAddr=_ExtremeAuthFailSrcAddr_Object((1,3,6,1,4,1,1916,1,1,1,30),_ExtremeAuthFailSrcAddr_Type())
extremeAuthFailSrcAddr.setMaxAccess(_I)
if mibBuilder.loadTexts:extremeAuthFailSrcAddr.setStatus(_G)
class _ExtremeCpuTransmitPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('normal',1),('high',2)))
_ExtremeCpuTransmitPriority_Type.__name__=_C
_ExtremeCpuTransmitPriority_Object=MibScalar
extremeCpuTransmitPriority=_ExtremeCpuTransmitPriority_Object((1,3,6,1,4,1,1916,1,1,1,31),_ExtremeCpuTransmitPriority_Type())
extremeCpuTransmitPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeCpuTransmitPriority.setStatus(_G)
class _ExtremeImageBooted_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_ExtremeImageBooted_Type.__name__=_C
_ExtremeImageBooted_Object=MibScalar
extremeImageBooted=_ExtremeImageBooted_Object((1,3,6,1,4,1,1916,1,1,1,32),_ExtremeImageBooted_Type())
extremeImageBooted.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeImageBooted.setStatus(_A)
class _ExtremeMsmFailoverCause_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('never',1),('admin',2),('exception',3),('removal',4),('hwFailure',5),('watchdog',6),('keepalive',7)))
_ExtremeMsmFailoverCause_Type.__name__=_C
_ExtremeMsmFailoverCause_Object=MibScalar
extremeMsmFailoverCause=_ExtremeMsmFailoverCause_Object((1,3,6,1,4,1,1916,1,1,1,33),_ExtremeMsmFailoverCause_Type())
extremeMsmFailoverCause.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeMsmFailoverCause.setStatus(_A)
_ExtremeImageTable_Object=MibTable
extremeImageTable=_ExtremeImageTable_Object((1,3,6,1,4,1,1916,1,1,1,34))
if mibBuilder.loadTexts:extremeImageTable.setStatus(_A)
_ExtremeImageEntry_Object=MibTableRow
extremeImageEntry=_ExtremeImageEntry_Object((1,3,6,1,4,1,1916,1,1,1,34,1))
extremeImageEntry.setIndexNames((0,_E,_d))
if mibBuilder.loadTexts:extremeImageEntry.setStatus(_A)
class _ExtremeImageNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('cur',0),('pri',1),('sec',2),('curr',3)))
_ExtremeImageNumber_Type.__name__=_C
_ExtremeImageNumber_Object=MibTableColumn
extremeImageNumber=_ExtremeImageNumber_Object((1,3,6,1,4,1,1916,1,1,1,34,1,1),_ExtremeImageNumber_Type())
extremeImageNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeImageNumber.setStatus(_A)
_ExtremeMajorVersion_Type=Integer32
_ExtremeMajorVersion_Object=MibTableColumn
extremeMajorVersion=_ExtremeMajorVersion_Object((1,3,6,1,4,1,1916,1,1,1,34,1,2),_ExtremeMajorVersion_Type())
extremeMajorVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeMajorVersion.setStatus(_A)
_ExtremeSubMajorVersion_Type=Integer32
_ExtremeSubMajorVersion_Object=MibTableColumn
extremeSubMajorVersion=_ExtremeSubMajorVersion_Object((1,3,6,1,4,1,1916,1,1,1,34,1,3),_ExtremeSubMajorVersion_Type())
extremeSubMajorVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeSubMajorVersion.setStatus(_G)
_ExtremeMinorVersion_Type=Integer32
_ExtremeMinorVersion_Object=MibTableColumn
extremeMinorVersion=_ExtremeMinorVersion_Object((1,3,6,1,4,1,1916,1,1,1,34,1,4),_ExtremeMinorVersion_Type())
extremeMinorVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeMinorVersion.setStatus(_A)
_ExtremeBuildNumber_Type=Integer32
_ExtremeBuildNumber_Object=MibTableColumn
extremeBuildNumber=_ExtremeBuildNumber_Object((1,3,6,1,4,1,1916,1,1,1,34,1,5),_ExtremeBuildNumber_Type())
extremeBuildNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeBuildNumber.setStatus(_A)
_ExtremeTechnologyReleaseNumber_Type=Integer32
_ExtremeTechnologyReleaseNumber_Object=MibTableColumn
extremeTechnologyReleaseNumber=_ExtremeTechnologyReleaseNumber_Object((1,3,6,1,4,1,1916,1,1,1,34,1,6),_ExtremeTechnologyReleaseNumber_Type())
extremeTechnologyReleaseNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeTechnologyReleaseNumber.setStatus(_A)
_ExtremeSustainingReleaseNumber_Type=Integer32
_ExtremeSustainingReleaseNumber_Object=MibTableColumn
extremeSustainingReleaseNumber=_ExtremeSustainingReleaseNumber_Object((1,3,6,1,4,1,1916,1,1,1,34,1,7),_ExtremeSustainingReleaseNumber_Type())
extremeSustainingReleaseNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeSustainingReleaseNumber.setStatus(_A)
_ExtremeBranchRevisionNumber_Type=Integer32
_ExtremeBranchRevisionNumber_Object=MibTableColumn
extremeBranchRevisionNumber=_ExtremeBranchRevisionNumber_Object((1,3,6,1,4,1,1916,1,1,1,34,1,8),_ExtremeBranchRevisionNumber_Type())
extremeBranchRevisionNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeBranchRevisionNumber.setStatus(_A)
class _ExtremeImageType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('trunk',0),('branch',1),('patch',2),('technology',3),('beta',4)))
_ExtremeImageType_Type.__name__=_C
_ExtremeImageType_Object=MibTableColumn
extremeImageType=_ExtremeImageType_Object((1,3,6,1,4,1,1916,1,1,1,34,1,9),_ExtremeImageType_Type())
extremeImageType.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeImageType.setStatus(_A)
class _ExtremeImageDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_ExtremeImageDescription_Type.__name__=_F
_ExtremeImageDescription_Object=MibTableColumn
extremeImageDescription=_ExtremeImageDescription_Object((1,3,6,1,4,1,1916,1,1,1,34,1,10),_ExtremeImageDescription_Type())
extremeImageDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeImageDescription.setStatus(_A)
class _ExtremeImageSecurity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_J,0),('nossh',1),('ssh',2)))
_ExtremeImageSecurity_Type.__name__=_C
_ExtremeImageSecurity_Object=MibTableColumn
extremeImageSecurity=_ExtremeImageSecurity_Object((1,3,6,1,4,1,1916,1,1,1,34,1,11),_ExtremeImageSecurity_Type())
extremeImageSecurity.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeImageSecurity.setStatus(_G)
_ExtremePatchVersion_Type=Integer32
_ExtremePatchVersion_Object=MibTableColumn
extremePatchVersion=_ExtremePatchVersion_Object((1,3,6,1,4,1,1916,1,1,1,34,1,12),_ExtremePatchVersion_Type())
extremePatchVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:extremePatchVersion.setStatus(_A)
_ExtremeImageFeatureTable_Object=MibTable
extremeImageFeatureTable=_ExtremeImageFeatureTable_Object((1,3,6,1,4,1,1916,1,1,1,35))
if mibBuilder.loadTexts:extremeImageFeatureTable.setStatus(_A)
_ExtremeImageFeatureEntry_Object=MibTableRow
extremeImageFeatureEntry=_ExtremeImageFeatureEntry_Object((1,3,6,1,4,1,1916,1,1,1,35,1))
extremeImageFeatureEntry.setIndexNames((0,_E,_e))
if mibBuilder.loadTexts:extremeImageFeatureEntry.setStatus(_A)
class _ExtremeImageFeatureNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('cur',0),('pri',1),('sec',2)))
_ExtremeImageFeatureNumber_Type.__name__=_C
_ExtremeImageFeatureNumber_Object=MibTableColumn
extremeImageFeatureNumber=_ExtremeImageFeatureNumber_Object((1,3,6,1,4,1,1916,1,1,1,35,1,1),_ExtremeImageFeatureNumber_Type())
extremeImageFeatureNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeImageFeatureNumber.setStatus(_A)
class _ExtremeImageSshCapability_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_J,0),('nossh',1),('ssh',2)))
_ExtremeImageSshCapability_Type.__name__=_C
_ExtremeImageSshCapability_Object=MibTableColumn
extremeImageSshCapability=_ExtremeImageSshCapability_Object((1,3,6,1,4,1,1916,1,1,1,35,1,2),_ExtremeImageSshCapability_Type())
extremeImageSshCapability.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeImageSshCapability.setStatus(_A)
class _ExtremeImageUAACapability_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_J,0),('nouaa',1),('uaa',2)))
_ExtremeImageUAACapability_Type.__name__=_C
_ExtremeImageUAACapability_Object=MibTableColumn
extremeImageUAACapability=_ExtremeImageUAACapability_Object((1,3,6,1,4,1,1916,1,1,1,35,1,3),_ExtremeImageUAACapability_Type())
extremeImageUAACapability.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeImageUAACapability.setStatus(_A)
class _ExtremeSystemPowerState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('computing',1),('sufficientButNotRedundantPower',2),('redundantPowerAvailable',3),('insufficientPower',4)))
_ExtremeSystemPowerState_Type.__name__=_C
_ExtremeSystemPowerState_Object=MibScalar
extremeSystemPowerState=_ExtremeSystemPowerState_Object((1,3,6,1,4,1,1916,1,1,1,36),_ExtremeSystemPowerState_Type())
extremeSystemPowerState.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeSystemPowerState.setStatus(_A)
_ExtremeBootTime_Type=Counter64
_ExtremeBootTime_Object=MibScalar
extremeBootTime=_ExtremeBootTime_Object((1,3,6,1,4,1,1916,1,1,1,37),_ExtremeBootTime_Type())
extremeBootTime.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeBootTime.setStatus(_A)
_ExtremePowerSupplyOutputPowerTable_Object=MibTable
extremePowerSupplyOutputPowerTable=_ExtremePowerSupplyOutputPowerTable_Object((1,3,6,1,4,1,1916,1,1,1,38))
if mibBuilder.loadTexts:extremePowerSupplyOutputPowerTable.setStatus(_A)
_ExtremePowerSupplyOutputPowerEntry_Object=MibTableRow
extremePowerSupplyOutputPowerEntry=_ExtremePowerSupplyOutputPowerEntry_Object((1,3,6,1,4,1,1916,1,1,1,38,1))
extremePowerSupplyOutputPowerEntry.setIndexNames((0,_E,_f),(0,_E,_g))
if mibBuilder.loadTexts:extremePowerSupplyOutputPowerEntry.setStatus(_A)
_ExtremePowerSupplyIndex_Type=Integer32
_ExtremePowerSupplyIndex_Object=MibTableColumn
extremePowerSupplyIndex=_ExtremePowerSupplyIndex_Object((1,3,6,1,4,1,1916,1,1,1,38,1,1),_ExtremePowerSupplyIndex_Type())
extremePowerSupplyIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:extremePowerSupplyIndex.setStatus(_A)
_ExtremePowerSupplyOutputSensorIdx_Type=Integer32
_ExtremePowerSupplyOutputSensorIdx_Object=MibTableColumn
extremePowerSupplyOutputSensorIdx=_ExtremePowerSupplyOutputSensorIdx_Object((1,3,6,1,4,1,1916,1,1,1,38,1,2),_ExtremePowerSupplyOutputSensorIdx_Type())
extremePowerSupplyOutputSensorIdx.setMaxAccess(_B)
if mibBuilder.loadTexts:extremePowerSupplyOutputSensorIdx.setStatus(_A)
_ExtremePowerSupplyOutputVoltage_Type=Integer32
_ExtremePowerSupplyOutputVoltage_Object=MibTableColumn
extremePowerSupplyOutputVoltage=_ExtremePowerSupplyOutputVoltage_Object((1,3,6,1,4,1,1916,1,1,1,38,1,3),_ExtremePowerSupplyOutputVoltage_Type())
extremePowerSupplyOutputVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:extremePowerSupplyOutputVoltage.setStatus(_A)
_ExtremePowerSupplyOutputCurrent_Type=Integer32
_ExtremePowerSupplyOutputCurrent_Object=MibTableColumn
extremePowerSupplyOutputCurrent=_ExtremePowerSupplyOutputCurrent_Object((1,3,6,1,4,1,1916,1,1,1,38,1,4),_ExtremePowerSupplyOutputCurrent_Type())
extremePowerSupplyOutputCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:extremePowerSupplyOutputCurrent.setStatus(_A)
_ExtremePowerSupplyOutputUnitMultiplier_Type=UnitMultiplier
_ExtremePowerSupplyOutputUnitMultiplier_Object=MibTableColumn
extremePowerSupplyOutputUnitMultiplier=_ExtremePowerSupplyOutputUnitMultiplier_Object((1,3,6,1,4,1,1916,1,1,1,38,1,5),_ExtremePowerSupplyOutputUnitMultiplier_Type())
extremePowerSupplyOutputUnitMultiplier.setMaxAccess(_B)
if mibBuilder.loadTexts:extremePowerSupplyOutputUnitMultiplier.setStatus(_A)
_ExtremePowerSupplyUsageTable_Object=MibTable
extremePowerSupplyUsageTable=_ExtremePowerSupplyUsageTable_Object((1,3,6,1,4,1,1916,1,1,1,39))
if mibBuilder.loadTexts:extremePowerSupplyUsageTable.setStatus(_A)
_ExtremePowerSupplyUsageEntry_Object=MibTableRow
extremePowerSupplyUsageEntry=_ExtremePowerSupplyUsageEntry_Object((1,3,6,1,4,1,1916,1,1,1,39,1))
extremePowerSupplyUsageEntry.setIndexNames((0,_E,_h))
if mibBuilder.loadTexts:extremePowerSupplyUsageEntry.setStatus(_A)
_ExtremeSlotIndex_Type=Integer32
_ExtremeSlotIndex_Object=MibTableColumn
extremeSlotIndex=_ExtremeSlotIndex_Object((1,3,6,1,4,1,1916,1,1,1,39,1,1),_ExtremeSlotIndex_Type())
extremeSlotIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeSlotIndex.setStatus(_A)
_ExtremePowerSupplyUsageValue_Type=Integer32
_ExtremePowerSupplyUsageValue_Object=MibTableColumn
extremePowerSupplyUsageValue=_ExtremePowerSupplyUsageValue_Object((1,3,6,1,4,1,1916,1,1,1,39,1,2),_ExtremePowerSupplyUsageValue_Type())
extremePowerSupplyUsageValue.setMaxAccess(_B)
if mibBuilder.loadTexts:extremePowerSupplyUsageValue.setStatus(_A)
_ExtremePowerSupplyUnitMultiplier_Type=UnitMultiplier
_ExtremePowerSupplyUnitMultiplier_Object=MibTableColumn
extremePowerSupplyUnitMultiplier=_ExtremePowerSupplyUnitMultiplier_Object((1,3,6,1,4,1,1916,1,1,1,39,1,3),_ExtremePowerSupplyUnitMultiplier_Type())
extremePowerSupplyUnitMultiplier.setMaxAccess(_B)
if mibBuilder.loadTexts:extremePowerSupplyUnitMultiplier.setStatus(_A)
_ExtremeSystemPowerUsage_ObjectIdentity=ObjectIdentity
extremeSystemPowerUsage=_ExtremeSystemPowerUsage_ObjectIdentity((1,3,6,1,4,1,1916,1,1,1,40))
_ExtremeSystemPowerUsageValue_Type=Integer32
_ExtremeSystemPowerUsageValue_Object=MibScalar
extremeSystemPowerUsageValue=_ExtremeSystemPowerUsageValue_Object((1,3,6,1,4,1,1916,1,1,1,40,1),_ExtremeSystemPowerUsageValue_Type())
extremeSystemPowerUsageValue.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeSystemPowerUsageValue.setStatus(_A)
_ExtremeSystemPowerUsageUnitMultiplier_Type=UnitMultiplier
_ExtremeSystemPowerUsageUnitMultiplier_Object=MibScalar
extremeSystemPowerUsageUnitMultiplier=_ExtremeSystemPowerUsageUnitMultiplier_Object((1,3,6,1,4,1,1916,1,1,1,40,2),_ExtremeSystemPowerUsageUnitMultiplier_Type())
extremeSystemPowerUsageUnitMultiplier.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeSystemPowerUsageUnitMultiplier.setStatus(_A)
_ExtremeSystemPowerMonitorTable_Object=MibTable
extremeSystemPowerMonitorTable=_ExtremeSystemPowerMonitorTable_Object((1,3,6,1,4,1,1916,1,1,1,41))
if mibBuilder.loadTexts:extremeSystemPowerMonitorTable.setStatus(_A)
_ExtremeSystemPowerMonitorEntry_Object=MibTableRow
extremeSystemPowerMonitorEntry=_ExtremeSystemPowerMonitorEntry_Object((1,3,6,1,4,1,1916,1,1,1,41,1))
extremeSystemPowerMonitorEntry.setIndexNames((0,_E,_i))
if mibBuilder.loadTexts:extremeSystemPowerMonitorEntry.setStatus(_A)
_ExtremeSystemPowerMonitorIndex1_Type=Integer32
_ExtremeSystemPowerMonitorIndex1_Object=MibTableColumn
extremeSystemPowerMonitorIndex1=_ExtremeSystemPowerMonitorIndex1_Object((1,3,6,1,4,1,1916,1,1,1,41,1,1),_ExtremeSystemPowerMonitorIndex1_Type())
extremeSystemPowerMonitorIndex1.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeSystemPowerMonitorIndex1.setStatus(_A)
class _ExtremeSystemPowerMonitorPollInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,300))
_ExtremeSystemPowerMonitorPollInterval_Type.__name__=_C
_ExtremeSystemPowerMonitorPollInterval_Object=MibTableColumn
extremeSystemPowerMonitorPollInterval=_ExtremeSystemPowerMonitorPollInterval_Object((1,3,6,1,4,1,1916,1,1,1,41,1,2),_ExtremeSystemPowerMonitorPollInterval_Type())
extremeSystemPowerMonitorPollInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeSystemPowerMonitorPollInterval.setStatus(_A)
class _ExtremeSystemPowerMonitorReportChanges_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('none',1),('log',2),('trap',3),('logandtrap',4)))
_ExtremeSystemPowerMonitorReportChanges_Type.__name__=_C
_ExtremeSystemPowerMonitorReportChanges_Object=MibTableColumn
extremeSystemPowerMonitorReportChanges=_ExtremeSystemPowerMonitorReportChanges_Object((1,3,6,1,4,1,1916,1,1,1,41,1,3),_ExtremeSystemPowerMonitorReportChanges_Type())
extremeSystemPowerMonitorReportChanges.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeSystemPowerMonitorReportChanges.setStatus(_A)
_ExtremeSystemPowerMonitorChangeThreshold_Type=Integer32
_ExtremeSystemPowerMonitorChangeThreshold_Object=MibTableColumn
extremeSystemPowerMonitorChangeThreshold=_ExtremeSystemPowerMonitorChangeThreshold_Object((1,3,6,1,4,1,1916,1,1,1,41,1,4),_ExtremeSystemPowerMonitorChangeThreshold_Type())
extremeSystemPowerMonitorChangeThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeSystemPowerMonitorChangeThreshold.setStatus(_A)
_ExtremeRebootTable_Object=MibTable
extremeRebootTable=_ExtremeRebootTable_Object((1,3,6,1,4,1,1916,1,1,1,42))
if mibBuilder.loadTexts:extremeRebootTable.setStatus(_A)
_RebootTimeEntry_Object=MibTableRow
rebootTimeEntry=_RebootTimeEntry_Object((1,3,6,1,4,1,1916,1,1,1,42,1))
rebootTimeEntry.setIndexNames((0,_E,_j))
if mibBuilder.loadTexts:rebootTimeEntry.setStatus(_A)
class _ExtremeRebootSlotId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ExtremeRebootSlotId_Type.__name__=_C
_ExtremeRebootSlotId_Object=MibTableColumn
extremeRebootSlotId=_ExtremeRebootSlotId_Object((1,3,6,1,4,1,1916,1,1,1,42,1,1),_ExtremeRebootSlotId_Type())
extremeRebootSlotId.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeRebootSlotId.setStatus(_A)
_ExtremeRebootNodeAddress_Type=MacAddress
_ExtremeRebootNodeAddress_Object=MibTableColumn
extremeRebootNodeAddress=_ExtremeRebootNodeAddress_Object((1,3,6,1,4,1,1916,1,1,1,42,1,2),_ExtremeRebootNodeAddress_Type())
extremeRebootNodeAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeRebootNodeAddress.setStatus(_A)
_ExtremeRebootModuleSlotId_Type=DisplayString
_ExtremeRebootModuleSlotId_Object=MibTableColumn
extremeRebootModuleSlotId=_ExtremeRebootModuleSlotId_Object((1,3,6,1,4,1,1916,1,1,1,42,1,3),_ExtremeRebootModuleSlotId_Type())
extremeRebootModuleSlotId.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeRebootModuleSlotId.setStatus(_A)
_ExtremeRebootSlotNumber_Type=Integer32
_ExtremeRebootSlotNumber_Object=MibTableColumn
extremeRebootSlotNumber=_ExtremeRebootSlotNumber_Object((1,3,6,1,4,1,1916,1,1,1,42,1,4),_ExtremeRebootSlotNumber_Type())
extremeRebootSlotNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeRebootSlotNumber.setStatus(_A)
class _ExtremeRebootAsStandby_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_ExtremeRebootAsStandby_Type.__name__=_C
_ExtremeRebootAsStandby_Object=MibTableColumn
extremeRebootAsStandby=_ExtremeRebootAsStandby_Object((1,3,6,1,4,1,1916,1,1,1,42,1,5),_ExtremeRebootAsStandby_Type())
extremeRebootAsStandby.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeRebootAsStandby.setStatus(_A)
class _ExtremeRebootStackTopology_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_ExtremeRebootStackTopology_Type.__name__=_C
_ExtremeRebootStackTopology_Object=MibTableColumn
extremeRebootStackTopology=_ExtremeRebootStackTopology_Object((1,3,6,1,4,1,1916,1,1,1,42,1,6),_ExtremeRebootStackTopology_Type())
extremeRebootStackTopology.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeRebootStackTopology.setStatus(_A)
class _ExtremeRebootMonth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,12))
_ExtremeRebootMonth_Type.__name__=_C
_ExtremeRebootMonth_Object=MibTableColumn
extremeRebootMonth=_ExtremeRebootMonth_Object((1,3,6,1,4,1,1916,1,1,1,42,1,7),_ExtremeRebootMonth_Type())
extremeRebootMonth.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeRebootMonth.setStatus(_A)
class _ExtremeRebootDay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,31))
_ExtremeRebootDay_Type.__name__=_C
_ExtremeRebootDay_Object=MibTableColumn
extremeRebootDay=_ExtremeRebootDay_Object((1,3,6,1,4,1,1916,1,1,1,42,1,8),_ExtremeRebootDay_Type())
extremeRebootDay.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeRebootDay.setStatus(_A)
class _ExtremeRebootYear_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2003,2036))
_ExtremeRebootYear_Type.__name__=_C
_ExtremeRebootYear_Object=MibTableColumn
extremeRebootYear=_ExtremeRebootYear_Object((1,3,6,1,4,1,1916,1,1,1,42,1,9),_ExtremeRebootYear_Type())
extremeRebootYear.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeRebootYear.setStatus(_A)
class _ExtremeRebootHour_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,23))
_ExtremeRebootHour_Type.__name__=_C
_ExtremeRebootHour_Object=MibTableColumn
extremeRebootHour=_ExtremeRebootHour_Object((1,3,6,1,4,1,1916,1,1,1,42,1,10),_ExtremeRebootHour_Type())
extremeRebootHour.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeRebootHour.setStatus(_A)
class _ExtremeRebootMinute_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,59))
_ExtremeRebootMinute_Type.__name__=_C
_ExtremeRebootMinute_Object=MibTableColumn
extremeRebootMinute=_ExtremeRebootMinute_Object((1,3,6,1,4,1,1916,1,1,1,42,1,11),_ExtremeRebootMinute_Type())
extremeRebootMinute.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeRebootMinute.setStatus(_A)
class _ExtremeRebootSeconds_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,59))
_ExtremeRebootSeconds_Type.__name__=_C
_ExtremeRebootSeconds_Object=MibTableColumn
extremeRebootSeconds=_ExtremeRebootSeconds_Object((1,3,6,1,4,1,1916,1,1,1,42,1,12),_ExtremeRebootSeconds_Type())
extremeRebootSeconds.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeRebootSeconds.setStatus(_A)
class _ExtremeRebootCancel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_ExtremeRebootCancel_Type.__name__=_C
_ExtremeRebootCancel_Object=MibTableColumn
extremeRebootCancel=_ExtremeRebootCancel_Object((1,3,6,1,4,1,1916,1,1,1,42,1,13),_ExtremeRebootCancel_Type())
extremeRebootCancel.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeRebootCancel.setStatus(_A)
class _ExtremeRebootImmediate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_ExtremeRebootImmediate_Type.__name__=_C
_ExtremeRebootImmediate_Object=MibTableColumn
extremeRebootImmediate=_ExtremeRebootImmediate_Object((1,3,6,1,4,1,1916,1,1,1,42,1,14),_ExtremeRebootImmediate_Type())
extremeRebootImmediate.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeRebootImmediate.setStatus(_A)
_ExtremeRebootRowStatus_Type=RowStatus
_ExtremeRebootRowStatus_Object=MibTableColumn
extremeRebootRowStatus=_ExtremeRebootRowStatus_Object((1,3,6,1,4,1,1916,1,1,1,42,1,15),_ExtremeRebootRowStatus_Type())
extremeRebootRowStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:extremeRebootRowStatus.setStatus(_A)
_ExtremeDownloadImageTable_Object=MibTable
extremeDownloadImageTable=_ExtremeDownloadImageTable_Object((1,3,6,1,4,1,1916,1,1,1,43))
if mibBuilder.loadTexts:extremeDownloadImageTable.setStatus(_A)
_ExtremeDownloadImageEntry_Object=MibTableRow
extremeDownloadImageEntry=_ExtremeDownloadImageEntry_Object((1,3,6,1,4,1,1916,1,1,1,43,1))
extremeDownloadImageEntry.setIndexNames((0,_E,_U))
if mibBuilder.loadTexts:extremeDownloadImageEntry.setStatus(_A)
class _ExtremeDownloadImageSlotId_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ExtremeDownloadImageSlotId_Type.__name__=_C
_ExtremeDownloadImageSlotId_Object=MibTableColumn
extremeDownloadImageSlotId=_ExtremeDownloadImageSlotId_Object((1,3,6,1,4,1,1916,1,1,1,43,1,1),_ExtremeDownloadImageSlotId_Type())
extremeDownloadImageSlotId.setMaxAccess(_H)
if mibBuilder.loadTexts:extremeDownloadImageSlotId.setStatus(_A)
class _ExtremeDownloadImageStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)));namedValues=NamedValues(*(('downloadInProgress',1),('downloadOperationSuccess',2),('downloadNotPrimary',3),('downloadNameLengthError',4),('downloadInvalidFileType',5),('downloadActivePartitionError',6),('downloadIllegalHostname',7),('downloadFailed',8),('downloadInvalidIpaddr',9),('downloadMemAllocFailed',10),('downloadNotInActiveTop',11),('downloadMissingFileName',12),('downloadIllegalFileName',13),('downloadOperationTimeout',14),('downloadInvalidRowStatus',15)))
_ExtremeDownloadImageStatus_Type.__name__=_C
_ExtremeDownloadImageStatus_Object=MibTableColumn
extremeDownloadImageStatus=_ExtremeDownloadImageStatus_Object((1,3,6,1,4,1,1916,1,1,1,43,1,2),_ExtremeDownloadImageStatus_Type())
extremeDownloadImageStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:extremeDownloadImageStatus.setStatus(_A)
class _ExtremeDownloadImageFilename_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_ExtremeDownloadImageFilename_Type.__name__=_F
_ExtremeDownloadImageFilename_Object=MibTableColumn
extremeDownloadImageFilename=_ExtremeDownloadImageFilename_Object((1,3,6,1,4,1,1916,1,1,1,43,1,3),_ExtremeDownloadImageFilename_Type())
extremeDownloadImageFilename.setMaxAccess(_H)
if mibBuilder.loadTexts:extremeDownloadImageFilename.setStatus(_A)
class _ExtremeDownloadImagePartition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_ExtremeDownloadImagePartition_Type.__name__=_C
_ExtremeDownloadImagePartition_Object=MibTableColumn
extremeDownloadImagePartition=_ExtremeDownloadImagePartition_Object((1,3,6,1,4,1,1916,1,1,1,43,1,4),_ExtremeDownloadImagePartition_Type())
extremeDownloadImagePartition.setMaxAccess(_H)
if mibBuilder.loadTexts:extremeDownloadImagePartition.setStatus(_A)
class _ExtremeDownloadImageHostName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_ExtremeDownloadImageHostName_Type.__name__=_F
_ExtremeDownloadImageHostName_Object=MibTableColumn
extremeDownloadImageHostName=_ExtremeDownloadImageHostName_Object((1,3,6,1,4,1,1916,1,1,1,43,1,5),_ExtremeDownloadImageHostName_Type())
extremeDownloadImageHostName.setMaxAccess(_H)
if mibBuilder.loadTexts:extremeDownloadImageHostName.setStatus(_A)
class _ExtremeDownloadImageIpaddress_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_ExtremeDownloadImageIpaddress_Type.__name__=_F
_ExtremeDownloadImageIpaddress_Object=MibTableColumn
extremeDownloadImageIpaddress=_ExtremeDownloadImageIpaddress_Object((1,3,6,1,4,1,1916,1,1,1,43,1,6),_ExtremeDownloadImageIpaddress_Type())
extremeDownloadImageIpaddress.setMaxAccess(_H)
if mibBuilder.loadTexts:extremeDownloadImageIpaddress.setStatus(_A)
class _ExtremeDownloadImageStartTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_ExtremeDownloadImageStartTime_Type.__name__=_F
_ExtremeDownloadImageStartTime_Object=MibTableColumn
extremeDownloadImageStartTime=_ExtremeDownloadImageStartTime_Object((1,3,6,1,4,1,1916,1,1,1,43,1,7),_ExtremeDownloadImageStartTime_Type())
extremeDownloadImageStartTime.setMaxAccess(_H)
if mibBuilder.loadTexts:extremeDownloadImageStartTime.setStatus(_A)
class _ExtremeDownloadImageMemorycard_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_ExtremeDownloadImageMemorycard_Type.__name__=_C
_ExtremeDownloadImageMemorycard_Object=MibTableColumn
extremeDownloadImageMemorycard=_ExtremeDownloadImageMemorycard_Object((1,3,6,1,4,1,1916,1,1,1,43,1,8),_ExtremeDownloadImageMemorycard_Type())
extremeDownloadImageMemorycard.setMaxAccess(_H)
if mibBuilder.loadTexts:extremeDownloadImageMemorycard.setStatus(_A)
class _ExtremeDownloadImageInstall_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_ExtremeDownloadImageInstall_Type.__name__=_C
_ExtremeDownloadImageInstall_Object=MibTableColumn
extremeDownloadImageInstall=_ExtremeDownloadImageInstall_Object((1,3,6,1,4,1,1916,1,1,1,43,1,9),_ExtremeDownloadImageInstall_Type())
extremeDownloadImageInstall.setMaxAccess(_H)
if mibBuilder.loadTexts:extremeDownloadImageInstall.setStatus(_A)
class _ExtremeDownloadSlotNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_ExtremeDownloadSlotNumber_Type.__name__=_C
_ExtremeDownloadSlotNumber_Object=MibTableColumn
extremeDownloadSlotNumber=_ExtremeDownloadSlotNumber_Object((1,3,6,1,4,1,1916,1,1,1,43,1,10),_ExtremeDownloadSlotNumber_Type())
extremeDownloadSlotNumber.setMaxAccess(_H)
if mibBuilder.loadTexts:extremeDownloadSlotNumber.setStatus(_A)
_ExtremeDownloadModuleSlotId_Type=DisplayString
_ExtremeDownloadModuleSlotId_Object=MibTableColumn
extremeDownloadModuleSlotId=_ExtremeDownloadModuleSlotId_Object((1,3,6,1,4,1,1916,1,1,1,43,1,11),_ExtremeDownloadModuleSlotId_Type())
extremeDownloadModuleSlotId.setMaxAccess(_H)
if mibBuilder.loadTexts:extremeDownloadModuleSlotId.setStatus(_A)
_ExtremeDownloadRowStatus_Type=RowStatus
_ExtremeDownloadRowStatus_Object=MibTableColumn
extremeDownloadRowStatus=_ExtremeDownloadRowStatus_Object((1,3,6,1,4,1,1916,1,1,1,43,1,12),_ExtremeDownloadRowStatus_Type())
extremeDownloadRowStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:extremeDownloadRowStatus.setStatus(_A)
class _ExtremeDownloadBlockSize_Type(Integer32):defaultValue=1400;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(24,65000))
_ExtremeDownloadBlockSize_Type.__name__=_C
_ExtremeDownloadBlockSize_Object=MibTableColumn
extremeDownloadBlockSize=_ExtremeDownloadBlockSize_Object((1,3,6,1,4,1,1916,1,1,1,43,1,13),_ExtremeDownloadBlockSize_Type())
extremeDownloadBlockSize.setMaxAccess(_H)
if mibBuilder.loadTexts:extremeDownloadBlockSize.setStatus(_A)
_ExtremeInstallImageTable_Object=MibTable
extremeInstallImageTable=_ExtremeInstallImageTable_Object((1,3,6,1,4,1,1916,1,1,1,44))
if mibBuilder.loadTexts:extremeInstallImageTable.setStatus(_A)
_ExtremeInstallImageEntry_Object=MibTableRow
extremeInstallImageEntry=_ExtremeInstallImageEntry_Object((1,3,6,1,4,1,1916,1,1,1,44,1))
extremeInstallImageEntry.setIndexNames((0,_E,_V))
if mibBuilder.loadTexts:extremeInstallImageEntry.setStatus(_A)
class _ExtremeInstallImageSlotId_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ExtremeInstallImageSlotId_Type.__name__=_C
_ExtremeInstallImageSlotId_Object=MibTableColumn
extremeInstallImageSlotId=_ExtremeInstallImageSlotId_Object((1,3,6,1,4,1,1916,1,1,1,44,1,1),_ExtremeInstallImageSlotId_Type())
extremeInstallImageSlotId.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeInstallImageSlotId.setStatus(_A)
class _ExtremeInstallImageStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)));namedValues=NamedValues(*(('installInProgress',1),('installOperationSuccess',2),('installOperationPending',3),('installNameLengthError',4),('installInvalidFileType',5),('installActivePartitionError',6),('installDwnloadSlotMismatch',7),('installFailed',8),('installNotPrimary',9),('installMemAllocFailed',10),('installNotInActiveTop',11),('installMissingFileName',12),('installIllegalFileName',13),('installOperationTimeout',14),('installOperBackupTimeout',15),('installInvalidRowStatus',16)))
_ExtremeInstallImageStatus_Type.__name__=_C
_ExtremeInstallImageStatus_Object=MibTableColumn
extremeInstallImageStatus=_ExtremeInstallImageStatus_Object((1,3,6,1,4,1,1916,1,1,1,44,1,2),_ExtremeInstallImageStatus_Type())
extremeInstallImageStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeInstallImageStatus.setStatus(_A)
class _ExtremeInstallImageFilename_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_ExtremeInstallImageFilename_Type.__name__=_F
_ExtremeInstallImageFilename_Object=MibTableColumn
extremeInstallImageFilename=_ExtremeInstallImageFilename_Object((1,3,6,1,4,1,1916,1,1,1,44,1,3),_ExtremeInstallImageFilename_Type())
extremeInstallImageFilename.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeInstallImageFilename.setStatus(_A)
class _ExtremeInstallImagePartition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_ExtremeInstallImagePartition_Type.__name__=_C
_ExtremeInstallImagePartition_Object=MibTableColumn
extremeInstallImagePartition=_ExtremeInstallImagePartition_Object((1,3,6,1,4,1,1916,1,1,1,44,1,4),_ExtremeInstallImagePartition_Type())
extremeInstallImagePartition.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeInstallImagePartition.setStatus(_A)
class _ExtremeInstallImageStartTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_ExtremeInstallImageStartTime_Type.__name__=_F
_ExtremeInstallImageStartTime_Object=MibTableColumn
extremeInstallImageStartTime=_ExtremeInstallImageStartTime_Object((1,3,6,1,4,1,1916,1,1,1,44,1,5),_ExtremeInstallImageStartTime_Type())
extremeInstallImageStartTime.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeInstallImageStartTime.setStatus(_A)
class _ExtremeInstallImageReboot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_ExtremeInstallImageReboot_Type.__name__=_C
_ExtremeInstallImageReboot_Object=MibTableColumn
extremeInstallImageReboot=_ExtremeInstallImageReboot_Object((1,3,6,1,4,1,1916,1,1,1,44,1,6),_ExtremeInstallImageReboot_Type())
extremeInstallImageReboot.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeInstallImageReboot.setStatus(_A)
_ExtremeInstallImageModuleSlotId_Type=DisplayString
_ExtremeInstallImageModuleSlotId_Object=MibTableColumn
extremeInstallImageModuleSlotId=_ExtremeInstallImageModuleSlotId_Object((1,3,6,1,4,1,1916,1,1,1,44,1,7),_ExtremeInstallImageModuleSlotId_Type())
extremeInstallImageModuleSlotId.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeInstallImageModuleSlotId.setStatus(_A)
class _ExtremeInstallImageSlotNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_ExtremeInstallImageSlotNumber_Type.__name__=_C
_ExtremeInstallImageSlotNumber_Object=MibTableColumn
extremeInstallImageSlotNumber=_ExtremeInstallImageSlotNumber_Object((1,3,6,1,4,1,1916,1,1,1,44,1,8),_ExtremeInstallImageSlotNumber_Type())
extremeInstallImageSlotNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeInstallImageSlotNumber.setStatus(_A)
_ExtremeInstallImageRowStatus_Type=RowStatus
_ExtremeInstallImageRowStatus_Object=MibTableColumn
extremeInstallImageRowStatus=_ExtremeInstallImageRowStatus_Object((1,3,6,1,4,1,1916,1,1,1,44,1,9),_ExtremeInstallImageRowStatus_Type())
extremeInstallImageRowStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:extremeInstallImageRowStatus.setStatus(_A)
_ExtremeLoadInstallTrap_ObjectIdentity=ObjectIdentity
extremeLoadInstallTrap=_ExtremeLoadInstallTrap_ObjectIdentity((1,3,6,1,4,1,1916,1,1,1,45))
_LoadInstallControl_ObjectIdentity=ObjectIdentity
loadInstallControl=_LoadInstallControl_ObjectIdentity((1,3,6,1,4,1,1916,1,1,1,45,1))
class _DownloadImageTrapEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('yes',1),('no',2)))
_DownloadImageTrapEnable_Type.__name__=_C
_DownloadImageTrapEnable_Object=MibScalar
downloadImageTrapEnable=_DownloadImageTrapEnable_Object((1,3,6,1,4,1,1916,1,1,1,45,1,1),_DownloadImageTrapEnable_Type())
downloadImageTrapEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:downloadImageTrapEnable.setStatus(_A)
class _InstallImageTrapEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('yes',1),('no',2)))
_InstallImageTrapEnable_Type.__name__=_C
_InstallImageTrapEnable_Object=MibScalar
installImageTrapEnable=_InstallImageTrapEnable_Object((1,3,6,1,4,1,1916,1,1,1,45,1,2),_InstallImageTrapEnable_Type())
installImageTrapEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:installImageTrapEnable.setStatus(_A)
_LoadInstallTraps_ObjectIdentity=ObjectIdentity
loadInstallTraps=_LoadInstallTraps_ObjectIdentity((1,3,6,1,4,1,1916,1,1,1,45,2))
class _ExtremeSaveConfigurationFileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_ExtremeSaveConfigurationFileName_Type.__name__=_F
_ExtremeSaveConfigurationFileName_Object=MibScalar
extremeSaveConfigurationFileName=_ExtremeSaveConfigurationFileName_Object((1,3,6,1,4,1,1916,1,1,1,48),_ExtremeSaveConfigurationFileName_Type())
extremeSaveConfigurationFileName.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeSaveConfigurationFileName.setStatus(_A)
class _ExtremeUseOnRebootFileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_ExtremeUseOnRebootFileName_Type.__name__=_F
_ExtremeUseOnRebootFileName_Object=MibScalar
extremeUseOnRebootFileName=_ExtremeUseOnRebootFileName_Object((1,3,6,1,4,1,1916,1,1,1,49),_ExtremeUseOnRebootFileName_Type())
extremeUseOnRebootFileName.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeUseOnRebootFileName.setStatus(_A)
_ExtremeAuthFailSrcAddressType_Type=InetAddressType
_ExtremeAuthFailSrcAddressType_Object=MibScalar
extremeAuthFailSrcAddressType=_ExtremeAuthFailSrcAddressType_Object((1,3,6,1,4,1,1916,1,1,1,50),_ExtremeAuthFailSrcAddressType_Type())
extremeAuthFailSrcAddressType.setMaxAccess(_I)
if mibBuilder.loadTexts:extremeAuthFailSrcAddressType.setStatus(_A)
_ExtremeAuthFailSrcAddress_Type=InetAddress
_ExtremeAuthFailSrcAddress_Object=MibScalar
extremeAuthFailSrcAddress=_ExtremeAuthFailSrcAddress_Object((1,3,6,1,4,1,1916,1,1,1,51),_ExtremeAuthFailSrcAddress_Type())
extremeAuthFailSrcAddress.setMaxAccess(_I)
if mibBuilder.loadTexts:extremeAuthFailSrcAddress.setStatus(_A)
class _ExtremeAuthFailSrcAddressVrName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ExtremeAuthFailSrcAddressVrName_Type.__name__=_F
_ExtremeAuthFailSrcAddressVrName_Object=MibScalar
extremeAuthFailSrcAddressVrName=_ExtremeAuthFailSrcAddressVrName_Object((1,3,6,1,4,1,1916,1,1,1,52),_ExtremeAuthFailSrcAddressVrName_Type())
extremeAuthFailSrcAddressVrName.setMaxAccess(_I)
if mibBuilder.loadTexts:extremeAuthFailSrcAddressVrName.setStatus(_A)
_ExtremeAutoSave_ObjectIdentity=ObjectIdentity
extremeAutoSave=_ExtremeAutoSave_ObjectIdentity((1,3,6,1,4,1,1916,1,1,1,53))
class _ExtremeAutoSaveConfigurationFileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_ExtremeAutoSaveConfigurationFileName_Type.__name__=_F
_ExtremeAutoSaveConfigurationFileName_Object=MibScalar
extremeAutoSaveConfigurationFileName=_ExtremeAutoSaveConfigurationFileName_Object((1,3,6,1,4,1,1916,1,1,1,53,1),_ExtremeAutoSaveConfigurationFileName_Type())
extremeAutoSaveConfigurationFileName.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeAutoSaveConfigurationFileName.setStatus(_A)
class _ExtremeAutoSaveConfigurationEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('disable',0),('enable',1)))
_ExtremeAutoSaveConfigurationEnabled_Type.__name__=_C
_ExtremeAutoSaveConfigurationEnabled_Object=MibScalar
extremeAutoSaveConfigurationEnabled=_ExtremeAutoSaveConfigurationEnabled_Object((1,3,6,1,4,1,1916,1,1,1,53,2),_ExtremeAutoSaveConfigurationEnabled_Type())
extremeAutoSaveConfigurationEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeAutoSaveConfigurationEnabled.setStatus(_A)
class _ExtremeAutoSaveConfigurationTimeInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,1440))
_ExtremeAutoSaveConfigurationTimeInterval_Type.__name__=_C
_ExtremeAutoSaveConfigurationTimeInterval_Object=MibScalar
extremeAutoSaveConfigurationTimeInterval=_ExtremeAutoSaveConfigurationTimeInterval_Object((1,3,6,1,4,1,1916,1,1,1,53,3),_ExtremeAutoSaveConfigurationTimeInterval_Type())
extremeAutoSaveConfigurationTimeInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeAutoSaveConfigurationTimeInterval.setStatus(_A)
_ExtremeChassisGroup_ObjectIdentity=ObjectIdentity
extremeChassisGroup=_ExtremeChassisGroup_ObjectIdentity((1,3,6,1,4,1,1916,1,1,2))
_ExtremeMasterMSMSlot_Type=Integer32
_ExtremeMasterMSMSlot_Object=MibScalar
extremeMasterMSMSlot=_ExtremeMasterMSMSlot_Object((1,3,6,1,4,1,1916,1,1,2,1),_ExtremeMasterMSMSlot_Type())
extremeMasterMSMSlot.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeMasterMSMSlot.setStatus(_A)
_ExtremeSlotTable_Object=MibTable
extremeSlotTable=_ExtremeSlotTable_Object((1,3,6,1,4,1,1916,1,1,2,2))
if mibBuilder.loadTexts:extremeSlotTable.setStatus(_A)
_ExtremeSlotEntry_Object=MibTableRow
extremeSlotEntry=_ExtremeSlotEntry_Object((1,3,6,1,4,1,1916,1,1,2,2,1))
extremeSlotEntry.setIndexNames((0,_E,_k))
if mibBuilder.loadTexts:extremeSlotEntry.setStatus(_A)
_ExtremeSlotNumber_Type=Integer32
_ExtremeSlotNumber_Object=MibTableColumn
extremeSlotNumber=_ExtremeSlotNumber_Object((1,3,6,1,4,1,1916,1,1,2,2,1,1),_ExtremeSlotNumber_Type())
extremeSlotNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeSlotNumber.setStatus(_A)
_ExtremeSlotName_Type=DisplayString
_ExtremeSlotName_Object=MibTableColumn
extremeSlotName=_ExtremeSlotName_Object((1,3,6,1,4,1,1916,1,1,2,2,1,2),_ExtremeSlotName_Type())
extremeSlotName.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeSlotName.setStatus(_A)
_ExtremeSlotModuleConfiguredType_Type=SlotType
_ExtremeSlotModuleConfiguredType_Object=MibTableColumn
extremeSlotModuleConfiguredType=_ExtremeSlotModuleConfiguredType_Object((1,3,6,1,4,1,1916,1,1,2,2,1,3),_ExtremeSlotModuleConfiguredType_Type())
extremeSlotModuleConfiguredType.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeSlotModuleConfiguredType.setStatus(_A)
_ExtremeSlotModuleInsertedType_Type=SlotType
_ExtremeSlotModuleInsertedType_Object=MibTableColumn
extremeSlotModuleInsertedType=_ExtremeSlotModuleInsertedType_Object((1,3,6,1,4,1,1916,1,1,2,2,1,4),_ExtremeSlotModuleInsertedType_Type())
extremeSlotModuleInsertedType.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeSlotModuleInsertedType.setStatus(_A)
class _ExtremeSlotModuleState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,100)));namedValues=NamedValues(*((_O,1),('testing',2),('mismatch',3),('failed',4),('operational',5),('powerdown',6),(_J,7),('present',8),('poweron',9),('post',10),('downloading',11),('booting',12),('offline',13),('initializing',14),('invalid',100)))
_ExtremeSlotModuleState_Type.__name__=_C
_ExtremeSlotModuleState_Object=MibTableColumn
extremeSlotModuleState=_ExtremeSlotModuleState_Object((1,3,6,1,4,1,1916,1,1,2,2,1,5),_ExtremeSlotModuleState_Type())
extremeSlotModuleState.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeSlotModuleState.setStatus(_A)
_ExtremeSlotModuleSerialNumber_Type=DisplayString
_ExtremeSlotModuleSerialNumber_Object=MibTableColumn
extremeSlotModuleSerialNumber=_ExtremeSlotModuleSerialNumber_Object((1,3,6,1,4,1,1916,1,1,2,2,1,6),_ExtremeSlotModuleSerialNumber_Type())
extremeSlotModuleSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeSlotModuleSerialNumber.setStatus(_A)
_ExtremeChassisPortsPerSlot_Type=Integer32
_ExtremeChassisPortsPerSlot_Object=MibScalar
extremeChassisPortsPerSlot=_ExtremeChassisPortsPerSlot_Object((1,3,6,1,4,1,1916,1,1,2,3),_ExtremeChassisPortsPerSlot_Type())
extremeChassisPortsPerSlot.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeChassisPortsPerSlot.setStatus(_A)
_ExtremeSystemHealthCheck_ObjectIdentity=ObjectIdentity
extremeSystemHealthCheck=_ExtremeSystemHealthCheck_ObjectIdentity((1,3,6,1,4,1,1916,1,1,3))
class _ExtremeHealthCheckErrorType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_J,1),('cpuPacket',2),('backplane',3),('hardwareFail',4),('pbusChecksum',5)))
_ExtremeHealthCheckErrorType_Type.__name__=_C
_ExtremeHealthCheckErrorType_Object=MibScalar
extremeHealthCheckErrorType=_ExtremeHealthCheckErrorType_Object((1,3,6,1,4,1,1916,1,1,3,1),_ExtremeHealthCheckErrorType_Type())
extremeHealthCheckErrorType.setMaxAccess(_I)
if mibBuilder.loadTexts:extremeHealthCheckErrorType.setStatus(_A)
class _ExtremeHealthCheckAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('syslogOnly',1),('healthCheckTrap',2),('ioModuleDown',3),('systemDown',4),('autoRecovery',5)))
_ExtremeHealthCheckAction_Type.__name__=_C
_ExtremeHealthCheckAction_Object=MibScalar
extremeHealthCheckAction=_ExtremeHealthCheckAction_Object((1,3,6,1,4,1,1916,1,1,3,2),_ExtremeHealthCheckAction_Type())
extremeHealthCheckAction.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeHealthCheckAction.setStatus(_A)
_ExtremeHealthCheckMaxRetries_Type=Integer32
_ExtremeHealthCheckMaxRetries_Object=MibScalar
extremeHealthCheckMaxRetries=_ExtremeHealthCheckMaxRetries_Object((1,3,6,1,4,1,1916,1,1,3,3),_ExtremeHealthCheckMaxRetries_Type())
extremeHealthCheckMaxRetries.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeHealthCheckMaxRetries.setStatus(_A)
_ExtremeSystemThresholds_ObjectIdentity=ObjectIdentity
extremeSystemThresholds=_ExtremeSystemThresholds_ObjectIdentity((1,3,6,1,4,1,1916,1,1,4))
class _ExtremeCpuUtilRisingThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_ExtremeCpuUtilRisingThreshold_Type.__name__=_C
_ExtremeCpuUtilRisingThreshold_Object=MibScalar
extremeCpuUtilRisingThreshold=_ExtremeCpuUtilRisingThreshold_Object((1,3,6,1,4,1,1916,1,1,4,1),_ExtremeCpuUtilRisingThreshold_Type())
extremeCpuUtilRisingThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeCpuUtilRisingThreshold.setStatus(_G)
_ExtremeCpuTaskUtilPair_Type=DisplayString
_ExtremeCpuTaskUtilPair_Object=MibScalar
extremeCpuTaskUtilPair=_ExtremeCpuTaskUtilPair_Object((1,3,6,1,4,1,1916,1,1,4,2),_ExtremeCpuTaskUtilPair_Type())
extremeCpuTaskUtilPair.setMaxAccess(_I)
if mibBuilder.loadTexts:extremeCpuTaskUtilPair.setStatus(_G)
_ExtremeSystemNotifications_ObjectIdentity=ObjectIdentity
extremeSystemNotifications=_ExtremeSystemNotifications_ObjectIdentity((1,3,6,1,4,1,1916,1,1,6))
_ExtremeSystemTrapsPrefix_ObjectIdentity=ObjectIdentity
extremeSystemTrapsPrefix=_ExtremeSystemTrapsPrefix_ObjectIdentity((1,3,6,1,4,1,1916,1,1,6,0))
_ExtremeGenericTrapParams_ObjectIdentity=ObjectIdentity
extremeGenericTrapParams=_ExtremeGenericTrapParams_ObjectIdentity((1,3,6,1,4,1,1916,1,1,7))
class _Severity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('critical',1),('error',2),('warning',3),('notice',4),('info',5),('debug-summary',6),('debug-verbose',7),('debug-data',8)))
_Severity_Type.__name__=_C
_Severity_Object=MibScalar
severity=_Severity_Object((1,3,6,1,4,1,1916,1,1,7,1),_Severity_Type())
severity.setMaxAccess(_I)
if mibBuilder.loadTexts:severity.setStatus(_A)
class _EventName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_EventName_Type.__name__=_F
_EventName_Object=MibScalar
eventName=_EventName_Object((1,3,6,1,4,1,1916,1,1,7,2),_EventName_Type())
eventName.setMaxAccess(_I)
if mibBuilder.loadTexts:eventName.setStatus(_A)
class _Message_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_Message_Type.__name__=_F
_Message_Object=MibScalar
message=_Message_Object((1,3,6,1,4,1,1916,1,1,7,3),_Message_Type())
message.setMaxAccess(_I)
if mibBuilder.loadTexts:message.setStatus(_A)
downloadImageTrap=NotificationType((1,3,6,1,4,1,1916,1,1,1,45,2,1))
downloadImageTrap.setObjects(*((_E,_U),(_E,_l),(_E,_m),(_E,_n),(_E,_o)))
if mibBuilder.loadTexts:downloadImageTrap.setStatus(_A)
installImageTrap=NotificationType((1,3,6,1,4,1,1916,1,1,1,45,2,2))
installImageTrap.setObjects(*((_E,_V),(_E,_p),(_E,_q),(_E,_r),(_E,_s)))
if mibBuilder.loadTexts:installImageTrap.setStatus(_A)
extremeSystemPowerStatus=NotificationType((1,3,6,1,4,1,1916,1,1,6,0,1))
extremeSystemPowerStatus.setObjects(*((_P,_Q),(_E,_t)))
if mibBuilder.loadTexts:extremeSystemPowerStatus.setStatus(_A)
extremeGenericTrap=NotificationType((1,3,6,1,4,1,1916,1,1,6,0,2))
extremeGenericTrap.setObjects(*((_E,_u),(_E,_v),(_E,_w)))
if mibBuilder.loadTexts:extremeGenericTrap.setStatus(_A)
extremePsuPowerStatus=NotificationType((1,3,6,1,4,1,1916,1,1,6,0,3))
extremePsuPowerStatus.setObjects(*((_P,_Q),(_E,_T),(_E,_x)))
if mibBuilder.loadTexts:extremePsuPowerStatus.setStatus(_A)
extremeSystemPowerUsageNotification=NotificationType((1,3,6,1,4,1,1916,1,1,6,0,4))
extremeSystemPowerUsageNotification.setObjects(*((_P,_W),(_P,_Q),(_E,_y),(_E,_z)))
if mibBuilder.loadTexts:extremeSystemPowerUsageNotification.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'SlotType':SlotType,'PowerValue':PowerValue,'UnitMultiplier':UnitMultiplier,'extremeSystem':extremeSystem,'extremeSystemCommon':extremeSystemCommon,'extremeSaveConfiguration':extremeSaveConfiguration,'extremeSaveStatus':extremeSaveStatus,'extremeCurrentConfigInUse':extremeCurrentConfigInUse,'extremeConfigToUseOnReboot':extremeConfigToUseOnReboot,'extremeOverTemperatureAlarm':extremeOverTemperatureAlarm,'extremeCurrentTemperature':extremeCurrentTemperature,'extremeFanStatusTable':extremeFanStatusTable,'extremeFanStatusEntry':extremeFanStatusEntry,_Y:extremeFanNumber,'extremeFanOperational':extremeFanOperational,'extremeFanEntPhysicalIndex':extremeFanEntPhysicalIndex,'extremeFanSpeed':extremeFanSpeed,'extremePrimaryPowerOperational':extremePrimaryPowerOperational,'extremeRedundantPowerStatus':extremeRedundantPowerStatus,'extremeRedundantPowerAlarm':extremeRedundantPowerAlarm,'extremePrimarySoftwareRev':extremePrimarySoftwareRev,'extremeSecondarySoftwareRev':extremeSecondarySoftwareRev,'extremeImageToUseOnReboot':extremeImageToUseOnReboot,'extremeSystemID':extremeSystemID,'extremeSystemBoardID':extremeSystemBoardID,'extremeSystemLeftBoardID':extremeSystemLeftBoardID,'extremeSystemRightBoardID':extremeSystemRightBoardID,'extremeInputPowerVoltage':extremeInputPowerVoltage,'extremePowerStatus':extremePowerStatus,'extremePowerAlarm':extremePowerAlarm,'extremeRmonEnable':extremeRmonEnable,'extremeBootROMVersion':extremeBootROMVersion,'extremeDot1dTpFdbTableEnable':extremeDot1dTpFdbTableEnable,'extremePowerSupplyTable':extremePowerSupplyTable,'extremePowerSupplyEntry':extremePowerSupplyEntry,_T:extremePowerSupplyNumber,_x:extremePowerSupplyStatus,'extremePowerSupplyInputVoltage':extremePowerSupplyInputVoltage,'extremePowerSupplySerialNumber':extremePowerSupplySerialNumber,'extremePowerSupplyEntPhysicalIndex':extremePowerSupplyEntPhysicalIndex,'extremePowerSupplyFan1Speed':extremePowerSupplyFan1Speed,'extremePowerSupplyFan2Speed':extremePowerSupplyFan2Speed,'extremePowerSupplySource':extremePowerSupplySource,'extremePowerSupplyInputPowerUsage':extremePowerSupplyInputPowerUsage,'extremePowerMonSupplyNumOutput':extremePowerMonSupplyNumOutput,'extremePowerSupplyInputPowerUsageUnitMultiplier':extremePowerSupplyInputPowerUsageUnitMultiplier,'extremeCpuAggregateUtilization':extremeCpuAggregateUtilization,'extremeCpuTask2Table':extremeCpuTask2Table,'extremeCpuTask2Entry':extremeCpuTask2Entry,_a:extremeCpuTask2CpuId,_b:extremeCpuTask2Name,'extremeCpuTask2Id':extremeCpuTask2Id,'extremeCpuTask2Pc':extremeCpuTask2Pc,'extremeCpuTask2Status':extremeCpuTask2Status,'extremeCpuTask2Utilization':extremeCpuTask2Utilization,'extremeCpuTask2MaxUtilization':extremeCpuTask2MaxUtilization,'extremeAuthFailSrcAddr':extremeAuthFailSrcAddr,'extremeCpuTransmitPriority':extremeCpuTransmitPriority,'extremeImageBooted':extremeImageBooted,'extremeMsmFailoverCause':extremeMsmFailoverCause,'extremeImageTable':extremeImageTable,'extremeImageEntry':extremeImageEntry,_d:extremeImageNumber,'extremeMajorVersion':extremeMajorVersion,'extremeSubMajorVersion':extremeSubMajorVersion,'extremeMinorVersion':extremeMinorVersion,'extremeBuildNumber':extremeBuildNumber,'extremeTechnologyReleaseNumber':extremeTechnologyReleaseNumber,'extremeSustainingReleaseNumber':extremeSustainingReleaseNumber,'extremeBranchRevisionNumber':extremeBranchRevisionNumber,'extremeImageType':extremeImageType,'extremeImageDescription':extremeImageDescription,'extremeImageSecurity':extremeImageSecurity,'extremePatchVersion':extremePatchVersion,'extremeImageFeatureTable':extremeImageFeatureTable,'extremeImageFeatureEntry':extremeImageFeatureEntry,_e:extremeImageFeatureNumber,'extremeImageSshCapability':extremeImageSshCapability,'extremeImageUAACapability':extremeImageUAACapability,_t:extremeSystemPowerState,'extremeBootTime':extremeBootTime,'extremePowerSupplyOutputPowerTable':extremePowerSupplyOutputPowerTable,'extremePowerSupplyOutputPowerEntry':extremePowerSupplyOutputPowerEntry,_f:extremePowerSupplyIndex,_g:extremePowerSupplyOutputSensorIdx,'extremePowerSupplyOutputVoltage':extremePowerSupplyOutputVoltage,'extremePowerSupplyOutputCurrent':extremePowerSupplyOutputCurrent,'extremePowerSupplyOutputUnitMultiplier':extremePowerSupplyOutputUnitMultiplier,'extremePowerSupplyUsageTable':extremePowerSupplyUsageTable,'extremePowerSupplyUsageEntry':extremePowerSupplyUsageEntry,_h:extremeSlotIndex,'extremePowerSupplyUsageValue':extremePowerSupplyUsageValue,'extremePowerSupplyUnitMultiplier':extremePowerSupplyUnitMultiplier,'extremeSystemPowerUsage':extremeSystemPowerUsage,_y:extremeSystemPowerUsageValue,_z:extremeSystemPowerUsageUnitMultiplier,'extremeSystemPowerMonitorTable':extremeSystemPowerMonitorTable,'extremeSystemPowerMonitorEntry':extremeSystemPowerMonitorEntry,_i:extremeSystemPowerMonitorIndex1,'extremeSystemPowerMonitorPollInterval':extremeSystemPowerMonitorPollInterval,'extremeSystemPowerMonitorReportChanges':extremeSystemPowerMonitorReportChanges,'extremeSystemPowerMonitorChangeThreshold':extremeSystemPowerMonitorChangeThreshold,'extremeRebootTable':extremeRebootTable,'rebootTimeEntry':rebootTimeEntry,_j:extremeRebootSlotId,'extremeRebootNodeAddress':extremeRebootNodeAddress,'extremeRebootModuleSlotId':extremeRebootModuleSlotId,'extremeRebootSlotNumber':extremeRebootSlotNumber,'extremeRebootAsStandby':extremeRebootAsStandby,'extremeRebootStackTopology':extremeRebootStackTopology,'extremeRebootMonth':extremeRebootMonth,'extremeRebootDay':extremeRebootDay,'extremeRebootYear':extremeRebootYear,'extremeRebootHour':extremeRebootHour,'extremeRebootMinute':extremeRebootMinute,'extremeRebootSeconds':extremeRebootSeconds,'extremeRebootCancel':extremeRebootCancel,'extremeRebootImmediate':extremeRebootImmediate,'extremeRebootRowStatus':extremeRebootRowStatus,'extremeDownloadImageTable':extremeDownloadImageTable,'extremeDownloadImageEntry':extremeDownloadImageEntry,_U:extremeDownloadImageSlotId,_l:extremeDownloadImageStatus,_m:extremeDownloadImageFilename,_n:extremeDownloadImagePartition,'extremeDownloadImageHostName':extremeDownloadImageHostName,'extremeDownloadImageIpaddress':extremeDownloadImageIpaddress,_o:extremeDownloadImageStartTime,'extremeDownloadImageMemorycard':extremeDownloadImageMemorycard,'extremeDownloadImageInstall':extremeDownloadImageInstall,'extremeDownloadSlotNumber':extremeDownloadSlotNumber,'extremeDownloadModuleSlotId':extremeDownloadModuleSlotId,'extremeDownloadRowStatus':extremeDownloadRowStatus,'extremeDownloadBlockSize':extremeDownloadBlockSize,'extremeInstallImageTable':extremeInstallImageTable,'extremeInstallImageEntry':extremeInstallImageEntry,_V:extremeInstallImageSlotId,_p:extremeInstallImageStatus,_q:extremeInstallImageFilename,_r:extremeInstallImagePartition,_s:extremeInstallImageStartTime,'extremeInstallImageReboot':extremeInstallImageReboot,'extremeInstallImageModuleSlotId':extremeInstallImageModuleSlotId,'extremeInstallImageSlotNumber':extremeInstallImageSlotNumber,'extremeInstallImageRowStatus':extremeInstallImageRowStatus,'extremeLoadInstallTrap':extremeLoadInstallTrap,'loadInstallControl':loadInstallControl,'downloadImageTrapEnable':downloadImageTrapEnable,'installImageTrapEnable':installImageTrapEnable,'loadInstallTraps':loadInstallTraps,'downloadImageTrap':downloadImageTrap,'installImageTrap':installImageTrap,'extremeSaveConfigurationFileName':extremeSaveConfigurationFileName,'extremeUseOnRebootFileName':extremeUseOnRebootFileName,'extremeAuthFailSrcAddressType':extremeAuthFailSrcAddressType,'extremeAuthFailSrcAddress':extremeAuthFailSrcAddress,'extremeAuthFailSrcAddressVrName':extremeAuthFailSrcAddressVrName,'extremeAutoSave':extremeAutoSave,'extremeAutoSaveConfigurationFileName':extremeAutoSaveConfigurationFileName,'extremeAutoSaveConfigurationEnabled':extremeAutoSaveConfigurationEnabled,'extremeAutoSaveConfigurationTimeInterval':extremeAutoSaveConfigurationTimeInterval,'extremeChassisGroup':extremeChassisGroup,'extremeMasterMSMSlot':extremeMasterMSMSlot,'extremeSlotTable':extremeSlotTable,'extremeSlotEntry':extremeSlotEntry,_k:extremeSlotNumber,'extremeSlotName':extremeSlotName,'extremeSlotModuleConfiguredType':extremeSlotModuleConfiguredType,'extremeSlotModuleInsertedType':extremeSlotModuleInsertedType,'extremeSlotModuleState':extremeSlotModuleState,'extremeSlotModuleSerialNumber':extremeSlotModuleSerialNumber,'extremeChassisPortsPerSlot':extremeChassisPortsPerSlot,'extremeSystemHealthCheck':extremeSystemHealthCheck,'extremeHealthCheckErrorType':extremeHealthCheckErrorType,'extremeHealthCheckAction':extremeHealthCheckAction,'extremeHealthCheckMaxRetries':extremeHealthCheckMaxRetries,'extremeSystemThresholds':extremeSystemThresholds,'extremeCpuUtilRisingThreshold':extremeCpuUtilRisingThreshold,'extremeCpuTaskUtilPair':extremeCpuTaskUtilPair,'extremeSystemNotifications':extremeSystemNotifications,'extremeSystemTrapsPrefix':extremeSystemTrapsPrefix,'extremeSystemPowerStatus':extremeSystemPowerStatus,'extremeGenericTrap':extremeGenericTrap,'extremePsuPowerStatus':extremePsuPowerStatus,'extremeSystemPowerUsageNotification':extremeSystemPowerUsageNotification,'extremeGenericTrapParams':extremeGenericTrapParams,_u:severity,_v:eventName,_w:message})