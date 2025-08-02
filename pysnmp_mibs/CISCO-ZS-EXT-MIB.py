_V='ciscoZsExtConfigGroupSup1'
_U='czseGlobalPropagationMode'
_T='czseGlobalDefaultZoneBehaviour'
_S='czseMergeControlRestrict'
_R='czseSessionCntlResult'
_Q='czseSessionCntl'
_P='czseSessionOwner'
_O='czseSessionOwnerType'
_N='czseReadFrom'
_M='czseOperationModeResult'
_L='czseOperationMode'
_K='czseCapabilityObject'
_J='inProgress'
_I='OctetString'
_H='ciscoZsExtConfigGroup'
_G='read-only'
_F='vsanIndex'
_E='CISCO-VSAN-MIB'
_D='read-write'
_C='Integer32'
_B='CISCO-ZS-EXT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_I,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
vsanIndex,=mibBuilder.importSymbols(_E,_F)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoZsExtMIB=ModuleIdentity((1,3,6,1,4,1,9,9,427))
if mibBuilder.loadTexts:ciscoZsExtMIB.setRevisions(('2006-01-03 00:00','2004-08-11 00:00'))
class CzseSessOwnerType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('other',1),('cli',2),('gs4client',3),('snmp',4)))
_CiscoZsExtMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoZsExtMIBNotifs=_CiscoZsExtMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,427,0))
_CiscoZsExtMIBObjects_ObjectIdentity=ObjectIdentity
ciscoZsExtMIBObjects=_CiscoZsExtMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,427,1))
_CzseConfiguration_ObjectIdentity=ObjectIdentity
czseConfiguration=_CzseConfiguration_ObjectIdentity((1,3,6,1,4,1,9,9,427,1,1))
_CzseCapabilityTable_Object=MibTable
czseCapabilityTable=_CzseCapabilityTable_Object((1,3,6,1,4,1,9,9,427,1,1,1))
if mibBuilder.loadTexts:czseCapabilityTable.setStatus(_A)
_CzseCapabilityEntry_Object=MibTableRow
czseCapabilityEntry=_CzseCapabilityEntry_Object((1,3,6,1,4,1,9,9,427,1,1,1,1))
czseCapabilityEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:czseCapabilityEntry.setStatus(_A)
class _CzseCapabilityObject_Type(Bits):namedValues=NamedValues(*(('enhancedMode',0),('zsetDb',1),('dirAct',2),('hardZoning',3)))
_CzseCapabilityObject_Type.__name__='Bits'
_CzseCapabilityObject_Object=MibTableColumn
czseCapabilityObject=_CzseCapabilityObject_Object((1,3,6,1,4,1,9,9,427,1,1,1,1,1),_CzseCapabilityObject_Type())
czseCapabilityObject.setMaxAccess(_G)
if mibBuilder.loadTexts:czseCapabilityObject.setStatus(_A)
_CzseModeTable_Object=MibTable
czseModeTable=_CzseModeTable_Object((1,3,6,1,4,1,9,9,427,1,1,2))
if mibBuilder.loadTexts:czseModeTable.setStatus(_A)
_CzseModeEntry_Object=MibTableRow
czseModeEntry=_CzseModeEntry_Object((1,3,6,1,4,1,9,9,427,1,1,2,1))
czseModeEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:czseModeEntry.setStatus(_A)
class _CzseOperationMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('basic',1),('enhanced',2)))
_CzseOperationMode_Type.__name__=_C
_CzseOperationMode_Object=MibTableColumn
czseOperationMode=_CzseOperationMode_Object((1,3,6,1,4,1,9,9,427,1,1,2,1,1),_CzseOperationMode_Type())
czseOperationMode.setMaxAccess(_D)
if mibBuilder.loadTexts:czseOperationMode.setStatus(_A)
class _CzseOperationModeResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('success',1),('failure',2),(_J,3)))
_CzseOperationModeResult_Type.__name__=_C
_CzseOperationModeResult_Object=MibTableColumn
czseOperationModeResult=_CzseOperationModeResult_Object((1,3,6,1,4,1,9,9,427,1,1,2,1,2),_CzseOperationModeResult_Type())
czseOperationModeResult.setMaxAccess(_G)
if mibBuilder.loadTexts:czseOperationModeResult.setStatus(_A)
class _CzseReadFrom_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('effectiveDB',1),('copyDB',2)))
_CzseReadFrom_Type.__name__=_C
_CzseReadFrom_Object=MibScalar
czseReadFrom=_CzseReadFrom_Object((1,3,6,1,4,1,9,9,427,1,1,3),_CzseReadFrom_Type())
czseReadFrom.setMaxAccess(_D)
if mibBuilder.loadTexts:czseReadFrom.setStatus(_A)
_CzseSessionTable_Object=MibTable
czseSessionTable=_CzseSessionTable_Object((1,3,6,1,4,1,9,9,427,1,1,4))
if mibBuilder.loadTexts:czseSessionTable.setStatus(_A)
_CzseSessionEntry_Object=MibTableRow
czseSessionEntry=_CzseSessionEntry_Object((1,3,6,1,4,1,9,9,427,1,1,4,1))
czseSessionEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:czseSessionEntry.setStatus(_A)
_CzseSessionOwnerType_Type=CzseSessOwnerType
_CzseSessionOwnerType_Object=MibTableColumn
czseSessionOwnerType=_CzseSessionOwnerType_Object((1,3,6,1,4,1,9,9,427,1,1,4,1,1),_CzseSessionOwnerType_Type())
czseSessionOwnerType.setMaxAccess(_G)
if mibBuilder.loadTexts:czseSessionOwnerType.setStatus(_A)
class _CzseSessionOwner_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CzseSessionOwner_Type.__name__=_I
_CzseSessionOwner_Object=MibTableColumn
czseSessionOwner=_CzseSessionOwner_Object((1,3,6,1,4,1,9,9,427,1,1,4,1,2),_CzseSessionOwner_Type())
czseSessionOwner.setMaxAccess(_G)
if mibBuilder.loadTexts:czseSessionOwner.setStatus(_A)
class _CzseSessionCntl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('commitChanges',1),('cleanup',2),('noop',3)))
_CzseSessionCntl_Type.__name__=_C
_CzseSessionCntl_Object=MibTableColumn
czseSessionCntl=_CzseSessionCntl_Object((1,3,6,1,4,1,9,9,427,1,1,4,1,3),_CzseSessionCntl_Type())
czseSessionCntl.setMaxAccess(_D)
if mibBuilder.loadTexts:czseSessionCntl.setStatus(_A)
class _CzseSessionCntlResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('commitSuccess',1),('commitFailure',2),(_J,3)))
_CzseSessionCntlResult_Type.__name__=_C
_CzseSessionCntlResult_Object=MibTableColumn
czseSessionCntlResult=_CzseSessionCntlResult_Object((1,3,6,1,4,1,9,9,427,1,1,4,1,4),_CzseSessionCntlResult_Type())
czseSessionCntlResult.setMaxAccess(_G)
if mibBuilder.loadTexts:czseSessionCntlResult.setStatus(_A)
_CzseMergeControlTable_Object=MibTable
czseMergeControlTable=_CzseMergeControlTable_Object((1,3,6,1,4,1,9,9,427,1,1,5))
if mibBuilder.loadTexts:czseMergeControlTable.setStatus(_A)
_CzseMergeControlEntry_Object=MibTableRow
czseMergeControlEntry=_CzseMergeControlEntry_Object((1,3,6,1,4,1,9,9,427,1,1,5,1))
czseMergeControlEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:czseMergeControlEntry.setStatus(_A)
class _CzseMergeControlRestrict_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('allow',1),('restrict',2)))
_CzseMergeControlRestrict_Type.__name__=_C
_CzseMergeControlRestrict_Object=MibTableColumn
czseMergeControlRestrict=_CzseMergeControlRestrict_Object((1,3,6,1,4,1,9,9,427,1,1,5,1,1),_CzseMergeControlRestrict_Type())
czseMergeControlRestrict.setMaxAccess(_D)
if mibBuilder.loadTexts:czseMergeControlRestrict.setStatus(_A)
class _CzseGlobalDefaultZoneBehaviour_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('permit',1),('deny',2)))
_CzseGlobalDefaultZoneBehaviour_Type.__name__=_C
_CzseGlobalDefaultZoneBehaviour_Object=MibScalar
czseGlobalDefaultZoneBehaviour=_CzseGlobalDefaultZoneBehaviour_Object((1,3,6,1,4,1,9,9,427,1,1,6),_CzseGlobalDefaultZoneBehaviour_Type())
czseGlobalDefaultZoneBehaviour.setMaxAccess(_D)
if mibBuilder.loadTexts:czseGlobalDefaultZoneBehaviour.setStatus(_A)
class _CzseGlobalPropagationMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('fullZoneset',1),('activeZoneset',2)))
_CzseGlobalPropagationMode_Type.__name__=_C
_CzseGlobalPropagationMode_Object=MibScalar
czseGlobalPropagationMode=_CzseGlobalPropagationMode_Object((1,3,6,1,4,1,9,9,427,1,1,7),_CzseGlobalPropagationMode_Type())
czseGlobalPropagationMode.setMaxAccess(_D)
if mibBuilder.loadTexts:czseGlobalPropagationMode.setStatus(_A)
_CzseStats_ObjectIdentity=ObjectIdentity
czseStats=_CzseStats_ObjectIdentity((1,3,6,1,4,1,9,9,427,1,2))
_CiscoZsExtMIBConform_ObjectIdentity=ObjectIdentity
ciscoZsExtMIBConform=_CiscoZsExtMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,427,2))
_CiscoZsExtMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoZsExtMIBCompliances=_CiscoZsExtMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,427,2,1))
_CiscoZsExtMIBGroups_ObjectIdentity=ObjectIdentity
ciscoZsExtMIBGroups=_CiscoZsExtMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,427,2,2))
ciscoZsExtConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,427,2,2,1))
ciscoZsExtConfigGroup.setObjects(*((_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S)))
if mibBuilder.loadTexts:ciscoZsExtConfigGroup.setStatus(_A)
ciscoZsExtConfigGroupSup1=ObjectGroup((1,3,6,1,4,1,9,9,427,2,2,2))
ciscoZsExtConfigGroupSup1.setObjects(*((_B,_T),(_B,_U)))
if mibBuilder.loadTexts:ciscoZsExtConfigGroupSup1.setStatus(_A)
ciscoZsExtMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,427,2,1,1))
ciscoZsExtMIBCompliance.setObjects((_B,_H))
if mibBuilder.loadTexts:ciscoZsExtMIBCompliance.setStatus('deprecated')
ciscoZsExtMIBComplianceRev1=ModuleCompliance((1,3,6,1,4,1,9,9,427,2,1,2))
ciscoZsExtMIBComplianceRev1.setObjects(*((_B,_H),(_B,_V)))
if mibBuilder.loadTexts:ciscoZsExtMIBComplianceRev1.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'CzseSessOwnerType':CzseSessOwnerType,'ciscoZsExtMIB':ciscoZsExtMIB,'ciscoZsExtMIBNotifs':ciscoZsExtMIBNotifs,'ciscoZsExtMIBObjects':ciscoZsExtMIBObjects,'czseConfiguration':czseConfiguration,'czseCapabilityTable':czseCapabilityTable,'czseCapabilityEntry':czseCapabilityEntry,_K:czseCapabilityObject,'czseModeTable':czseModeTable,'czseModeEntry':czseModeEntry,_L:czseOperationMode,_M:czseOperationModeResult,_N:czseReadFrom,'czseSessionTable':czseSessionTable,'czseSessionEntry':czseSessionEntry,_O:czseSessionOwnerType,_P:czseSessionOwner,_Q:czseSessionCntl,_R:czseSessionCntlResult,'czseMergeControlTable':czseMergeControlTable,'czseMergeControlEntry':czseMergeControlEntry,_S:czseMergeControlRestrict,_T:czseGlobalDefaultZoneBehaviour,_U:czseGlobalPropagationMode,'czseStats':czseStats,'ciscoZsExtMIBConform':ciscoZsExtMIBConform,'ciscoZsExtMIBCompliances':ciscoZsExtMIBCompliances,'ciscoZsExtMIBCompliance':ciscoZsExtMIBCompliance,'ciscoZsExtMIBComplianceRev1':ciscoZsExtMIBComplianceRev1,'ciscoZsExtMIBGroups':ciscoZsExtMIBGroups,_H:ciscoZsExtConfigGroup,_V:ciscoZsExtConfigGroupSup1})