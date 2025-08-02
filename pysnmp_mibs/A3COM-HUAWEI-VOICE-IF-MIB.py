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
h3cVoice,=mibBuilder.importSymbols('A3COM-HUAWEI-OID-MIB','h3cVoice')
ifIndex,=mibBuilder.importSymbols(_G,_H)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_I,'PhysAddress','TextualConvention')
h3cVoiceInterface=ModuleIdentity((1,3,6,1,4,1,43,45,1,10,2,39,13))
if mibBuilder.loadTexts:h3cVoiceInterface.setRevisions(('2007-12-10 17:00',))
_H3cVoiceIfObjects_ObjectIdentity=ObjectIdentity
h3cVoiceIfObjects=_H3cVoiceIfObjects_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,39,13,1))
_H3cVoiceIfConfigTable_Object=MibTable
h3cVoiceIfConfigTable=_H3cVoiceIfConfigTable_Object((1,3,6,1,4,1,43,45,1,10,2,39,13,1,1))
if mibBuilder.loadTexts:h3cVoiceIfConfigTable.setStatus(_A)
_H3cVoiceIfConfigEntry_Object=MibTableRow
h3cVoiceIfConfigEntry=_H3cVoiceIfConfigEntry_Object((1,3,6,1,4,1,43,45,1,10,2,39,13,1,1,1))
h3cVoiceIfConfigEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:h3cVoiceIfConfigEntry.setStatus(_A)
class _H3cVoiceIfCfgCngOn_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_H3cVoiceIfCfgCngOn_Type.__name__=_C
_H3cVoiceIfCfgCngOn_Object=MibTableColumn
h3cVoiceIfCfgCngOn=_H3cVoiceIfCfgCngOn_Object((1,3,6,1,4,1,43,45,1,10,2,39,13,1,1,1,1),_H3cVoiceIfCfgCngOn_Type())
h3cVoiceIfCfgCngOn.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoiceIfCfgCngOn.setStatus(_A)
class _H3cVoiceIfCfgNonLinearSwitch_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_H3cVoiceIfCfgNonLinearSwitch_Type.__name__=_C
_H3cVoiceIfCfgNonLinearSwitch_Object=MibTableColumn
h3cVoiceIfCfgNonLinearSwitch=_H3cVoiceIfCfgNonLinearSwitch_Object((1,3,6,1,4,1,43,45,1,10,2,39,13,1,1,1,2),_H3cVoiceIfCfgNonLinearSwitch_Type())
h3cVoiceIfCfgNonLinearSwitch.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoiceIfCfgNonLinearSwitch.setStatus(_A)
class _H3cVoiceIfCfgInputGain_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-140,139))
_H3cVoiceIfCfgInputGain_Type.__name__=_C
_H3cVoiceIfCfgInputGain_Object=MibTableColumn
h3cVoiceIfCfgInputGain=_H3cVoiceIfCfgInputGain_Object((1,3,6,1,4,1,43,45,1,10,2,39,13,1,1,1,3),_H3cVoiceIfCfgInputGain_Type())
h3cVoiceIfCfgInputGain.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoiceIfCfgInputGain.setStatus(_A)
class _H3cVoiceIfCfgOutputGain_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-140,139))
_H3cVoiceIfCfgOutputGain_Type.__name__=_C
_H3cVoiceIfCfgOutputGain_Object=MibTableColumn
h3cVoiceIfCfgOutputGain=_H3cVoiceIfCfgOutputGain_Object((1,3,6,1,4,1,43,45,1,10,2,39,13,1,1,1,4),_H3cVoiceIfCfgOutputGain_Type())
h3cVoiceIfCfgOutputGain.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoiceIfCfgOutputGain.setStatus(_A)
class _H3cVoiceIfCfgEchoCancelSwitch_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_H3cVoiceIfCfgEchoCancelSwitch_Type.__name__=_C
_H3cVoiceIfCfgEchoCancelSwitch_Object=MibTableColumn
h3cVoiceIfCfgEchoCancelSwitch=_H3cVoiceIfCfgEchoCancelSwitch_Object((1,3,6,1,4,1,43,45,1,10,2,39,13,1,1,1,5),_H3cVoiceIfCfgEchoCancelSwitch_Type())
h3cVoiceIfCfgEchoCancelSwitch.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoiceIfCfgEchoCancelSwitch.setStatus(_A)
class _H3cVoiceIfCfgEchoCancelDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,64))
_H3cVoiceIfCfgEchoCancelDelay_Type.__name__=_C
_H3cVoiceIfCfgEchoCancelDelay_Object=MibTableColumn
h3cVoiceIfCfgEchoCancelDelay=_H3cVoiceIfCfgEchoCancelDelay_Object((1,3,6,1,4,1,43,45,1,10,2,39,13,1,1,1,6),_H3cVoiceIfCfgEchoCancelDelay_Type())
h3cVoiceIfCfgEchoCancelDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoiceIfCfgEchoCancelDelay.setStatus(_A)
class _H3cVoiceIfCfgTimerDialInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,300))
_H3cVoiceIfCfgTimerDialInterval_Type.__name__=_C
_H3cVoiceIfCfgTimerDialInterval_Object=MibTableColumn
h3cVoiceIfCfgTimerDialInterval=_H3cVoiceIfCfgTimerDialInterval_Object((1,3,6,1,4,1,43,45,1,10,2,39,13,1,1,1,7),_H3cVoiceIfCfgTimerDialInterval_Type())
h3cVoiceIfCfgTimerDialInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoiceIfCfgTimerDialInterval.setStatus(_A)
class _H3cVoiceIfCfgTimerFirstDial_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,300))
_H3cVoiceIfCfgTimerFirstDial_Type.__name__=_C
_H3cVoiceIfCfgTimerFirstDial_Object=MibTableColumn
h3cVoiceIfCfgTimerFirstDial=_H3cVoiceIfCfgTimerFirstDial_Object((1,3,6,1,4,1,43,45,1,10,2,39,13,1,1,1,8),_H3cVoiceIfCfgTimerFirstDial_Type())
h3cVoiceIfCfgTimerFirstDial.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoiceIfCfgTimerFirstDial.setStatus(_A)
class _H3cVoiceIfCfgPrivateline_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_H3cVoiceIfCfgPrivateline_Type.__name__=_I
_H3cVoiceIfCfgPrivateline_Object=MibTableColumn
h3cVoiceIfCfgPrivateline=_H3cVoiceIfCfgPrivateline_Object((1,3,6,1,4,1,43,45,1,10,2,39,13,1,1,1,9),_H3cVoiceIfCfgPrivateline_Type())
h3cVoiceIfCfgPrivateline.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoiceIfCfgPrivateline.setStatus(_A)
class _H3cVoiceIfCfgRegTone_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(2,3))
_H3cVoiceIfCfgRegTone_Type.__name__=_F
_H3cVoiceIfCfgRegTone_Object=MibTableColumn
h3cVoiceIfCfgRegTone=_H3cVoiceIfCfgRegTone_Object((1,3,6,1,4,1,43,45,1,10,2,39,13,1,1,1,10),_H3cVoiceIfCfgRegTone_Type())
h3cVoiceIfCfgRegTone.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoiceIfCfgRegTone.setStatus(_A)
mibBuilder.exportSymbols('A3COM-HUAWEI-VOICE-IF-MIB',**{'h3cVoiceInterface':h3cVoiceInterface,'h3cVoiceIfObjects':h3cVoiceIfObjects,'h3cVoiceIfConfigTable':h3cVoiceIfConfigTable,'h3cVoiceIfConfigEntry':h3cVoiceIfConfigEntry,'h3cVoiceIfCfgCngOn':h3cVoiceIfCfgCngOn,'h3cVoiceIfCfgNonLinearSwitch':h3cVoiceIfCfgNonLinearSwitch,'h3cVoiceIfCfgInputGain':h3cVoiceIfCfgInputGain,'h3cVoiceIfCfgOutputGain':h3cVoiceIfCfgOutputGain,'h3cVoiceIfCfgEchoCancelSwitch':h3cVoiceIfCfgEchoCancelSwitch,'h3cVoiceIfCfgEchoCancelDelay':h3cVoiceIfCfgEchoCancelDelay,'h3cVoiceIfCfgTimerDialInterval':h3cVoiceIfCfgTimerDialInterval,'h3cVoiceIfCfgTimerFirstDial':h3cVoiceIfCfgTimerFirstDial,'h3cVoiceIfCfgPrivateline':h3cVoiceIfCfgPrivateline,'h3cVoiceIfCfgRegTone':h3cVoiceIfCfgRegTone})