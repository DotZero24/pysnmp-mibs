_I='ignoreAfterTimeout'
_H='interactWithOperator'
_G='ignore'
_F='abortJob'
_E='notSpecified'
_D='unknown'
_C='other'
_B='not-accessible'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
samsungCommonMIB,=mibBuilder.importSymbols('SAMSUNG-COMMON-MIB','samsungCommonMIB')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
scmPrintTC=ModuleIdentity((1,3,6,1,4,1,236,11,5,11,54))
class ScmPrtAuxSheetContent(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,5,6)));namedValues=NamedValues(*((_C,1),(_D,2),(_E,3),('concise',5),('verbose',6)))
class ScmPrtAuxSheetType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-3,-2,-1,1,2,101,102)));namedValues=NamedValues(*((_E,-3),(_D,-2),(_C,-1),('jobSetStart',1),('jobSetEnd',2),('printerStartupSheet',101),('jobErrorSheet',102)))
class ScmPrtChannelType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,26,27,28,31,32,33,34,35,36,37,38,39,40,41,42,43)));namedValues=NamedValues(*((_C,1),('chSerialPort',3),('chParallelPort',4),('chIEEE1284Port',5),('chSCSIPort',6),('chAppleTalkPAP',7),('chLPDServer',8),('chNetwareRPrinter',9),('chNetwarePServer',10),('chPort9100',11),('chAppSocket',12),('chFTP',13),('chTFTP',14),('chDLCLLCPort',15),('chIBM3270',16),('chIBM5250',17),('chFax',18),('chIEEE1394',19),('chTransport1',20),('chCPAP',21),('chPCPrint',26),('chServerMessageBlock',27),('chPSM',28),('chSystemObjectManager',31),('chDECLAT',32),('chNPAP',33),('chUSB',34),('chIRDA',35),('chPrintXChange',36),('chPortTCP',37),('chBidirPortTCP',38),('chUNPP',39),('chAppleTalkADSP',40),('chPortSPX',41),('chPortHTTP',42),('chNDPS',43)))
class ScmPrtGroupSupport(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
class ScmPrtIETFPrintMIBGroupSupport(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
class ScmPrtInterpreterLangFamily(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58)));namedValues=NamedValues(*((_C,1),(_D,2),('langPCL',3),('langHPGL',4),('langPJL',5),('langPS',6),('langIPDS',7),('langPPDS',8),('langEscapeP',9),('langEpson',10),('langDDIF',11),('langInterpress',12),('langISO6429',13),('langLineData',14),('langMODCA',15),('langREGIS',16),('langSCS',17),('langSPDL',18),('langTEK4014',19),('langPDS',20),('langIGP',21),('langCodeV',22),('langDSCDSE',23),('langWPS',24),('langLN03',25),('langCCITT',26),('langQUIC',27),('langCPAP',28),('langDecPPL',29),('langSimpleText',30),('langNPAP',31),('langDOC',32),('langimPress',33),('langPinwriter',34),('langNPDL',35),('langNEC201PL',36),('langAutomatic',37),('langPages',38),('langLIPS',39),('langTIFF',40),('langDiagnostic',41),('langPSPrinter',42),('langCaPSL',43),('langEXCL',44),('langLCDS',45),('langXES',46),('langPCLXL',47),('langART',48),('langTIPSI',49),('langPrescribe',50),('langLinePrinter',51),('langIDP',52),('langXJCL',53),('langPDF',54),('langRPDL',55),('langIntermecIPL',56),('langUBIFingerprint',57),('langUBIDirectProtocol',58)))
class ScmPrtMediaTypeErrorPolicy(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,11)));namedValues=NamedValues(*((_C,1),(_D,2),(_E,3),(_F,4),(_G,5),(_H,6),(_I,11)))
class ScmPrtMediumClassType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_C,1),(_D,2),(_E,3),('northAmerica',4),('iso',5),('jis',6)))
class ScmPrtMediumSize(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,10,1000,1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014,1015,1016,1020,1021,1022,1023,1024,1025,1026,1027,1028,1029,1030,1040,1041,1042,1043,1044,1045,1046,1047,1048,1049,1050,1063,1064,1065,1066,1067,1080,1081,1082,1083,1084,1085,1086,1087,1088,1089,1090,1100,1101,1102,1103,1104)));namedValues=NamedValues(*((_C,1),(_D,2),(_E,3),('mediumSize13x18',10),('naLetter',1000),('naLegal',1001),('na10x13Envelope',1002),('na9x12Envelope',1003),('naNumber10Envelope',1004),('na7x9Envelope',1005),('na9x11Envelope',1006),('na10x14Envelope',1007),('naNumber9Envelope',1008),('na6x9Envelope',1009),('na10x15Envelope',1010),('a',1011),('b',1012),('c',1013),('d',1014),('e',1015),('monarchEnvelope',1016),('isoA0',1020),('isoA1',1021),('isoA2',1022),('isoA3',1023),('isoA4',1024),('isoA5',1025),('isoA6',1026),('isoA7',1027),('isoA8',1028),('isoA9',1029),('isoA10',1030),('isoB0',1040),('isoB1',1041),('isoB2',1042),('isoB3',1043),('isoB4',1044),('isoB5',1045),('isoB6',1046),('isoB7',1047),('isoB8',1048),('isoB9',1049),('isoB10',1050),('isoC3',1063),('isoC4',1064),('isoC5',1065),('isoC6',1066),('isoDesignatedLong',1067),('jisB0',1080),('jisB1',1081),('jisB2',1082),('jisB3',1083),('jisB4',1084),('jisB5',1085),('jisB6',1086),('jisB7',1087),('jisB8',1088),('jisB9',1089),('jisB10',1090),('executive',1100),('folio',1101),('invoice',1102),('ledger',1103),('quarto',1104)))
class ScmPrtOutputOffsetStackingType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_C,1),(_D,2),(_E,3),('noOffset',4),('offsetOnJob',5),('offsetOnJobandCopy',6)))
class ScmPrtOutputStaplePosition(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
class ScmPrtPageSizeErrorPolicy(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*((_C,1),(_D,2),(_E,3),(_F,4),(_G,5),(_H,6),('useNearestAndAdjust',7),('useNextLargerAndAdjust',8),('useNearest',9),('useNextLarger',10),(_I,11)))
class ScmPrtPCLFontSource(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,20,41,42,43,44,45,46,47,48,49,61,62,63,64,65,66,67,68,69,80)));namedValues=NamedValues(*((_C,1),(_D,2),(_E,3),('internal',20),('romSimm1',41),('romSimm2',42),('romSimm3',43),('romSimm4',44),('romSimm5',45),('romSimm6',46),('romSimm7',47),('romSimm8',48),('romSimm9',49),('cartridge1',61),('cartridge2',62),('cartridge3',63),('cartridge4',64),('cartridge5',65),('cartridge6',66),('cartridge7',67),('cartridge8',68),('cartridge9',69),('permanentSoft',80)))
class ScmPrtPlex(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
class ScmPrtPrintQuality(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_C,1),(_D,2),(_E,3),('draft',4),('normal',5),('high',6)))
class ScmPrtPrintScreen(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_C,1),(_D,2),(_E,3),('off',4),('mode850',5),('mode852',6)))
class ScmPrtTraySwitch(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_C,1),(_D,2),(_E,3),('off',4),('useScmPrtInputNextPrtInputIndex',5),('useScmPrtInputAliasTable',6)))
class ScmPrtGeneralMonoPrintOpt(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3,4,5)));namedValues=NamedValues(*((_C,1),('optimizeForSpeed',3),('optimizeForEconomy',4),('notPresent',5)))
_SCmPrintTCDummy_ObjectIdentity=ObjectIdentity
sCmPrintTCDummy=_SCmPrintTCDummy_ObjectIdentity((1,3,6,1,4,1,236,11,5,11,54,999))
_SCmPrtTCAuxSheetContent_Type=ScmPrtAuxSheetContent
_SCmPrtTCAuxSheetContent_Object=MibScalar
sCmPrtTCAuxSheetContent=_SCmPrtTCAuxSheetContent_Object((1,3,6,1,4,1,236,11,5,11,54,999,1),_SCmPrtTCAuxSheetContent_Type())
sCmPrtTCAuxSheetContent.setMaxAccess(_B)
if mibBuilder.loadTexts:sCmPrtTCAuxSheetContent.setStatus(_A)
_SCmPrtTCScmPrtAuxSheetType_Type=ScmPrtAuxSheetType
_SCmPrtTCScmPrtAuxSheetType_Object=MibScalar
sCmPrtTCScmPrtAuxSheetType=_SCmPrtTCScmPrtAuxSheetType_Object((1,3,6,1,4,1,236,11,5,11,54,999,2),_SCmPrtTCScmPrtAuxSheetType_Type())
sCmPrtTCScmPrtAuxSheetType.setMaxAccess(_B)
if mibBuilder.loadTexts:sCmPrtTCScmPrtAuxSheetType.setStatus(_A)
_SCmPrtTCTCChannelType_Type=ScmPrtChannelType
_SCmPrtTCTCChannelType_Object=MibScalar
sCmPrtTCTCChannelType=_SCmPrtTCTCChannelType_Object((1,3,6,1,4,1,236,11,5,11,54,999,3),_SCmPrtTCTCChannelType_Type())
sCmPrtTCTCChannelType.setMaxAccess(_B)
if mibBuilder.loadTexts:sCmPrtTCTCChannelType.setStatus(_A)
_SCmPrtTCGroupSupport_Type=ScmPrtGroupSupport
_SCmPrtTCGroupSupport_Object=MibScalar
sCmPrtTCGroupSupport=_SCmPrtTCGroupSupport_Object((1,3,6,1,4,1,236,11,5,11,54,999,4),_SCmPrtTCGroupSupport_Type())
sCmPrtTCGroupSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:sCmPrtTCGroupSupport.setStatus(_A)
_SCmPrtTCIETFPrintMIBGroupSupport_Type=ScmPrtIETFPrintMIBGroupSupport
_SCmPrtTCIETFPrintMIBGroupSupport_Object=MibScalar
sCmPrtTCIETFPrintMIBGroupSupport=_SCmPrtTCIETFPrintMIBGroupSupport_Object((1,3,6,1,4,1,236,11,5,11,54,999,5),_SCmPrtTCIETFPrintMIBGroupSupport_Type())
sCmPrtTCIETFPrintMIBGroupSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:sCmPrtTCIETFPrintMIBGroupSupport.setStatus(_A)
_SCmPrtTCInterpreterLangFamily_Type=ScmPrtInterpreterLangFamily
_SCmPrtTCInterpreterLangFamily_Object=MibScalar
sCmPrtTCInterpreterLangFamily=_SCmPrtTCInterpreterLangFamily_Object((1,3,6,1,4,1,236,11,5,11,54,999,6),_SCmPrtTCInterpreterLangFamily_Type())
sCmPrtTCInterpreterLangFamily.setMaxAccess(_B)
if mibBuilder.loadTexts:sCmPrtTCInterpreterLangFamily.setStatus(_A)
_SCmPrtTCMediaTypeErrorPolicy_Type=ScmPrtMediaTypeErrorPolicy
_SCmPrtTCMediaTypeErrorPolicy_Object=MibScalar
sCmPrtTCMediaTypeErrorPolicy=_SCmPrtTCMediaTypeErrorPolicy_Object((1,3,6,1,4,1,236,11,5,11,54,999,7),_SCmPrtTCMediaTypeErrorPolicy_Type())
sCmPrtTCMediaTypeErrorPolicy.setMaxAccess(_B)
if mibBuilder.loadTexts:sCmPrtTCMediaTypeErrorPolicy.setStatus(_A)
_SCmPrtTCMediumClassType_Type=ScmPrtMediumClassType
_SCmPrtTCMediumClassType_Object=MibScalar
sCmPrtTCMediumClassType=_SCmPrtTCMediumClassType_Object((1,3,6,1,4,1,236,11,5,11,54,999,8),_SCmPrtTCMediumClassType_Type())
sCmPrtTCMediumClassType.setMaxAccess(_B)
if mibBuilder.loadTexts:sCmPrtTCMediumClassType.setStatus(_A)
_SCmPrtTCMediumSize_Type=ScmPrtMediumSize
_SCmPrtTCMediumSize_Object=MibScalar
sCmPrtTCMediumSize=_SCmPrtTCMediumSize_Object((1,3,6,1,4,1,236,11,5,11,54,999,9),_SCmPrtTCMediumSize_Type())
sCmPrtTCMediumSize.setMaxAccess(_B)
if mibBuilder.loadTexts:sCmPrtTCMediumSize.setStatus(_A)
_SCmPrtTCOutputOffsetStackingType_Type=ScmPrtOutputOffsetStackingType
_SCmPrtTCOutputOffsetStackingType_Object=MibScalar
sCmPrtTCOutputOffsetStackingType=_SCmPrtTCOutputOffsetStackingType_Object((1,3,6,1,4,1,236,11,5,11,54,999,10),_SCmPrtTCOutputOffsetStackingType_Type())
sCmPrtTCOutputOffsetStackingType.setMaxAccess(_B)
if mibBuilder.loadTexts:sCmPrtTCOutputOffsetStackingType.setStatus(_A)
_SCmPrtOutputStaplePosition_Type=ScmPrtOutputStaplePosition
_SCmPrtOutputStaplePosition_Object=MibScalar
sCmPrtOutputStaplePosition=_SCmPrtOutputStaplePosition_Object((1,3,6,1,4,1,236,11,5,11,54,999,11),_SCmPrtOutputStaplePosition_Type())
sCmPrtOutputStaplePosition.setMaxAccess(_B)
if mibBuilder.loadTexts:sCmPrtOutputStaplePosition.setStatus(_A)
_SCmPrtTCPageSizeErrorPolicy_Type=ScmPrtPageSizeErrorPolicy
_SCmPrtTCPageSizeErrorPolicy_Object=MibScalar
sCmPrtTCPageSizeErrorPolicy=_SCmPrtTCPageSizeErrorPolicy_Object((1,3,6,1,4,1,236,11,5,11,54,999,12),_SCmPrtTCPageSizeErrorPolicy_Type())
sCmPrtTCPageSizeErrorPolicy.setMaxAccess(_B)
if mibBuilder.loadTexts:sCmPrtTCPageSizeErrorPolicy.setStatus(_A)
_SCmPrtTCPCLFontSource_Type=ScmPrtPCLFontSource
_SCmPrtTCPCLFontSource_Object=MibScalar
sCmPrtTCPCLFontSource=_SCmPrtTCPCLFontSource_Object((1,3,6,1,4,1,236,11,5,11,54,999,13),_SCmPrtTCPCLFontSource_Type())
sCmPrtTCPCLFontSource.setMaxAccess(_B)
if mibBuilder.loadTexts:sCmPrtTCPCLFontSource.setStatus(_A)
_SCmPrtTCPlex_Type=ScmPrtPlex
_SCmPrtTCPlex_Object=MibScalar
sCmPrtTCPlex=_SCmPrtTCPlex_Object((1,3,6,1,4,1,236,11,5,11,54,999,14),_SCmPrtTCPlex_Type())
sCmPrtTCPlex.setMaxAccess(_B)
if mibBuilder.loadTexts:sCmPrtTCPlex.setStatus(_A)
_SCmPrtTCPrintQuality_Type=ScmPrtPrintQuality
_SCmPrtTCPrintQuality_Object=MibScalar
sCmPrtTCPrintQuality=_SCmPrtTCPrintQuality_Object((1,3,6,1,4,1,236,11,5,11,54,999,15),_SCmPrtTCPrintQuality_Type())
sCmPrtTCPrintQuality.setMaxAccess(_B)
if mibBuilder.loadTexts:sCmPrtTCPrintQuality.setStatus(_A)
_SCmPrtTCPrintScreen_Type=ScmPrtPrintScreen
_SCmPrtTCPrintScreen_Object=MibScalar
sCmPrtTCPrintScreen=_SCmPrtTCPrintScreen_Object((1,3,6,1,4,1,236,11,5,11,54,999,16),_SCmPrtTCPrintScreen_Type())
sCmPrtTCPrintScreen.setMaxAccess(_B)
if mibBuilder.loadTexts:sCmPrtTCPrintScreen.setStatus(_A)
_SCmPrtTCTraySwitch_Type=ScmPrtTraySwitch
_SCmPrtTCTraySwitch_Object=MibScalar
sCmPrtTCTraySwitch=_SCmPrtTCTraySwitch_Object((1,3,6,1,4,1,236,11,5,11,54,999,17),_SCmPrtTCTraySwitch_Type())
sCmPrtTCTraySwitch.setMaxAccess(_B)
if mibBuilder.loadTexts:sCmPrtTCTraySwitch.setStatus(_A)
_SCmPrtTCGeneralMonoPrintOpt_Type=ScmPrtGeneralMonoPrintOpt
_SCmPrtTCGeneralMonoPrintOpt_Object=MibScalar
sCmPrtTCGeneralMonoPrintOpt=_SCmPrtTCGeneralMonoPrintOpt_Object((1,3,6,1,4,1,236,11,5,11,54,999,18),_SCmPrtTCGeneralMonoPrintOpt_Type())
sCmPrtTCGeneralMonoPrintOpt.setMaxAccess(_B)
if mibBuilder.loadTexts:sCmPrtTCGeneralMonoPrintOpt.setStatus(_A)
mibBuilder.exportSymbols('SAMSUNG-PRINTER-EXT-TC',**{'ScmPrtAuxSheetContent':ScmPrtAuxSheetContent,'ScmPrtAuxSheetType':ScmPrtAuxSheetType,'ScmPrtChannelType':ScmPrtChannelType,'ScmPrtGroupSupport':ScmPrtGroupSupport,'ScmPrtIETFPrintMIBGroupSupport':ScmPrtIETFPrintMIBGroupSupport,'ScmPrtInterpreterLangFamily':ScmPrtInterpreterLangFamily,'ScmPrtMediaTypeErrorPolicy':ScmPrtMediaTypeErrorPolicy,'ScmPrtMediumClassType':ScmPrtMediumClassType,'ScmPrtMediumSize':ScmPrtMediumSize,'ScmPrtOutputOffsetStackingType':ScmPrtOutputOffsetStackingType,'ScmPrtOutputStaplePosition':ScmPrtOutputStaplePosition,'ScmPrtPageSizeErrorPolicy':ScmPrtPageSizeErrorPolicy,'ScmPrtPCLFontSource':ScmPrtPCLFontSource,'ScmPrtPlex':ScmPrtPlex,'ScmPrtPrintQuality':ScmPrtPrintQuality,'ScmPrtPrintScreen':ScmPrtPrintScreen,'ScmPrtTraySwitch':ScmPrtTraySwitch,'ScmPrtGeneralMonoPrintOpt':ScmPrtGeneralMonoPrintOpt,'scmPrintTC':scmPrintTC,'sCmPrintTCDummy':sCmPrintTCDummy,'sCmPrtTCAuxSheetContent':sCmPrtTCAuxSheetContent,'sCmPrtTCScmPrtAuxSheetType':sCmPrtTCScmPrtAuxSheetType,'sCmPrtTCTCChannelType':sCmPrtTCTCChannelType,'sCmPrtTCGroupSupport':sCmPrtTCGroupSupport,'sCmPrtTCIETFPrintMIBGroupSupport':sCmPrtTCIETFPrintMIBGroupSupport,'sCmPrtTCInterpreterLangFamily':sCmPrtTCInterpreterLangFamily,'sCmPrtTCMediaTypeErrorPolicy':sCmPrtTCMediaTypeErrorPolicy,'sCmPrtTCMediumClassType':sCmPrtTCMediumClassType,'sCmPrtTCMediumSize':sCmPrtTCMediumSize,'sCmPrtTCOutputOffsetStackingType':sCmPrtTCOutputOffsetStackingType,'sCmPrtOutputStaplePosition':sCmPrtOutputStaplePosition,'sCmPrtTCPageSizeErrorPolicy':sCmPrtTCPageSizeErrorPolicy,'sCmPrtTCPCLFontSource':sCmPrtTCPCLFontSource,'sCmPrtTCPlex':sCmPrtTCPlex,'sCmPrtTCPrintQuality':sCmPrtTCPrintQuality,'sCmPrtTCPrintScreen':sCmPrtTCPrintScreen,'sCmPrtTCTraySwitch':sCmPrtTCTraySwitch,'sCmPrtTCGeneralMonoPrintOpt':sCmPrtTCGeneralMonoPrintOpt})