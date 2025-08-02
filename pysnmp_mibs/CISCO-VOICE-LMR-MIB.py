_X='cvlToneSignalGroup'
_W='cvlToneClassGroup'
_V='cvlSignalToneDur'
_U='cvlSignalToneAmp'
_T='cvlSignalToneFreq'
_S='cvlSignalToneName'
_R='cvlIdleToneFlag'
_Q='cvlGuardToneAmp'
_P='cvlGuardToneFreq'
_O='cvlDigitalFilter'
_N='cvlClassName'
_M='cvlSignalToneIndex'
_L='cvlSignalToneGroupIndex'
_K='VoiceAmplitude'
_J='VoiceFrequency'
_I='cvlClassIndex'
_H='TruthValue'
_G='Integer32'
_F='not-accessible'
_E='SnmpAdminString'
_D='Unsigned32'
_C='read-only'
_B='CISCO-VOICE-LMR-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_E)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_H)
ciscoVoiceLmrMIB=ModuleIdentity((1,3,6,1,4,1,9,9,510))
if mibBuilder.loadTexts:ciscoVoiceLmrMIB.setRevisions(('2004-10-14 00:00',))
class VoiceFrequency(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4000))
class VoiceAmplitude(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-30,3))
class LmrToneDuration(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,500))
_CvlMIBObjects_ObjectIdentity=ObjectIdentity
cvlMIBObjects=_CvlMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,510,1))
_CvlToneObjects_ObjectIdentity=ObjectIdentity
cvlToneObjects=_CvlToneObjects_ObjectIdentity((1,3,6,1,4,1,9,9,510,1,1))
_CvlClassTable_Object=MibTable
cvlClassTable=_CvlClassTable_Object((1,3,6,1,4,1,9,9,510,1,1,1))
if mibBuilder.loadTexts:cvlClassTable.setStatus(_A)
_CvlClassEntry_Object=MibTableRow
cvlClassEntry=_CvlClassEntry_Object((1,3,6,1,4,1,9,9,510,1,1,1,1))
cvlClassEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:cvlClassEntry.setStatus(_A)
class _CvlClassIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10000))
_CvlClassIndex_Type.__name__=_D
_CvlClassIndex_Object=MibTableColumn
cvlClassIndex=_CvlClassIndex_Object((1,3,6,1,4,1,9,9,510,1,1,1,1,1),_CvlClassIndex_Type())
cvlClassIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:cvlClassIndex.setStatus(_A)
class _CvlClassName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,19))
_CvlClassName_Type.__name__=_E
_CvlClassName_Object=MibTableColumn
cvlClassName=_CvlClassName_Object((1,3,6,1,4,1,9,9,510,1,1,1,1,2),_CvlClassName_Type())
cvlClassName.setMaxAccess(_C)
if mibBuilder.loadTexts:cvlClassName.setStatus(_A)
class _CvlDigitalFilter_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('digitalFilterNone',0),('digitalFilter1950HZ',1),('digitalFilter2175HZ',2)))
_CvlDigitalFilter_Type.__name__=_G
_CvlDigitalFilter_Object=MibTableColumn
cvlDigitalFilter=_CvlDigitalFilter_Object((1,3,6,1,4,1,9,9,510,1,1,1,1,3),_CvlDigitalFilter_Type())
cvlDigitalFilter.setMaxAccess(_C)
if mibBuilder.loadTexts:cvlDigitalFilter.setStatus(_A)
class _CvlGuardToneFreq_Type(VoiceFrequency):defaultValue=0
_CvlGuardToneFreq_Type.__name__=_J
_CvlGuardToneFreq_Object=MibTableColumn
cvlGuardToneFreq=_CvlGuardToneFreq_Object((1,3,6,1,4,1,9,9,510,1,1,1,1,4),_CvlGuardToneFreq_Type())
cvlGuardToneFreq.setMaxAccess(_C)
if mibBuilder.loadTexts:cvlGuardToneFreq.setStatus(_A)
class _CvlGuardToneAmp_Type(VoiceAmplitude):defaultValue=0
_CvlGuardToneAmp_Type.__name__=_K
_CvlGuardToneAmp_Object=MibTableColumn
cvlGuardToneAmp=_CvlGuardToneAmp_Object((1,3,6,1,4,1,9,9,510,1,1,1,1,5),_CvlGuardToneAmp_Type())
cvlGuardToneAmp.setMaxAccess(_C)
if mibBuilder.loadTexts:cvlGuardToneAmp.setStatus(_A)
class _CvlIdleToneFlag_Type(TruthValue):defaultValue=2
_CvlIdleToneFlag_Type.__name__=_H
_CvlIdleToneFlag_Object=MibTableColumn
cvlIdleToneFlag=_CvlIdleToneFlag_Object((1,3,6,1,4,1,9,9,510,1,1,1,1,6),_CvlIdleToneFlag_Type())
cvlIdleToneFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:cvlIdleToneFlag.setStatus(_A)
_CvlSignalToneTable_Object=MibTable
cvlSignalToneTable=_CvlSignalToneTable_Object((1,3,6,1,4,1,9,9,510,1,1,2))
if mibBuilder.loadTexts:cvlSignalToneTable.setStatus(_A)
_CvlSignalToneEntry_Object=MibTableRow
cvlSignalToneEntry=_CvlSignalToneEntry_Object((1,3,6,1,4,1,9,9,510,1,1,2,1))
cvlSignalToneEntry.setIndexNames((0,_B,_L),(0,_B,_M))
if mibBuilder.loadTexts:cvlSignalToneEntry.setStatus(_A)
class _CvlSignalToneGroupIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10000))
_CvlSignalToneGroupIndex_Type.__name__=_D
_CvlSignalToneGroupIndex_Object=MibTableColumn
cvlSignalToneGroupIndex=_CvlSignalToneGroupIndex_Object((1,3,6,1,4,1,9,9,510,1,1,2,1,1),_CvlSignalToneGroupIndex_Type())
cvlSignalToneGroupIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:cvlSignalToneGroupIndex.setStatus(_A)
class _CvlSignalToneIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_CvlSignalToneIndex_Type.__name__=_D
_CvlSignalToneIndex_Object=MibTableColumn
cvlSignalToneIndex=_CvlSignalToneIndex_Object((1,3,6,1,4,1,9,9,510,1,1,2,1,2),_CvlSignalToneIndex_Type())
cvlSignalToneIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:cvlSignalToneIndex.setStatus(_A)
class _CvlSignalToneName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,19))
_CvlSignalToneName_Type.__name__=_E
_CvlSignalToneName_Object=MibTableColumn
cvlSignalToneName=_CvlSignalToneName_Object((1,3,6,1,4,1,9,9,510,1,1,2,1,3),_CvlSignalToneName_Type())
cvlSignalToneName.setMaxAccess(_C)
if mibBuilder.loadTexts:cvlSignalToneName.setStatus(_A)
_CvlSignalToneFreq_Type=VoiceFrequency
_CvlSignalToneFreq_Object=MibTableColumn
cvlSignalToneFreq=_CvlSignalToneFreq_Object((1,3,6,1,4,1,9,9,510,1,1,2,1,4),_CvlSignalToneFreq_Type())
cvlSignalToneFreq.setMaxAccess(_C)
if mibBuilder.loadTexts:cvlSignalToneFreq.setStatus(_A)
_CvlSignalToneAmp_Type=VoiceAmplitude
_CvlSignalToneAmp_Object=MibTableColumn
cvlSignalToneAmp=_CvlSignalToneAmp_Object((1,3,6,1,4,1,9,9,510,1,1,2,1,5),_CvlSignalToneAmp_Type())
cvlSignalToneAmp.setMaxAccess(_C)
if mibBuilder.loadTexts:cvlSignalToneAmp.setStatus(_A)
_CvlSignalToneDur_Type=LmrToneDuration
_CvlSignalToneDur_Object=MibTableColumn
cvlSignalToneDur=_CvlSignalToneDur_Object((1,3,6,1,4,1,9,9,510,1,1,2,1,6),_CvlSignalToneDur_Type())
cvlSignalToneDur.setMaxAccess(_C)
if mibBuilder.loadTexts:cvlSignalToneDur.setStatus(_A)
_CvlMIBConformance_ObjectIdentity=ObjectIdentity
cvlMIBConformance=_CvlMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,510,2))
_CvlMIBCompliances_ObjectIdentity=ObjectIdentity
cvlMIBCompliances=_CvlMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,510,2,1))
_CvlMIBGroups_ObjectIdentity=ObjectIdentity
cvlMIBGroups=_CvlMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,510,2,2))
cvlToneClassGroup=ObjectGroup((1,3,6,1,4,1,9,9,510,2,2,1))
cvlToneClassGroup.setObjects(*((_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:cvlToneClassGroup.setStatus(_A)
cvlToneSignalGroup=ObjectGroup((1,3,6,1,4,1,9,9,510,2,2,2))
cvlToneSignalGroup.setObjects(*((_B,_S),(_B,_T),(_B,_U),(_B,_V)))
if mibBuilder.loadTexts:cvlToneSignalGroup.setStatus(_A)
cvlMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,510,2,1,1))
cvlMIBCompliance.setObjects(*((_B,_W),(_B,_X)))
if mibBuilder.loadTexts:cvlMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_J:VoiceFrequency,_K:VoiceAmplitude,'LmrToneDuration':LmrToneDuration,'ciscoVoiceLmrMIB':ciscoVoiceLmrMIB,'cvlMIBObjects':cvlMIBObjects,'cvlToneObjects':cvlToneObjects,'cvlClassTable':cvlClassTable,'cvlClassEntry':cvlClassEntry,_I:cvlClassIndex,_N:cvlClassName,_O:cvlDigitalFilter,_P:cvlGuardToneFreq,_Q:cvlGuardToneAmp,_R:cvlIdleToneFlag,'cvlSignalToneTable':cvlSignalToneTable,'cvlSignalToneEntry':cvlSignalToneEntry,_L:cvlSignalToneGroupIndex,_M:cvlSignalToneIndex,_S:cvlSignalToneName,_T:cvlSignalToneFreq,_U:cvlSignalToneAmp,_V:cvlSignalToneDur,'cvlMIBConformance':cvlMIBConformance,'cvlMIBCompliances':cvlMIBCompliances,'cvlMIBCompliance':cvlMIBCompliance,'cvlMIBGroups':cvlMIBGroups,_W:cvlToneClassGroup,_X:cvlToneSignalGroup})