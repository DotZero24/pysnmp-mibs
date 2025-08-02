_b='coifccCcH2LAttenuation'
_a='coifccCcL2HAttenuation'
_Z='coifccCcRowStatus'
_Y='coifccCcH2LLastChange'
_X='coifccCcL2HLastChange'
_W='coifccCcH2LOperStatus'
_V='coifccCcL2HOperStatus'
_U='coifccCcCreationTime'
_T='coifccCcKind'
_S='coifccCcSwitchType'
_R='coifccCcLastChange'
_Q='coifccCcIndexNext'
_P='coifccIfCrossConnectIdentifier'
_O='1/10ths of dB'
_N='coifccCcHighIfIndex'
_M='coifccCcLowIfIndex'
_L='coifccCcIndex'
_K='unknown'
_J='ifIndex'
_I='IF-MIB'
_H='coifccCrossConnectGroup'
_G='coifccInterfaceGroup'
_F='not-accessible'
_E='read-create'
_D='read-only'
_C='Integer32'
_B='CISCO-OPTICAL-IF-CROSS-CONNECT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoExperiment,=mibBuilder.importSymbols('CISCO-SMI','ciscoExperiment')
InterfaceIndex,ifIndex=mibBuilder.importSymbols(_I,'InterfaceIndex',_J)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TimeStamp')
ciscoOpticalIfCrossConnectMIB=ModuleIdentity((1,3,6,1,4,1,9,10,68))
if mibBuilder.loadTexts:ciscoOpticalIfCrossConnectMIB.setRevisions(('2002-03-13 00:00','2001-04-20 00:00'))
class CoifccCrossConnectOperStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('up',1),('down',2),('dormant',3),(_K,4)))
_CoifccMIBObjects_ObjectIdentity=ObjectIdentity
coifccMIBObjects=_CoifccMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,10,68,1))
_CoifccInterface_ObjectIdentity=ObjectIdentity
coifccInterface=_CoifccInterface_ObjectIdentity((1,3,6,1,4,1,9,10,68,1,1))
_CoifccInterfaceTable_Object=MibTable
coifccInterfaceTable=_CoifccInterfaceTable_Object((1,3,6,1,4,1,9,10,68,1,1,1))
if mibBuilder.loadTexts:coifccInterfaceTable.setStatus(_A)
_CoifccInterfaceEntry_Object=MibTableRow
coifccInterfaceEntry=_CoifccInterfaceEntry_Object((1,3,6,1,4,1,9,10,68,1,1,1,1))
coifccInterfaceEntry.setIndexNames((0,_I,_J))
if mibBuilder.loadTexts:coifccInterfaceEntry.setStatus(_A)
class _CoifccIfCrossConnectIdentifier_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483547))
_CoifccIfCrossConnectIdentifier_Type.__name__=_C
_CoifccIfCrossConnectIdentifier_Object=MibTableColumn
coifccIfCrossConnectIdentifier=_CoifccIfCrossConnectIdentifier_Object((1,3,6,1,4,1,9,10,68,1,1,1,1,1),_CoifccIfCrossConnectIdentifier_Type())
coifccIfCrossConnectIdentifier.setMaxAccess(_D)
if mibBuilder.loadTexts:coifccIfCrossConnectIdentifier.setStatus(_A)
_CoifccCrossConnect_ObjectIdentity=ObjectIdentity
coifccCrossConnect=_CoifccCrossConnect_ObjectIdentity((1,3,6,1,4,1,9,10,68,1,2))
class _CoifccCcIndexNext_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CoifccCcIndexNext_Type.__name__=_C
_CoifccCcIndexNext_Object=MibScalar
coifccCcIndexNext=_CoifccCcIndexNext_Object((1,3,6,1,4,1,9,10,68,1,2,1),_CoifccCcIndexNext_Type())
coifccCcIndexNext.setMaxAccess(_D)
if mibBuilder.loadTexts:coifccCcIndexNext.setStatus(_A)
_CoifccCcLastChange_Type=TimeStamp
_CoifccCcLastChange_Object=MibScalar
coifccCcLastChange=_CoifccCcLastChange_Object((1,3,6,1,4,1,9,10,68,1,2,2),_CoifccCcLastChange_Type())
coifccCcLastChange.setMaxAccess(_D)
if mibBuilder.loadTexts:coifccCcLastChange.setStatus(_A)
_CoifccCrossConnectTable_Object=MibTable
coifccCrossConnectTable=_CoifccCrossConnectTable_Object((1,3,6,1,4,1,9,10,68,1,2,3))
if mibBuilder.loadTexts:coifccCrossConnectTable.setStatus(_A)
_CoifccCrossConnectEntry_Object=MibTableRow
coifccCrossConnectEntry=_CoifccCrossConnectEntry_Object((1,3,6,1,4,1,9,10,68,1,2,3,1))
coifccCrossConnectEntry.setIndexNames((0,_B,_L),(0,_B,_M),(0,_B,_N))
if mibBuilder.loadTexts:coifccCrossConnectEntry.setStatus(_A)
class _CoifccCcIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CoifccCcIndex_Type.__name__=_C
_CoifccCcIndex_Object=MibTableColumn
coifccCcIndex=_CoifccCcIndex_Object((1,3,6,1,4,1,9,10,68,1,2,3,1,1),_CoifccCcIndex_Type())
coifccCcIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:coifccCcIndex.setStatus(_A)
_CoifccCcLowIfIndex_Type=InterfaceIndex
_CoifccCcLowIfIndex_Object=MibTableColumn
coifccCcLowIfIndex=_CoifccCcLowIfIndex_Object((1,3,6,1,4,1,9,10,68,1,2,3,1,2),_CoifccCcLowIfIndex_Type())
coifccCcLowIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:coifccCcLowIfIndex.setStatus(_A)
_CoifccCcHighIfIndex_Type=InterfaceIndex
_CoifccCcHighIfIndex_Object=MibTableColumn
coifccCcHighIfIndex=_CoifccCcHighIfIndex_Object((1,3,6,1,4,1,9,10,68,1,2,3,1,3),_CoifccCcHighIfIndex_Type())
coifccCcHighIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:coifccCcHighIfIndex.setStatus(_A)
class _CoifccCcSwitchType_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_K,1),('electricalCrossConnect',2),('opticalCrossConnect',3),('autoSelect',4)))
_CoifccCcSwitchType_Type.__name__=_C
_CoifccCcSwitchType_Object=MibTableColumn
coifccCcSwitchType=_CoifccCcSwitchType_Object((1,3,6,1,4,1,9,10,68,1,2,3,1,4),_CoifccCcSwitchType_Type())
coifccCcSwitchType.setMaxAccess(_E)
if mibBuilder.loadTexts:coifccCcSwitchType.setStatus(_A)
class _CoifccCcKind_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('provisioned',1),('automatic',2),('dynamic',3),('protection',4),('other',5)))
_CoifccCcKind_Type.__name__=_C
_CoifccCcKind_Object=MibTableColumn
coifccCcKind=_CoifccCcKind_Object((1,3,6,1,4,1,9,10,68,1,2,3,1,5),_CoifccCcKind_Type())
coifccCcKind.setMaxAccess(_E)
if mibBuilder.loadTexts:coifccCcKind.setStatus(_A)
_CoifccCcCreationTime_Type=TimeStamp
_CoifccCcCreationTime_Object=MibTableColumn
coifccCcCreationTime=_CoifccCcCreationTime_Object((1,3,6,1,4,1,9,10,68,1,2,3,1,6),_CoifccCcCreationTime_Type())
coifccCcCreationTime.setMaxAccess(_D)
if mibBuilder.loadTexts:coifccCcCreationTime.setStatus(_A)
_CoifccCcL2HOperStatus_Type=CoifccCrossConnectOperStatus
_CoifccCcL2HOperStatus_Object=MibTableColumn
coifccCcL2HOperStatus=_CoifccCcL2HOperStatus_Object((1,3,6,1,4,1,9,10,68,1,2,3,1,7),_CoifccCcL2HOperStatus_Type())
coifccCcL2HOperStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:coifccCcL2HOperStatus.setStatus(_A)
_CoifccCcH2LOperStatus_Type=CoifccCrossConnectOperStatus
_CoifccCcH2LOperStatus_Object=MibTableColumn
coifccCcH2LOperStatus=_CoifccCcH2LOperStatus_Object((1,3,6,1,4,1,9,10,68,1,2,3,1,8),_CoifccCcH2LOperStatus_Type())
coifccCcH2LOperStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:coifccCcH2LOperStatus.setStatus(_A)
_CoifccCcL2HLastChange_Type=TimeStamp
_CoifccCcL2HLastChange_Object=MibTableColumn
coifccCcL2HLastChange=_CoifccCcL2HLastChange_Object((1,3,6,1,4,1,9,10,68,1,2,3,1,9),_CoifccCcL2HLastChange_Type())
coifccCcL2HLastChange.setMaxAccess(_D)
if mibBuilder.loadTexts:coifccCcL2HLastChange.setStatus(_A)
_CoifccCcH2LLastChange_Type=TimeStamp
_CoifccCcH2LLastChange_Object=MibTableColumn
coifccCcH2LLastChange=_CoifccCcH2LLastChange_Object((1,3,6,1,4,1,9,10,68,1,2,3,1,10),_CoifccCcH2LLastChange_Type())
coifccCcH2LLastChange.setMaxAccess(_D)
if mibBuilder.loadTexts:coifccCcH2LLastChange.setStatus(_A)
_CoifccCcRowStatus_Type=RowStatus
_CoifccCcRowStatus_Object=MibTableColumn
coifccCcRowStatus=_CoifccCcRowStatus_Object((1,3,6,1,4,1,9,10,68,1,2,3,1,11),_CoifccCcRowStatus_Type())
coifccCcRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:coifccCcRowStatus.setStatus(_A)
class _CoifccCcL2HAttenuation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-400,0))
_CoifccCcL2HAttenuation_Type.__name__=_C
_CoifccCcL2HAttenuation_Object=MibTableColumn
coifccCcL2HAttenuation=_CoifccCcL2HAttenuation_Object((1,3,6,1,4,1,9,10,68,1,2,3,1,12),_CoifccCcL2HAttenuation_Type())
coifccCcL2HAttenuation.setMaxAccess(_E)
if mibBuilder.loadTexts:coifccCcL2HAttenuation.setStatus(_A)
if mibBuilder.loadTexts:coifccCcL2HAttenuation.setUnits(_O)
class _CoifccCcH2LAttenuation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-400,0))
_CoifccCcH2LAttenuation_Type.__name__=_C
_CoifccCcH2LAttenuation_Object=MibTableColumn
coifccCcH2LAttenuation=_CoifccCcH2LAttenuation_Object((1,3,6,1,4,1,9,10,68,1,2,3,1,13),_CoifccCcH2LAttenuation_Type())
coifccCcH2LAttenuation.setMaxAccess(_E)
if mibBuilder.loadTexts:coifccCcH2LAttenuation.setStatus(_A)
if mibBuilder.loadTexts:coifccCcH2LAttenuation.setUnits(_O)
_CoifccMIBConformance_ObjectIdentity=ObjectIdentity
coifccMIBConformance=_CoifccMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,10,68,2))
_CoifccMIBCompliances_ObjectIdentity=ObjectIdentity
coifccMIBCompliances=_CoifccMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,10,68,2,1))
_CoifccMIBGroups_ObjectIdentity=ObjectIdentity
coifccMIBGroups=_CoifccMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,10,68,2,2))
coifccInterfaceGroup=ObjectGroup((1,3,6,1,4,1,9,10,68,2,2,1))
coifccInterfaceGroup.setObjects((_B,_P))
if mibBuilder.loadTexts:coifccInterfaceGroup.setStatus(_A)
coifccCrossConnectGroup=ObjectGroup((1,3,6,1,4,1,9,10,68,2,2,2))
coifccCrossConnectGroup.setObjects(*((_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z)))
if mibBuilder.loadTexts:coifccCrossConnectGroup.setStatus(_A)
coifccAttenuationGroup=ObjectGroup((1,3,6,1,4,1,9,10,68,2,2,3))
coifccAttenuationGroup.setObjects(*((_B,_a),(_B,_b)))
if mibBuilder.loadTexts:coifccAttenuationGroup.setStatus(_A)
coifccMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,10,68,2,1,1))
coifccMIBCompliance.setObjects(*((_B,_G),(_B,_H)))
if mibBuilder.loadTexts:coifccMIBCompliance.setStatus('deprecated')
coifccMIBComplianceRev1=ModuleCompliance((1,3,6,1,4,1,9,10,68,2,1,2))
coifccMIBComplianceRev1.setObjects(*((_B,_G),(_B,_H)))
if mibBuilder.loadTexts:coifccMIBComplianceRev1.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'CoifccCrossConnectOperStatus':CoifccCrossConnectOperStatus,'ciscoOpticalIfCrossConnectMIB':ciscoOpticalIfCrossConnectMIB,'coifccMIBObjects':coifccMIBObjects,'coifccInterface':coifccInterface,'coifccInterfaceTable':coifccInterfaceTable,'coifccInterfaceEntry':coifccInterfaceEntry,_P:coifccIfCrossConnectIdentifier,'coifccCrossConnect':coifccCrossConnect,_Q:coifccCcIndexNext,_R:coifccCcLastChange,'coifccCrossConnectTable':coifccCrossConnectTable,'coifccCrossConnectEntry':coifccCrossConnectEntry,_L:coifccCcIndex,_M:coifccCcLowIfIndex,_N:coifccCcHighIfIndex,_S:coifccCcSwitchType,_T:coifccCcKind,_U:coifccCcCreationTime,_V:coifccCcL2HOperStatus,_W:coifccCcH2LOperStatus,_X:coifccCcL2HLastChange,_Y:coifccCcH2LLastChange,_Z:coifccCcRowStatus,_a:coifccCcL2HAttenuation,_b:coifccCcH2LAttenuation,'coifccMIBConformance':coifccMIBConformance,'coifccMIBCompliances':coifccMIBCompliances,'coifccMIBCompliance':coifccMIBCompliance,'coifccMIBComplianceRev1':coifccMIBComplianceRev1,'coifccMIBGroups':coifccMIBGroups,_G:coifccInterfaceGroup,_H:coifccCrossConnectGroup,'coifccAttenuationGroup':coifccAttenuationGroup})