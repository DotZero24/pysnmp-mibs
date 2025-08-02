_l='fxoIfIncomingCallNotAllowedBehaviorTableVer1'
_k='fxoIfAnalogLineTypeTableVer1'
_j='fxoForcedEndOfCallVer1'
_i='fxoIfAnsweringDelayTableVer1'
_h='fxoLineFaultDetectionVer1'
_g='fxoLinePropertiesCustomizationVer1'
_f='fxoBasicGroupVer1'
_e='fxoIfIncomingCallNotAllowedBehavior'
_d='fxoIfAnalogLineType'
_c='fxoEndOfCallToneCustomRepetition'
_b='fxoEndOfCallToneCustomCadence'
_a='fxoEndOfCallToneCustomFrequency'
_Z='fxoFeocOnToneDetectionMode'
_Y='fxoFeocOnSilenceDetectionTimeout'
_X='fxoFeocOnSilenceDetectionMode'
_W='fxoFeocOnCallFailureTimeout'
_V='fxoFeocOnCallFailureEnable'
_U='fxoWaitForCalleeToAnswerEnable'
_T='fxoAnswerOnCallerIdDetectionEnable'
_S='fxoPreAnswerDelay'
_R='fxoLineStatus'
_Q='fxoLineSeizureTimeout'
_P='fxoLineFaultDetectionEnable'
_O='fxoCallerIdDetectionRange'
_N='fxoDialtoneDetectionTimeout'
_M='fxoDialtoneDetectionMode'
_L='fxoConnectCallDelay'
_K='countryTone'
_J='OctetString'
_I='disable'
_H='MxEnableState'
_G='ifIndex'
_F='IF-MIB'
_E='Unsigned32'
_D='Integer32'
_C='read-write'
_B='MX-FXO-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_J,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_F,_G)
mediatrixConfig,=mibBuilder.importSymbols('MX-SMI','mediatrixConfig')
MxEnableState,=mibBuilder.importSymbols('MX-TC',_H)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
fxoMIB=ModuleIdentity((1,3,6,1,4,1,4935,15,45))
if mibBuilder.loadTexts:fxoMIB.setRevisions(('2012-06-04 00:00','2008-08-25 00:00','2008-07-15 00:00','2005-08-23 00:00','2005-07-04 00:00','2004-08-04 00:00','2003-11-06 00:00','2003-10-20 00:00','2003-09-25 00:00','2003-08-19 00:00','2003-02-25 00:00'))
_FxoMIBObjects_ObjectIdentity=ObjectIdentity
fxoMIBObjects=_FxoMIBObjects_ObjectIdentity((1,3,6,1,4,1,4935,15,45,1))
_FxoLinePropertiesCustomization_ObjectIdentity=ObjectIdentity
fxoLinePropertiesCustomization=_FxoLinePropertiesCustomization_ObjectIdentity((1,3,6,1,4,1,4935,15,45,1,5))
class _FxoDialtoneDetectionMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_K,1)))
_FxoDialtoneDetectionMode_Type.__name__=_D
_FxoDialtoneDetectionMode_Object=MibScalar
fxoDialtoneDetectionMode=_FxoDialtoneDetectionMode_Object((1,3,6,1,4,1,4935,15,45,1,5,5),_FxoDialtoneDetectionMode_Type())
fxoDialtoneDetectionMode.setMaxAccess(_C)
if mibBuilder.loadTexts:fxoDialtoneDetectionMode.setStatus(_A)
class _FxoDialtoneDetectionTimeout_Type(Unsigned32):defaultValue=3000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1300,10000))
_FxoDialtoneDetectionTimeout_Type.__name__=_E
_FxoDialtoneDetectionTimeout_Object=MibScalar
fxoDialtoneDetectionTimeout=_FxoDialtoneDetectionTimeout_Object((1,3,6,1,4,1,4935,15,45,1,5,10),_FxoDialtoneDetectionTimeout_Type())
fxoDialtoneDetectionTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:fxoDialtoneDetectionTimeout.setStatus(_A)
class _FxoCallerIdDetectionRange_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('high',0),('low',1)))
_FxoCallerIdDetectionRange_Type.__name__=_D
_FxoCallerIdDetectionRange_Object=MibScalar
fxoCallerIdDetectionRange=_FxoCallerIdDetectionRange_Object((1,3,6,1,4,1,4935,15,45,1,5,15),_FxoCallerIdDetectionRange_Type())
fxoCallerIdDetectionRange.setMaxAccess(_C)
if mibBuilder.loadTexts:fxoCallerIdDetectionRange.setStatus(_A)
class _FxoAnswerSupervisionMode_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('none',0),('batteryReversal',1),('billingTone',2)))
_FxoAnswerSupervisionMode_Type.__name__=_D
_FxoAnswerSupervisionMode_Object=MibScalar
fxoAnswerSupervisionMode=_FxoAnswerSupervisionMode_Object((1,3,6,1,4,1,4935,15,45,1,5,50),_FxoAnswerSupervisionMode_Type())
fxoAnswerSupervisionMode.setMaxAccess(_C)
if mibBuilder.loadTexts:fxoAnswerSupervisionMode.setStatus(_A)
_FxoLineFaultDetection_ObjectIdentity=ObjectIdentity
fxoLineFaultDetection=_FxoLineFaultDetection_ObjectIdentity((1,3,6,1,4,1,4935,15,45,1,10))
class _FxoLineFaultDetectionEnable_Type(MxEnableState):defaultValue=1
_FxoLineFaultDetectionEnable_Type.__name__=_H
_FxoLineFaultDetectionEnable_Object=MibScalar
fxoLineFaultDetectionEnable=_FxoLineFaultDetectionEnable_Object((1,3,6,1,4,1,4935,15,45,1,10,5),_FxoLineFaultDetectionEnable_Type())
fxoLineFaultDetectionEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:fxoLineFaultDetectionEnable.setStatus(_A)
class _FxoLineSeizureTimeout_Type(Unsigned32):defaultValue=5000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(500,10000))
_FxoLineSeizureTimeout_Type.__name__=_E
_FxoLineSeizureTimeout_Object=MibScalar
fxoLineSeizureTimeout=_FxoLineSeizureTimeout_Object((1,3,6,1,4,1,4935,15,45,1,10,10),_FxoLineSeizureTimeout_Type())
fxoLineSeizureTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:fxoLineSeizureTimeout.setStatus(_A)
_FxoIfLineStatusTable_Object=MibTable
fxoIfLineStatusTable=_FxoIfLineStatusTable_Object((1,3,6,1,4,1,4935,15,45,1,10,15))
if mibBuilder.loadTexts:fxoIfLineStatusTable.setStatus(_A)
_FxoIfLineStatusEntry_Object=MibTableRow
fxoIfLineStatusEntry=_FxoIfLineStatusEntry_Object((1,3,6,1,4,1,4935,15,45,1,10,15,5))
fxoIfLineStatusEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:fxoIfLineStatusEntry.setStatus(_A)
class _FxoLineStatus_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('unknown',0),('connected',1),('disconnected',2)))
_FxoLineStatus_Type.__name__=_D
_FxoLineStatus_Object=MibTableColumn
fxoLineStatus=_FxoLineStatus_Object((1,3,6,1,4,1,4935,15,45,1,10,15,5,5),_FxoLineStatus_Type())
fxoLineStatus.setMaxAccess('read-only')
if mibBuilder.loadTexts:fxoLineStatus.setStatus(_A)
_FxoIfAnsweringDelayTable_Object=MibTable
fxoIfAnsweringDelayTable=_FxoIfAnsweringDelayTable_Object((1,3,6,1,4,1,4935,15,45,1,15))
if mibBuilder.loadTexts:fxoIfAnsweringDelayTable.setStatus(_A)
_FxoIfAnsweringDelayEntry_Object=MibTableRow
fxoIfAnsweringDelayEntry=_FxoIfAnsweringDelayEntry_Object((1,3,6,1,4,1,4935,15,45,1,15,5))
fxoIfAnsweringDelayEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:fxoIfAnsweringDelayEntry.setStatus(_A)
class _FxoPreAnswerDelay_Type(Unsigned32):defaultValue=8000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,30000))
_FxoPreAnswerDelay_Type.__name__=_E
_FxoPreAnswerDelay_Object=MibTableColumn
fxoPreAnswerDelay=_FxoPreAnswerDelay_Object((1,3,6,1,4,1,4935,15,45,1,15,5,5),_FxoPreAnswerDelay_Type())
fxoPreAnswerDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:fxoPreAnswerDelay.setStatus(_A)
class _FxoAnswerOnCallerIdDetectionEnable_Type(MxEnableState):defaultValue=1
_FxoAnswerOnCallerIdDetectionEnable_Type.__name__=_H
_FxoAnswerOnCallerIdDetectionEnable_Object=MibTableColumn
fxoAnswerOnCallerIdDetectionEnable=_FxoAnswerOnCallerIdDetectionEnable_Object((1,3,6,1,4,1,4935,15,45,1,15,5,10),_FxoAnswerOnCallerIdDetectionEnable_Type())
fxoAnswerOnCallerIdDetectionEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:fxoAnswerOnCallerIdDetectionEnable.setStatus(_A)
class _FxoWaitForCalleeToAnswerEnable_Type(MxEnableState):defaultValue=0
_FxoWaitForCalleeToAnswerEnable_Type.__name__=_H
_FxoWaitForCalleeToAnswerEnable_Object=MibTableColumn
fxoWaitForCalleeToAnswerEnable=_FxoWaitForCalleeToAnswerEnable_Object((1,3,6,1,4,1,4935,15,45,1,15,5,60),_FxoWaitForCalleeToAnswerEnable_Type())
fxoWaitForCalleeToAnswerEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:fxoWaitForCalleeToAnswerEnable.setStatus(_A)
_FxoForcedEndOfCallCustomization_ObjectIdentity=ObjectIdentity
fxoForcedEndOfCallCustomization=_FxoForcedEndOfCallCustomization_ObjectIdentity((1,3,6,1,4,1,4935,15,45,1,20))
class _FxoFeocOnCallFailureEnable_Type(MxEnableState):defaultValue=1
_FxoFeocOnCallFailureEnable_Type.__name__=_H
_FxoFeocOnCallFailureEnable_Object=MibScalar
fxoFeocOnCallFailureEnable=_FxoFeocOnCallFailureEnable_Object((1,3,6,1,4,1,4935,15,45,1,20,5),_FxoFeocOnCallFailureEnable_Type())
fxoFeocOnCallFailureEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:fxoFeocOnCallFailureEnable.setStatus(_A)
class _FxoFeocOnCallFailureTimeout_Type(Unsigned32):defaultValue=30;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,180))
_FxoFeocOnCallFailureTimeout_Type.__name__=_E
_FxoFeocOnCallFailureTimeout_Object=MibScalar
fxoFeocOnCallFailureTimeout=_FxoFeocOnCallFailureTimeout_Object((1,3,6,1,4,1,4935,15,45,1,20,10),_FxoFeocOnCallFailureTimeout_Type())
fxoFeocOnCallFailureTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:fxoFeocOnCallFailureTimeout.setStatus(_A)
class _FxoFeocOnSilenceDetectionMode_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_I,0),('onScnSilent',1),('onIpSilent',2),('onIpAndScnSilent',3),('onIpOrScnSilent',4)))
_FxoFeocOnSilenceDetectionMode_Type.__name__=_D
_FxoFeocOnSilenceDetectionMode_Object=MibScalar
fxoFeocOnSilenceDetectionMode=_FxoFeocOnSilenceDetectionMode_Object((1,3,6,1,4,1,4935,15,45,1,20,15),_FxoFeocOnSilenceDetectionMode_Type())
fxoFeocOnSilenceDetectionMode.setMaxAccess(_C)
if mibBuilder.loadTexts:fxoFeocOnSilenceDetectionMode.setStatus(_A)
class _FxoFeocOnSilenceDetectionTimeout_Type(Unsigned32):defaultValue=300;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,300))
_FxoFeocOnSilenceDetectionTimeout_Type.__name__=_E
_FxoFeocOnSilenceDetectionTimeout_Object=MibScalar
fxoFeocOnSilenceDetectionTimeout=_FxoFeocOnSilenceDetectionTimeout_Object((1,3,6,1,4,1,4935,15,45,1,20,20),_FxoFeocOnSilenceDetectionTimeout_Type())
fxoFeocOnSilenceDetectionTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:fxoFeocOnSilenceDetectionTimeout.setStatus(_A)
class _FxoFeocOnToneDetectionMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_I,0),(_K,1),('customTone',2)))
_FxoFeocOnToneDetectionMode_Type.__name__=_D
_FxoFeocOnToneDetectionMode_Object=MibScalar
fxoFeocOnToneDetectionMode=_FxoFeocOnToneDetectionMode_Object((1,3,6,1,4,1,4935,15,45,1,20,25),_FxoFeocOnToneDetectionMode_Type())
fxoFeocOnToneDetectionMode.setMaxAccess(_C)
if mibBuilder.loadTexts:fxoFeocOnToneDetectionMode.setStatus(_A)
_FxoEndOfCallToneCustomSettings_ObjectIdentity=ObjectIdentity
fxoEndOfCallToneCustomSettings=_FxoEndOfCallToneCustomSettings_ObjectIdentity((1,3,6,1,4,1,4935,15,45,1,20,30))
class _FxoEndOfCallToneCustomFrequency_Type(Unsigned32):defaultValue=440;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(350,620))
_FxoEndOfCallToneCustomFrequency_Type.__name__=_E
_FxoEndOfCallToneCustomFrequency_Object=MibScalar
fxoEndOfCallToneCustomFrequency=_FxoEndOfCallToneCustomFrequency_Object((1,3,6,1,4,1,4935,15,45,1,20,30,5),_FxoEndOfCallToneCustomFrequency_Type())
fxoEndOfCallToneCustomFrequency.setMaxAccess(_C)
if mibBuilder.loadTexts:fxoEndOfCallToneCustomFrequency.setStatus(_A)
class _FxoEndOfCallToneCustomCadence_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_FxoEndOfCallToneCustomCadence_Type.__name__=_J
_FxoEndOfCallToneCustomCadence_Object=MibScalar
fxoEndOfCallToneCustomCadence=_FxoEndOfCallToneCustomCadence_Object((1,3,6,1,4,1,4935,15,45,1,20,30,10),_FxoEndOfCallToneCustomCadence_Type())
fxoEndOfCallToneCustomCadence.setMaxAccess(_C)
if mibBuilder.loadTexts:fxoEndOfCallToneCustomCadence.setStatus(_A)
class _FxoEndOfCallToneCustomRepetition_Type(Unsigned32):defaultValue=3;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,10))
_FxoEndOfCallToneCustomRepetition_Type.__name__=_E
_FxoEndOfCallToneCustomRepetition_Object=MibScalar
fxoEndOfCallToneCustomRepetition=_FxoEndOfCallToneCustomRepetition_Object((1,3,6,1,4,1,4935,15,45,1,20,30,15),_FxoEndOfCallToneCustomRepetition_Type())
fxoEndOfCallToneCustomRepetition.setMaxAccess(_C)
if mibBuilder.loadTexts:fxoEndOfCallToneCustomRepetition.setStatus(_A)
_FxoIfAnalogLineTypeTable_Object=MibTable
fxoIfAnalogLineTypeTable=_FxoIfAnalogLineTypeTable_Object((1,3,6,1,4,1,4935,15,45,1,25))
if mibBuilder.loadTexts:fxoIfAnalogLineTypeTable.setStatus(_A)
_FxoIfAnalogLineTypeEntry_Object=MibTableRow
fxoIfAnalogLineTypeEntry=_FxoIfAnalogLineTypeEntry_Object((1,3,6,1,4,1,4935,15,45,1,25,5))
fxoIfAnalogLineTypeEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:fxoIfAnalogLineTypeEntry.setStatus(_A)
class _FxoIfAnalogLineType_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('loopStart',0),('groundStart',1)))
_FxoIfAnalogLineType_Type.__name__=_D
_FxoIfAnalogLineType_Object=MibTableColumn
fxoIfAnalogLineType=_FxoIfAnalogLineType_Object((1,3,6,1,4,1,4935,15,45,1,25,5,5),_FxoIfAnalogLineType_Type())
fxoIfAnalogLineType.setMaxAccess(_C)
if mibBuilder.loadTexts:fxoIfAnalogLineType.setStatus(_A)
_FxoIfIncomingCallNotAllowedBehaviorTable_Object=MibTable
fxoIfIncomingCallNotAllowedBehaviorTable=_FxoIfIncomingCallNotAllowedBehaviorTable_Object((1,3,6,1,4,1,4935,15,45,1,50))
if mibBuilder.loadTexts:fxoIfIncomingCallNotAllowedBehaviorTable.setStatus(_A)
_FxoIfIncomingCallNotAllowedBehaviorEntry_Object=MibTableRow
fxoIfIncomingCallNotAllowedBehaviorEntry=_FxoIfIncomingCallNotAllowedBehaviorEntry_Object((1,3,6,1,4,1,4935,15,45,1,50,5))
fxoIfIncomingCallNotAllowedBehaviorEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:fxoIfIncomingCallNotAllowedBehaviorEntry.setStatus(_A)
class _FxoIfIncomingCallNotAllowedBehavior_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('doNotAnswer',0),('playCongestionTone',1)))
_FxoIfIncomingCallNotAllowedBehavior_Type.__name__=_D
_FxoIfIncomingCallNotAllowedBehavior_Object=MibTableColumn
fxoIfIncomingCallNotAllowedBehavior=_FxoIfIncomingCallNotAllowedBehavior_Object((1,3,6,1,4,1,4935,15,45,1,50,5,5),_FxoIfIncomingCallNotAllowedBehavior_Type())
fxoIfIncomingCallNotAllowedBehavior.setMaxAccess(_C)
if mibBuilder.loadTexts:fxoIfIncomingCallNotAllowedBehavior.setStatus(_A)
class _FxoConnectCallDelay_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,60000))
_FxoConnectCallDelay_Type.__name__=_E
_FxoConnectCallDelay_Object=MibScalar
fxoConnectCallDelay=_FxoConnectCallDelay_Object((1,3,6,1,4,1,4935,15,45,1,60),_FxoConnectCallDelay_Type())
fxoConnectCallDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:fxoConnectCallDelay.setStatus(_A)
_FxoConformance_ObjectIdentity=ObjectIdentity
fxoConformance=_FxoConformance_ObjectIdentity((1,3,6,1,4,1,4935,15,45,5))
_FxoCompliances_ObjectIdentity=ObjectIdentity
fxoCompliances=_FxoCompliances_ObjectIdentity((1,3,6,1,4,1,4935,15,45,5,1))
_FxoGroups_ObjectIdentity=ObjectIdentity
fxoGroups=_FxoGroups_ObjectIdentity((1,3,6,1,4,1,4935,15,45,5,5))
fxoBasicGroupVer1=ObjectGroup((1,3,6,1,4,1,4935,15,45,5,5,5))
fxoBasicGroupVer1.setObjects((_B,_L))
if mibBuilder.loadTexts:fxoBasicGroupVer1.setStatus(_A)
fxoLinePropertiesCustomizationVer1=ObjectGroup((1,3,6,1,4,1,4935,15,45,5,5,10))
fxoLinePropertiesCustomizationVer1.setObjects(*((_B,_M),(_B,_N),(_B,_O)))
if mibBuilder.loadTexts:fxoLinePropertiesCustomizationVer1.setStatus(_A)
fxoLineFaultDetectionVer1=ObjectGroup((1,3,6,1,4,1,4935,15,45,5,5,15))
fxoLineFaultDetectionVer1.setObjects(*((_B,_P),(_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:fxoLineFaultDetectionVer1.setStatus(_A)
fxoIfAnsweringDelayTableVer1=ObjectGroup((1,3,6,1,4,1,4935,15,45,5,5,20))
fxoIfAnsweringDelayTableVer1.setObjects(*((_B,_S),(_B,_T),(_B,_U)))
if mibBuilder.loadTexts:fxoIfAnsweringDelayTableVer1.setStatus(_A)
fxoForcedEndOfCallVer1=ObjectGroup((1,3,6,1,4,1,4935,15,45,5,5,25))
fxoForcedEndOfCallVer1.setObjects(*((_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c)))
if mibBuilder.loadTexts:fxoForcedEndOfCallVer1.setStatus(_A)
fxoIfAnalogLineTypeTableVer1=ObjectGroup((1,3,6,1,4,1,4935,15,45,5,5,30))
fxoIfAnalogLineTypeTableVer1.setObjects((_B,_d))
if mibBuilder.loadTexts:fxoIfAnalogLineTypeTableVer1.setStatus(_A)
fxoIfIncomingCallNotAllowedBehaviorTableVer1=ObjectGroup((1,3,6,1,4,1,4935,15,45,5,5,35))
fxoIfIncomingCallNotAllowedBehaviorTableVer1.setObjects((_B,_e))
if mibBuilder.loadTexts:fxoIfIncomingCallNotAllowedBehaviorTableVer1.setStatus(_A)
fxoComplVer1=ModuleCompliance((1,3,6,1,4,1,4935,15,45,5,1,1))
fxoComplVer1.setObjects(*((_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l)))
if mibBuilder.loadTexts:fxoComplVer1.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'fxoMIB':fxoMIB,'fxoMIBObjects':fxoMIBObjects,'fxoLinePropertiesCustomization':fxoLinePropertiesCustomization,_M:fxoDialtoneDetectionMode,_N:fxoDialtoneDetectionTimeout,_O:fxoCallerIdDetectionRange,'fxoAnswerSupervisionMode':fxoAnswerSupervisionMode,'fxoLineFaultDetection':fxoLineFaultDetection,_P:fxoLineFaultDetectionEnable,_Q:fxoLineSeizureTimeout,'fxoIfLineStatusTable':fxoIfLineStatusTable,'fxoIfLineStatusEntry':fxoIfLineStatusEntry,_R:fxoLineStatus,'fxoIfAnsweringDelayTable':fxoIfAnsweringDelayTable,'fxoIfAnsweringDelayEntry':fxoIfAnsweringDelayEntry,_S:fxoPreAnswerDelay,_T:fxoAnswerOnCallerIdDetectionEnable,_U:fxoWaitForCalleeToAnswerEnable,'fxoForcedEndOfCallCustomization':fxoForcedEndOfCallCustomization,_V:fxoFeocOnCallFailureEnable,_W:fxoFeocOnCallFailureTimeout,_X:fxoFeocOnSilenceDetectionMode,_Y:fxoFeocOnSilenceDetectionTimeout,_Z:fxoFeocOnToneDetectionMode,'fxoEndOfCallToneCustomSettings':fxoEndOfCallToneCustomSettings,_a:fxoEndOfCallToneCustomFrequency,_b:fxoEndOfCallToneCustomCadence,_c:fxoEndOfCallToneCustomRepetition,'fxoIfAnalogLineTypeTable':fxoIfAnalogLineTypeTable,'fxoIfAnalogLineTypeEntry':fxoIfAnalogLineTypeEntry,_d:fxoIfAnalogLineType,'fxoIfIncomingCallNotAllowedBehaviorTable':fxoIfIncomingCallNotAllowedBehaviorTable,'fxoIfIncomingCallNotAllowedBehaviorEntry':fxoIfIncomingCallNotAllowedBehaviorEntry,_e:fxoIfIncomingCallNotAllowedBehavior,_L:fxoConnectCallDelay,'fxoConformance':fxoConformance,'fxoCompliances':fxoCompliances,'fxoComplVer1':fxoComplVer1,'fxoGroups':fxoGroups,_f:fxoBasicGroupVer1,_g:fxoLinePropertiesCustomizationVer1,_h:fxoLineFaultDetectionVer1,_i:fxoIfAnsweringDelayTableVer1,_j:fxoForcedEndOfCallVer1,_k:fxoIfAnalogLineTypeTableVer1,_l:fxoIfIncomingCallNotAllowedBehaviorTableVer1})