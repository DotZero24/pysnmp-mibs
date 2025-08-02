_U='cvUriClassGroup'
_T='cvUriClassSIPUserIDPreference'
_S='cvUriClassSIPHostPreference'
_R='cvCommonUriClassCfgURIPattern'
_Q='cvTELUriClassCfgPhoneCtxtPattern'
_P='cvTELUriClassCfgPhoneNumPattern'
_O='cvSIPUriClassCfgPhoneCtxtPattern'
_N='cvSIPUriClassCfgHostPattern'
_M='cvSIPUriClassCfgUserIDPattern'
_L='cvUriClassCfgStatus'
_K='cvUriClassCfgType'
_J='read-create'
_I='Integer32'
_H='OctetString'
_G='CvUriClassPreference'
_F='32a'
_E='cvUriClassCfgTag'
_D='CvUriClassPattern'
_C='read-write'
_B='CISCO-VOICE-URI-CLASS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_H,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoExperiment,=mibBuilder.importSymbols('CISCO-SMI','ciscoExperiment')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_I,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
ciscoVoiceUriClassMIB=ModuleIdentity((1,3,6,1,4,1,9,10,99999999))
if mibBuilder.loadTexts:ciscoVoiceUriClassMIB.setRevisions(('2002-10-10 00:00',))
class CvUriClassTagIndex(TextualConvention,OctetString):status=_A;displayHint=_F;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
class CvUriClassTag(TextualConvention,OctetString):status=_A;displayHint=_F;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
class CvUriClassPattern(TextualConvention,OctetString):status=_A;displayHint=_F;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
class CvUriClassPreference(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_CvUriClassMIBNotifications_ObjectIdentity=ObjectIdentity
cvUriClassMIBNotifications=_CvUriClassMIBNotifications_ObjectIdentity((1,3,6,1,4,1,9,10,99999999,0))
_CvUriClassMIBObjects_ObjectIdentity=ObjectIdentity
cvUriClassMIBObjects=_CvUriClassMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,10,99999999,1))
_CvUriClass_ObjectIdentity=ObjectIdentity
cvUriClass=_CvUriClass_ObjectIdentity((1,3,6,1,4,1,9,10,99999999,1,1))
_CvUriClassCfgTable_Object=MibTable
cvUriClassCfgTable=_CvUriClassCfgTable_Object((1,3,6,1,4,1,9,10,99999999,1,1,1))
if mibBuilder.loadTexts:cvUriClassCfgTable.setStatus(_A)
_CvUriClassCfgEntry_Object=MibTableRow
cvUriClassCfgEntry=_CvUriClassCfgEntry_Object((1,3,6,1,4,1,9,10,99999999,1,1,1,1))
cvUriClassCfgEntry.setIndexNames((1,_B,_E))
if mibBuilder.loadTexts:cvUriClassCfgEntry.setStatus(_A)
_CvUriClassCfgTag_Type=CvUriClassTagIndex
_CvUriClassCfgTag_Object=MibTableColumn
cvUriClassCfgTag=_CvUriClassCfgTag_Object((1,3,6,1,4,1,9,10,99999999,1,1,1,1,1),_CvUriClassCfgTag_Type())
cvUriClassCfgTag.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:cvUriClassCfgTag.setStatus(_A)
class _CvUriClassCfgType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('sip',1),('tel',2)))
_CvUriClassCfgType_Type.__name__=_I
_CvUriClassCfgType_Object=MibTableColumn
cvUriClassCfgType=_CvUriClassCfgType_Object((1,3,6,1,4,1,9,10,99999999,1,1,1,1,2),_CvUriClassCfgType_Type())
cvUriClassCfgType.setMaxAccess(_J)
if mibBuilder.loadTexts:cvUriClassCfgType.setStatus(_A)
_CvUriClassCfgStatus_Type=RowStatus
_CvUriClassCfgStatus_Object=MibTableColumn
cvUriClassCfgStatus=_CvUriClassCfgStatus_Object((1,3,6,1,4,1,9,10,99999999,1,1,1,1,3),_CvUriClassCfgStatus_Type())
cvUriClassCfgStatus.setMaxAccess(_J)
if mibBuilder.loadTexts:cvUriClassCfgStatus.setStatus(_A)
_CvSIPUriClassCfgTable_Object=MibTable
cvSIPUriClassCfgTable=_CvSIPUriClassCfgTable_Object((1,3,6,1,4,1,9,10,99999999,1,1,2))
if mibBuilder.loadTexts:cvSIPUriClassCfgTable.setStatus(_A)
_CvSIPUriClassCfgEntry_Object=MibTableRow
cvSIPUriClassCfgEntry=_CvSIPUriClassCfgEntry_Object((1,3,6,1,4,1,9,10,99999999,1,1,2,1))
cvSIPUriClassCfgEntry.setIndexNames((1,_B,_E))
if mibBuilder.loadTexts:cvSIPUriClassCfgEntry.setStatus(_A)
class _CvSIPUriClassCfgUserIDPattern_Type(CvUriClassPattern):defaultValue=OctetString('')
_CvSIPUriClassCfgUserIDPattern_Type.__name__=_D
_CvSIPUriClassCfgUserIDPattern_Object=MibTableColumn
cvSIPUriClassCfgUserIDPattern=_CvSIPUriClassCfgUserIDPattern_Object((1,3,6,1,4,1,9,10,99999999,1,1,2,1,1),_CvSIPUriClassCfgUserIDPattern_Type())
cvSIPUriClassCfgUserIDPattern.setMaxAccess(_C)
if mibBuilder.loadTexts:cvSIPUriClassCfgUserIDPattern.setStatus(_A)
class _CvSIPUriClassCfgHostPattern_Type(CvUriClassPattern):defaultValue=OctetString('')
_CvSIPUriClassCfgHostPattern_Type.__name__=_D
_CvSIPUriClassCfgHostPattern_Object=MibTableColumn
cvSIPUriClassCfgHostPattern=_CvSIPUriClassCfgHostPattern_Object((1,3,6,1,4,1,9,10,99999999,1,1,2,1,2),_CvSIPUriClassCfgHostPattern_Type())
cvSIPUriClassCfgHostPattern.setMaxAccess(_C)
if mibBuilder.loadTexts:cvSIPUriClassCfgHostPattern.setStatus(_A)
class _CvSIPUriClassCfgPhoneCtxtPattern_Type(CvUriClassPattern):defaultValue=OctetString('')
_CvSIPUriClassCfgPhoneCtxtPattern_Type.__name__=_D
_CvSIPUriClassCfgPhoneCtxtPattern_Object=MibTableColumn
cvSIPUriClassCfgPhoneCtxtPattern=_CvSIPUriClassCfgPhoneCtxtPattern_Object((1,3,6,1,4,1,9,10,99999999,1,1,2,1,3),_CvSIPUriClassCfgPhoneCtxtPattern_Type())
cvSIPUriClassCfgPhoneCtxtPattern.setMaxAccess(_C)
if mibBuilder.loadTexts:cvSIPUriClassCfgPhoneCtxtPattern.setStatus(_A)
_CvTELUriClassCfgTable_Object=MibTable
cvTELUriClassCfgTable=_CvTELUriClassCfgTable_Object((1,3,6,1,4,1,9,10,99999999,1,1,3))
if mibBuilder.loadTexts:cvTELUriClassCfgTable.setStatus(_A)
_CvTELUriClassCfgEntry_Object=MibTableRow
cvTELUriClassCfgEntry=_CvTELUriClassCfgEntry_Object((1,3,6,1,4,1,9,10,99999999,1,1,3,1))
cvTELUriClassCfgEntry.setIndexNames((1,_B,_E))
if mibBuilder.loadTexts:cvTELUriClassCfgEntry.setStatus(_A)
class _CvTELUriClassCfgPhoneNumPattern_Type(CvUriClassPattern):defaultValue=OctetString('')
_CvTELUriClassCfgPhoneNumPattern_Type.__name__=_D
_CvTELUriClassCfgPhoneNumPattern_Object=MibTableColumn
cvTELUriClassCfgPhoneNumPattern=_CvTELUriClassCfgPhoneNumPattern_Object((1,3,6,1,4,1,9,10,99999999,1,1,3,1,1),_CvTELUriClassCfgPhoneNumPattern_Type())
cvTELUriClassCfgPhoneNumPattern.setMaxAccess(_C)
if mibBuilder.loadTexts:cvTELUriClassCfgPhoneNumPattern.setStatus(_A)
class _CvTELUriClassCfgPhoneCtxtPattern_Type(CvUriClassPattern):defaultValue=OctetString('')
_CvTELUriClassCfgPhoneCtxtPattern_Type.__name__=_D
_CvTELUriClassCfgPhoneCtxtPattern_Object=MibTableColumn
cvTELUriClassCfgPhoneCtxtPattern=_CvTELUriClassCfgPhoneCtxtPattern_Object((1,3,6,1,4,1,9,10,99999999,1,1,3,1,2),_CvTELUriClassCfgPhoneCtxtPattern_Type())
cvTELUriClassCfgPhoneCtxtPattern.setMaxAccess(_C)
if mibBuilder.loadTexts:cvTELUriClassCfgPhoneCtxtPattern.setStatus(_A)
_CvCommonUriClassCfgTable_Object=MibTable
cvCommonUriClassCfgTable=_CvCommonUriClassCfgTable_Object((1,3,6,1,4,1,9,10,99999999,1,1,4))
if mibBuilder.loadTexts:cvCommonUriClassCfgTable.setStatus(_A)
_CvCommonUriClassCfgEntry_Object=MibTableRow
cvCommonUriClassCfgEntry=_CvCommonUriClassCfgEntry_Object((1,3,6,1,4,1,9,10,99999999,1,1,4,1))
cvCommonUriClassCfgEntry.setIndexNames((1,_B,_E))
if mibBuilder.loadTexts:cvCommonUriClassCfgEntry.setStatus(_A)
class _CvCommonUriClassCfgURIPattern_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_CvCommonUriClassCfgURIPattern_Type.__name__=_H
_CvCommonUriClassCfgURIPattern_Object=MibTableColumn
cvCommonUriClassCfgURIPattern=_CvCommonUriClassCfgURIPattern_Object((1,3,6,1,4,1,9,10,99999999,1,1,4,1,1),_CvCommonUriClassCfgURIPattern_Type())
cvCommonUriClassCfgURIPattern.setMaxAccess(_C)
if mibBuilder.loadTexts:cvCommonUriClassCfgURIPattern.setStatus(_A)
_CvUriClassSIPGeneralConfig_ObjectIdentity=ObjectIdentity
cvUriClassSIPGeneralConfig=_CvUriClassSIPGeneralConfig_ObjectIdentity((1,3,6,1,4,1,9,10,99999999,1,2))
class _CvUriClassSIPHostPreference_Type(CvUriClassPreference):defaultValue=1
_CvUriClassSIPHostPreference_Type.__name__=_G
_CvUriClassSIPHostPreference_Object=MibScalar
cvUriClassSIPHostPreference=_CvUriClassSIPHostPreference_Object((1,3,6,1,4,1,9,10,99999999,1,2,1),_CvUriClassSIPHostPreference_Type())
cvUriClassSIPHostPreference.setMaxAccess(_C)
if mibBuilder.loadTexts:cvUriClassSIPHostPreference.setStatus(_A)
class _CvUriClassSIPUserIDPreference_Type(CvUriClassPreference):defaultValue=2
_CvUriClassSIPUserIDPreference_Type.__name__=_G
_CvUriClassSIPUserIDPreference_Object=MibScalar
cvUriClassSIPUserIDPreference=_CvUriClassSIPUserIDPreference_Object((1,3,6,1,4,1,9,10,99999999,1,2,2),_CvUriClassSIPUserIDPreference_Type())
cvUriClassSIPUserIDPreference.setMaxAccess(_C)
if mibBuilder.loadTexts:cvUriClassSIPUserIDPreference.setStatus(_A)
_CvUriClassMIBConformance_ObjectIdentity=ObjectIdentity
cvUriClassMIBConformance=_CvUriClassMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,10,99999999,2))
_CvUriClassMIBCompliances_ObjectIdentity=ObjectIdentity
cvUriClassMIBCompliances=_CvUriClassMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,10,99999999,2,1))
_CvUriClassMIBGroups_ObjectIdentity=ObjectIdentity
cvUriClassMIBGroups=_CvUriClassMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,10,99999999,2,2))
cvUriClassGroup=ObjectGroup((1,3,6,1,4,1,9,10,99999999,2,2,1))
cvUriClassGroup.setObjects(*((_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T)))
if mibBuilder.loadTexts:cvUriClassGroup.setStatus(_A)
cvUriClassMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,10,99999999,2,1,1))
cvUriClassMIBCompliance.setObjects((_B,_U))
if mibBuilder.loadTexts:cvUriClassMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'CvUriClassTagIndex':CvUriClassTagIndex,'CvUriClassTag':CvUriClassTag,_D:CvUriClassPattern,_G:CvUriClassPreference,'ciscoVoiceUriClassMIB':ciscoVoiceUriClassMIB,'cvUriClassMIBNotifications':cvUriClassMIBNotifications,'cvUriClassMIBObjects':cvUriClassMIBObjects,'cvUriClass':cvUriClass,'cvUriClassCfgTable':cvUriClassCfgTable,'cvUriClassCfgEntry':cvUriClassCfgEntry,_E:cvUriClassCfgTag,_K:cvUriClassCfgType,_L:cvUriClassCfgStatus,'cvSIPUriClassCfgTable':cvSIPUriClassCfgTable,'cvSIPUriClassCfgEntry':cvSIPUriClassCfgEntry,_M:cvSIPUriClassCfgUserIDPattern,_N:cvSIPUriClassCfgHostPattern,_O:cvSIPUriClassCfgPhoneCtxtPattern,'cvTELUriClassCfgTable':cvTELUriClassCfgTable,'cvTELUriClassCfgEntry':cvTELUriClassCfgEntry,_P:cvTELUriClassCfgPhoneNumPattern,_Q:cvTELUriClassCfgPhoneCtxtPattern,'cvCommonUriClassCfgTable':cvCommonUriClassCfgTable,'cvCommonUriClassCfgEntry':cvCommonUriClassCfgEntry,_R:cvCommonUriClassCfgURIPattern,'cvUriClassSIPGeneralConfig':cvUriClassSIPGeneralConfig,_S:cvUriClassSIPHostPreference,_T:cvUriClassSIPUserIDPreference,'cvUriClassMIBConformance':cvUriClassMIBConformance,'cvUriClassMIBCompliances':cvUriClassMIBCompliances,'cvUriClassMIBCompliance':cvUriClassMIBCompliance,'cvUriClassMIBGroups':cvUriClassMIBGroups,_U:cvUriClassGroup})