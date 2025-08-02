_b='fxsEmergencyBypassGroupVer1'
_a='fxsGroupVer1'
_Z='fxsEmergencyBypassDialDelay'
_Y='fxsEmergencyBypassDialMap'
_X='fxsEmergencyBypassTimeout'
_W='fxsEmergencyBypassEnable'
_V='fxsCallingNumberTransformation'
_U='fxsCallingNumberCriteria'
_T='fxsFskMarkoutBits'
_S='fxsBlankAnonymousCallerId'
_R='fxsPowerDropOnDisconnectDuration'
_Q='fxsPolarityAndDenialBehavior'
_P='fxsReversalOnIdleEnable'
_O='fxsCalleeHangupDelay'
_N='fxsCalleeHangupSupervision'
_M='fxsLoopCurrentDropEnable'
_L='fxsFlashHookDetectionDelayMax'
_K='fxsFlashHookDetectionDelayMin'
_J='fxsLoopCurrent'
_I='fxsByPassEnable'
_H='MxDigitMap'
_G='Integer32'
_F='OctetString'
_E='MxEnableState'
_D='Unsigned32'
_C='read-write'
_B='MX-FXS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mediatrixConfig,=mibBuilder.importSymbols('MX-SMI','mediatrixConfig')
MxDigitMap,MxEnableState=mibBuilder.importSymbols('MX-TC',_H,_E)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
fxsMIB=ModuleIdentity((1,3,6,1,4,1,4935,15,40))
if mibBuilder.loadTexts:fxsMIB.setRevisions(('2009-08-05 00:00','2009-07-24 00:00','2009-01-26 00:00','2008-11-27 00:00','2007-05-18 00:00','2006-12-21 00:00','2006-02-13 00:00','2006-01-30 00:00','2005-11-07 00:00','2005-03-30 00:00','2005-01-27 00:00','2004-11-24 00:00','2004-09-27 00:00','2002-08-30 00:00','2002-08-22 00:00','2001-11-05 00:00','2001-08-29 00:00'))
_FxsMIBObjects_ObjectIdentity=ObjectIdentity
fxsMIBObjects=_FxsMIBObjects_ObjectIdentity((1,3,6,1,4,1,4935,15,40,1))
class _FxsByPassEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('disable',0),('enable',1)))
_FxsByPassEnable_Type.__name__=_G
_FxsByPassEnable_Object=MibScalar
fxsByPassEnable=_FxsByPassEnable_Object((1,3,6,1,4,1,4935,15,40,1,1),_FxsByPassEnable_Type())
fxsByPassEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:fxsByPassEnable.setStatus(_A)
class _FxsLoopCurrent_Type(Unsigned32):defaultValue=30;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(20,50))
_FxsLoopCurrent_Type.__name__=_D
_FxsLoopCurrent_Object=MibScalar
fxsLoopCurrent=_FxsLoopCurrent_Object((1,3,6,1,4,1,4935,15,40,1,2),_FxsLoopCurrent_Type())
fxsLoopCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:fxsLoopCurrent.setStatus(_A)
class _FxsFlashHookDetectionDelayMin_Type(Unsigned32):defaultValue=100;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,1200))
_FxsFlashHookDetectionDelayMin_Type.__name__=_D
_FxsFlashHookDetectionDelayMin_Object=MibScalar
fxsFlashHookDetectionDelayMin=_FxsFlashHookDetectionDelayMin_Object((1,3,6,1,4,1,4935,15,40,1,3),_FxsFlashHookDetectionDelayMin_Type())
fxsFlashHookDetectionDelayMin.setMaxAccess(_C)
if mibBuilder.loadTexts:fxsFlashHookDetectionDelayMin.setStatus(_A)
class _FxsFlashHookDetectionDelayMax_Type(Unsigned32):defaultValue=1200;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,1200))
_FxsFlashHookDetectionDelayMax_Type.__name__=_D
_FxsFlashHookDetectionDelayMax_Object=MibScalar
fxsFlashHookDetectionDelayMax=_FxsFlashHookDetectionDelayMax_Object((1,3,6,1,4,1,4935,15,40,1,4),_FxsFlashHookDetectionDelayMax_Type())
fxsFlashHookDetectionDelayMax.setMaxAccess(_C)
if mibBuilder.loadTexts:fxsFlashHookDetectionDelayMax.setStatus(_A)
class _FxsLoopCurrentDropEnable_Type(MxEnableState):defaultValue=0
_FxsLoopCurrentDropEnable_Type.__name__=_E
_FxsLoopCurrentDropEnable_Object=MibScalar
fxsLoopCurrentDropEnable=_FxsLoopCurrentDropEnable_Object((1,3,6,1,4,1,4935,15,40,1,50),_FxsLoopCurrentDropEnable_Type())
fxsLoopCurrentDropEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:fxsLoopCurrentDropEnable.setStatus(_A)
class _FxsCalleeHangupSupervision_Type(MxEnableState):defaultValue=0
_FxsCalleeHangupSupervision_Type.__name__=_E
_FxsCalleeHangupSupervision_Object=MibScalar
fxsCalleeHangupSupervision=_FxsCalleeHangupSupervision_Object((1,3,6,1,4,1,4935,15,40,1,75),_FxsCalleeHangupSupervision_Type())
fxsCalleeHangupSupervision.setMaxAccess(_C)
if mibBuilder.loadTexts:fxsCalleeHangupSupervision.setStatus(_A)
class _FxsCalleeHangupDelay_Type(Unsigned32):defaultValue=60;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,300))
_FxsCalleeHangupDelay_Type.__name__=_D
_FxsCalleeHangupDelay_Object=MibScalar
fxsCalleeHangupDelay=_FxsCalleeHangupDelay_Object((1,3,6,1,4,1,4935,15,40,1,100),_FxsCalleeHangupDelay_Type())
fxsCalleeHangupDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:fxsCalleeHangupDelay.setStatus(_A)
class _FxsReversalOnIdleEnable_Type(MxEnableState):defaultValue=0
_FxsReversalOnIdleEnable_Type.__name__=_E
_FxsReversalOnIdleEnable_Object=MibScalar
fxsReversalOnIdleEnable=_FxsReversalOnIdleEnable_Object((1,3,6,1,4,1,4935,15,40,1,125),_FxsReversalOnIdleEnable_Type())
fxsReversalOnIdleEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:fxsReversalOnIdleEnable.setStatus('deprecated')
class _FxsPolarityAndDenialBehavior_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('noReversal',0),('reversalOnIdle',1),('reversalOnEstablished',2)))
_FxsPolarityAndDenialBehavior_Type.__name__=_G
_FxsPolarityAndDenialBehavior_Object=MibScalar
fxsPolarityAndDenialBehavior=_FxsPolarityAndDenialBehavior_Object((1,3,6,1,4,1,4935,15,40,1,135),_FxsPolarityAndDenialBehavior_Type())
fxsPolarityAndDenialBehavior.setMaxAccess(_C)
if mibBuilder.loadTexts:fxsPolarityAndDenialBehavior.setStatus(_A)
class _FxsPowerDropOnDisconnectDuration_Type(Unsigned32):defaultValue=1000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,5000))
_FxsPowerDropOnDisconnectDuration_Type.__name__=_D
_FxsPowerDropOnDisconnectDuration_Object=MibScalar
fxsPowerDropOnDisconnectDuration=_FxsPowerDropOnDisconnectDuration_Object((1,3,6,1,4,1,4935,15,40,1,140),_FxsPowerDropOnDisconnectDuration_Type())
fxsPowerDropOnDisconnectDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:fxsPowerDropOnDisconnectDuration.setStatus(_A)
class _FxsBlankAnonymousCallerId_Type(MxEnableState):defaultValue=0
_FxsBlankAnonymousCallerId_Type.__name__=_E
_FxsBlankAnonymousCallerId_Object=MibScalar
fxsBlankAnonymousCallerId=_FxsBlankAnonymousCallerId_Object((1,3,6,1,4,1,4935,15,40,1,150),_FxsBlankAnonymousCallerId_Type())
fxsBlankAnonymousCallerId.setMaxAccess(_C)
if mibBuilder.loadTexts:fxsBlankAnonymousCallerId.setStatus(_A)
class _FxsFskMarkoutBits_Type(Unsigned32):defaultValue=200;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5280))
_FxsFskMarkoutBits_Type.__name__=_D
_FxsFskMarkoutBits_Object=MibScalar
fxsFskMarkoutBits=_FxsFskMarkoutBits_Object((1,3,6,1,4,1,4935,15,40,1,155),_FxsFskMarkoutBits_Type())
fxsFskMarkoutBits.setMaxAccess(_C)
if mibBuilder.loadTexts:fxsFskMarkoutBits.setStatus(_A)
class _FxsCallingNumberCriteria_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_FxsCallingNumberCriteria_Type.__name__=_F
_FxsCallingNumberCriteria_Object=MibScalar
fxsCallingNumberCriteria=_FxsCallingNumberCriteria_Object((1,3,6,1,4,1,4935,15,40,1,160),_FxsCallingNumberCriteria_Type())
fxsCallingNumberCriteria.setMaxAccess(_C)
if mibBuilder.loadTexts:fxsCallingNumberCriteria.setStatus(_A)
class _FxsCallingNumberTransformation_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_FxsCallingNumberTransformation_Type.__name__=_F
_FxsCallingNumberTransformation_Object=MibScalar
fxsCallingNumberTransformation=_FxsCallingNumberTransformation_Object((1,3,6,1,4,1,4935,15,40,1,161),_FxsCallingNumberTransformation_Type())
fxsCallingNumberTransformation.setMaxAccess(_C)
if mibBuilder.loadTexts:fxsCallingNumberTransformation.setStatus(_A)
_FxsEpSpecificLoopCurrentTable_Object=MibTable
fxsEpSpecificLoopCurrentTable=_FxsEpSpecificLoopCurrentTable_Object((1,3,6,1,4,1,4935,15,40,1,190))
if mibBuilder.loadTexts:fxsEpSpecificLoopCurrentTable.setStatus(_A)
_FxsEpSpecificLoopCurrentEntry_Object=MibTableRow
fxsEpSpecificLoopCurrentEntry=_FxsEpSpecificLoopCurrentEntry_Object((1,3,6,1,4,1,4935,15,40,1,190,1))
fxsEpSpecificLoopCurrentEntry.setIndexNames((0,_B,'ifIndex'))
if mibBuilder.loadTexts:fxsEpSpecificLoopCurrentEntry.setStatus(_A)
class _FxsEpSpecificLoopCurrentOverrideEnable_Type(MxEnableState):defaultValue=0
_FxsEpSpecificLoopCurrentOverrideEnable_Type.__name__=_E
_FxsEpSpecificLoopCurrentOverrideEnable_Object=MibTableColumn
fxsEpSpecificLoopCurrentOverrideEnable=_FxsEpSpecificLoopCurrentOverrideEnable_Object((1,3,6,1,4,1,4935,15,40,1,190,1,10),_FxsEpSpecificLoopCurrentOverrideEnable_Type())
fxsEpSpecificLoopCurrentOverrideEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:fxsEpSpecificLoopCurrentOverrideEnable.setStatus(_A)
class _FxsEpSpecificLoopCurrentOverride_Type(Unsigned32):defaultValue=30;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(20,50))
_FxsEpSpecificLoopCurrentOverride_Type.__name__=_D
_FxsEpSpecificLoopCurrentOverride_Object=MibTableColumn
fxsEpSpecificLoopCurrentOverride=_FxsEpSpecificLoopCurrentOverride_Object((1,3,6,1,4,1,4935,15,40,1,190,1,20),_FxsEpSpecificLoopCurrentOverride_Type())
fxsEpSpecificLoopCurrentOverride.setMaxAccess(_C)
if mibBuilder.loadTexts:fxsEpSpecificLoopCurrentOverride.setStatus(_A)
_FxsEmergencyBypass_ObjectIdentity=ObjectIdentity
fxsEmergencyBypass=_FxsEmergencyBypass_ObjectIdentity((1,3,6,1,4,1,4935,15,40,1,200))
class _FxsEmergencyBypassEnable_Type(MxEnableState):defaultValue=0
_FxsEmergencyBypassEnable_Type.__name__=_E
_FxsEmergencyBypassEnable_Object=MibScalar
fxsEmergencyBypassEnable=_FxsEmergencyBypassEnable_Object((1,3,6,1,4,1,4935,15,40,1,200,50),_FxsEmergencyBypassEnable_Type())
fxsEmergencyBypassEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:fxsEmergencyBypassEnable.setStatus(_A)
class _FxsEmergencyBypassTimeout_Type(Unsigned32):defaultValue=120;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3600))
_FxsEmergencyBypassTimeout_Type.__name__=_D
_FxsEmergencyBypassTimeout_Object=MibScalar
fxsEmergencyBypassTimeout=_FxsEmergencyBypassTimeout_Object((1,3,6,1,4,1,4935,15,40,1,200,100),_FxsEmergencyBypassTimeout_Type())
fxsEmergencyBypassTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:fxsEmergencyBypassTimeout.setStatus(_A)
class _FxsEmergencyBypassDialMap_Type(MxDigitMap):defaultValue=OctetString('')
_FxsEmergencyBypassDialMap_Type.__name__=_H
_FxsEmergencyBypassDialMap_Object=MibScalar
fxsEmergencyBypassDialMap=_FxsEmergencyBypassDialMap_Object((1,3,6,1,4,1,4935,15,40,1,200,150),_FxsEmergencyBypassDialMap_Type())
fxsEmergencyBypassDialMap.setMaxAccess(_C)
if mibBuilder.loadTexts:fxsEmergencyBypassDialMap.setStatus(_A)
class _FxsEmergencyBypassDialDelay_Type(Unsigned32):defaultValue=3;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_FxsEmergencyBypassDialDelay_Type.__name__=_D
_FxsEmergencyBypassDialDelay_Object=MibScalar
fxsEmergencyBypassDialDelay=_FxsEmergencyBypassDialDelay_Object((1,3,6,1,4,1,4935,15,40,1,200,200),_FxsEmergencyBypassDialDelay_Type())
fxsEmergencyBypassDialDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:fxsEmergencyBypassDialDelay.setStatus(_A)
_FxsConformance_ObjectIdentity=ObjectIdentity
fxsConformance=_FxsConformance_ObjectIdentity((1,3,6,1,4,1,4935,15,40,2))
_FxsCompliances_ObjectIdentity=ObjectIdentity
fxsCompliances=_FxsCompliances_ObjectIdentity((1,3,6,1,4,1,4935,15,40,2,1))
_FxsGroups_ObjectIdentity=ObjectIdentity
fxsGroups=_FxsGroups_ObjectIdentity((1,3,6,1,4,1,4935,15,40,2,5))
fxsGroupVer1=ObjectGroup((1,3,6,1,4,1,4935,15,40,2,5,5))
fxsGroupVer1.setObjects(*((_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V)))
if mibBuilder.loadTexts:fxsGroupVer1.setStatus(_A)
fxsEmergencyBypassGroupVer1=ObjectGroup((1,3,6,1,4,1,4935,15,40,2,5,10))
fxsEmergencyBypassGroupVer1.setObjects(*((_B,_W),(_B,_X),(_B,_Y),(_B,_Z)))
if mibBuilder.loadTexts:fxsEmergencyBypassGroupVer1.setStatus(_A)
fxsComplVer1=ModuleCompliance((1,3,6,1,4,1,4935,15,40,2,1,1))
fxsComplVer1.setObjects(*((_B,_a),(_B,_b)))
if mibBuilder.loadTexts:fxsComplVer1.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'fxsMIB':fxsMIB,'fxsMIBObjects':fxsMIBObjects,_I:fxsByPassEnable,_J:fxsLoopCurrent,_K:fxsFlashHookDetectionDelayMin,_L:fxsFlashHookDetectionDelayMax,_M:fxsLoopCurrentDropEnable,_N:fxsCalleeHangupSupervision,_O:fxsCalleeHangupDelay,_P:fxsReversalOnIdleEnable,_Q:fxsPolarityAndDenialBehavior,_R:fxsPowerDropOnDisconnectDuration,_S:fxsBlankAnonymousCallerId,_T:fxsFskMarkoutBits,_U:fxsCallingNumberCriteria,_V:fxsCallingNumberTransformation,'fxsEpSpecificLoopCurrentTable':fxsEpSpecificLoopCurrentTable,'fxsEpSpecificLoopCurrentEntry':fxsEpSpecificLoopCurrentEntry,'fxsEpSpecificLoopCurrentOverrideEnable':fxsEpSpecificLoopCurrentOverrideEnable,'fxsEpSpecificLoopCurrentOverride':fxsEpSpecificLoopCurrentOverride,'fxsEmergencyBypass':fxsEmergencyBypass,_W:fxsEmergencyBypassEnable,_X:fxsEmergencyBypassTimeout,_Y:fxsEmergencyBypassDialMap,_Z:fxsEmergencyBypassDialDelay,'fxsConformance':fxsConformance,'fxsCompliances':fxsCompliances,'fxsComplVer1':fxsComplVer1,'fxsGroups':fxsGroups,_a:fxsGroupVer1,_b:fxsEmergencyBypassGroupVer1})