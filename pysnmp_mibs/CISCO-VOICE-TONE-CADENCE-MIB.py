_Z='cvtcToneConfigGroup'
_Y='cvtcProgrammableToneRowStatus'
_X='cvtcProgrammableToneStorageType'
_W='cvtcProgrammableToneDuration'
_V='cvtcProgrammableToneCadence'
_U='cvtcProgrammableToneAmplitude'
_T='cvtcProgrammableToneFrequency'
_S='cvtcToneIdRowStatus'
_R='cvtcToneName'
_Q='cvtcTonePlanRowStatus'
_P='cvtcTonePlanStorageType'
_O='cvtcTonePlanFileName'
_N='cvtcTonePlanVersion'
_M='cvtcTonePlanCountry'
_L='cvtcTonePlanVifCount'
_K='read-only'
_J='not-accessible'
_I='cvtcToneId'
_H='cvtcTonePlanId'
_G='SnmpAdminString'
_F='Unsigned32'
_E='cmgwIndex'
_D='CISCO-MEDIA-GATEWAY-MIB'
_C='read-create'
_B='CISCO-VOICE-TONE-CADENCE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
CVoiceTonePlanIndex,cmgwIndex=mibBuilder.importSymbols(_D,'CVoiceTonePlanIndex',_E)
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CountryCode,=mibBuilder.importSymbols('CISCO-TC','CountryCode')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_G)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','StorageType','TextualConvention')
ciscoVoiceToneCadenceMIB=ModuleIdentity((1,3,6,1,4,1,9,9,356))
if mibBuilder.loadTexts:ciscoVoiceToneCadenceMIB.setRevisions(('2003-05-28 00:00',))
class CToneFrequency(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
class CToneAmplitude(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,64))
class CToneCadence(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,64))
_CiscoVoiceToneCadenceMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoVoiceToneCadenceMIBNotifs=_CiscoVoiceToneCadenceMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,356,0))
_CiscoVoiceToneCadenceMIBObjects_ObjectIdentity=ObjectIdentity
ciscoVoiceToneCadenceMIBObjects=_CiscoVoiceToneCadenceMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,356,1))
_CVoiceToneCadenceConfig_ObjectIdentity=ObjectIdentity
cVoiceToneCadenceConfig=_CVoiceToneCadenceConfig_ObjectIdentity((1,3,6,1,4,1,9,9,356,1,1))
_CvtcTonePlanTable_Object=MibTable
cvtcTonePlanTable=_CvtcTonePlanTable_Object((1,3,6,1,4,1,9,9,356,1,1,1))
if mibBuilder.loadTexts:cvtcTonePlanTable.setStatus(_A)
_CvtcTonePlanEntry_Object=MibTableRow
cvtcTonePlanEntry=_CvtcTonePlanEntry_Object((1,3,6,1,4,1,9,9,356,1,1,1,1))
cvtcTonePlanEntry.setIndexNames((0,_D,_E),(0,_B,_H))
if mibBuilder.loadTexts:cvtcTonePlanEntry.setStatus(_A)
_CvtcTonePlanId_Type=CVoiceTonePlanIndex
_CvtcTonePlanId_Object=MibTableColumn
cvtcTonePlanId=_CvtcTonePlanId_Object((1,3,6,1,4,1,9,9,356,1,1,1,1,1),_CvtcTonePlanId_Type())
cvtcTonePlanId.setMaxAccess(_J)
if mibBuilder.loadTexts:cvtcTonePlanId.setStatus(_A)
_CvtcTonePlanVifCount_Type=Gauge32
_CvtcTonePlanVifCount_Object=MibTableColumn
cvtcTonePlanVifCount=_CvtcTonePlanVifCount_Object((1,3,6,1,4,1,9,9,356,1,1,1,1,2),_CvtcTonePlanVifCount_Type())
cvtcTonePlanVifCount.setMaxAccess(_K)
if mibBuilder.loadTexts:cvtcTonePlanVifCount.setStatus(_A)
_CvtcTonePlanCountry_Type=CountryCode
_CvtcTonePlanCountry_Object=MibTableColumn
cvtcTonePlanCountry=_CvtcTonePlanCountry_Object((1,3,6,1,4,1,9,9,356,1,1,1,1,3),_CvtcTonePlanCountry_Type())
cvtcTonePlanCountry.setMaxAccess(_C)
if mibBuilder.loadTexts:cvtcTonePlanCountry.setStatus(_A)
class _CvtcTonePlanVersion_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CvtcTonePlanVersion_Type.__name__=_F
_CvtcTonePlanVersion_Object=MibTableColumn
cvtcTonePlanVersion=_CvtcTonePlanVersion_Object((1,3,6,1,4,1,9,9,356,1,1,1,1,4),_CvtcTonePlanVersion_Type())
cvtcTonePlanVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:cvtcTonePlanVersion.setStatus(_A)
class _CvtcTonePlanFileName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_CvtcTonePlanFileName_Type.__name__=_G
_CvtcTonePlanFileName_Object=MibTableColumn
cvtcTonePlanFileName=_CvtcTonePlanFileName_Object((1,3,6,1,4,1,9,9,356,1,1,1,1,5),_CvtcTonePlanFileName_Type())
cvtcTonePlanFileName.setMaxAccess(_C)
if mibBuilder.loadTexts:cvtcTonePlanFileName.setStatus(_A)
_CvtcTonePlanStorageType_Type=StorageType
_CvtcTonePlanStorageType_Object=MibTableColumn
cvtcTonePlanStorageType=_CvtcTonePlanStorageType_Object((1,3,6,1,4,1,9,9,356,1,1,1,1,6),_CvtcTonePlanStorageType_Type())
cvtcTonePlanStorageType.setMaxAccess(_K)
if mibBuilder.loadTexts:cvtcTonePlanStorageType.setStatus(_A)
_CvtcTonePlanRowStatus_Type=RowStatus
_CvtcTonePlanRowStatus_Object=MibTableColumn
cvtcTonePlanRowStatus=_CvtcTonePlanRowStatus_Object((1,3,6,1,4,1,9,9,356,1,1,1,1,7),_CvtcTonePlanRowStatus_Type())
cvtcTonePlanRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cvtcTonePlanRowStatus.setStatus(_A)
_CvtcToneIdTable_Object=MibTable
cvtcToneIdTable=_CvtcToneIdTable_Object((1,3,6,1,4,1,9,9,356,1,1,2))
if mibBuilder.loadTexts:cvtcToneIdTable.setStatus(_A)
_CvtcToneIdEntry_Object=MibTableRow
cvtcToneIdEntry=_CvtcToneIdEntry_Object((1,3,6,1,4,1,9,9,356,1,1,2,1))
cvtcToneIdEntry.setIndexNames((0,_D,_E),(0,_B,_I))
if mibBuilder.loadTexts:cvtcToneIdEntry.setStatus(_A)
class _CvtcToneId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CvtcToneId_Type.__name__=_F
_CvtcToneId_Object=MibTableColumn
cvtcToneId=_CvtcToneId_Object((1,3,6,1,4,1,9,9,356,1,1,2,1,1),_CvtcToneId_Type())
cvtcToneId.setMaxAccess(_J)
if mibBuilder.loadTexts:cvtcToneId.setStatus(_A)
class _CvtcToneName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_CvtcToneName_Type.__name__=_G
_CvtcToneName_Object=MibTableColumn
cvtcToneName=_CvtcToneName_Object((1,3,6,1,4,1,9,9,356,1,1,2,1,2),_CvtcToneName_Type())
cvtcToneName.setMaxAccess(_C)
if mibBuilder.loadTexts:cvtcToneName.setStatus(_A)
_CvtcToneIdRowStatus_Type=RowStatus
_CvtcToneIdRowStatus_Object=MibTableColumn
cvtcToneIdRowStatus=_CvtcToneIdRowStatus_Object((1,3,6,1,4,1,9,9,356,1,1,2,1,3),_CvtcToneIdRowStatus_Type())
cvtcToneIdRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cvtcToneIdRowStatus.setStatus(_A)
_CvtcProgrammableToneTable_Object=MibTable
cvtcProgrammableToneTable=_CvtcProgrammableToneTable_Object((1,3,6,1,4,1,9,9,356,1,1,3))
if mibBuilder.loadTexts:cvtcProgrammableToneTable.setStatus(_A)
_CvtcProgrammableToneEntry_Object=MibTableRow
cvtcProgrammableToneEntry=_CvtcProgrammableToneEntry_Object((1,3,6,1,4,1,9,9,356,1,1,3,1))
cvtcProgrammableToneEntry.setIndexNames((0,_D,_E),(0,_B,_H),(0,_B,_I))
if mibBuilder.loadTexts:cvtcProgrammableToneEntry.setStatus(_A)
_CvtcProgrammableToneFrequency_Type=CToneFrequency
_CvtcProgrammableToneFrequency_Object=MibTableColumn
cvtcProgrammableToneFrequency=_CvtcProgrammableToneFrequency_Object((1,3,6,1,4,1,9,9,356,1,1,3,1,1),_CvtcProgrammableToneFrequency_Type())
cvtcProgrammableToneFrequency.setMaxAccess(_C)
if mibBuilder.loadTexts:cvtcProgrammableToneFrequency.setStatus(_A)
_CvtcProgrammableToneAmplitude_Type=CToneAmplitude
_CvtcProgrammableToneAmplitude_Object=MibTableColumn
cvtcProgrammableToneAmplitude=_CvtcProgrammableToneAmplitude_Object((1,3,6,1,4,1,9,9,356,1,1,3,1,2),_CvtcProgrammableToneAmplitude_Type())
cvtcProgrammableToneAmplitude.setMaxAccess(_C)
if mibBuilder.loadTexts:cvtcProgrammableToneAmplitude.setStatus(_A)
_CvtcProgrammableToneCadence_Type=CToneCadence
_CvtcProgrammableToneCadence_Object=MibTableColumn
cvtcProgrammableToneCadence=_CvtcProgrammableToneCadence_Object((1,3,6,1,4,1,9,9,356,1,1,3,1,3),_CvtcProgrammableToneCadence_Type())
cvtcProgrammableToneCadence.setMaxAccess(_C)
if mibBuilder.loadTexts:cvtcProgrammableToneCadence.setStatus(_A)
class _CvtcProgrammableToneDuration_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CvtcProgrammableToneDuration_Type.__name__=_F
_CvtcProgrammableToneDuration_Object=MibTableColumn
cvtcProgrammableToneDuration=_CvtcProgrammableToneDuration_Object((1,3,6,1,4,1,9,9,356,1,1,3,1,4),_CvtcProgrammableToneDuration_Type())
cvtcProgrammableToneDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:cvtcProgrammableToneDuration.setStatus(_A)
if mibBuilder.loadTexts:cvtcProgrammableToneDuration.setUnits('milliseconds')
_CvtcProgrammableToneStorageType_Type=StorageType
_CvtcProgrammableToneStorageType_Object=MibTableColumn
cvtcProgrammableToneStorageType=_CvtcProgrammableToneStorageType_Object((1,3,6,1,4,1,9,9,356,1,1,3,1,5),_CvtcProgrammableToneStorageType_Type())
cvtcProgrammableToneStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:cvtcProgrammableToneStorageType.setStatus(_A)
_CvtcProgrammableToneRowStatus_Type=RowStatus
_CvtcProgrammableToneRowStatus_Object=MibTableColumn
cvtcProgrammableToneRowStatus=_CvtcProgrammableToneRowStatus_Object((1,3,6,1,4,1,9,9,356,1,1,3,1,6),_CvtcProgrammableToneRowStatus_Type())
cvtcProgrammableToneRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cvtcProgrammableToneRowStatus.setStatus(_A)
_CiscoVoiceToneCadenceMIBConform_ObjectIdentity=ObjectIdentity
ciscoVoiceToneCadenceMIBConform=_CiscoVoiceToneCadenceMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,356,3))
_CVoiceToneCadenceCompliances_ObjectIdentity=ObjectIdentity
cVoiceToneCadenceCompliances=_CVoiceToneCadenceCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,356,3,1))
_CVoiceToneCadenceGroups_ObjectIdentity=ObjectIdentity
cVoiceToneCadenceGroups=_CVoiceToneCadenceGroups_ObjectIdentity((1,3,6,1,4,1,9,9,356,3,2))
cvtcToneConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,356,3,2,1))
cvtcToneConfigGroup.setObjects(*((_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y)))
if mibBuilder.loadTexts:cvtcToneConfigGroup.setStatus(_A)
cVoiceToneCadenceCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,356,3,1,1))
cVoiceToneCadenceCompliance.setObjects((_B,_Z))
if mibBuilder.loadTexts:cVoiceToneCadenceCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'CToneFrequency':CToneFrequency,'CToneAmplitude':CToneAmplitude,'CToneCadence':CToneCadence,'ciscoVoiceToneCadenceMIB':ciscoVoiceToneCadenceMIB,'ciscoVoiceToneCadenceMIBNotifs':ciscoVoiceToneCadenceMIBNotifs,'ciscoVoiceToneCadenceMIBObjects':ciscoVoiceToneCadenceMIBObjects,'cVoiceToneCadenceConfig':cVoiceToneCadenceConfig,'cvtcTonePlanTable':cvtcTonePlanTable,'cvtcTonePlanEntry':cvtcTonePlanEntry,_H:cvtcTonePlanId,_L:cvtcTonePlanVifCount,_M:cvtcTonePlanCountry,_N:cvtcTonePlanVersion,_O:cvtcTonePlanFileName,_P:cvtcTonePlanStorageType,_Q:cvtcTonePlanRowStatus,'cvtcToneIdTable':cvtcToneIdTable,'cvtcToneIdEntry':cvtcToneIdEntry,_I:cvtcToneId,_R:cvtcToneName,_S:cvtcToneIdRowStatus,'cvtcProgrammableToneTable':cvtcProgrammableToneTable,'cvtcProgrammableToneEntry':cvtcProgrammableToneEntry,_T:cvtcProgrammableToneFrequency,_U:cvtcProgrammableToneAmplitude,_V:cvtcProgrammableToneCadence,_W:cvtcProgrammableToneDuration,_X:cvtcProgrammableToneStorageType,_Y:cvtcProgrammableToneRowStatus,'ciscoVoiceToneCadenceMIBConform':ciscoVoiceToneCadenceMIBConform,'cVoiceToneCadenceCompliances':cVoiceToneCadenceCompliances,'cVoiceToneCadenceCompliance':cVoiceToneCadenceCompliance,'cVoiceToneCadenceGroups':cVoiceToneCadenceGroups,_Z:cvtcToneConfigGroup})