_D='DisplayString'
_C='current'
_B='read-write'
_A='Integer32'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoDSGUtilities,=mibBuilder.importSymbols('CISCO-DMN-DSG-ROOT-MIB','ciscoDSGUtilities')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_A,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention')
ciscoDSGSubtitle=ModuleIdentity((1,3,6,1,4,1,1429,2,2,5,16))
if mibBuilder.loadTexts:ciscoDSGSubtitle.setRevisions(('2013-07-10 12:20','2010-08-30 11:00','2009-12-07 12:00'))
class _SubtitlesOPMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('off',1),('on',2),('imiText',3),('dvb',4)))
_SubtitlesOPMode_Type.__name__=_A
_SubtitlesOPMode_Object=MibScalar
subtitlesOPMode=_SubtitlesOPMode_Object((1,3,6,1,4,1,1429,2,2,5,16,1),_SubtitlesOPMode_Type())
subtitlesOPMode.setMaxAccess(_B)
if mibBuilder.loadTexts:subtitlesOPMode.setStatus(_C)
class _SubtitlesLangMenu_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('languageList',1),('languageEntry',2),('pmtOrder',3)))
_SubtitlesLangMenu_Type.__name__=_A
_SubtitlesLangMenu_Object=MibScalar
subtitlesLangMenu=_SubtitlesLangMenu_Object((1,3,6,1,4,1,1429,2,2,5,16,2),_SubtitlesLangMenu_Type())
subtitlesLangMenu.setMaxAccess(_B)
if mibBuilder.loadTexts:subtitlesLangMenu.setStatus(_C)
class _SubtitlesLangList_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43)));namedValues=NamedValues(*(('ara',1),('btk',2),('ben',3),('bul',4),('chi',5),('cze',6),('dan',7),('dut',8),('eng',9),('fin',10),('fre',11),('ger',12),('gre',13),('heb',14),('hin',15),('hun',16),('ice',17),('ind',18),('ita',19),('jpn',20),('kor',21),('may',22),('mul',23),('nor',24),('per',25),('pol',26),('por',27),('rum',28),('rus',29),('san',30),('scc',31),('sin',32),('slo',33),('slv',34),('som',35),('spa',36),('swe',37),('tai',38),('tam',39),('tha',40),('tur',41),('ukr',42),('vie',43)))
_SubtitlesLangList_Type.__name__=_A
_SubtitlesLangList_Object=MibScalar
subtitlesLangList=_SubtitlesLangList_Object((1,3,6,1,4,1,1429,2,2,5,16,3),_SubtitlesLangList_Type())
subtitlesLangList.setMaxAccess(_B)
if mibBuilder.loadTexts:subtitlesLangList.setStatus(_C)
class _SubtitlesPMTOrder_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('first',1),('second',2),('third',3),('fourth',4),('fifth',5),('sixth',6),('seventh',7),('eighth',8)))
_SubtitlesPMTOrder_Type.__name__=_A
_SubtitlesPMTOrder_Object=MibScalar
subtitlesPMTOrder=_SubtitlesPMTOrder_Object((1,3,6,1,4,1,1429,2,2,5,16,4),_SubtitlesPMTOrder_Type())
subtitlesPMTOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:subtitlesPMTOrder.setStatus(_C)
class _SubtitlesManualEntry_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,3))
_SubtitlesManualEntry_Type.__name__=_D
_SubtitlesManualEntry_Object=MibScalar
subtitlesManualEntry=_SubtitlesManualEntry_Object((1,3,6,1,4,1,1429,2,2,5,16,5),_SubtitlesManualEntry_Type())
subtitlesManualEntry.setMaxAccess(_B)
if mibBuilder.loadTexts:subtitlesManualEntry.setStatus(_C)
class _SubtitlesIMITextPos_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('standard',1),('extended',2)))
_SubtitlesIMITextPos_Type.__name__=_A
_SubtitlesIMITextPos_Object=MibScalar
subtitlesIMITextPos=_SubtitlesIMITextPos_Object((1,3,6,1,4,1,1429,2,2,5,16,6),_SubtitlesIMITextPos_Type())
subtitlesIMITextPos.setMaxAccess(_B)
if mibBuilder.loadTexts:subtitlesIMITextPos.setStatus(_C)
class _SubtitlesForeGround_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('auto',1),('yellow',2),('white',3)))
_SubtitlesForeGround_Type.__name__=_A
_SubtitlesForeGround_Object=MibScalar
subtitlesForeGround=_SubtitlesForeGround_Object((1,3,6,1,4,1,1429,2,2,5,16,7),_SubtitlesForeGround_Type())
subtitlesForeGround.setMaxAccess(_B)
if mibBuilder.loadTexts:subtitlesForeGround.setStatus(_C)
class _SubtitlesBackGround_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('none',1),('auto',2),('shadow',3),('opaque',4),('semi',5)))
_SubtitlesBackGround_Type.__name__=_A
_SubtitlesBackGround_Object=MibScalar
subtitlesBackGround=_SubtitlesBackGround_Object((1,3,6,1,4,1,1429,2,2,5,16,8),_SubtitlesBackGround_Type())
subtitlesBackGround.setMaxAccess(_B)
if mibBuilder.loadTexts:subtitlesBackGround.setStatus(_C)
mibBuilder.exportSymbols('CISCO-DMN-DSG-SUBTITLES-MIB',**{'ciscoDSGSubtitle':ciscoDSGSubtitle,'subtitlesOPMode':subtitlesOPMode,'subtitlesLangMenu':subtitlesLangMenu,'subtitlesLangList':subtitlesLangList,'subtitlesPMTOrder':subtitlesPMTOrder,'subtitlesManualEntry':subtitlesManualEntry,'subtitlesIMITextPos':subtitlesIMITextPos,'subtitlesForeGround':subtitlesForeGround,'subtitlesBackGround':subtitlesBackGround})