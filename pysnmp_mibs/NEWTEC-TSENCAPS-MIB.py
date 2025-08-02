_h='ntcTsEncConfGrpV1Standard'
_g='ntcTsEncDefEncProt'
_f='ntcTsEncChannelsAccessVlan'
_e='ntcTsEncChannelsTermName'
_d='ntcTsEncChannelsLabel'
_c='ntcTsEncChannelsOutInstanceName'
_b='ntcTsEncChannelsOutTypeName'
_a='ntcTsEncChannelsEnable'
_Z='ntcTsEncChannelsRowStatus'
_Y='ntcTsEncPidsAcmEnable'
_X='ntcTsEncPidsNomS2ExtModcod'
_W='ntcTsEncPidsNomS2Modcod'
_V='ntcTsEncPidsProtocol'
_U='ntcTsEncPidsOutInstanceName'
_T='ntcTsEncPidsOutTypeName'
_S='ntcTsEncPidsPid'
_R='ntcTsEncPidsEnable'
_Q='ntcTsEncPidsRowStatus'
_P='ntcTsEncIsisFrmTp'
_O='ntcTsEncIsisIsi'
_N='ntcTsEncIsisEnable'
_M='ntcTsEncIsisRowStatus'
_L='ntcTsEncChannelsName'
_K='unspecified'
_J='ntcTsEncPidsName'
_I='ntcTsEncIsisName'
_H='Unsigned32'
_G='not-accessible'
_F='OctetString'
_E='DisplayString'
_D='Integer32'
_C='read-create'
_B='NEWTEC-TSENCAPS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ntcFunction,=mibBuilder.importSymbols('NEWTEC-MAIN-MIB','ntcFunction')
NtcEnable,=mibBuilder.importSymbols('NEWTEC-TC-MIB','NtcEnable')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_H,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','RowStatus','TextualConvention')
ntcTsEncaps=ModuleIdentity((1,3,6,1,4,1,5835,5,2,5800))
if mibBuilder.loadTexts:ntcTsEncaps.setRevisions(('2015-09-25 11:00','2015-04-13 07:00','2015-01-30 08:00','2014-07-15 08:00','2014-02-03 12:00'))
_NtcTsEncObjects_ObjectIdentity=ObjectIdentity
ntcTsEncObjects=_NtcTsEncObjects_ObjectIdentity((1,3,6,1,4,1,5835,5,2,5800,1))
if mibBuilder.loadTexts:ntcTsEncObjects.setStatus(_A)
_NtcTsEncIsisTable_Object=MibTable
ntcTsEncIsisTable=_NtcTsEncIsisTable_Object((1,3,6,1,4,1,5835,5,2,5800,1,1))
if mibBuilder.loadTexts:ntcTsEncIsisTable.setStatus(_A)
_NtcTsEncIsisEntry_Object=MibTableRow
ntcTsEncIsisEntry=_NtcTsEncIsisEntry_Object((1,3,6,1,4,1,5835,5,2,5800,1,1,1))
ntcTsEncIsisEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:ntcTsEncIsisEntry.setStatus(_A)
class _NtcTsEncIsisName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,100))
_NtcTsEncIsisName_Type.__name__=_E
_NtcTsEncIsisName_Object=MibTableColumn
ntcTsEncIsisName=_NtcTsEncIsisName_Object((1,3,6,1,4,1,5835,5,2,5800,1,1,1,1),_NtcTsEncIsisName_Type())
ntcTsEncIsisName.setMaxAccess(_G)
if mibBuilder.loadTexts:ntcTsEncIsisName.setStatus(_A)
_NtcTsEncIsisRowStatus_Type=RowStatus
_NtcTsEncIsisRowStatus_Object=MibTableColumn
ntcTsEncIsisRowStatus=_NtcTsEncIsisRowStatus_Object((1,3,6,1,4,1,5835,5,2,5800,1,1,1,2),_NtcTsEncIsisRowStatus_Type())
ntcTsEncIsisRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsEncIsisRowStatus.setStatus(_A)
_NtcTsEncIsisEnable_Type=NtcEnable
_NtcTsEncIsisEnable_Object=MibTableColumn
ntcTsEncIsisEnable=_NtcTsEncIsisEnable_Object((1,3,6,1,4,1,5835,5,2,5800,1,1,1,3),_NtcTsEncIsisEnable_Type())
ntcTsEncIsisEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsEncIsisEnable.setStatus(_A)
_NtcTsEncIsisIsi_Type=Unsigned32
_NtcTsEncIsisIsi_Object=MibTableColumn
ntcTsEncIsisIsi=_NtcTsEncIsisIsi_Object((1,3,6,1,4,1,5835,5,2,5800,1,1,1,4),_NtcTsEncIsisIsi_Type())
ntcTsEncIsisIsi.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsEncIsisIsi.setStatus(_A)
class _NtcTsEncIsisFrmTp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('short',0),('normal',1)))
_NtcTsEncIsisFrmTp_Type.__name__=_D
_NtcTsEncIsisFrmTp_Object=MibTableColumn
ntcTsEncIsisFrmTp=_NtcTsEncIsisFrmTp_Object((1,3,6,1,4,1,5835,5,2,5800,1,1,1,5),_NtcTsEncIsisFrmTp_Type())
ntcTsEncIsisFrmTp.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsEncIsisFrmTp.setStatus(_A)
_NtcTsEncPidsTable_Object=MibTable
ntcTsEncPidsTable=_NtcTsEncPidsTable_Object((1,3,6,1,4,1,5835,5,2,5800,1,2))
if mibBuilder.loadTexts:ntcTsEncPidsTable.setStatus(_A)
_NtcTsEncPidsEntry_Object=MibTableRow
ntcTsEncPidsEntry=_NtcTsEncPidsEntry_Object((1,3,6,1,4,1,5835,5,2,5800,1,2,1))
ntcTsEncPidsEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:ntcTsEncPidsEntry.setStatus(_A)
class _NtcTsEncPidsName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,100))
_NtcTsEncPidsName_Type.__name__=_E
_NtcTsEncPidsName_Object=MibTableColumn
ntcTsEncPidsName=_NtcTsEncPidsName_Object((1,3,6,1,4,1,5835,5,2,5800,1,2,1,1),_NtcTsEncPidsName_Type())
ntcTsEncPidsName.setMaxAccess(_G)
if mibBuilder.loadTexts:ntcTsEncPidsName.setStatus(_A)
_NtcTsEncPidsRowStatus_Type=RowStatus
_NtcTsEncPidsRowStatus_Object=MibTableColumn
ntcTsEncPidsRowStatus=_NtcTsEncPidsRowStatus_Object((1,3,6,1,4,1,5835,5,2,5800,1,2,1,2),_NtcTsEncPidsRowStatus_Type())
ntcTsEncPidsRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsEncPidsRowStatus.setStatus(_A)
_NtcTsEncPidsEnable_Type=NtcEnable
_NtcTsEncPidsEnable_Object=MibTableColumn
ntcTsEncPidsEnable=_NtcTsEncPidsEnable_Object((1,3,6,1,4,1,5835,5,2,5800,1,2,1,3),_NtcTsEncPidsEnable_Type())
ntcTsEncPidsEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsEncPidsEnable.setStatus(_A)
_NtcTsEncPidsPid_Type=Unsigned32
_NtcTsEncPidsPid_Object=MibTableColumn
ntcTsEncPidsPid=_NtcTsEncPidsPid_Object((1,3,6,1,4,1,5835,5,2,5800,1,2,1,4),_NtcTsEncPidsPid_Type())
ntcTsEncPidsPid.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsEncPidsPid.setStatus(_A)
class _NtcTsEncPidsOutTypeName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_NtcTsEncPidsOutTypeName_Type.__name__=_F
_NtcTsEncPidsOutTypeName_Object=MibTableColumn
ntcTsEncPidsOutTypeName=_NtcTsEncPidsOutTypeName_Object((1,3,6,1,4,1,5835,5,2,5800,1,2,1,5),_NtcTsEncPidsOutTypeName_Type())
ntcTsEncPidsOutTypeName.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsEncPidsOutTypeName.setStatus(_A)
class _NtcTsEncPidsOutInstanceName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_NtcTsEncPidsOutInstanceName_Type.__name__=_F
_NtcTsEncPidsOutInstanceName_Object=MibTableColumn
ntcTsEncPidsOutInstanceName=_NtcTsEncPidsOutInstanceName_Object((1,3,6,1,4,1,5835,5,2,5800,1,2,1,6),_NtcTsEncPidsOutInstanceName_Type())
ntcTsEncPidsOutInstanceName.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsEncPidsOutInstanceName.setStatus(_A)
class _NtcTsEncPidsProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('default',0),('mpe',1),('ule',2)))
_NtcTsEncPidsProtocol_Type.__name__=_D
_NtcTsEncPidsProtocol_Object=MibTableColumn
ntcTsEncPidsProtocol=_NtcTsEncPidsProtocol_Object((1,3,6,1,4,1,5835,5,2,5800,1,2,1,7),_NtcTsEncPidsProtocol_Type())
ntcTsEncPidsProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsEncPidsProtocol.setStatus(_A)
class _NtcTsEncPidsNomS2Modcod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80)));namedValues=NamedValues(*((_K,0),('qpsk14',1),('qpsk13',2),('qpsk25',3),('qpsk12',4),('qpsk35',5),('qpsk23',6),('qpsk34',7),('qpsk45',8),('qpsk56',9),('qpsk89',10),('qpsk910',11),('e8psk35',12),('e8psk23',13),('e8psk34',14),('e8psk56',15),('e8psk89',16),('e8psk910',17),('e16apsk23',18),('e16apsk34',19),('e16apsk45',20),('e16apsk56',21),('e16apsk89',22),('e16apsk910',23),('e32apsk34',24),('e32apsk45',25),('e32apsk56',26),('e32apsk89',27),('e32apsk910',28),('qpsk1345',29),('qpsk920',30),('qpsk1120',31),('e8apsk59l',32),('e8apsk2645l',33),('e8psk2336',34),('e8psk2536',35),('e8psk1318',36),('e16apsk12l',37),('e16apsk815l',38),('e16apsk59l',39),('e16apsk2645',40),('e16apsk35',41),('e16apsk35l',42),('e16apsk2845',43),('e16apsk2336',44),('e16apsk23l',45),('e16apsk2536',46),('e16apsk1318',47),('e16apsk79',48),('e16apsk7790',49),('e32apsk23l',50),('e32apsk3245',51),('e32apsk1115',52),('e32apsk79',53),('e64apsk3245l',54),('e64apsk1115',55),('e64apsk79',56),('e64apsk45',57),('e64apsk56',58),('e128apsk34',59),('e128apsk79',60),('e256apsk2945l',61),('e256apsk23l',62),('e256apsk3145l',63),('e256apsk3245',64),('e256apsk1115l',65),('e256apsk34',66),('qpsk1145',67),('qpsk415',68),('qpsk1445',69),('qpsk715',70),('qpsk815',71),('qpsk3245',72),('e8psk715',73),('e8psk815',74),('e8psk2645',75),('e8psk3245',76),('e16apsk715',77),('e16apsk815',78),('e16apsk3245',79),('e32apsk23',80)))
_NtcTsEncPidsNomS2Modcod_Type.__name__=_D
_NtcTsEncPidsNomS2Modcod_Object=MibTableColumn
ntcTsEncPidsNomS2Modcod=_NtcTsEncPidsNomS2Modcod_Object((1,3,6,1,4,1,5835,5,2,5800,1,2,1,8),_NtcTsEncPidsNomS2Modcod_Type())
ntcTsEncPidsNomS2Modcod.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsEncPidsNomS2Modcod.setStatus(_A)
class _NtcTsEncPidsNomS2ExtModcod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,193,194,195,196,197,198,199,200,201,202,203,204,205,206,207,208,209,210,211,212,213,214,215)));namedValues=NamedValues(*((_K,0),('qpsk45180',129),('qpsk60180',130),('qpsk72180',131),('qpsk80180',132),('qpsk90180',133),('qpsk100180',134),('qpsk108180',135),('qpsk114180',136),('qpsk120180',137),('qpsk126180',138),('qpsk135180',139),('qpsk144180',140),('qpsk150180',141),('qpsk160180',142),('qpsk162180',143),('e8psk80180',144),('e8psk90180',145),('e8psk100180',146),('e8psk108180',147),('e8psk114180',148),('e8psk120180',149),('e8psk126180',150),('e8psk135180',151),('e8psk144180',152),('e8psk150180',153),('e16apsk80180',154),('e16apsk90180',155),('e16apsk100180',156),('e16apsk108180',157),('e16apsk114180',158),('e16apsk120180',159),('e16apsk126180',160),('e16apsk135180',161),('e16apsk144180',162),('e16apsk150180',163),('e16apsk160180',164),('e16apsk162180',165),('e32apsk100180',166),('e32apsk108180',167),('e32apsk114180',168),('e32apsk120180',169),('e32apsk126180',170),('e32apsk135180',171),('e32apsk144180',172),('e32apsk150180',173),('e32apsk160180',174),('e32apsk162180',175),('e64apsk90180',176),('e64apsk100180',177),('e64apsk108180',178),('e64apsk114180',179),('e64apsk120180',180),('e64apsk126180',181),('e64apsk135180',182),('e64apsk144180',183),('e64apsk150180',184),('e64apsk160180',185),('e64apsk162180',186),('e8pskl80180',187),('e8pskl90180',188),('e8pskl100180',189),('e8pskl108180',190),('e8pskl114180',191),('e8pskl120180',192),('e16apskl80180',193),('e16apskl90180',194),('e16apskl100180',195),('e16apskl108180',196),('e16apskl114180',197),('e16apskl120180',198),('e16apskl126180',199),('e16apskl135180',200),('e16apskl144180',201),('e16apskl150180',202),('e16apskl160180',203),('e16apskl162180',204),('e64apskl90180',205),('e64apskl100180',206),('e64apskl108180',207),('e64apskl114180',208),('e64apskl120180',209),('e64apskl126180',210),('e64apskl135180',211),('e64apskl144180',212),('e64apskl150180',213),('e64apskl160180',214),('e64apskl162180',215)))
_NtcTsEncPidsNomS2ExtModcod_Type.__name__=_D
_NtcTsEncPidsNomS2ExtModcod_Object=MibTableColumn
ntcTsEncPidsNomS2ExtModcod=_NtcTsEncPidsNomS2ExtModcod_Object((1,3,6,1,4,1,5835,5,2,5800,1,2,1,9),_NtcTsEncPidsNomS2ExtModcod_Type())
ntcTsEncPidsNomS2ExtModcod.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsEncPidsNomS2ExtModcod.setStatus(_A)
_NtcTsEncPidsAcmEnable_Type=NtcEnable
_NtcTsEncPidsAcmEnable_Object=MibTableColumn
ntcTsEncPidsAcmEnable=_NtcTsEncPidsAcmEnable_Object((1,3,6,1,4,1,5835,5,2,5800,1,2,1,10),_NtcTsEncPidsAcmEnable_Type())
ntcTsEncPidsAcmEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsEncPidsAcmEnable.setStatus(_A)
_NtcTsEncChannelsTable_Object=MibTable
ntcTsEncChannelsTable=_NtcTsEncChannelsTable_Object((1,3,6,1,4,1,5835,5,2,5800,1,3))
if mibBuilder.loadTexts:ntcTsEncChannelsTable.setStatus(_A)
_NtcTsEncChannelsEntry_Object=MibTableRow
ntcTsEncChannelsEntry=_NtcTsEncChannelsEntry_Object((1,3,6,1,4,1,5835,5,2,5800,1,3,1))
ntcTsEncChannelsEntry.setIndexNames((0,_B,_L))
if mibBuilder.loadTexts:ntcTsEncChannelsEntry.setStatus(_A)
class _NtcTsEncChannelsName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,100))
_NtcTsEncChannelsName_Type.__name__=_E
_NtcTsEncChannelsName_Object=MibTableColumn
ntcTsEncChannelsName=_NtcTsEncChannelsName_Object((1,3,6,1,4,1,5835,5,2,5800,1,3,1,1),_NtcTsEncChannelsName_Type())
ntcTsEncChannelsName.setMaxAccess(_G)
if mibBuilder.loadTexts:ntcTsEncChannelsName.setStatus(_A)
_NtcTsEncChannelsRowStatus_Type=RowStatus
_NtcTsEncChannelsRowStatus_Object=MibTableColumn
ntcTsEncChannelsRowStatus=_NtcTsEncChannelsRowStatus_Object((1,3,6,1,4,1,5835,5,2,5800,1,3,1,2),_NtcTsEncChannelsRowStatus_Type())
ntcTsEncChannelsRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsEncChannelsRowStatus.setStatus(_A)
_NtcTsEncChannelsEnable_Type=NtcEnable
_NtcTsEncChannelsEnable_Object=MibTableColumn
ntcTsEncChannelsEnable=_NtcTsEncChannelsEnable_Object((1,3,6,1,4,1,5835,5,2,5800,1,3,1,3),_NtcTsEncChannelsEnable_Type())
ntcTsEncChannelsEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsEncChannelsEnable.setStatus(_A)
class _NtcTsEncChannelsOutTypeName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_NtcTsEncChannelsOutTypeName_Type.__name__=_F
_NtcTsEncChannelsOutTypeName_Object=MibTableColumn
ntcTsEncChannelsOutTypeName=_NtcTsEncChannelsOutTypeName_Object((1,3,6,1,4,1,5835,5,2,5800,1,3,1,4),_NtcTsEncChannelsOutTypeName_Type())
ntcTsEncChannelsOutTypeName.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsEncChannelsOutTypeName.setStatus(_A)
class _NtcTsEncChannelsOutInstanceName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_NtcTsEncChannelsOutInstanceName_Type.__name__=_F
_NtcTsEncChannelsOutInstanceName_Object=MibTableColumn
ntcTsEncChannelsOutInstanceName=_NtcTsEncChannelsOutInstanceName_Object((1,3,6,1,4,1,5835,5,2,5800,1,3,1,5),_NtcTsEncChannelsOutInstanceName_Type())
ntcTsEncChannelsOutInstanceName.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsEncChannelsOutInstanceName.setStatus(_A)
class _NtcTsEncChannelsLabel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_NtcTsEncChannelsLabel_Type.__name__=_E
_NtcTsEncChannelsLabel_Object=MibTableColumn
ntcTsEncChannelsLabel=_NtcTsEncChannelsLabel_Object((1,3,6,1,4,1,5835,5,2,5800,1,3,1,6),_NtcTsEncChannelsLabel_Type())
ntcTsEncChannelsLabel.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsEncChannelsLabel.setStatus(_A)
class _NtcTsEncChannelsTermName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,100))
_NtcTsEncChannelsTermName_Type.__name__=_E
_NtcTsEncChannelsTermName_Object=MibTableColumn
ntcTsEncChannelsTermName=_NtcTsEncChannelsTermName_Object((1,3,6,1,4,1,5835,5,2,5800,1,3,1,7),_NtcTsEncChannelsTermName_Type())
ntcTsEncChannelsTermName.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsEncChannelsTermName.setStatus(_A)
class _NtcTsEncChannelsAccessVlan_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_NtcTsEncChannelsAccessVlan_Type.__name__=_H
_NtcTsEncChannelsAccessVlan_Object=MibTableColumn
ntcTsEncChannelsAccessVlan=_NtcTsEncChannelsAccessVlan_Object((1,3,6,1,4,1,5835,5,2,5800,1,3,1,8),_NtcTsEncChannelsAccessVlan_Type())
ntcTsEncChannelsAccessVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcTsEncChannelsAccessVlan.setStatus(_A)
class _NtcTsEncDefEncProt_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('mpe',0),('ule',1)))
_NtcTsEncDefEncProt_Type.__name__=_D
_NtcTsEncDefEncProt_Object=MibScalar
ntcTsEncDefEncProt=_NtcTsEncDefEncProt_Object((1,3,6,1,4,1,5835,5,2,5800,1,4),_NtcTsEncDefEncProt_Type())
ntcTsEncDefEncProt.setMaxAccess('read-write')
if mibBuilder.loadTexts:ntcTsEncDefEncProt.setStatus(_A)
_NtcTsEncConformance_ObjectIdentity=ObjectIdentity
ntcTsEncConformance=_NtcTsEncConformance_ObjectIdentity((1,3,6,1,4,1,5835,5,2,5800,2))
if mibBuilder.loadTexts:ntcTsEncConformance.setStatus(_A)
_NtcTsEncConfCompliance_ObjectIdentity=ObjectIdentity
ntcTsEncConfCompliance=_NtcTsEncConfCompliance_ObjectIdentity((1,3,6,1,4,1,5835,5,2,5800,2,1))
if mibBuilder.loadTexts:ntcTsEncConfCompliance.setStatus(_A)
_NtcTsEncConfGroup_ObjectIdentity=ObjectIdentity
ntcTsEncConfGroup=_NtcTsEncConfGroup_ObjectIdentity((1,3,6,1,4,1,5835,5,2,5800,2,2))
if mibBuilder.loadTexts:ntcTsEncConfGroup.setStatus(_A)
ntcTsEncConfGrpV1Standard=ObjectGroup((1,3,6,1,4,1,5835,5,2,5800,2,2,1))
ntcTsEncConfGrpV1Standard.setObjects(*((_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g)))
if mibBuilder.loadTexts:ntcTsEncConfGrpV1Standard.setStatus(_A)
ntcTsEncConfCompV1Standard=ModuleCompliance((1,3,6,1,4,1,5835,5,2,5800,2,1,1))
ntcTsEncConfCompV1Standard.setObjects((_B,_h))
if mibBuilder.loadTexts:ntcTsEncConfCompV1Standard.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ntcTsEncaps':ntcTsEncaps,'ntcTsEncObjects':ntcTsEncObjects,'ntcTsEncIsisTable':ntcTsEncIsisTable,'ntcTsEncIsisEntry':ntcTsEncIsisEntry,_I:ntcTsEncIsisName,_M:ntcTsEncIsisRowStatus,_N:ntcTsEncIsisEnable,_O:ntcTsEncIsisIsi,_P:ntcTsEncIsisFrmTp,'ntcTsEncPidsTable':ntcTsEncPidsTable,'ntcTsEncPidsEntry':ntcTsEncPidsEntry,_J:ntcTsEncPidsName,_Q:ntcTsEncPidsRowStatus,_R:ntcTsEncPidsEnable,_S:ntcTsEncPidsPid,_T:ntcTsEncPidsOutTypeName,_U:ntcTsEncPidsOutInstanceName,_V:ntcTsEncPidsProtocol,_W:ntcTsEncPidsNomS2Modcod,_X:ntcTsEncPidsNomS2ExtModcod,_Y:ntcTsEncPidsAcmEnable,'ntcTsEncChannelsTable':ntcTsEncChannelsTable,'ntcTsEncChannelsEntry':ntcTsEncChannelsEntry,_L:ntcTsEncChannelsName,_Z:ntcTsEncChannelsRowStatus,_a:ntcTsEncChannelsEnable,_b:ntcTsEncChannelsOutTypeName,_c:ntcTsEncChannelsOutInstanceName,_d:ntcTsEncChannelsLabel,_e:ntcTsEncChannelsTermName,_f:ntcTsEncChannelsAccessVlan,_g:ntcTsEncDefEncProt,'ntcTsEncConformance':ntcTsEncConformance,'ntcTsEncConfCompliance':ntcTsEncConfCompliance,'ntcTsEncConfCompV1Standard':ntcTsEncConfCompV1Standard,'ntcTsEncConfGroup':ntcTsEncConfGroup,_h:ntcTsEncConfGrpV1Standard})