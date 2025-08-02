_G='rlLocalizationLanguagesName'
_F='CISCOSB-LOCALIZATION-MIB'
_E='SnmpAdminString'
_D='Integer32'
_C='DisplayString'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
switch001,=mibBuilder.importSymbols('CISCOSB-MIB','switch001')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_E)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_C,'PhysAddress','RowStatus','TextualConvention','TruthValue')
rlLocalization=ModuleIdentity((1,3,6,1,4,1,9,6,1,101,103))
if mibBuilder.loadTexts:rlLocalization.setRevisions(('2005-03-15 00:00',))
class _RlLocalizationActivelanguage_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_RlLocalizationActivelanguage_Type.__name__=_C
_RlLocalizationActivelanguage_Object=MibScalar
rlLocalizationActivelanguage=_RlLocalizationActivelanguage_Object((1,3,6,1,4,1,9,6,1,101,103,8),_RlLocalizationActivelanguage_Type())
rlLocalizationActivelanguage.setMaxAccess('read-write')
if mibBuilder.loadTexts:rlLocalizationActivelanguage.setStatus(_A)
_RlLocalizationLoginlanguage_Type=DisplayString
_RlLocalizationLoginlanguage_Object=MibScalar
rlLocalizationLoginlanguage=_RlLocalizationLoginlanguage_Object((1,3,6,1,4,1,9,6,1,101,103,9),_RlLocalizationLoginlanguage_Type())
rlLocalizationLoginlanguage.setMaxAccess(_B)
if mibBuilder.loadTexts:rlLocalizationLoginlanguage.setStatus(_A)
_RlLocalizationLanguagesTable_Object=MibTable
rlLocalizationLanguagesTable=_RlLocalizationLanguagesTable_Object((1,3,6,1,4,1,9,6,1,101,103,10))
if mibBuilder.loadTexts:rlLocalizationLanguagesTable.setStatus(_A)
_RlLocalizationLanguagesEntry_Object=MibTableRow
rlLocalizationLanguagesEntry=_RlLocalizationLanguagesEntry_Object((1,3,6,1,4,1,9,6,1,101,103,10,1))
rlLocalizationLanguagesEntry.setIndexNames((1,_F,_G))
if mibBuilder.loadTexts:rlLocalizationLanguagesEntry.setStatus(_A)
class _RlLocalizationLanguagesName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,50))
_RlLocalizationLanguagesName_Type.__name__=_C
_RlLocalizationLanguagesName_Object=MibTableColumn
rlLocalizationLanguagesName=_RlLocalizationLanguagesName_Object((1,3,6,1,4,1,9,6,1,101,103,10,1,1),_RlLocalizationLanguagesName_Type())
rlLocalizationLanguagesName.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:rlLocalizationLanguagesName.setStatus(_A)
class _RlLocalizationLanguagesUnicodeName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_RlLocalizationLanguagesUnicodeName_Type.__name__=_E
_RlLocalizationLanguagesUnicodeName_Object=MibTableColumn
rlLocalizationLanguagesUnicodeName=_RlLocalizationLanguagesUnicodeName_Object((1,3,6,1,4,1,9,6,1,101,103,10,1,2),_RlLocalizationLanguagesUnicodeName_Type())
rlLocalizationLanguagesUnicodeName.setMaxAccess(_B)
if mibBuilder.loadTexts:rlLocalizationLanguagesUnicodeName.setStatus(_A)
_RlLocalizationLanguagesUrlDir_Type=DisplayString
_RlLocalizationLanguagesUrlDir_Object=MibTableColumn
rlLocalizationLanguagesUrlDir=_RlLocalizationLanguagesUrlDir_Object((1,3,6,1,4,1,9,6,1,101,103,10,1,3),_RlLocalizationLanguagesUrlDir_Type())
rlLocalizationLanguagesUrlDir.setMaxAccess(_B)
if mibBuilder.loadTexts:rlLocalizationLanguagesUrlDir.setStatus(_A)
_RlLocalizationLanguagesUrlHelpDir_Type=DisplayString
_RlLocalizationLanguagesUrlHelpDir_Object=MibTableColumn
rlLocalizationLanguagesUrlHelpDir=_RlLocalizationLanguagesUrlHelpDir_Object((1,3,6,1,4,1,9,6,1,101,103,10,1,4),_RlLocalizationLanguagesUrlHelpDir_Type())
rlLocalizationLanguagesUrlHelpDir.setMaxAccess(_B)
if mibBuilder.loadTexts:rlLocalizationLanguagesUrlHelpDir.setStatus(_A)
_RlLocalizationLanguageCode_Type=DisplayString
_RlLocalizationLanguageCode_Object=MibTableColumn
rlLocalizationLanguageCode=_RlLocalizationLanguageCode_Object((1,3,6,1,4,1,9,6,1,101,103,10,1,5),_RlLocalizationLanguageCode_Type())
rlLocalizationLanguageCode.setMaxAccess(_B)
if mibBuilder.loadTexts:rlLocalizationLanguageCode.setStatus(_A)
class _RlLocalizationNumOfSections_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_RlLocalizationNumOfSections_Type.__name__=_D
_RlLocalizationNumOfSections_Object=MibTableColumn
rlLocalizationNumOfSections=_RlLocalizationNumOfSections_Object((1,3,6,1,4,1,9,6,1,101,103,10,1,6),_RlLocalizationNumOfSections_Type())
rlLocalizationNumOfSections.setMaxAccess(_B)
if mibBuilder.loadTexts:rlLocalizationNumOfSections.setStatus(_A)
class _RlLocalizationNumOfEmbSections_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_RlLocalizationNumOfEmbSections_Type.__name__=_D
_RlLocalizationNumOfEmbSections_Object=MibTableColumn
rlLocalizationNumOfEmbSections=_RlLocalizationNumOfEmbSections_Object((1,3,6,1,4,1,9,6,1,101,103,10,1,7),_RlLocalizationNumOfEmbSections_Type())
rlLocalizationNumOfEmbSections.setMaxAccess(_B)
if mibBuilder.loadTexts:rlLocalizationNumOfEmbSections.setStatus(_A)
class _RlLocalizationDirection_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,3))
_RlLocalizationDirection_Type.__name__=_C
_RlLocalizationDirection_Object=MibTableColumn
rlLocalizationDirection=_RlLocalizationDirection_Object((1,3,6,1,4,1,9,6,1,101,103,10,1,8),_RlLocalizationDirection_Type())
rlLocalizationDirection.setMaxAccess(_B)
if mibBuilder.loadTexts:rlLocalizationDirection.setStatus(_A)
class _RlLocalizationDateFormat_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_RlLocalizationDateFormat_Type.__name__=_C
_RlLocalizationDateFormat_Object=MibTableColumn
rlLocalizationDateFormat=_RlLocalizationDateFormat_Object((1,3,6,1,4,1,9,6,1,101,103,10,1,9),_RlLocalizationDateFormat_Type())
rlLocalizationDateFormat.setMaxAccess(_B)
if mibBuilder.loadTexts:rlLocalizationDateFormat.setStatus(_A)
class _RlLocalizationTimeFormat_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_RlLocalizationTimeFormat_Type.__name__=_C
_RlLocalizationTimeFormat_Object=MibTableColumn
rlLocalizationTimeFormat=_RlLocalizationTimeFormat_Object((1,3,6,1,4,1,9,6,1,101,103,10,1,10),_RlLocalizationTimeFormat_Type())
rlLocalizationTimeFormat.setMaxAccess(_B)
if mibBuilder.loadTexts:rlLocalizationTimeFormat.setStatus(_A)
class _RlLocalizationNumberFormat_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_RlLocalizationNumberFormat_Type.__name__=_C
_RlLocalizationNumberFormat_Object=MibTableColumn
rlLocalizationNumberFormat=_RlLocalizationNumberFormat_Object((1,3,6,1,4,1,9,6,1,101,103,10,1,11),_RlLocalizationNumberFormat_Type())
rlLocalizationNumberFormat.setMaxAccess(_B)
if mibBuilder.loadTexts:rlLocalizationNumberFormat.setStatus(_A)
class _RlLocalizationShortButtonWidthPercentage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(50,300))
_RlLocalizationShortButtonWidthPercentage_Type.__name__=_D
_RlLocalizationShortButtonWidthPercentage_Object=MibTableColumn
rlLocalizationShortButtonWidthPercentage=_RlLocalizationShortButtonWidthPercentage_Object((1,3,6,1,4,1,9,6,1,101,103,10,1,12),_RlLocalizationShortButtonWidthPercentage_Type())
rlLocalizationShortButtonWidthPercentage.setMaxAccess(_B)
if mibBuilder.loadTexts:rlLocalizationShortButtonWidthPercentage.setStatus(_A)
class _RlLocalizationLongButtonWidthPercentage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(50,300))
_RlLocalizationLongButtonWidthPercentage_Type.__name__=_D
_RlLocalizationLongButtonWidthPercentage_Object=MibTableColumn
rlLocalizationLongButtonWidthPercentage=_RlLocalizationLongButtonWidthPercentage_Object((1,3,6,1,4,1,9,6,1,101,103,10,1,13),_RlLocalizationLongButtonWidthPercentage_Type())
rlLocalizationLongButtonWidthPercentage.setMaxAccess(_B)
if mibBuilder.loadTexts:rlLocalizationLongButtonWidthPercentage.setStatus(_A)
class _RlLocalizationVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_RlLocalizationVersion_Type.__name__=_C
_RlLocalizationVersion_Object=MibTableColumn
rlLocalizationVersion=_RlLocalizationVersion_Object((1,3,6,1,4,1,9,6,1,101,103,10,1,14),_RlLocalizationVersion_Type())
rlLocalizationVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:rlLocalizationVersion.setStatus(_A)
_RlLocalizationMd5ChksumFile_Type=DisplayString
_RlLocalizationMd5ChksumFile_Object=MibTableColumn
rlLocalizationMd5ChksumFile=_RlLocalizationMd5ChksumFile_Object((1,3,6,1,4,1,9,6,1,101,103,10,1,15),_RlLocalizationMd5ChksumFile_Type())
rlLocalizationMd5ChksumFile.setMaxAccess(_B)
if mibBuilder.loadTexts:rlLocalizationMd5ChksumFile.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'rlLocalization':rlLocalization,'rlLocalizationActivelanguage':rlLocalizationActivelanguage,'rlLocalizationLoginlanguage':rlLocalizationLoginlanguage,'rlLocalizationLanguagesTable':rlLocalizationLanguagesTable,'rlLocalizationLanguagesEntry':rlLocalizationLanguagesEntry,_G:rlLocalizationLanguagesName,'rlLocalizationLanguagesUnicodeName':rlLocalizationLanguagesUnicodeName,'rlLocalizationLanguagesUrlDir':rlLocalizationLanguagesUrlDir,'rlLocalizationLanguagesUrlHelpDir':rlLocalizationLanguagesUrlHelpDir,'rlLocalizationLanguageCode':rlLocalizationLanguageCode,'rlLocalizationNumOfSections':rlLocalizationNumOfSections,'rlLocalizationNumOfEmbSections':rlLocalizationNumOfEmbSections,'rlLocalizationDirection':rlLocalizationDirection,'rlLocalizationDateFormat':rlLocalizationDateFormat,'rlLocalizationTimeFormat':rlLocalizationTimeFormat,'rlLocalizationNumberFormat':rlLocalizationNumberFormat,'rlLocalizationShortButtonWidthPercentage':rlLocalizationShortButtonWidthPercentage,'rlLocalizationLongButtonWidthPercentage':rlLocalizationLongButtonWidthPercentage,'rlLocalizationVersion':rlLocalizationVersion,'rlLocalizationMd5ChksumFile':rlLocalizationMd5ChksumFile})