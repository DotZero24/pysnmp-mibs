_N='h3cQoSIfCapCharacteristicsIndex'
_M='h3cQoSIfCapModuleIndex'
_L='h3cQoSIfCapIfIndex'
_K='h3cQoSSysCapCharacteristicsIndex'
_J='h3cQoSSysCapModuleIndex'
_I='h3cQoSCharacteristicsIndex'
_H='h3cQoSModuleIndex'
_G='h3cQoSCapabilityPhysicalIndex'
_F='h3cQoSCapabilityPhysicalType'
_E='read-only'
_D='Integer32'
_C='not-accessible'
_B='H3C-QOS-CAPABILITY-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cSNMPAgCpb,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','h3cSNMPAgCpb')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
h3cQosCapability=ModuleIdentity((1,3,6,1,4,1,2011,10,7,1))
if mibBuilder.loadTexts:h3cQosCapability.setRevisions(('2016-10-25 00:00','2014-10-28 00:00'))
class CapabilityPhysicalType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('stack',1),('chassis',2),('module',3),('port',4)))
_H3cQoSCapabilityMibObjects_ObjectIdentity=ObjectIdentity
h3cQoSCapabilityMibObjects=_H3cQoSCapabilityMibObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,7,1,1))
_H3cQoSCapabilityGroup_ObjectIdentity=ObjectIdentity
h3cQoSCapabilityGroup=_H3cQoSCapabilityGroup_ObjectIdentity((1,3,6,1,4,1,2011,10,7,1,1,1))
_H3cQoSCapabilityTable_Object=MibTable
h3cQoSCapabilityTable=_H3cQoSCapabilityTable_Object((1,3,6,1,4,1,2011,10,7,1,1,1,1))
if mibBuilder.loadTexts:h3cQoSCapabilityTable.setStatus(_A)
_H3cQoSCapabilityEntry_Object=MibTableRow
h3cQoSCapabilityEntry=_H3cQoSCapabilityEntry_Object((1,3,6,1,4,1,2011,10,7,1,1,1,1,1))
h3cQoSCapabilityEntry.setIndexNames((0,_B,_F),(0,_B,_G),(0,_B,_H),(0,_B,_I))
if mibBuilder.loadTexts:h3cQoSCapabilityEntry.setStatus(_A)
_H3cQoSCapabilityPhysicalType_Type=CapabilityPhysicalType
_H3cQoSCapabilityPhysicalType_Object=MibTableColumn
h3cQoSCapabilityPhysicalType=_H3cQoSCapabilityPhysicalType_Object((1,3,6,1,4,1,2011,10,7,1,1,1,1,1,1),_H3cQoSCapabilityPhysicalType_Type())
h3cQoSCapabilityPhysicalType.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cQoSCapabilityPhysicalType.setStatus(_A)
_H3cQoSCapabilityPhysicalIndex_Type=Integer32
_H3cQoSCapabilityPhysicalIndex_Object=MibTableColumn
h3cQoSCapabilityPhysicalIndex=_H3cQoSCapabilityPhysicalIndex_Object((1,3,6,1,4,1,2011,10,7,1,1,1,1,1,2),_H3cQoSCapabilityPhysicalIndex_Type())
h3cQoSCapabilityPhysicalIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cQoSCapabilityPhysicalIndex.setStatus(_A)
_H3cQoSModuleIndex_Type=Integer32
_H3cQoSModuleIndex_Object=MibTableColumn
h3cQoSModuleIndex=_H3cQoSModuleIndex_Object((1,3,6,1,4,1,2011,10,7,1,1,1,1,1,3),_H3cQoSModuleIndex_Type())
h3cQoSModuleIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cQoSModuleIndex.setStatus(_A)
_H3cQoSCharacteristicsIndex_Type=Integer32
_H3cQoSCharacteristicsIndex_Object=MibTableColumn
h3cQoSCharacteristicsIndex=_H3cQoSCharacteristicsIndex_Object((1,3,6,1,4,1,2011,10,7,1,1,1,1,1,4),_H3cQoSCharacteristicsIndex_Type())
h3cQoSCharacteristicsIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cQoSCharacteristicsIndex.setStatus(_A)
_H3cQoSCharacteristicsValue_Type=Unsigned32
_H3cQoSCharacteristicsValue_Object=MibTableColumn
h3cQoSCharacteristicsValue=_H3cQoSCharacteristicsValue_Object((1,3,6,1,4,1,2011,10,7,1,1,1,1,1,5),_H3cQoSCharacteristicsValue_Type())
h3cQoSCharacteristicsValue.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cQoSCharacteristicsValue.setStatus(_A)
_H3cQoSSysCapabilityTable_Object=MibTable
h3cQoSSysCapabilityTable=_H3cQoSSysCapabilityTable_Object((1,3,6,1,4,1,2011,10,7,1,1,1,2))
if mibBuilder.loadTexts:h3cQoSSysCapabilityTable.setStatus(_A)
_H3cQoSSysCapabilityEntry_Object=MibTableRow
h3cQoSSysCapabilityEntry=_H3cQoSSysCapabilityEntry_Object((1,3,6,1,4,1,2011,10,7,1,1,1,2,1))
h3cQoSSysCapabilityEntry.setIndexNames((0,_B,_J),(0,_B,_K))
if mibBuilder.loadTexts:h3cQoSSysCapabilityEntry.setStatus(_A)
class _H3cQoSSysCapModuleIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_H3cQoSSysCapModuleIndex_Type.__name__=_D
_H3cQoSSysCapModuleIndex_Object=MibTableColumn
h3cQoSSysCapModuleIndex=_H3cQoSSysCapModuleIndex_Object((1,3,6,1,4,1,2011,10,7,1,1,1,2,1,1),_H3cQoSSysCapModuleIndex_Type())
h3cQoSSysCapModuleIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cQoSSysCapModuleIndex.setStatus(_A)
class _H3cQoSSysCapCharacteristicsIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_H3cQoSSysCapCharacteristicsIndex_Type.__name__=_D
_H3cQoSSysCapCharacteristicsIndex_Object=MibTableColumn
h3cQoSSysCapCharacteristicsIndex=_H3cQoSSysCapCharacteristicsIndex_Object((1,3,6,1,4,1,2011,10,7,1,1,1,2,1,2),_H3cQoSSysCapCharacteristicsIndex_Type())
h3cQoSSysCapCharacteristicsIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cQoSSysCapCharacteristicsIndex.setStatus(_A)
_H3cQoSSysCapCharacteristicsValue_Type=Unsigned32
_H3cQoSSysCapCharacteristicsValue_Object=MibTableColumn
h3cQoSSysCapCharacteristicsValue=_H3cQoSSysCapCharacteristicsValue_Object((1,3,6,1,4,1,2011,10,7,1,1,1,2,1,3),_H3cQoSSysCapCharacteristicsValue_Type())
h3cQoSSysCapCharacteristicsValue.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cQoSSysCapCharacteristicsValue.setStatus(_A)
_H3cQoSIfCapabilityTable_Object=MibTable
h3cQoSIfCapabilityTable=_H3cQoSIfCapabilityTable_Object((1,3,6,1,4,1,2011,10,7,1,1,1,3))
if mibBuilder.loadTexts:h3cQoSIfCapabilityTable.setStatus(_A)
_H3cQoSIfCapabilityEntry_Object=MibTableRow
h3cQoSIfCapabilityEntry=_H3cQoSIfCapabilityEntry_Object((1,3,6,1,4,1,2011,10,7,1,1,1,3,1))
h3cQoSIfCapabilityEntry.setIndexNames((0,_B,_L),(0,_B,_M),(0,_B,_N))
if mibBuilder.loadTexts:h3cQoSIfCapabilityEntry.setStatus(_A)
class _H3cQoSIfCapIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_H3cQoSIfCapIfIndex_Type.__name__=_D
_H3cQoSIfCapIfIndex_Object=MibTableColumn
h3cQoSIfCapIfIndex=_H3cQoSIfCapIfIndex_Object((1,3,6,1,4,1,2011,10,7,1,1,1,3,1,1),_H3cQoSIfCapIfIndex_Type())
h3cQoSIfCapIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cQoSIfCapIfIndex.setStatus(_A)
class _H3cQoSIfCapModuleIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_H3cQoSIfCapModuleIndex_Type.__name__=_D
_H3cQoSIfCapModuleIndex_Object=MibTableColumn
h3cQoSIfCapModuleIndex=_H3cQoSIfCapModuleIndex_Object((1,3,6,1,4,1,2011,10,7,1,1,1,3,1,2),_H3cQoSIfCapModuleIndex_Type())
h3cQoSIfCapModuleIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cQoSIfCapModuleIndex.setStatus(_A)
class _H3cQoSIfCapCharacteristicsIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_H3cQoSIfCapCharacteristicsIndex_Type.__name__=_D
_H3cQoSIfCapCharacteristicsIndex_Object=MibTableColumn
h3cQoSIfCapCharacteristicsIndex=_H3cQoSIfCapCharacteristicsIndex_Object((1,3,6,1,4,1,2011,10,7,1,1,1,3,1,3),_H3cQoSIfCapCharacteristicsIndex_Type())
h3cQoSIfCapCharacteristicsIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cQoSIfCapCharacteristicsIndex.setStatus(_A)
_H3cQoSIfCapCharacteristicsValue_Type=Unsigned32
_H3cQoSIfCapCharacteristicsValue_Object=MibTableColumn
h3cQoSIfCapCharacteristicsValue=_H3cQoSIfCapCharacteristicsValue_Object((1,3,6,1,4,1,2011,10,7,1,1,1,3,1,4),_H3cQoSIfCapCharacteristicsValue_Type())
h3cQoSIfCapCharacteristicsValue.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cQoSIfCapCharacteristicsValue.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'CapabilityPhysicalType':CapabilityPhysicalType,'h3cQosCapability':h3cQosCapability,'h3cQoSCapabilityMibObjects':h3cQoSCapabilityMibObjects,'h3cQoSCapabilityGroup':h3cQoSCapabilityGroup,'h3cQoSCapabilityTable':h3cQoSCapabilityTable,'h3cQoSCapabilityEntry':h3cQoSCapabilityEntry,_F:h3cQoSCapabilityPhysicalType,_G:h3cQoSCapabilityPhysicalIndex,_H:h3cQoSModuleIndex,_I:h3cQoSCharacteristicsIndex,'h3cQoSCharacteristicsValue':h3cQoSCharacteristicsValue,'h3cQoSSysCapabilityTable':h3cQoSSysCapabilityTable,'h3cQoSSysCapabilityEntry':h3cQoSSysCapabilityEntry,_J:h3cQoSSysCapModuleIndex,_K:h3cQoSSysCapCharacteristicsIndex,'h3cQoSSysCapCharacteristicsValue':h3cQoSSysCapCharacteristicsValue,'h3cQoSIfCapabilityTable':h3cQoSIfCapabilityTable,'h3cQoSIfCapabilityEntry':h3cQoSIfCapabilityEntry,_L:h3cQoSIfCapIfIndex,_M:h3cQoSIfCapModuleIndex,_N:h3cQoSIfCapCharacteristicsIndex,'h3cQoSIfCapCharacteristicsValue':h3cQoSIfCapCharacteristicsValue})