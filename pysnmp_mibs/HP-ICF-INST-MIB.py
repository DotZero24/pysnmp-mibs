_R='hpicfInstBaseGroup'
_Q='hpicfInstParamValMax'
_P='hpicfInstParamValMin'
_O='hpicfInstParameterValue'
_N='hpicfInstIntervalName'
_M='hpicfInstParameterName'
_L='hpicfInstMaxMemMB'
_K='hpicfInstEnable'
_J='hpicfInstIntervalIndex'
_I='hpicfInstInterfaceIndex'
_H='hpicfInstParameterIndex'
_G='TruthValue'
_F='not-accessible'
_E='DisplayString'
_D='Integer32'
_C='read-only'
_B='HP-ICF-INST-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpSwitch,=mibBuilder.importSymbols('HP-ICF-OID','hpSwitch')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','TextualConvention',_G)
hpicfInstMIB=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,5,1,45))
if mibBuilder.loadTexts:hpicfInstMIB.setRevisions(('2007-09-07 00:00',))
_HpicfInstObjects_ObjectIdentity=ObjectIdentity
hpicfInstObjects=_HpicfInstObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,45,1))
class _HpicfInstEnable_Type(TruthValue):defaultValue=1
_HpicfInstEnable_Type.__name__=_G
_HpicfInstEnable_Object=MibScalar
hpicfInstEnable=_HpicfInstEnable_Object((1,3,6,1,4,1,11,2,14,11,5,1,45,1,1),_HpicfInstEnable_Type())
hpicfInstEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfInstEnable.setStatus(_A)
class _HpicfInstMaxMemMB_Type(Integer32):defaultValue=2
_HpicfInstMaxMemMB_Type.__name__=_D
_HpicfInstMaxMemMB_Object=MibScalar
hpicfInstMaxMemMB=_HpicfInstMaxMemMB_Object((1,3,6,1,4,1,11,2,14,11,5,1,45,1,2),_HpicfInstMaxMemMB_Type())
hpicfInstMaxMemMB.setMaxAccess('read-write')
if mibBuilder.loadTexts:hpicfInstMaxMemMB.setStatus(_A)
_HpicfInstParameterTable_Object=MibTable
hpicfInstParameterTable=_HpicfInstParameterTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,45,1,3))
if mibBuilder.loadTexts:hpicfInstParameterTable.setStatus(_A)
_HpicfInstParameterEntry_Object=MibTableRow
hpicfInstParameterEntry=_HpicfInstParameterEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,45,1,3,1))
hpicfInstParameterEntry.setIndexNames((0,_B,_H),(0,_B,_I),(0,_B,_J))
if mibBuilder.loadTexts:hpicfInstParameterEntry.setStatus(_A)
class _HpicfInstParameterIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpicfInstParameterIndex_Type.__name__=_D
_HpicfInstParameterIndex_Object=MibTableColumn
hpicfInstParameterIndex=_HpicfInstParameterIndex_Object((1,3,6,1,4,1,11,2,14,11,5,1,45,1,3,1,1),_HpicfInstParameterIndex_Type())
hpicfInstParameterIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:hpicfInstParameterIndex.setStatus(_A)
class _HpicfInstInterfaceIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpicfInstInterfaceIndex_Type.__name__=_D
_HpicfInstInterfaceIndex_Object=MibTableColumn
hpicfInstInterfaceIndex=_HpicfInstInterfaceIndex_Object((1,3,6,1,4,1,11,2,14,11,5,1,45,1,3,1,2),_HpicfInstInterfaceIndex_Type())
hpicfInstInterfaceIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:hpicfInstInterfaceIndex.setStatus(_A)
class _HpicfInstIntervalIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpicfInstIntervalIndex_Type.__name__=_D
_HpicfInstIntervalIndex_Object=MibTableColumn
hpicfInstIntervalIndex=_HpicfInstIntervalIndex_Object((1,3,6,1,4,1,11,2,14,11,5,1,45,1,3,1,3),_HpicfInstIntervalIndex_Type())
hpicfInstIntervalIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:hpicfInstIntervalIndex.setStatus(_A)
class _HpicfInstParameterName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_HpicfInstParameterName_Type.__name__=_E
_HpicfInstParameterName_Object=MibTableColumn
hpicfInstParameterName=_HpicfInstParameterName_Object((1,3,6,1,4,1,11,2,14,11,5,1,45,1,3,1,4),_HpicfInstParameterName_Type())
hpicfInstParameterName.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfInstParameterName.setStatus(_A)
class _HpicfInstIntervalName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_HpicfInstIntervalName_Type.__name__=_E
_HpicfInstIntervalName_Object=MibTableColumn
hpicfInstIntervalName=_HpicfInstIntervalName_Object((1,3,6,1,4,1,11,2,14,11,5,1,45,1,3,1,5),_HpicfInstIntervalName_Type())
hpicfInstIntervalName.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfInstIntervalName.setStatus(_A)
_HpicfInstParameterValue_Type=Unsigned32
_HpicfInstParameterValue_Object=MibTableColumn
hpicfInstParameterValue=_HpicfInstParameterValue_Object((1,3,6,1,4,1,11,2,14,11,5,1,45,1,3,1,6),_HpicfInstParameterValue_Type())
hpicfInstParameterValue.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfInstParameterValue.setStatus(_A)
_HpicfInstParamValMin_Type=Unsigned32
_HpicfInstParamValMin_Object=MibTableColumn
hpicfInstParamValMin=_HpicfInstParamValMin_Object((1,3,6,1,4,1,11,2,14,11,5,1,45,1,3,1,7),_HpicfInstParamValMin_Type())
hpicfInstParamValMin.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfInstParamValMin.setStatus(_A)
_HpicfInstParamValMax_Type=Unsigned32
_HpicfInstParamValMax_Object=MibTableColumn
hpicfInstParamValMax=_HpicfInstParamValMax_Object((1,3,6,1,4,1,11,2,14,11,5,1,45,1,3,1,8),_HpicfInstParamValMax_Type())
hpicfInstParamValMax.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfInstParamValMax.setStatus(_A)
_HpicfInstConformance_ObjectIdentity=ObjectIdentity
hpicfInstConformance=_HpicfInstConformance_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,45,2))
_HpicfInstGroups_ObjectIdentity=ObjectIdentity
hpicfInstGroups=_HpicfInstGroups_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,45,2,1))
_HpicfInstCompliances_ObjectIdentity=ObjectIdentity
hpicfInstCompliances=_HpicfInstCompliances_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,45,2,2))
hpicfInstBaseGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,45,2,1,2))
hpicfInstBaseGroup.setObjects(*((_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:hpicfInstBaseGroup.setStatus(_A)
hpicfInstBaseCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,45,2,2,1))
hpicfInstBaseCompliance.setObjects((_B,_R))
if mibBuilder.loadTexts:hpicfInstBaseCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'hpicfInstMIB':hpicfInstMIB,'hpicfInstObjects':hpicfInstObjects,_K:hpicfInstEnable,_L:hpicfInstMaxMemMB,'hpicfInstParameterTable':hpicfInstParameterTable,'hpicfInstParameterEntry':hpicfInstParameterEntry,_H:hpicfInstParameterIndex,_I:hpicfInstInterfaceIndex,_J:hpicfInstIntervalIndex,_M:hpicfInstParameterName,_N:hpicfInstIntervalName,_O:hpicfInstParameterValue,_P:hpicfInstParamValMin,_Q:hpicfInstParamValMax,'hpicfInstConformance':hpicfInstConformance,'hpicfInstGroups':hpicfInstGroups,_R:hpicfInstBaseGroup,'hpicfInstCompliances':hpicfInstCompliances,'hpicfInstBaseCompliance':hpicfInstBaseCompliance})