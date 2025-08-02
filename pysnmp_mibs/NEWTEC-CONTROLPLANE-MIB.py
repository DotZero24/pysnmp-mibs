_V='ntcCtrlPlaneConfGrpV1Standard'
_U='ntcCtrlPlaneAlmNoMaster'
_T='ntcCtrlPlaneMasterIp'
_S='ntcCtrlPlaneCfgMaxQTime'
_R='ntcCtrlPlaneCfgPrio'
_Q='ntcCtrlPlaneCfgPir'
_P='ntcCtrlPlaneCfgCir'
_O='ntcCtrlPlaneCfgLabel'
_N='ntcCtrlPlaneCfgIsi'
_M='ntcCtrlPlaneCfgFrmTyp'
_L='ntcCtrlPlaneCfgNomS2EModCod'
_K='ntcCtrlPlaneCfgNomS2ModCod'
_J='ntcCtrlPlaneEnable'
_I='unspecified'
_H='DisplayString'
_G='NtcNetworkAddress'
_F='NtcEnable'
_E='Integer32'
_D='Unsigned32'
_C='read-write'
_B='NEWTEC-CONTROLPLANE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ntcFunction,=mibBuilder.importSymbols('NEWTEC-MAIN-MIB','ntcFunction')
NtcAlarmState,NtcEnable,NtcNetworkAddress=mibBuilder.importSymbols('NEWTEC-TC-MIB','NtcAlarmState',_F,_G)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_H,'PhysAddress','TextualConvention')
ntcControlPlane=ModuleIdentity((1,3,6,1,4,1,5835,5,2,4300))
if mibBuilder.loadTexts:ntcControlPlane.setRevisions(('2018-02-02 09:00','2014-10-31 08:00','2014-09-04 12:00','2014-07-15 08:00','2013-05-22 06:00'))
_NtcCtrlPlaneObjects_ObjectIdentity=ObjectIdentity
ntcCtrlPlaneObjects=_NtcCtrlPlaneObjects_ObjectIdentity((1,3,6,1,4,1,5835,5,2,4300,1))
if mibBuilder.loadTexts:ntcCtrlPlaneObjects.setStatus(_A)
class _NtcCtrlPlaneEnable_Type(NtcEnable):defaultValue=0
_NtcCtrlPlaneEnable_Type.__name__=_F
_NtcCtrlPlaneEnable_Object=MibScalar
ntcCtrlPlaneEnable=_NtcCtrlPlaneEnable_Object((1,3,6,1,4,1,5835,5,2,4300,1,1),_NtcCtrlPlaneEnable_Type())
ntcCtrlPlaneEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcCtrlPlaneEnable.setStatus(_A)
_NtcCtrlPlaneCfg_ObjectIdentity=ObjectIdentity
ntcCtrlPlaneCfg=_NtcCtrlPlaneCfg_ObjectIdentity((1,3,6,1,4,1,5835,5,2,4300,1,2))
if mibBuilder.loadTexts:ntcCtrlPlaneCfg.setStatus(_A)
class _NtcCtrlPlaneCfgNomS2ModCod_Type(Integer32):defaultValue=7;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80)));namedValues=NamedValues(*((_I,0),('qpsk14',1),('qpsk13',2),('qpsk25',3),('qpsk12',4),('qpsk35',5),('qpsk23',6),('qpsk34',7),('qpsk45',8),('qpsk56',9),('qpsk89',10),('qpsk910',11),('e8psk35',12),('e8psk23',13),('e8psk34',14),('e8psk56',15),('e8psk89',16),('e8psk910',17),('e16apsk23',18),('e16apsk34',19),('e16apsk45',20),('e16apsk56',21),('e16apsk89',22),('e16apsk910',23),('e32apsk34',24),('e32apsk45',25),('e32apsk56',26),('e32apsk89',27),('e32apsk910',28),('qpsk1345',29),('qpsk920',30),('qpsk1120',31),('e8apsk59l',32),('e8apsk2645l',33),('e8psk2336',34),('e8psk2536',35),('e8psk1318',36),('e16apsk12l',37),('e16apsk815l',38),('e16apsk59l',39),('e16apsk2645',40),('e16apsk35',41),('e16apsk35l',42),('e16apsk2845',43),('e16apsk2336',44),('e16apsk23l',45),('e16apsk2536',46),('e16apsk1318',47),('e16apsk79',48),('e16apsk7790',49),('e32apsk23l',50),('e32apsk3245',51),('e32apsk1115',52),('e32apsk79',53),('e64apsk3245l',54),('e64apsk1115',55),('e64apsk79',56),('e64apsk45',57),('e64apsk56',58),('e128apsk34',59),('e128apsk79',60),('e256apsk2945l',61),('e256apsk23l',62),('e256apsk3145l',63),('e256apsk3245',64),('e256apsk1115l',65),('e256apsk34',66),('qpsk1145',67),('qpsk415',68),('qpsk1445',69),('qpsk715',70),('qpsk815',71),('qpsk3245',72),('e8psk715',73),('e8psk815',74),('e8psk2645',75),('e8psk3245',76),('e16apsk715',77),('e16apsk815',78),('e16apsk3245',79),('e32apsk23',80)))
_NtcCtrlPlaneCfgNomS2ModCod_Type.__name__=_E
_NtcCtrlPlaneCfgNomS2ModCod_Object=MibScalar
ntcCtrlPlaneCfgNomS2ModCod=_NtcCtrlPlaneCfgNomS2ModCod_Object((1,3,6,1,4,1,5835,5,2,4300,1,2,1),_NtcCtrlPlaneCfgNomS2ModCod_Type())
ntcCtrlPlaneCfgNomS2ModCod.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcCtrlPlaneCfgNomS2ModCod.setStatus(_A)
class _NtcCtrlPlaneCfgNomS2EModCod_Type(Integer32):defaultValue=129;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,193,194,195,196,197,198,199,200,201,202,203,204,205,206,207,208,209,210,211,212,213,214,215)));namedValues=NamedValues(*((_I,0),('qpsk45180',129),('qpsk60180',130),('qpsk72180',131),('qpsk80180',132),('qpsk90180',133),('qpsk100180',134),('qpsk108180',135),('qpsk114180',136),('qpsk120180',137),('qpsk126180',138),('qpsk135180',139),('qpsk144180',140),('qpsk150180',141),('qpsk160180',142),('qpsk162180',143),('e8psk80180',144),('e8psk90180',145),('e8psk100180',146),('e8psk108180',147),('e8psk114180',148),('e8psk120180',149),('e8psk126180',150),('e8psk135180',151),('e8psk144180',152),('e8psk150180',153),('e16apsk80180',154),('e16apsk90180',155),('e16apsk100180',156),('e16apsk108180',157),('e16apsk114180',158),('e16apsk120180',159),('e16apsk126180',160),('e16apsk135180',161),('e16apsk144180',162),('e16apsk150180',163),('e16apsk160180',164),('e16apsk162180',165),('e32apsk100180',166),('e32apsk108180',167),('e32apsk114180',168),('e32apsk120180',169),('e32apsk126180',170),('e32apsk135180',171),('e32apsk144180',172),('e32apsk150180',173),('e32apsk160180',174),('e32apsk162180',175),('e64apsk90180',176),('e64apsk100180',177),('e64apsk108180',178),('e64apsk114180',179),('e64apsk120180',180),('e64apsk126180',181),('e64apsk135180',182),('e64apsk144180',183),('e64apsk150180',184),('e64apsk160180',185),('e64apsk162180',186),('e8pskl80180',187),('e8pskl90180',188),('e8pskl100180',189),('e8pskl108180',190),('e8pskl114180',191),('e8pskl120180',192),('e16apskl80180',193),('e16apskl90180',194),('e16apskl100180',195),('e16apskl108180',196),('e16apskl114180',197),('e16apskl120180',198),('e16apskl126180',199),('e16apskl135180',200),('e16apskl144180',201),('e16apskl150180',202),('e16apskl160180',203),('e16apskl162180',204),('e64apskl90180',205),('e64apskl100180',206),('e64apskl108180',207),('e64apskl114180',208),('e64apskl120180',209),('e64apskl126180',210),('e64apskl135180',211),('e64apskl144180',212),('e64apskl150180',213),('e64apskl160180',214),('e64apskl162180',215)))
_NtcCtrlPlaneCfgNomS2EModCod_Type.__name__=_E
_NtcCtrlPlaneCfgNomS2EModCod_Object=MibScalar
ntcCtrlPlaneCfgNomS2EModCod=_NtcCtrlPlaneCfgNomS2EModCod_Object((1,3,6,1,4,1,5835,5,2,4300,1,2,2),_NtcCtrlPlaneCfgNomS2EModCod_Type())
ntcCtrlPlaneCfgNomS2EModCod.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcCtrlPlaneCfgNomS2EModCod.setStatus(_A)
class _NtcCtrlPlaneCfgFrmTyp_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('short',0),('normal',1)))
_NtcCtrlPlaneCfgFrmTyp_Type.__name__=_E
_NtcCtrlPlaneCfgFrmTyp_Object=MibScalar
ntcCtrlPlaneCfgFrmTyp=_NtcCtrlPlaneCfgFrmTyp_Object((1,3,6,1,4,1,5835,5,2,4300,1,2,3),_NtcCtrlPlaneCfgFrmTyp_Type())
ntcCtrlPlaneCfgFrmTyp.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcCtrlPlaneCfgFrmTyp.setStatus(_A)
class _NtcCtrlPlaneCfgIsi_Type(Unsigned32):defaultValue=63
_NtcCtrlPlaneCfgIsi_Type.__name__=_D
_NtcCtrlPlaneCfgIsi_Object=MibScalar
ntcCtrlPlaneCfgIsi=_NtcCtrlPlaneCfgIsi_Object((1,3,6,1,4,1,5835,5,2,4300,1,2,4),_NtcCtrlPlaneCfgIsi_Type())
ntcCtrlPlaneCfgIsi.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcCtrlPlaneCfgIsi.setStatus(_A)
class _NtcCtrlPlaneCfgLabel_Type(DisplayString):defaultValue=OctetString('3F:FF:FF');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_NtcCtrlPlaneCfgLabel_Type.__name__=_H
_NtcCtrlPlaneCfgLabel_Object=MibScalar
ntcCtrlPlaneCfgLabel=_NtcCtrlPlaneCfgLabel_Object((1,3,6,1,4,1,5835,5,2,4300,1,2,5),_NtcCtrlPlaneCfgLabel_Type())
ntcCtrlPlaneCfgLabel.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcCtrlPlaneCfgLabel.setStatus(_A)
class _NtcCtrlPlaneCfgCir_Type(Unsigned32):defaultValue=256000
_NtcCtrlPlaneCfgCir_Type.__name__=_D
_NtcCtrlPlaneCfgCir_Object=MibScalar
ntcCtrlPlaneCfgCir=_NtcCtrlPlaneCfgCir_Object((1,3,6,1,4,1,5835,5,2,4300,1,2,6),_NtcCtrlPlaneCfgCir_Type())
ntcCtrlPlaneCfgCir.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcCtrlPlaneCfgCir.setStatus(_A)
if mibBuilder.loadTexts:ntcCtrlPlaneCfgCir.setUnits('bits')
class _NtcCtrlPlaneCfgPir_Type(Unsigned32):defaultValue=1000000
_NtcCtrlPlaneCfgPir_Type.__name__=_D
_NtcCtrlPlaneCfgPir_Object=MibScalar
ntcCtrlPlaneCfgPir=_NtcCtrlPlaneCfgPir_Object((1,3,6,1,4,1,5835,5,2,4300,1,2,7),_NtcCtrlPlaneCfgPir_Type())
ntcCtrlPlaneCfgPir.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcCtrlPlaneCfgPir.setStatus(_A)
if mibBuilder.loadTexts:ntcCtrlPlaneCfgPir.setUnits('bits')
class _NtcCtrlPlaneCfgPrio_Type(Unsigned32):defaultValue=0
_NtcCtrlPlaneCfgPrio_Type.__name__=_D
_NtcCtrlPlaneCfgPrio_Object=MibScalar
ntcCtrlPlaneCfgPrio=_NtcCtrlPlaneCfgPrio_Object((1,3,6,1,4,1,5835,5,2,4300,1,2,8),_NtcCtrlPlaneCfgPrio_Type())
ntcCtrlPlaneCfgPrio.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcCtrlPlaneCfgPrio.setStatus(_A)
class _NtcCtrlPlaneCfgMaxQTime_Type(Unsigned32):defaultValue=100
_NtcCtrlPlaneCfgMaxQTime_Type.__name__=_D
_NtcCtrlPlaneCfgMaxQTime_Object=MibScalar
ntcCtrlPlaneCfgMaxQTime=_NtcCtrlPlaneCfgMaxQTime_Object((1,3,6,1,4,1,5835,5,2,4300,1,2,9),_NtcCtrlPlaneCfgMaxQTime_Type())
ntcCtrlPlaneCfgMaxQTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcCtrlPlaneCfgMaxQTime.setStatus(_A)
if mibBuilder.loadTexts:ntcCtrlPlaneCfgMaxQTime.setUnits('ms')
class _NtcCtrlPlaneMasterIp_Type(NtcNetworkAddress):defaultValue=OctetString('0.0.0.0')
_NtcCtrlPlaneMasterIp_Type.__name__=_G
_NtcCtrlPlaneMasterIp_Object=MibScalar
ntcCtrlPlaneMasterIp=_NtcCtrlPlaneMasterIp_Object((1,3,6,1,4,1,5835,5,2,4300,1,3),_NtcCtrlPlaneMasterIp_Type())
ntcCtrlPlaneMasterIp.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcCtrlPlaneMasterIp.setStatus(_A)
_NtcCtrlPlaneAlarm_ObjectIdentity=ObjectIdentity
ntcCtrlPlaneAlarm=_NtcCtrlPlaneAlarm_ObjectIdentity((1,3,6,1,4,1,5835,5,2,4300,1,4))
if mibBuilder.loadTexts:ntcCtrlPlaneAlarm.setStatus(_A)
_NtcCtrlPlaneAlmNoMaster_Type=NtcAlarmState
_NtcCtrlPlaneAlmNoMaster_Object=MibScalar
ntcCtrlPlaneAlmNoMaster=_NtcCtrlPlaneAlmNoMaster_Object((1,3,6,1,4,1,5835,5,2,4300,1,4,1),_NtcCtrlPlaneAlmNoMaster_Type())
ntcCtrlPlaneAlmNoMaster.setMaxAccess('read-only')
if mibBuilder.loadTexts:ntcCtrlPlaneAlmNoMaster.setStatus(_A)
_NtcCtrlPlaneConformance_ObjectIdentity=ObjectIdentity
ntcCtrlPlaneConformance=_NtcCtrlPlaneConformance_ObjectIdentity((1,3,6,1,4,1,5835,5,2,4300,2))
if mibBuilder.loadTexts:ntcCtrlPlaneConformance.setStatus(_A)
_NtcCtrlPlaneConfCompliance_ObjectIdentity=ObjectIdentity
ntcCtrlPlaneConfCompliance=_NtcCtrlPlaneConfCompliance_ObjectIdentity((1,3,6,1,4,1,5835,5,2,4300,2,1))
if mibBuilder.loadTexts:ntcCtrlPlaneConfCompliance.setStatus(_A)
_NtcCtrlPlaneConfGroup_ObjectIdentity=ObjectIdentity
ntcCtrlPlaneConfGroup=_NtcCtrlPlaneConfGroup_ObjectIdentity((1,3,6,1,4,1,5835,5,2,4300,2,2))
if mibBuilder.loadTexts:ntcCtrlPlaneConfGroup.setStatus(_A)
ntcCtrlPlaneConfGrpV1Standard=ObjectGroup((1,3,6,1,4,1,5835,5,2,4300,2,2,1))
ntcCtrlPlaneConfGrpV1Standard.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U)))
if mibBuilder.loadTexts:ntcCtrlPlaneConfGrpV1Standard.setStatus(_A)
ntcCtrlPlaneConfCompV1Standard=ModuleCompliance((1,3,6,1,4,1,5835,5,2,4300,2,1,1))
ntcCtrlPlaneConfCompV1Standard.setObjects((_B,_V))
if mibBuilder.loadTexts:ntcCtrlPlaneConfCompV1Standard.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ntcControlPlane':ntcControlPlane,'ntcCtrlPlaneObjects':ntcCtrlPlaneObjects,_J:ntcCtrlPlaneEnable,'ntcCtrlPlaneCfg':ntcCtrlPlaneCfg,_K:ntcCtrlPlaneCfgNomS2ModCod,_L:ntcCtrlPlaneCfgNomS2EModCod,_M:ntcCtrlPlaneCfgFrmTyp,_N:ntcCtrlPlaneCfgIsi,_O:ntcCtrlPlaneCfgLabel,_P:ntcCtrlPlaneCfgCir,_Q:ntcCtrlPlaneCfgPir,_R:ntcCtrlPlaneCfgPrio,_S:ntcCtrlPlaneCfgMaxQTime,_T:ntcCtrlPlaneMasterIp,'ntcCtrlPlaneAlarm':ntcCtrlPlaneAlarm,_U:ntcCtrlPlaneAlmNoMaster,'ntcCtrlPlaneConformance':ntcCtrlPlaneConformance,'ntcCtrlPlaneConfCompliance':ntcCtrlPlaneConfCompliance,'ntcCtrlPlaneConfCompV1Standard':ntcCtrlPlaneConfCompV1Standard,'ntcCtrlPlaneConfGroup':ntcCtrlPlaneConfGroup,_V:ntcCtrlPlaneConfGrpV1Standard})