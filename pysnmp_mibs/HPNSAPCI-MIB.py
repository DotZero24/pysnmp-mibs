_J='hpnsaPciFunctionIndex'
_I='hpnsaPciDeviceIndex'
_H='hpnsaPciBusIndex'
_G='hpnsaPciAgentIndex'
_F='DisplayString'
_E='HPNSAPCI-MIB'
_D='OctetString'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','TextualConvention')
_Hp_ObjectIdentity=ObjectIdentity
hp=_Hp_ObjectIdentity((1,3,6,1,4,1,11))
_Nm_ObjectIdentity=ObjectIdentity
nm=_Nm_ObjectIdentity((1,3,6,1,4,1,11,2))
_Hpnsa_ObjectIdentity=ObjectIdentity
hpnsa=_Hpnsa_ObjectIdentity((1,3,6,1,4,1,11,2,23))
_HpnsaPci_ObjectIdentity=ObjectIdentity
hpnsaPci=_HpnsaPci_ObjectIdentity((1,3,6,1,4,1,11,2,23,10))
_HpnsaPciMibRev_ObjectIdentity=ObjectIdentity
hpnsaPciMibRev=_HpnsaPciMibRev_ObjectIdentity((1,3,6,1,4,1,11,2,23,10,1))
class _HpnsaPciMibRevMajor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpnsaPciMibRevMajor_Type.__name__=_C
_HpnsaPciMibRevMajor_Object=MibScalar
hpnsaPciMibRevMajor=_HpnsaPciMibRevMajor_Object((1,3,6,1,4,1,11,2,23,10,1,1),_HpnsaPciMibRevMajor_Type())
hpnsaPciMibRevMajor.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaPciMibRevMajor.setStatus(_A)
class _HpnsaPciMibRevMinor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnsaPciMibRevMinor_Type.__name__=_C
_HpnsaPciMibRevMinor_Object=MibScalar
hpnsaPciMibRevMinor=_HpnsaPciMibRevMinor_Object((1,3,6,1,4,1,11,2,23,10,1,2),_HpnsaPciMibRevMinor_Type())
hpnsaPciMibRevMinor.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaPciMibRevMinor.setStatus(_A)
_HpnsaPciAgent_ObjectIdentity=ObjectIdentity
hpnsaPciAgent=_HpnsaPciAgent_ObjectIdentity((1,3,6,1,4,1,11,2,23,10,2))
_HpnsaPciAgentTable_Object=MibTable
hpnsaPciAgentTable=_HpnsaPciAgentTable_Object((1,3,6,1,4,1,11,2,23,10,2,1))
if mibBuilder.loadTexts:hpnsaPciAgentTable.setStatus(_A)
_HpnsaPciAgentEntry_Object=MibTableRow
hpnsaPciAgentEntry=_HpnsaPciAgentEntry_Object((1,3,6,1,4,1,11,2,23,10,2,1,1))
hpnsaPciAgentEntry.setIndexNames((0,_E,_G))
if mibBuilder.loadTexts:hpnsaPciAgentEntry.setStatus(_A)
class _HpnsaPciAgentIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HpnsaPciAgentIndex_Type.__name__=_C
_HpnsaPciAgentIndex_Object=MibTableColumn
hpnsaPciAgentIndex=_HpnsaPciAgentIndex_Object((1,3,6,1,4,1,11,2,23,10,2,1,1,1),_HpnsaPciAgentIndex_Type())
hpnsaPciAgentIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaPciAgentIndex.setStatus(_A)
class _HpnsaPciAgentName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnsaPciAgentName_Type.__name__=_F
_HpnsaPciAgentName_Object=MibTableColumn
hpnsaPciAgentName=_HpnsaPciAgentName_Object((1,3,6,1,4,1,11,2,23,10,2,1,1,2),_HpnsaPciAgentName_Type())
hpnsaPciAgentName.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaPciAgentName.setStatus(_A)
class _HpnsaPciAgentVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_HpnsaPciAgentVersion_Type.__name__=_F
_HpnsaPciAgentVersion_Object=MibTableColumn
hpnsaPciAgentVersion=_HpnsaPciAgentVersion_Object((1,3,6,1,4,1,11,2,23,10,2,1,1,3),_HpnsaPciAgentVersion_Type())
hpnsaPciAgentVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaPciAgentVersion.setStatus(_A)
class _HpnsaPciAgentDate_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(7,7));fixedLength=7
_HpnsaPciAgentDate_Type.__name__=_D
_HpnsaPciAgentDate_Object=MibTableColumn
hpnsaPciAgentDate=_HpnsaPciAgentDate_Object((1,3,6,1,4,1,11,2,23,10,2,1,1,4),_HpnsaPciAgentDate_Type())
hpnsaPciAgentDate.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaPciAgentDate.setStatus(_A)
_HpnsaPciBios_ObjectIdentity=ObjectIdentity
hpnsaPciBios=_HpnsaPciBios_ObjectIdentity((1,3,6,1,4,1,11,2,23,10,3))
class _HpnsaPciBiosPresent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('notPresent',0),('present',1)))
_HpnsaPciBiosPresent_Type.__name__=_C
_HpnsaPciBiosPresent_Object=MibScalar
hpnsaPciBiosPresent=_HpnsaPciBiosPresent_Object((1,3,6,1,4,1,11,2,23,10,3,1),_HpnsaPciBiosPresent_Type())
hpnsaPciBiosPresent.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaPciBiosPresent.setStatus(_A)
_HpnsaPciBiosVersion_Type=Integer32
_HpnsaPciBiosVersion_Object=MibScalar
hpnsaPciBiosVersion=_HpnsaPciBiosVersion_Object((1,3,6,1,4,1,11,2,23,10,3,2),_HpnsaPciBiosVersion_Type())
hpnsaPciBiosVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaPciBiosVersion.setStatus(_A)
class _HpnsaPciBuses_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HpnsaPciBuses_Type.__name__=_C
_HpnsaPciBuses_Object=MibScalar
hpnsaPciBuses=_HpnsaPciBuses_Object((1,3,6,1,4,1,11,2,23,10,3,3),_HpnsaPciBuses_Type())
hpnsaPciBuses.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaPciBuses.setStatus(_A)
_HpnsaPciConfig_ObjectIdentity=ObjectIdentity
hpnsaPciConfig=_HpnsaPciConfig_ObjectIdentity((1,3,6,1,4,1,11,2,23,10,4))
_HpnsaPciTable_Object=MibTable
hpnsaPciTable=_HpnsaPciTable_Object((1,3,6,1,4,1,11,2,23,10,4,1))
if mibBuilder.loadTexts:hpnsaPciTable.setStatus(_A)
_HpnsaPciEntry_Object=MibTableRow
hpnsaPciEntry=_HpnsaPciEntry_Object((1,3,6,1,4,1,11,2,23,10,4,1,1))
hpnsaPciEntry.setIndexNames((0,_E,_H),(0,_E,_I),(0,_E,_J))
if mibBuilder.loadTexts:hpnsaPciEntry.setStatus(_A)
class _HpnsaPciBusIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HpnsaPciBusIndex_Type.__name__=_C
_HpnsaPciBusIndex_Object=MibTableColumn
hpnsaPciBusIndex=_HpnsaPciBusIndex_Object((1,3,6,1,4,1,11,2,23,10,4,1,1,1),_HpnsaPciBusIndex_Type())
hpnsaPciBusIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaPciBusIndex.setStatus(_A)
class _HpnsaPciDeviceIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
_HpnsaPciDeviceIndex_Type.__name__=_C
_HpnsaPciDeviceIndex_Object=MibTableColumn
hpnsaPciDeviceIndex=_HpnsaPciDeviceIndex_Object((1,3,6,1,4,1,11,2,23,10,4,1,1,2),_HpnsaPciDeviceIndex_Type())
hpnsaPciDeviceIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaPciDeviceIndex.setStatus(_A)
class _HpnsaPciFunctionIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_HpnsaPciFunctionIndex_Type.__name__=_C
_HpnsaPciFunctionIndex_Object=MibTableColumn
hpnsaPciFunctionIndex=_HpnsaPciFunctionIndex_Object((1,3,6,1,4,1,11,2,23,10,4,1,1,3),_HpnsaPciFunctionIndex_Type())
hpnsaPciFunctionIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaPciFunctionIndex.setStatus(_A)
class _HpnsaPciVendorId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(3601,4096,4098,4099,4100,4101,4102,4103,4104,4106,4107,4108,4109,4110,4112,4113,4114,4115,4116,4118,4119,4120,4121,4122,4123,4124,4126,4127,4128,4129,4130,4131,4132,4133,4136,4137,4139,4140,4141,4142,4143,4144,4145,4146,4147,4148,4149,4150,4151,4152,4153,4154,4155,4156,4158,4159,4160,4161,4162,4163,4164,4165,4166,4167,4168,4169,4170,4171,4172,4173,4174,4175,4176,4177,4178,4180,4181,4182,4183,4184,4185,4186,4187,4188,4189,4190,4191,4192,4193,4194,4195,4196,4197,4198,4199,4200,4201,4202,4203,4204,4205,4206,4207,4208,4209,4210,4211,4212,4213,4214,4215,4216,4217,4218,4219,4220,4221,4222,4223,4224,4225,4226,4227,4228,4229,4230,4231,4232,4233,4234,4236,4237,4239,4240,4241,4242,4243,4244,4245,4246,4247,4248,4249,4250,4251,4252,4253,4254,4255,4256,4257,4258,4259,4260,4261,4262,4263,4264,4265,4266,4267,4268,4269,4270,4271,4272,4273,4274,4275,4276,4277,4279,4280,4281,4282,4283,4284,4285,4286,4287,4288,4289,4290,4291,4292,4293,4294,4295,4296,4297,4298,4299,4300,4301,4302,4303,4304,4305,4306,4307,4308,4309,4310,4312,4313,4314,4315,4316,4317,4318,4319,4320,4321,4322,4323,4324,4325,4326,4327,4328,4329,4330,4331,4332,4333,4334,4335,4336,4337,4338,4339,4340,4341,4342,4343,4344,4345,4346,4347,4348,4349,4350,4351,4352,4353,4354,4355,4356,4357,4358,4359,4360,4361,4363,4364,4365,4366,4367,4368,4369,4370,4371,4372,4373,4374,4375,4376,4377,4378,4379,4380,4381,4382,4383,4384,4385,4386,4387,4388,4389,4393,4394,4395,4397,4398,4399,4400,4401,4402,4403,4404,4405,4406,4407,4408,4409,4410,4412,4413,4414,4415,4416,4417,4418,4419,4420,4421,4422,4423,4424,4425,4426,4427,4428,4429,4430,4431,4432,4433,4434,4435,4436,4437,4438,21299,22272,32902,36868,60888)));namedValues=NamedValues(*(('Compaq_Computer_Corp',3601),('Symbios_Inc',4096),('ATI_Technologies_Inc',4098),('Ulsi_Systems',4099),('VLSI_Technology_Inc',4100),('Avance_Logics_Inc',4101),('Reply_Group',4102),('Netframe_Systems_Inc',4103),('Epson',4104),('Phoenix_Technologies',4106),('National_Semiconductor',4107),('Tseng_Labs_Inc',4108),('AST_Research_Inc',4109),('Weitek',4110),('Video_Logic_Ltd',4112),('DEC',4113),('Micronics_Computers_Inc',4114),('Cirrus_Logic',4115),('IBM',4116),('ICL_Personal_Systems',4118),('Spea_Software_Ag',4119),('Unisys_Systems',4120),('Elitegroup_Computer_Sys',4121),('NCR',4122),('Vitesse_Semiconductor',4123),('Western_Digital',4124),('American_Megatrends',4126),('Picture_Tel',4127),('Hitachi_Computer_Products',4128),('Oki_Electric_Industry',4129),('Advanced_Micro_Devices',4130),('Trident_Microsystems',4131),('Zenith_Data_Systems',4132),('Acer_Incorporated',4133),('Dell_Computer_Corporation',4136),('Siemens_Nixdorf_IS_AG',4137),('Matrox',4139),('Chips_And_Technologies',4140),('Wyse_Technology',4141),('Olivetti_Advanced_Technology',4142),('Toshiba_America_Elect',4143),('TMC_Research',4144),('Miro_Computer_Products_AG',4145),('Compaq',4146),('NEC_Corporation',4147),('Burndy_Corporation',4148),('Comp_Comm_Resh_Lab',4149),('Future_Domain',4150),('Hitachi_Micro_Systems',4151),('AMP_Inc',4152),('Silicon_Integrated_System',4153),('Seiko_Epson_Corporation',4154),('Tatung_Co_Of_America',4155),('Hewlett-Packard',4156),('Solliday_Engineering',4158),('Logic_Modeling',4159),('Kubota_Pacific_Computer_Inc',4160),('Computrend',4161),('PC_Technology_Inc',4162),('Asustek_Computer_Inc',4163),('Distributed_Processing_Technology',4164),('OPTI',4165),('IPC_Corporation_Ltd',4166),('Genoa_Systems_Corp',4167),('Elsa_Gmbh',4168),('Fountain_Technology',4169),('Sgs_Thomson_Microelectric',4170),('Buslogic',4171),('Texas_Instruments',4172),('Sony_Corporation',4173),('Oak_Technology_Inc',4174),('Co-Time_Computer_Ltd',4175),('Winbond_Electronics_Corp',4176),('Anigma_Inc',4177),('Young_Micro_Systems',4178),('Hitachi_Ltd',4180),('Efar_Microsystems',4181),('ICL',4182),('Motorola_Computer',4183),('Electronics_Telec_Rsh',4184),('Teknor_Microsystems',4185),('Promise_Technology',4186),('Foxconn_International',4187),('Wipro_Infotech_Limited',4188),('Number_9_Computer_Company',4189),('VTECH_Computers_Limites',4190),('Infotronic_America_Inc',4191),('United_Microelectronics',4192),('ITT',4193),('Maspar_Computer_Corp',4194),('Ocean_Office_Automation',4195),('Alcatel_CIT',4196),('Texas_Microsystems',4197),('Picopower_Technology',4198),('Mitsubishi_Electronics',4199),('Diversified_Technology',4200),('Mylex_Corporation',4201),('Aten_Research_Inc',4202),('Apple_Computer_Inc',4203),('Hyundai_Electronics_Ameri',4204),('Sequent',4205),('DFI_Inc',4206),('City_Gate_Development_Ltd',4207),('Daewoo_Telecom_Ltd',4208),('Mitac',4209),('GIT_CO_LTD',4210),('Yamaha_Corporation',4211),('Nexgen_Microsysteme',4212),('Advanced_Integration_Res',4213),('Chaintech_Computer_Co_Ltd',4214),('Q_Logic',4215),('Cyrix_Corporation',4216),('I-BUS',4217),('Networth',4218),('Gateway_2000',4219),('Goldstar_Co_Ltd',4220),('Leadtek_Research_Inc',4221),('Interphase_Corporation',4222),('Data_Technology_Corporation',4223),('Contaq_Microsystems_Inc',4224),('Supermac_Technology_Inc',4225),('EFA_Corporation_Of_America',4226),('Forex_Computer_Corporation',4227),('Parador',4228),('Tulip_Computers_Int_BV',4229),('J_Bond_Computer_Systems',4230),('Cache_Computer',4231),('Microcomputer_Systems__M_SON',4232),('Data_General_Corporation',4233),('Bit3_Computer',4234),('Oakleigh_Systems_Inc',4236),('Olicom',4237),('Systemsoft_Corporation',4239),('Encore_Computer_Corporation',4240),('Intergraph_Corporation',4241),('Diamond_Computer_Systems',4242),('National_Instruments',4243),('First_Intl_Computers',4244),('Cmd_Technology_Inc',4245),('Alacron',4246),('Appian_Technology_Inc',4247),('Quantum_Designs_HK_Ltd',4248),('Samsung_Electronics_Co_Ltd',4249),('Packard_Bell',4250),('Gemlight_Computer_Ltd',4251),('Megachips_Corporation',4252),('Zida_Technologies_Ltd',4253),('Brooktree_Corporation',4254),('Trigem_Computer_Inc',4255),('Meidensha_Corporation',4256),('Juko_Electronics_Ind_Co_Ltd',4257),('Quantum_Corporation',4258),('Everex_Systems_Inc',4259),('Globe_Manufacturing_Sales',4260),('Racal_Interlan',4261),('Informtech_Industrial_Ltd',4262),('Benchmarq_Microelectronics',4263),('Sierra_Semiconductor',4264),('Silicon_Graphics',4265),('Acc_Microelectronics_Corp',4266),('Digicom',4267),('Honeywell_Iasd',4268),('Symphony_Labs',4269),('Cornerstone_Technology',4270),('Micro_Computer_Sysytems_Inc',4271),('Cardexpert_Technology',4272),('Cabletron_Systems_Inc',4273),('Raytheon_Company',4274),('Databook_Inc',4275),('Stb_Systems_Inc',4276),('Plx_Technology',4277),('The_3COM_Corporation',4279),('Standard_Microsystems_Corporation',4280),('Acer_Labs',4281),('Mitsubishi_Electronics_Corp',4282),('Dapha_Electronics_Corporation',4283),('Advanced_Logic_Research_Inc',4284),('Surecom_Technology',4285),('Tsenglabs_International_Co',4286),('Most_Inc',4287),('Boca_Research_Inc',4288),('ICM_Co_Ltd',4289),('Auspex_Systems_Inc',4290),('Samsung_Semiconductors',4291),('Award_Software_Intl_Inc',4292),('Xerox_Corporation',4293),('Rambus_Inc',4294),('Media_Vision',4295),('Neomagic_Corporation',4296),('Dataexpert_Corporation',4297),('Fujitsu',4298),('Omron_Corporation',4299),('Mentor_Arc_Inc',4300),('Advanced_System_Products',4301),('Radius_Inc',4302),('Citicorp_TTI',4303),('Fujitsu_Limited',4304),('Future_Systems',4305),('Molex_Incorporated',4306),('Jabil_Circuit_Inc',4307),('Hualon_Microelectronics',4308),('Autologic_Inc',4309),('Cetia',4310),('Advanced_Peripherals_Labs',4312),('Macronix_International_Co_Ltd',4313),('Thomas-Conrad_Corporation',4314),('Rohm_Research',4315),('Cern_Ecp_Edu',4316),('Evans_Sutherland',4317),('Nvidia_Corporation',4318),('Emulex_Corporation',4319),('Integrated_Micro_Solutions_Inc',4320),('Tekram_Technology_Co_Ltd',4321),('Aptix_Corporation',4322),('Newbridge_Microsystems',4323),('Tandem_Computers',4324),('Micro_Industries_Corporation',4325),('Gainbery_Computer_Products_Inc',4326),('Vadem',4327),('Applied_Micro_Circuits_Corporation',4328),('Alps_Electric_Co_Ltd',4329),('Integraphics_Systems',4330),('Artists_Graphics',4331),('Realtek_Semiconductor_Co_Ltd',4332),('Ascii_Corporation',4333),('Xilinx_Corporation',4334),('Racore_Computer_Products_Inc',4335),('Peritek_Corporation',4336),('Tyan_Computer',4337),('Achme_Computer_Inc',4338),('Alaris_Inc',4339),('S-MOS_Systems',4340),('NKK_Corporation',4341),('Creative_Electronic_Systems_SA',4342),('Matsushita_Electric_Industrial_Co_Ltd',4343),('Altos_India_Ltd',4344),('PC_Direct',4345),('Truevision',4346),('Thesys_Ges_F_Mikroelektronik_MGH',4347),('I-O_Data_Device_Inc',4348),('Soyo_Technology_Co_Ltd',4349),('Fast_Electronic_GMBH',4350),('Ncube',4351),('Jazz_Multimedia',4352),('Initio_Corporation',4353),('Creative_Labs',4354),('Triones_Technologies_Inc',4355),('Rasterops',4356),('Sigma_Designs_Inc',4357),('Via_Technologies_Inc',4358),('Stratus_Computer',4359),('Proteon_Inc',4360),('Cogent_Data_Technologies',4361),('Xenon_Microsystems',4363),('Mini-Max_Technology_Inc',4364),('Znyx_Advanced_Systems',4365),('CPU_Technology',4366),('Ross_Technology',4367),('Powerhouse_Systems',4368),('Santa_Cruz_Operation',4369),('Rockwell_Network_Systems',4370),('Accton_Technology_Corporation',4371),('Atmel_Corp',4372),('The_3dLabs',4373),('Data_Translation',4374),('Datacube_Inc',4375),('Berg_Electronics',4376),('Vortex_Computersysteme_Gmbh',4377),('Efficent_Networks_Inc',4378),('Teledyne_Electronic_Systems',4379),('Tricord_Systems_Inc',4380),('Integrated_Device_Tech',4381),('Eldec_Corporaton',4382),('Prescision_Digital_Images',4383),('EMC_Corporation',4384),('Zilog',4385),('Multi-Tech_Systems_Inc',4386),('Leutron_Vision_Ag',4387),('Eurocore',4388),('Vigra',4389),('Firmworks',4393),('Hermes_Electronics_Co_Ltd',4394),('Linotype_Hell_AG',4395),('Ravicad',4397),('Infomedia_Microelectronics_Inc',4398),('Imaging_Technology_Inc',4399),('Computervision',4400),('Philips_Semiconductors',4401),('Mitel_Corp',4402),('Eicon_Technology_Corporation',4403),('Mercury_Computer_Systems_Inc',4404),('Fuji_Xerox_Co_Ltd',4405),('Momentum_Data_Systems',4406),('Cisco_Systems_Inc',4407),('Ziatech_Corporation',4408),('Dynamic_Pictures_Inc',4409),('FWB_Inc',4410),('Cyclone_Micro',4412),('Leading_Edge_Products_Inc',4413),('Sanyo_Electric_Co',4414),('Equinox_Systems',4415),('Intervoice_Inc',4416),('Crest_Microsystem_Inc',4417),('Alliance_Semiconductor_Corporation',4418),('Netpower_Inc',4419),('Cincinnati_Milacron',4420),('Workbit_Corp',4421),('Force_Computers',4422),('Interface_Corp',4423),('Schneider_Koch_Co',4424),('Win_System_Corporation',4425),('VMIC',4426),('Canopus_Co_Ltd',4427),('Annabooks',4428),('IC_Corporation',4429),('Nikon_Systems_Inc',4430),('Digi_International',4431),('Thinking_Machines_Corp',4432),('Jae_Electronics_Inc',4433),('Megatek',4434),('Land_Win_Electronic_Corp',4435),('Melco_Inc',4436),('Pine_Technology_Ltd',4437),('Periscope_Engineering',4438),('S3_Inc',21299),('Netpower',22272),('Intel',32902),('Adaptec',36868),('Ark_Logic_Inc',60888)))
_HpnsaPciVendorId_Type.__name__=_C
_HpnsaPciVendorId_Object=MibTableColumn
hpnsaPciVendorId=_HpnsaPciVendorId_Object((1,3,6,1,4,1,11,2,23,10,4,1,1,4),_HpnsaPciVendorId_Type())
hpnsaPciVendorId.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaPciVendorId.setStatus(_A)
_HpnsaPciDeviceId_Type=Integer32
_HpnsaPciDeviceId_Object=MibTableColumn
hpnsaPciDeviceId=_HpnsaPciDeviceId_Object((1,3,6,1,4,1,11,2,23,10,4,1,1,5),_HpnsaPciDeviceId_Type())
hpnsaPciDeviceId.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaPciDeviceId.setStatus(_A)
_HpnsaPciRevisionId_Type=Integer32
_HpnsaPciRevisionId_Object=MibTableColumn
hpnsaPciRevisionId=_HpnsaPciRevisionId_Object((1,3,6,1,4,1,11,2,23,10,4,1,1,6),_HpnsaPciRevisionId_Type())
hpnsaPciRevisionId.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaPciRevisionId.setStatus(_A)
class _HpnsaPciHeaderType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HpnsaPciHeaderType_Type.__name__=_C
_HpnsaPciHeaderType_Object=MibTableColumn
hpnsaPciHeaderType=_HpnsaPciHeaderType_Object((1,3,6,1,4,1,11,2,23,10,4,1,1,7),_HpnsaPciHeaderType_Type())
hpnsaPciHeaderType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaPciHeaderType.setStatus(_A)
class _HpnsaPciClassCode_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,3));fixedLength=3
_HpnsaPciClassCode_Type.__name__=_D
_HpnsaPciClassCode_Object=MibTableColumn
hpnsaPciClassCode=_HpnsaPciClassCode_Object((1,3,6,1,4,1,11,2,23,10,4,1,1,8),_HpnsaPciClassCode_Type())
hpnsaPciClassCode.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaPciClassCode.setStatus(_A)
_HpnsaPciCommand_Type=Integer32
_HpnsaPciCommand_Object=MibTableColumn
hpnsaPciCommand=_HpnsaPciCommand_Object((1,3,6,1,4,1,11,2,23,10,4,1,1,9),_HpnsaPciCommand_Type())
hpnsaPciCommand.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaPciCommand.setStatus(_A)
_HpnsaPciStatus_Type=Integer32
_HpnsaPciStatus_Object=MibTableColumn
hpnsaPciStatus=_HpnsaPciStatus_Object((1,3,6,1,4,1,11,2,23,10,4,1,1,10),_HpnsaPciStatus_Type())
hpnsaPciStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaPciStatus.setStatus(_A)
class _HpnsaPciCacheLineSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HpnsaPciCacheLineSize_Type.__name__=_C
_HpnsaPciCacheLineSize_Object=MibTableColumn
hpnsaPciCacheLineSize=_HpnsaPciCacheLineSize_Object((1,3,6,1,4,1,11,2,23,10,4,1,1,11),_HpnsaPciCacheLineSize_Type())
hpnsaPciCacheLineSize.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaPciCacheLineSize.setStatus(_A)
class _HpnsaPciLatencyTimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HpnsaPciLatencyTimer_Type.__name__=_C
_HpnsaPciLatencyTimer_Object=MibTableColumn
hpnsaPciLatencyTimer=_HpnsaPciLatencyTimer_Object((1,3,6,1,4,1,11,2,23,10,4,1,1,12),_HpnsaPciLatencyTimer_Type())
hpnsaPciLatencyTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaPciLatencyTimer.setStatus(_A)
class _HpnsaPciBist_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HpnsaPciBist_Type.__name__=_C
_HpnsaPciBist_Object=MibTableColumn
hpnsaPciBist=_HpnsaPciBist_Object((1,3,6,1,4,1,11,2,23,10,4,1,1,13),_HpnsaPciBist_Type())
hpnsaPciBist.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaPciBist.setStatus(_A)
class _HpnsaPciInterruptLine_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HpnsaPciInterruptLine_Type.__name__=_C
_HpnsaPciInterruptLine_Object=MibTableColumn
hpnsaPciInterruptLine=_HpnsaPciInterruptLine_Object((1,3,6,1,4,1,11,2,23,10,4,1,1,14),_HpnsaPciInterruptLine_Type())
hpnsaPciInterruptLine.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaPciInterruptLine.setStatus(_A)
class _HpnsaPciInterruptPin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HpnsaPciInterruptPin_Type.__name__=_C
_HpnsaPciInterruptPin_Object=MibTableColumn
hpnsaPciInterruptPin=_HpnsaPciInterruptPin_Object((1,3,6,1,4,1,11,2,23,10,4,1,1,15),_HpnsaPciInterruptPin_Type())
hpnsaPciInterruptPin.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaPciInterruptPin.setStatus(_A)
class _HpnsaPciMaxLat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HpnsaPciMaxLat_Type.__name__=_C
_HpnsaPciMaxLat_Object=MibTableColumn
hpnsaPciMaxLat=_HpnsaPciMaxLat_Object((1,3,6,1,4,1,11,2,23,10,4,1,1,16),_HpnsaPciMaxLat_Type())
hpnsaPciMaxLat.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaPciMaxLat.setStatus(_A)
class _HpnsaPciMinGnt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HpnsaPciMinGnt_Type.__name__=_C
_HpnsaPciMinGnt_Object=MibTableColumn
hpnsaPciMinGnt=_HpnsaPciMinGnt_Object((1,3,6,1,4,1,11,2,23,10,4,1,1,17),_HpnsaPciMinGnt_Type())
hpnsaPciMinGnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaPciMinGnt.setStatus(_A)
class _HpnsaPciBaseAddrRegs_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(24,24));fixedLength=24
_HpnsaPciBaseAddrRegs_Type.__name__=_D
_HpnsaPciBaseAddrRegs_Object=MibTableColumn
hpnsaPciBaseAddrRegs=_HpnsaPciBaseAddrRegs_Object((1,3,6,1,4,1,11,2,23,10,4,1,1,18),_HpnsaPciBaseAddrRegs_Type())
hpnsaPciBaseAddrRegs.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaPciBaseAddrRegs.setStatus(_A)
class _HpnsaPciExpRomBaseAddr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_HpnsaPciExpRomBaseAddr_Type.__name__=_D
_HpnsaPciExpRomBaseAddr_Object=MibTableColumn
hpnsaPciExpRomBaseAddr=_HpnsaPciExpRomBaseAddr_Object((1,3,6,1,4,1,11,2,23,10,4,1,1,19),_HpnsaPciExpRomBaseAddr_Type())
hpnsaPciExpRomBaseAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaPciExpRomBaseAddr.setStatus(_A)
class _HpnsaPciDeviceSpecific_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(192,192));fixedLength=192
_HpnsaPciDeviceSpecific_Type.__name__=_D
_HpnsaPciDeviceSpecific_Object=MibTableColumn
hpnsaPciDeviceSpecific=_HpnsaPciDeviceSpecific_Object((1,3,6,1,4,1,11,2,23,10,4,1,1,20),_HpnsaPciDeviceSpecific_Type())
hpnsaPciDeviceSpecific.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaPciDeviceSpecific.setStatus(_A)
_HpnsaPciSlotNumber_Type=Integer32
_HpnsaPciSlotNumber_Object=MibScalar
hpnsaPciSlotNumber=_HpnsaPciSlotNumber_Object((1,3,6,1,4,1,11,2,23,10,4,1,1,21),_HpnsaPciSlotNumber_Type())
hpnsaPciSlotNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaPciSlotNumber.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'hp':hp,'nm':nm,'hpnsa':hpnsa,'hpnsaPci':hpnsaPci,'hpnsaPciMibRev':hpnsaPciMibRev,'hpnsaPciMibRevMajor':hpnsaPciMibRevMajor,'hpnsaPciMibRevMinor':hpnsaPciMibRevMinor,'hpnsaPciAgent':hpnsaPciAgent,'hpnsaPciAgentTable':hpnsaPciAgentTable,'hpnsaPciAgentEntry':hpnsaPciAgentEntry,_G:hpnsaPciAgentIndex,'hpnsaPciAgentName':hpnsaPciAgentName,'hpnsaPciAgentVersion':hpnsaPciAgentVersion,'hpnsaPciAgentDate':hpnsaPciAgentDate,'hpnsaPciBios':hpnsaPciBios,'hpnsaPciBiosPresent':hpnsaPciBiosPresent,'hpnsaPciBiosVersion':hpnsaPciBiosVersion,'hpnsaPciBuses':hpnsaPciBuses,'hpnsaPciConfig':hpnsaPciConfig,'hpnsaPciTable':hpnsaPciTable,'hpnsaPciEntry':hpnsaPciEntry,_H:hpnsaPciBusIndex,_I:hpnsaPciDeviceIndex,_J:hpnsaPciFunctionIndex,'hpnsaPciVendorId':hpnsaPciVendorId,'hpnsaPciDeviceId':hpnsaPciDeviceId,'hpnsaPciRevisionId':hpnsaPciRevisionId,'hpnsaPciHeaderType':hpnsaPciHeaderType,'hpnsaPciClassCode':hpnsaPciClassCode,'hpnsaPciCommand':hpnsaPciCommand,'hpnsaPciStatus':hpnsaPciStatus,'hpnsaPciCacheLineSize':hpnsaPciCacheLineSize,'hpnsaPciLatencyTimer':hpnsaPciLatencyTimer,'hpnsaPciBist':hpnsaPciBist,'hpnsaPciInterruptLine':hpnsaPciInterruptLine,'hpnsaPciInterruptPin':hpnsaPciInterruptPin,'hpnsaPciMaxLat':hpnsaPciMaxLat,'hpnsaPciMinGnt':hpnsaPciMinGnt,'hpnsaPciBaseAddrRegs':hpnsaPciBaseAddrRegs,'hpnsaPciExpRomBaseAddr':hpnsaPciExpRomBaseAddr,'hpnsaPciDeviceSpecific':hpnsaPciDeviceSpecific,'hpnsaPciSlotNumber':hpnsaPciSlotNumber})