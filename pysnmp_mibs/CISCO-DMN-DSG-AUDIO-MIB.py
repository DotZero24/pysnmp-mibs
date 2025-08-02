_H='audioStatusSelKey'
_G='audioSelKey'
_F='CISCO-DMN-DSG-AUDIO-MIB'
_E='DisplayString'
_D='read-write'
_C='read-only'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoDSGUtilities,=mibBuilder.importSymbols('CISCO-DMN-DSG-ROOT-MIB','ciscoDSGUtilities')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','TextualConvention')
ciscoDSGAudio=ModuleIdentity((1,3,6,1,4,1,1429,2,2,5,15))
if mibBuilder.loadTexts:ciscoDSGAudio.setRevisions(('2013-07-10 12:20','2012-03-07 05:00','2010-08-30 05:00','2010-05-24 06:30','2010-05-21 16:45','2010-04-12 05:00','2010-03-22 05:00','2010-02-12 15:00','2009-12-07 12:00'))
_AudioCtrlTable_Object=MibTable
audioCtrlTable=_AudioCtrlTable_Object((1,3,6,1,4,1,1429,2,2,5,15,1))
if mibBuilder.loadTexts:audioCtrlTable.setStatus(_A)
_AudioCtrlEntry_Object=MibTableRow
audioCtrlEntry=_AudioCtrlEntry_Object((1,3,6,1,4,1,1429,2,2,5,15,1,1))
audioCtrlEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:audioCtrlEntry.setStatus(_A)
class _AudioSelKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_AudioSelKey_Type.__name__=_B
_AudioSelKey_Object=MibTableColumn
audioSelKey=_AudioSelKey_Object((1,3,6,1,4,1,1429,2,2,5,15,1,1,1),_AudioSelKey_Type())
audioSelKey.setMaxAccess(_C)
if mibBuilder.loadTexts:audioSelKey.setStatus(_A)
class _AudioMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('stereo',1),('mixed',2),('lMono',3),('rMono',4)))
_AudioMode_Type.__name__=_B
_AudioMode_Object=MibTableColumn
audioMode=_AudioMode_Object((1,3,6,1,4,1,1429,2,2,5,15,1,1,2),_AudioMode_Type())
audioMode.setMaxAccess(_D)
if mibBuilder.loadTexts:audioMode.setStatus(_A)
class _AudioDolbyDigitalComp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('rfMode',1),('lineMode',2),('custom1',3),('custom0',4)))
_AudioDolbyDigitalComp_Type.__name__=_B
_AudioDolbyDigitalComp_Object=MibTableColumn
audioDolbyDigitalComp=_AudioDolbyDigitalComp_Object((1,3,6,1,4,1,1429,2,2,5,15,1,1,3),_AudioDolbyDigitalComp_Type())
audioDolbyDigitalComp.setMaxAccess(_D)
if mibBuilder.loadTexts:audioDolbyDigitalComp.setStatus(_A)
class _AudioConsumerVolLeft_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,60))
_AudioConsumerVolLeft_Type.__name__=_B
_AudioConsumerVolLeft_Object=MibTableColumn
audioConsumerVolLeft=_AudioConsumerVolLeft_Object((1,3,6,1,4,1,1429,2,2,5,15,1,1,4),_AudioConsumerVolLeft_Type())
audioConsumerVolLeft.setMaxAccess(_D)
if mibBuilder.loadTexts:audioConsumerVolLeft.setStatus(_A)
class _AudioConsumerVolRight_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,60))
_AudioConsumerVolRight_Type.__name__=_B
_AudioConsumerVolRight_Object=MibTableColumn
audioConsumerVolRight=_AudioConsumerVolRight_Object((1,3,6,1,4,1,1429,2,2,5,15,1,1,5),_AudioConsumerVolRight_Type())
audioConsumerVolRight.setMaxAccess(_D)
if mibBuilder.loadTexts:audioConsumerVolRight.setStatus(_A)
class _AudioProfAttenuationLeft_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_AudioProfAttenuationLeft_Type.__name__=_B
_AudioProfAttenuationLeft_Object=MibTableColumn
audioProfAttenuationLeft=_AudioProfAttenuationLeft_Object((1,3,6,1,4,1,1429,2,2,5,15,1,1,6),_AudioProfAttenuationLeft_Type())
audioProfAttenuationLeft.setMaxAccess(_C)
if mibBuilder.loadTexts:audioProfAttenuationLeft.setStatus(_A)
class _AudioProfAttenuationRight_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_AudioProfAttenuationRight_Type.__name__=_B
_AudioProfAttenuationRight_Object=MibTableColumn
audioProfAttenuationRight=_AudioProfAttenuationRight_Object((1,3,6,1,4,1,1429,2,2,5,15,1,1,7),_AudioProfAttenuationRight_Type())
audioProfAttenuationRight.setMaxAccess(_C)
if mibBuilder.loadTexts:audioProfAttenuationRight.setStatus(_A)
class _AudioPmtSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65)));namedValues=NamedValues(*(('none',1),('aud1',2),('aud2',3),('aud3',4),('aud4',5),('aud5',6),('aud6',7),('aud7',8),('aud8',9),('aud9',10),('aud10',11),('aud11',12),('aud12',13),('aud13',14),('aud14',15),('aud15',16),('aud16',17),('aud17',18),('aud18',19),('aud19',20),('aud20',21),('aud21',22),('aud22',23),('aud23',24),('aud24',25),('aud25',26),('aud26',27),('aud27',28),('aud28',29),('aud29',30),('aud30',31),('aud31',32),('aud32',33),('aud33',34),('aud34',35),('aud35',36),('aud36',37),('aud37',38),('aud38',39),('aud39',40),('aud40',41),('aud41',42),('aud42',43),('aud43',44),('aud44',45),('aud45',46),('aud46',47),('aud47',48),('aud48',49),('aud49',50),('aud50',51),('aud51',52),('aud52',53),('aud53',54),('aud54',55),('aud55',56),('aud56',57),('aud57',58),('aud58',59),('aud59',60),('aud60',61),('aud61',62),('aud62',63),('aud63',64),('aud64',65)))
_AudioPmtSource_Type.__name__=_B
_AudioPmtSource_Object=MibTableColumn
audioPmtSource=_AudioPmtSource_Object((1,3,6,1,4,1,1429,2,2,5,15,1,1,8),_AudioPmtSource_Type())
audioPmtSource.setMaxAccess(_D)
if mibBuilder.loadTexts:audioPmtSource.setStatus(_A)
class _AudioMuted_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('no',1),('yes',2)))
_AudioMuted_Type.__name__=_B
_AudioMuted_Object=MibTableColumn
audioMuted=_AudioMuted_Object((1,3,6,1,4,1,1429,2,2,5,15,1,1,9),_AudioMuted_Type())
audioMuted.setMaxAccess(_D)
if mibBuilder.loadTexts:audioMuted.setStatus(_A)
class _AudioDigitalComp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('pcm',1),('compressed',2)))
_AudioDigitalComp_Type.__name__=_B
_AudioDigitalComp_Object=MibTableColumn
audioDigitalComp=_AudioDigitalComp_Object((1,3,6,1,4,1,1429,2,2,5,15,1,1,10),_AudioDigitalComp_Type())
audioDigitalComp.setMaxAccess(_D)
if mibBuilder.loadTexts:audioDigitalComp.setStatus(_A)
class _AudioDolbyDigitalPlusMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('transcoding',1),('passthrough',2)))
_AudioDolbyDigitalPlusMode_Type.__name__=_B
_AudioDolbyDigitalPlusMode_Object=MibTableColumn
audioDolbyDigitalPlusMode=_AudioDolbyDigitalPlusMode_Object((1,3,6,1,4,1,1429,2,2,5,15,1,1,11),_AudioDolbyDigitalPlusMode_Type())
audioDolbyDigitalPlusMode.setMaxAccess(_D)
if mibBuilder.loadTexts:audioDolbyDigitalPlusMode.setStatus(_A)
class _AudioLangMenu_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('languageList',1),('languageEntry',2),('pmtOrder',3)))
_AudioLangMenu_Type.__name__=_B
_AudioLangMenu_Object=MibTableColumn
audioLangMenu=_AudioLangMenu_Object((1,3,6,1,4,1,1429,2,2,5,15,1,1,12),_AudioLangMenu_Type())
audioLangMenu.setMaxAccess(_D)
if mibBuilder.loadTexts:audioLangMenu.setStatus(_A)
class _AudioLangList_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43)));namedValues=NamedValues(*(('ara',1),('btk',2),('ben',3),('bul',4),('chi',5),('cze',6),('dan',7),('dut',8),('eng',9),('fin',10),('fre',11),('ger',12),('gre',13),('heb',14),('hin',15),('hun',16),('ice',17),('ind',18),('ita',19),('jpn',20),('kor',21),('may',22),('mul',23),('nor',24),('per',25),('pol',26),('por',27),('rum',28),('rus',29),('san',30),('scc',31),('sin',32),('slo',33),('slv',34),('som',35),('spa',36),('swe',37),('tai',38),('tam',39),('tha',40),('tur',41),('ukr',42),('vie',43)))
_AudioLangList_Type.__name__=_B
_AudioLangList_Object=MibTableColumn
audioLangList=_AudioLangList_Object((1,3,6,1,4,1,1429,2,2,5,15,1,1,13),_AudioLangList_Type())
audioLangList.setMaxAccess(_D)
if mibBuilder.loadTexts:audioLangList.setStatus(_A)
class _AudioManualEntry_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,3))
_AudioManualEntry_Type.__name__=_E
_AudioManualEntry_Object=MibTableColumn
audioManualEntry=_AudioManualEntry_Object((1,3,6,1,4,1,1429,2,2,5,15,1,1,14),_AudioManualEntry_Type())
audioManualEntry.setMaxAccess(_D)
if mibBuilder.loadTexts:audioManualEntry.setStatus(_A)
_AudioStatusTable_Object=MibTable
audioStatusTable=_AudioStatusTable_Object((1,3,6,1,4,1,1429,2,2,5,15,2))
if mibBuilder.loadTexts:audioStatusTable.setStatus(_A)
_AudioStatusEntry_Object=MibTableRow
audioStatusEntry=_AudioStatusEntry_Object((1,3,6,1,4,1,1429,2,2,5,15,2,1))
audioStatusEntry.setIndexNames((0,_F,_H))
if mibBuilder.loadTexts:audioStatusEntry.setStatus(_A)
class _AudioStatusSelKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_AudioStatusSelKey_Type.__name__=_B
_AudioStatusSelKey_Object=MibTableColumn
audioStatusSelKey=_AudioStatusSelKey_Object((1,3,6,1,4,1,1429,2,2,5,15,2,1,1),_AudioStatusSelKey_Type())
audioStatusSelKey.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:audioStatusSelKey.setStatus(_A)
class _AudioStatusFormat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14)));namedValues=NamedValues(*(('none',1),('sine',2),('pink',3),('beep',4),('mpeg1L1',5),('mpeg1L2',6),('mpeg2L1',7),('mpeg2L2',8),('dolbyDigital',9),('loasAAC',10),('adtsAAC',11),('dolbyDigitalPlus',12),('adtsHEAAC',13),('loasHEAAC',14)))
_AudioStatusFormat_Type.__name__=_B
_AudioStatusFormat_Object=MibTableColumn
audioStatusFormat=_AudioStatusFormat_Object((1,3,6,1,4,1,1429,2,2,5,15,2,1,2),_AudioStatusFormat_Type())
audioStatusFormat.setMaxAccess(_C)
if mibBuilder.loadTexts:audioStatusFormat.setStatus(_A)
class _AudioStatusBitRate_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_AudioStatusBitRate_Type.__name__=_E
_AudioStatusBitRate_Object=MibTableColumn
audioStatusBitRate=_AudioStatusBitRate_Object((1,3,6,1,4,1,1429,2,2,5,15,2,1,3),_AudioStatusBitRate_Type())
audioStatusBitRate.setMaxAccess(_C)
if mibBuilder.loadTexts:audioStatusBitRate.setStatus(_A)
class _AudioStatusBufferLevel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_AudioStatusBufferLevel_Type.__name__=_E
_AudioStatusBufferLevel_Object=MibTableColumn
audioStatusBufferLevel=_AudioStatusBufferLevel_Object((1,3,6,1,4,1,1429,2,2,5,15,2,1,4),_AudioStatusBufferLevel_Type())
audioStatusBufferLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:audioStatusBufferLevel.setStatus(_A)
class _AudioStatusSFR_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_AudioStatusSFR_Type.__name__=_E
_AudioStatusSFR_Object=MibTableColumn
audioStatusSFR=_AudioStatusSFR_Object((1,3,6,1,4,1,1429,2,2,5,15,2,1,5),_AudioStatusSFR_Type())
audioStatusSFR.setMaxAccess(_C)
if mibBuilder.loadTexts:audioStatusSFR.setStatus(_A)
class _AudioStatusMuted_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('no',1),('yes',2)))
_AudioStatusMuted_Type.__name__=_B
_AudioStatusMuted_Object=MibTableColumn
audioStatusMuted=_AudioStatusMuted_Object((1,3,6,1,4,1,1429,2,2,5,15,2,1,6),_AudioStatusMuted_Type())
audioStatusMuted.setMaxAccess(_C)
if mibBuilder.loadTexts:audioStatusMuted.setStatus(_A)
class _AudioStatusLanguage_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_AudioStatusLanguage_Type.__name__=_E
_AudioStatusLanguage_Object=MibTableColumn
audioStatusLanguage=_AudioStatusLanguage_Object((1,3,6,1,4,1,1429,2,2,5,15,2,1,7),_AudioStatusLanguage_Type())
audioStatusLanguage.setMaxAccess(_C)
if mibBuilder.loadTexts:audioStatusLanguage.setStatus(_A)
class _AudioStatusDDPMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('off',1),('ddp',2)))
_AudioStatusDDPMode_Type.__name__=_B
_AudioStatusDDPMode_Object=MibTableColumn
audioStatusDDPMode=_AudioStatusDDPMode_Object((1,3,6,1,4,1,1429,2,2,5,15,2,1,8),_AudioStatusDDPMode_Type())
audioStatusDDPMode.setMaxAccess(_C)
if mibBuilder.loadTexts:audioStatusDDPMode.setStatus(_A)
class _AudioStatusDualMonoMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('off',1),('dualMono',2)))
_AudioStatusDualMonoMode_Type.__name__=_B
_AudioStatusDualMonoMode_Object=MibTableColumn
audioStatusDualMonoMode=_AudioStatusDualMonoMode_Object((1,3,6,1,4,1,1429,2,2,5,15,2,1,9),_AudioStatusDualMonoMode_Type())
audioStatusDualMonoMode.setMaxAccess(_C)
if mibBuilder.loadTexts:audioStatusDualMonoMode.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'ciscoDSGAudio':ciscoDSGAudio,'audioCtrlTable':audioCtrlTable,'audioCtrlEntry':audioCtrlEntry,_G:audioSelKey,'audioMode':audioMode,'audioDolbyDigitalComp':audioDolbyDigitalComp,'audioConsumerVolLeft':audioConsumerVolLeft,'audioConsumerVolRight':audioConsumerVolRight,'audioProfAttenuationLeft':audioProfAttenuationLeft,'audioProfAttenuationRight':audioProfAttenuationRight,'audioPmtSource':audioPmtSource,'audioMuted':audioMuted,'audioDigitalComp':audioDigitalComp,'audioDolbyDigitalPlusMode':audioDolbyDigitalPlusMode,'audioLangMenu':audioLangMenu,'audioLangList':audioLangList,'audioManualEntry':audioManualEntry,'audioStatusTable':audioStatusTable,'audioStatusEntry':audioStatusEntry,_H:audioStatusSelKey,'audioStatusFormat':audioStatusFormat,'audioStatusBitRate':audioStatusBitRate,'audioStatusBufferLevel':audioStatusBufferLevel,'audioStatusSFR':audioStatusSFR,'audioStatusMuted':audioStatusMuted,'audioStatusLanguage':audioStatusLanguage,'audioStatusDDPMode':audioStatusDDPMode,'audioStatusDualMonoMode':audioStatusDualMonoMode})