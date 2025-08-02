_m='ieee8021STObjectsGroup'
_l='ieee8021STSupportedListMax'
_k='ieee8021STConfigChangeError'
_j='ieee8021STConfigPending'
_i='ieee8021STCurrentTime'
_h='ieee8021STTickGranularity'
_g='ieee8021STConfigChangeTime'
_f='ieee8021STConfigChange'
_e='ieee8021STOperBaseTime'
_d='ieee8021STAdminBaseTime'
_c='ieee8021STOperCycleTimeExtension'
_b='ieee8021STAdminCycleTimeExtension'
_a='ieee8021STOperCycleTimeDenominator'
_Z='ieee8021STOperCycleTimeNumerator'
_Y='ieee8021STAdminCycleTimeDenominator'
_X='ieee8021STAdminCycleTimeNumerator'
_W='ieee8021STOperControlList'
_V='ieee8021STAdminControlList'
_U='ieee8021STOperControlListLength'
_T='ieee8021STAdminControlListLength'
_S='ieee8021STOperGateStates'
_R='ieee8021STAdminGateStates'
_Q='ieee8021STGateEnabled'
_P='ieee8021TransmissionOverrun'
_O='ieee8021STMaxSDU'
_N='nanoseconds'
_M='ieee8021STTrafficClass'
_L='TruthValue'
_K='Unsigned32'
_J='Counter64'
_I='PTP time'
_H='ieee8021BridgeBasePort'
_G='ieee8021BridgeBaseComponentId'
_F='OctetString'
_E='IEEE8021-BRIDGE-MIB'
_D='read-write'
_C='read-only'
_B='IEEE8021-ST-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ieee8021BridgeBaseComponentId,ieee8021BridgeBasePort=mibBuilder.importSymbols(_E,_G,_H)
ieee802dot1mibs,=mibBuilder.importSymbols('IEEE8021-TC-MIB','ieee802dot1mibs')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32',_J,'Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_K,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_L)
ieee8021STMib=ModuleIdentity((1,3,111,2,802,1,1,30))
if mibBuilder.loadTexts:ieee8021STMib.setRevisions(('2018-06-21 00:00','2016-08-15 00:00','2016-02-19 00:00'))
class IEEE8021STTrafficClassValue(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
class IEEE8021STPTPtimeValue(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(10,10));fixedLength=10
_Ieee8021STNotifications_ObjectIdentity=ObjectIdentity
ieee8021STNotifications=_Ieee8021STNotifications_ObjectIdentity((1,3,111,2,802,1,1,30,0))
_Ieee8021STObjects_ObjectIdentity=ObjectIdentity
ieee8021STObjects=_Ieee8021STObjects_ObjectIdentity((1,3,111,2,802,1,1,30,1))
_Ieee8021STMaxSDUSubtree_ObjectIdentity=ObjectIdentity
ieee8021STMaxSDUSubtree=_Ieee8021STMaxSDUSubtree_ObjectIdentity((1,3,111,2,802,1,1,30,1,1))
_Ieee8021STMaxSDUTable_Object=MibTable
ieee8021STMaxSDUTable=_Ieee8021STMaxSDUTable_Object((1,3,111,2,802,1,1,30,1,1,1))
if mibBuilder.loadTexts:ieee8021STMaxSDUTable.setStatus(_A)
_Ieee8021STMaxSDUEntry_Object=MibTableRow
ieee8021STMaxSDUEntry=_Ieee8021STMaxSDUEntry_Object((1,3,111,2,802,1,1,30,1,1,1,1))
ieee8021STMaxSDUEntry.setIndexNames((0,_E,_G),(0,_E,_H),(0,_B,_M))
if mibBuilder.loadTexts:ieee8021STMaxSDUEntry.setStatus(_A)
_Ieee8021STTrafficClass_Type=IEEE8021STTrafficClassValue
_Ieee8021STTrafficClass_Object=MibTableColumn
ieee8021STTrafficClass=_Ieee8021STTrafficClass_Object((1,3,111,2,802,1,1,30,1,1,1,1,1),_Ieee8021STTrafficClass_Type())
ieee8021STTrafficClass.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:ieee8021STTrafficClass.setStatus(_A)
class _Ieee8021STMaxSDU_Type(Unsigned32):defaultValue=0
_Ieee8021STMaxSDU_Type.__name__=_K
_Ieee8021STMaxSDU_Object=MibTableColumn
ieee8021STMaxSDU=_Ieee8021STMaxSDU_Object((1,3,111,2,802,1,1,30,1,1,1,1,2),_Ieee8021STMaxSDU_Type())
ieee8021STMaxSDU.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021STMaxSDU.setStatus(_A)
if mibBuilder.loadTexts:ieee8021STMaxSDU.setUnits('octets')
class _Ieee8021TransmissionOverrun_Type(Counter64):defaultValue=0
_Ieee8021TransmissionOverrun_Type.__name__=_J
_Ieee8021TransmissionOverrun_Object=MibTableColumn
ieee8021TransmissionOverrun=_Ieee8021TransmissionOverrun_Object((1,3,111,2,802,1,1,30,1,1,1,1,3),_Ieee8021TransmissionOverrun_Type())
ieee8021TransmissionOverrun.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021TransmissionOverrun.setStatus(_A)
_Ieee8021STParameters_ObjectIdentity=ObjectIdentity
ieee8021STParameters=_Ieee8021STParameters_ObjectIdentity((1,3,111,2,802,1,1,30,1,2))
_Ieee8021STParametersTable_Object=MibTable
ieee8021STParametersTable=_Ieee8021STParametersTable_Object((1,3,111,2,802,1,1,30,1,2,1))
if mibBuilder.loadTexts:ieee8021STParametersTable.setStatus(_A)
_Ieee8021STParametersEntry_Object=MibTableRow
ieee8021STParametersEntry=_Ieee8021STParametersEntry_Object((1,3,111,2,802,1,1,30,1,2,1,1))
ieee8021STParametersEntry.setIndexNames((0,_E,_G),(0,_E,_H))
if mibBuilder.loadTexts:ieee8021STParametersEntry.setStatus(_A)
class _Ieee8021STGateEnabled_Type(TruthValue):defaultValue=2
_Ieee8021STGateEnabled_Type.__name__=_L
_Ieee8021STGateEnabled_Object=MibTableColumn
ieee8021STGateEnabled=_Ieee8021STGateEnabled_Object((1,3,111,2,802,1,1,30,1,2,1,1,1),_Ieee8021STGateEnabled_Type())
ieee8021STGateEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021STGateEnabled.setStatus(_A)
class _Ieee8021STAdminGateStates_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1));fixedLength=1
_Ieee8021STAdminGateStates_Type.__name__=_F
_Ieee8021STAdminGateStates_Object=MibTableColumn
ieee8021STAdminGateStates=_Ieee8021STAdminGateStates_Object((1,3,111,2,802,1,1,30,1,2,1,1,2),_Ieee8021STAdminGateStates_Type())
ieee8021STAdminGateStates.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021STAdminGateStates.setStatus(_A)
class _Ieee8021STOperGateStates_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1));fixedLength=1
_Ieee8021STOperGateStates_Type.__name__=_F
_Ieee8021STOperGateStates_Object=MibTableColumn
ieee8021STOperGateStates=_Ieee8021STOperGateStates_Object((1,3,111,2,802,1,1,30,1,2,1,1,3),_Ieee8021STOperGateStates_Type())
ieee8021STOperGateStates.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021STOperGateStates.setStatus(_A)
_Ieee8021STAdminControlListLength_Type=Unsigned32
_Ieee8021STAdminControlListLength_Object=MibTableColumn
ieee8021STAdminControlListLength=_Ieee8021STAdminControlListLength_Object((1,3,111,2,802,1,1,30,1,2,1,1,4),_Ieee8021STAdminControlListLength_Type())
ieee8021STAdminControlListLength.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021STAdminControlListLength.setStatus(_A)
_Ieee8021STOperControlListLength_Type=Unsigned32
_Ieee8021STOperControlListLength_Object=MibTableColumn
ieee8021STOperControlListLength=_Ieee8021STOperControlListLength_Object((1,3,111,2,802,1,1,30,1,2,1,1,5),_Ieee8021STOperControlListLength_Type())
ieee8021STOperControlListLength.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021STOperControlListLength.setStatus(_A)
_Ieee8021STAdminControlList_Type=OctetString
_Ieee8021STAdminControlList_Object=MibTableColumn
ieee8021STAdminControlList=_Ieee8021STAdminControlList_Object((1,3,111,2,802,1,1,30,1,2,1,1,6),_Ieee8021STAdminControlList_Type())
ieee8021STAdminControlList.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021STAdminControlList.setStatus(_A)
_Ieee8021STOperControlList_Type=OctetString
_Ieee8021STOperControlList_Object=MibTableColumn
ieee8021STOperControlList=_Ieee8021STOperControlList_Object((1,3,111,2,802,1,1,30,1,2,1,1,7),_Ieee8021STOperControlList_Type())
ieee8021STOperControlList.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021STOperControlList.setStatus(_A)
_Ieee8021STAdminCycleTimeNumerator_Type=Unsigned32
_Ieee8021STAdminCycleTimeNumerator_Object=MibTableColumn
ieee8021STAdminCycleTimeNumerator=_Ieee8021STAdminCycleTimeNumerator_Object((1,3,111,2,802,1,1,30,1,2,1,1,8),_Ieee8021STAdminCycleTimeNumerator_Type())
ieee8021STAdminCycleTimeNumerator.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021STAdminCycleTimeNumerator.setStatus(_A)
_Ieee8021STAdminCycleTimeDenominator_Type=Unsigned32
_Ieee8021STAdminCycleTimeDenominator_Object=MibTableColumn
ieee8021STAdminCycleTimeDenominator=_Ieee8021STAdminCycleTimeDenominator_Object((1,3,111,2,802,1,1,30,1,2,1,1,9),_Ieee8021STAdminCycleTimeDenominator_Type())
ieee8021STAdminCycleTimeDenominator.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021STAdminCycleTimeDenominator.setStatus(_A)
_Ieee8021STOperCycleTimeNumerator_Type=Unsigned32
_Ieee8021STOperCycleTimeNumerator_Object=MibTableColumn
ieee8021STOperCycleTimeNumerator=_Ieee8021STOperCycleTimeNumerator_Object((1,3,111,2,802,1,1,30,1,2,1,1,10),_Ieee8021STOperCycleTimeNumerator_Type())
ieee8021STOperCycleTimeNumerator.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021STOperCycleTimeNumerator.setStatus(_A)
_Ieee8021STOperCycleTimeDenominator_Type=Unsigned32
_Ieee8021STOperCycleTimeDenominator_Object=MibTableColumn
ieee8021STOperCycleTimeDenominator=_Ieee8021STOperCycleTimeDenominator_Object((1,3,111,2,802,1,1,30,1,2,1,1,11),_Ieee8021STOperCycleTimeDenominator_Type())
ieee8021STOperCycleTimeDenominator.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021STOperCycleTimeDenominator.setStatus(_A)
_Ieee8021STAdminCycleTimeExtension_Type=Unsigned32
_Ieee8021STAdminCycleTimeExtension_Object=MibTableColumn
ieee8021STAdminCycleTimeExtension=_Ieee8021STAdminCycleTimeExtension_Object((1,3,111,2,802,1,1,30,1,2,1,1,12),_Ieee8021STAdminCycleTimeExtension_Type())
ieee8021STAdminCycleTimeExtension.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021STAdminCycleTimeExtension.setStatus(_A)
if mibBuilder.loadTexts:ieee8021STAdminCycleTimeExtension.setUnits(_N)
_Ieee8021STOperCycleTimeExtension_Type=Unsigned32
_Ieee8021STOperCycleTimeExtension_Object=MibTableColumn
ieee8021STOperCycleTimeExtension=_Ieee8021STOperCycleTimeExtension_Object((1,3,111,2,802,1,1,30,1,2,1,1,13),_Ieee8021STOperCycleTimeExtension_Type())
ieee8021STOperCycleTimeExtension.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021STOperCycleTimeExtension.setStatus(_A)
if mibBuilder.loadTexts:ieee8021STOperCycleTimeExtension.setUnits(_N)
_Ieee8021STAdminBaseTime_Type=IEEE8021STPTPtimeValue
_Ieee8021STAdminBaseTime_Object=MibTableColumn
ieee8021STAdminBaseTime=_Ieee8021STAdminBaseTime_Object((1,3,111,2,802,1,1,30,1,2,1,1,14),_Ieee8021STAdminBaseTime_Type())
ieee8021STAdminBaseTime.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021STAdminBaseTime.setStatus(_A)
if mibBuilder.loadTexts:ieee8021STAdminBaseTime.setUnits(_I)
_Ieee8021STOperBaseTime_Type=IEEE8021STPTPtimeValue
_Ieee8021STOperBaseTime_Object=MibTableColumn
ieee8021STOperBaseTime=_Ieee8021STOperBaseTime_Object((1,3,111,2,802,1,1,30,1,2,1,1,15),_Ieee8021STOperBaseTime_Type())
ieee8021STOperBaseTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021STOperBaseTime.setStatus(_A)
if mibBuilder.loadTexts:ieee8021STOperBaseTime.setUnits(_I)
_Ieee8021STConfigChange_Type=TruthValue
_Ieee8021STConfigChange_Object=MibTableColumn
ieee8021STConfigChange=_Ieee8021STConfigChange_Object((1,3,111,2,802,1,1,30,1,2,1,1,16),_Ieee8021STConfigChange_Type())
ieee8021STConfigChange.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021STConfigChange.setStatus(_A)
_Ieee8021STConfigChangeTime_Type=IEEE8021STPTPtimeValue
_Ieee8021STConfigChangeTime_Object=MibTableColumn
ieee8021STConfigChangeTime=_Ieee8021STConfigChangeTime_Object((1,3,111,2,802,1,1,30,1,2,1,1,17),_Ieee8021STConfigChangeTime_Type())
ieee8021STConfigChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021STConfigChangeTime.setStatus(_A)
if mibBuilder.loadTexts:ieee8021STConfigChangeTime.setUnits(_I)
_Ieee8021STTickGranularity_Type=Unsigned32
_Ieee8021STTickGranularity_Object=MibTableColumn
ieee8021STTickGranularity=_Ieee8021STTickGranularity_Object((1,3,111,2,802,1,1,30,1,2,1,1,18),_Ieee8021STTickGranularity_Type())
ieee8021STTickGranularity.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021STTickGranularity.setStatus(_A)
_Ieee8021STCurrentTime_Type=IEEE8021STPTPtimeValue
_Ieee8021STCurrentTime_Object=MibTableColumn
ieee8021STCurrentTime=_Ieee8021STCurrentTime_Object((1,3,111,2,802,1,1,30,1,2,1,1,19),_Ieee8021STCurrentTime_Type())
ieee8021STCurrentTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021STCurrentTime.setStatus(_A)
_Ieee8021STConfigPending_Type=TruthValue
_Ieee8021STConfigPending_Object=MibTableColumn
ieee8021STConfigPending=_Ieee8021STConfigPending_Object((1,3,111,2,802,1,1,30,1,2,1,1,20),_Ieee8021STConfigPending_Type())
ieee8021STConfigPending.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021STConfigPending.setStatus(_A)
_Ieee8021STConfigChangeError_Type=Counter64
_Ieee8021STConfigChangeError_Object=MibTableColumn
ieee8021STConfigChangeError=_Ieee8021STConfigChangeError_Object((1,3,111,2,802,1,1,30,1,2,1,1,21),_Ieee8021STConfigChangeError_Type())
ieee8021STConfigChangeError.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021STConfigChangeError.setStatus(_A)
_Ieee8021STSupportedListMax_Type=Unsigned32
_Ieee8021STSupportedListMax_Object=MibTableColumn
ieee8021STSupportedListMax=_Ieee8021STSupportedListMax_Object((1,3,111,2,802,1,1,30,1,2,1,1,22),_Ieee8021STSupportedListMax_Type())
ieee8021STSupportedListMax.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021STSupportedListMax.setStatus(_A)
_Ieee8021STConformance_ObjectIdentity=ObjectIdentity
ieee8021STConformance=_Ieee8021STConformance_ObjectIdentity((1,3,111,2,802,1,1,30,2))
_Ieee8021STCompliances_ObjectIdentity=ObjectIdentity
ieee8021STCompliances=_Ieee8021STCompliances_ObjectIdentity((1,3,111,2,802,1,1,30,2,1))
_Ieee8021STGroups_ObjectIdentity=ObjectIdentity
ieee8021STGroups=_Ieee8021STGroups_ObjectIdentity((1,3,111,2,802,1,1,30,2,2))
ieee8021STObjectsGroup=ObjectGroup((1,3,111,2,802,1,1,30,2,2,1))
ieee8021STObjectsGroup.setObjects(*((_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l)))
if mibBuilder.loadTexts:ieee8021STObjectsGroup.setStatus(_A)
ieee8021STCompliance=ModuleCompliance((1,3,111,2,802,1,1,30,2,1,1))
ieee8021STCompliance.setObjects((_B,_m))
if mibBuilder.loadTexts:ieee8021STCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'IEEE8021STTrafficClassValue':IEEE8021STTrafficClassValue,'IEEE8021STPTPtimeValue':IEEE8021STPTPtimeValue,'ieee8021STMib':ieee8021STMib,'ieee8021STNotifications':ieee8021STNotifications,'ieee8021STObjects':ieee8021STObjects,'ieee8021STMaxSDUSubtree':ieee8021STMaxSDUSubtree,'ieee8021STMaxSDUTable':ieee8021STMaxSDUTable,'ieee8021STMaxSDUEntry':ieee8021STMaxSDUEntry,_M:ieee8021STTrafficClass,_O:ieee8021STMaxSDU,_P:ieee8021TransmissionOverrun,'ieee8021STParameters':ieee8021STParameters,'ieee8021STParametersTable':ieee8021STParametersTable,'ieee8021STParametersEntry':ieee8021STParametersEntry,_Q:ieee8021STGateEnabled,_R:ieee8021STAdminGateStates,_S:ieee8021STOperGateStates,_T:ieee8021STAdminControlListLength,_U:ieee8021STOperControlListLength,_V:ieee8021STAdminControlList,_W:ieee8021STOperControlList,_X:ieee8021STAdminCycleTimeNumerator,_Y:ieee8021STAdminCycleTimeDenominator,_Z:ieee8021STOperCycleTimeNumerator,_a:ieee8021STOperCycleTimeDenominator,_b:ieee8021STAdminCycleTimeExtension,_c:ieee8021STOperCycleTimeExtension,_d:ieee8021STAdminBaseTime,_e:ieee8021STOperBaseTime,_f:ieee8021STConfigChange,_g:ieee8021STConfigChangeTime,_h:ieee8021STTickGranularity,_i:ieee8021STCurrentTime,_j:ieee8021STConfigPending,_k:ieee8021STConfigChangeError,_l:ieee8021STSupportedListMax,'ieee8021STConformance':ieee8021STConformance,'ieee8021STCompliances':ieee8021STCompliances,'ieee8021STCompliance':ieee8021STCompliance,'ieee8021STGroups':ieee8021STGroups,_m:ieee8021STObjectsGroup})