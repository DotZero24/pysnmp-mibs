_K='hwVoIfConfigGroupNumber'
_J='hwVoIfConfigPortNumber'
_I='obsolete'
_H='disable'
_G='enable'
_F='HUAWEI-VO-IF-MIB'
_E='read-only'
_D='OctetString'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
voice,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','voice')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
hwVoiceIfMIB=ModuleIdentity((1,3,6,1,4,1,2011,5,25,1,2))
if mibBuilder.loadTexts:hwVoiceIfMIB.setRevisions(('2004-04-08 13:45',))
_HwVoIfObjects_ObjectIdentity=ObjectIdentity
hwVoIfObjects=_HwVoIfObjects_ObjectIdentity((1,3,6,1,4,1,2011,5,25,1,2,1))
_HwVoIfConfigTable_Object=MibTable
hwVoIfConfigTable=_HwVoIfConfigTable_Object((1,3,6,1,4,1,2011,5,25,1,2,1,1))
if mibBuilder.loadTexts:hwVoIfConfigTable.setStatus(_A)
_HwVoIfConfigEntry_Object=MibTableRow
hwVoIfConfigEntry=_HwVoIfConfigEntry_Object((1,3,6,1,4,1,2011,5,25,1,2,1,1,1))
hwVoIfConfigEntry.setIndexNames((0,_F,_J),(0,_F,_K))
if mibBuilder.loadTexts:hwVoIfConfigEntry.setStatus(_A)
_HwVoIfConfigPortNumber_Type=Integer32
_HwVoIfConfigPortNumber_Object=MibTableColumn
hwVoIfConfigPortNumber=_HwVoIfConfigPortNumber_Object((1,3,6,1,4,1,2011,5,25,1,2,1,1,1,1),_HwVoIfConfigPortNumber_Type())
hwVoIfConfigPortNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:hwVoIfConfigPortNumber.setStatus(_A)
_HwVoIfConfigGroupNumber_Type=Integer32
_HwVoIfConfigGroupNumber_Object=MibTableColumn
hwVoIfConfigGroupNumber=_HwVoIfConfigGroupNumber_Object((1,3,6,1,4,1,2011,5,25,1,2,1,1,1,2),_HwVoIfConfigGroupNumber_Type())
hwVoIfConfigGroupNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:hwVoIfConfigGroupNumber.setStatus(_A)
class _HwVoIfConfigCngOn_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_HwVoIfConfigCngOn_Type.__name__=_B
_HwVoIfConfigCngOn_Object=MibTableColumn
hwVoIfConfigCngOn=_HwVoIfConfigCngOn_Object((1,3,6,1,4,1,2011,5,25,1,2,1,1,1,3),_HwVoIfConfigCngOn_Type())
hwVoIfConfigCngOn.setMaxAccess(_C)
if mibBuilder.loadTexts:hwVoIfConfigCngOn.setStatus(_A)
class _HwVoIfConfigNonLinearProcessSwitch_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_HwVoIfConfigNonLinearProcessSwitch_Type.__name__=_B
_HwVoIfConfigNonLinearProcessSwitch_Object=MibTableColumn
hwVoIfConfigNonLinearProcessSwitch=_HwVoIfConfigNonLinearProcessSwitch_Object((1,3,6,1,4,1,2011,5,25,1,2,1,1,1,4),_HwVoIfConfigNonLinearProcessSwitch_Type())
hwVoIfConfigNonLinearProcessSwitch.setMaxAccess(_C)
if mibBuilder.loadTexts:hwVoIfConfigNonLinearProcessSwitch.setStatus(_I)
class _HwVoIfConfigMusicThreshold_Type(Integer32):defaultValue=-38;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-70,-30))
_HwVoIfConfigMusicThreshold_Type.__name__=_B
_HwVoIfConfigMusicThreshold_Object=MibTableColumn
hwVoIfConfigMusicThreshold=_HwVoIfConfigMusicThreshold_Object((1,3,6,1,4,1,2011,5,25,1,2,1,1,1,5),_HwVoIfConfigMusicThreshold_Type())
hwVoIfConfigMusicThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:hwVoIfConfigMusicThreshold.setStatus(_I)
class _HwVoIfConfigInputGain_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-14,14))
_HwVoIfConfigInputGain_Type.__name__=_B
_HwVoIfConfigInputGain_Object=MibTableColumn
hwVoIfConfigInputGain=_HwVoIfConfigInputGain_Object((1,3,6,1,4,1,2011,5,25,1,2,1,1,1,6),_HwVoIfConfigInputGain_Type())
hwVoIfConfigInputGain.setMaxAccess(_C)
if mibBuilder.loadTexts:hwVoIfConfigInputGain.setStatus(_A)
class _HwVoIfConfigOutputGain_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-14,14))
_HwVoIfConfigOutputGain_Type.__name__=_B
_HwVoIfConfigOutputGain_Object=MibTableColumn
hwVoIfConfigOutputGain=_HwVoIfConfigOutputGain_Object((1,3,6,1,4,1,2011,5,25,1,2,1,1,1,7),_HwVoIfConfigOutputGain_Type())
hwVoIfConfigOutputGain.setMaxAccess(_C)
if mibBuilder.loadTexts:hwVoIfConfigOutputGain.setStatus(_A)
class _HwVoIfConfigEchoCancellationSwitch_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_HwVoIfConfigEchoCancellationSwitch_Type.__name__=_B
_HwVoIfConfigEchoCancellationSwitch_Object=MibTableColumn
hwVoIfConfigEchoCancellationSwitch=_HwVoIfConfigEchoCancellationSwitch_Object((1,3,6,1,4,1,2011,5,25,1,2,1,1,1,8),_HwVoIfConfigEchoCancellationSwitch_Type())
hwVoIfConfigEchoCancellationSwitch.setMaxAccess(_C)
if mibBuilder.loadTexts:hwVoIfConfigEchoCancellationSwitch.setStatus(_A)
class _HwVoIfConfigEchoCancellationCoverage_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('echoCancelCoverage16ms',1),('echoCancelCoverage24ms',2),('echoCancelCoverage32ms',3)))
_HwVoIfConfigEchoCancellationCoverage_Type.__name__=_B
_HwVoIfConfigEchoCancellationCoverage_Object=MibTableColumn
hwVoIfConfigEchoCancellationCoverage=_HwVoIfConfigEchoCancellationCoverage_Object((1,3,6,1,4,1,2011,5,25,1,2,1,1,1,9),_HwVoIfConfigEchoCancellationCoverage_Type())
hwVoIfConfigEchoCancellationCoverage.setMaxAccess(_C)
if mibBuilder.loadTexts:hwVoIfConfigEchoCancellationCoverage.setStatus(_I)
class _HwVoIfConfigEchoCancellationDelay_Type(Integer32):defaultValue=32;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,64))
_HwVoIfConfigEchoCancellationDelay_Type.__name__=_B
_HwVoIfConfigEchoCancellationDelay_Object=MibTableColumn
hwVoIfConfigEchoCancellationDelay=_HwVoIfConfigEchoCancellationDelay_Object((1,3,6,1,4,1,2011,5,25,1,2,1,1,1,10),_HwVoIfConfigEchoCancellationDelay_Type())
hwVoIfConfigEchoCancellationDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:hwVoIfConfigEchoCancellationDelay.setStatus(_A)
class _HwVoIfConfigPlarNumber_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_HwVoIfConfigPlarNumber_Type.__name__=_D
_HwVoIfConfigPlarNumber_Object=MibTableColumn
hwVoIfConfigPlarNumber=_HwVoIfConfigPlarNumber_Object((1,3,6,1,4,1,2011,5,25,1,2,1,1,1,11),_HwVoIfConfigPlarNumber_Type())
hwVoIfConfigPlarNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:hwVoIfConfigPlarNumber.setStatus(_A)
class _HwVoIfConfigRegionalTone_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(2,2))
_HwVoIfConfigRegionalTone_Type.__name__=_D
_HwVoIfConfigRegionalTone_Object=MibTableColumn
hwVoIfConfigRegionalTone=_HwVoIfConfigRegionalTone_Object((1,3,6,1,4,1,2011,5,25,1,2,1,1,1,12),_HwVoIfConfigRegionalTone_Type())
hwVoIfConfigRegionalTone.setMaxAccess(_E)
if mibBuilder.loadTexts:hwVoIfConfigRegionalTone.setStatus(_A)
class _HwVoIfConfigDescription_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HwVoIfConfigDescription_Type.__name__=_D
_HwVoIfConfigDescription_Object=MibTableColumn
hwVoIfConfigDescription=_HwVoIfConfigDescription_Object((1,3,6,1,4,1,2011,5,25,1,2,1,1,1,13),_HwVoIfConfigDescription_Type())
hwVoIfConfigDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:hwVoIfConfigDescription.setStatus(_A)
class _HwVoIfConfigStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_HwVoIfConfigStatus_Type.__name__=_B
_HwVoIfConfigStatus_Object=MibTableColumn
hwVoIfConfigStatus=_HwVoIfConfigStatus_Object((1,3,6,1,4,1,2011,5,25,1,2,1,1,1,14),_HwVoIfConfigStatus_Type())
hwVoIfConfigStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:hwVoIfConfigStatus.setStatus(_A)
class _HwVoIfConfigDtmfThreshold_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('sensitivity',1),('insensitivty',2)))
_HwVoIfConfigDtmfThreshold_Type.__name__=_B
_HwVoIfConfigDtmfThreshold_Object=MibTableColumn
hwVoIfConfigDtmfThreshold=_HwVoIfConfigDtmfThreshold_Object((1,3,6,1,4,1,2011,5,25,1,2,1,1,1,15),_HwVoIfConfigDtmfThreshold_Type())
hwVoIfConfigDtmfThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:hwVoIfConfigDtmfThreshold.setStatus(_A)
class _HwVoIfConfigCallingNumSubstRule_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_HwVoIfConfigCallingNumSubstRule_Type.__name__=_B
_HwVoIfConfigCallingNumSubstRule_Object=MibTableColumn
hwVoIfConfigCallingNumSubstRule=_HwVoIfConfigCallingNumSubstRule_Object((1,3,6,1,4,1,2011,5,25,1,2,1,1,1,16),_HwVoIfConfigCallingNumSubstRule_Type())
hwVoIfConfigCallingNumSubstRule.setMaxAccess(_C)
if mibBuilder.loadTexts:hwVoIfConfigCallingNumSubstRule.setStatus(_A)
class _HwVoIfConfigCalledNumSubstRule_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_HwVoIfConfigCalledNumSubstRule_Type.__name__=_B
_HwVoIfConfigCalledNumSubstRule_Object=MibTableColumn
hwVoIfConfigCalledNumSubstRule=_HwVoIfConfigCalledNumSubstRule_Object((1,3,6,1,4,1,2011,5,25,1,2,1,1,1,17),_HwVoIfConfigCalledNumSubstRule_Type())
hwVoIfConfigCalledNumSubstRule.setMaxAccess(_C)
if mibBuilder.loadTexts:hwVoIfConfigCalledNumSubstRule.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'hwVoiceIfMIB':hwVoiceIfMIB,'hwVoIfObjects':hwVoIfObjects,'hwVoIfConfigTable':hwVoIfConfigTable,'hwVoIfConfigEntry':hwVoIfConfigEntry,_J:hwVoIfConfigPortNumber,_K:hwVoIfConfigGroupNumber,'hwVoIfConfigCngOn':hwVoIfConfigCngOn,'hwVoIfConfigNonLinearProcessSwitch':hwVoIfConfigNonLinearProcessSwitch,'hwVoIfConfigMusicThreshold':hwVoIfConfigMusicThreshold,'hwVoIfConfigInputGain':hwVoIfConfigInputGain,'hwVoIfConfigOutputGain':hwVoIfConfigOutputGain,'hwVoIfConfigEchoCancellationSwitch':hwVoIfConfigEchoCancellationSwitch,'hwVoIfConfigEchoCancellationCoverage':hwVoIfConfigEchoCancellationCoverage,'hwVoIfConfigEchoCancellationDelay':hwVoIfConfigEchoCancellationDelay,'hwVoIfConfigPlarNumber':hwVoIfConfigPlarNumber,'hwVoIfConfigRegionalTone':hwVoIfConfigRegionalTone,'hwVoIfConfigDescription':hwVoIfConfigDescription,'hwVoIfConfigStatus':hwVoIfConfigStatus,'hwVoIfConfigDtmfThreshold':hwVoIfConfigDtmfThreshold,'hwVoIfConfigCallingNumSubstRule':hwVoIfConfigCallingNumSubstRule,'hwVoIfConfigCalledNumSubstRule':hwVoIfConfigCalledNumSubstRule})