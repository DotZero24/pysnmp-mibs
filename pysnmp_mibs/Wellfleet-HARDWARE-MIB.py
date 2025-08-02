_S='wfHwCfgSlot'
_R='read-write'
_Q='present'
_P='nofilesys'
_O='filesys'
_N='sysctrl'
_M='wfHwSlot'
_L='caution'
_K='Wellfleet-HARDWARE-MIB'
_J='asn'
_I='lite'
_H='arn'
_G='notapplicable'
_F='fail'
_E='ok'
_D='notpresent'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
wfHardwareConfig,=mibBuilder.importSymbols('Wellfleet-COMMON-MIB','wfHardwareConfig')
_WfHwBase_ObjectIdentity=ObjectIdentity
wfHwBase=_WfHwBase_ObjectIdentity((1,3,6,1,4,1,18,3,1,1))
class _WfHwBpIdOpt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,16,32,34,36,5000,16640,16896,17152,20480,20736,20992,24576,26368)));namedValues=NamedValues(*(('acefn',1),('aceln',2),('acecn',3),('afn',4),('in',5),('an',16),(_H,32),('fbr4slot',34),(_I,36),('sys5000',5000),('freln',16640),('frecn',16896),('frerbln',17152),(_J,20480),('asnzcable',20736),('asnbcable',20992),('sn',24576),('v15k',26368)))
_WfHwBpIdOpt_Type.__name__=_C
_WfHwBpIdOpt_Object=MibScalar
wfHwBpIdOpt=_WfHwBpIdOpt_Object((1,3,6,1,4,1,18,3,1,1,1),_WfHwBpIdOpt_Type())
wfHwBpIdOpt.setMaxAccess(_B)
if mibBuilder.loadTexts:wfHwBpIdOpt.setStatus(_A)
_WfHwBpRev_Type=OctetString
_WfHwBpRev_Object=MibScalar
wfHwBpRev=_WfHwBpRev_Object((1,3,6,1,4,1,18,3,1,1,2),_WfHwBpRev_Type())
wfHwBpRev.setMaxAccess(_B)
if mibBuilder.loadTexts:wfHwBpRev.setStatus(_A)
_WfHwBpSerialNumber_Type=OctetString
_WfHwBpSerialNumber_Object=MibScalar
wfHwBpSerialNumber=_WfHwBpSerialNumber_Object((1,3,6,1,4,1,18,3,1,1,3),_WfHwBpSerialNumber_Type())
wfHwBpSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:wfHwBpSerialNumber.setStatus(_A)
class _WfBCNPwrSupply1_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_D,3)))
_WfBCNPwrSupply1_Type.__name__=_C
_WfBCNPwrSupply1_Object=MibScalar
wfBCNPwrSupply1=_WfBCNPwrSupply1_Object((1,3,6,1,4,1,18,3,1,1,4),_WfBCNPwrSupply1_Type())
wfBCNPwrSupply1.setMaxAccess(_B)
if mibBuilder.loadTexts:wfBCNPwrSupply1.setStatus(_A)
class _WfBCNPwrSupply2_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_D,3)))
_WfBCNPwrSupply2_Type.__name__=_C
_WfBCNPwrSupply2_Object=MibScalar
wfBCNPwrSupply2=_WfBCNPwrSupply2_Object((1,3,6,1,4,1,18,3,1,1,5),_WfBCNPwrSupply2_Type())
wfBCNPwrSupply2.setMaxAccess(_B)
if mibBuilder.loadTexts:wfBCNPwrSupply2.setStatus(_A)
class _WfBCNPwrSupply3_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_D,3)))
_WfBCNPwrSupply3_Type.__name__=_C
_WfBCNPwrSupply3_Object=MibScalar
wfBCNPwrSupply3=_WfBCNPwrSupply3_Object((1,3,6,1,4,1,18,3,1,1,6),_WfBCNPwrSupply3_Type())
wfBCNPwrSupply3.setMaxAccess(_B)
if mibBuilder.loadTexts:wfBCNPwrSupply3.setStatus(_A)
class _WfBCNPwrSupply4_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_D,3)))
_WfBCNPwrSupply4_Type.__name__=_C
_WfBCNPwrSupply4_Object=MibScalar
wfBCNPwrSupply4=_WfBCNPwrSupply4_Object((1,3,6,1,4,1,18,3,1,1,7),_WfBCNPwrSupply4_Type())
wfBCNPwrSupply4.setMaxAccess(_B)
if mibBuilder.loadTexts:wfBCNPwrSupply4.setStatus(_A)
class _WfBCNFanStatus_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_D,3)))
_WfBCNFanStatus_Type.__name__=_C
_WfBCNFanStatus_Object=MibScalar
wfBCNFanStatus=_WfBCNFanStatus_Object((1,3,6,1,4,1,18,3,1,1,8),_WfBCNFanStatus_Type())
wfBCNFanStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:wfBCNFanStatus.setStatus(_A)
class _WfBCNTemperature_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_L,2),(_D,3),(_F,4)))
_WfBCNTemperature_Type.__name__=_C
_WfBCNTemperature_Object=MibScalar
wfBCNTemperature=_WfBCNTemperature_Object((1,3,6,1,4,1,18,3,1,1,9),_WfBCNTemperature_Type())
wfBCNTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:wfBCNTemperature.setStatus(_A)
class _WfBCNTemperature2_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_L,2),(_D,3),(_F,4)))
_WfBCNTemperature2_Type.__name__=_C
_WfBCNTemperature2_Object=MibScalar
wfBCNTemperature2=_WfBCNTemperature2_Object((1,3,6,1,4,1,18,3,1,1,10),_WfBCNTemperature2_Type())
wfBCNTemperature2.setMaxAccess(_B)
if mibBuilder.loadTexts:wfBCNTemperature2.setStatus(_A)
class _WfFanSpeed_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('low',1),('high',2),(_D,3)))
_WfFanSpeed_Type.__name__=_C
_WfFanSpeed_Object=MibScalar
wfFanSpeed=_WfFanSpeed_Object((1,3,6,1,4,1,18,3,1,1,11),_WfFanSpeed_Type())
wfFanSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:wfFanSpeed.setStatus(_A)
_WfHwTable_Object=MibTable
wfHwTable=_WfHwTable_Object((1,3,6,1,4,1,18,3,1,2))
if mibBuilder.loadTexts:wfHwTable.setStatus(_A)
_WfHwEntry_Object=MibTableRow
wfHwEntry=_WfHwEntry_Object((1,3,6,1,4,1,18,3,1,2,1))
wfHwEntry.setIndexNames((0,_K,_M))
if mibBuilder.loadTexts:wfHwEntry.setStatus(_A)
_WfHwSlot_Type=Integer32
_WfHwSlot_Object=MibTableColumn
wfHwSlot=_WfHwSlot_Object((1,3,6,1,4,1,18,3,1,2,1,1),_WfHwSlot_Type())
wfHwSlot.setMaxAccess(_B)
if mibBuilder.loadTexts:wfHwSlot.setStatus(_A)
class _WfHwModIdOpt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,8,16,17,24,32,33,40,41,42,43,44,45,46,47,48,49,56,57,58,60,61,62,63,64,65,66,67,68,69,80,81,88,89,104,112,113,114,116,117,118,119,120,132,156,160,161,162,164,165,168,169,176,184,185,188,189,190,191,192,193,194,195,196,197,198,199,200,201,202,203,204,208,216,217,224,225,232,233,234,235,236,237,238,239,256,508,509,510,511,512,513,767,777,778,787,1024,1025,1026,1027,1028,1029,1030,1031,1032,1033,1034,1035,1036,1037,1038,1039,1040,1041,1042,1043,1044,1045,1046,1047,1048,1049,1050,1051,1052,1053,1054,1055,1056,1057,1058,1059,1060,1061,1062,1063,1064,1066,1067,1068,1069,1070,1071,1072,1073,1074,1075,1076,1077,1078,1079,1080,1081,1082,1083,1084,1085,1086,1087,1088,1089,1090,1091,1092,1093,1094,1095,1096,1097,1098,1099,1100,1101,1102,1103,1104,1105,1106,1107,1108,1109,1110,1111,1112,1113,1114,1115,1116,1117,1118,1119,1120,1121,1122,1123,1124,1125,1126,1127,1128,1129,1130,1131,1132,1133,1134,1135,1136,1137,4096,4097,4098,4099,4352,4353,4354,4608,4609,4610,4864,5120,5121,5376,5377,5378,6144,6145,6400,6401,8448,8500,24848,24849,24864,24880,24896,24912,524288,524544,1048746,1048747,1048762,1048763,1048798,1048799,1048806,1048807,1048810,1048811,1048814,1048815,1048822,1048823,1048826,1048827,1048830,1048831,1048832,1048833,1048834,1048835,1048836,1048837,1048863,1048864,1048865,1048866,1048867,1048868,1048869,1048895,1048896,1048897,1048898,1048899,1048900,1048901,1048927,1048928,1048929,1048930,1048931,1048932,1048933,1048959,1048960,1048961,1048962,1048963,1048964,1048965,1048991,1049089,1049090,1049091,1049092,1049093,1049094,1049095,1049119,1049217,1049218,1049219,1049220,1049221,1049222,1049223,1049247,1049344,1049376)));namedValues=NamedValues(*(('enet1',1),('enet2',8),('sync1',16),('sync1a',17),('t11',24),('dse1',32),('dse1a',33),('dst416',40),('sst416a',41),('dst4',42),('sst4a',43),('sst416',44),('stok416',45),('sst4',46),('stok4',47),('floppy',48),('necfloppy',49),('t12',56),('t12a',57),('st1',58),('t156k',60),('e1',61),('st156k',62),('se1',63),('t12n',64),('st1n',65),('t156kn',66),('st156kn',67),('e1n',68),('se1n',69),('sync',80),('sync2a',81),('cmcfddi',88),('iphfddi',89),('dt',104),('dsde1',112),('dsde1a',113),('enet',114),('dse2',116),('dse2a',117),('sse',118),('ssea',119),('dsde10bt',120),('enet3',132),('dsde2',156),('oldqenf',160),('denf',161),('qenf',162),('qef',164),('def',165),('mct1',168),('smct1',169),('dtok',176),('mce1',184),('smce1',185),('mce1ii75',188),('smce1ii75',189),('mce1ii120',190),('smce1ii120',191),('wffddi2m',192),('wffddi1m',193),('wffddi2s',194),('wffddi1s',195),('wffddi2mf',196),('wffddi1mf',197),('wffddi2sf',198),('wffddi1sf',199),('fmdset',200),('fmdst',201),('fmdse',202),('fmsst',203),('fmsse',204),('fnsdse',208),('fnsdsdt',216),('fnsdst',217),('dhssi',224),('shssi',225),('esafnf',232),('esafdsenf',233),('esafssenf',234),('esafdenf',235),('esaf',236),('esafdse',237),('esafsse',238),('esafde',239),('qtok',256),('m5380',508),('m5580',509),('m5780',510),(_J,511),('m5782',512),('sn',513),(_H,767),('fbrcpu',777),('fbr2pmccarrier',778),(_I,787),('anseds',1024),('ansedst',1025),('ansedsh',1026),('ansedsi',1027),('ansedsti',1028),('ansedshi',1029),('ansets',1030),('ansetst',1031),('ansetsh',1032),('andeds',1033),('andedst',1034),('andedsh',1035),('andstx',1036),('andst',1037),('andsti',1038),('antst',1039),('antstx',1040),('ansdsedst',1041),('ansdsedstx',1042),('ansedsi2',1043),('ansedsti2',1044),('ansedshi2',1045),('andsti2',1046),('ansedsg',1047),('ansedsgx',1048),('ansetsg',1049),('andedsg',1050),('ansedsgi',1051),('ansetsgx',1052),('andedsgx',1053),('ansedsgix',1054),('ansedsx',1055),('ansetsx',1056),('andedsx',1057),('ansedstx',1058),('ansetstx',1059),('andedstx',1060),('andsti2x',1061),('ansedsi2x',1062),('ansedsti2x',1063),('ansedi',1064),('ansedsu',1066),('ansedsu2',1067),('andstu',1068),('andstu2',1069),('ansedstu',1070),('ansedstu2',1071),('ansedshu',1072),('ansedshu2',1073),('ansedsgu',1074),('ansedsu2x',1075),('andstu2x',1076),('ansedstu2x',1077),('ansedshu2x',1078),('ansedsgu2x',1079),('ansedsv',1080),('andstv',1081),('ansedstv',1082),('ansedshv',1083),('ansedsgv',1084),('ansedsvx',1085),('andstvx',1086),('ansedstvx',1087),('ansedshvx',1088),('ansedsgvx',1089),('ansedsc',1090),('andstc',1091),('ansedstc',1092),('ansedshc',1093),('ansedsgc',1094),('ansedscx',1095),('andstcx',1096),('ansedstcx',1097),('ansedshcx',1098),('ansedsgcx',1099),('ansedsf',1100),('ansedsf2',1101),('andstf',1102),('andstf2',1103),('ansedstf',1104),('ansedstf2',1105),('ansedshf',1106),('ansedshf2',1107),('ansedsgf',1108),('ansedsf2x',1109),('andstf2x',1110),('ansedstf2x',1111),('ansedshf2x',1112),('ansedsgf2x',1113),('ansedsfx',1114),('andstfx',1115),('ansedstfx',1116),('ansedshfx',1117),('ansedsgfx',1118),('ansedsj',1119),('ansedsj2',1120),('andstj',1121),('andstj2',1122),('ansedstj',1123),('ansedstj2',1124),('ansedshj',1125),('ansedshj2',1126),('ansedsgj',1127),('ansedsj2x',1128),('andstj2x',1129),('ansedstj2x',1130),('ansedshj2x',1131),('ansedsgj2x',1132),('ansedsjx',1133),('andstjx',1134),('ansedstjx',1135),('ansedshjx',1136),('ansedsgjx',1137),('atmalc',4096),('atmalctaxi100',4097),('atmalcsonetmm',4098),('atmalcsonetsm',4099),('osync',4352),('comp',4353),('comp128',4354),('atmcoc3mm',4608),('atmcoc3sm',4609),('atmcoc3utp5',4610),('de100',4864),('atmcds3',5120),('atmce3',5121),('qmct1rj48',5376),('qmct1db15',5377),('qmct1ds0a',5378),('sqe100',6144),('sqe100fx',6145),('gigenet',6400),('gigenetlx',6401),('srml',8448),('fvoip',8500),('hds3',24848),('arm',24849),('dmcoc3',24864),('atmoc12',24880),('sspcons',24896),('sspenet',24912),('atm5000ah',524288),('atm5000bh',524544),('qecddi1utphwf',1048746),('qecddi1utp',1048747),('qecddi2utphwf',1048762),('qecddi2utp',1048763),('qehwf',1048798),('qe',1048799),('qefddi1shwf',1048806),('qefddi1s',1048807),('qecddi1stphwf',1048810),('qecddi1stp',1048811),('qefddi1mhwf',1048814),('qefddi1m',1048815),('qefddi2shwf',1048822),('qefddi2s',1048823),('qecddi2stphwf',1048826),('qecddi2stp',1048827),('qefddi2mhwf',1048830),('qefddi2m',1048831),('enet3atm',1048832),('enet3enet',1048833),('enet3fddi',1048834),('enet3tok',1048835),('enet3tokf',1048836),('enet3sync',1048837),('enet3only',1048863),('fddiatm',1048864),('fddienet',1048865),('fddifddi',1048866),('fdditok',1048867),('fdditokf',1048868),('fddisync',1048869),('fddionly',1048895),('tok3atm',1048896),('tok3enet',1048897),('tok3fddi',1048898),('tok3tok',1048899),('tok3tokf',1048900),('tok3sync',1048901),('tok3only',1048927),('tokf3atm',1048928),('tokf3enet',1048929),('tokf3fddi',1048930),('tokf3tok',1048931),('tokf3tokf',1048932),('tokf3sync',1048933),('tokf3only',1048959),('enet3datm',1048960),('enet3denet',1048961),('enet3dfddi',1048962),('enet3dtok',1048963),('enet3dtokf',1048964),('enet3dsync',1048965),('enet3donly',1048991),('chipcomfenet',1049089),('chipcomffddi',1049090),('chipcomftok',1049091),('chipcomftokf',1049092),('chipcomfdsync',1049093),('chipcomfisdn',1049094),('chipcomffddis',1049095),('chipcomfonly',1049119),('chipcomenet',1049217),('chipcomfddi',1049218),('chipcomtok',1049219),('chipcomtokf',1049220),('chipcomdsync',1049221),('chipcomisdn',1049222),('chipcomfddis',1049223),('chipcomonly',1049247),('fntsenet',1049344),('fntstok',1049376)))
_WfHwModIdOpt_Type.__name__=_C
_WfHwModIdOpt_Object=MibTableColumn
wfHwModIdOpt=_WfHwModIdOpt_Object((1,3,6,1,4,1,18,3,1,2,1,2),_WfHwModIdOpt_Type())
wfHwModIdOpt.setMaxAccess(_B)
if mibBuilder.loadTexts:wfHwModIdOpt.setStatus(_A)
_WfHwModRev_Type=OctetString
_WfHwModRev_Object=MibTableColumn
wfHwModRev=_WfHwModRev_Object((1,3,6,1,4,1,18,3,1,2,1,3),_WfHwModRev_Type())
wfHwModRev.setMaxAccess(_B)
if mibBuilder.loadTexts:wfHwModRev.setStatus(_A)
_WfHwModSerialNumber_Type=OctetString
_WfHwModSerialNumber_Object=MibTableColumn
wfHwModSerialNumber=_WfHwModSerialNumber_Object((1,3,6,1,4,1,18,3,1,2,1,4),_WfHwModSerialNumber_Type())
wfHwModSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:wfHwModSerialNumber.setStatus(_A)
class _WfHwMotherBdIdOpt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,16,32,36,64,256,768,769,1024,1025,1280,1536,1792,2561,5632,5633,6656,8704,25088,25344,25600,25856)));namedValues=NamedValues(*((_N,1),('ace12',2),('ace25',3),('ace32',4),('afn',5),('in',6),('sysctrl2',7),('an',16),(_H,32),(_I,36),('fbr',64),('fre',256),('fre2',768),('o60',769),(_J,1024),('asn2',1025),('are',1280),('are5000',1536),('asn5000',1792),('sn060',2561),('fre2060epci',5632),('fre2060e',5633),('fre4',6656),('srmf',8704),('ssp',25088),('ifp',25344),('atp',25600),('cap',25856)))
_WfHwMotherBdIdOpt_Type.__name__=_C
_WfHwMotherBdIdOpt_Object=MibTableColumn
wfHwMotherBdIdOpt=_WfHwMotherBdIdOpt_Object((1,3,6,1,4,1,18,3,1,2,1,5),_WfHwMotherBdIdOpt_Type())
wfHwMotherBdIdOpt.setMaxAccess(_B)
if mibBuilder.loadTexts:wfHwMotherBdIdOpt.setStatus(_A)
_WfHwMotherBdRev_Type=OctetString
_WfHwMotherBdRev_Object=MibTableColumn
wfHwMotherBdRev=_WfHwMotherBdRev_Object((1,3,6,1,4,1,18,3,1,2,1,6),_WfHwMotherBdRev_Type())
wfHwMotherBdRev.setMaxAccess(_B)
if mibBuilder.loadTexts:wfHwMotherBdRev.setStatus(_A)
_WfHwMotherBdSerialNumber_Type=OctetString
_WfHwMotherBdSerialNumber_Object=MibTableColumn
wfHwMotherBdSerialNumber=_WfHwMotherBdSerialNumber_Object((1,3,6,1,4,1,18,3,1,2,1,7),_WfHwMotherBdSerialNumber_Type())
wfHwMotherBdSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:wfHwMotherBdSerialNumber.setStatus(_A)
class _WfHwDaughterBdIdOpt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,4352,4608,5888,5889,5890,5891,8752,25345,25857)));namedValues=NamedValues(*((_N,1),('ace68020mhz12',2),('ace68020mhz25',3),('ace68030mhz32',4),('fre68040mhz25',4352),('fre68040mhz33',4608),('hwcomp128pci',5888),('hwcomp128',5889),('hwcomp256pci',5890),('hwcomp256',5891),('arnv34',8752),('ifprspdtr',25345),('cap3m13dtr',25857)))
_WfHwDaughterBdIdOpt_Type.__name__=_C
_WfHwDaughterBdIdOpt_Object=MibTableColumn
wfHwDaughterBdIdOpt=_WfHwDaughterBdIdOpt_Object((1,3,6,1,4,1,18,3,1,2,1,8),_WfHwDaughterBdIdOpt_Type())
wfHwDaughterBdIdOpt.setMaxAccess(_B)
if mibBuilder.loadTexts:wfHwDaughterBdIdOpt.setStatus(_A)
_WfHwDaughterBdRev_Type=OctetString
_WfHwDaughterBdRev_Object=MibTableColumn
wfHwDaughterBdRev=_WfHwDaughterBdRev_Object((1,3,6,1,4,1,18,3,1,2,1,9),_WfHwDaughterBdRev_Type())
wfHwDaughterBdRev.setMaxAccess(_B)
if mibBuilder.loadTexts:wfHwDaughterBdRev.setStatus(_A)
_WfHwDaughterBdSerialNumber_Type=OctetString
_WfHwDaughterBdSerialNumber_Object=MibTableColumn
wfHwDaughterBdSerialNumber=_WfHwDaughterBdSerialNumber_Object((1,3,6,1,4,1,18,3,1,2,1,10),_WfHwDaughterBdSerialNumber_Type())
wfHwDaughterBdSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:wfHwDaughterBdSerialNumber.setStatus(_A)
_WfHwBabyBdIdOpt_Type=Integer32
_WfHwBabyBdIdOpt_Object=MibTableColumn
wfHwBabyBdIdOpt=_WfHwBabyBdIdOpt_Object((1,3,6,1,4,1,18,3,1,2,1,11),_WfHwBabyBdIdOpt_Type())
wfHwBabyBdIdOpt.setMaxAccess(_B)
if mibBuilder.loadTexts:wfHwBabyBdIdOpt.setStatus(_A)
_WfHwBabyBdRev_Type=OctetString
_WfHwBabyBdRev_Object=MibTableColumn
wfHwBabyBdRev=_WfHwBabyBdRev_Object((1,3,6,1,4,1,18,3,1,2,1,12),_WfHwBabyBdRev_Type())
wfHwBabyBdRev.setMaxAccess(_B)
if mibBuilder.loadTexts:wfHwBabyBdRev.setStatus(_A)
_WfHwBabyBdSerialNumber_Type=OctetString
_WfHwBabyBdSerialNumber_Object=MibTableColumn
wfHwBabyBdSerialNumber=_WfHwBabyBdSerialNumber_Object((1,3,6,1,4,1,18,3,1,2,1,13),_WfHwBabyBdSerialNumber_Type())
wfHwBabyBdSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:wfHwBabyBdSerialNumber.setStatus(_A)
_WfHwDiagPromRev_Type=OctetString
_WfHwDiagPromRev_Object=MibTableColumn
wfHwDiagPromRev=_WfHwDiagPromRev_Object((1,3,6,1,4,1,18,3,1,2,1,14),_WfHwDiagPromRev_Type())
wfHwDiagPromRev.setMaxAccess(_B)
if mibBuilder.loadTexts:wfHwDiagPromRev.setStatus(_A)
_WfHwDiagPromDate_Type=DisplayString
_WfHwDiagPromDate_Object=MibTableColumn
wfHwDiagPromDate=_WfHwDiagPromDate_Object((1,3,6,1,4,1,18,3,1,2,1,15),_WfHwDiagPromDate_Type())
wfHwDiagPromDate.setMaxAccess(_B)
if mibBuilder.loadTexts:wfHwDiagPromDate.setStatus(_A)
_WfHwDiagPromSource_Type=DisplayString
_WfHwDiagPromSource_Object=MibTableColumn
wfHwDiagPromSource=_WfHwDiagPromSource_Object((1,3,6,1,4,1,18,3,1,2,1,16),_WfHwDiagPromSource_Type())
wfHwDiagPromSource.setMaxAccess(_B)
if mibBuilder.loadTexts:wfHwDiagPromSource.setStatus(_A)
_WfHwBootPromRev_Type=OctetString
_WfHwBootPromRev_Object=MibTableColumn
wfHwBootPromRev=_WfHwBootPromRev_Object((1,3,6,1,4,1,18,3,1,2,1,17),_WfHwBootPromRev_Type())
wfHwBootPromRev.setMaxAccess(_B)
if mibBuilder.loadTexts:wfHwBootPromRev.setStatus(_A)
_WfHwBootPromDate_Type=DisplayString
_WfHwBootPromDate_Object=MibTableColumn
wfHwBootPromDate=_WfHwBootPromDate_Object((1,3,6,1,4,1,18,3,1,2,1,18),_WfHwBootPromDate_Type())
wfHwBootPromDate.setMaxAccess(_B)
if mibBuilder.loadTexts:wfHwBootPromDate.setStatus(_A)
_WfHwBootPromSource_Type=DisplayString
_WfHwBootPromSource_Object=MibTableColumn
wfHwBootPromSource=_WfHwBootPromSource_Object((1,3,6,1,4,1,18,3,1,2,1,19),_WfHwBootPromSource_Type())
wfHwBootPromSource.setMaxAccess(_B)
if mibBuilder.loadTexts:wfHwBootPromSource.setStatus(_A)
_WfHwSparePromRev_Type=OctetString
_WfHwSparePromRev_Object=MibTableColumn
wfHwSparePromRev=_WfHwSparePromRev_Object((1,3,6,1,4,1,18,3,1,2,1,20),_WfHwSparePromRev_Type())
wfHwSparePromRev.setMaxAccess(_B)
if mibBuilder.loadTexts:wfHwSparePromRev.setStatus(_A)
_WfHwSparePromDate_Type=DisplayString
_WfHwSparePromDate_Object=MibTableColumn
wfHwSparePromDate=_WfHwSparePromDate_Object((1,3,6,1,4,1,18,3,1,2,1,21),_WfHwSparePromDate_Type())
wfHwSparePromDate.setMaxAccess(_B)
if mibBuilder.loadTexts:wfHwSparePromDate.setStatus(_A)
_WfHwSparePromSource_Type=DisplayString
_WfHwSparePromSource_Object=MibTableColumn
wfHwSparePromSource=_WfHwSparePromSource_Object((1,3,6,1,4,1,18,3,1,2,1,22),_WfHwSparePromSource_Type())
wfHwSparePromSource.setMaxAccess(_B)
if mibBuilder.loadTexts:wfHwSparePromSource.setStatus(_A)
class _WfHwFileSysPresent_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_O,1),(_P,2)))
_WfHwFileSysPresent_Type.__name__=_C
_WfHwFileSysPresent_Object=MibTableColumn
wfHwFileSysPresent=_WfHwFileSysPresent_Object((1,3,6,1,4,1,18,3,1,2,1,23),_WfHwFileSysPresent_Type())
wfHwFileSysPresent.setMaxAccess(_B)
if mibBuilder.loadTexts:wfHwFileSysPresent.setStatus(_A)
class _WfHwFileSysPresent2_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_O,1),(_P,2)))
_WfHwFileSysPresent2_Type.__name__=_C
_WfHwFileSysPresent2_Object=MibTableColumn
wfHwFileSysPresent2=_WfHwFileSysPresent2_Object((1,3,6,1,4,1,18,3,1,2,1,24),_WfHwFileSysPresent2_Type())
wfHwFileSysPresent2.setMaxAccess(_B)
if mibBuilder.loadTexts:wfHwFileSysPresent2.setStatus(_A)
_WfHwConfigServer_Type=Integer32
_WfHwConfigServer_Object=MibTableColumn
wfHwConfigServer=_WfHwConfigServer_Object((1,3,6,1,4,1,18,3,1,2,1,25),_WfHwConfigServer_Type())
wfHwConfigServer.setMaxAccess(_B)
if mibBuilder.loadTexts:wfHwConfigServer.setStatus(_A)
_WfHwConfigFile_Type=DisplayString
_WfHwConfigFile_Object=MibTableColumn
wfHwConfigFile=_WfHwConfigFile_Object((1,3,6,1,4,1,18,3,1,2,1,26),_WfHwConfigFile_Type())
wfHwConfigFile.setMaxAccess(_B)
if mibBuilder.loadTexts:wfHwConfigFile.setStatus(_A)
_WfHwConfigDateAndTime_Type=OctetString
_WfHwConfigDateAndTime_Object=MibTableColumn
wfHwConfigDateAndTime=_WfHwConfigDateAndTime_Object((1,3,6,1,4,1,18,3,1,2,1,27),_WfHwConfigDateAndTime_Type())
wfHwConfigDateAndTime.setMaxAccess(_B)
if mibBuilder.loadTexts:wfHwConfigDateAndTime.setStatus(_A)
_WfHwActiveImageName_Type=DisplayString
_WfHwActiveImageName_Object=MibTableColumn
wfHwActiveImageName=_WfHwActiveImageName_Object((1,3,6,1,4,1,18,3,1,2,1,28),_WfHwActiveImageName_Type())
wfHwActiveImageName.setMaxAccess(_B)
if mibBuilder.loadTexts:wfHwActiveImageName.setStatus(_A)
_WfHwActiveImageSource_Type=DisplayString
_WfHwActiveImageSource_Object=MibTableColumn
wfHwActiveImageSource=_WfHwActiveImageSource_Object((1,3,6,1,4,1,18,3,1,2,1,29),_WfHwActiveImageSource_Type())
wfHwActiveImageSource.setMaxAccess(_B)
if mibBuilder.loadTexts:wfHwActiveImageSource.setStatus(_A)
_WfHwActiveImageDate_Type=DisplayString
_WfHwActiveImageDate_Object=MibTableColumn
wfHwActiveImageDate=_WfHwActiveImageDate_Object((1,3,6,1,4,1,18,3,1,2,1,30),_WfHwActiveImageDate_Type())
wfHwActiveImageDate.setMaxAccess(_B)
if mibBuilder.loadTexts:wfHwActiveImageDate.setStatus(_A)
_WfHwMotherBdMemorySize_Type=Integer32
_WfHwMotherBdMemorySize_Object=MibTableColumn
wfHwMotherBdMemorySize=_WfHwMotherBdMemorySize_Object((1,3,6,1,4,1,18,3,1,2,1,31),_WfHwMotherBdMemorySize_Type())
wfHwMotherBdMemorySize.setMaxAccess(_B)
if mibBuilder.loadTexts:wfHwMotherBdMemorySize.setStatus(_A)
_WfHwFastPacketCacheSize_Type=Integer32
_WfHwFastPacketCacheSize_Object=MibTableColumn
wfHwFastPacketCacheSize=_WfHwFastPacketCacheSize_Object((1,3,6,1,4,1,18,3,1,2,1,32),_WfHwFastPacketCacheSize_Type())
wfHwFastPacketCacheSize.setMaxAccess(_B)
if mibBuilder.loadTexts:wfHwFastPacketCacheSize.setStatus(_A)
_WfHwModDaughterBd1IdOpt_Type=Integer32
_WfHwModDaughterBd1IdOpt_Object=MibTableColumn
wfHwModDaughterBd1IdOpt=_WfHwModDaughterBd1IdOpt_Object((1,3,6,1,4,1,18,3,1,2,1,33),_WfHwModDaughterBd1IdOpt_Type())
wfHwModDaughterBd1IdOpt.setMaxAccess(_B)
if mibBuilder.loadTexts:wfHwModDaughterBd1IdOpt.setStatus(_A)
_WfHwModDaughterBd1AwRev_Type=OctetString
_WfHwModDaughterBd1AwRev_Object=MibTableColumn
wfHwModDaughterBd1AwRev=_WfHwModDaughterBd1AwRev_Object((1,3,6,1,4,1,18,3,1,2,1,34),_WfHwModDaughterBd1AwRev_Type())
wfHwModDaughterBd1AwRev.setMaxAccess(_B)
if mibBuilder.loadTexts:wfHwModDaughterBd1AwRev.setStatus(_A)
_WfHwModDaughterBd1Rev_Type=OctetString
_WfHwModDaughterBd1Rev_Object=MibTableColumn
wfHwModDaughterBd1Rev=_WfHwModDaughterBd1Rev_Object((1,3,6,1,4,1,18,3,1,2,1,35),_WfHwModDaughterBd1Rev_Type())
wfHwModDaughterBd1Rev.setMaxAccess(_B)
if mibBuilder.loadTexts:wfHwModDaughterBd1Rev.setStatus(_A)
_WfHwModDaughterBd1SerialNumber_Type=OctetString
_WfHwModDaughterBd1SerialNumber_Object=MibTableColumn
wfHwModDaughterBd1SerialNumber=_WfHwModDaughterBd1SerialNumber_Object((1,3,6,1,4,1,18,3,1,2,1,36),_WfHwModDaughterBd1SerialNumber_Type())
wfHwModDaughterBd1SerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:wfHwModDaughterBd1SerialNumber.setStatus(_A)
_WfHwModDaughterBd2IdOpt_Type=Integer32
_WfHwModDaughterBd2IdOpt_Object=MibTableColumn
wfHwModDaughterBd2IdOpt=_WfHwModDaughterBd2IdOpt_Object((1,3,6,1,4,1,18,3,1,2,1,37),_WfHwModDaughterBd2IdOpt_Type())
wfHwModDaughterBd2IdOpt.setMaxAccess(_B)
if mibBuilder.loadTexts:wfHwModDaughterBd2IdOpt.setStatus(_A)
_WfHwModDaughterBd2AwRev_Type=OctetString
_WfHwModDaughterBd2AwRev_Object=MibTableColumn
wfHwModDaughterBd2AwRev=_WfHwModDaughterBd2AwRev_Object((1,3,6,1,4,1,18,3,1,2,1,38),_WfHwModDaughterBd2AwRev_Type())
wfHwModDaughterBd2AwRev.setMaxAccess(_B)
if mibBuilder.loadTexts:wfHwModDaughterBd2AwRev.setStatus(_A)
_WfHwModDaughterBd2Rev_Type=OctetString
_WfHwModDaughterBd2Rev_Object=MibTableColumn
wfHwModDaughterBd2Rev=_WfHwModDaughterBd2Rev_Object((1,3,6,1,4,1,18,3,1,2,1,39),_WfHwModDaughterBd2Rev_Type())
wfHwModDaughterBd2Rev.setMaxAccess(_B)
if mibBuilder.loadTexts:wfHwModDaughterBd2Rev.setStatus(_A)
_WfHwModDaughterBd2SerialNumber_Type=OctetString
_WfHwModDaughterBd2SerialNumber_Object=MibTableColumn
wfHwModDaughterBd2SerialNumber=_WfHwModDaughterBd2SerialNumber_Object((1,3,6,1,4,1,18,3,1,2,1,40),_WfHwModDaughterBd2SerialNumber_Type())
wfHwModDaughterBd2SerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:wfHwModDaughterBd2SerialNumber.setStatus(_A)
class _WfRASNPwrSupply1_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_F,2),(_D,3),(_G,4)))
_WfRASNPwrSupply1_Type.__name__=_C
_WfRASNPwrSupply1_Object=MibTableColumn
wfRASNPwrSupply1=_WfRASNPwrSupply1_Object((1,3,6,1,4,1,18,3,1,2,1,41),_WfRASNPwrSupply1_Type())
wfRASNPwrSupply1.setMaxAccess(_B)
if mibBuilder.loadTexts:wfRASNPwrSupply1.setStatus(_A)
class _WfRASNPwrSupply2_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_F,2),(_D,3),(_G,4)))
_WfRASNPwrSupply2_Type.__name__=_C
_WfRASNPwrSupply2_Object=MibTableColumn
wfRASNPwrSupply2=_WfRASNPwrSupply2_Object((1,3,6,1,4,1,18,3,1,2,1,42),_WfRASNPwrSupply2_Type())
wfRASNPwrSupply2.setMaxAccess(_B)
if mibBuilder.loadTexts:wfRASNPwrSupply2.setStatus(_A)
class _WfPowerSupply1_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_F,2),(_D,3),(_G,4)))
_WfPowerSupply1_Type.__name__=_C
_WfPowerSupply1_Object=MibTableColumn
wfPowerSupply1=_WfPowerSupply1_Object((1,3,6,1,4,1,18,3,1,2,1,43),_WfPowerSupply1_Type())
wfPowerSupply1.setMaxAccess(_B)
if mibBuilder.loadTexts:wfPowerSupply1.setStatus(_A)
class _WfPowerSupply2_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_F,2),(_D,3),(_G,4)))
_WfPowerSupply2_Type.__name__=_C
_WfPowerSupply2_Object=MibTableColumn
wfPowerSupply2=_WfPowerSupply2_Object((1,3,6,1,4,1,18,3,1,2,1,44),_WfPowerSupply2_Type())
wfPowerSupply2.setMaxAccess(_B)
if mibBuilder.loadTexts:wfPowerSupply2.setStatus(_A)
class _WfFanStatus1_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_F,2),(_D,3),(_G,4)))
_WfFanStatus1_Type.__name__=_C
_WfFanStatus1_Object=MibTableColumn
wfFanStatus1=_WfFanStatus1_Object((1,3,6,1,4,1,18,3,1,2,1,45),_WfFanStatus1_Type())
wfFanStatus1.setMaxAccess(_B)
if mibBuilder.loadTexts:wfFanStatus1.setStatus(_A)
class _WfFanStatus2_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_F,2),(_D,3),(_G,4)))
_WfFanStatus2_Type.__name__=_C
_WfFanStatus2_Object=MibTableColumn
wfFanStatus2=_WfFanStatus2_Object((1,3,6,1,4,1,18,3,1,2,1,46),_WfFanStatus2_Type())
wfFanStatus2.setMaxAccess(_B)
if mibBuilder.loadTexts:wfFanStatus2.setStatus(_A)
class _WfRASNRPSUPresent_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_Q,1),(_D,2),(_G,3)))
_WfRASNRPSUPresent_Type.__name__=_C
_WfRASNRPSUPresent_Object=MibTableColumn
wfRASNRPSUPresent=_WfRASNRPSUPresent_Object((1,3,6,1,4,1,18,3,1,2,1,47),_WfRASNRPSUPresent_Type())
wfRASNRPSUPresent.setMaxAccess(_R)
if mibBuilder.loadTexts:wfRASNRPSUPresent.setStatus('obsolete')
class _WfModDiagStatus_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,20)));namedValues=NamedValues(*(('passed',1),('failed',2),('notrun',3),(_D,4),(_G,20)))
_WfModDiagStatus_Type.__name__=_C
_WfModDiagStatus_Object=MibTableColumn
wfModDiagStatus=_WfModDiagStatus_Object((1,3,6,1,4,1,18,3,1,2,1,48),_WfModDiagStatus_Type())
wfModDiagStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:wfModDiagStatus.setStatus(_A)
_WfHwCfgTable_Object=MibTable
wfHwCfgTable=_WfHwCfgTable_Object((1,3,6,1,4,1,18,3,1,7))
if mibBuilder.loadTexts:wfHwCfgTable.setStatus(_A)
_WfHwCfgEntry_Object=MibTableRow
wfHwCfgEntry=_WfHwCfgEntry_Object((1,3,6,1,4,1,18,3,1,7,1))
wfHwCfgEntry.setIndexNames((0,_K,_S))
if mibBuilder.loadTexts:wfHwCfgEntry.setStatus(_A)
_WfHwCfgSlot_Type=Integer32
_WfHwCfgSlot_Object=MibTableColumn
wfHwCfgSlot=_WfHwCfgSlot_Object((1,3,6,1,4,1,18,3,1,7,1,1),_WfHwCfgSlot_Type())
wfHwCfgSlot.setMaxAccess(_B)
if mibBuilder.loadTexts:wfHwCfgSlot.setStatus(_A)
class _WfRPSUPresent_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_Q,1),(_D,2),(_G,3)))
_WfRPSUPresent_Type.__name__=_C
_WfRPSUPresent_Object=MibTableColumn
wfRPSUPresent=_WfRPSUPresent_Object((1,3,6,1,4,1,18,3,1,7,1,2),_WfRPSUPresent_Type())
wfRPSUPresent.setMaxAccess(_R)
if mibBuilder.loadTexts:wfRPSUPresent.setStatus(_A)
mibBuilder.exportSymbols(_K,**{'wfHwBase':wfHwBase,'wfHwBpIdOpt':wfHwBpIdOpt,'wfHwBpRev':wfHwBpRev,'wfHwBpSerialNumber':wfHwBpSerialNumber,'wfBCNPwrSupply1':wfBCNPwrSupply1,'wfBCNPwrSupply2':wfBCNPwrSupply2,'wfBCNPwrSupply3':wfBCNPwrSupply3,'wfBCNPwrSupply4':wfBCNPwrSupply4,'wfBCNFanStatus':wfBCNFanStatus,'wfBCNTemperature':wfBCNTemperature,'wfBCNTemperature2':wfBCNTemperature2,'wfFanSpeed':wfFanSpeed,'wfHwTable':wfHwTable,'wfHwEntry':wfHwEntry,_M:wfHwSlot,'wfHwModIdOpt':wfHwModIdOpt,'wfHwModRev':wfHwModRev,'wfHwModSerialNumber':wfHwModSerialNumber,'wfHwMotherBdIdOpt':wfHwMotherBdIdOpt,'wfHwMotherBdRev':wfHwMotherBdRev,'wfHwMotherBdSerialNumber':wfHwMotherBdSerialNumber,'wfHwDaughterBdIdOpt':wfHwDaughterBdIdOpt,'wfHwDaughterBdRev':wfHwDaughterBdRev,'wfHwDaughterBdSerialNumber':wfHwDaughterBdSerialNumber,'wfHwBabyBdIdOpt':wfHwBabyBdIdOpt,'wfHwBabyBdRev':wfHwBabyBdRev,'wfHwBabyBdSerialNumber':wfHwBabyBdSerialNumber,'wfHwDiagPromRev':wfHwDiagPromRev,'wfHwDiagPromDate':wfHwDiagPromDate,'wfHwDiagPromSource':wfHwDiagPromSource,'wfHwBootPromRev':wfHwBootPromRev,'wfHwBootPromDate':wfHwBootPromDate,'wfHwBootPromSource':wfHwBootPromSource,'wfHwSparePromRev':wfHwSparePromRev,'wfHwSparePromDate':wfHwSparePromDate,'wfHwSparePromSource':wfHwSparePromSource,'wfHwFileSysPresent':wfHwFileSysPresent,'wfHwFileSysPresent2':wfHwFileSysPresent2,'wfHwConfigServer':wfHwConfigServer,'wfHwConfigFile':wfHwConfigFile,'wfHwConfigDateAndTime':wfHwConfigDateAndTime,'wfHwActiveImageName':wfHwActiveImageName,'wfHwActiveImageSource':wfHwActiveImageSource,'wfHwActiveImageDate':wfHwActiveImageDate,'wfHwMotherBdMemorySize':wfHwMotherBdMemorySize,'wfHwFastPacketCacheSize':wfHwFastPacketCacheSize,'wfHwModDaughterBd1IdOpt':wfHwModDaughterBd1IdOpt,'wfHwModDaughterBd1AwRev':wfHwModDaughterBd1AwRev,'wfHwModDaughterBd1Rev':wfHwModDaughterBd1Rev,'wfHwModDaughterBd1SerialNumber':wfHwModDaughterBd1SerialNumber,'wfHwModDaughterBd2IdOpt':wfHwModDaughterBd2IdOpt,'wfHwModDaughterBd2AwRev':wfHwModDaughterBd2AwRev,'wfHwModDaughterBd2Rev':wfHwModDaughterBd2Rev,'wfHwModDaughterBd2SerialNumber':wfHwModDaughterBd2SerialNumber,'wfRASNPwrSupply1':wfRASNPwrSupply1,'wfRASNPwrSupply2':wfRASNPwrSupply2,'wfPowerSupply1':wfPowerSupply1,'wfPowerSupply2':wfPowerSupply2,'wfFanStatus1':wfFanStatus1,'wfFanStatus2':wfFanStatus2,'wfRASNRPSUPresent':wfRASNRPSUPresent,'wfModDiagStatus':wfModDiagStatus,'wfHwCfgTable':wfHwCfgTable,'wfHwCfgEntry':wfHwCfgEntry,_S:wfHwCfgSlot,'wfRPSUPresent':wfRPSUPresent})