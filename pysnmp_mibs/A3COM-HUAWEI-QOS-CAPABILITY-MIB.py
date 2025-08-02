_G='h3cQoSCharacteristicsIndex'
_F='h3cQoSModuleIndex'
_E='h3cQoSCapabilityPhysicalIndex'
_D='h3cQoSCapabilityPhysicalType'
_C='not-accessible'
_B='A3COM-HUAWEI-QOS-CAPABILITY-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cSNMPAgCpb,=mibBuilder.importSymbols('A3COM-HUAWEI-OID-MIB','h3cSNMPAgCpb')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
h3cQosCapability=ModuleIdentity((1,3,6,1,4,1,43,45,1,10,7,1))
class CapabilityPhysicalType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('stack',1),('chassis',2),('module',3),('port',4)))
_H3cQoSCapabilityMibObjects_ObjectIdentity=ObjectIdentity
h3cQoSCapabilityMibObjects=_H3cQoSCapabilityMibObjects_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,7,1,1))
_H3cQoSCapabilityGroup_ObjectIdentity=ObjectIdentity
h3cQoSCapabilityGroup=_H3cQoSCapabilityGroup_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,7,1,1,1))
_H3cQoSCapabilityTable_Object=MibTable
h3cQoSCapabilityTable=_H3cQoSCapabilityTable_Object((1,3,6,1,4,1,43,45,1,10,7,1,1,1,1))
if mibBuilder.loadTexts:h3cQoSCapabilityTable.setStatus(_A)
_H3cQoSCapabilityEntry_Object=MibTableRow
h3cQoSCapabilityEntry=_H3cQoSCapabilityEntry_Object((1,3,6,1,4,1,43,45,1,10,7,1,1,1,1,1))
h3cQoSCapabilityEntry.setIndexNames((0,_B,_D),(0,_B,_E),(0,_B,_F),(0,_B,_G))
if mibBuilder.loadTexts:h3cQoSCapabilityEntry.setStatus(_A)
_H3cQoSCapabilityPhysicalType_Type=CapabilityPhysicalType
_H3cQoSCapabilityPhysicalType_Object=MibTableColumn
h3cQoSCapabilityPhysicalType=_H3cQoSCapabilityPhysicalType_Object((1,3,6,1,4,1,43,45,1,10,7,1,1,1,1,1,1),_H3cQoSCapabilityPhysicalType_Type())
h3cQoSCapabilityPhysicalType.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cQoSCapabilityPhysicalType.setStatus(_A)
_H3cQoSCapabilityPhysicalIndex_Type=Integer32
_H3cQoSCapabilityPhysicalIndex_Object=MibTableColumn
h3cQoSCapabilityPhysicalIndex=_H3cQoSCapabilityPhysicalIndex_Object((1,3,6,1,4,1,43,45,1,10,7,1,1,1,1,1,2),_H3cQoSCapabilityPhysicalIndex_Type())
h3cQoSCapabilityPhysicalIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cQoSCapabilityPhysicalIndex.setStatus(_A)
_H3cQoSModuleIndex_Type=Integer32
_H3cQoSModuleIndex_Object=MibTableColumn
h3cQoSModuleIndex=_H3cQoSModuleIndex_Object((1,3,6,1,4,1,43,45,1,10,7,1,1,1,1,1,3),_H3cQoSModuleIndex_Type())
h3cQoSModuleIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cQoSModuleIndex.setStatus(_A)
_H3cQoSCharacteristicsIndex_Type=Integer32
_H3cQoSCharacteristicsIndex_Object=MibTableColumn
h3cQoSCharacteristicsIndex=_H3cQoSCharacteristicsIndex_Object((1,3,6,1,4,1,43,45,1,10,7,1,1,1,1,1,4),_H3cQoSCharacteristicsIndex_Type())
h3cQoSCharacteristicsIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cQoSCharacteristicsIndex.setStatus(_A)
_H3cQoSCharacteristicsValue_Type=Unsigned32
_H3cQoSCharacteristicsValue_Object=MibTableColumn
h3cQoSCharacteristicsValue=_H3cQoSCharacteristicsValue_Object((1,3,6,1,4,1,43,45,1,10,7,1,1,1,1,1,5),_H3cQoSCharacteristicsValue_Type())
h3cQoSCharacteristicsValue.setMaxAccess('read-only')
if mibBuilder.loadTexts:h3cQoSCharacteristicsValue.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'CapabilityPhysicalType':CapabilityPhysicalType,'h3cQosCapability':h3cQosCapability,'h3cQoSCapabilityMibObjects':h3cQoSCapabilityMibObjects,'h3cQoSCapabilityGroup':h3cQoSCapabilityGroup,'h3cQoSCapabilityTable':h3cQoSCapabilityTable,'h3cQoSCapabilityEntry':h3cQoSCapabilityEntry,_D:h3cQoSCapabilityPhysicalType,_E:h3cQoSCapabilityPhysicalIndex,_F:h3cQoSModuleIndex,_G:h3cQoSCharacteristicsIndex,'h3cQoSCharacteristicsValue':h3cQoSCharacteristicsValue})