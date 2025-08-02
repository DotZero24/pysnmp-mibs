_h='ieee8021FqtssSRClassPriorityGroup'
_g='ieee8021FqtssBapMeasurementGroup'
_f='ieee8021FqtssBoundaryPortGroup'
_e='ieee8021FqtssTxSelectionAlgorithmGroup'
_d='ieee8021FqtssBapGroup'
_c='ieee8021FqtssSRClassToPriorityRowStatus'
_b='ieee8021FqtssSRClassToPrioritySrClassID'
_a='ieee8021FqtssBAPLockClassBandwidth'
_Z='ieee8021FqtssBAPClassMeasurementInterval'
_Y='ieee8021FqtssSrpBoundaryPort'
_X='ieee8021FqtssPriorityRegenOverride'
_W='ieee8021FqtssTxSelectionAlgorithmID'
_V='ieee8021FqtssBapRowStatus'
_U='ieee8021FqtssAdminIdleSlopeLs'
_T='ieee8021FqtssAdminIdleSlopeMs'
_S='ieee8021FqtssOperIdleSlopeLs'
_R='ieee8021FqtssOperIdleSlopeMs'
_Q='ieee8021FqtssDeltaBandwidth'
_P='ieee8021FqtssBapXEntry'
_O='ieee8021FqtssTrafficClass'
_N='ieee8021FqtssBAPTrafficClass'
_M='TruthValue'
_L='ieee8021FqtssSrClassPriority'
_K='read-only'
_J='not-accessible'
_I='Unsigned32'
_H='bits per second'
_G='read-create'
_F='read-write'
_E='ieee8021BridgeBasePort'
_D='ieee8021BridgeBaseComponentId'
_C='IEEE8021-BRIDGE-MIB'
_B='IEEE8021-FQTSS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
BridgeId,=mibBuilder.importSymbols('BRIDGE-MIB','BridgeId')
ieee8021BridgeBaseComponentId,ieee8021BridgeBaseEntry,ieee8021BridgeBasePort,ieee8021BridgeBasePortEntry=mibBuilder.importSymbols(_C,_D,'ieee8021BridgeBaseEntry',_E,'ieee8021BridgeBasePortEntry')
IEEE8021PriorityValue,ieee802dot1mibs=mibBuilder.importSymbols('IEEE8021-TC-MIB','IEEE8021PriorityValue','ieee802dot1mibs')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_I,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_M)
ieee8021FqtssMib=ModuleIdentity((1,3,111,2,802,1,1,16))
if mibBuilder.loadTexts:ieee8021FqtssMib.setRevisions(('2018-10-04 00:00','2018-06-28 00:00','2015-12-02 00:00','2014-12-15 00:00','2011-02-27 00:00','2009-10-01 00:00'))
class IEEE8021FqtssTrafficClassValue(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
class IEEE8021FqtssDeltaBandwidthValue(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100000000))
class IEEE8021FqtssTxSelectionAlgorithmIDValue(TextualConvention,Unsigned32):status=_A;displayHint='d'
_Ieee8021FqtssNotifications_ObjectIdentity=ObjectIdentity
ieee8021FqtssNotifications=_Ieee8021FqtssNotifications_ObjectIdentity((1,3,111,2,802,1,1,16,0))
_Ieee8021FqtssObjects_ObjectIdentity=ObjectIdentity
ieee8021FqtssObjects=_Ieee8021FqtssObjects_ObjectIdentity((1,3,111,2,802,1,1,16,1))
_Ieee8021FqtssBap_ObjectIdentity=ObjectIdentity
ieee8021FqtssBap=_Ieee8021FqtssBap_ObjectIdentity((1,3,111,2,802,1,1,16,1,1))
_Ieee8021FqtssBapTable_Object=MibTable
ieee8021FqtssBapTable=_Ieee8021FqtssBapTable_Object((1,3,111,2,802,1,1,16,1,1,1))
if mibBuilder.loadTexts:ieee8021FqtssBapTable.setStatus(_A)
_Ieee8021FqtssBapEntry_Object=MibTableRow
ieee8021FqtssBapEntry=_Ieee8021FqtssBapEntry_Object((1,3,111,2,802,1,1,16,1,1,1,1))
ieee8021FqtssBapEntry.setIndexNames((0,_C,_D),(0,_C,_E),(0,_B,_N))
if mibBuilder.loadTexts:ieee8021FqtssBapEntry.setStatus(_A)
_Ieee8021FqtssBAPTrafficClass_Type=IEEE8021FqtssTrafficClassValue
_Ieee8021FqtssBAPTrafficClass_Object=MibTableColumn
ieee8021FqtssBAPTrafficClass=_Ieee8021FqtssBAPTrafficClass_Object((1,3,111,2,802,1,1,16,1,1,1,1,1),_Ieee8021FqtssBAPTrafficClass_Type())
ieee8021FqtssBAPTrafficClass.setMaxAccess(_J)
if mibBuilder.loadTexts:ieee8021FqtssBAPTrafficClass.setStatus(_A)
_Ieee8021FqtssDeltaBandwidth_Type=IEEE8021FqtssDeltaBandwidthValue
_Ieee8021FqtssDeltaBandwidth_Object=MibTableColumn
ieee8021FqtssDeltaBandwidth=_Ieee8021FqtssDeltaBandwidth_Object((1,3,111,2,802,1,1,16,1,1,1,1,2),_Ieee8021FqtssDeltaBandwidth_Type())
ieee8021FqtssDeltaBandwidth.setMaxAccess(_F)
if mibBuilder.loadTexts:ieee8021FqtssDeltaBandwidth.setStatus(_A)
if mibBuilder.loadTexts:ieee8021FqtssDeltaBandwidth.setUnits('percent')
_Ieee8021FqtssOperIdleSlopeMs_Type=Unsigned32
_Ieee8021FqtssOperIdleSlopeMs_Object=MibTableColumn
ieee8021FqtssOperIdleSlopeMs=_Ieee8021FqtssOperIdleSlopeMs_Object((1,3,111,2,802,1,1,16,1,1,1,1,3),_Ieee8021FqtssOperIdleSlopeMs_Type())
ieee8021FqtssOperIdleSlopeMs.setMaxAccess(_K)
if mibBuilder.loadTexts:ieee8021FqtssOperIdleSlopeMs.setStatus(_A)
if mibBuilder.loadTexts:ieee8021FqtssOperIdleSlopeMs.setUnits(_H)
_Ieee8021FqtssOperIdleSlopeLs_Type=Unsigned32
_Ieee8021FqtssOperIdleSlopeLs_Object=MibTableColumn
ieee8021FqtssOperIdleSlopeLs=_Ieee8021FqtssOperIdleSlopeLs_Object((1,3,111,2,802,1,1,16,1,1,1,1,4),_Ieee8021FqtssOperIdleSlopeLs_Type())
ieee8021FqtssOperIdleSlopeLs.setMaxAccess(_K)
if mibBuilder.loadTexts:ieee8021FqtssOperIdleSlopeLs.setStatus(_A)
if mibBuilder.loadTexts:ieee8021FqtssOperIdleSlopeLs.setUnits(_H)
class _Ieee8021FqtssAdminIdleSlopeMs_Type(Unsigned32):defaultValue=0
_Ieee8021FqtssAdminIdleSlopeMs_Type.__name__=_I
_Ieee8021FqtssAdminIdleSlopeMs_Object=MibTableColumn
ieee8021FqtssAdminIdleSlopeMs=_Ieee8021FqtssAdminIdleSlopeMs_Object((1,3,111,2,802,1,1,16,1,1,1,1,5),_Ieee8021FqtssAdminIdleSlopeMs_Type())
ieee8021FqtssAdminIdleSlopeMs.setMaxAccess(_F)
if mibBuilder.loadTexts:ieee8021FqtssAdminIdleSlopeMs.setStatus(_A)
if mibBuilder.loadTexts:ieee8021FqtssAdminIdleSlopeMs.setUnits(_H)
class _Ieee8021FqtssAdminIdleSlopeLs_Type(Unsigned32):defaultValue=0
_Ieee8021FqtssAdminIdleSlopeLs_Type.__name__=_I
_Ieee8021FqtssAdminIdleSlopeLs_Object=MibTableColumn
ieee8021FqtssAdminIdleSlopeLs=_Ieee8021FqtssAdminIdleSlopeLs_Object((1,3,111,2,802,1,1,16,1,1,1,1,6),_Ieee8021FqtssAdminIdleSlopeLs_Type())
ieee8021FqtssAdminIdleSlopeLs.setMaxAccess(_F)
if mibBuilder.loadTexts:ieee8021FqtssAdminIdleSlopeLs.setStatus(_A)
if mibBuilder.loadTexts:ieee8021FqtssAdminIdleSlopeLs.setUnits(_H)
_Ieee8021FqtssBapRowStatus_Type=RowStatus
_Ieee8021FqtssBapRowStatus_Object=MibTableColumn
ieee8021FqtssBapRowStatus=_Ieee8021FqtssBapRowStatus_Object((1,3,111,2,802,1,1,16,1,1,1,1,7),_Ieee8021FqtssBapRowStatus_Type())
ieee8021FqtssBapRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:ieee8021FqtssBapRowStatus.setStatus(_A)
_Ieee8021FqtssMappings_ObjectIdentity=ObjectIdentity
ieee8021FqtssMappings=_Ieee8021FqtssMappings_ObjectIdentity((1,3,111,2,802,1,1,16,1,2))
_Ieee8021FqtssTxSelectionAlgorithmTable_Object=MibTable
ieee8021FqtssTxSelectionAlgorithmTable=_Ieee8021FqtssTxSelectionAlgorithmTable_Object((1,3,111,2,802,1,1,16,1,2,1))
if mibBuilder.loadTexts:ieee8021FqtssTxSelectionAlgorithmTable.setStatus(_A)
_Ieee8021FqtssTxSelectionAlgorithmEntry_Object=MibTableRow
ieee8021FqtssTxSelectionAlgorithmEntry=_Ieee8021FqtssTxSelectionAlgorithmEntry_Object((1,3,111,2,802,1,1,16,1,2,1,1))
ieee8021FqtssTxSelectionAlgorithmEntry.setIndexNames((0,_C,_D),(0,_C,_E),(0,_B,_O))
if mibBuilder.loadTexts:ieee8021FqtssTxSelectionAlgorithmEntry.setStatus(_A)
_Ieee8021FqtssTrafficClass_Type=IEEE8021FqtssTrafficClassValue
_Ieee8021FqtssTrafficClass_Object=MibTableColumn
ieee8021FqtssTrafficClass=_Ieee8021FqtssTrafficClass_Object((1,3,111,2,802,1,1,16,1,2,1,1,1),_Ieee8021FqtssTrafficClass_Type())
ieee8021FqtssTrafficClass.setMaxAccess(_J)
if mibBuilder.loadTexts:ieee8021FqtssTrafficClass.setStatus(_A)
_Ieee8021FqtssTxSelectionAlgorithmID_Type=IEEE8021FqtssTxSelectionAlgorithmIDValue
_Ieee8021FqtssTxSelectionAlgorithmID_Object=MibTableColumn
ieee8021FqtssTxSelectionAlgorithmID=_Ieee8021FqtssTxSelectionAlgorithmID_Object((1,3,111,2,802,1,1,16,1,2,1,1,2),_Ieee8021FqtssTxSelectionAlgorithmID_Type())
ieee8021FqtssTxSelectionAlgorithmID.setMaxAccess(_F)
if mibBuilder.loadTexts:ieee8021FqtssTxSelectionAlgorithmID.setStatus(_A)
_Ieee8021FqtssSrpRegenOverrideTable_Object=MibTable
ieee8021FqtssSrpRegenOverrideTable=_Ieee8021FqtssSrpRegenOverrideTable_Object((1,3,111,2,802,1,1,16,1,2,2))
if mibBuilder.loadTexts:ieee8021FqtssSrpRegenOverrideTable.setStatus(_A)
_Ieee8021FqtssSrpRegenOverrideEntry_Object=MibTableRow
ieee8021FqtssSrpRegenOverrideEntry=_Ieee8021FqtssSrpRegenOverrideEntry_Object((1,3,111,2,802,1,1,16,1,2,2,1))
ieee8021FqtssSrpRegenOverrideEntry.setIndexNames((0,_C,_D),(0,_C,_E),(0,_B,_L))
if mibBuilder.loadTexts:ieee8021FqtssSrpRegenOverrideEntry.setStatus(_A)
_Ieee8021FqtssSrClassPriority_Type=IEEE8021PriorityValue
_Ieee8021FqtssSrClassPriority_Object=MibTableColumn
ieee8021FqtssSrClassPriority=_Ieee8021FqtssSrClassPriority_Object((1,3,111,2,802,1,1,16,1,2,2,1,1),_Ieee8021FqtssSrClassPriority_Type())
ieee8021FqtssSrClassPriority.setMaxAccess(_J)
if mibBuilder.loadTexts:ieee8021FqtssSrClassPriority.setStatus(_A)
_Ieee8021FqtssPriorityRegenOverride_Type=IEEE8021PriorityValue
_Ieee8021FqtssPriorityRegenOverride_Object=MibTableColumn
ieee8021FqtssPriorityRegenOverride=_Ieee8021FqtssPriorityRegenOverride_Object((1,3,111,2,802,1,1,16,1,2,2,1,2),_Ieee8021FqtssPriorityRegenOverride_Type())
ieee8021FqtssPriorityRegenOverride.setMaxAccess(_F)
if mibBuilder.loadTexts:ieee8021FqtssPriorityRegenOverride.setStatus(_A)
_Ieee8021FqtssSrpBoundaryPort_Type=TruthValue
_Ieee8021FqtssSrpBoundaryPort_Object=MibTableColumn
ieee8021FqtssSrpBoundaryPort=_Ieee8021FqtssSrpBoundaryPort_Object((1,3,111,2,802,1,1,16,1,2,2,1,3),_Ieee8021FqtssSrpBoundaryPort_Type())
ieee8021FqtssSrpBoundaryPort.setMaxAccess(_K)
if mibBuilder.loadTexts:ieee8021FqtssSrpBoundaryPort.setStatus(_A)
_Ieee8021FqtssSRClassToPriorityTable_Object=MibTable
ieee8021FqtssSRClassToPriorityTable=_Ieee8021FqtssSRClassToPriorityTable_Object((1,3,111,2,802,1,1,16,1,2,3))
if mibBuilder.loadTexts:ieee8021FqtssSRClassToPriorityTable.setStatus(_A)
_Ieee8021FqtssSRClassToPriorityEntry_Object=MibTableRow
ieee8021FqtssSRClassToPriorityEntry=_Ieee8021FqtssSRClassToPriorityEntry_Object((1,3,111,2,802,1,1,16,1,2,3,1))
ieee8021FqtssSRClassToPriorityEntry.setIndexNames((0,_C,_D),(0,_C,_E),(0,_B,_L))
if mibBuilder.loadTexts:ieee8021FqtssSRClassToPriorityEntry.setStatus(_A)
_Ieee8021FqtssSRClassToPrioritySrClassID_Type=IEEE8021FqtssTrafficClassValue
_Ieee8021FqtssSRClassToPrioritySrClassID_Object=MibTableColumn
ieee8021FqtssSRClassToPrioritySrClassID=_Ieee8021FqtssSRClassToPrioritySrClassID_Object((1,3,111,2,802,1,1,16,1,2,3,1,1),_Ieee8021FqtssSRClassToPrioritySrClassID_Type())
ieee8021FqtssSRClassToPrioritySrClassID.setMaxAccess(_G)
if mibBuilder.loadTexts:ieee8021FqtssSRClassToPrioritySrClassID.setStatus(_A)
_Ieee8021FqtssSRClassToPriorityRowStatus_Type=RowStatus
_Ieee8021FqtssSRClassToPriorityRowStatus_Object=MibTableColumn
ieee8021FqtssSRClassToPriorityRowStatus=_Ieee8021FqtssSRClassToPriorityRowStatus_Object((1,3,111,2,802,1,1,16,1,2,3,1,2),_Ieee8021FqtssSRClassToPriorityRowStatus_Type())
ieee8021FqtssSRClassToPriorityRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:ieee8021FqtssSRClassToPriorityRowStatus.setStatus(_A)
_Ieee8021FqtssBapX_ObjectIdentity=ObjectIdentity
ieee8021FqtssBapX=_Ieee8021FqtssBapX_ObjectIdentity((1,3,111,2,802,1,1,16,1,3))
_Ieee8021FqtssBapXTable_Object=MibTable
ieee8021FqtssBapXTable=_Ieee8021FqtssBapXTable_Object((1,3,111,2,802,1,1,16,1,3,1))
if mibBuilder.loadTexts:ieee8021FqtssBapXTable.setStatus(_A)
_Ieee8021FqtssBapXEntry_Object=MibTableRow
ieee8021FqtssBapXEntry=_Ieee8021FqtssBapXEntry_Object((1,3,111,2,802,1,1,16,1,3,1,1))
if mibBuilder.loadTexts:ieee8021FqtssBapXEntry.setStatus(_A)
_Ieee8021FqtssBAPClassMeasurementInterval_Type=Unsigned32
_Ieee8021FqtssBAPClassMeasurementInterval_Object=MibTableColumn
ieee8021FqtssBAPClassMeasurementInterval=_Ieee8021FqtssBAPClassMeasurementInterval_Object((1,3,111,2,802,1,1,16,1,3,1,1,1),_Ieee8021FqtssBAPClassMeasurementInterval_Type())
ieee8021FqtssBAPClassMeasurementInterval.setMaxAccess(_G)
if mibBuilder.loadTexts:ieee8021FqtssBAPClassMeasurementInterval.setStatus(_A)
class _Ieee8021FqtssBAPLockClassBandwidth_Type(TruthValue):defaultValue=2
_Ieee8021FqtssBAPLockClassBandwidth_Type.__name__=_M
_Ieee8021FqtssBAPLockClassBandwidth_Object=MibTableColumn
ieee8021FqtssBAPLockClassBandwidth=_Ieee8021FqtssBAPLockClassBandwidth_Object((1,3,111,2,802,1,1,16,1,3,1,1,2),_Ieee8021FqtssBAPLockClassBandwidth_Type())
ieee8021FqtssBAPLockClassBandwidth.setMaxAccess(_G)
if mibBuilder.loadTexts:ieee8021FqtssBAPLockClassBandwidth.setStatus(_A)
_Ieee8021FqtssConformance_ObjectIdentity=ObjectIdentity
ieee8021FqtssConformance=_Ieee8021FqtssConformance_ObjectIdentity((1,3,111,2,802,1,1,16,2))
_Ieee8021FqtssCompliances_ObjectIdentity=ObjectIdentity
ieee8021FqtssCompliances=_Ieee8021FqtssCompliances_ObjectIdentity((1,3,111,2,802,1,1,16,2,1))
_Ieee8021FqtssGroups_ObjectIdentity=ObjectIdentity
ieee8021FqtssGroups=_Ieee8021FqtssGroups_ObjectIdentity((1,3,111,2,802,1,1,16,2,2))
ieee8021FqtssBapEntry.registerAugmentions((_B,_P))
ieee8021FqtssBapXEntry.setIndexNames(*ieee8021FqtssBapEntry.getIndexNames())
ieee8021FqtssBapGroup=ObjectGroup((1,3,111,2,802,1,1,16,2,2,1))
ieee8021FqtssBapGroup.setObjects(*((_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V)))
if mibBuilder.loadTexts:ieee8021FqtssBapGroup.setStatus(_A)
ieee8021FqtssTxSelectionAlgorithmGroup=ObjectGroup((1,3,111,2,802,1,1,16,2,2,2))
ieee8021FqtssTxSelectionAlgorithmGroup.setObjects((_B,_W))
if mibBuilder.loadTexts:ieee8021FqtssTxSelectionAlgorithmGroup.setStatus(_A)
ieee8021FqtssBoundaryPortGroup=ObjectGroup((1,3,111,2,802,1,1,16,2,2,3))
ieee8021FqtssBoundaryPortGroup.setObjects(*((_B,_X),(_B,_Y)))
if mibBuilder.loadTexts:ieee8021FqtssBoundaryPortGroup.setStatus(_A)
ieee8021FqtssBapMeasurementGroup=ObjectGroup((1,3,111,2,802,1,1,16,2,2,4))
ieee8021FqtssBapMeasurementGroup.setObjects(*((_B,_Z),(_B,_a)))
if mibBuilder.loadTexts:ieee8021FqtssBapMeasurementGroup.setStatus(_A)
ieee8021FqtssSRClassPriorityGroup=ObjectGroup((1,3,111,2,802,1,1,16,2,2,5))
ieee8021FqtssSRClassPriorityGroup.setObjects(*((_B,_b),(_B,_c)))
if mibBuilder.loadTexts:ieee8021FqtssSRClassPriorityGroup.setStatus(_A)
ieee8021FqtssCompliance=ModuleCompliance((1,3,111,2,802,1,1,16,2,1,1))
ieee8021FqtssCompliance.setObjects(*((_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h)))
if mibBuilder.loadTexts:ieee8021FqtssCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'IEEE8021FqtssTrafficClassValue':IEEE8021FqtssTrafficClassValue,'IEEE8021FqtssDeltaBandwidthValue':IEEE8021FqtssDeltaBandwidthValue,'IEEE8021FqtssTxSelectionAlgorithmIDValue':IEEE8021FqtssTxSelectionAlgorithmIDValue,'ieee8021FqtssMib':ieee8021FqtssMib,'ieee8021FqtssNotifications':ieee8021FqtssNotifications,'ieee8021FqtssObjects':ieee8021FqtssObjects,'ieee8021FqtssBap':ieee8021FqtssBap,'ieee8021FqtssBapTable':ieee8021FqtssBapTable,'ieee8021FqtssBapEntry':ieee8021FqtssBapEntry,_N:ieee8021FqtssBAPTrafficClass,_Q:ieee8021FqtssDeltaBandwidth,_R:ieee8021FqtssOperIdleSlopeMs,_S:ieee8021FqtssOperIdleSlopeLs,_T:ieee8021FqtssAdminIdleSlopeMs,_U:ieee8021FqtssAdminIdleSlopeLs,_V:ieee8021FqtssBapRowStatus,'ieee8021FqtssMappings':ieee8021FqtssMappings,'ieee8021FqtssTxSelectionAlgorithmTable':ieee8021FqtssTxSelectionAlgorithmTable,'ieee8021FqtssTxSelectionAlgorithmEntry':ieee8021FqtssTxSelectionAlgorithmEntry,_O:ieee8021FqtssTrafficClass,_W:ieee8021FqtssTxSelectionAlgorithmID,'ieee8021FqtssSrpRegenOverrideTable':ieee8021FqtssSrpRegenOverrideTable,'ieee8021FqtssSrpRegenOverrideEntry':ieee8021FqtssSrpRegenOverrideEntry,_L:ieee8021FqtssSrClassPriority,_X:ieee8021FqtssPriorityRegenOverride,_Y:ieee8021FqtssSrpBoundaryPort,'ieee8021FqtssSRClassToPriorityTable':ieee8021FqtssSRClassToPriorityTable,'ieee8021FqtssSRClassToPriorityEntry':ieee8021FqtssSRClassToPriorityEntry,_b:ieee8021FqtssSRClassToPrioritySrClassID,_c:ieee8021FqtssSRClassToPriorityRowStatus,'ieee8021FqtssBapX':ieee8021FqtssBapX,'ieee8021FqtssBapXTable':ieee8021FqtssBapXTable,_P:ieee8021FqtssBapXEntry,_Z:ieee8021FqtssBAPClassMeasurementInterval,_a:ieee8021FqtssBAPLockClassBandwidth,'ieee8021FqtssConformance':ieee8021FqtssConformance,'ieee8021FqtssCompliances':ieee8021FqtssCompliances,'ieee8021FqtssCompliance':ieee8021FqtssCompliance,'ieee8021FqtssGroups':ieee8021FqtssGroups,_d:ieee8021FqtssBapGroup,_e:ieee8021FqtssTxSelectionAlgorithmGroup,_f:ieee8021FqtssBoundaryPortGroup,_g:ieee8021FqtssBapMeasurementGroup,_h:ieee8021FqtssSRClassPriorityGroup})