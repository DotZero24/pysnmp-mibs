_I='DisplayString'
_H='ifIndex'
_G='IF-MIB'
_F='OctetString'
_E='disable'
_D='enable'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfVoice,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfVoice')
ifIndex,=mibBuilder.importSymbols(_G,_H)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_I,'PhysAddress','TextualConvention')
hpnicfVoiceInterface=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,39,13))
if mibBuilder.loadTexts:hpnicfVoiceInterface.setRevisions(('2007-12-10 17:00',))
_HpnicfVoiceIfObjects_ObjectIdentity=ObjectIdentity
hpnicfVoiceIfObjects=_HpnicfVoiceIfObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,39,13,1))
_HpnicfVoiceIfConfigTable_Object=MibTable
hpnicfVoiceIfConfigTable=_HpnicfVoiceIfConfigTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,39,13,1,1))
if mibBuilder.loadTexts:hpnicfVoiceIfConfigTable.setStatus(_A)
_HpnicfVoiceIfConfigEntry_Object=MibTableRow
hpnicfVoiceIfConfigEntry=_HpnicfVoiceIfConfigEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,39,13,1,1,1))
hpnicfVoiceIfConfigEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:hpnicfVoiceIfConfigEntry.setStatus(_A)
class _HpnicfVoiceIfCfgCngOn_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_HpnicfVoiceIfCfgCngOn_Type.__name__=_C
_HpnicfVoiceIfCfgCngOn_Object=MibTableColumn
hpnicfVoiceIfCfgCngOn=_HpnicfVoiceIfCfgCngOn_Object((1,3,6,1,4,1,11,2,14,11,15,2,39,13,1,1,1,1),_HpnicfVoiceIfCfgCngOn_Type())
hpnicfVoiceIfCfgCngOn.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfVoiceIfCfgCngOn.setStatus(_A)
class _HpnicfVoiceIfCfgNonLinearSwitch_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_HpnicfVoiceIfCfgNonLinearSwitch_Type.__name__=_C
_HpnicfVoiceIfCfgNonLinearSwitch_Object=MibTableColumn
hpnicfVoiceIfCfgNonLinearSwitch=_HpnicfVoiceIfCfgNonLinearSwitch_Object((1,3,6,1,4,1,11,2,14,11,15,2,39,13,1,1,1,2),_HpnicfVoiceIfCfgNonLinearSwitch_Type())
hpnicfVoiceIfCfgNonLinearSwitch.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfVoiceIfCfgNonLinearSwitch.setStatus(_A)
class _HpnicfVoiceIfCfgInputGain_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-140,139))
_HpnicfVoiceIfCfgInputGain_Type.__name__=_C
_HpnicfVoiceIfCfgInputGain_Object=MibTableColumn
hpnicfVoiceIfCfgInputGain=_HpnicfVoiceIfCfgInputGain_Object((1,3,6,1,4,1,11,2,14,11,15,2,39,13,1,1,1,3),_HpnicfVoiceIfCfgInputGain_Type())
hpnicfVoiceIfCfgInputGain.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfVoiceIfCfgInputGain.setStatus(_A)
class _HpnicfVoiceIfCfgOutputGain_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-140,139))
_HpnicfVoiceIfCfgOutputGain_Type.__name__=_C
_HpnicfVoiceIfCfgOutputGain_Object=MibTableColumn
hpnicfVoiceIfCfgOutputGain=_HpnicfVoiceIfCfgOutputGain_Object((1,3,6,1,4,1,11,2,14,11,15,2,39,13,1,1,1,4),_HpnicfVoiceIfCfgOutputGain_Type())
hpnicfVoiceIfCfgOutputGain.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfVoiceIfCfgOutputGain.setStatus(_A)
class _HpnicfVoiceIfCfgEchoCancelSwitch_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_HpnicfVoiceIfCfgEchoCancelSwitch_Type.__name__=_C
_HpnicfVoiceIfCfgEchoCancelSwitch_Object=MibTableColumn
hpnicfVoiceIfCfgEchoCancelSwitch=_HpnicfVoiceIfCfgEchoCancelSwitch_Object((1,3,6,1,4,1,11,2,14,11,15,2,39,13,1,1,1,5),_HpnicfVoiceIfCfgEchoCancelSwitch_Type())
hpnicfVoiceIfCfgEchoCancelSwitch.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfVoiceIfCfgEchoCancelSwitch.setStatus(_A)
class _HpnicfVoiceIfCfgEchoCancelDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,64))
_HpnicfVoiceIfCfgEchoCancelDelay_Type.__name__=_C
_HpnicfVoiceIfCfgEchoCancelDelay_Object=MibTableColumn
hpnicfVoiceIfCfgEchoCancelDelay=_HpnicfVoiceIfCfgEchoCancelDelay_Object((1,3,6,1,4,1,11,2,14,11,15,2,39,13,1,1,1,6),_HpnicfVoiceIfCfgEchoCancelDelay_Type())
hpnicfVoiceIfCfgEchoCancelDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfVoiceIfCfgEchoCancelDelay.setStatus(_A)
class _HpnicfVoiceIfCfgTimerDialInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,300))
_HpnicfVoiceIfCfgTimerDialInterval_Type.__name__=_C
_HpnicfVoiceIfCfgTimerDialInterval_Object=MibTableColumn
hpnicfVoiceIfCfgTimerDialInterval=_HpnicfVoiceIfCfgTimerDialInterval_Object((1,3,6,1,4,1,11,2,14,11,15,2,39,13,1,1,1,7),_HpnicfVoiceIfCfgTimerDialInterval_Type())
hpnicfVoiceIfCfgTimerDialInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfVoiceIfCfgTimerDialInterval.setStatus(_A)
class _HpnicfVoiceIfCfgTimerFirstDial_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,300))
_HpnicfVoiceIfCfgTimerFirstDial_Type.__name__=_C
_HpnicfVoiceIfCfgTimerFirstDial_Object=MibTableColumn
hpnicfVoiceIfCfgTimerFirstDial=_HpnicfVoiceIfCfgTimerFirstDial_Object((1,3,6,1,4,1,11,2,14,11,15,2,39,13,1,1,1,8),_HpnicfVoiceIfCfgTimerFirstDial_Type())
hpnicfVoiceIfCfgTimerFirstDial.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfVoiceIfCfgTimerFirstDial.setStatus(_A)
class _HpnicfVoiceIfCfgPrivateline_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_HpnicfVoiceIfCfgPrivateline_Type.__name__=_I
_HpnicfVoiceIfCfgPrivateline_Object=MibTableColumn
hpnicfVoiceIfCfgPrivateline=_HpnicfVoiceIfCfgPrivateline_Object((1,3,6,1,4,1,11,2,14,11,15,2,39,13,1,1,1,9),_HpnicfVoiceIfCfgPrivateline_Type())
hpnicfVoiceIfCfgPrivateline.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfVoiceIfCfgPrivateline.setStatus(_A)
class _HpnicfVoiceIfCfgRegTone_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(2,3))
_HpnicfVoiceIfCfgRegTone_Type.__name__=_F
_HpnicfVoiceIfCfgRegTone_Object=MibTableColumn
hpnicfVoiceIfCfgRegTone=_HpnicfVoiceIfCfgRegTone_Object((1,3,6,1,4,1,11,2,14,11,15,2,39,13,1,1,1,10),_HpnicfVoiceIfCfgRegTone_Type())
hpnicfVoiceIfCfgRegTone.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfVoiceIfCfgRegTone.setStatus(_A)
mibBuilder.exportSymbols('HPN-ICF-VOICE-IF-MIB',**{'hpnicfVoiceInterface':hpnicfVoiceInterface,'hpnicfVoiceIfObjects':hpnicfVoiceIfObjects,'hpnicfVoiceIfConfigTable':hpnicfVoiceIfConfigTable,'hpnicfVoiceIfConfigEntry':hpnicfVoiceIfConfigEntry,'hpnicfVoiceIfCfgCngOn':hpnicfVoiceIfCfgCngOn,'hpnicfVoiceIfCfgNonLinearSwitch':hpnicfVoiceIfCfgNonLinearSwitch,'hpnicfVoiceIfCfgInputGain':hpnicfVoiceIfCfgInputGain,'hpnicfVoiceIfCfgOutputGain':hpnicfVoiceIfCfgOutputGain,'hpnicfVoiceIfCfgEchoCancelSwitch':hpnicfVoiceIfCfgEchoCancelSwitch,'hpnicfVoiceIfCfgEchoCancelDelay':hpnicfVoiceIfCfgEchoCancelDelay,'hpnicfVoiceIfCfgTimerDialInterval':hpnicfVoiceIfCfgTimerDialInterval,'hpnicfVoiceIfCfgTimerFirstDial':hpnicfVoiceIfCfgTimerFirstDial,'hpnicfVoiceIfCfgPrivateline':hpnicfVoiceIfCfgPrivateline,'hpnicfVoiceIfCfgRegTone':hpnicfVoiceIfCfgRegTone})