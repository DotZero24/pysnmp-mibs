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
scmGeneralTC=ModuleIdentity((1,3,6,1,4,1,236,11,5,11,50))
class Cardinal16(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32767))
class Cardinal32(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
class Cardinal64High(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
class Cardinal64Low(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
class CodedCountry(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,2))
class CodedLanguage(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,2))
class CodeIndexedStringIndex(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
class Counter64High(TextualConvention,Counter32):status=_A
class Counter64Low(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
class Gauge64High(TextualConvention,Gauge32):status=_A
class Gauge64Low(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
class Integer64High(TextualConvention,Integer32):status=_A
class Integer64Low(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
class Ordinal16(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32767))
class Ordinal32(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
class Ordinal64High(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
class Ordinal64Low(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
class ScmFixedLocaleDisplayString(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
class ScmFixedLocaleUtf8String(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
class ScmNamedLocaleUtf8String(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
class ScmGenGroupSupport(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
class ScmGenLogFullPolicy(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_C,1),(_D,2),('disableService',3),('disableAndPauseService',4),('enableServiceAndFlushLog',5),('enableServiceAndFlushOldest',6)))
class ScmGenMessageMapStringLabel(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
class ScmGenNotifyDetailType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,10,20,21,22,23,30,31,32,33)));namedValues=NamedValues(*((_C,1),(_D,2),('notifyRecipientURI',10),('notifyEventNames',20),('notifyEventDelay',21),('notifySeverityFilter',22),('notifyTrainingFilter',23),('notifyMessageHeaderKeys',30),('notifyMessageHeaderText',31),('notifyMessageContentKeys',32),('notifyMessageContentText',33)))
class ScmGenNotifySchemeSupport(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
class ScmGenNotifySeverityFilter(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
class ScmGenNotifyTrainingFilter(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
class ScmGenOptionValueSyntax(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)));namedValues=NamedValues(*((_C,1),(_D,2),('integerNumber',3),('integerCounter',4),('integerEnum',5),('integerGauge',6),('integerIndex',7),('integerTruthValue',8),('oidObject',9),('oidAutonomous',10),('stringBinary',11),('stringDisplay',12),('stringLocalization',13),('stringCodedCharSet',14),('stringDynamicLocalization',15),('stringUtf8Localization',16)))
class ScmGenReconfOptionState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('idle',1),('validateForImmediateChange',2),('validateForRebootChange',3),('validateForImmediateReboot',4),('validateInProgress',5),('activateForImmediateChange',6),('activateForRebootChange',7),('activateForImmediateReboot',8),('activateInProgress',9)))
class ScmGenRowPersistence(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_C,1),(_D,2),('volatile',3),('nonvolatile',4),('permanent',5),('readonly',6)))
class ScmGenSNMPDomain(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,10,11,20,30)));namedValues=NamedValues(*(('snmpUDPDomain',1),('snmpCLNSDomain',2),('snmpCONSDomain',3),('snmpDDPDomain',4),('snmpIPXDomain',5),('snmpNetBIOSDomain',10),('snmpNetBEUIDomain',11),('snmpTCPDomain',20),('uriNotifyDomain',30)))
class ScmGenSNMPVersion(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_D,1),(_C,2),('snmpV1Community',3),('snmpV1Party',4),('snmpV2Party',5),('snmpV2Community',6),('snmpV2Usec',7),('snmpV2Star',8),('snmpV2Secure',9),('snmpV3Secure',10)))
class ScmGenSNMPv2ErrorStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18)));namedValues=NamedValues(*(('noError',0),('tooBig',1),('noSuchName',2),('badValue',3),('readOnly',4),('genErr',5),('noAccess',6),('wrongType',7),('wrongLength',8),('wrongEncoding',9),('wrongValue',10),('noCreation',11),('inconsistentValue',12),('resourceUnavailable',13),('commitFailed',14),('undoFailed',15),('authorizationError',16),('notWritable',17),('inconsistentName',18)))
class ScmGlobalUniqueID(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_ZeroDotZero_ObjectIdentity=ObjectIdentity
zeroDotZero=_ZeroDotZero_ObjectIdentity((0,0))
_ScmGenZeroDotZero_ObjectIdentity=ObjectIdentity
scmGenZeroDotZero=_ScmGenZeroDotZero_ObjectIdentity((0,0,0))
if mibBuilder.loadTexts:scmGenZeroDotZero.setStatus(_A)
_SCmGeneralDummy_ObjectIdentity=ObjectIdentity
sCmGeneralDummy=_SCmGeneralDummy_ObjectIdentity((1,3,6,1,4,1,236,11,5,11,50,999))
_SCmGenCardinal16_Type=Cardinal16
_SCmGenCardinal16_Object=MibScalar
sCmGenCardinal16=_SCmGenCardinal16_Object((1,3,6,1,4,1,236,11,5,11,50,999,1),_SCmGenCardinal16_Type())
sCmGenCardinal16.setMaxAccess(_B)
if mibBuilder.loadTexts:sCmGenCardinal16.setStatus(_A)
_SCmGenCardinal32_Type=Cardinal32
_SCmGenCardinal32_Object=MibScalar
sCmGenCardinal32=_SCmGenCardinal32_Object((1,3,6,1,4,1,236,11,5,11,50,999,2),_SCmGenCardinal32_Type())
sCmGenCardinal32.setMaxAccess(_B)
if mibBuilder.loadTexts:sCmGenCardinal32.setStatus(_A)
_SCmGenCardinal64High_Type=Cardinal64High
_SCmGenCardinal64High_Object=MibScalar
sCmGenCardinal64High=_SCmGenCardinal64High_Object((1,3,6,1,4,1,236,11,5,11,50,999,3),_SCmGenCardinal64High_Type())
sCmGenCardinal64High.setMaxAccess(_B)
if mibBuilder.loadTexts:sCmGenCardinal64High.setStatus(_A)
_SCmGenCardinal64Low_Type=Cardinal64Low
_SCmGenCardinal64Low_Object=MibScalar
sCmGenCardinal64Low=_SCmGenCardinal64Low_Object((1,3,6,1,4,1,236,11,5,11,50,999,4),_SCmGenCardinal64Low_Type())
sCmGenCardinal64Low.setMaxAccess(_B)
if mibBuilder.loadTexts:sCmGenCardinal64Low.setStatus(_A)
_SCmGenCodedCountry_Type=CodedCountry
_SCmGenCodedCountry_Object=MibScalar
sCmGenCodedCountry=_SCmGenCodedCountry_Object((1,3,6,1,4,1,236,11,5,11,50,999,5),_SCmGenCodedCountry_Type())
sCmGenCodedCountry.setMaxAccess(_B)
if mibBuilder.loadTexts:sCmGenCodedCountry.setStatus(_A)
_SCmGenCodedLanguage_Type=CodedLanguage
_SCmGenCodedLanguage_Object=MibScalar
sCmGenCodedLanguage=_SCmGenCodedLanguage_Object((1,3,6,1,4,1,236,11,5,11,50,999,6),_SCmGenCodedLanguage_Type())
sCmGenCodedLanguage.setMaxAccess(_B)
if mibBuilder.loadTexts:sCmGenCodedLanguage.setStatus(_A)
_SCmGenCodeIndexedStringIndex_Type=CodeIndexedStringIndex
_SCmGenCodeIndexedStringIndex_Object=MibScalar
sCmGenCodeIndexedStringIndex=_SCmGenCodeIndexedStringIndex_Object((1,3,6,1,4,1,236,11,5,11,50,999,7),_SCmGenCodeIndexedStringIndex_Type())
sCmGenCodeIndexedStringIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sCmGenCodeIndexedStringIndex.setStatus(_A)
_SCmGenCounter64High_Type=Counter64High
_SCmGenCounter64High_Object=MibScalar
sCmGenCounter64High=_SCmGenCounter64High_Object((1,3,6,1,4,1,236,11,5,11,50,999,8),_SCmGenCounter64High_Type())
sCmGenCounter64High.setMaxAccess(_B)
if mibBuilder.loadTexts:sCmGenCounter64High.setStatus(_A)
_SCmGenCounter64Low_Type=Counter64Low
_SCmGenCounter64Low_Object=MibScalar
sCmGenCounter64Low=_SCmGenCounter64Low_Object((1,3,6,1,4,1,236,11,5,11,50,999,9),_SCmGenCounter64Low_Type())
sCmGenCounter64Low.setMaxAccess(_B)
if mibBuilder.loadTexts:sCmGenCounter64Low.setStatus(_A)
_SCmGenGauge64High_Type=Gauge64High
_SCmGenGauge64High_Object=MibScalar
sCmGenGauge64High=_SCmGenGauge64High_Object((1,3,6,1,4,1,236,11,5,11,50,999,10),_SCmGenGauge64High_Type())
sCmGenGauge64High.setMaxAccess(_B)
if mibBuilder.loadTexts:sCmGenGauge64High.setStatus(_A)
_SCmGenGauge64Low_Type=Gauge64Low
_SCmGenGauge64Low_Object=MibScalar
sCmGenGauge64Low=_SCmGenGauge64Low_Object((1,3,6,1,4,1,236,11,5,11,50,999,11),_SCmGenGauge64Low_Type())
sCmGenGauge64Low.setMaxAccess(_B)
if mibBuilder.loadTexts:sCmGenGauge64Low.setStatus(_A)
_SCmGenInteger64High_Type=Integer64High
_SCmGenInteger64High_Object=MibScalar
sCmGenInteger64High=_SCmGenInteger64High_Object((1,3,6,1,4,1,236,11,5,11,50,999,12),_SCmGenInteger64High_Type())
sCmGenInteger64High.setMaxAccess(_B)
if mibBuilder.loadTexts:sCmGenInteger64High.setStatus(_A)
_SCmGenInteger64Low_Type=Integer64Low
_SCmGenInteger64Low_Object=MibScalar
sCmGenInteger64Low=_SCmGenInteger64Low_Object((1,3,6,1,4,1,236,11,5,11,50,999,13),_SCmGenInteger64Low_Type())
sCmGenInteger64Low.setMaxAccess(_B)
if mibBuilder.loadTexts:sCmGenInteger64Low.setStatus(_A)
_SCmGenOrdinal16_Type=Ordinal16
_SCmGenOrdinal16_Object=MibScalar
sCmGenOrdinal16=_SCmGenOrdinal16_Object((1,3,6,1,4,1,236,11,5,11,50,999,14),_SCmGenOrdinal16_Type())
sCmGenOrdinal16.setMaxAccess(_B)
if mibBuilder.loadTexts:sCmGenOrdinal16.setStatus(_A)
_SCmGenOrdinal32_Type=Ordinal32
_SCmGenOrdinal32_Object=MibScalar
sCmGenOrdinal32=_SCmGenOrdinal32_Object((1,3,6,1,4,1,236,11,5,11,50,999,15),_SCmGenOrdinal32_Type())
sCmGenOrdinal32.setMaxAccess(_B)
if mibBuilder.loadTexts:sCmGenOrdinal32.setStatus(_A)
_SCmGenOrdinal64High_Type=Ordinal64High
_SCmGenOrdinal64High_Object=MibScalar
sCmGenOrdinal64High=_SCmGenOrdinal64High_Object((1,3,6,1,4,1,236,11,5,11,50,999,16),_SCmGenOrdinal64High_Type())
sCmGenOrdinal64High.setMaxAccess(_B)
if mibBuilder.loadTexts:sCmGenOrdinal64High.setStatus(_A)
_SCmGenOrdinal64Low_Type=Ordinal64Low
_SCmGenOrdinal64Low_Object=MibScalar
sCmGenOrdinal64Low=_SCmGenOrdinal64Low_Object((1,3,6,1,4,1,236,11,5,11,50,999,17),_SCmGenOrdinal64Low_Type())
sCmGenOrdinal64Low.setMaxAccess(_B)
if mibBuilder.loadTexts:sCmGenOrdinal64Low.setStatus(_A)
_SCmGenFixedLocaleDisplayString_Type=ScmFixedLocaleDisplayString
_SCmGenFixedLocaleDisplayString_Object=MibScalar
sCmGenFixedLocaleDisplayString=_SCmGenFixedLocaleDisplayString_Object((1,3,6,1,4,1,236,11,5,11,50,999,18),_SCmGenFixedLocaleDisplayString_Type())
sCmGenFixedLocaleDisplayString.setMaxAccess(_B)
if mibBuilder.loadTexts:sCmGenFixedLocaleDisplayString.setStatus(_A)
_SCmGenGroupSupport_Type=ScmGenGroupSupport
_SCmGenGroupSupport_Object=MibScalar
sCmGenGroupSupport=_SCmGenGroupSupport_Object((1,3,6,1,4,1,236,11,5,11,50,999,19),_SCmGenGroupSupport_Type())
sCmGenGroupSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:sCmGenGroupSupport.setStatus(_A)
_SCmGenLogFullPolicy_Type=ScmGenLogFullPolicy
_SCmGenLogFullPolicy_Object=MibScalar
sCmGenLogFullPolicy=_SCmGenLogFullPolicy_Object((1,3,6,1,4,1,236,11,5,11,50,999,20),_SCmGenLogFullPolicy_Type())
sCmGenLogFullPolicy.setMaxAccess(_B)
if mibBuilder.loadTexts:sCmGenLogFullPolicy.setStatus(_A)
_SCmGenOptionValueSyntax_Type=ScmGenOptionValueSyntax
_SCmGenOptionValueSyntax_Object=MibScalar
sCmGenOptionValueSyntax=_SCmGenOptionValueSyntax_Object((1,3,6,1,4,1,236,11,5,11,50,999,21),_SCmGenOptionValueSyntax_Type())
sCmGenOptionValueSyntax.setMaxAccess(_B)
if mibBuilder.loadTexts:sCmGenOptionValueSyntax.setStatus(_A)
_SCmGenReconfOptionState_Type=ScmGenReconfOptionState
_SCmGenReconfOptionState_Object=MibScalar
sCmGenReconfOptionState=_SCmGenReconfOptionState_Object((1,3,6,1,4,1,236,11,5,11,50,999,22),_SCmGenReconfOptionState_Type())
sCmGenReconfOptionState.setMaxAccess(_B)
if mibBuilder.loadTexts:sCmGenReconfOptionState.setStatus(_A)
_SCmGenRowPersistence_Type=ScmGenRowPersistence
_SCmGenRowPersistence_Object=MibScalar
sCmGenRowPersistence=_SCmGenRowPersistence_Object((1,3,6,1,4,1,236,11,5,11,50,999,23),_SCmGenRowPersistence_Type())
sCmGenRowPersistence.setMaxAccess(_B)
if mibBuilder.loadTexts:sCmGenRowPersistence.setStatus(_A)
_SCmGenSNMPDomain_Type=ScmGenSNMPDomain
_SCmGenSNMPDomain_Object=MibScalar
sCmGenSNMPDomain=_SCmGenSNMPDomain_Object((1,3,6,1,4,1,236,11,5,11,50,999,24),_SCmGenSNMPDomain_Type())
sCmGenSNMPDomain.setMaxAccess(_B)
if mibBuilder.loadTexts:sCmGenSNMPDomain.setStatus(_A)
_SCmGenSNMPVersion_Type=ScmGenSNMPVersion
_SCmGenSNMPVersion_Object=MibScalar
sCmGenSNMPVersion=_SCmGenSNMPVersion_Object((1,3,6,1,4,1,236,11,5,11,50,999,25),_SCmGenSNMPVersion_Type())
sCmGenSNMPVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:sCmGenSNMPVersion.setStatus(_A)
_SCmGenSNMPv2ErrorStatus_Type=ScmGenSNMPv2ErrorStatus
_SCmGenSNMPv2ErrorStatus_Object=MibScalar
sCmGenSNMPv2ErrorStatus=_SCmGenSNMPv2ErrorStatus_Object((1,3,6,1,4,1,236,11,5,11,50,999,26),_SCmGenSNMPv2ErrorStatus_Type())
sCmGenSNMPv2ErrorStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sCmGenSNMPv2ErrorStatus.setStatus(_A)
_SCmGenGlobalUniqueID_Type=ScmGlobalUniqueID
_SCmGenGlobalUniqueID_Object=MibScalar
sCmGenGlobalUniqueID=_SCmGenGlobalUniqueID_Object((1,3,6,1,4,1,236,11,5,11,50,999,27),_SCmGenGlobalUniqueID_Type())
sCmGenGlobalUniqueID.setMaxAccess(_B)
if mibBuilder.loadTexts:sCmGenGlobalUniqueID.setStatus(_A)
_SCmGenFixedLocaleUtf8String_Type=ScmFixedLocaleUtf8String
_SCmGenFixedLocaleUtf8String_Object=MibScalar
sCmGenFixedLocaleUtf8String=_SCmGenFixedLocaleUtf8String_Object((1,3,6,1,4,1,236,11,5,11,50,999,28),_SCmGenFixedLocaleUtf8String_Type())
sCmGenFixedLocaleUtf8String.setMaxAccess(_B)
if mibBuilder.loadTexts:sCmGenFixedLocaleUtf8String.setStatus(_A)
_SCmGenMessageMapStringLabel_Type=ScmGenMessageMapStringLabel
_SCmGenMessageMapStringLabel_Object=MibScalar
sCmGenMessageMapStringLabel=_SCmGenMessageMapStringLabel_Object((1,3,6,1,4,1,236,11,5,11,50,999,29),_SCmGenMessageMapStringLabel_Type())
sCmGenMessageMapStringLabel.setMaxAccess(_B)
if mibBuilder.loadTexts:sCmGenMessageMapStringLabel.setStatus(_A)
_SCmGenNamedLocaleUtf8String_Type=ScmNamedLocaleUtf8String
_SCmGenNamedLocaleUtf8String_Object=MibScalar
sCmGenNamedLocaleUtf8String=_SCmGenNamedLocaleUtf8String_Object((1,3,6,1,4,1,236,11,5,11,50,999,30),_SCmGenNamedLocaleUtf8String_Type())
sCmGenNamedLocaleUtf8String.setMaxAccess(_B)
if mibBuilder.loadTexts:sCmGenNamedLocaleUtf8String.setStatus(_A)
_SCmGenNotifySchemeSupport_Type=ScmGenNotifySchemeSupport
_SCmGenNotifySchemeSupport_Object=MibScalar
sCmGenNotifySchemeSupport=_SCmGenNotifySchemeSupport_Object((1,3,6,1,4,1,236,11,5,11,50,999,31),_SCmGenNotifySchemeSupport_Type())
sCmGenNotifySchemeSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:sCmGenNotifySchemeSupport.setStatus(_A)
_SCmGenNotifySeverityFilter_Type=ScmGenNotifySeverityFilter
_SCmGenNotifySeverityFilter_Object=MibScalar
sCmGenNotifySeverityFilter=_SCmGenNotifySeverityFilter_Object((1,3,6,1,4,1,236,11,5,11,50,999,32),_SCmGenNotifySeverityFilter_Type())
sCmGenNotifySeverityFilter.setMaxAccess(_B)
if mibBuilder.loadTexts:sCmGenNotifySeverityFilter.setStatus(_A)
_SCmGenNotifyTrainingFilter_Type=ScmGenNotifyTrainingFilter
_SCmGenNotifyTrainingFilter_Object=MibScalar
sCmGenNotifyTrainingFilter=_SCmGenNotifyTrainingFilter_Object((1,3,6,1,4,1,236,11,5,11,50,999,33),_SCmGenNotifyTrainingFilter_Type())
sCmGenNotifyTrainingFilter.setMaxAccess(_B)
if mibBuilder.loadTexts:sCmGenNotifyTrainingFilter.setStatus(_A)
_SCmGenNotifyDetailType_Type=ScmGenNotifyDetailType
_SCmGenNotifyDetailType_Object=MibScalar
sCmGenNotifyDetailType=_SCmGenNotifyDetailType_Object((1,3,6,1,4,1,236,11,5,11,50,999,34),_SCmGenNotifyDetailType_Type())
sCmGenNotifyDetailType.setMaxAccess(_B)
if mibBuilder.loadTexts:sCmGenNotifyDetailType.setStatus(_A)
mibBuilder.exportSymbols('SAMSUNG-GENERAL-TC',**{'Cardinal16':Cardinal16,'Cardinal32':Cardinal32,'Cardinal64High':Cardinal64High,'Cardinal64Low':Cardinal64Low,'CodedCountry':CodedCountry,'CodedLanguage':CodedLanguage,'CodeIndexedStringIndex':CodeIndexedStringIndex,'Counter64High':Counter64High,'Counter64Low':Counter64Low,'Gauge64High':Gauge64High,'Gauge64Low':Gauge64Low,'Integer64High':Integer64High,'Integer64Low':Integer64Low,'Ordinal16':Ordinal16,'Ordinal32':Ordinal32,'Ordinal64High':Ordinal64High,'Ordinal64Low':Ordinal64Low,'ScmFixedLocaleDisplayString':ScmFixedLocaleDisplayString,'ScmFixedLocaleUtf8String':ScmFixedLocaleUtf8String,'ScmNamedLocaleUtf8String':ScmNamedLocaleUtf8String,'ScmGenGroupSupport':ScmGenGroupSupport,'ScmGenLogFullPolicy':ScmGenLogFullPolicy,'ScmGenMessageMapStringLabel':ScmGenMessageMapStringLabel,'ScmGenNotifyDetailType':ScmGenNotifyDetailType,'ScmGenNotifySchemeSupport':ScmGenNotifySchemeSupport,'ScmGenNotifySeverityFilter':ScmGenNotifySeverityFilter,'ScmGenNotifyTrainingFilter':ScmGenNotifyTrainingFilter,'ScmGenOptionValueSyntax':ScmGenOptionValueSyntax,'ScmGenReconfOptionState':ScmGenReconfOptionState,'ScmGenRowPersistence':ScmGenRowPersistence,'ScmGenSNMPDomain':ScmGenSNMPDomain,'ScmGenSNMPVersion':ScmGenSNMPVersion,'ScmGenSNMPv2ErrorStatus':ScmGenSNMPv2ErrorStatus,'ScmGlobalUniqueID':ScmGlobalUniqueID,'zeroDotZero':zeroDotZero,'scmGenZeroDotZero':scmGenZeroDotZero,'scmGeneralTC':scmGeneralTC,'sCmGeneralDummy':sCmGeneralDummy,'sCmGenCardinal16':sCmGenCardinal16,'sCmGenCardinal32':sCmGenCardinal32,'sCmGenCardinal64High':sCmGenCardinal64High,'sCmGenCardinal64Low':sCmGenCardinal64Low,'sCmGenCodedCountry':sCmGenCodedCountry,'sCmGenCodedLanguage':sCmGenCodedLanguage,'sCmGenCodeIndexedStringIndex':sCmGenCodeIndexedStringIndex,'sCmGenCounter64High':sCmGenCounter64High,'sCmGenCounter64Low':sCmGenCounter64Low,'sCmGenGauge64High':sCmGenGauge64High,'sCmGenGauge64Low':sCmGenGauge64Low,'sCmGenInteger64High':sCmGenInteger64High,'sCmGenInteger64Low':sCmGenInteger64Low,'sCmGenOrdinal16':sCmGenOrdinal16,'sCmGenOrdinal32':sCmGenOrdinal32,'sCmGenOrdinal64High':sCmGenOrdinal64High,'sCmGenOrdinal64Low':sCmGenOrdinal64Low,'sCmGenFixedLocaleDisplayString':sCmGenFixedLocaleDisplayString,'sCmGenGroupSupport':sCmGenGroupSupport,'sCmGenLogFullPolicy':sCmGenLogFullPolicy,'sCmGenOptionValueSyntax':sCmGenOptionValueSyntax,'sCmGenReconfOptionState':sCmGenReconfOptionState,'sCmGenRowPersistence':sCmGenRowPersistence,'sCmGenSNMPDomain':sCmGenSNMPDomain,'sCmGenSNMPVersion':sCmGenSNMPVersion,'sCmGenSNMPv2ErrorStatus':sCmGenSNMPv2ErrorStatus,'sCmGenGlobalUniqueID':sCmGenGlobalUniqueID,'sCmGenFixedLocaleUtf8String':sCmGenFixedLocaleUtf8String,'sCmGenMessageMapStringLabel':sCmGenMessageMapStringLabel,'sCmGenNamedLocaleUtf8String':sCmGenNamedLocaleUtf8String,'sCmGenNotifySchemeSupport':sCmGenNotifySchemeSupport,'sCmGenNotifySeverityFilter':sCmGenNotifySeverityFilter,'sCmGenNotifyTrainingFilter':sCmGenNotifyTrainingFilter,'sCmGenNotifyDetailType':sCmGenNotifyDetailType})