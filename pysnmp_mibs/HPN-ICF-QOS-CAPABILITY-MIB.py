_N='hpnicfQoSIfCapCharacteristicsIndex'
_M='hpnicfQoSIfCapModuleIndex'
_L='hpnicfQoSIfCapIfIndex'
_K='hpnicfQoSSysCapCharacteristicsIndex'
_J='hpnicfQoSSysCapModuleIndex'
_I='hpnicfQoSCharacteristicsIndex'
_H='hpnicfQoSModuleIndex'
_G='hpnicfQoSCapabilityPhysicalIndex'
_F='hpnicfQoSCapabilityPhysicalType'
_E='read-only'
_D='Integer32'
_C='not-accessible'
_B='HPN-ICF-QOS-CAPABILITY-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfSNMPAgCpb,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfSNMPAgCpb')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
hpnicfQosCapability=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,7,1))
class CapabilityPhysicalType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('stack',1),('chassis',2),('module',3),('port',4)))
_HpnicfQoSCapabilityMibObjects_ObjectIdentity=ObjectIdentity
hpnicfQoSCapabilityMibObjects=_HpnicfQoSCapabilityMibObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,7,1,1))
_HpnicfQoSCapabilityGroup_ObjectIdentity=ObjectIdentity
hpnicfQoSCapabilityGroup=_HpnicfQoSCapabilityGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,7,1,1,1))
_HpnicfQoSCapabilityTable_Object=MibTable
hpnicfQoSCapabilityTable=_HpnicfQoSCapabilityTable_Object((1,3,6,1,4,1,11,2,14,11,15,7,1,1,1,1))
if mibBuilder.loadTexts:hpnicfQoSCapabilityTable.setStatus(_A)
_HpnicfQoSCapabilityEntry_Object=MibTableRow
hpnicfQoSCapabilityEntry=_HpnicfQoSCapabilityEntry_Object((1,3,6,1,4,1,11,2,14,11,15,7,1,1,1,1,1))
hpnicfQoSCapabilityEntry.setIndexNames((0,_B,_F),(0,_B,_G),(0,_B,_H),(0,_B,_I))
if mibBuilder.loadTexts:hpnicfQoSCapabilityEntry.setStatus(_A)
_HpnicfQoSCapabilityPhysicalType_Type=CapabilityPhysicalType
_HpnicfQoSCapabilityPhysicalType_Object=MibTableColumn
hpnicfQoSCapabilityPhysicalType=_HpnicfQoSCapabilityPhysicalType_Object((1,3,6,1,4,1,11,2,14,11,15,7,1,1,1,1,1,1),_HpnicfQoSCapabilityPhysicalType_Type())
hpnicfQoSCapabilityPhysicalType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfQoSCapabilityPhysicalType.setStatus(_A)
_HpnicfQoSCapabilityPhysicalIndex_Type=Integer32
_HpnicfQoSCapabilityPhysicalIndex_Object=MibTableColumn
hpnicfQoSCapabilityPhysicalIndex=_HpnicfQoSCapabilityPhysicalIndex_Object((1,3,6,1,4,1,11,2,14,11,15,7,1,1,1,1,1,2),_HpnicfQoSCapabilityPhysicalIndex_Type())
hpnicfQoSCapabilityPhysicalIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfQoSCapabilityPhysicalIndex.setStatus(_A)
_HpnicfQoSModuleIndex_Type=Integer32
_HpnicfQoSModuleIndex_Object=MibTableColumn
hpnicfQoSModuleIndex=_HpnicfQoSModuleIndex_Object((1,3,6,1,4,1,11,2,14,11,15,7,1,1,1,1,1,3),_HpnicfQoSModuleIndex_Type())
hpnicfQoSModuleIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfQoSModuleIndex.setStatus(_A)
_HpnicfQoSCharacteristicsIndex_Type=Integer32
_HpnicfQoSCharacteristicsIndex_Object=MibTableColumn
hpnicfQoSCharacteristicsIndex=_HpnicfQoSCharacteristicsIndex_Object((1,3,6,1,4,1,11,2,14,11,15,7,1,1,1,1,1,4),_HpnicfQoSCharacteristicsIndex_Type())
hpnicfQoSCharacteristicsIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfQoSCharacteristicsIndex.setStatus(_A)
_HpnicfQoSCharacteristicsValue_Type=Unsigned32
_HpnicfQoSCharacteristicsValue_Object=MibTableColumn
hpnicfQoSCharacteristicsValue=_HpnicfQoSCharacteristicsValue_Object((1,3,6,1,4,1,11,2,14,11,15,7,1,1,1,1,1,5),_HpnicfQoSCharacteristicsValue_Type())
hpnicfQoSCharacteristicsValue.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfQoSCharacteristicsValue.setStatus(_A)
_HpnicfQoSSysCapabilityTable_Object=MibTable
hpnicfQoSSysCapabilityTable=_HpnicfQoSSysCapabilityTable_Object((1,3,6,1,4,1,11,2,14,11,15,7,1,1,1,2))
if mibBuilder.loadTexts:hpnicfQoSSysCapabilityTable.setStatus(_A)
_HpnicfQoSSysCapabilityEntry_Object=MibTableRow
hpnicfQoSSysCapabilityEntry=_HpnicfQoSSysCapabilityEntry_Object((1,3,6,1,4,1,11,2,14,11,15,7,1,1,1,2,1))
hpnicfQoSSysCapabilityEntry.setIndexNames((0,_B,_J),(0,_B,_K))
if mibBuilder.loadTexts:hpnicfQoSSysCapabilityEntry.setStatus(_A)
class _HpnicfQoSSysCapModuleIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HpnicfQoSSysCapModuleIndex_Type.__name__=_D
_HpnicfQoSSysCapModuleIndex_Object=MibTableColumn
hpnicfQoSSysCapModuleIndex=_HpnicfQoSSysCapModuleIndex_Object((1,3,6,1,4,1,11,2,14,11,15,7,1,1,1,2,1,1),_HpnicfQoSSysCapModuleIndex_Type())
hpnicfQoSSysCapModuleIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfQoSSysCapModuleIndex.setStatus(_A)
class _HpnicfQoSSysCapCharacteristicsIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HpnicfQoSSysCapCharacteristicsIndex_Type.__name__=_D
_HpnicfQoSSysCapCharacteristicsIndex_Object=MibTableColumn
hpnicfQoSSysCapCharacteristicsIndex=_HpnicfQoSSysCapCharacteristicsIndex_Object((1,3,6,1,4,1,11,2,14,11,15,7,1,1,1,2,1,2),_HpnicfQoSSysCapCharacteristicsIndex_Type())
hpnicfQoSSysCapCharacteristicsIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfQoSSysCapCharacteristicsIndex.setStatus(_A)
_HpnicfQoSSysCapCharacteristicsValue_Type=Unsigned32
_HpnicfQoSSysCapCharacteristicsValue_Object=MibTableColumn
hpnicfQoSSysCapCharacteristicsValue=_HpnicfQoSSysCapCharacteristicsValue_Object((1,3,6,1,4,1,11,2,14,11,15,7,1,1,1,2,1,3),_HpnicfQoSSysCapCharacteristicsValue_Type())
hpnicfQoSSysCapCharacteristicsValue.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfQoSSysCapCharacteristicsValue.setStatus(_A)
_HpnicfQoSIfCapabilityTable_Object=MibTable
hpnicfQoSIfCapabilityTable=_HpnicfQoSIfCapabilityTable_Object((1,3,6,1,4,1,11,2,14,11,15,7,1,1,1,3))
if mibBuilder.loadTexts:hpnicfQoSIfCapabilityTable.setStatus(_A)
_HpnicfQoSIfCapabilityEntry_Object=MibTableRow
hpnicfQoSIfCapabilityEntry=_HpnicfQoSIfCapabilityEntry_Object((1,3,6,1,4,1,11,2,14,11,15,7,1,1,1,3,1))
hpnicfQoSIfCapabilityEntry.setIndexNames((0,_B,_L),(0,_B,_M),(0,_B,_N))
if mibBuilder.loadTexts:hpnicfQoSIfCapabilityEntry.setStatus(_A)
class _HpnicfQoSIfCapIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_HpnicfQoSIfCapIfIndex_Type.__name__=_D
_HpnicfQoSIfCapIfIndex_Object=MibTableColumn
hpnicfQoSIfCapIfIndex=_HpnicfQoSIfCapIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,7,1,1,1,3,1,1),_HpnicfQoSIfCapIfIndex_Type())
hpnicfQoSIfCapIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfQoSIfCapIfIndex.setStatus(_A)
class _HpnicfQoSIfCapModuleIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HpnicfQoSIfCapModuleIndex_Type.__name__=_D
_HpnicfQoSIfCapModuleIndex_Object=MibTableColumn
hpnicfQoSIfCapModuleIndex=_HpnicfQoSIfCapModuleIndex_Object((1,3,6,1,4,1,11,2,14,11,15,7,1,1,1,3,1,2),_HpnicfQoSIfCapModuleIndex_Type())
hpnicfQoSIfCapModuleIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfQoSIfCapModuleIndex.setStatus(_A)
class _HpnicfQoSIfCapCharacteristicsIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HpnicfQoSIfCapCharacteristicsIndex_Type.__name__=_D
_HpnicfQoSIfCapCharacteristicsIndex_Object=MibTableColumn
hpnicfQoSIfCapCharacteristicsIndex=_HpnicfQoSIfCapCharacteristicsIndex_Object((1,3,6,1,4,1,11,2,14,11,15,7,1,1,1,3,1,3),_HpnicfQoSIfCapCharacteristicsIndex_Type())
hpnicfQoSIfCapCharacteristicsIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfQoSIfCapCharacteristicsIndex.setStatus(_A)
_HpnicfQoSIfCapCharacteristicsValue_Type=Unsigned32
_HpnicfQoSIfCapCharacteristicsValue_Object=MibTableColumn
hpnicfQoSIfCapCharacteristicsValue=_HpnicfQoSIfCapCharacteristicsValue_Object((1,3,6,1,4,1,11,2,14,11,15,7,1,1,1,3,1,4),_HpnicfQoSIfCapCharacteristicsValue_Type())
hpnicfQoSIfCapCharacteristicsValue.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfQoSIfCapCharacteristicsValue.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'CapabilityPhysicalType':CapabilityPhysicalType,'hpnicfQosCapability':hpnicfQosCapability,'hpnicfQoSCapabilityMibObjects':hpnicfQoSCapabilityMibObjects,'hpnicfQoSCapabilityGroup':hpnicfQoSCapabilityGroup,'hpnicfQoSCapabilityTable':hpnicfQoSCapabilityTable,'hpnicfQoSCapabilityEntry':hpnicfQoSCapabilityEntry,_F:hpnicfQoSCapabilityPhysicalType,_G:hpnicfQoSCapabilityPhysicalIndex,_H:hpnicfQoSModuleIndex,_I:hpnicfQoSCharacteristicsIndex,'hpnicfQoSCharacteristicsValue':hpnicfQoSCharacteristicsValue,'hpnicfQoSSysCapabilityTable':hpnicfQoSSysCapabilityTable,'hpnicfQoSSysCapabilityEntry':hpnicfQoSSysCapabilityEntry,_J:hpnicfQoSSysCapModuleIndex,_K:hpnicfQoSSysCapCharacteristicsIndex,'hpnicfQoSSysCapCharacteristicsValue':hpnicfQoSSysCapCharacteristicsValue,'hpnicfQoSIfCapabilityTable':hpnicfQoSIfCapabilityTable,'hpnicfQoSIfCapabilityEntry':hpnicfQoSIfCapabilityEntry,_L:hpnicfQoSIfCapIfIndex,_M:hpnicfQoSIfCapModuleIndex,_N:hpnicfQoSIfCapCharacteristicsIndex,'hpnicfQoSIfCapCharacteristicsValue':hpnicfQoSIfCapCharacteristicsValue})